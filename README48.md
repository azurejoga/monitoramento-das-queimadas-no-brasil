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
| 1edb8e1e-cf70-3feb-8702-613996a058bd | -5.63757 | -47.61424 | 2025-10-28 04:42:00 | NPP-375D | SÍTIO NOVO DO TOCANTINS | TOCANTINS | Brasil | 1720804 | 17 | 33 | nan | nan | nan | Cerrado | 1.3 |
| 9c102845-bbfb-332d-8b04-2cdee0c3af9e | -5.64782 | -47.63839 | 2025-10-28 04:42:00 | NPP-375D | SÍTIO NOVO DO TOCANTINS | TOCANTINS | Brasil | 1720804 | 17 | 33 | nan | nan | nan | Cerrado | 2.0 |
| fb170db9-a168-32b7-9f25-ffce1b5a7d35 | -1.55852 | -55.41378 | 2025-10-28 04:42:00 | NPP-375D | ÓBIDOS | PARÁ | Brasil | 1505106 | 15 | 33 | nan | nan | nan | Amazônia | 2.1 |
| a63d40d3-93e2-361e-aae9-f424e60f4a80 | -2.19326 | -56.98129 | 2025-10-28 04:42:00 | NPP-375D | NHAMUNDÁ | AMAZONAS | Brasil | 1303007 | 13 | 33 | nan | nan | nan | Amazônia | 1.1 |
| 8a9d86cc-eed9-3af8-a14c-eb9e5fd4fbfb | -6.44586 | -42.35692 | 2025-10-28 04:42:00 | NPP-375D | REGENERAÇÃO | PIAUÍ | Brasil | 2208809 | 22 | 33 | nan | nan | nan | Caatinga | 2.6 |
| 20dc29c7-18da-3b3d-9099-e4c5695571b2 | -7.81811 | -46.46615 | 2025-10-28 04:42:00 | NPP-375D | RIACHÃO | MARANHÃO | Brasil | 2109502 | 21 | 33 | nan | nan | nan | Cerrado | 2.5 |
| be1407fe-49f4-331b-9a8d-42ceb097bff3 | -6.16539 | -43.10057 | 2025-10-28 04:42:00 | NPP-375D | SÃO FRANCISCO DO MARANHÃO | MARANHÃO | Brasil | 2110906 | 21 | 33 | nan | nan | nan | Cerrado | 1.7 |
| 9bf9a934-61e2-3427-92e2-ba42782241a2 | -7.81206 | -46.45657 | 2025-10-28 04:42:00 | NPP-375D | RIACHÃO | MARANHÃO | Brasil | 2109502 | 21 | 33 | nan | nan | nan | Cerrado | 10.6 |
| 0247ac39-9bec-3532-8e9e-2ad2c4d92cfc | -7.3936 | -44.78471 | 2025-10-28 04:42:00 | NPP-375D | URUÇUÍ | PIAUÍ | Brasil | 2211209 | 22 | 33 | nan | nan | nan | Cerrado | 1.9 |
| eccdc510-b2a6-3a59-8f9c-a59c931191d3 | -4.74063 | -48.30424 | 2025-10-28 04:42:00 | NPP-375D | RONDON DO PARÁ | PARÁ | Brasil | 1506187 | 15 | 33 | nan | nan | nan | Amazônia | 1.0 |
| 96b64889-31ef-359d-addc-e3a40612b054 | -3.71045 | -41.5657 | 2025-10-28 04:42:00 | NPP-375D | PIRACURUCA | PIAUÍ | Brasil | 2208304 | 22 | 33 | nan | nan | nan | Caatinga | 3.3 |
| bfdea4da-619f-3895-9e76-2bee6200c80c | -3.37219 | -50.17669 | 2025-10-28 04:42:00 | NPP-375D | PACAJÁ | PARÁ | Brasil | 1505486 | 15 | 33 | nan | nan | nan | Amazônia | 1.4 |
| 3c203614-e390-3501-a91a-3d9280ab15b0 | -3.24123 | -50.64869 | 2025-10-28 04:42:00 | NPP-375D | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 1.2 |
| 93be23a2-c987-3aa6-9e7b-4e88e2d39d45 | -6.23004 | -42.53212 | 2025-10-28 04:42:00 | NPP-375D | REGENERAÇÃO | PIAUÍ | Brasil | 2208809 | 22 | 33 | nan | nan | nan | Caatinga | 1.8 |
| cd73c599-4dd5-3b06-86c8-fb57ee7ba6c4 | -7.95172 | -45.52041 | 2025-10-28 04:42:00 | NPP-375D | RIBEIRO GONÇALVES | PIAUÍ | Brasil | 2208908 | 22 | 33 | nan | nan | nan | Cerrado | 13.2 |
| f73ab8d3-e7e3-356c-b4e9-5406e3b3cff7 | -7.8209 | -46.42278 | 2025-10-28 04:42:00 | NPP-375D | BALSAS | MARANHÃO | Brasil | 2101400 | 21 | 33 | nan | nan | nan | Cerrado | 1.5 |
| 03b1eca9-6273-3526-bcac-bfc60988f2f9 | -4.06597 | -49.44519 | 2025-10-28 04:42:00 | NPP-375D | BREU BRANCO | PARÁ | Brasil | 1501782 | 15 | 33 | nan | nan | nan | Amazônia | 0.7 |
| f1604d3f-5b50-3f73-bb40-01004aa02e2a | -5.61094 | -42.77195 | 2025-10-28 04:42:00 | NPP-375D | CURRALINHOS | PIAUÍ | Brasil | 2203255 | 22 | 33 | nan | nan | nan | Caatinga | 1.6 |
| cfd38cee-cca3-35e9-b62c-7425a2511358 | -1.55772 | -55.41858 | 2025-10-28 04:42:00 | NPP-375D | ÓBIDOS | PARÁ | Brasil | 1505106 | 15 | 33 | nan | nan | nan | Amazônia | 2.1 |
| 0dbfd40a-a9ee-3da8-a119-3dc6b0a456a9 | -7.60159 | -43.59148 | 2025-10-28 04:42:00 | NPP-375D | CANAVIEIRA | PIAUÍ | Brasil | 2202251 | 22 | 33 | nan | nan | nan | Cerrado | 2.2 |
| 8e23644a-7251-3ae4-ad95-8a5a8a6d73cf | -7.00332 | -46.99463 | 2025-10-28 04:42:00 | NPP-375D | ESTREITO | MARANHÃO | Brasil | 2104057 | 21 | 33 | nan | nan | nan | Cerrado | 2.7 |
| 667e4719-d948-3dc0-9f5e-4262066556c4 | -3.14834 | -50.33371 | 2025-10-28 04:42:00 | NPP-375D | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 1.8 |
| 1047a269-3c1a-385c-a1f3-c95be55daf95 | -7.9643 | -46.75629 | 2025-10-28 04:42:00 | NPP-375D | CAMPOS LINDOS | TOCANTINS | Brasil | 1703842 | 17 | 33 | nan | nan | nan | Cerrado | 2.3 |
| d87a9ab0-7d66-38e9-897d-ea7c48b8aea7 | -7.85916 | -46.39332 | 2025-10-28 04:42:00 | NPP-375D | BALSAS | MARANHÃO | Brasil | 2101400 | 21 | 33 | nan | nan | nan | Cerrado | 1.3 |
| 63594bbc-acab-3069-b3bf-a13550983f97 | -6.28728 | -42.8744 | 2025-10-28 04:42:00 | NPP-375D | SÃO FRANCISCO DO MARANHÃO | MARANHÃO | Brasil | 2110906 | 21 | 33 | nan | nan | nan | Cerrado | 2.5 |
| fe90d4a3-6a98-39dd-a7f1-0c56ea4a48fe | -3.17297 | -45.64821 | 2025-10-28 04:42:00 | NPP-375D | ZÉ DOCA | MARANHÃO | Brasil | 2114007 | 21 | 33 | nan | nan | nan | Amazônia | 1.4 |
| 1b4cbd33-9695-3604-a3f4-c6cc88cadb64 | -7.85244 | -46.38804 | 2025-10-28 04:42:00 | NPP-375D | BALSAS | MARANHÃO | Brasil | 2101400 | 21 | 33 | nan | nan | nan | Cerrado | 1.2 |
| b913bb31-3d42-377e-978b-4a63fbee76ff | -4.57309 | -46.49549 | 2025-10-28 04:42:00 | NPP-375D | BOM JESUS DAS SELVAS | MARANHÃO | Brasil | 2102036 | 21 | 33 | nan | nan | nan | Amazônia | 0.9 |
| fddaa777-b7f9-32de-a497-f81511553a39 | -8.11011 | -45.95781 | 2025-10-28 04:42:00 | NPP-375D | BALSAS | MARANHÃO | Brasil | 2101400 | 21 | 33 | nan | nan | nan | Cerrado | 1.2 |
| 96403943-2294-3c0e-b3cb-d0261fabe1fd | -5.19637 | -46.14855 | 2025-10-28 04:42:00 | NPP-375D | ARAME | MARANHÃO | Brasil | 2100956 | 21 | 33 | nan | nan | nan | Amazônia | 1.4 |
| 5e755b49-e8ec-3af9-8c4c-7740fcdcf753 | -5.58977 | -47.17243 | 2025-10-28 04:42:00 | NPP-375D | BURITIRANA | MARANHÃO | Brasil | 2102358 | 21 | 33 | nan | nan | nan | Cerrado | 0.8 |
| 5e5958ef-4b89-37c8-bc65-b59b1c40ba1f | -4.31599 | -50.36848 | 2025-10-28 04:42:00 | NPP-375D | NOVO REPARTIMENTO | PARÁ | Brasil | 1505064 | 15 | 33 | nan | nan | nan | Amazônia | 0.4 |
| 99e88723-379e-36f9-a35c-4833b25b5213 | -5.79532 | -43.97302 | 2025-10-28 04:42:00 | NPP-375D | BURITI BRAVO | MARANHÃO | Brasil | 2102309 | 21 | 33 | nan | nan | nan | Cerrado | 0.8 |
| e3c2a1f9-7772-38ab-9419-579de196cae0 | -6.28862 | -42.86523 | 2025-10-28 04:42:00 | NPP-375D | SÃO FRANCISCO DO MARANHÃO | MARANHÃO | Brasil | 2110906 | 21 | 33 | nan | nan | nan | Cerrado | 1.2 |
| ca977ef7-6f2f-389a-9981-f781bb2642db | -8.07609 | -45.95279 | 2025-10-28 04:42:00 | NPP-375D | BALSAS | MARANHÃO | Brasil | 2101400 | 21 | 33 | nan | nan | nan | Cerrado | 1.7 |
| 83e335c4-0d7a-37f2-ab44-f321bb92f2d5 | -5.60325 | -42.77287 | 2025-10-28 04:42:00 | NPP-375D | CURRALINHOS | PIAUÍ | Brasil | 2203255 | 22 | 33 | nan | nan | nan | Caatinga | 1.5 |
| f1bb836d-58f0-3024-9529-6b49b327677d | -6.29248 | -44.70316 | 2025-10-28 04:42:00 | NPP-375D | MIRADOR | MARANHÃO | Brasil | 2106706 | 21 | 33 | nan | nan | nan | Cerrado | 2.1 |
| a24189c4-6597-3dbf-8c19-4612c5b04542 | -7.97465 | -46.73655 | 2025-10-28 04:42:00 | NPP-375D | CAMPOS LINDOS | TOCANTINS | Brasil | 1703842 | 17 | 33 | nan | nan | nan | Cerrado | 3.9 |
| 5f821b8a-1540-3bca-b991-216773b1606c | -4.35606 | -50.5147 | 2025-10-28 04:42:00 | NPP-375D | NOVO REPARTIMENTO | PARÁ | Brasil | 1505064 | 15 | 33 | nan | nan | nan | Amazônia | 0.5 |
| ddcb867b-80b0-3438-8ceb-3379e09eb100 | -5.30014 | -48.70231 | 2025-10-28 04:42:00 | NPP-375D | BOM JESUS DO TOCANTINS | PARÁ | Brasil | 1501576 | 15 | 33 | nan | nan | nan | Amazônia | 1.6 |
| dedc67cc-6134-35a9-a8a0-6584d4c10077 | -5.23813 | -49.49903 | 2025-10-28 04:42:00 | NPP-375D | ITUPIRANGA | PARÁ | Brasil | 1503705 | 15 | 33 | nan | nan | nan | Amazônia | 1.7 |
| f5dcb1e3-0435-3638-9535-61a3068f928a | -7.08512 | -47.12001 | 2025-10-28 04:42:00 | NPP-375D | CAROLINA | MARANHÃO | Brasil | 2102804 | 21 | 33 | nan | nan | nan | Cerrado | 1.0 |
| 2fc2a09b-4149-3670-a770-e3c891387927 | -7.81446 | -46.46555 | 2025-10-28 04:42:00 | NPP-375D | RIACHÃO | MARANHÃO | Brasil | 2109502 | 21 | 33 | nan | nan | nan | Cerrado | 7.0 |
| fbace583-f660-31bc-b03f-2cf0d4e904de | -8.1472 | -47.00081 | 2025-10-28 04:42:00 | NPP-375D | CAMPOS LINDOS | TOCANTINS | Brasil | 1703842 | 17 | 33 | nan | nan | nan | Cerrado | 1.5 |
| c30e282a-a1af-361f-a330-79b97d3687b3 | -7.97394 | -45.50414 | 2025-10-28 04:42:00 | NPP-375D | RIBEIRO GONÇALVES | PIAUÍ | Brasil | 2208908 | 22 | 33 | nan | nan | nan | Cerrado | 4.7 |
| d603196e-054e-3b74-8ec9-ef5c29566791 | -2.75163 | -45.40955 | 2025-10-28 04:42:00 | NPP-375D | PEDRO DO ROSÁRIO | MARANHÃO | Brasil | 2108256 | 21 | 33 | nan | nan | nan | Amazônia | 1.5 |
| 5c9749af-c2b2-38c5-b943-ed2f8b5f7720 | -3.40188 | -50.27673 | 2025-10-28 04:42:00 | NPP-375D | PACAJÁ | PARÁ | Brasil | 1505486 | 15 | 33 | nan | nan | nan | Amazônia | 1.5 |
| a919b6da-5b1b-313b-86fc-1bb150292961 | -4.42666 | -45.90079 | 2025-10-28 04:42:00 | NPP-375D | SANTA LUZIA | MARANHÃO | Brasil | 2110005 | 21 | 33 | nan | nan | nan | Amazônia | 0.8 |
| 8254ad7b-a1ae-34bb-adce-30606aa9824d | -1.69084 | -55.67164 | 2025-10-28 04:42:00 | NPP-375D | ÓBIDOS | PARÁ | Brasil | 1505106 | 15 | 33 | nan | nan | nan | Amazônia | 2.9 |
| e1ef623e-5b25-3e28-9117-c605e2f80436 | -7.22139 | -46.863 | 2025-10-28 04:42:00 | NPP-375D | CAROLINA | MARANHÃO | Brasil | 2102804 | 21 | 33 | nan | nan | nan | Cerrado | 1.1 |
| 88e48614-4b68-3546-9b00-65e559bba804 | -5.62961 | -47.62054 | 2025-10-28 04:42:00 | NPP-375D | SÍTIO NOVO DO TOCANTINS | TOCANTINS | Brasil | 1720804 | 17 | 33 | nan | nan | nan | Cerrado | 1.7 |
| 8dcff908-9ac7-35e2-90a4-d3ed9674aa23 | -7.75266 | -46.50396 | 2025-10-28 04:42:00 | NPP-375D | RIACHÃO | MARANHÃO | Brasil | 2109502 | 21 | 33 | nan | nan | nan | Cerrado | 2.0 |
| 4b510e95-9791-3cdd-bb61-3bd14191dfef | -4.71682 | -46.42796 | 2025-10-28 04:42:00 | NPP-375D | BURITICUPU | MARANHÃO | Brasil | 2102325 | 21 | 33 | nan | nan | nan | Amazônia | 5.0 |
| 3161b253-59d6-3d99-8413-6346daa03f0f | -2.58572 | -48.40511 | 2025-10-28 04:42:00 | NPP-375D | TOMÉ-AÇU | PARÁ | Brasil | 1508001 | 15 | 33 | nan | nan | nan | Amazônia | 1.3 |
| 234e7016-0c2e-37db-8ed7-2308e553f163 | -5.64839 | -47.63473 | 2025-10-28 04:42:00 | NPP-375D | SÍTIO NOVO DO TOCANTINS | TOCANTINS | Brasil | 1720804 | 17 | 33 | nan | nan | nan | Cerrado | 2.3 |
| c8cb670c-2245-3602-9b5b-d1f419e7612b | -5.6467 | -47.64569 | 2025-10-28 04:42:00 | NPP-375D | SÍTIO NOVO DO TOCANTINS | TOCANTINS | Brasil | 1720804 | 17 | 33 | nan | nan | nan | Cerrado | 1.7 |
| 8038e98d-9b7c-3f26-b432-bf7f9d6dc1c0 | -2.80425 | -49.14316 | 2025-10-28 04:42:00 | NPP-375D | MOJU | PARÁ | Brasil | 1504703 | 15 | 33 | nan | nan | nan | Amazônia | 1.6 |
| dd48136c-75ff-38db-847a-cacc0f278845 | -3.59286 | -48.99118 | 2025-10-28 04:42:00 | NPP-375D | GOIANÉSIA DO PARÁ | PARÁ | Brasil | 1503093 | 15 | 33 | nan | nan | nan | Amazônia | 0.9 |
| f65869a6-c56b-3b7d-9d4d-233876d2cec0 | -7.99906 | -46.19114 | 2025-10-28 04:42:00 | NPP-375D | BALSAS | MARANHÃO | Brasil | 2101400 | 21 | 33 | nan | nan | nan | Cerrado | 5.0 |
| d997714c-9994-3bd3-9d0d-f93997c25d5b | -3.28128 | -41.09248 | 2025-10-28 04:42:00 | NPP-375D | GRANJA | CEARÁ | Brasil | 2304707 | 23 | 33 | nan | nan | nan | Caatinga | 1.0 |
| f75d758e-cb96-3a22-b57b-8fc2ec88c018 | -3.36881 | -50.17615 | 2025-10-28 04:42:00 | NPP-375D | PACAJÁ | PARÁ | Brasil | 1505486 | 15 | 33 | nan | nan | nan | Amazônia | 1.1 |
| 8eac20ac-eff0-39db-8d59-5edc6cd04939 | -4.92694 | -48.6261 | 2025-10-28 04:42:00 | NPP-375D | BOM JESUS DO TOCANTINS | PARÁ | Brasil | 1501576 | 15 | 33 | nan | nan | nan | Amazônia | 1.5 |
| 1d9b699b-5dde-35e4-bc8b-fc9de5ffde11 | -3.60554 | -43.55614 | 2025-10-28 04:42:00 | NPP-375D | CHAPADINHA | MARANHÃO | Brasil | 2103208 | 21 | 33 | nan | nan | nan | Cerrado | 1.6 |
| 2ede41cb-5656-374f-9e3f-f4f5cb7b05f7 | -3.69782 | -49.56515 | 2025-10-28 04:42:00 | NPP-375D | BREU BRANCO | PARÁ | Brasil | 1501782 | 15 | 33 | nan | nan | nan | Amazônia | 1.5 |
| ca7844e1-f486-3cda-8cb3-40d62a770e7a | -2.95153 | -49.34812 | 2025-10-28 04:42:00 | NPP-375D | MOJU | PARÁ | Brasil | 1504703 | 15 | 33 | nan | nan | nan | Amazônia | 2.0 |
| 8601d4ac-75e1-3f0f-82fd-2f8d18f4af05 | -8.32207 | -46.16249 | 2025-10-28 04:42:00 | NPP-375D | BALSAS | MARANHÃO | Brasil | 2101400 | 21 | 33 | nan | nan | nan | Cerrado | 1.2 |
| d5d95610-cbab-361a-999f-7f8fa570a3b1 | -3.58098 | -43.63483 | 2025-10-28 04:42:00 | NPP-375D | NINA RODRIGUES | MARANHÃO | Brasil | 2107209 | 21 | 33 | nan | nan | nan | Cerrado | 6.3 |
| 19553dfd-1f94-355b-baac-cf8f23cc18dd | -7.3718 | -47.79053 | 2025-10-28 04:42:00 | NPP-375D | FILADÉLFIA | TOCANTINS | Brasil | 1707702 | 17 | 33 | nan | nan | nan | Cerrado | 2.9 |
| ee7a9ca6-42b5-3aa1-9acb-0eee767a3ea5 | -4.90518 | -48.56924 | 2025-10-28 04:42:00 | NPP-375D | BOM JESUS DO TOCANTINS | PARÁ | Brasil | 1501576 | 15 | 33 | nan | nan | nan | Amazônia | 0.8 |
| 4b2c1faa-9c8a-3c61-8863-9268fdf980d2 | -5.53532 | -48.98845 | 2025-10-28 04:42:00 | NPP-375D | MARABÁ | PARÁ | Brasil | 1504208 | 15 | 33 | nan | nan | nan | Amazônia | 0.8 |
| 4d0cd49d-97e8-3a9e-9d2f-c1b683cffba6 | -2.52818 | -44.07467 | 2025-10-28 04:42:00 | NPP-375D | PAÇO DO LUMIAR | MARANHÃO | Brasil | 2107506 | 21 | 33 | nan | nan | nan | Amazônia | 1.8 |
| 52475477-ef37-3a73-b78f-9d867aaca6c5 | -7.83881 | -46.40358 | 2025-10-28 04:42:00 | NPP-375D | BALSAS | MARANHÃO | Brasil | 2101400 | 21 | 33 | nan | nan | nan | Cerrado | 5.4 |
| a32b97ae-37d1-331c-a25e-c3c98cac4386 | -5.61708 | -51.78472 | 2025-10-28 04:42:00 | NPP-375D | SÃO FÉLIX DO XINGU | PARÁ | Brasil | 1507300 | 15 | 33 | nan | nan | nan | Amazônia | 0.8 |
| 8eef1b4b-d08d-3fdc-9b16-e42ee24fd6cf | -4.01644 | -48.98713 | 2025-10-28 04:42:00 | NPP-375D | GOIANÉSIA DO PARÁ | PARÁ | Brasil | 1503093 | 15 | 33 | nan | nan | nan | Amazônia | 0.5 |
| 98306020-134b-3503-b907-f154f769bc96 | -6.13444 | -41.70964 | 2025-10-28 04:42:00 | NPP-375D | AROAZES | PIAUÍ | Brasil | 2200905 | 22 | 33 | nan | nan | nan | Caatinga | 3.0 |
| 1a00a354-fed5-3314-8a24-f1d3d050bb52 | -1.67503 | -51.99688 | 2025-10-28 04:42:00 | NPP-375D | PORTO DE MOZ | PARÁ | Brasil | 1505908 | 15 | 33 | nan | nan | nan | Amazônia | 1.4 |
| 78beec78-0a97-306e-a1cc-9f19bf45f7be | -5.83763 | -47.65152 | 2025-10-28 04:42:00 | NPP-375D | ITAGUATINS | TOCANTINS | Brasil | 1710706 | 17 | 33 | nan | nan | nan | Cerrado | 1.1 |
| 1b67ad3d-9591-397e-9414-f32db898537d | -5.65646 | -47.82993 | 2025-10-28 04:42:00 | NPP-375D | AXIXÁ DO TOCANTINS | TOCANTINS | Brasil | 1702901 | 17 | 33 | nan | nan | nan | Cerrado | 1.3 |
| b1df78f5-cc1a-3d6e-9d01-831ba30fddc9 | -2.90361 | -53.13523 | 2025-10-28 04:42:00 | NPP-375D | MEDICILÂNDIA | PARÁ | Brasil | 1504455 | 15 | 33 | nan | nan | nan | Amazônia | 2.6 |
| 7258f9bd-ed28-3080-9b0a-d401f15380c5 | -5.70133 | -49.30914 | 2025-10-28 04:42:00 | NPP-375D | MARABÁ | PARÁ | Brasil | 1504208 | 15 | 33 | nan | nan | nan | Amazônia | 1.1 |
| c916c268-cd95-3cab-83f5-b3c797d70b22 | -3.59027 | -43.6289 | 2025-10-28 04:42:00 | NPP-375D | NINA RODRIGUES | MARANHÃO | Brasil | 2107209 | 21 | 33 | nan | nan | nan | Cerrado | 2.6 |
| ee0a1a53-ecd0-3958-bad7-124ac7f6e1bb | -7.81143 | -46.46076 | 2025-10-28 04:42:00 | NPP-375D | RIACHÃO | MARANHÃO | Brasil | 2109502 | 21 | 33 | nan | nan | nan | Cerrado | 10.6 |
| 66b6cfce-48e1-3426-9110-7de4f4ea54d3 | -7.99728 | -46.19295 | 2025-10-28 04:42:00 | NPP-375D | BALSAS | MARANHÃO | Brasil | 2101400 | 21 | 33 | nan | nan | nan | Cerrado | 3.9 |
| df029efd-ae82-358c-8e45-6bef2f965a43 | -3.57552 | -43.61532 | 2025-10-28 04:42:00 | NPP-375D | SÃO BENEDITO DO RIO PRETO | MARANHÃO | Brasil | 2110401 | 21 | 33 | nan | nan | nan | Cerrado | 1.7 |
| b8ca7ebc-a7db-336d-af17-6cf32f3e5f74 | -7.80904 | -46.45176 | 2025-10-28 04:42:00 | NPP-375D | RIACHÃO | MARANHÃO | Brasil | 2109502 | 21 | 33 | nan | nan | nan | Cerrado | 1.7 |
| 27ab03c2-d213-32d6-ab72-64573e608ed5 | -7.97653 | -46.72406 | 2025-10-28 04:42:00 | NPP-375D | CAMPOS LINDOS | TOCANTINS | Brasil | 1703842 | 17 | 33 | nan | nan | nan | Cerrado | 2.3 |
| eedc2557-6cdb-3059-8868-7b7f9955bd2e | -8.16171 | -42.82926 | 2025-10-28 04:42:00 | NPP-375D | BREJO DO PIAUÍ | PIAUÍ | Brasil | 2201988 | 22 | 33 | nan | nan | nan | Caatinga | 1.6 |
| 0e4450fb-e5c3-3d51-adbe-e98d461b9c80 | -4.90852 | -48.56976 | 2025-10-28 04:42:00 | NPP-375D | BOM JESUS DO TOCANTINS | PARÁ | Brasil | 1501576 | 15 | 33 | nan | nan | nan | Amazônia | 0.8 |
| 20a4dca8-3b6b-3e64-abcd-820a99e1fbdc | -5.58011 | -45.33702 | 2025-10-28 04:42:00 | NPP-375D | BARRA DO CORDA | MARANHÃO | Brasil | 2101608 | 21 | 33 | nan | nan | nan | Cerrado | 1.3 |
| 6fe904ae-a66e-38fd-adea-b876a3a5e2c5 | -8.65818 | -43.92523 | 2025-10-28 04:42:00 | NPP-375D | CRISTINO CASTRO | PIAUÍ | Brasil | 2203107 | 22 | 33 | nan | nan | nan | Cerrado | 0.9 |
| 6249e774-3fd0-3e59-9b3f-36fadefa01b4 | -4.63817 | -48.69506 | 2025-10-28 04:42:00 | NPP-375D | RONDON DO PARÁ | PARÁ | Brasil | 1506187 | 15 | 33 | nan | nan | nan | Amazônia | 0.9 |
| 4b687b87-eb32-3f94-98c9-86619b3d4b9d | -6.23993 | -42.56105 | 2025-10-28 04:42:00 | NPP-375D | REGENERAÇÃO | PIAUÍ | Brasil | 2208809 | 22 | 33 | nan | nan | nan | Caatinga | 1.9 |
| b26f59ed-e94b-3fa8-9c19-a243f7c6b607 | -6.87688 | -43.58443 | 2025-10-28 04:42:00 | NPP-375D | GUADALUPE | PIAUÍ | Brasil | 2204501 | 22 | 33 | nan | nan | nan | Cerrado | 0.8 |
| 5d0c5ed9-50cf-3645-b2bc-995d2ba89459 | -4.45849 | -43.23303 | 2025-10-28 04:42:00 | NPP-375D | ALDEIAS ALTAS | MARANHÃO | Brasil | 2100303 | 21 | 33 | nan | nan | nan | Cerrado | 20.3 |
| b2345da9-e9c5-3339-900a-e94d0d5d13d0 | -7.13272 | -46.9928 | 2025-10-28 04:42:00 | NPP-375D | CAROLINA | MARANHÃO | Brasil | 2102804 | 21 | 33 | nan | nan | nan | Cerrado | 1.1 |
| 47e3f692-7e66-33fb-a779-c90f13365c8f | -4.74008 | -48.30775 | 2025-10-28 04:42:00 | NPP-375D | RONDON DO PARÁ | PARÁ | Brasil | 1506187 | 15 | 33 | nan | nan | nan | Amazônia | 1.0 |
| 1dd62fa1-1e0c-33d6-8ed7-6a0fb3eb7319 | -7.41926 | -43.95394 | 2025-10-28 04:42:00 | NPP-375D | SEBASTIÃO LEAL | PIAUÍ | Brasil | 2210631 | 22 | 33 | nan | nan | nan | Cerrado | 0.9 |
| b4490a69-3371-3b47-bc83-9e7dd67c9ef1 | -3.48079 | -55.45594 | 2025-10-28 04:42:00 | NPP-375D | AVEIRO | PARÁ | Brasil | 1501006 | 15 | 33 | nan | nan | nan | Amazônia | 1.6 |
| d5e9a03c-5245-3b68-8b4f-50bf5fc31def | -3.43147 | -54.53669 | 2025-10-28 04:42:00 | NPP-375D | PLACAS | PARÁ | Brasil | 1505650 | 15 | 33 | nan | nan | nan | Amazônia | 0.8 |
| d2c0b448-5bce-3c39-a679-f1e1ea2b37c3 | -4.76697 | -49.53069 | 2025-10-28 04:42:00 | NPP-375D | NOVO REPARTIMENTO | PARÁ | Brasil | 1505064 | 15 | 33 | nan | nan | nan | Amazônia | 0.7 |


[Clique aqui para ver as próximas entradas](README49.md)
