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

## Dados Diários - Página 6

| ID | Latitude | Longitude | Data/Hora GMT | Satélite | Município | Estado | País | Município ID | Estado ID | País ID | Dias sem Chuva | Precipitação | Risco de Fogo | Bioma | FRP |
|----|----------|-----------|---------------|----------|-----------|--------|------|--------------|-----------|---------|----------------|--------------|----------------|-------|-----|
| 40b4a89f-10a4-3163-916b-7543f02603f3 | -7.11516 | -40.38424 | 2025-07-11 03:17:00 | NOAA-21 | SALITRE | CEARÁ | Brasil | 2311959 | 23 | 33 | nan | nan | nan | Caatinga | 4.8 |
| 62da00c1-d714-3918-99ae-3296dbcba50b | -7.20105 | -43.11317 | 2025-07-11 03:17:00 | NOAA-21 | FLORIANO | PIAUÍ | Brasil | 2203909 | 22 | 33 | nan | nan | nan | Caatinga | 13.2 |
| ad1b976e-c7fb-3692-a61a-b6d48f6e8872 | -10.6959 | -37.05053 | 2025-07-11 03:17:00 | NOAA-21 | ROSÁRIO DO CATETE | SERGIPE | Brasil | 2806107 | 28 | 33 | nan | nan | nan | Mata Atlântica | 1.4 |
| b022946a-f296-3c75-925c-d4ef63f96f6e | -7.20297 | -43.12334 | 2025-07-11 03:17:00 | NOAA-21 | FLORIANO | PIAUÍ | Brasil | 2203909 | 22 | 33 | nan | nan | nan | Caatinga | 11.7 |
| cfcda8eb-a3a9-3b06-9958-597e08174d0c | -14.39065 | -43.77645 | 2025-07-11 03:19:00 | NOAA-21 | MALHADA | BAHIA | Brasil | 2920205 | 29 | 33 | nan | nan | nan | Cerrado | 3.3 |
| 9a62137a-ddcb-32a9-a33b-c232a684fab9 | -12.41552 | -43.48856 | 2025-07-11 03:19:00 | NOAA-21 | MUQUÉM DO SÃO FRANCISCO | BAHIA | Brasil | 2922250 | 29 | 33 | nan | nan | nan | Cerrado | 3.8 |
| 61a4c3d8-2677-3edd-81c8-049b787a9b9c | -12.98767 | -44.85864 | 2025-07-11 03:19:00 | NOAA-21 | SÃO DESIDÉRIO | BAHIA | Brasil | 2928901 | 29 | 33 | nan | nan | nan | Cerrado | 3.2 |
| f4651df6-6be9-38c2-a82d-d232e76af643 | -14.39193 | -43.77061 | 2025-07-11 03:19:00 | NOAA-21 | MALHADA | BAHIA | Brasil | 2920205 | 29 | 33 | nan | nan | nan | Cerrado | 4.2 |
| 9fc2bbce-fc88-3c80-989c-fd7aa274c95d | -12.41876 | -43.49098 | 2025-07-11 03:19:00 | NOAA-21 | MUQUÉM DO SÃO FRANCISCO | BAHIA | Brasil | 2922250 | 29 | 33 | nan | nan | nan | Cerrado | 4.3 |
| e898b252-747d-37da-b5a5-35dcafebfd48 | -14.39848 | -43.77198 | 2025-07-11 03:19:00 | NOAA-21 | MALHADA | BAHIA | Brasil | 2920205 | 29 | 33 | nan | nan | nan | Cerrado | 1.2 |
| 15168692-e221-3919-9476-518c892e10dc | -14.39277 | -43.77324 | 2025-07-11 03:19:00 | NOAA-21 | MALHADA | BAHIA | Brasil | 2920205 | 29 | 33 | nan | nan | nan | Cerrado | 6.4 |
| 7f6a61ac-89dc-3971-9472-ed4cc554de1e | -12.4659 | -44.4966 | 2025-07-11 03:19:00 | NOAA-21 | BAIANÓPOLIS | BAHIA | Brasil | 2902500 | 29 | 33 | nan | nan | nan | Cerrado | 3.5 |
| f180d1e1-e50a-310f-a897-7da6f183b7eb | -9.9148 | -47.8282 | 2025-07-11 03:20:00 | GOES-19 | NOVO ACORDO | TOCANTINS | Brasil | 1715101 | 17 | 33 | nan | nan | nan | Cerrado | 100.9 |
| 4a4fc1c4-90c6-38eb-a103-a419e1b370dc | -10.6862 | -49.4874 | 2025-07-11 03:20:00 | GOES-19 | CRISTALÂNDIA | TOCANTINS | Brasil | 1706100 | 17 | 33 | nan | nan | nan | Cerrado | 162.6 |
| 2a2755af-de06-34d2-8b2b-5c34f7d81150 | -22.2852 | -54.9409 | 2025-07-11 03:20:00 | GOES-19 | DOURADOS | MATO GROSSO DO SUL | Brasil | 5003702 | 50 | 33 | nan | nan | nan | Cerrado | 70.6 |
| 08e5df8e-244c-3918-b979-e7b555cf8374 | -10.6859 | -49.509 | 2025-07-11 03:20:00 | GOES-19 | CRISTALÂNDIA | TOCANTINS | Brasil | 1706100 | 17 | 33 | nan | nan | nan | Cerrado | 54.5 |
| 12c08298-d5a9-39dc-9bc7-ffd2962599df | -10.5776 | -49.1316 | 2025-07-11 03:20:00 | GOES-19 | CRISTALÂNDIA | TOCANTINS | Brasil | 1706100 | 17 | 33 | nan | nan | nan | Cerrado | 58.0 |
| 82de18f1-2e5b-3962-9f27-baacae4d811e | -10.6672 | -49.4895 | 2025-07-11 03:20:00 | GOES-19 | CRISTALÂNDIA | TOCANTINS | Brasil | 1706100 | 17 | 33 | nan | nan | nan | Cerrado | 99.1 |
| 433938eb-3967-3e8e-9ca4-a9d75befe293 | -5.5427 | -43.9096 | 2025-07-11 03:30:00 | GOES-19 | FORTUNA | MARANHÃO | Brasil | 2104206 | 21 | 33 | nan | nan | nan | Cerrado | 90.9 |
| 7ec6e4af-3087-3f6f-a2bd-55d357e1fb73 | -5.5614 | -43.9082 | 2025-07-11 03:30:00 | GOES-19 | FORTUNA | MARANHÃO | Brasil | 2104206 | 21 | 33 | nan | nan | nan | Cerrado | 54.3 |
| 83b541b0-56c0-3f01-8886-0da936748f5d | -9.9148 | -47.8282 | 2025-07-11 03:30:00 | GOES-19 | NOVO ACORDO | TOCANTINS | Brasil | 1715101 | 17 | 33 | nan | nan | nan | Cerrado | 101.2 |
| cf01740b-21c6-3f86-9879-8a71f694ba50 | -10.6859 | -49.509 | 2025-07-11 03:30:00 | GOES-19 | CRISTALÂNDIA | TOCANTINS | Brasil | 1706100 | 17 | 33 | nan | nan | nan | Cerrado | 56.6 |
| 682b1f09-6ede-36ae-8b8c-0b06d3889586 | -10.6862 | -49.4874 | 2025-07-11 03:30:00 | GOES-19 | CRISTALÂNDIA | TOCANTINS | Brasil | 1706100 | 17 | 33 | nan | nan | nan | Cerrado | 134.1 |
| fb102950-924c-33b6-8b93-68057721cc24 | -5.5429 | -43.8864 | 2025-07-11 03:30:00 | GOES-19 | FORTUNA | MARANHÃO | Brasil | 2104206 | 21 | 33 | nan | nan | nan | Cerrado | 68.4 |
| 0983c702-667e-3147-9133-46e78e324b0f | -10.6672 | -49.4895 | 2025-07-11 03:30:00 | GOES-19 | CRISTALÂNDIA | TOCANTINS | Brasil | 1706100 | 17 | 33 | nan | nan | nan | Cerrado | 84.1 |
| ad3c6372-9055-3f49-b489-f91893f0950e | -10.5776 | -49.1316 | 2025-07-11 03:30:00 | GOES-19 | CRISTALÂNDIA | TOCANTINS | Brasil | 1706100 | 17 | 33 | nan | nan | nan | Cerrado | 56.4 |
| 55bac4f7-dd3d-390f-8993-0c757c07095a | -9.9148 | -47.8282 | 2025-07-11 03:40:00 | GOES-19 | NOVO ACORDO | TOCANTINS | Brasil | 1715101 | 17 | 33 | nan | nan | nan | Cerrado | 75.8 |
| d89816d1-02f8-3b73-9b4a-b67e7dbef714 | -10.5776 | -49.1316 | 2025-07-11 03:40:00 | GOES-19 | CRISTALÂNDIA | TOCANTINS | Brasil | 1706100 | 17 | 33 | nan | nan | nan | Cerrado | 66.2 |
| 7a4135d1-c058-3168-843c-88a34672a15d | -5.5427 | -43.9096 | 2025-07-11 03:40:00 | GOES-19 | FORTUNA | MARANHÃO | Brasil | 2104206 | 21 | 33 | nan | nan | nan | Cerrado | 158.7 |
| f866e709-6bdf-3afd-aa2f-250e0cb1732e | -5.5429 | -43.8864 | 2025-07-11 03:40:00 | GOES-19 | FORTUNA | MARANHÃO | Brasil | 2104206 | 21 | 33 | nan | nan | nan | Cerrado | 100.9 |
| 8ba1126a-ca31-3761-a72e-05a48303fa98 | -10.6862 | -49.4874 | 2025-07-11 03:40:00 | GOES-19 | CRISTALÂNDIA | TOCANTINS | Brasil | 1706100 | 17 | 33 | nan | nan | nan | Cerrado | 121.5 |
| 6d0273d4-b31f-3ab7-81fd-20b3eb5effe6 | -10.6672 | -49.4895 | 2025-07-11 03:40:00 | GOES-19 | CRISTALÂNDIA | TOCANTINS | Brasil | 1706100 | 17 | 33 | nan | nan | nan | Cerrado | 106.4 |
| 7aa49cbd-de49-352d-b64d-ddaa3f7cb9cd | -7.65623 | -45.34975 | 2025-07-11 03:45:00 | NPP-375D | RIBEIRO GONÇALVES | PIAUÍ | Brasil | 2208908 | 22 | 33 | nan | nan | nan | Cerrado | 1.1 |
| 5190bf3a-dcbf-3f43-8c02-ef957f3b0a80 | -9.53526 | -46.28936 | 2025-07-11 03:45:00 | NPP-375D | ALTO PARNAÍBA | MARANHÃO | Brasil | 2100501 | 21 | 33 | nan | nan | nan | Cerrado | 1.3 |
| 01ad10ed-2c20-330f-95be-194feb0d595c | -8.22176 | -44.91673 | 2025-07-11 03:45:00 | NPP-375D | BAIXA GRANDE DO RIBEIRO | PIAUÍ | Brasil | 2201150 | 22 | 33 | nan | nan | nan | Cerrado | 1.9 |
| d7179e6b-5577-3491-b30b-acb6fd0722c6 | -7.11402 | -40.38363 | 2025-07-11 03:45:00 | NPP-375D | SALITRE | CEARÁ | Brasil | 2311959 | 23 | 33 | nan | nan | nan | Caatinga | 2.3 |
| 7d439822-a85c-335c-a097-cfecf651c68c | -6.99068 | -44.44984 | 2025-07-11 03:45:00 | NPP-375D | BENEDITO LEITE | MARANHÃO | Brasil | 2101806 | 21 | 33 | nan | nan | nan | Cerrado | 1.6 |
| 374cd8e6-0c47-3a77-acc0-b31d4de506bb | -7.31718 | -38.13612 | 2025-07-11 03:45:00 | NPP-375D | ITAPORANGA | PARAÍBA | Brasil | 2507002 | 25 | 33 | nan | nan | nan | Caatinga | 1.2 |
| 496c18db-1f29-3891-a08b-78cbf9792f6d | -8.58317 | -47.1937 | 2025-07-11 03:45:00 | NPP-375D | RECURSOLÂNDIA | TOCANTINS | Brasil | 1718501 | 17 | 33 | nan | nan | nan | Cerrado | 1.5 |
| 78713851-8921-39e1-b953-bf494eb0063c | -7.55346 | -45.62515 | 2025-07-11 03:45:00 | NPP-375D | SAMBAÍBA | MARANHÃO | Brasil | 2109700 | 21 | 33 | nan | nan | nan | Cerrado | 1.1 |
| 69b2c316-bd80-3e56-86fe-9d2cba1dca09 | -8.24741 | -44.92847 | 2025-07-11 03:45:00 | NPP-375D | BAIXA GRANDE DO RIBEIRO | PIAUÍ | Brasil | 2201150 | 22 | 33 | nan | nan | nan | Cerrado | 0.7 |
| b29ecee0-d66d-3cd9-ad45-be7055d66b6e | -6.99388 | -44.4504 | 2025-07-11 03:45:00 | NPP-375D | BENEDITO LEITE | MARANHÃO | Brasil | 2101806 | 21 | 33 | nan | nan | nan | Cerrado | 2.3 |
| e37b9978-c088-3a07-aa6e-34b770aad81a | -3.75381 | -47.11195 | 2025-07-11 03:45:00 | NPP-375D | ULIANÓPOLIS | PARÁ | Brasil | 1508126 | 15 | 33 | nan | nan | nan | Amazônia | 2.4 |
| dffa2a8b-1305-33fd-b1aa-65016455fdf5 | -5.22196 | -38.12428 | 2025-07-11 03:45:00 | NPP-375D | TABULEIRO DO NORTE | CEARÁ | Brasil | 2313104 | 23 | 33 | nan | nan | nan | Caatinga | 1.0 |
| 8f08b524-7120-3b36-a00c-3302ecc544e1 | -6.99272 | -44.45678 | 2025-07-11 03:45:00 | NPP-375D | BENEDITO LEITE | MARANHÃO | Brasil | 2101806 | 21 | 33 | nan | nan | nan | Cerrado | 1.6 |
| 66d4634e-24ce-38df-b563-36e8b9e2b376 | -7.70168 | -43.57228 | 2025-07-11 03:45:00 | NPP-375D | CANAVIEIRA | PIAUÍ | Brasil | 2202251 | 22 | 33 | nan | nan | nan | Cerrado | 3.1 |
| 2faa1dc0-dafc-337f-bb8c-2d72fef40c3c | -6.85426 | -42.79984 | 2025-07-11 03:45:00 | NPP-375D | FLORIANO | PIAUÍ | Brasil | 2203909 | 22 | 33 | nan | nan | nan | Caatinga | 3.4 |
| 7b6ce7df-a55e-37c4-809a-db854653600f | -5.54949 | -43.90046 | 2025-07-11 03:45:00 | NPP-375D | FORTUNA | MARANHÃO | Brasil | 2104206 | 21 | 33 | nan | nan | nan | Cerrado | 3.5 |
| 89291f73-aa12-3c9f-8ffc-88b4334c2664 | -6.88611 | -44.06461 | 2025-07-11 03:45:00 | NPP-375D | PORTO ALEGRE DO PIAUÍ | PIAUÍ | Brasil | 2208551 | 22 | 33 | nan | nan | nan | Cerrado | 1.2 |
| 4d44b111-5d9f-37e9-aa4f-069ea9e23e10 | -9.53383 | -46.29702 | 2025-07-11 03:45:00 | NPP-375D | ALTO PARNAÍBA | MARANHÃO | Brasil | 2100501 | 21 | 33 | nan | nan | nan | Cerrado | 3.8 |
| 7320a7ad-2110-3566-96b9-c74640801354 | -5.78585 | -45.11151 | 2025-07-11 03:45:00 | NPP-375D | BARRA DO CORDA | MARANHÃO | Brasil | 2101608 | 21 | 33 | nan | nan | nan | Cerrado | 0.9 |
| 7c14f3af-ccf0-359c-9407-16ad4c7b3207 | -4.54733 | -48.00664 | 2025-07-11 03:45:00 | NPP-375D | RONDON DO PARÁ | PARÁ | Brasil | 1506187 | 15 | 33 | nan | nan | nan | Amazônia | 7.2 |
| 2b2cce58-318f-3d89-aa73-bd992111d7aa | -7.18968 | -43.12584 | 2025-07-11 03:45:00 | NPP-375D | FLORIANO | PIAUÍ | Brasil | 2203909 | 22 | 33 | nan | nan | nan | Caatinga | 2.4 |
| 08388711-9e4c-32d1-91fa-1fd378de5a51 | -6.08076 | -44.87019 | 2025-07-11 03:45:00 | NPP-375D | FERNANDO FALCÃO | MARANHÃO | Brasil | 2104081 | 21 | 33 | nan | nan | nan | Cerrado | 3.6 |
| be29144c-2307-39d5-91eb-c72eb38d72f4 | -7.20033 | -43.12214 | 2025-07-11 03:45:00 | NPP-375D | FLORIANO | PIAUÍ | Brasil | 2203909 | 22 | 33 | nan | nan | nan | Caatinga | 10.1 |
| 3874e0ec-3bab-3142-9168-67cbe6774b01 | -7.10939 | -40.38646 | 2025-07-11 03:45:00 | NPP-375D | CAMPOS SALES | CEARÁ | Brasil | 2302701 | 23 | 33 | nan | nan | nan | Caatinga | 12.1 |
| e68d638a-1ba2-3a64-a749-dd07dd70faf0 | -6.98958 | -44.45612 | 2025-07-11 03:45:00 | NPP-375D | BENEDITO LEITE | MARANHÃO | Brasil | 2101806 | 21 | 33 | nan | nan | nan | Cerrado | 1.4 |
| 59627ebe-3760-3520-8b2a-05faf7a3754c | -7.32915 | -44.32748 | 2025-07-11 03:45:00 | NPP-375D | SEBASTIÃO LEAL | PIAUÍ | Brasil | 2210631 | 22 | 33 | nan | nan | nan | Cerrado | 0.7 |
| 2510d7b6-ce1b-3219-bc82-d1afc9d74c47 | -8.5841 | -47.18875 | 2025-07-11 03:45:00 | NPP-375D | RECURSOLÂNDIA | TOCANTINS | Brasil | 1718501 | 17 | 33 | nan | nan | nan | Cerrado | 0.9 |
| eb34a048-0c91-3b7e-a814-2d5a3e9e5c9b | -6.67063 | -46.30319 | 2025-07-11 03:45:00 | NPP-375D | FORMOSA DA SERRA NEGRA | MARANHÃO | Brasil | 2104099 | 21 | 33 | nan | nan | nan | Cerrado | 2.2 |
| 958e1b78-1d5a-30f2-a74e-f23453fc78d1 | -6.0814 | -44.86659 | 2025-07-11 03:45:00 | NPP-375D | FERNANDO FALCÃO | MARANHÃO | Brasil | 2104081 | 21 | 33 | nan | nan | nan | Cerrado | 3.6 |
| b4a68d83-5370-36f5-85d8-c4da7aa03f8a | -6.96117 | -42.72127 | 2025-07-11 03:45:00 | NPP-375D | NAZARÉ DO PIAUÍ | PIAUÍ | Brasil | 2206704 | 22 | 33 | nan | nan | nan | Caatinga | 1.9 |
| fc009f5a-4034-3f60-92f3-872ffe0f2846 | -5.78516 | -45.11549 | 2025-07-11 03:45:00 | NPP-375D | BARRA DO CORDA | MARANHÃO | Brasil | 2101608 | 21 | 33 | nan | nan | nan | Cerrado | 0.9 |
| 6a7f8228-2f32-349f-812f-8249a7d3025f | -6.67745 | -46.30685 | 2025-07-11 03:45:00 | NPP-375D | FORMOSA DA SERRA NEGRA | MARANHÃO | Brasil | 2104099 | 21 | 33 | nan | nan | nan | Cerrado | 1.5 |
| accd07ca-69b7-361e-be30-30dc11427325 | -4.54622 | -48.01297 | 2025-07-11 03:45:00 | NPP-375D | RONDON DO PARÁ | PARÁ | Brasil | 1506187 | 15 | 33 | nan | nan | nan | Amazônia | 7.2 |
| 00cd2ce0-2096-345f-b55f-f361927d0d86 | -4.54576 | -48.00868 | 2025-07-11 03:45:00 | NPP-375D | RONDON DO PARÁ | PARÁ | Brasil | 1506187 | 15 | 33 | nan | nan | nan | Amazônia | 7.2 |
| a4523019-4ae5-383c-86ee-a4adb5f2ad89 | -5.54422 | -43.89959 | 2025-07-11 03:45:00 | NPP-375D | FORTUNA | MARANHÃO | Brasil | 2104206 | 21 | 33 | nan | nan | nan | Cerrado | 3.5 |
| 7f41fd56-095e-3057-b142-08a59da8b98a | -5.20306 | -37.66341 | 2025-07-11 03:45:00 | NPP-375D | BARAÚNA | RIO GRANDE DO NORTE | Brasil | 2401453 | 24 | 33 | nan | nan | nan | Caatinga | 1.4 |
| 569a009c-c537-3a2b-9f12-eb41b8cd4abe | -6.65022 | -43.19104 | 2025-07-11 03:45:00 | NPP-375D | BARÃO DE GRAJAÚ | MARANHÃO | Brasil | 2101509 | 21 | 33 | nan | nan | nan | Caatinga | 2.5 |
| 372a74e9-1387-3771-9acd-fd888d554cf2 | -3.74971 | -47.11835 | 2025-07-11 03:45:00 | NPP-375D | ULIANÓPOLIS | PARÁ | Brasil | 1508126 | 15 | 33 | nan | nan | nan | Amazônia | 4.8 |
| 0c57a086-5083-34bb-bc59-006e80f0a9d5 | -7.32968 | -44.32447 | 2025-07-11 03:45:00 | NPP-375D | SEBASTIÃO LEAL | PIAUÍ | Brasil | 2210631 | 22 | 33 | nan | nan | nan | Cerrado | 0.7 |
| 55e030dc-668e-3fea-9951-a592fc095d68 | -6.99605 | -44.45052 | 2025-07-11 03:45:00 | NPP-375D | BENEDITO LEITE | MARANHÃO | Brasil | 2101806 | 21 | 33 | nan | nan | nan | Cerrado | 1.3 |
| e5cf27a5-4704-3271-9ab4-a1826fafccf3 | -4.22688 | -47.21271 | 2025-07-11 03:45:00 | NPP-375D | ITINGA DO MARANHÃO | MARANHÃO | Brasil | 2105427 | 21 | 33 | nan | nan | nan | Amazônia | 0.6 |
| 3ec72e01-9d64-348a-846b-76ac54a2db06 | -2.44345 | -47.46752 | 2025-07-11 03:45:00 | NPP-375D | IPIXUNA DO PARÁ | PARÁ | Brasil | 1503457 | 15 | 33 | nan | nan | nan | Amazônia | 1.9 |
| d943a329-320b-3d35-9ee7-679dc895d6c8 | -7.20126 | -43.11682 | 2025-07-11 03:45:00 | NPP-375D | FLORIANO | PIAUÍ | Brasil | 2203909 | 22 | 33 | nan | nan | nan | Caatinga | 10.1 |
| 7154ae38-9d51-3e92-b6b0-18f5a3aacdad | -8.39303 | -46.9331 | 2025-07-11 03:45:00 | NPP-375D | CAMPOS LINDOS | TOCANTINS | Brasil | 1703842 | 17 | 33 | nan | nan | nan | Cerrado | 1.9 |
| 0f336e33-0e59-362c-9607-9b10aad7e968 | -5.75107 | -40.44615 | 2025-07-11 03:45:00 | NPP-375D | INDEPENDÊNCIA | CEARÁ | Brasil | 2305605 | 23 | 33 | nan | nan | nan | Caatinga | 2.3 |
| 7a69d4cf-d2ff-37d3-b279-d02f385ba12d | -5.54478 | -43.89631 | 2025-07-11 03:45:00 | NPP-375D | FORTUNA | MARANHÃO | Brasil | 2104206 | 21 | 33 | nan | nan | nan | Cerrado | 3.5 |
| 06f6b6f9-c081-3c31-951c-04ec11d30ab7 | -7.49406 | -43.93758 | 2025-07-11 03:45:00 | NPP-375D | SEBASTIÃO LEAL | PIAUÍ | Brasil | 2210631 | 22 | 33 | nan | nan | nan | Cerrado | 3.1 |
| 169cf06f-36ff-3d0b-9ce4-eeadb4ec02df | -5.7881 | -45.11076 | 2025-07-11 03:45:00 | NPP-375D | BARRA DO CORDA | MARANHÃO | Brasil | 2101608 | 21 | 33 | nan | nan | nan | Cerrado | 0.7 |
| 324ccc7c-2183-3f37-b397-193ffb5f8a05 | -6.84914 | -42.80216 | 2025-07-11 03:45:00 | NPP-375D | FLORIANO | PIAUÍ | Brasil | 2203909 | 22 | 33 | nan | nan | nan | Caatinga | 2.5 |
| 4e9c0afb-1f53-3d8e-af95-52335fcb50a3 | -7.48848 | -43.93937 | 2025-07-11 03:45:00 | NPP-375D | SEBASTIÃO LEAL | PIAUÍ | Brasil | 2210631 | 22 | 33 | nan | nan | nan | Cerrado | 5.8 |
| f205394f-cc25-38ff-84e7-9535ad071c44 | -6.87372 | -45.23518 | 2025-07-11 03:45:00 | NPP-375D | LORETO | MARANHÃO | Brasil | 2106102 | 21 | 33 | nan | nan | nan | Cerrado | 3.7 |
| e5d5326b-0961-3c50-85f7-4d09c55b0ff4 | -7.19455 | -43.12666 | 2025-07-11 03:45:00 | NPP-375D | FLORIANO | PIAUÍ | Brasil | 2203909 | 22 | 33 | nan | nan | nan | Caatinga | 3.0 |
| 72eabfbc-bcea-3bd9-93b1-a84aec10df36 | -7.4834 | -43.9383 | 2025-07-11 03:45:00 | NPP-375D | SEBASTIÃO LEAL | PIAUÍ | Brasil | 2210631 | 22 | 33 | nan | nan | nan | Cerrado | 5.8 |
| 432b93b9-a98b-3bad-980c-76a4efa95348 | -8.22592 | -44.92433 | 2025-07-11 03:45:00 | NPP-375D | BAIXA GRANDE DO RIBEIRO | PIAUÍ | Brasil | 2201150 | 22 | 33 | nan | nan | nan | Cerrado | 1.1 |
| 3a35bf01-4f8d-3087-bf4b-d6b72ebd64c4 | -6.9607 | -42.72378 | 2025-07-11 03:45:00 | NPP-375D | NAZARÉ DO PIAUÍ | PIAUÍ | Brasil | 2206704 | 22 | 33 | nan | nan | nan | Caatinga | 3.0 |
| 411e2f43-8961-3603-9de4-fb7a8224a7ed | -6.15809 | -47.27455 | 2025-07-11 03:45:00 | NPP-375D | CAMPESTRE DO MARANHÃO | MARANHÃO | Brasil | 2102556 | 21 | 33 | nan | nan | nan | Cerrado | 4.1 |
| 853e102f-01be-388f-bf51-2812b724e405 | -6.8495 | -42.79888 | 2025-07-11 03:45:00 | NPP-375D | FLORIANO | PIAUÍ | Brasil | 2203909 | 22 | 33 | nan | nan | nan | Caatinga | 3.4 |
| 90a7ed36-7bf3-30e1-ac68-5cac275b17a7 | -3.74714 | -47.11097 | 2025-07-11 03:45:00 | NPP-375D | ULIANÓPOLIS | PARÁ | Brasil | 1508126 | 15 | 33 | nan | nan | nan | Amazônia | 2.4 |
| cf03dae2-c4a1-3b40-ad25-a5fb0cf9115b | -8.24803 | -44.92507 | 2025-07-11 03:45:00 | NPP-375D | BAIXA GRANDE DO RIBEIRO | PIAUÍ | Brasil | 2201150 | 22 | 33 | nan | nan | nan | Cerrado | 0.6 |
| de0999fc-a929-3b8b-ae21-93de79646c87 | -7.19212 | -43.37513 | 2025-07-11 03:45:00 | NPP-375D | JERUMENHA | PIAUÍ | Brasil | 2205300 | 22 | 33 | nan | nan | nan | Caatinga | 2.5 |
| 14d34a3b-18a5-3572-b44a-320fa7089e66 | -5.54893 | -43.90371 | 2025-07-11 03:45:00 | NPP-375D | FORTUNA | MARANHÃO | Brasil | 2104206 | 21 | 33 | nan | nan | nan | Cerrado | 3.8 |
| b3425da0-0507-3b38-aa48-bf7a5849a013 | -8.57698 | -47.19258 | 2025-07-11 03:45:00 | NPP-375D | RECURSOLÂNDIA | TOCANTINS | Brasil | 1718501 | 17 | 33 | nan | nan | nan | Cerrado | 5.4 |
| ada29657-75f3-3129-83b0-84712d47651c | -6.72407 | -44.33828 | 2025-07-11 03:45:00 | NPP-375D | PASTOS BONS | MARANHÃO | Brasil | 2108009 | 21 | 33 | nan | nan | nan | Cerrado | 7.4 |
| 78fddb96-d736-3a95-b207-94f8b0cf66cc | -7.18671 | -43.11414 | 2025-07-11 03:45:00 | NPP-375D | FLORIANO | PIAUÍ | Brasil | 2203909 | 22 | 33 | nan | nan | nan | Caatinga | 7.1 |
| d3e7da71-2745-3407-9920-682fc599fd26 | -7.10879 | -40.38999 | 2025-07-11 03:45:00 | NPP-375D | CAMPOS SALES | CEARÁ | Brasil | 2302701 | 23 | 33 | nan | nan | nan | Caatinga | 6.6 |
| 6c9212f3-6cdd-3227-9ae6-aab34387d14e | -3.75479 | -47.10622 | 2025-07-11 03:45:00 | NPP-375D | ULIANÓPOLIS | PARÁ | Brasil | 1508126 | 15 | 33 | nan | nan | nan | Amazônia | 1.8 |
| b141f15b-de3e-3dc4-bcd2-d37a72cab718 | -7.195 | -43.35828 | 2025-07-11 03:45:00 | NPP-375D | JERUMENHA | PIAUÍ | Brasil | 2205300 | 22 | 33 | nan | nan | nan | Caatinga | 2.2 |
| a1ccd1a3-4a41-3f26-9434-b3a6b16f930a | -7.19287 | -43.37662 | 2025-07-11 03:45:00 | NPP-375D | JERUMENHA | PIAUÍ | Brasil | 2205300 | 22 | 33 | nan | nan | nan | Caatinga | 1.5 |


[Clique aqui para ver as próximas entradas](README7.md)
