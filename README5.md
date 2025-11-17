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

## Dados Diários - Página 5

| ID | Latitude | Longitude | Data/Hora GMT | Satélite | Município | Estado | País | Município ID | Estado ID | País ID | Dias sem Chuva | Precipitação | Risco de Fogo | Bioma | FRP |
|----|----------|-----------|---------------|----------|-----------|--------|------|--------------|-----------|---------|----------------|--------------|----------------|-------|-----|
| 75c4dc01-db08-37f6-9cc0-72561de60318 | -9.496 | -40.3337 | 2025-11-17 00:40:00 | GOES-19 | JUAZEIRO | BAHIA | Brasil | 2918407 | 29 | 33 | nan | nan | nan | Caatinga | 197.7 |
| 7f67dae7-5ad7-3240-bc80-0dc58bc7d037 | -2.694 | -52.0653 | 2025-11-17 00:40:00 | GOES-19 | PORTO DE MOZ | PARÁ | Brasil | 1505908 | 15 | 33 | nan | nan | nan | Amazônia | 64.7 |
| c092070c-7533-357b-8916-c7d338a5a4b5 | -9.5339 | -40.3531 | 2025-11-17 00:40:00 | GOES-19 | JUAZEIRO | BAHIA | Brasil | 2918407 | 29 | 33 | nan | nan | nan | Caatinga | 369.8 |
| 32cba768-3c6d-3e98-8f99-695ace81eb97 | -2.5238 | -47.8332 | 2025-11-17 00:40:00 | GOES-19 | IPIXUNA DO PARÁ | PARÁ | Brasil | 1503457 | 15 | 33 | nan | nan | nan | Amazônia | 82.3 |
| 84224147-ddc4-3712-9b84-b89f839cb293 | -3.2344 | -50.4952 | 2025-11-17 00:40:00 | GOES-19 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 85.3 |
| c4a5f04d-655b-3080-8923-eb7fc21238e3 | -11.8486 | -49.2218 | 2025-11-17 00:40:00 | GOES-19 | CARIRI DO TOCANTINS | TOCANTINS | Brasil | 1703867 | 17 | 33 | nan | nan | nan | Cerrado | 112.6 |
| 2df74ef2-0878-34d3-b29a-90bb1948474e | -4.1596 | -50.2098 | 2025-11-17 00:40:00 | GOES-19 | NOVO REPARTIMENTO | PARÁ | Brasil | 1505064 | 15 | 33 | nan | nan | nan | Amazônia | 79.7 |
| a0aa3982-cd78-335f-babd-87bba8faaaa2 | -6.6684 | -42.0553 | 2025-11-17 00:40:00 | GOES-19 | OEIRAS | PIAUÍ | Brasil | 2207009 | 22 | 33 | nan | nan | nan | Caatinga | 130.9 |
| 2ae48b7f-9102-3c6b-8ef0-de4ef93883ce | -9.5147 | -40.3558 | 2025-11-17 00:40:00 | GOES-19 | JUAZEIRO | BAHIA | Brasil | 2918407 | 29 | 33 | nan | nan | nan | Caatinga | 815.0 |
| c48f0cb5-4b95-3d5e-b4cf-13a919e97c5e | -9.5152 | -40.331 | 2025-11-17 00:40:00 | GOES-19 | JUAZEIRO | BAHIA | Brasil | 2918407 | 29 | 33 | nan | nan | nan | Caatinga | 1178.0 |
| 02e296cf-c6d2-3fc7-b320-ece8da66144d | -2.5053 | -47.8337 | 2025-11-17 00:40:00 | GOES-19 | IPIXUNA DO PARÁ | PARÁ | Brasil | 1503457 | 15 | 33 | nan | nan | nan | Amazônia | 73.2 |
| 63637a15-75d9-3225-bd95-ddf6b62ed45f | -3.2343 | -50.5162 | 2025-11-17 00:40:00 | GOES-19 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 66.3 |
| a0d7e7f7-369d-35dc-b184-1a678a2bc80f | -9.4956 | -40.3586 | 2025-11-17 00:40:00 | GOES-19 | JUAZEIRO | BAHIA | Brasil | 2918407 | 29 | 33 | nan | nan | nan | Caatinga | 101.1 |
| 0ef23b6d-2e06-35a7-a33c-66e53074aa70 | -10.6498 | -49.3834 | 2025-11-17 00:40:00 | GOES-19 | CRISTALÂNDIA | TOCANTINS | Brasil | 1706100 | 17 | 33 | nan | nan | nan | Cerrado | 76.4 |
| e4aa8139-4f3c-3ced-a0c0-8e23d2953838 | -11.849 | -49.2 | 2025-11-17 00:40:00 | GOES-19 | CARIRI DO TOCANTINS | TOCANTINS | Brasil | 1703867 | 17 | 33 | nan | nan | nan | Cerrado | 87.0 |
| 5c839991-0401-3a31-8788-51748ac72f27 | -2.5053 | -47.812 | 2025-11-17 00:40:00 | GOES-19 | IPIXUNA DO PARÁ | PARÁ | Brasil | 1503457 | 15 | 33 | nan | nan | nan | Amazônia | 91.6 |
| d2822a61-7012-3998-890c-8f3764c4676b | -11.7208 | -48.8669 | 2025-11-17 00:40:00 | GOES-19 | GURUPI | TOCANTINS | Brasil | 1709500 | 17 | 33 | nan | nan | nan | Cerrado | 69.7 |
| 2d4eada3-3935-3b38-a2f0-1028d0e99c51 | -4.1781 | -50.2091 | 2025-11-17 00:40:00 | GOES-19 | NOVO REPARTIMENTO | PARÁ | Brasil | 1505064 | 15 | 33 | nan | nan | nan | Amazônia | 81.6 |
| ee378e53-b766-343a-995d-db4069d12012 | -9.5156 | -40.3061 | 2025-11-17 00:40:00 | GOES-19 | JUAZEIRO | BAHIA | Brasil | 2918407 | 29 | 33 | nan | nan | nan | Caatinga | 76.2 |
| 9ea40ba3-2d42-3d68-8e21-a23ca5c58623 | -11.8987 | -46.1934 | 2025-11-17 00:40:00 | GOES-19 | PONTE ALTA DO BOM JESUS | TOCANTINS | Brasil | 1717800 | 17 | 33 | nan | nan | nan | Cerrado | 70.3 |
| 36b571f5-0ecb-32ad-a584-45f4036c584b | -2.5238 | -47.8115 | 2025-11-17 00:40:00 | GOES-19 | IPIXUNA DO PARÁ | PARÁ | Brasil | 1503457 | 15 | 33 | nan | nan | nan | Amazônia | 96.9 |
| 7dea3f5b-dc99-3fd4-9165-e77ea47dd8eb | -11.8299 | -49.2024 | 2025-11-17 00:40:00 | GOES-19 | CARIRI DO TOCANTINS | TOCANTINS | Brasil | 1703867 | 17 | 33 | nan | nan | nan | Cerrado | 67.7 |
| 11754d31-e435-32db-b7df-0e0d0fde9570 | -6.6687 | -42.0314 | 2025-11-17 00:40:00 | GOES-19 | OEIRAS | PIAUÍ | Brasil | 2207009 | 22 | 33 | nan | nan | nan | Caatinga | 277.2 |
| 70782e5a-8560-3f09-9d8a-df4d63725575 | -11.8188 | -45.2907 | 2025-11-17 00:40:00 | GOES-19 | BARREIRAS | BAHIA | Brasil | 2903201 | 29 | 33 | nan | nan | nan | Cerrado | 69.6 |
| f19f3365-0b6f-3f95-9226-71a6dc62f172 | -6.6875 | -42.0296 | 2025-11-17 00:40:00 | GOES-19 | OEIRAS | PIAUÍ | Brasil | 2207009 | 22 | 33 | nan | nan | nan | Caatinga | 344.8 |
| c94bfa95-eeab-3b57-b8de-8d179d4962d0 | -11.8295 | -49.2242 | 2025-11-17 00:40:00 | GOES-19 | CARIRI DO TOCANTINS | TOCANTINS | Brasil | 1703867 | 17 | 33 | nan | nan | nan | Cerrado | 81.2 |
| 64d855af-7c51-3e74-89a3-27af23de6ad6 | -4.7209 | -46.3832 | 2025-11-17 00:40:00 | GOES-19 | BURITICUPU | MARANHÃO | Brasil | 2102325 | 21 | 33 | nan | nan | nan | Amazônia | 70.0 |
| 2442f791-2e52-34a8-a759-7ce42d983655 | -23.43893 | -47.76825 | 2025-11-17 00:49:00 | TERRA_M-M | TATUÍ | SÃO PAULO | Brasil | 3554003 | 35 | 33 | nan | nan | nan | Mata Atlântica | 18.6 |
| 8473f3b7-4469-3f42-8025-64153df45435 | -20.3233 | -57.77885 | 2025-11-17 00:49:00 | TERRA_M-M | CORUMBÁ | MATO GROSSO DO SUL | Brasil | 5003207 | 50 | 33 | nan | nan | nan | Pantanal | 20.3 |
| 08f581a0-8d27-3477-a7a8-92ee12fdd321 | -15.00176 | -43.38089 | 2025-11-17 00:49:00 | TERRA_M-M | GAMELEIRAS | MINAS GERAIS | Brasil | 3127339 | 31 | 33 | nan | nan | nan | Caatinga | 32.7 |
| f42c7afe-e99a-321f-a794-c6ff136f0ec1 | -16.25019 | -46.96047 | 2025-11-17 00:49:00 | TERRA_M-M | UNAÍ | MINAS GERAIS | Brasil | 3170404 | 31 | 33 | nan | nan | nan | Cerrado | 30.6 |
| 9e97af80-1015-3ba9-a46a-0f3eade133dc | -6.6684 | -42.0553 | 2025-11-17 00:50:00 | GOES-19 | OEIRAS | PIAUÍ | Brasil | 2207009 | 22 | 33 | nan | nan | nan | Caatinga | 78.5 |
| e09e1c18-9cc6-3cf7-9032-7d7808bf8446 | -11.8188 | -45.2907 | 2025-11-17 00:50:00 | GOES-19 | BARREIRAS | BAHIA | Brasil | 2903201 | 29 | 33 | nan | nan | nan | Cerrado | 67.0 |
| a573e1f1-e749-34ea-bca1-100ce8197352 | -3.776 | -49.2517 | 2025-11-17 00:50:00 | GOES-19 | GOIANÉSIA DO PARÁ | PARÁ | Brasil | 1503093 | 15 | 33 | nan | nan | nan | Amazônia | 75.8 |
| 0fbc87f8-497d-3c24-b7d4-e287b6295784 | -2.5238 | -47.8115 | 2025-11-17 00:50:00 | GOES-19 | IPIXUNA DO PARÁ | PARÁ | Brasil | 1503457 | 15 | 33 | nan | nan | nan | Amazônia | 93.3 |
| 83453b8a-09da-3607-8aff-6680eb781634 | -11.8295 | -49.2242 | 2025-11-17 00:50:00 | GOES-19 | CARIRI DO TOCANTINS | TOCANTINS | Brasil | 1703867 | 17 | 33 | nan | nan | nan | Cerrado | 77.0 |
| b7eeb14c-1c3d-3c3e-b3e4-fc1f57eaa07d | -11.8299 | -49.2024 | 2025-11-17 00:50:00 | GOES-19 | CARIRI DO TOCANTINS | TOCANTINS | Brasil | 1703867 | 17 | 33 | nan | nan | nan | Cerrado | 62.8 |
| a91a6e2f-2fa5-3561-855c-a95d9230893f | -11.7208 | -48.8669 | 2025-11-17 00:50:00 | GOES-19 | GURUPI | TOCANTINS | Brasil | 1709500 | 17 | 33 | nan | nan | nan | Cerrado | 74.0 |
| f7a8d3c1-3ad0-3e9b-9de0-77cbf18c9c05 | -6.6873 | -42.0535 | 2025-11-17 00:50:00 | GOES-19 | OEIRAS | PIAUÍ | Brasil | 2207009 | 22 | 33 | nan | nan | nan | Caatinga | 237.8 |
| a8f73cce-3418-353e-b507-aca3f4570454 | -6.6687 | -42.0314 | 2025-11-17 00:50:00 | GOES-19 | OEIRAS | PIAUÍ | Brasil | 2207009 | 22 | 33 | nan | nan | nan | Caatinga | 113.4 |
| b7c68d5d-e70c-325e-8506-fed8fd4735f8 | -9.5343 | -40.3282 | 2025-11-17 00:50:00 | GOES-19 | JUAZEIRO | BAHIA | Brasil | 2918407 | 29 | 33 | nan | nan | nan | Caatinga | 146.4 |
| a879f384-a926-3f0d-9eeb-9f9e07dbf2e3 | -4.7395 | -46.3821 | 2025-11-17 00:50:00 | GOES-19 | BURITICUPU | MARANHÃO | Brasil | 2102325 | 21 | 33 | nan | nan | nan | Amazônia | 57.8 |
| 8d66da44-6055-3a1a-aa2e-89793fd292a7 | -2.5053 | -47.812 | 2025-11-17 00:50:00 | GOES-19 | IPIXUNA DO PARÁ | PARÁ | Brasil | 1503457 | 15 | 33 | nan | nan | nan | Amazônia | 124.4 |
| 76d5839b-512a-382b-a5a2-b5b52aae0955 | -9.5147 | -40.3558 | 2025-11-17 00:50:00 | GOES-19 | JUAZEIRO | BAHIA | Brasil | 2918407 | 29 | 33 | nan | nan | nan | Caatinga | 210.3 |
| 7d1d7425-b11e-3892-b9d9-9f93f3349ae1 | -4.7209 | -46.3832 | 2025-11-17 00:50:00 | GOES-19 | BURITICUPU | MARANHÃO | Brasil | 2102325 | 21 | 33 | nan | nan | nan | Amazônia | 77.0 |
| fb29c431-8a5f-39a4-a7c9-cdd8fbcde21e | -4.0634 | -47.4943 | 2025-11-17 00:50:00 | GOES-19 | ULIANÓPOLIS | PARÁ | Brasil | 1508126 | 15 | 33 | nan | nan | nan | Amazônia | 69.4 |
| 5540b18a-115c-3cd9-bd20-b01e9e50bef3 | -11.8486 | -49.2218 | 2025-11-17 00:50:00 | GOES-19 | CARIRI DO TOCANTINS | TOCANTINS | Brasil | 1703867 | 17 | 33 | nan | nan | nan | Cerrado | 83.1 |
| 25b20408-015b-36b3-921e-f090950bf8be | -11.7017 | -48.8692 | 2025-11-17 00:50:00 | GOES-19 | GURUPI | TOCANTINS | Brasil | 1709500 | 17 | 33 | nan | nan | nan | Cerrado | 79.5 |
| 51838a97-36b5-35ee-8d98-a9c7c9a235d5 | -10.6498 | -49.3834 | 2025-11-17 00:50:00 | GOES-19 | CRISTALÂNDIA | TOCANTINS | Brasil | 1706100 | 17 | 33 | nan | nan | nan | Cerrado | 63.6 |
| baee7faf-6d2b-3721-85c9-01f8781332db | -11.7996 | -45.2935 | 2025-11-17 00:50:00 | GOES-19 | BARREIRAS | BAHIA | Brasil | 2903201 | 29 | 33 | nan | nan | nan | Cerrado | 53.3 |
| 0130d005-d035-3248-92e2-80c72088b95a | -6.6875 | -42.0296 | 2025-11-17 00:50:00 | GOES-19 | OEIRAS | PIAUÍ | Brasil | 2207009 | 22 | 33 | nan | nan | nan | Caatinga | 309.9 |
| 62ca99a1-68f3-3205-9184-570bf60ab08a | -9.5152 | -40.331 | 2025-11-17 00:50:00 | GOES-19 | JUAZEIRO | BAHIA | Brasil | 2918407 | 29 | 33 | nan | nan | nan | Caatinga | 362.0 |
| a5a333df-234f-33b9-a16a-ca5948ed1464 | -2.5238 | -47.8332 | 2025-11-17 00:50:00 | GOES-19 | IPIXUNA DO PARÁ | PARÁ | Brasil | 1503457 | 15 | 33 | nan | nan | nan | Amazônia | 59.2 |
| f2fc8b52-056d-38d9-a556-d1e599367f88 | -2.5053 | -47.8337 | 2025-11-17 00:50:00 | GOES-19 | IPIXUNA DO PARÁ | PARÁ | Brasil | 1503457 | 15 | 33 | nan | nan | nan | Amazônia | 68.5 |
| ad3b977c-8eeb-3f90-b4e8-8e5787039a87 | -11.849 | -49.2 | 2025-11-17 00:50:00 | GOES-19 | CARIRI DO TOCANTINS | TOCANTINS | Brasil | 1703867 | 17 | 33 | nan | nan | nan | Cerrado | 66.7 |
| 9cb40a76-8270-35e1-960c-0d2b4d75cba2 | -9.5339 | -40.3531 | 2025-11-17 00:50:00 | GOES-19 | JUAZEIRO | BAHIA | Brasil | 2918407 | 29 | 33 | nan | nan | nan | Caatinga | 100.6 |
| ebd600e0-169d-3fde-89fb-539cb6688724 | -10.6687 | -49.3813 | 2025-11-17 00:50:00 | GOES-19 | CRISTALÂNDIA | TOCANTINS | Brasil | 1706100 | 17 | 33 | nan | nan | nan | Cerrado | 85.9 |
| 169b2138-2c67-35e7-9cdd-243ecb31bbad | -3.2344 | -50.4952 | 2025-11-17 00:50:00 | GOES-19 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 106.1 |
| fae6c04f-436e-3c5c-b700-82cb9cb74703 | -3.2343 | -50.5162 | 2025-11-17 00:50:00 | GOES-19 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 63.8 |
| daed560b-bf61-3b18-8673-7427360f6421 | -4.1596 | -50.2098 | 2025-11-17 00:50:00 | GOES-19 | NOVO REPARTIMENTO | PARÁ | Brasil | 1505064 | 15 | 33 | nan | nan | nan | Amazônia | 59.7 |
| 57b07b85-5967-36d6-acf9-3690f574792d | -13.727 | -51.45259 | 2025-11-17 00:52:00 | TERRA_M-M | COCALINHO | MATO GROSSO | Brasil | 5103106 | 51 | 33 | nan | nan | nan | Cerrado | 9.3 |
| 3274ea6e-72f3-3ca0-a044-b117a31810b2 | -7.96553 | -50.01281 | 2025-11-17 00:52:00 | TERRA_M-M | REDENÇÃO | PARÁ | Brasil | 1506138 | 15 | 33 | nan | nan | nan | Amazônia | 19.5 |
| 0297022f-a98b-3df3-bac6-0670468f4737 | -9.06442 | -44.78442 | 2025-11-17 00:52:00 | TERRA_M-M | BOM JESUS | PIAUÍ | Brasil | 2201903 | 22 | 33 | nan | nan | nan | Cerrado | 36.0 |
| a7ffced6-9b42-3c66-afa8-c3a780c8dea2 | -7.96332 | -49.99783 | 2025-11-17 00:52:00 | TERRA_M-M | REDENÇÃO | PARÁ | Brasil | 1506138 | 15 | 33 | nan | nan | nan | Amazônia | 20.6 |
| 9b150ab3-224c-3169-bc8b-97d0ed83a576 | -9.58726 | -49.11842 | 2025-11-17 00:52:00 | TERRA_M-M | ABREULÂNDIA | TOCANTINS | Brasil | 1700251 | 17 | 33 | nan | nan | nan | Cerrado | 32.9 |
| 995bc3b3-bd83-3e02-8903-3b8de1c6893b | -9.3262 | -46.58233 | 2025-11-17 00:52:00 | TERRA_M-M | ALTO PARNAÍBA | MARANHÃO | Brasil | 2100501 | 21 | 33 | nan | nan | nan | Cerrado | 59.0 |
| ba902dc5-954c-3fc8-a562-df015349b94e | -9.57289 | -49.1038 | 2025-11-17 00:52:00 | TERRA_M-M | ABREULÂNDIA | TOCANTINS | Brasil | 1700251 | 17 | 33 | nan | nan | nan | Cerrado | 10.7 |
| 10ee1c7b-3cf3-31b7-9d57-d9be63c5bf48 | -11.83655 | -49.21196 | 2025-11-17 00:52:00 | TERRA_M-M | CARIRI DO TOCANTINS | TOCANTINS | Brasil | 1703867 | 17 | 33 | nan | nan | nan | Cerrado | 125.1 |
| 6e46e623-4775-3f87-be5b-b5927fc1b0f1 | -10.91233 | -49.41636 | 2025-11-17 00:52:00 | TERRA_M-M | SANTA RITA DO TOCANTINS | TOCANTINS | Brasil | 1718899 | 17 | 33 | nan | nan | nan | Cerrado | 9.0 |
| cc8df701-150e-307f-a111-556d17a19023 | -11.72993 | -49.8504 | 2025-11-17 00:52:00 | TERRA_M-M | FORMOSO DO ARAGUAIA | TOCANTINS | Brasil | 1708205 | 17 | 33 | nan | nan | nan | Cerrado | 14.2 |
| 85d0a771-1297-3459-8123-bee2bd1127c9 | -10.95936 | -44.53313 | 2025-11-17 00:52:00 | TERRA_M-M | SANTA RITA DE CÁSSIA | BAHIA | Brasil | 2928406 | 29 | 33 | nan | nan | nan | Cerrado | 55.6 |
| 0177d4d8-8f46-3b7e-a80d-2f80f096dcaf | -10.31648 | -50.17632 | 2025-11-17 00:52:00 | TERRA_M-M | PIUM | TOCANTINS | Brasil | 1717503 | 17 | 33 | nan | nan | nan | Cerrado | 7.8 |
| d5f0df84-e8a5-3bce-86f0-d0774fd29e17 | -11.41558 | -43.34778 | 2025-11-17 00:52:00 | TERRA_M-M | BARRA | BAHIA | Brasil | 2902708 | 29 | 33 | nan | nan | nan | Cerrado | 41.9 |
| b4e5499a-80d1-3595-a584-cf225488ea39 | -8.539 | -46.06999 | 2025-11-17 00:52:00 | TERRA_M-M | TASSO FRAGOSO | MARANHÃO | Brasil | 2112001 | 21 | 33 | nan | nan | nan | Cerrado | 40.7 |
| 33d0030c-0588-3e0e-b4f5-718a626164c1 | -7.43794 | -48.93273 | 2025-11-17 00:52:00 | TERRA_M-M | ARAGUAÍNA | TOCANTINS | Brasil | 1702109 | 17 | 33 | nan | nan | nan | Amazônia | 17.5 |
| e045efdc-1b25-3d48-a3c4-9762dfe2a5af | -11.06036 | -45.16505 | 2025-11-17 00:52:00 | TERRA_M-M | FORMOSA DO RIO PRETO | BAHIA | Brasil | 2911105 | 29 | 33 | nan | nan | nan | Cerrado | 26.2 |
| 97327bb0-2214-3b02-ba6e-d682d78bcd73 | -10.91157 | -49.40984 | 2025-11-17 00:52:00 | TERRA_M-M | SANTA RITA DO TOCANTINS | TOCANTINS | Brasil | 1718899 | 17 | 33 | nan | nan | nan | Cerrado | 7.8 |
| 2a0c69a7-227e-38af-8b37-70ec20027c5f | -9.578 | -49.10965 | 2025-11-17 00:52:00 | TERRA_M-M | ABREULÂNDIA | TOCANTINS | Brasil | 1700251 | 17 | 33 | nan | nan | nan | Cerrado | 52.1 |
| e5348e91-7042-3c3e-82b3-36153ab56c26 | -10.85263 | -46.76208 | 2025-11-17 00:52:00 | TERRA_M-M | MATEIROS | TOCANTINS | Brasil | 1712702 | 17 | 33 | nan | nan | nan | Cerrado | 38.9 |
| 9260028a-2801-3cd1-bdf7-03bd81761fe6 | -9.58048 | -49.1261 | 2025-11-17 00:52:00 | TERRA_M-M | ABREULÂNDIA | TOCANTINS | Brasil | 1700251 | 17 | 33 | nan | nan | nan | Cerrado | 26.6 |
| 387ea9ed-7d00-3c62-bcf3-0fe0ad5b280f | -12.19544 | -54.27795 | 2025-11-17 00:52:00 | TERRA_M-M | FELIZ NATAL | MATO GROSSO | Brasil | 5103700 | 51 | 33 | nan | nan | nan | Amazônia | 6.2 |
| c15fa54f-37ce-3f80-9028-7ad4ad7c03f6 | -11.15914 | -49.44779 | 2025-11-17 00:52:00 | TERRA_M-M | SANTA RITA DO TOCANTINS | TOCANTINS | Brasil | 1718899 | 17 | 33 | nan | nan | nan | Cerrado | 17.6 |
| 92a5c321-df10-3516-895e-c056659923f9 | -9.32779 | -46.57547 | 2025-11-17 00:52:00 | TERRA_M-M | ALTO PARNAÍBA | MARANHÃO | Brasil | 2100501 | 21 | 33 | nan | nan | nan | Cerrado | 83.0 |
| 5d1f34d0-432e-3d17-8f4c-0b3c94bad540 | -7.97566 | -50.00555 | 2025-11-17 00:52:00 | TERRA_M-M | REDENÇÃO | PARÁ | Brasil | 1506138 | 15 | 33 | nan | nan | nan | Amazônia | 47.3 |
| 375f4cc5-d5a6-384f-afb3-dfa2b32138cc | -7.21482 | -47.99576 | 2025-11-17 00:52:00 | TERRA_M-M | BABAÇULÂNDIA | TOCANTINS | Brasil | 1703008 | 17 | 33 | nan | nan | nan | Cerrado | 15.5 |
| 89348331-e0a9-397c-9925-32652503d3ca | -11.71243 | -48.86041 | 2025-11-17 00:52:00 | TERRA_M-M | GURUPI | TOCANTINS | Brasil | 1709500 | 17 | 33 | nan | nan | nan | Cerrado | 76.7 |
| 312d2422-24d3-3bd2-8f12-2d86e072fb53 | -10.63786 | -51.76129 | 2025-11-17 00:52:00 | TERRA_M-M | CONFRESA | MATO GROSSO | Brasil | 5103353 | 51 | 33 | nan | nan | nan | Amazônia | 5.9 |
| 95d3dbe2-dc38-35a4-9d08-4b69a6ba5b35 | -13.72852 | -51.46282 | 2025-11-17 00:52:00 | TERRA_M-M | COCALINHO | MATO GROSSO | Brasil | 5103106 | 51 | 33 | nan | nan | nan | Cerrado | 7.3 |
| 60992509-e749-3c2b-a432-499e2629bcfa | -11.84774 | -49.21014 | 2025-11-17 00:52:00 | TERRA_M-M | CARIRI DO TOCANTINS | TOCANTINS | Brasil | 1703867 | 17 | 33 | nan | nan | nan | Cerrado | 50.0 |
| 13945b07-3129-3c0f-96f4-947e0ebbf3e0 | -9.63987 | -47.89147 | 2025-11-17 00:52:00 | TERRA_M-M | RIO SONO | TOCANTINS | Brasil | 1718758 | 17 | 33 | nan | nan | nan | Cerrado | 16.5 |
| 45b38d51-ece3-3cc9-961b-379eb5484359 | -7.22828 | -47.99378 | 2025-11-17 00:52:00 | TERRA_M-M | BABAÇULÂNDIA | TOCANTINS | Brasil | 1703008 | 17 | 33 | nan | nan | nan | Cerrado | 17.4 |
| c37d2bf0-62a2-321e-a4a4-b5923e15f486 | -10.66449 | -49.37683 | 2025-11-17 00:52:00 | TERRA_M-M | CRISTALÂNDIA | TOCANTINS | Brasil | 1706100 | 17 | 33 | nan | nan | nan | Cerrado | 157.4 |
| f5c5e2b4-d59d-3bca-ac2c-f81653695d21 | -11.81238 | -47.58854 | 2025-11-17 00:52:00 | TERRA_M-M | NATIVIDADE | TOCANTINS | Brasil | 1714203 | 17 | 33 | nan | nan | nan | Cerrado | 27.5 |
| ec57c760-dda5-311f-b5f4-37e3070810fa | -7.96441 | -50.00735 | 2025-11-17 00:52:00 | TERRA_M-M | REDENÇÃO | PARÁ | Brasil | 1506138 | 15 | 33 | nan | nan | nan | Amazônia | 28.4 |
| 964dcc39-6e87-39d4-801a-359405542881 | -11.71492 | -48.87633 | 2025-11-17 00:52:00 | TERRA_M-M | GURUPI | TOCANTINS | Brasil | 1709500 | 17 | 33 | nan | nan | nan | Cerrado | 31.3 |
| bc5b1056-0523-3f1e-90af-d2a6eb53217d | -10.66214 | -49.36176 | 2025-11-17 00:52:00 | TERRA_M-M | CRISTALÂNDIA | TOCANTINS | Brasil | 1706100 | 17 | 33 | nan | nan | nan | Cerrado | 31.6 |
| d569642b-cb1c-3a76-a2ab-6c729d466c60 | -11.4161 | -43.35262 | 2025-11-17 00:52:00 | TERRA_M-M | BARRA | BAHIA | Brasil | 2902708 | 29 | 33 | nan | nan | nan | Cerrado | 34.9 |
| 3a7d56e7-6781-3a38-9007-65e19fe841e6 | -8.86761 | -50.19574 | 2025-11-17 00:52:00 | TERRA_M-M | SANTA MARIA DAS BARREIRAS | PARÁ | Brasil | 1506583 | 15 | 33 | nan | nan | nan | Amazônia | 9.0 |
| 4606b888-f8bc-3b21-b239-9f2678c88c9e | -14.65127 | -46.54408 | 2025-11-17 00:52:00 | TERRA_M-M | ALVORADA DO NORTE | GOIÁS | Brasil | 5200803 | 52 | 33 | nan | nan | nan | Cerrado | 18.8 |
| f5ec46de-0640-31e5-9c66-aba6eecc505e | -12.1942 | -54.26892 | 2025-11-17 00:52:00 | TERRA_M-M | FELIZ NATAL | MATO GROSSO | Brasil | 5103700 | 51 | 33 | nan | nan | nan | Amazônia | 21.2 |


[Clique aqui para ver as próximas entradas](README6.md)
