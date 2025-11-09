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
| ad3cb1ee-2b76-3765-9924-1ae502e324f1 | -5.28578 | -44.94969 | 2025-11-09 03:49:00 | NOAA-21 | BARRA DO CORDA | MARANHÃO | Brasil | 2101608 | 21 | 33 | nan | nan | nan | Cerrado | 7.6 |
| 33561563-4b90-3334-8bc2-cf1d328f0147 | -4.46215 | -44.64611 | 2025-11-09 03:49:00 | NOAA-21 | TRIZIDELA DO VALE | MARANHÃO | Brasil | 2112233 | 21 | 33 | nan | nan | nan | Cerrado | 17.9 |
| 9f9f2ccc-c96e-3ba1-a8f3-3ea15e51195f | -4.00715 | -44.78536 | 2025-11-09 03:49:00 | NOAA-21 | BACABAL | MARANHÃO | Brasil | 2101202 | 21 | 33 | nan | nan | nan | Amazônia | 1.2 |
| dd4edb20-3b6f-384d-8b82-524e56352f31 | -4.70648 | -46.4601 | 2025-11-09 03:49:00 | NOAA-21 | BURITICUPU | MARANHÃO | Brasil | 2102325 | 21 | 33 | nan | nan | nan | Amazônia | 0.8 |
| 4e0804f3-0514-3e35-8eb8-d2f75e15232f | -4.84264 | -42.37641 | 2025-11-09 03:49:00 | NOAA-21 | ALTOS | PIAUÍ | Brasil | 2200400 | 22 | 33 | nan | nan | nan | Caatinga | 1.4 |
| 3ec703f0-c300-3382-aa3b-35dcfe3bbd64 | -4.58352 | -45.61741 | 2025-11-09 03:49:00 | NOAA-21 | PAULO RAMOS | MARANHÃO | Brasil | 2108108 | 21 | 33 | nan | nan | nan | Cerrado | 1.6 |
| 631dce9c-9e59-3c43-a473-3f6c3d7c8c7c | -4.40234 | -49.66406 | 2025-11-09 03:49:00 | NOAA-21 | NOVO REPARTIMENTO | PARÁ | Brasil | 1505064 | 15 | 33 | nan | nan | nan | Amazônia | 3.0 |
| ab48ca1c-bf9d-3245-95e1-f1e814ff4abd | -10.33401 | -49.63972 | 2025-11-09 03:49:00 | NOAA-21 | PIUM | TOCANTINS | Brasil | 1717503 | 17 | 33 | nan | nan | nan | Cerrado | 32.4 |
| dba496b1-e4f9-35fa-aaad-81a4a6446d22 | -4.14929 | -46.26351 | 2025-11-09 03:49:00 | NOAA-21 | ALTO ALEGRE DO PINDARÉ | MARANHÃO | Brasil | 2100477 | 21 | 33 | nan | nan | nan | Amazônia | 0.8 |
| db7021b4-039f-3e60-890e-4cbafcfe81c1 | -5.32082 | -44.8349 | 2025-11-09 03:49:00 | NOAA-21 | TUNTUM | MARANHÃO | Brasil | 2112308 | 21 | 33 | nan | nan | nan | Cerrado | 0.7 |
| 94d8a870-a2a7-3867-a375-b92ba2707790 | -5.72917 | -46.46878 | 2025-11-09 03:49:00 | NOAA-21 | AMARANTE DO MARANHÃO | MARANHÃO | Brasil | 2100600 | 21 | 33 | nan | nan | nan | Cerrado | 3.4 |
| 239b3351-b020-3f8f-a421-ee43fd8e27c6 | -4.51979 | -45.72649 | 2025-11-09 03:49:00 | NOAA-21 | BREJO DE AREIA | MARANHÃO | Brasil | 2102150 | 21 | 33 | nan | nan | nan | Amazônia | 1.9 |
| b7cc3d85-f2b2-3352-a766-d3a4b02ec5b2 | -6.79511 | -39.42146 | 2025-11-09 03:49:00 | NOAA-21 | VÁRZEA ALEGRE | CEARÁ | Brasil | 2314003 | 23 | 33 | nan | nan | nan | Caatinga | 2.5 |
| dac4bc4a-ebcb-3ab5-81ec-b1e387538429 | -4.70627 | -44.41731 | 2025-11-09 03:49:00 | NOAA-21 | CAPINZAL DO NORTE | MARANHÃO | Brasil | 2102754 | 21 | 33 | nan | nan | nan | Cerrado | 2.1 |
| fe674d20-a250-3e86-bbb7-7b29fb2e6539 | -4.39657 | -49.65615 | 2025-11-09 03:49:00 | NOAA-21 | NOVO REPARTIMENTO | PARÁ | Brasil | 1505064 | 15 | 33 | nan | nan | nan | Amazônia | 3.0 |
| a17485d9-1995-3772-a936-2a725d016bd4 | -6.02029 | -43.77088 | 2025-11-09 03:49:00 | NOAA-21 | PASSAGEM FRANCA | MARANHÃO | Brasil | 2107902 | 21 | 33 | nan | nan | nan | Cerrado | 7.9 |
| 8baa1cf2-5877-3488-b6fe-14d7b22db09a | -3.6416 | -49.87299 | 2025-11-09 03:49:00 | NOAA-21 | BAIÃO | PARÁ | Brasil | 1501204 | 15 | 33 | nan | nan | nan | Amazônia | 4.2 |
| b8ecae01-1b49-3c48-947e-a9bdf8b5d8d6 | -6.70235 | -39.68076 | 2025-11-09 03:49:00 | NOAA-21 | TARRAFAS | CEARÁ | Brasil | 2313252 | 23 | 33 | nan | nan | nan | Caatinga | 2.3 |
| f8037997-d1f4-39d6-94b4-8132d3ca88ca | -6.76265 | -35.44207 | 2025-11-09 03:49:00 | NOAA-21 | SERTÃOZINHO | PARAÍBA | Brasil | 2515930 | 25 | 33 | nan | nan | nan | Caatinga | 1.4 |
| 70817bf8-8595-358d-9f4f-374cb1953617 | -5.40418 | -47.26225 | 2025-11-09 03:49:00 | NOAA-21 | SENADOR LA ROCQUE | MARANHÃO | Brasil | 2111763 | 21 | 33 | nan | nan | nan | Amazônia | 1.5 |
| bdd3f939-a7ed-3fc0-b977-9a38a3b5de42 | -18.36987 | -40.16937 | 2025-11-09 03:49:00 | NOAA-21 | PINHEIROS | ESPÍRITO SANTO | Brasil | 3204104 | 32 | 33 | nan | nan | nan | Mata Atlântica | 0.7 |
| a5e15494-e7c8-396e-a1f1-9f1b695f772d | -5.72983 | -46.46509 | 2025-11-09 03:49:00 | NOAA-21 | AMARANTE DO MARANHÃO | MARANHÃO | Brasil | 2100600 | 21 | 33 | nan | nan | nan | Cerrado | 3.8 |
| e5232868-ac39-3fd0-bab3-8459a7edf077 | -4.63483 | -46.39864 | 2025-11-09 03:49:00 | NOAA-21 | BURITICUPU | MARANHÃO | Brasil | 2102325 | 21 | 33 | nan | nan | nan | Amazônia | 5.7 |
| e3d42130-9adf-3a35-aabd-a2d79a8132f1 | -6.76428 | -35.43141 | 2025-11-09 03:49:00 | NOAA-21 | PIRPIRITUBA | PARAÍBA | Brasil | 2511806 | 25 | 33 | nan | nan | nan | Caatinga | 2.0 |
| dadd2e23-befc-361b-a032-96721135f108 | -5.49342 | -39.07513 | 2025-11-09 03:49:00 | NOAA-21 | QUIXERAMOBIM | CEARÁ | Brasil | 2311405 | 23 | 33 | nan | nan | nan | Caatinga | 4.7 |
| 8ccbe645-52d5-3c0f-8db5-a1baa646804c | -5.09489 | -37.78928 | 2025-11-09 03:49:00 | NOAA-21 | QUIXERÉ | CEARÁ | Brasil | 2311504 | 23 | 33 | nan | nan | nan | Caatinga | 2.0 |
| e8177059-3031-374a-8569-92c26b8a89b8 | -11.73536 | -43.84739 | 2025-11-09 03:49:00 | NOAA-21 | WANDERLEY | BAHIA | Brasil | 2933455 | 29 | 33 | nan | nan | nan | Cerrado | 1.0 |
| f8b24b52-138c-3888-8c1f-e65f8a29f8b5 | -3.86328 | -49.37818 | 2025-11-09 03:49:00 | NOAA-21 | BREU BRANCO | PARÁ | Brasil | 1501782 | 15 | 33 | nan | nan | nan | Amazônia | 4.8 |
| a6afaa23-826a-3e31-979e-0040c87a0bcd | -6.76148 | -35.42733 | 2025-11-09 03:49:00 | NOAA-21 | PIRPIRITUBA | PARAÍBA | Brasil | 2511806 | 25 | 33 | nan | nan | nan | Caatinga | 2.0 |
| fe20b432-de9e-3766-bab1-83ae76757f5f | -6.98611 | -39.07105 | 2025-11-09 03:49:00 | NOAA-21 | AURORA | CEARÁ | Brasil | 2301703 | 23 | 33 | nan | nan | nan | Caatinga | 4.3 |
| 0adfca27-e207-3eca-ac38-ceea7f814c02 | -4.11766 | -47.286 | 2025-11-09 03:49:00 | NOAA-21 | ITINGA DO MARANHÃO | MARANHÃO | Brasil | 2105427 | 21 | 33 | nan | nan | nan | Amazônia | 6.1 |
| fda2c980-bbf7-3376-a563-1b76bcbd9e90 | -4.11074 | -47.28984 | 2025-11-09 03:49:00 | NOAA-21 | ITINGA DO MARANHÃO | MARANHÃO | Brasil | 2105427 | 21 | 33 | nan | nan | nan | Amazônia | 2.1 |
| f96b7a73-24cb-3f78-8e60-b676a1e79ac4 | -4.79976 | -46.01136 | 2025-11-09 03:49:00 | NOAA-21 | ARAME | MARANHÃO | Brasil | 2100956 | 21 | 33 | nan | nan | nan | Amazônia | 2.1 |
| d3d512e0-074a-3dfc-b90f-e0c4e368e8ac | -4.04867 | -46.42969 | 2025-11-09 03:49:00 | NOAA-21 | BOM JARDIM | MARANHÃO | Brasil | 2102002 | 21 | 33 | nan | nan | nan | Amazônia | 6.1 |
| 98dbc6af-4a6f-3a96-a1de-cdb1775410ce | -5.21995 | -42.91449 | 2025-11-09 03:49:00 | NOAA-21 | TIMON | MARANHÃO | Brasil | 2112209 | 21 | 33 | nan | nan | nan | Caatinga | 2.3 |
| b3ac935d-7da7-3324-bc2c-bd821929f5b9 | -9.47577 | -48.74146 | 2025-11-09 03:49:00 | NOAA-21 | MIRANORTE | TOCANTINS | Brasil | 1713304 | 17 | 33 | nan | nan | nan | Cerrado | 2.4 |
| 0204bf48-e904-3b6e-b090-a11d5f1349dd | -4.45147 | -44.6474 | 2025-11-09 03:49:00 | NOAA-21 | SÃO LUÍS GONZAGA DO MARANHÃO | MARANHÃO | Brasil | 2111409 | 21 | 33 | nan | nan | nan | Cerrado | 1.2 |
| 4d596632-03bb-3870-8cfb-f885d9123bd4 | -5.09883 | -37.78621 | 2025-11-09 03:49:00 | NOAA-21 | QUIXERÉ | CEARÁ | Brasil | 2311504 | 23 | 33 | nan | nan | nan | Caatinga | 2.5 |
| 2d2e0b96-372f-3819-8614-22ee1f3ff1f7 | -4.51444 | -45.7196 | 2025-11-09 03:49:00 | NOAA-21 | BREJO DE AREIA | MARANHÃO | Brasil | 2102150 | 21 | 33 | nan | nan | nan | Amazônia | 1.4 |
| ac1c9ec0-9a0d-37ba-9773-17b119aa2352 | -5.89421 | -43.96363 | 2025-11-09 03:49:00 | NOAA-21 | BURITI BRAVO | MARANHÃO | Brasil | 2102309 | 21 | 33 | nan | nan | nan | Cerrado | 2.0 |
| 7e93b0ba-ce8b-3b27-8fb4-de9d9377dc2c | -4.96241 | -44.94571 | 2025-11-09 03:49:00 | NOAA-21 | ESPERANTINÓPOLIS | MARANHÃO | Brasil | 2104008 | 21 | 33 | nan | nan | nan | Cerrado | 22.7 |
| da18c55f-0da2-3c13-9182-028a7bb4974b | -3.46495 | -48.8171 | 2025-11-09 03:49:00 | NOAA-21 | IPIXUNA DO PARÁ | PARÁ | Brasil | 1503457 | 15 | 33 | nan | nan | nan | Amazônia | 1.9 |
| 8342c7f0-2d51-3185-8f24-381893077cd2 | -13.20761 | -44.56425 | 2025-11-09 03:49:00 | NOAA-21 | SANTA MARIA DA VITÓRIA | BAHIA | Brasil | 2928109 | 29 | 33 | nan | nan | nan | Cerrado | 2.7 |
| 2c5c92b8-41d1-3d33-9291-bf93f2064518 | -4.68608 | -45.84584 | 2025-11-09 03:49:00 | NOAA-21 | MARAJÁ DO SENA | MARANHÃO | Brasil | 2106359 | 21 | 33 | nan | nan | nan | Amazônia | 1.6 |
| e3da7be5-e992-3294-ae84-377a54d6790e | -5.09826 | -37.78981 | 2025-11-09 03:49:00 | NOAA-21 | QUIXERÉ | CEARÁ | Brasil | 2311504 | 23 | 33 | nan | nan | nan | Caatinga | 1.3 |
| d5ee801c-69ad-3230-b5ed-1bb9ad22d7f3 | -10.34136 | -49.6358 | 2025-11-09 03:49:00 | NOAA-21 | PIUM | TOCANTINS | Brasil | 1717503 | 17 | 33 | nan | nan | nan | Cerrado | 32.4 |
| 75ca4668-cf8e-308c-93f6-2b1bcbfa9986 | -4.72365 | -42.93167 | 2025-11-09 03:49:00 | NOAA-21 | CAXIAS | MARANHÃO | Brasil | 2103000 | 21 | 33 | nan | nan | nan | Cerrado | 2.9 |
| 14a2765f-370a-3f51-8cf9-edf25cdf7958 | -4.11687 | -47.29061 | 2025-11-09 03:49:00 | NOAA-21 | ITINGA DO MARANHÃO | MARANHÃO | Brasil | 2105427 | 21 | 33 | nan | nan | nan | Amazônia | 5.0 |
| 188d058e-6d0e-39a3-a027-78673239eb05 | -5.49553 | -45.86172 | 2025-11-09 03:49:00 | NOAA-21 | GRAJAÚ | MARANHÃO | Brasil | 2104800 | 21 | 33 | nan | nan | nan | Cerrado | 1.5 |
| a9464a9e-f41f-3866-be5f-7d5744c278da | -14.4153 | -43.18572 | 2025-11-09 03:49:00 | NOAA-21 | PALMAS DE MONTE ALTO | BAHIA | Brasil | 2923407 | 29 | 33 | nan | nan | nan | Cerrado | 0.9 |
| 229e0c2a-5661-3b52-87e0-1a7723421c1f | -5.3843 | -44.72918 | 2025-11-09 03:49:00 | NOAA-21 | TUNTUM | MARANHÃO | Brasil | 2112308 | 21 | 33 | nan | nan | nan | Cerrado | 8.0 |
| 69e736b4-f9af-3fbc-9a5f-c70215a0c7fc | -6.4297 | -39.70183 | 2025-11-09 03:49:00 | NOAA-21 | JUCÁS | CEARÁ | Brasil | 2307403 | 23 | 33 | nan | nan | nan | Caatinga | 1.1 |
| f9a9b7ea-f33c-3349-870d-3c9add58f97f | -4.51867 | -45.72789 | 2025-11-09 03:49:00 | NOAA-21 | BREJO DE AREIA | MARANHÃO | Brasil | 2102150 | 21 | 33 | nan | nan | nan | Amazônia | 1.5 |
| de265a22-b609-3440-815d-966a10316315 | -4.14358 | -46.26262 | 2025-11-09 03:49:00 | NOAA-21 | ALTO ALEGRE DO PINDARÉ | MARANHÃO | Brasil | 2100477 | 21 | 33 | nan | nan | nan | Amazônia | 1.4 |
| 0b81cec3-a8d4-3a4e-b157-21fc8184efff | -10.714 | -47.73727 | 2025-11-09 03:49:00 | NOAA-21 | PONTE ALTA DO TOCANTINS | TOCANTINS | Brasil | 1717909 | 17 | 33 | nan | nan | nan | Cerrado | 1.2 |
| f4f557aa-68aa-3fad-a46a-078f9bb246a2 | -12.15967 | -48.00841 | 2025-11-09 03:49:00 | NOAA-21 | PARANÃ | TOCANTINS | Brasil | 1716208 | 17 | 33 | nan | nan | nan | Cerrado | 0.7 |
| 779f1da0-4e98-3388-b3ca-3717c454131e | -4.91075 | -44.64112 | 2025-11-09 03:49:00 | NOAA-21 | JOSELÂNDIA | MARANHÃO | Brasil | 2105609 | 21 | 33 | nan | nan | nan | Cerrado | 1.2 |
| 61075687-6c88-3e3d-b654-2b1041182992 | -4.5829 | -45.62099 | 2025-11-09 03:49:00 | NOAA-21 | PAULO RAMOS | MARANHÃO | Brasil | 2108108 | 21 | 33 | nan | nan | nan | Cerrado | 3.0 |
| 5d2d8df2-69f5-37ac-a1eb-657c0d0764b1 | -3.87017 | -49.37948 | 2025-11-09 03:49:00 | NOAA-21 | BREU BRANCO | PARÁ | Brasil | 1501782 | 15 | 33 | nan | nan | nan | Amazônia | 2.7 |
| b33a96a8-4d20-3406-9f91-dde0366f7eb7 | -3.8955 | -47.18463 | 2025-11-09 03:49:00 | NOAA-21 | ULIANÓPOLIS | PARÁ | Brasil | 1508126 | 15 | 33 | nan | nan | nan | Amazônia | 1.6 |
| de1211d8-6916-3712-839f-f655e6f9e44f | -4.45707 | -44.64525 | 2025-11-09 03:49:00 | NOAA-21 | TRIZIDELA DO VALE | MARANHÃO | Brasil | 2112233 | 21 | 33 | nan | nan | nan | Cerrado | 17.9 |
| 6cc5b874-6434-38ab-afcf-678edc2e6189 | -5.1772 | -37.86862 | 2025-11-09 03:49:00 | NOAA-21 | QUIXERÉ | CEARÁ | Brasil | 2311504 | 23 | 33 | nan | nan | nan | Caatinga | 1.1 |
| 1ec47171-4f2f-3222-a1c4-ba098771001f | -6.85814 | -40.15593 | 2025-11-09 03:49:00 | NOAA-21 | CAMPOS SALES | CEARÁ | Brasil | 2302701 | 23 | 33 | nan | nan | nan | Caatinga | 6.5 |
| 7b7b8ddb-eb37-32a1-9b97-11fcbf14bb71 | -10.41417 | -48.80595 | 2025-11-09 03:49:00 | NOAA-21 | PUGMIL | TOCANTINS | Brasil | 1718451 | 17 | 33 | nan | nan | nan | Cerrado | 2.0 |
| 29a8cc3f-6661-34ac-9ff3-5d25b96b44c6 | -3.75355 | -45.99265 | 2025-11-09 03:49:00 | NOAA-21 | ALTO ALEGRE DO PINDARÉ | MARANHÃO | Brasil | 2100477 | 21 | 33 | nan | nan | nan | Amazônia | 1.5 |
| b80467de-1e06-3bdb-b44b-8b18cecb5c17 | -4.70881 | -46.45741 | 2025-11-09 03:49:00 | NOAA-21 | BURITICUPU | MARANHÃO | Brasil | 2102325 | 21 | 33 | nan | nan | nan | Amazônia | 1.9 |
| 9678593a-14cf-3385-867a-6d2ee772d28b | -11.55429 | -48.55096 | 2025-11-09 03:49:00 | NOAA-21 | PEIXE | TOCANTINS | Brasil | 1716604 | 17 | 33 | nan | nan | nan | Cerrado | 1.2 |
| 72240658-9540-3923-bae1-5b9d718acf0c | -10.33604 | -49.62937 | 2025-11-09 03:49:00 | NOAA-21 | PIUM | TOCANTINS | Brasil | 1717503 | 17 | 33 | nan | nan | nan | Cerrado | 33.2 |
| b0ae8f74-49c6-32dd-8e1c-f42bf8b27a67 | -12.94461 | -43.43067 | 2025-11-09 03:49:00 | NOAA-21 | SÍTIO DO MATO | BAHIA | Brasil | 2930758 | 29 | 33 | nan | nan | nan | Cerrado | 0.6 |
| 27c77957-bfa1-33fb-b611-fdf490e5083c | -4.5455 | -44.60618 | 2025-11-09 03:49:00 | NOAA-21 | PEDREIRAS | MARANHÃO | Brasil | 2108207 | 21 | 33 | nan | nan | nan | Cerrado | 0.9 |
| 12a090f8-43cc-31a9-ae72-0d32c73ae1cd | -4.32596 | -45.69724 | 2025-11-09 03:49:00 | NOAA-21 | BREJO DE AREIA | MARANHÃO | Brasil | 2102150 | 21 | 33 | nan | nan | nan | Amazônia | 2.2 |
| 489d4220-4f9f-3e49-8927-f7cf1641bbf3 | -4.40353 | -49.65742 | 2025-11-09 03:49:00 | NOAA-21 | NOVO REPARTIMENTO | PARÁ | Brasil | 1505064 | 15 | 33 | nan | nan | nan | Amazônia | 3.0 |
| c367b9f0-5e9f-3ec1-a1d7-20b7ea025469 | -12.11054 | -43.64659 | 2025-11-09 03:49:00 | NOAA-21 | MUQUÉM DO SÃO FRANCISCO | BAHIA | Brasil | 2922250 | 29 | 33 | nan | nan | nan | Cerrado | 3.0 |
| a8d280db-9815-3aa2-882c-1a045e8dd977 | -3.79868 | -48.89797 | 2025-11-09 03:49:00 | NOAA-21 | GOIANÉSIA DO PARÁ | PARÁ | Brasil | 1503093 | 15 | 33 | nan | nan | nan | Amazônia | 5.4 |
| 15cf68e5-5f46-322c-894e-9ffa5371cbdf | -4.40291 | -45.97474 | 2025-11-09 03:49:00 | NOAA-21 | SANTA LUZIA | MARANHÃO | Brasil | 2110005 | 21 | 33 | nan | nan | nan | Amazônia | 1.5 |
| 34eb1c9b-bda7-35c4-a9e9-cbe77b7cfc67 | -5.32588 | -44.8359 | 2025-11-09 03:49:00 | NOAA-21 | TUNTUM | MARANHÃO | Brasil | 2112308 | 21 | 33 | nan | nan | nan | Cerrado | 0.7 |
| 343c1574-fd27-3d86-b696-4373e711b0d0 | -10.33296 | -49.64502 | 2025-11-09 03:49:00 | NOAA-21 | PIUM | TOCANTINS | Brasil | 1717503 | 17 | 33 | nan | nan | nan | Cerrado | 3.8 |
| e8d69a84-43a6-34c5-801f-874cb48d2eb3 | -5.65492 | -45.99057 | 2025-11-09 03:49:00 | NOAA-21 | GRAJAÚ | MARANHÃO | Brasil | 2104800 | 21 | 33 | nan | nan | nan | Cerrado | 2.7 |
| 55419cd4-4135-3bfd-9f7d-95ba0ddce5d5 | -7.2773 | -38.72529 | 2025-11-09 03:49:00 | NOAA-21 | MAURITI | CEARÁ | Brasil | 2308104 | 23 | 33 | nan | nan | nan | Caatinga | 1.4 |
| 5d0b5610-6d87-3f30-8631-a42ffc12a687 | -4.64056 | -46.39944 | 2025-11-09 03:49:00 | NOAA-21 | BURITICUPU | MARANHÃO | Brasil | 2102325 | 21 | 33 | nan | nan | nan | Amazônia | 6.7 |
| d656dcfe-97eb-3a14-a3b9-b319848e8b60 | -5.91974 | -39.46891 | 2025-11-09 03:49:00 | NOAA-21 | PIQUET CARNEIRO | CEARÁ | Brasil | 2310902 | 23 | 33 | nan | nan | nan | Caatinga | 1.5 |
| 0510f217-315f-39c5-bbe8-bebc1e0b6fbc | -4.01233 | -44.78621 | 2025-11-09 03:49:00 | NOAA-21 | BACABAL | MARANHÃO | Brasil | 2101202 | 21 | 33 | nan | nan | nan | Amazônia | 0.8 |
| be48e93a-c02e-3cfb-ac7f-09046f878c46 | -4.46165 | -44.64912 | 2025-11-09 03:49:00 | NOAA-21 | TRIZIDELA DO VALE | MARANHÃO | Brasil | 2112233 | 21 | 33 | nan | nan | nan | Cerrado | 14.7 |
| ea02572e-f36a-3978-9356-4fec2d4b4658 | -6.71886 | -39.99867 | 2025-11-09 03:49:00 | NOAA-21 | ANTONINA DO NORTE | CEARÁ | Brasil | 2300804 | 23 | 33 | nan | nan | nan | Caatinga | 3.9 |
| 6abfe7c3-e08f-3cc9-87a4-ccb79fa6f2fe | -17.26572 | -40.26033 | 2025-11-09 03:49:00 | NOAA-21 | MEDEIROS NETO | BAHIA | Brasil | 2921104 | 29 | 33 | nan | nan | nan | Mata Atlântica | 1.6 |
| dbc84f1e-e8ab-3a76-affd-645ae4a5b277 | -4.58835 | -45.62175 | 2025-11-09 03:49:00 | NOAA-21 | PAULO RAMOS | MARANHÃO | Brasil | 2108108 | 21 | 33 | nan | nan | nan | Cerrado | 3.0 |
| 2a0855c2-f262-3079-8e8f-5161670bee87 | -5.13554 | -41.24739 | 2025-11-09 03:49:00 | NOAA-21 | BURITI DOS MONTES | PIAUÍ | Brasil | 2202026 | 22 | 33 | nan | nan | nan | Caatinga | 1.8 |
| 0e8cb453-4bfc-3be9-a130-1a691ed1dae5 | -3.79658 | -48.9099 | 2025-11-09 03:49:00 | NOAA-21 | GOIANÉSIA DO PARÁ | PARÁ | Brasil | 1503093 | 15 | 33 | nan | nan | nan | Amazônia | 2.8 |
| cf9e76de-d9ee-3dcd-996d-f545b3da09ff | -10.41601 | -48.80437 | 2025-11-09 03:49:00 | NOAA-21 | PUGMIL | TOCANTINS | Brasil | 1718451 | 17 | 33 | nan | nan | nan | Cerrado | 4.5 |
| 47307e72-ed35-31fa-97c3-86c01dc1b7d2 | -6.95498 | -40.25389 | 2025-11-09 03:49:00 | NOAA-21 | CAMPOS SALES | CEARÁ | Brasil | 2302701 | 23 | 33 | nan | nan | nan | Caatinga | 1.1 |
| 6da06605-35b6-3b56-9714-f3e8cc980464 | -3.33112 | -49.13205 | 2025-11-09 03:49:00 | NOAA-21 | MOJU | PARÁ | Brasil | 1504703 | 15 | 33 | nan | nan | nan | Amazônia | 1.7 |
| 0b174140-28e0-38ff-9320-470c00a94b6b | -17.28258 | -41.92977 | 2025-11-09 03:49:00 | NOAA-21 | NOVO CRUZEIRO | MINAS GERAIS | Brasil | 3145307 | 31 | 33 | nan | nan | nan | Mata Atlântica | 0.8 |
| 4e20ba7e-f232-3c4e-ab62-f01733e9f6e7 | -4.71454 | -46.45829 | 2025-11-09 03:49:00 | NOAA-21 | BURITICUPU | MARANHÃO | Brasil | 2102325 | 21 | 33 | nan | nan | nan | Amazônia | 2.5 |
| 9c0bc58e-5921-3b2a-864d-f93a7cef40f9 | -12.10985 | -43.6505 | 2025-11-09 03:49:00 | NOAA-21 | MUQUÉM DO SÃO FRANCISCO | BAHIA | Brasil | 2922250 | 29 | 33 | nan | nan | nan | Cerrado | 1.9 |
| 28d66d06-f4dd-3037-a6e7-4e724be48739 | -4.46265 | -44.64315 | 2025-11-09 03:49:00 | NOAA-21 | TRIZIDELA DO VALE | MARANHÃO | Brasil | 2112233 | 21 | 33 | nan | nan | nan | Cerrado | 17.9 |
| 787605eb-7cee-3c52-be22-37284c470651 | -5.28015 | -44.95181 | 2025-11-09 03:49:00 | NOAA-21 | BARRA DO CORDA | MARANHÃO | Brasil | 2101608 | 21 | 33 | nan | nan | nan | Cerrado | 10.1 |
| 72f29fe3-0934-3a6e-8345-65d75899655d | -6.76763 | -35.43194 | 2025-11-09 03:49:00 | NOAA-21 | PIRPIRITUBA | PARAÍBA | Brasil | 2511806 | 25 | 33 | nan | nan | nan | Caatinga | 1.3 |
| 8e1baa1f-6d17-3573-99bb-8588ba108027 | -7.08358 | -35.12695 | 2025-11-09 03:49:00 | NOAA-21 | SAPÉ | PARAÍBA | Brasil | 2515302 | 25 | 33 | nan | nan | nan | Mata Atlântica | 0.7 |
| 529b53f5-ba78-3aa7-9073-f1c965efeec8 | -4.39179 | -45.97276 | 2025-11-09 03:49:00 | NOAA-21 | SANTA LUZIA | MARANHÃO | Brasil | 2110005 | 21 | 33 | nan | nan | nan | Amazônia | 2.3 |
| fdb32b62-dd95-3788-97a2-680253856ded | -5.65387 | -45.99051 | 2025-11-09 03:49:00 | NOAA-21 | GRAJAÚ | MARANHÃO | Brasil | 2104800 | 21 | 33 | nan | nan | nan | Cerrado | 2.9 |


[Clique aqui para ver as próximas entradas](README12.md)
