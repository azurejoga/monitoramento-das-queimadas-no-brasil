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
| 9b143ef4-fa3e-3d5f-aac6-53afcd14187d | -16.09079 | -52.34297 | 2026-08-24 04:49:00 | NOAA-20 | ARAGARÇAS | GOIÁS | Brasil | 5201702 | 52 | 33 | nan | nan | nan | Cerrado | 2.3 |
| 4f87bd47-feb9-381a-acdd-d4a8a59cbd1c | -20.91296 | -57.62219 | 2026-08-24 04:49:00 | NOAA-20 | PORTO MURTINHO | MATO GROSSO DO SUL | Brasil | 5006903 | 50 | 33 | nan | nan | nan | Pantanal | 0.7 |
| 40b85cb9-a0a9-3ccc-a2ac-6cb058a3eb00 | -15.26605 | -52.8198 | 2026-08-24 04:49:00 | NOAA-20 | BARRA DO GARÇAS | MATO GROSSO | Brasil | 5101803 | 51 | 33 | nan | nan | nan | Cerrado | 1.3 |
| 7715ff9c-69e2-3ae5-9c39-cd838e212f15 | -15.24836 | -52.80174 | 2026-08-24 04:49:00 | NOAA-20 | BARRA DO GARÇAS | MATO GROSSO | Brasil | 5101803 | 51 | 33 | nan | nan | nan | Cerrado | 3.2 |
| 0676307a-ad92-3fa0-8eeb-3924797c4d57 | -15.27129 | -52.85099 | 2026-08-24 04:49:00 | NOAA-20 | BARRA DO GARÇAS | MATO GROSSO | Brasil | 5101803 | 51 | 33 | nan | nan | nan | Cerrado | 2.4 |
| 3b5436a8-47c1-3f14-85b9-a19a98cb5186 | -15.49737 | -52.90431 | 2026-08-24 04:49:00 | NOAA-20 | BARRA DO GARÇAS | MATO GROSSO | Brasil | 5101803 | 51 | 33 | nan | nan | nan | Cerrado | 1.8 |
| c1b225f6-c079-31e7-8519-cac91ff33b72 | -16.06106 | -50.44359 | 2026-08-24 04:49:00 | NOAA-20 | GOIÁS | GOIÁS | Brasil | 5208905 | 52 | 33 | nan | nan | nan | Cerrado | 3.5 |
| 4c647d62-9de3-33dd-8beb-851819fa0d65 | -15.2707 | -52.85466 | 2026-08-24 04:49:00 | NOAA-20 | BARRA DO GARÇAS | MATO GROSSO | Brasil | 5101803 | 51 | 33 | nan | nan | nan | Cerrado | 20.1 |
| 72eb6929-2297-32f5-9188-134c34276a45 | -16.38696 | -51.82616 | 2026-08-24 04:49:00 | NOAA-20 | PIRANHAS | GOIÁS | Brasil | 5217203 | 52 | 33 | nan | nan | nan | Cerrado | 2.9 |
| a0aaa413-9c1f-3359-bc6d-8e57dbd1f704 | -15.44215 | -52.84206 | 2026-08-24 04:49:00 | NOAA-20 | BARRA DO GARÇAS | MATO GROSSO | Brasil | 5101803 | 51 | 33 | nan | nan | nan | Cerrado | 0.3 |
| 42a5545c-df85-3f84-a018-da7f03e14803 | -15.2627 | -52.81923 | 2026-08-24 04:49:00 | NOAA-20 | BARRA DO GARÇAS | MATO GROSSO | Brasil | 5101803 | 51 | 33 | nan | nan | nan | Cerrado | 1.3 |
| b5e6e4ae-8c39-35b6-84d5-c6a0ff8a1d85 | -14.94569 | -52.65625 | 2026-08-24 04:49:00 | NOAA-20 | BARRA DO GARÇAS | MATO GROSSO | Brasil | 5101803 | 51 | 33 | nan | nan | nan | Cerrado | 2.1 |
| 6d062476-d438-39c2-bad0-7c0c3b057c57 | -16.41781 | -51.84613 | 2026-08-24 04:49:00 | NOAA-20 | PIRANHAS | GOIÁS | Brasil | 5217203 | 52 | 33 | nan | nan | nan | Cerrado | 3.6 |
| dac02615-6b28-35eb-ac44-80b9ab8929ae | -16.06443 | -50.44414 | 2026-08-24 04:49:00 | NOAA-20 | GOIÁS | GOIÁS | Brasil | 5208905 | 52 | 33 | nan | nan | nan | Cerrado | 5.6 |
| 6f15c2ee-c8b3-3f1b-898b-92f379175f48 | -15.26665 | -52.81614 | 2026-08-24 04:49:00 | NOAA-20 | BARRA DO GARÇAS | MATO GROSSO | Brasil | 5101803 | 51 | 33 | nan | nan | nan | Cerrado | 1.3 |
| 46be9223-d9bc-3f58-8f62-cc566d238100 | -15.78991 | -56.06782 | 2026-08-24 04:49:00 | NOAA-20 | SANTO ANTÔNIO DO LEVERGER | MATO GROSSO | Brasil | 5107800 | 51 | 33 | nan | nan | nan | Pantanal | 3.3 |
| 0e84ae0b-bfde-3a49-8a98-d2122bcc5547 | -16.39746 | -51.82425 | 2026-08-24 04:49:00 | NOAA-20 | PIRANHAS | GOIÁS | Brasil | 5217203 | 52 | 33 | nan | nan | nan | Cerrado | 1.3 |
| 9ab400c7-d079-3cef-b6ff-222e4810c165 | -17.43769 | -48.83826 | 2026-08-24 04:49:00 | NOAA-20 | PIRACANJUBA | GOIÁS | Brasil | 5217104 | 52 | 33 | nan | nan | nan | Cerrado | 1.2 |
| b6382018-4d9b-38f2-9daf-240c3d1d13cb | -16.05993 | -50.45101 | 2026-08-24 04:49:00 | NOAA-20 | GOIÁS | GOIÁS | Brasil | 5208905 | 52 | 33 | nan | nan | nan | Cerrado | 2.1 |
| bc3819c6-53bf-3e38-8459-9f956e4fb907 | -16.14292 | -50.24618 | 2026-08-24 04:49:00 | NOAA-20 | MOSSÂMEDES | GOIÁS | Brasil | 5213905 | 52 | 33 | nan | nan | nan | Cerrado | 3.3 |
| 2b397ba0-10a5-30e4-b2ed-7062bb56d748 | -16.30241 | -53.15601 | 2026-08-24 04:49:00 | NOAA-20 | GUIRATINGA | MATO GROSSO | Brasil | 5104203 | 51 | 33 | nan | nan | nan | Cerrado | 0.5 |
| e9c37891-2d3d-357a-a483-09635edbe80e | -15.30404 | -52.81895 | 2026-08-24 04:49:00 | NOAA-20 | BARRA DO GARÇAS | MATO GROSSO | Brasil | 5101803 | 51 | 33 | nan | nan | nan | Cerrado | 2.1 |
| d38dab6a-898e-354f-b967-56905c442da8 | -16.06387 | -50.44786 | 2026-08-24 04:49:00 | NOAA-20 | GOIÁS | GOIÁS | Brasil | 5208905 | 52 | 33 | nan | nan | nan | Cerrado | 5.6 |
| 5ba44c2e-2223-3db0-8171-9f5edaeab639 | -15.28337 | -52.81913 | 2026-08-24 04:49:00 | NOAA-20 | BARRA DO GARÇAS | MATO GROSSO | Brasil | 5101803 | 51 | 33 | nan | nan | nan | Cerrado | 2.2 |
| 42a1eabb-d840-3643-8c66-22556c7ea889 | -16.02162 | -45.52134 | 2026-08-24 04:49:00 | NOAA-20 | URUCUIA | MINAS GERAIS | Brasil | 3170529 | 31 | 33 | nan | nan | nan | Cerrado | 1.3 |
| 9b409997-e022-31bb-ab7c-b7c424e7dead | -15.07624 | -52.77633 | 2026-08-24 04:49:00 | NOAA-20 | BARRA DO GARÇAS | MATO GROSSO | Brasil | 5101803 | 51 | 33 | nan | nan | nan | Cerrado | 0.6 |
| cd870d12-51ed-3fa8-a3f5-1084ed7db692 | -14.3365 | -51.7662 | 2026-08-24 04:50:00 | GOES-19 | NOVA NAZARÉ | MATO GROSSO | Brasil | 5106174 | 51 | 33 | nan | nan | nan | Cerrado | 60.7 |
| d9459796-d0ff-3fe1-a3d6-9a6647c3b0e7 | -10.0481 | -46.4341 | 2026-08-24 04:50:00 | GOES-19 | ALTO PARNAÍBA | MARANHÃO | Brasil | 2100501 | 21 | 33 | nan | nan | nan | Cerrado | 79.3 |
| c4444a35-fed4-3059-b8f5-41ed68bf3e49 | -14.7791 | -48.7659 | 2026-08-24 04:50:00 | GOES-19 | BARRO ALTO | GOIÁS | Brasil | 5203203 | 52 | 33 | nan | nan | nan | Cerrado | 62.7 |
| 7330994f-aafb-3512-b0c7-559835c24e26 | -7.685 | -63.3255 | 2026-08-24 04:50:00 | GOES-19 | HUMAITÁ | AMAZONAS | Brasil | 1301704 | 13 | 33 | nan | nan | nan | Amazônia | 66.3 |
| c4e674c4-b1cf-3c9d-a56a-3829d6779ea9 | -14.3171 | -51.7688 | 2026-08-24 04:50:00 | GOES-19 | NOVA NAZARÉ | MATO GROSSO | Brasil | 5106174 | 51 | 33 | nan | nan | nan | Cerrado | 50.3 |
| 4343fd0e-4d6e-3f05-8074-dbea30edecc9 | -7.6849 | -63.3443 | 2026-08-24 05:00:00 | GOES-19 | HUMAITÁ | AMAZONAS | Brasil | 1301704 | 13 | 33 | nan | nan | nan | Amazônia | 74.8 |
| 67742229-c89d-3459-92b6-4ac64e9f161a | -7.6851 | -63.3067 | 2026-08-24 05:00:00 | GOES-19 | HUMAITÁ | AMAZONAS | Brasil | 1301704 | 13 | 33 | nan | nan | nan | Amazônia | 45.2 |
| 8e8adb10-b271-3084-8926-a7427dd46640 | -7.6665 | -63.3261 | 2026-08-24 05:00:00 | GOES-19 | HUMAITÁ | AMAZONAS | Brasil | 1301704 | 13 | 33 | nan | nan | nan | Amazônia | 48.1 |
| dabcda5b-b045-3464-90ff-62742bf3469e | -7.685 | -63.3255 | 2026-08-24 05:00:00 | GOES-19 | HUMAITÁ | AMAZONAS | Brasil | 1301704 | 13 | 33 | nan | nan | nan | Amazônia | 151.1 |
| ba8043cd-f526-30b5-9476-c159b6b1c254 | -7.6851 | -63.3067 | 2026-08-24 05:10:00 | GOES-19 | HUMAITÁ | AMAZONAS | Brasil | 1301704 | 13 | 33 | nan | nan | nan | Amazônia | 45.5 |
| 1559fe72-2845-3b47-9f1c-282d39003d9f | -7.6849 | -63.3443 | 2026-08-24 05:10:00 | GOES-19 | HUMAITÁ | AMAZONAS | Brasil | 1301704 | 13 | 33 | nan | nan | nan | Amazônia | 50.1 |
| 63fdf733-1ed2-3013-b3df-684f1024a371 | -7.685 | -63.3255 | 2026-08-24 05:10:00 | GOES-19 | HUMAITÁ | AMAZONAS | Brasil | 1301704 | 13 | 33 | nan | nan | nan | Amazônia | 131.5 |
| 0c76734b-03a5-307f-b1fd-2c05710d9ed6 | -14.3368 | -51.7448 | 2026-08-24 05:10:00 | GOES-19 | NOVA NAZARÉ | MATO GROSSO | Brasil | 5106174 | 51 | 33 | nan | nan | nan | Cerrado | 51.6 |
| a1a1cdda-60c9-329e-b18f-937ba9291148 | -7.685 | -63.3255 | 2026-08-24 05:20:00 | GOES-19 | HUMAITÁ | AMAZONAS | Brasil | 1301704 | 13 | 33 | nan | nan | nan | Amazônia | 61.9 |
| 3c3f4384-cfad-34ef-a5b7-ccf3a7d99e8d | -12.0941 | -50.5951 | 2026-08-24 05:20:00 | GOES-19 | FORMOSO DO ARAGUAIA | TOCANTINS | Brasil | 1708205 | 17 | 33 | nan | nan | nan | Cerrado | 91.8 |
| fc9c137d-9105-3cfd-8533-60dc4eafa4e5 | -12.0938 | -50.6166 | 2026-08-24 05:20:00 | GOES-19 | FORMOSO DO ARAGUAIA | TOCANTINS | Brasil | 1708205 | 17 | 33 | nan | nan | nan | Cerrado | 93.2 |
| 9c2c5d5c-5f60-3a7a-880f-e52e81d5996d | -12.1128 | -50.6143 | 2026-08-24 05:20:00 | GOES-19 | FORMOSO DO ARAGUAIA | TOCANTINS | Brasil | 1708205 | 17 | 33 | nan | nan | nan | Cerrado | 194.3 |
| 6603dfb2-b14a-3481-a9fd-0ba34c189c5b | -12.1132 | -50.5929 | 2026-08-24 05:20:00 | GOES-19 | FORMOSO DO ARAGUAIA | TOCANTINS | Brasil | 1708205 | 17 | 33 | nan | nan | nan | Cerrado | 134.3 |
| 46b66567-adc3-3667-8d0c-e3b4640d7064 | -16.0919 | -52.3335 | 2026-08-24 05:20:00 | GOES-19 | ARAGARÇAS | GOIÁS | Brasil | 5201702 | 52 | 33 | nan | nan | nan | Cerrado | 58.7 |
| 2800d9c3-ffd2-3052-b5ab-d9a4d128acb2 | -2.43754 | -54.75869 | 2026-08-24 05:27:00 | NOAA-21 | SANTARÉM | PARÁ | Brasil | 1506807 | 15 | 33 | nan | nan | nan | Amazônia | 1.7 |
| 6b25fe87-fa74-3e1d-89f2-5d7bf953242a | -2.75148 | -58.04467 | 2026-08-24 05:27:00 | NOAA-21 | ITAPIRANGA | AMAZONAS | Brasil | 1302009 | 13 | 33 | nan | nan | nan | Amazônia | 1.7 |
| 247e651e-ff9e-3707-b9d2-1841a0e7104c | -3.53402 | -48.18336 | 2026-08-24 05:27:00 | NOAA-21 | PARAGOMINAS | PARÁ | Brasil | 1505502 | 15 | 33 | nan | nan | nan | Amazônia | 7.3 |
| ecbda69c-a8dd-3f1f-baac-e5d3ddb9895e | -3.53498 | -48.17669 | 2026-08-24 05:27:00 | NOAA-21 | PARAGOMINAS | PARÁ | Brasil | 1505502 | 15 | 33 | nan | nan | nan | Amazônia | 5.7 |
| 240093cd-8868-370d-888e-7e1ad3b3e9f1 | -3.54192 | -48.17805 | 2026-08-24 05:27:00 | NOAA-21 | PARAGOMINAS | PARÁ | Brasil | 1505502 | 15 | 33 | nan | nan | nan | Amazônia | 5.7 |
| 6b8f88c0-a992-34f6-bf67-7e3b93520322 | -1.7456 | -55.24913 | 2026-08-24 05:27:00 | NOAA-21 | ÓBIDOS | PARÁ | Brasil | 1505106 | 15 | 33 | nan | nan | nan | Amazônia | 1.5 |
| 962b1cc3-a288-39d1-a9f6-8f6450dcfee3 | -3.53977 | -48.18253 | 2026-08-24 05:27:00 | NOAA-21 | PARAGOMINAS | PARÁ | Brasil | 1505502 | 15 | 33 | nan | nan | nan | Amazônia | 17.2 |
| bd54bfef-1aba-3628-a275-2e58e5c5466e | -3.5331 | -48.18973 | 2026-08-24 05:27:00 | NOAA-21 | PARAGOMINAS | PARÁ | Brasil | 1505502 | 15 | 33 | nan | nan | nan | Amazônia | 7.3 |
| b5d8c01f-bf66-3f22-b395-7c5cd706736a | -3.54097 | -48.18465 | 2026-08-24 05:27:00 | NOAA-21 | PARAGOMINAS | PARÁ | Brasil | 1505502 | 15 | 33 | nan | nan | nan | Amazônia | 7.3 |
| 858ee19d-f735-39a3-9d7f-8a65f03679a3 | -3.42525 | -50.09772 | 2026-08-24 05:27:00 | NOAA-21 | PACAJÁ | PARÁ | Brasil | 1505486 | 15 | 33 | nan | nan | nan | Amazônia | 0.8 |
| 5e1120eb-90e3-3dd5-a250-800d45d47b44 | -3.42597 | -50.09264 | 2026-08-24 05:27:00 | NOAA-21 | PACAJÁ | PARÁ | Brasil | 1505486 | 15 | 33 | nan | nan | nan | Amazônia | 0.6 |
| 1c2bf40b-302b-3c24-b017-e981ec12716a | -1.47832 | -54.96415 | 2026-08-24 05:27:00 | NOAA-21 | ALENQUER | PARÁ | Brasil | 1500404 | 15 | 33 | nan | nan | nan | Amazônia | 3.5 |
| f113d13a-cb9e-3880-b586-5c74b17d5831 | -6.85764 | -59.40725 | 2026-08-24 05:29:00 | NOAA-21 | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 2.1 |
| 86ab568d-86f3-39e7-8cbf-5d5985cf8789 | -7.69051 | -63.33484 | 2026-08-24 05:29:00 | NOAA-21 | HUMAITÁ | AMAZONAS | Brasil | 1301704 | 13 | 33 | nan | nan | nan | Amazônia | 11.2 |
| 5ce5e566-ab29-35b3-ad78-8d5ce2a45caa | -6.88054 | -56.63927 | 2026-08-24 05:29:00 | NOAA-21 | ITAITUBA | PARÁ | Brasil | 1503606 | 15 | 33 | nan | nan | nan | Amazônia | 0.7 |
| 55f637a2-ae76-349a-90da-250068cf7701 | -5.68846 | -53.74197 | 2026-08-24 05:29:00 | NOAA-21 | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 0.8 |
| 3365aac4-55e4-3f56-a54e-9835e1b80b07 | -7.76757 | -61.10606 | 2026-08-24 05:29:00 | NOAA-21 | NOVO ARIPUANÃ | AMAZONAS | Brasil | 1303304 | 13 | 33 | nan | nan | nan | Amazônia | 2.1 |
| 923fb5e1-7474-3815-ab59-0306cde92d3a | -6.34849 | -54.75456 | 2026-08-24 05:29:00 | NOAA-21 | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 3.7 |
| 853f3848-b292-3f7c-99ed-c3fa48a471b4 | -9.03005 | -50.7548 | 2026-08-24 05:29:00 | NOAA-21 | SANTANA DO ARAGUAIA | PARÁ | Brasil | 1506708 | 15 | 33 | nan | nan | nan | Amazônia | 5.0 |
| 23178249-91f6-3de1-a52b-e4e4dc2740ca | -4.53512 | -55.51361 | 2026-08-24 05:29:00 | NOAA-21 | RURÓPOLIS | PARÁ | Brasil | 1506195 | 15 | 33 | nan | nan | nan | Amazônia | 1.2 |
| cdbf06cc-7735-3187-a37e-4f2b3edd9941 | -6.61597 | -58.38317 | 2026-08-24 05:29:00 | NOAA-21 | JACAREACANGA | PARÁ | Brasil | 1503754 | 15 | 33 | nan | nan | nan | Amazônia | 6.2 |
| ae00a93b-8c79-3fad-9c98-74eae1cebd3a | -6.79635 | -59.81378 | 2026-08-24 05:29:00 | NOAA-21 | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 1.7 |
| 7d815688-98fe-3b82-b741-37767cc3dec4 | -6.22116 | -55.9206 | 2026-08-24 05:29:00 | NOAA-21 | ITAITUBA | PARÁ | Brasil | 1503606 | 15 | 33 | nan | nan | nan | Amazônia | 1.8 |
| 7ec01b0a-5e50-3a12-aa34-79eabd387aef | -6.79734 | -59.59156 | 2026-08-24 05:29:00 | NOAA-21 | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 2.4 |
| 4812ee7b-f0a0-32c7-a834-3ebb6636428d | -6.74776 | -59.65462 | 2026-08-24 05:29:00 | NOAA-21 | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 2.5 |
| fd87d936-b7b6-37fe-9d4c-85e2e4d673a8 | -4.53446 | -55.51797 | 2026-08-24 05:29:00 | NOAA-21 | RURÓPOLIS | PARÁ | Brasil | 1506195 | 15 | 33 | nan | nan | nan | Amazônia | 1.2 |
| 4add1fc6-38c4-313b-9ae6-8e6600aab442 | -6.18356 | -53.53157 | 2026-08-24 05:29:00 | NOAA-21 | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 3.5 |
| 8d6c20b8-7e50-3cb3-a205-893fcac72a37 | -9.05303 | -50.76907 | 2026-08-24 05:29:00 | NOAA-21 | SANTANA DO ARAGUAIA | PARÁ | Brasil | 1506708 | 15 | 33 | nan | nan | nan | Amazônia | 2.5 |
| 01f0b15b-3bcb-36b5-b510-f90f1b01d336 | -6.89675 | -55.69943 | 2026-08-24 05:29:00 | NOAA-21 | NOVO PROGRESSO | PARÁ | Brasil | 1505031 | 15 | 33 | nan | nan | nan | Amazônia | 2.0 |
| 1ac06fa8-e4c6-3cbf-a73a-d56e873f3c0a | -6.61419 | -58.39006 | 2026-08-24 05:29:00 | NOAA-21 | JACAREACANGA | PARÁ | Brasil | 1503754 | 15 | 33 | nan | nan | nan | Amazônia | 5.7 |
| ad1cc3b3-23f1-31a6-9dc0-d45a2f49474b | -5.94347 | -57.72644 | 2026-08-24 05:29:00 | NOAA-21 | JACAREACANGA | PARÁ | Brasil | 1503754 | 15 | 33 | nan | nan | nan | Amazônia | 3.3 |
| efa931ad-6945-382b-b9d7-d4c6c11e664a | -5.87178 | -57.56469 | 2026-08-24 05:29:00 | NOAA-21 | JACAREACANGA | PARÁ | Brasil | 1503754 | 15 | 33 | nan | nan | nan | Amazônia | 3.3 |
| 8017e958-2b6a-3048-8174-8ed052b812a6 | -6.96288 | -59.08177 | 2026-08-24 05:29:00 | NOAA-21 | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 2.5 |
| 68f87480-e2a4-3351-a355-29e16c6b1c40 | -7.78804 | -56.28669 | 2026-08-24 05:29:00 | NOAA-21 | ITAITUBA | PARÁ | Brasil | 1503606 | 15 | 33 | nan | nan | nan | Amazônia | 1.9 |
| 9db2eb0e-97eb-3c9b-9b21-a3e129c5dd46 | -6.59662 | -52.45348 | 2026-08-24 05:29:00 | NOAA-21 | SÃO FÉLIX DO XINGU | PARÁ | Brasil | 1507300 | 15 | 33 | nan | nan | nan | Amazônia | 1.8 |
| 4532a25d-f852-3901-a1d9-5b32ef190db7 | -6.81268 | -58.65208 | 2026-08-24 05:29:00 | NOAA-21 | MAUÉS | AMAZONAS | Brasil | 1302900 | 13 | 33 | nan | nan | nan | Amazônia | 2.5 |
| b4263afc-8194-3c5c-8646-7662624df7c8 | -6.78782 | -59.6553 | 2026-08-24 05:29:00 | NOAA-21 | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 2.3 |
| e1bb9eaa-3a90-371e-bfcf-3165d0030ed5 | -7.78366 | -56.28609 | 2026-08-24 05:29:00 | NOAA-21 | ITAITUBA | PARÁ | Brasil | 1503606 | 15 | 33 | nan | nan | nan | Amazônia | 1.9 |
| a73eee33-b9f4-38f3-8cf4-4913a1707977 | -4.38186 | -55.75658 | 2026-08-24 05:29:00 | NOAA-21 | ITAITUBA | PARÁ | Brasil | 1503606 | 15 | 33 | nan | nan | nan | Amazônia | 1.2 |
| c17441c5-9784-36b0-8f07-cd2fda12e62e | -7.44326 | -59.77293 | 2026-08-24 05:29:00 | NOAA-21 | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 1.2 |
| 0177ff8a-1bd6-39e2-af36-9e175957da7d | -6.9635 | -59.07755 | 2026-08-24 05:29:00 | NOAA-21 | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 2.1 |
| beccf6e8-f10c-310e-996b-566c4ff22900 | -7.4866 | -55.33797 | 2026-08-24 05:29:00 | NOAA-21 | NOVO PROGRESSO | PARÁ | Brasil | 1505031 | 15 | 33 | nan | nan | nan | Amazônia | 1.7 |
| 7b5eadc0-b1b9-3dbe-ad79-4312bbe3a9a9 | -5.7881 | -57.56093 | 2026-08-24 05:29:00 | NOAA-21 | JACAREACANGA | PARÁ | Brasil | 1503754 | 15 | 33 | nan | nan | nan | Amazônia | 1.8 |
| 1d6892a2-19b7-3f8f-842c-b3cce96517a0 | -5.004 | -56.13568 | 2026-08-24 05:29:00 | NOAA-21 | TRAIRÃO | PARÁ | Brasil | 1508050 | 15 | 33 | nan | nan | nan | Amazônia | 2.0 |
| 646198a3-1892-3ba2-9b2a-92bd7808b546 | -6.70256 | -52.0933 | 2026-08-24 05:29:00 | NOAA-21 | SÃO FÉLIX DO XINGU | PARÁ | Brasil | 1507300 | 15 | 33 | nan | nan | nan | Amazônia | 2.0 |
| d614bbd8-aa8f-3a61-9d3a-cd4cbefc9018 | -6.96713 | -59.0781 | 2026-08-24 05:29:00 | NOAA-21 | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 2.1 |
| e4496fc4-d8c4-3492-b6e6-429db379742a | -6.15093 | -57.9359 | 2026-08-24 05:29:00 | NOAA-21 | JACAREACANGA | PARÁ | Brasil | 1503754 | 15 | 33 | nan | nan | nan | Amazônia | 4.0 |
| 500007aa-8340-3883-8584-f37d1fb6ba1f | -7.02589 | -59.56322 | 2026-08-24 05:29:00 | NOAA-21 | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 0.6 |
| ce4c8a72-a576-3ba9-9bc1-c77a045ccb8a | -4.99919 | -56.13904 | 2026-08-24 05:29:00 | NOAA-21 | TRAIRÃO | PARÁ | Brasil | 1508050 | 15 | 33 | nan | nan | nan | Amazônia | 2.0 |
| 2f3b456a-9082-3395-bdfa-2426a5431a58 | -4.99564 | -56.1358 | 2026-08-24 05:29:00 | NOAA-21 | TRAIRÃO | PARÁ | Brasil | 1508050 | 15 | 33 | nan | nan | nan | Amazônia | 1.6 |
| f723cd19-e290-3c7e-a4bf-c2c8e1923029 | -6.81138 | -58.66098 | 2026-08-24 05:29:00 | NOAA-21 | MAUÉS | AMAZONAS | Brasil | 1302900 | 13 | 33 | nan | nan | nan | Amazônia | 1.7 |
| a838fff1-a297-346a-8ecb-9e0bfa103c8c | -7.67387 | -63.33222 | 2026-08-24 05:29:00 | NOAA-21 | HUMAITÁ | AMAZONAS | Brasil | 1301704 | 13 | 33 | nan | nan | nan | Amazônia | 2.5 |
| 2bb449aa-2c54-397c-99d0-dcb54104b097 | -6.34114 | -55.86938 | 2026-08-24 05:29:00 | NOAA-21 | ITAITUBA | PARÁ | Brasil | 1503606 | 15 | 33 | nan | nan | nan | Amazônia | 1.7 |
| d58dd0f3-2b70-3113-87f1-26583b3e00f7 | -5.94838 | -57.72978 | 2026-08-24 05:29:00 | NOAA-21 | JACAREACANGA | PARÁ | Brasil | 1503754 | 15 | 33 | nan | nan | nan | Amazônia | 2.5 |
| fc04ee66-63d3-337c-9dbc-b7367770e3ce | -6.81944 | -58.65773 | 2026-08-24 05:29:00 | NOAA-21 | MAUÉS | AMAZONAS | Brasil | 1302900 | 13 | 33 | nan | nan | nan | Amazônia | 1.8 |


[Clique aqui para ver as próximas entradas](README39.md)
