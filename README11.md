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

## Dados Diários - Página 11

| ID | Latitude | Longitude | Data/Hora GMT | Satélite | Município | Estado | País | Município ID | Estado ID | País ID | Dias sem Chuva | Precipitação | Risco de Fogo | Bioma | FRP |
|----|----------|-----------|---------------|----------|-----------|--------|------|--------------|-----------|---------|----------------|--------------|----------------|-------|-----|
| f0d2dcf5-3ce5-3730-bc18-84adb352ce56 | -10.58054 | -44.06431 | 2025-09-25 03:42:00 | NOAA-20 | BURITIRAMA | BAHIA | Brasil | 2904753 | 29 | 33 | nan | nan | nan | Cerrado | 1.4 |
| 0a253f2d-c079-3536-b00e-968ae3b611cf | -11.68855 | -44.3832 | 2025-09-25 03:42:00 | NOAA-20 | COTEGIPE | BAHIA | Brasil | 2909406 | 29 | 33 | nan | nan | nan | Cerrado | 1.5 |
| b62ba1cc-1490-3f38-a20b-991e52009f48 | -6.56344 | -42.06089 | 2025-09-25 03:42:00 | NOAA-20 | BARRA D'ALCÂNTARA | PIAUÍ | Brasil | 2201176 | 22 | 33 | nan | nan | nan | Caatinga | 7.8 |
| 180a7513-30ac-31b8-9a0e-f5bb40050ed5 | -10.58744 | -44.06688 | 2025-09-25 03:42:00 | NOAA-20 | BURITIRAMA | BAHIA | Brasil | 2904753 | 29 | 33 | nan | nan | nan | Cerrado | 3.0 |
| a6e85865-027a-3731-87fb-c4389b2b7687 | -11.40557 | -44.97844 | 2025-09-25 03:42:00 | NOAA-20 | RIACHÃO DAS NEVES | BAHIA | Brasil | 2926202 | 29 | 33 | nan | nan | nan | Cerrado | 1.2 |
| e0ab30b0-f039-32e6-a879-578cfd25a785 | -8.84248 | -42.99842 | 2025-09-25 03:42:00 | NOAA-20 | SÃO BRAZ DO PIAUÍ | PIAUÍ | Brasil | 2209559 | 22 | 33 | nan | nan | nan | Caatinga | 0.8 |
| f26062dc-8598-3556-a0cf-aed24903ef1d | -8.64394 | -40.39839 | 2025-09-25 03:42:00 | NOAA-20 | LAGOA GRANDE | PERNAMBUCO | Brasil | 2608750 | 26 | 33 | nan | nan | nan | Caatinga | 1.0 |
| 0aea73b7-e036-3bbe-bfd4-3c8c8c0b5407 | -12.62546 | -40.83089 | 2025-09-25 03:42:00 | NOAA-20 | IBIQUERA | BAHIA | Brasil | 2912608 | 29 | 33 | nan | nan | nan | Caatinga | 1.0 |
| e8f2fc47-0abb-3fe9-a5e9-7f5001acba60 | -8.47816 | -45.00347 | 2025-09-25 03:42:00 | NOAA-20 | BAIXA GRANDE DO RIBEIRO | PIAUÍ | Brasil | 2201150 | 22 | 33 | nan | nan | nan | Cerrado | 2.1 |
| f13fbc63-f87c-37d0-802a-80cc3301c13c | -7.04746 | -43.95878 | 2025-09-25 03:42:00 | NOAA-20 | MARCOS PARENTE | PIAUÍ | Brasil | 2206001 | 22 | 33 | nan | nan | nan | Cerrado | 1.2 |
| 94feabd2-cfc8-3be8-ae89-092129aad551 | -11.39183 | -44.95312 | 2025-09-25 03:42:00 | NOAA-20 | RIACHÃO DAS NEVES | BAHIA | Brasil | 2926202 | 29 | 33 | nan | nan | nan | Cerrado | 1.1 |
| 4015f339-39fa-36ad-9bc3-9096f0cba018 | -12.04894 | -44.83024 | 2025-09-25 03:42:00 | NOAA-20 | ANGICAL | BAHIA | Brasil | 2901403 | 29 | 33 | nan | nan | nan | Cerrado | 0.7 |
| 87b6c51f-0b2e-3e82-a65d-d130fc35fd81 | -11.79316 | -45.58339 | 2025-09-25 03:42:00 | NOAA-20 | BARREIRAS | BAHIA | Brasil | 2903201 | 29 | 33 | nan | nan | nan | Cerrado | 1.4 |
| 206784ac-19a7-3ac3-80ac-e9c90b24c0a3 | -11.41795 | -44.96909 | 2025-09-25 03:42:00 | NOAA-20 | RIACHÃO DAS NEVES | BAHIA | Brasil | 2926202 | 29 | 33 | nan | nan | nan | Cerrado | 2.4 |
| c398320d-bddc-34bb-9fdb-40f4b4fff5f3 | -7.048 | -43.95568 | 2025-09-25 03:42:00 | NOAA-20 | MARCOS PARENTE | PIAUÍ | Brasil | 2206001 | 22 | 33 | nan | nan | nan | Cerrado | 1.2 |
| 65a68762-bfae-3e59-a418-da06b4fbcffb | -7.9862 | -43.58641 | 2025-09-25 03:42:00 | NOAA-20 | ELISEU MARTINS | PIAUÍ | Brasil | 2203602 | 22 | 33 | nan | nan | nan | Cerrado | 2.3 |
| f870f577-2fe8-3df7-9ac5-db35c3820659 | -9.05663 | -40.52593 | 2025-09-25 03:42:00 | NOAA-20 | PETROLINA | PERNAMBUCO | Brasil | 2611101 | 26 | 33 | nan | nan | nan | Caatinga | 2.6 |
| 02d68454-d8c0-3b48-ab5c-7b3ac9542dd7 | -9.30484 | -40.63107 | 2025-09-25 03:42:00 | NOAA-20 | PETROLINA | PERNAMBUCO | Brasil | 2611101 | 26 | 33 | nan | nan | nan | Caatinga | 1.1 |
| 2dfd92bd-44eb-344d-8101-cfaf77fb730b | -6.72628 | -43.97645 | 2025-09-25 03:42:00 | NOAA-20 | NOVA IORQUE | MARANHÃO | Brasil | 2107308 | 21 | 33 | nan | nan | nan | Cerrado | 1.3 |
| ff920167-01d3-32b3-948f-0e43d4cbbd67 | -6.59278 | -44.61986 | 2025-09-25 03:42:00 | NOAA-20 | MIRADOR | MARANHÃO | Brasil | 2106706 | 21 | 33 | nan | nan | nan | Cerrado | 4.1 |
| a505ca37-4be9-3181-a971-428d47a9078c | -10.18967 | -44.84543 | 2025-09-25 03:42:00 | NOAA-20 | RIACHO FRIO | PIAUÍ | Brasil | 2208858 | 22 | 33 | nan | nan | nan | Cerrado | 1.0 |
| 31a4a1a6-d6bb-3e3d-a6df-4a5693b3b7f7 | -10.10797 | -45.31389 | 2025-09-25 03:42:00 | NOAA-20 | SÃO GONÇALO DO GURGUÉIA | PIAUÍ | Brasil | 2209757 | 22 | 33 | nan | nan | nan | Cerrado | 1.3 |
| 39b55772-f582-31ff-a96d-3ba0b971542e | -12.05395 | -44.83113 | 2025-09-25 03:42:00 | NOAA-20 | ANGICAL | BAHIA | Brasil | 2901403 | 29 | 33 | nan | nan | nan | Cerrado | 1.0 |
| 7246518d-b70a-38e0-bb12-90ea4f75eb1a | -11.53533 | -43.64562 | 2025-09-25 03:42:00 | NOAA-20 | BARRA | BAHIA | Brasil | 2902708 | 29 | 33 | nan | nan | nan | Cerrado | 3.2 |
| cfadf91b-8e2e-37a5-84d6-997c6a6a6101 | -8.49052 | -45.01624 | 2025-09-25 03:42:00 | NOAA-20 | BAIXA GRANDE DO RIBEIRO | PIAUÍ | Brasil | 2201150 | 22 | 33 | nan | nan | nan | Cerrado | 1.8 |
| 0ab350e0-3549-3f26-b4b2-1ddc025a701a | -11.39633 | -44.95734 | 2025-09-25 03:42:00 | NOAA-20 | RIACHÃO DAS NEVES | BAHIA | Brasil | 2926202 | 29 | 33 | nan | nan | nan | Cerrado | 1.1 |
| c57a6560-8c11-36da-8abd-1aef365977ef | -8.19713 | -43.59545 | 2025-09-25 03:42:00 | NOAA-20 | COLÔNIA DO GURGUÉIA | PIAUÍ | Brasil | 2202752 | 22 | 33 | nan | nan | nan | Cerrado | 2.9 |
| 5b9cb3d2-15f1-3030-bd67-38a8c30a5106 | -6.42504 | -43.09465 | 2025-09-25 03:42:00 | NOAA-20 | SÃO FRANCISCO DO MARANHÃO | MARANHÃO | Brasil | 2110906 | 21 | 33 | nan | nan | nan | Cerrado | 27.8 |
| 3756bfbf-a81c-39b4-8b77-1005c34c8fc1 | -6.56719 | -42.06646 | 2025-09-25 03:42:00 | NOAA-20 | BARRA D'ALCÂNTARA | PIAUÍ | Brasil | 2201176 | 22 | 33 | nan | nan | nan | Caatinga | 11.8 |
| 902bdecd-c207-3b0b-aa98-b8e3b5dd9785 | -6.59762 | -44.62418 | 2025-09-25 03:42:00 | NOAA-20 | MIRADOR | MARANHÃO | Brasil | 2106706 | 21 | 33 | nan | nan | nan | Cerrado | 1.3 |
| 68b323f9-63e5-3b6e-925f-332a6fcc0653 | -12.0658 | -44.85098 | 2025-09-25 03:42:00 | NOAA-20 | ANGICAL | BAHIA | Brasil | 2901403 | 29 | 33 | nan | nan | nan | Cerrado | 1.4 |
| 0782f368-534e-32bd-b693-0e71ddd094ef | -10.59028 | -44.06623 | 2025-09-25 03:42:00 | NOAA-20 | BURITIRAMA | BAHIA | Brasil | 2904753 | 29 | 33 | nan | nan | nan | Cerrado | 0.7 |
| 6cb27810-894f-3ea5-9a42-9acd9c0758d2 | -11.40264 | -44.96619 | 2025-09-25 03:42:00 | NOAA-20 | RIACHÃO DAS NEVES | BAHIA | Brasil | 2926202 | 29 | 33 | nan | nan | nan | Cerrado | 2.7 |
| 5f2140cb-ed5a-3715-a9c0-d1c43f0ad322 | -11.41847 | -44.96638 | 2025-09-25 03:42:00 | NOAA-20 | RIACHÃO DAS NEVES | BAHIA | Brasil | 2926202 | 29 | 33 | nan | nan | nan | Cerrado | 2.4 |
| 1ed13eea-40d9-3afb-885c-ea10631725ab | -10.43628 | -44.23403 | 2025-09-25 03:42:00 | NOAA-20 | JÚLIO BORGES | PIAUÍ | Brasil | 2205524 | 22 | 33 | nan | nan | nan | Cerrado | 3.3 |
| 9e2e8dd1-78ee-38af-aa32-1834f28e7000 | -7.29496 | -43.91273 | 2025-09-25 03:42:00 | NOAA-20 | LANDRI SALES | PIAUÍ | Brasil | 2205607 | 22 | 33 | nan | nan | nan | Cerrado | 2.0 |
| 52b24927-7854-3bd8-9e07-09971ca5cd2c | -11.80101 | -45.57084 | 2025-09-25 03:42:00 | NOAA-20 | BARREIRAS | BAHIA | Brasil | 2903201 | 29 | 33 | nan | nan | nan | Cerrado | 0.9 |
| 0194e4fb-efeb-35cd-9161-4be8c97c7133 | -11.66766 | -44.41375 | 2025-09-25 03:42:00 | NOAA-20 | COTEGIPE | BAHIA | Brasil | 2909406 | 29 | 33 | nan | nan | nan | Cerrado | 2.4 |
| 8383e567-b5f2-3706-8a6a-2252fe7280f9 | -10.5873 | -44.08275 | 2025-09-25 03:42:00 | NOAA-20 | JÚLIO BORGES | PIAUÍ | Brasil | 2205524 | 22 | 33 | nan | nan | nan | Cerrado | 2.1 |
| 87cde80b-8ea4-38b3-87f4-cbf3e8069eed | -10.08388 | -45.26558 | 2025-09-25 03:42:00 | NOAA-20 | SÃO GONÇALO DO GURGUÉIA | PIAUÍ | Brasil | 2209757 | 22 | 33 | nan | nan | nan | Cerrado | 1.4 |
| be236fe8-440a-329c-9320-f90d498d2582 | -6.41805 | -43.07648 | 2025-09-25 03:42:00 | NOAA-20 | SÃO FRANCISCO DO MARANHÃO | MARANHÃO | Brasil | 2110906 | 21 | 33 | nan | nan | nan | Cerrado | 24.9 |
| 3d869dcb-e6ec-3b30-9eb2-00ff7734bdb1 | -11.90913 | -44.77752 | 2025-09-25 03:42:00 | NOAA-20 | ANGICAL | BAHIA | Brasil | 2901403 | 29 | 33 | nan | nan | nan | Cerrado | 3.6 |
| 326bed62-9c8f-3653-9803-3a5a97b6be1a | -7.26212 | -43.02396 | 2025-09-25 03:42:00 | NOAA-20 | FLORIANO | PIAUÍ | Brasil | 2203909 | 22 | 33 | nan | nan | nan | Caatinga | 3.2 |
| a523d830-58e4-324c-ae2d-e1098dc88c14 | -11.7938 | -45.58001 | 2025-09-25 03:42:00 | NOAA-20 | BARREIRAS | BAHIA | Brasil | 2903201 | 29 | 33 | nan | nan | nan | Cerrado | 1.4 |
| 46551fce-db99-3d01-8229-222eb319e760 | -6.82176 | -43.18349 | 2025-09-25 03:42:00 | NOAA-20 | FLORIANO | PIAUÍ | Brasil | 2203909 | 22 | 33 | nan | nan | nan | Caatinga | 2.8 |
| daa2d482-aef2-3ba8-88ab-ef685aedf28f | -8.2969 | -44.93595 | 2025-09-25 03:42:00 | NOAA-20 | BAIXA GRANDE DO RIBEIRO | PIAUÍ | Brasil | 2201150 | 22 | 33 | nan | nan | nan | Cerrado | 1.3 |
| 591e7d39-9361-3b4e-b01b-d5ffdb4d4b9c | -8.68931 | -44.03382 | 2025-09-25 03:42:00 | NOAA-20 | CRISTINO CASTRO | PIAUÍ | Brasil | 2203107 | 22 | 33 | nan | nan | nan | Cerrado | 1.2 |
| 9dac3693-f148-3cc6-96b0-243840fa17fa | -8.28733 | -44.95758 | 2025-09-25 03:42:00 | NOAA-20 | BAIXA GRANDE DO RIBEIRO | PIAUÍ | Brasil | 2201150 | 22 | 33 | nan | nan | nan | Cerrado | 3.9 |
| 7a118f08-e11b-3c20-8e86-5dcbd144853d | -11.61616 | -44.44432 | 2025-09-25 03:42:00 | NOAA-20 | COTEGIPE | BAHIA | Brasil | 2909406 | 29 | 33 | nan | nan | nan | Cerrado | 2.2 |
| 3ee0a3f0-ac72-3386-9fed-27d31bdb05b5 | -7.59527 | -42.33042 | 2025-09-25 03:42:00 | NOAA-20 | SÃO MIGUEL DO FIDALGO | PIAUÍ | Brasil | 2210391 | 22 | 33 | nan | nan | nan | Caatinga | 2.0 |
| 3d7c4a4f-d1b6-357c-b019-438ee68f32d6 | -11.4019 | -44.95585 | 2025-09-25 03:42:00 | NOAA-20 | RIACHÃO DAS NEVES | BAHIA | Brasil | 2926202 | 29 | 33 | nan | nan | nan | Cerrado | 1.3 |
| 67a44548-9e6a-36a4-88e5-342a67cabdb0 | -12.06909 | -44.86119 | 2025-09-25 03:42:00 | NOAA-20 | ANGICAL | BAHIA | Brasil | 2901403 | 29 | 33 | nan | nan | nan | Cerrado | 0.9 |
| 255daca6-4062-347e-a81a-80ae33180854 | -11.92818 | -38.32777 | 2025-09-25 03:42:00 | NOAA-20 | INHAMBUPE | BAHIA | Brasil | 2913705 | 29 | 33 | nan | nan | nan | Mata Atlântica | 5.1 |
| 6d886e05-d23d-3041-a21e-b000f4cbbdea | -11.68808 | -44.33146 | 2025-09-25 03:42:00 | NOAA-20 | COTEGIPE | BAHIA | Brasil | 2909406 | 29 | 33 | nan | nan | nan | Cerrado | 2.1 |
| 92e6ca25-f416-35f3-ab32-c9a260750359 | -7.09958 | -44.09568 | 2025-09-25 03:42:00 | NOAA-20 | PORTO ALEGRE DO PIAUÍ | PIAUÍ | Brasil | 2208551 | 22 | 33 | nan | nan | nan | Cerrado | 4.1 |
| 9395a685-3d5f-3272-a464-f623a720aeb7 | -11.01839 | -45.91439 | 2025-09-25 03:42:00 | NOAA-20 | FORMOSA DO RIO PRETO | BAHIA | Brasil | 2911105 | 29 | 33 | nan | nan | nan | Cerrado | 1.0 |
| 2d9414f7-e434-30b4-8897-158dca348223 | -11.41686 | -44.97477 | 2025-09-25 03:42:00 | NOAA-20 | RIACHÃO DAS NEVES | BAHIA | Brasil | 2926202 | 29 | 33 | nan | nan | nan | Cerrado | 2.5 |
| 5a6a55cd-a307-3eac-9300-073864071bab | -11.39581 | -44.96014 | 2025-09-25 03:42:00 | NOAA-20 | RIACHÃO DAS NEVES | BAHIA | Brasil | 2926202 | 29 | 33 | nan | nan | nan | Cerrado | 1.2 |
| 67c6c1de-4775-3c06-9a9b-53695e0b772d | -6.40091 | -43.52983 | 2025-09-25 03:42:00 | NOAA-20 | SUCUPIRA DO RIACHÃO | MARANHÃO | Brasil | 2111953 | 21 | 33 | nan | nan | nan | Cerrado | 1.2 |
| a5b2bd7b-2e8f-3065-85f1-c2b7ea87f0a2 | -8.49412 | -45.0075 | 2025-09-25 03:42:00 | NOAA-20 | BAIXA GRANDE DO RIBEIRO | PIAUÍ | Brasil | 2201150 | 22 | 33 | nan | nan | nan | Cerrado | 1.6 |
| a890b2f1-2885-306d-949d-5edae65d4439 | -6.73649 | -43.16811 | 2025-09-25 03:42:00 | NOAA-20 | BARÃO DE GRAJAÚ | MARANHÃO | Brasil | 2101509 | 21 | 33 | nan | nan | nan | Caatinga | 3.1 |
| fc7c2167-7d8c-3bd7-8926-1391a764ed9b | -10.59218 | -44.08371 | 2025-09-25 03:42:00 | NOAA-20 | MANSIDÃO | BAHIA | Brasil | 2920452 | 29 | 33 | nan | nan | nan | Cerrado | 2.1 |
| f376ff85-e2c2-31cd-9815-86084115c623 | -8.47514 | -45.00884 | 2025-09-25 03:42:00 | NOAA-20 | BAIXA GRANDE DO RIBEIRO | PIAUÍ | Brasil | 2201150 | 22 | 33 | nan | nan | nan | Cerrado | 3.3 |
| 4ce52014-36f1-30bc-811e-140459b7b05c | -12.05952 | -44.82904 | 2025-09-25 03:42:00 | NOAA-20 | ANGICAL | BAHIA | Brasil | 2901403 | 29 | 33 | nan | nan | nan | Cerrado | 0.8 |
| 572271e7-4ae1-3a21-864b-2a37f63b0d67 | -6.72111 | -43.97541 | 2025-09-25 03:42:00 | NOAA-20 | NOVA IORQUE | MARANHÃO | Brasil | 2107308 | 21 | 33 | nan | nan | nan | Cerrado | 1.7 |
| 9e1c2777-e4de-3118-8168-6053c85403e6 | -6.68962 | -44.61763 | 2025-09-25 03:42:00 | NOAA-20 | SÃO DOMINGOS DO AZEITÃO | MARANHÃO | Brasil | 2110658 | 21 | 33 | nan | nan | nan | Cerrado | 1.7 |
| 0057b45a-159a-379e-98c4-1c1f09793427 | -11.64248 | -45.35045 | 2025-09-25 03:42:00 | NOAA-20 | RIACHÃO DAS NEVES | BAHIA | Brasil | 2926202 | 29 | 33 | nan | nan | nan | Cerrado | 1.3 |
| 756fa098-55ee-369d-b468-6b385380fd09 | -11.68752 | -44.38877 | 2025-09-25 03:42:00 | NOAA-20 | COTEGIPE | BAHIA | Brasil | 2909406 | 29 | 33 | nan | nan | nan | Cerrado | 1.6 |
| 4f969c86-03db-3608-9ba7-0a1b60866742 | -10.5892 | -44.08431 | 2025-09-25 03:42:00 | NOAA-20 | JÚLIO BORGES | PIAUÍ | Brasil | 2205524 | 22 | 33 | nan | nan | nan | Cerrado | 1.8 |
| 2026962a-fe82-32cc-9c26-7d3b49aeb716 | -7.14681 | -43.53255 | 2025-09-25 03:42:00 | NOAA-20 | JERUMENHA | PIAUÍ | Brasil | 2205300 | 22 | 33 | nan | nan | nan | Cerrado | 0.7 |
| 342b85d8-430b-34e5-87e2-bf0b19e6dd04 | -8.12908 | -44.14131 | 2025-09-25 03:42:00 | NOAA-20 | SEBASTIÃO LEAL | PIAUÍ | Brasil | 2210631 | 22 | 33 | nan | nan | nan | Cerrado | 0.9 |
| 3b7f2b0f-958f-32e0-af3f-1258f65570d8 | -11.61378 | -44.3386 | 2025-09-25 03:42:00 | NOAA-20 | COTEGIPE | BAHIA | Brasil | 2909406 | 29 | 33 | nan | nan | nan | Cerrado | 2.7 |
| 14ad4e04-867f-3c6f-bd32-de5728668ac7 | -11.40843 | -44.97769 | 2025-09-25 03:42:00 | NOAA-20 | RIACHÃO DAS NEVES | BAHIA | Brasil | 2926202 | 29 | 33 | nan | nan | nan | Cerrado | 1.3 |
| 474439b5-7340-320b-a370-cf98e92518a4 | -8.28651 | -44.95086 | 2025-09-25 03:42:00 | NOAA-20 | BAIXA GRANDE DO RIBEIRO | PIAUÍ | Brasil | 2201150 | 22 | 33 | nan | nan | nan | Cerrado | 2.7 |
| c7b97bb6-4cd7-32b1-89e0-d11b371a6f93 | -6.42789 | -43.07801 | 2025-09-25 03:42:00 | NOAA-20 | SÃO FRANCISCO DO MARANHÃO | MARANHÃO | Brasil | 2110906 | 21 | 33 | nan | nan | nan | Cerrado | 31.4 |
| c386417c-af8c-38fd-9009-d390071b789b | -6.74947 | -44.63641 | 2025-09-25 03:42:00 | NOAA-20 | SÃO DOMINGOS DO AZEITÃO | MARANHÃO | Brasil | 2110658 | 21 | 33 | nan | nan | nan | Cerrado | 6.3 |
| 0f428df9-c040-325a-a465-407f111dabb8 | -12.07404 | -44.86248 | 2025-09-25 03:42:00 | NOAA-20 | ANGICAL | BAHIA | Brasil | 2901403 | 29 | 33 | nan | nan | nan | Cerrado | 0.9 |
| 74ab857e-9ba9-38a3-b444-b37ed170a220 | -11.69344 | -44.38416 | 2025-09-25 03:42:00 | NOAA-20 | COTEGIPE | BAHIA | Brasil | 2909406 | 29 | 33 | nan | nan | nan | Cerrado | 1.7 |
| bf58e95d-babb-36f6-94f6-e77f1b737ccb | -11.78723 | -45.58579 | 2025-09-25 03:42:00 | NOAA-20 | RIACHÃO DAS NEVES | BAHIA | Brasil | 2926202 | 29 | 33 | nan | nan | nan | Cerrado | 1.3 |
| d922f880-dbf2-34ff-a3db-250941499e65 | -7.22539 | -45.17671 | 2025-09-25 03:42:00 | NOAA-20 | LORETO | MARANHÃO | Brasil | 2106102 | 21 | 33 | nan | nan | nan | Cerrado | 1.9 |
| e75de11c-7c8c-3f74-bb03-22a52a640494 | -8.49113 | -45.01281 | 2025-09-25 03:42:00 | NOAA-20 | BAIXA GRANDE DO RIBEIRO | PIAUÍ | Brasil | 2201150 | 22 | 33 | nan | nan | nan | Cerrado | 1.8 |
| 31507c94-d27d-31db-9ec7-6bd6ee267cc6 | -8.28594 | -44.9541 | 2025-09-25 03:42:00 | NOAA-20 | BAIXA GRANDE DO RIBEIRO | PIAUÍ | Brasil | 2201150 | 22 | 33 | nan | nan | nan | Cerrado | 2.7 |
| 88fe7bc8-8c35-32eb-8e70-bc85ab00d5bd | -10.11059 | -45.3296 | 2025-09-25 03:42:00 | NOAA-20 | SÃO GONÇALO DO GURGUÉIA | PIAUÍ | Brasil | 2209757 | 22 | 33 | nan | nan | nan | Cerrado | 1.6 |
| 194868ad-81ab-39b9-9f32-a36a0851f2e7 | -8.84698 | -42.47697 | 2025-09-25 03:42:00 | NOAA-20 | CORONEL JOSÉ DIAS | PIAUÍ | Brasil | 2202851 | 22 | 33 | nan | nan | nan | Caatinga | 10.3 |
| cfac881e-f8e2-3cb0-af36-2fac2dc1e012 | -11.78513 | -45.56812 | 2025-09-25 03:42:00 | NOAA-20 | BARREIRAS | BAHIA | Brasil | 2903201 | 29 | 33 | nan | nan | nan | Cerrado | 1.3 |
| 743ad4a9-b56f-344e-9257-bcf1ce7ce4ae | -8.47748 | -45.00709 | 2025-09-25 03:42:00 | NOAA-20 | BAIXA GRANDE DO RIBEIRO | PIAUÍ | Brasil | 2201150 | 22 | 33 | nan | nan | nan | Cerrado | 1.5 |
| a82a35df-cd8e-3733-b093-55618a1e34ef | -6.33167 | -44.01335 | 2025-09-25 03:42:00 | NOAA-20 | PARAIBANO | MARANHÃO | Brasil | 2107704 | 21 | 33 | nan | nan | nan | Cerrado | 2.7 |
| a920d06c-2211-34e8-8c29-2d1f37d3c626 | -11.928 | -38.32745 | 2025-09-25 03:42:00 | NOAA-20 | INHAMBUPE | BAHIA | Brasil | 2913705 | 29 | 33 | nan | nan | nan | Mata Atlântica | 3.7 |
| 8c315021-5d5c-3525-b4d4-1e82868eae89 | -11.40896 | -44.97481 | 2025-09-25 03:42:00 | NOAA-20 | RIACHÃO DAS NEVES | BAHIA | Brasil | 2926202 | 29 | 33 | nan | nan | nan | Cerrado | 1.3 |
| ac3b99e9-8e8c-3855-827d-89347bba3284 | -12.06687 | -44.84521 | 2025-09-25 03:42:00 | NOAA-20 | ANGICAL | BAHIA | Brasil | 2901403 | 29 | 33 | nan | nan | nan | Cerrado | 1.1 |
| 54bee872-9010-3d22-83ec-bf030c3bf914 | -10.15822 | -36.18683 | 2025-09-25 03:42:00 | NOAA-20 | CORURIPE | ALAGOAS | Brasil | 2702306 | 27 | 33 | nan | nan | nan | Mata Atlântica | 7.7 |
| 5e909d1c-8882-34c3-a313-1d83ab995102 | -11.63723 | -45.34961 | 2025-09-25 03:42:00 | NOAA-20 | RIACHÃO DAS NEVES | BAHIA | Brasil | 2926202 | 29 | 33 | nan | nan | nan | Cerrado | 1.0 |
| 58c0999f-a52e-3b9b-a533-f64ddc37b3d6 | -6.75011 | -44.63289 | 2025-09-25 03:42:00 | NOAA-20 | SÃO DOMINGOS DO AZEITÃO | MARANHÃO | Brasil | 2110658 | 21 | 33 | nan | nan | nan | Cerrado | 6.3 |
| fe19bda8-7278-3e07-866c-2dfd2a32d6c7 | -8.4948 | -45.00381 | 2025-09-25 03:42:00 | NOAA-20 | BAIXA GRANDE DO RIBEIRO | PIAUÍ | Brasil | 2201150 | 22 | 33 | nan | nan | nan | Cerrado | 1.6 |
| ec3d3d0d-e144-3d29-a319-7d36f059a9bc | -11.41742 | -44.97187 | 2025-09-25 03:42:00 | NOAA-20 | RIACHÃO DAS NEVES | BAHIA | Brasil | 2926202 | 29 | 33 | nan | nan | nan | Cerrado | 2.5 |
| 007ed588-629b-3931-b145-6a0cbb6c0c46 | -12.10032 | -45.79038 | 2025-09-25 03:42:00 | NOAA-20 | LUÍS EDUARDO MAGALHÃES | BAHIA | Brasil | 2919553 | 29 | 33 | nan | nan | nan | Cerrado | 0.8 |
| 2fc3c7f3-6e36-3833-9f2e-5c4b44c7c168 | -11.92756 | -38.33156 | 2025-09-25 03:42:00 | NOAA-20 | INHAMBUPE | BAHIA | Brasil | 2913705 | 29 | 33 | nan | nan | nan | Caatinga | 2.6 |
| d3622940-5f69-3cb4-8a2e-b0899143137b | -11.9108 | -44.76875 | 2025-09-25 03:42:00 | NOAA-20 | ANGICAL | BAHIA | Brasil | 2901403 | 29 | 33 | nan | nan | nan | Cerrado | 1.6 |
| ae45be3d-da95-3fe6-9bc5-0dec385b2dcc | -11.78557 | -44.9116 | 2025-09-25 03:42:00 | NOAA-20 | RIACHÃO DAS NEVES | BAHIA | Brasil | 2926202 | 29 | 33 | nan | nan | nan | Cerrado | 1.0 |
| 35a685f9-a28e-3f6a-bb26-0f10dc9e4512 | -11.60526 | -44.44804 | 2025-09-25 03:42:00 | NOAA-20 | COTEGIPE | BAHIA | Brasil | 2909406 | 29 | 33 | nan | nan | nan | Cerrado | 1.2 |


[Clique aqui para ver as próximas entradas](README12.md)
