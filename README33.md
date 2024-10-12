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

## Dados Diários - Página 33

| ID | Latitude | Longitude | Data/Hora GMT | Satélite | Município | Estado | País | Município ID | Estado ID | País ID | Dias sem Chuva | Precipitação | Risco de Fogo | Bioma | FRP |
|----|----------|-----------|---------------|----------|-----------|--------|------|--------------|-----------|---------|----------------|--------------|----------------|-------|-----|
| 81cbfd44-9c48-33df-993c-d38619b21bc3 | -4.82851 | -37.83649 | 2024-10-12 03:15:00 | NOAA-21 | JAGUARUANA | CEARÁ | Brasil | 2307007 | 23 | 33 | nan | nan | nan | Caatinga | 1.2 |
| 4d8ce1a1-499c-3661-8efa-8a19260b6f1c | -3.71091 | -40.70498 | 2024-10-12 03:15:00 | NOAA-21 | COREAÚ | CEARÁ | Brasil | 2304004 | 23 | 33 | nan | nan | nan | Caatinga | 2.8 |
| a941fcb2-c0b0-336d-b593-4758f896e131 | -2.7884 | -51.3825 | 2024-10-12 03:15:22 | GOES-16 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 63.9 |
| cf48b609-b36a-3538-9664-eb9af8b1f2dc | -2.7885 | -51.3618 | 2024-10-12 03:15:22 | GOES-16 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 99.4 |
| 7c2af875-8b1f-3351-a5c4-405611ae7769 | -2.807 | -51.3406 | 2024-10-12 03:15:22 | GOES-16 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 54.0 |
| cf52465a-2b09-3f18-8985-e48eac8c1e7d | -2.8254 | -51.3401 | 2024-10-12 03:15:22 | GOES-16 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 59.3 |
| 44d2d8d8-8995-3612-89ac-fa55b15bc119 | -2.7701 | -51.3622 | 2024-10-12 03:15:22 | GOES-16 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 60.9 |
| 7311f56f-9fc2-3078-8d94-adaa524b98e3 | -3.6978 | -50.1225 | 2024-10-12 03:15:27 | GOES-16 | PACAJÁ | PARÁ | Brasil | 1505486 | 15 | 33 | nan | nan | nan | Amazônia | 77.0 |
| 781318f7-f02a-30c1-ab53-be8a0a5a64e4 | -3.6979 | -50.1015 | 2024-10-12 03:15:27 | GOES-16 | PACAJÁ | PARÁ | Brasil | 1505486 | 15 | 33 | nan | nan | nan | Amazônia | 44.3 |
| c9d6b1d5-6afb-30dc-9ec7-e09f60617f9a | -3.7163 | -50.1219 | 2024-10-12 03:15:27 | GOES-16 | PACAJÁ | PARÁ | Brasil | 1505486 | 15 | 33 | nan | nan | nan | Amazônia | 47.6 |
| decd4d4a-5da2-3ef4-b1ad-bbe4c8567f59 | -3.9394 | -46.445 | 2024-10-12 03:15:29 | GOES-16 | BOM JARDIM | MARANHÃO | Brasil | 2102002 | 21 | 33 | nan | nan | nan | Amazônia | 93.6 |
| 78122611-7969-3063-aed7-a9c2c1880964 | -3.9396 | -46.4229 | 2024-10-12 03:15:29 | GOES-16 | BOM JARDIM | MARANHÃO | Brasil | 2102002 | 21 | 33 | nan | nan | nan | Amazônia | 68.2 |
| 882f9a36-e503-389a-8441-20256f8bd11e | -3.958 | -46.4442 | 2024-10-12 03:15:29 | GOES-16 | BOM JARDIM | MARANHÃO | Brasil | 2102002 | 21 | 33 | nan | nan | nan | Amazônia | 34.9 |
| 0fa3fbae-6f7d-3f38-8845-8f46e45103d2 | -4.1148 | -48.2515 | 2024-10-12 03:15:30 | GOES-16 | DOM ELISEU | PARÁ | Brasil | 1502939 | 15 | 33 | nan | nan | nan | Amazônia | 38.8 |
| 2016b522-42d9-31c5-9b35-11557eef1eff | -4.2665 | -50.9594 | 2024-10-12 03:15:31 | GOES-16 | PACAJÁ | PARÁ | Brasil | 1505486 | 15 | 33 | nan | nan | nan | Amazônia | 57.2 |
| 571b20fa-67d1-384f-96b0-ded318cb2585 | -5.2486 | -48.0424 | 2024-10-12 03:15:36 | GOES-16 | VILA NOVA DOS MARTÍRIOS | MARANHÃO | Brasil | 2112852 | 21 | 33 | nan | nan | nan | Cerrado | 56.0 |
| 9f9243ef-9194-3aa0-87b3-ed496ceb6404 | -5.3997 | -45.3574 | 2024-10-12 03:15:37 | GOES-16 | BARRA DO CORDA | MARANHÃO | Brasil | 2101608 | 21 | 33 | nan | nan | nan | Cerrado | 111.2 |
| dd145090-521e-3ead-a4d9-4f949cf1a195 | -6.0791 | -44.6276 | 2024-10-12 03:15:41 | GOES-16 | MIRADOR | MARANHÃO | Brasil | 2106706 | 21 | 33 | nan | nan | nan | Cerrado | 58.9 |
| c991c045-4f24-3d3e-bc8d-026789453cdb | -6.7469 | -59.3452 | 2024-10-12 03:15:45 | GOES-16 | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 61.7 |
| b5783e90-6a00-3a74-bcb5-9f6df051173d | -6.747 | -59.3259 | 2024-10-12 03:15:45 | GOES-16 | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 104.7 |
| 99228554-1301-3fb8-b24c-74c3171fb1c8 | -7.8529 | -54.7027 | 2024-10-12 03:15:51 | GOES-16 | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 57.5 |
| 40c05464-4b86-38b0-bd3f-2090755ec50a | -7.8713 | -54.7217 | 2024-10-12 03:15:51 | GOES-16 | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 98.6 |
| 1e99e58a-9139-3efd-894d-c597ef6a7c94 | -7.8715 | -54.7016 | 2024-10-12 03:15:51 | GOES-16 | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 132.8 |
| ee8131ba-f1b5-35cf-9823-b4d2d0548995 | -7.8717 | -54.6814 | 2024-10-12 03:15:51 | GOES-16 | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 51.9 |
| 2b9dc899-9675-3dc0-b0dc-66ede9df7aae | -7.89 | -54.7206 | 2024-10-12 03:15:51 | GOES-16 | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 67.0 |
| fb2c4fcf-deb3-3f6a-a154-ed7d1011392d | -7.8901 | -54.7004 | 2024-10-12 03:15:51 | GOES-16 | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 72.0 |
| f9dbd2d0-83bb-3dad-927c-256680955a29 | -11.8377 | -58.8445 | 2024-10-12 03:16:14 | GOES-16 | JUÍNA | MATO GROSSO | Brasil | 5105150 | 51 | 33 | nan | nan | nan | Cerrado | 76.9 |
| 766d3d68-ffdb-3619-944a-b227fc97f3c4 | -12.4367 | -54.5778 | 2024-10-12 03:16:17 | GOES-16 | FELIZ NATAL | MATO GROSSO | Brasil | 5103700 | 51 | 33 | nan | nan | nan | Amazônia | 51.8 |
| 428a86b1-1e0a-37d8-ba55-6e958ee9980f | -12.437 | -54.5573 | 2024-10-12 03:16:17 | GOES-16 | FELIZ NATAL | MATO GROSSO | Brasil | 5103700 | 51 | 33 | nan | nan | nan | Amazônia | 55.4 |
| 0527e4b8-ae98-3ff5-b74a-836c3317914b | -12.4558 | -54.576 | 2024-10-12 03:16:17 | GOES-16 | FELIZ NATAL | MATO GROSSO | Brasil | 5103700 | 51 | 33 | nan | nan | nan | Amazônia | 50.6 |
| f3914476-d2b1-3665-8fc7-537ffe716d23 | -12.456 | -54.5554 | 2024-10-12 03:16:17 | GOES-16 | FELIZ NATAL | MATO GROSSO | Brasil | 5103700 | 51 | 33 | nan | nan | nan | Amazônia | 54.8 |
| 2254413d-052d-3e0c-b57d-3f1e0617d282 | -12.9461 | -53.5548 | 2024-10-12 03:16:20 | GOES-16 | GAÚCHA DO NORTE | MATO GROSSO | Brasil | 5103858 | 51 | 33 | nan | nan | nan | Amazônia | 119.4 |
| 0618cca8-e9a6-3617-bc50-bf71d15b42a9 | -12.9464 | -53.5339 | 2024-10-12 03:16:20 | GOES-16 | GAÚCHA DO NORTE | MATO GROSSO | Brasil | 5103858 | 51 | 33 | nan | nan | nan | Amazônia | 425.0 |
| 453f0ac4-6ef3-32f3-a6d3-17e2e5644d23 | -12.9467 | -53.5131 | 2024-10-12 03:16:20 | GOES-16 | GAÚCHA DO NORTE | MATO GROSSO | Brasil | 5103858 | 51 | 33 | nan | nan | nan | Amazônia | 218.5 |
| 87190812-6ae1-36b4-9d25-0ce5891f2b69 | -12.9652 | -53.5527 | 2024-10-12 03:16:20 | GOES-16 | GAÚCHA DO NORTE | MATO GROSSO | Brasil | 5103858 | 51 | 33 | nan | nan | nan | Amazônia | 115.7 |
| 5ba73fdc-83c3-3627-a27e-03699be1b6ea | -12.9655 | -53.5319 | 2024-10-12 03:16:20 | GOES-16 | GAÚCHA DO NORTE | MATO GROSSO | Brasil | 5103858 | 51 | 33 | nan | nan | nan | Amazônia | 320.2 |
| 23cb322d-05a3-337a-8097-976d9d81ccb2 | -12.9658 | -53.511 | 2024-10-12 03:16:20 | GOES-16 | GAÚCHA DO NORTE | MATO GROSSO | Brasil | 5103858 | 51 | 33 | nan | nan | nan | Amazônia | 163.5 |
| c65de398-b9ba-3a4b-8c52-6ae0f91ffadb | -14.3246 | -57.6002 | 2024-10-12 03:16:27 | GOES-16 | NOVA MARILÂNDIA | MATO GROSSO | Brasil | 5108857 | 51 | 33 | nan | nan | nan | Amazônia | 70.0 |
| 43511294-5a3d-3988-8556-587de1bf97e0 | -14.3249 | -57.58 | 2024-10-12 03:16:27 | GOES-16 | NOVA MARILÂNDIA | MATO GROSSO | Brasil | 5108857 | 51 | 33 | nan | nan | nan | Amazônia | 54.0 |
| fc558d5c-49f3-3ede-bc14-4805ee529289 | -14.8101 | -54.6289 | 2024-10-12 03:16:30 | GOES-16 | NOVA BRASILÂNDIA | MATO GROSSO | Brasil | 5106208 | 51 | 33 | nan | nan | nan | Cerrado | 56.9 |
| fe59e88a-726e-354d-bbe1-363cf2b4e0df | -17.0426 | -56.0333 | 2024-10-12 03:16:42 | GOES-16 | BARÃO DE MELGAÇO | MATO GROSSO | Brasil | 5101605 | 51 | 33 | nan | nan | nan | Pantanal | 47.1 |
| 2ed7a490-1038-3424-a375-af872981238f | -16.9805 | -57.4404 | 2024-10-12 03:16:42 | GOES-16 | CÁCERES | MATO GROSSO | Brasil | 5102504 | 51 | 33 | nan | nan | nan | Pantanal | 67.7 |
| c58122b6-2323-3342-a57a-993b985b03bd | -17.1761 | -57.4585 | 2024-10-12 03:16:43 | GOES-16 | CÁCERES | MATO GROSSO | Brasil | 5102504 | 51 | 33 | nan | nan | nan | Pantanal | 84.4 |
| 8b265b98-9c1f-3f62-85a8-41d1f22c00f6 | -17.1758 | -57.479 | 2024-10-12 03:16:43 | GOES-16 | CÁCERES | MATO GROSSO | Brasil | 5102504 | 51 | 33 | nan | nan | nan | Pantanal | 61.6 |
| 6674d6af-508b-3e46-bf48-16a94c2b22bd | -17.964 | -57.3843 | 2024-10-12 03:16:47 | GOES-16 | CORUMBÁ | MATO GROSSO DO SUL | Brasil | 5003207 | 50 | 33 | nan | nan | nan | Pantanal | 44.6 |
| 81624ffe-7195-336d-b269-8c1353ceaace | -18.1758 | -56.5509 | 2024-10-12 03:16:48 | GOES-16 | CORUMBÁ | MATO GROSSO DO SUL | Brasil | 5003207 | 50 | 33 | nan | nan | nan | Pantanal | 67.6 |
| 03d06987-b876-3891-9dc0-1ab96e3d208e | -18.1762 | -56.5301 | 2024-10-12 03:16:48 | GOES-16 | CORUMBÁ | MATO GROSSO DO SUL | Brasil | 5003207 | 50 | 33 | nan | nan | nan | Pantanal | 43.5 |
| 6b68fb0a-6c2c-3cf0-ac2b-13fc2aa23c20 | -18.1956 | -56.5483 | 2024-10-12 03:16:48 | GOES-16 | CORUMBÁ | MATO GROSSO DO SUL | Brasil | 5003207 | 50 | 33 | nan | nan | nan | Pantanal | 177.0 |
| 2268aef7-acaa-37f4-9943-993117faf7d1 | -18.196 | -56.5275 | 2024-10-12 03:16:48 | GOES-16 | CORUMBÁ | MATO GROSSO DO SUL | Brasil | 5003207 | 50 | 33 | nan | nan | nan | Pantanal | 114.8 |
| 01812ccf-d940-32ff-8213-0c3528da5d09 | -18.2155 | -56.5457 | 2024-10-12 03:16:48 | GOES-16 | CORUMBÁ | MATO GROSSO DO SUL | Brasil | 5003207 | 50 | 33 | nan | nan | nan | Pantanal | 79.3 |
| afb97202-45f7-32f6-a3df-b2847c7fa464 | -18.2158 | -56.5249 | 2024-10-12 03:16:48 | GOES-16 | CORUMBÁ | MATO GROSSO DO SUL | Brasil | 5003207 | 50 | 33 | nan | nan | nan | Pantanal | 82.3 |
| b7804b43-c69a-384a-b887-4b14a4e8aaf6 | -7.16371 | -41.41066 | 2024-10-12 03:17:00 | NOAA-21 | GEMINIANO | PIAUÍ | Brasil | 2204352 | 22 | 33 | nan | nan | nan | Caatinga | 7.2 |
| 314620a3-bc6d-3d47-b465-c6be71be5cb9 | -7.16323 | -41.41202 | 2024-10-12 03:17:00 | NOAA-21 | GEMINIANO | PIAUÍ | Brasil | 2204352 | 22 | 33 | nan | nan | nan | Caatinga | 6.2 |
| c7a4ba1f-2a05-30b7-a040-0bb64f37ce29 | -7.09119 | -39.93361 | 2024-10-12 03:17:00 | NOAA-21 | POTENGI | CEARÁ | Brasil | 2311207 | 23 | 33 | nan | nan | nan | Caatinga | 1.9 |
| 2f759a0d-611b-332a-98aa-79f1aeaef2ce | -7.08521 | -39.93274 | 2024-10-12 03:17:00 | NOAA-21 | POTENGI | CEARÁ | Brasil | 2311207 | 23 | 33 | nan | nan | nan | Caatinga | 1.9 |
| b0597367-8ff0-384e-8654-9cc6bf576de3 | -7.06405 | -38.78586 | 2024-10-12 03:17:00 | NOAA-21 | BARRO | CEARÁ | Brasil | 2302008 | 23 | 33 | nan | nan | nan | Caatinga | 2.5 |
| 7eeea7c8-1e9b-3ecb-bf8c-b79bba55448f | -7.06273 | -39.72176 | 2024-10-12 03:17:00 | NOAA-21 | NOVA OLINDA | CEARÁ | Brasil | 2309201 | 23 | 33 | nan | nan | nan | Caatinga | 1.8 |
| 1c85b954-80cf-3cd8-bb8b-c04c3188aeee | -6.60878 | -37.94266 | 2024-10-12 03:17:00 | NOAA-21 | LAGOA | PARAÍBA | Brasil | 2508109 | 25 | 33 | nan | nan | nan | Caatinga | 3.6 |
| a7546af3-9016-3f75-939f-e76a4cca9b2b | -6.60854 | -37.94035 | 2024-10-12 03:17:00 | NOAA-21 | LAGOA | PARAÍBA | Brasil | 2508109 | 25 | 33 | nan | nan | nan | Caatinga | 1.6 |
| fbfbab34-5652-37a8-b58f-7186e9ae849c | -6.60823 | -37.94585 | 2024-10-12 03:17:00 | NOAA-21 | LAGOA | PARAÍBA | Brasil | 2508109 | 25 | 33 | nan | nan | nan | Caatinga | 3.6 |
| 302c4e15-1310-35ca-97fc-516ab7a3398b | -6.60794 | -37.94371 | 2024-10-12 03:17:00 | NOAA-21 | LAGOA | PARAÍBA | Brasil | 2508109 | 25 | 33 | nan | nan | nan | Caatinga | 4.1 |
| 9f45c646-c844-3dc1-b6bf-242a03281038 | -6.60739 | -37.94674 | 2024-10-12 03:17:00 | NOAA-21 | LAGOA | PARAÍBA | Brasil | 2508109 | 25 | 33 | nan | nan | nan | Caatinga | 4.1 |
| ba7c942b-52a5-311d-ab4a-f96a1ecb6a62 | -6.60334 | -37.94269 | 2024-10-12 03:17:00 | NOAA-21 | LAGOA | PARAÍBA | Brasil | 2508109 | 25 | 33 | nan | nan | nan | Caatinga | 2.0 |
| b03c9c2a-d47e-35c6-97fd-b9442e11d7e6 | -6.60306 | -37.94062 | 2024-10-12 03:17:00 | NOAA-21 | LAGOA | PARAÍBA | Brasil | 2508109 | 25 | 33 | nan | nan | nan | Caatinga | 1.1 |
| c0506b14-e020-316d-b939-bb9adf3a62cd | -6.51729 | -39.69063 | 2024-10-12 03:17:00 | NOAA-21 | JUCÁS | CEARÁ | Brasil | 2307403 | 23 | 33 | nan | nan | nan | Caatinga | 1.9 |
| 3b871fb7-282e-34a9-afd8-45e05944d5e1 | -6.51339 | -39.69136 | 2024-10-12 03:17:00 | NOAA-21 | JUCÁS | CEARÁ | Brasil | 2307403 | 23 | 33 | nan | nan | nan | Caatinga | 4.0 |
| a9464ab2-f245-3336-b695-4c7c570aecd8 | -6.51139 | -39.68948 | 2024-10-12 03:17:00 | NOAA-21 | JUCÁS | CEARÁ | Brasil | 2307403 | 23 | 33 | nan | nan | nan | Caatinga | 2.6 |
| df283e55-33d2-3a16-a6a2-9b34e8450452 | -6.44907 | -38.8201 | 2024-10-12 03:17:00 | NOAA-21 | ICÓ | CEARÁ | Brasil | 2305407 | 23 | 33 | nan | nan | nan | Caatinga | 0.8 |
| 4576ea3d-b1cd-338b-8bab-21aaee1bc70d | -6.44344 | -38.81924 | 2024-10-12 03:17:00 | NOAA-21 | ICÓ | CEARÁ | Brasil | 2305407 | 23 | 33 | nan | nan | nan | Caatinga | 1.4 |
| e0143286-7b3d-3239-bee1-965b2d8f825d | -5.63897 | -40.6978 | 2024-10-12 03:17:00 | NOAA-21 | NOVO ORIENTE | CEARÁ | Brasil | 2309409 | 23 | 33 | nan | nan | nan | Caatinga | 2.2 |
| 5cf8abdd-ab9a-3d48-9ace-ad243813d9df | -5.3727 | -37.77914 | 2024-10-12 03:17:00 | NOAA-21 | APODI | RIO GRANDE DO NORTE | Brasil | 2401008 | 24 | 33 | nan | nan | nan | Caatinga | 1.1 |
| 1bf8a33c-a00c-3498-b370-40d26baf2e15 | -5.37212 | -37.78247 | 2024-10-12 03:17:00 | NOAA-21 | APODI | RIO GRANDE DO NORTE | Brasil | 2401008 | 24 | 33 | nan | nan | nan | Caatinga | 1.1 |
| 6a6b252c-5487-3cd0-93df-0d5b1cec2de3 | -5.36739 | -37.77819 | 2024-10-12 03:17:00 | NOAA-21 | APODI | RIO GRANDE DO NORTE | Brasil | 2401008 | 24 | 33 | nan | nan | nan | Caatinga | 0.8 |
| 1e019c57-9a7b-380d-a93f-a5a46da7a3ae | -5.21307 | -37.88532 | 2024-10-12 03:17:00 | NOAA-21 | LIMOEIRO DO NORTE | CEARÁ | Brasil | 2307601 | 23 | 33 | nan | nan | nan | Caatinga | 1.4 |
| 776da70a-3d99-323a-bd8c-8bd455803b0d | -5.21039 | -37.8847 | 2024-10-12 03:17:00 | NOAA-21 | LIMOEIRO DO NORTE | CEARÁ | Brasil | 2307601 | 23 | 33 | nan | nan | nan | Caatinga | 1.9 |
| 382bcc1a-1c0b-311f-9827-49c91758372f | -10.05993 | -38.55389 | 2024-10-12 03:17:00 | NOAA-21 | JEREMOABO | BAHIA | Brasil | 2918100 | 29 | 33 | nan | nan | nan | Caatinga | 2.4 |
| 2049c2da-0a11-3fdc-8af4-ec9366af10d0 | -9.80101 | -36.48942 | 2024-10-12 03:17:00 | NOAA-21 | LIMOEIRO DE ANADIA | ALAGOAS | Brasil | 2704203 | 27 | 33 | nan | nan | nan | Mata Atlântica | 0.9 |
| 6d621fed-f890-3097-ae93-70ba321daa7e | -9.80017 | -36.49406 | 2024-10-12 03:17:00 | NOAA-21 | LIMOEIRO DE ANADIA | ALAGOAS | Brasil | 2704203 | 27 | 33 | nan | nan | nan | Mata Atlântica | 1.5 |
| 378b78ca-544e-3de1-ad0b-298df3021763 | -9.79926 | -36.49144 | 2024-10-12 03:17:00 | NOAA-21 | LIMOEIRO DE ANADIA | ALAGOAS | Brasil | 2704203 | 27 | 33 | nan | nan | nan | Mata Atlântica | 4.6 |
| 84fdf00a-9f8e-3494-9056-d6ad797186d0 | -9.79846 | -36.49608 | 2024-10-12 03:17:00 | NOAA-21 | LIMOEIRO DE ANADIA | ALAGOAS | Brasil | 2704203 | 27 | 33 | nan | nan | nan | Mata Atlântica | 3.9 |
| 2686e190-05e4-373d-8f56-e8b39057100f | -9.79565 | -36.49323 | 2024-10-12 03:17:00 | NOAA-21 | LIMOEIRO DE ANADIA | ALAGOAS | Brasil | 2704203 | 27 | 33 | nan | nan | nan | Mata Atlântica | 6.1 |
| 1a18aaf1-4c5e-3d84-bd93-9f44a426d1d8 | -9.79498 | -35.99425 | 2024-10-12 03:17:00 | NOAA-21 | BARRA DE SÃO MIGUEL | ALAGOAS | Brasil | 2700607 | 27 | 33 | nan | nan | nan | Mata Atlântica | 2.9 |
| 8eac5b6a-de6c-3977-b252-b55390329f1d | -8.15032 | -39.70608 | 2024-10-12 03:17:00 | NOAA-21 | PARNAMIRIM | PERNAMBUCO | Brasil | 2610400 | 26 | 33 | nan | nan | nan | Caatinga | 2.1 |
| 32147034-4c2a-30fe-8d55-e3eda319dcd7 | -8.14457 | -39.705 | 2024-10-12 03:17:00 | NOAA-21 | PARNAMIRIM | PERNAMBUCO | Brasil | 2610400 | 26 | 33 | nan | nan | nan | Caatinga | 2.1 |
| 8c69a4a9-d16c-31a0-ba06-1f3dd9672ff4 | -8.07231 | -34.97586 | 2024-10-12 03:17:00 | NOAA-21 | RECIFE | PERNAMBUCO | Brasil | 2611606 | 26 | 33 | nan | nan | nan | Mata Atlântica | 2.3 |
| 7a4111d7-1aa9-3718-a61d-0baee5ae2075 | -7.47112 | -40.2224 | 2024-10-12 03:17:00 | NOAA-21 | IPUBI | PERNAMBUCO | Brasil | 2607307 | 26 | 33 | nan | nan | nan | Caatinga | 2.2 |
| ac0f6993-68ce-3ecd-8371-6cf6424a6706 | -7.46894 | -40.2241 | 2024-10-12 03:17:00 | NOAA-21 | IPUBI | PERNAMBUCO | Brasil | 2607307 | 26 | 33 | nan | nan | nan | Caatinga | 4.4 |
| 7c6d29b0-61f2-3897-8b3a-8e1ca2234662 | -7.46294 | -40.22293 | 2024-10-12 03:17:00 | NOAA-21 | IPUBI | PERNAMBUCO | Brasil | 2607307 | 26 | 33 | nan | nan | nan | Caatinga | 4.4 |
| d680175f-920d-3978-b79a-e0232cb31735 | -18.15889 | -42.44396 | 2024-10-12 03:19:00 | NOAA-21 | SANTA MARIA DO SUAÇUÍ | MINAS GERAIS | Brasil | 3158201 | 31 | 33 | nan | nan | nan | Mata Atlântica | 1.3 |
| d15fadc8-e205-3e49-9ec0-d8b8cb477d06 | -17.54772 | -42.30508 | 2024-10-12 03:19:00 | NOAA-21 | MINAS NOVAS | MINAS GERAIS | Brasil | 3141801 | 31 | 33 | nan | nan | nan | Cerrado | 6.6 |
| dcc62f7c-9b2d-3582-9d89-f3856ac8aedc | -17.54212 | -42.30328 | 2024-10-12 03:19:00 | NOAA-21 | MINAS NOVAS | MINAS GERAIS | Brasil | 3141801 | 31 | 33 | nan | nan | nan | Cerrado | 6.6 |
| 3dc8677e-6527-360f-a5e8-f54a6742d973 | -14.99657 | -44.41106 | 2024-10-12 03:19:00 | NOAA-21 | JANUÁRIA | MINAS GERAIS | Brasil | 3135209 | 31 | 33 | nan | nan | nan | Cerrado | 2.6 |
| f5c12d35-3d66-30ab-bb2b-82ba26734f60 | -14.76927 | -42.3145 | 2024-10-12 03:19:00 | NOAA-21 | JACARACI | BAHIA | Brasil | 2917409 | 29 | 33 | nan | nan | nan | Caatinga | 2.7 |
| d8a6729f-2615-3ec2-ac8c-e88fb2093807 | -14.71108 | -40.36822 | 2024-10-12 03:19:00 | NOAA-21 | PLANALTO | BAHIA | Brasil | 2925006 | 29 | 33 | nan | nan | nan | Mata Atlântica | 2.1 |
| 18dda568-ee9a-3b3a-a5d9-425edadafde1 | -14.22989 | -39.76071 | 2024-10-12 03:19:00 | NOAA-21 | ITAGIBÁ | BAHIA | Brasil | 2915205 | 29 | 33 | nan | nan | nan | Mata Atlântica | 3.5 |
| fea6797d-68d8-3026-9821-86fb647eb725 | -14.22538 | -39.75626 | 2024-10-12 03:19:00 | NOAA-21 | ITAGIBÁ | BAHIA | Brasil | 2915205 | 29 | 33 | nan | nan | nan | Mata Atlântica | 4.4 |
| 02b16a1b-b17b-3a41-b8c7-c15d3b9fbe26 | -14.22472 | -39.75956 | 2024-10-12 03:19:00 | NOAA-21 | ITAGIBÁ | BAHIA | Brasil | 2915205 | 29 | 33 | nan | nan | nan | Mata Atlântica | 3.5 |
| 0638d92c-7145-3988-8ef2-84c3d9798fe5 | -14.21466 | -42.31363 | 2024-10-12 03:19:00 | NOAA-21 | IBIASSUCÊ | BAHIA | Brasil | 2912004 | 29 | 33 | nan | nan | nan | Caatinga | 1.4 |
| 01015514-116e-398b-8cc6-d21d1a25aba9 | -14.21367 | -42.31827 | 2024-10-12 03:19:00 | NOAA-21 | IBIASSUCÊ | BAHIA | Brasil | 2912004 | 29 | 33 | nan | nan | nan | Caatinga | 1.6 |
| 69af3789-ee0b-3f35-be95-6eb2fac0acda | -13.70494 | -44.26654 | 2024-10-12 03:19:00 | NOAA-21 | CORIBE | BAHIA | Brasil | 2909109 | 29 | 33 | nan | nan | nan | Cerrado | 3.3 |


[Clique aqui para ver as próximas entradas](README34.md)
