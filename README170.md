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

## Dados Diários - Página 170

| ID | Latitude | Longitude | Data/Hora GMT | Satélite | Município | Estado | País | Município ID | Estado ID | País ID | Dias sem Chuva | Precipitação | Risco de Fogo | Bioma | FRP |
|----|----------|-----------|---------------|----------|-----------|--------|------|--------------|-----------|---------|----------------|--------------|----------------|-------|-----|
| 61bac8e1-4d1e-3637-8808-dd374fe582dc | -3.65052 | -58.77067 | 2026-08-31 16:52:00 | NOAA-20 | NOVA OLINDA DO NORTE | AMAZONAS | Brasil | 1303106 | 13 | 33 | nan | nan | nan | Amazônia | 4.7 |
| 3f475e85-2861-3a43-bee7-93f6232944db | -2.73664 | -49.29535 | 2026-08-31 16:52:00 | NOAA-20 | MOJU | PARÁ | Brasil | 1504703 | 15 | 33 | nan | nan | nan | Amazônia | 2.9 |
| 934729bb-99e3-388a-a1a6-3207305eb596 | -3.94406 | -59.33816 | 2026-08-31 16:52:00 | NOAA-20 | BORBA | AMAZONAS | Brasil | 1300805 | 13 | 33 | nan | nan | nan | Amazônia | 8.7 |
| d13fad4b-a969-39c7-9dc6-b2edeb05f8a1 | -3.11433 | -44.41535 | 2026-08-31 16:52:00 | NOAA-20 | SANTA RITA | MARANHÃO | Brasil | 2110203 | 21 | 33 | nan | nan | nan | Amazônia | 4.9 |
| f7b109b1-d8de-3a58-aa9e-a9366953b921 | -2.91241 | -45.1679 | 2026-08-31 16:52:00 | NOAA-20 | SÃO VICENTE FERRER | MARANHÃO | Brasil | 2111706 | 21 | 33 | nan | nan | nan | Amazônia | 2.0 |
| 3e228bf2-cd5a-367a-8203-775fca8936b2 | -6.79948 | -59.78489 | 2026-08-31 16:52:00 | NOAA-20 | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 6.3 |
| b88903a8-af8f-3407-a7ca-912caa2c764f | -6.79566 | -59.78551 | 2026-08-31 16:52:00 | NOAA-20 | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 10.1 |
| 67b62796-f188-3174-828b-38cf2f16c035 | -5.15335 | -46.21353 | 2026-08-31 16:52:00 | NOAA-20 | ARAME | MARANHÃO | Brasil | 2100956 | 21 | 33 | nan | nan | nan | Amazônia | 6.7 |
| bc4e05f9-5295-3744-876e-04b3c236dba2 | -6.60757 | -58.59362 | 2026-08-31 16:52:00 | NOAA-20 | MAUÉS | AMAZONAS | Brasil | 1302900 | 13 | 33 | nan | nan | nan | Amazônia | 11.6 |
| f355f15e-836e-3502-9eb4-137182ed6ea0 | -4.08444 | -45.93809 | 2026-08-31 16:52:00 | NOAA-20 | SANTA LUZIA | MARANHÃO | Brasil | 2110005 | 21 | 33 | nan | nan | nan | Amazônia | 16.7 |
| 348d2c93-8e72-3256-90e1-ed0fc71c07e4 | -6.91291 | -59.47795 | 2026-08-31 16:52:00 | NOAA-20 | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 12.1 |
| 9b124441-0ca6-3b9e-8f33-6493e2d9b609 | -3.44819 | -47.2683 | 2026-08-31 16:52:00 | NOAA-20 | PARAGOMINAS | PARÁ | Brasil | 1505502 | 15 | 33 | nan | nan | nan | Amazônia | 2.6 |
| c080d563-c61a-36fe-bc42-5f13a685844f | -5.42501 | -51.20226 | 2026-08-31 16:52:00 | NOAA-20 | SÃO FÉLIX DO XINGU | PARÁ | Brasil | 1507300 | 15 | 33 | nan | nan | nan | Amazônia | 13.2 |
| 203df2b5-0d2f-3127-a524-df60b0fe2afc | -5.87947 | -52.06719 | 2026-08-31 16:52:00 | NOAA-20 | SÃO FÉLIX DO XINGU | PARÁ | Brasil | 1507300 | 15 | 33 | nan | nan | nan | Amazônia | 97.8 |
| 0c14a60a-8a53-37b8-8701-81b57947fc38 | -3.06562 | -49.36055 | 2026-08-31 16:52:00 | NOAA-20 | MOJU | PARÁ | Brasil | 1504703 | 15 | 33 | nan | nan | nan | Amazônia | 3.8 |
| a7ffda95-bd51-34cd-831a-efa50a147664 | -6.41723 | -54.76375 | 2026-08-31 16:52:00 | NOAA-20 | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 4.0 |
| 71bc5bd4-43cd-3152-8e72-2358227e4667 | -6.12616 | -57.67128 | 2026-08-31 16:52:00 | NOAA-20 | JACAREACANGA | PARÁ | Brasil | 1503754 | 15 | 33 | nan | nan | nan | Amazônia | 17.0 |
| 6638c2f6-d303-3cda-bc0e-f8a5cd0325f9 | -3.49171 | -60.4538 | 2026-08-31 16:52:00 | NOAA-20 | MANAQUIRI | AMAZONAS | Brasil | 1302553 | 13 | 33 | nan | nan | nan | Amazônia | 3.9 |
| 38ec1705-5ef5-3585-b0c8-032eb5d7deef | 0.14102 | -60.39775 | 2026-08-31 16:52:00 | NOAA-20 | RORAINÓPOLIS | RORAIMA | Brasil | 1400472 | 14 | 33 | nan | nan | nan | Amazônia | 7.4 |
| fe7d356c-c7e4-3eb7-8be2-fb2baf4f119f | -0.9575 | -47.30954 | 2026-08-31 16:52:00 | NOAA-20 | SANTARÉM NOVO | PARÁ | Brasil | 1506906 | 15 | 33 | nan | nan | nan | Amazônia | 6.5 |
| e767b1a6-cd4a-37d9-8a38-82a0d422e20d | -3.71664 | -51.10248 | 2026-08-31 16:52:00 | NOAA-20 | PACAJÁ | PARÁ | Brasil | 1505486 | 15 | 33 | nan | nan | nan | Amazônia | 8.4 |
| 3d72a378-7b61-357a-8a0c-f12ac7807d70 | -1.68511 | -54.93976 | 2026-08-31 16:52:00 | NOAA-20 | ALENQUER | PARÁ | Brasil | 1500404 | 15 | 33 | nan | nan | nan | Amazônia | 10.7 |
| 904d0389-4303-33a9-aafe-5e976ae97a1a | -1.91187 | -44.70496 | 2026-08-31 16:52:00 | NOAA-20 | PORTO RICO DO MARANHÃO | MARANHÃO | Brasil | 2109056 | 21 | 33 | nan | nan | nan | Amazônia | 5.2 |
| d874b937-3dcc-399d-b372-a35cb0b6e19d | -7.31085 | -60.5865 | 2026-08-31 16:52:00 | NOAA-20 | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 16.1 |
| e8e64950-b35c-3ed4-b39b-2d23eaa66472 | 1.10453 | -50.97271 | 2026-08-31 16:52:00 | NOAA-20 | TARTARUGALZINHO | AMAPÁ | Brasil | 1600709 | 16 | 33 | nan | nan | nan | Amazônia | 3.7 |
| 8fbb48e4-96ec-3d8b-bcb3-bf224f4086cb | -7.00678 | -59.5611 | 2026-08-31 16:52:00 | NOAA-20 | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 5.1 |
| 4dcc121a-5b32-35de-8cde-63007ff2e156 | -0.98401 | -48.1042 | 2026-08-31 16:52:00 | NOAA-20 | VIGIA | PARÁ | Brasil | 1508209 | 15 | 33 | nan | nan | nan | Amazônia | 5.4 |
| 17da3b45-a4c7-35eb-ba73-10d0d1225920 | -5.58064 | -60.23564 | 2026-08-31 16:52:00 | NOAA-20 | NOVO ARIPUANÃ | AMAZONAS | Brasil | 1303304 | 13 | 33 | nan | nan | nan | Amazônia | 50.4 |
| eb75498f-767e-328b-bc63-b5cef2431620 | -6.86976 | -58.94556 | 2026-08-31 16:52:00 | NOAA-20 | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 7.1 |
| 12262bdf-267b-3240-8d4c-99f9efa7d040 | -6.25374 | -53.6283 | 2026-08-31 16:52:00 | NOAA-20 | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 4.6 |
| c8b16553-b4cb-30d1-accb-6fd8b1af3e69 | -3.83517 | -55.56274 | 2026-08-31 16:52:00 | NOAA-20 | AVEIRO | PARÁ | Brasil | 1501006 | 15 | 33 | nan | nan | nan | Amazônia | 27.7 |
| b4dc6564-e04a-31e0-b8a5-d7fdb1a457e4 | -3.21068 | -61.17408 | 2026-08-31 16:52:00 | NOAA-20 | MANACAPURU | AMAZONAS | Brasil | 1302504 | 13 | 33 | nan | nan | nan | Amazônia | 14.1 |
| ab9a2503-4dad-3e8a-a5a9-28cd24ba597b | -6.15047 | -52.6361 | 2026-08-31 16:52:00 | NOAA-20 | SÃO FÉLIX DO XINGU | PARÁ | Brasil | 1507300 | 15 | 33 | nan | nan | nan | Amazônia | 24.7 |
| ce75de76-fd9e-38d0-a29b-5b8cb16c51bb | -7.34439 | -60.598 | 2026-08-31 16:52:00 | NOAA-20 | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 9.8 |
| 3905f02b-7bd4-32e3-b90a-f5ee706b3d84 | -5.38746 | -47.71461 | 2026-08-31 16:52:00 | NOAA-20 | IMPERATRIZ | MARANHÃO | Brasil | 2105302 | 21 | 33 | nan | nan | nan | Cerrado | 5.2 |
| a5796345-98b4-30b0-aa6a-798c54aad6fb | -0.9865 | -48.16578 | 2026-08-31 16:52:00 | NOAA-20 | VIGIA | PARÁ | Brasil | 1508209 | 15 | 33 | nan | nan | nan | Amazônia | 26.2 |
| a171935f-7d93-3217-bcdd-2d5c94274b6f | -1.17018 | -46.77819 | 2026-08-31 16:52:00 | NOAA-20 | BRAGANÇA | PARÁ | Brasil | 1501709 | 15 | 33 | nan | nan | nan | Amazônia | 9.3 |
| 15f7ef68-0824-331d-88cd-9eaace478a59 | -6.22256 | -53.57816 | 2026-08-31 16:52:00 | NOAA-20 | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 6.8 |
| 7136ace8-f630-3150-960e-df096478dbef | -4.30867 | -49.0994 | 2026-08-31 16:52:00 | NOAA-20 | GOIANÉSIA DO PARÁ | PARÁ | Brasil | 1503093 | 15 | 33 | nan | nan | nan | Amazônia | 44.9 |
| 7f7d35ac-3375-3f16-9985-4ca9c523c2ad | -0.85267 | -47.21499 | 2026-08-31 16:52:00 | NOAA-20 | SÃO JOÃO DE PIRABAS | PARÁ | Brasil | 1507474 | 15 | 33 | nan | nan | nan | Amazônia | 31.2 |
| 2637f961-6100-3c7d-9542-788f29ebea0b | -2.83388 | -43.75132 | 2026-08-31 16:52:00 | NOAA-20 | MORROS | MARANHÃO | Brasil | 2107100 | 21 | 33 | nan | nan | nan | Cerrado | 5.8 |
| c0f04143-5da9-3fbc-9be7-a03067d133cf | -6.6532 | -59.43791 | 2026-08-31 16:52:00 | NOAA-20 | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 6.7 |
| 0ec85879-89b9-362a-9924-4c88558bdc6d | -3.37691 | -58.06287 | 2026-08-31 16:52:00 | NOAA-20 | MAUÉS | AMAZONAS | Brasil | 1302900 | 13 | 33 | nan | nan | nan | Amazônia | 12.1 |
| f1db87c3-1261-3784-a067-da29e1ca77f6 | -6.78377 | -59.78692 | 2026-08-31 16:52:00 | NOAA-20 | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 10.7 |
| 1ff1cc99-e820-3677-9bc4-e0466551653d | -2.9259 | -58.33203 | 2026-08-31 16:52:00 | NOAA-20 | SILVES | AMAZONAS | Brasil | 1304005 | 13 | 33 | nan | nan | nan | Amazônia | 2.7 |
| e5b4b099-0422-39b8-afd3-27101a8a684f | -4.25582 | -44.73986 | 2026-08-31 16:52:00 | NOAA-20 | BACABAL | MARANHÃO | Brasil | 2101202 | 21 | 33 | nan | nan | nan | Cerrado | 7.0 |
| 61f8022f-d7e9-3b7e-a6e1-d866df3d3de1 | -3.3933 | -59.38403 | 2026-08-31 16:52:00 | NOAA-20 | CAREIRO DA VÁRZEA | AMAZONAS | Brasil | 1301159 | 13 | 33 | nan | nan | nan | Amazônia | 7.3 |
| 63709e79-7a0f-3a84-95d2-199cfbad568a | -6.12225 | -57.68059 | 2026-08-31 16:52:00 | NOAA-20 | JACAREACANGA | PARÁ | Brasil | 1503754 | 15 | 33 | nan | nan | nan | Amazônia | 38.8 |
| 1ebbd75d-793d-36af-950d-84233e5e0ccd | -6.61353 | -58.5964 | 2026-08-31 16:52:00 | NOAA-20 | MAUÉS | AMAZONAS | Brasil | 1302900 | 13 | 33 | nan | nan | nan | Amazônia | 8.8 |
| 7d01246d-de1a-37d8-b9fd-d7c5b472dcfd | -6.60308 | -58.60147 | 2026-08-31 16:52:00 | NOAA-20 | MAUÉS | AMAZONAS | Brasil | 1302900 | 13 | 33 | nan | nan | nan | Amazônia | 7.5 |
| 31d8cb0e-f1dd-3cd5-8c84-3c5d359fbd36 | -6.24946 | -55.42724 | 2026-08-31 16:52:00 | NOAA-20 | ITAITUBA | PARÁ | Brasil | 1503606 | 15 | 33 | nan | nan | nan | Amazônia | 6.6 |
| fce77a56-5777-3649-b2de-4642a1b39af4 | -3.513 | -56.31407 | 2026-08-31 16:52:00 | NOAA-20 | AVEIRO | PARÁ | Brasil | 1501006 | 15 | 33 | nan | nan | nan | Amazônia | 16.0 |
| 6871fca7-a5c0-36a5-adfd-945bc3e5f2fe | -4.9644 | -55.85874 | 2026-08-31 16:52:00 | NOAA-20 | TRAIRÃO | PARÁ | Brasil | 1508050 | 15 | 33 | nan | nan | nan | Amazônia | 9.6 |
| df8f6219-aca3-3067-bd2c-10f692d9729d | -7.35419 | -60.59497 | 2026-08-31 16:52:00 | NOAA-20 | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 7.7 |
| b2a44c3d-ec74-3a73-8466-cdd1a5da7d49 | -3.79361 | -59.34784 | 2026-08-31 16:52:00 | NOAA-20 | AUTAZES | AMAZONAS | Brasil | 1300300 | 13 | 33 | nan | nan | nan | Amazônia | 39.6 |
| d9c093ef-46d6-3a3b-9faa-279e73562718 | -2.94522 | -60.90028 | 2026-08-31 16:52:00 | NOAA-20 | IRANDUBA | AMAZONAS | Brasil | 1301852 | 13 | 33 | nan | nan | nan | Amazônia | 5.9 |
| ab73ea90-497d-3080-8ea5-af0b62b01df7 | -4.0754 | -55.77728 | 2026-08-31 16:52:00 | NOAA-20 | ITAITUBA | PARÁ | Brasil | 1503606 | 15 | 33 | nan | nan | nan | Amazônia | 14.9 |
| ed9d8e96-3278-3a63-a44d-a26a657316f7 | -1.62201 | -48.62722 | 2026-08-31 16:52:00 | NOAA-20 | BARCARENA | PARÁ | Brasil | 1501303 | 15 | 33 | nan | nan | nan | Amazônia | 4.0 |
| ca15d7c1-fa39-3e41-a3a4-50ec176cbe0a | -3.32668 | -49.86897 | 2026-08-31 16:52:00 | NOAA-20 | BAIÃO | PARÁ | Brasil | 1501204 | 15 | 33 | nan | nan | nan | Amazônia | 15.7 |
| 1e2fd4d4-b66c-3121-bc1b-ff51f23387ba | -6.59713 | -58.59876 | 2026-08-31 16:52:00 | NOAA-20 | MAUÉS | AMAZONAS | Brasil | 1302900 | 13 | 33 | nan | nan | nan | Amazônia | 5.5 |
| 2917646a-0677-3294-b8c9-a67057a1f6f9 | -3.38779 | -59.38479 | 2026-08-31 16:52:00 | NOAA-20 | CAREIRO DA VÁRZEA | AMAZONAS | Brasil | 1301159 | 13 | 33 | nan | nan | nan | Amazônia | 7.3 |
| 3ed3977e-021f-3163-9aca-15b5ecfb98e5 | -1.16721 | -46.73417 | 2026-08-31 16:52:00 | NOAA-20 | BRAGANÇA | PARÁ | Brasil | 1501709 | 15 | 33 | nan | nan | nan | Amazônia | 2.2 |
| 54cc2fd9-8733-34bc-82f8-3b54ffd93ed3 | -3.61266 | -44.39723 | 2026-08-31 16:52:00 | NOAA-20 | CANTANHEDE | MARANHÃO | Brasil | 2102705 | 21 | 33 | nan | nan | nan | Cerrado | 2.4 |
| 6254cc99-93ed-3be0-9ea2-7a66d0913941 | -1.14778 | -46.45142 | 2026-08-31 16:52:00 | NOAA-20 | AUGUSTO CORRÊA | PARÁ | Brasil | 1500909 | 15 | 33 | nan | nan | nan | Amazônia | 15.1 |
| fbd82640-dd07-35c0-8aeb-84edcb988e56 | -5.88606 | -59.98037 | 2026-08-31 16:52:00 | NOAA-20 | NOVO ARIPUANÃ | AMAZONAS | Brasil | 1303304 | 13 | 33 | nan | nan | nan | Amazônia | 5.8 |
| d79624ec-3e3c-3429-b4fa-b5bd31274c93 | -6.23771 | -55.40743 | 2026-08-31 16:52:00 | NOAA-20 | ITAITUBA | PARÁ | Brasil | 1503606 | 15 | 33 | nan | nan | nan | Amazônia | 5.6 |
| 9499ca8b-553c-35cc-843b-77bc2a42654b | -1.78698 | -47.87715 | 2026-08-31 16:52:00 | NOAA-20 | SÃO DOMINGOS DO CAPIM | PARÁ | Brasil | 1507201 | 15 | 33 | nan | nan | nan | Amazônia | 6.6 |
| e3be6ba0-ffb7-32fe-869e-449d7ebcb22d | -1.75949 | -56.09217 | 2026-08-31 16:52:00 | NOAA-20 | ORIXIMINÁ | PARÁ | Brasil | 1505304 | 15 | 33 | nan | nan | nan | Amazônia | 6.5 |
| 58caa49b-9dd6-3c47-a2d9-b4d4c8db4f39 | -1.92481 | -48.16026 | 2026-08-31 16:52:00 | NOAA-20 | ACARÁ | PARÁ | Brasil | 1500206 | 15 | 33 | nan | nan | nan | Amazônia | 11.8 |
| 5c8bc4e8-df56-31a5-973a-84809685eed5 | -6.0914 | -57.7215 | 2026-08-31 16:52:00 | NOAA-20 | JACAREACANGA | PARÁ | Brasil | 1503754 | 15 | 33 | nan | nan | nan | Amazônia | 5.5 |
| 3b866b8d-5e3e-3424-9319-a9a645130dfc | -2.56538 | -47.19566 | 2026-08-31 16:52:00 | NOAA-20 | GARRAFÃO DO NORTE | PARÁ | Brasil | 1503077 | 15 | 33 | nan | nan | nan | Amazônia | 4.0 |
| 791e809d-792a-31af-bb05-a6b3e679c480 | -6.60904 | -58.60423 | 2026-08-31 16:52:00 | NOAA-20 | MAUÉS | AMAZONAS | Brasil | 1302900 | 13 | 33 | nan | nan | nan | Amazônia | 7.5 |
| 7d3022cb-0e69-3f4e-840d-80f450a796c5 | -4.38456 | -55.15628 | 2026-08-31 16:52:00 | NOAA-20 | RURÓPOLIS | PARÁ | Brasil | 1506195 | 15 | 33 | nan | nan | nan | Amazônia | 9.5 |
| 3e022206-7fdb-3108-94ed-d15ad2d1b4d6 | -6.20775 | -53.58508 | 2026-08-31 16:52:00 | NOAA-20 | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 9.1 |
| 0144fc62-2f66-3881-9ce6-24e2caad81b1 | -3.41779 | -43.37533 | 2026-08-31 16:52:00 | NOAA-20 | URBANO SANTOS | MARANHÃO | Brasil | 2112605 | 21 | 33 | nan | nan | nan | Cerrado | 7.6 |
| f4d33a88-750e-32f3-807c-a721d37d422a | -5.59847 | -51.66051 | 2026-08-31 16:52:00 | NOAA-20 | SÃO FÉLIX DO XINGU | PARÁ | Brasil | 1507300 | 15 | 33 | nan | nan | nan | Amazônia | 11.2 |
| eff439e4-4f73-3529-a6aa-02a31e76b6ce | -4.85234 | -55.82995 | 2026-08-31 16:52:00 | NOAA-20 | TRAIRÃO | PARÁ | Brasil | 1508050 | 15 | 33 | nan | nan | nan | Amazônia | 7.1 |
| 5542da1f-df6e-3594-92d5-7ccec6b2e366 | -3.70566 | -58.10983 | 2026-08-31 16:52:00 | NOAA-20 | MAUÉS | AMAZONAS | Brasil | 1302900 | 13 | 33 | nan | nan | nan | Amazônia | 51.6 |
| eab022f9-cb8d-30e2-a3e9-5fba8b6124d7 | -3.6127 | -59.06731 | 2026-08-31 16:52:00 | NOAA-20 | AUTAZES | AMAZONAS | Brasil | 1300300 | 13 | 33 | nan | nan | nan | Amazônia | 18.3 |
| 1c89c92e-ee1d-394f-ab43-145ff7124090 | -6.10923 | -57.86635 | 2026-08-31 16:52:00 | NOAA-20 | JACAREACANGA | PARÁ | Brasil | 1503754 | 15 | 33 | nan | nan | nan | Amazônia | 11.0 |
| 222a6c04-ec6f-333f-be15-a25b9ce16cb6 | -3.21615 | -61.16848 | 2026-08-31 16:52:00 | NOAA-20 | MANACAPURU | AMAZONAS | Brasil | 1302504 | 13 | 33 | nan | nan | nan | Amazônia | 14.1 |
| 23255604-a267-3a60-8641-427069951304 | -4.23067 | -59.86465 | 2026-08-31 16:52:00 | NOAA-20 | BORBA | AMAZONAS | Brasil | 1300805 | 13 | 33 | nan | nan | nan | Amazônia | 4.4 |
| 1b68cdf7-7672-3b17-9c2b-dc2e1597fb85 | -6.13365 | -53.5364 | 2026-08-31 16:52:00 | NOAA-20 | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 80.9 |
| bf25f0f3-a16f-3752-815b-10d911a7cb16 | -1.09915 | -48.05552 | 2026-08-31 16:52:00 | NOAA-20 | SANTO ANTÔNIO DO TAUÁ | PARÁ | Brasil | 1507003 | 15 | 33 | nan | nan | nan | Amazônia | 21.4 |
| 66e41fc2-62e1-345f-8980-50b8731c5423 | -1.63769 | -48.16258 | 2026-08-31 16:52:00 | NOAA-20 | BUJARU | PARÁ | Brasil | 1501907 | 15 | 33 | nan | nan | nan | Amazônia | 19.3 |
| 4bed6d81-027d-36a3-8959-d22474657cf9 | -6.80394 | -59.45835 | 2026-08-31 16:52:00 | NOAA-20 | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 6.2 |
| 392bf00a-097b-37e4-be6e-23febdb5d09a | 0.25888 | -51.48624 | 2026-08-31 16:52:00 | NOAA-20 | SANTANA | AMAPÁ | Brasil | 1600600 | 16 | 33 | nan | nan | nan | Amazônia | 4.1 |
| 82a29546-0c50-3950-91be-3db7be7a509a | -4.84795 | -55.8307 | 2026-08-31 16:52:00 | NOAA-20 | TRAIRÃO | PARÁ | Brasil | 1508050 | 15 | 33 | nan | nan | nan | Amazônia | 7.1 |
| b16bde4d-d97f-3113-98ca-a9290bef58eb | -5.25169 | -55.88858 | 2026-08-31 16:52:00 | NOAA-20 | TRAIRÃO | PARÁ | Brasil | 1508050 | 15 | 33 | nan | nan | nan | Amazônia | 11.9 |
| f5f6ffe5-48fb-3f62-b72c-d9bba449d696 | -3.18567 | -48.02239 | 2026-08-31 16:52:00 | NOAA-20 | PARAGOMINAS | PARÁ | Brasil | 1505502 | 15 | 33 | nan | nan | nan | Amazônia | 11.5 |
| e40605ed-59bc-38ba-835e-6cd6f44cbcc8 | -4.21243 | -48.60739 | 2026-08-31 16:52:00 | NOAA-20 | RONDON DO PARÁ | PARÁ | Brasil | 1506187 | 15 | 33 | nan | nan | nan | Amazônia | 22.2 |
| 7ec24497-bbd0-37f1-8b49-e4f00da2575d | -6.61961 | -58.38436 | 2026-08-31 16:52:00 | NOAA-20 | JACAREACANGA | PARÁ | Brasil | 1503754 | 15 | 33 | nan | nan | nan | Amazônia | 5.9 |
| 24d754f2-bc81-3b88-b112-df5480bd30f3 | -6.06373 | -53.83453 | 2026-08-31 16:52:00 | NOAA-20 | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 9.4 |
| 987868bb-fc84-39c7-8d69-15e0ef854400 | -4.15884 | -60.70931 | 2026-08-31 16:52:00 | NOAA-20 | CAREIRO | AMAZONAS | Brasil | 1301100 | 13 | 33 | nan | nan | nan | Amazônia | 7.6 |
| 4ada81f0-14c7-3eb5-9409-fb454bd04992 | -6.59665 | -58.59526 | 2026-08-31 16:52:00 | NOAA-20 | MAUÉS | AMAZONAS | Brasil | 1302900 | 13 | 33 | nan | nan | nan | Amazônia | 5.5 |
| da929c9f-f003-39e1-8e5d-b23d0614485a | -6.88154 | -56.51124 | 2026-08-31 16:52:00 | NOAA-20 | ITAITUBA | PARÁ | Brasil | 1503606 | 15 | 33 | nan | nan | nan | Amazônia | 27.5 |
| 4f1a4e48-1b45-3bb7-ac10-785204e8c368 | -7.30754 | -60.58008 | 2026-08-31 16:52:00 | NOAA-20 | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 12.7 |
| c9683250-fa0e-3922-9730-f5586643ca91 | -4.36893 | -55.4338 | 2026-08-31 16:52:00 | NOAA-20 | RURÓPOLIS | PARÁ | Brasil | 1506195 | 15 | 33 | nan | nan | nan | Amazônia | 4.1 |
| 1ee89fe5-af6c-3f14-8d7e-780636cd3619 | -4.59904 | -42.92676 | 2026-08-31 16:52:00 | NOAA-20 | CAXIAS | MARANHÃO | Brasil | 2103000 | 21 | 33 | nan | nan | nan | Cerrado | 46.7 |
| 695e0fa7-5ab0-3384-931f-ae0552b2d660 | -3.94437 | -44.74931 | 2026-08-31 16:52:00 | NOAA-20 | BACABAL | MARANHÃO | Brasil | 2101202 | 21 | 33 | nan | nan | nan | Amazônia | 6.8 |


[Clique aqui para ver as próximas entradas](README171.md)
