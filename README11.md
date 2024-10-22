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

## Dados Diários - Página 11

| ID | Latitude | Longitude | Data/Hora GMT | Satélite | Município | Estado | País | Município ID | Estado ID | País ID | Dias sem Chuva | Precipitação | Risco de Fogo | Bioma | FRP |
|----|----------|-----------|---------------|----------|-----------|--------|------|--------------|-----------|---------|----------------|--------------|----------------|-------|-----|
| 049931e5-e07f-3ab1-8bdd-93a170063594 | -3.0837 | -51.2708 | 2024-10-22 02:15:24 | GOES-16 | ANAPU | PARÁ | Brasil | 1500859 | 15 | 33 | nan | nan | nan | Amazônia | 63.6 |
| 9aa9ebd4-af32-37b9-8cc1-696dbad4b4ae | -3.0765 | -53.239 | 2024-10-22 02:15:24 | GOES-16 | MEDICILÂNDIA | PARÁ | Brasil | 1504455 | 15 | 33 | nan | nan | nan | Amazônia | 52.7 |
| 40e3f063-4ea4-3ac5-962f-1ed4a2e68d3e | -3.0581 | -53.2395 | 2024-10-22 02:15:24 | GOES-16 | MEDICILÂNDIA | PARÁ | Brasil | 1504455 | 15 | 33 | nan | nan | nan | Amazônia | 54.4 |
| 88175afd-cc80-3e43-80e7-4c47849ea19a | -3.1102 | -54.146 | 2024-10-22 02:15:24 | GOES-16 | SANTARÉM | PARÁ | Brasil | 1506807 | 15 | 33 | nan | nan | nan | Amazônia | 59.0 |
| 11cdfb36-c0c3-3b78-a7f8-aef05d053a6b | -3.1101 | -54.1661 | 2024-10-22 02:15:24 | GOES-16 | SANTARÉM | PARÁ | Brasil | 1506807 | 15 | 33 | nan | nan | nan | Amazônia | 103.6 |
| d21c0531-563e-3ba3-af81-8bf1847783e1 | -3.0918 | -54.1465 | 2024-10-22 02:15:24 | GOES-16 | SANTARÉM | PARÁ | Brasil | 1506807 | 15 | 33 | nan | nan | nan | Amazônia | 57.2 |
| f67e96ca-e979-390d-9092-c750ea4a379b | -4.0163 | -46.0193 | 2024-10-22 02:15:29 | GOES-16 | SANTA LUZIA | MARANHÃO | Brasil | 2110005 | 21 | 33 | nan | nan | nan | Amazônia | 77.4 |
| e0a4f4b9-601d-3fa4-8bcf-fb1831668dab | -3.9977 | -46.0202 | 2024-10-22 02:15:29 | GOES-16 | SANTA LUZIA | MARANHÃO | Brasil | 2110005 | 21 | 33 | nan | nan | nan | Amazônia | 75.3 |
| 38e02004-87eb-34d4-b7ad-6ac8c5808aaa | -4.5572 | -45.8128 | 2024-10-22 02:15:32 | GOES-16 | SANTA LUZIA | MARANHÃO | Brasil | 2110005 | 21 | 33 | nan | nan | nan | Amazônia | 64.7 |
| d4ae4b7f-84e6-3975-bdfb-130a96bb77ed | -4.5759 | -45.8118 | 2024-10-22 02:15:32 | GOES-16 | MARAJÁ DO SENA | MARANHÃO | Brasil | 2106359 | 21 | 33 | nan | nan | nan | Amazônia | 49.4 |
| ff8ddc5d-d93b-3337-8300-0f3d4dd334ac | -4.5574 | -45.7905 | 2024-10-22 02:15:32 | GOES-16 | SANTA LUZIA | MARANHÃO | Brasil | 2110005 | 21 | 33 | nan | nan | nan | Amazônia | 49.2 |
| 205bde7a-0e0b-325d-95f4-5d09226d7c6b | -5.5905 | -44.8687 | 2024-10-22 02:15:38 | GOES-16 | TUNTUM | MARANHÃO | Brasil | 2112308 | 21 | 33 | nan | nan | nan | Cerrado | 66.5 |
| 3c34bc8c-2e37-33e8-8ef4-6646c06e4156 | -7.8245 | -61.3709 | 2024-10-22 02:15:51 | GOES-16 | MANICORÉ | AMAZONAS | Brasil | 1302702 | 13 | 33 | nan | nan | nan | Amazônia | 59.1 |
| 20f03a6a-3863-3137-a76b-2d207bfbe570 | -14.3031 | -59.32 | 2024-10-22 02:16:27 | GOES-16 | CAMPOS DE JÚLIO | MATO GROSSO | Brasil | 5102686 | 51 | 33 | nan | nan | nan | Cerrado | 60.2 |
| 386703d7-61be-31fb-86d0-ed3bea053c8d | -14.3223 | -59.3184 | 2024-10-22 02:16:27 | GOES-16 | CAMPOS DE JÚLIO | MATO GROSSO | Brasil | 5102686 | 51 | 33 | nan | nan | nan | Cerrado | 66.7 |
| ef5f12ae-425e-3a94-8b8f-23ac19c511fd | -1.1834 | -53.6569 | 2024-10-22 02:25:13 | GOES-16 | PRAINHA | PARÁ | Brasil | 1506005 | 15 | 33 | nan | nan | nan | Amazônia | 50.9 |
| 9a7e360b-39e6-340b-ab97-0ba05d761704 | -2.4824 | -49.1233 | 2024-10-22 02:25:20 | GOES-16 | MOJU | PARÁ | Brasil | 1504703 | 15 | 33 | nan | nan | nan | Amazônia | 71.0 |
| cc253171-b303-3d20-be63-bcf0c3521063 | -2.4824 | -49.102 | 2024-10-22 02:25:20 | GOES-16 | MOJU | PARÁ | Brasil | 1504703 | 15 | 33 | nan | nan | nan | Amazônia | 61.5 |
| 7495cb97-9a1a-39f9-a3a0-608a5aff1737 | -2.8668 | -45.4631 | 2024-10-22 02:25:22 | GOES-16 | PEDRO DO ROSÁRIO | MARANHÃO | Brasil | 2108256 | 21 | 33 | nan | nan | nan | Amazônia | 68.8 |
| 82ee593b-aaad-3f67-b6b9-c4f9e52ecbcf | -3.0581 | -53.2598 | 2024-10-22 02:25:24 | GOES-16 | MEDICILÂNDIA | PARÁ | Brasil | 1504455 | 15 | 33 | nan | nan | nan | Amazônia | 56.2 |
| ca83e4bf-3b05-37fd-a196-17e1120d0a7a | -3.0581 | -53.2395 | 2024-10-22 02:25:24 | GOES-16 | MEDICILÂNDIA | PARÁ | Brasil | 1504455 | 15 | 33 | nan | nan | nan | Amazônia | 56.7 |
| 17fbb147-6bbc-327c-b1a0-79a06a47a353 | -3.1137 | -53.1366 | 2024-10-22 02:25:24 | GOES-16 | MEDICILÂNDIA | PARÁ | Brasil | 1504455 | 15 | 33 | nan | nan | nan | Amazônia | 52.4 |
| c318959f-e635-3c31-a2c7-6dc779a9f217 | -3.1101 | -54.1661 | 2024-10-22 02:25:24 | GOES-16 | SANTARÉM | PARÁ | Brasil | 1506807 | 15 | 33 | nan | nan | nan | Amazônia | 69.6 |
| 603dfe28-470e-3f8e-a7cd-104b2a2931a1 | -3.0917 | -54.1666 | 2024-10-22 02:25:24 | GOES-16 | SANTARÉM | PARÁ | Brasil | 1506807 | 15 | 33 | nan | nan | nan | Amazônia | 59.0 |
| ad35c7e7-bdc9-36a0-a3b0-e55d7e7e552c | -3.0765 | -53.239 | 2024-10-22 02:25:24 | GOES-16 | MEDICILÂNDIA | PARÁ | Brasil | 1504455 | 15 | 33 | nan | nan | nan | Amazônia | 52.7 |
| edc59f17-55d2-3153-a7c7-87f9bd7a037a | -3.0765 | -53.2593 | 2024-10-22 02:25:24 | GOES-16 | MEDICILÂNDIA | PARÁ | Brasil | 1504455 | 15 | 33 | nan | nan | nan | Amazônia | 53.5 |
| 07e37520-08ea-3703-96f8-540b09286cf4 | -4.0163 | -46.0193 | 2024-10-22 02:25:29 | GOES-16 | SANTA LUZIA | MARANHÃO | Brasil | 2110005 | 21 | 33 | nan | nan | nan | Amazônia | 104.2 |
| 5f1d7700-d6c0-3fe0-90d3-b526ced7a3ea | -4.0161 | -46.0416 | 2024-10-22 02:25:29 | GOES-16 | SANTA LUZIA | MARANHÃO | Brasil | 2110005 | 21 | 33 | nan | nan | nan | Amazônia | 50.6 |
| 28808353-a63d-3f14-b98f-eb36b6b964cb | -3.9977 | -46.0202 | 2024-10-22 02:25:29 | GOES-16 | SANTA LUZIA | MARANHÃO | Brasil | 2110005 | 21 | 33 | nan | nan | nan | Amazônia | 97.5 |
| d7b68252-97f3-30eb-92f2-d170456b1c20 | -3.9975 | -46.0425 | 2024-10-22 02:25:29 | GOES-16 | ALTO ALEGRE DO PINDARÉ | MARANHÃO | Brasil | 2100477 | 21 | 33 | nan | nan | nan | Amazônia | 45.8 |
| e7c65e76-a69a-3bbc-b1de-34362d1dbe0b | -4.5572 | -45.8128 | 2024-10-22 02:25:32 | GOES-16 | SANTA LUZIA | MARANHÃO | Brasil | 2110005 | 21 | 33 | nan | nan | nan | Amazônia | 52.9 |
| e951f404-59d8-3652-ace0-aa15c84f5ed0 | -5.5905 | -44.8687 | 2024-10-22 02:25:38 | GOES-16 | TUNTUM | MARANHÃO | Brasil | 2112308 | 21 | 33 | nan | nan | nan | Cerrado | 60.1 |
| 8ea4d508-e04e-30eb-b0b8-33910352b388 | -17.6868 | -57.4593 | 2024-10-22 02:26:46 | GOES-16 | POCONÉ | MATO GROSSO | Brasil | 5106505 | 51 | 33 | nan | nan | nan | Pantanal | 50.3 |
| 8b817b43-f98f-3ffb-8097-7d2e7ac6acad | -1.1834 | -53.6569 | 2024-10-22 02:35:13 | GOES-16 | PRAINHA | PARÁ | Brasil | 1506005 | 15 | 33 | nan | nan | nan | Amazônia | 49.5 |
| 2f8b38d6-b880-33b4-9a0d-7663afae12b1 | -2.4824 | -49.1233 | 2024-10-22 02:35:20 | GOES-16 | MOJU | PARÁ | Brasil | 1504703 | 15 | 33 | nan | nan | nan | Amazônia | 58.9 |
| cb13349c-c4ef-397a-b89a-de1279256efe | -3.0765 | -53.239 | 2024-10-22 02:35:24 | GOES-16 | MEDICILÂNDIA | PARÁ | Brasil | 1504455 | 15 | 33 | nan | nan | nan | Amazônia | 52.7 |
| 74ece20f-0a9f-3540-a3b7-a453fe860f1e | -3.0917 | -54.1666 | 2024-10-22 02:35:24 | GOES-16 | SANTARÉM | PARÁ | Brasil | 1506807 | 15 | 33 | nan | nan | nan | Amazônia | 76.3 |
| d02608a2-08e9-3cdd-83b6-eed8039541b4 | -3.1101 | -54.1661 | 2024-10-22 02:35:24 | GOES-16 | SANTARÉM | PARÁ | Brasil | 1506807 | 15 | 33 | nan | nan | nan | Amazônia | 98.7 |
| 5dd73150-7c04-35b9-930d-f84f9fa0868e | -3.1102 | -54.146 | 2024-10-22 02:35:24 | GOES-16 | SANTARÉM | PARÁ | Brasil | 1506807 | 15 | 33 | nan | nan | nan | Amazônia | 56.1 |
| f111c4a6-b6f5-3fd8-9cb4-2f68d2e4c294 | -3.1137 | -53.1366 | 2024-10-22 02:35:24 | GOES-16 | MEDICILÂNDIA | PARÁ | Brasil | 1504455 | 15 | 33 | nan | nan | nan | Amazônia | 52.5 |
| d351e367-ccd6-3afa-bf12-c796dc52600b | -3.9977 | -46.0202 | 2024-10-22 02:35:29 | GOES-16 | SANTA LUZIA | MARANHÃO | Brasil | 2110005 | 21 | 33 | nan | nan | nan | Amazônia | 52.2 |
| 41f81093-a35a-381a-b716-c08fe0b28169 | -4.0163 | -46.0193 | 2024-10-22 02:35:29 | GOES-16 | SANTA LUZIA | MARANHÃO | Brasil | 2110005 | 21 | 33 | nan | nan | nan | Amazônia | 49.3 |
| d25c5a3a-ead7-35f0-af60-73d24a184de5 | -5.5718 | -44.87 | 2024-10-22 02:35:38 | GOES-16 | TUNTUM | MARANHÃO | Brasil | 2112308 | 21 | 33 | nan | nan | nan | Cerrado | 53.1 |
| bc85295b-6143-37be-9bad-18f6037cda2a | -5.5903 | -44.8914 | 2024-10-22 02:35:38 | GOES-16 | TUNTUM | MARANHÃO | Brasil | 2112308 | 21 | 33 | nan | nan | nan | Cerrado | 53.7 |
| 1041139c-3821-389e-840c-d4a2bf43e121 | -5.5905 | -44.8687 | 2024-10-22 02:35:38 | GOES-16 | TUNTUM | MARANHÃO | Brasil | 2112308 | 21 | 33 | nan | nan | nan | Cerrado | 76.0 |
| ae6cc1bf-ad6e-3fb7-8f9a-2da5abcae6e7 | -2.7588 | -49.3285 | 2024-10-22 02:45:22 | GOES-16 | MOJU | PARÁ | Brasil | 1504703 | 15 | 33 | nan | nan | nan | Amazônia | 130.6 |
| e4d549ee-1324-32ba-9afb-eaaa3d21b9d5 | -2.7589 | -49.3072 | 2024-10-22 02:45:22 | GOES-16 | MOJU | PARÁ | Brasil | 1504703 | 15 | 33 | nan | nan | nan | Amazônia | 91.9 |
| ae378655-283c-3388-9906-f10372725bf8 | -2.7773 | -49.3279 | 2024-10-22 02:45:22 | GOES-16 | MOJU | PARÁ | Brasil | 1504703 | 15 | 33 | nan | nan | nan | Amazônia | 53.0 |
| f9acd97d-2ac5-3951-9898-a393d73eee3d | -3.11 | -54.1862 | 2024-10-22 02:45:24 | GOES-16 | SANTARÉM | PARÁ | Brasil | 1506807 | 15 | 33 | nan | nan | nan | Amazônia | 81.1 |
| a4212784-5993-3303-bc13-c110f8098858 | -3.1101 | -54.1661 | 2024-10-22 02:45:24 | GOES-16 | SANTARÉM | PARÁ | Brasil | 1506807 | 15 | 33 | nan | nan | nan | Amazônia | 162.7 |
| ef3e5c78-b3c1-38b7-86ed-9db3720cc3ee | -3.1102 | -54.146 | 2024-10-22 02:45:24 | GOES-16 | SANTARÉM | PARÁ | Brasil | 1506807 | 15 | 33 | nan | nan | nan | Amazônia | 76.6 |
| 254e95ca-5a04-30c7-97b8-6ff2e481dbc3 | -3.1137 | -53.1366 | 2024-10-22 02:45:24 | GOES-16 | MEDICILÂNDIA | PARÁ | Brasil | 1504455 | 15 | 33 | nan | nan | nan | Amazônia | 52.8 |
| 9b9630b3-9540-3659-a3dd-65003b0b1df6 | -3.0917 | -54.1867 | 2024-10-22 02:45:24 | GOES-16 | SANTARÉM | PARÁ | Brasil | 1506807 | 15 | 33 | nan | nan | nan | Amazônia | 68.0 |
| 057af842-ac64-3890-9987-6af61ae06a4d | -3.0917 | -54.1666 | 2024-10-22 02:45:24 | GOES-16 | SANTARÉM | PARÁ | Brasil | 1506807 | 15 | 33 | nan | nan | nan | Amazônia | 123.9 |
| 0038e100-11a8-3c44-be20-de6fe2e30da7 | -3.0918 | -54.1465 | 2024-10-22 02:45:24 | GOES-16 | SANTARÉM | PARÁ | Brasil | 1506807 | 15 | 33 | nan | nan | nan | Amazônia | 68.0 |
| dd0258a6-70a7-39a8-9fb7-3dc864d52b0f | -3.9977 | -46.0202 | 2024-10-22 02:45:29 | GOES-16 | SANTA LUZIA | MARANHÃO | Brasil | 2110005 | 21 | 33 | nan | nan | nan | Amazônia | 67.4 |
| dc1de165-3c41-3daa-9bdb-06b42d6216a9 | -4.0163 | -46.0193 | 2024-10-22 02:45:29 | GOES-16 | SANTA LUZIA | MARANHÃO | Brasil | 2110005 | 21 | 33 | nan | nan | nan | Amazônia | 65.0 |
| d4485950-1609-392f-ada0-e54ab9024408 | -4.5572 | -45.8128 | 2024-10-22 02:45:32 | GOES-16 | SANTA LUZIA | MARANHÃO | Brasil | 2110005 | 21 | 33 | nan | nan | nan | Amazônia | 56.3 |
| e07f7f1c-ea88-3ef5-b200-f8c6b4d1852d | -5.5716 | -44.8927 | 2024-10-22 02:45:38 | GOES-16 | TUNTUM | MARANHÃO | Brasil | 2112308 | 21 | 33 | nan | nan | nan | Cerrado | 46.7 |
| 8e84741b-c32b-3a7f-ba35-36c1de8e2951 | -5.5718 | -44.87 | 2024-10-22 02:45:38 | GOES-16 | TUNTUM | MARANHÃO | Brasil | 2112308 | 21 | 33 | nan | nan | nan | Cerrado | 62.4 |
| 861a13b0-62fe-358b-a7fb-1e75838cf07d | -5.5903 | -44.8914 | 2024-10-22 02:45:38 | GOES-16 | TUNTUM | MARANHÃO | Brasil | 2112308 | 21 | 33 | nan | nan | nan | Cerrado | 65.5 |
| 2c89c867-3af2-3428-9daa-fd06274bcb8b | -5.5905 | -44.8687 | 2024-10-22 02:45:38 | GOES-16 | TUNTUM | MARANHÃO | Brasil | 2112308 | 21 | 33 | nan | nan | nan | Cerrado | 90.4 |
| 3e524c09-b323-3862-b7eb-1d947c944f87 | -14.3218 | -59.3581 | 2024-10-22 02:46:27 | GOES-16 | CAMPOS DE JÚLIO | MATO GROSSO | Brasil | 5102686 | 51 | 33 | nan | nan | nan | Cerrado | 75.8 |
| 2cdb17ce-126c-32da-911c-36920fd2e826 | -14.322 | -59.3382 | 2024-10-22 02:46:27 | GOES-16 | CAMPOS DE JÚLIO | MATO GROSSO | Brasil | 5102686 | 51 | 33 | nan | nan | nan | Cerrado | 101.4 |
| a84881a1-2a86-35f9-b37e-ecf2c81303d2 | -14.3412 | -59.3366 | 2024-10-22 02:46:28 | GOES-16 | CAMPOS DE JÚLIO | MATO GROSSO | Brasil | 5102686 | 51 | 33 | nan | nan | nan | Cerrado | 78.4 |
| 8595cfc7-81eb-3d2d-8eab-6dc1580e87ee | -14.341 | -59.3565 | 2024-10-22 02:46:28 | GOES-16 | CAMPOS DE JÚLIO | MATO GROSSO | Brasil | 5102686 | 51 | 33 | nan | nan | nan | Cerrado | 58.6 |
| 35c4fb50-1dfb-38bd-ba86-f37e036c96e0 | -17.0184 | -57.5178 | 2024-10-22 02:46:42 | GOES-16 | CÁCERES | MATO GROSSO | Brasil | 5102504 | 51 | 33 | nan | nan | nan | Pantanal | 74.6 |
| c26af6f8-f138-32e9-968c-2b6f5b1a62e2 | -17.6868 | -57.4593 | 2024-10-22 02:46:46 | GOES-16 | POCONÉ | MATO GROSSO | Brasil | 5106505 | 51 | 33 | nan | nan | nan | Pantanal | 65.0 |
| fe89bb23-336c-31e1-8aa2-97cb91038572 | -1.165 | -53.6571 | 2024-10-22 02:55:13 | GOES-16 | PRAINHA | PARÁ | Brasil | 1506005 | 15 | 33 | nan | nan | nan | Amazônia | 50.5 |
| 52c68c7b-dde0-3f1d-8763-acf06c6252f9 | -1.1834 | -53.6569 | 2024-10-22 02:55:13 | GOES-16 | PRAINHA | PARÁ | Brasil | 1506005 | 15 | 33 | nan | nan | nan | Amazônia | 48.7 |
| 2d973b4f-b9b6-314d-83b6-f630731d0643 | -3.0765 | -53.2593 | 2024-10-22 02:55:24 | GOES-16 | MEDICILÂNDIA | PARÁ | Brasil | 1504455 | 15 | 33 | nan | nan | nan | Amazônia | 51.5 |
| 4427095c-d12e-3fa4-8797-eee2e13ad93a | -3.0765 | -53.239 | 2024-10-22 02:55:24 | GOES-16 | MEDICILÂNDIA | PARÁ | Brasil | 1504455 | 15 | 33 | nan | nan | nan | Amazônia | 51.2 |
| d1fe1f21-d6e3-3ef8-abaa-78be0af5429b | -3.0917 | -54.1867 | 2024-10-22 02:55:24 | GOES-16 | SANTARÉM | PARÁ | Brasil | 1506807 | 15 | 33 | nan | nan | nan | Amazônia | 78.3 |
| 09d31f7f-6482-334a-b0fe-295705351642 | -3.0917 | -54.1666 | 2024-10-22 02:55:24 | GOES-16 | SANTARÉM | PARÁ | Brasil | 1506807 | 15 | 33 | nan | nan | nan | Amazônia | 151.3 |
| 66df48d0-278d-30e5-8541-e692156e7be8 | -3.0918 | -54.1465 | 2024-10-22 02:55:24 | GOES-16 | SANTARÉM | PARÁ | Brasil | 1506807 | 15 | 33 | nan | nan | nan | Amazônia | 75.5 |
| b051574d-8dd1-3041-a5de-6d44b4716093 | -3.11 | -54.1862 | 2024-10-22 02:55:24 | GOES-16 | SANTARÉM | PARÁ | Brasil | 1506807 | 15 | 33 | nan | nan | nan | Amazônia | 70.5 |
| f9884a32-01b1-311c-b361-85ccf5151b49 | -3.1101 | -54.1661 | 2024-10-22 02:55:24 | GOES-16 | SANTARÉM | PARÁ | Brasil | 1506807 | 15 | 33 | nan | nan | nan | Amazônia | 134.8 |
| ef836984-20d0-3135-ad0a-1086dbaf85e4 | -3.1102 | -54.146 | 2024-10-22 02:55:24 | GOES-16 | SANTARÉM | PARÁ | Brasil | 1506807 | 15 | 33 | nan | nan | nan | Amazônia | 70.0 |
| 6819ec40-e612-3815-8310-2700d2cad22c | -4.0163 | -46.0193 | 2024-10-22 02:55:29 | GOES-16 | SANTA LUZIA | MARANHÃO | Brasil | 2110005 | 21 | 33 | nan | nan | nan | Amazônia | 76.8 |
| d5c72c48-7ace-33be-ac66-0b2108f0b662 | -4.5572 | -45.8128 | 2024-10-22 02:55:32 | GOES-16 | SANTA LUZIA | MARANHÃO | Brasil | 2110005 | 21 | 33 | nan | nan | nan | Amazônia | 64.7 |
| 8003272f-614f-3358-9a99-e8bdb2c7b4d6 | -5.5716 | -44.8927 | 2024-10-22 02:55:38 | GOES-16 | TUNTUM | MARANHÃO | Brasil | 2112308 | 21 | 33 | nan | nan | nan | Cerrado | 47.1 |
| 7016a7ae-9f88-3c8e-9444-d8ab1403628a | -5.5718 | -44.87 | 2024-10-22 02:55:38 | GOES-16 | TUNTUM | MARANHÃO | Brasil | 2112308 | 21 | 33 | nan | nan | nan | Cerrado | 78.1 |
| 41e76002-195d-3b13-ad4e-f4a95d52715d | -5.5903 | -44.8914 | 2024-10-22 02:55:38 | GOES-16 | TUNTUM | MARANHÃO | Brasil | 2112308 | 21 | 33 | nan | nan | nan | Cerrado | 57.1 |
| a791a761-20e7-3af9-904d-af0078eb0501 | -5.5905 | -44.8687 | 2024-10-22 02:55:38 | GOES-16 | TUNTUM | MARANHÃO | Brasil | 2112308 | 21 | 33 | nan | nan | nan | Cerrado | 84.7 |
| 5aecdb8c-b9d7-3508-b25e-37e7a2beb9f2 | -14.322 | -59.3382 | 2024-10-22 02:56:27 | GOES-16 | CAMPOS DE JÚLIO | MATO GROSSO | Brasil | 5102686 | 51 | 33 | nan | nan | nan | Cerrado | 61.8 |
| f9f9dcd0-9a22-30d6-9043-f432f2b7d54a | -14.341 | -59.3565 | 2024-10-22 02:56:28 | GOES-16 | CAMPOS DE JÚLIO | MATO GROSSO | Brasil | 5102686 | 51 | 33 | nan | nan | nan | Cerrado | 73.2 |
| 33d392af-c5df-323d-8d62-5c1a4c4b3cfd | -14.3412 | -59.3366 | 2024-10-22 02:56:28 | GOES-16 | CAMPOS DE JÚLIO | MATO GROSSO | Brasil | 5102686 | 51 | 33 | nan | nan | nan | Cerrado | 113.7 |
| d6bf46f9-d66b-3e6a-994b-c7f9be13853f | -18.3019 | -56.1386 | 2024-10-22 02:56:49 | GOES-16 | CORUMBÁ | MATO GROSSO DO SUL | Brasil | 5003207 | 50 | 33 | nan | nan | nan | Pantanal | 69.9 |
| d9645c93-bb83-3ee4-84cd-0566e1811fa2 | -18.4422 | -52.0928 | 2024-10-22 02:56:49 | GOES-16 | SERRANÓPOLIS | GOIÁS | Brasil | 5220504 | 52 | 33 | nan | nan | nan | Cerrado | 78.8 |
| d33f4b9c-9a2f-34f8-ab20-e791ddfc92e5 | -1.1834 | -53.6569 | 2024-10-22 03:05:13 | GOES-16 | PRAINHA | PARÁ | Brasil | 1506005 | 15 | 33 | nan | nan | nan | Amazônia | 54.2 |
| b9b07f2e-020c-39d6-87a5-3c480cfefe1e | -2.7588 | -49.3285 | 2024-10-22 03:05:22 | GOES-16 | MOJU | PARÁ | Brasil | 1504703 | 15 | 33 | nan | nan | nan | Amazônia | 102.8 |
| 369256f9-5065-30cf-9d1f-d0b8be9ac3b8 | -2.7589 | -49.3072 | 2024-10-22 03:05:22 | GOES-16 | MOJU | PARÁ | Brasil | 1504703 | 15 | 33 | nan | nan | nan | Amazônia | 87.5 |
| 7137e980-cc30-30d3-a600-c6b52955ad79 | -2.7773 | -49.3279 | 2024-10-22 03:05:22 | GOES-16 | MOJU | PARÁ | Brasil | 1504703 | 15 | 33 | nan | nan | nan | Amazônia | 64.7 |
| e98e5138-e1b5-3ec4-af9b-ba024a7bc9b1 | -2.7773 | -49.3067 | 2024-10-22 03:05:22 | GOES-16 | MOJU | PARÁ | Brasil | 1504703 | 15 | 33 | nan | nan | nan | Amazônia | 58.6 |
| 01411038-1662-36c1-93c1-6752862b4d0a | -3.1102 | -54.146 | 2024-10-22 03:05:24 | GOES-16 | SANTARÉM | PARÁ | Brasil | 1506807 | 15 | 33 | nan | nan | nan | Amazônia | 68.0 |
| 3b3f8061-4807-3f92-8371-a3a632024f62 | -3.1101 | -54.1661 | 2024-10-22 03:05:24 | GOES-16 | SANTARÉM | PARÁ | Brasil | 1506807 | 15 | 33 | nan | nan | nan | Amazônia | 141.8 |
| a2674585-2e28-310f-969f-752286dc771c | -3.0917 | -54.1666 | 2024-10-22 03:05:24 | GOES-16 | SANTARÉM | PARÁ | Brasil | 1506807 | 15 | 33 | nan | nan | nan | Amazônia | 130.4 |
| 5c2644ed-1722-3abd-a9e1-3f54bc6b69c3 | -3.0918 | -54.1465 | 2024-10-22 03:05:24 | GOES-16 | SANTARÉM | PARÁ | Brasil | 1506807 | 15 | 33 | nan | nan | nan | Amazônia | 77.8 |
| 9714c864-35eb-352d-bb42-af397b4b4839 | -3.11 | -54.1862 | 2024-10-22 03:05:24 | GOES-16 | SANTARÉM | PARÁ | Brasil | 1506807 | 15 | 33 | nan | nan | nan | Amazônia | 73.7 |
| c19ed83f-96fc-3b83-a239-0e61696302b7 | -4.0163 | -46.0193 | 2024-10-22 03:05:29 | GOES-16 | SANTA LUZIA | MARANHÃO | Brasil | 2110005 | 21 | 33 | nan | nan | nan | Amazônia | 71.4 |


[Clique aqui para ver as próximas entradas](README12.md)
