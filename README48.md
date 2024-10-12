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

## Dados Diários - Página 48

| ID | Latitude | Longitude | Data/Hora GMT | Satélite | Município | Estado | País | Município ID | Estado ID | País ID | Dias sem Chuva | Precipitação | Risco de Fogo | Bioma | FRP |
|----|----------|-----------|---------------|----------|-----------|--------|------|--------------|-----------|---------|----------------|--------------|----------------|-------|-----|
| cf859967-489c-372d-a04a-c8469305cdfa | -3.8159 | -52.34713 | 2024-10-12 04:06:00 | NOAA-20 | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 0.9 |
| 53777196-7647-3eef-93cd-fd8578d3625f | -10.9506 | -44.653 | 2024-10-12 04:06:08 | GOES-16 | SANTA RITA DE CÁSSIA | BAHIA | Brasil | 2928406 | 29 | 33 | nan | nan | nan | Cerrado | 80.0 |
| 32909670-6e38-317e-8c4d-bca2122d7f2a | -11.8377 | -58.8445 | 2024-10-12 04:06:14 | GOES-16 | JUÍNA | MATO GROSSO | Brasil | 5105150 | 51 | 33 | nan | nan | nan | Cerrado | 91.0 |
| 6edd7698-78af-36d3-8129-2d33beb608d6 | -12.456 | -54.5554 | 2024-10-12 04:06:17 | GOES-16 | FELIZ NATAL | MATO GROSSO | Brasil | 5103700 | 51 | 33 | nan | nan | nan | Amazônia | 118.2 |
| 6a79639b-53b4-3f6c-8e17-e560411fd349 | -12.4558 | -54.576 | 2024-10-12 04:06:17 | GOES-16 | FELIZ NATAL | MATO GROSSO | Brasil | 5103700 | 51 | 33 | nan | nan | nan | Amazônia | 105.3 |
| b20017d7-129e-330f-a882-05b32ec0f1e3 | -12.437 | -54.5573 | 2024-10-12 04:06:17 | GOES-16 | FELIZ NATAL | MATO GROSSO | Brasil | 5103700 | 51 | 33 | nan | nan | nan | Amazônia | 71.2 |
| d8312f7e-8415-3170-b8f0-24d03f16d509 | -12.4367 | -54.5778 | 2024-10-12 04:06:17 | GOES-16 | FELIZ NATAL | MATO GROSSO | Brasil | 5103700 | 51 | 33 | nan | nan | nan | Amazônia | 71.5 |
| f620446f-f374-361b-a88e-adac4703c021 | -12.8893 | -53.5194 | 2024-10-12 04:06:19 | GOES-16 | GAÚCHA DO NORTE | MATO GROSSO | Brasil | 5103858 | 51 | 33 | nan | nan | nan | Amazônia | 71.5 |
| f6228058-4166-32a4-8ab7-da39f15bffc4 | -12.9652 | -53.5527 | 2024-10-12 04:06:20 | GOES-16 | GAÚCHA DO NORTE | MATO GROSSO | Brasil | 5103858 | 51 | 33 | nan | nan | nan | Amazônia | 73.5 |
| 56a1a387-5753-3bcc-aad3-51e12022601f | -12.9464 | -53.5339 | 2024-10-12 04:06:20 | GOES-16 | GAÚCHA DO NORTE | MATO GROSSO | Brasil | 5103858 | 51 | 33 | nan | nan | nan | Amazônia | 180.4 |
| bc68553e-9662-3bcf-bc6c-24205a337b2b | -12.9461 | -53.5548 | 2024-10-12 04:06:20 | GOES-16 | GAÚCHA DO NORTE | MATO GROSSO | Brasil | 5103858 | 51 | 33 | nan | nan | nan | Amazônia | 65.8 |
| 8bdd6a75-6486-3fca-9ca6-56f36866d612 | -12.9467 | -53.5131 | 2024-10-12 04:06:20 | GOES-16 | GAÚCHA DO NORTE | MATO GROSSO | Brasil | 5103858 | 51 | 33 | nan | nan | nan | Amazônia | 131.4 |
| 76524d9c-3051-3ab4-9384-f02fa94066a3 | -12.9658 | -53.511 | 2024-10-12 04:06:20 | GOES-16 | GAÚCHA DO NORTE | MATO GROSSO | Brasil | 5103858 | 51 | 33 | nan | nan | nan | Amazônia | 141.8 |
| 770114e0-f893-3754-8167-732c6ea4fbf0 | -12.9655 | -53.5319 | 2024-10-12 04:06:20 | GOES-16 | GAÚCHA DO NORTE | MATO GROSSO | Brasil | 5103858 | 51 | 33 | nan | nan | nan | Amazônia | 212.2 |
| 9ee55417-ba39-35cc-a160-1c76c066fa8e | -16.9805 | -57.4404 | 2024-10-12 04:06:42 | GOES-16 | CÁCERES | MATO GROSSO | Brasil | 5102504 | 51 | 33 | nan | nan | nan | Pantanal | 65.1 |
| ec1d9b4a-d0b2-3b7f-b404-098e4326ed8e | -17.1761 | -57.4585 | 2024-10-12 04:06:43 | GOES-16 | CÁCERES | MATO GROSSO | Brasil | 5102504 | 51 | 33 | nan | nan | nan | Pantanal | 88.0 |
| e90de912-4383-3ad1-abb4-12fb364333c2 | -17.6467 | -56.3292 | 2024-10-12 04:06:45 | GOES-16 | CORUMBÁ | MATO GROSSO DO SUL | Brasil | 5003207 | 50 | 33 | nan | nan | nan | Pantanal | 103.0 |
| d773e3ef-e330-3662-bbb4-77762c03d92a | -17.6679 | -56.2435 | 2024-10-12 04:06:46 | GOES-16 | CORUMBÁ | MATO GROSSO DO SUL | Brasil | 5003207 | 50 | 33 | nan | nan | nan | Pantanal | 65.8 |
| b77e5a30-fca0-3ce6-9ced-468dc5adb347 | -17.9837 | -57.3819 | 2024-10-12 04:06:47 | GOES-16 | CORUMBÁ | MATO GROSSO DO SUL | Brasil | 5003207 | 50 | 33 | nan | nan | nan | Pantanal | 50.6 |
| fcb61d1f-e56e-3ac8-a478-e1686357b45f | -17.9841 | -57.3612 | 2024-10-12 04:06:47 | GOES-16 | CORUMBÁ | MATO GROSSO DO SUL | Brasil | 5003207 | 50 | 33 | nan | nan | nan | Pantanal | 42.8 |
| 70bf2fbc-0abd-3b41-8c0c-c27a3abd1b52 | -18.1956 | -56.5483 | 2024-10-12 04:06:48 | GOES-16 | CORUMBÁ | MATO GROSSO DO SUL | Brasil | 5003207 | 50 | 33 | nan | nan | nan | Pantanal | 69.1 |
| b0867aed-d96b-3947-ae12-7d83951ed8f5 | -14.32631 | -57.6011 | 2024-10-12 04:08:00 | NOAA-20 | NOVA MARILÂNDIA | MATO GROSSO | Brasil | 5108857 | 51 | 33 | nan | nan | nan | Amazônia | 6.8 |
| a6145740-4e1d-319d-a47f-4f0c54d15000 | -14.32457 | -57.60896 | 2024-10-12 04:08:00 | NOAA-20 | NOVA MARILÂNDIA | MATO GROSSO | Brasil | 5108857 | 51 | 33 | nan | nan | nan | Amazônia | 5.3 |
| 6bf4d445-bbcc-3fa8-b14a-29c5041f602d | -14.31927 | -57.59948 | 2024-10-12 04:08:00 | NOAA-20 | NOVA MARILÂNDIA | MATO GROSSO | Brasil | 5108857 | 51 | 33 | nan | nan | nan | Amazônia | 6.8 |
| 8d234328-4d14-3e14-ad2e-c54a2ba367d4 | -14.31753 | -57.6073 | 2024-10-12 04:08:00 | NOAA-20 | NOVA MARILÂNDIA | MATO GROSSO | Brasil | 5108857 | 51 | 33 | nan | nan | nan | Amazônia | 5.3 |
| 2369c462-83c9-3127-a1f1-86d33ad7dab7 | -14.31219 | -57.59799 | 2024-10-12 04:08:00 | NOAA-20 | NOVA MARILÂNDIA | MATO GROSSO | Brasil | 5108857 | 51 | 33 | nan | nan | nan | Amazônia | 4.8 |
| 6618fbd8-aa64-334e-86a7-69fff4aff9e2 | -12.81336 | -44.88113 | 2024-10-12 04:08:00 | NOAA-20 | SÃO DESIDÉRIO | BAHIA | Brasil | 2928901 | 29 | 33 | nan | nan | nan | Cerrado | 3.4 |
| 36d5b3fc-776a-31e0-9287-f73aeedbedb1 | -12.81273 | -44.88491 | 2024-10-12 04:08:00 | NOAA-20 | SÃO DESIDÉRIO | BAHIA | Brasil | 2928901 | 29 | 33 | nan | nan | nan | Cerrado | 3.5 |
| 26f89a4b-2e72-3ba4-bb5b-f029a49be9e3 | -12.80932 | -44.88433 | 2024-10-12 04:08:00 | NOAA-20 | SÃO DESIDÉRIO | BAHIA | Brasil | 2928901 | 29 | 33 | nan | nan | nan | Cerrado | 1.5 |
| 4cfeb698-420b-3c4d-85a5-eabadfee1970 | -12.80869 | -44.8881 | 2024-10-12 04:08:00 | NOAA-20 | SÃO DESIDÉRIO | BAHIA | Brasil | 2928901 | 29 | 33 | nan | nan | nan | Cerrado | 1.5 |
| 79e2568c-243c-3eea-806d-b43f1bf07e65 | -12.80841 | -44.86864 | 2024-10-12 04:08:00 | NOAA-20 | SÃO DESIDÉRIO | BAHIA | Brasil | 2928901 | 29 | 33 | nan | nan | nan | Cerrado | 1.6 |
| b118bd65-3ef1-31ca-ad2e-de995b6a0584 | -12.80499 | -44.86806 | 2024-10-12 04:08:00 | NOAA-20 | SÃO DESIDÉRIO | BAHIA | Brasil | 2928901 | 29 | 33 | nan | nan | nan | Cerrado | 2.0 |
| 52658fa9-b152-391d-8fc7-fcbeffd1a521 | -12.80402 | -44.89508 | 2024-10-12 04:08:00 | NOAA-20 | SÃO DESIDÉRIO | BAHIA | Brasil | 2928901 | 29 | 33 | nan | nan | nan | Cerrado | 3.9 |
| cca88885-21a2-3b59-8c09-7046441472be | -13.14618 | -43.37347 | 2024-10-12 04:08:00 | NOAA-20 | BOM JESUS DA LAPA | BAHIA | Brasil | 2903904 | 29 | 33 | nan | nan | nan | Cerrado | 2.4 |
| 83d7a51a-0aec-3ac7-a48a-fa6f2ebc61e8 | -13.14562 | -43.37701 | 2024-10-12 04:08:00 | NOAA-20 | BOM JESUS DA LAPA | BAHIA | Brasil | 2903904 | 29 | 33 | nan | nan | nan | Cerrado | 2.4 |
| 715c9d4f-e5cc-309a-ab42-5271fc61468b | -13.18997 | -43.50412 | 2024-10-12 04:08:00 | NOAA-20 | BOM JESUS DA LAPA | BAHIA | Brasil | 2903904 | 29 | 33 | nan | nan | nan | Cerrado | 3.9 |
| 31f2d935-7bba-3867-88ae-4b4d9c4d40bb | -18.15938 | -42.44205 | 2024-10-12 04:08:00 | NOAA-20 | SANTA MARIA DO SUAÇUÍ | MINAS GERAIS | Brasil | 3158201 | 31 | 33 | nan | nan | nan | Mata Atlântica | 0.9 |
| 443bad9d-ff3c-3068-8961-c30f700f091c | -18.15882 | -42.44586 | 2024-10-12 04:08:00 | NOAA-20 | SANTA MARIA DO SUAÇUÍ | MINAS GERAIS | Brasil | 3158201 | 31 | 33 | nan | nan | nan | Mata Atlântica | 0.6 |
| d2f35987-0f16-37c0-8a62-5bc19aaf97f0 | -14.133 | -41.69109 | 2024-10-12 04:08:00 | NOAA-20 | BRUMADO | BAHIA | Brasil | 2904605 | 29 | 33 | nan | nan | nan | Caatinga | 0.8 |
| 7ef6989b-ab6e-3520-a697-2850a57a0ea2 | -14.12121 | -41.67751 | 2024-10-12 04:08:00 | NOAA-20 | BRUMADO | BAHIA | Brasil | 2904605 | 29 | 33 | nan | nan | nan | Caatinga | 0.6 |
| 08903cd0-845d-33b4-8588-57c94ad2ef65 | -12.87153 | -42.46091 | 2024-10-12 04:08:00 | NOAA-20 | IBIPITANGA | BAHIA | Brasil | 2912509 | 29 | 33 | nan | nan | nan | Caatinga | 0.6 |
| bc649ad6-a44b-362d-8220-b1585bf1ff3b | -12.20642 | -38.24923 | 2024-10-12 04:08:00 | NOAA-20 | ARAÇÁS | BAHIA | Brasil | 2902054 | 29 | 33 | nan | nan | nan | Mata Atlântica | 1.5 |
| 315913a6-fd7d-326c-8d96-a50eae7a8772 | -12.32152 | -45.32734 | 2024-10-12 04:08:00 | NOAA-20 | BARREIRAS | BAHIA | Brasil | 2903201 | 29 | 33 | nan | nan | nan | Cerrado | 3.0 |
| 0b5bbb06-7f34-3d86-b97d-196ee519df53 | -12.80221 | -44.86371 | 2024-10-12 04:08:00 | NOAA-20 | SÃO DESIDÉRIO | BAHIA | Brasil | 2928901 | 29 | 33 | nan | nan | nan | Cerrado | 2.3 |
| f36a5dca-4788-31b2-8eeb-660588bfff7e | -14.71134 | -40.36811 | 2024-10-12 04:08:00 | NOAA-20 | PLANALTO | BAHIA | Brasil | 2925006 | 29 | 33 | nan | nan | nan | Mata Atlântica | 1.1 |
| 1b50c3cb-133b-3ef0-973e-f4c0aec8d5a4 | -14.22786 | -39.75409 | 2024-10-12 04:08:00 | NOAA-20 | ITAGIBÁ | BAHIA | Brasil | 2915205 | 29 | 33 | nan | nan | nan | Mata Atlântica | 3.0 |
| eb64f3f9-a7b8-3ed6-bb3a-d3f17bfeb6e4 | -14.22723 | -39.75846 | 2024-10-12 04:08:00 | NOAA-20 | ITAGIBÁ | BAHIA | Brasil | 2915205 | 29 | 33 | nan | nan | nan | Mata Atlântica | 3.0 |
| 5e9350eb-f813-3855-b5c8-bab15932f88f | -14.22714 | -39.75691 | 2024-10-12 04:08:00 | NOAA-20 | ITAGIBÁ | BAHIA | Brasil | 2915205 | 29 | 33 | nan | nan | nan | Mata Atlântica | 4.1 |
| a0456517-f18c-3987-8704-88322e326e92 | -14.22653 | -39.76129 | 2024-10-12 04:08:00 | NOAA-20 | ITAGIBÁ | BAHIA | Brasil | 2915205 | 29 | 33 | nan | nan | nan | Mata Atlântica | 1.3 |
| 66c8af98-5e66-327d-a9e5-606d9f8ed2a8 | -14.22357 | -39.75792 | 2024-10-12 04:08:00 | NOAA-20 | ITAGIBÁ | BAHIA | Brasil | 2915205 | 29 | 33 | nan | nan | nan | Mata Atlântica | 3.0 |
| f5e947a5-3efd-33c8-a58c-925f8866dbad | -14.22293 | -39.7623 | 2024-10-12 04:08:00 | NOAA-20 | ITAGIBÁ | BAHIA | Brasil | 2915205 | 29 | 33 | nan | nan | nan | Mata Atlântica | 2.0 |
| 5ad53ef0-4d8f-3ad8-85a1-b9a934cab3af | -13.6409 | -41.35777 | 2024-10-12 04:08:00 | NOAA-20 | BARRA DA ESTIVA | BAHIA | Brasil | 2902807 | 29 | 33 | nan | nan | nan | Caatinga | 1.3 |
| 6ed84fa8-39e1-3b54-b606-3043aa1af918 | -13.46583 | -40.8422 | 2024-10-12 04:08:00 | NOAA-20 | IRAMAIA | BAHIA | Brasil | 2914307 | 29 | 33 | nan | nan | nan | Caatinga | 4.6 |
| a120a9b6-b74d-3406-8bd5-dd6bbaec1351 | -13.46525 | -40.84611 | 2024-10-12 04:08:00 | NOAA-20 | IRAMAIA | BAHIA | Brasil | 2914307 | 29 | 33 | nan | nan | nan | Caatinga | 4.6 |
| 840e1aa3-2ae4-3956-baa2-88621bd78cb7 | -13.46237 | -40.84167 | 2024-10-12 04:08:00 | NOAA-20 | IRAMAIA | BAHIA | Brasil | 2914307 | 29 | 33 | nan | nan | nan | Caatinga | 0.8 |
| 112a4871-c791-3282-bdf9-e8b050bcb60b | -13.88216 | -41.66315 | 2024-10-12 04:08:00 | NOAA-20 | DOM BASÍLIO | BAHIA | Brasil | 2910107 | 29 | 33 | nan | nan | nan | Caatinga | 2.0 |
| 1216b9a1-42a3-3b0d-90fe-78abba8ed809 | -15.03331 | -41.66036 | 2024-10-12 04:08:00 | NOAA-20 | PIRIPÁ | BAHIA | Brasil | 2924702 | 29 | 33 | nan | nan | nan | Mata Atlântica | 0.9 |
| 4b928e5e-459f-3fa3-9ac2-bca3f12ec8a7 | -16.12552 | -41.62893 | 2024-10-12 04:08:00 | NOAA-20 | MEDINA | MINAS GERAIS | Brasil | 3141405 | 31 | 33 | nan | nan | nan | Mata Atlântica | 1.4 |
| eac280df-b8a4-3735-b6e8-a594fbc018b5 | -16.12252 | -41.62893 | 2024-10-12 04:08:00 | NOAA-20 | MEDINA | MINAS GERAIS | Brasil | 3141405 | 31 | 33 | nan | nan | nan | Mata Atlântica | 3.6 |
| c912879c-d476-37a1-8c70-4453753e0d05 | -15.263 | -41.76545 | 2024-10-12 04:08:00 | NOAA-20 | NINHEIRA | MINAS GERAIS | Brasil | 3144656 | 31 | 33 | nan | nan | nan | Mata Atlântica | 0.4 |
| ea6af7fc-b66f-35a1-9441-928311598c4c | -15.26244 | -41.76925 | 2024-10-12 04:08:00 | NOAA-20 | NINHEIRA | MINAS GERAIS | Brasil | 3144656 | 31 | 33 | nan | nan | nan | Mata Atlântica | 0.4 |
| 491fd87f-cf8c-3d2e-82d8-6de4df05e985 | -17.77906 | -42.80843 | 2024-10-12 04:08:00 | NOAA-20 | ITAMARANDIBA | MINAS GERAIS | Brasil | 3132503 | 31 | 33 | nan | nan | nan | Cerrado | 1.1 |
| a4457c52-b021-3633-b595-16a27fb37ae6 | -17.7785 | -42.81214 | 2024-10-12 04:08:00 | NOAA-20 | ITAMARANDIBA | MINAS GERAIS | Brasil | 3132503 | 31 | 33 | nan | nan | nan | Cerrado | 0.8 |
| 90d47f4d-ae11-3d3f-be73-ef01a5f4d5af | -17.75219 | -42.8952 | 2024-10-12 04:08:00 | NOAA-20 | ITAMARANDIBA | MINAS GERAIS | Brasil | 3132503 | 31 | 33 | nan | nan | nan | Cerrado | 0.7 |
| 1a0d7312-a5d4-3372-a52c-4265bd475a3e | -17.67702 | -42.74229 | 2024-10-12 04:08:00 | NOAA-20 | ITAMARANDIBA | MINAS GERAIS | Brasil | 3132503 | 31 | 33 | nan | nan | nan | Cerrado | 0.9 |
| beedeacf-2f00-34ee-814f-54ff02024c83 | -17.54782 | -42.3014 | 2024-10-12 04:08:00 | NOAA-20 | MINAS NOVAS | MINAS GERAIS | Brasil | 3141801 | 31 | 33 | nan | nan | nan | Cerrado | 1.5 |
| 00dfc5f7-62f7-3eec-9101-d860c18cd440 | -17.54725 | -42.30522 | 2024-10-12 04:08:00 | NOAA-20 | MINAS NOVAS | MINAS GERAIS | Brasil | 3141801 | 31 | 33 | nan | nan | nan | Cerrado | 16.6 |
| 864be177-4711-3903-bd2c-7fab8f5b4150 | -17.54441 | -42.3009 | 2024-10-12 04:08:00 | NOAA-20 | MINAS NOVAS | MINAS GERAIS | Brasil | 3141801 | 31 | 33 | nan | nan | nan | Cerrado | 1.5 |
| 8edeee13-d753-31d0-b953-c0ef8c44410a | -17.54385 | -42.30472 | 2024-10-12 04:08:00 | NOAA-20 | MINAS NOVAS | MINAS GERAIS | Brasil | 3141801 | 31 | 33 | nan | nan | nan | Cerrado | 16.6 |
| 79af2aea-b6e4-3817-9899-fc839553b220 | -17.54369 | -42.30114 | 2024-10-12 04:08:00 | NOAA-20 | MINAS NOVAS | MINAS GERAIS | Brasil | 3141801 | 31 | 33 | nan | nan | nan | Cerrado | 1.6 |
| 83a1d173-8c2d-3d84-8d74-16d9b6fad408 | -17.54312 | -42.30495 | 2024-10-12 04:08:00 | NOAA-20 | MINAS NOVAS | MINAS GERAIS | Brasil | 3141801 | 31 | 33 | nan | nan | nan | Cerrado | 12.6 |
| 36e82b5a-a899-3bce-a588-a36f15550e15 | -17.78416 | -41.80772 | 2024-10-12 04:08:00 | NOAA-20 | POTÉ | MINAS GERAIS | Brasil | 3152402 | 31 | 33 | nan | nan | nan | Mata Atlântica | 0.6 |
| 28410130-3f7e-3789-989a-47b7db20d3ca | -18.15542 | -42.44532 | 2024-10-12 04:08:00 | NOAA-20 | SANTA MARIA DO SUAÇUÍ | MINAS GERAIS | Brasil | 3158201 | 31 | 33 | nan | nan | nan | Mata Atlântica | 0.6 |
| 75669b4e-3738-3286-9ee3-bf7b0b1a8629 | -11.91308 | -41.67543 | 2024-10-12 04:08:00 | NOAA-20 | CANARANA | BAHIA | Brasil | 2906204 | 29 | 33 | nan | nan | nan | Caatinga | 1.9 |
| c37224f6-2264-3749-acd9-54845e90a7f6 | -11.79571 | -42.06497 | 2024-10-12 04:08:00 | NOAA-20 | BARRA DO MENDES | BAHIA | Brasil | 2903003 | 29 | 33 | nan | nan | nan | Caatinga | 0.9 |
| 097ca25e-7772-3427-9f15-088e4036ba4c | -13.43353 | -42.16378 | 2024-10-12 04:08:00 | NOAA-20 | ÉRICO CARDOSO | BAHIA | Brasil | 2900504 | 29 | 33 | nan | nan | nan | Caatinga | 0.5 |
| 4910ba1a-fef5-313a-88b5-7764271f1800 | -13.25245 | -42.3691 | 2024-10-12 04:08:00 | NOAA-20 | CATURAMA | BAHIA | Brasil | 2907558 | 29 | 33 | nan | nan | nan | Caatinga | 0.8 |
| b3f5ab32-8989-34ec-93db-f47d26b471d4 | -13.21703 | -42.3561 | 2024-10-12 04:08:00 | NOAA-20 | CATURAMA | BAHIA | Brasil | 2907558 | 29 | 33 | nan | nan | nan | Caatinga | 1.1 |
| 6a2970d1-e635-3f85-8354-6f8ac386bd75 | -13.08685 | -42.29934 | 2024-10-12 04:08:00 | NOAA-20 | RIO DO PIRES | BAHIA | Brasil | 2926905 | 29 | 33 | nan | nan | nan | Caatinga | 1.1 |
| 449fbb79-36b9-396b-9982-0f86e86d6e16 | -13.03487 | -43.26084 | 2024-10-12 04:08:00 | NOAA-20 | BOM JESUS DA LAPA | BAHIA | Brasil | 2903904 | 29 | 33 | nan | nan | nan | Caatinga | 2.4 |
| 0759381c-c925-3444-af61-ef9cb75e3ca6 | -13.55055 | -43.50178 | 2024-10-12 04:08:00 | NOAA-20 | SERRA DO RAMALHO | BAHIA | Brasil | 2930154 | 29 | 33 | nan | nan | nan | Cerrado | 1.0 |
| ee2fad36-3da5-3362-94f0-10f8704070e7 | -12.72584 | -42.50251 | 2024-10-12 04:08:00 | NOAA-20 | IBIPITANGA | BAHIA | Brasil | 2912509 | 29 | 33 | nan | nan | nan | Caatinga | 1.2 |
| c9eefb8e-daa3-3f29-a0ad-10fcb5aa21e9 | -12.7764 | -43.30571 | 2024-10-12 04:08:00 | NOAA-20 | BOM JESUS DA LAPA | BAHIA | Brasil | 2903904 | 29 | 33 | nan | nan | nan | Cerrado | 1.6 |
| d252f5a5-8252-3067-8139-22bb3b219721 | -12.77584 | -43.30924 | 2024-10-12 04:08:00 | NOAA-20 | BOM JESUS DA LAPA | BAHIA | Brasil | 2903904 | 29 | 33 | nan | nan | nan | Cerrado | 1.3 |
| 7e1677e9-335a-34f6-8f2c-87441c7b8bc3 | -12.62818 | -43.21271 | 2024-10-12 04:08:00 | NOAA-20 | MUQUÉM DO SÃO FRANCISCO | BAHIA | Brasil | 2922250 | 29 | 33 | nan | nan | nan | Cerrado | 1.1 |
| c8fda96f-1f81-3e8c-abbc-f71722b72c6d | -12.62762 | -43.21624 | 2024-10-12 04:08:00 | NOAA-20 | MUQUÉM DO SÃO FRANCISCO | BAHIA | Brasil | 2922250 | 29 | 33 | nan | nan | nan | Cerrado | 1.1 |
| 5eda87fa-fa07-3953-ac37-f4fc325552bf | -14.7677 | -42.31168 | 2024-10-12 04:08:00 | NOAA-20 | JACARACI | BAHIA | Brasil | 2917409 | 29 | 33 | nan | nan | nan | Caatinga | 1.9 |
| 567fea3c-fe29-386a-b2c7-5746b5907d41 | -14.48029 | -42.3518 | 2024-10-12 04:08:00 | NOAA-20 | CACULÉ | BAHIA | Brasil | 2905008 | 29 | 33 | nan | nan | nan | Caatinga | 0.9 |
| 25430243-d0f1-3273-b92e-70116c5cd60c | -14.21845 | -42.39825 | 2024-10-12 04:08:00 | NOAA-20 | CAETITÉ | BAHIA | Brasil | 2905206 | 29 | 33 | nan | nan | nan | Caatinga | 0.6 |
| cbe11162-ffab-3621-a00b-3e1077b33265 | -14.21726 | -42.31683 | 2024-10-12 04:08:00 | NOAA-20 | IBIASSUCÊ | BAHIA | Brasil | 2912004 | 29 | 33 | nan | nan | nan | Caatinga | 2.2 |
| 4dbd3abd-429e-3ef1-a9c1-c9033d244778 | -13.92373 | -42.39616 | 2024-10-12 04:08:00 | NOAA-20 | CAETITÉ | BAHIA | Brasil | 2905206 | 29 | 33 | nan | nan | nan | Caatinga | 1.3 |
| 98242fbf-b9e3-3a80-baae-db6de83491a6 | -13.9204 | -42.39561 | 2024-10-12 04:08:00 | NOAA-20 | CAETITÉ | BAHIA | Brasil | 2905206 | 29 | 33 | nan | nan | nan | Caatinga | 0.9 |
| e3b883ee-8461-3eae-8ee8-6f6cd94ef493 | -13.78293 | -43.19191 | 2024-10-12 04:08:00 | NOAA-20 | RIACHO DE SANTANA | BAHIA | Brasil | 2926400 | 29 | 33 | nan | nan | nan | Caatinga | 1.1 |
| d16fc2fb-0dd2-3aec-b38c-0602eb98bcdb | -14.3667 | -43.60423 | 2024-10-12 04:08:00 | NOAA-20 | IUIU | BAHIA | Brasil | 2917334 | 29 | 33 | nan | nan | nan | Cerrado | 1.5 |
| c040fa24-107c-31ac-826b-fed60d07bb47 | -14.36339 | -43.60368 | 2024-10-12 04:08:00 | NOAA-20 | IUIU | BAHIA | Brasil | 2917334 | 29 | 33 | nan | nan | nan | Cerrado | 2.1 |
| 9dc35bae-5929-3c65-a5bc-336f5eed74df | -15.41276 | -43.08266 | 2024-10-12 04:08:00 | NOAA-20 | CATUTI | MINAS GERAIS | Brasil | 3115474 | 31 | 33 | nan | nan | nan | Caatinga | 1.4 |
| cea63785-5a7a-35d6-8324-beef3637dd7a | -16.34943 | -43.69559 | 2024-10-12 04:08:00 | NOAA-20 | CAPITÃO ENÉAS | MINAS GERAIS | Brasil | 3112703 | 31 | 33 | nan | nan | nan | Cerrado | 0.9 |
| ca314339-23e8-3139-89ee-fe99cb2bbb48 | -16.13212 | -43.6305 | 2024-10-12 04:08:00 | NOAA-20 | CAPITÃO ENÉAS | MINAS GERAIS | Brasil | 3112703 | 31 | 33 | nan | nan | nan | Cerrado | 1.0 |
| 2dace718-ccfd-3383-989f-b71ff4b9905f | -16.08242 | -43.66615 | 2024-10-12 04:08:00 | NOAA-20 | CAPITÃO ENÉAS | MINAS GERAIS | Brasil | 3112703 | 31 | 33 | nan | nan | nan | Cerrado | 0.5 |
| 626ef04e-7620-35d1-9452-d88ef6dd0f2d | -16.07911 | -43.66559 | 2024-10-12 04:08:00 | NOAA-20 | CAPITÃO ENÉAS | MINAS GERAIS | Brasil | 3112703 | 31 | 33 | nan | nan | nan | Cerrado | 0.5 |


[Clique aqui para ver as próximas entradas](README49.md)
