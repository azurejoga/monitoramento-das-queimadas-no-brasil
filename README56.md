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

## Dados Diários - Página 56

| ID | Latitude | Longitude | Data/Hora GMT | Satélite | Município | Estado | País | Município ID | Estado ID | País ID | Dias sem Chuva | Precipitação | Risco de Fogo | Bioma | FRP |
|----|----------|-----------|---------------|----------|-----------|--------|------|--------------|-----------|---------|----------------|--------------|----------------|-------|-----|
| 07781560-4e1d-3bab-9628-ee7049781574 | -8.20784 | -46.98907 | 2025-10-24 12:19:00 | TERRA_M-T | CAMPOS LINDOS | TOCANTINS | Brasil | 1703842 | 17 | 33 | nan | nan | nan | Cerrado | 10.3 |
| 0c37e75a-b2fc-3f24-af96-b4a723560932 | -9.23401 | -51.82597 | 2025-10-24 12:19:00 | TERRA_M-T | SÃO FÉLIX DO XINGU | PARÁ | Brasil | 1507300 | 15 | 33 | nan | nan | nan | Amazônia | 13.7 |
| 6e2a30c7-887e-3b23-97b1-279e5fca88d5 | -10.55874 | -50.00485 | 2025-10-24 12:19:00 | TERRA_M-T | PIUM | TOCANTINS | Brasil | 1717503 | 17 | 33 | nan | nan | nan | Cerrado | 16.2 |
| f47af4d7-08e3-344b-a9d8-bcf1fcae08a8 | -9.56083 | -49.63753 | 2025-10-24 12:19:00 | TERRA_M-T | MARIANÓPOLIS DO TOCANTINS | TOCANTINS | Brasil | 1712504 | 17 | 33 | nan | nan | nan | Cerrado | 41.6 |
| cac3de1f-28d1-32c9-a1b1-4805f088bbf7 | -10.54201 | -50.17844 | 2025-10-24 12:19:00 | TERRA_M-T | PIUM | TOCANTINS | Brasil | 1717503 | 17 | 33 | nan | nan | nan | Cerrado | 22.6 |
| 66063306-e342-3935-9af2-8dec4e961c6a | -12.2397 | -47.49242 | 2025-10-24 12:19:00 | TERRA_M-T | CONCEIÇÃO DO TOCANTINS | TOCANTINS | Brasil | 1705607 | 17 | 33 | nan | nan | nan | Cerrado | 11.4 |
| 2c0746cd-8dc3-3aba-ab35-313718b886d4 | -14.47357 | -47.92442 | 2025-10-24 12:19:00 | TERRA_M-T | NIQUELÂNDIA | GOIÁS | Brasil | 5214606 | 52 | 33 | nan | nan | nan | Cerrado | 5.4 |
| 4d4173b0-e0f1-32cb-b259-edb07b172c39 | -11.02912 | -49.88472 | 2025-10-24 12:19:00 | TERRA_M-T | LAGOA DA CONFUSÃO | TOCANTINS | Brasil | 1711902 | 17 | 33 | nan | nan | nan | Cerrado | 15.7 |
| 6fc3250e-28fb-3d6e-94eb-1e93cc93d838 | -10.04821 | -47.08533 | 2025-10-24 12:19:00 | TERRA_M-T | LIZARDA | TOCANTINS | Brasil | 1712405 | 17 | 33 | nan | nan | nan | Cerrado | 14.4 |
| 0a3ff6ea-fd4b-3b47-99a1-b5e50ed2ffd4 | -8.09935 | -46.91204 | 2025-10-24 12:19:00 | TERRA_M-T | CAMPOS LINDOS | TOCANTINS | Brasil | 1703842 | 17 | 33 | nan | nan | nan | Cerrado | 5.3 |
| c32376db-fd53-304a-b0cf-4e40f0b36e4d | -10.38473 | -48.28844 | 2025-10-24 12:19:00 | TERRA_M-T | PALMAS | TOCANTINS | Brasil | 1721000 | 17 | 33 | nan | nan | nan | Cerrado | 11.1 |
| f485ce55-ef79-371d-9ffc-d2f9d66c5b57 | -14.26546 | -52.11903 | 2025-10-24 12:19:00 | TERRA_M-T | ÁGUA BOA | MATO GROSSO | Brasil | 5100201 | 51 | 33 | nan | nan | nan | Cerrado | 36.8 |
| c6536438-ece9-3213-8699-d43d6a119adf | -10.89398 | -50.11261 | 2025-10-24 12:19:00 | TERRA_M-T | LAGOA DA CONFUSÃO | TOCANTINS | Brasil | 1711902 | 17 | 33 | nan | nan | nan | Cerrado | 36.1 |
| 0308e2f2-7d6e-3f28-855d-6333c3ff420d | -12.78099 | -47.37334 | 2025-10-24 12:19:00 | TERRA_M-T | PARANÃ | TOCANTINS | Brasil | 1716208 | 17 | 33 | nan | nan | nan | Cerrado | 85.5 |
| cfb6b1e9-3bba-313d-8164-6cd8110b2cba | -12.24618 | -47.44566 | 2025-10-24 12:19:00 | TERRA_M-T | CONCEIÇÃO DO TOCANTINS | TOCANTINS | Brasil | 1705607 | 17 | 33 | nan | nan | nan | Cerrado | 11.9 |
| f0e5d699-8064-34dd-afdf-1914e1e04365 | -12.64843 | -44.12109 | 2025-10-24 12:19:00 | TERRA_M-T | TABOCAS DO BREJO VELHO | BAHIA | Brasil | 2930907 | 29 | 33 | nan | nan | nan | Cerrado | 16.5 |
| 90e23188-2742-3ba2-a0a9-2084fc5b596e | -8.65067 | -44.78268 | 2025-10-24 12:19:00 | TERRA_M-T | CURRAIS | PIAUÍ | Brasil | 2203230 | 22 | 33 | nan | nan | nan | Cerrado | 29.0 |
| 786ead20-11dd-3500-8a9c-413041f986db | -12.77059 | -47.38165 | 2025-10-24 12:19:00 | TERRA_M-T | PARANÃ | TOCANTINS | Brasil | 1716208 | 17 | 33 | nan | nan | nan | Cerrado | 44.4 |
| af92ffd4-e4ee-39dc-a650-dd891edfce07 | -14.5347 | -47.94923 | 2025-10-24 12:19:00 | TERRA_M-T | NIQUELÂNDIA | GOIÁS | Brasil | 5214606 | 52 | 33 | nan | nan | nan | Cerrado | 9.0 |
| 0656fe39-d946-3c72-b14a-0504ed7c66cc | -10.94932 | -50.36357 | 2025-10-24 12:19:00 | TERRA_M-T | LAGOA DA CONFUSÃO | TOCANTINS | Brasil | 1711902 | 17 | 33 | nan | nan | nan | Cerrado | 22.9 |
| 1aa26761-085e-3eaa-8a12-ddb71d2782a3 | -15.36067 | -51.05009 | 2025-10-24 12:19:00 | TERRA_M-T | BRITÂNIA | GOIÁS | Brasil | 5203807 | 52 | 33 | nan | nan | nan | Cerrado | 12.3 |
| 9cabcff9-08ea-3826-83f6-500488118efe | -12.17431 | -49.43759 | 2025-10-24 12:19:00 | TERRA_M-T | FORMOSO DO ARAGUAIA | TOCANTINS | Brasil | 1708205 | 17 | 33 | nan | nan | nan | Cerrado | 35.3 |
| cba8e26a-d756-317d-977a-d47c5332efdc | -7.41791 | -46.38398 | 2025-10-24 12:19:00 | TERRA_M-T | RIACHÃO | MARANHÃO | Brasil | 2109502 | 21 | 33 | nan | nan | nan | Cerrado | 7.1 |
| 5c03c22e-f79d-3fdd-8078-7c22590ded4a | -11.37028 | -45.98262 | 2025-10-24 12:19:00 | TERRA_M-T | FORMOSA DO RIO PRETO | BAHIA | Brasil | 2911105 | 29 | 33 | nan | nan | nan | Cerrado | 78.0 |
| c9c1e672-be30-3c60-b9b3-58864bfbcfda | -7.79241 | -45.39717 | 2025-10-24 12:19:00 | TERRA_M-T | RIBEIRO GONÇALVES | PIAUÍ | Brasil | 2208908 | 22 | 33 | nan | nan | nan | Cerrado | 6.6 |
| 4e9c2b20-be52-378c-aab5-440a9d62a872 | -7.65686 | -46.3243 | 2025-10-24 12:19:00 | TERRA_M-T | BALSAS | MARANHÃO | Brasil | 2101400 | 21 | 33 | nan | nan | nan | Cerrado | 11.7 |
| 881efcd4-fa27-3199-bb19-49a3d65d70ac | -10.64754 | -48.0714 | 2025-10-24 12:19:00 | TERRA_M-T | MONTE DO CARMO | TOCANTINS | Brasil | 1713601 | 17 | 33 | nan | nan | nan | Cerrado | 21.2 |
| f2ab5438-243b-3e1c-a064-0bbe8bd1cd9d | -13.93137 | -49.40973 | 2025-10-24 12:19:00 | TERRA_M-T | AMARALINA | GOIÁS | Brasil | 5200829 | 52 | 33 | nan | nan | nan | Cerrado | 7.2 |
| 96003642-8d84-3a2f-97f6-79f946dad99a | -13.88445 | -48.38256 | 2025-10-24 12:19:00 | TERRA_M-T | CAMPINAÇU | GOIÁS | Brasil | 5204656 | 52 | 33 | nan | nan | nan | Cerrado | 10.5 |
| fd80e792-394d-36ed-8916-9f15b57af83a | -16.4932 | -49.42755 | 2025-10-24 12:19:00 | TERRA_M-T | GOIANIRA | GOIÁS | Brasil | 5208806 | 52 | 33 | nan | nan | nan | Cerrado | 6.2 |
| f7dc2918-e485-3800-8fb0-a0227f2c0171 | -12.56424 | -43.79245 | 2025-10-24 12:19:00 | TERRA_M-T | BREJOLÂNDIA | BAHIA | Brasil | 2904407 | 29 | 33 | nan | nan | nan | Cerrado | 49.9 |
| b263cf55-57e2-3dcc-8af2-5720b86e06f5 | -12.01329 | -46.92533 | 2025-10-24 12:19:00 | TERRA_M-T | TAIPAS DO TOCANTINS | TOCANTINS | Brasil | 1720937 | 17 | 33 | nan | nan | nan | Cerrado | 11.0 |
| c53b3889-38d3-3e9c-9589-acb0f2be398c | -8.8467 | -47.23844 | 2025-10-24 12:19:00 | TERRA_M-T | CENTENÁRIO | TOCANTINS | Brasil | 1704105 | 17 | 33 | nan | nan | nan | Cerrado | 10.3 |
| 94c945e6-4d2c-3b85-8224-a32928e697ff | -9.34361 | -49.92245 | 2025-10-24 12:19:00 | TERRA_M-T | CASEARA | TOCANTINS | Brasil | 1703909 | 17 | 33 | nan | nan | nan | Cerrado | 6.7 |
| fc1a815a-8536-3614-a99d-ff8640cff056 | -10.63204 | -42.31396 | 2025-10-24 12:19:00 | TERRA_M-T | ITAGUAÇU DA BAHIA | BAHIA | Brasil | 2915353 | 29 | 33 | nan | nan | nan | Caatinga | 96.4 |
| b3dedb44-5fc2-3d84-b300-f6494e8ec11f | -12.63746 | -44.12556 | 2025-10-24 12:19:00 | TERRA_M-T | TABOCAS DO BREJO VELHO | BAHIA | Brasil | 2930907 | 29 | 33 | nan | nan | nan | Cerrado | 39.2 |
| 250fcad4-10f1-3370-9194-0ef0e966ed14 | -13.29163 | -48.27871 | 2025-10-24 12:19:00 | TERRA_M-T | MINAÇU | GOIÁS | Brasil | 5213087 | 52 | 33 | nan | nan | nan | Cerrado | 6.3 |
| f8f26388-43fa-30d9-8385-0e28e98853d6 | -14.875 | -50.96233 | 2025-10-24 12:19:00 | TERRA_M-T | ARUANÃ | GOIÁS | Brasil | 5202502 | 52 | 33 | nan | nan | nan | Cerrado | 9.9 |
| c5ace0a2-4787-3333-a779-f09ccb703733 | -10.9232 | -48.39369 | 2025-10-24 12:19:00 | TERRA_M-T | PORTO NACIONAL | TOCANTINS | Brasil | 1718204 | 17 | 33 | nan | nan | nan | Cerrado | 8.4 |
| bf2523cd-98b0-38e1-8c25-e227fabae7f3 | -12.66056 | -48.62471 | 2025-10-24 12:19:00 | TERRA_M-T | JAÚ DO TOCANTINS | TOCANTINS | Brasil | 1711506 | 17 | 33 | nan | nan | nan | Cerrado | 15.4 |
| a602d814-c4f9-36ee-977a-c8e6c493c8c3 | -10.93201 | -48.39495 | 2025-10-24 12:19:00 | TERRA_M-T | PORTO NACIONAL | TOCANTINS | Brasil | 1718204 | 17 | 33 | nan | nan | nan | Cerrado | 11.7 |
| bf396ee4-defe-3d3b-810b-e0802d5b2296 | -8.02919 | -45.15085 | 2025-10-24 12:19:00 | TERRA_M-T | BAIXA GRANDE DO RIBEIRO | PIAUÍ | Brasil | 2201150 | 22 | 33 | nan | nan | nan | Cerrado | 21.8 |
| c8e48506-7c2a-3f6e-bdd0-1ca8fa0f08bd | -8.50922 | -48.81968 | 2025-10-24 12:19:00 | TERRA_M-T | ITAPORÃ DO TOCANTINS | TOCANTINS | Brasil | 1711100 | 17 | 33 | nan | nan | nan | Amazônia | 8.2 |
| ec43edc8-23d2-33f5-91eb-810165dcb40d | -15.03538 | -43.3634 | 2025-10-24 12:19:00 | TERRA_M-T | GAMELEIRAS | MINAS GERAIS | Brasil | 3127339 | 31 | 33 | nan | nan | nan | Caatinga | 29.0 |
| 4e1f27a4-76f4-39b8-9f9c-adbcdf65b6d3 | -10.93724 | -50.38171 | 2025-10-24 12:19:00 | TERRA_M-T | LAGOA DA CONFUSÃO | TOCANTINS | Brasil | 1711902 | 17 | 33 | nan | nan | nan | Cerrado | 5.3 |
| 6635ae22-8d5d-3257-bb56-98756bdc18f5 | -17.11649 | -51.28457 | 2025-10-24 12:19:00 | TERRA_M-T | CAIAPÔNIA | GOIÁS | Brasil | 5204409 | 52 | 33 | nan | nan | nan | Cerrado | 6.6 |
| 93853bce-5fb2-361e-a42b-1315fae64d19 | -12.0807 | -46.42311 | 2025-10-24 12:19:00 | TERRA_M-T | PONTE ALTA DO BOM JESUS | TOCANTINS | Brasil | 1717800 | 17 | 33 | nan | nan | nan | Cerrado | 32.6 |
| a04f6f72-5058-36b8-b169-0a1b84b9bf4e | -10.95474 | -50.13754 | 2025-10-24 12:19:00 | TERRA_M-T | LAGOA DA CONFUSÃO | TOCANTINS | Brasil | 1711902 | 17 | 33 | nan | nan | nan | Cerrado | 12.5 |
| 416b8531-cf55-3a3e-b1fb-d3304b3c9012 | -11.97124 | -49.19239 | 2025-10-24 12:19:00 | TERRA_M-T | CARIRI DO TOCANTINS | TOCANTINS | Brasil | 1703867 | 17 | 33 | nan | nan | nan | Cerrado | 40.9 |
| 0bb348d7-a86c-3db1-a2ef-78e5b099b0f6 | -12.11201 | -47.01449 | 2025-10-24 12:19:00 | TERRA_M-T | TAIPAS DO TOCANTINS | TOCANTINS | Brasil | 1720937 | 17 | 33 | nan | nan | nan | Cerrado | 11.8 |
| 781aec9e-aed5-3a77-a958-63bda8f0641f | -13.89203 | -48.39313 | 2025-10-24 12:19:00 | TERRA_M-T | CAMPINAÇU | GOIÁS | Brasil | 5204656 | 52 | 33 | nan | nan | nan | Cerrado | 24.0 |
| c185ce05-bc8a-3166-a47b-07150f29764d | -10.6488 | -48.06255 | 2025-10-24 12:19:00 | TERRA_M-T | MONTE DO CARMO | TOCANTINS | Brasil | 1713601 | 17 | 33 | nan | nan | nan | Cerrado | 14.2 |
| 79a401f4-e805-3a47-9b97-69aff4d90ec7 | -10.0495 | -47.07598 | 2025-10-24 12:19:00 | TERRA_M-T | LIZARDA | TOCANTINS | Brasil | 1712405 | 17 | 33 | nan | nan | nan | Cerrado | 20.7 |
| 7acaa888-c781-326c-98bf-34514523e541 | -13.02768 | -48.5739 | 2025-10-24 12:19:00 | TERRA_M-T | JAÚ DO TOCANTINS | TOCANTINS | Brasil | 1711506 | 17 | 33 | nan | nan | nan | Cerrado | 6.6 |
| 80b0c238-f1fc-3df8-a839-7f128e3f0f60 | -12.17563 | -49.42852 | 2025-10-24 12:19:00 | TERRA_M-T | FORMOSO DO ARAGUAIA | TOCANTINS | Brasil | 1708205 | 17 | 33 | nan | nan | nan | Cerrado | 15.6 |
| 13f0c3d7-ec04-3bbd-bfa1-f348d5f796c1 | -11.03052 | -49.87537 | 2025-10-24 12:19:00 | TERRA_M-T | LAGOA DA CONFUSÃO | TOCANTINS | Brasil | 1711902 | 17 | 33 | nan | nan | nan | Cerrado | 12.9 |
| a3f332e4-435b-39f5-ab63-7a181fa4f015 | -8.74585 | -45.83356 | 2025-10-24 12:19:00 | TERRA_M-T | SANTA FILOMENA | PIAUÍ | Brasil | 2209203 | 22 | 33 | nan | nan | nan | Cerrado | 8.8 |
| 45a8ce21-29bf-34b0-a526-691efc7a1f6b | -10.61987 | -47.93363 | 2025-10-24 12:19:00 | TERRA_M-T | MONTE DO CARMO | TOCANTINS | Brasil | 1713601 | 17 | 33 | nan | nan | nan | Cerrado | 8.7 |
| 330223ff-05b1-3677-a5cf-3d53076eb1c9 | -9.59068 | -46.9277 | 2025-10-24 12:19:00 | TERRA_M-T | LIZARDA | TOCANTINS | Brasil | 1712405 | 17 | 33 | nan | nan | nan | Cerrado | 28.5 |
| 2de6a9cc-be4e-3f0f-ada4-3d2565b5dfe7 | -11.00091 | -50.2589 | 2025-10-24 12:19:00 | TERRA_M-T | LAGOA DA CONFUSÃO | TOCANTINS | Brasil | 1711902 | 17 | 33 | nan | nan | nan | Cerrado | 11.4 |
| 5eb2f595-816c-36a2-9e3c-b838d1146d2a | -12.77189 | -47.37207 | 2025-10-24 12:19:00 | TERRA_M-T | PARANÃ | TOCANTINS | Brasil | 1716208 | 17 | 33 | nan | nan | nan | Cerrado | 45.9 |
| f2d2ceb2-768b-3ef0-870d-0ddcec388065 | -10.04692 | -47.09462 | 2025-10-24 12:19:00 | TERRA_M-T | LIZARDA | TOCANTINS | Brasil | 1712405 | 17 | 33 | nan | nan | nan | Cerrado | 19.3 |
| cfd69ebb-9cb4-386d-a6b3-fcd3c2dcbd37 | -16.40206 | -50.12364 | 2025-10-24 12:19:00 | TERRA_M-T | ANICUNS | GOIÁS | Brasil | 5201306 | 52 | 33 | nan | nan | nan | Cerrado | 7.0 |
| dc5b070d-42e5-3160-b643-2dd43b9e46e0 | -8.16139 | -48.73548 | 2025-10-24 12:19:00 | TERRA_M-T | BANDEIRANTES DO TOCANTINS | TOCANTINS | Brasil | 1703057 | 17 | 33 | nan | nan | nan | Amazônia | 24.9 |
| 8eba9e33-efdc-3cfb-b13d-468f559425c7 | -16.47327 | -43.98554 | 2025-10-24 12:19:00 | TERRA_M-T | CORAÇÃO DE JESUS | MINAS GERAIS | Brasil | 3118809 | 31 | 33 | nan | nan | nan | Cerrado | 65.3 |
| ae08e018-4be1-3d71-823f-b1205b789bb8 | -7.46226 | -49.40893 | 2025-10-24 12:19:00 | TERRA_M-T | FLORESTA DO ARAGUAIA | PARÁ | Brasil | 1503044 | 15 | 33 | nan | nan | nan | Amazônia | 76.2 |
| 229745ef-0b0e-38c0-92c0-f98aa3af560f | -8.61607 | -44.81358 | 2025-10-24 12:19:00 | TERRA_M-T | CURRAIS | PIAUÍ | Brasil | 2203230 | 22 | 33 | nan | nan | nan | Cerrado | 27.4 |
| 245728f8-ca33-32ea-a9bd-7da51284e9e8 | -10.99117 | -50.38637 | 2025-10-24 12:19:00 | TERRA_M-T | LAGOA DA CONFUSÃO | TOCANTINS | Brasil | 1711902 | 17 | 33 | nan | nan | nan | Cerrado | 21.1 |
| 329f2f4b-bd9f-3ec2-9e6b-7c676d16bd96 | -12.14866 | -47.01988 | 2025-10-24 12:19:00 | TERRA_M-T | TAIPAS DO TOCANTINS | TOCANTINS | Brasil | 1720937 | 17 | 33 | nan | nan | nan | Cerrado | 6.9 |
| 40223024-19c3-35ea-86c8-1f0e062d37f5 | -11.25232 | -49.87301 | 2025-10-24 12:19:00 | TERRA_M-T | LAGOA DA CONFUSÃO | TOCANTINS | Brasil | 1711902 | 17 | 33 | nan | nan | nan | Cerrado | 5.9 |
| 8621565e-53a9-324a-a246-34dc6b26f824 | -13.36195 | -47.9699 | 2025-10-24 12:19:00 | TERRA_M-T | CAVALCANTE | GOIÁS | Brasil | 5205307 | 52 | 33 | nan | nan | nan | Cerrado | 52.3 |
| 603818af-86ae-3697-9a01-98bd0c11171c | -10.53766 | -50.2074 | 2025-10-24 12:19:00 | TERRA_M-T | PIUM | TOCANTINS | Brasil | 1717503 | 17 | 33 | nan | nan | nan | Cerrado | 54.2 |
| 4520d81e-e292-3b25-b445-86104745133b | -12.63538 | -44.13447 | 2025-10-24 12:19:00 | TERRA_M-T | TABOCAS DO BREJO VELHO | BAHIA | Brasil | 2930907 | 29 | 33 | nan | nan | nan | Cerrado | 90.1 |
| 97d63952-8e52-3cd7-be61-3feb1285d068 | -14.52513 | -47.95095 | 2025-10-24 12:19:00 | TERRA_M-T | NIQUELÂNDIA | GOIÁS | Brasil | 5214606 | 52 | 33 | nan | nan | nan | Cerrado | 11.9 |
| 1890c0be-9e45-3468-b1ee-56179701e350 | -9.61188 | -46.90878 | 2025-10-24 12:19:00 | TERRA_M-T | LIZARDA | TOCANTINS | Brasil | 1712405 | 17 | 33 | nan | nan | nan | Cerrado | 12.7 |
| fcbfe834-93da-31d3-940f-7916ac89b940 | -7.76423 | -46.9395 | 2025-10-24 12:19:00 | TERRA_M-T | CAROLINA | MARANHÃO | Brasil | 2102804 | 21 | 33 | nan | nan | nan | Cerrado | 11.2 |
| 8de04bd1-4661-3e58-96f8-af0e9d2ef600 | -16.47533 | -43.96794 | 2025-10-24 12:19:00 | TERRA_M-T | MONTES CLAROS | MINAS GERAIS | Brasil | 3143302 | 31 | 33 | nan | nan | nan | Cerrado | 25.0 |
| 13295561-3acf-3bbf-8291-5db2ebacc60b | -7.43416 | -49.60019 | 2025-10-24 12:19:00 | TERRA_M-T | FLORESTA DO ARAGUAIA | PARÁ | Brasil | 1503044 | 15 | 33 | nan | nan | nan | Amazônia | 25.9 |
| d5c12b7e-2301-380a-87de-88d776380e4b | -10.94788 | -50.37333 | 2025-10-24 12:19:00 | TERRA_M-T | LAGOA DA CONFUSÃO | TOCANTINS | Brasil | 1711902 | 17 | 33 | nan | nan | nan | Cerrado | 29.0 |
| 6c3b8b5c-3df7-3d35-8f24-341dcc3f2ad0 | -12.83072 | -48.66174 | 2025-10-24 12:19:00 | TERRA_M-T | JAÚ DO TOCANTINS | TOCANTINS | Brasil | 1711506 | 17 | 33 | nan | nan | nan | Cerrado | 8.2 |
| fac83933-9748-3bfb-a1f9-da1a801234a6 | -8.02775 | -45.16152 | 2025-10-24 12:19:00 | TERRA_M-T | BAIXA GRANDE DO RIBEIRO | PIAUÍ | Brasil | 2201150 | 22 | 33 | nan | nan | nan | Cerrado | 7.8 |
| c32a520d-10d8-3765-bf02-52323d903b3b | -11.01006 | -50.26027 | 2025-10-24 12:19:00 | TERRA_M-T | LAGOA DA CONFUSÃO | TOCANTINS | Brasil | 1711902 | 17 | 33 | nan | nan | nan | Cerrado | 28.8 |
| 4d992e0f-853e-3033-8df5-d46791ba25c3 | -7.63765 | -44.56789 | 2025-10-24 12:19:00 | TERRA_M-T | URUÇUÍ | PIAUÍ | Brasil | 2211209 | 22 | 33 | nan | nan | nan | Cerrado | 8.0 |
| 03f5f0be-23f4-340f-b62d-8171cec82a60 | -15.69775 | -49.43903 | 2025-10-24 12:19:00 | TERRA_M-T | JARAGUÁ | GOIÁS | Brasil | 5211800 | 52 | 33 | nan | nan | nan | Cerrado | 8.0 |
| 380caa84-7a09-3d93-8463-063037208889 | -7.93019 | -48.09603 | 2025-10-24 12:19:00 | TERRA_M-T | PALMEIRANTE | TOCANTINS | Brasil | 1715705 | 17 | 33 | nan | nan | nan | Cerrado | 4.4 |
| bbe44818-c9e3-3b56-ae5b-65e09b939076 | -11.05009 | -47.89674 | 2025-10-24 12:19:00 | TERRA_M-T | MONTE DO CARMO | TOCANTINS | Brasil | 1713601 | 17 | 33 | nan | nan | nan | Cerrado | 6.7 |
| 71732e96-f64f-39b8-bf6b-67d9af9b6bd2 | -9.26719 | -45.3527 | 2025-10-24 12:19:00 | TERRA_M-T | GILBUÉS | PIAUÍ | Brasil | 2204402 | 22 | 33 | nan | nan | nan | Cerrado | 19.4 |
| b0273b82-2384-37a2-b957-9058f3ed7d83 | -13.30529 | -47.44832 | 2025-10-24 12:19:00 | TERRA_M-T | CAVALCANTE | GOIÁS | Brasil | 5205307 | 52 | 33 | nan | nan | nan | Cerrado | 14.1 |
| ca6f861a-8f94-3c95-a43a-24d311ec4f3c | -7.45315 | -49.40764 | 2025-10-24 12:19:00 | TERRA_M-T | FLORESTA DO ARAGUAIA | PARÁ | Brasil | 1503044 | 15 | 33 | nan | nan | nan | Amazônia | 21.4 |
| 3a789a66-1e62-3e86-adcc-2eda3437abe9 | -7.78709 | -45.40057 | 2025-10-24 12:19:00 | TERRA_M-T | RIBEIRO GONÇALVES | PIAUÍ | Brasil | 2208908 | 22 | 33 | nan | nan | nan | Cerrado | 27.7 |
| 264e2f21-feaf-3ba2-aa30-379a454a66e0 | -9.52544 | -49.24862 | 2025-10-24 12:19:00 | TERRA_M-T | ABREULÂNDIA | TOCANTINS | Brasil | 1700251 | 17 | 33 | nan | nan | nan | Cerrado | 5.9 |
| b4366d1b-f492-335b-a6fe-0bf462b501db | -12.8182 | -48.62325 | 2025-10-24 12:19:00 | TERRA_M-T | JAÚ DO TOCANTINS | TOCANTINS | Brasil | 1711506 | 17 | 33 | nan | nan | nan | Cerrado | 7.3 |
| bf898e70-fb82-3508-abca-6f35770582a0 | -7.24124 | -49.40323 | 2025-10-24 12:19:00 | TERRA_M-T | RIO MARIA | PARÁ | Brasil | 1506161 | 15 | 33 | nan | nan | nan | Amazônia | 10.5 |
| 7dd2d969-a5ad-3c2e-9fe4-bfa655a6177a | -13.36324 | -47.96063 | 2025-10-24 12:19:00 | TERRA_M-T | CAVALCANTE | GOIÁS | Brasil | 5205307 | 52 | 33 | nan | nan | nan | Cerrado | 12.5 |
| a820cdc1-c07e-3342-9db0-51b60a3927a9 | -7.8505 | -49.65229 | 2025-10-24 12:19:00 | TERRA_M-T | FLORESTA DO ARAGUAIA | PARÁ | Brasil | 1503044 | 15 | 33 | nan | nan | nan | Amazônia | 8.7 |
| eaf73163-f692-394b-bcc2-7b9b9c1b822c | -14.93829 | -47.68743 | 2025-10-24 12:19:00 | TERRA_M-T | ÁGUA FRIA DE GOIÁS | GOIÁS | Brasil | 5200175 | 52 | 33 | nan | nan | nan | Cerrado | 112.4 |
| 92c5300e-ae8c-3e0a-9948-d3efd4d06527 | -14.73232 | -46.60582 | 2025-10-24 12:19:00 | TERRA_M-T | ALVORADA DO NORTE | GOIÁS | Brasil | 5200803 | 52 | 33 | nan | nan | nan | Cerrado | 10.2 |
| cfbf7482-0863-3c95-b821-641dfbd47a4a | -14.47614 | -47.90575 | 2025-10-24 12:19:00 | TERRA_M-T | NIQUELÂNDIA | GOIÁS | Brasil | 5214606 | 52 | 33 | nan | nan | nan | Cerrado | 7.4 |
| 8899e46a-c7e9-36f8-b276-08891e7144ab | -12.11846 | -46.70765 | 2025-10-24 12:19:00 | TERRA_M-T | PONTE ALTA DO BOM JESUS | TOCANTINS | Brasil | 1717800 | 17 | 33 | nan | nan | nan | Cerrado | 12.9 |
| cd08d1f7-0ebf-3688-b3f6-e4321a978d5a | -8.16271 | -48.72647 | 2025-10-24 12:19:00 | TERRA_M-T | BANDEIRANTES DO TOCANTINS | TOCANTINS | Brasil | 1703057 | 17 | 33 | nan | nan | nan | Amazônia | 10.0 |


[Clique aqui para ver as próximas entradas](README57.md)
