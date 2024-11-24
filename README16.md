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

## Dados Diários - Página 16

| ID | Latitude | Longitude | Data/Hora GMT | Satélite | Município | Estado | País | Município ID | Estado ID | País ID | Dias sem Chuva | Precipitação | Risco de Fogo | Bioma | FRP |
|----|----------|-----------|---------------|----------|-----------|--------|------|--------------|-----------|---------|----------------|--------------|----------------|-------|-----|
| 3d0907fa-6f13-3bb5-86d8-ba1dc38a7199 | -4.52893 | -46.4281 | 2024-11-24 00:49:00 | TERRA_M-M | BURITICUPU | MARANHÃO | Brasil | 2102325 | 21 | 33 | nan | nan | nan | Amazônia | 11.9 |
| eae434b3-772b-35f1-bede-f978083414c2 | -4.98732 | -44.29752 | 2024-11-24 00:49:00 | TERRA_M-M | GOVERNADOR ARCHER | MARANHÃO | Brasil | 2104503 | 21 | 33 | nan | nan | nan | Cerrado | 5.0 |
| 1a24865d-b8d0-3739-be93-ee4aeb6cfcc0 | -1.13074 | -48.35357 | 2024-11-24 00:49:00 | TERRA_M-M | BELÉM | PARÁ | Brasil | 1501402 | 15 | 33 | nan | nan | nan | Amazônia | 6.6 |
| 2a7a60ac-e982-3661-be60-66d4ba1b41c0 | -3.48347 | -48.24492 | 2024-11-24 00:49:00 | TERRA_M-M | PARAGOMINAS | PARÁ | Brasil | 1505502 | 15 | 33 | nan | nan | nan | Amazônia | 3.8 |
| 59c044b8-1260-3665-9094-79c7dd398b3e | -3.93357 | -44.4461 | 2024-11-24 00:49:00 | TERRA_M-M | SÃO MATEUS DO MARANHÃO | MARANHÃO | Brasil | 2111508 | 21 | 33 | nan | nan | nan | Cerrado | 6.6 |
| fd8d7a09-e7bf-396a-b675-d62ccaf8b8e7 | -3.86529 | -44.18729 | 2024-11-24 00:49:00 | TERRA_M-M | PIRAPEMAS | MARANHÃO | Brasil | 2108801 | 21 | 33 | nan | nan | nan | Cerrado | 5.5 |
| d4364ea9-e0ae-307f-80ea-f55f20ae9824 | -4.71171 | -45.44086 | 2024-11-24 00:49:00 | TERRA_M-M | MARAJÁ DO SENA | MARANHÃO | Brasil | 2106359 | 21 | 33 | nan | nan | nan | Cerrado | 16.1 |
| adbad670-fb14-3d33-b2e3-f287b0028dfc | -2.59604 | -45.59722 | 2024-11-24 00:49:00 | TERRA_M-M | SANTA LUZIA DO PARUÁ | MARANHÃO | Brasil | 2110039 | 21 | 33 | nan | nan | nan | Amazônia | 12.5 |
| 76fdc82b-9284-36fb-ab54-18e5272812fc | -1.42867 | -46.0584 | 2024-11-24 00:49:00 | TERRA_M-M | CARUTAPERA | MARANHÃO | Brasil | 2102903 | 21 | 33 | nan | nan | nan | Amazônia | 37.1 |
| 8566fed8-7add-3cd1-ab08-3dab34fc6d81 | -4.66079 | -46.05428 | 2024-11-24 00:49:00 | TERRA_M-M | SANTA LUZIA | MARANHÃO | Brasil | 2110005 | 21 | 33 | nan | nan | nan | Amazônia | 6.3 |
| 30ada104-229b-396d-acb1-ca96bf5818f0 | -1.16584 | -49.32779 | 2024-11-24 00:49:00 | TERRA_M-M | MUANÁ | PARÁ | Brasil | 1504901 | 15 | 33 | nan | nan | nan | Amazônia | 4.0 |
| cedd7364-35ee-350f-abe4-e7fc1cec2a23 | -2.18273 | -49.1595 | 2024-11-24 00:49:00 | TERRA_M-M | IGARAPÉ-MIRI | PARÁ | Brasil | 1503309 | 15 | 33 | nan | nan | nan | Amazônia | 5.1 |
| 0cccc43d-b30a-3abf-8354-d5c734bdcaba | -5.18854 | -46.13736 | 2024-11-24 00:49:00 | TERRA_M-M | ARAME | MARANHÃO | Brasil | 2100956 | 21 | 33 | nan | nan | nan | Amazônia | 3.5 |
| 2fcba999-1df5-3cad-9eee-67dd44be4866 | -1.19212 | -51.93075 | 2024-11-24 00:49:00 | TERRA_M-M | ALMEIRIM | PARÁ | Brasil | 1500503 | 15 | 33 | nan | nan | nan | Amazônia | 6.8 |
| 9d150ccc-6508-3c1f-82e7-4ff1e394ad96 | -1.86177 | -48.16846 | 2024-11-24 00:49:00 | TERRA_M-M | ACARÁ | PARÁ | Brasil | 1500206 | 15 | 33 | nan | nan | nan | Amazônia | 5.1 |
| 8aead0f2-7b07-37fa-8cf1-1657676a4752 | -2.74696 | -49.11072 | 2024-11-24 00:49:00 | TERRA_M-M | MOJU | PARÁ | Brasil | 1504703 | 15 | 33 | nan | nan | nan | Amazônia | 11.7 |
| b2b8e4fa-df27-38b5-9759-693d6429f180 | -2.45904 | -49.09332 | 2024-11-24 00:49:00 | TERRA_M-M | MOJU | PARÁ | Brasil | 1504703 | 15 | 33 | nan | nan | nan | Amazônia | 14.0 |
| 5ae830e4-224f-332c-89c9-4a003ec5d5cb | -2.65256 | -46.24969 | 2024-11-24 00:49:00 | TERRA_M-M | CENTRO NOVO DO MARANHÃO | MARANHÃO | Brasil | 2103174 | 21 | 33 | nan | nan | nan | Amazônia | 6.5 |
| fe01c4f2-173e-32fb-a05b-5969dbdb98bd | -4.61734 | -44.08028 | 2024-11-24 00:49:00 | TERRA_M-M | CODÓ | MARANHÃO | Brasil | 2103307 | 21 | 33 | nan | nan | nan | Cerrado | 6.0 |
| dc330ee1-d51f-327e-aba6-1bb4ebdd3961 | -3.17745 | -54.32033 | 2024-11-24 00:49:00 | TERRA_M-M | MOJUÍ DOS CAMPOS | PARÁ | Brasil | 1504752 | 15 | 33 | nan | nan | nan | Amazônia | 23.1 |
| 9ddec845-d863-3e01-ad6c-f4ee0a4db1f5 | -4.76818 | -44.78661 | 2024-11-24 00:49:00 | TERRA_M-M | POÇÃO DE PEDRAS | MARANHÃO | Brasil | 2108900 | 21 | 33 | nan | nan | nan | Cerrado | 11.3 |
| 6231ec0e-bd66-3d98-8802-dbbbf95db549 | -1.11093 | -53.40199 | 2024-11-24 00:49:00 | TERRA_M-M | ALMEIRIM | PARÁ | Brasil | 1500503 | 15 | 33 | nan | nan | nan | Amazônia | 17.5 |
| 29811895-7bb3-3669-860c-9d00b6126af5 | -0.35945 | -50.02736 | 2024-11-24 00:49:00 | TERRA_M-M | CHAVES | PARÁ | Brasil | 1502509 | 15 | 33 | nan | nan | nan | Amazônia | 6.2 |
| 33b964e7-a232-3e15-bc51-615ca2587334 | -2.69154 | -46.26627 | 2024-11-24 00:49:00 | TERRA_M-M | CENTRO NOVO DO MARANHÃO | MARANHÃO | Brasil | 2103174 | 21 | 33 | nan | nan | nan | Amazônia | 11.5 |
| 852720d8-92a9-3808-8343-3a8db91435e8 | -1.19213 | -51.77517 | 2024-11-24 00:49:00 | TERRA_M-M | GURUPÁ | PARÁ | Brasil | 1503101 | 15 | 33 | nan | nan | nan | Amazônia | 8.3 |
| 15e2d3fc-6a1a-3c3e-9c91-a3c6d0790341 | -2.35266 | -49.12357 | 2024-11-24 00:49:00 | TERRA_M-M | MOJU | PARÁ | Brasil | 1504703 | 15 | 33 | nan | nan | nan | Amazônia | 4.4 |
| 4498d321-6a30-30fd-a90b-e573bca845f4 | -2.17843 | -53.79026 | 2024-11-24 00:49:00 | TERRA_M-M | PRAINHA | PARÁ | Brasil | 1506005 | 15 | 33 | nan | nan | nan | Amazônia | 16.4 |
| 615ead34-e41e-3a53-ab64-39a9528d2f4e | -3.42056 | -50.37902 | 2024-11-24 00:49:00 | TERRA_M-M | PACAJÁ | PARÁ | Brasil | 1505486 | 15 | 33 | nan | nan | nan | Amazônia | 4.6 |
| 4a9bb84c-db78-3aa8-b034-37d9e2e700a8 | -2.711 | -46.27298 | 2024-11-24 00:49:00 | TERRA_M-M | CENTRO NOVO DO MARANHÃO | MARANHÃO | Brasil | 2103174 | 21 | 33 | nan | nan | nan | Amazônia | 42.8 |
| f7c5d59f-e8b8-3923-85d3-c90c4de77959 | -3.83566 | -44.04983 | 2024-11-24 00:49:00 | TERRA_M-M | PIRAPEMAS | MARANHÃO | Brasil | 2108801 | 21 | 33 | nan | nan | nan | Cerrado | 19.2 |
| 0ba5437a-6168-3f52-a408-2f2664562bd9 | -1.95461 | -46.85505 | 2024-11-24 00:49:00 | TERRA_M-M | SANTA LUZIA DO PARÁ | PARÁ | Brasil | 1506559 | 15 | 33 | nan | nan | nan | Amazônia | 5.0 |
| 88b59ab6-3771-3706-9ce3-862057d15ba5 | -1.27602 | -47.86568 | 2024-11-24 00:49:00 | TERRA_M-M | CASTANHAL | PARÁ | Brasil | 1502400 | 15 | 33 | nan | nan | nan | Amazônia | 43.4 |
| bfa1c815-dca8-3321-a807-3bcafb397244 | -2.15811 | -46.66615 | 2024-11-24 00:49:00 | TERRA_M-M | NOVA ESPERANÇA DO PIRIÁ | PARÁ | Brasil | 1504950 | 15 | 33 | nan | nan | nan | Amazônia | 8.7 |
| 446fd67e-d2d5-31a4-8aff-3786347a2505 | -4.9351 | -50.61819 | 2024-11-24 00:49:00 | TERRA_M-M | NOVO REPARTIMENTO | PARÁ | Brasil | 1505064 | 15 | 33 | nan | nan | nan | Amazônia | 9.7 |
| 640e59e5-08ff-317b-afe1-e3d28070f562 | -2.65649 | -46.60505 | 2024-11-24 00:49:00 | TERRA_M-M | CENTRO NOVO DO MARANHÃO | MARANHÃO | Brasil | 2103174 | 21 | 33 | nan | nan | nan | Amazônia | 5.2 |
| a1f8ba66-7fd6-3f2e-9ec1-5fa94ba6a7ce | -2.70443 | -46.22652 | 2024-11-24 00:49:00 | TERRA_M-M | CENTRO NOVO DO MARANHÃO | MARANHÃO | Brasil | 2103174 | 21 | 33 | nan | nan | nan | Amazônia | 4.3 |
| fc2d087f-9edc-3cf5-b726-2be3e5e6a44d | -2.53478 | -46.39517 | 2024-11-24 00:49:00 | TERRA_M-M | CENTRO NOVO DO MARANHÃO | MARANHÃO | Brasil | 2103174 | 21 | 33 | nan | nan | nan | Amazônia | 8.8 |
| 18c9b5d5-0157-3a9a-97dc-4befa9738632 | -3.23138 | -54.24108 | 2024-11-24 00:49:00 | TERRA_M-M | SANTARÉM | PARÁ | Brasil | 1506807 | 15 | 33 | nan | nan | nan | Amazônia | 19.0 |
| 7475787c-f0b8-30e8-be0b-8a95766406b4 | -2.07417 | -50.31343 | 2024-11-24 00:49:00 | TERRA_M-M | BAGRE | PARÁ | Brasil | 1501105 | 15 | 33 | nan | nan | nan | Amazônia | 5.6 |
| 5ae267fc-2675-35a9-bdd5-7590f9748ad8 | -4.48714 | -47.11124 | 2024-11-24 00:49:00 | TERRA_M-M | AÇAILÂNDIA | MARANHÃO | Brasil | 2100055 | 21 | 33 | nan | nan | nan | Amazônia | 5.6 |
| 43e8de6e-237d-311d-b227-df4263aa022c | -2.84312 | -46.68634 | 2024-11-24 00:49:00 | TERRA_M-M | PARAGOMINAS | PARÁ | Brasil | 1505502 | 15 | 33 | nan | nan | nan | Amazônia | 3.6 |
| 226d742c-1bce-3be1-8bf7-92292fa26758 | -2.25112 | -46.86801 | 2024-11-24 00:49:00 | TERRA_M-M | NOVA ESPERANÇA DO PIRIÁ | PARÁ | Brasil | 1504950 | 15 | 33 | nan | nan | nan | Amazônia | 6.1 |
| 09a84f64-424c-3315-a5af-bb187560b2ad | -3.70888 | -51.79891 | 2024-11-24 00:49:00 | TERRA_M-M | SENADOR JOSÉ PORFÍRIO | PARÁ | Brasil | 1507805 | 15 | 33 | nan | nan | nan | Amazônia | 11.5 |
| 55c4fd74-0bb8-3f77-868f-f5578eee7507 | -1.73512 | -52.71618 | 2024-11-24 00:49:00 | TERRA_M-M | PORTO DE MOZ | PARÁ | Brasil | 1505908 | 15 | 33 | nan | nan | nan | Amazônia | 13.9 |
| 430f706b-2005-3caf-8e5a-c25b096e7f77 | -4.41926 | -49.82999 | 2024-11-24 00:49:00 | TERRA_M-M | NOVO REPARTIMENTO | PARÁ | Brasil | 1505064 | 15 | 33 | nan | nan | nan | Amazônia | 5.4 |
| 25289cc6-9d08-324f-9064-5417aea8eae9 | -0.04773 | -50.82218 | 2024-11-24 00:49:00 | TERRA_M-M | AFUÁ | PARÁ | Brasil | 1500305 | 15 | 33 | nan | nan | nan | Amazônia | 6.3 |
| c86e6adb-1e30-341f-8c44-e7877be8e56d | -2.24011 | -46.46129 | 2024-11-24 00:49:00 | TERRA_M-M | CACHOEIRA DO PIRIÁ | PARÁ | Brasil | 1501956 | 15 | 33 | nan | nan | nan | Amazônia | 4.7 |
| fa2aca1b-720e-32c0-a610-bf7844455721 | -1.98611 | -46.42476 | 2024-11-24 00:49:00 | TERRA_M-M | CACHOEIRA DO PIRIÁ | PARÁ | Brasil | 1501956 | 15 | 33 | nan | nan | nan | Amazônia | 5.2 |
| 7d96c2e8-9a23-30ec-b46e-44a755318a54 | -4.44281 | -50.07631 | 2024-11-24 00:49:00 | TERRA_M-M | NOVO REPARTIMENTO | PARÁ | Brasil | 1505064 | 15 | 33 | nan | nan | nan | Amazônia | 5.1 |
| badd6123-8dc8-36a1-827a-e0880f8cc780 | -2.57829 | -49.22307 | 2024-11-24 00:49:00 | TERRA_M-M | MOJU | PARÁ | Brasil | 1504703 | 15 | 33 | nan | nan | nan | Amazônia | 9.1 |
| 6222d825-753a-34b5-8413-feb6320083a3 | -3.68362 | -50.12033 | 2024-11-24 00:49:00 | TERRA_M-M | PACAJÁ | PARÁ | Brasil | 1505486 | 15 | 33 | nan | nan | nan | Amazônia | 6.1 |
| bf743b4d-3fdb-3ad6-9d99-25c5ba8d23b1 | -3.78533 | -45.85501 | 2024-11-24 00:49:00 | TERRA_M-M | ALTO ALEGRE DO PINDARÉ | MARANHÃO | Brasil | 2100477 | 21 | 33 | nan | nan | nan | Amazônia | 3.8 |
| e0c6f2d2-47be-357a-a108-4c957cbb4a56 | -3.96377 | -46.72816 | 2024-11-24 00:49:00 | TERRA_M-M | BOM JARDIM | MARANHÃO | Brasil | 2102002 | 21 | 33 | nan | nan | nan | Amazônia | 5.6 |
| 048f390f-f30a-3af8-b9ec-e79b3bd181ba | -3.65198 | -45.69623 | 2024-11-24 00:49:00 | TERRA_M-M | ALTO ALEGRE DO PINDARÉ | MARANHÃO | Brasil | 2100477 | 21 | 33 | nan | nan | nan | Amazônia | 4.4 |
| 5af4517e-3478-3dd7-84b4-cf60aef9c59e | -3.59016 | -49.35656 | 2024-11-24 00:49:00 | TERRA_M-M | BREU BRANCO | PARÁ | Brasil | 1501782 | 15 | 33 | nan | nan | nan | Amazônia | 24.5 |
| 4d39c732-e1df-358d-9bed-f01b2f7114b1 | -1.7554 | -54.52514 | 2024-11-24 00:49:00 | TERRA_M-M | ALENQUER | PARÁ | Brasil | 1500404 | 15 | 33 | nan | nan | nan | Amazônia | 34.7 |
| 61009940-f9ab-33b5-9301-c22398e555e4 | -4.63893 | -46.87914 | 2024-11-24 00:49:00 | TERRA_M-M | BOM JESUS DAS SELVAS | MARANHÃO | Brasil | 2102036 | 21 | 33 | nan | nan | nan | Amazônia | 3.9 |
| 8ac808f8-8638-3391-9f8c-cef482432fda | -4.2118 | -50.40702 | 2024-11-24 00:49:00 | TERRA_M-M | NOVO REPARTIMENTO | PARÁ | Brasil | 1505064 | 15 | 33 | nan | nan | nan | Amazônia | 34.6 |
| fcf9bb50-d04f-3aba-94f3-7695db31ea3b | -2.59544 | -47.02925 | 2024-11-24 00:49:00 | TERRA_M-M | PARAGOMINAS | PARÁ | Brasil | 1505502 | 15 | 33 | nan | nan | nan | Amazônia | 5.4 |
| 4d6f1e17-f384-36a9-a487-7534d798e91c | -2.68043 | -45.65551 | 2024-11-24 00:49:00 | TERRA_M-M | NOVA OLINDA DO MARANHÃO | MARANHÃO | Brasil | 2107357 | 21 | 33 | nan | nan | nan | Amazônia | 10.5 |
| 3ec0b0e1-e328-36f2-b096-69b8aa43927c | -2.68239 | -46.26436 | 2024-11-24 00:49:00 | TERRA_M-M | CENTRO NOVO DO MARANHÃO | MARANHÃO | Brasil | 2103174 | 21 | 33 | nan | nan | nan | Amazônia | 4.2 |
| 9cc9e9c4-89c9-37a7-8fa4-aa2dc2722082 | -3.47429 | -43.88993 | 2024-11-24 00:49:00 | TERRA_M-M | NINA RODRIGUES | MARANHÃO | Brasil | 2107209 | 21 | 33 | nan | nan | nan | Cerrado | 8.3 |
| 8e18bd78-0875-3d6a-8992-dc52a1fdab13 | -2.59193 | -54.24371 | 2024-11-24 00:49:00 | TERRA_M-M | PRAINHA | PARÁ | Brasil | 1506005 | 15 | 33 | nan | nan | nan | Amazônia | 17.4 |
| db4d293a-8a18-3072-8b82-18493234b363 | -3.1113 | -45.78131 | 2024-11-24 00:49:00 | TERRA_M-M | ARAGUANÃ | MARANHÃO | Brasil | 2100873 | 21 | 33 | nan | nan | nan | Amazônia | 7.2 |
| eb776c5a-8914-3561-b96b-674d25f6dc1a | -4.08317 | -50.36845 | 2024-11-24 00:49:00 | TERRA_M-M | NOVO REPARTIMENTO | PARÁ | Brasil | 1505064 | 15 | 33 | nan | nan | nan | Amazônia | 18.4 |
| d402613b-bfc4-3310-97e5-b7e9e26bf9c3 | -2.6818 | -45.66532 | 2024-11-24 00:49:00 | TERRA_M-M | NOVA OLINDA DO MARANHÃO | MARANHÃO | Brasil | 2107357 | 21 | 33 | nan | nan | nan | Amazônia | 7.5 |
| c7082ff8-5809-30b6-ad88-e2bb56ed7cab | -4.23615 | -48.69438 | 2024-11-24 00:49:00 | TERRA_M-M | RONDON DO PARÁ | PARÁ | Brasil | 1506187 | 15 | 33 | nan | nan | nan | Amazônia | 10.4 |
| 1de38450-6ed9-3dc2-9c29-0f799a2de2c0 | -4.08409 | -46.14536 | 2024-11-24 00:49:00 | TERRA_M-M | ALTO ALEGRE DO PINDARÉ | MARANHÃO | Brasil | 2100477 | 21 | 33 | nan | nan | nan | Amazônia | 6.6 |
| abddc189-3fca-3296-a3d0-f345dca44786 | -2.10265 | -46.26923 | 2024-11-24 00:49:00 | TERRA_M-M | CACHOEIRA DO PIRIÁ | PARÁ | Brasil | 1501956 | 15 | 33 | nan | nan | nan | Amazônia | 7.8 |
| 23c9b6fa-6b52-3eb0-b6e5-543001c07d84 | -2.37087 | -50.3932 | 2024-11-24 00:49:00 | TERRA_M-M | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 12.1 |
| aa08728e-9884-3fde-b198-7304db7458e6 | -1.94775 | -49.52812 | 2024-11-24 00:49:00 | TERRA_M-M | LIMOEIRO DO AJURU | PARÁ | Brasil | 1504000 | 15 | 33 | nan | nan | nan | Amazônia | 15.3 |
| c5c45541-bff5-308d-af35-0ec768c64b78 | 0.00328 | -51.18811 | 2024-11-24 00:49:00 | TERRA_M-M | MACAPÁ | AMAPÁ | Brasil | 1600303 | 16 | 33 | nan | nan | nan | Amazônia | 6.1 |
| 69d4641a-39a5-34c7-8735-79c3b1cf3b27 | -3.17276 | -45.29419 | 2024-11-24 00:49:00 | TERRA_M-M | PENALVA | MARANHÃO | Brasil | 2108306 | 21 | 33 | nan | nan | nan | Amazônia | 10.8 |
| 0b9cb99a-e9cc-310a-a7a5-831d0c0f1587 | -3.17482 | -49.07804 | 2024-11-24 00:49:00 | TERRA_M-M | MOJU | PARÁ | Brasil | 1504703 | 15 | 33 | nan | nan | nan | Amazônia | 6.0 |
| b750da0a-6cc3-3925-a07c-828ad12be072 | -4.35647 | -45.26801 | 2024-11-24 00:49:00 | TERRA_M-M | VITORINO FREIRE | MARANHÃO | Brasil | 2113009 | 21 | 33 | nan | nan | nan | Amazônia | 4.8 |
| 2a5ad4a6-7b34-3a8c-9a6c-2ad59425d531 | -3.93444 | -45.02571 | 2024-11-24 00:49:00 | TERRA_M-M | PIO XII | MARANHÃO | Brasil | 2108702 | 21 | 33 | nan | nan | nan | Amazônia | 14.6 |
| e20c9ec9-037c-3bf8-be0d-7b3cf45589f8 | -1.42716 | -53.38517 | 2024-11-24 00:49:00 | TERRA_M-M | ALMEIRIM | PARÁ | Brasil | 1500503 | 15 | 33 | nan | nan | nan | Amazônia | 24.0 |
| fe7ec66c-607d-3388-8852-0d4d7bd5a4fc | -5.10699 | -49.1282 | 2024-11-24 00:49:00 | TERRA_M-M | MARABÁ | PARÁ | Brasil | 1504208 | 15 | 33 | nan | nan | nan | Amazônia | 7.0 |
| f99e1fae-81eb-3447-b64b-50d428bc38e3 | -2.22981 | -47.84068 | 2024-11-24 00:49:00 | TERRA_M-M | AURORA DO PARÁ | PARÁ | Brasil | 1500958 | 15 | 33 | nan | nan | nan | Amazônia | 3.9 |
| 76632028-c5b1-3c54-b5e5-1710d01bbd54 | -2.73155 | -46.08905 | 2024-11-24 00:49:00 | TERRA_M-M | CENTRO NOVO DO MARANHÃO | MARANHÃO | Brasil | 2103174 | 21 | 33 | nan | nan | nan | Amazônia | 4.9 |
| 27c2cb3b-b7cf-3297-a7db-631b89197d2f | -3.83633 | -46.01972 | 2024-11-24 00:49:00 | TERRA_M-M | ALTO ALEGRE DO PINDARÉ | MARANHÃO | Brasil | 2100477 | 21 | 33 | nan | nan | nan | Amazônia | 50.5 |
| d510c7ba-adaa-34d3-96a3-1a8c446f5ea3 | -3.13841 | -52.98418 | 2024-11-24 00:49:00 | TERRA_M-M | MEDICILÂNDIA | PARÁ | Brasil | 1504455 | 15 | 33 | nan | nan | nan | Amazônia | 23.5 |
| ff9b9eab-09bc-3bbb-8b90-040c20503e80 | -0.81609 | -51.49136 | 2024-11-24 00:49:00 | TERRA_M-M | GURUPÁ | PARÁ | Brasil | 1503101 | 15 | 33 | nan | nan | nan | Amazônia | 6.1 |
| 2b605542-f2d9-3ab3-99f9-928b46ab88c8 | -3.84416 | -44.04224 | 2024-11-24 00:49:00 | TERRA_M-M | COROATÁ | MARANHÃO | Brasil | 2103604 | 21 | 33 | nan | nan | nan | Cerrado | 13.7 |
| 81e40d72-7038-3c48-af52-93bc8c0b083a | -4.12017 | -48.51888 | 2024-11-24 00:49:00 | TERRA_M-M | RONDON DO PARÁ | PARÁ | Brasil | 1506187 | 15 | 33 | nan | nan | nan | Amazônia | 9.3 |
| ecb3681e-5221-3eac-a0a0-0226a1c52606 | -2.57493 | -51.8887 | 2024-11-24 00:49:00 | TERRA_M-M | SENADOR JOSÉ PORFÍRIO | PARÁ | Brasil | 1507805 | 15 | 33 | nan | nan | nan | Amazônia | 49.8 |
| 637cd856-f860-3c46-8205-5ed55c028d7a | -2.74043 | -49.13077 | 2024-11-24 00:49:00 | TERRA_M-M | MOJU | PARÁ | Brasil | 1504703 | 15 | 33 | nan | nan | nan | Amazônia | 6.0 |
| a5504999-9962-36c3-a516-729f50382069 | -2.37895 | -49.85142 | 2024-11-24 00:49:00 | TERRA_M-M | OEIRAS DO PARÁ | PARÁ | Brasil | 1505205 | 15 | 33 | nan | nan | nan | Amazônia | 6.5 |
| 530f5920-3060-3fd0-bc97-db7f5738cfe4 | -2.5478 | -46.55225 | 2024-11-24 00:49:00 | TERRA_M-M | PARAGOMINAS | PARÁ | Brasil | 1505502 | 15 | 33 | nan | nan | nan | Amazônia | 5.3 |
| 99585cbc-b0ba-303a-816a-538d38a4f14b | -0.88781 | -51.72156 | 2024-11-24 00:49:00 | TERRA_M-M | VITÓRIA DO JARI | AMAPÁ | Brasil | 1600808 | 16 | 33 | nan | nan | nan | Amazônia | 7.9 |
| 5fdd0ff0-b816-3e8d-ae65-2e43a1f54e38 | -1.34497 | -46.91014 | 2024-11-24 00:49:00 | TERRA_M-M | BRAGANÇA | PARÁ | Brasil | 1501709 | 15 | 33 | nan | nan | nan | Amazônia | 7.8 |
| e42b97e3-2810-3045-8abe-8c4150498080 | -4.30685 | -48.07386 | 2024-11-24 00:49:00 | TERRA_M-M | RONDON DO PARÁ | PARÁ | Brasil | 1506187 | 15 | 33 | nan | nan | nan | Amazônia | 5.1 |
| dcd006c8-5e30-3a4e-b422-d8c7664008a2 | -1.60823 | -46.88246 | 2024-11-24 00:49:00 | TERRA_M-M | SANTA LUZIA DO PARÁ | PARÁ | Brasil | 1506559 | 15 | 33 | nan | nan | nan | Amazônia | 17.3 |
| 3566abd8-32bf-32a9-94b6-851e18606108 | -2.07277 | -46.51617 | 2024-11-24 00:49:00 | TERRA_M-M | CACHOEIRA DO PIRIÁ | PARÁ | Brasil | 1501956 | 15 | 33 | nan | nan | nan | Amazônia | 13.9 |
| 5154a4a9-bdc2-300b-8bac-a4daa612a204 | -3.57911 | -41.94293 | 2024-11-24 00:49:00 | TERRA_M-M | JOAQUIM PIRES | PIAUÍ | Brasil | 2205409 | 22 | 33 | nan | nan | nan | Caatinga | 12.2 |
| 18372dfa-1af8-34ab-9a52-8e9e10c36d2a | -1.34623 | -46.91917 | 2024-11-24 00:49:00 | TERRA_M-M | BRAGANÇA | PARÁ | Brasil | 1501709 | 15 | 33 | nan | nan | nan | Amazônia | 6.8 |
| a92f65c4-615d-3964-bbc5-aa9200290854 | -4.44971 | -46.12483 | 2024-11-24 00:49:00 | TERRA_M-M | SANTA LUZIA | MARANHÃO | Brasil | 2110005 | 21 | 33 | nan | nan | nan | Amazônia | 4.2 |
| 53d4f2b3-3a99-3c4c-a72c-b1bc5bc50a3e | -2.54651 | -46.54313 | 2024-11-24 00:49:00 | TERRA_M-M | PARAGOMINAS | PARÁ | Brasil | 1505502 | 15 | 33 | nan | nan | nan | Amazônia | 4.8 |
| 17fcabb9-a431-3019-a7cd-c18b47a7afee | -3.28913 | -45.53549 | 2024-11-24 00:49:00 | TERRA_M-M | ZÉ DOCA | MARANHÃO | Brasil | 2114007 | 21 | 33 | nan | nan | nan | Amazônia | 4.9 |
| 8254d22c-d052-34b2-941c-e175fe18f2c0 | -1.73381 | -52.0522 | 2024-11-24 00:49:00 | TERRA_M-M | PORTO DE MOZ | PARÁ | Brasil | 1505908 | 15 | 33 | nan | nan | nan | Amazônia | 8.2 |


[Clique aqui para ver as próximas entradas](README17.md)
