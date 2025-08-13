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

## Dados Diários - Página 19

| ID | Latitude | Longitude | Data/Hora GMT | Satélite | Município | Estado | País | Município ID | Estado ID | País ID | Dias sem Chuva | Precipitação | Risco de Fogo | Bioma | FRP |
|----|----------|-----------|---------------|----------|-----------|--------|------|--------------|-----------|---------|----------------|--------------|----------------|-------|-----|
| 6360f888-c9f8-3f33-af63-d5e3e0394102 | -12.68849 | -46.96323 | 2025-08-13 04:40:00 | NOAA-21 | ARRAIAS | TOCANTINS | Brasil | 1702406 | 17 | 33 | nan | nan | nan | Cerrado | 2.2 |
| a43862ec-0d5e-3511-ab38-bb4f36efb0ec | -8.11652 | -55.57306 | 2025-08-13 04:40:00 | NOAA-21 | NOVO PROGRESSO | PARÁ | Brasil | 1505031 | 15 | 33 | nan | nan | nan | Amazônia | 2.7 |
| ae00322e-6975-3732-a840-bc9c0898576e | -11.63719 | -50.14413 | 2025-08-13 04:40:00 | NOAA-21 | FORMOSO DO ARAGUAIA | TOCANTINS | Brasil | 1708205 | 17 | 33 | nan | nan | nan | Cerrado | 1.0 |
| f6259e2b-0594-3f46-9c45-6dec85a29269 | -12.49094 | -46.96638 | 2025-08-13 04:40:00 | NOAA-21 | ARRAIAS | TOCANTINS | Brasil | 1702406 | 17 | 33 | nan | nan | nan | Cerrado | 5.6 |
| 3f725cd9-37eb-3413-8164-e89af69e7e06 | -10.35583 | -50.81922 | 2025-08-13 04:40:00 | NOAA-21 | SANTA TEREZINHA | MATO GROSSO | Brasil | 5107776 | 51 | 33 | nan | nan | nan | Cerrado | 2.3 |
| dfcd9d03-bc4f-3d2b-8b82-63edca907e61 | -6.27843 | -53.63088 | 2025-08-13 04:40:00 | NOAA-21 | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 1.6 |
| 266eca51-63a4-340c-a3f7-591cee628b9b | -10.00699 | -59.21551 | 2025-08-13 04:40:00 | NOAA-21 | ARIPUANÃ | MATO GROSSO | Brasil | 5101407 | 51 | 33 | nan | nan | nan | Amazônia | 1.0 |
| 81ae9579-1895-323a-a8a5-c66ddeea7c3d | -5.8498 | -59.91751 | 2025-08-13 04:40:00 | NOAA-21 | NOVO ARIPUANÃ | AMAZONAS | Brasil | 1303304 | 13 | 33 | nan | nan | nan | Amazônia | 1.8 |
| 703e7e14-424e-399d-b8f1-cec3158d6aa5 | -12.53045 | -46.98672 | 2025-08-13 04:40:00 | NOAA-21 | ARRAIAS | TOCANTINS | Brasil | 1702406 | 17 | 33 | nan | nan | nan | Cerrado | 8.8 |
| f4056966-3117-3c25-91b8-a3d931d07284 | -6.91646 | -59.13544 | 2025-08-13 04:40:00 | NOAA-21 | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 1.3 |
| e97a4923-49ca-3d22-b995-a819ee13d91c | -12.14855 | -48.01715 | 2025-08-13 04:40:00 | NOAA-21 | PARANÃ | TOCANTINS | Brasil | 1716208 | 17 | 33 | nan | nan | nan | Cerrado | 0.6 |
| cc4f50d7-54e8-3d31-b789-65a2ce411495 | -6.86899 | -59.15197 | 2025-08-13 04:40:00 | NOAA-21 | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 19.0 |
| 7aa1c5c5-ef4f-3b66-bdcf-3ab31710f13e | -6.10562 | -59.9245 | 2025-08-13 04:40:00 | NOAA-21 | NOVO ARIPUANÃ | AMAZONAS | Brasil | 1303304 | 13 | 33 | nan | nan | nan | Amazônia | 1.7 |
| cdbb1886-599d-31d6-b8b1-29cfe151bdbf | -5.88349 | -57.74138 | 2025-08-13 04:40:00 | NOAA-21 | JACAREACANGA | PARÁ | Brasil | 1503754 | 15 | 33 | nan | nan | nan | Amazônia | 2.7 |
| 41ff9db4-025a-3d10-bf31-5943fedb1ae5 | -7.12845 | -60.12982 | 2025-08-13 04:40:00 | NOAA-21 | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 15.0 |
| 36b469d0-636c-3aad-a540-9da86af9d9c6 | -12.50226 | -46.96812 | 2025-08-13 04:40:00 | NOAA-21 | ARRAIAS | TOCANTINS | Brasil | 1702406 | 17 | 33 | nan | nan | nan | Cerrado | 2.5 |
| f5e91766-1b41-3c35-ba24-ff4c42fd3eed | -11.72129 | -50.12845 | 2025-08-13 04:40:00 | NOAA-21 | FORMOSO DO ARAGUAIA | TOCANTINS | Brasil | 1708205 | 17 | 33 | nan | nan | nan | Cerrado | 0.3 |
| 5540df6d-0db3-3354-ad1f-588082624488 | -6.86909 | -59.13914 | 2025-08-13 04:40:00 | NOAA-21 | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 6.2 |
| 76e9215b-4594-3b6c-981c-116cca3bb127 | -5.85484 | -59.92257 | 2025-08-13 04:40:00 | NOAA-21 | NOVO ARIPUANÃ | AMAZONAS | Brasil | 1303304 | 13 | 33 | nan | nan | nan | Amazônia | 1.0 |
| acb5cecc-c7f0-347d-9441-18e07f7ee459 | -5.88302 | -57.74417 | 2025-08-13 04:40:00 | NOAA-21 | JACAREACANGA | PARÁ | Brasil | 1503754 | 15 | 33 | nan | nan | nan | Amazônia | 2.7 |
| deb67671-496f-3f56-9730-fcc1968f98c6 | -8.57013 | -54.71183 | 2025-08-13 04:40:00 | NOAA-21 | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 1.1 |
| bef683e5-6eb9-35f5-862d-05ebe37787bf | -5.7351 | -51.68871 | 2025-08-13 04:40:00 | NOAA-21 | SÃO FÉLIX DO XINGU | PARÁ | Brasil | 1507300 | 15 | 33 | nan | nan | nan | Amazônia | 2.0 |
| cee355b1-a172-307d-949d-a23c6e22249d | -8.11172 | -55.5762 | 2025-08-13 04:40:00 | NOAA-21 | NOVO PROGRESSO | PARÁ | Brasil | 1505031 | 15 | 33 | nan | nan | nan | Amazônia | 2.7 |
| d2e945aa-fd3a-338c-8492-9bad12ab88c8 | -12.52402 | -46.97902 | 2025-08-13 04:40:00 | NOAA-21 | ARRAIAS | TOCANTINS | Brasil | 1702406 | 17 | 33 | nan | nan | nan | Cerrado | 7.4 |
| 103f5742-e39e-3d5e-b07b-acc9681ff96d | -9.19271 | -59.66444 | 2025-08-13 04:40:00 | NOAA-21 | COLNIZA | MATO GROSSO | Brasil | 5103254 | 51 | 33 | nan | nan | nan | Amazônia | 5.3 |
| d859e809-58b0-3404-bed9-52941deaca65 | -6.89964 | -59.13623 | 2025-08-13 04:40:00 | NOAA-21 | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 18.5 |
| fb1ec0e0-9833-3bde-905a-edc98af99d5d | -5.84328 | -59.92062 | 2025-08-13 04:40:00 | NOAA-21 | NOVO ARIPUANÃ | AMAZONAS | Brasil | 1303304 | 13 | 33 | nan | nan | nan | Amazônia | 1.8 |
| 020718fb-5847-316f-b8b9-ed74a62976d2 | -11.91365 | -52.54129 | 2025-08-13 04:40:00 | NOAA-21 | QUERÊNCIA | MATO GROSSO | Brasil | 5107065 | 51 | 33 | nan | nan | nan | Amazônia | 1.3 |
| d400ed66-d8e6-3ee0-af23-5260a72251e2 | -12.57814 | -46.97814 | 2025-08-13 04:40:00 | NOAA-21 | ARRAIAS | TOCANTINS | Brasil | 1702406 | 17 | 33 | nan | nan | nan | Cerrado | 7.2 |
| 348c572f-5367-3e30-965a-bd030187b1c1 | -12.68781 | -46.96806 | 2025-08-13 04:40:00 | NOAA-21 | ARRAIAS | TOCANTINS | Brasil | 1702406 | 17 | 33 | nan | nan | nan | Cerrado | 2.2 |
| deb02b1f-c530-3529-8487-8f6739c29bfa | -6.10634 | -59.92044 | 2025-08-13 04:40:00 | NOAA-21 | NOVO ARIPUANÃ | AMAZONAS | Brasil | 1303304 | 13 | 33 | nan | nan | nan | Amazônia | 1.7 |
| 895503d9-bbb7-3cb5-8e27-fd1183d79f86 | -8.11716 | -55.56923 | 2025-08-13 04:40:00 | NOAA-21 | NOVO PROGRESSO | PARÁ | Brasil | 1505031 | 15 | 33 | nan | nan | nan | Amazônia | 1.4 |
| 66e17e64-edea-3d96-aaa3-ff34fc1908e6 | -7.12783 | -60.12629 | 2025-08-13 04:40:00 | NOAA-21 | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 8.2 |
| 0a2cc5df-0aae-30c5-bb5c-decfd8d8052e | -9.1807 | -59.66935 | 2025-08-13 04:40:00 | NOAA-21 | COLNIZA | MATO GROSSO | Brasil | 5103254 | 51 | 33 | nan | nan | nan | Amazônia | 2.3 |
| ce3cf492-5b8c-301b-b80a-a9d991d0654f | -6.97491 | -59.28819 | 2025-08-13 04:40:00 | NOAA-21 | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 2.1 |
| c2912f95-bbb2-3ca2-b76a-1c3936787982 | -5.8541 | -59.92666 | 2025-08-13 04:40:00 | NOAA-21 | NOVO ARIPUANÃ | AMAZONAS | Brasil | 1303304 | 13 | 33 | nan | nan | nan | Amazônia | 1.6 |
| ba34fcbc-2c02-321c-9150-1cccf29cf1e1 | -9.05644 | -45.08023 | 2025-08-13 04:40:00 | NOAA-21 | BOM JESUS | PIAUÍ | Brasil | 2201903 | 22 | 33 | nan | nan | nan | Cerrado | 1.3 |
| aefb4131-e60a-3957-90c2-f67c29ec7f63 | -7.06444 | -44.36349 | 2025-08-13 04:40:00 | NOAA-21 | BENEDITO LEITE | MARANHÃO | Brasil | 2101806 | 21 | 33 | nan | nan | nan | Cerrado | 2.2 |
| b5ae85a4-6a0c-3f21-a623-8e9374001fd8 | -10.34921 | -50.81816 | 2025-08-13 04:40:00 | NOAA-21 | SANTA TEREZINHA | MATO GROSSO | Brasil | 5107776 | 51 | 33 | nan | nan | nan | Cerrado | 1.4 |
| 59b993dd-14af-3af7-99f0-4839676c5b1c | -6.61189 | -43.88453 | 2025-08-13 04:40:00 | NOAA-21 | NOVA IORQUE | MARANHÃO | Brasil | 2107308 | 21 | 33 | nan | nan | nan | Cerrado | 10.8 |
| 492772dc-afaa-3827-9843-2fb551de6fb2 | -6.90153 | -59.12566 | 2025-08-13 04:40:00 | NOAA-21 | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 13.3 |
| 3a936149-93aa-3b9a-8bdc-75638cdb800d | -9.05905 | -60.64632 | 2025-08-13 04:40:00 | NOAA-21 | COLNIZA | MATO GROSSO | Brasil | 5103254 | 51 | 33 | nan | nan | nan | Amazônia | 4.8 |
| 2009711c-260d-31cd-ab6a-4e58be1f490b | -8.56504 | -54.67035 | 2025-08-13 04:40:00 | NOAA-21 | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 1.5 |
| b0a70ad8-6f96-3bbf-b018-061b74236d45 | -9.16865 | -59.67445 | 2025-08-13 04:40:00 | NOAA-21 | COLNIZA | MATO GROSSO | Brasil | 5103254 | 51 | 33 | nan | nan | nan | Amazônia | 4.0 |
| f8bec7ce-f6f7-3412-a4a5-97e15cb14767 | -12.53423 | -46.98727 | 2025-08-13 04:40:00 | NOAA-21 | ARRAIAS | TOCANTINS | Brasil | 1702406 | 17 | 33 | nan | nan | nan | Cerrado | 8.8 |
| 0f1e6a69-b594-3ab6-931a-5c7beffaccca | -12.57893 | -47.05457 | 2025-08-13 04:40:00 | NOAA-21 | ARRAIAS | TOCANTINS | Brasil | 1702406 | 17 | 33 | nan | nan | nan | Cerrado | 2.2 |
| 52c5d939-e5b1-31f0-9c92-1b323487c4a5 | -6.28148 | -53.63604 | 2025-08-13 04:40:00 | NOAA-21 | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 2.8 |
| 89da4d87-2d49-3079-beef-78d53a556c8e | -6.07322 | -59.93961 | 2025-08-13 04:40:00 | NOAA-21 | NOVO ARIPUANÃ | AMAZONAS | Brasil | 1303304 | 13 | 33 | nan | nan | nan | Amazônia | 2.4 |
| 82916149-2305-32c6-9d69-48703790bf71 | -9.06324 | -60.65545 | 2025-08-13 04:40:00 | NOAA-21 | COLNIZA | MATO GROSSO | Brasil | 5103254 | 51 | 33 | nan | nan | nan | Amazônia | 7.6 |
| 98241a8e-451c-35ed-b397-627a38d533fd | -9.05828 | -60.65034 | 2025-08-13 04:40:00 | NOAA-21 | COLNIZA | MATO GROSSO | Brasil | 5103254 | 51 | 33 | nan | nan | nan | Amazônia | 6.3 |
| ff75ac78-fbbc-31cd-9424-462da11eb4ad | -12.47583 | -46.96408 | 2025-08-13 04:40:00 | NOAA-21 | ARRAIAS | TOCANTINS | Brasil | 1702406 | 17 | 33 | nan | nan | nan | Cerrado | 1.7 |
| 40b9d2d8-84b4-313a-8791-05714141a941 | -7.0767 | -59.19828 | 2025-08-13 04:40:00 | NOAA-21 | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 1.9 |
| 5e09ef73-2833-3714-8037-efc8a3e39acc | -13.02772 | -48.40693 | 2025-08-13 04:40:00 | NOAA-21 | PALMEIRÓPOLIS | TOCANTINS | Brasil | 1715754 | 17 | 33 | nan | nan | nan | Cerrado | 1.6 |
| 39acba2f-582d-3586-a2ab-3cd1a537b602 | -10.18544 | -49.50956 | 2025-08-13 04:40:00 | NOAA-21 | PIUM | TOCANTINS | Brasil | 1717503 | 17 | 33 | nan | nan | nan | Cerrado | 0.3 |
| 422e32ca-a050-30ed-ba37-d63777b1fa84 | -6.87086 | -59.14161 | 2025-08-13 04:40:00 | NOAA-21 | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 9.0 |
| 47dd759d-4c4b-3e38-9e08-7004505500a1 | -7.12854 | -60.12227 | 2025-08-13 04:40:00 | NOAA-21 | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 8.2 |
| 09d3a831-19e5-3582-991a-6dda070748ec | -12.59263 | -46.98476 | 2025-08-13 04:40:00 | NOAA-21 | ARRAIAS | TOCANTINS | Brasil | 1702406 | 17 | 33 | nan | nan | nan | Cerrado | 1.3 |
| 3ee6b8bb-14eb-3f76-a598-57b7e85a6578 | -12.52466 | -46.97434 | 2025-08-13 04:40:00 | NOAA-21 | ARRAIAS | TOCANTINS | Brasil | 1702406 | 17 | 33 | nan | nan | nan | Cerrado | 7.8 |
| da4b2b76-a4ab-37a5-bf9d-9e811228a561 | -8.3798 | -49.36049 | 2025-08-13 04:40:00 | NOAA-21 | CONCEIÇÃO DO ARAGUAIA | PARÁ | Brasil | 1502707 | 15 | 33 | nan | nan | nan | Amazônia | 0.6 |
| 07912418-b0ac-3aa1-896f-d402c67e96b7 | -7.14209 | -60.11989 | 2025-08-13 04:40:00 | NOAA-21 | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 3.3 |
| 9a112de8-ac22-311b-be7d-015c90c16c82 | -9.94976 | -48.34004 | 2025-08-13 04:40:00 | NOAA-21 | PALMAS | TOCANTINS | Brasil | 1721000 | 17 | 33 | nan | nan | nan | Cerrado | 1.3 |
| c8d3cb7d-d0e6-33fa-b9c1-7ca54eb826e6 | -6.09766 | -59.93581 | 2025-08-13 04:40:00 | NOAA-21 | NOVO ARIPUANÃ | AMAZONAS | Brasil | 1303304 | 13 | 33 | nan | nan | nan | Amazônia | 5.0 |
| a0de24fd-0d52-38da-8b3c-d310bd6e5720 | -11.64329 | -50.14873 | 2025-08-13 04:40:00 | NOAA-21 | FORMOSO DO ARAGUAIA | TOCANTINS | Brasil | 1708205 | 17 | 33 | nan | nan | nan | Cerrado | 1.4 |
| 2344171b-e83c-389f-8eaf-b3b97c5cb30c | -8.93423 | -60.73219 | 2025-08-13 04:40:00 | NOAA-21 | COLNIZA | MATO GROSSO | Brasil | 5103254 | 51 | 33 | nan | nan | nan | Amazônia | 2.3 |
| a86c0e93-8c4f-3721-b6aa-24672c522cb4 | -7.25737 | -60.00166 | 2025-08-13 04:40:00 | NOAA-21 | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 1.9 |
| 0ece8d64-a9ae-3fd3-aed4-bd2b76462998 | -10.96352 | -49.57195 | 2025-08-13 04:40:00 | NOAA-21 | SANTA RITA DO TOCANTINS | TOCANTINS | Brasil | 1718899 | 17 | 33 | nan | nan | nan | Cerrado | 7.5 |
| bd9b1bd2-47bc-37cf-bca1-aebdfdb08431 | -6.88824 | -59.13778 | 2025-08-13 04:40:00 | NOAA-21 | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 23.2 |
| 910aa72c-024f-3453-902d-b741fa789012 | -8.5693 | -54.7168 | 2025-08-13 04:40:00 | NOAA-21 | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 1.7 |
| 88d87807-8174-3ac4-bf7b-d9c9a4ee5a08 | -9.19207 | -59.6679 | 2025-08-13 04:40:00 | NOAA-21 | COLNIZA | MATO GROSSO | Brasil | 5103254 | 51 | 33 | nan | nan | nan | Amazônia | 1.8 |
| f8431ca7-d87a-3378-9508-f9cd1764f009 | -11.89969 | -52.53545 | 2025-08-13 04:40:00 | NOAA-21 | QUERÊNCIA | MATO GROSSO | Brasil | 5107065 | 51 | 33 | nan | nan | nan | Amazônia | 1.3 |
| eccc1dc3-5be7-3fb4-857c-533064434a83 | -8.93502 | -60.72932 | 2025-08-13 04:40:00 | NOAA-21 | COLNIZA | MATO GROSSO | Brasil | 5103254 | 51 | 33 | nan | nan | nan | Amazônia | 1.5 |
| d2c1bddd-5221-389c-817e-b015a80d007b | -7.06468 | -59.20312 | 2025-08-13 04:40:00 | NOAA-21 | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 1.3 |
| 41fc8ebd-ede4-3f45-a129-f541fc0c6974 | -10.34204 | -50.8206 | 2025-08-13 04:40:00 | NOAA-21 | SANTA TEREZINHA | MATO GROSSO | Brasil | 5107776 | 51 | 33 | nan | nan | nan | Cerrado | 0.9 |
| cacb3b55-52b8-3cb4-930f-f4d453990b19 | -9.05763 | -60.6469 | 2025-08-13 04:40:00 | NOAA-21 | COLNIZA | MATO GROSSO | Brasil | 5103254 | 51 | 33 | nan | nan | nan | Amazônia | 4.4 |
| 3c631eb5-32b2-3136-b342-150b2c2c5262 | -5.84833 | -59.92564 | 2025-08-13 04:40:00 | NOAA-21 | NOVO ARIPUANÃ | AMAZONAS | Brasil | 1303304 | 13 | 33 | nan | nan | nan | Amazônia | 2.4 |
| 79463ca0-417e-371b-8062-877d66478233 | -8.79708 | -52.04205 | 2025-08-13 04:40:00 | NOAA-21 | SÃO FÉLIX DO XINGU | PARÁ | Brasil | 1507300 | 15 | 33 | nan | nan | nan | Amazônia | 1.2 |
| eb39803d-f942-36df-b5a9-3059d430dfc9 | -6.281 | -53.63852 | 2025-08-13 04:40:00 | NOAA-21 | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 2.4 |
| 83a185f8-5a5a-356e-a2a6-3c70d977c66e | -12.14499 | -48.01663 | 2025-08-13 04:40:00 | NOAA-21 | PARANÃ | TOCANTINS | Brasil | 1716208 | 17 | 33 | nan | nan | nan | Cerrado | 4.7 |
| 3b71e8c6-e879-3c07-9068-f9950b72b932 | -6.92543 | -59.14759 | 2025-08-13 04:40:00 | NOAA-21 | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 13.2 |
| 7f206482-575c-3006-9e34-70fa8d3a0b6d | -9.21191 | -59.65045 | 2025-08-13 04:40:00 | NOAA-21 | COLNIZA | MATO GROSSO | Brasil | 5103254 | 51 | 33 | nan | nan | nan | Amazônia | 4.5 |
| 2c7f3f23-c109-305b-b2f4-b44404c8c879 | -7.11904 | -59.84618 | 2025-08-13 04:40:00 | NOAA-21 | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 1.4 |
| fe8850c8-3212-39f0-8d9e-eafb621f2c29 | -12.14795 | -48.02125 | 2025-08-13 04:40:00 | NOAA-21 | PARANÃ | TOCANTINS | Brasil | 1716208 | 17 | 33 | nan | nan | nan | Cerrado | 0.6 |
| 716fc1e8-4b5b-35fb-979b-cdd4beefd253 | -12.58372 | -46.9933 | 2025-08-13 04:40:00 | NOAA-21 | ARRAIAS | TOCANTINS | Brasil | 1702406 | 17 | 33 | nan | nan | nan | Cerrado | 2.1 |
| af2db793-abcc-3dd3-9756-7489ad023752 | -12.57826 | -47.0593 | 2025-08-13 04:40:00 | NOAA-21 | ARRAIAS | TOCANTINS | Brasil | 1702406 | 17 | 33 | nan | nan | nan | Cerrado | 2.2 |
| 8330eb42-6b13-34f4-9bb4-1470180a6b5f | -6.69411 | -59.14001 | 2025-08-13 04:40:00 | NOAA-21 | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 4.0 |
| b7a934db-3648-3227-b930-8a75e4804891 | -12.53157 | -46.98016 | 2025-08-13 04:40:00 | NOAA-21 | ARRAIAS | TOCANTINS | Brasil | 1702406 | 17 | 33 | nan | nan | nan | Cerrado | 7.9 |
| 57476fc7-c438-3e2f-b923-45b58c588188 | -8.62805 | -50.01724 | 2025-08-13 04:40:00 | NOAA-21 | SANTA MARIA DAS BARREIRAS | PARÁ | Brasil | 1506583 | 15 | 33 | nan | nan | nan | Amazônia | 1.4 |
| 9004ec19-4164-3ae1-9292-34708949b8a1 | -7.55916 | -49.30381 | 2025-08-13 04:40:00 | NOAA-21 | PAU D'ARCO | TOCANTINS | Brasil | 1716307 | 17 | 33 | nan | nan | nan | Amazônia | 2.5 |
| d37f4c21-caec-3938-a876-b8188defe6ec | -7.45942 | -60.64062 | 2025-08-13 04:40:00 | NOAA-21 | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 2.4 |
| da88eee8-2773-3f6c-ba11-66532edee2a5 | -7.80578 | -48.38267 | 2025-08-13 04:40:00 | NOAA-21 | PALMEIRANTE | TOCANTINS | Brasil | 1715705 | 17 | 33 | nan | nan | nan | Cerrado | 0.8 |
| f84fb42b-dc01-3886-8117-7a6629b7f5e0 | -7.26991 | -60.63155 | 2025-08-13 04:40:00 | NOAA-21 | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 2.6 |
| 654afcc3-1ff0-37fa-a45d-4224b492eb7c | -5.85424 | -59.92367 | 2025-08-13 04:40:00 | NOAA-21 | NOVO ARIPUANÃ | AMAZONAS | Brasil | 1303304 | 13 | 33 | nan | nan | nan | Amazônia | 1.6 |
| f7a1e508-02b6-3f37-babe-df24dc7ab003 | -7.4634 | -59.89148 | 2025-08-13 04:40:00 | NOAA-21 | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 7.2 |
| 87bc9db4-ff35-34fc-871a-c5a0ffd09a52 | -8.12259 | -55.56235 | 2025-08-13 04:40:00 | NOAA-21 | NOVO PROGRESSO | PARÁ | Brasil | 1505031 | 15 | 33 | nan | nan | nan | Amazônia | 1.3 |
| dd84dd1c-4537-3533-9202-89356fd2bd65 | -8.57485 | -54.70758 | 2025-08-13 04:40:00 | NOAA-21 | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 1.2 |
| 9a4101d2-e59f-33cf-9591-12bd4320c8d5 | -11.76091 | -48.19354 | 2025-08-13 04:40:00 | NOAA-21 | SÃO VALÉRIO | TOCANTINS | Brasil | 1720499 | 17 | 33 | nan | nan | nan | Cerrado | 5.4 |
| 4d93f20d-7cd1-3402-8f6c-812016117674 | -12.58125 | -46.98347 | 2025-08-13 04:40:00 | NOAA-21 | ARRAIAS | TOCANTINS | Brasil | 1702406 | 17 | 33 | nan | nan | nan | Cerrado | 7.2 |
| bf265b26-1aed-3758-bf04-e6169542f01e | -12.56954 | -47.03937 | 2025-08-13 04:40:00 | NOAA-21 | ARRAIAS | TOCANTINS | Brasil | 1702406 | 17 | 33 | nan | nan | nan | Cerrado | 2.3 |
| 6f52af5a-58ff-34b1-aa44-9713f170317c | -12.21236 | -45.46751 | 2025-08-13 04:40:00 | NOAA-21 | BARREIRAS | BAHIA | Brasil | 2903201 | 29 | 33 | nan | nan | nan | Cerrado | 0.9 |
| 7ac4f0ed-676c-3818-a005-626287426bfe | -7.26404 | -60.63037 | 2025-08-13 04:40:00 | NOAA-21 | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 10.7 |


[Clique aqui para ver as próximas entradas](README20.md)
