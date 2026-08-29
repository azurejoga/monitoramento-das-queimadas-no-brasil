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

## Dados Diários - Página 6

| ID | Latitude | Longitude | Data/Hora GMT | Satélite | Município | Estado | País | Município ID | Estado ID | País ID | Dias sem Chuva | Precipitação | Risco de Fogo | Bioma | FRP |
|----|----------|-----------|---------------|----------|-----------|--------|------|--------------|-----------|---------|----------------|--------------|----------------|-------|-----|
| c177f33b-05c5-37bf-b96b-90a238ebd324 | -5.8894 | -57.7708 | 2026-08-29 00:10:00 | GOES-19 | JACAREACANGA | PARÁ | Brasil | 1503754 | 15 | 33 | nan | nan | nan | Amazônia | 171.5 |
| 94fda530-32fe-35c0-8461-7dc2333dfee9 | -7.5139 | -55.2851 | 2026-08-29 00:10:00 | GOES-19 | NOVO PROGRESSO | PARÁ | Brasil | 1505031 | 15 | 33 | nan | nan | nan | Amazônia | 73.9 |
| 4ed678d8-6df4-3335-b06a-f00dfffdcb21 | -7.5845 | -61.3423 | 2026-08-29 00:10:00 | GOES-19 | MANICORÉ | AMAZONAS | Brasil | 1302702 | 13 | 33 | nan | nan | nan | Amazônia | 57.1 |
| 5aeece9e-41c2-3d62-81be-c1c6fffc7c6a | -10.9187 | -46.6192 | 2026-08-29 00:10:00 | GOES-19 | MATEIROS | TOCANTINS | Brasil | 1712702 | 17 | 33 | nan | nan | nan | Cerrado | 68.9 |
| c30d71b5-c7d3-3284-9437-b0d7de7bbaf8 | -10.919 | -46.5967 | 2026-08-29 00:10:00 | GOES-19 | MATEIROS | TOCANTINS | Brasil | 1712702 | 17 | 33 | nan | nan | nan | Cerrado | 44.8 |
| d76a7a96-ec3e-3e05-af5e-cd6973558deb | -9.9288 | -60.4277 | 2026-08-29 00:10:00 | GOES-19 | ARIPUANÃ | MATO GROSSO | Brasil | 5101407 | 51 | 33 | nan | nan | nan | Amazônia | 49.5 |
| b8f217fa-f220-386f-86b4-d0a036ce6183 | -5.8895 | -57.7513 | 2026-08-29 00:10:00 | GOES-19 | JACAREACANGA | PARÁ | Brasil | 1503754 | 15 | 33 | nan | nan | nan | Amazônia | 252.1 |
| 90c81ccb-0bb8-3d05-835f-6cb5069476fc | -6.7699 | -55.6644 | 2026-08-29 00:10:00 | GOES-19 | NOVO PROGRESSO | PARÁ | Brasil | 1505031 | 15 | 33 | nan | nan | nan | Amazônia | 233.5 |
| b33f619e-377b-30d1-acb0-207cf56f8bce | -6.7343 | -55.4671 | 2026-08-29 00:10:00 | GOES-19 | NOVO PROGRESSO | PARÁ | Brasil | 1505031 | 15 | 33 | nan | nan | nan | Amazônia | 150.9 |
| e2e7a059-b7a1-35bc-a1e6-ad3f43542c65 | -6.7884 | -55.6635 | 2026-08-29 00:10:00 | GOES-19 | NOVO PROGRESSO | PARÁ | Brasil | 1505031 | 15 | 33 | nan | nan | nan | Amazônia | 58.9 |
| 67d8bec1-6380-3642-984a-b5fd653836ae | -5.9078 | -57.77 | 2026-08-29 00:10:00 | GOES-19 | JACAREACANGA | PARÁ | Brasil | 1503754 | 15 | 33 | nan | nan | nan | Amazônia | 47.5 |
| 4cc34a55-7c89-3ff6-aed5-d8246eb7969c | -8.5359 | -55.3428 | 2026-08-29 00:10:00 | GOES-19 | NOVO PROGRESSO | PARÁ | Brasil | 1505031 | 15 | 33 | nan | nan | nan | Amazônia | 76.8 |
| 38653995-59f4-3243-94b7-f431a57ec380 | -6.7698 | -55.6844 | 2026-08-29 00:10:00 | GOES-19 | NOVO PROGRESSO | PARÁ | Brasil | 1505031 | 15 | 33 | nan | nan | nan | Amazônia | 107.8 |
| 8e2cdccd-25b8-3406-a024-f5a291e050d1 | -11.0441 | -57.2421 | 2026-08-29 00:10:00 | GOES-19 | JUARA | MATO GROSSO | Brasil | 5105101 | 51 | 33 | nan | nan | nan | Amazônia | 76.1 |
| 21154937-d894-3ea8-a307-d9734183f774 | 2.4154 | -60.8888 | 2026-08-29 00:10:00 | GOES-19 | MUCAJAÍ | RORAIMA | Brasil | 1400308 | 14 | 33 | nan | nan | nan | Amazônia | 59.4 |
| a1a1809e-21c5-32cb-b369-d5473c4c9f33 | -20.941 | -57.5694 | 2026-08-29 00:10:00 | GOES-19 | PORTO MURTINHO | MATO GROSSO DO SUL | Brasil | 5006903 | 50 | 33 | nan | nan | nan | Pantanal | 108.0 |
| d409224e-aa86-3574-95e6-cb58bd1cc042 | -6.7514 | -55.6654 | 2026-08-29 00:10:00 | GOES-19 | NOVO PROGRESSO | PARÁ | Brasil | 1505031 | 15 | 33 | nan | nan | nan | Amazônia | 79.6 |
| 88d49290-46d9-3c3f-929f-fde630addfee | -5.9819 | -57.6892 | 2026-08-29 00:10:00 | GOES-19 | JACAREACANGA | PARÁ | Brasil | 1503754 | 15 | 33 | nan | nan | nan | Amazônia | 51.8 |
| 89d28de1-2446-36bb-a035-7325ed5d6874 | -7.5137 | -55.3051 | 2026-08-29 00:10:00 | GOES-19 | NOVO PROGRESSO | PARÁ | Brasil | 1505031 | 15 | 33 | nan | nan | nan | Amazônia | 85.0 |
| 42e89fd4-a914-3106-ad20-d8797dfc3994 | 2.4155 | -60.8699 | 2026-08-29 00:10:00 | GOES-19 | MUCAJAÍ | RORAIMA | Brasil | 1400308 | 14 | 33 | nan | nan | nan | Amazônia | 59.8 |
| d76be9c1-9e1a-348f-a07f-5a2e31ee8749 | 4.5366 | -60.72963 | 2026-08-29 00:11:00 | TERRA_M-M | PACARAIMA | RORAIMA | Brasil | 1400456 | 14 | 33 | nan | nan | nan | Amazônia | 17.8 |
| f502448a-f4e3-3609-9907-2b962cbfb753 | 4.54012 | -60.73537 | 2026-08-29 00:11:00 | TERRA_M-M | PACARAIMA | RORAIMA | Brasil | 1400456 | 14 | 33 | nan | nan | nan | Amazônia | 21.9 |
| 72258204-e406-3686-ba91-606e033e8042 | -6.61 | -43.79 | 2026-08-29 00:15:00 | MSG-03 | NOVA IORQUE | MARANHÃO | Brasil | 2107308 | 21 | 33 | nan | nan | nan | Cerrado | nan |
| e02b0392-6915-3b8b-85d2-8085a4f26ad9 | -6.64 | -43.75 | 2026-08-29 00:15:00 | MSG-03 | SÃO JOÃO DOS PATOS | MARANHÃO | Brasil | 2111102 | 21 | 33 | nan | nan | nan | Cerrado | nan |
| 4652a424-310f-3ac3-a8bb-400e8b65cef2 | -6.61 | -43.74 | 2026-08-29 00:15:00 | MSG-03 | SÃO JOÃO DOS PATOS | MARANHÃO | Brasil | 2111102 | 21 | 33 | nan | nan | nan | Cerrado | nan |
| cd183df2-edd5-347d-8be2-8d48452adfdf | -6.64 | -43.79 | 2026-08-29 00:15:00 | MSG-03 | NOVA IORQUE | MARANHÃO | Brasil | 2107308 | 21 | 33 | nan | nan | nan | Cerrado | nan |
| 55652a90-02e0-3f13-a7d8-a27d336c8f90 | -6.74 | -55.48 | 2026-08-29 00:15:00 | MSG-03 | NOVO PROGRESSO | PARÁ | Brasil | 1505031 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| 63e4dd3b-91be-3c7d-a01b-951a474b3c7b | -6.7528 | -55.4661 | 2026-08-29 00:20:00 | GOES-19 | NOVO PROGRESSO | PARÁ | Brasil | 1505031 | 15 | 33 | nan | nan | nan | Amazônia | 51.7 |
| 3d99b36e-b0a7-3f76-9b26-f786ac0a3214 | -10.919 | -46.5967 | 2026-08-29 00:20:00 | GOES-19 | MATEIROS | TOCANTINS | Brasil | 1712702 | 17 | 33 | nan | nan | nan | Cerrado | 40.2 |
| 509b175f-889d-3a0a-a900-b1bdaf302077 | -7.5845 | -61.3423 | 2026-08-29 00:20:00 | GOES-19 | MANICORÉ | AMAZONAS | Brasil | 1302702 | 13 | 33 | nan | nan | nan | Amazônia | 51.6 |
| 1dff469e-fd9e-3d11-8151-b390a6872d18 | -11.0256 | -57.2038 | 2026-08-29 00:20:00 | GOES-19 | JUARA | MATO GROSSO | Brasil | 5105101 | 51 | 33 | nan | nan | nan | Amazônia | 51.5 |
| ffae90c4-a15b-3b2a-a8c6-5fab3c40ee71 | -6.7514 | -55.6654 | 2026-08-29 00:20:00 | GOES-19 | NOVO PROGRESSO | PARÁ | Brasil | 1505031 | 15 | 33 | nan | nan | nan | Amazônia | 67.2 |
| f0fb5319-5610-3873-9f34-45c65b170d0f | -20.9606 | -57.6086 | 2026-08-29 00:20:00 | GOES-19 | PORTO MURTINHO | MATO GROSSO DO SUL | Brasil | 5006903 | 50 | 33 | nan | nan | nan | Pantanal | 80.2 |
| ad031013-1d8b-3ad8-9df9-3b14f2e233c3 | 0.1367 | -60.393 | 2026-08-29 00:20:00 | GOES-19 | RORAINÓPOLIS | RORAIMA | Brasil | 1400472 | 14 | 33 | nan | nan | nan | Amazônia | 55.0 |
| 60b8e277-824f-3133-9709-7ac925eda285 | 2.4154 | -60.8888 | 2026-08-29 00:20:00 | GOES-19 | MUCAJAÍ | RORAIMA | Brasil | 1400308 | 14 | 33 | nan | nan | nan | Amazônia | 56.7 |
| 46f5a0d2-db5b-3859-a35a-18d7a1904204 | -12.43 | -43.4182 | 2026-08-29 00:20:00 | GOES-19 | MUQUÉM DO SÃO FRANCISCO | BAHIA | Brasil | 2922250 | 29 | 33 | nan | nan | nan | Cerrado | 80.3 |
| 1c293fc8-989f-3c0e-9683-97bb1df54abc | -10.9377 | -46.6168 | 2026-08-29 00:20:00 | GOES-19 | MATEIROS | TOCANTINS | Brasil | 1712702 | 17 | 33 | nan | nan | nan | Cerrado | 46.9 |
| 005945fa-4f6f-3efd-9431-9ee1f5a1b5d5 | -6.6315 | -43.7533 | 2026-08-29 00:20:00 | GOES-19 | SÃO JOÃO DOS PATOS | MARANHÃO | Brasil | 2111102 | 21 | 33 | nan | nan | nan | Cerrado | 112.4 |
| 753e11a7-2800-363f-b11c-907909c50b5a | -11.0252 | -57.2436 | 2026-08-29 00:20:00 | GOES-19 | JUARA | MATO GROSSO | Brasil | 5105101 | 51 | 33 | nan | nan | nan | Amazônia | 105.6 |
| c1f3b54e-6fac-3b8c-ae26-21cdec982a31 | -5.8895 | -57.7513 | 2026-08-29 00:20:00 | GOES-19 | JACAREACANGA | PARÁ | Brasil | 1503754 | 15 | 33 | nan | nan | nan | Amazônia | 238.0 |
| da3526d3-ed55-3900-97fe-1616aa9cf6f5 | -11.0443 | -57.2222 | 2026-08-29 00:20:00 | GOES-19 | JUARA | MATO GROSSO | Brasil | 5105101 | 51 | 33 | nan | nan | nan | Amazônia | 140.5 |
| 1a2e6594-ebe8-3c7a-aafa-57b958b265ba | -5.8894 | -57.7708 | 2026-08-29 00:20:00 | GOES-19 | JACAREACANGA | PARÁ | Brasil | 1503754 | 15 | 33 | nan | nan | nan | Amazônia | 146.2 |
| 42d335d9-114e-3073-90b6-fd8e582b5cc1 | -7.5139 | -55.2851 | 2026-08-29 00:20:00 | GOES-19 | NOVO PROGRESSO | PARÁ | Brasil | 1505031 | 15 | 33 | nan | nan | nan | Amazônia | 67.9 |
| 385b48ef-a871-3b25-9310-8b2d0d49d743 | -7.5137 | -55.3051 | 2026-08-29 00:20:00 | GOES-19 | NOVO PROGRESSO | PARÁ | Brasil | 1505031 | 15 | 33 | nan | nan | nan | Amazônia | 80.9 |
| 3b63984c-670d-31a9-8ef3-affe8ab1fd70 | 2.4155 | -60.8699 | 2026-08-29 00:20:00 | GOES-19 | MUCAJAÍ | RORAIMA | Brasil | 1400308 | 14 | 33 | nan | nan | nan | Amazônia | 58.9 |
| 25db28df-0b8a-34fd-85bf-626726c9b3f0 | -6.7343 | -55.4671 | 2026-08-29 00:20:00 | GOES-19 | NOVO PROGRESSO | PARÁ | Brasil | 1505031 | 15 | 33 | nan | nan | nan | Amazônia | 114.2 |
| 14f7b0d5-8e9d-3d13-8b08-a171307f21a6 | -12.4305 | -43.3944 | 2026-08-29 00:20:00 | GOES-19 | MUQUÉM DO SÃO FRANCISCO | BAHIA | Brasil | 2922250 | 29 | 33 | nan | nan | nan | Cerrado | 71.6 |
| 8b0b866f-4441-37ed-9063-1a176b26efb9 | -8.9929 | -50.785 | 2026-08-29 00:20:00 | GOES-19 | SANTANA DO ARAGUAIA | PARÁ | Brasil | 1506708 | 15 | 33 | nan | nan | nan | Amazônia | 68.8 |
| d421404a-8d6d-34fe-b03f-9c75c2751740 | -6.6317 | -43.73 | 2026-08-29 00:20:00 | GOES-19 | SÃO JOÃO DOS PATOS | MARANHÃO | Brasil | 2111102 | 21 | 33 | nan | nan | nan | Cerrado | 143.8 |
| e630178d-778a-3140-865d-e4104f2b324a | -11.0445 | -57.2023 | 2026-08-29 00:20:00 | GOES-19 | JUARA | MATO GROSSO | Brasil | 5105101 | 51 | 33 | nan | nan | nan | Amazônia | 74.2 |
| 580919a5-f7e6-3078-bf45-80bddf49e868 | -10.9187 | -46.6192 | 2026-08-29 00:20:00 | GOES-19 | MATEIROS | TOCANTINS | Brasil | 1712702 | 17 | 33 | nan | nan | nan | Cerrado | 83.2 |
| 117d6527-b3fa-3018-83d9-dd84e11b6fad | -8.5358 | -55.3629 | 2026-08-29 00:20:00 | GOES-19 | NOVO PROGRESSO | PARÁ | Brasil | 1505031 | 15 | 33 | nan | nan | nan | Amazônia | 86.2 |
| ac669c24-6abd-3735-a4e2-074e2e27ce46 | -6.6505 | -43.7284 | 2026-08-29 00:20:00 | GOES-19 | SÃO JOÃO DOS PATOS | MARANHÃO | Brasil | 2111102 | 21 | 33 | nan | nan | nan | Cerrado | 52.3 |
| ad277ce9-eaee-3bc9-9d0f-6059b7d08a1c | -9.2465 | -65.5043 | 2026-08-29 00:20:00 | GOES-19 | LÁBREA | AMAZONAS | Brasil | 1302405 | 13 | 33 | nan | nan | nan | Amazônia | 49.7 |
| 69fa2009-0923-358d-96b7-0131be337ae0 | -6.6127 | -43.7549 | 2026-08-29 00:20:00 | GOES-19 | SÃO JOÃO DOS PATOS | MARANHÃO | Brasil | 2111102 | 21 | 33 | nan | nan | nan | Cerrado | 114.2 |
| 89009309-a4ce-3ab2-b7db-ff9863c863ef | -9.2644 | -45.6444 | 2026-08-29 00:20:00 | GOES-19 | SANTA FILOMENA | PIAUÍ | Brasil | 2209203 | 22 | 33 | nan | nan | nan | Cerrado | 47.3 |
| e2ef38e9-8a63-33d4-865e-8359c41f23f5 | -6.77 | -55.6445 | 2026-08-29 00:20:00 | GOES-19 | NOVO PROGRESSO | PARÁ | Brasil | 1505031 | 15 | 33 | nan | nan | nan | Amazônia | 56.8 |
| fdf0beee-3310-3986-9843-8b050ffe64c5 | -6.6129 | -43.7317 | 2026-08-29 00:20:00 | GOES-19 | SÃO JOÃO DOS PATOS | MARANHÃO | Brasil | 2111102 | 21 | 33 | nan | nan | nan | Cerrado | 108.4 |
| 031918e5-b625-38a5-b7ae-cbcc525f2c02 | -10.4609 | -64.4831 | 2026-08-29 00:20:00 | GOES-19 | NOVA MAMORÉ | RONDÔNIA | Brasil | 1100338 | 11 | 33 | nan | nan | nan | Amazônia | 32.7 |
| 73db996b-7598-3bc2-a7cc-e06fc1332b70 | -6.7699 | -55.6644 | 2026-08-29 00:20:00 | GOES-19 | NOVO PROGRESSO | PARÁ | Brasil | 1505031 | 15 | 33 | nan | nan | nan | Amazônia | 232.4 |
| a4681d50-5fe4-31ed-8bff-b644073a0b5e | -6.7698 | -55.6844 | 2026-08-29 00:20:00 | GOES-19 | NOVO PROGRESSO | PARÁ | Brasil | 1505031 | 15 | 33 | nan | nan | nan | Amazônia | 89.9 |
| a6b003b9-b7f0-36c8-bc72-d33f00da6046 | -5.9079 | -57.7506 | 2026-08-29 00:20:00 | GOES-19 | JACAREACANGA | PARÁ | Brasil | 1503754 | 15 | 33 | nan | nan | nan | Amazônia | 109.0 |
| 36212007-7043-365d-8eaf-83da33d75c7e | -7.2847 | -45.8652 | 2026-08-29 00:20:00 | GOES-19 | SÃO RAIMUNDO DAS MANGABEIRAS | MARANHÃO | Brasil | 2111607 | 21 | 33 | nan | nan | nan | Cerrado | 128.4 |
| 1ef72224-a141-3303-a517-cd020e1ce8dc | -10.4794 | -64.5012 | 2026-08-29 00:20:00 | GOES-19 | NOVA MAMORÉ | RONDÔNIA | Brasil | 1100338 | 11 | 33 | nan | nan | nan | Amazônia | 34.6 |
| 98b850a7-4915-3887-9778-d2f04599c5f9 | -6.7884 | -55.6635 | 2026-08-29 00:20:00 | GOES-19 | NOVO PROGRESSO | PARÁ | Brasil | 1505031 | 15 | 33 | nan | nan | nan | Amazônia | 73.3 |
| c465f5b0-0882-3dec-b185-7b69165e0476 | -5.9078 | -57.77 | 2026-08-29 00:20:00 | GOES-19 | JACAREACANGA | PARÁ | Brasil | 1503754 | 15 | 33 | nan | nan | nan | Amazônia | 50.2 |
| 2a5a6813-128d-366e-889c-896590049d16 | -3.8749 | -48.0458 | 2026-08-29 00:20:00 | GOES-19 | DOM ELISEU | PARÁ | Brasil | 1502939 | 15 | 33 | nan | nan | nan | Amazônia | 66.3 |
| 44022ba6-e65a-3df8-90a7-bcc0c0ae35f9 | -11.0441 | -57.2421 | 2026-08-29 00:20:00 | GOES-19 | JUARA | MATO GROSSO | Brasil | 5105101 | 51 | 33 | nan | nan | nan | Amazônia | 71.7 |
| eb64fbe9-ceec-33c9-a83d-5aaa8073a8b2 | -9.9288 | -60.4277 | 2026-08-29 00:20:00 | GOES-19 | ARIPUANÃ | MATO GROSSO | Brasil | 5101407 | 51 | 33 | nan | nan | nan | Amazônia | 58.4 |
| 3c8757b6-1fb2-3a04-9872-38c63bb75da7 | -10.4795 | -64.4824 | 2026-08-29 00:20:00 | GOES-19 | NOVA MAMORÉ | RONDÔNIA | Brasil | 1100338 | 11 | 33 | nan | nan | nan | Amazônia | 32.1 |
| e5b2fa87-8d74-39be-9da0-7000985bc1ea | -7.2849 | -45.8427 | 2026-08-29 00:20:00 | GOES-19 | SÃO RAIMUNDO DAS MANGABEIRAS | MARANHÃO | Brasil | 2111607 | 21 | 33 | nan | nan | nan | Cerrado | 113.9 |
| 8628801b-e8a3-3a8f-ba1d-114f1f11a82f | -11.0254 | -57.2237 | 2026-08-29 00:20:00 | GOES-19 | JUARA | MATO GROSSO | Brasil | 5105101 | 51 | 33 | nan | nan | nan | Amazônia | 103.9 |
| 9af3a994-727e-3fe3-8b6d-334aa8bfe186 | -14.2027 | -52.8432 | 2026-08-29 00:20:00 | GOES-19 | ÁGUA BOA | MATO GROSSO | Brasil | 5100201 | 51 | 33 | nan | nan | nan | Cerrado | 69.0 |
| 1ef960b8-7bbf-392e-8f65-d9857585ba34 | -20.941 | -57.5694 | 2026-08-29 00:20:00 | GOES-19 | PORTO MURTINHO | MATO GROSSO DO SUL | Brasil | 5006903 | 50 | 33 | nan | nan | nan | Pantanal | 122.3 |
| 73c580ac-b557-3e43-b900-be85e7ea6d36 | -10.7596 | -54.0384 | 2026-08-29 00:20:00 | GOES-19 | MARCELÂNDIA | MATO GROSSO | Brasil | 5105580 | 51 | 33 | nan | nan | nan | Amazônia | 45.7 |
| b9d1fc23-fbbf-3d6c-81d0-1dec49f50173 | -5.871 | -57.7715 | 2026-08-29 00:20:00 | GOES-19 | JACAREACANGA | PARÁ | Brasil | 1503754 | 15 | 33 | nan | nan | nan | Amazônia | 59.2 |
| 07f4b1ec-8c3c-31ec-8c5e-de919c4d86ef | -8.5359 | -55.3428 | 2026-08-29 00:20:00 | GOES-19 | NOVO PROGRESSO | PARÁ | Brasil | 1505031 | 15 | 33 | nan | nan | nan | Amazônia | 99.5 |
| acd967ac-6691-306d-bb5b-2fba1ffabf79 | -14.2027 | -52.8432 | 2026-08-29 00:30:00 | GOES-19 | ÁGUA BOA | MATO GROSSO | Brasil | 5100201 | 51 | 33 | nan | nan | nan | Cerrado | 63.6 |
| 105b93c9-9339-3dee-8748-7fe26e2cc564 | -5.8711 | -57.752 | 2026-08-29 00:30:00 | GOES-19 | JACAREACANGA | PARÁ | Brasil | 1503754 | 15 | 33 | nan | nan | nan | Amazônia | 47.9 |
| 96aa117b-dc20-3d56-ade8-c8107f60a528 | -8.9613 | -63.279 | 2026-08-29 00:30:00 | GOES-19 | ITAPUÃ DO OESTE | RONDÔNIA | Brasil | 1101104 | 11 | 33 | nan | nan | nan | Amazônia | 44.5 |
| 90ffbcd7-0b72-3dcb-ab7d-64d4daffa873 | -10.9187 | -46.6192 | 2026-08-29 00:30:00 | GOES-19 | MATEIROS | TOCANTINS | Brasil | 1712702 | 17 | 33 | nan | nan | nan | Cerrado | 280.8 |
| e87fb612-d1a9-3cbd-a811-7e2a0e48c9e5 | -6.6317 | -43.73 | 2026-08-29 00:30:00 | GOES-19 | SÃO JOÃO DOS PATOS | MARANHÃO | Brasil | 2111102 | 21 | 33 | nan | nan | nan | Cerrado | 265.9 |
| cb50da71-e436-3cc5-8c6b-56624878c445 | -6.7528 | -55.4661 | 2026-08-29 00:30:00 | GOES-19 | NOVO PROGRESSO | PARÁ | Brasil | 1505031 | 15 | 33 | nan | nan | nan | Amazônia | 66.8 |
| 0e73114c-91ac-3597-9638-12cf18507cba | -11.0443 | -57.2222 | 2026-08-29 00:30:00 | GOES-19 | JUARA | MATO GROSSO | Brasil | 5105101 | 51 | 33 | nan | nan | nan | Amazônia | 121.3 |
| f0dec345-9671-3958-8174-da80704af349 | -12.43 | -43.4182 | 2026-08-29 00:30:00 | GOES-19 | MUQUÉM DO SÃO FRANCISCO | BAHIA | Brasil | 2922250 | 29 | 33 | nan | nan | nan | Cerrado | 70.3 |
| 0bc6ed64-549b-31cc-afe7-88ee6ade5ea6 | -6.7699 | -55.6644 | 2026-08-29 00:30:00 | GOES-19 | NOVO PROGRESSO | PARÁ | Brasil | 1505031 | 15 | 33 | nan | nan | nan | Amazônia | 187.3 |
| 97067f2a-0734-3e74-9189-b2a4d27fbc51 | -8.9428 | -63.2797 | 2026-08-29 00:30:00 | GOES-19 | ITAPUÃ DO OESTE | RONDÔNIA | Brasil | 1101104 | 11 | 33 | nan | nan | nan | Amazônia | 59.8 |
| c4e99bf6-9c8e-360a-9adf-b574cde1059f | -10.9377 | -46.6168 | 2026-08-29 00:30:00 | GOES-19 | MATEIROS | TOCANTINS | Brasil | 1712702 | 17 | 33 | nan | nan | nan | Cerrado | 192.9 |
| c0223f57-c216-305d-9e74-ec0682bebc98 | -7.2849 | -45.8427 | 2026-08-29 00:30:00 | GOES-19 | SÃO RAIMUNDO DAS MANGABEIRAS | MARANHÃO | Brasil | 2111607 | 21 | 33 | nan | nan | nan | Cerrado | 116.3 |
| da6a1804-d2c7-378a-862c-e313c85c0804 | -6.6315 | -43.7533 | 2026-08-29 00:30:00 | GOES-19 | SÃO JOÃO DOS PATOS | MARANHÃO | Brasil | 2111102 | 21 | 33 | nan | nan | nan | Cerrado | 333.7 |
| a3e276d8-5891-3c19-b79d-ad69b33e862b | -6.7514 | -55.6654 | 2026-08-29 00:30:00 | GOES-19 | NOVO PROGRESSO | PARÁ | Brasil | 1505031 | 15 | 33 | nan | nan | nan | Amazônia | 63.9 |
| f755d036-b09a-35b4-b98d-506541cb462a | -10.919 | -46.5967 | 2026-08-29 00:30:00 | GOES-19 | MATEIROS | TOCANTINS | Brasil | 1712702 | 17 | 33 | nan | nan | nan | Cerrado | 137.8 |
| 3b8ae333-7377-36a9-8d9a-88800aaccd7a | -5.9079 | -57.7506 | 2026-08-29 00:30:00 | GOES-19 | JACAREACANGA | PARÁ | Brasil | 1503754 | 15 | 33 | nan | nan | nan | Amazônia | 96.1 |
| b9c36dfd-eb08-36d8-a504-fb2a3fe336b9 | -10.4981 | -64.5005 | 2026-08-29 00:30:00 | GOES-19 | NOVA MAMORÉ | RONDÔNIA | Brasil | 1100338 | 11 | 33 | nan | nan | nan | Amazônia | 39.9 |
| 5bb9351e-61e5-30dd-9537-f911fabf4005 | -4.3774 | -47.7627 | 2026-08-29 00:30:00 | GOES-19 | DOM ELISEU | PARÁ | Brasil | 1502939 | 15 | 33 | nan | nan | nan | Amazônia | 82.1 |
| 391dfc07-216d-3514-96e3-f0341e23493f | -11.0441 | -57.2421 | 2026-08-29 00:30:00 | GOES-19 | JUARA | MATO GROSSO | Brasil | 5105101 | 51 | 33 | nan | nan | nan | Amazônia | 70.7 |
| ed8c49c7-fc3d-35a9-b7d5-e329082e235b | -11.0254 | -57.2237 | 2026-08-29 00:30:00 | GOES-19 | JUARA | MATO GROSSO | Brasil | 5105101 | 51 | 33 | nan | nan | nan | Amazônia | 111.8 |
| d8b38a10-b35b-36d2-bf2f-2aff215122bf | -10.9 | -46.5991 | 2026-08-29 00:30:00 | GOES-19 | MATEIROS | TOCANTINS | Brasil | 1712702 | 17 | 33 | nan | nan | nan | Cerrado | 65.2 |
| 69eb8e33-3bb3-341d-ae53-e5113ad9ec5f | -6.6127 | -43.7549 | 2026-08-29 00:30:00 | GOES-19 | SÃO JOÃO DOS PATOS | MARANHÃO | Brasil | 2111102 | 21 | 33 | nan | nan | nan | Cerrado | 328.7 |
| e2a8d8d1-8946-38a1-a8b8-c4248ed5f9c5 | -3.8749 | -48.0458 | 2026-08-29 00:30:00 | GOES-19 | DOM ELISEU | PARÁ | Brasil | 1502939 | 15 | 33 | nan | nan | nan | Amazônia | 53.6 |


[Clique aqui para ver as próximas entradas](README7.md)
