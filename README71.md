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

## Dados Diários - Página 71

| ID | Latitude | Longitude | Data/Hora GMT | Satélite | Município | Estado | País | Município ID | Estado ID | País ID | Dias sem Chuva | Precipitação | Risco de Fogo | Bioma | FRP |
|----|----------|-----------|---------------|----------|-----------|--------|------|--------------|-----------|---------|----------------|--------------|----------------|-------|-----|
| 9c9eac77-b165-302f-89c1-91c099eb7f95 | -9.03955 | -47.09319 | 2025-09-12 04:25:00 | NOAA-20 | LIZARDA | TOCANTINS | Brasil | 1712405 | 17 | 33 | nan | nan | nan | Cerrado | 4.0 |
| 5392506f-d486-375a-ac70-4495a1b187cc | -10.68378 | -48.66373 | 2025-09-12 04:25:00 | NOAA-20 | PORTO NACIONAL | TOCANTINS | Brasil | 1718204 | 17 | 33 | nan | nan | nan | Cerrado | 3.1 |
| e3812787-08dd-38a7-b446-d95479fc51f9 | -9.11017 | -47.1188 | 2025-09-12 04:25:00 | NOAA-20 | LIZARDA | TOCANTINS | Brasil | 1712405 | 17 | 33 | nan | nan | nan | Cerrado | 2.2 |
| dc1be4c5-b716-3fdd-82e8-c1624e670933 | -7.51605 | -44.73981 | 2025-09-12 04:25:00 | NOAA-20 | URUÇUÍ | PIAUÍ | Brasil | 2211209 | 22 | 33 | nan | nan | nan | Cerrado | 1.8 |
| 4b183c47-1a01-3332-ad5a-d332e9aad373 | -8.36303 | -44.83244 | 2025-09-12 04:25:00 | NOAA-20 | BAIXA GRANDE DO RIBEIRO | PIAUÍ | Brasil | 2201150 | 22 | 33 | nan | nan | nan | Cerrado | 2.2 |
| 54bc6a83-2683-37f6-a493-5fa1417001bf | -9.77518 | -47.85099 | 2025-09-12 04:25:00 | NOAA-20 | RIO SONO | TOCANTINS | Brasil | 1718758 | 17 | 33 | nan | nan | nan | Cerrado | 3.4 |
| 1cba4cb4-64cf-3333-ad30-d87934e3fd23 | -6.68225 | -44.14835 | 2025-09-12 04:25:00 | NOAA-20 | PASTOS BONS | MARANHÃO | Brasil | 2108009 | 21 | 33 | nan | nan | nan | Cerrado | 8.2 |
| 8b9a9510-aac4-370c-a8bc-04023895d136 | -11.69956 | -48.28576 | 2025-09-12 04:25:00 | NOAA-20 | SÃO VALÉRIO | TOCANTINS | Brasil | 1720499 | 17 | 33 | nan | nan | nan | Cerrado | 1.6 |
| 97b2c5d3-74db-3b7a-9086-072d434a0a88 | -7.51778 | -44.68319 | 2025-09-12 04:25:00 | NOAA-20 | URUÇUÍ | PIAUÍ | Brasil | 2211209 | 22 | 33 | nan | nan | nan | Cerrado | 2.7 |
| 8667739c-ff0b-37a0-8525-1582c33fc724 | -7.44835 | -44.40501 | 2025-09-12 04:25:00 | NOAA-20 | URUÇUÍ | PIAUÍ | Brasil | 2211209 | 22 | 33 | nan | nan | nan | Cerrado | 2.6 |
| 5b0de3b6-49bc-37e4-9a58-d517014000b5 | -7.71464 | -50.35224 | 2025-09-12 04:25:00 | NOAA-20 | PAU D'ARCO | PARÁ | Brasil | 1505551 | 15 | 33 | nan | nan | nan | Amazônia | 3.5 |
| 74a4fed7-03d3-3364-8a74-a00c3994311e | -7.47089 | -44.96498 | 2025-09-12 04:25:00 | NOAA-20 | BENEDITO LEITE | MARANHÃO | Brasil | 2101806 | 21 | 33 | nan | nan | nan | Cerrado | 2.1 |
| bde226de-c2e0-3b8b-a18e-13a09cf23e9b | -8.43004 | -47.25247 | 2025-09-12 04:25:00 | NOAA-20 | GOIATINS | TOCANTINS | Brasil | 1709005 | 17 | 33 | nan | nan | nan | Cerrado | 1.7 |
| c10cd53c-3d33-31f5-93f5-d67dddd864b0 | -9.79808 | -48.8897 | 2025-09-12 04:25:00 | NOAA-20 | BARROLÂNDIA | TOCANTINS | Brasil | 1703107 | 17 | 33 | nan | nan | nan | Cerrado | 2.1 |
| d2bf5114-f05a-3e00-9a2f-2d7948f8f0a9 | -12.11248 | -44.87074 | 2025-09-12 04:25:00 | NOAA-20 | BARREIRAS | BAHIA | Brasil | 2903201 | 29 | 33 | nan | nan | nan | Cerrado | 2.5 |
| 9b669b19-a153-32ee-ba4f-42d897cee92f | -11.36935 | -43.51362 | 2025-09-12 04:25:00 | NOAA-20 | BARRA | BAHIA | Brasil | 2902708 | 29 | 33 | nan | nan | nan | Cerrado | 2.3 |
| 9ff254d1-e080-3ade-9ecb-504864df2e07 | -10.56063 | -43.66024 | 2025-09-12 04:25:00 | NOAA-20 | BURITIRAMA | BAHIA | Brasil | 2904753 | 29 | 33 | nan | nan | nan | Cerrado | 1.2 |
| 1ab18e0f-2453-3c3d-af06-40aad08348a2 | -10.18779 | -46.24268 | 2025-09-12 04:25:00 | NOAA-20 | SÃO FÉLIX DO TOCANTINS | TOCANTINS | Brasil | 1720150 | 17 | 33 | nan | nan | nan | Cerrado | 0.6 |
| 49947bbf-9f2c-38ca-8a32-a288dfc9046d | -7.27493 | -44.6007 | 2025-09-12 04:25:00 | NOAA-20 | BENEDITO LEITE | MARANHÃO | Brasil | 2101806 | 21 | 33 | nan | nan | nan | Cerrado | 1.9 |
| 7d4bc4ee-2e10-32fd-bf01-84cd7269196a | -10.41739 | -50.6171 | 2025-09-12 04:25:00 | NOAA-20 | SANTA TEREZINHA | MATO GROSSO | Brasil | 5107776 | 51 | 33 | nan | nan | nan | Cerrado | 1.7 |
| 72f63e39-1197-3cdf-a76c-cfcf0cca1e25 | -11.11707 | -50.71631 | 2025-09-12 04:25:00 | NOAA-20 | LUCIARA | MATO GROSSO | Brasil | 5105309 | 51 | 33 | nan | nan | nan | Cerrado | 1.1 |
| e737ecc1-bcfc-3562-91fa-74f404d621be | -11.15492 | -45.31708 | 2025-09-12 04:25:00 | NOAA-20 | FORMOSA DO RIO PRETO | BAHIA | Brasil | 2911105 | 29 | 33 | nan | nan | nan | Cerrado | 1.8 |
| ea9661aa-ec77-3c98-9575-c39ce160983a | -12.14371 | -44.8303 | 2025-09-12 04:25:00 | NOAA-20 | ANGICAL | BAHIA | Brasil | 2901403 | 29 | 33 | nan | nan | nan | Cerrado | 1.2 |
| 04c8a3e5-e5d9-367f-b6c8-76301a30cc69 | -8.94537 | -46.7212 | 2025-09-12 04:25:00 | NOAA-20 | BALSAS | MARANHÃO | Brasil | 2101400 | 21 | 33 | nan | nan | nan | Cerrado | 1.8 |
| 22b3f651-01c5-3a12-a5bc-c12869b137cb | -9.73253 | -48.34555 | 2025-09-12 04:25:00 | NOAA-20 | LAJEADO | TOCANTINS | Brasil | 1712009 | 17 | 33 | nan | nan | nan | Cerrado | 1.1 |
| 96db6970-46c6-3059-9ff9-792f588b2041 | -11.69428 | -46.552 | 2025-09-12 04:25:00 | NOAA-20 | NOVO JARDIM | TOCANTINS | Brasil | 1715259 | 17 | 33 | nan | nan | nan | Cerrado | 1.8 |
| 80e1a8a2-f1a2-345f-a427-4026d2ac4770 | -11.87439 | -47.52924 | 2025-09-12 04:25:00 | NOAA-20 | NATIVIDADE | TOCANTINS | Brasil | 1714203 | 17 | 33 | nan | nan | nan | Cerrado | 1.1 |
| a7a73bb2-b352-3ca0-8359-61aa68c8a643 | -10.74752 | -48.18384 | 2025-09-12 04:25:00 | NOAA-20 | MONTE DO CARMO | TOCANTINS | Brasil | 1713601 | 17 | 33 | nan | nan | nan | Cerrado | 8.1 |
| c072b75d-4688-3c16-8aed-04c2696d1526 | -5.96728 | -44.72443 | 2025-09-12 04:25:00 | NOAA-20 | TUNTUM | MARANHÃO | Brasil | 2112308 | 21 | 33 | nan | nan | nan | Cerrado | 8.0 |
| a971f10e-7e87-34bf-b5e4-530a8d0cdf33 | -9.78132 | -47.85221 | 2025-09-12 04:25:00 | NOAA-20 | RIO SONO | TOCANTINS | Brasil | 1718758 | 17 | 33 | nan | nan | nan | Cerrado | 2.1 |
| 58de2d79-1d4f-358d-b40a-7a79ce154cb8 | -9.77462 | -47.85453 | 2025-09-12 04:25:00 | NOAA-20 | RIO SONO | TOCANTINS | Brasil | 1718758 | 17 | 33 | nan | nan | nan | Cerrado | 3.4 |
| a7dfd4ce-a3b4-3948-89a9-fdb741d856bf | -7.31648 | -49.62472 | 2025-09-12 04:25:00 | NOAA-20 | RIO MARIA | PARÁ | Brasil | 1506161 | 15 | 33 | nan | nan | nan | Amazônia | 1.5 |
| abb3f3d2-8bef-33fa-9373-73c53e73e0e6 | -8.89247 | -49.93266 | 2025-09-12 04:25:00 | NOAA-20 | SANTA MARIA DAS BARREIRAS | PARÁ | Brasil | 1506583 | 15 | 33 | nan | nan | nan | Amazônia | 4.2 |
| 696ce9a4-318b-3ab0-b9ae-efbb3b851288 | -10.14077 | -46.30402 | 2025-09-12 04:25:00 | NOAA-20 | ALTO PARNAÍBA | MARANHÃO | Brasil | 2100501 | 21 | 33 | nan | nan | nan | Cerrado | 0.4 |
| d7bca436-cc00-3900-8e7a-f8a2c323c7be | -11.67377 | -46.59622 | 2025-09-12 04:25:00 | NOAA-20 | NOVO JARDIM | TOCANTINS | Brasil | 1715259 | 17 | 33 | nan | nan | nan | Cerrado | 1.5 |
| 78794e0e-5957-3dc3-8825-b28a13494114 | -10.87581 | -45.56749 | 2025-09-12 04:25:00 | NOAA-20 | FORMOSA DO RIO PRETO | BAHIA | Brasil | 2911105 | 29 | 33 | nan | nan | nan | Cerrado | 1.0 |
| eafd6712-e7be-348f-8d37-25268f18e63b | -8.88034 | -49.56183 | 2025-09-12 04:25:00 | NOAA-20 | ARAGUACEMA | TOCANTINS | Brasil | 1701903 | 17 | 33 | nan | nan | nan | Cerrado | 1.4 |
| d3549e42-8f8e-38a8-bf73-cfce2489c384 | -8.2199 | -49.4995 | 2025-09-12 04:25:00 | NOAA-20 | CONCEIÇÃO DO ARAGUAIA | PARÁ | Brasil | 1502707 | 15 | 33 | nan | nan | nan | Amazônia | 1.0 |
| 82adfa8d-b513-3906-bcfd-e63607ea457e | -11.66653 | -46.57676 | 2025-09-12 04:25:00 | NOAA-20 | NOVO JARDIM | TOCANTINS | Brasil | 1715259 | 17 | 33 | nan | nan | nan | Cerrado | 3.0 |
| 6f9ef9e9-2abd-3211-8bd6-99a33a379751 | -9.01405 | -45.73898 | 2025-09-12 04:25:00 | NOAA-20 | SANTA FILOMENA | PIAUÍ | Brasil | 2209203 | 22 | 33 | nan | nan | nan | Cerrado | 2.3 |
| 6dffa39f-2ae7-3264-a225-204a56f5dd9a | -7.65654 | -50.26496 | 2025-09-12 04:25:00 | NOAA-20 | PAU D'ARCO | PARÁ | Brasil | 1505551 | 15 | 33 | nan | nan | nan | Amazônia | 2.1 |
| bd8b289e-d6cc-31fb-a5c1-739bfb3a5dc3 | -5.76518 | -45.5214 | 2025-09-12 04:25:00 | NOAA-20 | BARRA DO CORDA | MARANHÃO | Brasil | 2101608 | 21 | 33 | nan | nan | nan | Cerrado | 2.0 |
| adaf4d8b-62ac-3a86-a834-d52b77f68d9c | -6.52554 | -44.60121 | 2025-09-12 04:25:00 | NOAA-20 | MIRADOR | MARANHÃO | Brasil | 2106706 | 21 | 33 | nan | nan | nan | Cerrado | 0.9 |
| 9dbbe45b-d55b-36ea-a727-20ec08df94f4 | -8.89351 | -49.93563 | 2025-09-12 04:25:00 | NOAA-20 | SANTA MARIA DAS BARREIRAS | PARÁ | Brasil | 1506583 | 15 | 33 | nan | nan | nan | Amazônia | 10.3 |
| c6367d5d-b346-35b9-8b4d-9605c154cf86 | -6.08463 | -44.82326 | 2025-09-12 04:25:00 | NOAA-20 | FERNANDO FALCÃO | MARANHÃO | Brasil | 2104081 | 21 | 33 | nan | nan | nan | Cerrado | 1.4 |
| 886928ec-459b-319e-af00-6c679cc53a65 | -10.3221 | -48.79675 | 2025-09-12 04:25:00 | NOAA-20 | PARAÍSO DO TOCANTINS | TOCANTINS | Brasil | 1716109 | 17 | 33 | nan | nan | nan | Cerrado | 1.1 |
| 2a08cccd-de2b-3e89-afc4-90d372f66c7f | -7.44204 | -44.42324 | 2025-09-12 04:25:00 | NOAA-20 | URUÇUÍ | PIAUÍ | Brasil | 2211209 | 22 | 33 | nan | nan | nan | Cerrado | 1.3 |
| baf5aafc-17aa-3c5f-b526-5e2b031e0f0f | -9.97949 | -51.70317 | 2025-09-12 04:25:00 | NOAA-20 | VILA RICA | MATO GROSSO | Brasil | 5108600 | 51 | 33 | nan | nan | nan | Amazônia | 3.5 |
| c9ba68c6-9d03-3382-9b95-cfcf6f5f504d | -10.67298 | -48.60244 | 2025-09-12 04:25:00 | NOAA-20 | PORTO NACIONAL | TOCANTINS | Brasil | 1718204 | 17 | 33 | nan | nan | nan | Cerrado | 2.2 |
| 8a86a0d8-680d-3f1a-aa79-d35edcb60a5a | -10.14018 | -47.90345 | 2025-09-12 04:25:00 | NOAA-20 | PALMAS | TOCANTINS | Brasil | 1721000 | 17 | 33 | nan | nan | nan | Cerrado | 1.1 |
| d9e76ee6-52d9-36b7-9abd-a0210fc84d63 | -11.68157 | -46.61203 | 2025-09-12 04:25:00 | NOAA-20 | NOVO JARDIM | TOCANTINS | Brasil | 1715259 | 17 | 33 | nan | nan | nan | Cerrado | 1.8 |
| 637c46cc-05d5-3ba6-bd77-d8790cfb8f5d | -7.31762 | -44.15578 | 2025-09-12 04:25:00 | NOAA-20 | ANTÔNIO ALMEIDA | PIAUÍ | Brasil | 2200806 | 22 | 33 | nan | nan | nan | Cerrado | 1.8 |
| 1384d03d-2052-3fe4-b41a-c715e28108c0 | -6.46718 | -53.4124 | 2025-09-12 04:25:00 | NOAA-20 | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 1.6 |
| fbb8e827-fdfc-3bee-896d-e81c50461602 | -10.65678 | -48.65953 | 2025-09-12 04:25:00 | NOAA-20 | PORTO NACIONAL | TOCANTINS | Brasil | 1718204 | 17 | 33 | nan | nan | nan | Cerrado | 4.0 |
| c6f59628-f0c0-313b-bbbc-16b4f6bc93ca | -9.0146 | -45.73542 | 2025-09-12 04:25:00 | NOAA-20 | SANTA FILOMENA | PIAUÍ | Brasil | 2209203 | 22 | 33 | nan | nan | nan | Cerrado | 2.6 |
| 175aaadb-f727-3ef9-9b7f-ee2ec4598b90 | -9.09023 | -46.94434 | 2025-09-12 04:25:00 | NOAA-20 | LIZARDA | TOCANTINS | Brasil | 1712405 | 17 | 33 | nan | nan | nan | Cerrado | 1.9 |
| ef1a17bd-f732-3265-b0d4-403ef19bdc96 | -11.52395 | -50.59723 | 2025-09-12 04:25:00 | NOAA-20 | LAGOA DA CONFUSÃO | TOCANTINS | Brasil | 1711902 | 17 | 33 | nan | nan | nan | Cerrado | 3.3 |
| a9135c01-17ce-3b59-8580-7fce29d2f919 | -5.22093 | -49.42962 | 2025-09-12 04:25:00 | NOAA-20 | ITUPIRANGA | PARÁ | Brasil | 1503705 | 15 | 33 | nan | nan | nan | Amazônia | 1.1 |
| e14f7e21-f510-3d25-aa67-265be7f14114 | -9.02229 | -46.12126 | 2025-09-12 04:25:00 | NOAA-20 | ALTO PARNAÍBA | MARANHÃO | Brasil | 2100501 | 21 | 33 | nan | nan | nan | Cerrado | 1.2 |
| 68f2f8ac-361a-361a-a02f-f186360e7404 | -11.67766 | -46.59319 | 2025-09-12 04:25:00 | NOAA-20 | NOVO JARDIM | TOCANTINS | Brasil | 1715259 | 17 | 33 | nan | nan | nan | Cerrado | 2.2 |
| c6efa46a-3e92-3e58-a2f6-0dce7d83f5ea | -11.53046 | -50.41512 | 2025-09-12 04:25:00 | NOAA-20 | LAGOA DA CONFUSÃO | TOCANTINS | Brasil | 1711902 | 17 | 33 | nan | nan | nan | Cerrado | 1.8 |
| 8f1b8fa4-48e7-3d00-b7fe-ec4e20d743c5 | -10.12128 | -47.91485 | 2025-09-12 04:25:00 | NOAA-20 | APARECIDA DO RIO NEGRO | TOCANTINS | Brasil | 1701101 | 17 | 33 | nan | nan | nan | Cerrado | 2.1 |
| 7c0ac3e4-61b2-3816-8f3d-e917aa03e81a | -5.69682 | -49.19975 | 2025-09-12 04:25:00 | NOAA-20 | MARABÁ | PARÁ | Brasil | 1504208 | 15 | 33 | nan | nan | nan | Amazônia | 4.3 |
| a9e159c4-d604-386b-a106-650561c5f07b | -11.53963 | -50.40398 | 2025-09-12 04:25:00 | NOAA-20 | FORMOSO DO ARAGUAIA | TOCANTINS | Brasil | 1708205 | 17 | 33 | nan | nan | nan | Cerrado | 29.8 |
| 04ff076f-7eb0-3c90-b867-22eec99678ee | -8.87454 | -51.12292 | 2025-09-12 04:25:00 | NOAA-20 | CUMARU DO NORTE | PARÁ | Brasil | 1502764 | 15 | 33 | nan | nan | nan | Amazônia | 2.2 |
| e931b865-0ae1-3bb1-9f6e-bd754a14999a | -7.54189 | -44.36485 | 2025-09-12 04:25:00 | NOAA-20 | URUÇUÍ | PIAUÍ | Brasil | 2211209 | 22 | 33 | nan | nan | nan | Cerrado | 1.1 |
| 022e9c23-0073-38af-8082-b84e7e3519eb | -10.40915 | -50.59944 | 2025-09-12 04:25:00 | NOAA-20 | SANTA TEREZINHA | MATO GROSSO | Brasil | 5107776 | 51 | 33 | nan | nan | nan | Cerrado | 2.4 |
| 99ceeff2-7b3b-3c51-bbfd-99ec8e7c3e6e | -9.89003 | -51.87001 | 2025-09-12 04:25:00 | NOAA-20 | VILA RICA | MATO GROSSO | Brasil | 5108600 | 51 | 33 | nan | nan | nan | Amazônia | 4.6 |
| f0b22b91-a3cb-3de4-9a0e-1fb13fbecb53 | -6.82728 | -45.65559 | 2025-09-12 04:25:00 | NOAA-20 | SÃO RAIMUNDO DAS MANGABEIRAS | MARANHÃO | Brasil | 2111607 | 21 | 33 | nan | nan | nan | Cerrado | 2.7 |
| 229e30a3-ffac-31a2-93da-d32c6d976445 | -12.1078 | -44.87807 | 2025-09-12 04:25:00 | NOAA-20 | BARREIRAS | BAHIA | Brasil | 2903201 | 29 | 33 | nan | nan | nan | Cerrado | 1.6 |
| 8d4ede90-f12b-3d49-a727-04db1bfd405c | -10.77536 | -45.99737 | 2025-09-12 04:25:00 | NOAA-20 | FORMOSA DO RIO PRETO | BAHIA | Brasil | 2911105 | 29 | 33 | nan | nan | nan | Cerrado | 1.2 |
| 37a3f5d7-b34f-3f30-b63d-0ef63a1f54da | -6.9669 | -44.82508 | 2025-09-12 04:25:00 | NOAA-20 | SÃO FÉLIX DE BALSAS | MARANHÃO | Brasil | 2110807 | 21 | 33 | nan | nan | nan | Cerrado | 5.0 |
| baf349b6-2d1f-3a95-a913-d2ec8e4c0004 | -11.68931 | -46.58409 | 2025-09-12 04:25:00 | NOAA-20 | NOVO JARDIM | TOCANTINS | Brasil | 1715259 | 17 | 33 | nan | nan | nan | Cerrado | 0.8 |
| f69fe37c-9d84-3edf-9c76-720438c74a6e | -9.71109 | -46.9042 | 2025-09-12 04:25:00 | NOAA-20 | LIZARDA | TOCANTINS | Brasil | 1712405 | 17 | 33 | nan | nan | nan | Cerrado | 0.7 |
| 282d4256-1135-378e-8b9c-441e0a784b9a | -9.33913 | -48.9509 | 2025-09-12 04:25:00 | NOAA-20 | DOIS IRMÃOS DO TOCANTINS | TOCANTINS | Brasil | 1707207 | 17 | 33 | nan | nan | nan | Cerrado | 1.5 |
| 078a1379-0058-3c3d-b815-fa6535048b99 | -5.94804 | -42.79116 | 2025-09-12 04:25:00 | NOAA-20 | PALMEIRAIS | PIAUÍ | Brasil | 2207504 | 22 | 33 | nan | nan | nan | Caatinga | 0.5 |
| 0dd92e79-ca7d-307a-8673-de18f35a6cda | -9.49196 | -48.65875 | 2025-09-12 04:25:00 | NOAA-20 | MIRANORTE | TOCANTINS | Brasil | 1713304 | 17 | 33 | nan | nan | nan | Cerrado | 4.7 |
| 258d9b93-0286-322f-bcfa-7adfe581033a | -10.4392 | -50.59933 | 2025-09-12 04:25:00 | NOAA-20 | SANTA TEREZINHA | MATO GROSSO | Brasil | 5107776 | 51 | 33 | nan | nan | nan | Cerrado | 1.4 |
| 3b64f056-eb9b-326a-bb61-dad455acd317 | -12.14135 | -44.87078 | 2025-09-12 04:25:00 | NOAA-20 | BARREIRAS | BAHIA | Brasil | 2903201 | 29 | 33 | nan | nan | nan | Cerrado | 2.1 |
| b86a6692-410b-3a3b-ad37-4b08b74ff218 | -11.5281 | -50.38504 | 2025-09-12 04:25:00 | NOAA-20 | FORMOSO DO ARAGUAIA | TOCANTINS | Brasil | 1708205 | 17 | 33 | nan | nan | nan | Cerrado | 11.3 |
| cb59ac66-6e4c-3449-91e9-1f238c60d2f9 | -11.6982 | -46.59283 | 2025-09-12 04:25:00 | NOAA-20 | NOVO JARDIM | TOCANTINS | Brasil | 1715259 | 17 | 33 | nan | nan | nan | Cerrado | 1.2 |
| 6c8b1dbd-0b0d-3c57-bfaf-38bda51987a0 | -6.94598 | -44.78086 | 2025-09-12 04:25:00 | NOAA-20 | SÃO FÉLIX DE BALSAS | MARANHÃO | Brasil | 2110807 | 21 | 33 | nan | nan | nan | Cerrado | 1.5 |
| a24b707d-c819-3cbe-831b-1bb16d8602a8 | -7.56086 | -44.37948 | 2025-09-12 04:25:00 | NOAA-20 | URUÇUÍ | PIAUÍ | Brasil | 2211209 | 22 | 33 | nan | nan | nan | Cerrado | 1.7 |
| 48ccbd8e-3322-3738-be29-30bf4a294b79 | -8.18639 | -46.105 | 2025-09-12 04:25:00 | NOAA-20 | TASSO FRAGOSO | MARANHÃO | Brasil | 2112001 | 21 | 33 | nan | nan | nan | Cerrado | 2.9 |
| ffc273b8-e1cb-370c-a746-3dcac66e9272 | -6.15352 | -42.6149 | 2025-09-12 04:25:00 | NOAA-20 | JARDIM DO MULATO | PIAUÍ | Brasil | 2205250 | 22 | 33 | nan | nan | nan | Caatinga | 1.3 |
| 390ff98b-8176-3cab-9d65-6b2609cb5b95 | -7.37302 | -43.97742 | 2025-09-12 04:25:00 | NOAA-20 | LANDRI SALES | PIAUÍ | Brasil | 2205607 | 22 | 33 | nan | nan | nan | Cerrado | 0.9 |
| 3b942cee-64e8-30f0-996e-23adbc1751d9 | -7.44379 | -51.83165 | 2025-09-12 04:25:00 | NOAA-20 | SÃO FÉLIX DO XINGU | PARÁ | Brasil | 1507300 | 15 | 33 | nan | nan | nan | Amazônia | 2.3 |
| 08c36f2a-ac71-3de6-b779-aa9d5a71b3fc | -6.55384 | -44.77711 | 2025-09-12 04:25:00 | NOAA-20 | MIRADOR | MARANHÃO | Brasil | 2106706 | 21 | 33 | nan | nan | nan | Cerrado | 2.0 |
| abd31d98-1612-3ebe-9dd4-b7df92866d82 | -11.70427 | -46.53164 | 2025-09-12 04:25:00 | NOAA-20 | NOVO JARDIM | TOCANTINS | Brasil | 1715259 | 17 | 33 | nan | nan | nan | Cerrado | 2.2 |
| 772f0053-18dc-3c91-9583-81b854c52cd8 | -7.40526 | -44.3636 | 2025-09-12 04:25:00 | NOAA-20 | URUÇUÍ | PIAUÍ | Brasil | 2211209 | 22 | 33 | nan | nan | nan | Cerrado | 3.0 |
| 3df11cdf-6bb6-30c1-b6ad-f8d85a1a1f4c | -10.40201 | -50.02856 | 2025-09-12 04:25:00 | NOAA-20 | PIUM | TOCANTINS | Brasil | 1717503 | 17 | 33 | nan | nan | nan | Cerrado | 2.5 |
| 35dd8d53-70f8-3f3f-adf5-c5f25b92f5f7 | -7.53486 | -44.6858 | 2025-09-12 04:25:00 | NOAA-20 | URUÇUÍ | PIAUÍ | Brasil | 2211209 | 22 | 33 | nan | nan | nan | Cerrado | 1.7 |
| 8ea327f8-8f2f-369f-8afc-ce828404c81b | -11.52454 | -50.38442 | 2025-09-12 04:25:00 | NOAA-20 | LAGOA DA CONFUSÃO | TOCANTINS | Brasil | 1711902 | 17 | 33 | nan | nan | nan | Cerrado | 11.3 |
| b32c8e39-f4ad-3ee9-8be1-26b47f4a73fb | -10.67323 | -48.6435 | 2025-09-12 04:25:00 | NOAA-20 | PORTO NACIONAL | TOCANTINS | Brasil | 1718204 | 17 | 33 | nan | nan | nan | Cerrado | 2.1 |
| 3baff46d-cc4e-38f0-accf-1676cf33ade3 | -11.09357 | -48.40216 | 2025-09-12 04:25:00 | NOAA-20 | IPUEIRAS | TOCANTINS | Brasil | 1709807 | 17 | 33 | nan | nan | nan | Cerrado | 1.4 |
| 477cce04-f199-333e-87e3-21be3d96c6d6 | -6.8245 | -45.65157 | 2025-09-12 04:25:00 | NOAA-20 | SÃO RAIMUNDO DAS MANGABEIRAS | MARANHÃO | Brasil | 2111607 | 21 | 33 | nan | nan | nan | Cerrado | 1.7 |
| e6fc0e07-fe6f-3651-a514-e2968e415f04 | -9.16026 | -45.56385 | 2025-09-12 04:25:00 | NOAA-20 | SANTA FILOMENA | PIAUÍ | Brasil | 2209203 | 22 | 33 | nan | nan | nan | Cerrado | 1.6 |
| 131883ad-86da-3bdf-8f5c-337f428dbb5d | -7.55625 | -44.38652 | 2025-09-12 04:25:00 | NOAA-20 | URUÇUÍ | PIAUÍ | Brasil | 2211209 | 22 | 33 | nan | nan | nan | Cerrado | 1.9 |
| 52243d52-6565-306f-93ae-65af50e91e77 | -11.11166 | -51.97947 | 2025-09-12 04:25:00 | NOAA-20 | CANABRAVA DO NORTE | MATO GROSSO | Brasil | 5102694 | 51 | 33 | nan | nan | nan | Amazônia | 1.9 |
| aebad9a7-51dd-31ba-bf72-ceebcd67e4d1 | -11.3158 | -50.78339 | 2025-09-12 04:25:00 | NOAA-20 | SÃO FÉLIX DO ARAGUAIA | MATO GROSSO | Brasil | 5107859 | 51 | 33 | nan | nan | nan | Cerrado | 0.8 |


[Clique aqui para ver as próximas entradas](README72.md)
