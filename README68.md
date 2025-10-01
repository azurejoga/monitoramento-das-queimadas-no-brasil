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

## Dados Diários - Página 68

| ID | Latitude | Longitude | Data/Hora GMT | Satélite | Município | Estado | País | Município ID | Estado ID | País ID | Dias sem Chuva | Precipitação | Risco de Fogo | Bioma | FRP |
|----|----------|-----------|---------------|----------|-----------|--------|------|--------------|-----------|---------|----------------|--------------|----------------|-------|-----|
| d5dc83cb-3d92-3bd4-82e0-8a6d52f27fa8 | -13.47842 | -43.70617 | 2025-10-01 04:21:00 | NOAA-21 | SERRA DO RAMALHO | BAHIA | Brasil | 2930154 | 29 | 33 | nan | nan | nan | Cerrado | 0.8 |
| 562ce0ca-f897-3c7f-a536-0af2d98dcd99 | -17.63116 | -41.49422 | 2025-10-01 04:21:00 | NOAA-21 | TEÓFILO OTONI | MINAS GERAIS | Brasil | 3168606 | 31 | 33 | nan | nan | nan | Mata Atlântica | 2.1 |
| 42eaa479-c3c4-3d22-a7aa-fcf9fbc49042 | -11.12863 | -49.78053 | 2025-10-01 04:21:00 | NOAA-21 | DUERÉ | TOCANTINS | Brasil | 1707306 | 17 | 33 | nan | nan | nan | Cerrado | 1.6 |
| 2887dae9-3f30-3e9b-9b26-8630d718d47b | -13.09218 | -47.04235 | 2025-10-01 04:21:00 | NOAA-21 | ARRAIAS | TOCANTINS | Brasil | 1702406 | 17 | 33 | nan | nan | nan | Cerrado | 0.9 |
| d8d660a4-d5e8-347c-9f55-c4a3e0ea5917 | -13.77302 | -47.97561 | 2025-10-01 04:21:00 | NOAA-21 | CAVALCANTE | GOIÁS | Brasil | 5205307 | 52 | 33 | nan | nan | nan | Cerrado | 6.6 |
| 391a1d8b-4505-312a-a266-b8280c4f24d8 | -15.49244 | -45.91705 | 2025-10-01 04:21:00 | NOAA-21 | ARINOS | MINAS GERAIS | Brasil | 3104502 | 31 | 33 | nan | nan | nan | Cerrado | 3.0 |
| a6d2a395-14c0-3e5b-bea8-0b11938ef414 | -12.95667 | -48.43436 | 2025-10-01 04:21:00 | NOAA-21 | PALMEIRÓPOLIS | TOCANTINS | Brasil | 1715754 | 17 | 33 | nan | nan | nan | Cerrado | 2.9 |
| 3fce4957-637f-3dd5-8155-8b3ade0f3af9 | -15.39841 | -44.98016 | 2025-10-01 04:21:00 | NOAA-21 | JANUÁRIA | MINAS GERAIS | Brasil | 3135209 | 31 | 33 | nan | nan | nan | Cerrado | 1.8 |
| d167c4b4-047b-3cfa-bbf2-fd138286c1ed | -13.70205 | -48.6454 | 2025-10-01 04:21:00 | NOAA-21 | CAMPINAÇU | GOIÁS | Brasil | 5204656 | 52 | 33 | nan | nan | nan | Cerrado | 2.0 |
| 3b9cd26c-bbd1-3255-a002-05b274a59466 | -12.79405 | -46.88346 | 2025-10-01 04:21:00 | NOAA-21 | ARRAIAS | TOCANTINS | Brasil | 1702406 | 17 | 33 | nan | nan | nan | Cerrado | 1.0 |
| 75c9b362-6d3e-31f1-9540-5aa62f70b94e | -13.54256 | -47.27038 | 2025-10-01 04:21:00 | NOAA-21 | CAVALCANTE | GOIÁS | Brasil | 5205307 | 52 | 33 | nan | nan | nan | Cerrado | 2.9 |
| 1eb0c7a7-f0fd-34fc-ae89-cb1b1d70d413 | -16.38231 | -47.04786 | 2025-10-01 04:21:00 | NOAA-21 | UNAÍ | MINAS GERAIS | Brasil | 3170404 | 31 | 33 | nan | nan | nan | Cerrado | 1.2 |
| 507234ae-24eb-3b16-82fc-dfbcd0b1e5bd | -12.77383 | -44.22487 | 2025-10-01 04:21:00 | NOAA-21 | BAIANÓPOLIS | BAHIA | Brasil | 2902500 | 29 | 33 | nan | nan | nan | Cerrado | 0.3 |
| 1afd1954-205d-3e74-9b6c-5df97ef481ca | -15.48728 | -48.54964 | 2025-10-01 04:21:00 | NOAA-21 | PADRE BERNARDO | GOIÁS | Brasil | 5215603 | 52 | 33 | nan | nan | nan | Cerrado | 3.8 |
| 982bc17d-20a8-32a9-b319-42ef1670c3b7 | -14.70262 | -48.22776 | 2025-10-01 04:21:00 | NOAA-21 | NIQUELÂNDIA | GOIÁS | Brasil | 5214606 | 52 | 33 | nan | nan | nan | Cerrado | 1.5 |
| 7572500c-9078-3367-acf1-130122224c1c | -13.66937 | -48.05016 | 2025-10-01 04:21:00 | NOAA-21 | CAVALCANTE | GOIÁS | Brasil | 5205307 | 52 | 33 | nan | nan | nan | Cerrado | 3.1 |
| 394539bd-3b34-37fb-99e3-ff73c8a493a3 | -10.83083 | -45.38469 | 2025-10-01 04:21:00 | NOAA-21 | FORMOSA DO RIO PRETO | BAHIA | Brasil | 2911105 | 29 | 33 | nan | nan | nan | Cerrado | 1.6 |
| 48f94c3f-6cb1-353a-97b8-51a80e272963 | -15.26374 | -49.25803 | 2025-10-01 04:21:00 | NOAA-21 | GOIANÉSIA | GOIÁS | Brasil | 5208608 | 52 | 33 | nan | nan | nan | Cerrado | 2.9 |
| f129e358-7f89-3357-9a2d-d6e0063493d0 | -15.85582 | -46.25298 | 2025-10-01 04:21:00 | NOAA-21 | ARINOS | MINAS GERAIS | Brasil | 3104502 | 31 | 33 | nan | nan | nan | Cerrado | 1.5 |
| bfc67c35-17af-32d9-b2a4-7ce0cb26fcc1 | -13.09881 | -47.04345 | 2025-10-01 04:21:00 | NOAA-21 | ARRAIAS | TOCANTINS | Brasil | 1702406 | 17 | 33 | nan | nan | nan | Cerrado | 1.0 |
| 2840840c-3d8b-3fc0-95a3-21bd4b65636b | -9.52045 | -54.74038 | 2025-10-01 04:21:00 | NOAA-21 | NOVO PROGRESSO | PARÁ | Brasil | 1505031 | 15 | 33 | nan | nan | nan | Amazônia | 1.1 |
| 46c2e0f0-7a31-31a6-901d-30f9f79909f4 | -13.79434 | -48.02558 | 2025-10-01 04:21:00 | NOAA-21 | COLINAS DO SUL | GOIÁS | Brasil | 5205521 | 52 | 33 | nan | nan | nan | Cerrado | 1.8 |
| eb9e24c0-6432-3eb5-9f7f-ba90a6532135 | -14.04563 | -47.99168 | 2025-10-01 04:21:00 | NOAA-21 | COLINAS DO SUL | GOIÁS | Brasil | 5205521 | 52 | 33 | nan | nan | nan | Cerrado | 1.6 |
| 2473cd59-17ed-3373-b5a2-9c1da1581f59 | -13.13677 | -47.42077 | 2025-10-01 04:21:00 | NOAA-21 | ARRAIAS | TOCANTINS | Brasil | 1702406 | 17 | 33 | nan | nan | nan | Cerrado | 2.7 |
| 6238c4df-abae-3a68-819a-6543ccd3d4e1 | -11.76023 | -46.83305 | 2025-10-01 04:21:00 | NOAA-21 | DIANÓPOLIS | TOCANTINS | Brasil | 1707009 | 17 | 33 | nan | nan | nan | Cerrado | 2.5 |
| 00098826-33de-30bb-b85c-c15bcfdac982 | -10.12827 | -45.67876 | 2025-10-01 04:21:00 | NOAA-21 | BARREIRAS DO PIAUÍ | PIAUÍ | Brasil | 2201309 | 22 | 33 | nan | nan | nan | Cerrado | 1.9 |
| 2159462e-d090-305c-844a-edf61203085e | -12.95168 | -48.42171 | 2025-10-01 04:21:00 | NOAA-21 | PALMEIRÓPOLIS | TOCANTINS | Brasil | 1715754 | 17 | 33 | nan | nan | nan | Cerrado | 2.2 |
| 915ab5c0-95b9-39e5-aa1c-4b2d685d4e68 | -12.9601 | -48.43499 | 2025-10-01 04:21:00 | NOAA-21 | PALMEIRÓPOLIS | TOCANTINS | Brasil | 1715754 | 17 | 33 | nan | nan | nan | Cerrado | 2.9 |
| 538a3d45-d5db-37ca-ba26-3b5fe843c5ee | -11.84975 | -44.99754 | 2025-10-01 04:21:00 | NOAA-21 | RIACHÃO DAS NEVES | BAHIA | Brasil | 2926202 | 29 | 33 | nan | nan | nan | Cerrado | 12.6 |
| 5fe0bc7e-769c-3ddd-beea-bf0f5e9c5bc8 | -10.91219 | -44.27596 | 2025-10-01 04:21:00 | NOAA-21 | SANTA RITA DE CÁSSIA | BAHIA | Brasil | 2928406 | 29 | 33 | nan | nan | nan | Cerrado | 1.0 |
| 52548ec9-d6bb-393d-95de-d173c4bafac7 | -11.73638 | -44.42836 | 2025-10-01 04:21:00 | NOAA-21 | COTEGIPE | BAHIA | Brasil | 2909406 | 29 | 33 | nan | nan | nan | Cerrado | 2.2 |
| e94395f5-f6d5-3f2c-bedb-1318e902478a | -14.90686 | -48.12129 | 2025-10-01 04:21:00 | NOAA-21 | MIMOSO DE GOIÁS | GOIÁS | Brasil | 5213053 | 52 | 33 | nan | nan | nan | Cerrado | 1.5 |
| cbba8791-1bdb-38b4-abc6-0ac39e7d9281 | -12.82446 | -47.01244 | 2025-10-01 04:21:00 | NOAA-21 | ARRAIAS | TOCANTINS | Brasil | 1702406 | 17 | 33 | nan | nan | nan | Cerrado | 4.4 |
| 1436a8fb-a63a-3da7-b00c-330d6129844c | -12.46671 | -50.21843 | 2025-10-01 04:21:00 | NOAA-21 | SÃO MIGUEL DO ARAGUAIA | GOIÁS | Brasil | 5220207 | 52 | 33 | nan | nan | nan | Cerrado | 3.6 |
| 256b56f5-8447-38e1-a708-2c8108d1e313 | -11.68435 | -44.29227 | 2025-10-01 04:21:00 | NOAA-21 | COTEGIPE | BAHIA | Brasil | 2909406 | 29 | 33 | nan | nan | nan | Cerrado | 1.8 |
| 5a4f69a7-cee2-31d8-99bd-312d2506d16c | -10.62344 | -48.60023 | 2025-10-01 04:21:00 | NOAA-21 | PORTO NACIONAL | TOCANTINS | Brasil | 1718204 | 17 | 33 | nan | nan | nan | Cerrado | 5.0 |
| d8fbf2b8-8841-37fe-96a0-d9ceece1be4d | -11.84714 | -48.05902 | 2025-10-01 04:21:00 | NOAA-21 | SÃO VALÉRIO | TOCANTINS | Brasil | 1720499 | 17 | 33 | nan | nan | nan | Cerrado | 2.2 |
| ea44d314-0e34-33f7-a5d2-76c02e21040e | -15.91821 | -46.22265 | 2025-10-01 04:21:00 | NOAA-21 | ARINOS | MINAS GERAIS | Brasil | 3104502 | 31 | 33 | nan | nan | nan | Cerrado | 1.6 |
| a221f2b3-9914-393e-a699-cc43f4cdc6d2 | -15.28439 | -46.40875 | 2025-10-01 04:21:00 | NOAA-21 | BURITIS | MINAS GERAIS | Brasil | 3109303 | 31 | 33 | nan | nan | nan | Cerrado | 1.3 |
| 1eb637f2-3284-3775-a93c-8a0193d4b701 | -12.9355 | -47.2137 | 2025-10-01 04:21:00 | NOAA-21 | ARRAIAS | TOCANTINS | Brasil | 1702406 | 17 | 33 | nan | nan | nan | Cerrado | 1.6 |
| 5691c7ca-bf1f-39ab-b270-2b878f016f30 | -15.36863 | -46.10402 | 2025-10-01 04:21:00 | NOAA-21 | FORMOSO | MINAS GERAIS | Brasil | 3126208 | 31 | 33 | nan | nan | nan | Cerrado | 1.2 |
| ffe578fe-47e7-3c3b-a49a-b950999fc3ed | -10.67188 | -48.54911 | 2025-10-01 04:21:00 | NOAA-21 | PORTO NACIONAL | TOCANTINS | Brasil | 1718204 | 17 | 33 | nan | nan | nan | Cerrado | 2.3 |
| e4858535-1246-334e-a058-28340bbae88b | -15.28384 | -47.83367 | 2025-10-01 04:21:00 | NOAA-21 | PLANALTINA | GOIÁS | Brasil | 5217609 | 52 | 33 | nan | nan | nan | Cerrado | 1.4 |
| c58345b6-f1c2-314e-b17e-06955dbbe160 | -15.83539 | -46.25338 | 2025-10-01 04:21:00 | NOAA-21 | ARINOS | MINAS GERAIS | Brasil | 3104502 | 31 | 33 | nan | nan | nan | Cerrado | 1.9 |
| 0a2f8ca4-6ac7-3920-a020-9e30d5db32af | -13.76864 | -47.96001 | 2025-10-01 04:21:00 | NOAA-21 | CAVALCANTE | GOIÁS | Brasil | 5205307 | 52 | 33 | nan | nan | nan | Cerrado | 6.0 |
| 4e3c4c7c-62af-3f24-a992-453f2603f26e | -14.90748 | -48.11751 | 2025-10-01 04:21:00 | NOAA-21 | MIMOSO DE GOIÁS | GOIÁS | Brasil | 5213053 | 52 | 33 | nan | nan | nan | Cerrado | 1.1 |
| 8ca0d9f2-8102-3677-bf7a-151865edcd15 | -15.23848 | -48.73546 | 2025-10-01 04:21:00 | NOAA-21 | VILA PROPÍCIO | GOIÁS | Brasil | 5222302 | 52 | 33 | nan | nan | nan | Cerrado | 5.7 |
| 2512115c-c6d6-32bf-b1ac-86d79d997180 | -14.19609 | -46.10046 | 2025-10-01 04:21:00 | NOAA-21 | POSSE | GOIÁS | Brasil | 5218300 | 52 | 33 | nan | nan | nan | Cerrado | 1.7 |
| d3dc5d0f-05ba-3134-aa1f-9bc7d8a66757 | -14.5934 | -48.22892 | 2025-10-01 04:21:00 | NOAA-21 | NIQUELÂNDIA | GOIÁS | Brasil | 5214606 | 52 | 33 | nan | nan | nan | Cerrado | 3.4 |
| 960cf8c7-7080-3c77-bdcc-9de0a51c6baf | -11.82199 | -44.97851 | 2025-10-01 04:21:00 | NOAA-21 | RIACHÃO DAS NEVES | BAHIA | Brasil | 2926202 | 29 | 33 | nan | nan | nan | Cerrado | 6.1 |
| 998931b7-d600-3338-a389-37f8a6c8090b | -11.87111 | -48.02015 | 2025-10-01 04:21:00 | NOAA-21 | SÃO VALÉRIO | TOCANTINS | Brasil | 1720499 | 17 | 33 | nan | nan | nan | Cerrado | 2.4 |
| bea57f88-be75-3da3-a74a-d0dd80d0f811 | -16.40816 | -47.05586 | 2025-10-01 04:21:00 | NOAA-21 | UNAÍ | MINAS GERAIS | Brasil | 3170404 | 31 | 33 | nan | nan | nan | Cerrado | 3.6 |
| 79d08e0d-520d-3f66-a52a-dd7cf5aa9974 | -12.82389 | -47.01602 | 2025-10-01 04:21:00 | NOAA-21 | ARRAIAS | TOCANTINS | Brasil | 1702406 | 17 | 33 | nan | nan | nan | Cerrado | 4.5 |
| d01214dd-25f2-3cb4-a9d9-d24369967fd0 | -14.97825 | -50.78431 | 2025-10-01 04:21:00 | NOAA-21 | ARAGUAPAZ | GOIÁS | Brasil | 5202155 | 52 | 33 | nan | nan | nan | Cerrado | 4.1 |
| ae4e7332-10e4-3cd9-b7ea-ed63723fdbdc | -15.16869 | -52.81111 | 2025-10-01 04:21:00 | NOAA-21 | BARRA DO GARÇAS | MATO GROSSO | Brasil | 5101803 | 51 | 33 | nan | nan | nan | Cerrado | 2.9 |
| db2571c0-8099-3e69-a3a7-f6e9ef28181d | -15.26938 | -49.28822 | 2025-10-01 04:21:00 | NOAA-21 | GOIANÉSIA | GOIÁS | Brasil | 5208608 | 52 | 33 | nan | nan | nan | Cerrado | 2.7 |
| c9bfe0bd-c7a9-3f1e-a149-d793d21712ed | -13.76899 | -51.22128 | 2025-10-01 04:21:00 | NOAA-21 | COCALINHO | MATO GROSSO | Brasil | 5103106 | 51 | 33 | nan | nan | nan | Cerrado | 0.9 |
| 7c477b89-8aac-3ddb-8dc2-e7168059ab50 | -15.48329 | -48.55281 | 2025-10-01 04:21:00 | NOAA-21 | PADRE BERNARDO | GOIÁS | Brasil | 5215603 | 52 | 33 | nan | nan | nan | Cerrado | 3.8 |
| f34bff09-b3ce-3129-8b14-83c634957eea | -13.66516 | -48.07618 | 2025-10-01 04:21:00 | NOAA-21 | CAVALCANTE | GOIÁS | Brasil | 5205307 | 52 | 33 | nan | nan | nan | Cerrado | 4.0 |
| c0282521-6dfe-335e-af94-811c7a7476de | -12.87535 | -44.59952 | 2025-10-01 04:21:00 | NOAA-21 | SÃO DESIDÉRIO | BAHIA | Brasil | 2928901 | 29 | 33 | nan | nan | nan | Cerrado | 1.8 |
| f263427f-05a3-3a95-9177-c6dc26305719 | -17.40252 | -47.1566 | 2025-10-01 04:21:00 | NOAA-21 | PARACATU | MINAS GERAIS | Brasil | 3147006 | 31 | 33 | nan | nan | nan | Cerrado | 4.3 |
| 3fa7e1c9-e179-37e3-95bb-267b4cbb48e0 | -15.18271 | -46.40686 | 2025-10-01 04:21:00 | NOAA-21 | FORMOSO | MINAS GERAIS | Brasil | 3126208 | 31 | 33 | nan | nan | nan | Cerrado | 1.0 |
| 8ad12914-115b-3ea9-8775-5f783ebc7417 | -15.24588 | -48.73308 | 2025-10-01 04:21:00 | NOAA-21 | VILA PROPÍCIO | GOIÁS | Brasil | 5222302 | 52 | 33 | nan | nan | nan | Cerrado | 2.0 |
| 4c0f1d5d-d7da-30b9-bc56-fcfcdc48db7c | -14.05065 | -45.02174 | 2025-10-01 04:21:00 | NOAA-21 | JABORANDI | BAHIA | Brasil | 2917359 | 29 | 33 | nan | nan | nan | Cerrado | 0.7 |
| d8b4d388-b588-33cf-a61c-f9502da6f728 | -15.81802 | -41.88999 | 2025-10-01 04:21:00 | NOAA-21 | TAIOBEIRAS | MINAS GERAIS | Brasil | 3168002 | 31 | 33 | nan | nan | nan | Cerrado | 6.7 |
| 34e736e0-c80f-3391-b7bd-5e82ded7bfe9 | -15.69492 | -46.25964 | 2025-10-01 04:21:00 | NOAA-21 | ARINOS | MINAS GERAIS | Brasil | 3104502 | 31 | 33 | nan | nan | nan | Cerrado | 1.0 |
| 3de1324b-4011-30cb-942e-099415b349ed | -10.91688 | -44.33629 | 2025-10-01 04:21:00 | NOAA-21 | SANTA RITA DE CÁSSIA | BAHIA | Brasil | 2928406 | 29 | 33 | nan | nan | nan | Cerrado | 1.0 |
| 4bea1d25-b90c-36e4-9712-b45ff32b09f1 | -16.08993 | -51.04192 | 2025-10-01 04:21:00 | NOAA-21 | FAZENDA NOVA | GOIÁS | Brasil | 5207600 | 52 | 33 | nan | nan | nan | Cerrado | 2.6 |
| 5706c375-9234-31b1-aee9-89b59f2531b3 | -15.26058 | -47.89294 | 2025-10-01 04:21:00 | NOAA-21 | PLANALTINA | GOIÁS | Brasil | 5217609 | 52 | 33 | nan | nan | nan | Cerrado | 1.1 |
| b845d8bd-2fdc-39ad-a72b-ccc43b3b1f99 | -10.90264 | -44.27074 | 2025-10-01 04:21:00 | NOAA-21 | SANTA RITA DE CÁSSIA | BAHIA | Brasil | 2928406 | 29 | 33 | nan | nan | nan | Cerrado | 1.5 |
| a587a9bd-37ef-34bc-861d-2840a12443d9 | -10.44694 | -48.0849 | 2025-10-01 04:21:00 | NOAA-21 | PALMAS | TOCANTINS | Brasil | 1721000 | 17 | 33 | nan | nan | nan | Cerrado | 3.6 |
| 6e9dad19-a25b-3b97-b32b-bce9b340521d | -16.29554 | -48.97938 | 2025-10-01 04:21:00 | NOAA-21 | ANÁPOLIS | GOIÁS | Brasil | 5201108 | 52 | 33 | nan | nan | nan | Cerrado | 1.7 |
| e1e37536-c1cb-3aab-a600-8c1d3f8df08c | -14.1994 | -46.10099 | 2025-10-01 04:21:00 | NOAA-21 | POSSE | GOIÁS | Brasil | 5218300 | 52 | 33 | nan | nan | nan | Cerrado | 1.0 |
| 8b8396d0-4a3c-38e1-98cb-2f3fbb46330d | -16.38073 | -47.01459 | 2025-10-01 04:21:00 | NOAA-21 | UNAÍ | MINAS GERAIS | Brasil | 3170404 | 31 | 33 | nan | nan | nan | Cerrado | 0.9 |
| baa390af-361b-3624-8e7e-d23ddb3f518f | -10.64603 | -48.52882 | 2025-10-01 04:21:00 | NOAA-21 | PORTO NACIONAL | TOCANTINS | Brasil | 1718204 | 17 | 33 | nan | nan | nan | Cerrado | 2.8 |
| f0f5e81c-fe2f-34cd-b821-df75bd1a01e0 | -13.06148 | -47.08478 | 2025-10-01 04:21:00 | NOAA-21 | ARRAIAS | TOCANTINS | Brasil | 1702406 | 17 | 33 | nan | nan | nan | Cerrado | 1.5 |
| 6ee34c6c-548e-3933-9d9f-c3c442595d50 | -14.88427 | -48.32294 | 2025-10-01 04:21:00 | NOAA-21 | NIQUELÂNDIA | GOIÁS | Brasil | 5214606 | 52 | 33 | nan | nan | nan | Cerrado | 3.6 |
| 27fc7d42-3e96-39fc-9726-fe6435c89e77 | -14.99557 | -46.95134 | 2025-10-01 04:21:00 | NOAA-21 | VILA BOA | GOIÁS | Brasil | 5222203 | 52 | 33 | nan | nan | nan | Cerrado | 4.1 |
| e15281e1-809e-34ee-8711-b61a5410035c | -13.70138 | -48.64939 | 2025-10-01 04:21:00 | NOAA-21 | CAMPINAÇU | GOIÁS | Brasil | 5204656 | 52 | 33 | nan | nan | nan | Cerrado | 2.0 |
| f3f8e96c-160c-373f-a546-c1d3a2833c3c | -15.54317 | -44.3304 | 2025-10-01 04:21:00 | NOAA-21 | PEDRAS DE MARIA DA CRUZ | MINAS GERAIS | Brasil | 3149150 | 31 | 33 | nan | nan | nan | Caatinga | 7.1 |
| 1fb51aee-1aab-3a6c-bdb8-418937b9a0ac | -11.76401 | -46.85207 | 2025-10-01 04:21:00 | NOAA-21 | DIANÓPOLIS | TOCANTINS | Brasil | 1707009 | 17 | 33 | nan | nan | nan | Cerrado | 12.2 |
| 543bb92a-5e64-3e09-a10d-38effe475495 | -14.61057 | -48.20855 | 2025-10-01 04:21:00 | NOAA-21 | NIQUELÂNDIA | GOIÁS | Brasil | 5214606 | 52 | 33 | nan | nan | nan | Cerrado | 1.5 |
| 9aed880f-a7ad-30b1-ba61-5a6f7289748a | -11.46228 | -45.08565 | 2025-10-01 04:21:00 | NOAA-21 | RIACHÃO DAS NEVES | BAHIA | Brasil | 2926202 | 29 | 33 | nan | nan | nan | Cerrado | 2.5 |
| fec50fa1-584c-305a-83f6-386bccb64eab | -11.67688 | -45.32585 | 2025-10-01 04:21:00 | NOAA-21 | RIACHÃO DAS NEVES | BAHIA | Brasil | 2926202 | 29 | 33 | nan | nan | nan | Cerrado | 0.9 |
| e786c09b-0c0f-3c6b-8413-08d907f53ca9 | -9.4271 | -54.71878 | 2025-10-01 04:21:00 | NOAA-21 | NOVO PROGRESSO | PARÁ | Brasil | 1505031 | 15 | 33 | nan | nan | nan | Amazônia | 2.3 |
| d18a6c80-005a-30b9-80a3-14479f8c7518 | -10.91384 | -44.26501 | 2025-10-01 04:21:00 | NOAA-21 | SANTA RITA DE CÁSSIA | BAHIA | Brasil | 2928406 | 29 | 33 | nan | nan | nan | Cerrado | 1.5 |
| a8f4d70e-ba9b-3450-b9e8-dffe6f82bb28 | -13.21457 | -47.34131 | 2025-10-01 04:21:00 | NOAA-21 | ARRAIAS | TOCANTINS | Brasil | 1702406 | 17 | 33 | nan | nan | nan | Cerrado | 5.6 |
| ba95e964-268e-3390-9307-f318ac6a9a85 | -11.8425 | -44.9781 | 2025-10-01 04:21:00 | NOAA-21 | RIACHÃO DAS NEVES | BAHIA | Brasil | 2926202 | 29 | 33 | nan | nan | nan | Cerrado | 5.6 |
| 3e8ad10b-521c-3b22-ae23-3e92106bc636 | -10.43344 | -50.86452 | 2025-10-01 04:21:00 | NOAA-21 | SANTA TEREZINHA | MATO GROSSO | Brasil | 5107776 | 51 | 33 | nan | nan | nan | Cerrado | 1.3 |
| fc217970-3aca-3a2c-b558-61051ab05393 | -11.09745 | -47.71875 | 2025-10-01 04:21:00 | NOAA-21 | PINDORAMA DO TOCANTINS | TOCANTINS | Brasil | 1717008 | 17 | 33 | nan | nan | nan | Cerrado | 1.4 |
| e9fe5b8b-ef71-3f2f-b1f1-058a2cff3288 | -16.2458 | -50.93715 | 2025-10-01 04:21:00 | NOAA-21 | JAUPACI | GOIÁS | Brasil | 5212006 | 52 | 33 | nan | nan | nan | Cerrado | 9.1 |
| 597dd315-e633-3d20-9360-b60e3e4502b6 | -13.33039 | -47.82529 | 2025-10-01 04:21:00 | NOAA-21 | CAVALCANTE | GOIÁS | Brasil | 5205307 | 52 | 33 | nan | nan | nan | Cerrado | 3.2 |
| a4fbf062-3021-3623-9046-13886777daa0 | -15.5327 | -44.35328 | 2025-10-01 04:21:00 | NOAA-21 | PEDRAS DE MARIA DA CRUZ | MINAS GERAIS | Brasil | 3149150 | 31 | 33 | nan | nan | nan | Caatinga | 1.2 |
| e1a59293-3c33-3bf8-9f94-f5fe8041d28c | -10.03661 | -52.10107 | 2025-10-01 04:21:00 | NOAA-21 | VILA RICA | MATO GROSSO | Brasil | 5108600 | 51 | 33 | nan | nan | nan | Amazônia | 4.4 |
| 5e62b4af-f832-37c0-a97c-be1c64c26a8b | -14.79075 | -45.79385 | 2025-10-01 04:21:00 | NOAA-21 | COCOS | BAHIA | Brasil | 2908101 | 29 | 33 | nan | nan | nan | Cerrado | 5.9 |
| 32204ecf-d21c-397e-9a62-7753f7bcd148 | -9.51453 | -54.74268 | 2025-10-01 04:21:00 | NOAA-21 | NOVO PROGRESSO | PARÁ | Brasil | 1505031 | 15 | 33 | nan | nan | nan | Amazônia | 1.1 |
| 83f4234c-83b6-30cf-b283-8d1f9833d6ed | -11.43823 | -43.50134 | 2025-10-01 04:21:00 | NOAA-21 | BARRA | BAHIA | Brasil | 2902708 | 29 | 33 | nan | nan | nan | Cerrado | 0.8 |
| 8f4e3bfd-5811-3ef1-a70d-b461a60c90ca | -10.91045 | -46.50476 | 2025-10-01 04:21:00 | NOAA-21 | MATEIROS | TOCANTINS | Brasil | 1712702 | 17 | 33 | nan | nan | nan | Cerrado | 84.8 |
| 3307eb02-1d03-3fba-ab8e-1e08dd94e773 | -15.53569 | -45.21642 | 2025-10-01 04:21:00 | NOAA-21 | CHAPADA GAÚCHA | MINAS GERAIS | Brasil | 3116159 | 31 | 33 | nan | nan | nan | Cerrado | 6.0 |
| e318b72f-56d4-308a-8faa-98ba66355530 | -13.91831 | -48.10318 | 2025-10-01 04:21:00 | NOAA-21 | COLINAS DO SUL | GOIÁS | Brasil | 5205521 | 52 | 33 | nan | nan | nan | Cerrado | 1.0 |


[Clique aqui para ver as próximas entradas](README69.md)
