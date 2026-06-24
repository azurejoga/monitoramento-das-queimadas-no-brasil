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
| c233ecc0-dd4c-3f27-973f-dd7817d44f35 | -12.8349 | -44.3892 | 2026-06-24 04:50:00 | GOES-19 | BAIANÓPOLIS | BAHIA | Brasil | 2902500 | 29 | 33 | nan | nan | nan | Cerrado | 48.7 |
| 5a2d9dcc-7c3e-3eff-a98c-b225279ef0a0 | -12.8552 | -44.3389 | 2026-06-24 04:50:00 | GOES-19 | BAIANÓPOLIS | BAHIA | Brasil | 2902500 | 29 | 33 | nan | nan | nan | Cerrado | 132.6 |
| 82fa3f8c-489d-3e0a-b3b6-2b2c072bfd47 | -12.8548 | -44.3625 | 2026-06-24 04:50:00 | GOES-19 | BAIANÓPOLIS | BAHIA | Brasil | 2902500 | 29 | 33 | nan | nan | nan | Cerrado | 248.3 |
| 242e47c5-4860-31f6-9d62-26a8b4c8534f | -12.8359 | -44.3422 | 2026-06-24 04:50:00 | GOES-19 | BAIANÓPOLIS | BAHIA | Brasil | 2902500 | 29 | 33 | nan | nan | nan | Cerrado | 202.3 |
| 4408795f-ba67-380d-aa1b-8b4fb2b1ecf1 | -12.8354 | -44.3657 | 2026-06-24 04:50:00 | GOES-19 | BAIANÓPOLIS | BAHIA | Brasil | 2902500 | 29 | 33 | nan | nan | nan | Cerrado | 345.9 |
| 8718b2c6-e4cf-3b3e-92d0-5deb8d894d82 | -12.8543 | -44.386 | 2026-06-24 04:50:00 | GOES-19 | BAIANÓPOLIS | BAHIA | Brasil | 2902500 | 29 | 33 | nan | nan | nan | Cerrado | 40.1 |
| c05d32e1-b822-3f37-9ce4-26bd85323c79 | -13.0635 | -53.3546 | 2026-06-24 04:50:00 | GOES-19 | GAÚCHA DO NORTE | MATO GROSSO | Brasil | 5103858 | 51 | 33 | nan | nan | nan | Amazônia | 68.3 |
| d1b8d255-c432-380e-9d32-115343552613 | -12.8548 | -44.3625 | 2026-06-24 05:00:00 | GOES-19 | BAIANÓPOLIS | BAHIA | Brasil | 2902500 | 29 | 33 | nan | nan | nan | Cerrado | 234.5 |
| 21dd57f1-deed-3c24-82c8-dac1622160c2 | -12.8552 | -44.3389 | 2026-06-24 05:00:00 | GOES-19 | BAIANÓPOLIS | BAHIA | Brasil | 2902500 | 29 | 33 | nan | nan | nan | Cerrado | 144.7 |
| 34a6f76e-c3f2-368e-b2e4-96c291ab77b1 | -12.8359 | -44.3422 | 2026-06-24 05:00:00 | GOES-19 | BAIANÓPOLIS | BAHIA | Brasil | 2902500 | 29 | 33 | nan | nan | nan | Cerrado | 220.9 |
| 0e1ea6db-4c10-361e-8e4a-c6703e375517 | -6.3703 | -43.5898 | 2026-06-24 05:00:00 | GOES-19 | SUCUPIRA DO RIACHÃO | MARANHÃO | Brasil | 2111953 | 21 | 33 | nan | nan | nan | Cerrado | 83.8 |
| 05f8cce3-f80e-3588-9f75-50a83c5d5e24 | -12.8349 | -44.3892 | 2026-06-24 05:00:00 | GOES-19 | BAIANÓPOLIS | BAHIA | Brasil | 2902500 | 29 | 33 | nan | nan | nan | Cerrado | 39.1 |
| 950e1f0b-dbd6-3e69-bdbd-e6c7133dc558 | -12.8354 | -44.3657 | 2026-06-24 05:00:00 | GOES-19 | BAIANÓPOLIS | BAHIA | Brasil | 2902500 | 29 | 33 | nan | nan | nan | Cerrado | 342.8 |
| 0c5c720f-4f16-3119-8d68-211f826da8ee | -3.87008 | -42.96161 | 2026-06-24 05:08:00 | NPP-375D | BURITI | MARANHÃO | Brasil | 2102200 | 21 | 33 | nan | nan | nan | Cerrado | 1.3 |
| 576c4499-034a-3775-a6d3-7e9af325c8f4 | -3.87611 | -42.96252 | 2026-06-24 05:08:00 | NPP-375D | BURITI | MARANHÃO | Brasil | 2102200 | 21 | 33 | nan | nan | nan | Cerrado | 1.0 |
| aa6ef2df-f521-39f6-869e-da107a049bb1 | -7.37441 | -42.80431 | 2026-06-24 05:08:00 | NPP-375D | SÃO JOSÉ DO PEIXE | PIAUÍ | Brasil | 2210102 | 22 | 33 | nan | nan | nan | Caatinga | 2.3 |
| 542477e6-0ff2-3a63-ba86-00d6a2393394 | -3.95973 | -43.1162 | 2026-06-24 05:08:00 | NPP-375D | BURITI | MARANHÃO | Brasil | 2102200 | 21 | 33 | nan | nan | nan | Cerrado | 0.9 |
| e7c2a809-6af9-3496-9104-f854e5bb88b9 | -6.84539 | -47.86547 | 2026-06-24 05:08:00 | NPP-375D | DARCINÓPOLIS | TOCANTINS | Brasil | 1706506 | 17 | 33 | nan | nan | nan | Cerrado | 1.9 |
| 35ee437e-a2c0-3cdc-82ce-c4c3ed6803d6 | -7.29081 | -46.25249 | 2026-06-24 05:08:00 | NPP-375D | NOVA COLINAS | MARANHÃO | Brasil | 2107258 | 21 | 33 | nan | nan | nan | Cerrado | 1.2 |
| 7ed75cea-4fee-3d7c-8c2a-4f06ef0e5e92 | -3.87395 | -42.96462 | 2026-06-24 05:08:00 | NPP-375D | BURITI | MARANHÃO | Brasil | 2102200 | 21 | 33 | nan | nan | nan | Cerrado | 1.1 |
| f829d77e-70f8-375c-ba24-b465c8072e6d | -8.33498 | -50.49367 | 2026-06-24 05:08:00 | NPP-375D | SANTA MARIA DAS BARREIRAS | PARÁ | Brasil | 1506583 | 15 | 33 | nan | nan | nan | Amazônia | 1.1 |
| 07292a47-c674-3fe3-9e7f-a6b362a98da8 | -8.33541 | -50.49641 | 2026-06-24 05:08:00 | NPP-375D | SANTA MARIA DAS BARREIRAS | PARÁ | Brasil | 1506583 | 15 | 33 | nan | nan | nan | Amazônia | 0.9 |
| c26f0a60-8119-3be1-9b28-d6f277d63fe3 | -7.29208 | -46.24351 | 2026-06-24 05:08:00 | NPP-375D | NOVA COLINAS | MARANHÃO | Brasil | 2107258 | 21 | 33 | nan | nan | nan | Cerrado | 0.9 |
| ba564da9-dda4-370a-aff0-e288cacb0458 | -7.91329 | -48.29106 | 2026-06-24 05:08:00 | NPP-375D | PALMEIRANTE | TOCANTINS | Brasil | 1715705 | 17 | 33 | nan | nan | nan | Cerrado | 8.9 |
| 09b92b2d-b716-37de-ba73-2489adcb49cf | -4.45449 | -48.02193 | 2026-06-24 05:08:00 | NPP-375D | RONDON DO PARÁ | PARÁ | Brasil | 1506187 | 15 | 33 | nan | nan | nan | Amazônia | 1.4 |
| 9bccbb33-a8d6-38ae-9cf9-7e4be2195dd3 | -9.58475 | -49.11378 | 2026-06-24 05:08:00 | NPP-375D | ABREULÂNDIA | TOCANTINS | Brasil | 1700251 | 17 | 33 | nan | nan | nan | Cerrado | 2.0 |
| 227e1d14-4f6a-322f-ae11-63ee77ac691d | -8.13344 | -47.88699 | 2026-06-24 05:08:00 | NPP-375D | GOIATINS | TOCANTINS | Brasil | 1709005 | 17 | 33 | nan | nan | nan | Cerrado | 1.6 |
| 0dd51905-7df4-3920-8e85-9ec9a9a27d32 | -4.66711 | -43.21992 | 2026-06-24 05:08:00 | NPP-375D | ALDEIAS ALTAS | MARANHÃO | Brasil | 2100303 | 21 | 33 | nan | nan | nan | Cerrado | 1.3 |
| f68b9685-8639-3610-be75-5cc82c69b2d2 | -6.50338 | -42.22203 | 2026-06-24 05:08:00 | NPP-375D | VÁRZEA GRANDE | PIAUÍ | Brasil | 2211407 | 22 | 33 | nan | nan | nan | Caatinga | 1.9 |
| 34531c57-1721-399f-93f4-74f4237100c3 | -4.66346 | -43.21925 | 2026-06-24 05:08:00 | NPP-375D | ALDEIAS ALTAS | MARANHÃO | Brasil | 2100303 | 21 | 33 | nan | nan | nan | Cerrado | 2.1 |
| 40d7d119-ca90-3eee-b54b-4a08516a51bf | -8.8845 | -48.50734 | 2026-06-24 05:08:00 | NPP-375D | GUARAÍ | TOCANTINS | Brasil | 1709302 | 17 | 33 | nan | nan | nan | Cerrado | 1.1 |
| d449fa8e-456c-3585-8807-7abed93d2b82 | -6.50268 | -42.22727 | 2026-06-24 05:08:00 | NPP-375D | VÁRZEA GRANDE | PIAUÍ | Brasil | 2211407 | 22 | 33 | nan | nan | nan | Caatinga | 1.9 |
| 4eda7e40-23eb-3ec6-bbc1-29858edfddb2 | -9.00751 | -48.00025 | 2026-06-24 05:08:00 | NPP-375D | BOM JESUS DO TOCANTINS | TOCANTINS | Brasil | 1703305 | 17 | 33 | nan | nan | nan | Cerrado | 1.2 |
| 21b2f085-61f3-35bb-9704-d0048057853d | -9.21464 | -45.34452 | 2026-06-24 05:08:00 | NPP-375D | BAIXA GRANDE DO RIBEIRO | PIAUÍ | Brasil | 2201150 | 22 | 33 | nan | nan | nan | Cerrado | 1.5 |
| 88c9fd34-4a51-3ca0-a37e-1477e38bf9e0 | -3.51436 | -48.03675 | 2026-06-24 05:08:00 | NPP-375D | PARAGOMINAS | PARÁ | Brasil | 1505502 | 15 | 33 | nan | nan | nan | Amazônia | 1.2 |
| ea781085-532f-332c-89ea-10dce3d7cac3 | -9.00613 | -47.99685 | 2026-06-24 05:08:00 | NPP-375D | BOM JESUS DO TOCANTINS | TOCANTINS | Brasil | 1703305 | 17 | 33 | nan | nan | nan | Cerrado | 1.8 |
| 5319008a-3091-3d8e-99c2-1ee634fabfe8 | -10.11099 | -47.55411 | 2026-06-24 05:08:00 | NPP-375D | NOVO ACORDO | TOCANTINS | Brasil | 1715101 | 17 | 33 | nan | nan | nan | Cerrado | 6.4 |
| 529a1a33-e28a-38b6-b1b3-5e99e0382f25 | -8.61161 | -45.99758 | 2026-06-24 05:08:00 | NPP-375D | TASSO FRAGOSO | MARANHÃO | Brasil | 2112001 | 21 | 33 | nan | nan | nan | Cerrado | 4.6 |
| f7f67070-1d4c-3dca-a9c2-3b8318f4277b | -8.12885 | -47.88626 | 2026-06-24 05:08:00 | NPP-375D | GOIATINS | TOCANTINS | Brasil | 1709005 | 17 | 33 | nan | nan | nan | Cerrado | 1.2 |
| c4985fd0-7032-3d21-87f6-f62e3de5100b | -8.61117 | -46.00076 | 2026-06-24 05:08:00 | NPP-375D | TASSO FRAGOSO | MARANHÃO | Brasil | 2112001 | 21 | 33 | nan | nan | nan | Cerrado | 4.6 |
| d3d48ee2-d0ee-30b6-8f72-98607f59b312 | -7.29633 | -46.25021 | 2026-06-24 05:08:00 | NPP-375D | NOVA COLINAS | MARANHÃO | Brasil | 2107258 | 21 | 33 | nan | nan | nan | Cerrado | 1.5 |
| 372a5819-04d8-3cee-84c6-1659124619fa | -3.87072 | -42.95714 | 2026-06-24 05:08:00 | NPP-375D | BURITI | MARANHÃO | Brasil | 2102200 | 21 | 33 | nan | nan | nan | Cerrado | 1.3 |
| 897f6de7-d635-332d-a36e-c2c6c858203f | -6.51 | -42.22234 | 2026-06-24 05:08:00 | NPP-375D | VÁRZEA GRANDE | PIAUÍ | Brasil | 2211407 | 22 | 33 | nan | nan | nan | Caatinga | 1.9 |
| 090450d7-252c-3c6a-9520-c3eb3d753c99 | -3.8686 | -42.95926 | 2026-06-24 05:08:00 | NPP-375D | BURITI | MARANHÃO | Brasil | 2102200 | 21 | 33 | nan | nan | nan | Cerrado | 1.1 |
| fd82e1fb-b738-346d-bfc2-c17039bf7a2d | -3.50952 | -48.0399 | 2026-06-24 05:08:00 | NPP-375D | PARAGOMINAS | PARÁ | Brasil | 1505502 | 15 | 33 | nan | nan | nan | Amazônia | 1.2 |
| b1010618-ff07-32a6-8682-749c9e7d818a | -6.84088 | -47.86472 | 2026-06-24 05:08:00 | NPP-375D | DARCINÓPOLIS | TOCANTINS | Brasil | 1706506 | 17 | 33 | nan | nan | nan | Cerrado | 1.9 |
| 90072099-3605-3e78-8027-ce9fa0a52b83 | -6.9922 | -42.90198 | 2026-06-24 05:08:00 | NPP-375D | FLORIANO | PIAUÍ | Brasil | 2203909 | 22 | 33 | nan | nan | nan | Caatinga | 8.3 |
| ddf01559-c6f8-3563-84c6-3e81d4de416e | -6.99288 | -42.89693 | 2026-06-24 05:08:00 | NPP-375D | FLORIANO | PIAUÍ | Brasil | 2203909 | 22 | 33 | nan | nan | nan | Caatinga | 8.3 |
| 401b0b45-4509-3a93-bbb4-95b2f76099cf | -7.29674 | -46.24726 | 2026-06-24 05:08:00 | NPP-375D | NOVA COLINAS | MARANHÃO | Brasil | 2107258 | 21 | 33 | nan | nan | nan | Cerrado | 1.5 |
| abaf5ea3-7a11-3232-8aca-42d5cafa1eb2 | -3.96036 | -43.11187 | 2026-06-24 05:08:00 | NPP-375D | BURITI | MARANHÃO | Brasil | 2102200 | 21 | 33 | nan | nan | nan | Cerrado | 0.9 |
| a3b5812e-677d-3105-b3d4-f42ec1a18938 | -6.99356 | -42.89191 | 2026-06-24 05:08:00 | NPP-375D | FLORIANO | PIAUÍ | Brasil | 2203909 | 22 | 33 | nan | nan | nan | Caatinga | 2.6 |
| 6787c652-eca8-3b33-adfc-28dcfbc81e05 | -6.50427 | -42.22133 | 2026-06-24 05:08:00 | NPP-375D | VÁRZEA GRANDE | PIAUÍ | Brasil | 2211407 | 22 | 33 | nan | nan | nan | Caatinga | 1.8 |
| 44fa893a-ea2a-3a50-88c2-7c630fab1ef5 | -8.12425 | -47.88556 | 2026-06-24 05:08:00 | NPP-375D | GOIATINS | TOCANTINS | Brasil | 1709005 | 17 | 33 | nan | nan | nan | Cerrado | 1.2 |
| c815d1b6-1033-3c4a-8b16-039b203bba33 | -8.68309 | -47.85407 | 2026-06-24 05:08:00 | NPP-375D | ITACAJÁ | TOCANTINS | Brasil | 1710508 | 17 | 33 | nan | nan | nan | Cerrado | 8.2 |
| 48abfebb-e706-3ce2-b3e6-516f72a7cc2d | -9.80483 | -48.91896 | 2026-06-24 05:08:00 | NPP-375D | BARROLÂNDIA | TOCANTINS | Brasil | 1703107 | 17 | 33 | nan | nan | nan | Cerrado | 2.5 |
| 3ddec2f8-9a05-3e83-a429-485e9271befe | -9.37053 | -50.53166 | 2026-06-24 05:08:00 | NPP-375D | SANTANA DO ARAGUAIA | PARÁ | Brasil | 1506708 | 15 | 33 | nan | nan | nan | Amazônia | 0.8 |
| 307a737a-c231-3967-bf57-8f5b1620d53a | -9.22069 | -45.34157 | 2026-06-24 05:08:00 | NPP-375D | BAIXA GRANDE DO RIBEIRO | PIAUÍ | Brasil | 2201150 | 22 | 33 | nan | nan | nan | Cerrado | 1.9 |
| cd41f5f7-4a4d-3135-92c3-6efa53f428b7 | -7.92282 | -48.28804 | 2026-06-24 05:08:00 | NPP-375D | PALMEIRANTE | TOCANTINS | Brasil | 1715705 | 17 | 33 | nan | nan | nan | Cerrado | 2.9 |
| c51ebfe5-0bc0-3a5c-93ad-1407504ab45a | -8.07871 | -46.3908 | 2026-06-24 05:08:00 | NPP-375D | BALSAS | MARANHÃO | Brasil | 2101400 | 21 | 33 | nan | nan | nan | Cerrado | 1.3 |
| b5861991-74aa-3ffa-b714-969a18e2d734 | -4.66047 | -43.22346 | 2026-06-24 05:08:00 | NPP-375D | ALDEIAS ALTAS | MARANHÃO | Brasil | 2100303 | 21 | 33 | nan | nan | nan | Cerrado | 2.0 |
| ca4137e2-e419-3a02-9956-ef910f93ef92 | -8.68775 | -47.85464 | 2026-06-24 05:08:00 | NPP-375D | ITACAJÁ | TOCANTINS | Brasil | 1710508 | 17 | 33 | nan | nan | nan | Cerrado | 8.2 |
| 789f0f89-f8b9-3ac2-98e1-7f7eb5608593 | -8.85714 | -46.94659 | 2026-06-24 05:08:00 | NPP-375D | RECURSOLÂNDIA | TOCANTINS | Brasil | 1718501 | 17 | 33 | nan | nan | nan | Cerrado | 2.0 |
| e070ff86-3811-319e-a554-5a17932989ac | -7.37585 | -42.80009 | 2026-06-24 05:08:00 | NPP-375D | SÃO JOSÉ DO PEIXE | PIAUÍ | Brasil | 2210102 | 22 | 33 | nan | nan | nan | Caatinga | 1.3 |
| db054f8c-11ab-3f84-8879-99faae4e7a57 | -9.36979 | -50.53668 | 2026-06-24 05:08:00 | NPP-375D | SANTANA DO ARAGUAIA | PARÁ | Brasil | 1506708 | 15 | 33 | nan | nan | nan | Amazônia | 0.8 |
| efc3c7df-ad21-3bfb-8be6-39da0dda075c | -9.44114 | -48.86874 | 2026-06-24 05:08:00 | NPP-375D | DOIS IRMÃOS DO TOCANTINS | TOCANTINS | Brasil | 1707207 | 17 | 33 | nan | nan | nan | Cerrado | 1.5 |
| a4130c8d-1e2b-3d14-9ce5-f398930ac27d | -3.51011 | -48.03609 | 2026-06-24 05:08:00 | NPP-375D | PARAGOMINAS | PARÁ | Brasil | 1505502 | 15 | 33 | nan | nan | nan | Amazônia | 1.2 |
| 30943c1e-9c98-3bba-828c-733b429e94c6 | -9.41057 | -50.69632 | 2026-06-24 05:08:00 | NPP-375D | SANTANA DO ARAGUAIA | PARÁ | Brasil | 1506708 | 15 | 33 | nan | nan | nan | Amazônia | 2.2 |
| ac843c8e-81c1-3810-9a0d-a94dd1767d26 | -7.59932 | -46.48062 | 2026-06-24 05:08:00 | NPP-375D | RIACHÃO | MARANHÃO | Brasil | 2109502 | 21 | 33 | nan | nan | nan | Cerrado | 1.9 |
| f54fb8e9-28cb-37ec-b859-cd8603a03275 | -9.44055 | -48.87304 | 2026-06-24 05:08:00 | NPP-375D | DOIS IRMÃOS DO TOCANTINS | TOCANTINS | Brasil | 1707207 | 17 | 33 | nan | nan | nan | Cerrado | 1.5 |
| 8bd1144b-1fd3-31a5-b555-e656749893f5 | -9.21513 | -45.34082 | 2026-06-24 05:08:00 | NPP-375D | BAIXA GRANDE DO RIBEIRO | PIAUÍ | Brasil | 2201150 | 22 | 33 | nan | nan | nan | Cerrado | 1.5 |
| 0ebbbf7a-fdad-3576-9b02-2049afb762a9 | -10.62662 | -44.85626 | 2026-06-24 05:08:00 | NPP-375D | SEBASTIÃO BARROS | PIAUÍ | Brasil | 2210623 | 22 | 33 | nan | nan | nan | Cerrado | 1.1 |
| 4021a17e-7633-3ec3-86dd-4ba020fd4be3 | -9.4601 | -49.83138 | 2026-06-24 05:08:00 | NPP-375D | CASEARA | TOCANTINS | Brasil | 1703909 | 17 | 33 | nan | nan | nan | Cerrado | 2.2 |
| ee3b7cdd-208e-3ce8-b10c-891a3c6bbec8 | -8.85295 | -46.94007 | 2026-06-24 05:08:00 | NPP-375D | RECURSOLÂNDIA | TOCANTINS | Brasil | 1718501 | 17 | 33 | nan | nan | nan | Cerrado | 2.1 |
| c05d608c-8937-3c8f-b509-2409a5ceded7 | -9.36832 | -50.54669 | 2026-06-24 05:08:00 | NPP-375D | SANTANA DO ARAGUAIA | PARÁ | Brasil | 1506708 | 15 | 33 | nan | nan | nan | Amazônia | 3.2 |
| a3b8dba9-3263-3b9e-b646-22a04e7c5d09 | -8.61031 | -46.00703 | 2026-06-24 05:08:00 | NPP-375D | TASSO FRAGOSO | MARANHÃO | Brasil | 2112001 | 21 | 33 | nan | nan | nan | Cerrado | 1.9 |
| 96dca153-48ea-38dd-9ec5-fc75cb7a2085 | -9.44174 | -48.86438 | 2026-06-24 05:08:00 | NPP-375D | DOIS IRMÃOS DO TOCANTINS | TOCANTINS | Brasil | 1707207 | 17 | 33 | nan | nan | nan | Cerrado | 0.3 |
| ab09ea6b-a527-3293-af62-4c94893738a9 | -7.59938 | -46.47526 | 2026-06-24 05:08:00 | NPP-375D | RIACHÃO | MARANHÃO | Brasil | 2109502 | 21 | 33 | nan | nan | nan | Cerrado | 1.9 |
| d4306daf-0d01-3dfe-b111-3f7c97314211 | -8.61205 | -45.99436 | 2026-06-24 05:08:00 | NPP-375D | TASSO FRAGOSO | MARANHÃO | Brasil | 2112001 | 21 | 33 | nan | nan | nan | Cerrado | 1.6 |
| b5d7404b-70a7-3abc-8634-302b91538bd9 | -4.66222 | -43.22809 | 2026-06-24 05:08:00 | NPP-375D | ALDEIAS ALTAS | MARANHÃO | Brasil | 2100303 | 21 | 33 | nan | nan | nan | Cerrado | 2.9 |
| 2ed598f9-eaa0-3ef8-9539-180a6b39cb98 | -7.3646 | -47.03101 | 2026-06-24 05:08:00 | NPP-375D | CAROLINA | MARANHÃO | Brasil | 2102804 | 21 | 33 | nan | nan | nan | Cerrado | 5.3 |
| 2cbf7045-6295-3c39-a39f-b4805dbe3e48 | -10.11173 | -47.54873 | 2026-06-24 05:08:00 | NPP-375D | NOVO ACORDO | TOCANTINS | Brasil | 1715101 | 17 | 33 | nan | nan | nan | Cerrado | 1.5 |
| 888c802e-2d34-3a1f-9e81-65705f04abc6 | -4.45393 | -49.14901 | 2026-06-24 05:08:00 | NPP-375D | JACUNDÁ | PARÁ | Brasil | 1503804 | 15 | 33 | nan | nan | nan | Amazônia | 0.7 |
| 71902170-ecda-3ceb-beaf-d5a2b692044b | -8.85223 | -46.94547 | 2026-06-24 05:08:00 | NPP-375D | RECURSOLÂNDIA | TOCANTINS | Brasil | 1718501 | 17 | 33 | nan | nan | nan | Cerrado | 2.1 |
| c2ef6e76-5396-302e-8b11-ea1136462566 | -9.13881 | -47.98429 | 2026-06-24 05:08:00 | NPP-375D | PEDRO AFONSO | TOCANTINS | Brasil | 1716505 | 17 | 33 | nan | nan | nan | Cerrado | 2.1 |
| 7b32c8ba-4cba-3608-b7f1-fe6e35f267a7 | -4.66646 | -43.22435 | 2026-06-24 05:08:00 | NPP-375D | ALDEIAS ALTAS | MARANHÃO | Brasil | 2100303 | 21 | 33 | nan | nan | nan | Cerrado | 1.3 |
| 9c152344-e5db-39da-9249-805bdc1d02e5 | -4.45018 | -48.02124 | 2026-06-24 05:08:00 | NPP-375D | RONDON DO PARÁ | PARÁ | Brasil | 1506187 | 15 | 33 | nan | nan | nan | Amazônia | 1.0 |
| ca7d8844-a04f-302f-ab33-6cb559b19909 | -8.61074 | -46.00389 | 2026-06-24 05:08:00 | NPP-375D | TASSO FRAGOSO | MARANHÃO | Brasil | 2112001 | 21 | 33 | nan | nan | nan | Cerrado | 1.9 |
| c49c6310-9a5b-38e3-81d6-827bbebeffae | -7.29123 | -46.2495 | 2026-06-24 05:08:00 | NPP-375D | NOVA COLINAS | MARANHÃO | Brasil | 2107258 | 21 | 33 | nan | nan | nan | Cerrado | 1.5 |
| 563b1ed0-3019-340f-942f-ab3629b1eb29 | -4.65665 | -43.12375 | 2026-06-24 05:08:00 | NPP-375D | CAXIAS | MARANHÃO | Brasil | 2103000 | 21 | 33 | nan | nan | nan | Cerrado | 1.0 |
| 477153b3-b2f8-3717-a187-a181f81f2781 | -8.85644 | -46.95173 | 2026-06-24 05:08:00 | NPP-375D | RECURSOLÂNDIA | TOCANTINS | Brasil | 1718501 | 17 | 33 | nan | nan | nan | Cerrado | 2.7 |
| bdf89127-7212-37ba-bceb-6612c87f5ee1 | -7.80519 | -46.46306 | 2026-06-24 05:08:00 | NPP-375D | RIACHÃO | MARANHÃO | Brasil | 2109502 | 21 | 33 | nan | nan | nan | Cerrado | 1.5 |
| 2bc5034c-0c39-3824-a972-92c41759894f | -6.84465 | -47.90217 | 2026-06-24 05:08:00 | NPP-375D | WANDERLÂNDIA | TOCANTINS | Brasil | 1722081 | 17 | 33 | nan | nan | nan | Cerrado | 6.9 |
| 785076ce-50be-3a14-8bfe-ea9d69eb9cf0 | -7.91774 | -48.29175 | 2026-06-24 05:08:00 | NPP-375D | PALMEIRANTE | TOCANTINS | Brasil | 1715705 | 17 | 33 | nan | nan | nan | Cerrado | 8.9 |
| d20bda4e-8a3f-33ed-899d-a11851cec3bc | -6.50353 | -42.22658 | 2026-06-24 05:08:00 | NPP-375D | VÁRZEA GRANDE | PIAUÍ | Brasil | 2211407 | 22 | 33 | nan | nan | nan | Caatinga | 4.3 |
| e76a1247-662e-3394-92d4-a7aa4a1a8d2f | -9.2202 | -45.34528 | 2026-06-24 05:08:00 | NPP-375D | BAIXA GRANDE DO RIBEIRO | PIAUÍ | Brasil | 2201150 | 22 | 33 | nan | nan | nan | Cerrado | 1.9 |
| 11284f02-22eb-30e0-bb61-3da10e3edde5 | -4.65982 | -43.22786 | 2026-06-24 05:08:00 | NPP-375D | ALDEIAS ALTAS | MARANHÃO | Brasil | 2100303 | 21 | 33 | nan | nan | nan | Cerrado | 1.7 |
| f24d2b3d-aaf1-3d8e-9442-7be6cfcd0c67 | -7.60015 | -46.47482 | 2026-06-24 05:08:00 | NPP-375D | RIACHÃO | MARANHÃO | Brasil | 2109502 | 21 | 33 | nan | nan | nan | Cerrado | 1.9 |
| 05b320d3-3a8b-3d5a-9cbb-740639882e99 | -7.5986 | -46.48107 | 2026-06-24 05:08:00 | NPP-375D | RIACHÃO | MARANHÃO | Brasil | 2109502 | 21 | 33 | nan | nan | nan | Cerrado | 2.5 |
| 2bb7d530-d0cb-3b21-9b6b-6acb2d9acbab | -6.83958 | -47.87367 | 2026-06-24 05:08:00 | NPP-375D | DARCINÓPOLIS | TOCANTINS | Brasil | 1706506 | 17 | 33 | nan | nan | nan | Cerrado | 1.7 |
| 99a4f80b-f9d6-3c65-b43d-f544acfdc4ea | -10.63246 | -44.85717 | 2026-06-24 05:08:00 | NPP-375D | SEBASTIÃO BARROS | PIAUÍ | Brasil | 2210623 | 22 | 33 | nan | nan | nan | Cerrado | 1.1 |


[Clique aqui para ver as próximas entradas](README16.md)
