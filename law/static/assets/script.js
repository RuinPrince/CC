// desktop three bar link
function scrollToheader(sectionId) {
const section = document.getElementById(sectionId);
const offset = 50; // Adjust this value to scroll slightly lower
const sectionPosition = section.getBoundingClientRect().top + window.scrollY;

window.scrollTo({
    top: sectionPosition - offset,
    behavior: "smooth"
});
}

document.addEventListener("scroll", function() {
  const scrollBtn = document.querySelector(".scroll-to-top");
  if (!scrollBtn) return;
  // Show button after scrolling 300px, hide when at top
  if (window.scrollY > 300) {
      scrollBtn.classList.add("visible");
  } else {
      scrollBtn.classList.remove("visible");
  }
});

// Smooth scroll to top
const scrollTopBtn = document.querySelector(".scroll-to-top");
if (scrollTopBtn) {
  scrollTopBtn.addEventListener("click", function(e) {
    e.preventDefault();
    window.scrollTo({
        top: 0,
        behavior: "smooth"
    });
  });
}


// ==========================================
// DARK MODE THEME TOGGLE
// ==========================================
document.addEventListener('DOMContentLoaded', () => {
  const themeToggle = document.getElementById('theme-toggle');
  if (themeToggle) {
    // Check local storage for theme preference
    if (localStorage.getItem('theme') === 'dark') {
      document.body.classList.add('dark-mode');
      themeToggle.innerHTML = '<i class="bi bi-sun-fill fs-5 text-warning"></i>';
    }

    themeToggle.addEventListener('click', () => {
      document.body.classList.toggle('dark-mode');
      if (document.body.classList.contains('dark-mode')) {
        localStorage.setItem('theme', 'dark');
        themeToggle.innerHTML = '<i class="bi bi-sun-fill fs-5 text-warning"></i>';
      } else {
        localStorage.setItem('theme', 'light');
        themeToggle.innerHTML = '<i class="bi bi-moon-fill fs-5"></i>';
      }
    });
  }
});

