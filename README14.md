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

## Dados Diários - Página 14

| ID | Latitude | Longitude | Data/Hora GMT | Satélite | Município | Estado | País | Município ID | Estado ID | País ID | Dias sem Chuva | Precipitação | Risco de Fogo | Bioma | FRP |
|----|----------|-----------|---------------|----------|-----------|--------|------|--------------|-----------|---------|----------------|--------------|----------------|-------|-----|
| a6f4da13-f5da-387d-aa60-8892b455491c | -3.2112 | -54.96529 | 2025-07-24 04:40:00 | NPP-375D | BELTERRA | PARÁ | Brasil | 1501451 | 15 | 33 | nan | nan | nan | Amazônia | 1.5 |
| 85bc979d-5d8a-37b4-8d79-5fc3caa1fa8a | -8.03415 | -47.65432 | 2025-07-24 04:40:00 | NPP-375D | GOIATINS | TOCANTINS | Brasil | 1709005 | 17 | 33 | nan | nan | nan | Cerrado | 1.6 |
| 513702be-7cff-3231-9b9c-0deeb0c8d221 | -6.64226 | -43.05582 | 2025-07-24 04:40:00 | NPP-375D | BARÃO DE GRAJAÚ | MARANHÃO | Brasil | 2101509 | 21 | 33 | nan | nan | nan | Cerrado | 0.9 |
| 0c4d9734-e45a-3f0f-9a8f-7173a4fb2315 | -3.17856 | -49.4567 | 2025-07-24 04:40:00 | NPP-375D | MOJU | PARÁ | Brasil | 1504703 | 15 | 33 | nan | nan | nan | Amazônia | 14.7 |
| e48bde48-c08a-3833-a143-747b9caba466 | -6.90953 | -44.98454 | 2025-07-24 04:40:00 | NPP-375D | LORETO | MARANHÃO | Brasil | 2106102 | 21 | 33 | nan | nan | nan | Cerrado | 2.9 |
| 7221fac3-3bf6-3170-9146-3feffa49b479 | -4.05758 | -42.52462 | 2025-07-24 04:40:00 | NPP-375D | NOSSA SENHORA DOS REMÉDIOS | PIAUÍ | Brasil | 2206803 | 22 | 33 | nan | nan | nan | Caatinga | 2.2 |
| 5bb86c91-690e-319c-ac23-ff93fd3d7050 | -3.04881 | -47.37979 | 2025-07-24 04:40:00 | NPP-375D | PARAGOMINAS | PARÁ | Brasil | 1505502 | 15 | 33 | nan | nan | nan | Amazônia | 2.3 |
| 34cae028-a61c-3716-ab30-194feecf3710 | -3.24919 | -51.10679 | 2025-07-24 04:40:00 | NPP-375D | PACAJÁ | PARÁ | Brasil | 1505486 | 15 | 33 | nan | nan | nan | Amazônia | 0.7 |
| b3c6d175-71af-3f75-a1e2-7e21d76c8822 | -3.17134 | -49.45914 | 2025-07-24 04:40:00 | NPP-375D | MOJU | PARÁ | Brasil | 1504703 | 15 | 33 | nan | nan | nan | Amazônia | 15.6 |
| 0594ebcd-3b4e-335f-947e-47d19690c2c7 | -3.3593 | -47.1584 | 2025-07-24 04:40:00 | NPP-375D | PARAGOMINAS | PARÁ | Brasil | 1505502 | 15 | 33 | nan | nan | nan | Amazônia | 1.2 |
| 16c80742-2ab2-3295-a6ba-dc3f5c0615ef | -3.93253 | -43.16697 | 2025-07-24 04:40:00 | NPP-375D | BURITI | MARANHÃO | Brasil | 2102200 | 21 | 33 | nan | nan | nan | Cerrado | 1.4 |
| 5798c841-98cd-3f0e-adb0-b28b8b2a6d83 | -7.17145 | -44.37398 | 2025-07-24 04:40:00 | NPP-375D | URUÇUÍ | PIAUÍ | Brasil | 2211209 | 22 | 33 | nan | nan | nan | Cerrado | 1.0 |
| 0fc1a607-948c-3d0d-b857-109cde2f4692 | -3.61505 | -51.90752 | 2025-07-24 04:40:00 | NPP-375D | SENADOR JOSÉ PORFÍRIO | PARÁ | Brasil | 1507805 | 15 | 33 | nan | nan | nan | Amazônia | 2.2 |
| a4048e66-2317-355b-bf07-17703225a173 | -4.30526 | -48.10064 | 2025-07-24 04:40:00 | NPP-375D | RONDON DO PARÁ | PARÁ | Brasil | 1506187 | 15 | 33 | nan | nan | nan | Amazônia | 6.9 |
| d8452062-f7e1-3e55-bb98-c9c3242bcf33 | -3.22508 | -46.78644 | 2025-07-24 04:40:00 | NPP-375D | PARAGOMINAS | PARÁ | Brasil | 1505502 | 15 | 33 | nan | nan | nan | Amazônia | 7.7 |
| ebc96675-b4e5-3ddf-bd59-811170498aa2 | -6.13706 | -42.96304 | 2025-07-24 04:40:00 | NPP-375D | AMARANTE | PIAUÍ | Brasil | 2200509 | 22 | 33 | nan | nan | nan | Caatinga | 1.2 |
| de153e42-e491-36ff-9a19-bf52456b8c5b | -8.52125 | -44.67841 | 2025-07-24 04:40:00 | NPP-375D | PALMEIRA DO PIAUÍ | PIAUÍ | Brasil | 2207405 | 22 | 33 | nan | nan | nan | Cerrado | 0.6 |
| 5fe6d84d-0c34-3c4c-b38b-8b40909b4f22 | -4.41052 | -42.14184 | 2025-07-24 04:40:00 | NPP-375D | BOA HORA | PIAUÍ | Brasil | 2201770 | 22 | 33 | nan | nan | nan | Caatinga | 1.2 |
| 0e0fccb2-85aa-3ff4-be36-ba9cf2cbf610 | -7.24824 | -43.0685 | 2025-07-24 04:40:00 | NPP-375D | FLORIANO | PIAUÍ | Brasil | 2203909 | 22 | 33 | nan | nan | nan | Caatinga | 18.9 |
| 70f77605-1313-3cd7-ba9f-4417df29e1c0 | -3.183 | -49.45024 | 2025-07-24 04:40:00 | NPP-375D | MOJU | PARÁ | Brasil | 1504703 | 15 | 33 | nan | nan | nan | Amazônia | 10.0 |
| 1a7cef6a-8dd8-3da4-9715-d87d40140cec | -4.04873 | -42.5233 | 2025-07-24 04:40:00 | NPP-375D | NOSSA SENHORA DOS REMÉDIOS | PIAUÍ | Brasil | 2206803 | 22 | 33 | nan | nan | nan | Caatinga | 1.4 |
| 25995f39-d51c-3d39-8341-d31d7298d29e | -3.32525 | -48.71769 | 2025-07-24 04:40:00 | NPP-375D | IPIXUNA DO PARÁ | PARÁ | Brasil | 1503457 | 15 | 33 | nan | nan | nan | Amazônia | 1.0 |
| df700fcf-89dd-38fa-9b28-01ea55374a28 | -7.24633 | -43.08183 | 2025-07-24 04:40:00 | NPP-375D | FLORIANO | PIAUÍ | Brasil | 2203909 | 22 | 33 | nan | nan | nan | Caatinga | 6.0 |
| cce273b6-c6a9-3e1e-8b2e-b4d7291276e7 | -7.2425 | -43.07675 | 2025-07-24 04:40:00 | NPP-375D | FLORIANO | PIAUÍ | Brasil | 2203909 | 22 | 33 | nan | nan | nan | Caatinga | 10.8 |
| 095de2aa-918a-3b35-bfa4-7eb66487cc87 | -5.69402 | -50.05127 | 2025-07-24 04:40:00 | NPP-375D | MARABÁ | PARÁ | Brasil | 1504208 | 15 | 33 | nan | nan | nan | Amazônia | 0.7 |
| 10f8f4de-069a-390d-bfb6-e29b814e66df | -7.06989 | -43.91992 | 2025-07-24 04:40:00 | NPP-375D | MARCOS PARENTE | PIAUÍ | Brasil | 2206001 | 22 | 33 | nan | nan | nan | Cerrado | 1.4 |
| bae6d0ad-c850-32b2-8f47-a27ff80cb0e4 | -7.25719 | -43.0698 | 2025-07-24 04:40:00 | NPP-375D | FLORIANO | PIAUÍ | Brasil | 2203909 | 22 | 33 | nan | nan | nan | Caatinga | 27.7 |
| 7bc67d47-3fe0-35ce-95a5-f237f90f341b | -8.12368 | -43.54724 | 2025-07-24 04:40:00 | NPP-375D | ELISEU MARTINS | PIAUÍ | Brasil | 2203602 | 22 | 33 | nan | nan | nan | Cerrado | 1.5 |
| 2ec997bb-bc20-3ea5-8307-e35955d3bab9 | -5.48303 | -42.14849 | 2025-07-24 04:40:00 | NPP-375D | ALTO LONGÁ | PIAUÍ | Brasil | 2200301 | 22 | 33 | nan | nan | nan | Caatinga | 1.4 |
| 41afc1a1-125b-3705-ab83-61f7bc2560a0 | -4.05837 | -42.50927 | 2025-07-24 04:40:00 | NPP-375D | BARRAS | PIAUÍ | Brasil | 2201200 | 22 | 33 | nan | nan | nan | Caatinga | 5.3 |
| 1e8d87d5-d4e3-30ae-94ed-8727fb61521e | -7.84306 | -44.48178 | 2025-07-24 04:40:00 | NPP-375D | URUÇUÍ | PIAUÍ | Brasil | 2211209 | 22 | 33 | nan | nan | nan | Cerrado | 1.9 |
| 3aa10e42-04dd-3b35-935a-d4027b9d6959 | -3.07754 | -52.43831 | 2025-07-24 04:40:00 | NPP-375D | BRASIL NOVO | PARÁ | Brasil | 1501725 | 15 | 33 | nan | nan | nan | Amazônia | 0.9 |
| 0f9c5437-58f1-3ae9-9245-54683bb5ecda | -3.18245 | -49.45374 | 2025-07-24 04:40:00 | NPP-375D | MOJU | PARÁ | Brasil | 1504703 | 15 | 33 | nan | nan | nan | Amazônia | 10.0 |
| 6b459ce7-116a-3f07-89cb-840eec2e1705 | -3.9731 | -47.56525 | 2025-07-24 04:40:00 | NPP-375D | ULIANÓPOLIS | PARÁ | Brasil | 1508126 | 15 | 33 | nan | nan | nan | Amazônia | 0.8 |
| 0f94a8d0-338f-38ad-87c2-2cb5da624dba | -4.30137 | -48.10362 | 2025-07-24 04:40:00 | NPP-375D | RONDON DO PARÁ | PARÁ | Brasil | 1506187 | 15 | 33 | nan | nan | nan | Amazônia | 6.9 |
| 4bc98be5-4aab-3d30-a639-c528ed0d08cf | -4.05297 | -47.31997 | 2025-07-24 04:40:00 | NPP-375D | ITINGA DO MARANHÃO | MARANHÃO | Brasil | 2105427 | 21 | 33 | nan | nan | nan | Amazônia | 0.6 |
| 076f5113-291b-3b91-a500-38f6810ad82a | -3.03703 | -49.42738 | 2025-07-24 04:40:00 | NPP-375D | MOJU | PARÁ | Brasil | 1504703 | 15 | 33 | nan | nan | nan | Amazônia | 1.1 |
| 721269cd-b00a-3e9d-b388-18bce562f40a | -7.71747 | -43.95613 | 2025-07-24 04:40:00 | NPP-375D | BERTOLÍNIA | PIAUÍ | Brasil | 2201705 | 22 | 33 | nan | nan | nan | Cerrado | 1.9 |
| 6379fe59-ebba-3d90-aeb8-d6427a2b29b6 | -4.8091 | -43.20986 | 2025-07-24 04:40:00 | NPP-375D | CAXIAS | MARANHÃO | Brasil | 2103000 | 21 | 33 | nan | nan | nan | Cerrado | 3.9 |
| c1f0f363-1b94-3bc1-88e5-92964d15791e | -3.0369 | -47.86086 | 2025-07-24 04:40:00 | NPP-375D | PARAGOMINAS | PARÁ | Brasil | 1505502 | 15 | 33 | nan | nan | nan | Amazônia | 1.3 |
| c64f79d3-291b-3e63-84d2-16d20b5136e8 | -5.91486 | -43.46344 | 2025-07-24 04:40:00 | NPP-375D | LAGOA DO MATO | MARANHÃO | Brasil | 2105922 | 21 | 33 | nan | nan | nan | Cerrado | 1.7 |
| ea6e9f74-3eec-3395-89bb-3b8cfde54a7f | -4.05013 | -42.50361 | 2025-07-24 04:40:00 | NPP-375D | BARRAS | PIAUÍ | Brasil | 2201200 | 22 | 33 | nan | nan | nan | Caatinga | 1.7 |
| 6eebb178-4de4-3b4e-aedd-82cd07ed225f | -3.94892 | -41.48457 | 2025-07-24 04:40:00 | NPP-375D | PIRACURUCA | PIAUÍ | Brasil | 2208304 | 22 | 33 | nan | nan | nan | Caatinga | 1.0 |
| e1ebdd00-8412-3c9e-badc-2104d55038e1 | -3.04489 | -47.38282 | 2025-07-24 04:40:00 | NPP-375D | PARAGOMINAS | PARÁ | Brasil | 1505502 | 15 | 33 | nan | nan | nan | Amazônia | 1.9 |
| fa55040a-a9ea-352f-8e52-cd10a6f8aa07 | -5.68186 | -43.67065 | 2025-07-24 04:40:00 | NPP-375D | BURITI BRAVO | MARANHÃO | Brasil | 2102309 | 21 | 33 | nan | nan | nan | Cerrado | 2.7 |
| 7729a80b-089e-3441-ae19-23a2269801c9 | -7.83842 | -44.48481 | 2025-07-24 04:40:00 | NPP-375D | URUÇUÍ | PIAUÍ | Brasil | 2211209 | 22 | 33 | nan | nan | nan | Cerrado | 1.9 |
| a0697686-c46f-3c94-ba4d-7e63da31661f | -7.87911 | -46.89224 | 2025-07-24 04:40:00 | NPP-375D | CAROLINA | MARANHÃO | Brasil | 2102804 | 21 | 33 | nan | nan | nan | Cerrado | 2.0 |
| b699b2f6-5705-3bd5-b65b-2e48ad0e9eba | -6.41491 | -41.74381 | 2025-07-24 04:40:00 | NPP-375D | VALENÇA DO PIAUÍ | PIAUÍ | Brasil | 2211308 | 22 | 33 | nan | nan | nan | Caatinga | 0.8 |
| faf533e5-8a6a-3318-bb7a-61b9dd04b94c | -7.71942 | -43.94995 | 2025-07-24 04:40:00 | NPP-375D | BERTOLÍNIA | PIAUÍ | Brasil | 2201705 | 22 | 33 | nan | nan | nan | Cerrado | 1.1 |
| ad21693f-ff11-3680-a8d4-787ce324df88 | -3.17633 | -49.4492 | 2025-07-24 04:40:00 | NPP-375D | MOJU | PARÁ | Brasil | 1504703 | 15 | 33 | nan | nan | nan | Amazônia | 27.9 |
| 9706b43e-c123-3dd8-a32e-ebe4df8c540b | -6.53645 | -44.65775 | 2025-07-24 04:40:00 | NPP-375D | MIRADOR | MARANHÃO | Brasil | 2106706 | 21 | 33 | nan | nan | nan | Cerrado | 1.8 |
| ca9854f7-3788-3ed8-bdff-dce5773df103 | -3.05947 | -47.3778 | 2025-07-24 04:40:00 | NPP-375D | PARAGOMINAS | PARÁ | Brasil | 1505502 | 15 | 33 | nan | nan | nan | Amazônia | 3.0 |
| 2088d372-0e0d-31df-ab56-ecd478899d75 | -6.93763 | -50.31734 | 2025-07-24 04:40:00 | NPP-375D | ÁGUA AZUL DO NORTE | PARÁ | Brasil | 1500347 | 15 | 33 | nan | nan | nan | Amazônia | 1.1 |
| edd74124-f4e6-3861-aad1-9c96e9d00011 | -3.47389 | -41.23747 | 2025-07-24 04:40:00 | NPP-375D | VIÇOSA DO CEARÁ | CEARÁ | Brasil | 2314102 | 23 | 33 | nan | nan | nan | Caatinga | 1.1 |
| 7cb8512f-fd06-3952-8500-661024aa2927 | -3.18422 | -50.39254 | 2025-07-24 04:40:00 | NPP-375D | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 0.8 |
| 0802ec76-69c2-39a4-ad9e-dcf6c2551a56 | -3.1819 | -49.45723 | 2025-07-24 04:40:00 | NPP-375D | MOJU | PARÁ | Brasil | 1504703 | 15 | 33 | nan | nan | nan | Amazônia | 2.1 |
| 30cb19c3-5002-3f83-be10-c32288cbb351 | -5.67767 | -43.66996 | 2025-07-24 04:40:00 | NPP-375D | BURITI BRAVO | MARANHÃO | Brasil | 2102309 | 21 | 33 | nan | nan | nan | Cerrado | 2.7 |
| cfd3a52a-bbdf-3cc6-a4ea-ebed2a2958da | -3.58398 | -47.52751 | 2025-07-24 04:40:00 | NPP-375D | ULIANÓPOLIS | PARÁ | Brasil | 1508126 | 15 | 33 | nan | nan | nan | Amazônia | 1.0 |
| e2582f6e-c763-317a-bed3-261ae5158b29 | -3.04204 | -49.4389 | 2025-07-24 04:40:00 | NPP-375D | MOJU | PARÁ | Brasil | 1504703 | 15 | 33 | nan | nan | nan | Amazônia | 1.8 |
| 7bcda468-570c-3d31-99b1-1bb7a10ae932 | -0.7463 | -47.75217 | 2025-07-24 04:40:00 | NPP-375D | MARAPANIM | PARÁ | Brasil | 1504406 | 15 | 33 | nan | nan | nan | Amazônia | 0.7 |
| 1b8773b8-9546-32a4-b0e6-ee9e4b677f95 | -3.17299 | -49.44867 | 2025-07-24 04:40:00 | NPP-375D | MOJU | PARÁ | Brasil | 1504703 | 15 | 33 | nan | nan | nan | Amazônia | 10.7 |
| 3e3e2ac6-ea0c-3a39-9bac-9024331c79e0 | -6.57789 | -49.51059 | 2025-07-24 04:40:00 | NPP-375D | XINGUARA | PARÁ | Brasil | 1508407 | 15 | 33 | nan | nan | nan | Amazônia | 3.8 |
| 477c526b-e844-398c-8310-d97e593431db | -4.04628 | -42.50973 | 2025-07-24 04:40:00 | NPP-375D | BARRAS | PIAUÍ | Brasil | 2201200 | 22 | 33 | nan | nan | nan | Caatinga | 6.8 |
| a00f511d-e265-3ae6-a81e-556a0ae93ccc | -4.57251 | -48.01674 | 2025-07-24 04:40:00 | NPP-375D | RONDON DO PARÁ | PARÁ | Brasil | 1506187 | 15 | 33 | nan | nan | nan | Amazônia | 0.6 |
| 4e87ef34-de34-3821-92c8-def4a2ec3669 | -7.08589 | -44.87357 | 2025-07-24 04:40:00 | NPP-375D | SÃO FÉLIX DE BALSAS | MARANHÃO | Brasil | 2110807 | 21 | 33 | nan | nan | nan | Cerrado | 2.1 |
| 55b7c167-3e54-3981-915b-409f9daf84f4 | -3.18022 | -49.44623 | 2025-07-24 04:40:00 | NPP-375D | MOJU | PARÁ | Brasil | 1504703 | 15 | 33 | nan | nan | nan | Amazônia | 2.7 |
| 1b6093fa-8881-3bee-888f-593321aea0a9 | -6.81699 | -44.00102 | 2025-07-24 04:40:00 | NPP-375D | PORTO ALEGRE DO PIAUÍ | PIAUÍ | Brasil | 2208551 | 22 | 33 | nan | nan | nan | Cerrado | 1.5 |
| dc23156e-a28e-3611-acfb-c7e81030e78f | -3.05273 | -47.37676 | 2025-07-24 04:40:00 | NPP-375D | PARAGOMINAS | PARÁ | Brasil | 1505502 | 15 | 33 | nan | nan | nan | Amazônia | 2.7 |
| d8ef7c3a-376b-371a-b3d8-6b27b5232af1 | -3.47221 | -42.85601 | 2025-07-24 04:40:00 | NPP-375D | MILAGRES DO MARANHÃO | MARANHÃO | Brasil | 2106672 | 21 | 33 | nan | nan | nan | Cerrado | 1.1 |
| e73a7ff5-d72e-384f-96ea-d7216504aa20 | -7.5481 | -44.48409 | 2025-07-24 04:40:00 | NPP-375D | URUÇUÍ | PIAUÍ | Brasil | 2211209 | 22 | 33 | nan | nan | nan | Cerrado | 0.9 |
| 33ea680e-2890-32a3-84ec-b0cd335c168f | -4.80631 | -43.21614 | 2025-07-24 04:40:00 | NPP-375D | CAXIAS | MARANHÃO | Brasil | 2103000 | 21 | 33 | nan | nan | nan | Cerrado | 2.0 |
| 7312fe74-80f4-3148-b8f3-b680ff073f87 | -6.63655 | -43.09461 | 2025-07-24 04:40:00 | NPP-375D | BARÃO DE GRAJAÚ | MARANHÃO | Brasil | 2101509 | 21 | 33 | nan | nan | nan | Cerrado | 1.7 |
| ce7ad547-17d9-3d22-bc13-72cde04247c5 | -3.18578 | -49.45426 | 2025-07-24 04:40:00 | NPP-375D | MOJU | PARÁ | Brasil | 1504703 | 15 | 33 | nan | nan | nan | Amazônia | 10.0 |
| 9de6d6fd-60d1-36c2-8709-d7934687367e | -8.03761 | -47.65485 | 2025-07-24 04:40:00 | NPP-375D | GOIATINS | TOCANTINS | Brasil | 1709005 | 17 | 33 | nan | nan | nan | Cerrado | 1.6 |
| f64b3a7e-5061-37fd-98f7-d6b2b2206c3d | -4.31664 | -47.98383 | 2025-07-24 04:40:00 | NPP-375D | DOM ELISEU | PARÁ | Brasil | 1502939 | 15 | 33 | nan | nan | nan | Amazônia | 1.1 |
| ec354a12-5b89-3037-9b5c-07139e9fe64a | -6.13771 | -42.9587 | 2025-07-24 04:40:00 | NPP-375D | AMARANTE | PIAUÍ | Brasil | 2200509 | 22 | 33 | nan | nan | nan | Caatinga | 1.2 |
| 253c2c0c-6e3e-3416-b311-2a5c7a24a99c | -3.2245 | -46.79014 | 2025-07-24 04:40:00 | NPP-375D | PARAGOMINAS | PARÁ | Brasil | 1505502 | 15 | 33 | nan | nan | nan | Amazônia | 10.6 |
| f55f5ec2-eaa5-351b-b137-183eaec1e63c | -4.0571 | -42.51793 | 2025-07-24 04:40:00 | NPP-375D | NOSSA SENHORA DOS REMÉDIOS | PIAUÍ | Brasil | 2206803 | 22 | 33 | nan | nan | nan | Caatinga | 1.4 |
| b51d25b1-9992-3fd5-a451-005b80100ace | -7.46481 | -49.4015 | 2025-07-24 04:40:00 | NPP-375D | FLORESTA DO ARAGUAIA | PARÁ | Brasil | 1503044 | 15 | 33 | nan | nan | nan | Amazônia | 6.1 |
| d2c8d12e-33b4-3c34-a8a5-0bc13f40a2d2 | -6.96908 | -44.37138 | 2025-07-24 04:40:00 | NPP-375D | BENEDITO LEITE | MARANHÃO | Brasil | 2101806 | 21 | 33 | nan | nan | nan | Cerrado | 1.0 |
| 38ba8b9f-95be-3cb5-a85f-0a7131a2c5bc | -6.97234 | -44.8289 | 2025-07-24 04:40:00 | NPP-375D | SÃO FÉLIX DE BALSAS | MARANHÃO | Brasil | 2110807 | 21 | 33 | nan | nan | nan | Cerrado | 3.7 |
| e7f46d4d-9e91-36b0-b4dd-4e575ab19f2b | -6.57899 | -49.50366 | 2025-07-24 04:40:00 | NPP-375D | XINGUARA | PARÁ | Brasil | 1508407 | 15 | 33 | nan | nan | nan | Amazônia | 2.3 |
| 637b2346-1154-33a9-a8c7-711e3b5c478e | -5.18423 | -44.95631 | 2025-07-24 04:40:00 | NPP-375D | BARRA DO CORDA | MARANHÃO | Brasil | 2101608 | 21 | 33 | nan | nan | nan | Cerrado | 2.3 |
| e05e53de-4949-3dec-ada5-901c1191f51d | -3.05218 | -47.38031 | 2025-07-24 04:40:00 | NPP-375D | PARAGOMINAS | PARÁ | Brasil | 1505502 | 15 | 33 | nan | nan | nan | Amazônia | 2.3 |
| 973205ca-d16a-3db8-9678-d205f5786ed8 | -7.2508 | -43.08252 | 2025-07-24 04:40:00 | NPP-375D | FLORIANO | PIAUÍ | Brasil | 2203909 | 22 | 33 | nan | nan | nan | Caatinga | 2.3 |
| ffdb9c42-b0bf-3ce7-9506-048d3d12b77a | -4.78168 | -45.34157 | 2025-07-24 04:40:00 | NPP-375D | LAGO DA PEDRA | MARANHÃO | Brasil | 2105708 | 21 | 33 | nan | nan | nan | Cerrado | 19.9 |
| 15be800b-23ad-3f54-9c8c-3c28a267a8db | -8.03875 | -47.64728 | 2025-07-24 04:40:00 | NPP-375D | GOIATINS | TOCANTINS | Brasil | 1709005 | 17 | 33 | nan | nan | nan | Cerrado | 0.9 |
| 72290a2a-f153-3c25-80d7-779a1ef466d8 | -3.47505 | -42.85514 | 2025-07-24 04:40:00 | NPP-375D | MILAGRES DO MARANHÃO | MARANHÃO | Brasil | 2106672 | 21 | 33 | nan | nan | nan | Cerrado | 0.8 |
| f126e9c9-d0f0-34ae-b1d7-7f5191073df4 | -6.57844 | -49.50712 | 2025-07-24 04:40:00 | NPP-375D | XINGUARA | PARÁ | Brasil | 1508407 | 15 | 33 | nan | nan | nan | Amazônia | 2.3 |
| 48e0c012-7d23-3a3d-945c-cb954dc7820b | -3.57127 | -49.49704 | 2025-07-24 04:40:00 | NPP-375D | BREU BRANCO | PARÁ | Brasil | 1501782 | 15 | 33 | nan | nan | nan | Amazônia | 1.5 |
| 389e1ca7-a1f9-3cbc-974a-53bd90fbecc4 | -3.59799 | -44.79013 | 2025-07-24 04:40:00 | NPP-375D | ARARI | MARANHÃO | Brasil | 2101004 | 21 | 33 | nan | nan | nan | Amazônia | 1.8 |
| 00bbba7f-a56b-33f6-829e-f13288b756ec | -3.32857 | -48.71821 | 2025-07-24 04:40:00 | NPP-375D | IPIXUNA DO PARÁ | PARÁ | Brasil | 1503457 | 15 | 33 | nan | nan | nan | Amazônia | 1.0 |
| 5ef649d7-2b36-35c8-8171-d99547c394b1 | -6.57512 | -49.5066 | 2025-07-24 04:40:00 | NPP-375D | XINGUARA | PARÁ | Brasil | 1508407 | 15 | 33 | nan | nan | nan | Amazônia | 1.5 |
| bbfb4999-24ad-34c0-8152-fefd4614ec48 | -4.54295 | -48.00852 | 2025-07-24 04:40:00 | NPP-375D | RONDON DO PARÁ | PARÁ | Brasil | 1506187 | 15 | 33 | nan | nan | nan | Amazônia | 0.5 |
| be9600b6-7ab8-31df-8122-a5ab4f86184e | -2.58706 | -51.92229 | 2025-07-24 04:40:00 | NPP-375D | SENADOR JOSÉ PORFÍRIO | PARÁ | Brasil | 1507805 | 15 | 33 | nan | nan | nan | Amazônia | 2.5 |
| b15e0bf4-6432-3514-a232-c46346e5696e | -5.55207 | -44.26103 | 2025-07-24 04:40:00 | NPP-375D | SÃO DOMINGOS DO MARANHÃO | MARANHÃO | Brasil | 2110708 | 21 | 33 | nan | nan | nan | Cerrado | 1.5 |
| f46e7a1e-1456-352b-9315-6244ce52dbd1 | -3.0561 | -47.37728 | 2025-07-24 04:40:00 | NPP-375D | PARAGOMINAS | PARÁ | Brasil | 1505502 | 15 | 33 | nan | nan | nan | Amazônia | 3.0 |
| 2afa37a5-78e7-353f-9792-1bce8fc030e7 | -7.26167 | -43.07044 | 2025-07-24 04:40:00 | NPP-375D | FLORIANO | PIAUÍ | Brasil | 2203909 | 22 | 33 | nan | nan | nan | Caatinga | 9.0 |
| 62a1ae9e-df2d-39f2-acc6-4f4d6cd82040 | -6.88919 | -44.21023 | 2025-07-24 04:40:00 | NPP-375D | NOVA IORQUE | MARANHÃO | Brasil | 2107308 | 21 | 33 | nan | nan | nan | Cerrado | 1.4 |
| a63a73d1-4cdd-3d5a-a0c9-529bd03ee5f9 | -5.90575 | -43.46609 | 2025-07-24 04:40:00 | NPP-375D | PARNARAMA | MARANHÃO | Brasil | 2107803 | 21 | 33 | nan | nan | nan | Cerrado | 1.4 |


[Clique aqui para ver as próximas entradas](README15.md)
