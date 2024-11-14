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

## Dados Diários - Página 39

| ID | Latitude | Longitude | Data/Hora GMT | Satélite | Município | Estado | País | Município ID | Estado ID | País ID | Dias sem Chuva | Precipitação | Risco de Fogo | Bioma | FRP |
|----|----------|-----------|---------------|----------|-----------|--------|------|--------------|-----------|---------|----------------|--------------|----------------|-------|-----|
| 425d1a77-0370-3c93-ab2e-b46e9a42eeb9 | -17.69271 | -57.54365 | 2024-11-14 04:44:00 | NOAA-21 | POCONÉ | MATO GROSSO | Brasil | 5106505 | 51 | 33 | nan | nan | nan | Pantanal | 4.8 |
| 5b30a476-046d-3c32-a861-a48824ee7b26 | -17.70273 | -57.53423 | 2024-11-14 04:44:00 | NOAA-21 | POCONÉ | MATO GROSSO | Brasil | 5106505 | 51 | 33 | nan | nan | nan | Pantanal | 1.6 |
| bbc4217d-ddb8-3c0b-b549-45e433edc793 | -17.57963 | -57.54327 | 2024-11-14 04:44:00 | NOAA-21 | POCONÉ | MATO GROSSO | Brasil | 5106505 | 51 | 33 | nan | nan | nan | Pantanal | 3.4 |
| 2ff064a0-017b-3ebc-a253-2443e3af736b | -17.63045 | -57.54276 | 2024-11-14 04:44:00 | NOAA-21 | POCONÉ | MATO GROSSO | Brasil | 5106505 | 51 | 33 | nan | nan | nan | Pantanal | 4.0 |
| f3f06ed8-59b5-3b58-a089-346aaf699354 | -18.7238 | -55.58102 | 2024-11-14 04:44:00 | NOAA-21 | CORUMBÁ | MATO GROSSO DO SUL | Brasil | 5003207 | 50 | 33 | nan | nan | nan | Pantanal | 1.2 |
| fdf8a2bf-d174-3406-9c5e-46b03f542714 | -21.72063 | -48.46955 | 2024-11-14 04:44:00 | NOAA-21 | NOVA EUROPA | SÃO PAULO | Brasil | 3532900 | 35 | 33 | nan | nan | nan | Cerrado | 1.5 |
| c9ae56c9-53c3-3505-a267-ceff4495cf42 | -17.61771 | -57.54405 | 2024-11-14 04:44:00 | NOAA-21 | POCONÉ | MATO GROSSO | Brasil | 5106505 | 51 | 33 | nan | nan | nan | Pantanal | 4.1 |
| 195da4f1-94fb-31e5-a760-2edd054aaa54 | -17.29081 | -57.30863 | 2024-11-14 04:44:00 | NOAA-21 | POCONÉ | MATO GROSSO | Brasil | 5106505 | 51 | 33 | nan | nan | nan | Pantanal | 3.6 |
| 7dd2a4d1-7c37-3e38-a4b3-be41b57d4d9b | -17.31124 | -57.49837 | 2024-11-14 04:44:00 | NOAA-21 | CÁCERES | MATO GROSSO | Brasil | 5102504 | 51 | 33 | nan | nan | nan | Pantanal | 2.0 |
| 9dc9d6b9-75c7-3100-96f4-9d0d340334d5 | -17.59156 | -57.40952 | 2024-11-14 04:44:00 | NOAA-21 | POCONÉ | MATO GROSSO | Brasil | 5106505 | 51 | 33 | nan | nan | nan | Pantanal | 2.1 |
| f797383f-06e1-352f-b594-3c678b74f692 | -17.61245 | -57.54596 | 2024-11-14 04:44:00 | NOAA-21 | POCONÉ | MATO GROSSO | Brasil | 5106505 | 51 | 33 | nan | nan | nan | Pantanal | 5.4 |
| 5aa2c1fa-90ac-301a-ae07-496d0a0b0330 | -16.18804 | -59.35544 | 2024-11-14 04:44:00 | NOAA-21 | PORTO ESPERIDIÃO | MATO GROSSO | Brasil | 5106828 | 51 | 33 | nan | nan | nan | Amazônia | 2.1 |
| d6697938-82a9-33a8-b5ae-a9ce5f7f3550 | -17.57828 | -57.55063 | 2024-11-14 04:44:00 | NOAA-21 | POCONÉ | MATO GROSSO | Brasil | 5106505 | 51 | 33 | nan | nan | nan | Pantanal | 7.1 |
| e15a4c3b-f6b2-3ccc-a009-eda4c870ba7d | -17.29522 | -57.46782 | 2024-11-14 04:44:00 | NOAA-21 | CÁCERES | MATO GROSSO | Brasil | 5102504 | 51 | 33 | nan | nan | nan | Pantanal | 1.3 |
| 62567ef9-cb72-3c3d-93e1-0cb13303d19f | -17.58231 | -57.55143 | 2024-11-14 04:44:00 | NOAA-21 | POCONÉ | MATO GROSSO | Brasil | 5106505 | 51 | 33 | nan | nan | nan | Pantanal | 7.1 |
| 1876a411-a20e-32dc-b098-8200cec93b81 | -17.58432 | -57.54037 | 2024-11-14 04:44:00 | NOAA-21 | POCONÉ | MATO GROSSO | Brasil | 5106505 | 51 | 33 | nan | nan | nan | Pantanal | 3.4 |
| 55682dbf-9d7a-3b96-a833-0f723f844659 | -17.60299 | -57.48329 | 2024-11-14 04:44:00 | NOAA-21 | POCONÉ | MATO GROSSO | Brasil | 5106505 | 51 | 33 | nan | nan | nan | Pantanal | 4.9 |
| 1f8c5439-6e61-389a-af61-8c6b05787221 | -17.70108 | -54.08688 | 2024-11-14 04:44:00 | NOAA-21 | PEDRO GOMES | MATO GROSSO DO SUL | Brasil | 5006408 | 50 | 33 | nan | nan | nan | Cerrado | 0.6 |
| 1ca6d490-3657-33e8-88e0-39fc956fc38f | -16.03587 | -60.04863 | 2024-11-14 04:44:00 | NOAA-21 | VILA BELA DA SANTÍSSIMA TRINDADE | MATO GROSSO | Brasil | 5105507 | 51 | 33 | nan | nan | nan | Amazônia | 2.0 |
| 95cd59e9-ef68-3752-8822-d4cc17922320 | -15.87201 | -59.29906 | 2024-11-14 04:44:00 | NOAA-21 | PONTES E LACERDA | MATO GROSSO | Brasil | 5106752 | 51 | 33 | nan | nan | nan | Amazônia | 7.5 |
| 1adb9a57-ee07-34b1-b5d1-f707af2dfd0e | -17.6137 | -57.54327 | 2024-11-14 04:44:00 | NOAA-21 | POCONÉ | MATO GROSSO | Brasil | 5106505 | 51 | 33 | nan | nan | nan | Pantanal | 4.1 |
| c77ac839-b869-3817-b8d1-4410dd2f2d92 | -17.81989 | -57.37634 | 2024-11-14 04:44:00 | NOAA-21 | POCONÉ | MATO GROSSO | Brasil | 5106505 | 51 | 33 | nan | nan | nan | Pantanal | 1.5 |
| b1b39ac8-a8fc-3124-828b-551d96e82a63 | -15.87596 | -59.28672 | 2024-11-14 04:44:00 | NOAA-21 | PONTES E LACERDA | MATO GROSSO | Brasil | 5106752 | 51 | 33 | nan | nan | nan | Amazônia | 6.3 |
| 5b2fac77-1d30-367a-9938-0d3fe2988d1d | -18.72736 | -55.5817 | 2024-11-14 04:44:00 | NOAA-21 | CORUMBÁ | MATO GROSSO DO SUL | Brasil | 5003207 | 50 | 33 | nan | nan | nan | Pantanal | 2.1 |
| 63f303f2-eed7-3856-96a1-82baec74de6d | -17.57762 | -57.53143 | 2024-11-14 04:44:00 | NOAA-21 | POCONÉ | MATO GROSSO | Brasil | 5106505 | 51 | 33 | nan | nan | nan | Pantanal | 5.4 |
| 2c0b1fff-704e-3abb-a60a-237b094460c2 | -17.62908 | -57.5501 | 2024-11-14 04:44:00 | NOAA-21 | POCONÉ | MATO GROSSO | Brasil | 5106505 | 51 | 33 | nan | nan | nan | Pantanal | 8.5 |
| 8d01d357-a717-3c0c-a972-87ebd117037d | -17.59833 | -57.48615 | 2024-11-14 04:44:00 | NOAA-21 | POCONÉ | MATO GROSSO | Brasil | 5106505 | 51 | 33 | nan | nan | nan | Pantanal | 4.9 |
| 75ea1dd2-c2e5-39b5-ab03-454ce02f847d | -19.57883 | -54.8892 | 2024-11-14 04:44:00 | NOAA-21 | RIO NEGRO | MATO GROSSO DO SUL | Brasil | 5007307 | 50 | 33 | nan | nan | nan | Cerrado | 6.2 |
| c30a6297-1f06-319b-9b63-3a6a7d1fd217 | -17.57694 | -57.558 | 2024-11-14 04:44:00 | NOAA-21 | POCONÉ | MATO GROSSO | Brasil | 5106505 | 51 | 33 | nan | nan | nan | Pantanal | 9.8 |
| ed3fc238-c8ab-3fff-b08a-a3bfee861466 | -16.94505 | -57.64325 | 2024-11-14 04:44:00 | NOAA-21 | CÁCERES | MATO GROSSO | Brasil | 5102504 | 51 | 33 | nan | nan | nan | Pantanal | 1.2 |
| 5e3e0099-0995-333c-b8b8-79fed2d88d62 | -17.35959 | -57.43938 | 2024-11-14 04:44:00 | NOAA-21 | CÁCERES | MATO GROSSO | Brasil | 5102504 | 51 | 33 | nan | nan | nan | Pantanal | 1.1 |
| 1e42645f-b0c4-3359-99f6-1899817c954b | -17.70608 | -57.53867 | 2024-11-14 04:44:00 | NOAA-21 | POCONÉ | MATO GROSSO | Brasil | 5106505 | 51 | 33 | nan | nan | nan | Pantanal | 9.9 |
| 7307bc68-3454-3166-8d71-b251a7c54d10 | -17.23756 | -57.4641 | 2024-11-14 04:44:00 | NOAA-21 | CÁCERES | MATO GROSSO | Brasil | 5102504 | 51 | 33 | nan | nan | nan | Pantanal | 3.0 |
| 24af7259-3e02-39b6-90f3-5210cdbf6a28 | -17.26372 | -57.48069 | 2024-11-14 04:44:00 | NOAA-21 | CÁCERES | MATO GROSSO | Brasil | 5102504 | 51 | 33 | nan | nan | nan | Pantanal | 6.3 |
| 83df1e3d-4684-33dd-8fa8-933a9bad2dbc | -17.59432 | -57.48536 | 2024-11-14 04:44:00 | NOAA-21 | POCONÉ | MATO GROSSO | Brasil | 5106505 | 51 | 33 | nan | nan | nan | Pantanal | 4.3 |
| a9299ebd-fb83-3b71-8523-91550da5dfdc | -16.95207 | -57.64519 | 2024-11-14 04:44:00 | NOAA-21 | CÁCERES | MATO GROSSO | Brasil | 5102504 | 51 | 33 | nan | nan | nan | Pantanal | 3.6 |
| 684430d8-55c2-3359-ac9f-fab4e2d6ad03 | -17.70943 | -57.54314 | 2024-11-14 04:44:00 | NOAA-21 | POCONÉ | MATO GROSSO | Brasil | 5106505 | 51 | 33 | nan | nan | nan | Pantanal | 1.2 |
| f514516b-4734-39d7-8de0-8df4263c188c | -18.33322 | -55.58601 | 2024-11-14 04:44:00 | NOAA-21 | CORUMBÁ | MATO GROSSO DO SUL | Brasil | 5003207 | 50 | 33 | nan | nan | nan | Pantanal | 1.3 |
| 20e3af36-b3ea-3de3-9c14-91673a57639d | -17.58834 | -57.54117 | 2024-11-14 04:44:00 | NOAA-21 | POCONÉ | MATO GROSSO | Brasil | 5106505 | 51 | 33 | nan | nan | nan | Pantanal | 3.4 |
| 160e903b-c518-348d-b555-e1788ca0e7f7 | -17.587 | -57.54852 | 2024-11-14 04:44:00 | NOAA-21 | POCONÉ | MATO GROSSO | Brasil | 5106505 | 51 | 33 | nan | nan | nan | Pantanal | 5.7 |
| aee4e1f1-a2d9-3897-a4b6-938fbc32cb4c | -17.589 | -57.53749 | 2024-11-14 04:44:00 | NOAA-21 | POCONÉ | MATO GROSSO | Brasil | 5106505 | 51 | 33 | nan | nan | nan | Pantanal | 0.6 |
| c3c9b616-f82c-3470-b480-cb4e720dec94 | -17.61179 | -57.54964 | 2024-11-14 04:44:00 | NOAA-21 | POCONÉ | MATO GROSSO | Brasil | 5106505 | 51 | 33 | nan | nan | nan | Pantanal | 5.4 |
| 85d7c363-7cfa-3013-a55c-da45764787f4 | -20.61289 | -50.20416 | 2024-11-14 04:44:00 | NOAA-21 | MAGDA | SÃO PAULO | Brasil | 3528304 | 35 | 33 | nan | nan | nan | Mata Atlântica | 0.4 |
| dbf5d235-65bb-3a65-9400-8c45879a673b | -17.26305 | -57.48438 | 2024-11-14 04:44:00 | NOAA-21 | CÁCERES | MATO GROSSO | Brasil | 5102504 | 51 | 33 | nan | nan | nan | Pantanal | 2.4 |
| b4c4542e-6aa3-3f0d-8566-fd5a6867cea4 | -21.55212 | -55.82077 | 2024-11-14 04:44:00 | NOAA-21 | GUIA LOPES DA LAGUNA | MATO GROSSO DO SUL | Brasil | 5004106 | 50 | 33 | nan | nan | nan | Cerrado | 2.5 |
| 33a204c3-d3bc-3733-af5a-3e9b7e8ef2e1 | -17.23689 | -57.46778 | 2024-11-14 04:44:00 | NOAA-21 | CÁCERES | MATO GROSSO | Brasil | 5102504 | 51 | 33 | nan | nan | nan | Pantanal | 3.0 |
| cc56be54-0a04-3c9f-b969-4771ae4d58d9 | -15.90849 | -59.28458 | 2024-11-14 04:44:00 | NOAA-21 | PORTO ESPERIDIÃO | MATO GROSSO | Brasil | 5106828 | 51 | 33 | nan | nan | nan | Amazônia | 1.4 |
| b3551bd0-6bdf-31e0-aaaa-07df426bf87c | -17.61581 | -57.55044 | 2024-11-14 04:44:00 | NOAA-21 | POCONÉ | MATO GROSSO | Brasil | 5106505 | 51 | 33 | nan | nan | nan | Pantanal | 5.4 |
| c3629b8f-bc2b-3ca0-8a55-fd299cd8ce07 | -17.59766 | -57.4898 | 2024-11-14 04:44:00 | NOAA-21 | POCONÉ | MATO GROSSO | Brasil | 5106505 | 51 | 33 | nan | nan | nan | Pantanal | 3.4 |
| 7776b85b-67ae-3394-93bf-a2f774eb26a8 | -17.58162 | -57.44133 | 2024-11-14 04:44:00 | NOAA-21 | POCONÉ | MATO GROSSO | Brasil | 5106505 | 51 | 33 | nan | nan | nan | Pantanal | 1.2 |
| e51651cf-5182-35d2-a9c7-224d49a145a5 | -17.59303 | -57.53828 | 2024-11-14 04:44:00 | NOAA-21 | POCONÉ | MATO GROSSO | Brasil | 5106505 | 51 | 33 | nan | nan | nan | Pantanal | 0.6 |
| fa5cabec-fb56-3607-8d66-d193be5c1652 | -17.6321 | -57.44477 | 2024-11-14 04:44:00 | NOAA-21 | POCONÉ | MATO GROSSO | Brasil | 5106505 | 51 | 33 | nan | nan | nan | Pantanal | 0.7 |
| fb7d4f3d-5495-3de8-8423-42b74bf0aab2 | -15.87403 | -59.28873 | 2024-11-14 04:44:00 | NOAA-21 | PONTES E LACERDA | MATO GROSSO | Brasil | 5106752 | 51 | 33 | nan | nan | nan | Amazônia | 3.6 |
| e6a70332-3077-3625-b2fa-b91381525d80 | -17.56824 | -57.5372 | 2024-11-14 04:44:00 | NOAA-21 | POCONÉ | MATO GROSSO | Brasil | 5106505 | 51 | 33 | nan | nan | nan | Pantanal | 2.4 |
| 1e49a9e0-820c-3072-9681-21a01f8431df | -20.89507 | -49.96742 | 2024-11-14 04:44:00 | NOAA-21 | MACAUBAL | SÃO PAULO | Brasil | 3528106 | 35 | 33 | nan | nan | nan | Mata Atlântica | 2.0 |
| ab683ba3-3d74-3db0-8219-42a6045b7259 | -17.59365 | -57.48901 | 2024-11-14 04:44:00 | NOAA-21 | POCONÉ | MATO GROSSO | Brasil | 5106505 | 51 | 33 | nan | nan | nan | Pantanal | 1.9 |
| f39f0a63-6b58-3f1a-adf1-eece4368c62b | -17.61648 | -57.54675 | 2024-11-14 04:44:00 | NOAA-21 | POCONÉ | MATO GROSSO | Brasil | 5106505 | 51 | 33 | nan | nan | nan | Pantanal | 5.4 |
| 8845da67-a201-3e15-9e6e-16b3cbdb0e3b | -17.57761 | -57.55432 | 2024-11-14 04:44:00 | NOAA-21 | POCONÉ | MATO GROSSO | Brasil | 5106505 | 51 | 33 | nan | nan | nan | Pantanal | 9.8 |
| 0b32b429-9558-3c49-a8ca-61cccc7c1c98 | -16.00451 | -59.40139 | 2024-11-14 04:44:00 | NOAA-21 | PONTES E LACERDA | MATO GROSSO | Brasil | 5106752 | 51 | 33 | nan | nan | nan | Amazônia | 2.1 |
| 173d8b00-b443-3cf1-bc0f-c5d04b869b95 | -17.57628 | -57.53878 | 2024-11-14 04:44:00 | NOAA-21 | POCONÉ | MATO GROSSO | Brasil | 5106505 | 51 | 33 | nan | nan | nan | Pantanal | 4.3 |
| bad14f31-05f0-395c-9982-1f400a411aa1 | -19.8555 | -51.50452 | 2024-11-14 04:44:00 | NOAA-21 | PARANAÍBA | MATO GROSSO DO SUL | Brasil | 5006309 | 50 | 33 | nan | nan | nan | Cerrado | 1.0 |
| cf9a9e54-1201-333e-b946-bda6385b50ab | -15.87503 | -59.29165 | 2024-11-14 04:44:00 | NOAA-21 | PONTES E LACERDA | MATO GROSSO | Brasil | 5106752 | 51 | 33 | nan | nan | nan | Amazônia | 6.3 |
| d7d47acd-fa56-30df-b0d7-7fe99d951c6a | -16.00103 | -59.09922 | 2024-11-14 04:44:00 | NOAA-21 | PORTO ESPERIDIÃO | MATO GROSSO | Brasil | 5106828 | 51 | 33 | nan | nan | nan | Amazônia | 1.1 |
| 07f7844e-7ef8-3b4b-a5fb-eca12976b6dc | -17.57695 | -57.5351 | 2024-11-14 04:44:00 | NOAA-21 | POCONÉ | MATO GROSSO | Brasil | 5106505 | 51 | 33 | nan | nan | nan | Pantanal | 5.4 |
| 3ac07cb9-0503-3e51-ae23-b96497840355 | -17.56891 | -57.53352 | 2024-11-14 04:44:00 | NOAA-21 | POCONÉ | MATO GROSSO | Brasil | 5106505 | 51 | 33 | nan | nan | nan | Pantanal | 18.7 |
| a006dbd1-43d4-3840-b4b6-0c6dc908d468 | -17.26775 | -57.48147 | 2024-11-14 04:44:00 | NOAA-21 | CÁCERES | MATO GROSSO | Brasil | 5102504 | 51 | 33 | nan | nan | nan | Pantanal | 6.3 |
| bcab0241-dede-3580-8725-e597e38af14d | -17.61113 | -57.55332 | 2024-11-14 04:44:00 | NOAA-21 | POCONÉ | MATO GROSSO | Brasil | 5106505 | 51 | 33 | nan | nan | nan | Pantanal | 8.2 |
| 19cc1c1d-5825-3f43-ad13-ae1dba829b57 | -20.69457 | -48.8053 | 2024-11-14 04:44:00 | NOAA-21 | OLÍMPIA | SÃO PAULO | Brasil | 3533908 | 35 | 33 | nan | nan | nan | Mata Atlântica | 3.6 |
| 61c7cf63-826d-3930-96d7-f9f9d261203e | -15.89769 | -59.31557 | 2024-11-14 04:44:00 | NOAA-21 | PONTES E LACERDA | MATO GROSSO | Brasil | 5106752 | 51 | 33 | nan | nan | nan | Amazônia | 1.8 |
| 08652805-a831-3faf-bb4b-2f9f8a87b55c | -17.24628 | -57.46201 | 2024-11-14 04:44:00 | NOAA-21 | CÁCERES | MATO GROSSO | Brasil | 5102504 | 51 | 33 | nan | nan | nan | Pantanal | 5.8 |
| 6f5b88a1-848e-3b8b-b835-217f7e9934cf | -17.597 | -57.49346 | 2024-11-14 04:44:00 | NOAA-21 | POCONÉ | MATO GROSSO | Brasil | 5106505 | 51 | 33 | nan | nan | nan | Pantanal | 3.4 |
| 9fdbb34b-4a8a-3de0-b005-3c56f9493028 | -17.25567 | -57.4791 | 2024-11-14 04:44:00 | NOAA-21 | CÁCERES | MATO GROSSO | Brasil | 5102504 | 51 | 33 | nan | nan | nan | Pantanal | 8.5 |
| 73904ca2-c0fb-300e-9262-13a19713f565 | -21.55559 | -55.82149 | 2024-11-14 04:44:00 | NOAA-21 | GUIA LOPES DA LAGUNA | MATO GROSSO DO SUL | Brasil | 5004106 | 50 | 33 | nan | nan | nan | Cerrado | 2.5 |
| 5f8efa94-abbf-3384-aa20-74141e85d7c2 | -17.26909 | -57.4741 | 2024-11-14 04:44:00 | NOAA-21 | CÁCERES | MATO GROSSO | Brasil | 5102504 | 51 | 33 | nan | nan | nan | Pantanal | 4.5 |
| c32bb11b-4971-3136-b294-a4d4e00c92a2 | -15.87776 | -59.29427 | 2024-11-14 04:44:00 | NOAA-21 | PONTES E LACERDA | MATO GROSSO | Brasil | 5106752 | 51 | 33 | nan | nan | nan | Amazônia | 8.3 |
| 6c707c97-8782-3dda-a621-4619d35e9698 | -19.10245 | -54.07587 | 2024-11-14 04:44:00 | NOAA-21 | CAMAPUÃ | MATO GROSSO DO SUL | Brasil | 5002605 | 50 | 33 | nan | nan | nan | Cerrado | 0.5 |
| 9505a265-4160-3b5d-9a97-514218ae7da2 | -17.04964 | -57.43529 | 2024-11-14 04:44:00 | NOAA-21 | CÁCERES | MATO GROSSO | Brasil | 5102504 | 51 | 33 | nan | nan | nan | Pantanal | 0.6 |
| 9bb058bd-5acc-3fc0-a795-c9f0c5e97690 | -17.24226 | -57.46121 | 2024-11-14 04:44:00 | NOAA-21 | CÁCERES | MATO GROSSO | Brasil | 5102504 | 51 | 33 | nan | nan | nan | Pantanal | 5.8 |
| 2ba427b3-d670-3502-8524-932bf7a98afa | -17.62575 | -57.54564 | 2024-11-14 04:44:00 | NOAA-21 | POCONÉ | MATO GROSSO | Brasil | 5106505 | 51 | 33 | nan | nan | nan | Pantanal | 1.9 |
| 2232ce8e-9e6c-3481-a55c-22933b1e14c1 | -16.94574 | -57.63943 | 2024-11-14 04:44:00 | NOAA-21 | CÁCERES | MATO GROSSO | Brasil | 5102504 | 51 | 33 | nan | nan | nan | Pantanal | 1.2 |
| b181b83f-3cd4-334f-9810-5751d35f7ac3 | -17.37094 | -52.00999 | 2024-11-14 04:44:00 | NOAA-21 | CAIAPÔNIA | GOIÁS | Brasil | 5204409 | 52 | 33 | nan | nan | nan | Cerrado | 1.6 |
| 60460412-a95e-3216-b005-29d74ac49ac5 | -17.58097 | -57.5359 | 2024-11-14 04:44:00 | NOAA-21 | POCONÉ | MATO GROSSO | Brasil | 5106505 | 51 | 33 | nan | nan | nan | Pantanal | 2.2 |
| b83c9499-fa48-3f23-8534-3c1afc6dab86 | -15.41121 | -58.60995 | 2024-11-14 04:44:00 | NOAA-21 | INDIAVAÍ | MATO GROSSO | Brasil | 5104500 | 51 | 33 | nan | nan | nan | Amazônia | 1.2 |
| 1b12d0a0-f205-348c-8133-dbf96ebda548 | -17.60101 | -57.49425 | 2024-11-14 04:44:00 | NOAA-21 | POCONÉ | MATO GROSSO | Brasil | 5106505 | 51 | 33 | nan | nan | nan | Pantanal | 3.4 |
| 8dc9ba00-56c3-3aeb-b103-79b41243e6d7 | -17.21705 | -57.22732 | 2024-11-14 04:44:00 | NOAA-21 | POCONÉ | MATO GROSSO | Brasil | 5106505 | 51 | 33 | nan | nan | nan | Pantanal | 1.0 |
| 4b09324f-de6f-3aff-a44a-c629e60cca12 | -17.24963 | -57.46647 | 2024-11-14 04:44:00 | NOAA-21 | CÁCERES | MATO GROSSO | Brasil | 5102504 | 51 | 33 | nan | nan | nan | Pantanal | 18.7 |
| a130888a-8e34-33fe-9511-985efe588461 | -21.07841 | -54.22025 | 2024-11-14 04:44:00 | NOAA-21 | CAMPO GRANDE | MATO GROSSO DO SUL | Brasil | 5002704 | 50 | 33 | nan | nan | nan | Cerrado | 0.5 |
| b2120f6f-9600-35c6-bba3-b1928610776a | -17.25366 | -57.46727 | 2024-11-14 04:44:00 | NOAA-21 | CÁCERES | MATO GROSSO | Brasil | 5102504 | 51 | 33 | nan | nan | nan | Pantanal | 18.7 |
| 8f7078ce-2246-34b8-a0af-08f9693f0add | -16.94028 | -57.64625 | 2024-11-14 04:44:00 | NOAA-21 | CÁCERES | MATO GROSSO | Brasil | 5102504 | 51 | 33 | nan | nan | nan | Pantanal | 1.3 |
| d8dfadba-cccc-3bd9-bac9-d1a6c9a0cf40 | -16.95278 | -57.64139 | 2024-11-14 04:44:00 | NOAA-21 | CÁCERES | MATO GROSSO | Brasil | 5102504 | 51 | 33 | nan | nan | nan | Pantanal | 3.6 |
| ed652c0c-1e1c-3bf9-b130-de8dba62f218 | -17.255 | -57.48279 | 2024-11-14 04:44:00 | NOAA-21 | CÁCERES | MATO GROSSO | Brasil | 5102504 | 51 | 33 | nan | nan | nan | Pantanal | 2.4 |
| 03b99859-94c8-3170-b1c9-81b46632cb9c | -15.48332 | -58.19846 | 2024-11-14 04:44:00 | NOAA-21 | SÃO JOSÉ DOS QUATRO MARCOS | MATO GROSSO | Brasil | 5107107 | 51 | 33 | nan | nan | nan | Amazônia | 1.6 |
| e38e5a41-88f7-30ce-8b16-2d23c1c92147 | -16.94643 | -57.63562 | 2024-11-14 04:44:00 | NOAA-21 | CÁCERES | MATO GROSSO | Brasil | 5102504 | 51 | 33 | nan | nan | nan | Pantanal | 1.7 |
| 0b440007-147c-34ba-811a-6ba103737e5b | -17.58767 | -57.54484 | 2024-11-14 04:44:00 | NOAA-21 | POCONÉ | MATO GROSSO | Brasil | 5106505 | 51 | 33 | nan | nan | nan | Pantanal | 3.4 |
| e2187166-b65d-3c7b-8135-ae1617e98aac | -20.38808 | -55.69277 | 2024-11-14 04:44:00 | NOAA-21 | AQUIDAUANA | MATO GROSSO DO SUL | Brasil | 5001102 | 50 | 33 | nan | nan | nan | Cerrado | 1.9 |
| 5c716c23-d08f-345c-a067-a5e6fa68c7dd | -17.58096 | -57.5588 | 2024-11-14 04:44:00 | NOAA-21 | POCONÉ | MATO GROSSO | Brasil | 5106505 | 51 | 33 | nan | nan | nan | Pantanal | 9.8 |
| 86460f4f-665d-347f-9807-4b080ebf15e5 | -15.87876 | -59.28912 | 2024-11-14 04:44:00 | NOAA-21 | PONTES E LACERDA | MATO GROSSO | Brasil | 5106752 | 51 | 33 | nan | nan | nan | Amazônia | 2.4 |
| c962cbdd-418c-338e-9355-f7852f5b652d | -17.59899 | -57.4825 | 2024-11-14 04:44:00 | NOAA-21 | POCONÉ | MATO GROSSO | Brasil | 5106505 | 51 | 33 | nan | nan | nan | Pantanal | 4.9 |
| d79e98e4-dc1b-301f-add8-2117b567427f | -17.3715 | -52.00639 | 2024-11-14 04:44:00 | NOAA-21 | CAIAPÔNIA | GOIÁS | Brasil | 5204409 | 52 | 33 | nan | nan | nan | Cerrado | 1.6 |
| 4d5eb579-e9ea-389f-be16-bff5199b9bb5 | -17.58627 | -57.43849 | 2024-11-14 04:44:00 | NOAA-21 | POCONÉ | MATO GROSSO | Brasil | 5106505 | 51 | 33 | nan | nan | nan | Pantanal | 2.5 |


[Clique aqui para ver as próximas entradas](README40.md)
