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

## Dados Diários - Página 38

| ID | Latitude | Longitude | Data/Hora GMT | Satélite | Município | Estado | País | Município ID | Estado ID | País ID | Dias sem Chuva | Precipitação | Risco de Fogo | Bioma | FRP |
|----|----------|-----------|---------------|----------|-----------|--------|------|--------------|-----------|---------|----------------|--------------|----------------|-------|-----|
| e72484ab-1382-36bf-b828-d4ebae8df195 | -6.64292 | -59.44059 | 2026-09-03 04:57:00 | NOAA-20 | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 7.4 |
| 49af8704-9886-3a93-8ec5-d4454ff44aa4 | -10.88196 | -45.3045 | 2026-09-03 04:57:00 | NOAA-20 | FORMOSA DO RIO PRETO | BAHIA | Brasil | 2911105 | 29 | 33 | nan | nan | nan | Cerrado | 13.3 |
| 92a993a5-7f6c-32e9-8293-468cfec16bdf | -7.50374 | -60.77699 | 2026-09-03 04:57:00 | NOAA-20 | NOVO ARIPUANÃ | AMAZONAS | Brasil | 1303304 | 13 | 33 | nan | nan | nan | Amazônia | 1.3 |
| 948b49c1-e6b5-3305-8989-29e44f1e01d5 | -6.62743 | -55.23896 | 2026-09-03 04:57:00 | NOAA-20 | ITAITUBA | PARÁ | Brasil | 1503606 | 15 | 33 | nan | nan | nan | Amazônia | 0.5 |
| f4120e71-a949-3d37-863c-34205c8e376a | -6.32747 | -43.81837 | 2026-09-03 04:57:00 | NOAA-20 | SÃO JOÃO DOS PATOS | MARANHÃO | Brasil | 2111102 | 21 | 33 | nan | nan | nan | Cerrado | 1.5 |
| 8abd181f-4768-317e-bfdf-6c3f7dbc184e | -8.26381 | -54.94351 | 2026-09-03 04:57:00 | NOAA-20 | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 1.8 |
| cc6896ac-2a53-3d1e-bc44-1720c161c4ba | -8.42344 | -54.71458 | 2026-09-03 04:57:00 | NOAA-20 | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 2.4 |
| 342f2be3-1b64-3b13-a0df-b3a154f50a80 | -7.32355 | -55.13647 | 2026-09-03 04:57:00 | NOAA-20 | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 1.9 |
| 569d65fd-7f25-3043-aaf8-17a24e091cde | -6.75862 | -44.57277 | 2026-09-03 04:57:00 | NOAA-20 | SÃO DOMINGOS DO AZEITÃO | MARANHÃO | Brasil | 2110658 | 21 | 33 | nan | nan | nan | Cerrado | 2.3 |
| 0689b08c-c45e-33b4-b85e-201328c89e24 | -9.14972 | -49.97844 | 2026-09-03 04:57:00 | NOAA-20 | SANTANA DO ARAGUAIA | PARÁ | Brasil | 1506708 | 15 | 33 | nan | nan | nan | Amazônia | 2.8 |
| 475a51fc-80a7-33bc-9948-f72742ee5f14 | -7.35625 | -60.60772 | 2026-09-03 04:57:00 | NOAA-20 | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 1.5 |
| e7ab90ff-253e-35a8-9aa5-3739d2ed3933 | -10.99593 | -45.08984 | 2026-09-03 04:57:00 | NOAA-20 | FORMOSA DO RIO PRETO | BAHIA | Brasil | 2911105 | 29 | 33 | nan | nan | nan | Cerrado | 18.6 |
| 0babada0-be1a-3a07-8cd1-10e1e882d8f0 | -7.19332 | -60.6672 | 2026-09-03 04:57:00 | NOAA-20 | NOVO ARIPUANÃ | AMAZONAS | Brasil | 1303304 | 13 | 33 | nan | nan | nan | Amazônia | 1.4 |
| a4839d12-7726-360d-b95f-41bb3a707f1c | -6.62681 | -55.24283 | 2026-09-03 04:57:00 | NOAA-20 | ITAITUBA | PARÁ | Brasil | 1503606 | 15 | 33 | nan | nan | nan | Amazônia | 1.3 |
| ad4c54dd-708f-30d7-b775-d2ee547a560b | -3.61941 | -60.5711 | 2026-09-03 04:57:00 | NOAA-20 | MANAQUIRI | AMAZONAS | Brasil | 1302553 | 13 | 33 | nan | nan | nan | Amazônia | 1.3 |
| 6cd2eea1-f66b-3bf6-9823-97b5cb74f2d9 | -10.89443 | -45.32799 | 2026-09-03 04:57:00 | NOAA-20 | FORMOSA DO RIO PRETO | BAHIA | Brasil | 2911105 | 29 | 33 | nan | nan | nan | Cerrado | 1.1 |
| f2e0705b-53b6-3a6e-8c93-4449ae656e62 | -4.24127 | -62.24272 | 2026-09-03 04:57:00 | NOAA-20 | ANORI | AMAZONAS | Brasil | 1300102 | 13 | 33 | nan | nan | nan | Amazônia | 1.1 |
| 0d0b1fd2-75d3-3386-87e4-fc8ec020a8f7 | -11.28973 | -45.17402 | 2026-09-03 04:57:00 | NOAA-20 | FORMOSA DO RIO PRETO | BAHIA | Brasil | 2911105 | 29 | 33 | nan | nan | nan | Cerrado | 3.0 |
| a3f9f5d1-1d3c-3b50-8c7c-bdd67c4b401f | -6.76921 | -59.44227 | 2026-09-03 04:57:00 | NOAA-20 | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 1.7 |
| a1836878-2a86-3b96-9731-3130b2e1acdd | -6.25238 | -55.4318 | 2026-09-03 04:57:00 | NOAA-20 | ITAITUBA | PARÁ | Brasil | 1503606 | 15 | 33 | nan | nan | nan | Amazônia | 1.9 |
| ba58653b-c29d-3c52-915c-6e896741c292 | -11.32243 | -50.53429 | 2026-09-03 04:57:00 | NOAA-20 | LAGOA DA CONFUSÃO | TOCANTINS | Brasil | 1711902 | 17 | 33 | nan | nan | nan | Cerrado | 20.0 |
| 0b44aeeb-6cbf-31c5-aec0-5e59c8fd7090 | -10.57397 | -47.71335 | 2026-09-03 04:57:00 | NOAA-20 | PONTE ALTA DO TOCANTINS | TOCANTINS | Brasil | 1717909 | 17 | 33 | nan | nan | nan | Cerrado | 1.1 |
| 0fd038cd-ae49-3051-af49-2347399271ec | -6.63439 | -55.24012 | 2026-09-03 04:57:00 | NOAA-20 | ITAITUBA | PARÁ | Brasil | 1503606 | 15 | 33 | nan | nan | nan | Amazônia | 0.7 |
| 7ff99841-0089-3cd5-83fc-9df727295a3a | -5.58816 | -60.19838 | 2026-09-03 04:57:00 | NOAA-20 | NOVO ARIPUANÃ | AMAZONAS | Brasil | 1303304 | 13 | 33 | nan | nan | nan | Amazônia | 2.5 |
| a82f157b-eaff-3cf0-ae37-296679968462 | -11.317 | -50.5202 | 2026-09-03 04:57:00 | NOAA-20 | LAGOA DA CONFUSÃO | TOCANTINS | Brasil | 1711902 | 17 | 33 | nan | nan | nan | Cerrado | 12.4 |
| 4abe90f2-c023-345e-8cc8-4022240ca997 | -11.29907 | -45.14191 | 2026-09-03 04:57:00 | NOAA-20 | FORMOSA DO RIO PRETO | BAHIA | Brasil | 2911105 | 29 | 33 | nan | nan | nan | Cerrado | 1.5 |
| f41f3b64-b2d6-31a5-81f1-788383f4c2d9 | -8.42695 | -54.69282 | 2026-09-03 04:57:00 | NOAA-20 | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 1.4 |
| 0ecbaf8a-e34f-3917-bdb5-67ad999ffe29 | -10.99675 | -45.08349 | 2026-09-03 04:57:00 | NOAA-20 | FORMOSA DO RIO PRETO | BAHIA | Brasil | 2911105 | 29 | 33 | nan | nan | nan | Cerrado | 10.2 |
| 9b132394-29a1-3118-bc4e-290d3891d943 | -5.26532 | -60.18761 | 2026-09-03 04:57:00 | NOAA-20 | NOVO ARIPUANÃ | AMAZONAS | Brasil | 1303304 | 13 | 33 | nan | nan | nan | Amazônia | 1.8 |
| 34062301-4931-33f4-8d65-dbb9ed961b57 | -11.32734 | -50.52619 | 2026-09-03 04:57:00 | NOAA-20 | LAGOA DA CONFUSÃO | TOCANTINS | Brasil | 1711902 | 17 | 33 | nan | nan | nan | Cerrado | 11.8 |
| 829bfb9f-44f4-3f16-ade7-aaf285293d33 | -11.33578 | -50.54514 | 2026-09-03 04:57:00 | NOAA-20 | LAGOA DA CONFUSÃO | TOCANTINS | Brasil | 1711902 | 17 | 33 | nan | nan | nan | Cerrado | 23.9 |
| 5cf22bd5-fcc5-33fc-9db8-00ebafec8081 | -8.95988 | -49.51394 | 2026-09-03 04:57:00 | NOAA-20 | ARAGUACEMA | TOCANTINS | Brasil | 1701903 | 17 | 33 | nan | nan | nan | Cerrado | 1.6 |
| 39783519-8ef2-37f9-b5ab-7fbccd825e65 | -6.21783 | -55.42203 | 2026-09-03 04:57:00 | NOAA-20 | ITAITUBA | PARÁ | Brasil | 1503606 | 15 | 33 | nan | nan | nan | Amazônia | 1.3 |
| 1cbef6bc-59a9-31e5-b2af-bb283aee6b2e | -5.20229 | -60.04173 | 2026-09-03 04:57:00 | NOAA-20 | NOVO ARIPUANÃ | AMAZONAS | Brasil | 1303304 | 13 | 33 | nan | nan | nan | Amazônia | 4.3 |
| bef229eb-d71c-3a00-ac84-1c4bc678de2f | -6.36393 | -55.23665 | 2026-09-03 04:57:00 | NOAA-20 | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 1.2 |
| 59c10e93-25a4-3cc9-b598-f6eb4515406d | -3.20609 | -61.23267 | 2026-09-03 04:57:00 | NOAA-20 | MANACAPURU | AMAZONAS | Brasil | 1302504 | 13 | 33 | nan | nan | nan | Amazônia | 1.4 |
| 3a12679d-e82f-34da-b28b-4cd720d6d753 | -4.14787 | -60.69662 | 2026-09-03 04:57:00 | NOAA-20 | CAREIRO | AMAZONAS | Brasil | 1301100 | 13 | 33 | nan | nan | nan | Amazônia | 1.4 |
| 6748446c-b9c4-3ef9-b107-ace888552715 | -8.78325 | -54.59227 | 2026-09-03 04:57:00 | NOAA-20 | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 1.1 |
| 731ad9ef-1720-36db-b4c5-31f674dd2c4d | -8.46423 | -54.65451 | 2026-09-03 04:57:00 | NOAA-20 | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 1.0 |
| 0b163b0f-8c04-3aa6-b17b-7a49ee8b7c9b | -10.87054 | -45.31252 | 2026-09-03 04:57:00 | NOAA-20 | FORMOSA DO RIO PRETO | BAHIA | Brasil | 2911105 | 29 | 33 | nan | nan | nan | Cerrado | 0.4 |
| 407879d1-6b7d-3293-a669-e92a4ed0c1f7 | -8.46028 | -54.65757 | 2026-09-03 04:57:00 | NOAA-20 | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 1.3 |
| fce5c82f-6af9-3de4-a9ab-28a4b1cd4208 | -5.7601 | -53.39652 | 2026-09-03 04:57:00 | NOAA-20 | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 1.0 |
| 83645115-06fc-3d6d-8dbe-11195d04e103 | -5.51084 | -60.19019 | 2026-09-03 04:57:00 | NOAA-20 | NOVO ARIPUANÃ | AMAZONAS | Brasil | 1303304 | 13 | 33 | nan | nan | nan | Amazônia | 4.4 |
| 1cbcad30-8581-39d9-bddb-dacb7f2ab287 | -8.07412 | -50.96989 | 2026-09-03 04:57:00 | NOAA-20 | CUMARU DO NORTE | PARÁ | Brasil | 1502764 | 15 | 33 | nan | nan | nan | Amazônia | 0.7 |
| 9e1e1263-b579-3f0e-887f-309d0e6fb7e5 | -3.61891 | -60.57406 | 2026-09-03 04:57:00 | NOAA-20 | MANAQUIRI | AMAZONAS | Brasil | 1302553 | 13 | 33 | nan | nan | nan | Amazônia | 2.1 |
| d329cdbe-7eee-32c1-8c78-10876352b810 | -6.78181 | -59.42198 | 2026-09-03 04:57:00 | NOAA-20 | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 0.5 |
| 366755b5-184d-3ba6-8388-e314ec9aad36 | -7.41087 | -49.7434 | 2026-09-03 04:57:00 | NOAA-20 | FLORESTA DO ARAGUAIA | PARÁ | Brasil | 1503044 | 15 | 33 | nan | nan | nan | Amazônia | 2.0 |
| 4ba7ad99-0895-362a-94bf-3d2f37bb6dfc | -4.23631 | -62.23798 | 2026-09-03 04:57:00 | NOAA-20 | ANORI | AMAZONAS | Brasil | 1300102 | 13 | 33 | nan | nan | nan | Amazônia | 1.2 |
| 97f71f73-38af-3429-8731-becd281c2e07 | -6.84483 | -59.34158 | 2026-09-03 04:57:00 | NOAA-20 | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 1.5 |
| 40b4867e-11af-3488-8762-6eacc43c0c00 | -6.30378 | -56.04121 | 2026-09-03 04:57:00 | NOAA-20 | ITAITUBA | PARÁ | Brasil | 1503606 | 15 | 33 | nan | nan | nan | Amazônia | 3.5 |
| 454455bb-2ba4-3662-bb29-865e5368e4ea | -8.70488 | -52.36597 | 2026-09-03 04:57:00 | NOAA-20 | SÃO FÉLIX DO XINGU | PARÁ | Brasil | 1507300 | 15 | 33 | nan | nan | nan | Amazônia | 1.5 |
| c43e5d0a-3cb7-3a7b-9888-8f8c601063af | -5.10248 | -49.60427 | 2026-09-03 04:57:00 | NOAA-20 | ITUPIRANGA | PARÁ | Brasil | 1503705 | 15 | 33 | nan | nan | nan | Amazônia | 0.9 |
| bd099f2e-7670-39f0-9127-fe04e64e4792 | -3.61435 | -60.57024 | 2026-09-03 04:57:00 | NOAA-20 | MANAQUIRI | AMAZONAS | Brasil | 1302553 | 13 | 33 | nan | nan | nan | Amazônia | 6.8 |
| 4a4d654a-134c-37cd-a2a9-6cff9a736208 | -5.25572 | -60.18596 | 2026-09-03 04:57:00 | NOAA-20 | NOVO ARIPUANÃ | AMAZONAS | Brasil | 1303304 | 13 | 33 | nan | nan | nan | Amazônia | 3.7 |
| eb7f49cf-f5ff-3a0f-9ec5-e5dfe48f2082 | -10.49136 | -48.64899 | 2026-09-03 04:57:00 | NOAA-20 | PORTO NACIONAL | TOCANTINS | Brasil | 1718204 | 17 | 33 | nan | nan | nan | Cerrado | 3.8 |
| b68212fb-3c6a-376e-8fde-bf76e2a684f3 | -10.87446 | -45.32221 | 2026-09-03 04:57:00 | NOAA-20 | FORMOSA DO RIO PRETO | BAHIA | Brasil | 2911105 | 29 | 33 | nan | nan | nan | Cerrado | 3.0 |
| b7e6940f-d8eb-3744-a536-ba3582650f77 | -8.44297 | -54.74377 | 2026-09-03 04:57:00 | NOAA-20 | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 3.0 |
| 3932eca2-1e6a-34e3-a05c-7e69e5794bde | -6.31672 | -54.75051 | 2026-09-03 04:57:00 | NOAA-20 | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 1.2 |
| 9e36ce96-742d-38b4-90eb-fb81ead54846 | -10.99075 | -45.0891 | 2026-09-03 04:57:00 | NOAA-20 | FORMOSA DO RIO PRETO | BAHIA | Brasil | 2911105 | 29 | 33 | nan | nan | nan | Cerrado | 18.6 |
| fbddbf5e-86d0-3eaa-a20a-f45ea50f1966 | -9.07388 | -65.72172 | 2026-09-03 04:57:00 | NOAA-20 | LÁBREA | AMAZONAS | Brasil | 1302405 | 13 | 33 | nan | nan | nan | Amazônia | 4.4 |
| 81f5c89d-6f52-38cf-bc6f-1a44e8703828 | -9.60595 | -48.56389 | 2026-09-03 04:57:00 | NOAA-20 | MIRACEMA DO TOCANTINS | TOCANTINS | Brasil | 1713205 | 17 | 33 | nan | nan | nan | Cerrado | 3.4 |
| e2ba6d12-8cd0-3ec2-a68e-ec0e8e870439 | -5.97147 | -53.58386 | 2026-09-03 04:57:00 | NOAA-20 | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 0.9 |
| 5de59e53-b85a-3f3e-80f6-16731c07c42f | -9.73557 | -58.40172 | 2026-09-03 04:57:00 | NOAA-20 | COTRIGUAÇU | MATO GROSSO | Brasil | 5103379 | 51 | 33 | nan | nan | nan | Amazônia | 1.8 |
| 2293b432-75de-30fd-833e-774e92bef66e | -11.29747 | -50.52611 | 2026-09-03 04:57:00 | NOAA-20 | LAGOA DA CONFUSÃO | TOCANTINS | Brasil | 1711902 | 17 | 33 | nan | nan | nan | Cerrado | 4.4 |
| f3299709-b5c7-3359-9b7f-76542f68eea9 | -10.98995 | -45.09538 | 2026-09-03 04:57:00 | NOAA-20 | FORMOSA DO RIO PRETO | BAHIA | Brasil | 2911105 | 29 | 33 | nan | nan | nan | Cerrado | 5.1 |
| 49a3a57d-8e2d-3d04-9374-90677c615484 | -7.33993 | -55.20932 | 2026-09-03 04:57:00 | NOAA-20 | NOVO PROGRESSO | PARÁ | Brasil | 1505031 | 15 | 33 | nan | nan | nan | Amazônia | 1.0 |
| ed5060a6-9d11-3036-b6c3-0e59064d3b8d | -5.97639 | -55.70324 | 2026-09-03 04:57:00 | NOAA-20 | ITAITUBA | PARÁ | Brasil | 1503606 | 15 | 33 | nan | nan | nan | Amazônia | 1.5 |
| 951b6945-4f45-3868-8d9f-509107fbb393 | -7.53303 | -60.7226 | 2026-09-03 04:57:00 | NOAA-20 | NOVO ARIPUANÃ | AMAZONAS | Brasil | 1303304 | 13 | 33 | nan | nan | nan | Amazônia | 3.2 |
| 56598ea5-a96e-3884-8e01-660e522bb045 | -7.61186 | -57.6173 | 2026-09-03 04:57:00 | NOAA-20 | JACAREACANGA | PARÁ | Brasil | 1503754 | 15 | 33 | nan | nan | nan | Amazônia | 1.5 |
| 0aabaa34-7fde-3bed-9f38-2c18065218e6 | -10.56421 | -47.72031 | 2026-09-03 04:57:00 | NOAA-20 | PONTE ALTA DO TOCANTINS | TOCANTINS | Brasil | 1717909 | 17 | 33 | nan | nan | nan | Cerrado | 2.8 |
| 554e0f87-0c7c-3da2-83f5-aebe01f01091 | -3.14907 | -60.64597 | 2026-09-03 04:57:00 | NOAA-20 | MANACAPURU | AMAZONAS | Brasil | 1302504 | 13 | 33 | nan | nan | nan | Amazônia | 1.6 |
| 71a5ada0-ba8d-38ec-8ddd-c04b4a6e5e00 | -5.26052 | -60.18677 | 2026-09-03 04:57:00 | NOAA-20 | NOVO ARIPUANÃ | AMAZONAS | Brasil | 1303304 | 13 | 33 | nan | nan | nan | Amazônia | 3.7 |
| 0aa59469-b769-311f-854b-f3a766de1f0a | -9.08926 | -65.37107 | 2026-09-03 04:57:00 | NOAA-20 | LÁBREA | AMAZONAS | Brasil | 1302405 | 13 | 33 | nan | nan | nan | Amazônia | 1.4 |
| d2b4d47e-0e8e-3b64-bb81-ca0fe2d11dd5 | -6.75954 | -59.44525 | 2026-09-03 04:57:00 | NOAA-20 | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 1.9 |
| ffc3dd30-2997-3df8-8a75-3ce6a9c278bf | -10.75875 | -48.97546 | 2026-09-03 04:57:00 | NOAA-20 | CRISTALÂNDIA | TOCANTINS | Brasil | 1706100 | 17 | 33 | nan | nan | nan | Cerrado | 4.1 |
| 475e5dd4-c279-35ac-9a50-f358ba43f9a0 | -5.32788 | -60.13947 | 2026-09-03 04:57:00 | NOAA-20 | NOVO ARIPUANÃ | AMAZONAS | Brasil | 1303304 | 13 | 33 | nan | nan | nan | Amazônia | 5.3 |
| 145a6838-21cf-30ac-ab4b-ba02bb0b1895 | -5.25667 | -60.18449 | 2026-09-03 04:57:00 | NOAA-20 | NOVO ARIPUANÃ | AMAZONAS | Brasil | 1303304 | 13 | 33 | nan | nan | nan | Amazônia | 4.3 |
| ee0ae68a-53eb-3662-b4d4-319aced607cd | -10.41702 | -57.22899 | 2026-09-03 04:57:00 | NOAA-20 | JUARA | MATO GROSSO | Brasil | 5105101 | 51 | 33 | nan | nan | nan | Amazônia | 1.7 |
| f7f047dd-6b1c-3668-9842-3fead58ebdd7 | -5.56301 | -60.17269 | 2026-09-03 04:57:00 | NOAA-20 | NOVO ARIPUANÃ | AMAZONAS | Brasil | 1303304 | 13 | 33 | nan | nan | nan | Amazônia | 1.5 |
| aa50b829-5d6d-30d6-ad23-af9f0fee757a | -5.58338 | -60.19756 | 2026-09-03 04:57:00 | NOAA-20 | NOVO ARIPUANÃ | AMAZONAS | Brasil | 1303304 | 13 | 33 | nan | nan | nan | Amazônia | 1.1 |
| f68a2c9a-411d-381b-b538-cb5f407f1ca9 | -7.05077 | -59.22392 | 2026-09-03 04:57:00 | NOAA-20 | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 1.0 |
| 1fd0876c-9fa7-3bfc-9763-c654ee1448e7 | -10.89995 | -45.32553 | 2026-09-03 04:57:00 | NOAA-20 | FORMOSA DO RIO PRETO | BAHIA | Brasil | 2911105 | 29 | 33 | nan | nan | nan | Cerrado | 1.6 |
| 01a82783-37c8-3d4c-90d2-c137b1000288 | -3.39461 | -59.3668 | 2026-09-03 04:57:00 | NOAA-20 | CAREIRO DA VÁRZEA | AMAZONAS | Brasil | 1301159 | 13 | 33 | nan | nan | nan | Amazônia | 1.2 |
| a8df31ca-4d6c-3b79-ac1d-ede2d4603d36 | -8.43823 | -54.68722 | 2026-09-03 04:57:00 | NOAA-20 | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 10.1 |
| e247ecaa-f6c0-3854-a76e-d5c3309f3caf | -6.32189 | -56.04424 | 2026-09-03 04:57:00 | NOAA-20 | ITAITUBA | PARÁ | Brasil | 1503606 | 15 | 33 | nan | nan | nan | Amazônia | 1.1 |
| e89f3992-4d92-360f-a458-b560edc65fbf | -6.62395 | -55.23838 | 2026-09-03 04:57:00 | NOAA-20 | ITAITUBA | PARÁ | Brasil | 1503606 | 15 | 33 | nan | nan | nan | Amazônia | 1.1 |
| 949606dd-794e-36d8-8c44-e7ffdeae3636 | -8.42681 | -54.71513 | 2026-09-03 04:57:00 | NOAA-20 | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 2.4 |
| 219b80d2-92f1-31b3-94bc-f7c72cd19419 | -6.68202 | -59.95311 | 2026-09-03 04:57:00 | NOAA-20 | NOVO ARIPUANÃ | AMAZONAS | Brasil | 1303304 | 13 | 33 | nan | nan | nan | Amazônia | 9.0 |
| cdea5d66-d4c8-3b9b-8afe-c562d702bf6f | -6.14796 | -55.66985 | 2026-09-03 04:57:00 | NOAA-20 | ITAITUBA | PARÁ | Brasil | 1503606 | 15 | 33 | nan | nan | nan | Amazônia | 1.0 |
| ad7ae492-8f83-36db-9100-ee5110d3dda5 | -8.70932 | -52.35945 | 2026-09-03 04:57:00 | NOAA-20 | SÃO FÉLIX DO XINGU | PARÁ | Brasil | 1507300 | 15 | 33 | nan | nan | nan | Amazônia | 2.3 |
| 6d87c325-2862-3e5d-86e5-84e0aa56fefd | -6.76476 | -59.44153 | 2026-09-03 04:57:00 | NOAA-20 | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 1.9 |
| 93e03b98-72ed-3c53-ae8c-74f2a97b2ae0 | -6.10989 | -59.96724 | 2026-09-03 04:57:00 | NOAA-20 | NOVO ARIPUANÃ | AMAZONAS | Brasil | 1303304 | 13 | 33 | nan | nan | nan | Amazônia | 1.1 |
| 73af4a0b-e908-3353-8c35-f48897a076cd | -11.00194 | -45.08414 | 2026-09-03 04:57:00 | NOAA-20 | FORMOSA DO RIO PRETO | BAHIA | Brasil | 2911105 | 29 | 33 | nan | nan | nan | Cerrado | 2.6 |
| 3997f92e-09ac-330d-a251-a553d92cb78e | -10.48555 | -51.33109 | 2026-09-03 04:57:00 | NOAA-20 | CONFRESA | MATO GROSSO | Brasil | 5103353 | 51 | 33 | nan | nan | nan | Amazônia | 1.9 |
| bde80c8c-e2b8-3b91-bb71-bffda286ee78 | -4.94363 | -47.6554 | 2026-09-03 04:57:00 | NOAA-20 | AÇAILÂNDIA | MARANHÃO | Brasil | 2100055 | 21 | 33 | nan | nan | nan | Amazônia | 1.7 |
| 3f502a5a-093e-372e-a37b-7e0ee67c7476 | -8.79271 | -47.98673 | 2026-09-03 04:57:00 | NOAA-20 | SANTA MARIA DO TOCANTINS | TOCANTINS | Brasil | 1718881 | 17 | 33 | nan | nan | nan | Cerrado | 1.6 |
| 16c70b4f-58c9-317e-956e-f3a810128baa | -10.92848 | -45.34472 | 2026-09-03 04:57:00 | NOAA-20 | FORMOSA DO RIO PRETO | BAHIA | Brasil | 2911105 | 29 | 33 | nan | nan | nan | Cerrado | 0.6 |
| 9c2747de-7cd7-3ab2-a9a6-ea85970ca20e | -7.33608 | -55.1463 | 2026-09-03 04:57:00 | NOAA-20 | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 1.0 |
| 626dced0-f65d-30ef-ba6c-e043f16eb506 | -10.18461 | -50.27587 | 2026-09-03 04:57:00 | NOAA-20 | PIUM | TOCANTINS | Brasil | 1717503 | 17 | 33 | nan | nan | nan | Cerrado | 3.2 |
| 3a096458-a2d1-3307-96ad-6252c72580f1 | -8.43959 | -54.74321 | 2026-09-03 04:57:00 | NOAA-20 | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 3.0 |


[Clique aqui para ver as próximas entradas](README39.md)
