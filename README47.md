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

## Dados Diários - Página 47

| ID | Latitude | Longitude | Data/Hora GMT | Satélite | Município | Estado | País | Município ID | Estado ID | País ID | Dias sem Chuva | Precipitação | Risco de Fogo | Bioma | FRP |
|----|----------|-----------|---------------|----------|-----------|--------|------|--------------|-----------|---------|----------------|--------------|----------------|-------|-----|
| 1f5817db-43af-3cee-be42-0160e993acb7 | -14.25327 | -58.54073 | 2025-08-23 04:53:00 | NOAA-21 | TANGARÁ DA SERRA | MATO GROSSO | Brasil | 5107958 | 51 | 33 | nan | nan | nan | Cerrado | 0.8 |
| 39cc671b-2e2c-37cb-ba20-568c317dda09 | -13.49499 | -47.03418 | 2025-08-23 04:53:00 | NOAA-21 | MONTE ALEGRE DE GOIÁS | GOIÁS | Brasil | 5213509 | 52 | 33 | nan | nan | nan | Cerrado | 2.7 |
| 91e9f1aa-940d-3f57-ad9b-b45b03cf3602 | -15.01304 | -54.88588 | 2025-08-23 04:53:00 | NOAA-21 | NOVA BRASILÂNDIA | MATO GROSSO | Brasil | 5106208 | 51 | 33 | nan | nan | nan | Cerrado | 2.4 |
| f01c4ace-ca2f-38df-b0a9-166ea0a539b5 | -9.95145 | -60.18871 | 2025-08-23 04:53:00 | NOAA-21 | ARIPUANÃ | MATO GROSSO | Brasil | 5101407 | 51 | 33 | nan | nan | nan | Amazônia | 26.5 |
| e1e26e7f-adda-3cb1-8ed3-4539cbd8bad5 | -9.9588 | -60.19918 | 2025-08-23 04:53:00 | NOAA-21 | ARIPUANÃ | MATO GROSSO | Brasil | 5101407 | 51 | 33 | nan | nan | nan | Amazônia | 174.0 |
| 2a284559-ab35-3b79-8b65-a228df37feca | -15.21911 | -53.86036 | 2025-08-23 04:53:00 | NOAA-21 | NOVO SÃO JOAQUIM | MATO GROSSO | Brasil | 5106281 | 51 | 33 | nan | nan | nan | Cerrado | 2.3 |
| c3427e53-e8f7-3650-ae5f-f5af99fb39de | -11.50726 | -50.4725 | 2025-08-23 04:53:00 | NOAA-21 | LAGOA DA CONFUSÃO | TOCANTINS | Brasil | 1711902 | 17 | 33 | nan | nan | nan | Cerrado | 1.6 |
| e83af70b-f4b1-36bc-8afb-2a2f3a9d89c3 | -13.3416 | -54.39627 | 2025-08-23 04:53:00 | NOAA-21 | PARANATINGA | MATO GROSSO | Brasil | 5106307 | 51 | 33 | nan | nan | nan | Amazônia | 0.9 |
| dfbd0df3-9a11-3b29-a5e7-c8fe58a822d4 | -9.82156 | -64.26812 | 2025-08-23 04:53:00 | NOAA-21 | PORTO VELHO | RONDÔNIA | Brasil | 1100205 | 11 | 33 | nan | nan | nan | Amazônia | 1.7 |
| f26fe8d3-1fca-3d78-8e2a-e743c0f6fda4 | -13.36862 | -54.39705 | 2025-08-23 04:53:00 | NOAA-21 | PARANATINGA | MATO GROSSO | Brasil | 5106307 | 51 | 33 | nan | nan | nan | Amazônia | 1.0 |
| f1833fdc-8c48-3d68-b317-587c5d8b3a94 | -13.46297 | -47.02377 | 2025-08-23 04:53:00 | NOAA-21 | MONTE ALEGRE DE GOIÁS | GOIÁS | Brasil | 5213509 | 52 | 33 | nan | nan | nan | Cerrado | 7.3 |
| 2bec08a2-97f6-3328-95b8-1330e68e6b3d | -14.65722 | -56.59026 | 2025-08-23 04:53:00 | NOAA-21 | ALTO PARAGUAI | MATO GROSSO | Brasil | 5100508 | 51 | 33 | nan | nan | nan | Cerrado | 3.3 |
| 4b72d737-e2f2-34a1-8bea-37a87832846d | -9.51922 | -60.55827 | 2025-08-23 04:53:00 | NOAA-21 | ARIPUANÃ | MATO GROSSO | Brasil | 5101407 | 51 | 33 | nan | nan | nan | Amazônia | 6.1 |
| 8b19b166-9e95-3b4b-89be-249cdc59b524 | -15.54447 | -55.01043 | 2025-08-23 04:53:00 | NOAA-21 | CAMPO VERDE | MATO GROSSO | Brasil | 5102678 | 51 | 33 | nan | nan | nan | Cerrado | 2.2 |
| d794f07f-c77a-3589-882a-bc61936de140 | -14.37325 | -53.14715 | 2025-08-23 04:53:00 | NOAA-21 | CAMPINÁPOLIS | MATO GROSSO | Brasil | 5102603 | 51 | 33 | nan | nan | nan | Cerrado | 2.3 |
| a9ac6bb2-df73-35e6-bbaa-80e0af5e3771 | -13.83337 | -55.95894 | 2025-08-23 04:53:00 | NOAA-21 | NOVA MUTUM | MATO GROSSO | Brasil | 5106224 | 51 | 33 | nan | nan | nan | Cerrado | 2.0 |
| 44c74365-e061-3be7-b15b-0e647f628796 | -15.54878 | -51.70121 | 2025-08-23 04:53:00 | NOAA-21 | MONTES CLAROS DE GOIÁS | GOIÁS | Brasil | 5213707 | 52 | 33 | nan | nan | nan | Cerrado | 2.7 |
| 4ac5cfa9-5cac-3a04-a302-b4ae7004d013 | -14.63467 | -59.55555 | 2025-08-23 04:53:00 | NOAA-21 | CONQUISTA D'OESTE | MATO GROSSO | Brasil | 5103361 | 51 | 33 | nan | nan | nan | Amazônia | 0.8 |
| 15d458c7-628b-33da-abeb-a3c80623c8d0 | -14.2849 | -60.38438 | 2025-08-23 04:53:00 | NOAA-21 | VILA BELA DA SANTÍSSIMA TRINDADE | MATO GROSSO | Brasil | 5105507 | 51 | 33 | nan | nan | nan | Amazônia | 3.1 |
| 2093a7be-91d5-3612-9e6b-ec7dd718069b | -14.86664 | -59.60897 | 2025-08-23 04:53:00 | NOAA-21 | VILA BELA DA SANTÍSSIMA TRINDADE | MATO GROSSO | Brasil | 5105507 | 51 | 33 | nan | nan | nan | Amazônia | 1.6 |
| 6b8567b0-75ee-3c5c-97d0-51fdcddfb832 | -12.99699 | -45.22589 | 2025-08-23 04:53:00 | NOAA-21 | SÃO DESIDÉRIO | BAHIA | Brasil | 2928901 | 29 | 33 | nan | nan | nan | Cerrado | 13.3 |
| 9a57f741-292f-3207-9129-18f66308a5e6 | -14.46509 | -55.93384 | 2025-08-23 04:53:00 | NOAA-21 | NOBRES | MATO GROSSO | Brasil | 5105903 | 51 | 33 | nan | nan | nan | Cerrado | 1.2 |
| f40a6e49-b3ea-3c63-b097-3b7d4c2001cd | -14.7597 | -56.04787 | 2025-08-23 04:53:00 | NOAA-21 | ROSÁRIO OESTE | MATO GROSSO | Brasil | 5107701 | 51 | 33 | nan | nan | nan | Cerrado | 2.2 |
| 7977b67f-dbc9-3cde-83a6-18900b1d59ea | -13.4903 | -47.03365 | 2025-08-23 04:53:00 | NOAA-21 | MONTE ALEGRE DE GOIÁS | GOIÁS | Brasil | 5213509 | 52 | 33 | nan | nan | nan | Cerrado | 2.7 |
| b7e32e68-ea36-3822-9104-14f6bc87f5a4 | -13.3609 | -54.40303 | 2025-08-23 04:53:00 | NOAA-21 | PARANATINGA | MATO GROSSO | Brasil | 5106307 | 51 | 33 | nan | nan | nan | Amazônia | 1.1 |
| 2c07730d-2e61-3463-8db5-f420adcfa3d8 | -15.01583 | -54.86811 | 2025-08-23 04:53:00 | NOAA-21 | NOVA BRASILÂNDIA | MATO GROSSO | Brasil | 5106208 | 51 | 33 | nan | nan | nan | Cerrado | 1.8 |
| f88e0cc2-f664-33d5-b9a2-25407749fd42 | -12.99096 | -45.23172 | 2025-08-23 04:53:00 | NOAA-21 | SÃO DESIDÉRIO | BAHIA | Brasil | 2928901 | 29 | 33 | nan | nan | nan | Cerrado | 9.6 |
| ac3da177-c4c8-3894-be5a-ab7955a18c83 | -15.61678 | -57.33171 | 2025-08-23 04:53:00 | NOAA-21 | PORTO ESTRELA | MATO GROSSO | Brasil | 5106851 | 51 | 33 | nan | nan | nan | Cerrado | 3.0 |
| 58d1c993-f3a5-31b4-8865-8b2f811f1517 | -14.94465 | -48.0041 | 2025-08-23 04:53:00 | NOAA-21 | ÁGUA FRIA DE GOIÁS | GOIÁS | Brasil | 5200175 | 52 | 33 | nan | nan | nan | Cerrado | 2.1 |
| f384fd83-815e-3976-bb39-4e021f94c53f | -16.32657 | -46.76917 | 2025-08-23 04:53:00 | NOAA-21 | UNAÍ | MINAS GERAIS | Brasil | 3170404 | 31 | 33 | nan | nan | nan | Cerrado | 2.4 |
| 53b7e1df-bb8e-3fec-aac5-547c25795037 | -13.13138 | -57.1148 | 2025-08-23 04:53:00 | NOAA-21 | NOVA MARINGÁ | MATO GROSSO | Brasil | 5108907 | 51 | 33 | nan | nan | nan | Amazônia | 2.2 |
| 4e2326e5-55aa-39e5-bc4f-de4409c9861d | -14.82497 | -47.95731 | 2025-08-23 04:53:00 | NOAA-21 | ÁGUA FRIA DE GOIÁS | GOIÁS | Brasil | 5200175 | 52 | 33 | nan | nan | nan | Cerrado | 4.3 |
| 8559f8b5-b187-3b52-9af8-59e233495481 | -11.28374 | -52.75626 | 2025-08-23 04:53:00 | NOAA-21 | SÃO FÉLIX DO ARAGUAIA | MATO GROSSO | Brasil | 5107859 | 51 | 33 | nan | nan | nan | Amazônia | 0.6 |
| ab25ba31-f305-30fc-b959-ff4f4c0a726f | -15.34198 | -49.75632 | 2025-08-23 04:53:00 | NOAA-21 | CARMO DO RIO VERDE | GOIÁS | Brasil | 5205000 | 52 | 33 | nan | nan | nan | Cerrado | 1.6 |
| 6520ba8b-e210-3301-94fe-b8c6a56a6193 | -14.67394 | -56.61663 | 2025-08-23 04:53:00 | NOAA-21 | ALTO PARAGUAI | MATO GROSSO | Brasil | 5100508 | 51 | 33 | nan | nan | nan | Cerrado | 4.4 |
| f25db7b7-f7a8-305c-bbc8-4203faba0c64 | -15.56817 | -55.01072 | 2025-08-23 04:53:00 | NOAA-21 | CAMPO VERDE | MATO GROSSO | Brasil | 5102678 | 51 | 33 | nan | nan | nan | Cerrado | 2.8 |
| c899cdae-52fc-3551-bcb2-e0cf50d9299b | -16.33087 | -46.77569 | 2025-08-23 04:53:00 | NOAA-21 | UNAÍ | MINAS GERAIS | Brasil | 3170404 | 31 | 33 | nan | nan | nan | Cerrado | 7.9 |
| b681e4e1-ec7b-3d89-9e9e-7e9499b33933 | -14.79757 | -45.42861 | 2025-08-23 04:53:00 | NOAA-21 | COCOS | BAHIA | Brasil | 2908101 | 29 | 33 | nan | nan | nan | Cerrado | 1.4 |
| 886a2c69-e5ee-3c75-9d10-67b6d86bfd19 | -14.75709 | -55.40674 | 2025-08-23 04:53:00 | NOAA-21 | NOVA BRASILÂNDIA | MATO GROSSO | Brasil | 5106208 | 51 | 33 | nan | nan | nan | Cerrado | 1.8 |
| dbb1a602-bc44-35dd-9b84-694892a0095a | -14.47397 | -55.94292 | 2025-08-23 04:53:00 | NOAA-21 | NOBRES | MATO GROSSO | Brasil | 5105903 | 51 | 33 | nan | nan | nan | Cerrado | 1.2 |
| 43be53bc-4cf3-370d-8c6d-522d2245a8e6 | -11.11119 | -62.66689 | 2025-08-23 04:53:00 | NOAA-21 | MIRANTE DA SERRA | RONDÔNIA | Brasil | 1101302 | 11 | 33 | nan | nan | nan | Amazônia | 1.8 |
| 667df0e5-d608-36a6-a89b-bea7924b0438 | -9.95733 | -60.17456 | 2025-08-23 04:53:00 | NOAA-21 | ARIPUANÃ | MATO GROSSO | Brasil | 5101407 | 51 | 33 | nan | nan | nan | Amazônia | 16.0 |
| 5a6d9512-0505-3290-abcb-7bd8f1baf1a9 | -13.12862 | -46.89473 | 2025-08-23 04:53:00 | NOAA-21 | MONTE ALEGRE DE GOIÁS | GOIÁS | Brasil | 5213509 | 52 | 33 | nan | nan | nan | Cerrado | 3.5 |
| c45d712f-e038-373f-b556-d1e4e4d096ba | -15.72307 | -48.21589 | 2025-08-23 04:53:00 | NOAA-21 | ÁGUAS LINDAS DE GOIÁS | GOIÁS | Brasil | 5200258 | 52 | 33 | nan | nan | nan | Cerrado | 1.1 |
| 5b4dd843-3409-3d6e-ac9d-d1a4236743ea | -14.27926 | -58.55355 | 2025-08-23 04:53:00 | NOAA-21 | TANGARÁ DA SERRA | MATO GROSSO | Brasil | 5107958 | 51 | 33 | nan | nan | nan | Cerrado | 1.2 |
| 62a18fd0-8e95-3162-9b16-81f87d5aa133 | -13.03698 | -56.83559 | 2025-08-23 04:53:00 | NOAA-21 | NOVA MARINGÁ | MATO GROSSO | Brasil | 5108907 | 51 | 33 | nan | nan | nan | Amazônia | 1.3 |
| 176eeda8-c91f-349b-b81a-588688d34148 | -15.03122 | -54.89981 | 2025-08-23 04:53:00 | NOAA-21 | NOVA BRASILÂNDIA | MATO GROSSO | Brasil | 5106208 | 51 | 33 | nan | nan | nan | Cerrado | 4.8 |
| 12d034a8-d2e0-3d99-8be6-84de724533c4 | -14.29155 | -58.52743 | 2025-08-23 04:53:00 | NOAA-21 | TANGARÁ DA SERRA | MATO GROSSO | Brasil | 5107958 | 51 | 33 | nan | nan | nan | Cerrado | 2.3 |
| 2fd6fbdd-8a3b-3fa5-8aa1-dd248a70ef1b | -9.50392 | -60.5114 | 2025-08-23 04:53:00 | NOAA-21 | ARIPUANÃ | MATO GROSSO | Brasil | 5101407 | 51 | 33 | nan | nan | nan | Amazônia | 1.3 |
| 30f76a04-44d1-3f66-b547-241fff58328e | -13.34491 | -54.39681 | 2025-08-23 04:53:00 | NOAA-21 | PARANATINGA | MATO GROSSO | Brasil | 5106307 | 51 | 33 | nan | nan | nan | Amazônia | 0.9 |
| 189d474f-e42a-3f36-8272-dd957ab35d95 | -11.32172 | -55.22722 | 2025-08-23 04:53:00 | NOAA-21 | CLÁUDIA | MATO GROSSO | Brasil | 5103056 | 51 | 33 | nan | nan | nan | Amazônia | 1.7 |
| 33800512-3d31-3685-902c-664068288a1f | -14.96674 | -48.66974 | 2025-08-23 04:53:00 | NOAA-21 | NIQUELÂNDIA | GOIÁS | Brasil | 5214606 | 52 | 33 | nan | nan | nan | Cerrado | 1.3 |
| be1a409f-afd1-3bbc-95e9-43e7cf924d3b | -14.61192 | -54.79773 | 2025-08-23 04:53:00 | NOAA-21 | PLANALTO DA SERRA | MATO GROSSO | Brasil | 5106455 | 51 | 33 | nan | nan | nan | Cerrado | 2.7 |
| d5af1dea-9b5f-3d48-867a-ef53f505f967 | -9.94972 | -60.19131 | 2025-08-23 04:53:00 | NOAA-21 | ARIPUANÃ | MATO GROSSO | Brasil | 5101407 | 51 | 33 | nan | nan | nan | Amazônia | 7.8 |
| 97eb3cab-85f7-3e83-994a-a0d470a549fb | -14.26757 | -58.53244 | 2025-08-23 04:53:00 | NOAA-21 | TANGARÁ DA SERRA | MATO GROSSO | Brasil | 5107958 | 51 | 33 | nan | nan | nan | Cerrado | 7.7 |
| 1825e834-8099-3925-b2d1-2f92ec0aa0c2 | -13.37082 | -54.40465 | 2025-08-23 04:53:00 | NOAA-21 | PARANATINGA | MATO GROSSO | Brasil | 5106307 | 51 | 33 | nan | nan | nan | Amazônia | 1.1 |
| 9b8043e9-f396-3a71-b537-624f02600d07 | -11.19425 | -55.04306 | 2025-08-23 04:53:00 | NOAA-21 | ITAÚBA | MATO GROSSO | Brasil | 5104559 | 51 | 33 | nan | nan | nan | Amazônia | 1.0 |
| e3c54e05-b3ff-361d-b727-b7d29ce0fdeb | -15.02958 | -54.8886 | 2025-08-23 04:53:00 | NOAA-21 | NOVA BRASILÂNDIA | MATO GROSSO | Brasil | 5106208 | 51 | 33 | nan | nan | nan | Cerrado | 7.4 |
| 52916561-7443-3036-bcf9-57b6f363720a | -13.0292 | -56.83102 | 2025-08-23 04:53:00 | NOAA-21 | NOVA MARINGÁ | MATO GROSSO | Brasil | 5108907 | 51 | 33 | nan | nan | nan | Amazônia | 1.2 |
| e34b23d1-5696-3fa5-8445-ef336f8b26bf | -14.6771 | -56.59739 | 2025-08-23 04:53:00 | NOAA-21 | ALTO PARAGUAI | MATO GROSSO | Brasil | 5100508 | 51 | 33 | nan | nan | nan | Cerrado | 0.8 |
| 16e714c6-687e-3c6c-8083-7925969db126 | -15.0544 | -56.39489 | 2025-08-23 04:53:00 | NOAA-21 | ROSÁRIO OESTE | MATO GROSSO | Brasil | 5107701 | 51 | 33 | nan | nan | nan | Cerrado | 5.6 |
| 0aa3f4fa-5587-3486-8dd8-ad09cab3dfa6 | -14.64922 | -54.90588 | 2025-08-23 04:53:00 | NOAA-21 | PLANALTO DA SERRA | MATO GROSSO | Brasil | 5106455 | 51 | 33 | nan | nan | nan | Cerrado | 1.1 |
| aabb0962-6820-3b04-b15d-aa2e6f46bd47 | -15.54777 | -55.01098 | 2025-08-23 04:53:00 | NOAA-21 | CAMPO VERDE | MATO GROSSO | Brasil | 5102678 | 51 | 33 | nan | nan | nan | Cerrado | 2.2 |
| a3183ab7-8473-3eb7-b80c-38fe40c5b965 | -10.41179 | -57.68337 | 2025-08-23 04:53:00 | NOAA-21 | JUARA | MATO GROSSO | Brasil | 5105101 | 51 | 33 | nan | nan | nan | Amazônia | 2.5 |
| 0b6cbe36-d9fe-34ea-812a-8067c9bc8117 | -15.07727 | -48.51049 | 2025-08-23 04:53:00 | NOAA-21 | MIMOSO DE GOIÁS | GOIÁS | Brasil | 5213053 | 52 | 33 | nan | nan | nan | Cerrado | 6.6 |
| 039e0788-a2e6-30ad-99d2-dd5cb7fd0910 | -11.19148 | -55.03891 | 2025-08-23 04:53:00 | NOAA-21 | ITAÚBA | MATO GROSSO | Brasil | 5104559 | 51 | 33 | nan | nan | nan | Amazônia | 1.0 |
| de9ea05e-87f1-367d-9b19-40b23fde57e9 | -9.84749 | -64.29057 | 2025-08-23 04:53:00 | NOAA-21 | BURITIS | RONDÔNIA | Brasil | 1100452 | 11 | 33 | nan | nan | nan | Amazônia | 1.9 |
| 9f38168f-d42f-37aa-8b61-6c75eae53e07 | -11.19264 | -55.03172 | 2025-08-23 04:53:00 | NOAA-21 | ITAÚBA | MATO GROSSO | Brasil | 5104559 | 51 | 33 | nan | nan | nan | Amazônia | 2.0 |
| 5c8cab34-0fbc-3c63-84ac-347ce38af038 | -9.84037 | -64.2924 | 2025-08-23 04:53:00 | NOAA-21 | BURITIS | RONDÔNIA | Brasil | 1100452 | 11 | 33 | nan | nan | nan | Amazônia | 1.2 |
| c9402bf5-8f1b-3203-a0b1-f4a57b729b09 | -13.47083 | -47.03676 | 2025-08-23 04:53:00 | NOAA-21 | MONTE ALEGRE DE GOIÁS | GOIÁS | Brasil | 5213509 | 52 | 33 | nan | nan | nan | Cerrado | 3.6 |
| e4f3ec0e-36ab-3c96-99d3-f374c2184b3a | -14.66384 | -54.92265 | 2025-08-23 04:53:00 | NOAA-21 | NOVA BRASILÂNDIA | MATO GROSSO | Brasil | 5106208 | 51 | 33 | nan | nan | nan | Cerrado | 1.4 |
| d4cbc8bf-79ab-39b8-8372-04a68a09bd7b | -14.67927 | -56.60555 | 2025-08-23 04:53:00 | NOAA-21 | ALTO PARAGUAI | MATO GROSSO | Brasil | 5100508 | 51 | 33 | nan | nan | nan | Cerrado | 2.0 |
| 26061fca-76d2-3335-b630-77485e1d804c | -14.3746 | -52.05008 | 2025-08-23 04:53:00 | NOAA-21 | NOVA NAZARÉ | MATO GROSSO | Brasil | 5106174 | 51 | 33 | nan | nan | nan | Cerrado | 8.3 |
| fc6149a2-de9f-3c0c-9809-c66ddbf8783b | -12.79598 | -48.72117 | 2025-08-23 04:53:00 | NOAA-21 | JAÚ DO TOCANTINS | TOCANTINS | Brasil | 1711506 | 17 | 33 | nan | nan | nan | Cerrado | 3.7 |
| d337061c-874e-3743-a4c3-701c437ee1ac | -14.67432 | -56.59294 | 2025-08-23 04:53:00 | NOAA-21 | ALTO PARAGUAI | MATO GROSSO | Brasil | 5100508 | 51 | 33 | nan | nan | nan | Cerrado | 1.7 |
| 9bdb2a0f-14a7-35f7-a11c-8a85876e7297 | -15.22245 | -53.8609 | 2025-08-23 04:53:00 | NOAA-21 | NOVO SÃO JOAQUIM | MATO GROSSO | Brasil | 5106281 | 51 | 33 | nan | nan | nan | Cerrado | 2.3 |
| 6c3db3a9-f8a8-33c6-a784-27e0dc8289fc | -13.3642 | -54.40357 | 2025-08-23 04:53:00 | NOAA-21 | PARANATINGA | MATO GROSSO | Brasil | 5106307 | 51 | 33 | nan | nan | nan | Amazônia | 1.1 |
| 57dae4ab-8cb2-38ca-b08d-b5242a08b7b0 | -13.4532 | -50.67561 | 2025-08-23 04:53:00 | NOAA-21 | NOVA CRIXÁS | GOIÁS | Brasil | 5214838 | 52 | 33 | nan | nan | nan | Cerrado | 1.8 |
| 24bb9eea-0969-399c-968b-365c214f2533 | -14.67046 | -54.92375 | 2025-08-23 04:53:00 | NOAA-21 | NOVA BRASILÂNDIA | MATO GROSSO | Brasil | 5106208 | 51 | 33 | nan | nan | nan | Cerrado | 8.0 |
| 0fa0bf49-91bf-3077-9513-a37b401276c0 | -14.46786 | -55.93809 | 2025-08-23 04:53:00 | NOAA-21 | NOBRES | MATO GROSSO | Brasil | 5105903 | 51 | 33 | nan | nan | nan | Cerrado | 1.2 |
| 3f48c7a3-d647-34bb-885c-5584729b746a | -14.6699 | -54.9273 | 2025-08-23 04:53:00 | NOAA-21 | NOVA BRASILÂNDIA | MATO GROSSO | Brasil | 5106208 | 51 | 33 | nan | nan | nan | Cerrado | 5.3 |
| 0dab8745-6472-38e4-86d4-f8b93970b60e | -14.57288 | -54.50337 | 2025-08-23 04:53:00 | NOAA-21 | PLANALTO DA SERRA | MATO GROSSO | Brasil | 5106455 | 51 | 33 | nan | nan | nan | Cerrado | 1.4 |
| 9a6f04cb-0ded-3813-abfd-07f40112e558 | -15.05189 | -48.4667 | 2025-08-23 04:53:00 | NOAA-21 | MIMOSO DE GOIÁS | GOIÁS | Brasil | 5213053 | 52 | 33 | nan | nan | nan | Cerrado | 1.5 |
| ec445f94-e713-3f13-b79d-8117f0773463 | -14.77722 | -59.65892 | 2025-08-23 04:53:00 | NOAA-21 | NOVA LACERDA | MATO GROSSO | Brasil | 5106182 | 51 | 33 | nan | nan | nan | Amazônia | 1.1 |
| 405b5be5-c52a-304f-ad37-db35cdc791fa | -8.68891 | -62.86435 | 2025-08-23 04:53:00 | NOAA-21 | CANDEIAS DO JAMARI | RONDÔNIA | Brasil | 1100809 | 11 | 33 | nan | nan | nan | Amazônia | 2.6 |
| 45c42212-a054-3915-81e4-5649c5a2230c | -9.9578 | -60.19733 | 2025-08-23 04:53:00 | NOAA-21 | ARIPUANÃ | MATO GROSSO | Brasil | 5101407 | 51 | 33 | nan | nan | nan | Amazônia | 222.7 |
| ac381818-ecf8-3a06-a423-abf0412f8fa7 | -10.46613 | -59.1385 | 2025-08-23 04:53:00 | NOAA-21 | ARIPUANÃ | MATO GROSSO | Brasil | 5101407 | 51 | 33 | nan | nan | nan | Amazônia | 1.2 |
| 2ad1bddd-c7ff-3e91-9fff-83d691560d7d | -9.21855 | -60.78532 | 2025-08-23 04:53:00 | NOAA-21 | COLNIZA | MATO GROSSO | Brasil | 5103254 | 51 | 33 | nan | nan | nan | Amazônia | 2.0 |
| bd92728a-7c63-30c5-b5ab-3a257a348325 | -14.2713 | -58.53312 | 2025-08-23 04:53:00 | NOAA-21 | TANGARÁ DA SERRA | MATO GROSSO | Brasil | 5107958 | 51 | 33 | nan | nan | nan | Cerrado | 7.7 |
| 31d55ee2-3a19-3ea8-9e9f-28b20713bbd8 | -15.65076 | -52.68063 | 2025-08-23 04:53:00 | NOAA-21 | BARRA DO GARÇAS | MATO GROSSO | Brasil | 5101803 | 51 | 33 | nan | nan | nan | Cerrado | 2.9 |
| 110a50d9-b844-3c49-bf1e-044c658c4a7e | -14.75913 | -55.98748 | 2025-08-23 04:53:00 | NOAA-21 | ROSÁRIO OESTE | MATO GROSSO | Brasil | 5107701 | 51 | 33 | nan | nan | nan | Cerrado | 1.9 |
| 4c397aba-4418-3797-a498-cbe5c262210e | -13.03312 | -56.87978 | 2025-08-23 04:53:00 | NOAA-21 | NOVA MARINGÁ | MATO GROSSO | Brasil | 5108907 | 51 | 33 | nan | nan | nan | Amazônia | 0.8 |
| 19c9b184-4168-39ab-b27b-7dc255d0d8b0 | -12.78093 | -48.70744 | 2025-08-23 04:53:00 | NOAA-21 | JAÚ DO TOCANTINS | TOCANTINS | Brasil | 1711506 | 17 | 33 | nan | nan | nan | Cerrado | 11.6 |
| b8685fba-4c42-36ff-b05f-e03f129a7464 | -17.27287 | -46.76483 | 2025-08-23 04:53:00 | NOAA-21 | PARACATU | MINAS GERAIS | Brasil | 3147006 | 31 | 33 | nan | nan | nan | Cerrado | 1.5 |
| 6e64ac6c-12ca-3672-8939-763ce5454e80 | -15.01914 | -54.86866 | 2025-08-23 04:53:00 | NOAA-21 | NOVA BRASILÂNDIA | MATO GROSSO | Brasil | 5106208 | 51 | 33 | nan | nan | nan | Cerrado | 1.8 |
| bd43a456-ecec-39d1-aea7-355f72171481 | -14.6514 | -54.91354 | 2025-08-23 04:53:00 | NOAA-21 | NOVA BRASILÂNDIA | MATO GROSSO | Brasil | 5106208 | 51 | 33 | nan | nan | nan | Cerrado | 1.6 |
| 0ad73f73-01fd-353a-871b-155daa048c1f | -9.52716 | -60.54003 | 2025-08-23 04:53:00 | NOAA-21 | ARIPUANÃ | MATO GROSSO | Brasil | 5101407 | 51 | 33 | nan | nan | nan | Amazônia | 1.6 |
| ae673a56-3c7e-3d62-8c86-f8d5be96c6df | -12.48772 | -53.80938 | 2025-08-23 04:53:00 | NOAA-21 | PARANATINGA | MATO GROSSO | Brasil | 5106307 | 51 | 33 | nan | nan | nan | Amazônia | 0.9 |
| 64162b58-de67-32fb-93cc-9aa56bf90e38 | -9.5092 | -60.56146 | 2025-08-23 04:53:00 | NOAA-21 | ARIPUANÃ | MATO GROSSO | Brasil | 5101407 | 51 | 33 | nan | nan | nan | Amazônia | 2.1 |
| 8989ab59-146d-3c87-906c-696bef250aeb | -14.67989 | -56.60176 | 2025-08-23 04:53:00 | NOAA-21 | ALTO PARAGUAI | MATO GROSSO | Brasil | 5100508 | 51 | 33 | nan | nan | nan | Cerrado | 0.8 |


[Clique aqui para ver as próximas entradas](README48.md)
