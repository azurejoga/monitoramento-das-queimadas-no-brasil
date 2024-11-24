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

## Dados Diários - Página 23

| ID | Latitude | Longitude | Data/Hora GMT | Satélite | Município | Estado | País | Município ID | Estado ID | País ID | Dias sem Chuva | Precipitação | Risco de Fogo | Bioma | FRP |
|----|----------|-----------|---------------|----------|-----------|--------|------|--------------|-----------|---------|----------------|--------------|----------------|-------|-----|
| 463cde42-8f17-33d7-9086-ff6fadfde731 | -3.5159 | -53.8132 | 2024-11-24 01:40:00 | GOES-16 | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | 89.6 |
| 0dfab51c-0bf0-362d-a05c-605ddd983433 | -5.9556 | -48.0642 | 2024-11-24 01:40:00 | GOES-16 | SÃO BENTO DO TOCANTINS | TOCANTINS | Brasil | 1720101 | 17 | 33 | nan | nan | nan | Cerrado | 85.1 |
| 361ee183-c3cc-37ee-81ea-88f88a53fff7 | -1.601 | -46.8949 | 2024-11-24 01:40:00 | GOES-16 | SANTA LUZIA DO PARÁ | PARÁ | Brasil | 1506559 | 15 | 33 | nan | nan | nan | Amazônia | 110.9 |
| 969cc808-2f4a-3f95-9c89-3aaa827ceb07 | -1.8239 | -46.6265 | 2024-11-24 01:40:00 | GOES-16 | VISEU | PARÁ | Brasil | 1508308 | 15 | 33 | nan | nan | nan | Amazônia | 83.3 |
| d4a03eb3-2ed6-31ed-ae36-f7074c3c4df0 | -1.601 | -46.8729 | 2024-11-24 01:40:00 | GOES-16 | SANTA LUZIA DO PARÁ | PARÁ | Brasil | 1506559 | 15 | 33 | nan | nan | nan | Amazônia | 123.9 |
| bf07f4b8-f99e-345c-bb82-9cfe70e0cfd5 | -4.2419 | -48.7193 | 2024-11-24 01:40:00 | GOES-16 | RONDON DO PARÁ | PARÁ | Brasil | 1506187 | 15 | 33 | nan | nan | nan | Amazônia | 63.4 |
| 340b95a1-9331-3dec-be18-928e59b971db | -3.2929 | -45.7161 | 2024-11-24 01:50:00 | GOES-16 | ZÉ DOCA | MARANHÃO | Brasil | 2114007 | 21 | 33 | nan | nan | nan | Amazônia | 138.4 |
| b73d2ae2-9136-315b-afb5-5d4df4144c23 | -2.4456 | -49.0816 | 2024-11-24 01:50:00 | GOES-16 | MOJU | PARÁ | Brasil | 1504703 | 15 | 33 | nan | nan | nan | Amazônia | 61.7 |
| a2ea6c65-75d8-3b58-a010-0e53a8dbba03 | -1.5129 | -54.1959 | 2024-11-24 01:50:00 | GOES-16 | MONTE ALEGRE | PARÁ | Brasil | 1504802 | 15 | 33 | nan | nan | nan | Amazônia | 85.1 |
| 2ed2a927-ca20-3a06-a863-341266d14bfa | -1.8239 | -46.6265 | 2024-11-24 01:50:00 | GOES-16 | VISEU | PARÁ | Brasil | 1508308 | 15 | 33 | nan | nan | nan | Amazônia | 66.2 |
| fa71576e-812d-3218-afb4-f24a5471edbb | -4.242 | -48.6978 | 2024-11-24 01:50:00 | GOES-16 | RONDON DO PARÁ | PARÁ | Brasil | 1506187 | 15 | 33 | nan | nan | nan | Amazônia | 86.4 |
| 5c799f7f-167f-3dc1-8466-b919421d9ea1 | -1.8238 | -46.6486 | 2024-11-24 01:50:00 | GOES-16 | VISEU | PARÁ | Brasil | 1508308 | 15 | 33 | nan | nan | nan | Amazônia | 132.7 |
| 2c617694-4460-3cce-82c5-f3959a7ae973 | -1.8423 | -46.6482 | 2024-11-24 01:50:00 | GOES-16 | VISEU | PARÁ | Brasil | 1508308 | 15 | 33 | nan | nan | nan | Amazônia | 69.9 |
| 8419c21c-977f-3993-96c2-2678bfe9e7a8 | -3.2928 | -45.7384 | 2024-11-24 01:50:00 | GOES-16 | ZÉ DOCA | MARANHÃO | Brasil | 2114007 | 21 | 33 | nan | nan | nan | Amazônia | 162.7 |
| 10c2bf3a-11f0-3eb9-8912-2ebafbb4079d | -3.8417 | -44.0594 | 2024-11-24 01:50:00 | GOES-16 | COROATÁ | MARANHÃO | Brasil | 2103604 | 21 | 33 | nan | nan | nan | Cerrado | 57.5 |
| a38198e6-aee3-3d34-bb3f-ec1edb1ca78d | -2.2323 | -46.3961 | 2024-11-24 01:50:00 | GOES-16 | CACHOEIRA DO PIRIÁ | PARÁ | Brasil | 1501956 | 15 | 33 | nan | nan | nan | Amazônia | 77.9 |
| a556fe60-ac93-3b0f-ae79-3d3b26635571 | -5.9557 | -48.0425 | 2024-11-24 01:50:00 | GOES-16 | SÃO BENTO DO TOCANTINS | TOCANTINS | Brasil | 1720101 | 17 | 33 | nan | nan | nan | Cerrado | 107.4 |
| c59b9779-1aae-3eb6-95dc-5ea1f8cc855f | -2.2137 | -46.3965 | 2024-11-24 01:50:00 | GOES-16 | CACHOEIRA DO PIRIÁ | PARÁ | Brasil | 1501956 | 15 | 33 | nan | nan | nan | Amazônia | 82.9 |
| 7c3c67b7-bfbc-3dd1-8897-71e314d23653 | -1.601 | -46.8949 | 2024-11-24 01:50:00 | GOES-16 | SANTA LUZIA DO PARÁ | PARÁ | Brasil | 1506559 | 15 | 33 | nan | nan | nan | Amazônia | 150.4 |
| c3f7cb3f-e8ad-3333-af92-48df68f4d0c5 | -3.4013 | -50.3221 | 2024-11-24 01:50:00 | GOES-16 | PACAJÁ | PARÁ | Brasil | 1505486 | 15 | 33 | nan | nan | nan | Amazônia | 28.4 |
| 33a163b0-994a-34f8-b1d4-ad8c856ce856 | -3.5159 | -53.8132 | 2024-11-24 01:50:00 | GOES-16 | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | 109.0 |
| 2d83d261-ef9f-3ab3-ad93-8ff4b61b103a | -3.0355 | -49.4476 | 2024-11-24 01:50:00 | GOES-16 | MOJU | PARÁ | Brasil | 1504703 | 15 | 33 | nan | nan | nan | Amazônia | 51.4 |
| bd22dd67-0763-3ed2-bd3b-fc814afbaf24 | -3.5158 | -53.8333 | 2024-11-24 01:50:00 | GOES-16 | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | 55.0 |
| 3fbca1c8-45ee-33d4-bdf1-5fa005be1ef6 | -1.6195 | -46.8726 | 2024-11-24 01:50:00 | GOES-16 | SANTA LUZIA DO PARÁ | PARÁ | Brasil | 1506559 | 15 | 33 | nan | nan | nan | Amazônia | 84.9 |
| bdb6e98d-e7d2-3119-b761-1aefdb209a65 | -1.6195 | -46.8946 | 2024-11-24 01:50:00 | GOES-16 | SANTA LUZIA DO PARÁ | PARÁ | Brasil | 1506559 | 15 | 33 | nan | nan | nan | Amazônia | 79.7 |
| 5e9a1be5-2663-3445-876e-39af706b329f | -1.3666 | -53.8362 | 2024-11-24 01:50:00 | GOES-16 | MONTE ALEGRE | PARÁ | Brasil | 1504802 | 15 | 33 | nan | nan | nan | Amazônia | 70.3 |
| 6a7584b0-d354-3d2c-aa04-6bcb8ddeb5f2 | -1.5129 | -54.1759 | 2024-11-24 01:50:00 | GOES-16 | MONTE ALEGRE | PARÁ | Brasil | 1504802 | 15 | 33 | nan | nan | nan | Amazônia | 82.7 |
| fab60135-23bf-3e9e-9d47-934e5fd1fbaa | -1.601 | -46.8729 | 2024-11-24 01:50:00 | GOES-16 | SANTA LUZIA DO PARÁ | PARÁ | Brasil | 1506559 | 15 | 33 | nan | nan | nan | Amazônia | 187.7 |
| d567c74a-c82e-3b3b-a0b6-26ea834890c8 | -2.2137 | -46.3965 | 2024-11-24 02:00:00 | GOES-16 | CACHOEIRA DO PIRIÁ | PARÁ | Brasil | 1501956 | 15 | 33 | nan | nan | nan | Amazônia | 77.7 |
| 6598fe12-823d-3b0b-a344-ce5080f07e2f | -3.2928 | -45.7384 | 2024-11-24 02:00:00 | GOES-16 | ZÉ DOCA | MARANHÃO | Brasil | 2114007 | 21 | 33 | nan | nan | nan | Amazônia | 75.1 |
| 14f6e93b-395a-3f75-8df5-700aa9242ae5 | -5.1185 | -43.1497 | 2024-11-24 02:00:00 | GOES-16 | TIMON | MARANHÃO | Brasil | 2112209 | 21 | 33 | nan | nan | nan | Cerrado | 62.7 |
| 27cc0937-0412-325d-9292-5977a91b1453 | -4.2419 | -48.7193 | 2024-11-24 02:00:00 | GOES-16 | RONDON DO PARÁ | PARÁ | Brasil | 1506187 | 15 | 33 | nan | nan | nan | Amazônia | 60.7 |
| bc1a321e-0b6e-3f39-9898-6da28ac17215 | -0.2483 | -51.6248 | 2024-11-24 02:00:00 | GOES-16 | MAZAGÃO | AMAPÁ | Brasil | 1600402 | 16 | 33 | nan | nan | nan | Amazônia | 60.2 |
| aabf8fa7-1459-3c29-b736-6198ade42be1 | -5.9557 | -48.0425 | 2024-11-24 02:00:00 | GOES-16 | SÃO BENTO DO TOCANTINS | TOCANTINS | Brasil | 1720101 | 17 | 33 | nan | nan | nan | Cerrado | 87.5 |
| dbf93c9c-b345-3fbe-b823-2482521cf632 | -5.0998 | -43.151 | 2024-11-24 02:00:00 | GOES-16 | CAXIAS | MARANHÃO | Brasil | 2103000 | 21 | 33 | nan | nan | nan | Cerrado | 60.3 |
| 0a27b676-041a-3bc4-93bc-c5440656b07d | -1.8238 | -46.6486 | 2024-11-24 02:00:00 | GOES-16 | VISEU | PARÁ | Brasil | 1508308 | 15 | 33 | nan | nan | nan | Amazônia | 54.5 |
| 9515f755-a081-3995-b7bb-6316b66e390d | -4.242 | -48.6978 | 2024-11-24 02:00:00 | GOES-16 | RONDON DO PARÁ | PARÁ | Brasil | 1506187 | 15 | 33 | nan | nan | nan | Amazônia | 88.0 |
| de7a8e48-f6a1-3c40-8f9e-5b64893833e8 | -3.0582 | -53.2192 | 2024-11-24 02:00:00 | GOES-16 | MEDICILÂNDIA | PARÁ | Brasil | 1504455 | 15 | 33 | nan | nan | nan | Amazônia | 71.5 |
| b61f7a4b-e10d-3d91-94b1-183807a4fb09 | -3.2929 | -45.7161 | 2024-11-24 02:00:00 | GOES-16 | ZÉ DOCA | MARANHÃO | Brasil | 2114007 | 21 | 33 | nan | nan | nan | Amazônia | 68.6 |
| fafddaef-dd74-3f92-a998-4beb1131a8c1 | -3.5159 | -53.8132 | 2024-11-24 02:00:00 | GOES-16 | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | 123.7 |
| 5fc5b777-6cb9-3912-9393-bd13b9b1b040 | -3.4698 | -43.8931 | 2024-11-24 02:00:00 | GOES-16 | NINA RODRIGUES | MARANHÃO | Brasil | 2107209 | 21 | 33 | nan | nan | nan | Cerrado | 60.1 |
| 4fe88fe3-505e-3be7-bcd1-a44f8006b1cb | -1.6195 | -46.8726 | 2024-11-24 02:00:00 | GOES-16 | SANTA LUZIA DO PARÁ | PARÁ | Brasil | 1506559 | 15 | 33 | nan | nan | nan | Amazônia | 94.6 |
| b36f0e05-cf10-3d7a-8b6b-24054d639e01 | -1.5129 | -54.1959 | 2024-11-24 02:00:00 | GOES-16 | MONTE ALEGRE | PARÁ | Brasil | 1504802 | 15 | 33 | nan | nan | nan | Amazônia | 80.3 |
| 37c6e956-1b83-3074-904d-873a4b4df389 | -1.601 | -46.8949 | 2024-11-24 02:00:00 | GOES-16 | SANTA LUZIA DO PARÁ | PARÁ | Brasil | 1506559 | 15 | 33 | nan | nan | nan | Amazônia | 66.7 |
| a75ca504-ae4d-3143-a3f9-0da83dda143d | -1.601 | -46.8729 | 2024-11-24 02:00:00 | GOES-16 | SANTA LUZIA DO PARÁ | PARÁ | Brasil | 1506559 | 15 | 33 | nan | nan | nan | Amazônia | 77.9 |
| 4db1f936-82f7-39d5-abde-c3b8ab44bc71 | -1.6195 | -46.8946 | 2024-11-24 02:00:00 | GOES-16 | SANTA LUZIA DO PARÁ | PARÁ | Brasil | 1506559 | 15 | 33 | nan | nan | nan | Amazônia | 78.9 |
| 2cbc73dd-cb3a-306c-87bf-8b1612d4d4f4 | -1.5129 | -54.1759 | 2024-11-24 02:00:00 | GOES-16 | MONTE ALEGRE | PARÁ | Brasil | 1504802 | 15 | 33 | nan | nan | nan | Amazônia | 81.4 |
| 5feb4560-b62e-3859-ba1b-2772dcec7cb6 | -3.5158 | -53.8333 | 2024-11-24 02:00:00 | GOES-16 | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | 58.9 |
| 3bef0893-4ad2-36fb-9cab-5731326dd4a7 | -2.9612 | -45.1221 | 2024-11-24 02:10:00 | GOES-16 | VIANA | MARANHÃO | Brasil | 2112803 | 21 | 33 | nan | nan | nan | Amazônia | 73.6 |
| fa27b080-8b4b-36a6-ac6d-f6c1413c383b | -3.054 | -49.4471 | 2024-11-24 02:10:00 | GOES-16 | MOJU | PARÁ | Brasil | 1504703 | 15 | 33 | nan | nan | nan | Amazônia | 47.3 |
| 6edabf63-4d56-3fd8-b5b7-3717a70f036b | -4.242 | -48.6978 | 2024-11-24 02:10:00 | GOES-16 | RONDON DO PARÁ | PARÁ | Brasil | 1506187 | 15 | 33 | nan | nan | nan | Amazônia | 62.8 |
| be2aeede-c950-39d0-8267-4832898160a3 | -5.1185 | -43.1497 | 2024-11-24 02:10:00 | GOES-16 | TIMON | MARANHÃO | Brasil | 2112209 | 21 | 33 | nan | nan | nan | Cerrado | 63.5 |
| 29b5320e-2c0f-35d9-bf9b-ad7e91ec5966 | -3.0355 | -49.4476 | 2024-11-24 02:10:00 | GOES-16 | MOJU | PARÁ | Brasil | 1504703 | 15 | 33 | nan | nan | nan | Amazônia | 78.0 |
| 1aae35b7-2bac-3bf0-b831-2e7898a66bac | -2.2137 | -46.3965 | 2024-11-24 02:10:00 | GOES-16 | CACHOEIRA DO PIRIÁ | PARÁ | Brasil | 1501956 | 15 | 33 | nan | nan | nan | Amazônia | 56.8 |
| cd64f8cf-4bd2-38ef-adbf-4ca0d2ae6597 | -5.0998 | -43.151 | 2024-11-24 02:10:00 | GOES-16 | CAXIAS | MARANHÃO | Brasil | 2103000 | 21 | 33 | nan | nan | nan | Cerrado | 62.6 |
| 31dee09d-f3d8-3131-9eb6-32be64b71b95 | -1.601 | -46.8729 | 2024-11-24 02:10:00 | GOES-16 | SANTA LUZIA DO PARÁ | PARÁ | Brasil | 1506559 | 15 | 33 | nan | nan | nan | Amazônia | 60.2 |
| 7215b996-0d4a-3ba5-969d-b6cc66b4d84b | -3.5158 | -53.8333 | 2024-11-24 02:10:00 | GOES-16 | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | 57.2 |
| 8f7e52dc-7ff2-3bd5-9d3d-e7e84db1d5c1 | -1.6195 | -46.8726 | 2024-11-24 02:10:00 | GOES-16 | SANTA LUZIA DO PARÁ | PARÁ | Brasil | 1506559 | 15 | 33 | nan | nan | nan | Amazônia | 57.5 |
| 37d22ec4-5155-3d7d-bdea-1ed4b9c0b69d | -1.5129 | -54.1959 | 2024-11-24 02:10:00 | GOES-16 | MONTE ALEGRE | PARÁ | Brasil | 1504802 | 15 | 33 | nan | nan | nan | Amazônia | 83.0 |
| f54fa038-571d-3275-9c69-0e89ae44abe7 | -3.2928 | -45.7384 | 2024-11-24 02:10:00 | GOES-16 | ZÉ DOCA | MARANHÃO | Brasil | 2114007 | 21 | 33 | nan | nan | nan | Amazônia | 69.5 |
| 6db4111f-1a97-3e0d-93e9-81419ba7a4a6 | -1.5129 | -54.1759 | 2024-11-24 02:10:00 | GOES-16 | MONTE ALEGRE | PARÁ | Brasil | 1504802 | 15 | 33 | nan | nan | nan | Amazônia | 73.2 |
| 9e2a03c4-1777-3d35-817b-4151ed53c91b | -3.5159 | -53.8132 | 2024-11-24 02:10:00 | GOES-16 | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | 110.7 |
| b3b4ef2a-02f5-3ebf-899e-ae2aa49250a4 | -3.0582 | -53.2192 | 2024-11-24 02:10:00 | GOES-16 | MEDICILÂNDIA | PARÁ | Brasil | 1504455 | 15 | 33 | nan | nan | nan | Amazônia | 71.7 |
| 6e893fc8-0cba-3dc1-820c-1eb20c0e5e91 | -1.6195 | -46.8946 | 2024-11-24 02:10:00 | GOES-16 | SANTA LUZIA DO PARÁ | PARÁ | Brasil | 1506559 | 15 | 33 | nan | nan | nan | Amazônia | 53.3 |
| 83e98160-1e9a-38e8-8838-9a5d50d8852b | -1.601 | -46.8949 | 2024-11-24 02:10:00 | GOES-16 | SANTA LUZIA DO PARÁ | PARÁ | Brasil | 1506559 | 15 | 33 | nan | nan | nan | Amazônia | 55.7 |
| e09d5ccd-9e9e-3cc2-9835-9eafd627ec52 | -3.4698 | -43.8931 | 2024-11-24 02:10:00 | GOES-16 | NINA RODRIGUES | MARANHÃO | Brasil | 2107209 | 21 | 33 | nan | nan | nan | Cerrado | 81.8 |
| 1beeb94d-6575-3893-a526-36bdd1fdfe68 | -5.9557 | -48.0425 | 2024-11-24 02:10:00 | GOES-16 | SÃO BENTO DO TOCANTINS | TOCANTINS | Brasil | 1720101 | 17 | 33 | nan | nan | nan | Cerrado | 76.8 |
| 58fb72d4-5a0f-3c07-8d72-123fb339c03f | -4.242 | -48.6978 | 2024-11-24 02:20:00 | GOES-16 | RONDON DO PARÁ | PARÁ | Brasil | 1506187 | 15 | 33 | nan | nan | nan | Amazônia | 71.1 |
| 707a66d8-cef3-31e5-b1e0-bc96c02e17e1 | -5.0998 | -43.151 | 2024-11-24 02:20:00 | GOES-16 | CAXIAS | MARANHÃO | Brasil | 2103000 | 21 | 33 | nan | nan | nan | Cerrado | 74.5 |
| ac6d10d9-63cc-3dcb-8bcc-d7e2778c1e29 | -3.2929 | -45.7161 | 2024-11-24 02:20:00 | GOES-16 | ZÉ DOCA | MARANHÃO | Brasil | 2114007 | 21 | 33 | nan | nan | nan | Amazônia | 51.1 |
| 753bdee4-09a3-351a-8e90-9688957cc4db | -5.9557 | -48.0425 | 2024-11-24 02:20:00 | GOES-16 | SÃO BENTO DO TOCANTINS | TOCANTINS | Brasil | 1720101 | 17 | 33 | nan | nan | nan | Cerrado | 79.4 |
| b8e7391a-547f-31e4-94de-cdd1a2ad1c02 | -3.4698 | -43.8931 | 2024-11-24 02:20:00 | GOES-16 | NINA RODRIGUES | MARANHÃO | Brasil | 2107209 | 21 | 33 | nan | nan | nan | Cerrado | 54.0 |
| 32d0a8f5-632a-3a9a-9490-076fbb9b0cdc | -1.601 | -46.8949 | 2024-11-24 02:20:00 | GOES-16 | SANTA LUZIA DO PARÁ | PARÁ | Brasil | 1506559 | 15 | 33 | nan | nan | nan | Amazônia | 50.0 |
| 18b404de-68b2-36a8-b710-2f5fef67ef60 | -3.5159 | -53.8132 | 2024-11-24 02:20:00 | GOES-16 | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | 98.5 |
| 1d113988-1ed6-351f-b906-1aec13904957 | -1.601 | -46.8729 | 2024-11-24 02:20:00 | GOES-16 | SANTA LUZIA DO PARÁ | PARÁ | Brasil | 1506559 | 15 | 33 | nan | nan | nan | Amazônia | 65.9 |
| 3b6d8b7f-865a-39d9-8e5c-69ae116f5a99 | -1.3666 | -53.8362 | 2024-11-24 02:20:00 | GOES-16 | MONTE ALEGRE | PARÁ | Brasil | 1504802 | 15 | 33 | nan | nan | nan | Amazônia | 69.8 |
| 1c3a4ced-8c93-3293-bc83-10133cbf09b2 | -3.2943 | -45.447 | 2024-11-24 02:20:00 | GOES-16 | PENALVA | MARANHÃO | Brasil | 2108306 | 21 | 33 | nan | nan | nan | Amazônia | 51.7 |
| 2ffcd938-cce1-387f-8ace-1066c94fcdf5 | -1.5129 | -54.1959 | 2024-11-24 02:20:00 | GOES-16 | MONTE ALEGRE | PARÁ | Brasil | 1504802 | 15 | 33 | nan | nan | nan | Amazônia | 76.1 |
| e8622947-b50f-3ea0-8569-fca55bb2b5ee | -3.2928 | -45.7384 | 2024-11-24 02:20:00 | GOES-16 | ZÉ DOCA | MARANHÃO | Brasil | 2114007 | 21 | 33 | nan | nan | nan | Amazônia | 65.3 |
| b382e488-3f8b-3ace-823c-76391f8891fb | -1.5129 | -54.1759 | 2024-11-24 02:20:00 | GOES-16 | MONTE ALEGRE | PARÁ | Brasil | 1504802 | 15 | 33 | nan | nan | nan | Amazônia | 68.0 |
| fd9af45e-f56f-3d73-856f-cce219c958a0 | -3.0355 | -49.4476 | 2024-11-24 02:20:00 | GOES-16 | MOJU | PARÁ | Brasil | 1504703 | 15 | 33 | nan | nan | nan | Amazônia | 54.1 |
| 926085cd-45af-3514-a732-8ffafb158a95 | -2.8651 | -45.8437 | 2024-11-24 02:30:00 | GOES-16 | NOVA OLINDA DO MARANHÃO | MARANHÃO | Brasil | 2107357 | 21 | 33 | nan | nan | nan | Amazônia | 56.8 |
| 6dce3782-ebd6-3b01-b1d5-37c9e0c26eec | -3.2943 | -45.447 | 2024-11-24 02:30:00 | GOES-16 | PENALVA | MARANHÃO | Brasil | 2108306 | 21 | 33 | nan | nan | nan | Amazônia | 101.5 |
| 1361aa59-3a47-3cd5-958b-22489e012c73 | -1.5129 | -54.1759 | 2024-11-24 02:30:00 | GOES-16 | MONTE ALEGRE | PARÁ | Brasil | 1504802 | 15 | 33 | nan | nan | nan | Amazônia | 67.0 |
| 5cd0b7d9-10f1-37d6-8328-86eee0b84eca | -4.242 | -48.6978 | 2024-11-24 02:30:00 | GOES-16 | RONDON DO PARÁ | PARÁ | Brasil | 1506187 | 15 | 33 | nan | nan | nan | Amazônia | 63.8 |
| a039c7fa-e0c4-3e82-808d-50a5bb157dde | -3.2944 | -45.4245 | 2024-11-24 02:30:00 | GOES-16 | PENALVA | MARANHÃO | Brasil | 2108306 | 21 | 33 | nan | nan | nan | Amazônia | 52.0 |
| 12fa555c-78b8-3066-be64-0fed59594990 | -3.0582 | -53.2192 | 2024-11-24 02:30:00 | GOES-16 | MEDICILÂNDIA | PARÁ | Brasil | 1504455 | 15 | 33 | nan | nan | nan | Amazônia | 58.2 |
| d95a3d31-49f1-31a9-9aed-7f5076232a80 | -1.5129 | -54.1959 | 2024-11-24 02:30:00 | GOES-16 | MONTE ALEGRE | PARÁ | Brasil | 1504802 | 15 | 33 | nan | nan | nan | Amazônia | 72.9 |
| af43149b-58ca-3e98-85e8-aa52cff3ff75 | -3.4698 | -43.8931 | 2024-11-24 02:30:00 | GOES-16 | NINA RODRIGUES | MARANHÃO | Brasil | 2107209 | 21 | 33 | nan | nan | nan | Cerrado | 52.9 |
| e06f26f3-065e-3245-8b9a-ffb4bf52b428 | -3.2757 | -45.4477 | 2024-11-24 02:30:00 | GOES-16 | PENALVA | MARANHÃO | Brasil | 2108306 | 21 | 33 | nan | nan | nan | Amazônia | 87.4 |
| f3758e13-7bbb-3b93-b292-5b95f403c77a | -5.0998 | -43.151 | 2024-11-24 02:30:00 | GOES-16 | CAXIAS | MARANHÃO | Brasil | 2103000 | 21 | 33 | nan | nan | nan | Cerrado | 65.8 |
| 81301efd-9f7f-3347-a4d9-b82948bf81ff | -3.0355 | -49.4476 | 2024-11-24 02:30:00 | GOES-16 | MOJU | PARÁ | Brasil | 1504703 | 15 | 33 | nan | nan | nan | Amazônia | 65.2 |
| 95582fdc-b4e5-3bfc-9474-7b34f81cc0a5 | -3.5159 | -53.8132 | 2024-11-24 02:30:00 | GOES-16 | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | 93.8 |
| 2678a804-5067-3afa-824b-3f36906c76d9 | -3.5159 | -53.8132 | 2024-11-24 02:40:00 | GOES-16 | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | 104.0 |
| 092dec09-8e0a-3b68-880d-b87cdc8e521f | -2.2137 | -46.3965 | 2024-11-24 02:40:00 | GOES-16 | CACHOEIRA DO PIRIÁ | PARÁ | Brasil | 1501956 | 15 | 33 | nan | nan | nan | Amazônia | 55.5 |
| ed740af4-cb27-3108-906a-89d083ad4a37 | -2.3027 | -53.8825 | 2024-11-24 02:40:00 | GOES-16 | PRAINHA | PARÁ | Brasil | 1506005 | 15 | 33 | nan | nan | nan | Amazônia | 65.4 |
| e90e1856-540e-3818-8172-23a3c1838083 | -3.0582 | -53.2192 | 2024-11-24 02:40:00 | GOES-16 | MEDICILÂNDIA | PARÁ | Brasil | 1504455 | 15 | 33 | nan | nan | nan | Amazônia | 65.4 |
| 8522576e-5a2c-3959-a50e-048d3c59e557 | -4.242 | -48.6978 | 2024-11-24 02:40:00 | GOES-16 | RONDON DO PARÁ | PARÁ | Brasil | 1506187 | 15 | 33 | nan | nan | nan | Amazônia | 74.5 |
| 02e86f71-26c0-35ee-8250-eb784f314d95 | -2.8651 | -45.8437 | 2024-11-24 02:40:00 | GOES-16 | NOVA OLINDA DO MARANHÃO | MARANHÃO | Brasil | 2107357 | 21 | 33 | nan | nan | nan | Amazônia | 92.0 |
| 30e73b1a-1a14-3b0d-a1e2-047369bde5d8 | -3.0355 | -49.4476 | 2024-11-24 02:40:00 | GOES-16 | MOJU | PARÁ | Brasil | 1504703 | 15 | 33 | nan | nan | nan | Amazônia | 78.9 |


[Clique aqui para ver as próximas entradas](README24.md)
