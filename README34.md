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

## Dados Diários - Página 34

| ID | Latitude | Longitude | Data/Hora GMT | Satélite | Município | Estado | País | Município ID | Estado ID | País ID | Dias sem Chuva | Precipitação | Risco de Fogo | Bioma | FRP |
|----|----------|-----------|---------------|----------|-----------|--------|------|--------------|-----------|---------|----------------|--------------|----------------|-------|-----|
| a56dbf67-9774-398f-b10c-6e906cececda | -3.2101 | -53.880699 | 2026-10-08 00:48:00 | METOP-C | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| fcb4cb32-fdea-3ab5-9aed-0c0e5a4bcd81 | -10.8819 | -49.148201 | 2026-10-08 00:48:00 | METOP-C | SANTA RITA DO TOCANTINS | TOCANTINS | Brasil | 1718899 | 17 | 33 | nan | nan | nan | Cerrado | nan |
| 09ed76db-bb48-33cd-b212-773f96f4fff1 | -3.0499 | -53.900501 | 2026-10-08 00:48:00 | METOP-C | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| 80901a9b-c117-3f64-ab42-cb55dc38b8e0 | -3.6712 | -54.5056 | 2026-10-08 00:48:00 | METOP-C | PLACAS | PARÁ | Brasil | 1505650 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| fc13e302-70da-3868-86b0-064d5eb98e99 | -2.9702 | -54.138802 | 2026-10-08 00:48:00 | METOP-C | SANTARÉM | PARÁ | Brasil | 1506807 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| 3998be10-7671-31ca-b144-87b23dc2a92b | -2.5004 | -56.1465 | 2026-10-08 00:48:00 | METOP-C | JURUTI | PARÁ | Brasil | 1503903 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| 7da147de-8072-351d-9700-b5041daa1c8a | -6.2025 | -52.862 | 2026-10-08 00:48:00 | METOP-C | SÃO FÉLIX DO XINGU | PARÁ | Brasil | 1507300 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| 9fd86315-9c83-3afe-9f18-416ec8278c0d | -3.59 | -54.692299 | 2026-10-08 00:48:00 | METOP-C | PLACAS | PARÁ | Brasil | 1505650 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| 1fcc41c8-9597-388a-8038-0595d7d4aad0 | -2.9783 | -54.129101 | 2026-10-08 00:48:00 | METOP-C | SANTARÉM | PARÁ | Brasil | 1506807 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| 67bc9031-db2a-325a-846a-4e361b311480 | -6.8989 | -43.684101 | 2026-10-08 00:48:00 | METOP-C | GUADALUPE | PIAUÍ | Brasil | 2204501 | 22 | 33 | nan | nan | nan | Cerrado | nan |
| 6a89530f-c9fd-3175-b4db-060df55919a6 | -6.2139 | -52.867199 | 2026-10-08 00:48:00 | METOP-C | SÃO FÉLIX DO XINGU | PARÁ | Brasil | 1507300 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| e2c87c5a-9256-3218-acc6-4951f1d46552 | -8.7279 | -45.167801 | 2026-10-08 00:48:00 | METOP-C | BAIXA GRANDE DO RIBEIRO | PIAUÍ | Brasil | 2201150 | 22 | 33 | nan | nan | nan | Cerrado | nan |
| 26c69c9a-b5e1-3c29-afdd-b8c0de86db46 | -3.0579 | -54.207298 | 2026-10-08 00:48:00 | METOP-C | SANTARÉM | PARÁ | Brasil | 1506807 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| 12a69cdc-81a8-37ed-a8e9-4c682b7fbf27 | -2.4541 | -56.0783 | 2026-10-08 00:48:00 | METOP-C | JURUTI | PARÁ | Brasil | 1503903 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| 4c982b80-9959-34f8-b97a-2d9d0b939d65 | -1.7697 | -55.060902 | 2026-10-08 00:48:00 | METOP-C | ALENQUER | PARÁ | Brasil | 1500404 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| 8157cc34-4faa-3911-9913-c95f81baf6a9 | -3.1 | -54.166 | 2026-10-08 00:48:00 | METOP-C | SANTARÉM | PARÁ | Brasil | 1506807 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| 105c3782-fd55-3480-945d-b3922da02c5d | -8.0849 | -55.328899 | 2026-10-08 00:48:00 | METOP-C | NOVO PROGRESSO | PARÁ | Brasil | 1505031 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| 95388549-dcf3-3a83-a956-b1a5ab36f826 | -2.4949 | -56.1675 | 2026-10-08 00:48:00 | METOP-C | JURUTI | PARÁ | Brasil | 1503903 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| 1416becb-840b-3233-afdc-309292b24c68 | -3.1258 | -54.370098 | 2026-10-08 00:48:00 | METOP-C | MOJUÍ DOS CAMPOS | PARÁ | Brasil | 1504752 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| 154eb42f-f468-3e6f-bf2d-de6ae7e8a99d | -3.055 | -54.240002 | 2026-10-08 00:48:00 | METOP-C | MOJUÍ DOS CAMPOS | PARÁ | Brasil | 1504752 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| b75e86ab-960e-332a-9f36-51c675770bf6 | -6.2237 | -52.865002 | 2026-10-08 00:48:00 | METOP-C | SÃO FÉLIX DO XINGU | PARÁ | Brasil | 1507300 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| 72beb8eb-3fbc-33fb-a75a-79190854aafb | -11.6429 | -43.7085 | 2026-10-08 00:48:00 | METOP-C | BARRA | BAHIA | Brasil | 2902708 | 29 | 33 | nan | nan | nan | Cerrado | nan |
| 586eb265-6289-3062-a234-202e5083c5a7 | -8.7332 | -45.189701 | 2026-10-08 00:48:00 | METOP-C | BAIXA GRANDE DO RIBEIRO | PIAUÍ | Brasil | 2201150 | 22 | 33 | nan | nan | nan | Cerrado | nan |
| 5b021c26-4076-3e43-8588-1e49807d9e1d | -2.9241 | -54.117298 | 2026-10-08 00:48:00 | METOP-C | SANTARÉM | PARÁ | Brasil | 1506807 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| f90c937c-695d-3802-9fa2-5627203c25ea | -3.1928 | -50.567101 | 2026-10-08 00:48:00 | METOP-C | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| c5af8dcc-1de0-3425-b0dd-03ce9c08b627 | -7.8497 | -49.290199 | 2026-10-08 00:48:00 | METOP-C | CONCEIÇÃO DO ARAGUAIA | PARÁ | Brasil | 1502707 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| 7529aed6-7724-3f4c-bc9a-73bf48603100 | -3.0937 | -54.1833 | 2026-10-08 00:48:00 | METOP-C | SANTARÉM | PARÁ | Brasil | 1506807 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| a360b2af-0bd7-3360-9669-993dd3d07884 | -5.237 | -48.400002 | 2026-10-08 00:48:00 | METOP-C | SÃO SEBASTIÃO DO TOCANTINS | TOCANTINS | Brasil | 1720309 | 17 | 33 | nan | nan | nan | Amazônia | nan |
| 9e74e893-c5d1-34e7-8413-979fd4fe3464 | -2.1049 | -52.069 | 2026-10-08 00:48:00 | METOP-C | PORTO DE MOZ | PARÁ | Brasil | 1505908 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| da860b2d-9e8d-35c1-bce3-c35d537749e9 | -2.56 | -56.182899 | 2026-10-08 00:48:00 | METOP-C | JURUTI | PARÁ | Brasil | 1503903 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| aa8a258b-5448-31e1-8cd3-8d60ec9e00e6 | -2.4864 | -56.130001 | 2026-10-08 00:48:00 | METOP-C | JURUTI | PARÁ | Brasil | 1503903 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| c9cd972c-d9cb-3216-ae5c-7a3c8750fd4c | -2.8043 | -54.088501 | 2026-10-08 00:48:00 | METOP-C | PRAINHA | PARÁ | Brasil | 1506005 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| 04a7a4ad-554e-326d-8acc-4f11e518515b | -3.8497 | -55.9795 | 2026-10-08 00:48:00 | METOP-C | AVEIRO | PARÁ | Brasil | 1501006 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| 7fe7c22b-6cee-3eab-b585-7a2b9b94654c | -1.4011 | -48.931301 | 2026-10-08 00:48:00 | METOP-C | PONTA DE PEDRAS | PARÁ | Brasil | 1505700 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| 3ae88460-1719-3610-bc4d-27678dfc5109 | -2.494 | -56.118401 | 2026-10-08 00:48:00 | METOP-C | JURUTI | PARÁ | Brasil | 1503903 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| 3e4cc6ef-c927-3eee-bacf-08b646a06d0a | -3.4378 | -56.932499 | 2026-10-08 00:48:00 | METOP-C | BARREIRINHA | AMAZONAS | Brasil | 1300508 | 13 | 33 | nan | nan | nan | Amazônia | nan |
| c4b41480-3302-3918-9da2-8824d85f6b32 | -3.0354 | -54.108501 | 2026-10-08 00:48:00 | METOP-C | SANTARÉM | PARÁ | Brasil | 1506807 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| bea3635e-e169-3ffd-900d-1d70558202f5 | -4.1085 | -59.8964 | 2026-10-08 00:48:00 | METOP-C | AUTAZES | AMAZONAS | Brasil | 1300300 | 13 | 33 | nan | nan | nan | Amazônia | nan |
| c5d779bf-a8bb-3735-b42c-866f16612ac1 | -7.1696 | -47.797001 | 2026-10-08 00:48:00 | METOP-C | BABAÇULÂNDIA | TOCANTINS | Brasil | 1703008 | 17 | 33 | nan | nan | nan | Cerrado | nan |
| e34c09a3-13f3-3682-83c6-e4c4c6bed6b9 | -1.4549 | -54.765099 | 2026-10-08 00:48:00 | METOP-C | ALENQUER | PARÁ | Brasil | 1500404 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| 49dcb790-2ab3-39f6-8c6f-6e0a9d646966 | -3.0135 | -54.057899 | 2026-10-08 00:48:00 | METOP-C | SANTARÉM | PARÁ | Brasil | 1506807 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| 420db6c4-471b-34cf-8ca1-898818b71940 | -5.9873 | -40.9384 | 2026-10-08 00:48:00 | METOP-C | ASSUNÇÃO DO PIAUÍ | PIAUÍ | Brasil | 2201051 | 22 | 33 | nan | nan | nan | Caatinga | nan |
| c073aee7-93ca-3b8f-a61a-890d1c2a75db | -2.8413 | -57.471699 | 2026-10-08 00:48:00 | METOP-C | BOA VISTA DO RAMOS | AMAZONAS | Brasil | 1300680 | 13 | 33 | nan | nan | nan | Amazônia | nan |
| 0265f84b-4763-3508-be78-29bc7c6a45e3 | -3.2194 | -54.374001 | 2026-10-08 00:48:00 | METOP-C | MOJUÍ DOS CAMPOS | PARÁ | Brasil | 1504752 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| d57c2f3b-21cb-369b-b9eb-b696539397be | -3.2857 | -54.077 | 2026-10-08 00:48:00 | METOP-C | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| 1d733e14-161b-397d-a4ba-0697aabc7ad0 | -3.722 | -54.230099 | 2026-10-08 00:48:00 | METOP-C | PLACAS | PARÁ | Brasil | 1505650 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| 2c35ef21-6fc0-3b7a-bbe5-584d6c87d1fc | -3.3048 | -54.025002 | 2026-10-08 00:48:00 | METOP-C | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| 8ed18c0a-ff97-395b-a6d0-142c396efb89 | -5.9498 | -55.362801 | 2026-10-08 00:48:00 | METOP-C | ITAITUBA | PARÁ | Brasil | 1503606 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| ea890636-258a-3e1f-a983-c2c968f1890b | -2.5044 | -56.254902 | 2026-10-08 00:48:00 | METOP-C | JURUTI | PARÁ | Brasil | 1503903 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| 74c92de7-cdb3-3be4-ada9-b3d3facd790b | -2.9962 | -54.117199 | 2026-10-08 00:48:00 | METOP-C | SANTARÉM | PARÁ | Brasil | 1506807 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| b751b27d-b74a-352e-a56d-963b6aaecadc | -3.1484 | -54.107399 | 2026-10-08 00:48:00 | METOP-C | SANTARÉM | PARÁ | Brasil | 1506807 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| b05ba282-cf79-3108-bdf3-dfc4c0ec24a8 | -6.2008 | -52.854698 | 2026-10-08 00:48:00 | METOP-C | SÃO FÉLIX DO XINGU | PARÁ | Brasil | 1507300 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| 0e9f748e-6fc0-32d6-a13d-ae5f78a9313b | -2.4562 | -56.087601 | 2026-10-08 00:48:00 | METOP-C | JURUTI | PARÁ | Brasil | 1503903 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| b0d93196-b3a7-3279-9a93-17f61091792f | -6.2156 | -52.8745 | 2026-10-08 00:48:00 | METOP-C | SÃO FÉLIX DO XINGU | PARÁ | Brasil | 1507300 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| d7136881-14c1-3ea9-8860-3edc04a46c5b | 1.7115 | -55.604198 | 2026-10-08 00:48:00 | METOP-C | ÓBIDOS | PARÁ | Brasil | 1505106 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| f43f8e78-9d77-3b8d-aeb0-c83900e5245d | -3.2673 | -54.041199 | 2026-10-08 00:48:00 | METOP-C | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| c21c64a7-9ee8-3345-8391-9a9083f61fb1 | -3.2457 | -46.948601 | 2026-10-08 00:48:00 | METOP-C | PARAGOMINAS | PARÁ | Brasil | 1505502 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| 91cf338d-7095-3302-8a0a-f8b43f1ca7fa | -6.6392 | -43.7164 | 2026-10-08 00:48:00 | METOP-C | SÃO JOÃO DOS PATOS | MARANHÃO | Brasil | 2111102 | 21 | 33 | nan | nan | nan | Cerrado | nan |
| 4bff60ce-4e43-3307-84b0-b51e018cb596 | -8.0708 | -55.311001 | 2026-10-08 00:48:00 | METOP-C | NOVO PROGRESSO | PARÁ | Brasil | 1505031 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| 95b84a2d-a078-3ade-b004-247fd4f4907f | -4.1449 | -54.9175 | 2026-10-08 00:48:00 | METOP-C | RURÓPOLIS | PARÁ | Brasil | 1506195 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| 189ef016-1ac9-398e-9db9-14f1bc1157ad | -3.1133 | -54.179001 | 2026-10-08 00:48:00 | METOP-C | SANTARÉM | PARÁ | Brasil | 1506807 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| 3255f5b4-996e-3de6-aaf4-474e808807cb | -3.0088 | -54.7612 | 2026-10-08 00:48:00 | METOP-C | MOJUÍ DOS CAMPOS | PARÁ | Brasil | 1504752 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| 96b57797-7192-3347-b347-1bb26d2cfbef | -4.4521 | -47.913399 | 2026-10-08 00:48:00 | METOP-C | DOM ELISEU | PARÁ | Brasil | 1502939 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| e39c4268-5a90-3612-a8db-b51c604551fb | -4.1024 | -54.4105 | 2026-10-08 00:48:00 | METOP-C | PLACAS | PARÁ | Brasil | 1505650 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| 341ed707-96f5-30d5-82ea-dade162ba3c4 | -3.5957 | -54.581001 | 2026-10-08 00:48:00 | METOP-C | PLACAS | PARÁ | Brasil | 1505650 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| 21d1174d-470a-395f-979f-b57b6bd2720c | -2.4906 | -56.148701 | 2026-10-08 00:48:00 | METOP-C | JURUTI | PARÁ | Brasil | 1503903 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| 145b0dac-f794-30ee-ba6b-5e6577feb974 | -11.389 | -46.6866 | 2026-10-08 00:48:00 | METOP-C | RIO DA CONCEIÇÃO | TOCANTINS | Brasil | 1718659 | 17 | 33 | nan | nan | nan | Cerrado | nan |
| 98e941b1-a326-3836-9105-6ce7f49717f9 | -3.0533 | -54.232399 | 2026-10-08 00:48:00 | METOP-C | SANTARÉM | PARÁ | Brasil | 1506807 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| 9ca5983e-3bb1-3450-917d-d07f43616a22 | -6.0573 | -47.327599 | 2026-10-08 00:48:00 | METOP-C | RIBAMAR FIQUENE | MARANHÃO | Brasil | 2109551 | 21 | 33 | nan | nan | nan | Cerrado | nan |
| ff26db6c-fe93-327d-9df0-d941e8427959 | -6.2548 | -52.865799 | 2026-10-08 00:48:00 | METOP-C | SÃO FÉLIX DO XINGU | PARÁ | Brasil | 1507300 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| a40c8871-42cb-3b3e-b9da-ab0d389c7746 | -6.6464 | -43.745899 | 2026-10-08 00:48:00 | METOP-C | SÃO JOÃO DOS PATOS | MARANHÃO | Brasil | 2111102 | 21 | 33 | nan | nan | nan | Cerrado | nan |
| 659cf655-21a0-37ff-9c45-06b05444ba26 | -5.0747 | -48.4119 | 2026-10-08 00:48:00 | METOP-C | ABEL FIGUEIREDO | PARÁ | Brasil | 1500131 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| 1c53620d-5e56-3238-9857-3981c9f528f3 | -4.3168 | -50.789001 | 2026-10-08 00:48:00 | METOP-C | NOVO REPARTIMENTO | PARÁ | Brasil | 1505064 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| f0829ad8-accc-3dd1-b476-04445d133274 | -7.1459 | -46.525002 | 2026-10-08 00:48:00 | METOP-C | RIACHÃO | MARANHÃO | Brasil | 2109502 | 21 | 33 | nan | nan | nan | Cerrado | nan |
| a898261e-af78-3f5c-98d3-b252894c3dc0 | -2.5732 | -56.1502 | 2026-10-08 00:48:00 | METOP-C | JURUTI | PARÁ | Brasil | 1503903 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| 262d510f-70b2-392d-b29a-d363a28e4334 | -2.6564 | -52.584702 | 2026-10-08 00:48:00 | METOP-C | PORTO DE MOZ | PARÁ | Brasil | 1505908 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| b0ba6745-f780-3a0d-8f6a-1fc9495204c5 | -2.3364 | -55.695999 | 2026-10-08 00:48:00 | METOP-C | SANTARÉM | PARÁ | Brasil | 1506807 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| 3f422d7b-85b3-3659-ad2c-2e8445619236 | -3.0401 | -53.902699 | 2026-10-08 00:48:00 | METOP-C | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| b82638de-8500-3b86-856a-cd55dd792d49 | -6.9258 | -49.622601 | 2026-10-08 00:48:00 | METOP-C | SAPUCAIA | PARÁ | Brasil | 1507755 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| b97d0237-762e-3f7b-93ff-e363f8a9313b | -6.2286 | -52.8409 | 2026-10-08 00:48:00 | METOP-C | SÃO FÉLIX DO XINGU | PARÁ | Brasil | 1507300 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| e32621d6-8608-3422-9c3d-1833f1a8d6c5 | -11.0633 | -49.533798 | 2026-10-08 00:48:00 | METOP-C | SANTA RITA DO TOCANTINS | TOCANTINS | Brasil | 1718899 | 17 | 33 | nan | nan | nan | Cerrado | nan |
| b403ac73-0e2f-3638-9fb7-70bd128c2f60 | -1.8242 | -54.939301 | 2026-10-08 00:48:00 | METOP-C | ALENQUER | PARÁ | Brasil | 1500404 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| c62db24f-c842-340c-b32b-ff36d29b9305 | -8.7305 | -45.178799 | 2026-10-08 00:48:00 | METOP-C | BAIXA GRANDE DO RIBEIRO | PIAUÍ | Brasil | 2201150 | 22 | 33 | nan | nan | nan | Cerrado | nan |
| b022acd8-78be-3fdc-8e5c-b51f2c8ea214 | -7.7567 | -54.9519 | 2026-10-08 00:48:00 | METOP-C | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| 4607fad2-f1af-3325-beb4-050f3065a924 | -1.1217 | -54.120098 | 2026-10-08 00:48:00 | METOP-C | MONTE ALEGRE | PARÁ | Brasil | 1504802 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| 99f6ad64-a7af-3f84-a6f2-ba1259443310 | -3.1682 | -50.5947 | 2026-10-08 00:48:00 | METOP-C | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| c12627e8-f02a-3819-8909-f621c401609a | -3.1674 | -54.7346 | 2026-10-08 00:48:00 | METOP-C | MOJUÍ DOS CAMPOS | PARÁ | Brasil | 1504752 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| a4a554a7-b146-3d56-baa2-325094f936ac | -6.3203 | -55.321999 | 2026-10-08 00:48:00 | METOP-C | ITAITUBA | PARÁ | Brasil | 1503606 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| 28eb405b-33b1-3cb0-96e2-1958c6b6a006 | -3.5623 | -59.501202 | 2026-10-08 00:48:00 | METOP-C | AUTAZES | AMAZONAS | Brasil | 1300300 | 13 | 33 | nan | nan | nan | Amazônia | nan |
| 84d9870b-d080-3b05-b82d-dfb3691029e8 | -3.2042 | -50.571899 | 2026-10-08 00:48:00 | METOP-C | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| 57ce7eeb-45af-3804-a4f5-b233e35b10cb | -8.7234 | -45.192101 | 2026-10-08 00:48:00 | METOP-C | BAIXA GRANDE DO RIBEIRO | PIAUÍ | Brasil | 2201150 | 22 | 33 | nan | nan | nan | Cerrado | nan |
| 57010192-90ea-3f9f-aea9-c76b88fefbe0 | -5.8457 | -53.471298 | 2026-10-08 00:48:00 | METOP-C | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| da231716-b7d2-307b-a310-b4b16b9b87db | -16.8985 | -40.9007 | 2026-10-08 00:48:00 | METOP-C | FRONTEIRA DOS VALES | MINAS GERAIS | Brasil | 3127057 | 31 | 33 | nan | nan | nan | Mata Atlântica | nan |
| 28cd5724-a152-3647-b431-00273c5a1c44 | -6.2499 | -52.889801 | 2026-10-08 00:48:00 | METOP-C | SÃO FÉLIX DO XINGU | PARÁ | Brasil | 1507300 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| 319ccd24-9448-3acf-8cb9-f0abb29de93e | -3.2331 | -53.891201 | 2026-10-08 00:48:00 | METOP-C | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| 7dc229fa-4c26-3388-9b67-b029895e41fb | -2.93 | -54.0527 | 2026-10-08 00:48:00 | METOP-C | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| 5fd06030-d60a-36f7-bb63-2eb8590c9a64 | -7.902 | -54.7257 | 2026-10-08 00:48:00 | METOP-C | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| e5bd36a6-2248-3ddc-aa96-3d2e20e55bcb | -3.0089 | -54.0826 | 2026-10-08 00:48:00 | METOP-C | SANTARÉM | PARÁ | Brasil | 1506807 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| d3c54ee3-9930-3cd0-970b-43b61779ccc8 | -15.5598 | -42.979698 | 2026-10-08 00:48:00 | METOP-C | PORTEIRINHA | MINAS GERAIS | Brasil | 3152204 | 31 | 33 | nan | nan | nan | Cerrado | nan |
| 9193d89a-4192-36fe-944c-b1a6acf92fc9 | -3.6581 | -57.091599 | 2026-10-08 00:48:00 | METOP-C | MAUÉS | AMAZONAS | Brasil | 1302900 | 13 | 33 | nan | nan | nan | Amazônia | nan |


[Clique aqui para ver as próximas entradas](README35.md)
