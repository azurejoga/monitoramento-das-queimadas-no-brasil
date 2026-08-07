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

## Dados Diários - Página 7

| ID | Latitude | Longitude | Data/Hora GMT | Satélite | Município | Estado | País | Município ID | Estado ID | País ID | Dias sem Chuva | Precipitação | Risco de Fogo | Bioma | FRP |
|----|----------|-----------|---------------|----------|-----------|--------|------|--------------|-----------|---------|----------------|--------------|----------------|-------|-----|
| 7d3b1bf6-3433-3afa-a5a4-11b4bde4f293 | -4.11369 | -40.50103 | 2026-08-07 04:08:00 | NOAA-21 | VARJOTA | CEARÁ | Brasil | 2313955 | 23 | 33 | nan | nan | nan | Caatinga | 1.4 |
| bda84716-88ca-3077-b9bd-32f5d7a90757 | -4.26758 | -48.19558 | 2026-08-07 04:08:00 | NOAA-21 | RONDON DO PARÁ | PARÁ | Brasil | 1506187 | 15 | 33 | nan | nan | nan | Amazônia | 19.2 |
| 7fd797e9-9988-3553-9e95-6049002a77ba | -4.96386 | -43.00287 | 2026-08-07 04:08:00 | NOAA-21 | TIMON | MARANHÃO | Brasil | 2112209 | 21 | 33 | nan | nan | nan | Cerrado | 1.2 |
| 7b9b7e74-3239-328a-8e1b-e641dfab8c03 | -4.26838 | -48.1908 | 2026-08-07 04:08:00 | NOAA-21 | RONDON DO PARÁ | PARÁ | Brasil | 1506187 | 15 | 33 | nan | nan | nan | Amazônia | 5.0 |
| 04c0c27e-1dd1-3637-9de4-c38705f92c14 | -8.55724 | -45.37025 | 2026-08-07 04:08:00 | NOAA-21 | BAIXA GRANDE DO RIBEIRO | PIAUÍ | Brasil | 2201150 | 22 | 33 | nan | nan | nan | Cerrado | 1.9 |
| 05edf374-4644-3241-9404-b4db4af4d41d | -7.71955 | -46.2239 | 2026-08-07 04:08:00 | NOAA-21 | BALSAS | MARANHÃO | Brasil | 2101400 | 21 | 33 | nan | nan | nan | Cerrado | 2.1 |
| 5424511a-48c6-3223-884d-04df72539bc0 | -7.18058 | -42.33628 | 2026-08-07 04:08:00 | NOAA-21 | OEIRAS | PIAUÍ | Brasil | 2207009 | 22 | 33 | nan | nan | nan | Caatinga | 0.3 |
| 15b17404-900d-3687-b5b4-8423b50a487d | -6.92484 | -41.95049 | 2026-08-07 04:08:00 | NOAA-21 | SÃO JOÃO DA VARJOTA | PIAUÍ | Brasil | 2209955 | 22 | 33 | nan | nan | nan | Caatinga | 2.2 |
| 008001ee-b7ae-31bc-b109-41da79a181c2 | -6.91601 | -41.94201 | 2026-08-07 04:08:00 | NOAA-21 | SÃO JOÃO DA VARJOTA | PIAUÍ | Brasil | 2209955 | 22 | 33 | nan | nan | nan | Caatinga | 2.4 |
| 0e31da16-0422-3342-bc27-d5cb5857ae62 | -3.40255 | -49.77805 | 2026-08-07 04:08:00 | NOAA-21 | BAIÃO | PARÁ | Brasil | 1501204 | 15 | 33 | nan | nan | nan | Amazônia | 1.5 |
| 2f57d417-0ce1-333d-b6d5-a91a1ff3e4d9 | -8.37778 | -49.64539 | 2026-08-07 04:08:00 | NOAA-21 | CONCEIÇÃO DO ARAGUAIA | PARÁ | Brasil | 1502707 | 15 | 33 | nan | nan | nan | Amazônia | 3.5 |
| 71a91e36-a408-3087-a335-205cede62f24 | -4.3704 | -47.7726 | 2026-08-07 04:08:00 | NOAA-21 | DOM ELISEU | PARÁ | Brasil | 1502939 | 15 | 33 | nan | nan | nan | Amazônia | 5.2 |
| 5efb6043-30be-3648-81f0-3ba7bd7975ef | -6.06909 | -49.4932 | 2026-08-07 04:08:00 | NOAA-21 | CURIONÓPOLIS | PARÁ | Brasil | 1502772 | 15 | 33 | nan | nan | nan | Amazônia | 6.4 |
| 20ed069a-9120-3329-8a08-8ef05d804202 | -4.98416 | -45.38481 | 2026-08-07 04:08:00 | NOAA-21 | LAGOA GRANDE DO MARANHÃO | MARANHÃO | Brasil | 2105963 | 21 | 33 | nan | nan | nan | Cerrado | 0.6 |
| a1b5c034-c077-3b85-ac87-8751fc85a06e | -4.27301 | -48.19156 | 2026-08-07 04:08:00 | NOAA-21 | RONDON DO PARÁ | PARÁ | Brasil | 1506187 | 15 | 33 | nan | nan | nan | Amazônia | 5.0 |
| 64a84275-74d7-3e1b-9ae0-5d2468c6d6db | -5.82553 | -44.14087 | 2026-08-07 04:08:00 | NOAA-21 | JATOBÁ | MARANHÃO | Brasil | 2105450 | 21 | 33 | nan | nan | nan | Cerrado | 1.0 |
| e15af2b0-778e-3eb3-8f9d-a6e8c13df7f0 | -4.91261 | -49.23607 | 2026-08-07 04:08:00 | NOAA-21 | NOVA IPIXUNA | PARÁ | Brasil | 1504976 | 15 | 33 | nan | nan | nan | Amazônia | 3.6 |
| 2b0f80ff-1911-3cef-a033-8a8dc5c35eaa | -8.33547 | -46.39665 | 2026-08-07 04:08:00 | NOAA-21 | BALSAS | MARANHÃO | Brasil | 2101400 | 21 | 33 | nan | nan | nan | Cerrado | 1.1 |
| 9a55493d-79a2-3595-844b-60e998800ac0 | -2.6956 | -47.35912 | 2026-08-07 04:08:00 | NOAA-21 | NOVA ESPERANÇA DO PIRIÁ | PARÁ | Brasil | 1504950 | 15 | 33 | nan | nan | nan | Amazônia | 1.6 |
| 4bb4f7ee-7aed-3856-b561-35e14d30bf92 | -6.86554 | -46.00772 | 2026-08-07 04:08:00 | NOAA-21 | FORTALEZA DOS NOGUEIRAS | MARANHÃO | Brasil | 2104107 | 21 | 33 | nan | nan | nan | Cerrado | 1.2 |
| a6d6bb39-a444-398a-9d8c-da7fcc0f28c7 | -8.34013 | -46.39256 | 2026-08-07 04:08:00 | NOAA-21 | BALSAS | MARANHÃO | Brasil | 2101400 | 21 | 33 | nan | nan | nan | Cerrado | 2.4 |
| dc6ae15e-e578-30a6-bcae-bd5c5b2be36b | -8.34399 | -46.39316 | 2026-08-07 04:08:00 | NOAA-21 | BALSAS | MARANHÃO | Brasil | 2101400 | 21 | 33 | nan | nan | nan | Cerrado | 2.4 |
| b799b6c4-6183-3ea6-826a-a52f5846daf5 | -6.92153 | -41.94997 | 2026-08-07 04:08:00 | NOAA-21 | SÃO JOÃO DA VARJOTA | PIAUÍ | Brasil | 2209955 | 22 | 33 | nan | nan | nan | Caatinga | 2.2 |
| 69f1293f-1d6b-3b53-95b1-84e1fd6f472c | -6.34855 | -35.16064 | 2026-08-07 04:08:00 | NOAA-21 | CANGUARETAMA | RIO GRANDE DO NORTE | Brasil | 2402204 | 24 | 33 | nan | nan | nan | Mata Atlântica | 2.2 |
| 1489fc16-747d-3ab0-9e5a-99469665af5c | -6.47928 | -42.23174 | 2026-08-07 04:08:00 | NOAA-21 | VÁRZEA GRANDE | PIAUÍ | Brasil | 2211407 | 22 | 33 | nan | nan | nan | Caatinga | 3.1 |
| bfef0e78-4589-3eea-b0f9-dc412de201e9 | -3.96111 | -43.10901 | 2026-08-07 04:08:00 | NOAA-21 | BURITI | MARANHÃO | Brasil | 2102200 | 21 | 33 | nan | nan | nan | Cerrado | 4.5 |
| 54b8bfb8-072e-3cb1-a9ba-b2c9e4a79d02 | -7.99197 | -47.27662 | 2026-08-07 04:08:00 | NOAA-21 | GOIATINS | TOCANTINS | Brasil | 1709005 | 17 | 33 | nan | nan | nan | Cerrado | 1.3 |
| 73858723-4a80-3b88-8271-6b7aed017d5f | -6.92095 | -41.93213 | 2026-08-07 04:08:00 | NOAA-21 | SÃO JOÃO DA VARJOTA | PIAUÍ | Brasil | 2209955 | 22 | 33 | nan | nan | nan | Caatinga | 1.2 |
| dc2e91d7-4995-3ad7-a448-80e39978c01f | -2.79132 | -49.52817 | 2026-08-07 04:08:00 | NOAA-21 | BAIÃO | PARÁ | Brasil | 1501204 | 15 | 33 | nan | nan | nan | Amazônia | 1.1 |
| 0d2ce37d-47c9-35e0-b0e0-9df1ced5c209 | -4.91613 | -49.23478 | 2026-08-07 04:08:00 | NOAA-21 | NOVA IPIXUNA | PARÁ | Brasil | 1504976 | 15 | 33 | nan | nan | nan | Amazônia | 3.6 |
| 36560eb1-7f83-325e-8ce9-c91970ec292c | -4.91753 | -49.23691 | 2026-08-07 04:08:00 | NOAA-21 | NOVA IPIXUNA | PARÁ | Brasil | 1504976 | 15 | 33 | nan | nan | nan | Amazônia | 1.9 |
| 6e749316-9d90-3cb3-96cd-bb877e9c9d33 | -8.33932 | -46.39729 | 2026-08-07 04:08:00 | NOAA-21 | BALSAS | MARANHÃO | Brasil | 2101400 | 21 | 33 | nan | nan | nan | Cerrado | 2.8 |
| 064b4a64-baa9-3074-b488-25fad0fa5748 | -6.91677 | -42.4127 | 2026-08-07 04:08:00 | NOAA-21 | OEIRAS | PIAUÍ | Brasil | 2207009 | 22 | 33 | nan | nan | nan | Caatinga | 2.0 |
| 86fe7c4b-6493-3b61-b448-001603f8ec7b | -5.80037 | -43.6407 | 2026-08-07 04:08:00 | NOAA-21 | LAGOA DO MATO | MARANHÃO | Brasil | 2105922 | 21 | 33 | nan | nan | nan | Cerrado | 1.4 |
| 350642c2-4ba8-3eda-b7ee-91372c97e634 | -7.21172 | -42.95812 | 2026-08-07 04:08:00 | NOAA-21 | FLORIANO | PIAUÍ | Brasil | 2203909 | 22 | 33 | nan | nan | nan | Caatinga | 1.3 |
| 685e3e49-90bf-3bf4-8767-a755eaa76b36 | -4.8482 | -45.21775 | 2026-08-07 04:08:00 | NOAA-21 | LAGO DA PEDRA | MARANHÃO | Brasil | 2105708 | 21 | 33 | nan | nan | nan | Cerrado | 4.9 |
| 69d04f13-c1ff-3a66-91f9-242231169cfc | -5.37146 | -49.17447 | 2026-08-07 04:08:00 | NOAA-21 | MARABÁ | PARÁ | Brasil | 1504208 | 15 | 33 | nan | nan | nan | Amazônia | 2.5 |
| fe362c23-cd72-3fbd-aa00-4eb2e7f1d5d6 | -4.41163 | -42.14175 | 2026-08-07 04:08:00 | NOAA-21 | BOA HORA | PIAUÍ | Brasil | 2201770 | 22 | 33 | nan | nan | nan | Caatinga | 2.8 |
| 1903ca27-3a41-3ba8-88e1-8562f4ace583 | -2.4189 | -48.63299 | 2026-08-07 04:08:00 | NOAA-21 | ACARÁ | PARÁ | Brasil | 1500206 | 15 | 33 | nan | nan | nan | Amazônia | 1.3 |
| ebf75134-a475-33fa-a834-e39220c04862 | -6.07245 | -49.49069 | 2026-08-07 04:08:00 | NOAA-21 | CURIONÓPOLIS | PARÁ | Brasil | 1502772 | 15 | 33 | nan | nan | nan | Amazônia | 5.8 |
| 3f6fc538-11b4-387e-9d70-82f5e7f0395f | -6.55747 | -55.1711 | 2026-08-07 04:08:00 | NOAA-21 | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 3.9 |
| f85de60c-2497-3885-b0fe-64076d05ab7a | -7.08997 | -46.54359 | 2026-08-07 04:08:00 | NOAA-21 | FEIRA NOVA DO MARANHÃO | MARANHÃO | Brasil | 2104073 | 21 | 33 | nan | nan | nan | Cerrado | 2.2 |
| a383a9f7-fca3-3695-a625-396963a064a1 | -6.86304 | -46.00983 | 2026-08-07 04:08:00 | NOAA-21 | FORTALEZA DOS NOGUEIRAS | MARANHÃO | Brasil | 2104107 | 21 | 33 | nan | nan | nan | Cerrado | 6.3 |
| 282ba9f3-d68b-3602-b8fb-0c71a01c5f15 | -8.07953 | -45.58108 | 2026-08-07 04:08:00 | NOAA-21 | TASSO FRAGOSO | MARANHÃO | Brasil | 2112001 | 21 | 33 | nan | nan | nan | Cerrado | 4.4 |
| 0e94b265-609d-3457-a719-36b616722661 | -4.84367 | -45.22173 | 2026-08-07 04:08:00 | NOAA-21 | LAGO DA PEDRA | MARANHÃO | Brasil | 2105708 | 21 | 33 | nan | nan | nan | Cerrado | 2.3 |
| c4e72309-7d11-3521-b1cb-577975f5295a | -8.53698 | -49.55694 | 2026-08-07 04:08:00 | NOAA-21 | CONCEIÇÃO DO ARAGUAIA | PARÁ | Brasil | 1502707 | 15 | 33 | nan | nan | nan | Amazônia | 1.5 |
| bfcd399e-22ec-33ad-b7a3-03714816b057 | -8.3372 | -46.39875 | 2026-08-07 04:08:00 | NOAA-21 | BALSAS | MARANHÃO | Brasil | 2101400 | 21 | 33 | nan | nan | nan | Cerrado | 2.1 |
| ff10bbe3-1bc5-36fd-9f9c-2115215795ad | -6.47873 | -42.23522 | 2026-08-07 04:08:00 | NOAA-21 | VÁRZEA GRANDE | PIAUÍ | Brasil | 2211407 | 22 | 33 | nan | nan | nan | Caatinga | 6.7 |
| b1dc602b-6df4-3084-a3ed-a1b58f3df66e | -9.80294 | -46.70649 | 2026-08-07 04:08:00 | NOAA-21 | LIZARDA | TOCANTINS | Brasil | 1712405 | 17 | 33 | nan | nan | nan | Cerrado | 1.3 |
| 398f8545-19b6-33a7-8eac-c358d668cb64 | -6.95123 | -41.93336 | 2026-08-07 04:08:00 | NOAA-21 | SÃO JOÃO DA VARJOTA | PIAUÍ | Brasil | 2209955 | 22 | 33 | nan | nan | nan | Caatinga | 2.2 |
| 58b2ac86-56aa-3052-a622-abd38d57a4eb | -7.09309 | -46.54938 | 2026-08-07 04:08:00 | NOAA-21 | FEIRA NOVA DO MARANHÃO | MARANHÃO | Brasil | 2104073 | 21 | 33 | nan | nan | nan | Cerrado | 3.4 |
| b4bf744a-2aff-312c-9756-5eba7326192c | -4.84442 | -45.21716 | 2026-08-07 04:08:00 | NOAA-21 | LAGO DA PEDRA | MARANHÃO | Brasil | 2105708 | 21 | 33 | nan | nan | nan | Cerrado | 4.9 |
| d5728e1d-38d8-3e53-bd32-1eee440080a1 | -4.45982 | -47.91657 | 2026-08-07 04:08:00 | NOAA-21 | DOM ELISEU | PARÁ | Brasil | 1502939 | 15 | 33 | nan | nan | nan | Amazônia | 23.2 |
| 18f99cf0-3105-3105-bca5-bf233df9e66d | -9.39761 | -37.80431 | 2026-08-07 04:08:00 | NOAA-21 | OLHO D'ÁGUA DO CASADO | ALAGOAS | Brasil | 2705804 | 27 | 33 | nan | nan | nan | Caatinga | 1.6 |
| 322739b9-2f1c-3edf-be69-b12e13938fd9 | -10.22227 | -45.78982 | 2026-08-07 04:08:00 | NOAA-21 | BARREIRAS DO PIAUÍ | PIAUÍ | Brasil | 2201309 | 22 | 33 | nan | nan | nan | Cerrado | 1.8 |
| 249e7580-5a55-35d3-b369-4fa6483e812f | -7.18335 | -42.34027 | 2026-08-07 04:08:00 | NOAA-21 | OEIRAS | PIAUÍ | Brasil | 2207009 | 22 | 33 | nan | nan | nan | Caatinga | 1.4 |
| eb413640-92f1-3c1d-ba54-5564572430ce | -6.99101 | -42.9118 | 2026-08-07 04:08:00 | NOAA-21 | FLORIANO | PIAUÍ | Brasil | 2203909 | 22 | 33 | nan | nan | nan | Caatinga | 4.4 |
| d90dd78a-6384-336d-911a-2529565c2068 | -3.17979 | -49.52994 | 2026-08-07 04:08:00 | NOAA-21 | BAIÃO | PARÁ | Brasil | 1501204 | 15 | 33 | nan | nan | nan | Amazônia | 0.8 |
| 5e0316b9-c190-3ca0-bbbf-6d41d605bab2 | -6.27584 | -44.56417 | 2026-08-07 04:08:00 | NOAA-21 | MIRADOR | MARANHÃO | Brasil | 2106706 | 21 | 33 | nan | nan | nan | Cerrado | 3.3 |
| 0f838389-8ffc-37de-b12e-fee0af44a736 | -3.5953 | -49.07408 | 2026-08-07 04:08:00 | NOAA-21 | GOIANÉSIA DO PARÁ | PARÁ | Brasil | 1503093 | 15 | 33 | nan | nan | nan | Amazônia | 1.4 |
| bcd7b49c-741f-3840-932b-14ad1637bfd0 | -5.65441 | -44.83122 | 2026-08-07 04:08:00 | NOAA-21 | TUNTUM | MARANHÃO | Brasil | 2112308 | 21 | 33 | nan | nan | nan | Cerrado | 0.6 |
| 39136a12-e9d3-3f2a-a9be-48cb29b0e40c | -6.05545 | -43.86417 | 2026-08-07 04:08:00 | NOAA-21 | PASSAGEM FRANCA | MARANHÃO | Brasil | 2107902 | 21 | 33 | nan | nan | nan | Cerrado | 1.3 |
| 45f5bad1-0bd3-354c-ae83-ea83e7dcf0cd | -8.54171 | -49.55778 | 2026-08-07 04:08:00 | NOAA-21 | CONCEIÇÃO DO ARAGUAIA | PARÁ | Brasil | 1502707 | 15 | 33 | nan | nan | nan | Amazônia | 1.5 |
| e10017f9-26c0-3886-9f8f-6efd9c01a23f | -6.13493 | -47.17813 | 2026-08-07 04:08:00 | NOAA-21 | CAMPESTRE DO MARANHÃO | MARANHÃO | Brasil | 2102556 | 21 | 33 | nan | nan | nan | Cerrado | 2.9 |
| 2e00ada6-d675-3a8f-b0c4-7c64afa23e70 | -6.85995 | -46.00453 | 2026-08-07 04:08:00 | NOAA-21 | FORTALEZA DOS NOGUEIRAS | MARANHÃO | Brasil | 2104107 | 21 | 33 | nan | nan | nan | Cerrado | 6.8 |
| 0bf715cc-e5c9-3bda-bdca-1bf373a03213 | -6.91492 | -41.94894 | 2026-08-07 04:08:00 | NOAA-21 | SÃO JOÃO DA VARJOTA | PIAUÍ | Brasil | 2209955 | 22 | 33 | nan | nan | nan | Caatinga | 1.8 |
| 0f6c17a8-1359-32de-bece-5d9aa8b5c8b5 | -2.69489 | -47.36355 | 2026-08-07 04:08:00 | NOAA-21 | NOVA ESPERANÇA DO PIRIÁ | PARÁ | Brasil | 1504950 | 15 | 33 | nan | nan | nan | Amazônia | 2.5 |
| 1d4acc70-b9a4-31b2-af1f-002c9a4262cb | -6.54018 | -55.14779 | 2026-08-07 04:08:00 | NOAA-21 | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 5.5 |
| 7efa77ba-0dc7-3aa0-b7ab-4eb9557c88e7 | -6.13843 | -47.17812 | 2026-08-07 04:08:00 | NOAA-21 | CAMPESTRE DO MARANHÃO | MARANHÃO | Brasil | 2102556 | 21 | 33 | nan | nan | nan | Cerrado | 30.0 |
| 42ba31d3-1f4d-3c87-86fa-6b5be1d992da | -6.86379 | -46.00516 | 2026-08-07 04:08:00 | NOAA-21 | FORTALEZA DOS NOGUEIRAS | MARANHÃO | Brasil | 2104107 | 21 | 33 | nan | nan | nan | Cerrado | 6.8 |
| c6fd6e10-8222-3170-81b6-20e62b850d30 | -6.98766 | -42.91127 | 2026-08-07 04:08:00 | NOAA-21 | FLORIANO | PIAUÍ | Brasil | 2203909 | 22 | 33 | nan | nan | nan | Caatinga | 4.4 |
| 18229026-eaad-3e07-b0d8-7584bcb4f214 | -10.5676 | -42.38173 | 2026-08-07 04:08:00 | NOAA-21 | XIQUE-XIQUE | BAHIA | Brasil | 2933604 | 29 | 33 | nan | nan | nan | Caatinga | 0.5 |
| 5398c4f0-8152-303b-a41c-c0687751c4a7 | -6.92972 | -41.91934 | 2026-08-07 04:08:00 | NOAA-21 | SÃO JOÃO DA VARJOTA | PIAUÍ | Brasil | 2209955 | 22 | 33 | nan | nan | nan | Caatinga | 0.7 |
| 127bff44-25e1-3999-858c-ba9c911a8139 | -4.8065 | -40.04385 | 2026-08-07 04:08:00 | NOAA-21 | MONSENHOR TABOSA | CEARÁ | Brasil | 2308609 | 23 | 33 | nan | nan | nan | Caatinga | 0.7 |
| 6da5c769-dabd-355d-8fc8-c979155f471f | -7.28005 | -39.25233 | 2026-08-07 04:08:00 | NOAA-21 | BARBALHA | CEARÁ | Brasil | 2301901 | 23 | 33 | nan | nan | nan | Caatinga | 0.7 |
| ae2ca4ed-8781-3e07-9c1c-fbd79691bb2e | -8.55793 | -45.36604 | 2026-08-07 04:08:00 | NOAA-21 | BAIXA GRANDE DO RIBEIRO | PIAUÍ | Brasil | 2201150 | 22 | 33 | nan | nan | nan | Cerrado | 1.9 |
| 66c3a41b-fd8e-328b-8222-4a2f808c857e | -5.4257 | -43.25919 | 2026-08-07 04:08:00 | NOAA-21 | MATÕES | MARANHÃO | Brasil | 2106607 | 21 | 33 | nan | nan | nan | Cerrado | 1.2 |
| a9284555-9ebb-34a5-adc6-352a2556bd36 | -3.17462 | -49.5291 | 2026-08-07 04:08:00 | NOAA-21 | BAIÃO | PARÁ | Brasil | 1501204 | 15 | 33 | nan | nan | nan | Amazônia | 0.4 |
| c3f75317-f250-331f-bd0a-a02f985edaf4 | -2.47947 | -49.32716 | 2026-08-07 04:08:00 | NOAA-21 | MOCAJUBA | PARÁ | Brasil | 1504604 | 15 | 33 | nan | nan | nan | Amazônia | 2.3 |
| 4bb4506e-e221-3bcf-ad3f-ca4b35b2ffdc | -7.17726 | -42.33576 | 2026-08-07 04:08:00 | NOAA-21 | OEIRAS | PIAUÍ | Brasil | 2207009 | 22 | 33 | nan | nan | nan | Caatinga | 0.4 |
| 8d4d03eb-a8b9-3f6f-a672-ec2c880c4114 | -6.89876 | -42.44144 | 2026-08-07 04:08:00 | NOAA-21 | CAJAZEIRAS DO PIAUÍ | PIAUÍ | Brasil | 2202075 | 22 | 33 | nan | nan | nan | Caatinga | 4.5 |
| b44dcdbe-7421-3a2f-84b8-71205ef1fa5d | -6.71826 | -46.18344 | 2026-08-07 04:08:00 | NOAA-21 | FORMOSA DA SERRA NEGRA | MARANHÃO | Brasil | 2104099 | 21 | 33 | nan | nan | nan | Cerrado | 2.0 |
| 5d992c8f-a4c8-3bab-8112-68c901a5fa6f | -9.64058 | -47.80806 | 2026-08-07 04:08:00 | NOAA-21 | RIO SONO | TOCANTINS | Brasil | 1718758 | 17 | 33 | nan | nan | nan | Cerrado | 1.5 |
| 85f478da-16c8-3a88-9ce1-893afd4e7dc4 | -6.07006 | -49.48769 | 2026-08-07 04:08:00 | NOAA-21 | CURIONÓPOLIS | PARÁ | Brasil | 1502772 | 15 | 33 | nan | nan | nan | Amazônia | 7.4 |
| 4df54b23-7433-34b8-b6fb-2257cce48ef6 | -6.13779 | -47.18204 | 2026-08-07 04:08:00 | NOAA-21 | CAMPESTRE DO MARANHÃO | MARANHÃO | Brasil | 2102556 | 21 | 33 | nan | nan | nan | Cerrado | 30.0 |
| fcbd6494-706d-3e9e-a9ac-79baec8db52d | -5.09307 | -42.85119 | 2026-08-07 04:08:00 | NOAA-21 | TIMON | MARANHÃO | Brasil | 2112209 | 21 | 33 | nan | nan | nan | Cerrado | 1.9 |
| 8feccce3-48a9-3b58-af0e-c7f81c354c3e | -6.92869 | -41.94754 | 2026-08-07 04:08:00 | NOAA-21 | SÃO JOÃO DA VARJOTA | PIAUÍ | Brasil | 2209955 | 22 | 33 | nan | nan | nan | Caatinga | 1.3 |
| 77debb2b-6e9b-37fa-babe-496e42b6f168 | -8.6598 | -45.859 | 2026-08-07 04:08:00 | NOAA-21 | TASSO FRAGOSO | MARANHÃO | Brasil | 2112001 | 21 | 33 | nan | nan | nan | Cerrado | 1.3 |
| ba3cc147-1b07-3bde-ad03-619d9c9067f0 | -8.65755 | -54.95092 | 2026-08-07 04:08:00 | NOAA-21 | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 1.7 |
| 2a2e91d7-cbd0-3331-8d74-e68db13f113b | -6.86073 | -45.9997 | 2026-08-07 04:08:00 | NOAA-21 | FORTALEZA DOS NOGUEIRAS | MARANHÃO | Brasil | 2104107 | 21 | 33 | nan | nan | nan | Cerrado | 6.8 |
| 44207c5c-74ec-3161-97a5-e8b0b6556a37 | -3.40204 | -49.7812 | 2026-08-07 04:08:00 | NOAA-21 | BAIÃO | PARÁ | Brasil | 1501204 | 15 | 33 | nan | nan | nan | Amazônia | 3.2 |
| 3e8b2632-264c-3cab-91ad-de60d7d68022 | -6.9068 | -42.43266 | 2026-08-07 04:08:00 | NOAA-21 | OEIRAS | PIAUÍ | Brasil | 2207009 | 22 | 33 | nan | nan | nan | Caatinga | 1.8 |
| 652fee6d-95e4-3080-aa63-7d452d3bfde8 | -5.42595 | -43.43507 | 2026-08-07 04:08:00 | NOAA-21 | MATÕES | MARANHÃO | Brasil | 2106607 | 21 | 33 | nan | nan | nan | Cerrado | 2.6 |
| f396ec48-d1e3-324c-bedf-bf0e93342245 | -6.13426 | -47.18206 | 2026-08-07 04:08:00 | NOAA-21 | CAMPESTRE DO MARANHÃO | MARANHÃO | Brasil | 2102556 | 21 | 33 | nan | nan | nan | Cerrado | 2.9 |
| 7e122c79-4ffb-3c22-9554-f212e53e461d | -6.50878 | -42.0869 | 2026-08-07 04:08:00 | NOAA-21 | BARRA D'ALCÂNTARA | PIAUÍ | Brasil | 2201176 | 22 | 33 | nan | nan | nan | Caatinga | 0.8 |
| 40ec1599-9c72-3712-88ef-93dace4f9765 | -6.54929 | -55.1764 | 2026-08-07 04:08:00 | NOAA-21 | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 4.7 |
| 556b6322-6d2f-3bca-bf86-456102c17c51 | -7.08913 | -46.54873 | 2026-08-07 04:08:00 | NOAA-21 | FEIRA NOVA DO MARANHÃO | MARANHÃO | Brasil | 2104073 | 21 | 33 | nan | nan | nan | Cerrado | 3.4 |
| bcae77ce-7d23-3748-ba9e-98e8ea10730f | -9.80434 | -46.70924 | 2026-08-07 04:08:00 | NOAA-21 | LIZARDA | TOCANTINS | Brasil | 1712405 | 17 | 33 | nan | nan | nan | Cerrado | 1.8 |
| 2a0baa70-91fa-363c-b91b-65e2950a69fa | -6.47542 | -42.2347 | 2026-08-07 04:08:00 | NOAA-21 | FRANCINÓPOLIS | PIAUÍ | Brasil | 2204006 | 22 | 33 | nan | nan | nan | Caatinga | 6.7 |
| e93d2610-a4de-3dfc-b961-30de66e53069 | -8.6964 | -44.27887 | 2026-08-07 04:08:00 | NOAA-21 | PALMEIRA DO PIAUÍ | PIAUÍ | Brasil | 2207405 | 22 | 33 | nan | nan | nan | Cerrado | 0.6 |


[Clique aqui para ver as próximas entradas](README8.md)
