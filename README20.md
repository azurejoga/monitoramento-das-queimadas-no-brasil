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

## Dados Diários - Página 20

| ID | Latitude | Longitude | Data/Hora GMT | Satélite | Município | Estado | País | Município ID | Estado ID | País ID | Dias sem Chuva | Precipitação | Risco de Fogo | Bioma | FRP |
|----|----------|-----------|---------------|----------|-----------|--------|------|--------------|-----------|---------|----------------|--------------|----------------|-------|-----|
| 366152db-e40c-3e41-8725-e94cc1cbc054 | -11.32364 | -51.43662 | 2025-07-12 12:49:00 | TERRA_M-T | SÃO FÉLIX DO ARAGUAIA | MATO GROSSO | Brasil | 5107859 | 51 | 33 | nan | nan | nan | Cerrado | 25.1 |
| 9a881651-9ea2-32c4-ad0d-f77d7af2137a | -10.57305 | -49.13462 | 2025-07-12 12:49:00 | TERRA_M-T | CRISTALÂNDIA | TOCANTINS | Brasil | 1706100 | 17 | 33 | nan | nan | nan | Cerrado | 14.2 |
| 47580033-d39a-3797-a22c-ced3587c2d3e | -13.01542 | -57.99864 | 2025-07-12 12:49:00 | TERRA_M-T | BRASNORTE | MATO GROSSO | Brasil | 5101902 | 51 | 33 | nan | nan | nan | Cerrado | 12.1 |
| 01903bc0-18c7-34c4-bd31-974d59885f3d | -11.84312 | -47.49673 | 2025-07-12 12:49:00 | TERRA_M-T | NATIVIDADE | TOCANTINS | Brasil | 1714203 | 17 | 33 | nan | nan | nan | Cerrado | 31.7 |
| ec23b83d-a5a4-3e3a-92e1-5918e6abaf04 | -10.35976 | -49.91683 | 2025-07-12 12:49:00 | TERRA_M-T | PIUM | TOCANTINS | Brasil | 1717503 | 17 | 33 | nan | nan | nan | Cerrado | 17.8 |
| 5f1ec1ef-7270-3517-9a53-821a5758d3d9 | -11.27734 | -50.41204 | 2025-07-12 12:49:00 | TERRA_M-T | LAGOA DA CONFUSÃO | TOCANTINS | Brasil | 1711902 | 17 | 33 | nan | nan | nan | Cerrado | 16.9 |
| bc1780cc-8d6d-3e0a-9c29-b6c9dd3a9216 | -6.11413 | -45.94858 | 2025-07-12 12:49:00 | TERRA_M-T | GRAJAÚ | MARANHÃO | Brasil | 2104800 | 21 | 33 | nan | nan | nan | Cerrado | 22.9 |
| fa714eb2-543b-30e1-bc12-6d74107030f7 | -8.47047 | -49.62009 | 2025-07-12 12:49:00 | TERRA_M-T | CONCEIÇÃO DO ARAGUAIA | PARÁ | Brasil | 1502707 | 15 | 33 | nan | nan | nan | Amazônia | 12.6 |
| a410fe64-8463-35ba-82fc-6b3f96a5ac9f | -5.78473 | -43.62616 | 2025-07-12 12:49:00 | TERRA_M-T | LAGOA DO MATO | MARANHÃO | Brasil | 2105922 | 21 | 33 | nan | nan | nan | Cerrado | 36.6 |
| b392e631-0316-30df-b63e-971b3a4cf334 | -6.42887 | -45.36223 | 2025-07-12 12:49:00 | TERRA_M-T | MIRADOR | MARANHÃO | Brasil | 2106706 | 21 | 33 | nan | nan | nan | Cerrado | 52.8 |
| 582d15c2-0d9e-3d81-9b9a-6697124a4b74 | -6.12052 | -45.94258 | 2025-07-12 12:49:00 | TERRA_M-T | GRAJAÚ | MARANHÃO | Brasil | 2104800 | 21 | 33 | nan | nan | nan | Cerrado | 38.2 |
| 4da0ac55-86f5-36ed-9ef1-7a292f9aa815 | -14.68481 | -52.69379 | 2025-07-12 12:49:00 | TERRA_M-T | NOVA XAVANTINA | MATO GROSSO | Brasil | 5106257 | 51 | 33 | nan | nan | nan | Cerrado | 7.2 |
| 56c14692-dc97-3ef4-bc99-ca5a249d34a5 | -7.08288 | -49.61367 | 2025-07-12 12:49:00 | TERRA_M-T | XINGUARA | PARÁ | Brasil | 1508407 | 15 | 33 | nan | nan | nan | Amazônia | 8.8 |
| 086d02ae-6d9f-3048-8471-2d60b06a9dfc | -8.32128 | -44.92902 | 2025-07-12 12:49:00 | TERRA_M-T | BAIXA GRANDE DO RIBEIRO | PIAUÍ | Brasil | 2201150 | 22 | 33 | nan | nan | nan | Cerrado | 43.4 |
| 066186d2-d461-32e6-88fa-6aa3f9a46f02 | -8.34012 | -45.62038 | 2025-07-12 12:49:00 | TERRA_M-T | RIBEIRO GONÇALVES | PIAUÍ | Brasil | 2208908 | 22 | 33 | nan | nan | nan | Cerrado | 25.3 |
| 5ab8d3b8-931e-38b9-9cf5-7d540df7e096 | -8.31353 | -55.09798 | 2025-07-12 12:49:00 | TERRA_M-T | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 5.9 |
| 6cf0afec-4d68-3289-aba6-681b04c986f0 | -7.61305 | -49.93093 | 2025-07-12 12:49:00 | TERRA_M-T | RIO MARIA | PARÁ | Brasil | 1506161 | 15 | 33 | nan | nan | nan | Amazônia | 17.1 |
| f302d51a-1561-351b-b646-4d43e55adc7f | -7.85744 | -50.60825 | 2025-07-12 12:49:00 | TERRA_M-T | CUMARU DO NORTE | PARÁ | Brasil | 1502764 | 15 | 33 | nan | nan | nan | Amazônia | 14.2 |
| 0ab00571-8f28-3cde-a3c7-9bfa9713fc5f | -11.57072 | -44.80864 | 2025-07-12 12:49:00 | TERRA_M-T | RIACHÃO DAS NEVES | BAHIA | Brasil | 2926202 | 29 | 33 | nan | nan | nan | Cerrado | 48.5 |
| 39a8d0fa-818f-31e9-8f72-552453e08e72 | -11.56686 | -44.84319 | 2025-07-12 12:49:00 | TERRA_M-T | RIACHÃO DAS NEVES | BAHIA | Brasil | 2926202 | 29 | 33 | nan | nan | nan | Cerrado | 114.7 |
| 9b11aab9-5e1f-336d-abdc-4ea82775e057 | -13.65778 | -53.93876 | 2025-07-12 12:49:00 | TERRA_M-T | GAÚCHA DO NORTE | MATO GROSSO | Brasil | 5103858 | 51 | 33 | nan | nan | nan | Cerrado | 11.6 |
| 1a9ab97c-7ec7-3e7b-88df-1f8bea8d0308 | -10.35333 | -49.92289 | 2025-07-12 12:49:00 | TERRA_M-T | PIUM | TOCANTINS | Brasil | 1717503 | 17 | 33 | nan | nan | nan | Cerrado | 31.3 |
| d1eec7b4-6f09-3127-8ca6-48ea0bbe8505 | -8.92837 | -47.33441 | 2025-07-12 12:49:00 | TERRA_M-T | CENTENÁRIO | TOCANTINS | Brasil | 1704105 | 17 | 33 | nan | nan | nan | Cerrado | 82.0 |
| dc34194d-8c1d-3e36-a8db-48be27a6258f | -11.84597 | -47.49139 | 2025-07-12 12:49:00 | TERRA_M-T | ALMAS | TOCANTINS | Brasil | 1700400 | 17 | 33 | nan | nan | nan | Cerrado | 14.3 |
| 800101ff-86ba-39a7-a3eb-ae2c3a25eff3 | -11.27901 | -50.39948 | 2025-07-12 12:49:00 | TERRA_M-T | LAGOA DA CONFUSÃO | TOCANTINS | Brasil | 1711902 | 17 | 33 | nan | nan | nan | Cerrado | 7.1 |
| 5d6b9e76-e271-310c-9dab-8044727e293e | -8.9213 | -47.3374 | 2025-07-12 12:50:00 | GOES-19 | CENTENÁRIO | TOCANTINS | Brasil | 1704105 | 17 | 33 | nan | nan | nan | Cerrado | 98.9 |
| 9f7ab3ce-2d4a-3beb-a12e-f557d8148b49 | -12.4669 | -44.4959 | 2025-07-12 12:50:00 | GOES-19 | BAIANÓPOLIS | BAHIA | Brasil | 2902500 | 29 | 33 | nan | nan | nan | Cerrado | 93.4 |
| 7c1f2e2e-9ca4-36de-ba2e-12cf7f9b0c3d | -6.485 | -45.2554 | 2025-07-12 12:50:00 | GOES-19 | MIRADOR | MARANHÃO | Brasil | 2106706 | 21 | 33 | nan | nan | nan | Cerrado | 266.1 |
| 2b23060a-6632-3e28-bc0b-fb87513b0595 | -21.30034 | -56.85911 | 2025-07-12 12:51:00 | TERRA_M-T | PORTO MURTINHO | MATO GROSSO DO SUL | Brasil | 5006903 | 50 | 33 | nan | nan | nan | Cerrado | 6.7 |
| 495b3a7b-b3ce-3097-918f-830901a24c53 | -20.71047 | -56.66175 | 2025-07-12 12:51:00 | TERRA_M-T | BODOQUENA | MATO GROSSO DO SUL | Brasil | 5002159 | 50 | 33 | nan | nan | nan | Cerrado | 4.7 |
| fa6b9f68-4de0-397e-a644-1395961012ab | -16.05835 | -53.70672 | 2025-07-12 12:51:00 | TERRA_M-T | TESOURO | MATO GROSSO | Brasil | 5108105 | 51 | 33 | nan | nan | nan | Cerrado | 7.0 |
| ee0e66aa-cc58-37e6-bffb-1ef474fbe02c | -21.70437 | -57.67572 | 2025-07-12 12:51:00 | TERRA_M-T | PORTO MURTINHO | MATO GROSSO DO SUL | Brasil | 5006903 | 50 | 33 | nan | nan | nan | Cerrado | 6.5 |
| c7969fef-6d97-3d92-b0dc-cbc0be0b4bb5 | -16.97639 | -46.13124 | 2025-07-12 12:51:00 | TERRA_M-T | BRASILÂNDIA DE MINAS | MINAS GERAIS | Brasil | 3108552 | 31 | 33 | nan | nan | nan | Cerrado | 25.5 |
| 51f6587a-cead-3f4e-8d24-20d09cd110f0 | -17.6761 | -52.90603 | 2025-07-12 12:51:00 | TERRA_M-T | MINEIROS | GOIÁS | Brasil | 5213103 | 52 | 33 | nan | nan | nan | Cerrado | 8.9 |
| d0d1336f-ae6b-31ce-81e4-a2de3021e50b | -17.67921 | -52.91293 | 2025-07-12 12:51:00 | TERRA_M-T | MINEIROS | GOIÁS | Brasil | 5213103 | 52 | 33 | nan | nan | nan | Cerrado | 5.5 |
| fc4dac0f-cddf-3b26-8be7-531ba9380e8f | -20.55426 | -54.12968 | 2025-07-12 12:51:00 | TERRA_M-T | RIBAS DO RIO PARDO | MATO GROSSO DO SUL | Brasil | 5007109 | 50 | 33 | nan | nan | nan | Cerrado | 15.8 |
| ff2139b2-8049-358c-8757-50b359a9a35b | -20.55561 | -54.11925 | 2025-07-12 12:51:00 | TERRA_M-T | RIBAS DO RIO PARDO | MATO GROSSO DO SUL | Brasil | 5007109 | 50 | 33 | nan | nan | nan | Cerrado | 13.5 |
| fba3a11b-3e0e-3f6f-8c93-fb40c7c86474 | -21.70752 | -56.1417 | 2025-07-12 12:51:00 | TERRA_M-T | JARDIM | MATO GROSSO DO SUL | Brasil | 5005004 | 50 | 33 | nan | nan | nan | Cerrado | 4.5 |
| 2a4aae17-ff2c-388e-8c4d-2f15c5bf27dd | -21.30174 | -56.84963 | 2025-07-12 12:51:00 | TERRA_M-T | PORTO MURTINHO | MATO GROSSO DO SUL | Brasil | 5006903 | 50 | 33 | nan | nan | nan | Cerrado | 5.5 |
| 0adecc93-3849-3f0e-83e6-4d4fa1756b5e | -16.05702 | -53.71641 | 2025-07-12 12:51:00 | TERRA_M-T | TESOURO | MATO GROSSO | Brasil | 5108105 | 51 | 33 | nan | nan | nan | Cerrado | 6.8 |
| 80b3503d-3efd-37bf-8e63-7a42b2381258 | -21.70583 | -57.66595 | 2025-07-12 12:51:00 | TERRA_M-T | PORTO MURTINHO | MATO GROSSO DO SUL | Brasil | 5006903 | 50 | 33 | nan | nan | nan | Cerrado | 8.3 |
| 4c3edac8-c18f-392c-ae6d-202002e56af4 | -21.69867 | -56.14029 | 2025-07-12 12:51:00 | TERRA_M-T | JARDIM | MATO GROSSO DO SUL | Brasil | 5005004 | 50 | 33 | nan | nan | nan | Cerrado | 4.6 |
| 39490edb-ca67-31a2-9490-96c2eaa04508 | -15.69 | -53.63959 | 2025-07-12 12:51:00 | TERRA_M-T | GENERAL CARNEIRO | MATO GROSSO | Brasil | 5103908 | 51 | 33 | nan | nan | nan | Cerrado | 4.5 |
| 5aed7576-28e5-3abe-babb-4558e725c9de | -23.68382 | -50.69614 | 2025-07-12 12:53:00 | TERRA_M-T | SÃO JERÔNIMO DA SERRA | PARANÁ | Brasil | 4124707 | 41 | 33 | nan | nan | nan | Mata Atlântica | 13.3 |
| 2f4e76ee-3aad-3a12-828a-5fb3ada9b044 | -23.68581 | -50.67715 | 2025-07-12 12:53:00 | TERRA_M-T | SÃO JERÔNIMO DA SERRA | PARANÁ | Brasil | 4124707 | 41 | 33 | nan | nan | nan | Mata Atlântica | 11.9 |
| 041473a8-7c26-39bb-96a7-84d99367ee0f | -23.68938 | -50.68312 | 2025-07-12 12:53:00 | TERRA_M-T | SÃO JERÔNIMO DA SERRA | PARANÁ | Brasil | 4124707 | 41 | 33 | nan | nan | nan | Mata Atlântica | 16.8 |
| c03e602a-f013-33de-af7a-8915842fda99 | -12.4862 | -44.4928 | 2025-07-12 13:00:00 | GOES-19 | BAIANÓPOLIS | BAHIA | Brasil | 2902500 | 29 | 33 | nan | nan | nan | Cerrado | 89.4 |
| 8b9ad23d-fd7c-3710-915b-3f3069acead9 | -8.9213 | -47.3374 | 2025-07-12 13:00:00 | GOES-19 | CENTENÁRIO | TOCANTINS | Brasil | 1704105 | 17 | 33 | nan | nan | nan | Cerrado | 84.6 |
| 944d7a1c-8016-3073-a5ca-8a6e0c4118d6 | -5.9748 | -43.7613 | 2025-07-12 13:00:00 | GOES-19 | BURITI BRAVO | MARANHÃO | Brasil | 2102309 | 21 | 33 | nan | nan | nan | Cerrado | 74.3 |
| 875a6a99-7fb4-350d-8cc7-e19276039d41 | -6.485 | -45.2554 | 2025-07-12 13:00:00 | GOES-19 | MIRADOR | MARANHÃO | Brasil | 2106706 | 21 | 33 | nan | nan | nan | Cerrado | 139.2 |
| 1e3ca49d-9ccf-3308-b97c-f6ab2897466a | -12.4669 | -44.4959 | 2025-07-12 13:00:00 | GOES-19 | BAIANÓPOLIS | BAHIA | Brasil | 2902500 | 29 | 33 | nan | nan | nan | Cerrado | 91.3 |
| c5791a67-1b63-3716-8076-9ef3a83e0a96 | -6.1232 | -45.9363 | 2025-07-12 13:00:00 | GOES-19 | GRAJAÚ | MARANHÃO | Brasil | 2104800 | 21 | 33 | nan | nan | nan | Cerrado | 67.6 |
| fd34feed-132a-3dad-a9d0-7d00fec0d838 | -8.921 | -47.3595 | 2025-07-12 13:10:00 | GOES-19 | CENTENÁRIO | TOCANTINS | Brasil | 1704105 | 17 | 33 | nan | nan | nan | Cerrado | 78.6 |
| e4765c0d-a713-3a5c-a6fb-9ec7100d4598 | -12.4862 | -44.4928 | 2025-07-12 13:10:00 | GOES-19 | BAIANÓPOLIS | BAHIA | Brasil | 2902500 | 29 | 33 | nan | nan | nan | Cerrado | 87.0 |
| 76cbe1ef-aad7-3627-9bd9-89538b89575d | -12.4669 | -44.4959 | 2025-07-12 13:10:00 | GOES-19 | BAIANÓPOLIS | BAHIA | Brasil | 2902500 | 29 | 33 | nan | nan | nan | Cerrado | 114.2 |
| 10f3f80e-a623-3e65-8f1f-e1aa43bdae6e | -6.1232 | -45.9363 | 2025-07-12 13:10:00 | GOES-19 | GRAJAÚ | MARANHÃO | Brasil | 2104800 | 21 | 33 | nan | nan | nan | Cerrado | 97.5 |
| 975081a3-548e-3f3d-9c0b-9e1c0153d47e | -8.9213 | -47.3374 | 2025-07-12 13:10:00 | GOES-19 | CENTENÁRIO | TOCANTINS | Brasil | 1704105 | 17 | 33 | nan | nan | nan | Cerrado | 130.3 |
| 9a21e90d-8de4-3428-a0bd-188d70e0df3f | -8.6416 | -64.176 | 2025-07-12 13:20:00 | GOES-19 | CANUTAMA | AMAZONAS | Brasil | 1300904 | 13 | 33 | nan | nan | nan | Amazônia | 64.8 |
| bee27971-ed92-37b1-8099-94c7a21db2b5 | -12.4862 | -44.4928 | 2025-07-12 13:20:00 | GOES-19 | BAIANÓPOLIS | BAHIA | Brasil | 2902500 | 29 | 33 | nan | nan | nan | Cerrado | 104.3 |
| e8b14f5a-e129-3fab-a742-bf869da5d188 | -8.9213 | -47.3374 | 2025-07-12 13:20:00 | GOES-19 | CENTENÁRIO | TOCANTINS | Brasil | 1704105 | 17 | 33 | nan | nan | nan | Cerrado | 99.9 |
| 9a03ce7c-04a5-3fd8-9d75-40120749b89b | -6.1232 | -45.9363 | 2025-07-12 13:20:00 | GOES-19 | GRAJAÚ | MARANHÃO | Brasil | 2104800 | 21 | 33 | nan | nan | nan | Cerrado | 76.2 |
| 19ff8b4c-54a3-30f4-898e-f902db3b28bf | -12.4669 | -44.4959 | 2025-07-12 13:20:00 | GOES-19 | BAIANÓPOLIS | BAHIA | Brasil | 2902500 | 29 | 33 | nan | nan | nan | Cerrado | 108.2 |
| a6d56868-cc61-3835-9baf-e9c425b572e3 | -5.9748 | -43.7613 | 2025-07-12 13:20:00 | GOES-19 | BURITI BRAVO | MARANHÃO | Brasil | 2102309 | 21 | 33 | nan | nan | nan | Cerrado | 77.5 |
| 691868cd-608f-3a76-809c-85fbe2c46b36 | -6.1232 | -45.9363 | 2025-07-12 13:30:00 | GOES-19 | GRAJAÚ | MARANHÃO | Brasil | 2104800 | 21 | 33 | nan | nan | nan | Cerrado | 92.6 |
| 6a537522-fd43-3dca-bf56-3d70483fb7aa | -5.9748 | -43.7613 | 2025-07-12 13:30:00 | GOES-19 | BURITI BRAVO | MARANHÃO | Brasil | 2102309 | 21 | 33 | nan | nan | nan | Cerrado | 77.4 |
| f8a6b20a-6780-3173-bb61-b494a5785c5c | -12.4862 | -44.4928 | 2025-07-12 13:30:00 | GOES-19 | BAIANÓPOLIS | BAHIA | Brasil | 2902500 | 29 | 33 | nan | nan | nan | Cerrado | 119.4 |
| fc648c78-b6d8-3dd7-8928-69ea64ecdf43 | -8.6416 | -64.176 | 2025-07-12 13:30:00 | GOES-19 | CANUTAMA | AMAZONAS | Brasil | 1300904 | 13 | 33 | nan | nan | nan | Amazônia | 67.4 |
| c10d573d-397b-38ec-8b23-1946909a0fff | -12.4669 | -44.4959 | 2025-07-12 13:30:00 | GOES-19 | BAIANÓPOLIS | BAHIA | Brasil | 2902500 | 29 | 33 | nan | nan | nan | Cerrado | 99.6 |
| fa5c7ab5-fc1a-384b-a2f2-714cd8172c0b | -8.9213 | -47.3374 | 2025-07-12 13:30:00 | GOES-19 | CENTENÁRIO | TOCANTINS | Brasil | 1704105 | 17 | 33 | nan | nan | nan | Cerrado | 78.5 |
| 60d850dc-9b00-3f99-8aaf-c1e91d5d350f | -6.1232 | -45.9363 | 2025-07-12 13:40:00 | GOES-19 | GRAJAÚ | MARANHÃO | Brasil | 2104800 | 21 | 33 | nan | nan | nan | Cerrado | 74.7 |
| 3f1206e0-e730-3dd1-8b09-0249e40f045e | -4.2896 | -46.936 | 2025-07-12 13:40:00 | GOES-19 | BOM JARDIM | MARANHÃO | Brasil | 2102002 | 21 | 33 | nan | nan | nan | Amazônia | 69.7 |
| 19583925-af54-3cc8-8900-ee844650c26d | -12.4862 | -44.4928 | 2025-07-12 13:40:00 | GOES-19 | BAIANÓPOLIS | BAHIA | Brasil | 2902500 | 29 | 33 | nan | nan | nan | Cerrado | 155.3 |
| 56cd2660-2e80-3321-819f-80962da2d3e0 | -12.4669 | -44.4959 | 2025-07-12 13:40:00 | GOES-19 | BAIANÓPOLIS | BAHIA | Brasil | 2902500 | 29 | 33 | nan | nan | nan | Cerrado | 115.1 |
| 6086969a-6e12-3456-b15c-f8b6ba364963 | -8.9213 | -47.3374 | 2025-07-12 13:40:00 | GOES-19 | CENTENÁRIO | TOCANTINS | Brasil | 1704105 | 17 | 33 | nan | nan | nan | Cerrado | 91.7 |
| 107d3088-c7ac-36fd-a3fd-8628b30a7b29 | -6.1608 | -45.9111 | 2025-07-12 13:50:00 | GOES-19 | GRAJAÚ | MARANHÃO | Brasil | 2104800 | 21 | 33 | nan | nan | nan | Cerrado | 80.5 |
| d57f4191-1043-31bc-8fbd-8b1834f4c2af | -8.6416 | -64.176 | 2025-07-12 13:50:00 | GOES-19 | CANUTAMA | AMAZONAS | Brasil | 1300904 | 13 | 33 | nan | nan | nan | Amazônia | 78.2 |
| 68e0e0e2-de7c-3af9-bb7f-9eb9c5478b6a | -7.1853 | -42.9777 | 2025-07-12 13:50:00 | GOES-19 | FLORIANO | PIAUÍ | Brasil | 2203909 | 22 | 33 | nan | nan | nan | Caatinga | 98.3 |
| 545f4221-8a0a-3e3b-976e-2cac7e5066a6 | -6.7288 | -45.2355 | 2025-07-12 13:50:00 | GOES-19 | MIRADOR | MARANHÃO | Brasil | 2106706 | 21 | 33 | nan | nan | nan | Cerrado | 117.6 |
| 5064c8ef-bc10-31ad-8c18-ea1bf66e6965 | -11.8382 | -47.506 | 2025-07-12 13:50:00 | GOES-19 | NATIVIDADE | TOCANTINS | Brasil | 1714203 | 17 | 33 | nan | nan | nan | Cerrado | 62.8 |
| 392254bd-141d-320a-b1ae-fab937f96d4a | -12.0628 | -43.5022 | 2025-07-12 13:50:00 | GOES-19 | MUQUÉM DO SÃO FRANCISCO | BAHIA | Brasil | 2922250 | 29 | 33 | nan | nan | nan | Cerrado | 91.0 |
| af144009-4b81-36ed-9b11-bf0649967c2c | -6.1232 | -45.9363 | 2025-07-12 13:50:00 | GOES-19 | GRAJAÚ | MARANHÃO | Brasil | 2104800 | 21 | 33 | nan | nan | nan | Cerrado | 69.7 |
| b55739c5-84d1-3e34-94cf-faa369d7a7e0 | -6.71 | -45.2371 | 2025-07-12 13:50:00 | GOES-19 | MIRADOR | MARANHÃO | Brasil | 2106706 | 21 | 33 | nan | nan | nan | Cerrado | 151.9 |
| 8f482f0e-50b1-3528-9de0-f42df22fc16e | -12.4669 | -44.4959 | 2025-07-12 13:50:00 | GOES-19 | BAIANÓPOLIS | BAHIA | Brasil | 2902500 | 29 | 33 | nan | nan | nan | Cerrado | 97.6 |
| 53f6e496-d1b8-3d17-b884-3e2a52eb43e4 | -6.0882 | -47.7944 | 2025-07-12 13:50:00 | GOES-19 | CACHOEIRINHA | TOCANTINS | Brasil | 1703826 | 17 | 33 | nan | nan | nan | Cerrado | 66.6 |
| eb91f914-fff2-38bd-985e-e43738e39718 | -8.9213 | -47.3374 | 2025-07-12 13:50:00 | GOES-19 | CENTENÁRIO | TOCANTINS | Brasil | 1704105 | 17 | 33 | nan | nan | nan | Cerrado | 92.6 |
| bade3259-f32f-32e5-9c4a-3a124a52e440 | -12.4862 | -44.4928 | 2025-07-12 13:50:00 | GOES-19 | BAIANÓPOLIS | BAHIA | Brasil | 2902500 | 29 | 33 | nan | nan | nan | Cerrado | 156.1 |
| a7319918-cdbb-3b08-bd44-a1e2832ad9f9 | -11.9255 | -51.6987 | 2025-07-12 14:00:00 | GOES-19 | ALTO BOA VISTA | MATO GROSSO | Brasil | 5100359 | 51 | 33 | nan | nan | nan | Amazônia | 79.0 |
| c3a2e799-d554-3aec-aac4-27292b028e91 | -12.0628 | -43.5022 | 2025-07-12 14:00:00 | GOES-19 | MUQUÉM DO SÃO FRANCISCO | BAHIA | Brasil | 2922250 | 29 | 33 | nan | nan | nan | Cerrado | 191.0 |
| 9fa04bc1-707d-3741-b65b-e98bdb9d79cb | -6.2783 | -43.4113 | 2025-07-12 14:00:00 | GOES-19 | SUCUPIRA DO RIACHÃO | MARANHÃO | Brasil | 2111953 | 21 | 33 | nan | nan | nan | Cerrado | 73.3 |
| a1ca9bea-ae4c-3e96-846c-e50c45691750 | -6.71 | -45.2371 | 2025-07-12 14:00:00 | GOES-19 | MIRADOR | MARANHÃO | Brasil | 2106706 | 21 | 33 | nan | nan | nan | Cerrado | 111.4 |
| 42380125-f9f0-3cde-9cb0-183c248ca2b8 | -12.4669 | -44.4959 | 2025-07-12 14:00:00 | GOES-19 | BAIANÓPOLIS | BAHIA | Brasil | 2902500 | 29 | 33 | nan | nan | nan | Cerrado | 108.4 |
| ac6e4818-8d9b-3749-aba1-5010d3191767 | -8.9213 | -47.3374 | 2025-07-12 14:00:00 | GOES-19 | CENTENÁRIO | TOCANTINS | Brasil | 1704105 | 17 | 33 | nan | nan | nan | Cerrado | 83.6 |
| b92d18a2-57d2-3e5f-9826-5e289a42b0d5 | -6.0882 | -47.7944 | 2025-07-12 14:00:00 | GOES-19 | CACHOEIRINHA | TOCANTINS | Brasil | 1703826 | 17 | 33 | nan | nan | nan | Cerrado | 101.4 |
| 2c559fbe-a1ee-3a12-832e-3a5bfcee4570 | -12.4862 | -44.4928 | 2025-07-12 14:00:00 | GOES-19 | BAIANÓPOLIS | BAHIA | Brasil | 2902500 | 29 | 33 | nan | nan | nan | Cerrado | 162.3 |
| b8873d05-7b99-37b4-ad53-6ae8576e8e95 | -6.1608 | -45.9111 | 2025-07-12 14:00:00 | GOES-19 | GRAJAÚ | MARANHÃO | Brasil | 2104800 | 21 | 33 | nan | nan | nan | Cerrado | 67.8 |
| 232d8576-72b7-3dcd-ad83-a989da13715b | -6.1069 | -47.7932 | 2025-07-12 14:00:00 | GOES-19 | CACHOEIRINHA | TOCANTINS | Brasil | 1703826 | 17 | 33 | nan | nan | nan | Cerrado | 80.3 |
| 69051638-faca-3ef0-9e05-dda5b57d7697 | -7.1853 | -42.9777 | 2025-07-12 14:00:00 | GOES-19 | FLORIANO | PIAUÍ | Brasil | 2203909 | 22 | 33 | nan | nan | nan | Caatinga | 87.7 |
| 190c176f-b58d-325b-a30c-1b7bd5d177db | -6.1232 | -45.9363 | 2025-07-12 14:00:00 | GOES-19 | GRAJAÚ | MARANHÃO | Brasil | 2104800 | 21 | 33 | nan | nan | nan | Cerrado | 82.2 |
| 1ce67280-8dea-378e-98de-2bd3ff617b15 | -12.4862 | -44.4928 | 2025-07-12 14:10:00 | GOES-19 | BAIANÓPOLIS | BAHIA | Brasil | 2902500 | 29 | 33 | nan | nan | nan | Cerrado | 158.9 |
| 902fcd47-e1c7-3c97-99ba-b1726f21aee7 | -11.4364 | -46.416 | 2025-07-12 14:10:00 | GOES-19 | FORMOSA DO RIO PRETO | BAHIA | Brasil | 2911105 | 29 | 33 | nan | nan | nan | Cerrado | 59.4 |


[Clique aqui para ver as próximas entradas](README21.md)
