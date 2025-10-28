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

## Dados Diários - Página 34

| ID | Latitude | Longitude | Data/Hora GMT | Satélite | Município | Estado | País | Município ID | Estado ID | País ID | Dias sem Chuva | Precipitação | Risco de Fogo | Bioma | FRP |
|----|----------|-----------|---------------|----------|-----------|--------|------|--------------|-----------|---------|----------------|--------------|----------------|-------|-----|
| 824caa85-bc3a-3fdc-971a-08ac4c2e0b3d | -6.70325 | -42.04449 | 2025-10-28 04:14:00 | NOAA-21 | OEIRAS | PIAUÍ | Brasil | 2207009 | 22 | 33 | nan | nan | nan | Caatinga | 8.3 |
| a710c1f0-39c8-3558-a1fa-2793e80a9e5b | -9.0443 | -46.93716 | 2025-10-28 04:14:00 | NOAA-21 | BALSAS | MARANHÃO | Brasil | 2101400 | 21 | 33 | nan | nan | nan | Cerrado | 2.7 |
| 00c39f24-69fd-32ba-883b-76186a94b050 | -6.83668 | -43.99517 | 2025-10-28 04:14:00 | NOAA-21 | PORTO ALEGRE DO PIAUÍ | PIAUÍ | Brasil | 2208551 | 22 | 33 | nan | nan | nan | Cerrado | 2.5 |
| 7b74124e-566a-3398-9023-e071ec0840ab | -10.78021 | -43.87234 | 2025-10-28 04:14:00 | NOAA-21 | BURITIRAMA | BAHIA | Brasil | 2904753 | 29 | 33 | nan | nan | nan | Cerrado | 2.1 |
| 6c16d485-c453-3f7f-9520-fb7da7fce3d4 | -7.97134 | -45.45748 | 2025-10-28 04:14:00 | NOAA-21 | RIBEIRO GONÇALVES | PIAUÍ | Brasil | 2208908 | 22 | 33 | nan | nan | nan | Cerrado | 1.8 |
| c3eb0876-54c1-3d01-8acd-5837b5f008b3 | -10.691 | -48.02592 | 2025-10-28 04:14:00 | NOAA-21 | MONTE DO CARMO | TOCANTINS | Brasil | 1713601 | 17 | 33 | nan | nan | nan | Cerrado | 1.4 |
| f5229f36-0126-3a61-b801-861321c5da31 | -6.58867 | -42.69283 | 2025-10-28 04:14:00 | NOAA-21 | FRANCISCO AYRES | PIAUÍ | Brasil | 2204105 | 22 | 33 | nan | nan | nan | Caatinga | 1.8 |
| 03bb09ea-124b-3441-9d38-fbf48f1ca48f | -9.27857 | -46.39486 | 2025-10-28 04:14:00 | NOAA-21 | ALTO PARNAÍBA | MARANHÃO | Brasil | 2100501 | 21 | 33 | nan | nan | nan | Cerrado | 1.4 |
| 5bf76aa3-19e3-34a6-9d5f-47d979fc2189 | -10.02372 | -44.99568 | 2025-10-28 04:14:00 | NOAA-21 | RIACHO FRIO | PIAUÍ | Brasil | 2208858 | 22 | 33 | nan | nan | nan | Cerrado | 2.2 |
| f969d6a8-2e1b-320d-971c-06810984a1e4 | -10.22404 | -49.84581 | 2025-10-28 04:14:00 | NOAA-21 | PIUM | TOCANTINS | Brasil | 1717503 | 17 | 33 | nan | nan | nan | Cerrado | 1.7 |
| 9c878a5d-7a2f-3414-9b0a-aeb7da48d2b7 | -9.29706 | -45.21451 | 2025-10-28 04:14:00 | NOAA-21 | GILBUÉS | PIAUÍ | Brasil | 2204402 | 22 | 33 | nan | nan | nan | Cerrado | 2.5 |
| 08a43775-4076-3f2f-b219-77b3a2eb2003 | -7.81177 | -46.46167 | 2025-10-28 04:14:00 | NOAA-21 | RIACHÃO | MARANHÃO | Brasil | 2109502 | 21 | 33 | nan | nan | nan | Cerrado | 11.4 |
| 69bfc26d-928d-3209-88ff-085c4a97d60d | -6.86545 | -43.44725 | 2025-10-28 04:14:00 | NOAA-21 | JERUMENHA | PIAUÍ | Brasil | 2205300 | 22 | 33 | nan | nan | nan | Cerrado | 1.0 |
| be57dade-4621-31ec-b8b8-72b98c5389c9 | -11.37897 | -49.8587 | 2025-10-28 04:14:00 | NOAA-21 | LAGOA DA CONFUSÃO | TOCANTINS | Brasil | 1711902 | 17 | 33 | nan | nan | nan | Cerrado | 1.1 |
| 4a301959-5a7f-357f-8958-2b1fa85b3534 | -9.21754 | -46.34773 | 2025-10-28 04:14:00 | NOAA-21 | ALTO PARNAÍBA | MARANHÃO | Brasil | 2100501 | 21 | 33 | nan | nan | nan | Cerrado | 4.4 |
| e4272409-5b71-3672-9bf6-deb79bbc6262 | -7.10301 | -45.2202 | 2025-10-28 04:14:00 | NOAA-21 | LORETO | MARANHÃO | Brasil | 2106102 | 21 | 33 | nan | nan | nan | Cerrado | 0.7 |
| cf2621ff-9a01-3332-937b-dcb890e555a3 | -9.72075 | -43.90152 | 2025-10-28 04:14:00 | NOAA-21 | MORRO CABEÇA NO TEMPO | PIAUÍ | Brasil | 2206654 | 22 | 33 | nan | nan | nan | Caatinga | 1.5 |
| 6430a66d-1742-3694-a7d4-2438f3f5a342 | -9.2204 | -46.3523 | 2025-10-28 04:14:00 | NOAA-21 | ALTO PARNAÍBA | MARANHÃO | Brasil | 2100501 | 21 | 33 | nan | nan | nan | Cerrado | 3.9 |
| 8e4585b3-c0bb-33a0-8415-3df8f1ff5721 | -7.42312 | -41.87177 | 2025-10-28 04:14:00 | NOAA-21 | SANTO INÁCIO DO PIAUÍ | PIAUÍ | Brasil | 2209500 | 22 | 33 | nan | nan | nan | Caatinga | 2.0 |
| 200f61c8-85e0-3d2e-94c8-047d18aa79cc | -12.13653 | -45.2363 | 2025-10-28 04:14:00 | NOAA-21 | BARREIRAS | BAHIA | Brasil | 2903201 | 29 | 33 | nan | nan | nan | Cerrado | 0.8 |
| 4322a145-16ba-32d1-85a2-c556bb4e267c | -11.94731 | -43.33779 | 2025-10-28 04:14:00 | NOAA-21 | IBOTIRAMA | BAHIA | Brasil | 2913200 | 29 | 33 | nan | nan | nan | Cerrado | 1.6 |
| 1a241189-f892-31cd-be6a-5c209c3c9ada | -6.12069 | -43.39964 | 2025-10-28 04:14:00 | NOAA-21 | LAGOA DO MATO | MARANHÃO | Brasil | 2105922 | 21 | 33 | nan | nan | nan | Cerrado | 1.7 |
| d9826df8-2234-3aea-8ce4-abbc3d55de75 | -7.78643 | -46.43622 | 2025-10-28 04:14:00 | NOAA-21 | BALSAS | MARANHÃO | Brasil | 2101400 | 21 | 33 | nan | nan | nan | Cerrado | 0.4 |
| eb26001e-9551-314f-ab64-bed3296525a0 | -7.94267 | -45.50381 | 2025-10-28 04:14:00 | NOAA-21 | RIBEIRO GONÇALVES | PIAUÍ | Brasil | 2208908 | 22 | 33 | nan | nan | nan | Cerrado | 4.1 |
| 425dfa8a-0c50-3dc3-b3e5-97b24fb5a189 | -8.1047 | -45.95663 | 2025-10-28 04:14:00 | NOAA-21 | BALSAS | MARANHÃO | Brasil | 2101400 | 21 | 33 | nan | nan | nan | Cerrado | 1.3 |
| e4859d3c-505a-39da-a9e1-d19121166d1b | -10.0886 | -45.33593 | 2025-10-28 04:14:00 | NOAA-21 | SÃO GONÇALO DO GURGUÉIA | PIAUÍ | Brasil | 2209757 | 22 | 33 | nan | nan | nan | Cerrado | 1.7 |
| 56942b40-3f99-3f28-82d0-98723651c492 | -8.11169 | -45.95783 | 2025-10-28 04:14:00 | NOAA-21 | BALSAS | MARANHÃO | Brasil | 2101400 | 21 | 33 | nan | nan | nan | Cerrado | 2.1 |
| b23706af-111c-33c3-9e8a-eba599c5b9a2 | -7.45499 | -49.57858 | 2025-10-28 04:14:00 | NOAA-21 | FLORESTA DO ARAGUAIA | PARÁ | Brasil | 1503044 | 15 | 33 | nan | nan | nan | Amazônia | 0.9 |
| 3eb98e17-3e7c-32c4-9d1f-197ca62753e7 | -8.70578 | -47.98409 | 2025-10-28 04:14:00 | NOAA-21 | SANTA MARIA DO TOCANTINS | TOCANTINS | Brasil | 1718881 | 17 | 33 | nan | nan | nan | Cerrado | 6.5 |
| 2bcd387d-e81a-382f-80a0-a456125bf5f0 | -10.5863 | -49.76334 | 2025-10-28 04:14:00 | NOAA-21 | LAGOA DA CONFUSÃO | TOCANTINS | Brasil | 1711902 | 17 | 33 | nan | nan | nan | Cerrado | 11.0 |
| 51125b02-54ec-35fb-8c8d-998c47cabc9d | -12.20534 | -46.49925 | 2025-10-28 04:14:00 | NOAA-21 | TAGUATINGA | TOCANTINS | Brasil | 1720903 | 17 | 33 | nan | nan | nan | Cerrado | 1.6 |
| 2cad3015-9803-3aac-9abe-46de59329ea5 | -9.97404 | -47.17531 | 2025-10-28 04:14:00 | NOAA-21 | LIZARDA | TOCANTINS | Brasil | 1712405 | 17 | 33 | nan | nan | nan | Cerrado | 2.4 |
| 0efe6dee-6146-38fa-972b-2d4acdc343f0 | -7.95109 | -45.47369 | 2025-10-28 04:14:00 | NOAA-21 | RIBEIRO GONÇALVES | PIAUÍ | Brasil | 2208908 | 22 | 33 | nan | nan | nan | Cerrado | 3.2 |
| e52316bd-03e3-3c68-a84a-fcaaa2f55c58 | -7.98021 | -46.71718 | 2025-10-28 04:14:00 | NOAA-21 | CAMPOS LINDOS | TOCANTINS | Brasil | 1703842 | 17 | 33 | nan | nan | nan | Cerrado | 2.5 |
| d78e1cd7-956f-3e97-9da2-f2f50e591b50 | -6.44724 | -44.60108 | 2025-10-28 04:14:00 | NOAA-21 | MIRADOR | MARANHÃO | Brasil | 2106706 | 21 | 33 | nan | nan | nan | Cerrado | 1.0 |
| 430b94f2-df13-34ed-b808-e8eb99c10a43 | -12.25677 | -47.92395 | 2025-10-28 04:14:00 | NOAA-21 | PARANÃ | TOCANTINS | Brasil | 1716208 | 17 | 33 | nan | nan | nan | Cerrado | 5.3 |
| 8e66d0ef-a0a9-34dc-8e9d-3ea0c1902463 | -9.70652 | -43.9705 | 2025-10-28 04:14:00 | NOAA-21 | MORRO CABEÇA NO TEMPO | PIAUÍ | Brasil | 2206654 | 22 | 33 | nan | nan | nan | Caatinga | 0.8 |
| b2e2dbdb-8d01-3a9c-8816-059da59f9039 | -9.13845 | -51.30353 | 2025-10-28 04:14:00 | NOAA-21 | CUMARU DO NORTE | PARÁ | Brasil | 1502764 | 15 | 33 | nan | nan | nan | Amazônia | 4.4 |
| 199c5e37-7013-3081-bcef-77418b0c90f8 | -6.49571 | -42.21981 | 2025-10-28 04:14:00 | NOAA-21 | VÁRZEA GRANDE | PIAUÍ | Brasil | 2211407 | 22 | 33 | nan | nan | nan | Caatinga | 1.9 |
| b68c9bf8-4555-3fc1-8f83-32b7c1798fbd | -7.45737 | -47.15347 | 2025-10-28 04:14:00 | NOAA-21 | CAROLINA | MARANHÃO | Brasil | 2102804 | 21 | 33 | nan | nan | nan | Cerrado | 1.5 |
| d73dcff5-68c7-39e5-9a19-16c8c59df405 | -11.75082 | -50.21955 | 2025-10-28 04:14:00 | NOAA-21 | FORMOSO DO ARAGUAIA | TOCANTINS | Brasil | 1708205 | 17 | 33 | nan | nan | nan | Cerrado | 1.6 |
| 5404dd2e-f793-3723-be17-366610305df3 | -5.62627 | -47.62176 | 2025-10-28 04:14:00 | NOAA-21 | SÍTIO NOVO DO TOCANTINS | TOCANTINS | Brasil | 1720804 | 17 | 33 | nan | nan | nan | Cerrado | 1.8 |
| a2b38209-40ea-3c12-9563-936852138062 | -8.18663 | -45.71492 | 2025-10-28 04:14:00 | NOAA-21 | TASSO FRAGOSO | MARANHÃO | Brasil | 2112001 | 21 | 33 | nan | nan | nan | Cerrado | 1.7 |
| 6b921de2-1db4-30f1-8c98-164193923b76 | -6.96188 | -46.24146 | 2025-10-28 04:14:00 | NOAA-21 | FORTALEZA DOS NOGUEIRAS | MARANHÃO | Brasil | 2104107 | 21 | 33 | nan | nan | nan | Cerrado | 4.1 |
| 3d27de27-86bc-3203-a9ae-05cc4aae977f | -9.14015 | -45.85915 | 2025-10-28 04:14:00 | NOAA-21 | SANTA FILOMENA | PIAUÍ | Brasil | 2209203 | 22 | 33 | nan | nan | nan | Cerrado | 2.6 |
| c808129f-176e-388b-8b51-e8e1a10a2b93 | -6.88714 | -45.03248 | 2025-10-28 04:14:00 | NOAA-21 | LORETO | MARANHÃO | Brasil | 2106102 | 21 | 33 | nan | nan | nan | Cerrado | 1.0 |
| fcd2f2e8-752c-3726-af25-eb3e25b7a5aa | -7.40972 | -47.77464 | 2025-10-28 04:14:00 | NOAA-21 | FILADÉLFIA | TOCANTINS | Brasil | 1707702 | 17 | 33 | nan | nan | nan | Cerrado | 1.2 |
| 1041ada6-1fb1-30d0-9395-f74024200c2f | -10.88499 | -44.39412 | 2025-10-28 04:14:00 | NOAA-21 | SANTA RITA DE CÁSSIA | BAHIA | Brasil | 2928406 | 29 | 33 | nan | nan | nan | Cerrado | 1.7 |
| fbb89ea7-32b2-3059-b71e-e3b81d2b2762 | -8.03596 | -45.14285 | 2025-10-28 04:14:00 | NOAA-21 | BAIXA GRANDE DO RIBEIRO | PIAUÍ | Brasil | 2201150 | 22 | 33 | nan | nan | nan | Cerrado | 1.1 |
| b57903ae-2b18-33f1-8d72-22a0aa71279e | -5.47238 | -50.16183 | 2025-10-28 04:14:00 | NOAA-21 | MARABÁ | PARÁ | Brasil | 1504208 | 15 | 33 | nan | nan | nan | Amazônia | 2.5 |
| f182b6e3-e9a2-39e4-94ed-07a1de00f143 | -12.56961 | -43.97739 | 2025-10-28 04:14:00 | NOAA-21 | BREJOLÂNDIA | BAHIA | Brasil | 2904407 | 29 | 33 | nan | nan | nan | Cerrado | 1.5 |
| 7932f745-8696-3c7a-a0d0-8c3fd0603abe | -7.9546 | -45.5174 | 2025-10-28 04:14:00 | NOAA-21 | RIBEIRO GONÇALVES | PIAUÍ | Brasil | 2208908 | 22 | 33 | nan | nan | nan | Cerrado | 4.5 |
| 570b558c-9d8e-3fbd-a0ba-6586b10ce464 | -10.77855 | -43.86135 | 2025-10-28 04:14:00 | NOAA-21 | BURITIRAMA | BAHIA | Brasil | 2904753 | 29 | 33 | nan | nan | nan | Cerrado | 0.5 |
| c1759522-6f5c-33da-bb60-6dc17ac4e3c1 | -13.04149 | -45.8561 | 2025-10-28 04:14:00 | NOAA-21 | SÃO DESIDÉRIO | BAHIA | Brasil | 2928901 | 29 | 33 | nan | nan | nan | Cerrado | 0.9 |
| 5df3c7cf-b82e-323e-97a1-9b1040413545 | -10.83309 | -44.95638 | 2025-10-28 04:14:00 | NOAA-21 | CRISTALÂNDIA DO PIAUÍ | PIAUÍ | Brasil | 2203008 | 22 | 33 | nan | nan | nan | Cerrado | 1.4 |
| df551514-cd57-3349-b93f-3c9d5b50c777 | -6.28837 | -42.87482 | 2025-10-28 04:14:00 | NOAA-21 | SÃO FRANCISCO DO MARANHÃO | MARANHÃO | Brasil | 2110906 | 21 | 33 | nan | nan | nan | Cerrado | 1.4 |
| 990b1f21-1e97-36dc-b322-e31c6197b9f8 | -7.78934 | -46.44095 | 2025-10-28 04:14:00 | NOAA-21 | BALSAS | MARANHÃO | Brasil | 2101400 | 21 | 33 | nan | nan | nan | Cerrado | 0.8 |
| d2ba2acf-30e5-3dab-bdd9-32524ce29480 | -6.13306 | -42.69126 | 2025-10-28 04:14:00 | NOAA-21 | ANGICAL DO PIAUÍ | PIAUÍ | Brasil | 2200608 | 22 | 33 | nan | nan | nan | Caatinga | 0.8 |
| 1ac4b68e-5e6b-3277-a894-1483cc70f519 | -9.88225 | -44.89957 | 2025-10-28 04:14:00 | NOAA-21 | RIACHO FRIO | PIAUÍ | Brasil | 2208858 | 22 | 33 | nan | nan | nan | Cerrado | 2.4 |
| 47c05147-1f44-3953-b876-77b3e135b74f | -10.36292 | -47.14464 | 2025-10-28 04:14:00 | NOAA-21 | NOVO ACORDO | TOCANTINS | Brasil | 1715101 | 17 | 33 | nan | nan | nan | Cerrado | 1.7 |
| 69c561d1-d0f7-3eac-850e-8bb2872da4de | -11.28814 | -45.51268 | 2025-10-28 04:14:00 | NOAA-21 | FORMOSA DO RIO PRETO | BAHIA | Brasil | 2911105 | 29 | 33 | nan | nan | nan | Cerrado | 38.5 |
| 13a8d32e-03bf-3ed2-9eba-84f56167ba83 | -9.62591 | -47.72257 | 2025-10-28 04:14:00 | NOAA-21 | RIO SONO | TOCANTINS | Brasil | 1718758 | 17 | 33 | nan | nan | nan | Cerrado | 0.6 |
| a888978f-064b-3616-80fe-b13c515b5803 | -9.29076 | -45.23211 | 2025-10-28 04:14:00 | NOAA-21 | GILBUÉS | PIAUÍ | Brasil | 2204402 | 22 | 33 | nan | nan | nan | Cerrado | 1.7 |
| bdcccf7f-3d3e-3ffa-a7ce-326d0b4e0b3f | -10.86847 | -44.41298 | 2025-10-28 04:14:00 | NOAA-21 | SANTA RITA DE CÁSSIA | BAHIA | Brasil | 2928406 | 29 | 33 | nan | nan | nan | Cerrado | 1.4 |
| ce2928b4-4ff6-3bfe-84b6-b3ce3c26aabc | -7.26592 | -45.01679 | 2025-10-28 04:14:00 | NOAA-21 | SÃO FÉLIX DE BALSAS | MARANHÃO | Brasil | 2110807 | 21 | 33 | nan | nan | nan | Cerrado | 4.2 |
| 0dc13d3f-5183-304e-8b5e-c6b80782464c | -9.31039 | -45.8472 | 2025-10-28 04:14:00 | NOAA-21 | SANTA FILOMENA | PIAUÍ | Brasil | 2209203 | 22 | 33 | nan | nan | nan | Cerrado | 3.9 |
| 758ccef6-52ae-3d11-89ad-03aff73c45b9 | -7.30928 | -42.47929 | 2025-10-28 04:14:00 | NOAA-21 | SÃO FRANCISCO DO PIAUÍ | PIAUÍ | Brasil | 2209708 | 22 | 33 | nan | nan | nan | Caatinga | 1.3 |
| bdb7ffe3-237b-3390-bc74-36d4b5933a3b | -7.76127 | -45.40932 | 2025-10-28 04:14:00 | NOAA-21 | RIBEIRO GONÇALVES | PIAUÍ | Brasil | 2208908 | 22 | 33 | nan | nan | nan | Cerrado | 1.9 |
| e14423b8-c9a3-3198-85af-8025769ae2c6 | -7.2581 | -45.00041 | 2025-10-28 04:14:00 | NOAA-21 | SÃO FÉLIX DE BALSAS | MARANHÃO | Brasil | 2110807 | 21 | 33 | nan | nan | nan | Cerrado | 2.0 |
| c5b8e0a0-062e-3a35-91c2-de5e417b168d | -6.24996 | -41.80758 | 2025-10-28 04:14:00 | NOAA-21 | AROAZES | PIAUÍ | Brasil | 2200905 | 22 | 33 | nan | nan | nan | Caatinga | 0.9 |
| da743b74-de52-3d81-ba84-b930f90a527a | -10.52345 | -47.72879 | 2025-10-28 04:14:00 | NOAA-21 | PONTE ALTA DO TOCANTINS | TOCANTINS | Brasil | 1717909 | 17 | 33 | nan | nan | nan | Cerrado | 1.1 |
| b99572a3-cf3e-3021-bcc9-71d84754be0a | -8.96975 | -50.18572 | 2025-10-28 04:14:00 | NOAA-21 | SANTANA DO ARAGUAIA | PARÁ | Brasil | 1506708 | 15 | 33 | nan | nan | nan | Amazônia | 1.4 |
| 3deeaa07-b889-3fe6-8fba-3f9c4181f43e | -12.64396 | -46.71877 | 2025-10-28 04:14:00 | NOAA-21 | ARRAIAS | TOCANTINS | Brasil | 1702406 | 17 | 33 | nan | nan | nan | Cerrado | 0.5 |
| 28a0cd2a-117b-3c9f-8114-febfba934385 | -7.59978 | -43.58213 | 2025-10-28 04:14:00 | NOAA-21 | CANAVIEIRA | PIAUÍ | Brasil | 2202251 | 22 | 33 | nan | nan | nan | Cerrado | 2.3 |
| ca904d1e-58eb-3388-969b-450c8f704cce | -10.58559 | -49.7673 | 2025-10-28 04:14:00 | NOAA-21 | LAGOA DA CONFUSÃO | TOCANTINS | Brasil | 1711902 | 17 | 33 | nan | nan | nan | Cerrado | 33.2 |
| 10efe9e3-4369-334e-9ec9-62286b46c926 | -6.87394 | -43.5869 | 2025-10-28 04:14:00 | NOAA-21 | GUADALUPE | PIAUÍ | Brasil | 2204501 | 22 | 33 | nan | nan | nan | Cerrado | 1.1 |
| cfcc5bfd-6144-3343-9cd1-ac5f4ba923b4 | -9.97547 | -47.16673 | 2025-10-28 04:14:00 | NOAA-21 | LIZARDA | TOCANTINS | Brasil | 1712405 | 17 | 33 | nan | nan | nan | Cerrado | 1.7 |
| a26823d7-2aea-3318-be9c-856033e30e62 | -10.9531 | -50.27272 | 2025-10-28 04:14:00 | NOAA-21 | LAGOA DA CONFUSÃO | TOCANTINS | Brasil | 1711902 | 17 | 33 | nan | nan | nan | Cerrado | 2.2 |
| afc57716-72c8-302c-9fa6-3ca45060fa1b | -7.0681 | -47.36581 | 2025-10-28 04:14:00 | NOAA-21 | CAROLINA | MARANHÃO | Brasil | 2102804 | 21 | 33 | nan | nan | nan | Cerrado | 4.7 |
| 73419888-111b-39eb-8c51-8bddbd5daeca | -5.73339 | -45.26271 | 2025-10-28 04:14:00 | NOAA-21 | BARRA DO CORDA | MARANHÃO | Brasil | 2101608 | 21 | 33 | nan | nan | nan | Cerrado | 2.4 |
| 36bf7d4e-1ee6-3d97-bbff-ac0e17d220b6 | -7.97669 | -46.73856 | 2025-10-28 04:14:00 | NOAA-21 | CAMPOS LINDOS | TOCANTINS | Brasil | 1703842 | 17 | 33 | nan | nan | nan | Cerrado | 2.8 |
| f00c72fd-c3a0-324f-8686-5a0a25d9ccb2 | -9.95931 | -47.08512 | 2025-10-28 04:14:00 | NOAA-21 | LIZARDA | TOCANTINS | Brasil | 1712405 | 17 | 33 | nan | nan | nan | Cerrado | 2.7 |
| 6c52c271-766a-3a30-a94e-632e3e33045d | -11.74304 | -50.21395 | 2025-10-28 04:14:00 | NOAA-21 | FORMOSO DO ARAGUAIA | TOCANTINS | Brasil | 1708205 | 17 | 33 | nan | nan | nan | Cerrado | 2.9 |
| caad934e-4ca6-3bf0-a0f2-9cbd547fb217 | -5.10833 | -48.48328 | 2025-10-28 04:14:00 | NOAA-21 | BOM JESUS DO TOCANTINS | PARÁ | Brasil | 1501576 | 15 | 33 | nan | nan | nan | Amazônia | 0.8 |
| f6452a5a-1a31-338d-8253-7f6448b74fdd | -10.56029 | -49.78733 | 2025-10-28 04:14:00 | NOAA-21 | LAGOA DA CONFUSÃO | TOCANTINS | Brasil | 1711902 | 17 | 33 | nan | nan | nan | Cerrado | 3.6 |
| b329b1fc-9064-3079-83bd-2aaadce17ed8 | -8.66204 | -43.92362 | 2025-10-28 04:14:00 | NOAA-21 | CRISTINO CASTRO | PIAUÍ | Brasil | 2203107 | 22 | 33 | nan | nan | nan | Cerrado | 0.9 |
| d5dd4b47-158e-3fd1-937b-2a9d7b8e836a | -11.18653 | -49.78836 | 2025-10-28 04:14:00 | NOAA-21 | LAGOA DA CONFUSÃO | TOCANTINS | Brasil | 1711902 | 17 | 33 | nan | nan | nan | Cerrado | 1.0 |
| 60eb0ba4-2560-353b-9457-20b33e337404 | -10.34139 | -44.64722 | 2025-10-28 04:14:00 | NOAA-21 | PARNAGUÁ | PIAUÍ | Brasil | 2207603 | 22 | 33 | nan | nan | nan | Cerrado | 1.7 |
| eefb7336-8dc8-3c43-9eb0-a11d2eecd74e | -10.65218 | -47.9077 | 2025-10-28 04:14:00 | NOAA-21 | MONTE DO CARMO | TOCANTINS | Brasil | 1713601 | 17 | 33 | nan | nan | nan | Cerrado | 3.3 |
| 9dc87dd4-b50a-375f-86ca-04b5dd0c31e6 | -7.97799 | -46.70802 | 2025-10-28 04:14:00 | NOAA-21 | CAMPOS LINDOS | TOCANTINS | Brasil | 1703842 | 17 | 33 | nan | nan | nan | Cerrado | 1.9 |
| a006c564-2e25-3637-90b4-47341f81c07b | -7.38911 | -45.12343 | 2025-10-28 04:14:00 | NOAA-21 | LORETO | MARANHÃO | Brasil | 2106102 | 21 | 33 | nan | nan | nan | Cerrado | 1.4 |
| 69ba4a9d-2ba7-356a-a7df-65d75c80f1c0 | -9.99257 | -48.10385 | 2025-10-28 04:14:00 | NOAA-21 | APARECIDA DO RIO NEGRO | TOCANTINS | Brasil | 1701101 | 17 | 33 | nan | nan | nan | Cerrado | 2.7 |
| 3659cd69-a6d7-314a-b3b3-4444b59dbfa0 | -5.64817 | -46.3312 | 2025-10-28 04:14:00 | NOAA-21 | AMARANTE DO MARANHÃO | MARANHÃO | Brasil | 2100600 | 21 | 33 | nan | nan | nan | Cerrado | 1.0 |
| 8c3a7561-bd76-35f4-8a17-dbde929fd63e | -9.97815 | -46.33922 | 2025-10-28 04:14:00 | NOAA-21 | ALTO PARNAÍBA | MARANHÃO | Brasil | 2100501 | 21 | 33 | nan | nan | nan | Cerrado | 2.0 |
| a3a8f16b-eb0b-3177-9e1e-5b645a38b439 | -8.57166 | -47.02416 | 2025-10-28 04:14:00 | NOAA-21 | RECURSOLÂNDIA | TOCANTINS | Brasil | 1718501 | 17 | 33 | nan | nan | nan | Cerrado | 2.3 |
| caa56151-bf55-3096-8b94-d4314e02bf0d | -7.2315 | -44.99236 | 2025-10-28 04:14:00 | NOAA-21 | SÃO FÉLIX DE BALSAS | MARANHÃO | Brasil | 2110807 | 21 | 33 | nan | nan | nan | Cerrado | 1.8 |
| 319c9fbb-4d35-3454-913c-717ad53ac146 | -9.22195 | -46.36488 | 2025-10-28 04:14:00 | NOAA-21 | ALTO PARNAÍBA | MARANHÃO | Brasil | 2100501 | 21 | 33 | nan | nan | nan | Cerrado | 5.0 |
| 34700fa9-d025-3fcd-b5bd-6e7f0c0822b9 | -7.97024 | -46.75504 | 2025-10-28 04:14:00 | NOAA-21 | CAMPOS LINDOS | TOCANTINS | Brasil | 1703842 | 17 | 33 | nan | nan | nan | Cerrado | 38.7 |
| b4c3591f-1320-310e-aadd-ca66aa45f0bc | -9.03925 | -46.94512 | 2025-10-28 04:14:00 | NOAA-21 | BALSAS | MARANHÃO | Brasil | 2101400 | 21 | 33 | nan | nan | nan | Cerrado | 1.5 |
| f348cf15-e0e7-3df9-a22b-3bb129c9be07 | -6.39972 | -42.62038 | 2025-10-28 04:14:00 | NOAA-21 | REGENERAÇÃO | PIAUÍ | Brasil | 2208809 | 22 | 33 | nan | nan | nan | Caatinga | 3.1 |


[Clique aqui para ver as próximas entradas](README35.md)
