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

## Dados Diários - Página 96

| ID | Latitude | Longitude | Data/Hora GMT | Satélite | Município | Estado | País | Município ID | Estado ID | País ID | Dias sem Chuva | Precipitação | Risco de Fogo | Bioma | FRP |
|----|----------|-----------|---------------|----------|-----------|--------|------|--------------|-----------|---------|----------------|--------------|----------------|-------|-----|
| 1e0990f6-25a2-3150-82dc-e452c531b593 | -9.9581 | -43.5987 | 2025-09-29 14:10:00 | GOES-19 | PILÃO ARCADO | BAHIA | Brasil | 2924405 | 29 | 33 | nan | nan | nan | Cerrado | 87.6 |
| d5fedc15-18e4-3188-b680-862b08993799 | -7.7416 | -46.9626 | 2025-09-29 14:10:00 | GOES-19 | CAROLINA | MARANHÃO | Brasil | 2102804 | 21 | 33 | nan | nan | nan | Cerrado | 84.5 |
| 147863c7-99d4-3469-b8b5-82d2a832ac0b | -5.7413 | -42.6576 | 2025-09-29 14:10:00 | GOES-19 | AGRICOLÂNDIA | PIAUÍ | Brasil | 2200103 | 22 | 33 | nan | nan | nan | Caatinga | 72.6 |
| aa23e3d9-4dec-3262-9db4-3f05cb5e3fee | -6.9692 | -43.7927 | 2025-09-29 14:10:00 | GOES-19 | MARCOS PARENTE | PIAUÍ | Brasil | 2206001 | 22 | 33 | nan | nan | nan | Cerrado | 74.6 |
| 351cac3f-4866-31a4-a593-d41fbdc7ebfa | -22.6286 | -49.03 | 2025-09-29 14:10:00 | GOES-19 | AGUDOS | SÃO PAULO | Brasil | 3500709 | 35 | 33 | nan | nan | nan | Cerrado | 171.3 |
| c4ff8d4e-709e-3563-85d9-88973bc6a1f2 | -5.9004 | -43.6976 | 2025-09-29 14:10:00 | GOES-19 | BURITI BRAVO | MARANHÃO | Brasil | 2102309 | 21 | 33 | nan | nan | nan | Cerrado | 73.0 |
| 92681390-bb52-3872-8383-18bae7d1c68d | -9.4744 | -45.5068 | 2025-09-29 14:10:00 | GOES-19 | GILBUÉS | PIAUÍ | Brasil | 2204402 | 22 | 33 | nan | nan | nan | Cerrado | 67.1 |
| 76453c6a-47b6-340b-bae2-63b29035c910 | -9.2821 | -45.733 | 2025-09-29 14:10:00 | GOES-19 | SANTA FILOMENA | PIAUÍ | Brasil | 2209203 | 22 | 33 | nan | nan | nan | Cerrado | 69.3 |
| 0bc25456-9e75-3b7c-90e6-5fa57ba151d9 | -7.8375 | -46.7766 | 2025-09-29 14:10:00 | GOES-19 | RIACHÃO | MARANHÃO | Brasil | 2109502 | 21 | 33 | nan | nan | nan | Cerrado | 92.5 |
| 5b8efeaf-e9da-3094-996f-1550c8d07d4e | -11.4405 | -45.0461 | 2025-09-29 14:10:00 | GOES-19 | RIACHÃO DAS NEVES | BAHIA | Brasil | 2926202 | 29 | 33 | nan | nan | nan | Cerrado | 113.5 |
| 6d5b841b-348f-3931-9e42-7a69e3c298bf | -8.88 | -47.6282 | 2025-09-29 14:10:00 | GOES-19 | SANTA MARIA DO TOCANTINS | TOCANTINS | Brasil | 1718881 | 17 | 33 | nan | nan | nan | Cerrado | 73.1 |
| a124a87b-41ed-30f1-950b-1adfda08e24a | -7.8566 | -46.7527 | 2025-09-29 14:10:00 | GOES-19 | RIACHÃO | MARANHÃO | Brasil | 2109502 | 21 | 33 | nan | nan | nan | Cerrado | 157.4 |
| bdd5a725-4ad6-33ad-9e37-10df9adcf17c | -9.0685 | -47.6093 | 2025-09-29 14:10:00 | GOES-19 | CENTENÁRIO | TOCANTINS | Brasil | 1704105 | 17 | 33 | nan | nan | nan | Cerrado | 67.2 |
| d2c1f447-1094-3c9a-9452-f31675b57f56 | -6.0811 | -42.4644 | 2025-09-29 14:10:00 | GOES-19 | HUGO NAPOLEÃO | PIAUÍ | Brasil | 2204600 | 22 | 33 | nan | nan | nan | Caatinga | 121.5 |
| 87703782-b8be-3be7-8590-18218afb8ca4 | -10.8238 | -45.407 | 2025-09-29 14:10:00 | GOES-19 | FORMOSA DO RIO PRETO | BAHIA | Brasil | 2911105 | 29 | 33 | nan | nan | nan | Cerrado | 90.7 |
| 285b7cd7-886b-3c56-bc62-cfe75495b349 | -7.7414 | -46.9848 | 2025-09-29 14:10:00 | GOES-19 | CAROLINA | MARANHÃO | Brasil | 2102804 | 21 | 33 | nan | nan | nan | Cerrado | 77.5 |
| 34808630-d780-3ab9-bd9d-278e862ea3aa | -11.4866 | -43.5219 | 2025-09-29 14:10:00 | GOES-19 | BARRA | BAHIA | Brasil | 2902708 | 29 | 33 | nan | nan | nan | Cerrado | 100.3 |
| 14aa5b5b-a4dc-3199-b771-d1844e89daf3 | -6.8256 | -44.9319 | 2025-09-29 14:10:00 | GOES-19 | SÃO FÉLIX DE BALSAS | MARANHÃO | Brasil | 2110807 | 21 | 33 | nan | nan | nan | Cerrado | 137.8 |
| c0d42602-90c4-34de-8569-ffd625006aa7 | -8.5221 | -44.6535 | 2025-09-29 14:10:00 | GOES-19 | PALMEIRA DO PIAUÍ | PIAUÍ | Brasil | 2207405 | 22 | 33 | nan | nan | nan | Cerrado | 69.6 |
| 98cea363-fcaa-3877-b2b6-a93d365aa97b | -9.7674 | -46.1971 | 2025-09-29 14:10:00 | GOES-19 | ALTO PARNAÍBA | MARANHÃO | Brasil | 2100501 | 21 | 33 | nan | nan | nan | Cerrado | 143.1 |
| b54d50b2-b37c-3103-a1ac-577e2db652de | -9.764 | -47.8006 | 2025-09-29 14:10:00 | GOES-19 | RIO SONO | TOCANTINS | Brasil | 1718758 | 17 | 33 | nan | nan | nan | Cerrado | 67.3 |
| 3cdc73fb-f094-3ffb-b686-62dd387ad46d | -11.925 | -48.0273 | 2025-09-29 14:10:00 | GOES-19 | SÃO VALÉRIO | TOCANTINS | Brasil | 1720499 | 17 | 33 | nan | nan | nan | Cerrado | 121.4 |
| 50fa6793-e54f-3c73-9e97-0c025f2e9336 | -13.3796 | -48.1577 | 2025-09-29 14:10:00 | GOES-19 | MINAÇU | GOIÁS | Brasil | 5213087 | 52 | 33 | nan | nan | nan | Cerrado | 331.2 |
| 5f00f79d-691e-32f2-b771-a8ea955df812 | -7.4488 | -46.299 | 2025-09-29 14:10:00 | GOES-19 | BALSAS | MARANHÃO | Brasil | 2101400 | 21 | 33 | nan | nan | nan | Cerrado | 77.0 |
| d15987a0-cc1f-3637-bd10-4be7be68ffa3 | -5.7294 | -43.9651 | 2025-09-29 14:10:00 | GOES-19 | BURITI BRAVO | MARANHÃO | Brasil | 2102309 | 21 | 33 | nan | nan | nan | Cerrado | 67.2 |
| d0d812dd-7a6b-33cc-9701-c7e0922db2c5 | -5.7866 | -43.8453 | 2025-09-29 14:10:00 | GOES-19 | BURITI BRAVO | MARANHÃO | Brasil | 2102309 | 21 | 33 | nan | nan | nan | Cerrado | 70.1 |
| f7d6a0fe-7ce9-3dfd-b32e-210d6e2cf703 | -8.2665 | -45.4791 | 2025-09-29 14:10:00 | GOES-19 | RIBEIRO GONÇALVES | PIAUÍ | Brasil | 2208908 | 22 | 33 | nan | nan | nan | Cerrado | 73.7 |
| db927a61-3ec2-39fb-afc6-c4ce48066596 | -9.4194 | -54.697 | 2025-09-29 14:10:00 | GOES-19 | NOVO PROGRESSO | PARÁ | Brasil | 1505031 | 15 | 33 | nan | nan | nan | Amazônia | 98.8 |
| 5da2a8cb-99fe-3a1d-96fb-9fade9c11c69 | -11.3642 | -45.0339 | 2025-09-29 14:10:00 | GOES-19 | FORMOSA DO RIO PRETO | BAHIA | Brasil | 2911105 | 29 | 33 | nan | nan | nan | Cerrado | 117.8 |
| 37339efd-0a2a-33c9-882d-4c8146453b60 | -6.797 | -44.0859 | 2025-09-29 14:10:00 | GOES-19 | NOVA IORQUE | MARANHÃO | Brasil | 2107308 | 21 | 33 | nan | nan | nan | Cerrado | 60.2 |
| d304a055-3893-3235-bb7c-d6915c047bd1 | -11.5246 | -43.5397 | 2025-09-29 14:10:00 | GOES-19 | BARRA | BAHIA | Brasil | 2902708 | 29 | 33 | nan | nan | nan | Cerrado | 128.4 |
| d34c846d-c911-3a1c-8552-c3c038d75605 | -9.7264 | -47.7827 | 2025-09-29 14:10:00 | GOES-19 | RIO SONO | TOCANTINS | Brasil | 1718758 | 17 | 33 | nan | nan | nan | Cerrado | 94.7 |
| 16af97e2-efaa-3243-84c7-d9142db7c6e2 | -10.6429 | -48.5364 | 2025-09-29 14:10:00 | GOES-19 | PORTO NACIONAL | TOCANTINS | Brasil | 1718204 | 17 | 33 | nan | nan | nan | Cerrado | 69.3 |
| 8b6c4b28-4d89-3d8d-94cb-cab584b2e804 | -13.5933 | -48.0593 | 2025-09-29 14:10:00 | GOES-19 | CAVALCANTE | GOIÁS | Brasil | 5205307 | 52 | 33 | nan | nan | nan | Cerrado | 95.6 |
| 48cbcf92-9705-3f11-bfe0-ea0112e7cb5a | -11.383 | -45.0543 | 2025-09-29 14:10:00 | GOES-19 | FORMOSA DO RIO PRETO | BAHIA | Brasil | 2911105 | 29 | 33 | nan | nan | nan | Cerrado | 77.7 |
| f10511b6-5a2a-39a0-a496-145a78b74c50 | -7.2605 | -42.9939 | 2025-09-29 14:10:00 | GOES-19 | FLORIANO | PIAUÍ | Brasil | 2203909 | 22 | 33 | nan | nan | nan | Caatinga | 85.5 |
| 494d250e-827c-31cf-a6d4-5c358dcc347a | -7.8165 | -46.9781 | 2025-09-29 14:10:00 | GOES-19 | CAROLINA | MARANHÃO | Brasil | 2102804 | 21 | 33 | nan | nan | nan | Cerrado | 93.3 |
| 20f9d99b-6b54-38c3-8a72-25e4e6518486 | -9.5199 | -47.6946 | 2025-09-29 14:10:00 | GOES-19 | RIO SONO | TOCANTINS | Brasil | 1718758 | 17 | 33 | nan | nan | nan | Cerrado | 79.6 |
| feaa8654-b136-3d05-aafc-7a3e3e7a7484 | -17.7144 | -46.6865 | 2025-09-29 14:10:00 | GOES-19 | VAZANTE | MINAS GERAIS | Brasil | 3171006 | 31 | 33 | nan | nan | nan | Cerrado | 173.6 |
| 81cbd1c4-e3c4-30cb-81cd-a908358a56ce | -8.9641 | -51.6906 | 2025-09-29 14:10:00 | GOES-19 | CUMARU DO NORTE | PARÁ | Brasil | 1502764 | 15 | 33 | nan | nan | nan | Amazônia | 60.3 |
| 53aa9718-cd54-3a38-883a-8b3bcd589d84 | -9.9585 | -43.5752 | 2025-09-29 14:10:00 | GOES-19 | PILÃO ARCADO | BAHIA | Brasil | 2924405 | 29 | 33 | nan | nan | nan | Cerrado | 65.5 |
| d1f56dba-b822-3f27-8ae1-1ecba2a13b89 | -8.2662 | -45.5018 | 2025-09-29 14:10:00 | GOES-19 | RIBEIRO GONÇALVES | PIAUÍ | Brasil | 2208908 | 22 | 33 | nan | nan | nan | Cerrado | 121.1 |
| d21c8db9-c88f-34b3-8167-95910a2d5d26 | -8.2474 | -45.5037 | 2025-09-29 14:10:00 | GOES-19 | RIBEIRO GONÇALVES | PIAUÍ | Brasil | 2208908 | 22 | 33 | nan | nan | nan | Cerrado | 65.6 |
| 5b3bb7ab-fae3-304c-8fd2-3901f5a7b781 | -7.9816 | -47.3168 | 2025-09-29 14:10:00 | GOES-19 | GOIATINS | TOCANTINS | Brasil | 1709005 | 17 | 33 | nan | nan | nan | Cerrado | 79.9 |
| b0c60459-b6cd-3726-9d92-b40bc4f4a171 | -6.5774 | -45.3837 | 2025-09-29 14:10:00 | GOES-19 | MIRADOR | MARANHÃO | Brasil | 2106706 | 21 | 33 | nan | nan | nan | Cerrado | 82.3 |
| cd9ac4d3-a199-30fb-911d-a2e95538b805 | -12.887 | -44.6846 | 2025-09-29 14:10:00 | GOES-19 | SÃO DESIDÉRIO | BAHIA | Brasil | 2928901 | 29 | 33 | nan | nan | nan | Cerrado | 238.3 |
| cee0d001-8bd2-3211-aa4f-f8dec6a6fbe3 | -13.011 | -49.4423 | 2025-09-29 14:10:00 | GOES-19 | ARAGUAÇU | TOCANTINS | Brasil | 1702000 | 17 | 33 | nan | nan | nan | Cerrado | 84.2 |
| 825ca52c-a14f-3f1d-b3ec-14f5a1427da9 | -14.7176 | -45.2057 | 2025-09-29 14:10:00 | GOES-19 | COCOS | BAHIA | Brasil | 2908101 | 29 | 33 | nan | nan | nan | Cerrado | 180.4 |
| e2fc6af1-890e-3104-9fd8-b57527f5d2d9 | -7.3001 | -42.825 | 2025-09-29 14:10:00 | GOES-19 | FLORIANO | PIAUÍ | Brasil | 2203909 | 22 | 33 | nan | nan | nan | Caatinga | 75.9 |
| f915c1bc-c48e-3d1f-ae55-adcb6d7d70c0 | -6.4317 | -43.0942 | 2025-09-29 14:10:00 | GOES-19 | BARÃO DE GRAJAÚ | MARANHÃO | Brasil | 2101509 | 21 | 33 | nan | nan | nan | Cerrado | 81.5 |
| 46b3bcf3-27d8-3c47-a7b4-f22e4385ddce | -10.3896 | -49.0437 | 2025-09-29 14:10:00 | GOES-19 | PIUM | TOCANTINS | Brasil | 1717503 | 17 | 33 | nan | nan | nan | Cerrado | 69.8 |
| b42d12d7-171d-3125-8d11-77c879d35552 | -14.5668 | -44.9763 | 2025-09-29 14:10:00 | GOES-19 | COCOS | BAHIA | Brasil | 2908101 | 29 | 33 | nan | nan | nan | Cerrado | 194.1 |
| a13f0a47-2f99-34d2-918b-e19c7f3e21ea | -8.2848 | -45.5225 | 2025-09-29 14:10:00 | GOES-19 | RIBEIRO GONÇALVES | PIAUÍ | Brasil | 2208908 | 22 | 33 | nan | nan | nan | Cerrado | 205.9 |
| 4bf48eae-b1a8-32ca-9747-11a57c856ce5 | -11.7981 | -47.6226 | 2025-09-29 14:10:00 | GOES-19 | NATIVIDADE | TOCANTINS | Brasil | 1714203 | 17 | 33 | nan | nan | nan | Cerrado | 98.3 |
| 908a5f36-aa0a-3ef6-954c-6c308b4289e1 | -9.3328 | -47.5821 | 2025-09-29 14:10:00 | GOES-19 | RIO SONO | TOCANTINS | Brasil | 1718758 | 17 | 33 | nan | nan | nan | Cerrado | 91.8 |
| bece7d64-ea77-39ed-9c7a-e7384393f583 | -6.7782 | -44.0876 | 2025-09-29 14:10:00 | GOES-19 | NOVA IORQUE | MARANHÃO | Brasil | 2107308 | 21 | 33 | nan | nan | nan | Cerrado | 59.0 |
| 3432d610-e071-3c9e-86df-0561f908d9b8 | -7.2416 | -42.9957 | 2025-09-29 14:10:00 | GOES-19 | FLORIANO | PIAUÍ | Brasil | 2203909 | 22 | 33 | nan | nan | nan | Caatinga | 76.1 |
| 8a799c3c-b4b6-3064-9778-a8b38016bbf2 | -13.2154 | -50.9715 | 2025-09-29 14:10:00 | GOES-19 | COCALINHO | MATO GROSSO | Brasil | 5103106 | 51 | 33 | nan | nan | nan | Cerrado | 80.1 |
| 9b209c61-be84-3539-9a4f-223dff4a0b07 | -6.2968 | -43.4331 | 2025-09-29 14:10:00 | GOES-19 | SUCUPIRA DO RIACHÃO | MARANHÃO | Brasil | 2111953 | 21 | 33 | nan | nan | nan | Cerrado | 63.2 |
| 2b6ec747-58b9-34fe-992f-cd58c3a6e490 | -9.301 | -45.7309 | 2025-09-29 14:10:00 | GOES-19 | SANTA FILOMENA | PIAUÍ | Brasil | 2209203 | 22 | 33 | nan | nan | nan | Cerrado | 107.5 |
| 4540dfd1-635a-3a60-8738-0ecbdb696b62 | -6.6981 | -42.7882 | 2025-09-29 14:10:00 | GOES-19 | FRANCISCO AYRES | PIAUÍ | Brasil | 2204105 | 22 | 33 | nan | nan | nan | Caatinga | 70.7 |
| 9429ad2e-0c7f-33e4-9afc-92b674124fe0 | -7.4573 | -47.2523 | 2025-09-29 14:10:00 | GOES-19 | CAROLINA | MARANHÃO | Brasil | 2102804 | 21 | 33 | nan | nan | nan | Cerrado | 66.5 |
| 3941c1e2-bf18-381d-9852-8aed1c4af732 | -9.4007 | -54.6984 | 2025-09-29 14:10:00 | GOES-19 | NOVO PROGRESSO | PARÁ | Brasil | 1505031 | 15 | 33 | nan | nan | nan | Amazônia | 104.5 |
| dce2e556-309d-3a14-b1a7-bc62bde61772 | -7.5447 | -46.1115 | 2025-09-29 14:10:00 | GOES-19 | BALSAS | MARANHÃO | Brasil | 2101400 | 21 | 33 | nan | nan | nan | Cerrado | 89.8 |
| 493f53e4-a4b7-343a-ab71-ebeee9bf84c6 | -7.6062 | -47.3498 | 2025-09-29 14:10:00 | GOES-19 | CAROLINA | MARANHÃO | Brasil | 2102804 | 21 | 33 | nan | nan | nan | Cerrado | 68.7 |
| 5be8b0e3-bf55-3853-bb95-de73fc0c347d | -6.4131 | -43.0724 | 2025-09-29 14:10:00 | GOES-19 | SÃO FRANCISCO DO MARANHÃO | MARANHÃO | Brasil | 2110906 | 21 | 33 | nan | nan | nan | Cerrado | 87.4 |
| 6ad4e5e4-a471-33d4-8ba3-8fdaf569ad35 | -4.1489 | -40.0227 | 2025-09-29 14:10:00 | GOES-19 | SANTA QUITÉRIA | CEARÁ | Brasil | 2312205 | 23 | 33 | nan | nan | nan | Caatinga | 101.7 |
| b994563c-3235-3272-9dfc-f2a40534aa07 | -9.4192 | -54.7172 | 2025-09-29 14:10:00 | GOES-19 | NOVO PROGRESSO | PARÁ | Brasil | 1505031 | 15 | 33 | nan | nan | nan | Amazônia | 77.6 |
| 52270f34-1a60-3861-835a-7508edb539d9 | -10.4022 | -48.1476 | 2025-09-29 14:10:00 | GOES-19 | PALMAS | TOCANTINS | Brasil | 1721000 | 17 | 33 | nan | nan | nan | Cerrado | 57.5 |
| da1edf2d-5636-36e4-b467-d11f3b11713b | -6.8266 | -44.8407 | 2025-09-29 14:10:00 | GOES-19 | SÃO FÉLIX DE BALSAS | MARANHÃO | Brasil | 2110807 | 21 | 33 | nan | nan | nan | Cerrado | 67.7 |
| 095fea85-e50a-3054-a37a-72f5d99e1657 | -10.8429 | -45.4044 | 2025-09-29 14:10:00 | GOES-19 | FORMOSA DO RIO PRETO | BAHIA | Brasil | 2911105 | 29 | 33 | nan | nan | nan | Cerrado | 81.0 |
| 11a3b8b7-41ac-31b5-8289-311913084aa8 | -7.6064 | -47.3278 | 2025-09-29 14:10:00 | GOES-19 | CAROLINA | MARANHÃO | Brasil | 2102804 | 21 | 33 | nan | nan | nan | Cerrado | 77.6 |
| 54cbc36a-667a-3496-994f-c5fd61a0af6a | -6.0797 | -42.6064 | 2025-09-29 14:10:00 | GOES-19 | JARDIM DO MULATO | PIAUÍ | Brasil | 2205250 | 22 | 33 | nan | nan | nan | Caatinga | 83.8 |
| c9fe6f72-befc-3b42-a74d-1bc5997b02dc | -9.939 | -55.1632 | 2025-09-29 14:10:00 | GOES-19 | NOVO MUNDO | MATO GROSSO | Brasil | 5106265 | 51 | 33 | nan | nan | nan | Amazônia | 68.8 |
| 249328b2-a8ef-3809-b3b9-3aa455caeac0 | -6.3154 | -43.4548 | 2025-09-29 14:10:00 | GOES-19 | SUCUPIRA DO RIACHÃO | MARANHÃO | Brasil | 2111953 | 21 | 33 | nan | nan | nan | Cerrado | 74.9 |
| d9431eab-df99-30b8-94ac-abaad46a7f45 | -7.8019 | -48.3173 | 2025-09-29 14:10:00 | GOES-19 | PALMEIRANTE | TOCANTINS | Brasil | 1715705 | 17 | 33 | nan | nan | nan | Cerrado | 81.2 |
| e0945009-04e2-32aa-95be-7142a2ca4246 | -11.9247 | -48.0495 | 2025-09-29 14:10:00 | GOES-19 | SÃO VALÉRIO | TOCANTINS | Brasil | 1720499 | 17 | 33 | nan | nan | nan | Cerrado | 105.7 |
| 4669a9ea-a190-3e98-a3c1-2915f38d2e38 | -9.7867 | -46.1723 | 2025-09-29 14:10:00 | GOES-19 | ALTO PARNAÍBA | MARANHÃO | Brasil | 2100501 | 21 | 33 | nan | nan | nan | Cerrado | 73.6 |
| ae8f44b2-ecab-371b-9b25-52af9682586e | -7.4414 | -46.9888 | 2025-09-29 14:10:00 | GOES-19 | RIACHÃO | MARANHÃO | Brasil | 2109502 | 21 | 33 | nan | nan | nan | Cerrado | 65.4 |
| 882d08e9-d6e5-3046-94cc-98ea92440467 | -7.2999 | -42.8486 | 2025-09-29 14:10:00 | GOES-19 | FLORIANO | PIAUÍ | Brasil | 2203909 | 22 | 33 | nan | nan | nan | Caatinga | 86.1 |
| 6bffa8b2-0966-333f-89cf-5c695eb1f780 | -20.7334 | -57.8293 | 2025-09-29 14:10:00 | GOES-19 | CORUMBÁ | MATO GROSSO DO SUL | Brasil | 5003207 | 50 | 33 | nan | nan | nan | Pantanal | 68.4 |
| ebe4c4ba-ff4f-3156-a637-d6cae29c961d | -18.4667 | -43.9996 | 2025-09-29 14:10:00 | GOES-19 | MONJOLOS | MINAS GERAIS | Brasil | 3142502 | 31 | 33 | nan | nan | nan | Cerrado | 127.4 |
| 2030ce0c-54db-3f47-a759-32d0ab92b407 | -7.5089 | -44.297 | 2025-09-29 14:10:00 | GOES-19 | URUÇUÍ | PIAUÍ | Brasil | 2211209 | 22 | 33 | nan | nan | nan | Cerrado | 108.6 |
| 3f78578d-898f-33ce-bba2-5931a74b2af4 | -9.7864 | -46.1949 | 2025-09-29 14:10:00 | GOES-19 | ALTO PARNAÍBA | MARANHÃO | Brasil | 2100501 | 21 | 33 | nan | nan | nan | Cerrado | 166.8 |
| 723450dc-0fbb-3369-8028-20986137e43e | -8.9456 | -51.6712 | 2025-09-29 14:10:00 | GOES-19 | CUMARU DO NORTE | PARÁ | Brasil | 1502764 | 15 | 33 | nan | nan | nan | Amazônia | 107.5 |
| ea408b89-f334-30bb-9ef4-5bc5dabdcd8d | -7.9006 | -44.6035 | 2025-09-29 14:10:00 | GOES-19 | URUÇUÍ | PIAUÍ | Brasil | 2211209 | 22 | 33 | nan | nan | nan | Cerrado | 85.1 |
| 6de37393-1e77-3f98-a5d4-4b1b61b9ff5f | -7.6275 | -45.428 | 2025-09-29 14:10:00 | GOES-19 | LORETO | MARANHÃO | Brasil | 2106102 | 21 | 33 | nan | nan | nan | Cerrado | 66.2 |
| 05426843-a437-3ef8-800a-2106ca872ce1 | -9.7454 | -47.7806 | 2025-09-29 14:10:00 | GOES-19 | RIO SONO | TOCANTINS | Brasil | 1718758 | 17 | 33 | nan | nan | nan | Cerrado | 96.0 |
| c0cdcc06-fd15-3e9d-a254-f7fcc2bf730d | -5.7679 | -43.8467 | 2025-09-29 14:10:00 | GOES-19 | BURITI BRAVO | MARANHÃO | Brasil | 2102309 | 21 | 33 | nan | nan | nan | Cerrado | 78.5 |
| 1b8a52b9-aee5-30fb-90f9-39a6530fac73 | -7.2216 | -44.7601 | 2025-09-29 14:10:00 | GOES-19 | SÃO FÉLIX DE BALSAS | MARANHÃO | Brasil | 2110807 | 21 | 33 | nan | nan | nan | Cerrado | 89.1 |
| 88a6bf34-bafb-3d34-85a0-86d7f9fb41b3 | -8.1614 | -46.3899 | 2025-09-29 14:10:00 | GOES-19 | BALSAS | MARANHÃO | Brasil | 2101400 | 21 | 33 | nan | nan | nan | Cerrado | 74.2 |
| d54196c6-4137-39f0-9213-6c815350a5b6 | -7.2813 | -42.8269 | 2025-09-29 14:10:00 | GOES-19 | FLORIANO | PIAUÍ | Brasil | 2203909 | 22 | 33 | nan | nan | nan | Caatinga | 99.9 |
| d67c1301-8f67-392a-9d62-0142aeed6e0b | -10.0528 | -50.2192 | 2025-09-29 14:10:00 | GOES-19 | PIUM | TOCANTINS | Brasil | 1717503 | 17 | 33 | nan | nan | nan | Cerrado | 88.1 |
| e0eedbd7-7036-3110-a4a3-75108348c744 | -7.4676 | -46.2974 | 2025-09-29 14:10:00 | GOES-19 | BALSAS | MARANHÃO | Brasil | 2101400 | 21 | 33 | nan | nan | nan | Cerrado | 95.6 |
| ece0e6c3-d700-3f12-9741-b12bcc187055 | -13.38 | -48.1354 | 2025-09-29 14:10:00 | GOES-19 | CAVALCANTE | GOIÁS | Brasil | 5205307 | 52 | 33 | nan | nan | nan | Cerrado | 120.7 |
| a5348614-1e09-3517-af1b-0eb1fd7a9449 | -9.7671 | -46.2196 | 2025-09-29 14:10:00 | GOES-19 | ALTO PARNAÍBA | MARANHÃO | Brasil | 2100501 | 21 | 33 | nan | nan | nan | Cerrado | 60.7 |
| 873c93d4-3f14-34ed-9a22-953199c81841 | -11.4862 | -43.5456 | 2025-09-29 14:10:00 | GOES-19 | BARRA | BAHIA | Brasil | 2902708 | 29 | 33 | nan | nan | nan | Cerrado | 109.4 |
| 39676934-dea2-3c5a-9a77-97c5541603e2 | -11.3638 | -45.057 | 2025-09-29 14:10:00 | GOES-19 | FORMOSA DO RIO PRETO | BAHIA | Brasil | 2911105 | 29 | 33 | nan | nan | nan | Cerrado | 506.8 |
| 62cede39-9387-3868-92f0-037894c01e58 | -9.4458 | -47.5923 | 2025-09-29 14:10:00 | GOES-19 | RIO SONO | TOCANTINS | Brasil | 1718758 | 17 | 33 | nan | nan | nan | Cerrado | 68.9 |
| fcb42671-1be9-3f4e-9e91-77b73ba13743 | -7.8163 | -47.0003 | 2025-09-29 14:10:00 | GOES-19 | CAROLINA | MARANHÃO | Brasil | 2102804 | 21 | 33 | nan | nan | nan | Cerrado | 154.8 |


[Clique aqui para ver as próximas entradas](README97.md)
