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

## Dados Diários - Página 24

| ID | Latitude | Longitude | Data/Hora GMT | Satélite | Município | Estado | País | Município ID | Estado ID | País ID | Dias sem Chuva | Precipitação | Risco de Fogo | Bioma | FRP |
|----|----------|-----------|---------------|----------|-----------|--------|------|--------------|-----------|---------|----------------|--------------|----------------|-------|-----|
| b245ed7a-6b1a-3ee1-afde-069af8826646 | -10.5195 | -46.6243 | 2026-08-09 12:40:00 | GOES-19 | MATEIROS | TOCANTINS | Brasil | 1712702 | 17 | 33 | nan | nan | nan | Cerrado | 62.6 |
| bd05b7c2-66fd-3aea-a7ed-fd13468a5fe7 | -7.3751 | -42.8647 | 2026-08-09 12:40:00 | GOES-19 | ITAUEIRA | PIAUÍ | Brasil | 2205102 | 22 | 33 | nan | nan | nan | Caatinga | 90.5 |
| f9d99d44-29b8-31f6-b6e6-1219bff98950 | -10.5195 | -46.6243 | 2026-08-09 12:50:00 | GOES-19 | MATEIROS | TOCANTINS | Brasil | 1712702 | 17 | 33 | nan | nan | nan | Cerrado | 85.8 |
| 0f570498-1a32-3130-ac0b-36bfd5de94ef | -7.3748 | -42.8883 | 2026-08-09 12:50:00 | GOES-19 | ITAUEIRA | PIAUÍ | Brasil | 2205102 | 22 | 33 | nan | nan | nan | Caatinga | 302.6 |
| 1feff061-b378-3c2d-9616-19d0c57e792a | -10.4811 | -46.6515 | 2026-08-09 12:50:00 | GOES-19 | MATEIROS | TOCANTINS | Brasil | 1712702 | 17 | 33 | nan | nan | nan | Cerrado | 88.3 |
| 09bbc297-00ea-3691-bd3f-3c2874eb5137 | -7.3751 | -42.8647 | 2026-08-09 12:50:00 | GOES-19 | ITAUEIRA | PIAUÍ | Brasil | 2205102 | 22 | 33 | nan | nan | nan | Caatinga | 180.5 |
| c1315be6-597e-3493-8d1b-bc275cecb540 | -10.4811 | -46.6515 | 2026-08-09 13:00:00 | GOES-19 | MATEIROS | TOCANTINS | Brasil | 1712702 | 17 | 33 | nan | nan | nan | Cerrado | 90.1 |
| 82f5f5c6-02fb-3274-947d-73de5bd2d59e | -14.4464 | -58.5709 | 2026-08-09 13:00:00 | GOES-19 | TANGARÁ DA SERRA | MATO GROSSO | Brasil | 5107958 | 51 | 33 | nan | nan | nan | Cerrado | 90.8 |
| 0d4bf5bc-cebe-3da3-b6c0-ef492149db7e | -10.5001 | -46.6491 | 2026-08-09 13:10:00 | GOES-19 | MATEIROS | TOCANTINS | Brasil | 1712702 | 17 | 33 | nan | nan | nan | Cerrado | 70.8 |
| 0943d1d5-1fed-344b-b429-b5200b25e4be | -10.4814 | -46.629 | 2026-08-09 13:10:00 | GOES-19 | MATEIROS | TOCANTINS | Brasil | 1712702 | 17 | 33 | nan | nan | nan | Cerrado | 60.8 |
| d8434016-548d-35f0-9eb5-f241de7047cb | -11.2716 | -44.8624 | 2026-08-09 13:10:00 | GOES-19 | SANTA RITA DE CÁSSIA | BAHIA | Brasil | 2928406 | 29 | 33 | nan | nan | nan | Cerrado | 79.4 |
| d449d794-914c-32f7-bf32-166de9d1e53a | -10.4811 | -46.6515 | 2026-08-09 13:10:00 | GOES-19 | MATEIROS | TOCANTINS | Brasil | 1712702 | 17 | 33 | nan | nan | nan | Cerrado | 184.0 |
| b5d05b9d-23b0-372c-b903-0684b4a1fe60 | -14.4464 | -58.5709 | 2026-08-09 13:10:00 | GOES-19 | TANGARÁ DA SERRA | MATO GROSSO | Brasil | 5107958 | 51 | 33 | nan | nan | nan | Cerrado | 81.4 |
| 362c98a5-cc45-39f9-91e9-af453da3a695 | -7.3748 | -42.8883 | 2026-08-09 13:20:00 | GOES-19 | ITAUEIRA | PIAUÍ | Brasil | 2205102 | 22 | 33 | nan | nan | nan | Caatinga | 98.9 |
| 03a8f582-7030-3d6a-a481-a7a1065c45fb | -10.5195 | -46.6243 | 2026-08-09 13:20:00 | GOES-19 | MATEIROS | TOCANTINS | Brasil | 1712702 | 17 | 33 | nan | nan | nan | Cerrado | 87.4 |
| a91f53ed-20f9-32f7-a114-ecb8da937db9 | -15.1131 | -52.6832 | 2026-08-09 13:30:00 | GOES-19 | BARRA DO GARÇAS | MATO GROSSO | Brasil | 5101803 | 51 | 33 | nan | nan | nan | Cerrado | 59.6 |
| 83b2dc82-59c9-3afa-a448-babe783edf00 | -10.5195 | -46.6243 | 2026-08-09 13:30:00 | GOES-19 | MATEIROS | TOCANTINS | Brasil | 1712702 | 17 | 33 | nan | nan | nan | Cerrado | 71.6 |
| 13324266-5524-3738-8f6a-696f40e3c14c | -10.5004 | -46.6266 | 2026-08-09 13:30:00 | GOES-19 | MATEIROS | TOCANTINS | Brasil | 1712702 | 17 | 33 | nan | nan | nan | Cerrado | 92.2 |
| de0d1c04-98e2-3c5b-9005-139ec83b42a6 | -8.5501 | -45.4044 | 2026-08-09 13:40:00 | GOES-19 | RIBEIRO GONÇALVES | PIAUÍ | Brasil | 2208908 | 22 | 33 | nan | nan | nan | Cerrado | 74.1 |
| 406d8b80-e88d-358e-8639-62c25dc79e71 | -10.4811 | -46.6515 | 2026-08-09 13:40:00 | GOES-19 | MATEIROS | TOCANTINS | Brasil | 1712702 | 17 | 33 | nan | nan | nan | Cerrado | 158.5 |
| 6edd810f-f3b3-350e-a11c-a1d4f3c4eb52 | -11.2716 | -44.8624 | 2026-08-09 13:40:00 | GOES-19 | SANTA RITA DE CÁSSIA | BAHIA | Brasil | 2928406 | 29 | 33 | nan | nan | nan | Cerrado | 162.5 |
| 1ba93d72-77dc-393b-9155-5c772d2e1288 | -10.4814 | -46.629 | 2026-08-09 13:40:00 | GOES-19 | MATEIROS | TOCANTINS | Brasil | 1712702 | 17 | 33 | nan | nan | nan | Cerrado | 71.5 |
| 1679798d-7992-369a-9bc6-8c8dcfd0b2ea | -10.5195 | -46.6243 | 2026-08-09 13:40:00 | GOES-19 | MATEIROS | TOCANTINS | Brasil | 1712702 | 17 | 33 | nan | nan | nan | Cerrado | 87.3 |
| 28081a44-d94e-3a61-8182-225a22d1d12a | -11.272 | -44.8392 | 2026-08-09 13:40:00 | GOES-19 | SANTA RITA DE CÁSSIA | BAHIA | Brasil | 2928406 | 29 | 33 | nan | nan | nan | Cerrado | 80.5 |
| 9f560499-eef4-3258-bdb9-1041129756b8 | -6.8388 | -56.4146 | 2026-08-09 13:50:00 | GOES-19 | ITAITUBA | PARÁ | Brasil | 1503606 | 15 | 33 | nan | nan | nan | Amazônia | 58.1 |
| 3110c3c9-5855-3087-8972-1bc9883836d6 | -10.4811 | -46.6515 | 2026-08-09 13:50:00 | GOES-19 | MATEIROS | TOCANTINS | Brasil | 1712702 | 17 | 33 | nan | nan | nan | Cerrado | 132.4 |
| 93e92a3b-ea9c-3b11-996a-6cb42709d132 | -10.4998 | -46.6716 | 2026-08-09 13:50:00 | GOES-19 | MATEIROS | TOCANTINS | Brasil | 1712702 | 17 | 33 | nan | nan | nan | Cerrado | 68.5 |
| e395559b-28fc-3031-9758-ee93ee43e7a0 | -15.1131 | -52.6832 | 2026-08-09 13:50:00 | GOES-19 | BARRA DO GARÇAS | MATO GROSSO | Brasil | 5101803 | 51 | 33 | nan | nan | nan | Cerrado | 60.6 |
| 77a550c0-99cc-3c40-a0b1-17b514eb2c76 | -15.0933 | -52.7071 | 2026-08-09 13:50:00 | GOES-19 | BARRA DO GARÇAS | MATO GROSSO | Brasil | 5101803 | 51 | 33 | nan | nan | nan | Cerrado | 84.5 |
| b5b5f9fd-f424-36f9-a9f2-9046a72383d7 | -11.272 | -44.8392 | 2026-08-09 13:50:00 | GOES-19 | SANTA RITA DE CÁSSIA | BAHIA | Brasil | 2928406 | 29 | 33 | nan | nan | nan | Cerrado | 80.8 |
| 2ea3167b-b9d1-34e4-9613-cecf9b967a61 | -14.855 | -54.2287 | 2026-08-09 13:50:00 | GOES-19 | PRIMAVERA DO LESTE | MATO GROSSO | Brasil | 5107040 | 51 | 33 | nan | nan | nan | Cerrado | 92.8 |
| 5e8ec290-d9b6-3c47-9a81-9068ec715ab2 | -11.2716 | -44.8624 | 2026-08-09 13:50:00 | GOES-19 | SANTA RITA DE CÁSSIA | BAHIA | Brasil | 2928406 | 29 | 33 | nan | nan | nan | Cerrado | 128.2 |
| 0b5cf8f1-418b-3ef7-b39f-6804502160d5 | -15.0933 | -52.7071 | 2026-08-09 14:00:00 | GOES-19 | BARRA DO GARÇAS | MATO GROSSO | Brasil | 5101803 | 51 | 33 | nan | nan | nan | Cerrado | 95.8 |
| 675971f0-e383-3235-b3ac-db8b59857617 | -10.4814 | -46.629 | 2026-08-09 14:00:00 | GOES-19 | MATEIROS | TOCANTINS | Brasil | 1712702 | 17 | 33 | nan | nan | nan | Cerrado | 62.5 |
| 608a8404-bad6-381a-8f8f-2b73354c1ecf | -11.272 | -44.8392 | 2026-08-09 14:00:00 | GOES-19 | SANTA RITA DE CÁSSIA | BAHIA | Brasil | 2928406 | 29 | 33 | nan | nan | nan | Cerrado | 107.5 |
| b07ddff2-c398-365f-ac9d-0c56745816d6 | -15.1128 | -52.7045 | 2026-08-09 14:00:00 | GOES-19 | BARRA DO GARÇAS | MATO GROSSO | Brasil | 5101803 | 51 | 33 | nan | nan | nan | Cerrado | 80.3 |
| 2b4d435c-4044-362b-ae7f-6b0ccc50d3b3 | -6.8389 | -56.3949 | 2026-08-09 14:00:00 | GOES-19 | ITAITUBA | PARÁ | Brasil | 1503606 | 15 | 33 | nan | nan | nan | Amazônia | 55.0 |
| b7aaa3d0-69b6-3d5a-bfd4-91b0ae5a13cf | -6.8574 | -56.394 | 2026-08-09 14:00:00 | GOES-19 | ITAITUBA | PARÁ | Brasil | 1503606 | 15 | 33 | nan | nan | nan | Amazônia | 66.9 |
| ef9844f1-62d2-38d2-9ad3-85b660fdc7a7 | -10.4811 | -46.6515 | 2026-08-09 14:00:00 | GOES-19 | MATEIROS | TOCANTINS | Brasil | 1712702 | 17 | 33 | nan | nan | nan | Cerrado | 157.1 |
| 4e18623d-2f60-305f-8734-ea6b4c29b68c | -6.8388 | -56.4146 | 2026-08-09 14:00:00 | GOES-19 | ITAITUBA | PARÁ | Brasil | 1503606 | 15 | 33 | nan | nan | nan | Amazônia | 85.1 |
| fa40bd86-1457-3c89-9abc-c3492538488a | -15.1131 | -52.6832 | 2026-08-09 14:00:00 | GOES-19 | BARRA DO GARÇAS | MATO GROSSO | Brasil | 5101803 | 51 | 33 | nan | nan | nan | Cerrado | 80.4 |
| d7716a86-8793-3065-8cfe-64beea572688 | -11.2716 | -44.8624 | 2026-08-09 14:00:00 | GOES-19 | SANTA RITA DE CÁSSIA | BAHIA | Brasil | 2928406 | 29 | 33 | nan | nan | nan | Cerrado | 173.5 |
| d6bc11ee-5053-34d8-857b-a287059fbf1d | -10.4998 | -46.6716 | 2026-08-09 14:00:00 | GOES-19 | MATEIROS | TOCANTINS | Brasil | 1712702 | 17 | 33 | nan | nan | nan | Cerrado | 58.4 |
| 755f1c9a-b23a-3565-a157-ba3e0a4a1715 | -11.1651 | -54.8193 | 2026-08-09 14:10:00 | GOES-19 | NOVA SANTA HELENA | MATO GROSSO | Brasil | 5106190 | 51 | 33 | nan | nan | nan | Amazônia | 63.2 |
| d3769fd2-0317-37cb-9747-03b787dcc6ad | -10.5004 | -46.6266 | 2026-08-09 14:10:00 | GOES-19 | MATEIROS | TOCANTINS | Brasil | 1712702 | 17 | 33 | nan | nan | nan | Cerrado | 70.9 |
| 6971521d-c151-3ce6-8348-8e1d613c778b | -15.1131 | -52.6832 | 2026-08-09 14:10:00 | GOES-19 | BARRA DO GARÇAS | MATO GROSSO | Brasil | 5101803 | 51 | 33 | nan | nan | nan | Cerrado | 77.5 |
| 04c4d35c-b371-37f4-ae65-5a54e35f06e8 | -11.2716 | -44.8624 | 2026-08-09 14:10:00 | GOES-19 | SANTA RITA DE CÁSSIA | BAHIA | Brasil | 2928406 | 29 | 33 | nan | nan | nan | Cerrado | 62.6 |
| f4fbb58d-834b-36bc-a4b5-082cbf14102b | -10.5385 | -46.622 | 2026-08-09 14:10:00 | GOES-19 | MATEIROS | TOCANTINS | Brasil | 1712702 | 17 | 33 | nan | nan | nan | Cerrado | 60.4 |
| e7895c72-8eed-3f48-b5b0-973c2ea70cfb | -10.4814 | -46.629 | 2026-08-09 14:10:00 | GOES-19 | MATEIROS | TOCANTINS | Brasil | 1712702 | 17 | 33 | nan | nan | nan | Cerrado | 74.0 |
| 7cb3060c-da22-381e-b3d3-86907311b92e | -6.8574 | -56.394 | 2026-08-09 14:10:00 | GOES-19 | ITAITUBA | PARÁ | Brasil | 1503606 | 15 | 33 | nan | nan | nan | Amazônia | 71.0 |
| 015b4442-e854-3e14-94a6-3a5ff89668b5 | -10.4811 | -46.6515 | 2026-08-09 14:10:00 | GOES-19 | MATEIROS | TOCANTINS | Brasil | 1712702 | 17 | 33 | nan | nan | nan | Cerrado | 109.8 |
| 74be9eb6-5dbc-311d-a00d-273ace65e126 | -6.8388 | -56.4146 | 2026-08-09 14:10:00 | GOES-19 | ITAITUBA | PARÁ | Brasil | 1503606 | 15 | 33 | nan | nan | nan | Amazônia | 57.8 |
| d5824a94-3567-3b76-b7b7-fa2f162e1ca0 | -10.5195 | -46.6243 | 2026-08-09 14:10:00 | GOES-19 | MATEIROS | TOCANTINS | Brasil | 1712702 | 17 | 33 | nan | nan | nan | Cerrado | 92.3 |
| 640f8927-cb18-3dbc-86a1-aecd7672bd34 | -11.1583 | -45.9323 | 2026-08-09 14:10:00 | GOES-19 | FORMOSA DO RIO PRETO | BAHIA | Brasil | 2911105 | 29 | 33 | nan | nan | nan | Cerrado | 72.6 |
| 80cd5ce3-4662-3558-b7c3-3f0c3f565e1a | -6.8202 | -56.4353 | 2026-08-09 14:10:00 | GOES-19 | ITAITUBA | PARÁ | Brasil | 1503606 | 15 | 33 | nan | nan | nan | Amazônia | 53.9 |
| f248b500-48d3-32d9-bec0-8db346140a05 | -15.1131 | -52.6832 | 2026-08-09 14:20:00 | GOES-19 | BARRA DO GARÇAS | MATO GROSSO | Brasil | 5101803 | 51 | 33 | nan | nan | nan | Cerrado | 139.3 |
| 1fda380c-74bf-3355-a67d-1166a61a6892 | -15.1128 | -52.7045 | 2026-08-09 14:20:00 | GOES-19 | BARRA DO GARÇAS | MATO GROSSO | Brasil | 5101803 | 51 | 33 | nan | nan | nan | Cerrado | 83.1 |
| bd56bd8b-d4e7-325f-93cc-998ad401874f | -6.8389 | -56.3949 | 2026-08-09 14:20:00 | GOES-19 | ITAITUBA | PARÁ | Brasil | 1503606 | 15 | 33 | nan | nan | nan | Amazônia | 54.9 |
| eb03cd88-7425-3bb7-947e-ac89fe9e7fde | -6.8202 | -56.4353 | 2026-08-09 14:20:00 | GOES-19 | ITAITUBA | PARÁ | Brasil | 1503606 | 15 | 33 | nan | nan | nan | Amazônia | 55.4 |
| c8c29d0c-8c63-328a-8e7f-648d0a51e9b5 | -12.1105 | -47.2234 | 2026-08-09 14:20:00 | GOES-19 | CONCEIÇÃO DO TOCANTINS | TOCANTINS | Brasil | 1705607 | 17 | 33 | nan | nan | nan | Cerrado | 75.2 |
| 7e198038-afb7-37a1-bef4-93c1e3cdb906 | -11.1583 | -45.9323 | 2026-08-09 14:20:00 | GOES-19 | FORMOSA DO RIO PRETO | BAHIA | Brasil | 2911105 | 29 | 33 | nan | nan | nan | Cerrado | 83.2 |
| 0f31d1bc-f3fb-3526-be6d-079ab32cfd11 | -11.2908 | -44.8596 | 2026-08-09 14:20:00 | GOES-19 | SANTA RITA DE CÁSSIA | BAHIA | Brasil | 2928406 | 29 | 33 | nan | nan | nan | Cerrado | 75.7 |
| fd681ce5-b526-3261-9c38-92f78dc2880d | -6.8574 | -56.394 | 2026-08-09 14:20:00 | GOES-19 | ITAITUBA | PARÁ | Brasil | 1503606 | 15 | 33 | nan | nan | nan | Amazônia | 82.2 |
| fbf99884-477b-3612-926a-2d242cdd622e | -11.2716 | -44.8624 | 2026-08-09 14:20:00 | GOES-19 | SANTA RITA DE CÁSSIA | BAHIA | Brasil | 2928406 | 29 | 33 | nan | nan | nan | Cerrado | 161.7 |
| 5178d488-97d0-3276-9315-b77444079b8a | -10.2829 | -49.9391 | 2026-08-09 14:20:00 | GOES-19 | PIUM | TOCANTINS | Brasil | 1717503 | 17 | 33 | nan | nan | nan | Cerrado | 65.2 |
| b5a0469a-3f8a-390a-a149-3e85a57ffe9b | -10.5195 | -46.6243 | 2026-08-09 14:20:00 | GOES-19 | MATEIROS | TOCANTINS | Brasil | 1712702 | 17 | 33 | nan | nan | nan | Cerrado | 91.9 |
| 07ccb6fb-b4cb-3c6b-b9e7-7d652e3847fa | -11.1651 | -54.8193 | 2026-08-09 14:20:00 | GOES-19 | NOVA SANTA HELENA | MATO GROSSO | Brasil | 5106190 | 51 | 33 | nan | nan | nan | Amazônia | 64.8 |
| d2055b1a-ac2e-37c1-8b56-b741a458868b | -14.014 | -53.8292 | 2026-08-09 14:20:00 | GOES-19 | PARANATINGA | MATO GROSSO | Brasil | 5106307 | 51 | 33 | nan | nan | nan | Cerrado | 69.5 |
| f81c98b4-c0c1-396c-ba5d-dbe7b2c445fb | -10.5004 | -46.6266 | 2026-08-09 14:20:00 | GOES-19 | MATEIROS | TOCANTINS | Brasil | 1712702 | 17 | 33 | nan | nan | nan | Cerrado | 99.2 |
| fc9301ea-3833-3f7f-a1fb-076354f421be | -15.0933 | -52.7071 | 2026-08-09 14:20:00 | GOES-19 | BARRA DO GARÇAS | MATO GROSSO | Brasil | 5101803 | 51 | 33 | nan | nan | nan | Cerrado | 90.1 |
| 5b37f814-18c9-378e-a80c-cefd264692e6 | -6.8388 | -56.4146 | 2026-08-09 14:30:00 | GOES-19 | ITAITUBA | PARÁ | Brasil | 1503606 | 15 | 33 | nan | nan | nan | Amazônia | 99.1 |
| 46a55a03-d67c-3fbe-84b3-5845d96c574a | -6.8202 | -56.4353 | 2026-08-09 14:30:00 | GOES-19 | ITAITUBA | PARÁ | Brasil | 1503606 | 15 | 33 | nan | nan | nan | Amazônia | 57.9 |
| 09ca10b7-a073-3d3e-9544-2441726a29bf | -22.22 | -43.0351 | 2026-08-09 14:30:00 | GOES-19 | PETRÓPOLIS | RIO DE JANEIRO | Brasil | 3303906 | 33 | 33 | nan | nan | nan | Mata Atlântica | 119.3 |
| 38f3951e-c520-334f-8d35-a571a59d6982 | -6.8574 | -56.394 | 2026-08-09 14:30:00 | GOES-19 | ITAITUBA | PARÁ | Brasil | 1503606 | 15 | 33 | nan | nan | nan | Amazônia | 82.4 |
| 09c66e21-f57f-3924-8044-d6b6904fd0ee | -11.2312 | -54.0369 | 2026-08-09 14:30:00 | GOES-19 | MARCELÂNDIA | MATO GROSSO | Brasil | 5105580 | 51 | 33 | nan | nan | nan | Amazônia | 88.5 |
| 3caa8647-aed1-31b1-b3fe-c580bed9fa79 | -15.1128 | -52.7045 | 2026-08-09 14:30:00 | GOES-19 | BARRA DO GARÇAS | MATO GROSSO | Brasil | 5101803 | 51 | 33 | nan | nan | nan | Cerrado | 95.0 |
| 8f3852a1-4539-3268-8d96-df597d34c096 | -11.2314 | -54.0164 | 2026-08-09 14:30:00 | GOES-19 | MARCELÂNDIA | MATO GROSSO | Brasil | 5105580 | 51 | 33 | nan | nan | nan | Amazônia | 83.4 |
| 1836f64f-63eb-3f53-996a-07a885552795 | -6.8389 | -56.3949 | 2026-08-09 14:30:00 | GOES-19 | ITAITUBA | PARÁ | Brasil | 1503606 | 15 | 33 | nan | nan | nan | Amazônia | 71.3 |
| d5de6c29-1cc6-3ef4-80a1-0b26ee97ae09 | -10.2829 | -49.9391 | 2026-08-09 14:30:00 | GOES-19 | PIUM | TOCANTINS | Brasil | 1717503 | 17 | 33 | nan | nan | nan | Cerrado | 56.1 |
| 0c328bf2-66b5-397e-99bd-15041b52eacb | -15.1131 | -52.6832 | 2026-08-09 14:30:00 | GOES-19 | BARRA DO GARÇAS | MATO GROSSO | Brasil | 5101803 | 51 | 33 | nan | nan | nan | Cerrado | 197.8 |
| 83f55693-bedb-3c0d-bd37-833a6ef44923 | -7.3892 | -59.9731 | 2026-08-09 14:30:00 | GOES-19 | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 49.0 |
| 62cb4512-ee55-30d1-832c-dcc11877c734 | -15.0736 | -52.7309 | 2026-08-09 14:30:00 | GOES-19 | BARRA DO GARÇAS | MATO GROSSO | Brasil | 5101803 | 51 | 33 | nan | nan | nan | Cerrado | 74.1 |
| 3b60b300-649b-3624-a980-9ed404d5f72c | -15.0933 | -52.7071 | 2026-08-09 14:30:00 | GOES-19 | BARRA DO GARÇAS | MATO GROSSO | Brasil | 5101803 | 51 | 33 | nan | nan | nan | Cerrado | 100.0 |
| e646088d-6744-3dd4-9e0a-5e1fa4814ef2 | -11.272 | -44.8392 | 2026-08-09 14:40:00 | GOES-19 | SANTA RITA DE CÁSSIA | BAHIA | Brasil | 2928406 | 29 | 33 | nan | nan | nan | Cerrado | 127.2 |
| 62fe357a-72bb-369b-a368-72d2e53a85ee | -19.5797 | -42.6003 | 2026-08-09 14:40:00 | GOES-19 | TIMÓTEO | MINAS GERAIS | Brasil | 3168705 | 31 | 33 | nan | nan | nan | Mata Atlântica | 101.8 |
| 5a6ca0b8-2b65-3b33-9edc-b0077a54eef5 | -6.8389 | -56.3949 | 2026-08-09 14:40:00 | GOES-19 | ITAITUBA | PARÁ | Brasil | 1503606 | 15 | 33 | nan | nan | nan | Amazônia | 86.1 |
| 0058e220-7c7c-3dc1-9d36-169726d83ad3 | -15.1128 | -52.7045 | 2026-08-09 14:40:00 | GOES-19 | BARRA DO GARÇAS | MATO GROSSO | Brasil | 5101803 | 51 | 33 | nan | nan | nan | Cerrado | 94.3 |
| 38916913-6382-3881-94ca-4c5922e1f97b | -6.8574 | -56.394 | 2026-08-09 14:40:00 | GOES-19 | ITAITUBA | PARÁ | Brasil | 1503606 | 15 | 33 | nan | nan | nan | Amazônia | 111.0 |
| b0dd35e8-64d1-3c22-bed2-ebc504342b91 | -11.1651 | -54.8193 | 2026-08-09 14:40:00 | GOES-19 | NOVA SANTA HELENA | MATO GROSSO | Brasil | 5106190 | 51 | 33 | nan | nan | nan | Amazônia | 83.2 |
| cfe9c744-86a3-3fd4-8dc9-ad877a8e0785 | -15.4055 | -41.799 | 2026-08-09 14:40:00 | GOES-19 | NINHEIRA | MINAS GERAIS | Brasil | 3144656 | 31 | 33 | nan | nan | nan | Mata Atlântica | 107.7 |
| 52bf5462-d27d-38d1-89a0-0db7402f73d6 | -8.6573 | -45.8686 | 2026-08-09 14:40:00 | GOES-19 | TASSO FRAGOSO | MARANHÃO | Brasil | 2112001 | 21 | 33 | nan | nan | nan | Cerrado | 91.2 |
| 4c97c2b0-1267-3de6-af74-6e7bea9c0861 | -11.2312 | -54.0369 | 2026-08-09 14:40:00 | GOES-19 | MARCELÂNDIA | MATO GROSSO | Brasil | 5105580 | 51 | 33 | nan | nan | nan | Amazônia | 90.3 |
| 7d546ab3-5ec2-33ad-b88f-67e3ea4a140e | -22.22 | -43.0351 | 2026-08-09 14:40:00 | GOES-19 | PETRÓPOLIS | RIO DE JANEIRO | Brasil | 3303906 | 33 | 33 | nan | nan | nan | Mata Atlântica | 115.7 |
| c087dff8-a3d6-3904-9406-d7d93dad34f8 | -11.2314 | -54.0164 | 2026-08-09 14:40:00 | GOES-19 | MARCELÂNDIA | MATO GROSSO | Brasil | 5105580 | 51 | 33 | nan | nan | nan | Amazônia | 78.3 |
| 1942ba46-06e3-31b1-861c-cccb50367c56 | -15.0933 | -52.7071 | 2026-08-09 14:40:00 | GOES-19 | BARRA DO GARÇAS | MATO GROSSO | Brasil | 5101803 | 51 | 33 | nan | nan | nan | Cerrado | 118.7 |
| b4adff4d-7abd-3cc0-9ae7-093334cbd76f | -7.3892 | -59.9731 | 2026-08-09 14:40:00 | GOES-19 | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 92.7 |
| 22ba13bf-aa04-3b66-bea7-2ed992f194c8 | -14.2019 | -51.7413 | 2026-08-09 14:40:00 | GOES-19 | NOVA NAZARÉ | MATO GROSSO | Brasil | 5106174 | 51 | 33 | nan | nan | nan | Cerrado | 173.0 |
| e797c47d-7eb4-3972-a756-63b113cdccae | -8.6576 | -45.846 | 2026-08-09 14:40:00 | GOES-19 | TASSO FRAGOSO | MARANHÃO | Brasil | 2112001 | 21 | 33 | nan | nan | nan | Cerrado | 57.8 |
| d5bec803-a2ed-37ac-af4f-06018dd2484a | -15.1131 | -52.6832 | 2026-08-09 14:40:00 | GOES-19 | BARRA DO GARÇAS | MATO GROSSO | Brasil | 5101803 | 51 | 33 | nan | nan | nan | Cerrado | 155.1 |
| fb4b5a11-3682-3674-ba9a-6de3b3920b9c | -14.2023 | -51.72 | 2026-08-09 14:40:00 | GOES-19 | COCALINHO | MATO GROSSO | Brasil | 5103106 | 51 | 33 | nan | nan | nan | Cerrado | 65.2 |


[Clique aqui para ver as próximas entradas](README25.md)
