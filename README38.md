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

## Dados Diários - Página 38

| ID | Latitude | Longitude | Data/Hora GMT | Satélite | Município | Estado | País | Município ID | Estado ID | País ID | Dias sem Chuva | Precipitação | Risco de Fogo | Bioma | FRP |
|----|----------|-----------|---------------|----------|-----------|--------|------|--------------|-----------|---------|----------------|--------------|----------------|-------|-----|
| cb9be706-1c27-350b-8f83-a82cfb421c01 | -3.4522 | -40.4068 | 2025-11-09 13:00:00 | GOES-19 | MASSAPÊ | CEARÁ | Brasil | 2308005 | 23 | 33 | nan | nan | nan | Caatinga | 88.2 |
| fc9d0db7-3a55-3ad9-9e3e-f98b48bce26b | -3.2744 | -42.0785 | 2025-11-09 13:00:00 | GOES-19 | MURICI DOS PORTELAS | PIAUÍ | Brasil | 2206696 | 22 | 33 | nan | nan | nan | Cerrado | 98.5 |
| d628a97a-8f32-32f7-9cbb-3587345702e4 | -19.7826 | -58.0412 | 2025-11-09 13:00:00 | GOES-19 | CORUMBÁ | MATO GROSSO DO SUL | Brasil | 5003207 | 50 | 33 | nan | nan | nan | Pantanal | 102.5 |
| a21fdb59-f463-3032-b3d8-022877d2180b | -19.7822 | -58.062 | 2025-11-09 13:00:00 | GOES-19 | CORUMBÁ | MATO GROSSO DO SUL | Brasil | 5003207 | 50 | 33 | nan | nan | nan | Pantanal | 97.8 |
| 21142d5e-21e5-3d10-9f55-4404840f770d | -19.8023 | -58.0593 | 2025-11-09 13:00:00 | GOES-19 | CORUMBÁ | MATO GROSSO DO SUL | Brasil | 5003207 | 50 | 33 | nan | nan | nan | Pantanal | 99.3 |
| 40ff9611-b296-32eb-a890-3f37bb4f6ebb | -3.3183 | -44.3585 | 2025-11-09 13:00:00 | GOES-19 | ITAPECURU MIRIM | MARANHÃO | Brasil | 2105401 | 21 | 33 | nan | nan | nan | Cerrado | 116.7 |
| 95275a2a-deda-30dd-86dc-0dd5095e339e | -33.30517 | -52.84165 | 2025-11-09 13:03:00 | TERRA_M-T | SANTA VITÓRIA DO PALMAR | RIO GRANDE DO SUL | Brasil | 4317301 | 43 | 33 | nan | nan | nan | Pampa | 38.4 |
| dcc81585-8d89-32ff-80d8-6930684ac5d9 | -33.34282 | -52.8906 | 2025-11-09 13:03:00 | TERRA_M-T | SANTA VITÓRIA DO PALMAR | RIO GRANDE DO SUL | Brasil | 4317301 | 43 | 33 | nan | nan | nan | Pampa | 27.7 |
| 626447ce-0854-30d1-ac9d-4930515da42c | -3.3183 | -44.3585 | 2025-11-09 13:10:00 | GOES-19 | ITAPECURU MIRIM | MARANHÃO | Brasil | 2105401 | 21 | 33 | nan | nan | nan | Cerrado | 83.9 |
| b1ff0cb2-39e8-3d4a-a036-479049524cf2 | -5.8992 | -39.9623 | 2025-11-09 13:10:00 | GOES-19 | TAUÁ | CEARÁ | Brasil | 2313302 | 23 | 33 | nan | nan | nan | Caatinga | 92.8 |
| 8a521a57-d022-33b9-abef-3c5a47c14b23 | -19.7826 | -58.0412 | 2025-11-09 13:10:00 | GOES-19 | CORUMBÁ | MATO GROSSO DO SUL | Brasil | 5003207 | 50 | 33 | nan | nan | nan | Pantanal | 103.4 |
| 05f1431c-4cfa-3a96-9207-5fdf17b5cc00 | -5.6059 | -41.066 | 2025-11-09 13:10:00 | GOES-19 | SÃO MIGUEL DO TAPUIO | PIAUÍ | Brasil | 2210409 | 22 | 33 | nan | nan | nan | Caatinga | 83.6 |
| 4e253044-2a2e-3c69-8add-60d0a8e15490 | -1.6605 | -53.7118 | 2025-11-09 13:10:00 | GOES-19 | PRAINHA | PARÁ | Brasil | 1506005 | 15 | 33 | nan | nan | nan | Amazônia | 69.6 |
| c359ef62-f664-3fa9-933c-18638f82ab23 | -19.8023 | -58.0593 | 2025-11-09 13:10:00 | GOES-19 | CORUMBÁ | MATO GROSSO DO SUL | Brasil | 5003207 | 50 | 33 | nan | nan | nan | Pantanal | 102.1 |
| f01ac6d7-35f9-30a3-abd0-896c22681239 | -5.6057 | -41.0903 | 2025-11-09 13:10:00 | GOES-19 | SÃO MIGUEL DO TAPUIO | PIAUÍ | Brasil | 2210409 | 22 | 33 | nan | nan | nan | Caatinga | 99.8 |
| eedbdfd9-35c0-3bb5-b10b-aeaec14cb72b | -19.7822 | -58.062 | 2025-11-09 13:20:00 | GOES-19 | CORUMBÁ | MATO GROSSO DO SUL | Brasil | 5003207 | 50 | 33 | nan | nan | nan | Pantanal | 108.5 |
| 1c10721a-b053-3e39-ad39-ca521d00c7cb | -19.7625 | -58.0438 | 2025-11-09 13:20:00 | GOES-19 | CORUMBÁ | MATO GROSSO DO SUL | Brasil | 5003207 | 50 | 33 | nan | nan | nan | Pantanal | 95.1 |
| aecbb197-9e13-3bb0-9c2f-af921bb6bc96 | -1.6605 | -53.7319 | 2025-11-09 13:20:00 | GOES-19 | PRAINHA | PARÁ | Brasil | 1506005 | 15 | 33 | nan | nan | nan | Amazônia | 67.2 |
| 0ec551e9-5af1-3f07-aaa3-5aebb8f629fc | -5.8992 | -39.9623 | 2025-11-09 13:20:00 | GOES-19 | TAUÁ | CEARÁ | Brasil | 2313302 | 23 | 33 | nan | nan | nan | Caatinga | 88.7 |
| ec976dca-58ec-333b-aba8-6219db5f4833 | -3.7732 | -43.0434 | 2025-11-09 13:20:00 | GOES-19 | BURITI | MARANHÃO | Brasil | 2102200 | 21 | 33 | nan | nan | nan | Cerrado | 73.6 |
| ef3cd083-4da3-3b43-a207-f64deef07f66 | -19.7826 | -58.0412 | 2025-11-09 13:20:00 | GOES-19 | CORUMBÁ | MATO GROSSO DO SUL | Brasil | 5003207 | 50 | 33 | nan | nan | nan | Pantanal | 102.9 |
| 90605d97-4ec6-3606-890a-e8c8e931cb81 | -5.6059 | -41.066 | 2025-11-09 13:20:00 | GOES-19 | SÃO MIGUEL DO TAPUIO | PIAUÍ | Brasil | 2210409 | 22 | 33 | nan | nan | nan | Caatinga | 85.4 |
| 0d34ed8a-1008-3dea-84f6-4d8d925e2b1d | -5.6057 | -41.0903 | 2025-11-09 13:20:00 | GOES-19 | SÃO MIGUEL DO TAPUIO | PIAUÍ | Brasil | 2210409 | 22 | 33 | nan | nan | nan | Caatinga | 101.1 |
| e02c7277-1a3e-34ce-b1e1-7d059d1d2508 | -19.8023 | -58.0593 | 2025-11-09 13:20:00 | GOES-19 | CORUMBÁ | MATO GROSSO DO SUL | Brasil | 5003207 | 50 | 33 | nan | nan | nan | Pantanal | 109.5 |
| dc5b9909-103d-389d-9766-86aa27258fcb | -1.6605 | -53.7118 | 2025-11-09 13:20:00 | GOES-19 | PRAINHA | PARÁ | Brasil | 1506005 | 15 | 33 | nan | nan | nan | Amazônia | 67.2 |
| f717345f-fd84-324f-b409-45b58e29e351 | -3.7732 | -43.0434 | 2025-11-09 13:30:00 | GOES-19 | BURITI | MARANHÃO | Brasil | 2102200 | 21 | 33 | nan | nan | nan | Cerrado | 75.9 |
| a769ff5c-4715-325b-8118-f352186ef7c1 | -5.6057 | -41.0903 | 2025-11-09 13:30:00 | GOES-19 | SÃO MIGUEL DO TAPUIO | PIAUÍ | Brasil | 2210409 | 22 | 33 | nan | nan | nan | Caatinga | 121.7 |
| 3e1b95f5-c686-37d3-b02a-14675d9b96c6 | -19.7822 | -58.062 | 2025-11-09 13:30:00 | GOES-19 | CORUMBÁ | MATO GROSSO DO SUL | Brasil | 5003207 | 50 | 33 | nan | nan | nan | Pantanal | 109.7 |
| 2d60ef72-a92d-30a6-b6a6-6b98e5a4b9c7 | -19.8023 | -58.0593 | 2025-11-09 13:30:00 | GOES-19 | CORUMBÁ | MATO GROSSO DO SUL | Brasil | 5003207 | 50 | 33 | nan | nan | nan | Pantanal | 111.3 |
| 1f52d4bc-ee30-3b56-b8d9-fa81daade216 | -19.7826 | -58.0412 | 2025-11-09 13:30:00 | GOES-19 | CORUMBÁ | MATO GROSSO DO SUL | Brasil | 5003207 | 50 | 33 | nan | nan | nan | Pantanal | 110.2 |
| bd1eaee2-5280-35cd-9dca-436c3ad0f9fe | -7.5477 | -45.8417 | 2025-11-09 13:30:00 | GOES-19 | BALSAS | MARANHÃO | Brasil | 2101400 | 21 | 33 | nan | nan | nan | Cerrado | 89.4 |
| a415718f-e929-317b-b8cf-be3995ddbff2 | -19.7625 | -58.0438 | 2025-11-09 13:30:00 | GOES-19 | CORUMBÁ | MATO GROSSO DO SUL | Brasil | 5003207 | 50 | 33 | nan | nan | nan | Pantanal | 100.3 |
| f7d82768-6f59-34b8-b3e9-45f25e4a9c05 | -5.6059 | -41.066 | 2025-11-09 13:30:00 | GOES-19 | SÃO MIGUEL DO TAPUIO | PIAUÍ | Brasil | 2210409 | 22 | 33 | nan | nan | nan | Caatinga | 86.7 |
| bb6eebcb-d072-38d0-a4a5-59cc39fa22d0 | -19.8023 | -58.0593 | 2025-11-09 13:40:00 | GOES-19 | CORUMBÁ | MATO GROSSO DO SUL | Brasil | 5003207 | 50 | 33 | nan | nan | nan | Pantanal | 129.1 |
| 93036ea4-6d5e-3a1a-a5e5-75780e0a9d2c | -5.6059 | -41.066 | 2025-11-09 13:40:00 | GOES-19 | SÃO MIGUEL DO TAPUIO | PIAUÍ | Brasil | 2210409 | 22 | 33 | nan | nan | nan | Caatinga | 105.6 |
| a22b44db-d490-3945-b0ba-dc4aa3afde73 | -8.0137 | -38.8788 | 2025-11-09 13:40:00 | GOES-19 | VERDEJANTE | PERNAMBUCO | Brasil | 2616100 | 26 | 33 | nan | nan | nan | Caatinga | 109.2 |
| fa2fe31b-ba6a-3878-bfba-388905b2228f | -19.7625 | -58.0438 | 2025-11-09 13:40:00 | GOES-19 | CORUMBÁ | MATO GROSSO DO SUL | Brasil | 5003207 | 50 | 33 | nan | nan | nan | Pantanal | 102.6 |
| 515aabd2-3ed4-3e0a-b1bc-ca2e829e1505 | -7.5477 | -45.8417 | 2025-11-09 13:40:00 | GOES-19 | BALSAS | MARANHÃO | Brasil | 2101400 | 21 | 33 | nan | nan | nan | Cerrado | 108.4 |
| dce4247a-cce3-3600-8849-816fe0ec01cd | -5.6057 | -41.0903 | 2025-11-09 13:40:00 | GOES-19 | SÃO MIGUEL DO TAPUIO | PIAUÍ | Brasil | 2210409 | 22 | 33 | nan | nan | nan | Caatinga | 146.8 |
| c18052a8-b25e-39d7-a379-be9e49c7a7eb | -19.7822 | -58.062 | 2025-11-09 13:40:00 | GOES-19 | CORUMBÁ | MATO GROSSO DO SUL | Brasil | 5003207 | 50 | 33 | nan | nan | nan | Pantanal | 121.5 |
| c44615c6-414c-3c97-bdc9-b44956b52b4f | -19.7826 | -58.0412 | 2025-11-09 13:40:00 | GOES-19 | CORUMBÁ | MATO GROSSO DO SUL | Brasil | 5003207 | 50 | 33 | nan | nan | nan | Pantanal | 125.5 |
| 73cec777-0459-36f4-ab6c-df4435c76045 | -6.1083 | -41.627 | 2025-11-09 13:40:00 | GOES-19 | PIMENTEIRAS | PIAUÍ | Brasil | 2208106 | 22 | 33 | nan | nan | nan | Caatinga | 102.7 |
| cb15f66a-548c-3ff2-856d-c6e4d2f47a94 | -19.8027 | -58.0386 | 2025-11-09 13:40:00 | GOES-19 | CORUMBÁ | MATO GROSSO DO SUL | Brasil | 5003207 | 50 | 33 | nan | nan | nan | Pantanal | 99.1 |
| e68c237a-6f7f-3e30-8fc5-16cdae9a428c | -1.2566 | -53.7972 | 2025-11-09 13:50:00 | GOES-19 | PRAINHA | PARÁ | Brasil | 1506005 | 15 | 33 | nan | nan | nan | Amazônia | 124.6 |
| d9ecb408-1734-30a7-9a59-5a39183514f6 | -5.6245 | -41.0887 | 2025-11-09 13:50:00 | GOES-19 | SÃO MIGUEL DO TAPUIO | PIAUÍ | Brasil | 2210409 | 22 | 33 | nan | nan | nan | Caatinga | 107.8 |
| 1d116cc6-6383-320f-820a-35707061180d | -5.9229 | -41.354 | 2025-11-09 13:50:00 | GOES-19 | SÃO MIGUEL DO TAPUIO | PIAUÍ | Brasil | 2210409 | 22 | 33 | nan | nan | nan | Caatinga | 98.4 |
| 7692eedd-5e47-3443-af04-a4ba3eb33e8c | -1.2383 | -53.7974 | 2025-11-09 13:50:00 | GOES-19 | PRAINHA | PARÁ | Brasil | 1506005 | 15 | 33 | nan | nan | nan | Amazônia | 91.6 |
| a29dc094-6e53-3d32-965d-2a32b2382ac9 | -5.6057 | -41.0903 | 2025-11-09 13:50:00 | GOES-19 | SÃO MIGUEL DO TAPUIO | PIAUÍ | Brasil | 2210409 | 22 | 33 | nan | nan | nan | Caatinga | 156.0 |
| 82b7d0cd-e1ea-33da-9e41-f1c9590981b8 | -7.5477 | -45.8417 | 2025-11-09 13:50:00 | GOES-19 | BALSAS | MARANHÃO | Brasil | 2101400 | 21 | 33 | nan | nan | nan | Cerrado | 118.5 |
| 110d7926-f7d7-3933-be0a-1a88346e112a | -3.1963 | -42.7195 | 2025-11-09 13:50:00 | GOES-19 | SANTANA DO MARANHÃO | MARANHÃO | Brasil | 2110237 | 21 | 33 | nan | nan | nan | Cerrado | 76.2 |
| a3337c39-4137-30f9-a57f-e35a61ac81df | 1.9681 | -55.8595 | 2025-11-09 13:50:00 | GOES-19 | ORIXIMINÁ | PARÁ | Brasil | 1505304 | 15 | 33 | nan | nan | nan | Amazônia | 69.4 |
| 5c3bf6c7-9de8-3afc-baaa-910f4813c549 | -5.6059 | -41.066 | 2025-11-09 13:50:00 | GOES-19 | SÃO MIGUEL DO TAPUIO | PIAUÍ | Brasil | 2210409 | 22 | 33 | nan | nan | nan | Caatinga | 122.8 |
| 53d7d47a-131a-39be-a160-2788cd065987 | -12.5102 | -39.5456 | 2025-11-09 13:50:00 | GOES-19 | RAFAEL JAMBEIRO | BAHIA | Brasil | 2925956 | 29 | 33 | nan | nan | nan | Caatinga | 146.5 |
| e0c9c1d2-891d-39e0-a2a2-9de579ce826d | -5.6059 | -41.066 | 2025-11-09 14:00:00 | GOES-19 | SÃO MIGUEL DO TAPUIO | PIAUÍ | Brasil | 2210409 | 22 | 33 | nan | nan | nan | Caatinga | 127.6 |
| 82988369-724c-331f-a1e6-c00f2db9e670 | -4.0949 | -42.4152 | 2025-11-09 14:00:00 | GOES-19 | BARRAS | PIAUÍ | Brasil | 2201200 | 22 | 33 | nan | nan | nan | Caatinga | 84.7 |
| a5974b0d-a9a3-3c7c-a936-8bf7eadf3fe0 | -12.5102 | -39.5456 | 2025-11-09 14:00:00 | GOES-19 | RAFAEL JAMBEIRO | BAHIA | Brasil | 2925956 | 29 | 33 | nan | nan | nan | Caatinga | 156.8 |
| b7bd42ea-fa74-33ab-b856-bc27810c2bfd | -1.2383 | -53.7974 | 2025-11-09 14:00:00 | GOES-19 | PRAINHA | PARÁ | Brasil | 1506005 | 15 | 33 | nan | nan | nan | Amazônia | 78.1 |
| 45f5de03-d76b-396a-a242-3be1ffaefbf9 | -1.2566 | -53.7972 | 2025-11-09 14:00:00 | GOES-19 | PRAINHA | PARÁ | Brasil | 1506005 | 15 | 33 | nan | nan | nan | Amazônia | 79.3 |
| 4da01cf7-1a84-33a2-8d6c-46b9e6eeba0a | -3.1963 | -42.7195 | 2025-11-09 14:00:00 | GOES-19 | SANTANA DO MARANHÃO | MARANHÃO | Brasil | 2110237 | 21 | 33 | nan | nan | nan | Cerrado | 76.8 |
| 2a397a41-7a7b-37ad-ac38-a7e54ba0583c | -19.7822 | -58.062 | 2025-11-09 14:10:00 | GOES-19 | CORUMBÁ | MATO GROSSO DO SUL | Brasil | 5003207 | 50 | 33 | nan | nan | nan | Pantanal | 121.9 |
| 70caf262-cd19-3007-8ccc-399aeae1ff13 | -19.7625 | -58.0438 | 2025-11-09 14:10:00 | GOES-19 | CORUMBÁ | MATO GROSSO DO SUL | Brasil | 5003207 | 50 | 33 | nan | nan | nan | Pantanal | 111.1 |
| 46a55b22-8327-3187-8bb3-a720fcb3db4d | -5.6059 | -41.066 | 2025-11-09 14:10:00 | GOES-19 | SÃO MIGUEL DO TAPUIO | PIAUÍ | Brasil | 2210409 | 22 | 33 | nan | nan | nan | Caatinga | 103.6 |
| 3cb35f63-2876-3f50-95fa-ca281f6d71bc | -12.5102 | -39.5456 | 2025-11-09 14:10:00 | GOES-19 | RAFAEL JAMBEIRO | BAHIA | Brasil | 2925956 | 29 | 33 | nan | nan | nan | Caatinga | 157.6 |
| 87e5fcda-3885-30b9-be85-00ecad517e5b | -4.8434 | -40.1231 | 2025-11-09 14:10:00 | GOES-19 | TAMBORIL | CEARÁ | Brasil | 2313203 | 23 | 33 | nan | nan | nan | Caatinga | 117.1 |
| 4028a7fa-9aa2-3023-b35b-8ac0acd2dcec | -19.8027 | -58.0386 | 2025-11-09 14:10:00 | GOES-19 | CORUMBÁ | MATO GROSSO DO SUL | Brasil | 5003207 | 50 | 33 | nan | nan | nan | Pantanal | 97.2 |
| eb1243cf-3a2f-3a7f-9e0d-edf47f70e30c | -1.6605 | -53.7319 | 2025-11-09 14:10:00 | GOES-19 | PRAINHA | PARÁ | Brasil | 1506005 | 15 | 33 | nan | nan | nan | Amazônia | 64.5 |
| dd69d74b-345b-3906-9fc8-ed283e931be6 | -19.8023 | -58.0593 | 2025-11-09 14:10:00 | GOES-19 | CORUMBÁ | MATO GROSSO DO SUL | Brasil | 5003207 | 50 | 33 | nan | nan | nan | Pantanal | 130.0 |
| 2f7df625-0fd6-3e57-9004-283c45cbae0b | -19.7826 | -58.0412 | 2025-11-09 14:10:00 | GOES-19 | CORUMBÁ | MATO GROSSO DO SUL | Brasil | 5003207 | 50 | 33 | nan | nan | nan | Pantanal | 126.9 |