// ==========================================
// FLOATING ASK AI INTERACTION (PREMIUM SAAS)
// ==========================================
document.addEventListener('DOMContentLoaded', () => {
  // Inject floating elements
  const floatBtn = document.createElement('button');
  floatBtn.className = 'ask-ai-floating-btn';
  floatBtn.innerHTML = '<i class="bi bi-chat-dots-fill"></i>';
  document.body.appendChild(floatBtn);

  const chatWindow = document.createElement('div');
  chatWindow.className = 'ask-ai-chat-window shadow-lg';
  chatWindow.innerHTML = `
    <div class="chat-header d-flex justify-content-between align-items-center">
      <div>
        <h5 class="m-0 fw-bold d-flex align-items-center gap-2">
          <i class="bi bi-robot fs-4"></i> Civic AI
        </h5>
        <small class="text-white-50">Your intelligent legal assistant</small>
      </div>
      <div class="d-flex gap-2">
        <button class="btn btn-link text-white p-0 shadow-none" id="toggle-chat-settings" title="AI Settings"><i class="bi bi-gear-fill fs-5"></i></button>
        <button class="btn btn-link text-white p-0 shadow-none" id="close-chat"><i class="bi bi-x-lg fs-5"></i></button>
      </div>
    </div>
    <div class="bg-light p-3 border-bottom d-none text-dark" id="chat-settings-panel">
      <label class="form-label small fw-bold text-muted mb-1" style="font-size: 0.75rem;">HUGGING FACE API TOKEN (100% Free)</label>
      <div class="input-group input-group-sm">
        <input type="password" id="hf-token-input" class="form-control" placeholder="Paste hf_token here...">
        <button class="btn btn-primary btn-sm" id="save-hf-token">Save</button>
      </div>
      <small class="text-muted d-block mt-1" style="font-size: 0.7rem; line-height: 1;">Create a free account on huggingface.co to get a token. No credit cards needed!</small>
    </div>
    <div class="chat-body" id="chat-messages-container">
      <div class="chat-message bot">
        <p class="m-0">👋 Hello! I am your AI Legal Assistant.</p>
        <p class="m-0 mt-2">I can help you search the Indian Penal Code, explain complex sections, or summarize amendments.</p>
      </div>
    </div>
    <div class="chat-footer">
      <div class="chat-input-group">
        <input type="text" id="chat-input" placeholder="Ask a legal question...">
        <button id="chat-send"><i class="bi bi-send-fill"></i></button>
      </div>
      <div class="text-center mt-2">
        <small class="text-muted" style="font-size: 0.7rem;">AI generated content may be inaccurate.</small>
      </div>
    </div>
  `;
  document.body.appendChild(chatWindow);

  floatBtn.addEventListener('click', () => {
    const isVisible = chatWindow.style.display === 'flex';
    chatWindow.style.display = isVisible ? 'none' : 'flex';
    if (!isVisible) document.getElementById('chat-input').focus();
  });

  document.getElementById('close-chat').addEventListener('click', () => {
    chatWindow.style.display = 'none';
  });

  // Settings Panel Logic
  const settingsBtn = document.getElementById('toggle-chat-settings');
  const settingsPanel = document.getElementById('chat-settings-panel');
  const tokenInput = document.getElementById('hf-token-input');
  const saveTokenBtn = document.getElementById('save-hf-token');

  // Load saved token on load
  const savedToken = localStorage.getItem('hf_token') || '';
  tokenInput.value = savedToken;

  settingsBtn.addEventListener('click', () => {
    settingsPanel.classList.toggle('d-none');
  });

  saveTokenBtn.addEventListener('click', () => {
    const token = tokenInput.value.trim();
    localStorage.setItem('hf_token', token);
    showToast(token ? 'Hugging Face API token saved!' : 'Token cleared.');
    settingsPanel.classList.add('d-none');
  });

  const chatInput = document.getElementById('chat-input');
  const chatSend = document.getElementById('chat-send');
  const chatMessages = document.getElementById('chat-messages-container');

  // Simple markdown renderer for AI responses
  function renderMarkdown(text) {
    let html = text.replace(/\*\*(.*?)\*\*/g, '<strong>$1</strong>');
    html = html.replace(/\*(.*?)\*/g, '<em>$1</em>');
    html = html.replace(/\n/g, '<br>');
    return html;
  }

  function sendMessage() {
    const query = chatInput.value.trim();
    if (!query) return;

    // Append user message
    const userMsg = document.createElement('div');
    userMsg.className = 'chat-message user animate-fade-in';
    userMsg.textContent = query;
    chatMessages.appendChild(userMsg);
    chatInput.value = '';
    chatMessages.scrollTop = chatMessages.scrollHeight;

    // Loading indicator
    const botLoading = document.createElement('div');
    botLoading.className = 'chat-message bot animate-fade-in';
    botLoading.innerHTML = `
      <div class="typing-indicator">
        <div class="typing-dot"></div>
        <div class="typing-dot"></div>
        <div class="typing-dot"></div>
      </div>
    `;
    chatMessages.appendChild(botLoading);
    chatMessages.scrollTop = chatMessages.scrollHeight;

    const userToken = localStorage.getItem('hf_token') || '';

    // Call backend API (which tries Ollama first, then HF if token provided)
    fetch('/api/ai/chat/', {
      method: 'POST',
      headers: {
        'Content-Type': 'application/json',
        'X-CSRFToken': window.csrfToken
      },
      body: JSON.stringify({ query: query, hf_token: userToken })
    })
    .then(res => res.json())
    .then(data => {
      botLoading.remove();
      const botMsg = document.createElement('div');

      if (data.error) {
        // Backend couldn't answer — try client-side HF fallback
        if (userToken) {
          clientSideHFFallback(query, userToken, botLoading, botMsg);
          return;
        }
        botMsg.className = 'chat-message bot animate-fade-in border-warning border';
        botMsg.innerHTML = renderMarkdown(
          "⚠️ **AI is currently offline.**\n\nI apologize, but the server is currently unable to process requests."
        );
      } else {
        botMsg.className = 'chat-message bot animate-fade-in';
        botMsg.innerHTML = renderMarkdown(data.answer || 'Sorry, I encountered an error while processing that request.');
      }

      chatMessages.appendChild(botMsg);
      chatMessages.scrollTop = chatMessages.scrollHeight;
    })
    .catch(() => {
      // Network error — try client-side HF fallback
      if (userToken) {
        clientSideHFFallback(query, userToken, botLoading);
        return;
      }

      botLoading.remove();
      const botMsg = document.createElement('div');
      botMsg.className = 'chat-message bot animate-fade-in border-warning border';
      botMsg.innerHTML = renderMarkdown(
        "⚠️ **Could not connect to the server.**\n\nPlease check your internet connection and try again."
      );
      chatMessages.appendChild(botMsg);
      chatMessages.scrollTop = chatMessages.scrollHeight;
    });
  }

  function clientSideHFFallback(query, token, loadingEl) {
    // Direct client-side Hugging Face call as ultimate fallback
    fetch('https://router.huggingface.co/v1/chat/completions', {
      method: 'POST',
      headers: {
        'Authorization': `Bearer ${token}`,
        'Content-Type': 'application/json'
      },
      body: JSON.stringify({
        model: 'Qwen/Qwen2.5-72B-Instruct',
        messages: [
          { role: 'system', content: 'You are a helpful Legal Assistant for Indian Law. Explain clearly and concisely.' },
          { role: 'user', content: query }
        ],
        max_tokens: 500
      })
    })
    .then(res => {
      if (!res.ok) throw new Error('HF API Failed');
      return res.json();
    })
    .then(data => {
      if (loadingEl && loadingEl.parentNode) loadingEl.remove();
      const botMsg = document.createElement('div');
      botMsg.className = 'chat-message bot animate-fade-in';
      const answer = data.choices[0].message.content;
      botMsg.innerHTML = renderMarkdown(answer || 'Sorry, I encountered an error while processing that request.');
      chatMessages.appendChild(botMsg);
      chatMessages.scrollTop = chatMessages.scrollHeight;
    })
    .catch((err) => {
      if (loadingEl && loadingEl.parentNode) loadingEl.remove();
      const botMsg = document.createElement('div');
      botMsg.className = 'chat-message bot animate-fade-in border-danger border';
      botMsg.innerHTML = `<span class="text-danger"><i class="bi bi-exclamation-triangle-fill"></i> Failed to connect to Hugging Face Cloud. Please make sure your token is valid: ${err.message}</span>`;
      chatMessages.appendChild(botMsg);
    });
  }

  chatSend.addEventListener('click', sendMessage);
  chatInput.addEventListener('keypress', (e) => {
    if (e.key === 'Enter') sendMessage();
  });
});

