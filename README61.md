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

## Dados Diários - Página 61

| ID | Latitude | Longitude | Data/Hora GMT | Satélite | Município | Estado | País | Município ID | Estado ID | País ID | Dias sem Chuva | Precipitação | Risco de Fogo | Bioma | FRP |
|----|----------|-----------|---------------|----------|-----------|--------|------|--------------|-----------|---------|----------------|--------------|----------------|-------|-----|
| 1f10de18-aa20-3417-a01d-8f5b76a1731d | -6.39117 | -43.39253 | 2025-10-04 04:12:00 | NOAA-20 | SUCUPIRA DO RIACHÃO | MARANHÃO | Brasil | 2111953 | 21 | 33 | nan | nan | nan | Cerrado | 1.2 |
| 0fed8540-f4f6-3655-b018-79f5feeccb85 | -6.45691 | -44.57332 | 2025-10-04 04:12:00 | NOAA-20 | MIRADOR | MARANHÃO | Brasil | 2106706 | 21 | 33 | nan | nan | nan | Cerrado | 7.2 |
| 8f58881b-d6f2-3dc0-bc67-adcabc3cd6ec | -5.93809 | -42.88495 | 2025-10-04 04:12:00 | NOAA-20 | PALMEIRAIS | PIAUÍ | Brasil | 2207504 | 22 | 33 | nan | nan | nan | Caatinga | 3.2 |
| 641b7c99-ae8d-32f4-8c2c-b529d9a68029 | -5.7161 | -42.63451 | 2025-10-04 04:12:00 | NOAA-20 | MIGUEL LEÃO | PIAUÍ | Brasil | 2206308 | 22 | 33 | nan | nan | nan | Caatinga | 1.6 |
| 2e31c941-5d46-3598-9448-5a0b61799fdf | -6.07135 | -42.51296 | 2025-10-04 04:12:00 | NOAA-20 | JARDIM DO MULATO | PIAUÍ | Brasil | 2205250 | 22 | 33 | nan | nan | nan | Caatinga | 26.9 |
| a05e08aa-f8c0-33ab-b585-a2792db3b8eb | -5.74717 | -42.93291 | 2025-10-04 04:12:00 | NOAA-20 | PALMEIRAIS | PIAUÍ | Brasil | 2207504 | 22 | 33 | nan | nan | nan | Caatinga | 1.6 |
| 859e5e9c-8f6c-30ca-a77a-9ad55443d75a | -7.79214 | -42.56226 | 2025-10-04 04:12:00 | NOAA-20 | SOCORRO DO PIAUÍ | PIAUÍ | Brasil | 2210904 | 22 | 33 | nan | nan | nan | Caatinga | 1.3 |
| 7f9c7fad-1540-390c-a134-f4d467d8a944 | -7.75438 | -42.52044 | 2025-10-04 04:12:00 | NOAA-20 | SÃO JOSÉ DO PEIXE | PIAUÍ | Brasil | 2210102 | 22 | 33 | nan | nan | nan | Caatinga | 9.5 |
| cf137499-d6c3-35e9-84da-64b3ad33254e | -3.84531 | -41.57101 | 2025-10-04 04:12:00 | NOAA-20 | PIRACURUCA | PIAUÍ | Brasil | 2208304 | 22 | 33 | nan | nan | nan | Caatinga | 9.5 |
| 7da70c4f-0603-395a-95f7-97c0885c1c37 | -5.25395 | -42.63592 | 2025-10-04 04:12:00 | NOAA-20 | DEMERVAL LOBÃO | PIAUÍ | Brasil | 2203305 | 22 | 33 | nan | nan | nan | Cerrado | 1.9 |
| df12068d-eaa1-3df1-8068-04e60b3cf04c | -7.54152 | -42.40419 | 2025-10-04 04:12:00 | NOAA-20 | SÃO MIGUEL DO FIDALGO | PIAUÍ | Brasil | 2210391 | 22 | 33 | nan | nan | nan | Caatinga | 3.5 |
| 7578ab06-d069-3a39-8995-30c8fa7fe098 | -5.93219 | -43.30902 | 2025-10-04 04:12:00 | NOAA-20 | SÃO FRANCISCO DO MARANHÃO | MARANHÃO | Brasil | 2110906 | 21 | 33 | nan | nan | nan | Cerrado | 0.7 |
| 7f5ce260-cebc-3b8f-8d95-04cb6c4cb0af | -5.82366 | -42.87776 | 2025-10-04 04:12:00 | NOAA-20 | PALMEIRAIS | PIAUÍ | Brasil | 2207504 | 22 | 33 | nan | nan | nan | Caatinga | 2.7 |
| 7fb24fe3-d06d-3285-b4bb-dccbf0c01eca | -6.04146 | -44.18291 | 2025-10-04 04:12:00 | NOAA-20 | COLINAS | MARANHÃO | Brasil | 2103505 | 21 | 33 | nan | nan | nan | Cerrado | 1.3 |
| daf3e557-1b6f-36d2-96a0-14c3fc9be273 | -3.83656 | -44.55074 | 2025-10-04 04:12:00 | NOAA-20 | MATÕES DO NORTE | MARANHÃO | Brasil | 2106631 | 21 | 33 | nan | nan | nan | Cerrado | 2.0 |
| a13ae621-3c14-374c-ac02-329b791ce1ac | -7.48667 | -43.03808 | 2025-10-04 04:12:00 | NOAA-20 | ITAUEIRA | PIAUÍ | Brasil | 2205102 | 22 | 33 | nan | nan | nan | Caatinga | 0.9 |
| 8533887c-92c7-3257-86db-bfc6c86a91cf | -4.38669 | -41.92926 | 2025-10-04 04:12:00 | NOAA-20 | PIRIPIRI | PIAUÍ | Brasil | 2208403 | 22 | 33 | nan | nan | nan | Caatinga | 1.3 |
| f3604776-cde8-3e75-bed5-5743df472556 | -7.04994 | -42.77017 | 2025-10-04 04:12:00 | NOAA-20 | NAZARÉ DO PIAUÍ | PIAUÍ | Brasil | 2206704 | 22 | 33 | nan | nan | nan | Caatinga | 1.3 |
| d6bcbedd-2308-351a-a910-c43b8ad6ea5e | -5.45906 | -44.14588 | 2025-10-04 04:12:00 | NOAA-20 | GOVERNADOR LUIZ ROCHA | MARANHÃO | Brasil | 2104628 | 21 | 33 | nan | nan | nan | Cerrado | 2.3 |
| 959ae2fc-b85b-34b4-9b19-82e5cfb64f1e | -5.2578 | -42.633 | 2025-10-04 04:12:00 | NOAA-20 | DEMERVAL LOBÃO | PIAUÍ | Brasil | 2203305 | 22 | 33 | nan | nan | nan | Cerrado | 2.0 |
| 3db43045-637c-3eca-ac42-60963dfda41a | -5.68516 | -42.85237 | 2025-10-04 04:12:00 | NOAA-20 | CURRALINHOS | PIAUÍ | Brasil | 2203255 | 22 | 33 | nan | nan | nan | Caatinga | 3.6 |
| be4efb2d-8d5e-389f-8447-2c9a005ab255 | -6.28959 | -43.647 | 2025-10-04 04:12:00 | NOAA-20 | PASSAGEM FRANCA | MARANHÃO | Brasil | 2107902 | 21 | 33 | nan | nan | nan | Cerrado | 1.6 |
| 2d148abe-7253-3888-869d-c4aa286a4f5c | -5.7165 | -44.24138 | 2025-10-04 04:12:00 | NOAA-20 | SÃO DOMINGOS DO MARANHÃO | MARANHÃO | Brasil | 2110708 | 21 | 33 | nan | nan | nan | Cerrado | 6.2 |
| 729fcfe9-6e5e-3799-9b76-ba19434145be | -6.37138 | -44.30075 | 2025-10-04 04:12:00 | NOAA-20 | MIRADOR | MARANHÃO | Brasil | 2106706 | 21 | 33 | nan | nan | nan | Cerrado | 2.8 |
| f3ed8c2c-a84d-3f4f-bb51-bf3fd235374a | -5.69341 | -42.84306 | 2025-10-04 04:12:00 | NOAA-20 | SÃO PEDRO DO PIAUÍ | PIAUÍ | Brasil | 2210508 | 22 | 33 | nan | nan | nan | Caatinga | 1.7 |
| e219f458-2b14-3701-a783-717f052a1296 | -7.51176 | -44.27119 | 2025-10-04 04:12:00 | NOAA-20 | URUÇUÍ | PIAUÍ | Brasil | 2211209 | 22 | 33 | nan | nan | nan | Cerrado | 1.3 |
| 33deb858-7a7f-3dd7-b691-1d756b13c491 | -6.65022 | -42.80653 | 2025-10-04 04:12:00 | NOAA-20 | FRANCISCO AYRES | PIAUÍ | Brasil | 2204105 | 22 | 33 | nan | nan | nan | Caatinga | 1.9 |
| 9dbe2f2a-b9c7-350a-bb07-125318ed5e3b | -6.37863 | -46.51324 | 2025-10-04 04:12:00 | NOAA-20 | SÍTIO NOVO | MARANHÃO | Brasil | 2111805 | 21 | 33 | nan | nan | nan | Cerrado | 2.7 |
| 0956e759-d84a-3fc3-a8b8-52cf405ead1d | -5.96041 | -43.49534 | 2025-10-04 04:12:00 | NOAA-20 | LAGOA DO MATO | MARANHÃO | Brasil | 2105922 | 21 | 33 | nan | nan | nan | Cerrado | 1.7 |
| 8011e5f2-a99a-39eb-af18-b84fc84a17a0 | -6.67087 | -46.1488 | 2025-10-04 04:12:00 | NOAA-20 | FORMOSA DA SERRA NEGRA | MARANHÃO | Brasil | 2104099 | 21 | 33 | nan | nan | nan | Cerrado | 0.9 |
| cf791382-4d0c-37e5-9662-0eeaeb02d643 | -6.87701 | -45.46355 | 2025-10-04 04:12:00 | NOAA-20 | SÃO RAIMUNDO DAS MANGABEIRAS | MARANHÃO | Brasil | 2111607 | 21 | 33 | nan | nan | nan | Cerrado | 3.1 |
| 4e7eaa9c-c06d-379c-9a69-5b804fc27ff8 | -6.17952 | -46.31158 | 2025-10-04 04:12:00 | NOAA-20 | GRAJAÚ | MARANHÃO | Brasil | 2104800 | 21 | 33 | nan | nan | nan | Cerrado | 0.9 |
| 1caca873-20bc-35d9-9fa9-9fce50a7d0f8 | -5.97775 | -44.15073 | 2025-10-04 04:12:00 | NOAA-20 | COLINAS | MARANHÃO | Brasil | 2103505 | 21 | 33 | nan | nan | nan | Cerrado | 2.4 |
| b3a435c2-2137-39cd-958a-b78bee13e49b | -5.84718 | -42.79306 | 2025-10-04 04:12:00 | NOAA-20 | SÃO PEDRO DO PIAUÍ | PIAUÍ | Brasil | 2210508 | 22 | 33 | nan | nan | nan | Caatinga | 2.1 |
| ef7c2be9-4017-3902-8d38-da582993d8f6 | -6.72042 | -42.16145 | 2025-10-04 04:12:00 | NOAA-20 | TANQUE DO PIAUÍ | PIAUÍ | Brasil | 2210979 | 22 | 33 | nan | nan | nan | Caatinga | 1.9 |
| b5178440-837b-3ab9-bda5-b429eb270d73 | -6.0675 | -42.5159 | 2025-10-04 04:12:00 | NOAA-20 | JARDIM DO MULATO | PIAUÍ | Brasil | 2205250 | 22 | 33 | nan | nan | nan | Caatinga | 2.2 |
| 5fc8632e-3096-3603-940a-60a0874cbb71 | -3.49551 | -50.27 | 2025-10-04 04:12:00 | NOAA-20 | PACAJÁ | PARÁ | Brasil | 1505486 | 15 | 33 | nan | nan | nan | Amazônia | 1.9 |
| 07faa01f-a940-3590-a88b-5ce679ae4b1d | -6.19975 | -44.64099 | 2025-10-04 04:12:00 | NOAA-20 | MIRADOR | MARANHÃO | Brasil | 2106706 | 21 | 33 | nan | nan | nan | Cerrado | 9.3 |
| c145e574-d3a5-32fc-91ae-e9029dd5a4ed | -5.67113 | -42.72642 | 2025-10-04 04:12:00 | NOAA-20 | MIGUEL LEÃO | PIAUÍ | Brasil | 2206308 | 22 | 33 | nan | nan | nan | Caatinga | 3.4 |
| 00a78ff8-8f9a-3395-8645-c3eba308cb76 | -5.4588 | -43.16656 | 2025-10-04 04:12:00 | NOAA-20 | MATÕES | MARANHÃO | Brasil | 2106607 | 21 | 33 | nan | nan | nan | Cerrado | 15.3 |
| 2e478760-0ac6-36da-aa2c-ebe914240dd4 | -7.71834 | -42.57938 | 2025-10-04 04:12:00 | NOAA-20 | SOCORRO DO PIAUÍ | PIAUÍ | Brasil | 2210904 | 22 | 33 | nan | nan | nan | Caatinga | 0.8 |
| b1ad3a46-f564-3855-92a8-2d1dfd3744f8 | -4.44925 | -43.2555 | 2025-10-04 04:12:00 | NOAA-20 | ALDEIAS ALTAS | MARANHÃO | Brasil | 2100303 | 21 | 33 | nan | nan | nan | Cerrado | 1.0 |
| fbde3b28-1062-311f-80b9-8519ae601ea1 | -7.06016 | -43.22232 | 2025-10-04 04:12:00 | NOAA-20 | FLORIANO | PIAUÍ | Brasil | 2203909 | 22 | 33 | nan | nan | nan | Caatinga | 2.2 |
| 5d408f51-c7ed-329a-bf43-5c9d73d75e9d | -6.65574 | -42.81448 | 2025-10-04 04:12:00 | NOAA-20 | FRANCISCO AYRES | PIAUÍ | Brasil | 2204105 | 22 | 33 | nan | nan | nan | Caatinga | 3.4 |
| 7ce738dd-eac0-3551-8793-bedda1189cf7 | -5.69099 | -43.03011 | 2025-10-04 04:12:00 | NOAA-20 | PALMEIRAIS | PIAUÍ | Brasil | 2207504 | 22 | 33 | nan | nan | nan | Caatinga | 1.3 |
| abab59d3-daa5-3481-a65e-77919f897d46 | -7.71392 | -42.58584 | 2025-10-04 04:12:00 | NOAA-20 | SOCORRO DO PIAUÍ | PIAUÍ | Brasil | 2210904 | 22 | 33 | nan | nan | nan | Caatinga | 0.6 |
| 72d4358a-a464-3e35-beca-1d2f489052d8 | -6.24629 | -44.24038 | 2025-10-04 04:12:00 | NOAA-20 | MIRADOR | MARANHÃO | Brasil | 2106706 | 21 | 33 | nan | nan | nan | Cerrado | 2.3 |
| 99536eb9-8516-3988-9381-1e62d8cae087 | -5.97687 | -44.0921 | 2025-10-04 04:12:00 | NOAA-20 | COLINAS | MARANHÃO | Brasil | 2103505 | 21 | 33 | nan | nan | nan | Cerrado | 1.5 |
| 3b368438-4c61-38d6-83a2-118eda156057 | -4.43207 | -43.23498 | 2025-10-04 04:12:00 | NOAA-20 | ALDEIAS ALTAS | MARANHÃO | Brasil | 2100303 | 21 | 33 | nan | nan | nan | Cerrado | 1.6 |
| b6c7ca6c-88cf-38fa-a237-fe2dacdca7af | -6.18573 | -43.59552 | 2025-10-04 04:12:00 | NOAA-20 | PASSAGEM FRANCA | MARANHÃO | Brasil | 2107902 | 21 | 33 | nan | nan | nan | Cerrado | 3.0 |
| d1c3fa7c-f67c-3d5c-bba3-422050da33eb | -6.37211 | -43.89741 | 2025-10-04 04:12:00 | NOAA-20 | PARAIBANO | MARANHÃO | Brasil | 2107704 | 21 | 33 | nan | nan | nan | Cerrado | 1.6 |
| 8fea3bef-4163-3b45-a130-cb82c7428a85 | -6.87556 | -47.24009 | 2025-10-04 04:12:00 | NOAA-20 | ESTREITO | MARANHÃO | Brasil | 2104057 | 21 | 33 | nan | nan | nan | Cerrado | 23.9 |
| ab1716a1-7d52-35c7-adaf-44233d130045 | -6.29125 | -43.63654 | 2025-10-04 04:12:00 | NOAA-20 | PASSAGEM FRANCA | MARANHÃO | Brasil | 2107902 | 21 | 33 | nan | nan | nan | Cerrado | 1.4 |
| 225d94ef-b56d-3286-b5e7-2e42f86ee8d5 | -5.84386 | -42.88074 | 2025-10-04 04:12:00 | NOAA-20 | PALMEIRAIS | PIAUÍ | Brasil | 2207504 | 22 | 33 | nan | nan | nan | Caatinga | 1.0 |
| 41648361-31a6-346a-813c-cdd8c7c25bcd | -6.61104 | -44.2917 | 2025-10-04 04:12:00 | NOAA-20 | PASTOS BONS | MARANHÃO | Brasil | 2108009 | 21 | 33 | nan | nan | nan | Cerrado | 2.7 |
| 645ba7b5-bef7-319a-a618-1793e88850db | -6.10731 | -43.42589 | 2025-10-04 04:12:00 | NOAA-20 | LAGOA DO MATO | MARANHÃO | Brasil | 2105922 | 21 | 33 | nan | nan | nan | Cerrado | 1.6 |
| 8c8aa8e8-74d3-3be7-a2f1-4933b0a79e5c | -7.46638 | -46.85205 | 2025-10-04 04:12:00 | NOAA-20 | RIACHÃO | MARANHÃO | Brasil | 2109502 | 21 | 33 | nan | nan | nan | Cerrado | 7.3 |
| f506f03c-4be8-3edc-8f65-5c073daec6ac | -4.44204 | -43.23654 | 2025-10-04 04:12:00 | NOAA-20 | ALDEIAS ALTAS | MARANHÃO | Brasil | 2100303 | 21 | 33 | nan | nan | nan | Cerrado | 3.0 |
| 024ee091-46f3-35dd-8f4c-a950d0e236b3 | -7.29987 | -44.19352 | 2025-10-04 04:12:00 | NOAA-20 | ANTÔNIO ALMEIDA | PIAUÍ | Brasil | 2200806 | 22 | 33 | nan | nan | nan | Cerrado | 2.0 |
| c8089d91-8a70-370c-8bd7-fea11c9b5fbe | -3.393 | -50.26859 | 2025-10-04 04:12:00 | NOAA-20 | PACAJÁ | PARÁ | Brasil | 1505486 | 15 | 33 | nan | nan | nan | Amazônia | 1.3 |
| 7f89661d-ff9d-3830-878c-0110e132f0c3 | -5.78949 | -45.77951 | 2025-10-04 04:12:00 | NOAA-20 | GRAJAÚ | MARANHÃO | Brasil | 2104800 | 21 | 33 | nan | nan | nan | Cerrado | 2.5 |
| 73bd26e1-46b8-31bc-8352-75ac4f6cbe50 | -7.79437 | -42.56977 | 2025-10-04 04:12:00 | NOAA-20 | SOCORRO DO PIAUÍ | PIAUÍ | Brasil | 2210904 | 22 | 33 | nan | nan | nan | Caatinga | 2.5 |
| 8875bffd-c420-3a2a-84c9-c51f97dc81a0 | -7.54873 | -42.40171 | 2025-10-04 04:12:00 | NOAA-20 | SÃO MIGUEL DO FIDALGO | PIAUÍ | Brasil | 2210391 | 22 | 33 | nan | nan | nan | Caatinga | 3.5 |
| 0de4e9b3-1f03-375e-8c5c-3ff03ed411b6 | -4.64845 | -47.54777 | 2025-10-04 04:12:00 | NOAA-20 | ITINGA DO MARANHÃO | MARANHÃO | Brasil | 2105427 | 21 | 33 | nan | nan | nan | Amazônia | 0.7 |
| fea50784-5521-33b3-9f60-3d78ecbc3427 | -5.26275 | -43.16014 | 2025-10-04 04:12:00 | NOAA-20 | TIMON | MARANHÃO | Brasil | 2112209 | 21 | 33 | nan | nan | nan | Cerrado | 1.8 |
| 8b393abc-1ce0-302d-8498-2ad683caa630 | -5.23593 | -45.5498 | 2025-10-04 04:12:00 | NOAA-20 | JENIPAPO DOS VIEIRAS | MARANHÃO | Brasil | 2105476 | 21 | 33 | nan | nan | nan | Cerrado | 0.9 |
| 12eabba8-2b10-39f7-9376-52ba0461e483 | -5.72835 | -42.68589 | 2025-10-04 04:12:00 | NOAA-20 | MIGUEL LEÃO | PIAUÍ | Brasil | 2206308 | 22 | 33 | nan | nan | nan | Caatinga | 7.6 |
| 2f7f3e49-1159-3f3d-b607-b9024d861321 | -6.35092 | -43.45369 | 2025-10-04 04:12:00 | NOAA-20 | SUCUPIRA DO RIACHÃO | MARANHÃO | Brasil | 2111953 | 21 | 33 | nan | nan | nan | Cerrado | 1.9 |
| b36f1abc-8056-3e20-b8a0-6ad36f383023 | -5.40873 | -41.32404 | 2025-10-04 04:12:00 | NOAA-20 | CASTELO DO PIAUÍ | PIAUÍ | Brasil | 2202604 | 22 | 33 | nan | nan | nan | Caatinga | 1.9 |
| c8a57861-534a-360a-b95b-d311394dd2a8 | -4.44371 | -43.24749 | 2025-10-04 04:12:00 | NOAA-20 | ALDEIAS ALTAS | MARANHÃO | Brasil | 2100303 | 21 | 33 | nan | nan | nan | Cerrado | 30.3 |
| c88e6b03-68ae-32b5-a0a8-46875b7713df | -4.43984 | -43.25045 | 2025-10-04 04:12:00 | NOAA-20 | ALDEIAS ALTAS | MARANHÃO | Brasil | 2100303 | 21 | 33 | nan | nan | nan | Cerrado | 2.2 |
| 83359c37-6a66-3493-b67a-c93f673db5f6 | -6.29698 | -42.43863 | 2025-10-04 04:12:00 | NOAA-20 | REGENERAÇÃO | PIAUÍ | Brasil | 2208809 | 22 | 33 | nan | nan | nan | Caatinga | 2.0 |
| 97111044-6a03-3a11-9aa4-4feea7a90570 | -7.74186 | -42.60096 | 2025-10-04 04:12:00 | NOAA-20 | RIBEIRA DO PIAUÍ | PIAUÍ | Brasil | 2208874 | 22 | 33 | nan | nan | nan | Caatinga | 2.2 |
| e9436510-b954-34c2-abc9-7696d6767d0e | -5.26869 | -46.1762 | 2025-10-04 04:12:00 | NOAA-20 | ARAME | MARANHÃO | Brasil | 2100956 | 21 | 33 | nan | nan | nan | Amazônia | 1.8 |
| 845012ff-0c36-317b-96f3-a93be80802d4 | -6.2699 | -43.10794 | 2025-10-04 04:12:00 | NOAA-20 | SÃO FRANCISCO DO MARANHÃO | MARANHÃO | Brasil | 2110906 | 21 | 33 | nan | nan | nan | Cerrado | 1.8 |
| 88f4e485-7bdf-3baf-983a-af881acc6cad | -1.13242 | -47.80827 | 2025-10-04 04:12:00 | NOAA-20 | SÃO FRANCISCO DO PARÁ | PARÁ | Brasil | 1507409 | 15 | 33 | nan | nan | nan | Amazônia | 2.3 |
| c33e7db9-3347-3133-a02f-e21a3174a504 | -6.70696 | -42.79063 | 2025-10-04 04:12:00 | NOAA-20 | FRANCISCO AYRES | PIAUÍ | Brasil | 2204105 | 22 | 33 | nan | nan | nan | Caatinga | 1.9 |
| b4f48741-556b-3baf-86bf-25edeb0e5c2e | -5.83303 | -42.88277 | 2025-10-04 04:12:00 | NOAA-20 | PALMEIRAIS | PIAUÍ | Brasil | 2207504 | 22 | 33 | nan | nan | nan | Caatinga | 3.7 |
| 1fe03bcb-13eb-3cc1-9871-d3dfd1267cff | -5.83242 | -43.44617 | 2025-10-04 04:12:00 | NOAA-20 | PARNARAMA | MARANHÃO | Brasil | 2107803 | 21 | 33 | nan | nan | nan | Cerrado | 1.5 |
| 9e2e0fe8-a824-3f7b-b3f8-c5f7dd001a81 | -6.61382 | -44.29583 | 2025-10-04 04:12:00 | NOAA-20 | PASTOS BONS | MARANHÃO | Brasil | 2108009 | 21 | 33 | nan | nan | nan | Cerrado | 2.2 |
| 298d53ce-45aa-32ec-9ca3-91bed37f5b6a | -6.63538 | -45.00888 | 2025-10-04 04:12:00 | NOAA-20 | MIRADOR | MARANHÃO | Brasil | 2106706 | 21 | 33 | nan | nan | nan | Cerrado | 1.0 |
| 3d602b7b-b922-3a37-96e8-da5722f69c5c | -4.51463 | -50.48011 | 2025-10-04 04:12:00 | NOAA-20 | NOVO REPARTIMENTO | PARÁ | Brasil | 1505064 | 15 | 33 | nan | nan | nan | Amazônia | 2.4 |
| f147d5d2-2367-304d-9d39-4912d2c00cb3 | -6.67343 | -44.2028 | 2025-10-04 04:12:00 | NOAA-20 | PASTOS BONS | MARANHÃO | Brasil | 2108009 | 21 | 33 | nan | nan | nan | Cerrado | 3.1 |
| 6c961fed-bacc-3127-8cce-d98b4c72de02 | -5.87415 | -42.51419 | 2025-10-04 04:12:00 | NOAA-20 | OLHO D'ÁGUA DO PIAUÍ | PIAUÍ | Brasil | 2207108 | 22 | 33 | nan | nan | nan | Caatinga | 1.2 |
| 0d4f2c8b-831d-3512-ad71-75ff31d878e0 | -6.38859 | -44.77624 | 2025-10-04 04:12:00 | NOAA-20 | MIRADOR | MARANHÃO | Brasil | 2106706 | 21 | 33 | nan | nan | nan | Cerrado | 4.3 |
| bf9b6e78-b1cb-3662-bb1f-a8d5a96d8221 | -6.09516 | -43.48091 | 2025-10-04 04:12:00 | NOAA-20 | LAGOA DO MATO | MARANHÃO | Brasil | 2105922 | 21 | 33 | nan | nan | nan | Cerrado | 2.3 |
| 9c64c8fe-ac28-399a-8879-a7a91c70d92b | -6.66349 | -42.82989 | 2025-10-04 04:12:00 | NOAA-20 | FRANCISCO AYRES | PIAUÍ | Brasil | 2204105 | 22 | 33 | nan | nan | nan | Caatinga | 3.6 |
| 425bd0d6-696e-3ede-92a9-2f292dfcf0a3 | -7.70063 | -42.58376 | 2025-10-04 04:12:00 | NOAA-20 | SOCORRO DO PIAUÍ | PIAUÍ | Brasil | 2210904 | 22 | 33 | nan | nan | nan | Caatinga | 1.0 |
| ecb00916-7f4c-3c45-b82e-471e5bc37527 | -5.89434 | -42.53839 | 2025-10-04 04:12:00 | NOAA-20 | OLHO D'ÁGUA DO PIAUÍ | PIAUÍ | Brasil | 2207108 | 22 | 33 | nan | nan | nan | Caatinga | 1.4 |
| c0ed874d-2922-36e3-a5f4-567a5fc13499 | -6.07027 | -42.51987 | 2025-10-04 04:12:00 | NOAA-20 | JARDIM DO MULATO | PIAUÍ | Brasil | 2205250 | 22 | 33 | nan | nan | nan | Caatinga | 12.3 |
| 3ecb2d5a-4a37-3666-ba90-25e4bcb79560 | -6.87422 | -47.24262 | 2025-10-04 04:12:00 | NOAA-20 | ESTREITO | MARANHÃO | Brasil | 2104057 | 21 | 33 | nan | nan | nan | Cerrado | 3.3 |
| 8b821713-49ed-3f3e-9667-106d03df1165 | -5.38314 | -36.83459 | 2025-10-04 04:12:00 | NOAA-20 | ALTO DO RODRIGUES | RIO GRANDE DO NORTE | Brasil | 2400703 | 24 | 33 | nan | nan | nan | Caatinga | 0.8 |
| c74fea56-bd84-3e80-9f2e-e69fab26ca18 | -5.43274 | -47.09685 | 2025-10-04 04:12:00 | NOAA-20 | BURITIRANA | MARANHÃO | Brasil | 2102358 | 21 | 33 | nan | nan | nan | Amazônia | 2.3 |
| aae9f523-4d01-39a7-ba0c-19cde8effd9c | -6.22377 | -44.27352 | 2025-10-04 04:12:00 | NOAA-20 | MIRADOR | MARANHÃO | Brasil | 2106706 | 21 | 33 | nan | nan | nan | Cerrado | 4.3 |
| 0b2135ed-9ce7-3e39-a835-86d26f4c2189 | -7.88833 | -42.59912 | 2025-10-04 04:12:00 | NOAA-20 | RIBEIRA DO PIAUÍ | PIAUÍ | Brasil | 2208874 | 22 | 33 | nan | nan | nan | Caatinga | 1.8 |
| a2f17a4a-f7e6-371e-ae72-b02edf579cba | -6.76742 | -44.82084 | 2025-10-04 04:12:00 | NOAA-20 | SÃO FÉLIX DE BALSAS | MARANHÃO | Brasil | 2110807 | 21 | 33 | nan | nan | nan | Cerrado | 2.1 |
| 0a679506-864c-304a-ae6a-e0ca0668873e | -4.13529 | -47.65392 | 2025-10-04 04:12:00 | NOAA-20 | DOM ELISEU | PARÁ | Brasil | 1502939 | 15 | 33 | nan | nan | nan | Amazônia | 1.9 |
| c7d37ddc-1f52-3f8c-a6fc-80d376b977c9 | -6.87745 | -44.50276 | 2025-10-04 04:12:00 | NOAA-20 | SÃO DOMINGOS DO AZEITÃO | MARANHÃO | Brasil | 2110658 | 21 | 33 | nan | nan | nan | Cerrado | 9.6 |
| ddd6059e-07c8-3388-8d56-dbd8e66ced24 | -5.24237 | -45.55504 | 2025-10-04 04:12:00 | NOAA-20 | JENIPAPO DOS VIEIRAS | MARANHÃO | Brasil | 2105476 | 21 | 33 | nan | nan | nan | Cerrado | 1.4 |
| 5047bc89-6a4e-3a24-b0db-da9a5c461b64 | -3.68718 | -49.05618 | 2025-10-04 04:12:00 | NOAA-20 | GOIANÉSIA DO PARÁ | PARÁ | Brasil | 1503093 | 15 | 33 | nan | nan | nan | Amazônia | 1.1 |


[Clique aqui para ver as próximas entradas](README62.md)
