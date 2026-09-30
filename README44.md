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

## Dados Diários - Página 44

| ID | Latitude | Longitude | Data/Hora GMT | Satélite | Município | Estado | País | Município ID | Estado ID | País ID | Dias sem Chuva | Precipitação | Risco de Fogo | Bioma | FRP |
|----|----------|-----------|---------------|----------|-----------|--------|------|--------------|-----------|---------|----------------|--------------|----------------|-------|-----|
| b1eba6bb-ea86-3690-9d80-17979ca9c735 | -2.86119 | -54.12193 | 2026-09-30 04:53:00 | NOAA-20 | SANTARÉM | PARÁ | Brasil | 1506807 | 15 | 33 | nan | nan | nan | Amazônia | 1.0 |
| a83d7bf5-ef1b-3454-9ac6-3b56092e6ab0 | -8.9372 | -49.79163 | 2026-09-30 04:53:00 | NOAA-20 | SANTA MARIA DAS BARREIRAS | PARÁ | Brasil | 1506583 | 15 | 33 | nan | nan | nan | Amazônia | 0.4 |
| aa262c2b-7b46-33d3-9202-d18ddf1a315e | -7.82632 | -45.82174 | 2026-09-30 04:53:00 | NOAA-20 | TASSO FRAGOSO | MARANHÃO | Brasil | 2112001 | 21 | 33 | nan | nan | nan | Cerrado | 2.7 |
| 41860de8-c695-3a5d-abc2-a9ec51201246 | -16.11236 | -48.32829 | 2026-09-30 04:53:00 | NOAA-20 | SANTO ANTÔNIO DO DESCOBERTO | GOIÁS | Brasil | 5219753 | 52 | 33 | nan | nan | nan | Cerrado | 1.7 |
| 1949840a-0c0c-3a78-9ea3-280aa18080f5 | -3.35823 | -50.46875 | 2026-09-30 04:53:00 | NOAA-20 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 1.7 |
| 37831d53-c389-37f2-b3c7-0312432a03f1 | -7.12938 | -49.18308 | 2026-09-30 04:53:00 | NOAA-20 | SANTA FÉ DO ARAGUAIA | TOCANTINS | Brasil | 1718865 | 17 | 33 | nan | nan | nan | Amazônia | 1.5 |
| 83362655-f43b-3fec-9b90-e9a7b5f9fa8b | -11.43054 | -43.43272 | 2026-09-30 04:53:00 | NOAA-20 | BARRA | BAHIA | Brasil | 2902708 | 29 | 33 | nan | nan | nan | Cerrado | 1.9 |
| 66a80a22-09d1-3a14-93df-baccfd439f76 | -12.89312 | -61.71796 | 2026-09-30 04:53:00 | NOAA-20 | PIMENTEIRAS DO OESTE | RONDÔNIA | Brasil | 1101468 | 11 | 33 | nan | nan | nan | Amazônia | 1.4 |
| 6f8c225f-96cd-39ef-b2bc-257818c8104d | -5.76149 | -45.18107 | 2026-09-30 04:53:00 | NOAA-20 | BARRA DO CORDA | MARANHÃO | Brasil | 2101608 | 21 | 33 | nan | nan | nan | Cerrado | 2.6 |
| 57d998d3-ae14-319e-94b9-da80731a3458 | -10.77808 | -47.25349 | 2026-09-30 04:53:00 | NOAA-20 | PONTE ALTA DO TOCANTINS | TOCANTINS | Brasil | 1717909 | 17 | 33 | nan | nan | nan | Cerrado | 1.2 |
| 6d82a0db-8569-3448-a21e-b0dd9dfd5d96 | -6.18691 | -55.96828 | 2026-09-30 04:53:00 | NOAA-20 | ITAITUBA | PARÁ | Brasil | 1503606 | 15 | 33 | nan | nan | nan | Amazônia | 0.8 |
| 09c35bee-b13c-35e7-8993-830fa079fbca | -9.15311 | -45.60125 | 2026-09-30 04:53:00 | NOAA-20 | SANTA FILOMENA | PIAUÍ | Brasil | 2209203 | 22 | 33 | nan | nan | nan | Cerrado | 1.5 |
| 33b93b50-d1a0-3dc4-9b85-96429f8f3bc4 | -3.51141 | -50.31683 | 2026-09-30 04:53:00 | NOAA-20 | PACAJÁ | PARÁ | Brasil | 1505486 | 15 | 33 | nan | nan | nan | Amazônia | 1.6 |
| c7742026-2560-3cc0-9d96-1aa9d57c3583 | -8.2972 | -54.70802 | 2026-09-30 04:53:00 | NOAA-20 | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 1.2 |
| 2e154f3c-d186-3b55-975c-1658cb9cf620 | -6.52952 | -47.12021 | 2026-09-30 04:53:00 | NOAA-20 | PORTO FRANCO | MARANHÃO | Brasil | 2109007 | 21 | 33 | nan | nan | nan | Cerrado | 1.2 |
| 4fc9c05e-bfd7-3353-84e9-6193a9278d56 | -7.92814 | -45.44458 | 2026-09-30 04:53:00 | NOAA-20 | RIBEIRO GONÇALVES | PIAUÍ | Brasil | 2208908 | 22 | 33 | nan | nan | nan | Cerrado | 2.7 |
| 15048baa-8334-3b97-a423-cce96af27c21 | -6.79407 | -55.82335 | 2026-09-30 04:53:00 | NOAA-20 | NOVO PROGRESSO | PARÁ | Brasil | 1505031 | 15 | 33 | nan | nan | nan | Amazônia | 1.5 |
| e4b25e25-db99-3ccc-9073-9cb7140e7529 | -2.89765 | -54.13231 | 2026-09-30 04:53:00 | NOAA-20 | SANTARÉM | PARÁ | Brasil | 1506807 | 15 | 33 | nan | nan | nan | Amazônia | 1.4 |
| 5d4c74bc-f519-3153-95f5-2547f46b051f | -6.1415 | -53.06501 | 2026-09-30 04:53:00 | NOAA-20 | SÃO FÉLIX DO XINGU | PARÁ | Brasil | 1507300 | 15 | 33 | nan | nan | nan | Amazônia | 1.3 |
| 2ddf2173-4adb-3214-8a02-0e36d934116e | -4.44315 | -46.2867 | 2026-09-30 04:53:00 | NOAA-20 | BURITICUPU | MARANHÃO | Brasil | 2102325 | 21 | 33 | nan | nan | nan | Amazônia | 2.5 |
| bc81c93d-db70-3ec0-85c1-66174cab953e | -9.28231 | -46.41458 | 2026-09-30 04:53:00 | NOAA-20 | ALTO PARNAÍBA | MARANHÃO | Brasil | 2100501 | 21 | 33 | nan | nan | nan | Cerrado | 2.6 |
| 16aa9d98-c6f5-3ea8-8257-814fb760802f | -4.80587 | -45.64489 | 2026-09-30 04:53:00 | NOAA-20 | MARAJÁ DO SENA | MARANHÃO | Brasil | 2106359 | 21 | 33 | nan | nan | nan | Amazônia | 1.7 |
| 5d355142-b164-3ba6-bd67-2901a4e87b7b | -2.9961 | -54.76753 | 2026-09-30 04:53:00 | NOAA-20 | MOJUÍ DOS CAMPOS | PARÁ | Brasil | 1504752 | 15 | 33 | nan | nan | nan | Amazônia | 3.4 |
| aa5247da-8891-319e-9ad2-158738c63825 | -11.1636 | -48.31698 | 2026-09-30 04:53:00 | NOAA-20 | IPUEIRAS | TOCANTINS | Brasil | 1709807 | 17 | 33 | nan | nan | nan | Cerrado | 2.2 |
| 308e8040-94db-395b-8e2c-3fba5baae443 | -6.48632 | -58.53648 | 2026-09-30 04:53:00 | NOAA-20 | MAUÉS | AMAZONAS | Brasil | 1302900 | 13 | 33 | nan | nan | nan | Amazônia | 2.7 |
| aabc584f-68cf-3467-aa3d-c503a837db4a | -15.57378 | -47.89254 | 2026-09-30 04:53:00 | NOAA-20 | BRASÍLIA | DISTRITO FEDERAL | Brasil | 5300108 | 53 | 33 | nan | nan | nan | Cerrado | 1.9 |
| b96a5fea-3368-353e-b304-823df79871fd | -4.81515 | -45.63881 | 2026-09-30 04:53:00 | NOAA-20 | MARAJÁ DO SENA | MARANHÃO | Brasil | 2106359 | 21 | 33 | nan | nan | nan | Amazônia | 3.8 |
| 4f52313c-3324-3bb4-bfa1-507b5ad54304 | -7.49291 | -45.79982 | 2026-09-30 04:53:00 | NOAA-20 | SAMBAÍBA | MARANHÃO | Brasil | 2109700 | 21 | 33 | nan | nan | nan | Cerrado | 1.2 |
| f53ee085-9bec-3df2-a2bf-cc177152d998 | -6.92213 | -44.55972 | 2026-09-30 04:53:00 | NOAA-20 | SÃO DOMINGOS DO AZEITÃO | MARANHÃO | Brasil | 2110658 | 21 | 33 | nan | nan | nan | Cerrado | 5.3 |
| f2c7f313-c1c0-33ab-a129-bcf7a4767039 | -11.38337 | -43.46925 | 2026-09-30 04:53:00 | NOAA-20 | BARRA | BAHIA | Brasil | 2902708 | 29 | 33 | nan | nan | nan | Cerrado | 3.6 |
| 4847a1ff-23d4-3a1e-969e-5db63a005f35 | -9.97313 | -50.24923 | 2026-09-30 04:53:00 | NOAA-20 | PIUM | TOCANTINS | Brasil | 1717503 | 17 | 33 | nan | nan | nan | Cerrado | 1.2 |
| 030c9a47-3ef7-3985-a6fd-a2c7ae642978 | -6.28719 | -43.64643 | 2026-09-30 04:53:00 | NOAA-20 | PASSAGEM FRANCA | MARANHÃO | Brasil | 2107902 | 21 | 33 | nan | nan | nan | Cerrado | 1.9 |
| a47182c8-3937-3ea9-a9be-192b28f35397 | -2.90335 | -54.09699 | 2026-09-30 04:53:00 | NOAA-20 | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | 32.3 |
| bf904a26-9392-3c8c-a4d8-8bdf43caa40a | -7.82248 | -45.82067 | 2026-09-30 04:53:00 | NOAA-20 | TASSO FRAGOSO | MARANHÃO | Brasil | 2112001 | 21 | 33 | nan | nan | nan | Cerrado | 5.1 |
| 96f1431f-7d85-3382-aab4-e1f5ac4ea2fc | -7.12881 | -49.18686 | 2026-09-30 04:53:00 | NOAA-20 | SANTA FÉ DO ARAGUAIA | TOCANTINS | Brasil | 1718865 | 17 | 33 | nan | nan | nan | Amazônia | 2.6 |
| 71a1eafd-97b5-382d-94f9-4ade3f5d6264 | -3.87566 | -51.95547 | 2026-09-30 04:53:00 | NOAA-20 | SENADOR JOSÉ PORFÍRIO | PARÁ | Brasil | 1507805 | 15 | 33 | nan | nan | nan | Amazônia | 0.9 |
| c752328c-7b68-3b7d-86ad-2918b5902f6b | -10.08192 | -50.31866 | 2026-09-30 04:53:00 | NOAA-20 | PIUM | TOCANTINS | Brasil | 1717503 | 17 | 33 | nan | nan | nan | Cerrado | 1.9 |
| 8954d827-1d11-3e6f-8d95-46ad47314b3a | -14.90973 | -43.41628 | 2026-09-30 04:53:00 | NOAA-20 | GAMELEIRAS | MINAS GERAIS | Brasil | 3127339 | 31 | 33 | nan | nan | nan | Caatinga | 2.4 |
| 93b8565d-3d17-3052-a6e8-decf47712a39 | -9.06584 | -49.86446 | 2026-09-30 04:53:00 | NOAA-20 | SANTA MARIA DAS BARREIRAS | PARÁ | Brasil | 1506583 | 15 | 33 | nan | nan | nan | Amazônia | 1.0 |
| 5ae7c194-e217-3abf-b0db-40c9acb56a77 | -7.82576 | -45.82553 | 2026-09-30 04:53:00 | NOAA-20 | TASSO FRAGOSO | MARANHÃO | Brasil | 2112001 | 21 | 33 | nan | nan | nan | Cerrado | 2.7 |
| ff227cd6-abe2-30d6-a2a9-8694f6c1f7bf | -9.66262 | -45.12584 | 2026-09-30 04:53:00 | NOAA-20 | MONTE ALEGRE DO PIAUÍ | PIAUÍ | Brasil | 2206605 | 22 | 33 | nan | nan | nan | Cerrado | 2.9 |
| 8af630fb-17a8-33ac-a09b-e9e23c3d8206 | -15.75331 | -46.03837 | 2026-09-30 04:53:00 | NOAA-20 | ARINOS | MINAS GERAIS | Brasil | 3104502 | 31 | 33 | nan | nan | nan | Cerrado | 2.1 |
| 3ed87a78-4b30-3929-8531-babc1e73390d | -11.41565 | -43.42416 | 2026-09-30 04:53:00 | NOAA-20 | BARRA | BAHIA | Brasil | 2902708 | 29 | 33 | nan | nan | nan | Cerrado | 5.7 |
| d137ac11-3a87-3405-808b-03f94cfd3f7d | -14.91344 | -51.8675 | 2026-09-30 04:53:00 | NOAA-20 | ARAGUAIANA | MATO GROSSO | Brasil | 5101001 | 51 | 33 | nan | nan | nan | Cerrado | 3.2 |
| 790b2729-306e-3a47-9610-f7a451d1f994 | -10.72272 | -44.42524 | 2026-09-30 04:53:00 | NOAA-20 | SANTA RITA DE CÁSSIA | BAHIA | Brasil | 2928406 | 29 | 33 | nan | nan | nan | Cerrado | 9.3 |
| 443777fc-3618-3395-853c-c275ed846069 | -4.34722 | -48.96927 | 2026-09-30 04:53:00 | NOAA-20 | GOIANÉSIA DO PARÁ | PARÁ | Brasil | 1503093 | 15 | 33 | nan | nan | nan | Amazônia | 2.4 |
| 68604503-b096-3d87-8d86-a0c21a9cc012 | -7.82722 | -45.81755 | 2026-09-30 04:53:00 | NOAA-20 | TASSO FRAGOSO | MARANHÃO | Brasil | 2112001 | 21 | 33 | nan | nan | nan | Cerrado | 5.6 |
| 1cc87e95-e6e2-3d9d-9a33-1114f8dd923c | -16.7184 | -49.33566 | 2026-09-30 04:53:00 | NOAA-20 | GOIÂNIA | GOIÁS | Brasil | 5208707 | 52 | 33 | nan | nan | nan | Cerrado | 0.4 |
| 4dacb241-6282-3103-8c90-10a34333bca3 | -7.70105 | -54.7922 | 2026-09-30 04:53:00 | NOAA-20 | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 1.0 |
| 13c18938-967b-36f0-af7a-cf87defb6a7e | -8.20449 | -45.45347 | 2026-09-30 04:53:00 | NOAA-20 | RIBEIRO GONÇALVES | PIAUÍ | Brasil | 2208908 | 22 | 33 | nan | nan | nan | Cerrado | 1.9 |
| 48c90b29-ed52-3abe-b14e-18733a593a4c | -3.2468 | -50.80722 | 2026-09-30 04:53:00 | NOAA-20 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 0.9 |
| 88b3cc95-ec22-3227-b2c8-164020d2881a | -7.49673 | -55.02845 | 2026-09-30 04:53:00 | NOAA-20 | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 2.6 |
| 40dd75c1-6812-3563-8e49-b27088c8a374 | -16.4937 | -52.57403 | 2026-09-30 04:53:00 | NOAA-20 | BALIZA | GOIÁS | Brasil | 5203104 | 52 | 33 | nan | nan | nan | Cerrado | 0.7 |
| 5b4d1a62-c2eb-32c4-b2b6-daf09bee0a7b | -2.91023 | -54.12523 | 2026-09-30 04:53:00 | NOAA-20 | SANTARÉM | PARÁ | Brasil | 1506807 | 15 | 33 | nan | nan | nan | Amazônia | 2.2 |
| 1bdf3876-3837-32a5-865f-c6ed331677aa | -7.63888 | -45.51167 | 2026-09-30 04:53:00 | NOAA-20 | SAMBAÍBA | MARANHÃO | Brasil | 2109700 | 21 | 33 | nan | nan | nan | Cerrado | 1.4 |
| c2366431-a602-3259-83b3-34d45ec4091b | -11.43577 | -43.43341 | 2026-09-30 04:53:00 | NOAA-20 | BARRA | BAHIA | Brasil | 2902708 | 29 | 33 | nan | nan | nan | Cerrado | 1.9 |
| 8fb518e4-80d9-3656-bb37-ff3bab6f8df7 | -5.97977 | -53.54871 | 2026-09-30 04:53:00 | NOAA-20 | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 0.8 |
| 21cd11de-9108-3ba3-b1e6-4056da3e115f | -3.15821 | -54.09861 | 2026-09-30 04:53:00 | NOAA-20 | SANTARÉM | PARÁ | Brasil | 1506807 | 15 | 33 | nan | nan | nan | Amazônia | 3.6 |
| d3a5fd2a-9171-35b8-aad9-837625808e93 | -3.81794 | -50.63287 | 2026-09-30 04:53:00 | NOAA-20 | PACAJÁ | PARÁ | Brasil | 1505486 | 15 | 33 | nan | nan | nan | Amazônia | 0.8 |
| d61d5002-3069-3708-9d18-2272b92ad393 | -8.98059 | -44.17827 | 2026-09-30 04:53:00 | NOAA-20 | SANTA LUZ | PIAUÍ | Brasil | 2209302 | 22 | 33 | nan | nan | nan | Cerrado | 2.3 |
| 9123cbc6-552a-3221-9e78-8510735ca702 | -10.6638 | -50.74261 | 2026-09-30 04:53:00 | NOAA-20 | LUCIARA | MATO GROSSO | Brasil | 5105309 | 51 | 33 | nan | nan | nan | Cerrado | 1.8 |
| 40265ff0-eaf3-3fc7-8edc-82ebb7ea0f0c | -10.2114 | -49.97385 | 2026-09-30 04:53:00 | NOAA-20 | PIUM | TOCANTINS | Brasil | 1717503 | 17 | 33 | nan | nan | nan | Cerrado | 1.1 |
| 3ccc5d5f-d945-306d-9cbf-3770731292ed | -7.82211 | -45.82103 | 2026-09-30 04:53:00 | NOAA-20 | TASSO FRAGOSO | MARANHÃO | Brasil | 2112001 | 21 | 33 | nan | nan | nan | Cerrado | 4.6 |
| 62b0da14-031d-3ac6-b54f-75445c72d5e0 | -4.81051 | -45.64185 | 2026-09-30 04:53:00 | NOAA-20 | MARAJÁ DO SENA | MARANHÃO | Brasil | 2106359 | 21 | 33 | nan | nan | nan | Amazônia | 3.8 |
| 5d5ff375-c9b9-349b-a9ca-08984b62a940 | -3.37741 | -50.94829 | 2026-09-30 04:53:00 | NOAA-20 | PACAJÁ | PARÁ | Brasil | 1505486 | 15 | 33 | nan | nan | nan | Amazônia | 4.0 |
| b6c05b2a-913d-33ce-bb29-115673b8b281 | -9.92825 | -50.15461 | 2026-09-30 04:53:00 | NOAA-20 | PIUM | TOCANTINS | Brasil | 1717503 | 17 | 33 | nan | nan | nan | Cerrado | 9.2 |
| 89dfe4e9-957a-3c27-8898-ec70938d688d | -11.67072 | -44.51458 | 2026-09-30 04:53:00 | NOAA-20 | COTEGIPE | BAHIA | Brasil | 2909406 | 29 | 33 | nan | nan | nan | Cerrado | 2.2 |
| 5d894d25-d85f-3a77-8f35-ff2f750262b9 | -6.74908 | -55.08454 | 2026-09-30 04:53:00 | NOAA-20 | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 1.3 |
| d36634fd-95df-3bc5-8855-c69e92150953 | -8.30079 | -54.70861 | 2026-09-30 04:53:00 | NOAA-20 | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 1.2 |
| 53e9dfa3-9275-3591-8e55-e908374484c2 | -8.32187 | -54.75894 | 2026-09-30 04:53:00 | NOAA-20 | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 1.8 |
| 6b5906f3-3723-3c93-ad55-2c2a9f045ea5 | -7.51301 | -47.33837 | 2026-09-30 04:53:00 | NOAA-20 | CAROLINA | MARANHÃO | Brasil | 2102804 | 21 | 33 | nan | nan | nan | Cerrado | 2.3 |
| 9f871ee1-da42-3e64-85b6-d80b91de9d03 | -16.71765 | -49.33177 | 2026-09-30 04:53:00 | NOAA-20 | GOIÂNIA | GOIÁS | Brasil | 5208707 | 52 | 33 | nan | nan | nan | Cerrado | 0.8 |
| 83e05a1b-7e00-3e92-a64d-be6b78d7ae7c | -14.40328 | -51.28924 | 2026-09-30 04:53:00 | NOAA-20 | COCALINHO | MATO GROSSO | Brasil | 5103106 | 51 | 33 | nan | nan | nan | Cerrado | 0.9 |
| 2d467e66-4084-30b2-9acd-73757e0ac9bf | -11.39381 | -43.47067 | 2026-09-30 04:53:00 | NOAA-20 | BARRA | BAHIA | Brasil | 2902708 | 29 | 33 | nan | nan | nan | Cerrado | 3.9 |
| ff3ee313-0e4f-355c-ace9-a0fea9b8ee3f | -14.89718 | -51.86111 | 2026-09-30 04:53:00 | NOAA-20 | ARAGUAIANA | MATO GROSSO | Brasil | 5101001 | 51 | 33 | nan | nan | nan | Cerrado | 3.6 |
| 8a5d0cae-99d3-3cb6-89cd-890b01b4f675 | -6.38191 | -45.80775 | 2026-09-30 04:53:00 | NOAA-20 | FERNANDO FALCÃO | MARANHÃO | Brasil | 2104081 | 21 | 33 | nan | nan | nan | Cerrado | 1.2 |
| a83b9b3c-bd05-30d0-a4f4-18950f9c1da5 | -6.11154 | -53.09834 | 2026-09-30 04:53:00 | NOAA-20 | SÃO FÉLIX DO XINGU | PARÁ | Brasil | 1507300 | 15 | 33 | nan | nan | nan | Amazônia | 1.7 |
| 3efff857-0520-3af2-bf70-ac7faaf46d3e | -15.83374 | -42.56278 | 2026-09-30 04:53:00 | NOAA-20 | RIO PARDO DE MINAS | MINAS GERAIS | Brasil | 3155603 | 31 | 33 | nan | nan | nan | Mata Atlântica | 3.4 |
| 525ca973-14b6-3132-b92b-048279943ddc | -11.71681 | -43.4472 | 2026-09-30 04:53:00 | NOAA-20 | BARRA | BAHIA | Brasil | 2902708 | 29 | 33 | nan | nan | nan | Cerrado | 1.0 |
| db4de924-e86f-3112-be50-79d5cf2254cc | -6.9252 | -44.56185 | 2026-09-30 04:53:00 | NOAA-20 | SÃO DOMINGOS DO AZEITÃO | MARANHÃO | Brasil | 2110658 | 21 | 33 | nan | nan | nan | Cerrado | 5.4 |
| 3649731e-9345-3cc8-9118-990a1840d0a5 | -17.1003 | -46.47154 | 2026-09-30 04:53:00 | NOAA-20 | PARACATU | MINAS GERAIS | Brasil | 3147006 | 31 | 33 | nan | nan | nan | Cerrado | 1.9 |
| 54dda380-6a91-3a48-9da0-201ea686e605 | -6.33022 | -51.15887 | 2026-09-30 04:53:00 | NOAA-20 | SÃO FÉLIX DO XINGU | PARÁ | Brasil | 1507300 | 15 | 33 | nan | nan | nan | Amazônia | 1.0 |
| 96c547a8-f667-3395-ba6d-395cdabc9226 | -5.86964 | -50.16051 | 2026-09-30 04:53:00 | NOAA-20 | MARABÁ | PARÁ | Brasil | 1504208 | 15 | 33 | nan | nan | nan | Amazônia | 11.2 |
| d3b9f9de-e07c-34d7-b03c-b1df2edb9b6f | -4.35817 | -47.77425 | 2026-09-30 04:53:00 | NOAA-20 | DOM ELISEU | PARÁ | Brasil | 1502939 | 15 | 33 | nan | nan | nan | Amazônia | 5.4 |
| eafa3d2b-5d47-33e0-bea0-5dd0038d553e | -7.01413 | -45.29867 | 2026-09-30 04:53:00 | NOAA-20 | SAMBAÍBA | MARANHÃO | Brasil | 2109700 | 21 | 33 | nan | nan | nan | Cerrado | 2.2 |
| 85f226bf-aa6d-36ab-a178-ba3c1551ad3b | -3.37631 | -50.95519 | 2026-09-30 04:53:00 | NOAA-20 | PACAJÁ | PARÁ | Brasil | 1505486 | 15 | 33 | nan | nan | nan | Amazônia | 4.1 |
| 1041f609-814c-305d-bfe2-6841cfa5ab5b | -11.42571 | -43.42878 | 2026-09-30 04:53:00 | NOAA-20 | BARRA | BAHIA | Brasil | 2902708 | 29 | 33 | nan | nan | nan | Cerrado | 2.0 |
| 204d2016-8408-359e-8d70-aa153fd3456f | -9.67079 | -54.34691 | 2026-09-30 04:53:00 | NOAA-20 | GUARANTÃ DO NORTE | MATO GROSSO | Brasil | 5104104 | 51 | 33 | nan | nan | nan | Amazônia | 2.1 |
| 29c943a0-d5d7-3994-9f61-304bb3bb816d | -8.32695 | -51.31315 | 2026-09-30 04:53:00 | NOAA-20 | CUMARU DO NORTE | PARÁ | Brasil | 1502764 | 15 | 33 | nan | nan | nan | Amazônia | 0.9 |
| 970b5c50-774c-34f4-a3a6-9368d758b052 | -6.3655 | -46.25772 | 2026-09-30 04:53:00 | NOAA-20 | FORMOSA DA SERRA NEGRA | MARANHÃO | Brasil | 2104099 | 21 | 33 | nan | nan | nan | Cerrado | 1.2 |
| 6ec92cec-9e15-3be2-b1f8-748e01e57971 | -5.72306 | -43.28353 | 2026-09-30 04:53:00 | NOAA-20 | PARNARAMA | MARANHÃO | Brasil | 2107803 | 21 | 33 | nan | nan | nan | Cerrado | 1.9 |
| 41f92dc7-1c90-3d89-abd2-29f79ead5f4c | -5.98832 | -53.54899 | 2026-09-30 04:53:00 | NOAA-20 | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 0.9 |
| 5c96418d-05c4-335b-be88-9fc2158b679e | -7.83089 | -45.82207 | 2026-09-30 04:53:00 | NOAA-20 | TASSO FRAGOSO | MARANHÃO | Brasil | 2112001 | 21 | 33 | nan | nan | nan | Cerrado | 9.3 |
| 2cafd4df-d2c1-3ab1-b75b-5dabdb28f108 | -11.35533 | -43.35209 | 2026-09-30 04:53:00 | NOAA-20 | BARRA | BAHIA | Brasil | 2902708 | 29 | 33 | nan | nan | nan | Cerrado | 1.8 |
| 2bbcca8e-a3e9-3359-a7f1-7be5a30f0e65 | -5.75632 | -45.1648 | 2026-09-30 04:53:00 | NOAA-20 | BARRA DO CORDA | MARANHÃO | Brasil | 2101608 | 21 | 33 | nan | nan | nan | Cerrado | 4.6 |
| 16743c5a-0564-38cc-81e1-9275326fb1e2 | -5.86345 | -51.78725 | 2026-09-30 04:53:00 | NOAA-20 | SÃO FÉLIX DO XINGU | PARÁ | Brasil | 1507300 | 15 | 33 | nan | nan | nan | Amazônia | 0.9 |
| d62d0df9-b7ea-33db-8448-5aad77cc0dd5 | -9.81425 | -48.21618 | 2026-09-30 04:53:00 | NOAA-20 | TOCANTÍNIA | TOCANTINS | Brasil | 1721109 | 17 | 33 | nan | nan | nan | Cerrado | 1.9 |
| c1570a16-6730-3d00-a567-f06e0764d2af | -6.92587 | -44.55736 | 2026-09-30 04:53:00 | NOAA-20 | SÃO DOMINGOS DO AZEITÃO | MARANHÃO | Brasil | 2110658 | 21 | 33 | nan | nan | nan | Cerrado | 5.4 |
| 1d9404d0-317b-3e62-8230-1189c5f476f4 | -10.57791 | -50.85189 | 2026-09-30 04:53:00 | NOAA-20 | SANTA TEREZINHA | MATO GROSSO | Brasil | 5107776 | 51 | 33 | nan | nan | nan | Cerrado | 0.8 |
| 00afeebb-d89e-3d9e-9bd1-2f111c775044 | -4.02142 | -54.20175 | 2026-09-30 04:53:00 | NOAA-20 | PLACAS | PARÁ | Brasil | 1505650 | 15 | 33 | nan | nan | nan | Amazônia | 2.4 |


[Clique aqui para ver as próximas entradas](README45.md)
