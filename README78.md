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

## Dados Diários - Página 78

| ID | Latitude | Longitude | Data/Hora GMT | Satélite | Município | Estado | País | Município ID | Estado ID | País ID | Dias sem Chuva | Precipitação | Risco de Fogo | Bioma | FRP |
|----|----------|-----------|---------------|----------|-----------|--------|------|--------------|-----------|---------|----------------|--------------|----------------|-------|-----|
| 70b75c60-4ec3-3ebb-b771-c63b017da89d | -10.89447 | -55.71482 | 2025-09-08 05:21:00 | NPP-375D | NOVA CANAÃ DO NORTE | MATO GROSSO | Brasil | 5106216 | 51 | 33 | nan | nan | nan | Amazônia | 11.3 |
| 8d920355-c84b-3d26-90ad-324fb175103a | -11.41372 | -50.37344 | 2025-09-08 05:21:00 | NPP-375D | LAGOA DA CONFUSÃO | TOCANTINS | Brasil | 1711902 | 17 | 33 | nan | nan | nan | Cerrado | 3.3 |
| 1bbdc242-96e6-3ffa-9a89-2a2e2ed7dc6b | -12.93749 | -54.76672 | 2025-09-08 05:21:00 | NPP-375D | NOVA UBIRATÃ | MATO GROSSO | Brasil | 5106240 | 51 | 33 | nan | nan | nan | Amazônia | 1.3 |
| b99b6ae3-ec38-36f5-b6e7-47af2e3f949d | -9.96647 | -51.19924 | 2025-09-08 05:21:00 | NPP-375D | VILA RICA | MATO GROSSO | Brasil | 5108600 | 51 | 33 | nan | nan | nan | Amazônia | 0.9 |
| 8755c879-dd45-3722-b07b-403f1059c8ef | -12.94218 | -54.79505 | 2025-09-08 05:21:00 | NPP-375D | NOVA UBIRATÃ | MATO GROSSO | Brasil | 5106240 | 51 | 33 | nan | nan | nan | Cerrado | 4.9 |
| 96d35bf9-d58a-39bc-9832-b176072106c6 | -9.78606 | -48.33712 | 2025-09-08 05:21:00 | NPP-375D | LAJEADO | TOCANTINS | Brasil | 1712009 | 17 | 33 | nan | nan | nan | Cerrado | 2.8 |
| 5e2701ae-d4ab-3d00-ae33-cc55842dda2a | -9.44169 | -61.82172 | 2025-09-08 05:21:00 | NPP-375D | MACHADINHO D'OESTE | RONDÔNIA | Brasil | 1100130 | 11 | 33 | nan | nan | nan | Amazônia | 10.3 |
| 26eb6b06-b1ff-34b3-a305-8ce11776211d | -11.61981 | -47.14874 | 2025-09-08 05:21:00 | NPP-375D | ALMAS | TOCANTINS | Brasil | 1700400 | 17 | 33 | nan | nan | nan | Cerrado | 2.4 |
| ff3d71f7-7323-337d-ad40-dbd15d35be01 | -11.38609 | -50.41419 | 2025-09-08 05:21:00 | NPP-375D | LAGOA DA CONFUSÃO | TOCANTINS | Brasil | 1711902 | 17 | 33 | nan | nan | nan | Cerrado | 5.1 |
| 514fb3a1-6320-39d9-b746-e040b296ded5 | -7.87549 | -46.24949 | 2025-09-08 05:21:00 | NPP-375D | BALSAS | MARANHÃO | Brasil | 2101400 | 21 | 33 | nan | nan | nan | Cerrado | 3.7 |
| a21e010f-e57d-3e4b-a420-2d820e61dc3e | -11.28524 | -46.46117 | 2025-09-08 05:21:00 | NPP-375D | FORMOSA DO RIO PRETO | BAHIA | Brasil | 2911105 | 29 | 33 | nan | nan | nan | Cerrado | 2.9 |
| 9d4fbfff-1eae-3955-a3e6-22df8d162147 | -12.83481 | -52.93554 | 2025-09-08 05:21:00 | NPP-375D | GAÚCHA DO NORTE | MATO GROSSO | Brasil | 5103858 | 51 | 33 | nan | nan | nan | Amazônia | 0.8 |
| 50e76bc0-6e55-30b1-a823-15f2146f55be | -9.97966 | -51.67712 | 2025-09-08 05:21:00 | NPP-375D | VILA RICA | MATO GROSSO | Brasil | 5108600 | 51 | 33 | nan | nan | nan | Amazônia | 2.8 |
| 6b7cb573-2eed-3475-8351-ab5050dbbec6 | -12.95215 | -54.7847 | 2025-09-08 05:21:00 | NPP-375D | NOVA UBIRATÃ | MATO GROSSO | Brasil | 5106240 | 51 | 33 | nan | nan | nan | Amazônia | 1.1 |
| af08a2e9-adde-3bde-b033-5ecc34c0f61d | -11.40633 | -50.3873 | 2025-09-08 05:21:00 | NPP-375D | LAGOA DA CONFUSÃO | TOCANTINS | Brasil | 1711902 | 17 | 33 | nan | nan | nan | Cerrado | 4.6 |
| b411c82b-7053-3da9-9d3f-014f45d895ea | -7.4722 | -61.58978 | 2025-09-08 05:21:00 | NPP-375D | MANICORÉ | AMAZONAS | Brasil | 1302702 | 13 | 33 | nan | nan | nan | Amazônia | 1.8 |
| 1d9b1be4-531f-312b-8e3a-83cffdeedfac | -9.47287 | -60.49843 | 2025-09-08 05:21:00 | NPP-375D | ARIPUANÃ | MATO GROSSO | Brasil | 5101407 | 51 | 33 | nan | nan | nan | Amazônia | 1.7 |
| f787c494-326c-3ad1-920a-c47eacbc6d5b | -10.05378 | -59.35934 | 2025-09-08 05:21:00 | NPP-375D | ARIPUANÃ | MATO GROSSO | Brasil | 5101407 | 51 | 33 | nan | nan | nan | Amazônia | 1.9 |
| 57520eb2-9a32-34c2-81c4-33fe30f4ba91 | -9.33228 | -55.19106 | 2025-09-08 05:21:00 | NPP-375D | NOVO PROGRESSO | PARÁ | Brasil | 1505031 | 15 | 33 | nan | nan | nan | Amazônia | 2.1 |
| 922fb6fa-fce9-38e3-9e7e-5f254f3342e5 | -9.19506 | -46.04059 | 2025-09-08 05:21:00 | NPP-375D | ALTO PARNAÍBA | MARANHÃO | Brasil | 2100501 | 21 | 33 | nan | nan | nan | Cerrado | 2.4 |
| ddde880e-9a2b-3d0a-8874-b9412978998c | -9.38813 | -62.33807 | 2025-09-08 05:21:00 | NPP-375D | MACHADINHO D'OESTE | RONDÔNIA | Brasil | 1100130 | 11 | 33 | nan | nan | nan | Amazônia | 4.6 |
| a8e1f20b-62b6-39af-8022-63d65c3c3ba2 | -6.16616 | -57.93924 | 2025-09-08 05:21:00 | NPP-375D | JACAREACANGA | PARÁ | Brasil | 1503754 | 15 | 33 | nan | nan | nan | Amazônia | 1.1 |
| c9c75228-e0d9-3c34-be4f-81c64a7a6e06 | -12.85626 | -47.98284 | 2025-09-08 05:21:00 | NPP-375D | PARANÃ | TOCANTINS | Brasil | 1716208 | 17 | 33 | nan | nan | nan | Cerrado | 2.7 |
| 90745dc2-b192-3810-981e-c872c6013f48 | -6.22647 | -49.41681 | 2025-09-08 05:21:00 | NPP-375D | ELDORADO DO CARAJÁS | PARÁ | Brasil | 1502954 | 15 | 33 | nan | nan | nan | Amazônia | 2.8 |
| f8f19581-c944-3895-a088-cb748e9bef99 | -8.19467 | -50.14112 | 2025-09-08 05:21:00 | NPP-375D | REDENÇÃO | PARÁ | Brasil | 1506138 | 15 | 33 | nan | nan | nan | Amazônia | 1.9 |
| 25e220ef-fc91-3aef-b7ff-555af224352a | -8.88853 | -51.0569 | 2025-09-08 05:21:00 | NPP-375D | SANTANA DO ARAGUAIA | PARÁ | Brasil | 1506708 | 15 | 33 | nan | nan | nan | Amazônia | 1.3 |
| fd9963dd-adb7-3a24-a534-a9770b22faee | -13.54452 | -48.11141 | 2025-09-08 05:21:00 | NPP-375D | MINAÇU | GOIÁS | Brasil | 5213087 | 52 | 33 | nan | nan | nan | Cerrado | 2.0 |
| 48827c2f-4f28-3a9f-bbdf-1f468216a2a5 | -11.6131 | -47.14719 | 2025-09-08 05:21:00 | NPP-375D | ALMAS | TOCANTINS | Brasil | 1700400 | 17 | 33 | nan | nan | nan | Cerrado | 1.7 |
| 551d3d5d-bffd-3bbd-9d46-35381102046a | -11.20789 | -55.00209 | 2025-09-08 05:21:00 | NPP-375D | CLÁUDIA | MATO GROSSO | Brasil | 5103056 | 51 | 33 | nan | nan | nan | Amazônia | 1.7 |
| e5f2db42-b55b-3801-a72b-ddabefe6dbf7 | -12.93852 | -54.79058 | 2025-09-08 05:21:00 | NPP-375D | NOVA UBIRATÃ | MATO GROSSO | Brasil | 5106240 | 51 | 33 | nan | nan | nan | Amazônia | 2.4 |
| 17b54f88-606b-3429-9e96-c870547a8fe9 | -7.3928 | -61.63309 | 2025-09-08 05:21:00 | NPP-375D | MANICORÉ | AMAZONAS | Brasil | 1302702 | 13 | 33 | nan | nan | nan | Amazônia | 4.6 |
| a944fab0-7ba0-309d-916d-4145abdbe3ec | -10.16823 | -61.12374 | 2025-09-08 05:21:00 | NPP-375D | RONDOLÂNDIA | MATO GROSSO | Brasil | 5107578 | 51 | 33 | nan | nan | nan | Amazônia | 2.1 |
| 1687b686-d14e-3e2f-9edc-a9a0cfa6ceac | -11.41186 | -50.38802 | 2025-09-08 05:21:00 | NPP-375D | LAGOA DA CONFUSÃO | TOCANTINS | Brasil | 1711902 | 17 | 33 | nan | nan | nan | Cerrado | 5.6 |
| 15c86ef0-2277-34d9-ad4b-dc97cb2c571d | -6.83763 | -52.8054 | 2025-09-08 05:21:00 | NPP-375D | SÃO FÉLIX DO XINGU | PARÁ | Brasil | 1507300 | 15 | 33 | nan | nan | nan | Amazônia | 2.3 |
| 161ad349-5946-3f6a-a908-98c983fa882e | -6.221 | -49.41594 | 2025-09-08 05:21:00 | NPP-375D | ELDORADO DO CARAJÁS | PARÁ | Brasil | 1502954 | 15 | 33 | nan | nan | nan | Amazônia | 2.3 |
| a205b1f7-b34d-3108-96fc-d6bd00b93c54 | -9.96213 | -51.19249 | 2025-09-08 05:21:00 | NPP-375D | VILA RICA | MATO GROSSO | Brasil | 5108600 | 51 | 33 | nan | nan | nan | Amazônia | 4.4 |
| fc96122a-173b-3635-974e-e9e77b4f798e | -6.84418 | -52.85367 | 2025-09-08 05:21:00 | NPP-375D | SÃO FÉLIX DO XINGU | PARÁ | Brasil | 1507300 | 15 | 33 | nan | nan | nan | Amazônia | 1.3 |
| 8940d59d-7c16-3408-a2d4-9d72ba4364fe | -9.69539 | -57.80249 | 2025-09-08 05:21:00 | NPP-375D | NOVA BANDEIRANTES | MATO GROSSO | Brasil | 5106158 | 51 | 33 | nan | nan | nan | Amazônia | 1.6 |
| 93b4366d-fcac-3e74-beb9-21ba0381d923 | -6.53984 | -49.50597 | 2025-09-08 05:21:00 | NPP-375D | XINGUARA | PARÁ | Brasil | 1508407 | 15 | 33 | nan | nan | nan | Amazônia | 0.8 |
| 73d2c602-2e98-38a3-9a36-9174d9841018 | -12.83465 | -52.89879 | 2025-09-08 05:21:00 | NPP-375D | GAÚCHA DO NORTE | MATO GROSSO | Brasil | 5103858 | 51 | 33 | nan | nan | nan | Amazônia | 3.3 |
| a92493d2-8355-36f6-9bbc-8bbc849af4f0 | -9.9619 | -59.59645 | 2025-09-08 05:21:00 | NPP-375D | ARIPUANÃ | MATO GROSSO | Brasil | 5101407 | 51 | 33 | nan | nan | nan | Amazônia | 1.2 |
| 4dfe0cab-6e7e-3bec-93e8-d1b9e846b85a | -9.10322 | -60.97025 | 2025-09-08 05:21:00 | NPP-375D | COLNIZA | MATO GROSSO | Brasil | 5103254 | 51 | 33 | nan | nan | nan | Amazônia | 1.0 |
| 919b54d5-16ae-36a5-af68-c6a3f44656e5 | -12.94429 | -54.77963 | 2025-09-08 05:21:00 | NPP-375D | NOVA UBIRATÃ | MATO GROSSO | Brasil | 5106240 | 51 | 33 | nan | nan | nan | Amazônia | 1.3 |
| 831463db-2ba0-3a02-8e10-9da859cbd016 | -6.957 | -62.93124 | 2025-09-08 05:21:00 | NPP-375D | HUMAITÁ | AMAZONAS | Brasil | 1301704 | 13 | 33 | nan | nan | nan | Amazônia | 1.6 |
| b544a31e-2bbb-3c97-8938-32495c2609a8 | -11.01774 | -46.03074 | 2025-09-08 05:21:00 | NPP-375D | FORMOSA DO RIO PRETO | BAHIA | Brasil | 2911105 | 29 | 33 | nan | nan | nan | Cerrado | 2.5 |
| f80ad3c4-deec-37e0-951e-dcfbf6be2088 | -13.81174 | -46.27369 | 2025-09-08 05:21:00 | NPP-375D | GUARANI DE GOIÁS | GOIÁS | Brasil | 5209408 | 52 | 33 | nan | nan | nan | Cerrado | 6.4 |
| 57987ceb-d65e-3423-911c-60ca68fc621c | -12.94637 | -54.79567 | 2025-09-08 05:21:00 | NPP-375D | NOVA UBIRATÃ | MATO GROSSO | Brasil | 5106240 | 51 | 33 | nan | nan | nan | Amazônia | 2.2 |
| 09a0dcca-4f0e-3e63-8070-ba71f0d9d052 | -9.25939 | -67.60628 | 2025-09-08 05:21:00 | NPP-375D | BOCA DO ACRE | AMAZONAS | Brasil | 1300706 | 13 | 33 | nan | nan | nan | Amazônia | 2.0 |
| 907db37f-afe3-3737-9892-66718d03b712 | -9.46419 | -56.04736 | 2025-09-08 05:21:00 | NPP-375D | ALTA FLORESTA | MATO GROSSO | Brasil | 5100250 | 51 | 33 | nan | nan | nan | Amazônia | 1.6 |
| e0ae0a5f-42f5-3078-a3ab-302e9f8220e5 | -12.94955 | -54.77239 | 2025-09-08 05:21:00 | NPP-375D | NOVA UBIRATÃ | MATO GROSSO | Brasil | 5106240 | 51 | 33 | nan | nan | nan | Amazônia | 2.0 |
| fc39b1c8-11a2-332e-b0ec-dbc0871d19a1 | -11.86368 | -51.05361 | 2025-09-08 05:21:00 | NPP-375D | SÃO FÉLIX DO ARAGUAIA | MATO GROSSO | Brasil | 5107859 | 51 | 33 | nan | nan | nan | Cerrado | 2.5 |
| 8a73f04f-2719-341a-bd97-d6c9de9e753a | -9.95604 | -67.19644 | 2025-09-08 05:21:00 | NPP-375D | SENADOR GUIOMARD | ACRE | Brasil | 1200450 | 12 | 33 | nan | nan | nan | Amazônia | 1.2 |
| 34bff567-eb05-35d9-ab11-224a07082ecb | -9.98049 | -51.67766 | 2025-09-08 05:21:00 | NPP-375D | VILA RICA | MATO GROSSO | Brasil | 5108600 | 51 | 33 | nan | nan | nan | Amazônia | 3.0 |
| a30860a3-c1e4-3f80-9ae4-9a919a03d194 | -12.95376 | -54.77293 | 2025-09-08 05:21:00 | NPP-375D | NOVA UBIRATÃ | MATO GROSSO | Brasil | 5106240 | 51 | 33 | nan | nan | nan | Amazônia | 2.0 |
| b0e553ce-84c9-38ce-aea2-a8b8c0bf3735 | -7.74037 | -50.31233 | 2025-09-08 05:21:00 | NPP-375D | PAU D'ARCO | PARÁ | Brasil | 1505551 | 15 | 33 | nan | nan | nan | Amazônia | 1.5 |
| 4e495e3a-f674-3cae-b0bd-3b342d74f313 | -6.28115 | -53.44579 | 2025-09-08 05:21:00 | NPP-375D | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 0.7 |
| d93576c1-570f-3481-90ba-0d4d71a12a12 | -11.66337 | -46.88266 | 2025-09-08 05:21:00 | NPP-375D | DIANÓPOLIS | TOCANTINS | Brasil | 1707009 | 17 | 33 | nan | nan | nan | Cerrado | 2.6 |
| d2341516-36a0-3141-8671-b759a294806c | -6.2851 | -53.41934 | 2025-09-08 05:21:00 | NPP-375D | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 1.7 |
| 9aca4efc-bf9b-3381-b898-e3c4419308fc | -9.1852 | -60.76767 | 2025-09-08 05:21:00 | NPP-375D | COLNIZA | MATO GROSSO | Brasil | 5103254 | 51 | 33 | nan | nan | nan | Amazônia | 3.2 |
| c72dd723-6490-3016-a6bf-5ebae711ef82 | -9.97402 | -51.6814 | 2025-09-08 05:21:00 | NPP-375D | VILA RICA | MATO GROSSO | Brasil | 5108600 | 51 | 33 | nan | nan | nan | Amazônia | 2.8 |
| 8489b508-0f4c-3375-aca9-5aa1c05de311 | -10.76973 | -59.85536 | 2025-09-08 05:21:00 | NPP-375D | ARIPUANÃ | MATO GROSSO | Brasil | 5101407 | 51 | 33 | nan | nan | nan | Amazônia | 1.2 |
| a68366a9-96a0-3f3e-ad76-73f84c7ec90a | -12.95211 | -54.8161 | 2025-09-08 05:21:00 | NPP-375D | NOVA UBIRATÃ | MATO GROSSO | Brasil | 5106240 | 51 | 33 | nan | nan | nan | Cerrado | 1.2 |
| 931858f4-0dc9-357f-980e-59f94b28b4ea | -13.82119 | -46.25428 | 2025-09-08 05:21:00 | NPP-375D | CORRENTINA | BAHIA | Brasil | 2909307 | 29 | 33 | nan | nan | nan | Cerrado | 3.8 |
| baba9071-e4ea-3b89-bd55-1ec366ce39f8 | -11.2104 | -55.01334 | 2025-09-08 05:21:00 | NPP-375D | CLÁUDIA | MATO GROSSO | Brasil | 5103056 | 51 | 33 | nan | nan | nan | Amazônia | 1.7 |
| aa0e04d4-0ddd-33a4-b745-c52ed598a507 | -6.63706 | -53.37122 | 2025-09-08 05:21:00 | NPP-375D | SÃO FÉLIX DO XINGU | PARÁ | Brasil | 1507300 | 15 | 33 | nan | nan | nan | Amazônia | 1.5 |
| cd1fe68c-0f28-33b8-b4b5-37dbbf3e5a53 | -11.66311 | -46.88283 | 2025-09-08 05:21:00 | NPP-375D | DIANÓPOLIS | TOCANTINS | Brasil | 1707009 | 17 | 33 | nan | nan | nan | Cerrado | 1.8 |
| 76fb7965-f628-3bca-adca-587b406ddb9f | -9.06955 | -60.48421 | 2025-09-08 05:21:00 | NPP-375D | COLNIZA | MATO GROSSO | Brasil | 5103254 | 51 | 33 | nan | nan | nan | Amazônia | 0.6 |
| ef6f5629-ac78-379e-a7fd-469172abc5f5 | -9.18066 | -60.77432 | 2025-09-08 05:21:00 | NPP-375D | COLNIZA | MATO GROSSO | Brasil | 5103254 | 51 | 33 | nan | nan | nan | Amazônia | 1.1 |
| a934805c-a90e-3bad-907d-6f4d4212a5b5 | -8.20048 | -50.13858 | 2025-09-08 05:21:00 | NPP-375D | REDENÇÃO | PARÁ | Brasil | 1506138 | 15 | 33 | nan | nan | nan | Amazônia | 2.3 |
| 31efd1c5-867e-33c3-80b9-ea95f4f9a11d | -6.22597 | -49.42028 | 2025-09-08 05:21:00 | NPP-375D | ELDORADO DO CARAJÁS | PARÁ | Brasil | 1502954 | 15 | 33 | nan | nan | nan | Amazônia | 1.5 |
| a0768fc1-b04c-3a68-9bbc-b42d1c7a6a88 | -12.93383 | -54.76216 | 2025-09-08 05:21:00 | NPP-375D | NOVA UBIRATÃ | MATO GROSSO | Brasil | 5106240 | 51 | 33 | nan | nan | nan | Amazônia | 1.3 |
| e6f031df-bcda-3d9d-8a6b-6187cbdda7ba | -11.90724 | -50.98914 | 2025-09-08 05:21:00 | NPP-375D | SÃO FÉLIX DO ARAGUAIA | MATO GROSSO | Brasil | 5107859 | 51 | 33 | nan | nan | nan | Cerrado | 3.3 |
| 39b77633-e3f4-3ab7-962b-9884d2178787 | -7.43356 | -49.26131 | 2025-09-08 05:21:00 | NPP-375D | PAU D'ARCO | TOCANTINS | Brasil | 1716307 | 17 | 33 | nan | nan | nan | Amazônia | 1.2 |
| 537eb408-b7bc-3151-90fd-95f3b04e0b18 | -5.83464 | -52.20242 | 2025-09-08 05:21:00 | NPP-375D | SÃO FÉLIX DO XINGU | PARÁ | Brasil | 1507300 | 15 | 33 | nan | nan | nan | Amazônia | 1.5 |
| 91bc1bd1-797d-3866-ad56-01eaa443b245 | -12.87582 | -47.98605 | 2025-09-08 05:21:00 | NPP-375D | PARANÃ | TOCANTINS | Brasil | 1716208 | 17 | 33 | nan | nan | nan | Cerrado | 2.1 |
| ca18b747-b7b7-3c8c-a12d-ce953f1a28d4 | -13.73772 | -46.90004 | 2025-09-08 05:21:00 | NPP-375D | NOVA ROMA | GOIÁS | Brasil | 5214903 | 52 | 33 | nan | nan | nan | Cerrado | 2.4 |
| 857abe33-5037-3875-9409-8f86190a2d07 | -7.2289 | -46.21122 | 2025-09-08 05:21:00 | NPP-375D | NOVA COLINAS | MARANHÃO | Brasil | 2107258 | 21 | 33 | nan | nan | nan | Cerrado | 2.5 |
| 1df82872-a978-30ee-9be7-fbd110612745 | -9.99184 | -51.66813 | 2025-09-08 05:21:00 | NPP-375D | VILA RICA | MATO GROSSO | Brasil | 5108600 | 51 | 33 | nan | nan | nan | Amazônia | 4.4 |
| 1d00acb7-87b2-3cb9-a5b5-d7a0df8538f5 | -9.94375 | -60.49832 | 2025-09-08 05:21:00 | NPP-375D | ARIPUANÃ | MATO GROSSO | Brasil | 5101407 | 51 | 33 | nan | nan | nan | Amazônia | 1.1 |
| 224d03df-f85c-3c41-815e-466466f488a2 | -9.82205 | -53.31832 | 2025-09-08 05:21:00 | NPP-375D | PEIXOTO DE AZEVEDO | MATO GROSSO | Brasil | 5106422 | 51 | 33 | nan | nan | nan | Amazônia | 2.2 |
| d47158db-fcaf-3302-b62b-3b26b943a47b | -11.40494 | -50.39822 | 2025-09-08 05:21:00 | NPP-375D | LAGOA DA CONFUSÃO | TOCANTINS | Brasil | 1711902 | 17 | 33 | nan | nan | nan | Cerrado | 1.7 |
| 621f8d62-1af3-3cdf-a398-984294ba53c1 | -11.91259 | -50.98985 | 2025-09-08 05:21:00 | NPP-375D | SÃO FÉLIX DO ARAGUAIA | MATO GROSSO | Brasil | 5107859 | 51 | 33 | nan | nan | nan | Cerrado | 3.3 |
| cf825dc5-2a29-3042-9fef-700fa57563c3 | -6.542 | -54.98789 | 2025-09-08 05:21:00 | NPP-375D | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 1.1 |
| 51d9e661-35e2-3a13-93ba-219a9a486724 | -12.25901 | -59.32273 | 2025-09-08 05:21:00 | NPP-375D | JUÍNA | MATO GROSSO | Brasil | 5105150 | 51 | 33 | nan | nan | nan | Cerrado | 0.9 |
| f44bc28d-1d21-3a67-9b79-34ab420b3231 | -9.44927 | -61.81904 | 2025-09-08 05:21:00 | NPP-375D | MACHADINHO D'OESTE | RONDÔNIA | Brasil | 1100130 | 11 | 33 | nan | nan | nan | Amazônia | 7.2 |
| 2cf0cd1f-7c3f-342c-9fc5-d23c27f1c516 | -8.50142 | -51.33337 | 2025-09-08 05:21:00 | NPP-375D | CUMARU DO NORTE | PARÁ | Brasil | 1502764 | 15 | 33 | nan | nan | nan | Amazônia | 3.5 |
| 3f52b5ac-7c79-332c-a020-333eda098f96 | -7.78097 | -52.1287 | 2025-09-08 05:21:00 | NPP-375D | SÃO FÉLIX DO XINGU | PARÁ | Brasil | 1507300 | 15 | 33 | nan | nan | nan | Amazônia | 1.8 |
| e62ecb68-c412-38ba-a776-eb22c529d944 | -13.70971 | -46.87434 | 2025-09-08 05:21:00 | NPP-375D | NOVA ROMA | GOIÁS | Brasil | 5214903 | 52 | 33 | nan | nan | nan | Cerrado | 1.3 |
| 1e2846b1-db20-31ef-85cf-e12cd0b21c91 | -11.22353 | -55.00792 | 2025-09-08 05:21:00 | NPP-375D | CLÁUDIA | MATO GROSSO | Brasil | 5103056 | 51 | 33 | nan | nan | nan | Amazônia | 1.5 |
| bc686de9-f8ae-3a9d-ba32-dfc91ec572c0 | -12.95009 | -54.76847 | 2025-09-08 05:21:00 | NPP-375D | NOVA UBIRATÃ | MATO GROSSO | Brasil | 5106240 | 51 | 33 | nan | nan | nan | Amazônia | 2.5 |
| da88214e-2d0f-30d5-a315-d17f725879d0 | -12.61271 | -56.9748 | 2025-09-08 05:21:00 | NPP-375D | NOVA MARINGÁ | MATO GROSSO | Brasil | 5108907 | 51 | 33 | nan | nan | nan | Amazônia | 3.6 |
| ed74c279-79ca-363c-9321-1fadafa83e70 | -9.85262 | -48.85015 | 2025-09-08 05:21:00 | NPP-375D | BARROLÂNDIA | TOCANTINS | Brasil | 1703107 | 17 | 33 | nan | nan | nan | Cerrado | 1.7 |
| b2da1e89-f4b5-30b7-b8ae-baa80f8aad11 | -12.85703 | -47.97557 | 2025-09-08 05:21:00 | NPP-375D | PARANÃ | TOCANTINS | Brasil | 1716208 | 17 | 33 | nan | nan | nan | Cerrado | 3.1 |
| d94443c2-67e1-3ed8-bcc1-51abe77f48a2 | -8.19504 | -50.13834 | 2025-09-08 05:21:00 | NPP-375D | REDENÇÃO | PARÁ | Brasil | 1506138 | 15 | 33 | nan | nan | nan | Amazônia | 1.9 |
| 659bfe81-9b8e-387c-b0ef-70b4ccb0ff49 | -11.86197 | -51.06689 | 2025-09-08 05:21:00 | NPP-375D | SÃO FÉLIX DO ARAGUAIA | MATO GROSSO | Brasil | 5107859 | 51 | 33 | nan | nan | nan | Cerrado | 5.9 |
| 53642fa7-6247-3f38-976e-aab7b1cfd409 | -9.96336 | -55.04002 | 2025-09-08 05:21:00 | NPP-375D | NOVO MUNDO | MATO GROSSO | Brasil | 5106265 | 51 | 33 | nan | nan | nan | Amazônia | 1.7 |
| ad253dc7-270e-36c0-adb6-603ed495b159 | -8.08313 | -54.76044 | 2025-09-08 05:21:00 | NPP-375D | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 1.6 |
| a35d0e32-aee1-316d-a96a-890641d636aa | -9.17221 | -59.37328 | 2025-09-08 05:21:00 | NPP-375D | COLNIZA | MATO GROSSO | Brasil | 5103254 | 51 | 33 | nan | nan | nan | Amazônia | 2.8 |
| fb27960a-9085-37cb-867e-14cd8971bd52 | -11.27922 | -46.46872 | 2025-09-08 05:21:00 | NPP-375D | FORMOSA DO RIO PRETO | BAHIA | Brasil | 2911105 | 29 | 33 | nan | nan | nan | Cerrado | 0.9 |
| 2f246e10-5abd-3cc1-9e81-a549fd08676a | -9.43519 | -62.36261 | 2025-09-08 05:21:00 | NPP-375D | MACHADINHO D'OESTE | RONDÔNIA | Brasil | 1100130 | 11 | 33 | nan | nan | nan | Amazônia | 1.1 |


[Clique aqui para ver as próximas entradas](README79.md)
