# Monitoramento de Queimadas na Amazônia

Este projeto tem como objetivo monitorar as queimadas na Amazônia e apresentar informações diárias atualizadas sobre os focos de incêndio detectados. Abaixo, você pode visualizar as queimadas mais recentes, com detalhes sobre localização, satélite que realizou a detecção, e outros fatores relevantes.

## Estrutura dos Dados

Cada entrada na tabela representa um foco de incêndio com as seguintes informações:

- **ID:** Identificador único do foco de incêndio.
- **Latitude/Longitude:** Coordenadas geográficas do foco detectado. Para visualizar o local exato, insira estas coordenadas no Google Maps ou outro aplicativo de mapas.
- **Data/Hora GMT:** Data e hora da detecção em formato GMT (Greenwich Mean Time).
- **Satélite:** Satélite responsável pela detecção do foco de incêndio.
- **Município, Estado e País:** Localização administrativa do foco detectado.
- **Dias sem Chuva:** Número de dias consecutivos sem precipitação na região, o que pode indicar um aumento no risco de incêndio.
- **Precipitação:** Quantidade de chuva (em milímetros) registrada no local.
- **Risco de Fogo:** Índice que indica a probabilidade de ocorrência de incêndio, baseado em fatores como condições climáticas e quantidade de combustível disponível.
- **Bioma:** Bioma onde o foco foi identificado, como Amazônia, Cerrado, ou Mata Atlântica.
- **FRP (Fire Radiative Power):** Potência radiativa do fogo, que mede a intensidade do incêndio. Focos com FRP mais alto indicam incêndios mais intensos.

## Visualização Gráfica

Se você deseja visualizar de forma gráfica onde as queimadas estão ocorrendo, copie as coordenadas de latitude e longitude mais recentes e cole no Google Maps. Isso permite uma compreensão espacial mais clara da distribuição dos focos de incêndio. Alternativamente, você também pode usar a descrição de localização (Município, Estado e País) para identificar a região afetada.

## Informação Adicional

As queimadas na Amazônia não apenas afetam a biodiversidade local, mas também têm implicações globais, contribuindo para o aquecimento global e a emissão de gases de efeito estufa. O monitoramento contínuo é essencial para entender e mitigar os impactos desses incêndios, além de auxiliar na gestão de políticas ambientais e ações de preservação.

## Dados Diários - Página 81

