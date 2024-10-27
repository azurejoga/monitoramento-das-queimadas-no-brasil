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

## Dados Diários - Página 30

| ID | Latitude | Longitude | Data/Hora GMT | Satélite | Município | Estado | País | Município ID | Estado ID | País ID | Dias sem Chuva | Precipitação | Risco de Fogo | Bioma | FRP |
|----|----------|-----------|---------------|----------|-----------|--------|------|--------------|-----------|---------|----------------|--------------|----------------|-------|-----|
| 2157e2f6-da45-3b64-b15a-dfeccf1133d2 | -2.79911 | -42.65284 | 2024-10-27 03:57:00 | NPP-375D | PAULINO NEVES | MARANHÃO | Brasil | 2108058 | 21 | 33 | nan | nan | nan | Cerrado | 3.4 |
| 886e416a-59f0-39a1-bd33-93ba5f418209 | -2.79539 | -42.65224 | 2024-10-27 03:57:00 | NPP-375D | PAULINO NEVES | MARANHÃO | Brasil | 2108058 | 21 | 33 | nan | nan | nan | Cerrado | 2.2 |
| 10c69a14-2dd2-3701-854c-4b3c6e606590 | -2.78597 | -42.47643 | 2024-10-27 03:57:00 | NPP-375D | PAULINO NEVES | MARANHÃO | Brasil | 2108058 | 21 | 33 | nan | nan | nan | Cerrado | 1.3 |
| b1ab81f7-b7b4-3878-8fad-029c0aa8f424 | -2.52066 | -44.14188 | 2024-10-27 03:57:00 | NPP-375D | PAÇO DO LUMIAR | MARANHÃO | Brasil | 2107506 | 21 | 33 | nan | nan | nan | Amazônia | 1.4 |
| 807f1752-607a-3bfd-b045-7333af181059 | -2.51744 | -44.14164 | 2024-10-27 03:57:00 | NPP-375D | PAÇO DO LUMIAR | MARANHÃO | Brasil | 2107506 | 21 | 33 | nan | nan | nan | Amazônia | 3.0 |
| 91d450a4-3779-3269-8333-277f9d60fa39 | -2.51657 | -44.14124 | 2024-10-27 03:57:00 | NPP-375D | PAÇO DO LUMIAR | MARANHÃO | Brasil | 2107506 | 21 | 33 | nan | nan | nan | Amazônia | 1.4 |
| 8100c85c-8267-3b30-86a8-b48004e557ef | -2.50631 | -44.13243 | 2024-10-27 03:57:00 | NPP-375D | PAÇO DO LUMIAR | MARANHÃO | Brasil | 2107506 | 21 | 33 | nan | nan | nan | Amazônia | 2.3 |
| 21685897-7c22-3a7d-8f8b-3b28656ce24c | -2.50573 | -44.13607 | 2024-10-27 03:57:00 | NPP-375D | PAÇO DO LUMIAR | MARANHÃO | Brasil | 2107506 | 21 | 33 | nan | nan | nan | Amazônia | 2.2 |
| 80456e43-622c-3414-917f-dd35b40e2ed8 | -2.46411 | -44.9407 | 2024-10-27 03:57:00 | NPP-375D | BEQUIMÃO | MARANHÃO | Brasil | 2101905 | 21 | 33 | nan | nan | nan | Amazônia | 0.9 |
| de9a5493-596b-3ebe-ad8e-cac1d77675dc | -2.45979 | -44.94 | 2024-10-27 03:57:00 | NPP-375D | BEQUIMÃO | MARANHÃO | Brasil | 2101905 | 21 | 33 | nan | nan | nan | Amazônia | 2.3 |
| 73b70596-2e2d-34b4-b1dc-9d8828a43ef7 | -2.45613 | -44.93521 | 2024-10-27 03:57:00 | NPP-375D | BEQUIMÃO | MARANHÃO | Brasil | 2101905 | 21 | 33 | nan | nan | nan | Amazônia | 1.0 |
| 4ffad514-6257-34ad-8a02-7b9b9146064a | -1.97712 | -46.63573 | 2024-10-27 03:57:00 | NPP-375D | VISEU | PARÁ | Brasil | 1508308 | 15 | 33 | nan | nan | nan | Amazônia | 2.3 |
| f4c673af-8c10-3de5-b19d-26268c1a8a25 | -1.79598 | -46.39431 | 2024-10-27 03:57:00 | NPP-375D | CACHOEIRA DO PIRIÁ | PARÁ | Brasil | 1501956 | 15 | 33 | nan | nan | nan | Amazônia | 1.4 |
| 865da1c3-6453-3430-a507-97a9d1c5f81c | -1.79116 | -46.39344 | 2024-10-27 03:57:00 | NPP-375D | CACHOEIRA DO PIRIÁ | PARÁ | Brasil | 1501956 | 15 | 33 | nan | nan | nan | Amazônia | 1.4 |
| d3e3f195-717d-371a-9f6c-0866c12b5dd3 | -1.66798 | -46.55262 | 2024-10-27 03:57:00 | NPP-375D | CACHOEIRA DO PIRIÁ | PARÁ | Brasil | 1501956 | 15 | 33 | nan | nan | nan | Amazônia | 1.7 |
| 9fe23757-0c50-3469-b13c-063139c07ef2 | -2.34447 | -46.20356 | 2024-10-27 03:57:00 | NPP-375D | CENTRO NOVO DO MARANHÃO | MARANHÃO | Brasil | 2103174 | 21 | 33 | nan | nan | nan | Amazônia | 1.8 |
| f02df961-bf07-3102-92cd-606a82c5accd | -2.26788 | -46.13338 | 2024-10-27 03:57:00 | NPP-375D | CENTRO DO GUILHERME | MARANHÃO | Brasil | 2103158 | 21 | 33 | nan | nan | nan | Amazônia | 1.7 |
| cda48631-7b7b-38f9-a243-846cf7abfcf5 | -2.19163 | -46.42294 | 2024-10-27 03:57:00 | NPP-375D | CACHOEIRA DO PIRIÁ | PARÁ | Brasil | 1501956 | 15 | 33 | nan | nan | nan | Amazônia | 1.4 |
| b305ead8-4db5-3fa4-8a9d-95db650f8e39 | -1.78817 | -48.43861 | 2024-10-27 03:57:00 | NPP-375D | ACARÁ | PARÁ | Brasil | 1500206 | 15 | 33 | nan | nan | nan | Amazônia | 1.2 |
| 90daa940-696d-3dba-96ad-52d9e313417b | -1.78758 | -48.44228 | 2024-10-27 03:57:00 | NPP-375D | ACARÁ | PARÁ | Brasil | 1500206 | 15 | 33 | nan | nan | nan | Amazônia | 1.0 |
| efa2410b-fb03-3f0f-8068-fb6f72014441 | -1.53161 | -47.20848 | 2024-10-27 03:57:00 | NPP-375D | OURÉM | PARÁ | Brasil | 1505403 | 15 | 33 | nan | nan | nan | Amazônia | 0.5 |
| 65bbc07b-9172-3678-bbbc-f17ff85198fd | -1.52698 | -47.20456 | 2024-10-27 03:57:00 | NPP-375D | OURÉM | PARÁ | Brasil | 1505403 | 15 | 33 | nan | nan | nan | Amazônia | 0.6 |
| 44d48490-01f2-35a6-b8eb-1e458ba386d5 | -1.5265 | -47.20754 | 2024-10-27 03:57:00 | NPP-375D | OURÉM | PARÁ | Brasil | 1505403 | 15 | 33 | nan | nan | nan | Amazônia | 0.6 |
| 2729a76d-31ca-3d7a-a3b9-eb5415edcd8a | 1.78317 | -50.45757 | 2024-10-27 03:57:00 | NPP-375D | AMAPÁ | AMAPÁ | Brasil | 1600105 | 16 | 33 | nan | nan | nan | Amazônia | 0.6 |
| 4d040dad-477c-3989-b1ad-4122ff670374 | 1.78061 | -50.46324 | 2024-10-27 03:57:00 | NPP-375D | AMAPÁ | AMAPÁ | Brasil | 1600105 | 16 | 33 | nan | nan | nan | Amazônia | 3.0 |
| a7a6533d-0512-37bd-886d-ffcce764564b | 1.77972 | -50.45751 | 2024-10-27 03:57:00 | NPP-375D | AMAPÁ | AMAPÁ | Brasil | 1600105 | 16 | 33 | nan | nan | nan | Amazônia | 2.6 |
| bcce2073-08af-3ab8-b661-629850efefd9 | 1.77907 | -50.47589 | 2024-10-27 03:57:00 | NPP-375D | AMAPÁ | AMAPÁ | Brasil | 1600105 | 16 | 33 | nan | nan | nan | Amazônia | 2.1 |
| 80a6c93a-2a62-3304-bce9-eacdb9b28d85 | 1.77822 | -50.47014 | 2024-10-27 03:57:00 | NPP-375D | AMAPÁ | AMAPÁ | Brasil | 1600105 | 16 | 33 | nan | nan | nan | Amazônia | 2.1 |
| 1a2d1df1-3dbc-3ae9-897c-b33c85c501aa | 1.77738 | -50.46438 | 2024-10-27 03:57:00 | NPP-375D | AMAPÁ | AMAPÁ | Brasil | 1600105 | 16 | 33 | nan | nan | nan | Amazônia | 4.0 |
| f0d8d1fc-d273-3081-bd7f-ee6108ec4aed | 1.77574 | -50.47579 | 2024-10-27 03:57:00 | NPP-375D | AMAPÁ | AMAPÁ | Brasil | 1600105 | 16 | 33 | nan | nan | nan | Amazônia | 2.9 |
| 20fdfad3-462c-3d91-8b8b-bc0606c25083 | 1.77397 | -50.46431 | 2024-10-27 03:57:00 | NPP-375D | AMAPÁ | AMAPÁ | Brasil | 1600105 | 16 | 33 | nan | nan | nan | Amazônia | 3.0 |
| 414268e8-876e-351c-bf3f-f4408ea97ee7 | 3.4053 | -51.29803 | 2024-10-27 03:57:00 | NPP-375D | OIAPOQUE | AMAPÁ | Brasil | 1600501 | 16 | 33 | nan | nan | nan | Amazônia | 1.5 |
| fde1dd2d-f462-3239-a21c-56b23448115f | 3.40112 | -51.30014 | 2024-10-27 03:57:00 | NPP-375D | OIAPOQUE | AMAPÁ | Brasil | 1600501 | 16 | 33 | nan | nan | nan | Amazônia | 2.4 |
| 30e2cd4a-8968-3482-824a-2c795a2c3600 | 3.40014 | -51.2932 | 2024-10-27 03:57:00 | NPP-375D | OIAPOQUE | AMAPÁ | Brasil | 1600501 | 16 | 33 | nan | nan | nan | Amazônia | 1.9 |
| 0a54f774-51aa-386d-8700-805bae957c7f | 3.39915 | -51.28624 | 2024-10-27 03:57:00 | NPP-375D | OIAPOQUE | AMAPÁ | Brasil | 1600501 | 16 | 33 | nan | nan | nan | Amazônia | 1.9 |
| 519c53d3-7e39-3df3-9bf6-a57c41e7b561 | 3.39714 | -51.29214 | 2024-10-27 03:57:00 | NPP-375D | OIAPOQUE | AMAPÁ | Brasil | 1600501 | 16 | 33 | nan | nan | nan | Amazônia | 3.2 |
| 60152752-ccc7-3a6a-a822-6027a7a4f761 | 3.39611 | -51.28518 | 2024-10-27 03:57:00 | NPP-375D | OIAPOQUE | AMAPÁ | Brasil | 1600501 | 16 | 33 | nan | nan | nan | Amazônia | 2.4 |
| 80c0e9e9-489a-386b-b114-5617bc3c5cd7 | -7.25397 | -41.2309 | 2024-10-27 04:00:00 | NPP-375D | GEMINIANO | PIAUÍ | Brasil | 2204352 | 22 | 33 | nan | nan | nan | Caatinga | 6.0 |
| c7aecf91-1a88-3d3b-90da-eb91f04c085d | -7.25175 | -41.22327 | 2024-10-27 04:00:00 | NPP-375D | GEMINIANO | PIAUÍ | Brasil | 2204352 | 22 | 33 | nan | nan | nan | Caatinga | 1.2 |
| 914e6868-8083-3c7f-8c66-c61d693bba6f | -7.54934 | -38.75238 | 2024-10-27 04:00:00 | NPP-375D | MAURITI | CEARÁ | Brasil | 2308104 | 23 | 33 | nan | nan | nan | Caatinga | 2.1 |
| 7479c1b5-257b-3e6b-8e0b-6d598ebdd36c | -6.72989 | -40.50701 | 2024-10-27 04:00:00 | NPP-375D | AIUABA | CEARÁ | Brasil | 2300408 | 23 | 33 | nan | nan | nan | Caatinga | 1.0 |
| 9c656765-9f99-3990-abaf-233346e2a370 | -7.00139 | -35.63294 | 2024-10-27 04:00:00 | NPP-375D | ALAGOA GRANDE | PARAÍBA | Brasil | 2500304 | 25 | 33 | nan | nan | nan | Caatinga | 1.3 |
| 34754950-1fab-3733-bc1c-09ff27df1c11 | -5.46923 | -36.80847 | 2024-10-27 04:00:00 | NPP-375D | IPANGUAÇU | RIO GRANDE DO NORTE | Brasil | 2404705 | 24 | 33 | nan | nan | nan | Caatinga | 1.0 |
| 86ba2e4e-740a-3fcc-98e9-6dbd639b390a | -7.47784 | -37.40587 | 2024-10-27 04:00:00 | NPP-375D | SANTA TEREZINHA | PERNAMBUCO | Brasil | 2612802 | 26 | 33 | nan | nan | nan | Caatinga | 2.3 |
| b4a8590a-67a0-317f-8568-e7cfb4debd75 | -7.47769 | -37.40474 | 2024-10-27 04:00:00 | NPP-375D | SANTA TEREZINHA | PERNAMBUCO | Brasil | 2612802 | 26 | 33 | nan | nan | nan | Caatinga | 2.4 |
| 27590a3a-a867-3f58-a097-66ab5e5ffa59 | -8.55541 | -36.38107 | 2024-10-27 04:00:00 | NPP-375D | SÃO BENTO DO UNA | PERNAMBUCO | Brasil | 2613008 | 26 | 33 | nan | nan | nan | Caatinga | 0.8 |
| d73474a4-1e1e-3527-acfd-0550f62fc6cc | -5.93934 | -38.12939 | 2024-10-27 04:00:00 | NPP-375D | RODOLFO FERNANDES | RIO GRANDE DO NORTE | Brasil | 2411007 | 24 | 33 | nan | nan | nan | Caatinga | 1.0 |
| 1d1b04a1-743b-39fe-a372-3da28a032e13 | -5.93537 | -38.13251 | 2024-10-27 04:00:00 | NPP-375D | RODOLFO FERNANDES | RIO GRANDE DO NORTE | Brasil | 2411007 | 24 | 33 | nan | nan | nan | Caatinga | 0.6 |
| 4e02b36a-96ce-3284-ac33-76770f9128b9 | -5.68817 | -38.03934 | 2024-10-27 04:00:00 | NPP-375D | APODI | RIO GRANDE DO NORTE | Brasil | 2401008 | 24 | 33 | nan | nan | nan | Caatinga | 2.0 |
| c2d5ca61-a1b3-3b47-a647-d8783bbd9068 | -7.56339 | -38.75093 | 2024-10-27 04:00:00 | NPP-375D | MAURITI | CEARÁ | Brasil | 2308104 | 23 | 33 | nan | nan | nan | Caatinga | 3.4 |
| d768bd67-4d6f-3b4c-991f-87d08ca2119f | -7.56283 | -38.75452 | 2024-10-27 04:00:00 | NPP-375D | MAURITI | CEARÁ | Brasil | 2308104 | 23 | 33 | nan | nan | nan | Caatinga | 3.4 |
| 5c1fcc02-314e-360f-8a9c-82bd99b64fac | -7.56001 | -38.7504 | 2024-10-27 04:00:00 | NPP-375D | MAURITI | CEARÁ | Brasil | 2308104 | 23 | 33 | nan | nan | nan | Caatinga | 3.4 |
| 2d10d6ba-df48-31b4-a562-41a1366369de | -7.55946 | -38.75398 | 2024-10-27 04:00:00 | NPP-375D | MAURITI | CEARÁ | Brasil | 2308104 | 23 | 33 | nan | nan | nan | Caatinga | 3.4 |
| 8ab88ef7-aa35-35f9-807c-8aa60b252b5f | -7.55664 | -38.74985 | 2024-10-27 04:00:00 | NPP-375D | MAURITI | CEARÁ | Brasil | 2308104 | 23 | 33 | nan | nan | nan | Caatinga | 2.3 |
| ac1d25bc-05a4-30a1-9411-e05c6f996ee1 | -7.55609 | -38.75343 | 2024-10-27 04:00:00 | NPP-375D | MAURITI | CEARÁ | Brasil | 2308104 | 23 | 33 | nan | nan | nan | Caatinga | 2.3 |
| 70a899f8-be44-36e2-8b5b-9a884b91747c | -7.55271 | -38.7529 | 2024-10-27 04:00:00 | NPP-375D | MAURITI | CEARÁ | Brasil | 2308104 | 23 | 33 | nan | nan | nan | Caatinga | 2.3 |
| cc6db3e4-9c49-38cd-be9c-a34e8195007b | -7.48614 | -39.04983 | 2024-10-27 04:00:00 | NPP-375D | BREJO SANTO | CEARÁ | Brasil | 2302503 | 23 | 33 | nan | nan | nan | Caatinga | 1.5 |
| 07a0b77c-d8cd-3f5e-b3e5-7abede83cd1d | -7.29096 | -38.93568 | 2024-10-27 04:00:00 | NPP-375D | MILAGRES | CEARÁ | Brasil | 2308302 | 23 | 33 | nan | nan | nan | Caatinga | 1.7 |
| 9359a1b7-a840-318e-9715-914473b4abe7 | -7.26464 | -38.92802 | 2024-10-27 04:00:00 | NPP-375D | MILAGRES | CEARÁ | Brasil | 2308302 | 23 | 33 | nan | nan | nan | Caatinga | 0.9 |
| bf6c33d8-5469-39eb-8e3a-0ae265b38f89 | -7.26128 | -38.92751 | 2024-10-27 04:00:00 | NPP-375D | MILAGRES | CEARÁ | Brasil | 2308302 | 23 | 33 | nan | nan | nan | Caatinga | 0.9 |
| 7bfbeeaa-d94b-3af0-939b-ad70288d3b04 | -7.16479 | -38.87243 | 2024-10-27 04:00:00 | NPP-375D | BARRO | CEARÁ | Brasil | 2302008 | 23 | 33 | nan | nan | nan | Caatinga | 1.1 |
| fb953a27-4d0e-3730-9cbd-40940be6083b | -8.27029 | -39.05317 | 2024-10-27 04:00:00 | NPP-375D | SALGUEIRO | PERNAMBUCO | Brasil | 2612208 | 26 | 33 | nan | nan | nan | Caatinga | 1.2 |
| ca1169a5-9442-38cd-b637-4da4871b55e9 | -7.88334 | -39.16927 | 2024-10-27 04:00:00 | NPP-375D | SALGUEIRO | PERNAMBUCO | Brasil | 2612208 | 26 | 33 | nan | nan | nan | Caatinga | 1.7 |
| d14de308-22fa-38ae-a778-ab7930e24c98 | -7.88279 | -39.17281 | 2024-10-27 04:00:00 | NPP-375D | SALGUEIRO | PERNAMBUCO | Brasil | 2612208 | 26 | 33 | nan | nan | nan | Caatinga | 2.0 |
| e7a07ae8-c707-317c-969b-7ba13f3091d3 | -4.46289 | -38.74274 | 2024-10-27 04:00:00 | NPP-375D | ARACOIABA | CEARÁ | Brasil | 2301208 | 23 | 33 | nan | nan | nan | Caatinga | 4.8 |
| 2daa3a81-3bd8-3b05-b1b6-fef42a002264 | -4.3368 | -39.13882 | 2024-10-27 04:00:00 | NPP-375D | CANINDÉ | CEARÁ | Brasil | 2302800 | 23 | 33 | nan | nan | nan | Caatinga | 2.5 |
| 33ab84bf-ae42-3ea0-a76d-28131dbd9776 | -6.50268 | -39.69522 | 2024-10-27 04:00:00 | NPP-375D | JUCÁS | CEARÁ | Brasil | 2307403 | 23 | 33 | nan | nan | nan | Caatinga | 1.6 |
| dd765744-7e73-369f-bfd1-535ba54bd9a0 | -6.4999 | -39.69123 | 2024-10-27 04:00:00 | NPP-375D | JUCÁS | CEARÁ | Brasil | 2307403 | 23 | 33 | nan | nan | nan | Caatinga | 1.4 |
| e6c3dddf-d0d0-38af-8739-7ab92f487718 | -6.4046 | -39.69402 | 2024-10-27 04:00:00 | NPP-375D | JUCÁS | CEARÁ | Brasil | 2307403 | 23 | 33 | nan | nan | nan | Caatinga | 1.4 |
| 2966b577-7efe-30cf-a790-53fc1fe8910a | -6.04292 | -39.82161 | 2024-10-27 04:00:00 | NPP-375D | ACOPIARA | CEARÁ | Brasil | 2300309 | 23 | 33 | nan | nan | nan | Caatinga | 37.3 |
| 91cdf71e-f568-349a-aa93-036636353cd8 | -6.04237 | -39.82508 | 2024-10-27 04:00:00 | NPP-375D | ACOPIARA | CEARÁ | Brasil | 2300309 | 23 | 33 | nan | nan | nan | Caatinga | 37.3 |
| 1588fdf1-58ed-3ee8-8d1a-8fbe1f822c9a | -6.0396 | -39.82109 | 2024-10-27 04:00:00 | NPP-375D | ACOPIARA | CEARÁ | Brasil | 2300309 | 23 | 33 | nan | nan | nan | Caatinga | 37.3 |
| 537f2e7c-e84b-3369-b3d6-c69262a5bc6b | -6.03905 | -39.82456 | 2024-10-27 04:00:00 | NPP-375D | ACOPIARA | CEARÁ | Brasil | 2300309 | 23 | 33 | nan | nan | nan | Caatinga | 37.3 |
| 77913b04-5ab2-3383-ae43-23bd731a41e8 | -6.03573 | -39.82404 | 2024-10-27 04:00:00 | NPP-375D | MOMBAÇA | CEARÁ | Brasil | 2308500 | 23 | 33 | nan | nan | nan | Caatinga | 4.4 |
| 29fa14a3-4bcf-3b6f-ae30-22c6368c731d | -5.87162 | -39.21183 | 2024-10-27 04:00:00 | NPP-375D | DEPUTADO IRAPUAN PINHEIRO | CEARÁ | Brasil | 2304269 | 23 | 33 | nan | nan | nan | Caatinga | 5.4 |
| a8f91b67-e205-3ca8-b545-d179a1fd3b86 | -5.12648 | -39.30524 | 2024-10-27 04:00:00 | NPP-375D | QUIXERAMOBIM | CEARÁ | Brasil | 2311405 | 23 | 33 | nan | nan | nan | Caatinga | 2.6 |
| 525009d5-3a3b-355a-8ab0-0ded55475ac5 | -7.79827 | -40.49095 | 2024-10-27 04:00:00 | NPP-375D | ARARIPINA | PERNAMBUCO | Brasil | 2601102 | 26 | 33 | nan | nan | nan | Caatinga | 1.0 |
| 76e53b79-03b9-31c1-afed-fe302a588810 | -7.95137 | -39.33889 | 2024-10-27 04:00:00 | NPP-375D | SERRITA | PERNAMBUCO | Brasil | 2614006 | 26 | 33 | nan | nan | nan | Caatinga | 1.2 |
| 55e2b56b-3592-3e79-a030-67bad276ccec | -7.89909 | -39.67585 | 2024-10-27 04:00:00 | NPP-375D | PARNAMIRIM | PERNAMBUCO | Brasil | 2610400 | 26 | 33 | nan | nan | nan | Caatinga | 1.0 |
| dd932f70-137f-3968-bd42-07dd882de290 | -7.53813 | -39.84402 | 2024-10-27 04:00:00 | NPP-375D | EXU | PERNAMBUCO | Brasil | 2605301 | 26 | 33 | nan | nan | nan | Caatinga | 0.7 |
| 02f3554f-95e6-39f5-8e46-1b8521ce17cf | -7.46717 | -40.14605 | 2024-10-27 04:00:00 | NPP-375D | IPUBI | PERNAMBUCO | Brasil | 2607307 | 26 | 33 | nan | nan | nan | Caatinga | 0.5 |
| abf839b2-fd64-3746-8fc2-7d96f1056df4 | -7.32788 | -39.3712 | 2024-10-27 04:00:00 | NPP-375D | BARBALHA | CEARÁ | Brasil | 2301901 | 23 | 33 | nan | nan | nan | Caatinga | 0.8 |
| b0dcc030-1668-3f97-9bb7-4b1988fb267a | -7.30649 | -39.14484 | 2024-10-27 04:00:00 | NPP-375D | MISSÃO VELHA | CEARÁ | Brasil | 2308401 | 23 | 33 | nan | nan | nan | Caatinga | 1.4 |
| 37365066-3f95-3f68-8a0a-31f060f9f828 | -7.10888 | -39.58398 | 2024-10-27 04:00:00 | NPP-375D | CRATO | CEARÁ | Brasil | 2304202 | 23 | 33 | nan | nan | nan | Caatinga | 1.6 |
| a35e3b01-859e-3438-9e99-febf81516771 | -7.0794 | -39.53297 | 2024-10-27 04:00:00 | NPP-375D | CRATO | CEARÁ | Brasil | 2304202 | 23 | 33 | nan | nan | nan | Caatinga | 1.1 |
| 2489c008-f1ff-3cde-be78-3a3d8115fe72 | -7.07885 | -39.53645 | 2024-10-27 04:00:00 | NPP-375D | CRATO | CEARÁ | Brasil | 2304202 | 23 | 33 | nan | nan | nan | Caatinga | 0.9 |
| ce405b20-c159-3866-bcc0-31aece718391 | -7.06671 | -40.00438 | 2024-10-27 04:00:00 | NPP-375D | POTENGI | CEARÁ | Brasil | 2311207 | 23 | 33 | nan | nan | nan | Caatinga | 1.5 |
| 7a838fa3-2a3b-33fb-9520-5d2f39512b35 | -6.9684 | -39.25106 | 2024-10-27 04:00:00 | NPP-375D | CARIRIAÇU | CEARÁ | Brasil | 2303204 | 23 | 33 | nan | nan | nan | Caatinga | 1.0 |
| 9e7dcf26-9d6e-396d-aa6c-5742b312e129 | -6.96507 | -39.25053 | 2024-10-27 04:00:00 | NPP-375D | CARIRIAÇU | CEARÁ | Brasil | 2303204 | 23 | 33 | nan | nan | nan | Caatinga | 2.3 |
| 99586fc4-d5cb-3334-a1eb-58eb032f860f | -8.61822 | -40.71854 | 2024-10-27 04:00:00 | NPP-375D | DORMENTES | PERNAMBUCO | Brasil | 2605152 | 26 | 33 | nan | nan | nan | Caatinga | 0.7 |
| 72018827-3f93-34b3-99b1-56e4d8327fd6 | -8.54864 | -40.41042 | 2024-10-27 04:00:00 | NPP-375D | DORMENTES | PERNAMBUCO | Brasil | 2605152 | 26 | 33 | nan | nan | nan | Caatinga | 0.8 |
| 8aa8493d-b129-3d69-856f-57291e7c5516 | -8.2681 | -40.34459 | 2024-10-27 04:00:00 | NPP-375D | SANTA CRUZ | PERNAMBUCO | Brasil | 2612455 | 26 | 33 | nan | nan | nan | Caatinga | 0.9 |
| eb6a8647-866f-3ea8-8dff-5022dc31063c | -8.16241 | -40.50214 | 2024-10-27 04:00:00 | NPP-375D | SANTA FILOMENA | PERNAMBUCO | Brasil | 2612554 | 26 | 33 | nan | nan | nan | Caatinga | 1.6 |
| 543f9884-de22-397a-9c9f-ddae7a6a1216 | -9.35692 | -39.91928 | 2024-10-27 04:00:00 | NPP-375D | JUAZEIRO | BAHIA | Brasil | 2918407 | 29 | 33 | nan | nan | nan | Caatinga | 0.9 |
| 04a462fe-bdab-3464-a80f-2fe98da2c081 | -9.3436 | -39.91718 | 2024-10-27 04:00:00 | NPP-375D | JUAZEIRO | BAHIA | Brasil | 2918407 | 29 | 33 | nan | nan | nan | Caatinga | 1.1 |
| b6f25fe0-933d-3227-93f0-a7d93d6bb625 | -8.26397 | -39.72555 | 2024-10-27 04:00:00 | NPP-375D | PARNAMIRIM | PERNAMBUCO | Brasil | 2610400 | 26 | 33 | nan | nan | nan | Caatinga | 0.7 |
| 0744f3d9-21a4-39d6-b605-f1bfc92ba84d | -8.17957 | -39.63708 | 2024-10-27 04:00:00 | NPP-375D | PARNAMIRIM | PERNAMBUCO | Brasil | 2610400 | 26 | 33 | nan | nan | nan | Caatinga | 0.6 |
| a93f9354-94f0-34bd-b3a2-cf0ca9870c95 | -4.51094 | -40.68805 | 2024-10-27 04:00:00 | NPP-375D | IPUEIRAS | CEARÁ | Brasil | 2305902 | 23 | 33 | nan | nan | nan | Caatinga | 0.9 |
| 35e94f37-8b1d-333b-8f64-403c4426ced1 | -4.29463 | -40.59967 | 2024-10-27 04:00:00 | NPP-375D | PIRES FERREIRA | CEARÁ | Brasil | 2310951 | 23 | 33 | nan | nan | nan | Caatinga | 1.9 |
| 99513fe7-725f-397e-b7e6-b93cdf5fd8a5 | -4.18688 | -40.68452 | 2024-10-27 04:00:00 | NPP-375D | RERIUTABA | CEARÁ | Brasil | 2311702 | 23 | 33 | nan | nan | nan | Caatinga | 0.7 |


[Clique aqui para ver as próximas entradas](README31.md)
