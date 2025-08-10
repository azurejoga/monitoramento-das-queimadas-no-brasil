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

## Dados Diários - Página 26

| ID | Latitude | Longitude | Data/Hora GMT | Satélite | Município | Estado | País | Município ID | Estado ID | País ID | Dias sem Chuva | Precipitação | Risco de Fogo | Bioma | FRP |
|----|----------|-----------|---------------|----------|-----------|--------|------|--------------|-----------|---------|----------------|--------------|----------------|-------|-----|
| 9390e015-69ac-3762-8c3b-42984d5c8745 | -8.7822 | -46.4174 | 2025-08-10 05:00:00 | GOES-19 | BALSAS | MARANHÃO | Brasil | 2101400 | 21 | 33 | nan | nan | nan | Cerrado | 56.5 |
| a97e9f6a-b208-344e-b38b-2d0a1ccb7a88 | -9.5015 | -46.2725 | 2025-08-10 05:00:00 | GOES-19 | ALTO PARNAÍBA | MARANHÃO | Brasil | 2100501 | 21 | 33 | nan | nan | nan | Cerrado | 89.2 |
| c1d44bf3-11d4-3588-808c-1981b956906f | -8.9401 | -60.7288 | 2025-08-10 05:00:00 | GOES-19 | COLNIZA | MATO GROSSO | Brasil | 5103254 | 51 | 33 | nan | nan | nan | Amazônia | 89.3 |
| 5648bfdb-a333-3d4a-b642-a815f48d8832 | -9.362 | -61.5324 | 2025-08-10 05:00:00 | GOES-19 | COLNIZA | MATO GROSSO | Brasil | 5103254 | 51 | 33 | nan | nan | nan | Amazônia | 94.5 |
| c1751b54-f0e3-3d16-aa57-4441d487cbdf | -9.3806 | -61.5315 | 2025-08-10 05:00:00 | GOES-19 | COLNIZA | MATO GROSSO | Brasil | 5103254 | 51 | 33 | nan | nan | nan | Amazônia | 80.3 |
| 0b1fa19f-733e-3d0e-9091-575447b49050 | -8.9213 | -60.7489 | 2025-08-10 05:00:00 | GOES-19 | COLNIZA | MATO GROSSO | Brasil | 5103254 | 51 | 33 | nan | nan | nan | Amazônia | 87.2 |
| 651df248-bad5-35c1-b964-d6fbab0a09af | -7.08 | -59.1771 | 2025-08-10 05:10:00 | GOES-19 | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 47.5 |
| 28562579-f652-32b5-a493-8b01e39349fa | -8.9213 | -60.7489 | 2025-08-10 05:10:00 | GOES-19 | COLNIZA | MATO GROSSO | Brasil | 5103254 | 51 | 33 | nan | nan | nan | Amazônia | 75.2 |
| d9abcd44-d9f2-3cb9-9222-2f29ccb89235 | -7.0614 | -59.1972 | 2025-08-10 05:10:00 | GOES-19 | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 55.3 |
| 4bd53ca9-3b3b-3142-a518-54080dc9ab93 | -9.3806 | -61.5315 | 2025-08-10 05:10:00 | GOES-19 | COLNIZA | MATO GROSSO | Brasil | 5103254 | 51 | 33 | nan | nan | nan | Amazônia | 85.6 |
| 9e6a75f7-5a05-306c-91b8-512d7f426a1a | -8.9401 | -60.7288 | 2025-08-10 05:10:00 | GOES-19 | COLNIZA | MATO GROSSO | Brasil | 5103254 | 51 | 33 | nan | nan | nan | Amazônia | 75.9 |
| 65b080fc-3574-3f9d-8e14-22135133d8cc | -8.9215 | -60.7297 | 2025-08-10 05:10:00 | GOES-19 | COLNIZA | MATO GROSSO | Brasil | 5103254 | 51 | 33 | nan | nan | nan | Amazônia | 63.9 |
| e9c28bae-6fed-3f0f-b7c6-170b58701fec | -8.9399 | -60.7481 | 2025-08-10 05:10:00 | GOES-19 | COLNIZA | MATO GROSSO | Brasil | 5103254 | 51 | 33 | nan | nan | nan | Amazônia | 136.0 |
| df78e2dd-4c6e-3a48-9b61-072c9f5c2612 | -9.362 | -61.5324 | 2025-08-10 05:10:00 | GOES-19 | COLNIZA | MATO GROSSO | Brasil | 5103254 | 51 | 33 | nan | nan | nan | Amazônia | 93.1 |
| 63db3c40-9e40-31b3-97b7-762bab9075f1 | -9.4825 | -46.2746 | 2025-08-10 05:10:00 | GOES-19 | ALTO PARNAÍBA | MARANHÃO | Brasil | 2100501 | 21 | 33 | nan | nan | nan | Cerrado | 64.3 |
| 61f94afe-c12a-3fe7-a814-c9919d9dfc5f | -7.0799 | -59.1964 | 2025-08-10 05:10:00 | GOES-19 | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 61.8 |
| 66c811a6-8db3-3443-87d6-cf38588f993e | -9.3806 | -61.5315 | 2025-08-10 05:20:00 | GOES-19 | COLNIZA | MATO GROSSO | Brasil | 5103254 | 51 | 33 | nan | nan | nan | Amazônia | 96.1 |
| 52054d69-d322-3676-bc08-c5a575c8cbce | -8.9401 | -60.7288 | 2025-08-10 05:20:00 | GOES-19 | COLNIZA | MATO GROSSO | Brasil | 5103254 | 51 | 33 | nan | nan | nan | Amazônia | 64.9 |
| 8a7e893a-0eab-3b8c-b19c-425b4fc08ec8 | -9.362 | -61.5324 | 2025-08-10 05:20:00 | GOES-19 | COLNIZA | MATO GROSSO | Brasil | 5103254 | 51 | 33 | nan | nan | nan | Amazônia | 86.4 |
| 1ccd2bce-48de-3fdb-9941-c0ccbbb8c79d | -8.9215 | -60.7297 | 2025-08-10 05:20:00 | GOES-19 | COLNIZA | MATO GROSSO | Brasil | 5103254 | 51 | 33 | nan | nan | nan | Amazônia | 53.0 |
| 9f92cd6e-3c6b-3956-8e06-ecfa241f3eac | -8.9398 | -60.7673 | 2025-08-10 05:20:00 | GOES-19 | COLNIZA | MATO GROSSO | Brasil | 5103254 | 51 | 33 | nan | nan | nan | Amazônia | 52.6 |
| 1c09d1e8-575c-38bf-92d6-0b2ae562e154 | -8.9213 | -60.7489 | 2025-08-10 05:20:00 | GOES-19 | COLNIZA | MATO GROSSO | Brasil | 5103254 | 51 | 33 | nan | nan | nan | Amazônia | 60.5 |
| c0c0e154-b86a-340b-9004-535aab01b977 | -8.9399 | -60.7481 | 2025-08-10 05:20:00 | GOES-19 | COLNIZA | MATO GROSSO | Brasil | 5103254 | 51 | 33 | nan | nan | nan | Amazônia | 120.0 |
| f34784c9-5f9c-35ac-8fec-653f52c3e12c | -8.9213 | -60.7489 | 2025-08-10 05:30:00 | GOES-19 | COLNIZA | MATO GROSSO | Brasil | 5103254 | 51 | 33 | nan | nan | nan | Amazônia | 46.8 |
| c0ce9a5b-c126-3d7f-9769-572a2432291c | -8.9399 | -60.7481 | 2025-08-10 05:30:00 | GOES-19 | COLNIZA | MATO GROSSO | Brasil | 5103254 | 51 | 33 | nan | nan | nan | Amazônia | 80.8 |
| af481188-96c4-3290-b50c-0eeaecfb0e5c | -9.3806 | -61.5315 | 2025-08-10 05:30:00 | GOES-19 | COLNIZA | MATO GROSSO | Brasil | 5103254 | 51 | 33 | nan | nan | nan | Amazônia | 102.3 |
| eeb64646-72ad-3f08-97f6-de7ac5afe5fd | -9.362 | -61.5324 | 2025-08-10 05:30:00 | GOES-19 | COLNIZA | MATO GROSSO | Brasil | 5103254 | 51 | 33 | nan | nan | nan | Amazônia | 74.3 |
| 7f0ad82d-429c-31c7-9190-29e0239af597 | -2.61688 | -54.7288 | 2025-08-10 05:33:00 | NOAA-21 | SANTARÉM | PARÁ | Brasil | 1506807 | 15 | 33 | nan | nan | nan | Amazônia | 2.7 |
| eb0aad92-a08a-32c9-ab21-4c479c484da3 | -2.37132 | -51.90772 | 2025-08-10 05:33:00 | NOAA-21 | PORTO DE MOZ | PARÁ | Brasil | 1505908 | 15 | 33 | nan | nan | nan | Amazônia | 1.7 |
| a4f01654-8e67-3f91-9d51-049813521071 | -2.36956 | -51.90971 | 2025-08-10 05:33:00 | NOAA-21 | PORTO DE MOZ | PARÁ | Brasil | 1505908 | 15 | 33 | nan | nan | nan | Amazônia | 2.2 |
| 21846cb2-4f2a-3f4e-acf5-e079516fc7ca | -2.37066 | -51.91225 | 2025-08-10 05:33:00 | NOAA-21 | PORTO DE MOZ | PARÁ | Brasil | 1505908 | 15 | 33 | nan | nan | nan | Amazônia | 1.7 |
| 693c6949-69ae-3a08-84c8-0f7808f65d58 | -2.61731 | -54.72586 | 2025-08-10 05:33:00 | NOAA-21 | SANTARÉM | PARÁ | Brasil | 1506807 | 15 | 33 | nan | nan | nan | Amazônia | 2.7 |
| 166fc0d7-b87c-39ab-99e4-2a1612ef42ee | -2.37669 | -51.91339 | 2025-08-10 05:33:00 | NOAA-21 | PORTO DE MOZ | PARÁ | Brasil | 1505908 | 15 | 33 | nan | nan | nan | Amazônia | 1.6 |
| d83c2d0d-7d34-3b04-8fb2-f11d583da6d5 | -2.3756 | -51.91078 | 2025-08-10 05:33:00 | NOAA-21 | PORTO DE MOZ | PARÁ | Brasil | 1505908 | 15 | 33 | nan | nan | nan | Amazônia | 2.2 |
| 91a50708-5be9-39ad-988c-28ed7ac45ce3 | -8.5707 | -54.66932 | 2025-08-10 05:36:00 | NOAA-21 | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 2.8 |
| 6ec20453-a096-36da-9347-de8b0a7e3ace | -7.3982 | -59.99697 | 2025-08-10 05:36:00 | NOAA-21 | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 2.8 |
| 27949bb3-4e2b-3530-9539-5892f2166bbe | -6.34529 | -55.56374 | 2025-08-10 05:36:00 | NOAA-21 | ITAITUBA | PARÁ | Brasil | 1503606 | 15 | 33 | nan | nan | nan | Amazônia | 0.8 |
| b63671da-9bd3-325a-bb0c-846cb6071aea | -5.28548 | -56.01904 | 2025-08-10 05:36:00 | NOAA-21 | TRAIRÃO | PARÁ | Brasil | 1508050 | 15 | 33 | nan | nan | nan | Amazônia | 2.2 |
| d31c7f50-68fe-326d-a135-05aa0cebc942 | -8.56873 | -54.6842 | 2025-08-10 05:36:00 | NOAA-21 | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 5.2 |
| 030af23d-b623-3327-8aff-49c28a8aa9b8 | -8.5637 | -54.67968 | 2025-08-10 05:36:00 | NOAA-21 | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 4.3 |
| ec6c292f-c3b5-33b5-b23a-1b5b146ccedc | -8.56922 | -54.68049 | 2025-08-10 05:36:00 | NOAA-21 | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 4.3 |
| 8d626688-6ac9-3ef2-ac31-9cc5c84c8706 | -8.57021 | -54.67305 | 2025-08-10 05:36:00 | NOAA-21 | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 2.8 |
| 4ea6c8f8-3513-304d-9b0d-996cc8e21e45 | -7.402 | -59.9976 | 2025-08-10 05:36:00 | NOAA-21 | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 1.6 |
| 492d5bc2-1841-3c12-9ca9-d6b13fe5fd7e | -7.4058 | -59.99822 | 2025-08-10 05:36:00 | NOAA-21 | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 1.6 |
| 6217647e-aeb5-38cb-927a-c913b1f6d277 | -8.56823 | -54.68792 | 2025-08-10 05:36:00 | NOAA-21 | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 5.2 |
| 4ca4386a-9927-3574-8c7b-ccf56dca6310 | -7.07087 | -59.19805 | 2025-08-10 05:36:00 | NOAA-21 | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 2.6 |
| c02deea0-b032-3343-bece-cea1ba830ca0 | -8.56222 | -54.69084 | 2025-08-10 05:36:00 | NOAA-21 | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 3.7 |
| adb53f7d-c163-360c-b2ad-ce8319780c6e | -8.31011 | -55.09955 | 2025-08-10 05:36:00 | NOAA-21 | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 1.4 |
| 32c4255c-1ec2-3b20-ac4c-fe2aeae8640f | -5.34112 | -55.90343 | 2025-08-10 05:36:00 | NOAA-21 | TRAIRÃO | PARÁ | Brasil | 1508050 | 15 | 33 | nan | nan | nan | Amazônia | 2.3 |
| fceaa164-860d-33ae-8805-15a3c71a80d8 | -6.63707 | -55.26752 | 2025-08-10 05:36:00 | NOAA-21 | NOVO PROGRESSO | PARÁ | Brasil | 1505031 | 15 | 33 | nan | nan | nan | Amazônia | 0.6 |
| 9bd857ed-d6b1-3257-b4e9-e1442cb67ba9 | -8.56271 | -54.68716 | 2025-08-10 05:36:00 | NOAA-21 | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 5.2 |
| 433bc0d3-ebef-3695-8cb3-acc2e4734b14 | -5.34597 | -55.90411 | 2025-08-10 05:36:00 | NOAA-21 | TRAIRÃO | PARÁ | Brasil | 1508050 | 15 | 33 | nan | nan | nan | Amazônia | 2.3 |
| 4cc7c4df-f2e4-331a-84e6-2b48777ba182 | -7.40509 | -60.00293 | 2025-08-10 05:36:00 | NOAA-21 | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 1.6 |
| db151e34-21ea-3f45-9ebc-79822e25f1cd | -6.35035 | -55.56437 | 2025-08-10 05:36:00 | NOAA-21 | ITAITUBA | PARÁ | Brasil | 1503606 | 15 | 33 | nan | nan | nan | Amazônia | 0.8 |
| 3e347d36-2a40-311b-8174-b77331a76b00 | -6.6375 | -55.26434 | 2025-08-10 05:36:00 | NOAA-21 | NOVO PROGRESSO | PARÁ | Brasil | 1505031 | 15 | 33 | nan | nan | nan | Amazônia | 0.6 |
| c7df8601-910e-3d09-87a5-f40def04fae5 | -8.56971 | -54.67678 | 2025-08-10 05:36:00 | NOAA-21 | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 4.3 |
| b9080764-7006-3280-9207-49ffc91f8344 | -6.3457 | -55.5608 | 2025-08-10 05:36:00 | NOAA-21 | ITAITUBA | PARÁ | Brasil | 1503606 | 15 | 33 | nan | nan | nan | Amazônia | 0.8 |
| 7fecfc76-85f2-3133-9122-bebabda54c18 | -8.56774 | -54.69163 | 2025-08-10 05:36:00 | NOAA-21 | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 3.7 |
| b6a48423-b1c0-3e11-9e3e-a63dff684ea4 | -8.56419 | -54.67597 | 2025-08-10 05:36:00 | NOAA-21 | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 4.3 |
| fccd637f-60b9-3fa1-ba19-5f22b8aef146 | -7.07209 | -59.16192 | 2025-08-10 05:36:00 | NOAA-21 | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 1.5 |
| 8529c0b8-e0dd-3801-96e9-64122ec6904b | -5.28639 | -56.01691 | 2025-08-10 05:36:00 | NOAA-21 | TRAIRÃO | PARÁ | Brasil | 1508050 | 15 | 33 | nan | nan | nan | Amazônia | 2.2 |
| fcd9bad9-5956-31af-aa84-f702d48096f8 | -7.07353 | -59.17989 | 2025-08-10 05:36:00 | NOAA-21 | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 2.2 |
| ddc7c544-cd90-3148-8e8d-d525febf58bb | -8.5632 | -54.68342 | 2025-08-10 05:36:00 | NOAA-21 | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 5.2 |
| 89b44591-61f5-309b-94fc-4bdcedede992 | -9.55989 | -62.72114 | 2025-08-10 05:38:00 | NOAA-21 | RIO CRESPO | RONDÔNIA | Brasil | 1100262 | 11 | 33 | nan | nan | nan | Amazônia | 1.8 |
| a008673d-365e-3993-81e6-a4bf2573bb68 | -8.92484 | -60.74538 | 2025-08-10 05:38:00 | NOAA-21 | COLNIZA | MATO GROSSO | Brasil | 5103254 | 51 | 33 | nan | nan | nan | Amazônia | 1.0 |
| b6933c4d-f1a4-3b59-b203-669b59d6da6d | -8.92681 | -60.73204 | 2025-08-10 05:38:00 | NOAA-21 | COLNIZA | MATO GROSSO | Brasil | 5103254 | 51 | 33 | nan | nan | nan | Amazônia | 9.0 |
| 9a38aa5e-2617-358d-93a2-a85318d8675e | -8.93119 | -60.72815 | 2025-08-10 05:38:00 | NOAA-21 | COLNIZA | MATO GROSSO | Brasil | 5103254 | 51 | 33 | nan | nan | nan | Amazônia | 3.0 |
| 0c4a708e-c720-353b-8063-8c549e862738 | -8.95188 | -64.33948 | 2025-08-10 05:38:00 | NOAA-21 | PORTO VELHO | RONDÔNIA | Brasil | 1100205 | 11 | 33 | nan | nan | nan | Amazônia | 0.8 |
| 3cf1b46f-46af-3935-a999-62024fe62d46 | -9.20097 | -59.67406 | 2025-08-10 05:38:00 | NOAA-21 | COLNIZA | MATO GROSSO | Brasil | 5103254 | 51 | 33 | nan | nan | nan | Amazônia | 1.6 |
| e748b8fe-5579-34c0-b3bc-786971191f50 | -8.9231 | -60.73148 | 2025-08-10 05:38:00 | NOAA-21 | COLNIZA | MATO GROSSO | Brasil | 5103254 | 51 | 33 | nan | nan | nan | Amazônia | 1.0 |
| 57e3ccb4-cd7f-3737-9828-05107f0d8514 | -16.3056 | -52.92963 | 2025-08-10 05:38:00 | NOAA-21 | TORIXORÉU | MATO GROSSO | Brasil | 5108204 | 51 | 33 | nan | nan | nan | Cerrado | 4.6 |
| 7b685aae-d816-34c2-9922-a2f268a02062 | -9.19699 | -59.6735 | 2025-08-10 05:38:00 | NOAA-21 | COLNIZA | MATO GROSSO | Brasil | 5103254 | 51 | 33 | nan | nan | nan | Amazônia | 1.4 |
| b3f098e4-6dda-30f5-9197-2e5b07369f2a | -9.71396 | -61.29968 | 2025-08-10 05:38:00 | NOAA-21 | COLNIZA | MATO GROSSO | Brasil | 5103254 | 51 | 33 | nan | nan | nan | Amazônia | 0.9 |
| f02494c5-313b-3d31-a2b6-12efd3e7df12 | -9.70968 | -61.30341 | 2025-08-10 05:38:00 | NOAA-21 | COLNIZA | MATO GROSSO | Brasil | 5103254 | 51 | 33 | nan | nan | nan | Amazônia | 0.9 |
| c508e604-1e80-30e4-82f9-32230ac2a561 | -9.67437 | -62.89075 | 2025-08-10 05:38:00 | NOAA-21 | RIO CRESPO | RONDÔNIA | Brasil | 1100262 | 11 | 33 | nan | nan | nan | Amazônia | 2.9 |
| 0f57e1ff-4c3c-380a-a539-1d1fdcd96af0 | -10.91712 | -68.43546 | 2025-08-10 05:38:00 | NOAA-21 | EPITACIOLÂNDIA | ACRE | Brasil | 1200252 | 12 | 33 | nan | nan | nan | Amazônia | 0.9 |
| d23115fb-0116-3d99-a8d6-8f6a51d50aa9 | -8.93029 | -60.75982 | 2025-08-10 05:38:00 | NOAA-21 | COLNIZA | MATO GROSSO | Brasil | 5103254 | 51 | 33 | nan | nan | nan | Amazônia | 3.2 |
| b9728234-e6f8-3a51-bb7c-1119bd10f783 | -8.93443 | -60.74532 | 2025-08-10 05:38:00 | NOAA-21 | COLNIZA | MATO GROSSO | Brasil | 5103254 | 51 | 33 | nan | nan | nan | Amazônia | 10.8 |
| 3c92736f-151b-37a7-a874-b30e28e4f171 | -8.93751 | -60.75033 | 2025-08-10 05:38:00 | NOAA-21 | COLNIZA | MATO GROSSO | Brasil | 5103254 | 51 | 33 | nan | nan | nan | Amazônia | 10.9 |
| 76778522-2685-3b31-9e98-a25bcb2c85a7 | -9.67493 | -62.88707 | 2025-08-10 05:38:00 | NOAA-21 | RIO CRESPO | RONDÔNIA | Brasil | 1100262 | 11 | 33 | nan | nan | nan | Amazônia | 4.9 |
| d7aff47c-aee2-34a7-9357-273c0945941d | -8.90469 | -60.54404 | 2025-08-10 05:38:00 | NOAA-21 | COLNIZA | MATO GROSSO | Brasil | 5103254 | 51 | 33 | nan | nan | nan | Amazônia | 1.2 |
| 66f1e2b0-f086-36da-a16a-4e5afbcad35f | -8.57617 | -62.64546 | 2025-08-10 05:38:00 | NOAA-21 | PORTO VELHO | RONDÔNIA | Brasil | 1100205 | 11 | 33 | nan | nan | nan | Amazônia | 0.4 |
| e7f87f3a-9075-333c-ad9b-9b3d2c5099fd | -8.92657 | -60.75927 | 2025-08-10 05:38:00 | NOAA-21 | COLNIZA | MATO GROSSO | Brasil | 5103254 | 51 | 33 | nan | nan | nan | Amazônia | 3.0 |
| bf874645-7a16-34ee-900e-df989d509730 | -8.9357 | -60.7364 | 2025-08-10 05:38:00 | NOAA-21 | COLNIZA | MATO GROSSO | Brasil | 5103254 | 51 | 33 | nan | nan | nan | Amazônia | 2.3 |
| b0f95cef-1bb7-30f4-be52-56eb1092345b | -8.93379 | -60.74976 | 2025-08-10 05:38:00 | NOAA-21 | COLNIZA | MATO GROSSO | Brasil | 5103254 | 51 | 33 | nan | nan | nan | Amazônia | 10.9 |
| b5b38945-59dc-3a46-89ef-e5050a9992cc | -8.91662 | -60.54119 | 2025-08-10 05:38:00 | NOAA-21 | COLNIZA | MATO GROSSO | Brasil | 5103254 | 51 | 33 | nan | nan | nan | Amazônia | 1.7 |
| 0521e81d-2cf8-3537-a9a4-5c049785d0d3 | -8.93506 | -60.74086 | 2025-08-10 05:38:00 | NOAA-21 | COLNIZA | MATO GROSSO | Brasil | 5103254 | 51 | 33 | nan | nan | nan | Amazônia | 10.8 |
| 15519e70-ceb0-3ca8-9279-7c1314e0d86c | -8.94036 | -60.74317 | 2025-08-10 05:38:00 | NOAA-21 | COLNIZA | MATO GROSSO | Brasil | 5103254 | 51 | 33 | nan | nan | nan | Amazônia | 1.4 |
| e4854405-47b7-3637-9ec6-fd43f2a21367 | -9.70794 | -61.29003 | 2025-08-10 05:38:00 | NOAA-21 | COLNIZA | MATO GROSSO | Brasil | 5103254 | 51 | 33 | nan | nan | nan | Amazônia | 1.8 |
| 6a968004-6034-3d15-a62b-37a2c973f612 | -8.9316 | -60.75095 | 2025-08-10 05:38:00 | NOAA-21 | COLNIZA | MATO GROSSO | Brasil | 5103254 | 51 | 33 | nan | nan | nan | Amazônia | 9.3 |
| a2ac58d8-e57c-36c7-9263-89da89cb4f9a | -8.93316 | -60.75422 | 2025-08-10 05:38:00 | NOAA-21 | COLNIZA | MATO GROSSO | Brasil | 5103254 | 51 | 33 | nan | nan | nan | Amazônia | 10.9 |
| af0decad-a053-3a24-a12a-656086048f47 | -8.93814 | -60.74588 | 2025-08-10 05:38:00 | NOAA-21 | COLNIZA | MATO GROSSO | Brasil | 5103254 | 51 | 33 | nan | nan | nan | Amazônia | 10.8 |
| aeb536fd-9310-35c9-916c-5def8a224ae6 | -8.93466 | -60.75594 | 2025-08-10 05:38:00 | NOAA-21 | COLNIZA | MATO GROSSO | Brasil | 5103254 | 51 | 33 | nan | nan | nan | Amazônia | 9.3 |
| a83b0c1a-b8d4-3340-b982-009695c7621e | -8.93903 | -60.75206 | 2025-08-10 05:38:00 | NOAA-21 | COLNIZA | MATO GROSSO | Brasil | 5103254 | 51 | 33 | nan | nan | nan | Amazônia | 0.9 |
| e7e5999d-fe8a-3c94-a209-0519617e5cb4 | -9.19857 | -59.67258 | 2025-08-10 05:38:00 | NOAA-21 | COLNIZA | MATO GROSSO | Brasil | 5103254 | 51 | 33 | nan | nan | nan | Amazônia | 2.2 |
| 7da7ac95-cc97-3993-b437-9ff79d013a81 | -8.92855 | -60.74594 | 2025-08-10 05:38:00 | NOAA-21 | COLNIZA | MATO GROSSO | Brasil | 5103254 | 51 | 33 | nan | nan | nan | Amazônia | 1.0 |
| c5d4128f-dbbb-37ff-bece-6dc7c29f0b2e | -9.20653 | -59.67371 | 2025-08-10 05:38:00 | NOAA-21 | COLNIZA | MATO GROSSO | Brasil | 5103254 | 51 | 33 | nan | nan | nan | Amazônia | 1.5 |
| 48e35146-73e9-3ada-8ca2-732f50139e92 | -9.20026 | -59.67924 | 2025-08-10 05:38:00 | NOAA-21 | COLNIZA | MATO GROSSO | Brasil | 5103254 | 51 | 33 | nan | nan | nan | Amazônia | 1.4 |
| 9b0b218b-84ff-30e3-8549-3c645d1409bf | -9.20331 | -59.66797 | 2025-08-10 05:38:00 | NOAA-21 | COLNIZA | MATO GROSSO | Brasil | 5103254 | 51 | 33 | nan | nan | nan | Amazônia | 2.2 |
| 7bd4645a-b6d4-37ca-92cb-5017547b9e82 | -9.71332 | -61.30395 | 2025-08-10 05:38:00 | NOAA-21 | COLNIZA | MATO GROSSO | Brasil | 5103254 | 51 | 33 | nan | nan | nan | Amazônia | 0.9 |


[Clique aqui para ver as próximas entradas](README27.md)
