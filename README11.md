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

## Dados Diários - Página 11

| ID | Latitude | Longitude | Data/Hora GMT | Satélite | Município | Estado | País | Município ID | Estado ID | País ID | Dias sem Chuva | Precipitação | Risco de Fogo | Bioma | FRP |
|----|----------|-----------|---------------|----------|-----------|--------|------|--------------|-----------|---------|----------------|--------------|----------------|-------|-----|
| b5700533-195e-35db-8bca-cebfab58bab5 | -13.04834 | -53.72078 | 2025-05-15 04:53:00 | NPP-375D | GAÚCHA DO NORTE | MATO GROSSO | Brasil | 5103858 | 51 | 33 | nan | nan | nan | Amazônia | 4.2 |
| c78803e5-a899-3dc4-9c56-80d175d82b2d | -13.05223 | -53.71776 | 2025-05-15 04:53:00 | NPP-375D | GAÚCHA DO NORTE | MATO GROSSO | Brasil | 5103858 | 51 | 33 | nan | nan | nan | Amazônia | 1.4 |
| be031870-50aa-36aa-881d-25e56ee27d31 | -15.26023 | -51.46106 | 2025-05-15 04:55:00 | NPP-375D | JUSSARA | GOIÁS | Brasil | 5212204 | 52 | 33 | nan | nan | nan | Cerrado | 6.5 |
| cad65029-70d0-318f-91bf-f21f76b683c4 | -15.63293 | -59.72108 | 2025-05-15 04:55:00 | NPP-375D | PONTES E LACERDA | MATO GROSSO | Brasil | 5106752 | 51 | 33 | nan | nan | nan | Amazônia | 1.2 |
| 40fb78c8-53aa-330d-bd2a-752c770753ec | -20.20782 | -46.75712 | 2025-05-15 04:55:00 | NPP-375D | SÃO ROQUE DE MINAS | MINAS GERAIS | Brasil | 3164308 | 31 | 33 | nan | nan | nan | Cerrado | 1.1 |
| 8e02bd08-fe50-31cc-95a0-101f3aa6728b | -15.57036 | -47.85705 | 2025-05-15 04:55:00 | NPP-375D | BRASÍLIA | DISTRITO FEDERAL | Brasil | 5300108 | 53 | 33 | nan | nan | nan | Cerrado | 1.3 |
| 6e067d4d-c3c6-303c-89d7-269ee63b769f | -15.26688 | -51.46649 | 2025-05-15 04:55:00 | NPP-375D | JUSSARA | GOIÁS | Brasil | 5212204 | 52 | 33 | nan | nan | nan | Cerrado | 3.6 |
| f816f3cf-80ad-396b-bc55-22cb595759af | -15.78688 | -54.52174 | 2025-05-15 04:55:00 | NPP-375D | POXORÉU | MATO GROSSO | Brasil | 5107008 | 51 | 33 | nan | nan | nan | Cerrado | 0.5 |
| f4c16bab-5357-301e-a8f1-b49ade2cfa3c | -20.51889 | -54.60614 | 2025-05-15 04:55:00 | NPP-375D | CAMPO GRANDE | MATO GROSSO DO SUL | Brasil | 5002704 | 50 | 33 | nan | nan | nan | Cerrado | 0.3 |
| 8e8b827a-de82-32dd-bb49-71ba3dc25b91 | -19.27158 | -54.99277 | 2025-05-15 04:55:00 | NPP-375D | RIO NEGRO | MATO GROSSO DO SUL | Brasil | 5007307 | 50 | 33 | nan | nan | nan | Cerrado | 0.5 |
| aac6b354-f372-3272-a83c-3d179f34c7ab | -16.38447 | -58.16317 | 2025-05-15 04:55:00 | NPP-375D | CÁCERES | MATO GROSSO | Brasil | 5102504 | 51 | 33 | nan | nan | nan | Pantanal | 0.8 |
| 6690f693-ec82-37bf-87d6-cc435c3ab614 | -14.00522 | -53.00817 | 2025-05-15 04:55:00 | NPP-375D | CAMPINÁPOLIS | MATO GROSSO | Brasil | 5102603 | 51 | 33 | nan | nan | nan | Cerrado | 0.9 |
| f4c10509-0866-3c18-a1cb-13e620f95daf | -17.24634 | -48.10602 | 2025-05-15 04:55:00 | NPP-375D | ORIZONA | GOIÁS | Brasil | 5215306 | 52 | 33 | nan | nan | nan | Cerrado | 0.7 |
| 9bd7e0d8-092f-3085-b8d0-9fdf492797f4 | -20.20818 | -46.75372 | 2025-05-15 04:55:00 | NPP-375D | SÃO ROQUE DE MINAS | MINAS GERAIS | Brasil | 3164308 | 31 | 33 | nan | nan | nan | Cerrado | 1.1 |
| 6d33b6c3-59d0-3f1e-8f30-b60585dec3bd | -15.23449 | -51.19326 | 2025-05-15 04:55:00 | NPP-375D | BRITÂNIA | GOIÁS | Brasil | 5203807 | 52 | 33 | nan | nan | nan | Cerrado | 2.0 |
| 5232a0d5-754b-3b58-8606-12774eeb9a1a | -20.59317 | -47.87631 | 2025-05-15 04:55:00 | NPP-375D | SÃO JOAQUIM DA BARRA | SÃO PAULO | Brasil | 3549409 | 35 | 33 | nan | nan | nan | Cerrado | 0.8 |
| a83a2f7a-cb7d-3683-a68c-bc8c5df0e048 | -19.06757 | -53.45143 | 2025-05-15 04:55:00 | NPP-375D | CAMAPUÃ | MATO GROSSO DO SUL | Brasil | 5002605 | 50 | 33 | nan | nan | nan | Cerrado | 0.9 |
| eb62c772-a61e-316a-b658-53278dad1d3d | -19.06064 | -53.45031 | 2025-05-15 04:55:00 | NPP-375D | CAMAPUÃ | MATO GROSSO DO SUL | Brasil | 5002605 | 50 | 33 | nan | nan | nan | Cerrado | 1.9 |
| 81b52289-0d49-3913-aaff-e44cb1c0237a | -15.26387 | -51.46162 | 2025-05-15 04:55:00 | NPP-375D | JUSSARA | GOIÁS | Brasil | 5212204 | 52 | 33 | nan | nan | nan | Cerrado | 6.5 |
| 6791f19e-1825-39ee-8420-395c9d40bb46 | -19.17239 | -57.53996 | 2025-05-15 04:55:00 | NPP-375D | LADÁRIO | MATO GROSSO DO SUL | Brasil | 5005202 | 50 | 33 | nan | nan | nan | Pantanal | 2.0 |
| ce2c1ab8-9667-389c-b2ed-61c5a72dbd8f | -20.7618 | -46.76872 | 2025-05-15 04:55:00 | NPP-375D | ITAÚ DE MINAS | MINAS GERAIS | Brasil | 3133758 | 31 | 33 | nan | nan | nan | Mata Atlântica | 0.7 |
| d785e2f8-ad08-3aed-8bb1-89dfb05573d0 | -14.40635 | -52.86403 | 2025-05-15 04:55:00 | NPP-375D | CAMPINÁPOLIS | MATO GROSSO | Brasil | 5102603 | 51 | 33 | nan | nan | nan | Cerrado | 0.5 |
| ea9c2504-7288-3435-a3c4-0f12c1bf49b9 | -20.59802 | -47.87712 | 2025-05-15 04:55:00 | NPP-375D | SÃO JOAQUIM DA BARRA | SÃO PAULO | Brasil | 3549409 | 35 | 33 | nan | nan | nan | Cerrado | 0.8 |
| 71c036ac-72b6-3592-ae36-dbc1420595a7 | -14.00578 | -53.00447 | 2025-05-15 04:55:00 | NPP-375D | CAMPINÁPOLIS | MATO GROSSO | Brasil | 5102603 | 51 | 33 | nan | nan | nan | Cerrado | 1.0 |
| 3e6c2e34-47a5-3b83-9066-d2a87009598e | -19.06411 | -53.45088 | 2025-05-15 04:55:00 | NPP-375D | CAMAPUÃ | MATO GROSSO DO SUL | Brasil | 5002605 | 50 | 33 | nan | nan | nan | Cerrado | 1.9 |
| d2db4b69-6df3-3063-b2d1-fadfac3adbc4 | -20.47586 | -53.67632 | 2025-05-15 04:55:00 | NPP-375D | RIBAS DO RIO PARDO | MATO GROSSO DO SUL | Brasil | 5007109 | 50 | 33 | nan | nan | nan | Cerrado | 0.8 |
| bb467b3b-6dc0-3ca9-bb2c-046f4b287201 | -15.2675 | -51.46218 | 2025-05-15 04:55:00 | NPP-375D | JUSSARA | GOIÁS | Brasil | 5212204 | 52 | 33 | nan | nan | nan | Cerrado | 3.6 |
| 254713c9-1abe-3e7c-861a-6402a79ab51f | -20.20746 | -46.76055 | 2025-05-15 04:55:00 | NPP-375D | SÃO ROQUE DE MINAS | MINAS GERAIS | Brasil | 3164308 | 31 | 33 | nan | nan | nan | Cerrado | 1.3 |
| ca4d1f78-d3d9-3361-bd94-1b54283f1b37 | -19.17173 | -57.54385 | 2025-05-15 04:55:00 | NPP-375D | LADÁRIO | MATO GROSSO DO SUL | Brasil | 5005202 | 50 | 33 | nan | nan | nan | Pantanal | 2.0 |
| a668e479-5bb8-3561-890c-7a4455fe5c3e | -17.88001 | -51.18885 | 2025-05-15 04:55:00 | NPP-375D | RIO VERDE | GOIÁS | Brasil | 5218805 | 52 | 33 | nan | nan | nan | Cerrado | 0.4 |
| 74042a44-026a-3576-9902-cbab78d9015d | -21.05467 | -55.99785 | 2025-05-15 04:55:00 | NPP-375D | NIOAQUE | MATO GROSSO DO SUL | Brasil | 5005806 | 50 | 33 | nan | nan | nan | Cerrado | 2.1 |
| 8b153c8f-6a35-3d97-8caf-a9eaf22967b8 | -19.16088 | -47.82045 | 2025-05-15 04:55:00 | NPP-375D | NOVA PONTE | MINAS GERAIS | Brasil | 3145000 | 31 | 33 | nan | nan | nan | Cerrado | 1.4 |
| 991109a8-28f2-3e7e-8030-7eb06e6fd7fb | -14.06733 | -57.10917 | 2025-05-15 04:55:00 | NPP-375D | DIAMANTINO | MATO GROSSO | Brasil | 5103502 | 51 | 33 | nan | nan | nan | Amazônia | 1.9 |
| fdd264b5-3aa7-330d-a173-f6aad748fcd3 | -19.05625 | -52.44611 | 2025-05-15 04:55:00 | NPP-375D | CASSILÂNDIA | MATO GROSSO DO SUL | Brasil | 5002902 | 50 | 33 | nan | nan | nan | Cerrado | 1.6 |
| 7c913bbf-f381-3852-aaed-da6989b22453 | -16.68156 | -43.88276 | 2025-05-15 04:55:00 | NPP-375D | MONTES CLAROS | MINAS GERAIS | Brasil | 3143302 | 31 | 33 | nan | nan | nan | Cerrado | 2.0 |
| 5043c63a-a497-3275-aa0f-7f55205c966d | -15.23282 | -51.19094 | 2025-05-15 04:55:00 | NPP-375D | BRITÂNIA | GOIÁS | Brasil | 5203807 | 52 | 33 | nan | nan | nan | Cerrado | 1.5 |
| 4e21e4c1-6f91-348c-941d-434e2d27582e | -15.78745 | -54.51814 | 2025-05-15 04:55:00 | NPP-375D | POXORÉU | MATO GROSSO | Brasil | 5107008 | 51 | 33 | nan | nan | nan | Cerrado | 0.7 |
| 96ae864e-64c8-3c1f-ade9-1baf79e28eab | -16.61317 | -53.40874 | 2025-05-15 04:55:00 | NPP-375D | ALTO GARÇAS | MATO GROSSO | Brasil | 5100409 | 51 | 33 | nan | nan | nan | Cerrado | 1.4 |
| 5cdbd9ec-e8d4-3967-9f54-6fe33b3f6ac4 | -16.67883 | -43.88582 | 2025-05-15 04:55:00 | NPP-375D | MONTES CLAROS | MINAS GERAIS | Brasil | 3143302 | 31 | 33 | nan | nan | nan | Cerrado | 2.0 |
| 41be9640-ae5a-3708-bc13-814d70b92dc7 | -19.15846 | -55.3246 | 2025-05-15 04:55:00 | NPP-375D | RIO VERDE DE MATO GROSSO | MATO GROSSO DO SUL | Brasil | 5007406 | 50 | 33 | nan | nan | nan | Pantanal | 0.6 |
| a9052fd5-4162-3ab9-aaec-e181ebe5c365 | -19.15604 | -47.82019 | 2025-05-15 04:55:00 | NPP-375D | NOVA PONTE | MINAS GERAIS | Brasil | 3145000 | 31 | 33 | nan | nan | nan | Cerrado | 4.5 |
| 972313b8-5cd9-3c7c-8958-0250d10e31b1 | -15.26325 | -51.46593 | 2025-05-15 04:55:00 | NPP-375D | JUSSARA | GOIÁS | Brasil | 5212204 | 52 | 33 | nan | nan | nan | Cerrado | 6.5 |
| a9504861-5c5b-33c7-8948-d3d971679b80 | -21.77858 | -52.73986 | 2025-05-15 04:57:00 | NPP-375D | BATAGUASSU | MATO GROSSO DO SUL | Brasil | 5001904 | 50 | 33 | nan | nan | nan | Cerrado | 1.0 |
| de9cdbac-a719-3d5d-9b28-b1afb0ce9a18 | -23.60493 | -48.29364 | 2025-05-15 04:57:00 | NPP-375D | ITAPETININGA | SÃO PAULO | Brasil | 3522307 | 35 | 33 | nan | nan | nan | Cerrado | 27.1 |
| 67f60f1d-9e30-3942-99ba-356914357f09 | -21.78225 | -52.74045 | 2025-05-15 04:57:00 | NPP-375D | BATAGUASSU | MATO GROSSO DO SUL | Brasil | 5001904 | 50 | 33 | nan | nan | nan | Cerrado | 1.1 |
| 6d3e3b97-79bb-3c53-8459-e0cc9c965dca | -27.11506 | -50.57163 | 2025-05-15 04:57:00 | NPP-375D | CURITIBANOS | SANTA CATARINA | Brasil | 4204806 | 42 | 33 | nan | nan | nan | Mata Atlântica | 0.9 |
| 99df18b6-6d50-3997-ad7f-0a08a75bb0f7 | -23.60799 | -48.298 | 2025-05-15 04:57:00 | NPP-375D | ITAPETININGA | SÃO PAULO | Brasil | 3522307 | 35 | 33 | nan | nan | nan | Cerrado | 9.4 |
| 6fdcccb2-21e7-32c9-a7f6-6a15b30c35c3 | -23.60306 | -48.29743 | 2025-05-15 04:57:00 | NPP-375D | ITAPETININGA | SÃO PAULO | Brasil | 3522307 | 35 | 33 | nan | nan | nan | Cerrado | 7.9 |
| e7f3c006-6971-3867-8209-68b9a98d2649 | -22.15669 | -56.64392 | 2025-05-15 04:57:00 | NPP-375D | BELA VISTA | MATO GROSSO DO SUL | Brasil | 5002100 | 50 | 33 | nan | nan | nan | Cerrado | 0.6 |
| d37d8977-8985-3dd4-8a73-618ece390c2e | -21.78103 | -55.31597 | 2025-05-15 04:57:00 | NPP-375D | MARACAJU | MATO GROSSO DO SUL | Brasil | 5005400 | 50 | 33 | nan | nan | nan | Cerrado | 0.5 |
| e8afa2e3-a968-394b-bb8c-c57b5bb71969 | -23.64538 | -54.56958 | 2025-05-15 04:57:00 | NPP-375D | IGUATEMI | MATO GROSSO DO SUL | Brasil | 5004304 | 50 | 33 | nan | nan | nan | Mata Atlântica | 4.3 |
| 4197b75c-0128-3511-aefa-de43699724bf | -23.60861 | -48.29219 | 2025-05-15 04:57:00 | NPP-375D | ITAPETININGA | SÃO PAULO | Brasil | 3522307 | 35 | 33 | nan | nan | nan | Cerrado | 9.4 |
| 779bc138-cf1e-33e0-b839-8788bab74b6e | -21.71985 | -55.37163 | 2025-05-15 04:57:00 | NPP-375D | MARACAJU | MATO GROSSO DO SUL | Brasil | 5005400 | 50 | 33 | nan | nan | nan | Cerrado | 0.9 |
| 928fa896-387b-3085-9411-b2ac758a96cd | -23.60367 | -48.29168 | 2025-05-15 04:57:00 | NPP-375D | ITAPETININGA | SÃO PAULO | Brasil | 3522307 | 35 | 33 | nan | nan | nan | Cerrado | 7.9 |
| 4bf85f21-cb47-371d-819f-78a4d040ec7a | -6.1633 | -48.53418 | 2025-05-15 05:14:00 | NOAA-20 | SÃO GERALDO DO ARAGUAIA | PARÁ | Brasil | 1507458 | 15 | 33 | nan | nan | nan | Amazônia | 0.7 |
| e6a4f329-ec84-3e73-b5b6-dc09dd8f1db5 | -6.15814 | -48.52885 | 2025-05-15 05:14:00 | NOAA-20 | SÃO GERALDO DO ARAGUAIA | PARÁ | Brasil | 1507458 | 15 | 33 | nan | nan | nan | Amazônia | 1.2 |
| 73ca5260-a1a3-36ce-8b6b-ae15463e2620 | -6.71667 | -47.59745 | 2025-05-15 05:14:00 | NOAA-20 | DARCINÓPOLIS | TOCANTINS | Brasil | 1706506 | 17 | 33 | nan | nan | nan | Cerrado | 5.6 |
| 606569cf-4a71-3d72-9ad9-d73d1ed0079b | -6.15753 | -48.53325 | 2025-05-15 05:14:00 | NOAA-20 | SÃO GERALDO DO ARAGUAIA | PARÁ | Brasil | 1507458 | 15 | 33 | nan | nan | nan | Amazônia | 1.5 |
| f867d0b7-3a3d-3242-9bcd-9d63695d80c5 | -11.00877 | -50.76286 | 2025-05-15 05:16:00 | NOAA-20 | LUCIARA | MATO GROSSO | Brasil | 5105309 | 51 | 33 | nan | nan | nan | Cerrado | 0.9 |
| c9308891-044a-3e7f-89ae-8f5049b989a4 | -12.6896 | -58.13002 | 2025-05-15 05:16:00 | NOAA-20 | BRASNORTE | MATO GROSSO | Brasil | 5101902 | 51 | 33 | nan | nan | nan | Cerrado | 0.6 |
| 5aa52594-4c0d-305f-a9a8-8461ad299bd4 | -11.38511 | -57.82372 | 2025-05-15 05:16:00 | NOAA-20 | JUARA | MATO GROSSO | Brasil | 5105101 | 51 | 33 | nan | nan | nan | Amazônia | 1.0 |
| 79b49991-94cc-3fd4-b8a1-caac816c75a9 | -13.16407 | -53.27842 | 2025-05-15 05:16:00 | NOAA-20 | GAÚCHA DO NORTE | MATO GROSSO | Brasil | 5103858 | 51 | 33 | nan | nan | nan | Amazônia | 0.7 |
| c3ccec83-50c5-3dd6-9372-8a1929ebc197 | -11.89062 | -56.40999 | 2025-05-15 05:16:00 | NOAA-20 | PORTO DOS GAÚCHOS | MATO GROSSO | Brasil | 5106802 | 51 | 33 | nan | nan | nan | Amazônia | 1.6 |
| f2c92e3b-9a74-3d30-930e-42f118b117c9 | -11.91494 | -54.4073 | 2025-05-15 05:16:00 | NOAA-20 | SANTA CARMEM | MATO GROSSO | Brasil | 5107248 | 51 | 33 | nan | nan | nan | Amazônia | 1.5 |
| 47407763-5837-36d3-98fd-1ca797190754 | -11.1636 | -48.67337 | 2025-05-15 05:16:00 | NOAA-20 | BREJINHO DE NAZARÉ | TOCANTINS | Brasil | 1703701 | 17 | 33 | nan | nan | nan | Cerrado | 4.1 |
| 5b03f2c9-d3e7-3063-b10c-b322858386e8 | -13.0866 | -54.87307 | 2025-05-15 05:16:00 | NOAA-20 | NOVA UBIRATÃ | MATO GROSSO | Brasil | 5106240 | 51 | 33 | nan | nan | nan | Amazônia | 0.9 |
| 7dafa02f-561a-3406-a070-b628d86eb8d2 | -12.14745 | -48.00968 | 2025-05-15 05:16:00 | NOAA-20 | PARANÃ | TOCANTINS | Brasil | 1716208 | 17 | 33 | nan | nan | nan | Cerrado | 1.4 |
| e965b30b-90ed-3907-a879-5b035a6d3e86 | -11.65345 | -48.1154 | 2025-05-15 05:16:00 | NOAA-20 | CHAPADA DA NATIVIDADE | TOCANTINS | Brasil | 1705102 | 17 | 33 | nan | nan | nan | Cerrado | 3.1 |
| a469a829-8c3a-37ac-a91c-2ede01e18383 | -11.91548 | -54.40333 | 2025-05-15 05:16:00 | NOAA-20 | SANTA CARMEM | MATO GROSSO | Brasil | 5107248 | 51 | 33 | nan | nan | nan | Amazônia | 1.5 |
| 4bb7b9e3-206b-340f-88de-6c6bcd4dba25 | -11.65848 | -58.26417 | 2025-05-15 05:16:00 | NOAA-20 | BRASNORTE | MATO GROSSO | Brasil | 5101902 | 51 | 33 | nan | nan | nan | Amazônia | 0.6 |
| 0a92e499-621c-337c-831b-8488442f9c33 | -10.52417 | -59.38127 | 2025-05-15 05:16:00 | NOAA-20 | ARIPUANÃ | MATO GROSSO | Brasil | 5101407 | 51 | 33 | nan | nan | nan | Amazônia | 1.1 |
| 3ad77b33-b7c1-30a9-832b-c8eac982b827 | -11.64706 | -48.11465 | 2025-05-15 05:16:00 | NOAA-20 | CHAPADA DA NATIVIDADE | TOCANTINS | Brasil | 1705102 | 17 | 33 | nan | nan | nan | Cerrado | 6.6 |
| 41315ee3-a948-3984-8e88-242a8fc0acf4 | -11.78289 | -47.35287 | 2025-05-15 05:16:00 | NOAA-20 | ALMAS | TOCANTINS | Brasil | 1700400 | 17 | 33 | nan | nan | nan | Cerrado | 3.0 |
| e71c1793-c804-3e1e-ac30-5e0ef0d9abe2 | -13.04624 | -53.71939 | 2025-05-15 05:16:00 | NOAA-20 | GAÚCHA DO NORTE | MATO GROSSO | Brasil | 5103858 | 51 | 33 | nan | nan | nan | Amazônia | 5.8 |
| 69ef1af2-e740-3d5b-9b06-26c568ff6764 | -8.71062 | -50.24974 | 2025-05-15 05:16:00 | NOAA-20 | SANTA MARIA DAS BARREIRAS | PARÁ | Brasil | 1506583 | 15 | 33 | nan | nan | nan | Amazônia | 2.3 |
| 3c99f0e5-0dc0-386a-83dc-7414a2f5e6bb | -10.34385 | -47.97838 | 2025-05-15 05:16:00 | NOAA-20 | MONTE DO CARMO | TOCANTINS | Brasil | 1713601 | 17 | 33 | nan | nan | nan | Cerrado | 0.9 |
| 2c7b3554-57d0-38a9-887d-996c3f4257bd | -13.67152 | -53.93494 | 2025-05-15 05:16:00 | NOAA-20 | GAÚCHA DO NORTE | MATO GROSSO | Brasil | 5103858 | 51 | 33 | nan | nan | nan | Cerrado | 2.5 |
| 063547c2-306a-3493-8b7c-11e4c3bb48d6 | -11.7822 | -47.35875 | 2025-05-15 05:16:00 | NOAA-20 | ALMAS | TOCANTINS | Brasil | 1700400 | 17 | 33 | nan | nan | nan | Cerrado | 3.0 |
| 741504f7-6129-32d6-8c59-f06f22d646d7 | -11.78614 | -47.35383 | 2025-05-15 05:16:00 | NOAA-20 | ALMAS | TOCANTINS | Brasil | 1700400 | 17 | 33 | nan | nan | nan | Cerrado | 5.4 |
| e2180fb7-8036-3636-bc7a-63b805479a54 | -13.621 | -54.88006 | 2025-05-15 05:16:00 | NOAA-20 | NOVA UBIRATÃ | MATO GROSSO | Brasil | 5106240 | 51 | 33 | nan | nan | nan | Cerrado | 0.8 |
| 76ae39dd-0d13-3e4a-b47e-550b7b9fd365 | -13.07186 | -52.01745 | 2025-05-15 05:16:00 | NOAA-20 | RIBEIRÃO CASCALHEIRA | MATO GROSSO | Brasil | 5107180 | 51 | 33 | nan | nan | nan | Amazônia | 1.6 |
| 2074346f-fd64-355e-afab-870362356711 | -12.68556 | -58.13335 | 2025-05-15 05:16:00 | NOAA-20 | BRASNORTE | MATO GROSSO | Brasil | 5101902 | 51 | 33 | nan | nan | nan | Cerrado | 3.2 |
| 338267f8-79f5-3fa5-806d-b400109f2e13 | -11.57959 | -47.61593 | 2025-05-15 05:16:00 | NOAA-20 | NATIVIDADE | TOCANTINS | Brasil | 1714203 | 17 | 33 | nan | nan | nan | Cerrado | 1.9 |
| bc7ca4c0-8779-3243-a8c9-b52e22b20780 | -7.74272 | -46.33821 | 2025-05-15 05:16:00 | NOAA-20 | BALSAS | MARANHÃO | Brasil | 2101400 | 21 | 33 | nan | nan | nan | Cerrado | 3.5 |
| c6c7e823-78b5-3df5-a646-b4bf722b6b75 | -12.14644 | -48.01373 | 2025-05-15 05:16:00 | NOAA-20 | PARANÃ | TOCANTINS | Brasil | 1716208 | 17 | 33 | nan | nan | nan | Cerrado | 2.0 |
| f991a4d6-32d6-3337-ba75-1e7631f4ab3c | -8.71641 | -50.24713 | 2025-05-15 05:16:00 | NOAA-20 | SANTA MARIA DAS BARREIRAS | PARÁ | Brasil | 1506583 | 15 | 33 | nan | nan | nan | Amazônia | 0.6 |
| 8f7e6a6f-ba94-3972-b612-79bfbcc7e040 | -11.56559 | -47.44444 | 2025-05-15 05:16:00 | NOAA-20 | NATIVIDADE | TOCANTINS | Brasil | 1714203 | 17 | 33 | nan | nan | nan | Cerrado | 5.6 |
| 6e2d581e-71b6-3905-825b-579c8b238f08 | -8.80127 | -49.82064 | 2025-05-15 05:16:00 | NOAA-20 | SANTA MARIA DAS BARREIRAS | PARÁ | Brasil | 1506583 | 15 | 33 | nan | nan | nan | Amazônia | 3.3 |
| d32de2de-aa1e-3407-8340-b67c7f878faa | -8.58505 | -45.88901 | 2025-05-15 05:16:00 | NOAA-20 | TASSO FRAGOSO | MARANHÃO | Brasil | 2112001 | 21 | 33 | nan | nan | nan | Cerrado | 2.1 |
| edf8bcf0-c0c4-31a5-952d-70896050ac87 | -10.66788 | -57.64006 | 2025-05-15 05:16:00 | NOAA-20 | JUARA | MATO GROSSO | Brasil | 5105101 | 51 | 33 | nan | nan | nan | Amazônia | 1.2 |
| a68aeb55-3626-3804-9ea6-fc81767c7587 | -11.30512 | -54.01623 | 2025-05-15 05:16:00 | NOAA-20 | UNIÃO DO SUL | MATO GROSSO | Brasil | 5108303 | 51 | 33 | nan | nan | nan | Amazônia | 1.8 |
| 11533f31-83da-312e-a6d4-08494a34c113 | -12.49346 | -54.39754 | 2025-05-15 05:16:00 | NOAA-20 | NOVA UBIRATÃ | MATO GROSSO | Brasil | 5106240 | 51 | 33 | nan | nan | nan | Amazônia | 0.8 |
| c45c766c-5cb5-321b-9456-ab073576bce5 | -11.55475 | -47.61189 | 2025-05-15 05:16:00 | NOAA-20 | NATIVIDADE | TOCANTINS | Brasil | 1714203 | 17 | 33 | nan | nan | nan | Cerrado | 4.5 |
| b874b2f4-16e3-306b-b623-1a5d5df66408 | -11.87441 | -56.41683 | 2025-05-15 05:16:00 | NOAA-20 | PORTO DOS GAÚCHOS | MATO GROSSO | Brasil | 5106802 | 51 | 33 | nan | nan | nan | Amazônia | 1.2 |
| 06a44c1e-cabe-3aad-b7d3-8ecdae9b4303 | -13.16472 | -53.27348 | 2025-05-15 05:16:00 | NOAA-20 | GAÚCHA DO NORTE | MATO GROSSO | Brasil | 5103858 | 51 | 33 | nan | nan | nan | Amazônia | 0.6 |
| afe17350-5d5b-3f64-b507-7cb4273d916a | -7.94953 | -49.7619 | 2025-05-15 05:16:00 | NOAA-20 | CONCEIÇÃO DO ARAGUAIA | PARÁ | Brasil | 1502707 | 15 | 33 | nan | nan | nan | Amazônia | 5.4 |
| df297317-84ac-352c-ae06-b2ed14e85263 | -12.68902 | -58.1339 | 2025-05-15 05:16:00 | NOAA-20 | BRASNORTE | MATO GROSSO | Brasil | 5101902 | 51 | 33 | nan | nan | nan | Cerrado | 1.0 |
| ff0da54f-5639-3a43-81b0-70ba6eee67a7 | -11.15748 | -48.67255 | 2025-05-15 05:16:00 | NOAA-20 | BREJINHO DE NAZARÉ | TOCANTINS | Brasil | 1703701 | 17 | 33 | nan | nan | nan | Cerrado | 1.7 |
| 10a625ea-2497-316b-8fb5-c928a0d1b7f8 | -8.80175 | -49.81705 | 2025-05-15 05:16:00 | NOAA-20 | SANTA MARIA DAS BARREIRAS | PARÁ | Brasil | 1506583 | 15 | 33 | nan | nan | nan | Amazônia | 3.7 |
| 28a0cfd0-1305-305d-a191-10b43f4b8c65 | -11.89179 | -56.41257 | 2025-05-15 05:16:00 | NOAA-20 | PORTO DOS GAÚCHOS | MATO GROSSO | Brasil | 5106802 | 51 | 33 | nan | nan | nan | Amazônia | 1.1 |


[Clique aqui para ver as próximas entradas](README12.md)