// ==========================================
// LAW DETAIL INTERACTIVE FUNCTIONS
// ==========================================
document.addEventListener('DOMContentLoaded', () => {
  // 1. Citation Generator Modal (Bug 1 fix: capture originalHtml)
  const citeModal = document.getElementById('citationModal') ? new bootstrap.Modal(document.getElementById('citationModal')) : null;
  document.querySelectorAll('.generate-citation-btn').forEach(btn => {
    btn.addEventListener('click', () => {
      const section = btn.getAttribute('data-section');
      const title = btn.getAttribute('data-title');
      const originalHtml = btn.innerHTML; // Bug 1 fix: capture BEFORE changing

      btn.innerHTML = '<i class="bi bi-arrow-repeat text-muted me-2" style="animation: spin 1s linear infinite;"></i> <span class="d-none d-md-inline">Generating...</span>';
      btn.disabled = true;

      fetch(`/api/utils/citation/?law=${encodeURIComponent(title)}&section=${section}&year=2025`)
        .then(res => res.json())
        .then(data => {
          document.getElementById('cite-apa').value = data.APA;
          document.getElementById('cite-mla').value = data.MLA;
          document.getElementById('cite-bluebook').value = data.Bluebook;
          document.getElementById('cite-indian').value = data.Indian;
          citeModal.show();
        })
        .catch(() => showToast('Failed to generate citation', true))
        .finally(() => {
          btn.innerHTML = originalHtml;
          btn.disabled = false;
        });
    });
  });

  // Copy citation buttons
  document.querySelectorAll('.copy-cite-btn').forEach(btn => {
    btn.addEventListener('click', () => {
      const targetId = btn.getAttribute('data-target');
      const input = document.getElementById(targetId);
      navigator.clipboard.writeText(input.value).then(() => {
        showToast('Citation copied to clipboard!');
      }).catch(() => {
        // Fallback for older browsers
        input.select();
        document.execCommand('copy');
        showToast('Citation copied to clipboard!');
      });
    });
  });

  // 2. PDF Download
  document.querySelectorAll('.download-pdf-btn').forEach(btn => {
    btn.addEventListener('click', () => {
      const title = btn.getAttribute('data-title');
      const desc = btn.getAttribute('data-desc');

      // Use POST for long content to avoid URL length limits (Bug 20 fix)
      fetch('/api/utils/pdf/', {
        method: 'POST',
        headers: {
          'Content-Type': 'application/json',
          'X-CSRFToken': window.csrfToken
        },
        body: JSON.stringify({ law: title, content: desc })
      })
      .then(res => {
        if (!res.ok) throw new Error('PDF generation failed');
        return res.blob();
      })
      .then(blob => {
        const url = URL.createObjectURL(blob);
        const a = document.createElement('a');
        a.href = url;
        a.download = `${title}.pdf`;
        a.click();
        URL.revokeObjectURL(url);
        showToast('PDF downloaded!');
      })
      .catch(() => showToast('Failed to generate PDF', true));
    });
  });

  // 3. Bookmark Saving/Removal
  document.querySelectorAll('.bookmark-btn').forEach(btn => {
    const section = btn.getAttribute('data-section');
    const table = btn.getAttribute('data-table');

    btn.addEventListener('click', () => {
      const isBookmarked = btn.classList.contains('active');
      if (!isBookmarked) {
        fetch('/api/bookmarks/items/', {
          method: 'POST',
          headers: {
            'Content-Type': 'application/json',
            'X-CSRFToken': window.csrfToken
          },
          body: JSON.stringify({
            title: `${table.toUpperCase()} Section ${section}`,
            law_table: table,
            section_id: section
          })
        })
        .then(res => res.json())
        .then(() => {
          btn.classList.add('active', 'btn-primary');
          btn.innerHTML = '<i class="bi bi-bookmark-fill me-2"></i> Bookmarked';
          showToast('Section saved to bookmarks!');
        })
        .catch(() => showToast('Failed to bookmark', true));
      } else {
        showToast('Already bookmarked! Visit Bookmarks to manage folders.');
      }
    });
  });

  // 4. Notes Autosave (Bug 6 fix: update existing notes via PATCH instead of always POSTing)
  document.querySelectorAll('.notes-textarea').forEach(textarea => {
    const section = textarea.getAttribute('data-section');
    const table = textarea.getAttribute('data-table');
    const statusContainer = textarea.closest('.card-premium') || textarea.parentElement;
    const status = statusContainer ? statusContainer.querySelector('.notes-status') : null;

    let existingNoteId = null;

    // Load initial note
    fetch(`/api/notes/items/`, {
      headers: { 'X-CSRFToken': window.csrfToken }
    })
    .then(res => res.json())
    .then(notes => {
      if (!Array.isArray(notes)) return;
      const existing = notes.find(n => n.section_id == section && n.law_table == table);
      if (existing) {
        textarea.value = existing.content;
        existingNoteId = existing.id;
      }
    })
    .catch(() => {});

    // Autosave logic (Debounced) — uses PATCH for existing, POST for new
    let timeout = null;
    textarea.addEventListener('input', () => {
      if (status) status.textContent = 'Saving...';
      clearTimeout(timeout);
      timeout = setTimeout(() => {
        const url = existingNoteId ? `/api/notes/items/${existingNoteId}/` : '/api/notes/items/';
        const method = existingNoteId ? 'PATCH' : 'POST';

        fetch(url, {
          method: method,
          headers: {
            'Content-Type': 'application/json',
            'X-CSRFToken': window.csrfToken
          },
          body: JSON.stringify({
            law_table: table,
            section_id: section,
            content: textarea.value
          })
        })
        .then(res => res.json())
        .then(data => {
          if (data.id) existingNoteId = data.id; // Save ID for future PATCHes
          if (status) status.innerHTML = '<i class="bi bi-check2-circle text-success me-1"></i> Saved';
        })
        .catch(() => {
          if (status) status.textContent = 'Autosave failed.';
        });
      }, 1000);
    });
  });
});

