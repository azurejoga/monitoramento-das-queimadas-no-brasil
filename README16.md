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
| 06b4d4a2-8c0f-386f-a551-b2b008e3e0ec | -7.12918 | -60.12584 | 2025-08-13 04:40:00 | NOAA-21 | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 8.9 |
| 240e0ecb-914c-3672-a908-83ef0a4fa931 | -8.11237 | -55.57233 | 2025-08-13 04:40:00 | NOAA-21 | NOVO PROGRESSO | PARÁ | Brasil | 1505031 | 15 | 33 | nan | nan | nan | Amazônia | 2.7 |
| ace3a797-3c71-3312-8892-963b9c78a0d7 | -6.90027 | -59.13271 | 2025-08-13 04:40:00 | NOAA-21 | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 18.5 |
| 5ca1b971-7009-386f-9317-3a835a750bf9 | -8.11302 | -55.56849 | 2025-08-13 04:40:00 | NOAA-21 | NOVO PROGRESSO | PARÁ | Brasil | 1505031 | 15 | 33 | nan | nan | nan | Amazônia | 1.4 |
| 6bc3a996-67d8-3cb8-807a-a88ef36f2571 | -12.55175 | -46.97369 | 2025-08-13 04:40:00 | NOAA-21 | ARRAIAS | TOCANTINS | Brasil | 1702406 | 17 | 33 | nan | nan | nan | Cerrado | 1.0 |
| 4d9a9b1b-ea64-3257-b57c-88547c4ae83f | -12.53112 | -46.98206 | 2025-08-13 04:40:00 | NOAA-21 | ARRAIAS | TOCANTINS | Brasil | 1702406 | 17 | 33 | nan | nan | nan | Cerrado | 8.8 |
| bd882243-747e-361d-9098-949a20d5ff86 | -6.89902 | -59.13969 | 2025-08-13 04:40:00 | NOAA-21 | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 50.6 |
| 7e89ba14-a214-3546-81ac-3ff2535d822f | -13.11133 | -46.86504 | 2025-08-13 04:40:00 | NOAA-21 | MONTE ALEGRE DE GOIÁS | GOIÁS | Brasil | 5213509 | 52 | 33 | nan | nan | nan | Cerrado | 4.6 |
| c7dd900c-aeac-3b01-b000-84d7dfcf62b8 | -6.90629 | -59.13013 | 2025-08-13 04:40:00 | NOAA-21 | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 9.7 |
| adf03397-d872-303b-949a-c1b6d4f568e7 | -6.54981 | -44.01271 | 2025-08-13 04:40:00 | NOAA-21 | PASTOS BONS | MARANHÃO | Brasil | 2108009 | 21 | 33 | nan | nan | nan | Cerrado | 1.9 |
| 01b1065a-602b-355b-8813-bb69d0629f36 | -8.10885 | -55.56785 | 2025-08-13 04:40:00 | NOAA-21 | NOVO PROGRESSO | PARÁ | Brasil | 1505031 | 15 | 33 | nan | nan | nan | Amazônia | 23.5 |
| 404e083c-15bd-39c7-9b4d-6aafd64de9ea | -5.84269 | -59.92167 | 2025-08-13 04:40:00 | NOAA-21 | NOVO ARIPUANÃ | AMAZONAS | Brasil | 1303304 | 13 | 33 | nan | nan | nan | Amazônia | 1.4 |
| 830e3fdd-d2ce-38bf-9c35-cdeed416d5aa | -12.30558 | -50.01653 | 2025-08-13 04:40:00 | NOAA-21 | SANDOLÂNDIA | TOCANTINS | Brasil | 1718840 | 17 | 33 | nan | nan | nan | Cerrado | 1.8 |
| 2a3ff46d-a0db-3242-83a7-bee8a7feaf50 | -9.84527 | -47.81867 | 2025-08-13 04:40:00 | NOAA-21 | RIO SONO | TOCANTINS | Brasil | 1718758 | 17 | 33 | nan | nan | nan | Cerrado | 4.9 |
| 3c692298-7485-3f0c-86fa-da6b3e203338 | -7.07533 | -44.936 | 2025-08-13 04:40:00 | NOAA-21 | SÃO FÉLIX DE BALSAS | MARANHÃO | Brasil | 2110807 | 21 | 33 | nan | nan | nan | Cerrado | 4.6 |
| a0ae7fd1-3722-3746-936b-57054774e2c0 | -6.0926 | -59.93092 | 2025-08-13 04:40:00 | NOAA-21 | NOVO ARIPUANÃ | AMAZONAS | Brasil | 1303304 | 13 | 33 | nan | nan | nan | Amazônia | 4.0 |
| 32ddad82-c2fe-3e06-b65c-350d149c093a | -8.1178 | -55.56543 | 2025-08-13 04:40:00 | NOAA-21 | NOVO PROGRESSO | PARÁ | Brasil | 1505031 | 15 | 33 | nan | nan | nan | Amazônia | 1.4 |
| f1e9e4bb-1b8d-3a7b-9b52-6f5a616f8c9a | -9.06334 | -60.64809 | 2025-08-13 04:40:00 | NOAA-21 | COLNIZA | MATO GROSSO | Brasil | 5103254 | 51 | 33 | nan | nan | nan | Amazônia | 7.5 |
| 6a9a0bd3-4a1e-3923-a0ab-683df5ff9c87 | -10.34314 | -50.81361 | 2025-08-13 04:40:00 | NOAA-21 | SANTA TEREZINHA | MATO GROSSO | Brasil | 5107776 | 51 | 33 | nan | nan | nan | Cerrado | 1.6 |
| fe5585b2-fd1f-3d54-bd76-2019d18ade49 | -9.37038 | -47.62915 | 2025-08-13 04:40:00 | NOAA-21 | RIO SONO | TOCANTINS | Brasil | 1718758 | 17 | 33 | nan | nan | nan | Cerrado | 0.7 |
| 3593341a-943b-37f3-b0ff-f90f6400f677 | -12.51048 | -46.96465 | 2025-08-13 04:40:00 | NOAA-21 | ARRAIAS | TOCANTINS | Brasil | 1702406 | 17 | 33 | nan | nan | nan | Cerrado | 6.3 |
| 8003ed3c-8d22-382c-aea9-5bde674c7043 | -13.10751 | -46.86442 | 2025-08-13 04:40:00 | NOAA-21 | MONTE ALEGRE DE GOIÁS | GOIÁS | Brasil | 5213509 | 52 | 33 | nan | nan | nan | Cerrado | 0.7 |
| a8d1dbf8-70bc-3413-90f6-29991f95b8f5 | -9.47507 | -57.84187 | 2025-08-13 04:40:00 | NOAA-21 | APIACÁS | MATO GROSSO | Brasil | 5100805 | 51 | 33 | nan | nan | nan | Amazônia | 1.1 |
| 2392c5fd-dab9-3e6d-963d-e96b64651a10 | -6.89841 | -59.14309 | 2025-08-13 04:40:00 | NOAA-21 | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 50.6 |
| 712bd494-0ff1-3554-94fd-fa2b612622ec | -6.07277 | -59.9381 | 2025-08-13 04:40:00 | NOAA-21 | NOVO ARIPUANÃ | AMAZONAS | Brasil | 1303304 | 13 | 33 | nan | nan | nan | Amazônia | 2.7 |
| 486bdae9-42fd-30eb-842f-5a1375571b62 | -7.0748 | -59.20876 | 2025-08-13 04:40:00 | NOAA-21 | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 2.4 |
| 24e29252-95e8-3c24-ada4-fc9d70c27001 | -6.88102 | -59.14701 | 2025-08-13 04:40:00 | NOAA-21 | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 32.4 |
| 78e93a6f-fcce-385e-a2f7-afe5b7605103 | -12.32716 | -46.05129 | 2025-08-13 04:40:00 | NOAA-21 | LUÍS EDUARDO MAGALHÃES | BAHIA | Brasil | 2919553 | 29 | 33 | nan | nan | nan | Cerrado | 4.1 |
| 8537af4f-e75d-3234-a35c-374efe00062e | -7.45665 | -60.6322 | 2025-08-13 04:40:00 | NOAA-21 | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 3.4 |
| c3b33a20-b69e-3424-9d17-c90d1ff64a0f | -5.85459 | -52.11139 | 2025-08-13 04:40:00 | NOAA-21 | SÃO FÉLIX DO XINGU | PARÁ | Brasil | 1507300 | 15 | 33 | nan | nan | nan | Amazônia | 6.3 |
| 8c0953d8-196b-31ee-ac7a-adf439c1a1b6 | -12.58504 | -46.98394 | 2025-08-13 04:40:00 | NOAA-21 | ARRAIAS | TOCANTINS | Brasil | 1702406 | 17 | 33 | nan | nan | nan | Cerrado | 3.4 |
| bd533329-6a09-30e6-ad1f-31287a5a6415 | -6.90691 | -59.12663 | 2025-08-13 04:40:00 | NOAA-21 | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 9.7 |
| b66a4a4c-30d6-36dd-9691-9b5fa9b0157f | -6.88163 | -59.1436 | 2025-08-13 04:40:00 | NOAA-21 | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 32.4 |
| 53f31986-c7a0-3319-a47a-cd53de967522 | -10.96297 | -49.57552 | 2025-08-13 04:40:00 | NOAA-21 | SANTA RITA DO TOCANTINS | TOCANTINS | Brasil | 1718899 | 17 | 33 | nan | nan | nan | Cerrado | 7.5 |
| 0669d12c-8db3-3bfc-885c-e7fa8c0d0127 | -7.07136 | -44.93533 | 2025-08-13 04:40:00 | NOAA-21 | SÃO FÉLIX DE BALSAS | MARANHÃO | Brasil | 2110807 | 21 | 33 | nan | nan | nan | Cerrado | 2.5 |
| fa45edae-f9ed-3e29-8d04-ef87a51a1510 | -12.57747 | -46.98288 | 2025-08-13 04:40:00 | NOAA-21 | ARRAIAS | TOCANTINS | Brasil | 1702406 | 17 | 33 | nan | nan | nan | Cerrado | 7.2 |
| 57036999-2dbd-3e9f-be48-ba7d952b1b4c | -6.07395 | -59.93557 | 2025-08-13 04:40:00 | NOAA-21 | NOVO ARIPUANÃ | AMAZONAS | Brasil | 1303304 | 13 | 33 | nan | nan | nan | Amazônia | 1.5 |
| 85af22e1-efa7-3fd4-8fe9-8c512965b0a2 | -6.09838 | -59.93179 | 2025-08-13 04:40:00 | NOAA-21 | NOVO ARIPUANÃ | AMAZONAS | Brasil | 1303304 | 13 | 33 | nan | nan | nan | Amazônia | 4.0 |
| 3e0a2454-5464-3dbe-9c0c-d1c72b185eff | -6.86968 | -59.13572 | 2025-08-13 04:40:00 | NOAA-21 | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 7.6 |
| aefaadc7-ebdd-3eb1-804b-fb4c18c070bc | -12.55552 | -46.97427 | 2025-08-13 04:40:00 | NOAA-21 | ARRAIAS | TOCANTINS | Brasil | 1702406 | 17 | 33 | nan | nan | nan | Cerrado | 1.0 |
| e3963ef4-a0b2-3827-919a-5942f8bd22f0 | -6.88224 | -59.14021 | 2025-08-13 04:40:00 | NOAA-21 | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 23.2 |
| 041f78c9-d6c7-309b-aa80-9824afbd1600 | -6.88762 | -59.14121 | 2025-08-13 04:40:00 | NOAA-21 | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 23.2 |
| 70e7e923-0add-3551-9ad5-0ec371f87635 | -12.48405 | -46.96056 | 2025-08-13 04:40:00 | NOAA-21 | ARRAIAS | TOCANTINS | Brasil | 1702406 | 17 | 33 | nan | nan | nan | Cerrado | 3.4 |
| 685945d6-e7aa-301e-980c-37fdb5ca348e | -11.7177 | -51.60758 | 2025-08-13 04:40:00 | NOAA-21 | ALTO BOA VISTA | MATO GROSSO | Brasil | 5100359 | 51 | 33 | nan | nan | nan | Cerrado | 2.7 |
| 340a5b54-9a13-3c48-83c7-3ad7a5ffd5b7 | -8.57793 | -54.71321 | 2025-08-13 04:40:00 | NOAA-21 | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 1.2 |
| 30c63612-fdf8-3b9f-b649-74845e91f55d | -6.90566 | -59.13366 | 2025-08-13 04:40:00 | NOAA-21 | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 19.9 |
| b7d5d7dd-f8e0-36e2-90a0-c4036c9488e1 | -7.11973 | -59.8423 | 2025-08-13 04:40:00 | NOAA-21 | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 1.1 |
| 40cd2486-aa48-39f7-b0af-de8aca526aba | -10.34645 | -50.81414 | 2025-08-13 04:40:00 | NOAA-21 | SANTA TEREZINHA | MATO GROSSO | Brasil | 5107776 | 51 | 33 | nan | nan | nan | Cerrado | 1.6 |
| fad8457a-d538-399d-8709-6512dbaad741 | -9.05674 | -60.6584 | 2025-08-13 04:40:00 | NOAA-21 | COLNIZA | MATO GROSSO | Brasil | 5103254 | 51 | 33 | nan | nan | nan | Amazônia | 3.9 |
| 6b41cd5e-c9bf-3a81-aeaa-19a6c69ad922 | -10.75614 | -48.78257 | 2025-08-13 04:40:00 | NOAA-21 | FÁTIMA | TOCANTINS | Brasil | 1707553 | 17 | 33 | nan | nan | nan | Cerrado | 1.4 |
| 76bc30ca-9284-30a5-9290-be8c961009aa | -10.34976 | -50.81467 | 2025-08-13 04:40:00 | NOAA-21 | SANTA TEREZINHA | MATO GROSSO | Brasil | 5107776 | 51 | 33 | nan | nan | nan | Cerrado | 1.4 |
| ebda5417-9951-3412-94de-e80920018686 | -11.6933 | -51.61091 | 2025-08-13 04:40:00 | NOAA-21 | SÃO FÉLIX DO ARAGUAIA | MATO GROSSO | Brasil | 5107859 | 51 | 33 | nan | nan | nan | Amazônia | 1.2 |
| 2515aa7f-3cee-3c3d-ba38-c9b771045f49 | -12.47961 | -46.96465 | 2025-08-13 04:40:00 | NOAA-21 | ARRAIAS | TOCANTINS | Brasil | 1702406 | 17 | 33 | nan | nan | nan | Cerrado | 2.8 |
| 6d5a165b-ecab-38ab-9926-2a27705b017c | -12.67717 | -46.96117 | 2025-08-13 04:40:00 | NOAA-21 | ARRAIAS | TOCANTINS | Brasil | 1702406 | 17 | 33 | nan | nan | nan | Cerrado | 1.4 |
| 8bd72114-acea-3183-91c5-e82e9d5d5e71 | -11.71714 | -51.61113 | 2025-08-13 04:40:00 | NOAA-21 | ALTO BOA VISTA | MATO GROSSO | Brasil | 5100359 | 51 | 33 | nan | nan | nan | Cerrado | 2.7 |
| 76d2004a-ff92-3035-bed5-01f56aeefd1e | -10.34667 | -57.59806 | 2025-08-13 04:40:00 | NOAA-21 | JUARA | MATO GROSSO | Brasil | 5105101 | 51 | 33 | nan | nan | nan | Amazônia | 1.0 |
| 62076e33-37ba-3569-b6df-9d60e72692f0 | -7.12991 | -60.12183 | 2025-08-13 04:40:00 | NOAA-21 | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 8.9 |
| 99c9064d-8d54-350d-9b68-38dafc334ade | -9.06246 | -60.65953 | 2025-08-13 04:40:00 | NOAA-21 | COLNIZA | MATO GROSSO | Brasil | 5103254 | 51 | 33 | nan | nan | nan | Amazônia | 4.8 |
| fd7bf3c2-b050-3d11-a6c7-6c1010de98de | -12.48027 | -46.95999 | 2025-08-13 04:40:00 | NOAA-21 | ARRAIAS | TOCANTINS | Brasil | 1702406 | 17 | 33 | nan | nan | nan | Cerrado | 3.4 |
| 36972220-4ed8-3a69-913f-58bef6341b00 | -9.21255 | -59.647 | 2025-08-13 04:40:00 | NOAA-21 | COLNIZA | MATO GROSSO | Brasil | 5103254 | 51 | 33 | nan | nan | nan | Amazônia | 6.4 |
| ec5ef89f-edb4-3b04-bc94-0335708b32ff | -6.27798 | -53.63333 | 2025-08-13 04:40:00 | NOAA-21 | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 2.4 |
| 8fc443d5-bf75-3cd8-be12-ff6ff0b77315 | -10.97409 | -49.56994 | 2025-08-13 04:40:00 | NOAA-21 | SANTA RITA DO TOCANTINS | TOCANTINS | Brasil | 1718899 | 17 | 33 | nan | nan | nan | Cerrado | 3.2 |
| f4b75ac6-1138-3d92-8b02-c30e9c4c4568 | -11.68998 | -51.61037 | 2025-08-13 04:40:00 | NOAA-21 | SÃO FÉLIX DO ARAGUAIA | MATO GROSSO | Brasil | 5107859 | 51 | 33 | nan | nan | nan | Amazônia | 0.8 |
| 7417e1d3-957e-36e4-a857-72cf5336561c | -10.71539 | -48.84162 | 2025-08-13 04:40:00 | NOAA-21 | OLIVEIRA DE FÁTIMA | TOCANTINS | Brasil | 1715507 | 17 | 33 | nan | nan | nan | Cerrado | 0.6 |
| 0fce792c-8815-333b-8a5b-fd43bdc2ca20 | -11.76502 | -48.19006 | 2025-08-13 04:40:00 | NOAA-21 | SÃO VALÉRIO | TOCANTINS | Brasil | 1720499 | 17 | 33 | nan | nan | nan | Cerrado | 12.6 |
| ff902ff2-3777-3c65-9b38-79a46ae6ca8f | -9.05613 | -60.65505 | 2025-08-13 04:40:00 | NOAA-21 | COLNIZA | MATO GROSSO | Brasil | 5103254 | 51 | 33 | nan | nan | nan | Amazônia | 4.3 |
| 822c36fa-4fd0-3089-8c93-e77b2c977c26 | -10.23735 | -48.24575 | 2025-08-13 04:40:00 | NOAA-21 | PALMAS | TOCANTINS | Brasil | 1721000 | 17 | 33 | nan | nan | nan | Cerrado | 1.6 |
| 69f2d12c-b992-3084-995d-607f052edf22 | -9.18737 | -59.6633 | 2025-08-13 04:40:00 | NOAA-21 | COLNIZA | MATO GROSSO | Brasil | 5103254 | 51 | 33 | nan | nan | nan | Amazônia | 5.3 |
| f0672844-b470-3457-824b-99d747fde7b3 | -12.54861 | -46.96846 | 2025-08-13 04:40:00 | NOAA-21 | ARRAIAS | TOCANTINS | Brasil | 1702406 | 17 | 33 | nan | nan | nan | Cerrado | 1.1 |
| d6625cb3-670f-3a72-9b11-5d0139f3262f | -7.09843 | -60.02638 | 2025-08-13 04:40:00 | NOAA-21 | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 7.0 |
| 26adb2b9-d0e7-3380-9aac-483288288907 | -12.57991 | -46.99298 | 2025-08-13 04:40:00 | NOAA-21 | ARRAIAS | TOCANTINS | Brasil | 1702406 | 17 | 33 | nan | nan | nan | Cerrado | 2.1 |
| 1f1710aa-dee6-31a0-8d24-ffbc60067d48 | -7.45744 | -60.62778 | 2025-08-13 04:40:00 | NOAA-21 | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 3.1 |
| a36e9100-1e1d-3b7c-8a63-d6eee9d2353a | -6.8918 | -59.14897 | 2025-08-13 04:40:00 | NOAA-21 | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 35.6 |
| fba8829e-6e45-33cd-a929-a7f97f4d9f62 | -5.84776 | -59.92672 | 2025-08-13 04:40:00 | NOAA-21 | NOVO ARIPUANÃ | AMAZONAS | Brasil | 1303304 | 13 | 33 | nan | nan | nan | Amazônia | 2.1 |
| 821574a4-4d93-3c3f-9d85-659362eac83f | -7.06498 | -44.35981 | 2025-08-13 04:40:00 | NOAA-21 | BENEDITO LEITE | MARANHÃO | Brasil | 2101806 | 21 | 33 | nan | nan | nan | Cerrado | 2.2 |
| 5f3349a6-4512-32d0-aef7-787740da7df9 | -7.13995 | -60.13163 | 2025-08-13 04:40:00 | NOAA-21 | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 6.2 |
| 57cb92ce-82fe-34bd-8e60-6a3728c9efb6 | -9.37098 | -47.62515 | 2025-08-13 04:40:00 | NOAA-21 | RIO SONO | TOCANTINS | Brasil | 1718758 | 17 | 33 | nan | nan | nan | Cerrado | 0.7 |
| c66a54f0-e21d-3d88-90a6-9b99654357d9 | -12.58058 | -46.98825 | 2025-08-13 04:40:00 | NOAA-21 | ARRAIAS | TOCANTINS | Brasil | 1702406 | 17 | 33 | nan | nan | nan | Cerrado | 2.1 |
| 535052bb-dc32-3e90-9ef2-569e2b60445a | -9.9503 | -48.33641 | 2025-08-13 04:40:00 | NOAA-21 | PALMAS | TOCANTINS | Brasil | 1721000 | 17 | 33 | nan | nan | nan | Cerrado | 1.3 |
| d5cb8b9b-d673-3ba2-ac74-decde71da2f0 | -7.07412 | -59.20103 | 2025-08-13 04:40:00 | NOAA-21 | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 4.3 |
| 2686d56d-94d1-32e4-a511-3a94f18a8553 | -10.01859 | -58.42955 | 2025-08-13 04:40:00 | NOAA-21 | COTRIGUAÇU | MATO GROSSO | Brasil | 5103379 | 51 | 33 | nan | nan | nan | Amazônia | 3.2 |
| 9daf051a-3e92-33e5-b104-c68bb8cff901 | -6.87978 | -59.15387 | 2025-08-13 04:40:00 | NOAA-21 | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 21.3 |
| 51170f1b-5ebd-3183-8ebb-1dc79ccfa644 | -10.75955 | -48.78309 | 2025-08-13 04:40:00 | NOAA-21 | FÁTIMA | TOCANTINS | Brasil | 1707553 | 17 | 33 | nan | nan | nan | Cerrado | 1.4 |
| 63d14a68-496c-3384-b47e-2c3ec8eaeb2c | -7.07778 | -44.94686 | 2025-08-13 04:40:00 | NOAA-21 | SÃO FÉLIX DE BALSAS | MARANHÃO | Brasil | 2110807 | 21 | 33 | nan | nan | nan | Cerrado | 1.5 |
| 8ed84ba8-aa70-329a-95b7-375993d40bf0 | -12.49915 | -46.96288 | 2025-08-13 04:40:00 | NOAA-21 | ARRAIAS | TOCANTINS | Brasil | 1702406 | 17 | 33 | nan | nan | nan | Cerrado | 7.2 |
| f0ba8e16-46aa-306a-92b4-c495691f296b | -9.061 | -45.07724 | 2025-08-13 04:40:00 | NOAA-21 | BOM JESUS | PIAUÍ | Brasil | 2201903 | 22 | 33 | nan | nan | nan | Cerrado | 2.4 |
| 8dd0eb37-ebdd-3d9d-ae98-ddbdd2715af7 | -10.97021 | -49.573 | 2025-08-13 04:40:00 | NOAA-21 | SANTA RITA DO TOCANTINS | TOCANTINS | Brasil | 1718899 | 17 | 33 | nan | nan | nan | Cerrado | 4.0 |
| fbdd2ad7-29b2-323b-b216-667569886c05 | -10.9674 | -49.5689 | 2025-08-13 04:40:00 | NOAA-21 | SANTA RITA DO TOCANTINS | TOCANTINS | Brasil | 1718899 | 17 | 33 | nan | nan | nan | Cerrado | 2.2 |
| 358ce191-a28b-3f93-a665-6145d517cfbd | -8.11365 | -55.56472 | 2025-08-13 04:40:00 | NOAA-21 | NOVO PROGRESSO | PARÁ | Brasil | 1505031 | 15 | 33 | nan | nan | nan | Amazônia | 1.4 |
| 533d885c-c598-31cd-b0b4-5d6bfde66b66 | -11.68146 | -50.14391 | 2025-08-13 04:40:00 | NOAA-21 | FORMOSO DO ARAGUAIA | TOCANTINS | Brasil | 1708205 | 17 | 33 | nan | nan | nan | Cerrado | 0.7 |
| 5d61a9bb-2935-32b7-8876-76ebda83c747 | -6.8972 | -59.14991 | 2025-08-13 04:40:00 | NOAA-21 | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 35.6 |
| 297158c8-420c-3731-8ea0-bc61bb21f938 | -6.11067 | -59.9294 | 2025-08-13 04:40:00 | NOAA-21 | NOVO ARIPUANÃ | AMAZONAS | Brasil | 1303304 | 13 | 33 | nan | nan | nan | Amazônia | 2.6 |
| 6f809ac5-8516-34a4-82e8-beaf7f61ea8e | -7.13566 | -60.12274 | 2025-08-13 04:40:00 | NOAA-21 | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 6.2 |
| c0b7578a-ff92-3555-b883-4af9257174d1 | -7.25732 | -60.63374 | 2025-08-13 04:40:00 | NOAA-21 | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 5.5 |
| 20f25f90-b1a7-34be-b2bd-5d88d7db4af3 | -5.84339 | -59.91763 | 2025-08-13 04:40:00 | NOAA-21 | NOVO ARIPUANÃ | AMAZONAS | Brasil | 1303304 | 13 | 33 | nan | nan | nan | Amazônia | 1.4 |
| 8d1d56e2-7fa4-3bc2-9cb4-b44d95df45c9 | -5.85108 | -52.11081 | 2025-08-13 04:40:00 | NOAA-21 | SÃO FÉLIX DO XINGU | PARÁ | Brasil | 1507300 | 15 | 33 | nan | nan | nan | Amazônia | 6.3 |
| b7ed9f32-473a-302f-80dc-89368a6694d0 | -8.30689 | -55.10857 | 2025-08-13 04:40:00 | NOAA-21 | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 1.4 |
| 162f5cfb-125d-3ca9-b5ae-54ad0432e271 | -11.76853 | -48.19061 | 2025-08-13 04:40:00 | NOAA-21 | SÃO VALÉRIO | TOCANTINS | Brasil | 1720499 | 17 | 33 | nan | nan | nan | Cerrado | 2.5 |
| d0e4201c-f57b-364b-a9b0-aa86d7c7088e | -10.7601 | -48.77934 | 2025-08-13 04:40:00 | NOAA-21 | FÁTIMA | TOCANTINS | Brasil | 1707553 | 17 | 33 | nan | nan | nan | Cerrado | 1.4 |
| 9b4e85e8-ac85-3d9c-aced-adab4cf5c2b7 | -6.24492 | -55.36302 | 2025-08-13 04:40:00 | NOAA-21 | ITAITUBA | PARÁ | Brasil | 1503606 | 15 | 33 | nan | nan | nan | Amazônia | 1.3 |


[Clique aqui para ver as próximas entradas](README17.md)
