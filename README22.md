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

## Dados Diários - Página 22

| ID | Latitude | Longitude | Data/Hora GMT | Satélite | Município | Estado | País | Município ID | Estado ID | País ID | Dias sem Chuva | Precipitação | Risco de Fogo | Bioma | FRP |
|----|----------|-----------|---------------|----------|-----------|--------|------|--------------|-----------|---------|----------------|--------------|----------------|-------|-----|
| cae6b70a-3d6b-31fe-b5a6-305fbfc47997 | -5.73865 | -42.04684 | 2025-10-05 03:32:00 | NPP-375D | SÃO MIGUEL DO TAPUIO | PIAUÍ | Brasil | 2210409 | 22 | 33 | nan | nan | nan | Caatinga | 2.2 |
| 42b305cc-b279-32e6-8461-14691e4d65dd | -5.91634 | -42.90122 | 2025-10-05 03:32:00 | NPP-375D | PALMEIRAIS | PIAUÍ | Brasil | 2207504 | 22 | 33 | nan | nan | nan | Caatinga | 4.3 |
| bccbfaf2-5c05-370d-90ff-90de93c3947c | -6.61155 | -43.71845 | 2025-10-05 03:32:00 | NPP-375D | SÃO JOÃO DOS PATOS | MARANHÃO | Brasil | 2111102 | 21 | 33 | nan | nan | nan | Cerrado | 3.5 |
| 161472a1-9969-3d35-8fc4-ef873f6fcb5d | -6.43293 | -46.02358 | 2025-10-05 03:32:00 | NPP-375D | FORMOSA DA SERRA NEGRA | MARANHÃO | Brasil | 2104099 | 21 | 33 | nan | nan | nan | Cerrado | 3.3 |
| 78974faf-3765-3dbc-bfaf-8296133720d8 | -6.36072 | -42.87964 | 2025-10-05 03:32:00 | NPP-375D | SÃO FRANCISCO DO MARANHÃO | MARANHÃO | Brasil | 2110906 | 21 | 33 | nan | nan | nan | Caatinga | 1.4 |
| 5533157d-467e-3631-b9e1-2cc157fa20fc | -6.42648 | -46.02739 | 2025-10-05 03:32:00 | NPP-375D | FORMOSA DA SERRA NEGRA | MARANHÃO | Brasil | 2104099 | 21 | 33 | nan | nan | nan | Cerrado | 2.3 |
| aac9f9d4-5348-3b31-b389-4015903f3990 | -6.70558 | -42.16405 | 2025-10-05 03:32:00 | NPP-375D | TANQUE DO PIAUÍ | PIAUÍ | Brasil | 2210979 | 22 | 33 | nan | nan | nan | Caatinga | 3.1 |
| dbc48c97-0969-34b9-a06b-dd4125e89dd2 | -5.78531 | -42.96675 | 2025-10-05 03:32:00 | NPP-375D | PALMEIRAIS | PIAUÍ | Brasil | 2207504 | 22 | 33 | nan | nan | nan | Caatinga | 1.4 |
| 9d080087-f90c-38f3-9d55-fbe6416b8759 | -7.29506 | -39.26509 | 2025-10-05 03:32:00 | NPP-375D | BARBALHA | CEARÁ | Brasil | 2301901 | 23 | 33 | nan | nan | nan | Caatinga | 2.2 |
| 749c48a5-25cc-3f2d-82b7-86aac9fa7791 | -6.41018 | -43.05967 | 2025-10-05 03:32:00 | NPP-375D | SÃO FRANCISCO DO MARANHÃO | MARANHÃO | Brasil | 2110906 | 21 | 33 | nan | nan | nan | Cerrado | 8.0 |
| b06a74a4-c7aa-3fd1-bcf9-4a894ef5da05 | -7.04309 | -42.76251 | 2025-10-05 03:32:00 | NPP-375D | NAZARÉ DO PIAUÍ | PIAUÍ | Brasil | 2206704 | 22 | 33 | nan | nan | nan | Caatinga | 1.7 |
| ea7cfb24-6402-3467-9a00-dd0852452073 | -5.78509 | -42.93391 | 2025-10-05 03:32:00 | NPP-375D | PALMEIRAIS | PIAUÍ | Brasil | 2207504 | 22 | 33 | nan | nan | nan | Caatinga | 85.2 |
| f88962b4-f712-3c49-bf85-b973c271aba9 | -5.38074 | -45.70429 | 2025-10-05 03:32:00 | NPP-375D | JENIPAPO DOS VIEIRAS | MARANHÃO | Brasil | 2105476 | 21 | 33 | nan | nan | nan | Cerrado | 3.7 |
| e89cac5d-0cd3-3e63-88d9-686268cbf38a | -5.78363 | -42.93568 | 2025-10-05 03:32:00 | NPP-375D | PALMEIRAIS | PIAUÍ | Brasil | 2207504 | 22 | 33 | nan | nan | nan | Caatinga | 118.5 |
| 7ba24699-e4b0-3cc7-ab80-9a13ce1d4bee | -6.91585 | -37.4453 | 2025-10-05 03:32:00 | NPP-375D | SÃO JOSÉ DE ESPINHARAS | PARAÍBA | Brasil | 2514404 | 25 | 33 | nan | nan | nan | Caatinga | 1.8 |
| 8b7422d7-da4d-3e5b-963a-02fdcf815c90 | -5.83717 | -42.88691 | 2025-10-05 03:32:00 | NPP-375D | PALMEIRAIS | PIAUÍ | Brasil | 2207504 | 22 | 33 | nan | nan | nan | Caatinga | 3.4 |
| 220487ff-183b-3cc4-b2cd-41715241db75 | -6.60197 | -44.32071 | 2025-10-05 03:32:00 | NPP-375D | PASTOS BONS | MARANHÃO | Brasil | 2108009 | 21 | 33 | nan | nan | nan | Cerrado | 2.1 |
| f9be07dc-6a44-3b81-be7b-309c19ff6fc0 | -5.77155 | -42.97369 | 2025-10-05 03:32:00 | NPP-375D | PALMEIRAIS | PIAUÍ | Brasil | 2207504 | 22 | 33 | nan | nan | nan | Caatinga | 1.2 |
| 6f6c825e-15f8-3e98-9b19-3457252fd66c | -6.12322 | -42.86279 | 2025-10-05 03:32:00 | NPP-375D | AMARANTE | PIAUÍ | Brasil | 2200509 | 22 | 33 | nan | nan | nan | Caatinga | 2.0 |
| e3ca128e-16c0-3663-b487-6a0a22b7bb33 | -5.77822 | -42.93738 | 2025-10-05 03:32:00 | NPP-375D | PALMEIRAIS | PIAUÍ | Brasil | 2207504 | 22 | 33 | nan | nan | nan | Caatinga | 85.2 |
| 06e165a4-a04e-35f8-b6b2-b792ac02fffa | -5.93324 | -43.33171 | 2025-10-05 03:32:00 | NPP-375D | LAGOA DO MATO | MARANHÃO | Brasil | 2105922 | 21 | 33 | nan | nan | nan | Cerrado | 3.6 |
| 3c9ed402-6deb-3a2c-97a1-1b702abdf8ee | -5.06786 | -40.47689 | 2025-10-05 03:32:00 | NPP-375D | CRATEÚS | CEARÁ | Brasil | 2304103 | 23 | 33 | nan | nan | nan | Caatinga | 4.2 |
| f2a660a2-f4ce-30e0-8238-bb27b79ff7f4 | -5.79618 | -42.9707 | 2025-10-05 03:32:00 | NPP-375D | PALMEIRAIS | PIAUÍ | Brasil | 2207504 | 22 | 33 | nan | nan | nan | Caatinga | 1.7 |
| b5a2c0bd-87f7-3df7-a490-900896fabad7 | -6.14728 | -44.61487 | 2025-10-05 03:32:00 | NPP-375D | MIRADOR | MARANHÃO | Brasil | 2106706 | 21 | 33 | nan | nan | nan | Cerrado | 1.9 |
| 7fc144ff-0c13-3778-b508-677db5420bca | -6.1464 | -44.63736 | 2025-10-05 03:32:00 | NPP-375D | MIRADOR | MARANHÃO | Brasil | 2106706 | 21 | 33 | nan | nan | nan | Cerrado | 13.8 |
| f03b05e0-646f-383f-9dbc-2530f15e86ed | -5.84355 | -44.45502 | 2025-10-05 03:32:00 | NPP-375D | JATOBÁ | MARANHÃO | Brasil | 2105450 | 21 | 33 | nan | nan | nan | Cerrado | 5.4 |
| 6b8bb175-785e-35fb-973b-3e26299b7b3b | -6.14139 | -44.66526 | 2025-10-05 03:32:00 | NPP-375D | MIRADOR | MARANHÃO | Brasil | 2106706 | 21 | 33 | nan | nan | nan | Cerrado | 20.8 |
| b59c9705-d7b7-3781-985c-cbabd0cdef0f | -5.26799 | -39.26727 | 2025-10-05 03:32:00 | NPP-375D | QUIXERAMOBIM | CEARÁ | Brasil | 2311405 | 23 | 33 | nan | nan | nan | Caatinga | 1.6 |
| 8a835887-e98d-3cce-8610-c3973af6116a | -5.26593 | -37.92065 | 2025-10-05 03:32:00 | NPP-375D | LIMOEIRO DO NORTE | CEARÁ | Brasil | 2307601 | 23 | 33 | nan | nan | nan | Caatinga | 1.4 |
| c44e5ef9-6268-3ee0-8f64-3a2c6171b1fb | -6.15092 | -44.66922 | 2025-10-05 03:32:00 | NPP-375D | MIRADOR | MARANHÃO | Brasil | 2106706 | 21 | 33 | nan | nan | nan | Cerrado | 75.0 |
| eb18b748-a5d7-363a-b708-8fcd6f642db7 | -6.37252 | -42.88238 | 2025-10-05 03:32:00 | NPP-375D | SÃO FRANCISCO DO MARANHÃO | MARANHÃO | Brasil | 2110906 | 21 | 33 | nan | nan | nan | Caatinga | 1.1 |
| 9f57478c-fe10-3d72-9020-dd57a58e1db3 | -6.32536 | -43.90409 | 2025-10-05 03:32:00 | NPP-375D | PARAIBANO | MARANHÃO | Brasil | 2107704 | 21 | 33 | nan | nan | nan | Cerrado | 3.2 |
| 7bb41425-811b-39fe-bb87-6930ab51d055 | -5.89433 | -42.91973 | 2025-10-05 03:32:00 | NPP-375D | PALMEIRAIS | PIAUÍ | Brasil | 2207504 | 22 | 33 | nan | nan | nan | Caatinga | 12.5 |
| bde1884a-4f23-3419-babe-1b2018369fcb | -5.77037 | -42.97552 | 2025-10-05 03:32:00 | NPP-375D | PALMEIRAIS | PIAUÍ | Brasil | 2207504 | 22 | 33 | nan | nan | nan | Caatinga | 1.1 |
| 63b318a0-aecc-332f-a14d-a7e5374f1953 | -5.46963 | -42.79461 | 2025-10-05 03:32:00 | NPP-375D | NAZÁRIA | PIAUÍ | Brasil | 2206720 | 22 | 33 | nan | nan | nan | Caatinga | 3.9 |
| 367c8d21-97a7-3dd3-8612-3ef56f8a4d2e | -5.75748 | -42.97773 | 2025-10-05 03:32:00 | NPP-375D | PALMEIRAIS | PIAUÍ | Brasil | 2207504 | 22 | 33 | nan | nan | nan | Caatinga | 1.1 |
| e92f713b-2da3-33d6-b8de-aab01dd7e723 | -6.14537 | -44.64309 | 2025-10-05 03:32:00 | NPP-375D | MIRADOR | MARANHÃO | Brasil | 2106706 | 21 | 33 | nan | nan | nan | Cerrado | 13.8 |
| cc69a498-2b4e-3c81-8fdc-dd9d7f2d9107 | -5.22262 | -43.70666 | 2025-10-05 03:32:00 | NPP-375D | CAXIAS | MARANHÃO | Brasil | 2103000 | 21 | 33 | nan | nan | nan | Cerrado | 1.4 |
| 71b49d85-92f5-39f7-bf68-19c00c4ba58a | -6.11628 | -42.86718 | 2025-10-05 03:32:00 | NPP-375D | AMARANTE | PIAUÍ | Brasil | 2200509 | 22 | 33 | nan | nan | nan | Caatinga | 2.0 |
| 4c3341ab-3951-353c-a4d9-a4dc783729f5 | -5.94219 | -43.5211 | 2025-10-05 03:32:00 | NPP-375D | LAGOA DO MATO | MARANHÃO | Brasil | 2105922 | 21 | 33 | nan | nan | nan | Cerrado | 5.0 |
| 07fdee2f-456f-34b8-b29c-a279bc6f9c4b | -5.78202 | -42.94484 | 2025-10-05 03:32:00 | NPP-375D | PALMEIRAIS | PIAUÍ | Brasil | 2207504 | 22 | 33 | nan | nan | nan | Caatinga | 8.6 |
| 3f2fecc8-ae11-37c2-a23b-06ed351850e9 | -4.64088 | -43.18525 | 2025-10-05 03:32:00 | NPP-375D | CAXIAS | MARANHÃO | Brasil | 2103000 | 21 | 33 | nan | nan | nan | Cerrado | 13.7 |
| fa2b4497-3a36-305c-8e01-1270f3d6274d | -6.35082 | -43.91629 | 2025-10-05 03:32:00 | NPP-375D | PARAIBANO | MARANHÃO | Brasil | 2107704 | 21 | 33 | nan | nan | nan | Cerrado | 5.3 |
| bba0d68c-2e17-368b-8958-5671d19dd7f4 | -7.42603 | -41.12602 | 2025-10-05 03:32:00 | NPP-375D | JAICÓS | PIAUÍ | Brasil | 2205201 | 22 | 33 | nan | nan | nan | Caatinga | 1.1 |
| 6a16035f-da58-35f1-991b-e650f36f1d17 | -6.70628 | -42.16022 | 2025-10-05 03:32:00 | NPP-375D | TANQUE DO PIAUÍ | PIAUÍ | Brasil | 2210979 | 22 | 33 | nan | nan | nan | Caatinga | 1.3 |
| 1d29e981-a2aa-34aa-8153-66f49a812804 | -5.96276 | -43.5143 | 2025-10-05 03:32:00 | NPP-375D | LAGOA DO MATO | MARANHÃO | Brasil | 2105922 | 21 | 33 | nan | nan | nan | Cerrado | 3.8 |
| aba59543-4f4a-373b-a982-289331c5014c | -6.61069 | -43.72319 | 2025-10-05 03:32:00 | NPP-375D | SÃO JOÃO DOS PATOS | MARANHÃO | Brasil | 2111102 | 21 | 33 | nan | nan | nan | Cerrado | 3.5 |
| a7a690ec-1887-300f-b419-753b15e2ce3b | -7.0576 | -42.78237 | 2025-10-05 03:32:00 | NPP-375D | NAZARÉ DO PIAUÍ | PIAUÍ | Brasil | 2206704 | 22 | 33 | nan | nan | nan | Caatinga | 1.4 |
| cce70793-6c83-3352-a4a5-7bde3b722640 | -6.16415 | -44.67219 | 2025-10-05 03:32:00 | NPP-375D | MIRADOR | MARANHÃO | Brasil | 2106706 | 21 | 33 | nan | nan | nan | Cerrado | 2.7 |
| 18fc9f7f-0745-3536-8392-c23c79147448 | -6.41178 | -43.05103 | 2025-10-05 03:32:00 | NPP-375D | SÃO FRANCISCO DO MARANHÃO | MARANHÃO | Brasil | 2110906 | 21 | 33 | nan | nan | nan | Cerrado | 2.4 |
| e0679ed3-a5a9-3f1b-aa3f-8323be9a7d3c | -6.14326 | -44.67334 | 2025-10-05 03:32:00 | NPP-375D | MIRADOR | MARANHÃO | Brasil | 2106706 | 21 | 33 | nan | nan | nan | Cerrado | 13.2 |
| e1e7a4e1-ac0e-3d33-99a4-a253c528b9c3 | -6.40916 | -43.0568 | 2025-10-05 03:32:00 | NPP-375D | SÃO FRANCISCO DO MARANHÃO | MARANHÃO | Brasil | 2110906 | 21 | 33 | nan | nan | nan | Cerrado | 12.6 |
| de898895-47a7-32d6-ab7b-19991fa05b55 | -5.89328 | -42.92033 | 2025-10-05 03:32:00 | NPP-375D | PALMEIRAIS | PIAUÍ | Brasil | 2207504 | 22 | 33 | nan | nan | nan | Caatinga | 12.7 |
| 9df6e34c-b655-3433-8c9b-abaade4d92a7 | -6.6292 | -42.42004 | 2025-10-05 03:32:00 | NPP-375D | ARRAIAL | PIAUÍ | Brasil | 2201002 | 22 | 33 | nan | nan | nan | Caatinga | 1.6 |
| 4d2d0ad3-274e-3ef5-bc13-b042b9a10fb3 | -6.4033 | -43.06322 | 2025-10-05 03:32:00 | NPP-375D | SÃO FRANCISCO DO MARANHÃO | MARANHÃO | Brasil | 2110906 | 21 | 33 | nan | nan | nan | Cerrado | 10.0 |
| effb5cec-cbd9-3329-8f54-0b66be3f36b2 | -5.58698 | -43.41071 | 2025-10-05 03:32:00 | NPP-375D | PARNARAMA | MARANHÃO | Brasil | 2107803 | 21 | 33 | nan | nan | nan | Cerrado | 1.5 |
| b1f71cfd-d74d-3e07-b369-cfd75a783853 | -5.8542 | -42.79249 | 2025-10-05 03:32:00 | NPP-375D | PALMEIRAIS | PIAUÍ | Brasil | 2207504 | 22 | 33 | nan | nan | nan | Caatinga | 1.7 |
| 4472cf87-a427-326f-a4d5-6d1300315b14 | -5.76594 | -42.96525 | 2025-10-05 03:32:00 | NPP-375D | PALMEIRAIS | PIAUÍ | Brasil | 2207504 | 22 | 33 | nan | nan | nan | Caatinga | 1.5 |
| c625c29b-3571-3bf0-bee3-a3c5078b84e1 | -7.0295 | -42.80365 | 2025-10-05 03:32:00 | NPP-375D | NAZARÉ DO PIAUÍ | PIAUÍ | Brasil | 2206704 | 22 | 33 | nan | nan | nan | Caatinga | 2.3 |
| 74898bf6-a091-31ab-9175-476c38b5d159 | -6.43973 | -44.15491 | 2025-10-05 03:32:00 | NPP-375D | SUCUPIRA DO NORTE | MARANHÃO | Brasil | 2111904 | 21 | 33 | nan | nan | nan | Cerrado | 2.2 |
| 6cd2234d-477f-39a5-ba0b-295c4fb98b6b | -7.43125 | -41.12696 | 2025-10-05 03:32:00 | NPP-375D | MASSAPÊ DO PIAUÍ | PIAUÍ | Brasil | 2206050 | 22 | 33 | nan | nan | nan | Caatinga | 1.4 |
| 86f138e8-1032-340b-bff2-29afdc96830f | -5.48771 | -42.79758 | 2025-10-05 03:32:00 | NPP-375D | TERESINA | PIAUÍ | Brasil | 2211001 | 22 | 33 | nan | nan | nan | Caatinga | 3.6 |
| 31f926a6-d4c7-33a8-8afc-1b24e3b18d59 | -6.33164 | -43.90563 | 2025-10-05 03:32:00 | NPP-375D | PARAIBANO | MARANHÃO | Brasil | 2107704 | 21 | 33 | nan | nan | nan | Cerrado | 4.1 |
| 8a5f0a73-32d2-33d6-a275-4300d175962b | -6.15974 | -44.6588 | 2025-10-05 03:32:00 | NPP-375D | MIRADOR | MARANHÃO | Brasil | 2106706 | 21 | 33 | nan | nan | nan | Cerrado | 40.5 |
| 87a3fb84-9916-3be4-b075-376ffb4148eb | -6.62464 | -42.41307 | 2025-10-05 03:32:00 | NPP-375D | ARRAIAL | PIAUÍ | Brasil | 2201002 | 22 | 33 | nan | nan | nan | Caatinga | 2.6 |
| b2fa200c-ad48-3c32-aa04-8c48d8010457 | -5.8883 | -42.91869 | 2025-10-05 03:32:00 | NPP-375D | PALMEIRAIS | PIAUÍ | Brasil | 2207504 | 22 | 33 | nan | nan | nan | Caatinga | 12.5 |
| 50011684-3094-3ea3-95a3-554b89562f94 | -5.76434 | -42.9743 | 2025-10-05 03:32:00 | NPP-375D | PALMEIRAIS | PIAUÍ | Brasil | 2207504 | 22 | 33 | nan | nan | nan | Caatinga | 1.1 |
| fae2bd0e-e307-398b-817c-acce6874515d | -6.01808 | -44.01971 | 2025-10-05 03:32:00 | NPP-375D | COLINAS | MARANHÃO | Brasil | 2103505 | 21 | 33 | nan | nan | nan | Cerrado | 2.4 |
| d2520286-aab5-3bb0-b3b8-f761d8804c04 | -6.14838 | -44.60897 | 2025-10-05 03:32:00 | NPP-375D | MIRADOR | MARANHÃO | Brasil | 2106706 | 21 | 33 | nan | nan | nan | Cerrado | 1.9 |
| cc50307f-fa2e-35bc-b5d0-f446453da250 | -5.84094 | -44.44905 | 2025-10-05 03:32:00 | NPP-375D | JATOBÁ | MARANHÃO | Brasil | 2105450 | 21 | 33 | nan | nan | nan | Cerrado | 18.6 |
| 36895e7c-8a2f-33ba-a45c-0df46318b0b0 | -3.83427 | -44.55569 | 2025-10-05 03:32:00 | NPP-375D | MATÕES DO NORTE | MARANHÃO | Brasil | 2106631 | 21 | 33 | nan | nan | nan | Cerrado | 1.8 |
| 0737cbc4-83ec-3d28-ad00-a800bb632646 | -5.77678 | -42.9792 | 2025-10-05 03:32:00 | NPP-375D | PALMEIRAIS | PIAUÍ | Brasil | 2207504 | 22 | 33 | nan | nan | nan | Caatinga | 1.5 |
| d0190731-3a41-3747-bb55-b2ca5391ff5d | -6.55027 | -44.16839 | 2025-10-05 03:32:00 | NPP-375D | PASTOS BONS | MARANHÃO | Brasil | 2108009 | 21 | 33 | nan | nan | nan | Cerrado | 1.1 |
| 6e413a2d-f428-38b0-b6d4-fc63239627ce | -7.05325 | -42.77307 | 2025-10-05 03:32:00 | NPP-375D | NAZARÉ DO PIAUÍ | PIAUÍ | Brasil | 2206704 | 22 | 33 | nan | nan | nan | Caatinga | 0.8 |
| 2100af66-4795-37ec-abf3-d2c5adb737ed | -6.01844 | -45.41797 | 2025-10-05 03:32:00 | NPP-375D | FERNANDO FALCÃO | MARANHÃO | Brasil | 2104081 | 21 | 33 | nan | nan | nan | Cerrado | 1.9 |
| 4fb47042-1da5-3971-ac5a-71374b607521 | -4.87734 | -45.85798 | 2025-10-05 03:32:00 | NPP-375D | ARAME | MARANHÃO | Brasil | 2100956 | 21 | 33 | nan | nan | nan | Amazônia | 7.5 |
| deb5a6da-6dc8-36cc-946c-f7a90910eceb | -4.44437 | -43.23887 | 2025-10-05 03:32:00 | NPP-375D | ALDEIAS ALTAS | MARANHÃO | Brasil | 2100303 | 21 | 33 | nan | nan | nan | Cerrado | 12.6 |
| 08c81bed-66ec-3172-8089-fd895e9813d7 | -5.06895 | -40.47065 | 2025-10-05 03:32:00 | NPP-375D | CRATEÚS | CEARÁ | Brasil | 2304103 | 23 | 33 | nan | nan | nan | Caatinga | 3.6 |
| 51994ce1-90b8-3733-87d3-b2de7d82c725 | -6.60849 | -44.32167 | 2025-10-05 03:32:00 | NPP-375D | PASTOS BONS | MARANHÃO | Brasil | 2108009 | 21 | 33 | nan | nan | nan | Cerrado | 2.1 |
| 8787ef12-dfc2-3eb9-a810-5e61db03b42f | -7.02171 | -42.78013 | 2025-10-05 03:32:00 | NPP-375D | NAZARÉ DO PIAUÍ | PIAUÍ | Brasil | 2206704 | 22 | 33 | nan | nan | nan | Caatinga | 4.9 |
| 8075948c-3330-31ac-bc28-bdc834aa6e3e | -6.02306 | -44.02514 | 2025-10-05 03:32:00 | NPP-375D | COLINAS | MARANHÃO | Brasil | 2103505 | 21 | 33 | nan | nan | nan | Cerrado | 4.4 |
| 5170821a-edaa-3d96-a6aa-f58f4e14bfef | -6.36238 | -43.91708 | 2025-10-05 03:32:00 | NPP-375D | PARAIBANO | MARANHÃO | Brasil | 2107704 | 21 | 33 | nan | nan | nan | Cerrado | 2.4 |
| cbac6f8c-cf36-3c57-aca4-43ac35a83d2f | -6.69999 | -41.95443 | 2025-10-05 03:32:00 | NPP-375D | OEIRAS | PIAUÍ | Brasil | 2207009 | 22 | 33 | nan | nan | nan | Caatinga | 1.9 |
| d9f4317a-9bf4-3e8e-a27f-e0e5e99ecc2f | -6.4007 | -43.06938 | 2025-10-05 03:32:00 | NPP-375D | SÃO FRANCISCO DO MARANHÃO | MARANHÃO | Brasil | 2110906 | 21 | 33 | nan | nan | nan | Cerrado | 12.5 |
| f47e6dcc-be48-37df-aa88-8bf5c990eb07 | -4.88587 | -37.49932 | 2025-10-05 03:32:00 | NPP-375D | ARACATI | CEARÁ | Brasil | 2301109 | 23 | 33 | nan | nan | nan | Caatinga | 3.1 |
| ad150d43-3ba6-3444-b01e-4620dcfc197e | -5.0923 | -37.6098 | 2025-10-05 03:32:00 | NPP-375D | BARAÚNA | RIO GRANDE DO NORTE | Brasil | 2401453 | 24 | 33 | nan | nan | nan | Caatinga | 1.8 |
| 01aca3d5-48de-35a9-a2a0-9a45e4c9c739 | -5.94597 | -42.87462 | 2025-10-05 03:32:00 | NPP-375D | PALMEIRAIS | PIAUÍ | Brasil | 2207504 | 22 | 33 | nan | nan | nan | Caatinga | 1.8 |
| 42dc697e-6eec-3a07-94f6-cdfa016e751a | -7.52331 | -37.99183 | 2025-10-05 03:32:00 | NPP-375D | NOVA OLINDA | PARAÍBA | Brasil | 2510204 | 25 | 33 | nan | nan | nan | Caatinga | 5.4 |
| 90fd29ac-f8e8-358d-862e-4760a71085fc | -5.78282 | -42.94028 | 2025-10-05 03:32:00 | NPP-375D | PALMEIRAIS | PIAUÍ | Brasil | 2207504 | 22 | 33 | nan | nan | nan | Caatinga | 118.5 |
| d751041a-92e9-3e9f-929f-f14b23be8ccb | -5.78425 | -42.93851 | 2025-10-05 03:32:00 | NPP-375D | PALMEIRAIS | PIAUÍ | Brasil | 2207504 | 22 | 33 | nan | nan | nan | Caatinga | 85.2 |
| 0f2e01c5-1700-301b-8f35-280adcb43702 | -6.40173 | -42.68834 | 2025-10-05 03:32:00 | NPP-375D | AMARANTE | PIAUÍ | Brasil | 2200509 | 22 | 33 | nan | nan | nan | Caatinga | 1.4 |
| 38305a41-6ebf-3847-9475-6b905b2612e1 | -5.93241 | -43.33638 | 2025-10-05 03:32:00 | NPP-375D | LAGOA DO MATO | MARANHÃO | Brasil | 2105922 | 21 | 33 | nan | nan | nan | Cerrado | 3.6 |
| 74798110-6c7b-30f5-ad9d-193e495dd7b7 | -4.64001 | -43.1902 | 2025-10-05 03:32:00 | NPP-375D | CAXIAS | MARANHÃO | Brasil | 2103000 | 21 | 33 | nan | nan | nan | Cerrado | 22.3 |
| da2d5126-09d7-3ff6-beee-0be89df848a5 | -6.0196 | -45.41178 | 2025-10-05 03:32:00 | NPP-375D | FERNANDO FALCÃO | MARANHÃO | Brasil | 2104081 | 21 | 33 | nan | nan | nan | Cerrado | 1.9 |
| 5adbc7da-2dad-33bf-aaec-ead2eeb32390 | -6.14334 | -44.65439 | 2025-10-05 03:32:00 | NPP-375D | MIRADOR | MARANHÃO | Brasil | 2106706 | 21 | 33 | nan | nan | nan | Cerrado | 23.6 |
| 39d52b27-b20d-3a23-9aa0-c3d23ed1d603 | -6.14902 | -44.66108 | 2025-10-05 03:32:00 | NPP-375D | MIRADOR | MARANHÃO | Brasil | 2106706 | 21 | 33 | nan | nan | nan | Cerrado | 20.8 |
| c391bd8c-b707-3cd1-afaf-f580d13c70ac | -6.40993 | -43.05246 | 2025-10-05 03:32:00 | NPP-375D | SÃO FRANCISCO DO MARANHÃO | MARANHÃO | Brasil | 2110906 | 21 | 33 | nan | nan | nan | Cerrado | 8.2 |
| 71e21be6-3c04-387d-96c7-3ee1ec8e2365 | -6.41255 | -43.04686 | 2025-10-05 03:32:00 | NPP-375D | SÃO FRANCISCO DO MARANHÃO | MARANHÃO | Brasil | 2110906 | 21 | 33 | nan | nan | nan | Cerrado | 2.4 |
| 5cef2418-ef18-3752-984c-e943185f4c0a | -6.7088 | -42.83522 | 2025-10-05 03:32:00 | NPP-375D | FRANCISCO AYRES | PIAUÍ | Brasil | 2204105 | 22 | 33 | nan | nan | nan | Caatinga | 1.8 |
| 0c780868-e25a-3dd3-ae9c-700c7907a44a | -4.44523 | -43.23391 | 2025-10-05 03:32:00 | NPP-375D | ALDEIAS ALTAS | MARANHÃO | Brasil | 2100303 | 21 | 33 | nan | nan | nan | Cerrado | 12.6 |


[Clique aqui para ver as próximas entradas](README23.md)