| ID | Latitude | Longitude | Data/Hora GMT | Satélite | Município | Estado | País | Município ID | Estado ID | País ID | Dias sem Chuva | Precipitação | Risco de Fogo | Bioma | FRP |
|----|----------|-----------|---------------|----------|-----------|--------|------|--------------|-----------|---------|----------------|--------------|----------------|-------|-----|
| 149abbd9-1eca-3b42-bfc8-0e7363d2efd2 | -7.07013 | -46.53741 | 2024-10-03 04:25:00 | NOAA-21 | FEIRA NOVA DO MARANHÃO | MARANHÃO | Brasil | 2104073 | 21 | 33 | nan | nan | nan | Cerrado | 1.7 |
| daa39eab-90c6-3f28-9176-d63d47c0f73f | -7.04247 | -45.34084 | 2024-10-03 04:25:00 | NOAA-21 | SAMBAÍBA | MARANHÃO | Brasil | 2109700 | 21 | 33 | nan | nan | nan | Cerrado | 1.3 |
| 54811044-9d6e-3385-bf48-a2472f611844 | -7.00624 | -45.66193 | 2024-10-03 04:25:00 | NOAA-21 | SÃO RAIMUNDO DAS MANGABEIRAS | MARANHÃO | Brasil | 2111607 | 21 | 33 | nan | nan | nan | Cerrado | 0.7 |
| 9fe4c0e7-898a-34b6-89d2-018348b299b5 | -7.00188 | -45.49296 | 2024-10-03 04:25:00 | NOAA-21 | SÃO RAIMUNDO DAS MANGABEIRAS | MARANHÃO | Brasil | 2111607 | 21 | 33 | nan | nan | nan | Cerrado | 1.1 |
| 397416a8-613f-3561-8447-46abe9b34822 | -7.00079 | -45.49997 | 2024-10-03 04:25:00 | NOAA-21 | SÃO RAIMUNDO DAS MANGABEIRAS | MARANHÃO | Brasil | 2111607 | 21 | 33 | nan | nan | nan | Cerrado | 1.6 |
| 57153aae-e3a3-35a6-bc24-f4e098af005f | -6.99856 | -45.49244 | 2024-10-03 04:25:00 | NOAA-21 | SÃO RAIMUNDO DAS MANGABEIRAS | MARANHÃO | Brasil | 2111607 | 21 | 33 | nan | nan | nan | Cerrado | 1.1 |
| 27cc9700-5eb8-325b-9fa7-5b03c0800382 | -6.99801 | -45.49596 | 2024-10-03 04:25:00 | NOAA-21 | SÃO RAIMUNDO DAS MANGABEIRAS | MARANHÃO | Brasil | 2111607 | 21 | 33 | nan | nan | nan | Cerrado | 1.1 |
| 51657351-e3dd-31f2-9819-ec84e6f48fa1 | -0.99514 | -46.81029 | 2024-10-03 04:25:00 | NOAA-21 | BRAGANÇA | PARÁ | Brasil | 1501709 | 15 | 33 | nan | nan | nan | Amazônia | 2.4 |
| 4a560fb1-b81a-3442-ad45-6d3c44a214bb | -0.99174 | -46.80977 | 2024-10-03 04:25:00 | NOAA-21 | BRAGANÇA | PARÁ | Brasil | 1501709 | 15 | 33 | nan | nan | nan | Amazônia | 2.4 |
| 742158e8-672d-3f6f-bdbb-3da65d3a8fad | -3.32169 | -47.02018 | 2024-10-03 04:25:00 | NOAA-21 | PARAGOMINAS | PARÁ | Brasil | 1505502 | 15 | 33 | nan | nan | nan | Amazônia | 1.5 |
| a7e1a561-afaa-3bdd-9165-659f86034484 | -3.30941 | -46.27626 | 2024-10-03 04:25:00 | NOAA-21 | ZÉ DOCA | MARANHÃO | Brasil | 2114007 | 21 | 33 | nan | nan | nan | Amazônia | 1.3 |
| 365e6401-a879-3332-8d0b-4a278709c981 | -2.99031 | -47.45286 | 2024-10-03 04:25:00 | NOAA-21 | PARAGOMINAS | PARÁ | Brasil | 1505502 | 15 | 33 | nan | nan | nan | Amazônia | 2.3 |
| d20f5c03-aaf6-37b5-9916-ccb014eb5179 | -3.41271 | -47.0673 | 2024-10-03 04:25:00 | NOAA-21 | PARAGOMINAS | PARÁ | Brasil | 1505502 | 15 | 33 | nan | nan | nan | Amazônia | 1.5 |
| 3fa38e40-e047-3666-bbce-4c444c96b32f | -2.72998 | -46.79572 | 2024-10-03 04:25:00 | NOAA-21 | PARAGOMINAS | PARÁ | Brasil | 1505502 | 15 | 33 | nan | nan | nan | Amazônia | 1.8 |
| 2bd9977b-59b2-3484-b797-332ae4487640 | -2.72662 | -46.7952 | 2024-10-03 04:25:00 | NOAA-21 | PARAGOMINAS | PARÁ | Brasil | 1505502 | 15 | 33 | nan | nan | nan | Amazônia | 1.3 |
| 2e4fe1cd-273f-39a8-98c8-ba21c3cd9153 | -2.72383 | -46.79113 | 2024-10-03 04:25:00 | NOAA-21 | PARAGOMINAS | PARÁ | Brasil | 1505502 | 15 | 33 | nan | nan | nan | Amazônia | 2.6 |
| 23d98972-7030-36c1-8097-3eee5d67165d | -2.72327 | -46.79468 | 2024-10-03 04:25:00 | NOAA-21 | PARAGOMINAS | PARÁ | Brasil | 1505502 | 15 | 33 | nan | nan | nan | Amazônia | 1.3 |
| 573c8280-cc57-3535-84e1-53fda3baf8d9 | -2.72162 | -46.79073 | 2024-10-03 04:25:00 | NOAA-21 | PARAGOMINAS | PARÁ | Brasil | 1505502 | 15 | 33 | nan | nan | nan | Amazônia | 0.9 |
| 29d338a6-1c5b-322a-bcbc-4faf269ee0cd | -2.53999 | -47.23261 | 2024-10-03 04:25:00 | NOAA-21 | CAPITÃO POÇO | PARÁ | Brasil | 1502301 | 15 | 33 | nan | nan | nan | Amazônia | 0.9 |
| 559324b0-001a-3d32-af68-b5311bea360e | -2.53774 | -47.22474 | 2024-10-03 04:25:00 | NOAA-21 | CAPITÃO POÇO | PARÁ | Brasil | 1502301 | 15 | 33 | nan | nan | nan | Amazônia | 4.5 |
| f290c284-627a-34de-8923-e71c8c703cfc | -2.53717 | -47.22839 | 2024-10-03 04:25:00 | NOAA-21 | CAPITÃO POÇO | PARÁ | Brasil | 1502301 | 15 | 33 | nan | nan | nan | Amazônia | 4.5 |
| 82e21b94-398d-3cac-a0ba-0217c4caba6e | -2.52735 | -47.0698 | 2024-10-03 04:25:00 | NOAA-21 | NOVA ESPERANÇA DO PIRIÁ | PARÁ | Brasil | 1504950 | 15 | 33 | nan | nan | nan | Amazônia | 1.0 |
| b8521be8-824f-347f-b894-67c3e7b500da | -2.52677 | -47.07343 | 2024-10-03 04:25:00 | NOAA-21 | NOVA ESPERANÇA DO PIRIÁ | PARÁ | Brasil | 1504950 | 15 | 33 | nan | nan | nan | Amazônia | 0.9 |
| fe6b2c3c-8a78-3948-a5e5-05b763f85468 | -4.74657 | -46.78842 | 2024-10-03 04:25:00 | NOAA-21 | BOM JESUS DAS SELVAS | MARANHÃO | Brasil | 2102036 | 21 | 33 | nan | nan | nan | Amazônia | 1.4 |
| 1c8b8d20-295d-328b-a440-ba97082e0885 | -4.68893 | -46.82965 | 2024-10-03 04:25:00 | NOAA-21 | BOM JESUS DAS SELVAS | MARANHÃO | Brasil | 2102036 | 21 | 33 | nan | nan | nan | Amazônia | 0.9 |
| 0865fe95-12bf-3448-8d5c-7ab69cabca0b | -4.60942 | -46.47089 | 2024-10-03 04:25:00 | NOAA-21 | BURITICUPU | MARANHÃO | Brasil | 2102325 | 21 | 33 | nan | nan | nan | Amazônia | 0.8 |
| 8a5aba90-5396-3df3-a3b9-41059c6f3875 | -4.49648 | -46.38927 | 2024-10-03 04:25:00 | NOAA-21 | BURITICUPU | MARANHÃO | Brasil | 2102325 | 21 | 33 | nan | nan | nan | Amazônia | 1.3 |
| 04dd2d2f-0348-39bb-8dad-219a23dd8a47 | -4.49372 | -46.3853 | 2024-10-03 04:25:00 | NOAA-21 | BURITICUPU | MARANHÃO | Brasil | 2102325 | 21 | 33 | nan | nan | nan | Amazônia | 1.5 |
| fe466a84-3cd6-3310-a5a7-6039a9a614ec | -4.49317 | -46.38876 | 2024-10-03 04:25:00 | NOAA-21 | BURITICUPU | MARANHÃO | Brasil | 2102325 | 21 | 33 | nan | nan | nan | Amazônia | 1.5 |
| fa754899-7d15-346f-906a-d69b664cb546 | -4.40658 | -46.33274 | 2024-10-03 04:25:00 | NOAA-21 | BURITICUPU | MARANHÃO | Brasil | 2102325 | 21 | 33 | nan | nan | nan | Amazônia | 1.0 |
| 0aaa9381-f3c5-39cf-96e5-c53c3cc0b7f8 | -4.40327 | -46.33224 | 2024-10-03 04:25:00 | NOAA-21 | BURITICUPU | MARANHÃO | Brasil | 2102325 | 21 | 33 | nan | nan | nan | Amazônia | 1.0 |
| 20f4b147-9432-37a2-9203-c272666390fe | -4.13289 | -46.70916 | 2024-10-03 04:25:00 | NOAA-21 | BOM JARDIM | MARANHÃO | Brasil | 2102002 | 21 | 33 | nan | nan | nan | Amazônia | 1.0 |
| 3df41b80-e0ee-3fa6-8342-8856ce4f62a3 | -4.12424 | -46.37646 | 2024-10-03 04:25:00 | NOAA-21 | BURITICUPU | MARANHÃO | Brasil | 2102325 | 21 | 33 | nan | nan | nan | Amazônia | 1.3 |
| ade30093-640d-3c6f-b6ca-874cad004724 | -5.04932 | -47.15694 | 2024-10-03 04:25:00 | NOAA-21 | AÇAILÂNDIA | MARANHÃO | Brasil | 2100055 | 21 | 33 | nan | nan | nan | Amazônia | 0.9 |
| 836bcf1f-672e-3fc1-b343-1d0a3466a06b | -5.04598 | -47.15642 | 2024-10-03 04:25:00 | NOAA-21 | AÇAILÂNDIA | MARANHÃO | Brasil | 2100055 | 21 | 33 | nan | nan | nan | Amazônia | 0.9 |
| 2b791083-f40d-343c-9cc7-0911970aa524 | -4.94628 | -47.14109 | 2024-10-03 04:25:00 | NOAA-21 | AÇAILÂNDIA | MARANHÃO | Brasil | 2100055 | 21 | 33 | nan | nan | nan | Amazônia | 2.9 |
| 90d901de-64b1-36d3-bb71-c88da55ff4be | -4.94293 | -47.14058 | 2024-10-03 04:25:00 | NOAA-21 | AÇAILÂNDIA | MARANHÃO | Brasil | 2100055 | 21 | 33 | nan | nan | nan | Amazônia | 2.9 |
| 8e785a45-bea1-3d77-b983-efaa56a0234e | -4.92287 | -47.13744 | 2024-10-03 04:25:00 | NOAA-21 | AÇAILÂNDIA | MARANHÃO | Brasil | 2100055 | 21 | 33 | nan | nan | nan | Amazônia | 3.8 |
| 50715d05-3884-37b8-b3c7-3aa71e0ca531 | -4.81769 | -47.64727 | 2024-10-03 04:25:00 | NOAA-21 | AÇAILÂNDIA | MARANHÃO | Brasil | 2100055 | 21 | 33 | nan | nan | nan | Amazônia | 1.8 |
| 2624b01e-b4b2-3ce5-a6bc-4d49690006a6 | -4.65095 | -47.43501 | 2024-10-03 04:25:00 | NOAA-21 | AÇAILÂNDIA | MARANHÃO | Brasil | 2100055 | 21 | 33 | nan | nan | nan | Amazônia | 4.9 |
| 4d1d0653-5503-368f-9c43-dea3562e39c1 | -4.64757 | -47.43449 | 2024-10-03 04:25:00 | NOAA-21 | AÇAILÂNDIA | MARANHÃO | Brasil | 2100055 | 21 | 33 | nan | nan | nan | Amazônia | 8.6 |
| 587f1f58-d83a-3288-a79f-278ebef69ad8 | -4.47324 | -47.7365 | 2024-10-03 04:25:00 | NOAA-21 | DOM ELISEU | PARÁ | Brasil | 1502939 | 15 | 33 | nan | nan | nan | Amazônia | 0.9 |
| 781a6cb0-1494-3e13-afc7-4596e18aa862 | -4.39507 | -47.28375 | 2024-10-03 04:25:00 | NOAA-21 | ITINGA DO MARANHÃO | MARANHÃO | Brasil | 2105427 | 21 | 33 | nan | nan | nan | Amazônia | 1.9 |
| 3ec9e810-d977-3bbb-a2cd-26db28279c3f | -4.38124 | -47.47793 | 2024-10-03 04:25:00 | NOAA-21 | ITINGA DO MARANHÃO | MARANHÃO | Brasil | 2105427 | 21 | 33 | nan | nan | nan | Amazônia | 1.3 |
| 68d49a74-f21d-3277-883b-b8eb97f803b8 | -4.38065 | -47.48159 | 2024-10-03 04:25:00 | NOAA-21 | ITINGA DO MARANHÃO | MARANHÃO | Brasil | 2105427 | 21 | 33 | nan | nan | nan | Amazônia | 1.2 |
| 2f7f592c-dbb3-3106-949c-57bf4ab3d49e | -4.29013 | -47.49725 | 2024-10-03 04:25:00 | NOAA-21 | DOM ELISEU | PARÁ | Brasil | 1502939 | 15 | 33 | nan | nan | nan | Amazônia | 2.4 |
| b28ca6ae-bc52-3d20-a5e4-3318075dbb69 | -4.15716 | -47.2027 | 2024-10-03 04:25:00 | NOAA-21 | ITINGA DO MARANHÃO | MARANHÃO | Brasil | 2105427 | 21 | 33 | nan | nan | nan | Amazônia | 1.5 |
| fd853ab8-fa67-3855-8f26-75003ddb5a06 | -3.92282 | -46.44426 | 2024-10-03 04:25:00 | NOAA-21 | BOM JARDIM | MARANHÃO | Brasil | 2102002 | 21 | 33 | nan | nan | nan | Amazônia | 0.7 |
| b082d24b-5361-3014-a3ae-ca5cc4b3e0d0 | -3.92005 | -46.44028 | 2024-10-03 04:25:00 | NOAA-21 | BOM JARDIM | MARANHÃO | Brasil | 2102002 | 21 | 33 | nan | nan | nan | Amazônia | 0.6 |
| 9a77ffe0-1d2e-319e-8273-ff7c9e5bd391 | -3.9057 | -46.44516 | 2024-10-03 04:25:00 | NOAA-21 | BOM JARDIM | MARANHÃO | Brasil | 2102002 | 21 | 33 | nan | nan | nan | Amazônia | 2.0 |
| e22dd0a1-d132-397a-b3ad-d07867d78eee | -3.90238 | -46.44466 | 2024-10-03 04:25:00 | NOAA-21 | BOM JARDIM | MARANHÃO | Brasil | 2102002 | 21 | 33 | nan | nan | nan | Amazônia | 2.0 |
| 45cf0fd2-136e-3773-b363-d273669868fd | -3.76282 | -47.49788 | 2024-10-03 04:25:00 | NOAA-21 | ULIANÓPOLIS | PARÁ | Brasil | 1508126 | 15 | 33 | nan | nan | nan | Amazônia | 1.9 |
| cdfb4911-a895-353e-b122-305a8f39a2eb | -3.70652 | -47.6098 | 2024-10-03 04:25:00 | NOAA-21 | ULIANÓPOLIS | PARÁ | Brasil | 1508126 | 15 | 33 | nan | nan | nan | Amazônia | 2.1 |
| e1c54d3b-5ea8-3990-ac1e-bc066d865e11 | -3.70593 | -47.61349 | 2024-10-03 04:25:00 | NOAA-21 | ULIANÓPOLIS | PARÁ | Brasil | 1508126 | 15 | 33 | nan | nan | nan | Amazônia | 2.1 |
| fe69a3c0-0f1a-3677-bae2-ed91b76b161b | -3.70311 | -47.60924 | 2024-10-03 04:25:00 | NOAA-21 | ULIANÓPOLIS | PARÁ | Brasil | 1508126 | 15 | 33 | nan | nan | nan | Amazônia | 2.1 |
| a35b09d1-df82-364e-98cf-1a3f6a479b19 | -3.70252 | -47.61293 | 2024-10-03 04:25:00 | NOAA-21 | ULIANÓPOLIS | PARÁ | Brasil | 1508126 | 15 | 33 | nan | nan | nan | Amazônia | 2.1 |
| 33923763-ffb9-3666-a64d-327a6cc6a4a6 | -3.70088 | -47.60131 | 2024-10-03 04:25:00 | NOAA-21 | ULIANÓPOLIS | PARÁ | Brasil | 1508126 | 15 | 33 | nan | nan | nan | Amazônia | 2.5 |
| 6727b837-6cd0-3b8f-87da-ccd9f2dc19d6 | -3.70029 | -47.60501 | 2024-10-03 04:25:00 | NOAA-21 | ULIANÓPOLIS | PARÁ | Brasil | 1508126 | 15 | 33 | nan | nan | nan | Amazônia | 2.5 |
| ef468056-ecb4-3bc1-81b7-7a7b51e00ef0 | -3.69806 | -47.59708 | 2024-10-03 04:25:00 | NOAA-21 | ULIANÓPOLIS | PARÁ | Brasil | 1508126 | 15 | 33 | nan | nan | nan | Amazônia | 1.5 |
| 1629dfea-0317-36b5-9614-f19d6f4e80da | -5.23973 | -46.77067 | 2024-10-03 04:25:00 | NOAA-21 | AMARANTE DO MARANHÃO | MARANHÃO | Brasil | 2100600 | 21 | 33 | nan | nan | nan | Cerrado | 3.3 |
| 827dc895-f5e5-3cfc-b0ad-41b6c887f473 | -5.23918 | -46.77415 | 2024-10-03 04:25:00 | NOAA-21 | AMARANTE DO MARANHÃO | MARANHÃO | Brasil | 2100600 | 21 | 33 | nan | nan | nan | Cerrado | 2.0 |
| 147b4f61-c67e-3f03-b259-bebf42cef123 | -6.43303 | -47.40282 | 2024-10-03 04:25:00 | NOAA-21 | PORTO FRANCO | MARANHÃO | Brasil | 2109007 | 21 | 33 | nan | nan | nan | Cerrado | 3.6 |
| 089d567b-9fb3-31a7-822e-dff144a058fe | -6.35462 | -47.3795 | 2024-10-03 04:25:00 | NOAA-21 | PORTO FRANCO | MARANHÃO | Brasil | 2109007 | 21 | 33 | nan | nan | nan | Cerrado | 3.1 |
| 6cbe51bd-2441-352f-8c72-9b34cd8cd24c | -6.28093 | -46.9866 | 2024-10-03 04:25:00 | NOAA-21 | SÃO JOÃO DO PARAÍSO | MARANHÃO | Brasil | 2111052 | 21 | 33 | nan | nan | nan | Cerrado | 1.1 |
| bc31487b-c281-3c4b-aa8a-3fd1ab8629a6 | -6.28038 | -46.99009 | 2024-10-03 04:25:00 | NOAA-21 | SÃO JOÃO DO PARAÍSO | MARANHÃO | Brasil | 2111052 | 21 | 33 | nan | nan | nan | Cerrado | 2.1 |
| 9f189b48-b756-3c68-9cca-7e620462f704 | -6.27706 | -46.98957 | 2024-10-03 04:25:00 | NOAA-21 | SÃO JOÃO DO PARAÍSO | MARANHÃO | Brasil | 2111052 | 21 | 33 | nan | nan | nan | Cerrado | 2.8 |
| ab622e1f-72ac-3875-8fab-95165a081bff | -5.06313 | -47.67029 | 2024-10-03 04:25:00 | NOAA-21 | CIDELÂNDIA | MARANHÃO | Brasil | 2103257 | 21 | 33 | nan | nan | nan | Amazônia | 2.0 |
| 2cf680f8-97e1-3320-8392-57f6880dfe29 | -5.06255 | -47.67394 | 2024-10-03 04:25:00 | NOAA-21 | CIDELÂNDIA | MARANHÃO | Brasil | 2103257 | 21 | 33 | nan | nan | nan | Amazônia | 2.0 |
| 51eb92f8-1667-3434-af79-d5c030ccdfe9 | -6.1278 | -47.26708 | 2024-10-03 04:25:00 | NOAA-21 | CAMPESTRE DO MARANHÃO | MARANHÃO | Brasil | 2102556 | 21 | 33 | nan | nan | nan | Cerrado | 1.6 |
| f4af2ba3-a4b7-3383-b2f1-fdb2b0cc9567 | -6.1257 | -48.06059 | 2024-10-03 04:25:00 | NOAA-21 | SÃO BENTO DO TOCANTINS | TOCANTINS | Brasil | 1720101 | 17 | 33 | nan | nan | nan | Cerrado | 1.0 |
| 3ec446ae-5f26-30e0-b7ee-339a50aeac6b | -6.12447 | -47.26655 | 2024-10-03 04:25:00 | NOAA-21 | CAMPESTRE DO MARANHÃO | MARANHÃO | Brasil | 2102556 | 21 | 33 | nan | nan | nan | Cerrado | 1.6 |
| ddd976b0-325a-3a74-89e5-13cdf398126d | -6.12391 | -47.27009 | 2024-10-03 04:25:00 | NOAA-21 | CAMPESTRE DO MARANHÃO | MARANHÃO | Brasil | 2102556 | 21 | 33 | nan | nan | nan | Cerrado | 1.6 |
| 42ba8caf-a433-383c-8173-0fd6a2c89875 | -5.97251 | -47.27886 | 2024-10-03 04:25:00 | NOAA-21 | RIBAMAR FIQUENE | MARANHÃO | Brasil | 2109551 | 21 | 33 | nan | nan | nan | Cerrado | 1.7 |
| dc01f6ec-1242-36ac-8f1e-1d526c1313a4 | -5.46495 | -47.08907 | 2024-10-03 04:25:00 | NOAA-21 | BURITIRANA | MARANHÃO | Brasil | 2102358 | 21 | 33 | nan | nan | nan | Cerrado | 2.2 |
| e0db63ba-02c5-37ab-822e-cce14756bc0f | -5.46162 | -47.08855 | 2024-10-03 04:25:00 | NOAA-21 | BURITIRANA | MARANHÃO | Brasil | 2102358 | 21 | 33 | nan | nan | nan | Cerrado | 2.2 |
| 038871ed-3509-365d-9781-524582ef4781 | -5.43138 | -47.53962 | 2024-10-03 04:25:00 | NOAA-21 | IMPERATRIZ | MARANHÃO | Brasil | 2105302 | 21 | 33 | nan | nan | nan | Cerrado | 1.3 |
| 4a9de16f-67a1-36de-ad15-9d1edd9de0b4 | -5.42939 | -47.09798 | 2024-10-03 04:25:00 | NOAA-21 | BURITIRANA | MARANHÃO | Brasil | 2102358 | 21 | 33 | nan | nan | nan | Amazônia | 2.0 |
| 65763029-95e2-3598-975d-57e4c57f1fbf | -5.41613 | -47.57051 | 2024-10-03 04:25:00 | NOAA-21 | IMPERATRIZ | MARANHÃO | Brasil | 2105302 | 21 | 33 | nan | nan | nan | Cerrado | 1.1 |
| c75981d9-f0a4-321a-8659-ce47519e53bd | -5.37515 | -47.69777 | 2024-10-03 04:25:00 | NOAA-21 | IMPERATRIZ | MARANHÃO | Brasil | 2105302 | 21 | 33 | nan | nan | nan | Cerrado | 0.9 |
| 3c2e6ac6-adfc-3135-ad39-92d51d9d3be7 | -5.3645 | -47.8084 | 2024-10-03 04:25:00 | NOAA-21 | IMPERATRIZ | MARANHÃO | Brasil | 2105302 | 21 | 33 | nan | nan | nan | Cerrado | 1.7 |
| ba8da666-635a-3176-b246-318a74665f0e | -5.35645 | -46.72141 | 2024-10-03 04:25:00 | NOAA-21 | AMARANTE DO MARANHÃO | MARANHÃO | Brasil | 2100600 | 21 | 33 | nan | nan | nan | Amazônia | 0.9 |
| 7e991e25-a604-3227-b7ec-683cb19e0f0b | -7.06438 | -48.03305 | 2024-10-03 04:25:00 | NOAA-21 | WANDERLÂNDIA | TOCANTINS | Brasil | 1722081 | 17 | 33 | nan | nan | nan | Cerrado | 2.2 |
| 41ab1ca3-cc1e-39f0-aa82-c65df0821d4a | -5.35589 | -46.72489 | 2024-10-03 04:25:00 | NOAA-21 | AMARANTE DO MARANHÃO | MARANHÃO | Brasil | 2100600 | 21 | 33 | nan | nan | nan | Amazônia | 0.9 |
| 9de1ee6d-8b9b-3e76-b22e-c079ba0d440d | -5.35314 | -46.72089 | 2024-10-03 04:25:00 | NOAA-21 | AMARANTE DO MARANHÃO | MARANHÃO | Brasil | 2100600 | 21 | 33 | nan | nan | nan | Amazônia | 6.3 |
| 320b002d-6026-3574-aaab-c5b9b1e38642 | -5.35258 | -46.72437 | 2024-10-03 04:25:00 | NOAA-21 | AMARANTE DO MARANHÃO | MARANHÃO | Brasil | 2100600 | 21 | 33 | nan | nan | nan | Amazônia | 6.3 |
| 3621ee97-ac61-33cd-b4e3-4e3aa490c276 | -5.3487 | -46.87716 | 2024-10-03 04:25:00 | NOAA-21 | AMARANTE DO MARANHÃO | MARANHÃO | Brasil | 2100600 | 21 | 33 | nan | nan | nan | Cerrado | 0.7 |
| b1fa3432-740e-3d44-97d7-26907f563eef | -7.17886 | -47.82548 | 2024-10-03 04:25:00 | NOAA-21 | BABAÇULÂNDIA | TOCANTINS | Brasil | 1703008 | 17 | 33 | nan | nan | nan | Cerrado | 2.7 |
| eb33b778-ba03-3325-adaa-896c9e240ecc | -7.17828 | -47.82906 | 2024-10-03 04:25:00 | NOAA-21 | BABAÇULÂNDIA | TOCANTINS | Brasil | 1703008 | 17 | 33 | nan | nan | nan | Cerrado | 2.4 |
| fee60f5f-a9de-3524-abad-425af12d142c | -7.17771 | -47.83263 | 2024-10-03 04:25:00 | NOAA-21 | BABAÇULÂNDIA | TOCANTINS | Brasil | 1703008 | 17 | 33 | nan | nan | nan | Cerrado | 2.4 |
| 35a4e792-4237-3f48-a336-680da606d631 | -7.17378 | -47.83566 | 2024-10-03 04:25:00 | NOAA-21 | BABAÇULÂNDIA | TOCANTINS | Brasil | 1703008 | 17 | 33 | nan | nan | nan | Cerrado | 3.4 |
| 26b0a7f5-28a1-3e4e-8be8-7fbdc97ade3e | -7.1156 | -47.88525 | 2024-10-03 04:25:00 | NOAA-21 | BABAÇULÂNDIA | TOCANTINS | Brasil | 1703008 | 17 | 33 | nan | nan | nan | Cerrado | 2.6 |
| 333f8466-2245-3afd-b8be-f617fb5f172c | -7.11397 | -47.87381 | 2024-10-03 04:25:00 | NOAA-21 | BABAÇULÂNDIA | TOCANTINS | Brasil | 1703008 | 17 | 33 | nan | nan | nan | Cerrado | 2.5 |
| 1a73ca37-9ecf-3a42-b27c-d05cc78608de | -7.1134 | -47.87741 | 2024-10-03 04:25:00 | NOAA-21 | BABAÇULÂNDIA | TOCANTINS | Brasil | 1703008 | 17 | 33 | nan | nan | nan | Cerrado | 3.7 |
| 4ff562bf-99d6-38f4-b311-6bc4fc2cb708 | -7.11282 | -47.88105 | 2024-10-03 04:25:00 | NOAA-21 | BABAÇULÂNDIA | TOCANTINS | Brasil | 1703008 | 17 | 33 | nan | nan | nan | Cerrado | 3.7 |
| f0c88334-4615-3516-88db-82c5ea29b241 | -7.11224 | -47.88467 | 2024-10-03 04:25:00 | NOAA-21 | BABAÇULÂNDIA | TOCANTINS | Brasil | 1703008 | 17 | 33 | nan | nan | nan | Cerrado | 2.6 |
| 33030e90-9b85-353c-9ffe-a0fb56fc7008 | -7.11167 | -47.8883 | 2024-10-03 04:25:00 | NOAA-21 | BABAÇULÂNDIA | TOCANTINS | Brasil | 1703008 | 17 | 33 | nan | nan | nan | Cerrado | 2.6 |
| 1638502d-0733-3017-aad7-f5d8e3a039f5 | -7.11118 | -47.86965 | 2024-10-03 04:25:00 | NOAA-21 | BABAÇULÂNDIA | TOCANTINS | Brasil | 1703008 | 17 | 33 | nan | nan | nan | Cerrado | 2.7 |
| 854e166c-38e0-3f15-b202-eddad02c66f9 | -7.11061 | -47.87328 | 2024-10-03 04:25:00 | NOAA-21 | BABAÇULÂNDIA | TOCANTINS | Brasil | 1703008 | 17 | 33 | nan | nan | nan | Cerrado | 2.7 |
| ebb3a242-29db-3634-ac52-ad841e56ef73 | -7.10887 | -47.88417 | 2024-10-03 04:25:00 | NOAA-21 | BABAÇULÂNDIA | TOCANTINS | Brasil | 1703008 | 17 | 33 | nan | nan | nan | Cerrado | 1.6 |
| 78a6451d-e9eb-3c1d-bf35-b0f97feb59b5 | -7.10839 | -47.86554 | 2024-10-03 04:25:00 | NOAA-21 | BABAÇULÂNDIA | TOCANTINS | Brasil | 1703008 | 17 | 33 | nan | nan | nan | Cerrado | 2.6 |


[Clique aqui para ver as próximas entradas](README82.md)
