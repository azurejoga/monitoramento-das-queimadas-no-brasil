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

## Dados Diários - Página 9

| ID | Latitude | Longitude | Data/Hora GMT | Satélite | Município | Estado | País | Município ID | Estado ID | País ID | Dias sem Chuva | Precipitação | Risco de Fogo | Bioma | FRP |
|----|----------|-----------|---------------|----------|-----------|--------|------|--------------|-----------|---------|----------------|--------------|----------------|-------|-----|
| ee96d4ef-0ed5-3fbf-93cc-dbd326a87978 | -4.6043 | -46.88565 | 2024-11-05 01:15:00 | TERRA_M-M | BOM JESUS DAS SELVAS | MARANHÃO | Brasil | 2102036 | 21 | 33 | nan | nan | nan | Amazônia | 22.7 |
| 36c02dc3-ba59-3778-a221-1a703b4ce0d1 | -3.41015 | -50.28361 | 2024-11-05 01:15:00 | TERRA_M-M | PACAJÁ | PARÁ | Brasil | 1505486 | 15 | 33 | nan | nan | nan | Amazônia | 9.4 |
| 230491ea-911f-3eee-9c8a-80d9b214cc64 | -5.6959 | -45.85197 | 2024-11-05 01:15:00 | TERRA_M-M | GRAJAÚ | MARANHÃO | Brasil | 2104800 | 21 | 33 | nan | nan | nan | Cerrado | 49.4 |
| 3a9892ba-07d4-3512-86e3-3b12fd9ee752 | -3.54006 | -47.38449 | 2024-11-05 01:15:00 | TERRA_M-M | ULIANÓPOLIS | PARÁ | Brasil | 1508126 | 15 | 33 | nan | nan | nan | Amazônia | 38.2 |
| 41fe895c-cd46-396b-9608-829b25f92a8c | -4.35098 | -48.63458 | 2024-11-05 01:15:00 | TERRA_M-M | RONDON DO PARÁ | PARÁ | Brasil | 1506187 | 15 | 33 | nan | nan | nan | Amazônia | 17.3 |
| fb352d2c-1d0c-391b-98a0-f7a613963722 | -4.08352 | -53.76171 | 2024-11-05 01:15:00 | TERRA_M-M | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | 6.6 |
| affe09d4-7f3a-3a1f-b7db-673f337241ae | -4.23888 | -48.03588 | 2024-11-05 01:15:00 | TERRA_M-M | DOM ELISEU | PARÁ | Brasil | 1502939 | 15 | 33 | nan | nan | nan | Amazônia | 24.9 |
| 42ab0e1f-9f5d-3684-8714-f0ca0f1c4cc6 | -4.36403 | -47.89489 | 2024-11-05 01:15:00 | TERRA_M-M | DOM ELISEU | PARÁ | Brasil | 1502939 | 15 | 33 | nan | nan | nan | Amazônia | 15.1 |
| e190a23b-d8cb-3964-8673-3ab5d9b8e25d | -4.19394 | -51.0233 | 2024-11-05 01:15:00 | TERRA_M-M | PACAJÁ | PARÁ | Brasil | 1505486 | 15 | 33 | nan | nan | nan | Amazônia | 9.8 |
| 5c6a3d1b-7c40-3f4a-b220-26e18469d4ff | -6.11119 | -43.95904 | 2024-11-05 01:15:00 | TERRA_M-M | COLINAS | MARANHÃO | Brasil | 2103505 | 21 | 33 | nan | nan | nan | Cerrado | 100.6 |
| 434b83c7-f001-36f0-b545-14d0efc6ee17 | -4.23394 | -48.5428 | 2024-11-05 01:15:00 | TERRA_M-M | RONDON DO PARÁ | PARÁ | Brasil | 1506187 | 15 | 33 | nan | nan | nan | Amazônia | 64.5 |
| e7f26f7a-75ae-35ca-a1bb-11940eb0ffb3 | -4.24156 | -48.05393 | 2024-11-05 01:15:00 | TERRA_M-M | DOM ELISEU | PARÁ | Brasil | 1502939 | 15 | 33 | nan | nan | nan | Amazônia | 12.0 |
| 293073af-9927-34d5-a518-27da7632f702 | -3.55601 | -47.40282 | 2024-11-05 01:15:00 | TERRA_M-M | ULIANÓPOLIS | PARÁ | Brasil | 1508126 | 15 | 33 | nan | nan | nan | Amazônia | 138.4 |
| 2fd5d6aa-db3f-3087-a4a8-8bc43fd199ab | -4.36936 | -47.23992 | 2024-11-05 01:15:00 | TERRA_M-M | ITINGA DO MARANHÃO | MARANHÃO | Brasil | 2105427 | 21 | 33 | nan | nan | nan | Amazônia | 13.5 |
| 0cb08883-6aac-34c7-ade1-c96a611c988a | -5.68515 | -45.84811 | 2024-11-05 01:15:00 | TERRA_M-M | GRAJAÚ | MARANHÃO | Brasil | 2104800 | 21 | 33 | nan | nan | nan | Cerrado | 24.3 |
| f2a22c41-4c0c-3cc1-ae2a-c33948e70847 | -5.69934 | -45.84592 | 2024-11-05 01:15:00 | TERRA_M-M | GRAJAÚ | MARANHÃO | Brasil | 2104800 | 21 | 33 | nan | nan | nan | Cerrado | 55.1 |
| 5734dd42-66df-3e19-b1ab-a8edc873ac82 | -3.30364 | -47.01739 | 2024-11-05 01:15:00 | TERRA_M-M | PARAGOMINAS | PARÁ | Brasil | 1505502 | 15 | 33 | nan | nan | nan | Amazônia | 15.3 |
| 9257923b-40c1-3afb-8d93-8d47484bc518 | -5.4722 | -48.60667 | 2024-11-05 01:15:00 | TERRA_M-M | SÃO JOÃO DO ARAGUAIA | PARÁ | Brasil | 1507508 | 15 | 33 | nan | nan | nan | Amazônia | 9.7 |
| 64c925ca-ae1d-32b5-8583-b7aad4fb9ac4 | -3.55063 | -47.37745 | 2024-11-05 01:15:00 | TERRA_M-M | ULIANÓPOLIS | PARÁ | Brasil | 1508126 | 15 | 33 | nan | nan | nan | Amazônia | 261.5 |
| 19a5fdf7-d9b5-3c3c-9d0d-c4c6f404afb6 | -3.56372 | -47.37582 | 2024-11-05 01:15:00 | TERRA_M-M | ULIANÓPOLIS | PARÁ | Brasil | 1508126 | 15 | 33 | nan | nan | nan | Amazônia | 17.9 |
| ab63f488-d4a0-387e-8364-55b596af3f13 | -3.48811 | -50.38495 | 2024-11-05 01:15:00 | TERRA_M-M | PACAJÁ | PARÁ | Brasil | 1505486 | 15 | 33 | nan | nan | nan | Amazônia | 27.3 |
| 9291d991-e94b-39af-91da-915dd0a8523f | -3.0296 | -53.26746 | 2024-11-05 01:17:00 | TERRA_M-M | MEDICILÂNDIA | PARÁ | Brasil | 1504455 | 15 | 33 | nan | nan | nan | Amazônia | 10.5 |
| a07936e7-9931-3934-b52f-474f95f2ad00 | -3.61793 | -53.51922 | 2024-11-05 01:17:00 | TERRA_M-M | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | 9.3 |
| 23e148c4-6c25-35bb-936a-f8bfce353fd2 | -0.6834 | -51.66615 | 2024-11-05 01:17:00 | TERRA_M-M | MAZAGÃO | AMAPÁ | Brasil | 1600402 | 16 | 33 | nan | nan | nan | Amazônia | 6.6 |
| e3ca3037-f5b3-39e7-88e7-ace5dba9c78f | -3.09127 | -54.49907 | 2024-11-05 01:17:00 | TERRA_M-M | MOJUÍ DOS CAMPOS | PARÁ | Brasil | 1504752 | 15 | 33 | nan | nan | nan | Amazônia | 11.1 |
| a7ba95d2-75ce-33aa-b8b4-d1dfc626d0fd | -3.23247 | -53.39941 | 2024-11-05 01:17:00 | TERRA_M-M | MEDICILÂNDIA | PARÁ | Brasil | 1504455 | 15 | 33 | nan | nan | nan | Amazônia | 6.1 |
| a80f8aea-5a48-3288-936d-26fd93897705 | -1.47536 | -52.36679 | 2024-11-05 01:17:00 | TERRA_M-M | ALMEIRIM | PARÁ | Brasil | 1500503 | 15 | 33 | nan | nan | nan | Amazônia | 8.1 |
| 15012d08-43f0-3a16-89e6-71be4f141e42 | -1.32337 | -52.53056 | 2024-11-05 01:17:00 | TERRA_M-M | ALMEIRIM | PARÁ | Brasil | 1500503 | 15 | 33 | nan | nan | nan | Amazônia | 9.1 |
| cbbe9c9c-e5d3-32ae-bc65-bcfc98bfbe84 | -2.78403 | -51.60679 | 2024-11-05 01:17:00 | TERRA_M-M | ANAPU | PARÁ | Brasil | 1500859 | 15 | 33 | nan | nan | nan | Amazônia | 8.1 |
| 3b9260e0-2aa9-38d3-8cb8-48c297961200 | 0.2075 | -51.0787 | 2024-11-05 01:17:00 | TERRA_M-M | MACAPÁ | AMAPÁ | Brasil | 1600303 | 16 | 33 | nan | nan | nan | Amazônia | 8.0 |
| cb228e61-7a63-3e99-b643-834e0d43d68d | -3.08143 | -54.50631 | 2024-11-05 01:17:00 | TERRA_M-M | MOJUÍ DOS CAMPOS | PARÁ | Brasil | 1504752 | 15 | 33 | nan | nan | nan | Amazônia | 30.1 |
| afff7f87-9049-36d9-a63b-c690e6afa572 | -1.15222 | -52.03031 | 2024-11-05 01:17:00 | TERRA_M-M | VITÓRIA DO JARI | AMAPÁ | Brasil | 1600808 | 16 | 33 | nan | nan | nan | Amazônia | 7.0 |
| 84ff93fd-510b-3cb9-9efb-9d8603ec5ce6 | -2.84202 | -51.8087 | 2024-11-05 01:17:00 | TERRA_M-M | SENADOR JOSÉ PORFÍRIO | PARÁ | Brasil | 1507805 | 15 | 33 | nan | nan | nan | Amazônia | 5.9 |
| 1280162c-1361-33b1-8f25-81704a8ca01c | -1.24547 | -51.96851 | 2024-11-05 01:17:00 | TERRA_M-M | ALMEIRIM | PARÁ | Brasil | 1500503 | 15 | 33 | nan | nan | nan | Amazônia | 4.3 |
| e4445f6b-b0b5-3430-90eb-b0a8d9339a69 | -2.85004 | -51.79713 | 2024-11-05 01:17:00 | TERRA_M-M | SENADOR JOSÉ PORFÍRIO | PARÁ | Brasil | 1507805 | 15 | 33 | nan | nan | nan | Amazônia | 7.7 |
| 1e5d9900-0ee7-302c-9b15-3ec6cf2d9f3f | 1.19407 | -51.18438 | 2024-11-05 01:17:00 | TERRA_M-M | TARTARUGALZINHO | AMAPÁ | Brasil | 1600709 | 16 | 33 | nan | nan | nan | Amazônia | 6.0 |
| 6a81d00f-8849-3cf4-8866-216f21ed15a1 | -3.03851 | -53.26619 | 2024-11-05 01:17:00 | TERRA_M-M | MEDICILÂNDIA | PARÁ | Brasil | 1504455 | 15 | 33 | nan | nan | nan | Amazônia | 12.5 |
| 50a2d633-0aa6-3bd2-851a-87d0df0bcbf6 | -2.80925 | -51.78216 | 2024-11-05 01:17:00 | TERRA_M-M | SENADOR JOSÉ PORFÍRIO | PARÁ | Brasil | 1507805 | 15 | 33 | nan | nan | nan | Amazônia | 16.9 |
| 9a2fab2f-125d-388e-a255-6113392ffb36 | -3.03977 | -53.27516 | 2024-11-05 01:17:00 | TERRA_M-M | MEDICILÂNDIA | PARÁ | Brasil | 1504455 | 15 | 33 | nan | nan | nan | Amazônia | 10.1 |
| b2e08437-20ac-3c35-849d-d9229efc4847 | 3.50303 | -51.26206 | 2024-11-05 01:17:00 | TERRA_M-M | OIAPOQUE | AMAPÁ | Brasil | 1600501 | 16 | 33 | nan | nan | nan | Amazônia | 38.4 |
| 1bf36140-4637-3f46-a3e0-94dbe3adf5bb | 0.19716 | -51.07722 | 2024-11-05 01:17:00 | TERRA_M-M | MACAPÁ | AMAPÁ | Brasil | 1600303 | 16 | 33 | nan | nan | nan | Amazônia | 11.5 |
| 76eff057-5535-3f2d-8e91-15b05fc07e73 | -1.15078 | -52.01997 | 2024-11-05 01:17:00 | TERRA_M-M | VITÓRIA DO JARI | AMAPÁ | Brasil | 1600808 | 16 | 33 | nan | nan | nan | Amazônia | 6.8 |
| f36732f9-b1b0-3651-a532-abffbc37eea3 | 3.5685 | -51.81812 | 2024-11-05 01:17:00 | TERRA_M-M | OIAPOQUE | AMAPÁ | Brasil | 1600501 | 16 | 33 | nan | nan | nan | Amazônia | 7.5 |
| 6da4fb8a-b655-39da-8f16-01e31bc76a65 | -2.02176 | -52.32253 | 2024-11-05 01:17:00 | TERRA_M-M | PORTO DE MOZ | PARÁ | Brasil | 1505908 | 15 | 33 | nan | nan | nan | Amazônia | 6.2 |
| 67d46f0d-822f-3edb-82c2-9d6bb1fb0fc3 | -3.10806 | -50.3015 | 2024-11-05 01:17:00 | TERRA_M-M | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 8.5 |
| 83afb0e5-fd0f-3bbb-91ee-a39205f960a3 | -3.09407 | -50.27803 | 2024-11-05 01:17:00 | TERRA_M-M | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 9.4 |
| 12fcdc8a-b777-36b7-809b-d8b8cb8d0f63 | -3.08266 | -54.51514 | 2024-11-05 01:17:00 | TERRA_M-M | MOJUÍ DOS CAMPOS | PARÁ | Brasil | 1504752 | 15 | 33 | nan | nan | nan | Amazônia | 19.0 |
| 5a7222c3-90c5-3746-a8b1-4cc927c9868e | -2.84058 | -51.79852 | 2024-11-05 01:17:00 | TERRA_M-M | SENADOR JOSÉ PORFÍRIO | PARÁ | Brasil | 1507805 | 15 | 33 | nan | nan | nan | Amazônia | 15.9 |
| 0a700a4a-47e6-3100-b37a-3520ede155d2 | -3.09227 | -50.26545 | 2024-11-05 01:17:00 | TERRA_M-M | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 11.0 |
| ebb2c23c-3ae8-3ae6-8ad2-f701848d7ac4 | -6.1041 | -43.9593 | 2024-11-05 01:20:00 | GOES-16 | COLINAS | MARANHÃO | Brasil | 2103505 | 21 | 33 | nan | nan | nan | Cerrado | 83.3 |
| f0217a66-dce5-3274-88dc-2524b0dfa305 | -3.967 | -48.15 | 2024-11-05 01:20:00 | GOES-16 | DOM ELISEU | PARÁ | Brasil | 1502939 | 15 | 33 | nan | nan | nan | Amazônia | 97.7 |
| 4cd18f93-9cb4-3d12-a67f-ef51d2d3b666 | -6.1043 | -43.9362 | 2024-11-05 01:20:00 | GOES-16 | COLINAS | MARANHÃO | Brasil | 2103505 | 21 | 33 | nan | nan | nan | Cerrado | 45.7 |
| 91a55013-960d-3857-8266-1440b055b27b | -4.606 | -46.8758 | 2024-11-05 01:20:00 | GOES-16 | BOM JESUS DAS SELVAS | MARANHÃO | Brasil | 2102036 | 21 | 33 | nan | nan | nan | Amazônia | 42.8 |
| 895e4a9e-ec6a-3623-b800-0fc237607438 | -4.4079 | -43.1252 | 2024-11-05 01:20:00 | GOES-16 | COELHO NETO | MARANHÃO | Brasil | 2103406 | 21 | 33 | nan | nan | nan | Cerrado | 70.9 |
| 7f697dfa-8756-34f0-a9ea-f39a6937b8eb | -4.408 | -43.1018 | 2024-11-05 01:20:00 | GOES-16 | COELHO NETO | MARANHÃO | Brasil | 2103406 | 21 | 33 | nan | nan | nan | Cerrado | 71.4 |
| 5ad61e2f-77d1-3f32-983e-359f11ee0b55 | -2.8065 | -51.4855 | 2024-11-05 01:20:00 | GOES-16 | ANAPU | PARÁ | Brasil | 1500859 | 15 | 33 | nan | nan | nan | Amazônia | 42.3 |
| e8345d9a-d9ba-3e1e-92fb-09812e661ed3 | -6.1229 | -43.9578 | 2024-11-05 01:20:00 | GOES-16 | COLINAS | MARANHÃO | Brasil | 2103505 | 21 | 33 | nan | nan | nan | Cerrado | 51.9 |
| e6d8c888-0d02-3a52-b506-048bad488ec0 | -11.8639 | -43.8644 | 2024-11-05 01:20:00 | GOES-16 | WANDERLEY | BAHIA | Brasil | 2933455 | 29 | 33 | nan | nan | nan | Cerrado | 58.8 |
| 5dd400a6-7eca-3ec0-993d-a4f7f1d3f9f7 | -3.0906 | -54.5073 | 2024-11-05 01:20:00 | GOES-16 | MOJUÍ DOS CAMPOS | PARÁ | Brasil | 1504752 | 15 | 33 | nan | nan | nan | Amazônia | 63.3 |
| 6f8d5b16-ff96-3d0d-88d8-97503c8dd399 | -10.1592 | -36.4078 | 2024-11-05 01:20:00 | GOES-16 | PENEDO | ALAGOAS | Brasil | 2706703 | 27 | 33 | nan | nan | nan | Mata Atlântica | 68.0 |
| 8a4c3ca9-d1c8-3a7d-a031-37068e24d653 | -4.0667 | -46.9246 | 2024-11-05 01:20:00 | GOES-16 | ITINGA DO MARANHÃO | MARANHÃO | Brasil | 2105427 | 21 | 33 | nan | nan | nan | Amazônia | 49.8 |
| d0779638-9c1f-3cbf-a0b0-28c3f0da81e1 | -10.1791 | -36.3773 | 2024-11-05 01:20:00 | GOES-16 | PENEDO | ALAGOAS | Brasil | 2706703 | 27 | 33 | nan | nan | nan | Mata Atlântica | 89.0 |
| 03ab075c-0295-3080-921d-ff053c239c33 | -10.1785 | -36.4043 | 2024-11-05 01:20:00 | GOES-16 | PENEDO | ALAGOAS | Brasil | 2706703 | 27 | 33 | nan | nan | nan | Mata Atlântica | 124.5 |
| 7e98adfe-59fa-31f2-81a8-9704b8b475cf | -3.4934 | -50.3819 | 2024-11-05 01:20:00 | GOES-16 | PACAJÁ | PARÁ | Brasil | 1505486 | 15 | 33 | nan | nan | nan | Amazônia | 46.3 |
| 06f7b227-a476-3165-8d64-bb8c7244d018 | -3.0906 | -54.5073 | 2024-11-05 01:30:00 | GOES-16 | MOJUÍ DOS CAMPOS | PARÁ | Brasil | 1504752 | 15 | 33 | nan | nan | nan | Amazônia | 61.8 |
| cca1d48e-9515-3c5c-95e9-7860a64592a0 | -6.1041 | -43.9593 | 2024-11-05 01:30:00 | GOES-16 | COLINAS | MARANHÃO | Brasil | 2103505 | 21 | 33 | nan | nan | nan | Cerrado | 199.4 |
| ee6c4d0e-0c34-3938-901c-76dd7625f3d9 | -4.0667 | -46.9246 | 2024-11-05 01:30:00 | GOES-16 | ITINGA DO MARANHÃO | MARANHÃO | Brasil | 2105427 | 21 | 33 | nan | nan | nan | Amazônia | 49.2 |
| cd619290-056d-327f-93e3-0af2614492de | -3.967 | -48.15 | 2024-11-05 01:30:00 | GOES-16 | DOM ELISEU | PARÁ | Brasil | 1502939 | 15 | 33 | nan | nan | nan | Amazônia | 92.4 |
| 4c47b687-b78f-32ad-876d-a57c2621bcd8 | -11.8639 | -43.8644 | 2024-11-05 01:30:00 | GOES-16 | WANDERLEY | BAHIA | Brasil | 2933455 | 29 | 33 | nan | nan | nan | Cerrado | 56.5 |
| 77cb0da4-f507-363d-8ac6-c00deef6bdca | -4.2459 | -48.0293 | 2024-11-05 01:30:00 | GOES-16 | DOM ELISEU | PARÁ | Brasil | 1502939 | 15 | 33 | nan | nan | nan | Amazônia | 41.9 |
| e6294c79-1aca-334c-93b0-cbb252c515ff | -3.1061 | -50.2686 | 2024-11-05 01:30:00 | GOES-16 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 50.0 |
| 0ac2fed3-58c2-3b55-b1f9-957716974a26 | -4.408 | -43.1018 | 2024-11-05 01:30:00 | GOES-16 | COELHO NETO | MARANHÃO | Brasil | 2103406 | 21 | 33 | nan | nan | nan | Cerrado | 70.9 |
| 244369bf-0954-3fae-a7d2-3706e489b297 | -3.3919 | -44.5379 | 2024-11-05 01:30:00 | GOES-16 | ANAJATUBA | MARANHÃO | Brasil | 2100709 | 21 | 33 | nan | nan | nan | Amazônia | 49.5 |
| c5c96588-9e2c-331d-9137-1cdeb25374d3 | -6.1229 | -43.9578 | 2024-11-05 01:30:00 | GOES-16 | COLINAS | MARANHÃO | Brasil | 2103505 | 21 | 33 | nan | nan | nan | Cerrado | 57.9 |
| e7f8741d-f540-376e-b8f1-bea9e3a1bee4 | -6.1039 | -43.9824 | 2024-11-05 01:30:00 | GOES-16 | COLINAS | MARANHÃO | Brasil | 2103505 | 21 | 33 | nan | nan | nan | Cerrado | 67.1 |
| ebf4adfc-dc9f-3c1a-ad4c-93dd67f179ff | -6.0853 | -43.9608 | 2024-11-05 01:30:00 | GOES-16 | COLINAS | MARANHÃO | Brasil | 2103505 | 21 | 33 | nan | nan | nan | Cerrado | 42.4 |
| f47a2cfe-1099-323f-9574-32c03ae3a8a0 | -3.1062 | -50.2476 | 2024-11-05 01:30:00 | GOES-16 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 59.1 |
| ac9a4769-3fb0-3d04-a263-1285422b19c3 | -6.1043 | -43.9362 | 2024-11-05 01:30:00 | GOES-16 | COLINAS | MARANHÃO | Brasil | 2103505 | 21 | 33 | nan | nan | nan | Cerrado | 76.2 |
| 2eb83bc3-1d6e-3bd0-97c7-13fd351e8b8c | -4.4079 | -43.1252 | 2024-11-05 01:30:00 | GOES-16 | COELHO NETO | MARANHÃO | Brasil | 2103406 | 21 | 33 | nan | nan | nan | Cerrado | 66.9 |
| a9b7dce4-e9d7-3b92-98e7-5978e4e19010 | -3.5447 | -47.3636 | 2024-11-05 01:40:00 | GOES-16 | ULIANÓPOLIS | PARÁ | Brasil | 1508126 | 15 | 33 | nan | nan | nan | Amazônia | 99.2 |
| e0be2b4f-de29-3e81-bbc8-e917dc3ba8a3 | -3.5631 | -47.3847 | 2024-11-05 01:40:00 | GOES-16 | ULIANÓPOLIS | PARÁ | Brasil | 1508126 | 15 | 33 | nan | nan | nan | Amazônia | 455.3 |
| 01459ada-0821-3461-a297-d7b1da6a89dc | -4.4079 | -43.1252 | 2024-11-05 01:40:00 | GOES-16 | COELHO NETO | MARANHÃO | Brasil | 2103406 | 21 | 33 | nan | nan | nan | Cerrado | 52.7 |
| 19852360-0753-3a6a-8c92-637f2330ec86 | -3.5444 | -47.4073 | 2024-11-05 01:40:00 | GOES-16 | ULIANÓPOLIS | PARÁ | Brasil | 1508126 | 15 | 33 | nan | nan | nan | Amazônia | 100.6 |
| f714dc00-e6fa-346f-aae5-eb6c0f300578 | -3.5446 | -47.3855 | 2024-11-05 01:40:00 | GOES-16 | ULIANÓPOLIS | PARÁ | Brasil | 1508126 | 15 | 33 | nan | nan | nan | Amazônia | 274.0 |
| 1f6e7aca-ea6d-38a1-abdd-8af56dc31ea1 | -6.1041 | -43.9593 | 2024-11-05 01:40:00 | GOES-16 | COLINAS | MARANHÃO | Brasil | 2103505 | 21 | 33 | nan | nan | nan | Cerrado | 47.1 |
| 9c718947-fafb-3bf0-9545-c3430ec01a25 | -11.8639 | -43.8644 | 2024-11-05 01:40:00 | GOES-16 | WANDERLEY | BAHIA | Brasil | 2933455 | 29 | 33 | nan | nan | nan | Cerrado | 58.7 |
| 549b5eec-49ed-3e3d-a121-6c2473f221a4 | -3.563 | -47.4066 | 2024-11-05 01:40:00 | GOES-16 | ULIANÓPOLIS | PARÁ | Brasil | 1508126 | 15 | 33 | nan | nan | nan | Amazônia | 143.5 |
| 818dc630-4833-35d5-93d7-0a1ff651d707 | -3.5632 | -47.3629 | 2024-11-05 01:40:00 | GOES-16 | ULIANÓPOLIS | PARÁ | Brasil | 1508126 | 15 | 33 | nan | nan | nan | Amazônia | 153.4 |
| 2984046b-bd40-325d-8e9f-da99523217d4 | -3.0906 | -54.5073 | 2024-11-05 01:40:00 | GOES-16 | MOJUÍ DOS CAMPOS | PARÁ | Brasil | 1504752 | 15 | 33 | nan | nan | nan | Amazônia | 47.8 |
| 7aac6746-cb65-3b8d-9685-fec49b117c66 | -4.408 | -43.1018 | 2024-11-05 01:40:00 | GOES-16 | COELHO NETO | MARANHÃO | Brasil | 2103406 | 21 | 33 | nan | nan | nan | Cerrado | 53.2 |
| a92476bf-f781-3b90-aecf-b4b320064612 | -3.967 | -48.15 | 2024-11-05 01:40:00 | GOES-16 | DOM ELISEU | PARÁ | Brasil | 1502939 | 15 | 33 | nan | nan | nan | Amazônia | 105.5 |
| 655c5c01-be9d-3f94-81c1-62fceaa7718b | -3.967 | -48.15 | 2024-11-05 01:50:00 | GOES-16 | DOM ELISEU | PARÁ | Brasil | 1502939 | 15 | 33 | nan | nan | nan | Amazônia | 87.2 |
| d5aa776c-8a09-35a6-82f9-433da5ff3efe | -3.0906 | -54.5073 | 2024-11-05 01:50:00 | GOES-16 | MOJUÍ DOS CAMPOS | PARÁ | Brasil | 1504752 | 15 | 33 | nan | nan | nan | Amazônia | 49.7 |
| f45837e9-33c6-3ca1-97bd-b10d742e2cd8 | -10.1613 | -36.2997 | 2024-11-05 01:50:00 | GOES-16 | CORURIPE | ALAGOAS | Brasil | 2702306 | 27 | 33 | nan | nan | nan | Mata Atlântica | 72.4 |
| 1ac4c5dd-a56b-3d16-8953-cece72227f0d | -4.606 | -46.8758 | 2024-11-05 01:50:00 | GOES-16 | BOM JESUS DAS SELVAS | MARANHÃO | Brasil | 2102036 | 21 | 33 | nan | nan | nan | Amazônia | 73.7 |
| 502c73b6-570e-3d88-82db-e512ff91620e | -6.1039 | -43.9824 | 2024-11-05 01:50:00 | GOES-16 | COLINAS | MARANHÃO | Brasil | 2103505 | 21 | 33 | nan | nan | nan | Cerrado | 55.1 |
| a5163168-8f16-3b08-85fe-1fd0952201da | -6.1229 | -43.9578 | 2024-11-05 01:50:00 | GOES-16 | COLINAS | MARANHÃO | Brasil | 2103505 | 21 | 33 | nan | nan | nan | Cerrado | 44.8 |
| 2ac0bbd5-efbd-3665-833d-859f6ab62843 | -6.1043 | -43.9362 | 2024-11-05 01:50:00 | GOES-16 | COLINAS | MARANHÃO | Brasil | 2103505 | 21 | 33 | nan | nan | nan | Cerrado | 59.0 |
| 8562eb8d-ead1-3611-8b7f-7b778ffc738a | -6.1041 | -43.9593 | 2024-11-05 01:50:00 | GOES-16 | COLINAS | MARANHÃO | Brasil | 2103505 | 21 | 33 | nan | nan | nan | Cerrado | 154.5 |
| 3f35fc26-a8a3-3736-bd8e-65f9317a9980 | -4.4079 | -43.1252 | 2024-11-05 01:50:00 | GOES-16 | COELHO NETO | MARANHÃO | Brasil | 2103406 | 21 | 33 | nan | nan | nan | Cerrado | 70.0 |


[Clique aqui para ver as próximas entradas](README10.md)
