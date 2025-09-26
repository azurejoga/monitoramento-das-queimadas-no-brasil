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

## Dados Diários - Página 53

| ID | Latitude | Longitude | Data/Hora GMT | Satélite | Município | Estado | País | Município ID | Estado ID | País ID | Dias sem Chuva | Precipitação | Risco de Fogo | Bioma | FRP |
|----|----------|-----------|---------------|----------|-----------|--------|------|--------------|-----------|---------|----------------|--------------|----------------|-------|-----|
| d0706a6d-f620-3b2a-a07a-972e7374bcd5 | -11.4102 | -43.5099 | 2025-09-26 13:30:00 | GOES-19 | BARRA | BAHIA | Brasil | 2902708 | 29 | 33 | nan | nan | nan | Cerrado | 91.5 |
| 20ad8633-9447-3e4b-a4f8-600245354488 | -14.8304 | -45.3947 | 2025-09-26 13:30:00 | GOES-19 | COCOS | BAHIA | Brasil | 2908101 | 29 | 33 | nan | nan | nan | Cerrado | 86.2 |
| 6ff9f8b6-284d-3fb5-9857-e5408c1040e0 | -7.6584 | -46.0114 | 2025-09-26 13:30:00 | GOES-19 | BALSAS | MARANHÃO | Brasil | 2101400 | 21 | 33 | nan | nan | nan | Cerrado | 88.7 |
| ff9da47f-8509-386e-a95d-539b6e87f364 | -11.0444 | -45.9021 | 2025-09-26 13:30:00 | GOES-19 | FORMOSA DO RIO PRETO | BAHIA | Brasil | 2911105 | 29 | 33 | nan | nan | nan | Cerrado | 77.1 |
| b4a1da37-0c33-3fe9-9cc3-b848c094d1bf | -8.6631 | -43.991 | 2025-09-26 13:30:00 | GOES-19 | CRISTINO CASTRO | PIAUÍ | Brasil | 2203107 | 22 | 33 | nan | nan | nan | Cerrado | 99.0 |
| 9b5edfe6-5a1b-34e9-b47b-b400e7a952cb | -20.7338 | -57.8083 | 2025-09-26 13:30:00 | GOES-19 | CORUMBÁ | MATO GROSSO DO SUL | Brasil | 5003207 | 50 | 33 | nan | nan | nan | Pantanal | 90.1 |
| 8de90670-ce38-3f25-ae58-ff76c35fb7e2 | -8.8415 | -46.2095 | 2025-09-26 13:30:00 | GOES-19 | ALTO PARNAÍBA | MARANHÃO | Brasil | 2100501 | 21 | 33 | nan | nan | nan | Cerrado | 106.5 |
| 5fdaea25-0fb9-33ea-9e3d-9703772f1cd3 | -12.631 | -48.1313 | 2025-09-26 13:30:00 | GOES-19 | PARANÃ | TOCANTINS | Brasil | 1716208 | 17 | 33 | nan | nan | nan | Cerrado | 115.2 |
| f6077de5-a81f-37ac-a2c5-9faf58231e31 | -10.0062 | -44.1766 | 2025-09-26 13:30:00 | GOES-19 | CURIMATÁ | PIAUÍ | Brasil | 2203206 | 22 | 33 | nan | nan | nan | Cerrado | 150.1 |
| 30d97624-c5cf-36c4-adee-99b92bd3c8e5 | -11.9659 | -47.8669 | 2025-09-26 13:30:00 | GOES-19 | SÃO VALÉRIO | TOCANTINS | Brasil | 1720499 | 17 | 33 | nan | nan | nan | Cerrado | 69.9 |
| b80834ad-2cbd-3beb-b5df-cd9c99ed2d2d | -7.3371 | -46.2194 | 2025-09-26 13:40:00 | GOES-19 | RIACHÃO | MARANHÃO | Brasil | 2109502 | 21 | 33 | nan | nan | nan | Cerrado | 93.5 |
| 6e2b32f4-e7fa-3527-8d8d-bfcdfe87d59d | -5.9264 | -42.9253 | 2025-09-26 13:40:00 | GOES-19 | PALMEIRAIS | PIAUÍ | Brasil | 2207504 | 22 | 33 | nan | nan | nan | Caatinga | 96.0 |
| 163369cf-d672-35ae-bc22-1d01816bbbb1 | -7.6587 | -45.9889 | 2025-09-26 13:40:00 | GOES-19 | BALSAS | MARANHÃO | Brasil | 2101400 | 21 | 33 | nan | nan | nan | Cerrado | 94.1 |
| 24400059-2e13-3877-9d82-d3d70a90b3ac | -8.7708 | -43.0417 | 2025-09-26 13:40:00 | GOES-19 | JUREMA | PIAUÍ | Brasil | 2205532 | 22 | 33 | nan | nan | nan | Caatinga | 118.6 |
| cd075d64-c66b-367d-950e-12dd60d6f420 | -12.3427 | -50.544 | 2025-09-26 13:40:00 | GOES-19 | FORMOSO DO ARAGUAIA | TOCANTINS | Brasil | 1708205 | 17 | 33 | nan | nan | nan | Cerrado | 136.7 |
| 480f4826-ffc1-3588-b462-bc5927477e09 | -14.8309 | -45.3714 | 2025-09-26 13:40:00 | GOES-19 | COCOS | BAHIA | Brasil | 2908101 | 29 | 33 | nan | nan | nan | Cerrado | 89.1 |
| 2a9c5de9-124f-3165-9faf-4b0a1d5850f6 | -8.1327 | -44.1185 | 2025-09-26 13:40:00 | GOES-19 | SEBASTIÃO LEAL | PIAUÍ | Brasil | 2210631 | 22 | 33 | nan | nan | nan | Cerrado | 106.2 |
| 7a255863-0707-3f27-a695-fe0ef0181bb3 | -10.4392 | -48.2092 | 2025-09-26 13:40:00 | GOES-19 | PORTO NACIONAL | TOCANTINS | Brasil | 1718204 | 17 | 33 | nan | nan | nan | Cerrado | 69.2 |
| f98c4786-319a-3094-a57b-12a610c4ede8 | -8.6631 | -43.991 | 2025-09-26 13:40:00 | GOES-19 | CRISTINO CASTRO | PIAUÍ | Brasil | 2203107 | 22 | 33 | nan | nan | nan | Cerrado | 90.5 |
| 1fa27c74-c8e7-30d7-935b-b959c3e3c11e | -7.6775 | -45.9872 | 2025-09-26 13:40:00 | GOES-19 | BALSAS | MARANHÃO | Brasil | 2101400 | 21 | 33 | nan | nan | nan | Cerrado | 103.9 |
| 78e088d9-931b-3941-989f-f111e3cd1c16 | -5.475 | -43.0774 | 2025-09-26 13:40:00 | GOES-19 | MATÕES | MARANHÃO | Brasil | 2106607 | 21 | 33 | nan | nan | nan | Cerrado | 84.2 |
| 0dd9bf0f-c059-393c-8077-ae38e232ec06 | -20.7338 | -57.8083 | 2025-09-26 13:40:00 | GOES-19 | CORUMBÁ | MATO GROSSO DO SUL | Brasil | 5003207 | 50 | 33 | nan | nan | nan | Pantanal | 117.9 |
| ad2b91a6-16a0-3664-ba7d-3a0c4a3603ee | -10.3938 | -46.1444 | 2025-09-26 13:40:00 | GOES-19 | MATEIROS | TOCANTINS | Brasil | 1712702 | 17 | 33 | nan | nan | nan | Cerrado | 77.5 |
| 09d78547-0575-31c4-ad04-e9e8139c6c02 | -17.1746 | -56.3478 | 2025-09-26 13:40:00 | GOES-19 | BARÃO DE MELGAÇO | MATO GROSSO | Brasil | 5101605 | 51 | 33 | nan | nan | nan | Pantanal | 49.8 |
| bf873e27-a119-34cf-8ad2-9c6e028fdb81 | -6.9303 | -45.6931 | 2025-09-26 13:40:00 | GOES-19 | SÃO RAIMUNDO DAS MANGABEIRAS | MARANHÃO | Brasil | 2111607 | 21 | 33 | nan | nan | nan | Cerrado | 91.5 |
| c20f3935-090f-3224-8b01-b9dbf2f8fcd6 | -11.9659 | -47.8669 | 2025-09-26 13:40:00 | GOES-19 | SÃO VALÉRIO | TOCANTINS | Brasil | 1720499 | 17 | 33 | nan | nan | nan | Cerrado | 68.5 |
| 48c5f23b-9fed-3ce4-83cb-8c85093d7bdd | -8.8603 | -46.2075 | 2025-09-26 13:40:00 | GOES-19 | ALTO PARNAÍBA | MARANHÃO | Brasil | 2100501 | 21 | 33 | nan | nan | nan | Cerrado | 99.2 |
| acd1b79d-6b9c-3bb8-bb6f-30fb876eb668 | -12.5568 | -45.8459 | 2025-09-26 13:40:00 | GOES-19 | SÃO DESIDÉRIO | BAHIA | Brasil | 2928901 | 29 | 33 | nan | nan | nan | Cerrado | 64.8 |
| 7adbd806-0c12-39d7-94a6-7b0fcd5c977d | -11.0131 | -44.3424 | 2025-09-26 13:40:00 | GOES-19 | SANTA RITA DE CÁSSIA | BAHIA | Brasil | 2928406 | 29 | 33 | nan | nan | nan | Cerrado | 66.4 |
| 890b9cea-2039-3b5e-9e6d-256c17149ded | -8.8409 | -46.2544 | 2025-09-26 13:40:00 | GOES-19 | ALTO PARNAÍBA | MARANHÃO | Brasil | 2100501 | 21 | 33 | nan | nan | nan | Cerrado | 177.8 |
| cf5924cb-d1f8-3edc-8609-c01bc4acc692 | -12.1031 | -43.4008 | 2025-09-26 13:40:00 | GOES-19 | MUQUÉM DO SÃO FRANCISCO | BAHIA | Brasil | 2922250 | 29 | 33 | nan | nan | nan | Cerrado | 110.6 |
| f7037f03-14ad-3d5a-9d49-a3079dd0eb52 | -11.6238 | -44.4164 | 2025-09-26 13:40:00 | GOES-19 | COTEGIPE | BAHIA | Brasil | 2909406 | 29 | 33 | nan | nan | nan | Cerrado | 90.0 |
| e947d04a-1f95-34bd-b5d1-6f094ebd8582 | -8.0056 | -45.2555 | 2025-09-26 13:40:00 | GOES-19 | BAIXA GRANDE DO RIBEIRO | PIAUÍ | Brasil | 2201150 | 22 | 33 | nan | nan | nan | Cerrado | 79.4 |
| 473163e5-93b6-3599-93b2-07cc90028472 | -6.2689 | -42.472 | 2025-09-26 13:40:00 | GOES-19 | REGENERAÇÃO | PIAUÍ | Brasil | 2208809 | 22 | 33 | nan | nan | nan | Caatinga | 79.9 |
| d39ea153-8a1b-341f-9e2d-83a7666450ca | -7.6329 | -46.6172 | 2025-09-26 13:40:00 | GOES-19 | RIACHÃO | MARANHÃO | Brasil | 2109502 | 21 | 33 | nan | nan | nan | Cerrado | 92.4 |
| e47fdd39-1919-3967-baa1-f8c181360d37 | -5.4752 | -43.054 | 2025-09-26 13:40:00 | GOES-19 | MATÕES | MARANHÃO | Brasil | 2106607 | 21 | 33 | nan | nan | nan | Cerrado | 85.8 |
| bed1d02a-4967-3e0d-a684-8df39c019c26 | -10.0062 | -44.1766 | 2025-09-26 13:40:00 | GOES-19 | CURIMATÁ | PIAUÍ | Brasil | 2203206 | 22 | 33 | nan | nan | nan | Cerrado | 155.7 |
| ba889b34-3327-34b4-8a10-f51381c52990 | -5.4565 | -43.0554 | 2025-09-26 13:40:00 | GOES-19 | MATÕES | MARANHÃO | Brasil | 2106607 | 21 | 33 | nan | nan | nan | Cerrado | 79.8 |
| 59d4e013-7e26-3d3a-9a81-36abee0a7590 | -10.5979 | -44.0741 | 2025-09-26 13:40:00 | GOES-19 | BURITIRAMA | BAHIA | Brasil | 2904753 | 29 | 33 | nan | nan | nan | Cerrado | 84.2 |
| 495f4b38-502f-374e-9d6e-4729e59fef0d | -6.2501 | -42.4736 | 2025-09-26 13:40:00 | GOES-19 | REGENERAÇÃO | PIAUÍ | Brasil | 2208809 | 22 | 33 | nan | nan | nan | Caatinga | 72.0 |
| 2eb76ec2-b110-38ba-9dec-3f31b4241299 | -6.9115 | -45.6947 | 2025-09-26 13:40:00 | GOES-19 | SÃO RAIMUNDO DAS MANGABEIRAS | MARANHÃO | Brasil | 2111607 | 21 | 33 | nan | nan | nan | Cerrado | 73.4 |
| dc05a43d-1378-3371-8796-ea8c160317e8 | -10.4129 | -46.142 | 2025-09-26 13:40:00 | GOES-19 | MATEIROS | TOCANTINS | Brasil | 1712702 | 17 | 33 | nan | nan | nan | Cerrado | 75.1 |
| 3d3dec82-3c40-3f42-b961-b6ea22effa0b | -9.5648 | -48.5877 | 2025-09-26 13:40:00 | GOES-19 | MIRANORTE | TOCANTINS | Brasil | 1713304 | 17 | 33 | nan | nan | nan | Cerrado | 82.3 |
| 09484c7c-6ac4-310f-a877-61f7167f9815 | -11.6233 | -44.4398 | 2025-09-26 13:40:00 | GOES-19 | COTEGIPE | BAHIA | Brasil | 2909406 | 29 | 33 | nan | nan | nan | Cerrado | 85.3 |
| 05870348-f946-3c7a-9930-732c4af86f09 | -8.8415 | -46.2095 | 2025-09-26 13:40:00 | GOES-19 | ALTO PARNAÍBA | MARANHÃO | Brasil | 2100501 | 21 | 33 | nan | nan | nan | Cerrado | 81.0 |
| 753041be-42f9-3cc5-97a9-6a4a04b0800f | -10.9377 | -44.2832 | 2025-09-26 13:40:00 | GOES-19 | SANTA RITA DE CÁSSIA | BAHIA | Brasil | 2928406 | 29 | 33 | nan | nan | nan | Cerrado | 85.1 |
| 64be27d6-6d8f-3292-9d98-500822a08cca | -14.866 | -45.5511 | 2025-09-26 13:40:00 | GOES-19 | COCOS | BAHIA | Brasil | 2908101 | 29 | 33 | nan | nan | nan | Cerrado | 67.5 |
| 035ef584-db70-37ed-ab05-617fc2a127cc | -9.8658 | -45.9372 | 2025-09-26 13:40:00 | GOES-19 | ALTO PARNAÍBA | MARANHÃO | Brasil | 2100501 | 21 | 33 | nan | nan | nan | Cerrado | 63.7 |
| 696d5043-f6ab-3cbf-be1e-c5413fadf988 | -12.631 | -48.1313 | 2025-09-26 13:40:00 | GOES-19 | PARANÃ | TOCANTINS | Brasil | 1716208 | 17 | 33 | nan | nan | nan | Cerrado | 68.5 |
| 7f78d354-5a0a-3480-a386-64e1ef653c67 | -12.3424 | -50.5655 | 2025-09-26 13:40:00 | GOES-19 | FORMOSO DO ARAGUAIA | TOCANTINS | Brasil | 1708205 | 17 | 33 | nan | nan | nan | Cerrado | 159.6 |
| e27f00c8-682a-3ab2-9b61-e692fd6e443c | -14.8855 | -45.5475 | 2025-09-26 13:40:00 | GOES-19 | COCOS | BAHIA | Brasil | 2908101 | 29 | 33 | nan | nan | nan | Cerrado | 69.5 |
| fcc1bdba-959b-30f9-9b24-6a1319174754 | -8.1324 | -44.1417 | 2025-09-26 13:40:00 | GOES-19 | SEBASTIÃO LEAL | PIAUÍ | Brasil | 2210631 | 22 | 33 | nan | nan | nan | Cerrado | 98.1 |
| 3b449755-b2be-3c43-9f26-5115bffd3364 | -17.1743 | -56.3685 | 2025-09-26 13:40:00 | GOES-19 | BARÃO DE MELGAÇO | MATO GROSSO | Brasil | 5101605 | 51 | 33 | nan | nan | nan | Pantanal | 53.4 |
| f57762d7-8a15-373a-9f1a-660a47e03151 | -7.8735 | -45.2911 | 2025-09-26 13:40:00 | GOES-19 | RIBEIRO GONÇALVES | PIAUÍ | Brasil | 2208908 | 22 | 33 | nan | nan | nan | Cerrado | 89.1 |
| bc732043-d421-32f5-8a19-54a835b34606 | -11.6622 | -44.4107 | 2025-09-26 13:50:00 | GOES-19 | COTEGIPE | BAHIA | Brasil | 2909406 | 29 | 33 | nan | nan | nan | Cerrado | 98.2 |
| adbd3d62-b98c-39fb-8123-1348d85a8bc2 | -7.2203 | -46.6306 | 2025-09-26 13:50:00 | GOES-19 | RIACHÃO | MARANHÃO | Brasil | 2109502 | 21 | 33 | nan | nan | nan | Cerrado | 78.4 |
| ac2e5e6f-fb62-372d-a87a-6d90985b534e | -17.1743 | -56.3685 | 2025-09-26 13:50:00 | GOES-19 | BARÃO DE MELGAÇO | MATO GROSSO | Brasil | 5101605 | 51 | 33 | nan | nan | nan | Pantanal | 66.2 |
| 8307a4c9-4fa2-3465-b5a5-c34ca40d1932 | -7.6587 | -45.9889 | 2025-09-26 13:50:00 | GOES-19 | BALSAS | MARANHÃO | Brasil | 2101400 | 21 | 33 | nan | nan | nan | Cerrado | 140.9 |
| 786be6ff-7adc-3a62-b462-7171d8db769a | -5.4565 | -43.0554 | 2025-09-26 13:50:00 | GOES-19 | MATÕES | MARANHÃO | Brasil | 2106607 | 21 | 33 | nan | nan | nan | Cerrado | 88.8 |
| 45c7e662-a17f-39f7-9bb7-72543ba9a602 | -11.6233 | -44.4398 | 2025-09-26 13:50:00 | GOES-19 | COTEGIPE | BAHIA | Brasil | 2909406 | 29 | 33 | nan | nan | nan | Cerrado | 91.5 |
| 1457ea59-6fe5-336b-9218-eb4ccd431b39 | -11.4229 | -44.9563 | 2025-09-26 13:50:00 | GOES-19 | RIACHÃO DAS NEVES | BAHIA | Brasil | 2926202 | 29 | 33 | nan | nan | nan | Cerrado | 87.4 |
| 6d8c56fe-d666-3ddb-9783-74b3a7346545 | -6.9115 | -45.6947 | 2025-09-26 13:50:00 | GOES-19 | SÃO RAIMUNDO DAS MANGABEIRAS | MARANHÃO | Brasil | 2111607 | 21 | 33 | nan | nan | nan | Cerrado | 71.8 |
| 0155ec4c-b8f9-39dc-926c-277bc23207b9 | -11.9659 | -47.8669 | 2025-09-26 13:50:00 | GOES-19 | SÃO VALÉRIO | TOCANTINS | Brasil | 1720499 | 17 | 33 | nan | nan | nan | Cerrado | 70.4 |
| b567c464-432f-3548-890a-061861348570 | -6.5962 | -45.3822 | 2025-09-26 13:50:00 | GOES-19 | MIRADOR | MARANHÃO | Brasil | 2106706 | 21 | 33 | nan | nan | nan | Cerrado | 76.2 |
| a54863c6-b930-3f42-8c48-31977ce760a2 | -11.701 | -44.3815 | 2025-09-26 13:50:00 | GOES-19 | COTEGIPE | BAHIA | Brasil | 2909406 | 29 | 33 | nan | nan | nan | Cerrado | 88.5 |
| 80254318-46e4-39e1-9942-ba29165b8187 | -9.8658 | -45.9372 | 2025-09-26 13:50:00 | GOES-19 | ALTO PARNAÍBA | MARANHÃO | Brasil | 2100501 | 21 | 33 | nan | nan | nan | Cerrado | 72.6 |
| 471d01b2-d249-3c85-b613-95f8d0402b20 | -5.9264 | -42.9253 | 2025-09-26 13:50:00 | GOES-19 | PALMEIRAIS | PIAUÍ | Brasil | 2207504 | 22 | 33 | nan | nan | nan | Caatinga | 74.4 |
| 4d51ba21-5b20-3949-bdb4-97b31863bd45 | -11.4041 | -44.9359 | 2025-09-26 13:50:00 | GOES-19 | RIACHÃO DAS NEVES | BAHIA | Brasil | 2926202 | 29 | 33 | nan | nan | nan | Cerrado | 70.2 |
| 5925b6a6-be25-3347-b0e5-74364b429d03 | -11.7006 | -44.4049 | 2025-09-26 13:50:00 | GOES-19 | COTEGIPE | BAHIA | Brasil | 2909406 | 29 | 33 | nan | nan | nan | Cerrado | 220.8 |
| 4f4d68df-ad8f-3b47-bfaf-aaae917263eb | -11.6238 | -44.4164 | 2025-09-26 13:50:00 | GOES-19 | COTEGIPE | BAHIA | Brasil | 2909406 | 29 | 33 | nan | nan | nan | Cerrado | 87.9 |
| 972651e0-cf8e-389c-aed7-36c498b5de5d | -8.8415 | -46.2095 | 2025-09-26 13:50:00 | GOES-19 | ALTO PARNAÍBA | MARANHÃO | Brasil | 2100501 | 21 | 33 | nan | nan | nan | Cerrado | 84.8 |
| b648c7a8-45a8-340b-974e-d6aebfdb25d9 | -8.8603 | -46.2075 | 2025-09-26 13:50:00 | GOES-19 | ALTO PARNAÍBA | MARANHÃO | Brasil | 2100501 | 21 | 33 | nan | nan | nan | Cerrado | 109.7 |
| 3efd148f-2d70-31de-87f8-aa0b7ea8ff24 | -15.9273 | -57.4972 | 2025-09-26 13:50:00 | GOES-19 | CÁCERES | MATO GROSSO | Brasil | 5102504 | 51 | 33 | nan | nan | nan | Cerrado | 57.9 |
| b6ccad05-42ba-3b6a-a3c3-0e0edf8d4735 | -10.4129 | -46.142 | 2025-09-26 13:50:00 | GOES-19 | MATEIROS | TOCANTINS | Brasil | 1712702 | 17 | 33 | nan | nan | nan | Cerrado | 82.7 |
| 2ea8c0a3-726d-367a-9464-b3a7fbd9c8cf | -7.6775 | -45.9872 | 2025-09-26 13:50:00 | GOES-19 | BALSAS | MARANHÃO | Brasil | 2101400 | 21 | 33 | nan | nan | nan | Cerrado | 126.5 |
| 7966d6b8-68ed-3b44-bce4-84dc849e1c9e | -9.5648 | -48.5877 | 2025-09-26 13:50:00 | GOES-19 | MIRANORTE | TOCANTINS | Brasil | 1713304 | 17 | 33 | nan | nan | nan | Cerrado | 90.5 |
| f1cf47b1-3287-39d7-8fd4-f2c45e0d32fb | -10.0062 | -44.1766 | 2025-09-26 13:50:00 | GOES-19 | CURIMATÁ | PIAUÍ | Brasil | 2203206 | 22 | 33 | nan | nan | nan | Cerrado | 132.3 |
| b5dcefa2-517a-3f81-abbe-d6efc2b84dab | -8.1324 | -44.1417 | 2025-09-26 13:50:00 | GOES-19 | SEBASTIÃO LEAL | PIAUÍ | Brasil | 2210631 | 22 | 33 | nan | nan | nan | Cerrado | 75.3 |
| 6677f75b-8111-3816-b9fe-856d8942a737 | -4.1761 | -44.2716 | 2025-09-26 13:50:00 | GOES-19 | COROATÁ | MARANHÃO | Brasil | 2103604 | 21 | 33 | nan | nan | nan | Cerrado | 114.2 |
| d07a6eb2-6d3d-368c-a8a7-d5db4bd0a70b | -7.3371 | -46.2194 | 2025-09-26 13:50:00 | GOES-19 | RIACHÃO | MARANHÃO | Brasil | 2109502 | 21 | 33 | nan | nan | nan | Cerrado | 89.2 |
| 964bbd6f-3f81-3fa6-accc-dcf57dc61f7d | -10.3938 | -46.1444 | 2025-09-26 13:50:00 | GOES-19 | MATEIROS | TOCANTINS | Brasil | 1712702 | 17 | 33 | nan | nan | nan | Cerrado | 81.5 |
| d01a38c6-b0b8-3b7e-90f8-5052df9b5b86 | -10.5979 | -44.0741 | 2025-09-26 13:50:00 | GOES-19 | BURITIRAMA | BAHIA | Brasil | 2904753 | 29 | 33 | nan | nan | nan | Cerrado | 76.3 |
| 32b9ee3d-f1aa-3d54-b762-09da2f16ce4c | -11.4225 | -44.9794 | 2025-09-26 13:50:00 | GOES-19 | RIACHÃO DAS NEVES | BAHIA | Brasil | 2926202 | 29 | 33 | nan | nan | nan | Cerrado | 596.1 |
| 16fec300-3f86-3790-8732-b3eee163a387 | -11.6618 | -44.434 | 2025-09-26 13:50:00 | GOES-19 | COTEGIPE | BAHIA | Brasil | 2909406 | 29 | 33 | nan | nan | nan | Cerrado | 91.1 |
| d4116541-b25e-3d02-82a5-e793bcaaac65 | -11.681 | -44.4312 | 2025-09-26 13:50:00 | GOES-19 | COTEGIPE | BAHIA | Brasil | 2909406 | 29 | 33 | nan | nan | nan | Cerrado | 107.7 |
| 629bba2c-3d20-3898-a086-1b10075520e0 | -5.3091 | -42.761 | 2025-09-26 13:50:00 | GOES-19 | TERESINA | PIAUÍ | Brasil | 2211001 | 22 | 33 | nan | nan | nan | Caatinga | 120.7 |
| f15d6e2b-a4f1-338f-960e-18e9302948e7 | -12.631 | -48.1313 | 2025-09-26 13:50:00 | GOES-19 | PARANÃ | TOCANTINS | Brasil | 1716208 | 17 | 33 | nan | nan | nan | Cerrado | 123.2 |
| 665d2b69-ad3a-3652-9063-cff8d3bfc7f5 | -8.8409 | -46.2544 | 2025-09-26 13:50:00 | GOES-19 | ALTO PARNAÍBA | MARANHÃO | Brasil | 2100501 | 21 | 33 | nan | nan | nan | Cerrado | 133.2 |
| 0a58fe3c-8eb8-34ab-b9fd-0671dac23e2b | -14.7723 | -60.191 | 2025-09-26 13:50:00 | GOES-19 | VILA BELA DA SANTÍSSIMA TRINDADE | MATO GROSSO | Brasil | 5105507 | 51 | 33 | nan | nan | nan | Amazônia | 59.0 |
| 1011b7fc-3b34-3895-9592-efc219409b04 | -12.3424 | -50.5655 | 2025-09-26 13:50:00 | GOES-19 | FORMOSO DO ARAGUAIA | TOCANTINS | Brasil | 1708205 | 17 | 33 | nan | nan | nan | Cerrado | 159.5 |
| b551f395-c480-3544-b8a6-d41a2ef7318f | -20.7334 | -57.8293 | 2025-09-26 13:50:00 | GOES-19 | CORUMBÁ | MATO GROSSO DO SUL | Brasil | 5003207 | 50 | 33 | nan | nan | nan | Pantanal | 85.3 |
| 2d921bb9-e3e2-302e-b85f-68499c9ac15c | -5.4752 | -43.054 | 2025-09-26 13:50:00 | GOES-19 | MATÕES | MARANHÃO | Brasil | 2106607 | 21 | 33 | nan | nan | nan | Cerrado | 83.0 |
| 39ee29c2-ad25-3101-8329-9dad8e4a1ea7 | -7.6141 | -46.6188 | 2025-09-26 13:50:00 | GOES-19 | RIACHÃO | MARANHÃO | Brasil | 2109502 | 21 | 33 | nan | nan | nan | Cerrado | 91.9 |
| bc4550f1-81de-3bb3-b6cf-4b02beddc4f6 | -20.7342 | -57.7873 | 2025-09-26 13:50:00 | GOES-19 | CORUMBÁ | MATO GROSSO DO SUL | Brasil | 5003207 | 50 | 33 | nan | nan | nan | Pantanal | 72.3 |
| 5cb0330c-7917-3278-9ea7-6de1fe894f3a | -17.1939 | -56.3661 | 2025-09-26 13:50:00 | GOES-19 | BARÃO DE MELGAÇO | MATO GROSSO | Brasil | 5101605 | 51 | 33 | nan | nan | nan | Pantanal | 85.0 |
| 25bdbdcc-7e5c-3d6c-b412-36ab57154d79 | -5.7579 | -42.8917 | 2025-09-26 13:50:00 | GOES-19 | SÃO PEDRO DO PIAUÍ | PIAUÍ | Brasil | 2210508 | 22 | 33 | nan | nan | nan | Caatinga | 104.4 |
| 52816aeb-94bf-3950-87e3-9c0347cfb430 | -5.4562 | -43.0788 | 2025-09-26 13:50:00 | GOES-19 | MATÕES | MARANHÃO | Brasil | 2106607 | 21 | 33 | nan | nan | nan | Cerrado | 98.6 |
| 54e8927c-096c-333b-a44f-ef4c73ab5588 | -12.3427 | -50.544 | 2025-09-26 13:50:00 | GOES-19 | FORMOSO DO ARAGUAIA | TOCANTINS | Brasil | 1708205 | 17 | 33 | nan | nan | nan | Cerrado | 103.2 |
| 709ada24-fc7a-3442-99d0-b5e24e4b87e7 | -8.7708 | -43.0417 | 2025-09-26 13:50:00 | GOES-19 | JUREMA | PIAUÍ | Brasil | 2205532 | 22 | 33 | nan | nan | nan | Caatinga | 93.1 |
| b1f86e1c-03f6-3e0b-b057-41d11bb5d9a7 | -6.078 | -44.7418 | 2025-09-26 13:50:00 | GOES-19 | TUNTUM | MARANHÃO | Brasil | 2112308 | 21 | 33 | nan | nan | nan | Cerrado | 67.2 |


[Clique aqui para ver as próximas entradas](README54.md)
