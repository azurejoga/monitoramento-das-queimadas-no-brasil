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

## Dados Diários - Página 21

| ID | Latitude | Longitude | Data/Hora GMT | Satélite | Município | Estado | País | Município ID | Estado ID | País ID | Dias sem Chuva | Precipitação | Risco de Fogo | Bioma | FRP |
|----|----------|-----------|---------------|----------|-----------|--------|------|--------------|-----------|---------|----------------|--------------|----------------|-------|-----|
| b46b87d1-09f1-3cc2-bbed-0abe969cbd9f | -11.54 | -52.119 | 2025-08-26 02:10:00 | GOES-19 | SÃO FÉLIX DO ARAGUAIA | MATO GROSSO | Brasil | 5107859 | 51 | 33 | nan | nan | nan | Amazônia | 150.3 |
| 1e90c0e9-98e8-3421-a750-d5e53a13d041 | -7.3854 | -64.3662 | 2025-08-26 02:10:00 | GOES-19 | CANUTAMA | AMAZONAS | Brasil | 1300904 | 13 | 33 | nan | nan | nan | Amazônia | 78.2 |
| 60acf25f-27ea-3a38-9cd9-726ec8227016 | -6.2275 | -60.018 | 2025-08-26 02:10:00 | GOES-19 | NOVO ARIPUANÃ | AMAZONAS | Brasil | 1303304 | 13 | 33 | nan | nan | nan | Amazônia | 70.6 |
| d968beec-3266-36c8-8c9d-0fbc47c66284 | -11.5397 | -52.14 | 2025-08-26 02:10:00 | GOES-19 | SÃO FÉLIX DO ARAGUAIA | MATO GROSSO | Brasil | 5107859 | 51 | 33 | nan | nan | nan | Amazônia | 131.9 |
| 9913794c-458f-359d-a878-34ed34dd8afe | -12.6741 | -47.8589 | 2025-08-26 02:10:00 | GOES-19 | PARANÃ | TOCANTINS | Brasil | 1716208 | 17 | 33 | nan | nan | nan | Cerrado | 56.8 |
| 94d0fb0d-95e2-3892-87be-5bc6f4f7eda8 | -9.1909 | -59.4619 | 2025-08-26 02:10:00 | GOES-19 | COLNIZA | MATO GROSSO | Brasil | 5103254 | 51 | 33 | nan | nan | nan | Amazônia | 70.7 |
| 5f070f97-756e-3855-807f-c5ee58249be7 | -11.1587 | -44.7627 | 2025-08-26 02:10:00 | GOES-19 | SANTA RITA DE CÁSSIA | BAHIA | Brasil | 2928406 | 29 | 33 | nan | nan | nan | Cerrado | 344.5 |
| d8c32a72-6f5b-36cd-a24d-935855f45821 | -8.9874 | -65.4192 | 2025-08-26 02:20:00 | GOES-19 | LÁBREA | AMAZONAS | Brasil | 1302405 | 13 | 33 | nan | nan | nan | Amazônia | 48.7 |
| e2abeaac-7f12-36cc-8ff7-ac3cae2d6538 | -6.8044 | -58.9568 | 2025-08-26 02:20:00 | GOES-19 | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 100.0 |
| c474f2fc-e1d0-341f-bc0b-3465285b1fc1 | -9.1909 | -59.4619 | 2025-08-26 02:20:00 | GOES-19 | COLNIZA | MATO GROSSO | Brasil | 5103254 | 51 | 33 | nan | nan | nan | Amazônia | 62.5 |
| ae111c5c-dbb0-3f5f-8478-1eb248f12326 | -6.8229 | -58.956 | 2025-08-26 02:20:00 | GOES-19 | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 175.9 |
| 2f620267-413d-3aa9-98f0-3e9a5c7c0094 | -9.1722 | -59.4629 | 2025-08-26 02:20:00 | GOES-19 | COLNIZA | MATO GROSSO | Brasil | 5103254 | 51 | 33 | nan | nan | nan | Amazônia | 68.6 |
| 82084b6f-a399-36a6-9bd4-95501584f597 | -6.8228 | -58.9753 | 2025-08-26 02:20:00 | GOES-19 | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 262.8 |
| 3ef6c496-3d73-3e08-b8ad-93e381827d04 | -8.855 | -62.4313 | 2025-08-26 02:20:00 | GOES-19 | CUJUBIM | RONDÔNIA | Brasil | 1100940 | 11 | 33 | nan | nan | nan | Amazônia | 76.2 |
| a0b4c1bd-ce19-3f82-8aca-81fd40e6bd84 | -11.1396 | -44.7654 | 2025-08-26 02:20:00 | GOES-19 | SANTA RITA DE CÁSSIA | BAHIA | Brasil | 2928406 | 29 | 33 | nan | nan | nan | Cerrado | 68.3 |
| c3fd82e3-908d-3a2e-ade9-589099272f7c | -8.8734 | -62.4495 | 2025-08-26 02:20:00 | GOES-19 | CUJUBIM | RONDÔNIA | Brasil | 1100940 | 11 | 33 | nan | nan | nan | Amazônia | 55.9 |
| 27cc2721-6f48-327f-a3ff-a001fe8398d3 | -8.9873 | -65.4379 | 2025-08-26 02:20:00 | GOES-19 | LÁBREA | AMAZONAS | Brasil | 1302405 | 13 | 33 | nan | nan | nan | Amazônia | 44.9 |
| 997f9826-ba2f-35a3-8ced-3e7e41007b33 | -6.2459 | -60.0174 | 2025-08-26 02:20:00 | GOES-19 | NOVO ARIPUANÃ | AMAZONAS | Brasil | 1303304 | 13 | 33 | nan | nan | nan | Amazônia | 113.8 |
| 06976967-bebb-322f-a432-b66a8fab9233 | -8.3209 | -50.5667 | 2025-08-26 02:20:00 | GOES-19 | SANTA MARIA DAS BARREIRAS | PARÁ | Brasil | 1506583 | 15 | 33 | nan | nan | nan | Amazônia | 51.0 |
| 26276565-22e0-35b5-80ac-80fd84c46c80 | -11.2937 | -55.1129 | 2025-08-26 02:20:00 | GOES-19 | CLÁUDIA | MATO GROSSO | Brasil | 5103056 | 51 | 33 | nan | nan | nan | Amazônia | 49.6 |
| f018c9c2-fbe9-3b81-a74b-9ccd463e4668 | -7.3854 | -64.3662 | 2025-08-26 02:20:00 | GOES-19 | CANUTAMA | AMAZONAS | Brasil | 1300904 | 13 | 33 | nan | nan | nan | Amazônia | 63.9 |
| 605d7c3f-0cff-32ad-83c4-69e54f22c76e | -11.5397 | -52.14 | 2025-08-26 02:20:00 | GOES-19 | SÃO FÉLIX DO ARAGUAIA | MATO GROSSO | Brasil | 5107859 | 51 | 33 | nan | nan | nan | Amazônia | 106.4 |
| 20de6f61-65d1-3ab5-af75-460aa920419d | -11.54 | -52.119 | 2025-08-26 02:20:00 | GOES-19 | SÃO FÉLIX DO ARAGUAIA | MATO GROSSO | Brasil | 5107859 | 51 | 33 | nan | nan | nan | Amazônia | 115.0 |
| 5fa87f7e-27bc-3cca-88d8-97a632a133c3 | -11.6351 | -44.8561 | 2025-08-26 02:20:00 | GOES-19 | RIACHÃO DAS NEVES | BAHIA | Brasil | 2926202 | 29 | 33 | nan | nan | nan | Cerrado | 75.2 |
| 7d0c94b6-3adc-35ee-9985-d78d462ac4bb | -6.8412 | -58.9746 | 2025-08-26 02:20:00 | GOES-19 | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 74.2 |
| dd90b8b8-a415-3ec4-af36-bed9ba4dda94 | -6.9128 | -59.3578 | 2025-08-26 02:20:00 | GOES-19 | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 46.6 |
| 1d8e99f8-bacf-37f5-b968-1ec2c6396f09 | -8.8548 | -62.4503 | 2025-08-26 02:20:00 | GOES-19 | CUJUBIM | RONDÔNIA | Brasil | 1100940 | 11 | 33 | nan | nan | nan | Amazônia | 186.2 |
| fe50ed33-2d5a-3cf9-afcf-4d2100672b32 | -7.367 | -64.348 | 2025-08-26 02:20:00 | GOES-19 | CANUTAMA | AMAZONAS | Brasil | 1300904 | 13 | 33 | nan | nan | nan | Amazônia | 56.9 |
| 88bb78a7-ac4c-3b5f-b8c2-057cbf824bf5 | -11.5587 | -52.138 | 2025-08-26 02:20:00 | GOES-19 | SÃO FÉLIX DO ARAGUAIA | MATO GROSSO | Brasil | 5107859 | 51 | 33 | nan | nan | nan | Amazônia | 75.5 |
| 78984401-7b45-3d67-b69a-6bf89bc4f526 | -6.8043 | -58.9761 | 2025-08-26 02:20:00 | GOES-19 | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 151.4 |
| 0eda9be2-ab39-3a53-95ab-d99debfa4032 | -11.1583 | -44.7859 | 2025-08-26 02:20:00 | GOES-19 | SANTA RITA DE CÁSSIA | BAHIA | Brasil | 2928406 | 29 | 33 | nan | nan | nan | Cerrado | 65.7 |
| 49198af0-eb37-30ea-ae63-c12fec2c5f81 | -10.4241 | -64.3903 | 2025-08-26 02:20:00 | GOES-19 | NOVA MAMORÉ | RONDÔNIA | Brasil | 1100338 | 11 | 33 | nan | nan | nan | Amazônia | 34.8 |
| 33e933bf-ad49-3ddf-9a34-5dec02e879d1 | -9.023 | -65.7355 | 2025-08-26 02:20:00 | GOES-19 | LÁBREA | AMAZONAS | Brasil | 1302405 | 13 | 33 | nan | nan | nan | Amazônia | 36.0 |
| 936e6ade-a88e-3bff-88fe-f55a86848090 | -6.246 | -59.9982 | 2025-08-26 02:20:00 | GOES-19 | NOVO ARIPUANÃ | AMAZONAS | Brasil | 1303304 | 13 | 33 | nan | nan | nan | Amazônia | 57.4 |
| 9519fb99-cecd-3a82-b628-4fa92990928b | -9.1724 | -59.4436 | 2025-08-26 02:20:00 | GOES-19 | COLNIZA | MATO GROSSO | Brasil | 5103254 | 51 | 33 | nan | nan | nan | Amazônia | 52.4 |
| 2182998a-c5f3-3e0d-a1d5-3640a3a5bd49 | -11.559 | -52.117 | 2025-08-26 02:20:00 | GOES-19 | SÃO FÉLIX DO ARAGUAIA | MATO GROSSO | Brasil | 5107859 | 51 | 33 | nan | nan | nan | Amazônia | 118.6 |
| b4cfa1b6-1895-3c95-997d-764f7afd5f73 | -6.8413 | -58.9552 | 2025-08-26 02:20:00 | GOES-19 | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 65.0 |
| ba401a3f-e5fb-3aae-b53a-bca5bf269301 | -14.2876 | -49.1291 | 2025-08-26 02:20:00 | GOES-19 | CAMPINORTE | GOIÁS | Brasil | 5204706 | 52 | 33 | nan | nan | nan | Cerrado | 47.8 |
| f095b992-5068-303a-8c8f-07f702c94320 | -8.8363 | -62.451 | 2025-08-26 02:20:00 | GOES-19 | CUJUBIM | RONDÔNIA | Brasil | 1100940 | 11 | 33 | nan | nan | nan | Amazônia | 76.4 |
| 2e968fd7-1e8c-30fe-b20c-2c8b95c3f5c6 | -11.1591 | -44.7395 | 2025-08-26 02:20:00 | GOES-19 | SANTA RITA DE CÁSSIA | BAHIA | Brasil | 2928406 | 29 | 33 | nan | nan | nan | Cerrado | 153.6 |
| b9ff66ed-0464-33c3-853d-da9b9ee40bf9 | -7.3854 | -64.3475 | 2025-08-26 02:20:00 | GOES-19 | CANUTAMA | AMAZONAS | Brasil | 1300904 | 13 | 33 | nan | nan | nan | Amazônia | 100.4 |
| 7948d1f6-14d3-37a5-ad1d-42694fea4206 | -6.2275 | -60.018 | 2025-08-26 02:20:00 | GOES-19 | NOVO ARIPUANÃ | AMAZONAS | Brasil | 1303304 | 13 | 33 | nan | nan | nan | Amazônia | 58.0 |
| 15595c13-2c89-3520-b5fc-b4e740b16b97 | -11.1587 | -44.7627 | 2025-08-26 02:20:00 | GOES-19 | SANTA RITA DE CÁSSIA | BAHIA | Brasil | 2928406 | 29 | 33 | nan | nan | nan | Cerrado | 328.0 |
| fa9cecc9-bd54-3862-ab8b-12ee3713b19f | -7.3541 | -59.6669 | 2025-08-26 02:20:00 | GOES-19 | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 49.4 |
| ff644652-56f4-377f-b4cf-0f6107c64f36 | -4.9605 | -55.8226 | 2025-08-26 02:20:00 | GOES-19 | TRAIRÃO | PARÁ | Brasil | 1508050 | 15 | 33 | nan | nan | nan | Amazônia | 59.6 |
| 728d2668-0e30-3821-af5b-d5dd46c09610 | -9.191 | -59.4425 | 2025-08-26 02:20:00 | GOES-19 | COLNIZA | MATO GROSSO | Brasil | 5103254 | 51 | 33 | nan | nan | nan | Amazônia | 60.6 |
| 42491860-a23b-3405-96b2-5dafc572960b | -9.191 | -59.4425 | 2025-08-26 02:30:00 | GOES-19 | COLNIZA | MATO GROSSO | Brasil | 5103254 | 51 | 33 | nan | nan | nan | Amazônia | 53.9 |
| 3f645a81-ba91-3209-8ef5-1e40a6160d74 | -10.4241 | -64.3903 | 2025-08-26 02:30:00 | GOES-19 | NOVA MAMORÉ | RONDÔNIA | Brasil | 1100338 | 11 | 33 | nan | nan | nan | Amazônia | 36.8 |
| 32aa0a92-b8db-3532-804c-3978a37576c0 | -11.1587 | -44.7627 | 2025-08-26 02:30:00 | GOES-19 | SANTA RITA DE CÁSSIA | BAHIA | Brasil | 2928406 | 29 | 33 | nan | nan | nan | Cerrado | 228.2 |
| f6b5a07b-27fb-3c8b-9e6d-50e088b7336a | -6.7636 | -59.6526 | 2025-08-26 02:30:00 | GOES-19 | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 37.8 |
| 0d2382a5-d62c-3c67-9d39-b40a577effa6 | -7.3854 | -64.3475 | 2025-08-26 02:30:00 | GOES-19 | CANUTAMA | AMAZONAS | Brasil | 1300904 | 13 | 33 | nan | nan | nan | Amazônia | 98.7 |
| ca0f22f5-c731-3401-b70a-725d0e65a933 | -6.8229 | -58.956 | 2025-08-26 02:30:00 | GOES-19 | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 210.7 |
| 6415d24b-9f62-3d27-a443-c9f57f580e8f | -11.54 | -52.119 | 2025-08-26 02:30:00 | GOES-19 | SÃO FÉLIX DO ARAGUAIA | MATO GROSSO | Brasil | 5107859 | 51 | 33 | nan | nan | nan | Amazônia | 109.6 |
| e99b5288-19c5-3e2c-a5e6-ad8bcc518358 | -8.855 | -62.4313 | 2025-08-26 02:30:00 | GOES-19 | CUJUBIM | RONDÔNIA | Brasil | 1100940 | 11 | 33 | nan | nan | nan | Amazônia | 73.3 |
| 6f70b2fe-f83c-310d-a895-a869818bc69e | -8.8363 | -62.451 | 2025-08-26 02:30:00 | GOES-19 | CUJUBIM | RONDÔNIA | Brasil | 1100940 | 11 | 33 | nan | nan | nan | Amazônia | 89.0 |
| 10e1b776-b172-30a4-83ca-23626fe211b5 | -11.1591 | -44.7395 | 2025-08-26 02:30:00 | GOES-19 | SANTA RITA DE CÁSSIA | BAHIA | Brasil | 2928406 | 29 | 33 | nan | nan | nan | Cerrado | 112.3 |
| 162ccbb9-5410-3744-a0af-75aeb5d24999 | -6.7819 | -59.6711 | 2025-08-26 02:30:00 | GOES-19 | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 48.7 |
| cad2b16f-1cee-3546-b239-200767df9b38 | -9.1724 | -59.4436 | 2025-08-26 02:30:00 | GOES-19 | COLNIZA | MATO GROSSO | Brasil | 5103254 | 51 | 33 | nan | nan | nan | Amazônia | 56.4 |
| 782504a1-6b3b-3346-9914-644edd878615 | -6.8412 | -58.9746 | 2025-08-26 02:30:00 | GOES-19 | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 56.9 |
| d611e5bb-c39b-34de-815d-3b96480718bc | -8.9873 | -65.4379 | 2025-08-26 02:30:00 | GOES-19 | LÁBREA | AMAZONAS | Brasil | 1302405 | 13 | 33 | nan | nan | nan | Amazônia | 47.9 |
| 49d3cbd1-0c69-357e-9568-d42317c334a3 | -9.1722 | -59.4629 | 2025-08-26 02:30:00 | GOES-19 | COLNIZA | MATO GROSSO | Brasil | 5103254 | 51 | 33 | nan | nan | nan | Amazônia | 75.9 |
| 00c1b805-ea7a-3b29-a53e-db9cc21fb8d6 | -12.7455 | -48.1597 | 2025-08-26 02:30:00 | GOES-19 | PARANÃ | TOCANTINS | Brasil | 1716208 | 17 | 33 | nan | nan | nan | Cerrado | 82.7 |
| 1b9f37a2-7aca-33d3-ab26-7794d65cce27 | -4.9605 | -55.8226 | 2025-08-26 02:30:00 | GOES-19 | TRAIRÃO | PARÁ | Brasil | 1508050 | 15 | 33 | nan | nan | nan | Amazônia | 81.7 |
| abcf80a4-480c-30d9-b37a-8e6fe9b85815 | -6.8044 | -58.9568 | 2025-08-26 02:30:00 | GOES-19 | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 67.2 |
| 6ade0bb7-54c2-3e0a-9778-104a20011cfd | -6.8043 | -58.9761 | 2025-08-26 02:30:00 | GOES-19 | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 88.7 |
| dca706df-8329-3fad-acfc-d1e482567e86 | -6.7476 | -62.8664 | 2025-08-26 02:30:00 | GOES-19 | HUMAITÁ | AMAZONAS | Brasil | 1301704 | 13 | 33 | nan | nan | nan | Amazônia | 59.2 |
| 07fe6044-83f1-3c51-98d3-8f5f326d4564 | -11.5587 | -52.138 | 2025-08-26 02:30:00 | GOES-19 | SÃO FÉLIX DO ARAGUAIA | MATO GROSSO | Brasil | 5107859 | 51 | 33 | nan | nan | nan | Amazônia | 70.4 |
| 4b25e498-118f-3afe-973a-6208b4b41fb9 | -9.0415 | -65.7349 | 2025-08-26 02:30:00 | GOES-19 | LÁBREA | AMAZONAS | Brasil | 1302405 | 13 | 33 | nan | nan | nan | Amazônia | 38.4 |
| 4c8b6322-023b-394f-aca2-159a7621350a | -8.3396 | -50.5652 | 2025-08-26 02:30:00 | GOES-19 | SANTA MARIA DAS BARREIRAS | PARÁ | Brasil | 1506583 | 15 | 33 | nan | nan | nan | Amazônia | 44.3 |
| 57830b31-9d63-3714-9bc3-011c128b0730 | -11.5397 | -52.14 | 2025-08-26 02:30:00 | GOES-19 | SÃO FÉLIX DO ARAGUAIA | MATO GROSSO | Brasil | 5107859 | 51 | 33 | nan | nan | nan | Amazônia | 92.8 |
| 4a0e43db-c6e4-308b-8034-da94e18ccb26 | -6.7635 | -59.6718 | 2025-08-26 02:30:00 | GOES-19 | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 79.5 |
| c7766c53-2c96-3994-b443-589ae329e69b | -11.6351 | -44.8561 | 2025-08-26 02:30:00 | GOES-19 | RIACHÃO DAS NEVES | BAHIA | Brasil | 2926202 | 29 | 33 | nan | nan | nan | Cerrado | 67.0 |
| 5ee31b83-5103-3306-b253-62cad0e9b192 | -11.559 | -52.117 | 2025-08-26 02:30:00 | GOES-19 | SÃO FÉLIX DO ARAGUAIA | MATO GROSSO | Brasil | 5107859 | 51 | 33 | nan | nan | nan | Amazônia | 106.2 |
| ab1b8fd4-5210-33f8-8f82-93d4108bcbeb | -7.3854 | -64.3662 | 2025-08-26 02:30:00 | GOES-19 | CANUTAMA | AMAZONAS | Brasil | 1300904 | 13 | 33 | nan | nan | nan | Amazônia | 58.7 |
| c1cc5e4e-7017-3c4c-8834-554dbcd0a2f1 | -8.9874 | -65.4192 | 2025-08-26 02:30:00 | GOES-19 | LÁBREA | AMAZONAS | Brasil | 1302405 | 13 | 33 | nan | nan | nan | Amazônia | 47.6 |
| da154d48-d490-3473-a586-6b9baff55240 | -9.006 | -65.4 | 2025-08-26 02:30:00 | GOES-19 | LÁBREA | AMAZONAS | Brasil | 1302405 | 13 | 33 | nan | nan | nan | Amazônia | 38.0 |
| 598ddcdf-af0a-36f2-a12f-7568b8bbeca4 | -6.8413 | -58.9552 | 2025-08-26 02:30:00 | GOES-19 | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 72.2 |
| 381844da-4994-3e99-84f3-c3e480d596b6 | -6.2275 | -60.018 | 2025-08-26 02:30:00 | GOES-19 | NOVO ARIPUANÃ | AMAZONAS | Brasil | 1303304 | 13 | 33 | nan | nan | nan | Amazônia | 63.7 |
| e3d79a9f-048b-3b0e-a985-0f8dfcfeaf38 | -6.8228 | -58.9753 | 2025-08-26 02:30:00 | GOES-19 | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 288.3 |
| 54f61f5e-e954-30f3-af5d-d2de2c3543c3 | -6.2459 | -60.0174 | 2025-08-26 02:30:00 | GOES-19 | NOVO ARIPUANÃ | AMAZONAS | Brasil | 1303304 | 13 | 33 | nan | nan | nan | Amazônia | 93.8 |
| 56afa318-a102-34af-951a-76f2d93c354f | -6.9128 | -59.3578 | 2025-08-26 02:30:00 | GOES-19 | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 54.2 |
| 3872d28d-3f27-3e83-9f96-6c4be502cda0 | -14.2876 | -49.1291 | 2025-08-26 02:30:00 | GOES-19 | CAMPINORTE | GOIÁS | Brasil | 5204706 | 52 | 33 | nan | nan | nan | Cerrado | 47.5 |
| 34f2fc0d-b2bb-3e2d-a9e0-f2bd069f521c | -8.8734 | -62.4495 | 2025-08-26 02:30:00 | GOES-19 | CUJUBIM | RONDÔNIA | Brasil | 1100940 | 11 | 33 | nan | nan | nan | Amazônia | 68.4 |
| b2f80895-7cd4-3de2-ad1c-e1591b2f89c2 | -8.8548 | -62.4503 | 2025-08-26 02:30:00 | GOES-19 | CUJUBIM | RONDÔNIA | Brasil | 1100940 | 11 | 33 | nan | nan | nan | Amazônia | 170.2 |
| b1648925-a729-36b4-98db-00c7fb334cde | -9.1909 | -59.4619 | 2025-08-26 02:30:00 | GOES-19 | COLNIZA | MATO GROSSO | Brasil | 5103254 | 51 | 33 | nan | nan | nan | Amazônia | 61.8 |
| 60aaf6e2-baff-3c91-8d1b-15a5ba7e871c | -4.9606 | -55.8028 | 2025-08-26 02:30:00 | GOES-19 | TRAIRÃO | PARÁ | Brasil | 1508050 | 15 | 33 | nan | nan | nan | Amazônia | 61.6 |
| 19be2298-b1a0-37a5-b24f-5005f2a83044 | -6.246 | -59.9982 | 2025-08-26 02:40:00 | GOES-19 | NOVO ARIPUANÃ | AMAZONAS | Brasil | 1303304 | 13 | 33 | nan | nan | nan | Amazônia | 58.5 |
| 3c6bed25-0b33-381a-9dde-b051512ea14d | -9.1724 | -59.4436 | 2025-08-26 02:40:00 | GOES-19 | COLNIZA | MATO GROSSO | Brasil | 5103254 | 51 | 33 | nan | nan | nan | Amazônia | 55.0 |
| 67959d50-f85d-398c-bd34-75063344163b | -6.8229 | -58.956 | 2025-08-26 02:40:00 | GOES-19 | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 185.7 |
| d10edd00-3046-370e-bba3-e607e5ac3c9d | -7.367 | -64.348 | 2025-08-26 02:40:00 | GOES-19 | CANUTAMA | AMAZONAS | Brasil | 1300904 | 13 | 33 | nan | nan | nan | Amazônia | 49.0 |
| 39af2cef-5af6-33b1-b4f9-b37b8d5cb49f | -7.3854 | -64.3662 | 2025-08-26 02:40:00 | GOES-19 | CANUTAMA | AMAZONAS | Brasil | 1300904 | 13 | 33 | nan | nan | nan | Amazônia | 49.9 |
| 855bb760-0e77-3cfe-b067-3d4bbc9738a6 | -6.7635 | -59.6718 | 2025-08-26 02:40:00 | GOES-19 | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 62.7 |
| 2c10f83f-d9ef-35b8-8808-484201b4dc20 | -6.2459 | -60.0174 | 2025-08-26 02:40:00 | GOES-19 | NOVO ARIPUANÃ | AMAZONAS | Brasil | 1303304 | 13 | 33 | nan | nan | nan | Amazônia | 109.8 |
| 78482ce0-dea3-3a97-a073-84ab68f8ea1d | -6.8044 | -58.9568 | 2025-08-26 02:40:00 | GOES-19 | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 67.0 |
| c8f16817-51b0-3dc8-98ef-4a17f9437514 | -14.2876 | -49.1291 | 2025-08-26 02:40:00 | GOES-19 | CAMPINORTE | GOIÁS | Brasil | 5204706 | 52 | 33 | nan | nan | nan | Cerrado | 67.9 |
| 2fe6ffc2-e481-32d0-88cc-42de95049339 | -11.1591 | -44.7395 | 2025-08-26 02:40:00 | GOES-19 | SANTA RITA DE CÁSSIA | BAHIA | Brasil | 2928406 | 29 | 33 | nan | nan | nan | Cerrado | 78.7 |
| 6eccdcd0-8993-3f6f-9204-2dbe20c9c55f | -7.3854 | -64.3475 | 2025-08-26 02:40:00 | GOES-19 | CANUTAMA | AMAZONAS | Brasil | 1300904 | 13 | 33 | nan | nan | nan | Amazônia | 76.0 |
| cee1a64d-0596-35ad-b3d9-e06e6e8f8608 | -11.1587 | -44.7627 | 2025-08-26 02:40:00 | GOES-19 | SANTA RITA DE CÁSSIA | BAHIA | Brasil | 2928406 | 29 | 33 | nan | nan | nan | Cerrado | 169.1 |
| fe6430f4-1d74-34df-b263-a46eea26cd20 | -11.54 | -52.119 | 2025-08-26 02:40:00 | GOES-19 | SÃO FÉLIX DO ARAGUAIA | MATO GROSSO | Brasil | 5107859 | 51 | 33 | nan | nan | nan | Amazônia | 96.7 |
| 646deced-0b67-35b3-b443-6caeceec3456 | -11.5397 | -52.14 | 2025-08-26 02:40:00 | GOES-19 | SÃO FÉLIX DO ARAGUAIA | MATO GROSSO | Brasil | 5107859 | 51 | 33 | nan | nan | nan | Amazônia | 66.2 |


[Clique aqui para ver as próximas entradas](README22.md)
