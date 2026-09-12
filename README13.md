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
| d13de845-4d46-38fa-a97a-474bbf547f34 | -9.78079 | -42.00258 | 2026-09-12 03:49:00 | NOAA-20 | SENTO SÉ | BAHIA | Brasil | 2930204 | 29 | 33 | nan | nan | nan | Caatinga | 2.5 |
| 942d2079-68d2-3874-b0a8-9faa3afc1504 | -9.90578 | -46.2299 | 2026-09-12 03:49:00 | NOAA-20 | ALTO PARNAÍBA | MARANHÃO | Brasil | 2100501 | 21 | 33 | nan | nan | nan | Cerrado | 1.8 |
| 2d1ebf48-0384-3f3c-9471-fb2abf6a6fcf | -11.18579 | -40.88575 | 2026-09-12 03:49:00 | NOAA-20 | VÁRZEA NOVA | BAHIA | Brasil | 2933158 | 29 | 33 | nan | nan | nan | Caatinga | 3.3 |
| 914373bf-6bbd-3c95-8ce6-66c716d5ae06 | -10.372 | -45.12908 | 2026-09-12 03:49:00 | NOAA-20 | CORRENTE | PIAUÍ | Brasil | 2202901 | 22 | 33 | nan | nan | nan | Cerrado | 1.3 |
| 9ce2364c-6177-300d-91bf-ae313d452d56 | -11.40195 | -43.9423 | 2026-09-12 03:49:00 | NOAA-20 | COTEGIPE | BAHIA | Brasil | 2909406 | 29 | 33 | nan | nan | nan | Cerrado | 1.0 |
| cd6dc2af-f527-3b8b-9b99-96dc6b4cbc5e | -3.33025 | -42.30333 | 2026-09-12 03:49:00 | NOAA-20 | SÃO BERNARDO | MARANHÃO | Brasil | 2110609 | 21 | 33 | nan | nan | nan | Cerrado | 6.1 |
| 6b03b6d7-3174-3030-9cd7-c4b00e476a2c | -9.93315 | -48.51982 | 2026-09-12 03:49:00 | NOAA-20 | MIRACEMA DO TOCANTINS | TOCANTINS | Brasil | 1713205 | 17 | 33 | nan | nan | nan | Cerrado | 9.2 |
| c981cee5-0d1f-390c-82a0-75ee34f30c34 | -15.9754 | -40.28126 | 2026-09-12 03:49:00 | NOAA-20 | JORDÂNIA | MINAS GERAIS | Brasil | 3136504 | 31 | 33 | nan | nan | nan | Mata Atlântica | 0.6 |
| 7ae85419-2ef3-312c-8019-cb327320a260 | -10.63026 | -46.12703 | 2026-09-12 03:49:00 | NOAA-20 | FORMOSA DO RIO PRETO | BAHIA | Brasil | 2911105 | 29 | 33 | nan | nan | nan | Cerrado | 1.3 |
| 5758aa51-bd3c-32a5-934f-2cfeef4ec23b | -7.60766 | -46.12497 | 2026-09-12 03:49:00 | NOAA-20 | BALSAS | MARANHÃO | Brasil | 2101400 | 21 | 33 | nan | nan | nan | Cerrado | 0.9 |
| f2f17e2f-2369-3731-9829-1b6be5e8bf31 | -10.63093 | -46.1234 | 2026-09-12 03:49:00 | NOAA-20 | FORMOSA DO RIO PRETO | BAHIA | Brasil | 2911105 | 29 | 33 | nan | nan | nan | Cerrado | 1.3 |
| 7b446763-f663-36af-85a3-ae3e77710fc0 | -11.37107 | -46.83889 | 2026-09-12 03:49:00 | NOAA-20 | RIO DA CONCEIÇÃO | TOCANTINS | Brasil | 1718659 | 17 | 33 | nan | nan | nan | Cerrado | 2.1 |
| 3a1bbbe3-341a-3b4e-a0a0-899f5c7dd4d2 | -12.73717 | -44.73946 | 2026-09-12 03:49:00 | NOAA-20 | SÃO DESIDÉRIO | BAHIA | Brasil | 2928901 | 29 | 33 | nan | nan | nan | Cerrado | 2.5 |
| a46bc8c7-4e0e-348b-abf3-82ccd232d41c | -7.95897 | -44.00507 | 2026-09-12 03:49:00 | NOAA-20 | SEBASTIÃO LEAL | PIAUÍ | Brasil | 2210631 | 22 | 33 | nan | nan | nan | Cerrado | 0.9 |
| a614b38e-42b3-3102-b97d-1f8f425d3307 | -10.35242 | -40.56004 | 2026-09-12 03:49:00 | NOAA-20 | CAMPO FORMOSO | BAHIA | Brasil | 2906006 | 29 | 33 | nan | nan | nan | Caatinga | 1.1 |
| af6909b8-d4ab-32af-83cd-0d18d8a84394 | -11.35631 | -46.28802 | 2026-09-12 03:49:00 | NOAA-20 | FORMOSA DO RIO PRETO | BAHIA | Brasil | 2911105 | 29 | 33 | nan | nan | nan | Cerrado | 2.5 |
| ca8d1bba-c298-3d41-8d96-d1caca1c6a65 | -10.54989 | -45.22113 | 2026-09-12 03:49:00 | NOAA-20 | CORRENTE | PIAUÍ | Brasil | 2202901 | 22 | 33 | nan | nan | nan | Cerrado | 2.2 |
| cbb60cd8-33fb-3eb4-baec-23a7b34481e2 | -11.38977 | -43.98179 | 2026-09-12 03:49:00 | NOAA-20 | MANSIDÃO | BAHIA | Brasil | 2920452 | 29 | 33 | nan | nan | nan | Cerrado | 1.1 |
| 2fba7d75-acc0-317d-b261-0127ddb40d62 | -12.32839 | -46.76386 | 2026-09-12 03:49:00 | NOAA-20 | TAGUATINGA | TOCANTINS | Brasil | 1720903 | 17 | 33 | nan | nan | nan | Cerrado | 2.2 |
| 0a312a94-e547-37cb-bedd-71c64ea8794a | -9.67282 | -46.01704 | 2026-09-12 03:49:00 | NOAA-20 | ALTO PARNAÍBA | MARANHÃO | Brasil | 2100501 | 21 | 33 | nan | nan | nan | Cerrado | 3.9 |
| 2de2332a-acd4-3ec3-8a26-4f1897b2f20c | -14.95067 | -47.52694 | 2026-09-12 03:49:00 | NOAA-20 | FORMOSA | GOIÁS | Brasil | 5208004 | 52 | 33 | nan | nan | nan | Cerrado | 0.8 |
| 58624eb0-97c7-33a5-9a0a-2f4300073339 | -12.11886 | -48.97508 | 2026-09-12 03:49:00 | NOAA-20 | FIGUEIRÓPOLIS | TOCANTINS | Brasil | 1707652 | 17 | 33 | nan | nan | nan | Cerrado | 4.3 |
| ac93b98c-e0c9-3175-98ef-bfe75cfeca2e | -9.53564 | -45.47352 | 2026-09-12 03:49:00 | NOAA-20 | GILBUÉS | PIAUÍ | Brasil | 2204402 | 22 | 33 | nan | nan | nan | Cerrado | 1.3 |
| c709b6b3-271c-32e7-9401-062e02ad0f39 | -9.31337 | -44.3502 | 2026-09-12 03:49:00 | NOAA-20 | BOM JESUS | PIAUÍ | Brasil | 2201903 | 22 | 33 | nan | nan | nan | Cerrado | 1.3 |
| e7f66cee-5e0e-3533-ac1d-8fdb6fbd02da | -12.4441 | -49.5909 | 2026-09-12 03:49:00 | NOAA-20 | SANDOLÂNDIA | TOCANTINS | Brasil | 1718840 | 17 | 33 | nan | nan | nan | Cerrado | 3.1 |
| 5cbc62ab-0ee8-3584-bb26-ad61a3639378 | -9.36924 | -48.41743 | 2026-09-12 03:49:00 | NOAA-20 | MIRACEMA DO TOCANTINS | TOCANTINS | Brasil | 1713205 | 17 | 33 | nan | nan | nan | Cerrado | 1.5 |
| 847519d3-c88d-318e-98b3-539f034b38f8 | -11.36339 | -46.79905 | 2026-09-12 03:49:00 | NOAA-20 | RIO DA CONCEIÇÃO | TOCANTINS | Brasil | 1718659 | 17 | 33 | nan | nan | nan | Cerrado | 2.4 |
| f8d1185f-4f44-3bdb-a938-422cb4a9ed4c | -12.13064 | -48.9582 | 2026-09-12 03:49:00 | NOAA-20 | FIGUEIRÓPOLIS | TOCANTINS | Brasil | 1707652 | 17 | 33 | nan | nan | nan | Cerrado | 5.5 |
| 7a5471c2-7a48-399e-a443-891d652da25f | -12.12038 | -48.97559 | 2026-09-12 03:49:00 | NOAA-20 | FIGUEIRÓPOLIS | TOCANTINS | Brasil | 1707652 | 17 | 33 | nan | nan | nan | Cerrado | 3.2 |
| dd0a04c1-6d78-3939-acc4-8a41e6d09139 | -10.22452 | -50.37096 | 2026-09-12 03:49:00 | NOAA-20 | PIUM | TOCANTINS | Brasil | 1717503 | 17 | 33 | nan | nan | nan | Cerrado | 2.2 |
| 6723beb1-414c-3ed1-a9cf-fd043e066326 | -7.96184 | -44.01797 | 2026-09-12 03:49:00 | NOAA-20 | SEBASTIÃO LEAL | PIAUÍ | Brasil | 2210631 | 22 | 33 | nan | nan | nan | Cerrado | 1.2 |
| b003257c-b609-3691-9426-af1cf098b2ae | -12.20646 | -49.40225 | 2026-09-12 03:49:00 | NOAA-20 | FIGUEIRÓPOLIS | TOCANTINS | Brasil | 1707652 | 17 | 33 | nan | nan | nan | Cerrado | 1.9 |
| 72de6abe-e6a5-3898-94c0-e622490f2ddb | -10.54587 | -45.21394 | 2026-09-12 03:49:00 | NOAA-20 | CORRENTE | PIAUÍ | Brasil | 2202901 | 22 | 33 | nan | nan | nan | Cerrado | 2.3 |
| 18380e43-5bff-3e1e-9ece-6b24d899cf09 | -12.13448 | -48.9716 | 2026-09-12 03:49:00 | NOAA-20 | FIGUEIRÓPOLIS | TOCANTINS | Brasil | 1707652 | 17 | 33 | nan | nan | nan | Cerrado | 3.4 |
| 3e1c8dd9-0fa3-39ed-91e5-2f7af62d3e64 | -4.64797 | -37.89212 | 2026-09-12 03:49:00 | NOAA-20 | ARACATI | CEARÁ | Brasil | 2301109 | 23 | 33 | nan | nan | nan | Caatinga | 3.1 |
| d90f8d45-8574-3aed-b954-008303421636 | -9.46286 | -50.31478 | 2026-09-12 03:49:00 | NOAA-20 | SANTANA DO ARAGUAIA | PARÁ | Brasil | 1506708 | 15 | 33 | nan | nan | nan | Amazônia | 2.8 |
| cb8c0770-1ff2-3588-b5f7-df174f3916c4 | -9.63828 | -49.68556 | 2026-09-12 03:49:00 | NOAA-20 | MARIANÓPOLIS DO TOCANTINS | TOCANTINS | Brasil | 1712504 | 17 | 33 | nan | nan | nan | Cerrado | 4.0 |
| be0effaa-e31f-3e91-b0fe-086cc3491097 | -14.58334 | -48.83437 | 2026-09-12 03:49:00 | NOAA-20 | NIQUELÂNDIA | GOIÁS | Brasil | 5214606 | 52 | 33 | nan | nan | nan | Cerrado | 2.5 |
| 1541400b-f41b-3c05-ba0f-24a12aecb5fb | -9.69483 | -43.40226 | 2026-09-12 03:49:00 | NOAA-20 | PILÃO ARCADO | BAHIA | Brasil | 2924405 | 29 | 33 | nan | nan | nan | Caatinga | 1.5 |
| 8303867f-f831-388e-a07f-d8ac791def2e | -8.03143 | -43.86074 | 2026-09-12 03:49:00 | NOAA-20 | MANOEL EMÍDIO | PIAUÍ | Brasil | 2205904 | 22 | 33 | nan | nan | nan | Caatinga | 6.3 |
| a0b9ffb7-f5a1-3f6a-a0a7-d0d2438ab2c5 | -10.22099 | -45.18634 | 2026-09-12 03:49:00 | NOAA-20 | CORRENTE | PIAUÍ | Brasil | 2202901 | 22 | 33 | nan | nan | nan | Cerrado | 1.7 |
| 8ab321a7-9d55-3187-8574-3ce0d98d2800 | -9.54098 | -45.47461 | 2026-09-12 03:49:00 | NOAA-20 | GILBUÉS | PIAUÍ | Brasil | 2204402 | 22 | 33 | nan | nan | nan | Cerrado | 1.3 |
| 849a0655-43d1-3aa5-9021-79506dd7f311 | -10.55743 | -45.20937 | 2026-09-12 03:49:00 | NOAA-20 | CORRENTE | PIAUÍ | Brasil | 2202901 | 22 | 33 | nan | nan | nan | Cerrado | 1.5 |
| 8d32abb0-6864-3797-993e-ef75d8c0db77 | -12.64388 | -47.09347 | 2026-09-12 03:49:00 | NOAA-20 | ARRAIAS | TOCANTINS | Brasil | 1702406 | 17 | 33 | nan | nan | nan | Cerrado | 3.1 |
| ac8edbb3-15b7-3deb-a07a-94e1bcca1e8e | -3.32521 | -42.29868 | 2026-09-12 03:49:00 | NOAA-20 | SÃO BERNARDO | MARANHÃO | Brasil | 2110609 | 21 | 33 | nan | nan | nan | Cerrado | 7.0 |
| f840808b-dd91-3a97-859c-2075a957098f | -7.92253 | -49.73543 | 2026-09-12 03:49:00 | NOAA-20 | CONCEIÇÃO DO ARAGUAIA | PARÁ | Brasil | 1502707 | 15 | 33 | nan | nan | nan | Amazônia | 2.0 |
| dee01f34-3708-3edf-87c6-cbacfd60a53d | -11.82615 | -39.58595 | 2026-09-12 03:49:00 | NOAA-20 | PÉ DE SERRA | BAHIA | Brasil | 2924058 | 29 | 33 | nan | nan | nan | Caatinga | 1.2 |
| 0eb85736-d265-3dbc-9e6c-c7f19d56cce6 | -3.32542 | -42.3026 | 2026-09-12 03:49:00 | NOAA-20 | SÃO BERNARDO | MARANHÃO | Brasil | 2110609 | 21 | 33 | nan | nan | nan | Cerrado | 6.1 |
| eb81edb8-463f-3225-aaca-569bd6c7ed50 | -14.39168 | -43.79097 | 2026-09-12 03:49:00 | NOAA-20 | MALHADA | BAHIA | Brasil | 2920205 | 29 | 33 | nan | nan | nan | Cerrado | 2.8 |
| 15d4327d-0634-3777-af85-9e5c7c5aa920 | -3.33111 | -42.29799 | 2026-09-12 03:49:00 | NOAA-20 | SÃO BERNARDO | MARANHÃO | Brasil | 2110609 | 21 | 33 | nan | nan | nan | Cerrado | 6.1 |
| d9f6d27e-1617-3ee7-b8e0-89f7817c27ce | -12.11634 | -48.96319 | 2026-09-12 03:49:00 | NOAA-20 | FIGUEIRÓPOLIS | TOCANTINS | Brasil | 1707652 | 17 | 33 | nan | nan | nan | Cerrado | 3.7 |
| abcd0867-7fc7-34ae-be71-de8e426b6855 | -15.44854 | -41.38549 | 2026-09-12 03:49:00 | NOAA-20 | CÂNDIDO SALES | BAHIA | Brasil | 2906709 | 29 | 33 | nan | nan | nan | Mata Atlântica | 0.7 |
| 97d2442b-f1f2-314b-97b4-3e4746014d61 | -11.36092 | -46.79978 | 2026-09-12 03:49:00 | NOAA-20 | RIO DA CONCEIÇÃO | TOCANTINS | Brasil | 1718659 | 17 | 33 | nan | nan | nan | Cerrado | 2.6 |
| b09c847e-4829-342f-9d47-24a6797fabc4 | -11.35088 | -46.28675 | 2026-09-12 03:49:00 | NOAA-20 | FORMOSA DO RIO PRETO | BAHIA | Brasil | 2911105 | 29 | 33 | nan | nan | nan | Cerrado | 1.0 |
| 9681a556-9a9b-3197-ae6f-e7ce37547834 | -7.96502 | -43.99998 | 2026-09-12 03:49:00 | NOAA-20 | SEBASTIÃO LEAL | PIAUÍ | Brasil | 2210631 | 22 | 33 | nan | nan | nan | Cerrado | 2.8 |
| db5248ba-c1f3-3076-b842-fe4251632011 | -9.70502 | -43.39901 | 2026-09-12 03:49:00 | NOAA-20 | PILÃO ARCADO | BAHIA | Brasil | 2924405 | 29 | 33 | nan | nan | nan | Caatinga | 2.3 |
| a1a1ad83-cfc7-3b05-86b0-fdb59e340895 | -10.55047 | -45.218 | 2026-09-12 03:49:00 | NOAA-20 | CORRENTE | PIAUÍ | Brasil | 2202901 | 22 | 33 | nan | nan | nan | Cerrado | 2.2 |
| 697cc11c-c787-3e03-a947-c67ff93adb14 | -9.67431 | -46.0093 | 2026-09-12 03:49:00 | NOAA-20 | ALTO PARNAÍBA | MARANHÃO | Brasil | 2100501 | 21 | 33 | nan | nan | nan | Cerrado | 3.3 |
| 74b2b813-2a67-3eb1-a44f-c51cdda705e6 | -9.52913 | -40.33456 | 2026-09-12 03:49:00 | NOAA-20 | JUAZEIRO | BAHIA | Brasil | 2918407 | 29 | 33 | nan | nan | nan | Caatinga | 7.3 |
| c6b4cc9a-d115-3761-8ad9-a44fc0f83f37 | -13.3701 | -48.02299 | 2026-09-12 03:49:00 | NOAA-20 | CAVALCANTE | GOIÁS | Brasil | 5205307 | 52 | 33 | nan | nan | nan | Cerrado | 2.7 |
| b0850325-a38d-3738-8e77-ab7ffa67f4f1 | -9.52149 | -40.33323 | 2026-09-12 03:49:00 | NOAA-20 | JUAZEIRO | BAHIA | Brasil | 2918407 | 29 | 33 | nan | nan | nan | Caatinga | 31.4 |
| cc5cacc2-7cd2-3f25-b384-38ca607c8985 | -10.0653 | -45.47157 | 2026-09-12 03:49:00 | NOAA-20 | SÃO GONÇALO DO GURGUÉIA | PIAUÍ | Brasil | 2209757 | 22 | 33 | nan | nan | nan | Cerrado | 2.5 |
| 22b963bb-4491-33bf-aa26-c2c3c3d7ec78 | -9.54627 | -45.47602 | 2026-09-12 03:49:00 | NOAA-20 | GILBUÉS | PIAUÍ | Brasil | 2204402 | 22 | 33 | nan | nan | nan | Cerrado | 4.3 |
| 8995bbfc-428f-309b-a7c6-79c11ad13ba0 | -7.9579 | -44.01109 | 2026-09-12 03:49:00 | NOAA-20 | SEBASTIÃO LEAL | PIAUÍ | Brasil | 2210631 | 22 | 33 | nan | nan | nan | Cerrado | 1.1 |
| 1f129504-f5c3-3fe5-8040-c50fc9018ec4 | -10.51479 | -40.54635 | 2026-09-12 03:49:00 | NOAA-20 | CAMPO FORMOSO | BAHIA | Brasil | 2906006 | 29 | 33 | nan | nan | nan | Caatinga | 0.8 |
| 99fb361c-9db5-361d-9746-a50ecd5ff6b6 | -10.21935 | -45.19514 | 2026-09-12 03:49:00 | NOAA-20 | CORRENTE | PIAUÍ | Brasil | 2202901 | 22 | 33 | nan | nan | nan | Cerrado | 2.7 |
| 39deb3a6-f816-385e-a5ab-0ce2b73e88db | -4.54387 | -38.55727 | 2026-09-12 03:49:00 | NOAA-20 | OCARA | CEARÁ | Brasil | 2309458 | 23 | 33 | nan | nan | nan | Caatinga | 3.2 |
| d31746b9-c8f3-3937-a874-faa090f47839 | -11.37487 | -46.83001 | 2026-09-12 03:49:00 | NOAA-20 | RIO DA CONCEIÇÃO | TOCANTINS | Brasil | 1718659 | 17 | 33 | nan | nan | nan | Cerrado | 10.5 |
| b23cbef4-d3c1-336b-94cf-1872801a4723 | -14.00929 | -42.14738 | 2026-09-12 03:49:00 | NOAA-20 | LAGOA REAL | BAHIA | Brasil | 2918753 | 29 | 33 | nan | nan | nan | Caatinga | 1.6 |
| 7cdc4993-b4a5-3df6-af6a-5faf4f357b63 | -14.89534 | -41.18696 | 2026-09-12 03:49:00 | NOAA-20 | BELO CAMPO | BAHIA | Brasil | 2903508 | 29 | 33 | nan | nan | nan | Mata Atlântica | 0.8 |
| 23e7784c-11b2-338a-ac67-62cb50a1a5e3 | -11.18791 | -42.78691 | 2026-09-12 03:49:00 | NOAA-20 | GENTIO DO OURO | BAHIA | Brasil | 2911303 | 29 | 33 | nan | nan | nan | Caatinga | 5.6 |
| 18b75649-7407-3da0-8c3a-3055d51b2b93 | -14.95681 | -47.52517 | 2026-09-12 03:49:00 | NOAA-20 | FORMOSA | GOIÁS | Brasil | 5208004 | 52 | 33 | nan | nan | nan | Cerrado | 1.9 |
| 70f3204b-651c-357a-b750-f8749bbeca90 | -11.3521 | -45.79261 | 2026-09-12 03:49:00 | NOAA-20 | FORMOSA DO RIO PRETO | BAHIA | Brasil | 2911105 | 29 | 33 | nan | nan | nan | Cerrado | 1.9 |
| fe945430-9f71-3598-b96a-d71c5ee1c9f6 | -9.67374 | -46.01682 | 2026-09-12 03:49:00 | NOAA-20 | ALTO PARNAÍBA | MARANHÃO | Brasil | 2100501 | 21 | 33 | nan | nan | nan | Cerrado | 4.8 |
| 0849412e-ca47-3051-867c-6b71c58288bd | -3.33003 | -42.29942 | 2026-09-12 03:49:00 | NOAA-20 | SÃO BERNARDO | MARANHÃO | Brasil | 2110609 | 21 | 33 | nan | nan | nan | Cerrado | 7.0 |
| 4d72fd24-4ad3-3eb5-8fe5-efa08a65836c | -7.95736 | -44.01416 | 2026-09-12 03:49:00 | NOAA-20 | SEBASTIÃO LEAL | PIAUÍ | Brasil | 2210631 | 22 | 33 | nan | nan | nan | Cerrado | 1.3 |
| 0dabbbca-78a7-306b-ab11-5d7b59027d29 | -3.72669 | -40.42868 | 2026-09-12 03:49:00 | NOAA-20 | SOBRAL | CEARÁ | Brasil | 2312908 | 23 | 33 | nan | nan | nan | Caatinga | 10.5 |
| 3a8fdbdb-5164-3a73-957f-f359bd19b05e | -3.23133 | -46.96015 | 2026-09-12 03:49:00 | NOAA-20 | PARAGOMINAS | PARÁ | Brasil | 1505502 | 15 | 33 | nan | nan | nan | Amazônia | 12.4 |
| 176a8c4c-c837-3786-b8e8-5a706d0d81f4 | -9.31389 | -44.34732 | 2026-09-12 03:49:00 | NOAA-20 | BOM JESUS | PIAUÍ | Brasil | 2201903 | 22 | 33 | nan | nan | nan | Cerrado | 1.3 |
| 5297fe4f-fe16-3154-80d6-2009c5f65ced | -12.13146 | -48.95425 | 2026-09-12 03:49:00 | NOAA-20 | FIGUEIRÓPOLIS | TOCANTINS | Brasil | 1707652 | 17 | 33 | nan | nan | nan | Cerrado | 3.8 |
| 02133b8b-3ce7-3153-bbaf-9192a75ba62f | -11.35604 | -46.28739 | 2026-09-12 03:49:00 | NOAA-20 | FORMOSA DO RIO PRETO | BAHIA | Brasil | 2911105 | 29 | 33 | nan | nan | nan | Cerrado | 2.5 |
| b6317ae5-942e-32e9-a29f-60472061d3ce | -12.85274 | -44.39124 | 2026-09-12 03:49:00 | NOAA-20 | BAIANÓPOLIS | BAHIA | Brasil | 2902500 | 29 | 33 | nan | nan | nan | Cerrado | 13.1 |
| 6e38a96b-7276-326d-9022-e2eb4aee9fe2 | -14.58942 | -48.83547 | 2026-09-12 03:49:00 | NOAA-20 | NIQUELÂNDIA | GOIÁS | Brasil | 5214606 | 52 | 33 | nan | nan | nan | Cerrado | 2.9 |
| 88b6163e-49b9-30bf-beec-2d98cec73a1d | -14.95609 | -47.52869 | 2026-09-12 03:49:00 | NOAA-20 | FORMOSA | GOIÁS | Brasil | 5208004 | 52 | 33 | nan | nan | nan | Cerrado | 1.9 |
| fddf5abe-2c2c-323f-9dd6-e88b5f3ecbd7 | -14.58853 | -48.83973 | 2026-09-12 03:49:00 | NOAA-20 | NIQUELÂNDIA | GOIÁS | Brasil | 5214606 | 52 | 33 | nan | nan | nan | Cerrado | 4.1 |
| df861b14-e3b1-357a-a809-0a1f4befa243 | -10.54828 | -45.201 | 2026-09-12 03:49:00 | NOAA-20 | CORRENTE | PIAUÍ | Brasil | 2202901 | 22 | 33 | nan | nan | nan | Cerrado | 0.9 |
| b343ab44-8941-3b15-9ebc-f71e8af1a0be | -13.3741 | -48.02312 | 2026-09-12 03:49:00 | NOAA-20 | CAVALCANTE | GOIÁS | Brasil | 5205307 | 52 | 33 | nan | nan | nan | Cerrado | 2.2 |
| a670aa9b-237a-3fb4-983d-a3a9bb30912b | -12.20121 | -49.39479 | 2026-09-12 03:49:00 | NOAA-20 | FIGUEIRÓPOLIS | TOCANTINS | Brasil | 1707652 | 17 | 33 | nan | nan | nan | Cerrado | 2.6 |
| e5205241-c032-31a8-9e17-fb074f490d05 | -9.34734 | -40.64029 | 2026-09-12 03:49:00 | NOAA-20 | PETROLINA | PERNAMBUCO | Brasil | 2611101 | 26 | 33 | nan | nan | nan | Caatinga | 0.8 |
| 54703d82-2498-304a-b46e-8d02fad3ee39 | -3.74664 | -42.47939 | 2026-09-12 03:49:00 | NOAA-20 | LUZILÂNDIA | PIAUÍ | Brasil | 2205805 | 22 | 33 | nan | nan | nan | Cerrado | 1.6 |
| e453f990-e549-3784-a4ef-2c96e145c0ff | -12.29486 | -40.56643 | 2026-09-12 03:49:00 | NOAA-20 | RUY BARBOSA | BAHIA | Brasil | 2927200 | 29 | 33 | nan | nan | nan | Caatinga | 1.7 |
| 5c678e3c-d0da-32b9-9d4e-67e53cf4b892 | -8.03065 | -43.8596 | 2026-09-12 03:49:00 | NOAA-20 | MANOEL EMÍDIO | PIAUÍ | Brasil | 2205904 | 22 | 33 | nan | nan | nan | Caatinga | 3.9 |
| 326437a2-6efe-39f0-9930-0ddf09ed3c2c | -10.62963 | -46.13004 | 2026-09-12 03:49:00 | NOAA-20 | FORMOSA DO RIO PRETO | BAHIA | Brasil | 2911105 | 29 | 33 | nan | nan | nan | Cerrado | 1.2 |
| cb36f58b-019f-3859-b39e-f47dcc5e1eed | -2.46975 | -48.04598 | 2026-09-12 03:49:00 | NOAA-20 | TOMÉ-AÇU | PARÁ | Brasil | 1508001 | 15 | 33 | nan | nan | nan | Amazônia | 7.8 |
| eb59add1-aab5-3230-bef1-a3a5beb3736c | -11.36414 | -46.79523 | 2026-09-12 03:49:00 | NOAA-20 | RIO DA CONCEIÇÃO | TOCANTINS | Brasil | 1718659 | 17 | 33 | nan | nan | nan | Cerrado | 2.4 |
| 9670b2c9-72de-3b9c-bc4f-fcede49479c2 | -9.3158 | -45.64729 | 2026-09-12 03:49:00 | NOAA-20 | SANTA FILOMENA | PIAUÍ | Brasil | 2209203 | 22 | 33 | nan | nan | nan | Cerrado | 2.9 |
| 43406e0b-de01-38e8-9c4e-033bcc05f8c3 | -9.67517 | -46.00907 | 2026-09-12 03:49:00 | NOAA-20 | ALTO PARNAÍBA | MARANHÃO | Brasil | 2100501 | 21 | 33 | nan | nan | nan | Cerrado | 3.0 |
| 0ffcaaa7-0ffd-3662-9eac-97d6408d1deb | -13.16613 | -43.38649 | 2026-09-12 03:49:00 | NOAA-20 | BOM JESUS DA LAPA | BAHIA | Brasil | 2903904 | 29 | 33 | nan | nan | nan | Cerrado | 1.7 |
| c12a6bfd-81bf-3d0b-abf0-432d4a82ad79 | -9.90009 | -46.2294 | 2026-09-12 03:49:00 | NOAA-20 | ALTO PARNAÍBA | MARANHÃO | Brasil | 2100501 | 21 | 33 | nan | nan | nan | Cerrado | 1.8 |
| 847820a9-9135-3303-8c0e-27c89713c8dc | -9.31518 | -44.36886 | 2026-09-12 03:49:00 | NOAA-20 | BOM JESUS | PIAUÍ | Brasil | 2201903 | 22 | 33 | nan | nan | nan | Cerrado | 1.8 |


[Clique aqui para ver as próximas entradas](README14.md)
