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

## Dados Diários - Página 37

| ID | Latitude | Longitude | Data/Hora GMT | Satélite | Município | Estado | País | Município ID | Estado ID | País ID | Dias sem Chuva | Precipitação | Risco de Fogo | Bioma | FRP |
|----|----------|-----------|---------------|----------|-----------|--------|------|--------------|-----------|---------|----------------|--------------|----------------|-------|-----|
| 9a1e755a-1254-3377-90fe-e675a909c0ed | 1.1504 | -50.9357 | 2025-10-13 14:00:00 | GOES-19 | TARTARUGALZINHO | AMAPÁ | Brasil | 1600709 | 16 | 33 | nan | nan | nan | Amazônia | 88.8 |
| d5f81fd3-0898-33a6-b216-b400a2ecb796 | -12.238 | -51.1545 | 2025-10-13 14:00:00 | GOES-19 | NOVO SANTO ANTÔNIO | MATO GROSSO | Brasil | 5106315 | 51 | 33 | nan | nan | nan | Cerrado | 78.5 |
| 028c609d-3889-3ec8-a404-b276b670cae8 | 1.9134 | -55.7221 | 2025-10-13 14:00:00 | GOES-19 | ÓBIDOS | PARÁ | Brasil | 1505106 | 15 | 33 | nan | nan | nan | Amazônia | 89.4 |
| 36da18ed-3e8d-3d83-a5ce-82bcb95f7c3c | 1.9134 | -55.7024 | 2025-10-13 14:00:00 | GOES-19 | ÓBIDOS | PARÁ | Brasil | 1505106 | 15 | 33 | nan | nan | nan | Amazônia | 85.1 |
| a1ad2966-da1c-31ba-bec5-e2720f041ea1 | 1.8033 | -55.8026 | 2025-10-13 14:00:00 | GOES-19 | ÓBIDOS | PARÁ | Brasil | 1505106 | 15 | 33 | nan | nan | nan | Amazônia | 59.6 |
| 2596383e-daae-3eaf-ae81-d702a6caaf41 | 1.7851 | -55.7831 | 2025-10-13 14:00:00 | GOES-19 | ÓBIDOS | PARÁ | Brasil | 1505106 | 15 | 33 | nan | nan | nan | Amazônia | 84.3 |
| 5ff0f037-8385-306c-9d9c-f2ea7217266b | -12.6762 | -51.1878 | 2025-10-13 14:00:00 | GOES-19 | RIBEIRÃO CASCALHEIRA | MATO GROSSO | Brasil | 5107180 | 51 | 33 | nan | nan | nan | Cerrado | 95.0 |
| bc0299f5-afbe-32cc-a1ee-99d5c587f093 | 1.9135 | -55.6826 | 2025-10-13 14:00:00 | GOES-19 | ÓBIDOS | PARÁ | Brasil | 1505106 | 15 | 33 | nan | nan | nan | Amazônia | 129.4 |
| 0b34d26f-1730-307a-a0ba-4ef3cd3fd29a | -12.6954 | -51.1855 | 2025-10-13 14:00:00 | GOES-19 | RIBEIRÃO CASCALHEIRA | MATO GROSSO | Brasil | 5107180 | 51 | 33 | nan | nan | nan | Cerrado | 102.4 |
| 88c37885-9576-39b4-8d48-30d5415f4237 | -12.2383 | -51.1332 | 2025-10-13 14:00:00 | GOES-19 | NOVO SANTO ANTÔNIO | MATO GROSSO | Brasil | 5106315 | 51 | 33 | nan | nan | nan | Cerrado | 92.2 |
| 7f443462-e758-3d0e-9b77-856ed71243c7 | 1.785 | -55.8028 | 2025-10-13 14:00:00 | GOES-19 | ÓBIDOS | PARÁ | Brasil | 1505106 | 15 | 33 | nan | nan | nan | Amazônia | 77.3 |
| 438eb65e-04e2-3688-b560-dabc43050370 | 1.9135 | -55.6629 | 2025-10-13 14:00:00 | GOES-19 | ÓBIDOS | PARÁ | Brasil | 1505106 | 15 | 33 | nan | nan | nan | Amazônia | 71.8 |
| e34d14a0-9bc1-3177-b1c0-c9359cc63b08 | -19.0519 | -57.5356 | 2025-10-13 14:00:00 | GOES-19 | LADÁRIO | MATO GROSSO DO SUL | Brasil | 5005202 | 50 | 33 | nan | nan | nan | Pantanal | 113.8 |
| 54f4ab93-950e-3b1a-93db-fb0a89be6c6e | -12.7798 | -50.6834 | 2025-10-13 14:00:00 | GOES-19 | COCALINHO | MATO GROSSO | Brasil | 5103106 | 51 | 33 | nan | nan | nan | Cerrado | 79.2 |
| a42249f4-ea33-3d4a-a500-b8424486e1ed | -12.7798 | -50.6834 | 2025-10-13 14:10:00 | GOES-19 | COCALINHO | MATO GROSSO | Brasil | 5103106 | 51 | 33 | nan | nan | nan | Cerrado | 122.2 |
| cf6b02cd-a059-3055-8426-92b0599fc5e7 | -12.6766 | -51.1665 | 2025-10-13 14:10:00 | GOES-19 | RIBEIRÃO CASCALHEIRA | MATO GROSSO | Brasil | 5107180 | 51 | 33 | nan | nan | nan | Cerrado | 81.5 |
| 2c19a105-74be-323b-b9f9-7b1750b541fb | -19.0519 | -57.5356 | 2025-10-13 14:10:00 | GOES-19 | LADÁRIO | MATO GROSSO DO SUL | Brasil | 5005202 | 50 | 33 | nan | nan | nan | Pantanal | 119.6 |
| 3a6b10d6-df9c-3eb7-85d0-4becdbd2886d | -19.0319 | -57.5382 | 2025-10-13 14:10:00 | GOES-19 | LADÁRIO | MATO GROSSO DO SUL | Brasil | 5005202 | 50 | 33 | nan | nan | nan | Pantanal | 113.5 |
| 9be2c8a6-72bc-3390-bf89-15aab662be1d | 1.8033 | -55.8026 | 2025-10-13 14:10:00 | GOES-19 | ÓBIDOS | PARÁ | Brasil | 1505106 | 15 | 33 | nan | nan | nan | Amazônia | 59.4 |
| 63d5825d-b6e8-3e71-bfae-809854b75af3 | -12.6762 | -51.1878 | 2025-10-13 14:10:00 | GOES-19 | RIBEIRÃO CASCALHEIRA | MATO GROSSO | Brasil | 5107180 | 51 | 33 | nan | nan | nan | Cerrado | 85.4 |
| 05793d65-3bae-3e13-9a89-c2c8ee29a523 | -12.7606 | -50.6857 | 2025-10-13 14:10:00 | GOES-19 | COCALINHO | MATO GROSSO | Brasil | 5103106 | 51 | 33 | nan | nan | nan | Cerrado | 74.0 |
| b8bfb1a5-df35-323e-92bc-17d66d386c5c | -12.6954 | -51.1855 | 2025-10-13 14:10:00 | GOES-19 | RIBEIRÃO CASCALHEIRA | MATO GROSSO | Brasil | 5107180 | 51 | 33 | nan | nan | nan | Cerrado | 99.4 |
| 8e3f6c55-0b73-366d-9d58-9503b375116f | 1.785 | -55.8028 | 2025-10-13 14:10:00 | GOES-19 | ÓBIDOS | PARÁ | Brasil | 1505106 | 15 | 33 | nan | nan | nan | Amazônia | 68.3 |
| 22cba4e9-5901-3908-a55b-5a0e81c43bce | 1.9135 | -55.6629 | 2025-10-13 14:10:00 | GOES-19 | ÓBIDOS | PARÁ | Brasil | 1505106 | 15 | 33 | nan | nan | nan | Amazônia | 74.9 |
| 0cec3cb1-7e6d-3725-9035-d9dbb12451ce | 1.7851 | -55.7831 | 2025-10-13 14:10:00 | GOES-19 | ÓBIDOS | PARÁ | Brasil | 1505106 | 15 | 33 | nan | nan | nan | Amazônia | 70.3 |
| 2339ba09-82d6-371a-8356-fcffa4a1f859 | -12.2383 | -51.1332 | 2025-10-13 14:10:00 | GOES-19 | NOVO SANTO ANTÔNIO | MATO GROSSO | Brasil | 5106315 | 51 | 33 | nan | nan | nan | Cerrado | 94.7 |
| 1b9ab349-f47a-3369-9a73-f467b15d794f | -12.238 | -51.1545 | 2025-10-13 14:10:00 | GOES-19 | NOVO SANTO ANTÔNIO | MATO GROSSO | Brasil | 5106315 | 51 | 33 | nan | nan | nan | Cerrado | 80.3 |
| c815526d-63af-3063-8900-78415984b664 | -12.6957 | -51.1641 | 2025-10-13 14:10:00 | GOES-19 | RIBEIRÃO CASCALHEIRA | MATO GROSSO | Brasil | 5107180 | 51 | 33 | nan | nan | nan | Cerrado | 86.3 |
| ec05713e-5e52-30e2-a1f6-f8984b4fff7b | 1.9135 | -55.6826 | 2025-10-13 14:10:00 | GOES-19 | ÓBIDOS | PARÁ | Brasil | 1505106 | 15 | 33 | nan | nan | nan | Amazônia | 93.8 |
| cd43154f-24f4-3cd3-823b-c247b9664d59 | -8.5419 | -44.5824 | 2025-10-13 14:10:00 | GOES-19 | PALMEIRA DO PIAUÍ | PIAUÍ | Brasil | 2207405 | 22 | 33 | nan | nan | nan | Cerrado | 86.5 |
| 682821ef-a8d5-3261-b98e-8c8b7847866f | -4.6883 | -43.1314 | 2025-10-13 14:10:00 | GOES-19 | CAXIAS | MARANHÃO | Brasil | 2103000 | 21 | 33 | nan | nan | nan | Cerrado | 588.6 |
| c74575de-3bf0-360f-9bd5-c74795457fb5 | 1.895 | -55.7421 | 2025-10-13 14:20:00 | GOES-19 | ÓBIDOS | PARÁ | Brasil | 1505106 | 15 | 33 | nan | nan | nan | Amazônia | 81.5 |
| d0cd001b-a77d-3b2c-81d8-060260292f80 | 1.7851 | -55.7831 | 2025-10-13 14:20:00 | GOES-19 | ÓBIDOS | PARÁ | Brasil | 1505106 | 15 | 33 | nan | nan | nan | Amazônia | 66.0 |
| dcf638c2-dfc0-39c5-9c81-ceaf8e079397 | -5.6057 | -41.0903 | 2025-10-13 14:20:00 | GOES-19 | SÃO MIGUEL DO TAPUIO | PIAUÍ | Brasil | 2210409 | 22 | 33 | nan | nan | nan | Caatinga | 125.0 |
| 9028aac9-4ff9-3378-a0d0-46b8e702ae0c | 1.9134 | -55.7221 | 2025-10-13 14:20:00 | GOES-19 | ÓBIDOS | PARÁ | Brasil | 1505106 | 15 | 33 | nan | nan | nan | Amazônia | 74.7 |
| 1691d25a-441a-31c3-9d9b-329103c5b9a3 | -12.6957 | -51.1641 | 2025-10-13 14:20:00 | GOES-19 | RIBEIRÃO CASCALHEIRA | MATO GROSSO | Brasil | 5107180 | 51 | 33 | nan | nan | nan | Cerrado | 72.1 |
| 704d7f79-9fe9-3f9c-833b-b97816e0d036 | 1.8034 | -55.7829 | 2025-10-13 14:20:00 | GOES-19 | ÓBIDOS | PARÁ | Brasil | 1505106 | 15 | 33 | nan | nan | nan | Amazônia | 66.7 |
| 6e5dbddb-8d7e-3406-a537-a7381df89a1c | 1.8033 | -55.8026 | 2025-10-13 14:20:00 | GOES-19 | ÓBIDOS | PARÁ | Brasil | 1505106 | 15 | 33 | nan | nan | nan | Amazônia | 68.8 |
| 009fdd2a-4e46-345c-b0b6-9f747a91f475 | 1.9135 | -55.6826 | 2025-10-13 14:20:00 | GOES-19 | ÓBIDOS | PARÁ | Brasil | 1505106 | 15 | 33 | nan | nan | nan | Amazônia | 145.2 |
| 05618364-4c65-35d2-9172-69205812209e | 1.9135 | -55.6629 | 2025-10-13 14:20:00 | GOES-19 | ÓBIDOS | PARÁ | Brasil | 1505106 | 15 | 33 | nan | nan | nan | Amazônia | 81.4 |
| 4926d149-21e3-34c9-80ed-2eee8b7c0e58 | -6.2218 | -41.5688 | 2025-10-13 14:20:00 | GOES-19 | PIMENTEIRAS | PIAUÍ | Brasil | 2208106 | 22 | 33 | nan | nan | nan | Caatinga | 106.9 |
| afc14450-efcd-33b7-8498-0d38e5c066a2 | 1.8582 | -55.8413 | 2025-10-13 14:20:00 | GOES-19 | ORIXIMINÁ | PARÁ | Brasil | 1505304 | 15 | 33 | nan | nan | nan | Amazônia | 69.0 |
| ca849af9-d07d-3209-b8c7-a4601412ebe4 | -12.238 | -51.1545 | 2025-10-13 14:20:00 | GOES-19 | NOVO SANTO ANTÔNIO | MATO GROSSO | Brasil | 5106315 | 51 | 33 | nan | nan | nan | Cerrado | 79.5 |
| 3adfb5d9-fb0c-304d-894b-9e3c6b97a459 | -8.4034 | -45.0783 | 2025-10-13 14:20:00 | GOES-19 | BAIXA GRANDE DO RIBEIRO | PIAUÍ | Brasil | 2201150 | 22 | 33 | nan | nan | nan | Cerrado | 138.3 |
| 52bed4a2-6ffc-30e4-84b3-b5b4a4d0b91f | -8.4037 | -45.0555 | 2025-10-13 14:20:00 | GOES-19 | BAIXA GRANDE DO RIBEIRO | PIAUÍ | Brasil | 2201150 | 22 | 33 | nan | nan | nan | Cerrado | 175.4 |
| f7163dc2-84b7-3d0c-bb9e-890d82ca10bf | -12.2383 | -51.1332 | 2025-10-13 14:20:00 | GOES-19 | NOVO SANTO ANTÔNIO | MATO GROSSO | Brasil | 5106315 | 51 | 33 | nan | nan | nan | Cerrado | 94.7 |
| daba71ba-040d-3dc2-974c-b2f997b893bd | 1.9135 | -55.6826 | 2025-10-13 14:30:00 | GOES-19 | ÓBIDOS | PARÁ | Brasil | 1505106 | 15 | 33 | nan | nan | nan | Amazônia | 149.1 |
| 5285a2a4-1b08-3b6f-832a-4383bee24f04 | -5.5867 | -41.1161 | 2025-10-13 14:30:00 | GOES-19 | SÃO MIGUEL DO TAPUIO | PIAUÍ | Brasil | 2210409 | 22 | 33 | nan | nan | nan | Caatinga | 132.2 |
| 0741b50a-4241-33d9-b3ed-ccdf2ef0f1f6 | -12.7798 | -50.6834 | 2025-10-13 14:30:00 | GOES-19 | COCALINHO | MATO GROSSO | Brasil | 5103106 | 51 | 33 | nan | nan | nan | Cerrado | 97.6 |
| 2aaa3cdd-24a0-396b-8922-d6b19d2bbdd9 | -8.5419 | -44.5824 | 2025-10-13 14:30:00 | GOES-19 | PALMEIRA DO PIAUÍ | PIAUÍ | Brasil | 2207405 | 22 | 33 | nan | nan | nan | Cerrado | 102.5 |
| 918b10ae-cc99-34ce-a761-42ab67116fe0 | -12.6957 | -51.1641 | 2025-10-13 14:30:00 | GOES-19 | RIBEIRÃO CASCALHEIRA | MATO GROSSO | Brasil | 5107180 | 51 | 33 | nan | nan | nan | Cerrado | 80.0 |
| e3d8c2d6-9e67-3a91-b02f-76a01d0b4817 | -6.4451 | -41.8128 | 2025-10-13 14:30:00 | GOES-19 | VALENÇA DO PIAUÍ | PIAUÍ | Brasil | 2211308 | 22 | 33 | nan | nan | nan | Caatinga | 191.5 |
| 7d62f7b8-4697-37ea-9b18-3cb955fd065c | -12.2383 | -51.1332 | 2025-10-13 14:30:00 | GOES-19 | NOVO SANTO ANTÔNIO | MATO GROSSO | Brasil | 5106315 | 51 | 33 | nan | nan | nan | Cerrado | 89.2 |
| 6e675809-11cb-3c3f-b93a-68d6fa6839e8 | 1.7851 | -55.7831 | 2025-10-13 14:30:00 | GOES-19 | ÓBIDOS | PARÁ | Brasil | 1505106 | 15 | 33 | nan | nan | nan | Amazônia | 70.0 |
| f75b5452-c458-38f5-a3f3-be9e70ad1987 | -8.4037 | -45.0555 | 2025-10-13 14:30:00 | GOES-19 | BAIXA GRANDE DO RIBEIRO | PIAUÍ | Brasil | 2201150 | 22 | 33 | nan | nan | nan | Cerrado | 200.1 |
| e0c4c8f7-aa42-3c7c-9b66-a57ad7876932 | -7.1567 | -42.1987 | 2025-10-13 14:30:00 | GOES-19 | COLÔNIA DO PIAUÍ | PIAUÍ | Brasil | 2202778 | 22 | 33 | nan | nan | nan | Caatinga | 137.9 |
| aeceadef-3a06-36ed-9dd5-8b057faee367 | 1.9135 | -55.6629 | 2025-10-13 14:30:00 | GOES-19 | ÓBIDOS | PARÁ | Brasil | 1505106 | 15 | 33 | nan | nan | nan | Amazônia | 88.3 |
| b32eda04-9ec7-33b9-a35b-f5350ff25f29 | -6.2218 | -41.5688 | 2025-10-13 14:30:00 | GOES-19 | PIMENTEIRAS | PIAUÍ | Brasil | 2208106 | 22 | 33 | nan | nan | nan | Caatinga | 103.6 |
| 6789ff87-e716-30df-bdfc-2b360fe23781 | -14.0893 | -51.5641 | 2025-10-13 14:40:00 | GOES-19 | COCALINHO | MATO GROSSO | Brasil | 5103106 | 51 | 33 | nan | nan | nan | Cerrado | 85.5 |
| 21e55990-079a-3ce3-800d-387a8d4ddc3c | -3.1433 | -50.2044 | 2025-10-13 14:40:00 | GOES-19 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 306.9 |
| 5c83902f-21ca-3438-93dd-b9d94a3fc5e8 | 1.9135 | -55.6629 | 2025-10-13 14:40:00 | GOES-19 | ÓBIDOS | PARÁ | Brasil | 1505106 | 15 | 33 | nan | nan | nan | Amazônia | 87.5 |
| 50cfbd9c-f3d4-362a-b284-cfd2d1bcbf92 | 1.7851 | -55.7831 | 2025-10-13 14:40:00 | GOES-19 | ÓBIDOS | PARÁ | Brasil | 1505106 | 15 | 33 | nan | nan | nan | Amazônia | 72.7 |
| d0b0591a-931d-3d56-b642-f61d98edc4cb | -8.4034 | -45.0783 | 2025-10-13 14:40:00 | GOES-19 | BAIXA GRANDE DO RIBEIRO | PIAUÍ | Brasil | 2201150 | 22 | 33 | nan | nan | nan | Cerrado | 142.0 |
| e8712caa-e82a-370b-b832-5b43969506ff | 1.9135 | -55.6826 | 2025-10-13 14:40:00 | GOES-19 | ÓBIDOS | PARÁ | Brasil | 1505106 | 15 | 33 | nan | nan | nan | Amazônia | 129.9 |
| 0b89bd5f-7ea4-3547-8294-549e987682c7 | 1.9134 | -55.7221 | 2025-10-13 14:40:00 | GOES-19 | ÓBIDOS | PARÁ | Brasil | 1505106 | 15 | 33 | nan | nan | nan | Amazônia | 70.3 |
| fa0ad4f1-600b-3007-b916-05da717e97c3 | -8.4037 | -45.0555 | 2025-10-13 14:40:00 | GOES-19 | BAIXA GRANDE DO RIBEIRO | PIAUÍ | Brasil | 2201150 | 22 | 33 | nan | nan | nan | Cerrado | 176.7 |
| 127aa218-cacc-3cdc-95ba-a0930d4da850 | -8.5419 | -44.5824 | 2025-10-13 14:40:00 | GOES-19 | PALMEIRA DO PIAUÍ | PIAUÍ | Brasil | 2207405 | 22 | 33 | nan | nan | nan | Cerrado | 93.9 |
| 7ecf7547-01f4-3017-bc40-e60f098011ee | -8.2449 | -44.1991 | 2025-10-13 14:40:00 | GOES-19 | SEBASTIÃO LEAL | PIAUÍ | Brasil | 2210631 | 22 | 33 | nan | nan | nan | Cerrado | 93.9 |


