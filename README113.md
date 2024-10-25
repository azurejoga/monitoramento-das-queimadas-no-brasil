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

## Dados Diários - Página 113

| ID | Latitude | Longitude | Data/Hora GMT | Satélite | Município | Estado | País | Município ID | Estado ID | País ID | Dias sem Chuva | Precipitação | Risco de Fogo | Bioma | FRP |
|----|----------|-----------|---------------|----------|-----------|--------|------|--------------|-----------|---------|----------------|--------------|----------------|-------|-----|
| 6ab90e6b-6ba7-3092-92ea-125a56846ea6 | -18.321 | -56.1777 | 2024-10-25 12:36:48 | GOES-16 | CORUMBÁ | MATO GROSSO DO SUL | Brasil | 5003207 | 50 | 33 | nan | nan | nan | Pantanal | 119.9 |
| 94c4bd2a-1907-3f1a-9cf4-86396a6de943 | -18.3398 | -56.2377 | 2024-10-25 12:36:48 | GOES-16 | CORUMBÁ | MATO GROSSO DO SUL | Brasil | 5003207 | 50 | 33 | nan | nan | nan | Pantanal | 101.4 |
| dc535b77-6107-310d-9fb7-dd3a87567b0c | -18.3012 | -56.1804 | 2024-10-25 12:36:48 | GOES-16 | CORUMBÁ | MATO GROSSO DO SUL | Brasil | 5003207 | 50 | 33 | nan | nan | nan | Pantanal | 102.5 |
| b6c11745-a81c-3d4e-a61f-d223a5bef455 | -19.6442 | -56.8311 | 2024-10-25 12:36:55 | GOES-16 | AQUIDAUANA | MATO GROSSO DO SUL | Brasil | 5001102 | 50 | 33 | nan | nan | nan | Pantanal | 70.3 |
| 1f325898-f055-3f27-8da7-355511a6c0bb | -19.6438 | -56.8521 | 2024-10-25 12:36:55 | GOES-16 | AQUIDAUANA | MATO GROSSO DO SUL | Brasil | 5001102 | 50 | 33 | nan | nan | nan | Pantanal | 71.0 |
| be691cba-7966-3bea-9cdc-98e4abda6760 | -12.5272 | -43.3782 | 2024-10-25 12:46:15 | GOES-16 | MUQUÉM DO SÃO FRANCISCO | BAHIA | Brasil | 2922250 | 29 | 33 | nan | nan | nan | Cerrado | 86.8 |
| c8326ac2-3385-3be1-bf51-d0ccb49169f3 | -16.554 | -57.2237 | 2024-10-25 12:46:39 | GOES-16 | POCONÉ | MATO GROSSO | Brasil | 5106505 | 51 | 33 | nan | nan | nan | Pantanal | 90.1 |
| 1892a67d-d5bf-35f9-a017-a49729444fba | -16.94 | -57.5268 | 2024-10-25 12:46:41 | GOES-16 | CÁCERES | MATO GROSSO | Brasil | 5102504 | 51 | 33 | nan | nan | nan | Pantanal | 87.0 |
| 7be66873-cbba-334a-b898-8c33a88891b1 | -16.9596 | -57.5245 | 2024-10-25 12:46:41 | GOES-16 | CÁCERES | MATO GROSSO | Brasil | 5102504 | 51 | 33 | nan | nan | nan | Pantanal | 91.2 |
| 3f6341da-9927-3ce9-95c8-859c203b2ae4 | -17.2386 | -57.2256 | 2024-10-25 12:46:42 | GOES-16 | POCONÉ | MATO GROSSO | Brasil | 5106505 | 51 | 33 | nan | nan | nan | Pantanal | 613.2 |
| 13a7ea29-8263-378b-a467-1c288d1bfe07 | -17.219 | -57.228 | 2024-10-25 12:46:42 | GOES-16 | POCONÉ | MATO GROSSO | Brasil | 5106505 | 51 | 33 | nan | nan | nan | Pantanal | 778.0 |
| b5d40d73-a176-365f-b472-5bbe2be579da | -17.0789 | -57.4085 | 2024-10-25 12:46:42 | GOES-16 | CÁCERES | MATO GROSSO | Brasil | 5102504 | 51 | 33 | nan | nan | nan | Pantanal | 137.0 |
| 7f2592a7-fc29-319f-999d-03ee5c2f0914 | -17.2383 | -57.2462 | 2024-10-25 12:46:42 | GOES-16 | POCONÉ | MATO GROSSO | Brasil | 5106505 | 51 | 33 | nan | nan | nan | Pantanal | 190.7 |
| 5dcf6587-5a02-35e5-815b-a26dd526223b | -17.2186 | -57.2485 | 2024-10-25 12:46:42 | GOES-16 | POCONÉ | MATO GROSSO | Brasil | 5106505 | 51 | 33 | nan | nan | nan | Pantanal | 244.0 |
| e4f36c64-7712-32cd-a20e-dfe5c5c2242f | -17.0786 | -57.429 | 2024-10-25 12:46:42 | GOES-16 | CÁCERES | MATO GROSSO | Brasil | 5102504 | 51 | 33 | nan | nan | nan | Pantanal | 90.9 |
| 8fec49ba-490a-3461-b292-665c0c40f990 | -17.2769 | -57.2826 | 2024-10-25 12:46:43 | GOES-16 | POCONÉ | MATO GROSSO | Brasil | 5106505 | 51 | 33 | nan | nan | nan | Pantanal | 86.3 |
| 8ea903ab-7986-30b4-be7e-d1ac1d8d7137 | -17.2966 | -57.2803 | 2024-10-25 12:46:43 | GOES-16 | POCONÉ | MATO GROSSO | Brasil | 5106505 | 51 | 33 | nan | nan | nan | Pantanal | 86.3 |
| 7bad10c7-1f39-3a4f-ab37-de7c559eb5f0 | -17.2586 | -57.2027 | 2024-10-25 12:46:43 | GOES-16 | POCONÉ | MATO GROSSO | Brasil | 5106505 | 51 | 33 | nan | nan | nan | Pantanal | 86.0 |
| 46b69b0a-f809-38ab-8779-006f08c782df | -17.2583 | -57.2233 | 2024-10-25 12:46:43 | GOES-16 | POCONÉ | MATO GROSSO | Brasil | 5106505 | 51 | 33 | nan | nan | nan | Pantanal | 105.0 |
| 0f43609e-283d-35bc-8769-38529c712a4d | -17.6868 | -57.4593 | 2024-10-25 12:46:45 | GOES-16 | POCONÉ | MATO GROSSO | Brasil | 5106505 | 51 | 33 | nan | nan | nan | Pantanal | 90.5 |
| 7ce4dc13-c1fd-3e8f-a1b0-5ed0b95b3483 | -17.7644 | -57.532 | 2024-10-25 12:46:45 | GOES-16 | POCONÉ | MATO GROSSO | Brasil | 5106505 | 51 | 33 | nan | nan | nan | Pantanal | 151.7 |
| 770e2fbd-8559-38c4-a1f7-29c3d0afc614 | -17.765 | -57.4909 | 2024-10-25 12:46:45 | GOES-16 | POCONÉ | MATO GROSSO | Brasil | 5106505 | 51 | 33 | nan | nan | nan | Pantanal | 116.8 |
| 4175afcb-938c-3736-96ef-23cb17faf701 | -17.7453 | -57.4933 | 2024-10-25 12:46:45 | GOES-16 | POCONÉ | MATO GROSSO | Brasil | 5106505 | 51 | 33 | nan | nan | nan | Pantanal | 135.4 |
| ff82ff27-a3bc-3b09-af31-00cd42eefe2e | -17.7446 | -57.5344 | 2024-10-25 12:46:45 | GOES-16 | POCONÉ | MATO GROSSO | Brasil | 5106505 | 51 | 33 | nan | nan | nan | Pantanal | 94.3 |
| 55d511ec-8cea-31de-93a5-a2312e9a3943 | -17.7647 | -57.5115 | 2024-10-25 12:46:45 | GOES-16 | POCONÉ | MATO GROSSO | Brasil | 5106505 | 51 | 33 | nan | nan | nan | Pantanal | 144.1 |
| b2355820-3062-371b-95bf-44ee7d688a3f | -17.6888 | -57.3357 | 2024-10-25 12:46:45 | GOES-16 | POCONÉ | MATO GROSSO | Brasil | 5106505 | 51 | 33 | nan | nan | nan | Pantanal | 111.7 |
| 513c9b06-5fb8-3c48-8bd0-2fb73119bfb9 | -17.6865 | -57.4798 | 2024-10-25 12:46:45 | GOES-16 | POCONÉ | MATO GROSSO | Brasil | 5106505 | 51 | 33 | nan | nan | nan | Pantanal | 85.7 |
| 7c9a6a08-6926-3a59-96bd-51f7a43cb154 | -17.7634 | -57.5937 | 2024-10-25 12:46:45 | GOES-16 | POCONÉ | MATO GROSSO | Brasil | 5106505 | 51 | 33 | nan | nan | nan | Pantanal | 108.7 |
| 677c4f49-51d9-3318-8f11-8b9ad2992f30 | -17.9268 | -57.2447 | 2024-10-25 12:46:46 | GOES-16 | CORUMBÁ | MATO GROSSO DO SUL | Brasil | 5003207 | 50 | 33 | nan | nan | nan | Pantanal | 102.2 |
| 735040a9-ac1d-3829-8e71-77a7aace5dc1 | -17.8222 | -57.6072 | 2024-10-25 12:46:46 | GOES-16 | CORUMBÁ | MATO GROSSO DO SUL | Brasil | 5003207 | 50 | 33 | nan | nan | nan | Pantanal | 110.7 |
| 72704729-feda-3310-a963-a6ba9aa9e11d | -17.8825 | -57.5383 | 2024-10-25 12:46:46 | GOES-16 | CORUMBÁ | MATO GROSSO DO SUL | Brasil | 5003207 | 50 | 33 | nan | nan | nan | Pantanal | 95.2 |
| 614db1c7-b4bf-3075-82b8-caf1ea8d0325 | -17.8628 | -57.5407 | 2024-10-25 12:46:46 | GOES-16 | CORUMBÁ | MATO GROSSO DO SUL | Brasil | 5003207 | 50 | 33 | nan | nan | nan | Pantanal | 90.7 |
| 99ba1781-7c0c-3a12-8d77-820cb52d40e1 | -17.9272 | -57.224 | 2024-10-25 12:46:46 | GOES-16 | CORUMBÁ | MATO GROSSO DO SUL | Brasil | 5003207 | 50 | 33 | nan | nan | nan | Pantanal | 116.0 |
| e0a96b10-7004-3440-8a68-e3c5468f7748 | -17.9071 | -57.2472 | 2024-10-25 12:46:46 | GOES-16 | CORUMBÁ | MATO GROSSO DO SUL | Brasil | 5003207 | 50 | 33 | nan | nan | nan | Pantanal | 97.6 |
| 085900f9-500b-3cc9-8899-5a49b1e3ff64 | -18.0254 | -57.253 | 2024-10-25 12:46:47 | GOES-16 | CORUMBÁ | MATO GROSSO DO SUL | Brasil | 5003207 | 50 | 33 | nan | nan | nan | Pantanal | 84.4 |
| 8d053e8a-842f-33d1-b82a-9f81bb5feb27 | -18.0434 | -57.3539 | 2024-10-25 12:46:47 | GOES-16 | CORUMBÁ | MATO GROSSO DO SUL | Brasil | 5003207 | 50 | 33 | nan | nan | nan | Pantanal | 90.0 |
| df5f3a73-be5d-3268-9e88-45777303704a | -18.0452 | -57.2506 | 2024-10-25 12:46:47 | GOES-16 | CORUMBÁ | MATO GROSSO DO SUL | Brasil | 5003207 | 50 | 33 | nan | nan | nan | Pantanal | 99.8 |
| 65c770dd-2138-38a7-a625-a719419249b2 | -18.0431 | -57.3745 | 2024-10-25 12:46:47 | GOES-16 | CORUMBÁ | MATO GROSSO DO SUL | Brasil | 5003207 | 50 | 33 | nan | nan | nan | Pantanal | 105.4 |
| eb65e507-b273-3567-82ca-7d8619952a77 | -18.0441 | -57.3126 | 2024-10-25 12:46:47 | GOES-16 | CORUMBÁ | MATO GROSSO DO SUL | Brasil | 5003207 | 50 | 33 | nan | nan | nan | Pantanal | 88.5 |
| d7a708e8-3286-3cff-8c6d-33bb1dd2b2e6 | -18.2641 | -56.0394 | 2024-10-25 12:46:48 | GOES-16 | CORUMBÁ | MATO GROSSO DO SUL | Brasil | 5003207 | 50 | 33 | nan | nan | nan | Pantanal | 111.4 |
| acbb366f-437b-3563-b229-cf9d28217639 | -18.3004 | -56.2222 | 2024-10-25 12:46:48 | GOES-16 | CORUMBÁ | MATO GROSSO DO SUL | Brasil | 5003207 | 50 | 33 | nan | nan | nan | Pantanal | 96.8 |
| 03fa7e46-ad54-3420-a7c0-73171fbea187 | -18.2645 | -56.0184 | 2024-10-25 12:46:48 | GOES-16 | CORUMBÁ | MATO GROSSO DO SUL | Brasil | 5003207 | 50 | 33 | nan | nan | nan | Pantanal | 114.2 |
| 3a55957b-7065-3abc-a1bb-dca1579d1367 | -19.6446 | -56.8101 | 2024-10-25 12:46:55 | GOES-16 | AQUIDAUANA | MATO GROSSO DO SUL | Brasil | 5001102 | 50 | 33 | nan | nan | nan | Pantanal | 71.5 |
| 8b86e1d9-2e75-376c-8807-cc6af25043fe | -19.6442 | -56.8311 | 2024-10-25 12:46:55 | GOES-16 | AQUIDAUANA | MATO GROSSO DO SUL | Brasil | 5001102 | 50 | 33 | nan | nan | nan | Pantanal | 73.6 |
| 5c8daae6-ec8d-3d6f-981c-e5eb8b291aa0 | -19.6647 | -56.8073 | 2024-10-25 12:46:55 | GOES-16 | AQUIDAUANA | MATO GROSSO DO SUL | Brasil | 5001102 | 50 | 33 | nan | nan | nan | Pantanal | 65.9 |
| 2661c329-1c13-3fbb-bca1-38a355b272cb | -19.6438 | -56.8521 | 2024-10-25 12:46:55 | GOES-16 | AQUIDAUANA | MATO GROSSO DO SUL | Brasil | 5001102 | 50 | 33 | nan | nan | nan | Pantanal | 73.0 |
| b7dfba9b-ac47-3e1c-85e1-9f067abce131 | -3.50162 | -42.15397 | 2024-10-25 12:49:00 | TERRA_M-T | JOAQUIM PIRES | PIAUÍ | Brasil | 2205409 | 22 | 33 | nan | nan | nan | Caatinga | 28.0 |
| 733f086e-4c09-37d3-b152-a5d1964e2fdb | -3.50117 | -42.15977 | 2024-10-25 12:49:00 | TERRA_M-T | JOAQUIM PIRES | PIAUÍ | Brasil | 2205409 | 22 | 33 | nan | nan | nan | Caatinga | 43.8 |
| 359fd797-51de-382f-b88a-ffdaef16cfb3 | -3.49886 | -42.17352 | 2024-10-25 12:49:00 | TERRA_M-T | JOAQUIM PIRES | PIAUÍ | Brasil | 2205409 | 22 | 33 | nan | nan | nan | Caatinga | 25.5 |
| 7c6b497c-996b-3e13-bafd-b541be85a3e3 | -3.48232 | -42.00999 | 2024-10-25 12:49:00 | TERRA_M-T | MURICI DOS PORTELAS | PIAUÍ | Brasil | 2206696 | 22 | 33 | nan | nan | nan | Caatinga | 40.3 |
| 3b22f886-7ac8-34f1-a2e4-c21f97f50c0d | -3.45804 | -42.55162 | 2024-10-25 12:49:00 | TERRA_M-T | SANTA QUITÉRIA DO MARANHÃO | MARANHÃO | Brasil | 2110104 | 21 | 33 | nan | nan | nan | Cerrado | 17.9 |
| f800f023-9d95-3b0d-9a4c-558335530fcf | -3.45544 | -42.56985 | 2024-10-25 12:49:00 | TERRA_M-T | SANTA QUITÉRIA DO MARANHÃO | MARANHÃO | Brasil | 2110104 | 21 | 33 | nan | nan | nan | Cerrado | 19.0 |
| 27421a7c-71d0-3f69-8c41-2dc5ea5ed6b8 | -3.4482 | -42.55628 | 2024-10-25 12:49:00 | TERRA_M-T | SANTA QUITÉRIA DO MARANHÃO | MARANHÃO | Brasil | 2110104 | 21 | 33 | nan | nan | nan | Cerrado | 36.5 |
| bff2d8ae-d456-30e3-8638-a766e161ab83 | -3.38167 | -42.17068 | 2024-10-25 12:49:00 | TERRA_M-T | MAGALHÃES DE ALMEIDA | MARANHÃO | Brasil | 2106300 | 21 | 33 | nan | nan | nan | Caatinga | 88.2 |
| b3efe5ce-dd01-3dfb-bd5d-29b7e46bd59f | -3.23365 | -42.69733 | 2024-10-25 12:49:00 | TERRA_M-T | SANTANA DO MARANHÃO | MARANHÃO | Brasil | 2110237 | 21 | 33 | nan | nan | nan | Cerrado | 35.0 |
| 0a27e002-f482-313c-9718-806373a8b470 | -3.22977 | -42.6912 | 2024-10-25 12:49:00 | TERRA_M-T | SANTANA DO MARANHÃO | MARANHÃO | Brasil | 2110237 | 21 | 33 | nan | nan | nan | Cerrado | 25.9 |
| 027c2d44-b67c-3cce-95ae-0734c81dafa0 | -3.22728 | -42.70883 | 2024-10-25 12:49:00 | TERRA_M-T | SANTANA DO MARANHÃO | MARANHÃO | Brasil | 2110237 | 21 | 33 | nan | nan | nan | Cerrado | 24.4 |
| 5abea96a-dc76-3571-8e16-492c392c6060 | -3.2151 | -42.7072 | 2024-10-25 12:49:00 | TERRA_M-T | SANTANA DO MARANHÃO | MARANHÃO | Brasil | 2110237 | 21 | 33 | nan | nan | nan | Cerrado | 29.8 |
| 8642cded-a509-3506-b262-a68b3a7dafd4 | -2.95682 | -42.713 | 2024-10-25 12:49:00 | TERRA_M-T | PAULINO NEVES | MARANHÃO | Brasil | 2108058 | 21 | 33 | nan | nan | nan | Cerrado | 41.6 |
| a508258c-28f0-3893-a935-b62926d570ba | -2.9526 | -42.70586 | 2024-10-25 12:49:00 | TERRA_M-T | PAULINO NEVES | MARANHÃO | Brasil | 2108058 | 21 | 33 | nan | nan | nan | Cerrado | 42.6 |
| 4ff89fb1-d565-3cd6-81c9-c90604fc9bda | -4.7359 | -42.97829 | 2024-10-25 12:49:00 | TERRA_M-T | CAXIAS | MARANHÃO | Brasil | 2103000 | 21 | 33 | nan | nan | nan | Cerrado | 23.1 |
| d0c97e2d-c78f-3f8d-9d32-9c861622c978 | -4.54289 | -42.95861 | 2024-10-25 12:49:00 | TERRA_M-T | CAXIAS | MARANHÃO | Brasil | 2103000 | 21 | 33 | nan | nan | nan | Cerrado | 24.5 |
| 1983829a-5d97-382e-92b5-765030375453 | -4.07014 | -42.88254 | 2024-10-25 12:49:00 | TERRA_M-T | BURITI | MARANHÃO | Brasil | 2102200 | 21 | 33 | nan | nan | nan | Cerrado | 29.3 |
| 19a141be-dd55-39d8-858c-3f6c1c68e65c | -4.06776 | -42.90014 | 2024-10-25 12:49:00 | TERRA_M-T | BURITI | MARANHÃO | Brasil | 2102200 | 21 | 33 | nan | nan | nan | Cerrado | 24.6 |
| b1008c29-bc8f-3b1a-b97f-539b8262f5cc | -3.74534 | -42.28418 | 2024-10-25 12:49:00 | TERRA_M-T | MORRO DO CHAPÉU DO PIAUÍ | PIAUÍ | Brasil | 2206670 | 22 | 33 | nan | nan | nan | Caatinga | 26.5 |
| 948e00d6-8663-3539-a96b-4972b2573240 | -3.7451 | -42.2906 | 2024-10-25 12:49:00 | TERRA_M-T | MORRO DO CHAPÉU DO PIAUÍ | PIAUÍ | Brasil | 2206670 | 22 | 33 | nan | nan | nan | Caatinga | 34.1 |
| 75e2e9f8-b57c-3ca0-bfcf-1ddeca24f229 | -3.74267 | -42.3033 | 2024-10-25 12:49:00 | TERRA_M-T | MORRO DO CHAPÉU DO PIAUÍ | PIAUÍ | Brasil | 2206670 | 22 | 33 | nan | nan | nan | Caatinga | 22.6 |
| c2adc3b3-566b-3b49-9822-52d6373adc71 | -3.7301 | -42.50072 | 2024-10-25 12:49:00 | TERRA_M-T | MATIAS OLÍMPIO | PIAUÍ | Brasil | 2206100 | 22 | 33 | nan | nan | nan | Cerrado | 101.4 |
| de1f11ef-bc55-3256-8fb0-af0538ea3d4f | -3.72874 | -42.49407 | 2024-10-25 12:49:00 | TERRA_M-T | LUZILÂNDIA | PIAUÍ | Brasil | 2205805 | 22 | 33 | nan | nan | nan | Cerrado | 55.7 |
| d537b5cc-fadf-3d38-94ac-5a616c3b2fc6 | -3.72762 | -42.51936 | 2024-10-25 12:49:00 | TERRA_M-T | MATIAS OLÍMPIO | PIAUÍ | Brasil | 2206100 | 22 | 33 | nan | nan | nan | Cerrado | 38.6 |
| 75e03242-5d12-3c0f-97c1-68ab97ea7919 | -3.72613 | -42.51257 | 2024-10-25 12:49:00 | TERRA_M-T | MATIAS OLÍMPIO | PIAUÍ | Brasil | 2206100 | 22 | 33 | nan | nan | nan | Cerrado | 109.5 |
| be6aa147-e8bf-3713-a883-a9a46dc90b8f | -3.64371 | -42.46366 | 2024-10-25 12:49:00 | TERRA_M-T | LUZILÂNDIA | PIAUÍ | Brasil | 2205805 | 22 | 33 | nan | nan | nan | Caatinga | 27.3 |
| 418af8fe-d01c-34fe-b729-e0b01440fc4f | -3.642 | -42.4577 | 2024-10-25 12:49:00 | TERRA_M-T | LUZILÂNDIA | PIAUÍ | Brasil | 2205805 | 22 | 33 | nan | nan | nan | Caatinga | 24.6 |
| 577f4993-e472-3bea-9076-a4c8e3cfd321 | -3.525 | -43.60573 | 2024-10-25 12:49:00 | TERRA_M-T | SÃO BENEDITO DO RIO PRETO | MARANHÃO | Brasil | 2110401 | 21 | 33 | nan | nan | nan | Cerrado | 53.0 |
| e20666c5-2561-3762-897e-6ab816b0a8cf | -3.52293 | -43.62074 | 2024-10-25 12:49:00 | TERRA_M-T | SÃO BENEDITO DO RIO PRETO | MARANHÃO | Brasil | 2110401 | 21 | 33 | nan | nan | nan | Cerrado | 100.8 |
| 76b67637-adc0-3f4a-8c42-84b153527017 | -4.65238 | -43.75358 | 2024-10-25 12:49:00 | TERRA_M-T | CODÓ | MARANHÃO | Brasil | 2103307 | 21 | 33 | nan | nan | nan | Cerrado | 14.8 |
| ee9318bd-148e-38fd-a781-5f67a1daf09b | -4.5638 | -43.56147 | 2024-10-25 12:49:00 | TERRA_M-T | ALDEIAS ALTAS | MARANHÃO | Brasil | 2100303 | 21 | 33 | nan | nan | nan | Cerrado | 21.0 |
| a1bcd31f-f289-3fb5-aa86-359b23d84104 | -4.51416 | -43.49019 | 2024-10-25 12:49:00 | TERRA_M-T | ALDEIAS ALTAS | MARANHÃO | Brasil | 2100303 | 21 | 33 | nan | nan | nan | Cerrado | 20.4 |
| dc2e58db-3421-3cb8-b3bb-2107524d8494 | -4.33327 | -43.4957 | 2024-10-25 12:49:00 | TERRA_M-T | CODÓ | MARANHÃO | Brasil | 2103307 | 21 | 33 | nan | nan | nan | Cerrado | 21.7 |
| 54cee840-ae6f-375b-9505-91014fc4e5e5 | -4.27531 | -43.74064 | 2024-10-25 12:49:00 | TERRA_M-T | CODÓ | MARANHÃO | Brasil | 2103307 | 21 | 33 | nan | nan | nan | Cerrado | 21.9 |
| b8ab6968-e48d-3f01-a751-05f752be504d | -4.00142 | -43.24678 | 2024-10-25 12:49:00 | TERRA_M-T | CHAPADINHA | MARANHÃO | Brasil | 2103208 | 21 | 33 | nan | nan | nan | Cerrado | 18.9 |
| 06bb0705-3bdc-39f9-a0f6-6c605f515632 | -3.80432 | -43.25769 | 2024-10-25 12:49:00 | TERRA_M-T | CHAPADINHA | MARANHÃO | Brasil | 2103208 | 21 | 33 | nan | nan | nan | Cerrado | 38.4 |
| c9f38f42-ebc4-3cee-95c5-0d67950c2126 | -3.80143 | -43.24723 | 2024-10-25 12:49:00 | TERRA_M-T | CHAPADINHA | MARANHÃO | Brasil | 2103208 | 21 | 33 | nan | nan | nan | Cerrado | 19.7 |
| 7dc45ea6-9619-3d8f-93d7-d104c03251fa | -3.79926 | -43.2635 | 2024-10-25 12:49:00 | TERRA_M-T | CHAPADINHA | MARANHÃO | Brasil | 2103208 | 21 | 33 | nan | nan | nan | Cerrado | 26.7 |
| 122dd659-6c82-3e38-a976-246569262f20 | -4.74243 | -44.09619 | 2024-10-25 12:49:00 | TERRA_M-T | CODÓ | MARANHÃO | Brasil | 2103307 | 21 | 33 | nan | nan | nan | Cerrado | 23.3 |
| 1921b173-c3de-3693-b04a-b672e0b95936 | -1.91114 | -46.12376 | 2024-10-25 12:49:00 | TERRA_M-T | JUNCO DO MARANHÃO | MARANHÃO | Brasil | 2105658 | 21 | 33 | nan | nan | nan | Amazônia | 9.6 |
| 108c47c2-f61c-3de8-8c09-d431b926340f | -1.9018 | -46.12247 | 2024-10-25 12:49:00 | TERRA_M-T | JUNCO DO MARANHÃO | MARANHÃO | Brasil | 2105658 | 21 | 33 | nan | nan | nan | Amazônia | 12.4 |
| 1e5c9dd5-9252-3b1f-b90f-1dc30be5c156 | -1.73759 | -46.62205 | 2024-10-25 12:49:00 | TERRA_M-T | VISEU | PARÁ | Brasil | 1508308 | 15 | 33 | nan | nan | nan | Amazônia | 7.4 |
| d59acfe3-faf4-35e8-8e8d-6f048cbc8bd8 | -2.00596 | -48.53086 | 2024-10-25 12:49:00 | TERRA_M-T | ACARÁ | PARÁ | Brasil | 1500206 | 15 | 33 | nan | nan | nan | Amazônia | 19.4 |
| baa689c6-988b-3cd6-a944-a279a24c8131 | -1.63093 | -48.06116 | 2024-10-25 12:49:00 | TERRA_M-T | BUJARU | PARÁ | Brasil | 1501907 | 15 | 33 | nan | nan | nan | Amazônia | 12.5 |
| 329da912-6397-34a6-8e50-71aebc7cd7f7 | -1.53404 | -47.20393 | 2024-10-25 12:49:00 | TERRA_M-T | OURÉM | PARÁ | Brasil | 1505403 | 15 | 33 | nan | nan | nan | Amazônia | 17.5 |
| d5298229-76d5-3ee9-b997-9033d83374ff | -1.42339 | -47.6455 | 2024-10-25 12:49:00 | TERRA_M-T | SANTA MARIA DO PARÁ | PARÁ | Brasil | 1506609 | 15 | 33 | nan | nan | nan | Amazônia | 99.5 |
| 4e218a14-36c6-36b8-9506-27938b5d7c4d | -1.42211 | -47.65432 | 2024-10-25 12:49:00 | TERRA_M-T | SANTA MARIA DO PARÁ | PARÁ | Brasil | 1506609 | 15 | 33 | nan | nan | nan | Amazônia | 8.3 |
| 51a557c5-649e-314c-a3a6-f1e558afb6e3 | -1.37031 | -47.18703 | 2024-10-25 12:49:00 | TERRA_M-T | CAPANEMA | PARÁ | Brasil | 1502202 | 15 | 33 | nan | nan | nan | Amazônia | 56.5 |
| 1dfaabcc-d9f7-362f-ab60-2cf1091347a2 | -2.3483 | -47.50139 | 2024-10-25 12:49:00 | TERRA_M-T | AURORA DO PARÁ | PARÁ | Brasil | 1500958 | 15 | 33 | nan | nan | nan | Amazônia | 10.0 |
| 56c210c7-9144-3b5c-a613-1186b7467509 | -3.83531 | -48.88488 | 2024-10-25 12:49:00 | TERRA_M-T | GOIANÉSIA DO PARÁ | PARÁ | Brasil | 1503093 | 15 | 33 | nan | nan | nan | Amazônia | 8.2 |
| b85487e6-e0b9-36da-9650-650bbe090a4a | -3.83403 | -48.89372 | 2024-10-25 12:49:00 | TERRA_M-T | GOIANÉSIA DO PARÁ | PARÁ | Brasil | 1503093 | 15 | 33 | nan | nan | nan | Amazônia | 9.2 |
| 43ee5169-b428-33c3-bef1-744928ed8905 | 0.03276 | -49.49749 | 2024-10-25 12:49:00 | TERRA_M-T | CHAVES | PARÁ | Brasil | 1502509 | 15 | 33 | nan | nan | nan | Amazônia | 7.3 |
| 5685d06e-83d8-3436-b2cd-d5eb0d08fdae | -0.65352 | -49.52713 | 2024-10-25 12:49:00 | TERRA_M-T | ANAJÁS | PARÁ | Brasil | 1500701 | 15 | 33 | nan | nan | nan | Amazônia | 9.2 |
| 4d646534-f8fa-3b7e-b66a-5a525fb6e29d | -3.33584 | -49.72435 | 2024-10-25 12:49:00 | TERRA_M-T | BAIÃO | PARÁ | Brasil | 1501204 | 15 | 33 | nan | nan | nan | Amazônia | 12.1 |


[Clique aqui para ver as próximas entradas](README114.md)
