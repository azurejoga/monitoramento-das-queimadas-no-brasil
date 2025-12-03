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

## Dados Diários - Página 3

| ID | Latitude | Longitude | Data/Hora GMT | Satélite | Município | Estado | País | Município ID | Estado ID | País ID | Dias sem Chuva | Precipitação | Risco de Fogo | Bioma | FRP |
|----|----------|-----------|---------------|----------|-----------|--------|------|--------------|-----------|---------|----------------|--------------|----------------|-------|-----|
| 83922f3d-8f25-358e-82a7-8ff94c2e68c1 | -2.6265 | -45.1562 | 2025-12-03 01:20:00 | GOES-19 | PINHEIRO | MARANHÃO | Brasil | 2108603 | 21 | 33 | nan | nan | nan | Amazônia | 68.5 |
| 261f2ed1-ce6e-3abb-a777-c556ef05aec0 | -8.0516 | -43.0765 | 2025-12-03 01:20:00 | GOES-19 | CANTO DO BURITI | PIAUÍ | Brasil | 2202307 | 22 | 33 | nan | nan | nan | Caatinga | 119.1 |
| 1d56edbe-873f-3385-ac84-1bacd0cc47e4 | -11.119 | -53.9446 | 2025-12-03 01:20:00 | GOES-19 | MARCELÂNDIA | MATO GROSSO | Brasil | 5105580 | 51 | 33 | nan | nan | nan | Amazônia | 83.2 |
| 0fcc7c0d-b4ae-37e2-ab54-e32cd710916a | -8.051 | -43.1237 | 2025-12-03 01:20:00 | GOES-19 | CANTO DO BURITI | PIAUÍ | Brasil | 2202307 | 22 | 33 | nan | nan | nan | Caatinga | 130.1 |
| 7e9fa415-fd8f-3ef5-894c-c62db97a1e6a | -19.6249 | -56.7919 | 2025-12-03 01:20:00 | GOES-19 | AQUIDAUANA | MATO GROSSO DO SUL | Brasil | 5001102 | 50 | 33 | nan | nan | nan | Pantanal | 100.6 |
| b7fa59c2-4b1e-3ffc-b79a-8267777dae84 | -19.6453 | -56.7681 | 2025-12-03 01:20:00 | GOES-19 | AQUIDAUANA | MATO GROSSO DO SUL | Brasil | 5001102 | 50 | 33 | nan | nan | nan | Pantanal | 62.7 |
| 60d56125-17af-393b-ac05-6bd8f7a8bf95 | -8.0324 | -43.1022 | 2025-12-03 01:20:00 | GOES-19 | CANTO DO BURITI | PIAUÍ | Brasil | 2202307 | 22 | 33 | nan | nan | nan | Caatinga | 133.6 |
| b718fccd-d2b8-358a-93ec-ad23e0408855 | -2.9225 | -45.4611 | 2025-12-03 01:20:00 | GOES-19 | PEDRO DO ROSÁRIO | MARANHÃO | Brasil | 2108256 | 21 | 33 | nan | nan | nan | Amazônia | 90.2 |
| db70f405-3e2a-3bf0-a864-ff4a2f5587d5 | -2.6266 | -45.1336 | 2025-12-03 01:20:00 | GOES-19 | PINHEIRO | MARANHÃO | Brasil | 2108603 | 21 | 33 | nan | nan | nan | Amazônia | 100.1 |
| 85b95e60-1142-36a6-9b74-84bddfda5804 | -11.1379 | -53.9429 | 2025-12-03 01:20:00 | GOES-19 | MARCELÂNDIA | MATO GROSSO | Brasil | 5105580 | 51 | 33 | nan | nan | nan | Amazônia | 73.5 |
| d806186a-17a6-3243-8cac-66556e5f4ed4 | -2.2086 | -48.0145 | 2025-12-03 01:20:00 | GOES-19 | TOMÉ-AÇU | PARÁ | Brasil | 1508001 | 15 | 33 | nan | nan | nan | Amazônia | 71.8 |
| e659915b-2ed8-3730-a9ad-eb00197abb6e | -19.645 | -56.7891 | 2025-12-03 01:20:00 | GOES-19 | AQUIDAUANA | MATO GROSSO DO SUL | Brasil | 5001102 | 50 | 33 | nan | nan | nan | Pantanal | 109.5 |
| 0506aaec-92ab-303f-8580-64dba0716152 | -8.0513 | -43.1001 | 2025-12-03 01:20:00 | GOES-19 | CANTO DO BURITI | PIAUÍ | Brasil | 2202307 | 22 | 33 | nan | nan | nan | Caatinga | 313.6 |
| 43891fab-3dda-33b7-b6d3-bced7bbe248c | -2.2087 | -47.9929 | 2025-12-03 01:20:00 | GOES-19 | TOMÉ-AÇU | PARÁ | Brasil | 1508001 | 15 | 33 | nan | nan | nan | Amazônia | 99.8 |
| 63ab56ff-c373-3f76-8ff3-df1f14e8cf9e | -21.62944 | -56.13445 | 2025-12-03 01:26:00 | TERRA_M-M | JARDIM | MATO GROSSO DO SUL | Brasil | 5005004 | 50 | 33 | nan | nan | nan | Cerrado | 29.2 |
| 9819d6ea-5de3-365c-98f5-5d159d0e2ddb | -21.61772 | -56.1368 | 2025-12-03 01:26:00 | TERRA_M-M | JARDIM | MATO GROSSO DO SUL | Brasil | 5005004 | 50 | 33 | nan | nan | nan | Cerrado | 13.3 |
| eea8cd00-2799-3eba-b67b-3bd85b796345 | -19.61655 | -56.78517 | 2025-12-03 01:28:00 | TERRA_M-M | AQUIDAUANA | MATO GROSSO DO SUL | Brasil | 5001102 | 50 | 33 | nan | nan | nan | Pantanal | 12.5 |
| f120fb10-277a-33a7-81bf-87b0efe63920 | -19.64264 | -56.79743 | 2025-12-03 01:28:00 | TERRA_M-M | AQUIDAUANA | MATO GROSSO DO SUL | Brasil | 5001102 | 50 | 33 | nan | nan | nan | Pantanal | 38.2 |
| 5f542242-14b6-39a7-a835-4ca815c0833d | -19.63104 | -56.79972 | 2025-12-03 01:28:00 | TERRA_M-M | AQUIDAUANA | MATO GROSSO DO SUL | Brasil | 5001102 | 50 | 33 | nan | nan | nan | Pantanal | 28.2 |
| 58bd2897-ee34-3cf4-ac4b-a7d57e05341e | -19.61944 | -56.80199 | 2025-12-03 01:28:00 | TERRA_M-M | AQUIDAUANA | MATO GROSSO DO SUL | Brasil | 5001102 | 50 | 33 | nan | nan | nan | Pantanal | 12.1 |
| c2c3ed59-fc59-31fe-89b1-ea61e07c8d73 | -19.63978 | -56.78059 | 2025-12-03 01:28:00 | TERRA_M-M | AQUIDAUANA | MATO GROSSO DO SUL | Brasil | 5001102 | 50 | 33 | nan | nan | nan | Pantanal | 88.3 |
| 25cfc2ed-3938-33ca-9b78-3796d1b657ed | -19.62816 | -56.78288 | 2025-12-03 01:28:00 | TERRA_M-M | AQUIDAUANA | MATO GROSSO DO SUL | Brasil | 5001102 | 50 | 33 | nan | nan | nan | Pantanal | 37.8 |
| a5a82452-adf8-32e7-b800-c3f55a7b6a11 | -8.0516 | -43.0765 | 2025-12-03 01:30:00 | GOES-19 | CANTO DO BURITI | PIAUÍ | Brasil | 2202307 | 22 | 33 | nan | nan | nan | Caatinga | 121.6 |
| 53bd6e08-4428-3dfc-bd57-33c9161bef69 | -2.608 | -45.1342 | 2025-12-03 01:30:00 | GOES-19 | PINHEIRO | MARANHÃO | Brasil | 2108603 | 21 | 33 | nan | nan | nan | Amazônia | 65.9 |
| c7aeba18-6872-380e-b1de-be5db551c55a | -11.119 | -53.9446 | 2025-12-03 01:30:00 | GOES-19 | MARCELÂNDIA | MATO GROSSO | Brasil | 5105580 | 51 | 33 | nan | nan | nan | Amazônia | 89.6 |
| 282d5d3b-2485-3511-ab56-d50c32a69ddb | -8.051 | -43.1237 | 2025-12-03 01:30:00 | GOES-19 | CANTO DO BURITI | PIAUÍ | Brasil | 2202307 | 22 | 33 | nan | nan | nan | Caatinga | 66.0 |
| 61f4b827-9550-3537-a614-3c130522537d | -2.9798 | -49.513 | 2025-12-03 01:30:00 | GOES-19 | MOJU | PARÁ | Brasil | 1504703 | 15 | 33 | nan | nan | nan | Amazônia | 69.4 |
| 6b116ecb-6f48-3e91-b8e0-08ecbb062d99 | -2.6452 | -45.133 | 2025-12-03 01:30:00 | GOES-19 | PINHEIRO | MARANHÃO | Brasil | 2108603 | 21 | 33 | nan | nan | nan | Amazônia | 49.0 |
| 9a1b5477-f9c6-3223-9fc8-53bcca663a74 | -2.2087 | -47.9929 | 2025-12-03 01:30:00 | GOES-19 | TOMÉ-AÇU | PARÁ | Brasil | 1508001 | 15 | 33 | nan | nan | nan | Amazônia | 92.4 |
| 34c9f7c8-4e39-32c4-bcb3-1c563c178d26 | -8.0513 | -43.1001 | 2025-12-03 01:30:00 | GOES-19 | CANTO DO BURITI | PIAUÍ | Brasil | 2202307 | 22 | 33 | nan | nan | nan | Caatinga | 254.0 |
| c737504c-d7aa-3859-a0ef-07053a12b2be | -19.645 | -56.7891 | 2025-12-03 01:30:00 | GOES-19 | AQUIDAUANA | MATO GROSSO DO SUL | Brasil | 5001102 | 50 | 33 | nan | nan | nan | Pantanal | 100.3 |
| 1c29f58f-582e-36a3-b5c4-1676352ee2d2 | -2.6266 | -45.1336 | 2025-12-03 01:30:00 | GOES-19 | PINHEIRO | MARANHÃO | Brasil | 2108603 | 21 | 33 | nan | nan | nan | Amazônia | 218.9 |
| 395c7d63-844f-3832-9a31-074057acdd2d | -19.6453 | -56.7681 | 2025-12-03 01:30:00 | GOES-19 | AQUIDAUANA | MATO GROSSO DO SUL | Brasil | 5001102 | 50 | 33 | nan | nan | nan | Pantanal | 67.0 |
| cb39352f-e24b-3361-95b5-fb7d728aa415 | -11.1188 | -53.9652 | 2025-12-03 01:30:00 | GOES-19 | MARCELÂNDIA | MATO GROSSO | Brasil | 5105580 | 51 | 33 | nan | nan | nan | Amazônia | 61.1 |
| dd1818b2-844d-3b04-84bd-2c05f9c2af6b | -8.0703 | -43.0981 | 2025-12-03 01:30:00 | GOES-19 | CANTO DO BURITI | PIAUÍ | Brasil | 2202307 | 22 | 33 | nan | nan | nan | Caatinga | 80.1 |
| 4fbd4fac-69c5-3442-8796-b7246452a503 | -2.2086 | -48.0145 | 2025-12-03 01:30:00 | GOES-19 | TOMÉ-AÇU | PARÁ | Brasil | 1508001 | 15 | 33 | nan | nan | nan | Amazônia | 74.0 |
| ed3446c3-6d5a-3e09-a605-26abeb9d0671 | -11.1379 | -53.9429 | 2025-12-03 01:30:00 | GOES-19 | MARCELÂNDIA | MATO GROSSO | Brasil | 5105580 | 51 | 33 | nan | nan | nan | Amazônia | 75.5 |
| 58b1ec27-7a24-3aed-9773-e78572657d88 | -2.6265 | -45.1562 | 2025-12-03 01:30:00 | GOES-19 | PINHEIRO | MARANHÃO | Brasil | 2108603 | 21 | 33 | nan | nan | nan | Amazônia | 116.4 |
| 83cb7afb-b723-37ee-84c5-e8df429421c9 | -19.6253 | -56.7709 | 2025-12-03 01:30:00 | GOES-19 | AQUIDAUANA | MATO GROSSO DO SUL | Brasil | 5001102 | 50 | 33 | nan | nan | nan | Pantanal | 65.9 |
| f9b16929-1e8f-3126-8f13-400b6401011c | -2.9225 | -45.4611 | 2025-12-03 01:30:00 | GOES-19 | PEDRO DO ROSÁRIO | MARANHÃO | Brasil | 2108256 | 21 | 33 | nan | nan | nan | Amazônia | 106.9 |
| 77c4e9f6-f0db-302d-8ca4-5e25f6503dd2 | -3.2195 | -45.5398 | 2025-12-03 01:30:00 | GOES-19 | PEDRO DO ROSÁRIO | MARANHÃO | Brasil | 2108256 | 21 | 33 | nan | nan | nan | Amazônia | 84.1 |
| 915b0617-bf1f-3d38-8871-9823857f2644 | -19.6249 | -56.7919 | 2025-12-03 01:30:00 | GOES-19 | AQUIDAUANA | MATO GROSSO DO SUL | Brasil | 5001102 | 50 | 33 | nan | nan | nan | Pantanal | 106.9 |
| 0c097e84-8b33-34c9-a077-bcdbc85da1c9 | -8.0324 | -43.1022 | 2025-12-03 01:30:00 | GOES-19 | CANTO DO BURITI | PIAUÍ | Brasil | 2202307 | 22 | 33 | nan | nan | nan | Caatinga | 108.5 |
| d796b618-2e07-3379-bf9f-58bf1c4456a2 | 2.88002 | -60.25708 | 2025-12-03 01:34:00 | TERRA_M-M | BONFIM | RORAIMA | Brasil | 1400159 | 14 | 33 | nan | nan | nan | Amazônia | 23.6 |
| 0cf7f312-e0bf-3485-b3a7-3db00f64250f | 2.8731 | -60.2563 | 2025-12-03 01:40:00 | GOES-19 | BONFIM | RORAIMA | Brasil | 1400159 | 14 | 33 | nan | nan | nan | Amazônia | 45.7 |
| b859b0e2-9e26-3635-ad2b-7309b082751a | -2.9411 | -45.4604 | 2025-12-03 01:40:00 | GOES-19 | PEDRO DO ROSÁRIO | MARANHÃO | Brasil | 2108256 | 21 | 33 | nan | nan | nan | Amazônia | 98.8 |
| 30499430-287a-341c-b8f0-3eacbdf94938 | -2.6266 | -45.1336 | 2025-12-03 01:40:00 | GOES-19 | PINHEIRO | MARANHÃO | Brasil | 2108603 | 21 | 33 | nan | nan | nan | Amazônia | 186.6 |
| 090c4630-13e3-343a-8eb5-0fb19da6447d | -3.2564 | -45.5831 | 2025-12-03 01:40:00 | GOES-19 | ZÉ DOCA | MARANHÃO | Brasil | 2114007 | 21 | 33 | nan | nan | nan | Amazônia | 121.7 |
| c4c42dcd-b0c0-3f87-9fed-8c742b634478 | -19.6253 | -56.7709 | 2025-12-03 01:40:00 | GOES-19 | AQUIDAUANA | MATO GROSSO DO SUL | Brasil | 5001102 | 50 | 33 | nan | nan | nan | Pantanal | 63.6 |
| 7a827184-23be-3069-810c-03046b916313 | -3.2195 | -45.5398 | 2025-12-03 01:40:00 | GOES-19 | PEDRO DO ROSÁRIO | MARANHÃO | Brasil | 2108256 | 21 | 33 | nan | nan | nan | Amazônia | 94.7 |
| 34ce9122-6598-38e3-a40d-f97238dac57a | -19.645 | -56.7891 | 2025-12-03 01:40:00 | GOES-19 | AQUIDAUANA | MATO GROSSO DO SUL | Brasil | 5001102 | 50 | 33 | nan | nan | nan | Pantanal | 118.0 |
| adc7d8f8-deee-3a29-9e18-7df1c5486b75 | -2.608 | -45.1342 | 2025-12-03 01:40:00 | GOES-19 | PINHEIRO | MARANHÃO | Brasil | 2108603 | 21 | 33 | nan | nan | nan | Amazônia | 76.3 |
| 602f53a3-616d-302b-befe-bbe6c7709382 | -19.6453 | -56.7681 | 2025-12-03 01:40:00 | GOES-19 | AQUIDAUANA | MATO GROSSO DO SUL | Brasil | 5001102 | 50 | 33 | nan | nan | nan | Pantanal | 73.6 |
| 745653eb-6444-3b65-aa13-0ca331f75543 | -2.9225 | -45.4611 | 2025-12-03 01:40:00 | GOES-19 | PEDRO DO ROSÁRIO | MARANHÃO | Brasil | 2108256 | 21 | 33 | nan | nan | nan | Amazônia | 130.9 |
| 09735f3b-e5ef-3958-95f3-0b3c809597be | -3.275 | -45.5824 | 2025-12-03 01:40:00 | GOES-19 | ZÉ DOCA | MARANHÃO | Brasil | 2114007 | 21 | 33 | nan | nan | nan | Amazônia | 111.6 |
| 95ebe208-2656-335c-92fd-9ddc765e980c | -19.6249 | -56.7919 | 2025-12-03 01:40:00 | GOES-19 | AQUIDAUANA | MATO GROSSO DO SUL | Brasil | 5001102 | 50 | 33 | nan | nan | nan | Pantanal | 102.6 |
| 83c1b48a-f043-3f14-8454-240c63e8ab3f | -2.6265 | -45.1562 | 2025-12-03 01:40:00 | GOES-19 | PINHEIRO | MARANHÃO | Brasil | 2108603 | 21 | 33 | nan | nan | nan | Amazônia | 126.4 |
| 0d795567-a3ce-3eb7-b2e1-ef1b9749a808 | -2.9798 | -49.513 | 2025-12-03 01:40:00 | GOES-19 | MOJU | PARÁ | Brasil | 1504703 | 15 | 33 | nan | nan | nan | Amazônia | 71.1 |
| 6ca092d1-d3b8-3e4b-8cf7-56c6911dd42c | -2.2086 | -48.0145 | 2025-12-03 01:40:00 | GOES-19 | TOMÉ-AÇU | PARÁ | Brasil | 1508001 | 15 | 33 | nan | nan | nan | Amazônia | 56.7 |
| 8078fce4-b4d3-3d42-ae9b-3954099cd205 | -2.2087 | -47.9929 | 2025-12-03 01:40:00 | GOES-19 | TOMÉ-AÇU | PARÁ | Brasil | 1508001 | 15 | 33 | nan | nan | nan | Amazônia | 77.7 |
| 0dbe96d5-154e-3d1c-b587-39bffa30d83c | -3.275 | -45.5824 | 2025-12-03 01:50:00 | GOES-19 | ZÉ DOCA | MARANHÃO | Brasil | 2114007 | 21 | 33 | nan | nan | nan | Amazônia | 115.8 |
| 0edbacf2-8522-32a5-9977-fabc69c2f62a | -20.3121 | -47.3448 | 2025-12-03 01:50:00 | GOES-19 | CRISTAIS PAULISTA | SÃO PAULO | Brasil | 3513207 | 35 | 33 | nan | nan | nan | Cerrado | 71.7 |
| acf4a41f-2a83-33c9-a860-60f421bfcb84 | -2.2086 | -48.0145 | 2025-12-03 01:50:00 | GOES-19 | TOMÉ-AÇU | PARÁ | Brasil | 1508001 | 15 | 33 | nan | nan | nan | Amazônia | 58.2 |
| dd91997b-83e3-3d2e-a862-c1c4fb96059c | -19.645 | -56.7891 | 2025-12-03 01:50:00 | GOES-19 | AQUIDAUANA | MATO GROSSO DO SUL | Brasil | 5001102 | 50 | 33 | nan | nan | nan | Pantanal | 81.4 |
| aee3fe35-185d-3a75-937a-889815b0c31b | 2.8731 | -60.2563 | 2025-12-03 01:50:00 | GOES-19 | BONFIM | RORAIMA | Brasil | 1400159 | 14 | 33 | nan | nan | nan | Amazônia | 43.3 |
| f4b0f2b2-a1b3-3efe-b083-e9a42e9a93a4 | -19.6453 | -56.7681 | 2025-12-03 01:50:00 | GOES-19 | AQUIDAUANA | MATO GROSSO DO SUL | Brasil | 5001102 | 50 | 33 | nan | nan | nan | Pantanal | 60.8 |
| 15643f1e-ba03-3f1c-874e-e8ef8aa8d5b7 | -2.6265 | -45.1562 | 2025-12-03 01:50:00 | GOES-19 | PINHEIRO | MARANHÃO | Brasil | 2108603 | 21 | 33 | nan | nan | nan | Amazônia | 92.8 |
| fbe1edf9-7ccc-37bf-a8a4-789d7accb9ab | -3.2195 | -45.5398 | 2025-12-03 01:50:00 | GOES-19 | PEDRO DO ROSÁRIO | MARANHÃO | Brasil | 2108256 | 21 | 33 | nan | nan | nan | Amazônia | 74.5 |
| 62c5dab6-bfbd-3305-ba87-d3fa2625101b | -2.6266 | -45.1336 | 2025-12-03 01:50:00 | GOES-19 | PINHEIRO | MARANHÃO | Brasil | 2108603 | 21 | 33 | nan | nan | nan | Amazônia | 150.8 |
| b3eb32cb-f7de-399e-a28c-73e0644de9d3 | -3.2564 | -45.5831 | 2025-12-03 01:50:00 | GOES-19 | ZÉ DOCA | MARANHÃO | Brasil | 2114007 | 21 | 33 | nan | nan | nan | Amazônia | 131.4 |
| d6604f3b-ec54-30ff-8e52-ff44a586c0dd | -2.9411 | -45.4604 | 2025-12-03 01:50:00 | GOES-19 | PEDRO DO ROSÁRIO | MARANHÃO | Brasil | 2108256 | 21 | 33 | nan | nan | nan | Amazônia | 81.4 |
| d30338ab-1b56-3906-a89e-773737aff869 | -2.9225 | -45.4611 | 2025-12-03 01:50:00 | GOES-19 | PEDRO DO ROSÁRIO | MARANHÃO | Brasil | 2108256 | 21 | 33 | nan | nan | nan | Amazônia | 138.8 |
| 1e7eed2f-ab84-37d7-a5d7-7d61d586add0 | -2.2087 | -47.9929 | 2025-12-03 01:50:00 | GOES-19 | TOMÉ-AÇU | PARÁ | Brasil | 1508001 | 15 | 33 | nan | nan | nan | Amazônia | 67.2 |
| 4c8c08ef-51d0-307b-95b4-bf63fec6c800 | -19.6249 | -56.7919 | 2025-12-03 01:50:00 | GOES-19 | AQUIDAUANA | MATO GROSSO DO SUL | Brasil | 5001102 | 50 | 33 | nan | nan | nan | Pantanal | 68.7 |
| 7533bab6-6ad8-3d42-9463-1c9adc9b861a | -2.6266 | -45.1336 | 2025-12-03 02:00:00 | GOES-19 | PINHEIRO | MARANHÃO | Brasil | 2108603 | 21 | 33 | nan | nan | nan | Amazônia | 79.4 |
| b8421534-660c-36c3-bb66-f482e20ad628 | -2.608 | -45.1342 | 2025-12-03 02:00:00 | GOES-19 | PINHEIRO | MARANHÃO | Brasil | 2108603 | 21 | 33 | nan | nan | nan | Amazônia | 64.4 |
| 1db988a9-9597-3dc4-a17a-624dd6654c6f | -15.1281 | -52.9353 | 2025-12-03 02:00:00 | GOES-19 | NOVO SÃO JOAQUIM | MATO GROSSO | Brasil | 5106281 | 51 | 33 | nan | nan | nan | Cerrado | 61.4 |
| 1958c0e3-b9bc-3663-83c5-c8cb30be52a2 | -2.6265 | -45.1562 | 2025-12-03 02:00:00 | GOES-19 | PINHEIRO | MARANHÃO | Brasil | 2108603 | 21 | 33 | nan | nan | nan | Amazônia | 49.2 |
| d15c5e4d-c0c9-390b-9d78-3a34c2b7099e | -15.1277 | -52.9565 | 2025-12-03 02:00:00 | GOES-19 | NOVO SÃO JOAQUIM | MATO GROSSO | Brasil | 5106281 | 51 | 33 | nan | nan | nan | Cerrado | 68.4 |
| dd6d165f-a7d6-33ea-a9e0-20a5c183cbda | -3.2564 | -45.5831 | 2025-12-03 02:00:00 | GOES-19 | ZÉ DOCA | MARANHÃO | Brasil | 2114007 | 21 | 33 | nan | nan | nan | Amazônia | 80.5 |
| 89726f49-e6b4-301f-a23b-334683e138b4 | -2.9225 | -45.4611 | 2025-12-03 02:00:00 | GOES-19 | PEDRO DO ROSÁRIO | MARANHÃO | Brasil | 2108256 | 21 | 33 | nan | nan | nan | Amazônia | 78.2 |
| 42e2a6c5-dea2-32cb-bb17-35bfb66d43b8 | -5.8429 | -39.9426 | 2025-12-03 02:00:00 | GOES-19 | TAUÁ | CEARÁ | Brasil | 2313302 | 23 | 33 | nan | nan | nan | Caatinga | 81.5 |
| ae351118-ab46-3fdd-bfdf-a2c21d3aca51 | -2.2086 | -48.0145 | 2025-12-03 02:00:00 | GOES-19 | TOMÉ-AÇU | PARÁ | Brasil | 1508001 | 15 | 33 | nan | nan | nan | Amazônia | 41.3 |
| 8b1b000b-38bd-3bcd-bfc3-0e980ff322a8 | -5.8617 | -39.9409 | 2025-12-03 02:00:00 | GOES-19 | TAUÁ | CEARÁ | Brasil | 2313302 | 23 | 33 | nan | nan | nan | Caatinga | 147.9 |
| 7e9895fb-73b1-3fa9-ab96-f998f2fa5113 | -2.2087 | -47.9929 | 2025-12-03 02:00:00 | GOES-19 | TOMÉ-AÇU | PARÁ | Brasil | 1508001 | 15 | 33 | nan | nan | nan | Amazônia | 49.9 |
| 8a8a09ad-b89b-3b63-a84c-4aef661a9385 | -1.2025 | -53.0907 | 2025-12-03 02:00:00 | GOES-19 | ALMEIRIM | PARÁ | Brasil | 1500503 | 15 | 33 | nan | nan | nan | Amazônia | 22.7 |
| c0cb6c54-4476-32c9-af83-1bcdeee3010b | -5.862 | -39.9161 | 2025-12-03 02:00:00 | GOES-19 | MOMBAÇA | CEARÁ | Brasil | 2308500 | 23 | 33 | nan | nan | nan | Caatinga | 52.8 |
| 5a9bf924-a52d-3033-9887-55d3b0f9b6ea | -1.2025 | -53.0907 | 2025-12-03 02:10:00 | GOES-19 | ALMEIRIM | PARÁ | Brasil | 1500503 | 15 | 33 | nan | nan | nan | Amazônia | 28.4 |
| 814afc05-a15d-30f4-bd82-145ab2b5e08b | -15.1277 | -52.9565 | 2025-12-03 02:10:00 | GOES-19 | NOVO SÃO JOAQUIM | MATO GROSSO | Brasil | 5106281 | 51 | 33 | nan | nan | nan | Cerrado | 73.1 |
| 34f3cd67-5f48-3b4c-89d0-979fa2603842 | -5.8429 | -39.9426 | 2025-12-03 02:10:00 | GOES-19 | TAUÁ | CEARÁ | Brasil | 2313302 | 23 | 33 | nan | nan | nan | Caatinga | 63.4 |
| 7ce89f26-1f62-38d0-80c2-156267d56975 | -3.9053 | -45.913 | 2025-12-03 02:10:00 | GOES-19 | ALTO ALEGRE DO PINDARÉ | MARANHÃO | Brasil | 2100477 | 21 | 33 | nan | nan | nan | Amazônia | 65.9 |
| 0a1578e1-1910-39c2-80a8-8f8f1c7b1140 | -5.8617 | -39.9409 | 2025-12-03 02:10:00 | GOES-19 | TAUÁ | CEARÁ | Brasil | 2313302 | 23 | 33 | nan | nan | nan | Caatinga | 134.9 |
| c2a07d97-9255-3b38-88dc-c42d82cd1ae5 | -15.1281 | -52.9353 | 2025-12-03 02:10:00 | GOES-19 | NOVO SÃO JOAQUIM | MATO GROSSO | Brasil | 5106281 | 51 | 33 | nan | nan | nan | Cerrado | 68.7 |
| c521c9fc-79f1-3560-869d-108ae81b55e8 | -2.2087 | -47.9929 | 2025-12-03 02:10:00 | GOES-19 | TOMÉ-AÇU | PARÁ | Brasil | 1508001 | 15 | 33 | nan | nan | nan | Amazônia | 51.6 |
| 72187047-4c79-33a2-9f7e-1e6088442cd1 | -2.2086 | -48.0145 | 2025-12-03 02:10:00 | GOES-19 | TOMÉ-AÇU | PARÁ | Brasil | 1508001 | 15 | 33 | nan | nan | nan | Amazônia | 40.6 |
| b9b6c97e-490f-3e84-a927-8a1b4c5bcd52 | -1.2025 | -53.0907 | 2025-12-03 02:20:00 | GOES-19 | ALMEIRIM | PARÁ | Brasil | 1500503 | 15 | 33 | nan | nan | nan | Amazônia | 28.1 |
| 9268b4ca-c684-373a-905e-9e75797fa3dd | -5.8617 | -39.9409 | 2025-12-03 02:20:00 | GOES-19 | TAUÁ | CEARÁ | Brasil | 2313302 | 23 | 33 | nan | nan | nan | Caatinga | 76.6 |
| a667fde9-8fd7-3f26-8723-faeea1e750c3 | -3.9053 | -45.913 | 2025-12-03 02:20:00 | GOES-19 | ALTO ALEGRE DO PINDARÉ | MARANHÃO | Brasil | 2100477 | 21 | 33 | nan | nan | nan | Amazônia | 92.6 |
| fad51eef-a661-3ee5-85d4-82acc940b28f | -15.1277 | -52.9565 | 2025-12-03 02:20:00 | GOES-19 | NOVO SÃO JOAQUIM | MATO GROSSO | Brasil | 5106281 | 51 | 33 | nan | nan | nan | Cerrado | 66.9 |
| e88c6122-c958-3b4d-b284-fe0d971224da | -2.2087 | -47.9929 | 2025-12-03 02:20:00 | GOES-19 | TOMÉ-AÇU | PARÁ | Brasil | 1508001 | 15 | 33 | nan | nan | nan | Amazônia | 50.0 |


[Clique aqui para ver as próximas entradas](README4.md)
