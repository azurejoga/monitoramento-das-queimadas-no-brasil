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

## Dados Diários - Página 5

| ID | Latitude | Longitude | Data/Hora GMT | Satélite | Município | Estado | País | Município ID | Estado ID | País ID | Dias sem Chuva | Precipitação | Risco de Fogo | Bioma | FRP |
|----|----------|-----------|---------------|----------|-----------|--------|------|--------------|-----------|---------|----------------|--------------|----------------|-------|-----|
| 8825bc11-5e71-3a13-98e2-585f2d44ac46 | -6.748 | -59.1523 | 2026-08-18 01:30:00 | GOES-19 | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 56.7 |
| 6a29c7bd-51c4-3763-9da9-981c5cf69c87 | -6.8596 | -58.9931 | 2026-08-18 01:30:00 | GOES-19 | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 54.7 |
| bf5f351c-136d-3046-ba3f-b4f4ba6492b8 | -8.2036 | -55.0228 | 2026-08-18 01:30:00 | GOES-19 | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 86.2 |
| 57d343c5-91f8-3ddf-afca-7ed93d0cd0df | -23.8208 | -51.9003 | 2026-08-18 01:30:00 | GOES-19 | SÃO PEDRO DO IVAÍ | PARANÁ | Brasil | 4125803 | 41 | 33 | nan | nan | nan | Mata Atlântica | 60.6 |
| 58f48e43-0ec8-367a-b9ec-16eabd79bcb8 | -8.5853 | -50.3543 | 2026-08-18 01:30:00 | GOES-19 | SANTA MARIA DAS BARREIRAS | PARÁ | Brasil | 1506583 | 15 | 33 | nan | nan | nan | Amazônia | 45.7 |
| ccecccea-1153-3562-b8a6-6722b119722e | -9.4257 | -60.416 | 2026-08-18 01:30:00 | GOES-19 | ARIPUANÃ | MATO GROSSO | Brasil | 5101407 | 51 | 33 | nan | nan | nan | Amazônia | 53.9 |
| 60cf197c-0166-3012-bd01-cbb1b98c0fa2 | -14.1628 | -52.9323 | 2026-08-18 01:30:00 | GOES-19 | ÁGUA BOA | MATO GROSSO | Brasil | 5100201 | 51 | 33 | nan | nan | nan | Cerrado | 61.9 |
| d6f4991a-4b49-36d4-bc6e-8a352bf5d7c7 | -14.1631 | -52.9113 | 2026-08-18 01:30:00 | GOES-19 | ÁGUA BOA | MATO GROSSO | Brasil | 5100201 | 51 | 33 | nan | nan | nan | Cerrado | 63.6 |
| e522f7cc-cb3e-33cd-8ebd-38fd77fff2a5 | -14.2759 | -51.9234 | 2026-08-18 01:30:00 | GOES-19 | NOVA NAZARÉ | MATO GROSSO | Brasil | 5106174 | 51 | 33 | nan | nan | nan | Cerrado | 67.8 |
| f4d32cfd-e991-3eae-a9f5-8b906bc6d69c | -8.9973 | -60.5147 | 2026-08-18 01:30:00 | GOES-19 | COLNIZA | MATO GROSSO | Brasil | 5103254 | 51 | 33 | nan | nan | nan | Amazônia | 80.3 |
| 93764b0f-1eca-3266-804d-3fbc991c97e8 | -10.8695 | -44.9415 | 2026-08-18 01:30:00 | GOES-19 | CRISTALÂNDIA DO PIAUÍ | PIAUÍ | Brasil | 2203008 | 22 | 33 | nan | nan | nan | Cerrado | 70.8 |
| d7bc05ea-247d-3823-a059-30a0d125f8be | -8.185 | -55.024 | 2026-08-18 01:30:00 | GOES-19 | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 54.9 |
| f9b9fc96-d838-3808-a9b8-3186314a3df6 | -17.1016 | -46.5808 | 2026-08-18 01:30:00 | GOES-19 | PARACATU | MINAS GERAIS | Brasil | 3147006 | 31 | 33 | nan | nan | nan | Cerrado | 64.4 |
| 9db32f46-bb7b-3ac6-826d-15a60c0fd0f1 | -6.8411 | -58.9939 | 2026-08-18 01:30:00 | GOES-19 | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 58.0 |
| 43f69633-0678-3f4f-9059-08f2b825b050 | -14.2562 | -51.9472 | 2026-08-18 01:30:00 | GOES-19 | NOVA NAZARÉ | MATO GROSSO | Brasil | 5106174 | 51 | 33 | nan | nan | nan | Cerrado | 94.9 |
| 6e42a619-3b9b-3c0f-80b9-2e535f14359e | -9.4256 | -60.4353 | 2026-08-18 01:30:00 | GOES-19 | ARIPUANÃ | MATO GROSSO | Brasil | 5101407 | 51 | 33 | nan | nan | nan | Amazônia | 83.7 |
| 2e9506ba-7987-3e4e-9c2c-ad24cd9c7a8f | -10.8688 | -44.9877 | 2026-08-18 01:30:00 | GOES-19 | CRISTALÂNDIA DO PIAUÍ | PIAUÍ | Brasil | 2203008 | 22 | 33 | nan | nan | nan | Cerrado | 66.1 |
| 13e67158-5c6c-3fa0-8b05-9c1acdc6e4fe | -14.2566 | -51.9259 | 2026-08-18 01:30:00 | GOES-19 | NOVA NAZARÉ | MATO GROSSO | Brasil | 5106174 | 51 | 33 | nan | nan | nan | Cerrado | 129.1 |
| 0c93ab45-8f4e-3171-ba0c-ffe060aba085 | -14.2755 | -51.9447 | 2026-08-18 01:30:00 | GOES-19 | NOVA NAZARÉ | MATO GROSSO | Brasil | 5106174 | 51 | 33 | nan | nan | nan | Cerrado | 52.5 |
| 658fd994-67d5-318b-b2c4-cda7e7a77f96 | -8.222 | -55.0418 | 2026-08-18 01:30:00 | GOES-19 | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 61.7 |
| 47802880-f4a6-37a7-8c0f-cd3eeb7d538e | -10.8691 | -44.9646 | 2026-08-18 01:30:00 | GOES-19 | CRISTALÂNDIA DO PIAUÍ | PIAUÍ | Brasil | 2203008 | 22 | 33 | nan | nan | nan | Cerrado | 214.9 |
| bb0a2e0e-6c20-34fe-ac7d-c8d3b2395cea | -6.8594 | -59.0125 | 2026-08-18 01:30:00 | GOES-19 | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 109.3 |
| 3c1efe26-19e5-327e-b440-59946a0daaea | -9.016 | -60.4945 | 2026-08-18 01:30:00 | GOES-19 | COLNIZA | MATO GROSSO | Brasil | 5103254 | 51 | 33 | nan | nan | nan | Amazônia | 155.9 |
| a99d89a9-6790-3b4c-97d7-ff43008d1cf7 | -9.4254 | -60.4545 | 2026-08-18 01:30:00 | GOES-19 | ARIPUANÃ | MATO GROSSO | Brasil | 5101407 | 51 | 33 | nan | nan | nan | Amazônia | 74.2 |
| d5533a81-2989-31e1-8710-1ad20e510a3c | -6.7663 | -59.1708 | 2026-08-18 01:30:00 | GOES-19 | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 71.5 |
| d00f0058-ce5b-3dc9-9dd2-2871f99f73b8 | -6.841 | -59.0132 | 2026-08-18 01:30:00 | GOES-19 | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 93.7 |
| f9df51c3-617f-3de5-b828-9250bfaa0941 | -6.8596 | -58.9931 | 2026-08-18 01:40:00 | GOES-19 | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 39.4 |
| 216941d8-8c8a-3ceb-b7a6-ad6d46dff43e | -9.0158 | -60.5138 | 2026-08-18 01:40:00 | GOES-19 | COLNIZA | MATO GROSSO | Brasil | 5103254 | 51 | 33 | nan | nan | nan | Amazônia | 63.3 |
| 6c23e95d-b101-3705-8f2e-76e63a6124a3 | -8.604 | -50.3527 | 2026-08-18 01:40:00 | GOES-19 | SANTA MARIA DAS BARREIRAS | PARÁ | Brasil | 1506583 | 15 | 33 | nan | nan | nan | Amazônia | 98.2 |
| 20fbf014-2744-33aa-9fd0-d1cd63fc62c7 | -16.3647 | -49.4818 | 2026-08-18 01:40:00 | GOES-19 | INHUMAS | GOIÁS | Brasil | 5210000 | 52 | 33 | nan | nan | nan | Cerrado | 74.0 |
| 2f7459ac-da9a-38c7-9d88-3bd4fd942aa8 | -14.2759 | -51.9234 | 2026-08-18 01:40:00 | GOES-19 | NOVA NAZARÉ | MATO GROSSO | Brasil | 5106174 | 51 | 33 | nan | nan | nan | Cerrado | 77.0 |
| 45eb4755-0082-3e88-afd1-8bee0d037b28 | -8.6042 | -50.3315 | 2026-08-18 01:40:00 | GOES-19 | SANTA MARIA DAS BARREIRAS | PARÁ | Brasil | 1506583 | 15 | 33 | nan | nan | nan | Amazônia | 58.0 |
| f52e00dc-52ff-3121-9c67-49177d202e2d | -6.7664 | -59.1515 | 2026-08-18 01:40:00 | GOES-19 | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 19.0 |
| 9c33f30c-a418-3c34-b9b6-55df0c24c26d | -8.5853 | -50.3543 | 2026-08-18 01:40:00 | GOES-19 | SANTA MARIA DAS BARREIRAS | PARÁ | Brasil | 1506583 | 15 | 33 | nan | nan | nan | Amazônia | 41.7 |
| f7d70bdc-feae-32e7-a314-c28690316402 | -6.8411 | -58.9939 | 2026-08-18 01:40:00 | GOES-19 | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 67.2 |
| dc9f75c8-75ef-3385-a841-18a930e518bc | -10.8691 | -44.9646 | 2026-08-18 01:40:00 | GOES-19 | CRISTALÂNDIA DO PIAUÍ | PIAUÍ | Brasil | 2203008 | 22 | 33 | nan | nan | nan | Cerrado | 97.2 |
| 9d2481af-ccfe-3e95-8f2b-684d4b875a3c | -14.1631 | -52.9113 | 2026-08-18 01:40:00 | GOES-19 | ÁGUA BOA | MATO GROSSO | Brasil | 5100201 | 51 | 33 | nan | nan | nan | Cerrado | 60.0 |
| d7a08a9c-afd1-33b9-bcf9-e5e64c724585 | -9.4257 | -60.416 | 2026-08-18 01:40:00 | GOES-19 | ARIPUANÃ | MATO GROSSO | Brasil | 5101407 | 51 | 33 | nan | nan | nan | Amazônia | 52.0 |
| eb99ea46-6d41-33a4-9cbf-db426d9d8c68 | -9.4254 | -60.4545 | 2026-08-18 01:40:00 | GOES-19 | ARIPUANÃ | MATO GROSSO | Brasil | 5101407 | 51 | 33 | nan | nan | nan | Amazônia | 68.0 |
| 87e8a23b-6ba9-306d-a880-0524245bfb4f | -14.2566 | -51.9259 | 2026-08-18 01:40:00 | GOES-19 | NOVA NAZARÉ | MATO GROSSO | Brasil | 5106174 | 51 | 33 | nan | nan | nan | Cerrado | 105.3 |
| 41742cd9-b05a-32dd-87d0-d71560b2761c | -16.345 | -49.4851 | 2026-08-18 01:40:00 | GOES-19 | INHUMAS | GOIÁS | Brasil | 5210000 | 52 | 33 | nan | nan | nan | Cerrado | 56.4 |
| 4cee4342-738b-32b2-8490-2c5f1311d59f | -14.1824 | -52.9089 | 2026-08-18 01:40:00 | GOES-19 | ÁGUA BOA | MATO GROSSO | Brasil | 5100201 | 51 | 33 | nan | nan | nan | Cerrado | 72.1 |
| c56fec8f-9a19-385c-ab64-8958674c541a | -14.1821 | -52.93 | 2026-08-18 01:40:00 | GOES-19 | ÁGUA BOA | MATO GROSSO | Brasil | 5100201 | 51 | 33 | nan | nan | nan | Cerrado | 86.6 |
| fb00c69e-8889-3a52-b89a-5f7248eff126 | -14.2755 | -51.9447 | 2026-08-18 01:40:00 | GOES-19 | NOVA NAZARÉ | MATO GROSSO | Brasil | 5106174 | 51 | 33 | nan | nan | nan | Cerrado | 49.2 |
| 5915fa20-ff37-3929-8bc9-164fcc3a09dd | -6.748 | -59.1523 | 2026-08-18 01:40:00 | GOES-19 | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 56.0 |
| c6e8bf1b-bacd-3f29-a955-98362b1bcd24 | -10.85 | -44.9672 | 2026-08-18 01:40:00 | GOES-19 | CRISTALÂNDIA DO PIAUÍ | PIAUÍ | Brasil | 2203008 | 22 | 33 | nan | nan | nan | Cerrado | 141.6 |
| f0021d74-411a-3d77-91ba-1c498e3c8adc | -8.185 | -55.024 | 2026-08-18 01:40:00 | GOES-19 | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 54.4 |
| 65c763ce-7c0a-3832-bbfb-a2e2c28cb781 | -6.841 | -59.0132 | 2026-08-18 01:40:00 | GOES-19 | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 122.6 |
| e4967a96-1bdc-3620-b2aa-e7c088e40235 | -8.2222 | -55.0216 | 2026-08-18 01:40:00 | GOES-19 | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 56.3 |
| fff042c3-b83d-3f42-b14f-20952c395172 | -6.7478 | -59.1716 | 2026-08-18 01:40:00 | GOES-19 | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 137.2 |
| 8d0ca128-720a-3d62-875b-18476c66741d | -9.4256 | -60.4353 | 2026-08-18 01:40:00 | GOES-19 | ARIPUANÃ | MATO GROSSO | Brasil | 5101407 | 51 | 33 | nan | nan | nan | Amazônia | 81.2 |
| 405dadfb-9259-3752-92e2-727d6105d5da | -6.1668 | -47.3297 | 2026-08-18 01:40:00 | GOES-19 | CAMPESTRE DO MARANHÃO | MARANHÃO | Brasil | 2102556 | 21 | 33 | nan | nan | nan | Cerrado | 58.1 |
| 32700c70-f716-3f18-80de-d1e2c9c68803 | -9.016 | -60.4945 | 2026-08-18 01:40:00 | GOES-19 | COLNIZA | MATO GROSSO | Brasil | 5103254 | 51 | 33 | nan | nan | nan | Amazônia | 68.8 |
| 47a38167-6c69-34c9-9871-4fb4cb8fab04 | -8.2036 | -55.0228 | 2026-08-18 01:40:00 | GOES-19 | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 79.4 |
| 944a4761-530e-38eb-862b-0f43261866fe | -8.2034 | -55.0429 | 2026-08-18 01:40:00 | GOES-19 | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 55.0 |
| eb4cba22-116e-380b-8002-9e5a4e0bc781 | -6.8594 | -59.0125 | 2026-08-18 01:40:00 | GOES-19 | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 75.4 |
| cbef9ea6-7921-381d-a33a-ed0a6adf4c30 | -6.7477 | -59.1909 | 2026-08-18 01:40:00 | GOES-19 | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 49.1 |
| c162f938-794e-3734-9dbe-53f39305ad61 | -6.7663 | -59.1708 | 2026-08-18 01:40:00 | GOES-19 | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 36.6 |
| 58375e27-741a-3e57-8bb7-221b13f9b1dd | -14.1824 | -52.9089 | 2026-08-18 01:50:00 | GOES-19 | ÁGUA BOA | MATO GROSSO | Brasil | 5100201 | 51 | 33 | nan | nan | nan | Cerrado | 68.9 |
| 8ea85af8-159c-3fd4-bbc0-c7ffb95da2a9 | -14.1631 | -52.9113 | 2026-08-18 01:50:00 | GOES-19 | ÁGUA BOA | MATO GROSSO | Brasil | 5100201 | 51 | 33 | nan | nan | nan | Cerrado | 66.0 |
| b79f7608-51c2-35b1-851f-9fbb980049c4 | -8.222 | -55.0418 | 2026-08-18 01:50:00 | GOES-19 | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 56.7 |
| e22a150d-251e-388d-8f0e-e179d726cce4 | -8.604 | -50.3527 | 2026-08-18 01:50:00 | GOES-19 | SANTA MARIA DAS BARREIRAS | PARÁ | Brasil | 1506583 | 15 | 33 | nan | nan | nan | Amazônia | 129.4 |
| 6e478a57-8a68-3830-8356-b23ed1ba13a7 | -8.2222 | -55.0216 | 2026-08-18 01:50:00 | GOES-19 | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 56.1 |
| 95e95634-4f7c-34a1-a4f6-83fedad24a97 | -6.8411 | -58.9939 | 2026-08-18 01:50:00 | GOES-19 | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 45.5 |
| 2d2717f7-f5ac-3793-b950-f47a53d30b45 | -6.841 | -59.0132 | 2026-08-18 01:50:00 | GOES-19 | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 81.7 |
| 4d5f12df-31cc-328d-955b-84593419c7b1 | -6.8596 | -58.9931 | 2026-08-18 01:50:00 | GOES-19 | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 37.3 |
| 03c3db56-5632-3928-a302-dddfce112c96 | -12.7205 | -48.4948 | 2026-08-18 01:50:00 | GOES-19 | SÃO SALVADOR DO TOCANTINS | TOCANTINS | Brasil | 1720259 | 17 | 33 | nan | nan | nan | Cerrado | 63.7 |
| 56aee319-fdb3-3afd-a4e8-fabfd4de50e1 | -9.0158 | -60.5138 | 2026-08-18 01:50:00 | GOES-19 | COLNIZA | MATO GROSSO | Brasil | 5103254 | 51 | 33 | nan | nan | nan | Amazônia | 56.3 |
| 9f0686d0-343f-332a-a65a-31f79c8fb67b | -8.5855 | -50.3331 | 2026-08-18 01:50:00 | GOES-19 | SANTA MARIA DAS BARREIRAS | PARÁ | Brasil | 1506583 | 15 | 33 | nan | nan | nan | Amazônia | 42.3 |
| 5059a146-3ac8-3d0c-8271-7efef86677b3 | -9.016 | -60.4945 | 2026-08-18 01:50:00 | GOES-19 | COLNIZA | MATO GROSSO | Brasil | 5103254 | 51 | 33 | nan | nan | nan | Amazônia | 50.3 |
| 7c7a8f76-25c5-30ec-ad87-af8df97e3912 | -14.1821 | -52.93 | 2026-08-18 01:50:00 | GOES-19 | ÁGUA BOA | MATO GROSSO | Brasil | 5100201 | 51 | 33 | nan | nan | nan | Cerrado | 87.4 |
| db83be96-7205-3e23-8e9f-1430fc9b375e | -6.8594 | -59.0125 | 2026-08-18 01:50:00 | GOES-19 | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 81.7 |
| 256146cf-9f42-3b90-9e5e-4d2751a5cc5f | -10.85 | -44.9672 | 2026-08-18 01:50:00 | GOES-19 | CRISTALÂNDIA DO PIAUÍ | PIAUÍ | Brasil | 2203008 | 22 | 33 | nan | nan | nan | Cerrado | 76.4 |
| ddec7312-06c4-3be2-adac-7a9eb69b2c55 | -8.5853 | -50.3543 | 2026-08-18 01:50:00 | GOES-19 | SANTA MARIA DAS BARREIRAS | PARÁ | Brasil | 1506583 | 15 | 33 | nan | nan | nan | Amazônia | 81.0 |
| 075776ce-8cda-3777-944e-f14d9001ab61 | -9.4254 | -60.4545 | 2026-08-18 01:50:00 | GOES-19 | ARIPUANÃ | MATO GROSSO | Brasil | 5101407 | 51 | 33 | nan | nan | nan | Amazônia | 64.8 |
| 7d0143fc-28f2-3dc0-9631-6f3714ff9677 | -8.2036 | -55.0228 | 2026-08-18 01:50:00 | GOES-19 | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 77.6 |
| 8a6f1fda-72a9-388d-acce-3610c48a15fa | -8.6042 | -50.3315 | 2026-08-18 01:50:00 | GOES-19 | SANTA MARIA DAS BARREIRAS | PARÁ | Brasil | 1506583 | 15 | 33 | nan | nan | nan | Amazônia | 67.4 |
| ba93c187-1360-3a1d-836f-e442164c136f | -9.4256 | -60.4353 | 2026-08-18 01:50:00 | GOES-19 | ARIPUANÃ | MATO GROSSO | Brasil | 5101407 | 51 | 33 | nan | nan | nan | Amazônia | 81.9 |
| 9a51ad66-75ad-3fbc-8de4-790f701a436d | -10.8691 | -44.9646 | 2026-08-18 01:50:00 | GOES-19 | CRISTALÂNDIA DO PIAUÍ | PIAUÍ | Brasil | 2203008 | 22 | 33 | nan | nan | nan | Cerrado | 107.3 |
| 147f635c-2166-3f0e-8b2c-df71c0029346 | -6.7663 | -59.1708 | 2026-08-18 02:00:00 | GOES-19 | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 56.7 |
| b93996cd-cf1f-33cf-b9e0-09448c0d89c9 | -8.2036 | -55.0228 | 2026-08-18 02:00:00 | GOES-19 | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 80.8 |
| d6f8c0bd-e5d2-3cd6-85af-e1e8c535e79e | -14.2755 | -51.9447 | 2026-08-18 02:00:00 | GOES-19 | NOVA NAZARÉ | MATO GROSSO | Brasil | 5106174 | 51 | 33 | nan | nan | nan | Cerrado | 111.8 |
| 88a61fb5-33f8-380b-ac4b-4399ab3cd736 | -14.1821 | -52.93 | 2026-08-18 02:00:00 | GOES-19 | ÁGUA BOA | MATO GROSSO | Brasil | 5100201 | 51 | 33 | nan | nan | nan | Cerrado | 70.0 |
| afb0d73d-79b0-3378-82f0-7572ba43970d | -6.7664 | -59.1515 | 2026-08-18 02:00:00 | GOES-19 | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 26.3 |
| b0483401-3c85-3dec-a553-e71134a24378 | -14.2952 | -51.9208 | 2026-08-18 02:00:00 | GOES-19 | NOVA NAZARÉ | MATO GROSSO | Brasil | 5106174 | 51 | 33 | nan | nan | nan | Cerrado | 78.3 |
| 1381c491-7c1d-32dc-b6e3-5d3f19feddad | -6.8411 | -58.9939 | 2026-08-18 02:00:00 | GOES-19 | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 44.7 |
| 43d9a7bf-783e-3da1-913e-066a8ba2b241 | -14.2949 | -51.9422 | 2026-08-18 02:00:00 | GOES-19 | NOVA NAZARÉ | MATO GROSSO | Brasil | 5106174 | 51 | 33 | nan | nan | nan | Cerrado | 74.3 |
| eadd7b62-05d6-3842-af5a-084f37507e39 | -14.1631 | -52.9113 | 2026-08-18 02:00:00 | GOES-19 | ÁGUA BOA | MATO GROSSO | Brasil | 5100201 | 51 | 33 | nan | nan | nan | Cerrado | 67.6 |
| 221e6f6e-e728-360b-86d4-fb7d4ae36023 | -8.5855 | -50.3331 | 2026-08-18 02:00:00 | GOES-19 | SANTA MARIA DAS BARREIRAS | PARÁ | Brasil | 1506583 | 15 | 33 | nan | nan | nan | Amazônia | 43.1 |
| dca87aec-00fd-374e-a2b2-84f6085a9ca8 | -6.8596 | -58.9931 | 2026-08-18 02:00:00 | GOES-19 | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 34.5 |
| 1e66ba4e-c72b-35f7-8248-fbd57db181ef | -6.7478 | -59.1716 | 2026-08-18 02:00:00 | GOES-19 | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 116.5 |
| be2c6977-48f4-36be-b951-c51232eef3b0 | -8.604 | -50.3527 | 2026-08-18 02:00:00 | GOES-19 | SANTA MARIA DAS BARREIRAS | PARÁ | Brasil | 1506583 | 15 | 33 | nan | nan | nan | Amazônia | 121.0 |
| b080652d-8c46-3ae9-bc17-dfea36b67687 | -6.7123 | -58.9412 | 2026-08-18 02:00:00 | GOES-19 | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 33.2 |
| 91c309ed-2eeb-35a4-bd9b-801f1f5f6c2d | -6.7477 | -59.1909 | 2026-08-18 02:00:00 | GOES-19 | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 40.8 |
| 96613522-7779-3a4c-b267-9f8eac83a707 | -6.7294 | -59.1723 | 2026-08-18 02:00:00 | GOES-19 | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 23.8 |
| d4841900-4606-3003-bbb1-7362e81bc2b7 | -9.4256 | -60.4353 | 2026-08-18 02:00:00 | GOES-19 | ARIPUANÃ | MATO GROSSO | Brasil | 5101407 | 51 | 33 | nan | nan | nan | Amazônia | 54.1 |
| 795bfb4f-75a0-30d4-a00b-c77d3c227205 | -6.748 | -59.1523 | 2026-08-18 02:00:00 | GOES-19 | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 48.7 |
| d9a02720-9529-3be3-b35b-ded262bcd175 | -8.6042 | -50.3315 | 2026-08-18 02:00:00 | GOES-19 | SANTA MARIA DAS BARREIRAS | PARÁ | Brasil | 1506583 | 15 | 33 | nan | nan | nan | Amazônia | 93.4 |
| 40e2545a-f771-3e3d-bfc9-6b7031b7ecc7 | -14.1824 | -52.9089 | 2026-08-18 02:00:00 | GOES-19 | ÁGUA BOA | MATO GROSSO | Brasil | 5100201 | 51 | 33 | nan | nan | nan | Cerrado | 72.8 |
| a660b50c-46f0-3afc-a504-b46a0f849749 | -14.2566 | -51.9259 | 2026-08-18 02:00:00 | GOES-19 | NOVA NAZARÉ | MATO GROSSO | Brasil | 5106174 | 51 | 33 | nan | nan | nan | Cerrado | 94.7 |


[Clique aqui para ver as próximas entradas](README6.md)
