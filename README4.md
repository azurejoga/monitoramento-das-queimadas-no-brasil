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
| 808ded1f-bee8-3d58-8bbf-1e9d36b3bfb7 | -7.71971 | -44.16628 | 2026-06-18 03:40:00 | NPP-375D | SEBASTIÃO LEAL | PIAUÍ | Brasil | 2210631 | 22 | 33 | nan | nan | nan | Cerrado | 4.7 |
| 72d58d5f-779d-3551-a94d-b1bb3af12e62 | -10.55073 | -46.23681 | 2026-06-18 03:40:00 | NPP-375D | MATEIROS | TOCANTINS | Brasil | 1712702 | 17 | 33 | nan | nan | nan | Cerrado | 1.0 |
| cff4ed9f-a0e4-39b1-a238-ce923f585a29 | -8.83485 | -44.7951 | 2026-06-18 03:40:00 | NPP-375D | CURRAIS | PIAUÍ | Brasil | 2203230 | 22 | 33 | nan | nan | nan | Cerrado | 2.4 |
| 9c9270e5-67f9-3dcc-b663-7148dc0423f1 | -5.29646 | -43.70239 | 2026-06-18 03:40:00 | NPP-375D | CAXIAS | MARANHÃO | Brasil | 2103000 | 21 | 33 | nan | nan | nan | Cerrado | 3.1 |
| dd091efb-af20-3bd5-bf33-58ba43220546 | -9.54204 | -40.33993 | 2026-06-18 03:40:00 | NPP-375D | JUAZEIRO | BAHIA | Brasil | 2918407 | 29 | 33 | nan | nan | nan | Caatinga | 9.3 |
| d7618be2-5cc8-3645-bc3f-8a7433748684 | -9.40965 | -36.86534 | 2026-06-18 03:40:00 | NPP-375D | CACIMBINHAS | ALAGOAS | Brasil | 2701209 | 27 | 33 | nan | nan | nan | Caatinga | 1.4 |
| 7a2e05c0-de7e-32bf-a12e-f961700f50e5 | -7.72063 | -44.16137 | 2026-06-18 03:40:00 | NPP-375D | SEBASTIÃO LEAL | PIAUÍ | Brasil | 2210631 | 22 | 33 | nan | nan | nan | Cerrado | 4.7 |
| c11793f8-66a9-3677-80dd-5d02ae0eacab | -9.5367 | -40.34533 | 2026-06-18 03:40:00 | NPP-375D | JUAZEIRO | BAHIA | Brasil | 2918407 | 29 | 33 | nan | nan | nan | Caatinga | 31.9 |
| 30b0a0ec-9e21-391e-baa6-7407c78b172b | -7.59815 | -46.47502 | 2026-06-18 03:40:00 | NPP-375D | RIACHÃO | MARANHÃO | Brasil | 2109502 | 21 | 33 | nan | nan | nan | Cerrado | 5.6 |
| 526979b7-ba8a-38d2-a406-853fadaac063 | -5.30173 | -43.69728 | 2026-06-18 03:40:00 | NPP-375D | MATÕES | MARANHÃO | Brasil | 2106607 | 21 | 33 | nan | nan | nan | Cerrado | 2.5 |
| ed1b24ba-163e-3d99-a1cc-80b987bb5570 | -6.28478 | -43.63423 | 2026-06-18 03:40:00 | NPP-375D | PASSAGEM FRANCA | MARANHÃO | Brasil | 2107902 | 21 | 33 | nan | nan | nan | Cerrado | 2.2 |
| 4204fe77-4d93-340e-a291-c1f081eab179 | -9.53642 | -40.34411 | 2026-06-18 03:40:00 | NPP-375D | JUAZEIRO | BAHIA | Brasil | 2918407 | 29 | 33 | nan | nan | nan | Caatinga | 49.9 |
| 63398e6e-34c4-3f62-b624-be4f8c325c94 | -10.55645 | -46.2354 | 2026-06-18 03:40:00 | NPP-375D | MATEIROS | TOCANTINS | Brasil | 1712702 | 17 | 33 | nan | nan | nan | Cerrado | 3.0 |
| 0ebd6798-f417-309f-bf83-5dd82bd6b929 | -5.80704 | -45.08361 | 2026-06-18 03:40:00 | NPP-375D | BARRA DO CORDA | MARANHÃO | Brasil | 2101608 | 21 | 33 | nan | nan | nan | Cerrado | 4.1 |
| ae59810d-4c7b-3ee9-aca0-efe2ff2e467a | -8.80185 | -46.63505 | 2026-06-18 03:40:00 | NPP-375D | BALSAS | MARANHÃO | Brasil | 2101400 | 21 | 33 | nan | nan | nan | Cerrado | 2.7 |
| fb69ec7a-ad64-3d86-bf47-ab9ffe7ed26e | -10.56313 | -46.23696 | 2026-06-18 03:40:00 | NPP-375D | MATEIROS | TOCANTINS | Brasil | 1712702 | 17 | 33 | nan | nan | nan | Cerrado | 1.9 |
| 522c9fa6-4d57-33ad-a007-a765e7f1cba7 | -10.47755 | -37.43439 | 2026-06-18 03:40:00 | NPP-375D | RIBEIRÓPOLIS | SERGIPE | Brasil | 2806008 | 28 | 33 | nan | nan | nan | Caatinga | 0.8 |
| 407d2849-27bd-343e-aa71-78cab21083ed | -9.53763 | -40.34028 | 2026-06-18 03:40:00 | NPP-375D | JUAZEIRO | BAHIA | Brasil | 2918407 | 29 | 33 | nan | nan | nan | Caatinga | 31.9 |
| edf539b8-c46b-3f05-90e2-970afafb56b2 | -6.39504 | -44.17616 | 2026-06-18 03:40:00 | NPP-375D | SUCUPIRA DO NORTE | MARANHÃO | Brasil | 2111904 | 21 | 33 | nan | nan | nan | Cerrado | 1.8 |
| a2e8a270-8d50-3427-8388-b2dfb336d25b | -11.94736 | -37.98277 | 2026-06-18 03:40:00 | NPP-375D | ENTRE RIOS | BAHIA | Brasil | 2910503 | 29 | 33 | nan | nan | nan | Mata Atlântica | 0.9 |
| 324860d5-0b18-3ebd-8246-375d497bcc0b | -5.80782 | -45.08499 | 2026-06-18 03:40:00 | NPP-375D | BARRA DO CORDA | MARANHÃO | Brasil | 2101608 | 21 | 33 | nan | nan | nan | Cerrado | 3.1 |
| ad16bb8f-3b4b-3686-9a49-79b842273811 | -5.29632 | -43.69106 | 2026-06-18 03:40:00 | NPP-375D | MATÕES | MARANHÃO | Brasil | 2106607 | 21 | 33 | nan | nan | nan | Cerrado | 2.5 |
| a0162440-515a-33ad-b800-460f063147e2 | -5.29737 | -43.69741 | 2026-06-18 03:40:00 | NPP-375D | MATÕES | MARANHÃO | Brasil | 2106607 | 21 | 33 | nan | nan | nan | Cerrado | 3.1 |
| be11b3f5-91e0-3c8e-8c68-311ca46e53df | -6.28972 | -43.6343 | 2026-06-18 03:40:00 | NPP-375D | PASSAGEM FRANCA | MARANHÃO | Brasil | 2107902 | 21 | 33 | nan | nan | nan | Cerrado | 1.5 |
| 4501b7ec-99ac-32c9-9b5b-f2a1b6fde063 | -5.29544 | -43.69605 | 2026-06-18 03:40:00 | NPP-375D | CAXIAS | MARANHÃO | Brasil | 2103000 | 21 | 33 | nan | nan | nan | Cerrado | 2.5 |
| 43108db8-67e3-310c-8fd4-43365dfc3a16 | -6.39411 | -44.18138 | 2026-06-18 03:40:00 | NPP-375D | SUCUPIRA DO NORTE | MARANHÃO | Brasil | 2111904 | 21 | 33 | nan | nan | nan | Cerrado | 4.7 |
| ac8cdbb4-4159-3634-a057-ad4c811bbf93 | -9.54114 | -40.34499 | 2026-06-18 03:40:00 | NPP-375D | JUAZEIRO | BAHIA | Brasil | 2918407 | 29 | 33 | nan | nan | nan | Caatinga | 49.9 |
| 1580fafd-17d5-33ca-b678-d6f993a094da | -5.29198 | -43.69129 | 2026-06-18 03:40:00 | NPP-375D | CAXIAS | MARANHÃO | Brasil | 2103000 | 21 | 33 | nan | nan | nan | Cerrado | 1.4 |
| eb9f192f-d0bc-33a7-82b4-80b839926d9d | -10.5587 | -46.23216 | 2026-06-18 03:40:00 | NPP-375D | MATEIROS | TOCANTINS | Brasil | 1712702 | 17 | 33 | nan | nan | nan | Cerrado | 3.0 |
| c085014c-4e7f-34dc-a92e-2713da3e1ba4 | -5.81012 | -45.07264 | 2026-06-18 03:40:00 | NPP-375D | BARRA DO CORDA | MARANHÃO | Brasil | 2101608 | 21 | 33 | nan | nan | nan | Cerrado | 2.4 |
| 004c4a61-6b1e-3373-862d-0be5de660033 | -8.90487 | -46.97151 | 2026-06-18 03:40:00 | NPP-375D | BALSAS | MARANHÃO | Brasil | 2101400 | 21 | 33 | nan | nan | nan | Cerrado | 2.1 |
| 18e47d88-7d01-35a7-862a-3df653a90ad0 | -5.52143 | -37.6226 | 2026-06-18 03:40:00 | NPP-375D | FELIPE GUERRA | RIO GRANDE DO NORTE | Brasil | 2403707 | 24 | 33 | nan | nan | nan | Caatinga | 1.5 |
| eb0d8b73-cb6c-3a09-a8f2-6dbaeecf0519 | -8.91194 | -46.97356 | 2026-06-18 03:40:00 | NPP-375D | RECURSOLÂNDIA | TOCANTINS | Brasil | 1718501 | 17 | 33 | nan | nan | nan | Cerrado | 2.2 |
| 858d8c3c-9eed-3055-8c6b-d620012c665e | -5.28989 | -43.95538 | 2026-06-18 03:40:00 | NPP-375D | SENADOR ALEXANDRE COSTA | MARANHÃO | Brasil | 2111748 | 21 | 33 | nan | nan | nan | Cerrado | 5.0 |
| 5e31b018-07f6-34ca-937f-3ae1ffd5b18d | -6.97452 | -42.88546 | 2026-06-18 03:40:00 | NPP-375D | FLORIANO | PIAUÍ | Brasil | 2203909 | 22 | 33 | nan | nan | nan | Caatinga | 1.9 |
| 7f5832d1-452c-375c-9265-498b93ccc53d | -5.29536 | -43.96173 | 2026-06-18 03:40:00 | NPP-375D | SENADOR ALEXANDRE COSTA | MARANHÃO | Brasil | 2111748 | 21 | 33 | nan | nan | nan | Cerrado | 5.7 |
| 9ac7e2c2-050c-3837-8ddf-b1a3a8c742b0 | -6.28344 | -43.63374 | 2026-06-18 03:40:00 | NPP-375D | PASSAGEM FRANCA | MARANHÃO | Brasil | 2107902 | 21 | 33 | nan | nan | nan | Cerrado | 1.5 |
| d5be4cd0-3ede-3e2a-93eb-df732e7b3de9 | -6.39611 | -44.17765 | 2026-06-18 03:40:00 | NPP-375D | SUCUPIRA DO NORTE | MARANHÃO | Brasil | 2111904 | 21 | 33 | nan | nan | nan | Cerrado | 2.9 |
| 78d3780d-583f-3715-a6c2-881c766fa1ea | -8.80047 | -46.64214 | 2026-06-18 03:40:00 | NPP-375D | BALSAS | MARANHÃO | Brasil | 2101400 | 21 | 33 | nan | nan | nan | Cerrado | 2.8 |
| ce91875f-caac-372d-9ab4-3611241c2f42 | -5.80897 | -45.07881 | 2026-06-18 03:40:00 | NPP-375D | BARRA DO CORDA | MARANHÃO | Brasil | 2101608 | 21 | 33 | nan | nan | nan | Cerrado | 3.1 |
| 7b55301c-7283-343b-96a1-009be60f8817 | -8.79682 | -46.63875 | 2026-06-18 03:40:00 | NPP-375D | BALSAS | MARANHÃO | Brasil | 2101400 | 21 | 33 | nan | nan | nan | Cerrado | 3.1 |
| 1bd2fb09-7e25-317a-b0d4-3c26a34c2957 | -5.30086 | -43.70227 | 2026-06-18 03:40:00 | NPP-375D | MATÕES | MARANHÃO | Brasil | 2106607 | 21 | 33 | nan | nan | nan | Cerrado | 2.3 |
| ee23d944-2ed0-3e25-bb75-57adc1ee4714 | -9.54234 | -40.34115 | 2026-06-18 03:40:00 | NPP-375D | JUAZEIRO | BAHIA | Brasil | 2918407 | 29 | 33 | nan | nan | nan | Caatinga | 31.9 |
| 7527750b-039a-360d-b42c-546e11285ebb | -5.29081 | -43.95027 | 2026-06-18 03:40:00 | NPP-375D | SENADOR ALEXANDRE COSTA | MARANHÃO | Brasil | 2111748 | 21 | 33 | nan | nan | nan | Cerrado | 5.0 |
| a0f39c92-384a-3736-9f19-f7b78ad2b3f9 | -9.54141 | -40.3462 | 2026-06-18 03:40:00 | NPP-375D | JUAZEIRO | BAHIA | Brasil | 2918407 | 29 | 33 | nan | nan | nan | Caatinga | 31.9 |
| 1631c78f-2b7c-3f1b-9abc-1b2da0668c2f | -7.71253 | -44.1701 | 2026-06-18 03:40:00 | NPP-375D | SEBASTIÃO LEAL | PIAUÍ | Brasil | 2210631 | 22 | 33 | nan | nan | nan | Cerrado | 2.4 |
| 56254efa-00e7-381a-a5f7-b731a4ca390c | -5.80816 | -45.07742 | 2026-06-18 03:40:00 | NPP-375D | BARRA DO CORDA | MARANHÃO | Brasil | 2101608 | 21 | 33 | nan | nan | nan | Cerrado | 2.2 |
| 3033d6ef-1f7d-3538-b659-92246ca3be86 | -8.90398 | -46.96978 | 2026-06-18 03:40:00 | NPP-375D | BALSAS | MARANHÃO | Brasil | 2101400 | 21 | 33 | nan | nan | nan | Cerrado | 1.3 |
| 600a40d6-e049-380e-8eb1-43581fd47485 | -7.59678 | -46.48208 | 2026-06-18 03:40:00 | NPP-375D | RIACHÃO | MARANHÃO | Brasil | 2109502 | 21 | 33 | nan | nan | nan | Cerrado | 5.6 |
| 9379d0b0-5afc-39b1-8607-58a5c4a1f6cc | -6.28399 | -43.63868 | 2026-06-18 03:40:00 | NPP-375D | PASSAGEM FRANCA | MARANHÃO | Brasil | 2107902 | 21 | 33 | nan | nan | nan | Cerrado | 4.3 |
| 24e8871e-58d3-3672-8428-958a7e502cc7 | -9.53732 | -40.33905 | 2026-06-18 03:40:00 | NPP-375D | JUAZEIRO | BAHIA | Brasil | 2918407 | 29 | 33 | nan | nan | nan | Caatinga | 9.3 |
| 60c8f575-d035-370f-8395-dd12add0ffc6 | -6.28264 | -43.63807 | 2026-06-18 03:40:00 | NPP-375D | PASSAGEM FRANCA | MARANHÃO | Brasil | 2107902 | 21 | 33 | nan | nan | nan | Cerrado | 2.3 |
| 5c33f7e2-99c0-33d6-a864-0b3c2bea48f3 | -5.29106 | -43.69628 | 2026-06-18 03:40:00 | NPP-375D | CAXIAS | MARANHÃO | Brasil | 2103000 | 21 | 33 | nan | nan | nan | Cerrado | 1.9 |
| 50bef72d-4a07-365d-9759-790fed2544a4 | -14.19777 | -42.75463 | 2026-06-18 03:42:00 | NPP-375D | GUANAMBI | BAHIA | Brasil | 2911709 | 29 | 33 | nan | nan | nan | Caatinga | 0.6 |
| 8b8e9588-5804-3f1e-9cbc-0fab8a8d3534 | -10.98481 | -47.75232 | 2026-06-18 03:42:00 | NPP-375D | SILVANÓPOLIS | TOCANTINS | Brasil | 1720655 | 17 | 33 | nan | nan | nan | Cerrado | 3.4 |
| 48c19e48-095b-37be-bf4c-bd8b71ca47aa | -15.76535 | -39.18189 | 2026-06-18 03:42:00 | NPP-375D | CANAVIEIRAS | BAHIA | Brasil | 2906303 | 29 | 33 | nan | nan | nan | Mata Atlântica | 1.1 |
| f021cdd0-6ed3-3c89-abe1-a61b5f56b317 | -17.31446 | -43.64461 | 2026-06-18 03:42:00 | NPP-375D | OLHOS-D'ÁGUA | MINAS GERAIS | Brasil | 3145455 | 31 | 33 | nan | nan | nan | Cerrado | 3.2 |
| 3ec340bc-05ca-3a21-8193-e265d3f1af40 | -11.25138 | -46.6384 | 2026-06-18 03:42:00 | NPP-375D | RIO DA CONCEIÇÃO | TOCANTINS | Brasil | 1718659 | 17 | 33 | nan | nan | nan | Cerrado | 3.5 |
| 4ab56063-af16-3e5a-9fb6-c20499624de9 | -17.31958 | -43.64555 | 2026-06-18 03:42:00 | NPP-375D | OLHOS-D'ÁGUA | MINAS GERAIS | Brasil | 3145455 | 31 | 33 | nan | nan | nan | Cerrado | 10.3 |
| c807663c-9ef4-30fb-984f-159674c3e378 | -11.24941 | -46.64432 | 2026-06-18 03:42:00 | NPP-375D | RIO DA CONCEIÇÃO | TOCANTINS | Brasil | 1718659 | 17 | 33 | nan | nan | nan | Cerrado | 2.1 |
| 7e9d408b-55c1-37a7-b136-e51fc71f10bf | -12.08785 | -44.97576 | 2026-06-18 03:42:00 | NPP-375D | BARREIRAS | BAHIA | Brasil | 2903201 | 29 | 33 | nan | nan | nan | Cerrado | 4.3 |
| 12312681-bab3-35ed-bd20-71c6d0c70577 | -16.02258 | -43.42268 | 2026-06-18 03:42:00 | NPP-375D | JANAÚBA | MINAS GERAIS | Brasil | 3135100 | 31 | 33 | nan | nan | nan | Cerrado | 5.7 |
| 73a10993-32b1-3099-b37a-9fe1a140025e | -11.25071 | -46.63789 | 2026-06-18 03:42:00 | NPP-375D | RIO DA CONCEIÇÃO | TOCANTINS | Brasil | 1718659 | 17 | 33 | nan | nan | nan | Cerrado | 2.1 |
| 6ab189ea-2008-38c0-bbe6-cecb6fca9fc9 | -17.31896 | -43.64859 | 2026-06-18 03:42:00 | NPP-375D | OLHOS-D'ÁGUA | MINAS GERAIS | Brasil | 3145455 | 31 | 33 | nan | nan | nan | Cerrado | 8.0 |
| 9ba6d8f7-2a76-3b4b-a995-38ca0406fc10 | -12.74466 | -46.32179 | 2026-06-18 03:42:00 | NPP-375D | AURORA DO TOCANTINS | TOCANTINS | Brasil | 1702703 | 17 | 33 | nan | nan | nan | Cerrado | 1.3 |
| 756f6d12-1f6f-303d-aad1-90497c396626 | -16.02771 | -43.42379 | 2026-06-18 03:42:00 | NPP-375D | JANAÚBA | MINAS GERAIS | Brasil | 3135100 | 31 | 33 | nan | nan | nan | Cerrado | 5.7 |
| baa7ced4-8589-3db1-8a96-ded33e36d727 | -16.50263 | -43.507 | 2026-06-18 03:42:00 | NPP-375D | FRANCISCO SÁ | MINAS GERAIS | Brasil | 3126703 | 31 | 33 | nan | nan | nan | Cerrado | 1.4 |
| 8e27fff7-b438-3999-81bd-5aba762a212d | -12.84159 | -44.37177 | 2026-06-18 03:42:00 | NPP-375D | BAIANÓPOLIS | BAHIA | Brasil | 2902500 | 29 | 33 | nan | nan | nan | Cerrado | 6.8 |
| b888d844-7ef9-39f7-a298-8a825de47df0 | -16.02706 | -43.427 | 2026-06-18 03:42:00 | NPP-375D | JANAÚBA | MINAS GERAIS | Brasil | 3135100 | 31 | 33 | nan | nan | nan | Cerrado | 7.8 |
| c304987d-716a-31ad-a9b4-93429c4bfd91 | -12.84074 | -44.37598 | 2026-06-18 03:42:00 | NPP-375D | BAIANÓPOLIS | BAHIA | Brasil | 2902500 | 29 | 33 | nan | nan | nan | Cerrado | 12.5 |
| e266f58b-2f11-3bee-ab9e-575ecdb7b109 | -12.83497 | -44.37476 | 2026-06-18 03:42:00 | NPP-375D | BAIANÓPOLIS | BAHIA | Brasil | 2902500 | 29 | 33 | nan | nan | nan | Cerrado | 26.0 |
| 2538a8f2-5bf4-30de-a5c4-b10cbb8d75c8 | -11.25004 | -46.64482 | 2026-06-18 03:42:00 | NPP-375D | RIO DA CONCEIÇÃO | TOCANTINS | Brasil | 1718659 | 17 | 33 | nan | nan | nan | Cerrado | 2.9 |
| 74eac761-1e8e-3e34-9401-d077465087c0 | -16.14326 | -43.59967 | 2026-06-18 03:42:00 | NPP-375D | CAPITÃO ENÉAS | MINAS GERAIS | Brasil | 3112703 | 31 | 33 | nan | nan | nan | Cerrado | 1.0 |
| 1b920505-6fd8-3eed-a9bb-1482cc68e910 | -15.79861 | -39.80232 | 2026-06-18 03:42:00 | NPP-375D | POTIRAGUÁ | BAHIA | Brasil | 2925402 | 29 | 33 | nan | nan | nan | Mata Atlântica | 0.6 |
| 1b56b418-aef8-31d9-a963-005e0f10b004 | -12.8358 | -44.37058 | 2026-06-18 03:42:00 | NPP-375D | BAIANÓPOLIS | BAHIA | Brasil | 2902500 | 29 | 33 | nan | nan | nan | Cerrado | 12.9 |
| c3836187-58c3-3fd9-baeb-214436c47024 | -10.9783 | -47.75042 | 2026-06-18 03:42:00 | NPP-375D | SILVANÓPOLIS | TOCANTINS | Brasil | 1720655 | 17 | 33 | nan | nan | nan | Cerrado | 1.5 |
| b3fb580e-bdeb-3237-a7d9-0cb46bfcdcb7 | -12.7459 | -46.31589 | 2026-06-18 03:42:00 | NPP-375D | AURORA DO TOCANTINS | TOCANTINS | Brasil | 1702703 | 17 | 33 | nan | nan | nan | Cerrado | 1.3 |
| 86eba967-a1c2-3aee-971a-5099650118dd | -10.97749 | -47.75112 | 2026-06-18 03:42:00 | NPP-375D | SILVANÓPOLIS | TOCANTINS | Brasil | 1720655 | 17 | 33 | nan | nan | nan | Cerrado | 1.4 |
| c53144e5-a2b4-3c41-be73-dc12cfd48e78 | -15.79452 | -39.80155 | 2026-06-18 03:42:00 | NPP-375D | POTIRAGUÁ | BAHIA | Brasil | 2925402 | 29 | 33 | nan | nan | nan | Mata Atlântica | 0.4 |
| eb12fafb-cb00-3853-afe0-124b4b04891b | -10.98565 | -47.75154 | 2026-06-18 03:42:00 | NPP-375D | SILVANÓPOLIS | TOCANTINS | Brasil | 1720655 | 17 | 33 | nan | nan | nan | Cerrado | 8.2 |
| 71c4dd71-12ec-3f53-9f35-1c1c2ccf4bfb | -10.99213 | -47.75357 | 2026-06-18 03:42:00 | NPP-375D | SILVANÓPOLIS | TOCANTINS | Brasil | 1720655 | 17 | 33 | nan | nan | nan | Cerrado | 3.4 |
| 3511a3ba-84ac-3e75-9dcc-663ec94f42d3 | -16.02193 | -43.42588 | 2026-06-18 03:42:00 | NPP-375D | JANAÚBA | MINAS GERAIS | Brasil | 3135100 | 31 | 33 | nan | nan | nan | Cerrado | 7.8 |
| f8748b2a-8879-31c5-8dac-f2529a07ce19 | -14.20286 | -42.75567 | 2026-06-18 03:42:00 | NPP-375D | GUANAMBI | BAHIA | Brasil | 2911709 | 29 | 33 | nan | nan | nan | Caatinga | 0.6 |
| e92f7a69-2f20-3ee2-9d6a-3cc032ac1f37 | -17.31383 | -43.64771 | 2026-06-18 03:42:00 | NPP-375D | OLHOS-D'ÁGUA | MINAS GERAIS | Brasil | 3145455 | 31 | 33 | nan | nan | nan | Cerrado | 3.5 |
| c98ae59d-0db1-3156-9dff-deb6e194f983 | -18.86199 | -41.979 | 2026-06-18 03:45:00 | NPP-375D | GOVERNADOR VALADARES | MINAS GERAIS | Brasil | 3127701 | 31 | 33 | nan | nan | nan | Mata Atlântica | 1.6 |
| adbd3587-78b1-3b27-8f8a-ffbc99f3e6ba | -17.79626 | -44.57937 | 2026-06-18 03:45:00 | NPP-375D | LASSANCE | MINAS GERAIS | Brasil | 3138104 | 31 | 33 | nan | nan | nan | Cerrado | 1.5 |
| c414553b-701b-3216-abb5-46f2f31f05ee | -17.7944 | -44.5796 | 2026-06-18 03:45:00 | NPP-375D | LASSANCE | MINAS GERAIS | Brasil | 3138104 | 31 | 33 | nan | nan | nan | Cerrado | 2.3 |
| b95eb7ac-b134-3231-bd0e-a3ac36889cea | -17.94577 | -44.4145 | 2026-06-18 03:45:00 | NPP-375D | LASSANCE | MINAS GERAIS | Brasil | 3138104 | 31 | 33 | nan | nan | nan | Cerrado | 0.6 |
| 7ac79ffb-d74b-302b-85a8-cc53e7343c0d | -17.9474 | -44.41498 | 2026-06-18 03:45:00 | NPP-375D | LASSANCE | MINAS GERAIS | Brasil | 3138104 | 31 | 33 | nan | nan | nan | Cerrado | 1.0 |
| 4d596136-f633-330f-89f3-d88642a96956 | -17.94653 | -44.41098 | 2026-06-18 03:45:00 | NPP-375D | LASSANCE | MINAS GERAIS | Brasil | 3138104 | 31 | 33 | nan | nan | nan | Cerrado | 0.6 |
| 231ac4d4-6340-3d9d-9b21-aa1cc974ea82 | -19.89343 | -40.28331 | 2026-06-18 03:45:00 | NPP-375D | ARACRUZ | ESPÍRITO SANTO | Brasil | 3200607 | 32 | 33 | nan | nan | nan | Mata Atlântica | 2.1 |
| 5d034df6-338e-3415-8812-c9598eb438e5 | -10.9164 | -56.8536 | 2026-06-18 03:50:00 | GOES-19 | JUARA | MATO GROSSO | Brasil | 5105101 | 51 | 33 | nan | nan | nan | Amazônia | 52.5 |
| a5d1b7f5-6efe-3912-be5d-1a285aade09c | -7.9187 | -48.24502 | 2026-06-18 03:57:00 | NOAA-20 | PALMEIRANTE | TOCANTINS | Brasil | 1715705 | 17 | 33 | nan | nan | nan | Cerrado | 0.9 |
| 3a0567de-c2f5-3c37-9e46-a11faf931d45 | -6.28633 | -43.63407 | 2026-06-18 03:57:00 | NOAA-20 | PASSAGEM FRANCA | MARANHÃO | Brasil | 2107902 | 21 | 33 | nan | nan | nan | Cerrado | 3.6 |
| 364caba5-61ad-3c1f-b658-f767f3eb477d | -6.15681 | -48.50251 | 2026-06-18 03:57:00 | NOAA-20 | SÃO GERALDO DO ARAGUAIA | PARÁ | Brasil | 1507458 | 15 | 33 | nan | nan | nan | Amazônia | 0.9 |
| 27f77667-7bd5-360c-bf16-c914b3b76cc1 | -7.92347 | -48.24947 | 2026-06-18 03:57:00 | NOAA-20 | PALMEIRANTE | TOCANTINS | Brasil | 1715705 | 17 | 33 | nan | nan | nan | Cerrado | 0.6 |
| 895e882c-ab66-3d3e-ae17-287e3029923d | -6.3989 | -44.17425 | 2026-06-18 03:57:00 | NOAA-20 | SUCUPIRA DO NORTE | MARANHÃO | Brasil | 2111904 | 21 | 33 | nan | nan | nan | Cerrado | 3.3 |
| b0173bf7-5672-38db-8e9c-f6c2460b8158 | -7.72102 | -44.1602 | 2026-06-18 03:57:00 | NOAA-20 | SEBASTIÃO LEAL | PIAUÍ | Brasil | 2210631 | 22 | 33 | nan | nan | nan | Cerrado | 5.5 |
| 72898eda-dedb-37b7-8e18-ecc21d73cde5 | -6.28693 | -43.63053 | 2026-06-18 03:57:00 | NOAA-20 | PASSAGEM FRANCA | MARANHÃO | Brasil | 2107902 | 21 | 33 | nan | nan | nan | Cerrado | 3.6 |
| 725ab7da-e989-334b-8e7f-ef00c10877fe | -7.91662 | -48.24747 | 2026-06-18 03:57:00 | NOAA-20 | PALMEIRANTE | TOCANTINS | Brasil | 1715705 | 17 | 33 | nan | nan | nan | Cerrado | 2.3 |


[Clique aqui para ver as próximas entradas](README5.md)
