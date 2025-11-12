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

## Dados Diários - Página 15

| ID | Latitude | Longitude | Data/Hora GMT | Satélite | Município | Estado | País | Município ID | Estado ID | País ID | Dias sem Chuva | Precipitação | Risco de Fogo | Bioma | FRP |
|----|----------|-----------|---------------|----------|-----------|--------|------|--------------|-----------|---------|----------------|--------------|----------------|-------|-----|
| 195ce514-dc55-359f-a58b-f4c12afb0f24 | -2.95389 | -45.55463 | 2025-11-12 04:31:00 | NOAA-21 | PEDRO DO ROSÁRIO | MARANHÃO | Brasil | 2108256 | 21 | 33 | nan | nan | nan | Amazônia | 2.0 |
| d726a491-744e-31ff-ba16-9b2f61f0e645 | -3.03781 | -51.03115 | 2025-11-12 04:31:00 | NOAA-21 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 3.4 |
| 472f3e1a-8c0b-36f6-aebb-8c8cd9f67455 | -3.26147 | -44.12547 | 2025-11-12 04:31:00 | NOAA-21 | ITAPECURU MIRIM | MARANHÃO | Brasil | 2105401 | 21 | 33 | nan | nan | nan | Amazônia | 1.4 |
| 4d0127b4-8460-3602-82fb-ae494408239c | -4.95527 | -43.72015 | 2025-11-12 04:31:00 | NOAA-21 | SÃO JOÃO DO SOTER | MARANHÃO | Brasil | 2111078 | 21 | 33 | nan | nan | nan | Cerrado | 6.6 |
| 04c2c7d1-413f-33ae-8e14-ab3145312d11 | -7.28598 | -41.58102 | 2025-11-12 04:31:00 | NOAA-21 | AROEIRAS DO ITAIM | PIAUÍ | Brasil | 2200954 | 22 | 33 | nan | nan | nan | Caatinga | 3.4 |
| 7d72969b-4b15-3035-b2ec-1076e9b59ca3 | -7.4587 | -44.74429 | 2025-11-12 04:31:00 | NOAA-21 | URUÇUÍ | PIAUÍ | Brasil | 2211209 | 22 | 33 | nan | nan | nan | Cerrado | 2.2 |
| 144ea600-2079-3755-bd67-1204742a44cf | -7.13114 | -41.86898 | 2025-11-12 04:31:00 | NOAA-21 | SANTA CRUZ DO PIAUÍ | PIAUÍ | Brasil | 2209104 | 22 | 33 | nan | nan | nan | Caatinga | 5.7 |
| 507fbf9f-9d5f-3e2f-8803-c39be3ff23cd | -6.00071 | -51.51804 | 2025-11-12 04:31:00 | NOAA-21 | SÃO FÉLIX DO XINGU | PARÁ | Brasil | 1507300 | 15 | 33 | nan | nan | nan | Amazônia | 0.9 |
| 5d7c81f5-7520-38bb-ac44-baa0c22d8c08 | -9.89691 | -47.86428 | 2025-11-12 04:31:00 | NOAA-21 | APARECIDA DO RIO NEGRO | TOCANTINS | Brasil | 1701101 | 17 | 33 | nan | nan | nan | Cerrado | 1.0 |
| bd873f04-822d-34ee-85fc-fc59de8fe17a | -6.09507 | -41.58076 | 2025-11-12 04:31:00 | NOAA-21 | PIMENTEIRAS | PIAUÍ | Brasil | 2208106 | 22 | 33 | nan | nan | nan | Caatinga | 1.8 |
| 90387bc6-1db2-3c79-a9ee-528775043ff3 | -4.28115 | -50.53412 | 2025-11-12 04:31:00 | NOAA-21 | NOVO REPARTIMENTO | PARÁ | Brasil | 1505064 | 15 | 33 | nan | nan | nan | Amazônia | 1.9 |
| c9bc8ca1-dd75-381e-b269-6f0593914424 | -3.64773 | -50.18034 | 2025-11-12 04:31:00 | NOAA-21 | PACAJÁ | PARÁ | Brasil | 1505486 | 15 | 33 | nan | nan | nan | Amazônia | 1.5 |
| 09d5283b-3fda-3433-981d-1747a6cbe334 | -4.15579 | -48.2228 | 2025-11-12 04:31:00 | NOAA-21 | DOM ELISEU | PARÁ | Brasil | 1502939 | 15 | 33 | nan | nan | nan | Amazônia | 1.9 |
| a7b28b8d-9f06-3dd8-823c-e1bd9d4cb4cd | -7.13861 | -41.25134 | 2025-11-12 04:31:00 | NOAA-21 | GEMINIANO | PIAUÍ | Brasil | 2204352 | 22 | 33 | nan | nan | nan | Caatinga | 1.5 |
| bf9a448b-a076-36bc-a480-09743d9dcb97 | -4.11258 | -48.02272 | 2025-11-12 04:31:00 | NOAA-21 | DOM ELISEU | PARÁ | Brasil | 1502939 | 15 | 33 | nan | nan | nan | Amazônia | 0.6 |
| 98fa0890-01f6-3a80-a951-889cad8e70bd | -2.84007 | -49.5138 | 2025-11-12 04:31:00 | NOAA-21 | BAIÃO | PARÁ | Brasil | 1501204 | 15 | 33 | nan | nan | nan | Amazônia | 1.2 |
| 6577ba37-f8e3-3fc6-826f-e77e91aafe16 | -2.46278 | -52.17919 | 2025-11-12 04:31:00 | NOAA-21 | PORTO DE MOZ | PARÁ | Brasil | 1505908 | 15 | 33 | nan | nan | nan | Amazônia | 0.9 |
| 187113f1-732b-3281-ad99-544e86f7c70e | -3.70621 | -50.1511 | 2025-11-12 04:31:00 | NOAA-21 | PACAJÁ | PARÁ | Brasil | 1505486 | 15 | 33 | nan | nan | nan | Amazônia | 1.3 |
| 60352ce2-d4ff-3511-9378-893529a20019 | -3.23915 | -50.0359 | 2025-11-12 04:31:00 | NOAA-21 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 4.1 |
| 947575ea-a641-39ac-b09d-0729d50342bd | -5.61439 | -41.07156 | 2025-11-12 04:31:00 | NOAA-21 | SÃO MIGUEL DO TAPUIO | PIAUÍ | Brasil | 2210409 | 22 | 33 | nan | nan | nan | Caatinga | 1.8 |
| 5a4ebbee-c886-3bdf-850c-d2bd5a79601b | -2.95053 | -45.5541 | 2025-11-12 04:31:00 | NOAA-21 | PEDRO DO ROSÁRIO | MARANHÃO | Brasil | 2108256 | 21 | 33 | nan | nan | nan | Amazônia | 13.1 |
| 8bc80c79-5c52-3229-907f-de4b017ba0a9 | -4.09985 | -48.01717 | 2025-11-12 04:31:00 | NOAA-21 | DOM ELISEU | PARÁ | Brasil | 1502939 | 15 | 33 | nan | nan | nan | Amazônia | 2.9 |
| cea9f22f-f5f7-315d-9091-9ab34ec1a6df | -5.35926 | -49.06963 | 2025-11-12 04:31:00 | NOAA-21 | MARABÁ | PARÁ | Brasil | 1504208 | 15 | 33 | nan | nan | nan | Amazônia | 1.2 |
| e4a7fba7-7771-3073-9d21-e2aeb109c30c | -8.00756 | -43.34845 | 2025-11-12 04:31:00 | NOAA-21 | PAVUSSU | PIAUÍ | Brasil | 2207850 | 22 | 33 | nan | nan | nan | Caatinga | 1.5 |
| 864d20b4-3eec-3bcd-a162-ce9bb7034965 | -3.08863 | -49.45551 | 2025-11-12 04:31:00 | NOAA-21 | MOJU | PARÁ | Brasil | 1504703 | 15 | 33 | nan | nan | nan | Amazônia | 1.6 |
| 42841a45-f4ac-3eda-bf36-0f70b49cd7af | -2.97723 | -44.58587 | 2025-11-12 04:31:00 | NOAA-21 | CAJAPIÓ | MARANHÃO | Brasil | 2102408 | 21 | 33 | nan | nan | nan | Amazônia | 2.4 |
| 532ed96c-0351-3da3-ab81-5d0aa2810bab | -5.89268 | -42.25539 | 2025-11-12 04:31:00 | NOAA-21 | SÃO MIGUEL DA BAIXA GRANDE | PIAUÍ | Brasil | 2210383 | 22 | 33 | nan | nan | nan | Caatinga | 2.4 |
| aca43ae1-b579-3173-b621-5aec0d388575 | -2.79835 | -48.94113 | 2025-11-12 04:31:00 | NOAA-21 | TAILÂNDIA | PARÁ | Brasil | 1507953 | 15 | 33 | nan | nan | nan | Amazônia | 0.7 |
| d39e8f63-ce65-3bb3-9906-21657575c04b | -6.09735 | -41.56452 | 2025-11-12 04:31:00 | NOAA-21 | SÃO MIGUEL DO TAPUIO | PIAUÍ | Brasil | 2210409 | 22 | 33 | nan | nan | nan | Caatinga | 2.1 |
| 3e77117b-ddef-39b7-802c-4e3c4642a6dc | -2.602 | -49.22821 | 2025-11-12 04:31:00 | NOAA-21 | MOJU | PARÁ | Brasil | 1504703 | 15 | 33 | nan | nan | nan | Amazônia | 1.5 |
| faee97c1-8b59-365a-8ddb-f00a4a6bace7 | -9.149 | -50.01816 | 2025-11-12 04:31:00 | NOAA-21 | SANTANA DO ARAGUAIA | PARÁ | Brasil | 1506708 | 15 | 33 | nan | nan | nan | Amazônia | 1.3 |
| a8192db4-2593-3b64-9bed-dd2751cbe941 | -4.14606 | -47.65894 | 2025-11-12 04:31:00 | NOAA-21 | DOM ELISEU | PARÁ | Brasil | 1502939 | 15 | 33 | nan | nan | nan | Amazônia | 2.6 |
| 26e79cda-3c6e-3539-b40d-f8494b0f1469 | -4.10539 | -48.02519 | 2025-11-12 04:31:00 | NOAA-21 | DOM ELISEU | PARÁ | Brasil | 1502939 | 15 | 33 | nan | nan | nan | Amazônia | 1.5 |
| 91e09f5e-772d-3807-8a4a-f6aa67acc9e7 | -4.11203 | -48.02623 | 2025-11-12 04:31:00 | NOAA-21 | DOM ELISEU | PARÁ | Brasil | 1502939 | 15 | 33 | nan | nan | nan | Amazônia | 0.6 |
| bb86c07e-7d5d-3073-88b1-3ffc59db5365 | -3.64121 | -50.17506 | 2025-11-12 04:31:00 | NOAA-21 | PACAJÁ | PARÁ | Brasil | 1505486 | 15 | 33 | nan | nan | nan | Amazônia | 3.8 |
| fdbba8d7-6f58-3471-9e86-e8c2640cd45f | -9.67625 | -43.90205 | 2025-11-12 04:31:00 | NOAA-21 | MORRO CABEÇA NO TEMPO | PIAUÍ | Brasil | 2206654 | 22 | 33 | nan | nan | nan | Caatinga | 1.0 |
| 2600e301-ef6b-33db-bcb3-22f8d9695ccb | -9.83664 | -44.27218 | 2025-11-12 04:31:00 | NOAA-21 | CURIMATÁ | PIAUÍ | Brasil | 2203206 | 22 | 33 | nan | nan | nan | Cerrado | 2.2 |
| 63422294-470d-3b68-be50-4c020bf39c3a | -4.10813 | -48.00777 | 2025-11-12 04:31:00 | NOAA-21 | DOM ELISEU | PARÁ | Brasil | 1502939 | 15 | 33 | nan | nan | nan | Amazônia | 2.3 |
| 000d2898-4522-38b6-8a5a-81812b1ff81e | -6.09739 | -41.57909 | 2025-11-12 04:31:00 | NOAA-21 | PIMENTEIRAS | PIAUÍ | Brasil | 2208106 | 22 | 33 | nan | nan | nan | Caatinga | 2.9 |
| 23cddb39-6f57-30dc-a9ca-f49f2826ed8c | -6.10167 | -41.56518 | 2025-11-12 04:31:00 | NOAA-21 | PIMENTEIRAS | PIAUÍ | Brasil | 2208106 | 22 | 33 | nan | nan | nan | Caatinga | 2.1 |
| 7b515bda-47df-363e-872a-9ce8dbbb29a4 | -4.33006 | -45.48687 | 2025-11-12 04:31:00 | NOAA-21 | BREJO DE AREIA | MARANHÃO | Brasil | 2102150 | 21 | 33 | nan | nan | nan | Amazônia | 2.4 |
| ab5067f1-ede0-37cf-87e9-9390ea756f95 | -7.07329 | -41.58729 | 2025-11-12 04:31:00 | NOAA-21 | PICOS | PIAUÍ | Brasil | 2208007 | 22 | 33 | nan | nan | nan | Caatinga | 2.9 |
| e5d8f58e-46e1-3889-a4b7-dcc0a8f3ff7d | -9.668 | -43.89866 | 2025-11-12 04:31:00 | NOAA-21 | MORRO CABEÇA NO TEMPO | PIAUÍ | Brasil | 2206654 | 22 | 33 | nan | nan | nan | Caatinga | 3.3 |
| 51ad2f69-0a97-3f4d-9a89-f194a6a90f27 | -3.08969 | -49.2708 | 2025-11-12 04:31:00 | NOAA-21 | MOJU | PARÁ | Brasil | 1504703 | 15 | 33 | nan | nan | nan | Amazônia | 3.8 |
| fa6f2f7e-a639-3df8-aa15-94c201bb9f80 | -2.87655 | -51.4782 | 2025-11-12 04:31:00 | NOAA-21 | ANAPU | PARÁ | Brasil | 1500859 | 15 | 33 | nan | nan | nan | Amazônia | 4.4 |
| 4be4fbc9-f7ea-3b1c-bd32-37f2edfa1649 | -6.11322 | -41.54589 | 2025-11-12 04:31:00 | NOAA-21 | PIMENTEIRAS | PIAUÍ | Brasil | 2208106 | 22 | 33 | nan | nan | nan | Caatinga | 1.8 |
| 6a9701fc-3c02-35a6-995b-5ee7ef85ba42 | -6.23116 | -51.53416 | 2025-11-12 04:31:00 | NOAA-21 | SÃO FÉLIX DO XINGU | PARÁ | Brasil | 1507300 | 15 | 33 | nan | nan | nan | Amazônia | 0.7 |
| cdb3fa8e-f3ba-3c55-938e-93fed112df61 | -6.31684 | -43.8134 | 2025-11-12 04:31:00 | NOAA-21 | SÃO JOÃO DOS PATOS | MARANHÃO | Brasil | 2111102 | 21 | 33 | nan | nan | nan | Cerrado | 10.2 |
| 3d9083dc-6d4d-3848-9914-187529265c02 | -7.13235 | -41.86069 | 2025-11-12 04:31:00 | NOAA-21 | SANTA CRUZ DO PIAUÍ | PIAUÍ | Brasil | 2209104 | 22 | 33 | nan | nan | nan | Caatinga | 2.0 |
| 91a52b90-1747-311f-8b18-99770dce54e3 | -2.40143 | -49.39902 | 2025-11-12 04:31:00 | NOAA-21 | CAMETÁ | PARÁ | Brasil | 1502103 | 15 | 33 | nan | nan | nan | Amazônia | 1.1 |
| 0e36d7f6-3358-3a17-90f6-1aae960ca388 | -3.21059 | -43.52383 | 2025-11-12 04:31:00 | NOAA-21 | BELÁGUA | MARANHÃO | Brasil | 2101731 | 21 | 33 | nan | nan | nan | Cerrado | 1.4 |
| fec1c50a-fa12-3c85-8062-7ebcd133683d | -2.95164 | -45.54697 | 2025-11-12 04:31:00 | NOAA-21 | PEDRO DO ROSÁRIO | MARANHÃO | Brasil | 2108256 | 21 | 33 | nan | nan | nan | Amazônia | 1.9 |
| eb7277e8-6c50-3d1f-b605-bfeb54beb0c8 | -4.64798 | -47.95052 | 2025-11-12 04:31:00 | NOAA-21 | RONDON DO PARÁ | PARÁ | Brasil | 1506187 | 15 | 33 | nan | nan | nan | Amazônia | 7.4 |
| 431244de-968f-3983-bb33-603b6099d9f2 | -3.26498 | -44.67485 | 2025-11-12 04:31:00 | NOAA-21 | ANAJATUBA | MARANHÃO | Brasil | 2100709 | 21 | 33 | nan | nan | nan | Amazônia | 1.0 |
| 352af214-a6e2-391f-b11e-ca602bf4d9ea | -6.68231 | -42.0118 | 2025-11-12 04:31:00 | NOAA-21 | OEIRAS | PIAUÍ | Brasil | 2207009 | 22 | 33 | nan | nan | nan | Caatinga | 1.4 |
| a36276dc-3860-318e-bb4a-80fb35d099a7 | -4.95593 | -43.71572 | 2025-11-12 04:31:00 | NOAA-21 | SÃO JOÃO DO SOTER | MARANHÃO | Brasil | 2111078 | 21 | 33 | nan | nan | nan | Cerrado | 2.0 |
| 49c90e81-769b-334b-813d-84df2717cbf5 | -7.43197 | -42.53786 | 2025-11-12 04:31:00 | NOAA-21 | SÃO JOSÉ DO PEIXE | PIAUÍ | Brasil | 2210102 | 22 | 33 | nan | nan | nan | Caatinga | 1.9 |
| 843a338c-f7d8-3167-87b4-2dbd4c1d013b | -3.49484 | -55.41785 | 2025-11-12 04:31:00 | NOAA-21 | AVEIRO | PARÁ | Brasil | 1501006 | 15 | 33 | nan | nan | nan | Amazônia | 2.7 |
| 2cfc7c24-f131-3b31-8bd8-cc360f20c7ca | -4.96571 | -43.72632 | 2025-11-12 04:31:00 | NOAA-21 | SÃO JOÃO DO SOTER | MARANHÃO | Brasil | 2111078 | 21 | 33 | nan | nan | nan | Cerrado | 8.6 |
| eb142c38-b731-33da-844a-916744d17c74 | -4.63968 | -45.66456 | 2025-11-12 04:31:00 | NOAA-21 | MARAJÁ DO SENA | MARANHÃO | Brasil | 2106359 | 21 | 33 | nan | nan | nan | Amazônia | 0.7 |
| 60450fa4-bf2a-3b91-a5e7-6cc8fee26542 | -10.45616 | -44.96477 | 2025-11-12 04:31:00 | NOAA-21 | CORRENTE | PIAUÍ | Brasil | 2202901 | 22 | 33 | nan | nan | nan | Cerrado | 1.9 |
| b140edac-e1c7-334d-b304-9bad09d94bfb | -2.64321 | -49.21502 | 2025-11-12 04:31:00 | NOAA-21 | MOJU | PARÁ | Brasil | 1504703 | 15 | 33 | nan | nan | nan | Amazônia | 1.1 |
| 52f082cd-cc95-3526-9086-b37eb7439c2c | -7.3083 | -45.2865 | 2025-11-12 04:31:00 | NOAA-21 | LORETO | MARANHÃO | Brasil | 2106102 | 21 | 33 | nan | nan | nan | Cerrado | 0.7 |
| dc34b71d-8cd9-3fcd-9599-5a40c64c0240 | -10.19229 | -44.89822 | 2025-11-12 04:31:00 | NOAA-21 | RIACHO FRIO | PIAUÍ | Brasil | 2208858 | 22 | 33 | nan | nan | nan | Cerrado | 1.8 |
| f7b65bc3-16e0-3499-8c46-0e61b98bac32 | -7.281 | -41.58469 | 2025-11-12 04:31:00 | NOAA-21 | AROEIRAS DO ITAIM | PIAUÍ | Brasil | 2200954 | 22 | 33 | nan | nan | nan | Caatinga | 3.4 |
| 0123b9be-7cde-3781-81a2-7da810ab0086 | -5.61066 | -47.28032 | 2025-11-12 04:31:00 | NOAA-21 | DAVINÓPOLIS | MARANHÃO | Brasil | 2103752 | 21 | 33 | nan | nan | nan | Cerrado | 0.6 |
| 2ef9f6fe-de1a-351e-b5f6-8df01fcbf3ab | -2.64273 | -49.19538 | 2025-11-12 04:31:00 | NOAA-21 | MOJU | PARÁ | Brasil | 1504703 | 15 | 33 | nan | nan | nan | Amazônia | 4.0 |
| 384d5fa3-c566-3eef-aa98-4f3d5cfcb5f1 | -7.28538 | -41.58538 | 2025-11-12 04:31:00 | NOAA-21 | AROEIRAS DO ITAIM | PIAUÍ | Brasil | 2200954 | 22 | 33 | nan | nan | nan | Caatinga | 3.4 |
| 49381369-be00-3c07-a7e5-7056a51c0537 | -4.72765 | -42.82277 | 2025-11-12 04:31:00 | NOAA-21 | UNIÃO | PIAUÍ | Brasil | 2211100 | 22 | 33 | nan | nan | nan | Cerrado | 3.5 |
| f1f96df9-bec6-35ed-8dcb-a610e5765ac6 | -3.49532 | -55.41489 | 2025-11-12 04:31:00 | NOAA-21 | AVEIRO | PARÁ | Brasil | 1501006 | 15 | 33 | nan | nan | nan | Amazônia | 3.0 |
| a1870090-62d7-3d6b-b398-d4c9a93ab0e2 | -3.77393 | -48.92187 | 2025-11-12 04:31:00 | NOAA-21 | GOIANÉSIA DO PARÁ | PARÁ | Brasil | 1503093 | 15 | 33 | nan | nan | nan | Amazônia | 1.6 |
| 8b09675e-1398-3ca0-9f87-fc43b1e7f7ac | -2.95445 | -45.55106 | 2025-11-12 04:31:00 | NOAA-21 | PEDRO DO ROSÁRIO | MARANHÃO | Brasil | 2108256 | 21 | 33 | nan | nan | nan | Amazônia | 1.3 |
| 13b361fc-f027-31ed-8b0c-4e2f7b5e67a1 | -8.73444 | -48.31824 | 2025-11-12 04:31:00 | NOAA-21 | GUARAÍ | TOCANTINS | Brasil | 1709302 | 17 | 33 | nan | nan | nan | Cerrado | 0.7 |
| cbe9aa2f-5654-3f2a-b12c-e31b510a979b | -2.44004 | -49.33726 | 2025-11-12 04:31:00 | NOAA-21 | CAMETÁ | PARÁ | Brasil | 1502103 | 15 | 33 | nan | nan | nan | Amazônia | 0.9 |
| 470957ee-da20-3bfd-a1bf-ec3acf1ccd8a | -11.84366 | -57.85234 | 2025-11-12 04:33:00 | NOAA-21 | JUARA | MATO GROSSO | Brasil | 5105101 | 51 | 33 | nan | nan | nan | Amazônia | 2.3 |
| 14664e74-2d6b-3fa1-9ab3-d0d22f280e34 | -17.6255 | -46.69921 | 2025-11-12 04:33:00 | NOAA-21 | VAZANTE | MINAS GERAIS | Brasil | 3171006 | 31 | 33 | nan | nan | nan | Cerrado | 1.1 |
| de803ecf-baa9-3794-a3d5-ceb23ccf0e0c | -12.33996 | -43.65516 | 2025-11-12 04:33:00 | NOAA-21 | MUQUÉM DO SÃO FRANCISCO | BAHIA | Brasil | 2922250 | 29 | 33 | nan | nan | nan | Cerrado | 7.7 |
| 60c1e684-7bfa-39e3-aafb-8e3f9d80fbc8 | -14.82171 | -46.11943 | 2025-11-12 04:33:00 | NOAA-21 | SÍTIO D'ABADIA | GOIÁS | Brasil | 5220702 | 52 | 33 | nan | nan | nan | Cerrado | 0.7 |
| 57324e43-02e5-37f4-9f8d-afcaf4629d70 | -16.89314 | -51.65404 | 2025-11-12 04:33:00 | NOAA-21 | PALESTINA DE GOIÁS | GOIÁS | Brasil | 5215652 | 52 | 33 | nan | nan | nan | Cerrado | 1.0 |
| bd6b957d-0dd3-311a-a00d-c05375a6d702 | -12.33945 | -43.65891 | 2025-11-12 04:33:00 | NOAA-21 | MUQUÉM DO SÃO FRANCISCO | BAHIA | Brasil | 2922250 | 29 | 33 | nan | nan | nan | Cerrado | 7.7 |
| 6e76b6ba-40e3-3f2f-816b-374b12892c1e | -13.26424 | -44.24324 | 2025-11-12 04:33:00 | NOAA-21 | SANTA MARIA DA VITÓRIA | BAHIA | Brasil | 2928109 | 29 | 33 | nan | nan | nan | Cerrado | 2.0 |
| 739f2689-84f1-39fd-a1b9-d280615137b9 | -16.31464 | -52.08989 | 2025-11-12 04:33:00 | NOAA-21 | BOM JARDIM DE GOIÁS | GOIÁS | Brasil | 5203401 | 52 | 33 | nan | nan | nan | Cerrado | 1.1 |
| e952b5bb-0b81-3a56-a0f5-7fa595f8a0ab | -10.50763 | -44.93908 | 2025-11-12 04:33:00 | NOAA-21 | CORRENTE | PIAUÍ | Brasil | 2202901 | 22 | 33 | nan | nan | nan | Cerrado | 10.4 |
| 0de9a909-ab9f-3fb2-bd55-885e91645189 | -16.83703 | -46.07843 | 2025-11-12 04:33:00 | NOAA-21 | BRASILÂNDIA DE MINAS | MINAS GERAIS | Brasil | 3108552 | 31 | 33 | nan | nan | nan | Cerrado | 2.3 |
| 17634670-931c-34c3-a71e-179711c5bebc | -16.69725 | -51.83694 | 2025-11-12 04:33:00 | NOAA-21 | CAIAPÔNIA | GOIÁS | Brasil | 5204409 | 52 | 33 | nan | nan | nan | Cerrado | 1.0 |
| 9c559b04-c292-3dc1-924a-e7bdb6204360 | -12.00588 | -46.76843 | 2025-11-12 04:33:00 | NOAA-21 | DIANÓPOLIS | TOCANTINS | Brasil | 1707009 | 17 | 33 | nan | nan | nan | Cerrado | 0.7 |
| 27dac21b-aa5a-35b4-897f-044255e195da | -16.88639 | -51.65289 | 2025-11-12 04:33:00 | NOAA-21 | PALESTINA DE GOIÁS | GOIÁS | Brasil | 5215652 | 52 | 33 | nan | nan | nan | Cerrado | 10.3 |
| 9bdfccd8-5b48-37c6-82cc-03c4dd0a59a3 | -15.59809 | -46.27972 | 2025-11-12 04:33:00 | NOAA-21 | BURITIS | MINAS GERAIS | Brasil | 3109303 | 31 | 33 | nan | nan | nan | Cerrado | 2.9 |
| 8e713b3e-da74-37f8-9b0d-7dee6aa63a16 | -16.36527 | -45.05144 | 2025-11-12 04:33:00 | NOAA-21 | ICARAÍ DE MINAS | MINAS GERAIS | Brasil | 3130051 | 31 | 33 | nan | nan | nan | Cerrado | 0.9 |
| 5d815c5a-dfee-3640-a0f1-7b0e1587be8d | -16.88364 | -51.64855 | 2025-11-12 04:33:00 | NOAA-21 | PALESTINA DE GOIÁS | GOIÁS | Brasil | 5215652 | 52 | 33 | nan | nan | nan | Cerrado | 1.2 |
| 80238242-975e-3283-8124-49dcceba70ca | -17.62917 | -46.69977 | 2025-11-12 04:33:00 | NOAA-21 | VAZANTE | MINAS GERAIS | Brasil | 3171006 | 31 | 33 | nan | nan | nan | Cerrado | 1.1 |
| 8aff6410-b1c1-3810-82b3-b1ac1fac9808 | -13.33027 | -43.17635 | 2025-11-12 04:33:00 | NOAA-21 | BOM JESUS DA LAPA | BAHIA | Brasil | 2903904 | 29 | 33 | nan | nan | nan | Caatinga | 2.6 |
| 03e811df-829f-3a16-8f10-65e755fb87a4 | -17.14998 | -44.66096 | 2025-11-12 04:33:00 | NOAA-21 | LAGOA DOS PATOS | MINAS GERAIS | Brasil | 3137304 | 31 | 33 | nan | nan | nan | Cerrado | 0.6 |
| 61ae151e-9544-382e-a9cf-6fc3cafafe27 | -16.45063 | -45.00696 | 2025-11-12 04:33:00 | NOAA-21 | UBAÍ | MINAS GERAIS | Brasil | 3170008 | 31 | 33 | nan | nan | nan | Cerrado | 1.9 |
| 9f9e474b-548b-3255-a1a0-65ac63d1350b | -17.9648 | -44.93082 | 2025-11-12 04:33:00 | NOAA-21 | LASSANCE | MINAS GERAIS | Brasil | 3138104 | 31 | 33 | nan | nan | nan | Cerrado | 1.1 |
| a5e45097-0721-388e-bb39-bfe61d6a1829 | -16.36597 | -45.04612 | 2025-11-12 04:33:00 | NOAA-21 | ICARAÍ DE MINAS | MINAS GERAIS | Brasil | 3130051 | 31 | 33 | nan | nan | nan | Cerrado | 0.9 |
| 3c99565f-076b-3a7a-903c-78d039c454ed | -10.6562 | -47.92313 | 2025-11-12 04:33:00 | NOAA-21 | MONTE DO CARMO | TOCANTINS | Brasil | 1713601 | 17 | 33 | nan | nan | nan | Cerrado | 0.6 |
| 0daca77e-1d14-3202-9371-b41bc6397d0d | -16.84016 | -46.08373 | 2025-11-12 04:33:00 | NOAA-21 | BRASILÂNDIA DE MINAS | MINAS GERAIS | Brasil | 3108552 | 31 | 33 | nan | nan | nan | Cerrado | 2.3 |
| a02289e9-0210-38a1-a49a-46eb9d5995c0 | -16.88089 | -51.64421 | 2025-11-12 04:33:00 | NOAA-21 | PALESTINA DE GOIÁS | GOIÁS | Brasil | 5215652 | 52 | 33 | nan | nan | nan | Cerrado | 1.2 |
| 1065800e-7aa2-356e-bd14-32de50933b59 | -13.71942 | -44.07407 | 2025-11-12 04:33:00 | NOAA-21 | SÃO FÉLIX DO CORIBE | BAHIA | Brasil | 2929057 | 29 | 33 | nan | nan | nan | Cerrado | 1.4 |


[Clique aqui para ver as próximas entradas](README16.md)
