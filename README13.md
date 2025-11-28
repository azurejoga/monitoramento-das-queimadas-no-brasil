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

## Dados Diários - Página 13

| ID | Latitude | Longitude | Data/Hora GMT | Satélite | Município | Estado | País | Município ID | Estado ID | País ID | Dias sem Chuva | Precipitação | Risco de Fogo | Bioma | FRP |
|----|----------|-----------|---------------|----------|-----------|--------|------|--------------|-----------|---------|----------------|--------------|----------------|-------|-----|
| dd100167-0224-38f3-8989-885aea1c77ec | -5.3515 | -44.88027 | 2025-11-28 04:31:00 | NOAA-21 | TUNTUM | MARANHÃO | Brasil | 2112308 | 21 | 33 | nan | nan | nan | Cerrado | 2.3 |
| a7fe9c81-030c-353f-88da-2b7d757e8bf5 | -3.75661 | -46.95539 | 2025-11-28 04:31:00 | NOAA-21 | CENTRO NOVO DO MARANHÃO | MARANHÃO | Brasil | 2103174 | 21 | 33 | nan | nan | nan | Amazônia | 1.7 |
| 1e2c9265-1de4-325d-9971-0e6cd596e0ab | -1.24444 | -54.05526 | 2025-11-28 04:31:00 | NOAA-21 | MONTE ALEGRE | PARÁ | Brasil | 1504802 | 15 | 33 | nan | nan | nan | Amazônia | 1.3 |
| ebadaee7-0f7e-3a10-acb4-52e9393d6748 | -2.64965 | -46.96453 | 2025-11-28 04:31:00 | NOAA-21 | PARAGOMINAS | PARÁ | Brasil | 1505502 | 15 | 33 | nan | nan | nan | Amazônia | 1.1 |
| e17ef29a-ac29-3ed4-a788-817ed8896287 | -2.83892 | -52.40148 | 2025-11-28 04:31:00 | NOAA-21 | BRASIL NOVO | PARÁ | Brasil | 1501725 | 15 | 33 | nan | nan | nan | Amazônia | 0.7 |
| 0b8b5471-154f-3434-baeb-8f4721ab3700 | -2.56375 | -49.03837 | 2025-11-28 04:31:00 | NOAA-21 | MOJU | PARÁ | Brasil | 1504703 | 15 | 33 | nan | nan | nan | Amazônia | 1.5 |
| 51a1f145-5b2f-3a59-87bc-61d0b0c8e823 | -3.5662 | -53.03337 | 2025-11-28 04:31:00 | NOAA-21 | MEDICILÂNDIA | PARÁ | Brasil | 1504455 | 15 | 33 | nan | nan | nan | Amazônia | 0.8 |
| 39c9f558-3a39-35d6-8765-0c906f0cca6d | -1.36293 | -55.43833 | 2025-11-28 04:31:00 | NOAA-21 | ÓBIDOS | PARÁ | Brasil | 1505106 | 15 | 33 | nan | nan | nan | Amazônia | 0.8 |
| 2af3a6d1-fdc3-3767-914e-34104aaa4c24 | -2.76886 | -49.6418 | 2025-11-28 04:31:00 | NOAA-21 | BAIÃO | PARÁ | Brasil | 1501204 | 15 | 33 | nan | nan | nan | Amazônia | 3.6 |
| da767584-6dee-34b1-b52f-7b3fbd2788c8 | -3.75715 | -46.95196 | 2025-11-28 04:31:00 | NOAA-21 | CENTRO NOVO DO MARANHÃO | MARANHÃO | Brasil | 2103174 | 21 | 33 | nan | nan | nan | Amazônia | 1.7 |
| 91cf5e52-4942-36de-ab9a-fade1a176bcb | -2.98646 | -49.11843 | 2025-11-28 04:31:00 | NOAA-21 | MOJU | PARÁ | Brasil | 1504703 | 15 | 33 | nan | nan | nan | Amazônia | 0.7 |
| fdca6933-5be3-36d9-8330-24074418dfba | -3.17585 | -48.61129 | 2025-11-28 04:31:00 | NOAA-21 | TAILÂNDIA | PARÁ | Brasil | 1507953 | 15 | 33 | nan | nan | nan | Amazônia | 2.7 |
| aa6571d0-9e1f-3382-b77b-036afc77203d | -3.96498 | -50.19272 | 2025-11-28 04:31:00 | NOAA-21 | PACAJÁ | PARÁ | Brasil | 1505486 | 15 | 33 | nan | nan | nan | Amazônia | 1.4 |
| 209abdfd-3833-3225-a9f6-6e9e8a17d047 | -3.0655 | -50.38087 | 2025-11-28 04:31:00 | NOAA-21 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 1.0 |
| 18352b1e-6ac9-3d41-8d2a-51ec40f469bb | -2.41882 | -45.73937 | 2025-11-28 04:31:00 | NOAA-21 | SANTA LUZIA DO PARUÁ | MARANHÃO | Brasil | 2110039 | 21 | 33 | nan | nan | nan | Amazônia | 0.9 |
| 147239d6-4a75-3c68-9c34-275b598e7b82 | -4.54574 | -45.75351 | 2025-11-28 04:31:00 | NOAA-21 | SANTA LUZIA | MARANHÃO | Brasil | 2110005 | 21 | 33 | nan | nan | nan | Amazônia | 1.0 |
| 7a0f485c-58be-3378-8ac5-f9a77039783c | -4.29806 | -55.61504 | 2025-11-28 04:31:00 | NOAA-21 | RURÓPOLIS | PARÁ | Brasil | 1506195 | 15 | 33 | nan | nan | nan | Amazônia | 2.0 |
| 9891ffc9-742d-3567-81e1-ee920d8e0d36 | -2.41017 | -47.5999 | 2025-11-28 04:31:00 | NOAA-21 | IPIXUNA DO PARÁ | PARÁ | Brasil | 1503457 | 15 | 33 | nan | nan | nan | Amazônia | 0.9 |
| e13ef6b6-5270-3fb8-be59-18e16fe3d9f8 | -5.13091 | -43.02175 | 2025-11-28 04:31:00 | NOAA-21 | TIMON | MARANHÃO | Brasil | 2112209 | 21 | 33 | nan | nan | nan | Cerrado | 12.4 |
| 1552b1ed-959c-3aa5-88f6-1229ebeb613b | -6.72286 | -40.81532 | 2025-11-28 04:31:00 | NOAA-21 | PIO IX | PIAUÍ | Brasil | 2208205 | 22 | 33 | nan | nan | nan | Caatinga | 4.1 |
| 8aaf8ba7-3bac-3acc-b80e-30011f6250a6 | -3.39734 | -44.17916 | 2025-11-28 04:31:00 | NOAA-21 | ITAPECURU MIRIM | MARANHÃO | Brasil | 2105401 | 21 | 33 | nan | nan | nan | Cerrado | 1.7 |
| 2564f719-5be1-36d2-9b9d-3c5e18fd21ba | -3.56194 | -53.03275 | 2025-11-28 04:31:00 | NOAA-21 | MEDICILÂNDIA | PARÁ | Brasil | 1504455 | 15 | 33 | nan | nan | nan | Amazônia | 0.8 |
| 78eaeece-ef50-317e-8891-d058c2bbe414 | -2.74924 | -47.13126 | 2025-11-28 04:31:00 | NOAA-21 | PARAGOMINAS | PARÁ | Brasil | 1505502 | 15 | 33 | nan | nan | nan | Amazônia | 1.2 |
| c65e7c20-41ea-3b1a-8b45-23747e973bff | -3.74322 | -50.96838 | 2025-11-28 04:31:00 | NOAA-21 | PACAJÁ | PARÁ | Brasil | 1505486 | 15 | 33 | nan | nan | nan | Amazônia | 1.2 |
| 57d3583f-5690-3fe5-bc89-734f7b0d237b | -3.40911 | -53.30396 | 2025-11-28 04:31:00 | NOAA-21 | MEDICILÂNDIA | PARÁ | Brasil | 1504455 | 15 | 33 | nan | nan | nan | Amazônia | 6.0 |
| cb702fd5-16b4-3e6c-aac6-868fa0aad9d7 | -5.3509 | -44.88426 | 2025-11-28 04:31:00 | NOAA-21 | TUNTUM | MARANHÃO | Brasil | 2112308 | 21 | 33 | nan | nan | nan | Cerrado | 1.8 |
| b5f96608-118f-3044-9093-d3d953de0adf | -2.65295 | -46.96505 | 2025-11-28 04:31:00 | NOAA-21 | PARAGOMINAS | PARÁ | Brasil | 1505502 | 15 | 33 | nan | nan | nan | Amazônia | 1.1 |
| 152d13ad-43bf-3720-a951-1be65750713e | -2.47004 | -50.23707 | 2025-11-28 04:31:00 | NOAA-21 | BAGRE | PARÁ | Brasil | 1501105 | 15 | 33 | nan | nan | nan | Amazônia | 0.9 |
| d0608ea2-ed83-3c3c-825f-956817796e13 | -3.49249 | -53.26706 | 2025-11-28 04:31:00 | NOAA-21 | MEDICILÂNDIA | PARÁ | Brasil | 1504455 | 15 | 33 | nan | nan | nan | Amazônia | 1.0 |
| b0f4c3bf-1f79-3d25-9a9d-4e15809c75e8 | -3.93192 | -50.171 | 2025-11-28 04:31:00 | NOAA-21 | PACAJÁ | PARÁ | Brasil | 1505486 | 15 | 33 | nan | nan | nan | Amazônia | 3.8 |
| 0bf3b585-004e-3564-b3aa-cfc1ed94a326 | -4.44345 | -50.98011 | 2025-11-28 04:31:00 | NOAA-21 | ANAPU | PARÁ | Brasil | 1500859 | 15 | 33 | nan | nan | nan | Amazônia | 1.1 |
| d6042fd2-2a30-3a68-8920-045890c65377 | -3.75 | -46.95437 | 2025-11-28 04:31:00 | NOAA-21 | CENTRO NOVO DO MARANHÃO | MARANHÃO | Brasil | 2103174 | 21 | 33 | nan | nan | nan | Amazônia | 0.7 |
| 896473ac-e8ed-3483-8f5e-ab0cfde65331 | -4.82859 | -49.89565 | 2025-11-28 04:31:00 | NOAA-21 | ITUPIRANGA | PARÁ | Brasil | 1503705 | 15 | 33 | nan | nan | nan | Amazônia | 1.2 |
| ee132009-e8e1-3a29-b899-ce0527db028b | -0.86724 | -47.30841 | 2025-11-28 04:31:00 | NOAA-21 | SANTARÉM NOVO | PARÁ | Brasil | 1506906 | 15 | 33 | nan | nan | nan | Amazônia | 1.5 |
| 5486d76b-cf0b-373c-9210-7d356402b9e1 | -2.99068 | -43.8407 | 2025-11-28 04:31:00 | NOAA-21 | MORROS | MARANHÃO | Brasil | 2107100 | 21 | 33 | nan | nan | nan | Cerrado | 1.8 |
| e9b0429f-d2af-3252-beda-1205f6619f87 | -1.49986 | -54.70596 | 2025-11-28 04:31:00 | NOAA-21 | ALENQUER | PARÁ | Brasil | 1500404 | 15 | 33 | nan | nan | nan | Amazônia | 3.4 |
| 08600ba0-955c-3031-8d20-55aab309424f | -3.41277 | -53.30882 | 2025-11-28 04:31:00 | NOAA-21 | MEDICILÂNDIA | PARÁ | Brasil | 1504455 | 15 | 33 | nan | nan | nan | Amazônia | 5.3 |
| cfaf5197-4065-3239-87db-5beb1733031a | -3.78905 | -49.86058 | 2025-11-28 04:31:00 | NOAA-21 | TUCURUÍ | PARÁ | Brasil | 1508100 | 15 | 33 | nan | nan | nan | Amazônia | 0.5 |
| e1fc80c5-243e-30a8-8c9b-51dafa897a37 | -4.30448 | -48.59835 | 2025-11-28 04:31:00 | NOAA-21 | RONDON DO PARÁ | PARÁ | Brasil | 1506187 | 15 | 33 | nan | nan | nan | Amazônia | 0.6 |
| 2921d888-885a-3ceb-a9dc-d79d9215acaa | -2.43616 | -50.25892 | 2025-11-28 04:31:00 | NOAA-21 | BAGRE | PARÁ | Brasil | 1501105 | 15 | 33 | nan | nan | nan | Amazônia | 1.7 |
| f11f49fc-0111-3e03-ab59-1a64336c601d | -3.84865 | -47.04084 | 2025-11-28 04:31:00 | NOAA-21 | ITINGA DO MARANHÃO | MARANHÃO | Brasil | 2105427 | 21 | 33 | nan | nan | nan | Amazônia | 1.5 |
| e73c3436-f52d-34d9-8d6c-46d233dfd419 | -2.85482 | -53.01072 | 2025-11-28 04:31:00 | NOAA-21 | MEDICILÂNDIA | PARÁ | Brasil | 1504455 | 15 | 33 | nan | nan | nan | Amazônia | 0.6 |
| 87605f66-1b20-3132-b74c-29f77e00b220 | -2.76306 | -48.62109 | 2025-11-28 04:31:00 | NOAA-21 | TAILÂNDIA | PARÁ | Brasil | 1507953 | 15 | 33 | nan | nan | nan | Amazônia | 1.3 |
| df1be21b-71e5-3d99-9c52-0e08fff53d4e | -2.71443 | -53.18373 | 2025-11-28 04:31:00 | NOAA-21 | MEDICILÂNDIA | PARÁ | Brasil | 1504455 | 15 | 33 | nan | nan | nan | Amazônia | 2.2 |
| 83a1cb61-a530-30da-bd2f-4493949777c8 | -5.06252 | -40.82095 | 2025-11-28 04:31:00 | NOAA-21 | CRATEÚS | CEARÁ | Brasil | 2304103 | 23 | 33 | nan | nan | nan | Caatinga | 9.9 |
| c5d456f1-9fef-3985-b67e-97c4216fb131 | -5.54532 | -47.75972 | 2025-11-28 04:31:00 | NOAA-21 | SÍTIO NOVO DO TOCANTINS | TOCANTINS | Brasil | 1720804 | 17 | 33 | nan | nan | nan | Cerrado | 1.0 |
| 2bd1e0c2-deaa-3565-8980-a93ae782326a | -2.36561 | -47.6889 | 2025-11-28 04:31:00 | NOAA-21 | IPIXUNA DO PARÁ | PARÁ | Brasil | 1503457 | 15 | 33 | nan | nan | nan | Amazônia | 1.5 |
| 0d1a4ad8-0bc4-3ecc-bee0-c9be0b6d1376 | -2.62672 | -47.34794 | 2025-11-28 04:31:00 | NOAA-21 | IPIXUNA DO PARÁ | PARÁ | Brasil | 1503457 | 15 | 33 | nan | nan | nan | Amazônia | 1.1 |
| 43d523d2-435b-3f9e-b530-80582e5b912d | -5.75417 | -45.11567 | 2025-11-28 04:31:00 | NOAA-21 | BARRA DO CORDA | MARANHÃO | Brasil | 2101608 | 21 | 33 | nan | nan | nan | Cerrado | 4.1 |
| b9119963-cade-3481-9ab5-ff423d268ecd | -4.30309 | -55.61578 | 2025-11-28 04:31:00 | NOAA-21 | RURÓPOLIS | PARÁ | Brasil | 1506195 | 15 | 33 | nan | nan | nan | Amazônia | 1.0 |
| 3925c15b-01a2-3c1d-b711-74c36ecfc621 | -3.35098 | -54.08765 | 2025-11-28 04:31:00 | NOAA-21 | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | 2.5 |
| 3dbfbfdc-c54c-3f06-9367-411d0948bba9 | -4.02201 | -50.73291 | 2025-11-28 04:31:00 | NOAA-21 | NOVO REPARTIMENTO | PARÁ | Brasil | 1505064 | 15 | 33 | nan | nan | nan | Amazônia | 1.0 |
| 97676b86-b3d8-342f-9292-25a32cc61f4f | -3.51749 | -43.67922 | 2025-11-28 04:31:00 | NOAA-21 | NINA RODRIGUES | MARANHÃO | Brasil | 2107209 | 21 | 33 | nan | nan | nan | Cerrado | 2.2 |
| f949b942-dd51-38a5-adc1-70eea16f60d5 | -3.17642 | -48.60769 | 2025-11-28 04:31:00 | NOAA-21 | TAILÂNDIA | PARÁ | Brasil | 1507953 | 15 | 33 | nan | nan | nan | Amazônia | 2.7 |
| 0c788193-da9a-3237-9dc4-fca178632a19 | -3.63829 | -44.88233 | 2025-11-28 04:31:00 | NOAA-21 | VITÓRIA DO MEARIM | MARANHÃO | Brasil | 2112902 | 21 | 33 | nan | nan | nan | Amazônia | 2.5 |
| 86db28b0-b4ca-385d-a026-8caeaaa34d2b | -4.3081 | -50.9336 | 2025-11-28 04:31:00 | NOAA-21 | NOVO REPARTIMENTO | PARÁ | Brasil | 1505064 | 15 | 33 | nan | nan | nan | Amazônia | 1.0 |
| 0a90506d-eb1d-3cae-b5a1-34646b72857b | -3.65569 | -42.23807 | 2025-11-28 04:31:00 | NOAA-21 | MORRO DO CHAPÉU DO PIAUÍ | PIAUÍ | Brasil | 2206670 | 22 | 33 | nan | nan | nan | Caatinga | 1.4 |
| 4acbb2ce-70db-3eeb-898e-4355a919f683 | -4.71131 | -46.28141 | 2025-11-28 04:31:00 | NOAA-21 | BURITICUPU | MARANHÃO | Brasil | 2102325 | 21 | 33 | nan | nan | nan | Amazônia | 1.7 |
| d5fbe5dc-e188-309b-a791-020c5050521d | -3.18146 | -48.61954 | 2025-11-28 04:31:00 | NOAA-21 | TAILÂNDIA | PARÁ | Brasil | 1507953 | 15 | 33 | nan | nan | nan | Amazônia | 1.2 |
| c4542bcc-4e75-3ddc-82bb-22d9470e0bce | -4.0384 | -43.36084 | 2025-11-28 04:31:00 | NOAA-21 | CHAPADINHA | MARANHÃO | Brasil | 2103208 | 21 | 33 | nan | nan | nan | Cerrado | 4.0 |
| 4d7ab119-868a-3b67-93e1-1ce62a988996 | -2.7319 | -51.83664 | 2025-11-28 04:31:00 | NOAA-21 | SENADOR JOSÉ PORFÍRIO | PARÁ | Brasil | 1507805 | 15 | 33 | nan | nan | nan | Amazônia | 1.9 |
| 8753903d-ad22-3fb8-9be5-65c6a89ecc5a | -2.56891 | -54.76022 | 2025-11-28 04:31:00 | NOAA-21 | SANTARÉM | PARÁ | Brasil | 1506807 | 15 | 33 | nan | nan | nan | Amazônia | 1.0 |
| b2279300-f367-33f1-9659-4ae2360821ed | -2.90835 | -39.973 | 2025-11-28 04:31:00 | NOAA-21 | ACARAÚ | CEARÁ | Brasil | 2300200 | 23 | 33 | nan | nan | nan | Caatinga | 4.4 |
| 2edd6d67-cc03-3954-bba4-07d4e5cc4a3f | -3.96434 | -50.19677 | 2025-11-28 04:31:00 | NOAA-21 | PACAJÁ | PARÁ | Brasil | 1505486 | 15 | 33 | nan | nan | nan | Amazônia | 1.4 |
| bb07fa92-593e-3826-aa9f-bcaacae13a1e | -5.792 | -47.8165 | 2025-11-28 04:31:00 | NOAA-21 | SÃO BENTO DO TOCANTINS | TOCANTINS | Brasil | 1720101 | 17 | 33 | nan | nan | nan | Cerrado | 1.8 |
| 1f6a5b06-4df9-3c25-a385-4381e58ce4e2 | -5.57276 | -44.97335 | 2025-11-28 04:31:00 | NOAA-21 | BARRA DO CORDA | MARANHÃO | Brasil | 2101608 | 21 | 33 | nan | nan | nan | Cerrado | 3.2 |
| 0de93910-2e34-3cf1-abf9-90de1974e42b | -3.86348 | -47.03256 | 2025-11-28 04:31:00 | NOAA-21 | ITINGA DO MARANHÃO | MARANHÃO | Brasil | 2105427 | 21 | 33 | nan | nan | nan | Amazônia | 2.0 |
| bd4ae4f6-bfa0-3847-99de-47a2aadb257b | -2.61349 | -47.34589 | 2025-11-28 04:31:00 | NOAA-21 | IPIXUNA DO PARÁ | PARÁ | Brasil | 1503457 | 15 | 33 | nan | nan | nan | Amazônia | 2.4 |
| ca84b0de-4944-3b78-a53e-02a8767c7956 | -3.4194 | -50.15751 | 2025-11-28 04:31:00 | NOAA-21 | PACAJÁ | PARÁ | Brasil | 1505486 | 15 | 33 | nan | nan | nan | Amazônia | 1.5 |
| f0089b29-0c9e-3ef5-83f4-79f9a238ea77 | -2.71052 | -48.35184 | 2025-11-28 04:31:00 | NOAA-21 | TOMÉ-AÇU | PARÁ | Brasil | 1508001 | 15 | 33 | nan | nan | nan | Amazônia | 1.1 |
| 4004fd52-78cc-37a5-9eb4-2cba259625d5 | -2.85553 | -49.50357 | 2025-11-28 04:31:00 | NOAA-21 | BAIÃO | PARÁ | Brasil | 1501204 | 15 | 33 | nan | nan | nan | Amazônia | 0.9 |
| 4fbb4998-b2cf-35dd-8a62-38cf56fda5f1 | -3.25165 | -50.02325 | 2025-11-28 04:31:00 | NOAA-21 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 1.5 |
| ddd4ed0d-87ea-393b-af76-97f6ba8e7e67 | -2.15954 | -50.62503 | 2025-11-28 04:31:00 | NOAA-21 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 1.2 |
| a1f5a222-2371-3ef8-a98a-e94aca347769 | -2.74441 | -54.59491 | 2025-11-28 04:31:00 | NOAA-21 | MOJUÍ DOS CAMPOS | PARÁ | Brasil | 1504752 | 15 | 33 | nan | nan | nan | Amazônia | 1.2 |
| 847a771b-5bc3-33d6-9924-0d81054299c7 | -3.39264 | -47.19394 | 2025-11-28 04:31:00 | NOAA-21 | PARAGOMINAS | PARÁ | Brasil | 1505502 | 15 | 33 | nan | nan | nan | Amazônia | 1.5 |
| d3bbaf0f-9d82-3339-97e2-1464b4bf8b0f | -3.85257 | -47.05906 | 2025-11-28 04:31:00 | NOAA-21 | ITINGA DO MARANHÃO | MARANHÃO | Brasil | 2105427 | 21 | 33 | nan | nan | nan | Amazônia | 1.5 |
| 485672a7-f081-3177-9752-fffdcbf5074e | -3.71785 | -50.45092 | 2025-11-28 04:31:00 | NOAA-21 | PACAJÁ | PARÁ | Brasil | 1505486 | 15 | 33 | nan | nan | nan | Amazônia | 1.4 |
| 05d691d4-e117-33d5-928b-e654681cd966 | -4.25919 | -46.24023 | 2025-11-28 04:31:00 | NOAA-21 | ALTO ALEGRE DO PINDARÉ | MARANHÃO | Brasil | 2100477 | 21 | 33 | nan | nan | nan | Amazônia | 2.2 |
| 6ca26f84-e433-3aab-84c3-29f5202c108f | -4.94934 | -41.19082 | 2025-11-28 04:31:00 | NOAA-21 | BURITI DOS MONTES | PIAUÍ | Brasil | 2202026 | 22 | 33 | nan | nan | nan | Caatinga | 3.3 |
| f26e8807-c8ae-3ec9-900d-89b65699c7b1 | -3.34734 | -45.4297 | 2025-11-28 04:31:00 | NOAA-21 | MONÇÃO | MARANHÃO | Brasil | 2106904 | 21 | 33 | nan | nan | nan | Amazônia | 2.3 |
| 2c858b66-f59d-36ed-bd37-dea74c31f7c3 | -3.76161 | -46.96674 | 2025-11-28 04:31:00 | NOAA-21 | CENTRO NOVO DO MARANHÃO | MARANHÃO | Brasil | 2103174 | 21 | 33 | nan | nan | nan | Amazônia | 1.3 |
| f7113d4a-08a3-316c-bfbf-8325c4de4636 | -2.61626 | -47.34985 | 2025-11-28 04:31:00 | NOAA-21 | IPIXUNA DO PARÁ | PARÁ | Brasil | 1503457 | 15 | 33 | nan | nan | nan | Amazônia | 3.0 |
| 338c1ae3-1c2d-33b6-99f9-cdf6fc0493db | -2.27161 | -47.09481 | 2025-11-28 04:31:00 | NOAA-21 | GARRAFÃO DO NORTE | PARÁ | Brasil | 1503077 | 15 | 33 | nan | nan | nan | Amazônia | 0.5 |
| c212e5b5-27e6-3847-b12c-fe092931e13c | -2.42563 | -45.7838 | 2025-11-28 04:31:00 | NOAA-21 | SANTA LUZIA DO PARUÁ | MARANHÃO | Brasil | 2110039 | 21 | 33 | nan | nan | nan | Amazônia | 1.3 |
| e2a2d92c-ae7f-39d8-8c56-275b941e101f | -3.6279 | -53.65193 | 2025-11-28 04:31:00 | NOAA-21 | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | 1.5 |
| 93671fe9-7066-3b2f-8eed-f3fb7ca0ec92 | -2.9648 | -51.02113 | 2025-11-28 04:31:00 | NOAA-21 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 2.0 |
| 08dfe1d9-9b62-3766-a85e-e287ebe01ce5 | -5.5759 | -45.16626 | 2025-11-28 04:31:00 | NOAA-21 | BARRA DO CORDA | MARANHÃO | Brasil | 2101608 | 21 | 33 | nan | nan | nan | Cerrado | 1.8 |
| f5baed6a-1896-331b-9c27-df2f8ba50768 | -3.74562 | -46.96074 | 2025-11-28 04:31:00 | NOAA-21 | CENTRO NOVO DO MARANHÃO | MARANHÃO | Brasil | 2103174 | 21 | 33 | nan | nan | nan | Amazônia | 1.9 |
| c6935dea-15e5-3b07-9345-e75c9d9be264 | -3.03385 | -50.97874 | 2025-11-28 04:31:00 | NOAA-21 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 5.8 |
| c24b6d65-76e8-3bb3-b5ff-37537bc361cd | -2.99365 | -43.84544 | 2025-11-28 04:31:00 | NOAA-21 | MORROS | MARANHÃO | Brasil | 2107100 | 21 | 33 | nan | nan | nan | Cerrado | 0.9 |
| 46efd3af-351f-3755-a501-a51c0b2bb810 | -3.75054 | -46.95094 | 2025-11-28 04:31:00 | NOAA-21 | CENTRO NOVO DO MARANHÃO | MARANHÃO | Brasil | 2103174 | 21 | 33 | nan | nan | nan | Amazônia | 0.7 |
| 33002bcc-521e-3c23-b1c2-2651ff55897d | -3.35074 | -45.43023 | 2025-11-28 04:31:00 | NOAA-21 | MONÇÃO | MARANHÃO | Brasil | 2106904 | 21 | 33 | nan | nan | nan | Amazônia | 2.0 |
| fb6ec93f-32ec-3dc1-957b-04154806d6ee | -3.22368 | -50.79502 | 2025-11-28 04:31:00 | NOAA-21 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 1.3 |
| 50571437-164f-3f68-bc29-3664d292d8e1 | -1.54352 | -46.26972 | 2025-11-28 04:31:00 | NOAA-21 | VISEU | PARÁ | Brasil | 1508308 | 15 | 33 | nan | nan | nan | Amazônia | 0.6 |
| 046f4f4d-cfee-3f4a-a233-d85d308f0779 | -2.80953 | -46.76788 | 2025-11-28 04:31:00 | NOAA-21 | PARAGOMINAS | PARÁ | Brasil | 1505502 | 15 | 33 | nan | nan | nan | Amazônia | 0.7 |
| 57518024-697f-30e5-9acf-6c9f57d23f3d | -3.35021 | -54.09221 | 2025-11-28 04:31:00 | NOAA-21 | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | 2.5 |
| 7fd5cce7-77ee-36e2-a05d-3f1033c57e75 | -3.3859 | -50.25299 | 2025-11-28 04:31:00 | NOAA-21 | PACAJÁ | PARÁ | Brasil | 1505486 | 15 | 33 | nan | nan | nan | Amazônia | 2.0 |
| 3a0543b1-e3f4-34b5-8841-f78ef1d4dcc1 | -2.6168 | -47.34641 | 2025-11-28 04:31:00 | NOAA-21 | IPIXUNA DO PARÁ | PARÁ | Brasil | 1503457 | 15 | 33 | nan | nan | nan | Amazônia | 1.4 |
| ce273443-6542-362d-9d48-99839d170254 | -2.43056 | -45.75204 | 2025-11-28 04:31:00 | NOAA-21 | SANTA LUZIA DO PARUÁ | MARANHÃO | Brasil | 2110039 | 21 | 33 | nan | nan | nan | Amazônia | 1.1 |
| 9277fd64-910b-39a4-af25-70cc56091aab | -3.27678 | -53.75845 | 2025-11-28 04:31:00 | NOAA-21 | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | 1.1 |


[Clique aqui para ver as próximas entradas](README14.md)
