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

## Dados Diários - Página 4

| ID | Latitude | Longitude | Data/Hora GMT | Satélite | Município | Estado | País | Município ID | Estado ID | País ID | Dias sem Chuva | Precipitação | Risco de Fogo | Bioma | FRP |
|----|----------|-----------|---------------|----------|-----------|--------|------|--------------|-----------|---------|----------------|--------------|----------------|-------|-----|
| eb713b08-517b-3329-bbd2-7feb97f2844f | -22.39517 | -49.78099 | 2025-07-17 00:22:00 | TERRA_M-M | LUPÉRCIO | SÃO PAULO | Brasil | 3527801 | 35 | 33 | nan | nan | nan | Mata Atlântica | 42.2 |
| 3139f1d3-58a0-324e-acc3-a8559fd875f2 | -21.07819 | -48.69171 | 2025-07-17 00:22:00 | TERRA_M-M | PIRANGI | SÃO PAULO | Brasil | 3539004 | 35 | 33 | nan | nan | nan | Mata Atlântica | 32.8 |
| 4500673a-fae4-322d-b09a-80d0063a5644 | -8.71643 | -50.05606 | 2025-07-17 00:24:00 | TERRA_M-M | SANTA MARIA DAS BARREIRAS | PARÁ | Brasil | 1506583 | 15 | 33 | nan | nan | nan | Amazônia | 10.4 |
| afd17210-07d7-3f3c-95bf-ae5d414500b0 | -9.24959 | -48.57526 | 2025-07-17 00:24:00 | TERRA_M-M | MIRANORTE | TOCANTINS | Brasil | 1713304 | 17 | 33 | nan | nan | nan | Cerrado | 9.2 |
| 6bb3f73e-e0b3-3a1d-bb21-d0868e766c4d | -7.21126 | -45.32624 | 2025-07-17 00:24:00 | TERRA_M-M | LORETO | MARANHÃO | Brasil | 2106102 | 21 | 33 | nan | nan | nan | Cerrado | 8.3 |
| 013cedf5-62bf-3066-a56d-bfa9ab61ff4b | -9.30931 | -44.84126 | 2025-07-17 00:24:00 | TERRA_M-M | BOM JESUS | PIAUÍ | Brasil | 2201903 | 22 | 33 | nan | nan | nan | Cerrado | 5.6 |
| c0d9cc62-4a70-32c5-a9e7-3749317d831b | -11.51057 | -48.96658 | 2025-07-17 00:24:00 | TERRA_M-M | DUERÉ | TOCANTINS | Brasil | 1707306 | 17 | 33 | nan | nan | nan | Cerrado | 12.5 |
| af179337-8ad0-3412-a3b2-4dd90c3ad18f | -12.03529 | -48.76592 | 2025-07-17 00:24:00 | TERRA_M-M | SUCUPIRA | TOCANTINS | Brasil | 1720853 | 17 | 33 | nan | nan | nan | Cerrado | 11.2 |
| b3ac9383-a613-357b-86b3-2080a2890d2d | -11.46337 | -45.10026 | 2025-07-17 00:24:00 | TERRA_M-M | RIACHÃO DAS NEVES | BAHIA | Brasil | 2926202 | 29 | 33 | nan | nan | nan | Cerrado | 10.0 |
| a816898f-84e6-3fd4-939c-e595ec9eff7f | -11.66495 | -43.77512 | 2025-07-17 00:24:00 | TERRA_M-M | WANDERLEY | BAHIA | Brasil | 2933455 | 29 | 33 | nan | nan | nan | Cerrado | 15.6 |
| 62f8abe3-1af4-3345-b83a-87e602c4f74e | -9.10431 | -44.29744 | 2025-07-17 00:24:00 | TERRA_M-M | BOM JESUS | PIAUÍ | Brasil | 2201903 | 22 | 33 | nan | nan | nan | Cerrado | 5.2 |
| 27fe4a8e-6492-32ed-9e32-512a019abad0 | -6.99675 | -43.74285 | 2025-07-17 00:24:00 | TERRA_M-M | JERUMENHA | PIAUÍ | Brasil | 2205300 | 22 | 33 | nan | nan | nan | Cerrado | 5.0 |
| db7501f4-b63b-336c-893f-637567770efd | -12.43071 | -50.0548 | 2025-07-17 00:24:00 | TERRA_M-M | SANDOLÂNDIA | TOCANTINS | Brasil | 1718840 | 17 | 33 | nan | nan | nan | Cerrado | 33.1 |
| 271cfc35-28cc-3ada-bf53-61122ab76b7e | -10.20783 | -47.32184 | 2025-07-17 00:24:00 | TERRA_M-M | NOVO ACORDO | TOCANTINS | Brasil | 1715101 | 17 | 33 | nan | nan | nan | Cerrado | 9.0 |
| de9769fb-1357-3f9c-bd0a-7cbeb2971052 | -9.24657 | -48.55191 | 2025-07-17 00:24:00 | TERRA_M-M | RIO DOS BOIS | TOCANTINS | Brasil | 1718709 | 17 | 33 | nan | nan | nan | Cerrado | 15.0 |
| 6003407f-b9f1-384e-9ff9-90b25102120a | -9.41197 | -48.4109 | 2025-07-17 00:24:00 | TERRA_M-M | MIRACEMA DO TOCANTINS | TOCANTINS | Brasil | 1713205 | 17 | 33 | nan | nan | nan | Cerrado | 18.5 |
| c703142e-ad36-396d-9199-b6994c395d0e | -12.48134 | -46.92103 | 2025-07-17 00:24:00 | TERRA_M-M | ARRAIAS | TOCANTINS | Brasil | 1702406 | 17 | 33 | nan | nan | nan | Cerrado | 23.7 |
| 285c015d-9dc3-3a97-b08e-89263159fbcc | -12.49084 | -46.91972 | 2025-07-17 00:24:00 | TERRA_M-M | ARRAIAS | TOCANTINS | Brasil | 1702406 | 17 | 33 | nan | nan | nan | Cerrado | 20.5 |
| 2f1ec089-8dac-3f35-80cd-307060d50c8c | -11.46013 | -48.15886 | 2025-07-17 00:24:00 | TERRA_M-M | SANTA ROSA DO TOCANTINS | TOCANTINS | Brasil | 1718907 | 17 | 33 | nan | nan | nan | Cerrado | 10.3 |
| cf6bfae2-39cd-3007-b5a6-e85926670415 | -12.71301 | -46.80721 | 2025-07-17 00:24:00 | TERRA_M-M | ARRAIAS | TOCANTINS | Brasil | 1702406 | 17 | 33 | nan | nan | nan | Cerrado | 21.1 |
| 5bfb184f-cb03-36c2-ae16-cdd8f3c187db | -8.87877 | -44.79712 | 2025-07-17 00:24:00 | TERRA_M-M | CURRAIS | PIAUÍ | Brasil | 2203230 | 22 | 33 | nan | nan | nan | Cerrado | 25.8 |
| 45b8da7e-cc3b-3267-8ad1-9621a40843a7 | -10.56847 | -49.14189 | 2025-07-17 00:24:00 | TERRA_M-M | CRISTALÂNDIA | TOCANTINS | Brasil | 1706100 | 17 | 33 | nan | nan | nan | Cerrado | 10.9 |
| f45757f2-8126-3996-aa83-fc49ac3248c9 | -8.91595 | -47.35702 | 2025-07-17 00:24:00 | TERRA_M-M | CENTENÁRIO | TOCANTINS | Brasil | 1704105 | 17 | 33 | nan | nan | nan | Cerrado | 9.1 |
| a57b3cdd-fe06-3f93-b110-dac86b41507c | -12.42264 | -50.0451 | 2025-07-17 00:24:00 | TERRA_M-M | SANDOLÂNDIA | TOCANTINS | Brasil | 1718840 | 17 | 33 | nan | nan | nan | Cerrado | 71.7 |
| debb2638-9039-315b-b375-dedf9656f945 | -11.11158 | -48.87968 | 2025-07-17 00:24:00 | TERRA_M-M | CRIXÁS DO TOCANTINS | TOCANTINS | Brasil | 1706258 | 17 | 33 | nan | nan | nan | Cerrado | 34.2 |
| 41dafa34-a56b-331f-95f0-a7996d8b21fe | -11.85017 | -46.75127 | 2025-07-17 00:24:00 | TERRA_M-M | NOVO JARDIM | TOCANTINS | Brasil | 1715259 | 17 | 33 | nan | nan | nan | Cerrado | 5.1 |
| 9754d5f9-7ae9-3ab9-bdcf-a36c144714ce | -9.23948 | -48.57657 | 2025-07-17 00:24:00 | TERRA_M-M | MIRANORTE | TOCANTINS | Brasil | 1713304 | 17 | 33 | nan | nan | nan | Cerrado | 13.0 |
| e0cfddb8-32e5-3f38-a6fc-c91801f2da65 | -13.00508 | -44.86527 | 2025-07-17 00:24:00 | TERRA_M-M | SÃO DESIDÉRIO | BAHIA | Brasil | 2928901 | 29 | 33 | nan | nan | nan | Cerrado | 5.9 |
| 8e51ed2a-f9a2-3002-b527-b5df1365c2b3 | -13.68059 | -44.22725 | 2025-07-17 00:24:00 | TERRA_M-M | CORIBE | BAHIA | Brasil | 2909109 | 29 | 33 | nan | nan | nan | Cerrado | 4.7 |
| fd8daedb-e93d-3026-ad38-e71495a10d73 | -7.72188 | -44.75391 | 2025-07-17 00:24:00 | TERRA_M-M | URUÇUÍ | PIAUÍ | Brasil | 2211209 | 22 | 33 | nan | nan | nan | Cerrado | 9.9 |
| 7147f5f7-5d26-3294-a512-58482eb5ecb5 | -8.87751 | -50.14933 | 2025-07-17 00:24:00 | TERRA_M-M | SANTA MARIA DAS BARREIRAS | PARÁ | Brasil | 1506583 | 15 | 33 | nan | nan | nan | Amazônia | 15.6 |
| 52b02861-0a9b-3942-bac1-6fe50d713523 | -8.1045 | -43.15952 | 2025-07-17 00:24:00 | TERRA_M-M | CANTO DO BURITI | PIAUÍ | Brasil | 2202307 | 22 | 33 | nan | nan | nan | Caatinga | 22.2 |
| f1534731-df54-3e91-981f-84a68b1c73d0 | -12.99745 | -44.87561 | 2025-07-17 00:24:00 | TERRA_M-M | SÃO DESIDÉRIO | BAHIA | Brasil | 2928901 | 29 | 33 | nan | nan | nan | Cerrado | 6.3 |
| 18ba0f9f-0c25-3f50-8b3f-5d830ff2f8fe | -11.45992 | -48.16461 | 2025-07-17 00:24:00 | TERRA_M-M | SANTA ROSA DO TOCANTINS | TOCANTINS | Brasil | 1718907 | 17 | 33 | nan | nan | nan | Cerrado | 9.3 |
| 342a4fe7-7a84-3e37-ad57-aa1b645f79f5 | -9.92173 | -48.01649 | 2025-07-17 00:24:00 | TERRA_M-M | APARECIDA DO RIO NEGRO | TOCANTINS | Brasil | 1701101 | 17 | 33 | nan | nan | nan | Cerrado | 13.6 |
| cde8e2fb-e04e-36fc-8f31-c45167ea0d85 | -12.09647 | -48.19122 | 2025-07-17 00:24:00 | TERRA_M-M | PEIXE | TOCANTINS | Brasil | 1716604 | 17 | 33 | nan | nan | nan | Cerrado | 14.0 |
| 9fc443a2-0e5b-326e-9a48-77af234b5aec | -8.87823 | -50.15876 | 2025-07-17 00:24:00 | TERRA_M-M | SANTA MARIA DAS BARREIRAS | PARÁ | Brasil | 1506583 | 15 | 33 | nan | nan | nan | Amazônia | 14.9 |
| c7b467c1-cd36-327c-8650-016bc548b41e | -7.61431 | -44.32003 | 2025-07-17 00:24:00 | TERRA_M-M | URUÇUÍ | PIAUÍ | Brasil | 2211209 | 22 | 33 | nan | nan | nan | Cerrado | 17.2 |
| 1db13dc3-952f-33fd-9f6d-a84029a03c35 | -12.41882 | -50.05629 | 2025-07-17 00:24:00 | TERRA_M-M | SANDOLÂNDIA | TOCANTINS | Brasil | 1718840 | 17 | 33 | nan | nan | nan | Cerrado | 28.5 |
| da52039e-9a86-3015-8da3-e2ab954e3de5 | -8.75022 | -46.60144 | 2025-07-17 00:24:00 | TERRA_M-M | BALSAS | MARANHÃO | Brasil | 2101400 | 21 | 33 | nan | nan | nan | Cerrado | 10.4 |
| e5f10af1-9b07-34ce-bc58-1b44f145460f | -8.87608 | -47.27116 | 2025-07-17 00:24:00 | TERRA_M-M | CENTENÁRIO | TOCANTINS | Brasil | 1704105 | 17 | 33 | nan | nan | nan | Cerrado | 6.2 |
| 3f8da1a0-6992-3516-9143-72fd3e5b8d3e | -7.2125 | -45.33512 | 2025-07-17 00:24:00 | TERRA_M-M | LORETO | MARANHÃO | Brasil | 2106102 | 21 | 33 | nan | nan | nan | Cerrado | 18.7 |
| ce53069c-e055-3115-91cb-ab532283db68 | -12.47679 | -44.50296 | 2025-07-17 00:24:00 | TERRA_M-M | BAIANÓPOLIS | BAHIA | Brasil | 2902500 | 29 | 33 | nan | nan | nan | Cerrado | 24.5 |
| cbe8732d-40db-32a7-bf3e-2f44180feec1 | -12.99497 | -44.85748 | 2025-07-17 00:24:00 | TERRA_M-M | SÃO DESIDÉRIO | BAHIA | Brasil | 2928901 | 29 | 33 | nan | nan | nan | Cerrado | 5.2 |
| 191fcaf2-0df3-3fd0-8f41-b6056ad82290 | -11.80823 | -44.2676 | 2025-07-17 00:24:00 | TERRA_M-M | COTEGIPE | BAHIA | Brasil | 2909406 | 29 | 33 | nan | nan | nan | Cerrado | 5.4 |
| 428ff41f-048c-3ee8-a26b-7a183ad86873 | -12.49607 | -46.92375 | 2025-07-17 00:24:00 | TERRA_M-M | ARRAIAS | TOCANTINS | Brasil | 1702406 | 17 | 33 | nan | nan | nan | Cerrado | 11.1 |
| 1566d7fe-a978-3a25-a138-c154c2775869 | -11.67259 | -43.7646 | 2025-07-17 00:24:00 | TERRA_M-M | WANDERLEY | BAHIA | Brasil | 2933455 | 29 | 33 | nan | nan | nan | Cerrado | 12.1 |
| 2ff3b5cf-90ff-37cd-841e-df1a5c7ebaa8 | -11.23339 | -49.50071 | 2025-07-17 00:24:00 | TERRA_M-M | DUERÉ | TOCANTINS | Brasil | 1707306 | 17 | 33 | nan | nan | nan | Cerrado | 17.5 |
| b3196a39-b7c0-34ee-beba-3d6f7072e7b8 | -8.10305 | -43.14934 | 2025-07-17 00:24:00 | TERRA_M-M | CANTO DO BURITI | PIAUÍ | Brasil | 2202307 | 22 | 33 | nan | nan | nan | Caatinga | 337.4 |
| ed3cdb54-9d4c-3d16-9b83-b978c1f0d85c | -11.50887 | -48.95301 | 2025-07-17 00:24:00 | TERRA_M-M | ALIANÇA DO TOCANTINS | TOCANTINS | Brasil | 1700350 | 17 | 33 | nan | nan | nan | Cerrado | 25.5 |
| 4b9f0929-ed4a-3ba0-9d69-c4eb1f99b03c | -12.43452 | -50.04364 | 2025-07-17 00:24:00 | TERRA_M-M | SANDOLÂNDIA | TOCANTINS | Brasil | 1718840 | 17 | 33 | nan | nan | nan | Cerrado | 31.0 |
| 45bf4b9b-0ddb-31fb-86b4-f28a12458bd1 | -13.00633 | -44.87434 | 2025-07-17 00:24:00 | TERRA_M-M | SÃO DESIDÉRIO | BAHIA | Brasil | 2928901 | 29 | 33 | nan | nan | nan | Cerrado | 11.7 |
| b2fd5da7-7c10-35b2-8354-778ffb22766c | -11.6073 | -43.11777 | 2025-07-17 00:24:00 | TERRA_M-M | MORPARÁ | BAHIA | Brasil | 2921609 | 29 | 33 | nan | nan | nan | Caatinga | 4.9 |
| 6bd5a72c-55fb-366a-81a3-bda22acd95e1 | -9.31056 | -44.85019 | 2025-07-17 00:24:00 | TERRA_M-M | BOM JESUS | PIAUÍ | Brasil | 2201903 | 22 | 33 | nan | nan | nan | Cerrado | 11.9 |
| fb6d6aec-e183-33ec-b4c1-32686d3d3e33 | -8.11692 | -43.14149 | 2025-07-17 00:24:00 | TERRA_M-M | CANTO DO BURITI | PIAUÍ | Brasil | 2202307 | 22 | 33 | nan | nan | nan | Caatinga | 20.0 |
| 3011ad83-81cc-3b88-80c6-a0a8652ff50b | -14.03709 | -51.22179 | 2025-07-17 00:24:00 | TERRA_M-M | COCALINHO | MATO GROSSO | Brasil | 5103106 | 51 | 33 | nan | nan | nan | Cerrado | 92.7 |
| f705e0e4-b832-3871-95b2-1f745f6c19a8 | -8.09507 | -43.16094 | 2025-07-17 00:24:00 | TERRA_M-M | CANTO DO BURITI | PIAUÍ | Brasil | 2202307 | 22 | 33 | nan | nan | nan | Caatinga | 7.5 |
| d6a7ef49-2a59-34a6-bdf2-6711a5b54205 | -9.23648 | -48.5532 | 2025-07-17 00:24:00 | TERRA_M-M | RIO DOS BOIS | TOCANTINS | Brasil | 1718709 | 17 | 33 | nan | nan | nan | Cerrado | 38.5 |
| 219dbf0c-2296-3649-8220-7ebedb7adad4 | -9.31941 | -44.84891 | 2025-07-17 00:24:00 | TERRA_M-M | BOM JESUS | PIAUÍ | Brasil | 2201903 | 22 | 33 | nan | nan | nan | Cerrado | 7.6 |
| b1d63b4d-2f6f-3ac6-8b34-eab6373bcd17 | -11.67388 | -43.77377 | 2025-07-17 00:24:00 | TERRA_M-M | WANDERLEY | BAHIA | Brasil | 2933455 | 29 | 33 | nan | nan | nan | Cerrado | 5.3 |
| f1621b5d-cf23-3da5-a4cd-aea5bb2738c7 | -11.56621 | -47.09642 | 2025-07-17 00:24:00 | TERRA_M-M | PORTO ALEGRE DO TOCANTINS | TOCANTINS | Brasil | 1718006 | 17 | 33 | nan | nan | nan | Cerrado | 10.3 |
| 76ba6c1e-0b64-3df8-8082-0b7380367368 | -11.66365 | -43.76595 | 2025-07-17 00:24:00 | TERRA_M-M | WANDERLEY | BAHIA | Brasil | 2933455 | 29 | 33 | nan | nan | nan | Cerrado | 18.1 |
| 03e57c6a-f1c3-344e-8de5-2d6a15b1d8ec | -8.8344 | -44.21548 | 2025-07-17 00:24:00 | TERRA_M-M | CRISTINO CASTRO | PIAUÍ | Brasil | 2203107 | 22 | 33 | nan | nan | nan | Cerrado | 7.7 |
| cd1227d6-26c7-3eac-9e51-4d0e5acb6a73 | -14.02369 | -51.22335 | 2025-07-17 00:24:00 | TERRA_M-M | COCALINHO | MATO GROSSO | Brasil | 5103106 | 51 | 33 | nan | nan | nan | Cerrado | 31.1 |
| b136e87f-4bfc-34e5-bffb-0325f897c47a | -11.95124 | -48.43251 | 2025-07-17 00:24:00 | TERRA_M-M | PEIXE | TOCANTINS | Brasil | 1716604 | 17 | 33 | nan | nan | nan | Cerrado | 34.1 |
| aa10c26c-f58e-3398-b186-190b1f8285e4 | -11.08142 | -44.53365 | 2025-07-17 00:24:00 | TERRA_M-M | SANTA RITA DE CÁSSIA | BAHIA | Brasil | 2928406 | 29 | 33 | nan | nan | nan | Cerrado | 6.3 |
| 9f0ae471-28ff-3fe4-acd2-53ff61e50a2b | -8.70522 | -50.05753 | 2025-07-17 00:24:00 | TERRA_M-M | SANTA MARIA DAS BARREIRAS | PARÁ | Brasil | 1506583 | 15 | 33 | nan | nan | nan | Amazônia | 28.6 |
| 6e7b51dc-98a8-3b14-b00c-70c2879b38b8 | -12.47996 | -46.91058 | 2025-07-17 00:24:00 | TERRA_M-M | ARRAIAS | TOCANTINS | Brasil | 1702406 | 17 | 33 | nan | nan | nan | Cerrado | 19.7 |
| 66011fca-2fda-3e87-95e0-953c716986e9 | -7.61302 | -44.31081 | 2025-07-17 00:24:00 | TERRA_M-M | URUÇUÍ | PIAUÍ | Brasil | 2211209 | 22 | 33 | nan | nan | nan | Cerrado | 6.5 |
| 41ffb579-d2df-3a73-8f23-1d33887db1ca | -12.69273 | -46.79947 | 2025-07-17 00:24:00 | TERRA_M-M | ARRAIAS | TOCANTINS | Brasil | 1702406 | 17 | 33 | nan | nan | nan | Cerrado | 8.2 |
| 5ba35a97-e808-3875-9d90-f47908f3927b | -14.03251 | -51.21567 | 2025-07-17 00:24:00 | TERRA_M-M | COCALINHO | MATO GROSSO | Brasil | 5103106 | 51 | 33 | nan | nan | nan | Cerrado | 81.6 |
| 316550be-0785-3545-a15e-6db2564fd457 | -8.11842 | -43.15168 | 2025-07-17 00:24:00 | TERRA_M-M | CANTO DO BURITI | PIAUÍ | Brasil | 2202307 | 22 | 33 | nan | nan | nan | Caatinga | 31.9 |
| a4f6498b-665e-3ad6-93be-bdfc014eccd1 | -11.35633 | -48.72258 | 2025-07-17 00:24:00 | TERRA_M-M | ALIANÇA DO TOCANTINS | TOCANTINS | Brasil | 1700350 | 17 | 33 | nan | nan | nan | Cerrado | 7.7 |
| 5aa387f1-287c-3987-954f-87928ce54de6 | -9.92029 | -48.00544 | 2025-07-17 00:24:00 | TERRA_M-M | APARECIDA DO RIO NEGRO | TOCANTINS | Brasil | 1701101 | 17 | 33 | nan | nan | nan | Cerrado | 6.0 |
| fe927838-51a5-3cb3-993b-e87dae2ae2ce | -11.40361 | -42.2982 | 2025-07-17 00:24:00 | TERRA_M-M | IBIPEBA | BAHIA | Brasil | 2912400 | 29 | 33 | nan | nan | nan | Caatinga | 9.4 |
| 26fcd859-c302-3278-b54f-aedbbd19ec7a | -7.3485 | -44.20038 | 2025-07-17 00:24:00 | TERRA_M-M | ANTÔNIO ALMEIDA | PIAUÍ | Brasil | 2200806 | 22 | 33 | nan | nan | nan | Cerrado | 6.6 |
| a54dba58-c86f-3296-a91d-361966e1bc08 | -6.98233 | -42.81263 | 2025-07-17 00:24:00 | TERRA_M-M | NAZARÉ DO PIAUÍ | PIAUÍ | Brasil | 2206704 | 22 | 33 | nan | nan | nan | Caatinga | 7.7 |
| 61742e96-6865-3248-95c4-7b3e68b9d0b2 | -10.96423 | -42.18096 | 2025-07-17 00:24:00 | TERRA_M-M | ITAGUAÇU DA BAHIA | BAHIA | Brasil | 2915353 | 29 | 33 | nan | nan | nan | Caatinga | 7.4 |
| ea00c1fd-a620-3a50-88d3-92457cfa31e6 | -12.70354 | -46.80854 | 2025-07-17 00:24:00 | TERRA_M-M | ARRAIAS | TOCANTINS | Brasil | 1702406 | 17 | 33 | nan | nan | nan | Cerrado | 63.5 |
| 321b4bbf-57dc-3910-b1b3-4544861789f6 | -12.69407 | -46.80986 | 2025-07-17 00:24:00 | TERRA_M-M | ARRAIAS | TOCANTINS | Brasil | 1702406 | 17 | 33 | nan | nan | nan | Cerrado | 11.6 |
| 2af144a1-a843-357e-8bc3-70f5406fd3ad | -9.15962 | -49.67545 | 2025-07-17 00:24:00 | TERRA_M-M | ARAGUACEMA | TOCANTINS | Brasil | 1701903 | 17 | 33 | nan | nan | nan | Cerrado | 10.9 |
| f28acb0a-fd89-3ae4-ab96-4becb6b6eb9d | -11.10995 | -48.8665 | 2025-07-17 00:24:00 | TERRA_M-M | CRIXÁS DO TOCANTINS | TOCANTINS | Brasil | 1706258 | 17 | 33 | nan | nan | nan | Cerrado | 229.8 |
| 69a5c14f-3265-32d4-86f1-2e9acfebcbb2 | -12.42873 | -50.03778 | 2025-07-17 00:24:00 | TERRA_M-M | SANDOLÂNDIA | TOCANTINS | Brasil | 1718840 | 17 | 33 | nan | nan | nan | Cerrado | 57.3 |
| cfee991e-d3af-3855-965d-59866166a73c | -12.99621 | -44.86654 | 2025-07-17 00:24:00 | TERRA_M-M | SÃO DESIDÉRIO | BAHIA | Brasil | 2928901 | 29 | 33 | nan | nan | nan | Cerrado | 13.0 |
| 73f4c98d-17eb-33e2-948a-4a612ef21454 | -7.19171 | -43.11822 | 2025-07-17 00:24:00 | TERRA_M-M | FLORIANO | PIAUÍ | Brasil | 2203909 | 22 | 33 | nan | nan | nan | Caatinga | 45.5 |
| 01be87f8-37a8-3a89-a3c3-eb4234512ebb | -7.70122 | -47.2838 | 2025-07-17 00:24:00 | TERRA_M-M | CAROLINA | MARANHÃO | Brasil | 2102804 | 21 | 33 | nan | nan | nan | Cerrado | 5.8 |
| b0fc8b1c-e4ec-3af1-8fa1-6ef9030a9370 | -15.93175 | -43.52462 | 2025-07-17 00:24:00 | TERRA_M-M | JANAÚBA | MINAS GERAIS | Brasil | 3135100 | 31 | 33 | nan | nan | nan | Cerrado | 7.6 |
| 9dee3155-b5ef-3316-901a-466d585f1d7c | -11.24455 | -49.49928 | 2025-07-17 00:24:00 | TERRA_M-M | DUERÉ | TOCANTINS | Brasil | 1707306 | 17 | 33 | nan | nan | nan | Cerrado | 20.8 |
| a8d40839-21e9-3e08-8bde-fe07e842260c | -13.67933 | -44.2182 | 2025-07-17 00:24:00 | TERRA_M-M | CORIBE | BAHIA | Brasil | 2909109 | 29 | 33 | nan | nan | nan | Cerrado | 5.7 |
| c2ebd78c-a60e-3490-b3ce-8553db975cdf | -8.10749 | -43.14289 | 2025-07-17 00:24:00 | TERRA_M-M | CANTO DO BURITI | PIAUÍ | Brasil | 2202307 | 22 | 33 | nan | nan | nan | Caatinga | 167.7 |
| 08dda001-9f09-3456-90c2-978a36b265c2 | -7.20241 | -45.32752 | 2025-07-17 00:24:00 | TERRA_M-M | LORETO | MARANHÃO | Brasil | 2106102 | 21 | 33 | nan | nan | nan | Cerrado | 7.8 |
| c879c738-0787-354d-bb79-7fcf4263365b | -9.23797 | -48.56481 | 2025-07-17 00:24:00 | TERRA_M-M | RIO DOS BOIS | TOCANTINS | Brasil | 1718709 | 17 | 33 | nan | nan | nan | Cerrado | 342.1 |
| 12efa1f5-f788-36fb-ab2b-1f0d8ba312bc | -11.56485 | -47.08608 | 2025-07-17 00:24:00 | TERRA_M-M | PORTO ALEGRE DO TOCANTINS | TOCANTINS | Brasil | 1718006 | 17 | 33 | nan | nan | nan | Cerrado | 5.9 |
| 388a5765-cff4-37fb-aa73-e66d45754581 | -9.41346 | -48.42242 | 2025-07-17 00:24:00 | TERRA_M-M | MIRACEMA DO TOCANTINS | TOCANTINS | Brasil | 1713205 | 17 | 33 | nan | nan | nan | Cerrado | 10.2 |
| e1768e19-300f-3c19-aa26-05c359e428ad | -8.88955 | -50.15733 | 2025-07-17 00:24:00 | TERRA_M-M | SANTA MARIA DAS BARREIRAS | PARÁ | Brasil | 1506583 | 15 | 33 | nan | nan | nan | Amazônia | 11.7 |
| 84141112-8712-3db2-b6ec-a7e203c68dc8 | -9.24807 | -48.56351 | 2025-07-17 00:24:00 | TERRA_M-M | RIO DOS BOIS | TOCANTINS | Brasil | 1718709 | 17 | 33 | nan | nan | nan | Cerrado | 209.0 |
| c96dc348-e68e-3c59-887a-4fbeb30bb397 | -8.04328 | -49.89445 | 2025-07-17 00:24:00 | TERRA_M-M | CONCEIÇÃO DO ARAGUAIA | PARÁ | Brasil | 1502707 | 15 | 33 | nan | nan | nan | Amazônia | 17.0 |
| 6cb34b19-a493-3922-89cb-2cda21022dfd | -8.54204 | -47.85517 | 2025-07-17 00:24:00 | TERRA_M-M | ITACAJÁ | TOCANTINS | Brasil | 1710508 | 17 | 33 | nan | nan | nan | Cerrado | 30.2 |
| 159b3542-be3d-32bb-9ee4-412813a0cbbf | -12.47554 | -44.49396 | 2025-07-17 00:24:00 | TERRA_M-M | BAIANÓPOLIS | BAHIA | Brasil | 2902500 | 29 | 33 | nan | nan | nan | Cerrado | 5.7 |
| ee17d014-2a39-311f-802e-c9effbf8b422 | -11.35794 | -48.73563 | 2025-07-17 00:24:00 | TERRA_M-M | GURUPI | TOCANTINS | Brasil | 1709500 | 17 | 33 | nan | nan | nan | Cerrado | 17.2 |


[Clique aqui para ver as próximas entradas](README5.md)
