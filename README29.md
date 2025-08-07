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

## Dados Diários - Página 29

| ID | Latitude | Longitude | Data/Hora GMT | Satélite | Município | Estado | País | Município ID | Estado ID | País ID | Dias sem Chuva | Precipitação | Risco de Fogo | Bioma | FRP |
|----|----------|-----------|---------------|----------|-----------|--------|------|--------------|-----------|---------|----------------|--------------|----------------|-------|-----|
| d58864cb-ae09-3216-a257-c2106966f50a | -6.2789 | -45.2716 | 2025-08-07 12:20:00 | GOES-19 | FERNANDO FALCÃO | MARANHÃO | Brasil | 2104081 | 21 | 33 | nan | nan | nan | Cerrado | 108.3 |
| 079cbcc9-eba6-3c1a-a508-2ed154def9b2 | -10.6441 | -44.7413 | 2025-08-07 12:20:00 | GOES-19 | SEBASTIÃO BARROS | PIAUÍ | Brasil | 2210623 | 22 | 33 | nan | nan | nan | Cerrado | 147.6 |
| 946c6ca4-d8ff-36ea-8201-6d10f718a4c7 | -6.2604 | -45.2504 | 2025-08-07 12:20:00 | GOES-19 | FERNANDO FALCÃO | MARANHÃO | Brasil | 2104081 | 21 | 33 | nan | nan | nan | Cerrado | 172.7 |
| b58579d2-afd6-32d6-80bd-1a9b0e36f176 | -6.2792 | -45.249 | 2025-08-07 12:20:00 | GOES-19 | FERNANDO FALCÃO | MARANHÃO | Brasil | 2104081 | 21 | 33 | nan | nan | nan | Cerrado | 117.9 |
| 16c3ddb9-8ec1-31a9-87b9-13f3a2fdc884 | -5.678 | -41.3987 | 2025-08-07 12:20:00 | GOES-19 | SÃO MIGUEL DO TAPUIO | PIAUÍ | Brasil | 2210409 | 22 | 33 | nan | nan | nan | Caatinga | 100.1 |
| 85a69782-bbb2-3e7f-8da0-4a3a8d58738d | -6.2602 | -45.2731 | 2025-08-07 12:20:00 | GOES-19 | FERNANDO FALCÃO | MARANHÃO | Brasil | 2104081 | 21 | 33 | nan | nan | nan | Cerrado | 144.6 |
| ae281ded-7fb5-3ac1-a432-c240d529d094 | -10.6438 | -44.7645 | 2025-08-07 12:20:00 | GOES-19 | SEBASTIÃO BARROS | PIAUÍ | Brasil | 2210623 | 22 | 33 | nan | nan | nan | Cerrado | 85.1 |
| ad4a7d93-4d33-332e-b4ae-c21d804dd53d | -6.2789 | -45.2716 | 2025-08-07 12:30:00 | GOES-19 | FERNANDO FALCÃO | MARANHÃO | Brasil | 2104081 | 21 | 33 | nan | nan | nan | Cerrado | 126.9 |
| 4f7ec1f3-b440-3434-b4de-5c9a023c46b4 | -10.6441 | -44.7413 | 2025-08-07 12:30:00 | GOES-19 | SEBASTIÃO BARROS | PIAUÍ | Brasil | 2210623 | 22 | 33 | nan | nan | nan | Cerrado | 162.3 |
| f7111fdd-101e-3d53-a6f0-51c312dbf148 | -10.6438 | -44.7645 | 2025-08-07 12:30:00 | GOES-19 | SEBASTIÃO BARROS | PIAUÍ | Brasil | 2210623 | 22 | 33 | nan | nan | nan | Cerrado | 88.7 |
| 304c0bfb-5c92-34f0-ad37-ca5452bd0963 | -6.2792 | -45.249 | 2025-08-07 12:30:00 | GOES-19 | FERNANDO FALCÃO | MARANHÃO | Brasil | 2104081 | 21 | 33 | nan | nan | nan | Cerrado | 117.8 |
| 58b5dc82-8a31-34c5-86cc-da44812853aa | -6.2602 | -45.2731 | 2025-08-07 12:30:00 | GOES-19 | FERNANDO FALCÃO | MARANHÃO | Brasil | 2104081 | 21 | 33 | nan | nan | nan | Cerrado | 167.8 |
| 76c8af8a-7f5d-3cab-915f-ee1b4a98af7c | -6.2604 | -45.2504 | 2025-08-07 12:30:00 | GOES-19 | FERNANDO FALCÃO | MARANHÃO | Brasil | 2104081 | 21 | 33 | nan | nan | nan | Cerrado | 168.0 |
| 6e77783a-da5b-3014-8f37-4d713f316d21 | -6.2789 | -45.2716 | 2025-08-07 12:40:00 | GOES-19 | FERNANDO FALCÃO | MARANHÃO | Brasil | 2104081 | 21 | 33 | nan | nan | nan | Cerrado | 127.8 |
| 250c72e4-9e24-368a-b21f-20e7796d0499 | -10.6438 | -44.7645 | 2025-08-07 12:40:00 | GOES-19 | SEBASTIÃO BARROS | PIAUÍ | Brasil | 2210623 | 22 | 33 | nan | nan | nan | Cerrado | 87.1 |
| 973bd46d-0c89-3648-85a9-2ac23318859f | -6.2792 | -45.249 | 2025-08-07 12:40:00 | GOES-19 | FERNANDO FALCÃO | MARANHÃO | Brasil | 2104081 | 21 | 33 | nan | nan | nan | Cerrado | 127.4 |
| de9bb434-8048-3f8d-93aa-1c0d72b3715e | -8.9213 | -60.7489 | 2025-08-07 12:40:00 | GOES-19 | COLNIZA | MATO GROSSO | Brasil | 5103254 | 51 | 33 | nan | nan | nan | Amazônia | 63.6 |
| b2232e6f-d3e6-3624-9a79-4ea5ad4489a3 | -8.4897 | -45.7053 | 2025-08-07 12:40:00 | GOES-19 | SANTA FILOMENA | PIAUÍ | Brasil | 2209203 | 22 | 33 | nan | nan | nan | Cerrado | 110.8 |
| 32f9fccc-bbb0-3167-b4b4-90b5f8eea0a9 | -6.2604 | -45.2504 | 2025-08-07 12:40:00 | GOES-19 | FERNANDO FALCÃO | MARANHÃO | Brasil | 2104081 | 21 | 33 | nan | nan | nan | Cerrado | 161.5 |
| 90f4020a-9760-3971-ab88-8144559002af | -10.6441 | -44.7413 | 2025-08-07 12:40:00 | GOES-19 | SEBASTIÃO BARROS | PIAUÍ | Brasil | 2210623 | 22 | 33 | nan | nan | nan | Cerrado | 168.4 |
| d5f7e141-c684-3e94-8090-34f629045c16 | -8.5211 | -43.3063 | 2025-08-07 12:40:00 | GOES-19 | CANTO DO BURITI | PIAUÍ | Brasil | 2202307 | 22 | 33 | nan | nan | nan | Cerrado | 105.0 |
| d59d9a57-3356-3790-9692-da4ee4eabd39 | -6.2602 | -45.2731 | 2025-08-07 12:40:00 | GOES-19 | FERNANDO FALCÃO | MARANHÃO | Brasil | 2104081 | 21 | 33 | nan | nan | nan | Cerrado | 147.2 |
| 1c7b19ee-e260-3bcb-94a4-90ec8d700ee0 | -8.49 | -45.6826 | 2025-08-07 12:40:00 | GOES-19 | SANTA FILOMENA | PIAUÍ | Brasil | 2209203 | 22 | 33 | nan | nan | nan | Cerrado | 127.9 |
| ff4a7caf-4e8f-35b2-b69e-4c482db1599c | -10.6441 | -44.7413 | 2025-08-07 12:50:00 | GOES-19 | SEBASTIÃO BARROS | PIAUÍ | Brasil | 2210623 | 22 | 33 | nan | nan | nan | Cerrado | 161.1 |
| 1ffa873b-df3d-38c9-a815-4a3bb43c74a9 | -7.3012 | -39.6453 | 2025-08-07 12:50:00 | GOES-19 | SANTANA DO CARIRI | CEARÁ | Brasil | 2312106 | 23 | 33 | nan | nan | nan | Caatinga | 99.4 |
| 4f436622-8d87-3ff4-89ef-03d528f1e3a9 | -5.678 | -41.3987 | 2025-08-07 12:50:00 | GOES-19 | SÃO MIGUEL DO TAPUIO | PIAUÍ | Brasil | 2210409 | 22 | 33 | nan | nan | nan | Caatinga | 111.7 |
| db1c31ff-53a1-3baf-b72d-9bf3132d9642 | -6.5192 | -45.5915 | 2025-08-07 12:50:00 | GOES-19 | MIRADOR | MARANHÃO | Brasil | 2106706 | 21 | 33 | nan | nan | nan | Cerrado | 92.6 |
| 9c544ee4-21a7-3a27-a808-c4d7b7eaabd3 | -10.625 | -44.7439 | 2025-08-07 13:00:00 | GOES-19 | SEBASTIÃO BARROS | PIAUÍ | Brasil | 2210623 | 22 | 33 | nan | nan | nan | Cerrado | 108.8 |
| 5ad5bba9-fd5b-309e-bff2-6f83e72a0779 | -6.5194 | -45.569 | 2025-08-07 13:00:00 | GOES-19 | MIRADOR | MARANHÃO | Brasil | 2106706 | 21 | 33 | nan | nan | nan | Cerrado | 92.2 |
| a0ca4a0d-64e0-3da7-b9c9-bfbf272a19a6 | -8.4897 | -45.7053 | 2025-08-07 13:00:00 | GOES-19 | SANTA FILOMENA | PIAUÍ | Brasil | 2209203 | 22 | 33 | nan | nan | nan | Cerrado | 92.5 |
| b2a4c30d-3fd4-3fc8-b41d-98f4907c9040 | -6.5192 | -45.5915 | 2025-08-07 13:00:00 | GOES-19 | MIRADOR | MARANHÃO | Brasil | 2106706 | 21 | 33 | nan | nan | nan | Cerrado | 195.2 |
| 846c2fd2-aadb-30e5-9d29-641dca3ce02e | -10.6441 | -44.7413 | 2025-08-07 13:00:00 | GOES-19 | SEBASTIÃO BARROS | PIAUÍ | Brasil | 2210623 | 22 | 33 | nan | nan | nan | Cerrado | 160.8 |
| 2c9ebcb1-5657-3cca-89a4-945eff896553 | -7.3012 | -39.6453 | 2025-08-07 13:00:00 | GOES-19 | SANTANA DO CARIRI | CEARÁ | Brasil | 2312106 | 23 | 33 | nan | nan | nan | Caatinga | 122.3 |
| cf98c90e-d422-3019-a8df-6865666ed882 | -10.6438 | -44.7645 | 2025-08-07 13:00:00 | GOES-19 | SEBASTIÃO BARROS | PIAUÍ | Brasil | 2210623 | 22 | 33 | nan | nan | nan | Cerrado | 88.7 |
| 9045fafc-8dc0-307b-8f93-111692333001 | -5.9247 | -45.1398 | 2025-08-07 13:10:00 | GOES-19 | FERNANDO FALCÃO | MARANHÃO | Brasil | 2104081 | 21 | 33 | nan | nan | nan | Cerrado | 150.6 |
| 01e8af69-f803-3841-abd2-8e1c46176fa1 | -7.3012 | -39.6453 | 2025-08-07 13:10:00 | GOES-19 | SANTANA DO CARIRI | CEARÁ | Brasil | 2312106 | 23 | 33 | nan | nan | nan | Caatinga | 135.8 |
| 60e9d329-2ae7-30eb-b196-44696afbd58d | -10.625 | -44.7439 | 2025-08-07 13:10:00 | GOES-19 | SEBASTIÃO BARROS | PIAUÍ | Brasil | 2210623 | 22 | 33 | nan | nan | nan | Cerrado | 96.8 |
| 90ce091c-b2f5-3596-92c4-205cc82e5c5d | -7.2417 | -44.6438 | 2025-08-07 13:10:00 | GOES-19 | BENEDITO LEITE | MARANHÃO | Brasil | 2101806 | 21 | 33 | nan | nan | nan | Cerrado | 73.5 |
| f2821ed3-1804-3ad4-aecf-fcc9f676965d | -6.5192 | -45.5915 | 2025-08-07 13:10:00 | GOES-19 | MIRADOR | MARANHÃO | Brasil | 2106706 | 21 | 33 | nan | nan | nan | Cerrado | 111.4 |
| 93427c4b-8279-3300-b5fc-55cc4ce8266d | -8.9213 | -60.7489 | 2025-08-07 13:10:00 | GOES-19 | COLNIZA | MATO GROSSO | Brasil | 5103254 | 51 | 33 | nan | nan | nan | Amazônia | 71.7 |
| 42d8cb41-5171-3bba-8896-8256072392b5 | -10.6441 | -44.7413 | 2025-08-07 13:10:00 | GOES-19 | SEBASTIÃO BARROS | PIAUÍ | Brasil | 2210623 | 22 | 33 | nan | nan | nan | Cerrado | 216.2 |
| fb1c36f8-8b2c-34ba-8a8f-bebf33f082ed | -7.7396 | -45.4854 | 2025-08-07 13:10:00 | GOES-19 | SAMBAÍBA | MARANHÃO | Brasil | 2109700 | 21 | 33 | nan | nan | nan | Cerrado | 117.7 |
| 2795224f-3599-3543-90b8-2f35bdbc4edd | -12.5522 | -47.1612 | 2025-08-07 13:10:00 | GOES-19 | ARRAIAS | TOCANTINS | Brasil | 1702406 | 17 | 33 | nan | nan | nan | Cerrado | 69.6 |
| c00b1967-16fe-35b8-8d3f-dfe245b4591e | -12.3816 | -47.0508 | 2025-08-07 13:10:00 | GOES-19 | ARRAIAS | TOCANTINS | Brasil | 1702406 | 17 | 33 | nan | nan | nan | Cerrado | 79.1 |
| 0a149fd5-9a52-31b7-80e9-44710dcad74e | -12.4263 | -47.7823 | 2025-08-07 13:10:00 | GOES-19 | PARANÃ | TOCANTINS | Brasil | 1716208 | 17 | 33 | nan | nan | nan | Cerrado | 66.1 |
| 47402e27-5084-380e-9a3e-361978896652 | -10.6438 | -44.7645 | 2025-08-07 13:10:00 | GOES-19 | SEBASTIÃO BARROS | PIAUÍ | Brasil | 2210623 | 22 | 33 | nan | nan | nan | Cerrado | 109.1 |
| e8c62381-7795-3160-ae2d-fd38789bc518 | -7.3012 | -39.6453 | 2025-08-07 13:20:00 | GOES-19 | SANTANA DO CARIRI | CEARÁ | Brasil | 2312106 | 23 | 33 | nan | nan | nan | Caatinga | 90.9 |
| ec837f3b-df51-32dd-b1b0-4e808a78f5c8 | -6.2604 | -45.2504 | 2025-08-07 13:20:00 | GOES-19 | FERNANDO FALCÃO | MARANHÃO | Brasil | 2104081 | 21 | 33 | nan | nan | nan | Cerrado | 90.3 |
| b0c96225-6a0e-3ff8-818d-8bfc68fe8c57 | -10.6049 | -52.7952 | 2025-08-07 13:20:00 | GOES-19 | SÃO JOSÉ DO XINGU | MATO GROSSO | Brasil | 5107354 | 51 | 33 | nan | nan | nan | Amazônia | 80.0 |
| 5966ee65-e63e-3c68-9387-89e5a07b162c | -10.6441 | -44.7413 | 2025-08-07 13:20:00 | GOES-19 | SEBASTIÃO BARROS | PIAUÍ | Brasil | 2210623 | 22 | 33 | nan | nan | nan | Cerrado | 146.8 |
| 3645d46e-9009-3ba4-810d-f0d4aced1cd9 | -8.4709 | -45.7072 | 2025-08-07 13:20:00 | GOES-19 | SANTA FILOMENA | PIAUÍ | Brasil | 2209203 | 22 | 33 | nan | nan | nan | Cerrado | 79.1 |
| dd21e717-20b4-37db-b38a-32d452f2d4f4 | -8.9213 | -60.7489 | 2025-08-07 13:20:00 | GOES-19 | COLNIZA | MATO GROSSO | Brasil | 5103254 | 51 | 33 | nan | nan | nan | Amazônia | 59.7 |
| 095d8532-c3d7-3c86-b0e8-ac64e555acd2 | -12.3816 | -47.0508 | 2025-08-07 13:20:00 | GOES-19 | ARRAIAS | TOCANTINS | Brasil | 1702406 | 17 | 33 | nan | nan | nan | Cerrado | 77.3 |
| 47937772-11ce-356d-86f4-32ce1311203c | -6.2602 | -45.2731 | 2025-08-07 13:20:00 | GOES-19 | FERNANDO FALCÃO | MARANHÃO | Brasil | 2104081 | 21 | 33 | nan | nan | nan | Cerrado | 71.4 |
| 388172b8-ad8c-3861-a93e-21a9bc8c6a06 | -12.5522 | -47.1612 | 2025-08-07 13:20:00 | GOES-19 | ARRAIAS | TOCANTINS | Brasil | 1702406 | 17 | 33 | nan | nan | nan | Cerrado | 86.5 |
| f6c4f32c-3f59-3ccf-9237-c61e8522cc60 | -8.4897 | -45.7053 | 2025-08-07 13:20:00 | GOES-19 | SANTA FILOMENA | PIAUÍ | Brasil | 2209203 | 22 | 33 | nan | nan | nan | Cerrado | 105.0 |
| 1d053801-3206-323b-ad55-8987051ea21b | -10.6441 | -44.7413 | 2025-08-07 13:30:00 | GOES-19 | SEBASTIÃO BARROS | PIAUÍ | Brasil | 2210623 | 22 | 33 | nan | nan | nan | Cerrado | 211.5 |
| 9de9fea0-af60-361d-a8a4-ee8e7d93daa0 | -7.8948 | -45.0843 | 2025-08-07 13:30:00 | GOES-19 | BAIXA GRANDE DO RIBEIRO | PIAUÍ | Brasil | 2201150 | 22 | 33 | nan | nan | nan | Cerrado | 73.1 |
| 0af99775-edc5-3b70-b0cd-1cbe4fec849a | -8.9213 | -60.7489 | 2025-08-07 13:30:00 | GOES-19 | COLNIZA | MATO GROSSO | Brasil | 5103254 | 51 | 33 | nan | nan | nan | Amazônia | 78.1 |
| 515d12c7-8e85-3282-9f18-38f743f56682 | -8.9215 | -60.7297 | 2025-08-07 13:30:00 | GOES-19 | COLNIZA | MATO GROSSO | Brasil | 5103254 | 51 | 33 | nan | nan | nan | Amazônia | 62.3 |
| d844a773-1a60-32b8-8a46-e511894d424d | -6.2789 | -45.2716 | 2025-08-07 13:30:00 | GOES-19 | FERNANDO FALCÃO | MARANHÃO | Brasil | 2104081 | 21 | 33 | nan | nan | nan | Cerrado | 111.7 |
| 5b73aa90-f5f2-3930-903b-dbd44536a913 | -6.8002 | -43.7848 | 2025-08-07 13:30:00 | GOES-19 | GUADALUPE | PIAUÍ | Brasil | 2204501 | 22 | 33 | nan | nan | nan | Cerrado | 75.5 |
| 1ff00d69-080d-3394-8a94-2c7321a883e3 | -12.5526 | -47.1387 | 2025-08-07 13:30:00 | GOES-19 | ARRAIAS | TOCANTINS | Brasil | 1702406 | 17 | 33 | nan | nan | nan | Cerrado | 99.5 |
| d3451d52-d150-3114-ae25-43d497db6b56 | -12.4071 | -47.7849 | 2025-08-07 13:30:00 | GOES-19 | PARANÃ | TOCANTINS | Brasil | 1716208 | 17 | 33 | nan | nan | nan | Cerrado | 68.9 |
| 9df7305c-7dd1-38e2-b899-53fca5f0865f | -6.2792 | -45.249 | 2025-08-07 13:30:00 | GOES-19 | FERNANDO FALCÃO | MARANHÃO | Brasil | 2104081 | 21 | 33 | nan | nan | nan | Cerrado | 107.0 |
| c7d12cf7-1f49-3a84-9eb2-d51f67a4bfe0 | -10.6049 | -52.7952 | 2025-08-07 13:30:00 | GOES-19 | SÃO JOSÉ DO XINGU | MATO GROSSO | Brasil | 5107354 | 51 | 33 | nan | nan | nan | Amazônia | 73.1 |
| a26155e0-eb88-3be3-bc1b-ab98068cec6b | -6.2604 | -45.2504 | 2025-08-07 13:30:00 | GOES-19 | FERNANDO FALCÃO | MARANHÃO | Brasil | 2104081 | 21 | 33 | nan | nan | nan | Cerrado | 97.8 |
| 800ae190-6ce8-3247-81fb-0c9c20b1598f | -7.2417 | -44.6438 | 2025-08-07 13:30:00 | GOES-19 | BENEDITO LEITE | MARANHÃO | Brasil | 2101806 | 21 | 33 | nan | nan | nan | Cerrado | 81.5 |
| e824d1e2-3389-3bda-9771-4dfd732d0cae | -12.5522 | -47.1612 | 2025-08-07 13:30:00 | GOES-19 | ARRAIAS | TOCANTINS | Brasil | 1702406 | 17 | 33 | nan | nan | nan | Cerrado | 164.3 |
| 2d4012f9-5bd8-3aeb-bf9c-5460f047c220 | -10.625 | -44.7439 | 2025-08-07 13:30:00 | GOES-19 | SEBASTIÃO BARROS | PIAUÍ | Brasil | 2210623 | 22 | 33 | nan | nan | nan | Cerrado | 148.5 |
| f582e9de-a5fd-3ec2-b29f-29f35219cd32 | -10.6438 | -44.7645 | 2025-08-07 13:30:00 | GOES-19 | SEBASTIÃO BARROS | PIAUÍ | Brasil | 2210623 | 22 | 33 | nan | nan | nan | Cerrado | 83.9 |
| a6152cf9-6e46-31f5-867f-c0334b458189 | -6.2602 | -45.2731 | 2025-08-07 13:30:00 | GOES-19 | FERNANDO FALCÃO | MARANHÃO | Brasil | 2104081 | 21 | 33 | nan | nan | nan | Cerrado | 95.0 |
| c91a35d6-ed59-3d72-ba0d-20f201cae37f | -8.4897 | -45.7053 | 2025-08-07 13:40:00 | GOES-19 | SANTA FILOMENA | PIAUÍ | Brasil | 2209203 | 22 | 33 | nan | nan | nan | Cerrado | 77.2 |
| c2923582-49d3-33ef-97f3-51df1f90c44a | -8.4709 | -45.7072 | 2025-08-07 13:40:00 | GOES-19 | SANTA FILOMENA | PIAUÍ | Brasil | 2209203 | 22 | 33 | nan | nan | nan | Cerrado | 80.7 |
| 7ff553a1-7830-35cc-a564-6fef960443d5 | -12.4071 | -47.7849 | 2025-08-07 13:40:00 | GOES-19 | PARANÃ | TOCANTINS | Brasil | 1716208 | 17 | 33 | nan | nan | nan | Cerrado | 75.9 |
| 82f063f6-bfdf-3105-8d24-812ef0cb75c5 | -2.9554 | -42.3529 | 2025-08-07 13:40:00 | GOES-19 | TUTÓIA | MARANHÃO | Brasil | 2112506 | 21 | 33 | nan | nan | nan | Cerrado | 102.5 |
| 4b15ba38-9593-329c-96df-b4eb42f1f409 | -8.9213 | -60.7489 | 2025-08-07 13:40:00 | GOES-19 | COLNIZA | MATO GROSSO | Brasil | 5103254 | 51 | 33 | nan | nan | nan | Amazônia | 92.1 |
| 112add7a-6ff5-373a-aa43-33c1fecfb316 | -5.678 | -41.3987 | 2025-08-07 13:40:00 | GOES-19 | SÃO MIGUEL DO TAPUIO | PIAUÍ | Brasil | 2210409 | 22 | 33 | nan | nan | nan | Caatinga | 110.5 |
| 4e9f105b-a080-39dc-bb1e-0214b04655eb | -10.6438 | -44.7645 | 2025-08-07 13:40:00 | GOES-19 | SEBASTIÃO BARROS | PIAUÍ | Brasil | 2210623 | 22 | 33 | nan | nan | nan | Cerrado | 89.8 |
| 2276fc5b-ebb6-3635-b95c-9e123b3dd9fb | -14.5535 | -45.5844 | 2025-08-07 13:40:00 | GOES-19 | COCOS | BAHIA | Brasil | 2908101 | 29 | 33 | nan | nan | nan | Cerrado | 85.1 |
| 9baed157-473f-38c8-985c-399096fd5f8c | -10.6441 | -44.7413 | 2025-08-07 13:40:00 | GOES-19 | SEBASTIÃO BARROS | PIAUÍ | Brasil | 2210623 | 22 | 33 | nan | nan | nan | Cerrado | 206.8 |
| 706b025d-8bf3-36ef-b5fe-9aba7ad45a00 | -8.9215 | -60.7297 | 2025-08-07 13:40:00 | GOES-19 | COLNIZA | MATO GROSSO | Brasil | 5103254 | 51 | 33 | nan | nan | nan | Amazônia | 79.1 |
| 70382813-f16b-32f3-b1f7-e7f6e4b046e6 | -12.5522 | -47.1612 | 2025-08-07 13:40:00 | GOES-19 | ARRAIAS | TOCANTINS | Brasil | 1702406 | 17 | 33 | nan | nan | nan | Cerrado | 84.0 |
| b2a5e8b1-355d-3b4b-a227-265d7b961b18 | -6.8002 | -43.7848 | 2025-08-07 13:40:00 | GOES-19 | GUADALUPE | PIAUÍ | Brasil | 2204501 | 22 | 33 | nan | nan | nan | Cerrado | 78.6 |
| 687ef323-c262-3380-a9ec-336d33ffcabf | -10.625 | -44.7439 | 2025-08-07 13:40:00 | GOES-19 | SEBASTIÃO BARROS | PIAUÍ | Brasil | 2210623 | 22 | 33 | nan | nan | nan | Cerrado | 101.4 |
| 626ae4a3-7205-3d4d-89ec-e9ac0de6d763 | -12.4071 | -47.7849 | 2025-08-07 13:50:00 | GOES-19 | PARANÃ | TOCANTINS | Brasil | 1716208 | 17 | 33 | nan | nan | nan | Cerrado | 68.2 |
| 72401fad-c8b9-3db3-9954-87f89c3df182 | -12.5522 | -47.1612 | 2025-08-07 13:50:00 | GOES-19 | ARRAIAS | TOCANTINS | Brasil | 1702406 | 17 | 33 | nan | nan | nan | Cerrado | 103.7 |
| b771c622-bbfc-3035-a31e-1c40f1c7f308 | -8.9215 | -60.7297 | 2025-08-07 13:50:00 | GOES-19 | COLNIZA | MATO GROSSO | Brasil | 5103254 | 51 | 33 | nan | nan | nan | Amazônia | 65.2 |
| c95bbb1d-abd4-3538-9f6e-6f8725cd85de | -8.4712 | -45.6846 | 2025-08-07 13:50:00 | GOES-19 | SANTA FILOMENA | PIAUÍ | Brasil | 2209203 | 22 | 33 | nan | nan | nan | Cerrado | 93.3 |
| d9b2b37e-d436-3aa9-b7cf-c8b114988f57 | -6.2789 | -45.2716 | 2025-08-07 13:50:00 | GOES-19 | FERNANDO FALCÃO | MARANHÃO | Brasil | 2104081 | 21 | 33 | nan | nan | nan | Cerrado | 124.3 |
| 0436dda9-eec8-3e4f-b7da-7b71083ea162 | -8.49 | -45.6826 | 2025-08-07 13:50:00 | GOES-19 | SANTA FILOMENA | PIAUÍ | Brasil | 2209203 | 22 | 33 | nan | nan | nan | Cerrado | 67.6 |
| a21b6501-727c-327c-aa0f-f5635e98f5bc | -10.6445 | -44.7182 | 2025-08-07 13:50:00 | GOES-19 | PARNAGUÁ | PIAUÍ | Brasil | 2207603 | 22 | 33 | nan | nan | nan | Cerrado | 84.1 |
| 39987cce-faf9-375c-bc69-ba83fdf25161 | -6.2602 | -45.2731 | 2025-08-07 13:50:00 | GOES-19 | FERNANDO FALCÃO | MARANHÃO | Brasil | 2104081 | 21 | 33 | nan | nan | nan | Cerrado | 93.9 |
| c1695515-16f8-325c-8293-0f65e6f8c057 | -8.9213 | -60.7489 | 2025-08-07 13:50:00 | GOES-19 | COLNIZA | MATO GROSSO | Brasil | 5103254 | 51 | 33 | nan | nan | nan | Amazônia | 84.4 |
| 23e6e176-e9f0-3436-8e62-8f7c683969bc | -5.678 | -41.3987 | 2025-08-07 13:50:00 | GOES-19 | SÃO MIGUEL DO TAPUIO | PIAUÍ | Brasil | 2210409 | 22 | 33 | nan | nan | nan | Caatinga | 93.8 |
| 07269f89-bdd3-32ee-a646-1536778e105d | -10.6438 | -44.7645 | 2025-08-07 13:50:00 | GOES-19 | SEBASTIÃO BARROS | PIAUÍ | Brasil | 2210623 | 22 | 33 | nan | nan | nan | Cerrado | 114.3 |
| 40744163-c122-33a6-8f5f-a0d095df3cdd | -2.9554 | -42.3529 | 2025-08-07 13:50:00 | GOES-19 | TUTÓIA | MARANHÃO | Brasil | 2112506 | 21 | 33 | nan | nan | nan | Cerrado | 88.1 |
| 7d897649-3362-31a2-9514-2916c24fbadc | -7.3012 | -39.6453 | 2025-08-07 13:50:00 | GOES-19 | SANTANA DO CARIRI | CEARÁ | Brasil | 2312106 | 23 | 33 | nan | nan | nan | Caatinga | 90.6 |
| 1850d53e-2330-3848-a106-a4fc1fa603a0 | -12.5526 | -47.1387 | 2025-08-07 13:50:00 | GOES-19 | ARRAIAS | TOCANTINS | Brasil | 1702406 | 17 | 33 | nan | nan | nan | Cerrado | 76.1 |
| 8501d581-a075-3dc8-b12a-7315bce4e452 | -10.625 | -44.7439 | 2025-08-07 13:50:00 | GOES-19 | SEBASTIÃO BARROS | PIAUÍ | Brasil | 2210623 | 22 | 33 | nan | nan | nan | Cerrado | 205.8 |


[Clique aqui para ver as próximas entradas](README30.md)
