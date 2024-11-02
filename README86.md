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

## Dados Diários - Página 86

| ID | Latitude | Longitude | Data/Hora GMT | Satélite | Município | Estado | País | Município ID | Estado ID | País ID | Dias sem Chuva | Precipitação | Risco de Fogo | Bioma | FRP |
|----|----------|-----------|---------------|----------|-----------|--------|------|--------------|-----------|---------|----------------|--------------|----------------|-------|-----|
| c9c4b016-4df0-30c0-923b-aa81027914f0 | -2.24522 | -52.84061 | 2024-11-02 05:27:00 | NPP-375D | PORTO DE MOZ | PARÁ | Brasil | 1505908 | 15 | 33 | nan | nan | nan | Amazônia | 0.5 |
| 1c406d59-6cab-3d42-8061-0dc171290f7b | -2.24477 | -52.84347 | 2024-11-02 05:27:00 | NPP-375D | PORTO DE MOZ | PARÁ | Brasil | 1505908 | 15 | 33 | nan | nan | nan | Amazônia | 0.5 |
| 8921f24a-aef7-312a-877f-b1bd399c1422 | -2.24323 | -52.84086 | 2024-11-02 05:27:00 | NPP-375D | PORTO DE MOZ | PARÁ | Brasil | 1505908 | 15 | 33 | nan | nan | nan | Amazônia | 1.1 |
| 269fa238-8718-380a-bc16-8969fa6b408b | -2.36736 | -52.01869 | 2024-11-02 05:27:00 | NPP-375D | PORTO DE MOZ | PARÁ | Brasil | 1505908 | 15 | 33 | nan | nan | nan | Amazônia | 1.1 |
| dc39f6e6-90b2-3237-87ed-e5e9f0bceb6f | -2.36684 | -52.02201 | 2024-11-02 05:27:00 | NPP-375D | PORTO DE MOZ | PARÁ | Brasil | 1505908 | 15 | 33 | nan | nan | nan | Amazônia | 1.4 |
| 6ea1ce94-1a02-35b4-9ab8-a98128992d18 | -4.28429 | -53.69441 | 2024-11-02 05:27:00 | NPP-375D | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 2.2 |
| 9e7ca15e-2d68-33a2-891e-8d23206277df | -4.10373 | -53.63665 | 2024-11-02 05:27:00 | NPP-375D | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | 2.1 |
| 6450417a-e7d3-3afb-a8af-088ae90be617 | -3.81394 | -52.34506 | 2024-11-02 05:27:00 | NPP-375D | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 1.8 |
| 6ec410b6-950d-3894-bb6d-ca4fa4bda75f | -3.81089 | -52.34431 | 2024-11-02 05:27:00 | NPP-375D | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 1.9 |
| 896acc8a-bb90-3343-a15e-156e90cfab06 | -3.71159 | -52.42057 | 2024-11-02 05:27:00 | NPP-375D | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 0.9 |
| c14712c6-452e-36a9-955d-9b508a7ea6d1 | -3.7111 | -52.42382 | 2024-11-02 05:27:00 | NPP-375D | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 1.2 |
| 78a0d1fd-b932-3f3e-84cb-dc90cb15f588 | -3.7106 | -52.42709 | 2024-11-02 05:27:00 | NPP-375D | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 1.2 |
| 65da3a24-8668-3421-ad0c-ec96bfcb0ca1 | -3.71008 | -52.42015 | 2024-11-02 05:27:00 | NPP-375D | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 0.9 |
| dcb66b81-783d-31da-89ec-7a6a1bf595d4 | -3.70961 | -52.42342 | 2024-11-02 05:27:00 | NPP-375D | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 1.7 |
| 2675bd6d-2461-3b72-804d-bd35c5355d02 | -3.70913 | -52.42673 | 2024-11-02 05:27:00 | NPP-375D | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 1.7 |
| d928af00-6e44-3e53-892d-3fb9d0275fae | -3.70629 | -52.41963 | 2024-11-02 05:27:00 | NPP-375D | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 0.9 |
| d3b9c8fb-7869-3334-8550-71076889b2ff | -3.7058 | -52.42288 | 2024-11-02 05:27:00 | NPP-375D | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 1.2 |
| b1a3269b-8114-39e2-b084-c6279a274131 | -3.70478 | -52.41922 | 2024-11-02 05:27:00 | NPP-375D | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 0.9 |
| e21a2a4a-94ef-3384-aaca-3cd4fa31c8b7 | -3.65625 | -53.63068 | 2024-11-02 05:27:00 | NPP-375D | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | 2.0 |
| 66b2e15c-042a-382b-af39-aef523fff1f1 | -3.65545 | -53.63612 | 2024-11-02 05:27:00 | NPP-375D | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | 2.0 |
| 47563649-dfea-3884-b9ba-b3e8655a5e98 | -2.16795 | -53.679 | 2024-11-02 05:27:00 | NPP-375D | PRAINHA | PARÁ | Brasil | 1506005 | 15 | 33 | nan | nan | nan | Amazônia | 1.8 |
| 7290feee-0240-3713-a046-e9273781b90b | -2.18797 | -53.739 | 2024-11-02 05:27:00 | NPP-375D | PRAINHA | PARÁ | Brasil | 1506005 | 15 | 33 | nan | nan | nan | Amazônia | 1.8 |
| 1e496af3-0fa4-3f10-8bc2-58a9e402a352 | -2.18324 | -53.7382 | 2024-11-02 05:27:00 | NPP-375D | PRAINHA | PARÁ | Brasil | 1506005 | 15 | 33 | nan | nan | nan | Amazônia | 1.4 |
| ac9d9e0c-6bae-3211-b6f5-9b668a3ccfcc | -2.17347 | -53.67474 | 2024-11-02 05:27:00 | NPP-375D | PRAINHA | PARÁ | Brasil | 1506005 | 15 | 33 | nan | nan | nan | Amazônia | 1.8 |
| 8324a175-7293-30f2-b8cb-dd7ec51e9ad5 | -2.17194 | -53.68481 | 2024-11-02 05:27:00 | NPP-375D | PRAINHA | PARÁ | Brasil | 1506005 | 15 | 33 | nan | nan | nan | Amazônia | 2.9 |
| 1915884b-9f68-3a44-86cf-652dd5d9da6d | -2.17117 | -53.68983 | 2024-11-02 05:27:00 | NPP-375D | PRAINHA | PARÁ | Brasil | 1506005 | 15 | 33 | nan | nan | nan | Amazônia | 2.9 |
| f8f9b812-b12f-33e7-8f27-56ea3959444a | -2.16871 | -53.67397 | 2024-11-02 05:27:00 | NPP-375D | PRAINHA | PARÁ | Brasil | 1506005 | 15 | 33 | nan | nan | nan | Amazônia | 1.8 |
| 54720c6f-e434-3ae8-ae17-5ef424f50f13 | -2.16718 | -53.68403 | 2024-11-02 05:27:00 | NPP-375D | PRAINHA | PARÁ | Brasil | 1506005 | 15 | 33 | nan | nan | nan | Amazônia | 2.9 |
| e7e0f765-e7c4-3a40-addf-7de1535e8efd | -2.16642 | -53.68905 | 2024-11-02 05:27:00 | NPP-375D | PRAINHA | PARÁ | Brasil | 1506005 | 15 | 33 | nan | nan | nan | Amazônia | 2.9 |
| 5b8df2e8-c091-383a-994f-810158c0ffd1 | -2.16395 | -53.67316 | 2024-11-02 05:27:00 | NPP-375D | PRAINHA | PARÁ | Brasil | 1506005 | 15 | 33 | nan | nan | nan | Amazônia | 3.3 |
| 355193f4-d99b-3edc-b3d4-ee9e12cfbdae | -2.1592 | -53.67233 | 2024-11-02 05:27:00 | NPP-375D | PRAINHA | PARÁ | Brasil | 1506005 | 15 | 33 | nan | nan | nan | Amazônia | 3.3 |
| d1b18e22-c9f1-3595-8b51-fb8824676bbd | -1.87075 | -54.68789 | 2024-11-02 05:27:00 | NPP-375D | ALENQUER | PARÁ | Brasil | 1500404 | 15 | 33 | nan | nan | nan | Amazônia | 2.5 |
| 1cce8c5b-4c1b-31c5-b70a-87562b88d126 | -1.86751 | -54.68488 | 2024-11-02 05:27:00 | NPP-375D | ALENQUER | PARÁ | Brasil | 1500404 | 15 | 33 | nan | nan | nan | Amazônia | 0.8 |
| e2b1d671-8ac0-336b-96f8-09486e8db354 | -1.82239 | -54.38541 | 2024-11-02 05:27:00 | NPP-375D | MONTE ALEGRE | PARÁ | Brasil | 1504802 | 15 | 33 | nan | nan | nan | Amazônia | 1.5 |
| 59c2e187-2960-38d7-bbfa-c67293bd584e | -1.97267 | -54.90101 | 2024-11-02 05:27:00 | NPP-375D | CURUÁ | PARÁ | Brasil | 1502855 | 15 | 33 | nan | nan | nan | Amazônia | 2.4 |
| 6bbdbc8e-8040-3617-8820-327cf0bf3399 | -1.86683 | -54.68916 | 2024-11-02 05:27:00 | NPP-375D | ALENQUER | PARÁ | Brasil | 1500404 | 15 | 33 | nan | nan | nan | Amazônia | 0.8 |
| caf4ac1e-5d5d-3dc5-881e-7dcb89742f3e | -1.82171 | -54.38992 | 2024-11-02 05:27:00 | NPP-375D | MONTE ALEGRE | PARÁ | Brasil | 1504802 | 15 | 33 | nan | nan | nan | Amazônia | 2.7 |
| 6c49302f-af51-35cb-b81e-991f61b4ad01 | -1.52508 | -54.2829 | 2024-11-02 05:27:00 | NPP-375D | MONTE ALEGRE | PARÁ | Brasil | 1504802 | 15 | 33 | nan | nan | nan | Amazônia | 3.3 |
| 31ad2752-02e3-31ee-ae62-b33a6af18762 | -1.52123 | -54.27777 | 2024-11-02 05:27:00 | NPP-375D | MONTE ALEGRE | PARÁ | Brasil | 1504802 | 15 | 33 | nan | nan | nan | Amazônia | 3.3 |
| 033b8836-c647-32ef-b1a4-a87f2b78a8d5 | -1.52056 | -54.28216 | 2024-11-02 05:27:00 | NPP-375D | MONTE ALEGRE | PARÁ | Brasil | 1504802 | 15 | 33 | nan | nan | nan | Amazônia | 3.3 |
| 126b4cad-e919-316d-a619-4615e48e3ed0 | -1.5198 | -54.49663 | 2024-11-02 05:27:00 | NPP-375D | ALENQUER | PARÁ | Brasil | 1500404 | 15 | 33 | nan | nan | nan | Amazônia | 1.6 |
| 4b8e36b8-7aa8-395b-b53d-0e746e0f97a4 | -1.51672 | -54.27698 | 2024-11-02 05:27:00 | NPP-375D | MONTE ALEGRE | PARÁ | Brasil | 1504802 | 15 | 33 | nan | nan | nan | Amazônia | 1.4 |
| 40727a9d-fa78-3dc9-a57b-a9731479fece | -1.45077 | -54.45176 | 2024-11-02 05:27:00 | NPP-375D | MONTE ALEGRE | PARÁ | Brasil | 1504802 | 15 | 33 | nan | nan | nan | Amazônia | 1.6 |
| b0667576-3b64-3496-be45-6ffceaaba15e | -1.41942 | -54.79285 | 2024-11-02 05:27:00 | NPP-375D | ALENQUER | PARÁ | Brasil | 1500404 | 15 | 33 | nan | nan | nan | Amazônia | 1.1 |
| 3510870a-dbf4-39f1-a1c6-7221f7e47fa6 | -1.34798 | -54.61727 | 2024-11-02 05:27:00 | NPP-375D | MONTE ALEGRE | PARÁ | Brasil | 1504802 | 15 | 33 | nan | nan | nan | Amazônia | 1.9 |
| aacc908c-0b3a-38ab-91d2-84c6a033bc24 | -1.34734 | -54.62148 | 2024-11-02 05:27:00 | NPP-375D | MONTE ALEGRE | PARÁ | Brasil | 1504802 | 15 | 33 | nan | nan | nan | Amazônia | 1.9 |
| ef8bb2da-0655-3a45-bb6b-df6824abf966 | -1.32837 | -54.63268 | 2024-11-02 05:27:00 | NPP-375D | MONTE ALEGRE | PARÁ | Brasil | 1504802 | 15 | 33 | nan | nan | nan | Amazônia | 0.7 |
| abef3761-b45d-3ff2-ae4a-f5a95ae8d6bf | -1.57786 | -54.75703 | 2024-11-02 05:27:00 | NPP-375D | ALENQUER | PARÁ | Brasil | 1500404 | 15 | 33 | nan | nan | nan | Amazônia | 3.1 |
| 5230a2d0-5bed-387a-b2a0-045bf234d0dc | -1.51467 | -54.29046 | 2024-11-02 05:27:00 | NPP-375D | MONTE ALEGRE | PARÁ | Brasil | 1504802 | 15 | 33 | nan | nan | nan | Amazônia | 1.1 |
| 95056b34-7123-353c-8d08-400ce9df5295 | -1.51013 | -54.2899 | 2024-11-02 05:27:00 | NPP-375D | MONTE ALEGRE | PARÁ | Brasil | 1504802 | 15 | 33 | nan | nan | nan | Amazônia | 1.1 |
| 724bd817-bf9f-3b6c-a397-5654d0fdc81c | -1.49661 | -53.5713 | 2024-11-02 05:27:00 | NPP-375D | PRAINHA | PARÁ | Brasil | 1506005 | 15 | 33 | nan | nan | nan | Amazônia | 0.9 |
| 7321cf2a-0de0-32a9-b79c-0df1eb583469 | -1.45828 | -54.28629 | 2024-11-02 05:27:00 | NPP-375D | MONTE ALEGRE | PARÁ | Brasil | 1504802 | 15 | 33 | nan | nan | nan | Amazônia | 1.5 |
| 8676cc11-9531-385c-9513-b5791fc84d0d | -1.41932 | -54.23862 | 2024-11-02 05:27:00 | NPP-375D | MONTE ALEGRE | PARÁ | Brasil | 1504802 | 15 | 33 | nan | nan | nan | Amazônia | 1.5 |
| 205e28f0-23a4-38a2-94be-216224cf47f0 | -1.4156 | -54.79459 | 2024-11-02 05:27:00 | NPP-375D | ALENQUER | PARÁ | Brasil | 1500404 | 15 | 33 | nan | nan | nan | Amazônia | 2.6 |
| eb6a0300-41d8-37f6-bd85-a475a6c28ea4 | -1.41509 | -54.79197 | 2024-11-02 05:27:00 | NPP-375D | ALENQUER | PARÁ | Brasil | 1500404 | 15 | 33 | nan | nan | nan | Amazônia | 1.1 |
| 397e902a-5b65-363d-a5f3-9e9e99de3983 | -1.40603 | -54.2039 | 2024-11-02 05:27:00 | NPP-375D | MONTE ALEGRE | PARÁ | Brasil | 1504802 | 15 | 33 | nan | nan | nan | Amazônia | 1.0 |
| ae18748b-e55e-381b-9fcc-339fe12411bf | -1.38981 | -54.12711 | 2024-11-02 05:27:00 | NPP-375D | MONTE ALEGRE | PARÁ | Brasil | 1504802 | 15 | 33 | nan | nan | nan | Amazônia | 2.4 |
| 998b01c0-3004-3a29-8444-fb5f224a0314 | -1.38523 | -54.12653 | 2024-11-02 05:27:00 | NPP-375D | MONTE ALEGRE | PARÁ | Brasil | 1504802 | 15 | 33 | nan | nan | nan | Amazônia | 2.4 |
| 2dd31c19-4d04-37dc-96ea-5f1b05bacdaf | -1.38064 | -54.126 | 2024-11-02 05:27:00 | NPP-375D | MONTE ALEGRE | PARÁ | Brasil | 1504802 | 15 | 33 | nan | nan | nan | Amazônia | 0.6 |
| 09e68eaf-af9b-3e1a-84e7-fd1d1288fa6e | -1.35175 | -54.62214 | 2024-11-02 05:27:00 | NPP-375D | MONTE ALEGRE | PARÁ | Brasil | 1504802 | 15 | 33 | nan | nan | nan | Amazônia | 2.0 |
| ca281d10-90c6-3369-a3ca-96ecc7ed043d | -1.34218 | -54.6555 | 2024-11-02 05:27:00 | NPP-375D | ALENQUER | PARÁ | Brasil | 1500404 | 15 | 33 | nan | nan | nan | Amazônia | 1.7 |
| a705da13-4d97-3a48-acd4-d414eb11d072 | -1.32769 | -54.63696 | 2024-11-02 05:27:00 | NPP-375D | MONTE ALEGRE | PARÁ | Brasil | 1504802 | 15 | 33 | nan | nan | nan | Amazônia | 0.7 |
| a7b1566d-e275-315d-8c86-9e926ccdc64a | -1.32714 | -54.63588 | 2024-11-02 05:27:00 | NPP-375D | MONTE ALEGRE | PARÁ | Brasil | 1504802 | 15 | 33 | nan | nan | nan | Amazônia | 1.1 |
| a4a761bc-dd64-3586-bfa4-d08b8760044a | -1.27402 | -53.37079 | 2024-11-02 05:27:00 | NPP-375D | ALMEIRIM | PARÁ | Brasil | 1500503 | 15 | 33 | nan | nan | nan | Amazônia | 1.5 |
| 4219e9b2-cb7f-3da3-b777-e877a8fbf647 | -1.26924 | -53.36991 | 2024-11-02 05:27:00 | NPP-375D | ALMEIRIM | PARÁ | Brasil | 1500503 | 15 | 33 | nan | nan | nan | Amazônia | 1.5 |
| 65b6d26f-cb0a-318e-8252-694c47d85ba5 | -1.21806 | -53.38346 | 2024-11-02 05:27:00 | NPP-375D | ALMEIRIM | PARÁ | Brasil | 1500503 | 15 | 33 | nan | nan | nan | Amazônia | 6.2 |
| 7244cb7d-69f8-3656-8bdb-2aeefa2f04ea | -1.21158 | -53.64771 | 2024-11-02 05:27:00 | NPP-375D | PRAINHA | PARÁ | Brasil | 1506005 | 15 | 33 | nan | nan | nan | Amazônia | 1.0 |
| 19eb0a1f-79cf-32ad-875e-be4b3793a3dd | -1.21084 | -53.65253 | 2024-11-02 05:27:00 | NPP-375D | PRAINHA | PARÁ | Brasil | 1506005 | 15 | 33 | nan | nan | nan | Amazônia | 3.7 |
| 1882090c-f15b-31a4-b875-94b4d419764e | -1.21006 | -53.65756 | 2024-11-02 05:27:00 | NPP-375D | PRAINHA | PARÁ | Brasil | 1506005 | 15 | 33 | nan | nan | nan | Amazônia | 3.7 |
| 8b41620b-27f1-34df-89ca-968132384537 | -1.20691 | -53.64679 | 2024-11-02 05:27:00 | NPP-375D | PRAINHA | PARÁ | Brasil | 1506005 | 15 | 33 | nan | nan | nan | Amazônia | 1.0 |
| 254146b4-f5ee-3113-a0b9-2ec4ddda384e | -1.20419 | -53.90951 | 2024-11-02 05:27:00 | NPP-375D | MONTE ALEGRE | PARÁ | Brasil | 1504802 | 15 | 33 | nan | nan | nan | Amazônia | 7.5 |
| d6745a27-b7fa-3331-9e4d-7f2c37c99fbd | -1.20343 | -53.9144 | 2024-11-02 05:27:00 | NPP-375D | MONTE ALEGRE | PARÁ | Brasil | 1504802 | 15 | 33 | nan | nan | nan | Amazônia | 7.5 |
| 76fa0640-d6de-358d-9b54-f41cadc479ab | -1.19951 | -53.90924 | 2024-11-02 05:27:00 | NPP-375D | MONTE ALEGRE | PARÁ | Brasil | 1504802 | 15 | 33 | nan | nan | nan | Amazônia | 15.4 |
| ef53904c-66b4-3e45-8486-25db040e02c6 | -1.19878 | -53.9139 | 2024-11-02 05:27:00 | NPP-375D | MONTE ALEGRE | PARÁ | Brasil | 1504802 | 15 | 33 | nan | nan | nan | Amazônia | 15.4 |
| fcdef0dc-b35c-3208-bba4-fa136def1c99 | -1.19483 | -53.90892 | 2024-11-02 05:27:00 | NPP-375D | MONTE ALEGRE | PARÁ | Brasil | 1504802 | 15 | 33 | nan | nan | nan | Amazônia | 15.4 |
| 048b771c-4969-30c9-8599-b5b88ee46026 | -1.19413 | -53.91335 | 2024-11-02 05:27:00 | NPP-375D | MONTE ALEGRE | PARÁ | Brasil | 1504802 | 15 | 33 | nan | nan | nan | Amazônia | 15.4 |
| 44492e96-2105-35f5-af39-8b5181903145 | -1.19288 | -53.64409 | 2024-11-02 05:27:00 | NPP-375D | PRAINHA | PARÁ | Brasil | 1506005 | 15 | 33 | nan | nan | nan | Amazônia | 4.9 |
| aeb4560b-d650-3e4c-85ef-5332a0ac1ca3 | -1.19205 | -53.6495 | 2024-11-02 05:27:00 | NPP-375D | PRAINHA | PARÁ | Brasil | 1506005 | 15 | 33 | nan | nan | nan | Amazônia | 6.2 |
| de3a5631-c471-3e6e-9f96-4e5d25d09dd1 | -1.19051 | -53.6909 | 2024-11-02 05:27:00 | NPP-375D | PRAINHA | PARÁ | Brasil | 1506005 | 15 | 33 | nan | nan | nan | Amazônia | 1.8 |
| 3a98a428-e793-3b3c-80af-4f5ee734e5d8 | -1.18658 | -53.68523 | 2024-11-02 05:27:00 | NPP-375D | PRAINHA | PARÁ | Brasil | 1506005 | 15 | 33 | nan | nan | nan | Amazônia | 1.1 |
| c5454f5f-5003-3563-a412-9fb9d42203f4 | -1.1858 | -53.6903 | 2024-11-02 05:27:00 | NPP-375D | PRAINHA | PARÁ | Brasil | 1506005 | 15 | 33 | nan | nan | nan | Amazônia | 3.1 |
| c06a6196-05ed-3eb0-ac4d-20b5e45c04e6 | -1.18502 | -53.6954 | 2024-11-02 05:27:00 | NPP-375D | PRAINHA | PARÁ | Brasil | 1506005 | 15 | 33 | nan | nan | nan | Amazônia | 3.1 |
| 64d07b73-c5a0-3655-b4b4-d2d6f7a4da97 | -1.18334 | -54.13198 | 2024-11-02 05:27:00 | NPP-375D | MONTE ALEGRE | PARÁ | Brasil | 1504802 | 15 | 33 | nan | nan | nan | Amazônia | 1.4 |
| 6dd46f05-883c-3298-8e30-814b64b7e206 | -1.18191 | -53.68436 | 2024-11-02 05:27:00 | NPP-375D | PRAINHA | PARÁ | Brasil | 1506005 | 15 | 33 | nan | nan | nan | Amazônia | 1.1 |
| 788a48cc-78a6-35ec-a217-e6052c1952d7 | -1.18111 | -53.68962 | 2024-11-02 05:27:00 | NPP-375D | PRAINHA | PARÁ | Brasil | 1506005 | 15 | 33 | nan | nan | nan | Amazônia | 3.1 |
| db5f3e4c-1999-3518-9e76-b1de7a379a53 | -1.16658 | -54.1784 | 2024-11-02 05:27:00 | NPP-375D | MONTE ALEGRE | PARÁ | Brasil | 1504802 | 15 | 33 | nan | nan | nan | Amazônia | 9.6 |
| 8d826f3a-6335-31fb-bd86-31f02b88d644 | -1.16276 | -54.08404 | 2024-11-02 05:27:00 | NPP-375D | MONTE ALEGRE | PARÁ | Brasil | 1504802 | 15 | 33 | nan | nan | nan | Amazônia | 1.9 |
| 6c7e7a28-31b4-3fee-8ad4-65de1db7da95 | -1.15892 | -54.0787 | 2024-11-02 05:27:00 | NPP-375D | MONTE ALEGRE | PARÁ | Brasil | 1504802 | 15 | 33 | nan | nan | nan | Amazônia | 1.2 |
| 574becb6-abd7-3a4d-a98c-a34b3b5fae06 | -1.1582 | -54.08333 | 2024-11-02 05:27:00 | NPP-375D | MONTE ALEGRE | PARÁ | Brasil | 1504802 | 15 | 33 | nan | nan | nan | Amazônia | 1.9 |
| fde6218e-e3d7-3608-a946-2696a0188b9e | -1.11813 | -54.16177 | 2024-11-02 05:27:00 | NPP-375D | MONTE ALEGRE | PARÁ | Brasil | 1504802 | 15 | 33 | nan | nan | nan | Amazônia | 1.8 |
| c71b4cf6-c564-3df1-ab9e-74cba722ff52 | -1.11743 | -54.16627 | 2024-11-02 05:27:00 | NPP-375D | MONTE ALEGRE | PARÁ | Brasil | 1504802 | 15 | 33 | nan | nan | nan | Amazônia | 1.8 |
| 1ed430a4-3277-3536-994d-bf6aaa7aa166 | -3.25065 | -54.16991 | 2024-11-02 05:27:00 | NPP-375D | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | 0.9 |
| 9b80bf71-ca68-3722-9bb0-c1af65c96ed2 | -3.20532 | -53.84855 | 2024-11-02 05:27:00 | NPP-375D | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | 3.2 |
| 5282050f-7526-341b-b020-b0937a4619ea | -3.63184 | -53.96309 | 2024-11-02 05:27:00 | NPP-375D | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | 3.1 |
| facf3170-54ad-3106-b24a-214a1a2ad088 | -3.62708 | -53.96226 | 2024-11-02 05:27:00 | NPP-375D | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | 3.1 |
| 1a22e273-df84-395e-b63d-ff5d84773d69 | -3.62635 | -53.96718 | 2024-11-02 05:27:00 | NPP-375D | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | 3.1 |
| 30503eaa-f91a-3007-bb74-8a003a42e483 | -3.40665 | -53.80373 | 2024-11-02 05:27:00 | NPP-375D | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | 1.5 |
| 39190850-c23e-360e-8639-3811b43fde87 | -3.40366 | -53.80052 | 2024-11-02 05:27:00 | NPP-375D | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | 1.4 |
| 3d81b931-3ca9-3b67-864d-95b1231a06d5 | -3.40284 | -53.8058 | 2024-11-02 05:27:00 | NPP-375D | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | 1.4 |
| fb6647b4-8d68-3fda-9386-03f3887522d4 | -3.40184 | -53.80293 | 2024-11-02 05:27:00 | NPP-375D | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | 1.5 |


[Clique aqui para ver as próximas entradas](README87.md)
