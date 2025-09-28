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
| 0c3b1766-0968-3d18-a6cc-3a21f39b898e | -2.97871 | -39.92916 | 2025-09-28 03:34:00 | NOAA-21 | ITAREMA | CEARÁ | Brasil | 2306553 | 23 | 33 | nan | nan | nan | Caatinga | 2.2 |
| e92b020a-faa1-3353-b8ec-b74f5d7d2dcf | -3.54404 | -39.80977 | 2025-09-28 03:34:00 | NOAA-21 | MIRAÍMA | CEARÁ | Brasil | 2308377 | 23 | 33 | nan | nan | nan | Caatinga | 2.4 |
| d2b7cad8-4e5b-3cc0-80a9-e9ec6f027f1a | -2.97882 | -39.93055 | 2025-09-28 03:34:00 | NOAA-21 | ITAREMA | CEARÁ | Brasil | 2306553 | 23 | 33 | nan | nan | nan | Caatinga | 1.6 |
| e0de94b3-87cb-3607-a6cf-92bc2ea962ca | -2.90934 | -40.49086 | 2025-09-28 03:34:00 | NOAA-21 | JIJOCA DE JERICOACOARA | CEARÁ | Brasil | 2307254 | 23 | 33 | nan | nan | nan | Caatinga | 6.9 |
| a9a569ac-7741-37d1-be10-66e4593ba7bc | -5.76588 | -42.79193 | 2025-09-28 03:36:00 | NOAA-21 | SÃO PEDRO DO PIAUÍ | PIAUÍ | Brasil | 2210508 | 22 | 33 | nan | nan | nan | Caatinga | 2.9 |
| fb3dfac7-b56d-3b4f-880f-ccc39672a7ac | -5.26877 | -44.73456 | 2025-09-28 03:36:00 | NOAA-21 | TUNTUM | MARANHÃO | Brasil | 2112308 | 21 | 33 | nan | nan | nan | Cerrado | 5.2 |
| 31d6b8b9-dc6b-3db3-b3fa-e5157cf066aa | -7.92723 | -42.67095 | 2025-09-28 03:36:00 | NOAA-21 | RIBEIRA DO PIAUÍ | PIAUÍ | Brasil | 2208874 | 22 | 33 | nan | nan | nan | Caatinga | 1.0 |
| 37003baf-c43a-3f09-8f5b-838c22fb8da2 | -5.79977 | -42.81878 | 2025-09-28 03:36:00 | NOAA-21 | SÃO PEDRO DO PIAUÍ | PIAUÍ | Brasil | 2210508 | 22 | 33 | nan | nan | nan | Caatinga | 2.2 |
| e15a8f72-58e3-372f-bd0b-d21fdcd4b8da | -9.29764 | -43.21685 | 2025-09-28 03:36:00 | NOAA-21 | CARACOL | PIAUÍ | Brasil | 2202505 | 22 | 33 | nan | nan | nan | Caatinga | 1.6 |
| 456a9780-712a-3974-a1ea-d15fac474a35 | -5.74403 | -42.88454 | 2025-09-28 03:36:00 | NOAA-21 | SÃO PEDRO DO PIAUÍ | PIAUÍ | Brasil | 2210508 | 22 | 33 | nan | nan | nan | Caatinga | 5.2 |
| adc3bc4d-30fd-3ae2-be65-c45e90e07d24 | -6.46425 | -44.21929 | 2025-09-28 03:36:00 | NOAA-21 | SUCUPIRA DO NORTE | MARANHÃO | Brasil | 2111904 | 21 | 33 | nan | nan | nan | Cerrado | 1.5 |
| 161bd866-d8fc-33f9-8fd7-97efff651476 | -5.88162 | -43.19598 | 2025-09-28 03:36:00 | NOAA-21 | PARNARAMA | MARANHÃO | Brasil | 2107803 | 21 | 33 | nan | nan | nan | Caatinga | 10.7 |
| 536aef71-536f-301a-879b-d31988815cfd | -5.54305 | -42.73662 | 2025-09-28 03:36:00 | NOAA-21 | MONSENHOR GIL | PIAUÍ | Brasil | 2206407 | 22 | 33 | nan | nan | nan | Caatinga | 2.1 |
| ea2a4291-b387-341d-aa5f-8a8e2bf9d57f | -6.13964 | -43.4769 | 2025-09-28 03:36:00 | NOAA-21 | LAGOA DO MATO | MARANHÃO | Brasil | 2105922 | 21 | 33 | nan | nan | nan | Cerrado | 4.0 |
| e43e9ce6-7afd-3b2c-b3b6-3370c9d96cc7 | -5.81052 | -42.82043 | 2025-09-28 03:36:00 | NOAA-21 | SÃO PEDRO DO PIAUÍ | PIAUÍ | Brasil | 2210508 | 22 | 33 | nan | nan | nan | Caatinga | 5.4 |
| 4d0bc54f-ac97-33be-97af-f38fdd9193de | -7.76051 | -45.7383 | 2025-09-28 03:36:00 | NOAA-21 | SAMBAÍBA | MARANHÃO | Brasil | 2109700 | 21 | 33 | nan | nan | nan | Cerrado | 3.8 |
| 7bd3d5f8-4427-3e67-8aa8-adfd1051947e | -5.63797 | -44.93293 | 2025-09-28 03:36:00 | NOAA-21 | TUNTUM | MARANHÃO | Brasil | 2112308 | 21 | 33 | nan | nan | nan | Cerrado | 2.5 |
| 4703c0a7-942f-3b27-bf1a-7bb6620ae7a6 | -7.10324 | -44.23156 | 2025-09-28 03:36:00 | NOAA-21 | ANTÔNIO ALMEIDA | PIAUÍ | Brasil | 2200806 | 22 | 33 | nan | nan | nan | Cerrado | 5.2 |
| c889b301-cb81-3b47-ac37-4578bf27ec66 | -8.64965 | -43.9906 | 2025-09-28 03:36:00 | NOAA-21 | CRISTINO CASTRO | PIAUÍ | Brasil | 2203107 | 22 | 33 | nan | nan | nan | Cerrado | 1.1 |
| 260fef11-6466-3e1e-b8f6-825faf774ec7 | -7.50356 | -44.30566 | 2025-09-28 03:36:00 | NOAA-21 | URUÇUÍ | PIAUÍ | Brasil | 2211209 | 22 | 33 | nan | nan | nan | Cerrado | 1.9 |
| c652105e-4239-3245-bebc-fa496a4dcdba | -5.90778 | -42.94603 | 2025-09-28 03:36:00 | NOAA-21 | PALMEIRAIS | PIAUÍ | Brasil | 2207504 | 22 | 33 | nan | nan | nan | Caatinga | 9.8 |
| 921afe29-386d-3896-9db2-45db9ce6be4b | -7.85484 | -43.79527 | 2025-09-28 03:36:00 | NOAA-21 | BERTOLÍNIA | PIAUÍ | Brasil | 2201705 | 22 | 33 | nan | nan | nan | Caatinga | 2.5 |
| 65dcf11e-4f00-328a-ada7-5b1f6b66c98a | -6.1144 | -43.45745 | 2025-09-28 03:36:00 | NOAA-21 | LAGOA DO MATO | MARANHÃO | Brasil | 2105922 | 21 | 33 | nan | nan | nan | Cerrado | 4.3 |
| d82d3635-eb2f-3061-93fb-1d87790beea2 | -5.27553 | -44.73363 | 2025-09-28 03:36:00 | NOAA-21 | TUNTUM | MARANHÃO | Brasil | 2112308 | 21 | 33 | nan | nan | nan | Cerrado | 4.5 |
| 83f0e4d4-5324-37c8-96c7-f95df99e52dc | -7.7828 | -47.02363 | 2025-09-28 03:36:00 | NOAA-21 | CAROLINA | MARANHÃO | Brasil | 2102804 | 21 | 33 | nan | nan | nan | Cerrado | 3.0 |
| 0e0a1269-9e2a-3f0e-824f-63dd653be1b3 | -5.53941 | -42.7376 | 2025-09-28 03:36:00 | NOAA-21 | MONSENHOR GIL | PIAUÍ | Brasil | 2206407 | 22 | 33 | nan | nan | nan | Caatinga | 3.4 |
| fafb424a-0abe-3399-a82b-6f56a6d4fe5d | -6.08502 | -42.63545 | 2025-09-28 03:36:00 | NOAA-21 | JARDIM DO MULATO | PIAUÍ | Brasil | 2205250 | 22 | 33 | nan | nan | nan | Caatinga | 5.9 |
| 1fb364f9-50c3-3acb-b739-20ca82edc77f | -6.45773 | -44.22222 | 2025-09-28 03:36:00 | NOAA-21 | SUCUPIRA DO NORTE | MARANHÃO | Brasil | 2111904 | 21 | 33 | nan | nan | nan | Cerrado | 1.9 |
| a540f5a1-818f-326c-be11-15b262457c24 | -6.78254 | -44.07765 | 2025-09-28 03:36:00 | NOAA-21 | NOVA IORQUE | MARANHÃO | Brasil | 2107308 | 21 | 33 | nan | nan | nan | Cerrado | 11.7 |
| 410a79a1-f303-30d5-9a01-d4256d4af60e | -5.71414 | -42.65805 | 2025-09-28 03:36:00 | NOAA-21 | MIGUEL LEÃO | PIAUÍ | Brasil | 2206308 | 22 | 33 | nan | nan | nan | Caatinga | 0.8 |
| 8182ca5c-68df-3a42-b48c-c0cef6fd7a24 | -6.31346 | -43.45462 | 2025-09-28 03:36:00 | NOAA-21 | SUCUPIRA DO RIACHÃO | MARANHÃO | Brasil | 2111953 | 21 | 33 | nan | nan | nan | Cerrado | 4.9 |
| 19e7a449-476d-38ad-9fad-cc8075e862d7 | -6.78185 | -44.08155 | 2025-09-28 03:36:00 | NOAA-21 | NOVA IORQUE | MARANHÃO | Brasil | 2107308 | 21 | 33 | nan | nan | nan | Cerrado | 11.7 |
| 6bec8bfa-cd82-37a7-a058-8219e5331502 | -5.82565 | -44.44628 | 2025-09-28 03:36:00 | NOAA-21 | JATOBÁ | MARANHÃO | Brasil | 2105450 | 21 | 33 | nan | nan | nan | Cerrado | 10.8 |
| 11ba8af6-e6b5-3c50-8d98-6f05411f215a | -6.53274 | -43.82774 | 2025-09-28 03:36:00 | NOAA-21 | PASTOS BONS | MARANHÃO | Brasil | 2108009 | 21 | 33 | nan | nan | nan | Cerrado | 2.0 |
| 6931e8c9-01cd-3941-9af5-21faac27a0a3 | -5.74799 | -42.83082 | 2025-09-28 03:36:00 | NOAA-21 | SÃO PEDRO DO PIAUÍ | PIAUÍ | Brasil | 2210508 | 22 | 33 | nan | nan | nan | Caatinga | 2.6 |
| 960d3a4f-74e7-35d0-8286-6bc8e63b986a | -5.75088 | -42.81441 | 2025-09-28 03:36:00 | NOAA-21 | SÃO PEDRO DO PIAUÍ | PIAUÍ | Brasil | 2210508 | 22 | 33 | nan | nan | nan | Caatinga | 5.2 |
| 1406d981-456d-3a9a-9e9f-3ff6aae9820e | -7.80346 | -47.002 | 2025-09-28 03:36:00 | NOAA-21 | CAROLINA | MARANHÃO | Brasil | 2102804 | 21 | 33 | nan | nan | nan | Cerrado | 10.5 |
| 53bea244-a40d-3d9c-b2be-7c4c78c05887 | -5.75802 | -42.80523 | 2025-09-28 03:36:00 | NOAA-21 | SÃO PEDRO DO PIAUÍ | PIAUÍ | Brasil | 2210508 | 22 | 33 | nan | nan | nan | Caatinga | 2.2 |
| acb6fef7-e362-383a-9181-7f53fb0432e0 | -6.49523 | -44.24667 | 2025-09-28 03:36:00 | NOAA-21 | SUCUPIRA DO NORTE | MARANHÃO | Brasil | 2111904 | 21 | 33 | nan | nan | nan | Cerrado | 2.1 |
| 78db4888-2131-388a-b03b-faf0a59df968 | -5.08984 | -37.60444 | 2025-09-28 03:36:00 | NOAA-21 | BARAÚNA | RIO GRANDE DO NORTE | Brasil | 2401453 | 24 | 33 | nan | nan | nan | Caatinga | 3.8 |
| e83792e3-ab63-3671-888e-c17012da5c84 | -5.69857 | -42.622 | 2025-09-28 03:36:00 | NOAA-21 | MONSENHOR GIL | PIAUÍ | Brasil | 2206407 | 22 | 33 | nan | nan | nan | Caatinga | 1.3 |
| 2de6ad01-424c-3d38-8c53-f1e77cdfb6c5 | -7.80103 | -47.01463 | 2025-09-28 03:36:00 | NOAA-21 | CAROLINA | MARANHÃO | Brasil | 2102804 | 21 | 33 | nan | nan | nan | Cerrado | 41.6 |
| c41b6d41-2d78-3d02-9f7a-b51b00d3dd4a | -5.63708 | -44.93789 | 2025-09-28 03:36:00 | NOAA-21 | TUNTUM | MARANHÃO | Brasil | 2112308 | 21 | 33 | nan | nan | nan | Cerrado | 2.6 |
| ddddd0d6-bd68-34dc-b2ba-e682e93093b4 | -6.27002 | -44.06897 | 2025-09-28 03:36:00 | NOAA-21 | COLINAS | MARANHÃO | Brasil | 2103505 | 21 | 33 | nan | nan | nan | Cerrado | 2.9 |
| 781984e1-0cad-35a9-9310-f6f5698c7d0d | -6.47781 | -44.24355 | 2025-09-28 03:36:00 | NOAA-21 | SUCUPIRA DO NORTE | MARANHÃO | Brasil | 2111904 | 21 | 33 | nan | nan | nan | Cerrado | 2.0 |
| 6c71ab05-7346-3e90-906e-5c04dcc77895 | -6.48295 | -44.24829 | 2025-09-28 03:36:00 | NOAA-21 | SUCUPIRA DO NORTE | MARANHÃO | Brasil | 2111904 | 21 | 33 | nan | nan | nan | Cerrado | 2.3 |
| 9e27c97d-5033-3ee2-a957-69a98c12936a | -6.40435 | -43.95668 | 2025-09-28 03:36:00 | NOAA-21 | PARAIBANO | MARANHÃO | Brasil | 2107704 | 21 | 33 | nan | nan | nan | Cerrado | 9.2 |
| 8ef3a71b-9b40-3db9-a593-1b0605013a90 | -6.11197 | -41.81343 | 2025-09-28 03:36:00 | NOAA-21 | AROAZES | PIAUÍ | Brasil | 2200905 | 22 | 33 | nan | nan | nan | Caatinga | 3.3 |
| d6cd9ec8-e73f-3f44-9f69-313cde022755 | -6.70349 | -44.57873 | 2025-09-28 03:36:00 | NOAA-21 | SUCUPIRA DO NORTE | MARANHÃO | Brasil | 2111904 | 21 | 33 | nan | nan | nan | Cerrado | 1.9 |
| fceefbc2-6e41-377e-b174-19624e4ed7ac | -5.69914 | -42.61874 | 2025-09-28 03:36:00 | NOAA-21 | MONSENHOR GIL | PIAUÍ | Brasil | 2206407 | 22 | 33 | nan | nan | nan | Caatinga | 1.3 |
| 3bccfb71-c7ac-3a4d-a320-b51ad7bd2a41 | -5.64585 | -44.92425 | 2025-09-28 03:36:00 | NOAA-21 | TUNTUM | MARANHÃO | Brasil | 2112308 | 21 | 33 | nan | nan | nan | Cerrado | 3.2 |
| beb62061-f32d-3854-b6c2-d8261d39c133 | -6.0708 | -42.43973 | 2025-09-28 03:36:00 | NOAA-21 | HUGO NAPOLEÃO | PIAUÍ | Brasil | 2204600 | 22 | 33 | nan | nan | nan | Caatinga | 2.3 |
| b1fc5b4e-5ac9-3805-85e5-10111a33d97d | -4.1496 | -40.00278 | 2025-09-28 03:36:00 | NOAA-21 | SANTA QUITÉRIA | CEARÁ | Brasil | 2312205 | 23 | 33 | nan | nan | nan | Caatinga | 2.7 |
| 060024d2-ba50-31ee-a6cf-f1f0c99d56e7 | -5.75458 | -42.82479 | 2025-09-28 03:36:00 | NOAA-21 | SÃO PEDRO DO PIAUÍ | PIAUÍ | Brasil | 2210508 | 22 | 33 | nan | nan | nan | Caatinga | 2.8 |
| 9da38409-60cd-37fe-a4cd-00dcb62a9c58 | -7.75244 | -45.74696 | 2025-09-28 03:36:00 | NOAA-21 | SAMBAÍBA | MARANHÃO | Brasil | 2109700 | 21 | 33 | nan | nan | nan | Cerrado | 3.4 |
| f7bebaf9-92ad-3368-8758-40085f7e3ea2 | -8.36651 | -41.41074 | 2025-09-28 03:36:00 | NOAA-21 | QUEIMADA NOVA | PIAUÍ | Brasil | 2208650 | 22 | 33 | nan | nan | nan | Caatinga | 1.0 |
| 17945c17-23d7-3972-a5e8-57f88110e3b0 | -5.88706 | -43.19718 | 2025-09-28 03:36:00 | NOAA-21 | PARNARAMA | MARANHÃO | Brasil | 2107803 | 21 | 33 | nan | nan | nan | Caatinga | 8.9 |
| b4cb0e3f-62f9-3afd-8bf6-0725c3cf9f48 | -6.71178 | -42.76051 | 2025-09-28 03:36:00 | NOAA-21 | FRANCISCO AYRES | PIAUÍ | Brasil | 2204105 | 22 | 33 | nan | nan | nan | Caatinga | 5.6 |
| 60041d00-c4b5-3407-8f64-8f8d72b88dec | -6.43401 | -43.51168 | 2025-09-28 03:36:00 | NOAA-21 | SUCUPIRA DO RIACHÃO | MARANHÃO | Brasil | 2111953 | 21 | 33 | nan | nan | nan | Cerrado | 9.0 |
| 405ca804-8325-3beb-982f-3dfbbd12c357 | -5.82046 | -44.441 | 2025-09-28 03:36:00 | NOAA-21 | JATOBÁ | MARANHÃO | Brasil | 2105450 | 21 | 33 | nan | nan | nan | Cerrado | 14.0 |
| 14e9751b-cb83-33bf-b68a-bc861858c06a | -5.64672 | -44.91933 | 2025-09-28 03:36:00 | NOAA-21 | TUNTUM | MARANHÃO | Brasil | 2112308 | 21 | 33 | nan | nan | nan | Cerrado | 3.2 |
| 705a77f9-f837-3e7f-9500-c0c77a52e751 | -6.31154 | -43.46542 | 2025-09-28 03:36:00 | NOAA-21 | SUCUPIRA DO RIACHÃO | MARANHÃO | Brasil | 2111953 | 21 | 33 | nan | nan | nan | Cerrado | 5.2 |
| 6a80e164-c009-3de4-b5c8-44fb1fb0b3cd | -5.41439 | -42.2686 | 2025-09-28 03:36:00 | NOAA-21 | ALTO LONGÁ | PIAUÍ | Brasil | 2200301 | 22 | 33 | nan | nan | nan | Caatinga | 2.0 |
| d33c55e4-c554-3b00-90fc-8d30ed9b20eb | -6.48537 | -44.50412 | 2025-09-28 03:36:00 | NOAA-21 | MIRADOR | MARANHÃO | Brasil | 2106706 | 21 | 33 | nan | nan | nan | Cerrado | 1.8 |
| b9613271-7c74-35a7-bc30-10215fa07f17 | -7.23228 | -44.76514 | 2025-09-28 03:36:00 | NOAA-21 | SÃO FÉLIX DE BALSAS | MARANHÃO | Brasil | 2110807 | 21 | 33 | nan | nan | nan | Cerrado | 2.4 |
| 84ed74f5-079a-337e-8dcd-4d2540e978fd | -7.79551 | -47.00716 | 2025-09-28 03:36:00 | NOAA-21 | CAROLINA | MARANHÃO | Brasil | 2102804 | 21 | 33 | nan | nan | nan | Cerrado | 10.5 |
| a4ac2212-4c64-36a1-b1c7-ba7eab1baea8 | -5.76339 | -42.80608 | 2025-09-28 03:36:00 | NOAA-21 | SÃO PEDRO DO PIAUÍ | PIAUÍ | Brasil | 2210508 | 22 | 33 | nan | nan | nan | Caatinga | 2.2 |
| ed9356bd-018f-3c59-8a2b-1f95317d43ea | -6.32133 | -41.88456 | 2025-09-28 03:36:00 | NOAA-21 | VALENÇA DO PIAUÍ | PIAUÍ | Brasil | 2211308 | 22 | 33 | nan | nan | nan | Caatinga | 1.7 |
| 67db3767-a39e-3250-b560-a041bc6c511c | -5.72946 | -42.84176 | 2025-09-28 03:36:00 | NOAA-21 | SÃO PEDRO DO PIAUÍ | PIAUÍ | Brasil | 2210508 | 22 | 33 | nan | nan | nan | Caatinga | 4.9 |
| 6ee6dfdd-65b2-317f-8243-1da6c77bc506 | -8.28827 | -45.45017 | 2025-09-28 03:36:00 | NOAA-21 | RIBEIRO GONÇALVES | PIAUÍ | Brasil | 2208908 | 22 | 33 | nan | nan | nan | Cerrado | 4.1 |
| ed3814b9-1705-3862-b772-449a755624ec | -6.71062 | -42.76691 | 2025-09-28 03:36:00 | NOAA-21 | FRANCISCO AYRES | PIAUÍ | Brasil | 2204105 | 22 | 33 | nan | nan | nan | Caatinga | 4.1 |
| 2cadb13a-0449-3b76-9b40-43e5da267492 | -6.07172 | -43.76611 | 2025-09-28 03:36:00 | NOAA-21 | PASSAGEM FRANCA | MARANHÃO | Brasil | 2107902 | 21 | 33 | nan | nan | nan | Cerrado | 4.2 |
| f60cf16c-b24e-3126-b813-b4c52aafe9d3 | -5.81109 | -42.8171 | 2025-09-28 03:36:00 | NOAA-21 | SÃO PEDRO DO PIAUÍ | PIAUÍ | Brasil | 2210508 | 22 | 33 | nan | nan | nan | Caatinga | 5.4 |
| 09e50874-463e-3687-a86f-a58fbd5f27f1 | -5.72764 | -43.33264 | 2025-09-28 03:36:00 | NOAA-21 | PARNARAMA | MARANHÃO | Brasil | 2107803 | 21 | 33 | nan | nan | nan | Cerrado | 5.0 |
| 37e96d70-3d6a-353a-8b86-45129a75ffcf | -7.23452 | -44.76712 | 2025-09-28 03:36:00 | NOAA-21 | SÃO FÉLIX DE BALSAS | MARANHÃO | Brasil | 2110807 | 21 | 33 | nan | nan | nan | Cerrado | 2.6 |
| e435eae1-e2cf-3b7f-9b44-b0485bfdd508 | -7.44089 | -43.19027 | 2025-09-28 03:36:00 | NOAA-21 | ITAUEIRA | PIAUÍ | Brasil | 2205102 | 22 | 33 | nan | nan | nan | Caatinga | 0.9 |
| 5d9e9457-ee6f-34e0-9d01-3f50167c0987 | -6.70475 | -42.77163 | 2025-09-28 03:36:00 | NOAA-21 | FRANCISCO AYRES | PIAUÍ | Brasil | 2204105 | 22 | 33 | nan | nan | nan | Caatinga | 3.3 |
| 730b76e7-b683-31ef-b9e3-c443230fc251 | -5.78196 | -42.82606 | 2025-09-28 03:36:00 | NOAA-21 | SÃO PEDRO DO PIAUÍ | PIAUÍ | Brasil | 2210508 | 22 | 33 | nan | nan | nan | Caatinga | 2.1 |
| adb42cc0-d0d9-3b34-b19d-3af998ab845b | -5.881 | -43.19961 | 2025-09-28 03:36:00 | NOAA-21 | PARNARAMA | MARANHÃO | Brasil | 2107803 | 21 | 33 | nan | nan | nan | Caatinga | 12.4 |
| 7f242ce9-dcae-3f25-8e2d-97bd62768bd5 | -6.9953 | -44.69649 | 2025-09-28 03:36:00 | NOAA-21 | BENEDITO LEITE | MARANHÃO | Brasil | 2101806 | 21 | 33 | nan | nan | nan | Cerrado | 2.4 |
| 5becb898-09d3-3777-9918-3da81a917207 | -5.41902 | -42.27272 | 2025-09-28 03:36:00 | NOAA-21 | ALTO LONGÁ | PIAUÍ | Brasil | 2200301 | 22 | 33 | nan | nan | nan | Caatinga | 1.9 |
| 3b3a422a-ac89-3f19-856d-37416fae9406 | -5.60078 | -43.37657 | 2025-09-28 03:36:00 | NOAA-21 | PARNARAMA | MARANHÃO | Brasil | 2107803 | 21 | 33 | nan | nan | nan | Cerrado | 16.4 |
| 2c74db18-b401-342f-a26b-cde753e97205 | -8.27264 | -45.46679 | 2025-09-28 03:36:00 | NOAA-21 | RIBEIRO GONÇALVES | PIAUÍ | Brasil | 2208908 | 22 | 33 | nan | nan | nan | Cerrado | 8.2 |
| 34588724-2bbf-36de-9703-b9ad70f984d0 | -7.62064 | -43.80021 | 2025-09-28 03:36:00 | NOAA-21 | BERTOLÍNIA | PIAUÍ | Brasil | 2201705 | 22 | 33 | nan | nan | nan | Caatinga | 1.9 |
| 8c90a7ab-db2f-3cc2-aefa-fb92c1616bd3 | -5.6139 | -43.36705 | 2025-09-28 03:36:00 | NOAA-21 | PARNARAMA | MARANHÃO | Brasil | 2107803 | 21 | 33 | nan | nan | nan | Cerrado | 6.6 |
| eb9dedef-a692-3829-a324-b4676c126ad3 | -8.18243 | -41.65263 | 2025-09-28 03:36:00 | NOAA-21 | SÃO FRANCISCO DE ASSIS DO PIAUÍ | PIAUÍ | Brasil | 2209658 | 22 | 33 | nan | nan | nan | Caatinga | 2.0 |
| 3ca1ea06-81d2-3ae5-9192-d91d2005f8e3 | -5.35972 | -45.03771 | 2025-09-28 03:36:00 | NOAA-21 | BARRA DO CORDA | MARANHÃO | Brasil | 2101608 | 21 | 33 | nan | nan | nan | Cerrado | 2.2 |
| a6b1f2f0-7471-3798-b5a8-21854680b1f7 | -5.8081 | -42.83443 | 2025-09-28 03:36:00 | NOAA-21 | SÃO PEDRO DO PIAUÍ | PIAUÍ | Brasil | 2210508 | 22 | 33 | nan | nan | nan | Caatinga | 3.2 |
| f70cfb75-3c21-314e-8a2c-d3d929e56648 | -6.42708 | -43.51855 | 2025-09-28 03:36:00 | NOAA-21 | SUCUPIRA DO RIACHÃO | MARANHÃO | Brasil | 2111953 | 21 | 33 | nan | nan | nan | Cerrado | 9.6 |
| 8347f861-e88b-3405-8f3f-d5bb3dd7e605 | -5.8045 | -42.82333 | 2025-09-28 03:36:00 | NOAA-21 | SÃO PEDRO DO PIAUÍ | PIAUÍ | Brasil | 2210508 | 22 | 33 | nan | nan | nan | Caatinga | 1.9 |
| a07b4a81-7909-3aa6-a225-08cefd242d6d | -5.6441 | -44.93407 | 2025-09-28 03:36:00 | NOAA-21 | TUNTUM | MARANHÃO | Brasil | 2112308 | 21 | 33 | nan | nan | nan | Cerrado | 8.6 |
| e2514678-de03-3e1e-b55a-bba292993345 | -7.92877 | -42.67799 | 2025-09-28 03:36:00 | NOAA-21 | RIBEIRA DO PIAUÍ | PIAUÍ | Brasil | 2208874 | 22 | 33 | nan | nan | nan | Caatinga | 1.2 |
| bbebe601-57b7-3641-bb63-8db48e402ff8 | -5.37576 | -42.3002 | 2025-09-28 03:36:00 | NOAA-21 | ALTO LONGÁ | PIAUÍ | Brasil | 2200301 | 22 | 33 | nan | nan | nan | Caatinga | 1.2 |
| 544d9d31-83e8-3428-aebd-447a85c06439 | -7.42289 | -40.07481 | 2025-09-28 03:36:00 | NOAA-21 | BODOCÓ | PERNAMBUCO | Brasil | 2602001 | 26 | 33 | nan | nan | nan | Caatinga | 2.2 |
| 90b446bc-8304-3ee6-8087-37b286fd99dd | -5.81591 | -42.82112 | 2025-09-28 03:36:00 | NOAA-21 | SÃO PEDRO DO PIAUÍ | PIAUÍ | Brasil | 2210508 | 22 | 33 | nan | nan | nan | Caatinga | 5.4 |
| 1928a6b6-5b23-3de2-a1eb-9047cb2d34e5 | -8.28301 | -45.4446 | 2025-09-28 03:36:00 | NOAA-21 | BAIXA GRANDE DO RIBEIRO | PIAUÍ | Brasil | 2201150 | 22 | 33 | nan | nan | nan | Cerrado | 5.5 |
| 0b5e3486-323b-3de7-bf77-f72dd8eb1668 | -6.31705 | -43.46655 | 2025-09-28 03:36:00 | NOAA-21 | SUCUPIRA DO RIACHÃO | MARANHÃO | Brasil | 2111953 | 21 | 33 | nan | nan | nan | Cerrado | 5.2 |
| f947adb1-c156-3a76-8471-3cf9bb9f75cd | -6.53552 | -43.82767 | 2025-09-28 03:36:00 | NOAA-21 | PASTOS BONS | MARANHÃO | Brasil | 2108009 | 21 | 33 | nan | nan | nan | Cerrado | 4.3 |
| ab573d3d-c3ad-3561-932f-c181f3608e4d | -8.63909 | -44.83825 | 2025-09-28 03:36:00 | NOAA-21 | CURRAIS | PIAUÍ | Brasil | 2203230 | 22 | 33 | nan | nan | nan | Cerrado | 2.3 |
| 1723ec26-46af-3329-80f3-76f35b8b32a0 | -8.27957 | -45.46329 | 2025-09-28 03:36:00 | NOAA-21 | RIBEIRO GONÇALVES | PIAUÍ | Brasil | 2208908 | 22 | 33 | nan | nan | nan | Cerrado | 5.5 |


[Clique aqui para ver as próximas entradas](README12.md)
