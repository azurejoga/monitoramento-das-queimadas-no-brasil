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

## Dados Diários - Página 37

| ID | Latitude | Longitude | Data/Hora GMT | Satélite | Município | Estado | País | Município ID | Estado ID | País ID | Dias sem Chuva | Precipitação | Risco de Fogo | Bioma | FRP |
|----|----------|-----------|---------------|----------|-----------|--------|------|--------------|-----------|---------|----------------|--------------|----------------|-------|-----|
| 3a7f8138-be28-3e29-b14d-e338a0200441 | -9.68982 | -47.05213 | 2025-08-30 04:21:00 | NOAA-21 | LIZARDA | TOCANTINS | Brasil | 1712405 | 17 | 33 | nan | nan | nan | Cerrado | 1.1 |
| 21453b47-b451-3491-8777-a670c5edd06d | -11.148 | -47.15253 | 2025-08-30 04:21:00 | NOAA-21 | ALMAS | TOCANTINS | Brasil | 1700400 | 17 | 33 | nan | nan | nan | Cerrado | 2.1 |
| f969f6b0-b401-3c42-b92f-f5bfef83c667 | -13.99961 | -44.57774 | 2025-08-30 04:21:00 | NOAA-21 | COCOS | BAHIA | Brasil | 2908101 | 29 | 33 | nan | nan | nan | Cerrado | 1.6 |
| 4903c25b-e099-3460-a717-1759556a0718 | -9.94091 | -44.02635 | 2025-08-30 04:21:00 | NOAA-21 | AVELINO LOPES | PIAUÍ | Brasil | 2201101 | 22 | 33 | nan | nan | nan | Cerrado | 1.6 |
| 275a6373-a000-3d90-a581-2bd19ff35aa3 | -14.35016 | -53.32569 | 2025-08-30 04:21:00 | NOAA-21 | CAMPINÁPOLIS | MATO GROSSO | Brasil | 5102603 | 51 | 33 | nan | nan | nan | Cerrado | 2.3 |
| 3af8bdb4-82c5-3275-b4ff-6c73004fac9f | -11.32635 | -43.63988 | 2025-08-30 04:21:00 | NOAA-21 | BARRA | BAHIA | Brasil | 2902708 | 29 | 33 | nan | nan | nan | Cerrado | 4.1 |
| fe1d8828-1f7d-3c12-9e20-bca6ae63dc83 | -9.50444 | -45.39001 | 2025-08-30 04:21:00 | NOAA-21 | GILBUÉS | PIAUÍ | Brasil | 2204402 | 22 | 33 | nan | nan | nan | Cerrado | 2.5 |
| 42b348ce-7afa-3016-bac4-9389d0ecca80 | -13.56579 | -46.92607 | 2025-08-30 04:21:00 | NOAA-21 | MONTE ALEGRE DE GOIÁS | GOIÁS | Brasil | 5213509 | 52 | 33 | nan | nan | nan | Cerrado | 1.5 |
| dd6d6159-caff-30a8-952c-2eac4646a180 | -9.47613 | -48.82648 | 2025-08-30 04:21:00 | NOAA-21 | DOIS IRMÃOS DO TOCANTINS | TOCANTINS | Brasil | 1707207 | 17 | 33 | nan | nan | nan | Cerrado | 1.4 |
| bd7341d4-6ffe-357c-8b06-14485340d9be | -12.63684 | -57.00871 | 2025-08-30 04:21:00 | NOAA-21 | NOVA MARINGÁ | MATO GROSSO | Brasil | 5108907 | 51 | 33 | nan | nan | nan | Amazônia | 3.6 |
| d0909a1f-1fe2-3e38-9c33-1e1fa457f9c7 | -14.0036 | -44.57449 | 2025-08-30 04:21:00 | NOAA-21 | COCOS | BAHIA | Brasil | 2908101 | 29 | 33 | nan | nan | nan | Cerrado | 3.8 |
| 61c9f67a-79f6-3697-b9f8-51087744aebd | -15.10068 | -48.39436 | 2025-08-30 04:21:00 | NOAA-21 | PADRE BERNARDO | GOIÁS | Brasil | 5215603 | 52 | 33 | nan | nan | nan | Cerrado | 1.4 |
| eb5eb740-5334-31de-831e-64cb6c12fbcc | -11.86735 | -46.39381 | 2025-08-30 04:21:00 | NOAA-21 | PONTE ALTA DO BOM JESUS | TOCANTINS | Brasil | 1717800 | 17 | 33 | nan | nan | nan | Cerrado | 3.8 |
| a45116af-4091-3fdb-9ef2-3bddf8a3f536 | -13.4575 | -46.94439 | 2025-08-30 04:21:00 | NOAA-21 | MONTE ALEGRE DE GOIÁS | GOIÁS | Brasil | 5213509 | 52 | 33 | nan | nan | nan | Cerrado | 3.2 |
| e02faf03-c647-375f-81d0-3d998ddb3460 | -11.37679 | -54.3431 | 2025-08-30 04:21:00 | NOAA-21 | UNIÃO DO SUL | MATO GROSSO | Brasil | 5108303 | 51 | 33 | nan | nan | nan | Amazônia | 1.9 |
| eaed2b06-5fe9-30d7-9d8d-0d5b4008c4ef | -14.46035 | -52.01375 | 2025-08-30 04:21:00 | NOAA-21 | NOVA NAZARÉ | MATO GROSSO | Brasil | 5106174 | 51 | 33 | nan | nan | nan | Cerrado | 1.4 |
| 25548799-b4dd-3029-88d3-485e2a503112 | -10.79433 | -49.59022 | 2025-08-30 04:21:00 | NOAA-21 | LAGOA DA CONFUSÃO | TOCANTINS | Brasil | 1711902 | 17 | 33 | nan | nan | nan | Cerrado | 1.5 |
| 7ff025d1-2b7a-33d0-aaee-1eeaa824d280 | -9.64317 | -48.31263 | 2025-08-30 04:21:00 | NOAA-21 | TOCANTÍNIA | TOCANTINS | Brasil | 1721109 | 17 | 33 | nan | nan | nan | Cerrado | 2.3 |
| ed62932d-9127-33e4-8f91-325e39f785ac | -15.17876 | -48.03266 | 2025-08-30 04:21:00 | NOAA-21 | PLANALTINA | GOIÁS | Brasil | 5217609 | 52 | 33 | nan | nan | nan | Cerrado | 1.1 |
| 1479681b-555a-3122-923f-97ee1b3011a2 | -13.45357 | -46.96922 | 2025-08-30 04:21:00 | NOAA-21 | MONTE ALEGRE DE GOIÁS | GOIÁS | Brasil | 5213509 | 52 | 33 | nan | nan | nan | Cerrado | 1.3 |
| 7cc7dbcf-93c0-3d6e-a16d-e05f91d44e25 | -14.99912 | -46.70165 | 2025-08-30 04:21:00 | NOAA-21 | FLORES DE GOIÁS | GOIÁS | Brasil | 5207907 | 52 | 33 | nan | nan | nan | Cerrado | 0.7 |
| b67c4e02-ba56-30bf-bb74-3e6a56dfe615 | -13.44037 | -46.94535 | 2025-08-30 04:21:00 | NOAA-21 | MONTE ALEGRE DE GOIÁS | GOIÁS | Brasil | 5213509 | 52 | 33 | nan | nan | nan | Cerrado | 1.3 |
| f57740e7-0e2d-3649-8a04-d0c68915a61e | -13.6428 | -48.15909 | 2025-08-30 04:21:00 | NOAA-21 | MINAÇU | GOIÁS | Brasil | 5213087 | 52 | 33 | nan | nan | nan | Cerrado | 2.5 |
| 915495cc-b48f-328a-a429-ad98086f0b56 | -15.10284 | -48.40239 | 2025-08-30 04:21:00 | NOAA-21 | PADRE BERNARDO | GOIÁS | Brasil | 5215603 | 52 | 33 | nan | nan | nan | Cerrado | 0.7 |
| 1a274f2e-f892-3e4a-a301-8f3f1dba5053 | -11.33519 | -43.28657 | 2025-08-30 04:21:00 | NOAA-21 | BARRA | BAHIA | Brasil | 2902708 | 29 | 33 | nan | nan | nan | Cerrado | 1.4 |
| f320845b-5732-376d-a9de-ab8d6d38aef8 | -11.31767 | -43.62658 | 2025-08-30 04:21:00 | NOAA-21 | BARRA | BAHIA | Brasil | 2902708 | 29 | 33 | nan | nan | nan | Cerrado | 1.7 |
| 53e78705-4dbb-37ed-b5cc-7fb830a6e270 | -13.38055 | -47.00106 | 2025-08-30 04:21:00 | NOAA-21 | MONTE ALEGRE DE GOIÁS | GOIÁS | Brasil | 5213509 | 52 | 33 | nan | nan | nan | Cerrado | 1.9 |
| b8e1a433-6922-326a-9852-ee206db83863 | -14.00123 | -44.54292 | 2025-08-30 04:21:00 | NOAA-21 | COCOS | BAHIA | Brasil | 2908101 | 29 | 33 | nan | nan | nan | Cerrado | 1.2 |
| f6610ebb-5bc7-347f-8e5b-436dd5497b00 | -13.36485 | -47.01325 | 2025-08-30 04:21:00 | NOAA-21 | MONTE ALEGRE DE GOIÁS | GOIÁS | Brasil | 5213509 | 52 | 33 | nan | nan | nan | Cerrado | 4.3 |
| 04a3aafb-3d7e-3414-91f0-9520c8149e36 | -10.71822 | -47.00875 | 2025-08-30 04:21:00 | NOAA-21 | PONTE ALTA DO TOCANTINS | TOCANTINS | Brasil | 1717909 | 17 | 33 | nan | nan | nan | Cerrado | 1.5 |
| d08e6c3a-4bda-3dcf-b752-e69227f0a8a9 | -11.32286 | -43.61541 | 2025-08-30 04:21:00 | NOAA-21 | BARRA | BAHIA | Brasil | 2902708 | 29 | 33 | nan | nan | nan | Cerrado | 1.5 |
| a4c6d740-87d5-3a93-88f3-e66ad9baf384 | -12.71593 | -48.19295 | 2025-08-30 04:21:00 | NOAA-21 | PARANÃ | TOCANTINS | Brasil | 1716208 | 17 | 33 | nan | nan | nan | Cerrado | 1.8 |
| 64430878-901a-3a71-aaee-2a7b65d0c0b1 | -9.2475 | -56.90034 | 2025-08-30 04:21:00 | NOAA-21 | PARANAÍTA | MATO GROSSO | Brasil | 5106299 | 51 | 33 | nan | nan | nan | Amazônia | 2.4 |
| d86e26ab-cf2c-3716-b2ac-78df68fcbc54 | -13.97679 | -46.3227 | 2025-08-30 04:21:00 | NOAA-21 | GUARANI DE GOIÁS | GOIÁS | Brasil | 5209408 | 52 | 33 | nan | nan | nan | Cerrado | 2.9 |
| 3426586f-8338-3c08-ac92-23e42261ccdc | -11.41689 | -46.91771 | 2025-08-30 04:21:00 | NOAA-21 | DIANÓPOLIS | TOCANTINS | Brasil | 1707009 | 17 | 33 | nan | nan | nan | Cerrado | 1.2 |
| 06af8f22-83cb-37fd-8b9b-3dd547b7dd44 | -13.38733 | -46.95845 | 2025-08-30 04:21:00 | NOAA-21 | MONTE ALEGRE DE GOIÁS | GOIÁS | Brasil | 5213509 | 52 | 33 | nan | nan | nan | Cerrado | 9.1 |
| 33f58f38-5eff-39ab-a8a9-999298436919 | -14.00416 | -44.57069 | 2025-08-30 04:21:00 | NOAA-21 | COCOS | BAHIA | Brasil | 2908101 | 29 | 33 | nan | nan | nan | Cerrado | 3.8 |
| 11f43747-791f-3a5c-8f3b-21c90ab3a415 | -10.03004 | -48.07529 | 2025-08-30 04:21:00 | NOAA-21 | APARECIDA DO RIO NEGRO | TOCANTINS | Brasil | 1701101 | 17 | 33 | nan | nan | nan | Cerrado | 0.6 |
| d00da898-c6af-32f0-8000-601df80a3c94 | -13.38329 | -47.00518 | 2025-08-30 04:21:00 | NOAA-21 | MONTE ALEGRE DE GOIÁS | GOIÁS | Brasil | 5213509 | 52 | 33 | nan | nan | nan | Cerrado | 10.3 |
| ec3a4b62-a95b-316e-94df-eb256215b601 | -11.40138 | -46.90791 | 2025-08-30 04:21:00 | NOAA-21 | DIANÓPOLIS | TOCANTINS | Brasil | 1707009 | 17 | 33 | nan | nan | nan | Cerrado | 1.3 |
| ecb6f845-fb24-37e4-9cd9-3e4a2b089cd5 | -13.96468 | -46.33524 | 2025-08-30 04:21:00 | NOAA-21 | GUARANI DE GOIÁS | GOIÁS | Brasil | 5209408 | 52 | 33 | nan | nan | nan | Cerrado | 2.0 |
| 165c0735-4cfe-3b6f-9c3f-a46cbfd72faf | -14.85489 | -46.77582 | 2025-08-30 04:21:00 | NOAA-21 | FLORES DE GOIÁS | GOIÁS | Brasil | 5207907 | 52 | 33 | nan | nan | nan | Cerrado | 2.3 |
| 6da4df2c-b79c-3f73-bc3f-8ff840e1a508 | -9.11176 | -46.0477 | 2025-08-30 04:21:00 | NOAA-21 | ALTO PARNAÍBA | MARANHÃO | Brasil | 2100501 | 21 | 33 | nan | nan | nan | Cerrado | 3.0 |
| 3a710cb6-8313-33c6-9836-07822015941f | -10.37178 | -57.82879 | 2025-08-30 04:21:00 | NOAA-21 | NOVA BANDEIRANTES | MATO GROSSO | Brasil | 5106158 | 51 | 33 | nan | nan | nan | Amazônia | 2.9 |
| a4d979e3-5689-3b68-9f4c-66b90534e13b | -11.34366 | -43.52267 | 2025-08-30 04:21:00 | NOAA-21 | BARRA | BAHIA | Brasil | 2902708 | 29 | 33 | nan | nan | nan | Cerrado | 1.9 |
| cc7b47ed-7d6a-38d7-8877-1bde3dbb4450 | -10.02219 | -48.10165 | 2025-08-30 04:21:00 | NOAA-21 | APARECIDA DO RIO NEGRO | TOCANTINS | Brasil | 1701101 | 17 | 33 | nan | nan | nan | Cerrado | 1.2 |
| 23495a58-e677-3763-b6ec-8df05ab8210e | -11.84968 | -46.44136 | 2025-08-30 04:21:00 | NOAA-21 | PONTE ALTA DO BOM JESUS | TOCANTINS | Brasil | 1717800 | 17 | 33 | nan | nan | nan | Cerrado | 3.5 |
| 8c5d38b7-f1ce-36dc-a44d-54291a10a2a3 | -13.59898 | -46.88793 | 2025-08-30 04:21:00 | NOAA-21 | MONTE ALEGRE DE GOIÁS | GOIÁS | Brasil | 5213509 | 52 | 33 | nan | nan | nan | Cerrado | 3.7 |
| d84c3d5b-2909-3f8e-b734-341d58fc8b45 | -13.19746 | -45.29187 | 2025-08-30 04:21:00 | NOAA-21 | CORRENTINA | BAHIA | Brasil | 2909307 | 29 | 33 | nan | nan | nan | Cerrado | 2.5 |
| 2d943878-002d-3137-be7b-448f53fc4a53 | -10.0789 | -54.93216 | 2025-08-30 04:21:00 | NOAA-21 | MATUPÁ | MATO GROSSO | Brasil | 5105606 | 51 | 33 | nan | nan | nan | Amazônia | 5.9 |
| 90c7d5bf-d35c-3bae-9f1c-44e5326eefae | -11.41527 | -46.90646 | 2025-08-30 04:21:00 | NOAA-21 | DIANÓPOLIS | TOCANTINS | Brasil | 1707009 | 17 | 33 | nan | nan | nan | Cerrado | 1.0 |
| 98ade955-b7d8-3a16-b82a-3b9be2a01b62 | -12.39852 | -46.49887 | 2025-08-30 04:21:00 | NOAA-21 | TAGUATINGA | TOCANTINS | Brasil | 1720903 | 17 | 33 | nan | nan | nan | Cerrado | 1.8 |
| 704b596b-1a04-3207-ab16-926592128e81 | -13.39784 | -46.95649 | 2025-08-30 04:21:00 | NOAA-21 | MONTE ALEGRE DE GOIÁS | GOIÁS | Brasil | 5213509 | 52 | 33 | nan | nan | nan | Cerrado | 3.5 |
| af2a9fb5-12e9-3028-89ce-f25fd3cfd21b | -12.82585 | -48.12262 | 2025-08-30 04:21:00 | NOAA-21 | PARANÃ | TOCANTINS | Brasil | 1716208 | 17 | 33 | nan | nan | nan | Cerrado | 3.7 |
| 9a2916f2-e351-3564-84d4-9c64c984a615 | -12.84813 | -48.15752 | 2025-08-30 04:21:00 | NOAA-21 | PARANÃ | TOCANTINS | Brasil | 1716208 | 17 | 33 | nan | nan | nan | Cerrado | 2.2 |
| 3a54197b-8ca4-36a8-906f-d1670b4cd465 | -13.41608 | -46.94859 | 2025-08-30 04:21:00 | NOAA-21 | MONTE ALEGRE DE GOIÁS | GOIÁS | Brasil | 5213509 | 52 | 33 | nan | nan | nan | Cerrado | 2.2 |
| b6a2cb99-9d67-3dd4-a8cd-2b984056fdb8 | -11.89123 | -46.71544 | 2025-08-30 04:21:00 | NOAA-21 | NOVO JARDIM | TOCANTINS | Brasil | 1715259 | 17 | 33 | nan | nan | nan | Cerrado | 3.5 |
| 6dea19f6-0fb9-3b0c-8725-cc3a9c646cc5 | -8.69481 | -50.37886 | 2025-08-30 04:21:00 | NOAA-21 | SANTA MARIA DAS BARREIRAS | PARÁ | Brasil | 1506583 | 15 | 33 | nan | nan | nan | Amazônia | 1.2 |
| 78004f62-4787-382a-864a-ca5729d7a6bc | -13.99325 | -44.54947 | 2025-08-30 04:21:00 | NOAA-21 | COCOS | BAHIA | Brasil | 2908101 | 29 | 33 | nan | nan | nan | Cerrado | 1.5 |
| cb452ec9-66b7-3d51-af06-a8e93e8a6701 | -12.0578 | -46.63091 | 2025-08-30 04:21:00 | NOAA-21 | PONTE ALTA DO BOM JESUS | TOCANTINS | Brasil | 1717800 | 17 | 33 | nan | nan | nan | Cerrado | 0.8 |
| e70a734c-6d1b-3aa6-8afd-bbe6b922085c | -14.85103 | -46.77882 | 2025-08-30 04:21:00 | NOAA-21 | FLORES DE GOIÁS | GOIÁS | Brasil | 5207907 | 52 | 33 | nan | nan | nan | Cerrado | 2.3 |
| 6d543fd6-416f-37c0-91c9-5269232e4ca7 | -13.39105 | -46.99914 | 2025-08-30 04:21:00 | NOAA-21 | MONTE ALEGRE DE GOIÁS | GOIÁS | Brasil | 5213509 | 52 | 33 | nan | nan | nan | Cerrado | 4.2 |
| bd5496a4-bd0b-3996-bd79-56afc2ae15b8 | -12.15451 | -47.19716 | 2025-08-30 04:21:00 | NOAA-21 | CONCEIÇÃO DO TOCANTINS | TOCANTINS | Brasil | 1705607 | 17 | 33 | nan | nan | nan | Cerrado | 1.9 |
| 96c5beb7-b4b9-3f4e-b18a-a76181533311 | -14.34714 | -51.89717 | 2025-08-30 04:21:00 | NOAA-21 | NOVA NAZARÉ | MATO GROSSO | Brasil | 5106174 | 51 | 33 | nan | nan | nan | Cerrado | 1.4 |
| 63a40f22-21e6-37b5-9af7-12dbf6c0e780 | -10.99874 | -46.95533 | 2025-08-30 04:21:00 | NOAA-21 | PONTE ALTA DO TOCANTINS | TOCANTINS | Brasil | 1717909 | 17 | 33 | nan | nan | nan | Cerrado | 4.9 |
| 132e9e61-faf0-353e-88bc-1c04529d44d3 | -14.32795 | -51.95776 | 2025-08-30 04:21:00 | NOAA-21 | NOVA NAZARÉ | MATO GROSSO | Brasil | 5106174 | 51 | 33 | nan | nan | nan | Cerrado | 2.0 |
| f1246a96-1154-3f03-ac16-caabf78a0956 | -11.33577 | -43.28254 | 2025-08-30 04:21:00 | NOAA-21 | BARRA | BAHIA | Brasil | 2902708 | 29 | 33 | nan | nan | nan | Cerrado | 0.8 |
| 47e71a6b-a775-3662-a711-21b0ce9ed533 | -13.66325 | -46.86986 | 2025-08-30 04:21:00 | NOAA-21 | NOVA ROMA | GOIÁS | Brasil | 5214903 | 52 | 33 | nan | nan | nan | Cerrado | 0.8 |
| 0756b29d-7779-36e5-9d03-3474fad30f08 | -11.83338 | -46.86576 | 2025-08-30 04:21:00 | NOAA-21 | DIANÓPOLIS | TOCANTINS | Brasil | 1707009 | 17 | 33 | nan | nan | nan | Cerrado | 1.7 |
| 13f7ba75-fb89-3dd3-9f6a-18047b6032c4 | -8.68596 | -50.40631 | 2025-08-30 04:21:00 | NOAA-21 | SANTA MARIA DAS BARREIRAS | PARÁ | Brasil | 1506583 | 15 | 33 | nan | nan | nan | Amazônia | 2.7 |
| efceb04c-326f-3da8-a4f5-02e27aab7637 | -11.34483 | -43.58703 | 2025-08-30 04:21:00 | NOAA-21 | BARRA | BAHIA | Brasil | 2902708 | 29 | 33 | nan | nan | nan | Cerrado | 2.1 |
| 3d8e5c31-6157-3176-afe6-d55338be84eb | -14.00877 | -44.58695 | 2025-08-30 04:21:00 | NOAA-21 | COCOS | BAHIA | Brasil | 2908101 | 29 | 33 | nan | nan | nan | Cerrado | 4.3 |
| 21a09549-0bcf-3d3d-a531-0130a71e76fb | -11.83534 | -46.44626 | 2025-08-30 04:21:00 | NOAA-21 | PONTE ALTA DO BOM JESUS | TOCANTINS | Brasil | 1717800 | 17 | 33 | nan | nan | nan | Cerrado | 11.7 |
| 619bf150-3190-3070-a487-014639799269 | -9.64382 | -48.30867 | 2025-08-30 04:21:00 | NOAA-21 | TOCANTÍNIA | TOCANTINS | Brasil | 1721109 | 17 | 33 | nan | nan | nan | Cerrado | 2.6 |
| 95242442-a688-3163-9f92-f38c0cfad5ae | -13.54808 | -46.95217 | 2025-08-30 04:21:00 | NOAA-21 | MONTE ALEGRE DE GOIÁS | GOIÁS | Brasil | 5213509 | 52 | 33 | nan | nan | nan | Cerrado | 1.0 |
| 9bbcdd51-0a8c-3423-b3ac-01f300eb9a30 | -12.70038 | -46.80538 | 2025-08-30 04:21:00 | NOAA-21 | ARRAIAS | TOCANTINS | Brasil | 1702406 | 17 | 33 | nan | nan | nan | Cerrado | 1.8 |
| f4d48a70-38a8-3b01-b2f8-843a207012a2 | -11.41173 | -44.68063 | 2025-08-30 04:21:00 | NOAA-21 | COTEGIPE | BAHIA | Brasil | 2909406 | 29 | 33 | nan | nan | nan | Cerrado | 3.1 |
| ede15844-113b-34d5-a789-20d6b13ef1e0 | -13.46744 | -46.94593 | 2025-08-30 04:21:00 | NOAA-21 | MONTE ALEGRE DE GOIÁS | GOIÁS | Brasil | 5213509 | 52 | 33 | nan | nan | nan | Cerrado | 3.3 |
| c0c37e8f-cea5-3220-8a43-5d5e6a450780 | -11.8866 | -46.42219 | 2025-08-30 04:21:00 | NOAA-21 | PONTE ALTA DO BOM JESUS | TOCANTINS | Brasil | 1717800 | 17 | 33 | nan | nan | nan | Cerrado | 1.7 |
| 36c7e8ea-6dd1-3b78-a6e4-3ea1dc5507b4 | -11.22727 | -45.01958 | 2025-08-30 04:21:00 | NOAA-21 | FORMOSA DO RIO PRETO | BAHIA | Brasil | 2911105 | 29 | 33 | nan | nan | nan | Cerrado | 1.2 |
| d7bae99a-7c8a-30a1-8478-d0fff15a89d2 | -10.70231 | -47.06522 | 2025-08-30 04:21:00 | NOAA-21 | PONTE ALTA DO TOCANTINS | TOCANTINS | Brasil | 1717909 | 17 | 33 | nan | nan | nan | Cerrado | 0.9 |
| 2afea754-e94e-3808-8fc0-db3ea84c766a | -9.12401 | -45.21125 | 2025-08-30 04:21:00 | NOAA-21 | BAIXA GRANDE DO RIBEIRO | PIAUÍ | Brasil | 2201150 | 22 | 33 | nan | nan | nan | Cerrado | 1.5 |
| 0c21e9eb-8341-33fc-bf17-b4b524295e86 | -11.86187 | -46.38567 | 2025-08-30 04:21:00 | NOAA-21 | PONTE ALTA DO BOM JESUS | TOCANTINS | Brasil | 1717800 | 17 | 33 | nan | nan | nan | Cerrado | 1.5 |
| 9ec77e76-de43-32a3-ad9f-4930a83be63c | -12.37112 | -46.38997 | 2025-08-30 04:21:00 | NOAA-21 | TAGUATINGA | TOCANTINS | Brasil | 1720903 | 17 | 33 | nan | nan | nan | Cerrado | 3.2 |
| b2d34083-ee79-3f0e-a57d-8b5f75332b30 | -12.8969 | -48.88545 | 2025-08-30 04:21:00 | NOAA-21 | PORANGATU | GOIÁS | Brasil | 5218003 | 52 | 33 | nan | nan | nan | Cerrado | 1.9 |
| 2923379c-c401-3da4-b59a-498194a7c041 | -12.83019 | -48.09594 | 2025-08-30 04:21:00 | NOAA-21 | PARANÃ | TOCANTINS | Brasil | 1716208 | 17 | 33 | nan | nan | nan | Cerrado | 1.1 |
| 154dd60b-6926-3258-bc44-eb9a859f2215 | -11.92562 | -46.69252 | 2025-08-30 04:21:00 | NOAA-21 | NOVO JARDIM | TOCANTINS | Brasil | 1715259 | 17 | 33 | nan | nan | nan | Cerrado | 4.3 |
| 2085ff36-cf80-3bc2-8547-62ac4118b3dc | -11.3142 | -43.62605 | 2025-08-30 04:21:00 | NOAA-21 | BARRA | BAHIA | Brasil | 2902708 | 29 | 33 | nan | nan | nan | Cerrado | 1.7 |
| d8712f7a-c081-3020-8b7b-f5d6354fed34 | -12.40957 | -46.47179 | 2025-08-30 04:21:00 | NOAA-21 | TAGUATINGA | TOCANTINS | Brasil | 1720903 | 17 | 33 | nan | nan | nan | Cerrado | 1.2 |
| c5a49ed5-1bc2-3a7f-9ee1-b8ac6bcd83f0 | -9.14354 | -49.61968 | 2025-08-30 04:21:00 | NOAA-21 | ARAGUACEMA | TOCANTINS | Brasil | 1701903 | 17 | 33 | nan | nan | nan | Cerrado | 3.2 |
| dfb494c8-7f58-3bcf-9ae3-541372fbf0e6 | -13.40697 | -47.02731 | 2025-08-30 04:21:00 | NOAA-21 | MONTE ALEGRE DE GOIÁS | GOIÁS | Brasil | 5213509 | 52 | 33 | nan | nan | nan | Cerrado | 2.1 |
| acb4db5f-d83e-3c37-9ab6-ba4e4a3a6b1a | -13.38119 | -46.97568 | 2025-08-30 04:21:00 | NOAA-21 | MONTE ALEGRE DE GOIÁS | GOIÁS | Brasil | 5213509 | 52 | 33 | nan | nan | nan | Cerrado | 4.0 |
| 180886d6-24fd-3b9e-9019-c19767a15813 | -13.47484 | -42.48067 | 2025-08-30 04:21:00 | NOAA-21 | TANQUE NOVO | BAHIA | Brasil | 2931053 | 29 | 33 | nan | nan | nan | Caatinga | 1.0 |
| 50502c4c-1b5b-3e88-b06f-a12ff6c99e07 | -14.49582 | -52.05055 | 2025-08-30 04:21:00 | NOAA-21 | NOVA NAZARÉ | MATO GROSSO | Brasil | 5106174 | 51 | 33 | nan | nan | nan | Cerrado | 3.7 |
| 10cac721-017b-3f86-94e8-9a97ee366628 | -14.0418 | -44.50597 | 2025-08-30 04:21:00 | NOAA-21 | COCOS | BAHIA | Brasil | 2908101 | 29 | 33 | nan | nan | nan | Cerrado | 2.0 |
| 01fd7076-f7be-3448-b48d-c3888a637b5b | -10.3832 | -57.83733 | 2025-08-30 04:21:00 | NOAA-21 | NOVA BANDEIRANTES | MATO GROSSO | Brasil | 5106158 | 51 | 33 | nan | nan | nan | Amazônia | 3.1 |
| ad13783f-f3bd-3402-9e09-afd02d260a9b | -13.38272 | -47.00873 | 2025-08-30 04:21:00 | NOAA-21 | MONTE ALEGRE DE GOIÁS | GOIÁS | Brasil | 5213509 | 52 | 33 | nan | nan | nan | Cerrado | 10.3 |
| 71e90f95-48af-38f5-8d62-335e5f238d05 | -11.33209 | -43.60104 | 2025-08-30 04:21:00 | NOAA-21 | BARRA | BAHIA | Brasil | 2902708 | 29 | 33 | nan | nan | nan | Cerrado | 6.4 |
| 438890dd-0d23-3ab3-9099-a526c35d1a17 | -13.68027 | -46.9125 | 2025-08-30 04:21:00 | NOAA-21 | NOVA ROMA | GOIÁS | Brasil | 5214903 | 52 | 33 | nan | nan | nan | Cerrado | 1.1 |
| e07adac8-fe85-3dee-9519-4c6b2ca7812c | -13.65938 | -46.87285 | 2025-08-30 04:21:00 | NOAA-21 | NOVA ROMA | GOIÁS | Brasil | 5214903 | 52 | 33 | nan | nan | nan | Cerrado | 0.8 |


[Clique aqui para ver as próximas entradas](README38.md)
