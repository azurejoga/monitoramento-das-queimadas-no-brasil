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

## Dados Diários - Página 1

| ID | Latitude | Longitude | Data/Hora GMT | Satélite | Município | Estado | País | Município ID | Estado ID | País ID | Dias sem Chuva | Precipitação | Risco de Fogo | Bioma | FRP |
|----|----------|-----------|---------------|----------|-----------|--------|------|--------------|-----------|---------|----------------|--------------|----------------|-------|-----|
| 3f23378b-72bb-36c1-b24f-d601d7f9d110 | -8.034 | -47.6639 | 2025-08-20 00:00:00 | GOES-19 | GOIATINS | TOCANTINS | Brasil | 1709005 | 17 | 33 | nan | nan | nan | Cerrado | 74.6 |
| 8b324934-89e8-3543-94e0-69532e935b34 | -4.4331 | -47.76 | 2025-08-20 00:00:00 | GOES-19 | DOM ELISEU | PARÁ | Brasil | 1502939 | 15 | 33 | nan | nan | nan | Amazônia | 50.7 |
| 778764f9-f1b5-366e-8ff3-45ea45fd2ff5 | -6.9607 | -42.858 | 2025-08-20 00:00:00 | GOES-19 | FLORIANO | PIAUÍ | Brasil | 2203909 | 22 | 33 | nan | nan | nan | Caatinga | 74.8 |
| b05ff0e6-6cc1-3ea5-aeb2-32b7f16c718c | -12.9775 | -56.8816 | 2025-08-20 00:00:00 | GOES-19 | NOVA MARINGÁ | MATO GROSSO | Brasil | 5108907 | 51 | 33 | nan | nan | nan | Amazônia | 54.5 |
| 1c6afb60-a97e-3e01-92b6-4e0c5c7560e1 | -11.7504 | -48.2046 | 2025-08-20 00:00:00 | GOES-19 | SÃO VALÉRIO | TOCANTINS | Brasil | 1720499 | 17 | 33 | nan | nan | nan | Cerrado | 59.3 |
| eebf8062-d1ed-3827-adf2-d4ffe2c0df05 | -6.1476 | -57.7215 | 2025-08-20 00:00:00 | GOES-19 | JACAREACANGA | PARÁ | Brasil | 1503754 | 15 | 33 | nan | nan | nan | Amazônia | 60.9 |
| 968441e3-96ab-3c72-9a92-090e1f688767 | -15.1505 | -49.6353 | 2025-08-20 00:00:00 | GOES-19 | IPIRANGA DE GOIÁS | GOIÁS | Brasil | 5210158 | 52 | 33 | nan | nan | nan | Cerrado | 58.3 |
| 2cd905a4-3b0c-34ae-83bd-78184e022292 | -18.3179 | -48.8553 | 2025-08-20 00:00:00 | GOES-19 | CORUMBAÍBA | GOIÁS | Brasil | 5205901 | 52 | 33 | nan | nan | nan | Mata Atlântica | 64.0 |
| 2b9f8252-9f55-3705-986a-8db2ffe412c8 | -15.0002 | -54.8135 | 2025-08-20 00:00:00 | GOES-19 | NOVA BRASILÂNDIA | MATO GROSSO | Brasil | 5106208 | 51 | 33 | nan | nan | nan | Cerrado | 54.4 |
| 90f6b526-eb1a-345b-b98e-04797fef84c9 | -13.1048 | -51.9009 | 2025-08-20 00:00:00 | GOES-19 | RIBEIRÃO CASCALHEIRA | MATO GROSSO | Brasil | 5107180 | 51 | 33 | nan | nan | nan | Amazônia | 74.4 |
| c516a46a-4d8b-3385-a518-382d66d0f7bd | -9.2216 | -60.3302 | 2025-08-20 00:00:00 | GOES-19 | COLNIZA | MATO GROSSO | Brasil | 5103254 | 51 | 33 | nan | nan | nan | Amazônia | 48.5 |
| bc05aa09-f46e-3d02-b43c-3d2c76cde7f1 | -13.1044 | -51.9221 | 2025-08-20 00:00:00 | GOES-19 | RIBEIRÃO CASCALHEIRA | MATO GROSSO | Brasil | 5107180 | 51 | 33 | nan | nan | nan | Amazônia | 68.3 |
| 95828ab2-8970-3082-8366-8551047f3ed7 | -6.9605 | -42.8816 | 2025-08-20 00:00:00 | GOES-19 | FLORIANO | PIAUÍ | Brasil | 2203909 | 22 | 33 | nan | nan | nan | Caatinga | 79.2 |
| 0b646ca8-cb8d-3ede-b7e9-9097d82e0f5e | -15.5506 | -42.285 | 2025-08-20 00:00:00 | GOES-19 | INDAIABIRA | MINAS GERAIS | Brasil | 3130655 | 31 | 33 | nan | nan | nan | Cerrado | 72.0 |
| f4b0d846-b1d3-3a42-bb01-3d3f5c20b669 | -15.1509 | -49.6133 | 2025-08-20 00:00:00 | GOES-19 | IPIRANGA DE GOIÁS | GOIÁS | Brasil | 5210158 | 52 | 33 | nan | nan | nan | Cerrado | 103.8 |
| 510933f2-8431-3e06-92e8-ff5e7f61f41d | -13.3346 | -54.4233 | 2025-08-20 00:00:00 | GOES-19 | PARANATINGA | MATO GROSSO | Brasil | 5106307 | 51 | 33 | nan | nan | nan | Amazônia | 47.0 |
| 316db178-4a48-3f05-8d15-3997e987e2ac | -15.1314 | -49.6163 | 2025-08-20 00:00:00 | GOES-19 | NOVA GLÓRIA | GOIÁS | Brasil | 5214861 | 52 | 33 | nan | nan | nan | Cerrado | 94.3 |
| 0a75dad3-ed53-3360-961e-f468091d875b | -13.1555 | -54.9357 | 2025-08-20 00:00:00 | GOES-19 | NOVA UBIRATÃ | MATO GROSSO | Brasil | 5106240 | 51 | 33 | nan | nan | nan | Amazônia | 181.6 |
| 25910d1c-a810-3889-9df3-139963118c6f | -3.232 | -46.8056 | 2025-08-20 00:00:00 | GOES-19 | PARAGOMINAS | PARÁ | Brasil | 1505502 | 15 | 33 | nan | nan | nan | Amazônia | 64.1 |
| 68b17b7b-ac1a-3557-88aa-32df4e125454 | -13.1558 | -54.9151 | 2025-08-20 00:00:00 | GOES-19 | NOVA UBIRATÃ | MATO GROSSO | Brasil | 5106240 | 51 | 33 | nan | nan | nan | Amazônia | 107.1 |
| 3e3948a7-9708-31a5-9c8e-f1b5c0e0b58c | -6.8583 | -43.6169 | 2025-08-20 00:00:00 | GOES-19 | GUADALUPE | PIAUÍ | Brasil | 2204501 | 22 | 33 | nan | nan | nan | Cerrado | 76.8 |
| 8c1768af-a170-39d1-b238-483b67bec9ca | -20.339 | -51.7062 | 2025-08-20 00:00:00 | GOES-19 | SELVÍRIA | MATO GROSSO DO SUL | Brasil | 5007802 | 50 | 33 | nan | nan | nan | Cerrado | 95.3 |
| 2f7aba70-8d2f-3353-b7dc-31e48dbb4f0a | -8.0152 | -47.6656 | 2025-08-20 00:00:00 | GOES-19 | GOIATINS | TOCANTINS | Brasil | 1709005 | 17 | 33 | nan | nan | nan | Cerrado | 61.9 |
| 141b087a-7480-3553-8159-b100439a053e | -12.9778 | -56.8614 | 2025-08-20 00:00:00 | GOES-19 | NOVA MARINGÁ | MATO GROSSO | Brasil | 5108907 | 51 | 33 | nan | nan | nan | Amazônia | 66.8 |
| 5b3eeef5-e59f-3da5-9f69-e23ff7afaa4e | -20.3594 | -51.7023 | 2025-08-20 00:00:00 | GOES-19 | SELVÍRIA | MATO GROSSO DO SUL | Brasil | 5007802 | 50 | 33 | nan | nan | nan | Cerrado | 67.6 |
| 6b45a8e4-4636-3e4f-bed4-467ed248b381 | -11.7508 | -48.1825 | 2025-08-20 00:00:00 | GOES-19 | SÃO VALÉRIO | TOCANTINS | Brasil | 1720499 | 17 | 33 | nan | nan | nan | Cerrado | 148.0 |
| d943583e-6acc-3b9e-a9ca-46fca1b0a6cc | -13.1364 | -54.9376 | 2025-08-20 00:00:00 | GOES-19 | NOVA UBIRATÃ | MATO GROSSO | Brasil | 5106240 | 51 | 33 | nan | nan | nan | Amazônia | 57.6 |
| 5997dd01-c213-361b-8be5-d7334e86eced | -15.131 | -49.6384 | 2025-08-20 00:00:00 | GOES-19 | IPIRANGA DE GOIÁS | GOIÁS | Brasil | 5210158 | 52 | 33 | nan | nan | nan | Cerrado | 48.6 |
| 5d669946-166d-3aa3-a6aa-8a8f2fc698da | -3.982 | -42.516 | 2025-08-20 00:00:00 | GOES-19 | CAMPO LARGO DO PIAUÍ | PIAUÍ | Brasil | 2202174 | 22 | 33 | nan | nan | nan | Caatinga | 44.7 |
| b8b7807e-a363-353c-9734-d0caaa3d714a | -4.912 | -43.2337 | 2025-08-20 00:00:00 | GOES-19 | CAXIAS | MARANHÃO | Brasil | 2103000 | 21 | 33 | nan | nan | nan | Cerrado | 206.7 |
| 5292bc82-9ef1-368f-ab61-1b00c0c7dc37 | -8.0152 | -47.6656 | 2025-08-20 00:10:00 | GOES-19 | GOIATINS | TOCANTINS | Brasil | 1709005 | 17 | 33 | nan | nan | nan | Cerrado | 58.9 |
| fbd9eb8c-aa12-36af-af55-32c1bc4f66ea | -3.232 | -46.8056 | 2025-08-20 00:10:00 | GOES-19 | PARAGOMINAS | PARÁ | Brasil | 1505502 | 15 | 33 | nan | nan | nan | Amazônia | 50.4 |
| ccfeac1f-b291-36ee-9f9f-5f8f3853b45a | -13.3346 | -54.4233 | 2025-08-20 00:10:00 | GOES-19 | PARANATINGA | MATO GROSSO | Brasil | 5106307 | 51 | 33 | nan | nan | nan | Amazônia | 49.1 |
| 71bbffbb-3f82-3f80-a5e6-7cf5198c0ca4 | -13.1555 | -54.9357 | 2025-08-20 00:10:00 | GOES-19 | NOVA UBIRATÃ | MATO GROSSO | Brasil | 5106240 | 51 | 33 | nan | nan | nan | Amazônia | 176.7 |
| f20ab155-1b77-399d-82a9-695b6230b20e | -13.1044 | -51.9221 | 2025-08-20 00:10:00 | GOES-19 | RIBEIRÃO CASCALHEIRA | MATO GROSSO | Brasil | 5107180 | 51 | 33 | nan | nan | nan | Amazônia | 86.6 |
| 647c81d7-ce90-3a5f-addc-0cddd99d5842 | -9.2216 | -60.3302 | 2025-08-20 00:10:00 | GOES-19 | COLNIZA | MATO GROSSO | Brasil | 5103254 | 51 | 33 | nan | nan | nan | Amazônia | 55.8 |
| 7b900c11-313d-3a67-8a42-261ff0ed7bf9 | -8.6156 | -62.1564 | 2025-08-20 00:10:00 | GOES-19 | HUMAITÁ | AMAZONAS | Brasil | 1301704 | 13 | 33 | nan | nan | nan | Amazônia | 53.5 |
| 1018c63f-ceae-3083-8635-2014da0b1695 | -8.034 | -47.6639 | 2025-08-20 00:10:00 | GOES-19 | GOIATINS | TOCANTINS | Brasil | 1709005 | 17 | 33 | nan | nan | nan | Cerrado | 76.6 |
| 7f635454-8e96-384d-9377-50576b31e153 | -8.6343 | -62.1367 | 2025-08-20 00:10:00 | GOES-19 | HUMAITÁ | AMAZONAS | Brasil | 1301704 | 13 | 33 | nan | nan | nan | Amazônia | 169.6 |
| 42edb840-15ff-3526-9c24-76be554f9739 | -20.4898 | -42.2404 | 2025-08-20 00:10:00 | GOES-19 | ORIZÂNIA | MINAS GERAIS | Brasil | 3145877 | 31 | 33 | nan | nan | nan | Mata Atlântica | 48.1 |
| cce75e93-4c53-3f02-aef7-85c3fe2059b9 | -4.4331 | -47.76 | 2025-08-20 00:10:00 | GOES-19 | DOM ELISEU | PARÁ | Brasil | 1502939 | 15 | 33 | nan | nan | nan | Amazônia | 47.5 |
| 02eb002d-0873-380f-ab9a-24f83114e7e9 | -20.3594 | -51.7023 | 2025-08-20 00:10:00 | GOES-19 | SELVÍRIA | MATO GROSSO DO SUL | Brasil | 5007802 | 50 | 33 | nan | nan | nan | Cerrado | 76.0 |
| 88ecbc0e-af14-38ff-b1f4-4e2a552b08ae | -12.9778 | -56.8614 | 2025-08-20 00:10:00 | GOES-19 | NOVA MARINGÁ | MATO GROSSO | Brasil | 5108907 | 51 | 33 | nan | nan | nan | Amazônia | 67.0 |
| 311410df-85ac-365f-b119-5194ec484778 | -12.9775 | -56.8816 | 2025-08-20 00:10:00 | GOES-19 | NOVA MARINGÁ | MATO GROSSO | Brasil | 5108907 | 51 | 33 | nan | nan | nan | Amazônia | 56.4 |
| 7240f1e9-321e-3f81-a5e5-2a39e6ec528a | -4.912 | -43.2337 | 2025-08-20 00:10:00 | GOES-19 | CAXIAS | MARANHÃO | Brasil | 2103000 | 21 | 33 | nan | nan | nan | Cerrado | 185.1 |
| 92174598-1ece-30b6-85c4-48a382052546 | -8.6157 | -62.1374 | 2025-08-20 00:10:00 | GOES-19 | HUMAITÁ | AMAZONAS | Brasil | 1301704 | 13 | 33 | nan | nan | nan | Amazônia | 54.9 |
| 1d6c58e2-cfa1-3a55-aa4e-a1a9325a51f1 | -13.1364 | -54.9376 | 2025-08-20 00:10:00 | GOES-19 | NOVA UBIRATÃ | MATO GROSSO | Brasil | 5106240 | 51 | 33 | nan | nan | nan | Amazônia | 61.1 |
| 701c8d4c-4fd4-35fc-8a62-d26d8f002cc1 | -13.1558 | -54.9151 | 2025-08-20 00:10:00 | GOES-19 | NOVA UBIRATÃ | MATO GROSSO | Brasil | 5106240 | 51 | 33 | nan | nan | nan | Amazônia | 130.2 |
| e6176c96-a39b-3003-8b6e-631d112fe726 | -6.9605 | -42.8816 | 2025-08-20 00:10:00 | GOES-19 | FLORIANO | PIAUÍ | Brasil | 2203909 | 22 | 33 | nan | nan | nan | Caatinga | 70.9 |
| d4b49803-b949-39da-a16e-27cccf7e51dc | -13.1048 | -51.9009 | 2025-08-20 00:10:00 | GOES-19 | RIBEIRÃO CASCALHEIRA | MATO GROSSO | Brasil | 5107180 | 51 | 33 | nan | nan | nan | Amazônia | 129.2 |
| e85ef7c9-eed4-336d-be04-1472eed15196 | -15.0002 | -54.8135 | 2025-08-20 00:10:00 | GOES-19 | NOVA BRASILÂNDIA | MATO GROSSO | Brasil | 5106208 | 51 | 33 | nan | nan | nan | Cerrado | 56.6 |
| cc023bf8-3c59-305a-83ba-8602fda0216a | -20.339 | -51.7062 | 2025-08-20 00:10:00 | GOES-19 | SELVÍRIA | MATO GROSSO DO SUL | Brasil | 5007802 | 50 | 33 | nan | nan | nan | Cerrado | 126.4 |
| 6ed7b6ee-53b4-3d7a-a65c-a60ce757fe82 | -8.6342 | -62.1557 | 2025-08-20 00:10:00 | GOES-19 | HUMAITÁ | AMAZONAS | Brasil | 1301704 | 13 | 33 | nan | nan | nan | Amazônia | 152.6 |
| 15f74f14-8794-32be-8c1f-e04c2e5404de | -11.7508 | -48.1825 | 2025-08-20 00:10:00 | GOES-19 | SÃO VALÉRIO | TOCANTINS | Brasil | 1720499 | 17 | 33 | nan | nan | nan | Cerrado | 93.6 |
| 40eb37b8-b3f3-38c1-9462-2ee1ddc7a4f0 | -6.9607 | -42.858 | 2025-08-20 00:10:00 | GOES-19 | FLORIANO | PIAUÍ | Brasil | 2203909 | 22 | 33 | nan | nan | nan | Caatinga | 69.0 |
| 7310071e-4201-3afb-9fb4-4f1ce08fa688 | -13.1367 | -54.9171 | 2025-08-20 00:10:00 | GOES-19 | NOVA UBIRATÃ | MATO GROSSO | Brasil | 5106240 | 51 | 33 | nan | nan | nan | Amazônia | 45.2 |
| ec4dac47-dcf0-3dae-a27d-306c57d13d38 | -3.982 | -42.516 | 2025-08-20 00:10:00 | GOES-19 | CAMPO LARGO DO PIAUÍ | PIAUÍ | Brasil | 2202174 | 22 | 33 | nan | nan | nan | Caatinga | 50.7 |
| 4fe82096-1dc5-3ca3-8c2f-2ed10cdae399 | -15.5506 | -42.285 | 2025-08-20 00:10:00 | GOES-19 | INDAIABIRA | MINAS GERAIS | Brasil | 3130655 | 31 | 33 | nan | nan | nan | Cerrado | 61.7 |
| 2b29a688-8151-3074-a871-cbbcc82a5b2b | -11.8783 | -40.9547 | 2025-08-20 00:14:00 | METOP-C | TAPIRAMUTÁ | BAHIA | Brasil | 2931301 | 29 | 33 | nan | nan | nan | Caatinga | nan |
| b499d8b3-72da-37cd-a50b-15be15e5a5b1 | -11.9697 | -46.775902 | 2025-08-20 00:14:00 | METOP-C | DIANÓPOLIS | TOCANTINS | Brasil | 1707009 | 17 | 33 | nan | nan | nan | Cerrado | nan |
| d73c6585-8e59-3e13-8a85-82246e762592 | -7.7833 | -45.155102 | 2025-08-20 00:14:00 | METOP-C | RIBEIRO GONÇALVES | PIAUÍ | Brasil | 2208908 | 22 | 33 | nan | nan | nan | Cerrado | nan |
| 421d498d-f1e4-37b9-a1b7-cd516cfd5e31 | -18.311501 | -48.879902 | 2025-08-20 00:14:00 | METOP-C | CORUMBAÍBA | GOIÁS | Brasil | 5205901 | 52 | 33 | nan | nan | nan | Mata Atlântica | nan |
| 869438a7-f705-35e1-8e02-222fb4f0ce5f | -6.6135 | -43.877998 | 2025-08-20 00:14:00 | METOP-C | NOVA IORQUE | MARANHÃO | Brasil | 2107308 | 21 | 33 | nan | nan | nan | Cerrado | nan |
| 7f3c199b-a9b7-3829-9151-fbb813ae630e | -6.1279 | -42.962399 | 2025-08-20 00:14:00 | METOP-C | PALMEIRAIS | PIAUÍ | Brasil | 2207504 | 22 | 33 | nan | nan | nan | Caatinga | nan |
| ecd6108b-9e0f-33c8-828c-c96df0630320 | -3.2604 | -49.136501 | 2025-08-20 00:14:00 | METOP-C | MOJU | PARÁ | Brasil | 1504703 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| 59f14ba7-3c70-3985-8d31-7b48c0620c7b | -12.9458 | -46.1688 | 2025-08-20 00:14:00 | METOP-C | CAMPOS BELOS | GOIÁS | Brasil | 5204904 | 52 | 33 | nan | nan | nan | Cerrado | nan |
| ca521d17-448a-3144-8759-d0c2786caae3 | -12.9916 | -45.208199 | 2025-08-20 00:14:00 | METOP-C | SÃO DESIDÉRIO | BAHIA | Brasil | 2928901 | 29 | 33 | nan | nan | nan | Cerrado | nan |
| 9f05f146-f923-38ef-bca5-ead904ab979a | -7.5932 | -44.391201 | 2025-08-20 00:14:00 | METOP-C | URUÇUÍ | PIAUÍ | Brasil | 2211209 | 22 | 33 | nan | nan | nan | Cerrado | nan |
| 94de91b2-9637-37fd-8d02-73ea435e88e5 | -3.8256 | -41.561199 | 2025-08-20 00:14:00 | METOP-C | PIRACURUCA | PIAUÍ | Brasil | 2208304 | 22 | 33 | nan | nan | nan | Caatinga | nan |
| e4736995-e56a-375e-9cdd-592300316d94 | -5.1138 | -43.217899 | 2025-08-20 00:14:00 | METOP-C | CAXIAS | MARANHÃO | Brasil | 2103000 | 21 | 33 | nan | nan | nan | Cerrado | nan |
| c5645508-dd24-3d5e-a91f-c4b90f9744c8 | -8.013 | -47.666801 | 2025-08-20 00:14:00 | METOP-C | GOIATINS | TOCANTINS | Brasil | 1709005 | 17 | 33 | nan | nan | nan | Cerrado | nan |
| 5a342004-fd6d-39f7-b114-d5055b70960c | -21.3561 | -41.926998 | 2025-08-20 00:14:00 | METOP-C | SÃO JOSÉ DE UBÁ | RIO DE JANEIRO | Brasil | 3305133 | 33 | 33 | nan | nan | nan | Mata Atlântica | nan |
| f7070827-09a9-3a74-b3a3-64d0607a938a | -20.483999 | -42.2668 | 2025-08-20 00:14:00 | METOP-C | SANTA MARGARIDA | MINAS GERAIS | Brasil | 3157906 | 31 | 33 | nan | nan | nan | Mata Atlântica | nan |
| 420218a3-2057-3302-9045-26aa9551ec38 | -5.7834 | -43.8969 | 2025-08-20 00:14:00 | METOP-C | BURITI BRAVO | MARANHÃO | Brasil | 2102309 | 21 | 33 | nan | nan | nan | Cerrado | nan |
| 62af514b-a55b-3406-a221-c235a2eba7fe | -13.0326 | -46.791901 | 2025-08-20 00:14:00 | METOP-C | CAMPOS BELOS | GOIÁS | Brasil | 5204904 | 52 | 33 | nan | nan | nan | Cerrado | nan |
| 4cd8402b-cd06-3355-ad82-2da77447af95 | -3.9822 | -42.509602 | 2025-08-20 00:14:00 | METOP-C | CAMPO LARGO DO PIAUÍ | PIAUÍ | Brasil | 2202174 | 22 | 33 | nan | nan | nan | Caatinga | nan |
| d3d70333-26eb-3c64-8178-9fb38ceb4718 | -7.8464 | -45.115398 | 2025-08-20 00:14:00 | METOP-C | BAIXA GRANDE DO RIBEIRO | PIAUÍ | Brasil | 2201150 | 22 | 33 | nan | nan | nan | Cerrado | nan |
| 4226f96c-690d-328e-9a7c-f4e8b0bc5e21 | -3.819 | -41.577499 | 2025-08-20 00:14:00 | METOP-C | PIRACURUCA | PIAUÍ | Brasil | 2208304 | 22 | 33 | nan | nan | nan | Caatinga | nan |
| 2420629e-b57a-3c7e-8ea8-0da993eb7be5 | -13.0949 | -51.897099 | 2025-08-20 00:14:00 | METOP-C | RIBEIRÃO CASCALHEIRA | MATO GROSSO | Brasil | 5107180 | 51 | 33 | nan | nan | nan | Amazônia | nan |
| d8976f4c-5cbb-3a58-9592-2cc7cb069954 | -7.1469 | -44.189602 | 2025-08-20 00:14:00 | METOP-C | ANTÔNIO ALMEIDA | PIAUÍ | Brasil | 2200806 | 22 | 33 | nan | nan | nan | Cerrado | nan |
| 0ae53d07-3027-39c5-859b-7417fa1f9684 | -5.7917 | -43.8876 | 2025-08-20 00:14:00 | METOP-C | BURITI BRAVO | MARANHÃO | Brasil | 2102309 | 21 | 33 | nan | nan | nan | Cerrado | nan |
| 2dd7adf9-17b7-3f8a-85a2-61d449e5cd8b | -5.9841 | -44.1464 | 2025-08-20 00:14:00 | METOP-C | COLINAS | MARANHÃO | Brasil | 2103505 | 21 | 33 | nan | nan | nan | Cerrado | nan |
| 4c9d8a29-985e-32d8-8ade-219f50e7f532 | -2.3851 | -47.6661 | 2025-08-20 00:14:00 | METOP-C | IPIXUNA DO PARÁ | PARÁ | Brasil | 1503457 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| 2e2769c9-3c64-3fe2-8c1f-84134d32a8e0 | -6.9722 | -42.8675 | 2025-08-20 00:14:00 | METOP-C | FLORIANO | PIAUÍ | Brasil | 2203909 | 22 | 33 | nan | nan | nan | Caatinga | nan |
| d6bab1bd-976a-3532-9c7a-7e6316d871de | -6.8068 | -43.684601 | 2025-08-20 00:14:00 | METOP-C | GUADALUPE | PIAUÍ | Brasil | 2204501 | 22 | 33 | nan | nan | nan | Cerrado | nan |
| 6de80393-6927-3faa-9aab-eef63a428fbb | -12.9896 | -45.198502 | 2025-08-20 00:14:00 | METOP-C | SÃO DESIDÉRIO | BAHIA | Brasil | 2928901 | 29 | 33 | nan | nan | nan | Cerrado | nan |
| d8c3750b-5a32-347b-a17c-08028f465d67 | -11.7389 | -48.185101 | 2025-08-20 00:14:00 | METOP-C | SÃO VALÉRIO | TOCANTINS | Brasil | 1720499 | 17 | 33 | nan | nan | nan | Cerrado | nan |
| f9b319d9-ecd3-3ba6-bef2-ca0e5034e5dd | -7.2663 | -50.186798 | 2025-08-20 00:14:00 | METOP-C | RIO MARIA | PARÁ | Brasil | 1506161 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| 5094b2c5-c681-38ad-bd9e-6ca792d27676 | -20.323 | -51.694801 | 2025-08-20 00:14:00 | METOP-C | SELVÍRIA | MATO GROSSO DO SUL | Brasil | 5007802 | 50 | 33 | nan | nan | nan | Cerrado | nan |
| 9da9ab98-0544-31ba-8d1a-465f75e15e6d | -3.8239 | -41.5541 | 2025-08-20 00:14:00 | METOP-C | PIRACURUCA | PIAUÍ | Brasil | 2208304 | 22 | 33 | nan | nan | nan | Caatinga | nan |
| bb654753-0643-35c9-a772-5c13a3368fc7 | -3.8141 | -41.556301 | 2025-08-20 00:14:00 | METOP-C | PIRACURUCA | PIAUÍ | Brasil | 2208304 | 22 | 33 | nan | nan | nan | Caatinga | nan |
| 9144c626-c969-3070-b2b5-f835ee0c5d57 | -13.0228 | -46.7939 | 2025-08-20 00:14:00 | METOP-C | CAMPOS BELOS | GOIÁS | Brasil | 5204904 | 52 | 33 | nan | nan | nan | Cerrado | nan |
| dc9aa095-07c4-39f2-a46b-2220fe0c6682 | -8.3041 | -46.3615 | 2025-08-20 00:14:00 | METOP-C | BALSAS | MARANHÃO | Brasil | 2101400 | 21 | 33 | nan | nan | nan | Cerrado | nan |
| fa1a2f05-7056-3752-9459-0de855c0df25 | -8.1315 | -49.517502 | 2025-08-20 00:14:00 | METOP-C | CONCEIÇÃO DO ARAGUAIA | PARÁ | Brasil | 1502707 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| 30c3d2a5-ab77-3d50-afa0-e21b352bf8a3 | -5.6461 | -43.381901 | 2025-08-20 00:14:00 | METOP-C | PARNARAMA | MARANHÃO | Brasil | 2107803 | 21 | 33 | nan | nan | nan | Cerrado | nan |
| c33d6ac4-c55f-3ed7-b890-85f4beb3ada4 | -14.5038 | -45.961102 | 2025-08-20 00:14:00 | METOP-C | JABORANDI | BAHIA | Brasil | 2917359 | 29 | 33 | nan | nan | nan | Cerrado | nan |
| 6ad838a8-02c0-3bb5-ab25-e62509249569 | -7.2627 | -50.169998 | 2025-08-20 00:14:00 | METOP-C | RIO MARIA | PARÁ | Brasil | 1506161 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| ed394e2b-ab06-3734-8c1d-9fe13caf8e93 | -10.3058 | -46.677299 | 2025-08-20 00:14:00 | METOP-C | MATEIROS | TOCANTINS | Brasil | 1712702 | 17 | 33 | nan | nan | nan | Cerrado | nan |
| f30c71c8-b048-3b4d-a86b-dec849259a89 | -5.785 | -43.903999 | 2025-08-20 00:14:00 | METOP-C | BURITI BRAVO | MARANHÃO | Brasil | 2102309 | 21 | 33 | nan | nan | nan | Cerrado | nan |
| 05fc8f5f-be31-3823-bc05-a0e6d4dd44f4 | -7.7851 | -45.1633 | 2025-08-20 00:14:00 | METOP-C | RIBEIRO GONÇALVES | PIAUÍ | Brasil | 2208908 | 22 | 33 | nan | nan | nan | Cerrado | nan |


[Clique aqui para ver as próximas entradas](README2.md)
