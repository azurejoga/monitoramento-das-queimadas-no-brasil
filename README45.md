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

## Dados Diários - Página 45

| ID | Latitude | Longitude | Data/Hora GMT | Satélite | Município | Estado | País | Município ID | Estado ID | País ID | Dias sem Chuva | Precipitação | Risco de Fogo | Bioma | FRP |
|----|----------|-----------|---------------|----------|-----------|--------|------|--------------|-----------|---------|----------------|--------------|----------------|-------|-----|
| 6bc87761-0e87-3892-a394-f6cb99135a23 | -3.5668 | -53.7509 | 2024-10-21 04:36:00 | NOAA-20 | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | 1.3 |
| edf446a8-fefc-3083-ac50-87e92c424c1c | -3.56453 | -53.53802 | 2024-10-21 04:36:00 | NOAA-20 | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | 1.4 |
| 8429e0c4-e67a-3816-aa2e-c13d86f2bc56 | -1.72962 | -53.50919 | 2024-10-21 04:36:00 | NOAA-20 | PRAINHA | PARÁ | Brasil | 1506005 | 15 | 33 | nan | nan | nan | Amazônia | 1.7 |
| b61455e9-49ac-38cf-8647-59f367806581 | -1.72905 | -53.51276 | 2024-10-21 04:36:00 | NOAA-20 | PRAINHA | PARÁ | Brasil | 1506005 | 15 | 33 | nan | nan | nan | Amazônia | 1.1 |
| 42aab758-ba99-3400-be9e-c908b8e1fceb | -1.57988 | -53.50677 | 2024-10-21 04:36:00 | NOAA-20 | PRAINHA | PARÁ | Brasil | 1506005 | 15 | 33 | nan | nan | nan | Amazônia | 1.2 |
| a202f641-1c09-3065-8941-f8a5d356e7a0 | -1.57984 | -53.50711 | 2024-10-21 04:36:00 | NOAA-20 | PRAINHA | PARÁ | Brasil | 1506005 | 15 | 33 | nan | nan | nan | Amazônia | 2.7 |
| b980e751-8865-3e66-965d-369a95b05aa3 | -1.57584 | -53.50604 | 2024-10-21 04:36:00 | NOAA-20 | PRAINHA | PARÁ | Brasil | 1506005 | 15 | 33 | nan | nan | nan | Amazônia | 1.2 |
| c6315e41-c03f-3d1b-b004-eae22e388851 | -1.20857 | -53.37793 | 2024-10-21 04:36:00 | NOAA-20 | ALMEIRIM | PARÁ | Brasil | 1500503 | 15 | 33 | nan | nan | nan | Amazônia | 1.8 |
| 7a85abcf-1692-36bf-8828-f5dcc808c689 | -1.20466 | -53.64088 | 2024-10-21 04:36:00 | NOAA-20 | PRAINHA | PARÁ | Brasil | 1506005 | 15 | 33 | nan | nan | nan | Amazônia | 2.4 |
| 761f574f-a382-3c7f-af64-9e3ae1067a97 | -1.20411 | -53.64438 | 2024-10-21 04:36:00 | NOAA-20 | PRAINHA | PARÁ | Brasil | 1506005 | 15 | 33 | nan | nan | nan | Amazônia | 1.9 |
| b87b950d-031a-34cb-9846-6e53632032dd | -1.20356 | -53.64792 | 2024-10-21 04:36:00 | NOAA-20 | PRAINHA | PARÁ | Brasil | 1506005 | 15 | 33 | nan | nan | nan | Amazônia | 1.9 |
| f9081f9e-4211-3219-979e-6ad54628e2ce | -1.20054 | -53.64026 | 2024-10-21 04:36:00 | NOAA-20 | PRAINHA | PARÁ | Brasil | 1506005 | 15 | 33 | nan | nan | nan | Amazônia | 7.0 |
| f595adb8-07d8-3159-99f9-c34e56eeb7a4 | -1.19999 | -53.64376 | 2024-10-21 04:36:00 | NOAA-20 | PRAINHA | PARÁ | Brasil | 1506005 | 15 | 33 | nan | nan | nan | Amazônia | 2.1 |
| 541c3677-200b-39f7-a40e-c9d10a2e65d5 | -1.19943 | -53.64729 | 2024-10-21 04:36:00 | NOAA-20 | PRAINHA | PARÁ | Brasil | 1506005 | 15 | 33 | nan | nan | nan | Amazônia | 2.1 |
| c0eca97e-dca1-3038-b79d-0bce60e9c0de | -1.19698 | -53.63605 | 2024-10-21 04:36:00 | NOAA-20 | PRAINHA | PARÁ | Brasil | 1506005 | 15 | 33 | nan | nan | nan | Amazônia | 7.0 |
| d7bdb12d-bd28-372e-97cf-3b858078e08d | -1.19642 | -53.6396 | 2024-10-21 04:36:00 | NOAA-20 | PRAINHA | PARÁ | Brasil | 1506005 | 15 | 33 | nan | nan | nan | Amazônia | 7.0 |
| 1c9d26d2-42db-3f45-b3d9-3eaba8fdf772 | -1.19586 | -53.64315 | 2024-10-21 04:36:00 | NOAA-20 | PRAINHA | PARÁ | Brasil | 1506005 | 15 | 33 | nan | nan | nan | Amazônia | 2.1 |
| 9d2dfea8-6541-383b-9a4c-06ecc556dc22 | -1.19284 | -53.6355 | 2024-10-21 04:36:00 | NOAA-20 | PRAINHA | PARÁ | Brasil | 1506005 | 15 | 33 | nan | nan | nan | Amazônia | 3.7 |
| b7a7db1e-3d64-3a4f-bc62-4fc7ce923da6 | -1.19228 | -53.63909 | 2024-10-21 04:36:00 | NOAA-20 | PRAINHA | PARÁ | Brasil | 1506005 | 15 | 33 | nan | nan | nan | Amazônia | 3.7 |
| 6e186a81-3bdc-3a44-9728-e26a26d3ff30 | -1.19171 | -53.64268 | 2024-10-21 04:36:00 | NOAA-20 | PRAINHA | PARÁ | Brasil | 1506005 | 15 | 33 | nan | nan | nan | Amazônia | 1.5 |
| 659f6501-1b49-388e-8d8e-1426ae5a08be | -1.1887 | -53.63497 | 2024-10-21 04:36:00 | NOAA-20 | PRAINHA | PARÁ | Brasil | 1506005 | 15 | 33 | nan | nan | nan | Amazônia | 3.7 |
| 2d54b487-8724-3d63-a7c3-4d4b67330c6a | -1.18635 | -53.62318 | 2024-10-21 04:36:00 | NOAA-20 | ALMEIRIM | PARÁ | Brasil | 1500503 | 15 | 33 | nan | nan | nan | Amazônia | 3.6 |
| 97dc17eb-9d5c-3c90-be6c-ab15853da893 | -1.18575 | -53.62694 | 2024-10-21 04:36:00 | NOAA-20 | ALMEIRIM | PARÁ | Brasil | 1500503 | 15 | 33 | nan | nan | nan | Amazônia | 1.3 |
| 298de009-d6a9-387d-8b23-a4529cbf964d | -1.18516 | -53.63066 | 2024-10-21 04:36:00 | NOAA-20 | ALMEIRIM | PARÁ | Brasil | 1500503 | 15 | 33 | nan | nan | nan | Amazônia | 1.3 |
| da047ce7-2b01-331f-8bb2-7981453e9b79 | -1.18225 | -53.62238 | 2024-10-21 04:36:00 | NOAA-20 | ALMEIRIM | PARÁ | Brasil | 1500503 | 15 | 33 | nan | nan | nan | Amazônia | 3.6 |
| e80fe38e-6cc4-3f6a-9d18-4a7ffddb4d35 | -1.18165 | -53.62616 | 2024-10-21 04:36:00 | NOAA-20 | ALMEIRIM | PARÁ | Brasil | 1500503 | 15 | 33 | nan | nan | nan | Amazônia | 1.3 |
| 3635aebd-0217-3c98-9d01-38c6a666291c | -1.18105 | -53.62995 | 2024-10-21 04:36:00 | NOAA-20 | ALMEIRIM | PARÁ | Brasil | 1500503 | 15 | 33 | nan | nan | nan | Amazônia | 1.3 |
| 9e39927c-5a88-3610-a9f1-544ab2fa403b | -1.16825 | -53.65728 | 2024-10-21 04:36:00 | NOAA-20 | PRAINHA | PARÁ | Brasil | 1506005 | 15 | 33 | nan | nan | nan | Amazônia | 1.2 |
| dc1af0ee-c9eb-34f1-9abe-82e8778dec14 | -1.16767 | -53.66095 | 2024-10-21 04:36:00 | NOAA-20 | PRAINHA | PARÁ | Brasil | 1506005 | 15 | 33 | nan | nan | nan | Amazônia | 0.7 |
| c3a56ce9-cd0b-3265-a8b9-34aece02093c | -1.16474 | -53.65279 | 2024-10-21 04:36:00 | NOAA-20 | PRAINHA | PARÁ | Brasil | 1506005 | 15 | 33 | nan | nan | nan | Amazônia | 1.5 |
| 5b362082-d07e-33c7-ac14-be66ed1175cc | -1.16416 | -53.65641 | 2024-10-21 04:36:00 | NOAA-20 | PRAINHA | PARÁ | Brasil | 1506005 | 15 | 33 | nan | nan | nan | Amazônia | 1.5 |
| fe9f83b2-5f7e-39f8-b064-4ce8c3c484d5 | -1.16357 | -53.66009 | 2024-10-21 04:36:00 | NOAA-20 | PRAINHA | PARÁ | Brasil | 1506005 | 15 | 33 | nan | nan | nan | Amazônia | 0.3 |
| e2d9d9b5-0207-35c2-940d-05a09eeb8628 | -1.16005 | -53.65563 | 2024-10-21 04:36:00 | NOAA-20 | PRAINHA | PARÁ | Brasil | 1506005 | 15 | 33 | nan | nan | nan | Amazônia | 1.5 |
| 1adf843c-9c9d-32bf-ad03-28d68311d970 | -2.10309 | -53.96238 | 2024-10-21 04:36:00 | NOAA-20 | PRAINHA | PARÁ | Brasil | 1506005 | 15 | 33 | nan | nan | nan | Amazônia | 1.8 |
| 01f9b3a4-45f8-3326-a52d-1680e77fade7 | -2.07505 | -53.56371 | 2024-10-21 04:36:00 | NOAA-20 | PRAINHA | PARÁ | Brasil | 1506005 | 15 | 33 | nan | nan | nan | Amazônia | 0.8 |
| 87af8581-a9e9-35b5-8208-4bab3028f20b | -3.02112 | -54.34234 | 2024-10-21 04:36:00 | NOAA-20 | MOJUÍ DOS CAMPOS | PARÁ | Brasil | 1504752 | 15 | 33 | nan | nan | nan | Amazônia | 1.0 |
| 859c530e-1a5d-37f1-aea3-4a9118fc152f | -3.02048 | -54.34629 | 2024-10-21 04:36:00 | NOAA-20 | MOJUÍ DOS CAMPOS | PARÁ | Brasil | 1504752 | 15 | 33 | nan | nan | nan | Amazônia | 1.5 |
| bd27cc15-135c-3190-97d9-a710deff713a | -3.01984 | -54.35025 | 2024-10-21 04:36:00 | NOAA-20 | MOJUÍ DOS CAMPOS | PARÁ | Brasil | 1504752 | 15 | 33 | nan | nan | nan | Amazônia | 1.5 |
| e7c9429c-132d-3886-a316-faee9c92fbfd | -3.0192 | -54.35422 | 2024-10-21 04:36:00 | NOAA-20 | MOJUÍ DOS CAMPOS | PARÁ | Brasil | 1504752 | 15 | 33 | nan | nan | nan | Amazônia | 0.7 |
| ceffecdd-77d2-3270-88a6-447ab7633d56 | -3.01857 | -54.35811 | 2024-10-21 04:36:00 | NOAA-20 | MOJUÍ DOS CAMPOS | PARÁ | Brasil | 1504752 | 15 | 33 | nan | nan | nan | Amazônia | 0.7 |
| 1b9dc2a1-5e0f-3b05-b5ac-489f8e982336 | -3.01629 | -54.34558 | 2024-10-21 04:36:00 | NOAA-20 | MOJUÍ DOS CAMPOS | PARÁ | Brasil | 1504752 | 15 | 33 | nan | nan | nan | Amazônia | 1.5 |
| 6b3d40d3-9062-3c6c-83bf-c76b0eb88c15 | -3.01564 | -54.34956 | 2024-10-21 04:36:00 | NOAA-20 | MOJUÍ DOS CAMPOS | PARÁ | Brasil | 1504752 | 15 | 33 | nan | nan | nan | Amazônia | 1.5 |
| 52a509d8-0910-305f-a280-d4f25096ab9f | -3.015 | -54.35355 | 2024-10-21 04:36:00 | NOAA-20 | MOJUÍ DOS CAMPOS | PARÁ | Brasil | 1504752 | 15 | 33 | nan | nan | nan | Amazônia | 0.7 |
| 34709181-35c7-3288-9ba7-5aebff65f959 | -3.01437 | -54.35741 | 2024-10-21 04:36:00 | NOAA-20 | MOJUÍ DOS CAMPOS | PARÁ | Brasil | 1504752 | 15 | 33 | nan | nan | nan | Amazônia | 0.7 |
| 0f004ad9-56d9-3cb0-b567-dac647ca03c6 | -2.95103 | -54.15883 | 2024-10-21 04:36:00 | NOAA-20 | SANTARÉM | PARÁ | Brasil | 1506807 | 15 | 33 | nan | nan | nan | Amazônia | 2.1 |
| 3c092ee9-9ba6-30c2-83a4-e714e4d1bb76 | -2.95043 | -54.16261 | 2024-10-21 04:36:00 | NOAA-20 | SANTARÉM | PARÁ | Brasil | 1506807 | 15 | 33 | nan | nan | nan | Amazônia | 0.7 |
| 310d8083-0aa6-3976-a71c-99ba7d182b9b | -3.50256 | -54.68689 | 2024-10-21 04:36:00 | NOAA-20 | PLACAS | PARÁ | Brasil | 1505650 | 15 | 33 | nan | nan | nan | Amazônia | 0.8 |
| 782f4fd8-2efd-3239-8324-0d2d5d82b3e3 | -3.4187 | -54.27401 | 2024-10-21 04:36:00 | NOAA-20 | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | 1.4 |
| 681ea85d-ece3-3da3-87b1-e33b9d6e0b68 | -3.41808 | -54.27777 | 2024-10-21 04:36:00 | NOAA-20 | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | 1.4 |
| c935c5ae-5599-38d4-8354-9e0712b48837 | -3.29808 | -54.69332 | 2024-10-21 04:36:00 | NOAA-20 | MOJUÍ DOS CAMPOS | PARÁ | Brasil | 1504752 | 15 | 33 | nan | nan | nan | Amazônia | 2.1 |
| b4c7bf0a-14ce-3ca2-8944-8f17a3363555 | -3.27566 | -54.16093 | 2024-10-21 04:36:00 | NOAA-20 | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | 1.7 |
| 414550b9-8d0c-32a7-a93f-e386ddf9ee9b | -3.27213 | -54.15652 | 2024-10-21 04:36:00 | NOAA-20 | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | 1.4 |
| 7a2fb2d2-8044-31c3-8d91-9ee222201b43 | -3.26866 | -53.71078 | 2024-10-21 04:36:00 | NOAA-20 | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | 1.9 |
| 19e30db6-cb66-3f71-99ba-3bde24457be0 | -3.26623 | -53.78313 | 2024-10-21 04:36:00 | NOAA-20 | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | 1.4 |
| 6173ed10-60b9-30c7-9ea4-51178c9d086e | -3.26566 | -53.78658 | 2024-10-21 04:36:00 | NOAA-20 | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | 2.6 |
| ab0073ef-40c4-3f43-a183-ea05cb66a093 | -3.26487 | -53.78672 | 2024-10-21 04:36:00 | NOAA-20 | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | 3.9 |
| be94b7b4-b7b1-3c41-9ce0-2e92211e1e99 | -3.26138 | -53.78269 | 2024-10-21 04:36:00 | NOAA-20 | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | 5.7 |
| e19fef4b-e08e-37e8-9d59-92809ec710ed | -3.23087 | -54.14947 | 2024-10-21 04:36:00 | NOAA-20 | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | 1.0 |
| fe6ddbea-44a8-3461-ad5d-30b8011e33a9 | -3.14785 | -54.36234 | 2024-10-21 04:36:00 | NOAA-20 | MOJUÍ DOS CAMPOS | PARÁ | Brasil | 1504752 | 15 | 33 | nan | nan | nan | Amazônia | 1.5 |
| d7a76a3d-0fc4-3ce9-9ecb-38bb61e429b5 | -3.14366 | -54.36161 | 2024-10-21 04:36:00 | NOAA-20 | MOJUÍ DOS CAMPOS | PARÁ | Brasil | 1504752 | 15 | 33 | nan | nan | nan | Amazônia | 0.8 |
| 6b80e2c6-4ca2-3276-869e-844935aa628f | -3.13528 | -54.36016 | 2024-10-21 04:36:00 | NOAA-20 | MOJUÍ DOS CAMPOS | PARÁ | Brasil | 1504752 | 15 | 33 | nan | nan | nan | Amazônia | 0.6 |
| 66c78234-51d6-3055-8a38-0d6046c7cedc | -3.13515 | -54.2812 | 2024-10-21 04:36:00 | NOAA-20 | MOJUÍ DOS CAMPOS | PARÁ | Brasil | 1504752 | 15 | 33 | nan | nan | nan | Amazônia | 3.9 |
| 2a9a408e-454c-3bed-859a-bda4400fe3d3 | -3.10424 | -54.18291 | 2024-10-21 04:36:00 | NOAA-20 | SANTARÉM | PARÁ | Brasil | 1506807 | 15 | 33 | nan | nan | nan | Amazônia | 23.9 |
| d4a4876f-b4d7-3b7d-8262-871e1ac345fe | -3.10361 | -54.18674 | 2024-10-21 04:36:00 | NOAA-20 | SANTARÉM | PARÁ | Brasil | 1506807 | 15 | 33 | nan | nan | nan | Amazônia | 4.1 |
| 384784fe-966e-325c-86cc-34f50ef28708 | -3.10258 | -54.16722 | 2024-10-21 04:36:00 | NOAA-20 | SANTARÉM | PARÁ | Brasil | 1506807 | 15 | 33 | nan | nan | nan | Amazônia | 2.0 |
| 79c1d49a-8dba-350f-b6c9-7d88099337f4 | -3.10136 | -54.17462 | 2024-10-21 04:36:00 | NOAA-20 | SANTARÉM | PARÁ | Brasil | 1506807 | 15 | 33 | nan | nan | nan | Amazônia | 11.2 |
| 4b90fff7-e282-3fd7-82f3-dd454be947fe | -3.10051 | -54.16704 | 2024-10-21 04:36:00 | NOAA-20 | SANTARÉM | PARÁ | Brasil | 1506807 | 15 | 33 | nan | nan | nan | Amazônia | 1.2 |
| dcc81538-08f0-3753-9cf0-2ffdf68d6ef2 | -3.09948 | -54.18596 | 2024-10-21 04:36:00 | NOAA-20 | SANTARÉM | PARÁ | Brasil | 1506807 | 15 | 33 | nan | nan | nan | Amazônia | 4.1 |
| 99fa68e6-e1de-3f23-9e7a-e19598f7f344 | -3.09904 | -54.1629 | 2024-10-21 04:36:00 | NOAA-20 | SANTARÉM | PARÁ | Brasil | 1506807 | 15 | 33 | nan | nan | nan | Amazônia | 5.4 |
| 1a77b76f-cc6b-3eca-9abc-60e31ce2f927 | -3.09783 | -54.17023 | 2024-10-21 04:36:00 | NOAA-20 | SANTARÉM | PARÁ | Brasil | 1506807 | 15 | 33 | nan | nan | nan | Amazônia | 26.0 |
| 2fa813fe-68c7-39f2-85af-087e2286b4d8 | -3.09755 | -54.18577 | 2024-10-21 04:36:00 | NOAA-20 | SANTARÉM | PARÁ | Brasil | 1506807 | 15 | 33 | nan | nan | nan | Amazônia | 9.5 |
| 234a71b4-c5b4-3a5c-816d-a7729a5ea5da | -3.09721 | -54.17394 | 2024-10-21 04:36:00 | NOAA-20 | SANTARÉM | PARÁ | Brasil | 1506807 | 15 | 33 | nan | nan | nan | Amazônia | 26.0 |
| 5eb201f5-4530-31f4-a677-b710ae43793b | -3.09659 | -54.17766 | 2024-10-21 04:36:00 | NOAA-20 | SANTARÉM | PARÁ | Brasil | 1506807 | 15 | 33 | nan | nan | nan | Amazônia | 65.6 |
| c8f2fe73-a791-3994-843f-66c7610f644a | -3.09636 | -54.16637 | 2024-10-21 04:36:00 | NOAA-20 | SANTARÉM | PARÁ | Brasil | 1506807 | 15 | 33 | nan | nan | nan | Amazônia | 1.2 |
| 12597a30-dad6-3bb2-874a-f0616e39a776 | -3.09597 | -54.18142 | 2024-10-21 04:36:00 | NOAA-20 | SANTARÉM | PARÁ | Brasil | 1506807 | 15 | 33 | nan | nan | nan | Amazônia | 65.6 |
| 885f6cd1-4817-37f1-b535-ad9d19b1933b | -3.094 | -54.18126 | 2024-10-21 04:36:00 | NOAA-20 | SANTARÉM | PARÁ | Brasil | 1506807 | 15 | 33 | nan | nan | nan | Amazônia | 93.7 |
| bb4dc552-d540-3b91-88b8-08192597367e | -3.09337 | -54.1584 | 2024-10-21 04:36:00 | NOAA-20 | SANTARÉM | PARÁ | Brasil | 1506807 | 15 | 33 | nan | nan | nan | Amazônia | 3.9 |
| fedeb287-541a-34b3-b4ee-61d5c120cea8 | -3.09306 | -54.17328 | 2024-10-21 04:36:00 | NOAA-20 | SANTARÉM | PARÁ | Brasil | 1506807 | 15 | 33 | nan | nan | nan | Amazônia | 26.0 |
| 19ad90b4-8668-387c-9685-0605bd8d28dc | -3.09279 | -54.16206 | 2024-10-21 04:36:00 | NOAA-20 | SANTARÉM | PARÁ | Brasil | 1506807 | 15 | 33 | nan | nan | nan | Amazônia | 36.3 |
| dfed3194-843e-3759-a0ef-fbc0d0ffd5d7 | -3.09221 | -54.19261 | 2024-10-21 04:36:00 | NOAA-20 | SANTARÉM | PARÁ | Brasil | 1506807 | 15 | 33 | nan | nan | nan | Amazônia | 2.3 |
| 2e15a30b-33fc-3fb5-a665-d378cac84703 | -3.09221 | -54.16573 | 2024-10-21 04:36:00 | NOAA-20 | SANTARÉM | PARÁ | Brasil | 1506807 | 15 | 33 | nan | nan | nan | Amazônia | 36.3 |
| d7062df9-b466-34f6-b50a-383b362bd98c | -3.09182 | -54.18074 | 2024-10-21 04:36:00 | NOAA-20 | SANTARÉM | PARÁ | Brasil | 1506807 | 15 | 33 | nan | nan | nan | Amazônia | 65.6 |
| 0900d850-e30f-3837-94be-96242e6a055e | -3.09057 | -54.18828 | 2024-10-21 04:36:00 | NOAA-20 | SANTARÉM | PARÁ | Brasil | 1506807 | 15 | 33 | nan | nan | nan | Amazônia | 9.7 |
| 5ed36f6b-1b40-3498-a48b-19e9e17a732f | -3.08985 | -54.18059 | 2024-10-21 04:36:00 | NOAA-20 | SANTARÉM | PARÁ | Brasil | 1506807 | 15 | 33 | nan | nan | nan | Amazônia | 21.7 |
| a72a5971-15f7-3f04-8745-c248bc1fd435 | -3.08925 | -54.18436 | 2024-10-21 04:36:00 | NOAA-20 | SANTARÉM | PARÁ | Brasil | 1506807 | 15 | 33 | nan | nan | nan | Amazônia | 3.7 |
| 197d7d95-686e-3fed-80ed-95fc88a35b3a | -3.08923 | -54.15773 | 2024-10-21 04:36:00 | NOAA-20 | SANTARÉM | PARÁ | Brasil | 1506807 | 15 | 33 | nan | nan | nan | Amazônia | 3.9 |
| 9871cca2-e7cc-3bc1-bcfd-7407f93c3e99 | -3.08864 | -54.16142 | 2024-10-21 04:36:00 | NOAA-20 | SANTARÉM | PARÁ | Brasil | 1506807 | 15 | 33 | nan | nan | nan | Amazônia | 36.3 |
| 48bc6125-b9ea-3ddf-a416-b204a2a1f02f | -3.08823 | -54.437 | 2024-10-21 04:36:00 | NOAA-20 | MOJUÍ DOS CAMPOS | PARÁ | Brasil | 1504752 | 15 | 33 | nan | nan | nan | Amazônia | 1.2 |
| 9c12fc94-428d-3e0d-a343-9239240dabdd | -3.08806 | -54.19191 | 2024-10-21 04:36:00 | NOAA-20 | SANTARÉM | PARÁ | Brasil | 1506807 | 15 | 33 | nan | nan | nan | Amazônia | 1.7 |
| 20445e83-3e8a-370b-acb5-0f4903233542 | -3.08806 | -54.16511 | 2024-10-21 04:36:00 | NOAA-20 | SANTARÉM | PARÁ | Brasil | 1506807 | 15 | 33 | nan | nan | nan | Amazônia | 36.3 |
| a579deaf-b803-3216-8de4-ff0fd0f25439 | -3.08747 | -54.16877 | 2024-10-21 04:36:00 | NOAA-20 | SANTARÉM | PARÁ | Brasil | 1506807 | 15 | 33 | nan | nan | nan | Amazônia | 31.9 |
| 438460ef-33ff-3c19-98bd-a8b72af9e1fc | -3.08688 | -54.17247 | 2024-10-21 04:36:00 | NOAA-20 | SANTARÉM | PARÁ | Brasil | 1506807 | 15 | 33 | nan | nan | nan | Amazônia | 31.9 |
| 53b69fc3-6dd6-34ac-a18e-f1e40ceb3354 | -3.0851 | -54.18367 | 2024-10-21 04:36:00 | NOAA-20 | SANTARÉM | PARÁ | Brasil | 1506807 | 15 | 33 | nan | nan | nan | Amazônia | 3.7 |
| a9d69e1b-423a-3c4b-b552-8eb5bd69f56d | -3.0845 | -54.18744 | 2024-10-21 04:36:00 | NOAA-20 | SANTARÉM | PARÁ | Brasil | 1506807 | 15 | 33 | nan | nan | nan | Amazônia | 3.7 |
| 342d518b-183a-3586-a5e6-154f6d4ecd84 | -3.0845 | -54.16075 | 2024-10-21 04:36:00 | NOAA-20 | SANTARÉM | PARÁ | Brasil | 1506807 | 15 | 33 | nan | nan | nan | Amazônia | 3.9 |
| a7f7cb35-15ca-33ac-8bc6-500e1c0a75da | -3.084 | -54.43633 | 2024-10-21 04:36:00 | NOAA-20 | MOJUÍ DOS CAMPOS | PARÁ | Brasil | 1504752 | 15 | 33 | nan | nan | nan | Amazônia | 1.2 |
| 32281c97-2198-302c-a5fd-d5742ce4c927 | -3.08332 | -54.16813 | 2024-10-21 04:36:00 | NOAA-20 | SANTARÉM | PARÁ | Brasil | 1506807 | 15 | 33 | nan | nan | nan | Amazônia | 12.9 |
| d5022c5c-4a8c-37d5-9607-353a72dcc66d | -3.07858 | -54.17116 | 2024-10-21 04:36:00 | NOAA-20 | SANTARÉM | PARÁ | Brasil | 1506807 | 15 | 33 | nan | nan | nan | Amazônia | 12.9 |
| a8b4421e-05a6-35dd-b5bc-459686a3dd9c | -3.07799 | -54.17487 | 2024-10-21 04:36:00 | NOAA-20 | SANTARÉM | PARÁ | Brasil | 1506807 | 15 | 33 | nan | nan | nan | Amazônia | 14.7 |
| b7d67676-9fbc-30cd-b78a-7d4a07f1061f | -3.0774 | -54.17859 | 2024-10-21 04:36:00 | NOAA-20 | SANTARÉM | PARÁ | Brasil | 1506807 | 15 | 33 | nan | nan | nan | Amazônia | 14.7 |


[Clique aqui para ver as próximas entradas](README46.md)
