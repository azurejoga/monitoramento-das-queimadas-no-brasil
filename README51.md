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

## Dados Diários - Página 51

| ID | Latitude | Longitude | Data/Hora GMT | Satélite | Município | Estado | País | Município ID | Estado ID | País ID | Dias sem Chuva | Precipitação | Risco de Fogo | Bioma | FRP |
|----|----------|-----------|---------------|----------|-----------|--------|------|--------------|-----------|---------|----------------|--------------|----------------|-------|-----|
| 123d690b-bf91-3e56-a5d5-bd528e3aec8a | -5.7119 | -53.4658 | 2026-10-09 02:10:00 | GOES-19 | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 58.5 |
| ce31390c-7c51-3ed6-9a8f-5f1aef35c455 | -6.8909 | -45.8763 | 2026-10-09 02:10:00 | GOES-19 | SÃO RAIMUNDO DAS MANGABEIRAS | MARANHÃO | Brasil | 2111607 | 21 | 33 | nan | nan | nan | Cerrado | 35.3 |
| d43405ff-693e-3b86-98ca-56b8fb799b70 | -12.2158 | -57.0887 | 2026-10-09 02:10:00 | GOES-19 | NOVA MARINGÁ | MATO GROSSO | Brasil | 5108907 | 51 | 33 | nan | nan | nan | Amazônia | 197.3 |
| bd02de07-c06e-3aca-b634-36997c61380b | -13.1639 | -54.3385 | 2026-10-09 02:10:00 | GOES-19 | PARANATINGA | MATO GROSSO | Brasil | 5106307 | 51 | 33 | nan | nan | nan | Amazônia | 66.7 |
| de9339c8-0ea8-3644-af5a-4e33393d33f7 | -3.1285 | -54.1657 | 2026-10-09 02:10:00 | GOES-19 | SANTARÉM | PARÁ | Brasil | 1506807 | 15 | 33 | nan | nan | nan | Amazônia | 96.0 |
| 58f7480f-8f74-3a78-9ab7-17388c5d1ea7 | -6.8719 | -45.9003 | 2026-10-09 02:10:00 | GOES-19 | SÃO RAIMUNDO DAS MANGABEIRAS | MARANHÃO | Brasil | 2111607 | 21 | 33 | nan | nan | nan | Cerrado | 73.2 |
| ce3f2277-75db-37f8-a4c0-a3cb6293bf08 | -3.1114 | -53.7839 | 2026-10-09 02:10:00 | GOES-19 | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | 67.6 |
| a841414f-82aa-3817-af65-39f394840e83 | -13.1636 | -54.3591 | 2026-10-09 02:10:00 | GOES-19 | PARANATINGA | MATO GROSSO | Brasil | 5106307 | 51 | 33 | nan | nan | nan | Amazônia | 71.6 |
| b50acf68-4502-34c0-a6c8-8f38bc4e9301 | -6.1402 | -53.0574 | 2026-10-09 02:10:00 | GOES-19 | SÃO FÉLIX DO XINGU | PARÁ | Brasil | 1507300 | 15 | 33 | nan | nan | nan | Amazônia | 25.3 |
| 54a5a50f-ecb1-33ca-a0ea-0a6e2107cdb6 | -8.7068 | -62.3995 | 2026-10-09 02:10:00 | GOES-19 | PORTO VELHO | RONDÔNIA | Brasil | 1100205 | 11 | 33 | nan | nan | nan | Amazônia | 48.6 |
| 0b6ce835-eea8-3eed-a708-d813a98ba089 | 2.4216 | -50.8307 | 2026-10-09 02:10:00 | GOES-19 | CALÇOENE | AMAPÁ | Brasil | 1600204 | 16 | 33 | nan | nan | nan | Amazônia | 49.5 |
| 57429b25-a7e5-3e46-8f2c-266125249bcf | -3.5493 | -54.6951 | 2026-10-09 02:10:00 | GOES-19 | PLACAS | PARÁ | Brasil | 1505650 | 15 | 33 | nan | nan | nan | Amazônia | 108.0 |
| c50573c4-b142-311a-aade-38e874420747 | -5.6934 | -53.4667 | 2026-10-09 02:10:00 | GOES-19 | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 55.3 |
| d5a8929b-8a58-32f4-a858-257a4519f6ce | -12.2348 | -57.0871 | 2026-10-09 02:10:00 | GOES-19 | NOVA MARINGÁ | MATO GROSSO | Brasil | 5108907 | 51 | 33 | nan | nan | nan | Amazônia | 130.4 |
| 53dde84a-e5ea-3aeb-9697-8eefd3f1627c | -6.0207 | -40.982 | 2026-10-09 02:10:00 | GOES-19 | ASSUNÇÃO DO PIAUÍ | PIAUÍ | Brasil | 2201051 | 22 | 33 | nan | nan | nan | Caatinga | 194.5 |
| 3c1d7e1e-5a9c-3ae6-a9c4-376225b1f5c6 | -6.0019 | -40.9837 | 2026-10-09 02:10:00 | GOES-19 | ASSUNÇÃO DO PIAUÍ | PIAUÍ | Brasil | 2201051 | 22 | 33 | nan | nan | nan | Caatinga | 205.1 |
| 7e04f44f-a029-303e-b429-32a6222a537a | -7.1995 | -55.1627 | 2026-10-09 02:10:00 | GOES-19 | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 104.4 |
| cb351277-5e83-3ef2-8d43-979c5293a068 | -3.2576 | -54.0418 | 2026-10-09 02:10:00 | GOES-19 | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | 53.7 |
| 66e31a92-68b7-332b-bd8f-3d7e847e7ca3 | -5.6932 | -53.487 | 2026-10-09 02:10:00 | GOES-19 | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 52.3 |
| 54077732-2a71-3a7d-8347-2a324b47a133 | -3.5677 | -54.6746 | 2026-10-09 02:10:00 | GOES-19 | PLACAS | PARÁ | Brasil | 1505650 | 15 | 33 | nan | nan | nan | Amazônia | 82.1 |
| 99075c8b-a7fb-3d96-88bc-990ce394eff4 | -7.2182 | -55.1416 | 2026-10-09 02:10:00 | GOES-19 | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 62.8 |
| e8aa68ec-44df-3cb9-86b9-715f9e3bc137 | -3.1284 | -54.1857 | 2026-10-09 02:10:00 | GOES-19 | SANTARÉM | PARÁ | Brasil | 1506807 | 15 | 33 | nan | nan | nan | Amazônia | 66.9 |
| 9577802a-b57a-3570-a15a-686d20aff77f | -8.7067 | -62.4184 | 2026-10-09 02:10:00 | GOES-19 | PORTO VELHO | RONDÔNIA | Brasil | 1100205 | 11 | 33 | nan | nan | nan | Amazônia | 64.5 |
| 233d72c9-a00c-37e7-968e-0fb1a5e52a30 | -3.0925 | -53.9455 | 2026-10-09 02:10:00 | GOES-19 | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | 86.4 |
| 6b7fb71e-ba0d-3b58-a8e9-8f10e0e79a01 | -3.2577 | -54.0217 | 2026-10-09 02:10:00 | GOES-19 | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | 49.1 |
| f084aa1e-3a34-3e6d-82f6-a1b8213bf3c9 | -8.911 | -45.229 | 2026-10-09 02:10:00 | GOES-19 | BAIXA GRANDE DO RIBEIRO | PIAUÍ | Brasil | 2201150 | 22 | 33 | nan | nan | nan | Cerrado | 70.2 |
| 02cbb38e-3694-3112-8aaf-19b3cda89117 | -10.6199 | -60.4852 | 2026-10-09 02:10:00 | GOES-19 | ARIPUANÃ | MATO GROSSO | Brasil | 5101407 | 51 | 33 | nan | nan | nan | Amazônia | 53.1 |
| 2f943889-9980-3b84-9b3c-46dec74e2563 | -6.021 | -40.9577 | 2026-10-09 02:10:00 | GOES-19 | ASSUNÇÃO DO PIAUÍ | PIAUÍ | Brasil | 2201051 | 22 | 33 | nan | nan | nan | Caatinga | 175.6 |
| ad2b8976-2d46-385a-aed9-4b279bf37744 | -10.6012 | -60.4863 | 2026-10-09 02:10:00 | GOES-19 | ARIPUANÃ | MATO GROSSO | Brasil | 5101407 | 51 | 33 | nan | nan | nan | Amazônia | 48.8 |
| 73985510-abd8-30b2-b576-cc3c870b954b | -3.1109 | -53.945 | 2026-10-09 02:10:00 | GOES-19 | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | 89.5 |
| f598565d-fb77-34a2-8d27-6ac5612ca29d | -9.2549 | -60.8863 | 2026-10-09 02:10:00 | GOES-19 | COLNIZA | MATO GROSSO | Brasil | 5103254 | 51 | 33 | nan | nan | nan | Amazônia | 33.3 |
| 736a4e85-e843-3af9-9555-e414c5838340 | -3.1787 | -50.5807 | 2026-10-09 02:10:00 | GOES-19 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 51.2 |
| 1b9e7396-039c-36ff-b5a3-1e81d90cd494 | -8.7423 | -45.1334 | 2026-10-09 02:10:00 | GOES-19 | BAIXA GRANDE DO RIBEIRO | PIAUÍ | Brasil | 2201150 | 22 | 33 | nan | nan | nan | Cerrado | 306.0 |
| 92715cf7-b3c2-35c9-bc8f-df09dcb07bbd | -2.7428 | -54.1146 | 2026-10-09 02:10:00 | GOES-19 | PRAINHA | PARÁ | Brasil | 1506005 | 15 | 33 | nan | nan | nan | Amazônia | 72.8 |
| d0cd05e7-e0a0-3a55-8e63-9f377d94d093 | -6.0024 | -40.935 | 2026-10-09 02:10:00 | GOES-19 | ASSUNÇÃO DO PIAUÍ | PIAUÍ | Brasil | 2201051 | 22 | 33 | nan | nan | nan | Caatinga | 82.6 |
| eefbee71-8cce-35c6-826f-216a3b7d43a2 | -7.218 | -55.1617 | 2026-10-09 02:10:00 | GOES-19 | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 84.3 |
| 5c707332-c1fb-3d46-8032-cdb5225d0762 | -6.0021 | -40.9594 | 2026-10-09 02:10:00 | GOES-19 | ASSUNÇÃO DO PIAUÍ | PIAUÍ | Brasil | 2201051 | 22 | 33 | nan | nan | nan | Caatinga | 295.2 |
| ff7ce107-5909-3dc8-9000-5059c6367a91 | -12.2346 | -57.1071 | 2026-10-09 02:10:00 | GOES-19 | NOVA MARINGÁ | MATO GROSSO | Brasil | 5108907 | 51 | 33 | nan | nan | nan | Amazônia | 215.8 |
| 29eb363b-b382-3c8f-a317-584ab53b1bb7 | -6.8907 | -45.8988 | 2026-10-09 02:10:00 | GOES-19 | SÃO RAIMUNDO DAS MANGABEIRAS | MARANHÃO | Brasil | 2111607 | 21 | 33 | nan | nan | nan | Cerrado | 101.0 |
| 65eb10f7-021a-3977-9bea-2f31e1f2f001 | -3.5676 | -54.6946 | 2026-10-09 02:10:00 | GOES-19 | PLACAS | PARÁ | Brasil | 1505650 | 15 | 33 | nan | nan | nan | Amazônia | 98.9 |
| fac4e44a-9fbb-3948-8ab7-8b1fce998acd | -13.2015 | -54.3757 | 2026-10-09 02:10:00 | GOES-19 | PARANATINGA | MATO GROSSO | Brasil | 5106307 | 51 | 33 | nan | nan | nan | Amazônia | 53.5 |
| 054191e3-63e0-3a87-91d4-84c1f98fcd55 | -7.5834 | -61.5516 | 2026-10-09 02:10:00 | GOES-19 | MANICORÉ | AMAZONAS | Brasil | 1302702 | 13 | 33 | nan | nan | nan | Amazônia | 34.4 |
| d957b8cc-72d2-3d9b-b382-db6f13ca5081 | -12.0058 | -43.464 | 2026-10-09 02:10:00 | GOES-19 | MUQUÉM DO SÃO FRANCISCO | BAHIA | Brasil | 2922250 | 29 | 33 | nan | nan | nan | Cerrado | 70.2 |
| 8196f011-fdde-3946-99a9-6e3a24ad0079 | -9.2781 | -47.4333 | 2026-10-09 02:10:00 | GOES-19 | RIO SONO | TOCANTINS | Brasil | 1718758 | 17 | 33 | nan | nan | nan | Cerrado | 64.1 |
| c865c6c2-ea9b-396c-b5f3-efef64c151a1 | -3.0007 | -53.9075 | 2026-10-09 02:10:00 | GOES-19 | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | 88.0 |
| 4d70e20a-19eb-313a-af86-24d351904ab9 | -12.2154 | -57.1287 | 2026-10-09 02:10:00 | GOES-19 | NOVA MARINGÁ | MATO GROSSO | Brasil | 5108907 | 51 | 33 | nan | nan | nan | Amazônia | 66.8 |
| 08ca9ba8-a4cc-335c-ad50-f0ed9b84fed8 | -4.6096 | -49.2156 | 2026-10-09 02:10:00 | GOES-19 | JACUNDÁ | PARÁ | Brasil | 1503804 | 15 | 33 | nan | nan | nan | Amazônia | 54.4 |
| 61a04ce2-def5-366e-8eb4-7eeafc50ae81 | -11.6177 | -43.6906 | 2026-10-09 02:10:00 | GOES-19 | BARRA | BAHIA | Brasil | 2902708 | 29 | 33 | nan | nan | nan | Cerrado | 80.7 |
| fb0bb61f-deac-3f83-aded-90c13e1d8f22 | -13.1827 | -54.3571 | 2026-10-09 02:10:00 | GOES-19 | PARANATINGA | MATO GROSSO | Brasil | 5106307 | 51 | 33 | nan | nan | nan | Amazônia | 78.2 |
| b3a06299-6d0b-34f4-86cc-c36d02a1191a | -8.7426 | -45.1106 | 2026-10-09 02:10:00 | GOES-19 | BAIXA GRANDE DO RIBEIRO | PIAUÍ | Brasil | 2201150 | 22 | 33 | nan | nan | nan | Cerrado | 45.7 |
| da10846a-6a24-3259-8864-6230a703027c | -8.537 | -66.9764 | 2026-10-09 02:10:00 | GOES-19 | LÁBREA | AMAZONAS | Brasil | 1302405 | 13 | 33 | nan | nan | nan | Amazônia | 58.7 |
| fb8eae89-e18f-3ff9-aceb-4d90efd5069c | -8.7612 | -45.1314 | 2026-10-09 02:10:00 | GOES-19 | BAIXA GRANDE DO RIBEIRO | PIAUÍ | Brasil | 2201150 | 22 | 33 | nan | nan | nan | Cerrado | 51.7 |
| 033d8c2c-7977-3cbe-98a3-b487dceb9c04 | -3.1101 | -54.1661 | 2026-10-09 02:10:00 | GOES-19 | SANTARÉM | PARÁ | Brasil | 1506807 | 15 | 33 | nan | nan | nan | Amazônia | 100.1 |
| 06e6bda9-7f0e-37ee-a57e-b102c8dd1cc9 | -5.7117 | -53.4862 | 2026-10-09 02:10:00 | GOES-19 | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 79.3 |
| a998f373-50e4-3ce9-b452-7e8a7bd5743d | -8.742 | -45.1563 | 2026-10-09 02:10:00 | GOES-19 | BAIXA GRANDE DO RIBEIRO | PIAUÍ | Brasil | 2201150 | 22 | 33 | nan | nan | nan | Cerrado | 166.9 |
| ebf9a06e-8e9c-3f8d-909b-56fbff0ddefc | -8.9687 | -45.1542 | 2026-10-09 02:10:00 | GOES-19 | BAIXA GRANDE DO RIBEIRO | PIAUÍ | Brasil | 2201150 | 22 | 33 | nan | nan | nan | Cerrado | 69.0 |
| 33a3aac9-8def-3a96-b6a2-27f98a730b31 | -2.499 | -56.0675 | 2026-10-09 02:10:00 | GOES-19 | JURUTI | PARÁ | Brasil | 1503903 | 15 | 33 | nan | nan | nan | Amazônia | 75.6 |
| 56ba123e-d84f-3e24-84f5-e84482359df1 | -8.7234 | -45.1355 | 2026-10-09 02:10:00 | GOES-19 | BAIXA GRANDE DO RIBEIRO | PIAUÍ | Brasil | 2201150 | 22 | 33 | nan | nan | nan | Cerrado | 208.6 |
| acbf5d3f-3f2e-34ec-9241-2e93bc106e22 | -11.6173 | -43.7142 | 2026-10-09 02:10:00 | GOES-19 | BARRA | BAHIA | Brasil | 2902708 | 29 | 33 | nan | nan | nan | Cerrado | 124.5 |
| 9a082e7e-7197-3489-90a6-ef4c1c89c884 | -8.7231 | -45.1583 | 2026-10-09 02:10:00 | GOES-19 | BAIXA GRANDE DO RIBEIRO | PIAUÍ | Brasil | 2201150 | 22 | 33 | nan | nan | nan | Cerrado | 129.3 |
| 71b74707-3b16-36b6-a97d-fe9e9d1fd1af | -12.2156 | -57.1087 | 2026-10-09 02:10:00 | GOES-19 | NOVA MARINGÁ | MATO GROSSO | Brasil | 5108907 | 51 | 33 | nan | nan | nan | Amazônia | 284.3 |
| 8ca09937-e101-3aa4-a080-444b555a9034 | -3.9912 | -59.356 | 2026-10-09 02:10:00 | GOES-19 | BORBA | AMAZONAS | Brasil | 1300805 | 13 | 33 | nan | nan | nan | Amazônia | 53.4 |
| ed148ae2-05fa-3b3a-b025-4f07fc1c150d | -11.6562 | -43.6846 | 2026-10-09 02:10:00 | GOES-19 | BARRA | BAHIA | Brasil | 2902708 | 29 | 33 | nan | nan | nan | Cerrado | 136.5 |
| 5f6dbed3-b81d-3fd0-b423-3fd0fb59e2a0 | -6.2598 | -45.3184 | 2026-10-09 02:10:00 | GOES-19 | FERNANDO FALCÃO | MARANHÃO | Brasil | 2104081 | 21 | 33 | nan | nan | nan | Cerrado | 59.5 |
| 1e08b049-6e65-3be1-b253-9c17d910311d | -8.73 | -45.15 | 2026-10-09 02:15:00 | MSG-03 | BAIXA GRANDE DO RIBEIRO | PIAUÍ | Brasil | 2201150 | 22 | 33 | nan | nan | nan | Cerrado | nan |
| 91f9f415-c02e-3786-8964-f31b0bde351f | -5.99 | -40.97 | 2026-10-09 02:15:00 | MSG-03 | ASSUNÇÃO DO PIAUÍ | PIAUÍ | Brasil | 2201051 | 22 | 33 | nan | nan | nan | Caatinga | nan |
| 00f30de7-8ff8-31c7-a69e-445e62664331 | -6.02 | -40.97 | 2026-10-09 02:15:00 | MSG-03 | ASSUNÇÃO DO PIAUÍ | PIAUÍ | Brasil | 2201051 | 22 | 33 | nan | nan | nan | Caatinga | nan |
| 27160876-1c63-3620-88a7-1ac5fa946890 | -6.0 | -41.01 | 2026-10-09 02:15:00 | MSG-03 | ASSUNÇÃO DO PIAUÍ | PIAUÍ | Brasil | 2201051 | 22 | 33 | nan | nan | nan | Caatinga | nan |
| f1a5d83f-11eb-33c2-9198-8c90c2894475 | -11.6365 | -43.7113 | 2026-10-09 02:20:00 | GOES-19 | BARRA | BAHIA | Brasil | 2902708 | 29 | 33 | nan | nan | nan | Cerrado | 75.2 |
| 402abe17-181c-3bea-bf28-a296df87cfd1 | -6.0019 | -40.9837 | 2026-10-09 02:20:00 | GOES-19 | ASSUNÇÃO DO PIAUÍ | PIAUÍ | Brasil | 2201051 | 22 | 33 | nan | nan | nan | Caatinga | 134.6 |
| 0daece7c-df91-34f6-abba-a280d2631cb8 | -6.7363 | -55.1675 | 2026-10-09 02:20:00 | GOES-19 | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 96.0 |
| b4f7e32f-db7a-3d42-ad81-79a21da11638 | -11.6566 | -43.661 | 2026-10-09 02:20:00 | GOES-19 | BARRA | BAHIA | Brasil | 2902708 | 29 | 33 | nan | nan | nan | Cerrado | 71.9 |
| d0e9b882-7367-3ad0-81fd-9df7b176b8fe | -6.8719 | -45.9003 | 2026-10-09 02:20:00 | GOES-19 | SÃO RAIMUNDO DAS MANGABEIRAS | MARANHÃO | Brasil | 2111607 | 21 | 33 | nan | nan | nan | Cerrado | 45.8 |
| 6200cb9c-75b0-35b3-a720-5aeb73994792 | -3.1114 | -53.7839 | 2026-10-09 02:20:00 | GOES-19 | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | 65.1 |
| 15313f0c-7030-36d9-8544-f43036d9845f | -12.2156 | -57.1087 | 2026-10-09 02:20:00 | GOES-19 | NOVA MARINGÁ | MATO GROSSO | Brasil | 5108907 | 51 | 33 | nan | nan | nan | Amazônia | 127.6 |
| 19447040-2765-3fa3-a068-bb99828e9944 | -6.8907 | -45.8988 | 2026-10-09 02:20:00 | GOES-19 | SÃO RAIMUNDO DAS MANGABEIRAS | MARANHÃO | Brasil | 2111607 | 21 | 33 | nan | nan | nan | Cerrado | 63.2 |
| 178631d2-134a-3c68-8b56-4e0a0bd6073c | -7.2182 | -55.1416 | 2026-10-09 02:20:00 | GOES-19 | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 60.8 |
| 6157d0f5-7c6b-345a-a784-d5928c1e2175 | -6.7178 | -55.1684 | 2026-10-09 02:20:00 | GOES-19 | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 52.0 |
| 9c1c9cf3-0bca-321b-8362-dd2b107a2d19 | -7.218 | -55.1617 | 2026-10-09 02:20:00 | GOES-19 | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 79.9 |
| acfd835f-cef5-339c-9957-8ec05562cb38 | -9.4578 | -40.3392 | 2026-10-09 02:20:00 | GOES-19 | JUAZEIRO | BAHIA | Brasil | 2918407 | 29 | 33 | nan | nan | nan | Caatinga | 89.0 |
| a08d6370-9bae-3ec5-8794-190cb58ce473 | -12.2346 | -57.1071 | 2026-10-09 02:20:00 | GOES-19 | NOVA MARINGÁ | MATO GROSSO | Brasil | 5108907 | 51 | 33 | nan | nan | nan | Amazônia | 129.8 |
| 01972c69-0dd8-3372-b976-18c941d80636 | -3.5493 | -54.6951 | 2026-10-09 02:20:00 | GOES-19 | PLACAS | PARÁ | Brasil | 1505650 | 15 | 33 | nan | nan | nan | Amazônia | 103.0 |
| 48f14a9e-5447-3b24-8431-a27fcc473ae7 | -7.1995 | -55.1627 | 2026-10-09 02:20:00 | GOES-19 | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 87.5 |
| a4e091c8-c52c-3132-8c59-669c688f3bf8 | -6.1402 | -53.0574 | 2026-10-09 02:20:00 | GOES-19 | SÃO FÉLIX DO XINGU | PARÁ | Brasil | 1507300 | 15 | 33 | nan | nan | nan | Amazônia | 25.2 |
| 23b53301-f95d-3a96-a93c-900b0b1dfb10 | -6.0024 | -40.935 | 2026-10-09 02:20:00 | GOES-19 | ASSUNÇÃO DO PIAUÍ | PIAUÍ | Brasil | 2201051 | 22 | 33 | nan | nan | nan | Caatinga | 95.7 |
| 2d9923f5-4c0d-39cc-b8c1-a5e77c6b4133 | -7.2187 | -55.0815 | 2026-10-09 02:20:00 | GOES-19 | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 58.8 |
| fd156391-4f4d-3763-88f2-504e154e7e76 | -11.6369 | -43.6876 | 2026-10-09 02:20:00 | GOES-19 | BARRA | BAHIA | Brasil | 2902708 | 29 | 33 | nan | nan | nan | Cerrado | 72.0 |
| b2cdff1e-d66b-3456-b506-e2a72fcd1e14 | -3.3455 | -50.4078 | 2026-10-09 02:20:00 | GOES-19 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 59.5 |
| d7d8d876-42a9-38b9-85f9-5dafd6bcbbd3 | -2.499 | -56.0675 | 2026-10-09 02:20:00 | GOES-19 | JURUTI | PARÁ | Brasil | 1503903 | 15 | 33 | nan | nan | nan | Amazônia | 77.7 |
| 3ca792ea-4679-3873-9ea6-4b227009dd12 | -13.1827 | -54.3571 | 2026-10-09 02:20:00 | GOES-19 | PARANATINGA | MATO GROSSO | Brasil | 5106307 | 51 | 33 | nan | nan | nan | Amazônia | 69.5 |
| 9dc0f52c-7f95-3656-bea7-50e0cc7b9bee | -5.6934 | -53.4667 | 2026-10-09 02:20:00 | GOES-19 | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 57.2 |
| d55c2bdc-eb00-3d76-bce2-de97fce0ae3f | -13.1636 | -54.3591 | 2026-10-09 02:20:00 | GOES-19 | PARANATINGA | MATO GROSSO | Brasil | 5106307 | 51 | 33 | nan | nan | nan | Amazônia | 68.1 |
| 4447b327-fd75-3091-94a5-33d6584af3fd | -3.5493 | -54.6752 | 2026-10-09 02:20:00 | GOES-19 | PLACAS | PARÁ | Brasil | 1505650 | 15 | 33 | nan | nan | nan | Amazônia | 79.6 |
| 3028a0b9-a288-3a9c-98b6-7bffd8add16f | -3.4396 | -54.5382 | 2026-10-09 02:20:00 | GOES-19 | PLACAS | PARÁ | Brasil | 1505650 | 15 | 33 | nan | nan | nan | Amazônia | 66.9 |
| f1ac8932-f391-355c-b043-cf1b6478a4d5 | -3.2576 | -54.0418 | 2026-10-09 02:20:00 | GOES-19 | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | 57.2 |
| 27364e32-8b29-3902-a097-7bc3f3164e68 | -13.1639 | -54.3385 | 2026-10-09 02:20:00 | GOES-19 | PARANATINGA | MATO GROSSO | Brasil | 5106307 | 51 | 33 | nan | nan | nan | Amazônia | 65.7 |
| 92264472-f2c1-3f1c-b6d6-b5c985b9de6f | -3.11 | -54.1862 | 2026-10-09 02:20:00 | GOES-19 | SANTARÉM | PARÁ | Brasil | 1506807 | 15 | 33 | nan | nan | nan | Amazônia | 78.7 |
| 7bdf78c8-bee1-3e2b-924a-32f6baa00ce0 | -3.1109 | -53.945 | 2026-10-09 02:20:00 | GOES-19 | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | 83.7 |
| a0ed20b6-0bf5-3e07-8804-56a2b9fbdd22 | -3.5677 | -54.6746 | 2026-10-09 02:20:00 | GOES-19 | PLACAS | PARÁ | Brasil | 1505650 | 15 | 33 | nan | nan | nan | Amazônia | 82.2 |
| 4282d3a3-1e33-3b41-8374-94c28a2d8304 | -11.6562 | -43.6846 | 2026-10-09 02:20:00 | GOES-19 | BARRA | BAHIA | Brasil | 2902708 | 29 | 33 | nan | nan | nan | Cerrado | 173.1 |


[Clique aqui para ver as próximas entradas](README52.md)
