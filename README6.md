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

## Dados Diários - Página 6

| ID | Latitude | Longitude | Data/Hora GMT | Satélite | Município | Estado | País | Município ID | Estado ID | País ID | Dias sem Chuva | Precipitação | Risco de Fogo | Bioma | FRP |
|----|----------|-----------|---------------|----------|-----------|--------|------|--------------|-----------|---------|----------------|--------------|----------------|-------|-----|
| 9cc8ec44-d479-3689-9f22-89b6ae00db67 | -2.86105 | -45.53365 | 2024-11-29 00:52:00 | TERRA_M-M | PEDRO DO ROSÁRIO | MARANHÃO | Brasil | 2108256 | 21 | 33 | nan | nan | nan | Amazônia | 282.2 |
| 8bc1b61f-25dd-3c48-a6a3-192d000963da | 0.92932 | -50.27312 | 2024-11-29 00:52:00 | TERRA_M-M | MACAPÁ | AMAPÁ | Brasil | 1600303 | 16 | 33 | nan | nan | nan | Amazônia | 5.3 |
| 15f0e993-61c7-3aab-9545-6f811e23dc7b | -3.18342 | -45.64561 | 2024-11-29 00:52:00 | TERRA_M-M | ZÉ DOCA | MARANHÃO | Brasil | 2114007 | 21 | 33 | nan | nan | nan | Amazônia | 7.5 |
| a3a42d39-374f-3d78-b11a-9081ce8abcbe | -1.69828 | -52.44886 | 2024-11-29 00:52:00 | TERRA_M-M | PORTO DE MOZ | PARÁ | Brasil | 1505908 | 15 | 33 | nan | nan | nan | Amazônia | 35.0 |
| 618c86bd-d038-3920-984a-165f596926e7 | -4.44135 | -46.5836 | 2024-11-29 00:52:00 | TERRA_M-M | BOM JESUS DAS SELVAS | MARANHÃO | Brasil | 2102036 | 21 | 33 | nan | nan | nan | Amazônia | 5.9 |
| 4b0ad529-a675-3e8b-898b-e2aed1b31191 | -2.76414 | -49.87924 | 2024-11-29 00:52:00 | TERRA_M-M | OEIRAS DO PARÁ | PARÁ | Brasil | 1505205 | 15 | 33 | nan | nan | nan | Amazônia | 5.1 |
| 42bbf557-223c-3c7d-87e9-c7d629dcce4a | -0.99297 | -51.71843 | 2024-11-29 00:52:00 | TERRA_M-M | VITÓRIA DO JARI | AMAPÁ | Brasil | 1600808 | 16 | 33 | nan | nan | nan | Amazônia | 17.7 |
| 30fa47da-9717-3ecd-9f1b-005612c00109 | -1.71579 | -52.49734 | 2024-11-29 00:52:00 | TERRA_M-M | PORTO DE MOZ | PARÁ | Brasil | 1505908 | 15 | 33 | nan | nan | nan | Amazônia | 18.3 |
| bfd50eac-a8f7-329e-a2c8-1e5c0b098a4b | -3.84389 | -46.65482 | 2024-11-29 00:52:00 | TERRA_M-M | BOM JARDIM | MARANHÃO | Brasil | 2102002 | 21 | 33 | nan | nan | nan | Amazônia | 6.2 |
| 02e374aa-069d-3ecf-b70d-47ec441b755c | -3.36307 | -52.6805 | 2024-11-29 00:52:00 | TERRA_M-M | BRASIL NOVO | PARÁ | Brasil | 1501725 | 15 | 33 | nan | nan | nan | Amazônia | 9.4 |
| 2121d5b0-61aa-3102-b1aa-367639b50049 | -2.65109 | -48.80084 | 2024-11-29 00:52:00 | TERRA_M-M | TAILÂNDIA | PARÁ | Brasil | 1507953 | 15 | 33 | nan | nan | nan | Amazônia | 5.8 |
| 63b2d26f-71cb-34ca-9b60-6e4aab06c411 | -3.69454 | -52.41905 | 2024-11-29 00:52:00 | TERRA_M-M | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 14.3 |
| 92ab0933-823b-3bc5-b6a9-fc251a289f72 | -2.67735 | -48.78184 | 2024-11-29 00:52:00 | TERRA_M-M | TAILÂNDIA | PARÁ | Brasil | 1507953 | 15 | 33 | nan | nan | nan | Amazônia | 5.2 |
| dfed5194-2041-3a85-9ce7-5f3de53e1d4f | -2.83381 | -46.80807 | 2024-11-29 00:52:00 | TERRA_M-M | PARAGOMINAS | PARÁ | Brasil | 1505502 | 15 | 33 | nan | nan | nan | Amazônia | 6.2 |
| b086a633-637c-3caa-8ddd-4484e12bbdb4 | -0.60532 | -51.71963 | 2024-11-29 00:52:00 | TERRA_M-M | MAZAGÃO | AMAPÁ | Brasil | 1600402 | 16 | 33 | nan | nan | nan | Amazônia | 10.1 |
| 43c4c6e6-b157-31e1-aefa-76fde2ba0a05 | -3.59763 | -50.37921 | 2024-11-29 00:52:00 | TERRA_M-M | PACAJÁ | PARÁ | Brasil | 1505486 | 15 | 33 | nan | nan | nan | Amazônia | 4.4 |
| 73d09155-41e6-3de5-bdeb-3eddcd39e41e | -2.64885 | -47.13374 | 2024-11-29 00:52:00 | TERRA_M-M | NOVA ESPERANÇA DO PIRIÁ | PARÁ | Brasil | 1504950 | 15 | 33 | nan | nan | nan | Amazônia | 4.7 |
| 0355358f-b302-3835-a70d-9e079236dbd9 | -4.04638 | -46.8524 | 2024-11-29 00:52:00 | TERRA_M-M | BOM JARDIM | MARANHÃO | Brasil | 2102002 | 21 | 33 | nan | nan | nan | Amazônia | 7.2 |
| ef68041f-f61c-3755-a3ea-d6ab64640e7d | -2.71702 | -48.67727 | 2024-11-29 00:52:00 | TERRA_M-M | TAILÂNDIA | PARÁ | Brasil | 1507953 | 15 | 33 | nan | nan | nan | Amazônia | 5.6 |
| d4292460-cdf1-3066-9be0-e632d0635dc7 | -1.21045 | -51.74296 | 2024-11-29 00:52:00 | TERRA_M-M | GURUPÁ | PARÁ | Brasil | 1503101 | 15 | 33 | nan | nan | nan | Amazônia | 10.2 |
| d43704f0-1113-3282-b8bc-a88432b7cfdc | -2.20052 | -48.34069 | 2024-11-29 00:52:00 | TERRA_M-M | TOMÉ-AÇU | PARÁ | Brasil | 1508001 | 15 | 33 | nan | nan | nan | Amazônia | 7.4 |
| ea4f820d-7b5b-3ba3-8763-cd23fa9dbc24 | -3.01809 | -47.79357 | 2024-11-29 00:52:00 | TERRA_M-M | PARAGOMINAS | PARÁ | Brasil | 1505502 | 15 | 33 | nan | nan | nan | Amazônia | 3.7 |
| a9f517f0-0903-3c91-8ef7-598c1f33c401 | -4.2029 | -50.69434 | 2024-11-29 00:52:00 | TERRA_M-M | PACAJÁ | PARÁ | Brasil | 1505486 | 15 | 33 | nan | nan | nan | Amazônia | 8.5 |
| ea9563e1-c8e5-3609-8443-6d6c2717e996 | -4.10714 | -51.02787 | 2024-11-29 00:52:00 | TERRA_M-M | PACAJÁ | PARÁ | Brasil | 1505486 | 15 | 33 | nan | nan | nan | Amazônia | 9.7 |
| 0c2304e0-272b-3469-8c6f-785b7b414f4d | 0.93738 | -50.7403 | 2024-11-29 00:52:00 | TERRA_M-M | CUTIAS | AMAPÁ | Brasil | 1600212 | 16 | 33 | nan | nan | nan | Amazônia | 23.8 |
| e6bc3ef3-85b1-3108-adde-5ee8258f0032 | -3.98103 | -46.65183 | 2024-11-29 00:52:00 | TERRA_M-M | BOM JARDIM | MARANHÃO | Brasil | 2102002 | 21 | 33 | nan | nan | nan | Amazônia | 10.1 |
| d8736da9-0a4c-3aa2-a631-f433d5328c04 | -1.96478 | -46.45097 | 2024-11-29 00:52:00 | TERRA_M-M | CACHOEIRA DO PIRIÁ | PARÁ | Brasil | 1501956 | 15 | 33 | nan | nan | nan | Amazônia | 23.0 |
| e9d637ef-8009-3dfc-8911-b70792e9bcd0 | -0.0218 | -49.63355 | 2024-11-29 00:52:00 | TERRA_M-M | CHAVES | PARÁ | Brasil | 1502509 | 15 | 33 | nan | nan | nan | Amazônia | 5.6 |
| fb4f63b5-2d38-3500-9130-630db2f5380e | -2.59042 | -46.21009 | 2024-11-29 00:52:00 | TERRA_M-M | CENTRO DO GUILHERME | MARANHÃO | Brasil | 2103158 | 21 | 33 | nan | nan | nan | Amazônia | 4.6 |
| deee12cd-c3ad-3ddc-b875-b9b4ce0093ac | -2.72369 | -48.59544 | 2024-11-29 00:52:00 | TERRA_M-M | TAILÂNDIA | PARÁ | Brasil | 1507953 | 15 | 33 | nan | nan | nan | Amazônia | 4.1 |
| 4321ab65-fb94-34a8-a106-d2a72724ec16 | -1.59863 | -52.62236 | 2024-11-29 00:52:00 | TERRA_M-M | PORTO DE MOZ | PARÁ | Brasil | 1505908 | 15 | 33 | nan | nan | nan | Amazônia | 12.9 |
| a3e5978c-3932-394e-9ae6-7d72d63dafee | -2.41267 | -48.54108 | 2024-11-29 00:52:00 | TERRA_M-M | ACARÁ | PARÁ | Brasil | 1500206 | 15 | 33 | nan | nan | nan | Amazônia | 8.0 |
| 95781379-f22a-32eb-aed7-8e45b492e98a | -3.32416 | -54.18959 | 2024-11-29 00:52:00 | TERRA_M-M | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | 15.1 |
| 8dc1b92c-d199-3aa9-a1bf-8b33e80ec356 | -3.53476 | -50.19789 | 2024-11-29 00:52:00 | TERRA_M-M | PACAJÁ | PARÁ | Brasil | 1505486 | 15 | 33 | nan | nan | nan | Amazônia | 5.9 |
| a94bb977-b53c-3724-989a-cf3aa097f5ee | -4.47999 | -48.10831 | 2024-11-29 00:52:00 | TERRA_M-M | RONDON DO PARÁ | PARÁ | Brasil | 1506187 | 15 | 33 | nan | nan | nan | Amazônia | 4.6 |
| c5aca22b-3bd5-3a8d-9e88-aca97457e512 | -4.00188 | -49.97404 | 2024-11-29 00:52:00 | TERRA_M-M | TUCURUÍ | PARÁ | Brasil | 1508100 | 15 | 33 | nan | nan | nan | Amazônia | 7.8 |
| 8936f81b-9b3f-335f-ad04-bdf35904f83d | -4.04767 | -46.86164 | 2024-11-29 00:52:00 | TERRA_M-M | BOM JARDIM | MARANHÃO | Brasil | 2102002 | 21 | 33 | nan | nan | nan | Amazônia | 4.9 |
| 4b52c377-adde-377b-a487-2c104c371815 | -3.80999 | -46.67908 | 2024-11-29 00:52:00 | TERRA_M-M | BOM JARDIM | MARANHÃO | Brasil | 2102002 | 21 | 33 | nan | nan | nan | Amazônia | 4.5 |
| 5e074dee-1752-3f33-8087-e8febe630529 | -2.83756 | -46.7005 | 2024-11-29 00:52:00 | TERRA_M-M | PARAGOMINAS | PARÁ | Brasil | 1505502 | 15 | 33 | nan | nan | nan | Amazônia | 5.9 |
| c3e178f9-ea91-3ea6-a022-74efdf14a7ad | -1.08361 | -53.37993 | 2024-11-29 00:52:00 | TERRA_M-M | ALMEIRIM | PARÁ | Brasil | 1500503 | 15 | 33 | nan | nan | nan | Amazônia | 14.9 |
| 1e031fa6-a993-3351-a8fe-8e667969f6e8 | -3.77342 | -46.68428 | 2024-11-29 00:52:00 | TERRA_M-M | BOM JARDIM | MARANHÃO | Brasil | 2102002 | 21 | 33 | nan | nan | nan | Amazônia | 7.1 |
| 49d47964-3edd-38f6-bece-4550d44b5616 | -2.80789 | -45.52492 | 2024-11-29 00:52:00 | TERRA_M-M | SANTA HELENA | MARANHÃO | Brasil | 2109809 | 21 | 33 | nan | nan | nan | Amazônia | 8.1 |
| 907e59db-e39b-346a-8ddd-dbe1025a3db7 | -2.5785 | -50.00309 | 2024-11-29 00:52:00 | TERRA_M-M | BAGRE | PARÁ | Brasil | 1501105 | 15 | 33 | nan | nan | nan | Amazônia | 21.9 |
| f3d07c54-65b4-36cd-8231-83484e351eac | -3.16406 | -53.23532 | 2024-11-29 00:52:00 | TERRA_M-M | MEDICILÂNDIA | PARÁ | Brasil | 1504455 | 15 | 33 | nan | nan | nan | Amazônia | 10.3 |
| 345f4376-5851-3b85-b54d-8843664828a3 | -2.69713 | -48.59919 | 2024-11-29 00:52:00 | TERRA_M-M | TAILÂNDIA | PARÁ | Brasil | 1507953 | 15 | 33 | nan | nan | nan | Amazônia | 4.0 |
| 9609adf6-4555-3083-9ea9-38268ca4ec83 | -3.96856 | -48.06752 | 2024-11-29 00:52:00 | TERRA_M-M | DOM ELISEU | PARÁ | Brasil | 1502939 | 15 | 33 | nan | nan | nan | Amazônia | 13.3 |
| 37a4f047-cb08-3dd1-9719-b76b78d394a4 | -1.30634 | -52.27906 | 2024-11-29 00:52:00 | TERRA_M-M | ALMEIRIM | PARÁ | Brasil | 1500503 | 15 | 33 | nan | nan | nan | Amazônia | 7.0 |
| 9aba8701-347a-3e5d-81b1-27aadbcbc53b | -3.89782 | -49.81998 | 2024-11-29 00:52:00 | TERRA_M-M | TUCURUÍ | PARÁ | Brasil | 1508100 | 15 | 33 | nan | nan | nan | Amazônia | 9.4 |
| eaf15805-436d-3c98-a786-3d251c79ee3f | -1.35489 | -55.01281 | 2024-11-29 00:52:00 | TERRA_M-M | ALENQUER | PARÁ | Brasil | 1500404 | 15 | 33 | nan | nan | nan | Amazônia | 17.2 |
| 8ca0f25b-536e-355e-8599-b125bd23b31a | -2.75155 | -54.10635 | 2024-11-29 00:52:00 | TERRA_M-M | PRAINHA | PARÁ | Brasil | 1506005 | 15 | 33 | nan | nan | nan | Amazônia | 12.0 |
| ac4c32d6-34bd-3c03-bc93-3741bb504bc9 | -3.46353 | -50.53224 | 2024-11-29 00:52:00 | TERRA_M-M | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 13.5 |
| 812f0399-ac74-316d-a71d-357826d33d5b | -3.22995 | -50.31436 | 2024-11-29 00:52:00 | TERRA_M-M | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 5.6 |
| eecd763c-d457-3279-a77c-6199c2e990fd | -3.31942 | -52.15984 | 2024-11-29 00:52:00 | TERRA_M-M | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 7.7 |
| 49c214f7-e0d4-39b9-a37e-fee2924369a9 | -3.31775 | -52.14724 | 2024-11-29 00:52:00 | TERRA_M-M | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 18.5 |
| 07fdb20a-8e4a-3850-b6bb-abd9ecfc7047 | -1.55626 | -52.02177 | 2024-11-29 00:52:00 | TERRA_M-M | GURUPÁ | PARÁ | Brasil | 1503101 | 15 | 33 | nan | nan | nan | Amazônia | 9.0 |
| 4e7f5104-edbc-3e1a-a522-f7345a17ce69 | -2.8443 | -46.81623 | 2024-11-29 00:52:00 | TERRA_M-M | PARAGOMINAS | PARÁ | Brasil | 1505502 | 15 | 33 | nan | nan | nan | Amazônia | 50.0 |
| eba75515-f3ad-332b-8bf8-b5989484b534 | -4.30961 | -48.20764 | 2024-11-29 00:52:00 | TERRA_M-M | RONDON DO PARÁ | PARÁ | Brasil | 1506187 | 15 | 33 | nan | nan | nan | Amazônia | 8.9 |
| b9c9ea07-19a1-3617-ac83-350232d0da3d | -3.33462 | -50.21815 | 2024-11-29 00:52:00 | TERRA_M-M | PACAJÁ | PARÁ | Brasil | 1505486 | 15 | 33 | nan | nan | nan | Amazônia | 11.2 |
| 5c5e16f6-1d34-333b-a1b4-75231e488279 | -1.83338 | -46.23734 | 2024-11-29 00:52:00 | TERRA_M-M | CACHOEIRA DO PIRIÁ | PARÁ | Brasil | 1501956 | 15 | 33 | nan | nan | nan | Amazônia | 11.8 |
| bbd08eb5-e782-30cf-bbd2-b9cc73a1a57d | -2.42044 | -47.60423 | 2024-11-29 00:52:00 | TERRA_M-M | IPIXUNA DO PARÁ | PARÁ | Brasil | 1503457 | 15 | 33 | nan | nan | nan | Amazônia | 6.6 |
| 021b6bdf-36d6-35c3-a5c6-b31c4dbccfea | -2.83514 | -46.81754 | 2024-11-29 00:52:00 | TERRA_M-M | PARAGOMINAS | PARÁ | Brasil | 1505502 | 15 | 33 | nan | nan | nan | Amazônia | 5.2 |
| aa0e4fc1-fbc2-38da-a39d-9e5964b785ef | -4.39526 | -47.23478 | 2024-11-29 00:52:00 | TERRA_M-M | ITINGA DO MARANHÃO | MARANHÃO | Brasil | 2105427 | 21 | 33 | nan | nan | nan | Amazônia | 4.6 |
| 20a6b1a2-bb10-3472-bae0-700e9d01fa17 | -4.91486 | -44.03305 | 2024-11-29 00:52:00 | TERRA_M-M | CODÓ | MARANHÃO | Brasil | 2103307 | 21 | 33 | nan | nan | nan | Cerrado | 9.7 |
| 88e8749a-5833-3059-8491-7ab589e02d6c | -2.45582 | -46.55632 | 2024-11-29 00:52:00 | TERRA_M-M | NOVA ESPERANÇA DO PIRIÁ | PARÁ | Brasil | 1504950 | 15 | 33 | nan | nan | nan | Amazônia | 4.8 |
| a7a3486b-53b9-3c10-b6fc-6096b82ba0d8 | -3.106 | -50.35741 | 2024-11-29 00:52:00 | TERRA_M-M | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 12.3 |
| 3ab7a3c4-e260-3e5f-90a0-724f81759a13 | -1.20339 | -51.6214 | 2024-11-29 00:52:00 | TERRA_M-M | GURUPÁ | PARÁ | Brasil | 1503101 | 15 | 33 | nan | nan | nan | Amazônia | 5.6 |
| 0d4eaa36-bc2c-354f-9d26-6bed267e654a | -3.05949 | -45.06572 | 2024-11-29 00:52:00 | TERRA_M-M | MATINHA | MARANHÃO | Brasil | 2106508 | 21 | 33 | nan | nan | nan | Amazônia | 73.6 |
| a8e68152-3645-3120-9720-d7867a7c3c99 | -4.76146 | -49.54254 | 2024-11-29 00:52:00 | TERRA_M-M | NOVO REPARTIMENTO | PARÁ | Brasil | 1505064 | 15 | 33 | nan | nan | nan | Amazônia | 20.4 |
| 995d24ab-667d-3eb9-98e1-3ad9be4b0368 | -1.09921 | -53.40019 | 2024-11-29 00:52:00 | TERRA_M-M | ALMEIRIM | PARÁ | Brasil | 1500503 | 15 | 33 | nan | nan | nan | Amazônia | 17.3 |
| 17d9eddc-2fae-3c84-a660-ed32dd7bcae6 | -2.06261 | -46.38382 | 2024-11-29 00:52:00 | TERRA_M-M | CACHOEIRA DO PIRIÁ | PARÁ | Brasil | 1501956 | 15 | 33 | nan | nan | nan | Amazônia | 14.4 |
| afeed6b8-c069-33eb-a4aa-79900445e241 | -3.3332 | -53.21494 | 2024-11-29 00:52:00 | TERRA_M-M | MEDICILÂNDIA | PARÁ | Brasil | 1504455 | 15 | 33 | nan | nan | nan | Amazônia | 25.3 |
| d0faecf9-53c8-3e66-9ce5-85095940e546 | -1.38527 | -53.64625 | 2024-11-29 00:52:00 | TERRA_M-M | PRAINHA | PARÁ | Brasil | 1506005 | 15 | 33 | nan | nan | nan | Amazônia | 23.0 |
| 41b7556c-9995-3fb7-bc0f-13f90863be39 | -4.11107 | -50.98331 | 2024-11-29 00:52:00 | TERRA_M-M | PACAJÁ | PARÁ | Brasil | 1505486 | 15 | 33 | nan | nan | nan | Amazônia | 12.2 |
| 1fa7553c-15d4-33bb-8c66-58895ca16d2a | -2.96971 | -45.22599 | 2024-11-29 00:52:00 | TERRA_M-M | VIANA | MARANHÃO | Brasil | 2112803 | 21 | 33 | nan | nan | nan | Amazônia | 6.0 |
| ca02308a-5fb5-3473-8d13-c3a420a9ab01 | -3.32455 | -46.70126 | 2024-11-29 00:52:00 | TERRA_M-M | CENTRO NOVO DO MARANHÃO | MARANHÃO | Brasil | 2103174 | 21 | 33 | nan | nan | nan | Amazônia | 17.6 |
| f18fda57-15f3-3390-9ae6-35c47ba53114 | -3.38608 | -50.11255 | 2024-11-29 00:52:00 | TERRA_M-M | PACAJÁ | PARÁ | Brasil | 1505486 | 15 | 33 | nan | nan | nan | Amazônia | 20.0 |
| 8aa9bee7-d671-3cff-b8e6-b2c3ed02af6d | -4.27909 | -46.47377 | 2024-11-29 00:52:00 | TERRA_M-M | BURITICUPU | MARANHÃO | Brasil | 2102325 | 21 | 33 | nan | nan | nan | Amazônia | 8.8 |
| 521cd848-ec27-3c58-a9c8-494f86feecd7 | -0.30001 | -51.74279 | 2024-11-29 00:52:00 | TERRA_M-M | MAZAGÃO | AMAPÁ | Brasil | 1600402 | 16 | 33 | nan | nan | nan | Amazônia | 7.2 |
| bed69fa4-13f9-3cda-975c-94d348583e5f | -1.68438 | -52.42549 | 2024-11-29 00:52:00 | TERRA_M-M | PORTO DE MOZ | PARÁ | Brasil | 1505908 | 15 | 33 | nan | nan | nan | Amazônia | 12.8 |
| 686a3dc0-5236-37f0-b6e3-e095a55d6bb3 | -3.52555 | -50.38513 | 2024-11-29 00:52:00 | TERRA_M-M | PACAJÁ | PARÁ | Brasil | 1505486 | 15 | 33 | nan | nan | nan | Amazônia | 5.0 |
| 17f84395-f7dc-3f90-b2b8-1a2574cf7152 | -3.04631 | -48.52549 | 2024-11-29 00:52:00 | TERRA_M-M | TAILÂNDIA | PARÁ | Brasil | 1507953 | 15 | 33 | nan | nan | nan | Amazônia | 4.0 |
| 94feafd6-49da-3430-b2b0-2af46d1f9b8c | -2.70821 | -46.18662 | 2024-11-29 00:52:00 | TERRA_M-M | CENTRO NOVO DO MARANHÃO | MARANHÃO | Brasil | 2103174 | 21 | 33 | nan | nan | nan | Amazônia | 5.3 |
| f75b4d96-5c88-3eb7-ae3d-5086ea410554 | -1.62214 | -53.87919 | 2024-11-29 00:52:00 | TERRA_M-M | PRAINHA | PARÁ | Brasil | 1506005 | 15 | 33 | nan | nan | nan | Amazônia | 15.1 |
| 4572689a-0ec7-3311-bd60-7d642c6b55e0 | -3.81428 | -44.05467 | 2024-11-29 00:52:00 | TERRA_M-M | PIRAPEMAS | MARANHÃO | Brasil | 2108801 | 21 | 33 | nan | nan | nan | Cerrado | 18.1 |
| de75c57e-5f5e-3628-96df-79c751df909a | -3.78391 | -46.69245 | 2024-11-29 00:52:00 | TERRA_M-M | BOM JARDIM | MARANHÃO | Brasil | 2102002 | 21 | 33 | nan | nan | nan | Amazônia | 16.4 |
| 43d1519b-c41d-36dd-b7ce-1e5c118f0bea | -3.25015 | -53.62859 | 2024-11-29 00:52:00 | TERRA_M-M | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | 38.6 |
| 0a43da8a-34d3-3ffa-8e7e-69dcce1e4168 | -2.70449 | -48.65207 | 2024-11-29 00:52:00 | TERRA_M-M | TAILÂNDIA | PARÁ | Brasil | 1507953 | 15 | 33 | nan | nan | nan | Amazônia | 6.9 |
| 4dc8eaef-931a-3265-a152-4dec8d417c41 | -1.199 | -52.10194 | 2024-11-29 00:52:00 | TERRA_M-M | VITÓRIA DO JARI | AMAPÁ | Brasil | 1600808 | 16 | 33 | nan | nan | nan | Amazônia | 8.1 |
| 01e31cfa-e4e7-33fa-8788-96ad9c934bcf | -4.41483 | -50.82512 | 2024-11-29 00:52:00 | TERRA_M-M | NOVO REPARTIMENTO | PARÁ | Brasil | 1505064 | 15 | 33 | nan | nan | nan | Amazônia | 19.0 |
| 8420e6b2-965b-330b-881a-0af63cb45cd3 | -2.57319 | -49.09774 | 2024-11-29 00:52:00 | TERRA_M-M | MOJU | PARÁ | Brasil | 1504703 | 15 | 33 | nan | nan | nan | Amazônia | 4.1 |
| bb8510a4-033f-3414-8c81-266d04297596 | -2.88591 | -51.58799 | 2024-11-29 00:52:00 | TERRA_M-M | ANAPU | PARÁ | Brasil | 1500859 | 15 | 33 | nan | nan | nan | Amazônia | 5.4 |
| e2c5474d-7555-3397-b1b8-52a09906e3e9 | -1.19382 | -51.76777 | 2024-11-29 00:52:00 | TERRA_M-M | GURUPÁ | PARÁ | Brasil | 1503101 | 15 | 33 | nan | nan | nan | Amazônia | 9.5 |
| 42df4358-0dbb-3c92-bb2d-c5306d249aaa | -3.42446 | -53.88534 | 2024-11-29 00:52:00 | TERRA_M-M | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | 14.5 |
| 55aacb6b-de65-31e2-8b38-354a7f19ed9b | -3.26907 | -46.44451 | 2024-11-29 00:52:00 | TERRA_M-M | CENTRO NOVO DO MARANHÃO | MARANHÃO | Brasil | 2103174 | 21 | 33 | nan | nan | nan | Amazônia | 9.7 |
| 35c7638c-ab73-389d-959a-abaf9dc07d04 | -3.97346 | -46.72971 | 2024-11-29 00:52:00 | TERRA_M-M | BOM JARDIM | MARANHÃO | Brasil | 2102002 | 21 | 33 | nan | nan | nan | Amazônia | 6.4 |
| e26150a0-8791-34e4-9765-d17529f23e55 | -4.01028 | -46.98927 | 2024-11-29 00:52:00 | TERRA_M-M | ITINGA DO MARANHÃO | MARANHÃO | Brasil | 2105427 | 21 | 33 | nan | nan | nan | Amazônia | 9.5 |
| d0541f8e-91c7-33cc-bb77-b832cc2f7f22 | -2.51991 | -48.51964 | 2024-11-29 00:52:00 | TERRA_M-M | ACARÁ | PARÁ | Brasil | 1500206 | 15 | 33 | nan | nan | nan | Amazônia | 3.8 |
| 0ac25af3-7d8d-3e84-a423-c9e3d940e7de | -2.58702 | -54.24736 | 2024-11-29 00:52:00 | TERRA_M-M | PRAINHA | PARÁ | Brasil | 1506005 | 15 | 33 | nan | nan | nan | Amazônia | 18.2 |
| 705458ed-9a3c-3e61-9152-73847d9dbc69 | -3.5696 | -53.0141 | 2024-11-29 00:52:00 | TERRA_M-M | MEDICILÂNDIA | PARÁ | Brasil | 1504455 | 15 | 33 | nan | nan | nan | Amazônia | 18.8 |
| 2ec6cd38-6e80-3b6c-8ecb-596d87d58a29 | -4.92542 | -44.53782 | 2024-11-29 00:52:00 | TERRA_M-M | SANTO ANTÔNIO DOS LOPES | MARANHÃO | Brasil | 2110302 | 21 | 33 | nan | nan | nan | Cerrado | 7.1 |


[Clique aqui para ver as próximas entradas](README7.md)
