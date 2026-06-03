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

## Dados Diários - Página 13

| ID | Latitude | Longitude | Data/Hora GMT | Satélite | Município | Estado | País | Município ID | Estado ID | País ID | Dias sem Chuva | Precipitação | Risco de Fogo | Bioma | FRP |
|----|----------|-----------|---------------|----------|-----------|--------|------|--------------|-----------|---------|----------------|--------------|----------------|-------|-----|
| f8effcba-ad9d-36e1-9de1-96f6833b5964 | -12.4283 | -58.4048 | 2026-06-03 16:00:00 | GOES-19 | BRASNORTE | MATO GROSSO | Brasil | 5101902 | 51 | 33 | nan | nan | nan | Cerrado | 80.9 |
| 3d93a429-c04d-3b4c-adac-8fc896ff6d79 | -10.8573 | -53.7425 | 2026-06-03 16:00:00 | GOES-19 | MARCELÂNDIA | MATO GROSSO | Brasil | 5105580 | 51 | 33 | nan | nan | nan | Amazônia | 98.6 |
| d5f34cd3-d3f2-33f0-b0c5-bf7357415d7d | -10.5736 | -57.3165 | 2026-06-03 16:00:00 | GOES-19 | JUARA | MATO GROSSO | Brasil | 5105101 | 51 | 33 | nan | nan | nan | Amazônia | 68.2 |
| 1700ee0d-ed72-361b-a9da-25b7c3039d23 | -14.0919 | -59.3777 | 2026-06-03 16:00:00 | GOES-19 | NOVA LACERDA | MATO GROSSO | Brasil | 5106182 | 51 | 33 | nan | nan | nan | Cerrado | 91.3 |
| 976c5877-9b65-300d-830f-151c4b382bf8 | -12.4473 | -58.4033 | 2026-06-03 16:00:00 | GOES-19 | BRASNORTE | MATO GROSSO | Brasil | 5101902 | 51 | 33 | nan | nan | nan | Cerrado | 88.3 |
| 72ce1a0f-de94-3bcc-a137-a0d6ec3b844b | -10.3675 | -64.5058 | 2026-06-03 16:00:00 | GOES-19 | NOVA MAMORÉ | RONDÔNIA | Brasil | 1100338 | 11 | 33 | nan | nan | nan | Amazônia | 45.7 |
| 11929923-2ff2-33dc-b3ba-01edbafb7338 | -10.8573 | -53.7425 | 2026-06-03 16:10:00 | GOES-19 | MARCELÂNDIA | MATO GROSSO | Brasil | 5105580 | 51 | 33 | nan | nan | nan | Amazônia | 94.4 |
| f328c675-db9f-3411-b745-baec3b9e2c8a | -14.1541 | -58.9755 | 2026-06-03 16:10:00 | GOES-19 | TANGARÁ DA SERRA | MATO GROSSO | Brasil | 5107958 | 51 | 33 | nan | nan | nan | Cerrado | 115.6 |
| 8d5cb821-b5c4-3e5f-84a4-1efea5a6646e | -11.614 | -55.1861 | 2026-06-03 16:10:00 | GOES-19 | CLÁUDIA | MATO GROSSO | Brasil | 5103056 | 51 | 33 | nan | nan | nan | Amazônia | 91.1 |
| e3c2de0f-de49-3b07-ab9b-437a254bf08f | -12.4283 | -58.4048 | 2026-06-03 16:10:00 | GOES-19 | BRASNORTE | MATO GROSSO | Brasil | 5101902 | 51 | 33 | nan | nan | nan | Cerrado | 103.0 |
| 8f0f619b-8eae-3088-b6f7-96a801d83c0e | -10.5736 | -57.3165 | 2026-06-03 16:10:00 | GOES-19 | JUARA | MATO GROSSO | Brasil | 5105101 | 51 | 33 | nan | nan | nan | Amazônia | 71.6 |
| fce28a61-ef44-3a5f-a929-9739d2f1b74e | -14.0919 | -59.3777 | 2026-06-03 16:10:00 | GOES-19 | NOVA LACERDA | MATO GROSSO | Brasil | 5106182 | 51 | 33 | nan | nan | nan | Cerrado | 102.8 |
| 24839d97-6fe5-3c9b-bc6a-31b35e15f74a | -12.7463 | -54.1969 | 2026-06-03 16:10:00 | GOES-19 | PARANATINGA | MATO GROSSO | Brasil | 5106307 | 51 | 33 | nan | nan | nan | Amazônia | 63.8 |
| 290f1fb3-cdd9-378a-9423-e8dc59880e4d | -12.4473 | -58.4033 | 2026-06-03 16:10:00 | GOES-19 | BRASNORTE | MATO GROSSO | Brasil | 5101902 | 51 | 33 | nan | nan | nan | Cerrado | 66.3 |
| e7fad905-26e6-3be2-af7c-13c9a96deae5 | -10.3675 | -64.5058 | 2026-06-03 16:10:00 | GOES-19 | NOVA MAMORÉ | RONDÔNIA | Brasil | 1100338 | 11 | 33 | nan | nan | nan | Amazônia | 48.0 |
| 44df85dc-ef9a-3d61-b64a-0c0166a6289b | -14.0917 | -59.3975 | 2026-06-03 16:10:00 | GOES-19 | NOVA LACERDA | MATO GROSSO | Brasil | 5106182 | 51 | 33 | nan | nan | nan | Cerrado | 81.6 |
| 909e8473-5adb-33d3-896b-a3fcc68fc736 | -10.8573 | -53.7425 | 2026-06-03 16:20:00 | GOES-19 | MARCELÂNDIA | MATO GROSSO | Brasil | 5105580 | 51 | 33 | nan | nan | nan | Amazônia | 91.2 |
| 463d59ec-68e3-3294-a17f-325747a30e85 | -10.5736 | -57.3165 | 2026-06-03 16:20:00 | GOES-19 | JUARA | MATO GROSSO | Brasil | 5105101 | 51 | 33 | nan | nan | nan | Amazônia | 86.4 |
| 6a4cd788-b0ad-38af-924d-000299ef78c1 | -12.4473 | -58.4033 | 2026-06-03 16:20:00 | GOES-19 | BRASNORTE | MATO GROSSO | Brasil | 5101902 | 51 | 33 | nan | nan | nan | Cerrado | 66.3 |
| 6f09031e-ca28-3b53-a4e1-41d9a947f757 | -11.614 | -55.1861 | 2026-06-03 16:20:00 | GOES-19 | CLÁUDIA | MATO GROSSO | Brasil | 5103056 | 51 | 33 | nan | nan | nan | Amazônia | 75.4 |
| 3d3efcd6-2a0b-3919-82d9-3229dcf81f75 | -14.0919 | -59.3777 | 2026-06-03 16:20:00 | GOES-19 | NOVA LACERDA | MATO GROSSO | Brasil | 5106182 | 51 | 33 | nan | nan | nan | Cerrado | 101.0 |
| 6dffe2da-0b99-324b-bac1-ea18db5db5f4 | -12.4283 | -58.4048 | 2026-06-03 16:20:00 | GOES-19 | BRASNORTE | MATO GROSSO | Brasil | 5101902 | 51 | 33 | nan | nan | nan | Cerrado | 82.0 |
| 55e206ba-e029-389f-a8a4-1407aed8ccbc | -11.614 | -55.1861 | 2026-06-03 16:30:00 | GOES-19 | CLÁUDIA | MATO GROSSO | Brasil | 5103056 | 51 | 33 | nan | nan | nan | Amazônia | 66.2 |
| 507019a0-8f6d-3730-8e1e-9598e47041aa | -10.8573 | -53.7425 | 2026-06-03 16:30:00 | GOES-19 | MARCELÂNDIA | MATO GROSSO | Brasil | 5105580 | 51 | 33 | nan | nan | nan | Amazônia | 87.8 |
| d692489a-eeba-3c4f-86e1-7e02251fba59 | -12.4473 | -58.4033 | 2026-06-03 16:30:00 | GOES-19 | BRASNORTE | MATO GROSSO | Brasil | 5101902 | 51 | 33 | nan | nan | nan | Cerrado | 67.4 |
| 0e923d94-7200-3917-a99a-4005323c3adc | -10.5736 | -57.3165 | 2026-06-03 16:30:00 | GOES-19 | JUARA | MATO GROSSO | Brasil | 5105101 | 51 | 33 | nan | nan | nan | Amazônia | 86.2 |
| 94e53174-2f3b-3c3b-bb6b-17d5e86264c7 | -14.0919 | -59.3777 | 2026-06-03 16:30:00 | GOES-19 | NOVA LACERDA | MATO GROSSO | Brasil | 5106182 | 51 | 33 | nan | nan | nan | Cerrado | 52.8 |
| 3721df08-519b-3b57-bb21-998f07199eea | -12.4283 | -58.4048 | 2026-06-03 16:30:00 | GOES-19 | BRASNORTE | MATO GROSSO | Brasil | 5101902 | 51 | 33 | nan | nan | nan | Cerrado | 63.4 |
| 241d238a-48e8-3cd3-a388-977c68318952 | -14.0919 | -59.3777 | 2026-06-03 16:40:00 | GOES-19 | NOVA LACERDA | MATO GROSSO | Brasil | 5106182 | 51 | 33 | nan | nan | nan | Cerrado | 85.4 |
| 0c5a5069-f1be-34d4-98aa-b48def375b61 | -12.7463 | -54.1969 | 2026-06-03 16:40:00 | GOES-19 | PARANATINGA | MATO GROSSO | Brasil | 5106307 | 51 | 33 | nan | nan | nan | Amazônia | 89.0 |
| 766a1652-bbdb-30c8-9476-438e66fdd94c | -10.5736 | -57.3165 | 2026-06-03 16:40:00 | GOES-19 | JUARA | MATO GROSSO | Brasil | 5105101 | 51 | 33 | nan | nan | nan | Amazônia | 85.9 |
| 6cf30f4b-3848-3e09-8f98-c62a296f87a3 | -14.1541 | -58.9755 | 2026-06-03 16:40:00 | GOES-19 | TANGARÁ DA SERRA | MATO GROSSO | Brasil | 5107958 | 51 | 33 | nan | nan | nan | Cerrado | 127.3 |
| 4c394fdc-0f6c-33e6-9064-6bd39866d24b | -11.614 | -55.1861 | 2026-06-03 16:40:00 | GOES-19 | CLÁUDIA | MATO GROSSO | Brasil | 5103056 | 51 | 33 | nan | nan | nan | Amazônia | 65.1 |
| ee0e7be9-623f-388a-9c58-165da9dbdc57 | -11.614 | -55.1861 | 2026-06-03 16:50:00 | GOES-19 | CLÁUDIA | MATO GROSSO | Brasil | 5103056 | 51 | 33 | nan | nan | nan | Amazônia | 60.7 |
| 6025f129-4716-3cee-8978-bc7d58b246c7 | -10.8573 | -53.7425 | 2026-06-03 16:50:00 | GOES-19 | MARCELÂNDIA | MATO GROSSO | Brasil | 5105580 | 51 | 33 | nan | nan | nan | Amazônia | 86.4 |
| 993b9093-5003-3b82-8354-bdded442e551 | -14.0919 | -59.3777 | 2026-06-03 16:50:00 | GOES-19 | NOVA LACERDA | MATO GROSSO | Brasil | 5106182 | 51 | 33 | nan | nan | nan | Cerrado | 76.3 |
| 8752a42d-60bb-3209-8cea-a9b8b2b4b59f | -10.5736 | -57.3165 | 2026-06-03 16:50:00 | GOES-19 | JUARA | MATO GROSSO | Brasil | 5105101 | 51 | 33 | nan | nan | nan | Amazônia | 87.7 |
| e7b2ee48-f51a-3037-b690-984749ba2d23 | -12.7463 | -54.1969 | 2026-06-03 16:50:00 | GOES-19 | PARANATINGA | MATO GROSSO | Brasil | 5106307 | 51 | 33 | nan | nan | nan | Amazônia | 98.5 |
| e9411ec5-9f5d-3cda-ae03-a0a603a34c75 | -12.7463 | -54.1969 | 2026-06-03 17:00:00 | GOES-19 | PARANATINGA | MATO GROSSO | Brasil | 5106307 | 51 | 33 | nan | nan | nan | Amazônia | 94.3 |
| b043ca46-07d8-3209-a1fe-853e2734d1f1 | -10.5736 | -57.3165 | 2026-06-03 17:00:00 | GOES-19 | JUARA | MATO GROSSO | Brasil | 5105101 | 51 | 33 | nan | nan | nan | Amazônia | 74.6 |
| 3b86a21c-ef07-3bbc-a5ce-e6e9524c7e19 | -10.8573 | -53.7425 | 2026-06-03 17:00:00 | GOES-19 | MARCELÂNDIA | MATO GROSSO | Brasil | 5105580 | 51 | 33 | nan | nan | nan | Amazônia | 93.6 |
| 20666657-170b-3ed6-982a-4746619fb73f | -12.7272 | -54.1988 | 2026-06-03 17:00:00 | GOES-19 | PARANATINGA | MATO GROSSO | Brasil | 5106307 | 51 | 33 | nan | nan | nan | Amazônia | 89.2 |
| 76183479-b7c7-35bd-bd96-856173b8fd9d | -11.614 | -55.1861 | 2026-06-03 17:00:00 | GOES-19 | CLÁUDIA | MATO GROSSO | Brasil | 5103056 | 51 | 33 | nan | nan | nan | Amazônia | 71.3 |
| 0079655d-d2fb-382f-94cf-4300da627313 | -14.0919 | -59.3777 | 2026-06-03 17:00:00 | GOES-19 | NOVA LACERDA | MATO GROSSO | Brasil | 5106182 | 51 | 33 | nan | nan | nan | Cerrado | 78.5 |
| 6aeef75a-661e-3a3b-8801-958a1e7f8693 | -10.8573 | -53.7425 | 2026-06-03 17:10:00 | GOES-19 | MARCELÂNDIA | MATO GROSSO | Brasil | 5105580 | 51 | 33 | nan | nan | nan | Amazônia | 82.8 |
| 47de4fb2-810d-3551-afb7-5a3af37a9419 | -12.7272 | -54.1988 | 2026-06-03 17:10:00 | GOES-19 | PARANATINGA | MATO GROSSO | Brasil | 5106307 | 51 | 33 | nan | nan | nan | Amazônia | 80.7 |
| 110f49dd-8d61-3a62-aee2-34558188b7c4 | -14.1735 | -58.9539 | 2026-06-03 17:10:00 | GOES-19 | TANGARÁ DA SERRA | MATO GROSSO | Brasil | 5107958 | 51 | 33 | nan | nan | nan | Cerrado | 60.9 |
| 42d2df09-9899-3529-adb8-da557b7e3bca | -12.7463 | -54.1969 | 2026-06-03 17:10:00 | GOES-19 | PARANATINGA | MATO GROSSO | Brasil | 5106307 | 51 | 33 | nan | nan | nan | Amazônia | 104.7 |
| 397f1353-f40b-3495-a350-9133a864d49c | -10.5736 | -57.3165 | 2026-06-03 17:10:00 | GOES-19 | JUARA | MATO GROSSO | Brasil | 5105101 | 51 | 33 | nan | nan | nan | Amazônia | 70.4 |
| a00a2f68-d0f0-324c-9b13-14026cd03d2c | -11.614 | -55.1861 | 2026-06-03 17:10:00 | GOES-19 | CLÁUDIA | MATO GROSSO | Brasil | 5103056 | 51 | 33 | nan | nan | nan | Amazônia | 57.0 |
| d38a85a4-cf24-316b-a736-41251ffbc3c2 | -12.7272 | -54.1988 | 2026-06-03 17:20:00 | GOES-19 | PARANATINGA | MATO GROSSO | Brasil | 5106307 | 51 | 33 | nan | nan | nan | Amazônia | 87.1 |
| cc49131a-a7eb-36cf-8adb-423351587769 | -12.7463 | -54.1969 | 2026-06-03 17:20:00 | GOES-19 | PARANATINGA | MATO GROSSO | Brasil | 5106307 | 51 | 33 | nan | nan | nan | Amazônia | 96.2 |
| 46b5df65-44e3-3e33-ad73-d3bf9dd542df | -10.8573 | -53.7425 | 2026-06-03 17:20:00 | GOES-19 | MARCELÂNDIA | MATO GROSSO | Brasil | 5105580 | 51 | 33 | nan | nan | nan | Amazônia | 82.8 |
| a47d2556-ec08-31fb-b1ec-25fe5b7c2df5 | -11.6123 | -55.3283 | 2026-06-03 17:20:00 | GOES-19 | SINOP | MATO GROSSO | Brasil | 5107909 | 51 | 33 | nan | nan | nan | Amazônia | 56.9 |
| 2a0cd857-a8a8-3402-a968-a898d7bbfb5b | -10.5736 | -57.3165 | 2026-06-03 17:20:00 | GOES-19 | JUARA | MATO GROSSO | Brasil | 5105101 | 51 | 33 | nan | nan | nan | Amazônia | 64.0 |
| 9ecead32-4d07-3da0-8fb6-89245b1879bb | -11.614 | -55.1861 | 2026-06-03 17:20:00 | GOES-19 | CLÁUDIA | MATO GROSSO | Brasil | 5103056 | 51 | 33 | nan | nan | nan | Amazônia | 64.1 |
| 3d7526c9-e7f5-320f-9f61-ebf8d8627956 | -11.5647 | -54.5794 | 2026-06-03 17:20:00 | GOES-19 | UNIÃO DO SUL | MATO GROSSO | Brasil | 5108303 | 51 | 33 | nan | nan | nan | Amazônia | 72.2 |
| b07abd02-da0b-3610-ba95-4b88c541096b | -14.0786 | -53.3832 | 2026-06-03 17:30:00 | GOES-19 | PARANATINGA | MATO GROSSO | Brasil | 5106307 | 51 | 33 | nan | nan | nan | Cerrado | 85.6 |
| a91c1d39-e808-30ea-bcb3-de8275bce6b5 | -14.0919 | -59.3777 | 2026-06-03 17:30:00 | GOES-19 | NOVA LACERDA | MATO GROSSO | Brasil | 5106182 | 51 | 33 | nan | nan | nan | Cerrado | 136.1 |
| aa6c1cb0-477e-3993-b17a-74849293716b | -10.8573 | -53.7425 | 2026-06-03 17:30:00 | GOES-19 | MARCELÂNDIA | MATO GROSSO | Brasil | 5105580 | 51 | 33 | nan | nan | nan | Amazônia | 75.6 |
| 31705c1d-df99-34af-9fe8-e08b5b8fdf7c | -10.5736 | -57.3165 | 2026-06-03 17:30:00 | GOES-19 | JUARA | MATO GROSSO | Brasil | 5105101 | 51 | 33 | nan | nan | nan | Amazônia | 63.2 |
| f2dc4f23-5a6f-34b3-87fc-3e9531fb4887 | -11.6123 | -55.3283 | 2026-06-03 17:30:00 | GOES-19 | SINOP | MATO GROSSO | Brasil | 5107909 | 51 | 33 | nan | nan | nan | Amazônia | 81.0 |
| 5da2dbab-34e0-3f5a-859d-8094db53a570 | -12.7272 | -54.1988 | 2026-06-03 17:30:00 | GOES-19 | PARANATINGA | MATO GROSSO | Brasil | 5106307 | 51 | 33 | nan | nan | nan | Amazônia | 105.4 |
| 7282e6ca-dc9d-3a8f-9a57-8243f43d89e9 | -12.7463 | -54.1969 | 2026-06-03 17:30:00 | GOES-19 | PARANATINGA | MATO GROSSO | Brasil | 5106307 | 51 | 33 | nan | nan | nan | Amazônia | 100.2 |
| dc11e146-7e8f-3840-9afb-41692f6bb144 | -14.0786 | -53.3832 | 2026-06-03 17:40:00 | GOES-19 | PARANATINGA | MATO GROSSO | Brasil | 5106307 | 51 | 33 | nan | nan | nan | Cerrado | 99.6 |
| db4fdcee-9155-36eb-90ee-7c3748503e57 | -11.6123 | -55.3283 | 2026-06-03 17:40:00 | GOES-19 | SINOP | MATO GROSSO | Brasil | 5107909 | 51 | 33 | nan | nan | nan | Amazônia | 81.9 |
| 9ea3c802-7b09-35f6-bb94-bf494cf491e9 | -10.5736 | -57.3165 | 2026-06-03 17:40:00 | GOES-19 | JUARA | MATO GROSSO | Brasil | 5105101 | 51 | 33 | nan | nan | nan | Amazônia | 59.4 |
| 7d79f981-9d01-3e82-a881-1eb37893d18b | -12.7463 | -54.1969 | 2026-06-03 17:40:00 | GOES-19 | PARANATINGA | MATO GROSSO | Brasil | 5106307 | 51 | 33 | nan | nan | nan | Amazônia | 89.3 |
| 67f8deb6-5f4b-3af9-b07a-c88f97e986bb | -14.7651 | -52.6658 | 2026-06-03 17:40:00 | GOES-19 | NOVA XAVANTINA | MATO GROSSO | Brasil | 5106257 | 51 | 33 | nan | nan | nan | Cerrado | 92.6 |
| 0fd8c008-1cd1-3a0d-a55d-f8f04aabd302 | -12.4473 | -58.4033 | 2026-06-03 17:40:00 | GOES-19 | BRASNORTE | MATO GROSSO | Brasil | 5101902 | 51 | 33 | nan | nan | nan | Cerrado | 71.5 |
| 176fd047-dba4-3cea-9aba-7ab853e7f7de | -14.7647 | -52.687 | 2026-06-03 17:40:00 | GOES-19 | NOVA XAVANTINA | MATO GROSSO | Brasil | 5106257 | 51 | 33 | nan | nan | nan | Cerrado | 69.0 |
| 3f4d467c-81a4-3a90-b312-b4f5ead87bf2 | -14.0919 | -59.3777 | 2026-06-03 17:40:00 | GOES-19 | NOVA LACERDA | MATO GROSSO | Brasil | 5106182 | 51 | 33 | nan | nan | nan | Cerrado | 140.8 |
| c306ae3a-93f8-3857-97c1-021c113cfe83 | -12.7272 | -54.1988 | 2026-06-03 17:40:00 | GOES-19 | PARANATINGA | MATO GROSSO | Brasil | 5106307 | 51 | 33 | nan | nan | nan | Amazônia | 93.3 |
| 148aa813-1b66-31dc-8f37-ffa818cbe390 | -14.1223 | -58.4406 | 2026-06-03 17:40:00 | GOES-19 | TANGARÁ DA SERRA | MATO GROSSO | Brasil | 5107958 | 51 | 33 | nan | nan | nan | Cerrado | 89.3 |


