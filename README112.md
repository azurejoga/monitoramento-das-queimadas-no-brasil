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

## Dados Diários - Página 112

| ID | Latitude | Longitude | Data/Hora GMT | Satélite | Município | Estado | País | Município ID | Estado ID | País ID | Dias sem Chuva | Precipitação | Risco de Fogo | Bioma | FRP |
|----|----------|-----------|---------------|----------|-----------|--------|------|--------------|-----------|---------|----------------|--------------|----------------|-------|-----|
| 0f3bb871-5ba5-3170-bef9-b90ef746a67f | -13.03862 | -51.24379 | 2024-10-01 05:06:00 | NOAA-21 | RIBEIRÃO CASCALHEIRA | MATO GROSSO | Brasil | 5107180 | 51 | 33 | nan | nan | nan | Cerrado | 2.3 |
| cce79e56-f89e-3630-bd14-74c363798ef8 | -13.03808 | -51.24791 | 2024-10-01 05:06:00 | NOAA-21 | RIBEIRÃO CASCALHEIRA | MATO GROSSO | Brasil | 5107180 | 51 | 33 | nan | nan | nan | Cerrado | 2.3 |
| bc574fb7-8e92-3641-9d7d-ff750aa2abab | -13.03707 | -51.22255 | 2024-10-01 05:06:00 | NOAA-21 | RIBEIRÃO CASCALHEIRA | MATO GROSSO | Brasil | 5107180 | 51 | 33 | nan | nan | nan | Cerrado | 6.0 |
| 5f1d85ce-fa43-3f2b-b91c-2fcf63c725b0 | -13.03652 | -51.22668 | 2024-10-01 05:06:00 | NOAA-21 | RIBEIRÃO CASCALHEIRA | MATO GROSSO | Brasil | 5107180 | 51 | 33 | nan | nan | nan | Cerrado | 16.5 |
| 8f7893b3-f9f6-3483-a259-23598deb5e6d | -13.03598 | -51.23081 | 2024-10-01 05:06:00 | NOAA-21 | RIBEIRÃO CASCALHEIRA | MATO GROSSO | Brasil | 5107180 | 51 | 33 | nan | nan | nan | Cerrado | 16.5 |
| f585286d-69e8-3e7d-994e-86abe2a7909f | -13.03543 | -51.23494 | 2024-10-01 05:06:00 | NOAA-21 | RIBEIRÃO CASCALHEIRA | MATO GROSSO | Brasil | 5107180 | 51 | 33 | nan | nan | nan | Cerrado | 10.2 |
| 12963f4f-2697-3bd3-9249-9f495517253d | -13.03489 | -51.23906 | 2024-10-01 05:06:00 | NOAA-21 | RIBEIRÃO CASCALHEIRA | MATO GROSSO | Brasil | 5107180 | 51 | 33 | nan | nan | nan | Cerrado | 10.2 |
| 918c853c-8bd7-3b1a-a488-201599006ce2 | -13.03387 | -51.21368 | 2024-10-01 05:06:00 | NOAA-21 | RIBEIRÃO CASCALHEIRA | MATO GROSSO | Brasil | 5107180 | 51 | 33 | nan | nan | nan | Cerrado | 1.5 |
| 5c142e2a-ec00-357d-8003-307db9aaee8c | -13.03278 | -51.22194 | 2024-10-01 05:06:00 | NOAA-21 | RIBEIRÃO CASCALHEIRA | MATO GROSSO | Brasil | 5107180 | 51 | 33 | nan | nan | nan | Cerrado | 6.0 |
| 4ac3853c-dc55-327f-993d-510741628c19 | -13.03224 | -51.22607 | 2024-10-01 05:06:00 | NOAA-21 | RIBEIRÃO CASCALHEIRA | MATO GROSSO | Brasil | 5107180 | 51 | 33 | nan | nan | nan | Cerrado | 16.5 |
| efbd6ee0-7947-3df0-9c67-d021cf6724dd | -13.0317 | -51.23019 | 2024-10-01 05:06:00 | NOAA-21 | RIBEIRÃO CASCALHEIRA | MATO GROSSO | Brasil | 5107180 | 51 | 33 | nan | nan | nan | Cerrado | 16.5 |
| 359f2788-388f-3b37-b710-7cc48735f1f3 | -13.03115 | -51.23432 | 2024-10-01 05:06:00 | NOAA-21 | RIBEIRÃO CASCALHEIRA | MATO GROSSO | Brasil | 5107180 | 51 | 33 | nan | nan | nan | Cerrado | 10.2 |
| 8f7f6646-6886-3bd0-a0ec-cebae8f31620 | -13.03061 | -51.23845 | 2024-10-01 05:06:00 | NOAA-21 | RIBEIRÃO CASCALHEIRA | MATO GROSSO | Brasil | 5107180 | 51 | 33 | nan | nan | nan | Cerrado | 10.2 |
| 014dc81d-3c82-3fdd-91fd-edd05173647e | -13.03007 | -51.24256 | 2024-10-01 05:06:00 | NOAA-21 | RIBEIRÃO CASCALHEIRA | MATO GROSSO | Brasil | 5107180 | 51 | 33 | nan | nan | nan | Cerrado | 10.8 |
| bf7d828e-3ede-3e8d-932f-cfdd44397d42 | -13.02953 | -51.24667 | 2024-10-01 05:06:00 | NOAA-21 | RIBEIRÃO CASCALHEIRA | MATO GROSSO | Brasil | 5107180 | 51 | 33 | nan | nan | nan | Cerrado | 10.8 |
| 97a94f5b-ee7c-395c-aedb-6a8e6f14da2c | -13.02796 | -51.22545 | 2024-10-01 05:06:00 | NOAA-21 | RIBEIRÃO CASCALHEIRA | MATO GROSSO | Brasil | 5107180 | 51 | 33 | nan | nan | nan | Cerrado | 11.0 |
| 0ec2fcec-c0af-3d8f-9922-e36a014e0826 | -13.02741 | -51.22958 | 2024-10-01 05:06:00 | NOAA-21 | RIBEIRÃO CASCALHEIRA | MATO GROSSO | Brasil | 5107180 | 51 | 33 | nan | nan | nan | Cerrado | 11.0 |
| a4c06564-b01e-32c2-9f45-76affac66818 | -13.02687 | -51.23371 | 2024-10-01 05:06:00 | NOAA-21 | RIBEIRÃO CASCALHEIRA | MATO GROSSO | Brasil | 5107180 | 51 | 33 | nan | nan | nan | Cerrado | 20.1 |
| 7d1e6cce-a875-39c2-b7eb-0522ff04077c | -13.02633 | -51.23783 | 2024-10-01 05:06:00 | NOAA-21 | RIBEIRÃO CASCALHEIRA | MATO GROSSO | Brasil | 5107180 | 51 | 33 | nan | nan | nan | Cerrado | 20.1 |
| d945553b-8540-348e-9e87-9c1be14fae35 | -13.02525 | -51.24607 | 2024-10-01 05:06:00 | NOAA-21 | RIBEIRÃO CASCALHEIRA | MATO GROSSO | Brasil | 5107180 | 51 | 33 | nan | nan | nan | Cerrado | 11.0 |
| 650b17d2-f993-3c43-909c-60a56f442318 | -13.02259 | -51.23309 | 2024-10-01 05:06:00 | NOAA-21 | RIBEIRÃO CASCALHEIRA | MATO GROSSO | Brasil | 5107180 | 51 | 33 | nan | nan | nan | Cerrado | 20.1 |
| 649eed4d-9282-34c8-9a5a-b94ee3ad9299 | -13.02205 | -51.23721 | 2024-10-01 05:06:00 | NOAA-21 | RIBEIRÃO CASCALHEIRA | MATO GROSSO | Brasil | 5107180 | 51 | 33 | nan | nan | nan | Cerrado | 20.1 |
| 83f67575-4487-3010-a6a3-9a496dbd9c44 | -13.02151 | -51.24134 | 2024-10-01 05:06:00 | NOAA-21 | RIBEIRÃO CASCALHEIRA | MATO GROSSO | Brasil | 5107180 | 51 | 33 | nan | nan | nan | Cerrado | 11.0 |
| 75eedfaf-a15a-3edd-a93f-ff29181d6659 | -13.01993 | -51.2201 | 2024-10-01 05:06:00 | NOAA-21 | RIBEIRÃO CASCALHEIRA | MATO GROSSO | Brasil | 5107180 | 51 | 33 | nan | nan | nan | Cerrado | 18.7 |
| 4b10bbb8-43f6-30e9-ae43-cec5f910671f | -13.01885 | -51.22835 | 2024-10-01 05:06:00 | NOAA-21 | RIBEIRÃO CASCALHEIRA | MATO GROSSO | Brasil | 5107180 | 51 | 33 | nan | nan | nan | Cerrado | 4.1 |
| 31af942e-32cc-3693-998a-531f6d24a518 | -13.01565 | -51.21948 | 2024-10-01 05:06:00 | NOAA-21 | RIBEIRÃO CASCALHEIRA | MATO GROSSO | Brasil | 5107180 | 51 | 33 | nan | nan | nan | Cerrado | 18.7 |
| c9a279e7-caaa-3823-bd3a-907620edb6fc | -13.0076 | -51.24773 | 2024-10-01 05:06:00 | NOAA-21 | RIBEIRÃO CASCALHEIRA | MATO GROSSO | Brasil | 5107180 | 51 | 33 | nan | nan | nan | Cerrado | 32.6 |
| 3b47aa7e-2d83-39c5-97ae-3b45a3bda6a4 | -13.006 | -51.22651 | 2024-10-01 05:06:00 | NOAA-21 | RIBEIRÃO CASCALHEIRA | MATO GROSSO | Brasil | 5107180 | 51 | 33 | nan | nan | nan | Cerrado | 13.3 |
| e1db0795-8945-38e8-95e5-608478b68413 | -13.00012 | -51.23826 | 2024-10-01 05:06:00 | NOAA-21 | RIBEIRÃO CASCALHEIRA | MATO GROSSO | Brasil | 5107180 | 51 | 33 | nan | nan | nan | Cerrado | 4.0 |
| 16346bd1-1f41-39e1-9ea2-facfb599a5fe | -12.99833 | -51.22771 | 2024-10-01 05:06:00 | NOAA-21 | RIBEIRÃO CASCALHEIRA | MATO GROSSO | Brasil | 5107180 | 51 | 33 | nan | nan | nan | Cerrado | 6.0 |
| 3b23efd5-b0c9-3234-8f8e-adcb7c0b9e3c | -12.9972 | -51.23594 | 2024-10-01 05:06:00 | NOAA-21 | RIBEIRÃO CASCALHEIRA | MATO GROSSO | Brasil | 5107180 | 51 | 33 | nan | nan | nan | Cerrado | 5.5 |
| 4f159d42-81a4-3a36-92c3-cdd89dcfe5cb | -12.99691 | -51.22941 | 2024-10-01 05:06:00 | NOAA-21 | RIBEIRÃO CASCALHEIRA | MATO GROSSO | Brasil | 5107180 | 51 | 33 | nan | nan | nan | Cerrado | 14.6 |
| 11a41b29-e89a-3949-aab2-8af326d48264 | -12.99461 | -51.22299 | 2024-10-01 05:06:00 | NOAA-21 | RIBEIRÃO CASCALHEIRA | MATO GROSSO | Brasil | 5107180 | 51 | 33 | nan | nan | nan | Cerrado | 6.0 |
| 7732e7e2-ce88-36a5-af0f-95888e656805 | -12.99369 | -51.22054 | 2024-10-01 05:06:00 | NOAA-21 | RIBEIRÃO CASCALHEIRA | MATO GROSSO | Brasil | 5107180 | 51 | 33 | nan | nan | nan | Cerrado | 4.1 |
| d702d3d1-bb8f-3773-bce7-6aa4b6e69ce2 | -12.98289 | -51.21292 | 2024-10-01 05:06:00 | NOAA-21 | RIBEIRÃO CASCALHEIRA | MATO GROSSO | Brasil | 5107180 | 51 | 33 | nan | nan | nan | Cerrado | 33.7 |
| 3282fb32-4558-3f22-b60f-55ba5151113b | -12.97804 | -51.21644 | 2024-10-01 05:06:00 | NOAA-21 | RIBEIRÃO CASCALHEIRA | MATO GROSSO | Brasil | 5107180 | 51 | 33 | nan | nan | nan | Cerrado | 33.7 |
| 77c86f71-f7f5-30a2-877d-17341b039230 | -12.97693 | -51.22466 | 2024-10-01 05:06:00 | NOAA-21 | RIBEIRÃO CASCALHEIRA | MATO GROSSO | Brasil | 5107180 | 51 | 33 | nan | nan | nan | Cerrado | 83.8 |
| a2753a6f-8340-3425-b308-55d2cf96e657 | -12.9656 | -51.24398 | 2024-10-01 05:06:00 | NOAA-21 | RIBEIRÃO CASCALHEIRA | MATO GROSSO | Brasil | 5107180 | 51 | 33 | nan | nan | nan | Cerrado | 6.9 |
| 8daa6117-aa4f-373d-9312-bd27d06b97b9 | -12.9652 | -51.21459 | 2024-10-01 05:06:00 | NOAA-21 | RIBEIRÃO CASCALHEIRA | MATO GROSSO | Brasil | 5107180 | 51 | 33 | nan | nan | nan | Cerrado | 48.5 |
| b23a519d-cfae-3283-ac73-b157f820ea2b | -12.96092 | -51.21396 | 2024-10-01 05:06:00 | NOAA-21 | RIBEIRÃO CASCALHEIRA | MATO GROSSO | Brasil | 5107180 | 51 | 33 | nan | nan | nan | Cerrado | 48.5 |
| 036d0172-28ef-3559-981a-d20aa36e639c | -13.06664 | -51.19727 | 2024-10-01 05:06:00 | NOAA-21 | RIBEIRÃO CASCALHEIRA | MATO GROSSO | Brasil | 5107180 | 51 | 33 | nan | nan | nan | Cerrado | 158.0 |
| 76701979-d0bc-3759-9280-a27494286032 | -13.05861 | -51.19189 | 2024-10-01 05:06:00 | NOAA-21 | RIBEIRÃO CASCALHEIRA | MATO GROSSO | Brasil | 5107180 | 51 | 33 | nan | nan | nan | Cerrado | 3.7 |
| be0122e1-1350-30c2-83a5-88d9a8e26eac | -13.05806 | -51.19604 | 2024-10-01 05:06:00 | NOAA-21 | RIBEIRÃO CASCALHEIRA | MATO GROSSO | Brasil | 5107180 | 51 | 33 | nan | nan | nan | Cerrado | 3.3 |
| c1e15e79-801b-3741-a36d-6b0ab3b1f5c1 | -13.05376 | -51.19544 | 2024-10-01 05:06:00 | NOAA-21 | RIBEIRÃO CASCALHEIRA | MATO GROSSO | Brasil | 5107180 | 51 | 33 | nan | nan | nan | Cerrado | 3.3 |
| 822f1c87-47c0-3434-8752-f5c67b1242a4 | -13.03659 | -51.19298 | 2024-10-01 05:06:00 | NOAA-21 | RIBEIRÃO CASCALHEIRA | MATO GROSSO | Brasil | 5107180 | 51 | 33 | nan | nan | nan | Cerrado | 4.8 |
| 17a32071-be47-362a-ba69-4ece63aee036 | -13.03605 | -51.19712 | 2024-10-01 05:06:00 | NOAA-21 | RIBEIRÃO CASCALHEIRA | MATO GROSSO | Brasil | 5107180 | 51 | 33 | nan | nan | nan | Cerrado | 4.8 |
| e58b1b01-94f3-3469-a199-0df4c379056c | -13.0323 | -51.19237 | 2024-10-01 05:06:00 | NOAA-21 | RIBEIRÃO CASCALHEIRA | MATO GROSSO | Brasil | 5107180 | 51 | 33 | nan | nan | nan | Cerrado | 132.4 |
| 4ffd1a70-0ebb-3c79-9cc4-60ed610ac1a1 | -13.03176 | -51.19651 | 2024-10-01 05:06:00 | NOAA-21 | RIBEIRÃO CASCALHEIRA | MATO GROSSO | Brasil | 5107180 | 51 | 33 | nan | nan | nan | Cerrado | 132.4 |
| b9bd252b-eda5-3381-a146-584650918723 | -13.02371 | -51.19114 | 2024-10-01 05:06:00 | NOAA-21 | RIBEIRÃO CASCALHEIRA | MATO GROSSO | Brasil | 5107180 | 51 | 33 | nan | nan | nan | Cerrado | 3.2 |
| 3666ed35-1cc1-3d5b-8225-7902677db3a4 | -13.02317 | -51.19527 | 2024-10-01 05:06:00 | NOAA-21 | RIBEIRÃO CASCALHEIRA | MATO GROSSO | Brasil | 5107180 | 51 | 33 | nan | nan | nan | Cerrado | 3.2 |
| 718615d9-a783-3b13-8bc8-999d4b331615 | -12.72723 | -52.01807 | 2024-10-01 05:06:00 | NOAA-21 | RIBEIRÃO CASCALHEIRA | MATO GROSSO | Brasil | 5107180 | 51 | 33 | nan | nan | nan | Amazônia | 2.3 |
| 08ffc753-fa28-3578-afad-40edbc49618c | -12.72601 | -51.93581 | 2024-10-01 05:06:00 | NOAA-21 | RIBEIRÃO CASCALHEIRA | MATO GROSSO | Brasil | 5107180 | 51 | 33 | nan | nan | nan | Amazônia | 1.6 |
| 1a97589a-7581-32b6-b1e6-7c3ac3e19525 | -12.7251 | -51.97308 | 2024-10-01 05:06:00 | NOAA-21 | RIBEIRÃO CASCALHEIRA | MATO GROSSO | Brasil | 5107180 | 51 | 33 | nan | nan | nan | Amazônia | 1.4 |
| 8d79458e-33c0-3b13-91d3-e16835220dd9 | -12.7246 | -51.97673 | 2024-10-01 05:06:00 | NOAA-21 | RIBEIRÃO CASCALHEIRA | MATO GROSSO | Brasil | 5107180 | 51 | 33 | nan | nan | nan | Amazônia | 0.9 |
| dd4867b2-8cfa-35ae-ba81-63c2d230cf14 | -12.71683 | -51.91153 | 2024-10-01 05:06:00 | NOAA-21 | RIBEIRÃO CASCALHEIRA | MATO GROSSO | Brasil | 5107180 | 51 | 33 | nan | nan | nan | Amazônia | 5.2 |
| 655db667-fc08-3c87-88e1-f618390f57c6 | -12.7141 | -52.02361 | 2024-10-01 05:06:00 | NOAA-21 | RIBEIRÃO CASCALHEIRA | MATO GROSSO | Brasil | 5107180 | 51 | 33 | nan | nan | nan | Amazônia | 2.2 |
| d1bb5379-6fac-3ea8-869e-61798386af05 | -12.7136 | -52.02722 | 2024-10-01 05:06:00 | NOAA-21 | RIBEIRÃO CASCALHEIRA | MATO GROSSO | Brasil | 5107180 | 51 | 33 | nan | nan | nan | Amazônia | 1.0 |
| f45d2598-9f1e-372e-8d95-bf97cacb2e6c | -12.70956 | -52.02665 | 2024-10-01 05:06:00 | NOAA-21 | RIBEIRÃO CASCALHEIRA | MATO GROSSO | Brasil | 5107180 | 51 | 33 | nan | nan | nan | Amazônia | 1.0 |
| e7e871cb-37a1-3039-8fa9-47cc6651c0ca | -12.5996 | -52.01041 | 2024-10-01 05:06:00 | NOAA-21 | RIBEIRÃO CASCALHEIRA | MATO GROSSO | Brasil | 5107180 | 51 | 33 | nan | nan | nan | Amazônia | 1.9 |
| c650b8c1-6ded-3e93-8cda-9ed656a7d058 | -13.04299 | -51.21077 | 2024-10-01 05:06:00 | NOAA-21 | RIBEIRÃO CASCALHEIRA | MATO GROSSO | Brasil | 5107180 | 51 | 33 | nan | nan | nan | Cerrado | 71.2 |
| 6e33261b-2d1b-3898-b4e5-0505686beb8f | -13.0387 | -51.21016 | 2024-10-01 05:06:00 | NOAA-21 | RIBEIRÃO CASCALHEIRA | MATO GROSSO | Brasil | 5107180 | 51 | 33 | nan | nan | nan | Cerrado | 1.5 |
| 619bda77-2c2a-3d22-bf01-46d88e190115 | -13.0355 | -51.20126 | 2024-10-01 05:06:00 | NOAA-21 | RIBEIRÃO CASCALHEIRA | MATO GROSSO | Brasil | 5107180 | 51 | 33 | nan | nan | nan | Cerrado | 4.0 |
| bfbdb223-4076-3bb8-bb47-c93637cd6363 | -13.03284 | -51.18822 | 2024-10-01 05:06:00 | NOAA-21 | RIBEIRÃO CASCALHEIRA | MATO GROSSO | Brasil | 5107180 | 51 | 33 | nan | nan | nan | Cerrado | 4.0 |
| 2ef051ff-db23-3b03-8f93-2e13f5b4a8c5 | -13.03121 | -51.20065 | 2024-10-01 05:06:00 | NOAA-21 | RIBEIRÃO CASCALHEIRA | MATO GROSSO | Brasil | 5107180 | 51 | 33 | nan | nan | nan | Cerrado | 40.8 |
| 9d943075-d8ab-3598-bdd6-20c183faceb8 | -13.03067 | -51.20479 | 2024-10-01 05:06:00 | NOAA-21 | RIBEIRÃO CASCALHEIRA | MATO GROSSO | Brasil | 5107180 | 51 | 33 | nan | nan | nan | Cerrado | 40.8 |
| 76d8a108-4a58-385b-95d1-2165e1469edc | -13.03013 | -51.20893 | 2024-10-01 05:06:00 | NOAA-21 | RIBEIRÃO CASCALHEIRA | MATO GROSSO | Brasil | 5107180 | 51 | 33 | nan | nan | nan | Cerrado | 5.9 |
| b1597de8-38bb-3a47-beed-b8a8425cdf6f | -13.02855 | -51.18761 | 2024-10-01 05:06:00 | NOAA-21 | RIBEIRÃO CASCALHEIRA | MATO GROSSO | Brasil | 5107180 | 51 | 33 | nan | nan | nan | Cerrado | 4.0 |
| c6df30a6-79d2-3444-b363-905331b32bed | -13.02801 | -51.19175 | 2024-10-01 05:06:00 | NOAA-21 | RIBEIRÃO CASCALHEIRA | MATO GROSSO | Brasil | 5107180 | 51 | 33 | nan | nan | nan | Cerrado | 132.4 |
| e8bdf173-3c9e-317a-ba91-bd2499e724f4 | -13.02692 | -51.20004 | 2024-10-01 05:06:00 | NOAA-21 | RIBEIRÃO CASCALHEIRA | MATO GROSSO | Brasil | 5107180 | 51 | 33 | nan | nan | nan | Cerrado | 40.8 |
| 64d65683-9f6f-3796-aa28-7bc5abaf4933 | -13.02638 | -51.20418 | 2024-10-01 05:06:00 | NOAA-21 | RIBEIRÃO CASCALHEIRA | MATO GROSSO | Brasil | 5107180 | 51 | 33 | nan | nan | nan | Cerrado | 40.8 |
| d61c8eb0-4375-3f41-a59b-0d10dfca844f | -13.02155 | -51.20769 | 2024-10-01 05:06:00 | NOAA-21 | RIBEIRÃO CASCALHEIRA | MATO GROSSO | Brasil | 5107180 | 51 | 33 | nan | nan | nan | Cerrado | 27.8 |
| 2dbd8482-96f8-3bbe-ac36-9eec3246dfbb | -13.01834 | -51.1988 | 2024-10-01 05:06:00 | NOAA-21 | RIBEIRÃO CASCALHEIRA | MATO GROSSO | Brasil | 5107180 | 51 | 33 | nan | nan | nan | Cerrado | 40.7 |
| ec33d43f-18c2-362c-bb57-bc27834491ad | -13.0178 | -51.20294 | 2024-10-01 05:06:00 | NOAA-21 | RIBEIRÃO CASCALHEIRA | MATO GROSSO | Brasil | 5107180 | 51 | 33 | nan | nan | nan | Cerrado | 40.7 |
| cb8ddad0-9e77-35ef-8454-6fffcbe931ab | -13.01459 | -51.19404 | 2024-10-01 05:06:00 | NOAA-21 | RIBEIRÃO CASCALHEIRA | MATO GROSSO | Brasil | 5107180 | 51 | 33 | nan | nan | nan | Cerrado | 1.3 |
| 2d019496-91ba-3440-beea-fe502ad52090 | -12.97004 | -51.2111 | 2024-10-01 05:06:00 | NOAA-21 | RIBEIRÃO CASCALHEIRA | MATO GROSSO | Brasil | 5107180 | 51 | 33 | nan | nan | nan | Cerrado | 11.0 |
| 2b18b2b1-4b68-3b67-aa6c-4e2b3e25150b | -12.92081 | -51.18718 | 2024-10-01 05:06:00 | NOAA-21 | RIBEIRÃO CASCALHEIRA | MATO GROSSO | Brasil | 5107180 | 51 | 33 | nan | nan | nan | Cerrado | 32.0 |
| 7e75663e-b9ce-36f7-895e-cbec7ca0e0f0 | -12.92027 | -51.19131 | 2024-10-01 05:06:00 | NOAA-21 | RIBEIRÃO CASCALHEIRA | MATO GROSSO | Brasil | 5107180 | 51 | 33 | nan | nan | nan | Cerrado | 32.0 |
| 1f648f81-cf8d-328c-ac3e-2ac9ee6c46c9 | -12.91919 | -51.19956 | 2024-10-01 05:06:00 | NOAA-21 | RIBEIRÃO CASCALHEIRA | MATO GROSSO | Brasil | 5107180 | 51 | 33 | nan | nan | nan | Cerrado | 31.1 |
| b05f0e86-2c02-3c4e-8faf-108afcd088a8 | -12.91811 | -51.20782 | 2024-10-01 05:06:00 | NOAA-21 | RIBEIRÃO CASCALHEIRA | MATO GROSSO | Brasil | 5107180 | 51 | 33 | nan | nan | nan | Cerrado | 2.3 |
| 5b057090-1eeb-36b6-b452-e1d86d2d3fb1 | -12.9812 | -51.32103 | 2024-10-01 05:06:00 | NOAA-21 | RIBEIRÃO CASCALHEIRA | MATO GROSSO | Brasil | 5107180 | 51 | 33 | nan | nan | nan | Cerrado | 86.3 |
| 0b5addef-2af6-3fd6-9cc2-3144d10247f9 | -12.97991 | -51.2669 | 2024-10-01 05:06:00 | NOAA-21 | RIBEIRÃO CASCALHEIRA | MATO GROSSO | Brasil | 5107180 | 51 | 33 | nan | nan | nan | Cerrado | 3.9 |
| c61cc774-9067-3fd1-af7e-01cab96f2f0c | -12.97889 | -51.33508 | 2024-10-01 05:06:00 | NOAA-21 | RIBEIRÃO CASCALHEIRA | MATO GROSSO | Brasil | 5107180 | 51 | 33 | nan | nan | nan | Cerrado | 8.8 |
| f222a116-3e3f-3c00-8bb4-3fca255830b8 | -12.97787 | -51.34533 | 2024-10-01 05:06:00 | NOAA-21 | RIBEIRÃO CASCALHEIRA | MATO GROSSO | Brasil | 5107180 | 51 | 33 | nan | nan | nan | Cerrado | 4.3 |
| d8c43c33-3049-391b-88e2-233757fb8939 | -12.97784 | -51.34319 | 2024-10-01 05:06:00 | NOAA-21 | RIBEIRÃO CASCALHEIRA | MATO GROSSO | Brasil | 5107180 | 51 | 33 | nan | nan | nan | Cerrado | 3.3 |
| 11d6d4ee-fa55-3b22-a650-80ded2c05d44 | -12.97732 | -51.34724 | 2024-10-01 05:06:00 | NOAA-21 | RIBEIRÃO CASCALHEIRA | MATO GROSSO | Brasil | 5107180 | 51 | 33 | nan | nan | nan | Cerrado | 3.3 |
| 265a15dd-c983-32cd-a5f7-5baab3f1df2c | -12.9762 | -51.2622 | 2024-10-01 05:06:00 | NOAA-21 | RIBEIRÃO CASCALHEIRA | MATO GROSSO | Brasil | 5107180 | 51 | 33 | nan | nan | nan | Cerrado | 4.0 |
| ecdeefea-3f7c-3ba0-b219-b178da01168e | -12.97533 | -51.42893 | 2024-10-01 05:06:00 | NOAA-21 | RIBEIRÃO CASCALHEIRA | MATO GROSSO | Brasil | 5107180 | 51 | 33 | nan | nan | nan | Cerrado | 2.8 |
| f7e41b48-50b3-3787-8722-6b3cb3f49913 | -12.97473 | -51.33664 | 2024-10-01 05:06:00 | NOAA-21 | RIBEIRÃO CASCALHEIRA | MATO GROSSO | Brasil | 5107180 | 51 | 33 | nan | nan | nan | Cerrado | 10.8 |
| ac655402-0765-373a-aba6-aaa3b682a473 | -12.97417 | -51.34068 | 2024-10-01 05:06:00 | NOAA-21 | RIBEIRÃO CASCALHEIRA | MATO GROSSO | Brasil | 5107180 | 51 | 33 | nan | nan | nan | Cerrado | 10.8 |
| fc648c22-3ed3-3a2d-98f9-3def189d3a03 | -12.9736 | -51.34258 | 2024-10-01 05:06:00 | NOAA-21 | RIBEIRÃO CASCALHEIRA | MATO GROSSO | Brasil | 5107180 | 51 | 33 | nan | nan | nan | Cerrado | 3.3 |
| e1f86c6f-921b-3711-b2a1-57692f8f27cc | -12.97248 | -51.25749 | 2024-10-01 05:06:00 | NOAA-21 | RIBEIRÃO CASCALHEIRA | MATO GROSSO | Brasil | 5107180 | 51 | 33 | nan | nan | nan | Cerrado | 7.7 |
| bbc3f1db-16d7-3288-9958-7af6578c1bbd | -12.97215 | -51.42033 | 2024-10-01 05:06:00 | NOAA-21 | RIBEIRÃO CASCALHEIRA | MATO GROSSO | Brasil | 5107180 | 51 | 33 | nan | nan | nan | Cerrado | 9.9 |
| 220fae16-47d2-3769-8a50-600089268fa9 | -12.97059 | -51.43231 | 2024-10-01 05:06:00 | NOAA-21 | RIBEIRÃO CASCALHEIRA | MATO GROSSO | Brasil | 5107180 | 51 | 33 | nan | nan | nan | Cerrado | 2.7 |
| 047e4224-1efb-3faf-89fa-c2d5afbef2f5 | -12.9701 | -51.30703 | 2024-10-01 05:06:00 | NOAA-21 | RIBEIRÃO CASCALHEIRA | MATO GROSSO | Brasil | 5107180 | 51 | 33 | nan | nan | nan | Cerrado | 4.7 |
| c2239f23-de77-3c8c-b197-c8f2628aa92f | -12.96955 | -51.31109 | 2024-10-01 05:06:00 | NOAA-21 | RIBEIRÃO CASCALHEIRA | MATO GROSSO | Brasil | 5107180 | 51 | 33 | nan | nan | nan | Cerrado | 6.0 |
| ccc9c5c3-691c-3e16-94ca-2eb2a0f797da | -12.96942 | -51.43821 | 2024-10-01 05:06:00 | NOAA-21 | RIBEIRÃO CASCALHEIRA | MATO GROSSO | Brasil | 5107180 | 51 | 33 | nan | nan | nan | Cerrado | 3.7 |
| 9c107e22-131a-3405-b642-8595448d58ec | -12.96899 | -51.31515 | 2024-10-01 05:06:00 | NOAA-21 | RIBEIRÃO CASCALHEIRA | MATO GROSSO | Brasil | 5107180 | 51 | 33 | nan | nan | nan | Cerrado | 6.0 |
| 6c95ea9b-0f51-35f3-8a37-df8d6073ad8e | -12.96792 | -51.41971 | 2024-10-01 05:06:00 | NOAA-21 | RIBEIRÃO CASCALHEIRA | MATO GROSSO | Brasil | 5107180 | 51 | 33 | nan | nan | nan | Cerrado | 12.9 |
| fdc6f3fc-7b03-3409-8bc0-f451b5fe6535 | -12.96662 | -51.36429 | 2024-10-01 05:06:00 | NOAA-21 | RIBEIRÃO CASCALHEIRA | MATO GROSSO | Brasil | 5107180 | 51 | 33 | nan | nan | nan | Cerrado | 8.4 |
| 52f96e90-7f2b-3d6f-a564-c180be423e2b | -12.96607 | -51.36832 | 2024-10-01 05:06:00 | NOAA-21 | RIBEIRÃO CASCALHEIRA | MATO GROSSO | Brasil | 5107180 | 51 | 33 | nan | nan | nan | Cerrado | 3.1 |


[Clique aqui para ver as próximas entradas](README113.md)
