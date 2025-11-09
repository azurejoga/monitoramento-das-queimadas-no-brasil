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
| 44c40b13-6ffb-3547-9375-cec91f2bf522 | -4.43359 | -43.57555 | 2025-11-09 04:16:00 | NPP-375D | ALDEIAS ALTAS | MARANHÃO | Brasil | 2100303 | 21 | 33 | nan | nan | nan | Cerrado | 2.2 |
| 3782ab2b-e46e-3626-8af4-e501994418e5 | -4.5838 | -45.61802 | 2025-11-09 04:16:00 | NPP-375D | PAULO RAMOS | MARANHÃO | Brasil | 2108108 | 21 | 33 | nan | nan | nan | Cerrado | 1.0 |
| 88417ec2-7cfc-33b3-9d13-6351f10822c3 | -3.45276 | -48.84084 | 2025-11-09 04:16:00 | NPP-375D | IPIXUNA DO PARÁ | PARÁ | Brasil | 1503457 | 15 | 33 | nan | nan | nan | Amazônia | 1.3 |
| dac82cbf-cf44-336a-b2d8-b016142be9b9 | -4.68502 | -45.85086 | 2025-11-09 04:16:00 | NPP-375D | MARAJÁ DO SENA | MARANHÃO | Brasil | 2106359 | 21 | 33 | nan | nan | nan | Amazônia | 0.9 |
| e92b9d1b-3471-3a75-9af1-208118fb3ca5 | -4.68211 | -45.84599 | 2025-11-09 04:16:00 | NPP-375D | MARAJÁ DO SENA | MARANHÃO | Brasil | 2106359 | 21 | 33 | nan | nan | nan | Amazônia | 2.8 |
| 2e779c81-f993-3306-a94e-71d7dc6a21e4 | -5.17917 | -37.86783 | 2025-11-09 04:16:00 | NPP-375D | QUIXERÉ | CEARÁ | Brasil | 2311504 | 23 | 33 | nan | nan | nan | Caatinga | 1.9 |
| a26249d2-77f9-36d2-866e-9ecf21030e94 | -2.63621 | -49.52303 | 2025-11-09 04:16:00 | NPP-375D | MOCAJUBA | PARÁ | Brasil | 1504604 | 15 | 33 | nan | nan | nan | Amazônia | 1.8 |
| 51af8ce0-b8ff-36ac-bbd9-32f2bd4c61aa | -3.33504 | -44.37852 | 2025-11-09 04:16:00 | NPP-375D | ITAPECURU MIRIM | MARANHÃO | Brasil | 2105401 | 21 | 33 | nan | nan | nan | Cerrado | 14.7 |
| a9e83f41-01c4-3d5a-bf04-a89c86542c36 | -3.80758 | -45.99072 | 2025-11-09 04:16:00 | NPP-375D | ALTO ALEGRE DO PINDARÉ | MARANHÃO | Brasil | 2100477 | 21 | 33 | nan | nan | nan | Amazônia | 2.5 |
| 0bfeb545-801e-38a5-aa57-4b5ee42ae81d | -3.85037 | -47.40434 | 2025-11-09 04:16:00 | NPP-375D | ULIANÓPOLIS | PARÁ | Brasil | 1508126 | 15 | 33 | nan | nan | nan | Amazônia | 2.2 |
| e0e7311a-3fa3-3574-ba53-ad6022f2f230 | -3.31729 | -50.12449 | 2025-11-09 04:16:00 | NPP-375D | PACAJÁ | PARÁ | Brasil | 1505486 | 15 | 33 | nan | nan | nan | Amazônia | 2.2 |
| 993ec80e-bb39-31c6-bf56-e59e8d1eb30b | -3.85093 | -47.40086 | 2025-11-09 04:16:00 | NPP-375D | ULIANÓPOLIS | PARÁ | Brasil | 1508126 | 15 | 33 | nan | nan | nan | Amazônia | 0.9 |
| fec76c48-bf16-3005-8fc2-e3a72f9a56d1 | -4.36055 | -45.76011 | 2025-11-09 04:16:00 | NPP-375D | BREJO DE AREIA | MARANHÃO | Brasil | 2102150 | 21 | 33 | nan | nan | nan | Amazônia | 1.1 |
| 2170a81c-1cdb-3e4c-b5d4-218041dd600f | -3.59305 | -41.65475 | 2025-11-09 04:16:00 | NPP-375D | COCAL | PIAUÍ | Brasil | 2202703 | 22 | 33 | nan | nan | nan | Caatinga | 4.2 |
| 9b6f5afb-8169-372c-a481-3db68cdfbd42 | -2.96573 | -41.57882 | 2025-11-09 04:16:00 | NPP-375D | LUÍS CORREIA | PIAUÍ | Brasil | 2205706 | 22 | 33 | nan | nan | nan | Cerrado | 16.8 |
| 60567f02-f09b-3bf6-930a-983408067dff | -3.32591 | -44.36942 | 2025-11-09 04:16:00 | NPP-375D | ITAPECURU MIRIM | MARANHÃO | Brasil | 2105401 | 21 | 33 | nan | nan | nan | Cerrado | 2.8 |
| f46bf5b9-e444-3da3-ad06-f01c18bfea73 | -3.46976 | -50.34676 | 2025-11-09 04:16:00 | NPP-375D | PACAJÁ | PARÁ | Brasil | 1505486 | 15 | 33 | nan | nan | nan | Amazônia | 1.2 |
| f47a8a08-f42a-36bf-a0c1-3955f9277fa3 | -3.31638 | -50.12987 | 2025-11-09 04:16:00 | NPP-375D | PACAJÁ | PARÁ | Brasil | 1505486 | 15 | 33 | nan | nan | nan | Amazônia | 2.6 |
| 6c171a8b-cfe2-32ec-9a76-9ad7f22110da | -3.95659 | -49.02669 | 2025-11-09 04:16:00 | NPP-375D | GOIANÉSIA DO PARÁ | PARÁ | Brasil | 1503093 | 15 | 33 | nan | nan | nan | Amazônia | 2.7 |
| e016cea5-18c8-3560-8c75-0a58a28b4212 | -5.70756 | -44.24541 | 2025-11-09 04:16:00 | NPP-375D | SÃO DOMINGOS DO MARANHÃO | MARANHÃO | Brasil | 2110708 | 21 | 33 | nan | nan | nan | Cerrado | 0.7 |
| c7eaed90-93af-30f6-a1eb-d57102660e93 | -2.83434 | -50.43942 | 2025-11-09 04:16:00 | NPP-375D | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 1.9 |
| e4182758-3f77-3a87-904a-59d329e3c0c8 | -4.77964 | -46.904 | 2025-11-09 04:16:00 | NPP-375D | BOM JESUS DAS SELVAS | MARANHÃO | Brasil | 2102036 | 21 | 33 | nan | nan | nan | Amazônia | 1.2 |
| 0d2c2bd9-d84d-349c-a5d3-53ea2a04f19f | -6.31112 | -39.94296 | 2025-11-09 04:16:00 | NPP-375D | CATARINA | CEARÁ | Brasil | 2303600 | 23 | 33 | nan | nan | nan | Caatinga | 0.6 |
| bc6d18a4-96c3-30f1-a1d6-885fd99a31d6 | -3.30611 | -50.16104 | 2025-11-09 04:16:00 | NPP-375D | PACAJÁ | PARÁ | Brasil | 1505486 | 15 | 33 | nan | nan | nan | Amazônia | 3.7 |
| a69319b9-23d0-36f9-b9b8-3f9473b80325 | -3.32875 | -44.3737 | 2025-11-09 04:16:00 | NPP-375D | ITAPECURU MIRIM | MARANHÃO | Brasil | 2105401 | 21 | 33 | nan | nan | nan | Cerrado | 15.1 |
| 92167740-36a6-3d1d-ab0e-38d8af7fc528 | -4.80575 | -38.69576 | 2025-11-09 04:16:00 | NPP-375D | IBARETAMA | CEARÁ | Brasil | 2305266 | 23 | 33 | nan | nan | nan | Caatinga | 1.6 |
| e2214fa7-175c-3c05-bf12-8e2e20d0a96e | -3.09283 | -49.26316 | 2025-11-09 04:16:00 | NPP-375D | MOJU | PARÁ | Brasil | 1504703 | 15 | 33 | nan | nan | nan | Amazônia | 2.4 |
| b8af2e5f-82c8-3aad-8f21-b3b0b875105e | -4.72218 | -43.3379 | 2025-11-09 04:16:00 | NPP-375D | CAXIAS | MARANHÃO | Brasil | 2103000 | 21 | 33 | nan | nan | nan | Cerrado | 0.6 |
| 7d660aa8-072a-3674-b81a-1ca8ef72c313 | -3.86892 | -49.38323 | 2025-11-09 04:16:00 | NPP-375D | BREU BRANCO | PARÁ | Brasil | 1501782 | 15 | 33 | nan | nan | nan | Amazônia | 6.2 |
| 73d6ca24-ef5c-3db9-aa16-b9c742770400 | -3.95143 | -49.03021 | 2025-11-09 04:16:00 | NPP-375D | GOIANÉSIA DO PARÁ | PARÁ | Brasil | 1503093 | 15 | 33 | nan | nan | nan | Amazônia | 2.7 |
| 0abd2869-0dcd-3ac9-9d4a-8dadafc63a91 | -4.45507 | -44.64336 | 2025-11-09 04:16:00 | NPP-375D | TRIZIDELA DO VALE | MARANHÃO | Brasil | 2112233 | 21 | 33 | nan | nan | nan | Cerrado | 8.9 |
| 39d20b8a-a151-35be-9785-7ac179d26477 | -4.37868 | -45.50028 | 2025-11-09 04:16:00 | NPP-375D | BREJO DE AREIA | MARANHÃO | Brasil | 2102150 | 21 | 33 | nan | nan | nan | Amazônia | 0.6 |
| 14be8fc9-66ca-3d7c-89a5-d06211a66dfb | -3.28821 | -50.19605 | 2025-11-09 04:16:00 | NPP-375D | PACAJÁ | PARÁ | Brasil | 1505486 | 15 | 33 | nan | nan | nan | Amazônia | 1.6 |
| 98786414-6465-3be4-aa46-c4fbd2d45419 | -4.33717 | -46.15606 | 2025-11-09 04:16:00 | NPP-375D | SANTA LUZIA | MARANHÃO | Brasil | 2110005 | 21 | 33 | nan | nan | nan | Amazônia | 1.4 |
| 7c766086-6d5d-300c-ad94-638f03678101 | -3.61884 | -43.65311 | 2025-11-09 04:16:00 | NPP-375D | VARGEM GRANDE | MARANHÃO | Brasil | 2112704 | 21 | 33 | nan | nan | nan | Cerrado | 3.3 |
| 34b790b1-3ed0-3fc8-9a0a-f66d6d6baf2c | -4.0392 | -46.24873 | 2025-11-09 04:16:00 | NPP-375D | BURITICUPU | MARANHÃO | Brasil | 2102325 | 21 | 33 | nan | nan | nan | Amazônia | 1.0 |
| 9878e257-e6b2-3b1e-9fd0-b3050fc86bbb | -5.16206 | -46.13174 | 2025-11-09 04:16:00 | NPP-375D | ARAME | MARANHÃO | Brasil | 2100956 | 21 | 33 | nan | nan | nan | Amazônia | 0.7 |
| 341d72e5-bbc0-31bd-9fbc-b9110e636846 | -5.05675 | -45.86075 | 2025-11-09 04:16:00 | NPP-375D | ARAME | MARANHÃO | Brasil | 2100956 | 21 | 33 | nan | nan | nan | Amazônia | 1.0 |
| c92cfd1c-5f30-39b9-b74e-085bcdb50f88 | 0.65712 | -51.54464 | 2025-11-09 04:16:00 | NPP-375D | PORTO GRANDE | AMAPÁ | Brasil | 1600535 | 16 | 33 | nan | nan | nan | Amazônia | 1.5 |
| c2642386-951f-34ca-a623-2156bcf8575e | -4.15027 | -46.2557 | 2025-11-09 04:16:00 | NPP-375D | ALTO ALEGRE DO PINDARÉ | MARANHÃO | Brasil | 2100477 | 21 | 33 | nan | nan | nan | Amazônia | 0.7 |
| 9d7dd322-e60a-33c6-b8f8-fc382fa8497f | -4.28618 | -46.84299 | 2025-11-09 04:16:00 | NPP-375D | BOM JARDIM | MARANHÃO | Brasil | 2102002 | 21 | 33 | nan | nan | nan | Amazônia | 1.2 |
| 5c263afa-c34e-3da5-a5b0-5cd33a2eb8e7 | -4.11212 | -47.28874 | 2025-11-09 04:16:00 | NPP-375D | ITINGA DO MARANHÃO | MARANHÃO | Brasil | 2105427 | 21 | 33 | nan | nan | nan | Amazônia | 2.8 |
| 21e875e9-cbae-3325-9365-e20fdbb4358f | -2.50822 | -49.46286 | 2025-11-09 04:16:00 | NPP-375D | CAMETÁ | PARÁ | Brasil | 1502103 | 15 | 33 | nan | nan | nan | Amazônia | 3.9 |
| 5e9ed493-f5db-3407-88a6-11d1490b4163 | -2.48145 | -54.19881 | 2025-11-09 04:16:00 | NPP-375D | PRAINHA | PARÁ | Brasil | 1506005 | 15 | 33 | nan | nan | nan | Amazônia | 1.7 |
| 798213bc-37f0-389d-a0b7-eaf12c6a04c3 | -7.08636 | -35.12774 | 2025-11-09 04:16:00 | NPP-375D | SAPÉ | PARAÍBA | Brasil | 2515302 | 25 | 33 | nan | nan | nan | Mata Atlântica | 1.4 |
| f0d0a6bc-bd50-3224-a1fd-f62e0b0f55ad | -4.23349 | -48.60552 | 2025-11-09 04:16:00 | NPP-375D | RONDON DO PARÁ | PARÁ | Brasil | 1506187 | 15 | 33 | nan | nan | nan | Amazônia | 1.1 |
| 8c5eff85-a81f-3944-8127-64da78c6d359 | -5.4311 | -45.0338 | 2025-11-09 04:16:00 | NPP-375D | BARRA DO CORDA | MARANHÃO | Brasil | 2101608 | 21 | 33 | nan | nan | nan | Cerrado | 1.4 |
| c12b8b07-bee3-3900-8325-e2b1ec7609f8 | -5.32252 | -44.83575 | 2025-11-09 04:16:00 | NPP-375D | TUNTUM | MARANHÃO | Brasil | 2112308 | 21 | 33 | nan | nan | nan | Cerrado | 1.1 |
| 6c5c20b6-90a4-30f8-8a87-5922f2c854f3 | -5.14019 | -45.7177 | 2025-11-09 04:16:00 | NPP-375D | ITAIPAVA DO GRAJAÚ | MARANHÃO | Brasil | 2105351 | 21 | 33 | nan | nan | nan | Cerrado | 2.0 |
| 69ce7d20-0a3e-38b9-9cdb-add56641d982 | -3.84211 | -50.74478 | 2025-11-09 04:16:00 | NPP-375D | PACAJÁ | PARÁ | Brasil | 1505486 | 15 | 33 | nan | nan | nan | Amazônia | 1.5 |
| aeae04d5-b4d8-398c-b88a-c48bd11c5f1a | -3.33682 | -44.36735 | 2025-11-09 04:16:00 | NPP-375D | ITAPECURU MIRIM | MARANHÃO | Brasil | 2105401 | 21 | 33 | nan | nan | nan | Cerrado | 6.6 |
| ac4aafd5-63c7-3d7a-b295-41d19582bf92 | -3.31497 | -50.1233 | 2025-11-09 04:16:00 | NPP-375D | PACAJÁ | PARÁ | Brasil | 1505486 | 15 | 33 | nan | nan | nan | Amazônia | 1.7 |
| a3ce2929-e0da-34cb-885e-2f4c1a357ae5 | -4.51878 | -45.72499 | 2025-11-09 04:16:00 | NPP-375D | BREJO DE AREIA | MARANHÃO | Brasil | 2102150 | 21 | 33 | nan | nan | nan | Amazônia | 2.2 |
| 0a9d2552-1e49-3d69-8be4-2b12d85f53fe | -4.63004 | -46.39621 | 2025-11-09 04:16:00 | NPP-375D | BURITICUPU | MARANHÃO | Brasil | 2102325 | 21 | 33 | nan | nan | nan | Amazônia | 1.4 |
| f4eb0449-54a3-3c80-882b-4d25966deabd | -4.29192 | -50.66186 | 2025-11-09 04:16:00 | NPP-375D | NOVO REPARTIMENTO | PARÁ | Brasil | 1505064 | 15 | 33 | nan | nan | nan | Amazônia | 3.2 |
| e165bf89-ba21-3d50-83c3-68ac5473e34b | -3.67229 | -51.16532 | 2025-11-09 04:16:00 | NPP-375D | PACAJÁ | PARÁ | Brasil | 1505486 | 15 | 33 | nan | nan | nan | Amazônia | 0.6 |
| a733036a-78f4-3dd7-91c7-47c9b5890fe9 | -5.72572 | -43.98228 | 2025-11-09 04:16:00 | NPP-375D | FORTUNA | MARANHÃO | Brasil | 2104206 | 21 | 33 | nan | nan | nan | Cerrado | 1.6 |
| 8c00f3d1-42fe-3b9c-a12e-fa49682e9db8 | -2.84104 | -49.5177 | 2025-11-09 04:16:00 | NPP-375D | BAIÃO | PARÁ | Brasil | 1501204 | 15 | 33 | nan | nan | nan | Amazônia | 1.5 |
| c82e4b9a-cc4d-30c1-b2e6-3683c2326414 | -2.92151 | -40.0074 | 2025-11-09 04:16:00 | NPP-375D | ACARAÚ | CEARÁ | Brasil | 2300200 | 23 | 33 | nan | nan | nan | Caatinga | 1.4 |
| f4a40054-e0b7-38ef-9a4c-dd7571215a01 | -3.8025 | -48.90134 | 2025-11-09 04:16:00 | NPP-375D | GOIANÉSIA DO PARÁ | PARÁ | Brasil | 1503093 | 15 | 33 | nan | nan | nan | Amazônia | 4.5 |
| ad371a5d-0140-344d-93fc-c632964df61e | -3.33966 | -44.37163 | 2025-11-09 04:16:00 | NPP-375D | ITAPECURU MIRIM | MARANHÃO | Brasil | 2105401 | 21 | 33 | nan | nan | nan | Cerrado | 6.6 |
| 50b17434-e237-3673-89c0-b6089c4efc72 | -5.44423 | -45.86843 | 2025-11-09 04:16:00 | NPP-375D | GRAJAÚ | MARANHÃO | Brasil | 2104800 | 21 | 33 | nan | nan | nan | Cerrado | 1.0 |
| b2867c32-abf8-3723-9d57-1177be7b43a8 | -4.61727 | -46.38078 | 2025-11-09 04:16:00 | NPP-375D | BURITICUPU | MARANHÃO | Brasil | 2102325 | 21 | 33 | nan | nan | nan | Amazônia | 1.0 |
| d0fe5410-8328-3340-aa87-e4354ced1781 | -4.00948 | -44.78666 | 2025-11-09 04:16:00 | NPP-375D | BACABAL | MARANHÃO | Brasil | 2101202 | 21 | 33 | nan | nan | nan | Amazônia | 2.2 |
| bb64aeeb-ebf9-3462-b14c-10c7e6a91719 | -3.32249 | -50.15289 | 2025-11-09 04:16:00 | NPP-375D | PACAJÁ | PARÁ | Brasil | 1505486 | 15 | 33 | nan | nan | nan | Amazônia | 4.5 |
| 85b114c8-aa9b-3331-bd13-9c38147c5753 | -4.63751 | -46.39729 | 2025-11-09 04:16:00 | NPP-375D | BURITICUPU | MARANHÃO | Brasil | 2102325 | 21 | 33 | nan | nan | nan | Amazônia | 12.2 |
| 902ce14b-b865-37df-9c7a-1f285388532e | -3.89311 | -47.18218 | 2025-11-09 04:16:00 | NPP-375D | ULIANÓPOLIS | PARÁ | Brasil | 1508126 | 15 | 33 | nan | nan | nan | Amazônia | 4.7 |
| 5b8c026a-1691-3780-91cb-fb60cbbf8877 | -5.2158 | -45.14429 | 2025-11-09 04:16:00 | NPP-375D | BARRA DO CORDA | MARANHÃO | Brasil | 2101608 | 21 | 33 | nan | nan | nan | Cerrado | 1.4 |
| d2ceb7cb-af30-3edb-9de1-c028080b7bfc | -2.26533 | -47.84621 | 2025-11-09 04:16:00 | NPP-375D | AURORA DO PARÁ | PARÁ | Brasil | 1500958 | 15 | 33 | nan | nan | nan | Amazônia | 3.1 |
| 63d2669a-aad5-3a47-b0d7-87a7560cb5bd | -3.31601 | -50.10252 | 2025-11-09 04:16:00 | NPP-375D | PACAJÁ | PARÁ | Brasil | 1505486 | 15 | 33 | nan | nan | nan | Amazônia | 8.8 |
| 629606b0-2d14-37da-bce0-f5a016897f47 | -4.69917 | -45.69666 | 2025-11-09 04:16:00 | NPP-375D | MARAJÁ DO SENA | MARANHÃO | Brasil | 2106359 | 21 | 33 | nan | nan | nan | Amazônia | 0.8 |
| 71584400-1fba-308f-9c05-cba3882b6e86 | -3.10043 | -50.19491 | 2025-11-09 04:16:00 | NPP-375D | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 2.7 |
| bf6f53cb-710c-3949-9615-a9d4e113fd66 | -2.98315 | -52.82438 | 2025-11-09 04:16:00 | NPP-375D | BRASIL NOVO | PARÁ | Brasil | 1501725 | 15 | 33 | nan | nan | nan | Amazônia | 1.2 |
| 363046be-df4f-357b-92c9-7d35fae55c3d | -3.9406 | -46.3838 | 2025-11-09 04:16:00 | NPP-375D | BOM JARDIM | MARANHÃO | Brasil | 2102002 | 21 | 33 | nan | nan | nan | Amazônia | 1.3 |
| b5922459-91e6-3011-aa64-bb6610743f2a | -2.10845 | -47.64409 | 2025-11-09 04:16:00 | NPP-375D | AURORA DO PARÁ | PARÁ | Brasil | 1500958 | 15 | 33 | nan | nan | nan | Amazônia | 1.0 |
| 8d6c7427-0460-3627-9a1c-1055435f1429 | -3.31268 | -50.10658 | 2025-11-09 04:16:00 | NPP-375D | PACAJÁ | PARÁ | Brasil | 1505486 | 15 | 33 | nan | nan | nan | Amazônia | 6.6 |
| 1f5c6fa2-94f3-3e38-a0b5-9ea5fe423f2d | -3.3416 | -39.99443 | 2025-11-09 04:16:00 | NPP-375D | MORRINHOS | CEARÁ | Brasil | 2308906 | 23 | 33 | nan | nan | nan | Caatinga | 1.7 |
| 88a2303d-eb5c-38b8-bef2-72b3bd3eb191 | -3.59584 | -41.65876 | 2025-11-09 04:16:00 | NPP-375D | COCAL | PIAUÍ | Brasil | 2202703 | 22 | 33 | nan | nan | nan | Caatinga | 4.5 |
| 47960f4e-4dbf-3e27-81ac-e156f17cac00 | -3.34025 | -44.3679 | 2025-11-09 04:16:00 | NPP-375D | ITAPECURU MIRIM | MARANHÃO | Brasil | 2105401 | 21 | 33 | nan | nan | nan | Cerrado | 6.6 |
| 0734b836-4281-31d4-a99a-39eb85337e1e | -2.6012 | -49.23101 | 2025-11-09 04:16:00 | NPP-375D | MOJU | PARÁ | Brasil | 1504703 | 15 | 33 | nan | nan | nan | Amazônia | 2.2 |
| fc7dddb1-d668-35b3-bb73-0da58f92208e | -3.94772 | -49.02501 | 2025-11-09 04:16:00 | NPP-375D | GOIANÉSIA DO PARÁ | PARÁ | Brasil | 1503093 | 15 | 33 | nan | nan | nan | Amazônia | 1.5 |
| ca281f74-8307-3958-82f4-e7f0fefa1d86 | -4.84073 | -42.84523 | 2025-11-09 04:16:00 | NPP-375D | TERESINA | PIAUÍ | Brasil | 2211001 | 22 | 33 | nan | nan | nan | Cerrado | 7.9 |
| 53f26d59-ae2f-39eb-a356-e583ba5baf9e | -4.54469 | -45.67863 | 2025-11-09 04:16:00 | NPP-375D | PAULO RAMOS | MARANHÃO | Brasil | 2108108 | 21 | 33 | nan | nan | nan | Amazônia | 1.1 |
| ac766a89-57f9-33bf-b2b6-594768ec9f51 | -5.80519 | -41.34471 | 2025-11-09 04:16:00 | NPP-375D | SÃO MIGUEL DO TAPUIO | PIAUÍ | Brasil | 2210409 | 22 | 33 | nan | nan | nan | Caatinga | 3.6 |
| ac8f6def-e628-3630-bdea-9024a44b5435 | -4.33048 | -45.70993 | 2025-11-09 04:16:00 | NPP-375D | BREJO DE AREIA | MARANHÃO | Brasil | 2102150 | 21 | 33 | nan | nan | nan | Amazônia | 1.1 |
| 3915d85b-280d-370a-b376-44856e9914ac | -3.32532 | -44.37315 | 2025-11-09 04:16:00 | NPP-375D | ITAPECURU MIRIM | MARANHÃO | Brasil | 2105401 | 21 | 33 | nan | nan | nan | Cerrado | 5.4 |
| 656531aa-772b-3162-ac3e-cf3c6021e50a | -2.59994 | -49.21939 | 2025-11-09 04:16:00 | NPP-375D | MOJU | PARÁ | Brasil | 1504703 | 15 | 33 | nan | nan | nan | Amazônia | 3.2 |
| f2222268-726d-3b3c-8b91-db4f10469d8b | -3.99111 | -50.43564 | 2025-11-09 04:16:00 | NPP-375D | NOVO REPARTIMENTO | PARÁ | Brasil | 1505064 | 15 | 33 | nan | nan | nan | Amazônia | 2.6 |
| 1f6cb93d-ea34-3358-bf87-9972f5905554 | -4.40033 | -45.95116 | 2025-11-09 04:16:00 | NPP-375D | SANTA LUZIA | MARANHÃO | Brasil | 2110005 | 21 | 33 | nan | nan | nan | Amazônia | 1.0 |
| c360cb8a-67f7-39b8-bc04-6286d23d8337 | -3.32944 | -49.13141 | 2025-11-09 04:16:00 | NPP-375D | MOJU | PARÁ | Brasil | 1504703 | 15 | 33 | nan | nan | nan | Amazônia | 1.5 |
| ec8f5f44-147b-3a75-9575-343abba0a397 | -4.58527 | -45.62125 | 2025-11-09 04:16:00 | NPP-375D | PAULO RAMOS | MARANHÃO | Brasil | 2108108 | 21 | 33 | nan | nan | nan | Cerrado | 5.1 |
| 54aff8bf-38af-3d01-a24a-651bba749490 | -2.26952 | -47.84608 | 2025-11-09 04:16:00 | NPP-375D | AURORA DO PARÁ | PARÁ | Brasil | 1500958 | 15 | 33 | nan | nan | nan | Amazônia | 0.9 |
| d3e194f3-01c1-3b3a-a1c9-f2c408506f37 | -3.41177 | -50.26353 | 2025-11-09 04:16:00 | NPP-375D | PACAJÁ | PARÁ | Brasil | 1505486 | 15 | 33 | nan | nan | nan | Amazônia | 3.5 |
| 2142e53c-7f7c-3ae2-9eb7-e6986e3fe15e | -3.09905 | -50.32425 | 2025-11-09 04:16:00 | NPP-375D | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 10.9 |
| d988560d-c6d3-3f58-a023-68d89e462cd8 | -3.35802 | -49.24352 | 2025-11-09 04:16:00 | NPP-375D | MOJU | PARÁ | Brasil | 1504703 | 15 | 33 | nan | nan | nan | Amazônia | 1.5 |
| 3980320a-d48d-3a05-af31-8cb58148c736 | -1.79432 | -48.07172 | 2025-11-09 04:16:00 | NPP-375D | BUJARU | PARÁ | Brasil | 1501907 | 15 | 33 | nan | nan | nan | Amazônia | 1.0 |
| ccc0a2ca-1f37-3770-bede-51efbc68debf | -4.33002 | -49.75936 | 2025-11-09 04:16:00 | NPP-375D | NOVO REPARTIMENTO | PARÁ | Brasil | 1505064 | 15 | 33 | nan | nan | nan | Amazônia | 12.6 |
| 320f6b49-da37-37ff-9b50-5ff4420f1f6e | -2.74365 | -45.16429 | 2025-11-09 04:16:00 | NPP-375D | PINHEIRO | MARANHÃO | Brasil | 2108603 | 21 | 33 | nan | nan | nan | Amazônia | 1.9 |
| 741fddf1-f095-3df8-bbc2-dd6a33e2090a | -3.58861 | -41.66122 | 2025-11-09 04:16:00 | NPP-375D | COCAL | PIAUÍ | Brasil | 2202703 | 22 | 33 | nan | nan | nan | Caatinga | 5.5 |
| 31eac77d-4bc9-3ffa-8d44-52e2a1f7a55e | -3.26808 | -50.04472 | 2025-11-09 04:16:00 | NPP-375D | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 4.3 |


[Clique aqui para ver as próximas entradas](README17.md)
