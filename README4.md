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
| 96016572-38c4-34d0-b378-282c8904fbb1 | -21.49734 | -48.72713 | 2026-05-13 04:25:00 | NOAA-21 | ITÁPOLIS | SÃO PAULO | Brasil | 3522703 | 35 | 33 | nan | nan | nan | Cerrado | 2.4 |
| 12b7c5b8-5d0f-356a-964f-3653ea29b698 | -22.98462 | -49.17277 | 2026-05-13 04:25:00 | NOAA-21 | CERQUEIRA CÉSAR | SÃO PAULO | Brasil | 3511409 | 35 | 33 | nan | nan | nan | Cerrado | 1.1 |
| a48b9231-18fe-3862-b611-b59f292cd085 | -28.42401 | -50.04519 | 2026-05-13 04:25:00 | NOAA-21 | SÃO JOAQUIM | SANTA CATARINA | Brasil | 4216503 | 42 | 33 | nan | nan | nan | Mata Atlântica | 0.7 |
| a6fdf2ab-775b-370a-b891-8a28e4c5a02f | -23.40658 | -46.42107 | 2026-05-13 04:25:00 | NOAA-21 | GUARULHOS | SÃO PAULO | Brasil | 3518800 | 35 | 33 | nan | nan | nan | Mata Atlântica | 1.3 |
| 62e2bc36-4a78-3e21-b24c-9db59f20f1b1 | -22.98401 | -49.17653 | 2026-05-13 04:25:00 | NOAA-21 | CERQUEIRA CÉSAR | SÃO PAULO | Brasil | 3511409 | 35 | 33 | nan | nan | nan | Cerrado | 1.1 |
| 8b8e6859-d300-3c98-ab6e-13e6dda35416 | -22.70191 | -43.36096 | 2026-05-13 04:25:00 | NOAA-21 | BELFORD ROXO | RIO DE JANEIRO | Brasil | 3300456 | 33 | 33 | nan | nan | nan | Mata Atlântica | 1.6 |
| 6dad114d-505d-3e1c-b8b8-78089ccd65c8 | -22.87695 | -48.62955 | 2026-05-13 04:25:00 | NOAA-21 | BOTUCATU | SÃO PAULO | Brasil | 3507506 | 35 | 33 | nan | nan | nan | Cerrado | 1.0 |
| f3efd511-f129-343b-bd92-03edcc4bc2f1 | -22.70052 | -43.3626 | 2026-05-13 04:25:00 | NOAA-21 | BELFORD ROXO | RIO DE JANEIRO | Brasil | 3300456 | 33 | 33 | nan | nan | nan | Mata Atlântica | 1.4 |
| 99b7379a-144e-3d72-8885-64bd04c0a8cb | -21.8395 | -48.79961 | 2026-05-13 04:25:00 | NOAA-21 | IBITINGA | SÃO PAULO | Brasil | 3519600 | 35 | 33 | nan | nan | nan | Cerrado | 0.5 |
| 007ad610-ed35-3f87-9f9e-d90d94b178de | -21.97933 | -57.59086 | 2026-05-13 04:25:00 | NOAA-21 | PORTO MURTINHO | MATO GROSSO DO SUL | Brasil | 5006903 | 50 | 33 | nan | nan | nan | Cerrado | 1.9 |
| e1103595-fcf4-3a5f-9bd4-04ac5acf0b3e | -22.74041 | -42.24976 | 2026-05-13 04:25:00 | NOAA-21 | ARARUAMA | RIO DE JANEIRO | Brasil | 3300209 | 33 | 33 | nan | nan | nan | Mata Atlântica | 2.1 |
| e0e7fac6-55bc-367e-a52e-63a25ddd2002 | -22.81971 | -49.29006 | 2026-05-13 04:25:00 | NOAA-21 | ÁGUAS DE SANTA BÁRBARA | SÃO PAULO | Brasil | 3500550 | 35 | 33 | nan | nan | nan | Cerrado | 0.6 |
| d451f308-7045-3cda-8e5d-d72f68d5ce0f | -21.97421 | -57.58974 | 2026-05-13 04:25:00 | NOAA-21 | PORTO MURTINHO | MATO GROSSO DO SUL | Brasil | 5006903 | 50 | 33 | nan | nan | nan | Cerrado | 1.9 |
| ad54881d-f17a-38f9-aafe-f94d43dacfdf | -22.87365 | -48.62895 | 2026-05-13 04:25:00 | NOAA-21 | BOTUCATU | SÃO PAULO | Brasil | 3507506 | 35 | 33 | nan | nan | nan | Cerrado | 1.0 |
| f67bb7a9-df5b-30e2-a809-343b8b138d83 | -21.5004 | -48.72723 | 2026-05-13 04:25:00 | NOAA-21 | ITÁPOLIS | SÃO PAULO | Brasil | 3522703 | 35 | 33 | nan | nan | nan | Cerrado | 1.0 |
| 80ac6290-190c-305e-a998-e3b147077b11 | -28.33108 | -49.37146 | 2026-05-13 04:25:00 | NOAA-21 | ORLEANS | SANTA CATARINA | Brasil | 4211702 | 42 | 33 | nan | nan | nan | Mata Atlântica | 0.8 |
| 321ee087-cadd-3c18-bd9f-e4e26eb5f84c | -22.65472 | -47.09782 | 2026-05-13 04:25:00 | NOAA-21 | HOLAMBRA | SÃO PAULO | Brasil | 3519055 | 35 | 33 | nan | nan | nan | Cerrado | 0.6 |
| 11240247-8be7-38ac-ad58-3047d402df54 | -29.03035 | -51.51392 | 2026-05-13 04:27:00 | NOAA-21 | PINTO BANDEIRA | RIO GRANDE DO SUL | Brasil | 4314548 | 43 | 33 | nan | nan | nan | Mata Atlântica | 0.6 |
| 43be2032-4ad3-331d-a980-14b1cd9e6c86 | -8.70543 | -47.98027 | 2026-05-13 04:53:00 | NPP-375D | SANTA MARIA DO TOCANTINS | TOCANTINS | Brasil | 1718881 | 17 | 33 | nan | nan | nan | Cerrado | 2.1 |
| bd00e02b-dde8-365e-a325-e9af2e383f70 | -8.54378 | -45.98075 | 2026-05-13 04:53:00 | NPP-375D | TASSO FRAGOSO | MARANHÃO | Brasil | 2112001 | 21 | 33 | nan | nan | nan | Cerrado | 2.8 |
| 9357ac2b-5914-3e2d-b2b6-bc8a03696d0d | -7.27765 | -46.80273 | 2026-05-13 04:53:00 | NPP-375D | RIACHÃO | MARANHÃO | Brasil | 2109502 | 21 | 33 | nan | nan | nan | Cerrado | 1.4 |
| 9985c73c-2d28-347e-87de-f7d19af1f826 | -9.4574 | -47.78997 | 2026-05-13 04:53:00 | NPP-375D | RIO SONO | TOCANTINS | Brasil | 1718758 | 17 | 33 | nan | nan | nan | Cerrado | 1.5 |
| 946ed3de-e49a-3bcd-9140-bb040e5eeeb5 | -8.53899 | -45.98396 | 2026-05-13 04:53:00 | NPP-375D | TASSO FRAGOSO | MARANHÃO | Brasil | 2112001 | 21 | 33 | nan | nan | nan | Cerrado | 2.8 |
| 32302636-6e21-35c4-b7de-63734abd8719 | -8.74097 | -48.75282 | 2026-05-13 04:53:00 | NPP-375D | COLMÉIA | TOCANTINS | Brasil | 1716703 | 17 | 33 | nan | nan | nan | Amazônia | 1.4 |
| d4b3672d-0ef4-3cce-bc71-5d6bb1e5a3e3 | -7.27839 | -46.79765 | 2026-05-13 04:53:00 | NPP-375D | RIACHÃO | MARANHÃO | Brasil | 2109502 | 21 | 33 | nan | nan | nan | Cerrado | 1.4 |
| 242ced6d-84f4-3145-826f-5695d9b8472d | -8.70603 | -47.97868 | 2026-05-13 04:53:00 | NPP-375D | SANTA MARIA DO TOCANTINS | TOCANTINS | Brasil | 1718881 | 17 | 33 | nan | nan | nan | Cerrado | 2.1 |
| af8da6a2-b931-35fc-a1d4-acf455308518 | -8.70475 | -47.98476 | 2026-05-13 04:53:00 | NPP-375D | SANTA MARIA DO TOCANTINS | TOCANTINS | Brasil | 1718881 | 17 | 33 | nan | nan | nan | Cerrado | 2.1 |
| cd597f68-5639-3eb2-a4e3-470196267239 | -8.45043 | -49.57434 | 2026-05-13 04:53:00 | NPP-375D | CONCEIÇÃO DO ARAGUAIA | PARÁ | Brasil | 1502707 | 15 | 33 | nan | nan | nan | Amazônia | 1.0 |
| 9b9801d9-0dd0-354c-897b-333e3fa57c28 | -8.08814 | -44.17236 | 2026-05-13 04:53:00 | NPP-375D | SEBASTIÃO LEAL | PIAUÍ | Brasil | 2210631 | 22 | 33 | nan | nan | nan | Cerrado | 0.9 |
| 93dde974-4457-3b93-80a1-8e9858459dfa | -9.45288 | -47.79417 | 2026-05-13 04:53:00 | NPP-375D | RIO SONO | TOCANTINS | Brasil | 1718758 | 17 | 33 | nan | nan | nan | Cerrado | 3.8 |
| 220a6b54-4753-3585-9304-07c751a08cdb | -8.54322 | -45.9846 | 2026-05-13 04:53:00 | NPP-375D | TASSO FRAGOSO | MARANHÃO | Brasil | 2112001 | 21 | 33 | nan | nan | nan | Cerrado | 2.8 |
| 73bf7d94-025c-32a5-8022-11a80808b334 | -10.5522 | -42.43702 | 2026-05-13 04:53:00 | NPP-375D | XIQUE-XIQUE | BAHIA | Brasil | 2933604 | 29 | 33 | nan | nan | nan | Caatinga | 1.3 |
| 470cf96b-3bb6-3298-8d04-c76a15a37c6a | -10.55349 | -42.43911 | 2026-05-13 04:53:00 | NPP-375D | XIQUE-XIQUE | BAHIA | Brasil | 2933604 | 29 | 33 | nan | nan | nan | Caatinga | 1.2 |
| d8ea7f9d-d3e1-32be-b4a7-b9bb6d6a3463 | -8.70537 | -47.98319 | 2026-05-13 04:53:00 | NPP-375D | SANTA MARIA DO TOCANTINS | TOCANTINS | Brasil | 1718881 | 17 | 33 | nan | nan | nan | Cerrado | 2.1 |
| b0cf3a74-6121-3f8f-b027-ebd96f11e289 | -8.53955 | -45.98011 | 2026-05-13 04:53:00 | NPP-375D | TASSO FRAGOSO | MARANHÃO | Brasil | 2112001 | 21 | 33 | nan | nan | nan | Cerrado | 2.8 |
| 52b4607c-3c28-3112-96ab-f5a445bc649d | -8.09291 | -44.17303 | 2026-05-13 04:53:00 | NPP-375D | SEBASTIÃO LEAL | PIAUÍ | Brasil | 2210631 | 22 | 33 | nan | nan | nan | Cerrado | 0.9 |
| a3a8b8ce-71b2-3dfb-8d2f-be4ca90644fc | -8.85304 | -50.21437 | 2026-05-13 04:53:00 | NPP-375D | SANTA MARIA DAS BARREIRAS | PARÁ | Brasil | 1506583 | 15 | 33 | nan | nan | nan | Amazônia | 0.7 |
| 5c256faf-45dc-34b9-bfee-d64639c25917 | -9.4567 | -47.79474 | 2026-05-13 04:53:00 | NPP-375D | RIO SONO | TOCANTINS | Brasil | 1718758 | 17 | 33 | nan | nan | nan | Cerrado | 1.5 |
| 25381214-3aea-3d00-ba30-393064e4feb8 | -14.1155 | -45.31464 | 2026-05-13 04:55:00 | NPP-375D | JABORANDI | BAHIA | Brasil | 2917359 | 29 | 33 | nan | nan | nan | Cerrado | 1.4 |
| f2378dd4-263b-3ee8-bfed-26468f412cf7 | -14.19534 | -47.02293 | 2026-05-13 04:55:00 | NPP-375D | FLORES DE GOIÁS | GOIÁS | Brasil | 5207907 | 52 | 33 | nan | nan | nan | Cerrado | 0.5 |
| 7d853db0-8921-39c6-807c-d5ec86fb42b0 | -10.4056 | -46.65509 | 2026-05-13 04:55:00 | NPP-375D | MATEIROS | TOCANTINS | Brasil | 1712702 | 17 | 33 | nan | nan | nan | Cerrado | 3.8 |
| ff490e09-1958-3c3d-bb69-faa12222cf2c | -11.73267 | -54.2389 | 2026-05-13 04:55:00 | NPP-375D | UNIÃO DO SUL | MATO GROSSO | Brasil | 5108303 | 51 | 33 | nan | nan | nan | Amazônia | 0.6 |
| 2f9f001d-d221-31c8-a2cb-69ebc387768b | -11.63778 | -54.15771 | 2026-05-13 04:55:00 | NPP-375D | UNIÃO DO SUL | MATO GROSSO | Brasil | 5108303 | 51 | 33 | nan | nan | nan | Amazônia | 1.5 |
| 2212df3f-11b4-39e0-941b-3bff0e986b62 | -11.73826 | -54.24759 | 2026-05-13 04:55:00 | NPP-375D | UNIÃO DO SUL | MATO GROSSO | Brasil | 5108303 | 51 | 33 | nan | nan | nan | Amazônia | 2.9 |
| d383f389-8a9c-3212-8263-97c8353aada9 | -16.43489 | -54.9108 | 2026-05-13 04:55:00 | NPP-375D | RONDONÓPOLIS | MATO GROSSO | Brasil | 5107602 | 51 | 33 | nan | nan | nan | Cerrado | 0.6 |
| 343de739-5b80-32c8-b90f-41c48084be82 | -6.32944 | -44.62413 | 2026-05-13 04:55:00 | NPP-375D | MIRADOR | MARANHÃO | Brasil | 2106706 | 21 | 33 | nan | nan | nan | Cerrado | 3.4 |
| 34a65c0a-f6df-31d4-84b0-024f35919580 | -11.73609 | -54.23949 | 2026-05-13 04:55:00 | NPP-375D | UNIÃO DO SUL | MATO GROSSO | Brasil | 5108303 | 51 | 33 | nan | nan | nan | Amazônia | 1.4 |
| fe3cadf1-e21d-37f8-a7b6-89e8b67663e5 | -14.11491 | -45.31545 | 2026-05-13 04:55:00 | NPP-375D | JABORANDI | BAHIA | Brasil | 2917359 | 29 | 33 | nan | nan | nan | Cerrado | 1.9 |
| 3d1added-70cc-3b7a-a406-ce45816e7bc3 | -12.03533 | -54.25071 | 2026-05-13 04:55:00 | NPP-375D | FELIZ NATAL | MATO GROSSO | Brasil | 5103700 | 51 | 33 | nan | nan | nan | Amazônia | 1.5 |
| 8d82d924-2230-3949-a110-871f6f92bc5a | -4.06406 | -54.70599 | 2026-05-13 04:55:00 | NPP-375D | PLACAS | PARÁ | Brasil | 1505650 | 15 | 33 | nan | nan | nan | Amazônia | 1.0 |
| 0d6c9cd9-b5a5-3199-a6ca-c3344566aa9f | -13.03087 | -49.94414 | 2026-05-13 04:55:00 | NPP-375D | SÃO MIGUEL DO ARAGUAIA | GOIÁS | Brasil | 5220207 | 52 | 33 | nan | nan | nan | Cerrado | 1.4 |
| 56bcb9d4-8c4a-3713-a85e-a80e66417946 | -11.63381 | -54.16488 | 2026-05-13 04:55:00 | NPP-375D | UNIÃO DO SUL | MATO GROSSO | Brasil | 5108303 | 51 | 33 | nan | nan | nan | Amazônia | 0.9 |
| 846cef0f-c410-3f0d-b662-1c0deeae2f16 | -11.84135 | -49.44438 | 2026-05-13 04:55:00 | NPP-375D | FORMOSO DO ARAGUAIA | TOCANTINS | Brasil | 1708205 | 17 | 33 | nan | nan | nan | Cerrado | 1.0 |
| ad56ca5f-e1e5-3500-a940-065113ed61df | -12.11674 | -43.64423 | 2026-05-13 04:55:00 | NPP-375D | MUQUÉM DO SÃO FRANCISCO | BAHIA | Brasil | 2922250 | 29 | 33 | nan | nan | nan | Cerrado | 1.2 |
| 2bea913d-b7fc-3f91-a204-f80c00b47aea | -14.1258 | -45.31064 | 2026-05-13 04:55:00 | NPP-375D | JABORANDI | BAHIA | Brasil | 2917359 | 29 | 33 | nan | nan | nan | Cerrado | 1.9 |
| f1f08c2a-cc00-3439-92be-1cec5dbf2cd7 | -12.62522 | -44.52075 | 2026-05-13 04:55:00 | NPP-375D | BAIANÓPOLIS | BAHIA | Brasil | 2902500 | 29 | 33 | nan | nan | nan | Cerrado | 2.8 |
| a9024f59-d665-38d8-96f6-02f380ea8118 | -14.12998 | -45.31212 | 2026-05-13 04:55:00 | NPP-375D | JABORANDI | BAHIA | Brasil | 2917359 | 29 | 33 | nan | nan | nan | Cerrado | 1.2 |
| 448c2e7a-798e-30e9-8aa4-9b7410fa7744 | -11.18491 | -55.92543 | 2026-05-13 04:55:00 | NPP-375D | ITAÚBA | MATO GROSSO | Brasil | 5104559 | 51 | 33 | nan | nan | nan | Amazônia | 23.6 |
| ef8f6fe0-ad6a-324b-856e-2401443ed916 | -10.40662 | -46.65502 | 2026-05-13 04:55:00 | NPP-375D | MATEIROS | TOCANTINS | Brasil | 1712702 | 17 | 33 | nan | nan | nan | Cerrado | 5.2 |
| 2b2b6ca6-1258-390a-b721-298acfee9c21 | -12.04722 | -45.28728 | 2026-05-13 04:55:00 | NPP-375D | BARREIRAS | BAHIA | Brasil | 2903201 | 29 | 33 | nan | nan | nan | Cerrado | 0.9 |
| e159d1b7-7b61-348a-b950-5dafeeb86bec | -14.11962 | -45.32059 | 2026-05-13 04:55:00 | NPP-375D | JABORANDI | BAHIA | Brasil | 2917359 | 29 | 33 | nan | nan | nan | Cerrado | 1.1 |
| 5be18f41-4c75-34c6-8037-62b41705344f | -14.14756 | -45.40563 | 2026-05-13 04:55:00 | NPP-375D | JABORANDI | BAHIA | Brasil | 2917359 | 29 | 33 | nan | nan | nan | Cerrado | 1.2 |
| ab516b81-10aa-3676-b910-a19d9c5433ef | -14.13536 | -45.4254 | 2026-05-13 04:55:00 | NPP-375D | JABORANDI | BAHIA | Brasil | 2917359 | 29 | 33 | nan | nan | nan | Cerrado | 1.3 |
| ffbb3fe0-14d8-3d8c-9c71-1aed639db901 | -14.12511 | -45.31594 | 2026-05-13 04:55:00 | NPP-375D | JABORANDI | BAHIA | Brasil | 2917359 | 29 | 33 | nan | nan | nan | Cerrado | 1.1 |
| 6da7592d-4264-3579-96d7-f9161782f564 | -11.95721 | -54.68312 | 2026-05-13 04:55:00 | NPP-375D | SANTA CARMEM | MATO GROSSO | Brasil | 5107248 | 51 | 33 | nan | nan | nan | Amazônia | 0.9 |
| 7b94340c-b9dd-32e8-ab48-01771a8d319a | -11.63716 | -54.16145 | 2026-05-13 04:55:00 | NPP-375D | UNIÃO DO SUL | MATO GROSSO | Brasil | 5108303 | 51 | 33 | nan | nan | nan | Amazônia | 1.5 |
| e77f561f-97d9-39a5-a6f9-64e122852da1 | -12.85204 | -43.76056 | 2026-05-13 04:55:00 | NPP-375D | SERRA DOURADA | BAHIA | Brasil | 2930303 | 29 | 33 | nan | nan | nan | Cerrado | 1.3 |
| bfe4f3c0-fb5d-313f-b991-d942ae55149e | -16.46715 | -49.13116 | 2026-05-13 04:55:00 | NPP-375D | NERÓPOLIS | GOIÁS | Brasil | 5214507 | 52 | 33 | nan | nan | nan | Cerrado | 0.9 |
| 62928bb3-bfd8-3817-89d0-1273a57d1b11 | -11.98069 | -46.78559 | 2026-05-13 04:55:00 | NPP-375D | DIANÓPOLIS | TOCANTINS | Brasil | 1707009 | 17 | 33 | nan | nan | nan | Cerrado | 1.4 |
| 978fa6ab-8610-3c1b-9d68-727fd802976d | -14.14623 | -45.41615 | 2026-05-13 04:55:00 | NPP-375D | JABORANDI | BAHIA | Brasil | 2917359 | 29 | 33 | nan | nan | nan | Cerrado | 1.3 |
| 106e1abd-a1e8-3402-a00a-e7f27f543033 | -11.9717 | -46.78837 | 2026-05-13 04:55:00 | NPP-375D | DIANÓPOLIS | TOCANTINS | Brasil | 1707009 | 17 | 33 | nan | nan | nan | Cerrado | 1.7 |
| 4747ee14-089b-321e-9dcb-479c790a97af | -14.30755 | -49.24637 | 2026-05-13 04:55:00 | NPP-375D | NOVA IGUAÇU DE GOIÁS | GOIÁS | Brasil | 5214879 | 52 | 33 | nan | nan | nan | Cerrado | 1.2 |
| bcb472c2-19d7-32f9-860e-25eb1d4f7a36 | -11.4078 | -48.44673 | 2026-05-13 04:55:00 | NPP-375D | SÃO VALÉRIO | TOCANTINS | Brasil | 1720499 | 17 | 33 | nan | nan | nan | Cerrado | 0.9 |
| 0df57479-6a45-3884-a5e6-2c701a73886d | -14.13413 | -45.31808 | 2026-05-13 04:55:00 | NPP-375D | JABORANDI | BAHIA | Brasil | 2917359 | 29 | 33 | nan | nan | nan | Cerrado | 1.2 |
| 2328fcd2-70cc-3776-b49e-fcb2e83adb96 | -10.97063 | -45.09652 | 2026-05-13 04:55:00 | NPP-375D | FORMOSA DO RIO PRETO | BAHIA | Brasil | 2911105 | 29 | 33 | nan | nan | nan | Cerrado | 2.7 |
| 6bcdc0a3-a129-340f-80fe-59accc962857 | -11.93067 | -54.09913 | 2026-05-13 04:55:00 | NPP-375D | FELIZ NATAL | MATO GROSSO | Brasil | 5103700 | 51 | 33 | nan | nan | nan | Amazônia | 2.6 |
| 9d4dec15-a52f-32ac-8861-3d9fa5804d58 | -12.62522 | -44.52132 | 2026-05-13 04:55:00 | NPP-375D | BAIANÓPOLIS | BAHIA | Brasil | 2902500 | 29 | 33 | nan | nan | nan | Cerrado | 1.3 |
| 7c1912c1-aaf6-3d5a-8b12-c39dabdd7289 | -13.54243 | -49.90653 | 2026-05-13 04:55:00 | NPP-375D | BONÓPOLIS | GOIÁS | Brasil | 5203575 | 52 | 33 | nan | nan | nan | Cerrado | 0.8 |
| ba7101cd-2d04-3ace-ae4e-c3a4f43aa9c5 | -11.95657 | -54.68699 | 2026-05-13 04:55:00 | NPP-375D | SANTA CARMEM | MATO GROSSO | Brasil | 5107248 | 51 | 33 | nan | nan | nan | Amazônia | 0.8 |
| c781b881-1ee5-3067-8cf5-26312f6aee37 | -11.26797 | -55.78819 | 2026-05-13 04:55:00 | NPP-375D | ITAÚBA | MATO GROSSO | Brasil | 5104559 | 51 | 33 | nan | nan | nan | Amazônia | 0.8 |
| 5c8b574b-e34a-30c8-b062-439e6b4863b7 | -11.98492 | -46.78616 | 2026-05-13 04:55:00 | NPP-375D | DIANÓPOLIS | TOCANTINS | Brasil | 1707009 | 17 | 33 | nan | nan | nan | Cerrado | 2.1 |
| c6e2b202-b535-34d9-b170-b7bdfebade6a | -11.63161 | -54.15679 | 2026-05-13 04:55:00 | NPP-375D | UNIÃO DO SUL | MATO GROSSO | Brasil | 5108303 | 51 | 33 | nan | nan | nan | Amazônia | 1.7 |
| e3fbd9e6-abfe-3186-9c5e-e82e896d6ada | -11.93689 | -43.3819 | 2026-05-13 04:55:00 | NPP-375D | MUQUÉM DO SÃO FRANCISCO | BAHIA | Brasil | 2922250 | 29 | 33 | nan | nan | nan | Cerrado | 0.9 |
| 77f210ef-457a-336c-9618-dd01092686c6 | -12.11071 | -43.64991 | 2026-05-13 04:55:00 | NPP-375D | MUQUÉM DO SÃO FRANCISCO | BAHIA | Brasil | 2922250 | 29 | 33 | nan | nan | nan | Cerrado | 1.5 |
| 8368a8f9-d5ca-3c47-b991-11ecb0846f6f | -14.12933 | -45.31743 | 2026-05-13 04:55:00 | NPP-375D | JABORANDI | BAHIA | Brasil | 2917359 | 29 | 33 | nan | nan | nan | Cerrado | 1.2 |
| 0837caac-fdad-3f51-be34-af37569b0578 | -12.11111 | -43.64671 | 2026-05-13 04:55:00 | NPP-375D | MUQUÉM DO SÃO FRANCISCO | BAHIA | Brasil | 2922250 | 29 | 33 | nan | nan | nan | Cerrado | 1.2 |
| 00b183ea-caa4-3814-b406-bebc21b7f30d | -12.85244 | -43.75728 | 2026-05-13 04:55:00 | NPP-375D | SERRA DOURADA | BAHIA | Brasil | 2930303 | 29 | 33 | nan | nan | nan | Cerrado | 1.3 |
| 6d685a87-54cc-358e-a6f3-e690efb355c8 | -11.73951 | -54.24008 | 2026-05-13 04:55:00 | NPP-375D | UNIÃO DO SUL | MATO GROSSO | Brasil | 5108303 | 51 | 33 | nan | nan | nan | Amazônia | 1.4 |
| b092830c-fed0-37e4-8d2b-a04fd20cac5a | -11.63442 | -54.16114 | 2026-05-13 04:55:00 | NPP-375D | UNIÃO DO SUL | MATO GROSSO | Brasil | 5108303 | 51 | 33 | nan | nan | nan | Amazônia | 1.7 |
| c1cec6cd-0ee8-37de-920c-984d4e1e8465 | -11.63503 | -54.15739 | 2026-05-13 04:55:00 | NPP-375D | UNIÃO DO SUL | MATO GROSSO | Brasil | 5108303 | 51 | 33 | nan | nan | nan | Amazônia | 1.7 |
| 9d201ffe-f369-3685-8c09-322c1be94eb9 | -11.74418 | -54.23317 | 2026-05-13 04:55:00 | NPP-375D | UNIÃO DO SUL | MATO GROSSO | Brasil | 5108303 | 51 | 33 | nan | nan | nan | Amazônia | 0.7 |
| a7e5e449-7106-3e65-bd5a-6a99753cee51 | -14.12452 | -45.31678 | 2026-05-13 04:55:00 | NPP-375D | JABORANDI | BAHIA | Brasil | 2917359 | 29 | 33 | nan | nan | nan | Cerrado | 1.0 |
| c0d8bba8-79bc-3bcd-805a-ae454a1dab77 | -14.13602 | -45.42018 | 2026-05-13 04:55:00 | NPP-375D | JABORANDI | BAHIA | Brasil | 2917359 | 29 | 33 | nan | nan | nan | Cerrado | 1.3 |
| 62a32669-bb95-3749-acc3-3e2e6cde4a09 | -10.48459 | -49.35964 | 2026-05-13 04:55:00 | NPP-375D | CRISTALÂNDIA | TOCANTINS | Brasil | 1706100 | 17 | 33 | nan | nan | nan | Cerrado | 1.5 |
| d5c4090e-3d7b-3ba9-914a-4e71ec96b35c | -11.06192 | -52.45291 | 2026-05-13 04:55:00 | NPP-375D | SÃO JOSÉ DO XINGU | MATO GROSSO | Brasil | 5107354 | 51 | 33 | nan | nan | nan | Amazônia | 0.5 |
| fdd2c44a-f3e9-382d-9cb4-063da20eb8b5 | -11.18121 | -55.92478 | 2026-05-13 04:55:00 | NPP-375D | ITAÚBA | MATO GROSSO | Brasil | 5104559 | 51 | 33 | nan | nan | nan | Amazônia | 4.4 |
| e92177b7-8d1b-31f7-bb0e-40bf5d17431d | -14.12037 | -45.31081 | 2026-05-13 04:55:00 | NPP-375D | JABORANDI | BAHIA | Brasil | 2917359 | 29 | 33 | nan | nan | nan | Cerrado | 1.0 |
| 0b2bf5d7-994e-3b1b-adfd-bb05923db082 | -14.13479 | -45.31276 | 2026-05-13 04:55:00 | NPP-375D | JABORANDI | BAHIA | Brasil | 2917359 | 29 | 33 | nan | nan | nan | Cerrado | 1.2 |
| aa5157d3-8583-3678-be72-8aab9b24e8ea | -14.11972 | -45.31612 | 2026-05-13 04:55:00 | NPP-375D | JABORANDI | BAHIA | Brasil | 2917359 | 29 | 33 | nan | nan | nan | Cerrado | 1.0 |
| 48d374cf-0278-3a29-adb9-43fe0a5b686b | -10.40611 | -46.65878 | 2026-05-13 04:55:00 | NPP-375D | MATEIROS | TOCANTINS | Brasil | 1712702 | 17 | 33 | nan | nan | nan | Cerrado | 3.4 |


[Clique aqui para ver as próximas entradas](README5.md)
