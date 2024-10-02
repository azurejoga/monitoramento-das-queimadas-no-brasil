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

## Dados Diários - Página 71

| ID | Latitude | Longitude | Data/Hora GMT | Satélite | Município | Estado | País | Município ID | Estado ID | País ID | Dias sem Chuva | Precipitação | Risco de Fogo | Bioma | FRP |
|----|----------|-----------|---------------|----------|-----------|--------|------|--------------|-----------|---------|----------------|--------------|----------------|-------|-----|
| f5c36d7b-1bed-31a2-8f1e-b100237ed2bf | -20.5234 | -46.27677 | 2024-10-02 03:55:00 | NOAA-20 | VARGEM BONITA | MINAS GERAIS | Brasil | 3170602 | 31 | 33 | nan | nan | nan | Cerrado | 9.3 |
| 9e1702d1-50d7-3687-9af7-d69b49e0aa98 | -20.52241 | -46.28207 | 2024-10-02 03:55:00 | NOAA-20 | VARGEM BONITA | MINAS GERAIS | Brasil | 3170602 | 31 | 33 | nan | nan | nan | Cerrado | 3.1 |
| 31dd30fd-ff0f-33f6-a349-769fc39f4279 | -20.52051 | -46.31379 | 2024-10-02 03:55:00 | NOAA-20 | VARGEM BONITA | MINAS GERAIS | Brasil | 3170602 | 31 | 33 | nan | nan | nan | Cerrado | 28.6 |
| a8132670-fec2-3774-b59c-7e600c4fc18d | -20.5205 | -46.27081 | 2024-10-02 03:55:00 | NOAA-20 | VARGEM BONITA | MINAS GERAIS | Brasil | 3170602 | 31 | 33 | nan | nan | nan | Cerrado | 2.3 |
| c9e1845a-c2b1-3e02-aa44-a3ee392e97a3 | -20.51962 | -46.31856 | 2024-10-02 03:55:00 | NOAA-20 | VARGEM BONITA | MINAS GERAIS | Brasil | 3170602 | 31 | 33 | nan | nan | nan | Cerrado | 28.6 |
| 828f6756-a25f-32d1-b1c8-5b49f78ec1cc | -20.51951 | -46.27612 | 2024-10-02 03:55:00 | NOAA-20 | VARGEM BONITA | MINAS GERAIS | Brasil | 3170602 | 31 | 33 | nan | nan | nan | Cerrado | 2.3 |
| fcfd55f9-ad50-3fd4-855c-ecb09761fd6c | -20.51852 | -46.28139 | 2024-10-02 03:55:00 | NOAA-20 | VARGEM BONITA | MINAS GERAIS | Brasil | 3170602 | 31 | 33 | nan | nan | nan | Cerrado | 1.7 |
| 47e933b7-ec44-3be2-871f-d3b1b02a0bf2 | -20.51675 | -46.33394 | 2024-10-02 03:55:00 | NOAA-20 | VARGEM BONITA | MINAS GERAIS | Brasil | 3170602 | 31 | 33 | nan | nan | nan | Cerrado | 1.3 |
| 64e3f6dc-7902-3573-be45-a59c0d30947b | -20.51478 | -46.32296 | 2024-10-02 03:55:00 | NOAA-20 | VARGEM BONITA | MINAS GERAIS | Brasil | 3170602 | 31 | 33 | nan | nan | nan | Cerrado | 3.0 |
| 55769670-ef6a-309b-8b54-b584701a296c | -20.51381 | -46.32813 | 2024-10-02 03:55:00 | NOAA-20 | VARGEM BONITA | MINAS GERAIS | Brasil | 3170602 | 31 | 33 | nan | nan | nan | Cerrado | 3.0 |
| 076fcaed-dd62-3867-971b-4f30efd5204b | -20.51285 | -46.33327 | 2024-10-02 03:55:00 | NOAA-20 | VARGEM BONITA | MINAS GERAIS | Brasil | 3170602 | 31 | 33 | nan | nan | nan | Cerrado | 1.3 |
| 03bb9cf1-18f6-3905-a10a-62f12bcebfcc | -20.5118 | -46.31734 | 2024-10-02 03:55:00 | NOAA-20 | VARGEM BONITA | MINAS GERAIS | Brasil | 3170602 | 31 | 33 | nan | nan | nan | Cerrado | 5.3 |
| 658d1b39-37e9-3bdd-ac6f-632e920a6b44 | -20.51086 | -46.3224 | 2024-10-02 03:55:00 | NOAA-20 | VARGEM BONITA | MINAS GERAIS | Brasil | 3170602 | 31 | 33 | nan | nan | nan | Cerrado | 4.3 |
| 1d85a505-dee5-32f7-945b-a288be7d05e5 | -20.50978 | -46.30664 | 2024-10-02 03:55:00 | NOAA-20 | VARGEM BONITA | MINAS GERAIS | Brasil | 3170602 | 31 | 33 | nan | nan | nan | Cerrado | 6.2 |
| 51e73180-0d4d-32c3-98ce-40ebd07b40dd | -20.50884 | -46.3117 | 2024-10-02 03:55:00 | NOAA-20 | VARGEM BONITA | MINAS GERAIS | Brasil | 3170602 | 31 | 33 | nan | nan | nan | Cerrado | 5.3 |
| 33782761-fac6-3420-8685-c5c08ade22f0 | -20.50789 | -46.31675 | 2024-10-02 03:55:00 | NOAA-20 | VARGEM BONITA | MINAS GERAIS | Brasil | 3170602 | 31 | 33 | nan | nan | nan | Cerrado | 5.3 |
| 1f898e9e-97be-33a9-9c40-7e66c476e4fe | -20.5059 | -46.3059 | 2024-10-02 03:55:00 | NOAA-20 | VARGEM BONITA | MINAS GERAIS | Brasil | 3170602 | 31 | 33 | nan | nan | nan | Cerrado | 25.0 |
| d39b0de5-61cc-3636-98be-81df8d83acf5 | -20.50495 | -46.31099 | 2024-10-02 03:55:00 | NOAA-20 | VARGEM BONITA | MINAS GERAIS | Brasil | 3170602 | 31 | 33 | nan | nan | nan | Cerrado | 10.4 |
| 28b985d6-ad27-3555-a1f4-9d961d808be4 | -20.50202 | -46.30513 | 2024-10-02 03:55:00 | NOAA-20 | VARGEM BONITA | MINAS GERAIS | Brasil | 3170602 | 31 | 33 | nan | nan | nan | Cerrado | 25.0 |
| 9a44ecf2-03fc-3878-bd70-03bbcf34b22c | -20.50188 | -46.3034 | 2024-10-02 03:55:00 | NOAA-20 | VARGEM BONITA | MINAS GERAIS | Brasil | 3170602 | 31 | 33 | nan | nan | nan | Cerrado | 5.4 |
| 2cba08b3-4009-3159-a3ff-0e93d083c617 | -20.50096 | -46.30852 | 2024-10-02 03:55:00 | NOAA-20 | VARGEM BONITA | MINAS GERAIS | Brasil | 3170602 | 31 | 33 | nan | nan | nan | Cerrado | 5.4 |
| 4634ca35-0af3-3468-9159-5646f28d6e60 | -20.34313 | -46.37661 | 2024-10-02 03:55:00 | NOAA-20 | VARGEM BONITA | MINAS GERAIS | Brasil | 3170602 | 31 | 33 | nan | nan | nan | Cerrado | 1.1 |
| 842a86d6-b4d2-3051-959b-71a70ad8ad6c | -19.66172 | -46.23699 | 2024-10-02 03:55:00 | NOAA-20 | CAMPOS ALTOS | MINAS GERAIS | Brasil | 3111507 | 31 | 33 | nan | nan | nan | Cerrado | 1.5 |
| c39c6450-580c-38a8-9c0d-fefbed14cef1 | -14.65381 | -45.91749 | 2024-10-02 03:55:00 | NOAA-20 | JABORANDI | BAHIA | Brasil | 2917359 | 29 | 33 | nan | nan | nan | Cerrado | 2.0 |
| d7880195-8c46-310e-acf8-789aae3d5812 | -14.6531 | -45.92143 | 2024-10-02 03:55:00 | NOAA-20 | JABORANDI | BAHIA | Brasil | 2917359 | 29 | 33 | nan | nan | nan | Cerrado | 2.0 |
| e8b808d2-fea1-3f76-b189-9d13f567710a | -14.64965 | -45.91667 | 2024-10-02 03:55:00 | NOAA-20 | JABORANDI | BAHIA | Brasil | 2917359 | 29 | 33 | nan | nan | nan | Cerrado | 1.4 |
| 303da71f-b6dd-3e07-a610-a4e5664473cb | -14.64893 | -45.92062 | 2024-10-02 03:55:00 | NOAA-20 | JABORANDI | BAHIA | Brasil | 2917359 | 29 | 33 | nan | nan | nan | Cerrado | 1.4 |
| 79273f6e-51d6-3b5b-8110-fbdefa3f764f | -14.44236 | -45.71706 | 2024-10-02 03:55:00 | NOAA-20 | JABORANDI | BAHIA | Brasil | 2917359 | 29 | 33 | nan | nan | nan | Cerrado | 3.7 |
| 0cd86b37-c877-3c52-ae20-e692544e0ff2 | -14.43823 | -45.71627 | 2024-10-02 03:55:00 | NOAA-20 | JABORANDI | BAHIA | Brasil | 2917359 | 29 | 33 | nan | nan | nan | Cerrado | 3.7 |
| 7d869dac-4313-3e44-aa3c-4237ff565eea | -14.4348 | -45.71163 | 2024-10-02 03:55:00 | NOAA-20 | JABORANDI | BAHIA | Brasil | 2917359 | 29 | 33 | nan | nan | nan | Cerrado | 0.6 |
| f293bbfb-3d1b-34bb-bb13-b6f538967b62 | -14.18789 | -46.46387 | 2024-10-02 03:55:00 | NOAA-20 | POSSE | GOIÁS | Brasil | 5218300 | 52 | 33 | nan | nan | nan | Cerrado | 1.2 |
| 892a816e-3556-39ff-b400-674a2310c606 | -14.18706 | -46.46835 | 2024-10-02 03:55:00 | NOAA-20 | POSSE | GOIÁS | Brasil | 5218300 | 52 | 33 | nan | nan | nan | Cerrado | 1.2 |
| 4a097b81-0a64-3961-9a7e-86c6c415ea6e | -14.18273 | -46.46733 | 2024-10-02 03:55:00 | NOAA-20 | POSSE | GOIÁS | Brasil | 5218300 | 52 | 33 | nan | nan | nan | Cerrado | 1.2 |
| ce82db32-3019-35eb-b8cb-65d0645438e5 | -14.17332 | -46.46943 | 2024-10-02 03:55:00 | NOAA-20 | POSSE | GOIÁS | Brasil | 5218300 | 52 | 33 | nan | nan | nan | Cerrado | 3.0 |
| 9d98228c-9aa3-3e4b-9529-a40416af0232 | -14.16899 | -46.46841 | 2024-10-02 03:55:00 | NOAA-20 | POSSE | GOIÁS | Brasil | 5218300 | 52 | 33 | nan | nan | nan | Cerrado | 1.0 |
| af3f20fe-e3e9-3122-8ce5-fcb2a86948d4 | -14.16819 | -46.47268 | 2024-10-02 03:55:00 | NOAA-20 | POSSE | GOIÁS | Brasil | 5218300 | 52 | 33 | nan | nan | nan | Cerrado | 1.0 |
| 5001eb21-119a-3104-9fc9-0a878bbec07a | -16.44818 | -46.99079 | 2024-10-02 03:55:00 | NOAA-20 | UNAÍ | MINAS GERAIS | Brasil | 3170404 | 31 | 33 | nan | nan | nan | Cerrado | 0.8 |
| 1d02c944-5052-394e-9d79-8adf15da0cac | -16.44694 | -46.99238 | 2024-10-02 03:55:00 | NOAA-20 | UNAÍ | MINAS GERAIS | Brasil | 3170404 | 31 | 33 | nan | nan | nan | Cerrado | 1.4 |
| aa045540-76d7-346e-a2fb-6b4c02514aa6 | -16.44301 | -46.99435 | 2024-10-02 03:55:00 | NOAA-20 | UNAÍ | MINAS GERAIS | Brasil | 3170404 | 31 | 33 | nan | nan | nan | Cerrado | 1.4 |
| 475d6728-1bb0-3d90-aedf-01fa8b240e14 | -16.44178 | -46.99605 | 2024-10-02 03:55:00 | NOAA-20 | UNAÍ | MINAS GERAIS | Brasil | 3170404 | 31 | 33 | nan | nan | nan | Cerrado | 1.5 |
| 96c3de49-d395-3a9a-9458-17f8bfd7044e | -16.43613 | -47.00671 | 2024-10-02 03:55:00 | NOAA-20 | UNAÍ | MINAS GERAIS | Brasil | 3170404 | 31 | 33 | nan | nan | nan | Cerrado | 1.3 |
| 36009393-cecf-3353-ab7b-9e0ab84b9824 | -16.43526 | -47.01123 | 2024-10-02 03:55:00 | NOAA-20 | UNAÍ | MINAS GERAIS | Brasil | 3170404 | 31 | 33 | nan | nan | nan | Cerrado | 1.7 |
| 43e545a0-5d05-384a-9d2d-4180653e34e3 | -16.43499 | -47.00847 | 2024-10-02 03:55:00 | NOAA-20 | UNAÍ | MINAS GERAIS | Brasil | 3170404 | 31 | 33 | nan | nan | nan | Cerrado | 3.7 |
| eac417ae-ce7f-3a17-b938-ccd9109fc8ed | -16.43176 | -47.00602 | 2024-10-02 03:55:00 | NOAA-20 | UNAÍ | MINAS GERAIS | Brasil | 3170404 | 31 | 33 | nan | nan | nan | Cerrado | 1.3 |
| d92baf99-53e8-3228-81b3-991d94d45aaa | -16.42627 | -47.00701 | 2024-10-02 03:55:00 | NOAA-20 | UNAÍ | MINAS GERAIS | Brasil | 3170404 | 31 | 33 | nan | nan | nan | Cerrado | 2.2 |
| fdf7d8a2-8055-3887-966c-2e2369de7c7c | -15.34361 | -46.73478 | 2024-10-02 03:55:00 | NOAA-20 | BURITIS | MINAS GERAIS | Brasil | 3109303 | 31 | 33 | nan | nan | nan | Cerrado | 2.9 |
| a0d187fd-f0ac-3a94-8ec6-90687f92ea3e | -15.3428 | -46.73912 | 2024-10-02 03:55:00 | NOAA-20 | BURITIS | MINAS GERAIS | Brasil | 3109303 | 31 | 33 | nan | nan | nan | Cerrado | 2.9 |
| f7cc6eb3-2665-361c-892c-93dacb1754ea | -15.33926 | -46.73396 | 2024-10-02 03:55:00 | NOAA-20 | BURITIS | MINAS GERAIS | Brasil | 3109303 | 31 | 33 | nan | nan | nan | Cerrado | 2.9 |
| 9b926abf-28fc-31bd-9fef-bbe0da109a41 | -15.33764 | -46.74263 | 2024-10-02 03:55:00 | NOAA-20 | BURITIS | MINAS GERAIS | Brasil | 3109303 | 31 | 33 | nan | nan | nan | Cerrado | 16.3 |
| 6527d07d-7ae7-345d-a779-d4d2031036a5 | -15.33683 | -46.74697 | 2024-10-02 03:55:00 | NOAA-20 | BURITIS | MINAS GERAIS | Brasil | 3109303 | 31 | 33 | nan | nan | nan | Cerrado | 16.3 |
| b241716d-28fb-3ba6-807a-68ac5da33e1b | -15.33491 | -46.73312 | 2024-10-02 03:55:00 | NOAA-20 | BURITIS | MINAS GERAIS | Brasil | 3109303 | 31 | 33 | nan | nan | nan | Cerrado | 1.9 |
| 23964875-ce0c-30c8-b95a-68e88aa76562 | -15.33328 | -46.74183 | 2024-10-02 03:55:00 | NOAA-20 | BURITIS | MINAS GERAIS | Brasil | 3109303 | 31 | 33 | nan | nan | nan | Cerrado | 1.1 |
| f38391af-b445-34ca-a780-fdb14a3c2529 | -15.3322 | -46.72356 | 2024-10-02 03:55:00 | NOAA-20 | BURITIS | MINAS GERAIS | Brasil | 3109303 | 31 | 33 | nan | nan | nan | Cerrado | 1.6 |
| 79495171-4470-39d3-b3ee-c1f03302408a | -15.33138 | -46.72792 | 2024-10-02 03:55:00 | NOAA-20 | BURITIS | MINAS GERAIS | Brasil | 3109303 | 31 | 33 | nan | nan | nan | Cerrado | 1.6 |
| 7f545815-2cc0-3361-8746-3b824da54f74 | -15.33056 | -46.7323 | 2024-10-02 03:55:00 | NOAA-20 | BURITIS | MINAS GERAIS | Brasil | 3109303 | 31 | 33 | nan | nan | nan | Cerrado | 1.9 |
| 83010735-2af2-3b3b-be3e-7ec735065ed4 | -15.32893 | -46.74103 | 2024-10-02 03:55:00 | NOAA-20 | BURITIS | MINAS GERAIS | Brasil | 3109303 | 31 | 33 | nan | nan | nan | Cerrado | 1.1 |
| f3606a64-66b3-3edb-b435-ac99b5acfbc7 | -15.32621 | -46.7315 | 2024-10-02 03:55:00 | NOAA-20 | BURITIS | MINAS GERAIS | Brasil | 3109303 | 31 | 33 | nan | nan | nan | Cerrado | 1.0 |
| 76bf7c57-31f4-3f02-9379-8bbbda80db65 | -15.32103 | -46.7351 | 2024-10-02 03:55:00 | NOAA-20 | BURITIS | MINAS GERAIS | Brasil | 3109303 | 31 | 33 | nan | nan | nan | Cerrado | 1.0 |
| 461987a4-6171-39b6-9dc5-589f91b5d02d | -18.0843 | -46.14327 | 2024-10-02 03:55:00 | NOAA-20 | PRESIDENTE OLEGÁRIO | MINAS GERAIS | Brasil | 3153400 | 31 | 33 | nan | nan | nan | Cerrado | 1.8 |
| 97924d9d-3b00-3608-967f-d96d5f8fbb67 | -18.08362 | -46.14698 | 2024-10-02 03:55:00 | NOAA-20 | PRESIDENTE OLEGÁRIO | MINAS GERAIS | Brasil | 3153400 | 31 | 33 | nan | nan | nan | Cerrado | 1.8 |
| c2f16420-30cf-327a-9298-ab4e4d705fc7 | -17.97866 | -46.62315 | 2024-10-02 03:55:00 | NOAA-20 | LAGAMAR | MINAS GERAIS | Brasil | 3137106 | 31 | 33 | nan | nan | nan | Cerrado | 1.0 |
| 963110a1-26fa-3aa1-ba02-2f8fac0a8cd2 | -17.97453 | -46.62232 | 2024-10-02 03:55:00 | NOAA-20 | LAGAMAR | MINAS GERAIS | Brasil | 3137106 | 31 | 33 | nan | nan | nan | Cerrado | 1.0 |
| 397e863a-2ce5-3763-abcd-b8b8038787a9 | -17.59233 | -46.96201 | 2024-10-02 03:55:00 | NOAA-20 | GUARDA-MOR | MINAS GERAIS | Brasil | 3128600 | 31 | 33 | nan | nan | nan | Cerrado | 1.2 |
| e76e15cd-7a6e-3a66-ad8c-75fc13f3049d | -17.52903 | -46.71929 | 2024-10-02 03:55:00 | NOAA-20 | PARACATU | MINAS GERAIS | Brasil | 3147006 | 31 | 33 | nan | nan | nan | Cerrado | 1.9 |
| 9a27d4e6-c2b1-3b2b-83a4-f970991e7423 | -17.52828 | -46.72329 | 2024-10-02 03:55:00 | NOAA-20 | PARACATU | MINAS GERAIS | Brasil | 3147006 | 31 | 33 | nan | nan | nan | Cerrado | 1.9 |
| a28dc9b0-a005-3f46-8df1-d54102cda616 | -17.48315 | -47.01061 | 2024-10-02 03:55:00 | NOAA-20 | PARACATU | MINAS GERAIS | Brasil | 3147006 | 31 | 33 | nan | nan | nan | Cerrado | 1.5 |
| b470c688-ddd3-3d57-b830-7dac2a81bd56 | -19.47706 | -46.88632 | 2024-10-02 03:55:00 | NOAA-20 | IBIÁ | MINAS GERAIS | Brasil | 3129509 | 31 | 33 | nan | nan | nan | Cerrado | 0.9 |
| f4810360-1e12-3f7f-b6f6-873d002eaa51 | -19.47227 | -46.88923 | 2024-10-02 03:55:00 | NOAA-20 | IBIÁ | MINAS GERAIS | Brasil | 3129509 | 31 | 33 | nan | nan | nan | Cerrado | 2.0 |
| e46b90a8-d8fa-362c-bcf4-74386182082f | -19.46895 | -46.88437 | 2024-10-02 03:55:00 | NOAA-20 | PERDIZES | MINAS GERAIS | Brasil | 3149804 | 31 | 33 | nan | nan | nan | Cerrado | 2.8 |
| 89ad3273-7964-3b94-8fb0-adfa68531670 | -19.23805 | -46.86198 | 2024-10-02 03:55:00 | NOAA-20 | SERRA DO SALITRE | MINAS GERAIS | Brasil | 3166808 | 31 | 33 | nan | nan | nan | Cerrado | 3.2 |
| 2191f8e5-96f6-398a-8a31-98e57303d631 | -19.23732 | -46.86584 | 2024-10-02 03:55:00 | NOAA-20 | SERRA DO SALITRE | MINAS GERAIS | Brasil | 3166808 | 31 | 33 | nan | nan | nan | Cerrado | 3.4 |
| 32bb4ebb-f6a0-39c6-bbf0-0d98f413b1d2 | -19.23659 | -46.86972 | 2024-10-02 03:55:00 | NOAA-20 | SERRA DO SALITRE | MINAS GERAIS | Brasil | 3166808 | 31 | 33 | nan | nan | nan | Cerrado | 3.4 |
| b40fb6eb-9e9e-3dd6-b0a6-e91d1fbfcd27 | -19.23396 | -46.86115 | 2024-10-02 03:55:00 | NOAA-20 | SERRA DO SALITRE | MINAS GERAIS | Brasil | 3166808 | 31 | 33 | nan | nan | nan | Cerrado | 5.7 |
| d0c54db1-0968-342e-8551-b34947564350 | -19.23323 | -46.86502 | 2024-10-02 03:55:00 | NOAA-20 | SERRA DO SALITRE | MINAS GERAIS | Brasil | 3166808 | 31 | 33 | nan | nan | nan | Cerrado | 9.3 |
| cfbe7f91-0fcc-3b9f-980b-fee61368ec06 | -19.23249 | -46.86893 | 2024-10-02 03:55:00 | NOAA-20 | SERRA DO SALITRE | MINAS GERAIS | Brasil | 3166808 | 31 | 33 | nan | nan | nan | Cerrado | 9.3 |
| 36fa10c5-d222-38a8-abed-cdb8a1e8a3aa | -19.22987 | -46.86033 | 2024-10-02 03:55:00 | NOAA-20 | SERRA DO SALITRE | MINAS GERAIS | Brasil | 3166808 | 31 | 33 | nan | nan | nan | Cerrado | 5.7 |
| 72c00388-8231-3e83-bfc8-df0a0d79b5e8 | -19.02971 | -47.52242 | 2024-10-02 03:55:00 | NOAA-20 | IRAÍ DE MINAS | MINAS GERAIS | Brasil | 3131604 | 31 | 33 | nan | nan | nan | Cerrado | 0.9 |
| 899e171e-2def-3004-9c0d-c17b2e8cdbb2 | -18.98146 | -47.29543 | 2024-10-02 03:55:00 | NOAA-20 | PATROCÍNIO | MINAS GERAIS | Brasil | 3148103 | 31 | 33 | nan | nan | nan | Cerrado | 2.3 |
| 418bc0ac-245e-3d2c-968f-33183a0f1596 | -18.96487 | -46.59626 | 2024-10-02 03:55:00 | NOAA-20 | PATOS DE MINAS | MINAS GERAIS | Brasil | 3148004 | 31 | 33 | nan | nan | nan | Cerrado | 0.7 |
| 9dc8d5fe-7aab-3d62-9b92-26f1883875fb | -18.78319 | -46.62704 | 2024-10-02 03:55:00 | NOAA-20 | PATOS DE MINAS | MINAS GERAIS | Brasil | 3148004 | 31 | 33 | nan | nan | nan | Cerrado | 1.4 |
| cb272bdd-d3be-3091-b0ef-a8e8164974b4 | -18.66735 | -47.13366 | 2024-10-02 03:55:00 | NOAA-20 | COROMANDEL | MINAS GERAIS | Brasil | 3119302 | 31 | 33 | nan | nan | nan | Cerrado | 0.8 |
| 85ec29d4-e81a-38b7-9d4b-b3637791451b | -20.96725 | -46.88511 | 2024-10-02 03:55:00 | NOAA-20 | SÃO SEBASTIÃO DO PARAÍSO | MINAS GERAIS | Brasil | 3164704 | 31 | 33 | nan | nan | nan | Cerrado | 1.0 |
| 92694243-fce3-31df-8b8a-2456286df3d0 | -20.96326 | -46.88432 | 2024-10-02 03:55:00 | NOAA-20 | SÃO SEBASTIÃO DO PARAÍSO | MINAS GERAIS | Brasil | 3164704 | 31 | 33 | nan | nan | nan | Cerrado | 1.0 |
| e8d742dd-c87d-35aa-94f6-0951485d4c5d | -20.64745 | -47.04273 | 2024-10-02 03:55:00 | NOAA-20 | CAPETINGA | MINAS GERAIS | Brasil | 3112406 | 31 | 33 | nan | nan | nan | Cerrado | 1.6 |
| 50370f76-56c9-33f9-afcb-f8b3247ba376 | -20.64674 | -47.04651 | 2024-10-02 03:55:00 | NOAA-20 | CAPETINGA | MINAS GERAIS | Brasil | 3112406 | 31 | 33 | nan | nan | nan | Cerrado | 1.8 |
| 5761647b-fb61-3528-90a9-246d09cdd736 | -20.6434 | -47.04195 | 2024-10-02 03:55:00 | NOAA-20 | CAPETINGA | MINAS GERAIS | Brasil | 3112406 | 31 | 33 | nan | nan | nan | Cerrado | 1.4 |
| 7ba3ecf3-4051-3900-85eb-b060d8b5d163 | -20.64269 | -47.04573 | 2024-10-02 03:55:00 | NOAA-20 | CAPETINGA | MINAS GERAIS | Brasil | 3112406 | 31 | 33 | nan | nan | nan | Cerrado | 0.8 |
| 506d1fe5-77bb-3fe0-b712-b88039e380c4 | -20.63127 | -46.7765 | 2024-10-02 03:55:00 | NOAA-20 | PASSOS | MINAS GERAIS | Brasil | 3147907 | 31 | 33 | nan | nan | nan | Cerrado | 2.2 |
| f10f9a6d-0935-307a-af3b-a851f9948009 | -20.63057 | -46.78016 | 2024-10-02 03:55:00 | NOAA-20 | PASSOS | MINAS GERAIS | Brasil | 3147907 | 31 | 33 | nan | nan | nan | Cerrado | 2.2 |
| be418102-34b0-3f8a-a77b-53166bf61a32 | -20.628 | -46.77197 | 2024-10-02 03:55:00 | NOAA-20 | PASSOS | MINAS GERAIS | Brasil | 3147907 | 31 | 33 | nan | nan | nan | Cerrado | 2.2 |
| dd8f1384-c88f-378e-8543-455dfd410024 | -20.62731 | -46.77561 | 2024-10-02 03:55:00 | NOAA-20 | PASSOS | MINAS GERAIS | Brasil | 3147907 | 31 | 33 | nan | nan | nan | Cerrado | 2.2 |
| b490a3e7-f3fd-3d7f-80b8-569341826c20 | -20.62626 | -46.77207 | 2024-10-02 03:55:00 | NOAA-20 | PASSOS | MINAS GERAIS | Brasil | 3147907 | 31 | 33 | nan | nan | nan | Cerrado | 1.1 |
| 4d98b959-a62c-3bba-906e-46c4f199f321 | -20.62558 | -46.77575 | 2024-10-02 03:55:00 | NOAA-20 | PASSOS | MINAS GERAIS | Brasil | 3147907 | 31 | 33 | nan | nan | nan | Cerrado | 1.1 |
| 7838473a-cb2f-3512-ade9-d345245bc087 | -20.72066 | -46.9026 | 2024-10-02 03:55:00 | NOAA-20 | CÁSSIA | MINAS GERAIS | Brasil | 3115102 | 31 | 33 | nan | nan | nan | Mata Atlântica | 1.6 |
| 3c8e177a-3028-32d4-ba0c-0304ff634a0d | -20.01075 | -47.36586 | 2024-10-02 03:55:00 | NOAA-20 | SACRAMENTO | MINAS GERAIS | Brasil | 3156908 | 31 | 33 | nan | nan | nan | Cerrado | 10.9 |
| 83aa2d4f-36d7-3bbd-8296-0e465fbf4ca8 | -19.93021 | -46.93091 | 2024-10-02 03:55:00 | NOAA-20 | TAPIRA | MINAS GERAIS | Brasil | 3168101 | 31 | 33 | nan | nan | nan | Cerrado | 1.6 |
| 44e50224-9e9e-3407-9416-8b82ec07db71 | -19.92828 | -46.91859 | 2024-10-02 03:55:00 | NOAA-20 | TAPIRA | MINAS GERAIS | Brasil | 3168101 | 31 | 33 | nan | nan | nan | Cerrado | 9.2 |
| 37bdd817-ebb7-315f-8376-a11a5a84bad5 | -19.92614 | -46.93015 | 2024-10-02 03:55:00 | NOAA-20 | TAPIRA | MINAS GERAIS | Brasil | 3168101 | 31 | 33 | nan | nan | nan | Cerrado | 0.7 |
| f39ad2fb-656d-36b4-944e-db46103833ec | -19.76273 | -46.61263 | 2024-10-02 03:55:00 | NOAA-20 | IBIÁ | MINAS GERAIS | Brasil | 3129509 | 31 | 33 | nan | nan | nan | Cerrado | 1.0 |
| 28c90792-a862-3b64-aa1a-8a2ddf389e89 | -19.76206 | -46.61623 | 2024-10-02 03:55:00 | NOAA-20 | IBIÁ | MINAS GERAIS | Brasil | 3129509 | 31 | 33 | nan | nan | nan | Cerrado | 1.0 |


[Clique aqui para ver as próximas entradas](README72.md)
