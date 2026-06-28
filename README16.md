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

## Dados Diários - Página 16

| ID | Latitude | Longitude | Data/Hora GMT | Satélite | Município | Estado | País | Município ID | Estado ID | País ID | Dias sem Chuva | Precipitação | Risco de Fogo | Bioma | FRP |
|----|----------|-----------|---------------|----------|-----------|--------|------|--------------|-----------|---------|----------------|--------------|----------------|-------|-----|
| c9fd9592-68c2-3461-a911-7a804e4c098f | -9.59128 | -56.92277 | 2026-06-28 04:59:00 | NOAA-21 | PARANAÍTA | MATO GROSSO | Brasil | 5106299 | 51 | 33 | nan | nan | nan | Amazônia | 2.0 |
| 8ff093e9-34ec-3261-b1ca-b2eb5033920e | -11.31341 | -53.94714 | 2026-06-28 04:59:00 | NOAA-21 | UNIÃO DO SUL | MATO GROSSO | Brasil | 5108303 | 51 | 33 | nan | nan | nan | Amazônia | 0.8 |
| 92d04dde-ca7f-351e-ba19-ecf236a0e000 | -10.84025 | -49.1302 | 2026-06-28 04:59:00 | NOAA-21 | SANTA RITA DO TOCANTINS | TOCANTINS | Brasil | 1718899 | 17 | 33 | nan | nan | nan | Cerrado | 1.1 |
| b9cbbb70-2c08-33d8-840e-7733295d73c0 | -11.9426 | -58.61309 | 2026-06-28 04:59:00 | NOAA-21 | JUÍNA | MATO GROSSO | Brasil | 5105150 | 51 | 33 | nan | nan | nan | Cerrado | 1.1 |
| 21769e7f-10a8-32b7-bd7d-4f2d694fa627 | -10.83228 | -49.12485 | 2026-06-28 04:59:00 | NOAA-21 | SANTA RITA DO TOCANTINS | TOCANTINS | Brasil | 1718899 | 17 | 33 | nan | nan | nan | Cerrado | 1.8 |
| 8ffbdcfd-e254-3fc6-a6e1-f985b5cc098b | -12.19598 | -52.88526 | 2026-06-28 04:59:00 | NOAA-21 | QUERÊNCIA | MATO GROSSO | Brasil | 5107065 | 51 | 33 | nan | nan | nan | Amazônia | 2.2 |
| 9acc6544-de3d-3f8a-8ac2-5597dfb043f7 | -11.31934 | -54.46589 | 2026-06-28 04:59:00 | NOAA-21 | MARCELÂNDIA | MATO GROSSO | Brasil | 5105580 | 51 | 33 | nan | nan | nan | Amazônia | 0.9 |
| 50c28782-7fc7-3f8d-91f0-42a0477531ec | -12.17491 | -57.13603 | 2026-06-28 04:59:00 | NOAA-21 | NOVA MARINGÁ | MATO GROSSO | Brasil | 5108907 | 51 | 33 | nan | nan | nan | Amazônia | 0.9 |
| ced48524-716b-3008-8450-df5cacd1ae45 | -9.09248 | -59.40724 | 2026-06-28 04:59:00 | NOAA-21 | COLNIZA | MATO GROSSO | Brasil | 5103254 | 51 | 33 | nan | nan | nan | Amazônia | 6.0 |
| 0e64f182-6653-3f37-bd60-98a458ae3de3 | -9.03145 | -61.33735 | 2026-06-28 04:59:00 | NOAA-21 | COLNIZA | MATO GROSSO | Brasil | 5103254 | 51 | 33 | nan | nan | nan | Amazônia | 1.3 |
| 1782b204-09eb-3d62-8d96-cb6d8f22c747 | -9.08732 | -59.4146 | 2026-06-28 04:59:00 | NOAA-21 | COLNIZA | MATO GROSSO | Brasil | 5103254 | 51 | 33 | nan | nan | nan | Amazônia | 7.0 |
| 30e504cd-a8a7-3502-86b2-f968fb08bf5a | -12.08818 | -52.01119 | 2026-06-28 04:59:00 | NOAA-21 | BOM JESUS DO ARAGUAIA | MATO GROSSO | Brasil | 5101852 | 51 | 33 | nan | nan | nan | Amazônia | 3.3 |
| 283f7678-1487-331b-8655-ce4269542419 | -12.16933 | -57.12746 | 2026-06-28 04:59:00 | NOAA-21 | NOVA MARINGÁ | MATO GROSSO | Brasil | 5108907 | 51 | 33 | nan | nan | nan | Amazônia | 2.6 |
| bc19a31f-732a-33c3-90ec-4f976666c2d7 | -9.09334 | -59.40221 | 2026-06-28 04:59:00 | NOAA-21 | COLNIZA | MATO GROSSO | Brasil | 5103254 | 51 | 33 | nan | nan | nan | Amazônia | 2.4 |
| fd8faec8-cf67-3bfc-bf61-c7db002e038b | -12.59584 | -57.87769 | 2026-06-28 04:59:00 | NOAA-21 | BRASNORTE | MATO GROSSO | Brasil | 5101902 | 51 | 33 | nan | nan | nan | Cerrado | 8.1 |
| f442c78d-daae-3feb-b566-d1653b6547b3 | -12.16255 | -57.12636 | 2026-06-28 04:59:00 | NOAA-21 | NOVA MARINGÁ | MATO GROSSO | Brasil | 5108907 | 51 | 33 | nan | nan | nan | Amazônia | 1.8 |
| 4bcda988-cc74-363d-b411-accf14040a6e | -12.09482 | -52.01652 | 2026-06-28 04:59:00 | NOAA-21 | BOM JESUS DO ARAGUAIA | MATO GROSSO | Brasil | 5101852 | 51 | 33 | nan | nan | nan | Amazônia | 4.8 |
| ad09277b-8328-3676-adb4-d9de25313995 | -12.0833 | -52.01919 | 2026-06-28 04:59:00 | NOAA-21 | BOM JESUS DO ARAGUAIA | MATO GROSSO | Brasil | 5101852 | 51 | 33 | nan | nan | nan | Amazônia | 3.4 |
| 7aee58e8-a3da-319a-8a45-4f2e8a9f0dd5 | -11.91103 | -57.11893 | 2026-06-28 04:59:00 | NOAA-21 | PORTO DOS GAÚCHOS | MATO GROSSO | Brasil | 5106802 | 51 | 33 | nan | nan | nan | Amazônia | 1.4 |
| 14e00934-4d36-30c8-bf46-7010248ea39d | -10.80746 | -56.61681 | 2026-06-28 04:59:00 | NOAA-21 | TABAPORÃ | MATO GROSSO | Brasil | 5107941 | 51 | 33 | nan | nan | nan | Amazônia | 1.3 |
| 7fd7f476-3297-39ca-916a-90392c3b676c | -12.15856 | -57.12952 | 2026-06-28 04:59:00 | NOAA-21 | NOVA MARINGÁ | MATO GROSSO | Brasil | 5108907 | 51 | 33 | nan | nan | nan | Amazônia | 0.7 |
| b6ff273f-4be3-3235-af9f-44a54b960a65 | -12.61614 | -57.87624 | 2026-06-28 04:59:00 | NOAA-21 | BRASNORTE | MATO GROSSO | Brasil | 5101902 | 51 | 33 | nan | nan | nan | Cerrado | 0.8 |
| 37a470aa-c1b3-3312-9c78-b3591fdce441 | -10.39202 | -56.77126 | 2026-06-28 04:59:00 | NOAA-21 | ALTA FLORESTA | MATO GROSSO | Brasil | 5100250 | 51 | 33 | nan | nan | nan | Amazônia | 0.7 |
| 686ccbb8-d3e7-3aa0-a257-84edaddfe1f6 | -12.20119 | -52.87392 | 2026-06-28 04:59:00 | NOAA-21 | QUERÊNCIA | MATO GROSSO | Brasil | 5107065 | 51 | 33 | nan | nan | nan | Amazônia | 9.3 |
| e1b40350-df85-36b0-9197-5837b932fdcf | -11.31676 | -53.94766 | 2026-06-28 04:59:00 | NOAA-21 | UNIÃO DO SUL | MATO GROSSO | Brasil | 5108303 | 51 | 33 | nan | nan | nan | Amazônia | 0.8 |
| 08031225-30a5-3f5e-b476-507a6e4d529a | -11.92048 | -57.40614 | 2026-06-28 04:59:00 | NOAA-21 | NOVA MARINGÁ | MATO GROSSO | Brasil | 5108907 | 51 | 33 | nan | nan | nan | Amazônia | 1.3 |
| 5be923e5-9971-36cf-a8e5-c02ea0d6ab3c | -11.20867 | -54.30038 | 2026-06-28 04:59:00 | NOAA-21 | MARCELÂNDIA | MATO GROSSO | Brasil | 5105580 | 51 | 33 | nan | nan | nan | Amazônia | 3.4 |
| 8daf8ebb-9cc5-3688-b521-791cce0bd488 | -12.18738 | -52.90921 | 2026-06-28 04:59:00 | NOAA-21 | QUERÊNCIA | MATO GROSSO | Brasil | 5107065 | 51 | 33 | nan | nan | nan | Amazônia | 4.2 |
| fc13e798-8864-347c-a162-e2d305ee3995 | -11.91964 | -58.65406 | 2026-06-28 04:59:00 | NOAA-21 | JUÍNA | MATO GROSSO | Brasil | 5105150 | 51 | 33 | nan | nan | nan | Cerrado | 1.3 |
| aa40f70d-1105-3102-b32a-9c5780669a87 | -10.30394 | -57.12268 | 2026-06-28 04:59:00 | NOAA-21 | NOVA MONTE VERDE | MATO GROSSO | Brasil | 5108956 | 51 | 33 | nan | nan | nan | Amazônia | 12.8 |
| 874108b1-4be0-31fb-9d42-f58cc735cd69 | -12.1937 | -52.90105 | 2026-06-28 04:59:00 | NOAA-21 | QUERÊNCIA | MATO GROSSO | Brasil | 5107065 | 51 | 33 | nan | nan | nan | Amazônia | 2.9 |
| 94e1f598-689b-3172-af3b-53a76917f8f7 | -12.188 | -52.88108 | 2026-06-28 04:59:00 | NOAA-21 | QUERÊNCIA | MATO GROSSO | Brasil | 5107065 | 51 | 33 | nan | nan | nan | Amazônia | 3.7 |
| 04f62bf9-8da8-30b7-9032-d29734e8c1e6 | -14.04488 | -46.33498 | 2026-06-28 04:59:00 | NOAA-21 | POSSE | GOIÁS | Brasil | 5218300 | 52 | 33 | nan | nan | nan | Cerrado | 0.5 |
| 3a42a908-d030-3862-a86c-bf1b0d9753b8 | -12.5952 | -57.8816 | 2026-06-28 04:59:00 | NOAA-21 | BRASNORTE | MATO GROSSO | Brasil | 5101902 | 51 | 33 | nan | nan | nan | Cerrado | 8.1 |
| 75be4c85-abc2-3ae4-b65d-a4863c7bccca | -12.16972 | -57.14663 | 2026-06-28 04:59:00 | NOAA-21 | NOVA MARINGÁ | MATO GROSSO | Brasil | 5108907 | 51 | 33 | nan | nan | nan | Amazônia | 0.8 |
| 2bb48121-5484-35ae-8856-6311905fdee6 | -11.21616 | -53.82525 | 2026-06-28 04:59:00 | NOAA-21 | MARCELÂNDIA | MATO GROSSO | Brasil | 5105580 | 51 | 33 | nan | nan | nan | Amazônia | 11.4 |
| a6bdf74f-8811-3b9e-b49d-6c6c036b4e06 | -12.19827 | -52.86942 | 2026-06-28 04:59:00 | NOAA-21 | QUERÊNCIA | MATO GROSSO | Brasil | 5107065 | 51 | 33 | nan | nan | nan | Amazônia | 9.3 |
| 19222013-5b5c-3a82-959e-d1f7fcfc282b | -10.53777 | -53.70932 | 2026-06-28 04:59:00 | NOAA-21 | MARCELÂNDIA | MATO GROSSO | Brasil | 5105580 | 51 | 33 | nan | nan | nan | Amazônia | 1.3 |
| 53b55d5c-c017-3cfa-9f48-f0fa0c4da948 | -11.91893 | -58.65831 | 2026-06-28 04:59:00 | NOAA-21 | JUÍNA | MATO GROSSO | Brasil | 5105150 | 51 | 33 | nan | nan | nan | Cerrado | 1.3 |
| 5c84325f-e7b9-3b04-95e8-23bbff9c78c2 | -15.16642 | -49.82698 | 2026-06-28 04:59:00 | NOAA-21 | RUBIATABA | GOIÁS | Brasil | 5218904 | 52 | 33 | nan | nan | nan | Cerrado | 0.7 |
| 34e3efb7-4d62-38f7-8dc3-383aaef7926f | -12.20296 | -52.88634 | 2026-06-28 04:59:00 | NOAA-21 | QUERÊNCIA | MATO GROSSO | Brasil | 5107065 | 51 | 33 | nan | nan | nan | Amazônia | 2.8 |
| fa183773-807d-392c-8e48-ad63117738cd | -12.16693 | -57.14235 | 2026-06-28 04:59:00 | NOAA-21 | NOVA MARINGÁ | MATO GROSSO | Brasil | 5108907 | 51 | 33 | nan | nan | nan | Amazônia | 0.8 |
| 229695e4-5951-3a55-af37-e8a2877ebff6 | -9.03066 | -61.34188 | 2026-06-28 04:59:00 | NOAA-21 | COLNIZA | MATO GROSSO | Brasil | 5103254 | 51 | 33 | nan | nan | nan | Amazônia | 1.2 |
| 5824f195-2e1f-3744-9ce7-ea5e0970e4d3 | -11.2128 | -53.82472 | 2026-06-28 04:59:00 | NOAA-21 | MARCELÂNDIA | MATO GROSSO | Brasil | 5105580 | 51 | 33 | nan | nan | nan | Amazônia | 2.7 |
| 8880e138-b00a-3d7f-bad5-76f6c23bbb75 | -11.51543 | -56.1278 | 2026-06-28 04:59:00 | NOAA-21 | TABAPORÃ | MATO GROSSO | Brasil | 5107941 | 51 | 33 | nan | nan | nan | Amazônia | 0.8 |
| 6a78e935-b230-3fb7-ba64-8c9bd1a5f7e4 | -12.19947 | -52.8858 | 2026-06-28 04:59:00 | NOAA-21 | QUERÊNCIA | MATO GROSSO | Brasil | 5107065 | 51 | 33 | nan | nan | nan | Amazônia | 2.2 |
| f5ee01d4-4e5a-3e16-92af-f698a5caf28d | -10.81141 | -56.6137 | 2026-06-28 04:59:00 | NOAA-21 | TABAPORÃ | MATO GROSSO | Brasil | 5107941 | 51 | 33 | nan | nan | nan | Amazônia | 1.3 |
| 97bd67aa-d788-32b0-a2cd-961923c688ac | -12.61071 | -57.88737 | 2026-06-28 04:59:00 | NOAA-21 | BRASNORTE | MATO GROSSO | Brasil | 5101902 | 51 | 33 | nan | nan | nan | Cerrado | 3.5 |
| 8064ffd7-9e9c-3bec-bc4e-5794548c42b8 | -12.18647 | -57.15675 | 2026-06-28 04:59:00 | NOAA-21 | NOVA MARINGÁ | MATO GROSSO | Brasil | 5108907 | 51 | 33 | nan | nan | nan | Amazônia | 1.3 |
| a7be91b6-d3ef-3d94-af51-23dbd28476db | -11.92474 | -58.66818 | 2026-06-28 04:59:00 | NOAA-21 | JUÍNA | MATO GROSSO | Brasil | 5105150 | 51 | 33 | nan | nan | nan | Cerrado | 3.2 |
| 82261c93-a026-311d-b545-043a5c2f68f5 | -11.93028 | -58.66344 | 2026-06-28 04:59:00 | NOAA-21 | JUÍNA | MATO GROSSO | Brasil | 5105150 | 51 | 33 | nan | nan | nan | Cerrado | 0.8 |
| f1792ea8-b4da-344c-85ca-c5e94991a84d | -12.19078 | -52.89657 | 2026-06-28 04:59:00 | NOAA-21 | QUERÊNCIA | MATO GROSSO | Brasil | 5107065 | 51 | 33 | nan | nan | nan | Amazônia | 2.2 |
| 8a343269-b5ac-3e0a-8cab-aace5526d293 | -12.79238 | -54.8809 | 2026-06-28 04:59:00 | NOAA-21 | NOVA UBIRATÃ | MATO GROSSO | Brasil | 5106240 | 51 | 33 | nan | nan | nan | Amazônia | 3.9 |
| 4bf4a934-b0de-31b5-b62c-becfa0619755 | -12.16135 | -57.13379 | 2026-06-28 04:59:00 | NOAA-21 | NOVA MARINGÁ | MATO GROSSO | Brasil | 5108907 | 51 | 33 | nan | nan | nan | Amazônia | 1.8 |
| 8ef51541-963e-3e66-9436-5c9e41ef42e5 | -10.8408 | -49.12616 | 2026-06-28 04:59:00 | NOAA-21 | SANTA RITA DO TOCANTINS | TOCANTINS | Brasil | 1718899 | 17 | 33 | nan | nan | nan | Cerrado | 1.1 |
| 33ac0b83-77f1-3baf-bfca-cc9da5a33b26 | -12.26777 | -43.52217 | 2026-06-28 04:59:00 | NOAA-21 | MUQUÉM DO SÃO FRANCISCO | BAHIA | Brasil | 2922250 | 29 | 33 | nan | nan | nan | Cerrado | 2.0 |
| 3f580f76-46ed-3981-8495-b90ec64f921d | -12.23398 | -56.55345 | 2026-06-28 04:59:00 | NOAA-21 | ITANHANGÁ | MATO GROSSO | Brasil | 5104542 | 51 | 33 | nan | nan | nan | Amazônia | 2.1 |
| 978c9c52-f740-3e11-b6a3-bcb2a872dc05 | -10.78563 | -54.11016 | 2026-06-28 04:59:00 | NOAA-21 | MARCELÂNDIA | MATO GROSSO | Brasil | 5105580 | 51 | 33 | nan | nan | nan | Amazônia | 0.6 |
| 8665c0ab-b87b-362d-87ec-bc133a4d2444 | -12.23122 | -56.54931 | 2026-06-28 04:59:00 | NOAA-21 | ITANHANGÁ | MATO GROSSO | Brasil | 5104542 | 51 | 33 | nan | nan | nan | Amazônia | 3.5 |
| eba6ce77-1b4f-36d0-8e63-72683235ac0f | -11.9239 | -57.40673 | 2026-06-28 04:59:00 | NOAA-21 | NOVA MARINGÁ | MATO GROSSO | Brasil | 5108907 | 51 | 33 | nan | nan | nan | Amazônia | 1.3 |
| 2ee08707-9e0a-323c-b3e3-6f3dba63112d | -11.56454 | -54.57358 | 2026-06-28 04:59:00 | NOAA-21 | UNIÃO DO SUL | MATO GROSSO | Brasil | 5108303 | 51 | 33 | nan | nan | nan | Amazônia | 1.1 |
| d86b01c2-df12-3677-b620-b498dbdf9e24 | -12.16753 | -57.13864 | 2026-06-28 04:59:00 | NOAA-21 | NOVA MARINGÁ | MATO GROSSO | Brasil | 5108907 | 51 | 33 | nan | nan | nan | Amazônia | 1.3 |
| af358c1c-7f41-3f20-b446-607bba9a693a | -13.28957 | -43.54889 | 2026-06-28 04:59:00 | NOAA-21 | SERRA DO RAMALHO | BAHIA | Brasil | 2930154 | 29 | 33 | nan | nan | nan | Cerrado | 1.6 |
| d7d2ce36-ef25-3cd8-9ca3-e6e9db64483a | -12.18859 | -52.87713 | 2026-06-28 04:59:00 | NOAA-21 | QUERÊNCIA | MATO GROSSO | Brasil | 5107065 | 51 | 33 | nan | nan | nan | Amazônia | 3.7 |
| 9e73913b-5da1-3fb7-9d6a-a180b34bfa21 | -9.09028 | -59.39655 | 2026-06-28 04:59:00 | NOAA-21 | COLNIZA | MATO GROSSO | Brasil | 5103254 | 51 | 33 | nan | nan | nan | Amazônia | 1.8 |
| 4543ca3a-8748-3557-a9bb-16f593ce18d2 | -12.17332 | -57.12431 | 2026-06-28 04:59:00 | NOAA-21 | NOVA MARINGÁ | MATO GROSSO | Brasil | 5108907 | 51 | 33 | nan | nan | nan | Amazônia | 1.9 |
| 32f17e45-d69a-37e3-aab0-57f98213e97d | -12.1989 | -52.88975 | 2026-06-28 04:59:00 | NOAA-21 | QUERÊNCIA | MATO GROSSO | Brasil | 5107065 | 51 | 33 | nan | nan | nan | Amazônia | 2.2 |
| 44b654fe-fcc6-34a0-8957-9a0df24c9abd | -11.21868 | -54.30165 | 2026-06-28 04:59:00 | NOAA-21 | MARCELÂNDIA | MATO GROSSO | Brasil | 5105580 | 51 | 33 | nan | nan | nan | Amazônia | 6.1 |
| e1dce7f4-97bc-3dfc-9396-188964929aee | -11.91363 | -57.40499 | 2026-06-28 04:59:00 | NOAA-21 | NOVA MARINGÁ | MATO GROSSO | Brasil | 5108907 | 51 | 33 | nan | nan | nan | Amazônia | 1.3 |
| d44d06fb-e0dc-3bcc-bfab-59c7ce9f805b | -9.03512 | -61.34267 | 2026-06-28 04:59:00 | NOAA-21 | COLNIZA | MATO GROSSO | Brasil | 5103254 | 51 | 33 | nan | nan | nan | Amazônia | 1.6 |
| 1f6758e0-d14f-3407-ba71-f2f5233b38b5 | -9.09209 | -59.41019 | 2026-06-28 04:59:00 | NOAA-21 | COLNIZA | MATO GROSSO | Brasil | 5103254 | 51 | 33 | nan | nan | nan | Amazônia | 7.0 |
| 43b227d8-7c32-3719-9eb2-9917b831a5a7 | -12.32003 | -46.74026 | 2026-06-28 04:59:00 | NOAA-21 | TAGUATINGA | TOCANTINS | Brasil | 1720903 | 17 | 33 | nan | nan | nan | Cerrado | 1.2 |
| 2c41f84d-3723-3f4e-b3a2-db2e5378f120 | -12.59867 | -57.88219 | 2026-06-28 04:59:00 | NOAA-21 | BRASNORTE | MATO GROSSO | Brasil | 5101902 | 51 | 33 | nan | nan | nan | Cerrado | 6.6 |
| d1fcdfbe-7927-3d53-9bdc-ace2507d93d8 | -11.66377 | -57.25559 | 2026-06-28 04:59:00 | NOAA-21 | PORTO DOS GAÚCHOS | MATO GROSSO | Brasil | 5106802 | 51 | 33 | nan | nan | nan | Amazônia | 1.5 |
| 1f21a804-97cb-3069-93ee-6372c340d105 | -12.2041 | -52.87843 | 2026-06-28 04:59:00 | NOAA-21 | QUERÊNCIA | MATO GROSSO | Brasil | 5107065 | 51 | 33 | nan | nan | nan | Amazônia | 4.4 |
| fe576630-c7bc-3721-8df7-78b335d6231f | -12.19427 | -52.89711 | 2026-06-28 04:59:00 | NOAA-21 | QUERÊNCIA | MATO GROSSO | Brasil | 5107065 | 51 | 33 | nan | nan | nan | Amazônia | 3.1 |
| 9e8ee06f-634a-3f5d-ba33-eda895b5cd92 | -11.30952 | -53.95022 | 2026-06-28 04:59:00 | NOAA-21 | UNIÃO DO SUL | MATO GROSSO | Brasil | 5108303 | 51 | 33 | nan | nan | nan | Amazônia | 1.1 |
| 54b74d78-20c0-318d-8d00-01f8e8b9c987 | -12.44847 | -58.48472 | 2026-06-28 04:59:00 | NOAA-21 | SAPEZAL | MATO GROSSO | Brasil | 5107875 | 51 | 33 | nan | nan | nan | Cerrado | 11.9 |
| 5f290922-7a04-3550-ba84-4986dd833772 | -11.72165 | -59.35283 | 2026-06-28 04:59:00 | NOAA-21 | JUÍNA | MATO GROSSO | Brasil | 5105150 | 51 | 33 | nan | nan | nan | Cerrado | 2.6 |
| 0df9a293-7779-3116-a54c-4d58139e5830 | -11.91262 | -57.13063 | 2026-06-28 04:59:00 | NOAA-21 | PORTO DOS GAÚCHOS | MATO GROSSO | Brasil | 5106802 | 51 | 33 | nan | nan | nan | Amazônia | 0.8 |
| 48bceefb-ded5-3249-bd24-26f6bcf933f4 | -12.18914 | -52.89741 | 2026-06-28 04:59:00 | NOAA-21 | QUERÊNCIA | MATO GROSSO | Brasil | 5107065 | 51 | 33 | nan | nan | nan | Amazônia | 2.4 |
| 93974346-6654-3a57-857f-f160007cb7b7 | -12.27642 | -50.10411 | 2026-06-28 04:59:00 | NOAA-21 | SANDOLÂNDIA | TOCANTINS | Brasil | 1718840 | 17 | 33 | nan | nan | nan | Cerrado | 3.2 |
| d0d1f270-1c75-3e17-9ff0-4f6647791efa | -11.564 | -54.5771 | 2026-06-28 04:59:00 | NOAA-21 | UNIÃO DO SUL | MATO GROSSO | Brasil | 5108303 | 51 | 33 | nan | nan | nan | Amazônia | 1.1 |
| c4d1d380-5295-3946-af70-fdd40e61341d | -11.60583 | -43.11567 | 2026-06-28 04:59:00 | NOAA-21 | MORPARÁ | BAHIA | Brasil | 2921609 | 29 | 33 | nan | nan | nan | Caatinga | 5.5 |
| 23bbc56b-d922-32b7-8fd4-5f8e6f197fa5 | -12.19478 | -52.86887 | 2026-06-28 04:59:00 | NOAA-21 | QUERÊNCIA | MATO GROSSO | Brasil | 5107065 | 51 | 33 | nan | nan | nan | Amazônia | 6.3 |
| 1886f9c5-c171-3ee5-ba27-bef06c288e19 | -11.92615 | -58.65965 | 2026-06-28 04:59:00 | NOAA-21 | JUÍNA | MATO GROSSO | Brasil | 5105150 | 51 | 33 | nan | nan | nan | Cerrado | 1.5 |
| 687a7a45-d218-3f60-8f75-2922fb714a7e | -10.05846 | -59.10989 | 2026-06-28 04:59:00 | NOAA-21 | ARIPUANÃ | MATO GROSSO | Brasil | 5101407 | 51 | 33 | nan | nan | nan | Amazônia | 1.3 |
| c6ffc1a2-d4aa-3d8b-8c78-f878fca6e98c | -12.20239 | -52.89029 | 2026-06-28 04:59:00 | NOAA-21 | QUERÊNCIA | MATO GROSSO | Brasil | 5107065 | 51 | 33 | nan | nan | nan | Amazônia | 2.8 |
| 489f626c-096b-3820-bc27-bade2dc7016a | -12.1805 | -57.14457 | 2026-06-28 04:59:00 | NOAA-21 | NOVA MARINGÁ | MATO GROSSO | Brasil | 5108907 | 51 | 33 | nan | nan | nan | Amazônia | 1.3 |
| 0c6ccde0-ccd3-33f9-95f5-cd8ba1d817a0 | -12.08055 | -54.60114 | 2026-06-28 04:59:00 | NOAA-21 | FELIZ NATAL | MATO GROSSO | Brasil | 5103700 | 51 | 33 | nan | nan | nan | Amazônia | 1.0 |
| d0d5a10d-7f87-3f81-87fa-1f34132051dc | -11.3232 | -54.46288 | 2026-06-28 04:59:00 | NOAA-21 | MARCELÂNDIA | MATO GROSSO | Brasil | 5105580 | 51 | 33 | nan | nan | nan | Amazônia | 1.1 |
| 34bdd252-70b0-3979-8466-e1322581caa9 | -11.90922 | -57.13006 | 2026-06-28 04:59:00 | NOAA-21 | PORTO DOS GAÚCHOS | MATO GROSSO | Brasil | 5106802 | 51 | 33 | nan | nan | nan | Amazônia | 0.8 |
| 44c83986-dddd-363c-8a98-ae186dd1e44b | -11.9148 | -57.13867 | 2026-06-28 04:59:00 | NOAA-21 | PORTO DOS GAÚCHOS | MATO GROSSO | Brasil | 5106802 | 51 | 33 | nan | nan | nan | Amazônia | 0.7 |
| 0a43307f-7975-39ed-80a3-9bc3ee2dddb6 | -12.19208 | -52.87767 | 2026-06-28 04:59:00 | NOAA-21 | QUERÊNCIA | MATO GROSSO | Brasil | 5107065 | 51 | 33 | nan | nan | nan | Amazônia | 3.7 |
| 5257a463-b006-363e-82db-8a80a1ed31bf | -11.21814 | -54.30521 | 2026-06-28 04:59:00 | NOAA-21 | MARCELÂNDIA | MATO GROSSO | Brasil | 5105580 | 51 | 33 | nan | nan | nan | Amazônia | 6.1 |
| 212b41c8-e4ac-37f2-9fc8-8cf0efc388be | -12.16534 | -57.13063 | 2026-06-28 04:59:00 | NOAA-21 | NOVA MARINGÁ | MATO GROSSO | Brasil | 5108907 | 51 | 33 | nan | nan | nan | Amazônia | 1.8 |
| 581c7353-0739-3b8c-a508-64cdd2f5432b | -12.09506 | -52.01993 | 2026-06-28 04:59:00 | NOAA-21 | BOM JESUS DO ARAGUAIA | MATO GROSSO | Brasil | 5101852 | 51 | 33 | nan | nan | nan | Amazônia | 3.4 |
| 800a7274-2e6c-3103-b287-c42c0c0754ba | -9.08768 | -59.41161 | 2026-06-28 04:59:00 | NOAA-21 | COLNIZA | MATO GROSSO | Brasil | 5103254 | 51 | 33 | nan | nan | nan | Amazônia | 6.1 |
| 652ed074-afca-345b-be41-95f7fdcb92df | -12.18925 | -57.16103 | 2026-06-28 04:59:00 | NOAA-21 | NOVA MARINGÁ | MATO GROSSO | Brasil | 5108907 | 51 | 33 | nan | nan | nan | Amazônia | 0.9 |
| d6e1bc29-3211-3e53-8cd3-c15b5ee7048d | -12.58592 | -57.80796 | 2026-06-28 04:59:00 | NOAA-21 | BRASNORTE | MATO GROSSO | Brasil | 5101902 | 51 | 33 | nan | nan | nan | Amazônia | 2.0 |


[Clique aqui para ver as próximas entradas](README17.md)
