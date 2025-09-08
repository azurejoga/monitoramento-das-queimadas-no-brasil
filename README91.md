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

## Dados Diários - Página 91

| ID | Latitude | Longitude | Data/Hora GMT | Satélite | Município | Estado | País | Município ID | Estado ID | País ID | Dias sem Chuva | Precipitação | Risco de Fogo | Bioma | FRP |
|----|----------|-----------|---------------|----------|-----------|--------|------|--------------|-----------|---------|----------------|--------------|----------------|-------|-----|
| 61fb4194-bd20-36cd-8eaf-e1a878278c29 | -9.16824 | -59.38264 | 2025-09-08 05:42:00 | NOAA-20 | COLNIZA | MATO GROSSO | Brasil | 5103254 | 51 | 33 | nan | nan | nan | Amazônia | 2.0 |
| 4fb39060-5ca4-39bd-8531-3b882c9afe34 | -9.10626 | -60.97046 | 2025-09-08 05:42:00 | NOAA-20 | COLNIZA | MATO GROSSO | Brasil | 5103254 | 51 | 33 | nan | nan | nan | Amazônia | 1.0 |
| 2ffc5cc8-0be8-3911-a610-159006df886b | -9.93337 | -60.10437 | 2025-09-08 05:42:00 | NOAA-20 | ARIPUANÃ | MATO GROSSO | Brasil | 5101407 | 51 | 33 | nan | nan | nan | Amazônia | 1.8 |
| 1df965f5-1491-3fba-a584-70242a14089a | -9.17887 | -60.77724 | 2025-09-08 05:42:00 | NOAA-20 | COLNIZA | MATO GROSSO | Brasil | 5103254 | 51 | 33 | nan | nan | nan | Amazônia | 0.6 |
| fe4cb88d-07e6-3e4c-8b3d-ff2e4852a007 | -9.47352 | -60.48986 | 2025-09-08 05:42:00 | NOAA-20 | ARIPUANÃ | MATO GROSSO | Brasil | 5101407 | 51 | 33 | nan | nan | nan | Amazônia | 1.7 |
| 18453d4d-b4aa-3071-b776-dfbe3c24ea26 | -9.18449 | -60.76691 | 2025-09-08 05:42:00 | NOAA-20 | COLNIZA | MATO GROSSO | Brasil | 5103254 | 51 | 33 | nan | nan | nan | Amazônia | 2.8 |
| 528c6130-84bb-3243-ad6d-f01933b96e7e | -9.20528 | -65.91051 | 2025-09-08 05:42:00 | NOAA-20 | LÁBREA | AMAZONAS | Brasil | 1302405 | 13 | 33 | nan | nan | nan | Amazônia | 0.9 |
| 873de774-7859-3522-87fc-85d92640412f | -7.47472 | -61.58851 | 2025-09-08 05:42:00 | NOAA-20 | MANICORÉ | AMAZONAS | Brasil | 1302702 | 13 | 33 | nan | nan | nan | Amazônia | 1.6 |
| 98b01529-dc25-3a40-8f82-549dc4d325e1 | -7.9065 | -61.78209 | 2025-09-08 05:42:00 | NOAA-20 | MANICORÉ | AMAZONAS | Brasil | 1302702 | 13 | 33 | nan | nan | nan | Amazônia | 1.5 |
| fdb9e5c1-6254-3d3f-87d1-cb10ab1ea899 | -10.50969 | -57.80395 | 2025-09-08 05:42:00 | NOAA-20 | JUARA | MATO GROSSO | Brasil | 5105101 | 51 | 33 | nan | nan | nan | Amazônia | 1.2 |
| efd55ae1-076f-33b5-9466-70e08a41ae20 | -9.18856 | -60.76751 | 2025-09-08 05:42:00 | NOAA-20 | COLNIZA | MATO GROSSO | Brasil | 5103254 | 51 | 33 | nan | nan | nan | Amazônia | 2.8 |
| e91ff863-59f1-33b5-8b2d-cccda265209b | -9.20069 | -60.62361 | 2025-09-08 05:42:00 | NOAA-20 | COLNIZA | MATO GROSSO | Brasil | 5103254 | 51 | 33 | nan | nan | nan | Amazônia | 0.9 |
| 9e8cc6f7-2b8b-3151-8b39-cb7ee0e50610 | -9.13306 | -65.95965 | 2025-09-08 05:42:00 | NOAA-20 | LÁBREA | AMAZONAS | Brasil | 1302405 | 13 | 33 | nan | nan | nan | Amazônia | 1.8 |
| 280c6892-dc19-38ff-81dc-96466bf1318a | -9.17395 | -59.37431 | 2025-09-08 05:42:00 | NOAA-20 | COLNIZA | MATO GROSSO | Brasil | 5103254 | 51 | 33 | nan | nan | nan | Amazônia | 2.8 |
| 3d6b149f-208b-3450-bbc1-63c2001a5e47 | -11.77958 | -60.89581 | 2025-09-08 05:42:00 | NOAA-20 | PIMENTA BUENO | RONDÔNIA | Brasil | 1100189 | 11 | 33 | nan | nan | nan | Amazônia | 1.0 |
| a2b6ef08-7db5-39a2-8fb7-34c47a97bc95 | -10.892 | -55.71688 | 2025-09-08 05:42:00 | NOAA-20 | NOVA CANAÃ DO NORTE | MATO GROSSO | Brasil | 5106216 | 51 | 33 | nan | nan | nan | Amazônia | 3.1 |
| 00d37c9f-3df0-3841-9023-fe5dfb3abb17 | -7.40007 | -61.62425 | 2025-09-08 05:42:00 | NOAA-20 | MANICORÉ | AMAZONAS | Brasil | 1302702 | 13 | 33 | nan | nan | nan | Amazônia | 12.8 |
| 11266061-4384-3eac-8beb-999c2c1b241d | -10.05477 | -59.36018 | 2025-09-08 05:42:00 | NOAA-20 | ARIPUANÃ | MATO GROSSO | Brasil | 5101407 | 51 | 33 | nan | nan | nan | Amazônia | 5.9 |
| 8ec211d4-ff53-3c61-a014-842eca813c8e | -11.04585 | -54.17337 | 2025-09-08 05:42:00 | NOAA-20 | MARCELÂNDIA | MATO GROSSO | Brasil | 5105580 | 51 | 33 | nan | nan | nan | Amazônia | 0.8 |
| 3990c9b0-f856-39d5-ad6c-a39fc6d597c8 | -9.24342 | -60.84868 | 2025-09-08 05:42:00 | NOAA-20 | COLNIZA | MATO GROSSO | Brasil | 5103254 | 51 | 33 | nan | nan | nan | Amazônia | 0.7 |
| 056a0399-2e32-3847-a9e9-c1d4cc244b37 | -8.88033 | -69.34322 | 2025-09-08 05:42:00 | NOAA-20 | MANOEL URBANO | ACRE | Brasil | 1200344 | 12 | 33 | nan | nan | nan | Amazônia | 1.2 |
| 284e6434-0568-3713-8762-363d18b72abb | -10.27088 | -63.16832 | 2025-09-08 05:42:00 | NOAA-20 | CACAULÂNDIA | RONDÔNIA | Brasil | 1100601 | 11 | 33 | nan | nan | nan | Amazônia | 2.3 |
| f941c29e-c3b1-32d1-af80-65d1ae146535 | -9.2416 | -57.06756 | 2025-09-08 05:42:00 | NOAA-20 | PARANAÍTA | MATO GROSSO | Brasil | 5106299 | 51 | 33 | nan | nan | nan | Amazônia | 1.2 |
| 4013b964-a624-3cf4-841b-b251743a71cd | -9.81452 | -53.32792 | 2025-09-08 05:42:00 | NOAA-20 | PEIXOTO DE AZEVEDO | MATO GROSSO | Brasil | 5106422 | 51 | 33 | nan | nan | nan | Amazônia | 2.4 |
| 3b3a30ee-b753-3ab8-bae9-736d6debdfd7 | -9.62739 | -64.20935 | 2025-09-08 05:42:00 | NOAA-20 | PORTO VELHO | RONDÔNIA | Brasil | 1100205 | 11 | 33 | nan | nan | nan | Amazônia | 3.7 |
| b7f537e0-7303-3850-b8b3-7e06dc084c4a | -9.09008 | -64.01453 | 2025-09-08 05:42:00 | NOAA-20 | PORTO VELHO | RONDÔNIA | Brasil | 1100205 | 11 | 33 | nan | nan | nan | Amazônia | 0.5 |
| 026896ab-3042-31b1-93c6-e5f025556bb5 | -9.13085 | -65.95216 | 2025-09-08 05:42:00 | NOAA-20 | LÁBREA | AMAZONAS | Brasil | 1302405 | 13 | 33 | nan | nan | nan | Amazônia | 1.1 |
| d6bd2042-a5e8-312e-b714-b02bfcbed72a | -7.39422 | -61.63489 | 2025-09-08 05:42:00 | NOAA-20 | MANICORÉ | AMAZONAS | Brasil | 1302702 | 13 | 33 | nan | nan | nan | Amazônia | 4.0 |
| b2bcedae-cc79-32cf-9232-c73d7dc44375 | -7.7722 | -61.37725 | 2025-09-08 05:42:00 | NOAA-20 | MANICORÉ | AMAZONAS | Brasil | 1302702 | 13 | 33 | nan | nan | nan | Amazônia | 1.0 |
| cf2abdcd-c146-3621-8971-f5aa0c3b4fbf | -6.95008 | -62.92843 | 2025-09-08 05:42:00 | NOAA-20 | HUMAITÁ | AMAZONAS | Brasil | 1301704 | 13 | 33 | nan | nan | nan | Amazônia | 1.0 |
| 12b55f2f-1fdc-331c-8507-367c95421af1 | -9.53435 | -59.06671 | 2025-09-08 05:42:00 | NOAA-20 | COLNIZA | MATO GROSSO | Brasil | 5103254 | 51 | 33 | nan | nan | nan | Amazônia | 6.0 |
| c5580c0a-7ad2-3ce9-b61a-d6578f3a827e | -9.94481 | -60.14766 | 2025-09-08 05:42:00 | NOAA-20 | ARIPUANÃ | MATO GROSSO | Brasil | 5101407 | 51 | 33 | nan | nan | nan | Amazônia | 1.8 |
| e18ff8ac-fc9a-3d9a-9c50-3457df27bb20 | -10.58032 | -61.25904 | 2025-09-08 05:42:00 | NOAA-20 | RONDOLÂNDIA | MATO GROSSO | Brasil | 5107578 | 51 | 33 | nan | nan | nan | Amazônia | 1.7 |
| 161989ce-091c-3c5d-a1c6-fc5266aa5153 | -10.57491 | -61.25857 | 2025-09-08 05:42:00 | NOAA-20 | RONDOLÂNDIA | MATO GROSSO | Brasil | 5107578 | 51 | 33 | nan | nan | nan | Amazônia | 1.7 |
| b6a7d379-c8dc-3482-b12d-1ea1ceee98aa | -9.79525 | -59.80635 | 2025-09-08 05:42:00 | NOAA-20 | ARIPUANÃ | MATO GROSSO | Brasil | 5101407 | 51 | 33 | nan | nan | nan | Amazônia | 1.5 |
| 0efaafca-de5f-323e-adf2-3e498f1f88b9 | -12.82402 | -52.89266 | 2025-09-08 05:42:00 | NOAA-20 | GAÚCHA DO NORTE | MATO GROSSO | Brasil | 5103858 | 51 | 33 | nan | nan | nan | Amazônia | 2.5 |
| e5223a6b-1fc2-3e75-ae9d-81aa384b4f64 | -6.82441 | -52.80092 | 2025-09-08 05:42:00 | NOAA-20 | SÃO FÉLIX DO XINGU | PARÁ | Brasil | 1507300 | 15 | 33 | nan | nan | nan | Amazônia | 2.4 |
| beb2eba6-03d7-390e-b463-c2327d26ecbe | -6.84137 | -52.85749 | 2025-09-08 05:42:00 | NOAA-20 | SÃO FÉLIX DO XINGU | PARÁ | Brasil | 1507300 | 15 | 33 | nan | nan | nan | Amazônia | 1.6 |
| 66c451ea-1257-3d4c-b05c-78cdf23af0cc | -9.38973 | -62.33708 | 2025-09-08 05:42:00 | NOAA-20 | MACHADINHO D'OESTE | RONDÔNIA | Brasil | 1100130 | 11 | 33 | nan | nan | nan | Amazônia | 1.0 |
| 7b3f3ae5-c2e5-3b5a-9842-c09e2c3642de | -9.90983 | -67.01526 | 2025-09-08 05:42:00 | NOAA-20 | ACRELÂNDIA | ACRE | Brasil | 1200013 | 12 | 33 | nan | nan | nan | Amazônia | 1.0 |
| ff8c85cf-d45f-31d9-b583-fdda1ae83d1c | -9.35367 | -65.4193 | 2025-09-08 05:42:00 | NOAA-20 | PORTO VELHO | RONDÔNIA | Brasil | 1100205 | 11 | 33 | nan | nan | nan | Amazônia | 0.7 |
| 1a7be367-99b5-3171-9dc1-c558cdca06ee | -6.83039 | -52.80678 | 2025-09-08 05:42:00 | NOAA-20 | SÃO FÉLIX DO XINGU | PARÁ | Brasil | 1507300 | 15 | 33 | nan | nan | nan | Amazônia | 3.1 |
| 6d4c7ba0-9514-34dc-b67c-2bbc9b8e10db | -7.39497 | -61.63281 | 2025-09-08 05:42:00 | NOAA-20 | MANICORÉ | AMAZONAS | Brasil | 1302702 | 13 | 33 | nan | nan | nan | Amazônia | 5.2 |
| 4df24cfc-ba75-3d99-9b9a-e90ababa30e0 | -9.19866 | -65.90945 | 2025-09-08 05:42:00 | NOAA-20 | LÁBREA | AMAZONAS | Brasil | 1302405 | 13 | 33 | nan | nan | nan | Amazônia | 1.0 |
| 4b6bf3a8-1988-3fcd-b511-471b02231d10 | -10.15593 | -61.14058 | 2025-09-08 05:42:00 | NOAA-20 | RONDOLÂNDIA | MATO GROSSO | Brasil | 5107578 | 51 | 33 | nan | nan | nan | Amazônia | 1.8 |
| 9f081c85-a2cf-316d-b14d-8a94e16a11e0 | -10.50695 | -57.79815 | 2025-09-08 05:42:00 | NOAA-20 | JUARA | MATO GROSSO | Brasil | 5105101 | 51 | 33 | nan | nan | nan | Amazônia | 1.3 |
| 6818e0d1-35cb-3849-a2f6-b1289ece2c96 | -10.5112 | -57.80492 | 2025-09-08 05:42:00 | NOAA-20 | JUARA | MATO GROSSO | Brasil | 5105101 | 51 | 33 | nan | nan | nan | Amazônia | 0.9 |
| 5803e709-52f9-3417-a8cf-0f28adadc880 | -9.94308 | -60.4985 | 2025-09-08 05:42:00 | NOAA-20 | ARIPUANÃ | MATO GROSSO | Brasil | 5101407 | 51 | 33 | nan | nan | nan | Amazônia | 0.8 |
| f79d5c53-9221-3d8d-91c4-54620f70584f | -9.47605 | -60.50182 | 2025-09-08 05:42:00 | NOAA-20 | ARIPUANÃ | MATO GROSSO | Brasil | 5101407 | 51 | 33 | nan | nan | nan | Amazônia | 1.5 |
| d1ec606f-a51d-3684-8668-237d898f1f0a | -6.94888 | -62.93624 | 2025-09-08 05:42:00 | NOAA-20 | HUMAITÁ | AMAZONAS | Brasil | 1301704 | 13 | 33 | nan | nan | nan | Amazônia | 2.0 |
| 1c2fde5a-dc80-30a3-8429-23898db523bd | -10.57681 | -61.25478 | 2025-09-08 05:42:00 | NOAA-20 | RONDOLÂNDIA | MATO GROSSO | Brasil | 5107578 | 51 | 33 | nan | nan | nan | Amazônia | 1.7 |
| db3a38f9-131d-39ca-b094-009d878b0a8a | -9.61015 | -65.18874 | 2025-09-08 05:42:00 | NOAA-20 | PORTO VELHO | RONDÔNIA | Brasil | 1100205 | 11 | 33 | nan | nan | nan | Amazônia | 0.7 |
| 4003e2a4-00dc-3190-acbc-fb200797fea2 | -9.11658 | -61.48787 | 2025-09-08 05:42:00 | NOAA-20 | COLNIZA | MATO GROSSO | Brasil | 5103254 | 51 | 33 | nan | nan | nan | Amazônia | 1.5 |
| 680a34eb-47b4-3ca8-8dd5-3d14a7739b16 | -6.96289 | -62.93836 | 2025-09-08 05:42:00 | NOAA-20 | HUMAITÁ | AMAZONAS | Brasil | 1301704 | 13 | 33 | nan | nan | nan | Amazônia | 1.2 |
| a5276d4b-14a4-3d11-aff2-f90946185cc7 | -10.41592 | -60.74703 | 2025-09-08 05:42:00 | NOAA-20 | RONDOLÂNDIA | MATO GROSSO | Brasil | 5107578 | 51 | 33 | nan | nan | nan | Amazônia | 1.7 |
| be4b766c-50fa-3e86-9833-9e4fc68d9587 | -6.54749 | -54.99489 | 2025-09-08 05:42:00 | NOAA-20 | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 2.1 |
| 4d958776-8ac2-3959-8ef7-3301c79bdfd6 | -9.88187 | -56.14493 | 2025-09-08 05:42:00 | NOAA-20 | ALTA FLORESTA | MATO GROSSO | Brasil | 5100250 | 51 | 33 | nan | nan | nan | Amazônia | 2.1 |
| 44b62c34-cdce-35bf-8324-dec50cae6417 | -9.24119 | -57.07067 | 2025-09-08 05:42:00 | NOAA-20 | PARANAÍTA | MATO GROSSO | Brasil | 5106299 | 51 | 33 | nan | nan | nan | Amazônia | 2.1 |
| 2a02a9ed-4b1c-3331-bdbd-dbde1b4ea62b | -9.88404 | -56.14605 | 2025-09-08 05:42:00 | NOAA-20 | ALTA FLORESTA | MATO GROSSO | Brasil | 5100250 | 51 | 33 | nan | nan | nan | Amazônia | 3.7 |
| 017a8464-077a-3355-91bc-2c55bb70e1fb | -7.11661 | -63.0712 | 2025-09-08 05:42:00 | NOAA-20 | HUMAITÁ | AMAZONAS | Brasil | 1301704 | 13 | 33 | nan | nan | nan | Amazônia | 2.1 |
| 421b83a1-9cc9-37b3-84e6-e2ec5d9625c6 | -9.20234 | -67.56149 | 2025-09-08 05:42:00 | NOAA-20 | BOCA DO ACRE | AMAZONAS | Brasil | 1300706 | 13 | 33 | nan | nan | nan | Amazônia | 1.2 |
| 052aba05-cd97-3c19-a1ad-0caa17d279a5 | -9.17458 | -59.36979 | 2025-09-08 05:42:00 | NOAA-20 | COLNIZA | MATO GROSSO | Brasil | 5103254 | 51 | 33 | nan | nan | nan | Amazônia | 3.8 |
| bd003316-e070-321a-98cc-c4764a66722b | -9.13361 | -65.95617 | 2025-09-08 05:42:00 | NOAA-20 | LÁBREA | AMAZONAS | Brasil | 1302405 | 13 | 33 | nan | nan | nan | Amazônia | 1.1 |
| 8124ecd4-55af-31e2-bdb4-00da04ce1702 | -9.6096 | -65.19228 | 2025-09-08 05:42:00 | NOAA-20 | PORTO VELHO | RONDÔNIA | Brasil | 1100205 | 11 | 33 | nan | nan | nan | Amazônia | 0.7 |
| bad62150-813c-39bf-8274-9a4adaa6a4b8 | -8.88736 | -64.21968 | 2025-09-08 05:42:00 | NOAA-20 | CANUTAMA | AMAZONAS | Brasil | 1300904 | 13 | 33 | nan | nan | nan | Amazônia | 7.1 |
| 64d70e81-994b-3eaa-ad22-d99cdbbd5834 | -7.47403 | -61.59311 | 2025-09-08 05:42:00 | NOAA-20 | MANICORÉ | AMAZONAS | Brasil | 1302702 | 13 | 33 | nan | nan | nan | Amazônia | 1.7 |
| b0d3edff-7d50-38d8-bcdb-7deb04d4af70 | -9.48239 | -60.48725 | 2025-09-08 05:42:00 | NOAA-20 | ARIPUANÃ | MATO GROSSO | Brasil | 5101407 | 51 | 33 | nan | nan | nan | Amazônia | 1.6 |
| 0f9bd54e-9954-3b43-80df-b43095e8a7d2 | -7.59748 | -61.59562 | 2025-09-08 05:42:00 | NOAA-20 | MANICORÉ | AMAZONAS | Brasil | 1302702 | 13 | 33 | nan | nan | nan | Amazônia | 0.8 |
| bbb3a7f3-ea4d-3479-a89c-8fa9610aecea | -9.47243 | -60.49743 | 2025-09-08 05:42:00 | NOAA-20 | ARIPUANÃ | MATO GROSSO | Brasil | 5101407 | 51 | 33 | nan | nan | nan | Amazônia | 1.2 |
| c39ffccd-2500-320b-bd07-e3111d47f11f | -9.16948 | -59.37368 | 2025-09-08 05:42:00 | NOAA-20 | COLNIZA | MATO GROSSO | Brasil | 5103254 | 51 | 33 | nan | nan | nan | Amazônia | 3.5 |
| f9a21885-584e-3053-ae3e-b98ac3374772 | -6.84875 | -52.85288 | 2025-09-08 05:42:00 | NOAA-20 | SÃO FÉLIX DO XINGU | PARÁ | Brasil | 1507300 | 15 | 33 | nan | nan | nan | Amazônia | 1.6 |
| 271eeca4-5bf4-3063-be7a-973751509ae0 | -10.56594 | -61.23539 | 2025-09-08 05:42:00 | NOAA-20 | RONDOLÂNDIA | MATO GROSSO | Brasil | 5107578 | 51 | 33 | nan | nan | nan | Amazônia | 3.2 |
| 7ef39586-08c4-3c8c-ad3e-26a844caaf3c | -8.08628 | -54.76322 | 2025-09-08 05:42:00 | NOAA-20 | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 2.8 |
| 8ac43435-c319-32c7-adac-f58d0c1282f2 | -10.87977 | -55.71939 | 2025-09-08 05:42:00 | NOAA-20 | NOVA CANAÃ DO NORTE | MATO GROSSO | Brasil | 5106216 | 51 | 33 | nan | nan | nan | Amazônia | 1.7 |
| cccd3555-8e94-362b-a5e3-a38b2ca33726 | -9.20583 | -65.90702 | 2025-09-08 05:42:00 | NOAA-20 | LÁBREA | AMAZONAS | Brasil | 1302405 | 13 | 33 | nan | nan | nan | Amazônia | 0.9 |
| a62681d7-7e06-37f9-8af6-cc3ff77e782e | -9.96299 | -59.59621 | 2025-09-08 05:42:00 | NOAA-20 | ARIPUANÃ | MATO GROSSO | Brasil | 5101407 | 51 | 33 | nan | nan | nan | Amazônia | 2.0 |
| 46736c45-aba3-381b-bb47-4395724c9f74 | -9.08656 | -64.01483 | 2025-09-08 05:42:00 | NOAA-20 | PORTO VELHO | RONDÔNIA | Brasil | 1100205 | 11 | 33 | nan | nan | nan | Amazônia | 0.8 |
| 45d56da2-b699-3e32-9218-0c1ab3094a18 | -10.05025 | -59.35952 | 2025-09-08 05:42:00 | NOAA-20 | ARIPUANÃ | MATO GROSSO | Brasil | 5101407 | 51 | 33 | nan | nan | nan | Amazônia | 3.0 |
| c60b184c-aaa2-3373-b427-10b1edfe693b | -9.12313 | -65.95806 | 2025-09-08 05:42:00 | NOAA-20 | LÁBREA | AMAZONAS | Brasil | 1302405 | 13 | 33 | nan | nan | nan | Amazônia | 1.2 |
| fb946fbc-ec3c-31b8-b4a6-c2cc1d68fd75 | -9.25739 | -67.60821 | 2025-09-08 05:42:00 | NOAA-20 | BOCA DO ACRE | AMAZONAS | Brasil | 1300706 | 13 | 33 | nan | nan | nan | Amazônia | 0.6 |
| 3edce088-f9d4-3737-af6b-e79b87f5dfda | -9.13416 | -65.95269 | 2025-09-08 05:42:00 | NOAA-20 | LÁBREA | AMAZONAS | Brasil | 1302405 | 13 | 33 | nan | nan | nan | Amazônia | 1.1 |
| 94075673-4f69-379c-b2f7-68805e1e99a3 | -10.505 | -57.8002 | 2025-09-08 05:42:00 | NOAA-20 | JUARA | MATO GROSSO | Brasil | 5105101 | 51 | 33 | nan | nan | nan | Amazônia | 1.2 |
| c83c2a13-d353-3ff3-855c-c2df97a57f25 | -12.1965 | -53.90657 | 2025-09-08 05:42:00 | NOAA-20 | NOVA UBIRATÃ | MATO GROSSO | Brasil | 5106240 | 51 | 33 | nan | nan | nan | Amazônia | 1.9 |
| 0e139740-c067-3aea-82f4-b3868cafd27e | -9.08049 | -65.42941 | 2025-09-08 05:42:00 | NOAA-20 | LÁBREA | AMAZONAS | Brasil | 1302405 | 13 | 33 | nan | nan | nan | Amazônia | 0.6 |
| 9054957d-b5c2-34cc-8e15-5d9cfdb2b199 | -10.15547 | -61.1438 | 2025-09-08 05:42:00 | NOAA-20 | RONDOLÂNDIA | MATO GROSSO | Brasil | 5107578 | 51 | 33 | nan | nan | nan | Amazônia | 1.8 |
| 21ffc6e8-679b-39df-b6b3-331189294a7d | -9.06984 | -60.487 | 2025-09-08 05:42:00 | NOAA-20 | COLNIZA | MATO GROSSO | Brasil | 5103254 | 51 | 33 | nan | nan | nan | Amazônia | 0.8 |
| 20f0a862-33df-3d4e-be40-aebc71526cb0 | -10.57938 | -61.256 | 2025-09-08 05:42:00 | NOAA-20 | RONDOLÂNDIA | MATO GROSSO | Brasil | 5107578 | 51 | 33 | nan | nan | nan | Amazônia | 1.7 |
| 040dbadf-86e2-3c5d-9b80-2d40d8d5bc36 | -10.27446 | -63.16887 | 2025-09-08 05:42:00 | NOAA-20 | CACAULÂNDIA | RONDÔNIA | Brasil | 1100601 | 11 | 33 | nan | nan | nan | Amazônia | 2.3 |
| 8c592e62-01ef-322e-88a2-ae35d5d9c35c | -9.48184 | -60.49103 | 2025-09-08 05:42:00 | NOAA-20 | ARIPUANÃ | MATO GROSSO | Brasil | 5101407 | 51 | 33 | nan | nan | nan | Amazônia | 1.6 |
| d39617c8-d1c7-3b28-95d9-afe56aee4f72 | -10.1737 | -61.13963 | 2025-09-08 05:42:00 | NOAA-20 | RONDOLÂNDIA | MATO GROSSO | Brasil | 5107578 | 51 | 33 | nan | nan | nan | Amazônia | 1.7 |
| 32c9c9ef-6a59-308a-bb17-dd9d1a69e230 | -9.23595 | -57.06997 | 2025-09-08 05:42:00 | NOAA-20 | PARANAÍTA | MATO GROSSO | Brasil | 5106299 | 51 | 33 | nan | nan | nan | Amazônia | 0.8 |
| a514324f-ec07-38b3-961b-c59345630346 | -10.15141 | -61.1434 | 2025-09-08 05:42:00 | NOAA-20 | RONDOLÂNDIA | MATO GROSSO | Brasil | 5107578 | 51 | 33 | nan | nan | nan | Amazônia | 1.8 |
| b03befab-ef90-3197-8713-5e0143b8b70d | -9.3559 | -65.42683 | 2025-09-08 05:42:00 | NOAA-20 | PORTO VELHO | RONDÔNIA | Brasil | 1100205 | 11 | 33 | nan | nan | nan | Amazônia | 1.2 |
| 26b44713-f888-3b9b-8f0f-619f9f3db7aa | -8.88396 | -64.21916 | 2025-09-08 05:42:00 | NOAA-20 | CANUTAMA | AMAZONAS | Brasil | 1300904 | 13 | 33 | nan | nan | nan | Amazônia | 7.1 |
| fd5d8f24-1be9-367f-8773-86aef189290b | -10.51007 | -57.80091 | 2025-09-08 05:42:00 | NOAA-20 | JUARA | MATO GROSSO | Brasil | 5105101 | 51 | 33 | nan | nan | nan | Amazônia | 1.2 |
| cdcc4ad6-e170-3576-aa28-342c400c7f51 | -9.62056 | -64.20829 | 2025-09-08 05:42:00 | NOAA-20 | PORTO VELHO | RONDÔNIA | Brasil | 1100205 | 11 | 33 | nan | nan | nan | Amazônia | 7.3 |
| e2598acb-75c1-38b9-bce9-5eb9b51cb02a | -10.08848 | -59.18388 | 2025-09-08 05:42:00 | NOAA-20 | ARIPUANÃ | MATO GROSSO | Brasil | 5101407 | 51 | 33 | nan | nan | nan | Amazônia | 4.5 |
| 67e14b3b-79b7-3255-958b-222301d7caa8 | -8.8834 | -64.22283 | 2025-09-08 05:42:00 | NOAA-20 | CANUTAMA | AMAZONAS | Brasil | 1300904 | 13 | 33 | nan | nan | nan | Amazônia | 2.3 |
| ae1faf2e-c24e-3e7d-a2f4-9605ffb2e395 | -6.82747 | -52.8087 | 2025-09-08 05:42:00 | NOAA-20 | SÃO FÉLIX DO XINGU | PARÁ | Brasil | 1507300 | 15 | 33 | nan | nan | nan | Amazônia | 2.4 |
| 0ea6a62e-ce79-3fbb-af00-5ede738a7f1a | -9.71296 | -62.39762 | 2025-09-08 05:42:00 | NOAA-20 | MACHADINHO D'OESTE | RONDÔNIA | Brasil | 1100130 | 11 | 33 | nan | nan | nan | Amazônia | 0.7 |


[Clique aqui para ver as próximas entradas](README92.md)
