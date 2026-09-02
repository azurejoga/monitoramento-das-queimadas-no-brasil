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

## Dados Diários - Página 59

| ID | Latitude | Longitude | Data/Hora GMT | Satélite | Município | Estado | País | Município ID | Estado ID | País ID | Dias sem Chuva | Precipitação | Risco de Fogo | Bioma | FRP |
|----|----------|-----------|---------------|----------|-----------|--------|------|--------------|-----------|---------|----------------|--------------|----------------|-------|-----|
| d70d3efe-79c6-3a2f-b554-d6319347d4f6 | -9.82685 | -59.47576 | 2026-09-02 05:18:00 | NOAA-20 | ARIPUANÃ | MATO GROSSO | Brasil | 5101407 | 51 | 33 | nan | nan | nan | Amazônia | 0.4 |
| 8671f4cd-2ddc-3651-b766-717f07fc5802 | -8.76925 | -62.83958 | 2026-09-02 05:18:00 | NOAA-20 | CANDEIAS DO JAMARI | RONDÔNIA | Brasil | 1100809 | 11 | 33 | nan | nan | nan | Amazônia | 1.1 |
| 5216baf1-c0bc-3f74-87ae-8f4f1d000bc1 | -9.82593 | -63.01355 | 2026-09-02 05:18:00 | NOAA-20 | ARIQUEMES | RONDÔNIA | Brasil | 1100023 | 11 | 33 | nan | nan | nan | Amazônia | 2.2 |
| fad444ca-d9cf-30db-9c05-107cd712f616 | -11.67361 | -50.1967 | 2026-09-02 05:18:00 | NOAA-20 | FORMOSO DO ARAGUAIA | TOCANTINS | Brasil | 1708205 | 17 | 33 | nan | nan | nan | Cerrado | 1.8 |
| bfc980cb-c7f4-32e1-be92-fcabf73edf54 | -9.01564 | -65.45142 | 2026-09-02 05:18:00 | NOAA-20 | LÁBREA | AMAZONAS | Brasil | 1302405 | 13 | 33 | nan | nan | nan | Amazônia | 3.5 |
| 918f510e-543d-3a0e-8bca-38a2b32af0b2 | -9.44528 | -61.03106 | 2026-09-02 05:18:00 | NOAA-20 | COLNIZA | MATO GROSSO | Brasil | 5103254 | 51 | 33 | nan | nan | nan | Amazônia | 0.9 |
| 08854e4d-d237-3a5d-9871-2ebc7a5df5f8 | -11.29319 | -45.16883 | 2026-09-02 05:18:00 | NOAA-20 | FORMOSA DO RIO PRETO | BAHIA | Brasil | 2911105 | 29 | 33 | nan | nan | nan | Cerrado | 3.3 |
| f2511c04-a07a-3e28-8026-bf30740918db | -9.92635 | -67.84333 | 2026-09-02 05:18:00 | NOAA-20 | RIO BRANCO | ACRE | Brasil | 1200401 | 12 | 33 | nan | nan | nan | Amazônia | 0.6 |
| b83b014b-c390-3ad5-94cf-e409225ee94b | -12.36982 | -53.19369 | 2026-09-02 05:18:00 | NOAA-20 | GAÚCHA DO NORTE | MATO GROSSO | Brasil | 5103858 | 51 | 33 | nan | nan | nan | Amazônia | 1.0 |
| 48861518-dded-35c6-aac9-c6d8a8da7fcc | -9.44109 | -67.42494 | 2026-09-02 05:18:00 | NOAA-20 | BOCA DO ACRE | AMAZONAS | Brasil | 1300706 | 13 | 33 | nan | nan | nan | Amazônia | 2.0 |
| db1b9f94-ab00-35da-95e3-80f596ec47f8 | -13.55839 | -59.74638 | 2026-09-02 05:18:00 | NOAA-20 | COMODORO | MATO GROSSO | Brasil | 5103304 | 51 | 33 | nan | nan | nan | Amazônia | 1.1 |
| f433474c-84ff-3d6d-9b9c-0ae0cb374640 | -10.88724 | -45.34414 | 2026-09-02 05:18:00 | NOAA-20 | FORMOSA DO RIO PRETO | BAHIA | Brasil | 2911105 | 29 | 33 | nan | nan | nan | Cerrado | 1.7 |
| b9d93e59-95c1-3e95-b936-471d001c1758 | -12.07209 | -47.1319 | 2026-09-02 05:18:00 | NOAA-20 | CONCEIÇÃO DO TOCANTINS | TOCANTINS | Brasil | 1705607 | 17 | 33 | nan | nan | nan | Cerrado | 1.9 |
| 53fa7a65-140d-3e1f-9aa8-0333a67339db | -9.44269 | -67.44602 | 2026-09-02 05:18:00 | NOAA-20 | BOCA DO ACRE | AMAZONAS | Brasil | 1300706 | 13 | 33 | nan | nan | nan | Amazônia | 1.3 |
| a7cb4015-686c-37da-8b4d-58537ceaca9a | -8.91508 | -63.28906 | 2026-09-02 05:18:00 | NOAA-20 | ITAPUÃ DO OESTE | RONDÔNIA | Brasil | 1101104 | 11 | 33 | nan | nan | nan | Amazônia | 15.3 |
| fa380ac2-3374-3eda-8d46-f9c6da3a2b8c | -12.0795 | -47.12284 | 2026-09-02 05:18:00 | NOAA-20 | CONCEIÇÃO DO TOCANTINS | TOCANTINS | Brasil | 1705607 | 17 | 33 | nan | nan | nan | Cerrado | 2.7 |
| 4a048498-c829-3ff9-a4ee-9af16395dfc9 | -7.69574 | -67.12759 | 2026-09-02 05:18:00 | NOAA-20 | PAUINI | AMAZONAS | Brasil | 1303502 | 13 | 33 | nan | nan | nan | Amazônia | 1.5 |
| a9bc0f2f-1211-37d0-87e4-2078ba0ce6d1 | -14.96454 | -48.10979 | 2026-09-02 05:18:00 | NOAA-20 | MIMOSO DE GOIÁS | GOIÁS | Brasil | 5213053 | 52 | 33 | nan | nan | nan | Cerrado | 6.1 |
| 666f171d-e17b-3767-be6f-7b36bca22451 | -7.94295 | -63.45201 | 2026-09-02 05:18:00 | NOAA-20 | HUMAITÁ | AMAZONAS | Brasil | 1301704 | 13 | 33 | nan | nan | nan | Amazônia | 0.7 |
| c807a4fa-1e80-3a13-80f0-332b4fc1e421 | -11.04193 | -57.21812 | 2026-09-02 05:18:00 | NOAA-20 | JUARA | MATO GROSSO | Brasil | 5105101 | 51 | 33 | nan | nan | nan | Amazônia | 1.3 |
| 532b6163-97dc-3385-a9e8-a71b414560fb | -12.14919 | -47.12603 | 2026-09-02 05:18:00 | NOAA-20 | CONCEIÇÃO DO TOCANTINS | TOCANTINS | Brasil | 1705607 | 17 | 33 | nan | nan | nan | Cerrado | 4.4 |
| eabc12aa-73cd-378b-988d-9226a9862d5f | -7.76059 | -61.19483 | 2026-09-02 05:18:00 | NOAA-20 | NOVO ARIPUANÃ | AMAZONAS | Brasil | 1303304 | 13 | 33 | nan | nan | nan | Amazônia | 1.9 |
| 1974f616-52ad-3ceb-b9fb-0fc69175b47f | -12.15305 | -47.12674 | 2026-09-02 05:18:00 | NOAA-20 | CONCEIÇÃO DO TOCANTINS | TOCANTINS | Brasil | 1705607 | 17 | 33 | nan | nan | nan | Cerrado | 3.6 |
| 3ff5ed48-4a54-3cca-90fb-27c0f2954425 | -11.67399 | -50.19365 | 2026-09-02 05:18:00 | NOAA-20 | FORMOSO DO ARAGUAIA | TOCANTINS | Brasil | 1708205 | 17 | 33 | nan | nan | nan | Cerrado | 1.8 |
| 2ca01e91-0a27-3d9a-81e3-c5f65c4f3e19 | -12.12738 | -47.14862 | 2026-09-02 05:18:00 | NOAA-20 | CONCEIÇÃO DO TOCANTINS | TOCANTINS | Brasil | 1705607 | 17 | 33 | nan | nan | nan | Cerrado | 8.8 |
| 28e6446a-98f7-3659-955b-6486588834c9 | -12.14411 | -47.11525 | 2026-09-02 05:18:00 | NOAA-20 | CONCEIÇÃO DO TOCANTINS | TOCANTINS | Brasil | 1705607 | 17 | 33 | nan | nan | nan | Cerrado | 2.7 |
| ed5eb81d-a327-376c-aefa-170c342ba682 | -11.82713 | -46.06087 | 2026-09-02 05:18:00 | NOAA-20 | BARREIRAS | BAHIA | Brasil | 2903201 | 29 | 33 | nan | nan | nan | Cerrado | 2.3 |
| 846960dc-cf86-3b5a-a58d-ddf36f10378b | -10.51577 | -57.44287 | 2026-09-02 05:18:00 | NOAA-20 | JUARA | MATO GROSSO | Brasil | 5105101 | 51 | 33 | nan | nan | nan | Amazônia | 1.1 |
| e9a51e09-b155-3918-8939-052959787ff9 | -10.49599 | -59.60654 | 2026-09-02 05:18:00 | NOAA-20 | ARIPUANÃ | MATO GROSSO | Brasil | 5101407 | 51 | 33 | nan | nan | nan | Amazônia | 2.8 |
| 79eecafb-043d-37e5-b94a-6df8a0624590 | -10.40722 | -50.00389 | 2026-09-02 05:18:00 | NOAA-20 | PIUM | TOCANTINS | Brasil | 1717503 | 17 | 33 | nan | nan | nan | Cerrado | 2.0 |
| 1145f613-7900-3a15-8488-df9c8fd69019 | -8.74979 | -62.57423 | 2026-09-02 05:18:00 | NOAA-20 | CUJUBIM | RONDÔNIA | Brasil | 1100940 | 11 | 33 | nan | nan | nan | Amazônia | 11.0 |
| a7d6eba6-8d32-3aa0-83ae-8396d1176cb0 | -12.13535 | -47.11426 | 2026-09-02 05:18:00 | NOAA-20 | CONCEIÇÃO DO TOCANTINS | TOCANTINS | Brasil | 1705607 | 17 | 33 | nan | nan | nan | Cerrado | 1.8 |
| 2d9a8618-aa9f-3e0a-a9d5-4bc0cc910738 | -10.44117 | -46.72983 | 2026-09-02 05:18:00 | NOAA-20 | MATEIROS | TOCANTINS | Brasil | 1712702 | 17 | 33 | nan | nan | nan | Cerrado | 21.9 |
| 43889834-2f93-378f-91cf-7f04b693b586 | -10.39977 | -50.00664 | 2026-09-02 05:18:00 | NOAA-20 | PIUM | TOCANTINS | Brasil | 1717503 | 17 | 33 | nan | nan | nan | Cerrado | 0.5 |
| b49585b4-e0c5-3760-bc95-1958a13980b1 | -9.18343 | -59.54782 | 2026-09-02 05:18:00 | NOAA-20 | COLNIZA | MATO GROSSO | Brasil | 5103254 | 51 | 33 | nan | nan | nan | Amazônia | 3.2 |
| eb301946-a132-3337-acf1-6540d2a95a78 | -8.69177 | -62.93667 | 2026-09-02 05:18:00 | NOAA-20 | CANDEIAS DO JAMARI | RONDÔNIA | Brasil | 1100809 | 11 | 33 | nan | nan | nan | Amazônia | 2.2 |
| 78912408-b264-37f9-89a9-f654aeaf2083 | -7.72925 | -60.97506 | 2026-09-02 05:18:00 | NOAA-20 | NOVO ARIPUANÃ | AMAZONAS | Brasil | 1303304 | 13 | 33 | nan | nan | nan | Amazônia | 2.2 |
| 01442055-8f7e-3dc2-9cfa-79a158ce76d5 | -11.03533 | -49.66928 | 2026-09-02 05:18:00 | NOAA-20 | SANTA RITA DO TOCANTINS | TOCANTINS | Brasil | 1718899 | 17 | 33 | nan | nan | nan | Cerrado | 1.4 |
| 9f1b8112-fc3b-357f-926e-8c8b242e3684 | -11.65865 | -50.19157 | 2026-09-02 05:18:00 | NOAA-20 | FORMOSO DO ARAGUAIA | TOCANTINS | Brasil | 1708205 | 17 | 33 | nan | nan | nan | Cerrado | 1.1 |
| aa60ea91-5ed2-375e-b8cb-b4e515134667 | -12.14172 | -47.13518 | 2026-09-02 05:18:00 | NOAA-20 | CONCEIÇÃO DO TOCANTINS | TOCANTINS | Brasil | 1705607 | 17 | 33 | nan | nan | nan | Cerrado | 6.5 |
| 8e169cc0-8fc7-3d3f-8f3e-7d7ee850cc35 | -10.86277 | -45.37361 | 2026-09-02 05:18:00 | NOAA-20 | FORMOSA DO RIO PRETO | BAHIA | Brasil | 2911105 | 29 | 33 | nan | nan | nan | Cerrado | 1.3 |
| 32f413b5-9929-326e-88b6-b10f61a8908a | -10.05941 | -59.40351 | 2026-09-02 05:18:00 | NOAA-20 | ARIPUANÃ | MATO GROSSO | Brasil | 5101407 | 51 | 33 | nan | nan | nan | Amazônia | 0.8 |
| 02d82431-f0b1-30fd-9ace-528b4d01ae0c | -15.34915 | -47.04216 | 2026-09-02 05:18:00 | NOAA-20 | FORMOSA | GOIÁS | Brasil | 5208004 | 52 | 33 | nan | nan | nan | Cerrado | 4.2 |
| e8ca6021-df2c-3930-a899-c0ebd47e04bb | -7.66797 | -62.54573 | 2026-09-02 05:18:00 | NOAA-20 | HUMAITÁ | AMAZONAS | Brasil | 1301704 | 13 | 33 | nan | nan | nan | Amazônia | 1.9 |
| c7c53da9-2759-3aef-9a42-d90886424217 | -9.00269 | -67.80202 | 2026-09-02 05:18:00 | NOAA-20 | BOCA DO ACRE | AMAZONAS | Brasil | 1300706 | 13 | 33 | nan | nan | nan | Amazônia | 1.4 |
| 50200148-1c62-3603-9829-ac6ea8fa7b2e | -10.3215 | -49.9463 | 2026-09-02 05:18:00 | NOAA-20 | PIUM | TOCANTINS | Brasil | 1717503 | 17 | 33 | nan | nan | nan | Cerrado | 2.0 |
| bd7d60b4-38d9-3194-874a-894e08432af9 | -9.10287 | -63.97557 | 2026-09-02 05:18:00 | NOAA-20 | PORTO VELHO | RONDÔNIA | Brasil | 1100205 | 11 | 33 | nan | nan | nan | Amazônia | 1.2 |
| 9bb5e38e-66d9-3861-b0bd-58cbe3c6757e | -12.87069 | -45.82909 | 2026-09-02 05:18:00 | NOAA-20 | SÃO DESIDÉRIO | BAHIA | Brasil | 2928901 | 29 | 33 | nan | nan | nan | Cerrado | 4.9 |
| d705dc4a-cddb-3b1c-a821-6b200307fedf | -12.13724 | -47.11944 | 2026-09-02 05:18:00 | NOAA-20 | CONCEIÇÃO DO TOCANTINS | TOCANTINS | Brasil | 1705607 | 17 | 33 | nan | nan | nan | Cerrado | 2.0 |
| 922e0169-fcc0-33f5-b76a-1c5f7c552691 | -12.12494 | -47.06186 | 2026-09-02 05:18:00 | NOAA-20 | TAIPAS DO TOCANTINS | TOCANTINS | Brasil | 1720937 | 17 | 33 | nan | nan | nan | Cerrado | 4.6 |
| 0e388e58-2071-3ea5-bfe4-43363f487299 | -7.68203 | -67.12521 | 2026-09-02 05:18:00 | NOAA-20 | PAUINI | AMAZONAS | Brasil | 1303502 | 13 | 33 | nan | nan | nan | Amazônia | 0.9 |
| 5532b170-8382-392d-bb63-e13e3f64aca7 | -11.00083 | -45.08395 | 2026-09-02 05:18:00 | NOAA-20 | FORMOSA DO RIO PRETO | BAHIA | Brasil | 2911105 | 29 | 33 | nan | nan | nan | Cerrado | 6.7 |
| 2d394b96-e593-3e43-a43c-6b0f02fab378 | -8.69574 | -62.93736 | 2026-09-02 05:18:00 | NOAA-20 | CANDEIAS DO JAMARI | RONDÔNIA | Brasil | 1100809 | 11 | 33 | nan | nan | nan | Amazônia | 1.3 |
| 1e0eaab6-d284-3862-82ec-6d8f4592d764 | -8.90607 | -62.36499 | 2026-09-02 05:18:00 | NOAA-20 | CUJUBIM | RONDÔNIA | Brasil | 1100940 | 11 | 33 | nan | nan | nan | Amazônia | 7.9 |
| 02daca93-09b6-3c62-9465-0891a29c02a5 | -12.14352 | -47.12023 | 2026-09-02 05:18:00 | NOAA-20 | CONCEIÇÃO DO TOCANTINS | TOCANTINS | Brasil | 1705607 | 17 | 33 | nan | nan | nan | Cerrado | 2.7 |
| 26e8d4f6-b115-35f2-b9f4-f25725344424 | -9.22749 | -59.79706 | 2026-09-02 05:18:00 | NOAA-20 | COLNIZA | MATO GROSSO | Brasil | 5103254 | 51 | 33 | nan | nan | nan | Amazônia | 0.8 |
| 0af13121-dd8c-3db6-8bf3-122a04ade3b7 | -12.13825 | -47.14505 | 2026-09-02 05:18:00 | NOAA-20 | CONCEIÇÃO DO TOCANTINS | TOCANTINS | Brasil | 1705607 | 17 | 33 | nan | nan | nan | Cerrado | 10.6 |
| 041bd6b6-da85-3e1c-8fcd-355ffbd738c6 | -10.74287 | -54.03757 | 2026-09-02 05:18:00 | NOAA-20 | MARCELÂNDIA | MATO GROSSO | Brasil | 5105580 | 51 | 33 | nan | nan | nan | Amazônia | 3.5 |
| 07c82e77-f6ae-3137-a048-f6b432d0951f | -11.29235 | -45.16644 | 2026-09-02 05:18:00 | NOAA-20 | FORMOSA DO RIO PRETO | BAHIA | Brasil | 2911105 | 29 | 33 | nan | nan | nan | Cerrado | 4.8 |
| b214fc31-a0fd-3031-91c5-94be18a9b1e4 | -8.21606 | -61.47657 | 2026-09-02 05:18:00 | NOAA-20 | MANICORÉ | AMAZONAS | Brasil | 1302702 | 13 | 33 | nan | nan | nan | Amazônia | 1.0 |
| ae5b2cff-96ba-3f20-82d2-38b161d1ddf2 | -9.02935 | -65.4285 | 2026-09-02 05:18:00 | NOAA-20 | LÁBREA | AMAZONAS | Brasil | 1302405 | 13 | 33 | nan | nan | nan | Amazônia | 3.1 |
| 20bd64e3-2690-3b5e-91c0-b6b6926b16b0 | -8.9161 | -63.28579 | 2026-09-02 05:18:00 | NOAA-20 | ITAPUÃ DO OESTE | RONDÔNIA | Brasil | 1101104 | 11 | 33 | nan | nan | nan | Amazônia | 16.2 |
| c85b937d-38ea-3681-82e8-5453962010c9 | -11.66119 | -50.19123 | 2026-09-02 05:18:00 | NOAA-20 | FORMOSO DO ARAGUAIA | TOCANTINS | Brasil | 1708205 | 17 | 33 | nan | nan | nan | Cerrado | 1.5 |
| 08dac6db-9ef6-3a53-bfc7-50b46eba75e7 | -11.6663 | -50.19191 | 2026-09-02 05:18:00 | NOAA-20 | FORMOSO DO ARAGUAIA | TOCANTINS | Brasil | 1708205 | 17 | 33 | nan | nan | nan | Cerrado | 1.5 |
| 8d32a425-8ec7-3c15-9637-1f4ed89fe536 | -8.77319 | -62.84027 | 2026-09-02 05:18:00 | NOAA-20 | CANDEIAS DO JAMARI | RONDÔNIA | Brasil | 1100809 | 11 | 33 | nan | nan | nan | Amazônia | 1.1 |
| dc9d4cb0-ccae-3c7b-948a-f33e9ae49958 | -12.13545 | -47.1344 | 2026-09-02 05:18:00 | NOAA-20 | CONCEIÇÃO DO TOCANTINS | TOCANTINS | Brasil | 1705607 | 17 | 33 | nan | nan | nan | Cerrado | 3.4 |
| f492b662-40aa-3521-a0a6-9f086d20a6fe | -9.92615 | -60.48375 | 2026-09-02 05:18:00 | NOAA-20 | ARIPUANÃ | MATO GROSSO | Brasil | 5101407 | 51 | 33 | nan | nan | nan | Amazônia | 0.8 |
| ed190e4e-447d-30dd-bfb1-d82bdd1463bf | -11.65941 | -50.18546 | 2026-09-02 05:18:00 | NOAA-20 | FORMOSO DO ARAGUAIA | TOCANTINS | Brasil | 1708205 | 17 | 33 | nan | nan | nan | Cerrado | 1.0 |
| 1a62eaaa-177b-3c69-9d23-befd47e820f3 | -10.32032 | -49.95542 | 2026-09-02 05:18:00 | NOAA-20 | PIUM | TOCANTINS | Brasil | 1717503 | 17 | 33 | nan | nan | nan | Cerrado | 0.7 |
| 0b063d99-0c2b-3851-9491-5d847df65f77 | -9.08987 | -65.3841 | 2026-09-02 05:18:00 | NOAA-20 | LÁBREA | AMAZONAS | Brasil | 1302405 | 13 | 33 | nan | nan | nan | Amazônia | 1.6 |
| d60147a1-a895-3094-9f52-24b32eacb364 | -7.68631 | -67.11897 | 2026-09-02 05:18:00 | NOAA-20 | PAUINI | AMAZONAS | Brasil | 1303502 | 13 | 33 | nan | nan | nan | Amazônia | 1.9 |
| 85eb4cc3-b280-3728-b1ef-ccb688aece23 | -12.13365 | -47.1494 | 2026-09-02 05:18:00 | NOAA-20 | CONCEIÇÃO DO TOCANTINS | TOCANTINS | Brasil | 1705607 | 17 | 33 | nan | nan | nan | Cerrado | 8.8 |
| 0d31d010-d0a5-346b-83c5-31d80173d05a | -8.4671 | -54.7035 | 2026-09-02 05:20:00 | GOES-19 | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 146.3 |
| 329d8fe2-0573-36e5-9ad8-6fc898b89ffe | -8.4856 | -54.7225 | 2026-09-02 05:20:00 | GOES-19 | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 116.2 |
| 508b0996-bf81-31a1-92e4-9b1685d1f169 | -10.9204 | -45.3253 | 2026-09-02 05:20:00 | GOES-19 | FORMOSA DO RIO PRETO | BAHIA | Brasil | 2911105 | 29 | 33 | nan | nan | nan | Cerrado | 156.3 |
| c40c731d-56c1-3e81-9da8-2c8315b197f1 | -12.6483 | -45.0718 | 2026-09-02 05:20:00 | GOES-19 | SÃO DESIDÉRIO | BAHIA | Brasil | 2928901 | 29 | 33 | nan | nan | nan | Cerrado | 105.0 |
| bb860c8a-ad03-38a4-96b6-704597939c87 | -10.442 | -46.7235 | 2026-09-02 05:20:00 | GOES-19 | MATEIROS | TOCANTINS | Brasil | 1712702 | 17 | 33 | nan | nan | nan | Cerrado | 88.4 |
| 251b9db5-8a3c-3df6-9854-734a08dbd91f | -10.9013 | -45.3279 | 2026-09-02 05:20:00 | GOES-19 | FORMOSA DO RIO PRETO | BAHIA | Brasil | 2911105 | 29 | 33 | nan | nan | nan | Cerrado | 166.3 |
| 8edcf816-215b-39e4-babc-2a69d056eda5 | -10.92 | -45.3483 | 2026-09-02 05:20:00 | GOES-19 | FORMOSA DO RIO PRETO | BAHIA | Brasil | 2911105 | 29 | 33 | nan | nan | nan | Cerrado | 55.4 |
| 9601e4c5-815b-3c79-b11e-e31833013351 | -8.4485 | -54.7048 | 2026-09-02 05:20:00 | GOES-19 | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 90.9 |
| 9d570764-38cf-3b91-b4a0-1388ac2dc6be | -12.629 | -45.0749 | 2026-09-02 05:20:00 | GOES-19 | SÃO DESIDÉRIO | BAHIA | Brasil | 2928901 | 29 | 33 | nan | nan | nan | Cerrado | 132.6 |
| 8b143b68-2572-320a-a286-55de6b9bf2df | -10.7774 | -44.7463 | 2026-09-02 05:20:00 | GOES-19 | SEBASTIÃO BARROS | PIAUÍ | Brasil | 2210623 | 22 | 33 | nan | nan | nan | Cerrado | 54.4 |
| c7150c32-2951-3c9a-a63d-8f09f8c4821e | -10.7965 | -44.7437 | 2026-09-02 05:20:00 | GOES-19 | SANTA RITA DE CÁSSIA | BAHIA | Brasil | 2928406 | 29 | 33 | nan | nan | nan | Cerrado | 51.7 |
| b3049180-1211-31ba-9f99-5254a63dab1a | -12.6488 | -45.0486 | 2026-09-02 05:20:00 | GOES-19 | SÃO DESIDÉRIO | BAHIA | Brasil | 2928901 | 29 | 33 | nan | nan | nan | Cerrado | 43.9 |
| 3f4386bc-6a29-32e1-9f36-71c59052ef72 | -8.4858 | -54.7023 | 2026-09-02 05:20:00 | GOES-19 | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 138.4 |
| fc73531b-792f-395a-9597-7dbdd7fa946e | -8.4483 | -54.725 | 2026-09-02 05:20:00 | GOES-19 | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 68.2 |
| 408cbf3d-f4b2-3367-848d-ccf6e6149d59 | -10.9009 | -45.3509 | 2026-09-02 05:20:00 | GOES-19 | FORMOSA DO RIO PRETO | BAHIA | Brasil | 2911105 | 29 | 33 | nan | nan | nan | Cerrado | 64.2 |
| a0190dff-4f6e-3ffc-87ef-ac9e5403a0db | -8.4669 | -54.7237 | 2026-09-02 05:20:00 | GOES-19 | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 160.8 |
| d35db632-f7fe-3532-83a0-f93693951902 | -16.19201 | -47.48679 | 2026-09-02 05:21:00 | NOAA-20 | CRISTALINA | GOIÁS | Brasil | 5206206 | 52 | 33 | nan | nan | nan | Cerrado | 4.0 |
| 1c1f2099-9fc7-399f-b7a7-114f2c0870ba | -14.50225 | -59.8354 | 2026-09-02 05:21:00 | NOAA-20 | NOVA LACERDA | MATO GROSSO | Brasil | 5106182 | 51 | 33 | nan | nan | nan | Amazônia | 1.5 |
| dbdcb0eb-80a5-3062-80c9-3e0987c56e0d | -16.18454 | -47.48802 | 2026-09-02 05:21:00 | NOAA-20 | CRISTALINA | GOIÁS | Brasil | 5206206 | 52 | 33 | nan | nan | nan | Cerrado | 3.7 |
| 3eca3d52-d2ce-34b4-af90-3898359633ed | -17.18952 | -54.2966 | 2026-09-02 05:21:00 | NOAA-20 | ITIQUIRA | MATO GROSSO | Brasil | 5104609 | 51 | 33 | nan | nan | nan | Cerrado | 0.8 |
| fe74d718-44e4-36dd-8455-811548e2de5c | -14.49721 | -59.84555 | 2026-09-02 05:21:00 | NOAA-20 | NOVA LACERDA | MATO GROSSO | Brasil | 5106182 | 51 | 33 | nan | nan | nan | Amazônia | 1.4 |
| 0a0810bf-b36e-320a-a1ed-931885920755 | -17.18477 | -54.30037 | 2026-09-02 05:21:00 | NOAA-20 | ITIQUIRA | MATO GROSSO | Brasil | 5104609 | 51 | 33 | nan | nan | nan | Cerrado | 0.8 |
| 98f44445-0455-35f0-a5c5-09e2b01011cd | -15.17425 | -59.77548 | 2026-09-02 05:21:00 | NOAA-20 | VILA BELA DA SANTÍSSIMA TRINDADE | MATO GROSSO | Brasil | 5105507 | 51 | 33 | nan | nan | nan | Amazônia | 0.9 |
| ac16119c-8fe0-3110-9c1d-0daac7d0b9c2 | -15.17699 | -59.77961 | 2026-09-02 05:21:00 | NOAA-20 | VILA BELA DA SANTÍSSIMA TRINDADE | MATO GROSSO | Brasil | 5105507 | 51 | 33 | nan | nan | nan | Amazônia | 1.0 |
| 92c2c864-4c41-34cb-ba65-9be4352ce916 | -14.50831 | -59.84006 | 2026-09-02 05:21:00 | NOAA-20 | NOVA LACERDA | MATO GROSSO | Brasil | 5106182 | 51 | 33 | nan | nan | nan | Amazônia | 0.9 |
| 2d55c18e-b03d-340a-be68-c03439785ee3 | -14.49778 | -59.84199 | 2026-09-02 05:21:00 | NOAA-20 | NOVA LACERDA | MATO GROSSO | Brasil | 5106182 | 51 | 33 | nan | nan | nan | Amazônia | 2.9 |
| b97c5903-ab40-3849-90da-5e937c591dad | -16.72966 | -47.08906 | 2026-09-02 05:21:00 | NOAA-20 | PARACATU | MINAS GERAIS | Brasil | 3147006 | 31 | 33 | nan | nan | nan | Cerrado | 4.6 |
| 1a8512c6-5d6e-3e1a-bc26-369619410498 | -16.19048 | -47.49358 | 2026-09-02 05:21:00 | NOAA-20 | CRISTALINA | GOIÁS | Brasil | 5206206 | 52 | 33 | nan | nan | nan | Cerrado | 3.4 |


[Clique aqui para ver as próximas entradas](README60.md)
