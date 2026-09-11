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

## Dados Diários - Página 43

| ID | Latitude | Longitude | Data/Hora GMT | Satélite | Município | Estado | País | Município ID | Estado ID | País ID | Dias sem Chuva | Precipitação | Risco de Fogo | Bioma | FRP |
|----|----------|-----------|---------------|----------|-----------|--------|------|--------------|-----------|---------|----------------|--------------|----------------|-------|-----|
| 4d1cc2f5-cfe6-369c-8e8e-35181b460544 | -8.6195 | -47.3893 | 2026-09-11 15:10:00 | GOES-19 | ITACAJÁ | TOCANTINS | Brasil | 1710508 | 17 | 33 | nan | nan | nan | Cerrado | 71.3 |
| e7a51f64-3534-39e6-be09-d2ea57792829 | -8.0748 | -54.8499 | 2026-09-11 15:10:00 | GOES-19 | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 62.4 |
| 75f08687-252b-3454-8ca8-cf82716e112c | -5.6314 | -51.6444 | 2026-09-11 15:10:00 | GOES-19 | SÃO FÉLIX DO XINGU | PARÁ | Brasil | 1507300 | 15 | 33 | nan | nan | nan | Amazônia | 147.2 |
| df7e5b3f-e70c-3a6b-94fb-998203f1697a | -11.4021 | -43.9585 | 2026-09-11 15:10:00 | GOES-19 | COTEGIPE | BAHIA | Brasil | 2909406 | 29 | 33 | nan | nan | nan | Cerrado | 135.4 |
| b2c85a5f-4078-3548-8974-fb03c48c1ad2 | -6.4047 | -54.9642 | 2026-09-11 15:10:00 | GOES-19 | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 78.2 |
| b2dc95e6-0b8e-327f-a77a-9bbeb841faf8 | -8.0934 | -54.8488 | 2026-09-11 15:10:00 | GOES-19 | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 93.2 |
| 85e1893f-a57d-377b-8f9a-03ffa206c872 | -6.4045 | -54.9842 | 2026-09-11 15:10:00 | GOES-19 | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 85.9 |
| 2d13a53a-0096-3fc1-9d51-1b0102a5dc5d | -14.8863 | -49.236 | 2026-09-11 15:10:00 | GOES-19 | SÃO LUIZ DO NORTE | GOIÁS | Brasil | 5220157 | 52 | 33 | nan | nan | nan | Cerrado | 95.8 |
| f9654eff-51c0-374b-b5e8-b3fb158d66a8 | -9.9041 | -45.91 | 2026-09-11 15:10:00 | GOES-19 | ALTO PARNAÍBA | MARANHÃO | Brasil | 2100501 | 21 | 33 | nan | nan | nan | Cerrado | 213.0 |
| 8f966207-84ad-3cc2-99d6-7da16919bc01 | -6.6888 | -45.4877 | 2026-09-11 15:10:00 | GOES-19 | MIRADOR | MARANHÃO | Brasil | 2106706 | 21 | 33 | nan | nan | nan | Cerrado | 180.4 |
| 6ec79df8-d26b-3cd0-89b8-176a0e2d8cbf | -6.1994 | -55.254 | 2026-09-11 15:10:00 | GOES-19 | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 118.1 |
| 03c8587b-b048-3c3b-8274-9f4b321ca66f | -8.6496 | -66.5096 | 2026-09-11 15:10:00 | GOES-19 | LÁBREA | AMAZONAS | Brasil | 1302405 | 13 | 33 | nan | nan | nan | Amazônia | 85.0 |
| 9561f45d-ea99-3291-8be5-63c3bd173f37 | -9.1888 | -65.9542 | 2026-09-11 15:10:00 | GOES-19 | LÁBREA | AMAZONAS | Brasil | 1302405 | 13 | 33 | nan | nan | nan | Amazônia | 46.2 |
| abaaf3b2-8098-31d3-b104-da7ebff9175d | -11.3513 | -45.7922 | 2026-09-11 15:10:00 | GOES-19 | FORMOSA DO RIO PRETO | BAHIA | Brasil | 2911105 | 29 | 33 | nan | nan | nan | Cerrado | 148.8 |
| 1afc5930-e0fd-3ad4-90fa-acdfc5d34ca3 | -5.8021 | -53.8061 | 2026-09-11 15:10:00 | GOES-19 | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 50.9 |
| bbfdadae-6a88-3133-9274-4664d1b6404f | -12.169 | -64.1404 | 2026-09-11 15:10:00 | GOES-19 | COSTA MARQUES | RONDÔNIA | Brasil | 1100080 | 11 | 33 | nan | nan | nan | Amazônia | 47.8 |
| dce82259-c427-3597-ac3e-2b80e3b97476 | -8.9874 | -65.4192 | 2026-09-11 15:10:00 | GOES-19 | LÁBREA | AMAZONAS | Brasil | 1302405 | 13 | 33 | nan | nan | nan | Amazônia | 49.5 |
| a93fa536-1fd6-35cd-9a3b-b7536c54cf5b | -1.7683 | -54.9513 | 2026-09-11 15:10:00 | GOES-19 | ALENQUER | PARÁ | Brasil | 1500404 | 15 | 33 | nan | nan | nan | Amazônia | 78.4 |
| 1d6b737b-e19f-309b-acde-faf3287709c5 | -6.8281 | -55.2826 | 2026-09-11 15:10:00 | GOES-19 | NOVO PROGRESSO | PARÁ | Brasil | 1505031 | 15 | 33 | nan | nan | nan | Amazônia | 54.4 |
| 4a0a2088-2329-3346-ace9-2c6b6de03f70 | -7.12 | -42.107 | 2026-09-11 15:10:00 | GOES-19 | OEIRAS | PIAUÍ | Brasil | 2207009 | 22 | 33 | nan | nan | nan | Caatinga | 140.0 |
| a3817e2b-0bc6-3c3c-a196-34a848af705e | -9.3852 | -49.3847 | 2026-09-11 15:10:00 | GOES-19 | ABREULÂNDIA | TOCANTINS | Brasil | 1700251 | 17 | 33 | nan | nan | nan | Cerrado | 134.6 |
| 70a28c99-732b-316c-870a-972e2a166d45 | -6.7075 | -45.4861 | 2026-09-11 15:10:00 | GOES-19 | MIRADOR | MARANHÃO | Brasil | 2106706 | 21 | 33 | nan | nan | nan | Cerrado | 146.1 |
| 4924b9d7-560c-3739-b0f7-eea887b3231f | -9.3854 | -49.3631 | 2026-09-11 15:10:00 | GOES-19 | ABREULÂNDIA | TOCANTINS | Brasil | 1700251 | 17 | 33 | nan | nan | nan | Cerrado | 100.4 |
| ebaa5a3c-bdf1-3d73-9324-11d189134c3a | -9.1407 | -64.4024 | 2026-09-11 15:10:00 | GOES-19 | PORTO VELHO | RONDÔNIA | Brasil | 1100205 | 11 | 33 | nan | nan | nan | Amazônia | 52.6 |
| fc511df1-3230-3bbd-9aa2-87bae3d6d32e | -12.1501 | -64.1414 | 2026-09-11 15:10:00 | GOES-19 | COSTA MARQUES | RONDÔNIA | Brasil | 1100080 | 11 | 33 | nan | nan | nan | Amazônia | 69.1 |
| a4269a89-8f80-3229-8ba2-6270ad4327b9 | -11.4026 | -43.935 | 2026-09-11 15:10:00 | GOES-19 | COTEGIPE | BAHIA | Brasil | 2909406 | 29 | 33 | nan | nan | nan | Cerrado | 139.1 |
| cc00a07a-cf6b-3380-8604-c3d9af154734 | -10.4911 | -51.3423 | 2026-09-11 15:10:00 | GOES-19 | CONFRESA | MATO GROSSO | Brasil | 5103353 | 51 | 33 | nan | nan | nan | Amazônia | 98.9 |
| 90891f14-96a5-3eb4-980c-79ba05203eba | -8.0709 | -55.3121 | 2026-09-11 15:10:00 | GOES-19 | NOVO PROGRESSO | PARÁ | Brasil | 1505031 | 15 | 33 | nan | nan | nan | Amazônia | 50.1 |
| 16bde0da-2774-3208-8b4d-44c6809aa664 | -5.3646 | -56.0249 | 2026-09-11 15:10:00 | GOES-19 | TRAIRÃO | PARÁ | Brasil | 1508050 | 15 | 33 | nan | nan | nan | Amazônia | 65.7 |
| d7ef380b-ee8a-35eb-b475-c12b568d5fb2 | -6.1993 | -55.2739 | 2026-09-11 15:10:00 | GOES-19 | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 186.1 |
| 68352ff8-63ea-34a9-9e03-94368bb5f4c5 | -6.5002 | -47.6128 | 2026-09-11 15:10:00 | GOES-19 | PALMEIRAS DO TOCANTINS | TOCANTINS | Brasil | 1713809 | 17 | 33 | nan | nan | nan | Cerrado | 94.7 |
| d7ce5e57-179c-34f5-851b-fa3ddb4c84dd | -6.2429 | -51.6939 | 2026-09-11 15:10:00 | GOES-19 | SÃO FÉLIX DO XINGU | PARÁ | Brasil | 1507300 | 15 | 33 | nan | nan | nan | Amazônia | 114.3 |
| 8b403b15-2cfa-38ad-8c05-7d69d1ca7306 | -11.0434 | -49.6851 | 2026-09-11 15:10:00 | GOES-19 | SANTA RITA DO TOCANTINS | TOCANTINS | Brasil | 1718899 | 17 | 33 | nan | nan | nan | Cerrado | 127.7 |
| ce895d94-6ea5-34ed-8292-aa54c9c2e817 | -11.9547 | -49.7512 | 2026-09-11 15:10:00 | GOES-19 | FORMOSO DO ARAGUAIA | TOCANTINS | Brasil | 1708205 | 17 | 33 | nan | nan | nan | Cerrado | 144.2 |
| caee617f-b1ca-39ce-bd91-c07c0afb3a4a | -8.6311 | -66.5101 | 2026-09-11 15:10:00 | GOES-19 | LÁBREA | AMAZONAS | Brasil | 1302405 | 13 | 33 | nan | nan | nan | Amazônia | 79.4 |
| 7fd04fa4-b1b6-3190-8379-abf2e52c1788 | -10.4722 | -51.3442 | 2026-09-11 15:10:00 | GOES-19 | CONFRESA | MATO GROSSO | Brasil | 5103353 | 51 | 33 | nan | nan | nan | Amazônia | 205.3 |
| 3f98fcd4-6144-3232-9b16-3ac0f833d1e1 | -5.963 | -57.7874 | 2026-09-11 15:10:00 | GOES-19 | JACAREACANGA | PARÁ | Brasil | 1503754 | 15 | 33 | nan | nan | nan | Amazônia | 83.2 |
| 19319005-7f58-3459-9df3-e52687ebd9f6 | -7.5553 | -45.1624 | 2026-09-11 15:10:00 | GOES-19 | RIBEIRO GONÇALVES | PIAUÍ | Brasil | 2208908 | 22 | 33 | nan | nan | nan | Cerrado | 89.8 |
| 4c35e69a-8443-3fda-a387-6dd0d52091ce | -9.0982 | -65.4904 | 2026-09-11 15:10:00 | GOES-19 | LÁBREA | AMAZONAS | Brasil | 1302405 | 13 | 33 | nan | nan | nan | Amazônia | 55.8 |
| 5b9b441e-8ad5-3f78-b691-8dd3baa82527 | -6.7649 | -59.4216 | 2026-09-11 15:10:00 | GOES-19 | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 74.1 |
| f4db9d0d-cf1f-37ec-becf-5d260d464cd2 | -5.6313 | -51.6651 | 2026-09-11 15:10:00 | GOES-19 | SÃO FÉLIX DO XINGU | PARÁ | Brasil | 1507300 | 15 | 33 | nan | nan | nan | Amazônia | 122.3 |
| 4cf43879-ff12-3f00-9183-9fe2234c147b | -8.9428 | -63.2797 | 2026-09-11 15:10:00 | GOES-19 | ITAPUÃ DO OESTE | RONDÔNIA | Brasil | 1101104 | 11 | 33 | nan | nan | nan | Amazônia | 48.8 |
| f6110ce9-354e-39a1-96b2-b34bc7e81fa1 | -10.5478 | -51.3367 | 2026-09-11 15:10:00 | GOES-19 | CONFRESA | MATO GROSSO | Brasil | 5103353 | 51 | 33 | nan | nan | nan | Amazônia | 215.1 |
| 8c1b0c69-9f41-3ce4-bc7b-2f195295389c | -9.9045 | -45.8873 | 2026-09-11 15:10:00 | GOES-19 | ALTO PARNAÍBA | MARANHÃO | Brasil | 2100501 | 21 | 33 | nan | nan | nan | Cerrado | 121.2 |
| fdf0a3b8-8019-32c9-9272-5a37e5dc305f | -10.5475 | -51.3578 | 2026-09-11 15:10:00 | GOES-19 | CONFRESA | MATO GROSSO | Brasil | 5103353 | 51 | 33 | nan | nan | nan | Amazônia | 687.4 |
| 623dcb33-0767-3f4f-8753-9a0ace049c8b | -6.5004 | -47.5909 | 2026-09-11 15:10:00 | GOES-19 | PALMEIRAS DO TOCANTINS | TOCANTINS | Brasil | 1713809 | 17 | 33 | nan | nan | nan | Cerrado | 84.4 |
| c128a21e-733b-3d81-9d9c-baedb9252100 | -4.5229 | -54.9639 | 2026-09-11 15:10:00 | GOES-19 | RURÓPOLIS | PARÁ | Brasil | 1506195 | 15 | 33 | nan | nan | nan | Amazônia | 55.1 |
| 95ae359f-2de0-360e-ba57-13ecabd4a968 | -9.006 | -65.4 | 2026-09-11 15:10:00 | GOES-19 | LÁBREA | AMAZONAS | Brasil | 1302405 | 13 | 33 | nan | nan | nan | Amazônia | 66.6 |
| aaec4046-ef07-3b87-8fa6-aa33a234b2cb | -6.3248 | -55.8649 | 2026-09-11 15:10:00 | GOES-19 | ITAITUBA | PARÁ | Brasil | 1503606 | 15 | 33 | nan | nan | nan | Amazônia | 51.4 |
| 93246ea6-7324-3c4f-819e-76fdc68e6cad | -6.641 | -58.4987 | 2026-09-11 15:10:00 | GOES-19 | MAUÉS | AMAZONAS | Brasil | 1302900 | 13 | 33 | nan | nan | nan | Amazônia | 56.3 |
| 30e0ac23-79a7-35cb-bec3-a4085aefdbdd | -6.2427 | -51.7146 | 2026-09-11 15:10:00 | GOES-19 | SÃO FÉLIX DO XINGU | PARÁ | Brasil | 1507300 | 15 | 33 | nan | nan | nan | Amazônia | 70.3 |
| a2421d7a-eb27-3d2b-a522-c8b2024c65ab | -10.55 | -51.35 | 2026-09-11 15:15:00 | MSG-03 | CONFRESA | MATO GROSSO | Brasil | 5103353 | 51 | 33 | nan | nan | nan | Amazônia | nan |
| fdb13c52-8a6e-3dc8-b803-83af5d5cc463 | -10.52 | -51.34 | 2026-09-11 15:15:00 | MSG-03 | CONFRESA | MATO GROSSO | Brasil | 5103353 | 51 | 33 | nan | nan | nan | Amazônia | nan |
| 009b2f7c-13be-3172-9f72-4d8b23ebf7f6 | -11.383 | -43.9614 | 2026-09-11 15:20:00 | GOES-19 | COTEGIPE | BAHIA | Brasil | 2909406 | 29 | 33 | nan | nan | nan | Cerrado | 126.5 |
| 1fcb2875-63d3-3de7-8036-668ab2a9e8a3 | -6.828 | -55.3026 | 2026-09-11 15:20:00 | GOES-19 | NOVO PROGRESSO | PARÁ | Brasil | 1505031 | 15 | 33 | nan | nan | nan | Amazônia | 48.9 |
| e09d61b4-bc06-39e4-a888-7580bc86ca97 | -7.5553 | -45.1624 | 2026-09-11 15:20:00 | GOES-19 | RIBEIRO GONÇALVES | PIAUÍ | Brasil | 2208908 | 22 | 33 | nan | nan | nan | Cerrado | 90.6 |
| e961d6cb-8e87-38ad-a5cc-6700f40a3386 | -10.2743 | -45.2726 | 2026-09-11 15:20:00 | GOES-19 | CORRENTE | PIAUÍ | Brasil | 2202901 | 22 | 33 | nan | nan | nan | Cerrado | 254.1 |
| 6f7dc042-15d1-3459-999e-715a3935fec4 | -8.9874 | -65.4192 | 2026-09-11 15:20:00 | GOES-19 | LÁBREA | AMAZONAS | Brasil | 1302405 | 13 | 33 | nan | nan | nan | Amazônia | 55.7 |
| 4e86c29f-6086-3328-823d-63db11bd7ca1 | -5.8021 | -53.8061 | 2026-09-11 15:20:00 | GOES-19 | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 54.1 |
| bd328c8d-2d0c-36ec-9d1c-27e9b43798a6 | -6.2429 | -51.6939 | 2026-09-11 15:20:00 | GOES-19 | SÃO FÉLIX DO XINGU | PARÁ | Brasil | 1507300 | 15 | 33 | nan | nan | nan | Amazônia | 91.5 |
| 4628ab08-aa97-353b-b4bc-ec0f86351b71 | -8.9873 | -65.4379 | 2026-09-11 15:20:00 | GOES-19 | LÁBREA | AMAZONAS | Brasil | 1302405 | 13 | 33 | nan | nan | nan | Amazônia | 48.6 |
| 771acbd2-b5ac-3ae3-b183-7d688e441d26 | -5.9814 | -57.7867 | 2026-09-11 15:20:00 | GOES-19 | JACAREACANGA | PARÁ | Brasil | 1503754 | 15 | 33 | nan | nan | nan | Amazônia | 59.1 |
| 72972bb4-c1ad-3748-82a1-adf29590809a | -6.1993 | -55.2739 | 2026-09-11 15:20:00 | GOES-19 | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 283.0 |
| 661fc6c2-c9a9-384b-b04f-5f49c9df6ea1 | -8.9428 | -63.2797 | 2026-09-11 15:20:00 | GOES-19 | ITAPUÃ DO OESTE | RONDÔNIA | Brasil | 1101104 | 11 | 33 | nan | nan | nan | Amazônia | 49.6 |
| f9079e06-5b5b-363b-90f5-67fb091fe7ff | -11.9547 | -49.7512 | 2026-09-11 15:20:00 | GOES-19 | FORMOSO DO ARAGUAIA | TOCANTINS | Brasil | 1708205 | 17 | 33 | nan | nan | nan | Cerrado | 139.4 |
| 53af1798-1380-373b-942a-7acac2e3217b | -12.1501 | -64.1414 | 2026-09-11 15:20:00 | GOES-19 | COSTA MARQUES | RONDÔNIA | Brasil | 1100080 | 11 | 33 | nan | nan | nan | Amazônia | 70.3 |
| abc958d5-c523-3577-91cd-7ed2f4984167 | -6.1808 | -55.2748 | 2026-09-11 15:20:00 | GOES-19 | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 58.3 |
| 94c701ec-91e3-30cd-9cf6-286595f9743b | -6.641 | -58.4987 | 2026-09-11 15:20:00 | GOES-19 | MAUÉS | AMAZONAS | Brasil | 1302900 | 13 | 33 | nan | nan | nan | Amazônia | 58.8 |
| 7cbaa036-a4c0-39c8-82cd-96746911ccbb | -8.6311 | -66.5287 | 2026-09-11 15:20:00 | GOES-19 | LÁBREA | AMAZONAS | Brasil | 1302405 | 13 | 33 | nan | nan | nan | Amazônia | 62.7 |
| 714b48ff-4289-34ed-ad35-5b0095e7ebfa | -6.1994 | -55.254 | 2026-09-11 15:20:00 | GOES-19 | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 178.6 |
| 1782c3a2-1a08-3b52-8352-044d61e598e0 | -6.3248 | -55.8649 | 2026-09-11 15:20:00 | GOES-19 | ITAITUBA | PARÁ | Brasil | 1503606 | 15 | 33 | nan | nan | nan | Amazônia | 71.3 |
| 8aeb2149-7d11-37cc-b42f-6bc0971e5aec | -6.5002 | -47.6128 | 2026-09-11 15:20:00 | GOES-19 | PALMEIRAS DO TOCANTINS | TOCANTINS | Brasil | 1713809 | 17 | 33 | nan | nan | nan | Cerrado | 79.1 |
| 75fe97b6-2124-35c7-a5d7-557588e218ac | -6.7263 | -45.4846 | 2026-09-11 15:20:00 | GOES-19 | MIRADOR | MARANHÃO | Brasil | 2106706 | 21 | 33 | nan | nan | nan | Cerrado | 85.4 |
| 96e2c753-0130-355f-ba00-d5ef53620467 | -13.2848 | -61.8287 | 2026-09-11 15:20:00 | GOES-19 | CEREJEIRAS | RONDÔNIA | Brasil | 1100056 | 11 | 33 | nan | nan | nan | Amazônia | 43.6 |
| 86cd2468-1185-31cc-a5f1-f5480dbaba3b | -5.9815 | -57.7672 | 2026-09-11 15:20:00 | GOES-19 | JACAREACANGA | PARÁ | Brasil | 1503754 | 15 | 33 | nan | nan | nan | Amazônia | 85.0 |
| a57222ee-9faf-398b-a9fd-797656983975 | -9.0981 | -65.5091 | 2026-09-11 15:20:00 | GOES-19 | LÁBREA | AMAZONAS | Brasil | 1302405 | 13 | 33 | nan | nan | nan | Amazônia | 52.4 |
| 6c59e2ed-632d-3356-9f1e-e03702431c26 | -6.8281 | -55.2826 | 2026-09-11 15:20:00 | GOES-19 | NOVO PROGRESSO | PARÁ | Brasil | 1505031 | 15 | 33 | nan | nan | nan | Amazônia | 69.0 |
| e54109ac-b475-36fd-90eb-fe829c50fdff | -11.4026 | -43.935 | 2026-09-11 15:20:00 | GOES-19 | COTEGIPE | BAHIA | Brasil | 2909406 | 29 | 33 | nan | nan | nan | Cerrado | 129.7 |
| efdf1682-4856-3078-8f87-aa9468491993 | -5.963 | -57.7874 | 2026-09-11 15:20:00 | GOES-19 | JACAREACANGA | PARÁ | Brasil | 1503754 | 15 | 33 | nan | nan | nan | Amazônia | 69.9 |
| 35452b22-15ac-315b-97ce-79a99e6533fc | -11.0434 | -49.6851 | 2026-09-11 15:20:00 | GOES-19 | SANTA RITA DO TOCANTINS | TOCANTINS | Brasil | 1718899 | 17 | 33 | nan | nan | nan | Cerrado | 130.8 |
| 3a6eb696-e8c1-3b56-8119-32a279222668 | -10.5478 | -51.3367 | 2026-09-11 15:20:00 | GOES-19 | CONFRESA | MATO GROSSO | Brasil | 5103353 | 51 | 33 | nan | nan | nan | Amazônia | 165.9 |
| 293692a6-bd94-3756-bb94-8e402d86b7df | -6.7648 | -59.4408 | 2026-09-11 15:20:00 | GOES-19 | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 98.9 |
| 389c1629-f2f3-3f9a-9288-fe3944500352 | -6.6888 | -45.4877 | 2026-09-11 15:20:00 | GOES-19 | MIRADOR | MARANHÃO | Brasil | 2106706 | 21 | 33 | nan | nan | nan | Cerrado | 273.0 |
| d827300f-a132-3a8d-b1c2-846fba5646be | -6.0913 | -57.8992 | 2026-09-11 15:20:00 | GOES-19 | JACAREACANGA | PARÁ | Brasil | 1503754 | 15 | 33 | nan | nan | nan | Amazônia | 53.0 |
| e6747bf2-e8a8-3f0f-a4d7-9d564316b260 | -6.4045 | -54.9842 | 2026-09-11 15:20:00 | GOES-19 | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 70.5 |
| 905bc516-deb4-3d15-8cb3-c6f95fe8e239 | -9.9045 | -45.8873 | 2026-09-11 15:20:00 | GOES-19 | ALTO PARNAÍBA | MARANHÃO | Brasil | 2100501 | 21 | 33 | nan | nan | nan | Cerrado | 123.0 |
| 4c6d117b-1cf7-30ea-baaa-a96499a83ba5 | -11.3834 | -43.9378 | 2026-09-11 15:20:00 | GOES-19 | COTEGIPE | BAHIA | Brasil | 2909406 | 29 | 33 | nan | nan | nan | Cerrado | 105.9 |
| a5a31125-2fcc-3df0-a44f-9c593fda6827 | -11.2488 | -54.1378 | 2026-09-11 15:20:00 | GOES-19 | MARCELÂNDIA | MATO GROSSO | Brasil | 5105580 | 51 | 33 | nan | nan | nan | Amazônia | 90.7 |
| 7a6538d8-7738-3d29-9e8f-c7eb8f221508 | -8.0709 | -55.3121 | 2026-09-11 15:20:00 | GOES-19 | NOVO PROGRESSO | PARÁ | Brasil | 1505031 | 15 | 33 | nan | nan | nan | Amazônia | 61.6 |
| 0bbac7dd-babf-3aad-91a4-3b6ba635bb35 | -8.0748 | -54.8499 | 2026-09-11 15:20:00 | GOES-19 | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 81.1 |
| 6096a2ae-4e93-3c9f-abe7-2360d175a1b9 | -9.1523 | -49.9853 | 2026-09-11 15:20:00 | GOES-19 | SANTANA DO ARAGUAIA | PARÁ | Brasil | 1506708 | 15 | 33 | nan | nan | nan | Amazônia | 110.1 |
| b537b1a2-04e4-384d-b6a9-6a90b4dd8498 | -6.7073 | -45.5087 | 2026-09-11 15:20:00 | GOES-19 | MIRADOR | MARANHÃO | Brasil | 2106706 | 21 | 33 | nan | nan | nan | Cerrado | 91.3 |
| 482f716f-d698-3a09-a9d3-608429af21f2 | -10.2746 | -45.2497 | 2026-09-11 15:20:00 | GOES-19 | CORRENTE | PIAUÍ | Brasil | 2202901 | 22 | 33 | nan | nan | nan | Cerrado | 89.3 |
| 98aac882-d79b-3ff3-ba75-2f0fda6cd99e | -8.5421 | -72.4352 | 2026-09-11 15:20:00 | GOES-19 | PORTO WALTER | ACRE | Brasil | 1200393 | 12 | 33 | nan | nan | nan | Amazônia | 45.3 |
| fbb911f4-d68c-3026-8df5-d19bc5f94a96 | -10.4722 | -51.3442 | 2026-09-11 15:20:00 | GOES-19 | CONFRESA | MATO GROSSO | Brasil | 5103353 | 51 | 33 | nan | nan | nan | Amazônia | 155.7 |
| ab493daa-7d90-3390-9a61-cf081b2ba856 | -8.0934 | -54.8488 | 2026-09-11 15:20:00 | GOES-19 | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 122.7 |
| a0adeb7a-cb25-3abb-8f6d-03fc9e8a7434 | -6.4047 | -54.9642 | 2026-09-11 15:20:00 | GOES-19 | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 78.1 |
| 409cc22b-a56f-36bf-98f4-5260b82d1611 | -5.9817 | -57.7282 | 2026-09-11 15:20:00 | GOES-19 | JACAREACANGA | PARÁ | Brasil | 1503754 | 15 | 33 | nan | nan | nan | Amazônia | 56.5 |
| e0d65fb3-cf23-381a-bb1b-360c05773765 | -9.6857 | -48.0069 | 2026-09-11 15:20:00 | GOES-19 | TOCANTÍNIA | TOCANTINS | Brasil | 1721109 | 17 | 33 | nan | nan | nan | Cerrado | 216.5 |
| e46c6dc9-c588-31e5-9301-b24d492df49f | -8.6311 | -66.5101 | 2026-09-11 15:20:00 | GOES-19 | LÁBREA | AMAZONAS | Brasil | 1302405 | 13 | 33 | nan | nan | nan | Amazônia | 88.4 |


[Clique aqui para ver as próximas entradas](README44.md)
