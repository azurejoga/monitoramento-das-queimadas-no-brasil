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

## Dados Diários - Página 2

| ID | Latitude | Longitude | Data/Hora GMT | Satélite | Município | Estado | País | Município ID | Estado ID | País ID | Dias sem Chuva | Precipitação | Risco de Fogo | Bioma | FRP |
|----|----------|-----------|---------------|----------|-----------|--------|------|--------------|-----------|---------|----------------|--------------|----------------|-------|-----|
| 9edf7a0e-d82a-3393-b709-0b7f11fd1f11 | -3.6754 | -43.8143 | 2025-12-10 01:30:00 | GOES-19 | VARGEM GRANDE | MARANHÃO | Brasil | 2112704 | 21 | 33 | nan | nan | nan | Cerrado | 89.3 |
| a7a552c6-f257-39a8-8f57-527e42d7db9e | -5.1562 | -43.1237 | 2025-12-10 01:30:00 | GOES-19 | TIMON | MARANHÃO | Brasil | 2112209 | 21 | 33 | nan | nan | nan | Cerrado | 89.5 |
| 3d2eccc1-9338-3d42-b725-fc6c3bec956b | -2.2646 | -47.8617 | 2025-12-10 01:30:00 | GOES-19 | AURORA DO PARÁ | PARÁ | Brasil | 1500958 | 15 | 33 | nan | nan | nan | Amazônia | 49.0 |
| 30813a0b-62ba-33cc-9f5f-2bfe8f80b470 | -5.1749 | -43.1224 | 2025-12-10 01:30:00 | GOES-19 | TIMON | MARANHÃO | Brasil | 2112209 | 21 | 33 | nan | nan | nan | Cerrado | 121.3 |
| 4869d744-f6b5-3c4e-b1bb-91259fd2c9c0 | -3.694 | -43.8134 | 2025-12-10 01:30:00 | GOES-19 | VARGEM GRANDE | MARANHÃO | Brasil | 2112704 | 21 | 33 | nan | nan | nan | Cerrado | 142.0 |
| 01840c5b-211f-3f17-bad3-27701d2633c7 | -3.6752 | -43.8374 | 2025-12-10 01:30:00 | GOES-19 | VARGEM GRANDE | MARANHÃO | Brasil | 2112704 | 21 | 33 | nan | nan | nan | Cerrado | 74.5 |
| a628e6b0-a4af-3180-abba-cb132b427dea | -2.487 | -47.7692 | 2025-12-10 01:30:00 | GOES-19 | IPIXUNA DO PARÁ | PARÁ | Brasil | 1503457 | 15 | 33 | nan | nan | nan | Amazônia | 69.2 |
| 41dbd8b7-1483-3fdd-b867-64de21911646 | -3.759 | -45.4719 | 2025-12-10 01:30:00 | GOES-19 | PINDARÉ-MIRIM | MARANHÃO | Brasil | 2108504 | 21 | 33 | nan | nan | nan | Amazônia | 51.8 |
| e9445ed3-a8f2-3688-b7c6-7fb2a5452d68 | -2.4869 | -47.7909 | 2025-12-10 01:30:00 | GOES-19 | IPIXUNA DO PARÁ | PARÁ | Brasil | 1503457 | 15 | 33 | nan | nan | nan | Amazônia | 54.2 |
| 57aab1fc-5c6e-335d-9895-bec3014941ef | -3.6939 | -43.8365 | 2025-12-10 01:30:00 | GOES-19 | VARGEM GRANDE | MARANHÃO | Brasil | 2112704 | 21 | 33 | nan | nan | nan | Cerrado | 106.9 |
| 89667ceb-6c98-3d74-adaa-6232187f8661 | -4.4497 | -42.5123 | 2025-12-10 01:40:00 | GOES-19 | LAGOA ALEGRE | PIAUÍ | Brasil | 2205557 | 22 | 33 | nan | nan | nan | Caatinga | 58.3 |
| caf17033-9056-351d-a148-ccbc6197e96d | -5.1749 | -43.1224 | 2025-12-10 01:40:00 | GOES-19 | TIMON | MARANHÃO | Brasil | 2112209 | 21 | 33 | nan | nan | nan | Cerrado | 84.3 |
| 1d1cdb16-7b0b-3cb3-b176-114b16e2aa71 | -3.694 | -43.8134 | 2025-12-10 01:40:00 | GOES-19 | VARGEM GRANDE | MARANHÃO | Brasil | 2112704 | 21 | 33 | nan | nan | nan | Cerrado | 147.7 |
| 6b9dc535-d4e4-3ccd-a93f-ddf5b750128e | -3.6752 | -43.8374 | 2025-12-10 01:40:00 | GOES-19 | VARGEM GRANDE | MARANHÃO | Brasil | 2112704 | 21 | 33 | nan | nan | nan | Cerrado | 71.3 |
| f46229bf-0fa3-3eb5-a310-ef061a1c01e6 | -3.6939 | -43.8365 | 2025-12-10 01:40:00 | GOES-19 | VARGEM GRANDE | MARANHÃO | Brasil | 2112704 | 21 | 33 | nan | nan | nan | Cerrado | 114.6 |
| b637f093-e1c4-32cd-a55e-1b96799fb3e3 | -4.4495 | -42.5359 | 2025-12-10 01:40:00 | GOES-19 | LAGOA ALEGRE | PIAUÍ | Brasil | 2205557 | 22 | 33 | nan | nan | nan | Caatinga | 58.1 |
| 0e7b9624-8432-3fca-92e3-8d124473878f | -2.487 | -47.7692 | 2025-12-10 01:40:00 | GOES-19 | IPIXUNA DO PARÁ | PARÁ | Brasil | 1503457 | 15 | 33 | nan | nan | nan | Amazônia | 69.0 |
| 67626bb9-09fb-3b4e-a00a-f0a8900b9793 | -2.2646 | -47.8617 | 2025-12-10 01:40:00 | GOES-19 | AURORA DO PARÁ | PARÁ | Brasil | 1500958 | 15 | 33 | nan | nan | nan | Amazônia | 54.3 |
| 68c0dace-6289-327c-8e7e-e1c2ce3153b1 | -3.6754 | -43.8143 | 2025-12-10 01:40:00 | GOES-19 | VARGEM GRANDE | MARANHÃO | Brasil | 2112704 | 21 | 33 | nan | nan | nan | Cerrado | 86.0 |
| 3f2d7092-a846-38dd-9f6f-1eb611719371 | -3.6939 | -43.8365 | 2025-12-10 01:50:00 | GOES-19 | VARGEM GRANDE | MARANHÃO | Brasil | 2112704 | 21 | 33 | nan | nan | nan | Cerrado | 108.3 |
| be538f51-74c2-3f1e-a0e0-8e2ca0bd0b9e | -3.759 | -45.4719 | 2025-12-10 01:50:00 | GOES-19 | PINDARÉ-MIRIM | MARANHÃO | Brasil | 2108504 | 21 | 33 | nan | nan | nan | Amazônia | 69.2 |
| 76a305f4-2abc-3d7f-b85b-459ba238df54 | -3.6754 | -43.8143 | 2025-12-10 01:50:00 | GOES-19 | VARGEM GRANDE | MARANHÃO | Brasil | 2112704 | 21 | 33 | nan | nan | nan | Cerrado | 74.2 |
| 727fdd2a-2536-3beb-bd3f-b44ebf732cd1 | -3.7404 | -45.4728 | 2025-12-10 01:50:00 | GOES-19 | PINDARÉ-MIRIM | MARANHÃO | Brasil | 2108504 | 21 | 33 | nan | nan | nan | Amazônia | 47.1 |
| 651ffed5-aa2d-3fec-b63e-224556ea86d6 | -3.694 | -43.8134 | 2025-12-10 01:50:00 | GOES-19 | VARGEM GRANDE | MARANHÃO | Brasil | 2112704 | 21 | 33 | nan | nan | nan | Cerrado | 137.9 |
| bd00f202-209a-35a7-8d9b-212a62eae4fc | -10.0235 | -36.4589 | 2025-12-10 01:50:00 | GOES-19 | TEOTÔNIO VILELA | ALAGOAS | Brasil | 2709152 | 27 | 33 | nan | nan | nan | Mata Atlântica | 69.0 |
| 30e2c2ae-3d23-3aeb-9378-bf8d2c43fd54 | -3.6752 | -43.8374 | 2025-12-10 01:50:00 | GOES-19 | VARGEM GRANDE | MARANHÃO | Brasil | 2112704 | 21 | 33 | nan | nan | nan | Cerrado | 65.1 |
| 088d4dc6-5c17-3218-9d56-374744967ad0 | -2.487 | -47.7692 | 2025-12-10 01:50:00 | GOES-19 | IPIXUNA DO PARÁ | PARÁ | Brasil | 1503457 | 15 | 33 | nan | nan | nan | Amazônia | 57.1 |
| d6145eb9-910d-3d0a-82a9-b7b486448144 | -9.8191 | -36.0636 | 2025-12-10 02:00:00 | GOES-19 | SÃO MIGUEL DOS CAMPOS | ALAGOAS | Brasil | 2708600 | 27 | 33 | nan | nan | nan | Mata Atlântica | 106.7 |
| 0941dff0-536b-38a3-95a5-2e4348e89e04 | -3.694 | -43.8134 | 2025-12-10 02:00:00 | GOES-19 | VARGEM GRANDE | MARANHÃO | Brasil | 2112704 | 21 | 33 | nan | nan | nan | Cerrado | 111.6 |
| 83997414-b013-3902-b7aa-ea3498f18f6b | -5.1562 | -43.1237 | 2025-12-10 02:00:00 | GOES-19 | TIMON | MARANHÃO | Brasil | 2112209 | 21 | 33 | nan | nan | nan | Cerrado | 68.0 |
| 370ef026-372f-3618-ad32-fe3d2c602bf7 | -3.6754 | -43.8143 | 2025-12-10 02:00:00 | GOES-19 | VARGEM GRANDE | MARANHÃO | Brasil | 2112704 | 21 | 33 | nan | nan | nan | Cerrado | 73.4 |
| 6aa2c110-1ca9-39c6-8c9f-9d3cb5efde3c | -5.1749 | -43.1224 | 2025-12-10 02:00:00 | GOES-19 | TIMON | MARANHÃO | Brasil | 2112209 | 21 | 33 | nan | nan | nan | Cerrado | 99.0 |
| 0beaf16b-5f44-3c64-bab2-4e2b291a874b | -3.759 | -45.4719 | 2025-12-10 02:00:00 | GOES-19 | PINDARÉ-MIRIM | MARANHÃO | Brasil | 2108504 | 21 | 33 | nan | nan | nan | Amazônia | 51.4 |
| 45c9b397-fd20-3bc3-a730-b1f29932dd72 | -3.6939 | -43.8365 | 2025-12-10 02:00:00 | GOES-19 | VARGEM GRANDE | MARANHÃO | Brasil | 2112704 | 21 | 33 | nan | nan | nan | Cerrado | 92.7 |
| fd2327dc-ad6c-3447-8c3a-cd11a89ebe14 | -2.487 | -47.7692 | 2025-12-10 02:00:00 | GOES-19 | IPIXUNA DO PARÁ | PARÁ | Brasil | 1503457 | 15 | 33 | nan | nan | nan | Amazônia | 57.4 |
| 814e7061-9300-3be3-80a0-f6fc939b2abe | -2.8863 | -45.2375 | 2025-12-10 02:00:00 | GOES-19 | PEDRO DO ROSÁRIO | MARANHÃO | Brasil | 2108256 | 21 | 33 | nan | nan | nan | Amazônia | 43.3 |
| bc09fdcd-28e4-3c54-b797-e6d4fb2ad100 | -3.6752 | -43.8374 | 2025-12-10 02:00:00 | GOES-19 | VARGEM GRANDE | MARANHÃO | Brasil | 2112704 | 21 | 33 | nan | nan | nan | Cerrado | 63.6 |
| a9aca50d-a456-31a4-8554-ce8257aa39d4 | 3.3788 | -51.2618 | 2025-12-10 02:00:00 | GOES-19 | OIAPOQUE | AMAPÁ | Brasil | 1600501 | 16 | 33 | nan | nan | nan | Amazônia | 55.7 |
| 35213236-0921-3e43-b923-ffbaa3e8c19b | -3.694 | -43.8134 | 2025-12-10 02:10:00 | GOES-19 | VARGEM GRANDE | MARANHÃO | Brasil | 2112704 | 21 | 33 | nan | nan | nan | Cerrado | 108.7 |
| 33aeacf0-3300-3abb-8499-7ab3415ed521 | -3.6939 | -43.8365 | 2025-12-10 02:10:00 | GOES-19 | VARGEM GRANDE | MARANHÃO | Brasil | 2112704 | 21 | 33 | nan | nan | nan | Cerrado | 83.1 |
| 6b9bdc13-598a-3d29-87fe-114392326164 | -3.6754 | -43.8143 | 2025-12-10 02:10:00 | GOES-19 | VARGEM GRANDE | MARANHÃO | Brasil | 2112704 | 21 | 33 | nan | nan | nan | Cerrado | 66.1 |
| aadb86d1-8375-3a79-becc-9bb33591405b | -2.487 | -47.7692 | 2025-12-10 02:10:00 | GOES-19 | IPIXUNA DO PARÁ | PARÁ | Brasil | 1503457 | 15 | 33 | nan | nan | nan | Amazônia | 61.3 |
| e3936007-2378-3bd3-a118-a00d07130b08 | -2.4869 | -47.7909 | 2025-12-10 02:10:00 | GOES-19 | IPIXUNA DO PARÁ | PARÁ | Brasil | 1503457 | 15 | 33 | nan | nan | nan | Amazônia | 41.5 |
| bfd7d33a-48fd-39dd-9668-4467f3778124 | 3.3788 | -51.2618 | 2025-12-10 02:10:00 | GOES-19 | OIAPOQUE | AMAPÁ | Brasil | 1600501 | 16 | 33 | nan | nan | nan | Amazônia | 46.0 |
| ea567059-1835-38ea-8755-56eee9dc36e5 | -2.8863 | -45.2375 | 2025-12-10 02:10:00 | GOES-19 | PEDRO DO ROSÁRIO | MARANHÃO | Brasil | 2108256 | 21 | 33 | nan | nan | nan | Amazônia | 110.9 |
| 075d5280-f464-3fe1-a390-13769bf07c80 | -2.9049 | -45.2368 | 2025-12-10 02:10:00 | GOES-19 | PEDRO DO ROSÁRIO | MARANHÃO | Brasil | 2108256 | 21 | 33 | nan | nan | nan | Amazônia | 37.7 |
| 163f7feb-b2a8-3a75-a660-3bebdcaaa56c | -2.8862 | -45.26 | 2025-12-10 02:10:00 | GOES-19 | PEDRO DO ROSÁRIO | MARANHÃO | Brasil | 2108256 | 21 | 33 | nan | nan | nan | Amazônia | 38.4 |
| f0ba2dee-aff1-35e1-8141-39d5611540e7 | -5.1749 | -43.1224 | 2025-12-10 02:10:00 | GOES-19 | TIMON | MARANHÃO | Brasil | 2112209 | 21 | 33 | nan | nan | nan | Cerrado | 95.9 |
| 0c1e02d6-8a68-3eef-8d7e-9422aa0a73ac | -3.6939 | -43.8365 | 2025-12-10 02:20:00 | GOES-19 | VARGEM GRANDE | MARANHÃO | Brasil | 2112704 | 21 | 33 | nan | nan | nan | Cerrado | 81.8 |
| ddf8070b-621c-3a78-9ff5-045dd649c457 | -3.694 | -43.8134 | 2025-12-10 02:20:00 | GOES-19 | VARGEM GRANDE | MARANHÃO | Brasil | 2112704 | 21 | 33 | nan | nan | nan | Cerrado | 94.7 |
| fd39447f-d021-3c3b-8bf7-03c7182e8a82 | -2.4869 | -47.7909 | 2025-12-10 02:20:00 | GOES-19 | IPIXUNA DO PARÁ | PARÁ | Brasil | 1503457 | 15 | 33 | nan | nan | nan | Amazônia | 44.9 |
| b7c29ee6-9124-3356-861c-9455f8c057f2 | -5.1749 | -43.1224 | 2025-12-10 02:20:00 | GOES-19 | TIMON | MARANHÃO | Brasil | 2112209 | 21 | 33 | nan | nan | nan | Cerrado | 74.6 |
| ebeeadf6-89e1-35de-8f4c-92d861821ecc | -2.8863 | -45.2375 | 2025-12-10 02:20:00 | GOES-19 | PEDRO DO ROSÁRIO | MARANHÃO | Brasil | 2108256 | 21 | 33 | nan | nan | nan | Amazônia | 65.2 |
| 4a64a0d4-8d54-362a-b3a9-806178af90e9 | 3.3788 | -51.2618 | 2025-12-10 02:20:00 | GOES-19 | OIAPOQUE | AMAPÁ | Brasil | 1600501 | 16 | 33 | nan | nan | nan | Amazônia | 44.8 |
| 7c2302a5-b9e2-3acf-b9c3-a286cb8b8d0d | -3.7404 | -45.4728 | 2025-12-10 02:20:00 | GOES-19 | PINDARÉ-MIRIM | MARANHÃO | Brasil | 2108504 | 21 | 33 | nan | nan | nan | Amazônia | 40.3 |
| 7a302e24-e664-3fba-95b7-11924cd3bfdd | -3.759 | -45.4719 | 2025-12-10 02:20:00 | GOES-19 | PINDARÉ-MIRIM | MARANHÃO | Brasil | 2108504 | 21 | 33 | nan | nan | nan | Amazônia | 49.4 |
| 8cd05a94-3850-3f80-b534-d8152c518a13 | -2.487 | -47.7692 | 2025-12-10 02:20:00 | GOES-19 | IPIXUNA DO PARÁ | PARÁ | Brasil | 1503457 | 15 | 33 | nan | nan | nan | Amazônia | 62.0 |
| d69575fd-428e-35dd-9ff5-077c29970b38 | -3.6939 | -43.8365 | 2025-12-10 02:30:00 | GOES-19 | VARGEM GRANDE | MARANHÃO | Brasil | 2112704 | 21 | 33 | nan | nan | nan | Cerrado | 74.3 |
| f59764d4-512c-395e-aa8d-9f6c2f082696 | -3.694 | -43.8134 | 2025-12-10 02:30:00 | GOES-19 | VARGEM GRANDE | MARANHÃO | Brasil | 2112704 | 21 | 33 | nan | nan | nan | Cerrado | 89.4 |
| 8b339993-de73-3e3a-9eb4-882950928662 | -5.1749 | -43.1224 | 2025-12-10 02:30:00 | GOES-19 | TIMON | MARANHÃO | Brasil | 2112209 | 21 | 33 | nan | nan | nan | Cerrado | 76.6 |
| 4266019c-69db-3be8-897c-266afb46673e | -3.759 | -45.4719 | 2025-12-10 02:30:00 | GOES-19 | PINDARÉ-MIRIM | MARANHÃO | Brasil | 2108504 | 21 | 33 | nan | nan | nan | Amazônia | 53.6 |
| 5eae9ac3-a883-3f07-9a15-31fc196d6f7a | -3.7404 | -45.4728 | 2025-12-10 02:30:00 | GOES-19 | PINDARÉ-MIRIM | MARANHÃO | Brasil | 2108504 | 21 | 33 | nan | nan | nan | Amazônia | 53.8 |
| bb23bccc-287b-348d-bfd9-adfb98c7439b | -2.8863 | -45.2375 | 2025-12-10 02:30:00 | GOES-19 | PEDRO DO ROSÁRIO | MARANHÃO | Brasil | 2108256 | 21 | 33 | nan | nan | nan | Amazônia | 61.2 |
| eeb9d1ac-a78f-3803-9f4e-7643821bfd4f | -3.7404 | -45.4728 | 2025-12-10 02:40:00 | GOES-19 | PINDARÉ-MIRIM | MARANHÃO | Brasil | 2108504 | 21 | 33 | nan | nan | nan | Amazônia | 81.3 |
| 0c517444-9922-3170-a54f-4c209476a562 | -2.8863 | -45.2375 | 2025-12-10 02:40:00 | GOES-19 | PEDRO DO ROSÁRIO | MARANHÃO | Brasil | 2108256 | 21 | 33 | nan | nan | nan | Amazônia | 70.1 |
| 0da4a5ab-4ad2-3484-9407-122595347b7f | -3.7406 | -45.4503 | 2025-12-10 02:40:00 | GOES-19 | PINDARÉ-MIRIM | MARANHÃO | Brasil | 2108504 | 21 | 33 | nan | nan | nan | Amazônia | 37.8 |
| 28ba2219-cc89-3dbe-bcdd-e65a01a361ff | -2.487 | -47.7692 | 2025-12-10 02:40:00 | GOES-19 | IPIXUNA DO PARÁ | PARÁ | Brasil | 1503457 | 15 | 33 | nan | nan | nan | Amazônia | 45.7 |
| 07c336a6-5074-3dad-9050-322effd8e0c9 | -5.1562 | -43.1237 | 2025-12-10 02:40:00 | GOES-19 | TIMON | MARANHÃO | Brasil | 2112209 | 21 | 33 | nan | nan | nan | Cerrado | 62.4 |
| da7c1d37-c5c0-3587-bd74-48a858f6e4ef | -5.1749 | -43.1224 | 2025-12-10 02:40:00 | GOES-19 | TIMON | MARANHÃO | Brasil | 2112209 | 21 | 33 | nan | nan | nan | Cerrado | 64.2 |
| 8af22f4d-daf1-3b42-8acd-0184b171102d | -3.694 | -43.8134 | 2025-12-10 02:40:00 | GOES-19 | VARGEM GRANDE | MARANHÃO | Brasil | 2112704 | 21 | 33 | nan | nan | nan | Cerrado | 76.3 |
| 3bf4597e-5be3-357d-aef6-c6f683cc1888 | -3.7403 | -45.4952 | 2025-12-10 02:40:00 | GOES-19 | PINDARÉ-MIRIM | MARANHÃO | Brasil | 2108504 | 21 | 33 | nan | nan | nan | Amazônia | 41.5 |
| fbd8d6cc-5daf-30d4-badf-d3b720046172 | -3.7589 | -45.4944 | 2025-12-10 02:40:00 | GOES-19 | PINDARÉ-MIRIM | MARANHÃO | Brasil | 2108504 | 21 | 33 | nan | nan | nan | Amazônia | 52.1 |
| 9e3cfb62-f684-3c54-9425-3e7af33f48df | -3.7592 | -45.4494 | 2025-12-10 02:40:00 | GOES-19 | PINDARÉ-MIRIM | MARANHÃO | Brasil | 2108504 | 21 | 33 | nan | nan | nan | Amazônia | 47.2 |
| 6c1a4245-b5aa-3800-b631-a5d308273d1f | -3.6939 | -43.8365 | 2025-12-10 02:40:00 | GOES-19 | VARGEM GRANDE | MARANHÃO | Brasil | 2112704 | 21 | 33 | nan | nan | nan | Cerrado | 65.7 |
| a674448c-390f-36ed-aed2-e7fe10c741c1 | -3.759 | -45.4719 | 2025-12-10 02:40:00 | GOES-19 | PINDARÉ-MIRIM | MARANHÃO | Brasil | 2108504 | 21 | 33 | nan | nan | nan | Amazônia | 124.8 |
| 9e019a42-a0fc-32ea-8db0-a14b4859dfb2 | -3.6939 | -43.8365 | 2025-12-10 02:50:00 | GOES-19 | VARGEM GRANDE | MARANHÃO | Brasil | 2112704 | 21 | 33 | nan | nan | nan | Cerrado | 65.1 |
| fc8db4bb-c1a0-3fce-860f-6346795243b7 | -2.8863 | -45.2375 | 2025-12-10 02:50:00 | GOES-19 | PEDRO DO ROSÁRIO | MARANHÃO | Brasil | 2108256 | 21 | 33 | nan | nan | nan | Amazônia | 59.7 |
| 2db2738b-72aa-3d00-86fd-85276a198754 | -5.1749 | -43.1224 | 2025-12-10 02:50:00 | GOES-19 | TIMON | MARANHÃO | Brasil | 2112209 | 21 | 33 | nan | nan | nan | Cerrado | 90.4 |
| 5549a49d-e635-39b8-852e-603f4feaca09 | -3.694 | -43.8134 | 2025-12-10 02:50:00 | GOES-19 | VARGEM GRANDE | MARANHÃO | Brasil | 2112704 | 21 | 33 | nan | nan | nan | Cerrado | 77.0 |
| 0cae0452-2383-3d7a-9c9d-501996010817 | -6.6013 | -35.3069 | 2025-12-10 02:55:00 | NPP-375D | JACARAÚ | PARAÍBA | Brasil | 2507309 | 25 | 33 | nan | nan | nan | Caatinga | 2.2 |
| 63364b10-adc3-35da-a781-7302a1a96047 | -10.68325 | -37.11426 | 2025-12-10 02:57:00 | NPP-375D | DIVINA PASTORA | SERGIPE | Brasil | 2802007 | 28 | 33 | nan | nan | nan | Mata Atlântica | 1.1 |
| c44bd8da-a8f6-3e56-8285-362d5330e2c4 | -10.68197 | -37.12058 | 2025-12-10 02:57:00 | NPP-375D | DIVINA PASTORA | SERGIPE | Brasil | 2802007 | 28 | 33 | nan | nan | nan | Mata Atlântica | 1.7 |
| d96ad3d5-297f-3228-9f32-01fb89606ac9 | -10.69012 | -37.11591 | 2025-12-10 02:57:00 | NPP-375D | MARUIM | SERGIPE | Brasil | 2804003 | 28 | 33 | nan | nan | nan | Mata Atlântica | 3.2 |
| 0ba3b9ef-b12c-387a-93ce-43a4a43edcad | -10.68677 | -37.12394 | 2025-12-10 02:57:00 | NPP-375D | DIVINA PASTORA | SERGIPE | Brasil | 2802007 | 28 | 33 | nan | nan | nan | Mata Atlântica | 3.9 |
| ba755846-78c0-35f2-8e9e-c118cf257806 | -10.68884 | -37.12224 | 2025-12-10 02:57:00 | NPP-375D | DIVINA PASTORA | SERGIPE | Brasil | 2802007 | 28 | 33 | nan | nan | nan | Mata Atlântica | 4.5 |
| c5719107-3e6b-3278-a908-d3204e517e04 | -10.68808 | -37.11771 | 2025-12-10 02:57:00 | NPP-375D | DIVINA PASTORA | SERGIPE | Brasil | 2802007 | 28 | 33 | nan | nan | nan | Mata Atlântica | 3.9 |
| 092fba17-9651-35db-bbab-cbb64ac6d2cb | -2.8863 | -45.2375 | 2025-12-10 03:00:00 | GOES-19 | PEDRO DO ROSÁRIO | MARANHÃO | Brasil | 2108256 | 21 | 33 | nan | nan | nan | Amazônia | 54.0 |
| 52c20b6d-ef6f-3a03-909c-6dd2dcd528ba | -5.1749 | -43.1224 | 2025-12-10 03:00:00 | GOES-19 | TIMON | MARANHÃO | Brasil | 2112209 | 21 | 33 | nan | nan | nan | Cerrado | 72.6 |
| b7a3b74b-8921-3379-881e-5d94d4ccfede | -3.694 | -43.8134 | 2025-12-10 03:00:00 | GOES-19 | VARGEM GRANDE | MARANHÃO | Brasil | 2112704 | 21 | 33 | nan | nan | nan | Cerrado | 63.6 |
| aad3aa14-3378-3d49-9830-5661c195c985 | -3.6939 | -43.8365 | 2025-12-10 03:00:00 | GOES-19 | VARGEM GRANDE | MARANHÃO | Brasil | 2112704 | 21 | 33 | nan | nan | nan | Cerrado | 61.5 |
| 7b81eb46-b43e-3c8a-a805-df04be7021b7 | -3.694 | -43.8134 | 2025-12-10 03:10:00 | GOES-19 | VARGEM GRANDE | MARANHÃO | Brasil | 2112704 | 21 | 33 | nan | nan | nan | Cerrado | 64.3 |
| 6878756a-7b26-3350-8e9b-22ecc3f1b793 | -5.1749 | -43.1224 | 2025-12-10 03:10:00 | GOES-19 | TIMON | MARANHÃO | Brasil | 2112209 | 21 | 33 | nan | nan | nan | Cerrado | 77.8 |
| a06c5c9a-6bfe-3947-b4ac-4f2f7b48299a | -2.8863 | -45.2375 | 2025-12-10 03:10:00 | GOES-19 | PEDRO DO ROSÁRIO | MARANHÃO | Brasil | 2108256 | 21 | 33 | nan | nan | nan | Amazônia | 46.4 |
| fe30c973-3693-3ed7-bc86-996960f1be45 | -5.35823 | -38.06458 | 2025-12-10 03:17:00 | NOAA-20 | TABULEIRO DO NORTE | CEARÁ | Brasil | 2313104 | 23 | 33 | nan | nan | nan | Caatinga | 4.4 |
| d7c07e5e-3bf6-351e-b0c3-099304825118 | -5.35961 | -38.06812 | 2025-12-10 03:17:00 | NOAA-20 | TABULEIRO DO NORTE | CEARÁ | Brasil | 2313104 | 23 | 33 | nan | nan | nan | Caatinga | 4.2 |
| 300b396a-4c46-3ca5-a70f-6bf38879a074 | -11.10781 | -40.28243 | 2025-12-10 03:17:00 | NOAA-20 | CAÉM | BAHIA | Brasil | 2905107 | 29 | 33 | nan | nan | nan | Caatinga | 6.9 |
| 73801a56-8418-386f-8626-76cc0af045e3 | -9.08845 | -40.88297 | 2025-12-10 03:17:00 | NOAA-20 | CASA NOVA | BAHIA | Brasil | 2907202 | 29 | 33 | nan | nan | nan | Caatinga | 0.9 |
| 7b1e74d8-ef92-3774-8fa8-5f6638520252 | -10.00953 | -36.40128 | 2025-12-10 03:17:00 | NOAA-20 | TEOTÔNIO VILELA | ALAGOAS | Brasil | 2709152 | 27 | 33 | nan | nan | nan | Mata Atlântica | 10.6 |
| fbf170d3-b304-3ea6-9387-6979b3bc0519 | -11.11033 | -40.28304 | 2025-12-10 03:17:00 | NOAA-20 | CAÉM | BAHIA | Brasil | 2905107 | 29 | 33 | nan | nan | nan | Caatinga | 6.7 |
| d9780ccb-b773-3c02-9552-d33c9b017929 | -3.43851 | -41.6543 | 2025-12-10 03:17:00 | NOAA-20 | COCAL | PIAUÍ | Brasil | 2202703 | 22 | 33 | nan | nan | nan | Caatinga | 11.4 |


[Clique aqui para ver as próximas entradas](README3.md)
