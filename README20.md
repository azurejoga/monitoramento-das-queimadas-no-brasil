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

## Dados Diários - Página 20

| ID | Latitude | Longitude | Data/Hora GMT | Satélite | Município | Estado | País | Município ID | Estado ID | País ID | Dias sem Chuva | Precipitação | Risco de Fogo | Bioma | FRP |
|----|----------|-----------|---------------|----------|-----------|--------|------|--------------|-----------|---------|----------------|--------------|----------------|-------|-----|
| 1af4ab2f-8fe0-3db9-acc8-cd91c9954239 | -3.2174 | -50.139 | 2025-12-01 06:20:00 | GOES-19 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 65.7 |
| a68b5a06-c30b-3ef5-86b1-0ddfcc613899 | -4.3703 | -43.1508 | 2025-12-01 06:20:00 | GOES-19 | COELHO NETO | MARANHÃO | Brasil | 2103406 | 21 | 33 | nan | nan | nan | Cerrado | 79.7 |
| 6626ae40-7a18-31eb-a8f8-b4643fdaa503 | -4.389 | -43.1497 | 2025-12-01 06:20:00 | GOES-19 | COELHO NETO | MARANHÃO | Brasil | 2103406 | 21 | 33 | nan | nan | nan | Cerrado | 77.2 |
| dfc55799-55ae-3005-8ba6-d3c24bd62796 | -4.389 | -43.1497 | 2025-12-01 06:30:00 | GOES-19 | COELHO NETO | MARANHÃO | Brasil | 2103406 | 21 | 33 | nan | nan | nan | Cerrado | 68.7 |
| 7c7411ce-9ce2-392a-bc15-9668f1fcc100 | -4.3877 | -43.3362 | 2025-12-01 06:30:00 | GOES-19 | ALDEIAS ALTAS | MARANHÃO | Brasil | 2100303 | 21 | 33 | nan | nan | nan | Cerrado | 77.5 |
| 1550d840-af78-3589-8da6-334358d64bb3 | -4.3703 | -43.1508 | 2025-12-01 06:30:00 | GOES-19 | COELHO NETO | MARANHÃO | Brasil | 2103406 | 21 | 33 | nan | nan | nan | Cerrado | 73.5 |
| 497a2c38-218a-3506-92e1-043496964257 | -4.389 | -43.1497 | 2025-12-01 06:40:00 | GOES-19 | COELHO NETO | MARANHÃO | Brasil | 2103406 | 21 | 33 | nan | nan | nan | Cerrado | 63.5 |
| 520c2ff6-286e-363c-9739-bf2200f3dc01 | -4.3703 | -43.1508 | 2025-12-01 06:40:00 | GOES-19 | COELHO NETO | MARANHÃO | Brasil | 2103406 | 21 | 33 | nan | nan | nan | Cerrado | 66.1 |
| 33d21eeb-d3a9-3cfb-a868-84827e4a6058 | -4.3877 | -43.3362 | 2025-12-01 06:40:00 | GOES-19 | ALDEIAS ALTAS | MARANHÃO | Brasil | 2100303 | 21 | 33 | nan | nan | nan | Cerrado | 74.1 |
| d0b93768-4329-3b71-94d5-55310592c85e | -3.21355 | -50.13954 | 2025-12-01 06:44:00 | AQUA_M-M | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 45.3 |
| 5d689397-02f7-3668-8d24-1b18443ebf6f | -3.21743 | -50.12831 | 2025-12-01 06:44:00 | AQUA_M-M | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 42.9 |
| 06400373-225d-3245-917a-b80302a47994 | -2.93279 | -53.28204 | 2025-12-01 06:44:00 | AQUA_M-M | MEDICILÂNDIA | PARÁ | Brasil | 1504455 | 15 | 33 | nan | nan | nan | Amazônia | 10.4 |
| 17e676d7-d6c2-3ecf-90e9-ff0bbc050800 | -2.0406 | -52.099 | 2025-12-01 06:44:00 | AQUA_M-M | PORTO DE MOZ | PARÁ | Brasil | 1505908 | 15 | 33 | nan | nan | nan | Amazônia | 7.8 |
| 0db051c0-f410-3303-a7b8-a3152afe4b42 | -3.21628 | -50.12092 | 2025-12-01 06:44:00 | AQUA_M-M | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 20.1 |
| 72364c5f-dc28-33c7-bfe6-d9511fce15ed | -2.93439 | -53.27134 | 2025-12-01 06:44:00 | AQUA_M-M | MEDICILÂNDIA | PARÁ | Brasil | 1504455 | 15 | 33 | nan | nan | nan | Amazônia | 6.8 |
| 64112ce3-988e-3aa7-aff3-ce679fdd6428 | -20.0288 | -57.43897 | 2025-12-01 06:48:00 | AQUA_M-M | CORUMBÁ | MATO GROSSO DO SUL | Brasil | 5003207 | 50 | 33 | nan | nan | nan | Pantanal | 6.4 |
| 9c917818-478d-33df-b4e8-f44291c6eef0 | -20.02732 | -57.44982 | 2025-12-01 06:48:00 | AQUA_M-M | CORUMBÁ | MATO GROSSO DO SUL | Brasil | 5003207 | 50 | 33 | nan | nan | nan | Pantanal | 4.1 |
| 802b44bc-1883-30d1-85ef-1d8ae4d6a4c8 | -19.96376 | -57.37924 | 2025-12-01 06:48:00 | AQUA_M-M | CORUMBÁ | MATO GROSSO DO SUL | Brasil | 5003207 | 50 | 33 | nan | nan | nan | Pantanal | 5.5 |
| a9cd46be-754c-3c84-8a4f-882cdd809712 | -19.97326 | -57.38065 | 2025-12-01 06:48:00 | AQUA_M-M | CORUMBÁ | MATO GROSSO DO SUL | Brasil | 5003207 | 50 | 33 | nan | nan | nan | Pantanal | 4.7 |
| 508fb8fb-90b8-3a69-b9a2-477d869098f5 | -4.3877 | -43.3362 | 2025-12-01 06:50:00 | GOES-19 | ALDEIAS ALTAS | MARANHÃO | Brasil | 2100303 | 21 | 33 | nan | nan | nan | Cerrado | 86.5 |
| 3447ce66-2291-3f73-921c-a33afe5d7d47 | -3.2174 | -50.139 | 2025-12-01 06:50:00 | GOES-19 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 66.7 |
| 7b14cf31-549d-39e7-86d6-2518e518f00e | -4.3703 | -43.1508 | 2025-12-01 06:50:00 | GOES-19 | COELHO NETO | MARANHÃO | Brasil | 2103406 | 21 | 33 | nan | nan | nan | Cerrado | 75.4 |
| 206bb3f4-e9db-3ee2-b457-eb502b10f05f | -4.389 | -43.1497 | 2025-12-01 06:50:00 | GOES-19 | COELHO NETO | MARANHÃO | Brasil | 2103406 | 21 | 33 | nan | nan | nan | Cerrado | 58.6 |
| f74ce98e-a501-35a6-81c1-691d87a93885 | -4.3879 | -43.3129 | 2025-12-01 06:50:00 | GOES-19 | ALDEIAS ALTAS | MARANHÃO | Brasil | 2100303 | 21 | 33 | nan | nan | nan | Cerrado | 62.1 |
| 25bd8879-3868-3593-ba5a-e3c73fa580f8 | -3.2174 | -50.139 | 2025-12-01 07:00:00 | GOES-19 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 67.2 |
| 6117838f-89a9-3c86-8485-286f8523ada8 | -4.3877 | -43.3362 | 2025-12-01 07:00:00 | GOES-19 | ALDEIAS ALTAS | MARANHÃO | Brasil | 2100303 | 21 | 33 | nan | nan | nan | Cerrado | 96.6 |
| ae93147b-5546-3f4b-af3c-29f1a7d2a0de | -4.3703 | -43.1508 | 2025-12-01 07:00:00 | GOES-19 | COELHO NETO | MARANHÃO | Brasil | 2103406 | 21 | 33 | nan | nan | nan | Cerrado | 75.0 |
| 87dc50c3-facc-3236-b6d5-63871da4d6b7 | -4.389 | -43.1497 | 2025-12-01 07:00:00 | GOES-19 | COELHO NETO | MARANHÃO | Brasil | 2103406 | 21 | 33 | nan | nan | nan | Cerrado | 57.3 |
| bfae98ed-59a1-387a-8384-5d45497557fb | -4.3877 | -43.3362 | 2025-12-01 07:10:00 | GOES-19 | ALDEIAS ALTAS | MARANHÃO | Brasil | 2100303 | 21 | 33 | nan | nan | nan | Cerrado | 76.2 |
| bf8ab68c-963d-3d95-9c65-162d1ef710d0 | -4.3703 | -43.1508 | 2025-12-01 07:10:00 | GOES-19 | COELHO NETO | MARANHÃO | Brasil | 2103406 | 21 | 33 | nan | nan | nan | Cerrado | 66.7 |
| 68c5d207-e440-3d6e-83bf-193a44fa268e | -4.389 | -43.1497 | 2025-12-01 07:10:00 | GOES-19 | COELHO NETO | MARANHÃO | Brasil | 2103406 | 21 | 33 | nan | nan | nan | Cerrado | 62.1 |
| 66e4ee90-aa00-3f52-bbec-1f92c8574db5 | -4.389 | -43.1497 | 2025-12-01 07:20:00 | GOES-19 | COELHO NETO | MARANHÃO | Brasil | 2103406 | 21 | 33 | nan | nan | nan | Cerrado | 65.8 |
| 5a2c79ec-821a-3e1d-8d7e-4e7792865c4a | -4.3703 | -43.1508 | 2025-12-01 07:20:00 | GOES-19 | COELHO NETO | MARANHÃO | Brasil | 2103406 | 21 | 33 | nan | nan | nan | Cerrado | 62.6 |
| 939ee34b-314d-3991-a301-bd419e12c738 | -4.3877 | -43.3362 | 2025-12-01 07:20:00 | GOES-19 | ALDEIAS ALTAS | MARANHÃO | Brasil | 2100303 | 21 | 33 | nan | nan | nan | Cerrado | 68.2 |
| a62782be-dba8-3acf-bad4-4ce39b4d18bd | -4.3703 | -43.1508 | 2025-12-01 07:30:00 | GOES-19 | COELHO NETO | MARANHÃO | Brasil | 2103406 | 21 | 33 | nan | nan | nan | Cerrado | 67.7 |
| f3dfacfd-d9fe-33f9-849b-3a533fcc5d12 | -4.389 | -43.1497 | 2025-12-01 07:30:00 | GOES-19 | COELHO NETO | MARANHÃO | Brasil | 2103406 | 21 | 33 | nan | nan | nan | Cerrado | 67.0 |
| 9ccc6a33-0dd3-3651-bf63-b8a20d5288e1 | -4.3877 | -43.3362 | 2025-12-01 07:30:00 | GOES-19 | ALDEIAS ALTAS | MARANHÃO | Brasil | 2100303 | 21 | 33 | nan | nan | nan | Cerrado | 61.2 |
| faa93203-6875-3372-a77e-84f7ffaaa2a1 | -4.3877 | -43.3362 | 2025-12-01 07:40:00 | GOES-19 | ALDEIAS ALTAS | MARANHÃO | Brasil | 2100303 | 21 | 33 | nan | nan | nan | Cerrado | 58.2 |
| a673d9e5-730e-3802-906f-5c85540a4a29 | -4.389 | -43.1497 | 2025-12-01 07:40:00 | GOES-19 | COELHO NETO | MARANHÃO | Brasil | 2103406 | 21 | 33 | nan | nan | nan | Cerrado | 65.2 |
| 2d3db2dc-c69e-3d33-a55c-fea1f2527dca | -4.3703 | -43.1508 | 2025-12-01 07:40:00 | GOES-19 | COELHO NETO | MARANHÃO | Brasil | 2103406 | 21 | 33 | nan | nan | nan | Cerrado | 66.1 |
| c6fb74da-2d44-3188-bdca-e94ba01e0bb4 | -3.7769 | -45.6058 | 2025-12-01 07:50:00 | GOES-19 | TUFILÂNDIA | MARANHÃO | Brasil | 2112274 | 21 | 33 | nan | nan | nan | Amazônia | 57.1 |
| d63d83bd-1e25-3570-9a12-7789c29f9a8b | -19.975 | -57.3912 | 2025-12-01 12:10:00 | GOES-19 | CORUMBÁ | MATO GROSSO DO SUL | Brasil | 5003207 | 50 | 33 | nan | nan | nan | Pantanal | 143.5 |
| 81183864-482f-3653-a7d0-230d94a77b31 | -20.0343 | -57.4457 | 2025-12-01 12:30:00 | GOES-19 | CORUMBÁ | MATO GROSSO DO SUL | Brasil | 5003207 | 50 | 33 | nan | nan | nan | Pantanal | 125.0 |
| adb9346c-62e4-3f0f-89a2-83ee559930f8 | -19.975 | -57.3912 | 2025-12-01 12:30:00 | GOES-19 | CORUMBÁ | MATO GROSSO DO SUL | Brasil | 5003207 | 50 | 33 | nan | nan | nan | Pantanal | 174.9 |
| 0a5f963e-7c8d-3cba-8966-a95ef7dc1aeb | -19.9548 | -57.394 | 2025-12-01 12:30:00 | GOES-19 | CORUMBÁ | MATO GROSSO DO SUL | Brasil | 5003207 | 50 | 33 | nan | nan | nan | Pantanal | 125.5 |
| 2ae3f65d-ef5e-3ea3-a7e8-f905d9da51ff | -0.93679 | -47.57233 | 2025-12-01 12:33:00 | TERRA_M-T | MARACANÃ | PARÁ | Brasil | 1504307 | 15 | 33 | nan | nan | nan | Amazônia | 20.9 |
| 88d22e00-020b-3565-a6c9-8b761cb54491 | -0.84473 | -47.4125 | 2025-12-01 12:33:00 | TERRA_M-T | MARACANÃ | PARÁ | Brasil | 1504307 | 15 | 33 | nan | nan | nan | Amazônia | 11.4 |
| 477d7c6b-c20a-3114-98e1-b618bea5c64c | -0.93486 | -47.58596 | 2025-12-01 12:33:00 | TERRA_M-T | MAGALHÃES BARATA | PARÁ | Brasil | 1504109 | 15 | 33 | nan | nan | nan | Amazônia | 38.4 |
| 3f4b3086-003b-3385-931b-47025daa1c70 | -0.90562 | -47.63721 | 2025-12-01 12:33:00 | TERRA_M-T | MARAPANIM | PARÁ | Brasil | 1504406 | 15 | 33 | nan | nan | nan | Amazônia | 10.5 |
| bb9618d9-5711-3d71-af50-c904abaa5542 | 0.17304 | -49.86643 | 2025-12-01 12:33:00 | TERRA_M-T | CHAVES | PARÁ | Brasil | 1502509 | 15 | 33 | nan | nan | nan | Amazônia | 6.2 |
| c4ae8b42-7d3f-3470-9cdb-c79e52df7e83 | 3.35353 | -51.30142 | 2025-12-01 12:33:00 | TERRA_M-T | OIAPOQUE | AMAPÁ | Brasil | 1600501 | 16 | 33 | nan | nan | nan | Amazônia | 7.2 |
| 54d53a08-1add-3f3f-92fd-c86829a55b8b | -2.09011 | -47.21652 | 2025-12-01 12:36:00 | TERRA_M-T | CAPITÃO POÇO | PARÁ | Brasil | 1502301 | 15 | 33 | nan | nan | nan | Amazônia | 12.6 |
| 2593805c-9f7c-37ed-91aa-9c842a8fa307 | -3.91949 | -47.69323 | 2025-12-01 12:36:00 | TERRA_M-T | ULIANÓPOLIS | PARÁ | Brasil | 1508126 | 15 | 33 | nan | nan | nan | Amazônia | 19.7 |
| c5df1d50-6ddb-3871-a672-b02db5687bba | -3.44798 | -50.15169 | 2025-12-01 12:36:00 | TERRA_M-T | PACAJÁ | PARÁ | Brasil | 1505486 | 15 | 33 | nan | nan | nan | Amazônia | 11.2 |
| 1fa32bc2-2264-3193-8513-1f348d306974 | -1.48591 | -47.93661 | 2025-12-01 12:36:00 | TERRA_M-T | INHANGAPI | PARÁ | Brasil | 1503408 | 15 | 33 | nan | nan | nan | Amazônia | 13.9 |
| 09ca8db0-2f46-39ed-9b84-08ee11ef7980 | -3.92056 | -47.68475 | 2025-12-01 12:36:00 | TERRA_M-T | ULIANÓPOLIS | PARÁ | Brasil | 1508126 | 15 | 33 | nan | nan | nan | Amazônia | 33.0 |
| 5a05f846-e10b-38ed-aaa5-9f2ce935b62e | -1.7425 | -52.02391 | 2025-12-01 12:36:00 | TERRA_M-T | PORTO DE MOZ | PARÁ | Brasil | 1505908 | 15 | 33 | nan | nan | nan | Amazônia | 8.2 |
| 914b9002-833f-3160-93c0-9346834a3f7e | -1.05248 | -47.48196 | 2025-12-01 12:36:00 | TERRA_M-T | IGARAPÉ-AÇU | PARÁ | Brasil | 1503200 | 15 | 33 | nan | nan | nan | Amazônia | 24.5 |
| cf425881-96c3-36fc-908e-517a2f44f39a | -2.45391 | -49.00258 | 2025-12-01 12:36:00 | TERRA_M-T | MOJU | PARÁ | Brasil | 1504703 | 15 | 33 | nan | nan | nan | Amazônia | 12.1 |
| d81d1cee-96b7-3958-a8fc-1810ddc12451 | -3.09388 | -50.56512 | 2025-12-01 12:36:00 | TERRA_M-T | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 10.3 |
| 6612997f-eb05-3b22-8b27-8eefd70cd435 | -2.70158 | -51.89761 | 2025-12-01 12:36:00 | TERRA_M-T | SENADOR JOSÉ PORFÍRIO | PARÁ | Brasil | 1507805 | 15 | 33 | nan | nan | nan | Amazônia | 10.0 |
| 3960a7f0-a01b-330e-a185-366874f0b34b | -3.21614 | -50.14861 | 2025-12-01 12:36:00 | TERRA_M-T | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 10.1 |
| b5764bc4-6f3d-3bf6-a7e3-fc973f829b64 | -2.49717 | -49.35564 | 2025-12-01 12:36:00 | TERRA_M-T | MOCAJUBA | PARÁ | Brasil | 1504604 | 15 | 33 | nan | nan | nan | Amazônia | 17.4 |
| 4b93dd76-d121-32fd-83ec-80bf6e78c203 | -1.62317 | -47.68746 | 2025-12-01 12:36:00 | TERRA_M-T | SÃO MIGUEL DO GUAMÁ | PARÁ | Brasil | 1507607 | 15 | 33 | nan | nan | nan | Amazônia | 13.4 |
| f5afef01-592b-31ef-8469-073834ece7a8 | -0.8505 | -48.61338 | 2025-12-01 12:36:00 | TERRA_M-T | SALVATERRA | PARÁ | Brasil | 1506302 | 15 | 33 | nan | nan | nan | Amazônia | 11.2 |
| dc3fc963-ba57-308b-9ba3-a8c056b20a7b | -1.51673 | -47.79193 | 2025-12-01 12:36:00 | TERRA_M-T | SÃO MIGUEL DO GUAMÁ | PARÁ | Brasil | 1507607 | 15 | 33 | nan | nan | nan | Amazônia | 30.5 |
| 1cbfbdc6-bc82-3827-b66c-9294ead16ecc | -3.21895 | -50.12846 | 2025-12-01 12:36:00 | TERRA_M-T | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 27.5 |
| cae5eeff-ffbf-304f-baeb-f11271855ba3 | -3.33022 | -44.61451 | 2025-12-01 12:36:00 | TERRA_M-T | ANAJATUBA | MARANHÃO | Brasil | 2100709 | 21 | 33 | nan | nan | nan | Amazônia | 56.9 |
| 45694836-8cfe-3376-98fe-9177193c25f2 | -3.21754 | -50.13854 | 2025-12-01 12:36:00 | TERRA_M-T | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 123.3 |
| c092ba66-ab72-3f0f-9f36-830d88aed25a | -2.51077 | -49.10307 | 2025-12-01 12:36:00 | TERRA_M-T | MOJU | PARÁ | Brasil | 1504703 | 15 | 33 | nan | nan | nan | Amazônia | 9.3 |
| 7a9f99e1-1eea-3a80-9996-d0acc3934e80 | -2.0335 | -47.37642 | 2025-12-01 12:36:00 | TERRA_M-T | IRITUIA | PARÁ | Brasil | 1503507 | 15 | 33 | nan | nan | nan | Amazônia | 12.4 |
| 27d6cd27-294b-3362-b7c8-e76810a713da | -1.5863 | -47.84236 | 2025-12-01 12:36:00 | TERRA_M-T | SÃO MIGUEL DO GUAMÁ | PARÁ | Brasil | 1507607 | 15 | 33 | nan | nan | nan | Amazônia | 12.5 |
| bb9cd069-fe57-3963-95ed-83611eab3f05 | -3.33295 | -44.62021 | 2025-12-01 12:36:00 | TERRA_M-T | ANAJATUBA | MARANHÃO | Brasil | 2100709 | 21 | 33 | nan | nan | nan | Amazônia | 97.9 |
| 7069427a-a1fa-361c-bdda-9039aabe4293 | -11.28074 | -52.46259 | 2025-12-01 12:38:00 | TERRA_M-T | SÃO FÉLIX DO ARAGUAIA | MATO GROSSO | Brasil | 5107859 | 51 | 33 | nan | nan | nan | Amazônia | 5.7 |
| a585623c-6dce-3ced-9570-45f28463787c | -19.9548 | -57.394 | 2025-12-01 12:40:00 | GOES-19 | CORUMBÁ | MATO GROSSO DO SUL | Brasil | 5003207 | 50 | 33 | nan | nan | nan | Pantanal | 119.1 |
| b51e5b72-6422-31f6-a678-543bf25c56dc | -19.975 | -57.3912 | 2025-12-01 12:40:00 | GOES-19 | CORUMBÁ | MATO GROSSO DO SUL | Brasil | 5003207 | 50 | 33 | nan | nan | nan | Pantanal | 118.8 |
| 06293950-c0c6-3b12-98bf-15e8ee520794 | -17.53958 | -57.1642 | 2025-12-01 12:40:00 | TERRA_M-T | POCONÉ | MATO GROSSO | Brasil | 5106505 | 51 | 33 | nan | nan | nan | Pantanal | 65.8 |
| 9de7dbc6-0f27-3fc0-a2ec-d23bf0bc59e9 | -20.04809 | -57.43331 | 2025-12-01 12:40:00 | TERRA_M-T | CORUMBÁ | MATO GROSSO DO SUL | Brasil | 5003207 | 50 | 33 | nan | nan | nan | Pantanal | 9.8 |
| fc977a16-1506-35e3-8e07-a13647136133 | -20.03758 | -57.44161 | 2025-12-01 12:40:00 | TERRA_M-T | CORUMBÁ | MATO GROSSO DO SUL | Brasil | 5003207 | 50 | 33 | nan | nan | nan | Pantanal | 22.7 |
| 349d1a85-25f9-3d7e-bda7-b27712ece3aa | -17.49166 | -57.18023 | 2025-12-01 12:40:00 | TERRA_M-T | POCONÉ | MATO GROSSO | Brasil | 5106505 | 51 | 33 | nan | nan | nan | Pantanal | 50.1 |
| 62bec739-e49c-3112-99d6-b12e2dae23dc | -17.53807 | -57.17408 | 2025-12-01 12:40:00 | TERRA_M-T | POCONÉ | MATO GROSSO | Brasil | 5106505 | 51 | 33 | nan | nan | nan | Pantanal | 54.7 |
| a9ce62f1-9235-3ba4-814f-2061308e895b | -19.9713 | -57.39045 | 2025-12-01 12:40:00 | TERRA_M-T | CORUMBÁ | MATO GROSSO DO SUL | Brasil | 5003207 | 50 | 33 | nan | nan | nan | Pantanal | 159.2 |
| b1fdd173-99a4-3c2f-a698-f9d99485c5b4 | -17.54569 | -57.18545 | 2025-12-01 12:40:00 | TERRA_M-T | POCONÉ | MATO GROSSO | Brasil | 5106505 | 51 | 33 | nan | nan | nan | Pantanal | 6.6 |
| a199f801-329f-303b-9767-e2fbef89bdf9 | -16.75658 | -48.91029 | 2025-12-01 12:40:00 | TERRA_M-T | CALDAZINHA | GOIÁS | Brasil | 5204557 | 52 | 33 | nan | nan | nan | Cerrado | 24.0 |
| 53e7f660-937a-3a91-adb8-9690ceda3780 | -19.96325 | -57.38304 | 2025-12-01 12:40:00 | TERRA_M-T | CORUMBÁ | MATO GROSSO DO SUL | Brasil | 5003207 | 50 | 33 | nan | nan | nan | Pantanal | 17.4 |
| c27414ae-e62e-371f-b72c-1c9cfefd2c6b | -17.5472 | -57.17556 | 2025-12-01 12:40:00 | TERRA_M-T | POCONÉ | MATO GROSSO | Brasil | 5106505 | 51 | 33 | nan | nan | nan | Pantanal | 83.7 |
| ddd75d65-6719-32a4-b887-0adf3e61eaac | -19.96471 | -57.37326 | 2025-12-01 12:40:00 | TERRA_M-T | CORUMBÁ | MATO GROSSO DO SUL | Brasil | 5003207 | 50 | 33 | nan | nan | nan | Pantanal | 12.8 |
| 5cdc439a-a8de-371b-93ae-493343dc5363 | -13.4515 | -54.5892 | 2025-12-01 12:40:00 | TERRA_M-T | PARANATINGA | MATO GROSSO | Brasil | 5106307 | 51 | 33 | nan | nan | nan | Cerrado | 4.4 |
| 6ee74685-bcc4-31aa-8f59-a632f96e0fb1 | -17.51829 | -57.18101 | 2025-12-01 12:40:00 | TERRA_M-T | POCONÉ | MATO GROSSO | Brasil | 5106505 | 51 | 33 | nan | nan | nan | Pantanal | 46.4 |
| a375d095-696b-3210-b28f-b057509fd9cb | -19.97279 | -57.38068 | 2025-12-01 12:40:00 | TERRA_M-T | CORUMBÁ | MATO GROSSO DO SUL | Brasil | 5003207 | 50 | 33 | nan | nan | nan | Pantanal | 26.1 |
| 2ec8fcb8-a9d7-3773-a469-5753ecdc9765 | -17.51677 | -57.19091 | 2025-12-01 12:40:00 | TERRA_M-T | POCONÉ | MATO GROSSO | Brasil | 5106505 | 51 | 33 | nan | nan | nan | Pantanal | 103.4 |
| 4277c83c-39c3-36c5-ae73-5c960fef3bf7 | -20.03463 | -57.46124 | 2025-12-01 12:40:00 | TERRA_M-T | CORUMBÁ | MATO GROSSO DO SUL | Brasil | 5003207 | 50 | 33 | nan | nan | nan | Pantanal | 12.0 |
| 2e0af598-38ec-3937-ad90-6bd7f412adc6 | -17.52591 | -57.19238 | 2025-12-01 12:40:00 | TERRA_M-T | POCONÉ | MATO GROSSO | Brasil | 5106505 | 51 | 33 | nan | nan | nan | Pantanal | 43.2 |
| 9b2a55a1-245e-3ec3-aecf-fb1d563bef9c | -13.73931 | -53.93925 | 2025-12-01 12:40:00 | TERRA_M-T | GAÚCHA DO NORTE | MATO GROSSO | Brasil | 5103858 | 51 | 33 | nan | nan | nan | Cerrado | 6.4 |
| 32b5da3d-bf63-3253-8534-3c685756d581 | -17.5487 | -57.16568 | 2025-12-01 12:40:00 | TERRA_M-T | POCONÉ | MATO GROSSO | Brasil | 5106505 | 51 | 33 | nan | nan | nan | Pantanal | 89.0 |
| 7b9b5e20-6366-301e-9f96-ba96cad6ca02 | -17.48551 | -57.15895 | 2025-12-01 12:40:00 | TERRA_M-T | POCONÉ | MATO GROSSO | Brasil | 5106505 | 51 | 33 | nan | nan | nan | Pantanal | 36.1 |
| 22c001c1-345f-3e90-8e41-aef736b3c34b | -20.90427 | -55.20938 | 2025-12-01 12:40:00 | TERRA_M-T | DOIS IRMÃOS DO BURITI | MATO GROSSO DO SUL | Brasil | 5003488 | 50 | 33 | nan | nan | nan | Cerrado | 8.9 |
| 4617ee29-164f-3ab9-9566-817f8ad1f898 | -20.02707 | -57.44991 | 2025-12-01 12:40:00 | TERRA_M-T | CORUMBÁ | MATO GROSSO DO SUL | Brasil | 5003207 | 50 | 33 | nan | nan | nan | Pantanal | 10.6 |
| 14506263-09c1-366d-9e29-1d2f9f88a1c1 | -20.03611 | -57.45142 | 2025-12-01 12:40:00 | TERRA_M-T | CORUMBÁ | MATO GROSSO DO SUL | Brasil | 5003207 | 50 | 33 | nan | nan | nan | Pantanal | 30.5 |
| 84d0583e-f9b5-33bd-9e79-88473e3e91f1 | -17.52742 | -57.18249 | 2025-12-01 12:40:00 | TERRA_M-T | POCONÉ | MATO GROSSO | Brasil | 5106505 | 51 | 33 | nan | nan | nan | Pantanal | 93.6 |


[Clique aqui para ver as próximas entradas](README21.md)
