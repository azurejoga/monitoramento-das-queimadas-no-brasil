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

## Dados Diários - Página 12

| ID | Latitude | Longitude | Data/Hora GMT | Satélite | Município | Estado | País | Município ID | Estado ID | País ID | Dias sem Chuva | Precipitação | Risco de Fogo | Bioma | FRP |
|----|----------|-----------|---------------|----------|-----------|--------|------|--------------|-----------|---------|----------------|--------------|----------------|-------|-----|
| 5dbfe173-9662-3df8-9afd-cba3be9d5b10 | -6.90982 | -43.5188 | 2024-12-11 03:40:00 | NOAA-20 | JERUMENHA | PIAUÍ | Brasil | 2205300 | 22 | 33 | nan | nan | nan | Cerrado | 1.8 |
| f01767ae-630e-3020-92c5-8b7851d0f369 | -9.97188 | -36.47695 | 2024-12-11 03:40:00 | NOAA-20 | SÃO SEBASTIÃO | ALAGOAS | Brasil | 2708808 | 27 | 33 | nan | nan | nan | Mata Atlântica | 2.9 |
| 597f1f5f-8ee4-3e5b-8968-2cd7dbaaf8f0 | -5.42601 | -39.53162 | 2024-12-11 03:40:00 | NOAA-20 | SENADOR POMPEU | CEARÁ | Brasil | 2312700 | 23 | 33 | nan | nan | nan | Caatinga | 1.5 |
| 64520700-ec3c-3a5a-9148-8021140810aa | -8.2343 | -35.00461 | 2024-12-11 03:40:00 | NOAA-20 | CABO DE SANTO AGOSTINHO | PERNAMBUCO | Brasil | 2602902 | 26 | 33 | nan | nan | nan | Mata Atlântica | 1.2 |
| c773d4a8-b441-3cd9-ac95-06148db67e5a | -6.11655 | -42.52722 | 2024-12-11 03:40:00 | NOAA-20 | JARDIM DO MULATO | PIAUÍ | Brasil | 2205250 | 22 | 33 | nan | nan | nan | Caatinga | 6.1 |
| 488d6d99-de9e-3152-a1d6-626e550f558c | -7.8632 | -43.08889 | 2024-12-11 03:40:00 | NOAA-20 | RIO GRANDE DO PIAUÍ | PIAUÍ | Brasil | 2209005 | 22 | 33 | nan | nan | nan | Caatinga | 2.2 |
| 014d009a-d401-38b3-b4b2-4433883dd4e4 | -9.38729 | -36.00888 | 2024-12-11 03:40:00 | NOAA-20 | CAPELA | ALAGOAS | Brasil | 2701704 | 27 | 33 | nan | nan | nan | Mata Atlântica | 1.8 |
| ea93dc07-e606-3477-9393-328570c6f565 | -7.12663 | -40.33816 | 2024-12-11 03:40:00 | NOAA-20 | CAMPOS SALES | CEARÁ | Brasil | 2302701 | 23 | 33 | nan | nan | nan | Caatinga | 0.6 |
| cb40262f-99ba-34bd-b4a0-206713bff638 | -5.42335 | -39.52967 | 2024-12-11 03:40:00 | NOAA-20 | SENADOR POMPEU | CEARÁ | Brasil | 2312700 | 23 | 33 | nan | nan | nan | Caatinga | 1.7 |
| 94c402f4-b015-389d-8f24-d2de0ab827af | -7.75015 | -35.25559 | 2024-12-11 03:40:00 | NOAA-20 | NAZARÉ DA MATA | PERNAMBUCO | Brasil | 2609501 | 26 | 33 | nan | nan | nan | Mata Atlântica | 2.4 |
| ac5ea080-2f9d-3413-94e0-89f1066c6d96 | -8.10805 | -35.07449 | 2024-12-11 03:40:00 | NOAA-20 | MORENO | PERNAMBUCO | Brasil | 2609402 | 26 | 33 | nan | nan | nan | Mata Atlântica | 2.8 |
| 7795275f-e5a4-3306-a19b-9f8489fb8078 | -10.50882 | -44.93684 | 2024-12-11 03:40:00 | NOAA-20 | CORRENTE | PIAUÍ | Brasil | 2202901 | 22 | 33 | nan | nan | nan | Cerrado | 1.6 |
| a99d3581-0d6e-3d27-b278-4e3cc739fde1 | -7.529 | -35.1072 | 2024-12-11 03:40:00 | NOAA-20 | ITAMBÉ | PERNAMBUCO | Brasil | 2607653 | 26 | 33 | nan | nan | nan | Mata Atlântica | 7.8 |
| 61acdeba-fca4-38e4-9dfd-1b423fdaa51e | -6.89922 | -43.51992 | 2024-12-11 03:40:00 | NOAA-20 | JERUMENHA | PIAUÍ | Brasil | 2205300 | 22 | 33 | nan | nan | nan | Cerrado | 9.5 |
| e878250e-c527-3dd3-90a0-ea834a77bb88 | -6.96796 | -43.00462 | 2024-12-11 03:40:00 | NOAA-20 | FLORIANO | PIAUÍ | Brasil | 2203909 | 22 | 33 | nan | nan | nan | Caatinga | 10.0 |
| d938bfa7-55df-3160-a7a0-b576dab03160 | -9.94148 | -36.3064 | 2024-12-11 03:40:00 | NOAA-20 | TEOTÔNIO VILELA | ALAGOAS | Brasil | 2709152 | 27 | 33 | nan | nan | nan | Mata Atlântica | 6.5 |
| a832efb9-5a28-38c1-9183-4f494006d9ee | -7.34359 | -35.12022 | 2024-12-11 03:40:00 | NOAA-20 | PEDRAS DE FOGO | PARAÍBA | Brasil | 2511202 | 25 | 33 | nan | nan | nan | Mata Atlântica | 0.4 |
| 021944ad-82ed-3952-b2f5-b295e533e639 | -6.11783 | -42.54897 | 2024-12-11 03:40:00 | NOAA-20 | JARDIM DO MULATO | PIAUÍ | Brasil | 2205250 | 22 | 33 | nan | nan | nan | Caatinga | 1.2 |
| ed0b4c6b-4990-3663-9524-192627267225 | -9.07127 | -35.70827 | 2024-12-11 03:40:00 | NOAA-20 | JOAQUIM GOMES | ALAGOAS | Brasil | 2703809 | 27 | 33 | nan | nan | nan | Mata Atlântica | 0.5 |
| 8e8dc06d-ef37-3605-9d28-618076f31d49 | -5.42205 | -39.53096 | 2024-12-11 03:40:00 | NOAA-20 | SENADOR POMPEU | CEARÁ | Brasil | 2312700 | 23 | 33 | nan | nan | nan | Caatinga | 1.5 |
| 5f9777b8-b0e1-3db3-8073-bf9210977e8e | -4.462 | -41.56394 | 2024-12-11 03:40:00 | NOAA-20 | PEDRO II | PIAUÍ | Brasil | 2207900 | 22 | 33 | nan | nan | nan | Caatinga | 1.1 |
| 4830c979-8264-3919-ba81-d48ce468d1df | -6.12743 | -42.55054 | 2024-12-11 03:40:00 | NOAA-20 | JARDIM DO MULATO | PIAUÍ | Brasil | 2205250 | 22 | 33 | nan | nan | nan | Caatinga | 10.6 |
| 1c9cc9ea-fa1b-3ff5-8321-a75ea8d1d02d | -5.95027 | -38.32674 | 2024-12-11 03:40:00 | NOAA-20 | ERERÊ | CEARÁ | Brasil | 2304277 | 23 | 33 | nan | nan | nan | Caatinga | 2.3 |
| 2b52118f-8c36-302b-b570-556eabddf86f | -6.87619 | -35.28397 | 2024-12-11 03:40:00 | NOAA-20 | CUITÉ DE MAMANGUAPE | PARAÍBA | Brasil | 2505238 | 25 | 33 | nan | nan | nan | Caatinga | 1.2 |
| fb43fa06-a0ad-35ca-a237-7a77e9698360 | -6.89518 | -43.51318 | 2024-12-11 03:40:00 | NOAA-20 | JERUMENHA | PIAUÍ | Brasil | 2205300 | 22 | 33 | nan | nan | nan | Cerrado | 34.6 |
| 9a143ac1-c17c-3c92-b236-2919af734802 | -11.49597 | -40.47729 | 2024-12-11 03:40:00 | NOAA-20 | MIGUEL CALMON | BAHIA | Brasil | 2921203 | 29 | 33 | nan | nan | nan | Caatinga | 1.4 |
| 16620ebe-0fbf-3cdb-b1e1-fd923aa12b3a | -6.24387 | -35.18012 | 2024-12-11 03:40:00 | NOAA-20 | GOIANINHA | RIO GRANDE DO NORTE | Brasil | 2404200 | 24 | 33 | nan | nan | nan | Mata Atlântica | 3.7 |
| 73ac39f9-6a0c-3c6b-96d9-77e8599b7605 | -6.26328 | -43.55931 | 2024-12-11 03:40:00 | NOAA-20 | LAGOA DO MATO | MARANHÃO | Brasil | 2105922 | 21 | 33 | nan | nan | nan | Cerrado | 2.2 |
| 93955f43-2010-3200-b37a-635917cafef9 | -5.97964 | -44.60355 | 2024-12-11 03:40:00 | NOAA-20 | TUNTUM | MARANHÃO | Brasil | 2112308 | 21 | 33 | nan | nan | nan | Cerrado | 9.4 |
| f3d5e557-685b-37f1-8868-d4d7b3142346 | -6.12284 | -42.54584 | 2024-12-11 03:40:00 | NOAA-20 | JARDIM DO MULATO | PIAUÍ | Brasil | 2205250 | 22 | 33 | nan | nan | nan | Caatinga | 20.2 |
| fffe7b4c-4d4f-37d6-b267-7e1fd8e17b39 | -10.5926 | -44.98126 | 2024-12-11 03:40:00 | NOAA-20 | CORRENTE | PIAUÍ | Brasil | 2202901 | 22 | 33 | nan | nan | nan | Cerrado | 1.0 |
| f2189d55-b49e-345a-b915-09cf2aa04f1f | -10.40694 | -36.90342 | 2024-12-11 03:40:00 | NOAA-20 | JAPARATUBA | SERGIPE | Brasil | 2803302 | 28 | 33 | nan | nan | nan | Mata Atlântica | 1.2 |
| a45d1824-1f93-37d2-95ca-7f84685e7237 | -9.59559 | -36.40887 | 2024-12-11 03:40:00 | NOAA-20 | TANQUE D'ARCA | ALAGOAS | Brasil | 2709004 | 27 | 33 | nan | nan | nan | Mata Atlântica | 6.5 |
| c68fe4a2-e771-34a9-9a8d-69c4701984f8 | -6.11804 | -42.54507 | 2024-12-11 03:40:00 | NOAA-20 | JARDIM DO MULATO | PIAUÍ | Brasil | 2205250 | 22 | 33 | nan | nan | nan | Caatinga | 0.9 |
| 7c2aee8d-2f42-3d8e-8492-2e6457afa63f | -7.91846 | -35.20076 | 2024-12-11 03:40:00 | NOAA-20 | PAUDALHO | PERNAMBUCO | Brasil | 2610608 | 26 | 33 | nan | nan | nan | Mata Atlântica | 13.5 |
| 2b5b706e-0a37-3818-9c7d-fe625319b6ee | -11.04417 | -41.98252 | 2024-12-11 03:40:00 | NOAA-20 | JUSSARA | BAHIA | Brasil | 2918506 | 29 | 33 | nan | nan | nan | Caatinga | 1.2 |
| 8572a4d6-aa1a-3f4f-a40a-d13fb89d65da | -6.10117 | -44.04572 | 2024-12-11 03:40:00 | NOAA-20 | COLINAS | MARANHÃO | Brasil | 2103505 | 21 | 33 | nan | nan | nan | Cerrado | 0.8 |
| 3bd3b9ad-cff3-382a-bcfb-cd68dd8702b4 | -6.26539 | -43.56267 | 2024-12-11 03:40:00 | NOAA-20 | LAGOA DO MATO | MARANHÃO | Brasil | 2105922 | 21 | 33 | nan | nan | nan | Cerrado | 2.0 |
| b395ce03-2f0d-3e6c-be92-7ad26762362e | -6.94357 | -43.00051 | 2024-12-11 03:40:00 | NOAA-20 | FLORIANO | PIAUÍ | Brasil | 2203909 | 22 | 33 | nan | nan | nan | Caatinga | 7.3 |
| 50a0e44b-ee89-3720-bd63-4ed99b873994 | -12.12352 | -39.39846 | 2024-12-11 03:40:00 | NOAA-20 | SERRA PRETA | BAHIA | Brasil | 2930402 | 29 | 33 | nan | nan | nan | Caatinga | 0.8 |
| a08194da-cc6d-3575-9a4a-a71e72cab84f | -12.12423 | -39.39428 | 2024-12-11 03:40:00 | NOAA-20 | SERRA PRETA | BAHIA | Brasil | 2930402 | 29 | 33 | nan | nan | nan | Caatinga | 1.0 |
| cd941b5e-5c21-388a-8991-d05409bfd49e | -5.59837 | -41.32967 | 2024-12-11 03:40:00 | NOAA-20 | SÃO MIGUEL DO TAPUIO | PIAUÍ | Brasil | 2210409 | 22 | 33 | nan | nan | nan | Caatinga | 1.5 |
| 9e016bda-0c8d-3b3e-a44f-a97c84a51aa9 | -7.07247 | -39.78883 | 2024-12-11 03:40:00 | NOAA-20 | SANTANA DO CARIRI | CEARÁ | Brasil | 2312106 | 23 | 33 | nan | nan | nan | Caatinga | 1.2 |
| 541014d9-4444-31b5-bee7-43e0058b0625 | -6.9689 | -42.99916 | 2024-12-11 03:40:00 | NOAA-20 | FLORIANO | PIAUÍ | Brasil | 2203909 | 22 | 33 | nan | nan | nan | Caatinga | 23.2 |
| 0a75cdc5-6168-3c12-92cf-d0b4ced75e08 | -10.93917 | -40.50645 | 2024-12-11 03:40:00 | NOAA-20 | MIRANGABA | BAHIA | Brasil | 2921401 | 29 | 33 | nan | nan | nan | Caatinga | 0.9 |
| 3ceec2a2-d984-3290-b06c-f9a220b1d95f | -5.95036 | -38.32847 | 2024-12-11 03:40:00 | NOAA-20 | ERERÊ | CEARÁ | Brasil | 2304277 | 23 | 33 | nan | nan | nan | Caatinga | 5.2 |
| 08c25763-b385-3d99-b35a-17b199510b97 | -6.12611 | -42.52894 | 2024-12-11 03:40:00 | NOAA-20 | JARDIM DO MULATO | PIAUÍ | Brasil | 2205250 | 22 | 33 | nan | nan | nan | Caatinga | 12.3 |
| 3bca59e9-13d0-3d3e-b726-f3bb5fd094e6 | -9.59283 | -36.40481 | 2024-12-11 03:40:00 | NOAA-20 | TANQUE D'ARCA | ALAGOAS | Brasil | 2709004 | 27 | 33 | nan | nan | nan | Mata Atlântica | 0.7 |
| 2dddd656-a984-3bfb-a6ec-1ce1cd2d75f8 | -9.97132 | -36.48047 | 2024-12-11 03:40:00 | NOAA-20 | SÃO SEBASTIÃO | ALAGOAS | Brasil | 2708808 | 27 | 33 | nan | nan | nan | Mata Atlântica | 2.9 |
| e26a37b8-5e02-3700-97b7-e041cbe9eb6f | -5.68688 | -39.61065 | 2024-12-11 03:40:00 | NOAA-20 | MOMBAÇA | CEARÁ | Brasil | 2308500 | 23 | 33 | nan | nan | nan | Caatinga | 0.8 |
| 4e15a94e-4bc1-3174-8d80-e1c8cdf047a4 | -5.30012 | -43.28382 | 2024-12-11 03:40:00 | NOAA-20 | MATÕES | MARANHÃO | Brasil | 2106607 | 21 | 33 | nan | nan | nan | Cerrado | 2.2 |
| 3bc53d0d-5054-36d9-af4f-94efcf6cd4aa | -9.78106 | -43.99089 | 2024-12-11 03:40:00 | NOAA-20 | MORRO CABEÇA NO TEMPO | PIAUÍ | Brasil | 2206654 | 22 | 33 | nan | nan | nan | Cerrado | 2.0 |
| 3fcb376c-dda2-3493-87f6-c45a5d276d23 | -7.92838 | -35.20233 | 2024-12-11 03:40:00 | NOAA-20 | PAUDALHO | PERNAMBUCO | Brasil | 2610608 | 26 | 33 | nan | nan | nan | Mata Atlântica | 4.0 |
| 8679c307-ecad-3a16-8bcd-c9a6140db2ca | -7.86316 | -35.2059 | 2024-12-11 03:40:00 | NOAA-20 | PAUDALHO | PERNAMBUCO | Brasil | 2610608 | 26 | 33 | nan | nan | nan | Mata Atlântica | 6.6 |
| 79a1de3f-7d95-34a3-9fed-88611217e26f | -6.03346 | -42.52332 | 2024-12-11 03:40:00 | NOAA-20 | HUGO NAPOLEÃO | PIAUÍ | Brasil | 2204600 | 22 | 33 | nan | nan | nan | Caatinga | 1.7 |
| 0f2e750e-80b4-30ef-8eee-d7abb53db739 | -7.92507 | -35.20181 | 2024-12-11 03:40:00 | NOAA-20 | PAUDALHO | PERNAMBUCO | Brasil | 2610608 | 26 | 33 | nan | nan | nan | Mata Atlântica | 4.0 |
| 4beacb06-ffcd-31f0-92bc-c7df780d001e | -6.12465 | -42.53549 | 2024-12-11 03:40:00 | NOAA-20 | JARDIM DO MULATO | PIAUÍ | Brasil | 2205250 | 22 | 33 | nan | nan | nan | Caatinga | 20.6 |
| 3a6c875e-e2ef-3c03-9675-e7ceaaec72f6 | -7.86169 | -43.09097 | 2024-12-11 03:40:00 | NOAA-20 | RIO GRANDE DO PIAUÍ | PIAUÍ | Brasil | 2209005 | 22 | 33 | nan | nan | nan | Caatinga | 2.5 |
| feaba3ed-0b0c-350d-9056-5bf40aac1df6 | -6.12133 | -42.52808 | 2024-12-11 03:40:00 | NOAA-20 | JARDIM DO MULATO | PIAUÍ | Brasil | 2205250 | 22 | 33 | nan | nan | nan | Caatinga | 6.1 |
| 61c7e49c-3341-3c9d-869a-ed712678c911 | -6.89417 | -43.51904 | 2024-12-11 03:40:00 | NOAA-20 | JERUMENHA | PIAUÍ | Brasil | 2205300 | 22 | 33 | nan | nan | nan | Cerrado | 24.2 |
| f41947d1-0f03-370b-8c75-c086101696f3 | -7.8637 | -35.20243 | 2024-12-11 03:40:00 | NOAA-20 | PAUDALHO | PERNAMBUCO | Brasil | 2610608 | 26 | 33 | nan | nan | nan | Mata Atlântica | 6.6 |
| 70fd79c1-808d-3370-b6d9-44f935a7bb8b | -11.75117 | -41.14281 | 2024-12-11 03:40:00 | NOAA-20 | MORRO DO CHAPÉU | BAHIA | Brasil | 2921708 | 29 | 33 | nan | nan | nan | Caatinga | 1.6 |
| f4cbbbc2-8619-3216-ba06-010457863d12 | -9.94424 | -36.31044 | 2024-12-11 03:40:00 | NOAA-20 | TEOTÔNIO VILELA | ALAGOAS | Brasil | 2709152 | 27 | 33 | nan | nan | nan | Mata Atlântica | 4.3 |
| bbb99fba-fc42-3e32-852b-57de8f28591a | -8.99327 | -35.51396 | 2024-12-11 03:40:00 | NOAA-20 | JUNDIÁ | ALAGOAS | Brasil | 2703908 | 27 | 33 | nan | nan | nan | Mata Atlântica | 1.3 |
| 9525a8f0-1805-395e-abd6-2d0fe80b2ebb | -6.12854 | -42.54144 | 2024-12-11 03:40:00 | NOAA-20 | JARDIM DO MULATO | PIAUÍ | Brasil | 2205250 | 22 | 33 | nan | nan | nan | Caatinga | 20.6 |
| 78d460b7-2932-3906-b6ae-8d65f23d57df | -6.90784 | -43.50011 | 2024-12-11 03:40:00 | NOAA-20 | JERUMENHA | PIAUÍ | Brasil | 2205300 | 22 | 33 | nan | nan | nan | Cerrado | 8.1 |
| d9c1c85a-7daa-379b-9164-ba05412c86a8 | -5.98029 | -44.59991 | 2024-12-11 03:40:00 | NOAA-20 | COLINAS | MARANHÃO | Brasil | 2103505 | 21 | 33 | nan | nan | nan | Cerrado | 8.3 |
| d5939d11-943c-3114-af4a-8bfe4ce8e8d4 | -10.59199 | -44.9845 | 2024-12-11 03:40:00 | NOAA-20 | CORRENTE | PIAUÍ | Brasil | 2202901 | 22 | 33 | nan | nan | nan | Cerrado | 0.6 |
| fdc92614-b416-33e0-a7ff-543248a56882 | -6.12263 | -42.54975 | 2024-12-11 03:40:00 | NOAA-20 | JARDIM DO MULATO | PIAUÍ | Brasil | 2205250 | 22 | 33 | nan | nan | nan | Caatinga | 10.6 |
| 5ec7944e-f61b-358a-aa02-51486d19cceb | -7.86647 | -35.20642 | 2024-12-11 03:40:00 | NOAA-20 | PAUDALHO | PERNAMBUCO | Brasil | 2610608 | 26 | 33 | nan | nan | nan | Mata Atlântica | 6.6 |
| 3d61a504-c8a9-3f3b-a927-9e4cacc20463 | -6.18057 | -35.3013 | 2024-12-11 03:40:00 | NOAA-20 | SÃO JOSÉ DE MIPIBU | RIO GRANDE DO NORTE | Brasil | 2412203 | 24 | 33 | nan | nan | nan | Mata Atlântica | 1.0 |
| b9c3e6be-5134-3334-a435-76066b0f0b50 | -6.94108 | -43.54142 | 2024-12-11 03:40:00 | NOAA-20 | JERUMENHA | PIAUÍ | Brasil | 2205300 | 22 | 33 | nan | nan | nan | Cerrado | 0.7 |
| 3239bfaf-2bba-38a5-a504-13571e042745 | -6.95915 | -42.99756 | 2024-12-11 03:40:00 | NOAA-20 | FLORIANO | PIAUÍ | Brasil | 2203909 | 22 | 33 | nan | nan | nan | Caatinga | 34.4 |
| 992a94a6-8c85-356d-acc4-7fdef9f3058c | -9.00517 | -36.19099 | 2024-12-11 03:40:00 | NOAA-20 | CANHOTINHO | PERNAMBUCO | Brasil | 2603702 | 26 | 33 | nan | nan | nan | Mata Atlântica | 0.6 |
| 67a8b5f6-ae6a-372f-8968-efb7536f80de | -6.90734 | -43.50304 | 2024-12-11 03:40:00 | NOAA-20 | JERUMENHA | PIAUÍ | Brasil | 2205300 | 22 | 33 | nan | nan | nan | Cerrado | 8.1 |
| 6a7415c7-169f-30a3-929a-5e3baadba097 | -6.12671 | -42.55191 | 2024-12-11 03:40:00 | NOAA-20 | JARDIM DO MULATO | PIAUÍ | Brasil | 2205250 | 22 | 33 | nan | nan | nan | Caatinga | 20.2 |
| 54e9033a-f925-35cb-b6c1-d1e53fdc06b7 | -6.11711 | -42.55036 | 2024-12-11 03:40:00 | NOAA-20 | JARDIM DO MULATO | PIAUÍ | Brasil | 2205250 | 22 | 33 | nan | nan | nan | Caatinga | 0.9 |
| 6d546c96-178a-3715-b046-29435a947cab | -8.57095 | -35.52165 | 2024-12-11 03:40:00 | NOAA-20 | ÁGUA PRETA | PERNAMBUCO | Brasil | 2600401 | 26 | 33 | nan | nan | nan | Mata Atlântica | 0.7 |
| d6e08019-4b74-3820-b34f-39f34fbd6b15 | -9.38674 | -36.01237 | 2024-12-11 03:40:00 | NOAA-20 | CAPELA | ALAGOAS | Brasil | 2701704 | 27 | 33 | nan | nan | nan | Mata Atlântica | 1.8 |
| 329b0be8-7d87-3e0c-8f27-19ac747071da | -7.47535 | -34.8424 | 2024-12-11 03:40:00 | NOAA-20 | PITIMBU | PARAÍBA | Brasil | 2511905 | 25 | 33 | nan | nan | nan | Mata Atlântica | 1.2 |
| 60203423-a631-3420-9012-de225902536c | -11.97773 | -38.40356 | 2024-12-11 03:40:00 | NOAA-20 | ALAGOINHAS | BAHIA | Brasil | 2900702 | 29 | 33 | nan | nan | nan | Caatinga | 1.0 |
| dcaa5b70-06f7-32b8-8512-9391e703523d | -8.10859 | -35.07101 | 2024-12-11 03:40:00 | NOAA-20 | MORENO | PERNAMBUCO | Brasil | 2609402 | 26 | 33 | nan | nan | nan | Mata Atlântica | 2.8 |
| 4128275f-c302-3acd-828e-844952389844 | -6.97378 | -42.99997 | 2024-12-11 03:40:00 | NOAA-20 | FLORIANO | PIAUÍ | Brasil | 2203909 | 22 | 33 | nan | nan | nan | Caatinga | 23.2 |
| f40f545c-ead6-3b23-9730-df23f4bd793f | -8.94383 | -35.67725 | 2024-12-11 03:40:00 | NOAA-20 | NOVO LINO | ALAGOAS | Brasil | 2705606 | 27 | 33 | nan | nan | nan | Mata Atlântica | 3.1 |
| 755a9699-9ac8-36f5-bb1c-71a577eb8245 | -6.12351 | -42.54446 | 2024-12-11 03:40:00 | NOAA-20 | JARDIM DO MULATO | PIAUÍ | Brasil | 2205250 | 22 | 33 | nan | nan | nan | Caatinga | 27.3 |
| 602fac70-9b9d-3d88-bf47-4e57dde99dea | -6.95332 | -43.00219 | 2024-12-11 03:40:00 | NOAA-20 | FLORIANO | PIAUÍ | Brasil | 2203909 | 22 | 33 | nan | nan | nan | Caatinga | 18.6 |
| b3e1ce66-244f-397d-9975-a32eaa2b465b | -7.79152 | -35.23013 | 2024-12-11 03:40:00 | NOAA-20 | TRACUNHAÉM | PERNAMBUCO | Brasil | 2615508 | 26 | 33 | nan | nan | nan | Mata Atlântica | 1.0 |
| 4a3f85ee-f10d-34d5-a62b-5c6a8a63e541 | -7.21174 | -39.77404 | 2024-12-11 03:40:00 | NOAA-20 | SANTANA DO CARIRI | CEARÁ | Brasil | 2312106 | 23 | 33 | nan | nan | nan | Caatinga | 4.2 |
| 718874a2-7978-3cba-9576-b5451cba0309 | -6.49871 | -39.0158 | 2024-12-11 03:40:00 | NOAA-20 | CEDRO | CEARÁ | Brasil | 2303808 | 23 | 33 | nan | nan | nan | Caatinga | 0.9 |
| e333e459-28f6-3f84-9129-a09ac10a78c3 | -6.89621 | -43.50724 | 2024-12-11 03:40:00 | NOAA-20 | JERUMENHA | PIAUÍ | Brasil | 2205300 | 22 | 33 | nan | nan | nan | Cerrado | 20.0 |
| fc77f6a0-05fa-39d9-920c-323e62809965 | -6.96985 | -42.9937 | 2024-12-11 03:40:00 | NOAA-20 | FLORIANO | PIAUÍ | Brasil | 2203909 | 22 | 33 | nan | nan | nan | Caatinga | 23.2 |
| 162b4f67-3030-39c2-b237-f05bb2677110 | -5.94955 | -38.33103 | 2024-12-11 03:40:00 | NOAA-20 | ERERÊ | CEARÁ | Brasil | 2304277 | 23 | 33 | nan | nan | nan | Caatinga | 2.3 |
| 6dc2f569-0c66-3573-b1fb-cdca94b86357 | -7.37571 | -35.19628 | 2024-12-11 03:40:00 | NOAA-20 | JURIPIRANGA | PARAÍBA | Brasil | 2507903 | 25 | 33 | nan | nan | nan | Mata Atlântica | 1.3 |
| b2d57ce1-4b12-3fa2-bd8f-d1bf0a40c80f | -8.07244 | -34.97582 | 2024-12-11 03:40:00 | NOAA-20 | RECIFE | PERNAMBUCO | Brasil | 2611606 | 26 | 33 | nan | nan | nan | Mata Atlântica | 1.3 |
| 5b93fe79-5a78-325c-8fb5-53a98fc5b3eb | -9.94479 | -36.30693 | 2024-12-11 03:40:00 | NOAA-20 | TEOTÔNIO VILELA | ALAGOAS | Brasil | 2709152 | 27 | 33 | nan | nan | nan | Mata Atlântica | 4.3 |
| 54dbc4d5-b813-31a8-b210-35111fe518f0 | -6.97473 | -42.99448 | 2024-12-11 03:40:00 | NOAA-20 | FLORIANO | PIAUÍ | Brasil | 2203909 | 22 | 33 | nan | nan | nan | Caatinga | 23.2 |
| e71a12a5-56dc-3cd6-9894-00ccbcb68e5f | -6.11959 | -42.53846 | 2024-12-11 03:40:00 | NOAA-20 | JARDIM DO MULATO | PIAUÍ | Brasil | 2205250 | 22 | 33 | nan | nan | nan | Caatinga | 2.0 |
| a1851173-4385-3d96-92a9-b9d7022c0d46 | -6.1217 | -42.52419 | 2024-12-11 03:40:00 | NOAA-20 | JARDIM DO MULATO | PIAUÍ | Brasil | 2205250 | 22 | 33 | nan | nan | nan | Caatinga | 6.5 |
| a5c72a6c-f7a5-3bae-9649-83675382e006 | -6.82841 | -44.38967 | 2024-12-11 03:40:00 | NOAA-20 | PASTOS BONS | MARANHÃO | Brasil | 2108009 | 21 | 33 | nan | nan | nan | Cerrado | 1.1 |
| 4b5e5cad-90c7-31ed-8369-f144f6cffeda | -9.59503 | -36.4124 | 2024-12-11 03:40:00 | NOAA-20 | TANQUE D'ARCA | ALAGOAS | Brasil | 2709004 | 27 | 33 | nan | nan | nan | Mata Atlântica | 6.5 |


[Clique aqui para ver as próximas entradas](README13.md)
