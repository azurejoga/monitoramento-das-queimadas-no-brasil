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

## Dados Diários - Página 45

| ID | Latitude | Longitude | Data/Hora GMT | Satélite | Município | Estado | País | Município ID | Estado ID | País ID | Dias sem Chuva | Precipitação | Risco de Fogo | Bioma | FRP |
|----|----------|-----------|---------------|----------|-----------|--------|------|--------------|-----------|---------|----------------|--------------|----------------|-------|-----|
| 18e3e7b9-3c69-3f30-b198-d72cd8ee5ead | -11.94666 | -46.69437 | 2025-08-31 04:29:00 | NPP-375D | NOVO JARDIM | TOCANTINS | Brasil | 1715259 | 17 | 33 | nan | nan | nan | Cerrado | 1.7 |
| f6da3661-b5c5-3944-937e-a28dca5fd040 | -13.35151 | -46.96875 | 2025-08-31 04:29:00 | NPP-375D | MONTE ALEGRE DE GOIÁS | GOIÁS | Brasil | 5213509 | 52 | 33 | nan | nan | nan | Cerrado | 2.0 |
| 050fb263-a3ff-3bb9-9694-a9af97a0d942 | -13.48221 | -46.96729 | 2025-08-31 04:29:00 | NPP-375D | MONTE ALEGRE DE GOIÁS | GOIÁS | Brasil | 5213509 | 52 | 33 | nan | nan | nan | Cerrado | 1.9 |
| 41cadbee-243c-3997-bf22-730e063c9f52 | -11.29245 | -43.63837 | 2025-08-31 04:29:00 | NPP-375D | BARRA | BAHIA | Brasil | 2902708 | 29 | 33 | nan | nan | nan | Cerrado | 1.9 |
| db4b2d93-29ca-3990-962b-afd1294f43cb | -11.32962 | -43.64413 | 2025-08-31 04:29:00 | NPP-375D | BARRA | BAHIA | Brasil | 2902708 | 29 | 33 | nan | nan | nan | Cerrado | 1.7 |
| 2a7df2fd-2ebb-3861-901b-afed8ea5f567 | -12.31622 | -45.71718 | 2025-08-31 04:29:00 | NPP-375D | LUÍS EDUARDO MAGALHÃES | BAHIA | Brasil | 2919553 | 29 | 33 | nan | nan | nan | Cerrado | 0.8 |
| 09cef7fc-ed01-321e-b231-46f86490bbab | -13.55592 | -46.95663 | 2025-08-31 04:29:00 | NPP-375D | MONTE ALEGRE DE GOIÁS | GOIÁS | Brasil | 5213509 | 52 | 33 | nan | nan | nan | Cerrado | 0.5 |
| dcbc3ba3-1073-3050-ab8e-44095ad7b217 | -12.86051 | -48.08463 | 2025-08-31 04:29:00 | NPP-375D | PARANÃ | TOCANTINS | Brasil | 1716208 | 17 | 33 | nan | nan | nan | Cerrado | 3.5 |
| 565404d2-3225-3a3e-ba35-5dadbba7c52e | -11.33903 | -43.6318 | 2025-08-31 04:29:00 | NPP-375D | BARRA | BAHIA | Brasil | 2902708 | 29 | 33 | nan | nan | nan | Cerrado | 1.6 |
| d1fb6ed9-7747-392b-ba8b-1fd4251ad245 | -13.3687 | -46.95647 | 2025-08-31 04:29:00 | NPP-375D | MONTE ALEGRE DE GOIÁS | GOIÁS | Brasil | 5213509 | 52 | 33 | nan | nan | nan | Cerrado | 3.0 |
| 2d9a900e-4db7-31d5-89fe-26d4eea5b4c9 | -11.36386 | -43.56643 | 2025-08-31 04:29:00 | NPP-375D | BARRA | BAHIA | Brasil | 2902708 | 29 | 33 | nan | nan | nan | Cerrado | 1.6 |
| 073ed0ed-a751-32be-95ff-dff05ebeade7 | -13.02489 | -56.89167 | 2025-08-31 04:29:00 | NPP-375D | NOVA MARINGÁ | MATO GROSSO | Brasil | 5108907 | 51 | 33 | nan | nan | nan | Amazônia | 1.5 |
| 00ef0d65-b45d-30c0-9114-a3e4cdd74a5b | -13.34092 | -46.99274 | 2025-08-31 04:29:00 | NPP-375D | MONTE ALEGRE DE GOIÁS | GOIÁS | Brasil | 5213509 | 52 | 33 | nan | nan | nan | Cerrado | 1.4 |
| a9c3703a-95c4-38c7-aace-6746c561a434 | -13.35596 | -46.96214 | 2025-08-31 04:29:00 | NPP-375D | MONTE ALEGRE DE GOIÁS | GOIÁS | Brasil | 5213509 | 52 | 33 | nan | nan | nan | Cerrado | 2.9 |
| 51137150-1ddc-37d0-b838-78b936e7746f | -10.59983 | -44.32747 | 2025-08-31 04:29:00 | NPP-375D | SANTA RITA DE CÁSSIA | BAHIA | Brasil | 2928406 | 29 | 33 | nan | nan | nan | Cerrado | 7.5 |
| 710a8dfa-e07a-361b-8e21-636636ecbe67 | -13.35369 | -46.86612 | 2025-08-31 04:29:00 | NPP-375D | MONTE ALEGRE DE GOIÁS | GOIÁS | Brasil | 5213509 | 52 | 33 | nan | nan | nan | Cerrado | 1.3 |
| 9e8a56a1-5c8e-3595-8df3-eea65b43b2f2 | -11.86446 | -46.50595 | 2025-08-31 04:29:00 | NPP-375D | PONTE ALTA DO BOM JESUS | TOCANTINS | Brasil | 1717800 | 17 | 33 | nan | nan | nan | Cerrado | 2.9 |
| d91832a3-7b8a-3e5e-bd9d-c87874f2edd0 | -12.40382 | -46.46866 | 2025-08-31 04:29:00 | NPP-375D | TAGUATINGA | TOCANTINS | Brasil | 1720903 | 17 | 33 | nan | nan | nan | Cerrado | 1.5 |
| 43bd780a-1017-3f54-b455-e23266bece6d | -11.35019 | -43.63354 | 2025-08-31 04:29:00 | NPP-375D | BARRA | BAHIA | Brasil | 2902708 | 29 | 33 | nan | nan | nan | Cerrado | 12.9 |
| d8a2b8c4-7887-3e27-8e4d-aa9c488bccf1 | -10.03528 | -48.09 | 2025-08-31 04:29:00 | NPP-375D | APARECIDA DO RIO NEGRO | TOCANTINS | Brasil | 1701101 | 17 | 33 | nan | nan | nan | Cerrado | 8.0 |
| f188c6ef-e01e-34ab-adf8-58d9a31c9cbb | -11.35654 | -43.61624 | 2025-08-31 04:29:00 | NPP-375D | BARRA | BAHIA | Brasil | 2902708 | 29 | 33 | nan | nan | nan | Cerrado | 2.3 |
| 142a10aa-b367-3810-a8c5-fa813d7f4380 | -11.88435 | -46.35477 | 2025-08-31 04:29:00 | NPP-375D | PONTE ALTA DO BOM JESUS | TOCANTINS | Brasil | 1717800 | 17 | 33 | nan | nan | nan | Cerrado | 1.4 |
| caa781b8-7d09-3abb-b4f8-d7c48a46915b | -13.33146 | -43.19455 | 2025-08-31 04:29:00 | NPP-375D | BOM JESUS DA LAPA | BAHIA | Brasil | 2903904 | 29 | 33 | nan | nan | nan | Caatinga | 1.6 |
| aff87242-1958-3e59-a786-d6d5cdb738b0 | -9.68324 | -47.0449 | 2025-08-31 04:29:00 | NPP-375D | LIZARDA | TOCANTINS | Brasil | 1712405 | 17 | 33 | nan | nan | nan | Cerrado | 1.0 |
| cdef07c2-b947-3bef-8a80-f88bc999930a | -12.75587 | -44.41308 | 2025-08-31 04:29:00 | NPP-375D | BAIANÓPOLIS | BAHIA | Brasil | 2902500 | 29 | 33 | nan | nan | nan | Cerrado | 1.1 |
| 4ebf95ed-6055-3847-8152-ae82a46c533b | -10.10391 | -49.28082 | 2025-08-31 04:29:00 | NPP-375D | CHAPADA DE AREIA | TOCANTINS | Brasil | 1704600 | 17 | 33 | nan | nan | nan | Cerrado | 2.5 |
| be885969-6730-30be-ad17-b4b183238066 | -11.36212 | -43.55226 | 2025-08-31 04:29:00 | NPP-375D | BARRA | BAHIA | Brasil | 2902708 | 29 | 33 | nan | nan | nan | Cerrado | 1.6 |
| 096d19f2-c7a6-3339-bdac-18699cdbb0da | -13.46882 | -46.96519 | 2025-08-31 04:29:00 | NPP-375D | MONTE ALEGRE DE GOIÁS | GOIÁS | Brasil | 5213509 | 52 | 33 | nan | nan | nan | Cerrado | 1.4 |
| db15b5c4-baa4-3a45-803f-71a8b1bc6cdd | -13.46329 | -46.97876 | 2025-08-31 04:29:00 | NPP-375D | MONTE ALEGRE DE GOIÁS | GOIÁS | Brasil | 5213509 | 52 | 33 | nan | nan | nan | Cerrado | 1.6 |
| 1a13fa86-5cbb-3842-ba98-015422e8dd21 | -13.66956 | -46.87544 | 2025-08-31 04:29:00 | NPP-375D | NOVA ROMA | GOIÁS | Brasil | 5214903 | 52 | 33 | nan | nan | nan | Cerrado | 1.2 |
| 33b12fd2-f1fb-377d-bb6e-51783e252d60 | -11.30037 | -43.66248 | 2025-08-31 04:29:00 | NPP-375D | BARRA | BAHIA | Brasil | 2902708 | 29 | 33 | nan | nan | nan | Cerrado | 1.1 |
| 67c39585-d0b9-397c-8453-00353caf8326 | -14.63502 | -48.07376 | 2025-08-31 04:29:00 | NPP-375D | NIQUELÂNDIA | GOIÁS | Brasil | 5214606 | 52 | 33 | nan | nan | nan | Cerrado | 2.4 |
| 79bbb31b-05b6-30e8-b1d4-fddc0b785c10 | -13.56541 | -46.93969 | 2025-08-31 04:29:00 | NPP-375D | MONTE ALEGRE DE GOIÁS | GOIÁS | Brasil | 5213509 | 52 | 33 | nan | nan | nan | Cerrado | 0.4 |
| a7e9b791-1e8a-31f2-9540-410d2816c0ca | -9.69708 | -47.04359 | 2025-08-31 04:29:00 | NPP-375D | LIZARDA | TOCANTINS | Brasil | 1712405 | 17 | 33 | nan | nan | nan | Cerrado | 1.5 |
| 3ddd3f6a-8bc8-36fa-902c-b3e7af0be418 | -11.07472 | -44.61658 | 2025-08-31 04:29:00 | NPP-375D | SANTA RITA DE CÁSSIA | BAHIA | Brasil | 2928406 | 29 | 33 | nan | nan | nan | Cerrado | 1.7 |
| ee5c324b-bb7f-39b5-89d8-6666662b4765 | -13.51458 | -46.97983 | 2025-08-31 04:29:00 | NPP-375D | MONTE ALEGRE DE GOIÁS | GOIÁS | Brasil | 5213509 | 52 | 33 | nan | nan | nan | Cerrado | 1.1 |
| 0d80fa8f-de96-383e-a6ef-4d320881b764 | -14.3421 | -51.88017 | 2025-08-31 04:29:00 | NPP-375D | NOVA NAZARÉ | MATO GROSSO | Brasil | 5106174 | 51 | 33 | nan | nan | nan | Cerrado | 7.4 |
| 7d841228-16e3-3aae-b0f0-098153e50789 | -13.02176 | -56.90804 | 2025-08-31 04:29:00 | NPP-375D | NOVA MARINGÁ | MATO GROSSO | Brasil | 5108907 | 51 | 33 | nan | nan | nan | Amazônia | 0.9 |
| 19b69a57-0a18-3db5-a3ca-62790b7aca35 | -13.34776 | -51.76598 | 2025-08-31 04:29:00 | NPP-375D | RIBEIRÃO CASCALHEIRA | MATO GROSSO | Brasil | 5107180 | 51 | 33 | nan | nan | nan | Cerrado | 2.0 |
| 95291404-ba85-318a-829c-c8386808c4df | -11.894 | -46.42603 | 2025-08-31 04:29:00 | NPP-375D | PONTE ALTA DO BOM JESUS | TOCANTINS | Brasil | 1717800 | 17 | 33 | nan | nan | nan | Cerrado | 0.8 |
| 3bfc2bc1-52d7-31c2-972b-b15ec3ef3d81 | -11.07083 | -52.02355 | 2025-08-31 04:29:00 | NPP-375D | CANABRAVA DO NORTE | MATO GROSSO | Brasil | 5102694 | 51 | 33 | nan | nan | nan | Amazônia | 2.6 |
| 29bfcf1b-1abf-3ad9-878d-19647a35a093 | -13.33076 | -43.19957 | 2025-08-31 04:29:00 | NPP-375D | BOM JESUS DA LAPA | BAHIA | Brasil | 2903904 | 29 | 33 | nan | nan | nan | Caatinga | 1.3 |
| 6a6c5620-ee9d-34f6-b010-2227de72aa24 | -13.03019 | -56.91383 | 2025-08-31 04:29:00 | NPP-375D | NOVA MARINGÁ | MATO GROSSO | Brasil | 5108907 | 51 | 33 | nan | nan | nan | Amazônia | 0.9 |
| 9bdc5602-0ab0-301a-b777-6af93991709e | -13.47996 | -46.9597 | 2025-08-31 04:29:00 | NPP-375D | MONTE ALEGRE DE GOIÁS | GOIÁS | Brasil | 5213509 | 52 | 33 | nan | nan | nan | Cerrado | 3.4 |
| 88516b72-66b3-3f08-a9b0-68a75927ae9c | -13.47832 | -46.97025 | 2025-08-31 04:29:00 | NPP-375D | MONTE ALEGRE DE GOIÁS | GOIÁS | Brasil | 5213509 | 52 | 33 | nan | nan | nan | Cerrado | 1.9 |
| 49c3382f-64c7-3eb7-a9d8-dfe3c833c110 | -11.41698 | -46.90845 | 2025-08-31 04:29:00 | NPP-375D | DIANÓPOLIS | TOCANTINS | Brasil | 1707009 | 17 | 33 | nan | nan | nan | Cerrado | 1.0 |
| d7c11fa3-8635-36c6-8b9a-a082c358d1de | -11.29464 | -43.57001 | 2025-08-31 04:29:00 | NPP-375D | BARRA | BAHIA | Brasil | 2902708 | 29 | 33 | nan | nan | nan | Cerrado | 2.0 |
| cb52b40c-32db-3b54-9c3c-450a7435101f | -8.96697 | -50.00697 | 2025-08-31 04:29:00 | NPP-375D | SANTA MARIA DAS BARREIRAS | PARÁ | Brasil | 1506583 | 15 | 33 | nan | nan | nan | Amazônia | 0.9 |
| 71c370e7-fe90-3683-be20-a587f75b91df | -13.98208 | -46.31519 | 2025-08-31 04:29:00 | NPP-375D | GUARANI DE GOIÁS | GOIÁS | Brasil | 5209408 | 52 | 33 | nan | nan | nan | Cerrado | 0.6 |
| e7ed3b5e-afb6-3fbe-a2c1-4466334b7baa | -13.98944 | -46.3126 | 2025-08-31 04:29:00 | NPP-375D | GUARANI DE GOIÁS | GOIÁS | Brasil | 5209408 | 52 | 33 | nan | nan | nan | Cerrado | 1.2 |
| c4fc03ba-7f86-36a3-9c15-bd4a5f2c38d6 | -12.91908 | -56.98394 | 2025-08-31 04:29:00 | NPP-375D | NOVA MARINGÁ | MATO GROSSO | Brasil | 5108907 | 51 | 33 | nan | nan | nan | Amazônia | 2.0 |
| aa1b8150-3891-3451-adfc-1b12dda564e5 | -8.96273 | -50.01237 | 2025-08-31 04:29:00 | NPP-375D | SANTA MARIA DAS BARREIRAS | PARÁ | Brasil | 1506583 | 15 | 33 | nan | nan | nan | Amazônia | 2.6 |
| 68a6e1b0-cca2-3f5c-92b4-774cb3b63650 | -11.65104 | -51.6857 | 2025-08-31 04:29:00 | NPP-375D | SÃO FÉLIX DO ARAGUAIA | MATO GROSSO | Brasil | 5107859 | 51 | 33 | nan | nan | nan | Amazônia | 1.5 |
| 22d2f26e-9a2b-3acd-b449-14ab0a4c63aa | -13.53801 | -46.96141 | 2025-08-31 04:29:00 | NPP-375D | MONTE ALEGRE DE GOIÁS | GOIÁS | Brasil | 5213509 | 52 | 33 | nan | nan | nan | Cerrado | 2.1 |
| 0592ac2c-1c4b-3770-a35e-ddce7dcc96d7 | -14.0386 | -44.56125 | 2025-08-31 04:29:00 | NPP-375D | COCOS | BAHIA | Brasil | 2908101 | 29 | 33 | nan | nan | nan | Cerrado | 4.8 |
| 508e021d-7f39-3f1c-b524-cd0484ba76dc | -13.35811 | -46.95835 | 2025-08-31 04:29:00 | NPP-375D | MONTE ALEGRE DE GOIÁS | GOIÁS | Brasil | 5213509 | 52 | 33 | nan | nan | nan | Cerrado | 2.8 |
| 9fc68090-a26d-3cbf-a37f-1ee1141ec798 | -13.67349 | -46.87226 | 2025-08-31 04:29:00 | NPP-375D | NOVA ROMA | GOIÁS | Brasil | 5214903 | 52 | 33 | nan | nan | nan | Cerrado | 1.2 |
| 9a980603-42ac-3bbd-86fb-5393d37bce4b | -11.8791 | -46.72063 | 2025-08-31 04:29:00 | NPP-375D | NOVO JARDIM | TOCANTINS | Brasil | 1715259 | 17 | 33 | nan | nan | nan | Cerrado | 1.3 |
| a6977e02-04be-3ad3-97b7-5ad221b019a1 | -13.0209 | -56.88398 | 2025-08-31 04:29:00 | NPP-375D | NOVA MARINGÁ | MATO GROSSO | Brasil | 5108907 | 51 | 33 | nan | nan | nan | Amazônia | 1.0 |
| 8fa4d267-04fe-3cf2-aaec-fdd1a4db2a70 | -11.91804 | -46.40408 | 2025-08-31 04:29:00 | NPP-375D | PONTE ALTA DO BOM JESUS | TOCANTINS | Brasil | 1717800 | 17 | 33 | nan | nan | nan | Cerrado | 2.9 |
| d49f1e6f-e3d7-3409-8863-1c31a0956d74 | -10.04063 | -46.02328 | 2025-08-31 04:29:00 | NPP-375D | ALTO PARNAÍBA | MARANHÃO | Brasil | 2100501 | 21 | 33 | nan | nan | nan | Cerrado | 1.0 |
| f779d902-dfe6-333c-89e8-8567dd532d8c | -11.21953 | -45.01954 | 2025-08-31 04:29:00 | NPP-375D | FORMOSA DO RIO PRETO | BAHIA | Brasil | 2911105 | 29 | 33 | nan | nan | nan | Cerrado | 1.3 |
| bc466437-d14f-346a-89bc-1f2e8f7dd9d4 | -11.4169 | -44.68523 | 2025-08-31 04:29:00 | NPP-375D | COTEGIPE | BAHIA | Brasil | 2909406 | 29 | 33 | nan | nan | nan | Cerrado | 0.7 |
| 327e76c6-1717-3959-9576-a0318623dc26 | -11.87521 | -46.72365 | 2025-08-31 04:29:00 | NPP-375D | NOVO JARDIM | TOCANTINS | Brasil | 1715259 | 17 | 33 | nan | nan | nan | Cerrado | 1.3 |
| 83463861-dd7a-3a94-9577-0ec018f158b3 | -11.82207 | -46.53593 | 2025-08-31 04:29:00 | NPP-375D | PONTE ALTA DO BOM JESUS | TOCANTINS | Brasil | 1717800 | 17 | 33 | nan | nan | nan | Cerrado | 1.2 |
| 5de35bb9-021d-3f95-8277-56d1666bf90b | -11.91216 | -46.71804 | 2025-08-31 04:29:00 | NPP-375D | NOVO JARDIM | TOCANTINS | Brasil | 1715259 | 17 | 33 | nan | nan | nan | Cerrado | 1.0 |
| 12b2c8cd-d9a0-39b3-8faf-ad5b45fdab61 | -11.83026 | -46.43811 | 2025-08-31 04:29:00 | NPP-375D | PONTE ALTA DO BOM JESUS | TOCANTINS | Brasil | 1717800 | 17 | 33 | nan | nan | nan | Cerrado | 4.3 |
| e2506927-6882-3e1e-a9a3-9018e5661c8f | -15.96424 | -43.90036 | 2025-08-31 04:29:00 | NPP-375D | SÃO JOÃO DA PONTE | MINAS GERAIS | Brasil | 3162401 | 31 | 33 | nan | nan | nan | Caatinga | 2.4 |
| fc1bdfc3-93ad-3943-a23e-1064e5bc73c7 | -13.021 | -56.90495 | 2025-08-31 04:29:00 | NPP-375D | NOVA MARINGÁ | MATO GROSSO | Brasil | 5108907 | 51 | 33 | nan | nan | nan | Amazônia | 1.0 |
| a1ad308a-1a1e-3e51-a93f-a942a4e3b71d | -13.98633 | -44.53765 | 2025-08-31 04:29:00 | NPP-375D | CORIBE | BAHIA | Brasil | 2909109 | 29 | 33 | nan | nan | nan | Cerrado | 1.2 |
| df51b831-01d9-3ae9-b84e-2b4f804f8d60 | -11.90653 | -46.68803 | 2025-08-31 04:29:00 | NPP-375D | NOVO JARDIM | TOCANTINS | Brasil | 1715259 | 17 | 33 | nan | nan | nan | Cerrado | 4.2 |
| 3ddb7561-5265-3c98-bc82-542fc931120e | -13.36256 | -46.95173 | 2025-08-31 04:29:00 | NPP-375D | MONTE ALEGRE DE GOIÁS | GOIÁS | Brasil | 5213509 | 52 | 33 | nan | nan | nan | Cerrado | 10.2 |
| aa4a1fcb-2d3b-3476-a388-12ae2150c1c2 | -12.80984 | -48.08668 | 2025-08-31 04:29:00 | NPP-375D | PARANÃ | TOCANTINS | Brasil | 1716208 | 17 | 33 | nan | nan | nan | Cerrado | 3.2 |
| 8ab1ad6a-458b-391a-98cd-11ab91601b3f | -10.04436 | -46.0307 | 2025-08-31 04:29:00 | NPP-375D | ALTO PARNAÍBA | MARANHÃO | Brasil | 2100501 | 21 | 33 | nan | nan | nan | Cerrado | 1.4 |
| 7aa62a01-676e-39f4-8f64-c6937c251d9e | -9.5869 | -54.47651 | 2025-08-31 04:29:00 | NPP-375D | GUARANTÃ DO NORTE | MATO GROSSO | Brasil | 5104104 | 51 | 33 | nan | nan | nan | Amazônia | 3.6 |
| 33e2d779-c821-3972-97f5-8a3a587e00f7 | -11.0197 | -46.86994 | 2025-08-31 04:29:00 | NPP-375D | PONTE ALTA DO TOCANTINS | TOCANTINS | Brasil | 1717909 | 17 | 33 | nan | nan | nan | Cerrado | 2.8 |
| eebb34b7-11cf-3066-9694-843c9460d124 | -11.82593 | -46.51091 | 2025-08-31 04:29:00 | NPP-375D | PONTE ALTA DO BOM JESUS | TOCANTINS | Brasil | 1717800 | 17 | 33 | nan | nan | nan | Cerrado | 2.6 |
| 3f6d6e4b-76c0-3192-a6ca-500c3844cc7b | -13.46998 | -46.9798 | 2025-08-31 04:29:00 | NPP-375D | MONTE ALEGRE DE GOIÁS | GOIÁS | Brasil | 5213509 | 52 | 33 | nan | nan | nan | Cerrado | 5.8 |
| 549e5726-f64d-3d6b-8d38-b6b5ba583aa4 | -13.35262 | -46.96156 | 2025-08-31 04:29:00 | NPP-375D | MONTE ALEGRE DE GOIÁS | GOIÁS | Brasil | 5213509 | 52 | 33 | nan | nan | nan | Cerrado | 2.9 |
| 9c590226-1956-3f85-ba2e-e61842d6e384 | -10.03728 | -46.02273 | 2025-08-31 04:29:00 | NPP-375D | ALTO PARNAÍBA | MARANHÃO | Brasil | 2100501 | 21 | 33 | nan | nan | nan | Cerrado | 1.0 |
| bd8c0731-2285-313c-bc37-ab0245d4da6c | -13.52909 | -46.97471 | 2025-08-31 04:29:00 | NPP-375D | MONTE ALEGRE DE GOIÁS | GOIÁS | Brasil | 5213509 | 52 | 33 | nan | nan | nan | Cerrado | 1.7 |
| 0ef36c4d-e02d-3ed5-ae60-e41c2594a422 | -14.03314 | -44.57568 | 2025-08-31 04:29:00 | NPP-375D | COCOS | BAHIA | Brasil | 2908101 | 29 | 33 | nan | nan | nan | Cerrado | 4.4 |
| 4cdb6f0f-bad3-38f7-9d3a-da99e3a28873 | -13.02028 | -56.8872 | 2025-08-31 04:29:00 | NPP-375D | NOVA MARINGÁ | MATO GROSSO | Brasil | 5108907 | 51 | 33 | nan | nan | nan | Amazônia | 1.0 |
| cbcde016-da61-3901-b90a-1f4dae4412f2 | -12.10062 | -44.72924 | 2025-08-31 04:29:00 | NPP-375D | ANGICAL | BAHIA | Brasil | 2901403 | 29 | 33 | nan | nan | nan | Cerrado | 2.6 |
| 998fabfd-49f6-3117-b43f-3f663942c5da | -11.87576 | -46.7201 | 2025-08-31 04:29:00 | NPP-375D | NOVO JARDIM | TOCANTINS | Brasil | 1715259 | 17 | 33 | nan | nan | nan | Cerrado | 1.3 |
| 2b3fb85f-5c91-38bf-962f-dde15143c626 | -13.31749 | -46.94481 | 2025-08-31 04:29:00 | NPP-375D | MONTE ALEGRE DE GOIÁS | GOIÁS | Brasil | 5213509 | 52 | 33 | nan | nan | nan | Cerrado | 1.4 |
| 9df96d46-eb34-31d2-a321-8fb3712dab70 | -11.91601 | -46.69315 | 2025-08-31 04:29:00 | NPP-375D | NOVO JARDIM | TOCANTINS | Brasil | 1715259 | 17 | 33 | nan | nan | nan | Cerrado | 2.5 |
| 3d387c82-70f3-3644-a168-82a6cb187cad | -10.24231 | -54.98008 | 2025-08-31 04:29:00 | NPP-375D | PEIXOTO DE AZEVEDO | MATO GROSSO | Brasil | 5106422 | 51 | 33 | nan | nan | nan | Amazônia | 1.4 |
| aa32bd3a-fa95-36b7-9624-5cc3a4085d3b | -9.93827 | -51.61631 | 2025-08-31 04:29:00 | NPP-375D | VILA RICA | MATO GROSSO | Brasil | 5108600 | 51 | 33 | nan | nan | nan | Amazônia | 2.2 |
| a849c110-0b1b-3cca-882a-181f87753782 | -12.41446 | -46.46664 | 2025-08-31 04:29:00 | NPP-375D | TAGUATINGA | TOCANTINS | Brasil | 1720903 | 17 | 33 | nan | nan | nan | Cerrado | 2.2 |
| 2cb6a508-e502-302d-9724-ce7cfed56fca | -8.95615 | -50.00696 | 2025-08-31 04:29:00 | NPP-375D | SANTA MARIA DAS BARREIRAS | PARÁ | Brasil | 1506583 | 15 | 33 | nan | nan | nan | Amazônia | 1.3 |
| 7bcd881f-f7f1-31c3-a94a-1a04516a17cc | -14.03311 | -44.5737 | 2025-08-31 04:29:00 | NPP-375D | COCOS | BAHIA | Brasil | 2908101 | 29 | 33 | nan | nan | nan | Cerrado | 5.6 |
| 89e9d2e3-16df-3a46-a538-80384193a89b | -13.40383 | -46.95106 | 2025-08-31 04:29:00 | NPP-375D | MONTE ALEGRE DE GOIÁS | GOIÁS | Brasil | 5213509 | 52 | 33 | nan | nan | nan | Cerrado | 0.8 |
| 69b3087f-1c85-3662-b42a-a16d55612968 | -12.31451 | -45.72847 | 2025-08-31 04:29:00 | NPP-375D | LUÍS EDUARDO MAGALHÃES | BAHIA | Brasil | 2919553 | 29 | 33 | nan | nan | nan | Cerrado | 22.9 |
| 695cef91-afb8-302e-8c0e-8c62242432a9 | -15.67757 | -43.22683 | 2025-08-31 04:29:00 | NPP-375D | PORTEIRINHA | MINAS GERAIS | Brasil | 3152204 | 31 | 33 | nan | nan | nan | Caatinga | 5.8 |
| 512c1d1f-2f99-3ba3-beab-2784582f7364 | -11.29973 | -43.6669 | 2025-08-31 04:29:00 | NPP-375D | BARRA | BAHIA | Brasil | 2902708 | 29 | 33 | nan | nan | nan | Cerrado | 1.1 |
| b505f5c7-61ac-3edd-8e18-d7063118e754 | -9.69375 | -47.04306 | 2025-08-31 04:29:00 | NPP-375D | LIZARDA | TOCANTINS | Brasil | 1712405 | 17 | 33 | nan | nan | nan | Cerrado | 1.5 |
| f58cefe8-1389-3d5e-be01-6c35f9c026d9 | -13.97472 | -46.31776 | 2025-08-31 04:29:00 | NPP-375D | GUARANI DE GOIÁS | GOIÁS | Brasil | 5209408 | 52 | 33 | nan | nan | nan | Cerrado | 1.1 |
| 4fcd3d80-f7ac-3a1f-bd27-293e64adef5f | -10.93375 | -46.83842 | 2025-08-31 04:29:00 | NPP-375D | MATEIROS | TOCANTINS | Brasil | 1712702 | 17 | 33 | nan | nan | nan | Cerrado | 0.9 |
| 9dd3d125-9106-330c-bc06-a1aa2cf624ad | -10.75547 | -59.82496 | 2025-08-31 04:29:00 | NPP-375D | ARIPUANÃ | MATO GROSSO | Brasil | 5101407 | 51 | 33 | nan | nan | nan | Amazônia | 0.7 |


[Clique aqui para ver as próximas entradas](README46.md)
