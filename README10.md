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

## Dados Diários - Página 10

| ID | Latitude | Longitude | Data/Hora GMT | Satélite | Município | Estado | País | Município ID | Estado ID | País ID | Dias sem Chuva | Precipitação | Risco de Fogo | Bioma | FRP |
|----|----------|-----------|---------------|----------|-----------|--------|------|--------------|-----------|---------|----------------|--------------|----------------|-------|-----|
| 8b9153f8-e69b-3486-962a-d8f2f9dc534d | -6.38843 | -39.74325 | 2025-10-19 03:42:00 | NOAA-21 | JUCÁS | CEARÁ | Brasil | 2307403 | 23 | 33 | nan | nan | nan | Caatinga | 1.5 |
| 1d442b3b-4f14-3b5b-9f9c-48fdf2dd4e68 | -6.86233 | -46.29381 | 2025-10-19 03:42:00 | NOAA-21 | FORTALEZA DOS NOGUEIRAS | MARANHÃO | Brasil | 2104107 | 21 | 33 | nan | nan | nan | Cerrado | 3.8 |
| 6e3d7840-0bcc-3465-a1ef-f0cf7cb1a98d | -7.18629 | -42.21643 | 2025-10-19 03:42:00 | NOAA-21 | COLÔNIA DO PIAUÍ | PIAUÍ | Brasil | 2202778 | 22 | 33 | nan | nan | nan | Caatinga | 5.1 |
| 3ab3617c-df12-37fa-a9fd-58aa01efda93 | -5.53607 | -46.9887 | 2025-10-19 03:42:00 | NOAA-21 | BURITIRANA | MARANHÃO | Brasil | 2102358 | 21 | 33 | nan | nan | nan | Cerrado | 1.1 |
| 10118824-a41d-3a40-86a8-ac7888563528 | -6.41563 | -43.9164 | 2025-10-19 03:42:00 | NOAA-21 | PARAIBANO | MARANHÃO | Brasil | 2107704 | 21 | 33 | nan | nan | nan | Cerrado | 2.9 |
| 634189ee-9101-3b32-851a-7b002fe98ce3 | -8.43521 | -44.15444 | 2025-10-19 03:42:00 | NOAA-21 | ALVORADA DO GURGUÉIA | PIAUÍ | Brasil | 2200459 | 22 | 33 | nan | nan | nan | Cerrado | 3.1 |
| 2b3492a3-ea0d-3c08-97c8-90e039805d00 | -4.84001 | -42.74706 | 2025-10-19 03:42:00 | NOAA-21 | TERESINA | PIAUÍ | Brasil | 2211001 | 22 | 33 | nan | nan | nan | Cerrado | 5.2 |
| e71edb79-a541-3d0b-b519-10741bffe4d8 | -7.40909 | -44.80483 | 2025-10-19 03:42:00 | NOAA-21 | URUÇUÍ | PIAUÍ | Brasil | 2211209 | 22 | 33 | nan | nan | nan | Cerrado | 6.0 |
| 7e61c942-1990-3b4e-9d9c-295d7fe660f5 | -6.01873 | -41.92149 | 2025-10-19 03:42:00 | NOAA-21 | SANTA CRUZ DOS MILAGRES | PIAUÍ | Brasil | 2209153 | 22 | 33 | nan | nan | nan | Caatinga | 1.2 |
| bdc589f8-7cd7-31ef-9089-57c99fbb9a58 | -5.71263 | -43.82313 | 2025-10-19 03:42:00 | NOAA-21 | BURITI BRAVO | MARANHÃO | Brasil | 2102309 | 21 | 33 | nan | nan | nan | Cerrado | 2.1 |
| 9a81195a-62e6-3b04-b4ad-768411cbf5fd | -8.27717 | -43.35276 | 2025-10-19 03:42:00 | NOAA-21 | CANTO DO BURITI | PIAUÍ | Brasil | 2202307 | 22 | 33 | nan | nan | nan | Caatinga | 1.9 |
| 8ab9ac68-e349-3d0e-aecf-8d6367a63800 | -7.05131 | -41.82556 | 2025-10-19 03:42:00 | NOAA-21 | SÃO JOÃO DA VARJOTA | PIAUÍ | Brasil | 2209955 | 22 | 33 | nan | nan | nan | Caatinga | 5.5 |
| f4904bd6-b21e-3796-9b35-0538868d1072 | -4.28738 | -45.47943 | 2025-10-19 03:42:00 | NOAA-21 | BREJO DE AREIA | MARANHÃO | Brasil | 2102150 | 21 | 33 | nan | nan | nan | Amazônia | 1.4 |
| e17a34e8-775e-3681-af9b-caa026ca1e28 | -5.55222 | -44.95235 | 2025-10-19 03:42:00 | NOAA-21 | TUNTUM | MARANHÃO | Brasil | 2112308 | 21 | 33 | nan | nan | nan | Cerrado | 4.3 |
| 546faf05-61a6-384b-aa80-75924cfb4f77 | -5.1309 | -48.39622 | 2025-10-19 03:42:00 | NOAA-21 | SÃO PEDRO DA ÁGUA BRANCA | MARANHÃO | Brasil | 2111532 | 21 | 33 | nan | nan | nan | Amazônia | 3.1 |
| e6613848-ff57-3c0e-af4a-6e74267f7fba | -6.72593 | -46.31592 | 2025-10-19 03:42:00 | NOAA-21 | FORMOSA DA SERRA NEGRA | MARANHÃO | Brasil | 2104099 | 21 | 33 | nan | nan | nan | Cerrado | 4.9 |
| 66e9464e-bcea-37a9-bb85-1b9246fa4d1c | -5.34073 | -46.06244 | 2025-10-19 03:42:00 | NOAA-21 | GRAJAÚ | MARANHÃO | Brasil | 2104800 | 21 | 33 | nan | nan | nan | Amazônia | 3.4 |
| 13695948-a562-3920-915b-96d302ac7484 | -7.20321 | -42.20009 | 2025-10-19 03:42:00 | NOAA-21 | COLÔNIA DO PIAUÍ | PIAUÍ | Brasil | 2202778 | 22 | 33 | nan | nan | nan | Caatinga | 4.6 |
| bf258f8b-a05f-3353-a969-89020ca27ce9 | -5.31642 | -44.84923 | 2025-10-19 03:42:00 | NOAA-21 | TUNTUM | MARANHÃO | Brasil | 2112308 | 21 | 33 | nan | nan | nan | Cerrado | 8.0 |
| 0149577a-c037-3ce0-8eae-21100d28aaa1 | -5.67453 | -47.99517 | 2025-10-19 03:42:00 | NOAA-21 | ARAGUATINS | TOCANTINS | Brasil | 1702208 | 17 | 33 | nan | nan | nan | Amazônia | 2.5 |
| ba848bb3-f935-3ab8-8ba0-79cb2618ecbc | -6.72512 | -46.32037 | 2025-10-19 03:42:00 | NOAA-21 | FORMOSA DA SERRA NEGRA | MARANHÃO | Brasil | 2104099 | 21 | 33 | nan | nan | nan | Cerrado | 9.1 |
| a10141e7-5cab-3929-b840-71df7fb13fc0 | -9.2472 | -44.3427 | 2025-10-19 03:42:00 | NOAA-21 | BOM JESUS | PIAUÍ | Brasil | 2201903 | 22 | 33 | nan | nan | nan | Cerrado | 2.0 |
| e420c4e0-280a-3cbb-b396-396145ccad96 | -6.34391 | -40.98843 | 2025-10-19 03:42:00 | NOAA-21 | PIMENTEIRAS | PIAUÍ | Brasil | 2208106 | 22 | 33 | nan | nan | nan | Caatinga | 1.4 |
| 1b90cf8a-ca7b-3bdb-8512-8a4dab656a3b | -5.92496 | -45.44819 | 2025-10-19 03:42:00 | NOAA-21 | GRAJAÚ | MARANHÃO | Brasil | 2104800 | 21 | 33 | nan | nan | nan | Cerrado | 3.8 |
| c2948e03-22d8-3a4d-b462-4b93f290e37b | -7.40974 | -44.8013 | 2025-10-19 03:42:00 | NOAA-21 | URUÇUÍ | PIAUÍ | Brasil | 2211209 | 22 | 33 | nan | nan | nan | Cerrado | 6.0 |
| b1204e05-08c2-3b61-b6c4-693353627f55 | -9.25283 | -44.34058 | 2025-10-19 03:42:00 | NOAA-21 | BOM JESUS | PIAUÍ | Brasil | 2201903 | 22 | 33 | nan | nan | nan | Cerrado | 2.0 |
| 75fd9c67-ab10-383b-bdda-ab39177b3364 | -7.2003 | -42.19003 | 2025-10-19 03:42:00 | NOAA-21 | COLÔNIA DO PIAUÍ | PIAUÍ | Brasil | 2202778 | 22 | 33 | nan | nan | nan | Caatinga | 10.7 |
| 64fe457d-670d-3bf2-be2f-ae6b8222f2ca | -5.43638 | -45.36808 | 2025-10-19 03:42:00 | NOAA-21 | BARRA DO CORDA | MARANHÃO | Brasil | 2101608 | 21 | 33 | nan | nan | nan | Cerrado | 2.0 |
| 30ad234b-2604-35d2-b47a-2c0d2b8a426a | -5.10476 | -47.79241 | 2025-10-19 03:42:00 | NOAA-21 | CIDELÂNDIA | MARANHÃO | Brasil | 2103257 | 21 | 33 | nan | nan | nan | Amazônia | 9.4 |
| 20396c49-b66b-3be6-8851-4db48baa9325 | -7.58683 | -43.07148 | 2025-10-19 03:42:00 | NOAA-21 | ITAUEIRA | PIAUÍ | Brasil | 2205102 | 22 | 33 | nan | nan | nan | Caatinga | 2.6 |
| 6adeff78-b337-3fee-8130-4f3d255ec0b7 | -7.49726 | -42.13232 | 2025-10-19 03:42:00 | NOAA-21 | SANTO INÁCIO DO PIAUÍ | PIAUÍ | Brasil | 2209500 | 22 | 33 | nan | nan | nan | Caatinga | 2.1 |
| 5aba51fd-6c0a-3944-ae94-924aff1fadb5 | -7.36922 | -41.95074 | 2025-10-19 03:42:00 | NOAA-21 | SANTO INÁCIO DO PIAUÍ | PIAUÍ | Brasil | 2209500 | 22 | 33 | nan | nan | nan | Caatinga | 2.0 |
| 76c5ffa2-05c1-30bd-9644-816faa2737cf | -7.04952 | -43.94271 | 2025-10-19 03:42:00 | NOAA-21 | MARCOS PARENTE | PIAUÍ | Brasil | 2206001 | 22 | 33 | nan | nan | nan | Cerrado | 2.7 |
| e682c737-89df-3fe0-bae4-b296bcd9f17f | -5.33897 | -44.71747 | 2025-10-19 03:42:00 | NOAA-21 | TUNTUM | MARANHÃO | Brasil | 2112308 | 21 | 33 | nan | nan | nan | Cerrado | 1.7 |
| 57fd1395-4b9b-32fb-9c5e-f1e470170ace | -8.04638 | -41.10704 | 2025-10-19 03:42:00 | NOAA-21 | PAULISTANA | PIAUÍ | Brasil | 2207801 | 22 | 33 | nan | nan | nan | Caatinga | 2.0 |
| 0331dbf0-9989-332d-b7e9-cfd5612b0c0d | -4.75818 | -45.41982 | 2025-10-19 03:42:00 | NOAA-21 | LAGO DA PEDRA | MARANHÃO | Brasil | 2105708 | 21 | 33 | nan | nan | nan | Cerrado | 1.9 |
| b14ecddd-2d03-3b11-98cc-aa74b79665b4 | -5.36794 | -44.93936 | 2025-10-19 03:42:00 | NOAA-21 | BARRA DO CORDA | MARANHÃO | Brasil | 2101608 | 21 | 33 | nan | nan | nan | Cerrado | 2.8 |
| 63fdb752-20ca-3675-9a67-c3ce9a9d0ebc | -7.22063 | -35.11958 | 2025-10-19 03:42:00 | NOAA-21 | CRUZ DO ESPÍRITO SANTO | PARAÍBA | Brasil | 2504900 | 25 | 33 | nan | nan | nan | Mata Atlântica | 0.7 |
| 14d04b48-7015-3c9b-80fc-1bddc4d49a23 | -4.23401 | -44.67865 | 2025-10-19 03:42:00 | NOAA-21 | BACABAL | MARANHÃO | Brasil | 2101202 | 21 | 33 | nan | nan | nan | Cerrado | 1.6 |
| 0c087772-e7b9-323f-a162-c316a1001dfd | -7.19501 | -42.21418 | 2025-10-19 03:42:00 | NOAA-21 | COLÔNIA DO PIAUÍ | PIAUÍ | Brasil | 2202778 | 22 | 33 | nan | nan | nan | Caatinga | 6.0 |
| 696c053d-ee49-3da1-a6d8-32752545d412 | -9.18199 | -43.23323 | 2025-10-19 03:42:00 | NOAA-21 | CARACOL | PIAUÍ | Brasil | 2202505 | 22 | 33 | nan | nan | nan | Caatinga | 2.2 |
| 11f849f9-3210-3480-86dc-17b64c65bcf6 | -8.56175 | -48.51586 | 2025-10-19 03:42:00 | NOAA-21 | GUARAÍ | TOCANTINS | Brasil | 1709302 | 17 | 33 | nan | nan | nan | Cerrado | 1.6 |
| 388ccd1a-a8bc-3e56-881f-aed9db816153 | -6.37232 | -45.75677 | 2025-10-19 03:42:00 | NOAA-21 | FERNANDO FALCÃO | MARANHÃO | Brasil | 2104081 | 21 | 33 | nan | nan | nan | Cerrado | 1.7 |
| 7a714504-0fb9-35a9-b9d0-598d6ce04463 | -7.53103 | -43.93514 | 2025-10-19 03:42:00 | NOAA-21 | SEBASTIÃO LEAL | PIAUÍ | Brasil | 2210631 | 22 | 33 | nan | nan | nan | Cerrado | 2.9 |
| 31f046bb-e763-3063-9f8c-4c53cad9adcb | -4.93414 | -43.41075 | 2025-10-19 03:42:00 | NOAA-21 | CAXIAS | MARANHÃO | Brasil | 2103000 | 21 | 33 | nan | nan | nan | Cerrado | 1.7 |
| 0200313a-a0b3-3e46-9256-646647029a40 | -3.54952 | -46.43827 | 2025-10-19 03:42:00 | NOAA-21 | SÃO JOÃO DO CARÚ | MARANHÃO | Brasil | 2111029 | 21 | 33 | nan | nan | nan | Amazônia | 2.2 |
| 11635966-b2d2-3cb6-a4f7-d271cc0b80c5 | -5.1005 | -47.79255 | 2025-10-19 03:42:00 | NOAA-21 | CIDELÂNDIA | MARANHÃO | Brasil | 2103257 | 21 | 33 | nan | nan | nan | Amazônia | 4.3 |
| afbca04a-ddc8-37d8-b5ec-6d96789f1f54 | -8.22066 | -43.96798 | 2025-10-19 03:42:00 | NOAA-21 | MANOEL EMÍDIO | PIAUÍ | Brasil | 2205904 | 22 | 33 | nan | nan | nan | Cerrado | 0.9 |
| 9c220a8b-2514-353b-8e94-e63bff131f71 | -4.77184 | -45.88823 | 2025-10-19 03:42:00 | NOAA-21 | ARAME | MARANHÃO | Brasil | 2100956 | 21 | 33 | nan | nan | nan | Amazônia | 4.2 |
| 4047b978-8196-3646-bbb8-988b93e5123b | -4.84495 | -42.7477 | 2025-10-19 03:42:00 | NOAA-21 | TERESINA | PIAUÍ | Brasil | 2211001 | 22 | 33 | nan | nan | nan | Cerrado | 5.2 |
| 387dddcf-314c-38ef-b194-64e9f63a63cb | -4.84403 | -42.75309 | 2025-10-19 03:42:00 | NOAA-21 | TERESINA | PIAUÍ | Brasil | 2211001 | 22 | 33 | nan | nan | nan | Cerrado | 5.4 |
| 7ebf46c6-54dc-3706-aa56-3c5e86c567f2 | -7.16048 | -42.36249 | 2025-10-19 03:42:00 | NOAA-21 | OEIRAS | PIAUÍ | Brasil | 2207009 | 22 | 33 | nan | nan | nan | Caatinga | 4.5 |
| aabf2147-9c1b-391f-87fa-e30cf99e46c0 | -8.43624 | -44.14869 | 2025-10-19 03:42:00 | NOAA-21 | ALVORADA DO GURGUÉIA | PIAUÍ | Brasil | 2200459 | 22 | 33 | nan | nan | nan | Cerrado | 4.3 |
| 9bd8ef2f-8b33-3f82-b599-0eef99de80eb | -4.23965 | -44.67959 | 2025-10-19 03:42:00 | NOAA-21 | BACABAL | MARANHÃO | Brasil | 2101202 | 21 | 33 | nan | nan | nan | Cerrado | 2.8 |
| 34e176d5-de2e-312b-825d-7514847d27a4 | -7.21521 | -38.99562 | 2025-10-19 03:42:00 | NOAA-21 | MILAGRES | CEARÁ | Brasil | 2308302 | 23 | 33 | nan | nan | nan | Caatinga | 1.7 |
| 47e0af73-801f-389d-8093-b61ea70787b0 | -7.18431 | -39.66669 | 2025-10-19 03:42:00 | NOAA-21 | SANTANA DO CARIRI | CEARÁ | Brasil | 2312106 | 23 | 33 | nan | nan | nan | Caatinga | 1.5 |
| 91e0715a-daea-38fa-abc1-4f96fdf4380d | -8.43173 | -44.1446 | 2025-10-19 03:42:00 | NOAA-21 | ALVORADA DO GURGUÉIA | PIAUÍ | Brasil | 2200459 | 22 | 33 | nan | nan | nan | Cerrado | 2.7 |
| 54f65001-99af-3b62-a467-1d6f6886c705 | -7.20269 | -42.19632 | 2025-10-19 03:42:00 | NOAA-21 | COLÔNIA DO PIAUÍ | PIAUÍ | Brasil | 2202778 | 22 | 33 | nan | nan | nan | Caatinga | 10.6 |
| 07229cef-3188-32c6-8700-0e4b5fcfe483 | -4.2403 | -44.67575 | 2025-10-19 03:42:00 | NOAA-21 | BACABAL | MARANHÃO | Brasil | 2101202 | 21 | 33 | nan | nan | nan | Cerrado | 2.8 |
| e9ed7498-c11a-30a5-852d-6cb7e593d234 | -5.32017 | -44.84931 | 2025-10-19 03:42:00 | NOAA-21 | TUNTUM | MARANHÃO | Brasil | 2112308 | 21 | 33 | nan | nan | nan | Cerrado | 5.4 |
| 05bf4c02-e8bc-3e0b-9e62-11d1ee098dca | -9.18105 | -43.23837 | 2025-10-19 03:42:00 | NOAA-21 | CARACOL | PIAUÍ | Brasil | 2202505 | 22 | 33 | nan | nan | nan | Caatinga | 1.6 |
| b080c1c2-9eff-34df-8f97-af116d9e8d6e | -7.40779 | -44.812 | 2025-10-19 03:42:00 | NOAA-21 | URUÇUÍ | PIAUÍ | Brasil | 2211209 | 22 | 33 | nan | nan | nan | Cerrado | 2.7 |
| 2d6b0ee6-2141-34b7-80e2-703fca85a501 | -4.58664 | -45.37841 | 2025-10-19 03:42:00 | NOAA-21 | PAULO RAMOS | MARANHÃO | Brasil | 2108108 | 21 | 33 | nan | nan | nan | Cerrado | 1.7 |
| 8083e2a6-2163-3704-be30-126d39f947dc | -8.29985 | -42.30116 | 2025-10-19 03:42:00 | NOAA-21 | SÃO JOÃO DO PIAUÍ | PIAUÍ | Brasil | 2210003 | 22 | 33 | nan | nan | nan | Caatinga | 1.9 |
| bd1930d6-05fe-3b52-821d-77907510a4a2 | -4.77098 | -45.89316 | 2025-10-19 03:42:00 | NOAA-21 | ARAME | MARANHÃO | Brasil | 2100956 | 21 | 33 | nan | nan | nan | Amazônia | 2.9 |
| 85e8ae46-306f-38cc-a926-0dd76d932f16 | -8.61733 | -41.52869 | 2025-10-19 03:42:00 | NOAA-21 | LAGOA DO BARRO DO PIAUÍ | PIAUÍ | Brasil | 2205565 | 22 | 33 | nan | nan | nan | Caatinga | 1.7 |
| d9f6dffd-2222-32d5-9199-2d8adcc5d693 | -3.97474 | -47.58175 | 2025-10-19 03:42:00 | NOAA-21 | ULIANÓPOLIS | PARÁ | Brasil | 1508126 | 15 | 33 | nan | nan | nan | Amazônia | 3.8 |
| 1822b535-1bd0-3c35-abfc-caf77aadd087 | -8.4382 | -44.16709 | 2025-10-19 03:42:00 | NOAA-21 | ALVORADA DO GURGUÉIA | PIAUÍ | Brasil | 2200459 | 22 | 33 | nan | nan | nan | Cerrado | 1.1 |
| 7fca344c-8149-3919-974a-dcfbd60be7c6 | -8.36237 | -46.20753 | 2025-10-19 03:42:00 | NOAA-21 | BALSAS | MARANHÃO | Brasil | 2101400 | 21 | 33 | nan | nan | nan | Cerrado | 3.3 |
| 48beca90-943b-38af-a471-4065fc4fbac9 | -8.04705 | -41.1032 | 2025-10-19 03:42:00 | NOAA-21 | PAULISTANA | PIAUÍ | Brasil | 2207801 | 22 | 33 | nan | nan | nan | Caatinga | 2.5 |
| a27bb80f-a53e-3b87-a528-d667e963850a | -4.15149 | -47.67239 | 2025-10-19 03:42:00 | NOAA-21 | DOM ELISEU | PARÁ | Brasil | 1502939 | 15 | 33 | nan | nan | nan | Amazônia | 2.6 |
| 1098cb1f-53be-3ad9-b091-76802e1168d2 | -5.36856 | -45.27518 | 2025-10-19 03:42:00 | NOAA-21 | BARRA DO CORDA | MARANHÃO | Brasil | 2101608 | 21 | 33 | nan | nan | nan | Cerrado | 2.2 |
| 9d038bda-8851-3f94-b2c7-045bd1d0cffe | -8.6145 | -40.19266 | 2025-10-19 03:42:00 | NOAA-21 | LAGOA GRANDE | PERNAMBUCO | Brasil | 2608750 | 26 | 33 | nan | nan | nan | Caatinga | 75.7 |
| fb168cb0-11dc-33b8-b21e-b801d476ec99 | -5.90806 | -44.25404 | 2025-10-19 03:42:00 | NOAA-21 | JATOBÁ | MARANHÃO | Brasil | 2105450 | 21 | 33 | nan | nan | nan | Cerrado | 2.0 |
| b28cfcd7-0761-3273-a12c-85c28ac0ea8b | -5.63961 | -44.81493 | 2025-10-19 03:42:00 | NOAA-21 | TUNTUM | MARANHÃO | Brasil | 2112308 | 21 | 33 | nan | nan | nan | Cerrado | 5.3 |
| 5c5a5b1d-bca1-32bc-99e0-34b7a48d1e9b | -7.19518 | -42.18539 | 2025-10-19 03:42:00 | NOAA-21 | COLÔNIA DO PIAUÍ | PIAUÍ | Brasil | 2202778 | 22 | 33 | nan | nan | nan | Caatinga | 6.6 |
| c6402a46-32d0-3097-b295-67a9aee90372 | -9.23587 | -46.06192 | 2025-10-19 03:42:00 | NOAA-21 | ALTO PARNAÍBA | MARANHÃO | Brasil | 2100501 | 21 | 33 | nan | nan | nan | Cerrado | 3.0 |
| 07f0466d-160e-347c-bb23-abe8a72bcc8c | -3.46609 | -47.69009 | 2025-10-19 03:42:00 | NOAA-21 | PARAGOMINAS | PARÁ | Brasil | 1505502 | 15 | 33 | nan | nan | nan | Amazônia | 5.3 |
| f90595f5-a374-3387-9a22-a2be230f9fca | -5.31454 | -44.84846 | 2025-10-19 03:42:00 | NOAA-21 | TUNTUM | MARANHÃO | Brasil | 2112308 | 21 | 33 | nan | nan | nan | Cerrado | 5.4 |
| cf90a5a1-db61-35e4-8dd8-4cecaf92873b | -4.239 | -44.68343 | 2025-10-19 03:42:00 | NOAA-21 | BACABAL | MARANHÃO | Brasil | 2101202 | 21 | 33 | nan | nan | nan | Cerrado | 1.8 |
| de14c722-0b55-3711-87bb-10b8c13786a0 | -8.24665 | -43.99697 | 2025-10-19 03:42:00 | NOAA-21 | MANOEL EMÍDIO | PIAUÍ | Brasil | 2205904 | 22 | 33 | nan | nan | nan | Cerrado | 3.6 |
| 7b8495b0-52b2-39cc-9fed-03212bddb7f8 | -6.10482 | -44.8473 | 2025-10-19 03:42:00 | NOAA-21 | FERNANDO FALCÃO | MARANHÃO | Brasil | 2104081 | 21 | 33 | nan | nan | nan | Cerrado | 3.4 |
| 9734b69c-b27c-31d1-a358-99545f81f957 | -5.08607 | -47.18237 | 2025-10-19 03:42:00 | NOAA-21 | AÇAILÂNDIA | MARANHÃO | Brasil | 2100055 | 21 | 33 | nan | nan | nan | Amazônia | 3.1 |
| bb8a33d9-6d0f-3702-b76d-ca472c7bf08b | -5.26984 | -44.81833 | 2025-10-19 03:42:00 | NOAA-21 | TUNTUM | MARANHÃO | Brasil | 2112308 | 21 | 33 | nan | nan | nan | Cerrado | 2.5 |
| 96f2bd84-082c-32ff-a88b-3a3ad61bd0c2 | -5.92568 | -45.44416 | 2025-10-19 03:42:00 | NOAA-21 | GRAJAÚ | MARANHÃO | Brasil | 2104800 | 21 | 33 | nan | nan | nan | Cerrado | 3.8 |
| 20350324-5737-3367-b519-5262f5244bf2 | -4.44415 | -43.22311 | 2025-10-19 03:42:00 | NOAA-21 | ALDEIAS ALTAS | MARANHÃO | Brasil | 2100303 | 21 | 33 | nan | nan | nan | Cerrado | 2.7 |
| 6254230e-1f37-3d59-921e-9fdcaa91561e | -4.244 | -44.68817 | 2025-10-19 03:42:00 | NOAA-21 | BACABAL | MARANHÃO | Brasil | 2101202 | 21 | 33 | nan | nan | nan | Cerrado | 1.8 |
| 26a2a04a-e947-38e5-8c3e-4b59b68b9761 | -4.83459 | -43.01757 | 2025-10-19 03:42:00 | NOAA-21 | CAXIAS | MARANHÃO | Brasil | 2103000 | 21 | 33 | nan | nan | nan | Cerrado | 12.1 |
| 69980304-61d7-3edf-a240-996b2071ebb2 | -9.2579 | -44.34146 | 2025-10-19 03:42:00 | NOAA-21 | BOM JESUS | PIAUÍ | Brasil | 2201903 | 22 | 33 | nan | nan | nan | Cerrado | 2.1 |
| 9283cf47-959a-3119-9337-8b3cd9d7df9d | -7.74269 | -42.51597 | 2025-10-19 03:42:00 | NOAA-21 | SÃO JOSÉ DO PEIXE | PIAUÍ | Brasil | 2210102 | 22 | 33 | nan | nan | nan | Caatinga | 3.3 |
| 9e5a1534-60cc-3690-8133-f93ce5efd4f3 | -5.31527 | -44.84441 | 2025-10-19 03:42:00 | NOAA-21 | TUNTUM | MARANHÃO | Brasil | 2112308 | 21 | 33 | nan | nan | nan | Cerrado | 5.6 |
| c8678c7f-1d08-3c24-b82f-dbab1003661b | -4.91901 | -45.9888 | 2025-10-19 03:42:00 | NOAA-21 | ARAME | MARANHÃO | Brasil | 2100956 | 21 | 33 | nan | nan | nan | Amazônia | 1.5 |
| 3a667b88-9da4-3eee-b1b4-d91b5a578187 | -7.19206 | -42.18377 | 2025-10-19 03:42:00 | NOAA-21 | COLÔNIA DO PIAUÍ | PIAUÍ | Brasil | 2202778 | 22 | 33 | nan | nan | nan | Caatinga | 2.8 |
| 61778b11-7e59-325b-a555-37cc97554d30 | -4.91362 | -45.41622 | 2025-10-19 03:42:00 | NOAA-21 | LAGOA GRANDE DO MARANHÃO | MARANHÃO | Brasil | 2105963 | 21 | 33 | nan | nan | nan | Cerrado | 1.6 |
| d242cba1-6c2b-33f2-b456-4725ab98834d | -4.24335 | -44.69199 | 2025-10-19 03:42:00 | NOAA-21 | BACABAL | MARANHÃO | Brasil | 2101202 | 21 | 33 | nan | nan | nan | Cerrado | 1.4 |
| 48868fdb-a56e-3bd2-afc1-45c2776198fe | -5.21393 | -43.74262 | 2025-10-19 03:42:00 | NOAA-21 | CAXIAS | MARANHÃO | Brasil | 2103000 | 21 | 33 | nan | nan | nan | Cerrado | 2.7 |
| f252bb70-dc7a-3120-8fa2-28e6d78d4c7b | -8.42965 | -44.15624 | 2025-10-19 03:42:00 | NOAA-21 | ALVORADA DO GURGUÉIA | PIAUÍ | Brasil | 2200459 | 22 | 33 | nan | nan | nan | Cerrado | 1.9 |
| 08af2311-1cff-3c97-95aa-1a5ee68aa43b | -7.16041 | -42.36378 | 2025-10-19 03:42:00 | NOAA-21 | OEIRAS | PIAUÍ | Brasil | 2207009 | 22 | 33 | nan | nan | nan | Caatinga | 4.3 |
| 877e252b-e9aa-36f6-80cc-9f4608850c02 | -7.15878 | -42.37343 | 2025-10-19 03:42:00 | NOAA-21 | OEIRAS | PIAUÍ | Brasil | 2207009 | 22 | 33 | nan | nan | nan | Caatinga | 6.9 |
| b5073570-14ed-3cca-becd-e37be00ec620 | -7.18815 | -39.66729 | 2025-10-19 03:42:00 | NOAA-21 | SANTANA DO CARIRI | CEARÁ | Brasil | 2312106 | 23 | 33 | nan | nan | nan | Caatinga | 1.1 |


[Clique aqui para ver as próximas entradas](README11.md)
