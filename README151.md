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

## Dados Diários - Página 151

| ID | Latitude | Longitude | Data/Hora GMT | Satélite | Município | Estado | País | Município ID | Estado ID | País ID | Dias sem Chuva | Precipitação | Risco de Fogo | Bioma | FRP |
|----|----------|-----------|---------------|----------|-----------|--------|------|--------------|-----------|---------|----------------|--------------|----------------|-------|-----|
| c3c8f63f-1dee-30c2-9c80-e8f41fe4b1a2 | -8.71986 | -68.20191 | 2026-08-28 17:47:00 | NOAA-20 | BOCA DO ACRE | AMAZONAS | Brasil | 1300706 | 13 | 33 | nan | nan | nan | Amazônia | 9.4 |
| 70a68af7-4275-3fd7-810f-84bdac6ab1db | -6.94214 | -59.08391 | 2026-08-28 17:47:00 | NOAA-20 | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 4.9 |
| 41e0dbd2-06a9-386b-adb3-21e3f173b855 | -4.47994 | -55.40404 | 2026-08-28 17:47:00 | NOAA-20 | RURÓPOLIS | PARÁ | Brasil | 1506195 | 15 | 33 | nan | nan | nan | Amazônia | 11.8 |
| b97e7c8b-ca0f-3314-a78b-3eafc560669b | -6.84635 | -59.93978 | 2026-08-28 17:47:00 | NOAA-20 | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 16.5 |
| e646ed3f-d03b-3094-b10e-9196c91bd4bf | -4.3128 | -59.46746 | 2026-08-28 17:47:00 | NOAA-20 | BORBA | AMAZONAS | Brasil | 1300805 | 13 | 33 | nan | nan | nan | Amazônia | 11.0 |
| bb849e80-b9eb-3a88-9528-c6a949357c3b | -4.96187 | -56.26885 | 2026-08-28 17:47:00 | NOAA-20 | TRAIRÃO | PARÁ | Brasil | 1508050 | 15 | 33 | nan | nan | nan | Amazônia | 6.9 |
| ec2b54a1-ac20-3cd2-8f9f-069173cc08ef | -8.27651 | -72.75484 | 2026-08-28 17:47:00 | NOAA-20 | PORTO WALTER | ACRE | Brasil | 1200393 | 12 | 33 | nan | nan | nan | Amazônia | 13.8 |
| 87188530-2173-3904-8f01-90f4e87d7972 | -9.27475 | -71.91164 | 2026-08-28 17:47:00 | NOAA-20 | JORDÃO | ACRE | Brasil | 1200328 | 12 | 33 | nan | nan | nan | Amazônia | 6.6 |
| 35aa8863-f1ab-3caa-9566-78e883f97305 | -7.56654 | -61.19529 | 2026-08-28 17:47:00 | NOAA-20 | NOVO ARIPUANÃ | AMAZONAS | Brasil | 1303304 | 13 | 33 | nan | nan | nan | Amazônia | 8.0 |
| 0b434475-8b1e-313e-bf15-237d37f7e0f0 | -7.59439 | -61.32804 | 2026-08-28 17:47:00 | NOAA-20 | MANICORÉ | AMAZONAS | Brasil | 1302702 | 13 | 33 | nan | nan | nan | Amazônia | 5.1 |
| fc5aa24a-dd45-387f-8e01-44cfd3758518 | -4.14599 | -60.76028 | 2026-08-28 17:47:00 | NOAA-20 | CAREIRO | AMAZONAS | Brasil | 1301100 | 13 | 33 | nan | nan | nan | Amazônia | 35.6 |
| fead66bc-7590-396c-a351-309fb275a9f6 | -6.57706 | -55.44343 | 2026-08-28 17:47:00 | NOAA-20 | NOVO PROGRESSO | PARÁ | Brasil | 1505031 | 15 | 33 | nan | nan | nan | Amazônia | 18.4 |
| 2b0bb39a-c1b8-3ce6-b410-91638a69b1f1 | -6.68969 | -59.44456 | 2026-08-28 17:47:00 | NOAA-20 | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 10.4 |
| f31f2e73-3f69-3157-8b6c-5f17cb9345ea | -3.09554 | -57.22144 | 2026-08-28 17:47:00 | NOAA-20 | BARREIRINHA | AMAZONAS | Brasil | 1300508 | 13 | 33 | nan | nan | nan | Amazônia | 4.8 |
| 235ccfd2-b0e8-3361-96d0-a4bd8c21f4b1 | -8.87566 | -66.90285 | 2026-08-28 17:47:00 | NOAA-20 | LÁBREA | AMAZONAS | Brasil | 1302405 | 13 | 33 | nan | nan | nan | Amazônia | 7.3 |
| 2ad0356d-c49c-31cf-b2f3-5e6c2ea29322 | -5.80286 | -57.63864 | 2026-08-28 17:47:00 | NOAA-20 | JACAREACANGA | PARÁ | Brasil | 1503754 | 15 | 33 | nan | nan | nan | Amazônia | 17.2 |
| 7c66ad27-9030-30e3-97bc-1bbe7ff84942 | -7.51742 | -61.3748 | 2026-08-28 17:47:00 | NOAA-20 | MANICORÉ | AMAZONAS | Brasil | 1302702 | 13 | 33 | nan | nan | nan | Amazônia | 4.6 |
| c8d32a84-f3f2-356d-8541-561828df31de | -7.92663 | -72.28743 | 2026-08-28 17:47:00 | NOAA-20 | CRUZEIRO DO SUL | ACRE | Brasil | 1200203 | 12 | 33 | nan | nan | nan | Amazônia | 19.5 |
| 61ad03e9-65d5-37d9-93cd-cb43495e4eef | -6.94676 | -58.95316 | 2026-08-28 17:47:00 | NOAA-20 | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 23.1 |
| 6cd2e66f-179b-359d-94f4-b6afe46eaf82 | -6.54971 | -55.2439 | 2026-08-28 17:47:00 | NOAA-20 | ITAITUBA | PARÁ | Brasil | 1503606 | 15 | 33 | nan | nan | nan | Amazônia | 37.8 |
| 9913d066-d58a-331c-a2a3-191d62048933 | -7.94033 | -71.62814 | 2026-08-28 17:47:00 | NOAA-20 | TARAUACÁ | ACRE | Brasil | 1200609 | 12 | 33 | nan | nan | nan | Amazônia | 2.6 |
| c680d962-6c28-3344-9717-9273080e5738 | -6.95703 | -59.48888 | 2026-08-28 17:47:00 | NOAA-20 | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 30.6 |
| 5051aa14-8a82-3726-8dd5-f3aa6d21595d | -6.83973 | -59.94519 | 2026-08-28 17:47:00 | NOAA-20 | NOVO ARIPUANÃ | AMAZONAS | Brasil | 1303304 | 13 | 33 | nan | nan | nan | Amazônia | 27.7 |
| 3e6d6b41-ca2d-3656-a897-1c34f643353d | -8.78931 | -72.77225 | 2026-08-28 17:47:00 | NOAA-20 | MARECHAL THAUMATURGO | ACRE | Brasil | 1200351 | 12 | 33 | nan | nan | nan | Amazônia | 8.3 |
| 08ac4152-eb3e-3f2b-aedf-8a9b1afc02a5 | -7.7194 | -71.41817 | 2026-08-28 17:47:00 | NOAA-20 | TARAUACÁ | ACRE | Brasil | 1200609 | 12 | 33 | nan | nan | nan | Amazônia | 5.6 |
| cc27e3b0-bed5-356f-8b55-a15a5d82e689 | -7.60011 | -61.34228 | 2026-08-28 17:47:00 | NOAA-20 | MANICORÉ | AMAZONAS | Brasil | 1302702 | 13 | 33 | nan | nan | nan | Amazônia | 50.6 |
| f8afdcbd-e894-3c47-a0eb-ebe012b3a1ca | -9.1885 | -72.94262 | 2026-08-28 17:47:00 | NOAA-20 | MARECHAL THAUMATURGO | ACRE | Brasil | 1200351 | 12 | 33 | nan | nan | nan | Amazônia | 7.2 |
| 19cd5e89-15e3-30d5-8913-b908876f215d | -7.62056 | -61.3391 | 2026-08-28 17:47:00 | NOAA-20 | MANICORÉ | AMAZONAS | Brasil | 1302702 | 13 | 33 | nan | nan | nan | Amazônia | 2.4 |
| b58c77a6-126a-3caf-91ad-7fd0b48e9abf | -6.76755 | -59.47001 | 2026-08-28 17:47:00 | NOAA-20 | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 6.2 |
| 3934f27b-9168-3398-9ff6-c589680edd16 | -8.02654 | -69.88475 | 2026-08-28 17:47:00 | NOAA-20 | FEIJÓ | ACRE | Brasil | 1200302 | 12 | 33 | nan | nan | nan | Amazônia | 19.6 |
| 8b5e4217-7e81-3dc1-b7f4-6e9d2129f084 | -7.00562 | -59.57718 | 2026-08-28 17:47:00 | NOAA-20 | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 7.1 |
| 6f46046f-083d-3ade-b6de-3ac9dc710de4 | -8.39546 | -70.78625 | 2026-08-28 17:47:00 | NOAA-20 | TARAUACÁ | ACRE | Brasil | 1200609 | 12 | 33 | nan | nan | nan | Amazônia | 2.7 |
| 3f0b6c81-6384-3e7a-a7aa-003661be9490 | -8.63535 | -66.5377 | 2026-08-28 17:47:00 | NOAA-20 | LÁBREA | AMAZONAS | Brasil | 1302405 | 13 | 33 | nan | nan | nan | Amazônia | 13.3 |
| 47438d5c-6bad-3a9b-935c-f67e22c13537 | -8.8254 | -66.7131 | 2026-08-28 17:47:00 | NOAA-20 | LÁBREA | AMAZONAS | Brasil | 1302405 | 13 | 33 | nan | nan | nan | Amazônia | 8.1 |
| 303213d3-16f0-340b-ac0c-4b5fd3a0494d | -6.96899 | -59.30032 | 2026-08-28 17:47:00 | NOAA-20 | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 7.0 |
| bacce36a-6a1a-3cbc-bc34-584a4a43856a | -8.86552 | -71.25961 | 2026-08-28 17:47:00 | NOAA-20 | FEIJÓ | ACRE | Brasil | 1200302 | 12 | 33 | nan | nan | nan | Amazônia | 3.2 |
| 27630050-a988-363e-87cd-ced5b8c3e5d6 | -6.83818 | -59.74607 | 2026-08-28 17:47:00 | NOAA-20 | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 18.2 |
| e11c78b1-69c0-3653-9cd7-a68e82ad3759 | -8.83482 | -62.32022 | 2026-08-28 17:47:00 | NOAA-20 | CUJUBIM | RONDÔNIA | Brasil | 1100940 | 11 | 33 | nan | nan | nan | Amazônia | 8.5 |
| 0bb30d68-b534-34a4-a888-4962e5b9fa9a | -9.11352 | -72.237 | 2026-08-28 17:47:00 | NOAA-20 | MARECHAL THAUMATURGO | ACRE | Brasil | 1200351 | 12 | 33 | nan | nan | nan | Amazônia | 2.4 |
| 04c2026e-2634-3bae-aad8-10f8c8fe004e | -8.56353 | -64.17873 | 2026-08-28 17:47:00 | NOAA-20 | CANUTAMA | AMAZONAS | Brasil | 1300904 | 13 | 33 | nan | nan | nan | Amazônia | 4.8 |
| bac4b4e1-bdd2-3b0e-ab57-71bde7c2dd2a | -2.51762 | -60.03229 | 2026-08-28 17:47:00 | NOAA-20 | RIO PRETO DA EVA | AMAZONAS | Brasil | 1303569 | 13 | 33 | nan | nan | nan | Amazônia | 5.7 |
| 929f96e3-6d94-31e6-8ddb-1839b0776ffa | -7.73928 | -61.0911 | 2026-08-28 17:47:00 | NOAA-20 | NOVO ARIPUANÃ | AMAZONAS | Brasil | 1303304 | 13 | 33 | nan | nan | nan | Amazônia | 6.0 |
| ecdb9af1-02eb-3838-868d-bd76ac20233a | -9.01675 | -70.7152 | 2026-08-28 17:47:00 | NOAA-20 | FEIJÓ | ACRE | Brasil | 1200302 | 12 | 33 | nan | nan | nan | Amazônia | 28.4 |
| 184b3226-9f0d-32aa-b49a-28f3ca38c3c6 | -6.75745 | -58.73337 | 2026-08-28 17:47:00 | NOAA-20 | MAUÉS | AMAZONAS | Brasil | 1302900 | 13 | 33 | nan | nan | nan | Amazônia | 19.5 |
| f42f59cc-6823-3199-88c3-0b259e241b62 | -3.26575 | -60.9675 | 2026-08-28 17:47:00 | NOAA-20 | MANACAPURU | AMAZONAS | Brasil | 1302504 | 13 | 33 | nan | nan | nan | Amazônia | 1.5 |
| a6d35ca5-d494-37eb-a6ac-e46f75b423f4 | -6.94519 | -58.94363 | 2026-08-28 17:47:00 | NOAA-20 | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 4.7 |
| 23fe23ba-a989-3926-a485-124893b38fa2 | -6.73541 | -59.64951 | 2026-08-28 17:47:00 | NOAA-20 | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 23.0 |
| 6b81f8fb-03ee-3932-a0f7-bb8ed22fe026 | -6.95141 | -58.95733 | 2026-08-28 17:47:00 | NOAA-20 | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 11.1 |
| 64dff704-7aa6-37bb-8773-f45820684afc | -8.4536 | -70.41662 | 2026-08-28 17:47:00 | NOAA-20 | FEIJÓ | ACRE | Brasil | 1200302 | 12 | 33 | nan | nan | nan | Amazônia | 34.6 |
| c111033e-d3ba-393d-8223-a7da88530d86 | -7.83539 | -72.05317 | 2026-08-28 17:47:00 | NOAA-20 | CRUZEIRO DO SUL | ACRE | Brasil | 1200203 | 12 | 33 | nan | nan | nan | Amazônia | 18.4 |
| 0dc1181a-d5ba-32a6-ad13-05bb05b6ecc2 | -6.66805 | -52.88057 | 2026-08-28 17:47:00 | NOAA-20 | SÃO FÉLIX DO XINGU | PARÁ | Brasil | 1507300 | 15 | 33 | nan | nan | nan | Amazônia | 3.8 |
| 87793993-53f5-3297-bfbc-16b49e3b0c21 | -8.24433 | -73.31699 | 2026-08-28 17:47:00 | NOAA-20 | CRUZEIRO DO SUL | ACRE | Brasil | 1200203 | 12 | 33 | nan | nan | nan | Amazônia | 6.4 |
| 890244f3-0f7e-3435-a66e-e989c17bf288 | -7.88383 | -71.73425 | 2026-08-28 17:47:00 | NOAA-20 | TARAUACÁ | ACRE | Brasil | 1200609 | 12 | 33 | nan | nan | nan | Amazônia | 11.9 |
| b8a8c46a-b2db-39b2-82f3-bda6343cbd87 | -7.48799 | -61.40968 | 2026-08-28 17:47:00 | NOAA-20 | MANICORÉ | AMAZONAS | Brasil | 1302702 | 13 | 33 | nan | nan | nan | Amazônia | 8.0 |
| 93a9c14c-dc98-3cdb-8202-6e5e32e33285 | -4.47729 | -59.88329 | 2026-08-28 17:47:00 | NOAA-20 | BORBA | AMAZONAS | Brasil | 1300805 | 13 | 33 | nan | nan | nan | Amazônia | 4.7 |
| c531ac25-f26d-3398-bdb0-339678077345 | -7.10344 | -55.48096 | 2026-08-28 17:47:00 | NOAA-20 | NOVO PROGRESSO | PARÁ | Brasil | 1505031 | 15 | 33 | nan | nan | nan | Amazônia | 16.9 |
| 77d7adbc-6c89-375a-b05f-c6d4536089bc | -3.93642 | -59.32586 | 2026-08-28 17:47:00 | NOAA-20 | BORBA | AMAZONAS | Brasil | 1300805 | 13 | 33 | nan | nan | nan | Amazônia | 25.4 |
| 40ca8e41-0b5e-3b6f-a98b-dfea23e7b01d | -8.14044 | -64.00056 | 2026-08-28 17:47:00 | NOAA-20 | CANUTAMA | AMAZONAS | Brasil | 1300904 | 13 | 33 | nan | nan | nan | Amazônia | 5.6 |
| 174fe4c8-920d-30c6-891a-f9179060db98 | -7.59381 | -61.32435 | 2026-08-28 17:47:00 | NOAA-20 | MANICORÉ | AMAZONAS | Brasil | 1302702 | 13 | 33 | nan | nan | nan | Amazônia | 5.1 |
| 6c43d7f8-4197-3c9a-8162-14766fb97de6 | -7.58241 | -61.31854 | 2026-08-28 17:47:00 | NOAA-20 | MANICORÉ | AMAZONAS | Brasil | 1302702 | 13 | 33 | nan | nan | nan | Amazônia | 5.9 |
| 5138e8d0-fde2-3200-a86f-5f6422eabc09 | -7.5967 | -61.34281 | 2026-08-28 17:47:00 | NOAA-20 | MANICORÉ | AMAZONAS | Brasil | 1302702 | 13 | 33 | nan | nan | nan | Amazônia | 50.6 |
| 0f6b4c40-beba-3ff1-9e79-26daef0a1ff1 | -7.08922 | -64.90057 | 2026-08-28 17:47:00 | NOAA-20 | LÁBREA | AMAZONAS | Brasil | 1302405 | 13 | 33 | nan | nan | nan | Amazônia | 3.4 |
| 9a5007e0-f6ca-3ab5-ba80-7cc2c7d20069 | -6.23254 | -55.47014 | 2026-08-28 17:47:00 | NOAA-20 | ITAITUBA | PARÁ | Brasil | 1503606 | 15 | 33 | nan | nan | nan | Amazônia | 7.7 |
| 5a436539-421f-30a2-8a70-a04fe082388a | -6.32632 | -57.73625 | 2026-08-28 17:47:00 | NOAA-20 | JACAREACANGA | PARÁ | Brasil | 1503754 | 15 | 33 | nan | nan | nan | Amazônia | 9.3 |
| 4e2bbfa7-e1f4-3217-932d-fc19db6ec629 | -6.54612 | -58.59224 | 2026-08-28 17:47:00 | NOAA-20 | MAUÉS | AMAZONAS | Brasil | 1302900 | 13 | 33 | nan | nan | nan | Amazônia | 15.7 |
| fb6ae594-d3de-3296-a8aa-f3a39a767adb | -8.63422 | -66.54545 | 2026-08-28 17:47:00 | NOAA-20 | LÁBREA | AMAZONAS | Brasil | 1302405 | 13 | 33 | nan | nan | nan | Amazônia | 23.1 |
| 3114a873-3373-36e5-8572-8c39a4a937e7 | -5.92281 | -61.39739 | 2026-08-28 17:47:00 | NOAA-20 | MANICORÉ | AMAZONAS | Brasil | 1302702 | 13 | 33 | nan | nan | nan | Amazônia | 3.8 |
| 7f2291f2-0018-3cd0-aa63-0852f4ea7c2f | -8.46593 | -70.80858 | 2026-08-28 17:47:00 | NOAA-20 | TARAUACÁ | ACRE | Brasil | 1200609 | 12 | 33 | nan | nan | nan | Amazônia | 12.8 |
| 9fa59c79-5878-30cf-9055-c04bb3ba27f2 | -3.22056 | -61.23005 | 2026-08-28 17:47:00 | NOAA-20 | MANACAPURU | AMAZONAS | Brasil | 1302504 | 13 | 33 | nan | nan | nan | Amazônia | 12.7 |
| 07a52865-dc92-3ed5-8f72-1265400da0a0 | -9.17838 | -70.84349 | 2026-08-28 17:47:00 | NOAA-20 | FEIJÓ | ACRE | Brasil | 1200302 | 12 | 33 | nan | nan | nan | Amazônia | 22.8 |
| f65a7882-a9af-3247-8379-14091115200d | -2.9859 | -58.40485 | 2026-08-28 17:47:00 | NOAA-20 | SILVES | AMAZONAS | Brasil | 1304005 | 13 | 33 | nan | nan | nan | Amazônia | 5.9 |
| 6fcbbbd0-bb7a-3d01-aff1-c202d81a1864 | -7.28702 | -60.6191 | 2026-08-28 17:47:00 | NOAA-20 | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 2.4 |
| 406962e4-8192-3b06-8c01-81678d9a86f5 | -9.27087 | -71.91196 | 2026-08-28 17:47:00 | NOAA-20 | JORDÃO | ACRE | Brasil | 1200328 | 12 | 33 | nan | nan | nan | Amazônia | 6.2 |
| 0e186b97-a106-3d8f-bcbb-e44f2f4ebac7 | -8.61458 | -70.94655 | 2026-08-28 17:47:00 | NOAA-20 | TARAUACÁ | ACRE | Brasil | 1200609 | 12 | 33 | nan | nan | nan | Amazônia | 8.0 |
| 59b89a34-8185-38f4-a484-5e346f82c91a | -7.62738 | -61.33805 | 2026-08-28 17:47:00 | NOAA-20 | MANICORÉ | AMAZONAS | Brasil | 1302702 | 13 | 33 | nan | nan | nan | Amazônia | 20.9 |
| 94cd6c9a-25fe-3111-b170-6cabf65239eb | -7.4566 | -72.67667 | 2026-08-28 17:47:00 | NOAA-20 | GUAJARÁ | AMAZONAS | Brasil | 1301654 | 13 | 33 | nan | nan | nan | Amazônia | 3.7 |
| 026997c9-d679-3fde-a6ae-5048c36b8b87 | -6.73984 | -59.65335 | 2026-08-28 17:47:00 | NOAA-20 | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 14.0 |
| 4bb9d311-19ea-3bec-b719-02ba1c8cdea6 | -8.25009 | -73.31622 | 2026-08-28 17:47:00 | NOAA-20 | CRUZEIRO DO SUL | ACRE | Brasil | 1200203 | 12 | 33 | nan | nan | nan | Amazônia | 9.5 |
| ecf348e6-c3f9-3f57-9ed4-30874c7a3c6c | -3.23125 | -61.22839 | 2026-08-28 17:47:00 | NOAA-20 | MANACAPURU | AMAZONAS | Brasil | 1302504 | 13 | 33 | nan | nan | nan | Amazônia | 4.0 |
| 51315bc8-5c92-305e-9936-cfee64ebcdea | -5.92627 | -52.34628 | 2026-08-28 17:47:00 | NOAA-20 | SÃO FÉLIX DO XINGU | PARÁ | Brasil | 1507300 | 15 | 33 | nan | nan | nan | Amazônia | 4.2 |
| e187ec90-52d9-3d3f-a846-4313532e07cd | -8.3307 | -70.33701 | 2026-08-28 17:47:00 | NOAA-20 | FEIJÓ | ACRE | Brasil | 1200302 | 12 | 33 | nan | nan | nan | Amazônia | 12.1 |
| 7c1dddee-ff32-374d-ad30-2e7f22c01bdd | -7.5214 | -61.37796 | 2026-08-28 17:47:00 | NOAA-20 | MANICORÉ | AMAZONAS | Brasil | 1302702 | 13 | 33 | nan | nan | nan | Amazônia | 9.0 |
| 94c4bba5-dda5-30e1-bbe9-4fd65cd6f3ee | -6.13197 | -57.87112 | 2026-08-28 17:47:00 | NOAA-20 | JACAREACANGA | PARÁ | Brasil | 1503754 | 15 | 33 | nan | nan | nan | Amazônia | 6.6 |
| c3e515f9-330e-3a4c-a2df-bef8aaee63a9 | -4.30916 | -59.47617 | 2026-08-28 17:47:00 | NOAA-20 | BORBA | AMAZONAS | Brasil | 1300805 | 13 | 33 | nan | nan | nan | Amazônia | 11.8 |
| 69be0aab-18fc-3d30-a339-202f11d428b4 | -6.94983 | -58.94779 | 2026-08-28 17:47:00 | NOAA-20 | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 54.6 |
| af5ce37c-f225-3248-98bd-b753e4394b7a | -7.44689 | -65.42326 | 2026-08-28 17:47:00 | NOAA-20 | LÁBREA | AMAZONAS | Brasil | 1302405 | 13 | 33 | nan | nan | nan | Amazônia | 18.0 |
| 510494ba-b2af-372e-be0d-93f6770423f1 | -8.77569 | -68.98375 | 2026-08-28 17:47:00 | NOAA-20 | MANOEL URBANO | ACRE | Brasil | 1200344 | 12 | 33 | nan | nan | nan | Amazônia | 2.1 |
| 7fbc1f58-09c7-3dc9-8eb5-d1dbcad4ede8 | -4.47485 | -55.40482 | 2026-08-28 17:47:00 | NOAA-20 | RURÓPOLIS | PARÁ | Brasil | 1506195 | 15 | 33 | nan | nan | nan | Amazônia | 11.8 |
| ff066673-44e6-32b4-bb15-3953da4c8e98 | -8.64707 | -66.54047 | 2026-08-28 17:47:00 | NOAA-20 | LÁBREA | AMAZONAS | Brasil | 1302405 | 13 | 33 | nan | nan | nan | Amazônia | 5.4 |
| d83e2161-2f0e-349d-b289-9bf8f4443924 | -8.87682 | -71.26711 | 2026-08-28 17:47:00 | NOAA-20 | FEIJÓ | ACRE | Brasil | 1200302 | 12 | 33 | nan | nan | nan | Amazônia | 19.2 |
| 8f2217a4-2713-3c4f-805b-9cd46ff87b58 | -7.583 | -61.32224 | 2026-08-28 17:47:00 | NOAA-20 | MANICORÉ | AMAZONAS | Brasil | 1302702 | 13 | 33 | nan | nan | nan | Amazônia | 5.9 |
| 563cda59-e8cf-3843-aed1-13f881e495e1 | -9.21223 | -65.79352 | 2026-08-28 17:47:00 | NOAA-20 | LÁBREA | AMAZONAS | Brasil | 1302405 | 13 | 33 | nan | nan | nan | Amazônia | 7.6 |
| 2ef45fcb-3a49-3a27-ac1c-96091dd4c2a4 | -6.00886 | -57.83545 | 2026-08-28 17:47:00 | NOAA-20 | JACAREACANGA | PARÁ | Brasil | 1503754 | 15 | 33 | nan | nan | nan | Amazônia | 6.1 |
| dbded10d-4f3e-32aa-aded-a6e273faadb8 | -6.84042 | -59.74255 | 2026-08-28 17:47:00 | NOAA-20 | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 4.9 |
| 63ca2055-4c1a-377a-90b9-2aef06dd85cd | -9.42677 | -70.57591 | 2026-08-28 17:47:00 | NOAA-20 | SANTA ROSA DO PURUS | ACRE | Brasil | 1200435 | 12 | 33 | nan | nan | nan | Amazônia | 55.4 |
| 939ed556-d4a5-3e76-9497-8e3834172758 | -8.56635 | -64.17464 | 2026-08-28 17:47:00 | NOAA-20 | CANUTAMA | AMAZONAS | Brasil | 1300904 | 13 | 33 | nan | nan | nan | Amazônia | 18.5 |
| af327867-46eb-39e9-99cc-8479c35e6b2a | -9.50688 | -70.52341 | 2026-08-28 17:47:00 | NOAA-20 | SANTA ROSA DO PURUS | ACRE | Brasil | 1200435 | 12 | 33 | nan | nan | nan | Amazônia | 14.2 |
| 61e916a9-35e3-387c-9c7b-b8c232d0ba81 | -4.3105 | -59.47776 | 2026-08-28 17:47:00 | NOAA-20 | BORBA | AMAZONAS | Brasil | 1300805 | 13 | 33 | nan | nan | nan | Amazônia | 12.0 |
| 7913750c-0081-38ef-86cb-ffe59f5373be | -6.17098 | -53.48184 | 2026-08-28 17:47:00 | NOAA-20 | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 24.0 |
| def3ca01-b69d-394d-812e-91e618351912 | -5.85153 | -57.74953 | 2026-08-28 17:47:00 | NOAA-20 | JACAREACANGA | PARÁ | Brasil | 1503754 | 15 | 33 | nan | nan | nan | Amazônia | 8.4 |


[Clique aqui para ver as próximas entradas](README152.md)
