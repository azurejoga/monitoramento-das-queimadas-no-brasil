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

## Dados Diários - Página 62

| ID | Latitude | Longitude | Data/Hora GMT | Satélite | Município | Estado | País | Município ID | Estado ID | País ID | Dias sem Chuva | Precipitação | Risco de Fogo | Bioma | FRP |
|----|----------|-----------|---------------|----------|-----------|--------|------|--------------|-----------|---------|----------------|--------------|----------------|-------|-----|
| 3f1d2929-e273-3829-a728-9924450c485a | -14.21276 | -46.46575 | 2024-10-08 04:36:00 | NOAA-21 | POSSE | GOIÁS | Brasil | 5218300 | 52 | 33 | nan | nan | nan | Cerrado | 1.7 |
| 171d891d-0353-35c2-8eec-cfa64d676a1f | -14.21217 | -46.4441 | 2024-10-08 04:36:00 | NOAA-21 | POSSE | GOIÁS | Brasil | 5218300 | 52 | 33 | nan | nan | nan | Cerrado | 2.2 |
| 9d693dce-6897-3e05-9443-c1584b85e3c1 | -14.21157 | -46.44836 | 2024-10-08 04:36:00 | NOAA-21 | POSSE | GOIÁS | Brasil | 5218300 | 52 | 33 | nan | nan | nan | Cerrado | 2.0 |
| bded3167-bcc0-34cb-91ba-461a6bf552fe | -14.20917 | -46.46516 | 2024-10-08 04:36:00 | NOAA-21 | POSSE | GOIÁS | Brasil | 5218300 | 52 | 33 | nan | nan | nan | Cerrado | 1.7 |
| 774af9ee-d1ba-3113-a3ca-257bc83d6bce | -14.20858 | -46.44352 | 2024-10-08 04:36:00 | NOAA-21 | POSSE | GOIÁS | Brasil | 5218300 | 52 | 33 | nan | nan | nan | Cerrado | 2.0 |
| c6fb6f98-54d4-3989-9d95-109ea9b619bf | -14.20797 | -46.44777 | 2024-10-08 04:36:00 | NOAA-21 | POSSE | GOIÁS | Brasil | 5218300 | 52 | 33 | nan | nan | nan | Cerrado | 2.4 |
| 2a85192a-9348-34c4-b4f2-7abfded9ab67 | -14.20558 | -46.43871 | 2024-10-08 04:36:00 | NOAA-21 | POSSE | GOIÁS | Brasil | 5218300 | 52 | 33 | nan | nan | nan | Cerrado | 2.0 |
| 0d9219e9-1744-3acf-8018-cf536f2ee8bc | -14.20498 | -46.44295 | 2024-10-08 04:36:00 | NOAA-21 | POSSE | GOIÁS | Brasil | 5218300 | 52 | 33 | nan | nan | nan | Cerrado | 2.0 |
| bda9756b-d3e1-3028-82ce-70975108f59a | -14.20137 | -46.4425 | 2024-10-08 04:36:00 | NOAA-21 | POSSE | GOIÁS | Brasil | 5218300 | 52 | 33 | nan | nan | nan | Cerrado | 2.0 |
| f429c2e0-d6d7-3b6f-ad7b-fd2002b10167 | -14.20076 | -46.44677 | 2024-10-08 04:36:00 | NOAA-21 | POSSE | GOIÁS | Brasil | 5218300 | 52 | 33 | nan | nan | nan | Cerrado | 1.8 |
| 0d88349c-909a-333b-8e7d-3c5d552668fd | -14.19655 | -46.4506 | 2024-10-08 04:36:00 | NOAA-21 | POSSE | GOIÁS | Brasil | 5218300 | 52 | 33 | nan | nan | nan | Cerrado | 1.8 |
| 11ae7ae5-3ada-3a58-ad64-c7b1845c1464 | -16.59639 | -46.48394 | 2024-10-08 04:36:00 | NOAA-21 | NATALÂNDIA | MINAS GERAIS | Brasil | 3144375 | 31 | 33 | nan | nan | nan | Cerrado | 2.6 |
| adbc60ca-6ec3-38f3-b766-b656fc48c2c4 | -16.59576 | -46.48847 | 2024-10-08 04:36:00 | NOAA-21 | NATALÂNDIA | MINAS GERAIS | Brasil | 3144375 | 31 | 33 | nan | nan | nan | Cerrado | 2.8 |
| 1031cf97-3b81-3a70-b76d-535174069014 | -16.59513 | -46.49305 | 2024-10-08 04:36:00 | NOAA-21 | NATALÂNDIA | MINAS GERAIS | Brasil | 3144375 | 31 | 33 | nan | nan | nan | Cerrado | 2.8 |
| eb27bd2e-93ab-308b-a060-04350f390843 | -16.5945 | -46.49763 | 2024-10-08 04:36:00 | NOAA-21 | NATALÂNDIA | MINAS GERAIS | Brasil | 3144375 | 31 | 33 | nan | nan | nan | Cerrado | 10.0 |
| 61e28a2f-5315-32c4-a348-20f1c7850003 | -16.59269 | -46.48338 | 2024-10-08 04:36:00 | NOAA-21 | NATALÂNDIA | MINAS GERAIS | Brasil | 3144375 | 31 | 33 | nan | nan | nan | Cerrado | 3.0 |
| c915a5d3-7323-3680-89d9-42600e790354 | -16.59207 | -46.48792 | 2024-10-08 04:36:00 | NOAA-21 | NATALÂNDIA | MINAS GERAIS | Brasil | 3144375 | 31 | 33 | nan | nan | nan | Cerrado | 2.4 |
| 3ef2dac3-a429-3900-84d6-784d4730b13f | -16.59144 | -46.4925 | 2024-10-08 04:36:00 | NOAA-21 | NATALÂNDIA | MINAS GERAIS | Brasil | 3144375 | 31 | 33 | nan | nan | nan | Cerrado | 2.4 |
| eacff861-f8c4-399e-abf9-6a491b435dc2 | -16.59081 | -46.49708 | 2024-10-08 04:36:00 | NOAA-21 | NATALÂNDIA | MINAS GERAIS | Brasil | 3144375 | 31 | 33 | nan | nan | nan | Cerrado | 10.2 |
| de478df2-bb36-3d62-a9f1-18357f6700cb | -16.589 | -46.48283 | 2024-10-08 04:36:00 | NOAA-21 | NATALÂNDIA | MINAS GERAIS | Brasil | 3144375 | 31 | 33 | nan | nan | nan | Cerrado | 3.0 |
| deb59a28-262b-3e29-9d07-a86778414e81 | -16.58837 | -46.48738 | 2024-10-08 04:36:00 | NOAA-21 | NATALÂNDIA | MINAS GERAIS | Brasil | 3144375 | 31 | 33 | nan | nan | nan | Cerrado | 2.4 |
| fd15a855-167b-32a7-8b4e-437dab93ad33 | -16.58774 | -46.49195 | 2024-10-08 04:36:00 | NOAA-21 | NATALÂNDIA | MINAS GERAIS | Brasil | 3144375 | 31 | 33 | nan | nan | nan | Cerrado | 2.4 |
| 733a314d-75e2-318a-9cef-b087d8a278ee | -16.5853 | -46.48227 | 2024-10-08 04:36:00 | NOAA-21 | NATALÂNDIA | MINAS GERAIS | Brasil | 3144375 | 31 | 33 | nan | nan | nan | Cerrado | 7.4 |
| d5eace3b-b3b8-34a2-8db0-2a747ee9b12a | -16.58468 | -46.48683 | 2024-10-08 04:36:00 | NOAA-21 | NATALÂNDIA | MINAS GERAIS | Brasil | 3144375 | 31 | 33 | nan | nan | nan | Cerrado | 12.6 |
| e9b9f48b-8cd2-3ddd-9eff-bbd72776fa3c | -16.56993 | -46.4568 | 2024-10-08 04:36:00 | NOAA-21 | NATALÂNDIA | MINAS GERAIS | Brasil | 3144375 | 31 | 33 | nan | nan | nan | Cerrado | 64.5 |
| da739ecd-0147-3b51-8c78-b8116a85e511 | -16.56931 | -46.46136 | 2024-10-08 04:36:00 | NOAA-21 | NATALÂNDIA | MINAS GERAIS | Brasil | 3144375 | 31 | 33 | nan | nan | nan | Cerrado | 64.5 |
| af8cd2f7-a348-3d90-8682-dc568860edec | -16.56684 | -46.45173 | 2024-10-08 04:36:00 | NOAA-21 | NATALÂNDIA | MINAS GERAIS | Brasil | 3144375 | 31 | 33 | nan | nan | nan | Cerrado | 20.0 |
| 58738980-1e53-3c6a-8b47-1ab98f3e2c9e | -16.56622 | -46.45629 | 2024-10-08 04:36:00 | NOAA-21 | NATALÂNDIA | MINAS GERAIS | Brasil | 3144375 | 31 | 33 | nan | nan | nan | Cerrado | 43.3 |
| 7b9a3d7c-7a1a-31ea-913b-33f1374d1881 | -16.5656 | -46.46085 | 2024-10-08 04:36:00 | NOAA-21 | NATALÂNDIA | MINAS GERAIS | Brasil | 3144375 | 31 | 33 | nan | nan | nan | Cerrado | 43.3 |
| a75488dd-5b88-3e61-ad72-963a0bbbb2ba | -16.56252 | -46.45577 | 2024-10-08 04:36:00 | NOAA-21 | NATALÂNDIA | MINAS GERAIS | Brasil | 3144375 | 31 | 33 | nan | nan | nan | Cerrado | 43.3 |
| 48adc258-1fb1-3a45-af48-d9b51cc10c3c | -16.5619 | -46.46032 | 2024-10-08 04:36:00 | NOAA-21 | NATALÂNDIA | MINAS GERAIS | Brasil | 3144375 | 31 | 33 | nan | nan | nan | Cerrado | 43.3 |
| 7d0b12fb-1ce9-3d11-ac3b-48013f154ef4 | -16.56129 | -46.46484 | 2024-10-08 04:36:00 | NOAA-21 | NATALÂNDIA | MINAS GERAIS | Brasil | 3144375 | 31 | 33 | nan | nan | nan | Cerrado | 4.6 |
| 41d4f9b9-8c75-3625-9434-cf4ead810568 | -16.55759 | -46.46427 | 2024-10-08 04:36:00 | NOAA-21 | NATALÂNDIA | MINAS GERAIS | Brasil | 3144375 | 31 | 33 | nan | nan | nan | Cerrado | 3.0 |
| 1ef2534f-48f9-3e46-a6ab-a4d9bc5aff58 | -16.54641 | -46.44583 | 2024-10-08 04:36:00 | NOAA-21 | NATALÂNDIA | MINAS GERAIS | Brasil | 3144375 | 31 | 33 | nan | nan | nan | Cerrado | 3.3 |
| 04166784-ad2a-3959-9287-591bf3720599 | -16.18508 | -46.43699 | 2024-10-08 04:36:00 | NOAA-21 | UNAÍ | MINAS GERAIS | Brasil | 3170404 | 31 | 33 | nan | nan | nan | Cerrado | 2.7 |
| e37a06df-7097-34bf-b320-b79e89af3899 | -16.88173 | -47.18604 | 2024-10-08 04:36:00 | NOAA-21 | PARACATU | MINAS GERAIS | Brasil | 3147006 | 31 | 33 | nan | nan | nan | Cerrado | 6.3 |
| 240094a7-2ceb-37b7-9c19-4478e6eed672 | -16.88132 | -47.13799 | 2024-10-08 04:36:00 | NOAA-21 | PARACATU | MINAS GERAIS | Brasil | 3147006 | 31 | 33 | nan | nan | nan | Cerrado | 5.3 |
| 52325af3-8988-3469-b1a3-f131970f20c1 | -16.88009 | -47.18831 | 2024-10-08 04:36:00 | NOAA-21 | PARACATU | MINAS GERAIS | Brasil | 3147006 | 31 | 33 | nan | nan | nan | Cerrado | 12.5 |
| b4792d99-1d50-37ae-8ea0-7ed4c255f075 | -16.87466 | -47.15895 | 2024-10-08 04:36:00 | NOAA-21 | PARACATU | MINAS GERAIS | Brasil | 3147006 | 31 | 33 | nan | nan | nan | Cerrado | 7.7 |
| fca64845-bd7f-3353-8796-f7694ff929bc | -16.87415 | -47.13694 | 2024-10-08 04:36:00 | NOAA-21 | PARACATU | MINAS GERAIS | Brasil | 3147006 | 31 | 33 | nan | nan | nan | Cerrado | 17.0 |
| 81fa274e-59fe-3906-b04c-d2013cb0ed46 | -16.8849 | -47.13853 | 2024-10-08 04:36:00 | NOAA-21 | PARACATU | MINAS GERAIS | Brasil | 3147006 | 31 | 33 | nan | nan | nan | Cerrado | 5.3 |
| 2c5149bc-02cf-3813-a678-d283d6242ab9 | -16.88067 | -47.18415 | 2024-10-08 04:36:00 | NOAA-21 | PARACATU | MINAS GERAIS | Brasil | 3147006 | 31 | 33 | nan | nan | nan | Cerrado | 3.3 |
| e515dd26-6ba2-34eb-b4ca-263aa0b55bbb | -16.87711 | -47.1418 | 2024-10-08 04:36:00 | NOAA-21 | PARACATU | MINAS GERAIS | Brasil | 3147006 | 31 | 33 | nan | nan | nan | Cerrado | 17.0 |
| d10b918e-0bfe-3fec-a0cb-b929cec03e7f | -16.86994 | -47.14073 | 2024-10-08 04:36:00 | NOAA-21 | PARACATU | MINAS GERAIS | Brasil | 3147006 | 31 | 33 | nan | nan | nan | Cerrado | 1.4 |
| 4eb04d04-9ee9-3f97-b5f3-93f0c20580f7 | -16.90539 | -46.94368 | 2024-10-08 04:36:00 | NOAA-21 | PARACATU | MINAS GERAIS | Brasil | 3147006 | 31 | 33 | nan | nan | nan | Cerrado | 2.9 |
| 503fcc03-6365-3adf-af65-67ad45f92cac | -16.88425 | -47.18467 | 2024-10-08 04:36:00 | NOAA-21 | PARACATU | MINAS GERAIS | Brasil | 3147006 | 31 | 33 | nan | nan | nan | Cerrado | 3.3 |
| 2ddbd0bd-a8de-30cc-885a-f7c4f1109268 | -16.87773 | -47.13746 | 2024-10-08 04:36:00 | NOAA-21 | PARACATU | MINAS GERAIS | Brasil | 3147006 | 31 | 33 | nan | nan | nan | Cerrado | 17.0 |
| 6d6fbeff-88a8-3cb1-9589-71e94141729e | -16.87291 | -47.1456 | 2024-10-08 04:36:00 | NOAA-21 | PARACATU | MINAS GERAIS | Brasil | 3147006 | 31 | 33 | nan | nan | nan | Cerrado | 2.1 |
| 5d172e81-f467-3382-9e48-2082b70cc279 | -16.87108 | -47.15841 | 2024-10-08 04:36:00 | NOAA-21 | PARACATU | MINAS GERAIS | Brasil | 3147006 | 31 | 33 | nan | nan | nan | Cerrado | 7.7 |
| 14b1f3b2-ce56-32bc-9099-0627ed8aab7e | -16.88531 | -47.18658 | 2024-10-08 04:36:00 | NOAA-21 | PARACATU | MINAS GERAIS | Brasil | 3147006 | 31 | 33 | nan | nan | nan | Cerrado | 6.3 |
| b45053d6-fcad-3921-80b1-8d65e74d3fa8 | -16.88113 | -47.19019 | 2024-10-08 04:36:00 | NOAA-21 | PARACATU | MINAS GERAIS | Brasil | 3147006 | 31 | 33 | nan | nan | nan | Cerrado | 7.4 |
| 535cebc3-ee85-3f2a-b012-50cfb6d18ef8 | -16.87824 | -47.15948 | 2024-10-08 04:36:00 | NOAA-21 | PARACATU | MINAS GERAIS | Brasil | 3147006 | 31 | 33 | nan | nan | nan | Cerrado | 2.5 |
| 5e94f988-0b99-32ae-a719-adcfe3f5e4e9 | -16.87353 | -47.14127 | 2024-10-08 04:36:00 | NOAA-21 | PARACATU | MINAS GERAIS | Brasil | 3147006 | 31 | 33 | nan | nan | nan | Cerrado | 17.0 |
| a2051deb-42fe-3817-b33a-b2dd182df0a9 | -19.19999 | -46.58964 | 2024-10-08 04:36:00 | NOAA-21 | SERRA DO SALITRE | MINAS GERAIS | Brasil | 3166808 | 31 | 33 | nan | nan | nan | Cerrado | 1.4 |
| 76776166-7af1-381d-afb0-3e70a22033b1 | -19.19685 | -46.58419 | 2024-10-08 04:36:00 | NOAA-21 | SERRA DO SALITRE | MINAS GERAIS | Brasil | 3166808 | 31 | 33 | nan | nan | nan | Cerrado | 2.9 |
| 11a3f880-6f15-3b75-9dd3-2bd46a8a5017 | -19.46688 | -46.84598 | 2024-10-08 04:36:00 | NOAA-21 | IBIÁ | MINAS GERAIS | Brasil | 3129509 | 31 | 33 | nan | nan | nan | Cerrado | 1.0 |
| 068a867f-dcb4-3bcd-b800-4f63e2d135ae | -18.88139 | -47.52393 | 2024-10-08 04:36:00 | NOAA-21 | ROMARIA | MINAS GERAIS | Brasil | 3156403 | 31 | 33 | nan | nan | nan | Cerrado | 0.9 |
| a128420e-e548-3e2d-8027-fcebd9c12a7d | -18.71406 | -47.17307 | 2024-10-08 04:36:00 | NOAA-21 | COROMANDEL | MINAS GERAIS | Brasil | 3119302 | 31 | 33 | nan | nan | nan | Cerrado | 1.4 |
| a29fecc6-a886-341d-b4da-26ae02cab29a | -18.31993 | -47.24562 | 2024-10-08 04:36:00 | NOAA-21 | COROMANDEL | MINAS GERAIS | Brasil | 3119302 | 31 | 33 | nan | nan | nan | Cerrado | 2.0 |
| 0298ca80-de2a-30a5-8c66-f50cf6e4f749 | -18.30968 | -47.15808 | 2024-10-08 04:36:00 | NOAA-21 | COROMANDEL | MINAS GERAIS | Brasil | 3119302 | 31 | 33 | nan | nan | nan | Cerrado | 2.3 |
| 41fcab50-deb1-3332-bc88-30d6d32d73c1 | -18.29458 | -47.15979 | 2024-10-08 04:36:00 | NOAA-21 | COROMANDEL | MINAS GERAIS | Brasil | 3119302 | 31 | 33 | nan | nan | nan | Cerrado | 1.4 |
| 45829788-3d86-3d06-925e-5da3c05f6a3e | -18.29428 | -47.15767 | 2024-10-08 04:36:00 | NOAA-21 | COROMANDEL | MINAS GERAIS | Brasil | 3119302 | 31 | 33 | nan | nan | nan | Cerrado | 2.4 |
| 447aeac9-288d-3e92-bbf9-d6b43c478236 | -18.29212 | -47.15055 | 2024-10-08 04:36:00 | NOAA-21 | COROMANDEL | MINAS GERAIS | Brasil | 3119302 | 31 | 33 | nan | nan | nan | Cerrado | 3.2 |
| f5477f2f-e0a1-3d1d-acaa-7d7f37efe3f1 | -18.29186 | -47.14848 | 2024-10-08 04:36:00 | NOAA-21 | COROMANDEL | MINAS GERAIS | Brasil | 3119302 | 31 | 33 | nan | nan | nan | Cerrado | 2.2 |
| 2cd3957e-5400-3aa9-9c0c-f3ec44183868 | -18.29154 | -47.15482 | 2024-10-08 04:36:00 | NOAA-21 | COROMANDEL | MINAS GERAIS | Brasil | 3119302 | 31 | 33 | nan | nan | nan | Cerrado | 3.2 |
| d8a3e2f7-b774-3f41-969b-62857ae7e8c6 | -18.29126 | -47.15272 | 2024-10-08 04:36:00 | NOAA-21 | COROMANDEL | MINAS GERAIS | Brasil | 3119302 | 31 | 33 | nan | nan | nan | Cerrado | 5.4 |
| f5bd2a1f-e1d3-3116-b06e-1e431efd17ef | -18.28883 | -47.14359 | 2024-10-08 04:36:00 | NOAA-21 | COROMANDEL | MINAS GERAIS | Brasil | 3119302 | 31 | 33 | nan | nan | nan | Cerrado | 2.2 |
| 480c3b26-c611-32b5-86fa-ae915512a3ea | -18.2852 | -47.14299 | 2024-10-08 04:36:00 | NOAA-21 | COROMANDEL | MINAS GERAIS | Brasil | 3119302 | 31 | 33 | nan | nan | nan | Cerrado | 9.3 |
| da18d053-6ff7-3d14-86be-99cea5fdd86c | -18.28279 | -47.13362 | 2024-10-08 04:36:00 | NOAA-21 | COROMANDEL | MINAS GERAIS | Brasil | 3119302 | 31 | 33 | nan | nan | nan | Cerrado | 3.5 |
| 1597f570-e2a6-31f4-b55a-5793afab6cf5 | -18.28216 | -47.13812 | 2024-10-08 04:36:00 | NOAA-21 | COROMANDEL | MINAS GERAIS | Brasil | 3119302 | 31 | 33 | nan | nan | nan | Cerrado | 3.5 |
| 7b385e53-ef99-388f-a704-14fd9e7d55a7 | -18.28157 | -47.14238 | 2024-10-08 04:36:00 | NOAA-21 | COROMANDEL | MINAS GERAIS | Brasil | 3119302 | 31 | 33 | nan | nan | nan | Cerrado | 9.3 |
| ba3b5cb6-c102-38ed-8541-c75d04092be1 | -18.27853 | -47.13754 | 2024-10-08 04:36:00 | NOAA-21 | COROMANDEL | MINAS GERAIS | Brasil | 3119302 | 31 | 33 | nan | nan | nan | Cerrado | 2.4 |
| ad2f5d80-fcc2-3785-b517-49b9f9d04f2b | -18.24724 | -46.98607 | 2024-10-08 04:36:00 | NOAA-21 | COROMANDEL | MINAS GERAIS | Brasil | 3119302 | 31 | 33 | nan | nan | nan | Cerrado | 1.2 |
| efdd4750-7ff8-3e98-ad04-30b3bd8e3ba4 | -18.24662 | -46.99064 | 2024-10-08 04:36:00 | NOAA-21 | COROMANDEL | MINAS GERAIS | Brasil | 3119302 | 31 | 33 | nan | nan | nan | Cerrado | 1.2 |
| a6577a05-4723-3c26-b3f1-c2db36efb450 | -20.02443 | -46.71364 | 2024-10-08 04:36:00 | NOAA-21 | TAPIRA | MINAS GERAIS | Brasil | 3168101 | 31 | 33 | nan | nan | nan | Cerrado | 0.9 |
| 1873ab0d-a662-39c5-93c4-d3badf426ca0 | -19.82192 | -47.39295 | 2024-10-08 04:36:00 | NOAA-21 | SACRAMENTO | MINAS GERAIS | Brasil | 3156908 | 31 | 33 | nan | nan | nan | Cerrado | 5.2 |
| daa256f2-3838-3373-93bd-fca534f9b586 | -19.81825 | -47.39247 | 2024-10-08 04:36:00 | NOAA-21 | SACRAMENTO | MINAS GERAIS | Brasil | 3156908 | 31 | 33 | nan | nan | nan | Cerrado | 5.2 |
| 13a7a77d-377f-308a-ac20-e918d73900af | -19.81398 | -47.3965 | 2024-10-08 04:36:00 | NOAA-21 | SACRAMENTO | MINAS GERAIS | Brasil | 3156908 | 31 | 33 | nan | nan | nan | Cerrado | 3.3 |
| 787594bc-ae39-3bc1-8875-4fff58a958bb | -17.51513 | -49.07221 | 2024-10-08 04:36:00 | NOAA-21 | PIRACANJUBA | GOIÁS | Brasil | 5217104 | 52 | 33 | nan | nan | nan | Cerrado | 2.1 |
| 9c5d3e54-095a-37b1-ac75-8ff14635ee81 | -17.51458 | -49.07592 | 2024-10-08 04:36:00 | NOAA-21 | PIRACANJUBA | GOIÁS | Brasil | 5217104 | 52 | 33 | nan | nan | nan | Cerrado | 2.1 |
| cc09c1a9-0619-3dcb-bd55-5e768192c759 | -17.51177 | -49.07168 | 2024-10-08 04:36:00 | NOAA-21 | PIRACANJUBA | GOIÁS | Brasil | 5217104 | 52 | 33 | nan | nan | nan | Cerrado | 2.1 |
| a6aee446-e531-3adf-a1c7-4107ce83d7d0 | -17.51122 | -49.0754 | 2024-10-08 04:36:00 | NOAA-21 | PIRACANJUBA | GOIÁS | Brasil | 5217104 | 52 | 33 | nan | nan | nan | Cerrado | 2.1 |
| 2af8d0ff-38dc-3dac-b7ee-a87a851cfe7c | -18.17047 | -48.52412 | 2024-10-08 04:36:00 | NOAA-21 | CORUMBAÍBA | GOIÁS | Brasil | 5205901 | 52 | 33 | nan | nan | nan | Cerrado | 4.0 |
| 6d19408e-7a55-3c83-adfa-72ce92689968 | -18.1699 | -48.52795 | 2024-10-08 04:36:00 | NOAA-21 | CORUMBAÍBA | GOIÁS | Brasil | 5205901 | 52 | 33 | nan | nan | nan | Cerrado | 2.3 |
| 2bbb3082-52b3-3859-9513-e04112d276b6 | -18.16761 | -48.51965 | 2024-10-08 04:36:00 | NOAA-21 | CORUMBAÍBA | GOIÁS | Brasil | 5205901 | 52 | 33 | nan | nan | nan | Cerrado | 2.8 |
| a6e9b66d-2083-3bf8-96a7-b1e620560bc0 | -18.16705 | -48.52352 | 2024-10-08 04:36:00 | NOAA-21 | CORUMBAÍBA | GOIÁS | Brasil | 5205901 | 52 | 33 | nan | nan | nan | Cerrado | 2.8 |
| 9be8fc5f-7b92-3a53-8bff-b737700021d2 | -18.54456 | -48.40856 | 2024-10-08 04:36:00 | NOAA-21 | ARAGUARI | MINAS GERAIS | Brasil | 3103504 | 31 | 33 | nan | nan | nan | Mata Atlântica | 1.4 |
| 0d3ab61a-a760-31bd-b7ba-abe9f75cfb61 | -18.54053 | -48.41197 | 2024-10-08 04:36:00 | NOAA-21 | ARAGUARI | MINAS GERAIS | Brasil | 3103504 | 31 | 33 | nan | nan | nan | Mata Atlântica | 1.4 |
| 6ea95777-140c-3b32-8f30-a1d32b6ee849 | -18.50432 | -48.46681 | 2024-10-08 04:36:00 | NOAA-21 | ARAGUARI | MINAS GERAIS | Brasil | 3103504 | 31 | 33 | nan | nan | nan | Mata Atlântica | 1.3 |
| ac8d7ea0-9ad4-355b-b890-cc6321b32f85 | -19.15115 | -48.29708 | 2024-10-08 04:36:00 | NOAA-21 | UBERLÂNDIA | MINAS GERAIS | Brasil | 3170206 | 31 | 33 | nan | nan | nan | Cerrado | 1.8 |
| 2354acae-6728-3a20-afd2-6161070969c5 | -19.12561 | -48.30133 | 2024-10-08 04:36:00 | NOAA-21 | UBERLÂNDIA | MINAS GERAIS | Brasil | 3170206 | 31 | 33 | nan | nan | nan | Cerrado | 3.0 |
| f255e817-ec65-3af3-9f40-63aacec334c7 | -18.19045 | -48.14211 | 2024-10-08 04:36:00 | NOAA-21 | GOIANDIRA | GOIÁS | Brasil | 5208509 | 52 | 33 | nan | nan | nan | Cerrado | 6.2 |
| c18f30bf-3521-3391-b08d-c28a3620bb90 | -18.18754 | -48.13764 | 2024-10-08 04:36:00 | NOAA-21 | GOIANDIRA | GOIÁS | Brasil | 5208509 | 52 | 33 | nan | nan | nan | Cerrado | 2.8 |
| 47222c8a-f9e1-3503-9ae2-cb8abee5528a | -18.18697 | -48.14161 | 2024-10-08 04:36:00 | NOAA-21 | GOIANDIRA | GOIÁS | Brasil | 5208509 | 52 | 33 | nan | nan | nan | Cerrado | 3.3 |
| 5661f1d9-c5af-3d48-b6b6-0f0ec35a29a4 | -18.18349 | -48.14106 | 2024-10-08 04:36:00 | NOAA-21 | GOIANDIRA | GOIÁS | Brasil | 5208509 | 52 | 33 | nan | nan | nan | Cerrado | 3.3 |
| 88e955ee-bf0b-3c65-8997-ec52ce99e97b | -19.76011 | -48.28497 | 2024-10-08 04:36:00 | NOAA-21 | CONCEIÇÃO DAS ALAGOAS | MINAS GERAIS | Brasil | 3117306 | 31 | 33 | nan | nan | nan | Cerrado | 16.6 |
| d35214a2-73ef-3fe9-a64c-a75fffbeae81 | -19.75953 | -48.2891 | 2024-10-08 04:36:00 | NOAA-21 | CONCEIÇÃO DAS ALAGOAS | MINAS GERAIS | Brasil | 3117306 | 31 | 33 | nan | nan | nan | Cerrado | 2.4 |
| 3c3374a0-b0e2-36c9-87ec-0f0bcf15d345 | -19.75917 | -48.28637 | 2024-10-08 04:36:00 | NOAA-21 | CONCEIÇÃO DAS ALAGOAS | MINAS GERAIS | Brasil | 3117306 | 31 | 33 | nan | nan | nan | Cerrado | 19.9 |
| 797dae3a-77c4-3d75-a458-1ae06a54f13c | -19.75566 | -48.28581 | 2024-10-08 04:36:00 | NOAA-21 | UBERABA | MINAS GERAIS | Brasil | 3170107 | 31 | 33 | nan | nan | nan | Cerrado | 1.2 |
| f3d4d884-a58a-3f0b-9b07-726f6f86fca1 | -19.56041 | -49.49874 | 2024-10-08 04:36:00 | NOAA-21 | CAMPINA VERDE | MINAS GERAIS | Brasil | 3111101 | 31 | 33 | nan | nan | nan | Cerrado | 1.6 |


[Clique aqui para ver as próximas entradas](README63.md)
