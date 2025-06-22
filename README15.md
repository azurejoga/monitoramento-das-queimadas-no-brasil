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

## Dados Diários - Página 15

| ID | Latitude | Longitude | Data/Hora GMT | Satélite | Município | Estado | País | Município ID | Estado ID | País ID | Dias sem Chuva | Precipitação | Risco de Fogo | Bioma | FRP |
|----|----------|-----------|---------------|----------|-----------|--------|------|--------------|-----------|---------|----------------|--------------|----------------|-------|-----|
| 4a9633f7-79cf-34d8-9730-7fab35fd94bc | -11.6128 | -58.2901 | 2025-06-22 05:55:00 | NOAA-21 | BRASNORTE | MATO GROSSO | Brasil | 5101902 | 51 | 33 | nan | nan | nan | Amazônia | 4.3 |
| 7ce23c90-6b5a-3f1c-be6a-50b1aa0be4a3 | -9.63881 | -62.19859 | 2025-06-22 05:55:00 | NOAA-21 | MACHADINHO D'OESTE | RONDÔNIA | Brasil | 1100130 | 11 | 33 | nan | nan | nan | Amazônia | 2.6 |
| 4554bf96-aa18-32f9-a4a8-a23a00632ae0 | -9.25819 | -57.53168 | 2025-06-22 05:55:00 | NOAA-21 | APIACÁS | MATO GROSSO | Brasil | 5100805 | 51 | 33 | nan | nan | nan | Amazônia | 1.1 |
| 59eab251-a412-33e4-aeb3-6d622c8ecba6 | -11.78931 | -57.23856 | 2025-06-22 05:55:00 | NOAA-21 | PORTO DOS GAÚCHOS | MATO GROSSO | Brasil | 5106802 | 51 | 33 | nan | nan | nan | Amazônia | 7.5 |
| 1328c15a-6713-3431-8f85-2345f5df778c | -9.17292 | -61.40288 | 2025-06-22 05:55:00 | NOAA-21 | COLNIZA | MATO GROSSO | Brasil | 5103254 | 51 | 33 | nan | nan | nan | Amazônia | 11.1 |
| d3e22bf6-ba90-3ec0-8877-a9f84a002eac | -9.25408 | -57.53114 | 2025-06-22 05:55:00 | NOAA-21 | APIACÁS | MATO GROSSO | Brasil | 5100805 | 51 | 33 | nan | nan | nan | Amazônia | 4.5 |
| d08363fb-217b-3103-bbd7-a672acba4ea5 | -9.46481 | -56.05953 | 2025-06-22 05:55:00 | NOAA-21 | ALTA FLORESTA | MATO GROSSO | Brasil | 5100250 | 51 | 33 | nan | nan | nan | Amazônia | 14.9 |
| 3108b8b4-cbf7-36f6-8cdc-46265e2044de | -11.84262 | -57.75987 | 2025-06-22 05:55:00 | NOAA-21 | JUARA | MATO GROSSO | Brasil | 5105101 | 51 | 33 | nan | nan | nan | Amazônia | 1.8 |
| c9b94099-7ede-3eb3-ac8e-d42340f78028 | -9.92105 | -59.90791 | 2025-06-22 05:55:00 | NOAA-21 | ARIPUANÃ | MATO GROSSO | Brasil | 5101407 | 51 | 33 | nan | nan | nan | Amazônia | 4.9 |
| fd37922f-b49f-3e9f-92b5-7f8e79295f81 | -11.62511 | -58.29193 | 2025-06-22 05:55:00 | NOAA-21 | BRASNORTE | MATO GROSSO | Brasil | 5101902 | 51 | 33 | nan | nan | nan | Amazônia | 8.0 |
| fa190cf8-58d8-3cde-a752-b1529d7698f8 | -9.03317 | -61.23743 | 2025-06-22 05:55:00 | NOAA-21 | COLNIZA | MATO GROSSO | Brasil | 5103254 | 51 | 33 | nan | nan | nan | Amazônia | 2.1 |
| 663b275c-3afb-3509-a448-4284a5fd4732 | -11.83564 | -57.76424 | 2025-06-22 05:55:00 | NOAA-21 | JUARA | MATO GROSSO | Brasil | 5105101 | 51 | 33 | nan | nan | nan | Amazônia | 1.8 |
| c196e272-3ccb-3ae0-a568-ebfc84d8aefe | -8.1236 | -61.41593 | 2025-06-22 06:22:00 | NPP-375D | NOVO ARIPUANÃ | AMAZONAS | Brasil | 1303304 | 13 | 33 | nan | nan | nan | Amazônia | 3.1 |
| 6ba91758-03a0-366e-b7a0-faa435b063e4 | -9.17036 | -61.4101 | 2025-06-22 06:22:00 | NPP-375D | COLNIZA | MATO GROSSO | Brasil | 5103254 | 51 | 33 | nan | nan | nan | Amazônia | 5.3 |
| 6cda662e-3563-315e-ad7f-8efa8098cc53 | -9.17109 | -61.40857 | 2025-06-22 06:22:00 | NPP-375D | COLNIZA | MATO GROSSO | Brasil | 5103254 | 51 | 33 | nan | nan | nan | Amazônia | 4.7 |
| 489091e0-5b44-336e-a6fc-4af2d9a48173 | -6.9318 | -43.7729 | 2025-06-22 11:40:00 | GOES-19 | GUADALUPE | PIAUÍ | Brasil | 2204501 | 22 | 33 | nan | nan | nan | Cerrado | 107.0 |
| a1b0c149-ef05-3a1a-9cc5-8de539742fb1 | -4.538 | -48.00778 | 2025-06-22 12:44:00 | TERRA_M-T | RONDON DO PARÁ | PARÁ | Brasil | 1506187 | 15 | 33 | nan | nan | nan | Amazônia | 9.9 |
| 47b1b589-5008-3181-a325-33d199d0e8ae | -4.30287 | -48.07404 | 2025-06-22 12:44:00 | TERRA_M-T | DOM ELISEU | PARÁ | Brasil | 1502939 | 15 | 33 | nan | nan | nan | Amazônia | 33.8 |
| 914a998f-91e5-3f8e-a4d8-c47c2a3ebad8 | -7.34368 | -45.33687 | 2025-06-22 12:44:00 | TERRA_M-T | LORETO | MARANHÃO | Brasil | 2106102 | 21 | 33 | nan | nan | nan | Cerrado | 16.0 |
| 4001aa00-2a9e-30dd-97c8-371aa85cfd5d | -7.34088 | -45.35844 | 2025-06-22 12:44:00 | TERRA_M-T | LORETO | MARANHÃO | Brasil | 2106102 | 21 | 33 | nan | nan | nan | Cerrado | 49.8 |
| ee783ded-2156-37b3-98a0-62a2298b0de0 | -4.5451 | -48.01533 | 2025-06-22 12:44:00 | TERRA_M-T | RONDON DO PARÁ | PARÁ | Brasil | 1506187 | 15 | 33 | nan | nan | nan | Amazônia | 11.5 |
| 0fcd4301-2179-39be-a60f-8f9e19bf7e92 | -6.90598 | -43.77961 | 2025-06-22 12:44:00 | TERRA_M-T | GUADALUPE | PIAUÍ | Brasil | 2204501 | 22 | 33 | nan | nan | nan | Cerrado | 27.0 |
| e23fb4f8-3665-3191-a5a0-177b8a195cc1 | -7.32756 | -45.35675 | 2025-06-22 12:44:00 | TERRA_M-T | LORETO | MARANHÃO | Brasil | 2106102 | 21 | 33 | nan | nan | nan | Cerrado | 35.1 |
| c2f6def5-dec8-3adb-8cc3-0ad1d4fdb1cf | -11.93856 | -47.84372 | 2025-06-22 12:46:00 | TERRA_M-T | NATIVIDADE | TOCANTINS | Brasil | 1714203 | 17 | 33 | nan | nan | nan | Cerrado | 15.2 |
| e6e7dc45-19be-300f-902e-2f681d0d5d69 | -10.828 | -46.35836 | 2025-06-22 12:46:00 | TERRA_M-T | MATEIROS | TOCANTINS | Brasil | 1712702 | 17 | 33 | nan | nan | nan | Cerrado | 17.0 |
| 684955ae-6c94-33b3-8a9c-3fa95fd6e2ef | -12.4797 | -54.4253 | 2025-06-22 12:46:00 | TERRA_M-T | NOVA UBIRATÃ | MATO GROSSO | Brasil | 5106240 | 51 | 33 | nan | nan | nan | Amazônia | 5.8 |
| a1e57242-1230-3b59-a481-d5593ef9c25e | -9.90353 | -46.34783 | 2025-06-22 12:46:00 | TERRA_M-T | ALTO PARNAÍBA | MARANHÃO | Brasil | 2100501 | 21 | 33 | nan | nan | nan | Cerrado | 17.5 |
| 26ed8de1-7a47-38c8-93e2-23818a99e2b4 | -11.91262 | -54.8229 | 2025-06-22 12:46:00 | TERRA_M-T | SANTA CARMEM | MATO GROSSO | Brasil | 5107248 | 51 | 33 | nan | nan | nan | Amazônia | 9.9 |
| b70ab121-1122-3bc0-8067-73158100b758 | -11.14186 | -53.91931 | 2025-06-22 12:46:00 | TERRA_M-T | MARCELÂNDIA | MATO GROSSO | Brasil | 5105580 | 51 | 33 | nan | nan | nan | Amazônia | 8.7 |
| 09445ad8-a3de-3336-b404-db6f94ab7b46 | -10.86162 | -53.75684 | 2025-06-22 12:46:00 | TERRA_M-T | MARCELÂNDIA | MATO GROSSO | Brasil | 5105580 | 51 | 33 | nan | nan | nan | Amazônia | 12.6 |
| 0944c660-d48d-3fc6-a305-e887f2ee44c3 | -14.28656 | -53.22001 | 2025-06-22 12:46:00 | TERRA_M-T | CAMPINÁPOLIS | MATO GROSSO | Brasil | 5102603 | 51 | 33 | nan | nan | nan | Cerrado | 8.2 |
| e9f213f3-f8b8-389f-aee6-7d1c9fa79a5a | -10.30262 | -57.14037 | 2025-06-22 12:46:00 | TERRA_M-T | NOVA MONTE VERDE | MATO GROSSO | Brasil | 5108956 | 51 | 33 | nan | nan | nan | Amazônia | 8.7 |
| e865cf2e-1968-3394-ab98-adb33d838da9 | -11.81297 | -56.95511 | 2025-06-22 12:46:00 | TERRA_M-T | PORTO DOS GAÚCHOS | MATO GROSSO | Brasil | 5106802 | 51 | 33 | nan | nan | nan | Amazônia | 28.2 |
| d7da3a84-5ed4-369e-b53d-c2d35d798855 | -13.79996 | -54.29699 | 2025-06-22 12:46:00 | TERRA_M-T | PARANATINGA | MATO GROSSO | Brasil | 5106307 | 51 | 33 | nan | nan | nan | Cerrado | 9.9 |
| 7395657a-19be-32db-b2ff-c115b4468c20 | -11.11741 | -46.66443 | 2025-06-22 12:46:00 | TERRA_M-T | MATEIROS | TOCANTINS | Brasil | 1712702 | 17 | 33 | nan | nan | nan | Cerrado | 21.4 |
| 5fa3b5f8-f841-3993-940d-5719fa04fafd | -11.81103 | -56.96769 | 2025-06-22 12:46:00 | TERRA_M-T | PORTO DOS GAÚCHOS | MATO GROSSO | Brasil | 5106802 | 51 | 33 | nan | nan | nan | Amazônia | 26.9 |
| 22d5a8f2-7190-37a8-9017-357f997b96ac | -10.93499 | -57.12718 | 2025-06-22 12:46:00 | TERRA_M-T | JUARA | MATO GROSSO | Brasil | 5105101 | 51 | 33 | nan | nan | nan | Amazônia | 89.4 |
| 7e5d3038-fc25-3e77-b2c2-c20d4b5693bf | -11.57001 | -52.0972 | 2025-06-22 12:46:00 | TERRA_M-T | SÃO FÉLIX DO ARAGUAIA | MATO GROSSO | Brasil | 5107859 | 51 | 33 | nan | nan | nan | Amazônia | 5.7 |
| a9e4819a-4f27-377f-9990-cf4745d6db41 | -11.30394 | -48.15883 | 2025-06-22 12:46:00 | TERRA_M-T | SANTA ROSA DO TOCANTINS | TOCANTINS | Brasil | 1718907 | 17 | 33 | nan | nan | nan | Cerrado | 11.6 |
| d620202d-073e-320c-bbd9-a8b5c2c8fa5b | -10.81682 | -46.35041 | 2025-06-22 12:46:00 | TERRA_M-T | MATEIROS | TOCANTINS | Brasil | 1712702 | 17 | 33 | nan | nan | nan | Cerrado | 20.0 |
| a8454067-af5e-36f9-85c5-6c2169ed7656 | -9.90809 | -52.44805 | 2025-06-22 12:46:00 | TERRA_M-T | SANTA CRUZ DO XINGU | MATO GROSSO | Brasil | 5107743 | 51 | 33 | nan | nan | nan | Amazônia | 19.9 |
| 14b414f9-72a8-3253-984e-4b24bf82496f | -11.91405 | -54.81328 | 2025-06-22 12:46:00 | TERRA_M-T | SANTA CARMEM | MATO GROSSO | Brasil | 5107248 | 51 | 33 | nan | nan | nan | Amazônia | 12.2 |
| 6b5a1148-5c70-32a7-a26c-7c1a504d673f | -12.52624 | -57.22973 | 2025-06-22 12:46:00 | TERRA_M-T | NOVA MARINGÁ | MATO GROSSO | Brasil | 5108907 | 51 | 33 | nan | nan | nan | Amazônia | 11.2 |
| 75ff0230-8db1-32c9-a73f-1553550edc27 | -9.90414 | -46.34066 | 2025-06-22 12:46:00 | TERRA_M-T | ALTO PARNAÍBA | MARANHÃO | Brasil | 2100501 | 21 | 33 | nan | nan | nan | Cerrado | 26.0 |
| 14568b9a-2519-30c0-a132-57acbd347983 | -10.6053 | -47.09361 | 2025-06-22 12:46:00 | TERRA_M-T | PONTE ALTA DO TOCANTINS | TOCANTINS | Brasil | 1717909 | 17 | 33 | nan | nan | nan | Cerrado | 35.0 |
| c899e574-3b8b-338b-95ff-e0e8db597067 | -10.83044 | -46.3381 | 2025-06-22 12:46:00 | TERRA_M-T | MATEIROS | TOCANTINS | Brasil | 1712702 | 17 | 33 | nan | nan | nan | Cerrado | 18.9 |
| ea4f0279-405e-33cf-b61e-a956fa34bd35 | -10.39705 | -43.30523 | 2025-06-22 12:46:00 | TERRA_M-T | BARRA | BAHIA | Brasil | 2902708 | 29 | 33 | nan | nan | nan | Caatinga | 31.9 |
| 5855444c-942d-33e9-8422-5b374615bbc9 | -8.598 | -51.54064 | 2025-06-22 12:46:00 | TERRA_M-T | CUMARU DO NORTE | PARÁ | Brasil | 1502764 | 15 | 33 | nan | nan | nan | Amazônia | 11.8 |
| 1890d479-bb3f-3ae1-9e50-27cf3271a862 | -11.80929 | -56.96053 | 2025-06-22 12:46:00 | TERRA_M-T | PORTO DOS GAÚCHOS | MATO GROSSO | Brasil | 5106802 | 51 | 33 | nan | nan | nan | Amazônia | 32.3 |
| 2e408d3f-9aeb-3059-aeed-ea6fe2f85c46 | -10.6094 | -47.09986 | 2025-06-22 12:46:00 | TERRA_M-T | PONTE ALTA DO TOCANTINS | TOCANTINS | Brasil | 1717909 | 17 | 33 | nan | nan | nan | Cerrado | 19.5 |
| 7d310fa1-a907-3706-a3e0-b37f30991153 | -13.04636 | -53.71126 | 2025-06-22 12:46:00 | TERRA_M-T | GAÚCHA DO NORTE | MATO GROSSO | Brasil | 5103858 | 51 | 33 | nan | nan | nan | Amazônia | 9.4 |
| 1af2e7b0-4c67-3c89-b1d3-3a1d2cbc3156 | -10.86029 | -53.76593 | 2025-06-22 12:46:00 | TERRA_M-T | MARCELÂNDIA | MATO GROSSO | Brasil | 5105580 | 51 | 33 | nan | nan | nan | Amazônia | 15.8 |
| 1d6ab6fb-1a79-34e4-bfc4-b77fb5c9f0ab | -11.11742 | -46.65766 | 2025-06-22 12:46:00 | TERRA_M-T | MATEIROS | TOCANTINS | Brasil | 1712702 | 17 | 33 | nan | nan | nan | Cerrado | 16.4 |
| bba534cb-bacb-3c31-8289-93001880d140 | -13.44643 | -56.93071 | 2025-06-22 12:46:00 | TERRA_M-T | SÃO JOSÉ DO RIO CLARO | MATO GROSSO | Brasil | 5107305 | 51 | 33 | nan | nan | nan | Cerrado | 7.7 |
| aa67dc7c-89aa-33a5-9e76-b94c4db2d359 | -13.44458 | -56.94257 | 2025-06-22 12:46:00 | TERRA_M-T | SÃO JOSÉ DO RIO CLARO | MATO GROSSO | Brasil | 5107305 | 51 | 33 | nan | nan | nan | Cerrado | 8.0 |
| 42785c52-5e49-3be6-8abf-035a542a376b | -10.93703 | -57.11404 | 2025-06-22 12:46:00 | TERRA_M-T | JUARA | MATO GROSSO | Brasil | 5105101 | 51 | 33 | nan | nan | nan | Amazônia | 31.5 |
| 3766be9f-9e91-3342-b70c-2fdd70bb323b | -13.79107 | -54.29565 | 2025-06-22 12:46:00 | TERRA_M-T | PARANATINGA | MATO GROSSO | Brasil | 5106307 | 51 | 33 | nan | nan | nan | Cerrado | 16.2 |
| 9b56ea35-04cd-373f-918a-14668ad81655 | -12.35932 | -49.97984 | 2025-06-22 12:46:00 | TERRA_M-T | SANDOLÂNDIA | TOCANTINS | Brasil | 1718840 | 17 | 33 | nan | nan | nan | Cerrado | 8.5 |
| 2fc5abdb-26e1-3047-9049-6476f80a42d8 | -10.86919 | -53.76724 | 2025-06-22 12:46:00 | TERRA_M-T | MARCELÂNDIA | MATO GROSSO | Brasil | 5105580 | 51 | 33 | nan | nan | nan | Amazônia | 20.3 |
| a6a54591-5db3-399a-8f2d-5caec952372c | -17.6317 | -53.54491 | 2025-06-22 12:49:00 | TERRA_M-T | ALTO ARAGUAIA | MATO GROSSO | Brasil | 5100300 | 51 | 33 | nan | nan | nan | Cerrado | 4.3 |
| 2c5ff948-0dad-3951-abe1-22c09faa8f5c | -10.9324 | -57.1312 | 2025-06-22 12:50:00 | GOES-19 | JUARA | MATO GROSSO | Brasil | 5105101 | 51 | 33 | nan | nan | nan | Amazônia | 71.4 |
| f4b82868-6c63-3ef7-a38d-92e24096ba25 | -10.9324 | -57.1312 | 2025-06-22 13:00:00 | GOES-19 | JUARA | MATO GROSSO | Brasil | 5105101 | 51 | 33 | nan | nan | nan | Amazônia | 68.2 |
| 2a963fc6-6d5d-3163-a65a-fcda9edb42dd | -10.9324 | -57.1312 | 2025-06-22 13:10:00 | GOES-19 | JUARA | MATO GROSSO | Brasil | 5105101 | 51 | 33 | nan | nan | nan | Amazônia | 64.6 |
| a7101ca2-c902-3922-aa45-d3b76e017f1a | -10.4567 | -47.0124 | 2025-06-22 13:20:00 | GOES-19 | MATEIROS | TOCANTINS | Brasil | 1712702 | 17 | 33 | nan | nan | nan | Cerrado | 88.8 |
| 77fcbb21-84c9-36a4-b925-93689e341bc1 | -10.9324 | -57.1312 | 2025-06-22 13:20:00 | GOES-19 | JUARA | MATO GROSSO | Brasil | 5105101 | 51 | 33 | nan | nan | nan | Amazônia | 63.1 |
| 73a4cfc7-f2af-3f39-a5d3-a9215d81219b | -10.4564 | -47.0347 | 2025-06-22 13:20:00 | GOES-19 | MATEIROS | TOCANTINS | Brasil | 1712702 | 17 | 33 | nan | nan | nan | Cerrado | 101.2 |
| cb97645d-0525-3688-a5e2-5e98483a1919 | -14.1739 | -54.6817 | 2025-06-22 13:30:00 | GOES-19 | PARANATINGA | MATO GROSSO | Brasil | 5106307 | 51 | 33 | nan | nan | nan | Cerrado | 77.6 |
| fe7110c0-979f-3ec9-87c4-a5b8dadee269 | -10.8571 | -53.7631 | 2025-06-22 13:30:00 | GOES-19 | MARCELÂNDIA | MATO GROSSO | Brasil | 5105580 | 51 | 33 | nan | nan | nan | Amazônia | 64.1 |
| 6b77d8a0-e744-3a6d-9b79-156f73cfb3c6 | -10.9324 | -57.1312 | 2025-06-22 13:30:00 | GOES-19 | JUARA | MATO GROSSO | Brasil | 5105101 | 51 | 33 | nan | nan | nan | Amazônia | 75.2 |
| d6f3193f-0911-3e10-bc3c-669602eea681 | -10.4754 | -47.0325 | 2025-06-22 13:40:00 | GOES-19 | MATEIROS | TOCANTINS | Brasil | 1712702 | 17 | 33 | nan | nan | nan | Cerrado | 129.3 |
| 88f70c04-b070-3453-bc59-4d2d565fb119 | -10.4567 | -47.0124 | 2025-06-22 13:40:00 | GOES-19 | MATEIROS | TOCANTINS | Brasil | 1712702 | 17 | 33 | nan | nan | nan | Cerrado | 133.3 |
| 736cfe24-2c8e-35f2-9844-80db8ecd662d | -10.9324 | -57.1312 | 2025-06-22 13:40:00 | GOES-19 | JUARA | MATO GROSSO | Brasil | 5105101 | 51 | 33 | nan | nan | nan | Amazônia | 86.6 |
| b59278ba-6f42-3df3-b241-9b218cae8565 | -10.4564 | -47.0347 | 2025-06-22 13:40:00 | GOES-19 | MATEIROS | TOCANTINS | Brasil | 1712702 | 17 | 33 | nan | nan | nan | Cerrado | 130.8 |
| a477d8c2-5c80-3d77-805e-8266a95abeff | -14.1739 | -54.6817 | 2025-06-22 13:40:00 | GOES-19 | PARANATINGA | MATO GROSSO | Brasil | 5106307 | 51 | 33 | nan | nan | nan | Cerrado | 79.6 |
| e67f2bca-a879-35e3-96a1-543b97772329 | -10.8571 | -53.7631 | 2025-06-22 13:40:00 | GOES-19 | MARCELÂNDIA | MATO GROSSO | Brasil | 5105580 | 51 | 33 | nan | nan | nan | Amazônia | 67.9 |
| f0a9bd3c-3f6b-3a8b-8022-50379423d51b | -10.4564 | -47.0347 | 2025-06-22 13:50:00 | GOES-19 | MATEIROS | TOCANTINS | Brasil | 1712702 | 17 | 33 | nan | nan | nan | Cerrado | 107.3 |
| 829fe26a-6055-3a49-a26e-204c3ffac1d0 | -10.8571 | -53.7631 | 2025-06-22 13:50:00 | GOES-19 | MARCELÂNDIA | MATO GROSSO | Brasil | 5105580 | 51 | 33 | nan | nan | nan | Amazônia | 68.4 |
| d8931e17-2089-3726-abd7-cb9d1510d162 | -10.9324 | -57.1312 | 2025-06-22 13:50:00 | GOES-19 | JUARA | MATO GROSSO | Brasil | 5105101 | 51 | 33 | nan | nan | nan | Amazônia | 71.7 |
| e99224db-57f0-3783-af76-df843f42b7b0 | -10.4754 | -47.0325 | 2025-06-22 13:50:00 | GOES-19 | MATEIROS | TOCANTINS | Brasil | 1712702 | 17 | 33 | nan | nan | nan | Cerrado | 96.5 |
| 5d111d2b-27ad-3291-882f-3e11aa21a720 | -10.8571 | -53.7631 | 2025-06-22 14:00:00 | GOES-19 | MARCELÂNDIA | MATO GROSSO | Brasil | 5105580 | 51 | 33 | nan | nan | nan | Amazônia | 67.0 |
| 8d5fb40f-8c04-3e3f-8373-1fa3e97dbb54 | -10.5718 | -46.9315 | 2025-06-22 14:00:00 | GOES-19 | MATEIROS | TOCANTINS | Brasil | 1712702 | 17 | 33 | nan | nan | nan | Cerrado | 88.3 |
| f77a4dde-1ef9-3e5d-9081-d043a8e98283 | -9.8104 | -47.1764 | 2025-06-22 14:00:00 | GOES-19 | RIO SONO | TOCANTINS | Brasil | 1718758 | 17 | 33 | nan | nan | nan | Cerrado | 81.8 |
| ec9919d3-6f82-3325-af82-01ed60ed9195 | -10.9324 | -57.1312 | 2025-06-22 14:00:00 | GOES-19 | JUARA | MATO GROSSO | Brasil | 5105101 | 51 | 33 | nan | nan | nan | Amazônia | 71.7 |
| 75f5051b-a881-373b-aa4e-622ec634c24a | -10.876 | -53.7614 | 2025-06-22 14:00:00 | GOES-19 | MARCELÂNDIA | MATO GROSSO | Brasil | 5105580 | 51 | 33 | nan | nan | nan | Amazônia | 59.0 |
| 42ed98f9-3d94-3434-bddf-c2404592df3a | -10.4754 | -47.0325 | 2025-06-22 14:00:00 | GOES-19 | MATEIROS | TOCANTINS | Brasil | 1712702 | 17 | 33 | nan | nan | nan | Cerrado | 92.1 |
| 6efd4421-e36b-37f1-9d6e-c6da93b1ddce | -10.828 | -46.338 | 2025-06-22 14:10:00 | GOES-19 | MATEIROS | TOCANTINS | Brasil | 1712702 | 17 | 33 | nan | nan | nan | Cerrado | 95.2 |
| f4f5b63f-da54-377d-b39d-f8216d419736 | -10.6074 | -47.0834 | 2025-06-22 14:10:00 | GOES-19 | PONTE ALTA DO TOCANTINS | TOCANTINS | Brasil | 1717909 | 17 | 33 | nan | nan | nan | Cerrado | 116.3 |
| cd1f4c8e-472f-3c89-b781-2ee908a24ee6 | -10.9324 | -57.1312 | 2025-06-22 14:10:00 | GOES-19 | JUARA | MATO GROSSO | Brasil | 5105101 | 51 | 33 | nan | nan | nan | Amazônia | 59.9 |
| d36b4fcd-bb7d-3690-9131-49dbbac81bf5 | -9.8104 | -47.1764 | 2025-06-22 14:10:00 | GOES-19 | RIO SONO | TOCANTINS | Brasil | 1718758 | 17 | 33 | nan | nan | nan | Cerrado | 91.2 |
| 2119246a-5309-3368-88e6-8d9ee44edd3c | -10.8571 | -53.7631 | 2025-06-22 14:10:00 | GOES-19 | MARCELÂNDIA | MATO GROSSO | Brasil | 5105580 | 51 | 33 | nan | nan | nan | Amazônia | 70.9 |
| b8835763-6619-31df-834d-d9e1c433dc72 | -10.6071 | -47.1057 | 2025-06-22 14:10:00 | GOES-19 | PONTE ALTA DO TOCANTINS | TOCANTINS | Brasil | 1717909 | 17 | 33 | nan | nan | nan | Cerrado | 92.4 |
| 5fad61de-3b87-3747-804c-2be4ce3f930a | -14.1739 | -54.6817 | 2025-06-22 14:20:00 | GOES-19 | PARANATINGA | MATO GROSSO | Brasil | 5106307 | 51 | 33 | nan | nan | nan | Cerrado | 85.1 |
| ee757d0a-efda-341f-a32e-2faa6823e2ab | -10.876 | -53.7614 | 2025-06-22 14:20:00 | GOES-19 | MARCELÂNDIA | MATO GROSSO | Brasil | 5105580 | 51 | 33 | nan | nan | nan | Amazônia | 65.4 |
| afd4d1fd-e597-3214-9e55-ce31377f9377 | -10.9324 | -57.1312 | 2025-06-22 14:20:00 | GOES-19 | JUARA | MATO GROSSO | Brasil | 5105101 | 51 | 33 | nan | nan | nan | Amazônia | 57.3 |
| 4ff7115f-42b4-322e-b196-73d51c564241 | -9.8104 | -47.1764 | 2025-06-22 14:20:00 | GOES-19 | RIO SONO | TOCANTINS | Brasil | 1718758 | 17 | 33 | nan | nan | nan | Cerrado | 96.7 |
| 78a68566-e735-3770-a653-d4506b205bf6 | -10.8571 | -53.7631 | 2025-06-22 14:20:00 | GOES-19 | MARCELÂNDIA | MATO GROSSO | Brasil | 5105580 | 51 | 33 | nan | nan | nan | Amazônia | 71.8 |
| a75a4c1f-c081-39af-a4cc-e98aea18f7d4 | -10.6071 | -47.1057 | 2025-06-22 14:30:00 | GOES-19 | PONTE ALTA DO TOCANTINS | TOCANTINS | Brasil | 1717909 | 17 | 33 | nan | nan | nan | Cerrado | 107.4 |
| dea8ffaf-f2f6-35c1-88f0-a117f525fb5b | -10.8571 | -53.7631 | 2025-06-22 14:30:00 | GOES-19 | MARCELÂNDIA | MATO GROSSO | Brasil | 5105580 | 51 | 33 | nan | nan | nan | Amazônia | 86.1 |
| 499e7050-fbac-35e5-9039-00ff5c55be15 | -10.4564 | -47.0347 | 2025-06-22 14:30:00 | GOES-19 | MATEIROS | TOCANTINS | Brasil | 1712702 | 17 | 33 | nan | nan | nan | Cerrado | 110.6 |
| 35ee7de0-547b-330d-a61f-484ee52a4c29 | -7.3277 | -45.3649 | 2025-06-22 14:30:00 | GOES-19 | LORETO | MARANHÃO | Brasil | 2106102 | 21 | 33 | nan | nan | nan | Cerrado | 92.7 |


[Clique aqui para ver as próximas entradas](README16.md)