// ==========================================
// SMART SEMANTIC SEARCH AUTOCOMPLETE
// ==========================================
document.addEventListener('DOMContentLoaded', () => {
  const searchInput = document.getElementById('smart-search-input');
  const dropdown = document.getElementById('search-autocomplete-dropdown');

  if (searchInput && dropdown) {
    let debounceTimeout = null;

    searchInput.addEventListener('input', () => {
      const query = searchInput.value.trim();
      clearTimeout(debounceTimeout);

      if (query.length < 3) {
        dropdown.style.display = 'none';
        return;
      }

      debounceTimeout = setTimeout(() => {
        fetch('/api/ai/search/', {
          method: 'POST',
          headers: {
            'Content-Type': 'application/json',
            'X-CSRFToken': window.csrfToken
          },
          body: JSON.stringify({ query })
        })
        .then(res => res.json())
        .then(data => {
          const results = data.results || [];
          dropdown.innerHTML = '';
          
          if (results.length === 0) {
            dropdown.innerHTML = '<p class="text-muted small text-center m-0 py-2">No matching laws found.</p>';
            dropdown.style.display = 'block';
            return;
          }

          results.slice(0, 5).forEach(res => {
            const act = res.metadata.act;
            const secId = res.metadata.section_id;
            const title = res.metadata.title || 'Section Reference';
            
            const link = document.createElement('a');
            link.className = 'dropdown-item p-2 border-bottom text-decoration-none d-block';
            link.href = `/quick-law/${act}/${secId}/`;
            link.innerHTML = `
              <div class="fw-bold text-primary"><i class="bi bi-hammer me-2"></i> ${act} - Sec ${secId}</div>
              <small class="text-muted text-truncate d-block">${res.text}</small>
            `;
            dropdown.appendChild(link);
          });
          
          dropdown.style.display = 'block';
        })
        .catch(() => {});
      }, 500);
    });

    // Close dropdown on outside click
    document.addEventListener('click', (e) => {
      if (!searchInput.contains(e.target) && !dropdown.contains(e.target)) {
        dropdown.style.display = 'none';
      }
    });
  }
});

