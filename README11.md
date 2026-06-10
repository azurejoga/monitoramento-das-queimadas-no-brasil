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

## Dados Diários - Página 11

| ID | Latitude | Longitude | Data/Hora GMT | Satélite | Município | Estado | País | Município ID | Estado ID | País ID | Dias sem Chuva | Precipitação | Risco de Fogo | Bioma | FRP |
|----|----------|-----------|---------------|----------|-----------|--------|------|--------------|-----------|---------|----------------|--------------|----------------|-------|-----|
| 1f3d6c8d-9849-3c21-8236-a53e4e429533 | -21.32108 | -48.54166 | 2026-06-10 04:53:00 | NOAA-20 | MONTE ALTO | SÃO PAULO | Brasil | 3531308 | 35 | 33 | nan | nan | nan | Cerrado | 1.5 |
| 1e9b295f-ee8c-3510-9ddb-d7814f5a0e95 | -20.2338 | -41.89897 | 2026-06-10 04:53:00 | NOAA-20 | REDUTO | MINAS GERAIS | Brasil | 3154150 | 31 | 33 | nan | nan | nan | Mata Atlântica | 8.4 |
| 332cab42-642b-30a8-a350-018edc85e9d4 | -18.5861 | -46.58377 | 2026-06-10 04:53:00 | NOAA-20 | PATOS DE MINAS | MINAS GERAIS | Brasil | 3148004 | 31 | 33 | nan | nan | nan | Cerrado | 1.4 |
| 04794cfa-240a-3142-9760-4e38492ed752 | -17.44854 | -47.17978 | 2026-06-10 04:53:00 | NOAA-20 | PARACATU | MINAS GERAIS | Brasil | 3147006 | 31 | 33 | nan | nan | nan | Cerrado | 1.9 |
| 66ada288-f8dc-32f5-915e-9e2bd8b3a3b0 | -17.4529 | -47.18045 | 2026-06-10 04:53:00 | NOAA-20 | PARACATU | MINAS GERAIS | Brasil | 3147006 | 31 | 33 | nan | nan | nan | Cerrado | 1.4 |
| 9fa25669-2910-3977-ba08-f7b310c507f3 | -17.81215 | -50.64509 | 2026-06-10 04:53:00 | NOAA-20 | SANTA HELENA DE GOIÁS | GOIÁS | Brasil | 5219308 | 52 | 33 | nan | nan | nan | Cerrado | 1.8 |
| acd80719-a8d4-3d2f-b19c-a2d500f91ee3 | -18.68132 | -52.70855 | 2026-06-10 04:53:00 | NOAA-20 | CHAPADÃO DO CÉU | GOIÁS | Brasil | 5205471 | 52 | 33 | nan | nan | nan | Cerrado | 1.0 |
| 274aa196-6d5d-3a19-aebe-b50eb05e204b | -18.96221 | -52.46894 | 2026-06-10 04:53:00 | NOAA-20 | CASSILÂNDIA | MATO GROSSO DO SUL | Brasil | 5002902 | 50 | 33 | nan | nan | nan | Cerrado | 0.7 |
| 84fec9e3-6c37-3c1d-9137-a3614b7105e4 | -18.95883 | -52.4684 | 2026-06-10 04:53:00 | NOAA-20 | CASSILÂNDIA | MATO GROSSO DO SUL | Brasil | 5002902 | 50 | 33 | nan | nan | nan | Cerrado | 0.6 |
| 3870b81e-d103-30cb-b1db-46b0e6ffb777 | -17.81573 | -50.64561 | 2026-06-10 04:53:00 | NOAA-20 | SANTA HELENA DE GOIÁS | GOIÁS | Brasil | 5219308 | 52 | 33 | nan | nan | nan | Cerrado | 2.1 |
| d02022fc-a03c-30f5-8492-cd2dce37b612 | -18.58732 | -46.58205 | 2026-06-10 04:53:00 | NOAA-20 | PATOS DE MINAS | MINAS GERAIS | Brasil | 3148004 | 31 | 33 | nan | nan | nan | Cerrado | 1.5 |
| e1eb2dd6-bdc8-3405-bc85-f9916f46dfd7 | -18.95545 | -52.46785 | 2026-06-10 04:53:00 | NOAA-20 | CASSILÂNDIA | MATO GROSSO DO SUL | Brasil | 5002902 | 50 | 33 | nan | nan | nan | Cerrado | 0.6 |
| 638b5895-bc8e-3ad9-adf1-6c0853c05522 | -22.38108 | -49.78889 | 2026-06-10 04:53:00 | NOAA-20 | LUPÉRCIO | SÃO PAULO | Brasil | 3527801 | 35 | 33 | nan | nan | nan | Mata Atlântica | 2.0 |
| a566773e-c739-3fec-bcfd-590b26d408d1 | -19.47628 | -49.28799 | 2026-06-10 04:53:00 | NOAA-20 | PRATA | MINAS GERAIS | Brasil | 3152808 | 31 | 33 | nan | nan | nan | Cerrado | 0.8 |
| 25293e28-32d2-3ca8-8e80-96c837725c3c | -18.68468 | -52.70909 | 2026-06-10 04:53:00 | NOAA-20 | CHAPADÃO DO CÉU | GOIÁS | Brasil | 5205471 | 52 | 33 | nan | nan | nan | Cerrado | 1.0 |
| e6c1d158-bf0c-35a0-9f78-33000f1eaaaf | -20.23093 | -41.90199 | 2026-06-10 04:53:00 | NOAA-20 | REDUTO | MINAS GERAIS | Brasil | 3154150 | 31 | 33 | nan | nan | nan | Mata Atlântica | 4.8 |
| 05a83560-fde6-37ec-baa8-b0daf5e970bd | -23.56507 | -47.50971 | 2026-06-10 04:55:00 | NOAA-20 | SOROCABA | SÃO PAULO | Brasil | 3552205 | 35 | 33 | nan | nan | nan | Mata Atlântica | 1.8 |
| 7abb7b7b-0c6f-374d-9cba-f495e3a47371 | -9.3045 | -45.4809 | 2026-06-10 05:00:00 | GOES-19 | SANTA FILOMENA | PIAUÍ | Brasil | 2209203 | 22 | 33 | nan | nan | nan | Cerrado | 79.8 |
| b321ae1c-cb8d-3be9-b1b9-58cdfa98e145 | -9.3234 | -45.4787 | 2026-06-10 05:00:00 | GOES-19 | SANTA FILOMENA | PIAUÍ | Brasil | 2209203 | 22 | 33 | nan | nan | nan | Cerrado | 76.1 |
| fe48e80c-1504-3bb0-9a78-bfc81ad39d99 | -9.3045 | -45.4809 | 2026-06-10 05:10:00 | GOES-19 | SANTA FILOMENA | PIAUÍ | Brasil | 2209203 | 22 | 33 | nan | nan | nan | Cerrado | 73.0 |
| 9560c30c-a526-3e6d-a177-0f32eb7f9424 | -9.3234 | -45.4787 | 2026-06-10 05:10:00 | GOES-19 | SANTA FILOMENA | PIAUÍ | Brasil | 2209203 | 22 | 33 | nan | nan | nan | Cerrado | 76.0 |
| 76c7422c-bc5f-3f71-866c-1c42aed9d831 | -9.3234 | -45.4787 | 2026-06-10 05:20:00 | GOES-19 | SANTA FILOMENA | PIAUÍ | Brasil | 2209203 | 22 | 33 | nan | nan | nan | Cerrado | 71.7 |
| ef1d1492-7420-3399-9a13-badfd9f5bbdd | -9.3045 | -45.4809 | 2026-06-10 05:20:00 | GOES-19 | SANTA FILOMENA | PIAUÍ | Brasil | 2209203 | 22 | 33 | nan | nan | nan | Cerrado | 64.9 |
| 7fdc7504-fec5-38bc-a46e-9418a904027b | -9.3234 | -45.4787 | 2026-06-10 05:30:00 | GOES-19 | SANTA FILOMENA | PIAUÍ | Brasil | 2209203 | 22 | 33 | nan | nan | nan | Cerrado | 57.5 |
| f66b5413-da07-32e5-ac44-5227d060c064 | -10.85022 | -53.74443 | 2026-06-10 05:38:00 | NOAA-21 | MARCELÂNDIA | MATO GROSSO | Brasil | 5105580 | 51 | 33 | nan | nan | nan | Amazônia | 1.4 |
| c023411d-210f-3634-8bea-d22af70c481f | -10.85615 | -53.74529 | 2026-06-10 05:38:00 | NOAA-21 | MARCELÂNDIA | MATO GROSSO | Brasil | 5105580 | 51 | 33 | nan | nan | nan | Amazônia | 1.2 |
| 9cd709a0-586c-36a5-a360-58f7b631be4e | -10.86045 | -53.7399 | 2026-06-10 05:38:00 | NOAA-21 | MARCELÂNDIA | MATO GROSSO | Brasil | 5105580 | 51 | 33 | nan | nan | nan | Amazônia | 1.8 |
| 8514f502-914c-3f3d-aeb3-fc4a8004e38f | -10.84805 | -53.74274 | 2026-06-10 05:38:00 | NOAA-21 | MARCELÂNDIA | MATO GROSSO | Brasil | 5105580 | 51 | 33 | nan | nan | nan | Amazônia | 1.2 |
| 9bb46bca-5d10-3877-9e50-55c3baae5029 | -10.85398 | -53.74362 | 2026-06-10 05:38:00 | NOAA-21 | MARCELÂNDIA | MATO GROSSO | Brasil | 5105580 | 51 | 33 | nan | nan | nan | Amazônia | 2.3 |
| 40bd0b99-63eb-3803-befe-5d5bd0da7db4 | -4.33172 | -59.63354 | 2026-06-10 07:14:00 | AQUA_M-M | BORBA | AMAZONAS | Brasil | 1300805 | 13 | 33 | nan | nan | nan | Amazônia | 6.3 |
| 519704cc-9d88-36ec-86df-1d47a2b90f8b | -12.8548 | -44.3625 | 2026-06-10 08:10:00 | GOES-19 | BAIANÓPOLIS | BAHIA | Brasil | 2902500 | 29 | 33 | nan | nan | nan | Cerrado | 40.9 |
| d88018ee-96d2-33c5-b3bc-f54ef25b919c | -6.94859 | -41.20281 | 2026-06-10 11:13:00 | TERRA_M-M | SANTO ANTÔNIO DE LISBOA | PIAUÍ | Brasil | 2209401 | 22 | 33 | nan | nan | nan | Caatinga | 9.4 |
| f76fe05c-8f58-31fc-b76f-5612ca92fba6 | -18.74223 | -40.24826 | 2026-06-10 11:15:00 | TERRA_M-M | SÃO MATEUS | ESPÍRITO SANTO | Brasil | 3204906 | 32 | 33 | nan | nan | nan | Mata Atlântica | 4.7 |
| 6401d040-68f8-3cef-9405-53f0667ed451 | -12.86361 | -44.35374 | 2026-06-10 11:15:00 | TERRA_M-M | BAIANÓPOLIS | BAHIA | Brasil | 2902500 | 29 | 33 | nan | nan | nan | Cerrado | 15.7 |
| bdb2a521-61c7-37ec-81ee-32d686b976ed | -17.43487 | -43.81532 | 2026-06-10 11:15:00 | TERRA_M-M | BOCAIÚVA | MINAS GERAIS | Brasil | 3107307 | 31 | 33 | nan | nan | nan | Cerrado | 22.0 |
| 05955806-8a3d-3d4a-a087-b3fb6e40f72d | -14.74968 | -41.67705 | 2026-06-10 11:15:00 | TERRA_M-M | PRESIDENTE JÂNIO QUADROS | BAHIA | Brasil | 2925709 | 29 | 33 | nan | nan | nan | Caatinga | 6.7 |
| 919ac729-e2fa-3ec5-ac18-1ebf3a4029b4 | -14.06275 | -53.92497 | 2026-06-10 12:51:00 | TERRA_M-T | PARANATINGA | MATO GROSSO | Brasil | 5106307 | 51 | 33 | nan | nan | nan | Cerrado | 52.1 |
| fc0a37e4-7eda-35ed-a822-e09267c96cc1 | -10.84803 | -53.74193 | 2026-06-10 12:51:00 | TERRA_M-T | MARCELÂNDIA | MATO GROSSO | Brasil | 5105580 | 51 | 33 | nan | nan | nan | Amazônia | 48.8 |
| 0e558d44-7864-3a32-9f87-8cdc94dc7452 | -8.02297 | -55.50208 | 2026-06-10 12:51:00 | TERRA_M-T | NOVO PROGRESSO | PARÁ | Brasil | 1505031 | 15 | 33 | nan | nan | nan | Amazônia | 6.5 |
| e97e2ec3-144a-3405-ab82-ecfc9480086b | -8.9427 | -45.68 | 2026-06-10 13:00:00 | GOES-19 | SANTA FILOMENA | PIAUÍ | Brasil | 2209203 | 22 | 33 | nan | nan | nan | Cerrado | 73.2 |
| 2fccc2ca-3a8d-3e7c-a5b2-413e6802e27b | -8.9427 | -45.68 | 2026-06-10 13:20:00 | GOES-19 | SANTA FILOMENA | PIAUÍ | Brasil | 2209203 | 22 | 33 | nan | nan | nan | Cerrado | 70.5 |
| 21152b74-c48f-3592-8edc-41d9fa26f46f | -6.1445 | -45.6429 | 2026-06-10 16:40:00 | GOES-19 | FERNANDO FALCÃO | MARANHÃO | Brasil | 2104081 | 21 | 33 | nan | nan | nan | Cerrado | 63.0 |


