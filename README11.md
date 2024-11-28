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
| 86829579-9812-31b4-a3f9-27feacbfb6a6 | -2.8085 | -51.575699 | 2024-11-28 00:38:00 | METOP-B | ANAPU | PARÁ | Brasil | 1500859 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| b0cc264c-ba40-3489-a339-4e927367c7be | -2.8676 | -46.860001 | 2024-11-28 00:38:00 | METOP-B | PARAGOMINAS | PARÁ | Brasil | 1505502 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| 7fab643b-9317-3cd2-93eb-f9516ca5775c | -3.6489 | -54.434502 | 2024-11-28 00:38:00 | METOP-B | PLACAS | PARÁ | Brasil | 1505650 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| de39b4b4-ffe6-3922-8ee2-e4d876ba6946 | -17.6159 | -53.7383 | 2024-11-28 00:38:00 | METOP-B | SONORA | MATO GROSSO DO SUL | Brasil | 5007935 | 50 | 33 | nan | nan | nan | Cerrado | nan |
| 807a1424-760b-35d4-9b75-7459498553b8 | -2.8118 | -51.590099 | 2024-11-28 00:38:00 | METOP-B | ANAPU | PARÁ | Brasil | 1500859 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| c34f04ec-898f-3c12-8ca5-4028f5668428 | -2.7045 | -51.980202 | 2024-11-28 00:38:00 | METOP-B | SENADOR JOSÉ PORFÍRIO | PARÁ | Brasil | 1507805 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| 2a3e06d9-1cbb-35ac-a688-fba89f70a306 | -3.1275 | -53.258999 | 2024-11-28 00:38:00 | METOP-B | MEDICILÂNDIA | PARÁ | Brasil | 1504455 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| 0e1e6d9d-424b-3a18-9ac6-e7dab0a406bd | -3.1198 | -53.820202 | 2024-11-28 00:38:00 | METOP-B | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| b113ced8-e462-36df-a018-1edb1da3db93 | -2.6275 | -54.058899 | 2024-11-28 00:38:00 | METOP-B | PRAINHA | PARÁ | Brasil | 1506005 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| 4dbc9975-1ce7-3557-acd8-f26377234c17 | -3.5235 | -50.506199 | 2024-11-28 00:38:00 | METOP-B | PACAJÁ | PARÁ | Brasil | 1505486 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| 3f13b9a6-294f-3ea0-9e2c-557d263d7035 | -2.6187 | -53.974201 | 2024-11-28 00:38:00 | METOP-B | PRAINHA | PARÁ | Brasil | 1506005 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| 948a6fe1-1de3-3b19-bb3f-e6b447729f0d | -2.4508 | -53.9608 | 2024-11-28 00:38:00 | METOP-B | PRAINHA | PARÁ | Brasil | 1506005 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| 8b6d798b-d4a0-3b70-a30b-428818fc50e5 | -2.5964 | -54.058498 | 2024-11-28 00:38:00 | METOP-B | PRAINHA | PARÁ | Brasil | 1506005 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| f7bbf7ef-55b8-3fbf-b003-71fa5e720804 | -3.2596 | -50.614498 | 2024-11-28 00:38:00 | METOP-B | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| f499e22e-a1ca-393b-b89a-10612607cde1 | -3.3985 | -50.320202 | 2024-11-28 00:38:00 | METOP-B | PACAJÁ | PARÁ | Brasil | 1505486 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| 66b0539d-58f5-3e6b-a23e-5710dd93d150 | -3.4705 | -51.585701 | 2024-11-28 00:38:00 | METOP-B | ANAPU | PARÁ | Brasil | 1500859 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| 5e2db1fc-f06f-3793-94d9-7cfe78782a47 | -1.5527 | -46.056499 | 2024-11-28 00:38:00 | METOP-B | CARUTAPERA | MARANHÃO | Brasil | 2102903 | 21 | 33 | nan | nan | nan | Amazônia | nan |
| 0ec7f195-b77a-3784-ae85-456abdd9c528 | -3.2537 | -50.769001 | 2024-11-28 00:38:00 | METOP-B | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| 6447bab9-257e-34e6-bdc8-bca0f4b2b77b | -2.8527 | -54.052601 | 2024-11-28 00:38:00 | METOP-B | PRAINHA | PARÁ | Brasil | 1506005 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| 09792c16-167f-34e0-9d12-b6a07f36fa52 | -2.954 | -51.581001 | 2024-11-28 00:38:00 | METOP-B | ANAPU | PARÁ | Brasil | 1500859 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| 11c219ba-8a39-37f2-8a33-a7b6cc6253e1 | -2.7342 | -48.9058 | 2024-11-28 00:38:00 | METOP-B | TAILÂNDIA | PARÁ | Brasil | 1507953 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| 0456f3af-822d-3ff2-869a-8caeb0029f8a | -2.8315 | -54.050098 | 2024-11-28 00:38:00 | METOP-B | PRAINHA | PARÁ | Brasil | 1506005 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| 075addf3-5e57-3a00-9cab-fb67f18eda73 | -2.8145 | -53.013699 | 2024-11-28 00:38:00 | METOP-B | MEDICILÂNDIA | PARÁ | Brasil | 1504455 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| 7f8af2e7-2a4e-3243-9e47-d4d6503fc0e7 | -3.0896 | -54.557598 | 2024-11-28 00:38:00 | METOP-B | MOJUÍ DOS CAMPOS | PARÁ | Brasil | 1504752 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| b990dce5-d15b-3300-bd25-1e2a58937345 | -3.3998 | -50.1008 | 2024-11-28 00:38:00 | METOP-B | PACAJÁ | PARÁ | Brasil | 1505486 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| 4ca36153-402b-34c6-8433-3c3348e904eb | -3.5857 | -50.327702 | 2024-11-28 00:38:00 | METOP-B | PACAJÁ | PARÁ | Brasil | 1505486 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| a909562d-968d-39c6-85e5-3afeb907e725 | -3.245 | -51.546001 | 2024-11-28 00:38:00 | METOP-B | ANAPU | PARÁ | Brasil | 1500859 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| f31290b9-d539-3880-91d7-b409b7516eb3 | -2.8919 | -51.5798 | 2024-11-28 00:38:00 | METOP-B | ANAPU | PARÁ | Brasil | 1500859 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| 73c5b810-6f2f-33bd-a1b2-9bce0255e5d9 | -17.652901 | -57.5644 | 2024-11-28 00:38:00 | METOP-B | POCONÉ | MATO GROSSO | Brasil | 5106505 | 51 | 33 | nan | nan | nan | Pantanal | nan |
| e532b639-3331-3414-ae31-c10270b142cd | -3.043 | -50.975201 | 2024-11-28 00:38:00 | METOP-B | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| b4f31a1c-21f2-3eb4-970e-0e4ebc1aa98c | -2.5351 | -47.330101 | 2024-11-28 00:38:00 | METOP-B | CAPITÃO POÇO | PARÁ | Brasil | 1502301 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| 70723676-444e-3951-8315-9d21c1762557 | -3.4457 | -54.538799 | 2024-11-28 00:38:00 | METOP-B | PLACAS | PARÁ | Brasil | 1505650 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| 23282a0e-e117-3ab4-9cde-9a271d20f9d2 | -2.5417 | -53.998402 | 2024-11-28 00:38:00 | METOP-B | PRAINHA | PARÁ | Brasil | 1506005 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| 47b686f5-b7fa-3c2f-a790-2a1c3727976d | -2.6367 | -51.772202 | 2024-11-28 00:38:00 | METOP-B | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| b7b34378-ebdb-393e-8e1e-6b28b80daee3 | -4.6808 | -44.626499 | 2024-11-28 00:38:00 | METOP-B | BERNARDO DO MEARIM | MARANHÃO | Brasil | 2101939 | 21 | 33 | nan | nan | nan | Cerrado | nan |
| 01147db6-8f1a-3af8-95dd-270a2b2c17f1 | -3.0534 | -48.5042 | 2024-11-28 00:38:00 | METOP-B | TOMÉ-AÇU | PARÁ | Brasil | 1508001 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| da158237-f99c-382c-81cc-cff3cda1658b | -3.3285 | -53.694801 | 2024-11-28 00:38:00 | METOP-B | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| 47bdc0a0-ba97-30a7-a924-e27eaffa5c1f | -3.119 | -54.965099 | 2024-11-28 00:38:00 | METOP-B | BELTERRA | PARÁ | Brasil | 1501451 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| 3cd7cc6f-120e-313d-ad96-6aac3ae9b5ca | -2.6176 | -54.0611 | 2024-11-28 00:38:00 | METOP-B | PRAINHA | PARÁ | Brasil | 1506005 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| 874f1207-51c8-3ea5-9a21-45d018ce77d6 | -18.787701 | -55.8111 | 2024-11-28 00:38:00 | METOP-B | CORUMBÁ | MATO GROSSO DO SUL | Brasil | 5003207 | 50 | 33 | nan | nan | nan | Pantanal | nan |
| 46e46f14-a91d-3d80-89a9-700ce67cb691 | -3.5097 | -53.8134 | 2024-11-28 00:38:00 | METOP-B | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| b382aa1c-d468-34f2-9479-f0dd216bb59a | -3.3882 | -50.094898 | 2024-11-28 00:38:00 | METOP-B | PACAJÁ | PARÁ | Brasil | 1505486 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| 0170db40-b3dd-3649-bae7-fd2e399152d1 | -3.2792 | -50.6101 | 2024-11-28 00:38:00 | METOP-B | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| 818633bf-5f83-34ca-951d-2e1ef39f93ad | -2.4788 | -47.0434 | 2024-11-28 00:38:00 | METOP-B | NOVA ESPERANÇA DO PIRIÁ | PARÁ | Brasil | 1504950 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| 0c1bf6b1-c7f2-3ce9-9d07-762b0b98dada | -1.4486 | -47.116501 | 2024-11-28 00:38:00 | METOP-B | OURÉM | PARÁ | Brasil | 1505403 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| df2ec08d-a781-3cf3-966d-c49c5540f047 | -3.4307 | -53.874298 | 2024-11-28 00:38:00 | METOP-B | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| b0c846c8-cfa7-3a8d-854a-ee0782622920 | -3.9292 | -53.662899 | 2024-11-28 00:38:00 | METOP-B | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| 19fd5c0c-f49a-3877-84c5-f1b0ee4d4936 | -3.1176 | -53.261101 | 2024-11-28 00:38:00 | METOP-B | MEDICILÂNDIA | PARÁ | Brasil | 1504455 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| 4af18c4a-8bcb-3ad6-a1a2-4f6cb3aaa53e | -3.0521 | -54.023102 | 2024-11-28 00:38:00 | METOP-B | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| e572dbcc-7916-30a0-915d-4060fd353787 | -4.4775 | -46.362801 | 2024-11-28 00:38:00 | METOP-B | BURITICUPU | MARANHÃO | Brasil | 2102325 | 21 | 33 | nan | nan | nan | Amazônia | nan |
| a2af8a53-f62c-3678-8422-b9ef9633d396 | -3.1255 | -53.754101 | 2024-11-28 00:38:00 | METOP-B | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| ffd7a179-b991-32a9-8664-0feae80570bc | -3.5792 | -53.0229 | 2024-11-28 00:38:00 | METOP-B | MEDICILÂNDIA | PARÁ | Brasil | 1504455 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| 86155d6c-9fc6-3ad0-8de0-9a33b8ccfb18 | -21.017 | -47.633099 | 2024-11-28 00:38:00 | METOP-B | BRODOWSKI | SÃO PAULO | Brasil | 3507803 | 35 | 33 | nan | nan | nan | Cerrado | nan |
| c1ec30ae-993c-3f0d-a533-ee43805d5bc5 | -2.8444 | -54.061699 | 2024-11-28 00:38:00 | METOP-B | PRAINHA | PARÁ | Brasil | 1506005 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| 9180e1f7-ff9a-335f-bc86-63ce7594fa2d | -1.54 | -46.8451 | 2024-11-28 00:38:00 | METOP-B | BRAGANÇA | PARÁ | Brasil | 1501709 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| 310c3d70-8970-393c-939c-a29fc44fcea5 | -2.6671 | -49.510502 | 2024-11-28 00:38:00 | METOP-B | BAIÃO | PARÁ | Brasil | 1501204 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| 06b923d3-769d-3dcb-80b7-7552264160b5 | -2.9199 | -54.168598 | 2024-11-28 00:38:00 | METOP-B | SANTARÉM | PARÁ | Brasil | 1506807 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| 9d19ae36-4b1c-311f-9b3c-93e965671f7a | -2.9392 | -49.439701 | 2024-11-28 00:38:00 | METOP-B | MOJU | PARÁ | Brasil | 1504703 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| 51383d3f-32b4-337c-8f4e-afff3ac2cdcd | -3.248 | -50.202999 | 2024-11-28 00:38:00 | METOP-B | PACAJÁ | PARÁ | Brasil | 1505486 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| 6f6cd1a2-4b16-3fb2-b586-3f633a122e41 | -3.8193 | -52.352001 | 2024-11-28 00:38:00 | METOP-B | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| f81bac3b-9a40-30fd-9311-591d4f81e7d2 | -2.8367 | -54.027199 | 2024-11-28 00:38:00 | METOP-B | PRAINHA | PARÁ | Brasil | 1506005 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| 97e74631-6f07-3516-9b8a-d0ac9e6aa5a0 | -3.1954 | -46.5919 | 2024-11-28 00:38:00 | METOP-B | CENTRO NOVO DO MARANHÃO | MARANHÃO | Brasil | 2103174 | 21 | 33 | nan | nan | nan | Amazônia | nan |
| aeca4ce0-6102-33b0-bf34-225f5c7d1eb8 | -3.1314 | -53.093601 | 2024-11-28 00:38:00 | METOP-B | MEDICILÂNDIA | PARÁ | Brasil | 1504455 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| 55d4ca7f-4006-38c2-b589-94515b393bda | -3.5929 | -50.3592 | 2024-11-28 00:38:00 | METOP-B | PACAJÁ | PARÁ | Brasil | 1505486 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| 9d07cd8d-3152-35b6-aeef-ad9ddc08a829 | -3.5706 | -51.028999 | 2024-11-28 00:38:00 | METOP-B | PACAJÁ | PARÁ | Brasil | 1505486 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| d4725084-ca30-3819-962b-c86e6687b636 | -2.6132 | -51.941399 | 2024-11-28 00:38:00 | METOP-B | SENADOR JOSÉ PORFÍRIO | PARÁ | Brasil | 1507805 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| de79b7f2-4a07-3c44-a583-8356aa3d8fe8 | -2.1538 | -48.708599 | 2024-11-28 00:38:00 | METOP-B | MOJU | PARÁ | Brasil | 1504703 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| cd685ca3-dd0c-3396-941e-01c614598797 | -3.4392 | -51.674999 | 2024-11-28 00:38:00 | METOP-B | ANAPU | PARÁ | Brasil | 1500859 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| 4910168e-cabe-3549-b61d-74c6a3dc9fd0 | -3.8757 | -52.100201 | 2024-11-28 00:38:00 | METOP-B | SENADOR JOSÉ PORFÍRIO | PARÁ | Brasil | 1507805 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| d4d740f2-4490-3921-9246-842e915f1e28 | -2.8057 | -54.026798 | 2024-11-28 00:38:00 | METOP-B | PRAINHA | PARÁ | Brasil | 1506005 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| ef576f25-e6e0-39c4-b3a0-de4d932653c1 | -2.8549 | -46.8494 | 2024-11-28 00:38:00 | METOP-B | PARAGOMINAS | PARÁ | Brasil | 1505502 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| 686eb78e-4002-3be0-a4ea-c46af8c60493 | -3.7052 | -43.4203 | 2024-11-28 00:38:00 | METOP-B | CHAPADINHA | MARANHÃO | Brasil | 2103208 | 21 | 33 | nan | nan | nan | Cerrado | nan |
| 41adde96-6fa0-3afe-a184-922ec412789c | -2.8706 | -46.872898 | 2024-11-28 00:38:00 | METOP-B | PARAGOMINAS | PARÁ | Brasil | 1505502 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| 1b5900d0-da25-32c4-b4ff-d5f049559095 | -8.573 | -49.192299 | 2024-11-28 00:38:00 | METOP-B | COUTO MAGALHÃES | TOCANTINS | Brasil | 1706001 | 17 | 33 | nan | nan | nan | Cerrado | nan |
| 86aa99ed-c1d2-3e0d-9406-deb6de68839e | -3.6118 | -52.528 | 2024-11-28 00:38:00 | METOP-B | BRASIL NOVO | PARÁ | Brasil | 1501725 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| ce7679aa-713e-3266-bd1b-f09fb77a1e4a | -2.923 | -54.182499 | 2024-11-28 00:38:00 | METOP-B | SANTARÉM | PARÁ | Brasil | 1506807 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| 19155590-9cec-333f-bab7-49461464b2ef | -3.2466 | -51.5532 | 2024-11-28 00:38:00 | METOP-B | ANAPU | PARÁ | Brasil | 1500859 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| f96eed1e-1ab5-3ff1-b8bb-550eb1800b7f | -3.0392 | -54.011501 | 2024-11-28 00:38:00 | METOP-B | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| e2ca7445-20c9-36f3-bb42-071201c9a8bd | -3.2997 | -53.657902 | 2024-11-28 00:38:00 | METOP-B | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| bb4bc57f-b7b2-3814-b3c5-e20d5393d2d1 | -2.8878 | -53.979698 | 2024-11-28 00:38:00 | METOP-B | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| b6bae893-771d-3445-b395-fc92a5b28ccc | -3.3901 | -51.231998 | 2024-11-28 00:38:00 | METOP-B | ANAPU | PARÁ | Brasil | 1500859 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| 2065a3ce-02e7-3bd6-911b-0374ab7662dd | -3.3224 | -50.0326 | 2024-11-28 00:38:00 | METOP-B | PACAJÁ | PARÁ | Brasil | 1505486 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| 5639b342-a695-3fdd-8cc1-0a8fe1f2891b | -2.3273 | -51.953098 | 2024-11-28 00:38:00 | METOP-B | PORTO DE MOZ | PARÁ | Brasil | 1505908 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| 816d4648-00d8-3944-8104-0e78d518f4e6 | -3.1231 | -53.1026 | 2024-11-28 00:38:00 | METOP-B | MEDICILÂNDIA | PARÁ | Brasil | 1504455 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| a268f1bc-63b9-3602-89ba-5927dce76ccb | -4.2194 | -50.8908 | 2024-11-28 00:38:00 | METOP-B | PACAJÁ | PARÁ | Brasil | 1505486 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| 8c020d96-6b86-3dea-a1d1-bc44cf659380 | -4.2292 | -50.888599 | 2024-11-28 00:38:00 | METOP-B | PACAJÁ | PARÁ | Brasil | 1505486 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| 45b97e43-baf4-38da-b472-afc08c32424b | -2.1561 | -48.718601 | 2024-11-28 00:38:00 | METOP-B | MOJU | PARÁ | Brasil | 1504703 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| e3250c5f-9ca9-3716-9f0e-4099750e8cf0 | -3.8209 | -52.358898 | 2024-11-28 00:38:00 | METOP-B | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| c2f98c2c-7584-3c1d-8e39-64763e9e6328 | -2.5886 | -53.657398 | 2024-11-28 00:38:00 | METOP-B | PRAINHA | PARÁ | Brasil | 1506005 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| 3364aeb7-e4eb-3575-bc1b-a7433c9a1c92 | -3.6357 | -51.496201 | 2024-11-28 00:38:00 | METOP-B | ANAPU | PARÁ | Brasil | 1500859 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| ff91ae2d-f760-3d38-b941-d2e4080f4187 | -4.7652 | -44.422501 | 2024-11-28 00:38:00 | METOP-B | SANTO ANTÔNIO DOS LOPES | MARANHÃO | Brasil | 2110302 | 21 | 33 | nan | nan | nan | Cerrado | nan |
| e93e82a4-6c8f-3ba6-a586-6f492426f837 | -2.5872 | -51.9175 | 2024-11-28 00:38:00 | METOP-B | SENADOR JOSÉ PORFÍRIO | PARÁ | Brasil | 1507805 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| e552517d-d527-3f74-81fc-e3016d88370e | -2.5975 | -53.971699 | 2024-11-28 00:38:00 | METOP-B | PRAINHA | PARÁ | Brasil | 1506005 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| d421d6b0-ac26-3c50-b05d-0d4da391f051 | -6.1244 | -46.582802 | 2024-11-28 00:38:00 | METOP-B | SÍTIO NOVO | MARANHÃO | Brasil | 2111805 | 21 | 33 | nan | nan | nan | Cerrado | nan |
| d1633e7f-db39-30d1-8f07-9233bc203d26 | -2.8542 | -54.059502 | 2024-11-28 00:38:00 | METOP-B | PRAINHA | PARÁ | Brasil | 1506005 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| 9147c43b-c235-3429-9e92-7b28c5049dfc | -2.4283 | -53.8148 | 2024-11-28 00:38:00 | METOP-B | PRAINHA | PARÁ | Brasil | 1506005 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| 750aabee-1a52-31b8-a9e1-d2021f27e6b3 | -3.1329 | -53.100399 | 2024-11-28 00:38:00 | METOP-B | MEDICILÂNDIA | PARÁ | Brasil | 1504455 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| 24e513c4-df67-39b5-ac7c-dae80168fb7d | -3.3338 | -50.2174 | 2024-11-28 00:38:00 | METOP-B | PACAJÁ | PARÁ | Brasil | 1505486 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| 5fbea427-8a02-3a52-b1e6-c5237e3ca185 | -5.7576 | -46.252102 | 2024-11-28 00:38:00 | METOP-B | GRAJAÚ | MARANHÃO | Brasil | 2104800 | 21 | 33 | nan | nan | nan | Cerrado | nan |
| 020cc2cf-9d99-3081-99e8-85317eebcc68 | -17.854601 | -45.996799 | 2024-11-28 00:38:00 | METOP-B | JOÃO PINHEIRO | MINAS GERAIS | Brasil | 3136306 | 31 | 33 | nan | nan | nan | Cerrado | nan |


[Clique aqui para ver as próximas entradas](README12.md)
