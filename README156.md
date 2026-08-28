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

## Dados Diários - Página 156

| ID | Latitude | Longitude | Data/Hora GMT | Satélite | Município | Estado | País | Município ID | Estado ID | País ID | Dias sem Chuva | Precipitação | Risco de Fogo | Bioma | FRP |
|----|----------|-----------|---------------|----------|-----------|--------|------|--------------|-----------|---------|----------------|--------------|----------------|-------|-----|
| c793ba20-85d7-3449-b7ef-e0c416fc9381 | 1.7164 | -56.0347 | 2026-08-28 17:49:00 | NOAA-20 | ORIXIMINÁ | PARÁ | Brasil | 1505304 | 15 | 33 | nan | nan | nan | Amazônia | 4.9 |
| 97651f34-1a67-3d94-bccb-0eaf20e21d7d | -1.25122 | -55.70674 | 2026-08-28 17:49:00 | NOAA-20 | ÓBIDOS | PARÁ | Brasil | 1505106 | 15 | 33 | nan | nan | nan | Amazônia | 3.2 |
| 6dc6a0c5-4345-3d1d-9084-8698d1a10f03 | -1.25172 | -55.70983 | 2026-08-28 17:49:00 | NOAA-20 | ÓBIDOS | PARÁ | Brasil | 1505106 | 15 | 33 | nan | nan | nan | Amazônia | 6.7 |
| c0448720-252f-37c7-b7b7-5d99e4f98259 | 4.13516 | -61.28403 | 2026-08-28 17:49:00 | NOAA-20 | AMAJARI | RORAIMA | Brasil | 1400027 | 14 | 33 | nan | nan | nan | Amazônia | 6.9 |
| 701dcac2-8ab2-3962-975d-bee0956d05c5 | 0.08254 | -60.55837 | 2026-08-28 17:49:00 | NOAA-20 | RORAINÓPOLIS | RORAIMA | Brasil | 1400472 | 14 | 33 | nan | nan | nan | Amazônia | 6.1 |
| 1bbb1e58-e2f5-3dee-b201-da809f82648e | 4.93596 | -60.30511 | 2026-08-28 17:49:00 | NOAA-20 | UIRAMUTÃ | RORAIMA | Brasil | 1400704 | 14 | 33 | nan | nan | nan | Amazônia | 6.1 |
| 2a16c915-a60e-3d77-9053-e3872cd1680b | 4.13053 | -61.28836 | 2026-08-28 17:49:00 | NOAA-20 | AMAJARI | RORAIMA | Brasil | 1400027 | 14 | 33 | nan | nan | nan | Amazônia | 6.9 |
| 28c4ff36-a7a8-347b-9a7c-98e4340fea6f | 0.14633 | -60.39936 | 2026-08-28 17:49:00 | NOAA-20 | RORAINÓPOLIS | RORAIMA | Brasil | 1400472 | 14 | 33 | nan | nan | nan | Amazônia | 28.0 |
| 5d2c1167-1d03-3575-b77e-5933b2b553b7 | -1.33003 | -55.96684 | 2026-08-28 17:49:00 | NOAA-20 | ORIXIMINÁ | PARÁ | Brasil | 1505304 | 15 | 33 | nan | nan | nan | Amazônia | 2.8 |
| b7332ee7-6729-310a-91aa-f7f5ad5d90f3 | -1.25272 | -55.71605 | 2026-08-28 17:49:00 | NOAA-20 | ÓBIDOS | PARÁ | Brasil | 1505106 | 15 | 33 | nan | nan | nan | Amazônia | 3.9 |
| c8c4fe10-36e8-3728-9d7e-82133655bc18 | 4.13443 | -61.28893 | 2026-08-28 17:49:00 | NOAA-20 | AMAJARI | RORAIMA | Brasil | 1400027 | 14 | 33 | nan | nan | nan | Amazônia | 6.9 |
| 5bbea687-973d-3df2-8197-65db1f99bebb | 0.91303 | -59.62978 | 2026-08-28 17:49:00 | NOAA-20 | CAROEBE | RORAIMA | Brasil | 1400233 | 14 | 33 | nan | nan | nan | Amazônia | 18.3 |
| e5a383e7-89c3-30b9-8d50-c7255a233d7c | 1.7892 | -55.82312 | 2026-08-28 17:49:00 | NOAA-20 | ÓBIDOS | PARÁ | Brasil | 1505106 | 15 | 33 | nan | nan | nan | Amazônia | 4.6 |
| 351ba848-4650-3d35-a461-9618a1cba4b8 | 4.13371 | -61.29383 | 2026-08-28 17:49:00 | NOAA-20 | AMAJARI | RORAIMA | Brasil | 1400027 | 14 | 33 | nan | nan | nan | Amazônia | 5.2 |
| ce14054a-9cc6-31e9-860e-c02111f9c578 | -1.23299 | -55.96728 | 2026-08-28 17:49:00 | NOAA-20 | ÓBIDOS | PARÁ | Brasil | 1505106 | 15 | 33 | nan | nan | nan | Amazônia | 3.2 |
| 6d73c422-5140-3880-a109-1574642406fb | 0.9136 | -59.626 | 2026-08-28 17:49:00 | NOAA-20 | CAROEBE | RORAIMA | Brasil | 1400233 | 14 | 33 | nan | nan | nan | Amazônia | 11.5 |
| ffb9d08c-e1c2-3572-bcf3-3e10c8de3a6e | -1.25221 | -55.71289 | 2026-08-28 17:49:00 | NOAA-20 | ÓBIDOS | PARÁ | Brasil | 1505106 | 15 | 33 | nan | nan | nan | Amazônia | 6.7 |
| aeb10877-e6f9-3231-96ec-f4715893c663 | 4.12981 | -61.29326 | 2026-08-28 17:49:00 | NOAA-20 | AMAJARI | RORAIMA | Brasil | 1400027 | 14 | 33 | nan | nan | nan | Amazônia | 5.2 |
| 7b51a3bb-a103-3f7f-9c32-b07d21722b4d | -1.34648 | -55.46168 | 2026-08-28 17:49:00 | NOAA-20 | ÓBIDOS | PARÁ | Brasil | 1505106 | 15 | 33 | nan | nan | nan | Amazônia | 3.5 |
| 41c62920-1f9e-3163-8f31-1d3eb95b4c38 | 0.08077 | -60.55896 | 2026-08-28 17:49:00 | NOAA-20 | RORAINÓPOLIS | RORAIMA | Brasil | 1400472 | 14 | 33 | nan | nan | nan | Amazônia | 6.8 |
| 2b98eb6d-6299-3b73-9fa9-ae11f2003e3b | 0.14243 | -60.39878 | 2026-08-28 17:49:00 | NOAA-20 | RORAINÓPOLIS | RORAIMA | Brasil | 1400472 | 14 | 33 | nan | nan | nan | Amazônia | 28.0 |
| 77537c78-902c-39c4-acd6-762ecc30871f | 3.90969 | -59.85138 | 2026-08-28 17:49:00 | NOAA-20 | NORMANDIA | RORAIMA | Brasil | 1400407 | 14 | 33 | nan | nan | nan | Amazônia | 3.1 |
| b178d8e9-e51c-361f-951a-2487c85a2cc4 | 4.12417 | -61.27742 | 2026-08-28 17:49:00 | NOAA-20 | AMAJARI | RORAIMA | Brasil | 1400027 | 14 | 33 | nan | nan | nan | Amazônia | 10.8 |
| 14330b93-f998-3565-bb70-b744e119108e | -8.5975 | -54.715 | 2026-08-28 17:50:00 | GOES-19 | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 84.6 |
| e7c6b0aa-8e92-3bbb-a14c-4cbd9b1db315 | -8.0737 | -45.8598 | 2026-08-28 17:50:00 | GOES-19 | BALSAS | MARANHÃO | Brasil | 2101400 | 21 | 33 | nan | nan | nan | Cerrado | 66.2 |
| aa9aee85-7ffc-397c-ab05-fd009ee66ec8 | -4.3205 | -59.4821 | 2026-08-28 17:50:00 | GOES-19 | BORBA | AMAZONAS | Brasil | 1300805 | 13 | 33 | nan | nan | nan | Amazônia | 51.1 |
| 46441619-a6c3-396a-8da0-965e7d68a430 | -8.0739 | -45.8372 | 2026-08-28 17:50:00 | GOES-19 | BALSAS | MARANHÃO | Brasil | 2101400 | 21 | 33 | nan | nan | nan | Cerrado | 111.5 |
| 1cfefb80-cd87-38a6-9d12-f6e30154c436 | -8.631 | -66.5473 | 2026-08-28 17:50:00 | GOES-19 | LÁBREA | AMAZONAS | Brasil | 1302405 | 13 | 33 | nan | nan | nan | Amazônia | 77.8 |
| 859aee24-c91a-3cd4-b543-71d68f983b8f | -14.9008 | -52.6479 | 2026-08-28 17:50:00 | GOES-19 | BARRA DO GARÇAS | MATO GROSSO | Brasil | 5101803 | 51 | 33 | nan | nan | nan | Cerrado | 197.1 |
| 83e13ab0-c1ec-3f61-83c3-7ae8c6c46ef9 | -10.8422 | -50.5219 | 2026-08-28 17:50:00 | GOES-19 | LAGOA DA CONFUSÃO | TOCANTINS | Brasil | 1711902 | 17 | 33 | nan | nan | nan | Cerrado | 70.2 |
| 9c42d364-5945-304b-a3ad-c29f1a805427 | -11.2109 | -51.2476 | 2026-08-28 17:50:00 | GOES-19 | LUCIARA | MATO GROSSO | Brasil | 5105309 | 51 | 33 | nan | nan | nan | Cerrado | 44.8 |
| 6cdd7e80-e2ff-3237-b94d-ad3dd1ecef6d | -10.5598 | -50.4236 | 2026-08-28 17:50:00 | GOES-19 | PIUM | TOCANTINS | Brasil | 1717503 | 17 | 33 | nan | nan | nan | Cerrado | 77.3 |
| 9613b1c9-5d27-3499-9045-2f53f038154d | -9.8618 | -65.0146 | 2026-08-28 17:50:00 | GOES-19 | PORTO VELHO | RONDÔNIA | Brasil | 1100205 | 11 | 33 | nan | nan | nan | Amazônia | 92.7 |
| 12636e94-95f8-3663-a44e-25bcc285470d | -11.3476 | -48.3872 | 2026-08-28 17:50:00 | GOES-19 | SANTA ROSA DO TOCANTINS | TOCANTINS | Brasil | 1718907 | 17 | 33 | nan | nan | nan | Cerrado | 78.6 |
| ea184a8a-ebe1-3a5d-ab3d-b4c0285aebde | -12.2093 | -50.5386 | 2026-08-28 17:50:00 | GOES-19 | FORMOSO DO ARAGUAIA | TOCANTINS | Brasil | 1708205 | 17 | 33 | nan | nan | nan | Cerrado | 57.7 |
| 6f82eda7-b7df-3f4f-887c-95135ae14b85 | -11.006 | -49.6461 | 2026-08-28 17:50:00 | GOES-19 | SANTA RITA DO TOCANTINS | TOCANTINS | Brasil | 1718899 | 17 | 33 | nan | nan | nan | Cerrado | 98.9 |
| fd29ce96-7ac4-36f0-b221-77a196e2c0e5 | -9.2282 | -51.5428 | 2026-08-28 17:50:00 | GOES-19 | SÃO FÉLIX DO XINGU | PARÁ | Brasil | 1507300 | 15 | 33 | nan | nan | nan | Amazônia | 43.4 |
| 7b512a7b-134f-3a9a-bb4e-7a4260c73a54 | -7.5852 | -61.2089 | 2026-08-28 17:50:00 | GOES-19 | NOVO ARIPUANÃ | AMAZONAS | Brasil | 1303304 | 13 | 33 | nan | nan | nan | Amazônia | 65.5 |
| ecacc5f0-49f9-31a5-a519-a7f1145e456f | -10.498 | -64.5193 | 2026-08-28 17:50:00 | GOES-19 | NOVA MAMORÉ | RONDÔNIA | Brasil | 1100338 | 11 | 33 | nan | nan | nan | Amazônia | 67.2 |
| 2bd0f2c5-dc98-359e-ad48-c7f08104294e | -13.4707 | -57.0574 | 2026-08-28 17:50:00 | GOES-19 | NOVA MARINGÁ | MATO GROSSO | Brasil | 5108907 | 51 | 33 | nan | nan | nan | Cerrado | 82.4 |
| 49881cc0-7335-35ca-818f-e273710fe58b | -13.4132 | -51.7784 | 2026-08-28 17:50:00 | GOES-19 | RIBEIRÃO CASCALHEIRA | MATO GROSSO | Brasil | 5107180 | 51 | 33 | nan | nan | nan | Cerrado | 76.5 |
| c7fe052d-2cba-3641-b5ad-51c092764e68 | -14.8817 | -52.6293 | 2026-08-28 17:50:00 | GOES-19 | NOVA XAVANTINA | MATO GROSSO | Brasil | 5106257 | 51 | 33 | nan | nan | nan | Cerrado | 444.6 |
| d056a8c2-0199-37d7-a06f-bf470f5a5cf6 | -12.3999 | -48.2073 | 2026-08-28 17:50:00 | GOES-19 | PARANÃ | TOCANTINS | Brasil | 1716208 | 17 | 33 | nan | nan | nan | Cerrado | 61.0 |
| 695287b2-7475-363d-9db1-32b8e573dfbc | -10.7603 | -53.9769 | 2026-08-28 17:50:00 | GOES-19 | MARCELÂNDIA | MATO GROSSO | Brasil | 5105580 | 51 | 33 | nan | nan | nan | Amazônia | 74.4 |
| 7ae962b4-6b67-35a4-8e59-f49f928c7e6b | -6.7648 | -59.4408 | 2026-08-28 17:50:00 | GOES-19 | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 72.8 |
| 11deeca1-9957-3ba1-9873-1a13bbc34b42 | -6.8008 | -59.5934 | 2026-08-28 17:50:00 | GOES-19 | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 66.4 |
| 2c7892d4-82a5-3cc7-8048-f5c2c5c1b1c5 | -4.3022 | -59.4634 | 2026-08-28 17:50:00 | GOES-19 | BORBA | AMAZONAS | Brasil | 1300805 | 13 | 33 | nan | nan | nan | Amazônia | 78.1 |
| cc15e477-abce-3c1b-a570-a15abc3af92c | -6.8755 | -59.4364 | 2026-08-28 17:50:00 | GOES-19 | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 90.0 |
| 3cb3cdd3-352c-3eb3-a111-339c9341bc7e | -8.0742 | -45.8147 | 2026-08-28 17:50:00 | GOES-19 | BALSAS | MARANHÃO | Brasil | 2101400 | 21 | 33 | nan | nan | nan | Cerrado | 68.8 |
| d41e465b-f751-3690-843f-eb3f0d293b94 | -15.3654 | -53.7887 | 2026-08-28 17:50:00 | GOES-19 | POXORÉU | MATO GROSSO | Brasil | 5107008 | 51 | 33 | nan | nan | nan | Cerrado | 69.0 |
| 2cc1c78d-c12a-36ff-aa13-20db65c30725 | -7.4735 | -61.3846 | 2026-08-28 17:50:00 | GOES-19 | MANICORÉ | AMAZONAS | Brasil | 1302702 | 13 | 33 | nan | nan | nan | Amazônia | 70.2 |
| 08ad0aa1-8b0d-3221-a906-febe37ec39a9 | -6.8358 | -59.9379 | 2026-08-28 17:50:00 | GOES-19 | NOVO ARIPUANÃ | AMAZONAS | Brasil | 1303304 | 13 | 33 | nan | nan | nan | Amazônia | 104.2 |
| d9f61e88-ac13-3d60-a24b-15dd770b305a | -8.0928 | -45.8354 | 2026-08-28 17:50:00 | GOES-19 | BALSAS | MARANHÃO | Brasil | 2101400 | 21 | 33 | nan | nan | nan | Cerrado | 94.5 |
| e16364d2-2fff-3806-9024-b71e2c5e3621 | -8.803 | -70.84 | 2026-08-28 17:50:00 | GOES-19 | FEIJÓ | ACRE | Brasil | 1200302 | 12 | 33 | nan | nan | nan | Amazônia | 70.6 |
| d434c309-dcc1-31f8-ba6e-0e9e2e46ea2f | -8.87 | -66.8935 | 2026-08-28 17:50:00 | GOES-19 | LÁBREA | AMAZONAS | Brasil | 1302405 | 13 | 33 | nan | nan | nan | Amazônia | 51.5 |
| 5d210134-3a7d-3eec-a057-ddddbb78dbfa | -8.9138 | -70.8752 | 2026-08-28 17:50:00 | GOES-19 | FEIJÓ | ACRE | Brasil | 1200302 | 12 | 33 | nan | nan | nan | Amazônia | 52.5 |
| 54da7ec6-acb0-3162-9c68-7a9c6e9b9ebb | -8.6694 | -49.5369 | 2026-08-28 17:50:00 | GOES-19 | CONCEIÇÃO DO ARAGUAIA | PARÁ | Brasil | 1502707 | 15 | 33 | nan | nan | nan | Amazônia | 108.2 |
| 7648dcf6-84d1-3f28-8e51-4305e062ffde | -8.0551 | -45.839 | 2026-08-28 17:50:00 | GOES-19 | BALSAS | MARANHÃO | Brasil | 2101400 | 21 | 33 | nan | nan | nan | Cerrado | 64.6 |
| b2b45e32-90b1-3a06-be5f-0643f461887c | -7.3665 | -55.1534 | 2026-08-28 17:50:00 | GOES-19 | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 75.3 |
| 9a532a80-9553-3e56-9055-31dccb3ba3d7 | -9.8432 | -65.0153 | 2026-08-28 17:50:00 | GOES-19 | PORTO VELHO | RONDÔNIA | Brasil | 1100205 | 11 | 33 | nan | nan | nan | Amazônia | 52.8 |
| 6ad02bee-7a6e-3aab-b6bf-6fac38416f74 | -9.1525 | -49.9639 | 2026-08-28 17:50:00 | GOES-19 | SANTANA DO ARAGUAIA | PARÁ | Brasil | 1506708 | 15 | 33 | nan | nan | nan | Amazônia | 161.9 |
| 124b84ed-12a8-3580-9ba2-ef1e18079d2d | -12.2281 | -50.5578 | 2026-08-28 17:50:00 | GOES-19 | FORMOSO DO ARAGUAIA | TOCANTINS | Brasil | 1708205 | 17 | 33 | nan | nan | nan | Cerrado | 66.2 |
| 8d61f497-6545-3055-954c-989eadb6a27b | -12.9054 | -59.8857 | 2026-08-28 17:50:00 | GOES-19 | COMODORO | MATO GROSSO | Brasil | 5103304 | 51 | 33 | nan | nan | nan | Cerrado | 63.3 |
| 7d9b8299-5bc3-3f39-a3e1-52a5eed2b416 | -11.1998 | -55.0805 | 2026-08-28 17:50:00 | GOES-19 | ITAÚBA | MATO GROSSO | Brasil | 5104559 | 51 | 33 | nan | nan | nan | Amazônia | 59.9 |
| b43f87d2-2735-33cc-9df3-aad3e7291a47 | -8.6311 | -66.5287 | 2026-08-28 17:50:00 | GOES-19 | LÁBREA | AMAZONAS | Brasil | 1302405 | 13 | 33 | nan | nan | nan | Amazônia | 58.5 |
| 05680d88-e4c7-34a0-9b3b-72e9a5811532 | -9.1714 | -59.5793 | 2026-08-28 17:50:00 | GOES-19 | COLNIZA | MATO GROSSO | Brasil | 5103254 | 51 | 33 | nan | nan | nan | Amazônia | 65.1 |
| a222b294-f895-375b-a06c-c636db3bf7a9 | -8.4341 | -70.7166 | 2026-08-28 17:50:00 | GOES-19 | TARAUACÁ | ACRE | Brasil | 1200609 | 12 | 33 | nan | nan | nan | Amazônia | 72.2 |
| 991c7662-94b0-3215-a7b1-94ff974f436f | -9.2477 | -57.0697 | 2026-08-28 17:50:00 | GOES-19 | PARANAÍTA | MATO GROSSO | Brasil | 5106299 | 51 | 33 | nan | nan | nan | Amazônia | 82.0 |
| a903b123-fb31-3386-927e-0163b307dda0 | -14.8627 | -52.6106 | 2026-08-28 17:50:00 | GOES-19 | NOVA XAVANTINA | MATO GROSSO | Brasil | 5106257 | 51 | 33 | nan | nan | nan | Cerrado | 111.1 |
| f7a3c165-32c1-343b-a504-ead9dd4cc97a | -6.7123 | -58.9412 | 2026-08-28 17:50:00 | GOES-19 | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 78.3 |
| 28d1e039-476b-3e30-b57b-3615dac9b6b5 | -10.7649 | -50.6366 | 2026-08-28 17:50:00 | GOES-19 | LUCIARA | MATO GROSSO | Brasil | 5105309 | 51 | 33 | nan | nan | nan | Cerrado | 73.5 |
| b4e02546-234c-3a36-bd8b-ef4fe630aa89 | -6.8569 | -59.4564 | 2026-08-28 18:00:00 | GOES-19 | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 102.7 |
| c2c1e945-f867-3bd2-8000-ce1723028202 | -6.7647 | -59.4601 | 2026-08-28 18:00:00 | GOES-19 | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 92.4 |
| b446c8cf-dde4-3928-9e79-2d9d77b8ad68 | -4.3021 | -59.4826 | 2026-08-28 18:00:00 | GOES-19 | BORBA | AMAZONAS | Brasil | 1300805 | 13 | 33 | nan | nan | nan | Amazônia | 98.8 |
| 3ee03e2f-3618-392d-b418-ed7c48926d3b | -9.7878 | -43.5506 | 2026-08-28 18:00:00 | GOES-19 | PILÃO ARCADO | BAHIA | Brasil | 2924405 | 29 | 33 | nan | nan | nan | Cerrado | 137.8 |
| b1fc5251-6992-3148-b5f4-44a42419a81f | -7.5845 | -61.3423 | 2026-08-28 18:00:00 | GOES-19 | MANICORÉ | AMAZONAS | Brasil | 1302702 | 13 | 33 | nan | nan | nan | Amazônia | 253.4 |
| 434716ac-132b-3f47-b93a-0721e6b573ef | -8.7846 | -70.8219 | 2026-08-28 18:00:00 | GOES-19 | FEIJÓ | ACRE | Brasil | 1200302 | 12 | 33 | nan | nan | nan | Amazônia | 55.2 |
| cb6e7835-e1c7-35e8-b8f9-51166759e10a | -7.5847 | -61.3042 | 2026-08-28 18:00:00 | GOES-19 | MANICORÉ | AMAZONAS | Brasil | 1302702 | 13 | 33 | nan | nan | nan | Amazônia | 57.1 |
| d027cd75-f208-32b9-a809-389a85a9104c | -11.0057 | -49.6677 | 2026-08-28 18:00:00 | GOES-19 | SANTA RITA DO TOCANTINS | TOCANTINS | Brasil | 1718899 | 17 | 33 | nan | nan | nan | Cerrado | 64.7 |
| 203a3bc7-02e1-314a-b2bc-f414bb37e511 | -9.4331 | -51.6716 | 2026-08-28 18:00:00 | GOES-19 | SÃO FÉLIX DO XINGU | PARÁ | Brasil | 1507300 | 15 | 33 | nan | nan | nan | Amazônia | 86.0 |
| b6a85371-bb26-3635-8db5-79dc680d4f73 | -11.006 | -49.6461 | 2026-08-28 18:00:00 | GOES-19 | SANTA RITA DO TOCANTINS | TOCANTINS | Brasil | 1718899 | 17 | 33 | nan | nan | nan | Cerrado | 134.5 |
| 53614f48-e0d8-3710-aaa8-cbcebba8896a | -6.8358 | -59.9379 | 2026-08-28 18:00:00 | GOES-19 | NOVO ARIPUANÃ | AMAZONAS | Brasil | 1303304 | 13 | 33 | nan | nan | nan | Amazônia | 121.7 |
| 1677f107-de7f-3bf3-b705-1845b9dfa8ba | -10.0731 | -48.6868 | 2026-08-28 18:00:00 | GOES-19 | MIRACEMA DO TOCANTINS | TOCANTINS | Brasil | 1713205 | 17 | 33 | nan | nan | nan | Cerrado | 63.8 |
| a2d5e301-0160-3dfd-b2ac-340751c4e6e1 | -6.7451 | -59.6533 | 2026-08-28 18:00:00 | GOES-19 | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 70.7 |
| 2a119e19-4cd9-3750-8001-105f6acb0e71 | -8.8761 | -71.2607 | 2026-08-28 18:00:00 | GOES-19 | FEIJÓ | ACRE | Brasil | 1200302 | 12 | 33 | nan | nan | nan | Amazônia | 51.6 |
| 5413c84f-de54-3b5b-b1fd-ec63ac0e6eb6 | -15.6554 | -53.856 | 2026-08-28 18:00:00 | GOES-19 | GENERAL CARNEIRO | MATO GROSSO | Brasil | 5103908 | 51 | 33 | nan | nan | nan | Cerrado | 72.6 |
| aec8a1d4-7174-3e74-8c09-9dd58007b831 | -5.9996 | -57.8249 | 2026-08-28 18:00:00 | GOES-19 | JACAREACANGA | PARÁ | Brasil | 1503754 | 15 | 33 | nan | nan | nan | Amazônia | 64.2 |
| 4f173dfe-2a27-31b6-80cb-12d65b33fa7a | -8.795 | -50.0387 | 2026-08-28 18:00:00 | GOES-19 | SANTA MARIA DAS BARREIRAS | PARÁ | Brasil | 1506583 | 15 | 33 | nan | nan | nan | Amazônia | 71.2 |
| cf4f0727-d329-3933-868f-baaddb1fe30f | -8.6694 | -49.5369 | 2026-08-28 18:00:00 | GOES-19 | CONCEIÇÃO DO ARAGUAIA | PARÁ | Brasil | 1502707 | 15 | 33 | nan | nan | nan | Amazônia | 100.2 |
| f8a0291f-380f-3545-93b7-2563e54cc68f | -6.8368 | -59.7458 | 2026-08-28 18:00:00 | GOES-19 | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 116.6 |
| 742ed6ab-973b-3996-a1aa-4f5018eb6ba7 | -9.1543 | -70.8168 | 2026-08-28 18:00:00 | GOES-19 | FEIJÓ | ACRE | Brasil | 1200302 | 12 | 33 | nan | nan | nan | Amazônia | 51.5 |
| 6162cd81-b609-34be-8aa9-45f4c86e359f | -15.401 | -52.8564 | 2026-08-28 18:00:00 | GOES-19 | BARRA DO GARÇAS | MATO GROSSO | Brasil | 5101803 | 51 | 33 | nan | nan | nan | Cerrado | 105.2 |
| 11243f5f-7731-3c87-b10b-5315e59aad05 | -12.0733 | -47.1614 | 2026-08-28 18:00:00 | GOES-19 | CONCEIÇÃO DO TOCANTINS | TOCANTINS | Brasil | 1705607 | 17 | 33 | nan | nan | nan | Cerrado | 67.6 |
| 9d85dcd1-66c7-392d-a20e-2be7c7e63d83 | -9.8618 | -65.0146 | 2026-08-28 18:00:00 | GOES-19 | PORTO VELHO | RONDÔNIA | Brasil | 1100205 | 11 | 33 | nan | nan | nan | Amazônia | 91.9 |
| 86a988ea-2a15-3900-880a-7ff53886a428 | -8.8184 | -49.6308 | 2026-08-28 18:00:00 | GOES-19 | SANTA MARIA DAS BARREIRAS | PARÁ | Brasil | 1506583 | 15 | 33 | nan | nan | nan | Amazônia | 79.4 |
| 1db76ea1-8290-39f5-8286-d30d57b08ab9 | -14.8627 | -52.6106 | 2026-08-28 18:00:00 | GOES-19 | NOVA XAVANTINA | MATO GROSSO | Brasil | 5106257 | 51 | 33 | nan | nan | nan | Cerrado | 95.6 |
| fe648c29-a36f-3522-8210-308333aa2e46 | -8.8031 | -70.8217 | 2026-08-28 18:00:00 | GOES-19 | FEIJÓ | ACRE | Brasil | 1200302 | 12 | 33 | nan | nan | nan | Amazônia | 49.3 |
| a07b0882-ca09-3c28-99ea-0b2eb1ad8acb | -6.9521 | -58.9506 | 2026-08-28 18:00:00 | GOES-19 | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 204.5 |
| 66fe2586-dbc0-390e-909a-f2eb3dc325f8 | -8.631 | -66.5473 | 2026-08-28 18:00:00 | GOES-19 | LÁBREA | AMAZONAS | Brasil | 1302405 | 13 | 33 | nan | nan | nan | Amazônia | 86.1 |
| 38869960-d386-3621-9653-eafa64af0b02 | -12.9244 | -59.8843 | 2026-08-28 18:00:00 | GOES-19 | COMODORO | MATO GROSSO | Brasil | 5103304 | 51 | 33 | nan | nan | nan | Cerrado | 80.6 |


[Clique aqui para ver as próximas entradas](README157.md)
