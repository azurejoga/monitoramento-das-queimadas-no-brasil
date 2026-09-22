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

## Dados Diários - Página 145

| ID | Latitude | Longitude | Data/Hora GMT | Satélite | Município | Estado | País | Município ID | Estado ID | País ID | Dias sem Chuva | Precipitação | Risco de Fogo | Bioma | FRP |
|----|----------|-----------|---------------|----------|-----------|--------|------|--------------|-----------|---------|----------------|--------------|----------------|-------|-----|
| b71c5dd7-d4aa-345a-8c44-f16fa811adae | -6.9841 | -49.7777 | 2026-09-22 15:00:00 | GOES-19 | XINGUARA | PARÁ | Brasil | 1508407 | 15 | 33 | nan | nan | nan | Amazônia | 85.8 |
| a206e7fc-be17-3ae2-846a-c2c15d5b63e2 | -8.3777 | -45.6263 | 2026-09-22 15:00:00 | GOES-19 | RIBEIRO GONÇALVES | PIAUÍ | Brasil | 2208908 | 22 | 33 | nan | nan | nan | Cerrado | 113.8 |
| 02fc24f3-b70e-32c4-bc91-28f8a5cf7e3d | -3.6215 | -60.566 | 2026-09-22 15:00:00 | GOES-19 | MANAQUIRI | AMAZONAS | Brasil | 1302553 | 13 | 33 | nan | nan | nan | Amazônia | 111.5 |
| 47d9fdde-1ce9-3b1c-a732-c19eb6001539 | -3.4049 | -59.5794 | 2026-09-22 15:00:00 | GOES-19 | CAREIRO DA VÁRZEA | AMAZONAS | Brasil | 1301159 | 13 | 33 | nan | nan | nan | Amazônia | 68.4 |
| ef65c11d-7c76-35f4-8753-053859793c85 | -11.137 | -51.1071 | 2026-09-22 15:00:00 | GOES-19 | LUCIARA | MATO GROSSO | Brasil | 5105309 | 51 | 33 | nan | nan | nan | Cerrado | 121.4 |
| 8eb0d9e5-e9e1-3390-aefc-3ee527001f41 | -2.4206 | -58.2712 | 2026-09-22 15:00:00 | GOES-19 | ITAPIRANGA | AMAZONAS | Brasil | 1302009 | 13 | 33 | nan | nan | nan | Amazônia | 60.6 |
| 6f1dbfca-6d64-3a8d-b90e-309c344d54b2 | 3.9534 | -59.7206 | 2026-09-22 15:00:00 | GOES-19 | NORMANDIA | RORAIMA | Brasil | 1400407 | 14 | 33 | nan | nan | nan | Amazônia | 56.3 |
| c858fbb4-10dd-3a6f-9d14-741ae1fdb565 | -7.1203 | -43.7323 | 2026-09-22 15:00:00 | GOES-19 | LANDRI SALES | PIAUÍ | Brasil | 2205607 | 22 | 33 | nan | nan | nan | Cerrado | 107.2 |
| 5c729c70-2698-39f0-9f63-d6054fd32cfb | 3.8957 | -60.5984 | 2026-09-22 15:00:00 | GOES-19 | PACARAIMA | RORAIMA | Brasil | 1400456 | 14 | 33 | nan | nan | nan | Amazônia | 64.1 |
| 83a762c5-c3e9-3814-b45e-847d2e285c19 | -3.4598 | -59.5591 | 2026-09-22 15:00:00 | GOES-19 | CAREIRO DA VÁRZEA | AMAZONAS | Brasil | 1301159 | 13 | 33 | nan | nan | nan | Amazônia | 90.2 |
| 71515c8c-bdb1-3ee4-b05c-9c1e2e76429e | -10.5748 | -46.7296 | 2026-09-22 15:00:00 | GOES-19 | MATEIROS | TOCANTINS | Brasil | 1712702 | 17 | 33 | nan | nan | nan | Cerrado | 244.5 |
| 43792dcd-2239-323d-8dce-cbe25de74ab5 | -7.326 | -55.5953 | 2026-09-22 15:00:00 | GOES-19 | NOVO PROGRESSO | PARÁ | Brasil | 1505031 | 15 | 33 | nan | nan | nan | Amazônia | 85.6 |
| 1590d93c-74fc-3c3c-b257-5b590d920c37 | -3.3492 | -59.867 | 2026-09-22 15:00:00 | GOES-19 | CAREIRO DA VÁRZEA | AMAZONAS | Brasil | 1301159 | 13 | 33 | nan | nan | nan | Amazônia | 97.7 |
| 5f0293e0-ca6d-3075-ac22-94e0d3d784c7 | -1.3558 | -49.2945 | 2026-09-22 15:00:00 | GOES-19 | MUANÁ | PARÁ | Brasil | 1504901 | 15 | 33 | nan | nan | nan | Amazônia | 68.2 |
| 7c3fa2a9-d284-3436-b253-7a00192f42b5 | -3.3136 | -59.5046 | 2026-09-22 15:00:00 | GOES-19 | CAREIRO DA VÁRZEA | AMAZONAS | Brasil | 1301159 | 13 | 33 | nan | nan | nan | Amazônia | 58.7 |
| 0968f6e5-e51c-37b7-b561-b56b3b3f46f0 | -3.2372 | -60.8007 | 2026-09-22 15:00:00 | GOES-19 | MANACAPURU | AMAZONAS | Brasil | 1302504 | 13 | 33 | nan | nan | nan | Amazônia | 62.2 |
| f7b397ad-40f4-39ea-9d3d-705fe4cff90a | -5.7304 | -53.465 | 2026-09-22 15:00:00 | GOES-19 | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 54.1 |
| a4ada04a-934a-37a7-bd46-c2bb091de856 | -1.6583 | -54.913 | 2026-09-22 15:00:00 | GOES-19 | ALENQUER | PARÁ | Brasil | 1500404 | 15 | 33 | nan | nan | nan | Amazônia | 63.5 |
| 22e1f0bc-2d90-3826-9850-6014abb4b94d | -8.4985 | -57.6075 | 2026-09-22 15:00:00 | GOES-19 | JACAREACANGA | PARÁ | Brasil | 1503754 | 15 | 33 | nan | nan | nan | Amazônia | 48.8 |
| 2f3179cb-7259-3ec5-acc7-e4f262baafc6 | -3.6447 | -58.9224 | 2026-09-22 15:00:00 | GOES-19 | NOVA OLINDA DO NORTE | AMAZONAS | Brasil | 1303106 | 13 | 33 | nan | nan | nan | Amazônia | 47.7 |
| 03157191-44d7-3564-a0a4-9a52c9665614 | -10.2795 | -50.1963 | 2026-09-22 15:00:00 | GOES-19 | PIUM | TOCANTINS | Brasil | 1717503 | 17 | 33 | nan | nan | nan | Cerrado | 155.4 |
| 393f7fca-1f64-368e-bdc4-e2eac6a82e52 | -3.3138 | -59.4472 | 2026-09-22 15:00:00 | GOES-19 | CAREIRO DA VÁRZEA | AMAZONAS | Brasil | 1301159 | 13 | 33 | nan | nan | nan | Amazônia | 74.1 |
| 0c33a0f8-6f6d-3aaa-af4b-73c2ab7008f3 | -8.1304 | -62.8763 | 2026-09-22 15:00:00 | GOES-19 | PORTO VELHO | RONDÔNIA | Brasil | 1100205 | 11 | 33 | nan | nan | nan | Amazônia | 52.0 |
| 68b46aa3-2a82-34e3-9302-38d5dc2a3444 | -2.5687 | -57.5135 | 2026-09-22 15:00:00 | GOES-19 | URUCURITUBA | AMAZONAS | Brasil | 1304401 | 13 | 33 | nan | nan | nan | Amazônia | 74.4 |
| 6a15d58c-80e4-3e29-944b-27893f42e0cc | -9.247 | -57.1488 | 2026-09-22 15:00:00 | GOES-19 | APIACÁS | MATO GROSSO | Brasil | 5100805 | 51 | 33 | nan | nan | nan | Amazônia | 61.1 |
| e96a4557-6faf-3977-b5ac-5a0a7f6036a8 | -9.3797 | -48.3232 | 2026-09-22 15:00:00 | GOES-19 | TOCANTÍNIA | TOCANTINS | Brasil | 1721109 | 17 | 33 | nan | nan | nan | Cerrado | 50.7 |
| 15773db2-cdd7-37aa-9d5e-3f308db7522b | -3.4599 | -59.54 | 2026-09-22 15:00:00 | GOES-19 | CAREIRO DA VÁRZEA | AMAZONAS | Brasil | 1301159 | 13 | 33 | nan | nan | nan | Amazônia | 108.1 |
| 5ce855b9-d622-3deb-aba0-2c2dc4507285 | -7.9822 | -44.0879 | 2026-09-22 15:00:00 | GOES-19 | SEBASTIÃO LEAL | PIAUÍ | Brasil | 2210631 | 22 | 33 | nan | nan | nan | Cerrado | 78.3 |
| f4a5095c-ddfa-36ae-85d3-4979501efefe | -8.7916 | -44.2778 | 2026-09-22 15:00:00 | GOES-19 | PALMEIRA DO PIAUÍ | PIAUÍ | Brasil | 2207405 | 22 | 33 | nan | nan | nan | Cerrado | 159.9 |
| b7c6ba19-f31c-3fcf-867b-e89bb57c3bf4 | -3.3867 | -59.5415 | 2026-09-22 15:00:00 | GOES-19 | CAREIRO DA VÁRZEA | AMAZONAS | Brasil | 1301159 | 13 | 33 | nan | nan | nan | Amazônia | 46.2 |
| 19fbc514-908d-3785-a06d-71fdc7b845e8 | -5.9335 | -59.9515 | 2026-09-22 15:00:00 | GOES-19 | NOVO ARIPUANÃ | AMAZONAS | Brasil | 1303304 | 13 | 33 | nan | nan | nan | Amazônia | 53.6 |
| 45b591fe-d8ea-3cc1-87d8-d6a8ab2542cd | -3.9509 | -60.5022 | 2026-09-22 15:00:00 | GOES-19 | CAREIRO | AMAZONAS | Brasil | 1301100 | 13 | 33 | nan | nan | nan | Amazônia | 86.2 |
| 80b66271-ca63-3bbc-a7ac-43381fda6390 | -3.5146 | -59.5772 | 2026-09-22 15:00:00 | GOES-19 | CAREIRO DA VÁRZEA | AMAZONAS | Brasil | 1301159 | 13 | 33 | nan | nan | nan | Amazônia | 110.4 |
| 3cecc99c-7b8b-3f00-8038-0d50cbe6487f | -12.8 | -44.2073 | 2026-09-22 15:00:00 | GOES-19 | BAIANÓPOLIS | BAHIA | Brasil | 2902500 | 29 | 33 | nan | nan | nan | Cerrado | 147.3 |
| 9b9d7b8e-781a-3d2a-b7e0-31d60c6756bd | -9.8404 | -46.3911 | 2026-09-22 15:00:00 | GOES-19 | ALTO PARNAÍBA | MARANHÃO | Brasil | 2100501 | 21 | 33 | nan | nan | nan | Cerrado | 86.2 |
| 7b374b09-bb13-3f92-a46c-3a950a52042b | -1.4578 | -54.2367 | 2026-09-22 15:00:00 | GOES-19 | MONTE ALEGRE | PARÁ | Brasil | 1504802 | 15 | 33 | nan | nan | nan | Amazônia | 71.6 |
| ebf35fb5-0cd6-39bc-947d-2435cd0a6bcd | -12.0836 | -50.0378 | 2026-09-22 15:00:00 | GOES-19 | SANDOLÂNDIA | TOCANTINS | Brasil | 1718840 | 17 | 33 | nan | nan | nan | Cerrado | 97.7 |
| 739ffd88-6ea0-3cf4-bf10-af1f9312dcfe | -6.183 | -47.6133 | 2026-09-22 15:00:00 | GOES-19 | TOCANTINÓPOLIS | TOCANTINS | Brasil | 1721208 | 17 | 33 | nan | nan | nan | Cerrado | 50.7 |
| 61d51a3b-48c5-38e4-a50a-863b8c0e8c16 | -11.4345 | -45.3919 | 2026-09-22 15:00:00 | GOES-19 | RIACHÃO DAS NEVES | BAHIA | Brasil | 2926202 | 29 | 33 | nan | nan | nan | Cerrado | 150.6 |
| e831fbe6-19f9-316f-8efe-389fa4a20c43 | -3.6033 | -60.5664 | 2026-09-22 15:00:00 | GOES-19 | MANAQUIRI | AMAZONAS | Brasil | 1302553 | 13 | 33 | nan | nan | nan | Amazônia | 90.3 |
| 6edf9bc9-2521-3e3c-9b66-0be359d3a6a0 | -5.8314 | -52.1918 | 2026-09-22 15:00:00 | GOES-19 | SÃO FÉLIX DO XINGU | PARÁ | Brasil | 1507300 | 15 | 33 | nan | nan | nan | Amazônia | 77.9 |
| a8708260-bf96-3e64-9e74-5f5e188edf56 | -3.2955 | -59.4284 | 2026-09-22 15:00:00 | GOES-19 | CAREIRO DA VÁRZEA | AMAZONAS | Brasil | 1301159 | 13 | 33 | nan | nan | nan | Amazônia | 56.8 |
| 1c129df6-42df-3f77-86ac-2a8636bfdafb | -6.2017 | -47.612 | 2026-09-22 15:00:00 | GOES-19 | TOCANTINÓPOLIS | TOCANTINS | Brasil | 1721208 | 17 | 33 | nan | nan | nan | Cerrado | 45.9 |
| d2e0c713-eede-36bc-81a3-fb1f82d11903 | -9.859 | -46.4114 | 2026-09-22 15:00:00 | GOES-19 | ALTO PARNAÍBA | MARANHÃO | Brasil | 2100501 | 21 | 33 | nan | nan | nan | Cerrado | 84.8 |
| 5d349940-c30e-37e4-8f94-ce4872efc91d | -5.9151 | -59.9522 | 2026-09-22 15:00:00 | GOES-19 | NOVO ARIPUANÃ | AMAZONAS | Brasil | 1303304 | 13 | 33 | nan | nan | nan | Amazônia | 58.5 |
| 82d3b57d-501f-36cd-9498-aef18eafacc2 | -9.6108 | -43.9477 | 2026-09-22 15:00:00 | GOES-19 | MORRO CABEÇA NO TEMPO | PIAUÍ | Brasil | 2206654 | 22 | 33 | nan | nan | nan | Caatinga | 200.6 |
| 9687365c-2062-3f33-b490-9459c8756940 | -6.0924 | -57.7043 | 2026-09-22 15:00:00 | GOES-19 | JACAREACANGA | PARÁ | Brasil | 1503754 | 15 | 33 | nan | nan | nan | Amazônia | 71.5 |
| 9c020c55-e9a2-3add-b578-82cb2893984e | -9.9516 | -53.9844 | 2026-09-22 15:00:00 | GOES-19 | PEIXOTO DE AZEVEDO | MATO GROSSO | Brasil | 5106422 | 51 | 33 | nan | nan | nan | Amazônia | 66.8 |
| 868ff359-9517-3d92-8360-5fbd35623e86 | 4.0579 | -61.4095 | 2026-09-22 15:00:00 | GOES-19 | AMAJARI | RORAIMA | Brasil | 1400027 | 14 | 33 | nan | nan | nan | Amazônia | 74.3 |
| c2eacaef-d678-3cf1-a598-903ff0aa208e | -12.3824 | -47.0057 | 2026-09-22 15:00:00 | GOES-19 | ARRAIAS | TOCANTINS | Brasil | 1702406 | 17 | 33 | nan | nan | nan | Cerrado | 283.6 |
| 5faba018-93ca-34f5-b4d8-4f1954d307a9 | -6.2396 | -41.6634 | 2026-09-22 15:00:00 | GOES-19 | PIMENTEIRAS | PIAUÍ | Brasil | 2208106 | 22 | 33 | nan | nan | nan | Caatinga | 221.3 |
| fcaa78ab-d557-34aa-a1bf-29cb05f65f6c | -2.9723 | -57.1945 | 2026-09-22 15:00:00 | GOES-19 | BARREIRINHA | AMAZONAS | Brasil | 1300508 | 13 | 33 | nan | nan | nan | Amazônia | 53.7 |
| 697cd3dd-b486-34a6-baad-9bee43cf9e10 | -6.3014 | -59.9579 | 2026-09-22 15:00:00 | GOES-19 | NOVO ARIPUANÃ | AMAZONAS | Brasil | 1303304 | 13 | 33 | nan | nan | nan | Amazônia | 56.0 |
| f05b544e-3eee-34b4-bade-0551a0c0f61e | -3.0535 | -61.2578 | 2026-09-22 15:00:00 | GOES-19 | MANACAPURU | AMAZONAS | Brasil | 1302504 | 13 | 33 | nan | nan | nan | Amazônia | 50.2 |
| 51aa6916-af00-32d1-a850-dd824cd7b208 | -7.917 | -61.3481 | 2026-09-22 15:00:00 | GOES-19 | MANICORÉ | AMAZONAS | Brasil | 1302702 | 13 | 33 | nan | nan | nan | Amazônia | 86.2 |
| f55c64b8-4057-37d9-9855-e52d07568e93 | -12.3293 | -50.1802 | 2026-09-22 15:00:00 | GOES-19 | FORMOSO DO ARAGUAIA | TOCANTINS | Brasil | 1708205 | 17 | 33 | nan | nan | nan | Cerrado | 474.2 |
| 0d577dc3-a6e4-3d71-9505-37f5c2d0022b | -3.5136 | -59.9401 | 2026-09-22 15:00:00 | GOES-19 | CAREIRO | AMAZONAS | Brasil | 1301100 | 13 | 33 | nan | nan | nan | Amazônia | 45.3 |
| 6df32ac8-2608-3bf9-9288-6debf75a3af0 | -9.6111 | -43.9243 | 2026-09-22 15:00:00 | GOES-19 | MORRO CABEÇA NO TEMPO | PIAUÍ | Brasil | 2206654 | 22 | 33 | nan | nan | nan | Caatinga | 578.1 |
| 046030d5-f6a0-3425-aa26-2414cf6dfe95 | -7.9172 | -61.329 | 2026-09-22 15:00:00 | GOES-19 | MANICORÉ | AMAZONAS | Brasil | 1302702 | 13 | 33 | nan | nan | nan | Amazônia | 76.6 |
| f62fe004-3ad9-3ae3-beb9-61eba6735167 | -6.2394 | -41.6875 | 2026-09-22 15:00:00 | GOES-19 | AROAZES | PIAUÍ | Brasil | 2200905 | 22 | 33 | nan | nan | nan | Caatinga | 94.8 |
| 37f67759-37b7-3f16-a7d5-bb9bf4c83208 | -3.0534 | -61.2767 | 2026-09-22 15:00:00 | GOES-19 | MANACAPURU | AMAZONAS | Brasil | 1302504 | 13 | 33 | nan | nan | nan | Amazônia | 63.6 |
| b7f72a61-2260-37ff-9bc9-0d07c4e1810f | -11.1557 | -51.1263 | 2026-09-22 15:00:00 | GOES-19 | LUCIARA | MATO GROSSO | Brasil | 5105309 | 51 | 33 | nan | nan | nan | Cerrado | 105.1 |
| 901916bd-dcca-32c0-9659-bd6fe16fa8c8 | -6.9868 | -47.5104 | 2026-09-22 15:00:00 | GOES-19 | CAROLINA | MARANHÃO | Brasil | 2102804 | 21 | 33 | nan | nan | nan | Cerrado | 62.3 |
| 28555f86-6aaf-3a52-90c4-784efdd70284 | -11.8559 | -49.979 | 2026-09-22 15:00:00 | GOES-19 | FORMOSO DO ARAGUAIA | TOCANTINS | Brasil | 1708205 | 17 | 33 | nan | nan | nan | Cerrado | 103.2 |
| 2990975d-e1f1-3a43-a141-c7252d846cbc | -3.3183 | -57.8677 | 2026-09-22 15:00:00 | GOES-19 | MAUÉS | AMAZONAS | Brasil | 1302900 | 13 | 33 | nan | nan | nan | Amazônia | 67.7 |
| df144edb-afb7-3cc8-a241-7bc6596078bd | -3.1901 | -57.8898 | 2026-09-22 15:00:00 | GOES-19 | BOA VISTA DO RAMOS | AMAZONAS | Brasil | 1300680 | 13 | 33 | nan | nan | nan | Amazônia | 55.3 |
| 28fde613-2b4c-3fba-84bd-ac2852458d61 | -9.5356 | -47.9349 | 2026-09-22 15:00:00 | GOES-19 | RIO SONO | TOCANTINS | Brasil | 1718758 | 17 | 33 | nan | nan | nan | Cerrado | 40.1 |
| 7c6a1d82-3d89-37c9-b456-947f50267d05 | -8.7772 | -49.955 | 2026-09-22 15:00:00 | GOES-19 | SANTA MARIA DAS BARREIRAS | PARÁ | Brasil | 1506583 | 15 | 33 | nan | nan | nan | Amazônia | 67.0 |
| 6a7b518e-9f10-3bd8-b1d8-094dde2636a5 | -4.0925 | -62.0874 | 2026-09-22 15:00:00 | GOES-19 | ANORI | AMAZONAS | Brasil | 1300102 | 13 | 33 | nan | nan | nan | Amazônia | 82.7 |
| 1cea3755-8fd6-355b-a412-0cbf4c07feb7 | -8.3134 | -44.7446 | 2026-09-22 15:00:00 | GOES-19 | PALMEIRA DO PIAUÍ | PIAUÍ | Brasil | 2207405 | 22 | 33 | nan | nan | nan | Cerrado | 79.3 |
| a25c28bf-643f-3f57-8140-f34d139c9335 | -5.8225 | -53.5214 | 2026-09-22 15:00:00 | GOES-19 | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 51.2 |
| 9bcd5086-54c2-327b-b676-d86dc7ffddb4 | -10.8858 | -56.196 | 2026-09-22 15:00:00 | GOES-19 | NOVA CANAÃ DO NORTE | MATO GROSSO | Brasil | 5106216 | 51 | 33 | nan | nan | nan | Amazônia | 53.0 |
| f98548f6-bd06-38e0-9ebb-34324fe834ae | -3.7364 | -58.8626 | 2026-09-22 15:00:00 | GOES-19 | NOVA OLINDA DO NORTE | AMAZONAS | Brasil | 1303106 | 13 | 33 | nan | nan | nan | Amazônia | 78.4 |
| 8a9d7f0d-f820-31ef-878b-b6c6996b5bbb | -3.8096 | -58.8994 | 2026-09-22 15:00:00 | GOES-19 | NOVA OLINDA DO NORTE | AMAZONAS | Brasil | 1303106 | 13 | 33 | nan | nan | nan | Amazônia | 57.7 |
| 656e1965-6b2f-38b9-830a-9a88789d065f | -1.5858 | -54.4353 | 2026-09-22 15:00:00 | GOES-19 | ALENQUER | PARÁ | Brasil | 1500404 | 15 | 33 | nan | nan | nan | Amazônia | 78.0 |
| 3eaa3e2d-d82f-3aec-aa94-bb7e1bab8e0a | -8.7912 | -44.301 | 2026-09-22 15:00:00 | GOES-19 | PALMEIRA DO PIAUÍ | PIAUÍ | Brasil | 2207405 | 22 | 33 | nan | nan | nan | Cerrado | 74.8 |
| 1cb433c6-42a6-3473-bb48-c5f04a80ad9a | -8.7706 | -45.8567 | 2026-09-22 15:00:00 | GOES-19 | SANTA FILOMENA | PIAUÍ | Brasil | 2209203 | 22 | 33 | nan | nan | nan | Cerrado | 86.0 |
| be3b4225-6bcf-318f-befc-c76db241e04d | -3.8279 | -58.899 | 2026-09-22 15:00:00 | GOES-19 | NOVA OLINDA DO NORTE | AMAZONAS | Brasil | 1303106 | 13 | 33 | nan | nan | nan | Amazônia | 61.3 |
| 1b991221-b2ae-3303-84c9-6f0b71dd257b | -7.9825 | -44.0647 | 2026-09-22 15:00:00 | GOES-19 | SEBASTIÃO LEAL | PIAUÍ | Brasil | 2210631 | 22 | 33 | nan | nan | nan | Cerrado | 79.1 |
| 8a5c6801-6d22-348e-acf3-be63f996f4d5 | -6.0925 | -57.6847 | 2026-09-22 15:00:00 | GOES-19 | JACAREACANGA | PARÁ | Brasil | 1503754 | 15 | 33 | nan | nan | nan | Amazônia | 257.7 |
| 7f55135d-b47d-3422-98a8-3b97fbfadc59 | -5.8489 | -49.7875 | 2026-09-22 15:00:00 | GOES-19 | CURIONÓPOLIS | PARÁ | Brasil | 1502772 | 15 | 33 | nan | nan | nan | Amazônia | 55.0 |
| c0149a22-1274-3d25-b630-d18b9cea4304 | -9.7883 | -46.0593 | 2026-09-22 15:00:00 | GOES-19 | ALTO PARNAÍBA | MARANHÃO | Brasil | 2100501 | 21 | 33 | nan | nan | nan | Cerrado | 67.8 |
| a6725413-2623-381c-ab38-1a124e142a29 | -3.331 | -59.8292 | 2026-09-22 15:00:00 | GOES-19 | CAREIRO DA VÁRZEA | AMAZONAS | Brasil | 1301159 | 13 | 33 | nan | nan | nan | Amazônia | 65.3 |
| 9de8eb2e-8e7a-3495-a14d-7cfaec738e01 | -3.8039 | -60.7332 | 2026-09-22 15:00:00 | GOES-19 | MANAQUIRI | AMAZONAS | Brasil | 1302553 | 13 | 33 | nan | nan | nan | Amazônia | 47.6 |
| 24f79efa-ff45-34a0-b26d-350723a247ce | -3.3358 | -58.1384 | 2026-09-22 15:00:00 | GOES-19 | ITACOATIARA | AMAZONAS | Brasil | 1301902 | 13 | 33 | nan | nan | nan | Amazônia | 51.1 |
| 2132c8fb-4765-322d-8b52-6c066b317f2d | -3.4009 | -61.0629 | 2026-09-22 15:00:00 | GOES-19 | MANACAPURU | AMAZONAS | Brasil | 1302504 | 13 | 33 | nan | nan | nan | Amazônia | 74.3 |
| f9b77a9d-3bf8-312f-a7f3-0367353c992d | -12.6799 | -50.9526 | 2026-09-22 15:00:00 | GOES-19 | RIBEIRÃO CASCALHEIRA | MATO GROSSO | Brasil | 5107180 | 51 | 33 | nan | nan | nan | Cerrado | 91.8 |
| 95b2f6de-ec85-30d9-aab8-208572bc8928 | -6.4484 | -60.0101 | 2026-09-22 15:00:00 | GOES-19 | NOVO ARIPUANÃ | AMAZONAS | Brasil | 1303304 | 13 | 33 | nan | nan | nan | Amazônia | 64.4 |
| a24c631d-a5bd-3e4f-9034-d9530302329e | -3.2396 | -53.9417 | 2026-09-22 15:00:00 | GOES-19 | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | 154.2 |
| f29658d2-bbb3-372d-9436-a0f85d431c4d | -6.4485 | -59.9909 | 2026-09-22 15:00:00 | GOES-19 | NOVO ARIPUANÃ | AMAZONAS | Brasil | 1303304 | 13 | 33 | nan | nan | nan | Amazônia | 103.6 |
| d1c66c66-6390-3b99-a045-f843bf9d89a8 | -3.6032 | -60.5853 | 2026-09-22 15:00:00 | GOES-19 | MANAQUIRI | AMAZONAS | Brasil | 1302553 | 13 | 33 | nan | nan | nan | Amazônia | 60.8 |
| a164da08-7372-3b01-ad77-4dae4abab5c5 | -6.0926 | -57.6652 | 2026-09-22 15:00:00 | GOES-19 | JACAREACANGA | PARÁ | Brasil | 1503754 | 15 | 33 | nan | nan | nan | Amazônia | 152.2 |
| 6e1cdd70-db49-3e6a-b632-b9e9f647054e | -2.9723 | -57.214 | 2026-09-22 15:00:00 | GOES-19 | BARREIRINHA | AMAZONAS | Brasil | 1300508 | 13 | 33 | nan | nan | nan | Amazônia | 73.4 |
| a8b3975a-6e79-3cd1-8822-75da8864b49c | -11.1183 | -54.0062 | 2026-09-22 15:00:00 | GOES-19 | MARCELÂNDIA | MATO GROSSO | Brasil | 5105580 | 51 | 33 | nan | nan | nan | Amazônia | 79.5 |
| 1f84bbe9-f55e-32b0-a821-12de91edb2ea | -8.7703 | -45.8793 | 2026-09-22 15:00:00 | GOES-19 | SANTA FILOMENA | PIAUÍ | Brasil | 2209203 | 22 | 33 | nan | nan | nan | Cerrado | 65.8 |
| 9eda44f5-5e53-35b1-acb8-f50cbc6b188b | -9.1708 | -50.0049 | 2026-09-22 15:00:00 | GOES-19 | SANTANA DO ARAGUAIA | PARÁ | Brasil | 1506708 | 15 | 33 | nan | nan | nan | Amazônia | 65.3 |
| d6b841fd-9c57-3e45-83cc-d428f2e0b7cf | -7.4124 | -49.853 | 2026-09-22 15:00:00 | GOES-19 | RIO MARIA | PARÁ | Brasil | 1506161 | 15 | 33 | nan | nan | nan | Amazônia | 69.2 |
| 302979d7-7feb-3235-b6c9-feaeff528cd1 | -6.9414 | -42.907 | 2026-09-22 15:00:00 | GOES-19 | FLORIANO | PIAUÍ | Brasil | 2203909 | 22 | 33 | nan | nan | nan | Caatinga | 431.7 |
| c4ebe994-cebb-3ecb-a357-9501de474526 | -5.3646 | -56.0249 | 2026-09-22 15:00:00 | GOES-19 | TRAIRÃO | PARÁ | Brasil | 1508050 | 15 | 33 | nan | nan | nan | Amazônia | 58.1 |
| cfdaf66a-e2e9-3f82-a45b-0bb80eb58f4a | -6.3015 | -59.9387 | 2026-09-22 15:00:00 | GOES-19 | NOVO ARIPUANÃ | AMAZONAS | Brasil | 1303304 | 13 | 33 | nan | nan | nan | Amazônia | 50.8 |


[Clique aqui para ver as próximas entradas](README146.md)
