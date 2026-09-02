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

## Dados Diários - Página 79

| ID | Latitude | Longitude | Data/Hora GMT | Satélite | Município | Estado | País | Município ID | Estado ID | País ID | Dias sem Chuva | Precipitação | Risco de Fogo | Bioma | FRP |
|----|----------|-----------|---------------|----------|-----------|--------|------|--------------|-----------|---------|----------------|--------------|----------------|-------|-----|
| 1ae78722-b420-30ca-94bb-983b488bc65b | -7.3688 | -45.0432 | 2026-09-02 14:30:00 | GOES-19 | SÃO FÉLIX DE BALSAS | MARANHÃO | Brasil | 2110807 | 21 | 33 | nan | nan | nan | Cerrado | 51.7 |
| c210a368-fc41-35f8-83c8-77a6dbc8f105 | -10.1008 | -46.7195 | 2026-09-02 14:30:00 | GOES-19 | SÃO FÉLIX DO TOCANTINS | TOCANTINS | Brasil | 1720150 | 17 | 33 | nan | nan | nan | Cerrado | 115.9 |
| d8fc47b1-ae6e-3635-8ca2-77df731a0823 | -6.8018 | -59.4201 | 2026-09-02 14:30:00 | GOES-19 | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 50.4 |
| 365fef42-17c6-3cbb-a811-5f078940c6c8 | -10.7009 | -47.1835 | 2026-09-02 14:30:00 | GOES-19 | PONTE ALTA DO TOCANTINS | TOCANTINS | Brasil | 1717909 | 17 | 33 | nan | nan | nan | Cerrado | 73.2 |
| d74d463d-b91a-3435-8398-d3e8c1617ae7 | -3.7533 | -59.3231 | 2026-09-02 14:30:00 | GOES-19 | AUTAZES | AMAZONAS | Brasil | 1300300 | 13 | 33 | nan | nan | nan | Amazônia | 58.4 |
| 0639199d-edce-33d5-81e2-29ea15011c4d | -8.9111 | -62.353 | 2026-09-02 14:30:00 | GOES-19 | CUJUBIM | RONDÔNIA | Brasil | 1100940 | 11 | 33 | nan | nan | nan | Amazônia | 53.2 |
| f806110d-73fd-351b-95f7-9b6102bfbada | -12.0933 | -47.1138 | 2026-09-02 14:30:00 | GOES-19 | CONCEIÇÃO DO TOCANTINS | TOCANTINS | Brasil | 1705607 | 17 | 33 | nan | nan | nan | Cerrado | 117.5 |
| 26d00aff-dd6b-3f8f-8818-0f15299900f8 | -10.3004 | -50.0445 | 2026-09-02 14:30:00 | GOES-19 | PIUM | TOCANTINS | Brasil | 1717503 | 17 | 33 | nan | nan | nan | Cerrado | 159.7 |
| 5cc94d8e-a412-3777-b347-c5a1c78a9b04 | -6.6883 | -59.9436 | 2026-09-02 14:30:00 | GOES-19 | NOVO ARIPUANÃ | AMAZONAS | Brasil | 1303304 | 13 | 33 | nan | nan | nan | Amazônia | 49.4 |
| fd99a9ac-54d7-3255-a10f-0e5c188cf5cf | -10.7242 | -50.8534 | 2026-09-02 14:30:00 | GOES-19 | LUCIARA | MATO GROSSO | Brasil | 5105309 | 51 | 33 | nan | nan | nan | Cerrado | 80.5 |
| 980ad97d-df58-35a1-977e-cc23043d79b5 | -11.0623 | -47.1609 | 2026-09-02 14:30:00 | GOES-19 | ALMAS | TOCANTINS | Brasil | 1700400 | 17 | 33 | nan | nan | nan | Cerrado | 42.3 |
| d7402854-6f6a-3a75-9125-281209b28bd1 | -5.9635 | -57.6899 | 2026-09-02 14:30:00 | GOES-19 | JACAREACANGA | PARÁ | Brasil | 1503754 | 15 | 33 | nan | nan | nan | Amazônia | 60.0 |
| e2c0e005-e4d1-37fc-b1ad-abf0081e1ac8 | -9.4159 | -45.6271 | 2026-09-02 14:30:00 | GOES-19 | SANTA FILOMENA | PIAUÍ | Brasil | 2209203 | 22 | 33 | nan | nan | nan | Cerrado | 54.3 |
| 3491d8d1-0e07-3a48-9f96-2de597f29e39 | -12.3622 | -48.1681 | 2026-09-02 14:30:00 | GOES-19 | PARANÃ | TOCANTINS | Brasil | 1716208 | 17 | 33 | nan | nan | nan | Cerrado | 171.4 |
| 1fbcbb36-506c-3fb7-b8a9-bc80b447120b | -6.6541 | -59.4452 | 2026-09-02 14:30:00 | GOES-19 | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 83.5 |
| 2117f02a-5ca7-3c43-b41a-9d088ac65436 | -11.3579 | -45.4027 | 2026-09-02 14:30:00 | GOES-19 | FORMOSA DO RIO PRETO | BAHIA | Brasil | 2911105 | 29 | 33 | nan | nan | nan | Cerrado | 578.2 |
| ff004aff-dab2-3a84-af43-46a2b1d968e5 | -7.2005 | -60.6897 | 2026-09-02 14:30:00 | GOES-19 | NOVO ARIPUANÃ | AMAZONAS | Brasil | 1303304 | 13 | 33 | nan | nan | nan | Amazônia | 87.2 |
| ebcd1628-0c6c-38e8-9b34-c66ad9a0f6f5 | -11.1307 | -51.5728 | 2026-09-02 14:30:00 | GOES-19 | CANABRAVA DO NORTE | MATO GROSSO | Brasil | 5102694 | 51 | 33 | nan | nan | nan | Cerrado | 89.4 |
| cc409ba5-0bd3-39a5-a157-ebb50c73730c | -11.3771 | -45.4 | 2026-09-02 14:30:00 | GOES-19 | FORMOSA DO RIO PRETO | BAHIA | Brasil | 2911105 | 29 | 33 | nan | nan | nan | Cerrado | 463.8 |
| ff2d0e84-70d0-39e1-9271-2c9173ee5dc0 | -17.0878 | -56.8534 | 2026-09-02 14:30:00 | GOES-19 | POCONÉ | MATO GROSSO | Brasil | 5106505 | 51 | 33 | nan | nan | nan | Pantanal | 188.4 |
| 1cc4fbd8-2610-3ac8-98fd-67c9acb17b83 | -5.6016 | -60.211 | 2026-09-02 14:30:00 | GOES-19 | NOVO ARIPUANÃ | AMAZONAS | Brasil | 1303304 | 13 | 33 | nan | nan | nan | Amazônia | 118.1 |
| 34de0545-2d43-384c-9546-3d2a1795c338 | -12.3626 | -48.1459 | 2026-09-02 14:30:00 | GOES-19 | PARANÃ | TOCANTINS | Brasil | 1716208 | 17 | 33 | nan | nan | nan | Cerrado | 130.3 |
| 4807cc3e-478b-35d1-ba72-9bf7257b0b03 | -12.0936 | -47.0913 | 2026-09-02 14:30:00 | GOES-19 | CONCEIÇÃO DO TOCANTINS | TOCANTINS | Brasil | 1705607 | 17 | 33 | nan | nan | nan | Cerrado | 134.3 |
| 01060a1d-0fa6-3dcc-bda5-c3abf0d9ccdd | -8.7615 | -62.5679 | 2026-09-02 14:30:00 | GOES-19 | CUJUBIM | RONDÔNIA | Brasil | 1100940 | 11 | 33 | nan | nan | nan | Amazônia | 74.0 |
| e361dd29-c91d-3f27-a820-92782e94c2c5 | -6.7832 | -59.4401 | 2026-09-02 14:30:00 | GOES-19 | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 61.3 |
| ac08725b-094d-3d6e-b69a-12329b203a71 | -10.7428 | -50.8727 | 2026-09-02 14:30:00 | GOES-19 | LUCIARA | MATO GROSSO | Brasil | 5105309 | 51 | 33 | nan | nan | nan | Cerrado | 76.6 |
| fa3085d8-3efb-3660-9c58-7556081b9899 | -11.0563 | -51.4751 | 2026-09-02 14:30:00 | GOES-19 | CANABRAVA DO NORTE | MATO GROSSO | Brasil | 5102694 | 51 | 33 | nan | nan | nan | Cerrado | 94.3 |
| d17fe325-082c-31c3-98cc-77665b3f153b | -11.6627 | -50.1739 | 2026-09-02 14:30:00 | GOES-19 | FORMOSO DO ARAGUAIA | TOCANTINS | Brasil | 1708205 | 17 | 33 | nan | nan | nan | Cerrado | 81.8 |
| 4e7a03fa-15d6-3355-af86-7e1c13dce1a6 | -6.7647 | -59.4601 | 2026-09-02 14:30:00 | GOES-19 | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 51.8 |
| 33011ac3-ae82-3dd4-84e1-d4ae4596d420 | -7.3486 | -60.6074 | 2026-09-02 14:30:00 | GOES-19 | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 83.7 |
| 205f7d7c-0b2a-37cf-9897-71470f7decd4 | -10.7641 | -50.7005 | 2026-09-02 14:30:00 | GOES-19 | LUCIARA | MATO GROSSO | Brasil | 5105309 | 51 | 33 | nan | nan | nan | Cerrado | 79.5 |
| fd837d7a-f985-3225-81d1-f31fb0cc2365 | -10.3196 | -50.0211 | 2026-09-02 14:30:00 | GOES-19 | PIUM | TOCANTINS | Brasil | 1717503 | 17 | 33 | nan | nan | nan | Cerrado | 154.3 |
| a1f000f7-25fa-33c2-9930-5e6821b23438 | -10.1538 | -45.6982 | 2026-09-02 14:30:00 | GOES-19 | BARREIRAS DO PIAUÍ | PIAUÍ | Brasil | 2201309 | 22 | 33 | nan | nan | nan | Cerrado | 64.8 |
| 1940b999-ea87-3a4d-973e-fdf66b003945 | -12.1457 | -44.196 | 2026-09-02 14:30:00 | GOES-19 | CRISTÓPOLIS | BAHIA | Brasil | 2909703 | 29 | 33 | nan | nan | nan | Cerrado | 103.1 |
| 5b5aca67-9b5a-3c31-baab-f9d9be7a0e90 | -6.6764 | -58.7686 | 2026-09-02 14:30:00 | GOES-19 | MAUÉS | AMAZONAS | Brasil | 1302900 | 13 | 33 | nan | nan | nan | Amazônia | 90.3 |
| 8bf5f862-b232-3bfe-821c-96a558e3be78 | -10.7199 | -47.1812 | 2026-09-02 14:30:00 | GOES-19 | PONTE ALTA DO TOCANTINS | TOCANTINS | Brasil | 1717909 | 17 | 33 | nan | nan | nan | Cerrado | 78.7 |
| 29a13269-db72-34a8-83e3-8cbcf13d60de | -7.3117 | -60.6089 | 2026-09-02 14:30:00 | GOES-19 | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 60.3 |
| b6232451-1a5a-3855-8618-407cdb69c29d | -1.599 | -47.7458 | 2026-09-02 14:30:00 | GOES-19 | SÃO MIGUEL DO GUAMÁ | PARÁ | Brasil | 1507607 | 15 | 33 | nan | nan | nan | Amazônia | 71.8 |
| 9e7fc744-01d2-31c2-845d-71ad15021e84 | -10.7158 | -46.2169 | 2026-09-02 14:30:00 | GOES-19 | MATEIROS | TOCANTINS | Brasil | 1712702 | 17 | 33 | nan | nan | nan | Cerrado | 83.0 |
| ba3dbae5-84bd-3896-a19d-748e17b88b10 | -3.3688 | -59.3887 | 2026-09-02 14:30:00 | GOES-19 | CAREIRO DA VÁRZEA | AMAZONAS | Brasil | 1301159 | 13 | 33 | nan | nan | nan | Amazônia | 55.3 |
| e29af70b-e492-3ab2-836e-3b4a1ee34a81 | -12.1704 | -47.0806 | 2026-09-02 14:30:00 | GOES-19 | TAIPAS DO TOCANTINS | TOCANTINS | Brasil | 1720937 | 17 | 33 | nan | nan | nan | Cerrado | 117.1 |
| 1d2a667e-4847-3556-a45f-cbcf36719ff9 | -7.0057 | -59.2575 | 2026-09-02 14:30:00 | GOES-19 | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 58.6 |
| 7323e2e8-4721-3596-bc78-6532742f8f68 | -12.0741 | -47.1164 | 2026-09-02 14:30:00 | GOES-19 | CONCEIÇÃO DO TOCANTINS | TOCANTINS | Brasil | 1705607 | 17 | 33 | nan | nan | nan | Cerrado | 230.2 |
| bcf22319-3a9e-3858-a663-3aa870aecdea | -11.1304 | -51.5939 | 2026-09-02 14:30:00 | GOES-19 | CANABRAVA DO NORTE | MATO GROSSO | Brasil | 5102694 | 51 | 33 | nan | nan | nan | Cerrado | 80.7 |
| 359a616e-f0a5-3e10-a2b6-ca60056910a9 | -13.5531 | -59.7574 | 2026-09-02 14:30:00 | GOES-19 | COMODORO | MATO GROSSO | Brasil | 5103304 | 51 | 33 | nan | nan | nan | Amazônia | 58.3 |
| 34ca9843-6f16-3ed7-b4a3-b052dd708e6a | -10.301 | -50.0016 | 2026-09-02 14:30:00 | GOES-19 | PIUM | TOCANTINS | Brasil | 1717503 | 17 | 33 | nan | nan | nan | Cerrado | 90.0 |
| 37b1460f-a154-39a0-9c63-9ba6ec991d2d | -7.2006 | -60.6706 | 2026-09-02 14:30:00 | GOES-19 | NOVO ARIPUANÃ | AMAZONAS | Brasil | 1303304 | 13 | 33 | nan | nan | nan | Amazônia | 92.1 |
| 5cb2e169-a013-318f-a32d-81876aae9413 | -11.1315 | -51.5094 | 2026-09-02 14:30:00 | GOES-19 | CANABRAVA DO NORTE | MATO GROSSO | Brasil | 5102694 | 51 | 33 | nan | nan | nan | Cerrado | 77.9 |
| e66eaefc-43f8-3acf-b5f0-1b07eb3999e2 | -1.5991 | -47.7241 | 2026-09-02 14:30:00 | GOES-19 | SÃO MIGUEL DO GUAMÁ | PARÁ | Brasil | 1507607 | 15 | 33 | nan | nan | nan | Amazônia | 68.9 |
| 3674c347-ff7a-320a-994a-22a7210ccbaa | -7.3487 | -60.5883 | 2026-09-02 14:30:00 | GOES-19 | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 73.4 |
| 2ead5c79-31df-366d-a994-ae138e9c4683 | -13.5533 | -59.7377 | 2026-09-02 14:30:00 | GOES-19 | COMODORO | MATO GROSSO | Brasil | 5103304 | 51 | 33 | nan | nan | nan | Amazônia | 57.6 |
| 65cad7a5-868b-340c-a314-795661a72f8d | -12.1312 | -47.1309 | 2026-09-02 14:30:00 | GOES-19 | CONCEIÇÃO DO TOCANTINS | TOCANTINS | Brasil | 1705607 | 17 | 33 | nan | nan | nan | Cerrado | 130.3 |
| 39bb48d8-8ddc-3e5e-b306-4ba67635de9c | -10.3007 | -50.023 | 2026-09-02 14:30:00 | GOES-19 | PIUM | TOCANTINS | Brasil | 1717503 | 17 | 33 | nan | nan | nan | Cerrado | 113.6 |
| 76ec41b3-96c5-3ed7-82ab-454bb34a4f6d | -11.3388 | -45.4054 | 2026-09-02 14:30:00 | GOES-19 | FORMOSA DO RIO PRETO | BAHIA | Brasil | 2911105 | 29 | 33 | nan | nan | nan | Cerrado | 167.1 |
| 56754eac-d56d-367e-b25d-a7665bf73d93 | -6.6765 | -58.7492 | 2026-09-02 14:30:00 | GOES-19 | MAUÉS | AMAZONAS | Brasil | 1302900 | 13 | 33 | nan | nan | nan | Amazônia | 76.8 |
| dbfe8daa-b4cd-3d7e-834f-af278053d741 | -5.5832 | -60.2116 | 2026-09-02 14:30:00 | GOES-19 | NOVO ARIPUANÃ | AMAZONAS | Brasil | 1303304 | 13 | 33 | nan | nan | nan | Amazônia | 118.6 |
| e95c8c07-e922-3e87-b2c0-1ed65ceb42b6 | -3.6216 | -60.547 | 2026-09-02 14:30:00 | GOES-19 | MANAQUIRI | AMAZONAS | Brasil | 1302553 | 13 | 33 | nan | nan | nan | Amazônia | 59.2 |
| dd949347-9583-3237-b0b5-946b4028d9ad | -9.1533 | -59.5027 | 2026-09-02 14:30:00 | GOES-19 | COLNIZA | MATO GROSSO | Brasil | 5103254 | 51 | 33 | nan | nan | nan | Amazônia | 79.0 |
| c068f1df-5e81-3144-87d8-1034d60e3ac1 | -8.7819 | -46.4399 | 2026-09-02 14:30:00 | GOES-19 | BALSAS | MARANHÃO | Brasil | 2101400 | 21 | 33 | nan | nan | nan | Cerrado | 69.7 |
| d013cd4c-595f-3676-9998-836d75fe41b2 | -10.7154 | -46.2395 | 2026-09-02 14:30:00 | GOES-19 | MATEIROS | TOCANTINS | Brasil | 1712702 | 17 | 33 | nan | nan | nan | Cerrado | 97.2 |
| 5eea6506-abd3-380a-824f-3783c45faca8 | -8.7817 | -46.4623 | 2026-09-02 14:30:00 | GOES-19 | BALSAS | MARANHÃO | Brasil | 2101400 | 21 | 33 | nan | nan | nan | Cerrado | 51.7 |
| ba28dc34-6683-3fe9-ad63-e1801ae3436c | -7.3685 | -45.066 | 2026-09-02 14:30:00 | GOES-19 | LORETO | MARANHÃO | Brasil | 2106102 | 21 | 33 | nan | nan | nan | Cerrado | 42.9 |
| ab009a44-27b0-320a-a17b-99b5f2933097 | -6.3894 | -45.4664 | 2026-09-02 14:30:00 | GOES-19 | FERNANDO FALCÃO | MARANHÃO | Brasil | 2104081 | 21 | 33 | nan | nan | nan | Cerrado | 68.0 |
| 4d2bcacd-23af-3bac-9ff6-c9ef6013647e | -12.3814 | -48.1655 | 2026-09-02 14:30:00 | GOES-19 | PARANÃ | TOCANTINS | Brasil | 1716208 | 17 | 33 | nan | nan | nan | Cerrado | 109.4 |
| eef8fab0-5cb5-39e8-bef9-b16c81cf0235 | -1.5806 | -47.7245 | 2026-09-02 14:30:00 | GOES-19 | SÃO MIGUEL DO GUAMÁ | PARÁ | Brasil | 1507607 | 15 | 33 | nan | nan | nan | Amazônia | 73.6 |
| 0b8ed6b0-8b81-376a-8dde-8ada142388c1 | -6.6358 | -59.4267 | 2026-09-02 14:40:00 | GOES-19 | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 56.5 |
| 8e2e2824-73c6-3d00-8270-31c1b8df2ed3 | -11.0814 | -47.1585 | 2026-09-02 14:40:00 | GOES-19 | ALMAS | TOCANTINS | Brasil | 1700400 | 17 | 33 | nan | nan | nan | Cerrado | 65.2 |
| caecd06e-eb61-3caa-b408-5fe7f0f53087 | -6.8424 | -41.655 | 2026-09-02 14:40:00 | GOES-19 | IPIRANGA DO PIAUÍ | PIAUÍ | Brasil | 2204808 | 22 | 33 | nan | nan | nan | Caatinga | 85.9 |
| 3ad14780-0d34-3892-ac91-6a33d983b974 | -10.8624 | -45.3789 | 2026-09-02 14:40:00 | GOES-19 | FORMOSA DO RIO PRETO | BAHIA | Brasil | 2911105 | 29 | 33 | nan | nan | nan | Cerrado | 52.5 |
| 3f5ca831-4286-3d50-b49e-6a5506fe1c20 | -10.7428 | -50.8727 | 2026-09-02 14:40:00 | GOES-19 | LUCIARA | MATO GROSSO | Brasil | 5105309 | 51 | 33 | nan | nan | nan | Cerrado | 79.3 |
| 80715e19-3b7e-37eb-83fc-db3072f5b0f1 | -10.7618 | -50.8707 | 2026-09-02 14:40:00 | GOES-19 | LUCIARA | MATO GROSSO | Brasil | 5105309 | 51 | 33 | nan | nan | nan | Cerrado | 77.6 |
| 750874ee-f983-34f0-9860-6fefe021b670 | -5.5832 | -60.2116 | 2026-09-02 14:40:00 | GOES-19 | NOVO ARIPUANÃ | AMAZONAS | Brasil | 1303304 | 13 | 33 | nan | nan | nan | Amazônia | 158.8 |
| e8ec2597-0d4d-3090-b928-bdecbbc4afa3 | -12.1704 | -47.0806 | 2026-09-02 14:40:00 | GOES-19 | TAIPAS DO TOCANTINS | TOCANTINS | Brasil | 1720937 | 17 | 33 | nan | nan | nan | Cerrado | 213.6 |
| 98d46040-cb79-3e8a-a3a7-44236288632d | -3.3688 | -59.4079 | 2026-09-02 14:40:00 | GOES-19 | CAREIRO DA VÁRZEA | AMAZONAS | Brasil | 1301159 | 13 | 33 | nan | nan | nan | Amazônia | 77.2 |
| e0569923-7cce-348e-aa10-b6e45f8c72d8 | -3.3265 | -42.8075 | 2026-09-02 14:40:00 | GOES-19 | SANTA QUITÉRIA DO MARANHÃO | MARANHÃO | Brasil | 2110104 | 21 | 33 | nan | nan | nan | Cerrado | 78.2 |
| ea552c52-df3b-37a6-9fb9-472ef4201551 | -11.1307 | -51.5728 | 2026-09-02 14:40:00 | GOES-19 | CANABRAVA DO NORTE | MATO GROSSO | Brasil | 5102694 | 51 | 33 | nan | nan | nan | Cerrado | 88.1 |
| 84643435-9342-3338-b5c7-864a302d5e3e | -6.6764 | -58.7686 | 2026-09-02 14:40:00 | GOES-19 | MAUÉS | AMAZONAS | Brasil | 1302900 | 13 | 33 | nan | nan | nan | Amazônia | 109.0 |
| 500dca4b-61d2-3bf7-8bb5-94b7d63ccd91 | -12.3818 | -48.1433 | 2026-09-02 14:40:00 | GOES-19 | PARANÃ | TOCANTINS | Brasil | 1716208 | 17 | 33 | nan | nan | nan | Cerrado | 103.1 |
| 03e86e58-86e7-3a68-be03-43e351bcd16e | -9.0244 | -65.4367 | 2026-09-02 14:40:00 | GOES-19 | LÁBREA | AMAZONAS | Brasil | 1302405 | 13 | 33 | nan | nan | nan | Amazônia | 50.6 |
| b92986f8-e0e8-3311-bd96-468e996f24e9 | -9.4159 | -45.6271 | 2026-09-02 14:40:00 | GOES-19 | SANTA FILOMENA | PIAUÍ | Brasil | 2209203 | 22 | 33 | nan | nan | nan | Cerrado | 48.5 |
| 577c9487-7677-313e-ab82-72675ecaa164 | -10.7009 | -47.1835 | 2026-09-02 14:40:00 | GOES-19 | PONTE ALTA DO TOCANTINS | TOCANTINS | Brasil | 1717909 | 17 | 33 | nan | nan | nan | Cerrado | 79.1 |
| 1c83f306-be0e-3a51-937d-a5e9d2cf2005 | -10.1345 | -45.7233 | 2026-09-02 14:40:00 | GOES-19 | BARREIRAS DO PIAUÍ | PIAUÍ | Brasil | 2201309 | 22 | 33 | nan | nan | nan | Cerrado | 58.5 |
| 4917b7c1-5e68-3d96-abb5-b874ddc46d3f | -13.5724 | -59.7362 | 2026-09-02 14:40:00 | GOES-19 | COMODORO | MATO GROSSO | Brasil | 5103304 | 51 | 33 | nan | nan | nan | Amazônia | 87.1 |
| 09512da0-2c92-3e85-8150-4fc7719f2807 | -12.1504 | -47.1283 | 2026-09-02 14:40:00 | GOES-19 | CONCEIÇÃO DO TOCANTINS | TOCANTINS | Brasil | 1705607 | 17 | 33 | nan | nan | nan | Cerrado | 154.3 |
| 258bcafc-9810-32ef-8282-b16329be0f4c | -6.6949 | -58.7485 | 2026-09-02 14:40:00 | GOES-19 | MAUÉS | AMAZONAS | Brasil | 1302900 | 13 | 33 | nan | nan | nan | Amazônia | 111.4 |
| a058399e-4ba3-384b-9671-b502247f8efc | -6.6542 | -59.426 | 2026-09-02 14:40:00 | GOES-19 | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 90.5 |
| 7860aed0-f5f7-33b9-9fa5-22c03824d87e | -6.8183 | -59.7658 | 2026-09-02 14:40:00 | GOES-19 | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 49.9 |
| b0a1e308-8916-38f2-b5bd-a5f396d1288d | -11.1304 | -51.5939 | 2026-09-02 14:40:00 | GOES-19 | CANABRAVA DO NORTE | MATO GROSSO | Brasil | 5102694 | 51 | 33 | nan | nan | nan | Cerrado | 80.4 |
| 07a48b61-69c9-38b7-bb17-539748234cd5 | -12.1457 | -44.196 | 2026-09-02 14:40:00 | GOES-19 | CRISTÓPOLIS | BAHIA | Brasil | 2909703 | 29 | 33 | nan | nan | nan | Cerrado | 103.1 |
| 2673b0e3-db03-36ee-a106-83e9776bddc9 | -5.5833 | -60.1924 | 2026-09-02 14:40:00 | GOES-19 | NOVO ARIPUANÃ | AMAZONAS | Brasil | 1303304 | 13 | 33 | nan | nan | nan | Amazônia | 134.5 |
| ac14405b-3999-3ee0-9529-060082345b71 | -7.2191 | -60.6699 | 2026-09-02 14:40:00 | GOES-19 | NOVO ARIPUANÃ | AMAZONAS | Brasil | 1303304 | 13 | 33 | nan | nan | nan | Amazônia | 133.1 |
| 989ed925-eda5-3686-9309-be7ffeed9a30 | -13.5533 | -59.7377 | 2026-09-02 14:40:00 | GOES-19 | COMODORO | MATO GROSSO | Brasil | 5103304 | 51 | 33 | nan | nan | nan | Amazônia | 60.6 |
| 1c07101f-f2a4-3557-b6eb-306b33bbe585 | -11.3806 | -45.1928 | 2026-09-02 14:40:00 | GOES-19 | FORMOSA DO RIO PRETO | BAHIA | Brasil | 2911105 | 29 | 33 | nan | nan | nan | Cerrado | 66.8 |
| 92f92743-f2be-323a-ac79-ecc92e275aa4 | -4.9604 | -55.8424 | 2026-09-02 14:40:00 | GOES-19 | TRAIRÃO | PARÁ | Brasil | 1508050 | 15 | 33 | nan | nan | nan | Amazônia | 52.9 |
| e18fcb94-3389-3e9f-8438-969c201e356d | -9.4349 | -45.625 | 2026-09-02 14:40:00 | GOES-19 | SANTA FILOMENA | PIAUÍ | Brasil | 2209203 | 22 | 33 | nan | nan | nan | Cerrado | 52.1 |
| 040e9d33-6e7c-33ec-9f9d-fc4ed06dbcc0 | -12.1324 | -47.0635 | 2026-09-02 14:40:00 | GOES-19 | TAIPAS DO TOCANTINS | TOCANTINS | Brasil | 1720937 | 17 | 33 | nan | nan | nan | Cerrado | 113.8 |
| 777209b6-3842-3e61-a4bc-233c67c761ad | -7.2485 | -47.5335 | 2026-09-02 14:40:00 | GOES-19 | CAROLINA | MARANHÃO | Brasil | 2102804 | 21 | 33 | nan | nan | nan | Cerrado | 50.1 |
| 4f67f77e-34c6-3d47-85db-528ec3349253 | -9.0981 | -65.5091 | 2026-09-02 14:40:00 | GOES-19 | LÁBREA | AMAZONAS | Brasil | 1302405 | 13 | 33 | nan | nan | nan | Amazônia | 50.2 |
| 250d3f78-9c81-39a3-9e3e-c99b8e565fd1 | -12.3626 | -48.1459 | 2026-09-02 14:40:00 | GOES-19 | PARANÃ | TOCANTINS | Brasil | 1716208 | 17 | 33 | nan | nan | nan | Cerrado | 151.3 |
| fb7107e8-fdd1-36e7-a338-479f13eee5d2 | -12.0933 | -47.1138 | 2026-09-02 14:40:00 | GOES-19 | CONCEIÇÃO DO TOCANTINS | TOCANTINS | Brasil | 1705607 | 17 | 33 | nan | nan | nan | Cerrado | 110.5 |


[Clique aqui para ver as próximas entradas](README80.md)
