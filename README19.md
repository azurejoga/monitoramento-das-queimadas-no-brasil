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

## Dados Diários - Página 19

| ID | Latitude | Longitude | Data/Hora GMT | Satélite | Município | Estado | País | Município ID | Estado ID | País ID | Dias sem Chuva | Precipitação | Risco de Fogo | Bioma | FRP |
|----|----------|-----------|---------------|----------|-----------|--------|------|--------------|-----------|---------|----------------|--------------|----------------|-------|-----|
| 879ebb7a-9f9f-3482-ab4c-c5152542cba5 | -3.06693 | -50.49394 | 2024-10-19 04:25:00 | NOAA-21 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 1.6 |
| a1ab2413-58ba-322d-b682-df9747e32602 | -3.06572 | -50.36144 | 2024-10-19 04:25:00 | NOAA-21 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 4.0 |
| dd995351-4b78-3dbc-9725-e136edd3442d | -3.05371 | -49.41398 | 2024-10-19 04:25:00 | NOAA-21 | MOJU | PARÁ | Brasil | 1504703 | 15 | 33 | nan | nan | nan | Amazônia | 1.2 |
| 5afcc46d-349e-374f-806e-98e86eea627a | -3.04995 | -49.41339 | 2024-10-19 04:25:00 | NOAA-21 | MOJU | PARÁ | Brasil | 1504703 | 15 | 33 | nan | nan | nan | Amazônia | 1.2 |
| 027ad248-b035-39c8-9bef-7c8f31df055f | -3.46832 | -50.3575 | 2024-10-19 04:25:00 | NOAA-21 | PACAJÁ | PARÁ | Brasil | 1505486 | 15 | 33 | nan | nan | nan | Amazônia | 6.4 |
| dc382c96-a870-311e-bdc6-19f3e351872c | -3.46472 | -50.60898 | 2024-10-19 04:25:00 | NOAA-21 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 3.0 |
| 7465c969-c0c3-33db-8fad-a45f3a0e6213 | -3.45367 | -50.17533 | 2024-10-19 04:25:00 | NOAA-21 | PACAJÁ | PARÁ | Brasil | 1505486 | 15 | 33 | nan | nan | nan | Amazônia | 4.9 |
| e6ef2876-8406-306c-9ca4-c00b7981b83f | -3.45351 | -50.32394 | 2024-10-19 04:25:00 | NOAA-21 | PACAJÁ | PARÁ | Brasil | 1505486 | 15 | 33 | nan | nan | nan | Amazônia | 1.9 |
| 5847f324-13df-3f31-91dc-27ddb6e6ddaf | -3.45268 | -50.329 | 2024-10-19 04:25:00 | NOAA-21 | PACAJÁ | PARÁ | Brasil | 1505486 | 15 | 33 | nan | nan | nan | Amazônia | 3.6 |
| f5e42bbd-9a11-3bfb-9311-a259307d7a20 | -3.44242 | -50.2193 | 2024-10-19 04:25:00 | NOAA-21 | PACAJÁ | PARÁ | Brasil | 1505486 | 15 | 33 | nan | nan | nan | Amazônia | 1.6 |
| 47fec715-4ae1-377e-8825-0dff78e9cb3d | -3.44208 | -50.1704 | 2024-10-19 04:25:00 | NOAA-21 | PACAJÁ | PARÁ | Brasil | 1505486 | 15 | 33 | nan | nan | nan | Amazônia | 2.7 |
| 841d95bc-432e-3ea8-ab16-cc696f6ece3e | -3.44194 | -50.17352 | 2024-10-19 04:25:00 | NOAA-21 | PACAJÁ | PARÁ | Brasil | 1505486 | 15 | 33 | nan | nan | nan | Amazônia | 5.7 |
| bfda3825-fe78-32d9-b05a-a42a50038e02 | -3.44131 | -50.17524 | 2024-10-19 04:25:00 | NOAA-21 | PACAJÁ | PARÁ | Brasil | 1505486 | 15 | 33 | nan | nan | nan | Amazônia | 10.7 |
| 22399f63-3f4d-35a1-80e2-5024081858ca | -3.37557 | -52.17671 | 2024-10-19 04:25:00 | NOAA-21 | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 1.1 |
| 6b0f5dbd-c280-3a4c-a998-d2fd8b5e4373 | -4.13218 | -50.75038 | 2024-10-19 04:25:00 | NOAA-21 | PACAJÁ | PARÁ | Brasil | 1505486 | 15 | 33 | nan | nan | nan | Amazônia | 1.1 |
| 285397e4-a416-389e-979c-c9f6d87ab5ae | -3.44114 | -50.17836 | 2024-10-19 04:25:00 | NOAA-21 | PACAJÁ | PARÁ | Brasil | 1505486 | 15 | 33 | nan | nan | nan | Amazônia | 5.7 |
| b95908f9-fba7-3582-bc64-1acaa9a5e298 | -3.43896 | -50.21553 | 2024-10-19 04:25:00 | NOAA-21 | PACAJÁ | PARÁ | Brasil | 1505486 | 15 | 33 | nan | nan | nan | Amazônia | 3.2 |
| 7a5995b4-b25d-30c2-8ec3-cecbd5bd2f65 | -3.43849 | -50.21868 | 2024-10-19 04:25:00 | NOAA-21 | PACAJÁ | PARÁ | Brasil | 1505486 | 15 | 33 | nan | nan | nan | Amazônia | 1.6 |
| 69259b82-8416-394b-9736-143906964147 | -3.43622 | -50.2081 | 2024-10-19 04:25:00 | NOAA-21 | PACAJÁ | PARÁ | Brasil | 1505486 | 15 | 33 | nan | nan | nan | Amazônia | 1.8 |
| 93db6423-b777-31de-ab10-ed3ca4847b34 | -3.43541 | -50.21303 | 2024-10-19 04:25:00 | NOAA-21 | PACAJÁ | PARÁ | Brasil | 1505486 | 15 | 33 | nan | nan | nan | Amazônia | 74.1 |
| 8f1173b0-8391-39ec-9375-b0936aad5454 | -3.43458 | -50.21805 | 2024-10-19 04:25:00 | NOAA-21 | PACAJÁ | PARÁ | Brasil | 1505486 | 15 | 33 | nan | nan | nan | Amazônia | 74.1 |
| fcc1f634-7403-3dee-bfb4-4792af547220 | -3.43192 | -50.20923 | 2024-10-19 04:25:00 | NOAA-21 | PACAJÁ | PARÁ | Brasil | 1505486 | 15 | 33 | nan | nan | nan | Amazônia | 7.1 |
| 7956a3ba-2395-3a7c-82f5-75256b0983c2 | -3.43113 | -50.21421 | 2024-10-19 04:25:00 | NOAA-21 | PACAJÁ | PARÁ | Brasil | 1505486 | 15 | 33 | nan | nan | nan | Amazônia | 74.2 |
| 0c283edb-bcd3-3c1b-a114-6924e965a1b4 | -3.428 | -50.20859 | 2024-10-19 04:25:00 | NOAA-21 | PACAJÁ | PARÁ | Brasil | 1505486 | 15 | 33 | nan | nan | nan | Amazônia | 7.1 |
| 0ecbb0df-877f-3499-b00b-a2e750b1b740 | -3.42758 | -50.21172 | 2024-10-19 04:25:00 | NOAA-21 | PACAJÁ | PARÁ | Brasil | 1505486 | 15 | 33 | nan | nan | nan | Amazônia | 29.7 |
| 1bce43a4-ab7c-3d3a-95e1-ec41659cd7fb | -3.42675 | -50.21676 | 2024-10-19 04:25:00 | NOAA-21 | PACAJÁ | PARÁ | Brasil | 1505486 | 15 | 33 | nan | nan | nan | Amazônia | 29.7 |
| 9f9dc07f-e1bb-3ecc-855b-c6ec9261f549 | -2.36138 | -49.80833 | 2024-10-19 04:25:00 | NOAA-21 | OEIRAS DO PARÁ | PARÁ | Brasil | 1505205 | 15 | 33 | nan | nan | nan | Amazônia | 0.9 |
| eee6fe4b-509c-30c1-9d57-22fb52de701d | -2.35985 | -49.35513 | 2024-10-19 04:25:00 | NOAA-21 | IGARAPÉ-MIRI | PARÁ | Brasil | 1503309 | 15 | 33 | nan | nan | nan | Amazônia | 1.7 |
| cabe2b68-540f-38cc-82b5-20d02d934634 | -2.35913 | -49.35972 | 2024-10-19 04:25:00 | NOAA-21 | CAMETÁ | PARÁ | Brasil | 1502103 | 15 | 33 | nan | nan | nan | Amazônia | 1.7 |
| 68b549ec-1ec9-346f-9176-ef1fcf1209d7 | -2.35733 | -48.91573 | 2024-10-19 04:25:00 | NOAA-21 | MOJU | PARÁ | Brasil | 1504703 | 15 | 33 | nan | nan | nan | Amazônia | 2.0 |
| 9e28cade-3d1e-3e24-906b-c5ad7dd23c72 | -2.35663 | -48.92007 | 2024-10-19 04:25:00 | NOAA-21 | MOJU | PARÁ | Brasil | 1504703 | 15 | 33 | nan | nan | nan | Amazônia | 2.0 |
| 2eee0dcb-aaa4-3324-bee8-77b6d89296c4 | -2.34604 | -49.6577 | 2024-10-19 04:25:00 | NOAA-21 | CAMETÁ | PARÁ | Brasil | 1502103 | 15 | 33 | nan | nan | nan | Amazônia | 2.2 |
| 339a4516-1d49-3129-a6a8-7f3b64039f80 | -2.34527 | -49.66247 | 2024-10-19 04:25:00 | NOAA-21 | CAMETÁ | PARÁ | Brasil | 1502103 | 15 | 33 | nan | nan | nan | Amazônia | 2.2 |
| f82c0261-3c3b-311d-b23f-38856e3f5f45 | -2.3387 | -49.10185 | 2024-10-19 04:25:00 | NOAA-21 | MOJU | PARÁ | Brasil | 1504703 | 15 | 33 | nan | nan | nan | Amazônia | 2.3 |
| 5dfd198a-717e-3594-b039-6217aa4ef642 | -2.33727 | -49.11075 | 2024-10-19 04:25:00 | NOAA-21 | MOJU | PARÁ | Brasil | 1504703 | 15 | 33 | nan | nan | nan | Amazônia | 1.7 |
| 799d7389-65a0-3477-9604-dc38946b534e | -2.87381 | -49.46835 | 2024-10-19 04:25:00 | NOAA-21 | BAIÃO | PARÁ | Brasil | 1501204 | 15 | 33 | nan | nan | nan | Amazônia | 1.8 |
| ee201fdf-353f-38fa-8e86-ce971d86b794 | -2.84388 | -49.53445 | 2024-10-19 04:25:00 | NOAA-21 | BAIÃO | PARÁ | Brasil | 1501204 | 15 | 33 | nan | nan | nan | Amazônia | 1.6 |
| 78576220-508a-3fd4-af22-e8d7b1c3cec4 | -2.84314 | -49.53909 | 2024-10-19 04:25:00 | NOAA-21 | BAIÃO | PARÁ | Brasil | 1501204 | 15 | 33 | nan | nan | nan | Amazônia | 1.6 |
| 6b7d96fe-a99d-3599-bfb6-1bc0795b0964 | -2.83976 | -49.86721 | 2024-10-19 04:25:00 | NOAA-21 | OEIRAS DO PARÁ | PARÁ | Brasil | 1505205 | 15 | 33 | nan | nan | nan | Amazônia | 1.5 |
| 6b2e3c71-6a5d-31bd-a2d4-716be69ed01d | -2.77937 | -49.32962 | 2024-10-19 04:25:00 | NOAA-21 | MOJU | PARÁ | Brasil | 1504703 | 15 | 33 | nan | nan | nan | Amazônia | 6.6 |
| eda71274-b8e8-3450-81b8-375d2fc02040 | -2.77865 | -49.33414 | 2024-10-19 04:25:00 | NOAA-21 | MOJU | PARÁ | Brasil | 1504703 | 15 | 33 | nan | nan | nan | Amazônia | 6.6 |
| bdae5e6b-c52a-39c1-85e9-856f06b60e13 | -2.77562 | -49.32905 | 2024-10-19 04:25:00 | NOAA-21 | MOJU | PARÁ | Brasil | 1504703 | 15 | 33 | nan | nan | nan | Amazônia | 6.6 |
| e6597f03-658d-3cc1-af32-6a6b630935e1 | -2.76607 | -49.36478 | 2024-10-19 04:25:00 | NOAA-21 | MOJU | PARÁ | Brasil | 1504703 | 15 | 33 | nan | nan | nan | Amazônia | 2.2 |
| caf37185-d231-383f-8ae8-a5fd478724ca | -2.76232 | -49.3642 | 2024-10-19 04:25:00 | NOAA-21 | MOJU | PARÁ | Brasil | 1504703 | 15 | 33 | nan | nan | nan | Amazônia | 2.2 |
| 4b108d1c-6711-3ee0-94f4-8993b270c65f | -2.71288 | -49.16044 | 2024-10-19 04:25:00 | NOAA-21 | MOJU | PARÁ | Brasil | 1504703 | 15 | 33 | nan | nan | nan | Amazônia | 1.3 |
| e688b719-2223-393e-a7af-e0f5ebdbdfaf | -2.71218 | -49.16485 | 2024-10-19 04:25:00 | NOAA-21 | MOJU | PARÁ | Brasil | 1504703 | 15 | 33 | nan | nan | nan | Amazônia | 4.0 |
| 3519a9a9-4266-39fe-9b6d-0efcfba73201 | -2.62951 | -49.07148 | 2024-10-19 04:25:00 | NOAA-21 | MOJU | PARÁ | Brasil | 1504703 | 15 | 33 | nan | nan | nan | Amazônia | 3.6 |
| cfbff7e1-ab35-3207-aad9-8d7947e1eadc | -2.6265 | -49.06651 | 2024-10-19 04:25:00 | NOAA-21 | MOJU | PARÁ | Brasil | 1504703 | 15 | 33 | nan | nan | nan | Amazônia | 2.1 |
| 8363586e-4e53-3699-8797-790ead1492d0 | -2.62629 | -49.11618 | 2024-10-19 04:25:00 | NOAA-21 | MOJU | PARÁ | Brasil | 1504703 | 15 | 33 | nan | nan | nan | Amazônia | 2.0 |
| 9c8197bf-5d56-3de5-a1bd-bcad54e3bcb9 | -2.62581 | -49.07091 | 2024-10-19 04:25:00 | NOAA-21 | MOJU | PARÁ | Brasil | 1504703 | 15 | 33 | nan | nan | nan | Amazônia | 2.9 |
| 8609d747-5d57-361c-a8cd-a2ad7c3a7a44 | -2.62502 | -49.11493 | 2024-10-19 04:25:00 | NOAA-21 | MOJU | PARÁ | Brasil | 1504703 | 15 | 33 | nan | nan | nan | Amazônia | 1.9 |
| 41afabed-632c-3596-90a0-86ec19f7b260 | -2.62211 | -49.07033 | 2024-10-19 04:25:00 | NOAA-21 | MOJU | PARÁ | Brasil | 1504703 | 15 | 33 | nan | nan | nan | Amazônia | 2.9 |
| 4889c64f-54c9-3e16-aa7b-61898cd26c96 | -2.57081 | -48.94157 | 2024-10-19 04:25:00 | NOAA-21 | MOJU | PARÁ | Brasil | 1504703 | 15 | 33 | nan | nan | nan | Amazônia | 3.8 |
| c2bc355f-fa35-3a35-ad73-d21a6d780e46 | -2.57012 | -48.94589 | 2024-10-19 04:25:00 | NOAA-21 | MOJU | PARÁ | Brasil | 1504703 | 15 | 33 | nan | nan | nan | Amazônia | 3.4 |
| 4ee30dfb-1eec-3df0-a632-68f2a9e71240 | -2.56941 | -48.95024 | 2024-10-19 04:25:00 | NOAA-21 | MOJU | PARÁ | Brasil | 1504703 | 15 | 33 | nan | nan | nan | Amazônia | 3.4 |
| f0cc7fd0-4ad4-34b6-ae0a-fb1452dbb296 | -2.5647 | -49.216 | 2024-10-19 04:25:00 | NOAA-21 | MOJU | PARÁ | Brasil | 1504703 | 15 | 33 | nan | nan | nan | Amazônia | 2.8 |
| 0ce13f5e-070c-3dc1-8b9d-5100d5ee3337 | -2.54773 | -49.85302 | 2024-10-19 04:25:00 | NOAA-21 | OEIRAS DO PARÁ | PARÁ | Brasil | 1505205 | 15 | 33 | nan | nan | nan | Amazônia | 1.9 |
| 49965ada-b79d-3355-90ca-9024b6e68310 | -2.49918 | -49.28895 | 2024-10-19 04:25:00 | NOAA-21 | MOCAJUBA | PARÁ | Brasil | 1504604 | 15 | 33 | nan | nan | nan | Amazônia | 1.3 |
| 46cb0a4b-8498-34a9-8a43-b1bcf76da562 | -2.49845 | -49.29347 | 2024-10-19 04:25:00 | NOAA-21 | MOCAJUBA | PARÁ | Brasil | 1504604 | 15 | 33 | nan | nan | nan | Amazônia | 1.3 |
| 719585d6-d3a5-3ef7-b7ab-c14e55e9eb07 | -2.49799 | -49.29059 | 2024-10-19 04:25:00 | NOAA-21 | MOCAJUBA | PARÁ | Brasil | 1504604 | 15 | 33 | nan | nan | nan | Amazônia | 4.2 |
| 3908ca44-eabf-348c-ba19-4afe69b7577c | -2.49469 | -49.29289 | 2024-10-19 04:25:00 | NOAA-21 | MOCAJUBA | PARÁ | Brasil | 1504604 | 15 | 33 | nan | nan | nan | Amazônia | 1.3 |
| 31ceb9dc-b017-3cac-bf59-9c87c0c12a4b | -2.49343 | -49.91177 | 2024-10-19 04:25:00 | NOAA-21 | OEIRAS DO PARÁ | PARÁ | Brasil | 1505205 | 15 | 33 | nan | nan | nan | Amazônia | 1.2 |
| 3cc9f7e5-b5de-30ad-90ea-a9f0b07a77bd | -2.47328 | -49.39907 | 2024-10-19 04:25:00 | NOAA-21 | CAMETÁ | PARÁ | Brasil | 1502103 | 15 | 33 | nan | nan | nan | Amazônia | 1.8 |
| e825ebb0-63e4-3276-8c1f-5f333db09e3c | -2.4517 | -49.62806 | 2024-10-19 04:25:00 | NOAA-21 | CAMETÁ | PARÁ | Brasil | 1502103 | 15 | 33 | nan | nan | nan | Amazônia | 2.5 |
| ba0f5b06-efeb-344f-84d0-f4205a016858 | -2.41459 | -49.69782 | 2024-10-19 04:25:00 | NOAA-21 | CAMETÁ | PARÁ | Brasil | 1502103 | 15 | 33 | nan | nan | nan | Amazônia | 1.3 |
| a5c76619-7666-3e39-871c-d7e4f72e639e | -2.41281 | -48.94665 | 2024-10-19 04:25:00 | NOAA-21 | MOJU | PARÁ | Brasil | 1504703 | 15 | 33 | nan | nan | nan | Amazônia | 2.1 |
| 9b2c79e6-71fc-3a8c-8e76-767b1e2e89f4 | -2.40912 | -48.94607 | 2024-10-19 04:25:00 | NOAA-21 | MOJU | PARÁ | Brasil | 1504703 | 15 | 33 | nan | nan | nan | Amazônia | 2.1 |
| 1d2864b4-fce2-38c2-8452-4f273e59439a | -3.51354 | -50.32517 | 2024-10-19 04:25:00 | NOAA-21 | PACAJÁ | PARÁ | Brasil | 1505486 | 15 | 33 | nan | nan | nan | Amazônia | 1.3 |
| 659d448a-dc14-3141-b341-1c6f3eccf846 | -3.47227 | -50.35815 | 2024-10-19 04:25:00 | NOAA-21 | PACAJÁ | PARÁ | Brasil | 1505486 | 15 | 33 | nan | nan | nan | Amazônia | 4.1 |
| 264339d0-f354-37dd-a396-232864db42e7 | -3.46818 | -50.61311 | 2024-10-19 04:25:00 | NOAA-21 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 1.9 |
| 4c586e79-848d-3779-a816-88db8944494d | -3.46417 | -50.61242 | 2024-10-19 04:25:00 | NOAA-21 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 1.9 |
| cefe3adb-d4d6-3f51-9794-47299cdbcb87 | -3.4607 | -50.60833 | 2024-10-19 04:25:00 | NOAA-21 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 2.6 |
| 2a3fc3bd-0a27-36aa-bda4-43fd29b96db9 | -3.46015 | -50.61177 | 2024-10-19 04:25:00 | NOAA-21 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 2.4 |
| 89489867-8f80-3f43-a07e-f77117ba1294 | -3.45983 | -49.24903 | 2024-10-19 04:25:00 | NOAA-21 | BREU BRANCO | PARÁ | Brasil | 1501782 | 15 | 33 | nan | nan | nan | Amazônia | 1.8 |
| d9b083bf-fd2c-3efd-b82d-dc7ba55ac20a | -3.45663 | -50.32963 | 2024-10-19 04:25:00 | NOAA-21 | PACAJÁ | PARÁ | Brasil | 1505486 | 15 | 33 | nan | nan | nan | Amazônia | 3.6 |
| c4bb363a-84f2-3e2d-b8a7-07a76660c08b | -3.45613 | -50.61112 | 2024-10-19 04:25:00 | NOAA-21 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 2.4 |
| 00c3ec56-017e-38d0-9fcc-e488cc2c6949 | -3.43975 | -50.21053 | 2024-10-19 04:25:00 | NOAA-21 | PACAJÁ | PARÁ | Brasil | 1505486 | 15 | 33 | nan | nan | nan | Amazônia | 2.3 |
| fe101c3f-ddc3-3a2a-9269-44c69dcd026f | -3.43933 | -50.21365 | 2024-10-19 04:25:00 | NOAA-21 | PACAJÁ | PARÁ | Brasil | 1505486 | 15 | 33 | nan | nan | nan | Amazônia | 1.6 |
| 9a9646a9-5f8d-3889-b6f3-f075b4ac0953 | -3.43817 | -50.22057 | 2024-10-19 04:25:00 | NOAA-21 | PACAJÁ | PARÁ | Brasil | 1505486 | 15 | 33 | nan | nan | nan | Amazônia | 3.2 |
| b6514a3b-4d27-3311-9339-966a0f326173 | -3.43583 | -50.20992 | 2024-10-19 04:25:00 | NOAA-21 | PACAJÁ | PARÁ | Brasil | 1505486 | 15 | 33 | nan | nan | nan | Amazônia | 2.3 |
| 5c476dc4-c3ec-304a-9778-879ffb0d18b4 | -3.43504 | -50.21489 | 2024-10-19 04:25:00 | NOAA-21 | PACAJÁ | PARÁ | Brasil | 1505486 | 15 | 33 | nan | nan | nan | Amazônia | 3.2 |
| df3052ff-2afa-3c4b-b9f6-f9a13ecdb845 | -3.43425 | -50.21992 | 2024-10-19 04:25:00 | NOAA-21 | PACAJÁ | PARÁ | Brasil | 1505486 | 15 | 33 | nan | nan | nan | Amazônia | 3.2 |
| 72691c22-cd97-365e-81d0-989443cbedf4 | -3.43231 | -50.20743 | 2024-10-19 04:25:00 | NOAA-21 | PACAJÁ | PARÁ | Brasil | 1505486 | 15 | 33 | nan | nan | nan | Amazônia | 1.8 |
| 304b783f-0a72-364f-b961-fad018da5ad9 | -3.43066 | -50.2174 | 2024-10-19 04:25:00 | NOAA-21 | PACAJÁ | PARÁ | Brasil | 1505486 | 15 | 33 | nan | nan | nan | Amazônia | 74.1 |
| 132d4ccd-6550-3400-bee7-311fbbccf490 | -3.43033 | -50.21928 | 2024-10-19 04:25:00 | NOAA-21 | PACAJÁ | PARÁ | Brasil | 1505486 | 15 | 33 | nan | nan | nan | Amazônia | 74.2 |
| 3009bdec-1129-3a01-808c-2812f363eb6c | -3.42721 | -50.21358 | 2024-10-19 04:25:00 | NOAA-21 | PACAJÁ | PARÁ | Brasil | 1505486 | 15 | 33 | nan | nan | nan | Amazônia | 74.2 |
| a6d48312-3e23-3606-8924-c2b16c2391ca | -3.42641 | -50.21863 | 2024-10-19 04:25:00 | NOAA-21 | PACAJÁ | PARÁ | Brasil | 1505486 | 15 | 33 | nan | nan | nan | Amazônia | 74.2 |
| bd4be235-dc04-36b5-a568-80a1bb1e3171 | -3.42408 | -50.20801 | 2024-10-19 04:25:00 | NOAA-21 | PACAJÁ | PARÁ | Brasil | 1505486 | 15 | 33 | nan | nan | nan | Amazônia | 2.9 |
| 4571003d-8b55-38d3-b659-d16d52937b44 | -3.42365 | -50.21116 | 2024-10-19 04:25:00 | NOAA-21 | PACAJÁ | PARÁ | Brasil | 1505486 | 15 | 33 | nan | nan | nan | Amazônia | 29.7 |
| b5a632b7-48c0-3f48-b055-0b4e60fe3d3c | -3.42328 | -50.213 | 2024-10-19 04:25:00 | NOAA-21 | PACAJÁ | PARÁ | Brasil | 1505486 | 15 | 33 | nan | nan | nan | Amazônia | 2.8 |
| e08d6bd4-bd0c-3e96-98bc-228e02a1f43b | -3.41595 | -50.62998 | 2024-10-19 04:25:00 | NOAA-21 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 1.6 |
| cb0cb8ae-c4fc-3301-82f2-99a6dcfe522a | -3.40491 | -50.32868 | 2024-10-19 04:25:00 | NOAA-21 | PACAJÁ | PARÁ | Brasil | 1505486 | 15 | 33 | nan | nan | nan | Amazônia | 2.0 |
| 1181d050-94e2-34c1-a12b-aabc7ef9335b | -3.3898 | -50.34717 | 2024-10-19 04:25:00 | NOAA-21 | PACAJÁ | PARÁ | Brasil | 1505486 | 15 | 33 | nan | nan | nan | Amazônia | 5.4 |
| 9eb065cd-cab3-3d22-b101-42feada1e8fd | -3.38584 | -50.34656 | 2024-10-19 04:25:00 | NOAA-21 | PACAJÁ | PARÁ | Brasil | 1505486 | 15 | 33 | nan | nan | nan | Amazônia | 8.2 |
| c1cfaca2-1719-3b7c-94af-c9604d7c7b48 | -3.38188 | -50.34595 | 2024-10-19 04:25:00 | NOAA-21 | PACAJÁ | PARÁ | Brasil | 1505486 | 15 | 33 | nan | nan | nan | Amazônia | 8.2 |
| 931b9e2a-b051-351a-8e0f-e7d0588bfd7e | -3.36471 | -50.30163 | 2024-10-19 04:25:00 | NOAA-21 | PACAJÁ | PARÁ | Brasil | 1505486 | 15 | 33 | nan | nan | nan | Amazônia | 2.9 |
| 46ea659f-6e7d-3c3f-b97e-9b26ec79d4f5 | -3.36076 | -50.30102 | 2024-10-19 04:25:00 | NOAA-21 | PACAJÁ | PARÁ | Brasil | 1505486 | 15 | 33 | nan | nan | nan | Amazônia | 4.0 |
| 0e03406b-7b9d-3623-b13d-2a062488d2ac | -3.35994 | -50.30608 | 2024-10-19 04:25:00 | NOAA-21 | PACAJÁ | PARÁ | Brasil | 1505486 | 15 | 33 | nan | nan | nan | Amazônia | 2.3 |
| e5fd4a89-56e4-3c34-8e9b-35d103b449f7 | -3.34901 | -49.14371 | 2024-10-19 04:25:00 | NOAA-21 | MOJU | PARÁ | Brasil | 1504703 | 15 | 33 | nan | nan | nan | Amazônia | 1.3 |
| 7153bd97-6782-3e27-bdda-54624d0494f6 | -3.34832 | -49.14801 | 2024-10-19 04:25:00 | NOAA-21 | MOJU | PARÁ | Brasil | 1504703 | 15 | 33 | nan | nan | nan | Amazônia | 1.3 |


[Clique aqui para ver as próximas entradas](README20.md)
