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

## Dados Diários - Página 19

| ID | Latitude | Longitude | Data/Hora GMT | Satélite | Município | Estado | País | Município ID | Estado ID | País ID | Dias sem Chuva | Precipitação | Risco de Fogo | Bioma | FRP |
|----|----------|-----------|---------------|----------|-----------|--------|------|--------------|-----------|---------|----------------|--------------|----------------|-------|-----|
| 036976d4-1311-368e-a307-ee22cc10c32a | -8.8006 | -45.0128 | 2025-06-25 13:10:00 | GOES-19 | BAIXA GRANDE DO RIBEIRO | PIAUÍ | Brasil | 2201150 | 22 | 33 | nan | nan | nan | Cerrado | 103.6 |
| 4b75ed1c-3258-3445-9b9f-ef8606b1953a | -7.0171 | -44.5725 | 2025-06-25 13:10:00 | GOES-19 | BENEDITO LEITE | MARANHÃO | Brasil | 2101806 | 21 | 33 | nan | nan | nan | Cerrado | 124.5 |
| 31f4f990-96c0-335b-a74c-b90b69ac197d | -10.462 | -47.9428 | 2025-06-25 13:10:00 | GOES-19 | MONTE DO CARMO | TOCANTINS | Brasil | 1713601 | 17 | 33 | nan | nan | nan | Cerrado | 68.8 |
| 6e7aee3a-2918-3805-8604-db53092cdded | -8.0696 | -43.1452 | 2025-06-25 13:10:00 | GOES-19 | CANTO DO BURITI | PIAUÍ | Brasil | 2202307 | 22 | 33 | nan | nan | nan | Caatinga | 77.4 |
| 6e701d51-b761-3e53-8cf0-b145b0b543d1 | -7.0174 | -44.5495 | 2025-06-25 13:10:00 | GOES-19 | BENEDITO LEITE | MARANHÃO | Brasil | 2101806 | 21 | 33 | nan | nan | nan | Cerrado | 88.4 |
| 830c6e7e-d057-3516-b60f-79829da12271 | -7.0359 | -44.5708 | 2025-06-25 13:10:00 | GOES-19 | BENEDITO LEITE | MARANHÃO | Brasil | 2101806 | 21 | 33 | nan | nan | nan | Cerrado | 74.9 |
| 8d541c7a-6f28-3ba2-ba26-32923fb32078 | -7.0174 | -44.5495 | 2025-06-25 13:20:00 | GOES-19 | BENEDITO LEITE | MARANHÃO | Brasil | 2101806 | 21 | 33 | nan | nan | nan | Cerrado | 86.1 |
| b16d020e-9f0e-3f95-bb38-b3ec1b46429e | -7.0171 | -44.5725 | 2025-06-25 13:20:00 | GOES-19 | BENEDITO LEITE | MARANHÃO | Brasil | 2101806 | 21 | 33 | nan | nan | nan | Cerrado | 116.5 |
| f9d6a566-cd07-3683-81d3-1311d45297ce | -8.0696 | -43.1452 | 2025-06-25 13:20:00 | GOES-19 | CANTO DO BURITI | PIAUÍ | Brasil | 2202307 | 22 | 33 | nan | nan | nan | Caatinga | 90.5 |
| c8d5b8fb-b48e-3158-a7d9-7522132399d3 | -12.6439 | -45.3038 | 2025-06-25 13:20:00 | GOES-19 | SÃO DESIDÉRIO | BAHIA | Brasil | 2928901 | 29 | 33 | nan | nan | nan | Cerrado | 79.9 |
| 4bfeaa64-efe6-3c6d-a78e-a0069e94b1a3 | -8.8006 | -45.0128 | 2025-06-25 13:20:00 | GOES-19 | BAIXA GRANDE DO RIBEIRO | PIAUÍ | Brasil | 2201150 | 22 | 33 | nan | nan | nan | Cerrado | 115.4 |
| b0bcd8e7-1594-3f06-8f0b-7c82fb71c260 | -10.443 | -47.945 | 2025-06-25 13:20:00 | GOES-19 | MONTE DO CARMO | TOCANTINS | Brasil | 1713601 | 17 | 33 | nan | nan | nan | Cerrado | 77.9 |
| 60ca31f9-52a1-3d94-8219-ee7b90014672 | -8.0696 | -43.1452 | 2025-06-25 13:30:00 | GOES-19 | CANTO DO BURITI | PIAUÍ | Brasil | 2202307 | 22 | 33 | nan | nan | nan | Caatinga | 84.9 |
| 867c7967-e0d4-3ddf-9d61-79acf96646bc | -10.443 | -47.945 | 2025-06-25 13:30:00 | GOES-19 | MONTE DO CARMO | TOCANTINS | Brasil | 1713601 | 17 | 33 | nan | nan | nan | Cerrado | 89.6 |
| 6905f12e-a675-3b5d-b901-01e2b41d6ed2 | -11.0896 | -46.6422 | 2025-06-25 13:30:00 | GOES-19 | MATEIROS | TOCANTINS | Brasil | 1712702 | 17 | 33 | nan | nan | nan | Cerrado | 80.7 |
| 793ecbc2-c7fd-37fe-b026-d8effbe8b705 | -8.8006 | -45.0128 | 2025-06-25 13:30:00 | GOES-19 | BAIXA GRANDE DO RIBEIRO | PIAUÍ | Brasil | 2201150 | 22 | 33 | nan | nan | nan | Cerrado | 129.3 |
| f1ec98a4-1f72-34f5-94d5-39b0930717a7 | -7.0171 | -44.5725 | 2025-06-25 13:30:00 | GOES-19 | BENEDITO LEITE | MARANHÃO | Brasil | 2101806 | 21 | 33 | nan | nan | nan | Cerrado | 97.0 |
| 2a0c817f-952e-3302-a103-bfaed2dc7437 | -12.6439 | -45.3038 | 2025-06-25 13:30:00 | GOES-19 | SÃO DESIDÉRIO | BAHIA | Brasil | 2928901 | 29 | 33 | nan | nan | nan | Cerrado | 75.3 |
| 495b0c42-67b3-3883-9749-9afbcd096ad2 | -8.8006 | -45.0128 | 2025-06-25 13:40:00 | GOES-19 | BAIXA GRANDE DO RIBEIRO | PIAUÍ | Brasil | 2201150 | 22 | 33 | nan | nan | nan | Cerrado | 125.4 |
| f5c7e94a-1fe0-33df-825c-2d41b4bd9954 | -11.0896 | -46.6422 | 2025-06-25 13:40:00 | GOES-19 | MATEIROS | TOCANTINS | Brasil | 1712702 | 17 | 33 | nan | nan | nan | Cerrado | 110.1 |
| 7a00e059-21ae-3a62-a038-abe56d8dad7f | -12.6439 | -45.3038 | 2025-06-25 13:40:00 | GOES-19 | SÃO DESIDÉRIO | BAHIA | Brasil | 2928901 | 29 | 33 | nan | nan | nan | Cerrado | 84.5 |
| 84359957-28d1-390e-9e0e-284ea8a9672a | -7.0174 | -44.5495 | 2025-06-25 13:40:00 | GOES-19 | BENEDITO LEITE | MARANHÃO | Brasil | 2101806 | 21 | 33 | nan | nan | nan | Cerrado | 74.9 |
| 79fd73f6-d2a8-3cfe-9da4-d186479cd84f | -11.8879 | -45.7165 | 2025-06-25 13:40:00 | GOES-19 | BARREIRAS | BAHIA | Brasil | 2903201 | 29 | 33 | nan | nan | nan | Cerrado | 143.5 |
| bed45900-328c-310a-9c74-fd5c4633afcc | -7.0171 | -44.5725 | 2025-06-25 13:40:00 | GOES-19 | BENEDITO LEITE | MARANHÃO | Brasil | 2101806 | 21 | 33 | nan | nan | nan | Cerrado | 103.4 |
| 76802228-45f9-3903-bbe8-af59f653c1d3 | -8.0696 | -43.1452 | 2025-06-25 13:40:00 | GOES-19 | CANTO DO BURITI | PIAUÍ | Brasil | 2202307 | 22 | 33 | nan | nan | nan | Caatinga | 84.7 |
| b1acff31-9b0a-3d68-b8c4-acbb72e1ec11 | -7.3334 | -43.1981 | 2025-06-25 13:40:00 | GOES-19 | ITAUEIRA | PIAUÍ | Brasil | 2205102 | 22 | 33 | nan | nan | nan | Caatinga | 100.3 |
| df34c75c-968b-36c1-a1a9-5850b1adc2fe | -10.443 | -47.945 | 2025-06-25 13:40:00 | GOES-19 | MONTE DO CARMO | TOCANTINS | Brasil | 1713601 | 17 | 33 | nan | nan | nan | Cerrado | 79.2 |
| d1b1c75d-7c98-31be-9bcd-9f95c291d08c | -8.8009 | -44.9899 | 2025-06-25 13:40:00 | GOES-19 | BAIXA GRANDE DO RIBEIRO | PIAUÍ | Brasil | 2201150 | 22 | 33 | nan | nan | nan | Cerrado | 90.4 |
| 784a5aca-e599-3277-9160-e9b9f9e7c294 | -7.0174 | -44.5495 | 2025-06-25 13:50:00 | GOES-19 | BENEDITO LEITE | MARANHÃO | Brasil | 2101806 | 21 | 33 | nan | nan | nan | Cerrado | 70.6 |
| 758e0d7a-0a6e-359d-bc0c-5502a6c02a6f | -8.0696 | -43.1452 | 2025-06-25 13:50:00 | GOES-19 | CANTO DO BURITI | PIAUÍ | Brasil | 2202307 | 22 | 33 | nan | nan | nan | Caatinga | 78.9 |
| 8302b670-89fe-348c-ba1e-c2c0aa028af2 | -12.6439 | -45.3038 | 2025-06-25 13:50:00 | GOES-19 | SÃO DESIDÉRIO | BAHIA | Brasil | 2928901 | 29 | 33 | nan | nan | nan | Cerrado | 90.3 |
| 2819bdf6-27cd-3e3d-a211-2ec7a53f68ea | -7.0171 | -44.5725 | 2025-06-25 13:50:00 | GOES-19 | BENEDITO LEITE | MARANHÃO | Brasil | 2101806 | 21 | 33 | nan | nan | nan | Cerrado | 106.5 |
| b9f1a1e8-b8fa-33b5-abc4-cfffd5a7ccca | -11.8879 | -45.7165 | 2025-06-25 13:50:00 | GOES-19 | BARREIRAS | BAHIA | Brasil | 2903201 | 29 | 33 | nan | nan | nan | Cerrado | 66.7 |
| 5965842a-a116-3cfe-9cb3-1165e91aec13 | -7.0946 | -44.3589 | 2025-06-25 13:50:00 | GOES-19 | BENEDITO LEITE | MARANHÃO | Brasil | 2101806 | 21 | 33 | nan | nan | nan | Cerrado | 92.4 |
| 4385d3fc-1680-3b1b-b0a0-12034d5ae425 | -11.5723 | -47.4298 | 2025-06-25 13:50:00 | GOES-19 | NATIVIDADE | TOCANTINS | Brasil | 1714203 | 17 | 33 | nan | nan | nan | Cerrado | 69.0 |
| 7cde9bee-3139-3918-abcd-e3796cafcdbc | -8.8006 | -45.0128 | 2025-06-25 13:50:00 | GOES-19 | BAIXA GRANDE DO RIBEIRO | PIAUÍ | Brasil | 2201150 | 22 | 33 | nan | nan | nan | Cerrado | 146.5 |
| 092cdc12-e22d-339a-b30a-f038264f5579 | -10.443 | -47.945 | 2025-06-25 13:50:00 | GOES-19 | MONTE DO CARMO | TOCANTINS | Brasil | 1713601 | 17 | 33 | nan | nan | nan | Cerrado | 86.4 |
| 20f415f3-0412-34c7-a3db-7ce633f717dd | -11.5723 | -47.4298 | 2025-06-25 14:00:00 | GOES-19 | NATIVIDADE | TOCANTINS | Brasil | 1714203 | 17 | 33 | nan | nan | nan | Cerrado | 73.7 |
| 35cf5823-b589-3122-ac27-f03be1561835 | -7.0946 | -44.3589 | 2025-06-25 14:00:00 | GOES-19 | BENEDITO LEITE | MARANHÃO | Brasil | 2101806 | 21 | 33 | nan | nan | nan | Cerrado | 77.1 |
| a64cda1b-cfb6-3ed8-9460-57baaf16a07d | -7.0174 | -44.5495 | 2025-06-25 14:00:00 | GOES-19 | BENEDITO LEITE | MARANHÃO | Brasil | 2101806 | 21 | 33 | nan | nan | nan | Cerrado | 68.7 |
| 6e240b2c-4b69-3dc4-8352-fefb4bc44aeb | -9.518 | -56.0975 | 2025-06-25 14:00:00 | GOES-19 | ALTA FLORESTA | MATO GROSSO | Brasil | 5100250 | 51 | 33 | nan | nan | nan | Amazônia | 79.2 |
| af033a70-d008-336b-81eb-436bbf717488 | -11.961 | -47.0199 | 2025-06-25 14:00:00 | GOES-19 | TAIPAS DO TOCANTINS | TOCANTINS | Brasil | 1720937 | 17 | 33 | nan | nan | nan | Cerrado | 79.6 |
| 55d667e2-5f77-312d-9a74-373a7f084e8b | -8.8009 | -44.9899 | 2025-06-25 14:00:00 | GOES-19 | BAIXA GRANDE DO RIBEIRO | PIAUÍ | Brasil | 2201150 | 22 | 33 | nan | nan | nan | Cerrado | 95.0 |
| b6383817-f289-3b0c-9fa8-9ee6953cc8ab | -10.443 | -47.945 | 2025-06-25 14:00:00 | GOES-19 | MONTE DO CARMO | TOCANTINS | Brasil | 1713601 | 17 | 33 | nan | nan | nan | Cerrado | 70.4 |
| cc368251-63af-32b0-85da-3d4fcd901fc9 | -8.8006 | -45.0128 | 2025-06-25 14:00:00 | GOES-19 | BAIXA GRANDE DO RIBEIRO | PIAUÍ | Brasil | 2201150 | 22 | 33 | nan | nan | nan | Cerrado | 156.2 |
| 13698b2f-d3b8-3d82-8134-adc4be91713a | -12.6439 | -45.3038 | 2025-06-25 14:00:00 | GOES-19 | SÃO DESIDÉRIO | BAHIA | Brasil | 2928901 | 29 | 33 | nan | nan | nan | Cerrado | 77.4 |
| 5a753735-be75-3f1c-b73a-fa3698fdce10 | -7.0171 | -44.5725 | 2025-06-25 14:00:00 | GOES-19 | BENEDITO LEITE | MARANHÃO | Brasil | 2101806 | 21 | 33 | nan | nan | nan | Cerrado | 104.7 |
| 4aba3ee9-e82d-31c4-8ecf-d99f2c2ec44f | -11.0896 | -46.6422 | 2025-06-25 14:00:00 | GOES-19 | MATEIROS | TOCANTINS | Brasil | 1712702 | 17 | 33 | nan | nan | nan | Cerrado | 119.3 |
| b1f2d950-5f1d-3d0f-b637-fa0098bdcd86 | -10.462 | -47.9428 | 2025-06-25 14:00:00 | GOES-19 | MONTE DO CARMO | TOCANTINS | Brasil | 1713601 | 17 | 33 | nan | nan | nan | Cerrado | 83.8 |
| fa567dbc-e2dd-353e-a7d0-4f37ba3b5408 | -7.0171 | -44.5725 | 2025-06-25 14:10:00 | GOES-19 | BENEDITO LEITE | MARANHÃO | Brasil | 2101806 | 21 | 33 | nan | nan | nan | Cerrado | 82.2 |
| 48a21c85-e38f-3a14-81a5-7a968c1d9ff8 | -7.3334 | -43.1981 | 2025-06-25 14:10:00 | GOES-19 | ITAUEIRA | PIAUÍ | Brasil | 2205102 | 22 | 33 | nan | nan | nan | Caatinga | 70.5 |
| 9366e298-fe0d-3caa-899d-9c2f5316682d | -8.8006 | -45.0128 | 2025-06-25 14:10:00 | GOES-19 | BAIXA GRANDE DO RIBEIRO | PIAUÍ | Brasil | 2201150 | 22 | 33 | nan | nan | nan | Cerrado | 146.6 |
| 54b779f3-a6bd-3acb-90eb-af90ab667d3b | -7.0943 | -44.3819 | 2025-06-25 14:10:00 | GOES-19 | BENEDITO LEITE | MARANHÃO | Brasil | 2101806 | 21 | 33 | nan | nan | nan | Cerrado | 69.5 |
| 4ebbcb85-f1d1-32e5-8278-b524f7506233 | -10.443 | -47.945 | 2025-06-25 14:10:00 | GOES-19 | MONTE DO CARMO | TOCANTINS | Brasil | 1713601 | 17 | 33 | nan | nan | nan | Cerrado | 99.5 |
| 45e907a8-2679-3c4f-bb16-e315521c2e5b | -7.0946 | -44.3589 | 2025-06-25 14:10:00 | GOES-19 | BENEDITO LEITE | MARANHÃO | Brasil | 2101806 | 21 | 33 | nan | nan | nan | Cerrado | 87.6 |
| 1146c293-0488-3ca9-beb7-a3f43d5c7c5b | -8.0696 | -43.1452 | 2025-06-25 14:10:00 | GOES-19 | CANTO DO BURITI | PIAUÍ | Brasil | 2202307 | 22 | 33 | nan | nan | nan | Caatinga | 80.0 |
| 9da4bafc-437a-34ea-ab6d-cc65ea72b07b | -10.4427 | -47.967 | 2025-06-25 14:10:00 | GOES-19 | MONTE DO CARMO | TOCANTINS | Brasil | 1713601 | 17 | 33 | nan | nan | nan | Cerrado | 67.8 |
| 271b98ac-0cb4-353a-aefa-69f5cd31278a | -11.8879 | -45.7165 | 2025-06-25 14:10:00 | GOES-19 | BARREIRAS | BAHIA | Brasil | 2903201 | 29 | 33 | nan | nan | nan | Cerrado | 67.6 |
| 15b18433-35ca-3788-b997-cbade8c460bb | -11.961 | -47.0199 | 2025-06-25 14:10:00 | GOES-19 | TAIPAS DO TOCANTINS | TOCANTINS | Brasil | 1720937 | 17 | 33 | nan | nan | nan | Cerrado | 73.0 |
| 0e1cee40-3da0-3c9b-ab98-9ceb48645821 | -12.6439 | -45.3038 | 2025-06-25 14:10:00 | GOES-19 | SÃO DESIDÉRIO | BAHIA | Brasil | 2928901 | 29 | 33 | nan | nan | nan | Cerrado | 114.1 |
| 0377dfbb-5649-3896-954c-215ee6fd3c77 | -8.8009 | -44.9899 | 2025-06-25 14:10:00 | GOES-19 | BAIXA GRANDE DO RIBEIRO | PIAUÍ | Brasil | 2201150 | 22 | 33 | nan | nan | nan | Cerrado | 106.7 |
| c9369d08-15d5-3a44-bb8f-66fbc3e9c685 | -8.0696 | -43.1452 | 2025-06-25 14:20:00 | GOES-19 | CANTO DO BURITI | PIAUÍ | Brasil | 2202307 | 22 | 33 | nan | nan | nan | Caatinga | 74.5 |
| e021f856-711a-365d-99fd-2fe79515be8c | -7.0171 | -44.5725 | 2025-06-25 14:20:00 | GOES-19 | BENEDITO LEITE | MARANHÃO | Brasil | 2101806 | 21 | 33 | nan | nan | nan | Cerrado | 84.1 |
| 4a16cca9-0491-3f5a-9403-624d9cb5ac6b | -7.0946 | -44.3589 | 2025-06-25 14:20:00 | GOES-19 | BENEDITO LEITE | MARANHÃO | Brasil | 2101806 | 21 | 33 | nan | nan | nan | Cerrado | 78.4 |
| 61ccf404-a6c9-34c9-a741-080c48301c29 | -8.8009 | -44.9899 | 2025-06-25 14:20:00 | GOES-19 | BAIXA GRANDE DO RIBEIRO | PIAUÍ | Brasil | 2201150 | 22 | 33 | nan | nan | nan | Cerrado | 106.6 |
| e7135302-e18e-3721-a557-2e58c6c734f0 | -11.961 | -47.0199 | 2025-06-25 14:20:00 | GOES-19 | TAIPAS DO TOCANTINS | TOCANTINS | Brasil | 1720937 | 17 | 33 | nan | nan | nan | Cerrado | 64.6 |
| 98a16d05-caab-318d-b7c4-9525bab79509 | -11.5723 | -47.4298 | 2025-06-25 14:20:00 | GOES-19 | NATIVIDADE | TOCANTINS | Brasil | 1714203 | 17 | 33 | nan | nan | nan | Cerrado | 72.8 |
| 83c494cd-efa2-3fd0-8561-8221d3136fe2 | -7.3679 | -43.4756 | 2025-06-25 14:20:00 | GOES-19 | CANAVIEIRA | PIAUÍ | Brasil | 2202251 | 22 | 33 | nan | nan | nan | Cerrado | 80.0 |
| 7891ea72-f469-3366-92e6-bba1eac07de2 | -10.443 | -47.945 | 2025-06-25 14:20:00 | GOES-19 | MONTE DO CARMO | TOCANTINS | Brasil | 1713601 | 17 | 33 | nan | nan | nan | Cerrado | 106.4 |
| b3e9d544-a480-3685-a931-c0f61f41819d | -12.6439 | -45.3038 | 2025-06-25 14:20:00 | GOES-19 | SÃO DESIDÉRIO | BAHIA | Brasil | 2928901 | 29 | 33 | nan | nan | nan | Cerrado | 97.6 |
| 3db65734-33a5-36c1-acd3-4546b0629f66 | -8.8006 | -45.0128 | 2025-06-25 14:20:00 | GOES-19 | BAIXA GRANDE DO RIBEIRO | PIAUÍ | Brasil | 2201150 | 22 | 33 | nan | nan | nan | Cerrado | 151.2 |
| c02955e8-f968-3444-8980-01d036663cd4 | -7.0174 | -44.5495 | 2025-06-25 14:20:00 | GOES-19 | BENEDITO LEITE | MARANHÃO | Brasil | 2101806 | 21 | 33 | nan | nan | nan | Cerrado | 70.6 |
| 7934ac09-d00e-33cf-8184-af26fc720d15 | -7.3679 | -43.4756 | 2025-06-25 14:30:00 | GOES-19 | CANAVIEIRA | PIAUÍ | Brasil | 2202251 | 22 | 33 | nan | nan | nan | Cerrado | 71.7 |
| 72bbbdbe-3136-3c8b-8572-ca61d2cfda4d | -7.0171 | -44.5725 | 2025-06-25 14:30:00 | GOES-19 | BENEDITO LEITE | MARANHÃO | Brasil | 2101806 | 21 | 33 | nan | nan | nan | Cerrado | 75.3 |
| fa23279f-86cd-3e4c-b908-025d43d642ae | -15.6562 | -41.2442 | 2025-06-25 14:30:00 | GOES-19 | ENCRUZILHADA | BAHIA | Brasil | 2910404 | 29 | 33 | nan | nan | nan | Mata Atlântica | 114.6 |
| 0c277e5d-1b32-3525-9a8a-4bd44aa0c92d | -10.443 | -47.945 | 2025-06-25 14:30:00 | GOES-19 | MONTE DO CARMO | TOCANTINS | Brasil | 1713601 | 17 | 33 | nan | nan | nan | Cerrado | 110.3 |
| decfd82b-0429-32ca-ab5b-a256d32ebafb | -7.0946 | -44.3589 | 2025-06-25 14:30:00 | GOES-19 | BENEDITO LEITE | MARANHÃO | Brasil | 2101806 | 21 | 33 | nan | nan | nan | Cerrado | 87.3 |
| 4c4a0ed1-cdce-3beb-aa9b-01f5e45ba107 | -11.8879 | -45.7165 | 2025-06-25 14:30:00 | GOES-19 | BARREIRAS | BAHIA | Brasil | 2903201 | 29 | 33 | nan | nan | nan | Cerrado | 64.9 |
| c8ac2c13-e14d-36bf-8810-c106aaf311b1 | -7.0174 | -44.5495 | 2025-06-25 14:30:00 | GOES-19 | BENEDITO LEITE | MARANHÃO | Brasil | 2101806 | 21 | 33 | nan | nan | nan | Cerrado | 66.5 |
| c3944647-d2f5-3ddf-b900-200bb688cddd | -9.518 | -56.0975 | 2025-06-25 14:30:00 | GOES-19 | ALTA FLORESTA | MATO GROSSO | Brasil | 5100250 | 51 | 33 | nan | nan | nan | Amazônia | 74.1 |
| 936e800b-5b4e-39ad-83dd-12d7d3e268e4 | -8.8006 | -45.0128 | 2025-06-25 14:30:00 | GOES-19 | BAIXA GRANDE DO RIBEIRO | PIAUÍ | Brasil | 2201150 | 22 | 33 | nan | nan | nan | Cerrado | 130.1 |
| ec0d482a-1775-3484-835c-a82fc7df221a | -8.0696 | -43.1452 | 2025-06-25 14:30:00 | GOES-19 | CANTO DO BURITI | PIAUÍ | Brasil | 2202307 | 22 | 33 | nan | nan | nan | Caatinga | 67.0 |
| 24881a8f-0d29-3f78-a97e-1caafaf5f8b9 | -12.6439 | -45.3038 | 2025-06-25 14:30:00 | GOES-19 | SÃO DESIDÉRIO | BAHIA | Brasil | 2928901 | 29 | 33 | nan | nan | nan | Cerrado | 85.0 |
| ac067e34-b6b9-3f37-833e-052337611205 | -11.961 | -47.0199 | 2025-06-25 14:30:00 | GOES-19 | TAIPAS DO TOCANTINS | TOCANTINS | Brasil | 1720937 | 17 | 33 | nan | nan | nan | Cerrado | 79.8 |
| 6f5b1fbc-48ae-376a-aa3d-22aae98ce62f | -11.5723 | -47.4298 | 2025-06-25 14:40:00 | GOES-19 | NATIVIDADE | TOCANTINS | Brasil | 1714203 | 17 | 33 | nan | nan | nan | Cerrado | 72.7 |
| 324f551b-a01c-34dc-83ab-dd5dac66c348 | -6.2224 | -43.3693 | 2025-06-25 14:40:00 | GOES-19 | LAGOA DO MATO | MARANHÃO | Brasil | 2105922 | 21 | 33 | nan | nan | nan | Cerrado | 111.2 |
| 22598da7-dc79-3f02-88ac-a132b6d91f2e | -7.0174 | -44.5495 | 2025-06-25 14:40:00 | GOES-19 | BENEDITO LEITE | MARANHÃO | Brasil | 2101806 | 21 | 33 | nan | nan | nan | Cerrado | 63.4 |
| bfd695d7-6173-30e0-b9e7-b6056c1165b5 | -8.8006 | -45.0128 | 2025-06-25 14:40:00 | GOES-19 | BAIXA GRANDE DO RIBEIRO | PIAUÍ | Brasil | 2201150 | 22 | 33 | nan | nan | nan | Cerrado | 108.1 |
| 25fc3765-136e-3dd2-94bb-3c6808447a6f | -12.6439 | -45.3038 | 2025-06-25 14:40:00 | GOES-19 | SÃO DESIDÉRIO | BAHIA | Brasil | 2928901 | 29 | 33 | nan | nan | nan | Cerrado | 111.2 |
| 96aaa6d7-6f1e-3111-8a0a-7742c1739c79 | -10.4427 | -47.967 | 2025-06-25 14:40:00 | GOES-19 | MONTE DO CARMO | TOCANTINS | Brasil | 1713601 | 17 | 33 | nan | nan | nan | Cerrado | 64.2 |
| 95c60aa0-4412-35a9-87f9-11fcfd8c9f0a | -11.961 | -47.0199 | 2025-06-25 14:40:00 | GOES-19 | TAIPAS DO TOCANTINS | TOCANTINS | Brasil | 1720937 | 17 | 33 | nan | nan | nan | Cerrado | 69.2 |
| 93bfdc2c-0ddd-3ea2-b7ad-2eb300cec59f | -10.443 | -47.945 | 2025-06-25 14:40:00 | GOES-19 | MONTE DO CARMO | TOCANTINS | Brasil | 1713601 | 17 | 33 | nan | nan | nan | Cerrado | 91.4 |
| 3523ce1b-9af5-3d40-9aec-9bf94b28d653 | -7.0171 | -44.5725 | 2025-06-25 14:40:00 | GOES-19 | BENEDITO LEITE | MARANHÃO | Brasil | 2101806 | 21 | 33 | nan | nan | nan | Cerrado | 89.3 |
| 225220d2-c318-3a65-b0c0-1b50e12c37ec | -11.9418 | -47.0225 | 2025-06-25 14:40:00 | GOES-19 | DIANÓPOLIS | TOCANTINS | Brasil | 1707009 | 17 | 33 | nan | nan | nan | Cerrado | 55.9 |


