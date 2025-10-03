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

## Dados Diários - Página 124

| ID | Latitude | Longitude | Data/Hora GMT | Satélite | Município | Estado | País | Município ID | Estado ID | País ID | Dias sem Chuva | Precipitação | Risco de Fogo | Bioma | FRP |
|----|----------|-----------|---------------|----------|-----------|--------|------|--------------|-----------|---------|----------------|--------------|----------------|-------|-----|
| 49dd27a0-57f0-310c-97e6-a0f30475d506 | -13.13992 | -47.83864 | 2025-10-03 04:34:00 | NOAA-20 | PARANÃ | TOCANTINS | Brasil | 1716208 | 17 | 33 | nan | nan | nan | Cerrado | 3.2 |
| abbe36e5-ac2c-3480-8719-04f7101dd533 | -15.32374 | -46.29875 | 2025-10-03 04:34:00 | NOAA-20 | FORMOSO | MINAS GERAIS | Brasil | 3126208 | 31 | 33 | nan | nan | nan | Cerrado | 4.1 |
| d921111e-3fac-3c23-bdd6-cd3c9c5fa3a4 | -12.59794 | -47.00783 | 2025-10-03 04:34:00 | NOAA-20 | ARRAIAS | TOCANTINS | Brasil | 1702406 | 17 | 33 | nan | nan | nan | Cerrado | 6.3 |
| f534234e-23ee-3623-9d1b-29c56eb4cf3f | -12.91435 | -46.36552 | 2025-10-03 04:34:00 | NOAA-20 | CAMPOS BELOS | GOIÁS | Brasil | 5204904 | 52 | 33 | nan | nan | nan | Cerrado | 2.2 |
| 1ea0ae2a-41cd-3806-9d7e-89d6ff02ff92 | -14.40239 | -46.14654 | 2025-10-03 04:34:00 | NOAA-20 | MAMBAÍ | GOIÁS | Brasil | 5212709 | 52 | 33 | nan | nan | nan | Cerrado | 2.0 |
| 676b7b68-b049-39f2-86a2-62298b58a3d2 | -13.7653 | -48.06229 | 2025-10-03 04:34:00 | NOAA-20 | COLINAS DO SUL | GOIÁS | Brasil | 5205521 | 52 | 33 | nan | nan | nan | Cerrado | 3.5 |
| 74ddf1d9-d943-30a5-8e64-216c41a07548 | -13.19189 | -47.82379 | 2025-10-03 04:34:00 | NOAA-20 | PARANÃ | TOCANTINS | Brasil | 1716208 | 17 | 33 | nan | nan | nan | Cerrado | 2.7 |
| 7f1a2d79-281f-3045-b6ca-8f407625960c | -14.35819 | -43.84397 | 2025-10-03 04:34:00 | NOAA-20 | JUVENÍLIA | MINAS GERAIS | Brasil | 3136959 | 31 | 33 | nan | nan | nan | Cerrado | 1.0 |
| ffa9e4d3-8c89-3a6f-a4d8-10448ecbd31e | -18.33763 | -48.10871 | 2025-10-03 04:34:00 | NOAA-20 | CUMARI | GOIÁS | Brasil | 5206602 | 52 | 33 | nan | nan | nan | Cerrado | 0.6 |
| 0174f801-1f07-3449-9581-3b4dea69c35a | -13.65815 | -47.30234 | 2025-10-03 04:34:00 | NOAA-20 | TERESINA DE GOIÁS | GOIÁS | Brasil | 5221080 | 52 | 33 | nan | nan | nan | Cerrado | 2.6 |
| 31633626-d723-3a47-ae66-cad2bd3ebcec | -13.76537 | -48.08463 | 2025-10-03 04:34:00 | NOAA-20 | COLINAS DO SUL | GOIÁS | Brasil | 5205521 | 52 | 33 | nan | nan | nan | Cerrado | 1.1 |
| 1cb905b5-5d51-3015-bda3-db16111cb392 | -12.92669 | -46.38024 | 2025-10-03 04:34:00 | NOAA-20 | CAMPOS BELOS | GOIÁS | Brasil | 5204904 | 52 | 33 | nan | nan | nan | Cerrado | 2.2 |
| 888ebe63-298b-30f3-8966-f17e5bbea30d | -15.24251 | -49.29425 | 2025-10-03 04:34:00 | NOAA-20 | GOIANÉSIA | GOIÁS | Brasil | 5208608 | 52 | 33 | nan | nan | nan | Cerrado | 2.1 |
| d240634d-e120-3cab-9659-383ea35226b6 | -14.89769 | -46.84497 | 2025-10-03 04:34:00 | NOAA-20 | FLORES DE GOIÁS | GOIÁS | Brasil | 5207907 | 52 | 33 | nan | nan | nan | Cerrado | 2.9 |
| 2ab86d5b-63d1-3636-bf33-5e9766a96712 | -15.25236 | -47.91779 | 2025-10-03 04:34:00 | NOAA-20 | PLANALTINA | GOIÁS | Brasil | 5217609 | 52 | 33 | nan | nan | nan | Cerrado | 4.0 |
| 84e18caf-2b5b-3b0e-aee3-dea9d59f52a1 | -14.73353 | -50.04716 | 2025-10-03 04:34:00 | NOAA-20 | CRIXÁS | GOIÁS | Brasil | 5206404 | 52 | 33 | nan | nan | nan | Cerrado | 1.7 |
| b8984abf-41d4-347f-983e-386e206793d4 | -13.75478 | -48.07598 | 2025-10-03 04:34:00 | NOAA-20 | COLINAS DO SUL | GOIÁS | Brasil | 5205521 | 52 | 33 | nan | nan | nan | Cerrado | 6.0 |
| c6e41ff4-0eec-30fd-8f50-1d2421d6195f | -13.68261 | -48.62781 | 2025-10-03 04:34:00 | NOAA-20 | CAMPINAÇU | GOIÁS | Brasil | 5204656 | 52 | 33 | nan | nan | nan | Cerrado | 1.7 |
| 04d67fc7-5c36-3a16-9769-509a2fe204b9 | -18.22302 | -53.34605 | 2025-10-03 04:34:00 | NOAA-20 | COSTA RICA | MATO GROSSO DO SUL | Brasil | 5003256 | 50 | 33 | nan | nan | nan | Cerrado | 1.2 |
| 980f2d9a-265c-37f0-8105-5cb89a5d1d56 | -16.7643 | -43.96109 | 2025-10-03 04:34:00 | NOAA-20 | MONTES CLAROS | MINAS GERAIS | Brasil | 3143302 | 31 | 33 | nan | nan | nan | Cerrado | 1.5 |
| 82de7db9-9c7a-3c4c-9cf8-fb17eaf86bd3 | -13.1405 | -47.83485 | 2025-10-03 04:34:00 | NOAA-20 | PARANÃ | TOCANTINS | Brasil | 1716208 | 17 | 33 | nan | nan | nan | Cerrado | 2.4 |
| 47c78b28-924b-38f7-9a51-e3d35c1312f5 | -17.31603 | -49.37979 | 2025-10-03 04:34:00 | NOAA-20 | CROMÍNIA | GOIÁS | Brasil | 5206503 | 52 | 33 | nan | nan | nan | Cerrado | 0.7 |
| 20ac8a9d-1f4c-3283-8919-ecfd1470ff22 | -14.45195 | -46.3434 | 2025-10-03 04:34:00 | NOAA-20 | SÍTIO D'ABADIA | GOIÁS | Brasil | 5220702 | 52 | 33 | nan | nan | nan | Cerrado | 1.2 |
| c3db8ff6-248b-3aa3-8189-074b71c0c47f | -13.77536 | -47.52757 | 2025-10-03 04:34:00 | NOAA-20 | CAVALCANTE | GOIÁS | Brasil | 5205307 | 52 | 33 | nan | nan | nan | Cerrado | 1.9 |
| dd1d49c8-8327-3283-9a60-4d5d59d75438 | -12.379 | -46.51969 | 2025-10-03 04:34:00 | NOAA-20 | TAGUATINGA | TOCANTINS | Brasil | 1720903 | 17 | 33 | nan | nan | nan | Cerrado | 2.5 |
| 6ea71aa7-46e5-3c8c-a070-2e5ecf4286fd | -13.3316 | -47.80095 | 2025-10-03 04:34:00 | NOAA-20 | CAVALCANTE | GOIÁS | Brasil | 5205307 | 52 | 33 | nan | nan | nan | Cerrado | 1.7 |
| 82be0b3d-476d-3c11-8645-21770549f919 | -19.45491 | -44.2917 | 2025-10-03 04:34:00 | NOAA-20 | SETE LAGOAS | MINAS GERAIS | Brasil | 3167202 | 31 | 33 | nan | nan | nan | Cerrado | 1.0 |
| 307782c2-1e84-3aea-b590-da65f9cacc4d | -14.91091 | -48.65014 | 2025-10-03 04:34:00 | NOAA-20 | NIQUELÂNDIA | GOIÁS | Brasil | 5214606 | 52 | 33 | nan | nan | nan | Cerrado | 1.0 |
| 883a3686-dd72-3220-8c99-3ad95a4c92d2 | -12.72303 | -48.5803 | 2025-10-03 04:34:00 | NOAA-20 | JAÚ DO TOCANTINS | TOCANTINS | Brasil | 1711506 | 17 | 33 | nan | nan | nan | Cerrado | 3.7 |
| 11cbb2c5-e22e-3ca0-8a1c-081a3fdfac49 | -15.51164 | -45.91376 | 2025-10-03 04:34:00 | NOAA-20 | ARINOS | MINAS GERAIS | Brasil | 3104502 | 31 | 33 | nan | nan | nan | Cerrado | 2.1 |
| 906a26db-9b3a-34d9-af04-7cae9df3c5ca | -15.92231 | -43.30304 | 2025-10-03 04:34:00 | NOAA-20 | JANAÚBA | MINAS GERAIS | Brasil | 3135100 | 31 | 33 | nan | nan | nan | Cerrado | 1.8 |
| 14106748-3db0-35a1-a379-d83dbc3cbcb2 | -15.32455 | -45.05778 | 2025-10-03 04:34:00 | NOAA-20 | JANUÁRIA | MINAS GERAIS | Brasil | 3135209 | 31 | 33 | nan | nan | nan | Cerrado | 1.1 |
| 3819a3dc-2e85-3d05-98c5-724f6e3442cc | -16.6322 | -49.41362 | 2025-10-03 04:34:00 | NOAA-20 | TRINDADE | GOIÁS | Brasil | 5221403 | 52 | 33 | nan | nan | nan | Cerrado | 0.9 |
| 5997f73c-888d-3029-b835-25c6ece4d89c | -14.89414 | -46.84441 | 2025-10-03 04:34:00 | NOAA-20 | FLORES DE GOIÁS | GOIÁS | Brasil | 5207907 | 52 | 33 | nan | nan | nan | Cerrado | 2.9 |
| 7a15f5ee-2227-3fce-bb45-a5250d100be4 | -13.30462 | -47.81922 | 2025-10-03 04:34:00 | NOAA-20 | PARANÃ | TOCANTINS | Brasil | 1716208 | 17 | 33 | nan | nan | nan | Cerrado | 1.9 |
| ba5ed6e4-517e-3ea3-bf85-50a9a6d01b17 | -12.6152 | -46.96363 | 2025-10-03 04:34:00 | NOAA-20 | ARRAIAS | TOCANTINS | Brasil | 1702406 | 17 | 33 | nan | nan | nan | Cerrado | 3.3 |
| cb7d0e35-aea9-3194-91f3-5d1b36c48e07 | -18.2244 | -53.35933 | 2025-10-03 04:34:00 | NOAA-20 | ALCINÓPOLIS | MATO GROSSO DO SUL | Brasil | 5000252 | 50 | 33 | nan | nan | nan | Cerrado | 1.5 |
| e936a1cd-fd94-32bc-8386-12ffbc96cb3b | -15.99034 | -50.36793 | 2025-10-03 04:34:00 | NOAA-20 | GOIÁS | GOIÁS | Brasil | 5208905 | 52 | 33 | nan | nan | nan | Cerrado | 1.0 |
| 1b7c2bff-7e32-3136-9cd9-eb0185345e6f | -15.4897 | -45.93441 | 2025-10-03 04:34:00 | NOAA-20 | ARINOS | MINAS GERAIS | Brasil | 3104502 | 31 | 33 | nan | nan | nan | Cerrado | 3.4 |
| 8be5d03e-1fd5-3236-90e7-277724a11760 | -14.59452 | -46.72261 | 2025-10-03 04:34:00 | NOAA-20 | ALVORADA DO NORTE | GOIÁS | Brasil | 5200803 | 52 | 33 | nan | nan | nan | Cerrado | 1.9 |
| f2fc45b7-0aa7-3663-af75-2af9ef3d2a2f | -14.64188 | -48.25551 | 2025-10-03 04:34:00 | NOAA-20 | NIQUELÂNDIA | GOIÁS | Brasil | 5214606 | 52 | 33 | nan | nan | nan | Cerrado | 2.0 |
| e7887b18-8e4a-3bd7-9166-9962961f4ff3 | -15.22345 | -47.97118 | 2025-10-03 04:34:00 | NOAA-20 | PLANALTINA | GOIÁS | Brasil | 5217609 | 52 | 33 | nan | nan | nan | Cerrado | 1.7 |
| b1660248-37eb-312b-86bc-39a545322989 | -14.68497 | -48.08474 | 2025-10-03 04:34:00 | NOAA-20 | NIQUELÂNDIA | GOIÁS | Brasil | 5214606 | 52 | 33 | nan | nan | nan | Cerrado | 1.9 |
| 50ce8460-d8e9-342c-9fd3-f6ca6c27db87 | -14.97308 | -44.43626 | 2025-10-03 04:34:00 | NOAA-20 | ITACARAMBI | MINAS GERAIS | Brasil | 3132107 | 31 | 33 | nan | nan | nan | Cerrado | 0.8 |
| 496e61d9-7845-356a-8986-5bf28af45161 | -16.03627 | -50.92435 | 2025-10-03 04:34:00 | NOAA-20 | JUSSARA | GOIÁS | Brasil | 5212204 | 52 | 33 | nan | nan | nan | Cerrado | 2.6 |
| a2930dfa-8154-319b-b329-0157cb4ecd7f | -18.15888 | -53.33741 | 2025-10-03 04:34:00 | NOAA-20 | ALCINÓPOLIS | MATO GROSSO DO SUL | Brasil | 5000252 | 50 | 33 | nan | nan | nan | Cerrado | 1.3 |
| 06ad1811-9a27-3e03-bf30-105e88babec5 | -18.26199 | -53.30872 | 2025-10-03 04:34:00 | NOAA-20 | COSTA RICA | MATO GROSSO DO SUL | Brasil | 5003256 | 50 | 33 | nan | nan | nan | Cerrado | 1.1 |
| 1ecf3229-488f-3471-b57a-46a86803bd2e | -14.7426 | -48.12413 | 2025-10-03 04:34:00 | NOAA-20 | NIQUELÂNDIA | GOIÁS | Brasil | 5214606 | 52 | 33 | nan | nan | nan | Cerrado | 5.0 |
| a036fd19-0153-3881-bf7a-1ec6b79f088a | -13.33903 | -50.93222 | 2025-10-03 04:34:00 | NOAA-20 | COCALINHO | MATO GROSSO | Brasil | 5103106 | 51 | 33 | nan | nan | nan | Cerrado | 0.7 |
| eebc135d-eee2-3ba7-82d7-01cf288f9230 | -14.46466 | -48.40061 | 2025-10-03 04:34:00 | NOAA-20 | NIQUELÂNDIA | GOIÁS | Brasil | 5214606 | 52 | 33 | nan | nan | nan | Cerrado | 4.4 |
| e1a58786-b87b-372a-ac07-269a8efa5ed8 | -14.00617 | -44.97272 | 2025-10-03 04:34:00 | NOAA-20 | JABORANDI | BAHIA | Brasil | 2917359 | 29 | 33 | nan | nan | nan | Cerrado | 1.1 |
| 3764198b-03bd-335e-a959-7207dc69d369 | -14.66487 | -48.26309 | 2025-10-03 04:34:00 | NOAA-20 | NIQUELÂNDIA | GOIÁS | Brasil | 5214606 | 52 | 33 | nan | nan | nan | Cerrado | 4.1 |
| c2f329c9-2e45-33f9-9304-40227ad07b38 | -13.77204 | -47.54981 | 2025-10-03 04:34:00 | NOAA-20 | CAVALCANTE | GOIÁS | Brasil | 5205307 | 52 | 33 | nan | nan | nan | Cerrado | 2.2 |
| a62f8295-04b9-3707-8e67-8bfcb7a240d6 | -13.2321 | -48.49395 | 2025-10-03 04:34:00 | NOAA-20 | MINAÇU | GOIÁS | Brasil | 5213087 | 52 | 33 | nan | nan | nan | Cerrado | 1.5 |
| ae4e512b-a9de-383d-98c7-e2c027457098 | -12.6189 | -47.00177 | 2025-10-03 04:34:00 | NOAA-20 | ARRAIAS | TOCANTINS | Brasil | 1702406 | 17 | 33 | nan | nan | nan | Cerrado | 5.5 |
| 9a8fe043-528d-3b48-b824-7c196c714213 | -12.37375 | -46.53102 | 2025-10-03 04:34:00 | NOAA-20 | TAGUATINGA | TOCANTINS | Brasil | 1720903 | 17 | 33 | nan | nan | nan | Cerrado | 2.1 |
| 647bca3b-d199-35e4-bc79-a98af8168745 | -15.52669 | -46.81026 | 2025-10-03 04:34:00 | NOAA-20 | BURITIS | MINAS GERAIS | Brasil | 3109303 | 31 | 33 | nan | nan | nan | Cerrado | 1.3 |
| 1b6b4d56-0e3a-3a63-a180-cc40e4aaa10c | -14.91606 | -48.34454 | 2025-10-03 04:34:00 | NOAA-20 | MIMOSO DE GOIÁS | GOIÁS | Brasil | 5213053 | 52 | 33 | nan | nan | nan | Cerrado | 4.4 |
| 68d98f14-dbd0-358b-8aee-1f089d283134 | -13.76702 | -51.27311 | 2025-10-03 04:34:00 | NOAA-20 | COCALINHO | MATO GROSSO | Brasil | 5103106 | 51 | 33 | nan | nan | nan | Cerrado | 2.3 |
| 68adf094-5f32-3a55-8680-634ca9e661cd | -12.59968 | -49.901 | 2025-10-03 04:34:00 | NOAA-20 | SANDOLÂNDIA | TOCANTINS | Brasil | 1718840 | 17 | 33 | nan | nan | nan | Cerrado | 1.8 |
| eb9fec69-a3c1-3c39-ab89-c2bb1eb04ad9 | -15.31518 | -46.38702 | 2025-10-03 04:34:00 | NOAA-20 | BURITIS | MINAS GERAIS | Brasil | 3109303 | 31 | 33 | nan | nan | nan | Cerrado | 3.1 |
| dd5efb83-9402-3bb6-8305-c4c9bff4f4e9 | -13.78118 | -47.55877 | 2025-10-03 04:34:00 | NOAA-20 | CAVALCANTE | GOIÁS | Brasil | 5205307 | 52 | 33 | nan | nan | nan | Cerrado | 3.2 |
| 0424fcb1-520b-34a3-85ab-f1048c48f8b4 | -13.35271 | -48.08026 | 2025-10-03 04:34:00 | NOAA-20 | CAVALCANTE | GOIÁS | Brasil | 5205307 | 52 | 33 | nan | nan | nan | Cerrado | 0.5 |
| b079feb6-9412-36ef-aee2-8f938a8f6ca9 | -13.34955 | -47.33401 | 2025-10-03 04:34:00 | NOAA-20 | MONTE ALEGRE DE GOIÁS | GOIÁS | Brasil | 5213509 | 52 | 33 | nan | nan | nan | Cerrado | 1.8 |
| 0dd3ffbf-60ad-30e6-a1e2-2bd2e1a8dd4f | -13.21551 | -47.8275 | 2025-10-03 04:34:00 | NOAA-20 | PARANÃ | TOCANTINS | Brasil | 1716208 | 17 | 33 | nan | nan | nan | Cerrado | 1.4 |
| 2f2a5381-a272-3d87-b89e-77f3fa6cb7fa | -13.77139 | -47.53078 | 2025-10-03 04:34:00 | NOAA-20 | CAVALCANTE | GOIÁS | Brasil | 5205307 | 52 | 33 | nan | nan | nan | Cerrado | 4.4 |
| b016375f-3e3d-3293-9f98-e0d37330c842 | -14.43966 | -46.12067 | 2025-10-03 04:34:00 | NOAA-20 | MAMBAÍ | GOIÁS | Brasil | 5212709 | 52 | 33 | nan | nan | nan | Cerrado | 2.8 |
| b8064b5e-86fd-3366-b7d0-3a330fe002fa | -14.66703 | -48.08896 | 2025-10-03 04:34:00 | NOAA-20 | NIQUELÂNDIA | GOIÁS | Brasil | 5214606 | 52 | 33 | nan | nan | nan | Cerrado | 5.3 |
| 14aee7ce-4bfe-37e4-8b71-eb15f55b7119 | -15.48514 | -45.93106 | 2025-10-03 04:34:00 | NOAA-20 | ARINOS | MINAS GERAIS | Brasil | 3104502 | 31 | 33 | nan | nan | nan | Cerrado | 1.4 |
| d961ab8d-72fd-37a3-af93-1e730ce59ee6 | -14.91493 | -48.32912 | 2025-10-03 04:34:00 | NOAA-20 | MIMOSO DE GOIÁS | GOIÁS | Brasil | 5213053 | 52 | 33 | nan | nan | nan | Cerrado | 3.0 |
| a6c9443a-90dd-31ea-8ca2-b3e6916add98 | -15.94744 | -43.34509 | 2025-10-03 04:34:00 | NOAA-20 | JANAÚBA | MINAS GERAIS | Brasil | 3135100 | 31 | 33 | nan | nan | nan | Cerrado | 1.1 |
| a67f94c7-e468-3adf-a240-2507767a61ec | -13.82757 | -48.03832 | 2025-10-03 04:34:00 | NOAA-20 | COLINAS DO SUL | GOIÁS | Brasil | 5205521 | 52 | 33 | nan | nan | nan | Cerrado | 2.2 |
| 818447f1-80b9-3f9c-90a4-3f5e0013a4f6 | -13.68182 | -48.03431 | 2025-10-03 04:34:00 | NOAA-20 | CAVALCANTE | GOIÁS | Brasil | 5205307 | 52 | 33 | nan | nan | nan | Cerrado | 3.3 |
| 29e0101d-92bb-3a84-b979-841d96d19d8b | -12.89703 | -46.89766 | 2025-10-03 04:34:00 | NOAA-20 | ARRAIAS | TOCANTINS | Brasil | 1702406 | 17 | 33 | nan | nan | nan | Cerrado | 0.8 |
| fd365f8a-6229-3946-99c1-41d9f67c4add | -15.70296 | -46.25433 | 2025-10-03 04:34:00 | NOAA-20 | ARINOS | MINAS GERAIS | Brasil | 3104502 | 31 | 33 | nan | nan | nan | Cerrado | 0.7 |
| d7a3c7bf-86c0-3de9-9c0d-a9aa426c8c81 | -16.01704 | -50.85768 | 2025-10-03 04:34:00 | NOAA-20 | FAZENDA NOVA | GOIÁS | Brasil | 5207600 | 52 | 33 | nan | nan | nan | Cerrado | 2.0 |
| 8778b70a-a989-30a5-a5a0-8e3786642c60 | -15.35998 | -47.06528 | 2025-10-03 04:34:00 | NOAA-20 | FORMOSA | GOIÁS | Brasil | 5208004 | 52 | 33 | nan | nan | nan | Cerrado | 1.3 |
| 8ddb6227-8e66-3fdc-97f5-b6120e780331 | -12.62918 | -46.97996 | 2025-10-03 04:34:00 | NOAA-20 | ARRAIAS | TOCANTINS | Brasil | 1702406 | 17 | 33 | nan | nan | nan | Cerrado | 12.3 |
| 163a597c-50bf-3e3d-bb0f-b49e2236ddcf | -18.45124 | -43.81062 | 2025-10-03 04:34:00 | NOAA-20 | GOUVEIA | MINAS GERAIS | Brasil | 3127602 | 31 | 33 | nan | nan | nan | Cerrado | 2.9 |
| cf38f9de-2c10-31f1-8beb-ca5672de7957 | -15.25023 | -50.12967 | 2025-10-03 04:34:00 | NOAA-20 | FAINA | GOIÁS | Brasil | 5207535 | 52 | 33 | nan | nan | nan | Cerrado | 1.7 |
| 8404a973-e2db-3f04-a8d7-f56c6e4b3c00 | -13.35838 | -48.13325 | 2025-10-03 04:34:00 | NOAA-20 | CAVALCANTE | GOIÁS | Brasil | 5205307 | 52 | 33 | nan | nan | nan | Cerrado | 0.7 |
| de042235-e86b-3744-b728-b3a20800d323 | -14.90422 | -48.2975 | 2025-10-03 04:34:00 | NOAA-20 | MIMOSO DE GOIÁS | GOIÁS | Brasil | 5213053 | 52 | 33 | nan | nan | nan | Cerrado | 2.8 |
| f202ec3c-3e64-397e-b6de-014366d09a46 | -12.53211 | -47.30439 | 2025-10-03 04:34:00 | NOAA-20 | PARANÃ | TOCANTINS | Brasil | 1716208 | 17 | 33 | nan | nan | nan | Cerrado | 0.5 |
| 1b0fbc02-6bf3-39f6-903c-62736cc30c50 | -12.68508 | -48.58495 | 2025-10-03 04:34:00 | NOAA-20 | JAÚ DO TOCANTINS | TOCANTINS | Brasil | 1711506 | 17 | 33 | nan | nan | nan | Cerrado | 1.5 |
| 9c151172-5786-3ee9-9319-02f1687cbb68 | -15.28863 | -46.38984 | 2025-10-03 04:34:00 | NOAA-20 | BURITIS | MINAS GERAIS | Brasil | 3109303 | 31 | 33 | nan | nan | nan | Cerrado | 1.4 |
| 565e703b-e610-3c2b-9513-d64a73be6266 | -13.33094 | -47.59895 | 2025-10-03 04:34:00 | NOAA-20 | CAVALCANTE | GOIÁS | Brasil | 5205307 | 52 | 33 | nan | nan | nan | Cerrado | 3.0 |
| 9ff39b77-29d0-33e1-a16a-d2c1d76e9fa2 | -18.34111 | -48.10926 | 2025-10-03 04:34:00 | NOAA-20 | CUMARI | GOIÁS | Brasil | 5206602 | 52 | 33 | nan | nan | nan | Cerrado | 1.3 |
| 12713771-667d-35a3-9e79-887b228a9361 | -15.10401 | -43.4713 | 2025-10-03 04:34:00 | NOAA-20 | JAÍBA | MINAS GERAIS | Brasil | 3135050 | 31 | 33 | nan | nan | nan | Caatinga | 1.0 |
| b909c825-f675-3d82-a88a-6db205984f48 | -14.98291 | -46.85431 | 2025-10-03 04:34:00 | NOAA-20 | FLORES DE GOIÁS | GOIÁS | Brasil | 5207907 | 52 | 33 | nan | nan | nan | Cerrado | 1.2 |
| 88fe29b4-fcf2-34a3-a865-f144658d088b | -13.13641 | -47.89401 | 2025-10-03 04:34:00 | NOAA-20 | PARANÃ | TOCANTINS | Brasil | 1716208 | 17 | 33 | nan | nan | nan | Cerrado | 2.0 |
| e46d21b9-1362-36df-a1e2-5202ab8ca04b | -13.19364 | -47.85776 | 2025-10-03 04:34:00 | NOAA-20 | PARANÃ | TOCANTINS | Brasil | 1716208 | 17 | 33 | nan | nan | nan | Cerrado | 1.4 |
| 46aae258-730f-3a32-bdc2-6287e786be88 | -12.63198 | -46.96101 | 2025-10-03 04:34:00 | NOAA-20 | ARRAIAS | TOCANTINS | Brasil | 1702406 | 17 | 33 | nan | nan | nan | Cerrado | 1.1 |
| b1afb282-607d-3830-b006-a14b19787ce7 | -14.41577 | -46.15733 | 2025-10-03 04:34:00 | NOAA-20 | MAMBAÍ | GOIÁS | Brasil | 5212709 | 52 | 33 | nan | nan | nan | Cerrado | 1.2 |
| cdf31839-2226-3360-9cde-ffe98a9d4396 | -12.6812 | -48.5443 | 2025-10-03 04:34:00 | NOAA-20 | JAÚ DO TOCANTINS | TOCANTINS | Brasil | 1711506 | 17 | 33 | nan | nan | nan | Cerrado | 2.3 |
| e6a5ff27-5eaf-3de6-b978-eade3c9b736a | -14.3294 | -45.87043 | 2025-10-03 04:34:00 | NOAA-20 | JABORANDI | BAHIA | Brasil | 2917359 | 29 | 33 | nan | nan | nan | Cerrado | 1.7 |
| 26ef18f5-9d50-36e5-b2cf-9d91d8c37783 | -18.20529 | -53.36443 | 2025-10-03 04:34:00 | NOAA-20 | COSTA RICA | MATO GROSSO DO SUL | Brasil | 5003256 | 50 | 33 | nan | nan | nan | Cerrado | 1.4 |
| 0870542d-a8e8-30f8-9ecd-a048ba2127f8 | -14.64823 | -46.82213 | 2025-10-03 04:34:00 | NOAA-20 | FLORES DE GOIÁS | GOIÁS | Brasil | 5207907 | 52 | 33 | nan | nan | nan | Cerrado | 0.7 |
| 61d7114f-f7ea-3481-ae2c-8ca5c00a3f93 | -14.69743 | -43.88708 | 2025-10-03 04:34:00 | NOAA-20 | MATIAS CARDOSO | MINAS GERAIS | Brasil | 3140852 | 31 | 33 | nan | nan | nan | Caatinga | 5.9 |
| d5ea465f-effd-32d0-ae43-a4ee42838b1d | -14.90647 | -48.32796 | 2025-10-03 04:34:00 | NOAA-20 | MIMOSO DE GOIÁS | GOIÁS | Brasil | 5213053 | 52 | 33 | nan | nan | nan | Cerrado | 1.4 |
| 55743166-705d-3bf8-afc1-5c16368d43dc | -12.62911 | -46.95646 | 2025-10-03 04:34:00 | NOAA-20 | ARRAIAS | TOCANTINS | Brasil | 1702406 | 17 | 33 | nan | nan | nan | Cerrado | 1.8 |


[Clique aqui para ver as próximas entradas](README125.md)
