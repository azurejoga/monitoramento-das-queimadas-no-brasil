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

## Dados Diários - Página 14

| ID | Latitude | Longitude | Data/Hora GMT | Satélite | Município | Estado | País | Município ID | Estado ID | País ID | Dias sem Chuva | Precipitação | Risco de Fogo | Bioma | FRP |
|----|----------|-----------|---------------|----------|-----------|--------|------|--------------|-----------|---------|----------------|--------------|----------------|-------|-----|
| f14cccae-213c-3f83-b73d-7c38b4e93c9d | -14.79073 | -48.7728 | 2026-08-24 03:51:00 | NOAA-21 | BARRO ALTO | GOIÁS | Brasil | 5203203 | 52 | 33 | nan | nan | nan | Cerrado | 3.6 |
| 7901a26e-9cef-35f8-a60b-dae571a8d655 | -19.48287 | -44.33842 | 2026-08-24 03:51:00 | NOAA-21 | SETE LAGOAS | MINAS GERAIS | Brasil | 3167202 | 31 | 33 | nan | nan | nan | Cerrado | 1.0 |
| 3bdc6820-f25a-3a25-8304-0157dc0917d1 | -17.43838 | -48.8385 | 2026-08-24 03:51:00 | NOAA-21 | PIRACANJUBA | GOIÁS | Brasil | 5217104 | 52 | 33 | nan | nan | nan | Cerrado | 63.2 |
| 51d2929a-c69a-383c-ae49-6da0d5723381 | -14.7901 | -48.77588 | 2026-08-24 03:51:00 | NOAA-21 | BARRO ALTO | GOIÁS | Brasil | 5203203 | 52 | 33 | nan | nan | nan | Cerrado | 3.6 |
| 8abeee99-0a9a-3d8d-8d27-96a4a75b0987 | -17.42939 | -48.82919 | 2026-08-24 03:51:00 | NOAA-21 | PIRACANJUBA | GOIÁS | Brasil | 5217104 | 52 | 33 | nan | nan | nan | Cerrado | 2.5 |
| a7f877e5-85c0-311a-b024-c8f868e7520c | -11.84994 | -51.68521 | 2026-08-24 03:51:00 | NOAA-21 | ALTO BOA VISTA | MATO GROSSO | Brasil | 5100359 | 51 | 33 | nan | nan | nan | Cerrado | 4.3 |
| 01b90140-1c23-3497-b5d6-8d09921cfbfe | -12.61107 | -52.45995 | 2026-08-24 03:51:00 | NOAA-21 | QUERÊNCIA | MATO GROSSO | Brasil | 5107065 | 51 | 33 | nan | nan | nan | Amazônia | 3.6 |
| 618605a6-6fcd-3c35-8ed6-2fe59dd172bd | -20.65111 | -45.84551 | 2026-08-24 03:51:00 | NOAA-21 | PIMENTA | MINAS GERAIS | Brasil | 3150505 | 31 | 33 | nan | nan | nan | Cerrado | 0.8 |
| de287dc8-aeab-3d0d-8bd9-de2db3989a1d | -13.15808 | -51.39098 | 2026-08-24 03:51:00 | NOAA-21 | RIBEIRÃO CASCALHEIRA | MATO GROSSO | Brasil | 5107180 | 51 | 33 | nan | nan | nan | Cerrado | 2.9 |
| 33d12703-1693-37f9-99f6-f3d0713a2a94 | -13.1617 | -51.39618 | 2026-08-24 03:51:00 | NOAA-21 | RIBEIRÃO CASCALHEIRA | MATO GROSSO | Brasil | 5107180 | 51 | 33 | nan | nan | nan | Cerrado | 1.8 |
| f94264d8-2777-3e1d-8dfe-f1325838e806 | -17.70375 | -46.38794 | 2026-08-24 03:51:00 | NOAA-21 | LAGOA GRANDE | MINAS GERAIS | Brasil | 3137536 | 31 | 33 | nan | nan | nan | Cerrado | 6.4 |
| 47360120-ea10-3589-ba41-2fa3152b7cff | -19.01421 | -42.124 | 2026-08-24 03:51:00 | NOAA-21 | GOVERNADOR VALADARES | MINAS GERAIS | Brasil | 3127701 | 31 | 33 | nan | nan | nan | Mata Atlântica | 10.1 |
| 735b8905-2d18-324b-a068-b6c4a6254024 | -12.89017 | -48.48689 | 2026-08-24 03:51:00 | NOAA-21 | PALMEIRÓPOLIS | TOCANTINS | Brasil | 1715754 | 17 | 33 | nan | nan | nan | Cerrado | 2.4 |
| c0903fa7-0ca8-3bfb-9a5d-4f30e9cbd3d7 | -14.77906 | -48.77408 | 2026-08-24 03:51:00 | NOAA-21 | BARRO ALTO | GOIÁS | Brasil | 5203203 | 52 | 33 | nan | nan | nan | Cerrado | 3.3 |
| 11268c70-8377-3b03-b95e-e50823360be9 | -14.40312 | -51.78394 | 2026-08-24 03:51:00 | NOAA-21 | NOVA NAZARÉ | MATO GROSSO | Brasil | 5106174 | 51 | 33 | nan | nan | nan | Cerrado | 2.8 |
| 48b91a28-2b11-3eb7-ac66-5e9eeaaa774f | -13.18146 | -51.40038 | 2026-08-24 03:51:00 | NOAA-21 | RIBEIRÃO CASCALHEIRA | MATO GROSSO | Brasil | 5107180 | 51 | 33 | nan | nan | nan | Cerrado | 1.6 |
| 1e041355-e56a-3d9c-862b-9c4c58ce5bad | -12.09865 | -50.6179 | 2026-08-24 03:51:00 | NOAA-21 | FORMOSO DO ARAGUAIA | TOCANTINS | Brasil | 1708205 | 17 | 33 | nan | nan | nan | Cerrado | 3.8 |
| d5d7a905-dd03-3475-8560-0386c4871ddb | -15.02975 | -48.68773 | 2026-08-24 03:51:00 | NOAA-21 | VILA PROPÍCIO | GOIÁS | Brasil | 5222302 | 52 | 33 | nan | nan | nan | Cerrado | 3.5 |
| 5e94a59e-9468-3779-af76-2755d5b5f2de | -15.03047 | -48.68409 | 2026-08-24 03:51:00 | NOAA-21 | VILA PROPÍCIO | GOIÁS | Brasil | 5222302 | 52 | 33 | nan | nan | nan | Cerrado | 1.9 |
| 8c292ce0-317e-36f0-aead-1e3928154d62 | -15.35271 | -52.78159 | 2026-08-24 03:51:00 | NOAA-21 | BARRA DO GARÇAS | MATO GROSSO | Brasil | 5101803 | 51 | 33 | nan | nan | nan | Cerrado | 9.3 |
| fcb71451-b30d-3f97-9a51-60dcb5f172ad | -17.83287 | -44.4709 | 2026-08-24 03:51:00 | NOAA-21 | LASSANCE | MINAS GERAIS | Brasil | 3138104 | 31 | 33 | nan | nan | nan | Cerrado | 1.5 |
| 990e8376-6cf6-3657-a40f-406c4f72dad7 | -16.40918 | -49.91737 | 2026-08-24 03:51:00 | NOAA-21 | ANICUNS | GOIÁS | Brasil | 5201306 | 52 | 33 | nan | nan | nan | Cerrado | 2.6 |
| 640b9b98-969a-3351-af1f-a58206e3ffc8 | -12.86751 | -48.48453 | 2026-08-24 03:51:00 | NOAA-21 | PALMEIRÓPOLIS | TOCANTINS | Brasil | 1715754 | 17 | 33 | nan | nan | nan | Cerrado | 2.9 |
| 4955bad9-ffb3-351a-b04d-0423bb7e337f | -15.26449 | -52.82207 | 2026-08-24 03:51:00 | NOAA-21 | BARRA DO GARÇAS | MATO GROSSO | Brasil | 5101803 | 51 | 33 | nan | nan | nan | Cerrado | 12.4 |
| 3c7b1ca7-b2bd-30ec-9a05-dbf2a8221c71 | -12.89496 | -48.49202 | 2026-08-24 03:51:00 | NOAA-21 | PALMEIRÓPOLIS | TOCANTINS | Brasil | 1715754 | 17 | 33 | nan | nan | nan | Cerrado | 2.4 |
| 299aaed1-a27a-39fc-853d-2da2796ab536 | -16.39244 | -51.82639 | 2026-08-24 03:51:00 | NOAA-21 | PIRANHAS | GOIÁS | Brasil | 5217203 | 52 | 33 | nan | nan | nan | Cerrado | 3.4 |
| 78b9e1b8-83b9-3dc1-97c6-2d6d8fb768ab | -13.44944 | -43.84615 | 2026-08-24 03:51:00 | NOAA-21 | SERRA DO RAMALHO | BAHIA | Brasil | 2930154 | 29 | 33 | nan | nan | nan | Cerrado | 1.7 |
| 013d7d08-09a6-3425-8ed8-74f8d2c6168e | -14.78394 | -48.77808 | 2026-08-24 03:51:00 | NOAA-21 | BARRO ALTO | GOIÁS | Brasil | 5203203 | 52 | 33 | nan | nan | nan | Cerrado | 3.6 |
| f427ac12-02e8-3700-bf3a-f0de9addee7f | -16.41026 | -51.84142 | 2026-08-24 03:51:00 | NOAA-21 | PIRANHAS | GOIÁS | Brasil | 5217203 | 52 | 33 | nan | nan | nan | Cerrado | 3.0 |
| 69645022-aa36-3c3a-b3d0-a20629c53e21 | -13.17488 | -51.39898 | 2026-08-24 03:51:00 | NOAA-21 | RIBEIRÃO CASCALHEIRA | MATO GROSSO | Brasil | 5107180 | 51 | 33 | nan | nan | nan | Cerrado | 2.4 |
| 99f36edf-bcc1-3aa6-88eb-b7d40fe30a6f | -12.71794 | -48.40103 | 2026-08-24 03:51:00 | NOAA-21 | SÃO SALVADOR DO TOCANTINS | TOCANTINS | Brasil | 1720259 | 17 | 33 | nan | nan | nan | Cerrado | 4.0 |
| 02e5a4f0-c7e1-35ed-9ddf-b75d01b37345 | -13.68936 | -51.83862 | 2026-08-24 03:51:00 | NOAA-21 | CANARANA | MATO GROSSO | Brasil | 5102702 | 51 | 33 | nan | nan | nan | Cerrado | 3.0 |
| 1e97343a-212a-3f86-9cb6-33519bde320a | -13.27394 | -51.43994 | 2026-08-24 03:51:00 | NOAA-21 | RIBEIRÃO CASCALHEIRA | MATO GROSSO | Brasil | 5107180 | 51 | 33 | nan | nan | nan | Cerrado | 2.8 |
| 25f33015-37f6-3719-b91b-ec51e616b4b9 | -16.41073 | -51.83449 | 2026-08-24 03:51:00 | NOAA-21 | PIRANHAS | GOIÁS | Brasil | 5217203 | 52 | 33 | nan | nan | nan | Cerrado | 6.8 |
| e37c6b9c-609a-34e3-bcd2-aa8fd9e494a4 | -15.57987 | -47.51238 | 2026-08-24 03:51:00 | NOAA-21 | BRASÍLIA | DISTRITO FEDERAL | Brasil | 5300108 | 53 | 33 | nan | nan | nan | Cerrado | 6.1 |
| d4af03ac-9a19-3abd-929d-04e7ab0e4133 | -18.52354 | -47.16971 | 2026-08-24 03:51:00 | NOAA-21 | COROMANDEL | MINAS GERAIS | Brasil | 3119302 | 31 | 33 | nan | nan | nan | Cerrado | 1.6 |
| be8abe42-3eab-38c4-a648-af107dc9e550 | -13.27653 | -51.43923 | 2026-08-24 03:51:00 | NOAA-21 | RIBEIRÃO CASCALHEIRA | MATO GROSSO | Brasil | 5107180 | 51 | 33 | nan | nan | nan | Cerrado | 2.2 |
| 213630f3-4918-3054-8b21-eb4d2c2b15a7 | -16.4084 | -49.92118 | 2026-08-24 03:51:00 | NOAA-21 | ANICUNS | GOIÁS | Brasil | 5201306 | 52 | 33 | nan | nan | nan | Cerrado | 2.6 |
| 57f51fb2-8a62-3e12-a54a-4b51c2680ad6 | -14.7835 | -48.77829 | 2026-08-24 03:51:00 | NOAA-21 | BARRO ALTO | GOIÁS | Brasil | 5203203 | 52 | 33 | nan | nan | nan | Cerrado | 5.1 |
| e240b6fb-d3f3-3f73-ad7c-dfbdb24050f8 | -14.3188 | -51.75899 | 2026-08-24 03:51:00 | NOAA-21 | NOVA NAZARÉ | MATO GROSSO | Brasil | 5106174 | 51 | 33 | nan | nan | nan | Cerrado | 8.9 |
| be6f7ded-7e66-3fce-9d40-e1ccd9333b80 | -18.69601 | -47.47345 | 2026-08-24 03:51:00 | NOAA-21 | MONTE CARMELO | MINAS GERAIS | Brasil | 3143104 | 31 | 33 | nan | nan | nan | Cerrado | 15.6 |
| 40b17e5f-af12-32db-8226-8d69d493a2f2 | -16.41024 | -49.91867 | 2026-08-24 03:51:00 | NOAA-21 | ANICUNS | GOIÁS | Brasil | 5201306 | 52 | 33 | nan | nan | nan | Cerrado | 3.3 |
| 7ca35548-8e86-32d5-8ee8-eccdfeaac73b | -16.05099 | -50.44986 | 2026-08-24 03:51:00 | NOAA-21 | GOIÁS | GOIÁS | Brasil | 5208905 | 52 | 33 | nan | nan | nan | Cerrado | 3.6 |
| 74bd67d9-1ad9-33b3-8386-cac6b9effc21 | -19.93473 | -45.07024 | 2026-08-24 03:51:00 | NOAA-21 | PERDIGÃO | MINAS GERAIS | Brasil | 3149705 | 31 | 33 | nan | nan | nan | Cerrado | 1.5 |
| b1f6d25f-ebab-38f6-996e-fd6440747ce3 | -19.76585 | -44.2415 | 2026-08-24 03:51:00 | NOAA-21 | ESMERALDAS | MINAS GERAIS | Brasil | 3124104 | 31 | 33 | nan | nan | nan | Cerrado | 1.4 |
| 803da8dc-47f5-38e6-831a-6b3c12974956 | -14.93539 | -52.65362 | 2026-08-24 03:51:00 | NOAA-21 | BARRA DO GARÇAS | MATO GROSSO | Brasil | 5101803 | 51 | 33 | nan | nan | nan | Cerrado | 5.6 |
| 99f7874b-633b-3a26-a8b2-b9036ff2ff16 | -20.65036 | -45.84948 | 2026-08-24 03:51:00 | NOAA-21 | PIMENTA | MINAS GERAIS | Brasil | 3150505 | 31 | 33 | nan | nan | nan | Cerrado | 0.8 |
| 31084bc2-f576-3b61-a334-1ee774ea2b8c | -12.71631 | -48.40919 | 2026-08-24 03:51:00 | NOAA-21 | SÃO SALVADOR DO TOCANTINS | TOCANTINS | Brasil | 1720259 | 17 | 33 | nan | nan | nan | Cerrado | 2.9 |
| 8991a034-e94d-302d-817a-311ccb5915ad | -15.12161 | -42.92184 | 2026-08-24 03:51:00 | NOAA-21 | MONTE AZUL | MINAS GERAIS | Brasil | 3142908 | 31 | 33 | nan | nan | nan | Cerrado | 3.2 |
| 857a6bc2-d44c-3780-aec8-4473d3cd53cf | -12.89377 | -48.49104 | 2026-08-24 03:51:00 | NOAA-21 | PALMEIRÓPOLIS | TOCANTINS | Brasil | 1715754 | 17 | 33 | nan | nan | nan | Cerrado | 4.0 |
| 97a47fae-5355-3b93-9a42-85338a47ba4f | -19.28158 | -42.34973 | 2026-08-24 03:51:00 | NOAA-21 | BUGRE | MINAS GERAIS | Brasil | 3109253 | 31 | 33 | nan | nan | nan | Mata Atlântica | 1.9 |
| ad8ead4a-6005-3ece-9bcc-4010f08e2774 | -12.84876 | -48.49167 | 2026-08-24 03:51:00 | NOAA-21 | PALMEIRÓPOLIS | TOCANTINS | Brasil | 1715754 | 17 | 33 | nan | nan | nan | Cerrado | 1.9 |
| a9c0d402-ce47-398b-a4a8-4b7c2cf5ca6e | -13.27774 | -51.43339 | 2026-08-24 03:51:00 | NOAA-21 | RIBEIRÃO CASCALHEIRA | MATO GROSSO | Brasil | 5107180 | 51 | 33 | nan | nan | nan | Cerrado | 2.2 |
| fa606800-39a5-3ea8-b9ad-f362f96c58db | -14.93691 | -52.64669 | 2026-08-24 03:51:00 | NOAA-21 | BARRA DO GARÇAS | MATO GROSSO | Brasil | 5101803 | 51 | 33 | nan | nan | nan | Cerrado | 6.0 |
| 47bc78f1-a62b-3fbc-841a-31b45bd6d1d8 | -14.95154 | -52.67839 | 2026-08-24 03:51:00 | NOAA-21 | BARRA DO GARÇAS | MATO GROSSO | Brasil | 5101803 | 51 | 33 | nan | nan | nan | Cerrado | 3.2 |
| 8fd19ca3-84f7-3e35-ad4c-8e7ede7795ef | -15.26281 | -52.82952 | 2026-08-24 03:51:00 | NOAA-21 | BARRA DO GARÇAS | MATO GROSSO | Brasil | 5101803 | 51 | 33 | nan | nan | nan | Cerrado | 4.8 |
| c53ef046-2e90-39ee-a2e2-011026a715c3 | -15.98786 | -41.7746 | 2026-08-24 03:51:00 | NOAA-21 | SANTA CRUZ DE SALINAS | MINAS GERAIS | Brasil | 3157377 | 31 | 33 | nan | nan | nan | Mata Atlântica | 0.7 |
| cacf29b5-6728-313a-b7f3-fba5598482b5 | -14.39607 | -51.77367 | 2026-08-24 03:51:00 | NOAA-21 | NOVA NAZARÉ | MATO GROSSO | Brasil | 5106174 | 51 | 33 | nan | nan | nan | Cerrado | 1.9 |
| 63840d03-7411-3e38-b873-fe271319d4bd | -15.26112 | -52.83704 | 2026-08-24 03:51:00 | NOAA-21 | BARRA DO GARÇAS | MATO GROSSO | Brasil | 5101803 | 51 | 33 | nan | nan | nan | Cerrado | 4.8 |
| d176813a-d976-3a4f-8aa9-d835da5a3797 | -15.3697 | -45.59417 | 2026-08-24 03:51:00 | NOAA-21 | CHAPADA GAÚCHA | MINAS GERAIS | Brasil | 3116159 | 31 | 33 | nan | nan | nan | Cerrado | 2.2 |
| e07a1778-61df-30c1-b241-05f69bdcbdf2 | -12.11258 | -50.61514 | 2026-08-24 03:51:00 | NOAA-21 | FORMOSO DO ARAGUAIA | TOCANTINS | Brasil | 1708205 | 17 | 33 | nan | nan | nan | Cerrado | 58.1 |
| 24dccdcd-12c1-3277-84a6-2b8c71f2e678 | -17.41894 | -48.82695 | 2026-08-24 03:51:00 | NOAA-21 | PIRACANJUBA | GOIÁS | Brasil | 5217104 | 52 | 33 | nan | nan | nan | Cerrado | 5.7 |
| 8c23e8b3-3742-3f4e-a31c-9f77ea667638 | -17.67077 | -46.41481 | 2026-08-24 03:51:00 | NOAA-21 | LAGOA GRANDE | MINAS GERAIS | Brasil | 3137536 | 31 | 33 | nan | nan | nan | Cerrado | 2.7 |
| e16edb1d-5226-3160-9704-fd514a24df6f | -19.57293 | -42.70567 | 2026-08-24 03:51:00 | NOAA-21 | JAGUARAÇU | MINAS GERAIS | Brasil | 3135001 | 31 | 33 | nan | nan | nan | Mata Atlântica | 0.5 |
| 291c9ede-3412-329e-8688-7ab9f98c8fc6 | -17.43317 | -48.83728 | 2026-08-24 03:51:00 | NOAA-21 | PIRACANJUBA | GOIÁS | Brasil | 5217104 | 52 | 33 | nan | nan | nan | Cerrado | 63.2 |
| ff0ed9df-7974-3c1a-978f-c84845fe643a | -15.27155 | -52.85493 | 2026-08-24 03:51:00 | NOAA-21 | BARRA DO GARÇAS | MATO GROSSO | Brasil | 5101803 | 51 | 33 | nan | nan | nan | Cerrado | 3.2 |
| a99d1fc4-0075-37c1-a999-006a8c401c1c | -16.06809 | -50.44261 | 2026-08-24 03:51:00 | NOAA-21 | GOIÁS | GOIÁS | Brasil | 5208905 | 52 | 33 | nan | nan | nan | Cerrado | 2.3 |
| 50b65aa9-3613-3d15-b72e-fa76a6c2634c | -13.27518 | -51.43413 | 2026-08-24 03:51:00 | NOAA-21 | RIBEIRÃO CASCALHEIRA | MATO GROSSO | Brasil | 5107180 | 51 | 33 | nan | nan | nan | Cerrado | 2.7 |
| 55ee3a1a-bc83-31ea-b40d-15cfadab4125 | -16.41098 | -49.91516 | 2026-08-24 03:51:00 | NOAA-21 | ANICUNS | GOIÁS | Brasil | 5201306 | 52 | 33 | nan | nan | nan | Cerrado | 2.3 |
| 8b79e091-4a7b-395f-93eb-7b4ea90749b1 | -18.32228 | -47.20593 | 2026-08-24 03:51:00 | NOAA-21 | COROMANDEL | MINAS GERAIS | Brasil | 3119302 | 31 | 33 | nan | nan | nan | Cerrado | 4.6 |
| 4d73270b-c8dd-3bc2-977d-fbfeccc49d59 | -11.85677 | -51.68671 | 2026-08-24 03:51:00 | NOAA-21 | ALTO BOA VISTA | MATO GROSSO | Brasil | 5100359 | 51 | 33 | nan | nan | nan | Cerrado | 2.2 |
| 2d6e82c1-521f-3c88-a6dd-e1bc93c310b3 | -17.54385 | -42.53938 | 2026-08-24 03:51:00 | NOAA-21 | CAPELINHA | MINAS GERAIS | Brasil | 3112307 | 31 | 33 | nan | nan | nan | Cerrado | 10.2 |
| 5fabc31f-bcaf-34dc-bd58-b4eaeb82b8b3 | -16.4166 | -51.84301 | 2026-08-24 03:51:00 | NOAA-21 | PIRANHAS | GOIÁS | Brasil | 5217203 | 52 | 33 | nan | nan | nan | Cerrado | 3.0 |
| 22753128-08da-38e2-883b-2846cfc38fe4 | -16.41413 | -49.92227 | 2026-08-24 03:51:00 | NOAA-21 | ANICUNS | GOIÁS | Brasil | 5201306 | 52 | 33 | nan | nan | nan | Cerrado | 2.6 |
| ddf9fe56-5ed3-39d0-b286-f50bc4683a2a | -20.64705 | -45.84461 | 2026-08-24 03:51:00 | NOAA-21 | PIMENTA | MINAS GERAIS | Brasil | 3150505 | 31 | 33 | nan | nan | nan | Cerrado | 0.8 |
| 744ae895-0f85-332b-a199-5d820217651d | -14.79025 | -48.77297 | 2026-08-24 03:51:00 | NOAA-21 | BARRO ALTO | GOIÁS | Brasil | 5203203 | 52 | 33 | nan | nan | nan | Cerrado | 3.5 |
| a26c5037-b129-3e7c-a07c-a0a098307112 | -15.57943 | -47.51515 | 2026-08-24 03:51:00 | NOAA-21 | BRASÍLIA | DISTRITO FEDERAL | Brasil | 5300108 | 53 | 33 | nan | nan | nan | Cerrado | 7.9 |
| c4600b47-7f69-3de9-97b9-5fead1bdf3c1 | -15.57933 | -47.51516 | 2026-08-24 03:51:00 | NOAA-21 | BRASÍLIA | DISTRITO FEDERAL | Brasil | 5300108 | 53 | 33 | nan | nan | nan | Cerrado | 6.1 |
| 725170a8-f6f1-3915-813d-4aac70c84e62 | -15.03085 | -48.68948 | 2026-08-24 03:51:00 | NOAA-21 | VILA PROPÍCIO | GOIÁS | Brasil | 5222302 | 52 | 33 | nan | nan | nan | Cerrado | 2.7 |
| 3b2f77cc-9797-3931-a4f1-2568ec2eac10 | -17.42796 | -48.83611 | 2026-08-24 03:51:00 | NOAA-21 | PIRACANJUBA | GOIÁS | Brasil | 5217104 | 52 | 33 | nan | nan | nan | Cerrado | 24.1 |
| 8d76efe9-725b-3476-8f0c-fa72226cb7c5 | -12.09556 | -50.60031 | 2026-08-24 03:51:00 | NOAA-21 | FORMOSO DO ARAGUAIA | TOCANTINS | Brasil | 1708205 | 17 | 33 | nan | nan | nan | Cerrado | 3.1 |
| 84c03457-5b85-369b-8306-32c1e47e1938 | -12.86494 | -48.46811 | 2026-08-24 03:51:00 | NOAA-21 | PALMEIRÓPOLIS | TOCANTINS | Brasil | 1715754 | 17 | 33 | nan | nan | nan | Cerrado | 2.9 |
| 14f0fe4f-8d1e-3731-97ed-8ef71fe7f438 | -23.13285 | -47.39587 | 2026-08-24 03:53:00 | NOAA-21 | ELIAS FAUSTO | SÃO PAULO | Brasil | 3514908 | 35 | 33 | nan | nan | nan | Mata Atlântica | 1.2 |
| d8e9e989-d351-3d4b-bec2-91df65e929da | -23.26735 | -46.82372 | 2026-08-24 03:53:00 | NOAA-21 | JUNDIAÍ | SÃO PAULO | Brasil | 3525904 | 35 | 33 | nan | nan | nan | Mata Atlântica | 0.9 |
| 69c47171-94ca-3378-a7a5-07631ef2149e | -22.49771 | -48.59088 | 2026-08-24 03:53:00 | NOAA-21 | BARRA BONITA | SÃO PAULO | Brasil | 3505302 | 35 | 33 | nan | nan | nan | Mata Atlântica | 1.8 |
| ac3f3f74-36c3-37e3-ae40-c5efd6ddd455 | -23.00396 | -49.37724 | 2026-08-24 03:53:00 | NOAA-21 | ÓLEO | SÃO PAULO | Brasil | 3533809 | 35 | 33 | nan | nan | nan | Mata Atlântica | 4.3 |
| e65b8286-8b59-3d0c-b1f4-6b5632543b66 | -22.99794 | -49.38164 | 2026-08-24 03:53:00 | NOAA-21 | ÓLEO | SÃO PAULO | Brasil | 3533809 | 35 | 33 | nan | nan | nan | Mata Atlântica | 3.3 |
| dab0f945-4d92-32ae-8423-f3d0231c7c92 | -23.5223 | -47.37005 | 2026-08-24 03:53:00 | NOAA-21 | SOROCABA | SÃO PAULO | Brasil | 3552205 | 35 | 33 | nan | nan | nan | Mata Atlântica | 1.3 |
| 3527c0a9-41b2-3fee-9e7a-afdc870c1cf8 | -22.63962 | -47.81102 | 2026-08-24 03:53:00 | NOAA-21 | SÃO PEDRO | SÃO PAULO | Brasil | 3550407 | 35 | 33 | nan | nan | nan | Cerrado | 2.1 |
| a0712641-c6b0-3618-b3bf-f318cf157b4a | -23.19595 | -46.60851 | 2026-08-24 03:53:00 | NOAA-21 | ATIBAIA | SÃO PAULO | Brasil | 3504107 | 35 | 33 | nan | nan | nan | Mata Atlântica | 5.3 |
| d00fe1f4-223f-351e-ba80-2d4119ea9fbd | -23.3442 | -47.64502 | 2026-08-24 03:53:00 | NOAA-21 | BOITUVA | SÃO PAULO | Brasil | 3507001 | 35 | 33 | nan | nan | nan | Mata Atlântica | 0.6 |
| ad6c0191-1dc0-37be-b25e-a3b8545712ee | -23.33 | -46.43898 | 2026-08-24 03:53:00 | NOAA-21 | MAIRIPORÃ | SÃO PAULO | Brasil | 3528502 | 35 | 33 | nan | nan | nan | Mata Atlântica | 0.6 |
| 170f5e9e-8702-3458-8717-3eaa954e8341 | -23.17977 | -46.45543 | 2026-08-24 03:53:00 | NOAA-21 | BOM JESUS DOS PERDÕES | SÃO PAULO | Brasil | 3507100 | 35 | 33 | nan | nan | nan | Mata Atlântica | 1.1 |
| aeca8eb1-0970-316f-a40e-09b612850d22 | -23.82382 | -48.71832 | 2026-08-24 03:53:00 | NOAA-21 | BURI | SÃO PAULO | Brasil | 3508009 | 35 | 33 | nan | nan | nan | Cerrado | 1.8 |
| 4860dee5-0b84-3436-ba16-1990feaa4ecf | -22.95197 | -51.77837 | 2026-08-24 03:53:00 | NOAA-21 | NOSSA SENHORA DAS GRAÇAS | PARANÁ | Brasil | 4116406 | 41 | 33 | nan | nan | nan | Mata Atlântica | 15.0 |
| 71b5c985-64d7-3e66-8f4e-4ec86c799af2 | -23.42423 | -46.91113 | 2026-08-24 03:53:00 | NOAA-21 | SANTANA DE PARNAÍBA | SÃO PAULO | Brasil | 3547304 | 35 | 33 | nan | nan | nan | Mata Atlântica | 1.9 |
| a5422b4e-8bed-306e-9e9f-6cf5fb4c762e | -22.95102 | -51.78256 | 2026-08-24 03:53:00 | NOAA-21 | NOSSA SENHORA DAS GRAÇAS | PARANÁ | Brasil | 4116406 | 41 | 33 | nan | nan | nan | Mata Atlântica | 15.0 |
| 9e50702a-46bd-3856-83cf-62f079fe4ace | -22.95432 | -51.78043 | 2026-08-24 03:53:00 | NOAA-21 | NOSSA SENHORA DAS GRAÇAS | PARANÁ | Brasil | 4116406 | 41 | 33 | nan | nan | nan | Mata Atlântica | 13.2 |
| cbd744a2-91b3-3648-9e7c-5154f785bf52 | -23.00276 | -49.38291 | 2026-08-24 03:53:00 | NOAA-21 | ÓLEO | SÃO PAULO | Brasil | 3533809 | 35 | 33 | nan | nan | nan | Mata Atlântica | 3.3 |
| 0c8879ca-d282-33c0-a737-6e2d1ebcbf34 | -22.99916 | -49.37592 | 2026-08-24 03:53:00 | NOAA-21 | ÓLEO | SÃO PAULO | Brasil | 3533809 | 35 | 33 | nan | nan | nan | Mata Atlântica | 4.3 |


[Clique aqui para ver as próximas entradas](README15.md)
