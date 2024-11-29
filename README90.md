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

## Dados Diários - Página 90

| ID | Latitude | Longitude | Data/Hora GMT | Satélite | Município | Estado | País | Município ID | Estado ID | País ID | Dias sem Chuva | Precipitação | Risco de Fogo | Bioma | FRP |
|----|----------|-----------|---------------|----------|-----------|--------|------|--------------|-----------|---------|----------------|--------------|----------------|-------|-----|
| 923a9902-465b-32f6-8801-bcac68687913 | -2.56405 | -49.07662 | 2024-11-29 05:22:00 | NPP-375D | MOJU | PARÁ | Brasil | 1504703 | 15 | 33 | nan | nan | nan | Amazônia | 0.6 |
| 7e8d081d-9ad5-3084-8af0-6f0bc3e978d6 | -4.00831 | -53.72683 | 2024-11-29 05:22:00 | NPP-375D | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | 2.4 |
| 492756b7-359b-356b-9a2c-46bc1d432944 | -3.37961 | -50.11576 | 2024-11-29 05:22:00 | NPP-375D | PACAJÁ | PARÁ | Brasil | 1505486 | 15 | 33 | nan | nan | nan | Amazônia | 2.9 |
| ef98c1bc-b1ac-30b4-a460-fd127953ed68 | -4.07469 | -50.03032 | 2024-11-29 05:22:00 | NPP-375D | NOVO REPARTIMENTO | PARÁ | Brasil | 1505064 | 15 | 33 | nan | nan | nan | Amazônia | 5.2 |
| 44c929b0-6bf9-3111-8e5a-c47eed6d5507 | -2.86161 | -53.99879 | 2024-11-29 05:22:00 | NPP-375D | PRAINHA | PARÁ | Brasil | 1506005 | 15 | 33 | nan | nan | nan | Amazônia | 2.1 |
| 0732c083-adf3-3b2b-abb0-aa3c168a7cdf | -3.59071 | -50.35842 | 2024-11-29 05:22:00 | NPP-375D | PACAJÁ | PARÁ | Brasil | 1505486 | 15 | 33 | nan | nan | nan | Amazônia | 1.1 |
| ff63e2b7-2fba-36db-8f8c-699324477231 | -2.85493 | -46.82894 | 2024-11-29 05:22:00 | NPP-375D | PARAGOMINAS | PARÁ | Brasil | 1505502 | 15 | 33 | nan | nan | nan | Amazônia | 3.0 |
| a9a71c59-d05b-3880-aa70-77acd18ef244 | -3.05465 | -52.75955 | 2024-11-29 05:22:00 | NPP-375D | BRASIL NOVO | PARÁ | Brasil | 1501725 | 15 | 33 | nan | nan | nan | Amazônia | 1.9 |
| f8665c23-f612-357a-91dc-e6bb7facfc6c | -2.16758 | -53.66075 | 2024-11-29 05:22:00 | NPP-375D | PRAINHA | PARÁ | Brasil | 1506005 | 15 | 33 | nan | nan | nan | Amazônia | 1.5 |
| 1197a1e2-f5b3-3432-b052-e574cc0561d7 | -2.83061 | -54.12036 | 2024-11-29 05:22:00 | NPP-375D | SANTARÉM | PARÁ | Brasil | 1506807 | 15 | 33 | nan | nan | nan | Amazônia | 1.7 |
| b19a59e7-a910-3133-b271-69390263debf | -3.09106 | -54.13424 | 2024-11-29 05:22:00 | NPP-375D | SANTARÉM | PARÁ | Brasil | 1506807 | 15 | 33 | nan | nan | nan | Amazônia | 2.7 |
| 7c421c8d-eb58-3c0d-aa11-257def65dd82 | -2.59854 | -53.97303 | 2024-11-29 05:22:00 | NPP-375D | PRAINHA | PARÁ | Brasil | 1506005 | 15 | 33 | nan | nan | nan | Amazônia | 1.5 |
| 0a7076eb-31ca-30a7-a32c-a02ed7c0f5d6 | -2.91105 | -54.18321 | 2024-11-29 05:22:00 | NPP-375D | SANTARÉM | PARÁ | Brasil | 1506807 | 15 | 33 | nan | nan | nan | Amazônia | 1.5 |
| fbb699a5-8f5c-323b-b642-ee010bff9634 | -3.21708 | -54.06804 | 2024-11-29 05:22:00 | NPP-375D | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | 0.5 |
| 8e8d2c38-0937-35b5-a137-587d2e75e1ed | -2.5786 | -49.99405 | 2024-11-29 05:22:00 | NPP-375D | BAGRE | PARÁ | Brasil | 1501105 | 15 | 33 | nan | nan | nan | Amazônia | 3.2 |
| b389078a-2ff1-30e2-8e87-34d2816beb0a | -3.10551 | -53.80537 | 2024-11-29 05:22:00 | NPP-375D | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | 4.9 |
| 88bca8aa-2dd0-38b3-95bb-1ecf360ddc2b | -1.66654 | -52.73611 | 2024-11-29 05:22:00 | NPP-375D | PORTO DE MOZ | PARÁ | Brasil | 1505908 | 15 | 33 | nan | nan | nan | Amazônia | 2.9 |
| e76013ec-ee8b-3faf-a322-18ff931fb304 | -1.44002 | -55.21224 | 2024-11-29 05:22:00 | NPP-375D | ALENQUER | PARÁ | Brasil | 1500404 | 15 | 33 | nan | nan | nan | Amazônia | 1.8 |
| 0eb362e5-7caa-3cac-8595-ff9cce7f7139 | -1.93977 | -52.95641 | 2024-11-29 05:22:00 | NPP-375D | PORTO DE MOZ | PARÁ | Brasil | 1505908 | 15 | 33 | nan | nan | nan | Amazônia | 1.8 |
| 275f9df6-2629-3d24-bc77-bc2fc3f40782 | -3.10305 | -53.80633 | 2024-11-29 05:22:00 | NPP-375D | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | 3.0 |
| 4edb4150-b884-3113-8e46-816021815f67 | -3.86764 | -48.3645 | 2024-11-29 05:22:00 | NPP-375D | DOM ELISEU | PARÁ | Brasil | 1502939 | 15 | 33 | nan | nan | nan | Amazônia | 2.2 |
| 6712861b-43a5-3c50-8190-cf3d17845883 | -2.81923 | -51.79232 | 2024-11-29 05:22:00 | NPP-375D | SENADOR JOSÉ PORFÍRIO | PARÁ | Brasil | 1507805 | 15 | 33 | nan | nan | nan | Amazônia | 1.9 |
| 6d1d9f7e-ae82-3c00-933b-9204f86babc9 | -4.48583 | -48.11674 | 2024-11-29 05:22:00 | NPP-375D | RONDON DO PARÁ | PARÁ | Brasil | 1506187 | 15 | 33 | nan | nan | nan | Amazônia | 4.2 |
| 53a67a67-fdc0-3567-90ec-ec6b6fd99eea | -2.25986 | -53.67755 | 2024-11-29 05:22:00 | NPP-375D | PRAINHA | PARÁ | Brasil | 1506005 | 15 | 33 | nan | nan | nan | Amazônia | 2.8 |
| 1bb57a07-293e-3059-9a43-038225da314a | -1.71088 | -54.98821 | 2024-11-29 05:22:00 | NPP-375D | ALENQUER | PARÁ | Brasil | 1500404 | 15 | 33 | nan | nan | nan | Amazônia | 1.4 |
| 850e8bb6-fb56-3701-a091-54f6b6c2f215 | -2.46586 | -53.96912 | 2024-11-29 05:22:00 | NPP-375D | PRAINHA | PARÁ | Brasil | 1506005 | 15 | 33 | nan | nan | nan | Amazônia | 2.6 |
| d7fe61fa-9a41-3f31-b822-3043fbfc0b8a | -2.5775 | -50.00128 | 2024-11-29 05:22:00 | NPP-375D | BAGRE | PARÁ | Brasil | 1501105 | 15 | 33 | nan | nan | nan | Amazônia | 9.7 |
| 085db13c-aa9c-3ae3-92e1-6507f7dc683d | -2.37193 | -56.1155 | 2024-11-29 05:22:00 | NPP-375D | JURUTI | PARÁ | Brasil | 1503903 | 15 | 33 | nan | nan | nan | Amazônia | 1.5 |
| f328bbd0-c353-388e-9917-64dfcd00e353 | -2.44596 | -53.62183 | 2024-11-29 05:22:00 | NPP-375D | PRAINHA | PARÁ | Brasil | 1506005 | 15 | 33 | nan | nan | nan | Amazônia | 1.6 |
| dca0cfed-0bb2-3146-9f7b-79cda9a12ab7 | -3.21731 | -54.17991 | 2024-11-29 05:22:00 | NPP-375D | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | 0.9 |
| 9be85fde-85c6-3448-bbde-f3fb7b5f2a9e | -3.50942 | -62.85124 | 2024-11-29 05:22:00 | NPP-375D | CODAJÁS | AMAZONAS | Brasil | 1301308 | 13 | 33 | nan | nan | nan | Amazônia | 1.6 |
| adede69b-d910-3bfe-9424-f90255728c15 | -3.34528 | -50.23341 | 2024-11-29 05:22:00 | NPP-375D | PACAJÁ | PARÁ | Brasil | 1505486 | 15 | 33 | nan | nan | nan | Amazônia | 1.3 |
| f4c9387c-c595-3324-843b-39b6da92b7a7 | -3.22151 | -54.18054 | 2024-11-29 05:22:00 | NPP-375D | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | 5.3 |
| 7ae880c3-e6f1-3403-8693-336c69ff5f7c | -3.49438 | -53.80331 | 2024-11-29 05:22:00 | NPP-375D | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | 1.8 |
| 79a415a4-3e49-3fe7-b3c1-4f58b46e1750 | -2.25535 | -53.46181 | 2024-11-29 05:22:00 | NPP-375D | PRAINHA | PARÁ | Brasil | 1506005 | 15 | 33 | nan | nan | nan | Amazônia | 1.9 |
| 80ef5197-6889-3886-bd85-8a943431c035 | -2.21372 | -52.48138 | 2024-11-29 05:22:00 | NPP-375D | PORTO DE MOZ | PARÁ | Brasil | 1505908 | 15 | 33 | nan | nan | nan | Amazônia | 2.3 |
| 0e6dd770-143b-3be0-bb7b-66ab40473a73 | -3.53011 | -50.19429 | 2024-11-29 05:22:00 | NPP-375D | PACAJÁ | PARÁ | Brasil | 1505486 | 15 | 33 | nan | nan | nan | Amazônia | 0.8 |
| 9d2088f3-3455-3896-9981-fff1402383a4 | -1.67956 | -52.52567 | 2024-11-29 05:22:00 | NPP-375D | PORTO DE MOZ | PARÁ | Brasil | 1505908 | 15 | 33 | nan | nan | nan | Amazônia | 2.1 |
| 2ab7122b-1153-3c28-83d2-40a042e5755a | -4.04102 | -50.88399 | 2024-11-29 05:22:00 | NPP-375D | PACAJÁ | PARÁ | Brasil | 1505486 | 15 | 33 | nan | nan | nan | Amazônia | 1.8 |
| 8a69fcf5-8108-3725-8b8f-85fc85a406b9 | -2.01656 | -51.1951 | 2024-11-29 05:22:00 | NPP-375D | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 2.5 |
| 735380cb-9fae-3915-92ab-3f1f4f56b3b4 | -2.87123 | -53.99231 | 2024-11-29 05:22:00 | NPP-375D | PRAINHA | PARÁ | Brasil | 1506005 | 15 | 33 | nan | nan | nan | Amazônia | 3.2 |
| ea25f4ce-8a1a-33f5-b864-38291321e32d | -3.17762 | -54.32821 | 2024-11-29 05:22:00 | NPP-375D | MOJUÍ DOS CAMPOS | PARÁ | Brasil | 1504752 | 15 | 33 | nan | nan | nan | Amazônia | 2.1 |
| 6712d111-5180-344b-ac60-733225d6aa74 | -3.20075 | -46.56926 | 2024-11-29 05:22:00 | NPP-375D | CENTRO NOVO DO MARANHÃO | MARANHÃO | Brasil | 2103174 | 21 | 33 | nan | nan | nan | Amazônia | 12.6 |
| 42b51b84-9a5d-3ffd-9e1f-6829b82aafc4 | -4.09335 | -54.76714 | 2024-11-29 05:22:00 | NPP-375D | PLACAS | PARÁ | Brasil | 1505650 | 15 | 33 | nan | nan | nan | Amazônia | 0.9 |
| cf25fb15-3062-382a-80ad-c4be73ceeb31 | -1.32369 | -55.83482 | 2024-11-29 05:22:00 | NPP-375D | ORIXIMINÁ | PARÁ | Brasil | 1505304 | 15 | 33 | nan | nan | nan | Amazônia | 1.6 |
| 6a854c5b-5ce8-3a99-9a6c-5530aa745d9a | -1.68673 | -52.42697 | 2024-11-29 05:22:00 | NPP-375D | PORTO DE MOZ | PARÁ | Brasil | 1505908 | 15 | 33 | nan | nan | nan | Amazônia | 5.0 |
| 8def404d-4b0e-3db7-90b3-bd5a749943eb | -2.84223 | -46.82066 | 2024-11-29 05:22:00 | NPP-375D | PARAGOMINAS | PARÁ | Brasil | 1505502 | 15 | 33 | nan | nan | nan | Amazônia | 2.8 |
| 30127aed-4eae-3add-b3bf-e365b6a9ff1a | -3.58069 | -52.06335 | 2024-11-29 05:22:00 | NPP-375D | SENADOR JOSÉ PORFÍRIO | PARÁ | Brasil | 1507805 | 15 | 33 | nan | nan | nan | Amazônia | 1.0 |
| 44a4320e-bde5-337d-b872-23b94e5791a8 | -2.84792 | -54.03247 | 2024-11-29 05:22:00 | NPP-375D | PRAINHA | PARÁ | Brasil | 1506005 | 15 | 33 | nan | nan | nan | Amazônia | 3.3 |
| 30d7a4f7-9439-3780-880f-b8f8d47bcde6 | -1.62644 | -53.87978 | 2024-11-29 05:22:00 | NPP-375D | PRAINHA | PARÁ | Brasil | 1506005 | 15 | 33 | nan | nan | nan | Amazônia | 2.1 |
| edc06ed3-7367-38bd-b50c-09348285151b | -3.06839 | -53.91646 | 2024-11-29 05:22:00 | NPP-375D | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | 2.6 |
| 7abbc4e9-78db-34f0-ab6a-e7bfe0d32aa0 | -1.60639 | -55.38035 | 2024-11-29 05:22:00 | NPP-375D | ÓBIDOS | PARÁ | Brasil | 1505106 | 15 | 33 | nan | nan | nan | Amazônia | 1.2 |
| 8b3b0814-d83b-303a-8d70-d56a3e970571 | -3.34795 | -53.73972 | 2024-11-29 05:22:00 | NPP-375D | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | 1.4 |
| 38cfe0ad-0a41-36d4-9c22-8535665fcbf7 | -2.94734 | -51.58352 | 2024-11-29 05:22:00 | NPP-375D | ANAPU | PARÁ | Brasil | 1500859 | 15 | 33 | nan | nan | nan | Amazônia | 1.8 |
| 6ddc2473-678d-35f4-98f3-541a4845459e | -2.60509 | -54.21828 | 2024-11-29 05:22:00 | NPP-375D | PRAINHA | PARÁ | Brasil | 1506005 | 15 | 33 | nan | nan | nan | Amazônia | 2.3 |
| b66bd730-84db-3db0-89d2-3706f20eda46 | -2.8389 | -54.11766 | 2024-11-29 05:22:00 | NPP-375D | SANTARÉM | PARÁ | Brasil | 1506807 | 15 | 33 | nan | nan | nan | Amazônia | 2.1 |
| c454d8a4-e622-3205-8bd2-0c1bac3c47b1 | -1.5269 | -55.37046 | 2024-11-29 05:22:00 | NPP-375D | ÓBIDOS | PARÁ | Brasil | 1505106 | 15 | 33 | nan | nan | nan | Amazônia | 0.9 |
| 8fe29b12-35c2-3fd2-a056-d43d03d37592 | -3.09757 | -53.25413 | 2024-11-29 05:22:00 | NPP-375D | MEDICILÂNDIA | PARÁ | Brasil | 1504455 | 15 | 33 | nan | nan | nan | Amazônia | 1.5 |
| 0c2c0834-ffa4-3538-a882-1970bfc237d4 | -2.65511 | -48.795 | 2024-11-29 05:22:00 | NPP-375D | TAILÂNDIA | PARÁ | Brasil | 1507953 | 15 | 33 | nan | nan | nan | Amazônia | 8.8 |
| 7c97bdf8-5b3a-36e9-a5b4-89b4db656711 | -2.75694 | -54.12071 | 2024-11-29 05:22:00 | NPP-375D | SANTARÉM | PARÁ | Brasil | 1506807 | 15 | 33 | nan | nan | nan | Amazônia | 3.0 |
| bb6cd92b-fe73-3120-98b7-6e987fc6a769 | -3.39003 | -54.29103 | 2024-11-29 05:22:00 | NPP-375D | MOJUÍ DOS CAMPOS | PARÁ | Brasil | 1504752 | 15 | 33 | nan | nan | nan | Amazônia | 1.9 |
| 20a55c07-75b6-3c13-8c0b-f0c7b890b611 | -2.835 | -48.09349 | 2024-11-29 05:22:00 | NPP-375D | TOMÉ-AÇU | PARÁ | Brasil | 1508001 | 15 | 33 | nan | nan | nan | Amazônia | 2.2 |
| 4579a7de-ba25-3967-998f-fc24dc288abc | -4.48157 | -48.19013 | 2024-11-29 05:22:00 | NPP-375D | RONDON DO PARÁ | PARÁ | Brasil | 1506187 | 15 | 33 | nan | nan | nan | Amazônia | 4.3 |
| 4aaa782b-240c-3fe4-8057-89fbcab5be91 | -3.11046 | -53.10552 | 2024-11-29 05:22:00 | NPP-375D | MEDICILÂNDIA | PARÁ | Brasil | 1504455 | 15 | 33 | nan | nan | nan | Amazônia | 1.7 |
| 938779ed-5d30-3f74-aba7-4e46283ea20d | -1.69149 | -52.45688 | 2024-11-29 05:22:00 | NPP-375D | PORTO DE MOZ | PARÁ | Brasil | 1505908 | 15 | 33 | nan | nan | nan | Amazônia | 2.1 |
| 086d6969-f24e-3b86-8376-9cd506c0ae1a | -3.2269 | -54.17344 | 2024-11-29 05:22:00 | NPP-375D | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | 4.3 |
| 156f77b1-3c8d-3737-960a-9a0abe2204f1 | -2.87573 | -46.86357 | 2024-11-29 05:22:00 | NPP-375D | PARAGOMINAS | PARÁ | Brasil | 1505502 | 15 | 33 | nan | nan | nan | Amazônia | 1.1 |
| 45b26ad8-8509-33de-8c9d-ac864ab09ac1 | -2.16296 | -53.27787 | 2024-11-29 05:22:00 | NPP-375D | PRAINHA | PARÁ | Brasil | 1506005 | 15 | 33 | nan | nan | nan | Amazônia | 0.9 |
| 02048322-6301-32d4-af56-e7f886f08e42 | -4.44206 | -46.58124 | 2024-11-29 05:22:00 | NPP-375D | BOM JESUS DAS SELVAS | MARANHÃO | Brasil | 2102036 | 21 | 33 | nan | nan | nan | Amazônia | 3.4 |
| 3af0f39e-3b42-3266-a7dc-7b0a40027717 | -1.60001 | -55.42156 | 2024-11-29 05:22:00 | NPP-375D | ÓBIDOS | PARÁ | Brasil | 1505106 | 15 | 33 | nan | nan | nan | Amazônia | 0.8 |
| 44ad43c0-9758-3fa3-99ca-986d810d6719 | -3.68932 | -52.41954 | 2024-11-29 05:22:00 | NPP-375D | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 4.4 |
| 45f56931-c8d8-387c-8a74-c95a192c736d | -2.98597 | -53.28406 | 2024-11-29 05:22:00 | NPP-375D | MEDICILÂNDIA | PARÁ | Brasil | 1504455 | 15 | 33 | nan | nan | nan | Amazônia | 20.3 |
| 82d993a1-5c71-3a49-8446-d212158d6ab8 | -3.79293 | -51.25667 | 2024-11-29 05:22:00 | NPP-375D | ANAPU | PARÁ | Brasil | 1500859 | 15 | 33 | nan | nan | nan | Amazônia | 1.3 |
| 4f73dbc0-3a5e-3502-bce0-4e3d76c6de3d | -2.8395 | -54.11386 | 2024-11-29 05:22:00 | NPP-375D | SANTARÉM | PARÁ | Brasil | 1506807 | 15 | 33 | nan | nan | nan | Amazônia | 2.1 |
| b2ffb780-7718-349e-a1fd-31a7de9f8548 | -3.37785 | -51.24854 | 2024-11-29 05:22:00 | NPP-375D | ANAPU | PARÁ | Brasil | 1500859 | 15 | 33 | nan | nan | nan | Amazônia | 1.3 |
| 2507d56a-57e9-321b-bd95-10111a02f330 | -1.68449 | -52.42955 | 2024-11-29 05:22:00 | NPP-375D | PORTO DE MOZ | PARÁ | Brasil | 1505908 | 15 | 33 | nan | nan | nan | Amazônia | 5.6 |
| a28797f8-df96-31bc-8628-196f075ca360 | -3.59019 | -50.3619 | 2024-11-29 05:22:00 | NPP-375D | PACAJÁ | PARÁ | Brasil | 1505486 | 15 | 33 | nan | nan | nan | Amazônia | 2.1 |
| 7d469524-9c85-3a35-a066-98550c74ec61 | -3.58603 | -50.51091 | 2024-11-29 05:22:00 | NPP-375D | PACAJÁ | PARÁ | Brasil | 1505486 | 15 | 33 | nan | nan | nan | Amazônia | 5.7 |
| 9c19bc38-0117-3704-bad7-f652188f838b | -1.35638 | -54.97857 | 2024-11-29 05:22:00 | NPP-375D | ALENQUER | PARÁ | Brasil | 1500404 | 15 | 33 | nan | nan | nan | Amazônia | 2.1 |
| 58466c8a-00c6-394e-ad35-e3bca6be127d | -3.11921 | -53.26215 | 2024-11-29 05:22:00 | NPP-375D | MEDICILÂNDIA | PARÁ | Brasil | 1504455 | 15 | 33 | nan | nan | nan | Amazônia | 2.2 |
| ab190f9a-9f5b-374c-bdd1-8d74942cb460 | -2.84129 | -54.07492 | 2024-11-29 05:22:00 | NPP-375D | PRAINHA | PARÁ | Brasil | 1506005 | 15 | 33 | nan | nan | nan | Amazônia | 3.6 |
| c70626e1-b00c-3417-a92a-f6a9f70588e4 | -2.05748 | -56.0759 | 2024-11-29 05:22:00 | NPP-375D | JURUTI | PARÁ | Brasil | 1503903 | 15 | 33 | nan | nan | nan | Amazônia | 4.2 |
| 95b87e45-474e-383f-9f39-70138ebe61a8 | -2.69868 | -49.83385 | 2024-11-29 05:22:00 | NPP-375D | OEIRAS DO PARÁ | PARÁ | Brasil | 1505205 | 15 | 33 | nan | nan | nan | Amazônia | 0.5 |
| ea4bf4f7-1a52-31eb-853c-5b7da4bc3d09 | -2.5222 | -54.13654 | 2024-11-29 05:22:00 | NPP-375D | PRAINHA | PARÁ | Brasil | 1506005 | 15 | 33 | nan | nan | nan | Amazônia | 2.5 |
| 6c07b5e3-b8dd-3054-ba2b-ba99c8564ab0 | -3.70294 | -50.5105 | 2024-11-29 05:22:00 | NPP-375D | PACAJÁ | PARÁ | Brasil | 1505486 | 15 | 33 | nan | nan | nan | Amazônia | 2.0 |
| 51d61c83-258b-32b2-8053-e44b9fcd1c65 | -3.31573 | -52.1497 | 2024-11-29 05:22:00 | NPP-375D | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 1.8 |
| e474b5ac-a0af-3247-9b72-e18aea25ca3e | -4.51429 | -59.80921 | 2024-11-29 05:22:00 | NPP-375D | BORBA | AMAZONAS | Brasil | 1300805 | 13 | 33 | nan | nan | nan | Amazônia | 2.6 |
| b203a45b-0258-32c7-bd90-b43668ca88c3 | -1.95007 | -52.96473 | 2024-11-29 05:22:00 | NPP-375D | PORTO DE MOZ | PARÁ | Brasil | 1505908 | 15 | 33 | nan | nan | nan | Amazônia | 1.7 |
| f4174727-f0b8-3f4a-a995-5fede2cc90c4 | -3.39116 | -54.28351 | 2024-11-29 05:22:00 | NPP-375D | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | 1.7 |
| a873b1ec-bb5a-316e-83fc-fc13cda9d14c | -2.36713 | -53.82254 | 2024-11-29 05:22:00 | NPP-375D | PRAINHA | PARÁ | Brasil | 1506005 | 15 | 33 | nan | nan | nan | Amazônia | 2.0 |
| a003e0c2-63dd-32cf-ab37-09d8a6e18e21 | -3.5362 | -50.1914 | 2024-11-29 05:22:00 | NPP-375D | PACAJÁ | PARÁ | Brasil | 1505486 | 15 | 33 | nan | nan | nan | Amazônia | 0.8 |
| b1a833b0-72ef-3360-8000-6732b51e0c1c | -2.3158 | -51.95708 | 2024-11-29 05:22:00 | NPP-375D | PORTO DE MOZ | PARÁ | Brasil | 1505908 | 15 | 33 | nan | nan | nan | Amazônia | 2.3 |
| 5b8ac473-6680-3d06-82ca-253069da4103 | -3.38015 | -50.11212 | 2024-11-29 05:22:00 | NPP-375D | PACAJÁ | PARÁ | Brasil | 1505486 | 15 | 33 | nan | nan | nan | Amazônia | 2.3 |
| 95ccf91d-f655-31ec-bb12-946a128930c5 | -2.84733 | -46.82184 | 2024-11-29 05:22:00 | NPP-375D | PARAGOMINAS | PARÁ | Brasil | 1505502 | 15 | 33 | nan | nan | nan | Amazônia | 1.3 |
| 236b3a23-f342-393f-8386-3a61b45c529f | -3.31687 | -54.17837 | 2024-11-29 05:22:00 | NPP-375D | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | 1.0 |
| c024cde7-d980-33f0-afb6-886d247334ee | -4.05021 | -50.32405 | 2024-11-29 05:22:00 | NPP-375D | NOVO REPARTIMENTO | PARÁ | Brasil | 1505064 | 15 | 33 | nan | nan | nan | Amazônia | 1.0 |
| f4a952ee-37f0-37ab-9d78-34c87e337670 | -2.88634 | -51.58532 | 2024-11-29 05:22:00 | NPP-375D | ANAPU | PARÁ | Brasil | 1500859 | 15 | 33 | nan | nan | nan | Amazônia | 1.4 |
| cc8c8ad5-a9b9-3ea5-a192-acb7c1b4621a | -4.19894 | -50.68535 | 2024-11-29 05:22:00 | NPP-375D | PACAJÁ | PARÁ | Brasil | 1505486 | 15 | 33 | nan | nan | nan | Amazônia | 1.9 |
| 3b23593c-a85a-3aa5-a8d9-925c4a9ff441 | -2.89367 | -54.01572 | 2024-11-29 05:22:00 | NPP-375D | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | 2.6 |
| 36651ce9-9f33-3f0d-8768-8550f7d3b41b | -3.96264 | -50.18848 | 2024-11-29 05:22:00 | NPP-375D | PACAJÁ | PARÁ | Brasil | 1505486 | 15 | 33 | nan | nan | nan | Amazônia | 0.9 |


[Clique aqui para ver as próximas entradas](README91.md)
