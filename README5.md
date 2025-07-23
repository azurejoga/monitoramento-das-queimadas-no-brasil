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

## Dados Diários - Página 5

| ID | Latitude | Longitude | Data/Hora GMT | Satélite | Município | Estado | País | Município ID | Estado ID | País ID | Dias sem Chuva | Precipitação | Risco de Fogo | Bioma | FRP |
|----|----------|-----------|---------------|----------|-----------|--------|------|--------------|-----------|---------|----------------|--------------|----------------|-------|-----|
| 61c523e7-38c2-32a6-8ae2-3deee8b4ddb3 | -10.89185 | -44.36818 | 2025-07-23 03:42:00 | NOAA-20 | SANTA RITA DE CÁSSIA | BAHIA | Brasil | 2928406 | 29 | 33 | nan | nan | nan | Cerrado | 1.8 |
| 589f2b22-489c-36dc-9cb8-592461febc46 | -10.62868 | -45.22635 | 2025-07-23 03:42:00 | NOAA-20 | CRISTALÂNDIA DO PIAUÍ | PIAUÍ | Brasil | 2203008 | 22 | 33 | nan | nan | nan | Cerrado | 2.3 |
| 6d470fc7-75d2-3703-8c3b-fe2373228278 | -7.27665 | -44.36625 | 2025-07-23 03:42:00 | NOAA-20 | URUÇUÍ | PIAUÍ | Brasil | 2211209 | 22 | 33 | nan | nan | nan | Cerrado | 0.9 |
| a12fce17-db84-3b09-95f6-113cd9580a9a | -7.94052 | -44.85188 | 2025-07-23 03:42:00 | NOAA-20 | URUÇUÍ | PIAUÍ | Brasil | 2211209 | 22 | 33 | nan | nan | nan | Cerrado | 1.0 |
| 6b7cef57-d509-3e95-beda-3d815d3fd212 | -5.27978 | -44.95414 | 2025-07-23 03:42:00 | NOAA-20 | BARRA DO CORDA | MARANHÃO | Brasil | 2101608 | 21 | 33 | nan | nan | nan | Cerrado | 0.9 |
| ca6f488c-cb08-3bb6-9b38-360d1b6695b1 | -10.64426 | -45.22933 | 2025-07-23 03:42:00 | NOAA-20 | CRISTALÂNDIA DO PIAUÍ | PIAUÍ | Brasil | 2203008 | 22 | 33 | nan | nan | nan | Cerrado | 0.7 |
| b08ad719-1daa-3571-8b5f-375ed1239fdf | -7.04356 | -45.8444 | 2025-07-23 03:42:00 | NOAA-20 | SÃO RAIMUNDO DAS MANGABEIRAS | MARANHÃO | Brasil | 2111607 | 21 | 33 | nan | nan | nan | Cerrado | 1.0 |
| 4d8b6028-9faf-3f64-87ea-dcbe6bcee5b3 | -7.2014 | -45.33167 | 2025-07-23 03:42:00 | NOAA-20 | SAMBAÍBA | MARANHÃO | Brasil | 2109700 | 21 | 33 | nan | nan | nan | Cerrado | 4.1 |
| 1655765a-91d4-30af-a0f5-d0c033688a9f | -7.23281 | -44.7868 | 2025-07-23 03:42:00 | NOAA-20 | SÃO FÉLIX DE BALSAS | MARANHÃO | Brasil | 2110807 | 21 | 33 | nan | nan | nan | Cerrado | 1.2 |
| 9c1c44e2-06af-33eb-b6e1-99e8546733ec | -7.02463 | -45.84596 | 2025-07-23 03:42:00 | NOAA-20 | SÃO RAIMUNDO DAS MANGABEIRAS | MARANHÃO | Brasil | 2111607 | 21 | 33 | nan | nan | nan | Cerrado | 2.0 |
| 33b05e2e-a83c-36f8-af12-bd3a1337e573 | -7.05922 | -42.88571 | 2025-07-23 03:42:00 | NOAA-20 | NAZARÉ DO PIAUÍ | PIAUÍ | Brasil | 2206704 | 22 | 33 | nan | nan | nan | Caatinga | 1.3 |
| e0d71978-cb41-305a-9de0-a2dc6f1a3769 | -7.04269 | -45.84459 | 2025-07-23 03:42:00 | NOAA-20 | SÃO RAIMUNDO DAS MANGABEIRAS | MARANHÃO | Brasil | 2111607 | 21 | 33 | nan | nan | nan | Cerrado | 1.0 |
| 1fce41a5-58e5-3e23-98b8-f2d5b3df975a | -5.67646 | -43.66718 | 2025-07-23 03:42:00 | NOAA-20 | BURITI BRAVO | MARANHÃO | Brasil | 2102309 | 21 | 33 | nan | nan | nan | Cerrado | 0.9 |
| b663046f-970d-3781-8500-2bf22e40e120 | -7.04789 | -45.85314 | 2025-07-23 03:42:00 | NOAA-20 | SÃO RAIMUNDO DAS MANGABEIRAS | MARANHÃO | Brasil | 2111607 | 21 | 33 | nan | nan | nan | Cerrado | 3.0 |
| 7dfa4a98-38bd-3a3e-9140-93d6bd8e902d | -9.05546 | -45.07424 | 2025-07-23 03:42:00 | NOAA-20 | BOM JESUS | PIAUÍ | Brasil | 2201903 | 22 | 33 | nan | nan | nan | Cerrado | 4.4 |
| 881524c0-2c46-3068-9a11-85d96ba1b0d0 | -9.67331 | -43.72046 | 2025-07-23 03:42:00 | NOAA-20 | PILÃO ARCADO | BAHIA | Brasil | 2924405 | 29 | 33 | nan | nan | nan | Caatinga | 2.1 |
| 16e1b760-477c-33ae-adfd-9bfc81d7a35c | -7.06425 | -43.9302 | 2025-07-23 03:42:00 | NOAA-20 | MARCOS PARENTE | PIAUÍ | Brasil | 2206001 | 22 | 33 | nan | nan | nan | Cerrado | 1.8 |
| 11558feb-0374-30ac-b664-7a048e925dd4 | -9.26362 | -48.56363 | 2025-07-23 03:42:00 | NOAA-20 | RIO DOS BOIS | TOCANTINS | Brasil | 1718709 | 17 | 33 | nan | nan | nan | Cerrado | 1.4 |
| efea573e-c2d2-3f04-acd2-9d5997220ca0 | -10.88044 | -44.35989 | 2025-07-23 03:42:00 | NOAA-20 | SANTA RITA DE CÁSSIA | BAHIA | Brasil | 2928406 | 29 | 33 | nan | nan | nan | Cerrado | 1.7 |
| 8878b2f4-92d9-39f8-a3fc-ab17bd5e93ea | -9.06318 | -45.06204 | 2025-07-23 03:42:00 | NOAA-20 | BOM JESUS | PIAUÍ | Brasil | 2201903 | 22 | 33 | nan | nan | nan | Cerrado | 4.5 |
| 479f31b9-a2d3-39b1-b63b-422e5becc3f5 | -7.74895 | -44.02156 | 2025-07-23 03:42:00 | NOAA-20 | SEBASTIÃO LEAL | PIAUÍ | Brasil | 2210631 | 22 | 33 | nan | nan | nan | Cerrado | 6.7 |
| c6b2abd8-677f-36d4-8a1c-9b6f0444cbde | -8.26863 | -37.49093 | 2025-07-23 03:42:00 | NOAA-20 | SERTÂNIA | PERNAMBUCO | Brasil | 2614105 | 26 | 33 | nan | nan | nan | Caatinga | 0.7 |
| 1cf34e8b-c186-3789-876f-c6d48c318a27 | -10.88913 | -44.3674 | 2025-07-23 03:42:00 | NOAA-20 | SANTA RITA DE CÁSSIA | BAHIA | Brasil | 2928406 | 29 | 33 | nan | nan | nan | Cerrado | 2.4 |
| 5f39c8dc-cd36-3a75-974b-2bbab36f14f6 | -10.64501 | -44.48444 | 2025-07-23 03:42:00 | NOAA-20 | SANTA RITA DE CÁSSIA | BAHIA | Brasil | 2928406 | 29 | 33 | nan | nan | nan | Cerrado | 1.2 |
| a0e695f1-6fe6-36bd-b7d1-04b49a534fae | -9.06197 | -45.06858 | 2025-07-23 03:42:00 | NOAA-20 | BOM JESUS | PIAUÍ | Brasil | 2201903 | 22 | 33 | nan | nan | nan | Cerrado | 3.9 |
| f02d5229-12dc-33bb-a064-9218de59a65c | -7.98777 | -48.40345 | 2025-07-23 03:42:00 | NOAA-20 | PALMEIRANTE | TOCANTINS | Brasil | 1715705 | 17 | 33 | nan | nan | nan | Cerrado | 2.0 |
| be04b5b6-b61b-34bd-95b7-da64849eb207 | -7.24932 | -44.27934 | 2025-07-23 03:42:00 | NOAA-20 | ANTÔNIO ALMEIDA | PIAUÍ | Brasil | 2200806 | 22 | 33 | nan | nan | nan | Cerrado | 3.8 |
| 473e4ca6-0473-33b0-b838-518746f85056 | -6.56467 | -45.60777 | 2025-07-23 03:42:00 | NOAA-20 | MIRADOR | MARANHÃO | Brasil | 2106706 | 21 | 33 | nan | nan | nan | Cerrado | 1.6 |
| 63fc649f-02da-3aa9-a77b-1e119e360980 | -10.88427 | -44.3664 | 2025-07-23 03:42:00 | NOAA-20 | SANTA RITA DE CÁSSIA | BAHIA | Brasil | 2928406 | 29 | 33 | nan | nan | nan | Cerrado | 2.4 |
| 54c3f843-1dbe-32c7-8526-e80e284363be | -10.62817 | -45.2249 | 2025-07-23 03:42:00 | NOAA-20 | CRISTALÂNDIA DO PIAUÍ | PIAUÍ | Brasil | 2203008 | 22 | 33 | nan | nan | nan | Cerrado | 1.2 |
| ffb79eed-e548-3a47-bd9a-72571e31493f | -7.06478 | -43.92722 | 2025-07-23 03:42:00 | NOAA-20 | MARCOS PARENTE | PIAUÍ | Brasil | 2206001 | 22 | 33 | nan | nan | nan | Cerrado | 1.5 |
| 85c369cf-6dfc-3e15-be1e-34f02f97e099 | -4.89228 | -44.96261 | 2025-07-23 03:42:00 | NOAA-20 | ESPERANTINÓPOLIS | MARANHÃO | Brasil | 2104008 | 21 | 33 | nan | nan | nan | Cerrado | 1.0 |
| c0c38761-fa3d-34d1-8671-a4d4d629bd5c | -7.74668 | -44.03433 | 2025-07-23 03:42:00 | NOAA-20 | SEBASTIÃO LEAL | PIAUÍ | Brasil | 2210631 | 22 | 33 | nan | nan | nan | Cerrado | 0.4 |
| 32e2e52a-4aa4-3922-af24-9dea93ba0645 | -7.75854 | -44.02616 | 2025-07-23 03:42:00 | NOAA-20 | SEBASTIÃO LEAL | PIAUÍ | Brasil | 2210631 | 22 | 33 | nan | nan | nan | Cerrado | 2.1 |
| d74c0455-b12f-353d-ad4a-2baeb884bf94 | -5.39422 | -43.24384 | 2025-07-23 03:42:00 | NOAA-20 | MATÕES | MARANHÃO | Brasil | 2106607 | 21 | 33 | nan | nan | nan | Cerrado | 2.8 |
| ded3c7bd-a651-3794-886d-c9869aa0c189 | -9.05787 | -45.06123 | 2025-07-23 03:42:00 | NOAA-20 | BOM JESUS | PIAUÍ | Brasil | 2201903 | 22 | 33 | nan | nan | nan | Cerrado | 3.5 |
| baa992e9-12a3-38d0-871a-743a041f1f83 | -7.88646 | -45.55604 | 2025-07-23 03:42:00 | NOAA-20 | TASSO FRAGOSO | MARANHÃO | Brasil | 2112001 | 21 | 33 | nan | nan | nan | Cerrado | 2.1 |
| e61b6e6a-ab79-30bf-874d-c3429620a9cf | -7.14588 | -46.10009 | 2025-07-23 03:42:00 | NOAA-20 | NOVA COLINAS | MARANHÃO | Brasil | 2107258 | 21 | 33 | nan | nan | nan | Cerrado | 1.1 |
| 5628b1f9-185f-31a4-ab89-9e7340992e58 | -7.02534 | -45.84197 | 2025-07-23 03:42:00 | NOAA-20 | SÃO RAIMUNDO DAS MANGABEIRAS | MARANHÃO | Brasil | 2111607 | 21 | 33 | nan | nan | nan | Cerrado | 1.4 |
| d8cb9dba-39a4-3e1a-bea8-81e7873339c1 | -6.27063 | -45.27688 | 2025-07-23 03:42:00 | NOAA-20 | FERNANDO FALCÃO | MARANHÃO | Brasil | 2104081 | 21 | 33 | nan | nan | nan | Cerrado | 1.7 |
| ded56e74-9e7e-351e-99e2-99818fa1fe04 | -5.73233 | -44.49805 | 2025-07-23 03:42:00 | NOAA-20 | TUNTUM | MARANHÃO | Brasil | 2112308 | 21 | 33 | nan | nan | nan | Cerrado | 1.0 |
| 8537d1cc-77c3-32e0-bfe2-337d2373fd41 | -7.23473 | -44.78977 | 2025-07-23 03:42:00 | NOAA-20 | SÃO FÉLIX DE BALSAS | MARANHÃO | Brasil | 2110807 | 21 | 33 | nan | nan | nan | Cerrado | 1.3 |
| 035ca68b-9bfd-3b31-969f-395dd74f580c | -7.75295 | -44.02834 | 2025-07-23 03:42:00 | NOAA-20 | SEBASTIÃO LEAL | PIAUÍ | Brasil | 2210631 | 22 | 33 | nan | nan | nan | Cerrado | 2.0 |
| ee96b9fc-229c-365b-9f98-260c0dcc449c | -7.75402 | -44.0223 | 2025-07-23 03:42:00 | NOAA-20 | SEBASTIÃO LEAL | PIAUÍ | Brasil | 2210631 | 22 | 33 | nan | nan | nan | Cerrado | 6.7 |
| caad2b8d-fa9c-3bac-8bb7-66fb3374597f | -7.75349 | -44.0253 | 2025-07-23 03:42:00 | NOAA-20 | SEBASTIÃO LEAL | PIAUÍ | Brasil | 2210631 | 22 | 33 | nan | nan | nan | Cerrado | 6.7 |
| 59321dfe-854a-301b-abd4-d926338cae68 | -9.06135 | -45.07191 | 2025-07-23 03:42:00 | NOAA-20 | BOM JESUS | PIAUÍ | Brasil | 2201903 | 22 | 33 | nan | nan | nan | Cerrado | 1.2 |
| d8792a00-8e96-32dd-b9b9-e3837e3e1cf5 | -6.92699 | -44.29973 | 2025-07-23 03:42:00 | NOAA-20 | NOVA IORQUE | MARANHÃO | Brasil | 2107308 | 21 | 33 | nan | nan | nan | Cerrado | 0.8 |
| 876063f2-39cf-3676-a460-42f204e299ca | -6.84946 | -42.73657 | 2025-07-23 03:42:00 | NOAA-20 | NAZARÉ DO PIAUÍ | PIAUÍ | Brasil | 2206704 | 22 | 33 | nan | nan | nan | Caatinga | 3.3 |
| 1408ec89-6a38-358a-a08f-18aa5dc3bc9a | -5.68566 | -43.67477 | 2025-07-23 03:42:00 | NOAA-20 | BURITI BRAVO | MARANHÃO | Brasil | 2102309 | 21 | 33 | nan | nan | nan | Cerrado | 2.4 |
| 3dbab609-08da-32a2-b7cc-7a75ffdb6c8b | -5.67134 | -43.66637 | 2025-07-23 03:42:00 | NOAA-20 | BURITI BRAVO | MARANHÃO | Brasil | 2102309 | 21 | 33 | nan | nan | nan | Cerrado | 0.9 |
| f59c70dd-6863-3965-a233-1d8dddbbca46 | -7.04636 | -38.37355 | 2025-07-23 03:42:00 | NOAA-20 | SÃO JOSÉ DE PIRANHAS | PARAÍBA | Brasil | 2514503 | 25 | 33 | nan | nan | nan | Caatinga | 0.4 |
| ba30ab18-b1ed-3338-80fa-de1ee6afe397 | -9.05608 | -45.0709 | 2025-07-23 03:42:00 | NOAA-20 | BOM JESUS | PIAUÍ | Brasil | 2201903 | 22 | 33 | nan | nan | nan | Cerrado | 4.4 |
| 7d4344f6-ae4a-32c1-add2-b5baadc07a30 | -4.29809 | -48.10057 | 2025-07-23 03:42:00 | NOAA-20 | RONDON DO PARÁ | PARÁ | Brasil | 1506187 | 15 | 33 | nan | nan | nan | Amazônia | 1.9 |
| 0f8af941-0b56-3184-8c1f-973740fc3ccc | -7.25627 | -44.30014 | 2025-07-23 03:42:00 | NOAA-20 | ANTÔNIO ALMEIDA | PIAUÍ | Brasil | 2200806 | 22 | 33 | nan | nan | nan | Cerrado | 2.3 |
| 1ef37af4-d971-32e8-b857-6eb44972a702 | -10.50298 | -44.88534 | 2025-07-23 03:42:00 | NOAA-20 | CORRENTE | PIAUÍ | Brasil | 2202901 | 22 | 33 | nan | nan | nan | Cerrado | 1.1 |
| 25ececd2-40c3-3bb7-81a7-37acff1c5656 | -5.68618 | -43.67173 | 2025-07-23 03:42:00 | NOAA-20 | BURITI BRAVO | MARANHÃO | Brasil | 2102309 | 21 | 33 | nan | nan | nan | Cerrado | 2.4 |
| c00ab4d1-43ce-3e62-921d-08de7e58aad9 | -7.24875 | -44.28254 | 2025-07-23 03:42:00 | NOAA-20 | ANTÔNIO ALMEIDA | PIAUÍ | Brasil | 2200806 | 22 | 33 | nan | nan | nan | Cerrado | 3.8 |
| 85bd41ea-314c-3439-9b50-b71aa0153f14 | -8.28805 | -44.96413 | 2025-07-23 03:42:00 | NOAA-20 | BAIXA GRANDE DO RIBEIRO | PIAUÍ | Brasil | 2201150 | 22 | 33 | nan | nan | nan | Cerrado | 0.9 |
| 508e1a9e-9bd8-309c-aff7-cf28aa90483a | -6.61195 | -42.40117 | 2025-07-23 03:42:00 | NOAA-20 | ARRAIAL | PIAUÍ | Brasil | 2201002 | 22 | 33 | nan | nan | nan | Caatinga | 4.5 |
| c73b7305-9abe-3979-a912-6ca2a9080af9 | -9.06783 | -45.0664 | 2025-07-23 03:42:00 | NOAA-20 | BOM JESUS | PIAUÍ | Brasil | 2201903 | 22 | 33 | nan | nan | nan | Cerrado | 3.9 |
| 8f3b3f40-520a-3547-9e54-575d08826861 | -8.01071 | -37.07508 | 2025-07-23 03:42:00 | NOAA-20 | MONTEIRO | PARAÍBA | Brasil | 2509701 | 25 | 33 | nan | nan | nan | Caatinga | 1.7 |
| e66f664e-d0ec-3fe5-8143-af926532f632 | -6.6073 | -42.34624 | 2025-07-23 03:42:00 | NOAA-20 | TANQUE DO PIAUÍ | PIAUÍ | Brasil | 2210979 | 22 | 33 | nan | nan | nan | Caatinga | 4.3 |
| 7d6d30a7-aff3-356c-8580-9b15bb55fa93 | -5.67594 | -43.67022 | 2025-07-23 03:42:00 | NOAA-20 | BURITI BRAVO | MARANHÃO | Brasil | 2102309 | 21 | 33 | nan | nan | nan | Cerrado | 1.5 |
| 462b72f0-a5f0-3d94-a33a-fc4641873911 | -4.77313 | -45.33982 | 2025-07-23 03:42:00 | NOAA-20 | LAGO DA PEDRA | MARANHÃO | Brasil | 2105708 | 21 | 33 | nan | nan | nan | Cerrado | 0.8 |
| a7d26737-fe87-3053-847b-b2576e2e3743 | -5.82813 | -44.10265 | 2025-07-23 03:42:00 | NOAA-20 | FORTUNA | MARANHÃO | Brasil | 2104206 | 21 | 33 | nan | nan | nan | Cerrado | 0.7 |
| c8fde14c-4fc6-33de-bbb4-418efba035c4 | -7.21837 | -49.6016 | 2025-07-23 03:42:00 | NOAA-20 | RIO MARIA | PARÁ | Brasil | 1506161 | 15 | 33 | nan | nan | nan | Amazônia | 2.2 |
| 1752178a-42ff-3432-896f-246fe1c63a5e | -7.25569 | -44.3034 | 2025-07-23 03:42:00 | NOAA-20 | ANTÔNIO ALMEIDA | PIAUÍ | Brasil | 2200806 | 22 | 33 | nan | nan | nan | Cerrado | 2.3 |
| f10a94b9-9014-37cc-8d9f-f2293d5d72d8 | -4.77891 | -45.34081 | 2025-07-23 03:42:00 | NOAA-20 | LAGO DA PEDRA | MARANHÃO | Brasil | 2105708 | 21 | 33 | nan | nan | nan | Cerrado | 0.8 |
| 678e1829-84fd-32f5-89a5-29cf22f9cc51 | -7.74948 | -44.0186 | 2025-07-23 03:42:00 | NOAA-20 | SEBASTIÃO LEAL | PIAUÍ | Brasil | 2210631 | 22 | 33 | nan | nan | nan | Cerrado | 5.9 |
| 2d0cc63b-30b2-397e-ad9a-872dc4bd91b9 | -9.06375 | -45.05898 | 2025-07-23 03:42:00 | NOAA-20 | BOM JESUS | PIAUÍ | Brasil | 2201903 | 22 | 33 | nan | nan | nan | Cerrado | 4.5 |
| c87f6452-9229-3770-9024-1afc88d3e80f | -7.06613 | -43.92978 | 2025-07-23 03:42:00 | NOAA-20 | MARCOS PARENTE | PIAUÍ | Brasil | 2206001 | 22 | 33 | nan | nan | nan | Cerrado | 1.7 |
| 34f537d9-f705-3a66-b87a-80d1cef46865 | -10.64366 | -45.23251 | 2025-07-23 03:42:00 | NOAA-20 | CRISTALÂNDIA DO PIAUÍ | PIAUÍ | Brasil | 2203008 | 22 | 33 | nan | nan | nan | Cerrado | 0.7 |
| 5efeab2f-7076-31e0-8d07-c64d8337e3f9 | -6.84714 | -42.73937 | 2025-07-23 03:42:00 | NOAA-20 | NAZARÉ DO PIAUÍ | PIAUÍ | Brasil | 2206704 | 22 | 33 | nan | nan | nan | Caatinga | 1.9 |
| d98e93bf-00f3-33c6-aa48-b945243c6be8 | -5.68054 | -43.674 | 2025-07-23 03:42:00 | NOAA-20 | BURITI BRAVO | MARANHÃO | Brasil | 2102309 | 21 | 33 | nan | nan | nan | Cerrado | 2.4 |
| a4615aa4-346f-3347-9bcd-d0d21bf54f25 | -4.89792 | -44.96355 | 2025-07-23 03:42:00 | NOAA-20 | ESPERANTINÓPOLIS | MARANHÃO | Brasil | 2104008 | 21 | 33 | nan | nan | nan | Cerrado | 1.0 |
| 01d9548a-9cee-37f0-aef8-c578d979ad93 | -7.23534 | -44.78633 | 2025-07-23 03:42:00 | NOAA-20 | SÃO FÉLIX DE BALSAS | MARANHÃO | Brasil | 2110807 | 21 | 33 | nan | nan | nan | Cerrado | 1.0 |
| 274d56eb-a062-3c6a-85e2-a30108895ec4 | -7.25509 | -44.30673 | 2025-07-23 03:42:00 | NOAA-20 | ANTÔNIO ALMEIDA | PIAUÍ | Brasil | 2200806 | 22 | 33 | nan | nan | nan | Cerrado | 1.4 |
| eff158eb-4f29-3d4c-828a-cfebc6d9600e | -6.27131 | -45.27301 | 2025-07-23 03:42:00 | NOAA-20 | FERNANDO FALCÃO | MARANHÃO | Brasil | 2104081 | 21 | 33 | nan | nan | nan | Cerrado | 0.9 |
| 94aa14db-0455-3e2f-9454-cdc8397bc419 | -9.05078 | -45.06999 | 2025-07-23 03:42:00 | NOAA-20 | BOM JESUS | PIAUÍ | Brasil | 2201903 | 22 | 33 | nan | nan | nan | Cerrado | 4.4 |
| fcfe3931-f7b1-3f22-8bcb-ae722db087a0 | -5.68669 | -43.66875 | 2025-07-23 03:42:00 | NOAA-20 | BURITI BRAVO | MARANHÃO | Brasil | 2102309 | 21 | 33 | nan | nan | nan | Cerrado | 3.3 |
| e74c18df-4405-3a89-9649-b79a04c1b4de | -7.0421 | -45.85231 | 2025-07-23 03:42:00 | NOAA-20 | SÃO RAIMUNDO DAS MANGABEIRAS | MARANHÃO | Brasil | 2111607 | 21 | 33 | nan | nan | nan | Cerrado | 0.9 |
| b7ffdf29-bfd2-342a-a9ac-7531a121c387 | -6.18807 | -44.38924 | 2025-07-23 03:42:00 | NOAA-20 | MIRADOR | MARANHÃO | Brasil | 2106706 | 21 | 33 | nan | nan | nan | Cerrado | 1.4 |
| 07ca5014-d9d4-3aef-b136-1c34f8208656 | -10.6276 | -45.22804 | 2025-07-23 03:42:00 | NOAA-20 | CRISTALÂNDIA DO PIAUÍ | PIAUÍ | Brasil | 2203008 | 22 | 33 | nan | nan | nan | Cerrado | 1.2 |
| 66d5dfe5-4a90-3d61-bc05-c0e0a0a52875 | -9.05138 | -45.06676 | 2025-07-23 03:42:00 | NOAA-20 | BOM JESUS | PIAUÍ | Brasil | 2201903 | 22 | 33 | nan | nan | nan | Cerrado | 7.3 |
| 45d35ade-8086-3597-ae18-eccb6978ac19 | -9.65579 | -40.5873 | 2025-07-23 03:42:00 | NOAA-20 | JUAZEIRO | BAHIA | Brasil | 2918407 | 29 | 33 | nan | nan | nan | Caatinga | 9.3 |
| 5737f457-e955-3a7b-a7ce-3ad520bfc789 | -6.18751 | -44.39248 | 2025-07-23 03:42:00 | NOAA-20 | MIRADOR | MARANHÃO | Brasil | 2106706 | 21 | 33 | nan | nan | nan | Cerrado | 1.4 |
| b2ac29ca-8174-315f-baa5-093116515690 | -6.56562 | -45.61037 | 2025-07-23 03:42:00 | NOAA-20 | MIRADOR | MARANHÃO | Brasil | 2106706 | 21 | 33 | nan | nan | nan | Cerrado | 1.9 |
| 830626e6-b9e7-3234-b526-c299fc0111f9 | -7.74491 | -44.01509 | 2025-07-23 03:42:00 | NOAA-20 | SEBASTIÃO LEAL | PIAUÍ | Brasil | 2210631 | 22 | 33 | nan | nan | nan | Cerrado | 5.5 |
| bee998be-80a8-306c-8711-0f60a31e75d2 | -7.19522 | -45.33416 | 2025-07-23 03:42:00 | NOAA-20 | SAMBAÍBA | MARANHÃO | Brasil | 2109700 | 21 | 33 | nan | nan | nan | Cerrado | 17.2 |
| 6f45968c-06d6-34c9-8c0a-af4c2d110d9c | -6.95218 | -43.96394 | 2025-07-23 03:42:00 | NOAA-20 | PORTO ALEGRE DO PIAUÍ | PIAUÍ | Brasil | 2208551 | 22 | 33 | nan | nan | nan | Cerrado | 0.9 |
| b3d7473d-b4ed-30a7-bfb5-33280fd590e8 | -10.88698 | -44.36713 | 2025-07-23 03:42:00 | NOAA-20 | SANTA RITA DE CÁSSIA | BAHIA | Brasil | 2928406 | 29 | 33 | nan | nan | nan | Cerrado | 1.8 |
| dad1e957-bd00-3e45-a64f-881de080d292 | -5.67697 | -43.66416 | 2025-07-23 03:42:00 | NOAA-20 | BURITI BRAVO | MARANHÃO | Brasil | 2102309 | 21 | 33 | nan | nan | nan | Cerrado | 0.9 |
| 178d7ae7-f986-338c-b404-721254a2d601 | -4.29692 | -48.10706 | 2025-07-23 03:42:00 | NOAA-20 | RONDON DO PARÁ | PARÁ | Brasil | 1506187 | 15 | 33 | nan | nan | nan | Amazônia | 2.1 |
| a0bd19f2-4432-3fdc-a95d-0c57a03658b0 | -9.06258 | -45.06528 | 2025-07-23 03:42:00 | NOAA-20 | BOM JESUS | PIAUÍ | Brasil | 2201903 | 22 | 33 | nan | nan | nan | Cerrado | 3.9 |
| 3ec9a23b-bfcf-3283-add5-78169f28be41 | -8.26946 | -37.49036 | 2025-07-23 03:42:00 | NOAA-20 | SERTÂNIA | PERNAMBUCO | Brasil | 2614105 | 26 | 33 | nan | nan | nan | Caatinga | 0.4 |
| f59e18ff-4dbd-301e-a022-0d8d05b58de9 | -7.0181 | -45.84921 | 2025-07-23 03:42:00 | NOAA-20 | SÃO RAIMUNDO DAS MANGABEIRAS | MARANHÃO | Brasil | 2111607 | 21 | 33 | nan | nan | nan | Cerrado | 0.6 |
| a3f990b9-6cc5-33aa-bc6b-cc42d30a6ebc | -5.72571 | -44.50418 | 2025-07-23 03:42:00 | NOAA-20 | TUNTUM | MARANHÃO | Brasil | 2112308 | 21 | 33 | nan | nan | nan | Cerrado | 1.4 |
| e5eea657-7e48-340c-97e4-aaf7014a1f25 | -7.75455 | -44.01933 | 2025-07-23 03:42:00 | NOAA-20 | SEBASTIÃO LEAL | PIAUÍ | Brasil | 2210631 | 22 | 33 | nan | nan | nan | Cerrado | 5.9 |
| aae78a88-29c4-362e-9656-259737aff065 | -10.50354 | -44.88234 | 2025-07-23 03:42:00 | NOAA-20 | CORRENTE | PIAUÍ | Brasil | 2202901 | 22 | 33 | nan | nan | nan | Cerrado | 2.0 |
| 7c20c8e8-88c8-33c2-b376-cb763890cd96 | -9.65494 | -40.59227 | 2025-07-23 03:42:00 | NOAA-20 | JUAZEIRO | BAHIA | Brasil | 2918407 | 29 | 33 | nan | nan | nan | Caatinga | 7.5 |


[Clique aqui para ver as próximas entradas](README6.md)
