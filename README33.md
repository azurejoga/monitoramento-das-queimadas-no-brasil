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

## Dados Diários - Página 33

| ID | Latitude | Longitude | Data/Hora GMT | Satélite | Município | Estado | País | Município ID | Estado ID | País ID | Dias sem Chuva | Precipitação | Risco de Fogo | Bioma | FRP |
|----|----------|-----------|---------------|----------|-----------|--------|------|--------------|-----------|---------|----------------|--------------|----------------|-------|-----|
| c14e7f10-ce68-372d-ac3c-762fe84b576e | -2.84784 | -48.44913 | 2024-11-06 04:36:00 | NOAA-20 | TOMÉ-AÇU | PARÁ | Brasil | 1508001 | 15 | 33 | nan | nan | nan | Amazônia | 1.4 |
| 8eb1ac38-ca62-3c41-8608-db5146bb84df | -4.05603 | -46.94082 | 2024-11-06 04:36:00 | NOAA-20 | ITINGA DO MARANHÃO | MARANHÃO | Brasil | 2105427 | 21 | 33 | nan | nan | nan | Amazônia | 1.9 |
| dc880aa6-68e8-39dd-a136-b5d1ff9539f0 | -4.35151 | -45.90234 | 2024-11-06 04:36:00 | NOAA-20 | SANTA LUZIA | MARANHÃO | Brasil | 2110005 | 21 | 33 | nan | nan | nan | Amazônia | 1.1 |
| 74eb81b1-73d3-3b38-a4ea-948a1fb8dba8 | -2.83957 | -49.47102 | 2024-11-06 04:36:00 | NOAA-20 | BAIÃO | PARÁ | Brasil | 1501204 | 15 | 33 | nan | nan | nan | Amazônia | 7.8 |
| de4dc23c-a364-3f19-8596-5f287de48a74 | -3.08191 | -50.95445 | 2024-11-06 04:36:00 | NOAA-20 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 4.9 |
| 867a7d4a-aa38-36c0-8cee-bc6064d1b45e | -3.85535 | -52.27258 | 2024-11-06 04:36:00 | NOAA-20 | SENADOR JOSÉ PORFÍRIO | PARÁ | Brasil | 1507805 | 15 | 33 | nan | nan | nan | Amazônia | 2.8 |
| 12d45531-c003-3350-8b05-a18b1591ae3e | -3.17346 | -54.47095 | 2024-11-06 04:36:00 | NOAA-20 | MOJUÍ DOS CAMPOS | PARÁ | Brasil | 1504752 | 15 | 33 | nan | nan | nan | Amazônia | 3.0 |
| fec75c0b-4003-38aa-92be-c1f58a55b057 | -2.98926 | -53.84668 | 2024-11-06 04:36:00 | NOAA-20 | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | 1.7 |
| 4888c3bc-b6d0-328a-8ad1-e4abbed2b3c4 | -4.58671 | -48.47406 | 2024-11-06 04:36:00 | NOAA-20 | RONDON DO PARÁ | PARÁ | Brasil | 1506187 | 15 | 33 | nan | nan | nan | Amazônia | 4.6 |
| 58120e89-dfd3-3caf-86e6-9b522cb880ed | -5.41161 | -44.79953 | 2024-11-06 04:36:00 | NOAA-20 | TUNTUM | MARANHÃO | Brasil | 2112308 | 21 | 33 | nan | nan | nan | Cerrado | 1.1 |
| 6f9c576d-9180-3efe-a62e-925914c787a6 | -3.15912 | -50.20044 | 2024-11-06 04:36:00 | NOAA-20 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 8.7 |
| 08f573fa-8403-3297-97d1-580c17eb41c2 | -2.60414 | -48.20323 | 2024-11-06 04:36:00 | NOAA-20 | TOMÉ-AÇU | PARÁ | Brasil | 1508001 | 15 | 33 | nan | nan | nan | Amazônia | 0.9 |
| 12e999d6-8870-38bc-9e21-9779c425b29b | -3.42243 | -50.2492 | 2024-11-06 04:36:00 | NOAA-20 | PACAJÁ | PARÁ | Brasil | 1505486 | 15 | 33 | nan | nan | nan | Amazônia | 0.7 |
| ded828f9-e105-3f1e-9aa5-136d4a9ac661 | -2.51226 | -48.91695 | 2024-11-06 04:36:00 | NOAA-20 | MOJU | PARÁ | Brasil | 1504703 | 15 | 33 | nan | nan | nan | Amazônia | 0.9 |
| 4468c3fa-cf5e-3c4f-affc-c2e3ecfb52e3 | -4.20548 | -53.48524 | 2024-11-06 04:36:00 | NOAA-20 | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 1.5 |
| 06989389-b3b1-36bd-b742-1c348d4e374f | -3.4174 | -50.38869 | 2024-11-06 04:36:00 | NOAA-20 | PACAJÁ | PARÁ | Brasil | 1505486 | 15 | 33 | nan | nan | nan | Amazônia | 1.2 |
| 84141237-6fb6-33d7-a9c9-a3dec065c5d2 | -2.41055 | -48.87286 | 2024-11-06 04:36:00 | NOAA-20 | MOJU | PARÁ | Brasil | 1504703 | 15 | 33 | nan | nan | nan | Amazônia | 1.0 |
| 4153f1af-8ff4-3771-991a-e1711638e7d4 | -2.44647 | -49.03361 | 2024-11-06 04:36:00 | NOAA-20 | MOJU | PARÁ | Brasil | 1504703 | 15 | 33 | nan | nan | nan | Amazônia | 4.9 |
| caa0ca3e-4506-3d68-ba20-936d479bee66 | -3.0091 | -53.43254 | 2024-11-06 04:36:00 | NOAA-20 | MEDICILÂNDIA | PARÁ | Brasil | 1504455 | 15 | 33 | nan | nan | nan | Amazônia | 17.9 |
| f432908e-9305-3e8d-ac38-81bf4279d5af | -3.29379 | -53.11438 | 2024-11-06 04:36:00 | NOAA-20 | MEDICILÂNDIA | PARÁ | Brasil | 1504455 | 15 | 33 | nan | nan | nan | Amazônia | 3.1 |
| e0fb9e67-6962-3201-98f4-999c6ca84de2 | -2.39971 | -46.17039 | 2024-11-06 04:36:00 | NOAA-20 | CENTRO DO GUILHERME | MARANHÃO | Brasil | 2103158 | 21 | 33 | nan | nan | nan | Amazônia | 4.7 |
| f825fdef-b620-3390-a2ba-2a55973c6932 | -4.23293 | -49.81538 | 2024-11-06 04:36:00 | NOAA-20 | NOVO REPARTIMENTO | PARÁ | Brasil | 1505064 | 15 | 33 | nan | nan | nan | Amazônia | 1.4 |
| a1ee7d6a-4d09-302a-afc2-1cd4b12a87de | -2.79319 | -48.57795 | 2024-11-06 04:36:00 | NOAA-20 | TAILÂNDIA | PARÁ | Brasil | 1507953 | 15 | 33 | nan | nan | nan | Amazônia | 4.0 |
| 7aa9bf16-a71c-36ec-b39a-c7e1ab02c2ab | -2.84891 | -51.76923 | 2024-11-06 04:36:00 | NOAA-20 | SENADOR JOSÉ PORFÍRIO | PARÁ | Brasil | 1507805 | 15 | 33 | nan | nan | nan | Amazônia | 5.5 |
| e83c8a48-c58e-33c9-b2fa-488bce7e450b | -2.84543 | -51.80044 | 2024-11-06 04:36:00 | NOAA-20 | SENADOR JOSÉ PORFÍRIO | PARÁ | Brasil | 1507805 | 15 | 33 | nan | nan | nan | Amazônia | 2.4 |
| 717a3d2d-5e44-354b-938e-0105c7001e5c | -2.29208 | -51.27996 | 2024-11-06 04:36:00 | NOAA-20 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 0.5 |
| 2c29e02e-dce4-3a0a-907b-4a3d3416d62b | -4.08065 | -48.32048 | 2024-11-06 04:36:00 | NOAA-20 | DOM ELISEU | PARÁ | Brasil | 1502939 | 15 | 33 | nan | nan | nan | Amazônia | 1.4 |
| 9a6fb69d-7f6c-3eff-aca5-a33bfc5abcb4 | -3.08848 | -54.51316 | 2024-11-06 04:36:00 | NOAA-20 | MOJUÍ DOS CAMPOS | PARÁ | Brasil | 1504752 | 15 | 33 | nan | nan | nan | Amazônia | 1.4 |
| e1aa7681-a289-3684-bbc2-0ba759fe1012 | -2.55361 | -51.22995 | 2024-11-06 04:36:00 | NOAA-20 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 0.8 |
| 2fce675f-2272-3b33-9fc7-e30d614f36e4 | -4.04063 | -54.68176 | 2024-11-06 04:36:00 | NOAA-20 | PLACAS | PARÁ | Brasil | 1505650 | 15 | 33 | nan | nan | nan | Amazônia | 2.3 |
| b1d7a153-b5ea-3ffc-9d7c-47f47e127acf | -2.8525 | -51.76981 | 2024-11-06 04:36:00 | NOAA-20 | SENADOR JOSÉ PORFÍRIO | PARÁ | Brasil | 1507805 | 15 | 33 | nan | nan | nan | Amazônia | 24.6 |
| 898b1c4c-d026-32b8-9437-828699b529a0 | -3.34709 | -50.25562 | 2024-11-06 04:36:00 | NOAA-20 | PACAJÁ | PARÁ | Brasil | 1505486 | 15 | 33 | nan | nan | nan | Amazônia | 1.0 |
| 42cb678c-cdbc-3332-973d-c0effd56267a | -4.13759 | -43.58049 | 2024-11-06 04:36:00 | NOAA-20 | CHAPADINHA | MARANHÃO | Brasil | 2103208 | 21 | 33 | nan | nan | nan | Cerrado | 12.9 |
| d1f8f46f-5e7f-3f5f-bb22-667d7f194249 | -4.74774 | -49.26542 | 2024-11-06 04:36:00 | NOAA-20 | NOVA IPIXUNA | PARÁ | Brasil | 1504976 | 15 | 33 | nan | nan | nan | Amazônia | 0.8 |
| f608f642-de49-32dd-a84d-30059521c859 | -2.82681 | -52.9155 | 2024-11-06 04:36:00 | NOAA-20 | MEDICILÂNDIA | PARÁ | Brasil | 1504455 | 15 | 33 | nan | nan | nan | Amazônia | 5.4 |
| c71fe507-be51-38db-895c-46ee1bc876ea | -2.93059 | -51.04512 | 2024-11-06 04:36:00 | NOAA-20 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 4.2 |
| 2dcb251b-1911-3a98-8050-77c0bb5e8e4c | -2.17338 | -53.70934 | 2024-11-06 04:36:00 | NOAA-20 | PRAINHA | PARÁ | Brasil | 1506005 | 15 | 33 | nan | nan | nan | Amazônia | 1.0 |
| c6da2984-7883-35c3-8ef0-45b17348b7b3 | -3.49553 | -51.25611 | 2024-11-06 04:36:00 | NOAA-20 | ANAPU | PARÁ | Brasil | 1500859 | 15 | 33 | nan | nan | nan | Amazônia | 0.9 |
| aee9f29c-0c5b-3d38-a65f-8efdbc49725f | -2.50461 | -46.07907 | 2024-11-06 04:36:00 | NOAA-20 | CENTRO DO GUILHERME | MARANHÃO | Brasil | 2103158 | 21 | 33 | nan | nan | nan | Amazônia | 1.3 |
| 8f2b5b29-9743-376a-a223-223cf6917ffd | -3.91711 | -46.47489 | 2024-11-06 04:36:00 | NOAA-20 | BOM JARDIM | MARANHÃO | Brasil | 2102002 | 21 | 33 | nan | nan | nan | Amazônia | 1.6 |
| 8ae3a7a5-507f-3050-a912-8e9140b54a9e | -2.23567 | -49.18478 | 2024-11-06 04:36:00 | NOAA-20 | IGARAPÉ-MIRI | PARÁ | Brasil | 1503309 | 15 | 33 | nan | nan | nan | Amazônia | 0.9 |
| f1f29db0-ad74-3796-ae1b-d00f8259a1cd | -2.40537 | -48.43268 | 2024-11-06 04:36:00 | NOAA-20 | TOMÉ-AÇU | PARÁ | Brasil | 1508001 | 15 | 33 | nan | nan | nan | Amazônia | 1.4 |
| 9486ad02-49e8-3811-a5ac-0f6fe0e9b30e | -4.43895 | -50.97499 | 2024-11-06 04:36:00 | NOAA-20 | ANAPU | PARÁ | Brasil | 1500859 | 15 | 33 | nan | nan | nan | Amazônia | 0.9 |
| 577bd603-1e39-338e-b7fd-f502b67c099f | -2.919 | -49.33448 | 2024-11-06 04:36:00 | NOAA-20 | MOJU | PARÁ | Brasil | 1504703 | 15 | 33 | nan | nan | nan | Amazônia | 1.1 |
| 88fd9584-d952-30d9-87f8-85851d40eda9 | -3.55317 | -47.38644 | 2024-11-06 04:36:00 | NOAA-20 | ULIANÓPOLIS | PARÁ | Brasil | 1508126 | 15 | 33 | nan | nan | nan | Amazônia | 1.2 |
| d7ef0259-2831-38fc-af2d-e9b917ef8ae2 | -4.05784 | -48.24947 | 2024-11-06 04:36:00 | NOAA-20 | DOM ELISEU | PARÁ | Brasil | 1502939 | 15 | 33 | nan | nan | nan | Amazônia | 2.0 |
| b9a53219-3768-3e95-9379-6dca3e9e938b | -3.0787 | -49.69859 | 2024-11-06 04:36:00 | NOAA-20 | BAIÃO | PARÁ | Brasil | 1501204 | 15 | 33 | nan | nan | nan | Amazônia | 0.6 |
| be0ad188-806b-31bf-8c6b-d9acb34e6545 | -2.8846 | -51.31246 | 2024-11-06 04:36:00 | NOAA-20 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 1.5 |
| 12e9f99d-d96c-31cb-9d5c-3fa838014130 | -4.06194 | -50.01441 | 2024-11-06 04:36:00 | NOAA-20 | NOVO REPARTIMENTO | PARÁ | Brasil | 1505064 | 15 | 33 | nan | nan | nan | Amazônia | 1.6 |
| 2fb209ca-9579-33a8-b843-b3d2f702bc84 | -2.49902 | -49.1089 | 2024-11-06 04:36:00 | NOAA-20 | MOJU | PARÁ | Brasil | 1504703 | 15 | 33 | nan | nan | nan | Amazônia | 2.5 |
| 9b8e4f9d-4c32-3ab4-bb30-48f76fa34c95 | 0.3805 | -51.38179 | 2024-11-06 04:36:00 | NOAA-20 | MACAPÁ | AMAPÁ | Brasil | 1600303 | 16 | 33 | nan | nan | nan | Amazônia | 0.6 |
| a7d6d15a-6945-3367-bdfb-1c87592df16f | -4.75338 | -45.90843 | 2024-11-06 04:36:00 | NOAA-20 | ARAME | MARANHÃO | Brasil | 2100956 | 21 | 33 | nan | nan | nan | Amazônia | 5.7 |
| b7477d2a-cc2e-3b3b-899e-f408145c6e6b | -3.36034 | -50.10749 | 2024-11-06 04:36:00 | NOAA-20 | PACAJÁ | PARÁ | Brasil | 1505486 | 15 | 33 | nan | nan | nan | Amazônia | 1.1 |
| 75a448c0-1dba-3b4d-8a4b-6b4403e4c19e | -3.96411 | -48.15344 | 2024-11-06 04:36:00 | NOAA-20 | DOM ELISEU | PARÁ | Brasil | 1502939 | 15 | 33 | nan | nan | nan | Amazônia | 0.7 |
| 4d82f1df-aa44-3245-a7b3-86541de9b0b8 | -3.13669 | -51.20626 | 2024-11-06 04:36:00 | NOAA-20 | ANAPU | PARÁ | Brasil | 1500859 | 15 | 33 | nan | nan | nan | Amazônia | 11.5 |
| 5bb7db77-e44b-388a-ad34-3d35a922a1f1 | -2.83767 | -51.35759 | 2024-11-06 04:36:00 | NOAA-20 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 2.0 |
| c012e426-9874-3c90-ad7c-9217cb903baf | -3.05798 | -49.61622 | 2024-11-06 04:36:00 | NOAA-20 | MOJU | PARÁ | Brasil | 1504703 | 15 | 33 | nan | nan | nan | Amazônia | 1.1 |
| c9c04ac6-79f9-3364-ba84-71cdc49b1221 | -3.532 | -49.99296 | 2024-11-06 04:36:00 | NOAA-20 | PACAJÁ | PARÁ | Brasil | 1505486 | 15 | 33 | nan | nan | nan | Amazônia | 1.1 |
| 8ff462cd-a31e-311e-af3c-cb8b25b646bc | -3.66965 | -50.23607 | 2024-11-06 04:36:00 | NOAA-20 | PACAJÁ | PARÁ | Brasil | 1505486 | 15 | 33 | nan | nan | nan | Amazônia | 3.0 |
| 834e62a5-f8ff-3596-a77b-acbb19fb46b9 | -2.17048 | -53.70131 | 2024-11-06 04:36:00 | NOAA-20 | PRAINHA | PARÁ | Brasil | 1506005 | 15 | 33 | nan | nan | nan | Amazônia | 1.6 |
| 4e144222-d2b5-3392-83e3-7438b8a3605c | -3.06556 | -50.99068 | 2024-11-06 04:36:00 | NOAA-20 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 0.9 |
| e40762fa-4103-367c-9d61-141788e85c3d | -4.35083 | -48.63565 | 2024-11-06 04:36:00 | NOAA-20 | RONDON DO PARÁ | PARÁ | Brasil | 1506187 | 15 | 33 | nan | nan | nan | Amazônia | 2.4 |
| 2c2b6955-948e-3017-8551-1f4ff825cbd3 | -3.00746 | -53.44286 | 2024-11-06 04:36:00 | NOAA-20 | MEDICILÂNDIA | PARÁ | Brasil | 1504455 | 15 | 33 | nan | nan | nan | Amazônia | 1.6 |
| 1bc80f93-cbfc-3eab-970f-cf8535da0a82 | -2.9058 | -49.39631 | 2024-11-06 04:36:00 | NOAA-20 | MOJU | PARÁ | Brasil | 1504703 | 15 | 33 | nan | nan | nan | Amazônia | 2.3 |
| 9c09292b-0743-3219-ad42-e9e84e31eeb3 | -2.66883 | -48.50579 | 2024-11-06 04:36:00 | NOAA-20 | TAILÂNDIA | PARÁ | Brasil | 1507953 | 15 | 33 | nan | nan | nan | Amazônia | 1.0 |
| 11545226-cac6-376e-a25d-80e4cf927730 | -3.76091 | -51.65411 | 2024-11-06 04:36:00 | NOAA-20 | SENADOR JOSÉ PORFÍRIO | PARÁ | Brasil | 1507805 | 15 | 33 | nan | nan | nan | Amazônia | 1.5 |
| 0414ae54-b534-3ee6-9e0f-4c9e194ff3c8 | -3.03844 | -53.2726 | 2024-11-06 04:36:00 | NOAA-20 | MEDICILÂNDIA | PARÁ | Brasil | 1504455 | 15 | 33 | nan | nan | nan | Amazônia | 10.6 |
| 6f317aa1-512e-3018-b19f-28be6d5c1961 | -2.84124 | -49.48198 | 2024-11-06 04:36:00 | NOAA-20 | BAIÃO | PARÁ | Brasil | 1501204 | 15 | 33 | nan | nan | nan | Amazônia | 2.0 |
| a0d8817f-775e-3e7c-9fd2-c06e2f5f3c2a | -4.11208 | -46.89584 | 2024-11-06 04:36:00 | NOAA-20 | BOM JARDIM | MARANHÃO | Brasil | 2102002 | 21 | 33 | nan | nan | nan | Amazônia | 1.5 |
| f7258791-5b0d-31e8-acbc-1b9cdb457f12 | -5.02423 | -43.60112 | 2024-11-06 04:36:00 | NOAA-20 | SÃO JOÃO DO SOTER | MARANHÃO | Brasil | 2111078 | 21 | 33 | nan | nan | nan | Cerrado | 6.8 |
| 812c7ef7-4293-3735-a187-443c07862684 | -2.87539 | -51.61625 | 2024-11-06 04:36:00 | NOAA-20 | ANAPU | PARÁ | Brasil | 1500859 | 15 | 33 | nan | nan | nan | Amazônia | 1.8 |
| b94b4c2b-a081-3173-b354-79ff84dfabb8 | -2.28078 | -50.67391 | 2024-11-06 04:36:00 | NOAA-20 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 2.5 |
| ce1b0527-2227-3c7e-a0ce-df0e30fbbc84 | -2.80236 | -51.48671 | 2024-11-06 04:36:00 | NOAA-20 | ANAPU | PARÁ | Brasil | 1500859 | 15 | 33 | nan | nan | nan | Amazônia | 1.7 |
| 2098a0de-e50a-3930-99da-8d2d4b8b6840 | -3.01197 | -53.21247 | 2024-11-06 04:36:00 | NOAA-20 | MEDICILÂNDIA | PARÁ | Brasil | 1504455 | 15 | 33 | nan | nan | nan | Amazônia | 1.1 |
| 15b0aa45-a950-3cc1-9fae-64af7324c4c7 | -4.29864 | -48.62007 | 2024-11-06 04:36:00 | NOAA-20 | RONDON DO PARÁ | PARÁ | Brasil | 1506187 | 15 | 33 | nan | nan | nan | Amazônia | 3.7 |
| 61184f78-61ef-3681-acbf-293da4004578 | -2.42854 | -48.45737 | 2024-11-06 04:36:00 | NOAA-20 | TOMÉ-AÇU | PARÁ | Brasil | 1508001 | 15 | 33 | nan | nan | nan | Amazônia | 0.5 |
| 6c3cb280-f22e-398a-ab10-478588b9d8eb | -4.09346 | -50.50156 | 2024-11-06 04:36:00 | NOAA-20 | NOVO REPARTIMENTO | PARÁ | Brasil | 1505064 | 15 | 33 | nan | nan | nan | Amazônia | 2.2 |
| 98c427f1-bf74-363f-99f9-35d037d7294b | -2.84291 | -52.91322 | 2024-11-06 04:36:00 | NOAA-20 | MEDICILÂNDIA | PARÁ | Brasil | 1504455 | 15 | 33 | nan | nan | nan | Amazônia | 11.4 |
| ac7b112f-e5dc-37e9-8a1b-bc1edea56cdc | -4.1979 | -46.69987 | 2024-11-06 04:36:00 | NOAA-20 | BOM JARDIM | MARANHÃO | Brasil | 2102002 | 21 | 33 | nan | nan | nan | Amazônia | 1.3 |
| ba0ac9b4-29e0-3f1c-9ea6-bbc7c7c647c0 | -2.88863 | -49.37551 | 2024-11-06 04:36:00 | NOAA-20 | MOJU | PARÁ | Brasil | 1504703 | 15 | 33 | nan | nan | nan | Amazônia | 1.3 |
| 75500e55-a155-33e9-b309-f93ec5e2d29b | -3.54579 | -51.29984 | 2024-11-06 04:36:00 | NOAA-20 | ANAPU | PARÁ | Brasil | 1500859 | 15 | 33 | nan | nan | nan | Amazônia | 0.3 |
| 7fad82eb-ea45-3847-b4fd-e24b0efaf36b | -2.38178 | -54.411 | 2024-11-06 04:36:00 | NOAA-20 | SANTARÉM | PARÁ | Brasil | 1506807 | 15 | 33 | nan | nan | nan | Amazônia | 2.8 |
| 57df9df3-41f4-37ce-b835-3f5de667344c | -2.34572 | -48.9191 | 2024-11-06 04:36:00 | NOAA-20 | MOJU | PARÁ | Brasil | 1504703 | 15 | 33 | nan | nan | nan | Amazônia | 1.0 |
| 7119c9df-a506-313f-ba07-51d320d394fe | -2.55189 | -49.22725 | 2024-11-06 04:36:00 | NOAA-20 | MOJU | PARÁ | Brasil | 1504703 | 15 | 33 | nan | nan | nan | Amazônia | 0.9 |
| 4e27f05b-1997-3af8-94d1-996fa08456e6 | -1.42781 | -52.18562 | 2024-11-06 04:36:00 | NOAA-20 | ALMEIRIM | PARÁ | Brasil | 1500503 | 15 | 33 | nan | nan | nan | Amazônia | 1.5 |
| b773e6c8-ef0a-3b6c-8cdf-f409415ddecf | -4.03311 | -48.29886 | 2024-11-06 04:36:00 | NOAA-20 | DOM ELISEU | PARÁ | Brasil | 1502939 | 15 | 33 | nan | nan | nan | Amazônia | 0.9 |
| 811b205f-2da4-3c8d-8f76-96d6b58f3ad3 | -2.33861 | -49.62909 | 2024-11-06 04:36:00 | NOAA-20 | CAMETÁ | PARÁ | Brasil | 1502103 | 15 | 33 | nan | nan | nan | Amazônia | 0.7 |
| 71177585-af8c-34ae-aeeb-e8502b1b220e | -2.93512 | -51.06155 | 2024-11-06 04:36:00 | NOAA-20 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 8.1 |
| e19a5543-ca89-35e8-810b-5f5a16596cea | -2.6564 | -46.74648 | 2024-11-06 04:36:00 | NOAA-20 | PARAGOMINAS | PARÁ | Brasil | 1505502 | 15 | 33 | nan | nan | nan | Amazônia | 1.1 |
| 053fbcdd-4b04-3742-8063-c5e92a1b5647 | -3.45327 | -51.24259 | 2024-11-06 04:36:00 | NOAA-20 | ANAPU | PARÁ | Brasil | 1500859 | 15 | 33 | nan | nan | nan | Amazônia | 1.4 |
| 1bdd1b96-db9a-339f-bfa3-065de3372b6a | -3.71708 | -51.56669 | 2024-11-06 04:36:00 | NOAA-20 | SENADOR JOSÉ PORFÍRIO | PARÁ | Brasil | 1507805 | 15 | 33 | nan | nan | nan | Amazônia | 1.4 |
| 10f9c329-ef69-39c2-8bd2-2082ee2274ea | -2.79946 | -51.48215 | 2024-11-06 04:36:00 | NOAA-20 | ANAPU | PARÁ | Brasil | 1500859 | 15 | 33 | nan | nan | nan | Amazônia | 1.5 |
| b12fca04-ac4f-3b23-a689-4127641c1a8d | -2.54924 | -48.25109 | 2024-11-06 04:36:00 | NOAA-20 | TOMÉ-AÇU | PARÁ | Brasil | 1508001 | 15 | 33 | nan | nan | nan | Amazônia | 0.5 |
| c73508f0-ab44-383f-a0ca-d695fb968b19 | -3.54463 | -47.38589 | 2024-11-06 04:36:00 | NOAA-20 | ULIANÓPOLIS | PARÁ | Brasil | 1508126 | 15 | 33 | nan | nan | nan | Amazônia | 23.2 |
| 1fe8dfb0-93f3-3e43-8e22-8ec3393f494b | -3.04131 | -53.28008 | 2024-11-06 04:36:00 | NOAA-20 | MEDICILÂNDIA | PARÁ | Brasil | 1504455 | 15 | 33 | nan | nan | nan | Amazônia | 3.4 |
| 96b57253-f80e-321c-b52e-f2319e03004a | -3.62447 | -50.24775 | 2024-11-06 04:36:00 | NOAA-20 | PACAJÁ | PARÁ | Brasil | 1505486 | 15 | 33 | nan | nan | nan | Amazônia | 1.5 |
| 66016e63-f3a1-3b65-ab12-d5f55dbb8f89 | -4.09445 | -48.31903 | 2024-11-06 04:36:00 | NOAA-20 | DOM ELISEU | PARÁ | Brasil | 1502939 | 15 | 33 | nan | nan | nan | Amazônia | 2.0 |
| a53d7535-29ca-3b06-bd05-b50bccd0501d | -5.3504 | -46.86522 | 2024-11-06 04:36:00 | NOAA-20 | AMARANTE DO MARANHÃO | MARANHÃO | Brasil | 2100600 | 21 | 33 | nan | nan | nan | Cerrado | 2.0 |
| fdef9ec8-d4f2-3740-b3da-b623fb47f7fe | -3.95638 | -48.15933 | 2024-11-06 04:36:00 | NOAA-20 | DOM ELISEU | PARÁ | Brasil | 1502939 | 15 | 33 | nan | nan | nan | Amazônia | 4.6 |
| fc7cb596-e4d3-39d1-a03d-493a4157f255 | -3.00498 | -51.44335 | 2024-11-06 04:36:00 | NOAA-20 | ANAPU | PARÁ | Brasil | 1500859 | 15 | 33 | nan | nan | nan | Amazônia | 2.7 |


[Clique aqui para ver as próximas entradas](README34.md)
