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

## Dados Diários - Página 50

| ID | Latitude | Longitude | Data/Hora GMT | Satélite | Município | Estado | País | Município ID | Estado ID | País ID | Dias sem Chuva | Precipitação | Risco de Fogo | Bioma | FRP |
|----|----------|-----------|---------------|----------|-----------|--------|------|--------------|-----------|---------|----------------|--------------|----------------|-------|-----|
| 411a7f46-c707-3fd5-a22a-670bdc8d2ff5 | -12.88474 | -46.97775 | 2025-09-29 04:08:00 | NOAA-20 | ARRAIAS | TOCANTINS | Brasil | 1702406 | 17 | 33 | nan | nan | nan | Cerrado | 2.5 |
| 56c8fc75-3e98-32cf-847c-93967ada802d | -15.1672 | -46.41922 | 2025-09-29 04:08:00 | NOAA-20 | BURITIS | MINAS GERAIS | Brasil | 3109303 | 31 | 33 | nan | nan | nan | Cerrado | 2.4 |
| 863999ca-f90a-31c9-a9f6-a7a5f0fbcbce | -15.87051 | -46.83701 | 2025-09-29 04:08:00 | NOAA-20 | CABECEIRAS | GOIÁS | Brasil | 5204003 | 52 | 33 | nan | nan | nan | Cerrado | 3.1 |
| 0be6ea64-8fff-337f-b465-99ce40a2880c | -13.01095 | -49.45095 | 2025-09-29 04:08:00 | NOAA-20 | ARAGUAÇU | TOCANTINS | Brasil | 1702000 | 17 | 33 | nan | nan | nan | Cerrado | 4.4 |
| 2e848c9f-450b-3be4-970c-8af299c5dfe8 | -14.55894 | -44.97401 | 2025-09-29 04:08:00 | NOAA-20 | COCOS | BAHIA | Brasil | 2908101 | 29 | 33 | nan | nan | nan | Cerrado | 0.6 |
| c7f9104f-745c-3058-bb10-0df380ca188f | -14.47598 | -48.57396 | 2025-09-29 04:08:00 | NOAA-20 | NIQUELÂNDIA | GOIÁS | Brasil | 5214606 | 52 | 33 | nan | nan | nan | Cerrado | 1.5 |
| a8a615ad-eb70-3812-af9c-b622b38e8994 | -11.43782 | -45.04015 | 2025-09-29 04:08:00 | NOAA-20 | RIACHÃO DAS NEVES | BAHIA | Brasil | 2926202 | 29 | 33 | nan | nan | nan | Cerrado | 3.2 |
| 108e04f8-07f9-3cc7-a2e9-7ea561295288 | -7.88873 | -49.27924 | 2025-09-29 04:08:00 | NOAA-20 | CONCEIÇÃO DO ARAGUAIA | PARÁ | Brasil | 1502707 | 15 | 33 | nan | nan | nan | Amazônia | 1.5 |
| 9ef7eae8-09de-3aa8-a2a9-1970bb0a53a9 | -12.75812 | -46.85675 | 2025-09-29 04:08:00 | NOAA-20 | ARRAIAS | TOCANTINS | Brasil | 1702406 | 17 | 33 | nan | nan | nan | Cerrado | 4.2 |
| df593619-4d0c-30aa-b242-71444a857b7a | -10.02169 | -52.09804 | 2025-09-29 04:08:00 | NOAA-20 | VILA RICA | MATO GROSSO | Brasil | 5108600 | 51 | 33 | nan | nan | nan | Amazônia | 1.3 |
| 4ecf76c5-3479-3ee1-b2b2-9bca39bb17b2 | -11.26792 | -47.20019 | 2025-09-29 04:08:00 | NOAA-20 | ALMAS | TOCANTINS | Brasil | 1700400 | 17 | 33 | nan | nan | nan | Cerrado | 5.5 |
| 1c242b4b-5788-3b11-8c7d-268a5da224db | -12.69983 | -46.90052 | 2025-09-29 04:08:00 | NOAA-20 | ARRAIAS | TOCANTINS | Brasil | 1702406 | 17 | 33 | nan | nan | nan | Cerrado | 4.8 |
| 35732ac8-12fc-3d01-a42d-b8e6ddf27ec5 | -13.58051 | -47.29144 | 2025-09-29 04:08:00 | NOAA-20 | TERESINA DE GOIÁS | GOIÁS | Brasil | 5221080 | 52 | 33 | nan | nan | nan | Cerrado | 2.6 |
| 98e272b2-b419-3d82-a99d-df41f726560b | -11.35206 | -45.07499 | 2025-09-29 04:08:00 | NOAA-20 | FORMOSA DO RIO PRETO | BAHIA | Brasil | 2911105 | 29 | 33 | nan | nan | nan | Cerrado | 1.3 |
| 1d3b9e1a-a499-32d8-9059-72512b8c0bb9 | -11.81641 | -51.80503 | 2025-09-29 04:08:00 | NOAA-20 | ALTO BOA VISTA | MATO GROSSO | Brasil | 5100359 | 51 | 33 | nan | nan | nan | Amazônia | 0.8 |
| 874446d2-e3c2-3212-9004-018232c7f811 | -10.54088 | -43.6244 | 2025-09-29 04:08:00 | NOAA-20 | BURITIRAMA | BAHIA | Brasil | 2904753 | 29 | 33 | nan | nan | nan | Cerrado | 1.1 |
| abd6bfc1-1194-34d1-b56e-dc20070ebff5 | -9.31537 | -45.69163 | 2025-09-29 04:08:00 | NOAA-20 | SANTA FILOMENA | PIAUÍ | Brasil | 2209203 | 22 | 33 | nan | nan | nan | Cerrado | 2.3 |
| 78cc98c4-cd37-3b85-8a98-f929dd868d82 | -15.90646 | -46.23257 | 2025-09-29 04:08:00 | NOAA-20 | ARINOS | MINAS GERAIS | Brasil | 3104502 | 31 | 33 | nan | nan | nan | Cerrado | 1.8 |
| 7d4be50d-1019-3eb3-bced-fa4c3dfb398c | -9.94332 | -48.79809 | 2025-09-29 04:08:00 | NOAA-20 | BARROLÂNDIA | TOCANTINS | Brasil | 1703107 | 17 | 33 | nan | nan | nan | Cerrado | 2.4 |
| f1077722-086c-35c0-8ae7-caa4735a3ba4 | -10.07071 | -43.59614 | 2025-09-29 04:08:00 | NOAA-20 | PILÃO ARCADO | BAHIA | Brasil | 2924405 | 29 | 33 | nan | nan | nan | Cerrado | 0.7 |
| 6b5d3f03-2303-3e26-b669-17f75d8e80fc | -14.96592 | -47.26138 | 2025-09-29 04:08:00 | NOAA-20 | FORMOSA | GOIÁS | Brasil | 5208004 | 52 | 33 | nan | nan | nan | Cerrado | 0.8 |
| 30e1215c-c005-3492-a5e5-d6f4c7c39859 | -13.81814 | -47.4836 | 2025-09-29 04:08:00 | NOAA-20 | CAVALCANTE | GOIÁS | Brasil | 5205307 | 52 | 33 | nan | nan | nan | Cerrado | 1.3 |
| b1e978c6-1c07-3ad9-b458-c5e9053e2b03 | -13.8334 | -47.48661 | 2025-09-29 04:08:00 | NOAA-20 | CAVALCANTE | GOIÁS | Brasil | 5205307 | 52 | 33 | nan | nan | nan | Cerrado | 1.5 |
| 6a0b9a8b-30ec-3d2a-9c30-93c32bced60a | -15.24304 | -40.44523 | 2025-09-29 04:08:00 | NOAA-20 | ITAMBÉ | BAHIA | Brasil | 2915809 | 29 | 33 | nan | nan | nan | Mata Atlântica | 0.5 |
| 20558254-0211-33ed-8bc3-7b9ca1878975 | -12.35061 | -54.15705 | 2025-09-29 04:08:00 | NOAA-20 | NOVA UBIRATÃ | MATO GROSSO | Brasil | 5106240 | 51 | 33 | nan | nan | nan | Amazônia | 1.3 |
| f20d8705-cb3b-39ac-b51b-2add1dc6f8e9 | -14.5808 | -48.22518 | 2025-09-29 04:08:00 | NOAA-20 | NIQUELÂNDIA | GOIÁS | Brasil | 5214606 | 52 | 33 | nan | nan | nan | Cerrado | 3.0 |
| fc993f6b-0363-3563-88b1-23998d6eaf7f | -13.57631 | -48.10107 | 2025-09-29 04:08:00 | NOAA-20 | CAVALCANTE | GOIÁS | Brasil | 5205307 | 52 | 33 | nan | nan | nan | Cerrado | 3.4 |
| 13b42f3c-f830-38c7-8c91-3fff32bbe855 | -12.97205 | -46.24553 | 2025-09-29 04:08:00 | NOAA-20 | CAMPOS BELOS | GOIÁS | Brasil | 5204904 | 52 | 33 | nan | nan | nan | Cerrado | 3.0 |
| 75155b14-b82a-369c-b792-135cf1df4def | -13.00597 | -49.43068 | 2025-09-29 04:08:00 | NOAA-20 | ARAGUAÇU | TOCANTINS | Brasil | 1702000 | 17 | 33 | nan | nan | nan | Cerrado | 1.6 |
| 6e3b85e1-3459-3118-baa0-88544ebb8979 | -14.66469 | -48.16582 | 2025-09-29 04:08:00 | NOAA-20 | NIQUELÂNDIA | GOIÁS | Brasil | 5214606 | 52 | 33 | nan | nan | nan | Cerrado | 0.7 |
| 45dc782e-5816-30c9-8daa-7b077edf867c | -14.47532 | -48.57809 | 2025-09-29 04:08:00 | NOAA-20 | NIQUELÂNDIA | GOIÁS | Brasil | 5214606 | 52 | 33 | nan | nan | nan | Cerrado | 0.5 |
| 80b7c430-cce2-3b7b-a1f2-649e530dabd0 | -16.3671 | -41.58941 | 2025-09-29 04:08:00 | NOAA-20 | MEDINA | MINAS GERAIS | Brasil | 3141405 | 31 | 33 | nan | nan | nan | Mata Atlântica | 0.4 |
| 0d62c5fe-f1be-3aa8-b65c-8503d5a68bc3 | -12.1762 | -43.55892 | 2025-09-29 04:08:00 | NOAA-20 | MUQUÉM DO SÃO FRANCISCO | BAHIA | Brasil | 2922250 | 29 | 33 | nan | nan | nan | Cerrado | 3.0 |
| 33940732-ef60-3604-976c-039477168467 | -8.88426 | -45.02969 | 2025-09-29 04:08:00 | NOAA-20 | BAIXA GRANDE DO RIBEIRO | PIAUÍ | Brasil | 2201150 | 22 | 33 | nan | nan | nan | Cerrado | 2.3 |
| 3c2464ee-3054-3b0c-9c85-5f1f470d9c6b | -11.62168 | -52.85308 | 2025-09-29 04:08:00 | NOAA-20 | QUERÊNCIA | MATO GROSSO | Brasil | 5107065 | 51 | 33 | nan | nan | nan | Amazônia | 3.5 |
| e9a5b0c0-999f-3dfc-9b75-c930c351856e | -13.61691 | -47.30765 | 2025-09-29 04:08:00 | NOAA-20 | TERESINA DE GOIÁS | GOIÁS | Brasil | 5221080 | 52 | 33 | nan | nan | nan | Cerrado | 3.8 |
| 58b3f721-a866-303d-b154-342df76ce61e | -15.08593 | -48.33064 | 2025-09-29 04:08:00 | NOAA-20 | MIMOSO DE GOIÁS | GOIÁS | Brasil | 5213053 | 52 | 33 | nan | nan | nan | Cerrado | 1.5 |
| 5bbba00e-8311-3789-a2a8-0fd92a3e90e5 | -9.04636 | -46.70385 | 2025-09-29 04:08:00 | NOAA-20 | BALSAS | MARANHÃO | Brasil | 2101400 | 21 | 33 | nan | nan | nan | Cerrado | 3.8 |
| d782c54e-a995-30a7-9b29-4c5b73c19081 | -11.9284 | -48.03378 | 2025-09-29 04:08:00 | NOAA-20 | SÃO VALÉRIO | TOCANTINS | Brasil | 1720499 | 17 | 33 | nan | nan | nan | Cerrado | 13.7 |
| bd0e6865-65f4-3343-a0e8-c8b0a8697c21 | -9.99566 | -45.40803 | 2025-09-29 04:08:00 | NOAA-20 | SÃO GONÇALO DO GURGUÉIA | PIAUÍ | Brasil | 2209757 | 22 | 33 | nan | nan | nan | Cerrado | 1.7 |
| 4c97b665-effe-3070-aace-39ce827cc8e4 | -9.08565 | -47.6388 | 2025-09-29 04:08:00 | NOAA-20 | BOM JESUS DO TOCANTINS | TOCANTINS | Brasil | 1703305 | 17 | 33 | nan | nan | nan | Cerrado | 1.6 |
| 9c1cbb52-776c-39d8-a378-56b553d4ac05 | -11.45388 | -44.98653 | 2025-09-29 04:08:00 | NOAA-20 | RIACHÃO DAS NEVES | BAHIA | Brasil | 2926202 | 29 | 33 | nan | nan | nan | Cerrado | 3.4 |
| 2aefac83-a9a5-33da-8486-36fa8a3a5561 | -14.53553 | -48.43034 | 2025-09-29 04:08:00 | NOAA-20 | NIQUELÂNDIA | GOIÁS | Brasil | 5214606 | 52 | 33 | nan | nan | nan | Cerrado | 5.4 |
| 96e55d80-1163-32ef-a5b7-54cd0aff82c4 | -13.41637 | -48.20437 | 2025-09-29 04:08:00 | NOAA-20 | MINAÇU | GOIÁS | Brasil | 5213087 | 52 | 33 | nan | nan | nan | Cerrado | 3.0 |
| 6d9f9bb2-d662-3f68-bcf7-c5343b8b0f3e | -10.04908 | -50.19687 | 2025-09-29 04:08:00 | NOAA-20 | PIUM | TOCANTINS | Brasil | 1717503 | 17 | 33 | nan | nan | nan | Cerrado | 3.7 |
| 80dba7bc-dec3-3806-bf76-4e6f0f5a1928 | -10.69347 | -48.75047 | 2025-09-29 04:08:00 | NOAA-20 | PORTO NACIONAL | TOCANTINS | Brasil | 1718204 | 17 | 33 | nan | nan | nan | Cerrado | 2.6 |
| 85eaae74-5b50-3bb7-84f8-f012a7ac8e32 | -15.5424 | -47.87446 | 2025-09-29 04:08:00 | NOAA-20 | BRASÍLIA | DISTRITO FEDERAL | Brasil | 5300108 | 53 | 33 | nan | nan | nan | Cerrado | 3.6 |
| 066fb10e-3288-33c3-b247-e7e3496aea6f | -15.28994 | -46.41789 | 2025-09-29 04:08:00 | NOAA-20 | BURITIS | MINAS GERAIS | Brasil | 3109303 | 31 | 33 | nan | nan | nan | Cerrado | 1.5 |
| 7bf857b8-14e7-3a62-b5ed-9c6c44b38ff6 | -14.52143 | -48.3941 | 2025-09-29 04:08:00 | NOAA-20 | NIQUELÂNDIA | GOIÁS | Brasil | 5214606 | 52 | 33 | nan | nan | nan | Cerrado | 5.4 |
| 6f06178a-b3c2-3cd9-8b81-7b83818439ad | -14.72063 | -45.71063 | 2025-09-29 04:08:00 | NOAA-20 | COCOS | BAHIA | Brasil | 2908101 | 29 | 33 | nan | nan | nan | Cerrado | 0.8 |
| 6842ca4e-6b25-3b6b-8ed4-30c2484fb300 | -13.4204 | -48.2051 | 2025-09-29 04:08:00 | NOAA-20 | MINAÇU | GOIÁS | Brasil | 5213087 | 52 | 33 | nan | nan | nan | Cerrado | 2.4 |
| 85d63fa0-f604-3b74-b40e-30905759dd69 | -11.44196 | -45.03679 | 2025-09-29 04:08:00 | NOAA-20 | RIACHÃO DAS NEVES | BAHIA | Brasil | 2926202 | 29 | 33 | nan | nan | nan | Cerrado | 2.0 |
| 7211ce57-fe2e-3043-b096-b546a81f20d9 | -15.48165 | -45.88533 | 2025-09-29 04:08:00 | NOAA-20 | ARINOS | MINAS GERAIS | Brasil | 3104502 | 31 | 33 | nan | nan | nan | Cerrado | 1.2 |
| 1a8b6748-ed71-3e11-a973-56b770aa9ff7 | -13.84 | -47.97054 | 2025-09-29 04:08:00 | NOAA-20 | CAVALCANTE | GOIÁS | Brasil | 5205307 | 52 | 33 | nan | nan | nan | Cerrado | 1.5 |
| c7dbb2ee-7af8-35a3-baee-0452334a1987 | -12.87521 | -47.10163 | 2025-09-29 04:08:00 | NOAA-20 | ARRAIAS | TOCANTINS | Brasil | 1702406 | 17 | 33 | nan | nan | nan | Cerrado | 2.6 |
| c89cd69b-073c-32bb-8350-eca6db1370c4 | -9.44211 | -50.90211 | 2025-09-29 04:08:00 | NOAA-20 | SANTANA DO ARAGUAIA | PARÁ | Brasil | 1506708 | 15 | 33 | nan | nan | nan | Amazônia | 0.9 |
| 3f0c1a1f-8f21-3b99-9531-eecb4cb288f3 | -11.36317 | -45.07294 | 2025-09-29 04:08:00 | NOAA-20 | FORMOSA DO RIO PRETO | BAHIA | Brasil | 2911105 | 29 | 33 | nan | nan | nan | Cerrado | 6.4 |
| e7cb4f78-d6f7-3e40-b849-bf6cba64c5e4 | -15.1908 | -48.46532 | 2025-09-29 04:08:00 | NOAA-20 | PADRE BERNARDO | GOIÁS | Brasil | 5215603 | 52 | 33 | nan | nan | nan | Cerrado | 2.0 |
| 16b588fb-1df9-386e-8a31-6ee0a0a3eeea | -9.28883 | -45.69157 | 2025-09-29 04:08:00 | NOAA-20 | SANTA FILOMENA | PIAUÍ | Brasil | 2209203 | 22 | 33 | nan | nan | nan | Cerrado | 3.8 |
| 93401acf-72ae-31e5-9163-a03fcb44662e | -9.40741 | -54.7053 | 2025-09-29 04:08:00 | NOAA-20 | NOVO PROGRESSO | PARÁ | Brasil | 1505031 | 15 | 33 | nan | nan | nan | Amazônia | 3.5 |
| 96cce192-48e7-3e24-a600-a54f5de2a104 | -10.82095 | -47.93398 | 2025-09-29 04:08:00 | NOAA-20 | MONTE DO CARMO | TOCANTINS | Brasil | 1713601 | 17 | 33 | nan | nan | nan | Cerrado | 1.3 |
| 8f8d1003-750e-343e-b7c7-e138f569bb44 | -8.66434 | -49.42894 | 2025-09-29 04:08:00 | NOAA-20 | ARAGUACEMA | TOCANTINS | Brasil | 1701903 | 17 | 33 | nan | nan | nan | Cerrado | 5.0 |
| ccbdc7b8-e5a7-3c9e-925b-825bcd1ac84b | -9.54076 | -51.36211 | 2025-09-29 04:08:00 | NOAA-20 | CUMARU DO NORTE | PARÁ | Brasil | 1502764 | 15 | 33 | nan | nan | nan | Amazônia | 0.8 |
| 51aa9b9f-f12c-3930-a461-043fd06a3e75 | -12.79658 | -47.76351 | 2025-09-29 04:08:00 | NOAA-20 | PARANÃ | TOCANTINS | Brasil | 1716208 | 17 | 33 | nan | nan | nan | Cerrado | 1.8 |
| 85c0a1b6-508d-3caf-9aa3-e9075a7efc69 | -10.03751 | -52.10498 | 2025-09-29 04:08:00 | NOAA-20 | VILA RICA | MATO GROSSO | Brasil | 5108600 | 51 | 33 | nan | nan | nan | Amazônia | 2.3 |
| 9bce0a3b-e9cd-3e9a-a7e6-7b72f3c82522 | -8.88379 | -45.04479 | 2025-09-29 04:08:00 | NOAA-20 | BAIXA GRANDE DO RIBEIRO | PIAUÍ | Brasil | 2201150 | 22 | 33 | nan | nan | nan | Cerrado | 1.7 |
| c0527261-4587-36d5-9e1b-9469ecb4637c | -12.85985 | -45.16607 | 2025-09-29 04:08:00 | NOAA-20 | SÃO DESIDÉRIO | BAHIA | Brasil | 2928901 | 29 | 33 | nan | nan | nan | Cerrado | 0.5 |
| a2d2a56f-86ce-3ed0-85e3-0b6433432a18 | -13.82486 | -47.49023 | 2025-09-29 04:08:00 | NOAA-20 | CAVALCANTE | GOIÁS | Brasil | 5205307 | 52 | 33 | nan | nan | nan | Cerrado | 2.5 |
| 9397cc3e-35a2-380b-9b96-ab6a69b17967 | -15.27533 | -48.04027 | 2025-09-29 04:08:00 | NOAA-20 | PADRE BERNARDO | GOIÁS | Brasil | 5215603 | 52 | 33 | nan | nan | nan | Cerrado | 0.7 |
| a807d66b-a6b2-3aff-9f1e-afc784a548f0 | -14.54688 | -48.43631 | 2025-09-29 04:08:00 | NOAA-20 | NIQUELÂNDIA | GOIÁS | Brasil | 5214606 | 52 | 33 | nan | nan | nan | Cerrado | 5.5 |
| 2133dc76-2cca-340d-a123-77a54a21e459 | -15.87909 | -46.22385 | 2025-09-29 04:08:00 | NOAA-20 | ARINOS | MINAS GERAIS | Brasil | 3104502 | 31 | 33 | nan | nan | nan | Cerrado | 1.2 |
| 73dbdc91-445d-364a-9f8c-cb57de7a5f47 | -11.91625 | -44.7578 | 2025-09-29 04:08:00 | NOAA-20 | ANGICAL | BAHIA | Brasil | 2901403 | 29 | 33 | nan | nan | nan | Cerrado | 0.8 |
| 49fb2b91-8f8b-32e7-969a-da80c5ca8b56 | -13.24245 | -48.45128 | 2025-09-29 04:08:00 | NOAA-20 | PALMEIRÓPOLIS | TOCANTINS | Brasil | 1715754 | 17 | 33 | nan | nan | nan | Cerrado | 2.1 |
| 00168ca7-daac-39f7-8c61-e78159c28845 | -11.93144 | -48.06457 | 2025-09-29 04:08:00 | NOAA-20 | SÃO VALÉRIO | TOCANTINS | Brasil | 1720499 | 17 | 33 | nan | nan | nan | Cerrado | 5.6 |
| f31fdad8-f208-301d-a989-e793c96e27ae | -8.65737 | -50.09066 | 2025-09-29 04:08:00 | NOAA-20 | SANTA MARIA DAS BARREIRAS | PARÁ | Brasil | 1506583 | 15 | 33 | nan | nan | nan | Amazônia | 2.6 |
| 1e77161c-f55d-369c-8582-e005d7397972 | -11.72567 | -44.42422 | 2025-09-29 04:08:00 | NOAA-20 | COTEGIPE | BAHIA | Brasil | 2909406 | 29 | 33 | nan | nan | nan | Cerrado | 1.8 |
| 754a93c1-5d42-3d5e-bc6b-f5583b8a57f8 | -13.25191 | -48.44578 | 2025-09-29 04:08:00 | NOAA-20 | PALMEIRÓPOLIS | TOCANTINS | Brasil | 1715754 | 17 | 33 | nan | nan | nan | Cerrado | 2.7 |
| e9eefe11-251f-397b-a36f-7c83bf690021 | -12.91942 | -47.15815 | 2025-09-29 04:08:00 | NOAA-20 | ARRAIAS | TOCANTINS | Brasil | 1702406 | 17 | 33 | nan | nan | nan | Cerrado | 2.7 |
| e18cf872-c813-30b9-9710-38f5d09c0f37 | -11.62318 | -52.8455 | 2025-09-29 04:08:00 | NOAA-20 | QUERÊNCIA | MATO GROSSO | Brasil | 5107065 | 51 | 33 | nan | nan | nan | Amazônia | 2.2 |
| b9f251f1-5439-3b6a-a5b5-c9328bb1cc46 | -12.57931 | -41.28487 | 2025-09-29 04:08:00 | NOAA-20 | ANDARAÍ | BAHIA | Brasil | 2901304 | 29 | 33 | nan | nan | nan | Caatinga | 0.9 |
| f47c8e4d-7ad8-347b-8643-d42397e7cee8 | -12.85065 | -46.88331 | 2025-09-29 04:08:00 | NOAA-20 | ARRAIAS | TOCANTINS | Brasil | 1702406 | 17 | 33 | nan | nan | nan | Cerrado | 2.3 |
| 9ae75917-e7d6-31fd-b6c4-73657b9b46e4 | -14.59312 | -44.99923 | 2025-09-29 04:08:00 | NOAA-20 | COCOS | BAHIA | Brasil | 2908101 | 29 | 33 | nan | nan | nan | Cerrado | 1.6 |
| 4e3aa440-68a0-30ed-b5d8-270e40a21139 | -11.43703 | -43.50636 | 2025-09-29 04:08:00 | NOAA-20 | BARRA | BAHIA | Brasil | 2902708 | 29 | 33 | nan | nan | nan | Cerrado | 2.1 |
| 1b7bcacc-22b8-3aba-abc9-4abf0476b29a | -11.43402 | -44.95547 | 2025-09-29 04:08:00 | NOAA-20 | RIACHÃO DAS NEVES | BAHIA | Brasil | 2926202 | 29 | 33 | nan | nan | nan | Cerrado | 3.0 |
| 043ca983-1183-3666-b1b7-c38f402fbc39 | -12.96117 | -46.24368 | 2025-09-29 04:08:00 | NOAA-20 | CAMPOS BELOS | GOIÁS | Brasil | 5204904 | 52 | 33 | nan | nan | nan | Cerrado | 0.8 |
| 73cd5305-72bc-3eb5-8497-90ddaa5e1243 | -8.71472 | -47.98449 | 2025-09-29 04:08:00 | NOAA-20 | SANTA MARIA DO TOCANTINS | TOCANTINS | Brasil | 1718881 | 17 | 33 | nan | nan | nan | Cerrado | 4.0 |
| b9b3f1d1-1be2-38e7-afc9-bfb14d1ac785 | -8.88359 | -45.0338 | 2025-09-29 04:08:00 | NOAA-20 | BAIXA GRANDE DO RIBEIRO | PIAUÍ | Brasil | 2201150 | 22 | 33 | nan | nan | nan | Cerrado | 2.3 |
| 74142bba-4e20-3384-bf0d-92de08c97226 | -12.80027 | -47.74281 | 2025-09-29 04:08:00 | NOAA-20 | PARANÃ | TOCANTINS | Brasil | 1716208 | 17 | 33 | nan | nan | nan | Cerrado | 1.9 |
| d040a466-ab1b-39ed-a8ef-7118e53f5f0e | -11.43914 | -45.0322 | 2025-09-29 04:08:00 | NOAA-20 | RIACHÃO DAS NEVES | BAHIA | Brasil | 2926202 | 29 | 33 | nan | nan | nan | Cerrado | 2.0 |
| 34a4be59-8581-31e4-b2ac-62e24ca038a7 | -10.40551 | -48.14422 | 2025-09-29 04:08:00 | NOAA-20 | PALMAS | TOCANTINS | Brasil | 1721000 | 17 | 33 | nan | nan | nan | Cerrado | 1.8 |
| d7d1f732-05a6-37dd-8fdf-e833c7302f4b | -13.40865 | -48.15439 | 2025-09-29 04:08:00 | NOAA-20 | MINAÇU | GOIÁS | Brasil | 5213087 | 52 | 33 | nan | nan | nan | Cerrado | 1.9 |
| 4db2f139-6cfb-363b-a54d-98d135f3adcb | -15.32229 | -47.91028 | 2025-09-29 04:08:00 | NOAA-20 | PLANALTINA | GOIÁS | Brasil | 5217609 | 52 | 33 | nan | nan | nan | Cerrado | 2.1 |
| 8d876204-dcc5-38e1-a19f-5c01f0cce842 | -13.01533 | -49.45186 | 2025-09-29 04:08:00 | NOAA-20 | ARAGUAÇU | TOCANTINS | Brasil | 1702000 | 17 | 33 | nan | nan | nan | Cerrado | 4.1 |
| 6ddbea70-6154-34e3-93bf-c06c4d4baae8 | -11.83007 | -51.78872 | 2025-09-29 04:08:00 | NOAA-20 | ALTO BOA VISTA | MATO GROSSO | Brasil | 5100359 | 51 | 33 | nan | nan | nan | Amazônia | 14.9 |
| 3e3fbbfc-05ef-39aa-a47b-8f02874a6458 | -11.80332 | -44.91201 | 2025-09-29 04:08:00 | NOAA-20 | RIACHÃO DAS NEVES | BAHIA | Brasil | 2926202 | 29 | 33 | nan | nan | nan | Cerrado | 1.4 |
| fcfda6b7-2bd3-348c-9111-3dd8333b6c4a | -9.63658 | -48.12106 | 2025-09-29 04:08:00 | NOAA-20 | TOCANTÍNIA | TOCANTINS | Brasil | 1721109 | 17 | 33 | nan | nan | nan | Cerrado | 3.5 |
| 55cc7610-8a8a-37a1-a73f-aca8347c1d04 | -12.66349 | -46.90885 | 2025-09-29 04:08:00 | NOAA-20 | ARRAIAS | TOCANTINS | Brasil | 1702406 | 17 | 33 | nan | nan | nan | Cerrado | 1.8 |
| bc0fc4d8-7990-3299-8155-becc4cee39e8 | -11.20923 | -47.7473 | 2025-09-29 04:08:00 | NOAA-20 | PINDORAMA DO TOCANTINS | TOCANTINS | Brasil | 1717008 | 17 | 33 | nan | nan | nan | Cerrado | 3.0 |
| faf66022-cb96-345b-a209-4f7d15b827c6 | -10.04293 | -50.4081 | 2025-09-29 04:08:00 | NOAA-20 | SANTA TEREZINHA | MATO GROSSO | Brasil | 5107776 | 51 | 33 | nan | nan | nan | Amazônia | 1.9 |
| 9c16695d-06ca-3f8b-9de3-1e4e42b05930 | -15.60866 | -46.25394 | 2025-09-29 04:08:00 | NOAA-20 | BURITIS | MINAS GERAIS | Brasil | 3109303 | 31 | 33 | nan | nan | nan | Cerrado | 2.9 |


[Clique aqui para ver as próximas entradas](README51.md)
