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

## Dados Diários - Página 101

| ID | Latitude | Longitude | Data/Hora GMT | Satélite | Município | Estado | País | Município ID | Estado ID | País ID | Dias sem Chuva | Precipitação | Risco de Fogo | Bioma | FRP |
|----|----------|-----------|---------------|----------|-----------|--------|------|--------------|-----------|---------|----------------|--------------|----------------|-------|-----|
| c7cc9c86-25a8-3785-89f3-e4f1e007803f | -18.08753 | -57.33928 | 2024-10-24 05:23:00 | NOAA-20 | CORUMBÁ | MATO GROSSO DO SUL | Brasil | 5003207 | 50 | 33 | nan | nan | nan | Pantanal | 5.1 |
| 22ee7a5f-89bc-3588-90a0-2d930e3a20ca | -18.08716 | -57.33999 | 2024-10-24 05:23:00 | NOAA-20 | CORUMBÁ | MATO GROSSO DO SUL | Brasil | 5003207 | 50 | 33 | nan | nan | nan | Pantanal | 4.5 |
| a5ff948b-f186-30c5-a07e-1f39857f94e3 | -18.08716 | -57.30688 | 2024-10-24 05:23:00 | NOAA-20 | CORUMBÁ | MATO GROSSO DO SUL | Brasil | 5003207 | 50 | 33 | nan | nan | nan | Pantanal | 2.1 |
| 9379e51e-e361-3931-ab5a-0d2c20e95f03 | -18.0863 | -57.31425 | 2024-10-24 05:23:00 | NOAA-20 | CORUMBÁ | MATO GROSSO DO SUL | Brasil | 5003207 | 50 | 33 | nan | nan | nan | Pantanal | 1.2 |
| eb8d12ad-69f8-3313-a934-ee121ad5f0cb | -18.08407 | -57.29731 | 2024-10-24 05:23:00 | NOAA-20 | CORUMBÁ | MATO GROSSO DO SUL | Brasil | 5003207 | 50 | 33 | nan | nan | nan | Pantanal | 3.6 |
| 3bc45a9b-5da7-3583-8e95-be11166ac4c0 | -18.08399 | -57.29813 | 2024-10-24 05:23:00 | NOAA-20 | CORUMBÁ | MATO GROSSO DO SUL | Brasil | 5003207 | 50 | 33 | nan | nan | nan | Pantanal | 6.6 |
| 7a1be615-e915-3a3e-a104-79bc0f4a98de | -18.08357 | -57.30141 | 2024-10-24 05:23:00 | NOAA-20 | CORUMBÁ | MATO GROSSO DO SUL | Brasil | 5003207 | 50 | 33 | nan | nan | nan | Pantanal | 4.7 |
| 8deb06e6-45ed-346c-a894-f381f0cda788 | -18.08346 | -57.30222 | 2024-10-24 05:23:00 | NOAA-20 | CORUMBÁ | MATO GROSSO DO SUL | Brasil | 5003207 | 50 | 33 | nan | nan | nan | Pantanal | 3.4 |
| 246341da-2d79-34db-9f9e-e8ef170f1069 | -18.08331 | -57.3387 | 2024-10-24 05:23:00 | NOAA-20 | CORUMBÁ | MATO GROSSO DO SUL | Brasil | 5003207 | 50 | 33 | nan | nan | nan | Pantanal | 5.3 |
| 35d3b830-2d1d-38f7-ab4e-3e5528f90e3c | -18.08307 | -57.3055 | 2024-10-24 05:23:00 | NOAA-20 | CORUMBÁ | MATO GROSSO DO SUL | Brasil | 5003207 | 50 | 33 | nan | nan | nan | Pantanal | 4.7 |
| 53a93ea5-905d-3382-a756-5720d14af94d | -18.08294 | -57.33941 | 2024-10-24 05:23:00 | NOAA-20 | CORUMBÁ | MATO GROSSO DO SUL | Brasil | 5003207 | 50 | 33 | nan | nan | nan | Pantanal | 4.5 |
| b551407d-decc-35ea-aa63-9adb1f78085a | -18.08293 | -57.3063 | 2024-10-24 05:23:00 | NOAA-20 | CORUMBÁ | MATO GROSSO DO SUL | Brasil | 5003207 | 50 | 33 | nan | nan | nan | Pantanal | 3.4 |
| f02de3f0-9d50-333b-b55f-61e3a5118928 | -18.08257 | -57.30959 | 2024-10-24 05:23:00 | NOAA-20 | CORUMBÁ | MATO GROSSO DO SUL | Brasil | 5003207 | 50 | 33 | nan | nan | nan | Pantanal | 1.2 |
| bc121b27-c10f-3740-8513-1a4e3b87202c | -18.0824 | -57.31038 | 2024-10-24 05:23:00 | NOAA-20 | CORUMBÁ | MATO GROSSO DO SUL | Brasil | 5003207 | 50 | 33 | nan | nan | nan | Pantanal | 1.8 |
| 63fba27d-2ccf-3239-ae6e-d8369f54bdc4 | -18.08207 | -57.31368 | 2024-10-24 05:23:00 | NOAA-20 | CORUMBÁ | MATO GROSSO DO SUL | Brasil | 5003207 | 50 | 33 | nan | nan | nan | Pantanal | 1.2 |
| 64665981-cf25-3e4c-bd83-d1bc028bf558 | -18.07923 | -57.30164 | 2024-10-24 05:23:00 | NOAA-20 | CORUMBÁ | MATO GROSSO DO SUL | Brasil | 5003207 | 50 | 33 | nan | nan | nan | Pantanal | 3.4 |
| 7ddad98a-4bc2-3009-b55e-09e900d66e7b | -18.0787 | -57.30573 | 2024-10-24 05:23:00 | NOAA-20 | CORUMBÁ | MATO GROSSO DO SUL | Brasil | 5003207 | 50 | 33 | nan | nan | nan | Pantanal | 3.4 |
| cb574879-3e7c-3486-8d60-b67a8cc75a31 | -18.0786 | -57.34218 | 2024-10-24 05:23:00 | NOAA-20 | CORUMBÁ | MATO GROSSO DO SUL | Brasil | 5003207 | 50 | 33 | nan | nan | nan | Pantanal | 4.0 |
| bad2600f-9f62-3bb6-8d46-bde6c6dfa456 | -18.0782 | -57.3429 | 2024-10-24 05:23:00 | NOAA-20 | CORUMBÁ | MATO GROSSO DO SUL | Brasil | 5003207 | 50 | 33 | nan | nan | nan | Pantanal | 4.9 |
| fe901237-7123-35af-8dd6-78b116b89bca | -18.07818 | -57.3098 | 2024-10-24 05:23:00 | NOAA-20 | CORUMBÁ | MATO GROSSO DO SUL | Brasil | 5003207 | 50 | 33 | nan | nan | nan | Pantanal | 1.8 |
| 02f4541d-d1cf-3715-8b36-5d2d2eae86e9 | -18.07765 | -57.31387 | 2024-10-24 05:23:00 | NOAA-20 | CORUMBÁ | MATO GROSSO DO SUL | Brasil | 5003207 | 50 | 33 | nan | nan | nan | Pantanal | 1.8 |
| 2e1f9614-0b85-37fd-8010-9c7f49e114b0 | -18.07447 | -57.30515 | 2024-10-24 05:23:00 | NOAA-20 | CORUMBÁ | MATO GROSSO DO SUL | Brasil | 5003207 | 50 | 33 | nan | nan | nan | Pantanal | 4.4 |
| e75962da-ccde-3ba7-a993-cda4d34aae5b | -18.07399 | -57.34231 | 2024-10-24 05:23:00 | NOAA-20 | CORUMBÁ | MATO GROSSO DO SUL | Brasil | 5003207 | 50 | 33 | nan | nan | nan | Pantanal | 4.9 |
| 5526aca7-cf1a-3c0f-ba14-8e78251013a2 | -18.07395 | -57.30922 | 2024-10-24 05:23:00 | NOAA-20 | CORUMBÁ | MATO GROSSO DO SUL | Brasil | 5003207 | 50 | 33 | nan | nan | nan | Pantanal | 3.5 |
| 39845a49-3038-3455-8588-7ea85bf787b3 | -18.07343 | -57.31329 | 2024-10-24 05:23:00 | NOAA-20 | CORUMBÁ | MATO GROSSO DO SUL | Brasil | 5003207 | 50 | 33 | nan | nan | nan | Pantanal | 3.5 |
| cfc14c0b-a73a-304a-a5e3-bf42036a1008 | -18.0729 | -57.31737 | 2024-10-24 05:23:00 | NOAA-20 | CORUMBÁ | MATO GROSSO DO SUL | Brasil | 5003207 | 50 | 33 | nan | nan | nan | Pantanal | 2.1 |
| cf1e4fac-9260-3a3d-9497-8f4746344be1 | -18.07238 | -57.32144 | 2024-10-24 05:23:00 | NOAA-20 | CORUMBÁ | MATO GROSSO DO SUL | Brasil | 5003207 | 50 | 33 | nan | nan | nan | Pantanal | 2.1 |
| 2385678d-1e1f-3191-b306-d3fb75049d23 | -18.07186 | -57.3255 | 2024-10-24 05:23:00 | NOAA-20 | CORUMBÁ | MATO GROSSO DO SUL | Brasil | 5003207 | 50 | 33 | nan | nan | nan | Pantanal | 1.7 |
| f779c9f0-2f32-369b-bd64-217e2f98479d | -18.07025 | -57.30456 | 2024-10-24 05:23:00 | NOAA-20 | CORUMBÁ | MATO GROSSO DO SUL | Brasil | 5003207 | 50 | 33 | nan | nan | nan | Pantanal | 4.4 |
| ba102e29-ed76-3ab2-938b-bf1c701a18a7 | -18.06977 | -57.34174 | 2024-10-24 05:23:00 | NOAA-20 | CORUMBÁ | MATO GROSSO DO SUL | Brasil | 5003207 | 50 | 33 | nan | nan | nan | Pantanal | 2.3 |
| 49459835-982b-378d-9085-5af47e550bb6 | -18.06973 | -57.30864 | 2024-10-24 05:23:00 | NOAA-20 | CORUMBÁ | MATO GROSSO DO SUL | Brasil | 5003207 | 50 | 33 | nan | nan | nan | Pantanal | 3.5 |
| c730881e-1024-3ca1-8a65-a00cae76ae2e | -18.06868 | -57.31678 | 2024-10-24 05:23:00 | NOAA-20 | CORUMBÁ | MATO GROSSO DO SUL | Brasil | 5003207 | 50 | 33 | nan | nan | nan | Pantanal | 2.1 |
| 9e6ae80e-ca9e-3015-9113-1e1bae229014 | -18.06816 | -57.32085 | 2024-10-24 05:23:00 | NOAA-20 | CORUMBÁ | MATO GROSSO DO SUL | Brasil | 5003207 | 50 | 33 | nan | nan | nan | Pantanal | 2.1 |
| a18feae9-2c33-39ff-9f6b-e113bf2c2050 | -18.06764 | -57.32492 | 2024-10-24 05:23:00 | NOAA-20 | CORUMBÁ | MATO GROSSO DO SUL | Brasil | 5003207 | 50 | 33 | nan | nan | nan | Pantanal | 1.7 |
| fe00548c-21ad-3cf6-bcc6-0b665d36dd44 | -18.06498 | -57.31214 | 2024-10-24 05:23:00 | NOAA-20 | CORUMBÁ | MATO GROSSO DO SUL | Brasil | 5003207 | 50 | 33 | nan | nan | nan | Pantanal | 2.1 |
| 2789c786-4b75-38f5-9664-dcd6661ad673 | -18.06023 | -57.31562 | 2024-10-24 05:23:00 | NOAA-20 | CORUMBÁ | MATO GROSSO DO SUL | Brasil | 5003207 | 50 | 33 | nan | nan | nan | Pantanal | 3.8 |
| b0d105e2-eb9e-381d-8951-b3b16574e6db | -18.05601 | -57.31506 | 2024-10-24 05:23:00 | NOAA-20 | CORUMBÁ | MATO GROSSO DO SUL | Brasil | 5003207 | 50 | 33 | nan | nan | nan | Pantanal | 1.9 |
| 64d5917e-70fe-3036-ac28-6a2f8a962c26 | -18.05549 | -57.31913 | 2024-10-24 05:23:00 | NOAA-20 | CORUMBÁ | MATO GROSSO DO SUL | Brasil | 5003207 | 50 | 33 | nan | nan | nan | Pantanal | 1.9 |
| b0c4bc3b-4750-3f87-be8f-5b96c12b88b8 | -18.05497 | -57.3232 | 2024-10-24 05:23:00 | NOAA-20 | CORUMBÁ | MATO GROSSO DO SUL | Brasil | 5003207 | 50 | 33 | nan | nan | nan | Pantanal | 1.4 |
| f5e63465-5110-3071-8850-6adcb38a93a1 | -18.05334 | -57.30226 | 2024-10-24 05:23:00 | NOAA-20 | CORUMBÁ | MATO GROSSO DO SUL | Brasil | 5003207 | 50 | 33 | nan | nan | nan | Pantanal | 3.1 |
| 432c43c0-9455-3c57-bf2e-d69ff463c0d5 | -18.05282 | -57.30634 | 2024-10-24 05:23:00 | NOAA-20 | CORUMBÁ | MATO GROSSO DO SUL | Brasil | 5003207 | 50 | 33 | nan | nan | nan | Pantanal | 5.3 |
| 5ba58788-0119-324c-9f33-a54ac2f55532 | -18.05075 | -57.32262 | 2024-10-24 05:23:00 | NOAA-20 | CORUMBÁ | MATO GROSSO DO SUL | Brasil | 5003207 | 50 | 33 | nan | nan | nan | Pantanal | 1.4 |
| a4e639e0-0211-3e4e-82ff-9af250b4426a | -18.0486 | -57.30574 | 2024-10-24 05:23:00 | NOAA-20 | CORUMBÁ | MATO GROSSO DO SUL | Brasil | 5003207 | 50 | 33 | nan | nan | nan | Pantanal | 3.9 |
| 8b3db883-21fc-34e9-a373-523debf7cb17 | -18.04066 | -57.30051 | 2024-10-24 05:23:00 | NOAA-20 | CORUMBÁ | MATO GROSSO DO SUL | Brasil | 5003207 | 50 | 33 | nan | nan | nan | Pantanal | 2.0 |
| b0fb0477-f64e-314f-8c1c-c0c51a0951af | -18.04015 | -57.30458 | 2024-10-24 05:23:00 | NOAA-20 | CORUMBÁ | MATO GROSSO DO SUL | Brasil | 5003207 | 50 | 33 | nan | nan | nan | Pantanal | 3.9 |
| 4e84403f-7feb-33be-bd9c-0d60be83334a | -18.03819 | -57.35393 | 2024-10-24 05:23:00 | NOAA-20 | CORUMBÁ | MATO GROSSO DO SUL | Brasil | 5003207 | 50 | 33 | nan | nan | nan | Pantanal | 2.3 |
| 7854c96b-a3d5-3ccf-b30e-6e80d8b9adb0 | -18.03603 | -57.33714 | 2024-10-24 05:23:00 | NOAA-20 | CORUMBÁ | MATO GROSSO DO SUL | Brasil | 5003207 | 50 | 33 | nan | nan | nan | Pantanal | 2.2 |
| 6c38a556-7698-3307-a4c7-44c2c39a3703 | -17.83507 | -57.58994 | 2024-10-24 05:23:00 | NOAA-20 | CORUMBÁ | MATO GROSSO DO SUL | Brasil | 5003207 | 50 | 33 | nan | nan | nan | Pantanal | 1.3 |
| 53eb848b-8996-3b08-afd0-58a78abf4a3d | -17.83482 | -57.57751 | 2024-10-24 05:23:00 | NOAA-20 | CORUMBÁ | MATO GROSSO DO SUL | Brasil | 5003207 | 50 | 33 | nan | nan | nan | Pantanal | 3.0 |
| 329c17f4-aedc-350d-be9f-653d5320db4a | -17.83433 | -57.58142 | 2024-10-24 05:23:00 | NOAA-20 | CORUMBÁ | MATO GROSSO DO SUL | Brasil | 5003207 | 50 | 33 | nan | nan | nan | Pantanal | 3.0 |
| 23e1efbb-7bf0-36f1-a687-abc741cdb0f7 | -17.83248 | -57.57762 | 2024-10-24 05:23:00 | NOAA-20 | CORUMBÁ | MATO GROSSO DO SUL | Brasil | 5003207 | 50 | 33 | nan | nan | nan | Pantanal | 4.5 |
| 54d75c71-f1c8-361c-b262-99aaab649199 | -17.82369 | -57.58034 | 2024-10-24 05:23:00 | NOAA-20 | CORUMBÁ | MATO GROSSO DO SUL | Brasil | 5003207 | 50 | 33 | nan | nan | nan | Pantanal | 4.7 |
| be1f85a2-5ae7-3ad0-8bcf-ccb0f563385a | -17.83713 | -57.57432 | 2024-10-24 05:23:00 | NOAA-20 | CORUMBÁ | MATO GROSSO DO SUL | Brasil | 5003207 | 50 | 33 | nan | nan | nan | Pantanal | 8.5 |
| 09e8c644-7260-3b06-8d21-200f257a2379 | -17.83661 | -57.57825 | 2024-10-24 05:23:00 | NOAA-20 | CORUMBÁ | MATO GROSSO DO SUL | Brasil | 5003207 | 50 | 33 | nan | nan | nan | Pantanal | 4.2 |
| c7680315-642c-3cea-a0d4-4240bbd4d4e8 | -17.83559 | -57.58604 | 2024-10-24 05:23:00 | NOAA-20 | CORUMBÁ | MATO GROSSO DO SUL | Brasil | 5003207 | 50 | 33 | nan | nan | nan | Pantanal | 1.3 |
| 5aebf759-e855-31ac-8090-723089add918 | -17.8353 | -57.57358 | 2024-10-24 05:23:00 | NOAA-20 | CORUMBÁ | MATO GROSSO DO SUL | Brasil | 5003207 | 50 | 33 | nan | nan | nan | Pantanal | 8.5 |
| 15fbbf20-ed08-3e7e-9807-05fe3e01226d | -17.83197 | -57.58152 | 2024-10-24 05:23:00 | NOAA-20 | CORUMBÁ | MATO GROSSO DO SUL | Brasil | 5003207 | 50 | 33 | nan | nan | nan | Pantanal | 4.5 |
| 085f37b6-5da8-324c-8a7b-b2af611b12f1 | -17.80188 | -57.5535 | 2024-10-24 05:23:00 | NOAA-20 | POCONÉ | MATO GROSSO | Brasil | 5106505 | 51 | 33 | nan | nan | nan | Pantanal | 2.2 |
| 228de575-ff94-3234-8a1a-d957e86f8a3a | -17.79459 | -57.54454 | 2024-10-24 05:23:00 | NOAA-20 | POCONÉ | MATO GROSSO | Brasil | 5106505 | 51 | 33 | nan | nan | nan | Pantanal | 2.4 |
| 12a20cb8-029c-3320-8457-9b49bdf820da | -17.79345 | -57.52048 | 2024-10-24 05:23:00 | NOAA-20 | POCONÉ | MATO GROSSO | Brasil | 5106505 | 51 | 33 | nan | nan | nan | Pantanal | 4.5 |
| 8f469149-f1e7-3fdb-a22c-6a1c9840dec9 | -17.79295 | -57.52439 | 2024-10-24 05:23:00 | NOAA-20 | POCONÉ | MATO GROSSO | Brasil | 5106505 | 51 | 33 | nan | nan | nan | Pantanal | 2.5 |
| 821089cb-7f71-3a53-abb5-e6c914c6d3b1 | -17.78995 | -57.54786 | 2024-10-24 05:23:00 | NOAA-20 | POCONÉ | MATO GROSSO | Brasil | 5106505 | 51 | 33 | nan | nan | nan | Pantanal | 2.1 |
| 80229bd1-a845-39f3-8d9d-363665f8dcae | -17.7888 | -57.52381 | 2024-10-24 05:23:00 | NOAA-20 | POCONÉ | MATO GROSSO | Brasil | 5106505 | 51 | 33 | nan | nan | nan | Pantanal | 3.5 |
| af3c4b1e-1d81-3802-8992-cc2d5a6cf93d | -17.7883 | -57.52773 | 2024-10-24 05:23:00 | NOAA-20 | POCONÉ | MATO GROSSO | Brasil | 5106505 | 51 | 33 | nan | nan | nan | Pantanal | 3.5 |
| 84d4f2df-27bd-3fdf-8b79-78d034dc8c5f | -17.78664 | -57.50755 | 2024-10-24 05:23:00 | NOAA-20 | POCONÉ | MATO GROSSO | Brasil | 5106505 | 51 | 33 | nan | nan | nan | Pantanal | 2.0 |
| 856de90d-6339-3531-885d-3cf86c5ad56b | -17.78595 | -57.57904 | 2024-10-24 05:23:00 | NOAA-20 | POCONÉ | MATO GROSSO | Brasil | 5106505 | 51 | 33 | nan | nan | nan | Pantanal | 4.8 |
| ad51ca05-5300-3751-b303-45a420b22b47 | -17.78546 | -57.58294 | 2024-10-24 05:23:00 | NOAA-20 | POCONÉ | MATO GROSSO | Brasil | 5106505 | 51 | 33 | nan | nan | nan | Pantanal | 4.8 |
| d9afe841-29f2-33f3-8118-27a831b89e13 | -17.78415 | -57.52715 | 2024-10-24 05:23:00 | NOAA-20 | POCONÉ | MATO GROSSO | Brasil | 5106505 | 51 | 33 | nan | nan | nan | Pantanal | 3.5 |
| ace2f2f4-e23b-3fc3-843e-7cf9e950faf0 | -17.78298 | -57.50304 | 2024-10-24 05:23:00 | NOAA-20 | POCONÉ | MATO GROSSO | Brasil | 5106505 | 51 | 33 | nan | nan | nan | Pantanal | 4.2 |
| 00b05bc4-1169-34a2-8613-7f1b7a84dda5 | -17.78248 | -57.50697 | 2024-10-24 05:23:00 | NOAA-20 | POCONÉ | MATO GROSSO | Brasil | 5106505 | 51 | 33 | nan | nan | nan | Pantanal | 3.3 |
| 7516542d-4d99-3131-ac3a-90e6a25dc502 | -17.78082 | -57.58625 | 2024-10-24 05:23:00 | NOAA-20 | POCONÉ | MATO GROSSO | Brasil | 5106505 | 51 | 33 | nan | nan | nan | Pantanal | 1.8 |
| 80087bb3-1b5d-3581-8769-44010ffcf2cd | -17.78049 | -57.52266 | 2024-10-24 05:23:00 | NOAA-20 | POCONÉ | MATO GROSSO | Brasil | 5106505 | 51 | 33 | nan | nan | nan | Pantanal | 3.2 |
| 9a307f5e-2878-31dc-9044-f23b23d3a775 | -17.77882 | -57.50246 | 2024-10-24 05:23:00 | NOAA-20 | POCONÉ | MATO GROSSO | Brasil | 5106505 | 51 | 33 | nan | nan | nan | Pantanal | 4.2 |
| 5b760c0a-90b3-3271-ad5c-bab9c12ad06c | -17.77619 | -57.58955 | 2024-10-24 05:23:00 | NOAA-20 | POCONÉ | MATO GROSSO | Brasil | 5106505 | 51 | 33 | nan | nan | nan | Pantanal | 1.8 |
| 7b4d1f5f-5f3a-3ab3-944a-8abfa2abdb78 | -17.77299 | -57.48162 | 2024-10-24 05:23:00 | NOAA-20 | POCONÉ | MATO GROSSO | Brasil | 5106505 | 51 | 33 | nan | nan | nan | Pantanal | 1.9 |
| 1f3bd9b7-79cb-3d96-8401-8a4511e7aeb5 | -17.7712 | -57.52933 | 2024-10-24 05:23:00 | NOAA-20 | POCONÉ | MATO GROSSO | Brasil | 5106505 | 51 | 33 | nan | nan | nan | Pantanal | 2.3 |
| fbd6c638-7f93-38a0-b90c-422d886cc5e0 | -17.7707 | -57.53325 | 2024-10-24 05:23:00 | NOAA-20 | POCONÉ | MATO GROSSO | Brasil | 5106505 | 51 | 33 | nan | nan | nan | Pantanal | 2.3 |
| 408f0098-4eca-37a9-9c62-6ff31f4438f6 | -17.76044 | -57.54773 | 2024-10-24 05:23:00 | NOAA-20 | POCONÉ | MATO GROSSO | Brasil | 5106505 | 51 | 33 | nan | nan | nan | Pantanal | 9.9 |
| df02349f-d7b3-3779-ba0c-c4ecc75bb8aa | -17.75994 | -57.55162 | 2024-10-24 05:23:00 | NOAA-20 | POCONÉ | MATO GROSSO | Brasil | 5106505 | 51 | 33 | nan | nan | nan | Pantanal | 3.3 |
| 293e862c-891e-3ca4-97de-d36b76d7a6a4 | -17.75945 | -57.55553 | 2024-10-24 05:23:00 | NOAA-20 | POCONÉ | MATO GROSSO | Brasil | 5106505 | 51 | 33 | nan | nan | nan | Pantanal | 3.3 |
| 711200a3-c357-3aa5-8ea1-35e611aec356 | -17.7558 | -57.55105 | 2024-10-24 05:23:00 | NOAA-20 | POCONÉ | MATO GROSSO | Brasil | 5106505 | 51 | 33 | nan | nan | nan | Pantanal | 3.3 |
| 3d5249aa-11aa-34c3-bd04-3231d867ebca | -17.75117 | -57.55437 | 2024-10-24 05:23:00 | NOAA-20 | POCONÉ | MATO GROSSO | Brasil | 5106505 | 51 | 33 | nan | nan | nan | Pantanal | 13.8 |
| b7095d58-5644-371d-8007-c496c70170bc | -17.7509 | -57.58997 | 2024-10-24 05:23:00 | NOAA-20 | POCONÉ | MATO GROSSO | Brasil | 5106505 | 51 | 33 | nan | nan | nan | Pantanal | 5.6 |
| d8c0ee5b-3f90-340a-84d4-7ba5952ce4f1 | -17.75068 | -57.55826 | 2024-10-24 05:23:00 | NOAA-20 | POCONÉ | MATO GROSSO | Brasil | 5106505 | 51 | 33 | nan | nan | nan | Pantanal | 6.7 |
| 2c92e4f7-1ad5-35f5-971e-618b8ec5da43 | -17.74774 | -57.58162 | 2024-10-24 05:23:00 | NOAA-20 | POCONÉ | MATO GROSSO | Brasil | 5106505 | 51 | 33 | nan | nan | nan | Pantanal | 5.5 |
| fd38ef7f-7e7d-3a1a-accf-c0f5813a4fd5 | -17.74677 | -57.58939 | 2024-10-24 05:23:00 | NOAA-20 | POCONÉ | MATO GROSSO | Brasil | 5106505 | 51 | 33 | nan | nan | nan | Pantanal | 6.7 |
| 2f1f928c-4a24-3c7d-8e6c-d3e348dff8e3 | -17.74606 | -57.49389 | 2024-10-24 05:23:00 | NOAA-20 | POCONÉ | MATO GROSSO | Brasil | 5106505 | 51 | 33 | nan | nan | nan | Pantanal | 3.9 |
| 5ca2ae15-e42d-30bd-8474-be38eb350fa5 | -17.74523 | -57.48782 | 2024-10-24 05:23:00 | NOAA-20 | POCONÉ | MATO GROSSO | Brasil | 5106505 | 51 | 33 | nan | nan | nan | Pantanal | 5.6 |
| f79311ed-d2e2-3934-8561-67656d4cd516 | -17.74471 | -57.49175 | 2024-10-24 05:23:00 | NOAA-20 | POCONÉ | MATO GROSSO | Brasil | 5106505 | 51 | 33 | nan | nan | nan | Pantanal | 5.6 |
| 58c472cf-e5fb-34c9-bc0c-86276bd02513 | -17.74361 | -57.58104 | 2024-10-24 05:23:00 | NOAA-20 | POCONÉ | MATO GROSSO | Brasil | 5106505 | 51 | 33 | nan | nan | nan | Pantanal | 5.5 |
| 77ee0217-846f-33e6-9e36-9d0ab35cd109 | -17.74312 | -57.58493 | 2024-10-24 05:23:00 | NOAA-20 | POCONÉ | MATO GROSSO | Brasil | 5106505 | 51 | 33 | nan | nan | nan | Pantanal | 5.5 |
| 9946c74c-70e2-3b91-b858-95e1d342db7e | -17.74055 | -57.49118 | 2024-10-24 05:23:00 | NOAA-20 | POCONÉ | MATO GROSSO | Brasil | 5106505 | 51 | 33 | nan | nan | nan | Pantanal | 5.6 |
| af3336e7-1bb0-3cc5-ab58-e2d2fd9967d3 | -17.73224 | -57.49002 | 2024-10-24 05:23:00 | NOAA-20 | POCONÉ | MATO GROSSO | Brasil | 5106505 | 51 | 33 | nan | nan | nan | Pantanal | 2.3 |
| 61ecef46-62e7-300a-bbb3-25025ede7e16 | -17.70831 | -57.47871 | 2024-10-24 05:23:00 | NOAA-20 | POCONÉ | MATO GROSSO | Brasil | 5106505 | 51 | 33 | nan | nan | nan | Pantanal | 6.3 |
| cac46c7f-ad5b-39e9-bca4-61f4d9f6b946 | -17.70415 | -57.47813 | 2024-10-24 05:23:00 | NOAA-20 | POCONÉ | MATO GROSSO | Brasil | 5106505 | 51 | 33 | nan | nan | nan | Pantanal | 5.6 |
| 6d1f8b89-e909-30b1-bc53-cbe23db1bdb3 | -17.70365 | -57.48206 | 2024-10-24 05:23:00 | NOAA-20 | POCONÉ | MATO GROSSO | Brasil | 5106505 | 51 | 33 | nan | nan | nan | Pantanal | 4.1 |
| 1a830740-df1f-39b6-bf32-320a3d9ac132 | -17.69584 | -57.47698 | 2024-10-24 05:23:00 | NOAA-20 | POCONÉ | MATO GROSSO | Brasil | 5106505 | 51 | 33 | nan | nan | nan | Pantanal | 2.8 |
| 9b314196-0cb3-3f46-b5da-341548946233 | -17.68336 | -57.47523 | 2024-10-24 05:23:00 | NOAA-20 | POCONÉ | MATO GROSSO | Brasil | 5106505 | 51 | 33 | nan | nan | nan | Pantanal | 2.9 |
| b93c6caa-c317-3726-b399-d5538ab898ea | -17.6797 | -57.47073 | 2024-10-24 05:23:00 | NOAA-20 | POCONÉ | MATO GROSSO | Brasil | 5106505 | 51 | 33 | nan | nan | nan | Pantanal | 5.9 |
| 8b8b3768-1740-3765-8c6d-94c87214f70a | -17.6697 | -57.44929 | 2024-10-24 05:23:00 | NOAA-20 | POCONÉ | MATO GROSSO | Brasil | 5106505 | 51 | 33 | nan | nan | nan | Pantanal | 2.1 |


[Clique aqui para ver as próximas entradas](README102.md)