// ==========================================
// CONTACT FORM HANDLER
// ==========================================
document.addEventListener('DOMContentLoaded', () => {
  const contactForm = document.querySelector('.contact-form');
  if (contactForm) {
    contactForm.addEventListener('submit', (e) => {
      e.preventDefault();

      const inputs = contactForm.querySelectorAll('input, textarea');
      const name = inputs[0] ? inputs[0].value.trim() : '';
      const email = inputs[1] ? inputs[1].value.trim() : '';
      const message = inputs[2] ? inputs[2].value.trim() : '';

      if (!name || !email || !message) {
        showToast('Please fill in all fields.', true);
        return;
      }

      const submitBtn = contactForm.querySelector('button[type="submit"]');
      const originalText = submitBtn.textContent;
      submitBtn.textContent = 'Sending...';
      submitBtn.disabled = true;

      fetch('/api/contact/submit/', {
        method: 'POST',
        headers: {
          'Content-Type': 'application/json',
          'X-CSRFToken': window.csrfToken
        },
        body: JSON.stringify({ name, email, message })
      })
      .then(res => res.json())
      .then(data => {
        if (data.success) {
          showToast(data.message || 'Message sent successfully!');
          contactForm.reset();
        } else {
          showToast('Failed to send message. Please try again.', true);
        }
      })
      .catch(() => showToast('Network error. Please try again later.', true))
      .finally(() => {
        submitBtn.textContent = originalText;
        submitBtn.disabled = false;
      });
    });
  }
});

// ==========================================
// TOAST NOTIFICATIONS UTILITY
// ==========================================
function showToast(message, isError = false) {
  const container = document.querySelector('.toast-container');
  if (!container) {
    // Fallback: create container if it doesn't exist (for standalone pages)
    const fallback = document.createElement('div');
    fallback.className = 'toast-container position-fixed bottom-0 end-0 p-3';
    fallback.style.zIndex = '10050';
    document.body.appendChild(fallback);
    return showToast(message, isError); // Retry with new container
  }

  const toastEl = document.createElement('div');
  toastEl.className = `toast align-items-center text-white border-0 ${isError ? 'bg-danger' : 'bg-success'}`;
  toastEl.setAttribute('role', 'alert');
  toastEl.setAttribute('aria-live', 'assertive');
  toastEl.setAttribute('aria-atomic', 'true');

  toastEl.innerHTML = `
    <div class="d-flex">
      <div class="toast-body">
        <i class="bi ${isError ? 'bi-exclamation-circle-fill' : 'bi-check-circle-fill'} fs-5 me-2"></i>
        ${message}
      </div>
      <button type="button" class="btn-close btn-close-white me-2 m-auto" data-bs-dismiss="toast" aria-label="Close"></button>
    </div>
  `;

  container.appendChild(toastEl);
  try {
    const bsToast = new bootstrap.Toast(toastEl, { delay: 3000 });
    bsToast.show();
  } catch (e) {
    // Bootstrap not loaded (standalone pages) - manual toast
    toastEl.style.opacity = '1';
    setTimeout(() => toastEl.remove(), 3000);
  }

  toastEl.addEventListener('hidden.bs.toast', () => {
    toastEl.remove();
  });
}