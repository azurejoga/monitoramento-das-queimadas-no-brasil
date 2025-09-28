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

## Dados Diários - Página 84

| ID | Latitude | Longitude | Data/Hora GMT | Satélite | Município | Estado | País | Município ID | Estado ID | País ID | Dias sem Chuva | Precipitação | Risco de Fogo | Bioma | FRP |
|----|----------|-----------|---------------|----------|-----------|--------|------|--------------|-----------|---------|----------------|--------------|----------------|-------|-----|
| 058e9c06-ae2f-3200-8198-bc2076125448 | -7.7581 | -47.00064 | 2025-09-28 05:16:00 | NOAA-21 | CAROLINA | MARANHÃO | Brasil | 2102804 | 21 | 33 | nan | nan | nan | Cerrado | 2.9 |
| 75dbf148-2e46-3b29-9da0-b6945e65ef7a | -7.79701 | -47.00512 | 2025-09-28 05:16:00 | NOAA-21 | CAROLINA | MARANHÃO | Brasil | 2102804 | 21 | 33 | nan | nan | nan | Cerrado | 2.9 |
| 15c0f7a9-7217-32a3-aaa2-1309ab83b808 | -3.21143 | -51.27356 | 2025-09-28 05:16:00 | NOAA-21 | ANAPU | PARÁ | Brasil | 1500859 | 15 | 33 | nan | nan | nan | Amazônia | 1.7 |
| e55345ea-11e7-3d77-a965-9d596b0ce03e | -7.16568 | -45.51089 | 2025-09-28 05:16:00 | NOAA-21 | SÃO RAIMUNDO DAS MANGABEIRAS | MARANHÃO | Brasil | 2111607 | 21 | 33 | nan | nan | nan | Cerrado | 1.4 |
| f881de70-1e0b-36d4-9a51-c25564a20e4d | -7.80489 | -46.99521 | 2025-09-28 05:16:00 | NOAA-21 | CAROLINA | MARANHÃO | Brasil | 2102804 | 21 | 33 | nan | nan | nan | Cerrado | 2.8 |
| 0eb21a4c-a651-388a-87ff-960e646e930d | -7.37748 | -47.02469 | 2025-09-28 05:16:00 | NOAA-21 | RIACHÃO | MARANHÃO | Brasil | 2109502 | 21 | 33 | nan | nan | nan | Cerrado | 4.2 |
| 074c58f8-44a5-3e06-90d6-a642190e8164 | -5.81384 | -47.81242 | 2025-09-28 05:16:00 | NOAA-21 | SÃO BENTO DO TOCANTINS | TOCANTINS | Brasil | 1720101 | 17 | 33 | nan | nan | nan | Cerrado | 2.2 |
| d53f2f78-d404-39e6-974b-9ef129b71cee | -8.17131 | -46.42028 | 2025-09-28 05:16:00 | NOAA-21 | RIACHÃO | MARANHÃO | Brasil | 2109502 | 21 | 33 | nan | nan | nan | Cerrado | 15.8 |
| 49f0166b-027f-3523-9c18-48e4523479a2 | -8.17204 | -46.41421 | 2025-09-28 05:16:00 | NOAA-21 | RIACHÃO | MARANHÃO | Brasil | 2109502 | 21 | 33 | nan | nan | nan | Cerrado | 15.8 |
| 8bb224cf-a4b4-3567-83d0-ab9a8ffd0c4c | -4.53556 | -48.64959 | 2025-09-28 05:16:00 | NOAA-21 | RONDON DO PARÁ | PARÁ | Brasil | 1506187 | 15 | 33 | nan | nan | nan | Amazônia | 2.0 |
| 80c3b842-e241-3db3-8b03-a53a43dccea1 | -7.80962 | -47.01376 | 2025-09-28 05:16:00 | NOAA-21 | CAROLINA | MARANHÃO | Brasil | 2102804 | 21 | 33 | nan | nan | nan | Cerrado | 19.1 |
| a2f82769-195d-3c8a-abb5-c0e564ff647f | -5.3594 | -45.03679 | 2025-09-28 05:16:00 | NOAA-21 | BARRA DO CORDA | MARANHÃO | Brasil | 2101608 | 21 | 33 | nan | nan | nan | Cerrado | 1.8 |
| 413ada55-d984-3ba7-b28a-f65d18618967 | -3.64762 | -55.47836 | 2025-09-28 05:16:00 | NOAA-21 | AVEIRO | PARÁ | Brasil | 1501006 | 15 | 33 | nan | nan | nan | Amazônia | 0.6 |
| 9c36ce16-0b77-3b57-9bcc-d21d29743d27 | -5.35226 | -45.03593 | 2025-09-28 05:16:00 | NOAA-21 | BARRA DO CORDA | MARANHÃO | Brasil | 2101608 | 21 | 33 | nan | nan | nan | Cerrado | 1.2 |
| a04df2b2-6621-3f64-933b-b24d359aaeff | -7.81729 | -47.0025 | 2025-09-28 05:16:00 | NOAA-21 | CAROLINA | MARANHÃO | Brasil | 2102804 | 21 | 33 | nan | nan | nan | Cerrado | 6.9 |
| 83e4bd57-b92f-36ad-b9d3-550e314067bc | -7.75228 | -46.99406 | 2025-09-28 05:16:00 | NOAA-21 | CAROLINA | MARANHÃO | Brasil | 2102804 | 21 | 33 | nan | nan | nan | Cerrado | 7.3 |
| 42da87e5-89f8-3ed7-8131-9e1e16888649 | -6.80835 | -46.3982 | 2025-09-28 05:16:00 | NOAA-21 | FORMOSA DA SERRA NEGRA | MARANHÃO | Brasil | 2104099 | 21 | 33 | nan | nan | nan | Cerrado | 2.1 |
| 8eb33162-fd1b-33f5-a0c8-0ebf191f5933 | -7.80805 | -47.02336 | 2025-09-28 05:16:00 | NOAA-21 | CAROLINA | MARANHÃO | Brasil | 2102804 | 21 | 33 | nan | nan | nan | Cerrado | 20.9 |
| 400a3474-3035-36e3-8c32-394f4d436274 | -7.54089 | -46.10767 | 2025-09-28 05:16:00 | NOAA-21 | BALSAS | MARANHÃO | Brasil | 2101400 | 21 | 33 | nan | nan | nan | Cerrado | 3.3 |
| 8037aa02-5143-3804-9415-80073cf8b86f | -2.58703 | -48.40601 | 2025-09-28 05:16:00 | NOAA-21 | TOMÉ-AÇU | PARÁ | Brasil | 1508001 | 15 | 33 | nan | nan | nan | Amazônia | 10.6 |
| 19347f8f-ccf9-33dc-b30c-6ae6d5796c3d | -7.75157 | -46.99968 | 2025-09-28 05:16:00 | NOAA-21 | CAROLINA | MARANHÃO | Brasil | 2102804 | 21 | 33 | nan | nan | nan | Cerrado | 4.1 |
| b3c1cdd9-4fe5-3c82-ac8c-2f50a245a0e9 | -4.14281 | -47.64983 | 2025-09-28 05:16:00 | NOAA-21 | DOM ELISEU | PARÁ | Brasil | 1502939 | 15 | 33 | nan | nan | nan | Amazônia | 1.9 |
| 016a8b97-abfe-3ce8-876d-a94ed62966ec | -4.14216 | -47.65442 | 2025-09-28 05:16:00 | NOAA-21 | DOM ELISEU | PARÁ | Brasil | 1502939 | 15 | 33 | nan | nan | nan | Amazônia | 2.5 |
| 73e73269-3897-38ee-a14e-30cfcf86f964 | -7.78262 | -47.0139 | 2025-09-28 05:16:00 | NOAA-21 | CAROLINA | MARANHÃO | Brasil | 2102804 | 21 | 33 | nan | nan | nan | Cerrado | 2.4 |
| d5c4d935-5998-3ff1-a351-0fb6e769c51e | -7.75086 | -47.00522 | 2025-09-28 05:16:00 | NOAA-21 | CAROLINA | MARANHÃO | Brasil | 2102804 | 21 | 33 | nan | nan | nan | Cerrado | 4.1 |
| d17d3216-cbb5-3950-9b34-e2843c79a0e8 | -7.81074 | -47.00168 | 2025-09-28 05:16:00 | NOAA-21 | CAROLINA | MARANHÃO | Brasil | 2102804 | 21 | 33 | nan | nan | nan | Cerrado | 6.9 |
| 88ea0fed-f485-3dae-9aec-349024e19371 | -2.58147 | -48.40513 | 2025-09-28 05:16:00 | NOAA-21 | TOMÉ-AÇU | PARÁ | Brasil | 1508001 | 15 | 33 | nan | nan | nan | Amazônia | 7.9 |
| 79978d96-d840-3900-a0d7-269a80dafc98 | -7.80153 | -47.02229 | 2025-09-28 05:16:00 | NOAA-21 | CAROLINA | MARANHÃO | Brasil | 2102804 | 21 | 33 | nan | nan | nan | Cerrado | 6.9 |
| 1cfba085-d5d7-3614-bc34-48f6755cc2b2 | -8.16994 | -46.43166 | 2025-09-28 05:16:00 | NOAA-21 | RIACHÃO | MARANHÃO | Brasil | 2109502 | 21 | 33 | nan | nan | nan | Cerrado | 21.1 |
| 87e10881-625e-3b5c-af20-55a8ec5027dd | -7.78396 | -47.003 | 2025-09-28 05:16:00 | NOAA-21 | CAROLINA | MARANHÃO | Brasil | 2102804 | 21 | 33 | nan | nan | nan | Cerrado | 2.5 |
| 522a6a47-07a5-3292-a10b-3ae858abfe0d | -7.80286 | -47.01156 | 2025-09-28 05:16:00 | NOAA-21 | CAROLINA | MARANHÃO | Brasil | 2102804 | 21 | 33 | nan | nan | nan | Cerrado | 3.4 |
| a366f545-c834-360d-80b5-84bc2b56e19c | -3.64812 | -48.32322 | 2025-09-28 05:16:00 | NOAA-21 | PARAGOMINAS | PARÁ | Brasil | 1505502 | 15 | 33 | nan | nan | nan | Amazônia | 4.2 |
| 5d45c74b-c628-3cdd-a569-e8aa75fdb659 | -7.80892 | -47.01909 | 2025-09-28 05:16:00 | NOAA-21 | CAROLINA | MARANHÃO | Brasil | 2102804 | 21 | 33 | nan | nan | nan | Cerrado | 31.3 |
| 7368f468-dd5f-3b23-9276-75c2a5ddd92b | -8.17562 | -46.42746 | 2025-09-28 05:16:00 | NOAA-21 | RIACHÃO | MARANHÃO | Brasil | 2109502 | 21 | 33 | nan | nan | nan | Cerrado | 4.2 |
| 4177b2c1-d835-3256-b6fe-a95fc4214b50 | -7.81688 | -47.00916 | 2025-09-28 05:16:00 | NOAA-21 | CAROLINA | MARANHÃO | Brasil | 2102804 | 21 | 33 | nan | nan | nan | Cerrado | 19.1 |
| bccf1c3c-fa67-337d-b8fa-e1b0d6f68fd9 | -7.81456 | -47.02443 | 2025-09-28 05:16:00 | NOAA-21 | CAROLINA | MARANHÃO | Brasil | 2102804 | 21 | 33 | nan | nan | nan | Cerrado | 20.9 |
| 7f2c2f38-c674-3be4-8bcc-53faf1116fb5 | -7.77489 | -47.02516 | 2025-09-28 05:16:00 | NOAA-21 | CAROLINA | MARANHÃO | Brasil | 2102804 | 21 | 33 | nan | nan | nan | Cerrado | 2.8 |
| 7da70bd0-3c7c-30fa-8746-72dbd1f0bb15 | -7.80873 | -47.01789 | 2025-09-28 05:16:00 | NOAA-21 | CAROLINA | MARANHÃO | Brasil | 2102804 | 21 | 33 | nan | nan | nan | Cerrado | 25.8 |
| 05833c9c-60d1-37b2-b701-ab5bfe9723c9 | -7.79871 | -46.99542 | 2025-09-28 05:16:00 | NOAA-21 | CAROLINA | MARANHÃO | Brasil | 2102804 | 21 | 33 | nan | nan | nan | Cerrado | 2.6 |
| bd579172-4daf-39dc-b483-d7fa1d7a5fd0 | -7.8024 | -47.01811 | 2025-09-28 05:16:00 | NOAA-21 | CAROLINA | MARANHÃO | Brasil | 2102804 | 21 | 33 | nan | nan | nan | Cerrado | 5.8 |
| 57ebb6e6-53fd-309f-bd52-d77e638b9374 | -7.79117 | -46.9985 | 2025-09-28 05:16:00 | NOAA-21 | CAROLINA | MARANHÃO | Brasil | 2102804 | 21 | 33 | nan | nan | nan | Cerrado | 2.5 |
| a4cda714-b0c2-3976-8794-f7dfa19daf04 | -3.79418 | -48.86694 | 2025-09-28 05:16:00 | NOAA-21 | GOIANÉSIA DO PARÁ | PARÁ | Brasil | 1503093 | 15 | 33 | nan | nan | nan | Amazônia | 2.7 |
| 75a571e2-031c-364c-8522-4523e5db6e96 | -13.03162 | -49.45629 | 2025-09-28 05:18:00 | NOAA-21 | ARAGUAÇU | TOCANTINS | Brasil | 1702000 | 17 | 33 | nan | nan | nan | Cerrado | 3.3 |
| a2c7eff3-2efa-340f-bb94-f94c4d2963d8 | -9.8099 | -61.49335 | 2025-09-28 05:18:00 | NOAA-21 | COLNIZA | MATO GROSSO | Brasil | 5103254 | 51 | 33 | nan | nan | nan | Amazônia | 1.8 |
| 4bdd3516-7779-363a-b94f-10363d5bf828 | -11.14564 | -54.30841 | 2025-09-28 05:18:00 | NOAA-21 | MARCELÂNDIA | MATO GROSSO | Brasil | 5105580 | 51 | 33 | nan | nan | nan | Amazônia | 3.9 |
| ce62eb1b-a724-3e4f-b845-770a8307a85a | -11.86649 | -56.87367 | 2025-09-28 05:18:00 | NOAA-21 | PORTO DOS GAÚCHOS | MATO GROSSO | Brasil | 5106802 | 51 | 33 | nan | nan | nan | Amazônia | 1.9 |
| 3776e2c2-05aa-339f-af8f-7457cb733139 | -13.60838 | -48.07903 | 2025-09-28 05:18:00 | NOAA-21 | CAVALCANTE | GOIÁS | Brasil | 5205307 | 52 | 33 | nan | nan | nan | Cerrado | 9.1 |
| 06da9d46-6252-3856-b1df-577fa970ce22 | -9.75977 | -65.0374 | 2025-09-28 05:18:00 | NOAA-21 | PORTO VELHO | RONDÔNIA | Brasil | 1100205 | 11 | 33 | nan | nan | nan | Amazônia | 0.8 |
| d02a069b-5f47-3f1e-bc8e-889df6be871d | -11.09832 | -54.27404 | 2025-09-28 05:18:00 | NOAA-21 | MARCELÂNDIA | MATO GROSSO | Brasil | 5105580 | 51 | 33 | nan | nan | nan | Amazônia | 1.0 |
| eca2c692-fdee-30e3-ba9d-cdb5c82ce467 | -13.60644 | -48.09673 | 2025-09-28 05:18:00 | NOAA-21 | CAVALCANTE | GOIÁS | Brasil | 5205307 | 52 | 33 | nan | nan | nan | Cerrado | 6.4 |
| ed75fd00-dcd2-3ae4-bce4-93e38f54e084 | -9.9251 | -65.00369 | 2025-09-28 05:18:00 | NOAA-21 | PORTO VELHO | RONDÔNIA | Brasil | 1100205 | 11 | 33 | nan | nan | nan | Amazônia | 1.2 |
| 341a7ec1-3422-3ffc-ab04-4ce4e3f9e495 | -10.312 | -54.15495 | 2025-09-28 05:18:00 | NOAA-21 | PEIXOTO DE AZEVEDO | MATO GROSSO | Brasil | 5106422 | 51 | 33 | nan | nan | nan | Amazônia | 0.9 |
| ef8da391-2c30-3855-b5a5-6f5c134faa0a | -11.96761 | -48.00156 | 2025-09-28 05:18:00 | NOAA-21 | SÃO VALÉRIO | TOCANTINS | Brasil | 1720499 | 17 | 33 | nan | nan | nan | Cerrado | 2.2 |
| b6474379-c7cf-3d7b-a6af-f35322c77b39 | -13.58784 | -47.30256 | 2025-09-28 05:18:00 | NOAA-21 | CAVALCANTE | GOIÁS | Brasil | 5205307 | 52 | 33 | nan | nan | nan | Cerrado | 8.5 |
| 45092bec-6ec1-3f37-9f06-fa8280dec305 | -13.74859 | -47.88485 | 2025-09-28 05:18:00 | NOAA-21 | CAVALCANTE | GOIÁS | Brasil | 5205307 | 52 | 33 | nan | nan | nan | Cerrado | 5.5 |
| ddf025d4-ab00-3a6b-b14c-1f3125c4a39e | -13.61156 | -48.10325 | 2025-09-28 05:18:00 | NOAA-21 | CAVALCANTE | GOIÁS | Brasil | 5205307 | 52 | 33 | nan | nan | nan | Cerrado | 3.6 |
| d6eebd12-a83e-3e7c-8680-455f4059d379 | -13.29669 | -50.6893 | 2025-09-28 05:18:00 | NOAA-21 | COCALINHO | MATO GROSSO | Brasil | 5103106 | 51 | 33 | nan | nan | nan | Cerrado | 4.5 |
| 4be58780-657b-3f43-ad1e-6dbd483bc639 | -11.98433 | -47.08512 | 2025-09-28 05:18:00 | NOAA-21 | TAIPAS DO TOCANTINS | TOCANTINS | Brasil | 1720937 | 17 | 33 | nan | nan | nan | Cerrado | 6.4 |
| 95ded27c-fa9d-3f41-a9de-c7bc3304eec0 | -13.01352 | -49.45491 | 2025-09-28 05:18:00 | NOAA-21 | ARAGUAÇU | TOCANTINS | Brasil | 1702000 | 17 | 33 | nan | nan | nan | Cerrado | 5.4 |
| 19b9fc5d-75a1-3384-92c6-42448bec5877 | -12.98162 | -49.44387 | 2025-09-28 05:18:00 | NOAA-21 | ARAGUAÇU | TOCANTINS | Brasil | 1702000 | 17 | 33 | nan | nan | nan | Cerrado | 2.4 |
| aa237511-d94b-32c2-ae2c-fb62551561db | -12.00393 | -47.043 | 2025-09-28 05:18:00 | NOAA-21 | TAIPAS DO TOCANTINS | TOCANTINS | Brasil | 1720937 | 17 | 33 | nan | nan | nan | Cerrado | 8.7 |
| f18594ee-c102-3c06-b3e7-53a55e1313a8 | -13.3944 | -48.16534 | 2025-09-28 05:18:00 | NOAA-21 | MINAÇU | GOIÁS | Brasil | 5213087 | 52 | 33 | nan | nan | nan | Cerrado | 3.3 |
| 24a0b978-7c87-3473-b76e-b22aefcd898b | -12.62971 | -48.15879 | 2025-09-28 05:18:00 | NOAA-21 | PARANÃ | TOCANTINS | Brasil | 1716208 | 17 | 33 | nan | nan | nan | Cerrado | 6.1 |
| e2b3369e-60ce-38d4-b757-19ca460a1ff5 | -10.94913 | -47.78292 | 2025-09-28 05:18:00 | NOAA-21 | SILVANÓPOLIS | TOCANTINS | Brasil | 1720655 | 17 | 33 | nan | nan | nan | Cerrado | 2.7 |
| a014259c-c02a-3910-ae0f-7adc6cd3b924 | -10.28953 | -67.27612 | 2025-09-28 05:18:00 | NOAA-21 | PLÁCIDO DE CASTRO | ACRE | Brasil | 1200385 | 12 | 33 | nan | nan | nan | Amazônia | 5.2 |
| 7a4a080c-464e-35c7-880f-abdb7130bcc7 | -11.94256 | -47.92883 | 2025-09-28 05:18:00 | NOAA-21 | SÃO VALÉRIO | TOCANTINS | Brasil | 1720499 | 17 | 33 | nan | nan | nan | Cerrado | 1.0 |
| ecab52e9-0882-31ac-8276-f449fa0df01d | -7.8611 | -63.3108 | 2025-09-28 05:18:00 | NOAA-21 | HUMAITÁ | AMAZONAS | Brasil | 1301704 | 13 | 33 | nan | nan | nan | Amazônia | 2.0 |
| f3f29eb3-79b1-3610-884a-141f4915b5f1 | -8.67773 | -49.9369 | 2025-09-28 05:18:00 | NOAA-21 | SANTA MARIA DAS BARREIRAS | PARÁ | Brasil | 1506583 | 15 | 33 | nan | nan | nan | Amazônia | 10.6 |
| 2eb4bb8f-a0df-3ed6-899a-392c1c193fd7 | -13.6148 | -48.08121 | 2025-09-28 05:18:00 | NOAA-21 | CAVALCANTE | GOIÁS | Brasil | 5205307 | 52 | 33 | nan | nan | nan | Cerrado | 3.3 |
| f554a00b-71e3-3b7f-85a6-224d7ab4f31a | -13.78715 | -47.8772 | 2025-09-28 05:18:00 | NOAA-21 | CAVALCANTE | GOIÁS | Brasil | 5205307 | 52 | 33 | nan | nan | nan | Cerrado | 3.3 |
| 8ec6c0e1-1d6e-3c45-b4e5-d381adc80d7f | -12.66086 | -51.66383 | 2025-09-28 05:18:00 | NOAA-21 | RIBEIRÃO CASCALHEIRA | MATO GROSSO | Brasil | 5107180 | 51 | 33 | nan | nan | nan | Cerrado | 1.4 |
| 989f69dd-7eb5-3a18-8717-cc3b55407d6c | -9.05686 | -61.65326 | 2025-09-28 05:18:00 | NOAA-21 | MACHADINHO D'OESTE | RONDÔNIA | Brasil | 1100130 | 11 | 33 | nan | nan | nan | Amazônia | 0.6 |
| d87d29d3-34e6-3f3a-bd53-815d53fd067c | -9.99292 | -63.77244 | 2025-09-28 05:18:00 | NOAA-21 | BURITIS | RONDÔNIA | Brasil | 1100452 | 11 | 33 | nan | nan | nan | Amazônia | 0.9 |
| 34281421-5150-3e8c-8b52-410fd07d5d93 | -10.97145 | -49.5694 | 2025-09-28 05:18:00 | NOAA-21 | SANTA RITA DO TOCANTINS | TOCANTINS | Brasil | 1718899 | 17 | 33 | nan | nan | nan | Cerrado | 1.6 |
| 2ea04693-74f4-3421-9093-f0179c19434b | -13.40741 | -48.16733 | 2025-09-28 05:18:00 | NOAA-21 | MINAÇU | GOIÁS | Brasil | 5213087 | 52 | 33 | nan | nan | nan | Cerrado | 1.9 |
| 3fc92b90-1805-3cb3-8ece-08f43cc3c80b | -13.60545 | -48.09809 | 2025-09-28 05:18:00 | NOAA-21 | CAVALCANTE | GOIÁS | Brasil | 5205307 | 52 | 33 | nan | nan | nan | Cerrado | 6.6 |
| d6d39983-9001-3989-a9aa-50f2efe8b933 | -10.51531 | -51.94403 | 2025-09-28 05:18:00 | NOAA-21 | CONFRESA | MATO GROSSO | Brasil | 5103353 | 51 | 33 | nan | nan | nan | Amazônia | 3.3 |
| 870755fe-1a28-38c0-ab29-7f56e849f246 | -8.45113 | -46.91431 | 2025-09-28 05:18:00 | NOAA-21 | CAMPOS LINDOS | TOCANTINS | Brasil | 1703842 | 17 | 33 | nan | nan | nan | Cerrado | 1.5 |
| 8d519008-a057-3630-9c46-8eefd427e27e | -9.41086 | -54.69255 | 2025-09-28 05:18:00 | NOAA-21 | NOVO PROGRESSO | PARÁ | Brasil | 1505031 | 15 | 33 | nan | nan | nan | Amazônia | 1.4 |
| 251e7a83-5153-385e-9496-a1ae2c640098 | -9.64818 | -62.8426 | 2025-09-28 05:18:00 | NOAA-21 | RIO CRESPO | RONDÔNIA | Brasil | 1100262 | 11 | 33 | nan | nan | nan | Amazônia | 38.9 |
| f11817fa-2a45-3e06-943b-1b17e41566f6 | -9.72583 | -64.96849 | 2025-09-28 05:18:00 | NOAA-21 | PORTO VELHO | RONDÔNIA | Brasil | 1100205 | 11 | 33 | nan | nan | nan | Amazônia | 0.6 |
| 662c4d0f-bb76-3e1e-8365-04a2b109acc2 | -9.91599 | -58.56235 | 2025-09-28 05:18:00 | NOAA-21 | COTRIGUAÇU | MATO GROSSO | Brasil | 5103379 | 51 | 33 | nan | nan | nan | Amazônia | 1.0 |
| 6802a556-bddf-3f01-b0b0-843113ab7077 | -12.01082 | -47.96866 | 2025-09-28 05:18:00 | NOAA-21 | SÃO VALÉRIO | TOCANTINS | Brasil | 1720499 | 17 | 33 | nan | nan | nan | Cerrado | 5.6 |
| 48b4a8fe-4d60-3754-a2fb-2a072b71531d | -8.94543 | -65.92665 | 2025-09-28 05:18:00 | NOAA-21 | LÁBREA | AMAZONAS | Brasil | 1302405 | 13 | 33 | nan | nan | nan | Amazônia | 0.9 |
| 21cf8be0-4ec9-3256-8e1a-8101191f9d70 | -9.9608 | -64.7523 | 2025-09-28 05:18:00 | NOAA-21 | PORTO VELHO | RONDÔNIA | Brasil | 1100205 | 11 | 33 | nan | nan | nan | Amazônia | 1.3 |
| 053d619c-6f77-3d01-a7c0-ca8b6c476977 | -10.18263 | -52.57276 | 2025-09-28 05:18:00 | NOAA-21 | SANTA CRUZ DO XINGU | MATO GROSSO | Brasil | 5107743 | 51 | 33 | nan | nan | nan | Amazônia | 1.3 |
| 6989a418-931c-318b-b805-ea29e9dcdaef | -13.01086 | -49.45428 | 2025-09-28 05:18:00 | NOAA-21 | ARAGUAÇU | TOCANTINS | Brasil | 1702000 | 17 | 33 | nan | nan | nan | Cerrado | 7.1 |
| 3cccc97e-d7c0-3ffe-b227-7b4e133b0517 | -12.99438 | -49.43879 | 2025-09-28 05:18:00 | NOAA-21 | ARAGUAÇU | TOCANTINS | Brasil | 1702000 | 17 | 33 | nan | nan | nan | Cerrado | 3.0 |
| 4332597f-cbe8-36d0-bfca-e4edf3803c20 | -13.29608 | -50.68879 | 2025-09-28 05:18:00 | NOAA-21 | COCALINHO | MATO GROSSO | Brasil | 5103106 | 51 | 33 | nan | nan | nan | Cerrado | 3.8 |
| 8c98d06e-4a9a-392c-88b3-cbb73dffb283 | -13.79158 | -48.33239 | 2025-09-28 05:18:00 | NOAA-21 | MINAÇU | GOIÁS | Brasil | 5213087 | 52 | 33 | nan | nan | nan | Cerrado | 4.7 |
| 5329d1f8-c5af-37e6-b911-2099528a3278 | -12.23563 | -60.84393 | 2025-09-28 05:18:00 | NOAA-21 | CHUPINGUAIA | RONDÔNIA | Brasil | 1100924 | 11 | 33 | nan | nan | nan | Amazônia | 2.8 |
| a8233885-35af-38cc-8f59-bf80853ee59e | -11.81512 | -55.1319 | 2025-09-28 05:18:00 | NOAA-21 | SANTA CARMEM | MATO GROSSO | Brasil | 5107248 | 51 | 33 | nan | nan | nan | Amazônia | 4.8 |
| a5f69312-350b-3ad3-812c-81fb0520a66c | -12.00521 | -47.90213 | 2025-09-28 05:18:00 | NOAA-21 | SÃO VALÉRIO | TOCANTINS | Brasil | 1720499 | 17 | 33 | nan | nan | nan | Cerrado | 3.3 |
| efea371b-7580-38e0-bb39-fe5cbe69627d | -10.04621 | -62.45874 | 2025-09-28 05:18:00 | NOAA-21 | THEOBROMA | RONDÔNIA | Brasil | 1101609 | 11 | 33 | nan | nan | nan | Amazônia | 1.3 |
| dada2db0-d81d-3adb-b8a7-71ca26cb8066 | -13.29566 | -50.69258 | 2025-09-28 05:18:00 | NOAA-21 | COCALINHO | MATO GROSSO | Brasil | 5103106 | 51 | 33 | nan | nan | nan | Cerrado | 2.5 |
| 4db057c2-a1e7-3eff-a139-b77d6601a40e | -9.94514 | -55.16273 | 2025-09-28 05:18:00 | NOAA-21 | NOVO MUNDO | MATO GROSSO | Brasil | 5106265 | 51 | 33 | nan | nan | nan | Amazônia | 1.4 |
| 2ad764cb-9df1-365d-b718-b85061cd59d1 | -10.39556 | -64.92249 | 2025-09-28 05:18:00 | NOAA-21 | NOVA MAMORÉ | RONDÔNIA | Brasil | 1100338 | 11 | 33 | nan | nan | nan | Amazônia | 1.0 |
| 139627cd-0257-38cb-8ffe-4eca898da7ba | -12.63683 | -48.15387 | 2025-09-28 05:18:00 | NOAA-21 | PARANÃ | TOCANTINS | Brasil | 1716208 | 17 | 33 | nan | nan | nan | Cerrado | 6.1 |
| fdee177f-a1cc-37cb-abba-dd06f60e1bb6 | -9.74311 | -62.3576 | 2025-09-28 05:18:00 | NOAA-21 | MACHADINHO D'OESTE | RONDÔNIA | Brasil | 1100130 | 11 | 33 | nan | nan | nan | Amazônia | 1.7 |
| f3583eaa-9dc1-3ea4-9a2f-dbf57d67cf03 | -13.02201 | -49.46303 | 2025-09-28 05:18:00 | NOAA-21 | ARAGUAÇU | TOCANTINS | Brasil | 1702000 | 17 | 33 | nan | nan | nan | Cerrado | 6.1 |


[Clique aqui para ver as próximas entradas](README85.md)
