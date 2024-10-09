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

## Dados Diários - Página 56

| ID | Latitude | Longitude | Data/Hora GMT | Satélite | Município | Estado | País | Município ID | Estado ID | País ID | Dias sem Chuva | Precipitação | Risco de Fogo | Bioma | FRP |
|----|----------|-----------|---------------|----------|-----------|--------|------|--------------|-----------|---------|----------------|--------------|----------------|-------|-----|
| 22803398-40d7-31c8-bf22-45a506ef4b51 | -22.1571 | -48.1409 | 2024-10-09 02:57:08 | GOES-16 | RIBEIRÃO BONITO | SÃO PAULO | Brasil | 3542909 | 35 | 33 | nan | nan | nan | Cerrado | 81.3 |
| ef43c410-7130-3952-8954-44db1d8a25d2 | -22.1578 | -48.1172 | 2024-10-09 02:57:08 | GOES-16 | RIBEIRÃO BONITO | SÃO PAULO | Brasil | 3542909 | 35 | 33 | nan | nan | nan | Cerrado | 145.7 |
| 3e9e3106-97f7-33e3-ad71-516d20e6947c | -22.1585 | -48.0936 | 2024-10-09 02:57:08 | GOES-16 | RIBEIRÃO BONITO | SÃO PAULO | Brasil | 3542909 | 35 | 33 | nan | nan | nan | Cerrado | 78.4 |
| cc03874b-738b-35bb-aa21-2e22ee0524b0 | -22.1772 | -48.1593 | 2024-10-09 02:57:08 | GOES-16 | BROTAS | SÃO PAULO | Brasil | 3507902 | 35 | 33 | nan | nan | nan | Cerrado | 90.8 |
| e43f1a58-5ce1-390a-b077-3ab5be0b317e | -22.1794 | -48.0884 | 2024-10-09 02:57:08 | GOES-16 | BROTAS | SÃO PAULO | Brasil | 3507902 | 35 | 33 | nan | nan | nan | Cerrado | 89.0 |
| a99795e7-61ed-30dd-81f0-c9424f7db2cd | -22.1981 | -48.1541 | 2024-10-09 02:57:08 | GOES-16 | BROTAS | SÃO PAULO | Brasil | 3507902 | 35 | 33 | nan | nan | nan | Cerrado | 123.5 |
| 065a789d-b43f-327c-b3eb-e37b4e81ac74 | -22.8348 | -54.4471 | 2024-10-09 02:57:12 | GOES-16 | JUTI | MATO GROSSO DO SUL | Brasil | 5005152 | 50 | 33 | nan | nan | nan | Mata Atlântica | 72.0 |
| 8d852df8-393b-3dde-9ef5-7ffa2e326280 | -23.3478 | -53.907 | 2024-10-09 02:57:15 | GOES-16 | ITAQUIRAÍ | MATO GROSSO DO SUL | Brasil | 5004601 | 50 | 33 | nan | nan | nan | Mata Atlântica | 96.4 |
| 1bc23b48-1cd4-381f-b7f1-e17672dac3d5 | -7.82204 | -35.18055 | 2024-10-09 02:58:00 | NPP-375D | TRACUNHAÉM | PERNAMBUCO | Brasil | 2615508 | 26 | 33 | nan | nan | nan | Mata Atlântica | 2.0 |
| 8e157a83-b389-3090-9ea8-6ad630239e2e | -7.82063 | -35.17863 | 2024-10-09 02:58:00 | NPP-375D | TRACUNHAÉM | PERNAMBUCO | Brasil | 2615508 | 26 | 33 | nan | nan | nan | Mata Atlântica | 2.0 |
| 798ca3be-2056-3dfd-a187-ee80da7e5994 | -7.8161 | -35.17928 | 2024-10-09 02:58:00 | NPP-375D | TRACUNHAÉM | PERNAMBUCO | Brasil | 2615508 | 26 | 33 | nan | nan | nan | Mata Atlântica | 2.0 |
| e82275d6-e6dd-3e8a-91a9-ac166afeed06 | -7.81389 | -35.18174 | 2024-10-09 02:58:00 | NPP-375D | TRACUNHAÉM | PERNAMBUCO | Brasil | 2615508 | 26 | 33 | nan | nan | nan | Mata Atlântica | 0.9 |
| a9b9e318-c20e-30a9-a1da-69ecba7cd526 | -8.03184 | -35.26131 | 2024-10-09 02:58:00 | NPP-375D | GLÓRIA DO GOITÁ | PERNAMBUCO | Brasil | 2606101 | 26 | 33 | nan | nan | nan | Mata Atlântica | 2.4 |
| d7e18662-8474-30d6-9543-ea15ad80d800 | -18.62854 | -41.12789 | 2024-10-09 03:00:00 | NPP-375D | MANTENA | MINAS GERAIS | Brasil | 3139607 | 31 | 33 | nan | nan | nan | Mata Atlântica | 1.5 |
| 8e1fff13-d640-3d3c-a96e-94d5c7f74c69 | -18.62667 | -41.13563 | 2024-10-09 03:00:00 | NPP-375D | MANTENA | MINAS GERAIS | Brasil | 3139607 | 31 | 33 | nan | nan | nan | Mata Atlântica | 1.5 |
| 59f7c629-d388-36a7-9364-fa2988e263ca | -18.44194 | -41.16054 | 2024-10-09 03:00:00 | NPP-375D | ÁGUA DOCE DO NORTE | ESPÍRITO SANTO | Brasil | 3200169 | 32 | 33 | nan | nan | nan | Mata Atlântica | 3.5 |
| 76c51292-ce87-337e-9db7-da85454c1960 | -20.3515 | -41.8451 | 2024-10-09 03:02:00 | NPP-375D | IÚNA | ESPÍRITO SANTO | Brasil | 3203007 | 32 | 33 | nan | nan | nan | Mata Atlântica | 3.1 |
| 571e056f-bfbd-325d-b7aa-d89e863bb52b | -20.34956 | -41.85279 | 2024-10-09 03:02:00 | NPP-375D | IÚNA | ESPÍRITO SANTO | Brasil | 3203007 | 32 | 33 | nan | nan | nan | Mata Atlântica | 3.1 |
| 6af4d082-9119-3438-9c6b-c476432a9834 | -20.34872 | -41.84127 | 2024-10-09 03:02:00 | NPP-375D | IÚNA | ESPÍRITO SANTO | Brasil | 3203007 | 32 | 33 | nan | nan | nan | Mata Atlântica | 2.9 |
| 697bb84c-5df9-3ad2-b166-482d60c0c506 | -20.34657 | -41.85001 | 2024-10-09 03:02:00 | NPP-375D | IÚNA | ESPÍRITO SANTO | Brasil | 3203007 | 32 | 33 | nan | nan | nan | Mata Atlântica | 6.2 |
| f5f06fca-0604-3063-9806-8ce7518cb4f2 | -20.68328 | -42.33202 | 2024-10-09 03:02:00 | NPP-375D | FERVEDOURO | MINAS GERAIS | Brasil | 3125952 | 31 | 33 | nan | nan | nan | Mata Atlântica | 3.2 |
| 73535d39-694c-3807-9545-5f1c694ce26d | -20.68194 | -42.33019 | 2024-10-09 03:02:00 | NPP-375D | FERVEDOURO | MINAS GERAIS | Brasil | 3125952 | 31 | 33 | nan | nan | nan | Mata Atlântica | 1.5 |
| 019ddf06-55e2-3519-9ce2-2584706fd390 | -20.67998 | -42.33807 | 2024-10-09 03:02:00 | NPP-375D | FERVEDOURO | MINAS GERAIS | Brasil | 3125952 | 31 | 33 | nan | nan | nan | Mata Atlântica | 2.3 |
| 002a67d2-fa0c-3e5f-b82c-261348672bec | -19.82906 | -42.07417 | 2024-10-09 03:02:00 | NPP-375D | CARATINGA | MINAS GERAIS | Brasil | 3113404 | 31 | 33 | nan | nan | nan | Mata Atlântica | 3.7 |
| 0fbc687c-8cc6-31e3-8566-994e7b5f8b2e | -19.77129 | -42.33694 | 2024-10-09 03:02:00 | NPP-375D | BOM JESUS DO GALHO | MINAS GERAIS | Brasil | 3107802 | 31 | 33 | nan | nan | nan | Mata Atlântica | 9.4 |
| 72922cb6-1e40-3b01-a98f-fcaaddf8b3e2 | -19.76957 | -42.34381 | 2024-10-09 03:02:00 | NPP-375D | BOM JESUS DO GALHO | MINAS GERAIS | Brasil | 3107802 | 31 | 33 | nan | nan | nan | Mata Atlântica | 9.4 |
| 31f18df1-3a79-3e9f-82c2-e5482aa3345d | -13.91 | -44.52 | 2024-10-09 03:04:05 | MSG-03 | CORIBE | BAHIA | Brasil | 2909109 | 29 | 33 | nan | nan | nan | Cerrado | nan |
| 6d8ccd3a-c70a-360f-ad16-a561e1cae370 | -13.94 | -44.53 | 2024-10-09 03:04:05 | MSG-03 | CORIBE | BAHIA | Brasil | 2909109 | 29 | 33 | nan | nan | nan | Cerrado | nan |
| 83a8ec02-ef20-3d5e-9d53-c9a094e20f66 | -1.11 | -53.6173 | 2024-10-09 03:05:12 | GOES-16 | ALMEIRIM | PARÁ | Brasil | 1500503 | 15 | 33 | nan | nan | nan | Amazônia | 72.3 |
| e7bdaeb4-2e34-3171-bfcb-4be4f9bb6554 | -1.1284 | -53.6171 | 2024-10-09 03:05:12 | GOES-16 | ALMEIRIM | PARÁ | Brasil | 1500503 | 15 | 33 | nan | nan | nan | Amazônia | 41.4 |
| 91e07deb-e4c2-3b38-a49a-7f5082f6c544 | -2.6094 | -49.7985 | 2024-10-09 03:05:21 | GOES-16 | OEIRAS DO PARÁ | PARÁ | Brasil | 1505205 | 15 | 33 | nan | nan | nan | Amazônia | 50.1 |
| 79f5b094-1660-37bf-9380-e06032a1e4a5 | -3.9021 | -46.4689 | 2024-10-09 03:05:28 | GOES-16 | BOM JARDIM | MARANHÃO | Brasil | 2102002 | 21 | 33 | nan | nan | nan | Amazônia | 52.3 |
| 383f5355-3bd3-3d53-9ae6-43a15f15fd1f | -3.9023 | -46.4467 | 2024-10-09 03:05:28 | GOES-16 | BOM JARDIM | MARANHÃO | Brasil | 2102002 | 21 | 33 | nan | nan | nan | Amazônia | 58.1 |
| d6d25022-32c5-3524-827f-13a3670cc26b | -3.9207 | -46.468 | 2024-10-09 03:05:28 | GOES-16 | BOM JARDIM | MARANHÃO | Brasil | 2102002 | 21 | 33 | nan | nan | nan | Amazônia | 47.1 |
| 99f61f4e-2999-366f-9cff-70717d9cbbf4 | -3.9208 | -46.4459 | 2024-10-09 03:05:28 | GOES-16 | BOM JARDIM | MARANHÃO | Brasil | 2102002 | 21 | 33 | nan | nan | nan | Amazônia | 73.1 |
| 1274cbd2-a16b-3bb7-896c-e69c6fbddf8b | -3.9393 | -46.4672 | 2024-10-09 03:05:28 | GOES-16 | BOM JARDIM | MARANHÃO | Brasil | 2102002 | 21 | 33 | nan | nan | nan | Amazônia | 48.3 |
| c8fc61d5-2fff-3405-b948-22c48ddeeff4 | -3.9394 | -46.445 | 2024-10-09 03:05:28 | GOES-16 | BOM JARDIM | MARANHÃO | Brasil | 2102002 | 21 | 33 | nan | nan | nan | Amazônia | 94.2 |
| 8f452190-b5f2-3e7c-a692-68c27a783cf6 | -5.5905 | -44.8687 | 2024-10-09 03:05:38 | GOES-16 | TUNTUM | MARANHÃO | Brasil | 2112308 | 21 | 33 | nan | nan | nan | Cerrado | 54.1 |
| 56c7cc1f-1c92-3a32-bd1d-e985761898c5 | -6.7614 | -60.0559 | 2024-10-09 03:05:45 | GOES-16 | NOVO ARIPUANÃ | AMAZONAS | Brasil | 1303304 | 13 | 33 | nan | nan | nan | Amazônia | 117.0 |
| 3b0d6116-48cd-3e90-93d9-37a331e4f10b | -6.7615 | -60.0367 | 2024-10-09 03:05:45 | GOES-16 | NOVO ARIPUANÃ | AMAZONAS | Brasil | 1303304 | 13 | 33 | nan | nan | nan | Amazônia | 45.8 |
| 5851eac4-28c0-32c9-a14f-53ac3d3a832d | -6.7798 | -60.0552 | 2024-10-09 03:05:45 | GOES-16 | NOVO ARIPUANÃ | AMAZONAS | Brasil | 1303304 | 13 | 33 | nan | nan | nan | Amazônia | 181.2 |
| 4a8dac59-944e-3182-b2be-a2c2a7faf2c2 | -6.7799 | -60.036 | 2024-10-09 03:05:45 | GOES-16 | NOVO ARIPUANÃ | AMAZONAS | Brasil | 1303304 | 13 | 33 | nan | nan | nan | Amazônia | 70.0 |
| 38533824-f8cb-3d74-b408-6e9c014bd436 | -8.4919 | -48.6476 | 2024-10-09 03:05:54 | GOES-16 | PRESIDENTE KENNEDY | TOCANTINS | Brasil | 1718402 | 17 | 33 | nan | nan | nan | Amazônia | 80.8 |
| 6b194bbf-2996-3543-9330-1dc10fc95727 | -9.5817 | -65.2497 | 2024-10-09 03:06:01 | GOES-16 | PORTO VELHO | RONDÔNIA | Brasil | 1100205 | 11 | 33 | nan | nan | nan | Amazônia | 60.7 |
| ed2d2fa8-f49e-30e6-8dcc-d97a22bb235a | -9.5818 | -65.231 | 2024-10-09 03:06:01 | GOES-16 | PORTO VELHO | RONDÔNIA | Brasil | 1100205 | 11 | 33 | nan | nan | nan | Amazônia | 32.8 |
| 1d276321-f76e-3fd7-a511-32dfe0861964 | -10.3655 | -64.8451 | 2024-10-09 03:06:06 | GOES-16 | NOVA MAMORÉ | RONDÔNIA | Brasil | 1100338 | 11 | 33 | nan | nan | nan | Amazônia | 35.6 |
| 2d0898e9-bee4-3f6d-8578-15f1c4bf1094 | -10.3656 | -64.8262 | 2024-10-09 03:06:06 | GOES-16 | NOVA MAMORÉ | RONDÔNIA | Brasil | 1100338 | 11 | 33 | nan | nan | nan | Amazônia | 43.4 |
| a6cf5ba6-3047-3ed3-95fe-e19ea6a95e6a | -10.3894 | -61.2502 | 2024-10-09 03:06:06 | GOES-16 | RONDOLÂNDIA | MATO GROSSO | Brasil | 5107578 | 51 | 33 | nan | nan | nan | Amazônia | 51.1 |
| 39924b26-8741-3a0c-8ca6-096c68c692cf | -10.3842 | -64.8443 | 2024-10-09 03:06:06 | GOES-16 | NOVA MAMORÉ | RONDÔNIA | Brasil | 1100338 | 11 | 33 | nan | nan | nan | Amazônia | 40.8 |
| 352758b0-2c9d-3f01-9bbd-40835a09e738 | -10.3843 | -64.8255 | 2024-10-09 03:06:06 | GOES-16 | NOVA MAMORÉ | RONDÔNIA | Brasil | 1100338 | 11 | 33 | nan | nan | nan | Amazônia | 54.9 |
| e79b46d6-868d-3037-96b2-19b803daed03 | -10.6253 | -55.9355 | 2024-10-09 03:06:07 | GOES-16 | NOVA CANAÃ DO NORTE | MATO GROSSO | Brasil | 5106216 | 51 | 33 | nan | nan | nan | Amazônia | 43.2 |
| 8215e82a-d592-3ef6-8ae4-f83af056ee87 | -10.6256 | -55.9154 | 2024-10-09 03:06:07 | GOES-16 | NOVA CANAÃ DO NORTE | MATO GROSSO | Brasil | 5106216 | 51 | 33 | nan | nan | nan | Amazônia | 91.0 |
| b64cbd28-dcdb-3fe4-a632-3d458e836acf | -10.6258 | -55.8953 | 2024-10-09 03:06:07 | GOES-16 | NOVA CANAÃ DO NORTE | MATO GROSSO | Brasil | 5106216 | 51 | 33 | nan | nan | nan | Amazônia | 65.0 |
| bea55e6c-a6cf-3756-9803-8ff80b678dcd | -10.8754 | -63.9169 | 2024-10-09 03:06:08 | GOES-16 | GUAJARÁ-MIRIM | RONDÔNIA | Brasil | 1100106 | 11 | 33 | nan | nan | nan | Amazônia | 88.4 |
| 04bff1dc-9141-312c-861d-a2a418be7081 | -10.8755 | -63.8979 | 2024-10-09 03:06:08 | GOES-16 | GUAJARÁ-MIRIM | RONDÔNIA | Brasil | 1100106 | 11 | 33 | nan | nan | nan | Amazônia | 70.5 |
| 5cfeff61-9bbe-3fb3-b0f7-b57ae6f6c707 | -10.8941 | -63.916 | 2024-10-09 03:06:09 | GOES-16 | GUAJARÁ-MIRIM | RONDÔNIA | Brasil | 1100106 | 11 | 33 | nan | nan | nan | Amazônia | 54.0 |
| 41e421fd-643b-33dd-b326-3cf86636637c | -11.3467 | -51.021 | 2024-10-09 03:06:10 | GOES-16 | SÃO FÉLIX DO ARAGUAIA | MATO GROSSO | Brasil | 5107859 | 51 | 33 | nan | nan | nan | Cerrado | 62.1 |
| 2fb60136-25c2-3614-a299-70664efae6c5 | -11.2583 | -60.3885 | 2024-10-09 03:06:10 | GOES-16 | VILHENA | RONDÔNIA | Brasil | 1100304 | 11 | 33 | nan | nan | nan | Amazônia | 53.2 |
| ca9eeee9-99e0-317d-a056-c16d5b68a83f | -11.2585 | -60.3691 | 2024-10-09 03:06:10 | GOES-16 | VILHENA | RONDÔNIA | Brasil | 1100304 | 11 | 33 | nan | nan | nan | Amazônia | 46.1 |
| c902f313-db82-350a-aebb-9e3036f0be00 | -11.3657 | -51.0189 | 2024-10-09 03:06:10 | GOES-16 | SÃO FÉLIX DO ARAGUAIA | MATO GROSSO | Brasil | 5107859 | 51 | 33 | nan | nan | nan | Cerrado | 61.6 |
| f4e14074-a6ae-3a93-b0ab-770797af02d4 | -11.366 | -50.9977 | 2024-10-09 03:06:10 | GOES-16 | SÃO FÉLIX DO ARAGUAIA | MATO GROSSO | Brasil | 5107859 | 51 | 33 | nan | nan | nan | Cerrado | 63.6 |
| c2ac30c9-f944-3e15-85e2-bdd304aa87e1 | -11.2771 | -60.3873 | 2024-10-09 03:06:11 | GOES-16 | VILHENA | RONDÔNIA | Brasil | 1100304 | 11 | 33 | nan | nan | nan | Amazônia | 56.3 |
| 5054fdb8-01d5-35cc-84dd-a4efa73e8fa8 | -11.5232 | -65.1559 | 2024-10-09 03:06:12 | GOES-16 | GUAJARÁ-MIRIM | RONDÔNIA | Brasil | 1100106 | 11 | 33 | nan | nan | nan | Amazônia | 53.7 |
| 19191bc0-7c25-3ef5-8418-ce7c540a178e | -11.5233 | -65.137 | 2024-10-09 03:06:12 | GOES-16 | GUAJARÁ-MIRIM | RONDÔNIA | Brasil | 1100106 | 11 | 33 | nan | nan | nan | Amazônia | 56.0 |
| 73df9a9c-29e3-3938-a956-1f4d5014c661 | -11.6806 | -64.0312 | 2024-10-09 03:06:13 | GOES-16 | GUAJARÁ-MIRIM | RONDÔNIA | Brasil | 1100106 | 11 | 33 | nan | nan | nan | Amazônia | 54.3 |
| 3b476002-0c8c-3240-af32-48e2076acc54 | -11.693 | -65.0163 | 2024-10-09 03:06:13 | GOES-16 | GUAJARÁ-MIRIM | RONDÔNIA | Brasil | 1100106 | 11 | 33 | nan | nan | nan | Amazônia | 119.8 |
| 8b221b4c-92e3-30c9-9632-5da54aa342ec | -11.6931 | -64.9974 | 2024-10-09 03:06:13 | GOES-16 | GUAJARÁ-MIRIM | RONDÔNIA | Brasil | 1100106 | 11 | 33 | nan | nan | nan | Amazônia | 90.6 |
| 9200478c-eb80-3508-9670-5d4d8a76e2b4 | -11.7117 | -65.0155 | 2024-10-09 03:06:13 | GOES-16 | GUAJARÁ-MIRIM | RONDÔNIA | Brasil | 1100106 | 11 | 33 | nan | nan | nan | Amazônia | 113.1 |
| 3e0d6ead-6448-3b54-815e-773fa3afe169 | -11.7119 | -64.9966 | 2024-10-09 03:06:13 | GOES-16 | GUAJARÁ-MIRIM | RONDÔNIA | Brasil | 1100106 | 11 | 33 | nan | nan | nan | Amazônia | 94.8 |
| 9b67fa36-d9e2-39b2-a766-8e8af0cbb754 | -12.6676 | -63.0819 | 2024-10-09 03:06:18 | GOES-16 | SÃO FRANCISCO DO GUAPORÉ | RONDÔNIA | Brasil | 1101492 | 11 | 33 | nan | nan | nan | Amazônia | 55.3 |
| 74052984-770a-31f3-9257-1f8de8f8604f | -12.7501 | -62.269 | 2024-10-09 03:06:19 | GOES-16 | ALTA FLORESTA D'OESTE | RONDÔNIA | Brasil | 1100015 | 11 | 33 | nan | nan | nan | Amazônia | 65.1 |
| 886c99b3-8c59-3f5a-aaac-92e1e1e52b4e | -12.878 | -62.8007 | 2024-10-09 03:06:20 | GOES-16 | ALTA FLORESTA D'OESTE | RONDÔNIA | Brasil | 1100015 | 11 | 33 | nan | nan | nan | Amazônia | 83.4 |
| 934abaaf-c20e-342a-a308-c53e06090e92 | -12.9756 | -62.4673 | 2024-10-09 03:06:20 | GOES-16 | ALTA FLORESTA D'OESTE | RONDÔNIA | Brasil | 1100015 | 11 | 33 | nan | nan | nan | Amazônia | 61.3 |
| 435d8d19-0f44-386f-8942-01109286bc8e | -13.8364 | -44.5927 | 2024-10-09 03:06:23 | GOES-16 | CORIBE | BAHIA | Brasil | 2909109 | 29 | 33 | nan | nan | nan | Cerrado | 70.3 |
| 7ece54b0-9654-3c85-ad45-f1fbdfa73c3b | -13.8369 | -44.5691 | 2024-10-09 03:06:23 | GOES-16 | CORIBE | BAHIA | Brasil | 2909109 | 29 | 33 | nan | nan | nan | Cerrado | 173.3 |
| 25f1a5ff-0ab1-3b6a-8477-def2f686869f | -13.8564 | -44.5657 | 2024-10-09 03:06:24 | GOES-16 | CORIBE | BAHIA | Brasil | 2909109 | 29 | 33 | nan | nan | nan | Cerrado | 136.6 |
| 3d6958bb-8314-3fb3-ab66-3424f0c8b572 | -13.8569 | -44.5421 | 2024-10-09 03:06:24 | GOES-16 | CORIBE | BAHIA | Brasil | 2909109 | 29 | 33 | nan | nan | nan | Cerrado | 71.1 |
| 22dd80cb-75c9-32e0-b073-f547fc8f11cb | -13.8764 | -44.5386 | 2024-10-09 03:06:24 | GOES-16 | CORIBE | BAHIA | Brasil | 2909109 | 29 | 33 | nan | nan | nan | Cerrado | 74.3 |
| 4ef657fd-5ebf-304a-87cb-ab5e6e341125 | -13.8963 | -44.5116 | 2024-10-09 03:06:24 | GOES-16 | CORIBE | BAHIA | Brasil | 2909109 | 29 | 33 | nan | nan | nan | Cerrado | 102.8 |
| 363c7669-6787-3935-be3f-44491c17d355 | -13.9153 | -44.5317 | 2024-10-09 03:06:24 | GOES-16 | CORIBE | BAHIA | Brasil | 2909109 | 29 | 33 | nan | nan | nan | Cerrado | 86.4 |
| e0af3dbf-360e-3619-9a3c-d079c998d001 | -13.9158 | -44.5081 | 2024-10-09 03:06:24 | GOES-16 | CORIBE | BAHIA | Brasil | 2909109 | 29 | 33 | nan | nan | nan | Cerrado | 190.1 |
| 843fcdae-621a-39d4-a51f-df997be24ee6 | -13.9163 | -44.4845 | 2024-10-09 03:06:24 | GOES-16 | CORIBE | BAHIA | Brasil | 2909109 | 29 | 33 | nan | nan | nan | Cerrado | 79.4 |
| 361091f0-a6bc-31db-a7a4-5d382746484a | -13.9348 | -44.5282 | 2024-10-09 03:06:24 | GOES-16 | CORIBE | BAHIA | Brasil | 2909109 | 29 | 33 | nan | nan | nan | Cerrado | 216.9 |
| 95f60254-7daa-3f7c-8a83-f87e4c1a929c | -13.9353 | -44.5046 | 2024-10-09 03:06:24 | GOES-16 | CORIBE | BAHIA | Brasil | 2909109 | 29 | 33 | nan | nan | nan | Cerrado | 159.7 |
| 1f8e91d1-ad16-37cf-a2ce-a76f95f9dffa | -14.0971 | -51.1134 | 2024-10-09 03:06:26 | GOES-16 | COCALINHO | MATO GROSSO | Brasil | 5103106 | 51 | 33 | nan | nan | nan | Cerrado | 108.3 |
| 22e3c7ab-eb1b-3099-809f-6e772bef6b3c | -14.0975 | -51.0918 | 2024-10-09 03:06:26 | GOES-16 | COCALINHO | MATO GROSSO | Brasil | 5103106 | 51 | 33 | nan | nan | nan | Cerrado | 189.5 |
| a767b69c-c5e5-32f8-af66-61a3383eaf24 | -14.1168 | -51.0892 | 2024-10-09 03:06:26 | GOES-16 | COCALINHO | MATO GROSSO | Brasil | 5103106 | 51 | 33 | nan | nan | nan | Cerrado | 106.7 |
| ce547b4f-72b6-3188-8d38-8a38fd981302 | -16.4184 | -55.9455 | 2024-10-09 03:06:39 | GOES-16 | BARÃO DE MELGAÇO | MATO GROSSO | Brasil | 5101605 | 51 | 33 | nan | nan | nan | Pantanal | 76.5 |
| 3350d770-fa22-3b56-8634-69f6de2d75fe | -17.0623 | -56.0308 | 2024-10-09 03:06:42 | GOES-16 | BARÃO DE MELGAÇO | MATO GROSSO | Brasil | 5101605 | 51 | 33 | nan | nan | nan | Pantanal | 84.6 |
| 008ca197-13c3-316f-8476-5910c78e1934 | -17.1185 | -57.3834 | 2024-10-09 03:06:43 | GOES-16 | CÁCERES | MATO GROSSO | Brasil | 5102504 | 51 | 33 | nan | nan | nan | Pantanal | 47.5 |
| 44745c4c-0cdc-3d68-bc4b-f51d8cce34df | -17.1188 | -57.3628 | 2024-10-09 03:06:43 | GOES-16 | POCONÉ | MATO GROSSO | Brasil | 5106505 | 51 | 33 | nan | nan | nan | Pantanal | 58.5 |
| 67606090-82c7-3c1e-b630-203b0eace1bc | -17.1588 | -56.1222 | 2024-10-09 03:06:43 | GOES-16 | BARÃO DE MELGAÇO | MATO GROSSO | Brasil | 5101605 | 51 | 33 | nan | nan | nan | Pantanal | 75.8 |
| 2a4c6ef7-dfb1-3a21-a61b-febb214ecede | -18.1193 | -56.3921 | 2024-10-09 03:06:48 | GOES-16 | CORUMBÁ | MATO GROSSO DO SUL | Brasil | 5003207 | 50 | 33 | nan | nan | nan | Pantanal | 188.3 |
| c2ab0190-2a97-3e30-9f5f-918284c68f9a | -18.1196 | -56.3713 | 2024-10-09 03:06:48 | GOES-16 | CORUMBÁ | MATO GROSSO DO SUL | Brasil | 5003207 | 50 | 33 | nan | nan | nan | Pantanal | 79.6 |
| 69043d76-3eb9-3d80-94ce-35f618beb0cf | -18.1391 | -56.3895 | 2024-10-09 03:06:48 | GOES-16 | CORUMBÁ | MATO GROSSO DO SUL | Brasil | 5003207 | 50 | 33 | nan | nan | nan | Pantanal | 98.1 |
| a0f8371c-650a-3a4c-a949-9dd06aefb08a | -18.5794 | -57.2655 | 2024-10-09 03:06:50 | GOES-16 | CORUMBÁ | MATO GROSSO DO SUL | Brasil | 5003207 | 50 | 33 | nan | nan | nan | Pantanal | 47.7 |
| be26e54c-6743-3f2e-8204-133590568001 | -18.5993 | -57.2629 | 2024-10-09 03:06:50 | GOES-16 | CORUMBÁ | MATO GROSSO DO SUL | Brasil | 5003207 | 50 | 33 | nan | nan | nan | Pantanal | 73.2 |
| d16cc144-a657-3e12-ab56-06bcec43197b | -18.5996 | -57.2422 | 2024-10-09 03:06:50 | GOES-16 | CORUMBÁ | MATO GROSSO DO SUL | Brasil | 5003207 | 50 | 33 | nan | nan | nan | Pantanal | 78.7 |
| d3e5838f-044e-3a85-ba0d-8bfd8a80b16c | -18.6398 | -57.2163 | 2024-10-09 03:06:51 | GOES-16 | CORUMBÁ | MATO GROSSO DO SUL | Brasil | 5003207 | 50 | 33 | nan | nan | nan | Pantanal | 56.4 |
| 0cf39c30-48bd-3022-b756-44075af36e82 | -18.6597 | -57.2137 | 2024-10-09 03:06:51 | GOES-16 | CORUMBÁ | MATO GROSSO DO SUL | Brasil | 5003207 | 50 | 33 | nan | nan | nan | Pantanal | 48.1 |


[Clique aqui para ver as próximas entradas](README57.md)
