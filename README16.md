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
| f081259a-5051-32d6-93eb-e1e16ac1c6c7 | -1.12382 | -47.74265 | 2025-12-12 04:21:00 | NOAA-20 | SÃO FRANCISCO DO PARÁ | PARÁ | Brasil | 1507409 | 15 | 33 | nan | nan | nan | Amazônia | 1.1 |
| e06ac82d-bffa-3d51-943d-e4a444c47ab6 | -3.95931 | -41.5271 | 2025-12-12 04:21:00 | NOAA-20 | PIRACURUCA | PIAUÍ | Brasil | 2208304 | 22 | 33 | nan | nan | nan | Caatinga | 2.0 |
| dac70a91-624e-3b19-983b-f8fa00eba0ee | -2.64952 | -51.64235 | 2025-12-12 04:21:00 | NOAA-20 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 0.7 |
| 3d35a591-8dd7-34f9-8284-dd2173ac8740 | -2.54069 | -47.80053 | 2025-12-12 04:21:00 | NOAA-20 | IPIXUNA DO PARÁ | PARÁ | Brasil | 1503457 | 15 | 33 | nan | nan | nan | Amazônia | 1.3 |
| 6bf0b9c6-354f-3cfd-b64f-2355853deadf | -3.34355 | -53.07119 | 2025-12-12 04:21:00 | NOAA-20 | MEDICILÂNDIA | PARÁ | Brasil | 1504455 | 15 | 33 | nan | nan | nan | Amazônia | 0.6 |
| 6c2ca1ec-e9a8-307f-9917-07814f71ddb1 | -3.35242 | -46.86448 | 2025-12-12 04:21:00 | NOAA-20 | CENTRO NOVO DO MARANHÃO | MARANHÃO | Brasil | 2103174 | 21 | 33 | nan | nan | nan | Amazônia | 0.9 |
| 2616e94e-7280-34a0-bab1-8102545bf83a | -7.47275 | -35.31423 | 2025-12-12 04:21:00 | NOAA-20 | CAMUTANGA | PERNAMBUCO | Brasil | 2603603 | 26 | 33 | nan | nan | nan | Mata Atlântica | 1.1 |
| bbca5618-5d0e-3479-8e82-9d3559df9227 | -3.62758 | -45.39064 | 2025-12-12 04:21:00 | NOAA-20 | PINDARÉ-MIRIM | MARANHÃO | Brasil | 2108504 | 21 | 33 | nan | nan | nan | Amazônia | 2.1 |
| 6c656b8e-21ce-3261-9df6-aee5bdb54121 | -3.75825 | -47.15571 | 2025-12-12 04:21:00 | NOAA-20 | ULIANÓPOLIS | PARÁ | Brasil | 1508126 | 15 | 33 | nan | nan | nan | Amazônia | 1.2 |
| 6b488f6e-e8d6-3430-964c-0d0f957a8a78 | -5.24989 | -43.35518 | 2025-12-12 04:21:00 | NOAA-20 | MATÕES | MARANHÃO | Brasil | 2106607 | 21 | 33 | nan | nan | nan | Cerrado | 0.8 |
| 38e53d23-8656-33e9-b4d4-1afb7ee97013 | -6.46413 | -39.39546 | 2025-12-12 04:21:00 | NOAA-20 | IGUATU | CEARÁ | Brasil | 2305506 | 23 | 33 | nan | nan | nan | Caatinga | 1.4 |
| b23485e9-6528-398e-9bbb-af8aba7da1b3 | -3.40023 | -45.43116 | 2025-12-12 04:21:00 | NOAA-20 | MONÇÃO | MARANHÃO | Brasil | 2106904 | 21 | 33 | nan | nan | nan | Amazônia | 0.7 |
| 24989ef7-01a2-320e-b6fe-c06c304298ed | -6.71996 | -47.79223 | 2025-12-12 04:21:00 | NOAA-20 | DARCINÓPOLIS | TOCANTINS | Brasil | 1706506 | 17 | 33 | nan | nan | nan | Cerrado | 0.9 |
| 2be5b47b-3820-359d-8eb5-00297a75fe3b | -3.23464 | -42.07603 | 2025-12-12 04:21:00 | NOAA-20 | MAGALHÃES DE ALMEIDA | MARANHÃO | Brasil | 2106300 | 21 | 33 | nan | nan | nan | Cerrado | 1.5 |
| b95bd22c-58e1-34e2-b2a6-c54f026dd4ef | -5.15666 | -37.70271 | 2025-12-12 04:21:00 | NOAA-20 | BARAÚNA | RIO GRANDE DO NORTE | Brasil | 2401453 | 24 | 33 | nan | nan | nan | Caatinga | 1.9 |
| 6636952d-0760-3b40-983d-7171307de436 | -4.76991 | -43.60143 | 2025-12-12 04:21:00 | NOAA-20 | CAXIAS | MARANHÃO | Brasil | 2103000 | 21 | 33 | nan | nan | nan | Cerrado | 1.4 |
| bdeb344e-1f40-366a-921a-1f6d151241a2 | -2.96819 | -40.8558 | 2025-12-12 04:21:00 | NOAA-20 | CAMOCIM | CEARÁ | Brasil | 2302602 | 23 | 33 | nan | nan | nan | Caatinga | 0.6 |
| 6eb1bbab-fa39-33b2-b94b-9523375a5038 | -4.45983 | -38.24846 | 2025-12-12 04:21:00 | NOAA-20 | BEBERIBE | CEARÁ | Brasil | 2302206 | 23 | 33 | nan | nan | nan | Caatinga | 1.0 |
| 6eeeb2ea-725d-3377-a1ca-9491ce83f177 | -5.986 | -44.59466 | 2025-12-12 04:21:00 | NOAA-20 | COLINAS | MARANHÃO | Brasil | 2103505 | 21 | 33 | nan | nan | nan | Cerrado | 2.1 |
| e9a06e65-a2a4-37d5-974b-f4c11b9788c1 | -4.12093 | -47.36118 | 2025-12-12 04:21:00 | NOAA-20 | DOM ELISEU | PARÁ | Brasil | 1502939 | 15 | 33 | nan | nan | nan | Amazônia | 0.8 |
| f0b60ef5-77a4-39bc-a6ce-ba38bfe79820 | -3.21487 | -42.6925 | 2025-12-12 04:21:00 | NOAA-20 | SANTANA DO MARANHÃO | MARANHÃO | Brasil | 2110237 | 21 | 33 | nan | nan | nan | Cerrado | 0.6 |
| 812eae16-3357-3b18-b927-b9fc7f0ebe72 | -3.88273 | -46.12258 | 2025-12-12 04:21:00 | NOAA-20 | ALTO ALEGRE DO PINDARÉ | MARANHÃO | Brasil | 2100477 | 21 | 33 | nan | nan | nan | Amazônia | 1.0 |
| a3e9c552-9d0f-3d2b-88e0-b1cb9cf73678 | -2.42469 | -51.92708 | 2025-12-12 04:21:00 | NOAA-20 | PORTO DE MOZ | PARÁ | Brasil | 1505908 | 15 | 33 | nan | nan | nan | Amazônia | 20.1 |
| 3632be2c-2eed-3dc5-8fa7-2037026e328a | -2.89108 | -53.00669 | 2025-12-12 04:21:00 | NOAA-20 | MEDICILÂNDIA | PARÁ | Brasil | 1504455 | 15 | 33 | nan | nan | nan | Amazônia | 0.5 |
| 3e5cca96-2d53-3de6-9744-92e822d7a783 | -6.23646 | -43.97318 | 2025-12-12 04:21:00 | NOAA-20 | COLINAS | MARANHÃO | Brasil | 2103505 | 21 | 33 | nan | nan | nan | Cerrado | 0.6 |
| ab564f92-e6ab-3e15-bdc4-f5f2dd09035d | -3.60721 | -45.51866 | 2025-12-12 04:21:00 | NOAA-20 | BOM JARDIM | MARANHÃO | Brasil | 2102002 | 21 | 33 | nan | nan | nan | Amazônia | 0.8 |
| 15ea28aa-519a-357c-b762-cdab14bba6a2 | -4.73366 | -43.07145 | 2025-12-12 04:21:00 | NOAA-20 | CAXIAS | MARANHÃO | Brasil | 2103000 | 21 | 33 | nan | nan | nan | Cerrado | 2.5 |
| bb150fc1-c259-3d45-86c0-9342c601d32d | -2.36098 | -47.68799 | 2025-12-12 04:21:00 | NOAA-20 | IPIXUNA DO PARÁ | PARÁ | Brasil | 1503457 | 15 | 33 | nan | nan | nan | Amazônia | 1.3 |
| 187336f5-7ebd-37b3-a28f-f991ae900cd6 | -2.2385 | -46.51444 | 2025-12-12 04:21:00 | NOAA-20 | CACHOEIRA DO PIRIÁ | PARÁ | Brasil | 1501956 | 15 | 33 | nan | nan | nan | Amazônia | 0.9 |
| f0b7460e-374e-37db-b82f-4a5480279a93 | -3.49987 | -52.53203 | 2025-12-12 04:21:00 | NOAA-20 | BRASIL NOVO | PARÁ | Brasil | 1501725 | 15 | 33 | nan | nan | nan | Amazônia | 0.9 |
| 59a10778-e2c1-34df-b73a-acaa41ab4484 | -3.34007 | -53.34036 | 2025-12-12 04:21:00 | NOAA-20 | MEDICILÂNDIA | PARÁ | Brasil | 1504455 | 15 | 33 | nan | nan | nan | Amazônia | 2.2 |
| eeb00058-5527-38ce-b8b3-cc565aa296cc | -8.0394 | -43.099 | 2025-12-12 04:21:00 | NOAA-20 | CANTO DO BURITI | PIAUÍ | Brasil | 2202307 | 22 | 33 | nan | nan | nan | Caatinga | 1.2 |
| ca6909f1-44e4-3496-9b5f-128bf1577fb3 | -4.15854 | -39.24815 | 2025-12-12 04:21:00 | NOAA-20 | CARIDADE | CEARÁ | Brasil | 2303006 | 23 | 33 | nan | nan | nan | Caatinga | 1.1 |
| a76d36a6-b4a2-3cc3-8c1a-6c9dbcb67b98 | -2.88968 | -47.79924 | 2025-12-12 04:21:00 | NOAA-20 | IPIXUNA DO PARÁ | PARÁ | Brasil | 1503457 | 15 | 33 | nan | nan | nan | Amazônia | 1.1 |
| 3da9562a-231b-3143-a461-87187e32c396 | -3.34879 | -53.07222 | 2025-12-12 04:21:00 | NOAA-20 | MEDICILÂNDIA | PARÁ | Brasil | 1504455 | 15 | 33 | nan | nan | nan | Amazônia | 0.6 |
| 4707e699-2ba8-336e-8d86-e8057c43f287 | -3.23834 | -47.47433 | 2025-12-12 04:21:00 | NOAA-20 | PARAGOMINAS | PARÁ | Brasil | 1505502 | 15 | 33 | nan | nan | nan | Amazônia | 0.9 |
| 13083b65-f98a-3400-9aeb-f460e984f39d | -8.03479 | -43.10602 | 2025-12-12 04:21:00 | NOAA-20 | CANTO DO BURITI | PIAUÍ | Brasil | 2202307 | 22 | 33 | nan | nan | nan | Caatinga | 1.6 |
| dbca414b-a46b-32fa-b247-40437bc7564e | -3.38652 | -47.18731 | 2025-12-12 04:21:00 | NOAA-20 | PARAGOMINAS | PARÁ | Brasil | 1505502 | 15 | 33 | nan | nan | nan | Amazônia | 2.1 |
| 4dd6133e-3598-3bed-a634-54a7a7011f0d | -5.67611 | -41.86341 | 2025-12-12 04:21:00 | NOAA-20 | SÃO JOÃO DA SERRA | PIAUÍ | Brasil | 2209906 | 22 | 33 | nan | nan | nan | Caatinga | 2.7 |
| a6cd4f11-950d-3696-894e-f7a7862292bd | -2.41771 | -45.83165 | 2025-12-12 04:21:00 | NOAA-20 | PRESIDENTE MÉDICI | MARANHÃO | Brasil | 2109239 | 21 | 33 | nan | nan | nan | Amazônia | 1.6 |
| ef528c61-e90e-34c5-b8c1-160850503992 | -4.74389 | -49.8032 | 2025-12-12 04:21:00 | NOAA-20 | NOVO REPARTIMENTO | PARÁ | Brasil | 1505064 | 15 | 33 | nan | nan | nan | Amazônia | 0.8 |
| 87ecd3cf-11d6-3b6c-b15c-895b704cc3a5 | -1.8274 | -46.52625 | 2025-12-12 04:21:00 | NOAA-20 | CACHOEIRA DO PIRIÁ | PARÁ | Brasil | 1501956 | 15 | 33 | nan | nan | nan | Amazônia | 0.9 |
| 239dbd89-46fc-387d-b4b1-2a544b8db2d6 | -3.14158 | -39.57615 | 2025-12-12 04:21:00 | NOAA-20 | ITAPIPOCA | CEARÁ | Brasil | 2306405 | 23 | 33 | nan | nan | nan | Caatinga | 1.6 |
| e78d37cc-e542-3b01-9bee-b07a333f7f22 | -3.51203 | -45.32502 | 2025-12-12 04:21:00 | NOAA-20 | MONÇÃO | MARANHÃO | Brasil | 2106904 | 21 | 33 | nan | nan | nan | Amazônia | 1.0 |
| f07353cc-79b3-3455-b9bf-0edaa6aa27ba | -3.3041 | -42.52951 | 2025-12-12 04:21:00 | NOAA-20 | SÃO BERNARDO | MARANHÃO | Brasil | 2110609 | 21 | 33 | nan | nan | nan | Cerrado | 2.7 |
| 6b6a7258-f192-3c17-840d-b2dde4bb4979 | -6.0276 | -43.7002 | 2025-12-12 04:21:00 | NOAA-20 | PASSAGEM FRANCA | MARANHÃO | Brasil | 2107902 | 21 | 33 | nan | nan | nan | Cerrado | 1.8 |
| e4932ab0-ff96-3a2e-9323-212a552a9cd1 | -3.97254 | -42.51214 | 2025-12-12 04:21:00 | NOAA-20 | CAMPO LARGO DO PIAUÍ | PIAUÍ | Brasil | 2202174 | 22 | 33 | nan | nan | nan | Caatinga | 5.4 |
| 27a285d4-f381-3f3c-bcf6-6fec725ff902 | -2.77913 | -45.56892 | 2025-12-12 04:21:00 | NOAA-20 | SANTA HELENA | MARANHÃO | Brasil | 2109809 | 21 | 33 | nan | nan | nan | Amazônia | 0.8 |
| 302fdc04-057c-3b70-afe1-d63d025ebaf1 | -1.18881 | -54.05031 | 2025-12-12 04:21:00 | NOAA-20 | MONTE ALEGRE | PARÁ | Brasil | 1504802 | 15 | 33 | nan | nan | nan | Amazônia | 0.7 |
| 75bdd50b-058b-3443-8e44-3e4fb5f9b621 | -3.87807 | -41.58426 | 2025-12-12 04:21:00 | NOAA-20 | PIRACURUCA | PIAUÍ | Brasil | 2208304 | 22 | 33 | nan | nan | nan | Caatinga | 1.0 |
| f03ef5ae-2423-331a-9d4d-4522c5129c9d | -1.55498 | -45.80938 | 2025-12-12 04:21:00 | NOAA-20 | GODOFREDO VIANA | MARANHÃO | Brasil | 2104305 | 21 | 33 | nan | nan | nan | Amazônia | 2.6 |
| b817f21d-f787-3d64-ab7e-c1a7afff8734 | -7.22409 | -43.11808 | 2025-12-12 04:21:00 | NOAA-20 | FLORIANO | PIAUÍ | Brasil | 2203909 | 22 | 33 | nan | nan | nan | Caatinga | 1.8 |
| ad7efc07-1c8f-3bb6-a4a0-625f96245f13 | -3.01176 | -52.83498 | 2025-12-12 04:21:00 | NOAA-20 | BRASIL NOVO | PARÁ | Brasil | 1501725 | 15 | 33 | nan | nan | nan | Amazônia | 0.8 |
| f9a43413-fbdb-31bf-83f3-260a517fbb44 | -2.90891 | -51.94536 | 2025-12-12 04:21:00 | NOAA-20 | VITÓRIA DO XINGU | PARÁ | Brasil | 1508357 | 15 | 33 | nan | nan | nan | Amazônia | 7.7 |
| 042fa28e-9117-3258-8450-769c2688ee57 | -2.37837 | -48.67662 | 2025-12-12 04:21:00 | NOAA-20 | ACARÁ | PARÁ | Brasil | 1500206 | 15 | 33 | nan | nan | nan | Amazônia | 1.3 |
| 613bf1cd-ef64-3af0-bbec-cb8d6fa47d1d | -4.68262 | -42.72385 | 2025-12-12 04:21:00 | NOAA-20 | UNIÃO | PIAUÍ | Brasil | 2211100 | 22 | 33 | nan | nan | nan | Cerrado | 0.9 |
| d84897a8-0bee-363f-a7d3-8989b456ea13 | -6.51178 | -55.04264 | 2025-12-12 04:21:00 | NOAA-20 | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 0.6 |
| f5616469-fbe1-3180-aabe-96cf2e129aa4 | -2.87887 | -53.01469 | 2025-12-12 04:21:00 | NOAA-20 | MEDICILÂNDIA | PARÁ | Brasil | 1504455 | 15 | 33 | nan | nan | nan | Amazônia | 1.8 |
| e45a66e7-7d42-348c-beb1-924f4ebc385f | -3.60385 | -45.51813 | 2025-12-12 04:21:00 | NOAA-20 | BOM JARDIM | MARANHÃO | Brasil | 2102002 | 21 | 33 | nan | nan | nan | Amazônia | 4.2 |
| 58ea3f0d-a5d1-3ae0-a34a-f2c0ae2a7529 | -3.23064 | -42.07925 | 2025-12-12 04:21:00 | NOAA-20 | MAGALHÃES DE ALMEIDA | MARANHÃO | Brasil | 2106300 | 21 | 33 | nan | nan | nan | Cerrado | 1.4 |
| f4911477-ccc5-3723-91f3-11d454b77511 | -8.91719 | -37.94677 | 2025-12-12 04:21:00 | NOAA-20 | INAJÁ | PERNAMBUCO | Brasil | 2607000 | 26 | 33 | nan | nan | nan | Caatinga | 0.9 |
| 06596fe9-a9ec-367c-8f10-ef562520fe16 | -2.83303 | -46.7373 | 2025-12-12 04:21:00 | NOAA-20 | PARAGOMINAS | PARÁ | Brasil | 1505502 | 15 | 33 | nan | nan | nan | Amazônia | 0.8 |
| 1d5ec70d-e434-301a-b715-d5fce2a22f29 | -3.77186 | -47.16216 | 2025-12-12 04:21:00 | NOAA-20 | ULIANÓPOLIS | PARÁ | Brasil | 1508126 | 15 | 33 | nan | nan | nan | Amazônia | 0.9 |
| 2d0cc818-d40e-3f50-99e7-64e0e0f1adfc | -2.50056 | -51.80344 | 2025-12-12 04:21:00 | NOAA-20 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 7.6 |
| ddc3ed77-099b-3bd3-8a99-063b57782bde | -2.65305 | -51.64314 | 2025-12-12 04:21:00 | NOAA-20 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 0.9 |
| db9a9d83-ad8c-3e66-a409-b615a3bf8eef | -3.68343 | -45.03909 | 2025-12-12 04:21:00 | NOAA-20 | IGARAPÉ DO MEIO | MARANHÃO | Brasil | 2105153 | 21 | 33 | nan | nan | nan | Amazônia | 0.6 |
| ca80220c-8b04-3729-bd8f-88da5ebb5641 | -3.81136 | -47.05264 | 2025-12-12 04:21:00 | NOAA-20 | ITINGA DO MARANHÃO | MARANHÃO | Brasil | 2105427 | 21 | 33 | nan | nan | nan | Amazônia | 1.5 |
| f8891ff3-4ff3-34bc-9a3e-2dacbe793a46 | -2.88363 | -53.01863 | 2025-12-12 04:21:00 | NOAA-20 | MEDICILÂNDIA | PARÁ | Brasil | 1504455 | 15 | 33 | nan | nan | nan | Amazônia | 1.9 |
| 099cfb8a-e9bb-3696-b0be-b01143639183 | -3.86996 | -40.64219 | 2025-12-12 04:21:00 | NOAA-20 | CARIRÉ | CEARÁ | Brasil | 2303105 | 23 | 33 | nan | nan | nan | Caatinga | 3.4 |
| 04f93818-3e2c-3f71-90f9-62de0f046410 | -2.41974 | -51.9263 | 2025-12-12 04:21:00 | NOAA-20 | PORTO DE MOZ | PARÁ | Brasil | 1505908 | 15 | 33 | nan | nan | nan | Amazônia | 4.0 |
| f1f0d33c-580e-3e70-a5f1-4413584ab7d6 | -4.37507 | -43.62918 | 2025-12-12 04:21:00 | NOAA-20 | CODÓ | MARANHÃO | Brasil | 2103307 | 21 | 33 | nan | nan | nan | Cerrado | 1.4 |
| 80150289-9841-32a5-8506-b7fd342f3643 | -2.88474 | -53.0121 | 2025-12-12 04:21:00 | NOAA-20 | MEDICILÂNDIA | PARÁ | Brasil | 1504455 | 15 | 33 | nan | nan | nan | Amazônia | 1.8 |
| 9ed75d71-6f65-3ad9-be87-56185d360641 | -2.65699 | -51.64924 | 2025-12-12 04:21:00 | NOAA-20 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 3.2 |
| 11fe850a-ec08-3c86-b11d-22304c7b869d | -4.45464 | -43.70563 | 2025-12-12 04:21:00 | NOAA-20 | CODÓ | MARANHÃO | Brasil | 2103307 | 21 | 33 | nan | nan | nan | Cerrado | 1.6 |
| 920321a8-20d6-36db-a708-63cddd7c4b97 | -2.6667 | -46.8974 | 2025-12-12 04:21:00 | NOAA-20 | PARAGOMINAS | PARÁ | Brasil | 1505502 | 15 | 33 | nan | nan | nan | Amazônia | 4.4 |
| 977c70d1-3a6f-3606-b72a-0e7459b0e97d | -2.93596 | -53.03073 | 2025-12-12 04:21:00 | NOAA-20 | MEDICILÂNDIA | PARÁ | Brasil | 1504455 | 15 | 33 | nan | nan | nan | Amazônia | 1.0 |
| cf68a559-e05f-3988-976c-b058609e9693 | -3.1264 | -47.7968 | 2025-12-12 04:21:00 | NOAA-20 | PARAGOMINAS | PARÁ | Brasil | 1505502 | 15 | 33 | nan | nan | nan | Amazônia | 0.9 |
| 5bd22d25-d773-3347-b2e2-7b0bb63915c6 | -2.0238 | -46.38535 | 2025-12-12 04:21:00 | NOAA-20 | CACHOEIRA DO PIRIÁ | PARÁ | Brasil | 1501956 | 15 | 33 | nan | nan | nan | Amazônia | 0.8 |
| 11ec5409-1cd5-3680-9d19-216cc7298ef7 | -3.90992 | -46.06265 | 2025-12-12 04:21:00 | NOAA-20 | ALTO ALEGRE DO PINDARÉ | MARANHÃO | Brasil | 2100477 | 21 | 33 | nan | nan | nan | Amazônia | 0.8 |
| 404de79e-3db3-35f7-986c-a09297fe01de | -2.35637 | -54.37366 | 2025-12-12 04:21:00 | NOAA-20 | SANTARÉM | PARÁ | Brasil | 1506807 | 15 | 33 | nan | nan | nan | Amazônia | 4.7 |
| 88463db0-61e4-37b7-87b6-78a46a1b4aaf | -2.48616 | -47.77506 | 2025-12-12 04:21:00 | NOAA-20 | IPIXUNA DO PARÁ | PARÁ | Brasil | 1503457 | 15 | 33 | nan | nan | nan | Amazônia | 3.7 |
| 258fc3aa-1e11-35a7-94d0-8361efb548d9 | -4.04989 | -45.27627 | 2025-12-12 04:21:00 | NOAA-20 | SATUBINHA | MARANHÃO | Brasil | 2111722 | 21 | 33 | nan | nan | nan | Amazônia | 0.6 |
| ea21a1f0-53c7-38fc-ae51-ecf9cb3bb22d | -2.38061 | -48.67936 | 2025-12-12 04:21:00 | NOAA-20 | ACARÁ | PARÁ | Brasil | 1500206 | 15 | 33 | nan | nan | nan | Amazônia | 1.7 |
| 18ea1d3d-af1d-32c7-9308-6c735cd171ab | -8.04109 | -43.11084 | 2025-12-12 04:21:00 | NOAA-20 | CANTO DO BURITI | PIAUÍ | Brasil | 2202307 | 22 | 33 | nan | nan | nan | Caatinga | 1.0 |
| 12f43cb2-1cc9-36c0-a879-d8fc0b18a67c | -3.97708 | -42.50536 | 2025-12-12 04:21:00 | NOAA-20 | CAMPO LARGO DO PIAUÍ | PIAUÍ | Brasil | 2202174 | 22 | 33 | nan | nan | nan | Caatinga | 1.5 |
| 2830ea00-0bfa-3057-a024-02e3a8872704 | -5.67672 | -41.85942 | 2025-12-12 04:21:00 | NOAA-20 | SÃO JOÃO DA SERRA | PIAUÍ | Brasil | 2209906 | 22 | 33 | nan | nan | nan | Caatinga | 3.5 |
| b8264fe4-5bb9-310f-9512-f5184c8ae90c | -2.36472 | -47.68854 | 2025-12-12 04:21:00 | NOAA-20 | IPIXUNA DO PARÁ | PARÁ | Brasil | 1503457 | 15 | 33 | nan | nan | nan | Amazônia | 1.3 |
| 2be54d57-f8e8-3b00-9baf-2d0798c0dc2c | -2.97047 | -52.72462 | 2025-12-12 04:21:00 | NOAA-20 | BRASIL NOVO | PARÁ | Brasil | 1501725 | 15 | 33 | nan | nan | nan | Amazônia | 2.8 |
| 8b08ed5d-9a1d-3d0f-be0a-522ac082a55c | -1.12324 | -46.40152 | 2025-12-12 04:21:00 | NOAA-20 | AUGUSTO CORRÊA | PARÁ | Brasil | 1500909 | 15 | 33 | nan | nan | nan | Amazônia | 0.9 |
| c48fd452-4d48-31e4-80c3-82e513025649 | -3.03424 | -51.20467 | 2025-12-12 04:21:00 | NOAA-20 | ANAPU | PARÁ | Brasil | 1500859 | 15 | 33 | nan | nan | nan | Amazônia | 1.4 |
| b8bf2620-6638-303e-857a-a399d031af63 | -4.73702 | -43.07197 | 2025-12-12 04:21:00 | NOAA-20 | CAXIAS | MARANHÃO | Brasil | 2103000 | 21 | 33 | nan | nan | nan | Cerrado | 2.5 |
| 958ce591-b40d-3bea-bd12-c7c99beb51c5 | -8.03252 | -43.09796 | 2025-12-12 04:21:00 | NOAA-20 | CANTO DO BURITI | PIAUÍ | Brasil | 2202307 | 22 | 33 | nan | nan | nan | Caatinga | 0.9 |
| 056e5e2b-e53c-3df9-8e0c-dbbf6cc18bde | -1.66385 | -46.23213 | 2025-12-12 04:21:00 | NOAA-20 | VISEU | PARÁ | Brasil | 1508308 | 15 | 33 | nan | nan | nan | Amazônia | 1.3 |
| 6e31d8d3-4ed1-3e1d-9967-94eb34600e61 | -1.12298 | -46.40041 | 2025-12-12 04:21:00 | NOAA-20 | AUGUSTO CORRÊA | PARÁ | Brasil | 1500909 | 15 | 33 | nan | nan | nan | Amazônia | 0.8 |
| c41a18e0-9fc0-39eb-ae82-c31028771d6e | -2.09174 | -53.41748 | 2025-12-12 04:21:00 | NOAA-20 | PRAINHA | PARÁ | Brasil | 1506005 | 15 | 33 | nan | nan | nan | Amazônia | 1.5 |
| ac2afe39-e0c2-320d-8809-2c1a775654c6 | -3.93982 | -46.97343 | 2025-12-12 04:21:00 | NOAA-20 | ITINGA DO MARANHÃO | MARANHÃO | Brasil | 2105427 | 21 | 33 | nan | nan | nan | Amazônia | 0.9 |
| 1f3416b4-b836-30f2-b615-06172d00c6b4 | -2.65833 | -51.6493 | 2025-12-12 04:21:00 | NOAA-20 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 1.9 |
| b4bcc575-f479-34b8-8eb6-fea36f867b6a | -3.79861 | -51.37755 | 2025-12-12 04:21:00 | NOAA-20 | ANAPU | PARÁ | Brasil | 1500859 | 15 | 33 | nan | nan | nan | Amazônia | 1.4 |
| 51dad858-5486-3bc7-ac95-a151e1d4bf93 | -6.6063 | -47.6216 | 2025-12-12 04:21:00 | NOAA-20 | PALMEIRAS DO TOCANTINS | TOCANTINS | Brasil | 1713809 | 17 | 33 | nan | nan | nan | Cerrado | 1.3 |
| c5f4a52e-f763-3f84-ad0b-8e4709754954 | -2.22908 | -45.40567 | 2025-12-12 04:21:00 | NOAA-20 | TURILÂNDIA | MARANHÃO | Brasil | 2112456 | 21 | 33 | nan | nan | nan | Amazônia | 2.6 |


[Clique aqui para ver as próximas entradas](README17.md)
