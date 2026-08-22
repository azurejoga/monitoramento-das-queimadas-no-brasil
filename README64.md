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

## Dados Diários - Página 64

| ID | Latitude | Longitude | Data/Hora GMT | Satélite | Município | Estado | País | Município ID | Estado ID | País ID | Dias sem Chuva | Precipitação | Risco de Fogo | Bioma | FRP |
|----|----------|-----------|---------------|----------|-----------|--------|------|--------------|-----------|---------|----------------|--------------|----------------|-------|-----|
| 3110685a-933f-3d6f-b314-6b87ff9da3b4 | -6.37688 | -54.95963 | 2026-08-22 05:23:00 | NOAA-20 | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 1.5 |
| c83893e4-47db-3e1d-97d4-429e64ddd3ff | -6.11213 | -59.92587 | 2026-08-22 05:23:00 | NOAA-20 | NOVO ARIPUANÃ | AMAZONAS | Brasil | 1303304 | 13 | 33 | nan | nan | nan | Amazônia | 0.9 |
| 2e5b75fe-9daa-3eb6-81ba-2c21e5040853 | -6.79871 | -59.45469 | 2026-08-22 05:23:00 | NOAA-20 | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 1.5 |
| 9a0697f2-37ac-32fa-b04d-1804f84917c1 | -13.98609 | -53.67618 | 2026-08-22 05:23:00 | NOAA-20 | PARANATINGA | MATO GROSSO | Brasil | 5106307 | 51 | 33 | nan | nan | nan | Cerrado | 3.4 |
| 231b9b4a-c930-3934-8d41-fa5ee5e6ebc1 | -6.97036 | -59.05635 | 2026-08-22 05:23:00 | NOAA-20 | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 7.2 |
| 8b6879ac-6b90-38a7-8063-cf2c5c429245 | -6.26917 | -62.52881 | 2026-08-22 05:23:00 | NOAA-20 | MANICORÉ | AMAZONAS | Brasil | 1302702 | 13 | 33 | nan | nan | nan | Amazônia | 2.0 |
| 1eac27e5-1332-30e3-a8ac-69624dcccbbb | -6.82129 | -59.41924 | 2026-08-22 05:23:00 | NOAA-20 | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 2.6 |
| 3215ba40-62cc-39a2-8a4a-cf0d1d6a369d | -6.00049 | -57.81461 | 2026-08-22 05:23:00 | NOAA-20 | JACAREACANGA | PARÁ | Brasil | 1503754 | 15 | 33 | nan | nan | nan | Amazônia | 4.4 |
| bea10d81-d6a0-35b6-8f6c-278a2e11a444 | -14.00125 | -53.66868 | 2026-08-22 05:23:00 | NOAA-20 | PARANATINGA | MATO GROSSO | Brasil | 5106307 | 51 | 33 | nan | nan | nan | Cerrado | 6.7 |
| e4272db6-fb42-392a-99fb-279d1eae4c60 | -6.76126 | -59.15409 | 2026-08-22 05:23:00 | NOAA-20 | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 1.7 |
| bb0201b7-d00d-36ea-8897-098204be531b | -10.38587 | -61.20459 | 2026-08-22 05:23:00 | NOAA-20 | RONDOLÂNDIA | MATO GROSSO | Brasil | 5107578 | 51 | 33 | nan | nan | nan | Amazônia | 0.8 |
| 2084cb45-5031-3731-8af5-b227e7721c52 | -6.0128 | -57.82381 | 2026-08-22 05:23:00 | NOAA-20 | JACAREACANGA | PARÁ | Brasil | 1503754 | 15 | 33 | nan | nan | nan | Amazônia | 1.5 |
| ddf4a68f-e474-3dea-93e7-d0d5c668f1a6 | -6.86327 | -59.02521 | 2026-08-22 05:23:00 | NOAA-20 | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 2.4 |
| 5fc630ab-7fde-37f4-ba2e-720033e0f2bd | -10.38529 | -61.20817 | 2026-08-22 05:23:00 | NOAA-20 | RONDOLÂNDIA | MATO GROSSO | Brasil | 5107578 | 51 | 33 | nan | nan | nan | Amazônia | 0.8 |
| 63e77489-c0f5-3b5f-8a06-03b581b83f68 | -14.97753 | -52.6581 | 2026-08-22 05:23:00 | NOAA-20 | BARRA DO GARÇAS | MATO GROSSO | Brasil | 5101803 | 51 | 33 | nan | nan | nan | Cerrado | 0.7 |
| dc29f174-7952-38f4-b728-d1462904b087 | -6.13655 | -59.90105 | 2026-08-22 05:23:00 | NOAA-20 | NOVO ARIPUANÃ | AMAZONAS | Brasil | 1303304 | 13 | 33 | nan | nan | nan | Amazônia | 1.2 |
| 0fef9424-06dd-352d-8f43-754f758c9a17 | -6.12323 | -59.92046 | 2026-08-22 05:23:00 | NOAA-20 | NOVO ARIPUANÃ | AMAZONAS | Brasil | 1303304 | 13 | 33 | nan | nan | nan | Amazônia | 1.2 |
| 8d1665f6-1a52-3402-9d1f-4e690b90f9ae | -14.31294 | -51.86843 | 2026-08-22 05:23:00 | NOAA-20 | NOVA NAZARÉ | MATO GROSSO | Brasil | 5106174 | 51 | 33 | nan | nan | nan | Cerrado | 1.2 |
| 0cb76a52-af88-3229-81fd-6f790bab98ee | -6.0966 | -59.91624 | 2026-08-22 05:23:00 | NOAA-20 | NOVO ARIPUANÃ | AMAZONAS | Brasil | 1303304 | 13 | 33 | nan | nan | nan | Amazônia | 1.3 |
| f2af55b8-3a6b-35d8-a5c9-696b5549f440 | -6.2697 | -62.52575 | 2026-08-22 05:23:00 | NOAA-20 | MANICORÉ | AMAZONAS | Brasil | 1302702 | 13 | 33 | nan | nan | nan | Amazônia | 1.9 |
| e88cbfdc-a468-37c5-b063-d3285d2db582 | -6.89305 | -59.02991 | 2026-08-22 05:23:00 | NOAA-20 | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 1.3 |
| d2f6bda8-11d1-3ca0-974b-f915a21cb4aa | -6.75891 | -58.69563 | 2026-08-22 05:23:00 | NOAA-20 | MAUÉS | AMAZONAS | Brasil | 1302900 | 13 | 33 | nan | nan | nan | Amazônia | 1.2 |
| 47ff1e9d-b2f9-3dc0-8407-616977e89092 | -13.98963 | -53.67366 | 2026-08-22 05:23:00 | NOAA-20 | PARANATINGA | MATO GROSSO | Brasil | 5106307 | 51 | 33 | nan | nan | nan | Cerrado | 4.1 |
| 4c8ceb9d-fbc1-37a2-8909-dbf7359b22d1 | -6.89224 | -55.7148 | 2026-08-22 05:23:00 | NOAA-20 | NOVO PROGRESSO | PARÁ | Brasil | 1505031 | 15 | 33 | nan | nan | nan | Amazônia | 1.3 |
| 5b1486bd-f0aa-3475-810e-f76db2a110c8 | -6.76993 | -58.66883 | 2026-08-22 05:23:00 | NOAA-20 | MAUÉS | AMAZONAS | Brasil | 1302900 | 13 | 33 | nan | nan | nan | Amazônia | 2.5 |
| 44495860-da48-3de9-871c-ce8667f91528 | -6.77217 | -58.69772 | 2026-08-22 05:23:00 | NOAA-20 | MAUÉS | AMAZONAS | Brasil | 1302900 | 13 | 33 | nan | nan | nan | Amazônia | 0.7 |
| 1a6a124a-42b1-3ca4-86c4-0e078a8ecada | -6.131 | -59.91452 | 2026-08-22 05:23:00 | NOAA-20 | NOVO ARIPUANÃ | AMAZONAS | Brasil | 1303304 | 13 | 33 | nan | nan | nan | Amazônia | 1.8 |
| ef281881-52fd-3592-9176-037f9ac4be5b | -6.22078 | -55.48154 | 2026-08-22 05:23:00 | NOAA-20 | ITAITUBA | PARÁ | Brasil | 1503606 | 15 | 33 | nan | nan | nan | Amazônia | 1.6 |
| 50131c4d-7a30-328b-bda2-0c5a3b3a1f3a | -4.52718 | -54.85812 | 2026-08-22 05:23:00 | NOAA-20 | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 2.0 |
| 7034f282-342d-369d-bca5-da3903fd6a02 | -6.85823 | -59.42157 | 2026-08-22 05:23:00 | NOAA-20 | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 1.7 |
| cca0ff42-5a28-368c-9071-94cdf5a56199 | -8.53881 | -55.33454 | 2026-08-22 05:23:00 | NOAA-20 | NOVO PROGRESSO | PARÁ | Brasil | 1505031 | 15 | 33 | nan | nan | nan | Amazônia | 1.3 |
| 6e591a81-b125-36fc-80c1-f94a0ed7b5fd | -12.71653 | -48.41694 | 2026-08-22 05:23:00 | NOAA-20 | SÃO SALVADOR DO TOCANTINS | TOCANTINS | Brasil | 1720259 | 17 | 33 | nan | nan | nan | Cerrado | 2.3 |
| 24641dde-5a30-3840-805e-f91e655864b8 | -6.85996 | -59.02468 | 2026-08-22 05:23:00 | NOAA-20 | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 1.3 |
| 8bbb4ece-19dd-3a2a-ace0-b0c5732547c7 | -5.80386 | -57.54934 | 2026-08-22 05:23:00 | NOAA-20 | JACAREACANGA | PARÁ | Brasil | 1503754 | 15 | 33 | nan | nan | nan | Amazônia | 1.4 |
| adabba31-1251-373c-a1ee-dd4f2cd925b6 | -9.00539 | -50.75415 | 2026-08-22 05:23:00 | NOAA-20 | SANTANA DO ARAGUAIA | PARÁ | Brasil | 1506708 | 15 | 33 | nan | nan | nan | Amazônia | 2.9 |
| ae75e354-7b80-3b9c-aa9a-b407a222d5e6 | -8.52265 | -54.81653 | 2026-08-22 05:23:00 | NOAA-20 | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 8.0 |
| 32c1ba20-5278-394e-9c23-6747e2cc8b80 | -12.10255 | -56.32193 | 2026-08-22 05:23:00 | NOAA-20 | PORTO DOS GAÚCHOS | MATO GROSSO | Brasil | 5106802 | 51 | 33 | nan | nan | nan | Amazônia | 5.2 |
| f27e806c-61d8-34e6-86ee-9ab90a6a9480 | -6.8892 | -59.03285 | 2026-08-22 05:23:00 | NOAA-20 | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 1.2 |
| 2f6f33cb-8627-310f-b6f4-7852c69694fd | -6.77602 | -58.67336 | 2026-08-22 05:23:00 | NOAA-20 | MAUÉS | AMAZONAS | Brasil | 1302900 | 13 | 33 | nan | nan | nan | Amazônia | 1.6 |
| 82296cec-c1f3-38cb-929a-228f1ec85d5c | -3.07856 | -61.06439 | 2026-08-22 05:23:00 | NOAA-20 | MANACAPURU | AMAZONAS | Brasil | 1302504 | 13 | 33 | nan | nan | nan | Amazônia | 2.0 |
| fd9d2a54-53ad-30ff-be1d-a8a1863c8fc7 | -6.97825 | -59.58654 | 2026-08-22 05:23:00 | NOAA-20 | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 1.1 |
| 77d52e2e-f7dd-30d7-8868-5a4302edc74d | -6.85328 | -59.43142 | 2026-08-22 05:23:00 | NOAA-20 | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 1.9 |
| d80ef4a2-3867-3133-91b5-4db296f5f2ec | -1.98464 | -56.46677 | 2026-08-22 05:23:00 | NOAA-20 | TERRA SANTA | PARÁ | Brasil | 1507979 | 15 | 33 | nan | nan | nan | Amazônia | 1.1 |
| 5aa62194-64ab-3507-bb74-33a305caf656 | -6.66226 | -56.34188 | 2026-08-22 05:23:00 | NOAA-20 | ITAITUBA | PARÁ | Brasil | 1503606 | 15 | 33 | nan | nan | nan | Amazônia | 1.0 |
| 809992c0-48ce-3d0e-8234-9df2aa948f6c | -6.38305 | -54.96319 | 2026-08-22 05:23:00 | NOAA-20 | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 1.2 |
| a5b578ca-1854-3596-80bd-54a772ad8b35 | -6.78325 | -59.42385 | 2026-08-22 05:23:00 | NOAA-20 | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 16.2 |
| 3ca4bcbd-e4b3-3ca1-b24b-60e1155a5de9 | -7.60933 | -60.97656 | 2026-08-22 05:23:00 | NOAA-20 | NOVO ARIPUANÃ | AMAZONAS | Brasil | 1303304 | 13 | 33 | nan | nan | nan | Amazônia | 2.0 |
| 0912dfc3-3808-3e58-b5d9-95d7cae71aa2 | -6.89139 | -59.40561 | 2026-08-22 05:23:00 | NOAA-20 | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 0.7 |
| a658b8b5-5dfa-3c0b-9a11-65b6ca16f45e | -11.20252 | -55.07008 | 2026-08-22 05:23:00 | NOAA-20 | ITAÚBA | MATO GROSSO | Brasil | 5104559 | 51 | 33 | nan | nan | nan | Amazônia | 1.4 |
| cc91d962-bd9d-3408-b4b2-d23d578b742c | -6.43632 | -56.18547 | 2026-08-22 05:23:00 | NOAA-20 | ITAITUBA | PARÁ | Brasil | 1503606 | 15 | 33 | nan | nan | nan | Amazônia | 0.8 |
| 6d108eda-7e6a-3d5a-951b-4032de6caf2c | -7.05715 | -59.83699 | 2026-08-22 05:23:00 | NOAA-20 | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 2.1 |
| 826edae9-99ac-386c-9054-644329f52f67 | -7.60104 | -60.83409 | 2026-08-22 05:23:00 | NOAA-20 | NOVO ARIPUANÃ | AMAZONAS | Brasil | 1303304 | 13 | 33 | nan | nan | nan | Amazônia | 1.0 |
| 1214a353-2b2a-35b2-ac16-a3f9a4c1dd9e | -6.88027 | -59.41088 | 2026-08-22 05:23:00 | NOAA-20 | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 1.7 |
| 67bd3c72-62d2-3e79-99f8-e09a4892ec18 | -14.13861 | -48.07273 | 2026-08-22 05:23:00 | NOAA-20 | COLINAS DO SUL | GOIÁS | Brasil | 5205521 | 52 | 33 | nan | nan | nan | Cerrado | 2.7 |
| 750cd3be-7d55-3b32-9ba8-024d55085603 | -6.94092 | -59.30708 | 2026-08-22 05:23:00 | NOAA-20 | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 0.8 |
| 417f1981-a3a1-35f6-920d-ae5581ecab73 | -6.54751 | -56.26302 | 2026-08-22 05:23:00 | NOAA-20 | ITAITUBA | PARÁ | Brasil | 1503606 | 15 | 33 | nan | nan | nan | Amazônia | 1.9 |
| 89c0f03a-71ef-3d56-be89-a70248c09cf7 | -3.35147 | -59.68301 | 2026-08-22 05:23:00 | NOAA-20 | CAREIRO DA VÁRZEA | AMAZONAS | Brasil | 1301159 | 13 | 33 | nan | nan | nan | Amazônia | 1.1 |
| 2f4fe890-9a85-3aaf-8fcf-74dad489f030 | -6.11761 | -57.69334 | 2026-08-22 05:23:00 | NOAA-20 | JACAREACANGA | PARÁ | Brasil | 1503754 | 15 | 33 | nan | nan | nan | Amazônia | 1.8 |
| ff5ab70e-8126-38d2-bcaf-39ad2543a925 | -6.53714 | -58.52913 | 2026-08-22 05:23:00 | NOAA-20 | MAUÉS | AMAZONAS | Brasil | 1302900 | 13 | 33 | nan | nan | nan | Amazônia | 7.4 |
| cf9b8b8e-8957-36c8-83cf-b259682ac861 | -14.42327 | -51.7977 | 2026-08-22 05:23:00 | NOAA-20 | NOVA NAZARÉ | MATO GROSSO | Brasil | 5106174 | 51 | 33 | nan | nan | nan | Cerrado | 3.5 |
| ceb89c37-76c9-3d20-86a7-cd67a3705d8a | -6.88479 | -59.42585 | 2026-08-22 05:23:00 | NOAA-20 | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 1.1 |
| 465565e7-da02-3104-a04c-dc33aebff78f | -6.81082 | -59.42113 | 2026-08-22 05:23:00 | NOAA-20 | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 2.7 |
| 758d2c8e-b3ba-36af-ad73-e514d01d9c0a | -3.82198 | -55.66961 | 2026-08-22 05:23:00 | NOAA-20 | AVEIRO | PARÁ | Brasil | 1501006 | 15 | 33 | nan | nan | nan | Amazônia | 1.1 |
| c8ee23d8-6761-363a-abc6-c6e101be06cf | -8.6319 | -54.69737 | 2026-08-22 05:23:00 | NOAA-20 | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 2.8 |
| dfb07c21-c429-346e-9d02-a3f357e49348 | -13.83681 | -54.00254 | 2026-08-22 05:23:00 | NOAA-20 | PARANATINGA | MATO GROSSO | Brasil | 5106307 | 51 | 33 | nan | nan | nan | Cerrado | 1.5 |
| b7719ef4-be43-3704-b4fd-da6a897c46dd | -6.72315 | -59.0949 | 2026-08-22 05:23:00 | NOAA-20 | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 1.4 |
| 2c528d8d-62d0-38b6-9fa4-26a2ee652c8f | -6.86549 | -59.03265 | 2026-08-22 05:23:00 | NOAA-20 | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 3.3 |
| c87bc1d7-d947-3491-8e03-99fe2ac357e5 | -6.12715 | -57.7206 | 2026-08-22 05:23:00 | NOAA-20 | JACAREACANGA | PARÁ | Brasil | 1503754 | 15 | 33 | nan | nan | nan | Amazônia | 3.9 |
| 0983fff7-b6d7-3a8d-8973-029207bb3426 | -8.63431 | -54.73703 | 2026-08-22 05:23:00 | NOAA-20 | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 1.9 |
| c83091ad-0179-3283-9e5d-cfc66d8e76f7 | -9.00006 | -50.71432 | 2026-08-22 05:23:00 | NOAA-20 | SANTANA DO ARAGUAIA | PARÁ | Brasil | 1506708 | 15 | 33 | nan | nan | nan | Amazônia | 2.1 |
| 7c9dfaa8-a6a2-394c-bc2c-2b400d4a7ab2 | -6.0016 | -57.80751 | 2026-08-22 05:23:00 | NOAA-20 | JACAREACANGA | PARÁ | Brasil | 1503754 | 15 | 33 | nan | nan | nan | Amazônia | 0.8 |
| d12ff037-e9d1-3242-80da-97775bb705c7 | -6.11034 | -53.07479 | 2026-08-22 05:23:00 | NOAA-20 | SÃO FÉLIX DO XINGU | PARÁ | Brasil | 1507300 | 15 | 33 | nan | nan | nan | Amazônia | 1.5 |
| 14052a1d-cc18-3343-9da4-8b6647506ae5 | -8.99474 | -50.71384 | 2026-08-22 05:23:00 | NOAA-20 | SANTANA DO ARAGUAIA | PARÁ | Brasil | 1506708 | 15 | 33 | nan | nan | nan | Amazônia | 2.1 |
| 81ed76d3-c503-3025-928b-513713d2f1b6 | -12.93955 | -56.62165 | 2026-08-22 05:23:00 | NOAA-20 | NOVA MUTUM | MATO GROSSO | Brasil | 5106224 | 51 | 33 | nan | nan | nan | Amazônia | 3.3 |
| ea8d5b3b-8422-3267-9214-c20ed8a6fc3c | -7.43159 | -59.79059 | 2026-08-22 05:23:00 | NOAA-20 | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 1.5 |
| 1b33c249-4958-387c-a0e8-fef2d22cbdd0 | -7.10138 | -59.77277 | 2026-08-22 05:23:00 | NOAA-20 | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 1.2 |
| 55815932-1944-3063-bc44-6cfa3eaed49a | -6.80208 | -59.58299 | 2026-08-22 05:23:00 | NOAA-20 | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 0.8 |
| 6342d134-b97f-3cd1-a0a7-f64752a88d6f | -8.59179 | -54.74872 | 2026-08-22 05:23:00 | NOAA-20 | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 1.5 |
| 4f25742c-60db-356f-8be1-29b790688f56 | -8.52983 | -54.82288 | 2026-08-22 05:23:00 | NOAA-20 | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 6.6 |
| 64822854-89e7-33cd-8033-01a521cc39a8 | -6.86218 | -59.03213 | 2026-08-22 05:23:00 | NOAA-20 | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 3.3 |
| 6d9fa568-d28e-3bae-a809-39321d93b0d9 | -7.2642 | -60.62206 | 2026-08-22 05:23:00 | NOAA-20 | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 1.4 |
| b4b8bcb9-f23a-385c-86dc-58fd85fec0ad | -8.63539 | -54.70152 | 2026-08-22 05:23:00 | NOAA-20 | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 2.8 |
| 85740dfb-8b8c-38fe-8b92-9d911c3cb372 | -6.08059 | -57.7097 | 2026-08-22 05:23:00 | NOAA-20 | JACAREACANGA | PARÁ | Brasil | 1503754 | 15 | 33 | nan | nan | nan | Amazônia | 2.2 |
| 2dd405eb-6d5a-3f2d-a796-48cd562efdb1 | -6.88093 | -59.42878 | 2026-08-22 05:23:00 | NOAA-20 | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 0.9 |
| 484a0fb9-71e3-3276-81de-bdc10b9aa5cc | -6.66289 | -56.3378 | 2026-08-22 05:23:00 | NOAA-20 | ITAITUBA | PARÁ | Brasil | 1503606 | 15 | 33 | nan | nan | nan | Amazônia | 1.0 |
| 01803f9f-7947-3d82-94e3-97b86fd96549 | -6.78436 | -59.43822 | 2026-08-22 05:23:00 | NOAA-20 | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 2.6 |
| 2fabfb47-3de9-3555-906f-27e7f1487dbd | -8.10133 | -50.04647 | 2026-08-22 05:23:00 | NOAA-20 | REDENÇÃO | PARÁ | Brasil | 1506138 | 15 | 33 | nan | nan | nan | Amazônia | 1.9 |
| 6ac9df47-79fc-3a65-b280-59b9a1189332 | -6.80585 | -59.4097 | 2026-08-22 05:23:00 | NOAA-20 | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 2.5 |
| 711bc53d-ad9d-374c-8b60-58f84253c101 | -6.11266 | -59.94392 | 2026-08-22 05:23:00 | NOAA-20 | NOVO ARIPUANÃ | AMAZONAS | Brasil | 1303304 | 13 | 33 | nan | nan | nan | Amazônia | 1.3 |
| 18cf1aba-cc93-376b-b5e1-c8e4b694f3ce | -6.22817 | -55.48275 | 2026-08-22 05:23:00 | NOAA-20 | ITAITUBA | PARÁ | Brasil | 1503606 | 15 | 33 | nan | nan | nan | Amazônia | 1.8 |
| e4b5e2cd-c095-36fd-8e81-4032777bf186 | -6.88116 | -56.63502 | 2026-08-22 05:23:00 | NOAA-20 | ITAITUBA | PARÁ | Brasil | 1503606 | 15 | 33 | nan | nan | nan | Amazônia | 1.3 |
| a4211138-84ae-3bd2-af83-5b80bacad892 | -6.23442 | -55.41592 | 2026-08-22 05:23:00 | NOAA-20 | ITAITUBA | PARÁ | Brasil | 1503606 | 15 | 33 | nan | nan | nan | Amazônia | 2.2 |
| 25fd300b-e1f6-3d80-a075-2e7c1c3c7005 | -6.79933 | -59.66431 | 2026-08-22 05:23:00 | NOAA-20 | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 1.8 |
| 0b5cd32d-7704-349c-8fdb-2d282e74371d | -7.0207 | -59.55428 | 2026-08-22 05:23:00 | NOAA-20 | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 1.3 |
| 96e0925d-4887-399e-808c-8102bdabe36e | -14.39597 | -51.80102 | 2026-08-22 05:23:00 | NOAA-20 | NOVA NAZARÉ | MATO GROSSO | Brasil | 5106174 | 51 | 33 | nan | nan | nan | Cerrado | 3.1 |
| 27f0d74f-edaf-3d50-a628-cb595978aa82 | -1.98522 | -56.46312 | 2026-08-22 05:23:00 | NOAA-20 | TERRA SANTA | PARÁ | Brasil | 1507979 | 15 | 33 | nan | nan | nan | Amazônia | 1.5 |
| d0c6f2c5-0319-34c1-ba02-18c7c452d7c9 | -6.79428 | -59.41851 | 2026-08-22 05:23:00 | NOAA-20 | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 28.2 |
| 17bcff21-828c-3222-a3ac-b4b19125c2cc | -6.76113 | -58.7031 | 2026-08-22 05:23:00 | NOAA-20 | MAUÉS | AMAZONAS | Brasil | 1302900 | 13 | 33 | nan | nan | nan | Amazônia | 1.6 |
| 89ac4358-ab1e-33c2-8149-8e1b80375e88 | -4.94428 | -55.78376 | 2026-08-22 05:23:00 | NOAA-20 | TRAIRÃO | PARÁ | Brasil | 1508050 | 15 | 33 | nan | nan | nan | Amazônia | 1.6 |
| 737e6f90-c264-3fe1-9d3a-23e3fd1ce877 | -5.96411 | -51.95448 | 2026-08-22 05:23:00 | NOAA-20 | SÃO FÉLIX DO XINGU | PARÁ | Brasil | 1507300 | 15 | 33 | nan | nan | nan | Amazônia | 1.3 |


[Clique aqui para ver as próximas entradas](README65.md)
