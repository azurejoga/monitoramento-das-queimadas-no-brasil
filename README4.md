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

## Dados Diários - Página 4

| ID | Latitude | Longitude | Data/Hora GMT | Satélite | Município | Estado | País | Município ID | Estado ID | País ID | Dias sem Chuva | Precipitação | Risco de Fogo | Bioma | FRP |
|----|----------|-----------|---------------|----------|-----------|--------|------|--------------|-----------|---------|----------------|--------------|----------------|-------|-----|
| f8595947-70f7-31d2-8c39-358ead521dd2 | -12.05428 | -46.88919 | 2024-12-11 00:37:00 | TERRA_M-M | TAIPAS DO TOCANTINS | TOCANTINS | Brasil | 1720937 | 17 | 33 | nan | nan | nan | Cerrado | 4.9 |
| 93710aea-ef38-3112-a6f8-5ec9bf1f8df6 | -6.89361 | -43.52237 | 2024-12-11 00:37:00 | TERRA_M-M | JERUMENHA | PIAUÍ | Brasil | 2205300 | 22 | 33 | nan | nan | nan | Cerrado | 18.8 |
| 5d56336a-b16e-35cc-80bc-f0420f716a79 | -6.96744 | -43.00492 | 2024-12-11 00:37:00 | TERRA_M-M | FLORIANO | PIAUÍ | Brasil | 2203909 | 22 | 33 | nan | nan | nan | Caatinga | 38.2 |
| 72e2cc4a-f357-305f-a27a-a4b43d428abc | -10.54483 | -44.68114 | 2024-12-11 00:37:00 | TERRA_M-M | PARNAGUÁ | PIAUÍ | Brasil | 2207603 | 22 | 33 | nan | nan | nan | Cerrado | 5.2 |
| c2e728fe-b733-33bc-9ad3-23f436d754d5 | -13.25902 | -41.34256 | 2024-12-11 00:37:00 | TERRA_M-M | MUCUGÊ | BAHIA | Brasil | 2921906 | 29 | 33 | nan | nan | nan | Caatinga | 21.6 |
| a8046392-0654-3002-b028-17d770eb1a2c | -12.41255 | -43.80453 | 2024-12-11 00:37:00 | TERRA_M-M | BREJOLÂNDIA | BAHIA | Brasil | 2904407 | 29 | 33 | nan | nan | nan | Cerrado | 26.5 |
| 0c03ba70-de57-3bfe-ac90-19905e843699 | -6.12068 | -42.54549 | 2024-12-11 00:37:00 | TERRA_M-M | JARDIM DO MULATO | PIAUÍ | Brasil | 2205250 | 22 | 33 | nan | nan | nan | Caatinga | 32.8 |
| 76d8b825-abb8-3f16-adf4-433509c2c630 | -8.9228 | -35.95545 | 2024-12-11 00:37:00 | TERRA_M-M | IBATEGUARA | ALAGOAS | Brasil | 2703007 | 27 | 33 | nan | nan | nan | Mata Atlântica | 26.1 |
| 3cdd7a46-b0ca-3ae9-b82e-7c273d11d99e | -6.95829 | -43.00624 | 2024-12-11 00:37:00 | TERRA_M-M | FLORIANO | PIAUÍ | Brasil | 2203909 | 22 | 33 | nan | nan | nan | Caatinga | 29.3 |
| c3f84927-25c3-3c32-a987-0f4c2f817126 | -11.46241 | -42.74294 | 2024-12-11 00:37:00 | TERRA_M-M | GENTIO DO OURO | BAHIA | Brasil | 2911303 | 29 | 33 | nan | nan | nan | Caatinga | 7.0 |
| b6d687c6-aa88-3d71-8960-41bab97ee95f | -6.94914 | -43.00755 | 2024-12-11 00:37:00 | TERRA_M-M | FLORIANO | PIAUÍ | Brasil | 2203909 | 22 | 33 | nan | nan | nan | Caatinga | 25.4 |
| 826a0905-0ff4-388e-91f6-b25d7f237013 | -6.11925 | -42.53537 | 2024-12-11 00:37:00 | TERRA_M-M | JARDIM DO MULATO | PIAUÍ | Brasil | 2205250 | 22 | 33 | nan | nan | nan | Caatinga | 9.4 |
| fdb71aac-ed3b-3840-b6f3-c65feb28277c | -12.4113 | -43.79546 | 2024-12-11 00:37:00 | TERRA_M-M | BREJOLÂNDIA | BAHIA | Brasil | 2904407 | 29 | 33 | nan | nan | nan | Cerrado | 16.8 |
| 4c6f51a4-2745-3fd2-81f2-906bdd8c0e29 | -12.88752 | -43.64878 | 2024-12-11 00:37:00 | TERRA_M-M | SERRA DOURADA | BAHIA | Brasil | 2930303 | 29 | 33 | nan | nan | nan | Cerrado | 17.6 |
| 1558b4ef-1c99-3586-b0d0-e479352f0fc4 | -10.51579 | -44.93877 | 2024-12-11 00:37:00 | TERRA_M-M | CORRENTE | PIAUÍ | Brasil | 2202901 | 22 | 33 | nan | nan | nan | Cerrado | 7.1 |
| d4354d7e-b4fa-31e0-b5f1-1d3f869fa435 | -10.51454 | -44.92951 | 2024-12-11 00:37:00 | TERRA_M-M | CORRENTE | PIAUÍ | Brasil | 2202901 | 22 | 33 | nan | nan | nan | Cerrado | 6.6 |
| 9d6108d0-4b92-3e1f-ada6-dc4c1a6a1741 | -6.97388 | -42.9846 | 2024-12-11 00:37:00 | TERRA_M-M | FLORIANO | PIAUÍ | Brasil | 2203909 | 22 | 33 | nan | nan | nan | Caatinga | 11.5 |
| 42384dbb-e207-34dc-a4b1-802842bf908e | -10.19524 | -36.22902 | 2024-12-11 00:37:00 | TERRA_M-M | CORURIPE | ALAGOAS | Brasil | 2702306 | 27 | 33 | nan | nan | nan | Mata Atlântica | 27.6 |
| b647ea91-e0bc-321b-8dac-c8231b9d8a91 | -11.46487 | -44.95273 | 2024-12-11 00:37:00 | TERRA_M-M | RIACHÃO DAS NEVES | BAHIA | Brasil | 2926202 | 29 | 33 | nan | nan | nan | Cerrado | 7.4 |
| 1067b711-3510-3b65-9d1e-a7eb61016444 | -7.0259 | -40.1847 | 2024-12-11 00:37:00 | TERRA_M-M | SALITRE | CEARÁ | Brasil | 2311959 | 23 | 33 | nan | nan | nan | Caatinga | 12.9 |
| d410196e-3ea7-3963-b042-9de541875edf | -14.00942 | -44.18221 | 2024-12-11 00:37:00 | TERRA_M-M | FEIRA DA MATA | BAHIA | Brasil | 2910776 | 29 | 33 | nan | nan | nan | Cerrado | 4.7 |
| 58836508-6537-39ba-990e-3fe5e7211f29 | -6.97524 | -42.99412 | 2024-12-11 00:37:00 | TERRA_M-M | FLORIANO | PIAUÍ | Brasil | 2203909 | 22 | 33 | nan | nan | nan | Caatinga | 91.3 |
| 93349ce3-388b-3e36-9ebc-dd7cfb13982b | -6.29334 | -43.83804 | 2024-12-11 00:37:00 | TERRA_M-M | SÃO JOÃO DOS PATOS | MARANHÃO | Brasil | 2111102 | 21 | 33 | nan | nan | nan | Cerrado | 7.9 |
| 311ab1ac-ff7c-33cb-89ed-5a6753c26d35 | -3.80769 | -52.39521 | 2024-12-11 00:39:00 | TERRA_M-M | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 41.3 |
| 05150765-1f34-355b-82d9-a552a999b909 | -5.97858 | -44.60945 | 2024-12-11 00:39:00 | TERRA_M-M | TUNTUM | MARANHÃO | Brasil | 2112308 | 21 | 33 | nan | nan | nan | Cerrado | 5.2 |
| 0612fc9a-4b74-3a4d-98bf-47972ff3f700 | -3.55883 | -44.17227 | 2024-12-11 00:39:00 | TERRA_M-M | CANTANHEDE | MARANHÃO | Brasil | 2102705 | 21 | 33 | nan | nan | nan | Cerrado | 4.6 |
| b0aafe42-3552-3f9a-b36d-7eee3ebd0e9f | -3.35004 | -53.07978 | 2024-12-11 00:39:00 | TERRA_M-M | MEDICILÂNDIA | PARÁ | Brasil | 1504455 | 15 | 33 | nan | nan | nan | Amazônia | 17.8 |
| 6c76d207-ca42-3329-8df2-8c91564dc975 | -3.12268 | -54.09666 | 2024-12-11 00:39:00 | TERRA_M-M | SANTARÉM | PARÁ | Brasil | 1506807 | 15 | 33 | nan | nan | nan | Amazônia | 87.2 |
| e82bd068-de18-393a-a82d-96d7fd117bdb | -3.32038 | -46.8298 | 2024-12-11 00:39:00 | TERRA_M-M | CENTRO NOVO DO MARANHÃO | MARANHÃO | Brasil | 2103174 | 21 | 33 | nan | nan | nan | Amazônia | 13.5 |
| c5a9eefb-d8b1-3a07-9697-99bd30b929d3 | -3.15226 | -54.47245 | 2024-12-11 00:39:00 | TERRA_M-M | MOJUÍ DOS CAMPOS | PARÁ | Brasil | 1504752 | 15 | 33 | nan | nan | nan | Amazônia | 48.9 |
| 33f6c5a4-cf1e-3e7a-bd8d-cec0a15a751d | -3.33565 | -53.08137 | 2024-12-11 00:39:00 | TERRA_M-M | MEDICILÂNDIA | PARÁ | Brasil | 1504455 | 15 | 33 | nan | nan | nan | Amazônia | 15.2 |
| 8870a917-4c46-3566-b6f1-d25c154a2f7c | -3.32483 | -53.24411 | 2024-12-11 00:39:00 | TERRA_M-M | MEDICILÂNDIA | PARÁ | Brasil | 1504455 | 15 | 33 | nan | nan | nan | Amazônia | 37.2 |
| a8d2592e-eef7-3b38-a502-43907565ea0d | -3.11866 | -54.09192 | 2024-12-11 00:39:00 | TERRA_M-M | SANTARÉM | PARÁ | Brasil | 1506807 | 15 | 33 | nan | nan | nan | Amazônia | 27.4 |
| 8533c18d-ec54-36b8-ade2-159c97b4b481 | -3.0786 | -40.0625 | 2024-12-11 00:39:00 | TERRA_M-M | ACARAÚ | CEARÁ | Brasil | 2300200 | 23 | 33 | nan | nan | nan | Caatinga | 15.9 |
| 5d1d51f9-23ef-303f-b2e0-3126c6da4b5c | -3.1341 | -54.08957 | 2024-12-11 00:39:00 | TERRA_M-M | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | 103.0 |
| 980c6e25-747b-3352-b456-89e2bb0b837e | -3.34373 | -53.0601 | 2024-12-11 00:39:00 | TERRA_M-M | MEDICILÂNDIA | PARÁ | Brasil | 1504455 | 15 | 33 | nan | nan | nan | Amazônia | 18.4 |
| ff11f89b-6ce7-336b-9906-bbdfdbb1bc29 | -2.86444 | -52.54198 | 2024-12-11 00:39:00 | TERRA_M-M | BRASIL NOVO | PARÁ | Brasil | 1501725 | 15 | 33 | nan | nan | nan | Amazônia | 13.3 |
| 6cb29936-bcac-3a3c-b36c-b5a0802c59a4 | -3.20993 | -52.85805 | 2024-12-11 00:39:00 | TERRA_M-M | MEDICILÂNDIA | PARÁ | Brasil | 1504455 | 15 | 33 | nan | nan | nan | Amazônia | 12.0 |
| 357b2a7d-ab1b-3a5d-80af-158b63771b09 | -3.42782 | -52.76039 | 2024-12-11 00:39:00 | TERRA_M-M | MEDICILÂNDIA | PARÁ | Brasil | 1504455 | 15 | 33 | nan | nan | nan | Amazônia | 18.3 |
| faf9ca0d-ed9f-32ef-9353-c02038f2885d | -3.69093 | -43.73457 | 2024-12-11 00:39:00 | TERRA_M-M | VARGEM GRANDE | MARANHÃO | Brasil | 2112704 | 21 | 33 | nan | nan | nan | Cerrado | 7.4 |
| fbd01b5c-6f6d-3161-94d9-c5a96682342c | -3.81148 | -52.37682 | 2024-12-11 00:39:00 | TERRA_M-M | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 35.3 |
| d06f64b1-77fd-3471-ae68-7964825fad7f | -5.98621 | -44.59933 | 2024-12-11 00:39:00 | TERRA_M-M | COLINAS | MARANHÃO | Brasil | 2103505 | 21 | 33 | nan | nan | nan | Cerrado | 26.5 |
| 7b13c58e-4d6e-321a-9269-6023633005c6 | -6.16428 | -44.42606 | 2024-12-11 00:39:00 | TERRA_M-M | MIRADOR | MARANHÃO | Brasil | 2106706 | 21 | 33 | nan | nan | nan | Cerrado | 6.4 |
| e03b0a9e-c6a3-31ad-aaee-0109d6b4151b | -4.26416 | -45.99509 | 2024-12-11 00:39:00 | TERRA_M-M | SANTA LUZIA | MARANHÃO | Brasil | 2110005 | 21 | 33 | nan | nan | nan | Amazônia | 7.0 |
| 12c423bd-d9b8-34bf-863b-f90b9b76e6d4 | -5.97735 | -44.60059 | 2024-12-11 00:39:00 | TERRA_M-M | COLINAS | MARANHÃO | Brasil | 2103505 | 21 | 33 | nan | nan | nan | Cerrado | 18.8 |
| 38e9a32f-a6c5-3ea5-a8ec-04e10798b6d7 | -3.60254 | -53.72497 | 2024-12-11 00:39:00 | TERRA_M-M | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | 49.1 |
| 01521c0d-333a-3d0e-8d23-88809180ca0f | -4.76735 | -46.97555 | 2024-12-11 00:39:00 | TERRA_M-M | AÇAILÂNDIA | MARANHÃO | Brasil | 2100055 | 21 | 33 | nan | nan | nan | Amazônia | 15.1 |
| cbe676dc-57ef-3666-8680-c53b12933b3c | -3.13813 | -54.09437 | 2024-12-11 00:39:00 | TERRA_M-M | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | 43.4 |
| 0cadfcea-1185-34ee-9a38-5b85e2ab0176 | -4.48416 | -46.71926 | 2024-12-11 00:39:00 | TERRA_M-M | BOM JESUS DAS SELVAS | MARANHÃO | Brasil | 2102036 | 21 | 33 | nan | nan | nan | Amazônia | 6.3 |
| 206ec9c1-18b1-3865-be9b-6c8357e52343 | -3.60025 | -53.71992 | 2024-12-11 00:39:00 | TERRA_M-M | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | 46.5 |
| b5b5a591-a19a-3bcf-9b3c-a1f47a9614a2 | -3.15917 | -54.4767 | 2024-12-11 00:39:00 | TERRA_M-M | MOJUÍ DOS CAMPOS | PARÁ | Brasil | 1504752 | 15 | 33 | nan | nan | nan | Amazônia | 48.7 |
| 18c9c29f-bf0c-3bb9-87aa-ce886361108d | -6.10282 | -44.05246 | 2024-12-11 00:39:00 | TERRA_M-M | COLINAS | MARANHÃO | Brasil | 2103505 | 21 | 33 | nan | nan | nan | Cerrado | 24.5 |
| 1d7bfe6c-7beb-33e3-beae-de9668a49bae | -4.48285 | -46.70985 | 2024-12-11 00:39:00 | TERRA_M-M | BOM JESUS DAS SELVAS | MARANHÃO | Brasil | 2102036 | 21 | 33 | nan | nan | nan | Amazônia | 6.8 |
| 7480cfea-a58e-3392-8198-febd70c942c6 | -6.10155 | -44.04342 | 2024-12-11 00:39:00 | TERRA_M-M | COLINAS | MARANHÃO | Brasil | 2103505 | 21 | 33 | nan | nan | nan | Cerrado | 53.4 |
| b4462c61-5c8e-3abe-94d6-0566b59599df | -3.07626 | -40.04616 | 2024-12-11 00:39:00 | TERRA_M-M | ACARAÚ | CEARÁ | Brasil | 2300200 | 23 | 33 | nan | nan | nan | Caatinga | 34.5 |
| 40549ac1-37e6-33cb-ba35-122d7d05de75 | -3.80099 | -52.40162 | 2024-12-11 00:39:00 | TERRA_M-M | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 20.7 |
| 32193c03-c556-3594-bc3a-029075af79b9 | -3.34722 | -53.08526 | 2024-12-11 00:39:00 | TERRA_M-M | MEDICILÂNDIA | PARÁ | Brasil | 1504455 | 15 | 33 | nan | nan | nan | Amazônia | 25.0 |
| 4846e77b-f7ae-3263-bf9e-e68846c3accd | -11.1106 | -54.6408 | 2024-12-11 00:40:00 | GOES-16 | MARCELÂNDIA | MATO GROSSO | Brasil | 5105580 | 51 | 33 | nan | nan | nan | Amazônia | 99.1 |
| 7b446771-26bf-39db-874c-6050dbc9739f | 2.7444 | -60.6381 | 2024-12-11 00:40:00 | GOES-16 | CANTÁ | RORAIMA | Brasil | 1400175 | 14 | 33 | nan | nan | nan | Amazônia | 149.9 |
| 7309aec9-4526-3d76-9cd8-1750478c7745 | -3.1288 | -54.0853 | 2024-12-11 00:40:00 | GOES-16 | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | 77.1 |
| 005fd3f0-e0d5-32fd-9f1a-357fb54d650c | -3.8165 | -52.3813 | 2024-12-11 00:40:00 | GOES-16 | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 82.2 |
| f17f1732-f78c-325a-a74e-d4c8f0f01a38 | 2.7444 | -60.657 | 2024-12-11 00:40:00 | GOES-16 | CANTÁ | RORAIMA | Brasil | 1400175 | 14 | 33 | nan | nan | nan | Amazônia | 86.6 |
| 780dfbc9-ec03-309c-ba1f-a474e15136c3 | -18.0062 | -52.9861 | 2024-12-11 00:40:00 | GOES-16 | MINEIROS | GOIÁS | Brasil | 5213103 | 52 | 33 | nan | nan | nan | Cerrado | 77.3 |
| 7544b34f-656c-3b9c-b9ae-bbb9e9db9242 | -6.978 | -42.9977 | 2024-12-11 00:40:00 | GOES-16 | FLORIANO | PIAUÍ | Brasil | 2203909 | 22 | 33 | nan | nan | nan | Caatinga | 188.5 |
| 41bc1597-80f0-3855-8db6-db975b23df6f | -6.9592 | -42.9994 | 2024-12-11 00:40:00 | GOES-16 | FLORIANO | PIAUÍ | Brasil | 2203909 | 22 | 33 | nan | nan | nan | Caatinga | 250.3 |
| 6ac4c051-f0a9-3c15-90f2-6de73046bc6c | 2.7627 | -60.6378 | 2024-12-11 00:40:00 | GOES-16 | CANTÁ | RORAIMA | Brasil | 1400175 | 14 | 33 | nan | nan | nan | Amazônia | 156.9 |
| 0ea61544-a036-360a-be1e-d815ef75805e | -2.9666 | -53.1201 | 2024-12-11 00:40:00 | GOES-16 | MEDICILÂNDIA | PARÁ | Brasil | 1504455 | 15 | 33 | nan | nan | nan | Amazônia | 73.8 |
| c88cb293-74aa-381c-92e6-562e2620e279 | -18.0266 | -52.9614 | 2024-12-11 00:40:00 | GOES-16 | MINEIROS | GOIÁS | Brasil | 5213103 | 52 | 33 | nan | nan | nan | Cerrado | 76.1 |
| 5540ebe3-4982-3d3b-8a19-9d18bae87811 | -18.0989 | -40.1368 | 2024-12-11 00:40:00 | GOES-16 | MONTANHA | ESPÍRITO SANTO | Brasil | 3203502 | 32 | 33 | nan | nan | nan | Mata Atlântica | 141.8 |
| e56a2546-aa72-3662-8fa8-575130de6783 | -11.1295 | -54.6391 | 2024-12-11 00:40:00 | GOES-16 | MARCELÂNDIA | MATO GROSSO | Brasil | 5105580 | 51 | 33 | nan | nan | nan | Amazônia | 83.8 |
| 1b90b020-05f5-37bd-9c5a-d12d8f857db2 | -18.1192 | -40.1311 | 2024-12-11 00:40:00 | GOES-16 | MONTANHA | ESPÍRITO SANTO | Brasil | 3203502 | 32 | 33 | nan | nan | nan | Mata Atlântica | 239.3 |
| 55c14f01-158a-3013-af00-8055020daad5 | -6.897 | -43.5202 | 2024-12-11 00:40:00 | GOES-16 | JERUMENHA | PIAUÍ | Brasil | 2205300 | 22 | 33 | nan | nan | nan | Cerrado | 67.2 |
| b63531aa-5424-34be-9131-39a0a9186721 | -15.0865 | -59.6487 | 2024-12-11 00:40:00 | GOES-16 | VILA BELA DA SANTÍSSIMA TRINDADE | MATO GROSSO | Brasil | 5105507 | 51 | 33 | nan | nan | nan | Amazônia | 58.5 |
| 25b429d7-908f-3a42-98f8-2bcd0ba9df6e | -6.9403 | -43.0012 | 2024-12-11 00:40:00 | GOES-16 | FLORIANO | PIAUÍ | Brasil | 2203909 | 22 | 33 | nan | nan | nan | Caatinga | 85.0 |
| bd856fd2-8944-3eca-8deb-1cfeb3d08f0a | -3.2351 | -42.4353 | 2024-12-11 00:40:00 | GOES-16 | SÃO BERNARDO | MARANHÃO | Brasil | 2110609 | 21 | 33 | nan | nan | nan | Cerrado | 67.8 |
| 3c94a06d-3c09-3b1b-93e2-629f34582fe9 | 2.7627 | -60.6567 | 2024-12-11 00:40:00 | GOES-16 | CANTÁ | RORAIMA | Brasil | 1400175 | 14 | 33 | nan | nan | nan | Amazônia | 72.9 |
| c90b449c-4ab3-3ff7-966f-44d5c14495f6 | -6.9783 | -42.9741 | 2024-12-11 00:40:00 | GOES-16 | FLORIANO | PIAUÍ | Brasil | 2203909 | 22 | 33 | nan | nan | nan | Caatinga | 87.7 |
| a1cd6f0f-c60f-32cb-9aeb-316063f3ef3a | -18.12 | -40.1049 | 2024-12-11 00:40:00 | GOES-16 | MONTANHA | ESPÍRITO SANTO | Brasil | 3203502 | 32 | 33 | nan | nan | nan | Mata Atlântica | 74.3 |
| bc1805b9-5827-36e6-b468-ed7412f6d6da | -18.0261 | -52.9829 | 2024-12-11 00:40:00 | GOES-16 | MINEIROS | GOIÁS | Brasil | 5213103 | 52 | 33 | nan | nan | nan | Cerrado | 98.1 |
| 842cc98d-75bc-37f9-a346-5f32e7366ab4 | 3.2362 | -61.1982 | 2024-12-11 00:40:00 | GOES-16 | ALTO ALEGRE | RORAIMA | Brasil | 1400050 | 14 | 33 | nan | nan | nan | Amazônia | 59.6 |
| 3b4d3e31-6504-3128-acdd-a808d886c7c8 | -6.9594 | -42.9759 | 2024-12-11 00:40:00 | GOES-16 | FLORIANO | PIAUÍ | Brasil | 2203909 | 22 | 33 | nan | nan | nan | Caatinga | 100.0 |
| 60b25d30-3f4d-3f69-ab93-f6d6c4c7ebef | -2.9482 | -53.1206 | 2024-12-11 00:40:00 | GOES-16 | MEDICILÂNDIA | PARÁ | Brasil | 1504455 | 15 | 33 | nan | nan | nan | Amazônia | 65.8 |
| d5d37679-e29d-3032-b166-b989cd53e028 | -6.8972 | -43.4969 | 2024-12-11 00:50:00 | GOES-16 | JERUMENHA | PIAUÍ | Brasil | 2205300 | 22 | 33 | nan | nan | nan | Cerrado | 319.9 |
| 904b9f1f-09f7-3d8c-b9ff-02f18c9186ec | -6.9403 | -43.0012 | 2024-12-11 00:50:00 | GOES-16 | FLORIANO | PIAUÍ | Brasil | 2203909 | 22 | 33 | nan | nan | nan | Caatinga | 83.5 |
| 7245bc46-cbfe-3dcf-8896-5642887cc917 | -3.8165 | -52.3813 | 2024-12-11 00:50:00 | GOES-16 | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 78.1 |
| ef62811e-be42-3af4-8692-828b94aa05ab | -18.12 | -40.1049 | 2024-12-11 00:50:00 | GOES-16 | MONTANHA | ESPÍRITO SANTO | Brasil | 3203502 | 32 | 33 | nan | nan | nan | Mata Atlântica | 73.1 |
| 62d8a826-7f19-3413-ba92-c42ad44c8ff6 | 2.7444 | -60.6381 | 2024-12-11 00:50:00 | GOES-16 | CANTÁ | RORAIMA | Brasil | 1400175 | 14 | 33 | nan | nan | nan | Amazônia | 147.5 |
| cadb72fa-cda0-3459-8d0e-98b448fe2707 | -9.8597 | -35.9481 | 2024-12-11 00:50:00 | GOES-16 | ROTEIRO | ALAGOAS | Brasil | 2707800 | 27 | 33 | nan | nan | nan | Mata Atlântica | 66.0 |
| 14c353cb-11ea-3216-bad4-8427a7ca5b8f | -6.8967 | -43.5436 | 2024-12-11 00:50:00 | GOES-16 | GUADALUPE | PIAUÍ | Brasil | 2204501 | 22 | 33 | nan | nan | nan | Cerrado | 84.9 |
| a433abf8-05c3-3aba-a804-2098ec5d1aec | -6.9161 | -43.4952 | 2024-12-11 00:50:00 | GOES-16 | JERUMENHA | PIAUÍ | Brasil | 2205300 | 22 | 33 | nan | nan | nan | Cerrado | 227.3 |
| 1ed72b9b-bde1-3bdc-930e-190fd0d1e25c | -6.9592 | -42.9994 | 2024-12-11 00:50:00 | GOES-16 | FLORIANO | PIAUÍ | Brasil | 2203909 | 22 | 33 | nan | nan | nan | Caatinga | 244.9 |
| 5beca1af-2915-3c50-8358-a94639523c34 | -18.0989 | -40.1368 | 2024-12-11 00:50:00 | GOES-16 | MONTANHA | ESPÍRITO SANTO | Brasil | 3203502 | 32 | 33 | nan | nan | nan | Mata Atlântica | 184.1 |
| 587e4528-3cd9-3b13-a1f3-4055e032cd1b | -6.978 | -42.9977 | 2024-12-11 00:50:00 | GOES-16 | FLORIANO | PIAUÍ | Brasil | 2203909 | 22 | 33 | nan | nan | nan | Caatinga | 189.9 |
| e98a9f08-7a6c-3eb4-8e18-e3994352c092 | -2.9482 | -53.1206 | 2024-12-11 00:50:00 | GOES-16 | MEDICILÂNDIA | PARÁ | Brasil | 1504455 | 15 | 33 | nan | nan | nan | Amazônia | 73.1 |
| 504ac625-2cde-348c-adc1-efdbb048b1b1 | -2.9666 | -53.1201 | 2024-12-11 00:50:00 | GOES-16 | MEDICILÂNDIA | PARÁ | Brasil | 1504455 | 15 | 33 | nan | nan | nan | Amazônia | 78.5 |
| 189d95fb-79bd-32c7-93f9-ed712750075d | -15.0865 | -59.6487 | 2024-12-11 00:50:00 | GOES-16 | VILA BELA DA SANTÍSSIMA TRINDADE | MATO GROSSO | Brasil | 5105507 | 51 | 33 | nan | nan | nan | Amazônia | 69.8 |
| 5bc09b93-b8b0-36f2-b9b8-5e23d0c898d3 | 2.7444 | -60.657 | 2024-12-11 00:50:00 | GOES-16 | CANTÁ | RORAIMA | Brasil | 1400175 | 14 | 33 | nan | nan | nan | Amazônia | 83.4 |
| 07a95a82-b2e9-3dcc-b2b7-34c11600e89b | -6.9594 | -42.9759 | 2024-12-11 00:50:00 | GOES-16 | FLORIANO | PIAUÍ | Brasil | 2203909 | 22 | 33 | nan | nan | nan | Caatinga | 99.5 |
| 751e7f39-8a0b-3561-b211-1808f3c7a1d1 | 2.7627 | -60.6378 | 2024-12-11 00:50:00 | GOES-16 | CANTÁ | RORAIMA | Brasil | 1400175 | 14 | 33 | nan | nan | nan | Amazônia | 118.7 |
| 8c96048f-28bd-3cf2-8cf8-f26ae8f0ed61 | -15.971 | -57.1669 | 2024-12-11 00:50:00 | GOES-16 | CÁCERES | MATO GROSSO | Brasil | 5102504 | 51 | 33 | nan | nan | nan | Cerrado | 52.5 |


[Clique aqui para ver as próximas entradas](README5.md)
