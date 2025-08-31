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

## Dados Diários - Página 91

| ID | Latitude | Longitude | Data/Hora GMT | Satélite | Município | Estado | País | Município ID | Estado ID | País ID | Dias sem Chuva | Precipitação | Risco de Fogo | Bioma | FRP |
|----|----------|-----------|---------------|----------|-----------|--------|------|--------------|-----------|---------|----------------|--------------|----------------|-------|-----|
| 9a897969-1c84-3faa-9877-e322f12d51ba | -7.8729 | -46.973 | 2025-08-31 13:50:00 | GOES-19 | CAROLINA | MARANHÃO | Brasil | 2102804 | 21 | 33 | nan | nan | nan | Cerrado | 214.7 |
| b76613f4-0ec5-39c5-8961-0bcca35ceaf1 | -6.185 | -43.3491 | 2025-08-31 13:50:00 | GOES-19 | LAGOA DO MATO | MARANHÃO | Brasil | 2105922 | 21 | 33 | nan | nan | nan | Cerrado | 118.8 |
| d11e6f2f-6a11-3999-a24a-07773724cecb | -11.3509 | -43.6133 | 2025-08-31 13:50:00 | GOES-19 | BARRA | BAHIA | Brasil | 2902708 | 29 | 33 | nan | nan | nan | Cerrado | 191.9 |
| eb568a0c-4307-3fce-bf5d-71c1cecd8721 | -13.3439 | -46.9757 | 2025-08-31 13:50:00 | GOES-19 | MONTE ALEGRE DE GOIÁS | GOIÁS | Brasil | 5213509 | 52 | 33 | nan | nan | nan | Cerrado | 93.3 |
| e2ff97a0-1360-3a98-b862-5545c96ac933 | -13.3443 | -46.953 | 2025-08-31 13:50:00 | GOES-19 | MONTE ALEGRE DE GOIÁS | GOIÁS | Brasil | 5213509 | 52 | 33 | nan | nan | nan | Cerrado | 101.2 |
| 1da3f134-a322-3eef-9126-d6d255a1c82e | -6.5758 | -43.6885 | 2025-08-31 13:50:00 | GOES-19 | SÃO JOÃO DOS PATOS | MARANHÃO | Brasil | 2111102 | 21 | 33 | nan | nan | nan | Cerrado | 93.8 |
| 27c5202a-9243-385d-9388-f1a2dcd278ab | -14.8404 | -46.7303 | 2025-08-31 13:50:00 | GOES-19 | FLORES DE GOIÁS | GOIÁS | Brasil | 5207907 | 52 | 33 | nan | nan | nan | Cerrado | 82.0 |
| e8b40e56-ac10-3a10-a008-5cfc29b2c9d1 | -14.0313 | -44.5578 | 2025-08-31 13:50:00 | GOES-19 | COCOS | BAHIA | Brasil | 2908101 | 29 | 33 | nan | nan | nan | Cerrado | 110.6 |
| 7756bec7-b267-3ac1-a8a8-6eea96f261f2 | -6.5209 | -43.5537 | 2025-08-31 13:50:00 | GOES-19 | SÃO JOÃO DOS PATOS | MARANHÃO | Brasil | 2111102 | 21 | 33 | nan | nan | nan | Cerrado | 114.8 |
| d578da90-649a-340e-8f43-03b12a393c18 | -15.6944 | -52.7525 | 2025-08-31 14:00:00 | GOES-19 | GENERAL CARNEIRO | MATO GROSSO | Brasil | 5103908 | 51 | 33 | nan | nan | nan | Cerrado | 62.5 |
| 1c66a882-62a2-3699-b59a-8bb242434254 | -5.8696 | -42.9768 | 2025-08-31 14:00:00 | GOES-19 | PALMEIRAIS | PIAUÍ | Brasil | 2207504 | 22 | 33 | nan | nan | nan | Caatinga | 144.1 |
| 3099c9e9-66fd-39fc-a289-eaed5c8c7480 | -5.4824 | -44.3969 | 2025-08-31 14:00:00 | GOES-19 | SÃO DOMINGOS DO MARANHÃO | MARANHÃO | Brasil | 2110708 | 21 | 33 | nan | nan | nan | Cerrado | 122.0 |
| b89dc43c-bed8-3c7e-a554-f6e2f8094317 | -6.2956 | -43.5496 | 2025-08-31 14:00:00 | GOES-19 | SUCUPIRA DO RIACHÃO | MARANHÃO | Brasil | 2111953 | 21 | 33 | nan | nan | nan | Cerrado | 70.4 |
| ac1889f8-0a5f-3440-92f1-6de807cfac57 | -15.7098 | -48.9702 | 2025-08-31 14:00:00 | GOES-19 | PIRENÓPOLIS | GOIÁS | Brasil | 5217302 | 52 | 33 | nan | nan | nan | Cerrado | 112.9 |
| c6152fdd-d378-380d-a0b1-1ced00e0acee | -14.354 | -51.8705 | 2025-08-31 14:00:00 | GOES-19 | NOVA NAZARÉ | MATO GROSSO | Brasil | 5106174 | 51 | 33 | nan | nan | nan | Cerrado | 88.4 |
| f0919741-5f9e-3fde-883c-073a1d3d43b2 | -7.8541 | -46.9747 | 2025-08-31 14:00:00 | GOES-19 | CAROLINA | MARANHÃO | Brasil | 2102804 | 21 | 33 | nan | nan | nan | Cerrado | 109.2 |
| d75836a0-9b30-37ad-8e89-c3c914d5728a | -14.3346 | -51.873 | 2025-08-31 14:00:00 | GOES-19 | NOVA NAZARÉ | MATO GROSSO | Brasil | 5106174 | 51 | 33 | nan | nan | nan | Cerrado | 145.5 |
| 1673262f-66c4-3a3d-932d-18cbb6335dae | -6.5758 | -43.6885 | 2025-08-31 14:00:00 | GOES-19 | SÃO JOÃO DOS PATOS | MARANHÃO | Brasil | 2111102 | 21 | 33 | nan | nan | nan | Cerrado | 95.4 |
| 0de8cb59-e276-3165-b01e-24dd8223053e | -16.2221 | -52.6778 | 2025-08-31 14:00:00 | GOES-19 | TORIXORÉU | MATO GROSSO | Brasil | 5108204 | 51 | 33 | nan | nan | nan | Cerrado | 45.2 |
| 7b487680-5ad3-3a37-ba20-1f69a80e8278 | -6.2597 | -43.3895 | 2025-08-31 14:00:00 | GOES-19 | LAGOA DO MATO | MARANHÃO | Brasil | 2105922 | 21 | 33 | nan | nan | nan | Cerrado | 121.9 |
| d1be7720-e331-36d9-ad7c-0da0e7d8b1b6 | -14.0313 | -44.5578 | 2025-08-31 14:00:00 | GOES-19 | COCOS | BAHIA | Brasil | 2908101 | 29 | 33 | nan | nan | nan | Cerrado | 114.5 |
| f09ad492-6759-3762-b004-3e81971aabf1 | -8.875 | -45.0961 | 2025-08-31 14:00:00 | GOES-19 | BAIXA GRANDE DO RIBEIRO | PIAUÍ | Brasil | 2201150 | 22 | 33 | nan | nan | nan | Cerrado | 84.3 |
| 2589029a-8b10-32f8-b468-512bdf7ac6ba | -4.7346 | -44.4457 | 2025-08-31 14:00:00 | GOES-19 | SANTO ANTÔNIO DOS LOPES | MARANHÃO | Brasil | 2110302 | 21 | 33 | nan | nan | nan | Cerrado | 152.0 |
| 73f91577-0bbf-3833-9c10-af5f2729e6ed | -11.0849 | -44.611 | 2025-08-31 14:00:00 | GOES-19 | SANTA RITA DE CÁSSIA | BAHIA | Brasil | 2928406 | 29 | 33 | nan | nan | nan | Cerrado | 184.4 |
| 8d8b95c4-b20c-32d4-b089-6d66f3527041 | -6.2409 | -43.3911 | 2025-08-31 14:00:00 | GOES-19 | LAGOA DO MATO | MARANHÃO | Brasil | 2105922 | 21 | 33 | nan | nan | nan | Cerrado | 179.3 |
| c7315057-27ef-381a-9448-1bfb1a1002c1 | -11.0654 | -44.637 | 2025-08-31 14:00:00 | GOES-19 | SANTA RITA DE CÁSSIA | BAHIA | Brasil | 2928406 | 29 | 33 | nan | nan | nan | Cerrado | 144.1 |
| 8c3e66a3-a870-33ee-9852-5dabe5adc5ed | -7.0951 | -44.3128 | 2025-08-31 14:00:00 | GOES-19 | BENEDITO LEITE | MARANHÃO | Brasil | 2101806 | 21 | 33 | nan | nan | nan | Cerrado | 145.3 |
| 5b5be26a-83e5-3754-8e66-14fa5cc14486 | -6.2411 | -43.3677 | 2025-08-31 14:00:00 | GOES-19 | LAGOA DO MATO | MARANHÃO | Brasil | 2105922 | 21 | 33 | nan | nan | nan | Cerrado | 135.1 |
| f30bfc0a-6ed5-353b-8926-af036a75b6dd | -15.6948 | -52.7312 | 2025-08-31 14:00:00 | GOES-19 | BARRA DO GARÇAS | MATO GROSSO | Brasil | 5101803 | 51 | 33 | nan | nan | nan | Cerrado | 112.1 |
| 43bcc022-0ed5-3cd3-ab27-e3912faa147f | -6.5209 | -43.5537 | 2025-08-31 14:00:00 | GOES-19 | SÃO JOÃO DOS PATOS | MARANHÃO | Brasil | 2111102 | 21 | 33 | nan | nan | nan | Cerrado | 130.0 |
| b0bfd3c6-8678-33e8-8b29-a1e56c445b00 | -14.0307 | -44.5814 | 2025-08-31 14:00:00 | GOES-19 | COCOS | BAHIA | Brasil | 2908101 | 29 | 33 | nan | nan | nan | Cerrado | 140.6 |
| 2ec35368-87a4-3c46-8faa-0c0be1b4c99d | -14.3536 | -51.8918 | 2025-08-31 14:00:00 | GOES-19 | NOVA NAZARÉ | MATO GROSSO | Brasil | 5106174 | 51 | 33 | nan | nan | nan | Cerrado | 77.6 |
| 0a3ad062-b715-3793-9506-7a6a3aad1c70 | -15.7102 | -48.9479 | 2025-08-31 14:00:00 | GOES-19 | PIRENÓPOLIS | GOIÁS | Brasil | 5217302 | 52 | 33 | nan | nan | nan | Cerrado | 132.8 |
| 2585ba10-038d-3fa3-aa22-9ff8cd435d75 | -15.7093 | -48.9925 | 2025-08-31 14:00:00 | GOES-19 | PIRENÓPOLIS | GOIÁS | Brasil | 5217302 | 52 | 33 | nan | nan | nan | Cerrado | 67.7 |
| 87c0a7de-a133-3513-8ee3-ca14d8beb623 | -9.2639 | -47.0804 | 2025-08-31 14:00:00 | GOES-19 | LIZARDA | TOCANTINS | Brasil | 1712405 | 17 | 33 | nan | nan | nan | Cerrado | 115.5 |
| e61d8a5d-b492-316c-beee-675eebbaf314 | -7.1139 | -44.3111 | 2025-08-31 14:00:00 | GOES-19 | BENEDITO LEITE | MARANHÃO | Brasil | 2101806 | 21 | 33 | nan | nan | nan | Cerrado | 107.9 |
| e9b3a779-d0cc-3b56-9e42-046f1c1f87f4 | -8.421 | -48.2847 | 2025-08-31 14:00:00 | GOES-19 | TUPIRATINS | TOCANTINS | Brasil | 1721307 | 17 | 33 | nan | nan | nan | Cerrado | 97.8 |
| 107f04d9-b7ec-3f1e-976a-6d959ec64ce4 | -6.5021 | -43.5553 | 2025-08-31 14:00:00 | GOES-19 | SUCUPIRA DO RIACHÃO | MARANHÃO | Brasil | 2111953 | 21 | 33 | nan | nan | nan | Cerrado | 93.3 |
| 675dc5fa-065c-390d-b799-d84000411247 | -11.0658 | -44.6137 | 2025-08-31 14:00:00 | GOES-19 | SANTA RITA DE CÁSSIA | BAHIA | Brasil | 2928406 | 29 | 33 | nan | nan | nan | Cerrado | 118.1 |
| b1446f9d-c609-3081-9760-d2bbe262cee8 | -7.4178 | -47.4537 | 2025-08-31 14:00:00 | GOES-19 | CAROLINA | MARANHÃO | Brasil | 2102804 | 21 | 33 | nan | nan | nan | Cerrado | 126.1 |
| 30cbbfd3-2026-3345-805a-bd5578bf23cc | -13.4006 | -47.0347 | 2025-08-31 14:00:00 | GOES-19 | MONTE ALEGRE DE GOIÁS | GOIÁS | Brasil | 5213509 | 52 | 33 | nan | nan | nan | Cerrado | 85.7 |
| ad068310-a5dc-3365-934c-884a601b3235 | -12.3287 | -45.7201 | 2025-08-31 14:00:00 | GOES-19 | LUÍS EDUARDO MAGALHÃES | BAHIA | Brasil | 2919553 | 29 | 33 | nan | nan | nan | Cerrado | 80.5 |
| f9998c58-bb75-3680-9def-38dffe21142a | -7.8729 | -46.973 | 2025-08-31 14:00:00 | GOES-19 | CAROLINA | MARANHÃO | Brasil | 2102804 | 21 | 33 | nan | nan | nan | Cerrado | 184.7 |
| b0700eee-0517-30ae-b134-3a0738aaa9e6 | -11.3312 | -43.6399 | 2025-08-31 14:00:00 | GOES-19 | BARRA | BAHIA | Brasil | 2902708 | 29 | 33 | nan | nan | nan | Cerrado | 284.7 |
| 99e834ca-50bc-3212-a685-dea21d873fb2 | -15.7107 | -48.9255 | 2025-08-31 14:00:00 | GOES-19 | PIRENÓPOLIS | GOIÁS | Brasil | 5217302 | 52 | 33 | nan | nan | nan | Cerrado | 65.1 |
| 72883a8b-498b-37d4-bae5-6c2e775dc72f | -13.4199 | -47.0317 | 2025-08-31 14:00:00 | GOES-19 | MONTE ALEGRE DE GOIÁS | GOIÁS | Brasil | 5213509 | 52 | 33 | nan | nan | nan | Cerrado | 65.6 |
| c974005f-146d-34bc-a550-6df4bdc584a8 | -11.9143 | -46.3953 | 2025-08-31 14:00:00 | GOES-19 | PONTE ALTA DO BOM JESUS | TOCANTINS | Brasil | 1717800 | 17 | 33 | nan | nan | nan | Cerrado | 97.0 |
| 35b3fa5f-d030-3885-badc-e68da66adf16 | -13.3443 | -46.953 | 2025-08-31 14:00:00 | GOES-19 | MONTE ALEGRE DE GOIÁS | GOIÁS | Brasil | 5213509 | 52 | 33 | nan | nan | nan | Cerrado | 88.4 |
| d052ac75-4a68-3e63-8dc5-dbc6aff2255f | -14.8013 | -46.7371 | 2025-08-31 14:00:00 | GOES-19 | FLORES DE GOIÁS | GOIÁS | Brasil | 5207907 | 52 | 33 | nan | nan | nan | Cerrado | 158.9 |
| 9fe88d4d-b41e-334c-963e-23e5f1362e7a | -6.2599 | -43.3662 | 2025-08-31 14:00:00 | GOES-19 | LAGOA DO MATO | MARANHÃO | Brasil | 2105922 | 21 | 33 | nan | nan | nan | Cerrado | 86.9 |
| dcb42cc7-d9b7-3c6a-b4e6-c189c4991e25 | -7.5002 | -45.0538 | 2025-08-31 14:00:00 | GOES-19 | SÃO FÉLIX DE BALSAS | MARANHÃO | Brasil | 2110807 | 21 | 33 | nan | nan | nan | Cerrado | 100.6 |
| 5fd260dc-978f-3438-89ba-452e65083bad | -14.8208 | -46.7337 | 2025-08-31 14:00:00 | GOES-19 | FLORES DE GOIÁS | GOIÁS | Brasil | 5207907 | 52 | 33 | nan | nan | nan | Cerrado | 126.4 |
| 4bca6535-41c6-376f-92d6-e6e3b4d28ff6 | -15.7298 | -48.9446 | 2025-08-31 14:00:00 | GOES-19 | PIRENÓPOLIS | GOIÁS | Brasil | 5217302 | 52 | 33 | nan | nan | nan | Cerrado | 50.5 |
| 928fdbdc-9a46-3537-8704-a2e935791a60 | -11.0845 | -44.6343 | 2025-08-31 14:00:00 | GOES-19 | SANTA RITA DE CÁSSIA | BAHIA | Brasil | 2928406 | 29 | 33 | nan | nan | nan | Cerrado | 240.5 |
| 7f1ead2a-ab72-3294-926e-d84317508bd5 | -9.245 | -47.0824 | 2025-08-31 14:00:00 | GOES-19 | LIZARDA | TOCANTINS | Brasil | 1712405 | 17 | 33 | nan | nan | nan | Cerrado | 90.9 |
| 777fbfe3-6074-3d28-94fc-363d16f72b34 | -13.3636 | -46.95 | 2025-08-31 14:00:00 | GOES-19 | MONTE ALEGRE DE GOIÁS | GOIÁS | Brasil | 5213509 | 52 | 33 | nan | nan | nan | Cerrado | 78.4 |
| ab33a040-837e-353f-94c6-9bc0a784b1f2 | -6.2769 | -43.5512 | 2025-08-31 14:00:00 | GOES-19 | SUCUPIRA DO RIACHÃO | MARANHÃO | Brasil | 2111953 | 21 | 33 | nan | nan | nan | Cerrado | 64.7 |
| f4ce62d9-e79b-3ad7-b07f-d4c17c5c00c1 | -17.1536 | -46.0817 | 2025-08-31 14:00:00 | GOES-19 | JOÃO PINHEIRO | MINAS GERAIS | Brasil | 3136306 | 31 | 33 | nan | nan | nan | Cerrado | 77.6 |
| e1d8a722-7294-3782-98af-7b03e7769311 | -14.3343 | -51.8944 | 2025-08-31 14:00:00 | GOES-19 | NOVA NAZARÉ | MATO GROSSO | Brasil | 5106174 | 51 | 33 | nan | nan | nan | Cerrado | 104.4 |
| 1f7a1a25-c982-35e5-9653-c6fdede03312 | -13.3439 | -46.9757 | 2025-08-31 14:00:00 | GOES-19 | MONTE ALEGRE DE GOIÁS | GOIÁS | Brasil | 5213509 | 52 | 33 | nan | nan | nan | Cerrado | 67.0 |
| ffbfb2ee-a0fb-37e0-8f6c-cf1d60aea274 | -11.9147 | -46.3726 | 2025-08-31 14:00:00 | GOES-19 | PONTE ALTA DO BOM JESUS | TOCANTINS | Brasil | 1717800 | 17 | 33 | nan | nan | nan | Cerrado | 79.8 |
| 0b6b0717-a2a0-3bd7-bdc8-068e377c6d47 | -5.4824 | -44.3969 | 2025-08-31 14:10:00 | GOES-19 | SÃO DOMINGOS DO MARANHÃO | MARANHÃO | Brasil | 2110708 | 21 | 33 | nan | nan | nan | Cerrado | 106.7 |
| 02b702b5-4aee-35b2-9db9-1807ad54fa04 | -7.5002 | -45.0538 | 2025-08-31 14:10:00 | GOES-19 | SÃO FÉLIX DE BALSAS | MARANHÃO | Brasil | 2110807 | 21 | 33 | nan | nan | nan | Cerrado | 77.6 |
| 9d61b14b-0440-3dcc-a17d-76d5df6f01d0 | -5.6573 | -43.6465 | 2025-08-31 14:10:00 | GOES-19 | BURITI BRAVO | MARANHÃO | Brasil | 2102309 | 21 | 33 | nan | nan | nan | Cerrado | 96.4 |
| e186e45d-2053-38b5-8ab7-2928343cfad1 | -14.5646 | -51.9703 | 2025-08-31 14:10:00 | GOES-19 | NOVA NAZARÉ | MATO GROSSO | Brasil | 5106174 | 51 | 33 | nan | nan | nan | Cerrado | 62.9 |
| 1fcd03a5-469b-3de5-97a4-d0461e776cc8 | -8.6649 | -48.3057 | 2025-08-31 14:10:00 | GOES-19 | GUARAÍ | TOCANTINS | Brasil | 1709302 | 17 | 33 | nan | nan | nan | Cerrado | 85.5 |
| 509d2bf6-717e-3a27-8873-3fa2e4178275 | -8.8939 | -45.094 | 2025-08-31 14:10:00 | GOES-19 | BAIXA GRANDE DO RIBEIRO | PIAUÍ | Brasil | 2201150 | 22 | 33 | nan | nan | nan | Cerrado | 85.9 |
| d7a068b5-8bbf-3e86-ac0d-d4a9e325f712 | -10.0434 | -48.0998 | 2025-08-31 14:10:00 | GOES-19 | APARECIDA DO RIO NEGRO | TOCANTINS | Brasil | 1701101 | 17 | 33 | nan | nan | nan | Cerrado | 76.1 |
| 0266a1d1-27b5-34de-a042-ac872913783d | -6.1663 | -43.3506 | 2025-08-31 14:10:00 | GOES-19 | LAGOA DO MATO | MARANHÃO | Brasil | 2105922 | 21 | 33 | nan | nan | nan | Cerrado | 225.8 |
| f621da57-2dad-33dd-814a-54400ab116c4 | -7.8729 | -46.973 | 2025-08-31 14:10:00 | GOES-19 | CAROLINA | MARANHÃO | Brasil | 2102804 | 21 | 33 | nan | nan | nan | Cerrado | 279.1 |
| 00bc16de-8a75-3315-8a46-ce272dda3fb5 | -8.875 | -45.0961 | 2025-08-31 14:10:00 | GOES-19 | BAIXA GRANDE DO RIBEIRO | PIAUÍ | Brasil | 2201150 | 22 | 33 | nan | nan | nan | Cerrado | 100.1 |
| 4f3567e9-a7ec-3991-a4aa-2f8eef81e209 | -14.0307 | -44.5814 | 2025-08-31 14:10:00 | GOES-19 | COCOS | BAHIA | Brasil | 2908101 | 29 | 33 | nan | nan | nan | Cerrado | 118.7 |
| 696bd6af-e953-37c8-8ad2-666130245b05 | -6.185 | -43.3491 | 2025-08-31 14:10:00 | GOES-19 | LAGOA DO MATO | MARANHÃO | Brasil | 2105922 | 21 | 33 | nan | nan | nan | Cerrado | 125.3 |
| 363a2446-498c-33c3-8258-830e6b2537d1 | -15.7102 | -48.9479 | 2025-08-31 14:10:00 | GOES-19 | PIRENÓPOLIS | GOIÁS | Brasil | 5217302 | 52 | 33 | nan | nan | nan | Cerrado | 127.2 |
| c3fbea4c-5a34-353f-8743-a0fbe5fd9cba | -13.4006 | -47.0347 | 2025-08-31 14:10:00 | GOES-19 | MONTE ALEGRE DE GOIÁS | GOIÁS | Brasil | 5213509 | 52 | 33 | nan | nan | nan | Cerrado | 104.3 |
| 7e7e7fdd-7777-38f5-9d97-92342b299a1e | -13.4199 | -47.0317 | 2025-08-31 14:10:00 | GOES-19 | MONTE ALEGRE DE GOIÁS | GOIÁS | Brasil | 5213509 | 52 | 33 | nan | nan | nan | Cerrado | 65.7 |
| e9453b58-e537-3800-a122-29565e53f27b | -5.3472 | -47.2952 | 2025-08-31 14:10:00 | GOES-19 | JOÃO LISBOA | MARANHÃO | Brasil | 2105500 | 21 | 33 | nan | nan | nan | Amazônia | 62.4 |
| 75a879ce-9494-306e-a8e4-d993c8074f6f | -11.3317 | -43.6162 | 2025-08-31 14:10:00 | GOES-19 | BARRA | BAHIA | Brasil | 2902708 | 29 | 33 | nan | nan | nan | Cerrado | 146.0 |
| 076926d6-aca4-37d6-a5e7-6b3f9124c392 | -9.5139 | -45.3884 | 2025-08-31 14:10:00 | GOES-19 | GILBUÉS | PIAUÍ | Brasil | 2204402 | 22 | 33 | nan | nan | nan | Cerrado | 83.3 |
| 6aceccda-0d91-3770-a137-df91226d6114 | -7.1139 | -44.3111 | 2025-08-31 14:10:00 | GOES-19 | BENEDITO LEITE | MARANHÃO | Brasil | 2101806 | 21 | 33 | nan | nan | nan | Cerrado | 146.3 |
| df164f01-f52a-33c3-8f43-0270520440ac | -7.4178 | -47.4537 | 2025-08-31 14:10:00 | GOES-19 | CAROLINA | MARANHÃO | Brasil | 2102804 | 21 | 33 | nan | nan | nan | Cerrado | 108.2 |
| e1d1697b-b291-3b35-a7ec-4a82e3f4bb6a | -12.3287 | -45.7201 | 2025-08-31 14:10:00 | GOES-19 | LUÍS EDUARDO MAGALHÃES | BAHIA | Brasil | 2919553 | 29 | 33 | nan | nan | nan | Cerrado | 66.6 |
| 1ad2a6f2-4dfd-3bcc-b4ae-5361c0721cef | -14.5642 | -51.9917 | 2025-08-31 14:10:00 | GOES-19 | NOVA NAZARÉ | MATO GROSSO | Brasil | 5106174 | 51 | 33 | nan | nan | nan | Cerrado | 100.1 |
| cb38c93d-1616-3804-a9d0-d9421a865035 | -5.8696 | -42.9768 | 2025-08-31 14:10:00 | GOES-19 | PALMEIRAIS | PIAUÍ | Brasil | 2207504 | 22 | 33 | nan | nan | nan | Caatinga | 127.7 |
| c7531154-8b32-3bb9-b923-2bdb29b26a70 | -14.354 | -51.8705 | 2025-08-31 14:10:00 | GOES-19 | NOVA NAZARÉ | MATO GROSSO | Brasil | 5106174 | 51 | 33 | nan | nan | nan | Cerrado | 73.4 |
| 92824b9e-2b82-3c69-8c79-916c3fb3a04b | -11.3526 | -43.5187 | 2025-08-31 14:10:00 | GOES-19 | BARRA | BAHIA | Brasil | 2902708 | 29 | 33 | nan | nan | nan | Cerrado | 112.6 |
| e328b949-921b-3870-84d2-1af14ef0448f | -14.0508 | -44.5543 | 2025-08-31 14:10:00 | GOES-19 | COCOS | BAHIA | Brasil | 2908101 | 29 | 33 | nan | nan | nan | Cerrado | 88.7 |
| a8c32ea3-6284-35b8-ad61-7d2fb246535d | -15.6948 | -52.7312 | 2025-08-31 14:10:00 | GOES-19 | BARRA DO GARÇAS | MATO GROSSO | Brasil | 5101803 | 51 | 33 | nan | nan | nan | Cerrado | 70.3 |
| 97824ab8-aa0f-3694-b805-f61ed9f4e3e8 | -6.5812 | -44.9979 | 2025-08-31 14:10:00 | GOES-19 | MIRADOR | MARANHÃO | Brasil | 2106706 | 21 | 33 | nan | nan | nan | Cerrado | 148.9 |
| 4c285838-fc42-3615-9aa4-f86f019458e9 | -7.0951 | -44.3128 | 2025-08-31 14:10:00 | GOES-19 | BENEDITO LEITE | MARANHÃO | Brasil | 2101806 | 21 | 33 | nan | nan | nan | Cerrado | 116.4 |
| 152d71e7-ccfe-3b17-b44d-0a7a0b5b73ab | -13.4788 | -46.9774 | 2025-08-31 14:10:00 | GOES-19 | MONTE ALEGRE DE GOIÁS | GOIÁS | Brasil | 5213509 | 52 | 33 | nan | nan | nan | Cerrado | 74.8 |
| ced229ba-3908-3fdb-96f5-2ec6b4290ad8 | -6.2409 | -43.3911 | 2025-08-31 14:10:00 | GOES-19 | LAGOA DO MATO | MARANHÃO | Brasil | 2105922 | 21 | 33 | nan | nan | nan | Cerrado | 198.0 |
| 16472ffc-0284-334a-8a3a-6c8a7cc6261a | -12.3099 | -45.7 | 2025-08-31 14:10:00 | GOES-19 | LUÍS EDUARDO MAGALHÃES | BAHIA | Brasil | 2919553 | 29 | 33 | nan | nan | nan | Cerrado | 65.5 |
| bd3fe875-7307-3951-a1b5-f4e9e344828e | -9.2639 | -47.0804 | 2025-08-31 14:10:00 | GOES-19 | LIZARDA | TOCANTINS | Brasil | 1712405 | 17 | 33 | nan | nan | nan | Cerrado | 125.5 |
| 532e160c-75d0-375e-89e4-ffdafdf7261c | -11.0845 | -44.6343 | 2025-08-31 14:10:00 | GOES-19 | SANTA RITA DE CÁSSIA | BAHIA | Brasil | 2928406 | 29 | 33 | nan | nan | nan | Cerrado | 295.8 |
| af56b825-dcdd-3a18-9cb7-4e7212e4d2c9 | -12.1778 | -50.1126 | 2025-08-31 14:10:00 | GOES-19 | FORMOSO DO ARAGUAIA | TOCANTINS | Brasil | 1708205 | 17 | 33 | nan | nan | nan | Cerrado | 73.5 |
| dbe60884-2689-3989-8a67-d0825bd1a611 | -6.5021 | -43.5553 | 2025-08-31 14:10:00 | GOES-19 | SUCUPIRA DO RIACHÃO | MARANHÃO | Brasil | 2111953 | 21 | 33 | nan | nan | nan | Cerrado | 91.1 |
| 51a2c6e5-00ed-3c19-b703-652535ad0dac | -11.3312 | -43.6399 | 2025-08-31 14:10:00 | GOES-19 | BARRA | BAHIA | Brasil | 2902708 | 29 | 33 | nan | nan | nan | Cerrado | 481.2 |
| aa98e8d3-b99e-355e-ab65-58a5ac439103 | -11.8181 | -46.4314 | 2025-08-31 14:10:00 | GOES-19 | PONTE ALTA DO BOM JESUS | TOCANTINS | Brasil | 1717800 | 17 | 33 | nan | nan | nan | Cerrado | 96.9 |
| 70af6404-d149-31ea-a65c-0982fa628ddd | -11.0849 | -44.611 | 2025-08-31 14:10:00 | GOES-19 | SANTA RITA DE CÁSSIA | BAHIA | Brasil | 2928406 | 29 | 33 | nan | nan | nan | Cerrado | 244.4 |


[Clique aqui para ver as próximas entradas](README92.md)
