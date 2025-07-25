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

## Dados Diários - Página 2

| ID | Latitude | Longitude | Data/Hora GMT | Satélite | Município | Estado | País | Município ID | Estado ID | País ID | Dias sem Chuva | Precipitação | Risco de Fogo | Bioma | FRP |
|----|----------|-----------|---------------|----------|-----------|--------|------|--------------|-----------|---------|----------------|--------------|----------------|-------|-----|
| 13183ae4-84fe-361f-b6e1-9c84a2334ba5 | -8.0886 | -43.1431 | 2025-07-25 00:40:00 | GOES-19 | CANTO DO BURITI | PIAUÍ | Brasil | 2202307 | 22 | 33 | nan | nan | nan | Caatinga | 206.6 |
| 8196a1e5-4549-3973-839a-f65a464c6801 | -7.8894 | -45.539 | 2025-07-25 00:40:00 | GOES-19 | TASSO FRAGOSO | MARANHÃO | Brasil | 2112001 | 21 | 33 | nan | nan | nan | Cerrado | 68.3 |
| 7cd02b8d-20c9-396a-a208-1bc472d4ff65 | -6.9422 | -44.5562 | 2025-07-25 00:40:00 | GOES-19 | SÃO DOMINGOS DO AZEITÃO | MARANHÃO | Brasil | 2110658 | 21 | 33 | nan | nan | nan | Cerrado | 49.5 |
| 1f84ee22-8129-3fd4-8b12-a0aa38dc51ae | -11.4584 | -45.1126 | 2025-07-25 00:40:00 | GOES-19 | RIACHÃO DAS NEVES | BAHIA | Brasil | 2926202 | 29 | 33 | nan | nan | nan | Cerrado | 144.1 |
| 4bc53c32-6596-3cc2-b019-aa40b7b03df2 | -7.2594 | -43.0881 | 2025-07-25 00:40:00 | GOES-19 | FLORIANO | PIAUÍ | Brasil | 2203909 | 22 | 33 | nan | nan | nan | Caatinga | 71.7 |
| 92ee472b-d930-382c-828d-9346fc5b2b61 | -13.7169 | -45.6833 | 2025-07-25 00:40:00 | GOES-19 | CORRENTINA | BAHIA | Brasil | 2909307 | 29 | 33 | nan | nan | nan | Cerrado | 51.7 |
| 7a792700-4d36-3aba-8244-0ffd0300318f | -6.961 | -44.5546 | 2025-07-25 00:40:00 | GOES-19 | SÃO DOMINGOS DO AZEITÃO | MARANHÃO | Brasil | 2110658 | 21 | 33 | nan | nan | nan | Cerrado | 70.6 |
| e70cd9e2-4dcb-3e61-9fc3-d2267e001891 | -11.4393 | -45.1154 | 2025-07-25 00:40:00 | GOES-19 | RIACHÃO DAS NEVES | BAHIA | Brasil | 2926202 | 29 | 33 | nan | nan | nan | Cerrado | 44.3 |
| c1707aaa-d0ea-36ab-a3b5-709c3b1ff448 | -7.2597 | -43.0645 | 2025-07-25 00:40:00 | GOES-19 | FLORIANO | PIAUÍ | Brasil | 2203909 | 22 | 33 | nan | nan | nan | Caatinga | 188.9 |
| 79598817-0049-3316-9cb1-f5243578323b | -8.0693 | -43.1687 | 2025-07-25 00:40:00 | GOES-19 | CANTO DO BURITI | PIAUÍ | Brasil | 2202307 | 22 | 33 | nan | nan | nan | Caatinga | 76.1 |
| 99db1bbd-9a24-31b9-8bcf-1a147205b9c8 | -21.17255 | -48.8038 | 2025-07-25 00:41:00 | TERRA_M-M | ARIRANHA | SÃO PAULO | Brasil | 3503703 | 35 | 33 | nan | nan | nan | Mata Atlântica | 16.4 |
| a5b36200-0c83-3479-92d4-7f0a303043f4 | -21.34838 | -48.67584 | 2025-07-25 00:41:00 | TERRA_M-M | FERNANDO PRESTES | SÃO PAULO | Brasil | 3515608 | 35 | 33 | nan | nan | nan | Cerrado | 7.0 |
| bcea07b6-5f2a-354c-9d4f-3c4120e2508e | -22.54321 | -47.1997 | 2025-07-25 00:41:00 | TERRA_M-M | ARTUR NOGUEIRA | SÃO PAULO | Brasil | 3503802 | 35 | 33 | nan | nan | nan | Cerrado | 13.0 |
| 5738548d-89a6-3e2e-b131-59f2f0888e4d | -21.17127 | -48.79419 | 2025-07-25 00:41:00 | TERRA_M-M | ARIRANHA | SÃO PAULO | Brasil | 3503703 | 35 | 33 | nan | nan | nan | Mata Atlântica | 10.6 |
| 0415dfd8-58ec-39bd-9644-ffd772fac882 | -23.25906 | -52.15808 | 2025-07-25 00:41:00 | TERRA_M-M | PRESIDENTE CASTELO BRANCO | PARANÁ | Brasil | 4120408 | 41 | 33 | nan | nan | nan | Mata Atlântica | 12.2 |
| 8112731e-f813-3888-9eec-ec24f3eed02a | -20.53195 | -46.11145 | 2025-07-25 00:41:00 | TERRA_M-M | PIUMHI | MINAS GERAIS | Brasil | 3151503 | 31 | 33 | nan | nan | nan | Cerrado | 6.8 |
| 9ad26b4e-0e2b-343a-bbf5-91c3042eb3a5 | -14.95444 | -46.98062 | 2025-07-25 00:43:00 | TERRA_M-M | VILA BOA | GOIÁS | Brasil | 5222203 | 52 | 33 | nan | nan | nan | Cerrado | 28.0 |
| 9b2d9cab-5498-3212-b089-807a2f70bb19 | -19.16583 | -46.59097 | 2025-07-25 00:43:00 | TERRA_M-M | SERRA DO SALITRE | MINAS GERAIS | Brasil | 3166808 | 31 | 33 | nan | nan | nan | Cerrado | 10.7 |
| 83f9636b-ebb9-3d4d-8b5f-c01b6f18e024 | -13.70896 | -45.67266 | 2025-07-25 00:43:00 | TERRA_M-M | CORRENTINA | BAHIA | Brasil | 2909307 | 29 | 33 | nan | nan | nan | Cerrado | 26.9 |
| fce44b15-67c1-3667-8228-95786b7997ee | -17.71008 | -44.31707 | 2025-07-25 00:43:00 | TERRA_M-M | LASSANCE | MINAS GERAIS | Brasil | 3138104 | 31 | 33 | nan | nan | nan | Cerrado | 20.3 |
| 65b95542-77b7-3090-b0e9-2bfaf32f8519 | -15.04931 | -47.68714 | 2025-07-25 00:43:00 | TERRA_M-M | PLANALTINA | GOIÁS | Brasil | 5217609 | 52 | 33 | nan | nan | nan | Cerrado | 12.3 |
| 4bae5c8a-e6df-3811-b1e8-6c91031e9897 | -20.66867 | -50.86645 | 2025-07-25 00:43:00 | TERRA_M-M | SUD MENNUCCI | SÃO PAULO | Brasil | 3552304 | 35 | 33 | nan | nan | nan | Mata Atlântica | 7.6 |
| edcf6585-e477-3dbc-b5ac-be6d4e65ae81 | -13.71301 | -45.69837 | 2025-07-25 00:43:00 | TERRA_M-M | CORRENTINA | BAHIA | Brasil | 2909307 | 29 | 33 | nan | nan | nan | Cerrado | 10.0 |
| 3473e279-bd69-3ab8-b067-1eb044203938 | -17.69716 | -44.30521 | 2025-07-25 00:43:00 | TERRA_M-M | FRANCISCO DUMONT | MINAS GERAIS | Brasil | 3126604 | 31 | 33 | nan | nan | nan | Cerrado | 11.7 |
| ee3f0df5-3f5e-3dc8-8a2f-194e39df5a86 | -14.94641 | -46.99152 | 2025-07-25 00:43:00 | TERRA_M-M | VILA BOA | GOIÁS | Brasil | 5222203 | 52 | 33 | nan | nan | nan | Cerrado | 32.6 |
| b9437688-f32e-363c-9496-533c7e3012a5 | -16.82536 | -47.60483 | 2025-07-25 00:43:00 | TERRA_M-M | CRISTALINA | GOIÁS | Brasil | 5206206 | 52 | 33 | nan | nan | nan | Cerrado | 10.9 |
| 54d93dda-5361-3607-a1d3-237d5e8af3fc | -13.71099 | -45.68554 | 2025-07-25 00:43:00 | TERRA_M-M | CORRENTINA | BAHIA | Brasil | 2909307 | 29 | 33 | nan | nan | nan | Cerrado | 39.2 |
| 40a23f51-a6ad-3ac2-81f7-1a0fc709f254 | -15.05074 | -47.69687 | 2025-07-25 00:43:00 | TERRA_M-M | PLANALTINA | GOIÁS | Brasil | 5217609 | 52 | 33 | nan | nan | nan | Cerrado | 6.5 |
| b58fc28d-b4f7-352b-9712-3c9705544a87 | -14.94489 | -46.98133 | 2025-07-25 00:43:00 | TERRA_M-M | VILA BOA | GOIÁS | Brasil | 5222203 | 52 | 33 | nan | nan | nan | Cerrado | 97.8 |
| 4afafedb-1f04-3eee-bd6e-de3c050943f1 | -16.61039 | -47.9683 | 2025-07-25 00:43:00 | TERRA_M-M | LUZIÂNIA | GOIÁS | Brasil | 5212501 | 52 | 33 | nan | nan | nan | Cerrado | 5.0 |
| 617e5bcf-ec84-3b20-a3c3-ed25ead02299 | -14.95588 | -46.99024 | 2025-07-25 00:43:00 | TERRA_M-M | VILA BOA | GOIÁS | Brasil | 5222203 | 52 | 33 | nan | nan | nan | Cerrado | 26.6 |
| 7fbbd2c8-fa01-325c-9e5f-f54cf98178d7 | -14.65527 | -46.82995 | 2025-07-25 00:43:00 | TERRA_M-M | FLORES DE GOIÁS | GOIÁS | Brasil | 5207907 | 52 | 33 | nan | nan | nan | Cerrado | 16.1 |
| 99e63997-2f5f-3561-8e51-be74618f925a | -16.81494 | -47.59669 | 2025-07-25 00:43:00 | TERRA_M-M | CRISTALINA | GOIÁS | Brasil | 5206206 | 52 | 33 | nan | nan | nan | Cerrado | 13.1 |
| 979b8a8f-8be2-3d33-9bd8-774f161f6765 | -17.70789 | -44.30336 | 2025-07-25 00:43:00 | TERRA_M-M | LASSANCE | MINAS GERAIS | Brasil | 3138104 | 31 | 33 | nan | nan | nan | Cerrado | 28.1 |
| cae70706-31ce-35a3-abf5-da707cce1230 | -13.64486 | -45.71547 | 2025-07-25 00:43:00 | TERRA_M-M | CORRENTINA | BAHIA | Brasil | 2909307 | 29 | 33 | nan | nan | nan | Cerrado | 31.6 |
| 17dbe5f0-ba84-3402-b6cb-d39fb1e132cc | -13.65047 | -46.8266 | 2025-07-25 00:43:00 | TERRA_M-M | NOVA ROMA | GOIÁS | Brasil | 5214903 | 52 | 33 | nan | nan | nan | Cerrado | 6.3 |
| 6a7b5861-1dd3-3aae-a056-a948db3267b5 | -13.72341 | -45.69663 | 2025-07-25 00:43:00 | TERRA_M-M | CORRENTINA | BAHIA | Brasil | 2909307 | 29 | 33 | nan | nan | nan | Cerrado | 9.4 |
| 39561804-8d78-39fc-bcf9-00a302231430 | -14.65687 | -46.84063 | 2025-07-25 00:43:00 | TERRA_M-M | FLORES DE GOIÁS | GOIÁS | Brasil | 5207907 | 52 | 33 | nan | nan | nan | Cerrado | 10.5 |
| 09cbbb36-5fe7-30e9-997d-6ccdff6fc6a5 | -16.82397 | -47.5952 | 2025-07-25 00:43:00 | TERRA_M-M | CRISTALINA | GOIÁS | Brasil | 5206206 | 52 | 33 | nan | nan | nan | Cerrado | 12.9 |
| c16b99e2-eb12-3016-9290-a181fbdf829f | -13.71937 | -45.67084 | 2025-07-25 00:43:00 | TERRA_M-M | CORRENTINA | BAHIA | Brasil | 2909307 | 29 | 33 | nan | nan | nan | Cerrado | 18.9 |
| 2e5f0e8d-37c5-370e-b275-97bb1f3c0e42 | -13.7214 | -45.68376 | 2025-07-25 00:43:00 | TERRA_M-M | CORRENTINA | BAHIA | Brasil | 2909307 | 29 | 33 | nan | nan | nan | Cerrado | 34.0 |
| 674833aa-a3cc-3a0d-a7b4-65a0eea30dd0 | -13.64883 | -46.81561 | 2025-07-25 00:43:00 | TERRA_M-M | SÃO DOMINGOS | GOIÁS | Brasil | 5219803 | 52 | 33 | nan | nan | nan | Cerrado | 12.5 |
| 4709d806-c3b0-3d60-914b-0a97b636c1df | -16.09237 | -45.17161 | 2025-07-25 00:43:00 | TERRA_M-M | PINTÓPOLIS | MINAS GERAIS | Brasil | 3150570 | 31 | 33 | nan | nan | nan | Cerrado | 10.3 |
| b4770440-c3f4-310c-90f2-bcd3a847fe73 | -16.81633 | -47.60633 | 2025-07-25 00:43:00 | TERRA_M-M | CRISTALINA | GOIÁS | Brasil | 5206206 | 52 | 33 | nan | nan | nan | Cerrado | 28.1 |
| 092d41c5-e721-3557-b826-9a2dec170b13 | -10.62627 | -44.76442 | 2025-07-25 00:45:00 | TERRA_M-M | SEBASTIÃO BARROS | PIAUÍ | Brasil | 2210623 | 22 | 33 | nan | nan | nan | Cerrado | 20.7 |
| 1d31c83b-ecd0-387f-a375-db6525ff4c7f | -12.7028 | -46.98484 | 2025-07-25 00:45:00 | TERRA_M-M | ARRAIAS | TOCANTINS | Brasil | 1702406 | 17 | 33 | nan | nan | nan | Cerrado | 7.1 |
| 406e7a82-3a9d-3688-8a52-31f92a388d48 | -13.21569 | -51.1123 | 2025-07-25 00:45:00 | TERRA_M-M | COCALINHO | MATO GROSSO | Brasil | 5103106 | 51 | 33 | nan | nan | nan | Cerrado | 6.9 |
| 58030aee-6ea9-36b1-a1a0-59b0568f051c | -10.61106 | -45.24966 | 2025-07-25 00:45:00 | TERRA_M-M | CRISTALÂNDIA DO PIAUÍ | PIAUÍ | Brasil | 2203008 | 22 | 33 | nan | nan | nan | Cerrado | 36.4 |
| b76de437-d8d6-3a91-93cc-52cdd417657b | -12.0451 | -45.43682 | 2025-07-25 00:45:00 | TERRA_M-M | BARREIRAS | BAHIA | Brasil | 2903201 | 29 | 33 | nan | nan | nan | Cerrado | 26.1 |
| 50b28d1e-4298-38f3-9560-b4d3321679f4 | -12.42694 | -45.37784 | 2025-07-25 00:45:00 | TERRA_M-M | SÃO DESIDÉRIO | BAHIA | Brasil | 2928901 | 29 | 33 | nan | nan | nan | Cerrado | 34.0 |
| aa413a2f-951b-3b8e-9695-5dbcaead7893 | -10.74565 | -48.18528 | 2025-07-25 00:45:00 | TERRA_M-M | MONTE DO CARMO | TOCANTINS | Brasil | 1713601 | 17 | 33 | nan | nan | nan | Cerrado | 26.6 |
| 0db61a0a-3ed9-392f-889e-8f0737dcc342 | -9.59132 | -46.32619 | 2025-07-25 00:45:00 | TERRA_M-M | ALTO PARNAÍBA | MARANHÃO | Brasil | 2100501 | 21 | 33 | nan | nan | nan | Cerrado | 12.2 |
| 7c0f7c83-f1c4-322e-b3e3-449c4c1401c4 | -13.0942 | -52.14108 | 2025-07-25 00:45:00 | TERRA_M-M | QUERÊNCIA | MATO GROSSO | Brasil | 5107065 | 51 | 33 | nan | nan | nan | Amazônia | 16.7 |
| 69a9c797-2416-3f5a-805b-1711d84c1ca3 | -11.95722 | -58.75489 | 2025-07-25 00:45:00 | TERRA_M-M | JUÍNA | MATO GROSSO | Brasil | 5105150 | 51 | 33 | nan | nan | nan | Cerrado | 39.3 |
| ab052bea-64c7-3214-8ee6-a14705f12851 | -11.94183 | -58.7569 | 2025-07-25 00:45:00 | TERRA_M-M | JUÍNA | MATO GROSSO | Brasil | 5105150 | 51 | 33 | nan | nan | nan | Cerrado | 175.0 |
| 78556bff-f25f-3c27-a348-5dc10d34bda8 | -10.00555 | -48.12547 | 2025-07-25 00:45:00 | TERRA_M-M | APARECIDA DO RIO NEGRO | TOCANTINS | Brasil | 1701101 | 17 | 33 | nan | nan | nan | Cerrado | 8.4 |
| eb27b0a3-8377-3536-ac1c-cc0b25d9a2ea | -9.85669 | -44.71298 | 2025-07-25 00:45:00 | TERRA_M-M | RIACHO FRIO | PIAUÍ | Brasil | 2208858 | 22 | 33 | nan | nan | nan | Cerrado | 20.2 |
| 32cea1e3-42e0-394e-9e36-bc98b07b7881 | -11.46584 | -45.1184 | 2025-07-25 00:45:00 | TERRA_M-M | RIACHÃO DAS NEVES | BAHIA | Brasil | 2926202 | 29 | 33 | nan | nan | nan | Cerrado | 58.7 |
| 71b7b5d1-6da4-3443-85bf-e01762abc65b | -10.6407 | -44.77905 | 2025-07-25 00:45:00 | TERRA_M-M | SEBASTIÃO BARROS | PIAUÍ | Brasil | 2210623 | 22 | 33 | nan | nan | nan | Cerrado | 35.1 |
| 7370ad92-723c-3903-91fa-ca132ed87a8e | -11.46815 | -45.13332 | 2025-07-25 00:45:00 | TERRA_M-M | RIACHÃO DAS NEVES | BAHIA | Brasil | 2926202 | 29 | 33 | nan | nan | nan | Cerrado | 13.2 |
| a1d2b750-688c-3b15-8d18-6ad8160b28e4 | -12.25499 | -44.78794 | 2025-07-25 00:45:00 | TERRA_M-M | CATOLÂNDIA | BAHIA | Brasil | 2907400 | 29 | 33 | nan | nan | nan | Cerrado | 18.6 |
| a0b28862-7fd7-398d-b645-52e56d88d5ae | -13.09556 | -52.15155 | 2025-07-25 00:45:00 | TERRA_M-M | QUERÊNCIA | MATO GROSSO | Brasil | 5107065 | 51 | 33 | nan | nan | nan | Amazônia | 6.7 |
| 9c8bbc9f-7f99-319e-bded-b316eed3679a | -11.77847 | -47.32027 | 2025-07-25 00:45:00 | TERRA_M-M | ALMAS | TOCANTINS | Brasil | 1700400 | 17 | 33 | nan | nan | nan | Cerrado | 11.2 |
| 8f89b8af-f676-304b-98c2-e2efe2e0a6ee | -10.60864 | -45.2343 | 2025-07-25 00:45:00 | TERRA_M-M | CRISTALÂNDIA DO PIAUÍ | PIAUÍ | Brasil | 2203008 | 22 | 33 | nan | nan | nan | Cerrado | 47.6 |
| 122ffc6e-960f-3d9a-a73d-0a7afa02673f | -11.78007 | -47.33102 | 2025-07-25 00:45:00 | TERRA_M-M | ALMAS | TOCANTINS | Brasil | 1700400 | 17 | 33 | nan | nan | nan | Cerrado | 17.7 |
| 084cfcec-6b0b-356a-a3e4-99d91b69eeb1 | -11.94523 | -58.78814 | 2025-07-25 00:45:00 | TERRA_M-M | JUÍNA | MATO GROSSO | Brasil | 5105150 | 51 | 33 | nan | nan | nan | Cerrado | 60.7 |
| 91880a77-658b-3004-817e-c0310402e7b5 | -11.44326 | -45.12234 | 2025-07-25 00:45:00 | TERRA_M-M | RIACHÃO DAS NEVES | BAHIA | Brasil | 2926202 | 29 | 33 | nan | nan | nan | Cerrado | 11.4 |
| d1b8026a-3c6c-37ba-87ec-b0129c0a9f0e | -11.45691 | -45.13551 | 2025-07-25 00:45:00 | TERRA_M-M | RIACHÃO DAS NEVES | BAHIA | Brasil | 2926202 | 29 | 33 | nan | nan | nan | Cerrado | 25.6 |
| 638f0fcb-946f-33b3-98c1-f8f79011709e | -9.59334 | -46.33948 | 2025-07-25 00:45:00 | TERRA_M-M | ALTO PARNAÍBA | MARANHÃO | Brasil | 2100501 | 21 | 33 | nan | nan | nan | Cerrado | 14.7 |
| a30530ef-1e15-30ac-9b50-ae7ff1d7da74 | -9.84946 | -44.70162 | 2025-07-25 00:45:00 | TERRA_M-M | RIACHO FRIO | PIAUÍ | Brasil | 2208858 | 22 | 33 | nan | nan | nan | Cerrado | 22.6 |
| 06ab017d-d2e1-35f9-8020-cb89841971e4 | -9.85388 | -44.69557 | 2025-07-25 00:45:00 | TERRA_M-M | RIACHO FRIO | PIAUÍ | Brasil | 2208858 | 22 | 33 | nan | nan | nan | Cerrado | 14.6 |
| 9953c612-7225-3a4b-80f4-65fcd3e0d2b2 | -10.44536 | -49.05264 | 2025-07-25 00:45:00 | TERRA_M-M | NOVA ROSALÂNDIA | TOCANTINS | Brasil | 1715002 | 17 | 33 | nan | nan | nan | Cerrado | 36.8 |
| 2e824f29-77d6-3a8b-844c-81bb3a14266f | -13.20661 | -51.1136 | 2025-07-25 00:45:00 | TERRA_M-M | COCALINHO | MATO GROSSO | Brasil | 5103106 | 51 | 33 | nan | nan | nan | Cerrado | 5.0 |
| fe63bf47-7e91-31db-97c8-ea20647d3d7e | -10.63807 | -44.76246 | 2025-07-25 00:45:00 | TERRA_M-M | SEBASTIÃO BARROS | PIAUÍ | Brasil | 2210623 | 22 | 33 | nan | nan | nan | Cerrado | 173.5 |
| 078a16fc-74b7-3d51-98ae-498a074f0806 | -11.94533 | -58.76178 | 2025-07-25 00:45:00 | TERRA_M-M | JUÍNA | MATO GROSSO | Brasil | 5105150 | 51 | 33 | nan | nan | nan | Cerrado | 191.4 |
| fe7d096e-55fc-31d7-8ca9-277c5696a420 | -10.42304 | -47.22842 | 2025-07-25 00:45:00 | TERRA_M-M | PONTE ALTA DO TOCANTINS | TOCANTINS | Brasil | 1717909 | 17 | 33 | nan | nan | nan | Cerrado | 6.9 |
| 9507cfdb-988d-3ec3-a771-fbc036d1e642 | -11.45456 | -45.12043 | 2025-07-25 00:45:00 | TERRA_M-M | RIACHÃO DAS NEVES | BAHIA | Brasil | 2926202 | 29 | 33 | nan | nan | nan | Cerrado | 54.5 |
| 8e32435d-612c-3f95-9c3e-5498828019e9 | -12.25229 | -44.78277 | 2025-07-25 00:45:00 | TERRA_M-M | CATOLÂNDIA | BAHIA | Brasil | 2907400 | 29 | 33 | nan | nan | nan | Cerrado | 21.5 |
| ffb76e34-a051-3caa-a40c-9dc35a24dff7 | -12.42911 | -45.39195 | 2025-07-25 00:45:00 | TERRA_M-M | SÃO DESIDÉRIO | BAHIA | Brasil | 2928901 | 29 | 33 | nan | nan | nan | Cerrado | 13.9 |
| 4c572e3f-1f2a-3f66-b7d8-1ce5fb5dc224 | -5.97235 | -44.14354 | 2025-07-25 00:48:00 | TERRA_M-M | COLINAS | MARANHÃO | Brasil | 2103505 | 21 | 33 | nan | nan | nan | Cerrado | 15.2 |
| 01476c1a-5862-3b3f-9aee-4d5b72d56f99 | -9.73363 | -48.02598 | 2025-07-25 00:48:00 | TERRA_M-M | TOCANTÍNIA | TOCANTINS | Brasil | 1721109 | 17 | 33 | nan | nan | nan | Cerrado | 7.5 |
| 813083f4-829b-3e0c-a946-ee454a6a1041 | -7.24415 | -43.07481 | 2025-07-25 00:48:00 | TERRA_M-M | FLORIANO | PIAUÍ | Brasil | 2203909 | 22 | 33 | nan | nan | nan | Caatinga | 22.7 |
| a609cbc4-680d-3c36-af70-8f8a77de6876 | -7.90401 | -44.08577 | 2025-07-25 00:48:00 | TERRA_M-M | SEBASTIÃO LEAL | PIAUÍ | Brasil | 2210631 | 22 | 33 | nan | nan | nan | Cerrado | 36.3 |
| 712dce98-c967-3926-ad28-4dba752ef9b8 | -7.89463 | -45.54518 | 2025-07-25 00:48:00 | TERRA_M-M | TASSO FRAGOSO | MARANHÃO | Brasil | 2112001 | 21 | 33 | nan | nan | nan | Cerrado | 35.0 |
| 130e9295-7a30-3060-95e0-8da9414b65a7 | -3.75503 | -52.66426 | 2025-07-25 00:48:00 | TERRA_M-M | BRASIL NOVO | PARÁ | Brasil | 1501725 | 15 | 33 | nan | nan | nan | Amazônia | 5.8 |
| b8001134-c1d7-37c1-9fb7-af2890037c72 | -8.06696 | -43.14628 | 2025-07-25 00:48:00 | TERRA_M-M | CANTO DO BURITI | PIAUÍ | Brasil | 2202307 | 22 | 33 | nan | nan | nan | Caatinga | 58.2 |
| 5f0a93ae-89bf-3b87-8ece-1a9b6078e36b | -7.11507 | -47.83968 | 2025-07-25 00:48:00 | TERRA_M-M | BABAÇULÂNDIA | TOCANTINS | Brasil | 1703008 | 17 | 33 | nan | nan | nan | Cerrado | 47.0 |
| 570f3d04-e468-316c-ab0e-8d28b6a91bc0 | -6.956 | -44.57747 | 2025-07-25 00:48:00 | TERRA_M-M | SÃO DOMINGOS DO AZEITÃO | MARANHÃO | Brasil | 2110658 | 21 | 33 | nan | nan | nan | Cerrado | 35.6 |
| 61eda6e4-7fa6-335b-9bab-4cefbb646c64 | -7.48704 | -49.23927 | 2025-07-25 00:48:00 | TERRA_M-M | PAU D'ARCO | TOCANTINS | Brasil | 1716307 | 17 | 33 | nan | nan | nan | Amazônia | 6.9 |
| dbdda99b-274c-3405-a5e8-257a2ae3c8f2 | -8.9259 | -47.34711 | 2025-07-25 00:48:00 | TERRA_M-M | CENTENÁRIO | TOCANTINS | Brasil | 1704105 | 17 | 33 | nan | nan | nan | Cerrado | 10.7 |
| 228647bf-720d-3176-88ed-3c965b8ebacb | -8.07047 | -49.71934 | 2025-07-25 00:48:00 | TERRA_M-M | CONCEIÇÃO DO ARAGUAIA | PARÁ | Brasil | 1502707 | 15 | 33 | nan | nan | nan | Amazônia | 26.6 |
| d999cbb3-1760-3e68-8b75-35b193dc0998 | -9.13235 | -49.66776 | 2025-07-25 00:48:00 | TERRA_M-M | ARAGUACEMA | TOCANTINS | Brasil | 1701903 | 17 | 33 | nan | nan | nan | Cerrado | 7.1 |
| e4a484db-683f-3179-9563-a89cb0dc791f | -7.85482 | -48.21319 | 2025-07-25 00:48:00 | TERRA_M-M | PALMEIRANTE | TOCANTINS | Brasil | 1715705 | 17 | 33 | nan | nan | nan | Cerrado | 10.6 |
| 037b332e-d8ac-398d-b16d-4b5d6d0d420b | -8.09913 | -43.16653 | 2025-07-25 00:48:00 | TERRA_M-M | CANTO DO BURITI | PIAUÍ | Brasil | 2202307 | 22 | 33 | nan | nan | nan | Caatinga | 67.6 |
| 49f7a2cd-2f88-3c3f-9db0-821250927dc3 | -6.94007 | -44.55949 | 2025-07-25 00:48:00 | TERRA_M-M | SÃO DOMINGOS DO AZEITÃO | MARANHÃO | Brasil | 2110658 | 21 | 33 | nan | nan | nan | Cerrado | 13.0 |
| f8bb630a-bb23-3d1d-a979-a0f11c972b88 | -4.35001 | -47.6851 | 2025-07-25 00:48:00 | TERRA_M-M | DOM ELISEU | PARÁ | Brasil | 1502939 | 15 | 33 | nan | nan | nan | Amazônia | 31.3 |
| e09e5b01-9064-331f-85cd-ee85da1a99d4 | -8.51091 | -43.3159 | 2025-07-25 00:48:00 | TERRA_M-M | CANTO DO BURITI | PIAUÍ | Brasil | 2202307 | 22 | 33 | nan | nan | nan | Caatinga | 98.8 |
| f2b00d3b-0779-3569-bcc7-bd281f9c3c52 | -2.9095 | -48.25304 | 2025-07-25 00:48:00 | TERRA_M-M | TOMÉ-AÇU | PARÁ | Brasil | 1508001 | 15 | 33 | nan | nan | nan | Amazônia | 53.4 |
| 6c9f9027-9295-361e-9df8-abba2d953a04 | -7.91717 | -44.09932 | 2025-07-25 00:48:00 | TERRA_M-M | SEBASTIÃO LEAL | PIAUÍ | Brasil | 2210631 | 22 | 33 | nan | nan | nan | Cerrado | 71.4 |
| 4cef035b-4c54-3b7f-be4d-63008308a760 | -2.99086 | -49.32053 | 2025-07-25 00:48:00 | TERRA_M-M | MOJU | PARÁ | Brasil | 1504703 | 15 | 33 | nan | nan | nan | Amazônia | 10.9 |


[Clique aqui para ver as próximas entradas](README3.md)
