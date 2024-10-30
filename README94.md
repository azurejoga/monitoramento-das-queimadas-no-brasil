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

## Dados Diários - Página 94

| ID | Latitude | Longitude | Data/Hora GMT | Satélite | Município | Estado | País | Município ID | Estado ID | País ID | Dias sem Chuva | Precipitação | Risco de Fogo | Bioma | FRP |
|----|----------|-----------|---------------|----------|-----------|--------|------|--------------|-----------|---------|----------------|--------------|----------------|-------|-----|
| 7eb4cca7-b93d-3d34-80c9-c50ca2a9ca54 | -10.34176 | -49.65784 | 2024-10-30 05:10:00 | NOAA-20 | PIUM | TOCANTINS | Brasil | 1717503 | 17 | 33 | nan | nan | nan | Cerrado | 5.4 |
| a3b3d4f7-d752-3cc8-9878-3f5b08df5f51 | -10.33824 | -49.64484 | 2024-10-30 05:10:00 | NOAA-20 | PIUM | TOCANTINS | Brasil | 1717503 | 17 | 33 | nan | nan | nan | Cerrado | 3.1 |
| 8f7ce568-eb01-3dbf-8d18-5d31a7ce03ad | -10.33784 | -49.64793 | 2024-10-30 05:10:00 | NOAA-20 | PIUM | TOCANTINS | Brasil | 1717503 | 17 | 33 | nan | nan | nan | Cerrado | 3.1 |
| 1328b241-02ab-35dd-8f7c-18ae85aa1abb | -10.33743 | -49.65104 | 2024-10-30 05:10:00 | NOAA-20 | PIUM | TOCANTINS | Brasil | 1717503 | 17 | 33 | nan | nan | nan | Cerrado | 3.3 |
| b944476b-357f-3f8f-8078-e01873ebaea4 | -10.33702 | -49.65413 | 2024-10-30 05:10:00 | NOAA-20 | PIUM | TOCANTINS | Brasil | 1717503 | 17 | 33 | nan | nan | nan | Cerrado | 3.3 |
| dc246089-4a39-32ef-a1b4-45c2d7f26f34 | -10.19476 | -49.14976 | 2024-10-30 05:10:00 | NOAA-20 | CHAPADA DE AREIA | TOCANTINS | Brasil | 1704600 | 17 | 33 | nan | nan | nan | Cerrado | 1.1 |
| 76652fa7-176c-3288-989c-d746d38061a3 | -17.26878 | -57.50009 | 2024-10-30 05:12:00 | NOAA-20 | CÁCERES | MATO GROSSO | Brasil | 5102504 | 51 | 33 | nan | nan | nan | Pantanal | 1.1 |
| 6e8aa25b-d6aa-358d-885b-bbf225892172 | -17.25893 | -57.49447 | 2024-10-30 05:12:00 | NOAA-20 | CÁCERES | MATO GROSSO | Brasil | 5102504 | 51 | 33 | nan | nan | nan | Pantanal | 1.4 |
| 25fbaad7-8906-3d1e-bdc7-899386e1a4c6 | -17.24444 | -57.49629 | 2024-10-30 05:12:00 | NOAA-20 | CÁCERES | MATO GROSSO | Brasil | 5102504 | 51 | 33 | nan | nan | nan | Pantanal | 1.8 |
| 311b5d26-dd72-34c6-ad1f-68e728ec3736 | -17.24096 | -57.49574 | 2024-10-30 05:12:00 | NOAA-20 | CÁCERES | MATO GROSSO | Brasil | 5102504 | 51 | 33 | nan | nan | nan | Pantanal | 1.8 |
| abadc6f0-a963-3680-8a9e-7dc7ca50f13e | -15.12196 | -59.02322 | 2024-10-30 05:12:00 | NOAA-20 | PONTES E LACERDA | MATO GROSSO | Brasil | 5106752 | 51 | 33 | nan | nan | nan | Amazônia | 0.5 |
| 13937b18-0210-342e-b547-37f607b14bf0 | -18.25115 | -55.97076 | 2024-10-30 05:12:00 | NOAA-20 | CORUMBÁ | MATO GROSSO DO SUL | Brasil | 5003207 | 50 | 33 | nan | nan | nan | Pantanal | 2.2 |
| 17e9f68a-da0a-3961-aefd-37240354f23c | -18.25095 | -55.97315 | 2024-10-30 05:12:00 | NOAA-20 | CORUMBÁ | MATO GROSSO DO SUL | Brasil | 5003207 | 50 | 33 | nan | nan | nan | Pantanal | 3.3 |
| c30c7f09-abb1-3c78-8728-6ab8be58e3d8 | -18.25051 | -55.97559 | 2024-10-30 05:12:00 | NOAA-20 | CORUMBÁ | MATO GROSSO DO SUL | Brasil | 5003207 | 50 | 33 | nan | nan | nan | Pantanal | 3.2 |
| f747e687-fac0-3c67-af53-cdad4dec1d85 | -18.25028 | -55.97797 | 2024-10-30 05:12:00 | NOAA-20 | CORUMBÁ | MATO GROSSO DO SUL | Brasil | 5003207 | 50 | 33 | nan | nan | nan | Pantanal | 2.7 |
| 33f7e120-84e8-3765-9843-984f96b6fb57 | -18.24988 | -55.98041 | 2024-10-30 05:12:00 | NOAA-20 | CORUMBÁ | MATO GROSSO DO SUL | Brasil | 5003207 | 50 | 33 | nan | nan | nan | Pantanal | 3.2 |
| 9234209d-e813-3dae-9aec-3d9dba78c9a7 | -18.24962 | -55.98278 | 2024-10-30 05:12:00 | NOAA-20 | CORUMBÁ | MATO GROSSO DO SUL | Brasil | 5003207 | 50 | 33 | nan | nan | nan | Pantanal | 2.7 |
| eaa89d48-a97d-33f8-a623-df72130a0bcf | -18.24736 | -55.9702 | 2024-10-30 05:12:00 | NOAA-20 | CORUMBÁ | MATO GROSSO DO SUL | Brasil | 5003207 | 50 | 33 | nan | nan | nan | Pantanal | 1.6 |
| ba0b8580-68f9-3c77-8d26-3dcddfe221a9 | -18.24716 | -55.9726 | 2024-10-30 05:12:00 | NOAA-20 | CORUMBÁ | MATO GROSSO DO SUL | Brasil | 5003207 | 50 | 33 | nan | nan | nan | Pantanal | 3.3 |
| b9e6a776-e90b-34f0-85ca-181fb95b2a04 | -18.24673 | -55.97503 | 2024-10-30 05:12:00 | NOAA-20 | CORUMBÁ | MATO GROSSO DO SUL | Brasil | 5003207 | 50 | 33 | nan | nan | nan | Pantanal | 3.8 |
| 27cc80dc-c25d-36d7-b635-3d035efaa4d1 | -17.96558 | -54.48808 | 2024-10-30 05:12:00 | NOAA-20 | PEDRO GOMES | MATO GROSSO DO SUL | Brasil | 5006408 | 50 | 33 | nan | nan | nan | Cerrado | 0.8 |
| a1438149-2ea5-3577-86af-228198797de6 | -20.03198 | -54.67334 | 2024-10-30 05:12:00 | NOAA-20 | JARAGUARI | MATO GROSSO DO SUL | Brasil | 5004908 | 50 | 33 | nan | nan | nan | Cerrado | 0.9 |
| 6121eb7c-eec3-353a-bd9b-940309e81278 | -20.03122 | -54.67457 | 2024-10-30 05:12:00 | NOAA-20 | JARAGUARI | MATO GROSSO DO SUL | Brasil | 5004908 | 50 | 33 | nan | nan | nan | Cerrado | 0.9 |
| 1d8ada9e-a52c-3b9f-b9e0-35fda5dbc798 | -18.2465 | -55.97741 | 2024-10-30 05:12:00 | NOAA-20 | CORUMBÁ | MATO GROSSO DO SUL | Brasil | 5003207 | 50 | 33 | nan | nan | nan | Pantanal | 3.5 |
| 9e05b181-48f5-3c64-9f66-8f651a9267e4 | -18.25681 | -55.98635 | 2024-10-30 05:12:00 | NOAA-20 | CORUMBÁ | MATO GROSSO DO SUL | Brasil | 5003207 | 50 | 33 | nan | nan | nan | Pantanal | 3.6 |
| aee91c81-ad4c-3d0a-bef4-2f560b7bf224 | -18.25558 | -55.9665 | 2024-10-30 05:12:00 | NOAA-20 | CORUMBÁ | MATO GROSSO DO SUL | Brasil | 5003207 | 50 | 33 | nan | nan | nan | Pantanal | 2.2 |
| c7fbd261-5e6e-393b-a5a7-fbd8c8ca051b | -16.55624 | -56.23195 | 2024-10-30 05:12:00 | NOAA-20 | BARÃO DE MELGAÇO | MATO GROSSO | Brasil | 5101605 | 51 | 33 | nan | nan | nan | Pantanal | 1.3 |
| ed2454a5-c0a8-3959-aef4-724ffdbcafb3 | -16.55989 | -56.23249 | 2024-10-30 05:12:00 | NOAA-20 | BARÃO DE MELGAÇO | MATO GROSSO | Brasil | 5101605 | 51 | 33 | nan | nan | nan | Pantanal | 1.3 |
| 0ff81abe-8586-345d-ae05-fff879e3adb0 | -18.73535 | -55.59281 | 2024-10-30 05:12:00 | NOAA-20 | CORUMBÁ | MATO GROSSO DO SUL | Brasil | 5003207 | 50 | 33 | nan | nan | nan | Pantanal | 2.8 |
| 650b1dd5-39b7-34ef-9e70-9883b2abd183 | -18.73424 | -55.59567 | 2024-10-30 05:12:00 | NOAA-20 | CORUMBÁ | MATO GROSSO DO SUL | Brasil | 5003207 | 50 | 33 | nan | nan | nan | Pantanal | 5.0 |
| 1459df47-7924-3354-8a3e-0cb3d03480e9 | -18.73145 | -55.59224 | 2024-10-30 05:12:00 | NOAA-20 | CORUMBÁ | MATO GROSSO DO SUL | Brasil | 5003207 | 50 | 33 | nan | nan | nan | Pantanal | 2.8 |
| b64e6cef-6e84-30c9-8ebb-ddabc7992080 | -18.73035 | -55.59511 | 2024-10-30 05:12:00 | NOAA-20 | CORUMBÁ | MATO GROSSO DO SUL | Brasil | 5003207 | 50 | 33 | nan | nan | nan | Pantanal | 2.0 |
| 2de8bb95-4374-394b-865d-14dcc4f0a68b | -18.26566 | -55.97785 | 2024-10-30 05:12:00 | NOAA-20 | CORUMBÁ | MATO GROSSO DO SUL | Brasil | 5003207 | 50 | 33 | nan | nan | nan | Pantanal | 1.5 |
| b6c04b07-1971-3d38-96f9-6bcfda12c620 | -18.26187 | -55.97728 | 2024-10-30 05:12:00 | NOAA-20 | CORUMBÁ | MATO GROSSO DO SUL | Brasil | 5003207 | 50 | 33 | nan | nan | nan | Pantanal | 24.2 |
| 256b27f7-5af8-3c4e-a3d4-b29ec75973d0 | -18.26123 | -55.98211 | 2024-10-30 05:12:00 | NOAA-20 | CORUMBÁ | MATO GROSSO DO SUL | Brasil | 5003207 | 50 | 33 | nan | nan | nan | Pantanal | 24.2 |
| a5e02bd8-8454-3bb7-9884-74148b6b5085 | -18.25872 | -55.97188 | 2024-10-30 05:12:00 | NOAA-20 | CORUMBÁ | MATO GROSSO DO SUL | Brasil | 5003207 | 50 | 33 | nan | nan | nan | Pantanal | 6.6 |
| 45310ca2-3d3e-33bd-8564-007b47b9a75f | -18.25809 | -55.97671 | 2024-10-30 05:12:00 | NOAA-20 | CORUMBÁ | MATO GROSSO DO SUL | Brasil | 5003207 | 50 | 33 | nan | nan | nan | Pantanal | 24.2 |
| 2861f386-dfbe-31d9-af5b-0473bc60f9e4 | -18.25745 | -55.98154 | 2024-10-30 05:12:00 | NOAA-20 | CORUMBÁ | MATO GROSSO DO SUL | Brasil | 5003207 | 50 | 33 | nan | nan | nan | Pantanal | 24.2 |
| 12e4f1e5-66a4-3b36-a7c0-4ef8b87522e3 | -18.2554 | -55.96889 | 2024-10-30 05:12:00 | NOAA-20 | CORUMBÁ | MATO GROSSO DO SUL | Brasil | 5003207 | 50 | 33 | nan | nan | nan | Pantanal | 3.3 |
| 869ab078-7d3b-3a4f-b0d6-08a01ecdea19 | -18.25494 | -55.97132 | 2024-10-30 05:12:00 | NOAA-20 | CORUMBÁ | MATO GROSSO DO SUL | Brasil | 5003207 | 50 | 33 | nan | nan | nan | Pantanal | 2.2 |
| 3b9fa081-cc46-3283-8cc4-b66835d7c406 | -18.25474 | -55.97371 | 2024-10-30 05:12:00 | NOAA-20 | CORUMBÁ | MATO GROSSO DO SUL | Brasil | 5003207 | 50 | 33 | nan | nan | nan | Pantanal | 3.3 |
| a73b965a-2be0-3494-8704-f88268ddef9b | -18.2543 | -55.97615 | 2024-10-30 05:12:00 | NOAA-20 | CORUMBÁ | MATO GROSSO DO SUL | Brasil | 5003207 | 50 | 33 | nan | nan | nan | Pantanal | 3.2 |
| c2609224-15d9-3018-af7a-13253b25bbdd | -18.25407 | -55.97853 | 2024-10-30 05:12:00 | NOAA-20 | CORUMBÁ | MATO GROSSO DO SUL | Brasil | 5003207 | 50 | 33 | nan | nan | nan | Pantanal | 2.7 |
| 7aa278fc-9b56-3d9b-894d-8aef84583c38 | -18.25366 | -55.98097 | 2024-10-30 05:12:00 | NOAA-20 | CORUMBÁ | MATO GROSSO DO SUL | Brasil | 5003207 | 50 | 33 | nan | nan | nan | Pantanal | 3.2 |
| 561c094b-1c10-39d8-ac9b-06c6c6f75cab | -18.2534 | -55.98334 | 2024-10-30 05:12:00 | NOAA-20 | CORUMBÁ | MATO GROSSO DO SUL | Brasil | 5003207 | 50 | 33 | nan | nan | nan | Pantanal | 2.7 |
| 0ad735b4-ad8d-3809-84b4-e7bc040ad920 | -18.25303 | -55.98579 | 2024-10-30 05:12:00 | NOAA-20 | CORUMBÁ | MATO GROSSO DO SUL | Brasil | 5003207 | 50 | 33 | nan | nan | nan | Pantanal | 2.5 |
| b1c52b2a-05c7-39f7-967a-91cbcc052a9c | -18.25242 | -55.96111 | 2024-10-30 05:12:00 | NOAA-20 | CORUMBÁ | MATO GROSSO DO SUL | Brasil | 5003207 | 50 | 33 | nan | nan | nan | Pantanal | 2.2 |
| 78da20cb-80e0-3ffe-84f5-d7663cf1d376 | -18.25228 | -55.96352 | 2024-10-30 05:12:00 | NOAA-20 | CORUMBÁ | MATO GROSSO DO SUL | Brasil | 5003207 | 50 | 33 | nan | nan | nan | Pantanal | 3.4 |
| 8d196c16-947e-32a0-8b75-df716b3a4aa0 | -18.25179 | -55.96594 | 2024-10-30 05:12:00 | NOAA-20 | CORUMBÁ | MATO GROSSO DO SUL | Brasil | 5003207 | 50 | 33 | nan | nan | nan | Pantanal | 2.2 |
| 7104fcfb-b82c-38bc-a4cc-03a9805dab57 | -18.25161 | -55.96834 | 2024-10-30 05:12:00 | NOAA-20 | CORUMBÁ | MATO GROSSO DO SUL | Brasil | 5003207 | 50 | 33 | nan | nan | nan | Pantanal | 3.3 |
| def40a80-608b-322f-bfaf-bf63f756c4fb | -19.47962 | -56.63911 | 2024-10-30 05:12:00 | NOAA-20 | CORUMBÁ | MATO GROSSO DO SUL | Brasil | 5003207 | 50 | 33 | nan | nan | nan | Pantanal | 1.4 |
| 3c5780aa-a4c1-3d6c-a574-0474966c7091 | -19.479 | -56.64374 | 2024-10-30 05:12:00 | NOAA-20 | CORUMBÁ | MATO GROSSO DO SUL | Brasil | 5003207 | 50 | 33 | nan | nan | nan | Pantanal | 1.4 |
| a0106957-42b4-3f61-bfa2-91167eb28541 | -19.47653 | -56.63391 | 2024-10-30 05:12:00 | NOAA-20 | CORUMBÁ | MATO GROSSO DO SUL | Brasil | 5003207 | 50 | 33 | nan | nan | nan | Pantanal | 1.2 |
| e11082ee-fdec-397b-a818-1c2ee1ec8732 | -19.47591 | -56.63855 | 2024-10-30 05:12:00 | NOAA-20 | CORUMBÁ | MATO GROSSO DO SUL | Brasil | 5003207 | 50 | 33 | nan | nan | nan | Pantanal | 2.0 |
| e9ceb6fc-fe50-3f88-b60b-2a6717a1159a | -19.46974 | -56.62815 | 2024-10-30 05:12:00 | NOAA-20 | CORUMBÁ | MATO GROSSO DO SUL | Brasil | 5003207 | 50 | 33 | nan | nan | nan | Pantanal | 4.4 |
| 1ed726b1-7854-3ee2-803e-affe2f7c8439 | -19.46912 | -56.63279 | 2024-10-30 05:12:00 | NOAA-20 | CORUMBÁ | MATO GROSSO DO SUL | Brasil | 5003207 | 50 | 33 | nan | nan | nan | Pantanal | 4.4 |
| 738c8daa-3208-33dc-8e14-6368b473f310 | -19.46665 | -56.62294 | 2024-10-30 05:12:00 | NOAA-20 | CORUMBÁ | MATO GROSSO DO SUL | Brasil | 5003207 | 50 | 33 | nan | nan | nan | Pantanal | 3.0 |
| af37d77b-e30e-3d4b-8de5-100cb162571a | -19.46603 | -56.62759 | 2024-10-30 05:12:00 | NOAA-20 | CORUMBÁ | MATO GROSSO DO SUL | Brasil | 5003207 | 50 | 33 | nan | nan | nan | Pantanal | 4.4 |
| ebfd451a-9a8c-35dc-bd4d-1b8ecf0ab27b | -19.46541 | -56.63223 | 2024-10-30 05:12:00 | NOAA-20 | CORUMBÁ | MATO GROSSO DO SUL | Brasil | 5003207 | 50 | 33 | nan | nan | nan | Pantanal | 4.4 |
| dcc9558d-176b-3eda-b717-77946e87a4e5 | -19.62516 | -56.69563 | 2024-10-30 05:12:00 | NOAA-20 | AQUIDAUANA | MATO GROSSO DO SUL | Brasil | 5001102 | 50 | 33 | nan | nan | nan | Pantanal | 8.2 |
| 125c9582-b909-339e-b758-8d4c27d5eb98 | -19.62146 | -56.69506 | 2024-10-30 05:12:00 | NOAA-20 | AQUIDAUANA | MATO GROSSO DO SUL | Brasil | 5001102 | 50 | 33 | nan | nan | nan | Pantanal | 4.0 |
| ae9b5d82-3287-3fc1-bd39-df28e8f62989 | -19.61776 | -56.69451 | 2024-10-30 05:12:00 | NOAA-20 | AQUIDAUANA | MATO GROSSO DO SUL | Brasil | 5001102 | 50 | 33 | nan | nan | nan | Pantanal | 4.0 |
| 2fd9f248-78d9-301a-87f8-29d9b95647ef | -19.60603 | -56.69746 | 2024-10-30 05:12:00 | NOAA-20 | AQUIDAUANA | MATO GROSSO DO SUL | Brasil | 5001102 | 50 | 33 | nan | nan | nan | Pantanal | 9.1 |
| d585886b-06e7-30ae-8503-ac4cdc0e0fe4 | -19.59863 | -56.69634 | 2024-10-30 05:12:00 | NOAA-20 | AQUIDAUANA | MATO GROSSO DO SUL | Brasil | 5001102 | 50 | 33 | nan | nan | nan | Pantanal | 2.1 |
| 564242d2-c279-399b-85f5-954d03336f7d | -19.56841 | -56.69649 | 2024-10-30 05:12:00 | NOAA-20 | AQUIDAUANA | MATO GROSSO DO SUL | Brasil | 5001102 | 50 | 33 | nan | nan | nan | Pantanal | 1.7 |
| e37b2cbf-6930-3de5-8c6b-bb2d7402e55e | -19.56471 | -56.69593 | 2024-10-30 05:12:00 | NOAA-20 | AQUIDAUANA | MATO GROSSO DO SUL | Brasil | 5001102 | 50 | 33 | nan | nan | nan | Pantanal | 1.7 |
| 10585920-9773-32e4-b46b-61847551554d | -19.52453 | -56.69775 | 2024-10-30 05:12:00 | NOAA-20 | CORUMBÁ | MATO GROSSO DO SUL | Brasil | 5003207 | 50 | 33 | nan | nan | nan | Pantanal | 2.9 |
| 61700bbb-97ae-383d-b83f-fe70c9b3f0fc | -19.5094 | -56.58665 | 2024-10-30 05:12:00 | NOAA-20 | CORUMBÁ | MATO GROSSO DO SUL | Brasil | 5003207 | 50 | 33 | nan | nan | nan | Pantanal | 10.1 |
| 03dc42eb-0a93-3b5d-b3f9-03b569fc43d7 | -19.50877 | -56.59131 | 2024-10-30 05:12:00 | NOAA-20 | CORUMBÁ | MATO GROSSO DO SUL | Brasil | 5003207 | 50 | 33 | nan | nan | nan | Pantanal | 10.1 |
| e334073b-32f0-32da-9be8-394da927a6ad | -19.50814 | -56.59598 | 2024-10-30 05:12:00 | NOAA-20 | CORUMBÁ | MATO GROSSO DO SUL | Brasil | 5003207 | 50 | 33 | nan | nan | nan | Pantanal | 8.9 |
| 97827bbc-ff63-38fc-bb15-40f01faa0336 | -19.50794 | -56.68113 | 2024-10-30 05:12:00 | NOAA-20 | CORUMBÁ | MATO GROSSO DO SUL | Brasil | 5003207 | 50 | 33 | nan | nan | nan | Pantanal | 3.9 |
| 77da56ad-42f4-34e7-b31d-09eb9d189f67 | -19.50731 | -56.68575 | 2024-10-30 05:12:00 | NOAA-20 | CORUMBÁ | MATO GROSSO DO SUL | Brasil | 5003207 | 50 | 33 | nan | nan | nan | Pantanal | 3.9 |
| df80ffd3-1f38-3fd6-b2af-f6e050310818 | -19.50668 | -56.69036 | 2024-10-30 05:12:00 | NOAA-20 | CORUMBÁ | MATO GROSSO DO SUL | Brasil | 5003207 | 50 | 33 | nan | nan | nan | Pantanal | 3.8 |
| d1d1cd01-8408-37ec-830c-fd1fd992f093 | -19.50569 | -56.58609 | 2024-10-30 05:12:00 | NOAA-20 | CORUMBÁ | MATO GROSSO DO SUL | Brasil | 5003207 | 50 | 33 | nan | nan | nan | Pantanal | 3.8 |
| b9ec7f48-50be-3468-a27f-fd7defbef223 | -19.50506 | -56.59076 | 2024-10-30 05:12:00 | NOAA-20 | CORUMBÁ | MATO GROSSO DO SUL | Brasil | 5003207 | 50 | 33 | nan | nan | nan | Pantanal | 3.8 |
| 2dad020e-4400-330b-857a-b3a584135615 | -19.50443 | -56.59542 | 2024-10-30 05:12:00 | NOAA-20 | CORUMBÁ | MATO GROSSO DO SUL | Brasil | 5003207 | 50 | 33 | nan | nan | nan | Pantanal | 2.4 |
| 63f65b46-29dd-3386-b246-942c8734a3ce | -19.50361 | -56.68519 | 2024-10-30 05:12:00 | NOAA-20 | CORUMBÁ | MATO GROSSO DO SUL | Brasil | 5003207 | 50 | 33 | nan | nan | nan | Pantanal | 3.9 |
| 78d970ec-afc6-34e3-bf70-ce94764cb086 | -19.5026 | -56.58086 | 2024-10-30 05:12:00 | NOAA-20 | CORUMBÁ | MATO GROSSO DO SUL | Brasil | 5003207 | 50 | 33 | nan | nan | nan | Pantanal | 5.0 |
| c4f8a3e3-ac42-3194-be38-02d08da8145f | -19.50236 | -56.69441 | 2024-10-30 05:12:00 | NOAA-20 | CORUMBÁ | MATO GROSSO DO SUL | Brasil | 5003207 | 50 | 33 | nan | nan | nan | Pantanal | 3.8 |
| 624a80db-5d96-3b9c-bddf-49a7e3b146fe | -19.50197 | -56.58553 | 2024-10-30 05:12:00 | NOAA-20 | CORUMBÁ | MATO GROSSO DO SUL | Brasil | 5003207 | 50 | 33 | nan | nan | nan | Pantanal | 3.8 |
| a3502c96-4d11-3be6-b300-0b21c57446a4 | -19.50134 | -56.59019 | 2024-10-30 05:12:00 | NOAA-20 | CORUMBÁ | MATO GROSSO DO SUL | Brasil | 5003207 | 50 | 33 | nan | nan | nan | Pantanal | 3.8 |
| 2e0dc060-9ec2-33aa-b0fc-461a156d45e5 | -19.50071 | -56.59486 | 2024-10-30 05:12:00 | NOAA-20 | CORUMBÁ | MATO GROSSO DO SUL | Brasil | 5003207 | 50 | 33 | nan | nan | nan | Pantanal | 2.4 |
| 8ecbb036-1741-351c-afe4-6c8a9fddd343 | -19.49929 | -56.68924 | 2024-10-30 05:12:00 | NOAA-20 | CORUMBÁ | MATO GROSSO DO SUL | Brasil | 5003207 | 50 | 33 | nan | nan | nan | Pantanal | 1.4 |
| 515455d2-71b1-38d9-a99c-04ecae165d7a | -19.49866 | -56.69386 | 2024-10-30 05:12:00 | NOAA-20 | CORUMBÁ | MATO GROSSO DO SUL | Brasil | 5003207 | 50 | 33 | nan | nan | nan | Pantanal | 1.4 |
| b04610ee-4b5d-3b6c-8cfb-37a9c30d865d | -19.49762 | -56.58964 | 2024-10-30 05:12:00 | NOAA-20 | CORUMBÁ | MATO GROSSO DO SUL | Brasil | 5003207 | 50 | 33 | nan | nan | nan | Pantanal | 1.0 |
| 34f9043d-6ec6-3ebb-899d-4821ba2f9ce6 | -19.497 | -56.5943 | 2024-10-30 05:12:00 | NOAA-20 | CORUMBÁ | MATO GROSSO DO SUL | Brasil | 5003207 | 50 | 33 | nan | nan | nan | Pantanal | 3.8 |
| bec2b54e-ffa3-32a1-aee8-e719a520308d | -19.49559 | -56.68869 | 2024-10-30 05:12:00 | NOAA-20 | CORUMBÁ | MATO GROSSO DO SUL | Brasil | 5003207 | 50 | 33 | nan | nan | nan | Pantanal | 1.4 |
| d539caf6-e637-3703-9d24-15e4d81467e4 | -19.49434 | -56.6979 | 2024-10-30 05:12:00 | NOAA-20 | CORUMBÁ | MATO GROSSO DO SUL | Brasil | 5003207 | 50 | 33 | nan | nan | nan | Pantanal | 2.6 |
| de171210-bea8-3951-bea7-cd71b9b315ef | -19.49189 | -56.68813 | 2024-10-30 05:12:00 | NOAA-20 | CORUMBÁ | MATO GROSSO DO SUL | Brasil | 5003207 | 50 | 33 | nan | nan | nan | Pantanal | 1.8 |
| f1a31fde-b850-3666-a742-9f3d1202209a | -19.49127 | -56.69273 | 2024-10-30 05:12:00 | NOAA-20 | CORUMBÁ | MATO GROSSO DO SUL | Brasil | 5003207 | 50 | 33 | nan | nan | nan | Pantanal | 1.8 |
| fee91bf4-1491-320f-94dc-f3a5a5e44e53 | -19.49064 | -56.69734 | 2024-10-30 05:12:00 | NOAA-20 | CORUMBÁ | MATO GROSSO DO SUL | Brasil | 5003207 | 50 | 33 | nan | nan | nan | Pantanal | 1.6 |
| 82ad8a2a-b1fd-3972-bc8d-48465c9e0b33 | -19.48824 | -56.6593 | 2024-10-30 05:12:00 | NOAA-20 | CORUMBÁ | MATO GROSSO DO SUL | Brasil | 5003207 | 50 | 33 | nan | nan | nan | Pantanal | 2.7 |
| 20f79a32-0de8-39ff-b0c3-ded972697822 | -19.48695 | -56.69678 | 2024-10-30 05:12:00 | NOAA-20 | CORUMBÁ | MATO GROSSO DO SUL | Brasil | 5003207 | 50 | 33 | nan | nan | nan | Pantanal | 1.6 |
| 03584e7f-ce9d-3cfa-b229-dd58dc4770c2 | -19.48578 | -56.64949 | 2024-10-30 05:12:00 | NOAA-20 | CORUMBÁ | MATO GROSSO DO SUL | Brasil | 5003207 | 50 | 33 | nan | nan | nan | Pantanal | 1.3 |
| 9064e7ae-71be-3879-974c-09f28272de15 | -19.48516 | -56.65412 | 2024-10-30 05:12:00 | NOAA-20 | CORUMBÁ | MATO GROSSO DO SUL | Brasil | 5003207 | 50 | 33 | nan | nan | nan | Pantanal | 1.3 |
| ab4e8c6d-66cd-3b85-ac78-0cc2c8454f6c | -19.48457 | -56.63039 | 2024-10-30 05:12:00 | NOAA-20 | CORUMBÁ | MATO GROSSO DO SUL | Brasil | 5003207 | 50 | 33 | nan | nan | nan | Pantanal | 2.1 |
| ec32f174-2f7d-3bc1-9ef1-7ac16cc96538 | -19.4827 | -56.6443 | 2024-10-30 05:12:00 | NOAA-20 | CORUMBÁ | MATO GROSSO DO SUL | Brasil | 5003207 | 50 | 33 | nan | nan | nan | Pantanal | 1.4 |
| f3a7a0af-d912-3402-a4ad-f674b210375f | -19.48208 | -56.64893 | 2024-10-30 05:12:00 | NOAA-20 | CORUMBÁ | MATO GROSSO DO SUL | Brasil | 5003207 | 50 | 33 | nan | nan | nan | Pantanal | 4.3 |
| 16eb0d9b-5477-3cd2-b9cc-9483956fd3b3 | -19.48083 | -56.6582 | 2024-10-30 05:12:00 | NOAA-20 | CORUMBÁ | MATO GROSSO DO SUL | Brasil | 5003207 | 50 | 33 | nan | nan | nan | Pantanal | 5.8 |
| e821c4c9-7931-33bd-9ae9-09852b66e33e | -19.48021 | -56.66282 | 2024-10-30 05:12:00 | NOAA-20 | CORUMBÁ | MATO GROSSO DO SUL | Brasil | 5003207 | 50 | 33 | nan | nan | nan | Pantanal | 5.8 |


[Clique aqui para ver as próximas entradas](README95.md)
