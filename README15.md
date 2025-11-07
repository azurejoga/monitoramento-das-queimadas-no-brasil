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

## Dados Diários - Página 15

| ID | Latitude | Longitude | Data/Hora GMT | Satélite | Município | Estado | País | Município ID | Estado ID | País ID | Dias sem Chuva | Precipitação | Risco de Fogo | Bioma | FRP |
|----|----------|-----------|---------------|----------|-----------|--------|------|--------------|-----------|---------|----------------|--------------|----------------|-------|-----|
| 454b8e35-94f1-3b3d-8f9c-36db50e73c91 | -4.49119 | -55.79931 | 2025-11-07 04:55:00 | NPP-375D | ITAITUBA | PARÁ | Brasil | 1503606 | 15 | 33 | nan | nan | nan | Amazônia | 0.9 |
| 8881ecfd-754b-33e9-bdbc-b127b85bc04e | -9.44935 | -59.21104 | 2025-11-07 04:55:00 | NPP-375D | COLNIZA | MATO GROSSO | Brasil | 5103254 | 51 | 33 | nan | nan | nan | Amazônia | 2.4 |
| f3e63810-b2ba-345c-9cd7-ff2301d1c6e0 | -9.60642 | -67.15694 | 2025-11-07 04:55:00 | NPP-375D | LÁBREA | AMAZONAS | Brasil | 1302405 | 13 | 33 | nan | nan | nan | Amazônia | 1.1 |
| 4852aeba-55f6-3fc9-8f13-5ac8eef25ea2 | -6.11989 | -57.71104 | 2025-11-07 04:55:00 | NPP-375D | JACAREACANGA | PARÁ | Brasil | 1503754 | 15 | 33 | nan | nan | nan | Amazônia | 1.8 |
| 1b4f8e2d-f549-3349-a027-3b6e2235edea | -9.44015 | -59.21353 | 2025-11-07 04:55:00 | NPP-375D | COLNIZA | MATO GROSSO | Brasil | 5103254 | 51 | 33 | nan | nan | nan | Amazônia | 2.5 |
| 42d88d18-c9de-3bb0-b575-c45188337660 | -6.12048 | -57.70749 | 2025-11-07 04:55:00 | NPP-375D | JACAREACANGA | PARÁ | Brasil | 1503754 | 15 | 33 | nan | nan | nan | Amazônia | 1.4 |
| 6da87b86-4f46-3d67-97dd-4dc1a86b0eeb | -9.14726 | -62.40813 | 2025-11-07 04:55:00 | NPP-375D | CUJUBIM | RONDÔNIA | Brasil | 1100940 | 11 | 33 | nan | nan | nan | Amazônia | 0.6 |
| 891bb0a8-afae-3363-bb74-c61e1c511b65 | -9.0034 | -51.10398 | 2025-11-07 04:55:00 | NPP-375D | CUMARU DO NORTE | PARÁ | Brasil | 1502764 | 15 | 33 | nan | nan | nan | Amazônia | 3.8 |
| be41ec3b-f7bb-387c-a55a-94d230ca8dc8 | -6.12455 | -57.70816 | 2025-11-07 04:55:00 | NPP-375D | JACAREACANGA | PARÁ | Brasil | 1503754 | 15 | 33 | nan | nan | nan | Amazônia | 0.8 |
| 5a40aee3-ea8d-358d-b0da-ccc6bb8e36b9 | -13.26987 | -46.03626 | 2025-11-07 04:55:00 | NPP-375D | SÃO DESIDÉRIO | BAHIA | Brasil | 2928901 | 29 | 33 | nan | nan | nan | Cerrado | 2.8 |
| a21c00ef-dad9-3584-9af5-c1a6402dedbb | 0.61971 | -51.56108 | 2025-11-07 04:55:00 | NPP-375D | PORTO GRANDE | AMAPÁ | Brasil | 1600535 | 16 | 33 | nan | nan | nan | Amazônia | 2.4 |
| 418ca435-def2-3f1a-a133-013cc8765450 | -9.60776 | -67.15016 | 2025-11-07 04:55:00 | NPP-375D | LÁBREA | AMAZONAS | Brasil | 1302405 | 13 | 33 | nan | nan | nan | Amazônia | 1.1 |
| eeff2c6e-a0ab-329c-840b-24b15b0822a8 | -13.28757 | -46.05629 | 2025-11-07 04:55:00 | NPP-375D | SÃO DOMINGOS | GOIÁS | Brasil | 5219803 | 52 | 33 | nan | nan | nan | Cerrado | 4.4 |
| 5815d629-f3c3-32b0-9582-fba4cafe10bf | -6.62382 | -55.01853 | 2025-11-07 04:55:00 | NPP-375D | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 0.6 |
| 3518fd95-3d03-3745-aca9-c1757ef4992e | -9.04664 | -51.12238 | 2025-11-07 04:55:00 | NPP-375D | CUMARU DO NORTE | PARÁ | Brasil | 1502764 | 15 | 33 | nan | nan | nan | Amazônia | 0.9 |
| deb0756c-1175-3a46-946e-c81ffb2b88d4 | -15.09879 | -48.78445 | 2025-11-07 04:57:00 | NPP-375D | VILA PROPÍCIO | GOIÁS | Brasil | 5222302 | 52 | 33 | nan | nan | nan | Cerrado | 1.4 |
| c3239d33-bf12-35de-97a0-ebe6b8f73dd5 | -11.73134 | -59.31046 | 2025-11-07 04:57:00 | NPP-375D | JUÍNA | MATO GROSSO | Brasil | 5105150 | 51 | 33 | nan | nan | nan | Cerrado | 0.6 |
| c6f59141-dd3d-38bf-8400-80565392a98f | -19.03318 | -50.72536 | 2025-11-07 04:57:00 | NPP-375D | CAÇU | GOIÁS | Brasil | 5204300 | 52 | 33 | nan | nan | nan | Mata Atlântica | 2.8 |
| f926bde2-8f58-3115-80f4-737718a9a008 | -18.5002 | -48.77013 | 2025-11-07 04:57:00 | NPP-375D | TUPACIGUARA | MINAS GERAIS | Brasil | 3169604 | 31 | 33 | nan | nan | nan | Mata Atlântica | 0.9 |
| 2ac00401-f767-3378-baf5-202d1fee388b | -15.90815 | -50.39908 | 2025-11-07 04:57:00 | NPP-375D | GOIÁS | GOIÁS | Brasil | 5208905 | 52 | 33 | nan | nan | nan | Cerrado | 1.2 |
| 9f44d6ad-41ec-351b-a528-f7fd6b72e271 | -18.98259 | -50.02887 | 2025-11-07 04:57:00 | NPP-375D | SANTA VITÓRIA | MINAS GERAIS | Brasil | 3159803 | 31 | 33 | nan | nan | nan | Cerrado | 0.7 |
| 66335fbf-bdb9-3e41-8894-dcfbd179124f | -18.2102 | -50.93919 | 2025-11-07 04:57:00 | NPP-375D | RIO VERDE | GOIÁS | Brasil | 5218805 | 52 | 33 | nan | nan | nan | Cerrado | 1.0 |
| ba0775bc-7e97-3942-881c-a532dbd601ac | -13.77161 | -49.34702 | 2025-11-07 04:57:00 | NPP-375D | AMARALINA | GOIÁS | Brasil | 5200829 | 52 | 33 | nan | nan | nan | Cerrado | 0.5 |
| e42452a2-c8b3-3eb5-bd72-9508737d54ad | -17.533 | -45.31623 | 2025-11-07 04:57:00 | NPP-375D | BURITIZEIRO | MINAS GERAIS | Brasil | 3109402 | 31 | 33 | nan | nan | nan | Cerrado | 1.7 |
| 258e9bde-898d-3503-b30f-f88e2f752b58 | -14.02124 | -53.72403 | 2025-11-07 04:57:00 | NPP-375D | PARANATINGA | MATO GROSSO | Brasil | 5106307 | 51 | 33 | nan | nan | nan | Cerrado | 0.6 |
| 692b1e71-2cc5-3703-8678-e668225308d0 | -16.29735 | -45.6089 | 2025-11-07 04:57:00 | NPP-375D | SÃO ROMÃO | MINAS GERAIS | Brasil | 3164209 | 31 | 33 | nan | nan | nan | Cerrado | 1.4 |
| b2ef8949-b7bd-31f7-8ff8-fd0ed4799cfb | -18.33074 | -47.27169 | 2025-11-07 04:57:00 | NPP-375D | COROMANDEL | MINAS GERAIS | Brasil | 3119302 | 31 | 33 | nan | nan | nan | Cerrado | 3.7 |
| b57c6cb2-b8cd-359d-aa33-57c72e7ecfeb | -14.02902 | -53.71796 | 2025-11-07 04:57:00 | NPP-375D | PARANATINGA | MATO GROSSO | Brasil | 5106307 | 51 | 33 | nan | nan | nan | Cerrado | 0.7 |
| 6282523b-fc64-30fe-a58c-e740033488bc | -14.02569 | -53.71741 | 2025-11-07 04:57:00 | NPP-375D | PARANATINGA | MATO GROSSO | Brasil | 5106307 | 51 | 33 | nan | nan | nan | Cerrado | 1.6 |
| b55f6b26-1df1-348b-a8fa-33001c72d151 | -18.97845 | -50.02835 | 2025-11-07 04:57:00 | NPP-375D | SANTA VITÓRIA | MINAS GERAIS | Brasil | 3159803 | 31 | 33 | nan | nan | nan | Cerrado | 1.7 |
| cd988676-a827-31e7-a383-88f2cfb3ea02 | -12.02228 | -63.926 | 2025-11-07 04:57:00 | NPP-375D | SÃO FRANCISCO DO GUAPORÉ | RONDÔNIA | Brasil | 1101492 | 11 | 33 | nan | nan | nan | Amazônia | 1.3 |
| 30923339-9f9e-35ae-b4b6-49cb9ebc995b | -11.72518 | -59.32095 | 2025-11-07 04:57:00 | NPP-375D | JUÍNA | MATO GROSSO | Brasil | 5105150 | 51 | 33 | nan | nan | nan | Cerrado | 0.3 |
| f2889430-3a0c-32ba-bba4-811ddf03730a | -11.73546 | -59.31117 | 2025-11-07 04:57:00 | NPP-375D | JUÍNA | MATO GROSSO | Brasil | 5105150 | 51 | 33 | nan | nan | nan | Cerrado | 0.6 |
| 2fb022be-b447-3fad-b80d-ccfce03a111f | -14.63264 | -52.45527 | 2025-11-07 04:57:00 | NPP-375D | NOVA XAVANTINA | MATO GROSSO | Brasil | 5106257 | 51 | 33 | nan | nan | nan | Cerrado | 1.7 |
| 356f3cd2-e15a-3476-97db-0a25dbd387af | -14.02458 | -53.72458 | 2025-11-07 04:57:00 | NPP-375D | PARANATINGA | MATO GROSSO | Brasil | 5106307 | 51 | 33 | nan | nan | nan | Cerrado | 0.6 |
| b9ef8f4f-5c75-3786-ab00-a0e44103222a | -11.72105 | -59.32021 | 2025-11-07 04:57:00 | NPP-375D | JUÍNA | MATO GROSSO | Brasil | 5105150 | 51 | 33 | nan | nan | nan | Cerrado | 0.3 |
| 9c7519cf-5c79-3767-9493-7758492c3f04 | -14.91001 | -56.77168 | 2025-11-07 04:57:00 | NPP-375D | ALTO PARAGUAI | MATO GROSSO | Brasil | 5100508 | 51 | 33 | nan | nan | nan | Cerrado | 1.2 |
| 7c8ddf7e-c11d-3555-a629-86e435c6fe7b | -18.97432 | -50.02776 | 2025-11-07 04:57:00 | NPP-375D | SANTA VITÓRIA | MINAS GERAIS | Brasil | 3159803 | 31 | 33 | nan | nan | nan | Cerrado | 1.7 |
| 48dbf09f-f0d2-361f-899f-f6060ba9533c | -12.07065 | -56.67757 | 2025-11-07 04:57:00 | NPP-375D | ITANHANGÁ | MATO GROSSO | Brasil | 5104542 | 51 | 33 | nan | nan | nan | Amazônia | 1.3 |
| bf54a690-d78f-3eb1-b8ec-3b62daa1d758 | -15.09657 | -48.77773 | 2025-11-07 04:57:00 | NPP-375D | VILA PROPÍCIO | GOIÁS | Brasil | 5222302 | 52 | 33 | nan | nan | nan | Cerrado | 0.5 |
| d6304bf6-7a29-39af-840d-b8bbbaa862eb | -18.32584 | -47.27097 | 2025-11-07 04:57:00 | NPP-375D | COROMANDEL | MINAS GERAIS | Brasil | 3119302 | 31 | 33 | nan | nan | nan | Cerrado | 1.7 |
| 813c9267-f3c4-3c29-98d5-5c9e5c1eb368 | -11.99495 | -63.94765 | 2025-11-07 04:57:00 | NPP-375D | SÃO FRANCISCO DO GUAPORÉ | RONDÔNIA | Brasil | 1101492 | 11 | 33 | nan | nan | nan | Amazônia | 0.9 |
| 27fa4775-56d5-37bd-820d-c4802063810b | -11.9957 | -63.94384 | 2025-11-07 04:57:00 | NPP-375D | SÃO FRANCISCO DO GUAPORÉ | RONDÔNIA | Brasil | 1101492 | 11 | 33 | nan | nan | nan | Amazônia | 0.9 |
| 2e6c5dfa-b19a-3741-9782-292bee7b8723 | -12.07419 | -56.6782 | 2025-11-07 04:57:00 | NPP-375D | ITANHANGÁ | MATO GROSSO | Brasil | 5104542 | 51 | 33 | nan | nan | nan | Amazônia | 1.3 |
| d035b1d9-d9b7-3b05-a78c-0e0f1b87a323 | -19.03013 | -50.72797 | 2025-11-07 04:57:00 | NPP-375D | CAÇU | GOIÁS | Brasil | 5204300 | 52 | 33 | nan | nan | nan | Mata Atlântica | 3.0 |
| 3d902920-f8b6-3d6d-93f2-efe27980e3c0 | -15.09604 | -48.78163 | 2025-11-07 04:57:00 | NPP-375D | VILA PROPÍCIO | GOIÁS | Brasil | 5222302 | 52 | 33 | nan | nan | nan | Cerrado | 0.9 |
| d957daeb-ee67-361f-941f-341df118fefd | -15.09828 | -48.7884 | 2025-11-07 04:57:00 | NPP-375D | VILA PROPÍCIO | GOIÁS | Brasil | 5222302 | 52 | 33 | nan | nan | nan | Cerrado | 0.6 |
| 13a6a0d4-a224-33cf-aaf1-2d0ebd487f58 | -15.09777 | -48.79241 | 2025-11-07 04:57:00 | NPP-375D | VILA PROPÍCIO | GOIÁS | Brasil | 5222302 | 52 | 33 | nan | nan | nan | Cerrado | 0.6 |
| 80d53121-cd17-3d0a-9af2-21bba0f15d71 | -18.20611 | -56.74273 | 2025-11-07 04:57:00 | NPP-375D | CORUMBÁ | MATO GROSSO DO SUL | Brasil | 5003207 | 50 | 33 | nan | nan | nan | Pantanal | 1.3 |
| 39da4134-37d5-3ed5-87b0-9741e0ea4745 | -12.01672 | -63.92491 | 2025-11-07 04:57:00 | NPP-375D | SÃO FRANCISCO DO GUAPORÉ | RONDÔNIA | Brasil | 1101492 | 11 | 33 | nan | nan | nan | Amazônia | 1.3 |
| 7aa2dd7d-8b85-3a7a-b092-71fd1e0cc7a7 | -22.10697 | -47.12613 | 2025-11-07 04:59:00 | NPP-375D | MOGI GUAÇU | SÃO PAULO | Brasil | 3530706 | 35 | 33 | nan | nan | nan | Cerrado | 1.4 |
| fe38f846-614d-3f10-87c8-f605266dfc8d | -21.29765 | -56.06223 | 2025-11-07 04:59:00 | NPP-375D | NIOAQUE | MATO GROSSO DO SUL | Brasil | 5005806 | 50 | 33 | nan | nan | nan | Cerrado | 0.3 |
| 89971158-689e-3092-b951-3c6ab0378f2d | -21.91781 | -57.66794 | 2025-11-07 04:59:00 | NPP-375D | PORTO MURTINHO | MATO GROSSO DO SUL | Brasil | 5006903 | 50 | 33 | nan | nan | nan | Cerrado | 1.0 |
| 1dd274a1-174f-3aeb-9ede-f7bcf2fcd5bd | -22.1071 | -47.12555 | 2025-11-07 04:59:00 | NPP-375D | MOGI GUAÇU | SÃO PAULO | Brasil | 3530706 | 35 | 33 | nan | nan | nan | Cerrado | 1.4 |
| 91151dfb-c8b9-3064-88c9-3e1717ac5037 | -23.60333 | -49.01103 | 2025-11-07 04:59:00 | NPP-375D | ITAÍ | SÃO PAULO | Brasil | 3521804 | 35 | 33 | nan | nan | nan | Cerrado | 1.4 |
| 49c4def0-cdef-38b1-834f-b44e7f353dde | -20.87059 | -56.39078 | 2025-11-07 04:59:00 | NPP-375D | BONITO | MATO GROSSO DO SUL | Brasil | 5002209 | 50 | 33 | nan | nan | nan | Cerrado | 0.6 |
| 67f26f22-af62-3e08-bd23-5927fc90f498 | -21.1277 | -56.89602 | 2025-11-07 04:59:00 | NPP-375D | PORTO MURTINHO | MATO GROSSO DO SUL | Brasil | 5006903 | 50 | 33 | nan | nan | nan | Cerrado | 0.9 |
| c372fe02-d171-3100-ba60-3993133384bf | -5.0868 | -44.7887 | 2025-11-07 05:00:00 | GOES-19 | JOSELÂNDIA | MARANHÃO | Brasil | 2105609 | 21 | 33 | nan | nan | nan | Cerrado | 49.9 |
| dfeca07e-3631-39b0-aebe-ca8a6275146a | -9.4349 | -59.2154 | 2025-11-07 05:00:00 | GOES-19 | COLNIZA | MATO GROSSO | Brasil | 5103254 | 51 | 33 | nan | nan | nan | Amazônia | 56.1 |
| 69a5a852-2b23-3801-834d-0cdb79e478e3 | -9.4535 | -59.2143 | 2025-11-07 05:00:00 | GOES-19 | COLNIZA | MATO GROSSO | Brasil | 5103254 | 51 | 33 | nan | nan | nan | Amazônia | 60.7 |
| a7bbb74d-443a-3e8a-8cec-6a4afa047fc9 | -9.4537 | -59.1949 | 2025-11-07 05:00:00 | GOES-19 | COLNIZA | MATO GROSSO | Brasil | 5103254 | 51 | 33 | nan | nan | nan | Amazônia | 52.7 |
| fab4709f-8480-3f35-9200-0175662cc365 | -3.3525 | -53.2315 | 2025-11-07 05:00:00 | GOES-19 | MEDICILÂNDIA | PARÁ | Brasil | 1504455 | 15 | 33 | nan | nan | nan | Amazônia | 39.7 |
| 347576e5-6194-3fbe-a705-783fd13c26bb | -3.3525 | -53.2315 | 2025-11-07 05:10:00 | GOES-19 | MEDICILÂNDIA | PARÁ | Brasil | 1504455 | 15 | 33 | nan | nan | nan | Amazônia | 38.5 |
| 32059480-388f-3ceb-aa42-6b886ab34286 | -9.4349 | -59.2154 | 2025-11-07 05:10:00 | GOES-19 | COLNIZA | MATO GROSSO | Brasil | 5103254 | 51 | 33 | nan | nan | nan | Amazônia | 73.0 |
| 07962a86-42e9-3676-adbd-219fcc0d7651 | -9.4535 | -59.2143 | 2025-11-07 05:10:00 | GOES-19 | COLNIZA | MATO GROSSO | Brasil | 5103254 | 51 | 33 | nan | nan | nan | Amazônia | 63.2 |
| 4b339f3c-ee6e-380a-89d3-4e00364e61d5 | -9.435 | -59.1959 | 2025-11-07 05:10:00 | GOES-19 | COLNIZA | MATO GROSSO | Brasil | 5103254 | 51 | 33 | nan | nan | nan | Amazônia | 60.4 |
| 80a0d4c1-a515-36fe-af5c-12cc8b9c60b6 | 1.36952 | -50.71978 | 2025-11-07 05:14:00 | NOAA-20 | TARTARUGALZINHO | AMAPÁ | Brasil | 1600709 | 16 | 33 | nan | nan | nan | Amazônia | 0.9 |
| 452c175d-5a32-3c4d-9c00-a16a62516b03 | 1.35698 | -50.71997 | 2025-11-07 05:14:00 | NOAA-20 | TARTARUGALZINHO | AMAPÁ | Brasil | 1600709 | 16 | 33 | nan | nan | nan | Amazônia | 1.9 |
| 36a1c10e-e1c5-32ae-a49b-f0bdf23a8330 | -1.6908 | -52.12297 | 2025-11-07 05:14:00 | NOAA-20 | PORTO DE MOZ | PARÁ | Brasil | 1505908 | 15 | 33 | nan | nan | nan | Amazônia | 0.7 |
| 19d698a4-1639-3266-8d4e-aca90e102a6c | 2.55522 | -50.99395 | 2025-11-07 05:14:00 | NOAA-20 | CALÇOENE | AMAPÁ | Brasil | 1600204 | 16 | 33 | nan | nan | nan | Amazônia | 1.3 |
| bcdc8aa7-e25f-3ae7-8516-9c23c601bec8 | 2.56803 | -50.99188 | 2025-11-07 05:14:00 | NOAA-20 | CALÇOENE | AMAPÁ | Brasil | 1600204 | 16 | 33 | nan | nan | nan | Amazônia | 1.7 |
| 6e4c6504-7878-34ef-8104-921a41c5b9e9 | 2.56932 | -50.99993 | 2025-11-07 05:14:00 | NOAA-20 | CALÇOENE | AMAPÁ | Brasil | 1600204 | 16 | 33 | nan | nan | nan | Amazônia | 0.5 |
| a1325568-150d-3849-9d3d-bd02311b94e6 | 1.35254 | -50.72068 | 2025-11-07 05:14:00 | NOAA-20 | TARTARUGALZINHO | AMAPÁ | Brasil | 1600709 | 16 | 33 | nan | nan | nan | Amazônia | 1.9 |
| eeb5b2b1-16aa-3bc2-9278-1a15425f1bb8 | 2.56867 | -50.99589 | 2025-11-07 05:14:00 | NOAA-20 | CALÇOENE | AMAPÁ | Brasil | 1600204 | 16 | 33 | nan | nan | nan | Amazônia | 0.5 |
| 9ce2eacb-d45c-3f06-a774-5c21fd58b24e | 0.61962 | -51.56387 | 2025-11-07 05:14:00 | NOAA-20 | PORTO GRANDE | AMAPÁ | Brasil | 1600535 | 16 | 33 | nan | nan | nan | Amazônia | 2.7 |
| 01a77c3e-5d6c-3aa9-92e5-66c755a26ee0 | 2.55754 | -50.98121 | 2025-11-07 05:14:00 | NOAA-20 | CALÇOENE | AMAPÁ | Brasil | 1600204 | 16 | 33 | nan | nan | nan | Amazônia | 2.0 |
| ac82eff8-f18f-3520-9ca5-ae8198cdf241 | 1.7125 | -61.12133 | 2025-11-07 05:14:00 | NOAA-20 | CARACARAÍ | RORAIMA | Brasil | 1400209 | 14 | 33 | nan | nan | nan | Amazônia | 0.8 |
| 94f2807f-ac85-31b8-afea-46b624ff72c6 | -1.14575 | -48.09694 | 2025-11-07 05:14:00 | NOAA-20 | SANTO ANTÔNIO DO TAUÁ | PARÁ | Brasil | 1507003 | 15 | 33 | nan | nan | nan | Amazônia | 0.4 |
| fee64cf4-f9ed-3e7d-8099-9b3eee5ac967 | 2.56608 | -50.97982 | 2025-11-07 05:14:00 | NOAA-20 | CALÇOENE | AMAPÁ | Brasil | 1600204 | 16 | 33 | nan | nan | nan | Amazônia | 2.0 |
| 65a7f180-6234-3f49-bbe9-74e5cc748032 | 0.76322 | -60.09487 | 2025-11-07 05:14:00 | NOAA-20 | SÃO LUIZ | RORAIMA | Brasil | 1400605 | 14 | 33 | nan | nan | nan | Amazônia | 0.7 |
| ee45787a-146a-329c-ad51-e93c56ad8f75 | 0.61538 | -51.56446 | 2025-11-07 05:14:00 | NOAA-20 | PORTO GRANDE | AMAPÁ | Brasil | 1600535 | 16 | 33 | nan | nan | nan | Amazônia | 0.9 |
| 35a0c365-2ee0-3bab-9ce8-0b54951d0ea8 | -1.14022 | -48.09612 | 2025-11-07 05:14:00 | NOAA-20 | SANTO ANTÔNIO DO TAUÁ | PARÁ | Brasil | 1507003 | 15 | 33 | nan | nan | nan | Amazônia | 0.4 |
| 066a205c-d45b-3fd3-ab87-8fecb465c088 | 0.98876 | -51.29762 | 2025-11-07 05:14:00 | NOAA-20 | TARTARUGALZINHO | AMAPÁ | Brasil | 1600709 | 16 | 33 | nan | nan | nan | Amazônia | 1.2 |
| 3b8b0297-3805-34ab-af8a-27395f536217 | 2.53192 | -51.03878 | 2025-11-07 05:14:00 | NOAA-20 | CALÇOENE | AMAPÁ | Brasil | 1600204 | 16 | 33 | nan | nan | nan | Amazônia | 1.5 |
| ca81edb7-74ac-334e-a129-6529827e5b11 | -2.2563 | -47.87808 | 2025-11-07 05:14:00 | NOAA-20 | AURORA DO PARÁ | PARÁ | Brasil | 1500958 | 15 | 33 | nan | nan | nan | Amazônia | 2.3 |
| 7b8e5ced-09f7-3128-bf45-5a6f054bb0b9 | 2.45751 | -51.00454 | 2025-11-07 05:14:00 | NOAA-20 | CALÇOENE | AMAPÁ | Brasil | 1600204 | 16 | 33 | nan | nan | nan | Amazônia | 1.5 |
| e4913352-9d96-3d52-9855-24a70a673151 | -2.85694 | -49.88324 | 2025-11-07 05:16:00 | NOAA-20 | BAGRE | PARÁ | Brasil | 1501105 | 15 | 33 | nan | nan | nan | Amazônia | 0.8 |
| af6233ae-fd69-3ceb-96ef-40c7bd14aa43 | -3.34904 | -53.22856 | 2025-11-07 05:16:00 | NOAA-20 | MEDICILÂNDIA | PARÁ | Brasil | 1504455 | 15 | 33 | nan | nan | nan | Amazônia | 4.8 |
| 59115a77-d366-3de3-8145-b4ddaeac8fe4 | -3.59677 | -49.44022 | 2025-11-07 05:16:00 | NOAA-20 | BREU BRANCO | PARÁ | Brasil | 1501782 | 15 | 33 | nan | nan | nan | Amazônia | 3.3 |
| 540e4ac8-921c-3ba4-9790-1081eaf0f1a3 | -4.82931 | -48.55484 | 2025-11-07 05:16:00 | NOAA-20 | ABEL FIGUEIREDO | PARÁ | Brasil | 1500131 | 15 | 33 | nan | nan | nan | Amazônia | 1.7 |
| be44bcdf-82de-3e76-ad1d-1a2b6c0ada68 | -3.17092 | -48.61484 | 2025-11-07 05:16:00 | NOAA-20 | TAILÂNDIA | PARÁ | Brasil | 1507953 | 15 | 33 | nan | nan | nan | Amazônia | 2.7 |
| fd42431e-6260-3696-b842-db0c5e0c99bd | -3.33626 | -50.1983 | 2025-11-07 05:16:00 | NOAA-20 | PACAJÁ | PARÁ | Brasil | 1505486 | 15 | 33 | nan | nan | nan | Amazônia | 1.7 |
| d22e4598-9a36-3f5f-89c6-1f7bb2786502 | -3.12368 | -50.14775 | 2025-11-07 05:16:00 | NOAA-20 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 2.1 |
| 4650efc4-b377-31f7-8ea7-71e6452176a1 | -3.11958 | -50.14144 | 2025-11-07 05:16:00 | NOAA-20 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 5.4 |
| ccdc2279-cb6d-3334-bf1e-5d867a019472 | -4.44684 | -46.44031 | 2025-11-07 05:16:00 | NOAA-20 | BURITICUPU | MARANHÃO | Brasil | 2102325 | 21 | 33 | nan | nan | nan | Amazônia | 2.6 |
| 8ad477b0-4247-371f-a554-9c852db89c2f | -3.78536 | -49.43351 | 2025-11-07 05:16:00 | NOAA-20 | BREU BRANCO | PARÁ | Brasil | 1501782 | 15 | 33 | nan | nan | nan | Amazônia | 0.5 |
| 1aade70c-2ba5-3c09-85af-b5e4f92d8626 | -4.67204 | -46.30748 | 2025-11-07 05:16:00 | NOAA-20 | BURITICUPU | MARANHÃO | Brasil | 2102325 | 21 | 33 | nan | nan | nan | Amazônia | 4.9 |
| 84dddfd9-0c02-340d-bace-233e0d872bfe | -4.28552 | -45.8906 | 2025-11-07 05:16:00 | NOAA-20 | SANTA LUZIA | MARANHÃO | Brasil | 2110005 | 21 | 33 | nan | nan | nan | Amazônia | 6.6 |
| a451b1d9-c06d-3eae-bf05-3464a2b8294d | -3.53773 | -49.44071 | 2025-11-07 05:16:00 | NOAA-20 | BREU BRANCO | PARÁ | Brasil | 1501782 | 15 | 33 | nan | nan | nan | Amazônia | 0.4 |
| 2ac7ddfe-d3a2-3b9b-8b2e-5e35051927b6 | -6.11967 | -57.71321 | 2025-11-07 05:16:00 | NOAA-20 | JACAREACANGA | PARÁ | Brasil | 1503754 | 15 | 33 | nan | nan | nan | Amazônia | 0.9 |


[Clique aqui para ver as próximas entradas](README16.md)
