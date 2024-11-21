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
| 30467b82-4047-36e0-8268-9befbb0a1bad | -3.46426 | -54.55941 | 2024-11-21 04:08:00 | NOAA-21 | PLACAS | PARÁ | Brasil | 1505650 | 15 | 33 | nan | nan | nan | Amazônia | 2.8 |
| 13f18fe7-0dc3-3397-97dd-24547c0ec134 | -5.6253 | -43.95112 | 2024-11-21 04:08:00 | NOAA-21 | FORTUNA | MARANHÃO | Brasil | 2104206 | 21 | 33 | nan | nan | nan | Cerrado | 2.0 |
| 6f341ccf-f79b-3516-af2c-753a74b93637 | -1.1775 | -46.72385 | 2024-11-21 04:08:00 | NOAA-21 | BRAGANÇA | PARÁ | Brasil | 1501709 | 15 | 33 | nan | nan | nan | Amazônia | 2.1 |
| b1528547-0768-3143-a73f-11882a0151f2 | -5.01107 | -41.95996 | 2024-11-21 04:08:00 | NOAA-21 | JATOBÁ DO PIAUÍ | PIAUÍ | Brasil | 2205276 | 22 | 33 | nan | nan | nan | Caatinga | 1.3 |
| 5d73ce2f-67a0-321d-8484-d44f6d3b3604 | -6.29982 | -45.33947 | 2024-11-21 04:08:00 | NOAA-21 | FERNANDO FALCÃO | MARANHÃO | Brasil | 2104081 | 21 | 33 | nan | nan | nan | Cerrado | 1.9 |
| 043c0b32-c39b-3cd7-b4f6-4ab9a8499c62 | -2.36805 | -53.83343 | 2024-11-21 04:08:00 | NOAA-21 | PRAINHA | PARÁ | Brasil | 1506005 | 15 | 33 | nan | nan | nan | Amazônia | 3.1 |
| 1ee656f3-1177-39e7-a857-612d86b044ba | -2.63514 | -46.22183 | 2024-11-21 04:08:00 | NOAA-21 | CENTRO DO GUILHERME | MARANHÃO | Brasil | 2103158 | 21 | 33 | nan | nan | nan | Amazônia | 1.2 |
| 278da676-089b-3f3d-9b39-daf0d80dc5f9 | -4.06589 | -50.90114 | 2024-11-21 04:08:00 | NOAA-21 | PACAJÁ | PARÁ | Brasil | 1505486 | 15 | 33 | nan | nan | nan | Amazônia | 1.4 |
| a0850c36-5e93-3f7b-8a11-f49f9aa23fc8 | -3.68245 | -50.21957 | 2024-11-21 04:08:00 | NOAA-21 | PACAJÁ | PARÁ | Brasil | 1505486 | 15 | 33 | nan | nan | nan | Amazônia | 4.3 |
| 5f428389-71a9-3815-9a14-ee4f58e215e3 | -3.11097 | -53.17927 | 2024-11-21 04:08:00 | NOAA-21 | MEDICILÂNDIA | PARÁ | Brasil | 1504455 | 15 | 33 | nan | nan | nan | Amazônia | 2.1 |
| 8280b361-1fe8-3dec-84fd-3f2c8393ff15 | -4.49596 | -46.10199 | 2024-11-21 04:08:00 | NOAA-21 | SANTA LUZIA | MARANHÃO | Brasil | 2110005 | 21 | 33 | nan | nan | nan | Amazônia | 0.8 |
| 30f5ea54-85a4-3da8-8975-3d74c9325a9c | -4.94914 | -47.80568 | 2024-11-21 04:08:00 | NOAA-21 | CIDELÂNDIA | MARANHÃO | Brasil | 2103257 | 21 | 33 | nan | nan | nan | Amazônia | 1.2 |
| 888916d6-fb5c-3cc8-9651-a2f0c76ce3f6 | -3.27618 | -50.57924 | 2024-11-21 04:08:00 | NOAA-21 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 2.2 |
| 944de0ce-187d-3287-b157-ad8387a00680 | -3.40336 | -49.7879 | 2024-11-21 04:08:00 | NOAA-21 | BAIÃO | PARÁ | Brasil | 1501204 | 15 | 33 | nan | nan | nan | Amazônia | 1.8 |
| a6726ea8-7219-3b03-bbfd-b2d58e571b60 | -2.82192 | -49.15613 | 2024-11-21 04:08:00 | NOAA-21 | MOJU | PARÁ | Brasil | 1504703 | 15 | 33 | nan | nan | nan | Amazônia | 1.1 |
| c07e9934-8d16-3728-8bdc-d1f764247799 | -2.14665 | -53.57533 | 2024-11-21 04:08:00 | NOAA-21 | PRAINHA | PARÁ | Brasil | 1506005 | 15 | 33 | nan | nan | nan | Amazônia | 1.8 |
| 2a231b18-c03d-38f8-a33e-fa6a54ff2c0e | -2.16715 | -51.97046 | 2024-11-21 04:08:00 | NOAA-21 | PORTO DE MOZ | PARÁ | Brasil | 1505908 | 15 | 33 | nan | nan | nan | Amazônia | 5.4 |
| 1543e231-7976-3689-b0e8-b467aa647310 | -3.47029 | -50.00731 | 2024-11-21 04:08:00 | NOAA-21 | PACAJÁ | PARÁ | Brasil | 1505486 | 15 | 33 | nan | nan | nan | Amazônia | 5.7 |
| 5873c3e7-1453-3cc5-884b-ccaca72327f0 | -3.45624 | -42.28497 | 2024-11-21 04:08:00 | NOAA-21 | LUZILÂNDIA | PIAUÍ | Brasil | 2205805 | 22 | 33 | nan | nan | nan | Cerrado | 1.6 |
| 17618609-d044-3577-b7b8-34855c55907c | -4.3923 | -45.59502 | 2024-11-21 04:08:00 | NOAA-21 | BREJO DE AREIA | MARANHÃO | Brasil | 2102150 | 21 | 33 | nan | nan | nan | Amazônia | 9.7 |
| 52ab2a3e-f8ac-379a-acd4-cfa6554546e9 | -4.9004 | -48.06874 | 2024-11-21 04:08:00 | NOAA-21 | VILA NOVA DOS MARTÍRIOS | MARANHÃO | Brasil | 2112852 | 21 | 33 | nan | nan | nan | Amazônia | 1.2 |
| fb21ab82-ff48-3c80-b420-e281e2dca466 | -3.53901 | -50.5302 | 2024-11-21 04:08:00 | NOAA-21 | PACAJÁ | PARÁ | Brasil | 1505486 | 15 | 33 | nan | nan | nan | Amazônia | 4.1 |
| 6c4bf966-55cb-3462-b751-1e81902a9e99 | -4.02889 | -43.75023 | 2024-11-21 04:08:00 | NOAA-21 | TIMBIRAS | MARANHÃO | Brasil | 2112100 | 21 | 33 | nan | nan | nan | Cerrado | 1.4 |
| 15914b79-19b3-390a-8107-13c4dad011f3 | -3.72915 | -52.31568 | 2024-11-21 04:08:00 | NOAA-21 | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 3.6 |
| 3767d963-5fbc-31f4-b0a6-06160b5a2b67 | -4.05819 | -50.61238 | 2024-11-21 04:08:00 | NOAA-21 | NOVO REPARTIMENTO | PARÁ | Brasil | 1505064 | 15 | 33 | nan | nan | nan | Amazônia | 2.1 |
| 2fe2724c-7301-32e1-9894-3eff853932c1 | -5.01161 | -41.9565 | 2024-11-21 04:08:00 | NOAA-21 | JATOBÁ DO PIAUÍ | PIAUÍ | Brasil | 2205276 | 22 | 33 | nan | nan | nan | Caatinga | 1.3 |
| fc0fc7ae-b3f4-3b91-8bff-79c508e1cd7a | -2.06703 | -50.14713 | 2024-11-21 04:08:00 | NOAA-21 | BAGRE | PARÁ | Brasil | 1501105 | 15 | 33 | nan | nan | nan | Amazônia | 1.9 |
| 560f92f7-1a09-3a98-818f-43c91200f265 | -4.00957 | -49.12703 | 2024-11-21 04:08:00 | NOAA-21 | BREU BRANCO | PARÁ | Brasil | 1501782 | 15 | 33 | nan | nan | nan | Amazônia | 2.3 |
| 70e4d627-84f0-3906-99b6-cc42fe61c276 | -1.64886 | -52.61217 | 2024-11-21 04:08:00 | NOAA-21 | PORTO DE MOZ | PARÁ | Brasil | 1505908 | 15 | 33 | nan | nan | nan | Amazônia | 2.7 |
| ea25ca72-4f87-3c71-9bc5-68714da9c126 | -2.17884 | -52.13078 | 2024-11-21 04:08:00 | NOAA-21 | PORTO DE MOZ | PARÁ | Brasil | 1505908 | 15 | 33 | nan | nan | nan | Amazônia | 5.4 |
| 664da2da-d142-3899-9663-2d27938fa45f | -2.96292 | -51.01868 | 2024-11-21 04:08:00 | NOAA-21 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 5.9 |
| 3e469ede-01bd-336f-b69b-e89e3fda57e5 | -4.014 | -44.83571 | 2024-11-21 04:08:00 | NOAA-21 | LAGO VERDE | MARANHÃO | Brasil | 2105906 | 21 | 33 | nan | nan | nan | Amazônia | 2.4 |
| 7c6a586b-0b4a-34b3-8002-5b2e4dd952b0 | -5.53902 | -46.36753 | 2024-11-21 04:08:00 | NOAA-21 | AMARANTE DO MARANHÃO | MARANHÃO | Brasil | 2100600 | 21 | 33 | nan | nan | nan | Cerrado | 1.2 |
| 6505d9b1-82f2-3107-bec8-7e8d2c80159c | -2.24848 | -49.205 | 2024-11-21 04:08:00 | NOAA-21 | IGARAPÉ-MIRI | PARÁ | Brasil | 1503309 | 15 | 33 | nan | nan | nan | Amazônia | 1.9 |
| ee9cc7a0-1fdb-3448-b855-3260f9d58444 | -6.29913 | -45.33773 | 2024-11-21 04:08:00 | NOAA-21 | FERNANDO FALCÃO | MARANHÃO | Brasil | 2104081 | 21 | 33 | nan | nan | nan | Cerrado | 3.4 |
| cf3b2dab-b3c2-378b-b347-de0855020a41 | -2.37053 | -53.82878 | 2024-11-21 04:08:00 | NOAA-21 | PRAINHA | PARÁ | Brasil | 1506005 | 15 | 33 | nan | nan | nan | Amazônia | 2.8 |
| a8b48d2f-d787-30ec-9acb-008904888613 | -4.06804 | -46.83654 | 2024-11-21 04:08:00 | NOAA-21 | BOM JARDIM | MARANHÃO | Brasil | 2102002 | 21 | 33 | nan | nan | nan | Amazônia | 1.9 |
| 8ac92711-f421-3674-bb69-1ce9d62ca09c | -3.42044 | -53.28289 | 2024-11-21 04:08:00 | NOAA-21 | MEDICILÂNDIA | PARÁ | Brasil | 1504455 | 15 | 33 | nan | nan | nan | Amazônia | 3.1 |
| 566ae932-b3ae-3080-b3f7-92521271b79e | -2.41922 | -48.97624 | 2024-11-21 04:08:00 | NOAA-21 | MOJU | PARÁ | Brasil | 1504703 | 15 | 33 | nan | nan | nan | Amazônia | 1.3 |
| 7ee1c69c-f58e-3670-b73e-0e06ea618920 | -6.20077 | -37.43789 | 2024-11-21 04:08:00 | NOAA-21 | BELÉM DO BREJO DO CRUZ | PARAÍBA | Brasil | 2502003 | 25 | 33 | nan | nan | nan | Caatinga | 6.1 |
| a3fb65f0-72a7-3cb5-a09f-2118c3ca6fee | -4.63936 | -46.35315 | 2024-11-21 04:08:00 | NOAA-21 | BURITICUPU | MARANHÃO | Brasil | 2102325 | 21 | 33 | nan | nan | nan | Amazônia | 1.6 |
| 13ad6fbf-3384-306a-823c-44b063d981cb | -3.28865 | -49.19688 | 2024-11-21 04:08:00 | NOAA-21 | MOJU | PARÁ | Brasil | 1504703 | 15 | 33 | nan | nan | nan | Amazônia | 1.5 |
| 452eeba2-c1fa-3716-b1f4-2f737d4aa5ab | -2.25001 | -48.16205 | 2024-11-21 04:08:00 | NOAA-21 | TOMÉ-AÇU | PARÁ | Brasil | 1508001 | 15 | 33 | nan | nan | nan | Amazônia | 4.8 |
| e3a3e23b-edb3-3eb0-90af-39abc739f1eb | -5.54546 | -43.90366 | 2024-11-21 04:08:00 | NOAA-21 | FORTUNA | MARANHÃO | Brasil | 2104206 | 21 | 33 | nan | nan | nan | Cerrado | 4.0 |
| 809c8b2d-0acf-3b39-a846-2879833e7167 | -1.1065 | -51.75621 | 2024-11-21 04:08:00 | NOAA-21 | VITÓRIA DO JARI | AMAPÁ | Brasil | 1600808 | 16 | 33 | nan | nan | nan | Amazônia | 1.9 |
| 948a1252-e28d-3653-9bbd-3c0aee054c4b | -3.19355 | -54.32151 | 2024-11-21 04:08:00 | NOAA-21 | MOJUÍ DOS CAMPOS | PARÁ | Brasil | 1504752 | 15 | 33 | nan | nan | nan | Amazônia | 3.1 |
| ada36be8-e060-3c2f-9d99-284233021c50 | -2.73957 | -47.54179 | 2024-11-21 04:08:00 | NOAA-21 | IPIXUNA DO PARÁ | PARÁ | Brasil | 1503457 | 15 | 33 | nan | nan | nan | Amazônia | 2.8 |
| 6ab7065a-2f32-3a4d-9d6f-c5ac8f50dd11 | -2.58737 | -51.72094 | 2024-11-21 04:08:00 | NOAA-21 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 1.3 |
| b253560d-9cb1-3130-bf0c-eab9d6c465d0 | -6.2732 | -44.77877 | 2024-11-21 04:08:00 | NOAA-21 | MIRADOR | MARANHÃO | Brasil | 2106706 | 21 | 33 | nan | nan | nan | Cerrado | 0.8 |
| c7e90510-86bd-3aed-8985-1db195aa24c0 | -4.10291 | -50.7458 | 2024-11-21 04:08:00 | NOAA-21 | PACAJÁ | PARÁ | Brasil | 1505486 | 15 | 33 | nan | nan | nan | Amazônia | 0.8 |
| 4d0051fd-3816-3733-ad2d-f360fa39f3a8 | -4.24355 | -46.11754 | 2024-11-21 04:08:00 | NOAA-21 | SANTA LUZIA | MARANHÃO | Brasil | 2110005 | 21 | 33 | nan | nan | nan | Amazônia | 3.2 |
| 001960c0-2d37-39aa-be68-f3546db9804c | -3.41954 | -53.28819 | 2024-11-21 04:08:00 | NOAA-21 | MEDICILÂNDIA | PARÁ | Brasil | 1504455 | 15 | 33 | nan | nan | nan | Amazônia | 6.2 |
| ad8b55fd-e2aa-37ec-b595-7902da8efecd | -4.31569 | -43.70629 | 2024-11-21 04:08:00 | NOAA-21 | CODÓ | MARANHÃO | Brasil | 2103307 | 21 | 33 | nan | nan | nan | Cerrado | 2.4 |
| fa1a0e20-3657-3fd1-8161-d85af0239f4f | -0.29336 | -51.60789 | 2024-11-21 04:08:00 | NOAA-21 | MAZAGÃO | AMAPÁ | Brasil | 1600402 | 16 | 33 | nan | nan | nan | Amazônia | 1.5 |
| 9c1972c8-9941-355e-82dc-b3132cd71344 | -2.84782 | -49.15589 | 2024-11-21 04:08:00 | NOAA-21 | MOJU | PARÁ | Brasil | 1504703 | 15 | 33 | nan | nan | nan | Amazônia | 2.7 |
| 395a6c76-8ef1-3188-984f-b3c5b08994f6 | -2.40301 | -47.64237 | 2024-11-21 04:08:00 | NOAA-21 | IPIXUNA DO PARÁ | PARÁ | Brasil | 1503457 | 15 | 33 | nan | nan | nan | Amazônia | 1.3 |
| f7b500d3-a0f0-3414-a96b-f8dde20ccdf0 | -2.69763 | -46.24676 | 2024-11-21 04:08:00 | NOAA-21 | CENTRO NOVO DO MARANHÃO | MARANHÃO | Brasil | 2103174 | 21 | 33 | nan | nan | nan | Amazônia | 2.3 |
| 6a052519-8000-3734-ad51-850a49c90189 | -1.13934 | -53.67022 | 2024-11-21 04:08:00 | NOAA-21 | PRAINHA | PARÁ | Brasil | 1506005 | 15 | 33 | nan | nan | nan | Amazônia | 3.2 |
| 9df9289b-c0eb-34e3-8417-c63102ce627a | -2.768 | -52.11032 | 2024-11-21 04:08:00 | NOAA-21 | PORTO DE MOZ | PARÁ | Brasil | 1505908 | 15 | 33 | nan | nan | nan | Amazônia | 4.4 |
| c3de94e8-e13a-3289-9f93-1781c8c75f99 | -3.27782 | -53.83678 | 2024-11-21 04:08:00 | NOAA-21 | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | 7.1 |
| dfdc96b6-a1da-3781-879a-a093ded9e9ac | -4.64338 | -46.35377 | 2024-11-21 04:08:00 | NOAA-21 | BURITICUPU | MARANHÃO | Brasil | 2102325 | 21 | 33 | nan | nan | nan | Amazônia | 0.6 |
| c90f4ce7-5884-384c-9dcd-8a1bf5e3a638 | -5.10682 | -43.16837 | 2024-11-21 04:08:00 | NOAA-21 | CAXIAS | MARANHÃO | Brasil | 2103000 | 21 | 33 | nan | nan | nan | Cerrado | 7.4 |
| a89822e4-ed10-35f3-b87a-6a4814d958e4 | -2.63632 | -46.21449 | 2024-11-21 04:08:00 | NOAA-21 | CENTRO DO GUILHERME | MARANHÃO | Brasil | 2103158 | 21 | 33 | nan | nan | nan | Amazônia | 2.2 |
| 519dd680-80a3-3227-ad37-29e03caf62ac | -4.60763 | -45.74045 | 2024-11-21 04:08:00 | NOAA-21 | MARAJÁ DO SENA | MARANHÃO | Brasil | 2106359 | 21 | 33 | nan | nan | nan | Amazônia | 1.8 |
| 5914367a-434b-37d8-9d82-53625994671a | -1.59387 | -50.44082 | 2024-11-21 04:08:00 | NOAA-21 | BREVES | PARÁ | Brasil | 1501808 | 15 | 33 | nan | nan | nan | Amazônia | 2.7 |
| d1f58009-4a0b-381e-8ccd-074e351726ea | -2.95521 | -48.33275 | 2024-11-21 04:08:00 | NOAA-21 | TOMÉ-AÇU | PARÁ | Brasil | 1508001 | 15 | 33 | nan | nan | nan | Amazônia | 5.9 |
| 12039e19-2199-3c7a-8dcd-be17c266b091 | -5.02085 | -43.44624 | 2024-11-21 04:08:00 | NOAA-21 | CAXIAS | MARANHÃO | Brasil | 2103000 | 21 | 33 | nan | nan | nan | Cerrado | 2.0 |
| c8354524-36c7-3868-b878-2b37b0b040a6 | -3.57493 | -50.41494 | 2024-11-21 04:08:00 | NOAA-21 | PACAJÁ | PARÁ | Brasil | 1505486 | 15 | 33 | nan | nan | nan | Amazônia | 8.0 |
| a773e2ad-e9d8-3c92-888e-37e235776c23 | -2.24854 | -46.82773 | 2024-11-21 04:08:00 | NOAA-21 | NOVA ESPERANÇA DO PIRIÁ | PARÁ | Brasil | 1504950 | 15 | 33 | nan | nan | nan | Amazônia | 1.2 |
| c2462e09-ba7d-37f3-be55-f7a0e055228a | -1.7866 | -45.9682 | 2024-11-21 04:08:00 | NOAA-21 | AMAPÁ DO MARANHÃO | MARANHÃO | Brasil | 2100550 | 21 | 33 | nan | nan | nan | Amazônia | 2.2 |
| d569c7ff-5e1a-38c0-8dd9-7eefe6072e83 | -4.47767 | -44.75219 | 2024-11-21 04:08:00 | NOAA-21 | IGARAPÉ GRANDE | MARANHÃO | Brasil | 2105203 | 21 | 33 | nan | nan | nan | Cerrado | 1.9 |
| b17f570c-fcc9-3707-a390-9f46a8f35684 | -3.28818 | -53.85668 | 2024-11-21 04:08:00 | NOAA-21 | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | 7.5 |
| 340fc714-d258-3601-82d8-bed9ee8f634c | -6.12079 | -42.51718 | 2024-11-21 04:08:00 | NOAA-21 | JARDIM DO MULATO | PIAUÍ | Brasil | 2205250 | 22 | 33 | nan | nan | nan | Caatinga | 13.0 |
| f056e909-a089-3b4b-a95c-e8ebb763faac | -2.62939 | -51.92679 | 2024-11-21 04:08:00 | NOAA-21 | SENADOR JOSÉ PORFÍRIO | PARÁ | Brasil | 1507805 | 15 | 33 | nan | nan | nan | Amazônia | 1.0 |
| bef5808b-e843-3f61-a092-36c0f8400633 | -3.37855 | -52.45362 | 2024-11-21 04:08:00 | NOAA-21 | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 9.3 |
| 4d4a0f42-4d94-36e9-991e-4cbf594a9a7c | -3.81848 | -51.35572 | 2024-11-21 04:08:00 | NOAA-21 | ANAPU | PARÁ | Brasil | 1500859 | 15 | 33 | nan | nan | nan | Amazônia | 1.5 |
| 913ba119-1f92-330e-aac1-dcfa46285056 | -3.59375 | -43.63649 | 2024-11-21 04:08:00 | NOAA-21 | NINA RODRIGUES | MARANHÃO | Brasil | 2107209 | 21 | 33 | nan | nan | nan | Cerrado | 4.2 |
| 43fcd602-acc8-3959-8269-7550734b6861 | -5.45621 | -46.48549 | 2024-11-21 04:08:00 | NOAA-21 | AMARANTE DO MARANHÃO | MARANHÃO | Brasil | 2100600 | 21 | 33 | nan | nan | nan | Cerrado | 1.6 |
| ec74d2ce-e53d-3c89-baeb-63116bf82e46 | -2.72306 | -46.09043 | 2024-11-21 04:08:00 | NOAA-21 | CENTRO NOVO DO MARANHÃO | MARANHÃO | Brasil | 2103174 | 21 | 33 | nan | nan | nan | Amazônia | 2.4 |
| 52b0c2a2-0747-3f20-b609-c2fd90fe750f | -3.28921 | -53.85072 | 2024-11-21 04:08:00 | NOAA-21 | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | 7.5 |
| c603c89f-b7c5-38b3-abd1-b3f90bf45ef8 | -3.49783 | -50.44482 | 2024-11-21 04:08:00 | NOAA-21 | PACAJÁ | PARÁ | Brasil | 1505486 | 15 | 33 | nan | nan | nan | Amazônia | 2.6 |
| 4db8bb41-4278-3023-9026-ac3c39768c93 | -0.79937 | -51.78754 | 2024-11-21 04:08:00 | NOAA-21 | MAZAGÃO | AMAPÁ | Brasil | 1600402 | 16 | 33 | nan | nan | nan | Amazônia | 2.7 |
| 3addfc9e-956d-381c-a8c6-b7119be4af6b | -3.54233 | -50.1925 | 2024-11-21 04:08:00 | NOAA-21 | PACAJÁ | PARÁ | Brasil | 1505486 | 15 | 33 | nan | nan | nan | Amazônia | 1.1 |
| 5c510256-b5c7-3efa-93ca-e19d11f0ecb2 | -2.33307 | -45.66555 | 2024-11-21 04:08:00 | NOAA-21 | TURILÂNDIA | MARANHÃO | Brasil | 2112456 | 21 | 33 | nan | nan | nan | Amazônia | 1.5 |
| 19037353-34d4-332e-b69a-8f140a3705b7 | -3.0655 | -53.28964 | 2024-11-21 04:08:00 | NOAA-21 | MEDICILÂNDIA | PARÁ | Brasil | 1504455 | 15 | 33 | nan | nan | nan | Amazônia | 5.4 |
| a17f82b0-19f8-3c33-a19a-e56a4a2f2ba8 | -3.47008 | -47.68377 | 2024-11-21 04:08:00 | NOAA-21 | PARAGOMINAS | PARÁ | Brasil | 1505502 | 15 | 33 | nan | nan | nan | Amazônia | 2.0 |
| d0a69545-088e-32ab-aff8-ed9a30bed336 | -0.93553 | -51.72229 | 2024-11-21 04:08:00 | NOAA-21 | VITÓRIA DO JARI | AMAPÁ | Brasil | 1600808 | 16 | 33 | nan | nan | nan | Amazônia | 1.8 |
| ba567744-dfee-3a0e-95c4-c15fa9e20e5c | -6.55974 | -41.97483 | 2024-11-21 04:08:00 | NOAA-21 | NOVO ORIENTE DO PIAUÍ | PIAUÍ | Brasil | 2206902 | 22 | 33 | nan | nan | nan | Caatinga | 1.6 |
| 1cdefd83-4c38-37b7-84e0-82dd7bd9d351 | -3.07219 | -49.19872 | 2024-11-21 04:08:00 | NOAA-21 | MOJU | PARÁ | Brasil | 1504703 | 15 | 33 | nan | nan | nan | Amazônia | 7.1 |
| c1bb0da5-59a0-3d76-b7b1-e91f8bc8ba14 | -3.54753 | -51.43498 | 2024-11-21 04:08:00 | NOAA-21 | ANAPU | PARÁ | Brasil | 1500859 | 15 | 33 | nan | nan | nan | Amazônia | 3.6 |
| 754fbb47-19e0-3b47-b598-8aef1dbb8784 | -2.62584 | -48.4849 | 2024-11-21 04:08:00 | NOAA-21 | TAILÂNDIA | PARÁ | Brasil | 1507953 | 15 | 33 | nan | nan | nan | Amazônia | 2.6 |
| 05be070a-d0cc-332a-8223-f7ca93c36f27 | -2.67857 | -46.24013 | 2024-11-21 04:08:00 | NOAA-21 | CENTRO NOVO DO MARANHÃO | MARANHÃO | Brasil | 2103174 | 21 | 33 | nan | nan | nan | Amazônia | 1.6 |
| 8df25f3f-89e7-3d78-bfd0-d55bb477bdd6 | -4.6399 | -49.5453 | 2024-11-21 04:08:00 | NOAA-21 | NOVO REPARTIMENTO | PARÁ | Brasil | 1505064 | 15 | 33 | nan | nan | nan | Amazônia | 8.9 |
| aa206eeb-ffd2-396d-9120-06621ce8fef9 | -3.64738 | -52.35503 | 2024-11-21 04:08:00 | NOAA-21 | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 1.3 |
| d57dc7b6-89ee-36d0-b6cb-4e9a436d0ce1 | -4.97689 | -48.45499 | 2024-11-21 04:08:00 | NOAA-21 | ABEL FIGUEIREDO | PARÁ | Brasil | 1500131 | 15 | 33 | nan | nan | nan | Amazônia | 1.7 |
| 3ee404d7-2142-38d0-88ab-a5c42a81fdbe | -3.10816 | -50.20118 | 2024-11-21 04:08:00 | NOAA-21 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 2.1 |
| 5d507750-3e40-30b9-9716-20aad9fce084 | -3.29843 | -50.36784 | 2024-11-21 04:08:00 | NOAA-21 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 3.6 |
| ed944c54-8336-3a5f-93b7-0f697e3d3366 | -4.34477 | -46.13749 | 2024-11-21 04:08:00 | NOAA-21 | SANTA LUZIA | MARANHÃO | Brasil | 2110005 | 21 | 33 | nan | nan | nan | Amazônia | 3.4 |
| a021827c-f20d-3083-b698-534985ac4e2f | -4.48843 | -47.93942 | 2024-11-21 04:08:00 | NOAA-21 | RONDON DO PARÁ | PARÁ | Brasil | 1506187 | 15 | 33 | nan | nan | nan | Amazônia | 2.3 |
| 999f7bc4-5547-3cbd-b6e2-0b1626a86aa2 | -2.93069 | -45.2728 | 2024-11-21 04:08:00 | NOAA-21 | PEDRO DO ROSÁRIO | MARANHÃO | Brasil | 2108256 | 21 | 33 | nan | nan | nan | Amazônia | 1.2 |


[Clique aqui para ver as próximas entradas](README20.md)
