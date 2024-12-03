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

## Dados Diários - Página 43

| ID | Latitude | Longitude | Data/Hora GMT | Satélite | Município | Estado | País | Município ID | Estado ID | País ID | Dias sem Chuva | Precipitação | Risco de Fogo | Bioma | FRP |
|----|----------|-----------|---------------|----------|-----------|--------|------|--------------|-----------|---------|----------------|--------------|----------------|-------|-----|
| 2d7570e2-2ba4-3235-95a0-17d034dd29e6 | -2.47073 | -46.58158 | 2024-12-03 04:29:00 | NOAA-20 | NOVA ESPERANÇA DO PIRIÁ | PARÁ | Brasil | 1504950 | 15 | 33 | nan | nan | nan | Amazônia | 0.8 |
| 7a141c55-2d9f-31db-aeba-c62c601cbdaa | -1.72749 | -52.64829 | 2024-12-03 04:29:00 | NOAA-20 | PORTO DE MOZ | PARÁ | Brasil | 1505908 | 15 | 33 | nan | nan | nan | Amazônia | 2.2 |
| d4b9e08b-0d24-33c3-bac5-eb7d9e85ce09 | -3.10893 | -54.05408 | 2024-12-03 04:29:00 | NOAA-20 | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | 2.0 |
| 81f0b617-4e45-3b70-87bb-fe8b3d6291c4 | -4.11913 | -48.53983 | 2024-12-03 04:29:00 | NOAA-20 | RONDON DO PARÁ | PARÁ | Brasil | 1506187 | 15 | 33 | nan | nan | nan | Amazônia | 2.2 |
| 6d8df15a-7151-3fe0-89af-c2a851c1707f | -4.05376 | -46.81859 | 2024-12-03 04:29:00 | NOAA-20 | BOM JARDIM | MARANHÃO | Brasil | 2102002 | 21 | 33 | nan | nan | nan | Amazônia | 1.7 |
| bfd8e4a6-59f9-3d59-9d79-30312d35d9d3 | -3.98657 | -46.66299 | 2024-12-03 04:29:00 | NOAA-20 | BOM JARDIM | MARANHÃO | Brasil | 2102002 | 21 | 33 | nan | nan | nan | Amazônia | 1.5 |
| 10e63e41-8496-3f44-a055-232f9a3f2258 | -3.29833 | -53.66449 | 2024-12-03 04:29:00 | NOAA-20 | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | 47.8 |
| 4750fec3-3cb1-3ec1-ad66-40f16223ef10 | -7.78794 | -45.29041 | 2024-12-03 04:29:00 | NOAA-20 | RIBEIRO GONÇALVES | PIAUÍ | Brasil | 2208908 | 22 | 33 | nan | nan | nan | Cerrado | 0.9 |
| d32abff8-338b-33a3-9b4a-3ea878f7320d | -2.26034 | -53.60767 | 2024-12-03 04:29:00 | NOAA-20 | PRAINHA | PARÁ | Brasil | 1506005 | 15 | 33 | nan | nan | nan | Amazônia | 1.4 |
| 15b6dd64-350b-3078-ae46-b505e31a025f | -3.07907 | -53.09896 | 2024-12-03 04:29:00 | NOAA-20 | MEDICILÂNDIA | PARÁ | Brasil | 1504455 | 15 | 33 | nan | nan | nan | Amazônia | 2.4 |
| 78ac53e1-454c-3fc3-8fff-22f99e0d4aa5 | -3.02172 | -48.02005 | 2024-12-03 04:29:00 | NOAA-20 | IPIXUNA DO PARÁ | PARÁ | Brasil | 1503457 | 15 | 33 | nan | nan | nan | Amazônia | 1.2 |
| fe13afb8-ef01-32c1-b5e3-f11addca2467 | -3.3773 | -45.91037 | 2024-12-03 04:29:00 | NOAA-20 | ZÉ DOCA | MARANHÃO | Brasil | 2114007 | 21 | 33 | nan | nan | nan | Amazônia | 1.6 |
| 96d44066-99cd-30be-8991-56106eed29ce | -2.89295 | -51.79586 | 2024-12-03 04:29:00 | NOAA-20 | SENADOR JOSÉ PORFÍRIO | PARÁ | Brasil | 1507805 | 15 | 33 | nan | nan | nan | Amazônia | 2.3 |
| 1b8daf9e-832b-34be-a973-f7a35d86d632 | -3.99203 | -46.62833 | 2024-12-03 04:29:00 | NOAA-20 | BOM JARDIM | MARANHÃO | Brasil | 2102002 | 21 | 33 | nan | nan | nan | Amazônia | 2.2 |
| a7213502-9eaa-3ba7-89d5-1721dfb836c9 | -4.55814 | -45.72496 | 2024-12-03 04:29:00 | NOAA-20 | SANTA LUZIA | MARANHÃO | Brasil | 2110005 | 21 | 33 | nan | nan | nan | Amazônia | 1.6 |
| 0bcd777c-fdbe-382c-a7f9-1f7602f358cb | -2.54131 | -53.40839 | 2024-12-03 04:29:00 | NOAA-20 | PRAINHA | PARÁ | Brasil | 1506005 | 15 | 33 | nan | nan | nan | Amazônia | 1.7 |
| dbaee3af-6b37-38f7-971e-021b8b957013 | -2.88515 | -45.44813 | 2024-12-03 04:29:00 | NOAA-20 | PEDRO DO ROSÁRIO | MARANHÃO | Brasil | 2108256 | 21 | 33 | nan | nan | nan | Amazônia | 4.8 |
| afda8804-ac8b-344d-a4f9-f1447d3d173e | -3.54211 | -50.17754 | 2024-12-03 04:29:00 | NOAA-20 | PACAJÁ | PARÁ | Brasil | 1505486 | 15 | 33 | nan | nan | nan | Amazônia | 2.9 |
| a762c0bd-1952-3acb-a4f5-01d7cf91777e | -3.89116 | -46.68716 | 2024-12-03 04:29:00 | NOAA-20 | BOM JARDIM | MARANHÃO | Brasil | 2102002 | 21 | 33 | nan | nan | nan | Amazônia | 1.0 |
| 438eef7c-bf48-3b70-9133-a2a7e4afa73f | -3.89609 | -46.67731 | 2024-12-03 04:29:00 | NOAA-20 | BOM JARDIM | MARANHÃO | Brasil | 2102002 | 21 | 33 | nan | nan | nan | Amazônia | 0.9 |
| a49ea4ab-cb29-3ef9-a942-c73ad922c1c6 | -3.03562 | -54.06666 | 2024-12-03 04:29:00 | NOAA-20 | SANTARÉM | PARÁ | Brasil | 1506807 | 15 | 33 | nan | nan | nan | Amazônia | 2.2 |
| 1fcfea47-7eb3-3a45-b95b-1d87ce32ea83 | -2.5513 | -46.566 | 2024-12-03 04:29:00 | NOAA-20 | PARAGOMINAS | PARÁ | Brasil | 1505502 | 15 | 33 | nan | nan | nan | Amazônia | 1.7 |
| e82c943b-6b36-328a-a48f-aec403b383c3 | -3.28597 | -53.71288 | 2024-12-03 04:29:00 | NOAA-20 | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | 5.9 |
| 7cbe95b8-f7b3-3fd6-970a-c2f2b16c1b2e | -5.69499 | -46.59645 | 2024-12-03 04:29:00 | NOAA-20 | AMARANTE DO MARANHÃO | MARANHÃO | Brasil | 2100600 | 21 | 33 | nan | nan | nan | Cerrado | 0.8 |
| 6793b107-29ff-3b35-8026-73c7702e47e4 | -4.22736 | -53.71156 | 2024-12-03 04:29:00 | NOAA-20 | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 1.2 |
| bf0ef4f2-40aa-3e1e-8bf7-fadc9d7b9211 | -3.13468 | -45.98515 | 2024-12-03 04:29:00 | NOAA-20 | ZÉ DOCA | MARANHÃO | Brasil | 2114007 | 21 | 33 | nan | nan | nan | Amazônia | 1.0 |
| d9817858-0be1-367d-b6bf-f6c6162c5880 | -3.29558 | -53.66644 | 2024-12-03 04:29:00 | NOAA-20 | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | 13.7 |
| af75dfbd-4ef7-39f0-a5ce-18d178b3107d | -4.08479 | -47.35632 | 2024-12-03 04:29:00 | NOAA-20 | ULIANÓPOLIS | PARÁ | Brasil | 1508126 | 15 | 33 | nan | nan | nan | Amazônia | 1.7 |
| 799eaa3c-6eb4-39c7-ac3f-723243ac101b | -3.25418 | -53.62463 | 2024-12-03 04:29:00 | NOAA-20 | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | 2.5 |
| 56a33aa2-d6ed-36b7-833b-fb71ca839543 | -2.80139 | -45.94395 | 2024-12-03 04:29:00 | NOAA-20 | NOVA OLINDA DO MARANHÃO | MARANHÃO | Brasil | 2107357 | 21 | 33 | nan | nan | nan | Amazônia | 0.9 |
| 1109ee08-fb57-3995-902a-81b6513dcc89 | -2.56014 | -46.57443 | 2024-12-03 04:29:00 | NOAA-20 | PARAGOMINAS | PARÁ | Brasil | 1505502 | 15 | 33 | nan | nan | nan | Amazônia | 2.3 |
| e9c10558-c7c4-385f-95d0-ac1b456e0298 | -4.32088 | -48.09875 | 2024-12-03 04:29:00 | NOAA-20 | RONDON DO PARÁ | PARÁ | Brasil | 1506187 | 15 | 33 | nan | nan | nan | Amazônia | 5.2 |
| 92c7af55-d175-3069-a618-95cafd90713f | -2.80419 | -45.94796 | 2024-12-03 04:29:00 | NOAA-20 | NOVA OLINDA DO MARANHÃO | MARANHÃO | Brasil | 2107357 | 21 | 33 | nan | nan | nan | Amazônia | 6.4 |
| ec05955b-c656-3cc2-93b3-0c5ba8d9c5a0 | -2.57392 | -46.57304 | 2024-12-03 04:29:00 | NOAA-20 | PARAGOMINAS | PARÁ | Brasil | 1505502 | 15 | 33 | nan | nan | nan | Amazônia | 1.1 |
| 70f4ea9f-03a0-348a-bac5-8ce411ee8399 | -3.255 | -53.93543 | 2024-12-03 04:29:00 | NOAA-20 | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | 1.5 |
| bb191757-8e6f-30ae-8db7-2b8d10aa80d9 | -3.53787 | -50.18108 | 2024-12-03 04:29:00 | NOAA-20 | PACAJÁ | PARÁ | Brasil | 1505486 | 15 | 33 | nan | nan | nan | Amazônia | 1.5 |
| 931dd589-ca8e-388a-98fe-57e72b0a9ab0 | -2.56345 | -46.57494 | 2024-12-03 04:29:00 | NOAA-20 | PARAGOMINAS | PARÁ | Brasil | 1505502 | 15 | 33 | nan | nan | nan | Amazônia | 1.1 |
| 75dee85d-1531-397d-a19f-615ee0eac994 | -2.54958 | -47.37616 | 2024-12-03 04:29:00 | NOAA-20 | IPIXUNA DO PARÁ | PARÁ | Brasil | 1503457 | 15 | 33 | nan | nan | nan | Amazônia | 0.7 |
| 69a1050e-f51f-32d1-a9b4-75eed3dc5289 | -4.05347 | -46.9954 | 2024-12-03 04:29:00 | NOAA-20 | ITINGA DO MARANHÃO | MARANHÃO | Brasil | 2105427 | 21 | 33 | nan | nan | nan | Amazônia | 1.2 |
| 66dca29f-6f57-3172-9b2c-5b20d08ee560 | -2.78329 | -55.37072 | 2024-12-03 04:29:00 | NOAA-20 | SANTARÉM | PARÁ | Brasil | 1506807 | 15 | 33 | nan | nan | nan | Amazônia | 1.6 |
| ffb924bc-856f-3f83-accd-e90a8e6d0ecb | -1.90252 | -52.89465 | 2024-12-03 04:29:00 | NOAA-20 | PORTO DE MOZ | PARÁ | Brasil | 1505908 | 15 | 33 | nan | nan | nan | Amazônia | 1.7 |
| baf21a53-9bd9-3149-9aee-36c99471df1e | -3.32737 | -50.19549 | 2024-12-03 04:29:00 | NOAA-20 | PACAJÁ | PARÁ | Brasil | 1505486 | 15 | 33 | nan | nan | nan | Amazônia | 3.3 |
| 307eaaf3-03c0-3aef-8324-b985569cdd8b | -4.09066 | -48.48061 | 2024-12-03 04:29:00 | NOAA-20 | RONDON DO PARÁ | PARÁ | Brasil | 1506187 | 15 | 33 | nan | nan | nan | Amazônia | 0.8 |
| ea552abb-01b8-32d4-a636-921a8b8a6677 | -3.33812 | -46.05225 | 2024-12-03 04:29:00 | NOAA-20 | ZÉ DOCA | MARANHÃO | Brasil | 2114007 | 21 | 33 | nan | nan | nan | Amazônia | 6.3 |
| adb48855-240b-3c6b-956e-e80526d33797 | -3.81477 | -49.84968 | 2024-12-03 04:29:00 | NOAA-20 | TUCURUÍ | PARÁ | Brasil | 1508100 | 15 | 33 | nan | nan | nan | Amazônia | 2.9 |
| ce9697a6-cb3c-3409-94bb-21e369320e1c | -3.61183 | -42.74429 | 2024-12-03 04:29:00 | NOAA-20 | BREJO | MARANHÃO | Brasil | 2102101 | 21 | 33 | nan | nan | nan | Cerrado | 1.4 |
| f5c56f74-6664-39dd-b25c-48e3248ff63a | -5.80406 | -46.4831 | 2024-12-03 04:29:00 | NOAA-20 | SÍTIO NOVO | MARANHÃO | Brasil | 2111805 | 21 | 33 | nan | nan | nan | Cerrado | 19.6 |
| f9b7f438-a528-31c4-8ddb-d52229f0173b | -2.68234 | -46.61845 | 2024-12-03 04:29:00 | NOAA-20 | CENTRO NOVO DO MARANHÃO | MARANHÃO | Brasil | 2103174 | 21 | 33 | nan | nan | nan | Amazônia | 1.7 |
| 2bc3cfb6-6b50-3106-b964-0e8cdbd841b2 | -1.37173 | -52.41472 | 2024-12-03 04:29:00 | NOAA-20 | ALMEIRIM | PARÁ | Brasil | 1500503 | 15 | 33 | nan | nan | nan | Amazônia | 5.3 |
| 36bdac20-b4d8-39ec-a6e9-700477fc126a | -3.85418 | -46.53213 | 2024-12-03 04:29:00 | NOAA-20 | BOM JARDIM | MARANHÃO | Brasil | 2102002 | 21 | 33 | nan | nan | nan | Amazônia | 1.2 |
| cc6801b9-d1c4-3ac7-a1c2-b6bc4c4195c4 | -3.98582 | -48.19674 | 2024-12-03 04:29:00 | NOAA-20 | DOM ELISEU | PARÁ | Brasil | 1502939 | 15 | 33 | nan | nan | nan | Amazônia | 1.5 |
| 498d79ef-724a-326a-94fc-0a8dc029a5af | -2.75346 | -46.12318 | 2024-12-03 04:29:00 | NOAA-20 | CENTRO NOVO DO MARANHÃO | MARANHÃO | Brasil | 2103174 | 21 | 33 | nan | nan | nan | Amazônia | 1.3 |
| d339b7b1-d4f2-396a-b80b-521f66615894 | -3.10353 | -54.05817 | 2024-12-03 04:29:00 | NOAA-20 | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | 1.9 |
| 8c197368-4043-3cf9-92c4-3e7b28d806b9 | -3.97804 | -47.66794 | 2024-12-03 04:29:00 | NOAA-20 | ULIANÓPOLIS | PARÁ | Brasil | 1508126 | 15 | 33 | nan | nan | nan | Amazônia | 1.7 |
| 1529a5f9-41ee-308e-87a9-af1abbe7a5a9 | -2.7551 | -46.11275 | 2024-12-03 04:29:00 | NOAA-20 | CENTRO NOVO DO MARANHÃO | MARANHÃO | Brasil | 2103174 | 21 | 33 | nan | nan | nan | Amazônia | 1.1 |
| 8ff96387-5948-3d2b-8255-1d0efaa4d087 | -2.54434 | -53.41795 | 2024-12-03 04:29:00 | NOAA-20 | PRAINHA | PARÁ | Brasil | 1506005 | 15 | 33 | nan | nan | nan | Amazônia | 1.3 |
| 777713a9-3f8c-3794-9f79-3047de397b1d | -1.75729 | -52.79123 | 2024-12-03 04:29:00 | NOAA-20 | PORTO DE MOZ | PARÁ | Brasil | 1505908 | 15 | 33 | nan | nan | nan | Amazônia | 1.9 |
| afa73a45-3018-3264-9f93-ee75543f34e8 | -5.11279 | -43.21909 | 2024-12-03 04:29:00 | NOAA-20 | CAXIAS | MARANHÃO | Brasil | 2103000 | 21 | 33 | nan | nan | nan | Cerrado | 11.1 |
| 06b58837-0d3c-3593-b6b3-d6aeeca0db94 | -2.56446 | -46.35265 | 2024-12-03 04:29:00 | NOAA-20 | CENTRO NOVO DO MARANHÃO | MARANHÃO | Brasil | 2103174 | 21 | 33 | nan | nan | nan | Amazônia | 0.6 |
| cba220c6-f38a-3b7b-b003-4adbff13e8ef | -2.33021 | -53.81326 | 2024-12-03 04:29:00 | NOAA-20 | PRAINHA | PARÁ | Brasil | 1506005 | 15 | 33 | nan | nan | nan | Amazônia | 4.0 |
| f8d24959-a2a4-3343-867a-b3bdf7188416 | -3.92988 | -46.7215 | 2024-12-03 04:29:00 | NOAA-20 | BOM JARDIM | MARANHÃO | Brasil | 2102002 | 21 | 33 | nan | nan | nan | Amazônia | 2.3 |
| 0e6a98d6-72a2-3402-b8d5-c62f4d778bab | -2.48522 | -46.5769 | 2024-12-03 04:29:00 | NOAA-20 | NOVA ESPERANÇA DO PIRIÁ | PARÁ | Brasil | 1504950 | 15 | 33 | nan | nan | nan | Amazônia | 1.5 |
| 76f9e938-a5a6-32f1-bfe8-2c5b36bc8d3d | -3.25285 | -53.66096 | 2024-12-03 04:29:00 | NOAA-20 | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | 10.2 |
| 25dc743a-6b67-3b2d-9b97-287cd5f5632d | -3.46905 | -49.92935 | 2024-12-03 04:29:00 | NOAA-20 | PACAJÁ | PARÁ | Brasil | 1505486 | 15 | 33 | nan | nan | nan | Amazônia | 3.7 |
| 1e6ee1a2-6c56-3766-8af3-8f179013d210 | -8.13981 | -44.471 | 2024-12-03 04:29:00 | NOAA-20 | URUÇUÍ | PIAUÍ | Brasil | 2211209 | 22 | 33 | nan | nan | nan | Cerrado | 1.5 |
| 7dc6f44e-63bf-38d1-ad4b-54457fafa380 | -6.66159 | -46.55667 | 2024-12-03 04:29:00 | NOAA-20 | SÍTIO NOVO | MARANHÃO | Brasil | 2111805 | 21 | 33 | nan | nan | nan | Cerrado | 0.9 |
| 80e877b9-9973-3f7d-a7d5-53353a5c5e5a | -1.5667 | -53.47887 | 2024-12-03 04:29:00 | NOAA-20 | PRAINHA | PARÁ | Brasil | 1506005 | 15 | 33 | nan | nan | nan | Amazônia | 1.6 |
| 427976da-f26e-356c-83d8-565eb89672a8 | -2.68727 | -46.60865 | 2024-12-03 04:29:00 | NOAA-20 | CENTRO NOVO DO MARANHÃO | MARANHÃO | Brasil | 2103174 | 21 | 33 | nan | nan | nan | Amazônia | 2.9 |
| 90389338-1396-31ce-ae67-6b799897685e | -4.18707 | -51.1761 | 2024-12-03 04:29:00 | NOAA-20 | ANAPU | PARÁ | Brasil | 1500859 | 15 | 33 | nan | nan | nan | Amazônia | 1.1 |
| 950095da-e41d-35ca-acc5-486324e03fe8 | -3.02943 | -54.19031 | 2024-12-03 04:29:00 | NOAA-20 | SANTARÉM | PARÁ | Brasil | 1506807 | 15 | 33 | nan | nan | nan | Amazônia | 1.8 |
| 65894046-b9cb-37fd-b36c-9406a9f68f4e | -3.25346 | -53.62906 | 2024-12-03 04:29:00 | NOAA-20 | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | 2.5 |
| b81432ff-86e5-38da-8d4d-27245d4eb3ed | -3.84157 | -46.5692 | 2024-12-03 04:29:00 | NOAA-20 | BOM JARDIM | MARANHÃO | Brasil | 2102002 | 21 | 33 | nan | nan | nan | Amazônia | 2.0 |
| 0ec7a7cf-ada2-3ae6-8f54-9a30d6be15c8 | -5.80351 | -46.48663 | 2024-12-03 04:29:00 | NOAA-20 | SÍTIO NOVO | MARANHÃO | Brasil | 2111805 | 21 | 33 | nan | nan | nan | Cerrado | 19.6 |
| d21f42b7-9ed5-3920-9dfd-9531dfbb3803 | -2.80711 | -45.38538 | 2024-12-03 04:29:00 | NOAA-20 | PEDRO DO ROSÁRIO | MARANHÃO | Brasil | 2108256 | 21 | 33 | nan | nan | nan | Amazônia | 0.6 |
| 99d67621-097d-3c79-a708-6b91f15e1b3c | -2.79806 | -45.94343 | 2024-12-03 04:29:00 | NOAA-20 | NOVA OLINDA DO MARANHÃO | MARANHÃO | Brasil | 2107357 | 21 | 33 | nan | nan | nan | Amazônia | 0.9 |
| d5d5f759-d70b-3237-ac02-aecd4785da81 | -3.85363 | -46.53559 | 2024-12-03 04:29:00 | NOAA-20 | BOM JARDIM | MARANHÃO | Brasil | 2102002 | 21 | 33 | nan | nan | nan | Amazônia | 1.2 |
| 49ecf1a4-e90c-3ee4-a26f-f8d2c4d8a526 | -3.85749 | -46.53265 | 2024-12-03 04:29:00 | NOAA-20 | BOM JARDIM | MARANHÃO | Brasil | 2102002 | 21 | 33 | nan | nan | nan | Amazônia | 1.2 |
| ef087fe4-ff16-38e8-9307-ec6d203be13d | -3.03001 | -53.87393 | 2024-12-03 04:29:00 | NOAA-20 | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | 7.3 |
| 298a9c29-ee85-351e-bbf9-cc33df687014 | -2.98202 | -53.88039 | 2024-12-03 04:29:00 | NOAA-20 | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | 1.9 |
| daa589dd-3418-3716-931c-b4c9d38c44ab | -4.16235 | -48.58312 | 2024-12-03 04:29:00 | NOAA-20 | RONDON DO PARÁ | PARÁ | Brasil | 1506187 | 15 | 33 | nan | nan | nan | Amazônia | 1.2 |
| adc49908-a082-3cc5-a948-f149da3f5043 | -2.81486 | -53.05417 | 2024-12-03 04:29:00 | NOAA-20 | MEDICILÂNDIA | PARÁ | Brasil | 1504455 | 15 | 33 | nan | nan | nan | Amazônia | 2.5 |
| 37f16f29-9976-3648-a6b7-b86fa6f4a796 | -3.12691 | -45.99114 | 2024-12-03 04:29:00 | NOAA-20 | ZÉ DOCA | MARANHÃO | Brasil | 2114007 | 21 | 33 | nan | nan | nan | Amazônia | 3.1 |
| 05291520-f0eb-315d-aa6b-c53f734427c5 | -3.34814 | -46.05373 | 2024-12-03 04:29:00 | NOAA-20 | ZÉ DOCA | MARANHÃO | Brasil | 2114007 | 21 | 33 | nan | nan | nan | Amazônia | 3.4 |
| ab637efc-e3fe-33dd-88f3-3d191ede384e | -3.26837 | -50.20827 | 2024-12-03 04:29:00 | NOAA-20 | PACAJÁ | PARÁ | Brasil | 1505486 | 15 | 33 | nan | nan | nan | Amazônia | 1.6 |
| b5008d1a-b052-3daf-b6a5-1c62fdbf042d | -2.35846 | -53.93136 | 2024-12-03 04:29:00 | NOAA-20 | PRAINHA | PARÁ | Brasil | 1506005 | 15 | 33 | nan | nan | nan | Amazônia | 3.6 |
| 66cf0802-b0d0-3d10-81ea-d96ee84fcc3a | -3.98603 | -46.66645 | 2024-12-03 04:29:00 | NOAA-20 | BOM JARDIM | MARANHÃO | Brasil | 2102002 | 21 | 33 | nan | nan | nan | Amazônia | 1.8 |
| eb97752b-04cd-3d36-8586-fe4088485401 | -4.03697 | -46.92544 | 2024-12-03 04:29:00 | NOAA-20 | ITINGA DO MARANHÃO | MARANHÃO | Brasil | 2105427 | 21 | 33 | nan | nan | nan | Amazônia | 2.4 |
| ece8c7c9-88f2-3d51-a927-5bb59a1b4083 | -4.03811 | -48.34205 | 2024-12-03 04:29:00 | NOAA-20 | DOM ELISEU | PARÁ | Brasil | 1502939 | 15 | 33 | nan | nan | nan | Amazônia | 1.0 |
| 1f9a63f4-35d8-3492-927e-a5f5073ee1b3 | -1.72543 | -52.6172 | 2024-12-03 04:29:00 | NOAA-20 | PORTO DE MOZ | PARÁ | Brasil | 1505908 | 15 | 33 | nan | nan | nan | Amazônia | 2.5 |
| 8e8555a8-db23-3ae3-923a-dd9fb0a4d5ce | -4.0466 | -46.82101 | 2024-12-03 04:29:00 | NOAA-20 | BOM JARDIM | MARANHÃO | Brasil | 2102002 | 21 | 33 | nan | nan | nan | Amazônia | 2.1 |
| 8a24c84d-e206-36a4-90d0-32a253752f0d | -5.34833 | -45.09685 | 2024-12-03 04:29:00 | NOAA-20 | BARRA DO CORDA | MARANHÃO | Brasil | 2101608 | 21 | 33 | nan | nan | nan | Cerrado | 0.8 |
| c6b43684-9110-36dd-8f7f-c0e979efc9a4 | -4.00566 | -49.96822 | 2024-12-03 04:29:00 | NOAA-20 | TUCURUÍ | PARÁ | Brasil | 1508100 | 15 | 33 | nan | nan | nan | Amazônia | 1.8 |
| 26dd7c4c-dcdd-386d-9b77-658cbb8838b9 | -4.29309 | -48.209 | 2024-12-03 04:29:00 | NOAA-20 | RONDON DO PARÁ | PARÁ | Brasil | 1506187 | 15 | 33 | nan | nan | nan | Amazônia | 0.9 |
| e87dbe41-8c91-372b-803e-539206fa494c | -3.82392 | -46.57349 | 2024-12-03 04:29:00 | NOAA-20 | BOM JARDIM | MARANHÃO | Brasil | 2102002 | 21 | 33 | nan | nan | nan | Amazônia | 1.0 |
| 70930168-d33a-3da3-9ef4-fc480abdba05 | -4.09507 | -47.42149 | 2024-12-03 04:29:00 | NOAA-20 | ULIANÓPOLIS | PARÁ | Brasil | 1508126 | 15 | 33 | nan | nan | nan | Amazônia | 1.3 |
| 92180fee-2f04-3e3e-9808-8275cedb37b9 | -4.26837 | -47.61425 | 2024-12-03 04:29:00 | NOAA-20 | DOM ELISEU | PARÁ | Brasil | 1502939 | 15 | 33 | nan | nan | nan | Amazônia | 1.2 |
| e6a4cb14-792f-3b99-82c9-76478fa36918 | -3.77178 | -46.66821 | 2024-12-03 04:29:00 | NOAA-20 | BOM JARDIM | MARANHÃO | Brasil | 2102002 | 21 | 33 | nan | nan | nan | Amazônia | 1.0 |
| d8a01716-2247-3a00-8652-ba2fe6052ee2 | -2.56735 | -46.39907 | 2024-12-03 04:29:00 | NOAA-20 | CENTRO NOVO DO MARANHÃO | MARANHÃO | Brasil | 2103174 | 21 | 33 | nan | nan | nan | Amazônia | 1.1 |
| b669e69a-78d9-3c87-9863-d8ccafaff6f7 | -2.67187 | -46.62035 | 2024-12-03 04:29:00 | NOAA-20 | CENTRO NOVO DO MARANHÃO | MARANHÃO | Brasil | 2103174 | 21 | 33 | nan | nan | nan | Amazônia | 2.2 |
| b40ad64e-251e-3ef0-8106-2a69a49d2129 | -2.5902 | -46.57949 | 2024-12-03 04:29:00 | NOAA-20 | PARAGOMINAS | PARÁ | Brasil | 1505502 | 15 | 33 | nan | nan | nan | Amazônia | 2.4 |


[Clique aqui para ver as próximas entradas](README44.md)
