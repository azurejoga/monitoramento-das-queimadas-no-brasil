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

## Dados Diários - Página 66

| ID | Latitude | Longitude | Data/Hora GMT | Satélite | Município | Estado | País | Município ID | Estado ID | País ID | Dias sem Chuva | Precipitação | Risco de Fogo | Bioma | FRP |
|----|----------|-----------|---------------|----------|-----------|--------|------|--------------|-----------|---------|----------------|--------------|----------------|-------|-----|
| 6441f042-f176-3f0f-9642-3d77d9b62c76 | -8.7945 | -45.4693 | 2025-08-20 14:40:00 | GOES-19 | SANTA FILOMENA | PIAUÍ | Brasil | 2209203 | 22 | 33 | nan | nan | nan | Cerrado | 203.2 |
| 0e8a2c1d-9653-3eea-968d-604b7cd66a09 | -6.0025 | -42.8251 | 2025-08-20 14:40:00 | GOES-19 | PALMEIRAIS | PIAUÍ | Brasil | 2207504 | 22 | 33 | nan | nan | nan | Caatinga | 88.0 |
| 948bf667-df7d-3920-86c3-222b376cb410 | -15.0196 | -54.8112 | 2025-08-20 14:40:00 | GOES-19 | NOVA BRASILÂNDIA | MATO GROSSO | Brasil | 5106208 | 51 | 33 | nan | nan | nan | Cerrado | 55.4 |
| d7ed1662-7a9f-376a-a978-1baba850798f | -6.4454 | -45.4846 | 2025-08-20 14:40:00 | GOES-19 | MIRADOR | MARANHÃO | Brasil | 2106706 | 21 | 33 | nan | nan | nan | Cerrado | 139.5 |
| cfa8920a-2803-3bc6-911a-057c44bd86ea | -8.2234 | -44.4092 | 2025-08-20 14:40:00 | GOES-19 | URUÇUÍ | PIAUÍ | Brasil | 2211209 | 22 | 33 | nan | nan | nan | Cerrado | 84.7 |
| 0c42cfbd-2b6f-38b8-857d-30cc6835d629 | -12.9546 | -46.1732 | 2025-08-20 14:40:00 | GOES-19 | CAMPOS BELOS | GOIÁS | Brasil | 5204904 | 52 | 33 | nan | nan | nan | Cerrado | 50.5 |
| d20dbfd7-8bbb-374b-925f-cc985087ef4a | -6.4451 | -45.5072 | 2025-08-20 14:40:00 | GOES-19 | MIRADOR | MARANHÃO | Brasil | 2106706 | 21 | 33 | nan | nan | nan | Cerrado | 166.7 |
| c0701b41-2262-3207-b65f-7dec5688cbe4 | -8.7948 | -45.4465 | 2025-08-20 14:40:00 | GOES-19 | SANTA FILOMENA | PIAUÍ | Brasil | 2209203 | 22 | 33 | nan | nan | nan | Cerrado | 65.6 |
| a4b117d2-82e9-3827-9f71-1a0f8a33db5f | -12.8984 | -46.0906 | 2025-08-20 14:40:00 | GOES-19 | SÃO DESIDÉRIO | BAHIA | Brasil | 2928901 | 29 | 33 | nan | nan | nan | Cerrado | 54.5 |
| e5449f9d-7157-3a18-9f05-464d726e034f | -15.0002 | -54.8135 | 2025-08-20 14:40:00 | GOES-19 | NOVA BRASILÂNDIA | MATO GROSSO | Brasil | 5106208 | 51 | 33 | nan | nan | nan | Cerrado | 70.5 |
| fb0d17c9-25e4-3c63-889b-4c0d526b439c | -13.1265 | -57.1494 | 2025-08-20 14:40:00 | GOES-19 | NOVA MARINGÁ | MATO GROSSO | Brasil | 5108907 | 51 | 33 | nan | nan | nan | Amazônia | 70.0 |
| dab7913a-6d20-326d-b9a1-bac1d4f0ca15 | -13.1367 | -54.9171 | 2025-08-20 14:40:00 | GOES-19 | NOVA UBIRATÃ | MATO GROSSO | Brasil | 5106240 | 51 | 33 | nan | nan | nan | Amazônia | 108.2 |
| cfc0d7af-1938-399e-a6e8-6de89791a650 | -9.1709 | -59.6374 | 2025-08-20 14:40:00 | GOES-19 | COLNIZA | MATO GROSSO | Brasil | 5103254 | 51 | 33 | nan | nan | nan | Amazônia | 62.0 |
| aeb7ffa6-b643-3040-9bd6-3cb714660e8d | -3.982 | -42.516 | 2025-08-20 14:40:00 | GOES-19 | CAMPO LARGO DO PIAUÍ | PIAUÍ | Brasil | 2202174 | 22 | 33 | nan | nan | nan | Caatinga | 147.2 |
| cb8bac0d-179e-34a5-a735-6c5fd22a5d16 | -6.63 | -43.8925 | 2025-08-20 14:40:00 | GOES-19 | NOVA IORQUE | MARANHÃO | Brasil | 2107308 | 21 | 33 | nan | nan | nan | Cerrado | 107.7 |
| 8be0b28e-9286-38e0-a422-33cd19e5d26e | -12.978 | -56.8413 | 2025-08-20 14:40:00 | GOES-19 | NOVA MARINGÁ | MATO GROSSO | Brasil | 5108907 | 51 | 33 | nan | nan | nan | Amazônia | 59.1 |
| c43ec620-d9f2-3bb9-b887-d45093ce5aa0 | -7.2602 | -50.1613 | 2025-08-20 14:40:00 | GOES-19 | RIO MARIA | PARÁ | Brasil | 1506161 | 15 | 33 | nan | nan | nan | Amazônia | 75.4 |
| 4300e9f8-a6d6-300b-a6b8-b2dcb99daae3 | -12.9775 | -56.8816 | 2025-08-20 14:40:00 | GOES-19 | NOVA MARINGÁ | MATO GROSSO | Brasil | 5108907 | 51 | 33 | nan | nan | nan | Amazônia | 58.6 |
| a378a453-1ccc-34a1-8815-4c6db3b408f8 | -11.011 | -45.6105 | 2025-08-20 14:40:00 | GOES-19 | FORMOSA DO RIO PRETO | BAHIA | Brasil | 2911105 | 29 | 33 | nan | nan | nan | Cerrado | 207.1 |
| 7bd4b432-436b-31f7-8b37-23b4d004f9e1 | -12.898 | -46.1135 | 2025-08-20 14:40:00 | GOES-19 | SÃO DESIDÉRIO | BAHIA | Brasil | 2928901 | 29 | 33 | nan | nan | nan | Cerrado | 49.9 |
| ff3727c1-ae19-35a1-8145-a4d561089b3c | -13.0162 | -56.8378 | 2025-08-20 14:40:00 | GOES-19 | NOVA MARINGÁ | MATO GROSSO | Brasil | 5108907 | 51 | 33 | nan | nan | nan | Amazônia | 56.2 |
| 16e93489-d177-3eb1-adbb-353fb9a070b6 | -12.9778 | -56.8614 | 2025-08-20 14:40:00 | GOES-19 | NOVA MARINGÁ | MATO GROSSO | Brasil | 5108907 | 51 | 33 | nan | nan | nan | Amazônia | 87.6 |
| 8d4468b8-3fe5-39b1-ba1e-724b7695df1a | -8.6343 | -62.1367 | 2025-08-20 14:40:00 | GOES-19 | HUMAITÁ | AMAZONAS | Brasil | 1301704 | 13 | 33 | nan | nan | nan | Amazônia | 65.1 |
| d11bb356-5c56-3cdb-b954-388386be06d4 | -6.4264 | -45.5087 | 2025-08-20 14:40:00 | GOES-19 | FERNANDO FALCÃO | MARANHÃO | Brasil | 2104081 | 21 | 33 | nan | nan | nan | Cerrado | 82.2 |
| d9b38630-8421-3446-aece-555c06a16a54 | -13.0387 | -46.819 | 2025-08-20 14:40:00 | GOES-19 | CAMPOS BELOS | GOIÁS | Brasil | 5204904 | 52 | 33 | nan | nan | nan | Cerrado | 56.4 |
| 89c3c1ad-85ea-36ad-b6fa-065ff0fc9c37 | -13.1364 | -54.9376 | 2025-08-20 14:40:00 | GOES-19 | NOVA UBIRATÃ | MATO GROSSO | Brasil | 5106240 | 51 | 33 | nan | nan | nan | Amazônia | 106.8 |
| 9c03ab70-a1f8-3eb1-967e-6c4546edf824 | -6.5416 | -53.9102 | 2025-08-20 14:40:00 | GOES-19 | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 85.8 |
| 620f197d-ac94-3047-88a1-2ee38bdc86e9 | -5.7971 | -44.7628 | 2025-08-20 14:40:00 | GOES-19 | TUNTUM | MARANHÃO | Brasil | 2112308 | 21 | 33 | nan | nan | nan | Cerrado | 140.6 |
| 67a3bd1b-6762-3d51-bb6c-0c4894fb896b | -13.1555 | -54.9357 | 2025-08-20 14:40:00 | GOES-19 | NOVA UBIRATÃ | MATO GROSSO | Brasil | 5106240 | 51 | 33 | nan | nan | nan | Amazônia | 129.8 |
| f15c2a32-e1d7-3a67-b201-a65b0e337e0c | -11.3087 | -44.9264 | 2025-08-20 14:40:00 | GOES-19 | SANTA RITA DE CÁSSIA | BAHIA | Brasil | 2928406 | 29 | 33 | nan | nan | nan | Cerrado | 93.7 |
| 57dd17d1-5cab-37fb-9205-b87e364a1ae2 | -8.297 | -47.64 | 2025-08-20 14:40:00 | GOES-19 | GOIATINS | TOCANTINS | Brasil | 1709005 | 17 | 33 | nan | nan | nan | Cerrado | 84.9 |
| 14ab9dec-b60f-353b-9e2b-e73ecbd429a5 | -5.9713 | -44.1312 | 2025-08-20 14:40:00 | GOES-19 | COLINAS | MARANHÃO | Brasil | 2103505 | 21 | 33 | nan | nan | nan | Cerrado | 101.6 |
| fdebb718-f705-3dcf-977c-0cf811ee746b | -7.0169 | -44.5954 | 2025-08-20 14:40:00 | GOES-19 | BENEDITO LEITE | MARANHÃO | Brasil | 2101806 | 21 | 33 | nan | nan | nan | Cerrado | 104.5 |
| 5b1bdbd6-30f8-3236-98cf-6683246b90e0 | -14.6326 | -54.8773 | 2025-08-20 14:40:00 | GOES-19 | PLANALTO DA SERRA | MATO GROSSO | Brasil | 5106455 | 51 | 33 | nan | nan | nan | Cerrado | 71.9 |
| c831cf84-babe-3749-8d74-430bc932d060 | -12.9732 | -45.2051 | 2025-08-20 14:40:00 | GOES-19 | SÃO DESIDÉRIO | BAHIA | Brasil | 2928901 | 29 | 33 | nan | nan | nan | Cerrado | 144.8 |
| e42a3707-e6f4-389a-9f88-1da74b929378 | -5.9711 | -44.1542 | 2025-08-20 14:40:00 | GOES-19 | COLINAS | MARANHÃO | Brasil | 2103505 | 21 | 33 | nan | nan | nan | Cerrado | 171.5 |
| 8aa539c6-4b26-3be0-ae2a-223a973bde60 | -13.1558 | -54.9151 | 2025-08-20 14:40:00 | GOES-19 | NOVA UBIRATÃ | MATO GROSSO | Brasil | 5106240 | 51 | 33 | nan | nan | nan | Amazônia | 149.7 |
| b9da3c1f-b75b-3ad8-ae37-d72c5db6fe4b | -6.2753 | -43.7139 | 2025-08-20 14:40:00 | GOES-19 | PASSAGEM FRANCA | MARANHÃO | Brasil | 2107902 | 21 | 33 | nan | nan | nan | Cerrado | 95.7 |
| 439605bf-8dcf-39de-bfda-caeb29d1e914 | -8.5556 | -66.9389 | 2025-08-20 14:40:00 | GOES-19 | LÁBREA | AMAZONAS | Brasil | 1302405 | 13 | 33 | nan | nan | nan | Amazônia | 65.1 |
| 072ab624-81f3-38cd-8ca4-aa378e2c63b7 | -12.1952 | -50.2181 | 2025-08-20 14:40:00 | GOES-19 | FORMOSO DO ARAGUAIA | TOCANTINS | Brasil | 1708205 | 17 | 33 | nan | nan | nan | Cerrado | 45.4 |
| 645c2d55-5ae4-38f4-abe4-ac79ea0026fc | -12.9173 | -46.1106 | 2025-08-20 14:40:00 | GOES-19 | SÃO DESIDÉRIO | BAHIA | Brasil | 2928901 | 29 | 33 | nan | nan | nan | Cerrado | 59.9 |
| e45bd35d-fdc4-3380-8692-29407db57349 | -5.7969 | -44.7856 | 2025-08-20 14:40:00 | GOES-19 | TUNTUM | MARANHÃO | Brasil | 2112308 | 21 | 33 | nan | nan | nan | Cerrado | 97.6 |
| 11cdc8bc-06e6-3fcf-a4a7-8046c21df2db | -6.081 | -44.4214 | 2025-08-20 14:40:00 | GOES-19 | MIRADOR | MARANHÃO | Brasil | 2106706 | 21 | 33 | nan | nan | nan | Cerrado | 93.1 |
| 50f1180d-c34f-35e8-8cd7-500df67bb98f | -10.7043 | -48.2226 | 2025-08-20 14:40:00 | GOES-19 | PORTO NACIONAL | TOCANTINS | Brasil | 1718204 | 17 | 33 | nan | nan | nan | Cerrado | 100.6 |
| 57ae54f7-a7a4-3e41-a12f-1db662e88402 | -7.26 | -50.1825 | 2025-08-20 14:40:00 | GOES-19 | RIO MARIA | PARÁ | Brasil | 1506161 | 15 | 33 | nan | nan | nan | Amazônia | 89.7 |
| 52422e3c-1791-32b6-aa53-dc070930d1bb | -9.152 | -59.6772 | 2025-08-20 14:40:00 | GOES-19 | COLNIZA | MATO GROSSO | Brasil | 5103254 | 51 | 33 | nan | nan | nan | Amazônia | 55.3 |
| d3a863a8-7879-3283-bccc-4bb130dd71ee | -8.6901 | -62.0963 | 2025-08-20 14:40:00 | GOES-19 | HUMAITÁ | AMAZONAS | Brasil | 1301704 | 13 | 33 | nan | nan | nan | Amazônia | 56.8 |


