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

## Dados Diários - Página 4

| ID | Latitude | Longitude | Data/Hora GMT | Satélite | Município | Estado | País | Município ID | Estado ID | País ID | Dias sem Chuva | Precipitação | Risco de Fogo | Bioma | FRP |
|----|----------|-----------|---------------|----------|-----------|--------|------|--------------|-----------|---------|----------------|--------------|----------------|-------|-----|
| fd2b83a3-b9ea-3dc2-bbfe-4e0a85e7d142 | -17.6079 | -57.4688 | 2024-11-15 00:10:00 | GOES-16 | POCONÉ | MATO GROSSO | Brasil | 5106505 | 51 | 33 | nan | nan | nan | Pantanal | 61.3 |
| 151c81a1-dece-3a4e-bac4-bc108c4037e1 | -17.2543 | -57.4698 | 2024-11-15 00:10:00 | GOES-16 | CÁCERES | MATO GROSSO | Brasil | 5102504 | 51 | 33 | nan | nan | nan | Pantanal | 159.2 |
| 1d8bb233-f88c-3b50-ac1e-81ca5f2d4c81 | -17.5882 | -57.4711 | 2024-11-15 00:10:00 | GOES-16 | POCONÉ | MATO GROSSO | Brasil | 5106505 | 51 | 33 | nan | nan | nan | Pantanal | 106.3 |
| 673c46da-d73b-3df5-a17e-b8be58fef214 | -9.9665 | -36.4152 | 2024-11-15 00:10:00 | GOES-16 | TEOTÔNIO VILELA | ALAGOAS | Brasil | 2709152 | 27 | 33 | nan | nan | nan | Mata Atlântica | 64.1 |
| 1279f258-a282-3d70-b2f8-d13dc47464f4 | 1.0513 | -51.0825 | 2024-11-15 00:12:00 | METOP-B | TARTARUGALZINHO | AMAPÁ | Brasil | 1600709 | 16 | 33 | nan | nan | nan | Amazônia | nan |
| 437feea6-071b-3951-b9d6-d3b389b478b4 | 0.4415 | -50.915401 | 2024-11-15 00:12:00 | METOP-B | MACAPÁ | AMAPÁ | Brasil | 1600303 | 16 | 33 | nan | nan | nan | Amazônia | nan |
| aecf2959-5fea-37ea-99fd-3886827f0ad9 | -3.615 | -44.7925 | 2024-11-15 00:12:00 | METOP-B | ARARI | MARANHÃO | Brasil | 2101004 | 21 | 33 | nan | nan | nan | Amazônia | nan |
| 765692f4-8d7e-3082-a4cf-4007dac9bb2a | -5.9652 | -42.1679 | 2024-11-15 00:12:00 | METOP-B | SÃO FÉLIX DO PIAUÍ | PIAUÍ | Brasil | 2209609 | 22 | 33 | nan | nan | nan | Caatinga | nan |
| 161a48fc-4577-361e-b673-00b89491f0fb | 1.079 | -51.1413 | 2024-11-15 00:12:00 | METOP-B | TARTARUGALZINHO | AMAPÁ | Brasil | 1600709 | 16 | 33 | nan | nan | nan | Amazônia | nan |
| 43a52b51-6326-3ee3-8abf-339112c2c5a8 | -3.4332 | -44.081001 | 2024-11-15 00:12:00 | METOP-B | ITAPECURU MIRIM | MARANHÃO | Brasil | 2105401 | 21 | 33 | nan | nan | nan | Cerrado | nan |
| f673d1a0-c4ab-3cd3-b196-e4fc7e61e8ed | 1.0767 | -51.151402 | 2024-11-15 00:12:00 | METOP-B | TARTARUGALZINHO | AMAPÁ | Brasil | 1600709 | 16 | 33 | nan | nan | nan | Amazônia | nan |
| bb6a29fc-8985-3e78-b584-8525d0a63360 | -3.597 | -44.485199 | 2024-11-15 00:12:00 | METOP-B | MATÕES DO NORTE | MARANHÃO | Brasil | 2106631 | 21 | 33 | nan | nan | nan | Cerrado | nan |
| 956fe80b-9052-3f9a-95ea-4e675f0d70f7 | -0.9028 | -47.845798 | 2024-11-15 00:12:00 | METOP-B | CURUÇÁ | PARÁ | Brasil | 1502905 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| d6ce97dd-0098-34ab-b578-f34086a1acf2 | 1.0836 | -51.121201 | 2024-11-15 00:12:00 | METOP-B | TARTARUGALZINHO | AMAPÁ | Brasil | 1600709 | 16 | 33 | nan | nan | nan | Amazônia | nan |
| b7d1675d-a301-3506-a17a-e83ccfb29a47 | 1.0813 | -51.131302 | 2024-11-15 00:12:00 | METOP-B | TARTARUGALZINHO | AMAPÁ | Brasil | 1600709 | 16 | 33 | nan | nan | nan | Amazônia | nan |
| 2afece28-7299-370e-a700-d5bce03f29c5 | -3.3322 | -43.999401 | 2024-11-15 00:12:00 | METOP-B | PRESIDENTE VARGAS | MARANHÃO | Brasil | 2109304 | 21 | 33 | nan | nan | nan | Cerrado | nan |
| 0fdab9b8-cea7-3123-93b1-1da93c1c2ba8 | -3.5954 | -44.478298 | 2024-11-15 00:12:00 | METOP-B | MATÕES DO NORTE | MARANHÃO | Brasil | 2106631 | 21 | 33 | nan | nan | nan | Cerrado | nan |
| b7cd3f1c-6d7c-3e07-8178-7da64317b1cc | -3.6135 | -44.785702 | 2024-11-15 00:12:00 | METOP-B | ARARI | MARANHÃO | Brasil | 2101004 | 21 | 33 | nan | nan | nan | Amazônia | nan |
| 8f213f70-4a4b-38ea-b866-6363696ba151 | -3.81 | -45.7029 | 2024-11-15 00:12:00 | METOP-B | SANTA LUZIA | MARANHÃO | Brasil | 2110005 | 21 | 33 | nan | nan | nan | Amazônia | nan |
| b6330d6e-c76c-3cd7-ac47-dcf72ae43cc6 | -0.786 | -49.476398 | 2024-11-15 00:12:00 | METOP-B | PONTA DE PEDRAS | PARÁ | Brasil | 1505700 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| 04588b88-8c5f-387d-ad73-182e89fabdaf | -3.5373 | -45.727402 | 2024-11-15 00:12:00 | METOP-B | BOM JARDIM | MARANHÃO | Brasil | 2102002 | 21 | 33 | nan | nan | nan | Amazônia | nan |
| 9a655e52-d779-3b04-9be5-0969b0a4a451 | -3.3338 | -44.0065 | 2024-11-15 00:12:00 | METOP-B | PRESIDENTE VARGAS | MARANHÃO | Brasil | 2109304 | 21 | 33 | nan | nan | nan | Cerrado | nan |
| 88309ed3-7053-3073-8ea5-05d4fdf94684 | 0.1215 | -49.830601 | 2024-11-15 00:12:00 | METOP-B | CHAVES | PARÁ | Brasil | 1502509 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| f2efccc2-98a1-3bf0-92bd-d2a9dee4d69e | -3.6119 | -44.778801 | 2024-11-15 00:12:00 | METOP-B | ARARI | MARANHÃO | Brasil | 2101004 | 21 | 33 | nan | nan | nan | Amazônia | nan |
| 8f9591f0-1755-39e1-8525-13aa284237a1 | 0.1196 | -49.839401 | 2024-11-15 00:12:00 | METOP-B | CHAVES | PARÁ | Brasil | 1502509 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| 0b31277d-0bae-34ca-8c9a-3ad916148bbe | -3.3387 | -44.027802 | 2024-11-15 00:12:00 | METOP-B | PRESIDENTE VARGAS | MARANHÃO | Brasil | 2109304 | 21 | 33 | nan | nan | nan | Cerrado | nan |
| 997383b6-e640-3ce4-9a4f-3fcf3d4cc297 | 0.4438 | -50.905499 | 2024-11-15 00:12:00 | METOP-B | MACAPÁ | AMAPÁ | Brasil | 1600303 | 16 | 33 | nan | nan | nan | Amazônia | nan |
| d1766aaf-a27c-3ab0-ac61-22aa7d71652d | -17.6079 | -57.4688 | 2024-11-15 00:20:00 | GOES-16 | POCONÉ | MATO GROSSO | Brasil | 5106505 | 51 | 33 | nan | nan | nan | Pantanal | 59.6 |
| 6d0f8ad6-4483-3747-9683-e1c9594b5b7d | -2.8534 | -53.9915 | 2024-11-15 00:20:00 | GOES-16 | PRAINHA | PARÁ | Brasil | 1506005 | 15 | 33 | nan | nan | nan | Amazônia | 55.1 |
| 245fd24f-69d1-3089-88aa-0950a8c09b20 | -1.9012 | -45.4687 | 2024-11-15 00:20:00 | GOES-16 | TURIAÇU | MARANHÃO | Brasil | 2112407 | 21 | 33 | nan | nan | nan | Amazônia | 98.0 |
| 594b7d76-be03-3cf7-898d-1049662da343 | 1.0765 | -51.1441 | 2024-11-15 00:20:00 | GOES-16 | TARTARUGALZINHO | AMAPÁ | Brasil | 1600709 | 16 | 33 | nan | nan | nan | Amazônia | 85.2 |
| 820271aa-642b-367e-a034-dfe0be7cf98c | -17.5882 | -57.4711 | 2024-11-15 00:20:00 | GOES-16 | POCONÉ | MATO GROSSO | Brasil | 5106505 | 51 | 33 | nan | nan | nan | Pantanal | 102.7 |
| faf732a9-78d8-3372-96ca-be4305ec0112 | -17.7052 | -57.5392 | 2024-11-15 00:20:00 | GOES-16 | POCONÉ | MATO GROSSO | Brasil | 5106505 | 51 | 33 | nan | nan | nan | Pantanal | 59.1 |
| 8ddce37d-8a17-3f75-816e-253ba620d71f | -3.7068 | -41.6758 | 2024-11-15 00:20:00 | GOES-16 | PIRACURUCA | PIAUÍ | Brasil | 2208304 | 22 | 33 | nan | nan | nan | Caatinga | 89.7 |
| f6a6eb44-0646-3d3e-ad38-b5c5a0e26527 | -7.1725 | -35.0015 | 2024-11-15 00:20:00 | GOES-16 | SANTA RITA | PARAÍBA | Brasil | 2513703 | 25 | 33 | nan | nan | nan | Mata Atlântica | 61.2 |
| d38a9a0a-df42-3a42-bf6c-ec3e659dc416 | -2.6596 | -46.1843 | 2024-11-15 00:20:00 | GOES-16 | CENTRO DO GUILHERME | MARANHÃO | Brasil | 2103158 | 21 | 33 | nan | nan | nan | Amazônia | 111.8 |
| 1ce9e6ae-c814-3a75-9dd3-0115c7c81c01 | -3.7254 | -41.6987 | 2024-11-15 00:20:00 | GOES-16 | PIRACURUCA | PIAUÍ | Brasil | 2208304 | 22 | 33 | nan | nan | nan | Caatinga | 105.9 |
| 5cd88b82-4295-3a4c-aeef-6fc87886f961 | -3.8054 | -43.9002 | 2024-11-15 00:20:00 | GOES-16 | VARGEM GRANDE | MARANHÃO | Brasil | 2112704 | 21 | 33 | nan | nan | nan | Cerrado | 150.6 |
| daf0d86b-6ec9-309b-985c-85ec740c5d1d | 1.0764 | -51.1648 | 2024-11-15 00:20:00 | GOES-16 | TARTARUGALZINHO | AMAPÁ | Brasil | 1600709 | 16 | 33 | nan | nan | nan | Amazônia | 76.9 |
| 9cc08f6f-0c93-302f-9068-2df1e21b96d5 | -2.3408 | -47.2069 | 2024-11-15 00:20:00 | GOES-16 | GARRAFÃO DO NORTE | PARÁ | Brasil | 1503077 | 15 | 33 | nan | nan | nan | Amazônia | 79.8 |
| 80f1164b-7284-3e05-8da9-fa14cb028516 | -17.7048 | -57.5597 | 2024-11-15 00:20:00 | GOES-16 | POCONÉ | MATO GROSSO | Brasil | 5106505 | 51 | 33 | nan | nan | nan | Pantanal | 53.8 |
| 3ea738a2-eec9-31f0-8d60-e939e164a351 | -17.5885 | -57.4506 | 2024-11-15 00:20:00 | GOES-16 | POCONÉ | MATO GROSSO | Brasil | 5106505 | 51 | 33 | nan | nan | nan | Pantanal | 51.2 |
| 83eaa432-57ab-3e28-b310-176be12ec1ac | -17.5879 | -57.4917 | 2024-11-15 00:20:00 | GOES-16 | POCONÉ | MATO GROSSO | Brasil | 5106505 | 51 | 33 | nan | nan | nan | Pantanal | 58.4 |
| d42cd8bb-5aa1-3dc7-b29b-bab7a981ed61 | -17.2547 | -57.4493 | 2024-11-15 00:20:00 | GOES-16 | CÁCERES | MATO GROSSO | Brasil | 5102504 | 51 | 33 | nan | nan | nan | Pantanal | 129.3 |
| ee29ff4d-0a8f-30dc-8702-7b5ef125558f | -2.3407 | -47.2288 | 2024-11-15 00:20:00 | GOES-16 | CAPITÃO POÇO | PARÁ | Brasil | 1502301 | 15 | 33 | nan | nan | nan | Amazônia | 69.9 |
| 8d337977-7305-3b99-8822-9d0091d7317f | -2.3233 | -46.8786 | 2024-11-15 00:20:00 | GOES-16 | NOVA ESPERANÇA DO PIRIÁ | PARÁ | Brasil | 1504950 | 15 | 33 | nan | nan | nan | Amazônia | 114.7 |
| 73e02c16-1184-33be-a09c-f3250b0fcfa3 | -2.9825 | -53.8476 | 2024-11-15 00:20:00 | GOES-16 | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | 54.4 |
| 85781bb0-0772-37b8-9a14-5b4c23e45f89 | -3.7867 | -43.9011 | 2024-11-15 00:20:00 | GOES-16 | VARGEM GRANDE | MARANHÃO | Brasil | 2112704 | 21 | 33 | nan | nan | nan | Cerrado | 188.8 |
| 745d9f4d-d430-355f-ae69-9e35231f057e | -17.274 | -57.4675 | 2024-11-15 00:20:00 | GOES-16 | CÁCERES | MATO GROSSO | Brasil | 5102504 | 51 | 33 | nan | nan | nan | Pantanal | 63.2 |
| aac397cf-766a-3edd-a8d0-8622564fdad1 | -2.641 | -46.1849 | 2024-11-15 00:20:00 | GOES-16 | CENTRO DO GUILHERME | MARANHÃO | Brasil | 2103158 | 21 | 33 | nan | nan | nan | Amazônia | 96.9 |
| 475153eb-6e54-3ced-94d5-38efbbc136b2 | -2.9825 | -53.8677 | 2024-11-15 00:20:00 | GOES-16 | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | 54.8 |
| bf5e7b7b-4e87-3747-aa62-179e96bfc1ea | -15.3025 | -56.5268 | 2024-11-15 00:20:00 | GOES-16 | JANGADA | MATO GROSSO | Brasil | 5104906 | 51 | 33 | nan | nan | nan | Cerrado | 69.2 |
| a019fdd2-9444-3fd9-a769-d935bd849e09 | -3.7866 | -43.9241 | 2024-11-15 00:20:00 | GOES-16 | VARGEM GRANDE | MARANHÃO | Brasil | 2112704 | 21 | 33 | nan | nan | nan | Cerrado | 145.8 |
| 0a1caa80-3196-3afb-a31a-ea39852c978e | -2.8535 | -53.9714 | 2024-11-15 00:20:00 | GOES-16 | PRAINHA | PARÁ | Brasil | 1506005 | 15 | 33 | nan | nan | nan | Amazônia | 63.2 |
| 04ade7e1-ed53-3433-bb87-22ac895cc180 | -17.2347 | -57.4721 | 2024-11-15 00:20:00 | GOES-16 | CÁCERES | MATO GROSSO | Brasil | 5102504 | 51 | 33 | nan | nan | nan | Pantanal | 81.5 |
| 0140fae9-8a44-39b6-a7e8-c2c85ffd47fa | -17.235 | -57.4516 | 2024-11-15 00:20:00 | GOES-16 | CÁCERES | MATO GROSSO | Brasil | 5102504 | 51 | 33 | nan | nan | nan | Pantanal | 89.2 |
| 5b27539d-b2c1-3011-bf4a-3294aae0fedd | -17.2543 | -57.4698 | 2024-11-15 00:20:00 | GOES-16 | CÁCERES | MATO GROSSO | Brasil | 5102504 | 51 | 33 | nan | nan | nan | Pantanal | 163.2 |
| 7f1e8882-4c97-3544-800e-b940d7434e19 | -3.8053 | -43.9232 | 2024-11-15 00:20:00 | GOES-16 | VARGEM GRANDE | MARANHÃO | Brasil | 2112704 | 21 | 33 | nan | nan | nan | Cerrado | 116.0 |
| e9d99e4b-42da-3447-b2be-f24817cf2835 | -3.7066 | -41.6997 | 2024-11-15 00:20:00 | GOES-16 | PIRACURUCA | PIAUÍ | Brasil | 2208304 | 22 | 33 | nan | nan | nan | Caatinga | 143.0 |
| 0ece83de-9d7f-32d2-979a-772cc9233adb | -1.9013 | -45.4463 | 2024-11-15 00:20:00 | GOES-16 | TURIAÇU | MARANHÃO | Brasil | 2112407 | 21 | 33 | nan | nan | nan | Amazônia | 117.4 |
| 50dacf97-b92a-34c7-a787-1ce376ded41a | -3.3388 | -44.0139 | 2024-11-15 00:20:00 | GOES-16 | PRESIDENTE VARGAS | MARANHÃO | Brasil | 2109304 | 21 | 33 | nan | nan | nan | Cerrado | 112.0 |
| 360fec66-1eaa-35a3-b0c5-16d515a763ae | -2.3234 | -46.8567 | 2024-11-15 00:20:00 | GOES-16 | NOVA ESPERANÇA DO PIRIÁ | PARÁ | Brasil | 1504950 | 15 | 33 | nan | nan | nan | Amazônia | 101.1 |
| d1a5d593-d93d-33fc-9c39-883f2cdab09d | -2.6596 | -46.1843 | 2024-11-15 00:30:00 | GOES-16 | CENTRO DO GUILHERME | MARANHÃO | Brasil | 2103158 | 21 | 33 | nan | nan | nan | Amazônia | 113.5 |
| b71b27df-c5b0-3fc7-a8f1-ba0abaddb57e | -17.235 | -57.4516 | 2024-11-15 00:30:00 | GOES-16 | CÁCERES | MATO GROSSO | Brasil | 5102504 | 51 | 33 | nan | nan | nan | Pantanal | 108.4 |
| 221d36cc-08fc-3d76-a8ff-89cfb23b5780 | -17.274 | -57.4675 | 2024-11-15 00:30:00 | GOES-16 | CÁCERES | MATO GROSSO | Brasil | 5102504 | 51 | 33 | nan | nan | nan | Pantanal | 57.8 |
| 0df263d9-2d71-374a-9b8f-dda2b71f8ca0 | -3.7867 | -43.9011 | 2024-11-15 00:30:00 | GOES-16 | VARGEM GRANDE | MARANHÃO | Brasil | 2112704 | 21 | 33 | nan | nan | nan | Cerrado | 370.6 |
| 227acd59-fa4b-3456-8bc0-6542efa54115 | -17.2543 | -57.4698 | 2024-11-15 00:30:00 | GOES-16 | CÁCERES | MATO GROSSO | Brasil | 5102504 | 51 | 33 | nan | nan | nan | Pantanal | 158.5 |
| 536ca378-c88a-32d4-97a3-42b8754bd6b4 | -2.8535 | -53.9714 | 2024-11-15 00:30:00 | GOES-16 | PRAINHA | PARÁ | Brasil | 1506005 | 15 | 33 | nan | nan | nan | Amazônia | 80.6 |
| c5f2e4f6-5577-312e-824f-1f0a2095c227 | -2.3407 | -47.2288 | 2024-11-15 00:30:00 | GOES-16 | CAPITÃO POÇO | PARÁ | Brasil | 1502301 | 15 | 33 | nan | nan | nan | Amazônia | 72.8 |
| 9cb137fd-00c9-3db7-bc92-b87e42f978ab | -17.6079 | -57.4688 | 2024-11-15 00:30:00 | GOES-16 | POCONÉ | MATO GROSSO | Brasil | 5106505 | 51 | 33 | nan | nan | nan | Pantanal | 57.4 |
| f4519a24-3520-322f-974e-454b01b5aa39 | -3.8053 | -43.9232 | 2024-11-15 00:30:00 | GOES-16 | VARGEM GRANDE | MARANHÃO | Brasil | 2112704 | 21 | 33 | nan | nan | nan | Cerrado | 120.4 |
| dc6bc8a0-909d-3e6a-84b5-a98ae23758a5 | -3.7866 | -43.9241 | 2024-11-15 00:30:00 | GOES-16 | VARGEM GRANDE | MARANHÃO | Brasil | 2112704 | 21 | 33 | nan | nan | nan | Cerrado | 232.9 |
| 14e8f74e-de34-31fe-a94e-1bdc49479546 | -17.2547 | -57.4493 | 2024-11-15 00:30:00 | GOES-16 | CÁCERES | MATO GROSSO | Brasil | 5102504 | 51 | 33 | nan | nan | nan | Pantanal | 126.6 |
| c4eb9179-9e6a-3f86-bb4a-797ece98ac1e | -3.7066 | -41.6997 | 2024-11-15 00:30:00 | GOES-16 | PIRACURUCA | PIAUÍ | Brasil | 2208304 | 22 | 33 | nan | nan | nan | Caatinga | 92.8 |
| 46a69a1b-cbb1-3a1f-803c-9245eecaa188 | -2.3234 | -46.8567 | 2024-11-15 00:30:00 | GOES-16 | NOVA ESPERANÇA DO PIRIÁ | PARÁ | Brasil | 1504950 | 15 | 33 | nan | nan | nan | Amazônia | 91.7 |
| bf36f3d6-d2d9-3bec-bc0f-9c23516d5b5c | -2.8534 | -53.9915 | 2024-11-15 00:30:00 | GOES-16 | PRAINHA | PARÁ | Brasil | 1506005 | 15 | 33 | nan | nan | nan | Amazônia | 60.1 |
| d99f138e-a2d7-3804-a72b-64ac23f8856b | -3.8054 | -43.9002 | 2024-11-15 00:30:00 | GOES-16 | VARGEM GRANDE | MARANHÃO | Brasil | 2112704 | 21 | 33 | nan | nan | nan | Cerrado | 180.0 |
| 47786456-ed2a-3497-a3a4-9d291ff9fc8c | -3.7869 | -43.8781 | 2024-11-15 00:30:00 | GOES-16 | VARGEM GRANDE | MARANHÃO | Brasil | 2112704 | 21 | 33 | nan | nan | nan | Cerrado | 68.6 |
| e11d9bec-c0dc-3015-af77-8b3d538cba84 | -2.961 | -45.1672 | 2024-11-15 00:30:00 | GOES-16 | VIANA | MARANHÃO | Brasil | 2112803 | 21 | 33 | nan | nan | nan | Amazônia | 151.5 |
| df89b556-38c3-3554-8d9f-69edbaae22e1 | -3.7254 | -41.6987 | 2024-11-15 00:30:00 | GOES-16 | PIRACURUCA | PIAUÍ | Brasil | 2208304 | 22 | 33 | nan | nan | nan | Caatinga | 84.7 |
| 2bb4cf65-d857-311d-a58f-32146e037d0b | -2.641 | -46.1849 | 2024-11-15 00:30:00 | GOES-16 | CENTRO DO GUILHERME | MARANHÃO | Brasil | 2103158 | 21 | 33 | nan | nan | nan | Amazônia | 90.5 |
| d4cd9280-4ee8-3fa4-85d7-e3ffdcfa35c9 | -3.3388 | -44.0139 | 2024-11-15 00:30:00 | GOES-16 | PRESIDENTE VARGAS | MARANHÃO | Brasil | 2109304 | 21 | 33 | nan | nan | nan | Cerrado | 87.1 |
| 7ea5a5a9-7661-3c68-a54e-49a507c1d697 | -17.2347 | -57.4721 | 2024-11-15 00:30:00 | GOES-16 | CÁCERES | MATO GROSSO | Brasil | 5102504 | 51 | 33 | nan | nan | nan | Pantanal | 77.7 |
| 6be73f43-96a0-3e74-a0c3-968f52f96c3c | -7.2608 | -39.8494 | 2024-11-15 00:30:00 | GOES-16 | SANTANA DO CARIRI | CEARÁ | Brasil | 2312106 | 23 | 33 | nan | nan | nan | Caatinga | 59.3 |
| fcd8f621-ff9a-3635-94ef-8f0792b85a4f | -2.3233 | -46.8786 | 2024-11-15 00:30:00 | GOES-16 | NOVA ESPERANÇA DO PIRIÁ | PARÁ | Brasil | 1504950 | 15 | 33 | nan | nan | nan | Amazônia | 109.7 |
| 02bce166-8148-3e9b-ae73-d9b9472c236f | -2.9424 | -45.1679 | 2024-11-15 00:30:00 | GOES-16 | VIANA | MARANHÃO | Brasil | 2112803 | 21 | 33 | nan | nan | nan | Amazônia | 163.7 |
| 6aafc733-a953-3962-bf8b-dff02de80a15 | -17.7052 | -57.5392 | 2024-11-15 00:30:00 | GOES-16 | POCONÉ | MATO GROSSO | Brasil | 5106505 | 51 | 33 | nan | nan | nan | Pantanal | 55.6 |
| aa898d4d-fff9-3562-9252-4565ada503b0 | -3.7068 | -41.6758 | 2024-11-15 00:30:00 | GOES-16 | PIRACURUCA | PIAUÍ | Brasil | 2208304 | 22 | 33 | nan | nan | nan | Caatinga | 69.0 |
| a2455e22-2198-35ce-b0bb-d742a00f7235 | -1.9013 | -45.4463 | 2024-11-15 00:30:00 | GOES-16 | TURIAÇU | MARANHÃO | Brasil | 2112407 | 21 | 33 | nan | nan | nan | Amazônia | 88.9 |
| 55557f2e-8415-3935-9235-49fec196a4ef | -17.5879 | -57.4917 | 2024-11-15 00:30:00 | GOES-16 | POCONÉ | MATO GROSSO | Brasil | 5106505 | 51 | 33 | nan | nan | nan | Pantanal | 58.8 |
| 4f418dee-7611-3c48-89b3-886598b903f8 | -17.5882 | -57.4711 | 2024-11-15 00:30:00 | GOES-16 | POCONÉ | MATO GROSSO | Brasil | 5106505 | 51 | 33 | nan | nan | nan | Pantanal | 103.0 |
| 70bb4a43-b493-3025-b77a-7593a593066b | -1.9198 | -45.4459 | 2024-11-15 00:30:00 | GOES-16 | TURIAÇU | MARANHÃO | Brasil | 2112407 | 21 | 33 | nan | nan | nan | Amazônia | 98.2 |
| 36e5fe31-dbaa-3a01-a189-427b4f0c471e | -2.3408 | -47.2069 | 2024-11-15 00:30:00 | GOES-16 | GARRAFÃO DO NORTE | PARÁ | Brasil | 1503077 | 15 | 33 | nan | nan | nan | Amazônia | 68.7 |
| 7cec0d7e-c344-357f-8b2e-07f452b9cd0b | -3.0883 | -45.7687 | 2024-11-15 00:30:00 | GOES-16 | ARAGUANÃ | MARANHÃO | Brasil | 2100873 | 21 | 33 | nan | nan | nan | Amazônia | 90.3 |
| 0457072d-5ca0-3158-ba9c-55cac5300c0b | -15.3025 | -56.5268 | 2024-11-15 00:30:00 | GOES-16 | JANGADA | MATO GROSSO | Brasil | 5104906 | 51 | 33 | nan | nan | nan | Cerrado | 68.5 |
| afecabb2-ad23-34b2-a5bd-b9beaef89ffe | -3.8053 | -43.9232 | 2024-11-15 00:40:00 | GOES-16 | VARGEM GRANDE | MARANHÃO | Brasil | 2112704 | 21 | 33 | nan | nan | nan | Cerrado | 225.3 |
| adf17727-3e58-3df4-b735-46aa4629c1d6 | -2.961 | -45.1672 | 2024-11-15 00:40:00 | GOES-16 | VIANA | MARANHÃO | Brasil | 2112803 | 21 | 33 | nan | nan | nan | Amazônia | 102.0 |
| 4b0e7bb3-3830-3d1f-8af2-243999f4b61c | -4.2233 | -45.6289 | 2024-11-15 00:40:00 | GOES-16 | BREJO DE AREIA | MARANHÃO | Brasil | 2102150 | 21 | 33 | nan | nan | nan | Amazônia | 61.7 |
| 7a041293-3794-3d49-a8c2-b4ef1d941fd0 | -17.2347 | -57.4721 | 2024-11-15 00:40:00 | GOES-16 | CÁCERES | MATO GROSSO | Brasil | 5102504 | 51 | 33 | nan | nan | nan | Pantanal | 81.3 |
| b86ccdcb-e7ec-3585-8f5b-49f594805241 | -2.641 | -46.1849 | 2024-11-15 00:40:00 | GOES-16 | CENTRO DO GUILHERME | MARANHÃO | Brasil | 2103158 | 21 | 33 | nan | nan | nan | Amazônia | 94.4 |


[Clique aqui para ver as próximas entradas](README5.md)
