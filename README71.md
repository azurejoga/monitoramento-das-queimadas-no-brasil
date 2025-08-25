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

## Dados Diários - Página 71

| ID | Latitude | Longitude | Data/Hora GMT | Satélite | Município | Estado | País | Município ID | Estado ID | País ID | Dias sem Chuva | Precipitação | Risco de Fogo | Bioma | FRP |
|----|----------|-----------|---------------|----------|-----------|--------|------|--------------|-----------|---------|----------------|--------------|----------------|-------|-----|
| c1044af3-48c7-3073-9513-ad9b09c31753 | -8.88256 | -62.46069 | 2025-08-25 05:04:00 | NOAA-20 | CUJUBIM | RONDÔNIA | Brasil | 1100940 | 11 | 33 | nan | nan | nan | Amazônia | 4.6 |
| bdd18a9d-7b26-3ce5-8eb3-5b23ce27808c | -9.12629 | -60.73424 | 2025-08-25 05:04:00 | NOAA-20 | COLNIZA | MATO GROSSO | Brasil | 5103254 | 51 | 33 | nan | nan | nan | Amazônia | 5.4 |
| 1a7c9ccf-f601-3567-abbf-f8cad20b4cdd | -5.75231 | -57.57722 | 2025-08-25 05:04:00 | NOAA-20 | JACAREACANGA | PARÁ | Brasil | 1503754 | 15 | 33 | nan | nan | nan | Amazônia | 2.3 |
| 675d1484-9dcd-3800-b959-4cadbde3004b | -9.1663 | -59.45568 | 2025-08-25 05:04:00 | NOAA-20 | COLNIZA | MATO GROSSO | Brasil | 5103254 | 51 | 33 | nan | nan | nan | Amazônia | 8.3 |
| fe380cf9-981d-32aa-8b70-32ff16852bb8 | -8.58557 | -62.60479 | 2025-08-25 05:04:00 | NOAA-20 | PORTO VELHO | RONDÔNIA | Brasil | 1100205 | 11 | 33 | nan | nan | nan | Amazônia | 2.1 |
| 18d4ea9e-3ace-34ce-840a-cafe731040c9 | -12.95294 | -46.33152 | 2025-08-25 05:04:00 | NOAA-20 | LAVANDEIRA | TOCANTINS | Brasil | 1712157 | 17 | 33 | nan | nan | nan | Cerrado | 1.0 |
| 7cb946a8-f742-3e37-893c-47336ad84490 | -4.96446 | -55.81412 | 2025-08-25 05:04:00 | NOAA-20 | TRAIRÃO | PARÁ | Brasil | 1508050 | 15 | 33 | nan | nan | nan | Amazônia | 1.3 |
| 6ea3e441-85f5-373d-bd14-e9caefbf03d1 | -7.55274 | -63.86038 | 2025-08-25 05:04:00 | NOAA-20 | CANUTAMA | AMAZONAS | Brasil | 1300904 | 13 | 33 | nan | nan | nan | Amazônia | 1.8 |
| 0c0ab786-e49f-3471-86e1-2df46bea7925 | -8.49598 | -63.8702 | 2025-08-25 05:04:00 | NOAA-20 | PORTO VELHO | RONDÔNIA | Brasil | 1100205 | 11 | 33 | nan | nan | nan | Amazônia | 1.3 |
| 650f113a-0a9d-35e5-b427-8050934131fd | -8.985 | -65.42786 | 2025-08-25 05:04:00 | NOAA-20 | LÁBREA | AMAZONAS | Brasil | 1302405 | 13 | 33 | nan | nan | nan | Amazônia | 4.5 |
| 006317bc-905e-3425-96fb-e0d7159d7861 | -9.57384 | -55.36511 | 2025-08-25 05:04:00 | NOAA-20 | NOVO MUNDO | MATO GROSSO | Brasil | 5106265 | 51 | 33 | nan | nan | nan | Amazônia | 2.3 |
| 9f77f940-e42d-35e0-9968-a62379347aa4 | -6.91287 | -62.99992 | 2025-08-25 05:04:00 | NOAA-20 | HUMAITÁ | AMAZONAS | Brasil | 1301704 | 13 | 33 | nan | nan | nan | Amazônia | 1.7 |
| 9d482678-34f1-30b1-b514-760ba3505159 | -6.76668 | -59.6614 | 2025-08-25 05:04:00 | NOAA-20 | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 4.9 |
| 6c993796-cf82-36a3-9060-41c5c60f51f1 | -9.22834 | -59.71244 | 2025-08-25 05:04:00 | NOAA-20 | COLNIZA | MATO GROSSO | Brasil | 5103254 | 51 | 33 | nan | nan | nan | Amazônia | 1.0 |
| 5a1a30c0-ba1a-3cd7-9966-60474ffff571 | -12.74 | -48.14009 | 2025-08-25 05:04:00 | NOAA-20 | PARANÃ | TOCANTINS | Brasil | 1716208 | 17 | 33 | nan | nan | nan | Cerrado | 1.8 |
| cef6c52e-e541-3fc5-84d4-9d4765e38314 | -10.88634 | -55.79276 | 2025-08-25 05:04:00 | NOAA-20 | NOVA CANAÃ DO NORTE | MATO GROSSO | Brasil | 5106216 | 51 | 33 | nan | nan | nan | Amazônia | 2.2 |
| 109d401c-51b3-3619-8c8e-a795ed3afaf1 | -9.24137 | -60.48616 | 2025-08-25 05:04:00 | NOAA-20 | COLNIZA | MATO GROSSO | Brasil | 5103254 | 51 | 33 | nan | nan | nan | Amazônia | 1.3 |
| 6394e92b-ffd9-3d69-9308-723de8ff2eb5 | -8.22386 | -61.39002 | 2025-08-25 05:04:00 | NOAA-20 | NOVO ARIPUANÃ | AMAZONAS | Brasil | 1303304 | 13 | 33 | nan | nan | nan | Amazônia | 2.6 |
| 31cb57c7-8fb1-3964-998c-b6ff919ea436 | -11.62492 | -46.24094 | 2025-08-25 05:04:00 | NOAA-20 | NOVO JARDIM | TOCANTINS | Brasil | 1715259 | 17 | 33 | nan | nan | nan | Cerrado | 1.7 |
| 02452bb5-d4c7-367a-a0d3-40adb211ee17 | -6.82671 | -58.94629 | 2025-08-25 05:04:00 | NOAA-20 | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 3.4 |
| 786b2644-87ae-3531-82b6-acaaa7d4f8aa | -5.43556 | -60.17216 | 2025-08-25 05:04:00 | NOAA-20 | NOVO ARIPUANÃ | AMAZONAS | Brasil | 1303304 | 13 | 33 | nan | nan | nan | Amazônia | 9.0 |
| 05af5f45-9544-39e9-8f1d-5820b1760448 | -7.55368 | -63.85503 | 2025-08-25 05:04:00 | NOAA-20 | CANUTAMA | AMAZONAS | Brasil | 1300904 | 13 | 33 | nan | nan | nan | Amazônia | 2.8 |
| 04c85785-6b06-3ed7-ae3b-21af85d54c29 | -8.88969 | -62.44513 | 2025-08-25 05:04:00 | NOAA-20 | CUJUBIM | RONDÔNIA | Brasil | 1100940 | 11 | 33 | nan | nan | nan | Amazônia | 3.4 |
| 5caf70e1-1328-3b3c-b021-5837e30f935d | -8.89613 | -62.4589 | 2025-08-25 05:04:00 | NOAA-20 | CUJUBIM | RONDÔNIA | Brasil | 1100940 | 11 | 33 | nan | nan | nan | Amazônia | 2.6 |
| ec90f05c-894d-3065-a711-13a844b366fb | -6.14135 | -51.75312 | 2025-08-25 05:04:00 | NOAA-20 | SÃO FÉLIX DO XINGU | PARÁ | Brasil | 1507300 | 15 | 33 | nan | nan | nan | Amazônia | 0.8 |
| f1af3318-310d-354b-b071-79eb4652f862 | -7.56373 | -57.67292 | 2025-08-25 05:04:00 | NOAA-20 | JACAREACANGA | PARÁ | Brasil | 1503754 | 15 | 33 | nan | nan | nan | Amazônia | 1.6 |
| d25d2093-3a23-3945-a7e2-eaa48073ddef | -8.58559 | -62.63099 | 2025-08-25 05:04:00 | NOAA-20 | PORTO VELHO | RONDÔNIA | Brasil | 1100205 | 11 | 33 | nan | nan | nan | Amazônia | 1.1 |
| 7d61c4b1-3602-3346-bec3-f7a239dc8250 | -8.88326 | -62.43138 | 2025-08-25 05:04:00 | NOAA-20 | CUJUBIM | RONDÔNIA | Brasil | 1100940 | 11 | 33 | nan | nan | nan | Amazônia | 2.9 |
| c8ee57e1-7c0e-3f2f-a5bc-7e4fa492275f | -9.49533 | -58.93475 | 2025-08-25 05:04:00 | NOAA-20 | COTRIGUAÇU | MATO GROSSO | Brasil | 5103379 | 51 | 33 | nan | nan | nan | Amazônia | 1.8 |
| bb5d4bc3-e381-31fb-80e2-6845b68dbc3f | -10.41147 | -64.39192 | 2025-08-25 05:04:00 | NOAA-20 | NOVA MAMORÉ | RONDÔNIA | Brasil | 1100338 | 11 | 33 | nan | nan | nan | Amazônia | 12.3 |
| a1ab2e42-a11b-3c83-be5c-0ee1de3f2a7b | -6.79583 | -58.64252 | 2025-08-25 05:04:00 | NOAA-20 | MAUÉS | AMAZONAS | Brasil | 1302900 | 13 | 33 | nan | nan | nan | Amazônia | 1.0 |
| 5b46dcac-f53b-3c19-9387-0566145ffda6 | -8.51278 | -60.57568 | 2025-08-25 05:04:00 | NOAA-20 | NOVO ARIPUANÃ | AMAZONAS | Brasil | 1303304 | 13 | 33 | nan | nan | nan | Amazônia | 1.0 |
| a7110e4b-6970-368a-b7e4-5c7ada4c3543 | -8.89253 | -62.42884 | 2025-08-25 05:04:00 | NOAA-20 | CUJUBIM | RONDÔNIA | Brasil | 1100940 | 11 | 33 | nan | nan | nan | Amazônia | 1.5 |
| 88cf5f4f-3f6f-3ce7-83cf-804493478055 | -11.55272 | -50.52425 | 2025-08-25 05:04:00 | NOAA-20 | LAGOA DA CONFUSÃO | TOCANTINS | Brasil | 1711902 | 17 | 33 | nan | nan | nan | Cerrado | 1.9 |
| c86dc152-ad45-35cb-9227-74bbaf7d6189 | -6.50074 | -44.79404 | 2025-08-25 05:04:00 | NOAA-20 | MIRADOR | MARANHÃO | Brasil | 2106706 | 21 | 33 | nan | nan | nan | Cerrado | 1.6 |
| 2af80954-f94a-3dda-8e31-5b3ed1d803a1 | -6.83001 | -58.962 | 2025-08-25 05:04:00 | NOAA-20 | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 4.5 |
| 4fd3bf97-9018-306e-a079-08e3822a2cbf | -7.35635 | -57.63175 | 2025-08-25 05:04:00 | NOAA-20 | JACAREACANGA | PARÁ | Brasil | 1503754 | 15 | 33 | nan | nan | nan | Amazônia | 1.9 |
| 2172f01c-5802-3c6a-bdcf-586ec3980032 | -6.77186 | -59.65316 | 2025-08-25 05:04:00 | NOAA-20 | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 3.6 |
| 67d48e29-5b5d-397f-bfa0-6fd844ecef47 | -6.82605 | -58.95037 | 2025-08-25 05:04:00 | NOAA-20 | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 5.9 |
| 797aebdc-94bb-3845-90b4-edd10a73a75b | -6.1645 | -43.00765 | 2025-08-25 05:04:00 | NOAA-20 | SÃO FRANCISCO DO MARANHÃO | MARANHÃO | Brasil | 2110906 | 21 | 33 | nan | nan | nan | Cerrado | 1.3 |
| 9a226ec7-d002-3723-b986-35e070b535f0 | -6.83205 | -58.94973 | 2025-08-25 05:04:00 | NOAA-20 | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 5.6 |
| f32477d5-ae3e-3dad-a7ae-07bc2d888b5c | -8.49981 | -63.87617 | 2025-08-25 05:04:00 | NOAA-20 | PORTO VELHO | RONDÔNIA | Brasil | 1100205 | 11 | 33 | nan | nan | nan | Amazônia | 12.1 |
| 582cb431-66f6-3db0-85a7-e1fc5156ba48 | -9.00718 | -65.3954 | 2025-08-25 05:04:00 | NOAA-20 | LÁBREA | AMAZONAS | Brasil | 1302405 | 13 | 33 | nan | nan | nan | Amazônia | 3.7 |
| 00c59c0b-bcc9-31ec-8937-407bb54482c5 | -9.18223 | -60.79045 | 2025-08-25 05:04:00 | NOAA-20 | COLNIZA | MATO GROSSO | Brasil | 5103254 | 51 | 33 | nan | nan | nan | Amazônia | 19.9 |
| 2c9660f6-4837-39bd-b3af-978c6f276f9a | -9.19947 | -59.49931 | 2025-08-25 05:04:00 | NOAA-20 | COLNIZA | MATO GROSSO | Brasil | 5103254 | 51 | 33 | nan | nan | nan | Amazônia | 1.7 |
| 5b919e07-8798-3d61-b56d-a494e8a35d1e | -7.81585 | -46.8882 | 2025-08-25 05:04:00 | NOAA-20 | CAROLINA | MARANHÃO | Brasil | 2102804 | 21 | 33 | nan | nan | nan | Cerrado | 1.0 |
| 684193b4-3b79-3194-b149-b9f32748c21e | -9.15573 | -59.47499 | 2025-08-25 05:04:00 | NOAA-20 | COLNIZA | MATO GROSSO | Brasil | 5103254 | 51 | 33 | nan | nan | nan | Amazônia | 1.3 |
| 97cd71af-aa86-3a98-bcdf-144479c47d17 | -5.43477 | -60.17712 | 2025-08-25 05:04:00 | NOAA-20 | NOVO ARIPUANÃ | AMAZONAS | Brasil | 1303304 | 13 | 33 | nan | nan | nan | Amazônia | 13.4 |
| 2e9ff63f-f6e6-3802-8d04-6748907de423 | -8.91494 | -60.72267 | 2025-08-25 05:04:00 | NOAA-20 | COLNIZA | MATO GROSSO | Brasil | 5103254 | 51 | 33 | nan | nan | nan | Amazônia | 2.5 |
| d00c2f09-74c5-314e-94c4-61d8169ccb49 | -7.90197 | -45.88777 | 2025-08-25 05:04:00 | NOAA-20 | BALSAS | MARANHÃO | Brasil | 2101400 | 21 | 33 | nan | nan | nan | Cerrado | 0.7 |
| 7864bffb-abcb-3593-ab44-a8a694f529ae | -9.8072 | -61.2098 | 2025-08-25 05:04:00 | NOAA-20 | COLNIZA | MATO GROSSO | Brasil | 5103254 | 51 | 33 | nan | nan | nan | Amazônia | 1.9 |
| c74d8bf3-1504-391b-a23e-4324baf1719e | -9.16938 | -59.59212 | 2025-08-25 05:04:00 | NOAA-20 | COLNIZA | MATO GROSSO | Brasil | 5103254 | 51 | 33 | nan | nan | nan | Amazônia | 1.8 |
| f009e9ff-0bb5-3f04-9870-c4532612d047 | -8.32156 | -47.2593 | 2025-08-25 05:04:00 | NOAA-20 | GOIATINS | TOCANTINS | Brasil | 1709005 | 17 | 33 | nan | nan | nan | Cerrado | 0.9 |
| 3d8e319c-b944-3d68-881f-aff3c0a8eb8c | -9.2175 | -59.71064 | 2025-08-25 05:04:00 | NOAA-20 | COLNIZA | MATO GROSSO | Brasil | 5103254 | 51 | 33 | nan | nan | nan | Amazônia | 0.8 |
| 3bf32920-abaf-3765-8a60-ddcc02c6fea3 | -11.19495 | -48.47109 | 2025-08-25 05:04:00 | NOAA-20 | IPUEIRAS | TOCANTINS | Brasil | 1709807 | 17 | 33 | nan | nan | nan | Cerrado | 1.5 |
| 1e84c37e-d261-33ce-8365-96cb32541bc5 | -8.22993 | -61.42804 | 2025-08-25 05:04:00 | NOAA-20 | NOVO ARIPUANÃ | AMAZONAS | Brasil | 1303304 | 13 | 33 | nan | nan | nan | Amazônia | 1.0 |
| 00d578c8-955a-3bbe-ade9-8de3cf721a33 | -9.16136 | -59.46327 | 2025-08-25 05:04:00 | NOAA-20 | COLNIZA | MATO GROSSO | Brasil | 5103254 | 51 | 33 | nan | nan | nan | Amazônia | 1.8 |
| 5cc7026d-3e7b-31dc-b7af-05bb87eabdd8 | -8.11829 | -62.87226 | 2025-08-25 05:04:00 | NOAA-20 | PORTO VELHO | RONDÔNIA | Brasil | 1100205 | 11 | 33 | nan | nan | nan | Amazônia | 1.7 |
| 48b6dc83-0600-397b-8a2c-7d951ef6391c | -12.29627 | -49.14779 | 2025-08-25 05:04:00 | NOAA-20 | ALVORADA | TOCANTINS | Brasil | 1700707 | 17 | 33 | nan | nan | nan | Cerrado | 2.7 |
| 172176b1-ea27-3046-89f7-c1c8deb75339 | -8.21638 | -61.3851 | 2025-08-25 05:04:00 | NOAA-20 | NOVO ARIPUANÃ | AMAZONAS | Brasil | 1303304 | 13 | 33 | nan | nan | nan | Amazônia | 12.1 |
| 66dea24b-2a1a-34f8-af81-8ec3ba1ae6be | -6.81995 | -58.95617 | 2025-08-25 05:04:00 | NOAA-20 | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 3.8 |
| 97fc0740-c280-3dae-a3e9-be3d685ff8e1 | -9.6454 | -59.64444 | 2025-08-25 05:04:00 | NOAA-20 | COLNIZA | MATO GROSSO | Brasil | 5103254 | 51 | 33 | nan | nan | nan | Amazônia | 3.1 |
| 7f44d2e3-5837-3675-a98c-b479a5f670ae | -6.43963 | -44.55552 | 2025-08-25 05:04:00 | NOAA-20 | MIRADOR | MARANHÃO | Brasil | 2106706 | 21 | 33 | nan | nan | nan | Cerrado | 1.7 |
| f29c917c-0996-32ea-948b-361bb8307e44 | -10.72846 | -47.11607 | 2025-08-25 05:04:00 | NOAA-20 | PONTE ALTA DO TOCANTINS | TOCANTINS | Brasil | 1717909 | 17 | 33 | nan | nan | nan | Cerrado | 10.8 |
| 7bf33a23-24ff-341f-9ae7-fe464e6f86ae | -12.7529 | -48.12245 | 2025-08-25 05:04:00 | NOAA-20 | PARANÃ | TOCANTINS | Brasil | 1716208 | 17 | 33 | nan | nan | nan | Cerrado | 5.0 |
| 34f1e136-a469-3566-b3a7-34ad0c9a56ab | -13.0545 | -46.31923 | 2025-08-25 05:04:00 | NOAA-20 | CAMPOS BELOS | GOIÁS | Brasil | 5204904 | 52 | 33 | nan | nan | nan | Cerrado | 1.1 |
| d98d7e19-6e72-3f4b-9ea5-2e7d8359ad0f | -10.60147 | -54.88839 | 2025-08-25 05:04:00 | NOAA-20 | TERRA NOVA DO NORTE | MATO GROSSO | Brasil | 5108055 | 51 | 33 | nan | nan | nan | Amazônia | 2.3 |
| c3dd348d-a0b7-3ddf-8806-f55480a56729 | -8.60512 | -62.59526 | 2025-08-25 05:04:00 | NOAA-20 | PORTO VELHO | RONDÔNIA | Brasil | 1100205 | 11 | 33 | nan | nan | nan | Amazônia | 1.7 |
| 192ad02c-c220-389e-9300-5c5f30644964 | -8.59252 | -62.59631 | 2025-08-25 05:04:00 | NOAA-20 | PORTO VELHO | RONDÔNIA | Brasil | 1100205 | 11 | 33 | nan | nan | nan | Amazônia | 1.4 |
| a58ae021-2092-318a-8b41-671cd3d031aa | -9.15297 | -59.49149 | 2025-08-25 05:04:00 | NOAA-20 | COLNIZA | MATO GROSSO | Brasil | 5103254 | 51 | 33 | nan | nan | nan | Amazônia | 1.3 |
| 82786866-42bf-336e-9964-0be72b37b060 | -9.19404 | -59.62193 | 2025-08-25 05:04:00 | NOAA-20 | COLNIZA | MATO GROSSO | Brasil | 5103254 | 51 | 33 | nan | nan | nan | Amazônia | 1.6 |
| c8c53d17-5ac6-3de1-a153-2bae5f7b5983 | -12.75898 | -48.11684 | 2025-08-25 05:04:00 | NOAA-20 | PARANÃ | TOCANTINS | Brasil | 1716208 | 17 | 33 | nan | nan | nan | Cerrado | 2.0 |
| fa329f2f-3846-312e-87fb-ac3f602662ea | -8.7995 | -47.31958 | 2025-08-25 05:04:00 | NOAA-20 | RECURSOLÂNDIA | TOCANTINS | Brasil | 1718501 | 17 | 33 | nan | nan | nan | Cerrado | 1.5 |
| 881c180d-aade-323d-927f-59e2d9604ccb | -9.07695 | -66.06525 | 2025-08-25 05:04:00 | NOAA-20 | LÁBREA | AMAZONAS | Brasil | 1302405 | 13 | 33 | nan | nan | nan | Amazônia | 7.5 |
| 6c5d22f0-be45-3320-94e9-14d52392bb54 | -10.60948 | -54.88185 | 2025-08-25 05:04:00 | NOAA-20 | TERRA NOVA DO NORTE | MATO GROSSO | Brasil | 5108055 | 51 | 33 | nan | nan | nan | Amazônia | 0.5 |
| 2d1a0cef-c11a-3e1d-9346-4d055a3a6d82 | -9.25537 | -59.6395 | 2025-08-25 05:04:00 | NOAA-20 | COLNIZA | MATO GROSSO | Brasil | 5103254 | 51 | 33 | nan | nan | nan | Amazônia | 2.1 |
| 80cbfed9-aaeb-3727-ab33-0986f15c5e3d | -10.60489 | -54.88894 | 2025-08-25 05:04:00 | NOAA-20 | TERRA NOVA DO NORTE | MATO GROSSO | Brasil | 5108055 | 51 | 33 | nan | nan | nan | Amazônia | 2.3 |
| a006de41-ad6e-3bd7-8632-4af94320443b | -7.45257 | -60.40891 | 2025-08-25 05:04:00 | NOAA-20 | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 1.6 |
| 330df0a0-c7c5-349a-88df-5b1aefe8d6bd | -8.32112 | -47.26255 | 2025-08-25 05:04:00 | NOAA-20 | GOIATINS | TOCANTINS | Brasil | 1709005 | 17 | 33 | nan | nan | nan | Cerrado | 0.9 |
| 44ebbed2-b915-343a-ab54-b9749de61ebb | -6.82914 | -58.94506 | 2025-08-25 05:04:00 | NOAA-20 | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 3.2 |
| 2c669874-3392-3c4d-a42d-f282604f27a7 | -9.22473 | -59.71183 | 2025-08-25 05:04:00 | NOAA-20 | COLNIZA | MATO GROSSO | Brasil | 5103254 | 51 | 33 | nan | nan | nan | Amazônia | 1.0 |
| 6e2a19d7-2d77-3c6a-bec1-110bbfb472dc | -9.14254 | -60.76854 | 2025-08-25 05:04:00 | NOAA-20 | COLNIZA | MATO GROSSO | Brasil | 5103254 | 51 | 33 | nan | nan | nan | Amazônia | 5.1 |
| 40674bef-d1db-3ba3-81a3-1390aa9f6ae9 | -9.18606 | -60.79111 | 2025-08-25 05:04:00 | NOAA-20 | COLNIZA | MATO GROSSO | Brasil | 5103254 | 51 | 33 | nan | nan | nan | Amazônia | 19.9 |
| b5b7039e-476f-3b0c-af15-fe6f0c57eb8f | -10.60832 | -54.88943 | 2025-08-25 05:04:00 | NOAA-20 | TERRA NOVA DO NORTE | MATO GROSSO | Brasil | 5108055 | 51 | 33 | nan | nan | nan | Amazônia | 1.0 |
| a7481514-d7e2-34f0-8fdb-ff21b581d96e | -10.70865 | -47.13893 | 2025-08-25 05:04:00 | NOAA-20 | PONTE ALTA DO TOCANTINS | TOCANTINS | Brasil | 1717909 | 17 | 33 | nan | nan | nan | Cerrado | 1.1 |
| 7416576c-7f79-3d51-b3f8-b82d62564f19 | -10.25294 | -59.10886 | 2025-08-25 05:04:00 | NOAA-20 | ARIPUANÃ | MATO GROSSO | Brasil | 5101407 | 51 | 33 | nan | nan | nan | Amazônia | 3.9 |
| 1dd5b1a2-451a-3821-8c3e-2f946bed202c | -6.82353 | -58.95675 | 2025-08-25 05:04:00 | NOAA-20 | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 3.8 |
| b3b31f76-c144-31cd-a6f1-aa193bfbd4a3 | -8.54499 | -63.51792 | 2025-08-25 05:04:00 | NOAA-20 | PORTO VELHO | RONDÔNIA | Brasil | 1100205 | 11 | 33 | nan | nan | nan | Amazônia | 1.5 |
| 3c8eb803-a0ac-3686-995d-0c247c8156d5 | -5.79533 | -59.21268 | 2025-08-25 05:04:00 | NOAA-20 | BORBA | AMAZONAS | Brasil | 1300805 | 13 | 33 | nan | nan | nan | Amazônia | 1.4 |
| 8aba09e9-7495-3cac-aeaa-341b89f45d62 | -8.21111 | -61.39162 | 2025-08-25 05:04:00 | NOAA-20 | NOVO ARIPUANÃ | AMAZONAS | Brasil | 1303304 | 13 | 33 | nan | nan | nan | Amazônia | 2.7 |
| 91dd68ee-fb7f-3464-8ded-50b2c2cd7117 | -6.63355 | -58.54847 | 2025-08-25 05:04:00 | NOAA-20 | MAUÉS | AMAZONAS | Brasil | 1302900 | 13 | 33 | nan | nan | nan | Amazônia | 1.7 |
| e3f6c669-2acb-3d64-8c4d-416323f9f5fa | -5.42696 | -60.17581 | 2025-08-25 05:04:00 | NOAA-20 | NOVO ARIPUANÃ | AMAZONAS | Brasil | 1303304 | 13 | 33 | nan | nan | nan | Amazônia | 1.7 |
| 0fa155be-baf2-3392-b68f-aa365a599162 | -8.89184 | -62.45813 | 2025-08-25 05:04:00 | NOAA-20 | CUJUBIM | RONDÔNIA | Brasil | 1100940 | 11 | 33 | nan | nan | nan | Amazônia | 1.8 |
| 8b5fecb7-1f02-332e-8bd9-634265d1ddb3 | -8.97815 | -65.40654 | 2025-08-25 05:04:00 | NOAA-20 | LÁBREA | AMAZONAS | Brasil | 1302405 | 13 | 33 | nan | nan | nan | Amazônia | 6.6 |
| 896f3459-3116-3f7d-9e8b-a24f54ac8867 | -8.89323 | -62.42479 | 2025-08-25 05:04:00 | NOAA-20 | CUJUBIM | RONDÔNIA | Brasil | 1100940 | 11 | 33 | nan | nan | nan | Amazônia | 1.5 |
| 99f56acd-e531-35ab-8bc5-61766af3ebba | -9.58055 | -55.36618 | 2025-08-25 05:04:00 | NOAA-20 | NOVO MUNDO | MATO GROSSO | Brasil | 5106265 | 51 | 33 | nan | nan | nan | Amazônia | 1.6 |
| 81328ac1-6aa3-3340-9479-f07232f6171f | -11.67389 | -51.58224 | 2025-08-25 05:04:00 | NOAA-20 | SÃO FÉLIX DO ARAGUAIA | MATO GROSSO | Brasil | 5107859 | 51 | 33 | nan | nan | nan | Amazônia | 1.8 |
| 65e04340-741a-308d-8a9f-3211cfa52ae2 | -8.22202 | -61.40093 | 2025-08-25 05:04:00 | NOAA-20 | NOVO ARIPUANÃ | AMAZONAS | Brasil | 1303304 | 13 | 33 | nan | nan | nan | Amazônia | 3.0 |
| 91322082-cee5-349a-8564-12fe4e96bb82 | -5.42855 | -60.16592 | 2025-08-25 05:04:00 | NOAA-20 | NOVO ARIPUANÃ | AMAZONAS | Brasil | 1303304 | 13 | 33 | nan | nan | nan | Amazônia | 1.6 |
| 6a165c74-de01-38b6-a51f-30c6e70452d0 | -8.65514 | -63.43341 | 2025-08-25 05:04:00 | NOAA-20 | CANDEIAS DO JAMARI | RONDÔNIA | Brasil | 1100809 | 11 | 33 | nan | nan | nan | Amazônia | 3.2 |


[Clique aqui para ver as próximas entradas](README72.md)
