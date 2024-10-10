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

## Dados Diários - Página 5

| ID | Latitude | Longitude | Data/Hora GMT | Satélite | Município | Estado | País | Município ID | Estado ID | País ID | Dias sem Chuva | Precipitação | Risco de Fogo | Bioma | FRP |
|----|----------|-----------|---------------|----------|-----------|--------|------|--------------|-----------|---------|----------------|--------------|----------------|-------|-----|
| a8461730-a94a-3d6a-8b11-c2c3de21bb2e | -3.71662 | -44.97843 | 2024-10-10 00:18:00 | TERRA_M-M | CONCEIÇÃO DO LAGO-AÇU | MARANHÃO | Brasil | 2103554 | 21 | 33 | nan | nan | nan | Amazônia | 46.7 |
| 980a15f3-bbf2-3833-87a6-45023f3585a4 | -3.71409 | -44.95986 | 2024-10-10 00:18:00 | TERRA_M-M | CONCEIÇÃO DO LAGO-AÇU | MARANHÃO | Brasil | 2103554 | 21 | 33 | nan | nan | nan | Amazônia | 72.8 |
| 063cefff-ff19-31c6-a031-3ca4a1c9230c | -3.70422 | -45.0758 | 2024-10-10 00:18:00 | TERRA_M-M | IGARAPÉ DO MEIO | MARANHÃO | Brasil | 2105153 | 21 | 33 | nan | nan | nan | Amazônia | 27.2 |
| 5347c504-f568-35b1-a4bb-f968eb09dba5 | -4.90073 | -45.93133 | 2024-10-10 00:18:00 | TERRA_M-M | ARAME | MARANHÃO | Brasil | 2100956 | 21 | 33 | nan | nan | nan | Amazônia | 17.5 |
| cd91f0dc-1ffe-317f-9bf1-247669cb3f9d | -4.88476 | -45.70184 | 2024-10-10 00:18:00 | TERRA_M-M | ARAME | MARANHÃO | Brasil | 2100956 | 21 | 33 | nan | nan | nan | Amazônia | 26.2 |
| 76609f45-6a9b-346f-b816-559096d55376 | -4.87203 | -45.81703 | 2024-10-10 00:18:00 | TERRA_M-M | ARAME | MARANHÃO | Brasil | 2100956 | 21 | 33 | nan | nan | nan | Amazônia | 28.0 |
| ee255283-d38b-3db4-8965-498ff94f8d33 | -4.86908 | -45.79402 | 2024-10-10 00:18:00 | TERRA_M-M | ARAME | MARANHÃO | Brasil | 2100956 | 21 | 33 | nan | nan | nan | Amazônia | 20.7 |
| 1086c4d3-65f5-3118-8db6-c5b0b92c8007 | -4.86174 | -45.80114 | 2024-10-10 00:18:00 | TERRA_M-M | ARAME | MARANHÃO | Brasil | 2100956 | 21 | 33 | nan | nan | nan | Amazônia | 30.6 |
| d30dd716-f343-32c1-8e8c-fe66bfb7e761 | -5.91792 | -45.42719 | 2024-10-10 00:18:00 | TERRA_M-M | GRAJAÚ | MARANHÃO | Brasil | 2104800 | 21 | 33 | nan | nan | nan | Cerrado | 107.5 |
| df4bc6fd-324c-3712-866f-cb6c7a744242 | -5.91514 | -45.40524 | 2024-10-10 00:18:00 | TERRA_M-M | GRAJAÚ | MARANHÃO | Brasil | 2104800 | 21 | 33 | nan | nan | nan | Cerrado | 30.8 |
| 0a0cca93-f9ec-3e40-8c89-6d1eb19cc3af | -5.90954 | -45.43476 | 2024-10-10 00:18:00 | TERRA_M-M | GRAJAÚ | MARANHÃO | Brasil | 2104800 | 21 | 33 | nan | nan | nan | Cerrado | 187.4 |
| 78cc529f-e30a-3d10-8a52-802d26032ee0 | -5.90659 | -45.41264 | 2024-10-10 00:18:00 | TERRA_M-M | GRAJAÚ | MARANHÃO | Brasil | 2104800 | 21 | 33 | nan | nan | nan | Cerrado | 265.7 |
| ada81726-5202-3272-a647-327d0bd23205 | -5.90447 | -45.42906 | 2024-10-10 00:18:00 | TERRA_M-M | GRAJAÚ | MARANHÃO | Brasil | 2104800 | 21 | 33 | nan | nan | nan | Cerrado | 236.9 |
| 727d3d8f-d832-33bc-bb34-b2aacf8e0e07 | -5.90169 | -45.40689 | 2024-10-10 00:18:00 | TERRA_M-M | BARRA DO CORDA | MARANHÃO | Brasil | 2101608 | 21 | 33 | nan | nan | nan | Cerrado | 79.5 |
| bd5d7212-14f4-3ca4-93b7-60fbbf2b592c | -5.85018 | -46.45776 | 2024-10-10 00:18:00 | TERRA_M-M | GRAJAÚ | MARANHÃO | Brasil | 2104800 | 21 | 33 | nan | nan | nan | Cerrado | 30.8 |
| 3e616717-6950-30d0-8d1e-5c9c76929f35 | -5.84913 | -46.46461 | 2024-10-10 00:18:00 | TERRA_M-M | GRAJAÚ | MARANHÃO | Brasil | 2104800 | 21 | 33 | nan | nan | nan | Cerrado | 21.0 |
| 9fa2d364-db7b-3295-9f75-4b3769740d93 | -5.84555 | -46.43737 | 2024-10-10 00:18:00 | TERRA_M-M | GRAJAÚ | MARANHÃO | Brasil | 2104800 | 21 | 33 | nan | nan | nan | Cerrado | 29.8 |
| 6ccdda59-8198-3b0c-94b6-f16b9894b719 | -5.69821 | -46.46257 | 2024-10-10 00:18:00 | TERRA_M-M | AMARANTE DO MARANHÃO | MARANHÃO | Brasil | 2100600 | 21 | 33 | nan | nan | nan | Cerrado | 30.8 |
| 1e3cb029-1d34-39f5-89a3-af915172bcc6 | -5.69484 | -46.43594 | 2024-10-10 00:18:00 | TERRA_M-M | AMARANTE DO MARANHÃO | MARANHÃO | Brasil | 2100600 | 21 | 33 | nan | nan | nan | Cerrado | 33.8 |
| cdb03144-6eb0-3e5a-9e2c-e7dbf5c48927 | -5.69339 | -46.44268 | 2024-10-10 00:18:00 | TERRA_M-M | AMARANTE DO MARANHÃO | MARANHÃO | Brasil | 2100600 | 21 | 33 | nan | nan | nan | Cerrado | 33.7 |
| 47e13e83-512e-3744-86fe-c3a25063b31d | -5.54151 | -46.20693 | 2024-10-10 00:18:00 | TERRA_M-M | GRAJAÚ | MARANHÃO | Brasil | 2104800 | 21 | 33 | nan | nan | nan | Amazônia | 17.6 |
| 47a36c74-091b-328c-8c36-944a021d3c49 | -5.39526 | -46.00754 | 2024-10-10 00:18:00 | TERRA_M-M | GRAJAÚ | MARANHÃO | Brasil | 2104800 | 21 | 33 | nan | nan | nan | Cerrado | 76.4 |
| 8a39d16d-d7f7-35c1-8538-44984cc2d4ef | -5.39213 | -45.98357 | 2024-10-10 00:18:00 | TERRA_M-M | GRAJAÚ | MARANHÃO | Brasil | 2104800 | 21 | 33 | nan | nan | nan | Cerrado | 127.8 |
| 96e4d39d-b871-324b-8e52-64a16d27905f | -5.31272 | -45.48093 | 2024-10-10 00:18:00 | TERRA_M-M | JENIPAPO DOS VIEIRAS | MARANHÃO | Brasil | 2105476 | 21 | 33 | nan | nan | nan | Cerrado | 15.6 |
| 4cef690c-26a3-3f01-b5df-52c2cb2bf4df | -5.10157 | -46.11707 | 2024-10-10 00:18:00 | TERRA_M-M | ARAME | MARANHÃO | Brasil | 2100956 | 21 | 33 | nan | nan | nan | Amazônia | 22.8 |
| 1e54fb4b-7a5d-3447-92fb-68a57723cec0 | -7.39093 | -46.16148 | 2024-10-10 00:18:00 | TERRA_M-M | BALSAS | MARANHÃO | Brasil | 2101400 | 21 | 33 | nan | nan | nan | Cerrado | 53.2 |
| 425932c2-cb27-3f4a-a5e1-278b6b03d39e | -7.38952 | -46.16691 | 2024-10-10 00:18:00 | TERRA_M-M | BALSAS | MARANHÃO | Brasil | 2101400 | 21 | 33 | nan | nan | nan | Cerrado | 33.2 |
| 79d79165-568a-3db6-a948-a22abd1bca32 | -7.38766 | -46.13478 | 2024-10-10 00:18:00 | TERRA_M-M | BALSAS | MARANHÃO | Brasil | 2101400 | 21 | 33 | nan | nan | nan | Cerrado | 42.7 |
| 0f49e66a-e5f6-3b87-b3b4-4a4f8e69375b | -7.38607 | -46.14037 | 2024-10-10 00:18:00 | TERRA_M-M | BALSAS | MARANHÃO | Brasil | 2101400 | 21 | 33 | nan | nan | nan | Cerrado | 66.9 |
| fa38b260-9abd-355e-8b9d-8a8e4850caf2 | -6.98947 | -45.23896 | 2024-10-10 00:18:00 | TERRA_M-M | LORETO | MARANHÃO | Brasil | 2106102 | 21 | 33 | nan | nan | nan | Cerrado | 16.6 |
| a7200c7e-3621-3cbe-92e0-196f3a36a0b6 | -6.95997 | -45.29372 | 2024-10-10 00:18:00 | TERRA_M-M | SAMBAÍBA | MARANHÃO | Brasil | 2109700 | 21 | 33 | nan | nan | nan | Cerrado | 270.6 |
| 80e1636b-62a1-37fc-81ce-40d0dbd16e8b | -6.95714 | -45.27174 | 2024-10-10 00:18:00 | TERRA_M-M | SAMBAÍBA | MARANHÃO | Brasil | 2109700 | 21 | 33 | nan | nan | nan | Cerrado | 199.8 |
| fb92c2db-6b1f-3307-8ed2-d1df750aaab1 | -6.83906 | -46.23655 | 2024-10-10 00:18:00 | TERRA_M-M | FORTALEZA DOS NOGUEIRAS | MARANHÃO | Brasil | 2104107 | 21 | 33 | nan | nan | nan | Cerrado | 22.1 |
| aae66b21-24ed-368f-8cba-8c044d67bf60 | -6.83411 | -46.21581 | 2024-10-10 00:18:00 | TERRA_M-M | FORTALEZA DOS NOGUEIRAS | MARANHÃO | Brasil | 2104107 | 21 | 33 | nan | nan | nan | Cerrado | 22.7 |
| ff8821b4-99ce-35bd-af9b-a58decb2e2e8 | -6.78166 | -45.65638 | 2024-10-10 00:18:00 | TERRA_M-M | SÃO RAIMUNDO DAS MANGABEIRAS | MARANHÃO | Brasil | 2111607 | 21 | 33 | nan | nan | nan | Cerrado | 26.3 |
| 662b4b5c-70a0-3624-8fdf-d99bdf097460 | -6.77876 | -45.63313 | 2024-10-10 00:18:00 | TERRA_M-M | SÃO RAIMUNDO DAS MANGABEIRAS | MARANHÃO | Brasil | 2111607 | 21 | 33 | nan | nan | nan | Cerrado | 41.8 |
| 6e3d0a54-34d8-33c1-81b6-51f5bba59fa9 | -6.77291 | -45.63919 | 2024-10-10 00:18:00 | TERRA_M-M | SÃO RAIMUNDO DAS MANGABEIRAS | MARANHÃO | Brasil | 2111607 | 21 | 33 | nan | nan | nan | Cerrado | 15.9 |
| 85d63de1-8dc7-3362-ba0b-5233a621acd7 | -2.83866 | -46.69354 | 2024-10-10 00:18:00 | TERRA_M-M | PARAGOMINAS | PARÁ | Brasil | 1505502 | 15 | 33 | nan | nan | nan | Amazônia | 21.8 |
| 19f8ce05-a415-3056-83b0-a25f924e1e59 | -4.48587 | -46.59156 | 2024-10-10 00:18:00 | TERRA_M-M | BOM JESUS DAS SELVAS | MARANHÃO | Brasil | 2102036 | 21 | 33 | nan | nan | nan | Amazônia | 39.4 |
| 43e3f85f-cd60-3628-9325-90b01b3e3b37 | -4.48369 | -46.59723 | 2024-10-10 00:18:00 | TERRA_M-M | BOM JESUS DAS SELVAS | MARANHÃO | Brasil | 2102036 | 21 | 33 | nan | nan | nan | Amazônia | 196.1 |
| d8389a3b-1cd0-353a-97bf-6d0335c856da | -4.48085 | -47.74536 | 2024-10-10 00:18:00 | TERRA_M-M | DOM ELISEU | PARÁ | Brasil | 1502939 | 15 | 33 | nan | nan | nan | Amazônia | 32.8 |
| 3d9fce38-6b3f-32e6-ad9e-fea6909fe979 | -4.46927 | -46.59929 | 2024-10-10 00:18:00 | TERRA_M-M | BOM JESUS DAS SELVAS | MARANHÃO | Brasil | 2102036 | 21 | 33 | nan | nan | nan | Amazônia | 170.2 |
| 192e77e1-26db-3d1b-9879-dd6218cb5b17 | -4.32671 | -47.71246 | 2024-10-10 00:18:00 | TERRA_M-M | DOM ELISEU | PARÁ | Brasil | 1502939 | 15 | 33 | nan | nan | nan | Amazônia | 42.0 |
| 43288213-4847-3523-b145-2fb8df414067 | -4.3167 | -47.71869 | 2024-10-10 00:18:00 | TERRA_M-M | DOM ELISEU | PARÁ | Brasil | 1502939 | 15 | 33 | nan | nan | nan | Amazônia | 36.0 |
| 5360bd9c-1eb8-32ee-b305-a4cc4ed5c9cc | -3.93763 | -46.46791 | 2024-10-10 00:18:00 | TERRA_M-M | BOM JARDIM | MARANHÃO | Brasil | 2102002 | 21 | 33 | nan | nan | nan | Amazônia | 17.4 |
| 4d75efc1-1afc-312e-824a-4a1b47f1cbea | -3.93391 | -46.47384 | 2024-10-10 00:18:00 | TERRA_M-M | BOM JARDIM | MARANHÃO | Brasil | 2102002 | 21 | 33 | nan | nan | nan | Amazônia | 16.6 |
| 6ef81857-f292-3897-9e0e-0d060357af89 | -3.93036 | -46.44786 | 2024-10-10 00:18:00 | TERRA_M-M | BOM JARDIM | MARANHÃO | Brasil | 2102002 | 21 | 33 | nan | nan | nan | Amazônia | 48.7 |
| 5234732e-9241-36a3-b1d7-24290c0f4867 | -3.92015 | -46.44388 | 2024-10-10 00:18:00 | TERRA_M-M | BOM JARDIM | MARANHÃO | Brasil | 2102002 | 21 | 33 | nan | nan | nan | Amazônia | 24.4 |
| b8db53b3-1300-322d-a89f-10ad6d3223dc | -3.90208 | -46.45167 | 2024-10-10 00:18:00 | TERRA_M-M | BOM JARDIM | MARANHÃO | Brasil | 2102002 | 21 | 33 | nan | nan | nan | Amazônia | 19.6 |
| 2f6487b2-742c-3a17-a936-e7ea953d1d19 | -5.35283 | -46.61136 | 2024-10-10 00:18:00 | TERRA_M-M | AMARANTE DO MARANHÃO | MARANHÃO | Brasil | 2100600 | 21 | 33 | nan | nan | nan | Cerrado | 69.5 |
| f9632596-b2a1-31eb-8c23-b283ffb45564 | -5.35204 | -46.618 | 2024-10-10 00:18:00 | TERRA_M-M | AMARANTE DO MARANHÃO | MARANHÃO | Brasil | 2100600 | 21 | 33 | nan | nan | nan | Cerrado | 60.9 |
| 216ca10a-9bdb-3041-85f1-e1f776fbd6c2 | -6.97961 | -47.39398 | 2024-10-10 00:18:00 | TERRA_M-M | CAROLINA | MARANHÃO | Brasil | 2102804 | 21 | 33 | nan | nan | nan | Cerrado | 25.2 |
| 220f1b6c-7c37-3862-b4aa-cff7d2e57294 | -6.58109 | -47.7123 | 2024-10-10 00:18:00 | TERRA_M-M | PALMEIRAS DO TOCANTINS | TOCANTINS | Brasil | 1713809 | 17 | 33 | nan | nan | nan | Cerrado | 33.6 |
| 2db21d38-ba5d-33d5-9dca-6335da5fe008 | -4.60409 | -48.06617 | 2024-10-10 00:18:00 | TERRA_M-M | RONDON DO PARÁ | PARÁ | Brasil | 1506187 | 15 | 33 | nan | nan | nan | Amazônia | 40.5 |
| 542ca727-5d8a-3dff-adce-37d1dc40f51a | -4.59517 | -48.06033 | 2024-10-10 00:18:00 | TERRA_M-M | RONDON DO PARÁ | PARÁ | Brasil | 1506187 | 15 | 33 | nan | nan | nan | Amazônia | 29.8 |
| 8e4f4107-5992-3fde-a478-d3ab8ae5bf22 | -4.11414 | -48.29924 | 2024-10-10 00:18:00 | TERRA_M-M | DOM ELISEU | PARÁ | Brasil | 1502939 | 15 | 33 | nan | nan | nan | Amazônia | 32.8 |
| 850d39b7-3a17-3dd9-aae7-7c6aef65e5b8 | -4.10961 | -48.26418 | 2024-10-10 00:18:00 | TERRA_M-M | DOM ELISEU | PARÁ | Brasil | 1502939 | 15 | 33 | nan | nan | nan | Amazônia | 188.1 |
| dc6aad3c-8b4f-38c2-874a-790771bb62c9 | -4.10507 | -49.07102 | 2024-10-10 00:18:00 | TERRA_M-M | GOIANÉSIA DO PARÁ | PARÁ | Brasil | 1503093 | 15 | 33 | nan | nan | nan | Amazônia | 72.5 |
| 68f0b99e-8d78-3dce-ab93-c9ac4e950459 | -4.1033 | -49.0761 | 2024-10-10 00:18:00 | TERRA_M-M | GOIANÉSIA DO PARÁ | PARÁ | Brasil | 1503093 | 15 | 33 | nan | nan | nan | Amazônia | 69.1 |
| 02f2ee01-ec51-3b05-87cf-dbbe4681c18a | -4.10274 | -48.27204 | 2024-10-10 00:18:00 | TERRA_M-M | DOM ELISEU | PARÁ | Brasil | 1502939 | 15 | 33 | nan | nan | nan | Amazônia | 202.5 |
| a299aa20-900d-3c3d-9e2e-4a4fa904d1e8 | -4.09324 | -48.26623 | 2024-10-10 00:18:00 | TERRA_M-M | DOM ELISEU | PARÁ | Brasil | 1502939 | 15 | 33 | nan | nan | nan | Amazônia | 40.5 |
| d74b556f-5a69-349c-a89e-1968ebe8a994 | -2.94632 | -49.21939 | 2024-10-10 00:18:00 | TERRA_M-M | MOJU | PARÁ | Brasil | 1504703 | 15 | 33 | nan | nan | nan | Amazônia | 38.9 |
| 3a459a1c-f47a-36a7-b1fb-da96ffbde66c | -2.94421 | -49.22638 | 2024-10-10 00:18:00 | TERRA_M-M | MOJU | PARÁ | Brasil | 1504703 | 15 | 33 | nan | nan | nan | Amazônia | 29.2 |
| f33e087c-1c82-395d-92c8-d833ea9ce109 | -8.62768 | -40.38553 | 2024-10-10 00:18:00 | TERRA_M-M | LAGOA GRANDE | PERNAMBUCO | Brasil | 2608750 | 26 | 33 | nan | nan | nan | Caatinga | 14.2 |
| 919a3449-5437-3633-ad58-cb1efe7242f0 | -7.66743 | -39.62356 | 2024-10-10 00:18:00 | TERRA_M-M | EXU | PERNAMBUCO | Brasil | 2605301 | 26 | 33 | nan | nan | nan | Caatinga | 11.2 |
| 45ef8ba3-8060-38e3-a7b1-c1d11059f877 | -7.73996 | -40.30016 | 2024-10-10 00:18:00 | TERRA_M-M | TRINDADE | PERNAMBUCO | Brasil | 2615607 | 26 | 33 | nan | nan | nan | Caatinga | 8.8 |
| f8afe49a-b614-3fcf-9278-61dc8523480f | -5.58972 | -39.44714 | 2024-10-10 00:18:00 | TERRA_M-M | SENADOR POMPEU | CEARÁ | Brasil | 2312700 | 23 | 33 | nan | nan | nan | Caatinga | 8.1 |
| c9175a9d-8088-3a5a-8739-8703d64add70 | -5.59865 | -39.44585 | 2024-10-10 00:18:00 | TERRA_M-M | SENADOR POMPEU | CEARÁ | Brasil | 2312700 | 23 | 33 | nan | nan | nan | Caatinga | 9.8 |
| ace4de07-0405-34c3-98d5-5cfe83d8f801 | -5.81519 | -39.07699 | 2024-10-10 00:18:00 | TERRA_M-M | SOLONÓPOLE | CEARÁ | Brasil | 2313005 | 23 | 33 | nan | nan | nan | Caatinga | 9.9 |
| b42b051d-edbd-314d-91f2-906a207e20f4 | -5.91675 | -39.21164 | 2024-10-10 00:18:00 | TERRA_M-M | DEPUTADO IRAPUAN PINHEIRO | CEARÁ | Brasil | 2304269 | 23 | 33 | nan | nan | nan | Caatinga | 8.4 |
| 1bcfbee7-83ad-3e2d-b7a7-84611b8569ea | -5.91799 | -39.22062 | 2024-10-10 00:18:00 | TERRA_M-M | DEPUTADO IRAPUAN PINHEIRO | CEARÁ | Brasil | 2304269 | 23 | 33 | nan | nan | nan | Caatinga | 13.9 |
| 8b28e3e5-6eba-321f-a45c-17c66b0cd476 | -4.55192 | -38.88086 | 2024-10-10 00:18:00 | TERRA_M-M | ITAPIÚNA | CEARÁ | Brasil | 2306504 | 23 | 33 | nan | nan | nan | Caatinga | 7.7 |
| e9841d4e-1bc0-38ed-ab8e-2b3ca5d7ed37 | -6.44372 | -38.82759 | 2024-10-10 00:18:00 | TERRA_M-M | ICÓ | CEARÁ | Brasil | 2305407 | 23 | 33 | nan | nan | nan | Caatinga | 4.5 |
| 56f67596-8259-3a4a-9ad4-312955d07c87 | -6.44618 | -38.84536 | 2024-10-10 00:18:00 | TERRA_M-M | ICÓ | CEARÁ | Brasil | 2305407 | 23 | 33 | nan | nan | nan | Caatinga | 15.6 |
| 09ac945d-8d2d-3b62-a238-8dc75a839998 | -6.45504 | -38.84412 | 2024-10-10 00:18:00 | TERRA_M-M | ICÓ | CEARÁ | Brasil | 2305407 | 23 | 33 | nan | nan | nan | Caatinga | 17.0 |
| 4399967e-51c3-3649-a8bf-598d1a299f8a | -6.70682 | -34.99692 | 2024-10-10 00:18:00 | TERRA_M-M | MARCAÇÃO | PARAÍBA | Brasil | 2509057 | 25 | 33 | nan | nan | nan | Mata Atlântica | 11.1 |
| 37c7340b-7cf9-35b4-a454-272906fb43d3 | -6.80949 | -34.99906 | 2024-10-10 00:18:00 | TERRA_M-M | RIO TINTO | PARAÍBA | Brasil | 2512903 | 25 | 33 | nan | nan | nan | Mata Atlântica | 8.0 |
| ca51f928-75e3-320b-81b2-74502fb82421 | -7.177 | -35.05947 | 2024-10-10 00:18:00 | TERRA_M-M | CRUZ DO ESPÍRITO SANTO | PARAÍBA | Brasil | 2504900 | 25 | 33 | nan | nan | nan | Mata Atlântica | 12.7 |
| de564223-7b6f-30c0-957c-1d1eaed09a97 | -7.17868 | -35.07076 | 2024-10-10 00:18:00 | TERRA_M-M | CRUZ DO ESPÍRITO SANTO | PARAÍBA | Brasil | 2504900 | 25 | 33 | nan | nan | nan | Mata Atlântica | 13.7 |
| b0a662db-41f2-3964-aae9-9b98ad37091f | -6.45628 | -38.85302 | 2024-10-10 00:18:00 | TERRA_M-M | ICÓ | CEARÁ | Brasil | 2305407 | 23 | 33 | nan | nan | nan | Caatinga | 13.0 |
| 3526cde3-0b31-3a45-9613-85dc1a0cc2da | -6.43609 | -38.83771 | 2024-10-10 00:18:00 | TERRA_M-M | ICÓ | CEARÁ | Brasil | 2305407 | 23 | 33 | nan | nan | nan | Caatinga | 7.5 |
| eccd2f38-2ea3-33ff-bc57-761b32756b6a | -8.57592 | -40.43538 | 2024-10-10 00:18:00 | TERRA_M-M | DORMENTES | PERNAMBUCO | Brasil | 2605152 | 26 | 33 | nan | nan | nan | Caatinga | 31.4 |
| 0254b92e-ec88-3a59-805d-10ac3564ea90 | -8.57454 | -40.42495 | 2024-10-10 00:18:00 | TERRA_M-M | DORMENTES | PERNAMBUCO | Brasil | 2605152 | 26 | 33 | nan | nan | nan | Caatinga | 36.1 |
| a66649ff-000f-3449-93e5-fc2aae444b5e | -4.04399 | -40.40189 | 2024-10-10 00:18:00 | TERRA_M-M | CARIRÉ | CEARÁ | Brasil | 2303105 | 23 | 33 | nan | nan | nan | Caatinga | 5.1 |
| 0cde2de8-866b-3341-8226-e19afbf203de | -3.96291 | -41.48309 | 2024-10-10 00:18:00 | TERRA_M-M | PIRACURUCA | PIAUÍ | Brasil | 2208304 | 22 | 33 | nan | nan | nan | Caatinga | 13.3 |
| 3877ea0e-c2b4-32b1-bb0c-433070439a5e | -3.89263 | -41.04085 | 2024-10-10 00:18:00 | TERRA_M-M | UBAJARA | CEARÁ | Brasil | 2313609 | 23 | 33 | nan | nan | nan | Caatinga | 18.8 |
| 253b8180-01ab-3159-abee-92c51d013d29 | -5.39402 | -41.25245 | 2024-10-10 00:18:00 | TERRA_M-M | CASTELO DO PIAUÍ | PIAUÍ | Brasil | 2202604 | 22 | 33 | nan | nan | nan | Caatinga | 7.9 |
| b6bbc9c7-3ef6-30cb-9a09-799891ef227d | -5.22591 | -40.48538 | 2024-10-10 00:18:00 | TERRA_M-M | CRATEÚS | CEARÁ | Brasil | 2304103 | 23 | 33 | nan | nan | nan | Caatinga | 8.1 |
| a0542488-6e34-3df9-957d-a49db04e62ba | -5.1971 | -41.30274 | 2024-10-10 00:18:00 | TERRA_M-M | BURITI DOS MONTES | PIAUÍ | Brasil | 2202026 | 22 | 33 | nan | nan | nan | Caatinga | 29.9 |
| 74477295-ca5c-3ce0-a09f-d4eb8c7ce9e6 | -5.19565 | -41.29198 | 2024-10-10 00:18:00 | TERRA_M-M | BURITI DOS MONTES | PIAUÍ | Brasil | 2202026 | 22 | 33 | nan | nan | nan | Caatinga | 29.3 |
| 0299ad07-a4f5-38d3-923e-b23eddab528e | -5.18887 | -41.31486 | 2024-10-10 00:18:00 | TERRA_M-M | BURITI DOS MONTES | PIAUÍ | Brasil | 2202026 | 22 | 33 | nan | nan | nan | Caatinga | 12.6 |
| a067e393-b15b-35a3-8fbd-a122de46f524 | -5.18744 | -41.30414 | 2024-10-10 00:18:00 | TERRA_M-M | BURITI DOS MONTES | PIAUÍ | Brasil | 2202026 | 22 | 33 | nan | nan | nan | Caatinga | 66.5 |
| 45bb5b50-a8c2-3470-890c-ef89c9a915e5 | -5.18601 | -41.29341 | 2024-10-10 00:18:00 | TERRA_M-M | BURITI DOS MONTES | PIAUÍ | Brasil | 2202026 | 22 | 33 | nan | nan | nan | Caatinga | 11.2 |
| da3d0459-9d9d-3736-831f-0579b040b70a | -7.99365 | -40.9762 | 2024-10-10 00:18:00 | TERRA_M-M | PAULISTANA | PIAUÍ | Brasil | 2207801 | 22 | 33 | nan | nan | nan | Caatinga | 11.8 |
| b2c892e7-e96f-395b-9d3c-14fe1913858a | -7.60326 | -41.72966 | 2024-10-10 00:18:00 | TERRA_M-M | CAMPINAS DO PIAUÍ | PIAUÍ | Brasil | 2202109 | 22 | 33 | nan | nan | nan | Caatinga | 8.7 |
| a65d1826-ec2b-300f-86fc-416cfe16d331 | -15.333 | -43.0569 | 2024-10-10 00:18:01 | METOP-C | CATUTI | MINAS GERAIS | Brasil | 3115474 | 31 | 33 | nan | nan | nan | Caatinga | nan |
| 96ccac4a-08f6-3554-be03-34584686bf34 | -15.3349 | -43.0658 | 2024-10-10 00:18:01 | METOP-C | CATUTI | MINAS GERAIS | Brasil | 3115474 | 31 | 33 | nan | nan | nan | Caatinga | nan |
| 10fd56c9-f4c1-3a49-8e47-679fc3515bbe | -14.8413 | -41.512501 | 2024-10-10 00:18:03 | METOP-C | TREMEDAL | BAHIA | Brasil | 2931806 | 29 | 33 | nan | nan | nan | Caatinga | nan |
| 5c491e1a-3270-3f7e-9c60-b92deb0ee9cd | -14.843 | -41.5201 | 2024-10-10 00:18:03 | METOP-C | TREMEDAL | BAHIA | Brasil | 2931806 | 29 | 33 | nan | nan | nan | Caatinga | nan |
| a37c07a4-190d-3417-b198-db2c29ababb1 | -14.4925 | -41.750801 | 2024-10-10 00:18:10 | METOP-C | PRESIDENTE JÂNIO QUADROS | BAHIA | Brasil | 2925709 | 29 | 33 | nan | nan | nan | Caatinga | nan |


[Clique aqui para ver as próximas entradas](README6.md)
