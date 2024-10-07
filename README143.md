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

## Dados Diários - Página 143

| ID | Latitude | Longitude | Data/Hora GMT | Satélite | Município | Estado | País | Município ID | Estado ID | País ID | Dias sem Chuva | Precipitação | Risco de Fogo | Bioma | FRP |
|----|----------|-----------|---------------|----------|-----------|--------|------|--------------|-----------|---------|----------------|--------------|----------------|-------|-----|
| b5e14800-bd69-3385-aaac-12411d8249e8 | -17.1581 | -57.3582 | 2024-10-07 06:46:43 | GOES-16 | POCONÉ | MATO GROSSO | Brasil | 5106505 | 51 | 33 | nan | nan | nan | Pantanal | 84.5 |
| 83ff5b4e-8649-3078-b567-75ba29a6e368 | -17.1584 | -57.3377 | 2024-10-07 06:46:43 | GOES-16 | POCONÉ | MATO GROSSO | Brasil | 5106505 | 51 | 33 | nan | nan | nan | Pantanal | 103.1 |
| d5639eda-6f52-3b58-99fb-87fd3696cbac | -17.1777 | -57.3559 | 2024-10-07 06:46:43 | GOES-16 | CÁCERES | MATO GROSSO | Brasil | 5102504 | 51 | 33 | nan | nan | nan | Pantanal | 75.9 |
| e17bd2a6-d4ce-3ee3-b5e1-ef4c845c1e60 | -17.178 | -57.3354 | 2024-10-07 06:46:43 | GOES-16 | POCONÉ | MATO GROSSO | Brasil | 5106505 | 51 | 33 | nan | nan | nan | Pantanal | 96.3 |
| 92ffd586-6f8b-32a9-bb04-2ff8c3cfc3b5 | -17.7324 | -57.0833 | 2024-10-07 06:46:46 | GOES-16 | POCONÉ | MATO GROSSO | Brasil | 5106505 | 51 | 33 | nan | nan | nan | Pantanal | 78.3 |
| 613991d3-91b2-36bc-980b-72e00189ebef | -17.7327 | -57.0627 | 2024-10-07 06:46:46 | GOES-16 | POCONÉ | MATO GROSSO | Brasil | 5106505 | 51 | 33 | nan | nan | nan | Pantanal | 70.9 |
| 59ab9b83-14d1-390e-8c9a-e86aa89ffbee | -18.6391 | -57.2578 | 2024-10-07 06:46:51 | GOES-16 | CORUMBÁ | MATO GROSSO DO SUL | Brasil | 5003207 | 50 | 33 | nan | nan | nan | Pantanal | 114.6 |
| d10b189c-1beb-3255-b08a-c9e1c3b12c59 | -18.659 | -57.2552 | 2024-10-07 06:46:51 | GOES-16 | CORUMBÁ | MATO GROSSO DO SUL | Brasil | 5003207 | 50 | 33 | nan | nan | nan | Pantanal | 99.5 |
| ccf0acf7-a553-313a-ab4a-d7b50db1ab0a | -18.6789 | -57.2526 | 2024-10-07 06:46:51 | GOES-16 | CORUMBÁ | MATO GROSSO DO SUL | Brasil | 5003207 | 50 | 33 | nan | nan | nan | Pantanal | 72.4 |
| 8c759eca-b517-347f-9f94-9aa8a6463bd7 | -16.5072 | -57.7387 | 2024-10-07 06:56:39 | GOES-16 | CÁCERES | MATO GROSSO | Brasil | 5102504 | 51 | 33 | nan | nan | nan | Pantanal | 54.4 |
| a8a03074-adad-386f-a5b7-dd343e30c7f4 | -16.5267 | -57.7365 | 2024-10-07 06:56:40 | GOES-16 | CÁCERES | MATO GROSSO | Brasil | 5102504 | 51 | 33 | nan | nan | nan | Pantanal | 84.8 |
| d15f5b6e-9aea-33b4-9294-80ade1bd371f | -16.614 | -57.135 | 2024-10-07 06:56:40 | GOES-16 | POCONÉ | MATO GROSSO | Brasil | 5106505 | 51 | 33 | nan | nan | nan | Pantanal | 55.5 |
| 1eddd4d7-0894-321a-9045-930405f25878 | -16.6332 | -57.1533 | 2024-10-07 06:56:40 | GOES-16 | POCONÉ | MATO GROSSO | Brasil | 5106505 | 51 | 33 | nan | nan | nan | Pantanal | 65.6 |
| 4a775ed9-0e12-3c45-9eb8-e950bdb1553e | -16.6335 | -57.1328 | 2024-10-07 06:56:40 | GOES-16 | POCONÉ | MATO GROSSO | Brasil | 5106505 | 51 | 33 | nan | nan | nan | Pantanal | 66.0 |
| e05e1c5d-b15a-3a9d-987b-3156e38184b1 | -16.9521 | -56.7669 | 2024-10-07 06:56:42 | GOES-16 | POCONÉ | MATO GROSSO | Brasil | 5106505 | 51 | 33 | nan | nan | nan | Pantanal | 66.1 |
| d0ae5e8f-b6ef-35f6-8644-d50cdbfbd51d | -16.9717 | -56.7646 | 2024-10-07 06:56:42 | GOES-16 | POCONÉ | MATO GROSSO | Brasil | 5106505 | 51 | 33 | nan | nan | nan | Pantanal | 107.9 |
| 61282912-870f-3e89-b223-a63a418d3851 | -16.9721 | -56.744 | 2024-10-07 06:56:42 | GOES-16 | POCONÉ | MATO GROSSO | Brasil | 5106505 | 51 | 33 | nan | nan | nan | Pantanal | 85.4 |
| ea282094-197d-369b-b326-8e4c3d71a25f | -16.9741 | -56.6202 | 2024-10-07 06:56:42 | GOES-16 | BARÃO DE MELGAÇO | MATO GROSSO | Brasil | 5101605 | 51 | 33 | nan | nan | nan | Pantanal | 58.6 |
| a9cdff0b-1f95-3bd4-8cae-34060ea74e1f | -16.9744 | -56.5996 | 2024-10-07 06:56:42 | GOES-16 | BARÃO DE MELGAÇO | MATO GROSSO | Brasil | 5101605 | 51 | 33 | nan | nan | nan | Pantanal | 74.6 |
| 63996abe-0707-3abf-b77f-3dce127f15b0 | -16.9924 | -56.7003 | 2024-10-07 06:56:42 | GOES-16 | POCONÉ | MATO GROSSO | Brasil | 5106505 | 51 | 33 | nan | nan | nan | Pantanal | 52.6 |
| c3e3de1c-d2a3-3b54-9d26-6eb42880becf | -17.012 | -56.698 | 2024-10-07 06:56:42 | GOES-16 | POCONÉ | MATO GROSSO | Brasil | 5106505 | 51 | 33 | nan | nan | nan | Pantanal | 94.1 |
| ec4231f4-69e9-3462-bc76-4511389ed3e4 | -17.0123 | -56.6773 | 2024-10-07 06:56:42 | GOES-16 | POCONÉ | MATO GROSSO | Brasil | 5106505 | 51 | 33 | nan | nan | nan | Pantanal | 155.9 |
| 64d3743d-eca0-36d4-a84d-a9b031072215 | -17.0316 | -56.6956 | 2024-10-07 06:56:42 | GOES-16 | POCONÉ | MATO GROSSO | Brasil | 5106505 | 51 | 33 | nan | nan | nan | Pantanal | 89.5 |
| 4ca33165-d9a7-3466-8223-9a222ae08ae9 | -17.0319 | -56.6749 | 2024-10-07 06:56:42 | GOES-16 | POCONÉ | MATO GROSSO | Brasil | 5106505 | 51 | 33 | nan | nan | nan | Pantanal | 165.8 |
| ae306af1-32ea-3deb-8092-92405ce982e6 | -17.0323 | -56.6543 | 2024-10-07 06:56:42 | GOES-16 | POCONÉ | MATO GROSSO | Brasil | 5106505 | 51 | 33 | nan | nan | nan | Pantanal | 50.6 |
| 0edc4199-4684-3d7e-b45a-b626558b76b2 | -17.0982 | -57.4267 | 2024-10-07 06:56:43 | GOES-16 | CÁCERES | MATO GROSSO | Brasil | 5102504 | 51 | 33 | nan | nan | nan | Pantanal | 80.6 |
| 437d3532-4ae4-36a6-af7d-7616e11d59c9 | -17.0985 | -57.4062 | 2024-10-07 06:56:43 | GOES-16 | CÁCERES | MATO GROSSO | Brasil | 5102504 | 51 | 33 | nan | nan | nan | Pantanal | 74.2 |
| e954e88c-95e9-30d3-bec4-8d61b5472d0c | -17.1581 | -57.3582 | 2024-10-07 06:56:43 | GOES-16 | POCONÉ | MATO GROSSO | Brasil | 5106505 | 51 | 33 | nan | nan | nan | Pantanal | 77.1 |
| 48a04dbb-51ed-36a1-b22d-199a08afc3bb | -17.1584 | -57.3377 | 2024-10-07 06:56:43 | GOES-16 | POCONÉ | MATO GROSSO | Brasil | 5106505 | 51 | 33 | nan | nan | nan | Pantanal | 88.9 |
| eac3229d-73fc-32f0-ae90-39d3957fa0a0 | -17.1777 | -57.3559 | 2024-10-07 06:56:43 | GOES-16 | CÁCERES | MATO GROSSO | Brasil | 5102504 | 51 | 33 | nan | nan | nan | Pantanal | 64.7 |
| 58679d27-1bee-3c8d-81d9-0033839f03d5 | -17.178 | -57.3354 | 2024-10-07 06:56:43 | GOES-16 | POCONÉ | MATO GROSSO | Brasil | 5106505 | 51 | 33 | nan | nan | nan | Pantanal | 75.0 |
| f580636f-affe-391c-a31a-1ebb3c8106d3 | -17.7324 | -57.0833 | 2024-10-07 06:56:46 | GOES-16 | POCONÉ | MATO GROSSO | Brasil | 5106505 | 51 | 33 | nan | nan | nan | Pantanal | 66.7 |
| ce24d3d1-cbf5-384f-8928-13b1c5862e13 | -17.7918 | -53.8102 | 2024-10-07 06:56:46 | GOES-16 | ALTO ARAGUAIA | MATO GROSSO | Brasil | 5100300 | 51 | 33 | nan | nan | nan | Cerrado | 68.5 |
| 48fbf6ec-7e3c-3bcf-b5f4-bf40560c2916 | -18.6391 | -57.2578 | 2024-10-07 06:56:51 | GOES-16 | CORUMBÁ | MATO GROSSO DO SUL | Brasil | 5003207 | 50 | 33 | nan | nan | nan | Pantanal | 221.1 |
| d315a3f6-249e-3fb4-9247-61c6695b724c | -18.6394 | -57.237 | 2024-10-07 06:56:51 | GOES-16 | CORUMBÁ | MATO GROSSO DO SUL | Brasil | 5003207 | 50 | 33 | nan | nan | nan | Pantanal | 122.1 |
| fd300a7c-6aff-3676-b5fc-149cfe027a99 | -18.659 | -57.2552 | 2024-10-07 06:56:51 | GOES-16 | CORUMBÁ | MATO GROSSO DO SUL | Brasil | 5003207 | 50 | 33 | nan | nan | nan | Pantanal | 288.0 |
| 08d28427-b012-3820-9527-25acf77dec45 | -18.6593 | -57.2344 | 2024-10-07 06:56:51 | GOES-16 | CORUMBÁ | MATO GROSSO DO SUL | Brasil | 5003207 | 50 | 33 | nan | nan | nan | Pantanal | 191.4 |
| ef29e486-57da-3bd1-9b6c-41028f62fc4c | -18.6789 | -57.2526 | 2024-10-07 06:56:51 | GOES-16 | CORUMBÁ | MATO GROSSO DO SUL | Brasil | 5003207 | 50 | 33 | nan | nan | nan | Pantanal | 182.9 |
| 09692275-1d82-3483-889a-48fd0a2013cc | -18.6984 | -57.2708 | 2024-10-07 06:56:51 | GOES-16 | CORUMBÁ | MATO GROSSO DO SUL | Brasil | 5003207 | 50 | 33 | nan | nan | nan | Pantanal | 63.9 |
| a66157f6-bbd6-3f79-a3f2-1bf4b1924086 | -21.5698 | -47.746 | 2024-10-07 06:57:05 | GOES-16 | LUÍS ANTÔNIO | SÃO PAULO | Brasil | 3527603 | 35 | 33 | nan | nan | nan | Cerrado | 80.0 |
| 971eb7f9-b06c-3599-8c31-9a3887f8de10 | -21.5906 | -47.7409 | 2024-10-07 06:57:05 | GOES-16 | LUÍS ANTÔNIO | SÃO PAULO | Brasil | 3527603 | 35 | 33 | nan | nan | nan | Cerrado | 113.5 |
| c7ae0848-5254-3ad6-9a7d-36f711993a7f | -21.5913 | -47.7172 | 2024-10-07 06:57:05 | GOES-16 | LUÍS ANTÔNIO | SÃO PAULO | Brasil | 3527603 | 35 | 33 | nan | nan | nan | Cerrado | 91.4 |
| 0a523054-2454-3b13-b266-b228e2bd232a | -21.605 | -47.9485 | 2024-10-07 06:57:05 | GOES-16 | RINCÃO | SÃO PAULO | Brasil | 3543709 | 35 | 33 | nan | nan | nan | Cerrado | 93.7 |
| 595da686-c1d0-31af-aab7-6172e5d5a955 | -7.46779 | -72.68401 | 2024-10-07 06:59:00 | NPP-375D | GUAJARÁ | AMAZONAS | Brasil | 1301654 | 13 | 33 | nan | nan | nan | Amazônia | 1.0 |
| d1e02f6e-4798-3023-9286-f88e300c6829 | -7.46713 | -72.68913 | 2024-10-07 06:59:00 | NPP-375D | GUAJARÁ | AMAZONAS | Brasil | 1301654 | 13 | 33 | nan | nan | nan | Amazônia | 1.0 |
| bfd974c8-9be2-34ce-83d2-26d00f6d7444 | -20.34 | -48.84 | 2024-10-07 07:03:27 | MSG-03 | COLÔMBIA | SÃO PAULO | Brasil | 3512100 | 35 | 33 | nan | nan | nan | Cerrado | nan |
| 32c98451-30b0-304f-aafd-83f30d92ffd2 | -20.34 | -48.78 | 2024-10-07 07:03:27 | MSG-03 | COLÔMBIA | SÃO PAULO | Brasil | 3512100 | 35 | 33 | nan | nan | nan | Cerrado | nan |
| d334b8fc-b520-377c-bfbf-07669464b442 | -16.5267 | -57.7365 | 2024-10-07 07:06:40 | GOES-16 | CÁCERES | MATO GROSSO | Brasil | 5102504 | 51 | 33 | nan | nan | nan | Pantanal | 54.4 |
| ea21decf-b103-3e27-990c-af6a5d848717 | -16.5745 | -57.16 | 2024-10-07 07:06:40 | GOES-16 | POCONÉ | MATO GROSSO | Brasil | 5106505 | 51 | 33 | nan | nan | nan | Pantanal | 56.2 |
| a0220ae6-766e-388d-aa8a-a86ac3365dda | -16.5749 | -57.1395 | 2024-10-07 07:06:40 | GOES-16 | POCONÉ | MATO GROSSO | Brasil | 5106505 | 51 | 33 | nan | nan | nan | Pantanal | 62.5 |
| bdcd4d0a-fb81-383f-80a7-6d88c7d117da | -16.6136 | -57.1555 | 2024-10-07 07:06:40 | GOES-16 | POCONÉ | MATO GROSSO | Brasil | 5106505 | 51 | 33 | nan | nan | nan | Pantanal | 55.6 |
| a3e09e06-1eb6-3d2e-be24-6bb6106de41a | -16.614 | -57.135 | 2024-10-07 07:06:40 | GOES-16 | POCONÉ | MATO GROSSO | Brasil | 5106505 | 51 | 33 | nan | nan | nan | Pantanal | 58.4 |
| 9d1533d6-ddc8-36a4-a1df-dbf438de0141 | -16.6332 | -57.1533 | 2024-10-07 07:06:40 | GOES-16 | POCONÉ | MATO GROSSO | Brasil | 5106505 | 51 | 33 | nan | nan | nan | Pantanal | 60.2 |
| e75cf24d-a46a-38da-99ed-f8d5d967d789 | -16.6335 | -57.1328 | 2024-10-07 07:06:40 | GOES-16 | POCONÉ | MATO GROSSO | Brasil | 5106505 | 51 | 33 | nan | nan | nan | Pantanal | 58.4 |
| 31c997e3-7545-3f18-88de-b2ff775ef76e | -16.9717 | -56.7646 | 2024-10-07 07:06:42 | GOES-16 | POCONÉ | MATO GROSSO | Brasil | 5106505 | 51 | 33 | nan | nan | nan | Pantanal | 121.4 |
| a8c8824a-76f7-3185-a798-2a0eb0968fc6 | -16.9721 | -56.744 | 2024-10-07 07:06:42 | GOES-16 | POCONÉ | MATO GROSSO | Brasil | 5106505 | 51 | 33 | nan | nan | nan | Pantanal | 97.8 |
| 968b4ac5-393f-30ac-86af-d3d80d3b3041 | -16.9741 | -56.6202 | 2024-10-07 07:06:42 | GOES-16 | BARÃO DE MELGAÇO | MATO GROSSO | Brasil | 5101605 | 51 | 33 | nan | nan | nan | Pantanal | 70.8 |
| 68033219-1a11-3bd7-8fbf-7ba6c393cbd5 | -16.9744 | -56.5996 | 2024-10-07 07:06:42 | GOES-16 | BARÃO DE MELGAÇO | MATO GROSSO | Brasil | 5101605 | 51 | 33 | nan | nan | nan | Pantanal | 91.7 |
| 99156754-1e36-3395-a965-fe864a2a1121 | -17.0982 | -57.4267 | 2024-10-07 07:06:43 | GOES-16 | CÁCERES | MATO GROSSO | Brasil | 5102504 | 51 | 33 | nan | nan | nan | Pantanal | 71.4 |
| d5900334-adbe-3f83-9370-dd6b7a25780d | -17.0985 | -57.4062 | 2024-10-07 07:06:43 | GOES-16 | CÁCERES | MATO GROSSO | Brasil | 5102504 | 51 | 33 | nan | nan | nan | Pantanal | 71.1 |
| 2313a279-b5a5-3239-93f4-aafae488d1a8 | -17.1481 | -56.7638 | 2024-10-07 07:06:43 | GOES-16 | POCONÉ | MATO GROSSO | Brasil | 5106505 | 51 | 33 | nan | nan | nan | Pantanal | 54.3 |
| 2a277272-7f02-3f89-b6a8-39954a662f5e | -17.1484 | -56.7431 | 2024-10-07 07:06:43 | GOES-16 | POCONÉ | MATO GROSSO | Brasil | 5106505 | 51 | 33 | nan | nan | nan | Pantanal | 52.0 |
| fcba6587-59a3-3fa0-b78a-0c4736fb41b0 | -17.1581 | -57.3582 | 2024-10-07 07:06:43 | GOES-16 | POCONÉ | MATO GROSSO | Brasil | 5106505 | 51 | 33 | nan | nan | nan | Pantanal | 78.4 |
| 04a8f6c9-6a1d-3d3a-aa3b-a29af1fce39a | -17.1584 | -57.3377 | 2024-10-07 07:06:43 | GOES-16 | POCONÉ | MATO GROSSO | Brasil | 5106505 | 51 | 33 | nan | nan | nan | Pantanal | 89.0 |
| 54c7612a-78a2-3fa3-a1d4-d2073c762174 | -17.1777 | -57.3559 | 2024-10-07 07:06:43 | GOES-16 | CÁCERES | MATO GROSSO | Brasil | 5102504 | 51 | 33 | nan | nan | nan | Pantanal | 67.1 |
| d4e1834b-86a7-3af2-a7f2-fead5beb8d3d | -17.178 | -57.3354 | 2024-10-07 07:06:43 | GOES-16 | POCONÉ | MATO GROSSO | Brasil | 5106505 | 51 | 33 | nan | nan | nan | Pantanal | 75.5 |
| ce51792b-02fa-3382-b8fb-c12acce51154 | -20.3321 | -48.8231 | 2024-10-07 07:06:59 | GOES-16 | COLÔMBIA | SÃO PAULO | Brasil | 3512100 | 35 | 33 | nan | nan | nan | Cerrado | 155.4 |
| a6bc160b-1a25-3bcb-9b2d-7950523db0e0 | -20.3327 | -48.8 | 2024-10-07 07:06:59 | GOES-16 | COLÔMBIA | SÃO PAULO | Brasil | 3512100 | 35 | 33 | nan | nan | nan | Cerrado | 96.4 |
| 5092cd69-a4a8-3de3-b031-0d836b027e48 | -20.3525 | -48.8186 | 2024-10-07 07:06:59 | GOES-16 | COLÔMBIA | SÃO PAULO | Brasil | 3512100 | 35 | 33 | nan | nan | nan | Cerrado | 360.3 |
| 2d4acd51-ad22-3c23-a5cb-6be7d3217b04 | -20.3532 | -48.7955 | 2024-10-07 07:06:59 | GOES-16 | COLÔMBIA | SÃO PAULO | Brasil | 3512100 | 35 | 33 | nan | nan | nan | Cerrado | 213.9 |
| 7cd2e316-8c50-3809-81b7-bcc93ee35d7d | -20.373 | -48.8141 | 2024-10-07 07:06:59 | GOES-16 | COLÔMBIA | SÃO PAULO | Brasil | 3512100 | 35 | 33 | nan | nan | nan | Cerrado | 60.3 |
| ba8a3db9-8ab5-33ab-a01f-8347b5436b18 | -20.5848 | -48.5137 | 2024-10-07 07:07:00 | GOES-16 | BARRETOS | SÃO PAULO | Brasil | 3505500 | 35 | 33 | nan | nan | nan | Cerrado | 80.9 |
| eacc3e1d-0240-3888-8aa5-0ab9ba427130 | -21.5698 | -47.746 | 2024-10-07 07:07:05 | GOES-16 | LUÍS ANTÔNIO | SÃO PAULO | Brasil | 3527603 | 35 | 33 | nan | nan | nan | Cerrado | 74.3 |
| 66cb7a7c-aaad-3f9b-a9a5-bb14204db360 | -21.5843 | -47.9536 | 2024-10-07 07:07:05 | GOES-16 | GUATAPARÁ | SÃO PAULO | Brasil | 3518859 | 35 | 33 | nan | nan | nan | Cerrado | 46.2 |
| 413d9422-dcac-3e23-97da-bd9c76c8a309 | -21.5906 | -47.7409 | 2024-10-07 07:07:05 | GOES-16 | LUÍS ANTÔNIO | SÃO PAULO | Brasil | 3527603 | 35 | 33 | nan | nan | nan | Cerrado | 128.1 |
| 891ba583-7212-35e3-85f6-5ced2b0d0047 | -21.5913 | -47.7172 | 2024-10-07 07:07:05 | GOES-16 | LUÍS ANTÔNIO | SÃO PAULO | Brasil | 3527603 | 35 | 33 | nan | nan | nan | Cerrado | 87.8 |
| c2c90973-c2c9-34ce-a237-7f7ad12f9c57 | -21.605 | -47.9485 | 2024-10-07 07:07:05 | GOES-16 | RINCÃO | SÃO PAULO | Brasil | 3543709 | 35 | 33 | nan | nan | nan | Cerrado | 69.1 |
| aaca60ab-5e85-31e3-9e9b-2d6e034e3f9a | -16.5072 | -57.7387 | 2024-10-07 07:16:39 | GOES-16 | CÁCERES | MATO GROSSO | Brasil | 5102504 | 51 | 33 | nan | nan | nan | Pantanal | 56.7 |
| b492db25-ec20-37a6-9091-a9770532a20d | -16.6332 | -57.1533 | 2024-10-07 07:16:40 | GOES-16 | POCONÉ | MATO GROSSO | Brasil | 5106505 | 51 | 33 | nan | nan | nan | Pantanal | 62.6 |
| b68186ed-48de-3e8a-b2e4-f7e428c3156a | -16.6335 | -57.1328 | 2024-10-07 07:16:40 | GOES-16 | POCONÉ | MATO GROSSO | Brasil | 5106505 | 51 | 33 | nan | nan | nan | Pantanal | 61.9 |
| 75126985-d52e-3d55-9545-8c9fbec0e695 | -16.5267 | -57.7365 | 2024-10-07 07:16:40 | GOES-16 | CÁCERES | MATO GROSSO | Brasil | 5102504 | 51 | 33 | nan | nan | nan | Pantanal | 65.7 |
| 37f11c76-d50b-3647-b260-1842d4dcc908 | -16.6136 | -57.1555 | 2024-10-07 07:16:40 | GOES-16 | POCONÉ | MATO GROSSO | Brasil | 5106505 | 51 | 33 | nan | nan | nan | Pantanal | 52.7 |
| 8682df5c-7b4d-3312-8b10-75675ace7be1 | -16.614 | -57.135 | 2024-10-07 07:16:40 | GOES-16 | POCONÉ | MATO GROSSO | Brasil | 5106505 | 51 | 33 | nan | nan | nan | Pantanal | 57.3 |
| 410ac836-b565-3730-98ac-5b36db3cb0cc | -16.9717 | -56.7646 | 2024-10-07 07:16:42 | GOES-16 | POCONÉ | MATO GROSSO | Brasil | 5106505 | 51 | 33 | nan | nan | nan | Pantanal | 82.5 |
| cf7e9226-8012-3a17-99b7-6009a140f733 | -16.9721 | -56.744 | 2024-10-07 07:16:42 | GOES-16 | POCONÉ | MATO GROSSO | Brasil | 5106505 | 51 | 33 | nan | nan | nan | Pantanal | 63.0 |
| 20e29036-3b8b-351e-9a88-6811687a328e | -16.9741 | -56.6202 | 2024-10-07 07:16:42 | GOES-16 | BARÃO DE MELGAÇO | MATO GROSSO | Brasil | 5101605 | 51 | 33 | nan | nan | nan | Pantanal | 96.8 |
| c592191c-db02-35bf-ba31-2ca91b566bdf | -16.9744 | -56.5996 | 2024-10-07 07:16:42 | GOES-16 | BARÃO DE MELGAÇO | MATO GROSSO | Brasil | 5101605 | 51 | 33 | nan | nan | nan | Pantanal | 125.5 |
| 3e4c4062-3261-3d47-ad68-54b94dd19a1a | -16.9937 | -56.6178 | 2024-10-07 07:16:42 | GOES-16 | POCONÉ | MATO GROSSO | Brasil | 5106505 | 51 | 33 | nan | nan | nan | Pantanal | 69.9 |
| fbb03fca-01ed-3468-901d-8d44cbe13590 | -16.994 | -56.5972 | 2024-10-07 07:16:42 | GOES-16 | BARÃO DE MELGAÇO | MATO GROSSO | Brasil | 5101605 | 51 | 33 | nan | nan | nan | Pantanal | 88.6 |
| aac5624d-d185-37d5-9002-d2993c71f587 | -17.012 | -56.698 | 2024-10-07 07:16:42 | GOES-16 | POCONÉ | MATO GROSSO | Brasil | 5106505 | 51 | 33 | nan | nan | nan | Pantanal | 125.6 |
| a495daaf-c4a9-30a3-ab7c-9913d1bb24dc | -17.0123 | -56.6773 | 2024-10-07 07:16:42 | GOES-16 | POCONÉ | MATO GROSSO | Brasil | 5106505 | 51 | 33 | nan | nan | nan | Pantanal | 286.7 |
| 54d81993-70a9-3c19-8b16-212f0d9c02d8 | -17.0127 | -56.6567 | 2024-10-07 07:16:42 | GOES-16 | POCONÉ | MATO GROSSO | Brasil | 5106505 | 51 | 33 | nan | nan | nan | Pantanal | 73.7 |
| d1805b8a-4147-3b86-9f3f-d11fdd99fbe7 | -17.0316 | -56.6956 | 2024-10-07 07:16:42 | GOES-16 | POCONÉ | MATO GROSSO | Brasil | 5106505 | 51 | 33 | nan | nan | nan | Pantanal | 117.6 |
| 17654e88-2e97-31e1-9397-e34953cb32cf | -17.0319 | -56.6749 | 2024-10-07 07:16:42 | GOES-16 | POCONÉ | MATO GROSSO | Brasil | 5106505 | 51 | 33 | nan | nan | nan | Pantanal | 239.3 |
| 6bb22b56-a88b-3b18-927b-526e43de621f | -17.0323 | -56.6543 | 2024-10-07 07:16:42 | GOES-16 | POCONÉ | MATO GROSSO | Brasil | 5106505 | 51 | 33 | nan | nan | nan | Pantanal | 64.7 |
| 8d66a549-7768-398b-8f77-5b27a0a0a1c9 | -17.0982 | -57.4267 | 2024-10-07 07:16:43 | GOES-16 | CÁCERES | MATO GROSSO | Brasil | 5102504 | 51 | 33 | nan | nan | nan | Pantanal | 63.0 |
| cff87816-058f-3960-b490-33be102333a2 | -17.0985 | -57.4062 | 2024-10-07 07:16:43 | GOES-16 | CÁCERES | MATO GROSSO | Brasil | 5102504 | 51 | 33 | nan | nan | nan | Pantanal | 63.4 |
| 495a0946-1c38-31d5-806a-aaa36f044e94 | -17.1481 | -56.7638 | 2024-10-07 07:16:43 | GOES-16 | POCONÉ | MATO GROSSO | Brasil | 5106505 | 51 | 33 | nan | nan | nan | Pantanal | 60.2 |
| ccbeca63-d498-34fb-82fb-796b1c6102f3 | -17.1484 | -56.7431 | 2024-10-07 07:16:43 | GOES-16 | POCONÉ | MATO GROSSO | Brasil | 5106505 | 51 | 33 | nan | nan | nan | Pantanal | 55.7 |
| f56ab08e-e398-3d15-98cd-85ec3f8269f9 | -17.1581 | -57.3582 | 2024-10-07 07:16:43 | GOES-16 | POCONÉ | MATO GROSSO | Brasil | 5106505 | 51 | 33 | nan | nan | nan | Pantanal | 85.8 |


[Clique aqui para ver as próximas entradas](README144.md)
