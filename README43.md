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

## Dados Diários - Página 43

| ID | Latitude | Longitude | Data/Hora GMT | Satélite | Município | Estado | País | Município ID | Estado ID | País ID | Dias sem Chuva | Precipitação | Risco de Fogo | Bioma | FRP |
|----|----------|-----------|---------------|----------|-----------|--------|------|--------------|-----------|---------|----------------|--------------|----------------|-------|-----|
| e8475dbf-b79d-3961-ba85-5a266cae3200 | -4.91971 | -45.71537 | 2025-10-30 04:25:00 | NOAA-20 | ARAME | MARANHÃO | Brasil | 2100956 | 21 | 33 | nan | nan | nan | Amazônia | 0.9 |
| b7a6b915-2866-38a2-9d08-8725a6d3f409 | -9.84531 | -44.88831 | 2025-10-30 04:25:00 | NOAA-20 | RIACHO FRIO | PIAUÍ | Brasil | 2208858 | 22 | 33 | nan | nan | nan | Cerrado | 3.2 |
| 27fc5a2f-af0b-3b86-bbb9-7263b1c44b98 | -5.76258 | -49.11333 | 2025-10-30 04:25:00 | NOAA-20 | MARABÁ | PARÁ | Brasil | 1504208 | 15 | 33 | nan | nan | nan | Amazônia | 0.6 |
| 67391714-1046-3b5f-b4e6-be532e213415 | -7.88363 | -46.74132 | 2025-10-30 04:25:00 | NOAA-20 | RIACHÃO | MARANHÃO | Brasil | 2109502 | 21 | 33 | nan | nan | nan | Cerrado | 4.7 |
| 87f416c6-2308-3a74-9cd2-5c1624176ecb | -5.50647 | -44.98611 | 2025-10-30 04:25:00 | NOAA-20 | BARRA DO CORDA | MARANHÃO | Brasil | 2101608 | 21 | 33 | nan | nan | nan | Cerrado | 2.1 |
| 7ddf9dae-d6d6-32c8-8300-a36bf1992c5a | -3.44403 | -54.64041 | 2025-10-30 04:25:00 | NOAA-20 | PLACAS | PARÁ | Brasil | 1505650 | 15 | 33 | nan | nan | nan | Amazônia | 0.7 |
| 330cef65-b3cd-3221-a4f4-c8cb5f2f01d9 | -4.88788 | -45.44162 | 2025-10-30 04:25:00 | NOAA-20 | LAGOA GRANDE DO MARANHÃO | MARANHÃO | Brasil | 2105963 | 21 | 33 | nan | nan | nan | Cerrado | 1.3 |
| 88de995f-e8f3-3326-8751-aad97e3d9c75 | -5.47898 | -40.89387 | 2025-10-30 04:25:00 | NOAA-20 | CRATEÚS | CEARÁ | Brasil | 2304103 | 23 | 33 | nan | nan | nan | Caatinga | 1.1 |
| 6dac0c10-fe75-3b33-9247-d6b57e6d6fcd | -7.07016 | -44.46647 | 2025-10-30 04:25:00 | NOAA-20 | BENEDITO LEITE | MARANHÃO | Brasil | 2101806 | 21 | 33 | nan | nan | nan | Cerrado | 2.7 |
| 255c6f11-c06a-34b4-8eaa-7dbbae43b160 | -6.13435 | -41.56876 | 2025-10-30 04:25:00 | NOAA-20 | PIMENTEIRAS | PIAUÍ | Brasil | 2208106 | 22 | 33 | nan | nan | nan | Caatinga | 1.6 |
| 61bf41c7-5a95-34a0-9f17-1ce00c7a1ff2 | -7.75673 | -46.49002 | 2025-10-30 04:25:00 | NOAA-20 | RIACHÃO | MARANHÃO | Brasil | 2109502 | 21 | 33 | nan | nan | nan | Cerrado | 1.4 |
| b28d80a8-3981-32b5-9af3-d43d1ccf712f | -7.2955 | -45.66369 | 2025-10-30 04:25:00 | NOAA-20 | SÃO RAIMUNDO DAS MANGABEIRAS | MARANHÃO | Brasil | 2111607 | 21 | 33 | nan | nan | nan | Cerrado | 2.1 |
| 94e1d64f-c0e0-3ac5-ac53-29d3f706ec5a | -7.79794 | -46.42202 | 2025-10-30 04:25:00 | NOAA-20 | BALSAS | MARANHÃO | Brasil | 2101400 | 21 | 33 | nan | nan | nan | Cerrado | 2.2 |
| 01fe9ef3-598a-3181-9dfe-2b1dbdfe873b | -4.60045 | -46.05978 | 2025-10-30 04:25:00 | NOAA-20 | SANTA LUZIA | MARANHÃO | Brasil | 2110005 | 21 | 33 | nan | nan | nan | Amazônia | 0.5 |
| 1533986b-1a82-3209-9c26-0aa9aba3e39c | -10.76041 | -47.83952 | 2025-10-30 04:25:00 | NOAA-20 | MONTE DO CARMO | TOCANTINS | Brasil | 1713601 | 17 | 33 | nan | nan | nan | Cerrado | 1.1 |
| 4448fb64-bacd-3cc3-ac76-793b17dd6c48 | -7.62435 | -43.58099 | 2025-10-30 04:25:00 | NOAA-20 | CANAVIEIRA | PIAUÍ | Brasil | 2202251 | 22 | 33 | nan | nan | nan | Cerrado | 7.1 |
| 3939551f-bfb9-3b96-8b5c-034a872c2265 | -6.46705 | -41.64913 | 2025-10-30 04:25:00 | NOAA-20 | LAGOA DO SÍTIO | PIAUÍ | Brasil | 2205599 | 22 | 33 | nan | nan | nan | Caatinga | 1.0 |
| 24d4e537-aff8-3533-92f4-e44e52849592 | -10.87701 | -48.00374 | 2025-10-30 04:25:00 | NOAA-20 | MONTE DO CARMO | TOCANTINS | Brasil | 1713601 | 17 | 33 | nan | nan | nan | Cerrado | 1.5 |
| 252f4a2c-3a56-38e9-8654-1f59ae2bbea1 | -5.27951 | -47.24159 | 2025-10-30 04:25:00 | NOAA-20 | SÃO FRANCISCO DO BREJÃO | MARANHÃO | Brasil | 2110856 | 21 | 33 | nan | nan | nan | Amazônia | 0.6 |
| 52c53697-3a39-39d6-9070-e4bc2c693808 | -8.3347 | -47.93466 | 2025-10-30 04:25:00 | NOAA-20 | ITACAJÁ | TOCANTINS | Brasil | 1710508 | 17 | 33 | nan | nan | nan | Cerrado | 2.0 |
| 47b6e32c-5c02-340e-8c38-5c69b4915eb5 | -6.45458 | -42.21341 | 2025-10-30 04:25:00 | NOAA-20 | FRANCINÓPOLIS | PIAUÍ | Brasil | 2204006 | 22 | 33 | nan | nan | nan | Caatinga | 2.1 |
| 881edb7c-dfcc-3516-a4d0-8529be3118da | -7.95907 | -46.71423 | 2025-10-30 04:25:00 | NOAA-20 | CAMPOS LINDOS | TOCANTINS | Brasil | 1703842 | 17 | 33 | nan | nan | nan | Cerrado | 1.9 |
| ccb0fd62-70b2-3ec6-9e79-140d90e8fc3b | -5.73052 | -46.51869 | 2025-10-30 04:25:00 | NOAA-20 | AMARANTE DO MARANHÃO | MARANHÃO | Brasil | 2100600 | 21 | 33 | nan | nan | nan | Cerrado | 0.6 |
| 59922536-da89-33a9-bfb8-86f6eb692931 | -11.62267 | -47.73901 | 2025-10-30 04:25:00 | NOAA-20 | CHAPADA DA NATIVIDADE | TOCANTINS | Brasil | 1705102 | 17 | 33 | nan | nan | nan | Cerrado | 2.7 |
| dfacc925-eea9-3f04-9b01-91df9a596e74 | -6.13281 | -41.68391 | 2025-10-30 04:25:00 | NOAA-20 | PIMENTEIRAS | PIAUÍ | Brasil | 2208106 | 22 | 33 | nan | nan | nan | Caatinga | 2.4 |
| fa2870ec-fbf4-3c09-b88c-2b7c6fae1e37 | -5.59847 | -49.70269 | 2025-10-30 04:25:00 | NOAA-20 | MARABÁ | PARÁ | Brasil | 1504208 | 15 | 33 | nan | nan | nan | Amazônia | 0.6 |
| 6954908f-6195-37f8-a8ec-7691a67dc115 | -6.80756 | -48.64662 | 2025-10-30 04:25:00 | NOAA-20 | ARAGOMINAS | TOCANTINS | Brasil | 1701309 | 17 | 33 | nan | nan | nan | Amazônia | 2.0 |
| 60d6c0b9-2c03-32d0-9ed5-07ab83e35323 | -5.11182 | -44.7084 | 2025-10-30 04:25:00 | NOAA-20 | JOSELÂNDIA | MARANHÃO | Brasil | 2105609 | 21 | 33 | nan | nan | nan | Cerrado | 3.0 |
| 00a63e13-a2ff-3152-a93a-36259c3b2b51 | -5.76451 | -44.5494 | 2025-10-30 04:25:00 | NOAA-20 | TUNTUM | MARANHÃO | Brasil | 2112308 | 21 | 33 | nan | nan | nan | Cerrado | 2.3 |
| beb4abd0-c66a-3325-b66e-d93c488dc30f | -7.50854 | -44.07694 | 2025-10-30 04:25:00 | NOAA-20 | SEBASTIÃO LEAL | PIAUÍ | Brasil | 2210631 | 22 | 33 | nan | nan | nan | Cerrado | 1.0 |
| cc01f023-3eff-3fc5-ba48-7a939dc5099e | -9.91124 | -44.91339 | 2025-10-30 04:25:00 | NOAA-20 | RIACHO FRIO | PIAUÍ | Brasil | 2208858 | 22 | 33 | nan | nan | nan | Cerrado | 1.2 |
| 9da6ad3c-819f-3553-8a35-723be02c2012 | -9.74246 | -47.68114 | 2025-10-30 04:25:00 | NOAA-20 | RIO SONO | TOCANTINS | Brasil | 1718758 | 17 | 33 | nan | nan | nan | Cerrado | 0.8 |
| 32b24229-bb75-3fba-98c0-6690b2ba0e6c | -5.65262 | -45.97948 | 2025-10-30 04:25:00 | NOAA-20 | GRAJAÚ | MARANHÃO | Brasil | 2104800 | 21 | 33 | nan | nan | nan | Cerrado | 1.1 |
| 5628abf8-4d9d-3e35-8950-3d8112ce55d4 | -6.98039 | -42.66077 | 2025-10-30 04:25:00 | NOAA-20 | NAZARÉ DO PIAUÍ | PIAUÍ | Brasil | 2206704 | 22 | 33 | nan | nan | nan | Caatinga | 1.2 |
| 578b8b05-930d-3119-b671-2ed10c5fb815 | -3.45651 | -52.87294 | 2025-10-30 04:25:00 | NOAA-20 | MEDICILÂNDIA | PARÁ | Brasil | 1504455 | 15 | 33 | nan | nan | nan | Amazônia | 0.7 |
| 39319337-4deb-3320-90cb-53224ae38339 | -6.10131 | -47.04919 | 2025-10-30 04:25:00 | NOAA-20 | LAJEADO NOVO | MARANHÃO | Brasil | 2105989 | 21 | 33 | nan | nan | nan | Cerrado | 1.1 |
| 4710494e-cc55-381b-9855-011117edcb9a | -11.80564 | -47.22559 | 2025-10-30 04:25:00 | NOAA-20 | ALMAS | TOCANTINS | Brasil | 1700400 | 17 | 33 | nan | nan | nan | Cerrado | 1.4 |
| 60563eb7-cabf-34b7-a50f-65354e20795f | -9.84588 | -44.88455 | 2025-10-30 04:25:00 | NOAA-20 | RIACHO FRIO | PIAUÍ | Brasil | 2208858 | 22 | 33 | nan | nan | nan | Cerrado | 1.3 |
| 90d2ccd5-2b12-3023-a083-d051ae1edb15 | -8.32449 | -47.92216 | 2025-10-30 04:25:00 | NOAA-20 | ITACAJÁ | TOCANTINS | Brasil | 1710508 | 17 | 33 | nan | nan | nan | Cerrado | 3.1 |
| 6c622334-ea93-3b1e-9c7d-91df43e0c3dd | -7.43656 | -44.24577 | 2025-10-30 04:25:00 | NOAA-20 | SEBASTIÃO LEAL | PIAUÍ | Brasil | 2210631 | 22 | 33 | nan | nan | nan | Cerrado | 1.2 |
| fe30063f-9a3f-3cbd-b48c-4304e947968f | -9.90341 | -48.16253 | 2025-10-30 04:25:00 | NOAA-20 | TOCANTÍNIA | TOCANTINS | Brasil | 1721109 | 17 | 33 | nan | nan | nan | Cerrado | 1.1 |
| de3e67bc-6b2a-3ae6-9c1c-c2a79b5c3ac9 | -7.9236 | -45.49087 | 2025-10-30 04:25:00 | NOAA-20 | RIBEIRO GONÇALVES | PIAUÍ | Brasil | 2208908 | 22 | 33 | nan | nan | nan | Cerrado | 4.0 |
| 869c1776-cbda-3a61-b3aa-cef72b1fddf8 | -7.91935 | -39.71846 | 2025-10-30 04:25:00 | NOAA-20 | PARNAMIRIM | PERNAMBUCO | Brasil | 2610400 | 26 | 33 | nan | nan | nan | Caatinga | 1.1 |
| 1f537a40-0421-3a68-aa45-a8ff8516fe03 | -7.2151 | -43.39414 | 2025-10-30 04:25:00 | NOAA-20 | JERUMENHA | PIAUÍ | Brasil | 2205300 | 22 | 33 | nan | nan | nan | Caatinga | 1.3 |
| b588a0e0-d76e-3197-901e-c987d43c49ad | -7.30133 | -46.64098 | 2025-10-30 04:25:00 | NOAA-20 | RIACHÃO | MARANHÃO | Brasil | 2109502 | 21 | 33 | nan | nan | nan | Cerrado | 1.9 |
| 1c5c82be-3d62-3bc4-889b-e655f51818c3 | -5.04084 | -44.87799 | 2025-10-30 04:25:00 | NOAA-20 | BARRA DO CORDA | MARANHÃO | Brasil | 2101608 | 21 | 33 | nan | nan | nan | Cerrado | 3.6 |
| 785b0053-6ea0-35dc-8aaf-04f4075ea15d | -8.32639 | -47.92223 | 2025-10-30 04:25:00 | NOAA-20 | ITACAJÁ | TOCANTINS | Brasil | 1710508 | 17 | 33 | nan | nan | nan | Cerrado | 5.7 |
| 7ddff1ed-8d31-3435-88a9-ad81d65eed46 | -3.94007 | -50.32763 | 2025-10-30 04:25:00 | NOAA-20 | PACAJÁ | PARÁ | Brasil | 1505486 | 15 | 33 | nan | nan | nan | Amazônia | 0.9 |
| 32f8fe93-82f9-3d65-9188-9a22ba7d4cbc | -7.61845 | -43.57183 | 2025-10-30 04:25:00 | NOAA-20 | CANAVIEIRA | PIAUÍ | Brasil | 2202251 | 22 | 33 | nan | nan | nan | Cerrado | 1.9 |
| f8475de1-881d-3b2e-be15-954246f842a1 | -6.13161 | -41.70103 | 2025-10-30 04:25:00 | NOAA-20 | AROAZES | PIAUÍ | Brasil | 2200905 | 22 | 33 | nan | nan | nan | Caatinga | 2.6 |
| fc1f2d8a-9f29-3178-8ca4-7fbbcbc80922 | -7.5816 | -43.64847 | 2025-10-30 04:25:00 | NOAA-20 | CANAVIEIRA | PIAUÍ | Brasil | 2202251 | 22 | 33 | nan | nan | nan | Cerrado | 4.8 |
| ec14d4ab-3844-36e3-a2a7-1ac2ba7c94ac | -9.81312 | -44.72742 | 2025-10-30 04:25:00 | NOAA-20 | RIACHO FRIO | PIAUÍ | Brasil | 2208858 | 22 | 33 | nan | nan | nan | Cerrado | 1.7 |
| 0dc60fd8-65f9-3099-8544-5501635ab751 | -11.46226 | -48.5289 | 2025-10-30 04:25:00 | NOAA-20 | PEIXE | TOCANTINS | Brasil | 1716604 | 17 | 33 | nan | nan | nan | Cerrado | 1.2 |
| e6840a7c-05a0-3d60-a0ca-d1701bf5adaa | -7.95742 | -46.72463 | 2025-10-30 04:25:00 | NOAA-20 | CAMPOS LINDOS | TOCANTINS | Brasil | 1703842 | 17 | 33 | nan | nan | nan | Cerrado | 3.0 |
| dbcc8487-53a9-3ffa-ad51-3b048ec22129 | -3.88386 | -51.19215 | 2025-10-30 04:25:00 | NOAA-20 | PACAJÁ | PARÁ | Brasil | 1505486 | 15 | 33 | nan | nan | nan | Amazônia | 1.1 |
| 650cced1-5e41-32e7-badc-b314cc73b86e | -7.09844 | -46.52736 | 2025-10-30 04:25:00 | NOAA-20 | FEIRA NOVA DO MARANHÃO | MARANHÃO | Brasil | 2104073 | 21 | 33 | nan | nan | nan | Cerrado | 1.3 |
| 643e9716-8bb6-3a35-ad10-569f6bccba1e | -6.79379 | -43.09059 | 2025-10-30 04:25:00 | NOAA-20 | FLORIANO | PIAUÍ | Brasil | 2203909 | 22 | 33 | nan | nan | nan | Cerrado | 4.3 |
| 2d80991a-73d4-3a69-8710-2c38dae07568 | -5.65007 | -48.02174 | 2025-10-30 04:25:00 | NOAA-20 | ARAGUATINS | TOCANTINS | Brasil | 1702208 | 17 | 33 | nan | nan | nan | Amazônia | 0.5 |
| f5a87099-3eb9-3a95-8cfc-3d151fccda05 | -6.08589 | -41.78506 | 2025-10-30 04:25:00 | NOAA-20 | AROAZES | PIAUÍ | Brasil | 2200905 | 22 | 33 | nan | nan | nan | Caatinga | 3.1 |
| 912a37df-0fac-3155-8bfe-6adbf7df8c01 | -3.66463 | -51.71127 | 2025-10-30 04:25:00 | NOAA-20 | SENADOR JOSÉ PORFÍRIO | PARÁ | Brasil | 1507805 | 15 | 33 | nan | nan | nan | Amazônia | 1.6 |
| b56cd2a2-26b3-3890-874d-aa94e8bb5dd7 | -10.35437 | -47.27405 | 2025-10-30 04:25:00 | NOAA-20 | NOVO ACORDO | TOCANTINS | Brasil | 1715101 | 17 | 33 | nan | nan | nan | Cerrado | 3.2 |
| 2bf695bb-2fc7-3e7c-9975-d67d250fc52e | -10.8447 | -47.73775 | 2025-10-30 04:25:00 | NOAA-20 | PONTE ALTA DO TOCANTINS | TOCANTINS | Brasil | 1717909 | 17 | 33 | nan | nan | nan | Cerrado | 1.4 |
| cba51f51-b54d-3543-b668-6de359557916 | -7.42011 | -44.67041 | 2025-10-30 04:25:00 | NOAA-20 | URUÇUÍ | PIAUÍ | Brasil | 2211209 | 22 | 33 | nan | nan | nan | Cerrado | 2.4 |
| 81126d34-c71e-310d-adf3-9466a49cb446 | -10.26873 | -44.5799 | 2025-10-30 04:25:00 | NOAA-20 | PARNAGUÁ | PIAUÍ | Brasil | 2207603 | 22 | 33 | nan | nan | nan | Cerrado | 1.9 |
| 56b549c1-be7b-31e4-bf7b-9754a72f299c | -10.99285 | -47.87389 | 2025-10-30 04:25:00 | NOAA-20 | SILVANÓPOLIS | TOCANTINS | Brasil | 1720655 | 17 | 33 | nan | nan | nan | Cerrado | 1.0 |
| 16d55b13-00ea-3730-89da-cd43447ab7f3 | -7.30694 | -44.97659 | 2025-10-30 04:25:00 | NOAA-20 | SÃO FÉLIX DE BALSAS | MARANHÃO | Brasil | 2110807 | 21 | 33 | nan | nan | nan | Cerrado | 2.7 |
| d14d380a-886b-3199-aad0-097282d23755 | -8.70551 | -47.97972 | 2025-10-30 04:25:00 | NOAA-20 | SANTA MARIA DO TOCANTINS | TOCANTINS | Brasil | 1718881 | 17 | 33 | nan | nan | nan | Cerrado | 1.4 |
| 75a64688-df78-3e38-9205-a2627380aa5b | -9.81227 | -47.58456 | 2025-10-30 04:25:00 | NOAA-20 | RIO SONO | TOCANTINS | Brasil | 1718758 | 17 | 33 | nan | nan | nan | Cerrado | 1.4 |
| 578eb099-d662-3607-838d-8e3bedd95a8b | -9.81615 | -47.58159 | 2025-10-30 04:25:00 | NOAA-20 | RIO SONO | TOCANTINS | Brasil | 1718758 | 17 | 33 | nan | nan | nan | Cerrado | 1.6 |
| 2a75caf3-03e6-3d5a-bb04-9b81c6a860c3 | -9.86291 | -47.69379 | 2025-10-30 04:25:00 | NOAA-20 | RIO SONO | TOCANTINS | Brasil | 1718758 | 17 | 33 | nan | nan | nan | Cerrado | 0.8 |
| 3d36db5a-5049-352b-891b-cc44cf0e3e62 | -11.10184 | -44.70502 | 2025-10-30 04:25:00 | NOAA-20 | SANTA RITA DE CÁSSIA | BAHIA | Brasil | 2928406 | 29 | 33 | nan | nan | nan | Cerrado | 0.8 |
| 524d2503-efe6-33df-812f-09135ef89485 | -6.95822 | -44.8459 | 2025-10-30 04:25:00 | NOAA-20 | SÃO FÉLIX DE BALSAS | MARANHÃO | Brasil | 2110807 | 21 | 33 | nan | nan | nan | Cerrado | 1.4 |
| 7d2e758e-7dc6-371b-9afa-c8aed5e4d1e3 | -7.30975 | -44.98071 | 2025-10-30 04:25:00 | NOAA-20 | SÃO FÉLIX DE BALSAS | MARANHÃO | Brasil | 2110807 | 21 | 33 | nan | nan | nan | Cerrado | 7.1 |
| e195ad92-8c80-30db-b7db-ae04c36d961e | -7.35117 | -47.62975 | 2025-10-30 04:25:00 | NOAA-20 | FILADÉLFIA | TOCANTINS | Brasil | 1707702 | 17 | 33 | nan | nan | nan | Cerrado | 2.5 |
| 4fa2b746-18f7-3b72-ae2b-df3eef4ccc08 | -10.95366 | -47.84237 | 2025-10-30 04:25:00 | NOAA-20 | SILVANÓPOLIS | TOCANTINS | Brasil | 1720655 | 17 | 33 | nan | nan | nan | Cerrado | 1.5 |
| aee422b9-e6db-3a6c-848e-b58271553006 | -7.39699 | -43.65099 | 2025-10-30 04:25:00 | NOAA-20 | CANAVIEIRA | PIAUÍ | Brasil | 2202251 | 22 | 33 | nan | nan | nan | Caatinga | 1.6 |
| e5ec71b8-a729-30c9-9b1d-be370b0a5cd2 | -4.46809 | -45.75706 | 2025-10-30 04:25:00 | NOAA-20 | BREJO DE AREIA | MARANHÃO | Brasil | 2102150 | 21 | 33 | nan | nan | nan | Amazônia | 2.1 |
| ab5dc0d1-238d-3627-8d9d-f294d1821269 | -10.26173 | -44.57895 | 2025-10-30 04:25:00 | NOAA-20 | PARNAGUÁ | PIAUÍ | Brasil | 2207603 | 22 | 33 | nan | nan | nan | Cerrado | 13.3 |
| 3c02b682-e3a8-338b-8551-14da823ce789 | -6.11289 | -41.71073 | 2025-10-30 04:25:00 | NOAA-20 | AROAZES | PIAUÍ | Brasil | 2200905 | 22 | 33 | nan | nan | nan | Caatinga | 2.9 |
| eb088235-6272-3d62-a7b3-70c2f3f6404c | -5.03643 | -45.16724 | 2025-10-30 04:25:00 | NOAA-20 | SÃO RAIMUNDO DO DOCA BEZERRA | MARANHÃO | Brasil | 2111631 | 21 | 33 | nan | nan | nan | Cerrado | 1.8 |
| c6c54d73-1ab2-36ba-827d-fc04360b6d42 | -10.84885 | -50.12619 | 2025-10-30 04:25:00 | NOAA-20 | LAGOA DA CONFUSÃO | TOCANTINS | Brasil | 1711902 | 17 | 33 | nan | nan | nan | Cerrado | 1.0 |
| bedb2185-f5dd-398c-a2a3-305f024d54b4 | -11.33445 | -47.96994 | 2025-10-30 04:25:00 | NOAA-20 | SANTA ROSA DO TOCANTINS | TOCANTINS | Brasil | 1718907 | 17 | 33 | nan | nan | nan | Cerrado | 1.1 |
| 0e9dfda3-e149-30f0-be65-30bfbd9ecfd8 | -4.52596 | -54.9678 | 2025-10-30 04:25:00 | NOAA-20 | RURÓPOLIS | PARÁ | Brasil | 1506195 | 15 | 33 | nan | nan | nan | Amazônia | 1.0 |
| b6cd4b8a-edb1-3b83-8827-f7a9be1c9ea3 | -6.12525 | -41.70756 | 2025-10-30 04:25:00 | NOAA-20 | AROAZES | PIAUÍ | Brasil | 2200905 | 22 | 33 | nan | nan | nan | Caatinga | 4.7 |
| f2fab22d-a51e-38bd-b84c-07c268ea1152 | -9.90099 | -47.79396 | 2025-10-30 04:25:00 | NOAA-20 | RIO SONO | TOCANTINS | Brasil | 1718758 | 17 | 33 | nan | nan | nan | Cerrado | 0.9 |
| f084c23d-c57a-3f68-9b56-ed6b6a125c77 | -7.95852 | -46.7177 | 2025-10-30 04:25:00 | NOAA-20 | CAMPOS LINDOS | TOCANTINS | Brasil | 1703842 | 17 | 33 | nan | nan | nan | Cerrado | 1.4 |
| 26e0930f-f0b5-3d2c-868c-a9426391e078 | -10.87369 | -48.00316 | 2025-10-30 04:25:00 | NOAA-20 | MONTE DO CARMO | TOCANTINS | Brasil | 1713601 | 17 | 33 | nan | nan | nan | Cerrado | 1.7 |
| 449814dc-e989-3715-a545-695a6c991890 | -11.52986 | -44.967 | 2025-10-30 04:25:00 | NOAA-20 | RIACHÃO DAS NEVES | BAHIA | Brasil | 2926202 | 29 | 33 | nan | nan | nan | Cerrado | 3.7 |
| 95c50aa0-5ded-31d5-bc32-11f92de2932a | -7.79628 | -46.4111 | 2025-10-30 04:25:00 | NOAA-20 | BALSAS | MARANHÃO | Brasil | 2101400 | 21 | 33 | nan | nan | nan | Cerrado | 2.2 |
| a679c01d-98f1-3ff1-bd18-eb376844a1ca | -11.36871 | -47.75497 | 2025-10-30 04:25:00 | NOAA-20 | CHAPADA DA NATIVIDADE | TOCANTINS | Brasil | 1705102 | 17 | 33 | nan | nan | nan | Cerrado | 1.7 |
| c966ca45-2ad9-325d-83ce-632b5c461f43 | -7.20509 | -46.04453 | 2025-10-30 04:25:00 | NOAA-20 | BALSAS | MARANHÃO | Brasil | 2101400 | 21 | 33 | nan | nan | nan | Cerrado | 0.9 |
| b60fca6a-4013-3dcd-ba86-df9549d89ad3 | -5.78959 | -40.819 | 2025-10-30 04:25:00 | NOAA-20 | QUITERIANÓPOLIS | CEARÁ | Brasil | 2311264 | 23 | 33 | nan | nan | nan | Caatinga | 1.0 |
| b2ca85c9-09f3-37d2-9e2e-7db8950ac1e9 | -6.1076 | -41.71954 | 2025-10-30 04:25:00 | NOAA-20 | AROAZES | PIAUÍ | Brasil | 2200905 | 22 | 33 | nan | nan | nan | Caatinga | 3.4 |
| 91f6aca2-7651-376f-b0ae-c02aa8022fcc | -4.81359 | -45.69832 | 2025-10-30 04:25:00 | NOAA-20 | MARAJÁ DO SENA | MARANHÃO | Brasil | 2106359 | 21 | 33 | nan | nan | nan | Amazônia | 0.9 |
| 17e87fe7-001e-3cc0-8933-82737a84dbbf | -11.20493 | -47.56662 | 2025-10-30 04:25:00 | NOAA-20 | PINDORAMA DO TOCANTINS | TOCANTINS | Brasil | 1717008 | 17 | 33 | nan | nan | nan | Cerrado | 0.4 |
| 5c2c0ca6-67ad-3466-ac61-0003d316657c | -7.27759 | -46.05988 | 2025-10-30 04:25:00 | NOAA-20 | BALSAS | MARANHÃO | Brasil | 2101400 | 21 | 33 | nan | nan | nan | Cerrado | 0.7 |
| 0afc88e1-2268-3048-a0c6-fd753bf78d80 | -6.95766 | -44.84948 | 2025-10-30 04:25:00 | NOAA-20 | SÃO FÉLIX DE BALSAS | MARANHÃO | Brasil | 2110807 | 21 | 33 | nan | nan | nan | Cerrado | 1.4 |
| 991d3b55-675f-30fa-9bb3-36f8476adb0f | -7.95523 | -46.73849 | 2025-10-30 04:25:00 | NOAA-20 | CAMPOS LINDOS | TOCANTINS | Brasil | 1703842 | 17 | 33 | nan | nan | nan | Cerrado | 1.6 |
| b953aa4e-8bb1-32dc-a9e2-b8e6e0a4e8e5 | -6.14299 | -41.69511 | 2025-10-30 04:25:00 | NOAA-20 | PIMENTEIRAS | PIAUÍ | Brasil | 2208106 | 22 | 33 | nan | nan | nan | Caatinga | 3.4 |
| 1f33b4b7-ff55-3eb9-bdec-0aeccaa811a5 | -10.9929 | -47.85234 | 2025-10-30 04:25:00 | NOAA-20 | SILVANÓPOLIS | TOCANTINS | Brasil | 1720655 | 17 | 33 | nan | nan | nan | Cerrado | 1.7 |


[Clique aqui para ver as próximas entradas](README44.md)
