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

## Dados Diários - Página 77

| ID | Latitude | Longitude | Data/Hora GMT | Satélite | Município | Estado | País | Município ID | Estado ID | País ID | Dias sem Chuva | Precipitação | Risco de Fogo | Bioma | FRP |
|----|----------|-----------|---------------|----------|-----------|--------|------|--------------|-----------|---------|----------------|--------------|----------------|-------|-----|
| ed5cddf3-b2e8-3ed2-8c3b-4d675d6c4265 | -16.07113 | -50.44776 | 2024-10-06 04:19:00 | NOAA-20 | GOIÁS | GOIÁS | Brasil | 5208905 | 52 | 33 | nan | nan | nan | Cerrado | 6.5 |
| 3f609f2d-88d5-353f-9d12-4c881d634bb3 | -16.06746 | -50.44711 | 2024-10-06 04:19:00 | NOAA-20 | GOIÁS | GOIÁS | Brasil | 5208905 | 52 | 33 | nan | nan | nan | Cerrado | 6.5 |
| b316b982-ac95-31d1-a526-73095eb332bb | -16.12242 | -50.45718 | 2024-10-06 04:19:00 | NOAA-20 | BURITI DE GOIÁS | GOIÁS | Brasil | 5203939 | 52 | 33 | nan | nan | nan | Cerrado | 4.2 |
| bae73918-507a-3163-bd7e-acbc109533fc | -16.11356 | -50.46476 | 2024-10-06 04:19:00 | NOAA-20 | GOIÁS | GOIÁS | Brasil | 5208905 | 52 | 33 | nan | nan | nan | Cerrado | 3.2 |
| 28331c35-cda0-3003-adaa-70ee3a2de03d | -3.31822 | -50.45995 | 2024-10-06 04:19:00 | NOAA-20 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 3.3 |
| ae020f69-d94b-3492-9d93-c53be30095c4 | -3.31747 | -50.4644 | 2024-10-06 04:19:00 | NOAA-20 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 3.3 |
| 08bbd688-8cca-38d7-9a89-5799d83f4f80 | -3.31593 | -50.45708 | 2024-10-06 04:19:00 | NOAA-20 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 1.9 |
| eb5e602f-1ac6-3b05-9097-040991f4e34b | -3.31521 | -50.46161 | 2024-10-06 04:19:00 | NOAA-20 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 4.0 |
| a5df8063-b9aa-3b68-9bf0-72c07f7333bf | -3.31452 | -50.45465 | 2024-10-06 04:19:00 | NOAA-20 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 1.1 |
| b2dcf561-7a3d-377b-b5de-cfb156eeae67 | -3.3145 | -50.46603 | 2024-10-06 04:19:00 | NOAA-20 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 4.0 |
| d463e80c-9025-3d34-bd2e-eb20d85a2ff4 | -3.31376 | -50.45918 | 2024-10-06 04:19:00 | NOAA-20 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 3.1 |
| 1b2944aa-d5d1-3a03-ad2e-f9d1f3690cc6 | -3.31301 | -50.46368 | 2024-10-06 04:19:00 | NOAA-20 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 3.1 |
| b441f2d4-eaa4-3c5d-83bf-3322a038b14c | -3.31228 | -50.46807 | 2024-10-06 04:19:00 | NOAA-20 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 1.6 |
| 64353f1c-07f4-39b6-a68a-a691f9283fea | -3.31218 | -50.45187 | 2024-10-06 04:19:00 | NOAA-20 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 1.9 |
| c36eae03-38ae-3693-91cd-f7140879acc6 | -3.31147 | -50.45631 | 2024-10-06 04:19:00 | NOAA-20 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 1.9 |
| fe92d6bc-6a24-3b09-8acf-5aa376fe6ffa | -3.31079 | -50.44958 | 2024-10-06 04:19:00 | NOAA-20 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 1.1 |
| f34253ce-92ee-3b33-9445-3949708ec75f | -3.31075 | -50.46087 | 2024-10-06 04:19:00 | NOAA-20 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 4.0 |
| e794b6c7-037a-3e5a-8a00-2f925d5892e2 | -3.31005 | -50.45397 | 2024-10-06 04:19:00 | NOAA-20 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 1.1 |
| 79667f4f-c8b4-381c-9a79-4e09c5272f13 | -3.31004 | -50.46532 | 2024-10-06 04:19:00 | NOAA-20 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 4.0 |
| df2b8ace-7cb2-32a9-953b-2c253bd7098f | -3.3093 | -50.45848 | 2024-10-06 04:19:00 | NOAA-20 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 3.1 |
| cb03e455-c6eb-3e0e-9035-e0ec3f573b1e | -3.30855 | -50.46296 | 2024-10-06 04:19:00 | NOAA-20 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 3.1 |
| b3f3096c-0a86-3bf2-ab30-c5995fbf5eae | -3.30781 | -50.46736 | 2024-10-06 04:19:00 | NOAA-20 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 1.6 |
| 81439bb9-f664-312b-9b29-8d2f264d8157 | -3.30707 | -50.47177 | 2024-10-06 04:19:00 | NOAA-20 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 1.6 |
| a31d4c54-c8dd-377a-a711-a2c788ea2ced | -3.307 | -50.45567 | 2024-10-06 04:19:00 | NOAA-20 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 2.5 |
| a95d73de-3661-3328-80f9-86a323832c99 | -3.30628 | -50.46015 | 2024-10-06 04:19:00 | NOAA-20 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 1.9 |
| a99e9c39-0044-3e3f-a113-4e1e784f3c35 | -3.30558 | -50.45334 | 2024-10-06 04:19:00 | NOAA-20 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 1.7 |
| 2d1466f4-dc02-3b65-8765-3982a0ed1c2c | -3.30557 | -50.4646 | 2024-10-06 04:19:00 | NOAA-20 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 1.9 |
| 8dd7d9a0-2672-33c8-8cbc-13a7af7025ef | -3.30487 | -50.46899 | 2024-10-06 04:19:00 | NOAA-20 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 2.6 |
| 5e8c4ed2-4dad-33f3-af81-1d050b753135 | -3.30483 | -50.45781 | 2024-10-06 04:19:00 | NOAA-20 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 1.6 |
| 7af10122-8887-3a03-8119-b72cdf7dd3d4 | -3.30408 | -50.46226 | 2024-10-06 04:19:00 | NOAA-20 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 1.6 |
| 1f1e878f-e844-3f30-990d-06a6f6778947 | -3.30334 | -50.46665 | 2024-10-06 04:19:00 | NOAA-20 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 0.5 |
| e4de9db6-9cb8-32b2-9fba-c35f255485ef | -3.30261 | -50.47104 | 2024-10-06 04:19:00 | NOAA-20 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 0.5 |
| e255c9a2-d497-3145-a262-0f67a08ba2a9 | -3.30253 | -50.45498 | 2024-10-06 04:19:00 | NOAA-20 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 2.5 |
| 25cee86d-5341-33b8-9009-a0c859bfc86b | -3.30181 | -50.45944 | 2024-10-06 04:19:00 | NOAA-20 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 1.9 |
| 3565aaa1-37b0-39d1-9058-a316c94b551d | -3.30112 | -50.45262 | 2024-10-06 04:19:00 | NOAA-20 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 1.7 |
| 8a4c5b19-29db-3d43-b714-024c02d448c2 | -3.3011 | -50.46388 | 2024-10-06 04:19:00 | NOAA-20 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 1.9 |
| a27af55e-3a81-3044-ac69-4770937beb9a | -3.30037 | -50.45707 | 2024-10-06 04:19:00 | NOAA-20 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 1.6 |
| 1684b379-6584-3e8a-a8f9-2251f57a805c | -3.29962 | -50.46154 | 2024-10-06 04:19:00 | NOAA-20 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 1.6 |
| 68a508bf-a1e8-3fbf-8910-f19c534ed94f | -3.29888 | -50.46594 | 2024-10-06 04:19:00 | NOAA-20 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 0.5 |
| de70723a-9d2f-3710-afa4-b8412337c938 | -3.29807 | -50.4542 | 2024-10-06 04:19:00 | NOAA-20 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 1.9 |
| 691c85e2-6fd3-31d4-a6bc-9d6543cd2ff1 | -3.29664 | -50.46315 | 2024-10-06 04:19:00 | NOAA-20 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 3.5 |
| 20e52d5c-20f0-3187-8f18-d8754ce8f16e | -3.29362 | -50.45344 | 2024-10-06 04:19:00 | NOAA-20 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 1.9 |
| 1c65d805-8db5-33ba-b177-299f61812f54 | -3.28915 | -50.45272 | 2024-10-06 04:19:00 | NOAA-20 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 1.6 |
| 01fc56bc-b466-35cb-8dcf-c70872d55d2e | -3.21629 | -50.44996 | 2024-10-06 04:19:00 | NOAA-20 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 1.4 |
| 8c5846aa-fbb9-3d4b-9cf5-64feb09d5309 | -2.85054 | -50.46243 | 2024-10-06 04:19:00 | NOAA-20 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 4.2 |
| 05c5ff6d-46fe-3ef4-8559-64b5ccb06043 | -2.84982 | -50.46692 | 2024-10-06 04:19:00 | NOAA-20 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 16.5 |
| b75ab6ca-f499-34c5-b020-98d27bc62085 | -2.84909 | -50.47144 | 2024-10-06 04:19:00 | NOAA-20 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 16.5 |
| cc4876e7-2a08-3dda-8f7d-4185976d5a1e | -2.84532 | -50.4662 | 2024-10-06 04:19:00 | NOAA-20 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 2.4 |
| 3e187558-9e88-3b12-bec9-dab6f5cafdb5 | -3.50324 | -50.27087 | 2024-10-06 04:19:00 | NOAA-20 | PACAJÁ | PARÁ | Brasil | 1505486 | 15 | 33 | nan | nan | nan | Amazônia | 4.7 |
| 6b399a62-b26d-3437-a654-3280877077f8 | -3.50254 | -50.27514 | 2024-10-06 04:19:00 | NOAA-20 | PACAJÁ | PARÁ | Brasil | 1505486 | 15 | 33 | nan | nan | nan | Amazônia | 5.2 |
| 58ab2e4e-4e82-3b8b-9d2b-2b16d485a806 | -3.49885 | -50.27012 | 2024-10-06 04:19:00 | NOAA-20 | PACAJÁ | PARÁ | Brasil | 1505486 | 15 | 33 | nan | nan | nan | Amazônia | 7.2 |
| 0da9693c-ba3d-30b1-ba7c-bc486eed3358 | -3.49815 | -50.27439 | 2024-10-06 04:19:00 | NOAA-20 | PACAJÁ | PARÁ | Brasil | 1505486 | 15 | 33 | nan | nan | nan | Amazônia | 8.2 |
| 0acfd072-f2c2-3916-b72a-34eff5efbdc5 | -3.46556 | -50.33508 | 2024-10-06 04:19:00 | NOAA-20 | PACAJÁ | PARÁ | Brasil | 1505486 | 15 | 33 | nan | nan | nan | Amazônia | 3.2 |
| ccad3c0f-77c9-3851-86c5-bb1e00ae20f9 | -3.45008 | -50.31918 | 2024-10-06 04:19:00 | NOAA-20 | PACAJÁ | PARÁ | Brasil | 1505486 | 15 | 33 | nan | nan | nan | Amazônia | 1.7 |
| d131a843-64a6-347d-a42d-2ce9e7e42168 | -3.44936 | -50.32351 | 2024-10-06 04:19:00 | NOAA-20 | PACAJÁ | PARÁ | Brasil | 1505486 | 15 | 33 | nan | nan | nan | Amazônia | 1.7 |
| 0bf1d2a6-d6a0-3d60-9a01-4357987d8165 | -3.42629 | -50.13341 | 2024-10-06 04:19:00 | NOAA-20 | PACAJÁ | PARÁ | Brasil | 1505486 | 15 | 33 | nan | nan | nan | Amazônia | 2.7 |
| f88f7e76-9688-3904-82b2-865ff9cd1ce6 | -3.4256 | -50.13764 | 2024-10-06 04:19:00 | NOAA-20 | PACAJÁ | PARÁ | Brasil | 1505486 | 15 | 33 | nan | nan | nan | Amazônia | 2.7 |
| 5c58777e-b8f2-3607-a2e1-d41e0b489416 | -3.42522 | -50.38634 | 2024-10-06 04:19:00 | NOAA-20 | PACAJÁ | PARÁ | Brasil | 1505486 | 15 | 33 | nan | nan | nan | Amazônia | 17.8 |
| 01d96e6b-4027-341e-a3ca-1300f09f4786 | -3.4249 | -50.14193 | 2024-10-06 04:19:00 | NOAA-20 | PACAJÁ | PARÁ | Brasil | 1505486 | 15 | 33 | nan | nan | nan | Amazônia | 1.7 |
| f9787288-1c95-355e-abc3-4bf3d234ea10 | -3.42214 | -50.38264 | 2024-10-06 04:19:00 | NOAA-20 | PACAJÁ | PARÁ | Brasil | 1505486 | 15 | 33 | nan | nan | nan | Amazônia | 15.9 |
| ccdf9973-23a7-3154-b94c-7d616f8dfb52 | -3.42152 | -50.38129 | 2024-10-06 04:19:00 | NOAA-20 | PACAJÁ | PARÁ | Brasil | 1505486 | 15 | 33 | nan | nan | nan | Amazônia | 8.8 |
| 575834dc-ba2c-3cc4-92f7-34af0d514f01 | -3.42144 | -50.387 | 2024-10-06 04:19:00 | NOAA-20 | PACAJÁ | PARÁ | Brasil | 1505486 | 15 | 33 | nan | nan | nan | Amazônia | 44.2 |
| 452ef7ca-5b92-312c-8ba5-6f7521ed7ad2 | -3.42079 | -50.38564 | 2024-10-06 04:19:00 | NOAA-20 | PACAJÁ | PARÁ | Brasil | 1505486 | 15 | 33 | nan | nan | nan | Amazônia | 17.8 |
| bb13bcde-42a5-3870-bc00-caa2a0e39ad4 | -3.42006 | -50.38997 | 2024-10-06 04:19:00 | NOAA-20 | PACAJÁ | PARÁ | Brasil | 1505486 | 15 | 33 | nan | nan | nan | Amazônia | 17.8 |
| 87ad79f8-b3ac-37d1-b8f7-8f4532b44ab8 | -3.41701 | -50.38629 | 2024-10-06 04:19:00 | NOAA-20 | PACAJÁ | PARÁ | Brasil | 1505486 | 15 | 33 | nan | nan | nan | Amazônia | 2.7 |
| 99d9129f-f644-336c-9d5d-e2f960898f8c | -3.40884 | -50.38052 | 2024-10-06 04:19:00 | NOAA-20 | PACAJÁ | PARÁ | Brasil | 1505486 | 15 | 33 | nan | nan | nan | Amazônia | 3.1 |
| 3a0725e2-d896-3639-8e57-7e523343412f | -3.40813 | -50.38493 | 2024-10-06 04:19:00 | NOAA-20 | PACAJÁ | PARÁ | Brasil | 1505486 | 15 | 33 | nan | nan | nan | Amazônia | 2.2 |
| 48bd7e8d-8f74-3689-b47e-6434617d9a2f | -3.40369 | -50.38425 | 2024-10-06 04:19:00 | NOAA-20 | PACAJÁ | PARÁ | Brasil | 1505486 | 15 | 33 | nan | nan | nan | Amazônia | 2.2 |
| c28850ad-81bd-3279-bfbc-d2237b7a289e | -3.40298 | -50.38866 | 2024-10-06 04:19:00 | NOAA-20 | PACAJÁ | PARÁ | Brasil | 1505486 | 15 | 33 | nan | nan | nan | Amazônia | 2.2 |
| f955f8dc-991a-38b8-9886-a38d46f52c6c | -2.37108 | -48.95193 | 2024-10-06 04:19:00 | NOAA-20 | MOJU | PARÁ | Brasil | 1504703 | 15 | 33 | nan | nan | nan | Amazônia | 2.2 |
| aea4c2bd-138d-3e2c-b75e-e27f7c3f8f68 | -3.38632 | -49.25123 | 2024-10-06 04:19:00 | NOAA-20 | MOJU | PARÁ | Brasil | 1504703 | 15 | 33 | nan | nan | nan | Amazônia | 0.8 |
| ced67c35-b6b0-350a-9443-d85118c60944 | -3.38574 | -49.2549 | 2024-10-06 04:19:00 | NOAA-20 | MOJU | PARÁ | Brasil | 1504703 | 15 | 33 | nan | nan | nan | Amazônia | 0.8 |
| 44ca7517-c908-3ee5-9e0d-5897d69f06a5 | -3.38222 | -49.25057 | 2024-10-06 04:19:00 | NOAA-20 | MOJU | PARÁ | Brasil | 1504703 | 15 | 33 | nan | nan | nan | Amazônia | 0.5 |
| 5ceb0978-6bfb-3a79-98eb-79269994a4a4 | -3.32453 | -49.14007 | 2024-10-06 04:19:00 | NOAA-20 | MOJU | PARÁ | Brasil | 1504703 | 15 | 33 | nan | nan | nan | Amazônia | 0.9 |
| 7084f550-d3b9-3098-bdf4-ffce08f745d5 | -3.32045 | -49.1394 | 2024-10-06 04:19:00 | NOAA-20 | MOJU | PARÁ | Brasil | 1504703 | 15 | 33 | nan | nan | nan | Amazônia | 0.9 |
| 702aef0f-0fb2-3858-9b6f-85e48b2d997b | -3.31985 | -49.14303 | 2024-10-06 04:19:00 | NOAA-20 | MOJU | PARÁ | Brasil | 1504703 | 15 | 33 | nan | nan | nan | Amazônia | 1.9 |
| e976f426-d642-33df-be64-373eec954a58 | -3.31925 | -49.14666 | 2024-10-06 04:19:00 | NOAA-20 | MOJU | PARÁ | Brasil | 1504703 | 15 | 33 | nan | nan | nan | Amazônia | 1.9 |
| 12534075-f6e7-3715-80ea-3167b19856ef | -3.31577 | -49.14238 | 2024-10-06 04:19:00 | NOAA-20 | MOJU | PARÁ | Brasil | 1504703 | 15 | 33 | nan | nan | nan | Amazônia | 1.2 |
| ee025ed8-f2d5-310b-b200-a8848abdb2d8 | -3.1304 | -49.18081 | 2024-10-06 04:19:00 | NOAA-20 | MOJU | PARÁ | Brasil | 1504703 | 15 | 33 | nan | nan | nan | Amazônia | 1.2 |
| dc3f04a3-daeb-385f-9efe-409cac1ee623 | -3.12689 | -49.17649 | 2024-10-06 04:19:00 | NOAA-20 | MOJU | PARÁ | Brasil | 1504703 | 15 | 33 | nan | nan | nan | Amazônia | 0.4 |
| 89d618e4-9403-316c-93e3-d3b648c01873 | -2.87857 | -49.47683 | 2024-10-06 04:19:00 | NOAA-20 | BAIÃO | PARÁ | Brasil | 1501204 | 15 | 33 | nan | nan | nan | Amazônia | 3.3 |
| ab10e884-30fe-3d1c-914a-330fe2a8106d | -2.87437 | -49.47615 | 2024-10-06 04:19:00 | NOAA-20 | BAIÃO | PARÁ | Brasil | 1501204 | 15 | 33 | nan | nan | nan | Amazônia | 3.3 |
| 328de64d-e4d1-3e67-9496-773dbd5f1c13 | -2.82345 | -49.14717 | 2024-10-06 04:19:00 | NOAA-20 | MOJU | PARÁ | Brasil | 1504703 | 15 | 33 | nan | nan | nan | Amazônia | 1.2 |
| af824cfe-c7e9-3e5c-9052-d487b9ceedf8 | -2.80302 | -49.62094 | 2024-10-06 04:19:00 | NOAA-20 | BAIÃO | PARÁ | Brasil | 1501204 | 15 | 33 | nan | nan | nan | Amazônia | 1.6 |
| 43bbea4c-dabf-3d17-8fa0-6a5c77316f3b | -2.80237 | -49.62492 | 2024-10-06 04:19:00 | NOAA-20 | BAIÃO | PARÁ | Brasil | 1501204 | 15 | 33 | nan | nan | nan | Amazônia | 1.6 |
| eea9b878-b2a6-3e52-969b-15b9bccf05f1 | -2.79934 | -49.62149 | 2024-10-06 04:19:00 | NOAA-20 | BAIÃO | PARÁ | Brasil | 1501204 | 15 | 33 | nan | nan | nan | Amazônia | 1.4 |
| 5b7334eb-b777-3e28-9df8-08d45b701b24 | -3.34757 | -49.84385 | 2024-10-06 04:19:00 | NOAA-20 | BAIÃO | PARÁ | Brasil | 1501204 | 15 | 33 | nan | nan | nan | Amazônia | 1.9 |
| 897317b9-8c84-3e7e-8e67-62fdf64b184a | -3.32315 | -50.07509 | 2024-10-06 04:19:00 | NOAA-20 | PACAJÁ | PARÁ | Brasil | 1505486 | 15 | 33 | nan | nan | nan | Amazônia | 2.5 |
| 02ce31a4-f1d6-39b2-afd0-75d29ec3fc72 | -3.3188 | -50.0744 | 2024-10-06 04:19:00 | NOAA-20 | PACAJÁ | PARÁ | Brasil | 1505486 | 15 | 33 | nan | nan | nan | Amazônia | 2.5 |
| 110d5ced-b187-3191-81d2-ce3c92b5001e | -3.26425 | -50.13411 | 2024-10-06 04:19:00 | NOAA-20 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 2.7 |
| 579fa025-a413-37dd-bf76-a20df5018d46 | -3.26356 | -50.13831 | 2024-10-06 04:19:00 | NOAA-20 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 2.7 |
| 7eedf9ca-c2fd-3b34-9ee2-ffc477bf889c | -3.25989 | -50.13341 | 2024-10-06 04:19:00 | NOAA-20 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 2.4 |
| 3e694b21-ca14-3266-a05b-8fa2bde25cd0 | -3.25919 | -50.13761 | 2024-10-06 04:19:00 | NOAA-20 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 2.4 |
| 8509b881-0720-3d51-906d-da9056c496a4 | -3.25898 | -50.13434 | 2024-10-06 04:19:00 | NOAA-20 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 1.9 |
| 8d607182-e572-358b-a355-f1e183ce8130 | -3.25831 | -50.13856 | 2024-10-06 04:19:00 | NOAA-20 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 1.9 |
| 7244ffcc-13de-3a72-9601-d47cb65aeaa6 | -3.24424 | -50.36404 | 2024-10-06 04:19:00 | NOAA-20 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 4.5 |
| 1b329351-40f8-3e74-a15f-23fd7dfb8d63 | -3.24351 | -50.36841 | 2024-10-06 04:19:00 | NOAA-20 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 2.7 |
| db01387e-bff5-34f0-b02c-4744db08c9d5 | -3.24279 | -50.3728 | 2024-10-06 04:19:00 | NOAA-20 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 2.7 |
| 15c41458-b50a-3779-a40f-86b0a7202d47 | -3.24206 | -50.37718 | 2024-10-06 04:19:00 | NOAA-20 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 2.2 |
| f36477ba-fe51-3a23-b90b-77105d10b331 | -3.2398 | -50.36333 | 2024-10-06 04:19:00 | NOAA-20 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 2.6 |


[Clique aqui para ver as próximas entradas](README78.md)
