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

## Dados Diários - Página 18

| ID | Latitude | Longitude | Data/Hora GMT | Satélite | Município | Estado | País | Município ID | Estado ID | País ID | Dias sem Chuva | Precipitação | Risco de Fogo | Bioma | FRP |
|----|----------|-----------|---------------|----------|-----------|--------|------|--------------|-----------|---------|----------------|--------------|----------------|-------|-----|
| 84be540b-b8dd-3bca-bca9-ccd64978ac86 | -4.5562 | -43.3028 | 2024-12-01 02:00:00 | GOES-16 | ALDEIAS ALTAS | MARANHÃO | Brasil | 2100303 | 21 | 33 | nan | nan | nan | Cerrado | 164.1 |
| 1fb975a0-9157-3572-95f2-550711ae4e71 | -3.4569 | -50.2782 | 2024-12-01 02:00:00 | GOES-16 | PACAJÁ | PARÁ | Brasil | 1505486 | 15 | 33 | nan | nan | nan | Amazônia | 60.0 |
| d0bbf23e-df42-3dc1-8968-80a75489c6df | -3.2774 | -53.6383 | 2024-12-01 02:00:00 | GOES-16 | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | 68.8 |
| 7a003842-1ae6-380c-94c5-08608e69cea8 | -3.2591 | -53.6186 | 2024-12-01 02:00:00 | GOES-16 | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | 91.4 |
| 4227c6f4-e317-3b6e-857c-2722c81871af | -3.0081 | -51.7897 | 2024-12-01 02:00:00 | GOES-16 | SENADOR JOSÉ PORFÍRIO | PARÁ | Brasil | 1507805 | 15 | 33 | nan | nan | nan | Amazônia | 64.7 |
| f2702833-b709-30aa-9fe9-1a9f3ed9e2cf | -2.8012 | -53.0633 | 2024-12-01 02:00:00 | GOES-16 | MEDICILÂNDIA | PARÁ | Brasil | 1504455 | 15 | 33 | nan | nan | nan | Amazônia | 56.3 |
| 7dae28d5-7997-3e3b-b730-299835bc8518 | -4.5578 | -45.7232 | 2024-12-01 02:00:00 | GOES-16 | SANTA LUZIA | MARANHÃO | Brasil | 2110005 | 21 | 33 | nan | nan | nan | Amazônia | 129.8 |
| b6db1d76-fdc5-3f75-ad80-4bec2b9e0ebb | -4.5563 | -43.2795 | 2024-12-01 02:10:00 | GOES-16 | ALDEIAS ALTAS | MARANHÃO | Brasil | 2100303 | 21 | 33 | nan | nan | nan | Cerrado | 66.9 |
| c727f4ae-042f-325f-85f5-97e5b104f192 | -3.259 | -53.6388 | 2024-12-01 02:10:00 | GOES-16 | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | 128.2 |
| dfc223bf-bdae-38b1-8c64-36c9838ef849 | -6.9156 | -43.5418 | 2024-12-01 02:10:00 | GOES-16 | JERUMENHA | PIAUÍ | Brasil | 2205300 | 22 | 33 | nan | nan | nan | Cerrado | 137.9 |
| c0814db1-4208-3ddf-8aa7-12faa79897ab | 1.1439 | -55.9871 | 2024-12-01 02:10:00 | GOES-16 | ORIXIMINÁ | PARÁ | Brasil | 1505304 | 15 | 33 | nan | nan | nan | Amazônia | 62.8 |
| 3b294744-fb67-395f-80f4-3c9254e3b68d | -4.5562 | -43.3028 | 2024-12-01 02:10:00 | GOES-16 | ALDEIAS ALTAS | MARANHÃO | Brasil | 2100303 | 21 | 33 | nan | nan | nan | Cerrado | 176.5 |
| d4041d47-e764-31ea-94c9-1f8341ec9bee | -3.4754 | -50.2776 | 2024-12-01 02:10:00 | GOES-16 | PACAJÁ | PARÁ | Brasil | 1505486 | 15 | 33 | nan | nan | nan | Amazônia | 61.0 |
| 7baa5c64-3cbd-3845-9fab-3e7958d568cb | -4.558 | -45.7008 | 2024-12-01 02:10:00 | GOES-16 | PAULO RAMOS | MARANHÃO | Brasil | 2108108 | 21 | 33 | nan | nan | nan | Amazônia | 63.9 |
| 7c71ba3e-3f53-3925-a525-a232a3aa942c | -3.3134 | -53.8592 | 2024-12-01 02:10:00 | GOES-16 | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | 62.7 |
| f29d49b7-ec7c-3f6e-b672-e685018eb2e0 | -1.7139 | -46.1422 | 2024-12-01 02:10:00 | GOES-16 | BOA VISTA DO GURUPI | MARANHÃO | Brasil | 2101970 | 21 | 33 | nan | nan | nan | Amazônia | 81.5 |
| 84a10b08-b69a-3786-b36a-c7c17e49027d | -4.5394 | -45.7019 | 2024-12-01 02:10:00 | GOES-16 | PAULO RAMOS | MARANHÃO | Brasil | 2108108 | 21 | 33 | nan | nan | nan | Amazônia | 75.6 |
| 7d62f89c-845c-3866-80fa-dac9bcdb19ad | 1.1438 | -56.0067 | 2024-12-01 02:10:00 | GOES-16 | ORIXIMINÁ | PARÁ | Brasil | 1505304 | 15 | 33 | nan | nan | nan | Amazônia | 63.6 |
| d72642b6-331f-3b6c-9b3f-787208d9511c | -3.5158 | -53.8333 | 2024-12-01 02:10:00 | GOES-16 | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | 65.3 |
| 69ea7b88-455c-3bc5-8c20-fd0f1869c21f | -3.4755 | -50.2566 | 2024-12-01 02:10:00 | GOES-16 | PACAJÁ | PARÁ | Brasil | 1505486 | 15 | 33 | nan | nan | nan | Amazônia | 60.5 |
| 32294336-fc32-3e33-9f00-61cff0864c27 | -2.6578 | -51.8811 | 2024-12-01 02:10:00 | GOES-16 | SENADOR JOSÉ PORFÍRIO | PARÁ | Brasil | 1507805 | 15 | 33 | nan | nan | nan | Amazônia | 80.7 |
| 7b8f3e7d-08b8-39dd-9353-7b5095dbab6d | -2.8012 | -53.0633 | 2024-12-01 02:10:00 | GOES-16 | MEDICILÂNDIA | PARÁ | Brasil | 1504455 | 15 | 33 | nan | nan | nan | Amazônia | 57.0 |
| de1d70d1-6865-3b8c-b42a-34b58cdaecae | -2.7503 | -51.7553 | 2024-12-01 02:10:00 | GOES-16 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 83.6 |
| b7f76428-a1b4-3113-a0ce-b7ef5fe5cb54 | 1.1622 | -55.9672 | 2024-12-01 02:10:00 | GOES-16 | ORIXIMINÁ | PARÁ | Brasil | 1505304 | 15 | 33 | nan | nan | nan | Amazônia | 55.6 |
| 4649ae5a-f586-331c-b7a3-197c9ce3a53e | -4.5578 | -45.7232 | 2024-12-01 02:10:00 | GOES-16 | SANTA LUZIA | MARANHÃO | Brasil | 2110005 | 21 | 33 | nan | nan | nan | Amazônia | 115.8 |
| 8602e5c2-b20a-3b45-97d5-e7fecd888444 | -3.4974 | -53.8339 | 2024-12-01 02:10:00 | GOES-16 | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | 108.1 |
| a4bbc7ca-5ec8-31a9-9fea-e125c61a0a1f | -2.6579 | -51.8606 | 2024-12-01 02:10:00 | GOES-16 | SENADOR JOSÉ PORFÍRIO | PARÁ | Brasil | 1507805 | 15 | 33 | nan | nan | nan | Amazônia | 59.0 |
| da5b5c57-8e79-3ce5-9cb1-537b1f1e79c6 | -2.8013 | -53.043 | 2024-12-01 02:10:00 | GOES-16 | MEDICILÂNDIA | PARÁ | Brasil | 1504455 | 15 | 33 | nan | nan | nan | Amazônia | 65.3 |
| 47b4d2af-db97-36cf-a70d-6f5de778f4b2 | -3.2591 | -53.6186 | 2024-12-01 02:10:00 | GOES-16 | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | 85.9 |
| 8b9379b9-8cc9-3723-9cd4-9dd99e147e4d | -4.5375 | -43.304 | 2024-12-01 02:10:00 | GOES-16 | ALDEIAS ALTAS | MARANHÃO | Brasil | 2100303 | 21 | 33 | nan | nan | nan | Cerrado | 61.5 |
| 8c30659a-8587-34f1-a0e9-9f56ac93a307 | -9.7592 | -36.1822 | 2024-12-01 02:10:00 | GOES-16 | SÃO MIGUEL DOS CAMPOS | ALAGOAS | Brasil | 2708600 | 27 | 33 | nan | nan | nan | Mata Atlântica | 93.8 |
| 6f06a0ce-8e18-35fa-9228-8a7ba41f85e8 | 1.1622 | -55.9869 | 2024-12-01 02:10:00 | GOES-16 | ORIXIMINÁ | PARÁ | Brasil | 1505304 | 15 | 33 | nan | nan | nan | Amazônia | 63.8 |
| 537801ae-f42a-3921-bde8-deee5efef8b6 | -3.1273 | -54.5264 | 2024-12-01 02:10:00 | GOES-16 | MOJUÍ DOS CAMPOS | PARÁ | Brasil | 1504752 | 15 | 33 | nan | nan | nan | Amazônia | 90.2 |
| 8f63d001-2dd3-3d14-a5af-8923734193bb | -6.9344 | -43.5401 | 2024-12-01 02:10:00 | GOES-16 | JERUMENHA | PIAUÍ | Brasil | 2205300 | 22 | 33 | nan | nan | nan | Cerrado | 128.6 |
| 46c66a88-c013-3a70-919c-0c00cd65693d | -2.8197 | -53.0425 | 2024-12-01 02:20:00 | GOES-16 | MEDICILÂNDIA | PARÁ | Brasil | 1504455 | 15 | 33 | nan | nan | nan | Amazônia | 60.8 |
| fdf64388-1fa5-3923-b3b6-50aa4a402b5b | -4.5578 | -45.7232 | 2024-12-01 02:20:00 | GOES-16 | SANTA LUZIA | MARANHÃO | Brasil | 2110005 | 21 | 33 | nan | nan | nan | Amazônia | 109.9 |
| a00a24f9-ad5b-3a52-a053-7190a6179022 | -6.9344 | -43.5401 | 2024-12-01 02:20:00 | GOES-16 | JERUMENHA | PIAUÍ | Brasil | 2205300 | 22 | 33 | nan | nan | nan | Cerrado | 130.7 |
| 29bf857d-9fe6-35df-8cc5-54bf599b46e6 | -4.5562 | -43.3028 | 2024-12-01 02:20:00 | GOES-16 | ALDEIAS ALTAS | MARANHÃO | Brasil | 2100303 | 21 | 33 | nan | nan | nan | Cerrado | 193.6 |
| a8b7de08-da8a-3c54-a14e-a98d3e293d73 | -3.4755 | -50.2566 | 2024-12-01 02:20:00 | GOES-16 | PACAJÁ | PARÁ | Brasil | 1505486 | 15 | 33 | nan | nan | nan | Amazônia | 64.1 |
| 2607fead-ffa3-30ad-9806-49d8a7f79eaa | -2.9778 | -45.5713 | 2024-12-01 02:20:00 | GOES-16 | PEDRO DO ROSÁRIO | MARANHÃO | Brasil | 2108256 | 21 | 33 | nan | nan | nan | Amazônia | 90.6 |
| bb3dcaec-8253-3e5b-a468-37701cdac9e8 | -3.3134 | -53.8592 | 2024-12-01 02:20:00 | GOES-16 | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | 67.1 |
| 1c8577e8-a4dc-3a89-af71-225731a85e3b | -3.4754 | -50.2776 | 2024-12-01 02:20:00 | GOES-16 | PACAJÁ | PARÁ | Brasil | 1505486 | 15 | 33 | nan | nan | nan | Amazônia | 73.5 |
| 3e805733-0cd2-37c6-868d-c28dde5e20bb | -4.5394 | -45.7019 | 2024-12-01 02:20:00 | GOES-16 | PAULO RAMOS | MARANHÃO | Brasil | 2108108 | 21 | 33 | nan | nan | nan | Amazônia | 81.3 |
| 2da6e72b-5e0c-3c4c-be5b-22143c9bdee9 | -4.5563 | -43.2795 | 2024-12-01 02:20:00 | GOES-16 | ALDEIAS ALTAS | MARANHÃO | Brasil | 2100303 | 21 | 33 | nan | nan | nan | Cerrado | 74.2 |
| a17ecfe9-9a86-3cdc-9209-05d7f719a3e9 | -1.7139 | -46.1422 | 2024-12-01 02:20:00 | GOES-16 | BOA VISTA DO GURUPI | MARANHÃO | Brasil | 2101970 | 21 | 33 | nan | nan | nan | Amazônia | 60.8 |
| e2ea1db4-651f-3ea6-8578-e2cd65d3c563 | -2.7503 | -51.7553 | 2024-12-01 02:20:00 | GOES-16 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 76.6 |
| 8687d914-729c-3302-9aee-9eeeea86dbfc | -3.1456 | -54.5259 | 2024-12-01 02:20:00 | GOES-16 | MOJUÍ DOS CAMPOS | PARÁ | Brasil | 1504752 | 15 | 33 | nan | nan | nan | Amazônia | 67.3 |
| 2d42580e-3e79-3dec-bef8-418f959a5d3a | -10.6674 | -44.4835 | 2024-12-01 02:20:00 | GOES-16 | SANTA RITA DE CÁSSIA | BAHIA | Brasil | 2928406 | 29 | 33 | nan | nan | nan | Cerrado | 80.8 |
| 55419483-0b04-3fc6-b82b-ce9d07148d74 | -4.5392 | -45.7243 | 2024-12-01 02:20:00 | GOES-16 | BREJO DE AREIA | MARANHÃO | Brasil | 2102150 | 21 | 33 | nan | nan | nan | Amazônia | 55.6 |
| d8dc7572-335c-314b-84b1-9c4c55ab610c | -3.2774 | -53.6383 | 2024-12-01 02:20:00 | GOES-16 | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | 66.3 |
| e56d8e7e-e57d-3a0b-bd0c-0739e3fb90b3 | -3.1273 | -54.5264 | 2024-12-01 02:20:00 | GOES-16 | MOJUÍ DOS CAMPOS | PARÁ | Brasil | 1504752 | 15 | 33 | nan | nan | nan | Amazônia | 77.3 |
| f912b51f-b28e-3a89-902d-4e5eb9a7cb38 | -3.259 | -53.6388 | 2024-12-01 02:20:00 | GOES-16 | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | 115.1 |
| a9c2b8c4-b463-35fe-bae0-8b390cb28e3c | 1.1622 | -55.9869 | 2024-12-01 02:20:00 | GOES-16 | ORIXIMINÁ | PARÁ | Brasil | 1505304 | 15 | 33 | nan | nan | nan | Amazônia | 46.3 |
| 07a70802-08fd-33f7-a88c-dc8c31920e27 | -6.9156 | -43.5418 | 2024-12-01 02:20:00 | GOES-16 | JERUMENHA | PIAUÍ | Brasil | 2205300 | 22 | 33 | nan | nan | nan | Cerrado | 130.0 |
| b5aa43d6-ecb1-31d8-a407-0f08adabd302 | -2.6578 | -51.8811 | 2024-12-01 02:20:00 | GOES-16 | SENADOR JOSÉ PORFÍRIO | PARÁ | Brasil | 1507805 | 15 | 33 | nan | nan | nan | Amazônia | 77.9 |
| ee89f765-6397-345f-a3a6-4851b3a37e83 | -2.9963 | -45.5706 | 2024-12-01 02:20:00 | GOES-16 | PEDRO DO ROSÁRIO | MARANHÃO | Brasil | 2108256 | 21 | 33 | nan | nan | nan | Amazônia | 82.5 |
| 6d91e910-e76a-3f24-a88c-78bdccfa1c6a | -3.2591 | -53.6186 | 2024-12-01 02:20:00 | GOES-16 | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | 75.7 |
| b627c57c-8378-3d04-9590-e94d5d0ee21e | -3.4974 | -53.8339 | 2024-12-01 02:20:00 | GOES-16 | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | 110.8 |
| 97614896-5319-39fc-bc2a-94591a7a8905 | -2.6579 | -51.8606 | 2024-12-01 02:20:00 | GOES-16 | SENADOR JOSÉ PORFÍRIO | PARÁ | Brasil | 1507805 | 15 | 33 | nan | nan | nan | Amazônia | 61.1 |
| 6c1d001f-3c54-385c-9dd2-6e76a9165de3 | -2.7503 | -51.7553 | 2024-12-01 02:30:00 | GOES-16 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 62.7 |
| 3520ee09-90ef-35b8-b968-cbbbecfb9de4 | -3.2591 | -53.6186 | 2024-12-01 02:30:00 | GOES-16 | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | 76.9 |
| 74de6d62-cf5a-3da1-82aa-502e8b23ecea | -2.6578 | -51.8811 | 2024-12-01 02:30:00 | GOES-16 | SENADOR JOSÉ PORFÍRIO | PARÁ | Brasil | 1507805 | 15 | 33 | nan | nan | nan | Amazônia | 64.3 |
| 8839f6ce-50a7-3519-afc4-0e11997ea701 | -6.9156 | -43.5418 | 2024-12-01 02:30:00 | GOES-16 | JERUMENHA | PIAUÍ | Brasil | 2205300 | 22 | 33 | nan | nan | nan | Cerrado | 89.3 |
| e3c09cfe-765e-3719-8c38-e1075eb72a2c | -4.5375 | -43.304 | 2024-12-01 02:30:00 | GOES-16 | ALDEIAS ALTAS | MARANHÃO | Brasil | 2100303 | 21 | 33 | nan | nan | nan | Cerrado | 65.2 |
| 26761b9c-87a1-3f90-89ec-1c4209479403 | -10.1226 | -36.3067 | 2024-12-01 02:30:00 | GOES-16 | CORURIPE | ALAGOAS | Brasil | 2702306 | 27 | 33 | nan | nan | nan | Mata Atlântica | 74.1 |
| b4f90bbc-d826-3f68-872d-0ab54be7bb3f | -3.69 | -51.8101 | 2024-12-01 02:30:00 | GOES-16 | SENADOR JOSÉ PORFÍRIO | PARÁ | Brasil | 1507805 | 15 | 33 | nan | nan | nan | Amazônia | 64.1 |
| c6b3b344-b8c9-3804-952f-c59b7cc4afcf | -6.9344 | -43.5401 | 2024-12-01 02:30:00 | GOES-16 | JERUMENHA | PIAUÍ | Brasil | 2205300 | 22 | 33 | nan | nan | nan | Cerrado | 155.6 |
| aa5ac751-6cbb-3484-9c66-c7400d8ad4a7 | -3.4974 | -53.8339 | 2024-12-01 02:30:00 | GOES-16 | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | 88.5 |
| 0f603506-27d8-3ad7-8e5e-48ce2f4efe05 | -2.8197 | -53.0425 | 2024-12-01 02:30:00 | GOES-16 | MEDICILÂNDIA | PARÁ | Brasil | 1504455 | 15 | 33 | nan | nan | nan | Amazônia | 66.0 |
| 352b87c6-ccbe-3ffa-8570-4b447902ec6e | -4.5563 | -43.2795 | 2024-12-01 02:30:00 | GOES-16 | ALDEIAS ALTAS | MARANHÃO | Brasil | 2100303 | 21 | 33 | nan | nan | nan | Cerrado | 66.9 |
| 6d21ae1c-732b-3132-be77-6d6c0305fc63 | -3.2774 | -53.6383 | 2024-12-01 02:30:00 | GOES-16 | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | 64.4 |
| eb3e6fed-f06f-3e59-9076-d1b37e8d3397 | -10.1221 | -36.3337 | 2024-12-01 02:30:00 | GOES-16 | CORURIPE | ALAGOAS | Brasil | 2702306 | 27 | 33 | nan | nan | nan | Mata Atlântica | 116.5 |
| b43312bc-efc1-343f-89cd-dcd4dc350647 | -3.259 | -53.6388 | 2024-12-01 02:30:00 | GOES-16 | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | 98.6 |
| e682994f-9f6a-30d2-b824-c7b5333a5268 | -4.558 | -45.7008 | 2024-12-01 02:30:00 | GOES-16 | PAULO RAMOS | MARANHÃO | Brasil | 2108108 | 21 | 33 | nan | nan | nan | Amazônia | 61.2 |
| 07fd70f5-0e79-329a-9065-43b924f96d2e | -2.9963 | -45.5706 | 2024-12-01 02:30:00 | GOES-16 | PEDRO DO ROSÁRIO | MARANHÃO | Brasil | 2108256 | 21 | 33 | nan | nan | nan | Amazônia | 103.7 |
| 2f96ec13-f7f9-3eed-9a72-d816c1160f82 | -4.5562 | -43.3028 | 2024-12-01 02:30:00 | GOES-16 | ALDEIAS ALTAS | MARANHÃO | Brasil | 2100303 | 21 | 33 | nan | nan | nan | Cerrado | 167.5 |
| 5b16e7e9-d3a5-3112-bc66-0321a23e451a | -10.6674 | -44.4835 | 2024-12-01 02:30:00 | GOES-16 | SANTA RITA DE CÁSSIA | BAHIA | Brasil | 2928406 | 29 | 33 | nan | nan | nan | Cerrado | 64.8 |
| 8a5a6cd4-7509-3214-a277-e92b24b74246 | -3.5158 | -53.8333 | 2024-12-01 02:30:00 | GOES-16 | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | 78.6 |
| bde0256a-760b-32b8-b2b3-e388e8b7475f | -3.1273 | -54.5264 | 2024-12-01 02:30:00 | GOES-16 | MOJUÍ DOS CAMPOS | PARÁ | Brasil | 1504752 | 15 | 33 | nan | nan | nan | Amazônia | 79.0 |
| 5512bef5-5a29-3ccb-bd78-2247611d1d04 | -4.5394 | -45.7019 | 2024-12-01 02:30:00 | GOES-16 | PAULO RAMOS | MARANHÃO | Brasil | 2108108 | 21 | 33 | nan | nan | nan | Amazônia | 82.8 |
| 22dd8f68-a3cb-3696-9440-ed4eb0319733 | -2.9778 | -45.5713 | 2024-12-01 02:30:00 | GOES-16 | PEDRO DO ROSÁRIO | MARANHÃO | Brasil | 2108256 | 21 | 33 | nan | nan | nan | Amazônia | 90.1 |
| e14b1cf4-a9a6-36c1-a41d-859545aa26be | -4.5578 | -45.7232 | 2024-12-01 02:30:00 | GOES-16 | SANTA LUZIA | MARANHÃO | Brasil | 2110005 | 21 | 33 | nan | nan | nan | Amazônia | 136.9 |
| 73baf199-324a-34cb-ba69-b1e759ee9c4e | -6.9344 | -43.5401 | 2024-12-01 02:40:00 | GOES-16 | JERUMENHA | PIAUÍ | Brasil | 2205300 | 22 | 33 | nan | nan | nan | Cerrado | 137.0 |
| df276c80-89d7-3708-87c4-42101bfa8548 | 1.1438 | -56.0067 | 2024-12-01 02:40:00 | GOES-16 | ORIXIMINÁ | PARÁ | Brasil | 1505304 | 15 | 33 | nan | nan | nan | Amazônia | 46.2 |
| 389cd210-ce70-3936-9807-1ed8649bf23f | -3.4974 | -53.8339 | 2024-12-01 02:40:00 | GOES-16 | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | 85.3 |
| 0c810804-8114-30d3-b8c7-a04ac3f5d4f8 | -4.5563 | -43.2795 | 2024-12-01 02:40:00 | GOES-16 | ALDEIAS ALTAS | MARANHÃO | Brasil | 2100303 | 21 | 33 | nan | nan | nan | Cerrado | 60.4 |
| 6660ee14-95d0-339a-b888-f59bd102ccde | -2.8196 | -53.0629 | 2024-12-01 02:40:00 | GOES-16 | MEDICILÂNDIA | PARÁ | Brasil | 1504455 | 15 | 33 | nan | nan | nan | Amazônia | 56.8 |
| 36a880c7-b056-31a9-8fc8-9e499dbd1540 | -4.5562 | -43.3028 | 2024-12-01 02:40:00 | GOES-16 | ALDEIAS ALTAS | MARANHÃO | Brasil | 2100303 | 21 | 33 | nan | nan | nan | Cerrado | 190.6 |
| f875a0ed-2e0c-3c76-9a5f-a3cc0d3e03a7 | -2.9778 | -45.5713 | 2024-12-01 02:40:00 | GOES-16 | PEDRO DO ROSÁRIO | MARANHÃO | Brasil | 2108256 | 21 | 33 | nan | nan | nan | Amazônia | 75.3 |
| e7079fdb-ee03-3894-849c-24be52ab93d3 | -3.4754 | -50.2776 | 2024-12-01 02:40:00 | GOES-16 | PACAJÁ | PARÁ | Brasil | 1505486 | 15 | 33 | nan | nan | nan | Amazônia | 58.6 |
| a0f056c1-4f04-3b48-a62a-9f7d71325997 | 1.1622 | -55.9672 | 2024-12-01 02:40:00 | GOES-16 | ORIXIMINÁ | PARÁ | Brasil | 1505304 | 15 | 33 | nan | nan | nan | Amazônia | 39.9 |
| f678fb21-9738-3037-8a53-af986cb804f0 | -3.1273 | -54.5264 | 2024-12-01 02:40:00 | GOES-16 | MOJUÍ DOS CAMPOS | PARÁ | Brasil | 1504752 | 15 | 33 | nan | nan | nan | Amazônia | 70.2 |
| 96cf76dc-c2f2-3316-84c9-07795b91309c | 2.1515 | -55.7778 | 2024-12-01 02:40:00 | GOES-16 | ÓBIDOS | PARÁ | Brasil | 1505106 | 15 | 33 | nan | nan | nan | Amazônia | 41.9 |
| 172c390a-cf38-390b-8d21-6dabf3f76fc2 | 1.1622 | -55.9869 | 2024-12-01 02:40:00 | GOES-16 | ORIXIMINÁ | PARÁ | Brasil | 1505304 | 15 | 33 | nan | nan | nan | Amazônia | 68.3 |
| 2e0313ee-ab90-3bfe-9298-a0b77a99ead7 | -3.5158 | -53.8333 | 2024-12-01 02:40:00 | GOES-16 | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | 64.4 |
| 372fba92-20b6-33ca-935d-ff7e6ec22f56 | -2.8197 | -53.0425 | 2024-12-01 02:40:00 | GOES-16 | MEDICILÂNDIA | PARÁ | Brasil | 1504455 | 15 | 33 | nan | nan | nan | Amazônia | 66.1 |
| 50a2959e-ef68-31f0-bdc3-951a9d35271f | -4.5578 | -45.7232 | 2024-12-01 02:40:00 | GOES-16 | SANTA LUZIA | MARANHÃO | Brasil | 2110005 | 21 | 33 | nan | nan | nan | Amazônia | 133.9 |
| 0b56efca-b1c5-374a-ad08-6a00e3ac1a84 | -2.9962 | -45.593 | 2024-12-01 02:40:00 | GOES-16 | PEDRO DO ROSÁRIO | MARANHÃO | Brasil | 2108256 | 21 | 33 | nan | nan | nan | Amazônia | 61.7 |
| f246e336-616c-3656-b928-0d41f5b2635d | -6.9156 | -43.5418 | 2024-12-01 02:40:00 | GOES-16 | JERUMENHA | PIAUÍ | Brasil | 2205300 | 22 | 33 | nan | nan | nan | Cerrado | 83.5 |
| 8e9560b2-9360-38b1-8fd5-eff509430c96 | 1.1439 | -55.9871 | 2024-12-01 02:40:00 | GOES-16 | ORIXIMINÁ | PARÁ | Brasil | 1505304 | 15 | 33 | nan | nan | nan | Amazônia | 68.3 |


[Clique aqui para ver as próximas entradas](README19.md)
