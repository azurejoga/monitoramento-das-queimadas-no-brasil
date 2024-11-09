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

## Dados Diários - Página 8

| ID | Latitude | Longitude | Data/Hora GMT | Satélite | Município | Estado | País | Município ID | Estado ID | País ID | Dias sem Chuva | Precipitação | Risco de Fogo | Bioma | FRP |
|----|----------|-----------|---------------|----------|-----------|--------|------|--------------|-----------|---------|----------------|--------------|----------------|-------|-----|
| 85290404-8e6c-381b-aa2c-55f0b94616f0 | -1.52137 | -52.16496 | 2024-11-09 00:39:00 | TERRA_M-M | GURUPÁ | PARÁ | Brasil | 1503101 | 15 | 33 | nan | nan | nan | Amazônia | 17.7 |
| d62c729a-f431-3a26-8806-9fd8e075c7b3 | -2.87812 | -51.4636 | 2024-11-09 00:39:00 | TERRA_M-M | ANAPU | PARÁ | Brasil | 1500859 | 15 | 33 | nan | nan | nan | Amazônia | 13.2 |
| df8b46e8-0f7b-32f7-9b16-9cb0f856027b | -1.50327 | -47.18432 | 2024-11-09 00:39:00 | TERRA_M-M | OURÉM | PARÁ | Brasil | 1505403 | 15 | 33 | nan | nan | nan | Amazônia | 14.1 |
| 3de3618c-f9a7-38c8-8890-a3bf3eb5d02b | -2.72793 | -45.78803 | 2024-11-09 00:39:00 | TERRA_M-M | NOVA OLINDA DO MARANHÃO | MARANHÃO | Brasil | 2107357 | 21 | 33 | nan | nan | nan | Amazônia | 5.5 |
| f580211a-2e7c-3e9d-b233-3a11a304fa32 | -3.98577 | -46.42229 | 2024-11-09 00:39:00 | TERRA_M-M | BOM JARDIM | MARANHÃO | Brasil | 2102002 | 21 | 33 | nan | nan | nan | Amazônia | 17.9 |
| ff661028-78f8-3088-9e66-cfda2646ccd7 | -2.83629 | -48.46728 | 2024-11-09 00:39:00 | TERRA_M-M | TOMÉ-AÇU | PARÁ | Brasil | 1508001 | 15 | 33 | nan | nan | nan | Amazônia | 7.4 |
| 3bb5b73c-bac7-3e5e-8586-7af585aaad81 | -2.1953 | -49.29464 | 2024-11-09 00:39:00 | TERRA_M-M | CAMETÁ | PARÁ | Brasil | 1502103 | 15 | 33 | nan | nan | nan | Amazônia | 12.2 |
| 4c17a26a-3007-3144-98aa-717d9efca96b | -4.05686 | -46.93919 | 2024-11-09 00:39:00 | TERRA_M-M | ITINGA DO MARANHÃO | MARANHÃO | Brasil | 2105427 | 21 | 33 | nan | nan | nan | Amazônia | 20.8 |
| 2dcd3f83-9d42-33af-bb7e-e695c7b8a296 | -1.5159 | -52.1945 | 2024-11-09 00:39:00 | TERRA_M-M | GURUPÁ | PARÁ | Brasil | 1503101 | 15 | 33 | nan | nan | nan | Amazônia | 23.4 |
| 1e8138f8-90d6-36b3-a344-480b2517e25c | -3.12889 | -45.95508 | 2024-11-09 00:39:00 | TERRA_M-M | ZÉ DOCA | MARANHÃO | Brasil | 2114007 | 21 | 33 | nan | nan | nan | Amazônia | 14.6 |
| a5e780bc-0a56-366f-9a26-81c208d26967 | -2.72835 | -51.71896 | 2024-11-09 00:39:00 | TERRA_M-M | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 13.0 |
| abef1dc6-cb5a-38ce-b30a-0b93459fbad3 | -5.27175 | -45.86406 | 2024-11-09 00:39:00 | TERRA_M-M | ITAIPAVA DO GRAJAÚ | MARANHÃO | Brasil | 2105351 | 21 | 33 | nan | nan | nan | Cerrado | 5.1 |
| 133d6a79-419b-3072-b6c3-b5564738f817 | -2.79508 | -45.60931 | 2024-11-09 00:39:00 | TERRA_M-M | SANTA HELENA | MARANHÃO | Brasil | 2109809 | 21 | 33 | nan | nan | nan | Amazônia | 7.8 |
| 8cce83a6-2ca0-3cd1-b7f9-3dc5cd92f436 | -2.78581 | -49.65599 | 2024-11-09 00:39:00 | TERRA_M-M | BAIÃO | PARÁ | Brasil | 1501204 | 15 | 33 | nan | nan | nan | Amazônia | 13.9 |
| 999f8954-3cd8-384f-8d6e-6139bc108967 | -4.24278 | -46.01475 | 2024-11-09 00:39:00 | TERRA_M-M | SANTA LUZIA | MARANHÃO | Brasil | 2110005 | 21 | 33 | nan | nan | nan | Amazônia | 5.2 |
| 0ce1ba01-0eea-302e-97b5-5fe52f5bda95 | -5.2556 | -48.08154 | 2024-11-09 00:39:00 | TERRA_M-M | VILA NOVA DOS MARTÍRIOS | MARANHÃO | Brasil | 2112852 | 21 | 33 | nan | nan | nan | Amazônia | 8.5 |
| 51bd70e1-3e54-3eeb-868d-9cc78796224c | -2.20587 | -46.80257 | 2024-11-09 00:39:00 | TERRA_M-M | NOVA ESPERANÇA DO PIRIÁ | PARÁ | Brasil | 1504950 | 15 | 33 | nan | nan | nan | Amazônia | 4.8 |
| 9a54e940-305b-3c34-8b9c-9feca40d691a | -2.17323 | -46.43545 | 2024-11-09 00:39:00 | TERRA_M-M | CACHOEIRA DO PIRIÁ | PARÁ | Brasil | 1501956 | 15 | 33 | nan | nan | nan | Amazônia | 10.7 |
| b92fb897-b124-3e33-9e6d-3b85e8804d1e | -2.45151 | -46.31577 | 2024-11-09 00:39:00 | TERRA_M-M | CENTRO NOVO DO MARANHÃO | MARANHÃO | Brasil | 2103174 | 21 | 33 | nan | nan | nan | Amazônia | 15.4 |
| 068e430d-ee0e-3a38-8bb5-bc09d5db6596 | -2.51457 | -46.3726 | 2024-11-09 00:39:00 | TERRA_M-M | CENTRO NOVO DO MARANHÃO | MARANHÃO | Brasil | 2103174 | 21 | 33 | nan | nan | nan | Amazônia | 7.4 |
| f081d030-d2f7-3973-9ce3-7adea65756db | -2.16128 | -46.88646 | 2024-11-09 00:39:00 | TERRA_M-M | NOVA ESPERANÇA DO PIRIÁ | PARÁ | Brasil | 1504950 | 15 | 33 | nan | nan | nan | Amazônia | 10.0 |
| e4072ac1-de72-38b9-9e2b-f2c025264b06 | -7.04831 | -43.59053 | 2024-11-09 00:39:00 | TERRA_M-M | JERUMENHA | PIAUÍ | Brasil | 2205300 | 22 | 33 | nan | nan | nan | Cerrado | 4.5 |
| d9ace360-08d8-3d88-8e98-9e8e05f14dda | -2.54689 | -47.13097 | 2024-11-09 00:39:00 | TERRA_M-M | GARRAFÃO DO NORTE | PARÁ | Brasil | 1503077 | 15 | 33 | nan | nan | nan | Amazônia | 38.4 |
| 84e3d9a5-9a3d-36df-9798-bbadea51e884 | -6.33021 | -39.51315 | 2024-11-09 00:39:00 | TERRA_M-M | ACOPIARA | CEARÁ | Brasil | 2300309 | 23 | 33 | nan | nan | nan | Caatinga | 10.8 |
| 9fa376aa-71cc-306a-8b52-0e0541403383 | -4.835 | -45.63708 | 2024-11-09 00:39:00 | TERRA_M-M | MARAJÁ DO SENA | MARANHÃO | Brasil | 2106359 | 21 | 33 | nan | nan | nan | Amazônia | 11.1 |
| 8fdc732c-06d2-302f-9147-5fe47c0b4a82 | -2.58873 | -48.1601 | 2024-11-09 00:39:00 | TERRA_M-M | TOMÉ-AÇU | PARÁ | Brasil | 1508001 | 15 | 33 | nan | nan | nan | Amazônia | 6.1 |
| 2599418d-4a13-373f-891f-7fedb29d1769 | -3.97398 | -46.47259 | 2024-11-09 00:39:00 | TERRA_M-M | BOM JARDIM | MARANHÃO | Brasil | 2102002 | 21 | 33 | nan | nan | nan | Amazônia | 5.5 |
| 89aa15a4-7a48-3733-9b57-bda508206a54 | -5.45307 | -43.26106 | 2024-11-09 00:39:00 | TERRA_M-M | MATÕES | MARANHÃO | Brasil | 2106607 | 21 | 33 | nan | nan | nan | Cerrado | 10.4 |
| 1ce331cb-9c87-399b-87ea-d1f3c6e77b43 | -2.63647 | -46.78933 | 2024-11-09 00:39:00 | TERRA_M-M | PARAGOMINAS | PARÁ | Brasil | 1505502 | 15 | 33 | nan | nan | nan | Amazônia | 15.3 |
| e788b7cd-268d-3f6f-a960-864b4dea1709 | -5.13273 | -48.24169 | 2024-11-09 00:39:00 | TERRA_M-M | SÃO PEDRO DA ÁGUA BRANCA | MARANHÃO | Brasil | 2111532 | 21 | 33 | nan | nan | nan | Amazônia | 16.8 |
| 75295469-d712-31a6-ada1-e3558a977a62 | -2.62324 | -46.15834 | 2024-11-09 00:39:00 | TERRA_M-M | CENTRO DO GUILHERME | MARANHÃO | Brasil | 2103158 | 21 | 33 | nan | nan | nan | Amazônia | 15.8 |
| c88e2163-42e8-39a4-ae2a-e2736fc67ce0 | -6.06597 | -44.14886 | 2024-11-09 00:39:00 | TERRA_M-M | COLINAS | MARANHÃO | Brasil | 2103505 | 21 | 33 | nan | nan | nan | Cerrado | 17.1 |
| 93e3b0e7-534c-386b-8028-787807fbe495 | -2.02624 | -48.01555 | 2024-11-09 00:39:00 | TERRA_M-M | CONCÓRDIA DO PARÁ | PARÁ | Brasil | 1502756 | 15 | 33 | nan | nan | nan | Amazônia | 5.8 |
| d06968fe-52b2-3aab-9f72-b58ee3958a48 | -2.38623 | -46.77478 | 2024-11-09 00:39:00 | TERRA_M-M | NOVA ESPERANÇA DO PIRIÁ | PARÁ | Brasil | 1504950 | 15 | 33 | nan | nan | nan | Amazônia | 12.0 |
| 8daadbc7-8a2f-36df-8e52-29afe25bf318 | -2.40942 | -48.49041 | 2024-11-09 00:39:00 | TERRA_M-M | ACARÁ | PARÁ | Brasil | 1500206 | 15 | 33 | nan | nan | nan | Amazônia | 6.2 |
| 03aab485-842d-3f22-905f-23a34ad6b784 | -3.55528 | -47.37897 | 2024-11-09 00:39:00 | TERRA_M-M | ULIANÓPOLIS | PARÁ | Brasil | 1508126 | 15 | 33 | nan | nan | nan | Amazônia | 26.4 |
| c1b55c79-efa8-3619-bc04-ac8ded3922f7 | -4.42983 | -47.26097 | 2024-11-09 00:39:00 | TERRA_M-M | ITINGA DO MARANHÃO | MARANHÃO | Brasil | 2105427 | 21 | 33 | nan | nan | nan | Amazônia | 7.5 |
| a8efa549-d4e4-38be-9b48-ebf0c2f1687e | -3.53122 | -50.8692 | 2024-11-09 00:39:00 | TERRA_M-M | PACAJÁ | PARÁ | Brasil | 1505486 | 15 | 33 | nan | nan | nan | Amazônia | 38.0 |
| 319d68fe-641a-3a05-bce3-6a6beb464f64 | -5.3605 | -46.65688 | 2024-11-09 00:39:00 | TERRA_M-M | AMARANTE DO MARANHÃO | MARANHÃO | Brasil | 2100600 | 21 | 33 | nan | nan | nan | Cerrado | 7.3 |
| 41282218-3716-368f-bcbb-28d27ba56c57 | -4.40096 | -47.65631 | 2024-11-09 00:39:00 | TERRA_M-M | DOM ELISEU | PARÁ | Brasil | 1502939 | 15 | 33 | nan | nan | nan | Amazônia | 5.5 |
| 6bb25324-b557-3719-b97b-887cc134493b | -2.94437 | -52.69591 | 2024-11-09 00:39:00 | TERRA_M-M | BRASIL NOVO | PARÁ | Brasil | 1501725 | 15 | 33 | nan | nan | nan | Amazônia | 19.7 |
| 5f06f5f8-2291-3023-9261-668b4b67b0fb | -3.73333 | -44.34202 | 2024-11-09 00:39:00 | TERRA_M-M | MATÕES DO NORTE | MARANHÃO | Brasil | 2106631 | 21 | 33 | nan | nan | nan | Cerrado | 7.5 |
| 4d30171c-0f93-3e98-b83f-2b43f2095552 | -3.55059 | -43.55943 | 2024-11-09 00:39:00 | TERRA_M-M | CHAPADINHA | MARANHÃO | Brasil | 2103208 | 21 | 33 | nan | nan | nan | Cerrado | 13.8 |
| 72872f04-2790-3cea-b32e-e5f71157dc6c | -3.7087 | -44.89101 | 2024-11-09 00:39:00 | TERRA_M-M | VITÓRIA DO MEARIM | MARANHÃO | Brasil | 2112902 | 21 | 33 | nan | nan | nan | Amazônia | 7.6 |
| 36192c37-0c54-3dc2-90af-59571a288078 | -2.27894 | -48.72781 | 2024-11-09 00:39:00 | TERRA_M-M | ACARÁ | PARÁ | Brasil | 1500206 | 15 | 33 | nan | nan | nan | Amazônia | 5.5 |
| 26ae5e47-bb7b-3045-9741-d9a9afe89a93 | -5.57654 | -41.78794 | 2024-11-09 00:39:00 | TERRA_M-M | SÃO MIGUEL DO TAPUIO | PIAUÍ | Brasil | 2210409 | 22 | 33 | nan | nan | nan | Caatinga | 14.1 |
| d1f194b0-afd5-3b9f-a54d-11fb75aeadd4 | -3.23578 | -50.257 | 2024-11-09 00:39:00 | TERRA_M-M | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 14.3 |
| 5090fdfe-b84c-3fe2-b036-6a2c6c7f4fd5 | -2.33674 | -48.86391 | 2024-11-09 00:39:00 | TERRA_M-M | MOJU | PARÁ | Brasil | 1504703 | 15 | 33 | nan | nan | nan | Amazônia | 6.1 |
| e4e17689-c953-3a34-84c5-5ee14aabbf3f | -4.40887 | -43.37182 | 2024-11-09 00:39:00 | TERRA_M-M | ALDEIAS ALTAS | MARANHÃO | Brasil | 2100303 | 21 | 33 | nan | nan | nan | Cerrado | 6.8 |
| dc2464a2-531e-34c7-9914-07850573cb43 | -2.05757 | -50.75816 | 2024-11-09 00:39:00 | TERRA_M-M | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 11.8 |
| 85b0b939-76f9-322b-9c4a-7d95b95b4b7c | -3.15403 | -53.00142 | 2024-11-09 00:39:00 | TERRA_M-M | MEDICILÂNDIA | PARÁ | Brasil | 1504455 | 15 | 33 | nan | nan | nan | Amazônia | 45.5 |
| 7149f46a-fbef-3a31-b121-f578e8f7a1e2 | -4.60602 | -45.97725 | 2024-11-09 00:39:00 | TERRA_M-M | SANTA LUZIA | MARANHÃO | Brasil | 2110005 | 21 | 33 | nan | nan | nan | Amazônia | 5.7 |
| 2cb9e4af-6c69-35a7-a919-9a2bd6b60af8 | -3.18908 | -50.44957 | 2024-11-09 00:39:00 | TERRA_M-M | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 10.6 |
| dc0a69ec-3362-361c-b07b-e55947bb8281 | -3.36056 | -45.29718 | 2024-11-09 00:39:00 | TERRA_M-M | MONÇÃO | MARANHÃO | Brasil | 2106904 | 21 | 33 | nan | nan | nan | Amazônia | 9.0 |
| a2139675-57f4-35e2-a8f3-48bf8ea8cff9 | -6.92645 | -47.8384 | 2024-11-09 00:39:00 | TERRA_M-M | WANDERLÂNDIA | TOCANTINS | Brasil | 1722081 | 17 | 33 | nan | nan | nan | Cerrado | 10.1 |
| ec2e16e1-8536-3db4-af98-6303324fb01b | -2.37215 | -48.58587 | 2024-11-09 00:39:00 | TERRA_M-M | ACARÁ | PARÁ | Brasil | 1500206 | 15 | 33 | nan | nan | nan | Amazônia | 15.9 |
| c2c26334-7deb-3b1c-bd2d-59d159837ed2 | -4.19737 | -48.5628 | 2024-11-09 00:39:00 | TERRA_M-M | RONDON DO PARÁ | PARÁ | Brasil | 1506187 | 15 | 33 | nan | nan | nan | Amazônia | 5.7 |
| 06cda6ec-3679-31fd-8ac6-405c8a0db93f | -2.43419 | -46.2587 | 2024-11-09 00:39:00 | TERRA_M-M | CENTRO NOVO DO MARANHÃO | MARANHÃO | Brasil | 2103174 | 21 | 33 | nan | nan | nan | Amazônia | 4.8 |
| c83e98a9-4be0-36a3-a2ee-453727e312fd | -3.55321 | -43.57787 | 2024-11-09 00:39:00 | TERRA_M-M | SÃO BENEDITO DO RIO PRETO | MARANHÃO | Brasil | 2110401 | 21 | 33 | nan | nan | nan | Cerrado | 82.1 |
| 5d1ec05d-23c0-3e77-afd8-8110bd6512c8 | -4.8098 | -44.92291 | 2024-11-09 00:39:00 | TERRA_M-M | POÇÃO DE PEDRAS | MARANHÃO | Brasil | 2108900 | 21 | 33 | nan | nan | nan | Cerrado | 6.3 |
| 7acd7e85-ceb0-340a-b520-b7bc02b3eded | -2.67022 | -49.90245 | 2024-11-09 00:39:00 | TERRA_M-M | OEIRAS DO PARÁ | PARÁ | Brasil | 1505205 | 15 | 33 | nan | nan | nan | Amazônia | 13.3 |
| f750d9c4-75fd-3b76-b0e8-ff9207776763 | -2.28475 | -46.50772 | 2024-11-09 00:39:00 | TERRA_M-M | CACHOEIRA DO PIRIÁ | PARÁ | Brasil | 1501956 | 15 | 33 | nan | nan | nan | Amazônia | 12.9 |
| 36e06cbf-827e-3e86-bc11-dff46babcf16 | -3.94839 | -48.16224 | 2024-11-09 00:39:00 | TERRA_M-M | DOM ELISEU | PARÁ | Brasil | 1502939 | 15 | 33 | nan | nan | nan | Amazônia | 34.7 |
| 82542ac7-0b9a-39b5-9387-8cffe2b9b9d7 | -4.85105 | -48.6406 | 2024-11-09 00:39:00 | TERRA_M-M | BOM JESUS DO TOCANTINS | PARÁ | Brasil | 1501576 | 15 | 33 | nan | nan | nan | Amazônia | 8.4 |
| 97e6b292-c19b-37b7-8abc-3e40a390e901 | -2.3186 | -46.48764 | 2024-11-09 00:39:00 | TERRA_M-M | CACHOEIRA DO PIRIÁ | PARÁ | Brasil | 1501956 | 15 | 33 | nan | nan | nan | Amazônia | 12.8 |
| 3229f8dc-c664-387d-8c35-5d83f04ef8cd | -2.6077 | -45.84778 | 2024-11-09 00:39:00 | TERRA_M-M | SANTA LUZIA DO PARUÁ | MARANHÃO | Brasil | 2110039 | 21 | 33 | nan | nan | nan | Amazônia | 5.5 |
| 3623948a-1e4a-30f0-b850-073e03030854 | -2.52365 | -46.30565 | 2024-11-09 00:39:00 | TERRA_M-M | CENTRO NOVO DO MARANHÃO | MARANHÃO | Brasil | 2103174 | 21 | 33 | nan | nan | nan | Amazônia | 5.3 |
| f91f3cdb-2966-3b04-8b41-248370e281ee | -4.15642 | -44.39548 | 2024-11-09 00:39:00 | TERRA_M-M | ALTO ALEGRE DO MARANHÃO | MARANHÃO | Brasil | 2100436 | 21 | 33 | nan | nan | nan | Cerrado | 6.9 |
| 54ec4d9f-7310-3fac-bff9-a4cb27ba6645 | -4.80783 | -44.77911 | 2024-11-09 00:39:00 | TERRA_M-M | POÇÃO DE PEDRAS | MARANHÃO | Brasil | 2108900 | 21 | 33 | nan | nan | nan | Cerrado | 6.0 |
| 37fd28fd-a8bd-3257-8fe2-a3407145c7c2 | -4.12877 | -46.8618 | 2024-11-09 00:39:00 | TERRA_M-M | BOM JARDIM | MARANHÃO | Brasil | 2102002 | 21 | 33 | nan | nan | nan | Amazônia | 10.8 |
| ee7ea017-91f0-39c1-bebb-ab41fe7976f7 | -1.9528 | -46.50666 | 2024-11-09 00:39:00 | TERRA_M-M | CACHOEIRA DO PIRIÁ | PARÁ | Brasil | 1501956 | 15 | 33 | nan | nan | nan | Amazônia | 5.4 |
| 0061c967-e0a9-3c3d-903b-34a9c57be2b3 | -1.14577 | -53.6558 | 2024-11-09 00:39:00 | TERRA_M-M | PRAINHA | PARÁ | Brasil | 1506005 | 15 | 33 | nan | nan | nan | Amazônia | 45.5 |
| d9c0d960-f23b-3ff2-8589-c7cacefcfe5d | -4.65666 | -43.82498 | 2024-11-09 00:39:00 | TERRA_M-M | CODÓ | MARANHÃO | Brasil | 2103307 | 21 | 33 | nan | nan | nan | Cerrado | 8.2 |
| 5e87892e-eb53-3cd0-991d-dff24e871c85 | -5.97875 | -43.26664 | 2024-11-09 00:39:00 | TERRA_M-M | SÃO FRANCISCO DO MARANHÃO | MARANHÃO | Brasil | 2110906 | 21 | 33 | nan | nan | nan | Caatinga | 5.4 |
| 92520b65-b1e2-37c9-8ab3-6bc617dd8f17 | -3.2396 | -46.48847 | 2024-11-09 00:39:00 | TERRA_M-M | CENTRO NOVO DO MARANHÃO | MARANHÃO | Brasil | 2103174 | 21 | 33 | nan | nan | nan | Amazônia | 5.3 |
| df314d19-eff1-3e3d-8c32-6578168bd7c3 | -2.00062 | -46.85305 | 2024-11-09 00:39:00 | TERRA_M-M | SANTA LUZIA DO PARÁ | PARÁ | Brasil | 1506559 | 15 | 33 | nan | nan | nan | Amazônia | 7.4 |
| fe7b86dc-1d30-377d-bd1f-04e8d9cc0900 | -3.96013 | -48.17252 | 2024-11-09 00:39:00 | TERRA_M-M | DOM ELISEU | PARÁ | Brasil | 1502939 | 15 | 33 | nan | nan | nan | Amazônia | 86.2 |
| a58a6e1a-9d8a-3816-9dc7-87c7b839862a | -2.54231 | -46.30608 | 2024-11-09 00:39:00 | TERRA_M-M | CENTRO NOVO DO MARANHÃO | MARANHÃO | Brasil | 2103174 | 21 | 33 | nan | nan | nan | Amazônia | 8.3 |
| 3a9a6a9c-4b74-3269-8c16-18c3a03f4b92 | -3.58112 | -47.3541 | 2024-11-09 00:39:00 | TERRA_M-M | ULIANÓPOLIS | PARÁ | Brasil | 1508126 | 15 | 33 | nan | nan | nan | Amazônia | 49.8 |
| 55e50752-3086-3a7f-a9f6-f02e91f050bf | -2.62597 | -46.78108 | 2024-11-09 00:39:00 | TERRA_M-M | PARAGOMINAS | PARÁ | Brasil | 1505502 | 15 | 33 | nan | nan | nan | Amazônia | 11.0 |
| badb1385-39db-38e0-a705-84c411c429e5 | -2.71272 | -47.72892 | 2024-11-09 00:39:00 | TERRA_M-M | PARAGOMINAS | PARÁ | Brasil | 1505502 | 15 | 33 | nan | nan | nan | Amazônia | 18.1 |
| f8f54253-5f61-374b-8b74-aaf021517cf8 | -2.40724 | -46.79129 | 2024-11-09 00:39:00 | TERRA_M-M | NOVA ESPERANÇA DO PIRIÁ | PARÁ | Brasil | 1504950 | 15 | 33 | nan | nan | nan | Amazônia | 6.1 |
| 9156b2ae-8d27-3cc8-8b3b-0b53e9737ad3 | -4.39947 | -47.64524 | 2024-11-09 00:39:00 | TERRA_M-M | DOM ELISEU | PARÁ | Brasil | 1502939 | 15 | 33 | nan | nan | nan | Amazônia | 17.8 |
| 06815f3d-a344-38f5-ae30-809b61c6352c | -1.50798 | -52.16681 | 2024-11-09 00:39:00 | TERRA_M-M | GURUPÁ | PARÁ | Brasil | 1503101 | 15 | 33 | nan | nan | nan | Amazônia | 58.4 |
| ed90717e-f20c-3327-9a74-060a1b89adbe | -2.66961 | -49.89365 | 2024-11-09 00:39:00 | TERRA_M-M | OEIRAS DO PARÁ | PARÁ | Brasil | 1505205 | 15 | 33 | nan | nan | nan | Amazônia | 17.3 |
| 5adce5d6-a8ed-3203-9854-37ef0a11a60d | -6.22972 | -47.28442 | 2024-11-09 00:39:00 | TERRA_M-M | CAMPESTRE DO MARANHÃO | MARANHÃO | Brasil | 2102556 | 21 | 33 | nan | nan | nan | Cerrado | 14.8 |
| 3f325065-f081-33f2-989b-56413708b14d | -2.43292 | -46.24959 | 2024-11-09 00:39:00 | TERRA_M-M | CENTRO NOVO DO MARANHÃO | MARANHÃO | Brasil | 2103174 | 21 | 33 | nan | nan | nan | Amazônia | 4.6 |
| e0414da0-6558-3eed-9ee0-d08e999ffee5 | -4.7331 | -43.25347 | 2024-11-09 00:39:00 | TERRA_M-M | CAXIAS | MARANHÃO | Brasil | 2103000 | 21 | 33 | nan | nan | nan | Cerrado | 6.6 |
| e168aab4-f867-36d1-acab-829b896ae751 | -2.71421 | -47.73958 | 2024-11-09 00:39:00 | TERRA_M-M | PARAGOMINAS | PARÁ | Brasil | 1505502 | 15 | 33 | nan | nan | nan | Amazônia | 5.6 |
| 7d227be1-d5fd-3388-955e-1374dec1cb32 | -3.00358 | -49.23751 | 2024-11-09 00:39:00 | TERRA_M-M | MOJU | PARÁ | Brasil | 1504703 | 15 | 33 | nan | nan | nan | Amazônia | 13.7 |
| 82c5999f-d4b7-3a69-b357-10285a5c959f | -2.49238 | -47.21963 | 2024-11-09 00:39:00 | TERRA_M-M | CAPITÃO POÇO | PARÁ | Brasil | 1502301 | 15 | 33 | nan | nan | nan | Amazônia | 4.4 |
| 1d0dc280-c452-3e1f-9870-a6bc87daece3 | -2.92278 | -51.68686 | 2024-11-09 00:39:00 | TERRA_M-M | SENADOR JOSÉ PORFÍRIO | PARÁ | Brasil | 1507805 | 15 | 33 | nan | nan | nan | Amazônia | 14.4 |
| c5bc662e-b93a-32c3-a42f-974a780abd1d | -4.2669 | -46.91852 | 2024-11-09 00:39:00 | TERRA_M-M | BOM JARDIM | MARANHÃO | Brasil | 2102002 | 21 | 33 | nan | nan | nan | Amazônia | 6.7 |
| 28676013-405a-3053-9c37-07df5cf8af15 | -3.45133 | -52.72016 | 2024-11-09 00:39:00 | TERRA_M-M | MEDICILÂNDIA | PARÁ | Brasil | 1504455 | 15 | 33 | nan | nan | nan | Amazônia | 83.4 |
| 839b7c19-a753-3602-bc80-b46cff213cf7 | -5.14376 | -47.71231 | 2024-11-09 00:39:00 | TERRA_M-M | CIDELÂNDIA | MARANHÃO | Brasil | 2103257 | 21 | 33 | nan | nan | nan | Amazônia | 14.2 |
| d7f039f1-0263-32a1-938b-c15bb8d30ed8 | -3.23919 | -50.45964 | 2024-11-09 00:39:00 | TERRA_M-M | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 9.9 |
| f48785cf-8adb-3996-a61d-4d6fb7ec06a4 | -4.183 | -49.97892 | 2024-11-09 00:39:00 | TERRA_M-M | NOVO REPARTIMENTO | PARÁ | Brasil | 1505064 | 15 | 33 | nan | nan | nan | Amazônia | 11.5 |
| 96054060-a20b-36af-b5ad-d9a9954c1b59 | -2.89202 | -51.75602 | 2024-11-09 00:39:00 | TERRA_M-M | SENADOR JOSÉ PORFÍRIO | PARÁ | Brasil | 1507805 | 15 | 33 | nan | nan | nan | Amazônia | 28.4 |
| 45450188-8cbd-33fe-bf50-85f75f637dd8 | -3.43721 | -50.30119 | 2024-11-09 00:39:00 | TERRA_M-M | PACAJÁ | PARÁ | Brasil | 1505486 | 15 | 33 | nan | nan | nan | Amazônia | 9.5 |
| 3ebd5343-c00a-37b9-8916-0768783f61b9 | -4.01825 | -46.191 | 2024-11-09 00:39:00 | TERRA_M-M | ALTO ALEGRE DO PINDARÉ | MARANHÃO | Brasil | 2100477 | 21 | 33 | nan | nan | nan | Amazônia | 7.4 |


[Clique aqui para ver as próximas entradas](README9.md)
