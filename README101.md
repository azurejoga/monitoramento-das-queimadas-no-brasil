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

## Dados Diários - Página 101

| ID | Latitude | Longitude | Data/Hora GMT | Satélite | Município | Estado | País | Município ID | Estado ID | País ID | Dias sem Chuva | Precipitação | Risco de Fogo | Bioma | FRP |
|----|----------|-----------|---------------|----------|-----------|--------|------|--------------|-----------|---------|----------------|--------------|----------------|-------|-----|
| c7578e17-a258-3c8a-b745-e98d4b4b768e | -9.4497 | -62.3485 | 2025-08-30 13:40:00 | GOES-19 | MACHADINHO D'OESTE | RONDÔNIA | Brasil | 1100130 | 11 | 33 | nan | nan | nan | Amazônia | 83.5 |
| c39662de-0b55-3093-a83f-0d369106b1db | -14.0118 | -44.5614 | 2025-08-30 13:40:00 | GOES-19 | COCOS | BAHIA | Brasil | 2908101 | 29 | 33 | nan | nan | nan | Cerrado | 162.8 |
| 12ac7bd5-4e4f-3765-86a6-4ca635a52b77 | -11.312 | -43.6428 | 2025-08-30 13:40:00 | GOES-19 | BARRA | BAHIA | Brasil | 2902708 | 29 | 33 | nan | nan | nan | Cerrado | 224.2 |
| afcbfde3-3d1f-350c-a11a-4c5538232c90 | -9.7005 | -48.3119 | 2025-08-30 13:40:00 | GOES-19 | TOCANTÍNIA | TOCANTINS | Brasil | 1721109 | 17 | 33 | nan | nan | nan | Cerrado | 84.8 |
| 3cc1dff4-bcc7-3e18-8477-a7688a578429 | -6.185 | -43.3491 | 2025-08-30 13:40:00 | GOES-19 | LAGOA DO MATO | MARANHÃO | Brasil | 2105922 | 21 | 33 | nan | nan | nan | Cerrado | 208.4 |
| e432a5ec-2a6a-3e5d-8fee-0732fabad269 | -9.1338 | -65.8067 | 2025-08-30 13:40:00 | GOES-19 | LÁBREA | AMAZONAS | Brasil | 1302405 | 13 | 33 | nan | nan | nan | Amazônia | 96.0 |
| d5112ac3-4192-310a-9f65-62d3454660c9 | -6.1665 | -43.3273 | 2025-08-30 13:40:00 | GOES-19 | LAGOA DO MATO | MARANHÃO | Brasil | 2105922 | 21 | 33 | nan | nan | nan | Cerrado | 185.5 |
| 779c9f68-2879-31d5-86b0-f7929c4be42d | -9.4498 | -62.3294 | 2025-08-30 13:40:00 | GOES-19 | MACHADINHO D'OESTE | RONDÔNIA | Brasil | 1100130 | 11 | 33 | nan | nan | nan | Amazônia | 98.2 |
| b480d78d-12a7-38ef-b2ce-1ac1b3a5a190 | -7.1108 | -44.587 | 2025-08-30 13:40:00 | GOES-19 | BENEDITO LEITE | MARANHÃO | Brasil | 2101806 | 21 | 33 | nan | nan | nan | Cerrado | 71.8 |
| 17b240b9-7d69-3157-b75b-e5073a6caf54 | -6.7814 | -43.7865 | 2025-08-30 13:40:00 | GOES-19 | GUADALUPE | PIAUÍ | Brasil | 2204501 | 22 | 33 | nan | nan | nan | Cerrado | 94.7 |
| ea92c9a2-f714-304d-b7bf-a8a0f598c94f | -11.8952 | -46.398 | 2025-08-30 13:40:00 | GOES-19 | PONTE ALTA DO BOM JESUS | TOCANTINS | Brasil | 1717800 | 17 | 33 | nan | nan | nan | Cerrado | 139.2 |
| eea428f6-a1c5-38ff-9ab5-60013b5fd356 | -7.8541 | -46.9747 | 2025-08-30 13:40:00 | GOES-19 | CAROLINA | MARANHÃO | Brasil | 2102804 | 21 | 33 | nan | nan | nan | Cerrado | 235.2 |
| c26b8001-668d-322b-9315-faa33eec1091 | -13.4986 | -46.9517 | 2025-08-30 13:40:00 | GOES-19 | MONTE ALEGRE DE GOIÁS | GOIÁS | Brasil | 5213509 | 52 | 33 | nan | nan | nan | Cerrado | 64.9 |
| b9f9c254-36ed-38a0-83b5-f33bb87d7eac | -7.2147 | -43.7001 | 2025-08-30 13:40:00 | GOES-19 | JERUMENHA | PIAUÍ | Brasil | 2205300 | 22 | 33 | nan | nan | nan | Cerrado | 108.1 |
| 5445c9b7-b0ee-369f-99a4-caee69e169c9 | -6.2096 | -42.7607 | 2025-08-30 13:40:00 | GOES-19 | AMARANTE | PIAUÍ | Brasil | 2200509 | 22 | 33 | nan | nan | nan | Caatinga | 140.8 |
| e197e6d1-ee9e-3387-83c9-e901f7880f82 | -6.944 | -46.1856 | 2025-08-30 13:40:00 | GOES-19 | FORTALEZA DOS NOGUEIRAS | MARANHÃO | Brasil | 2104107 | 21 | 33 | nan | nan | nan | Cerrado | 94.0 |
| ef634b45-dba7-332c-9993-74acdc8ec587 | -14.0313 | -44.5578 | 2025-08-30 13:40:00 | GOES-19 | COCOS | BAHIA | Brasil | 2908101 | 29 | 33 | nan | nan | nan | Cerrado | 121.3 |
| d49b8466-dd82-31ef-ac50-999a89f11b96 | -9.1156 | -65.7513 | 2025-08-30 13:40:00 | GOES-19 | LÁBREA | AMAZONAS | Brasil | 1302405 | 13 | 33 | nan | nan | nan | Amazônia | 63.3 |
| 2817a6eb-9796-3e27-8a64-b94abaf395eb | -14.0113 | -44.5849 | 2025-08-30 13:40:00 | GOES-19 | COCOS | BAHIA | Brasil | 2908101 | 29 | 33 | nan | nan | nan | Cerrado | 104.8 |
| 8acc1940-e5f4-3468-9368-60d1de7ee92c | -9.6758 | -65.0214 | 2025-08-30 13:40:00 | GOES-19 | PORTO VELHO | RONDÔNIA | Brasil | 1100205 | 11 | 33 | nan | nan | nan | Amazônia | 79.0 |
| 9dd5c743-5651-3d96-8b35-72f1d9b5649a | -9.4862 | -48.8346 | 2025-08-30 13:40:00 | GOES-19 | DOIS IRMÃOS DO TOCANTINS | TOCANTINS | Brasil | 1707207 | 17 | 33 | nan | nan | nan | Cerrado | 107.5 |
| fe93dfd7-8c8f-31b0-80ae-de06cda6b682 | -9.0799 | -65.4536 | 2025-08-30 13:40:00 | GOES-19 | LÁBREA | AMAZONAS | Brasil | 1302405 | 13 | 33 | nan | nan | nan | Amazônia | 56.6 |
| 6b5f3984-695b-3709-9f34-c3748ac54654 | -11.3517 | -43.566 | 2025-08-30 13:40:00 | GOES-19 | BARRA | BAHIA | Brasil | 2902708 | 29 | 33 | nan | nan | nan | Cerrado | 158.3 |
| b9cfe345-d10d-35b3-8637-e6a7b8cb08d4 | -6.7816 | -43.7632 | 2025-08-30 13:40:00 | GOES-19 | GUADALUPE | PIAUÍ | Brasil | 2204501 | 22 | 33 | nan | nan | nan | Cerrado | 93.5 |
| a04b6857-30ab-305c-822b-b19053e8e2d1 | -9.4679 | -48.7931 | 2025-08-30 13:50:00 | GOES-19 | MIRANORTE | TOCANTINS | Brasil | 1713304 | 17 | 33 | nan | nan | nan | Cerrado | 105.7 |
| 1e96dcc2-d757-37f7-8648-5e7b85251469 | -6.1787 | -43.9995 | 2025-08-30 13:50:00 | GOES-19 | COLINAS | MARANHÃO | Brasil | 2103505 | 21 | 33 | nan | nan | nan | Cerrado | 124.6 |
| 5d452a5e-d2b8-39b1-b022-56f3758c519b | -6.185 | -43.3491 | 2025-08-30 13:50:00 | GOES-19 | LAGOA DO MATO | MARANHÃO | Brasil | 2105922 | 21 | 33 | nan | nan | nan | Cerrado | 156.4 |
| 421a93b3-4a2c-3b41-aa1b-0247baf73cd5 | -12.6494 | -48.1731 | 2025-08-30 13:50:00 | GOES-19 | PARANÃ | TOCANTINS | Brasil | 1716208 | 17 | 33 | nan | nan | nan | Cerrado | 164.8 |
| 80819906-a6b3-36aa-945f-3c0c4b4cd365 | -9.0613 | -65.4542 | 2025-08-30 13:50:00 | GOES-19 | LÁBREA | AMAZONAS | Brasil | 1302405 | 13 | 33 | nan | nan | nan | Amazônia | 62.7 |
| 7963bbdc-d41a-3fd0-86e1-5082e9935aa2 | -7.2147 | -43.7001 | 2025-08-30 13:50:00 | GOES-19 | JERUMENHA | PIAUÍ | Brasil | 2205300 | 22 | 33 | nan | nan | nan | Cerrado | 174.9 |
| 037ecfb8-8be4-3609-a12e-56e2511617b0 | -13.3632 | -46.9727 | 2025-08-30 13:50:00 | GOES-19 | MONTE ALEGRE DE GOIÁS | GOIÁS | Brasil | 5213509 | 52 | 33 | nan | nan | nan | Cerrado | 70.3 |
| 1fbe0485-b733-3864-bd72-eff148ecb17f | -11.8952 | -46.398 | 2025-08-30 13:50:00 | GOES-19 | PONTE ALTA DO BOM JESUS | TOCANTINS | Brasil | 1717800 | 17 | 33 | nan | nan | nan | Cerrado | 131.4 |
| 641a44c4-7ffe-3916-b8b9-581622b5e935 | -6.7816 | -43.7632 | 2025-08-30 13:50:00 | GOES-19 | GUADALUPE | PIAUÍ | Brasil | 2204501 | 22 | 33 | nan | nan | nan | Cerrado | 87.7 |
| d80810ea-3e75-3b14-b189-18eb75db5e7a | -8.082 | -48.4019 | 2025-08-30 13:50:00 | GOES-19 | PALMEIRANTE | TOCANTINS | Brasil | 1715705 | 17 | 33 | nan | nan | nan | Cerrado | 83.8 |
| c8f1351a-0c39-3931-b76a-7b8bdae841aa | -14.0323 | -44.5106 | 2025-08-30 13:50:00 | GOES-19 | COCOS | BAHIA | Brasil | 2908101 | 29 | 33 | nan | nan | nan | Cerrado | 138.9 |
| 2bf686b4-c70d-3c2c-aa79-d40838ff8980 | -14.3346 | -51.873 | 2025-08-30 13:50:00 | GOES-19 | NOVA NAZARÉ | MATO GROSSO | Brasil | 5106174 | 51 | 33 | nan | nan | nan | Cerrado | 75.7 |
| 120c786d-ead0-3692-b8ae-956981aae5b4 | -10.8164 | -47.0801 | 2025-08-30 13:50:00 | GOES-19 | PONTE ALTA DO TOCANTINS | TOCANTINS | Brasil | 1717909 | 17 | 33 | nan | nan | nan | Cerrado | 366.9 |
| a7ee9bb5-4509-3a43-9bdd-21173e4d4ea1 | -6.8682 | -44.448 | 2025-08-30 13:50:00 | GOES-19 | SÃO DOMINGOS DO AZEITÃO | MARANHÃO | Brasil | 2110658 | 21 | 33 | nan | nan | nan | Cerrado | 92.2 |
| 3806cc7d-7004-3836-ac00-f324c4892dc8 | -8.0818 | -48.4237 | 2025-08-30 13:50:00 | GOES-19 | PALMEIRANTE | TOCANTINS | Brasil | 1715705 | 17 | 33 | nan | nan | nan | Cerrado | 93.7 |
| 63b908b8-4bfc-316b-9c42-b709655a3e44 | -6.1665 | -43.3273 | 2025-08-30 13:50:00 | GOES-19 | LAGOA DO MATO | MARANHÃO | Brasil | 2105922 | 21 | 33 | nan | nan | nan | Cerrado | 243.3 |
| b2f67237-5c5a-30b5-ba83-ab18c73ba26b | -6.3942 | -44.9676 | 2025-08-30 13:50:00 | GOES-19 | MIRADOR | MARANHÃO | Brasil | 2106706 | 21 | 33 | nan | nan | nan | Cerrado | 100.7 |
| 19ba55e1-0ef9-3d3b-8aae-036d4bb717d0 | -7.1959 | -43.7019 | 2025-08-30 13:50:00 | GOES-19 | LANDRI SALES | PIAUÍ | Brasil | 2205607 | 22 | 33 | nan | nan | nan | Cerrado | 170.8 |
| 9e884fa7-5033-3977-b5f1-2b07aa5701e2 | -9.1156 | -65.7513 | 2025-08-30 13:50:00 | GOES-19 | LÁBREA | AMAZONAS | Brasil | 1302405 | 13 | 33 | nan | nan | nan | Amazônia | 97.7 |
| 7dbc25ce-42d2-356d-816d-6df1e1d02bef | -13.4014 | -46.9894 | 2025-08-30 13:50:00 | GOES-19 | MONTE ALEGRE DE GOIÁS | GOIÁS | Brasil | 5213509 | 52 | 33 | nan | nan | nan | Cerrado | 77.5 |
| aba6a6df-cabc-3187-845f-0a7baa9bb540 | -9.0799 | -65.4349 | 2025-08-30 13:50:00 | GOES-19 | LÁBREA | AMAZONAS | Brasil | 1302405 | 13 | 33 | nan | nan | nan | Amazônia | 53.4 |
| 44be295e-b3a1-3a2d-9dba-364723db8964 | -9.4498 | -62.3294 | 2025-08-30 13:50:00 | GOES-19 | MACHADINHO D'OESTE | RONDÔNIA | Brasil | 1100130 | 11 | 33 | nan | nan | nan | Amazônia | 101.8 |
| 0298d064-8742-3cec-b16c-3c70df12fdb3 | -9.4862 | -48.8346 | 2025-08-30 13:50:00 | GOES-19 | DOIS IRMÃOS DO TOCANTINS | TOCANTINS | Brasil | 1707207 | 17 | 33 | nan | nan | nan | Cerrado | 81.9 |
| a991c053-e2e0-3656-b865-fbc9c4d6c008 | -13.401 | -47.012 | 2025-08-30 13:50:00 | GOES-19 | MONTE ALEGRE DE GOIÁS | GOIÁS | Brasil | 5213509 | 52 | 33 | nan | nan | nan | Cerrado | 83.3 |
| 7f44d590-c668-3fd3-aae9-3f00a1254e8a | -9.1337 | -65.8253 | 2025-08-30 13:50:00 | GOES-19 | LÁBREA | AMAZONAS | Brasil | 1302405 | 13 | 33 | nan | nan | nan | Amazônia | 95.7 |
| cb131f8a-6d26-3188-8c38-a8d41d8fd6e7 | -13.3628 | -46.9953 | 2025-08-30 13:50:00 | GOES-19 | MONTE ALEGRE DE GOIÁS | GOIÁS | Brasil | 5213509 | 52 | 33 | nan | nan | nan | Cerrado | 69.7 |
| c6b31f38-9343-39fb-b926-9fcb6cc7232c | -9.6758 | -65.0214 | 2025-08-30 13:50:00 | GOES-19 | PORTO VELHO | RONDÔNIA | Brasil | 1100205 | 11 | 33 | nan | nan | nan | Amazônia | 81.7 |
| 1f983249-6500-3b48-ba6f-b377f873b989 | -12.6686 | -48.1704 | 2025-08-30 13:50:00 | GOES-19 | PARANÃ | TOCANTINS | Brasil | 1716208 | 17 | 33 | nan | nan | nan | Cerrado | 206.1 |
| 09daeaab-8171-34fc-a292-c93b0a355b5e | -12.6682 | -48.1926 | 2025-08-30 13:50:00 | GOES-19 | PARANÃ | TOCANTINS | Brasil | 1716208 | 17 | 33 | nan | nan | nan | Cerrado | 117.9 |
| e6456424-152c-35d9-90c6-8e5fd74d3289 | -7.6033 | -42.6995 | 2025-08-30 13:50:00 | GOES-19 | FLORES DO PIAUÍ | PIAUÍ | Brasil | 2203800 | 22 | 33 | nan | nan | nan | Caatinga | 97.4 |
| fcdae647-6de5-3e1b-ab62-9d620c09d260 | -7.1108 | -44.587 | 2025-08-30 13:50:00 | GOES-19 | BENEDITO LEITE | MARANHÃO | Brasil | 2101806 | 21 | 33 | nan | nan | nan | Cerrado | 80.4 |
| c64cb9e4-4326-3ccd-bf68-8bef32b9057a | -13.4986 | -46.9517 | 2025-08-30 13:50:00 | GOES-19 | MONTE ALEGRE DE GOIÁS | GOIÁS | Brasil | 5213509 | 52 | 33 | nan | nan | nan | Cerrado | 70.4 |
| 99517fd7-b942-3409-b9f7-71948089f968 | -13.3817 | -47.015 | 2025-08-30 13:50:00 | GOES-19 | MONTE ALEGRE DE GOIÁS | GOIÁS | Brasil | 5213509 | 52 | 33 | nan | nan | nan | Cerrado | 128.8 |
| 060ec32c-297a-3456-b021-a2df935318ac | -8.8665 | -45.7335 | 2025-08-30 13:50:00 | GOES-19 | SANTA FILOMENA | PIAUÍ | Brasil | 2209203 | 22 | 33 | nan | nan | nan | Cerrado | 69.3 |
| df498c12-c813-3462-b172-5b1e4ac3d482 | -11.3705 | -43.5868 | 2025-08-30 13:50:00 | GOES-19 | BARRA | BAHIA | Brasil | 2902708 | 29 | 33 | nan | nan | nan | Cerrado | 196.2 |
| e8b2b387-6846-31ab-898c-758011f80efb | -14.3153 | -51.8756 | 2025-08-30 13:50:00 | GOES-19 | NOVA NAZARÉ | MATO GROSSO | Brasil | 5106174 | 51 | 33 | nan | nan | nan | Cerrado | 77.6 |
| 2cbdb11f-4287-37aa-94be-10b2c6e2fbbd | -9.1338 | -65.8067 | 2025-08-30 13:50:00 | GOES-19 | LÁBREA | AMAZONAS | Brasil | 1302405 | 13 | 33 | nan | nan | nan | Amazônia | 90.5 |
| 0c47adbf-35af-34e3-8021-3231eeebf3cd | -9.4684 | -62.3286 | 2025-08-30 13:50:00 | GOES-19 | MACHADINHO D'OESTE | RONDÔNIA | Brasil | 1100130 | 11 | 33 | nan | nan | nan | Amazônia | 57.5 |
| 3bc2c089-7f5a-3530-afcc-21d1d3a12fa9 | -14.0328 | -44.487 | 2025-08-30 13:50:00 | GOES-19 | COCOS | BAHIA | Brasil | 2908101 | 29 | 33 | nan | nan | nan | Cerrado | 109.2 |
| c0d2560d-8c00-386b-adc5-fedf427c3f22 | -11.0658 | -44.6137 | 2025-08-30 13:50:00 | GOES-19 | SANTA RITA DE CÁSSIA | BAHIA | Brasil | 2928406 | 29 | 33 | nan | nan | nan | Cerrado | 115.7 |
| 06623c87-9b7c-3049-a60c-d5adf4f5fbd9 | -9.0614 | -65.4355 | 2025-08-30 13:50:00 | GOES-19 | LÁBREA | AMAZONAS | Brasil | 1302405 | 13 | 33 | nan | nan | nan | Amazônia | 108.4 |
| 9316f9e3-1bbb-3288-9bdd-5783c93a0362 | -9.1524 | -65.8061 | 2025-08-30 13:50:00 | GOES-19 | LÁBREA | AMAZONAS | Brasil | 1302405 | 13 | 33 | nan | nan | nan | Amazônia | 58.5 |
| 955e3fd2-38fc-34e7-a236-3f4de1c46f1e | -6.2096 | -42.7607 | 2025-08-30 13:50:00 | GOES-19 | AMARANTE | PIAUÍ | Brasil | 2200509 | 22 | 33 | nan | nan | nan | Caatinga | 193.7 |
| 70137db4-2834-3de8-a417-ee757e2e9b3e | -11.3321 | -43.5926 | 2025-08-30 13:50:00 | GOES-19 | BARRA | BAHIA | Brasil | 2902708 | 29 | 33 | nan | nan | nan | Cerrado | 125.7 |
| 1b4fcb6e-193c-356e-97bd-cf7813822173 | -11.3517 | -43.566 | 2025-08-30 13:50:00 | GOES-19 | BARRA | BAHIA | Brasil | 2902708 | 29 | 33 | nan | nan | nan | Cerrado | 129.5 |
| 3182a1f7-2e59-326e-96ec-1ebecbb44f43 | -11.8956 | -46.3753 | 2025-08-30 13:50:00 | GOES-19 | PONTE ALTA DO BOM JESUS | TOCANTINS | Brasil | 1717800 | 17 | 33 | nan | nan | nan | Cerrado | 169.5 |
| 58563da9-188d-3712-84a0-b9bdc917c904 | -10.99 | -50.783 | 2025-08-30 13:50:00 | GOES-19 | LUCIARA | MATO GROSSO | Brasil | 5105309 | 51 | 33 | nan | nan | nan | Cerrado | 121.8 |
| a331361c-f7a9-3436-8b99-781317c228f2 | -6.7814 | -43.7865 | 2025-08-30 13:50:00 | GOES-19 | GUADALUPE | PIAUÍ | Brasil | 2204501 | 22 | 33 | nan | nan | nan | Cerrado | 97.3 |
| a51bef8f-5c1a-3630-86a7-970c83f5b9ae | -10.9897 | -50.8043 | 2025-08-30 13:50:00 | GOES-19 | LUCIARA | MATO GROSSO | Brasil | 5105309 | 51 | 33 | nan | nan | nan | Cerrado | 123.1 |
| 77fc36c6-ed8f-334d-8d47-0ad3768d8c80 | -9.1155 | -65.7699 | 2025-08-30 13:50:00 | GOES-19 | LÁBREA | AMAZONAS | Brasil | 1302405 | 13 | 33 | nan | nan | nan | Amazônia | 115.0 |
| c46b1847-79d3-306f-9847-f7f42d2036b6 | -6.1663 | -43.3506 | 2025-08-30 13:50:00 | GOES-19 | LAGOA DO MATO | MARANHÃO | Brasil | 2105922 | 21 | 33 | nan | nan | nan | Cerrado | 262.4 |
| 0e91a48a-f4e4-3cb0-bdfb-b0d3041aa7f2 | -11.312 | -43.6428 | 2025-08-30 13:50:00 | GOES-19 | BARRA | BAHIA | Brasil | 2902708 | 29 | 33 | nan | nan | nan | Cerrado | 323.3 |
| c40eb5fc-6c18-32d6-a68a-b889cbbe62c1 | -6.1853 | -43.3257 | 2025-08-30 13:50:00 | GOES-19 | LAGOA DO MATO | MARANHÃO | Brasil | 2105922 | 21 | 33 | nan | nan | nan | Cerrado | 199.2 |
| db1e34ec-b541-3292-8720-1688df7ceb00 | -14.0518 | -44.5071 | 2025-08-30 13:50:00 | GOES-19 | COCOS | BAHIA | Brasil | 2908101 | 29 | 33 | nan | nan | nan | Cerrado | 108.9 |
| 78944c0e-18ce-382a-b75d-a788b9e0edd8 | -7.6028 | -42.7468 | 2025-08-30 13:50:00 | GOES-19 | FLORES DO PIAUÍ | PIAUÍ | Brasil | 2203800 | 22 | 33 | nan | nan | nan | Caatinga | 75.1 |
| 6d11ad83-a2d6-381b-86e8-415094282e72 | -11.3709 | -43.5631 | 2025-08-30 13:50:00 | GOES-19 | BARRA | BAHIA | Brasil | 2902708 | 29 | 33 | nan | nan | nan | Cerrado | 94.5 |
| 64627da4-35ea-3a3c-ac80-7c2d3a9114d5 | -6.1785 | -44.0226 | 2025-08-30 13:50:00 | GOES-19 | COLINAS | MARANHÃO | Brasil | 2103505 | 21 | 33 | nan | nan | nan | Cerrado | 66.2 |
| 887918af-95e6-3304-a859-47cb8439ec4a | -6.8237 | -43.3402 | 2025-08-30 13:50:00 | GOES-19 | FLORIANO | PIAUÍ | Brasil | 2203909 | 22 | 33 | nan | nan | nan | Caatinga | 99.8 |
| a19140e3-fc10-3001-ac3d-db527134aba2 | -9.4497 | -62.3485 | 2025-08-30 13:50:00 | GOES-19 | MACHADINHO D'OESTE | RONDÔNIA | Brasil | 1100130 | 11 | 33 | nan | nan | nan | Amazônia | 86.8 |
| 9185f4d9-41a6-3151-a2ea-9ded805e15f9 | -11.7347 | -51.7618 | 2025-08-30 13:50:00 | GOES-19 | ALTO BOA VISTA | MATO GROSSO | Brasil | 5100359 | 51 | 33 | nan | nan | nan | Amazônia | 89.5 |
| 3ae6bf3b-56ed-371c-a202-5e2783c3f85f | -7.0951 | -44.3128 | 2025-08-30 13:50:00 | GOES-19 | BENEDITO LEITE | MARANHÃO | Brasil | 2101806 | 21 | 33 | nan | nan | nan | Cerrado | 100.7 |
| 06d4b8b5-8923-368c-8078-79aab6d2634d | -9.6986 | -47.0555 | 2025-08-30 13:50:00 | GOES-19 | LIZARDA | TOCANTINS | Brasil | 1712405 | 17 | 33 | nan | nan | nan | Cerrado | 82.4 |
| d2ba0fad-ada1-3f47-bf09-8efecfbc50d7 | -12.649 | -48.1953 | 2025-08-30 13:50:00 | GOES-19 | PARANÃ | TOCANTINS | Brasil | 1716208 | 17 | 33 | nan | nan | nan | Cerrado | 97.7 |
| f56cb7ad-8510-3889-82d0-a909a8c24b2d | -9.4433 | -60.5499 | 2025-08-30 13:50:00 | GOES-19 | ARIPUANÃ | MATO GROSSO | Brasil | 5101407 | 51 | 33 | nan | nan | nan | Amazônia | 107.8 |
| fded35f0-bf0f-3192-bcfa-37d55b0c5c36 | -7.603 | -42.7232 | 2025-08-30 13:50:00 | GOES-19 | FLORES DO PIAUÍ | PIAUÍ | Brasil | 2203800 | 22 | 33 | nan | nan | nan | Caatinga | 162.4 |
| 52dccdc8-0d74-3f74-bd5e-707f0244cc5b | -11.0849 | -44.611 | 2025-08-30 13:50:00 | GOES-19 | SANTA RITA DE CÁSSIA | BAHIA | Brasil | 2928406 | 29 | 33 | nan | nan | nan | Cerrado | 76.7 |
| f4b61399-e5b9-30bb-96b1-60aa1abb2c04 | -7.8541 | -46.9747 | 2025-08-30 13:50:00 | GOES-19 | CAROLINA | MARANHÃO | Brasil | 2102804 | 21 | 33 | nan | nan | nan | Cerrado | 89.5 |
| 1654076a-bfd4-388a-9abd-957c4c313c9f | -10.8168 | -47.0577 | 2025-08-30 13:50:00 | GOES-19 | PONTE ALTA DO TOCANTINS | TOCANTINS | Brasil | 1717909 | 17 | 33 | nan | nan | nan | Cerrado | 89.6 |
| 32cafcf7-2ee9-3f0e-b56c-a0d9aa9873ba | -10.8161 | -47.1024 | 2025-08-30 13:50:00 | GOES-19 | PONTE ALTA DO TOCANTINS | TOCANTINS | Brasil | 1717909 | 17 | 33 | nan | nan | nan | Cerrado | 199.3 |
| 83a0dd34-2ef9-3045-b445-6ae47cc9334a | -13.401 | -47.012 | 2025-08-30 14:00:00 | GOES-19 | MONTE ALEGRE DE GOIÁS | GOIÁS | Brasil | 5213509 | 52 | 33 | nan | nan | nan | Cerrado | 75.1 |
| b3bdd03c-3aa0-3c31-b75d-e2106135c8d1 | -7.092 | -44.5887 | 2025-08-30 14:00:00 | GOES-19 | BENEDITO LEITE | MARANHÃO | Brasil | 2101806 | 21 | 33 | nan | nan | nan | Cerrado | 75.6 |
| 3c5dceb3-c014-3a3c-9b12-147a8aac6282 | -10.9897 | -50.8043 | 2025-08-30 14:00:00 | GOES-19 | LUCIARA | MATO GROSSO | Brasil | 5105309 | 51 | 33 | nan | nan | nan | Cerrado | 122.7 |
| bc9afd20-7866-3b9a-bb1f-6da54c060477 | -7.5842 | -42.7251 | 2025-08-30 14:00:00 | GOES-19 | FLORES DO PIAUÍ | PIAUÍ | Brasil | 2203800 | 22 | 33 | nan | nan | nan | Caatinga | 88.9 |
| 1a77754c-a74a-3b51-8f80-a21e2aa1adbd | -13.3632 | -46.9727 | 2025-08-30 14:00:00 | GOES-19 | MONTE ALEGRE DE GOIÁS | GOIÁS | Brasil | 5213509 | 52 | 33 | nan | nan | nan | Cerrado | 77.8 |
| 5bd829b2-cdea-3bbb-af90-3af794383cea | -11.7347 | -51.7618 | 2025-08-30 14:00:00 | GOES-19 | ALTO BOA VISTA | MATO GROSSO | Brasil | 5100359 | 51 | 33 | nan | nan | nan | Amazônia | 97.9 |
| 67dfc597-4cba-3d54-86cf-ff7b589085a2 | -7.4466 | -44.8079 | 2025-08-30 14:00:00 | GOES-19 | URUÇUÍ | PIAUÍ | Brasil | 2211209 | 22 | 33 | nan | nan | nan | Cerrado | 83.2 |


[Clique aqui para ver as próximas entradas](README102.md)
