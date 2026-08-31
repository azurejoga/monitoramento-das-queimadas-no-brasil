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

## Dados Diários - Página 110

| ID | Latitude | Longitude | Data/Hora GMT | Satélite | Município | Estado | País | Município ID | Estado ID | País ID | Dias sem Chuva | Precipitação | Risco de Fogo | Bioma | FRP |
|----|----------|-----------|---------------|----------|-----------|--------|------|--------------|-----------|---------|----------------|--------------|----------------|-------|-----|
| 247fa5d7-9032-3107-a752-d0b395db7a3f | -15.78549 | -47.7991 | 2026-08-31 16:28:00 | NPP-375 | BRASÍLIA | DISTRITO FEDERAL | Brasil | 5300108 | 53 | 33 | nan | nan | nan | Cerrado | 104.7 |
| 83f82a83-12ac-3e20-ae00-ec170fc6c1dd | -15.09008 | -48.36937 | 2026-08-31 16:28:00 | NPP-375 | MIMOSO DE GOIÁS | GOIÁS | Brasil | 5213053 | 52 | 33 | nan | nan | nan | Cerrado | 12.7 |
| 6ad7cd08-d193-3b5c-bb76-c4347b01f297 | -15.67145 | -45.92566 | 2026-08-31 16:28:00 | NPP-375 | ARINOS | MINAS GERAIS | Brasil | 3104502 | 31 | 33 | nan | nan | nan | Cerrado | 7.5 |
| f02f267f-9043-3e9f-aaff-78d40eab7f71 | -16.33821 | -39.5058 | 2026-08-31 16:28:00 | NPP-375 | EUNÁPOLIS | BAHIA | Brasil | 2910727 | 29 | 33 | nan | nan | nan | Mata Atlântica | 4.7 |
| 488905f8-4167-318a-a97e-acae9c66e948 | -17.87915 | -52.10112 | 2026-08-31 16:28:00 | NPP-375 | JATAÍ | GOIÁS | Brasil | 5211909 | 52 | 33 | nan | nan | nan | Cerrado | 279.8 |
| 2bfa0bb9-7936-3141-b1ac-1f3f8a1a86f9 | -16.08021 | -48.02566 | 2026-08-31 16:28:00 | NPP-375 | VALPARAÍSO DE GOIÁS | GOIÁS | Brasil | 5221858 | 52 | 33 | nan | nan | nan | Cerrado | 17.1 |
| dcdf4858-da33-3a5f-a4e8-6e003887cdb3 | -18.55136 | -39.78435 | 2026-08-31 16:28:00 | NPP-375 | CONCEIÇÃO DA BARRA | ESPÍRITO SANTO | Brasil | 3201605 | 32 | 33 | nan | nan | nan | Mata Atlântica | 6.5 |
| f680f63b-9935-368c-8d37-de7bfbb40f6d | -20.29812 | -47.83931 | 2026-08-31 16:28:00 | NPP-375 | ITUVERAVA | SÃO PAULO | Brasil | 3524105 | 35 | 33 | nan | nan | nan | Cerrado | 39.4 |
| 72ff875f-8bc4-3c19-9e7a-a14b26227fe5 | -19.85304 | -47.92582 | 2026-08-31 16:28:00 | NPP-375 | UBERABA | MINAS GERAIS | Brasil | 3170107 | 31 | 33 | nan | nan | nan | Cerrado | 194.8 |
| cb759c32-6334-33a8-95bc-d635512f5364 | -15.02236 | -48.1693 | 2026-08-31 16:28:00 | NPP-375 | MIMOSO DE GOIÁS | GOIÁS | Brasil | 5213053 | 52 | 33 | nan | nan | nan | Cerrado | 8.0 |
| ef79e0bc-e7bc-34ca-b20a-93a493b73efb | -18.20989 | -43.98058 | 2026-08-31 16:28:00 | NPP-375 | DIAMANTINA | MINAS GERAIS | Brasil | 3121605 | 31 | 33 | nan | nan | nan | Cerrado | 5.5 |
| f7b8444f-fe19-3904-9b43-a5f5868415b3 | -17.13496 | -44.77316 | 2026-08-31 16:28:00 | NPP-375 | VÁRZEA DA PALMA | MINAS GERAIS | Brasil | 3170800 | 31 | 33 | nan | nan | nan | Cerrado | 2.8 |
| 42cb4fe3-5378-3bc7-bc4b-6b4d9c791070 | -17.88001 | -52.17503 | 2026-08-31 16:28:00 | NPP-375 | JATAÍ | GOIÁS | Brasil | 5211909 | 52 | 33 | nan | nan | nan | Cerrado | 22.1 |
| 6a7003df-3123-3bdf-ad48-168b0fb4b1e8 | -19.85894 | -47.9299 | 2026-08-31 16:28:00 | NPP-375 | UBERABA | MINAS GERAIS | Brasil | 3170107 | 31 | 33 | nan | nan | nan | Cerrado | 23.5 |
| 5cdd975e-9947-3203-bff2-2a277d2d14cc | -15.19739 | -46.22574 | 2026-08-31 16:28:00 | NPP-375 | FORMOSO | MINAS GERAIS | Brasil | 3126208 | 31 | 33 | nan | nan | nan | Cerrado | 7.1 |
| 81373e2b-cfff-30f1-a788-07b30a56853b | -14.6424 | -41.10571 | 2026-08-31 16:28:00 | NPP-375 | ANAGÉ | BAHIA | Brasil | 2901205 | 29 | 33 | nan | nan | nan | Caatinga | 4.5 |
| 055c6cd5-1073-3b15-aa72-8049b2b896be | -16.02216 | -54.40852 | 2026-08-31 16:28:00 | NPP-375 | POXORÉU | MATO GROSSO | Brasil | 5107008 | 51 | 33 | nan | nan | nan | Cerrado | 11.8 |
| 61173f0c-fedb-31ef-9ca8-8c99460c4377 | -16.35669 | -51.01002 | 2026-08-31 16:28:00 | NPP-375 | ISRAELÂNDIA | GOIÁS | Brasil | 5210307 | 52 | 33 | nan | nan | nan | Cerrado | 6.7 |
| 53b78ac1-19d5-39c2-9161-8cbb40d9d6f5 | -17.86695 | -52.1072 | 2026-08-31 16:28:00 | NPP-375 | JATAÍ | GOIÁS | Brasil | 5211909 | 52 | 33 | nan | nan | nan | Cerrado | 75.1 |
| 9761e2a4-5e43-3847-8058-0bbd801da3a0 | -16.70878 | -49.35035 | 2026-08-31 16:28:00 | NPP-375 | GOIÂNIA | GOIÁS | Brasil | 5208707 | 52 | 33 | nan | nan | nan | Cerrado | 6.3 |
| 4b8df625-6fd2-3a96-a107-cbefd1270f48 | -20.50154 | -41.90105 | 2026-08-31 16:28:00 | NPP-375 | CAPARAÓ | MINAS GERAIS | Brasil | 3112109 | 31 | 33 | nan | nan | nan | Mata Atlântica | 2.3 |
| 6c37d9e7-fe99-352e-ad2a-288fc417ed72 | -17.53052 | -52.55463 | 2026-08-31 16:28:00 | NPP-375 | MINEIROS | GOIÁS | Brasil | 5213103 | 52 | 33 | nan | nan | nan | Cerrado | 12.9 |
| 88bccab0-7c36-3554-bc77-011e2750d0c6 | -16.20082 | -49.31874 | 2026-08-31 16:28:00 | NPP-375 | PETROLINA DE GOIÁS | GOIÁS | Brasil | 5216809 | 52 | 33 | nan | nan | nan | Cerrado | 5.0 |
| 05145206-065f-330d-8c1a-8c2773fd838b | -19.6173 | -40.77998 | 2026-08-31 16:28:00 | NPP-375 | ITAGUAÇU | ESPÍRITO SANTO | Brasil | 3202702 | 32 | 33 | nan | nan | nan | Mata Atlântica | 4.1 |
| 94ff33de-fe2a-314d-9c09-a30a2a3bc4a2 | -17.84455 | -50.50152 | 2026-08-31 16:28:00 | NPP-375 | SANTA HELENA DE GOIÁS | GOIÁS | Brasil | 5219308 | 52 | 33 | nan | nan | nan | Cerrado | 68.5 |
| 380ee7bf-a96a-3805-982a-4bd0193a7d98 | -17.53453 | -39.94307 | 2026-08-31 16:28:00 | NPP-375 | CARAVELAS | BAHIA | Brasil | 2906907 | 29 | 33 | nan | nan | nan | Mata Atlântica | 2.1 |
| 2d4656c1-1172-3562-8147-1c8b159b8ab3 | -16.38104 | -45.11034 | 2026-08-31 16:28:00 | NPP-375 | SÃO ROMÃO | MINAS GERAIS | Brasil | 3164209 | 31 | 33 | nan | nan | nan | Cerrado | 10.8 |
| 98d93477-84fd-3c99-bb2e-d945d9c635e3 | -14.23095 | -42.41081 | 2026-08-31 16:28:00 | NPP-375 | CAETITÉ | BAHIA | Brasil | 2905206 | 29 | 33 | nan | nan | nan | Caatinga | 8.2 |
| 77a3053f-7f36-3d8b-9f8e-16df0708341a | -15.0421 | -41.16132 | 2026-08-31 16:28:00 | NPP-375 | BELO CAMPO | BAHIA | Brasil | 2903508 | 29 | 33 | nan | nan | nan | Mata Atlântica | 6.5 |
| 4d2fd957-01c2-3612-be22-5e00b7ae1250 | -15.67492 | -45.95198 | 2026-08-31 16:28:00 | NPP-375 | ARINOS | MINAS GERAIS | Brasil | 3104502 | 31 | 33 | nan | nan | nan | Cerrado | 3.0 |
| d7a4f1e9-f662-3857-b4e3-d6e907aedc61 | -14.2304 | -42.40709 | 2026-08-31 16:28:00 | NPP-375 | CAETITÉ | BAHIA | Brasil | 2905206 | 29 | 33 | nan | nan | nan | Caatinga | 7.3 |
| 285a7daf-9ce2-3478-b7a2-af6f170c041a | -17.8735 | -52.08817 | 2026-08-31 16:28:00 | NPP-375 | JATAÍ | GOIÁS | Brasil | 5211909 | 52 | 33 | nan | nan | nan | Cerrado | 288.4 |
| d0fa6a99-efd1-3c4d-bf84-11b1c5861a7f | -15.5685 | -39.46799 | 2026-08-31 16:28:00 | NPP-375 | CAMACAN | BAHIA | Brasil | 2905602 | 29 | 33 | nan | nan | nan | Mata Atlântica | 2.4 |
| 9db12037-2d12-35af-a9a6-6a00121a16f6 | -13.82815 | -39.74076 | 2026-08-31 16:28:00 | NPP-375 | APUAREMA | BAHIA | Brasil | 2901957 | 29 | 33 | nan | nan | nan | Mata Atlântica | 5.6 |
| e8fff3f7-9f6f-34ff-bbbe-e91e2ed59c73 | -14.2313 | -42.41122 | 2026-08-31 16:28:00 | NPP-375 | CAETITÉ | BAHIA | Brasil | 2905206 | 29 | 33 | nan | nan | nan | Caatinga | 7.7 |
| 3f28da5c-a584-31cb-bfe1-c096bc63c967 | -17.86128 | -52.09426 | 2026-08-31 16:28:00 | NPP-375 | JATAÍ | GOIÁS | Brasil | 5211909 | 52 | 33 | nan | nan | nan | Cerrado | 45.2 |
| b728e64b-88c6-3622-84ae-5e118813191d | -16.80447 | -41.65736 | 2026-08-31 16:28:00 | NPP-375 | PONTO DOS VOLANTES | MINAS GERAIS | Brasil | 3152170 | 31 | 33 | nan | nan | nan | Mata Atlântica | 2.5 |
| 2cc4a0c2-fb7f-3647-996b-6dd6535ebd89 | -19.76905 | -47.89505 | 2026-08-31 16:28:00 | NPP-375 | UBERABA | MINAS GERAIS | Brasil | 3170107 | 31 | 33 | nan | nan | nan | Cerrado | 4.8 |
| 5f2c1a89-4e57-3bf6-93e6-5f692155ae3b | -18.83289 | -46.77528 | 2026-08-31 16:28:00 | NPP-375 | GUIMARÂNIA | MINAS GERAIS | Brasil | 3128907 | 31 | 33 | nan | nan | nan | Cerrado | 4.9 |
| 13a42413-2900-30e9-917c-c63e1cd26243 | -19.84741 | -47.92051 | 2026-08-31 16:28:00 | NPP-375 | UBERABA | MINAS GERAIS | Brasil | 3170107 | 31 | 33 | nan | nan | nan | Cerrado | 194.8 |
| 95ded705-d46c-32c5-bc49-593798e28bb7 | -15.01809 | -48.18184 | 2026-08-31 16:28:00 | NPP-375 | MIMOSO DE GOIÁS | GOIÁS | Brasil | 5213053 | 52 | 33 | nan | nan | nan | Cerrado | 2.0 |
| ad6de4c5-fd66-36c3-b280-ad2073224e0d | -19.84242 | -47.92092 | 2026-08-31 16:28:00 | NPP-375 | UBERABA | MINAS GERAIS | Brasil | 3170107 | 31 | 33 | nan | nan | nan | Cerrado | 253.1 |
| b199050f-49ed-3264-8f90-e525e6244a5e | -15.21394 | -41.74979 | 2026-08-31 16:28:00 | NPP-375 | NINHEIRA | MINAS GERAIS | Brasil | 3144656 | 31 | 33 | nan | nan | nan | Mata Atlântica | 2.8 |
| e85e7587-e104-32a3-8c4a-94dd577d8d5c | -15.20573 | -46.22453 | 2026-08-31 16:28:00 | NPP-375 | FORMOSO | MINAS GERAIS | Brasil | 3126208 | 31 | 33 | nan | nan | nan | Cerrado | 4.4 |
| 7d6785df-cb9d-3d79-a553-c26a91851448 | -14.41391 | -41.46623 | 2026-08-31 16:28:00 | NPP-375 | ARACATU | BAHIA | Brasil | 2902005 | 29 | 33 | nan | nan | nan | Caatinga | 4.5 |
| 713b58cc-e0d2-34ba-8c16-88b47f7efb03 | -15.87193 | -48.10705 | 2026-08-31 16:28:00 | NPP-375 | BRASÍLIA | DISTRITO FEDERAL | Brasil | 5300108 | 53 | 33 | nan | nan | nan | Cerrado | 9.9 |
| 9a54b0b1-f953-3dbd-af7b-8593a26476b5 | -16.15347 | -46.67916 | 2026-08-31 16:28:00 | NPP-375 | UNAÍ | MINAS GERAIS | Brasil | 3170404 | 31 | 33 | nan | nan | nan | Cerrado | 4.2 |
| 43068c75-aaa9-3beb-b33f-4fe2f6c8dd4f | -20.73554 | -46.21012 | 2026-08-31 16:28:00 | NPP-375 | SÃO JOSÉ DA BARRA | MINAS GERAIS | Brasil | 3162948 | 31 | 33 | nan | nan | nan | Cerrado | 3.0 |
| a904cf85-9ed2-340b-a5a2-bc3b48f2a52d | -19.15011 | -45.50058 | 2026-08-31 16:28:00 | NPP-375 | ABAETÉ | MINAS GERAIS | Brasil | 3100203 | 31 | 33 | nan | nan | nan | Cerrado | 15.7 |
| 38c95455-6ef7-3d43-8f0b-8919f7eb7baa | -17.86175 | -52.0995 | 2026-08-31 16:28:00 | NPP-375 | JATAÍ | GOIÁS | Brasil | 5211909 | 52 | 33 | nan | nan | nan | Cerrado | 90.1 |
| 0f4bb7c6-f4fa-3ef0-8699-59ddbe7cc662 | -17.85722 | -50.51198 | 2026-08-31 16:28:00 | NPP-375 | SANTA HELENA DE GOIÁS | GOIÁS | Brasil | 5219308 | 52 | 33 | nan | nan | nan | Cerrado | 37.3 |
| 28bf5fd2-11f1-312d-abd1-8d76c9e02cd9 | -14.41101 | -40.91633 | 2026-08-31 16:28:00 | NPP-375 | CAETANOS | BAHIA | Brasil | 2905156 | 29 | 33 | nan | nan | nan | Caatinga | 5.8 |
| 38a98e57-8f91-3544-84bb-0097aa3ee95f | -15.04259 | -48.09818 | 2026-08-31 16:28:00 | NPP-375 | MIMOSO DE GOIÁS | GOIÁS | Brasil | 5213053 | 52 | 33 | nan | nan | nan | Cerrado | 80.4 |
| 75fa6ea0-a2bf-32cf-83f0-773784ca7051 | -21.32467 | -45.93298 | 2026-08-31 16:28:00 | NPP-375 | ALFENAS | MINAS GERAIS | Brasil | 3101607 | 31 | 33 | nan | nan | nan | Mata Atlântica | 11.4 |
| f05748c7-49e4-3055-a3be-d7c3a5fa3e21 | -18.5077 | -43.97331 | 2026-08-31 16:28:00 | NPP-375 | MONJOLOS | MINAS GERAIS | Brasil | 3142502 | 31 | 33 | nan | nan | nan | Cerrado | 13.7 |
| 8eb96bd5-0cab-34a5-9b5a-073e70d7005e | -20.29906 | -47.84332 | 2026-08-31 16:28:00 | NPP-375 | ITUVERAVA | SÃO PAULO | Brasil | 3524105 | 35 | 33 | nan | nan | nan | Cerrado | 28.5 |
| 3da94889-b533-34f4-a911-dbbabbcf476e | -17.3715 | -44.88452 | 2026-08-31 16:28:00 | NPP-375 | PIRAPORA | MINAS GERAIS | Brasil | 3151206 | 31 | 33 | nan | nan | nan | Cerrado | 7.1 |
| 031d222f-e710-3fbf-88fe-813e5acac8f8 | -15.16222 | -41.85215 | 2026-08-31 16:28:00 | NPP-375 | SÃO JOÃO DO PARAÍSO | MINAS GERAIS | Brasil | 3162708 | 31 | 33 | nan | nan | nan | Mata Atlântica | 2.3 |
| 8b442087-10d8-359a-9a42-8ee203ce09e0 | -15.66931 | -45.94123 | 2026-08-31 16:28:00 | NPP-375 | ARINOS | MINAS GERAIS | Brasil | 3104502 | 31 | 33 | nan | nan | nan | Cerrado | 7.4 |
| 8b90de31-31fa-3598-ab32-f5a13f2e75d9 | -17.87383 | -52.11206 | 2026-08-31 16:28:00 | NPP-375 | JATAÍ | GOIÁS | Brasil | 5211909 | 52 | 33 | nan | nan | nan | Cerrado | 75.1 |
| abe5bc05-9897-3a7b-9b47-58510ba65796 | -14.52587 | -42.78767 | 2026-08-31 16:28:00 | NPP-375 | PINDAÍ | BAHIA | Brasil | 2924504 | 29 | 33 | nan | nan | nan | Caatinga | 6.5 |
| 1d687e58-72d5-3df7-aa64-922c7d199041 | -16.72518 | -43.7844 | 2026-08-31 16:28:00 | NPP-375 | MONTES CLAROS | MINAS GERAIS | Brasil | 3143302 | 31 | 33 | nan | nan | nan | Cerrado | 4.2 |
| 739203f5-25b1-3773-a1dc-7b356421551f | -16.55717 | -52.5121 | 2026-08-31 16:28:00 | NPP-375 | DOVERLÂNDIA | GOIÁS | Brasil | 5207253 | 52 | 33 | nan | nan | nan | Cerrado | 50.4 |
| 9f3e4824-502d-3873-9deb-a15c8782a9fe | -14.99009 | -48.14025 | 2026-08-31 16:28:00 | NPP-375 | MIMOSO DE GOIÁS | GOIÁS | Brasil | 5213053 | 52 | 33 | nan | nan | nan | Cerrado | 45.8 |
| b9b6b325-446c-314d-bb3c-cca56d5be0e6 | -14.50009 | -40.33377 | 2026-08-31 16:28:00 | NPP-375 | POÇÕES | BAHIA | Brasil | 2925105 | 29 | 33 | nan | nan | nan | Mata Atlântica | 8.4 |
| 0175fab6-2bb5-332e-8fdd-2a1e69c5013b | -15.65289 | -40.95779 | 2026-08-31 16:28:00 | NPP-375 | DIVISÓPOLIS | MINAS GERAIS | Brasil | 3122454 | 31 | 33 | nan | nan | nan | Mata Atlântica | 3.6 |
| fa2f68af-78e2-3d4b-8d49-4e339b456adc | -17.87085 | -44.26352 | 2026-08-31 16:28:00 | NPP-375 | BUENÓPOLIS | MINAS GERAIS | Brasil | 3109204 | 31 | 33 | nan | nan | nan | Cerrado | 7.0 |
| 8e0ddcd4-cd32-396e-b3e6-db6f739f0f5c | -15.68231 | -48.22216 | 2026-08-31 16:28:00 | NPP-375 | BRASÍLIA | DISTRITO FEDERAL | Brasil | 5300108 | 53 | 33 | nan | nan | nan | Cerrado | 27.6 |
| 4cd78aa3-9297-3777-a479-a469603cac43 | -17.86907 | -52.10959 | 2026-08-31 16:28:00 | NPP-375 | JATAÍ | GOIÁS | Brasil | 5211909 | 52 | 33 | nan | nan | nan | Cerrado | 62.2 |
| 53f34b95-65d1-3c98-b084-8f7a7e92af30 | -15.09941 | -43.64128 | 2026-08-31 16:28:00 | NPP-375 | MATIAS CARDOSO | MINAS GERAIS | Brasil | 3140852 | 31 | 33 | nan | nan | nan | Caatinga | 5.5 |
| 3dc76e21-8094-301a-98fb-d4c7b6d9eb24 | -19.85396 | -47.93049 | 2026-08-31 16:28:00 | NPP-375 | UBERABA | MINAS GERAIS | Brasil | 3170107 | 31 | 33 | nan | nan | nan | Cerrado | 23.5 |
| 92cabb13-7b98-3510-85e0-c56522996da8 | -17.85641 | -50.50395 | 2026-08-31 16:28:00 | NPP-375 | SANTA HELENA DE GOIÁS | GOIÁS | Brasil | 5219308 | 52 | 33 | nan | nan | nan | Cerrado | 283.8 |
| 05f8cf3f-d470-33d8-acbc-00440a19bd75 | -17.18543 | -48.7449 | 2026-08-31 16:28:00 | NPP-375 | CRISTIANÓPOLIS | GOIÁS | Brasil | 5206305 | 52 | 33 | nan | nan | nan | Cerrado | 23.1 |
| e88fd97c-5641-324b-b8c9-27167af6465a | -16.56303 | -52.50611 | 2026-08-31 16:28:00 | NPP-375 | DOVERLÂNDIA | GOIÁS | Brasil | 5207253 | 52 | 33 | nan | nan | nan | Cerrado | 36.0 |
| a054325e-4caf-3ed2-9a82-a61cd6408571 | -18.26502 | -52.72961 | 2026-08-31 16:28:00 | NPP-375 | CHAPADÃO DO CÉU | GOIÁS | Brasil | 5205471 | 52 | 33 | nan | nan | nan | Cerrado | 7.8 |
| 2f54ebd3-cc1b-3285-bc30-b99a06135c30 | -14.98835 | -48.1366 | 2026-08-31 16:28:00 | NPP-375 | MIMOSO DE GOIÁS | GOIÁS | Brasil | 5213053 | 52 | 33 | nan | nan | nan | Cerrado | 54.4 |
| caed9d7f-224a-383c-92a5-9a19e0b7a0ce | -14.80271 | -40.67221 | 2026-08-31 16:28:00 | NPP-375 | VITÓRIA DA CONQUISTA | BAHIA | Brasil | 2933307 | 29 | 33 | nan | nan | nan | Mata Atlântica | 8.5 |
| 48beb1db-3787-35b3-9d33-297192b19040 | -15.78079 | -47.7994 | 2026-08-31 16:28:00 | NPP-375 | BRASÍLIA | DISTRITO FEDERAL | Brasil | 5300108 | 53 | 33 | nan | nan | nan | Cerrado | 104.7 |
| c7707f44-e160-343d-853d-f877c8fe65ce | -17.86491 | -52.08633 | 2026-08-31 16:28:00 | NPP-375 | JATAÍ | GOIÁS | Brasil | 5211909 | 52 | 33 | nan | nan | nan | Cerrado | 219.1 |
| 7fcfeab9-8e5c-3d86-9b09-73d99755455f | -17.29137 | -45.99813 | 2026-08-31 16:28:00 | NPP-375 | JOÃO PINHEIRO | MINAS GERAIS | Brasil | 3136306 | 31 | 33 | nan | nan | nan | Cerrado | 2.6 |
| 6c0842e8-03d0-383b-bd65-50c2a1efeb78 | -16.87402 | -48.28177 | 2026-08-31 16:28:00 | NPP-375 | ORIZONA | GOIÁS | Brasil | 5215306 | 52 | 33 | nan | nan | nan | Cerrado | 10.2 |
| d0f73793-fb3d-3c11-931c-3b9037538457 | -17.57471 | -46.51116 | 2026-08-31 16:28:00 | NPP-375 | LAGOA GRANDE | MINAS GERAIS | Brasil | 3137536 | 31 | 33 | nan | nan | nan | Cerrado | 4.1 |
| 7adcf084-92e2-3d28-9185-f7430075a819 | -20.28792 | -47.83315 | 2026-08-31 16:28:00 | NPP-375 | ITUVERAVA | SÃO PAULO | Brasil | 3524105 | 35 | 33 | nan | nan | nan | Cerrado | 26.1 |
| e74c0210-3df8-3a5a-9c89-7e966ee4eb42 | -16.87379 | -40.52667 | 2026-08-31 16:28:00 | NPP-375 | BERTÓPOLIS | MINAS GERAIS | Brasil | 3106606 | 31 | 33 | nan | nan | nan | Mata Atlântica | 8.5 |
| 20515f6a-70eb-3a93-880d-8178e962dcc6 | -20.8195 | -44.84212 | 2026-08-31 16:28:00 | NPP-375 | OLIVEIRA | MINAS GERAIS | Brasil | 3145604 | 31 | 33 | nan | nan | nan | Mata Atlântica | 4.6 |
| 6928cde0-5d00-3b7a-9170-59455d14388a | -21.16574 | -42.93666 | 2026-08-31 16:28:00 | NPP-375 | UBÁ | MINAS GERAIS | Brasil | 3169901 | 31 | 33 | nan | nan | nan | Mata Atlântica | 5.4 |
| f91f8e34-0a03-33aa-9abf-5865bd96ef0b | -15.18956 | -46.24104 | 2026-08-31 16:28:00 | NPP-375 | FORMOSO | MINAS GERAIS | Brasil | 3126208 | 31 | 33 | nan | nan | nan | Cerrado | 9.2 |
| bdae6a30-4ce0-37b3-92b0-3882bc2fff96 | -17.53408 | -41.31257 | 2026-08-31 16:28:00 | NPP-375 | TEÓFILO OTONI | MINAS GERAIS | Brasil | 3168606 | 31 | 33 | nan | nan | nan | Mata Atlântica | 31.2 |
| 29387ea8-92cb-3f21-941d-a541e46330a6 | -18.48041 | -43.97178 | 2026-08-31 16:28:00 | NPP-375 | MONJOLOS | MINAS GERAIS | Brasil | 3142502 | 31 | 33 | nan | nan | nan | Cerrado | 4.1 |
| 4bc5cbe2-7ca6-341d-bb38-317c37167078 | -15.18678 | -46.24251 | 2026-08-31 16:28:00 | NPP-375 | FORMOSO | MINAS GERAIS | Brasil | 3126208 | 31 | 33 | nan | nan | nan | Cerrado | 7.8 |
| 9699afa7-7ea4-37c0-9599-e76f1a8fde25 | -20.19884 | -44.45158 | 2026-08-31 16:28:00 | NPP-375 | ITATIAIUÇU | MINAS GERAIS | Brasil | 3133709 | 31 | 33 | nan | nan | nan | Mata Atlântica | 4.5 |
| bb58c967-15ae-327b-9909-f436b94fe619 | -17.30692 | -46.95899 | 2026-08-31 16:28:00 | NPP-375 | PARACATU | MINAS GERAIS | Brasil | 3147006 | 31 | 33 | nan | nan | nan | Cerrado | 22.4 |
| 3c9e4b1a-cfc1-32d2-9ca1-46eb83b38ad4 | -15.19273 | -46.23291 | 2026-08-31 16:28:00 | NPP-375 | FORMOSO | MINAS GERAIS | Brasil | 3126208 | 31 | 33 | nan | nan | nan | Cerrado | 8.7 |
| 4e82034e-1dcb-3267-a762-2139b2e0ae79 | -14.51476 | -41.17804 | 2026-08-31 16:28:00 | NPP-375 | CARAÍBAS | BAHIA | Brasil | 2906899 | 29 | 33 | nan | nan | nan | Caatinga | 1.5 |
| c9baf2fb-8af8-3b95-8900-a528538e7e7b | -16.71386 | -39.16541 | 2026-08-31 16:28:00 | NPP-375 | PORTO SEGURO | BAHIA | Brasil | 2925303 | 29 | 33 | nan | nan | nan | Mata Atlântica | 6.2 |
| 829c9275-9cfb-324c-a941-890e4792e9e5 | -19.11016 | -39.7537 | 2026-08-31 16:28:00 | NPP-375 | SÃO MATEUS | ESPÍRITO SANTO | Brasil | 3204906 | 32 | 33 | nan | nan | nan | Mata Atlântica | 4.7 |
| 45115ecb-ef07-3aba-8ac6-a586e68125a2 | -20.35279 | -42.29915 | 2026-08-31 16:28:00 | NPP-375 | MATIPÓ | MINAS GERAIS | Brasil | 3140902 | 31 | 33 | nan | nan | nan | Mata Atlântica | 3.4 |
| e24da96a-7e45-3a7c-8111-daf3cad5bf12 | -15.11178 | -48.15278 | 2026-08-31 16:28:00 | NPP-375 | MIMOSO DE GOIÁS | GOIÁS | Brasil | 5213053 | 52 | 33 | nan | nan | nan | Cerrado | 9.3 |
| 740ac769-b127-3650-98ba-cbcf97e63535 | -17.30572 | -46.95749 | 2026-08-31 16:28:00 | NPP-375 | PARACATU | MINAS GERAIS | Brasil | 3147006 | 31 | 33 | nan | nan | nan | Cerrado | 9.9 |
| eec4afc0-5112-38df-9347-4251d6d1f18f | -16.2952 | -39.5168 | 2026-08-31 16:28:00 | NPP-375 | EUNÁPOLIS | BAHIA | Brasil | 2910727 | 29 | 33 | nan | nan | nan | Mata Atlântica | 9.8 |


[Clique aqui para ver as próximas entradas](README111.md)
