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

## Dados Diários - Página 17

| ID | Latitude | Longitude | Data/Hora GMT | Satélite | Município | Estado | País | Município ID | Estado ID | País ID | Dias sem Chuva | Precipitação | Risco de Fogo | Bioma | FRP |
|----|----------|-----------|---------------|----------|-----------|--------|------|--------------|-----------|---------|----------------|--------------|----------------|-------|-----|
| 6155c562-0a3d-303c-b257-23c47c407870 | -7.25159 | -44.6374 | 2025-06-18 04:38:00 | NOAA-20 | BENEDITO LEITE | MARANHÃO | Brasil | 2101806 | 21 | 33 | nan | nan | nan | Cerrado | 2.6 |
| c7b19a18-271f-3b82-aa90-36f2b2bff173 | -7.27979 | -50.00143 | 2025-06-18 04:38:00 | NOAA-20 | RIO MARIA | PARÁ | Brasil | 1506161 | 15 | 33 | nan | nan | nan | Amazônia | 1.6 |
| 90608e75-1fc4-33ab-af98-ad96758971a3 | -9.41251 | -48.42305 | 2025-06-18 04:38:00 | NOAA-20 | MIRACEMA DO TOCANTINS | TOCANTINS | Brasil | 1713205 | 17 | 33 | nan | nan | nan | Cerrado | 0.9 |
| f0e061c1-b6a6-35a6-89a4-107cd251130e | -9.32716 | -47.83053 | 2025-06-18 04:38:00 | NOAA-20 | PEDRO AFONSO | TOCANTINS | Brasil | 1716505 | 17 | 33 | nan | nan | nan | Cerrado | 0.9 |
| 3e22d7c8-874d-3eb7-9f61-1004c36785ec | -10.24102 | -52.23079 | 2025-06-18 04:38:00 | NOAA-20 | SANTA CRUZ DO XINGU | MATO GROSSO | Brasil | 5107743 | 51 | 33 | nan | nan | nan | Amazônia | 3.1 |
| 2efdcdd4-1abf-33d1-9f78-ccd868215bfc | -10.59468 | -49.45812 | 2025-06-18 04:38:00 | NOAA-20 | CRISTALÂNDIA | TOCANTINS | Brasil | 1706100 | 17 | 33 | nan | nan | nan | Cerrado | 0.4 |
| c1bbdc32-9270-3a1e-bf11-85eafd141803 | -7.29697 | -49.61373 | 2025-06-18 04:38:00 | NOAA-20 | RIO MARIA | PARÁ | Brasil | 1506161 | 15 | 33 | nan | nan | nan | Amazônia | 0.7 |
| c641521a-5647-3c3f-8841-152af1eb451f | -5.90759 | -43.45195 | 2025-06-18 04:38:00 | NOAA-20 | PARNARAMA | MARANHÃO | Brasil | 2107803 | 21 | 33 | nan | nan | nan | Cerrado | 8.9 |
| de301f27-5acb-357c-bc09-68d04b9d8fe0 | -10.46249 | -58.68854 | 2025-06-18 04:38:00 | NOAA-20 | JURUENA | MATO GROSSO | Brasil | 5105176 | 51 | 33 | nan | nan | nan | Amazônia | 1.5 |
| f6122899-f4fb-322e-911e-15f2ce6f52cb | -7.53969 | -45.65248 | 2025-06-18 04:38:00 | NOAA-20 | SAMBAÍBA | MARANHÃO | Brasil | 2109700 | 21 | 33 | nan | nan | nan | Cerrado | 3.7 |
| 3e365c70-0bcd-3c15-ad43-388655bbd650 | -9.26122 | -50.04067 | 2025-06-18 04:38:00 | NOAA-20 | SANTANA DO ARAGUAIA | PARÁ | Brasil | 1506708 | 15 | 33 | nan | nan | nan | Amazônia | 1.0 |
| fb5b85db-377a-3ae5-8d7e-22786201934a | -9.81688 | -48.10967 | 2025-06-18 04:38:00 | NOAA-20 | TOCANTÍNIA | TOCANTINS | Brasil | 1721109 | 17 | 33 | nan | nan | nan | Cerrado | 4.3 |
| 91144d2a-a48e-34e4-99b1-a0d2479f063f | -9.88692 | -47.80975 | 2025-06-18 04:38:00 | NOAA-20 | RIO SONO | TOCANTINS | Brasil | 1718758 | 17 | 33 | nan | nan | nan | Cerrado | 2.5 |
| d61f679b-93f2-3f5d-af4f-ca983b0cedae | -8.06956 | -43.10556 | 2025-06-18 04:38:00 | NOAA-20 | CANTO DO BURITI | PIAUÍ | Brasil | 2202307 | 22 | 33 | nan | nan | nan | Caatinga | 3.5 |
| cf3d039d-2b01-36ac-8111-2e2992ff8ee5 | -9.82126 | -47.1571 | 2025-06-18 04:38:00 | NOAA-20 | RIO SONO | TOCANTINS | Brasil | 1718758 | 17 | 33 | nan | nan | nan | Cerrado | 1.0 |
| 40f8dad6-420b-3651-925c-67650f522d2f | -6.66187 | -43.19009 | 2025-06-18 04:38:00 | NOAA-20 | BARÃO DE GRAJAÚ | MARANHÃO | Brasil | 2101509 | 21 | 33 | nan | nan | nan | Caatinga | 3.4 |
| 9e2b8aac-7a55-3b89-be25-5187874200e5 | -7.2324 | -43.0953 | 2025-06-18 04:38:00 | NOAA-20 | FLORIANO | PIAUÍ | Brasil | 2203909 | 22 | 33 | nan | nan | nan | Caatinga | 1.7 |
| 351fabeb-fdb8-3795-a232-6a39c77434af | -6.14144 | -42.96809 | 2025-06-18 04:38:00 | NOAA-20 | AMARANTE | PIAUÍ | Brasil | 2200509 | 22 | 33 | nan | nan | nan | Caatinga | 1.8 |
| 2da7a1d1-bb60-32b1-bdbe-e0b1a89be442 | -5.90877 | -43.44408 | 2025-06-18 04:38:00 | NOAA-20 | PARNARAMA | MARANHÃO | Brasil | 2107803 | 21 | 33 | nan | nan | nan | Cerrado | 1.3 |
| b0ec1a8f-ebb9-3e10-ae2f-7d18a8abab49 | -6.12815 | -42.54003 | 2025-06-18 04:38:00 | NOAA-20 | JARDIM DO MULATO | PIAUÍ | Brasil | 2205250 | 22 | 33 | nan | nan | nan | Caatinga | 3.5 |
| df816e87-e81b-31c7-8100-763f04eef734 | -9.41474 | -48.40827 | 2025-06-18 04:38:00 | NOAA-20 | MIRACEMA DO TOCANTINS | TOCANTINS | Brasil | 1713205 | 17 | 33 | nan | nan | nan | Cerrado | 1.6 |
| 6e19ab9b-9702-383f-92ed-135d019633d6 | -10.9218 | -56.84551 | 2025-06-18 04:38:00 | NOAA-20 | JUARA | MATO GROSSO | Brasil | 5105101 | 51 | 33 | nan | nan | nan | Amazônia | 7.7 |
| b492dcd1-b82a-34c4-b9b9-b89fd031f6e9 | -8.00371 | -46.80542 | 2025-06-18 04:38:00 | NOAA-20 | CAMPOS LINDOS | TOCANTINS | Brasil | 1703842 | 17 | 33 | nan | nan | nan | Cerrado | 0.5 |
| f057dcdb-b718-363a-9710-a45d88b50b12 | -6.41361 | -44.80072 | 2025-06-18 04:38:00 | NOAA-20 | MIRADOR | MARANHÃO | Brasil | 2106706 | 21 | 33 | nan | nan | nan | Cerrado | 2.6 |
| ef3c6558-a487-3e8e-b664-2a13795112ff | -6.1236 | -42.53936 | 2025-06-18 04:38:00 | NOAA-20 | JARDIM DO MULATO | PIAUÍ | Brasil | 2205250 | 22 | 33 | nan | nan | nan | Caatinga | 5.3 |
| ade6e918-bb06-350e-9da2-5f83523dc7e0 | -11.79116 | -43.78951 | 2025-06-18 04:38:00 | NOAA-20 | WANDERLEY | BAHIA | Brasil | 2933455 | 29 | 33 | nan | nan | nan | Cerrado | 1.2 |
| fdc7cff9-2059-3075-85e7-ea706f71b614 | -6.65748 | -43.18945 | 2025-06-18 04:38:00 | NOAA-20 | BARÃO DE GRAJAÚ | MARANHÃO | Brasil | 2101509 | 21 | 33 | nan | nan | nan | Caatinga | 4.8 |
| 89498708-b4a7-39ea-af7b-3d975af3ba52 | -8.01927 | -50.90751 | 2025-06-18 04:38:00 | NOAA-20 | CUMARU DO NORTE | PARÁ | Brasil | 1502764 | 15 | 33 | nan | nan | nan | Amazônia | 2.0 |
| 510174a3-de90-30ab-bd78-c414ac362c6b | -7.54347 | -45.65305 | 2025-06-18 04:38:00 | NOAA-20 | SAMBAÍBA | MARANHÃO | Brasil | 2109700 | 21 | 33 | nan | nan | nan | Cerrado | 7.6 |
| 4e7f0120-24be-3ab5-9a51-49ab3ad8b01f | -10.57892 | -49.64785 | 2025-06-18 04:38:00 | NOAA-20 | LAGOA DA CONFUSÃO | TOCANTINS | Brasil | 1711902 | 17 | 33 | nan | nan | nan | Cerrado | 1.4 |
| 5647c617-1d55-3af5-a72c-502a182872fa | -8.30851 | -55.10303 | 2025-06-18 04:38:00 | NOAA-20 | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 1.7 |
| 5b8871c3-48ee-3c54-9e28-feabb6db3356 | -11.13291 | -53.94068 | 2025-06-18 04:38:00 | NOAA-20 | MARCELÂNDIA | MATO GROSSO | Brasil | 5105580 | 51 | 33 | nan | nan | nan | Amazônia | 14.5 |
| 0d7a1b91-73c2-306c-8eaf-ae284766c269 | -9.46187 | -57.85426 | 2025-06-18 04:38:00 | NOAA-20 | APIACÁS | MATO GROSSO | Brasil | 5100805 | 51 | 33 | nan | nan | nan | Amazônia | 1.2 |
| bbcec6d5-c3b4-3e43-8d6a-9588bd7baae5 | -10.66017 | -49.36635 | 2025-06-18 04:38:00 | NOAA-20 | CRISTALÂNDIA | TOCANTINS | Brasil | 1706100 | 17 | 33 | nan | nan | nan | Cerrado | 15.6 |
| 369b6861-9504-3adf-8927-4e383ca0404c | -8.13402 | -47.98896 | 2025-06-18 04:38:00 | NOAA-20 | ITAPIRATINS | TOCANTINS | Brasil | 1710904 | 17 | 33 | nan | nan | nan | Cerrado | 0.9 |
| 8a56e923-497b-3273-b5c8-a309527b9aab | -10.35998 | -57.25035 | 2025-06-18 04:38:00 | NOAA-20 | JUARA | MATO GROSSO | Brasil | 5105101 | 51 | 33 | nan | nan | nan | Amazônia | 1.3 |
| 1b505cd7-9c5f-34dd-afac-0a945bc80d5e | -8.87966 | -47.41698 | 2025-06-18 04:38:00 | NOAA-20 | CENTENÁRIO | TOCANTINS | Brasil | 1704105 | 17 | 33 | nan | nan | nan | Cerrado | 0.7 |
| 7036364f-8058-3b0f-bde3-9db7c5b27856 | -11.56891 | -44.6731 | 2025-06-18 04:38:00 | NOAA-20 | COTEGIPE | BAHIA | Brasil | 2909406 | 29 | 33 | nan | nan | nan | Cerrado | 2.4 |
| 267de9e9-8492-328d-83c0-818cb593b703 | -6.03377 | -44.05094 | 2025-06-18 04:38:00 | NOAA-20 | COLINAS | MARANHÃO | Brasil | 2103505 | 21 | 33 | nan | nan | nan | Cerrado | 0.9 |
| d39a7d0d-2407-3167-933c-fd62f8c7ed70 | -5.61442 | -45.97391 | 2025-06-18 04:38:00 | NOAA-20 | GRAJAÚ | MARANHÃO | Brasil | 2104800 | 21 | 33 | nan | nan | nan | Cerrado | 1.9 |
| bccf0f72-c135-3901-9a1f-520af47f599b | -8.72045 | -49.02393 | 2025-06-18 04:38:00 | NOAA-20 | GOIANORTE | TOCANTINS | Brasil | 1708304 | 17 | 33 | nan | nan | nan | Cerrado | 2.5 |
| dfcd7ff7-daa3-3079-a7bf-aa9b42653082 | -11.14028 | -53.91962 | 2025-06-18 04:38:00 | NOAA-20 | MARCELÂNDIA | MATO GROSSO | Brasil | 5105580 | 51 | 33 | nan | nan | nan | Amazônia | 1.3 |
| 3fb22874-4308-36fa-8432-c2c67bab4eee | -5.91303 | -43.44472 | 2025-06-18 04:38:00 | NOAA-20 | LAGOA DO MATO | MARANHÃO | Brasil | 2105922 | 21 | 33 | nan | nan | nan | Cerrado | 8.9 |
| 044faf00-3d76-3570-aea7-b972141506ca | -9.87993 | -47.8088 | 2025-06-18 04:38:00 | NOAA-20 | RIO SONO | TOCANTINS | Brasil | 1718758 | 17 | 33 | nan | nan | nan | Cerrado | 0.9 |
| 4573837b-a4f4-3a2d-a3c9-b89f44d60dbd | -11.13582 | -53.94565 | 2025-06-18 04:38:00 | NOAA-20 | MARCELÂNDIA | MATO GROSSO | Brasil | 5105580 | 51 | 33 | nan | nan | nan | Amazônia | 10.7 |
| 7b201432-3068-3cd3-8763-99291276a5c8 | -8.67047 | -51.46552 | 2025-06-18 04:38:00 | NOAA-20 | CUMARU DO NORTE | PARÁ | Brasil | 1502764 | 15 | 33 | nan | nan | nan | Amazônia | 0.9 |
| 5a5150aa-03a2-3ca6-ad55-2572b6b7be84 | -10.46195 | -58.69145 | 2025-06-18 04:38:00 | NOAA-20 | JURUENA | MATO GROSSO | Brasil | 5105176 | 51 | 33 | nan | nan | nan | Amazônia | 1.5 |
| 9ecf03b9-e7b4-383e-958e-3e77836c3ae5 | -8.07407 | -43.10617 | 2025-06-18 04:38:00 | NOAA-20 | CANTO DO BURITI | PIAUÍ | Brasil | 2202307 | 22 | 33 | nan | nan | nan | Caatinga | 9.1 |
| 29c27802-3969-32ad-92e8-2e3bcaff2cc9 | -10.35712 | -57.24027 | 2025-06-18 04:38:00 | NOAA-20 | JUARA | MATO GROSSO | Brasil | 5105101 | 51 | 33 | nan | nan | nan | Amazônia | 2.0 |
| 62214400-4376-316c-8f69-db676a7f3da8 | -7.43923 | -44.90356 | 2025-06-18 04:38:00 | NOAA-20 | URUÇUÍ | PIAUÍ | Brasil | 2211209 | 22 | 33 | nan | nan | nan | Cerrado | 1.2 |
| 1cc99821-98a7-3538-8f4b-ec676527dde5 | -9.26176 | -50.03719 | 2025-06-18 04:38:00 | NOAA-20 | SANTANA DO ARAGUAIA | PARÁ | Brasil | 1506708 | 15 | 33 | nan | nan | nan | Amazônia | 2.5 |
| b187dd85-4a76-382d-aef8-5757ebe0a07e | -8.06828 | -43.11466 | 2025-06-18 04:38:00 | NOAA-20 | CANTO DO BURITI | PIAUÍ | Brasil | 2202307 | 22 | 33 | nan | nan | nan | Caatinga | 1.2 |
| e7200623-f5f4-3dc6-9a27-16951f6c42fe | -10.98984 | -45.09315 | 2025-06-18 04:38:00 | NOAA-20 | FORMOSA DO RIO PRETO | BAHIA | Brasil | 2911105 | 29 | 33 | nan | nan | nan | Cerrado | 1.9 |
| 0f7f7e56-29db-368e-b0c2-b8ca73ecf3cb | -9.41762 | -48.43514 | 2025-06-18 04:38:00 | NOAA-20 | MIRACEMA DO TOCANTINS | TOCANTINS | Brasil | 1713205 | 17 | 33 | nan | nan | nan | Cerrado | 3.1 |
| 5587eb03-e973-3462-9e5a-1ab8bf4cef78 | -10.57782 | -49.65492 | 2025-06-18 04:38:00 | NOAA-20 | LAGOA DA CONFUSÃO | TOCANTINS | Brasil | 1711902 | 17 | 33 | nan | nan | nan | Cerrado | 1.0 |
| a90cb104-7a50-32bc-82f2-e253ed7f2d12 | -9.27632 | -49.61848 | 2025-06-18 04:38:00 | NOAA-20 | ABREULÂNDIA | TOCANTINS | Brasil | 1700251 | 17 | 33 | nan | nan | nan | Cerrado | 1.0 |
| 6387f63d-6233-3146-94a3-44be8381a90b | -7.54316 | -45.65496 | 2025-06-18 04:38:00 | NOAA-20 | SAMBAÍBA | MARANHÃO | Brasil | 2109700 | 21 | 33 | nan | nan | nan | Cerrado | 4.9 |
| c56b7ce0-0c4f-3526-b363-449cbf753364 | -7.54834 | -45.64632 | 2025-06-18 04:38:00 | NOAA-20 | SAMBAÍBA | MARANHÃO | Brasil | 2109700 | 21 | 33 | nan | nan | nan | Cerrado | 4.8 |
| 76f06c9e-451d-3b05-983f-be738e049760 | -12.23452 | -44.20644 | 2025-06-18 04:38:00 | NOAA-20 | CRISTÓPOLIS | BAHIA | Brasil | 2909703 | 29 | 33 | nan | nan | nan | Cerrado | 2.5 |
| a48b4cac-5e52-34a8-a14f-00cfb0b4108b | -7.26011 | -44.63525 | 2025-06-18 04:38:00 | NOAA-20 | BENEDITO LEITE | MARANHÃO | Brasil | 2101806 | 21 | 33 | nan | nan | nan | Cerrado | 0.5 |
| 5b8a0458-b6f3-3ed5-b17b-47a28dd3b1ae | -7.61229 | -45.55412 | 2025-06-18 04:38:00 | NOAA-20 | SAMBAÍBA | MARANHÃO | Brasil | 2109700 | 21 | 33 | nan | nan | nan | Cerrado | 0.7 |
| 9c06a24a-495c-3205-a735-91ea6a0d2223 | -7.1455 | -46.55156 | 2025-06-18 04:38:00 | NOAA-20 | FEIRA NOVA DO MARANHÃO | MARANHÃO | Brasil | 2104073 | 21 | 33 | nan | nan | nan | Cerrado | 0.5 |
| 7f5d1505-49dd-3217-8e78-7bfda06eabca | -7.53938 | -45.6544 | 2025-06-18 04:38:00 | NOAA-20 | SAMBAÍBA | MARANHÃO | Brasil | 2109700 | 21 | 33 | nan | nan | nan | Cerrado | 2.9 |
| b6f778b5-b112-3229-8a47-76cdc2cbddd6 | -9.26209 | -46.56255 | 2025-06-18 04:38:00 | NOAA-20 | ALTO PARNAÍBA | MARANHÃO | Brasil | 2100501 | 21 | 33 | nan | nan | nan | Cerrado | 0.6 |
| c4bd6ccb-4da5-3f8e-ba9c-f8161c64df8f | -9.26783 | -50.04172 | 2025-06-18 04:38:00 | NOAA-20 | SANTANA DO ARAGUAIA | PARÁ | Brasil | 1506708 | 15 | 33 | nan | nan | nan | Amazônia | 1.1 |
| 628f3fdd-68c6-3051-9430-72717bc975d5 | -10.63409 | -49.42425 | 2025-06-18 04:38:00 | NOAA-20 | CRISTALÂNDIA | TOCANTINS | Brasil | 1706100 | 17 | 33 | nan | nan | nan | Cerrado | 2.5 |
| 82ae534a-b899-319d-97f0-290a77ead6d6 | -10.86545 | -53.77042 | 2025-06-18 04:38:00 | NOAA-20 | MARCELÂNDIA | MATO GROSSO | Brasil | 5105580 | 51 | 33 | nan | nan | nan | Amazônia | 1.1 |
| 29be613f-baf1-3078-af03-fafcbe7b586f | -9.26067 | -50.04414 | 2025-06-18 04:38:00 | NOAA-20 | SANTANA DO ARAGUAIA | PARÁ | Brasil | 1506708 | 15 | 33 | nan | nan | nan | Amazônia | 1.0 |
| 61acf259-9a59-3931-9392-b8acb61520a3 | -7.08166 | -44.38332 | 2025-06-18 04:38:00 | NOAA-20 | BENEDITO LEITE | MARANHÃO | Brasil | 2101806 | 21 | 33 | nan | nan | nan | Cerrado | 1.3 |
| b2e07119-cb8c-30a4-b999-6396eed2882f | -8.71766 | -49.01986 | 2025-06-18 04:38:00 | NOAA-20 | GOIANORTE | TOCANTINS | Brasil | 1708304 | 17 | 33 | nan | nan | nan | Cerrado | 1.7 |
| 58204176-3164-333d-918e-ef1fda5070a1 | -6.31791 | -43.74584 | 2025-06-18 04:38:00 | NOAA-20 | SÃO JOÃO DOS PATOS | MARANHÃO | Brasil | 2111102 | 21 | 33 | nan | nan | nan | Cerrado | 1.5 |
| 6f67b3e7-bd04-3d92-849d-6af56aee5872 | -10.07268 | -52.7421 | 2025-06-18 04:38:00 | NOAA-20 | SANTA CRUZ DO XINGU | MATO GROSSO | Brasil | 5107743 | 51 | 33 | nan | nan | nan | Amazônia | 0.5 |
| dea3d612-017b-343c-aba2-45ac0b92b051 | -4.81478 | -47.32396 | 2025-06-18 04:38:00 | NOAA-20 | AÇAILÂNDIA | MARANHÃO | Brasil | 2100055 | 21 | 33 | nan | nan | nan | Amazônia | 1.4 |
| 8987f27f-81b8-3d1c-9fbb-c8797de89ab3 | -11.57542 | -44.84364 | 2025-06-18 04:38:00 | NOAA-20 | RIACHÃO DAS NEVES | BAHIA | Brasil | 2926202 | 29 | 33 | nan | nan | nan | Cerrado | 1.1 |
| d7488ce1-7673-3c7e-af8e-e5d40ba1457e | -10.98372 | -45.10728 | 2025-06-18 04:38:00 | NOAA-20 | FORMOSA DO RIO PRETO | BAHIA | Brasil | 2911105 | 29 | 33 | nan | nan | nan | Cerrado | 1.3 |
| 1dba0ab9-f480-3c8e-b9e0-2c3348dd55d7 | -9.33004 | -47.8349 | 2025-06-18 04:38:00 | NOAA-20 | PEDRO AFONSO | TOCANTINS | Brasil | 1716505 | 17 | 33 | nan | nan | nan | Cerrado | 1.9 |
| 283de06a-ce37-33a9-bb49-135c1855575f | -8.67384 | -51.46607 | 2025-06-18 04:38:00 | NOAA-20 | CUMARU DO NORTE | PARÁ | Brasil | 1502764 | 15 | 33 | nan | nan | nan | Amazônia | 0.8 |
| 8997bf9a-f407-357a-99bb-ae2d1c18456a | -7.54525 | -45.64117 | 2025-06-18 04:38:00 | NOAA-20 | SAMBAÍBA | MARANHÃO | Brasil | 2109700 | 21 | 33 | nan | nan | nan | Cerrado | 2.3 |
| 003420a7-bd2c-3a7d-a435-def23fc7c0fb | -4.81112 | -46.82542 | 2025-06-18 04:38:00 | NOAA-20 | BOM JESUS DAS SELVAS | MARANHÃO | Brasil | 2102036 | 21 | 33 | nan | nan | nan | Amazônia | 0.6 |
| 31dc5550-43b9-3f2d-bccd-25ccd7caa530 | -6.67574 | -43.21778 | 2025-06-18 04:38:00 | NOAA-20 | BARÃO DE GRAJAÚ | MARANHÃO | Brasil | 2101509 | 21 | 33 | nan | nan | nan | Caatinga | 4.1 |
| d30fa061-020e-3ac5-94dd-da42e5350dd5 | -7.42191 | -47.65477 | 2025-06-18 04:38:00 | NOAA-20 | FILADÉLFIA | TOCANTINS | Brasil | 1707702 | 17 | 33 | nan | nan | nan | Cerrado | 0.9 |
| b9daa8c2-facf-3cb5-aa1f-9322e2dcd142 | -9.4233 | -44.72819 | 2025-06-18 04:38:00 | NOAA-20 | REDENÇÃO DO GURGUÉIA | PIAUÍ | Brasil | 2208700 | 22 | 33 | nan | nan | nan | Cerrado | 1.8 |
| e64727f6-5978-3c98-80a1-e69157a73236 | -7.44049 | -44.90148 | 2025-06-18 04:38:00 | NOAA-20 | URUÇUÍ | PIAUÍ | Brasil | 2211209 | 22 | 33 | nan | nan | nan | Cerrado | 1.7 |
| 196ef95b-cfcf-3026-8a5e-4a564189741a | -9.49128 | -56.08414 | 2025-06-18 04:38:00 | NOAA-20 | ALTA FLORESTA | MATO GROSSO | Brasil | 5100250 | 51 | 33 | nan | nan | nan | Amazônia | 16.4 |
| 8b25a3e2-1c42-3b96-8494-30ceb0e05b89 | -10.95202 | -49.25388 | 2025-06-18 04:38:00 | NOAA-20 | SANTA RITA DO TOCANTINS | TOCANTINS | Brasil | 1718899 | 17 | 33 | nan | nan | nan | Cerrado | 2.4 |
| d2c75e9a-4ad6-38cf-bfa3-8747f5d831ab | -7.08164 | -44.38346 | 2025-06-18 04:38:00 | NOAA-20 | BENEDITO LEITE | MARANHÃO | Brasil | 2101806 | 21 | 33 | nan | nan | nan | Cerrado | 1.3 |
| 3dfc53c2-aadd-3dc4-a87a-15244637fec7 | -6.67189 | -43.18277 | 2025-06-18 04:38:00 | NOAA-20 | BARÃO DE GRAJAÚ | MARANHÃO | Brasil | 2101509 | 21 | 33 | nan | nan | nan | Caatinga | 1.9 |
| 809983aa-fb54-362d-8988-0a44c978e796 | -7.80776 | -46.57082 | 2025-06-18 04:38:00 | NOAA-20 | RIACHÃO | MARANHÃO | Brasil | 2109502 | 21 | 33 | nan | nan | nan | Cerrado | 7.1 |
| c0c171b4-6fc0-32b2-9b38-cd4405030f1b | -4.82157 | -47.32505 | 2025-06-18 04:38:00 | NOAA-20 | AÇAILÂNDIA | MARANHÃO | Brasil | 2100055 | 21 | 33 | nan | nan | nan | Amazônia | 1.1 |
| e8a17dad-1ff6-3a55-b1ff-50bb33e14519 | -5.89907 | -43.45071 | 2025-06-18 04:38:00 | NOAA-20 | PARNARAMA | MARANHÃO | Brasil | 2107803 | 21 | 33 | nan | nan | nan | Cerrado | 0.8 |
| 80445f5a-5cbc-332e-9f5b-192f164c62ac | -8.72433 | -49.02091 | 2025-06-18 04:38:00 | NOAA-20 | GOIANORTE | TOCANTINS | Brasil | 1708304 | 17 | 33 | nan | nan | nan | Cerrado | 7.5 |
| 2d3f8824-6563-3fb2-ba60-befc7c0c4319 | -10.50512 | -46.43376 | 2025-06-18 04:38:00 | NOAA-20 | MATEIROS | TOCANTINS | Brasil | 1712702 | 17 | 33 | nan | nan | nan | Cerrado | 0.6 |
| 939a3e7a-1a09-3a37-ae1e-23cdbf9707cb | -9.32657 | -47.8344 | 2025-06-18 04:38:00 | NOAA-20 | PEDRO AFONSO | TOCANTINS | Brasil | 1716505 | 17 | 33 | nan | nan | nan | Cerrado | 0.9 |
| f6df8c60-35c4-39b6-8229-45fef70c7636 | -9.46206 | -57.84967 | 2025-06-18 04:38:00 | NOAA-20 | APIACÁS | MATO GROSSO | Brasil | 5100805 | 51 | 33 | nan | nan | nan | Amazônia | 2.2 |
| 01b45bc3-45aa-35ad-ac12-a3ef2c8ed73c | -10.98523 | -45.09624 | 2025-06-18 04:38:00 | NOAA-20 | FORMOSA DO RIO PRETO | BAHIA | Brasil | 2911105 | 29 | 33 | nan | nan | nan | Cerrado | 2.3 |
| 45ab893e-6296-329e-89b3-cb7bcf939c7b | -11.33472 | -45.2115 | 2025-06-18 04:38:00 | NOAA-20 | FORMOSA DO RIO PRETO | BAHIA | Brasil | 2911105 | 29 | 33 | nan | nan | nan | Cerrado | 1.1 |
| 300b31cb-1007-3728-94b6-6e07741ed6c3 | -6.37306 | -43.75032 | 2025-06-18 04:38:00 | NOAA-20 | SÃO JOÃO DOS PATOS | MARANHÃO | Brasil | 2111102 | 21 | 33 | nan | nan | nan | Cerrado | 4.4 |
| 0ab0f6f6-d8ab-3e78-81e1-ad4f67c2fb8b | -3.72326 | -53.99382 | 2025-06-18 04:38:00 | NOAA-20 | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | 0.5 |
| 6c7752fb-31e0-3cb7-927b-255e8f210135 | -9.26398 | -50.04467 | 2025-06-18 04:38:00 | NOAA-20 | SANTANA DO ARAGUAIA | PARÁ | Brasil | 1506708 | 15 | 33 | nan | nan | nan | Amazônia | 1.0 |
| 86cdb872-48a5-3621-b6cd-d49eb666800c | -10.72865 | -49.55948 | 2025-06-18 04:38:00 | NOAA-20 | LAGOA DA CONFUSÃO | TOCANTINS | Brasil | 1711902 | 17 | 33 | nan | nan | nan | Cerrado | 2.0 |


[Clique aqui para ver as próximas entradas](README18.md)
