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

## Dados Diários - Página 34

| ID | Latitude | Longitude | Data/Hora GMT | Satélite | Município | Estado | País | Município ID | Estado ID | País ID | Dias sem Chuva | Precipitação | Risco de Fogo | Bioma | FRP |
|----|----------|-----------|---------------|----------|-----------|--------|------|--------------|-----------|---------|----------------|--------------|----------------|-------|-----|
| 043615c9-23d9-3311-a35a-6912d271ef20 | 3.5264 | -51.257 | 2024-11-05 13:50:00 | GOES-16 | OIAPOQUE | AMAPÁ | Brasil | 1600501 | 16 | 33 | nan | nan | nan | Amazônia | 90.7 |
| e6b26757-e578-3276-9494-44facc77cf1a | -1.514 | -53.512 | 2024-11-05 13:50:00 | GOES-16 | PRAINHA | PARÁ | Brasil | 1506005 | 15 | 33 | nan | nan | nan | Amazônia | 90.3 |
| 5ade9833-1364-3a76-a346-f8cbeebe6a9d | -2.4197 | -45.8355 | 2024-11-05 13:50:00 | GOES-16 | PRESIDENTE MÉDICI | MARANHÃO | Brasil | 2109239 | 21 | 33 | nan | nan | nan | Amazônia | 97.4 |
| 02048344-22f4-3984-914d-603c7422779d | -4.1522 | -42.2463 | 2024-11-05 13:50:00 | GOES-16 | BATALHA | PIAUÍ | Brasil | 2201507 | 22 | 33 | nan | nan | nan | Caatinga | 94.1 |
| a0b636df-ddfc-3dbc-983e-2b3f862c868e | -8.5002 | -42.0747 | 2024-11-05 13:50:00 | GOES-16 | CAPITÃO GERVÁSIO OLIVEIRA | PIAUÍ | Brasil | 2202455 | 22 | 33 | nan | nan | nan | Caatinga | 116.6 |
| df1a35f6-bb13-3f04-9969-e43890e346bb | -8.4998 | -42.0987 | 2024-11-05 13:50:00 | GOES-16 | CAPITÃO GERVÁSIO OLIVEIRA | PIAUÍ | Brasil | 2202455 | 22 | 33 | nan | nan | nan | Caatinga | 109.6 |
| 71be6677-9a4d-388e-96be-49c751543140 | 3.6185 | -51.2955 | 2024-11-05 13:50:00 | GOES-16 | OIAPOQUE | AMAPÁ | Brasil | 1600501 | 16 | 33 | nan | nan | nan | Amazônia | 75.5 |
| fa3822dd-01b0-3430-b58d-899c3fa29061 | -4.6877 | -45.8056 | 2024-11-05 14:00:00 | GOES-16 | MARAJÁ DO SENA | MARANHÃO | Brasil | 2106359 | 21 | 33 | nan | nan | nan | Amazônia | 103.0 |
| b380fcc2-9ccf-3391-9875-e9b3655dd0f7 | 3.5264 | -51.257 | 2024-11-05 14:00:00 | GOES-16 | OIAPOQUE | AMAPÁ | Brasil | 1600501 | 16 | 33 | nan | nan | nan | Amazônia | 87.1 |
| 0c93aa74-e2ef-3c05-9898-f6b9d000a72b | -10.2829 | -42.3673 | 2024-11-05 14:00:00 | GOES-16 | ITAGUAÇU DA BAHIA | BAHIA | Brasil | 2915353 | 29 | 33 | nan | nan | nan | Caatinga | 107.8 |
| e6a69b6a-89e2-3130-af37-4c7fa15b9317 | -1.3876 | -52.1918 | 2024-11-05 14:00:00 | GOES-16 | ALMEIRIM | PARÁ | Brasil | 1500503 | 15 | 33 | nan | nan | nan | Amazônia | 76.6 |
| 3240ab0a-1a78-3922-8e44-442904df9e7e | -1.406 | -52.1916 | 2024-11-05 14:00:00 | GOES-16 | ALMEIRIM | PARÁ | Brasil | 1500503 | 15 | 33 | nan | nan | nan | Amazônia | 95.7 |
| 41af00eb-93f1-3c4d-b1a8-8b033bd5e0bc | -2.6574 | -46.7591 | 2024-11-05 14:00:00 | GOES-16 | PARAGOMINAS | PARÁ | Brasil | 1505502 | 15 | 33 | nan | nan | nan | Amazônia | 91.9 |
| 409c9db0-060f-3b66-afc6-6cb08ad26f62 | -1.514 | -53.512 | 2024-11-05 14:00:00 | GOES-16 | PRAINHA | PARÁ | Brasil | 1506005 | 15 | 33 | nan | nan | nan | Amazônia | 92.1 |
| d500f064-ae61-34aa-9905-cdbdeadddeb4 | -3.9445 | -45.5755 | 2024-11-05 14:00:00 | GOES-16 | SANTA INÊS | MARANHÃO | Brasil | 2109908 | 21 | 33 | nan | nan | nan | Amazônia | 117.3 |
| 6677c41d-a5b4-38a5-a4ac-9b9eac473aaa | -10.2243 | -42.4476 | 2024-11-05 14:00:00 | GOES-16 | PILÃO ARCADO | BAHIA | Brasil | 2924405 | 29 | 33 | nan | nan | nan | Caatinga | 105.2 |
| 43f81382-7242-3dc0-a1d9-35a4de0c835a | -2.4197 | -45.8355 | 2024-11-05 14:00:00 | GOES-16 | PRESIDENTE MÉDICI | MARANHÃO | Brasil | 2109239 | 21 | 33 | nan | nan | nan | Amazônia | 113.6 |
| 93964257-f008-31d1-80ef-bf0ef88dcbbe | -2.6507 | -48.5629 | 2024-11-05 14:00:00 | GOES-16 | TAILÂNDIA | PARÁ | Brasil | 1507953 | 15 | 33 | nan | nan | nan | Amazônia | 100.9 |
| cbdad817-7293-33a2-99ce-3693d2522024 | -4.34 | -44.7 | 2024-11-05 14:00:00 | MSG-03 | SÃO LUÍS GONZAGA DO MARANHÃO | MARANHÃO | Brasil | 2111409 | 21 | 33 | nan | nan | nan | Cerrado | nan |
| 6c17996d-2768-360a-9629-3c68ec1d0146 | -4.34 | -44.75 | 2024-11-05 14:00:00 | MSG-03 | SÃO LUÍS GONZAGA DO MARANHÃO | MARANHÃO | Brasil | 2111409 | 21 | 33 | nan | nan | nan | Cerrado | nan |
| a633dd19-7498-3a31-a527-7a11010fdfe3 | -4.31 | -44.7 | 2024-11-05 14:00:00 | MSG-03 | SÃO LUÍS GONZAGA DO MARANHÃO | MARANHÃO | Brasil | 2111409 | 21 | 33 | nan | nan | nan | Cerrado | nan |
| 1e504fdd-ef8e-38b0-b801-df7532b4bb36 | -4.31 | -44.75 | 2024-11-05 14:00:00 | MSG-03 | SÃO LUÍS GONZAGA DO MARANHÃO | MARANHÃO | Brasil | 2111409 | 21 | 33 | nan | nan | nan | Cerrado | nan |
| de3f401c-b429-3840-b8a9-8ac110860c15 | -2.6507 | -48.5629 | 2024-11-05 14:10:00 | GOES-16 | TAILÂNDIA | PARÁ | Brasil | 1507953 | 15 | 33 | nan | nan | nan | Amazônia | 113.7 |
| cb873ac4-2cf7-3f91-b6f1-933d2285a1be | -3.4956 | -46.0649 | 2024-11-05 14:10:00 | GOES-16 | BOM JARDIM | MARANHÃO | Brasil | 2102002 | 21 | 33 | nan | nan | nan | Amazônia | 100.7 |
| 939129de-db14-3189-9a49-b7f1591f5c78 | -1.5532 | -52.1076 | 2024-11-05 14:10:00 | GOES-16 | GURUPÁ | PARÁ | Brasil | 1503101 | 15 | 33 | nan | nan | nan | Amazônia | 75.4 |
| c5d7b003-4420-3a87-af98-3da6a419e71f | -2.4197 | -45.8355 | 2024-11-05 14:10:00 | GOES-16 | PRESIDENTE MÉDICI | MARANHÃO | Brasil | 2109239 | 21 | 33 | nan | nan | nan | Amazônia | 126.7 |
| de5455d3-7fb7-333f-adbd-129923a059d4 | -3.9445 | -45.5755 | 2024-11-05 14:10:00 | GOES-16 | SANTA INÊS | MARANHÃO | Brasil | 2109908 | 21 | 33 | nan | nan | nan | Amazônia | 106.5 |
| 600c521d-33f3-3df0-a738-9c606e115f27 | -1.3876 | -52.1918 | 2024-11-05 14:10:00 | GOES-16 | ALMEIRIM | PARÁ | Brasil | 1500503 | 15 | 33 | nan | nan | nan | Amazônia | 77.1 |
| 0f23fa1f-91da-394e-be50-eba571771d1b | -2.193 | -53.6831 | 2024-11-05 14:10:00 | GOES-16 | PRAINHA | PARÁ | Brasil | 1506005 | 15 | 33 | nan | nan | nan | Amazônia | 100.4 |
| d62a8359-7d8f-39c9-890e-7a277ed25e4c | -2.6574 | -46.7591 | 2024-11-05 14:10:00 | GOES-16 | PARAGOMINAS | PARÁ | Brasil | 1505502 | 15 | 33 | nan | nan | nan | Amazônia | 113.7 |
| 6414fbc8-20a7-32ac-8d01-136e2ae3bc5d | -10.2243 | -42.4476 | 2024-11-05 14:10:00 | GOES-16 | PILÃO ARCADO | BAHIA | Brasil | 2924405 | 29 | 33 | nan | nan | nan | Caatinga | 110.6 |
| bcf2e351-7062-36f4-b353-13f9a5d27fca | -2.7881 | -51.4859 | 2024-11-05 14:10:00 | GOES-16 | ANAPU | PARÁ | Brasil | 1500859 | 15 | 33 | nan | nan | nan | Amazônia | 85.6 |
| 0c2697c0-d4fa-3411-b3f0-61e660b898ef | -8.5002 | -42.0747 | 2024-11-05 14:10:00 | GOES-16 | CAPITÃO GERVÁSIO OLIVEIRA | PIAUÍ | Brasil | 2202455 | 22 | 33 | nan | nan | nan | Caatinga | 107.5 |
| 627f5dbc-ebea-30f4-8f85-dd1ffb40d88e | 2.2003 | -50.8773 | 2024-11-05 14:20:00 | GOES-16 | CALÇOENE | AMAPÁ | Brasil | 1600204 | 16 | 33 | nan | nan | nan | Amazônia | 82.6 |
| 0b8dc7fe-dc59-376d-b778-893ddd75a777 | -1.3876 | -52.1918 | 2024-11-05 14:20:00 | GOES-16 | ALMEIRIM | PARÁ | Brasil | 1500503 | 15 | 33 | nan | nan | nan | Amazônia | 76.8 |
| e4dda47a-0511-3594-a344-a79b66a4b24b | -1.406 | -52.1916 | 2024-11-05 14:20:00 | GOES-16 | ALMEIRIM | PARÁ | Brasil | 1500503 | 15 | 33 | nan | nan | nan | Amazônia | 96.8 |
| b889c5b1-272f-3027-9c93-941c69c349f2 | -2.193 | -53.6831 | 2024-11-05 14:20:00 | GOES-16 | PRAINHA | PARÁ | Brasil | 1506005 | 15 | 33 | nan | nan | nan | Amazônia | 122.8 |
| 24cfb1ec-076f-336c-babc-18fbeca6326e | -2.6574 | -46.7591 | 2024-11-05 14:20:00 | GOES-16 | PARAGOMINAS | PARÁ | Brasil | 1505502 | 15 | 33 | nan | nan | nan | Amazônia | 97.4 |
| df667f07-8594-3bf1-be06-3d8a62af9520 | -1.6999 | -52.3513 | 2024-11-05 14:20:00 | GOES-16 | PORTO DE MOZ | PARÁ | Brasil | 1505908 | 15 | 33 | nan | nan | nan | Amazônia | 87.0 |
| b450053c-4d17-33ac-bca9-335c733d1cf4 | -1.514 | -53.512 | 2024-11-05 14:20:00 | GOES-16 | PRAINHA | PARÁ | Brasil | 1506005 | 15 | 33 | nan | nan | nan | Amazônia | 76.0 |
| ec3f7bd4-b844-3da6-9498-c6760a9fe22a | -1.3507 | -52.2946 | 2024-11-05 14:20:00 | GOES-16 | ALMEIRIM | PARÁ | Brasil | 1500503 | 15 | 33 | nan | nan | nan | Amazônia | 86.6 |
| c95bb3d7-f0c2-3767-8324-29cb6403a6b8 | -2.4196 | -45.8578 | 2024-11-05 14:20:00 | GOES-16 | PRESIDENTE MÉDICI | MARANHÃO | Brasil | 2109239 | 21 | 33 | nan | nan | nan | Amazônia | 92.9 |
| c5a06abc-0949-30d6-a32e-6ebd2aed06fa | -3.4956 | -46.0649 | 2024-11-05 14:20:00 | GOES-16 | BOM JARDIM | MARANHÃO | Brasil | 2102002 | 21 | 33 | nan | nan | nan | Amazônia | 95.0 |
| 6122040c-cf9c-35d4-b691-a1625c927a4f | 3.5264 | -51.257 | 2024-11-05 14:20:00 | GOES-16 | OIAPOQUE | AMAPÁ | Brasil | 1600501 | 16 | 33 | nan | nan | nan | Amazônia | 84.6 |
| 9f7f5b9f-9994-37ef-b2d5-35e19c0903d2 | -2.4197 | -45.8355 | 2024-11-05 14:20:00 | GOES-16 | PRESIDENTE MÉDICI | MARANHÃO | Brasil | 2109239 | 21 | 33 | nan | nan | nan | Amazônia | 128.1 |
| 20393e9b-7650-3499-b555-82b07ae9799b | -1.3507 | -52.2946 | 2024-11-05 14:30:00 | GOES-16 | ALMEIRIM | PARÁ | Brasil | 1500503 | 15 | 33 | nan | nan | nan | Amazônia | 97.4 |
| 87f7084e-0871-3d3f-8d01-b7381e458a13 | -2.4196 | -45.8578 | 2024-11-05 14:30:00 | GOES-16 | PRESIDENTE MÉDICI | MARANHÃO | Brasil | 2109239 | 21 | 33 | nan | nan | nan | Amazônia | 89.1 |
| 1d6461cb-5bf6-3cb4-8a5f-efcf181a753d | 1.4084 | -50.8076 | 2024-11-05 14:30:00 | GOES-16 | TARTARUGALZINHO | AMAPÁ | Brasil | 1600709 | 16 | 33 | nan | nan | nan | Amazônia | 76.2 |
| cf423d17-afd3-3296-a158-8f2e59c4a095 | -3.0917 | -54.1666 | 2024-11-05 14:30:00 | GOES-16 | SANTARÉM | PARÁ | Brasil | 1506807 | 15 | 33 | nan | nan | nan | Amazônia | 77.1 |
| cb45fa7e-8ea3-3ef9-93a4-52fbad88de45 | 1.4083 | -50.8285 | 2024-11-05 14:30:00 | GOES-16 | TARTARUGALZINHO | AMAPÁ | Brasil | 1600709 | 16 | 33 | nan | nan | nan | Amazônia | 77.1 |
| 409ebfa3-c380-34ed-8c25-98e6eb71ff82 | -1.3323 | -52.2744 | 2024-11-05 14:30:00 | GOES-16 | ALMEIRIM | PARÁ | Brasil | 1500503 | 15 | 33 | nan | nan | nan | Amazônia | 90.1 |
| 35a57758-7b91-399c-bd07-eec1da6de014 | -2.8438 | -51.3603 | 2024-11-05 14:30:00 | GOES-16 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 104.6 |
| 0a7eb893-72dc-3e05-9490-5910d7bfa607 | -2.193 | -53.6831 | 2024-11-05 14:30:00 | GOES-16 | PRAINHA | PARÁ | Brasil | 1506005 | 15 | 33 | nan | nan | nan | Amazônia | 78.7 |
| 68c101d3-f250-3a93-9062-10513265da4b | -1.6999 | -52.3513 | 2024-11-05 14:30:00 | GOES-16 | PORTO DE MOZ | PARÁ | Brasil | 1505908 | 15 | 33 | nan | nan | nan | Amazônia | 107.6 |
| c4912f20-8e13-3460-882d-040a2680770c | -3.0001 | -54.0885 | 2024-11-05 14:30:00 | GOES-16 | SANTARÉM | PARÁ | Brasil | 1506807 | 15 | 33 | nan | nan | nan | Amazônia | 99.0 |


