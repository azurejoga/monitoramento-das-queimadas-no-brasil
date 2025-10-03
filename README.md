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

## Dados Diários - Página 1

| ID | Latitude | Longitude | Data/Hora GMT | Satélite | Município | Estado | País | Município ID | Estado ID | País ID | Dias sem Chuva | Precipitação | Risco de Fogo | Bioma | FRP |
|----|----------|-----------|---------------|----------|-----------|--------|------|--------------|-----------|---------|----------------|--------------|----------------|-------|-----|
| 963fd38e-773d-30d4-b1e6-770f5952439e | -7.8951 | -43.5155 | 2025-10-03 00:00:00 | GOES-19 | CANAVIEIRA | PIAUÍ | Brasil | 2202251 | 22 | 33 | nan | nan | nan | Cerrado | 76.5 |
| 20074eb1-2ebc-3286-8a76-2c4919a1bc4f | -4.5712 | -46.5022 | 2025-10-03 00:00:00 | GOES-19 | BOM JESUS DAS SELVAS | MARANHÃO | Brasil | 2102036 | 21 | 33 | nan | nan | nan | Amazônia | 92.5 |
| 3ef36b4e-f111-3471-b0aa-1517e504ef66 | -6.0605 | -44.6061 | 2025-10-03 00:00:00 | GOES-19 | MIRADOR | MARANHÃO | Brasil | 2106706 | 21 | 33 | nan | nan | nan | Cerrado | 120.8 |
| e0cc34ed-5e89-36e5-805b-4a702cc0a71c | -12.6131 | -46.9725 | 2025-10-03 00:00:00 | GOES-19 | ARRAIAS | TOCANTINS | Brasil | 1702406 | 17 | 33 | nan | nan | nan | Cerrado | 167.2 |
| 34c7129a-dc3c-31a4-96cd-0268d29dfad0 | -17.8812 | -57.6206 | 2025-10-03 00:00:00 | GOES-19 | CORUMBÁ | MATO GROSSO DO SUL | Brasil | 5003207 | 50 | 33 | nan | nan | nan | Pantanal | 59.3 |
| 0f735b11-83a6-38a6-8783-1e1b811e8576 | -14.8937 | -46.9718 | 2025-10-03 00:00:00 | GOES-19 | FLORES DE GOIÁS | GOIÁS | Brasil | 5207907 | 52 | 33 | nan | nan | nan | Cerrado | 76.1 |
| b266c187-2a7c-3a9f-aa53-836920b4a966 | -6.2406 | -45.365 | 2025-10-03 00:00:00 | GOES-19 | FERNANDO FALCÃO | MARANHÃO | Brasil | 2104081 | 21 | 33 | nan | nan | nan | Cerrado | 107.9 |
| 36d511a8-2f00-39ff-82fb-0796f1107023 | -17.8614 | -57.623 | 2025-10-03 00:00:00 | GOES-19 | CORUMBÁ | MATO GROSSO DO SUL | Brasil | 5003207 | 50 | 33 | nan | nan | nan | Pantanal | 90.2 |
| f6a4f2c2-f782-3e03-a9e8-1f8867b53d43 | -5.8657 | -43.3981 | 2025-10-03 00:00:00 | GOES-19 | PARNARAMA | MARANHÃO | Brasil | 2107803 | 21 | 33 | nan | nan | nan | Cerrado | 135.4 |
| 1b8b6709-ae1a-30e7-9172-54b53f5faa9a | -5.6174 | -43.9272 | 2025-10-03 00:00:00 | GOES-19 | FORTUNA | MARANHÃO | Brasil | 2104206 | 21 | 33 | nan | nan | nan | Cerrado | 142.4 |
| 2b2d2bd7-13ef-3231-8957-3ad6f5667081 | -11.1631 | -43.4054 | 2025-10-03 00:00:00 | GOES-19 | BARRA | BAHIA | Brasil | 2902708 | 29 | 33 | nan | nan | nan | Caatinga | 99.7 |
| 73d6de8d-5134-3eba-b234-a7c3dc90703b | -4.7895 | -44.6022 | 2025-10-03 00:00:00 | GOES-19 | PEDREIRAS | MARANHÃO | Brasil | 2108207 | 21 | 33 | nan | nan | nan | Cerrado | 71.0 |
| 2a38aa62-cc7f-3e9f-8434-adf869751364 | -8.6324 | -54.9747 | 2025-10-03 00:00:00 | GOES-19 | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 66.6 |
| c0dbd387-9470-37de-8f23-f22c1474b069 | -7.2578 | -48.4699 | 2025-10-03 00:00:00 | GOES-19 | ARAGUAÍNA | TOCANTINS | Brasil | 1702109 | 17 | 33 | nan | nan | nan | Cerrado | 95.6 |
| 0b611b74-b710-33b2-9fe0-543ffe103e52 | -12.6327 | -46.9471 | 2025-10-03 00:00:00 | GOES-19 | ARRAIAS | TOCANTINS | Brasil | 1702406 | 17 | 33 | nan | nan | nan | Cerrado | 95.7 |
| 700856a3-9aaa-3359-af80-8b6a0d826b92 | -17.8617 | -57.6024 | 2025-10-03 00:00:00 | GOES-19 | CORUMBÁ | MATO GROSSO DO SUL | Brasil | 5003207 | 50 | 33 | nan | nan | nan | Pantanal | 86.7 |
| 3e3c8c08-8857-3b1f-ba6a-a1e17d5eee43 | -5.8469 | -43.3995 | 2025-10-03 00:00:00 | GOES-19 | PARNARAMA | MARANHÃO | Brasil | 2107803 | 21 | 33 | nan | nan | nan | Cerrado | 114.2 |
| aacad1bc-c285-3192-b2b3-f4ecb1226504 | -8.6139 | -54.9558 | 2025-10-03 00:00:00 | GOES-19 | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 54.2 |
| 2eaf0460-6795-3f9e-ac55-f55ad05425ff | -4.6504 | -45.8077 | 2025-10-03 00:00:00 | GOES-19 | MARAJÁ DO SENA | MARANHÃO | Brasil | 2106359 | 21 | 33 | nan | nan | nan | Amazônia | 177.7 |
| 6e9e8b83-a234-3249-ba57-84938977ddd7 | -14.9342 | -46.8965 | 2025-10-03 00:00:00 | GOES-19 | FLORES DE GOIÁS | GOIÁS | Brasil | 5207907 | 52 | 33 | nan | nan | nan | Cerrado | 114.4 |
| 137e0ab0-636c-3565-8f7d-528a90b2e77f | -13.767 | -48.0553 | 2025-10-03 00:00:00 | GOES-19 | COLINAS DO SUL | GOIÁS | Brasil | 5205521 | 52 | 33 | nan | nan | nan | Cerrado | 75.6 |
| 11e726f9-e699-31b6-9a18-cfb3104a48d9 | -5.6361 | -43.9258 | 2025-10-03 00:00:00 | GOES-19 | FORTUNA | MARANHÃO | Brasil | 2104206 | 21 | 33 | nan | nan | nan | Cerrado | 345.9 |
| 55efaa66-676b-3e2e-81f8-2814e68a43b1 | -5.655 | -43.9013 | 2025-10-03 00:00:00 | GOES-19 | BURITI BRAVO | MARANHÃO | Brasil | 2102309 | 21 | 33 | nan | nan | nan | Cerrado | 90.8 |
| 5dbd4c6d-5651-3f56-9144-912c0dbffafe | -13.7666 | -48.0777 | 2025-10-03 00:00:00 | GOES-19 | COLINAS DO SUL | GOIÁS | Brasil | 5205521 | 52 | 33 | nan | nan | nan | Cerrado | 107.0 |
| 7d3f745e-8363-31eb-88a1-07fc849c4d41 | -14.827 | -49.2893 | 2025-10-03 00:00:00 | GOES-19 | SÃO LUIZ DO NORTE | GOIÁS | Brasil | 5220157 | 52 | 33 | nan | nan | nan | Cerrado | 75.8 |
| cca973d1-364f-324f-9196-5ed59a76cac6 | -5.8467 | -43.4229 | 2025-10-03 00:00:00 | GOES-19 | PARNARAMA | MARANHÃO | Brasil | 2107803 | 21 | 33 | nan | nan | nan | Cerrado | 77.1 |
| af028700-3e29-3f30-b671-785ff7e31d34 | -6.0603 | -44.629 | 2025-10-03 00:00:00 | GOES-19 | MIRADOR | MARANHÃO | Brasil | 2106706 | 21 | 33 | nan | nan | nan | Cerrado | 130.2 |
| 148018f4-62cb-3dac-a603-48846e877707 | -4.6692 | -45.7842 | 2025-10-03 00:00:00 | GOES-19 | MARAJÁ DO SENA | MARANHÃO | Brasil | 2106359 | 21 | 33 | nan | nan | nan | Amazônia | 371.2 |
| 0f8e9bfc-82c9-37f5-985f-e39012860ead | -6.2596 | -45.341 | 2025-10-03 00:00:00 | GOES-19 | FERNANDO FALCÃO | MARANHÃO | Brasil | 2104081 | 21 | 33 | nan | nan | nan | Cerrado | 90.7 |
| 30b00007-a7df-325f-9878-7eb720beb8b9 | -14.9132 | -46.9684 | 2025-10-03 00:00:00 | GOES-19 | FLORES DE GOIÁS | GOIÁS | Brasil | 5207907 | 52 | 33 | nan | nan | nan | Cerrado | 87.1 |
| c2e51087-a03c-3a61-8eb2-108ce5d767c5 | -14.9603 | -47.5047 | 2025-10-03 00:00:00 | GOES-19 | FORMOSA | GOIÁS | Brasil | 5208004 | 52 | 33 | nan | nan | nan | Cerrado | 60.3 |
| 05c5df68-680b-32e9-9609-a6e6a9c93752 | -12.6323 | -46.9697 | 2025-10-03 00:00:00 | GOES-19 | ARRAIAS | TOCANTINS | Brasil | 1702406 | 17 | 33 | nan | nan | nan | Cerrado | 164.1 |
| b5f229e3-2cfd-3d83-9954-f132d2c33756 | -11.1252 | -43.3874 | 2025-10-03 00:00:00 | GOES-19 | BARRA | BAHIA | Brasil | 2902708 | 29 | 33 | nan | nan | nan | Caatinga | 105.3 |
| 5a9e9697-d202-3806-ab45-0760546014d7 | -9.9365 | -43.7657 | 2025-10-03 00:00:00 | GOES-19 | MORRO CABEÇA NO TEMPO | PIAUÍ | Brasil | 2206654 | 22 | 33 | nan | nan | nan | Caatinga | 110.9 |
| c138b2b9-cec8-3d1e-9b32-36beb6e870ff | -9.9178 | -43.7447 | 2025-10-03 00:00:00 | GOES-19 | MORRO CABEÇA NO TEMPO | PIAUÍ | Brasil | 2206654 | 22 | 33 | nan | nan | nan | Caatinga | 91.8 |
| 334ba4be-ea78-35cf-9c70-1d0cf1a2eed5 | -6.0418 | -44.6076 | 2025-10-03 00:00:00 | GOES-19 | MIRADOR | MARANHÃO | Brasil | 2106706 | 21 | 33 | nan | nan | nan | Cerrado | 99.9 |
| 14a5e2f0-3171-3bfb-82cf-8b2d071e1700 | -6.0416 | -44.6304 | 2025-10-03 00:00:00 | GOES-19 | MIRADOR | MARANHÃO | Brasil | 2106706 | 21 | 33 | nan | nan | nan | Cerrado | 130.8 |
| 32687605-9730-3d45-ad1c-ba7d2db58b5b | -5.8655 | -43.4214 | 2025-10-03 00:00:00 | GOES-19 | PARNARAMA | MARANHÃO | Brasil | 2107803 | 21 | 33 | nan | nan | nan | Cerrado | 89.1 |
| fe88052b-0b7c-36aa-809f-73efc75a8b22 | -7.9137 | -43.5369 | 2025-10-03 00:00:00 | GOES-19 | CANAVIEIRA | PIAUÍ | Brasil | 2202251 | 22 | 33 | nan | nan | nan | Cerrado | 199.9 |
| 48982d85-64f6-3ee0-89d7-fd8bd2b1b187 | -11.144 | -43.4082 | 2025-10-03 00:00:00 | GOES-19 | BARRA | BAHIA | Brasil | 2902708 | 29 | 33 | nan | nan | nan | Caatinga | 293.5 |
| 4042adf7-20d9-36a6-9d81-512d34ef1c32 | -5.6548 | -43.9244 | 2025-10-03 00:00:00 | GOES-19 | FORTUNA | MARANHÃO | Brasil | 2104206 | 21 | 33 | nan | nan | nan | Cerrado | 78.7 |
| 38892de0-aea4-367f-8ac1-fe11a42db48f | -4.5898 | -46.5012 | 2025-10-03 00:00:00 | GOES-19 | BOM JESUS DAS SELVAS | MARANHÃO | Brasil | 2102036 | 21 | 33 | nan | nan | nan | Amazônia | 89.4 |
| 706265e1-f18c-3ff2-b352-5df49ad60d8b | -5.6176 | -43.9041 | 2025-10-03 00:00:00 | GOES-19 | FORTUNA | MARANHÃO | Brasil | 2104206 | 21 | 33 | nan | nan | nan | Cerrado | 133.2 |
| 20559d01-d2ee-3739-9ff7-39a43e302d17 | -9.9369 | -43.7422 | 2025-10-03 00:00:00 | GOES-19 | MORRO CABEÇA NO TEMPO | PIAUÍ | Brasil | 2206654 | 22 | 33 | nan | nan | nan | Caatinga | 76.1 |
| 4fffcd2a-c112-36b1-9a16-645160d5a737 | -7.8948 | -43.5389 | 2025-10-03 00:00:00 | GOES-19 | CANAVIEIRA | PIAUÍ | Brasil | 2202251 | 22 | 33 | nan | nan | nan | Cerrado | 131.6 |
| c20a7e57-abe5-3dbf-b346-7e4d86e0f1f4 | 1.5103 | -55.8259 | 2025-10-03 00:00:00 | GOES-19 | ORIXIMINÁ | PARÁ | Brasil | 1505304 | 15 | 33 | nan | nan | nan | Amazônia | 54.1 |
| fd7d7d57-bb50-3182-814e-69dde719a15a | -9.9182 | -43.7212 | 2025-10-03 00:00:00 | GOES-19 | MORRO CABEÇA NO TEMPO | PIAUÍ | Brasil | 2206654 | 22 | 33 | nan | nan | nan | Caatinga | 71.2 |
| 8c85ea04-b6e3-3a68-9805-a6d4c061c9ad | -14.9599 | -47.5274 | 2025-10-03 00:00:00 | GOES-19 | FORMOSA | GOIÁS | Brasil | 5208004 | 52 | 33 | nan | nan | nan | Cerrado | 58.5 |
| 0b60204c-de16-3d70-a887-47b1a6bde5fd | -6.2408 | -45.3424 | 2025-10-03 00:00:00 | GOES-19 | FERNANDO FALCÃO | MARANHÃO | Brasil | 2104081 | 21 | 33 | nan | nan | nan | Cerrado | 102.1 |
| 2a037ec3-cdbd-36a6-9ba2-ca4c9d2648dd | -12.6135 | -46.9499 | 2025-10-03 00:00:00 | GOES-19 | ARRAIAS | TOCANTINS | Brasil | 1702406 | 17 | 33 | nan | nan | nan | Cerrado | 87.5 |
| a2689f21-d25e-32e5-bf0d-ef13e047f815 | -4.6505 | -45.7853 | 2025-10-03 00:00:00 | GOES-19 | MARAJÁ DO SENA | MARANHÃO | Brasil | 2106359 | 21 | 33 | nan | nan | nan | Amazônia | 250.3 |
| f0c7cfdb-6377-3614-8b6f-a9e8fe2d0d5c | -10.8608 | -46.6715 | 2025-10-03 00:00:00 | GOES-19 | MATEIROS | TOCANTINS | Brasil | 1712702 | 17 | 33 | nan | nan | nan | Cerrado | 83.9 |
| 63e1118a-c173-3934-ac3b-bdd50a92540e | -7.914 | -43.5135 | 2025-10-03 00:00:00 | GOES-19 | PAVUSSU | PIAUÍ | Brasil | 2207850 | 22 | 33 | nan | nan | nan | Cerrado | 99.6 |
| 599ff3b1-e28f-360d-9544-c4b8b546dd6e | -8.6138 | -54.976 | 2025-10-03 00:00:00 | GOES-19 | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 80.3 |
| f13715f1-0e87-3542-b052-56d201fedbfe | -5.6363 | -43.9027 | 2025-10-03 00:00:00 | GOES-19 | FORTUNA | MARANHÃO | Brasil | 2104206 | 21 | 33 | nan | nan | nan | Cerrado | 340.2 |
| 099b3899-c232-30cf-b294-e8b54d51cfce | -11.1444 | -43.3845 | 2025-10-03 00:00:00 | GOES-19 | BARRA | BAHIA | Brasil | 2902708 | 29 | 33 | nan | nan | nan | Caatinga | 230.2 |
| 338f7acc-cb7a-3bce-9f67-6740da68fc87 | -9.9175 | -43.7682 | 2025-10-03 00:00:00 | GOES-19 | MORRO CABEÇA NO TEMPO | PIAUÍ | Brasil | 2206654 | 22 | 33 | nan | nan | nan | Caatinga | 186.5 |
| eeba0bbb-6947-35d6-9cb5-d1fd690e8b3c | -6.2594 | -45.3636 | 2025-10-03 00:00:00 | GOES-19 | FERNANDO FALCÃO | MARANHÃO | Brasil | 2104081 | 21 | 33 | nan | nan | nan | Cerrado | 102.0 |
| 4ab39fee-708d-35f2-ad39-fe0d1996c314 | -11.1248 | -43.4111 | 2025-10-03 00:00:00 | GOES-19 | BARRA | BAHIA | Brasil | 2902708 | 29 | 33 | nan | nan | nan | Caatinga | 86.8 |
| a52bf0a5-cc9c-3e23-8ee8-f892d8a7bf80 | -4.669 | -45.8066 | 2025-10-03 00:00:00 | GOES-19 | MARAJÁ DO SENA | MARANHÃO | Brasil | 2106359 | 21 | 33 | nan | nan | nan | Amazônia | 349.8 |
| c894100e-2cc0-3419-a576-c10cf3c7c16f | -18.6837 | -47.823 | 2025-10-03 00:00:00 | GOES-19 | ESTRELA DO SUL | MINAS GERAIS | Brasil | 3124807 | 31 | 33 | nan | nan | nan | Cerrado | 97.6 |
| 47c81f68-d2bb-3920-88a3-960905325ba4 | -10.8611 | -46.649 | 2025-10-03 00:00:00 | GOES-19 | MATEIROS | TOCANTINS | Brasil | 1712702 | 17 | 33 | nan | nan | nan | Cerrado | 61.1 |
| 19eae38e-c147-308b-9b74-b16602e463bf | -7.2576 | -48.4915 | 2025-10-03 00:00:00 | GOES-19 | ARAGOMINAS | TOCANTINS | Brasil | 1701309 | 17 | 33 | nan | nan | nan | Cerrado | 67.5 |
| 534a634b-1e6c-358f-9f91-0835e8c16353 | -13.7769 | -47.5392 | 2025-10-03 00:00:00 | GOES-19 | CAVALCANTE | GOIÁS | Brasil | 5205307 | 52 | 33 | nan | nan | nan | Cerrado | 102.9 |
| a0cdd5ce-46ba-3c41-8867-d1a5ca73acf5 | -6.0416 | -44.6304 | 2025-10-03 00:10:00 | GOES-19 | MIRADOR | MARANHÃO | Brasil | 2106706 | 21 | 33 | nan | nan | nan | Cerrado | 126.1 |
| 84aadf35-08fb-32ec-a975-7bd6399a0f3b | -4.6505 | -45.7853 | 2025-10-03 00:10:00 | GOES-19 | MARAJÁ DO SENA | MARANHÃO | Brasil | 2106359 | 21 | 33 | nan | nan | nan | Amazônia | 322.6 |
| 4cb0e703-cf93-3bc9-bc87-6c79278a013a | -5.8469 | -43.3995 | 2025-10-03 00:10:00 | GOES-19 | PARNARAMA | MARANHÃO | Brasil | 2107803 | 21 | 33 | nan | nan | nan | Cerrado | 89.9 |
| 43ffc39b-6d2d-30f5-be38-eecdafce4bd7 | -7.8951 | -43.5155 | 2025-10-03 00:10:00 | GOES-19 | CANAVIEIRA | PIAUÍ | Brasil | 2202251 | 22 | 33 | nan | nan | nan | Cerrado | 93.1 |
| 6a06373a-5e3d-38f2-a0c8-243326cdd23c | -5.3665 | -47.2063 | 2025-10-03 00:10:00 | GOES-19 | SENADOR LA ROCQUE | MARANHÃO | Brasil | 2111763 | 21 | 33 | nan | nan | nan | Amazônia | 72.0 |
| 6f2b1b25-848b-3577-b92d-772d7e28d164 | -7.2576 | -48.4915 | 2025-10-03 00:10:00 | GOES-19 | ARAGOMINAS | TOCANTINS | Brasil | 1701309 | 17 | 33 | nan | nan | nan | Cerrado | 71.6 |
| bd0e67c3-00a2-36b3-b7db-a20f3275df88 | -14.9538 | -46.8931 | 2025-10-03 00:10:00 | GOES-19 | FLORES DE GOIÁS | GOIÁS | Brasil | 5207907 | 52 | 33 | nan | nan | nan | Cerrado | 88.0 |
| 9162e378-0e9f-37c0-a5e1-b8a47d0fa0f8 | -6.0605 | -44.6061 | 2025-10-03 00:10:00 | GOES-19 | MIRADOR | MARANHÃO | Brasil | 2106706 | 21 | 33 | nan | nan | nan | Cerrado | 111.7 |
| 829a0a9c-9630-35b4-bf36-e3806b9f6ccd | -5.3851 | -47.2052 | 2025-10-03 00:10:00 | GOES-19 | SENADOR LA ROCQUE | MARANHÃO | Brasil | 2111763 | 21 | 33 | nan | nan | nan | Amazônia | 106.6 |
| 44402c01-a884-3011-bcd9-ae5831944bd4 | -7.914 | -43.5135 | 2025-10-03 00:10:00 | GOES-19 | PAVUSSU | PIAUÍ | Brasil | 2207850 | 22 | 33 | nan | nan | nan | Cerrado | 71.2 |
| 1f347016-90ad-3369-8304-d4b6ad8fd231 | -13.1345 | -47.882 | 2025-10-03 00:10:00 | GOES-19 | PARANÃ | TOCANTINS | Brasil | 1716208 | 17 | 33 | nan | nan | nan | Cerrado | 62.9 |
| 071b7251-17e6-3375-8624-b7ac23a1cca4 | -11.1444 | -43.3845 | 2025-10-03 00:10:00 | GOES-19 | BARRA | BAHIA | Brasil | 2902708 | 29 | 33 | nan | nan | nan | Caatinga | 119.3 |
| 9242a555-198b-33a7-a7eb-309e40be54b3 | -14.9342 | -46.8965 | 2025-10-03 00:10:00 | GOES-19 | FLORES DE GOIÁS | GOIÁS | Brasil | 5207907 | 52 | 33 | nan | nan | nan | Cerrado | 125.2 |
| b6ebc4af-068f-374a-bbd9-9d7503a2927e | -14.9408 | -47.508 | 2025-10-03 00:10:00 | GOES-19 | FORMOSA | GOIÁS | Brasil | 5208004 | 52 | 33 | nan | nan | nan | Cerrado | 53.7 |
| a65901fc-9633-3012-b9c1-012468da3b80 | -8.6324 | -54.9747 | 2025-10-03 00:10:00 | GOES-19 | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 56.0 |
| cab9db1e-4969-3e55-a518-efa1f3a0ba2b | -9.9369 | -43.7422 | 2025-10-03 00:10:00 | GOES-19 | MORRO CABEÇA NO TEMPO | PIAUÍ | Brasil | 2206654 | 22 | 33 | nan | nan | nan | Caatinga | 71.3 |
| b75c9f7c-5824-3e90-aefe-7ec24f8ebedf | -7.2578 | -48.4699 | 2025-10-03 00:10:00 | GOES-19 | ARAGUAÍNA | TOCANTINS | Brasil | 1702109 | 17 | 33 | nan | nan | nan | Cerrado | 85.0 |
| 9f9db375-a778-351c-8206-61fefcc9c004 | -5.6361 | -43.9258 | 2025-10-03 00:10:00 | GOES-19 | FORTUNA | MARANHÃO | Brasil | 2104206 | 21 | 33 | nan | nan | nan | Cerrado | 309.8 |
| 73c583bf-e6a1-3dbd-817d-f09356c72e12 | -18.6837 | -47.823 | 2025-10-03 00:10:00 | GOES-19 | ESTRELA DO SUL | MINAS GERAIS | Brasil | 3124807 | 31 | 33 | nan | nan | nan | Cerrado | 71.5 |
| bbaf210f-8e5d-3971-917c-efed95c93771 | -5.8655 | -43.4214 | 2025-10-03 00:10:00 | GOES-19 | PARNARAMA | MARANHÃO | Brasil | 2107803 | 21 | 33 | nan | nan | nan | Cerrado | 89.3 |
| f4b8b0bd-4da6-39dc-8c65-e8371d8a6d33 | -7.8948 | -43.5389 | 2025-10-03 00:10:00 | GOES-19 | CANAVIEIRA | PIAUÍ | Brasil | 2202251 | 22 | 33 | nan | nan | nan | Cerrado | 170.9 |
| 96b50910-a3fb-3932-8e96-304baa7e11a7 | -8.6138 | -54.976 | 2025-10-03 00:10:00 | GOES-19 | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 84.9 |
| 7bfdc7fc-11e6-3836-94eb-0024c867e817 | -5.6174 | -43.9272 | 2025-10-03 00:10:00 | GOES-19 | FORTUNA | MARANHÃO | Brasil | 2104206 | 21 | 33 | nan | nan | nan | Cerrado | 109.7 |
| 96c9ab7f-1faa-383b-8f4f-5ec83593d872 | -17.8617 | -57.6024 | 2025-10-03 00:10:00 | GOES-19 | CORUMBÁ | MATO GROSSO DO SUL | Brasil | 5003207 | 50 | 33 | nan | nan | nan | Pantanal | 84.1 |
| c2e384f3-ce58-340e-baab-58cd51c90a32 | -6.2408 | -45.3424 | 2025-10-03 00:10:00 | GOES-19 | FERNANDO FALCÃO | MARANHÃO | Brasil | 2104081 | 21 | 33 | nan | nan | nan | Cerrado | 271.6 |
| 28a480fc-1e65-3de8-b7c3-aeb50e7c5f5c | -14.9132 | -46.9684 | 2025-10-03 00:10:00 | GOES-19 | FLORES DE GOIÁS | GOIÁS | Brasil | 5207907 | 52 | 33 | nan | nan | nan | Cerrado | 79.3 |
| 7d9d83c9-3515-3b6a-a2ec-841b7fa978b7 | -7.9137 | -43.5369 | 2025-10-03 00:10:00 | GOES-19 | CANAVIEIRA | PIAUÍ | Brasil | 2202251 | 22 | 33 | nan | nan | nan | Cerrado | 139.8 |
| 2a48e820-7e2e-3b37-b092-130e4b5cbf17 | -14.9403 | -47.5307 | 2025-10-03 00:10:00 | GOES-19 | FORMOSA | GOIÁS | Brasil | 5208004 | 52 | 33 | nan | nan | nan | Cerrado | 63.9 |
| d89101b6-f397-3986-a41a-ee743442ef72 | -9.9178 | -43.7447 | 2025-10-03 00:10:00 | GOES-19 | MORRO CABEÇA NO TEMPO | PIAUÍ | Brasil | 2206654 | 22 | 33 | nan | nan | nan | Caatinga | 72.2 |
| 7045594d-d554-3d60-b481-0739afa12b22 | -4.669 | -45.8066 | 2025-10-03 00:10:00 | GOES-19 | MARAJÁ DO SENA | MARANHÃO | Brasil | 2106359 | 21 | 33 | nan | nan | nan | Amazônia | 348.7 |
| eeb70308-fa82-307d-acca-0e9af45d0ec3 | -9.9365 | -43.7657 | 2025-10-03 00:10:00 | GOES-19 | MORRO CABEÇA NO TEMPO | PIAUÍ | Brasil | 2206654 | 22 | 33 | nan | nan | nan | Caatinga | 84.2 |
| 510e2c93-1584-3b7c-833e-eeef09607998 | -6.2406 | -45.365 | 2025-10-03 00:10:00 | GOES-19 | FERNANDO FALCÃO | MARANHÃO | Brasil | 2104081 | 21 | 33 | nan | nan | nan | Cerrado | 279.5 |
| 7e21e500-bc61-3060-b34b-d151918961e5 | -11.144 | -43.4082 | 2025-10-03 00:10:00 | GOES-19 | BARRA | BAHIA | Brasil | 2902708 | 29 | 33 | nan | nan | nan | Caatinga | 150.1 |
| fe29328d-3fd7-34e4-8e05-73954316770a | -9.9182 | -43.7212 | 2025-10-03 00:10:00 | GOES-19 | MORRO CABEÇA NO TEMPO | PIAUÍ | Brasil | 2206654 | 22 | 33 | nan | nan | nan | Caatinga | 78.1 |
| 50b9d9b8-8d4b-3acb-b60d-f7b16849ba54 | -13.7666 | -48.0777 | 2025-10-03 00:10:00 | GOES-19 | COLINAS DO SUL | GOIÁS | Brasil | 5205521 | 52 | 33 | nan | nan | nan | Cerrado | 74.8 |
| 28124597-1412-3ecf-8a08-f3584c488a1a | -12.6131 | -46.9725 | 2025-10-03 00:10:00 | GOES-19 | ARRAIAS | TOCANTINS | Brasil | 1702406 | 17 | 33 | nan | nan | nan | Cerrado | 136.0 |


[Clique aqui para ver as próximas entradas](README2.md)
