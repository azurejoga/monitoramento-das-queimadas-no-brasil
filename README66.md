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

## Dados Diários - Página 66

| ID | Latitude | Longitude | Data/Hora GMT | Satélite | Município | Estado | País | Município ID | Estado ID | País ID | Dias sem Chuva | Precipitação | Risco de Fogo | Bioma | FRP |
|----|----------|-----------|---------------|----------|-----------|--------|------|--------------|-----------|---------|----------------|--------------|----------------|-------|-----|
| 2e6bc131-ba87-3c97-9d87-38eba63d47e0 | -20.33637 | -46.5716 | 2025-08-22 12:00:00 | TERRA_M-T | SÃO ROQUE DE MINAS | MINAS GERAIS | Brasil | 3164308 | 31 | 33 | nan | nan | nan | Cerrado | 7.2 |
| 656f955a-1d66-3890-8c9c-501d3bc2bb0e | -20.7655 | -45.13148 | 2025-08-22 12:00:00 | TERRA_M-T | CANDEIAS | MINAS GERAIS | Brasil | 3112000 | 31 | 33 | nan | nan | nan | Mata Atlântica | 7.9 |
| 55e040bf-7d6f-374b-8b91-ff85f352645a | -21.36788 | -45.05405 | 2025-08-22 12:00:00 | TERRA_M-T | LAVRAS | MINAS GERAIS | Brasil | 3138203 | 31 | 33 | nan | nan | nan | Mata Atlântica | 5.7 |
| 3887c2bd-55b9-3135-889d-29e6db55a0b4 | -21.90379 | -41.59056 | 2025-08-22 12:00:00 | TERRA_M-T | CAMPOS DOS GOYTACAZES | RIO DE JANEIRO | Brasil | 3301009 | 33 | 33 | nan | nan | nan | Mata Atlântica | 6.4 |
| 2e21012b-62fc-3cd0-91b7-72a9a2efc812 | -20.08162 | -46.12328 | 2025-08-22 12:00:00 | TERRA_M-T | BAMBUÍ | MINAS GERAIS | Brasil | 3105103 | 31 | 33 | nan | nan | nan | Cerrado | 17.8 |
| 1f2cd143-e2c5-3ff4-9abc-05df461eabdb | -19.67042 | -43.8744 | 2025-08-22 12:00:00 | TERRA_M-T | LAGOA SANTA | MINAS GERAIS | Brasil | 3137601 | 31 | 33 | nan | nan | nan | Cerrado | 8.6 |
| 1b717bf7-81f2-3c5d-89ef-a862b66f99b0 | -19.32227 | -45.08282 | 2025-08-22 12:00:00 | TERRA_M-T | MARTINHO CAMPOS | MINAS GERAIS | Brasil | 3140506 | 31 | 33 | nan | nan | nan | Cerrado | 9.4 |
| 8b8a5797-ba59-373b-b880-8436811f76a7 | -20.29351 | -46.64921 | 2025-08-22 12:00:00 | TERRA_M-T | SÃO ROQUE DE MINAS | MINAS GERAIS | Brasil | 3164308 | 31 | 33 | nan | nan | nan | Cerrado | 11.5 |
| 571bb57a-fea9-368c-9859-73514ddf900d | -21.89241 | -45.4896 | 2025-08-22 12:00:00 | TERRA_M-T | SÃO GONÇALO DO SAPUCAÍ | MINAS GERAIS | Brasil | 3162005 | 31 | 33 | nan | nan | nan | Mata Atlântica | 17.0 |
| cd8b8085-c094-3fe7-97e8-0823228cb027 | -19.85081 | -46.32861 | 2025-08-22 12:00:00 | TERRA_M-T | PRATINHA | MINAS GERAIS | Brasil | 3153004 | 31 | 33 | nan | nan | nan | Cerrado | 5.4 |
| 525727b2-cf10-38ea-9376-e0dca426aacf | -20.12331 | -41.56644 | 2025-08-22 12:00:00 | TERRA_M-T | LAJINHA | MINAS GERAIS | Brasil | 3137700 | 31 | 33 | nan | nan | nan | Mata Atlântica | 14.0 |
| 77c329c5-c675-3778-b7da-28fb7139dd81 | -21.54503 | -41.22806 | 2025-08-22 12:00:00 | TERRA_M-T | SÃO FRANCISCO DE ITABAPOANA | RIO DE JANEIRO | Brasil | 3304755 | 33 | 33 | nan | nan | nan | Mata Atlântica | 7.2 |
| 2d74f5f5-07a4-35a6-81b2-1f0cd3e96c9b | -21.89087 | -45.49967 | 2025-08-22 12:00:00 | TERRA_M-T | SÃO GONÇALO DO SAPUCAÍ | MINAS GERAIS | Brasil | 3162005 | 31 | 33 | nan | nan | nan | Mata Atlântica | 15.3 |
| 0f9757d3-cf01-3485-b2c9-0ebb1b45e2d8 | -20.81459 | -40.78688 | 2025-08-22 12:00:00 | TERRA_M-T | PIÚMA | ESPÍRITO SANTO | Brasil | 3204203 | 32 | 33 | nan | nan | nan | Mata Atlântica | 10.6 |
| 668e1a66-bb6d-3038-ae05-4e42705e3eb6 | -23.30241 | -47.47458 | 2025-08-22 12:00:00 | TERRA_M-T | PORTO FELIZ | SÃO PAULO | Brasil | 3540606 | 35 | 33 | nan | nan | nan | Mata Atlântica | 11.6 |
| d6f51790-a0a1-31bd-986b-c18d4725abc3 | -18.90386 | -46.92262 | 2025-08-22 12:00:00 | TERRA_M-T | PATROCÍNIO | MINAS GERAIS | Brasil | 3148103 | 31 | 33 | nan | nan | nan | Cerrado | 8.9 |
| 081094e1-978e-34fd-81ec-b35c24c954eb | -12.9925 | -45.202 | 2025-08-22 12:10:00 | GOES-19 | SÃO DESIDÉRIO | BAHIA | Brasil | 2928901 | 29 | 33 | nan | nan | nan | Cerrado | 204.1 |
| 25e5153b-8837-3530-b641-22a00e1c239e | -14.5063 | -48.8307 | 2025-08-22 12:10:00 | GOES-19 | NIQUELÂNDIA | GOIÁS | Brasil | 5214606 | 52 | 33 | nan | nan | nan | Cerrado | 136.0 |
| 84122307-f781-3972-ba7c-b5a762b667f8 | -12.9921 | -45.2252 | 2025-08-22 12:10:00 | GOES-19 | SÃO DESIDÉRIO | BAHIA | Brasil | 2928901 | 29 | 33 | nan | nan | nan | Cerrado | 216.7 |
| 3908f180-ecdd-3508-ba07-3351f200e7c5 | -12.3129 | -50.0097 | 2025-08-22 12:10:00 | GOES-19 | SANDOLÂNDIA | TOCANTINS | Brasil | 1718840 | 17 | 33 | nan | nan | nan | Cerrado | 93.3 |
| c8275625-c418-3e71-8727-4e5f401b7957 | -6.436 | -44.5306 | 2025-08-22 12:20:00 | GOES-19 | MIRADOR | MARANHÃO | Brasil | 2106706 | 21 | 33 | nan | nan | nan | Cerrado | 92.0 |
| 24e1a48d-3977-3e7a-9faa-9223524bec47 | -7.6296 | -45.2464 | 2025-08-22 12:20:00 | GOES-19 | RIBEIRO GONÇALVES | PIAUÍ | Brasil | 2208908 | 22 | 33 | nan | nan | nan | Cerrado | 69.2 |
| fa70dd06-b75b-3884-9e74-6a6daa378c6b | -9.6 | -55.3498 | 2025-08-22 12:20:00 | GOES-19 | NOVO MUNDO | MATO GROSSO | Brasil | 5106265 | 51 | 33 | nan | nan | nan | Amazônia | 99.0 |
| 87baeece-f3c8-3a08-bace-30d3d1ee8fb9 | -12.3129 | -50.0097 | 2025-08-22 12:20:00 | GOES-19 | SANDOLÂNDIA | TOCANTINS | Brasil | 1718840 | 17 | 33 | nan | nan | nan | Cerrado | 90.8 |
| fba16170-52d0-38e4-ab9a-99ce41e88406 | -13.0114 | -45.222 | 2025-08-22 12:20:00 | GOES-19 | SÃO DESIDÉRIO | BAHIA | Brasil | 2928901 | 29 | 33 | nan | nan | nan | Cerrado | 78.1 |
| a86899ec-1536-3faa-9d7f-3d629ef355ad | -6.4547 | -44.529 | 2025-08-22 12:20:00 | GOES-19 | MIRADOR | MARANHÃO | Brasil | 2106706 | 21 | 33 | nan | nan | nan | Cerrado | 77.5 |
| 27ff34e0-3c09-363a-b378-7fb0061485f3 | -14.6523 | -54.8543 | 2025-08-22 12:20:00 | GOES-19 | PLANALTO DA SERRA | MATO GROSSO | Brasil | 5106455 | 51 | 33 | nan | nan | nan | Cerrado | 91.3 |
| fa5df1d4-ed74-3125-9889-73cfccf1d7b6 | -12.9925 | -45.202 | 2025-08-22 12:20:00 | GOES-19 | SÃO DESIDÉRIO | BAHIA | Brasil | 2928901 | 29 | 33 | nan | nan | nan | Cerrado | 193.7 |
| 70494862-e76d-35c3-b4c9-ddbcdf03c476 | -12.9921 | -45.2252 | 2025-08-22 12:20:00 | GOES-19 | SÃO DESIDÉRIO | BAHIA | Brasil | 2928901 | 29 | 33 | nan | nan | nan | Cerrado | 246.0 |
| d1c79391-ee39-3e22-877a-b20c5ada2ec5 | -7.6559 | -46.2358 | 2025-08-22 12:20:00 | GOES-19 | BALSAS | MARANHÃO | Brasil | 2101400 | 21 | 33 | nan | nan | nan | Cerrado | 98.0 |
| 57628aeb-1c56-3957-b842-01c882316a9f | -14.6519 | -54.875 | 2025-08-22 12:20:00 | GOES-19 | PLANALTO DA SERRA | MATO GROSSO | Brasil | 5106455 | 51 | 33 | nan | nan | nan | Cerrado | 79.4 |
| 4345d9a5-43c2-3377-89e2-355318171ced | -7.6557 | -46.2582 | 2025-08-22 12:30:00 | GOES-19 | BALSAS | MARANHÃO | Brasil | 2101400 | 21 | 33 | nan | nan | nan | Cerrado | 63.8 |
| 3bc7b8c4-015c-3ae8-bc3b-a92610a0d1ab | -6.436 | -44.5306 | 2025-08-22 12:30:00 | GOES-19 | MIRADOR | MARANHÃO | Brasil | 2106706 | 21 | 33 | nan | nan | nan | Cerrado | 126.9 |
| b80c8e76-52b5-36df-847c-dc6c8915b0f1 | -7.6296 | -45.2464 | 2025-08-22 12:30:00 | GOES-19 | RIBEIRO GONÇALVES | PIAUÍ | Brasil | 2208908 | 22 | 33 | nan | nan | nan | Cerrado | 71.7 |
| 4d81c6e9-6ad8-3e32-b569-71e8cd70004e | -14.6519 | -54.875 | 2025-08-22 12:30:00 | GOES-19 | PLANALTO DA SERRA | MATO GROSSO | Brasil | 5106455 | 51 | 33 | nan | nan | nan | Cerrado | 121.0 |
| 63290b69-9d7b-3aec-aa2a-ac6f561c5c57 | -12.9921 | -45.2252 | 2025-08-22 12:30:00 | GOES-19 | SÃO DESIDÉRIO | BAHIA | Brasil | 2928901 | 29 | 33 | nan | nan | nan | Cerrado | 211.8 |
| 4357be8a-4547-31a0-ab11-dc8a0062587c | -7.6559 | -46.2358 | 2025-08-22 12:30:00 | GOES-19 | BALSAS | MARANHÃO | Brasil | 2101400 | 21 | 33 | nan | nan | nan | Cerrado | 112.5 |
| dc9fbfa2-c0b2-3e99-b600-6ad116240f19 | -12.3129 | -50.0097 | 2025-08-22 12:30:00 | GOES-19 | SANDOLÂNDIA | TOCANTINS | Brasil | 1718840 | 17 | 33 | nan | nan | nan | Cerrado | 117.9 |
| 7db6c6c0-d639-3566-a6e8-ca6dd06ba015 | -8.4779 | -48.236 | 2025-08-22 12:30:00 | GOES-19 | TUPIRATINS | TOCANTINS | Brasil | 1721307 | 17 | 33 | nan | nan | nan | Cerrado | 94.1 |
| 8e425e34-8c28-36f7-b516-152f7c04caf8 | -14.6716 | -54.8521 | 2025-08-22 12:30:00 | GOES-19 | PLANALTO DA SERRA | MATO GROSSO | Brasil | 5106455 | 51 | 33 | nan | nan | nan | Cerrado | 72.0 |
| d1513a55-4ca6-3610-8b80-53df25268af1 | -8.4776 | -48.2578 | 2025-08-22 12:30:00 | GOES-19 | TUPIRATINS | TOCANTINS | Brasil | 1721307 | 17 | 33 | nan | nan | nan | Cerrado | 106.1 |
| 5fb6997b-ef88-301c-abb5-c5cd77d10515 | -9.6 | -55.3498 | 2025-08-22 12:30:00 | GOES-19 | NOVO MUNDO | MATO GROSSO | Brasil | 5106265 | 51 | 33 | nan | nan | nan | Amazônia | 113.6 |
| 61d443e2-2750-3bae-b15f-5e38ace9bd5f | -12.9925 | -45.202 | 2025-08-22 12:30:00 | GOES-19 | SÃO DESIDÉRIO | BAHIA | Brasil | 2928901 | 29 | 33 | nan | nan | nan | Cerrado | 158.6 |
| fc4476af-180c-3b10-857b-8b9911f82719 | -14.8348 | -47.9311 | 2025-08-22 12:30:00 | GOES-19 | ÁGUA FRIA DE GOIÁS | GOIÁS | Brasil | 5200175 | 52 | 33 | nan | nan | nan | Cerrado | 78.3 |
| 68821b83-afdc-3516-b406-daf3142c5436 | -14.5063 | -48.8307 | 2025-08-22 12:30:00 | GOES-19 | NIQUELÂNDIA | GOIÁS | Brasil | 5214606 | 52 | 33 | nan | nan | nan | Cerrado | 110.7 |
| 1cf52e02-1d06-3f1f-afde-819fd8fe80a1 | -14.6713 | -54.8728 | 2025-08-22 12:30:00 | GOES-19 | PLANALTO DA SERRA | MATO GROSSO | Brasil | 5106455 | 51 | 33 | nan | nan | nan | Cerrado | 79.2 |
| c9f3c33d-c295-32ba-aa03-206858d05253 | -6.4362 | -44.5076 | 2025-08-22 12:30:00 | GOES-19 | MIRADOR | MARANHÃO | Brasil | 2106706 | 21 | 33 | nan | nan | nan | Cerrado | 71.0 |
| ecca17cd-8fbe-3f3b-a650-c5491ccfc34c | -13.0114 | -45.222 | 2025-08-22 12:30:00 | GOES-19 | SÃO DESIDÉRIO | BAHIA | Brasil | 2928901 | 29 | 33 | nan | nan | nan | Cerrado | 84.8 |
| 7c0cf8fc-38ca-3d2d-a835-cf47f1492185 | -14.6523 | -54.8543 | 2025-08-22 12:30:00 | GOES-19 | PLANALTO DA SERRA | MATO GROSSO | Brasil | 5106455 | 51 | 33 | nan | nan | nan | Cerrado | 103.2 |
| a1aca3aa-c81e-38b6-a2e6-b74cf53edbf8 | -14.6716 | -54.8521 | 2025-08-22 12:40:00 | GOES-19 | PLANALTO DA SERRA | MATO GROSSO | Brasil | 5106455 | 51 | 33 | nan | nan | nan | Cerrado | 77.7 |
| 3051b881-2847-3bf9-b676-71ee83464189 | -12.9921 | -45.2252 | 2025-08-22 12:40:00 | GOES-19 | SÃO DESIDÉRIO | BAHIA | Brasil | 2928901 | 29 | 33 | nan | nan | nan | Cerrado | 202.7 |
| 82527051-1cfb-3494-b8cc-7adaf0084bcb | -6.3123 | -43.7572 | 2025-08-22 12:40:00 | GOES-19 | SÃO JOÃO DOS PATOS | MARANHÃO | Brasil | 2111102 | 21 | 33 | nan | nan | nan | Cerrado | 73.7 |
| 089351f9-98d4-37b6-ac38-b4786c561e0e | -14.8348 | -47.9311 | 2025-08-22 12:40:00 | GOES-19 | ÁGUA FRIA DE GOIÁS | GOIÁS | Brasil | 5200175 | 52 | 33 | nan | nan | nan | Cerrado | 110.9 |
| 50093273-16b7-366b-ad65-89167eb27f1c | -14.7717 | -45.4055 | 2025-08-22 12:40:00 | GOES-19 | COCOS | BAHIA | Brasil | 2908101 | 29 | 33 | nan | nan | nan | Cerrado | 91.4 |
| 5cc88aba-67bd-3a9d-8569-f4ce2f868c25 | -14.6713 | -54.8728 | 2025-08-22 12:40:00 | GOES-19 | PLANALTO DA SERRA | MATO GROSSO | Brasil | 5106455 | 51 | 33 | nan | nan | nan | Cerrado | 107.8 |
| 89b29e18-c055-3200-b436-b7b5e5528825 | -7.6559 | -46.2358 | 2025-08-22 12:40:00 | GOES-19 | BALSAS | MARANHÃO | Brasil | 2101400 | 21 | 33 | nan | nan | nan | Cerrado | 93.1 |
| 7b3f38f9-fbc7-36d8-bf56-b2bbe6c2c262 | -6.436 | -44.5306 | 2025-08-22 12:40:00 | GOES-19 | MIRADOR | MARANHÃO | Brasil | 2106706 | 21 | 33 | nan | nan | nan | Cerrado | 122.9 |
| d54a8237-573e-3b1f-bae0-6ef3204a21df | -14.6519 | -54.875 | 2025-08-22 12:40:00 | GOES-19 | PLANALTO DA SERRA | MATO GROSSO | Brasil | 5106455 | 51 | 33 | nan | nan | nan | Cerrado | 130.1 |
| e584dc54-4c75-3f02-88e4-6babd4693917 | -9.6 | -55.3498 | 2025-08-22 12:40:00 | GOES-19 | NOVO MUNDO | MATO GROSSO | Brasil | 5106265 | 51 | 33 | nan | nan | nan | Amazônia | 81.1 |
| 9ab9d694-997f-3555-9902-d6c10ec7bbc3 | -12.3129 | -50.0097 | 2025-08-22 12:40:00 | GOES-19 | SANDOLÂNDIA | TOCANTINS | Brasil | 1718840 | 17 | 33 | nan | nan | nan | Cerrado | 117.5 |
| 7803a826-fbea-3f0c-8299-50a7c371b0ba | -7.0352 | -44.6396 | 2025-08-22 12:40:00 | GOES-19 | BENEDITO LEITE | MARANHÃO | Brasil | 2101806 | 21 | 33 | nan | nan | nan | Cerrado | 78.8 |
| d82e5f54-ae6f-3d8e-8d3d-5b6543d1fee7 | -13.0119 | -45.1988 | 2025-08-22 12:40:00 | GOES-19 | SÃO DESIDÉRIO | BAHIA | Brasil | 2928901 | 29 | 33 | nan | nan | nan | Cerrado | 73.9 |
| 8bde4a92-098e-30d3-8c89-75a3d6c5e91d | -6.4362 | -44.5076 | 2025-08-22 12:40:00 | GOES-19 | MIRADOR | MARANHÃO | Brasil | 2106706 | 21 | 33 | nan | nan | nan | Cerrado | 83.2 |
| 5b98d8eb-c78f-35f4-8f6a-937ca4902c17 | -14.6523 | -54.8543 | 2025-08-22 12:40:00 | GOES-19 | PLANALTO DA SERRA | MATO GROSSO | Brasil | 5106455 | 51 | 33 | nan | nan | nan | Cerrado | 86.1 |
| 6a4a9b65-c207-3887-9a83-01ad73208478 | -13.0114 | -45.222 | 2025-08-22 12:40:00 | GOES-19 | SÃO DESIDÉRIO | BAHIA | Brasil | 2928901 | 29 | 33 | nan | nan | nan | Cerrado | 91.2 |
| 52a59f25-457b-3a8e-bb56-307a99cded32 | -12.9925 | -45.202 | 2025-08-22 12:40:00 | GOES-19 | SÃO DESIDÉRIO | BAHIA | Brasil | 2928901 | 29 | 33 | nan | nan | nan | Cerrado | 181.6 |
| 7e7f465d-d935-3e91-ae30-b8141c9bde2a | -14.5063 | -48.8307 | 2025-08-22 12:40:00 | GOES-19 | NIQUELÂNDIA | GOIÁS | Brasil | 5214606 | 52 | 33 | nan | nan | nan | Cerrado | 96.5 |
| df986a42-afdf-31b8-802f-a11c3f9ae027 | -6.3311 | -43.7557 | 2025-08-22 12:40:00 | GOES-19 | SÃO JOÃO DOS PATOS | MARANHÃO | Brasil | 2111102 | 21 | 33 | nan | nan | nan | Cerrado | 88.7 |
| 16293f09-1784-3fd5-8ca9-d88ae7598405 | -7.9436 | -42.6631 | 2025-08-22 12:40:00 | GOES-19 | RIBEIRA DO PIAUÍ | PIAUÍ | Brasil | 2208874 | 22 | 33 | nan | nan | nan | Caatinga | 81.1 |
| 18bdfa5f-b3ba-3066-bcf6-8f886c4446c7 | -10.876 | -50.8163 | 2025-08-22 12:50:00 | GOES-19 | LUCIARA | MATO GROSSO | Brasil | 5105309 | 51 | 33 | nan | nan | nan | Cerrado | 83.6 |
| a88618f1-0d98-3bb4-9183-42ea732ec8d4 | -8.7951 | -45.4238 | 2025-08-22 12:50:00 | GOES-19 | SANTA FILOMENA | PIAUÍ | Brasil | 2209203 | 22 | 33 | nan | nan | nan | Cerrado | 86.1 |
| 935452d2-8051-38f2-842d-72be2faf383f | -6.3123 | -43.7572 | 2025-08-22 12:50:00 | GOES-19 | SÃO JOÃO DOS PATOS | MARANHÃO | Brasil | 2111102 | 21 | 33 | nan | nan | nan | Cerrado | 83.7 |
| 182a4514-391d-3037-8c3e-4aa29d273eff | -7.6559 | -46.2358 | 2025-08-22 12:50:00 | GOES-19 | BALSAS | MARANHÃO | Brasil | 2101400 | 21 | 33 | nan | nan | nan | Cerrado | 113.5 |
| e94c1011-fe07-367e-b39b-493e5392040b | -7.1017 | -43.7108 | 2025-08-22 12:50:00 | GOES-19 | JERUMENHA | PIAUÍ | Brasil | 2205300 | 22 | 33 | nan | nan | nan | Cerrado | 69.3 |
| df4d5736-2f28-315c-9fd9-7389e33fc6ff | -7.0352 | -44.6396 | 2025-08-22 12:50:00 | GOES-19 | BENEDITO LEITE | MARANHÃO | Brasil | 2101806 | 21 | 33 | nan | nan | nan | Cerrado | 84.4 |
| 2a2a46e2-2d9a-39b6-aff3-f8536bd5cd6e | -7.6484 | -45.2446 | 2025-08-22 12:50:00 | GOES-19 | RIBEIRO GONÇALVES | PIAUÍ | Brasil | 2208908 | 22 | 33 | nan | nan | nan | Cerrado | 77.0 |
| 3af96a9a-3cb0-3416-b2da-dce745f64a13 | -12.656 | -47.7947 | 2025-08-22 12:50:00 | GOES-19 | PARANÃ | TOCANTINS | Brasil | 1716208 | 17 | 33 | nan | nan | nan | Cerrado | 75.4 |
| 062939fe-291e-3257-bcae-aa69d703c54f | -12.9921 | -45.2252 | 2025-08-22 12:50:00 | GOES-19 | SÃO DESIDÉRIO | BAHIA | Brasil | 2928901 | 29 | 33 | nan | nan | nan | Cerrado | 172.7 |
| b84cb78b-696c-38d1-880d-0abcda1098cb | -13.1456 | -40.6567 | 2025-08-22 12:50:00 | GOES-19 | MARCIONÍLIO SOUZA | BAHIA | Brasil | 2920809 | 29 | 33 | nan | nan | nan | Caatinga | 126.4 |
| da43049f-a255-3f6a-928d-86315ec58c76 | -20.0828 | -46.1262 | 2025-08-22 12:50:00 | GOES-19 | BAMBUÍ | MINAS GERAIS | Brasil | 3105103 | 31 | 33 | nan | nan | nan | Cerrado | 117.7 |
| ae69f57d-77e6-3429-9c03-35c4309a6ab7 | -12.3129 | -50.0097 | 2025-08-22 12:50:00 | GOES-19 | SANDOLÂNDIA | TOCANTINS | Brasil | 1718840 | 17 | 33 | nan | nan | nan | Cerrado | 101.5 |
| f06172f3-b2c1-3cec-9a8e-1967898ff50b | -14.6713 | -54.8728 | 2025-08-22 12:50:00 | GOES-19 | PLANALTO DA SERRA | MATO GROSSO | Brasil | 5106455 | 51 | 33 | nan | nan | nan | Cerrado | 70.4 |
| 8e870579-864e-3a88-8fe7-673055a9cc6b | -13.0114 | -45.222 | 2025-08-22 12:50:00 | GOES-19 | SÃO DESIDÉRIO | BAHIA | Brasil | 2928901 | 29 | 33 | nan | nan | nan | Cerrado | 91.1 |
| b6dab5f1-6aa6-311a-b07b-999c605b3d84 | -12.9925 | -45.202 | 2025-08-22 12:50:00 | GOES-19 | SÃO DESIDÉRIO | BAHIA | Brasil | 2928901 | 29 | 33 | nan | nan | nan | Cerrado | 172.0 |
| 409c00a7-c42c-3609-83ce-c39c113cfd78 | -7.9436 | -42.6631 | 2025-08-22 12:50:00 | GOES-19 | RIBEIRA DO PIAUÍ | PIAUÍ | Brasil | 2208874 | 22 | 33 | nan | nan | nan | Caatinga | 78.9 |
| dc51f0e6-7890-3eca-9433-a60cd367a495 | -12.3133 | -49.9881 | 2025-08-22 12:50:00 | GOES-19 | SANDOLÂNDIA | TOCANTINS | Brasil | 1718840 | 17 | 33 | nan | nan | nan | Cerrado | 210.5 |
| 3bcac143-8694-388f-b9c5-23415efd9595 | -13.3966 | -46.2406 | 2025-08-22 12:50:00 | GOES-19 | SÃO DOMINGOS | GOIÁS | Brasil | 5219803 | 52 | 33 | nan | nan | nan | Cerrado | 95.0 |
| b0f8c085-fc7f-3007-a121-08983b37c195 | -7.0354 | -44.6167 | 2025-08-22 12:50:00 | GOES-19 | BENEDITO LEITE | MARANHÃO | Brasil | 2101806 | 21 | 33 | nan | nan | nan | Cerrado | 73.0 |
| a8803d7a-4fee-3b4c-a5ac-c594958898ac | -6.4362 | -44.5076 | 2025-08-22 12:50:00 | GOES-19 | MIRADOR | MARANHÃO | Brasil | 2106706 | 21 | 33 | nan | nan | nan | Cerrado | 71.0 |
| eb49f82a-2631-3a6b-883a-cca328254c84 | -14.7717 | -45.4055 | 2025-08-22 12:50:00 | GOES-19 | COCOS | BAHIA | Brasil | 2908101 | 29 | 33 | nan | nan | nan | Cerrado | 94.1 |
| 4fbcd3ee-a6a9-3089-941b-c943765302f6 | -8.7759 | -45.4486 | 2025-08-22 12:50:00 | GOES-19 | SANTA FILOMENA | PIAUÍ | Brasil | 2209203 | 22 | 33 | nan | nan | nan | Cerrado | 69.4 |
| 458e8775-5da1-397a-82bf-4297972e7778 | -7.6557 | -46.2582 | 2025-08-22 12:50:00 | GOES-19 | BALSAS | MARANHÃO | Brasil | 2101400 | 21 | 33 | nan | nan | nan | Cerrado | 70.0 |
| b6c5a74f-9736-3845-aa16-5b9a2ffbf0f1 | -12.2938 | -50.0121 | 2025-08-22 12:50:00 | GOES-19 | SANDOLÂNDIA | TOCANTINS | Brasil | 1718840 | 17 | 33 | nan | nan | nan | Cerrado | 92.3 |
| 3f0cff89-7d00-3add-8067-db616e19e3c4 | -14.6519 | -54.875 | 2025-08-22 12:50:00 | GOES-19 | PLANALTO DA SERRA | MATO GROSSO | Brasil | 5106455 | 51 | 33 | nan | nan | nan | Cerrado | 135.3 |
| 1d874254-36fa-3016-9fa8-3803104b290d | -6.436 | -44.5306 | 2025-08-22 12:50:00 | GOES-19 | MIRADOR | MARANHÃO | Brasil | 2106706 | 21 | 33 | nan | nan | nan | Cerrado | 133.8 |
| 4769377a-65e6-3c02-b7b0-905f38bea91f | -13.0119 | -45.1988 | 2025-08-22 12:50:00 | GOES-19 | SÃO DESIDÉRIO | BAHIA | Brasil | 2928901 | 29 | 33 | nan | nan | nan | Cerrado | 78.2 |
| deb7db98-df4b-3872-a38d-f8070e1f9f0e | -14.8348 | -47.9311 | 2025-08-22 12:50:00 | GOES-19 | ÁGUA FRIA DE GOIÁS | GOIÁS | Brasil | 5200175 | 52 | 33 | nan | nan | nan | Cerrado | 94.4 |
| a5508128-6f5d-31bc-9c59-567127ba48a9 | -14.6523 | -54.8543 | 2025-08-22 12:50:00 | GOES-19 | PLANALTO DA SERRA | MATO GROSSO | Brasil | 5106455 | 51 | 33 | nan | nan | nan | Cerrado | 90.8 |
| 54202b9d-605a-3555-b8ef-9ed0ad8c2368 | -8.7567 | -45.4733 | 2025-08-22 13:00:00 | GOES-19 | SANTA FILOMENA | PIAUÍ | Brasil | 2209203 | 22 | 33 | nan | nan | nan | Cerrado | 65.5 |
| 8b09c5df-2f31-3a81-bf6f-280aad605889 | -14.8348 | -47.9311 | 2025-08-22 13:00:00 | GOES-19 | ÁGUA FRIA DE GOIÁS | GOIÁS | Brasil | 5200175 | 52 | 33 | nan | nan | nan | Cerrado | 122.6 |


[Clique aqui para ver as próximas entradas](README67.md)
