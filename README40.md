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

## Dados Diários - Página 40

| ID | Latitude | Longitude | Data/Hora GMT | Satélite | Município | Estado | País | Município ID | Estado ID | País ID | Dias sem Chuva | Precipitação | Risco de Fogo | Bioma | FRP |
|----|----------|-----------|---------------|----------|-----------|--------|------|--------------|-----------|---------|----------------|--------------|----------------|-------|-----|
| c8528bf2-8738-3bd2-b6ba-7b1e7ca5581f | -1.89912 | -53.02585 | 2024-11-26 05:01:00 | NOAA-20 | PORTO DE MOZ | PARÁ | Brasil | 1505908 | 15 | 33 | nan | nan | nan | Amazônia | 1.8 |
| 14058b1b-979e-3baa-9068-4a6caea49978 | -3.96041 | -48.07371 | 2024-11-26 05:01:00 | NOAA-20 | DOM ELISEU | PARÁ | Brasil | 1502939 | 15 | 33 | nan | nan | nan | Amazônia | 1.3 |
| e66feb04-441a-39c6-a025-d84f1926b3e5 | -3.96964 | -48.0755 | 2024-11-26 05:01:00 | NOAA-20 | DOM ELISEU | PARÁ | Brasil | 1502939 | 15 | 33 | nan | nan | nan | Amazônia | 38.4 |
| e72a72bb-54ad-34f3-92ff-e1997b7aff7b | -2.64225 | -48.48103 | 2024-11-26 05:01:00 | NOAA-20 | TAILÂNDIA | PARÁ | Brasil | 1507953 | 15 | 33 | nan | nan | nan | Amazônia | 0.9 |
| 3458c5c9-cfd6-30e1-80ef-e26f90caab50 | -3.47229 | -47.68572 | 2024-11-26 05:01:00 | NOAA-20 | PARAGOMINAS | PARÁ | Brasil | 1505502 | 15 | 33 | nan | nan | nan | Amazônia | 5.4 |
| fffc3a98-2f5c-3d74-a659-302b56779971 | -3.96816 | -48.08509 | 2024-11-26 05:01:00 | NOAA-20 | DOM ELISEU | PARÁ | Brasil | 1502939 | 15 | 33 | nan | nan | nan | Amazônia | 5.2 |
| 0260cf3b-a606-3a5c-b786-4b4703666cd7 | -2.70208 | -51.99877 | 2024-11-26 05:01:00 | NOAA-20 | SENADOR JOSÉ PORFÍRIO | PARÁ | Brasil | 1507805 | 15 | 33 | nan | nan | nan | Amazônia | 2.7 |
| 9f358173-66b8-3d73-9afb-b3b8fb51920c | -3.50648 | -53.81856 | 2024-11-26 05:01:00 | NOAA-20 | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | 1.2 |
| b6442651-22ec-339d-ab35-0830d0ea3cf0 | -3.28524 | -53.68982 | 2024-11-26 05:01:00 | NOAA-20 | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | 1.2 |
| b2576579-f7aa-3178-9529-734ddeea93fa | -3.96577 | -48.06973 | 2024-11-26 05:01:00 | NOAA-20 | DOM ELISEU | PARÁ | Brasil | 1502939 | 15 | 33 | nan | nan | nan | Amazônia | 38.4 |
| 5b72851f-8686-3ae7-a501-5b86906120d4 | -4.11138 | -51.05919 | 2024-11-26 05:01:00 | NOAA-20 | PACAJÁ | PARÁ | Brasil | 1505486 | 15 | 33 | nan | nan | nan | Amazônia | 1.7 |
| 71928058-143f-37aa-98f8-db8c15578e7b | -2.80917 | -53.01304 | 2024-11-26 05:01:00 | NOAA-20 | MEDICILÂNDIA | PARÁ | Brasil | 1504455 | 15 | 33 | nan | nan | nan | Amazônia | 0.8 |
| 93e9cd99-c801-3c91-aaab-d7bfd6943138 | -6.37185 | -47.36008 | 2024-11-26 05:01:00 | NOAA-20 | PORTO FRANCO | MARANHÃO | Brasil | 2109007 | 21 | 33 | nan | nan | nan | Cerrado | 1.8 |
| 53e53018-9bd3-380c-b859-90d0b772f15a | -8.26171 | -49.54552 | 2024-11-26 05:01:00 | NOAA-20 | CONCEIÇÃO DO ARAGUAIA | PARÁ | Brasil | 1502707 | 15 | 33 | nan | nan | nan | Amazônia | 1.4 |
| 40a597b9-197b-3ea4-9e5b-bb35571d508c | -3.97032 | -48.09253 | 2024-11-26 05:01:00 | NOAA-20 | DOM ELISEU | PARÁ | Brasil | 1502939 | 15 | 33 | nan | nan | nan | Amazônia | 5.1 |
| 7a27fbe4-79c3-3614-85b8-0fcbbc11aae7 | -2.80062 | -53.02313 | 2024-11-26 05:01:00 | NOAA-20 | MEDICILÂNDIA | PARÁ | Brasil | 1504455 | 15 | 33 | nan | nan | nan | Amazônia | 1.5 |
| e6e1ba28-1b2f-36db-9ad3-de4807ab3ec2 | -6.63824 | -47.34618 | 2024-11-26 05:01:00 | NOAA-20 | ESTREITO | MARANHÃO | Brasil | 2104057 | 21 | 33 | nan | nan | nan | Cerrado | 6.6 |
| 316267a4-0ba3-35a9-bd39-5b9240e02ea7 | -3.23309 | -50.78439 | 2024-11-26 05:01:00 | NOAA-20 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 2.4 |
| 5a0b2964-53fd-3681-8087-ea99ad12b3c4 | -3.32753 | -53.71788 | 2024-11-26 05:01:00 | NOAA-20 | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | 0.8 |
| dbcbcb63-052e-3f89-a098-29d59ba63a0b | -2.27335 | -51.91654 | 2024-11-26 05:01:00 | NOAA-20 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 1.3 |
| 582dcfed-8f7f-3034-8bef-c04bacf0547e | -3.97672 | -48.04856 | 2024-11-26 05:01:00 | NOAA-20 | DOM ELISEU | PARÁ | Brasil | 1502939 | 15 | 33 | nan | nan | nan | Amazônia | 1.9 |
| 5c40549d-923a-33fa-ad7d-0f65517ea962 | -2.16933 | -53.26988 | 2024-11-26 05:01:00 | NOAA-20 | PRAINHA | PARÁ | Brasil | 1506005 | 15 | 33 | nan | nan | nan | Amazônia | 0.8 |
| 5632d273-cb3c-33d3-81a5-8672eda67965 | -2.98454 | -53.35017 | 2024-11-26 05:01:00 | NOAA-20 | MEDICILÂNDIA | PARÁ | Brasil | 1504455 | 15 | 33 | nan | nan | nan | Amazônia | 0.6 |
| c8ada6c5-7fd3-30d6-8435-61214b8d0c1c | -3.51655 | -53.82005 | 2024-11-26 05:01:00 | NOAA-20 | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | 0.4 |
| 46ef06cd-bd56-3f10-b6b6-855295191c35 | -3.24537 | -50.66689 | 2024-11-26 05:01:00 | NOAA-20 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 1.2 |
| 0a3d3fbc-d9de-3c31-a392-2d104b5a5d7d | -2.25259 | -53.62169 | 2024-11-26 05:01:00 | NOAA-20 | PRAINHA | PARÁ | Brasil | 1506005 | 15 | 33 | nan | nan | nan | Amazônia | 0.7 |
| 7ae026ff-580f-36be-bd32-81344ad4e182 | -3.26906 | -50.56143 | 2024-11-26 05:01:00 | NOAA-20 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 1.0 |
| e96ba04d-3f54-304f-ade2-ae542cc5776b | -3.3402 | -50.04785 | 2024-11-26 05:01:00 | NOAA-20 | PACAJÁ | PARÁ | Brasil | 1505486 | 15 | 33 | nan | nan | nan | Amazônia | 1.3 |
| cf5fb73c-3b14-3012-89b7-6375426a057a | -3.05991 | -50.24818 | 2024-11-26 05:01:00 | NOAA-20 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 2.4 |
| 9e21e546-05d3-36ce-a288-5ed267b133ac | -3.97455 | -48.06344 | 2024-11-26 05:01:00 | NOAA-20 | DOM ELISEU | PARÁ | Brasil | 1502939 | 15 | 33 | nan | nan | nan | Amazônia | 33.5 |
| cb9cabc5-3ff1-3c3e-8ee5-cda090ccacc6 | -3.50087 | -53.8105 | 2024-11-26 05:01:00 | NOAA-20 | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | 4.9 |
| d06e5b21-1be7-36a5-ade4-431b162215e7 | -4.24375 | -48.59232 | 2024-11-26 05:01:00 | NOAA-20 | RONDON DO PARÁ | PARÁ | Brasil | 1506187 | 15 | 33 | nan | nan | nan | Amazônia | 1.4 |
| a746f162-964c-313d-8de4-948de0bbd303 | -3.97958 | -48.09406 | 2024-11-26 05:01:00 | NOAA-20 | DOM ELISEU | PARÁ | Brasil | 1502939 | 15 | 33 | nan | nan | nan | Amazônia | 10.0 |
| 848cf5ce-f851-3cf0-b2fd-d202ec2d20b1 | -4.53651 | -43.29749 | 2024-11-26 05:01:00 | NOAA-20 | ALDEIAS ALTAS | MARANHÃO | Brasil | 2100303 | 21 | 33 | nan | nan | nan | Cerrado | 12.0 |
| d16a642b-4f34-3090-b287-54148a94e026 | -3.97565 | -48.08846 | 2024-11-26 05:01:00 | NOAA-20 | DOM ELISEU | PARÁ | Brasil | 1502939 | 15 | 33 | nan | nan | nan | Amazônia | 10.0 |
| 5a1d6c01-ba17-3463-8072-b895ad63b572 | -3.15691 | -50.5868 | 2024-11-26 05:01:00 | NOAA-20 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 1.1 |
| 1a949821-91e2-33e8-8b4f-cbd516e47e38 | -3.28786 | -51.15698 | 2024-11-26 05:01:00 | NOAA-20 | PACAJÁ | PARÁ | Brasil | 1505486 | 15 | 33 | nan | nan | nan | Amazônia | 2.1 |
| e28ae080-c4db-3003-bb87-a5cc2f62d3c7 | -3.96722 | -48.06027 | 2024-11-26 05:01:00 | NOAA-20 | DOM ELISEU | PARÁ | Brasil | 1502939 | 15 | 33 | nan | nan | nan | Amazônia | 44.8 |
| 99180d7c-250e-3983-b2ef-a27c0dcc9d49 | -2.4505 | -53.70247 | 2024-11-26 05:01:00 | NOAA-20 | PRAINHA | PARÁ | Brasil | 1506005 | 15 | 33 | nan | nan | nan | Amazônia | 2.0 |
| 491b935e-371f-334b-bbbf-85bae18f6f65 | -3.25853 | -53.27616 | 2024-11-26 05:01:00 | NOAA-20 | MEDICILÂNDIA | PARÁ | Brasil | 1504455 | 15 | 33 | nan | nan | nan | Amazônia | 1.3 |
| 4b6445c0-d6ca-300d-8c47-81a4cbcfee13 | -3.50254 | -53.79988 | 2024-11-26 05:01:00 | NOAA-20 | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | 1.1 |
| d2045687-6f6a-3323-9dd3-06678d9c42d4 | -3.27105 | -50.44087 | 2024-11-26 05:01:00 | NOAA-20 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 1.4 |
| d7f00a18-4330-376a-a80b-dfbad422b015 | -2.59361 | -51.83363 | 2024-11-26 05:01:00 | NOAA-20 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 1.4 |
| 1f228327-8785-311b-ba38-805615abb9f0 | -4.381 | -48.13128 | 2024-11-26 05:01:00 | NOAA-20 | RONDON DO PARÁ | PARÁ | Brasil | 1506187 | 15 | 33 | nan | nan | nan | Amazônia | 1.5 |
| 82306d1d-749a-3295-a886-ca4458bfaf83 | -3.23209 | -50.78203 | 2024-11-26 05:01:00 | NOAA-20 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 2.3 |
| 6d1197fd-d946-38e1-951d-b9002dad4389 | -2.64889 | -51.77392 | 2024-11-26 05:01:00 | NOAA-20 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 1.2 |
| 7de2c5b3-356b-3ed4-8c30-fc76ca527d36 | -8.26619 | -49.54614 | 2024-11-26 05:01:00 | NOAA-20 | CONCEIÇÃO DO ARAGUAIA | PARÁ | Brasil | 1502707 | 15 | 33 | nan | nan | nan | Amazônia | 1.4 |
| f0dfa22b-9191-31d8-ba91-d7928b56301a | -3.3481 | -50.51334 | 2024-11-26 05:01:00 | NOAA-20 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 2.0 |
| 9de39462-0517-3178-b1da-f9fd5e2129e7 | -3.38288 | -50.10092 | 2024-11-26 05:01:00 | NOAA-20 | PACAJÁ | PARÁ | Brasil | 1505486 | 15 | 33 | nan | nan | nan | Amazônia | 1.0 |
| 53918e21-7cce-3f9a-b0c7-02fcdfecc196 | -3.28911 | -50.27153 | 2024-11-26 05:01:00 | NOAA-20 | PACAJÁ | PARÁ | Brasil | 1505486 | 15 | 33 | nan | nan | nan | Amazônia | 5.0 |
| 3768a1b0-4c0f-304a-8888-7641a923c5e7 | -3.84473 | -49.96351 | 2024-11-26 05:01:00 | NOAA-20 | TUCURUÍ | PARÁ | Brasil | 1508100 | 15 | 33 | nan | nan | nan | Amazônia | 1.1 |
| f24ecd18-ce0b-38e7-98f7-93fd19bf6b0b | -4.53729 | -43.29211 | 2024-11-26 05:01:00 | NOAA-20 | ALDEIAS ALTAS | MARANHÃO | Brasil | 2100303 | 21 | 33 | nan | nan | nan | Cerrado | 8.9 |
| 43ad2ff3-63a3-379f-935f-78b3583aa305 | -2.59425 | -51.82957 | 2024-11-26 05:01:00 | NOAA-20 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 1.4 |
| 3d07ec56-f577-3a89-94d4-818df7631579 | -3.96427 | -48.0795 | 2024-11-26 05:01:00 | NOAA-20 | DOM ELISEU | PARÁ | Brasil | 1502939 | 15 | 33 | nan | nan | nan | Amazônia | 5.2 |
| 8c81d47c-60c9-36ed-a0ac-83d8c5418186 | -4.10759 | -51.05848 | 2024-11-26 05:01:00 | NOAA-20 | PACAJÁ | PARÁ | Brasil | 1505486 | 15 | 33 | nan | nan | nan | Amazônia | 1.7 |
| 7327ed81-fcab-3c4b-a655-b1612724878c | -3.29024 | -51.11563 | 2024-11-26 05:01:00 | NOAA-20 | PACAJÁ | PARÁ | Brasil | 1505486 | 15 | 33 | nan | nan | nan | Amazônia | 1.2 |
| 9f5fe7da-a5b0-37b6-ac75-5f10df39db57 | -3.97172 | -48.08292 | 2024-11-26 05:01:00 | NOAA-20 | DOM ELISEU | PARÁ | Brasil | 1502939 | 15 | 33 | nan | nan | nan | Amazônia | 27.8 |
| 35070595-3582-3fec-aa6e-c6f0171deff4 | -3.51715 | -50.22394 | 2024-11-26 05:01:00 | NOAA-20 | PACAJÁ | PARÁ | Brasil | 1505486 | 15 | 33 | nan | nan | nan | Amazônia | 1.9 |
| 8fe92bdc-0a0a-3099-b59d-525ce40015b3 | -4.54606 | -43.27693 | 2024-11-26 05:01:00 | NOAA-20 | ALDEIAS ALTAS | MARANHÃO | Brasil | 2100303 | 21 | 33 | nan | nan | nan | Cerrado | 2.4 |
| 2578da5a-9496-361a-b5df-f08080db19c2 | -2.99416 | -53.44385 | 2024-11-26 05:01:00 | NOAA-20 | MEDICILÂNDIA | PARÁ | Brasil | 1504455 | 15 | 33 | nan | nan | nan | Amazônia | 0.4 |
| 96b4dfd5-1f52-3fda-9f24-43b0ee3f1fae | -3.0376 | -48.51096 | 2024-11-26 05:01:00 | NOAA-20 | TOMÉ-AÇU | PARÁ | Brasil | 1508001 | 15 | 33 | nan | nan | nan | Amazônia | 0.8 |
| d7f8547c-ba38-3a11-9847-79e3ce421ef4 | -3.07526 | -49.50117 | 2024-11-26 05:01:00 | NOAA-20 | MOJU | PARÁ | Brasil | 1504703 | 15 | 33 | nan | nan | nan | Amazônia | 1.5 |
| 41edc963-a805-351a-a80c-72e5b3dabe01 | -4.53927 | -43.28679 | 2024-11-26 05:01:00 | NOAA-20 | ALDEIAS ALTAS | MARANHÃO | Brasil | 2100303 | 21 | 33 | nan | nan | nan | Cerrado | 3.4 |
| c7be3434-b28a-3624-82a0-d3b4ab6ed3eb | -3.24606 | -53.28913 | 2024-11-26 05:01:00 | NOAA-20 | MEDICILÂNDIA | PARÁ | Brasil | 1504455 | 15 | 33 | nan | nan | nan | Amazônia | 1.9 |
| d3ddc613-953f-3378-ac0d-21793468763e | -3.057 | -53.21984 | 2024-11-26 05:01:00 | NOAA-20 | MEDICILÂNDIA | PARÁ | Brasil | 1504455 | 15 | 33 | nan | nan | nan | Amazônia | 1.0 |
| 2f0105d3-16e0-3c2b-951c-36403e7aa6c6 | -3.22825 | -50.78146 | 2024-11-26 05:01:00 | NOAA-20 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 2.3 |
| 747f9d1c-e108-3329-b927-b139d974e15e | -2.79379 | -53.02208 | 2024-11-26 05:01:00 | NOAA-20 | MEDICILÂNDIA | PARÁ | Brasil | 1504455 | 15 | 33 | nan | nan | nan | Amazônia | 0.9 |
| 7e3fea8a-6ba2-3dee-9c0a-cf378ee3b83f | -2.88593 | -48.74039 | 2024-11-26 05:01:00 | NOAA-20 | TAILÂNDIA | PARÁ | Brasil | 1507953 | 15 | 33 | nan | nan | nan | Amazônia | 2.0 |
| 94c28561-2924-38f0-8e48-ce31904bf09f | -3.68206 | -49.63752 | 2024-11-26 05:01:00 | NOAA-20 | BREU BRANCO | PARÁ | Brasil | 1501782 | 15 | 33 | nan | nan | nan | Amazônia | 1.7 |
| e90491c7-b35d-3d1d-899e-fda756ab92f6 | -3.95726 | -48.06324 | 2024-11-26 05:01:00 | NOAA-20 | DOM ELISEU | PARÁ | Brasil | 1502939 | 15 | 33 | nan | nan | nan | Amazônia | 1.2 |
| 815fa249-535a-3a78-9280-db02387c587c | -3.25059 | -53.28239 | 2024-11-26 05:01:00 | NOAA-20 | MEDICILÂNDIA | PARÁ | Brasil | 1504455 | 15 | 33 | nan | nan | nan | Amazônia | 0.8 |
| 28770635-d3ad-3c51-89fd-1f170759b995 | -3.96317 | -48.07639 | 2024-11-26 05:01:00 | NOAA-20 | DOM ELISEU | PARÁ | Brasil | 1502939 | 15 | 33 | nan | nan | nan | Amazônia | 2.9 |
| 05b6e5ad-502e-376b-98cf-1a8e496a4444 | -2.22769 | -53.23842 | 2024-11-26 05:01:00 | NOAA-20 | PORTO DE MOZ | PARÁ | Brasil | 1505908 | 15 | 33 | nan | nan | nan | Amazônia | 0.9 |
| 6ebe1c96-ac64-3320-8517-8f1ea59e820b | -1.80499 | -55.67399 | 2024-11-26 05:01:00 | NOAA-20 | ÓBIDOS | PARÁ | Brasil | 1505106 | 15 | 33 | nan | nan | nan | Amazônia | 0.4 |
| 968e210a-9f6a-39c7-85e6-d33658f8a52d | -1.60617 | -54.95155 | 2024-11-26 05:01:00 | NOAA-20 | ALENQUER | PARÁ | Brasil | 1500404 | 15 | 33 | nan | nan | nan | Amazônia | 0.5 |
| 1decb333-4b92-3102-b74d-84bb61d652b9 | -3.7939 | -49.94114 | 2024-11-26 05:01:00 | NOAA-20 | TUCURUÍ | PARÁ | Brasil | 1508100 | 15 | 33 | nan | nan | nan | Amazônia | 0.9 |
| e3181c33-36c3-304f-b186-d84ded3b3f3c | -3.38341 | -50.09741 | 2024-11-26 05:01:00 | NOAA-20 | PACAJÁ | PARÁ | Brasil | 1505486 | 15 | 33 | nan | nan | nan | Amazônia | 1.8 |
| 88c85511-70ee-3080-aad0-330826d70b23 | -3.84419 | -49.96712 | 2024-11-26 05:01:00 | NOAA-20 | TUCURUÍ | PARÁ | Brasil | 1508100 | 15 | 33 | nan | nan | nan | Amazônia | 0.5 |
| dd5681cb-93b2-3685-b304-fda52e9bcd1b | -2.05599 | -53.23412 | 2024-11-26 05:01:00 | NOAA-20 | PORTO DE MOZ | PARÁ | Brasil | 1505908 | 15 | 33 | nan | nan | nan | Amazônia | 1.6 |
| fc5a9f79-f1a5-349b-a8a6-c1887b06b300 | -5.76565 | -47.81242 | 2024-11-26 05:01:00 | NOAA-20 | SÃO BENTO DO TOCANTINS | TOCANTINS | Brasil | 1720101 | 17 | 33 | nan | nan | nan | Cerrado | 4.3 |
| a309f799-1492-3777-b0b4-18243f3e743d | -3.50312 | -53.81807 | 2024-11-26 05:01:00 | NOAA-20 | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | 0.8 |
| 711acd6f-540a-34bb-b7b0-398c6c5905c7 | -3.50533 | -53.80394 | 2024-11-26 05:01:00 | NOAA-20 | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | 0.4 |
| caf23acb-7a07-3eb6-9184-7c3f65b12720 | -1.90251 | -53.02637 | 2024-11-26 05:01:00 | NOAA-20 | PORTO DE MOZ | PARÁ | Brasil | 1505908 | 15 | 33 | nan | nan | nan | Amazônia | 1.8 |
| 29128dce-e74d-3ee2-83c0-197621c89a58 | -3.17946 | -48.43616 | 2024-11-26 05:01:00 | NOAA-20 | TOMÉ-AÇU | PARÁ | Brasil | 1508001 | 15 | 33 | nan | nan | nan | Amazônia | 33.0 |
| 1a1e3137-01d4-3f02-8986-9bd7f62330a2 | -8.26413 | -49.54346 | 2024-11-26 05:01:00 | NOAA-20 | CONCEIÇÃO DO ARAGUAIA | PARÁ | Brasil | 1502707 | 15 | 33 | nan | nan | nan | Amazônia | 2.6 |
| 34a5281a-449f-3281-9713-e032b00036ad | -2.81087 | -53.0247 | 2024-11-26 05:01:00 | NOAA-20 | MEDICILÂNDIA | PARÁ | Brasil | 1504455 | 15 | 33 | nan | nan | nan | Amazônia | 3.6 |
| 9b3cfc26-b31d-3b0b-a016-53eda6925de7 | -3.96709 | -48.0821 | 2024-11-26 05:01:00 | NOAA-20 | DOM ELISEU | PARÁ | Brasil | 1502939 | 15 | 33 | nan | nan | nan | Amazônia | 27.8 |
| 228de455-102d-3db1-b9b1-e13f4165227c | -3.98139 | -48.04913 | 2024-11-26 05:01:00 | NOAA-20 | DOM ELISEU | PARÁ | Brasil | 1502939 | 15 | 33 | nan | nan | nan | Amazônia | 1.9 |
| 71d5afcf-fa5e-3ae1-9bb4-fb925f7cbe5d | -2.9983 | -53.7399 | 2024-11-26 05:01:00 | NOAA-20 | MEDICILÂNDIA | PARÁ | Brasil | 1504455 | 15 | 33 | nan | nan | nan | Amazônia | 0.4 |
| c0759b9a-8115-343a-9c0a-9f355ff5d9a8 | -3.96779 | -48.07729 | 2024-11-26 05:01:00 | NOAA-20 | DOM ELISEU | PARÁ | Brasil | 1502939 | 15 | 33 | nan | nan | nan | Amazônia | 27.8 |
| 16e0dbe9-1649-3765-a537-7b319201ffbc | -4.54453 | -43.2875 | 2024-11-26 05:01:00 | NOAA-20 | ALDEIAS ALTAS | MARANHÃO | Brasil | 2100303 | 21 | 33 | nan | nan | nan | Cerrado | 8.9 |
| fcae3f6d-6de7-3f6b-95c1-c135bc67f9ba | -3.38234 | -50.10444 | 2024-11-26 05:01:00 | NOAA-20 | PACAJÁ | PARÁ | Brasil | 1505486 | 15 | 33 | nan | nan | nan | Amazônia | 1.0 |
| e77e45c6-f1d9-3de6-b97c-ca335229663d | -3.68808 | -50.22829 | 2024-11-26 05:01:00 | NOAA-20 | PACAJÁ | PARÁ | Brasil | 1505486 | 15 | 33 | nan | nan | nan | Amazônia | 5.9 |
| 5f143853-6836-3461-a7ba-b2f813f6723d | -3.23093 | -53.92759 | 2024-11-26 05:01:00 | NOAA-20 | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | 1.0 |
| d316a941-8562-3f4b-bed2-85e460c375d3 | -1.93671 | -52.09951 | 2024-11-26 05:01:00 | NOAA-20 | PORTO DE MOZ | PARÁ | Brasil | 1505908 | 15 | 33 | nan | nan | nan | Amazônia | 2.0 |
| 68454272-b42e-3c62-ae98-50e825de0db2 | -3.9726 | -48.05617 | 2024-11-26 05:01:00 | NOAA-20 | DOM ELISEU | PARÁ | Brasil | 1502939 | 15 | 33 | nan | nan | nan | Amazônia | 2.2 |
| 4612a521-657b-3937-a2b7-550a6acf26e6 | -4.30934 | -48.08115 | 2024-11-26 05:01:00 | NOAA-20 | RONDON DO PARÁ | PARÁ | Brasil | 1506187 | 15 | 33 | nan | nan | nan | Amazônia | 2.1 |
| fc2c08ee-69cf-3e43-9f47-c680392cc503 | -2.17327 | -53.2668 | 2024-11-26 05:01:00 | NOAA-20 | PRAINHA | PARÁ | Brasil | 1506005 | 15 | 33 | nan | nan | nan | Amazônia | 1.0 |
| b07e2366-d685-321d-9997-7870e7368ed1 | -6.63785 | -47.34911 | 2024-11-26 05:01:00 | NOAA-20 | ESTREITO | MARANHÃO | Brasil | 2104057 | 21 | 33 | nan | nan | nan | Cerrado | 6.8 |
| 5adfab83-5ec8-383d-a556-ed562c13c6da | -3.90772 | -42.42514 | 2024-11-26 05:01:00 | NOAA-20 | CAMPO LARGO DO PIAUÍ | PIAUÍ | Brasil | 2202174 | 22 | 33 | nan | nan | nan | Caatinga | 4.8 |


[Clique aqui para ver as próximas entradas](README41.md)
