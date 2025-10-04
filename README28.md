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

## Dados Diários - Página 28

| ID | Latitude | Longitude | Data/Hora GMT | Satélite | Município | Estado | País | Município ID | Estado ID | País ID | Dias sem Chuva | Precipitação | Risco de Fogo | Bioma | FRP |
|----|----------|-----------|---------------|----------|-----------|--------|------|--------------|-----------|---------|----------------|--------------|----------------|-------|-----|
| afcb7490-4922-33a7-b58d-75ff4ee9a335 | -10.04841 | -49.20715 | 2025-10-04 03:51:00 | NPP-375D | MONTE SANTO DO TOCANTINS | TOCANTINS | Brasil | 1713700 | 17 | 33 | nan | nan | nan | Cerrado | 1.2 |
| 9f4ff85c-29d0-3bfc-baf9-1074c71b19c1 | -4.31044 | -48.08648 | 2025-10-04 03:51:00 | NPP-375D | RONDON DO PARÁ | PARÁ | Brasil | 1506187 | 15 | 33 | nan | nan | nan | Amazônia | 1.2 |
| 8ef01329-4aa4-3a7a-9a0e-4b5b37d584f4 | -5.07828 | -44.09107 | 2025-10-04 03:51:00 | NPP-375D | GONÇALVES DIAS | MARANHÃO | Brasil | 2104404 | 21 | 33 | nan | nan | nan | Cerrado | 2.9 |
| 8f870bbb-d459-35f1-815a-21927439fdde | -8.46584 | -47.41994 | 2025-10-04 03:51:00 | NPP-375D | GOIATINS | TOCANTINS | Brasil | 1709005 | 17 | 33 | nan | nan | nan | Cerrado | 3.4 |
| 409d8092-f9f2-356c-a218-1508a00c8983 | -7.27055 | -45.48475 | 2025-10-04 03:51:00 | NPP-375D | SAMBAÍBA | MARANHÃO | Brasil | 2109700 | 21 | 33 | nan | nan | nan | Cerrado | 0.7 |
| bdc735c4-89a2-381a-8b17-c86d20f7e9e4 | -6.2068 | -44.33324 | 2025-10-04 03:51:00 | NPP-375D | MIRADOR | MARANHÃO | Brasil | 2106706 | 21 | 33 | nan | nan | nan | Cerrado | 4.1 |
| 04e99f0c-9662-302b-865b-553de96c72b9 | -5.89882 | -38.48001 | 2025-10-04 03:51:00 | NPP-375D | PEREIRO | CEARÁ | Brasil | 2310803 | 23 | 33 | nan | nan | nan | Caatinga | 1.4 |
| ef1c8cdb-6763-36be-a3c5-a27405d80a8e | -8.20007 | -46.99226 | 2025-10-04 03:51:00 | NPP-375D | CAMPOS LINDOS | TOCANTINS | Brasil | 1703842 | 17 | 33 | nan | nan | nan | Cerrado | 5.8 |
| cbbf4a91-e207-3900-8b15-1a90543e2d9d | -7.74435 | -42.55235 | 2025-10-04 03:51:00 | NPP-375D | SÃO JOSÉ DO PEIXE | PIAUÍ | Brasil | 2210102 | 22 | 33 | nan | nan | nan | Caatinga | 1.8 |
| 56f1d35f-d9b1-393e-9d87-a22581d873dd | -6.33987 | -43.45982 | 2025-10-04 03:51:00 | NPP-375D | SUCUPIRA DO RIACHÃO | MARANHÃO | Brasil | 2111953 | 21 | 33 | nan | nan | nan | Cerrado | 4.5 |
| 2bd0313e-1649-3ea8-8ea6-472bfd9dde2d | -10.34539 | -48.17193 | 2025-10-04 03:51:00 | NPP-375D | PALMAS | TOCANTINS | Brasil | 1721000 | 17 | 33 | nan | nan | nan | Cerrado | 1.2 |
| 2c876803-8e3e-320c-9291-4e0dfee5cf00 | -9.91119 | -43.74202 | 2025-10-04 03:51:00 | NPP-375D | MORRO CABEÇA NO TEMPO | PIAUÍ | Brasil | 2206654 | 22 | 33 | nan | nan | nan | Caatinga | 2.0 |
| 8fec16b6-fe70-3ee7-b6aa-6605b4db416e | -11.46194 | -45.15149 | 2025-10-04 03:51:00 | NPP-375D | RIACHÃO DAS NEVES | BAHIA | Brasil | 2926202 | 29 | 33 | nan | nan | nan | Cerrado | 2.0 |
| 4829893c-819d-30f7-b115-56d2be213e59 | -7.79955 | -42.55413 | 2025-10-04 03:51:00 | NPP-375D | SOCORRO DO PIAUÍ | PIAUÍ | Brasil | 2210904 | 22 | 33 | nan | nan | nan | Caatinga | 2.3 |
| e9a4d9ff-745c-387b-9bd5-e91a144acfb3 | -5.93264 | -42.88548 | 2025-10-04 03:51:00 | NPP-375D | PALMEIRAIS | PIAUÍ | Brasil | 2207504 | 22 | 33 | nan | nan | nan | Caatinga | 3.7 |
| c119e841-1e27-3fc5-b4c2-22c96fc6f650 | -5.19839 | -45.06756 | 2025-10-04 03:51:00 | NPP-375D | BARRA DO CORDA | MARANHÃO | Brasil | 2101608 | 21 | 33 | nan | nan | nan | Cerrado | 44.1 |
| 6ce60a70-f36a-3fd3-ba86-263c6d012f8d | -4.69609 | -48.16939 | 2025-10-04 03:51:00 | NPP-375D | RONDON DO PARÁ | PARÁ | Brasil | 1506187 | 15 | 33 | nan | nan | nan | Amazônia | 2.4 |
| e46be3ed-e473-3c9e-9a10-e390a9fe6291 | -7.71553 | -42.57072 | 2025-10-04 03:51:00 | NPP-375D | SOCORRO DO PIAUÍ | PIAUÍ | Brasil | 2210904 | 22 | 33 | nan | nan | nan | Caatinga | 1.0 |
| 79b6b6d7-fcda-35e8-a3a1-9aeb91ee4913 | -5.6942 | -49.31306 | 2025-10-04 03:51:00 | NPP-375D | MARABÁ | PARÁ | Brasil | 1504208 | 15 | 33 | nan | nan | nan | Amazônia | 2.1 |
| afd2525a-9418-3aab-85d0-be811df8584d | -5.98383 | -43.48967 | 2025-10-04 03:51:00 | NPP-375D | LAGOA DO MATO | MARANHÃO | Brasil | 2105922 | 21 | 33 | nan | nan | nan | Cerrado | 9.6 |
| cb0d020c-d526-3093-bca8-8da0ee40cdfb | -6.1239 | -45.93279 | 2025-10-04 03:51:00 | NPP-375D | GRAJAÚ | MARANHÃO | Brasil | 2104800 | 21 | 33 | nan | nan | nan | Cerrado | 2.9 |
| e6129378-a5ec-38e1-b46e-e75ad0d61c9c | -5.6924 | -42.84331 | 2025-10-04 03:51:00 | NPP-375D | SÃO PEDRO DO PIAUÍ | PIAUÍ | Brasil | 2210508 | 22 | 33 | nan | nan | nan | Caatinga | 2.3 |
| 07a7da64-b183-3719-a1d8-5d64c6b5044c | -11.12002 | -47.89932 | 2025-10-04 03:51:00 | NPP-375D | SILVANÓPOLIS | TOCANTINS | Brasil | 1720655 | 17 | 33 | nan | nan | nan | Cerrado | 4.3 |
| 2541f0d2-1c09-3f7e-86bf-8586c62612ac | -6.64736 | -42.80578 | 2025-10-04 03:51:00 | NPP-375D | FRANCISCO AYRES | PIAUÍ | Brasil | 2204105 | 22 | 33 | nan | nan | nan | Caatinga | 4.7 |
| a10d16fe-8728-3d44-9612-1da33baa402b | -5.84792 | -43.37886 | 2025-10-04 03:51:00 | NPP-375D | PARNARAMA | MARANHÃO | Brasil | 2107803 | 21 | 33 | nan | nan | nan | Cerrado | 1.9 |
| 01706216-c58d-37c9-9886-fc59cb51b760 | -7.01226 | -42.30997 | 2025-10-04 03:51:00 | NPP-375D | OEIRAS | PIAUÍ | Brasil | 2207009 | 22 | 33 | nan | nan | nan | Caatinga | 1.3 |
| 8fe8f2f0-856c-37ff-8f61-48530a22eb9d | -7.77193 | -46.2675 | 2025-10-04 03:51:00 | NPP-375D | BALSAS | MARANHÃO | Brasil | 2101400 | 21 | 33 | nan | nan | nan | Cerrado | 2.6 |
| a0546bd7-03c0-3928-b095-bab87561dce7 | -7.77186 | -46.23714 | 2025-10-04 03:51:00 | NPP-375D | BALSAS | MARANHÃO | Brasil | 2101400 | 21 | 33 | nan | nan | nan | Cerrado | 1.4 |
| 4aeb6547-a51d-3bf4-adaf-30bfc775c7a0 | -9.94329 | -50.2393 | 2025-10-04 03:51:00 | NPP-375D | PIUM | TOCANTINS | Brasil | 1717503 | 17 | 33 | nan | nan | nan | Cerrado | 1.7 |
| 603d713d-59a5-36b6-8ef7-1443be11b086 | -4.65853 | -45.79514 | 2025-10-04 03:51:00 | NPP-375D | MARAJÁ DO SENA | MARANHÃO | Brasil | 2106359 | 21 | 33 | nan | nan | nan | Amazônia | 1.2 |
| 9aac3822-cd7a-30c1-ba4d-43ef1d5be28e | -7.017 | -44.76894 | 2025-10-04 03:51:00 | NPP-375D | SÃO FÉLIX DE BALSAS | MARANHÃO | Brasil | 2110807 | 21 | 33 | nan | nan | nan | Cerrado | 6.3 |
| 214991e8-1ff4-36cc-8912-8b55a57c9bbb | -6.44626 | -44.8056 | 2025-10-04 03:51:00 | NPP-375D | MIRADOR | MARANHÃO | Brasil | 2106706 | 21 | 33 | nan | nan | nan | Cerrado | 4.5 |
| 227f0398-f39f-3fd2-af5c-abe46108dbe2 | -5.6887 | -42.84026 | 2025-10-04 03:51:00 | NPP-375D | SÃO PEDRO DO PIAUÍ | PIAUÍ | Brasil | 2210508 | 22 | 33 | nan | nan | nan | Caatinga | 3.6 |
| 271bd87c-7e42-3789-b7a9-927778db130a | -5.71377 | -42.63514 | 2025-10-04 03:51:00 | NPP-375D | MIGUEL LEÃO | PIAUÍ | Brasil | 2206308 | 22 | 33 | nan | nan | nan | Caatinga | 1.9 |
| b9500020-667c-3530-817f-0271fa408bff | -5.24088 | -45.54846 | 2025-10-04 03:51:00 | NPP-375D | JENIPAPO DOS VIEIRAS | MARANHÃO | Brasil | 2105476 | 21 | 33 | nan | nan | nan | Cerrado | 4.0 |
| a597130c-89dc-326d-8188-f8f054c28ec6 | -6.30923 | -44.27864 | 2025-10-04 03:51:00 | NPP-375D | MIRADOR | MARANHÃO | Brasil | 2106706 | 21 | 33 | nan | nan | nan | Cerrado | 5.2 |
| e0917e9d-1657-3f4e-a8c6-305ecf1a7f45 | -11.62552 | -45.0308 | 2025-10-04 03:51:00 | NPP-375D | RIACHÃO DAS NEVES | BAHIA | Brasil | 2926202 | 29 | 33 | nan | nan | nan | Cerrado | 1.4 |
| c90059c1-3e4e-34fd-93fc-3fa424bb44df | -6.16212 | -44.61533 | 2025-10-04 03:51:00 | NPP-375D | MIRADOR | MARANHÃO | Brasil | 2106706 | 21 | 33 | nan | nan | nan | Cerrado | 4.6 |
| b805e20a-5947-348a-8280-00b3b307c75f | -7.35052 | -44.34913 | 2025-10-04 03:51:00 | NPP-375D | SEBASTIÃO LEAL | PIAUÍ | Brasil | 2210631 | 22 | 33 | nan | nan | nan | Cerrado | 2.8 |
| fe2f1fc8-16e1-3695-be0e-6aacc3a9ddfa | -4.44518 | -43.24636 | 2025-10-04 03:51:00 | NPP-375D | ALDEIAS ALTAS | MARANHÃO | Brasil | 2100303 | 21 | 33 | nan | nan | nan | Cerrado | 5.0 |
| 2b6358a6-308b-37da-b28c-aea72034ca2c | -5.98463 | -43.48492 | 2025-10-04 03:51:00 | NPP-375D | LAGOA DO MATO | MARANHÃO | Brasil | 2105922 | 21 | 33 | nan | nan | nan | Cerrado | 12.5 |
| 182053e8-b395-32eb-b31f-f198bcb208dd | -6.3452 | -43.46311 | 2025-10-04 03:51:00 | NPP-375D | SUCUPIRA DO RIACHÃO | MARANHÃO | Brasil | 2111953 | 21 | 33 | nan | nan | nan | Cerrado | 4.6 |
| 4240be81-2063-3f70-9b10-8ce24592f28e | -10.32594 | -50.34809 | 2025-10-04 03:51:00 | NPP-375D | PIUM | TOCANTINS | Brasil | 1717503 | 17 | 33 | nan | nan | nan | Cerrado | 17.6 |
| d48b18a5-b907-358b-b880-805af7230064 | -7.04815 | -44.34281 | 2025-10-04 03:51:00 | NPP-375D | BENEDITO LEITE | MARANHÃO | Brasil | 2101806 | 21 | 33 | nan | nan | nan | Cerrado | 2.3 |
| 1518cb94-f6a9-3ff6-aa52-fe31c88d1209 | -11.42402 | -43.48706 | 2025-10-04 03:51:00 | NPP-375D | BARRA | BAHIA | Brasil | 2902708 | 29 | 33 | nan | nan | nan | Cerrado | 0.9 |
| 41a129b3-b001-3b81-abd4-f27f00460af0 | -5.8364 | -42.87049 | 2025-10-04 03:51:00 | NPP-375D | PALMEIRAIS | PIAUÍ | Brasil | 2207504 | 22 | 33 | nan | nan | nan | Caatinga | 1.9 |
| f06cb789-1b35-3ff5-82bd-93e2648d4510 | -5.83546 | -44.98972 | 2025-10-04 03:51:00 | NPP-375D | FERNANDO FALCÃO | MARANHÃO | Brasil | 2104081 | 21 | 33 | nan | nan | nan | Cerrado | 1.3 |
| 55f78152-be1a-3528-85e1-9622340f8296 | -11.11662 | -47.88681 | 2025-10-04 03:51:00 | NPP-375D | SILVANÓPOLIS | TOCANTINS | Brasil | 1720655 | 17 | 33 | nan | nan | nan | Cerrado | 1.8 |
| 773daad9-a811-3cdf-9ba5-15b99d13ad1b | -6.44134 | -44.80464 | 2025-10-04 03:51:00 | NPP-375D | MIRADOR | MARANHÃO | Brasil | 2106706 | 21 | 33 | nan | nan | nan | Cerrado | 4.9 |
| 725ec679-a544-36fb-a0b8-77ac98045f13 | -10.99879 | -46.68853 | 2025-10-04 03:51:00 | NPP-375D | MATEIROS | TOCANTINS | Brasil | 1712702 | 17 | 33 | nan | nan | nan | Cerrado | 1.6 |
| 069b69ec-4b02-394e-a4a7-402ebe8e7004 | -7.74252 | -46.30869 | 2025-10-04 03:51:00 | NPP-375D | BALSAS | MARANHÃO | Brasil | 2101400 | 21 | 33 | nan | nan | nan | Cerrado | 13.0 |
| fe672805-24c5-37a1-beca-75686602d2d9 | -9.07954 | -48.02692 | 2025-10-04 03:51:00 | NPP-375D | BOM JESUS DO TOCANTINS | TOCANTINS | Brasil | 1703305 | 17 | 33 | nan | nan | nan | Cerrado | 2.0 |
| c13b7eb9-b53f-3505-aaec-8be0f0731b75 | -11.47958 | -45.03095 | 2025-10-04 03:51:00 | NPP-375D | RIACHÃO DAS NEVES | BAHIA | Brasil | 2926202 | 29 | 33 | nan | nan | nan | Cerrado | 3.2 |
| 0766b1cf-42f0-382f-bc03-c0449aca805d | -5.8065 | -42.72497 | 2025-10-04 03:51:00 | NPP-375D | SÃO PEDRO DO PIAUÍ | PIAUÍ | Brasil | 2210508 | 22 | 33 | nan | nan | nan | Caatinga | 1.4 |
| 3d1f0710-d709-38d7-a113-1eb841036f41 | -9.08331 | -48.02925 | 2025-10-04 03:51:00 | NPP-375D | BOM JESUS DO TOCANTINS | TOCANTINS | Brasil | 1703305 | 17 | 33 | nan | nan | nan | Cerrado | 5.0 |
| b35fa738-84cb-30b4-98bc-faa1d06fb7f1 | -9.76507 | -48.5841 | 2025-10-04 03:51:00 | NPP-375D | MIRACEMA DO TOCANTINS | TOCANTINS | Brasil | 1713205 | 17 | 33 | nan | nan | nan | Cerrado | 1.1 |
| 946cdf14-7c40-3b83-a64c-ccebfaeb5f3f | -7.56217 | -42.63131 | 2025-10-04 03:51:00 | NPP-375D | SÃO JOSÉ DO PEIXE | PIAUÍ | Brasil | 2210102 | 22 | 33 | nan | nan | nan | Caatinga | 2.5 |
| c15ee746-3983-337e-a170-99eee8d93930 | -8.84918 | -46.81968 | 2025-10-04 03:51:00 | NPP-375D | BALSAS | MARANHÃO | Brasil | 2101400 | 21 | 33 | nan | nan | nan | Cerrado | 1.0 |
| f8efc626-0e10-3ad4-a3c0-73ac7996962c | -8.91455 | -46.61253 | 2025-10-04 03:51:00 | NPP-375D | BALSAS | MARANHÃO | Brasil | 2101400 | 21 | 33 | nan | nan | nan | Cerrado | 1.9 |
| d261c723-f0d5-38c0-9019-de45a235d50c | -5.60969 | -43.23304 | 2025-10-04 03:51:00 | NPP-375D | PARNARAMA | MARANHÃO | Brasil | 2107803 | 21 | 33 | nan | nan | nan | Cerrado | 2.4 |
| e1ed20ef-d0f1-39c1-a47e-cff59b4a6b27 | -4.61141 | -46.46116 | 2025-10-04 03:51:00 | NPP-375D | BURITICUPU | MARANHÃO | Brasil | 2102325 | 21 | 33 | nan | nan | nan | Amazônia | 3.7 |
| 7e4b2d4a-5271-3984-994c-13dc3b7118fe | -6.34986 | -43.43651 | 2025-10-04 03:51:00 | NPP-375D | SUCUPIRA DO RIACHÃO | MARANHÃO | Brasil | 2111953 | 21 | 33 | nan | nan | nan | Cerrado | 1.1 |
| d68250ed-866d-37d3-be71-4f62fa28921d | -11.45825 | -45.14556 | 2025-10-04 03:51:00 | NPP-375D | RIACHÃO DAS NEVES | BAHIA | Brasil | 2926202 | 29 | 33 | nan | nan | nan | Cerrado | 1.4 |
| 50c9ff18-4849-3536-97ef-6bfcf8a17164 | -7.31107 | -42.89259 | 2025-10-04 03:51:00 | NPP-375D | FLORIANO | PIAUÍ | Brasil | 2203909 | 22 | 33 | nan | nan | nan | Caatinga | 0.8 |
| bd4ae39e-3c9c-363c-b6c0-fddfddd5604d | -7.00814 | -42.30922 | 2025-10-04 03:51:00 | NPP-375D | OEIRAS | PIAUÍ | Brasil | 2207009 | 22 | 33 | nan | nan | nan | Caatinga | 1.3 |
| 1750b935-e13b-3d25-b4dc-e035554d65d0 | -8.19803 | -47.00314 | 2025-10-04 03:51:00 | NPP-375D | CAMPOS LINDOS | TOCANTINS | Brasil | 1703842 | 17 | 33 | nan | nan | nan | Cerrado | 2.2 |
| 2259bbc2-e2e4-3de6-909c-98c25787433a | -9.90362 | -43.81018 | 2025-10-04 03:51:00 | NPP-375D | MORRO CABEÇA NO TEMPO | PIAUÍ | Brasil | 2206654 | 22 | 33 | nan | nan | nan | Cerrado | 0.9 |
| 8ab24aa9-78af-3f2b-bf68-3e5b3d82c570 | -10.27748 | -44.34876 | 2025-10-04 03:51:00 | NPP-375D | PARNAGUÁ | PIAUÍ | Brasil | 2207603 | 22 | 33 | nan | nan | nan | Cerrado | 1.6 |
| 2ce4910f-1b06-32ab-9914-a45770770367 | -8.22349 | -46.80798 | 2025-10-04 03:51:00 | NPP-375D | CAMPOS LINDOS | TOCANTINS | Brasil | 1703842 | 17 | 33 | nan | nan | nan | Cerrado | 2.0 |
| def7c395-16ad-3645-b036-5d056c2cc5a8 | -5.88739 | -42.96475 | 2025-10-04 03:51:00 | NPP-375D | PALMEIRAIS | PIAUÍ | Brasil | 2207504 | 22 | 33 | nan | nan | nan | Caatinga | 2.7 |
| b5d1d2f5-6355-31e9-b10f-51f72734e929 | -7.7679 | -42.61526 | 2025-10-04 03:51:00 | NPP-375D | RIBEIRA DO PIAUÍ | PIAUÍ | Brasil | 2208874 | 22 | 33 | nan | nan | nan | Caatinga | 2.4 |
| 9dc09ff5-414a-3e3b-9743-28b34531f60a | -11.08815 | -47.88422 | 2025-10-04 03:51:00 | NPP-375D | MONTE DO CARMO | TOCANTINS | Brasil | 1713601 | 17 | 33 | nan | nan | nan | Cerrado | 2.6 |
| 81bd1b0b-352d-3d31-811b-928a433803f3 | -5.66047 | -42.7409 | 2025-10-04 03:51:00 | NPP-375D | CURRALINHOS | PIAUÍ | Brasil | 2203255 | 22 | 33 | nan | nan | nan | Caatinga | 7.6 |
| 6e63f0cf-3aac-3d3c-bb8b-f173eac87cb5 | -7.80434 | -42.53507 | 2025-10-04 03:51:00 | NPP-375D | SOCORRO DO PIAUÍ | PIAUÍ | Brasil | 2210904 | 22 | 33 | nan | nan | nan | Caatinga | 3.0 |
| ab2599d4-414f-3c39-8c50-7d5b7d5a315f | -10.92831 | -48.8308 | 2025-10-04 03:51:00 | NPP-375D | FÁTIMA | TOCANTINS | Brasil | 1707553 | 17 | 33 | nan | nan | nan | Cerrado | 0.9 |
| 29169728-5346-3132-a087-e5f37fe1f591 | -11.45514 | -45.14664 | 2025-10-04 03:51:00 | NPP-375D | RIACHÃO DAS NEVES | BAHIA | Brasil | 2926202 | 29 | 33 | nan | nan | nan | Cerrado | 2.3 |
| e6ff0221-15f7-3e59-93e9-07760b11f642 | -11.50319 | -45.00599 | 2025-10-04 03:51:00 | NPP-375D | RIACHÃO DAS NEVES | BAHIA | Brasil | 2926202 | 29 | 33 | nan | nan | nan | Cerrado | 1.3 |
| d4e74490-a4a3-3812-96ec-05483d847bcf | -6.24733 | -45.34948 | 2025-10-04 03:51:00 | NPP-375D | FERNANDO FALCÃO | MARANHÃO | Brasil | 2104081 | 21 | 33 | nan | nan | nan | Cerrado | 4.3 |
| 4a82bc27-469c-3cc6-b034-3b67b2d6b31e | -5.67477 | -43.56656 | 2025-10-04 03:51:00 | NPP-375D | PARNARAMA | MARANHÃO | Brasil | 2107803 | 21 | 33 | nan | nan | nan | Cerrado | 1.2 |
| e528600c-858d-3f41-8e35-243ec7cfd7f5 | -6.37078 | -43.90328 | 2025-10-04 03:51:00 | NPP-375D | PARAIBANO | MARANHÃO | Brasil | 2107704 | 21 | 33 | nan | nan | nan | Cerrado | 3.5 |
| 8e2e0c33-113a-3e33-8c3b-6e974065db58 | -10.99937 | -46.68542 | 2025-10-04 03:51:00 | NPP-375D | MATEIROS | TOCANTINS | Brasil | 1712702 | 17 | 33 | nan | nan | nan | Cerrado | 1.2 |
| 9e88b60f-06c2-3680-b640-7d880850be39 | -11.44825 | -43.49543 | 2025-10-04 03:51:00 | NPP-375D | BARRA | BAHIA | Brasil | 2902708 | 29 | 33 | nan | nan | nan | Cerrado | 2.6 |
| 7e092af4-8617-3d99-b71e-302133232d68 | -6.36442 | -43.8992 | 2025-10-04 03:51:00 | NPP-375D | PARAIBANO | MARANHÃO | Brasil | 2107704 | 21 | 33 | nan | nan | nan | Cerrado | 14.6 |
| e6ff8428-f9c6-39a6-8cbc-a7c73c7d8097 | -6.28337 | -43.62836 | 2025-10-04 03:51:00 | NPP-375D | PASSAGEM FRANCA | MARANHÃO | Brasil | 2107902 | 21 | 33 | nan | nan | nan | Cerrado | 2.2 |
| 9f4a80a2-e6c2-31ba-b13a-44e74fbda197 | -6.6479 | -41.95914 | 2025-10-04 03:51:00 | NPP-375D | OEIRAS | PIAUÍ | Brasil | 2207009 | 22 | 33 | nan | nan | nan | Caatinga | 3.1 |
| 97cba9d1-1baa-326a-adff-837b2c2e67aa | -7.76656 | -46.23607 | 2025-10-04 03:51:00 | NPP-375D | BALSAS | MARANHÃO | Brasil | 2101400 | 21 | 33 | nan | nan | nan | Cerrado | 4.1 |
| 2a17bc63-0b2c-386c-92e2-a1d09abe8076 | -5.01786 | -43.66513 | 2025-10-04 03:51:00 | NPP-375D | SÃO JOÃO DO SOTER | MARANHÃO | Brasil | 2111078 | 21 | 33 | nan | nan | nan | Cerrado | 1.5 |
| 6f36152d-970e-36bc-aa28-b2d0b0ad6cfd | -7.79351 | -42.5647 | 2025-10-04 03:51:00 | NPP-375D | SOCORRO DO PIAUÍ | PIAUÍ | Brasil | 2210904 | 22 | 33 | nan | nan | nan | Caatinga | 2.8 |
| 59ec9f76-22de-3a28-91ba-2236b6c934d1 | -12.08737 | -42.74352 | 2025-10-04 03:51:00 | NPP-375D | OLIVEIRA DOS BREJINHOS | BAHIA | Brasil | 2923209 | 29 | 33 | nan | nan | nan | Caatinga | 1.1 |
| d67b1f12-512f-3b84-888e-1b2cc8205470 | -7.55059 | -42.39652 | 2025-10-04 03:51:00 | NPP-375D | SÃO MIGUEL DO FIDALGO | PIAUÍ | Brasil | 2210391 | 22 | 33 | nan | nan | nan | Caatinga | 4.3 |
| 75291648-e8c5-3892-a0dd-646aef15274e | -6.24726 | -44.24288 | 2025-10-04 03:51:00 | NPP-375D | MIRADOR | MARANHÃO | Brasil | 2106706 | 21 | 33 | nan | nan | nan | Cerrado | 3.1 |
| 26a6a150-5639-3d4c-b70c-ed9dc248863d | -7.72191 | -42.58342 | 2025-10-04 03:51:00 | NPP-375D | SOCORRO DO PIAUÍ | PIAUÍ | Brasil | 2210904 | 22 | 33 | nan | nan | nan | Caatinga | 0.9 |
| e6e0063f-5808-3923-96ac-478b2da8e0d0 | -7.51161 | -44.27291 | 2025-10-04 03:51:00 | NPP-375D | URUÇUÍ | PIAUÍ | Brasil | 2211209 | 22 | 33 | nan | nan | nan | Cerrado | 2.7 |
| 40bf2f77-28f2-33bf-8e3f-fa26645b39eb | -8.91516 | -46.60912 | 2025-10-04 03:51:00 | NPP-375D | BALSAS | MARANHÃO | Brasil | 2101400 | 21 | 33 | nan | nan | nan | Cerrado | 1.9 |
| 58f1d551-7009-3b9e-89f9-5d5a004460be | -5.66902 | -42.71661 | 2025-10-04 03:51:00 | NPP-375D | MIGUEL LEÃO | PIAUÍ | Brasil | 2206308 | 22 | 33 | nan | nan | nan | Caatinga | 4.4 |
| d24adcb0-d80f-39c6-be7d-7b7ac0ff7cf6 | -7.72034 | -42.56769 | 2025-10-04 03:51:00 | NPP-375D | SOCORRO DO PIAUÍ | PIAUÍ | Brasil | 2210904 | 22 | 33 | nan | nan | nan | Caatinga | 1.5 |
| c847fa88-6922-36c3-aed5-c7ae136d04f5 | -7.73653 | -46.31129 | 2025-10-04 03:51:00 | NPP-375D | BALSAS | MARANHÃO | Brasil | 2101400 | 21 | 33 | nan | nan | nan | Cerrado | 13.0 |
| c0574570-66f7-3aad-ac4d-e24d6b2a6cdd | -6.72733 | -45.9755 | 2025-10-04 03:51:00 | NPP-375D | FORTALEZA DOS NOGUEIRAS | MARANHÃO | Brasil | 2104107 | 21 | 33 | nan | nan | nan | Cerrado | 2.5 |
| b732d889-9a5c-3543-bab9-a51da78df0be | -11.04991 | -47.79481 | 2025-10-04 03:51:00 | NPP-375D | SILVANÓPOLIS | TOCANTINS | Brasil | 1720655 | 17 | 33 | nan | nan | nan | Cerrado | 2.3 |
| 7215627c-8f01-3c07-b775-5c43bae3760a | -7.7011 | -42.57988 | 2025-10-04 03:51:00 | NPP-375D | SOCORRO DO PIAUÍ | PIAUÍ | Brasil | 2210904 | 22 | 33 | nan | nan | nan | Caatinga | 1.1 |


[Clique aqui para ver as próximas entradas](README29.md)
