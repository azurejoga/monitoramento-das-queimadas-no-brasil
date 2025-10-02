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

## Dados Diários - Página 59

| ID | Latitude | Longitude | Data/Hora GMT | Satélite | Município | Estado | País | Município ID | Estado ID | País ID | Dias sem Chuva | Precipitação | Risco de Fogo | Bioma | FRP |
|----|----------|-----------|---------------|----------|-----------|--------|------|--------------|-----------|---------|----------------|--------------|----------------|-------|-----|
| 64441e0a-0fc2-3b01-96bf-de55051dd9b9 | -5.71249 | -45.51017 | 2025-10-02 04:27:00 | NPP-375D | BARRA DO CORDA | MARANHÃO | Brasil | 2101608 | 21 | 33 | nan | nan | nan | Cerrado | 0.9 |
| 387ae8e4-f5bd-3bfb-ba98-0d054ae8fa4d | -4.11046 | -47.93311 | 2025-10-02 04:27:00 | NPP-375D | DOM ELISEU | PARÁ | Brasil | 1502939 | 15 | 33 | nan | nan | nan | Amazônia | 2.5 |
| 1f04fd5e-daad-3b14-8b66-7026dbed71d8 | -4.62985 | -49.36975 | 2025-10-02 04:27:00 | NPP-375D | JACUNDÁ | PARÁ | Brasil | 1503804 | 15 | 33 | nan | nan | nan | Amazônia | 2.0 |
| 60d706d0-3123-3a41-ad55-0ac903ecc723 | -4.1495 | -41.52032 | 2025-10-02 04:27:00 | NPP-375D | BRASILEIRA | PIAUÍ | Brasil | 2201960 | 22 | 33 | nan | nan | nan | Caatinga | 1.1 |
| 8a2f05f6-42e6-396a-a8c0-53df861360bd | -3.41376 | -48.88388 | 2025-10-02 04:27:00 | NPP-375D | IPIXUNA DO PARÁ | PARÁ | Brasil | 1503457 | 15 | 33 | nan | nan | nan | Amazônia | 0.8 |
| 65b8a590-8b9a-3557-8f1a-765980ab7d11 | -3.17018 | -42.95885 | 2025-10-02 04:27:00 | NPP-375D | SANTA QUITÉRIA DO MARANHÃO | MARANHÃO | Brasil | 2110104 | 21 | 33 | nan | nan | nan | Cerrado | 1.7 |
| 51105370-e017-34cf-bcd2-125df4d3ffa5 | -4.05373 | -49.07789 | 2025-10-02 04:27:00 | NPP-375D | BREU BRANCO | PARÁ | Brasil | 1501782 | 15 | 33 | nan | nan | nan | Amazônia | 2.0 |
| 4772f575-7253-31af-bc2e-b0faf3c3c56a | -5.75452 | -42.92987 | 2025-10-02 04:27:00 | NPP-375D | PALMEIRAIS | PIAUÍ | Brasil | 2207504 | 22 | 33 | nan | nan | nan | Caatinga | 5.5 |
| 92037338-5147-3b35-9491-1557c1b4f519 | -5.24396 | -44.46166 | 2025-10-02 04:27:00 | NPP-375D | PRESIDENTE DUTRA | MARANHÃO | Brasil | 2109106 | 21 | 33 | nan | nan | nan | Cerrado | 8.4 |
| c916c2b8-53f2-3c3f-846d-dac39337d097 | -5.98908 | -44.60403 | 2025-10-02 04:27:00 | NPP-375D | TUNTUM | MARANHÃO | Brasil | 2112308 | 21 | 33 | nan | nan | nan | Cerrado | 3.4 |
| 07bf6574-6d3e-36b8-8856-644316b93971 | -3.6986 | -49.56997 | 2025-10-02 04:27:00 | NPP-375D | BREU BRANCO | PARÁ | Brasil | 1501782 | 15 | 33 | nan | nan | nan | Amazônia | 7.5 |
| 7c59d817-6942-31f5-b282-53951ebd31c8 | -5.485 | -42.76665 | 2025-10-02 04:27:00 | NPP-375D | TERESINA | PIAUÍ | Brasil | 2211001 | 22 | 33 | nan | nan | nan | Caatinga | 4.0 |
| 157f3f61-acb2-3366-98d1-1ce78f5a102d | -4.25854 | -48.5527 | 2025-10-02 04:27:00 | NPP-375D | RONDON DO PARÁ | PARÁ | Brasil | 1506187 | 15 | 33 | nan | nan | nan | Amazônia | 1.3 |
| 5880f117-2959-3f92-b321-6be64e2edee1 | -3.46182 | -50.09537 | 2025-10-02 04:27:00 | NPP-375D | PACAJÁ | PARÁ | Brasil | 1505486 | 15 | 33 | nan | nan | nan | Amazônia | 3.5 |
| d827b4a8-27c0-3de9-b0ac-6e1ef223fda4 | -4.26564 | -48.5539 | 2025-10-02 04:27:00 | NPP-375D | RONDON DO PARÁ | PARÁ | Brasil | 1506187 | 15 | 33 | nan | nan | nan | Amazônia | 0.9 |
| 63c89144-b091-3d24-937d-5c12a2ae4505 | -5.23517 | -46.22522 | 2025-10-02 04:27:00 | NPP-375D | ARAME | MARANHÃO | Brasil | 2100956 | 21 | 33 | nan | nan | nan | Amazônia | 0.9 |
| ac1d2df5-fd8a-3e9a-85dd-50c83b30932f | -5.32268 | -43.76627 | 2025-10-02 04:27:00 | NPP-375D | PARNARAMA | MARANHÃO | Brasil | 2107803 | 21 | 33 | nan | nan | nan | Cerrado | 5.2 |
| b32b4b91-b05e-31c9-862a-9bd04dae64a5 | -4.40663 | -50.84113 | 2025-10-02 04:27:00 | NPP-375D | NOVO REPARTIMENTO | PARÁ | Brasil | 1505064 | 15 | 33 | nan | nan | nan | Amazônia | 1.0 |
| a79fb7f8-8aeb-3551-9c1f-94a6e2bd9823 | -3.6544 | -51.22789 | 2025-10-02 04:27:00 | NPP-375D | ANAPU | PARÁ | Brasil | 1500859 | 15 | 33 | nan | nan | nan | Amazônia | 1.5 |
| 51d0b454-dee5-3cbd-ab96-05d45e8dc0ce | -5.1924 | -45.39708 | 2025-10-02 04:27:00 | NPP-375D | JENIPAPO DOS VIEIRAS | MARANHÃO | Brasil | 2105476 | 21 | 33 | nan | nan | nan | Cerrado | 3.6 |
| cfd7be49-2e13-38e3-9b52-1556c551a921 | -4.20863 | -48.70149 | 2025-10-02 04:27:00 | NPP-375D | RONDON DO PARÁ | PARÁ | Brasil | 1506187 | 15 | 33 | nan | nan | nan | Amazônia | 0.6 |
| a6fa1193-3b3c-30ba-8efa-32d54e0a94fb | -0.90324 | -47.54971 | 2025-10-02 04:27:00 | NPP-375D | MARACANÃ | PARÁ | Brasil | 1504307 | 15 | 33 | nan | nan | nan | Amazônia | 5.6 |
| a94672ea-5046-352d-9f02-113516c71bc0 | -5.45527 | -42.84012 | 2025-10-02 04:27:00 | NPP-375D | NAZÁRIA | PIAUÍ | Brasil | 2206720 | 22 | 33 | nan | nan | nan | Caatinga | 1.3 |
| eba73970-9e9d-3a45-a2ed-93e1b92d9308 | -5.9885 | -44.58522 | 2025-10-02 04:27:00 | NPP-375D | COLINAS | MARANHÃO | Brasil | 2103505 | 21 | 33 | nan | nan | nan | Cerrado | 2.9 |
| 39b6a105-eef6-3232-aa24-aae8c6f2e2ca | -5.23313 | -45.2024 | 2025-10-02 04:27:00 | NPP-375D | BARRA DO CORDA | MARANHÃO | Brasil | 2101608 | 21 | 33 | nan | nan | nan | Cerrado | 2.3 |
| 99a42a53-993a-3bd3-b841-6bfbb53659ef | -4.26209 | -48.5533 | 2025-10-02 04:27:00 | NPP-375D | RONDON DO PARÁ | PARÁ | Brasil | 1506187 | 15 | 33 | nan | nan | nan | Amazônia | 0.9 |
| 1b6cb27c-ec97-39f0-8457-18fac4c39042 | -5.40861 | -41.32641 | 2025-10-02 04:27:00 | NPP-375D | CASTELO DO PIAUÍ | PIAUÍ | Brasil | 2202604 | 22 | 33 | nan | nan | nan | Caatinga | 2.9 |
| 21a9c7a7-8bbb-3b96-aecf-0e726a8d4fc4 | -6.05032 | -42.43675 | 2025-10-02 04:27:00 | NPP-375D | HUGO NAPOLEÃO | PIAUÍ | Brasil | 2204600 | 22 | 33 | nan | nan | nan | Caatinga | 7.4 |
| 3a11e56e-b148-3a83-8326-60d580e6dd7f | -5.41044 | -37.69878 | 2025-10-02 04:27:00 | NPP-375D | APODI | RIO GRANDE DO NORTE | Brasil | 2401008 | 24 | 33 | nan | nan | nan | Caatinga | 0.8 |
| ef5bb309-a4e1-333a-b1da-38874ad7add9 | -6.11313 | -41.79281 | 2025-10-02 04:27:00 | NPP-375D | AROAZES | PIAUÍ | Brasil | 2200905 | 22 | 33 | nan | nan | nan | Caatinga | 7.6 |
| 1d6e9643-2897-318e-a907-4e43b4378661 | -4.52606 | -46.06381 | 2025-10-02 04:27:00 | NPP-375D | SANTA LUZIA | MARANHÃO | Brasil | 2110005 | 21 | 33 | nan | nan | nan | Amazônia | 0.8 |
| 60a990c9-c36e-3073-b371-4a7129504b34 | -0.09664 | -51.27621 | 2025-10-02 04:27:00 | NPP-375D | MAZAGÃO | AMAPÁ | Brasil | 1600402 | 16 | 33 | nan | nan | nan | Amazônia | 1.6 |
| 73984b58-842e-3ff2-9739-94ec01e7fcc7 | -5.97885 | -44.60248 | 2025-10-02 04:27:00 | NPP-375D | TUNTUM | MARANHÃO | Brasil | 2112308 | 21 | 33 | nan | nan | nan | Cerrado | 9.2 |
| 4d871090-7b9a-3db1-9211-f2546a9de918 | -5.7076 | -42.69611 | 2025-10-02 04:27:00 | NPP-375D | MIGUEL LEÃO | PIAUÍ | Brasil | 2206308 | 22 | 33 | nan | nan | nan | Caatinga | 2.4 |
| 427c2f61-ff0d-3878-9992-98dfd2c6da8e | -3.29895 | -50.01411 | 2025-10-02 04:27:00 | NPP-375D | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 0.8 |
| bb6bfaba-a194-3185-bee5-e15dab059e6b | -5.82818 | -42.45515 | 2025-10-02 04:27:00 | NPP-375D | PASSAGEM FRANCA DO PIAUÍ | PIAUÍ | Brasil | 2207751 | 22 | 33 | nan | nan | nan | Caatinga | 1.6 |
| 139b19f6-c56f-30c6-9c44-61ed6d2c84d0 | -0.91272 | -46.66708 | 2025-10-02 04:27:00 | NPP-375D | BRAGANÇA | PARÁ | Brasil | 1501709 | 15 | 33 | nan | nan | nan | Amazônia | 1.5 |
| 77ec5134-aa28-3656-8225-1c9a10e27cf9 | -3.35095 | -43.18906 | 2025-10-02 04:27:00 | NPP-375D | URBANO SANTOS | MARANHÃO | Brasil | 2112605 | 21 | 33 | nan | nan | nan | Cerrado | 2.7 |
| cc00e8a8-05a1-350f-90c3-fcb87c4c4f7c | -5.792 | -44.91079 | 2025-10-02 04:27:00 | NPP-375D | TUNTUM | MARANHÃO | Brasil | 2112308 | 21 | 33 | nan | nan | nan | Cerrado | 1.6 |
| 63cfb0a2-e847-31f1-9295-c1e6d42ed28b | -6.04999 | -42.43882 | 2025-10-02 04:27:00 | NPP-375D | HUGO NAPOLEÃO | PIAUÍ | Brasil | 2204600 | 22 | 33 | nan | nan | nan | Caatinga | 3.4 |
| 8046c9cd-b380-3a0d-adcf-7001bd5e6aa5 | -4.58251 | -48.02114 | 2025-10-02 04:27:00 | NPP-375D | RONDON DO PARÁ | PARÁ | Brasil | 1506187 | 15 | 33 | nan | nan | nan | Amazônia | 0.8 |
| b0993346-6aeb-3b09-bdba-22d4a204335f | -5.79235 | -45.7334 | 2025-10-02 04:27:00 | NPP-375D | GRAJAÚ | MARANHÃO | Brasil | 2104800 | 21 | 33 | nan | nan | nan | Cerrado | 0.9 |
| f0fabfef-9c60-3df5-9e04-f036eb08feb1 | -5.26061 | -42.77414 | 2025-10-02 04:27:00 | NPP-375D | TERESINA | PIAUÍ | Brasil | 2211001 | 22 | 33 | nan | nan | nan | Cerrado | 1.0 |
| 518355d8-68e7-3324-8e71-1afeb04b4923 | -5.94237 | -44.86039 | 2025-10-02 04:27:00 | NPP-375D | FERNANDO FALCÃO | MARANHÃO | Brasil | 2104081 | 21 | 33 | nan | nan | nan | Cerrado | 2.4 |
| f89d42cc-3d17-34c4-ba99-33e96590dad4 | -5.51076 | -45.16211 | 2025-10-02 04:27:00 | NPP-375D | BARRA DO CORDA | MARANHÃO | Brasil | 2101608 | 21 | 33 | nan | nan | nan | Cerrado | 1.9 |
| 92dd1009-13fc-3a1c-85bf-edeee8dbb4ab | -2.9174 | -51.97139 | 2025-10-02 04:27:00 | NPP-375D | VITÓRIA DO XINGU | PARÁ | Brasil | 1508357 | 15 | 33 | nan | nan | nan | Amazônia | 1.6 |
| 02090c94-a0b1-38a6-bf76-58a5e94356c8 | -5.39384 | -37.70554 | 2025-10-02 04:27:00 | NPP-375D | APODI | RIO GRANDE DO NORTE | Brasil | 2401008 | 24 | 33 | nan | nan | nan | Caatinga | 5.1 |
| 7b1a773f-fed6-3f78-85fd-6b017d5e98b8 | -3.82238 | -49.10023 | 2025-10-02 04:27:00 | NPP-375D | GOIANÉSIA DO PARÁ | PARÁ | Brasil | 1503093 | 15 | 33 | nan | nan | nan | Amazônia | 11.5 |
| 967ecd8d-e735-3c50-ac14-601754bad186 | -5.578 | -45.58943 | 2025-10-02 04:27:00 | NPP-375D | JENIPAPO DOS VIEIRAS | MARANHÃO | Brasil | 2105476 | 21 | 33 | nan | nan | nan | Cerrado | 1.2 |
| 070c118e-f5d6-35f0-8fd1-acc152081099 | -6.11203 | -43.12389 | 2025-10-02 04:27:00 | NPP-375D | SÃO FRANCISCO DO MARANHÃO | MARANHÃO | Brasil | 2110906 | 21 | 33 | nan | nan | nan | Caatinga | 2.8 |
| 8367b94a-51e6-333b-a71f-aaea09ac7a53 | -3.37869 | -52.71528 | 2025-10-02 04:27:00 | NPP-375D | MEDICILÂNDIA | PARÁ | Brasil | 1504455 | 15 | 33 | nan | nan | nan | Amazônia | 1.0 |
| ba7f3e76-8966-3af1-bf99-baf47a06547c | -3.80384 | -51.3172 | 2025-10-02 04:27:00 | NPP-375D | ANAPU | PARÁ | Brasil | 1500859 | 15 | 33 | nan | nan | nan | Amazônia | 4.4 |
| 46cb5215-2e92-3440-84a6-1fdd541287b4 | -5.41087 | -37.69581 | 2025-10-02 04:27:00 | NPP-375D | APODI | RIO GRANDE DO NORTE | Brasil | 2401008 | 24 | 33 | nan | nan | nan | Caatinga | 0.8 |
| dcd51653-7321-3f9f-ae56-4a26fdf60be5 | -1.981 | -47.9828 | 2025-10-02 04:27:00 | NPP-375D | CONCÓRDIA DO PARÁ | PARÁ | Brasil | 1502756 | 15 | 33 | nan | nan | nan | Amazônia | 0.9 |
| d05b1d01-edc6-3636-b975-750c660fcb2a | -4.97056 | -43.10759 | 2025-10-02 04:27:00 | NPP-375D | CAXIAS | MARANHÃO | Brasil | 2103000 | 21 | 33 | nan | nan | nan | Cerrado | 2.8 |
| 9efb0a3e-575e-3384-9160-23face4d8c15 | -3.80874 | -48.95582 | 2025-10-02 04:27:00 | NPP-375D | GOIANÉSIA DO PARÁ | PARÁ | Brasil | 1503093 | 15 | 33 | nan | nan | nan | Amazônia | 0.7 |
| 77630d4a-8b5a-3ad6-9bfc-154694a706a6 | -5.19054 | -45.06983 | 2025-10-02 04:27:00 | NPP-375D | BARRA DO CORDA | MARANHÃO | Brasil | 2101608 | 21 | 33 | nan | nan | nan | Cerrado | 9.6 |
| 68aa9873-0fd8-3d38-90a2-23b8ba486fb0 | -4.52552 | -46.06726 | 2025-10-02 04:27:00 | NPP-375D | SANTA LUZIA | MARANHÃO | Brasil | 2110005 | 21 | 33 | nan | nan | nan | Amazônia | 3.4 |
| 96c1d6e0-2e05-380f-b672-4ef1ca7413a7 | -5.92097 | -44.86439 | 2025-10-02 04:27:00 | NPP-375D | FERNANDO FALCÃO | MARANHÃO | Brasil | 2104081 | 21 | 33 | nan | nan | nan | Cerrado | 3.8 |
| 57fb1a01-01ff-3486-88e7-a7d039f5cd25 | -3.08957 | -47.01144 | 2025-10-02 04:27:00 | NPP-375D | PARAGOMINAS | PARÁ | Brasil | 1505502 | 15 | 33 | nan | nan | nan | Amazônia | 2.0 |
| 8eec6da5-573a-3958-a87f-75ed64e3936a | -3.95226 | -41.59062 | 2025-10-02 04:27:00 | NPP-375D | PIRACURUCA | PIAUÍ | Brasil | 2208304 | 22 | 33 | nan | nan | nan | Caatinga | 2.3 |
| bbf289d4-ccba-3f8b-a036-396e07004b91 | -5.40628 | -41.34195 | 2025-10-02 04:27:00 | NPP-375D | CASTELO DO PIAUÍ | PIAUÍ | Brasil | 2202604 | 22 | 33 | nan | nan | nan | Caatinga | 4.4 |
| 1bf0e434-db4b-3741-a690-4b4a453bbdeb | -3.8999 | -49.08619 | 2025-10-02 04:27:00 | NPP-375D | GOIANÉSIA DO PARÁ | PARÁ | Brasil | 1503093 | 15 | 33 | nan | nan | nan | Amazônia | 2.4 |
| ef94cac6-9055-3ec6-824a-057333058f9d | -4.6479 | -47.95841 | 2025-10-02 04:27:00 | NPP-375D | RONDON DO PARÁ | PARÁ | Brasil | 1506187 | 15 | 33 | nan | nan | nan | Amazônia | 1.3 |
| a9ee316b-dd58-3913-a060-ed4b75dbb1a4 | -5.75517 | -42.92567 | 2025-10-02 04:27:00 | NPP-375D | PALMEIRAIS | PIAUÍ | Brasil | 2207504 | 22 | 33 | nan | nan | nan | Caatinga | 5.5 |
| d00a1243-dd45-3e3b-8058-7f6696cbc9c5 | -5.9249 | -44.86135 | 2025-10-02 04:27:00 | NPP-375D | FERNANDO FALCÃO | MARANHÃO | Brasil | 2104081 | 21 | 33 | nan | nan | nan | Cerrado | 2.2 |
| 44a622ea-e071-371e-88ea-7d997bf1c817 | -5.99647 | -44.57888 | 2025-10-02 04:27:00 | NPP-375D | COLINAS | MARANHÃO | Brasil | 2103505 | 21 | 33 | nan | nan | nan | Cerrado | 2.8 |
| 9e2718f5-a2e6-3ece-aee1-b0e5da445508 | -5.48821 | -42.74529 | 2025-10-02 04:27:00 | NPP-375D | LAGOA DO PIAUÍ | PIAUÍ | Brasil | 2205581 | 22 | 33 | nan | nan | nan | Caatinga | 4.4 |
| 264438a9-3bd9-36b9-9577-3cc013a107b6 | -4.48136 | -47.67255 | 2025-10-02 04:27:00 | NPP-375D | DOM ELISEU | PARÁ | Brasil | 1502939 | 15 | 33 | nan | nan | nan | Amazônia | 0.7 |
| 2de2cdb6-197c-3842-9b56-41195a92cb3e | -5.98964 | -44.57786 | 2025-10-02 04:27:00 | NPP-375D | COLINAS | MARANHÃO | Brasil | 2103505 | 21 | 33 | nan | nan | nan | Cerrado | 4.1 |
| 45909553-e347-35f9-be88-87a4d4b3eba0 | -6.10439 | -43.43745 | 2025-10-02 04:27:00 | NPP-375D | LAGOA DO MATO | MARANHÃO | Brasil | 2105922 | 21 | 33 | nan | nan | nan | Cerrado | 3.1 |
| ad693d9d-db81-3315-a7a1-d720ea425034 | -3.46732 | -50.08629 | 2025-10-02 04:27:00 | NPP-375D | PACAJÁ | PARÁ | Brasil | 1505486 | 15 | 33 | nan | nan | nan | Amazônia | 2.5 |
| fd634600-7843-3328-b120-519299d3e4fc | -5.99306 | -44.60089 | 2025-10-02 04:27:00 | NPP-375D | COLINAS | MARANHÃO | Brasil | 2103505 | 21 | 33 | nan | nan | nan | Cerrado | 3.1 |
| e7fb1ed6-772e-3db6-8311-cbe4b958a7ba | -4.14876 | -41.52511 | 2025-10-02 04:27:00 | NPP-375D | BRASILEIRA | PIAUÍ | Brasil | 2201960 | 22 | 33 | nan | nan | nan | Caatinga | 1.9 |
| 0085e47d-6a36-397a-952a-b8c9bf2fe8dc | -5.7169 | -42.68444 | 2025-10-02 04:27:00 | NPP-375D | MIGUEL LEÃO | PIAUÍ | Brasil | 2206308 | 22 | 33 | nan | nan | nan | Caatinga | 2.2 |
| aa810be1-7558-3490-b66b-bf32fa5ef1a4 | -3.35386 | -43.19348 | 2025-10-02 04:27:00 | NPP-375D | URBANO SANTOS | MARANHÃO | Brasil | 2112605 | 21 | 33 | nan | nan | nan | Cerrado | 3.6 |
| cf061b2c-5bf1-377b-8bd3-79b8b21912ac | -3.34625 | -43.19627 | 2025-10-02 04:27:00 | NPP-375D | URBANO SANTOS | MARANHÃO | Brasil | 2112605 | 21 | 33 | nan | nan | nan | Cerrado | 4.7 |
| 0a477839-e6ee-3e8c-95c0-1bd2bedb6957 | -5.99305 | -44.57838 | 2025-10-02 04:27:00 | NPP-375D | COLINAS | MARANHÃO | Brasil | 2103505 | 21 | 33 | nan | nan | nan | Cerrado | 4.1 |
| 55c5957c-a753-3fec-85b1-590448911552 | -5.70089 | -42.69053 | 2025-10-02 04:27:00 | NPP-375D | MIGUEL LEÃO | PIAUÍ | Brasil | 2206308 | 22 | 33 | nan | nan | nan | Caatinga | 2.8 |
| 31926ce7-2259-376d-bc33-845230ae3df5 | -3.51981 | -44.04005 | 2025-10-02 04:27:00 | NPP-375D | VARGEM GRANDE | MARANHÃO | Brasil | 2112704 | 21 | 33 | nan | nan | nan | Cerrado | 0.8 |
| 87cc160a-21b9-3bc6-b5b4-aae48d4d2a3b | -6.10088 | -42.48365 | 2025-10-02 04:27:00 | NPP-375D | HUGO NAPOLEÃO | PIAUÍ | Brasil | 2204600 | 22 | 33 | nan | nan | nan | Caatinga | 1.2 |
| 613e6a7a-4ff1-3358-9651-96b301c863db | -6.04211 | -42.44012 | 2025-10-02 04:27:00 | NPP-375D | HUGO NAPOLEÃO | PIAUÍ | Brasil | 2204600 | 22 | 33 | nan | nan | nan | Caatinga | 2.7 |
| 9362bde7-4f53-3d2a-9d21-5203f7d18aa2 | -3.49334 | -50.27334 | 2025-10-02 04:27:00 | NPP-375D | PACAJÁ | PARÁ | Brasil | 1505486 | 15 | 33 | nan | nan | nan | Amazônia | 1.8 |
| 4b2acbe3-250d-32b7-81c5-0c8cbf933ad6 | -3.68553 | -49.05116 | 2025-10-02 04:27:00 | NPP-375D | GOIANÉSIA DO PARÁ | PARÁ | Brasil | 1503093 | 15 | 33 | nan | nan | nan | Amazônia | 1.7 |
| 19660047-e6be-3c5b-8603-55de7f8cbc23 | -5.79295 | -45.75134 | 2025-10-02 04:27:00 | NPP-375D | GRAJAÚ | MARANHÃO | Brasil | 2104800 | 21 | 33 | nan | nan | nan | Cerrado | 1.4 |
| dc8b009e-7a59-3c83-9307-9a9240e9de61 | -5.19295 | -45.39359 | 2025-10-02 04:27:00 | NPP-375D | JENIPAPO DOS VIEIRAS | MARANHÃO | Brasil | 2105476 | 21 | 33 | nan | nan | nan | Cerrado | 3.7 |
| 6ff10d72-dc10-39bb-b71b-e0c78826845f | -5.97998 | -44.59517 | 2025-10-02 04:27:00 | NPP-375D | COLINAS | MARANHÃO | Brasil | 2103505 | 21 | 33 | nan | nan | nan | Cerrado | 2.1 |
| 71ea3f5a-c4ff-38f2-a6e0-abb6aa323335 | -5.73006 | -45.4197 | 2025-10-02 04:27:00 | NPP-375D | BARRA DO CORDA | MARANHÃO | Brasil | 2101608 | 21 | 33 | nan | nan | nan | Cerrado | 1.6 |
| 8db0c638-2508-373c-9d55-ef6ff771c5fc | -4.15033 | -41.52322 | 2025-10-02 04:27:00 | NPP-375D | BRASILEIRA | PIAUÍ | Brasil | 2201960 | 22 | 33 | nan | nan | nan | Caatinga | 2.0 |
| adba4693-7bf9-3b24-ac58-510971126054 | -3.7802 | -48.62899 | 2025-10-02 04:27:00 | NPP-375D | GOIANÉSIA DO PARÁ | PARÁ | Brasil | 1503093 | 15 | 33 | nan | nan | nan | Amazônia | 1.2 |
| aaca6d9a-aedd-3871-8673-63fecf7fb79c | -5.27714 | -42.76365 | 2025-10-02 04:27:00 | NPP-375D | TERESINA | PIAUÍ | Brasil | 2211001 | 22 | 33 | nan | nan | nan | Cerrado | 1.3 |
| 163b6f3f-c816-32dd-a5c1-cf7cd783c815 | -5.41339 | -41.3217 | 2025-10-02 04:27:00 | NPP-375D | CASTELO DO PIAUÍ | PIAUÍ | Brasil | 2202604 | 22 | 33 | nan | nan | nan | Caatinga | 3.6 |
| 4c646023-190f-37e1-bdb8-dcc74a0dc387 | -5.78907 | -45.75431 | 2025-10-02 04:27:00 | NPP-375D | GRAJAÚ | MARANHÃO | Brasil | 2104800 | 21 | 33 | nan | nan | nan | Cerrado | 1.0 |
| 07656856-1c87-3f23-b5f5-3a46b7088837 | -3.52038 | -44.0364 | 2025-10-02 04:27:00 | NPP-375D | VARGEM GRANDE | MARANHÃO | Brasil | 2112704 | 21 | 33 | nan | nan | nan | Cerrado | 2.0 |
| 0f561bdc-0e12-33e7-8c7d-faf61d51b1c7 | -5.14676 | -46.41743 | 2025-10-02 04:27:00 | NPP-375D | AMARANTE DO MARANHÃO | MARANHÃO | Brasil | 2100600 | 21 | 33 | nan | nan | nan | Amazônia | 1.0 |
| cea21b8d-78de-3ce1-8db7-27b16948f679 | -2.96338 | -48.60043 | 2025-10-02 04:27:00 | NPP-375D | TAILÂNDIA | PARÁ | Brasil | 1507953 | 15 | 33 | nan | nan | nan | Amazônia | 1.4 |
| f40751aa-0177-39fa-8c8e-8d8c3fb04f89 | -5.70696 | -42.70039 | 2025-10-02 04:27:00 | NPP-375D | MIGUEL LEÃO | PIAUÍ | Brasil | 2206308 | 22 | 33 | nan | nan | nan | Caatinga | 4.2 |
| a08bce7b-4637-3841-bcdf-73c99f3d0462 | -3.68621 | -49.04689 | 2025-10-02 04:27:00 | NPP-375D | GOIANÉSIA DO PARÁ | PARÁ | Brasil | 1503093 | 15 | 33 | nan | nan | nan | Amazônia | 1.7 |
| 0658c272-6aa4-3bff-9231-c167210aa6d2 | -5.82182 | -42.85192 | 2025-10-02 04:27:00 | NPP-375D | SÃO PEDRO DO PIAUÍ | PIAUÍ | Brasil | 2210508 | 22 | 33 | nan | nan | nan | Caatinga | 2.8 |
| f6acfdf8-f9bb-31d5-b22d-503d04869365 | -5.98907 | -44.58154 | 2025-10-02 04:27:00 | NPP-375D | COLINAS | MARANHÃO | Brasil | 2103505 | 21 | 33 | nan | nan | nan | Cerrado | 4.1 |


[Clique aqui para ver as próximas entradas](README60.md)
