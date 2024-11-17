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

## Dados Diários - Página 1

| ID | Latitude | Longitude | Data/Hora GMT | Satélite | Município | Estado | País | Município ID | Estado ID | País ID | Dias sem Chuva | Precipitação | Risco de Fogo | Bioma | FRP |
|----|----------|-----------|---------------|----------|-----------|--------|------|--------------|-----------|---------|----------------|--------------|----------------|-------|-----|
| ee7a81d1-e122-3948-a857-a92bc723c208 | -2.8801 | -46.7079 | 2024-11-17 00:00:00 | GOES-16 | PARAGOMINAS | PARÁ | Brasil | 1505502 | 15 | 33 | nan | nan | nan | Amazônia | 89.9 |
| d46f319a-2525-3580-920a-e13035456423 | -4.5429 | -48.0151 | 2024-11-17 00:00:00 | GOES-16 | RONDON DO PARÁ | PARÁ | Brasil | 1506187 | 15 | 33 | nan | nan | nan | Amazônia | 38.6 |
| 300c7e96-56e9-3ccb-accd-347bfe76fcf1 | -3.5124 | -50.2553 | 2024-11-17 00:00:00 | GOES-16 | PACAJÁ | PARÁ | Brasil | 1505486 | 15 | 33 | nan | nan | nan | Amazônia | 99.6 |
| 9e4e1364-6d87-37e5-a643-078d864b01cc | -4.656 | -44.9966 | 2024-11-17 00:00:00 | GOES-16 | LAGO DOS RODRIGUES | MARANHÃO | Brasil | 2105948 | 21 | 33 | nan | nan | nan | Cerrado | 56.6 |
| 5bca5e05-0ce0-35a7-a2ca-33897f7f42dd | -2.678 | -46.2059 | 2024-11-17 00:00:00 | GOES-16 | CENTRO NOVO DO MARANHÃO | MARANHÃO | Brasil | 2103174 | 21 | 33 | nan | nan | nan | Amazônia | 119.7 |
| de9e1c15-92ed-3a0e-ae28-82351e1fcbd8 | -3.793 | -46.052 | 2024-11-17 00:00:00 | GOES-16 | ALTO ALEGRE DO PINDARÉ | MARANHÃO | Brasil | 2100477 | 21 | 33 | nan | nan | nan | Amazônia | 67.6 |
| 0846ab10-258b-3dc5-a3a4-8c3030964578 | -1.9166 | -46.5804 | 2024-11-17 00:00:00 | GOES-16 | CACHOEIRA DO PIRIÁ | PARÁ | Brasil | 1501956 | 15 | 33 | nan | nan | nan | Amazônia | 69.7 |
| 1d7282d5-cb5f-3ee9-92d1-5045f42e9852 | -2.3399 | -47.4688 | 2024-11-17 00:00:00 | GOES-16 | AURORA DO PARÁ | PARÁ | Brasil | 1500958 | 15 | 33 | nan | nan | nan | Amazônia | 51.1 |
| 1f265c29-39c9-39ca-958f-606ecfa90390 | -2.6137 | -48.5639 | 2024-11-17 00:00:00 | GOES-16 | TAILÂNDIA | PARÁ | Brasil | 1507953 | 15 | 33 | nan | nan | nan | Amazônia | 45.3 |
| d89a6581-1f20-317b-a512-09201e162ffe | -5.2725 | -44.913 | 2024-11-17 00:00:00 | GOES-16 | BARRA DO CORDA | MARANHÃO | Brasil | 2101608 | 21 | 33 | nan | nan | nan | Cerrado | 62.0 |
| 09d25912-e041-331c-a732-253b3e3bd620 | -2.5139 | -45.4522 | 2024-11-17 00:00:00 | GOES-16 | PRESIDENTE SARNEY | MARANHÃO | Brasil | 2109270 | 21 | 33 | nan | nan | nan | Amazônia | 52.3 |
| 48458ecc-83d5-36db-9c12-4208dd62324d | -3.5309 | -50.2547 | 2024-11-17 00:00:00 | GOES-16 | PACAJÁ | PARÁ | Brasil | 1505486 | 15 | 33 | nan | nan | nan | Amazônia | 229.0 |
| 2486a2cd-e2d5-3c3e-bd35-c4a3a5541900 | -2.8615 | -46.7086 | 2024-11-17 00:00:00 | GOES-16 | PARAGOMINAS | PARÁ | Brasil | 1505502 | 15 | 33 | nan | nan | nan | Amazônia | 111.3 |
| a3563038-d911-37a1-839b-65d584ecc926 | -2.6173 | -47.5482 | 2024-11-17 00:00:00 | GOES-16 | IPIXUNA DO PARÁ | PARÁ | Brasil | 1503457 | 15 | 33 | nan | nan | nan | Amazônia | 60.2 |
| 3bf7018e-ade5-364e-bcb4-d29a1788d882 | -3.7931 | -46.0297 | 2024-11-17 00:00:00 | GOES-16 | ALTO ALEGRE DO PINDARÉ | MARANHÃO | Brasil | 2100477 | 21 | 33 | nan | nan | nan | Amazônia | 97.4 |
| 03e7acaf-be8d-3993-877f-5d6141cfc793 | -12.4004 | -57.5127 | 2024-11-17 00:00:00 | GOES-16 | NOVA MARINGÁ | MATO GROSSO | Brasil | 5108907 | 51 | 33 | nan | nan | nan | Amazônia | 67.6 |
| 6250f9f3-ba25-3826-8cc2-268c4bfbde46 | -2.6322 | -48.5634 | 2024-11-17 00:00:00 | GOES-16 | TAILÂNDIA | PARÁ | Brasil | 1507953 | 15 | 33 | nan | nan | nan | Amazônia | 124.9 |
| c095dc33-a4b8-30e8-893b-5c4e5cf1ea4b | -2.6322 | -48.542 | 2024-11-17 00:00:00 | GOES-16 | TAILÂNDIA | PARÁ | Brasil | 1507953 | 15 | 33 | nan | nan | nan | Amazônia | 43.3 |
| bebdbc40-5f7e-3504-abca-088ab89ad02c | -2.6325 | -54.1571 | 2024-11-17 00:00:00 | GOES-16 | PRAINHA | PARÁ | Brasil | 1506005 | 15 | 33 | nan | nan | nan | Amazônia | 59.0 |
| 27ee0af9-7129-3fb7-b1a4-6f51277555ca | -2.6595 | -46.2065 | 2024-11-17 00:00:00 | GOES-16 | CENTRO NOVO DO MARANHÃO | MARANHÃO | Brasil | 2103174 | 21 | 33 | nan | nan | nan | Amazônia | 114.1 |
| bedc573d-77c1-3668-85dc-c0a7e6e7b8fb | -2.5987 | -47.5705 | 2024-11-17 00:00:00 | GOES-16 | IPIXUNA DO PARÁ | PARÁ | Brasil | 1503457 | 15 | 33 | nan | nan | nan | Amazônia | 125.8 |
| fc3d67b5-fa28-3182-ab79-c678811859ab | -3.7744 | -46.0528 | 2024-11-17 00:00:00 | GOES-16 | ALTO ALEGRE DO PINDARÉ | MARANHÃO | Brasil | 2100477 | 21 | 33 | nan | nan | nan | Amazônia | 74.8 |
| 6c690069-ba90-3206-b4c0-8500d9ee1684 | -4.58 | -48.0132 | 2024-11-17 00:00:00 | GOES-16 | RONDON DO PARÁ | PARÁ | Brasil | 1506187 | 15 | 33 | nan | nan | nan | Amazônia | 42.5 |
| 3e186edb-73bf-3aa9-814e-84d20ea8d80b | -2.8614 | -46.7306 | 2024-11-17 00:00:00 | GOES-16 | PARAGOMINAS | PARÁ | Brasil | 1505502 | 15 | 33 | nan | nan | nan | Amazônia | 154.7 |
| 34c060c8-118c-3150-9824-08aecae7f052 | -3.5851 | -50.5255 | 2024-11-17 00:00:00 | GOES-16 | PACAJÁ | PARÁ | Brasil | 1505486 | 15 | 33 | nan | nan | nan | Amazônia | 78.2 |
| d9a0727e-604c-3aab-af54-b13272abf397 | -4.5614 | -48.0141 | 2024-11-17 00:00:00 | GOES-16 | RONDON DO PARÁ | PARÁ | Brasil | 1506187 | 15 | 33 | nan | nan | nan | Amazônia | 54.5 |
| 4c1b7504-6ebc-30f8-bc4e-d34df2819e74 | -1.8008 | -48.4328 | 2024-11-17 00:00:00 | GOES-16 | ACARÁ | PARÁ | Brasil | 1500206 | 15 | 33 | nan | nan | nan | Amazônia | 124.3 |
| 4ced2dae-9485-3fe8-9759-100421237262 | -3.531 | -50.2337 | 2024-11-17 00:00:00 | GOES-16 | PACAJÁ | PARÁ | Brasil | 1505486 | 15 | 33 | nan | nan | nan | Amazônia | 108.5 |
| e870f1cd-5e1f-305d-954e-dcfededa40de | -4.543 | -47.9934 | 2024-11-17 00:00:00 | GOES-16 | RONDON DO PARÁ | PARÁ | Brasil | 1506187 | 15 | 33 | nan | nan | nan | Amazônia | 44.7 |
| 373dfb5c-98e3-37df-b2c1-f4b7c835f8c0 | -4.5799 | -48.0349 | 2024-11-17 00:00:00 | GOES-16 | RONDON DO PARÁ | PARÁ | Brasil | 1506187 | 15 | 33 | nan | nan | nan | Amazônia | 37.8 |
| 06330073-328f-3f51-b9ea-a718f97aaa61 | -3.5494 | -50.254 | 2024-11-17 00:00:00 | GOES-16 | PACAJÁ | PARÁ | Brasil | 1505486 | 15 | 33 | nan | nan | nan | Amazônia | 93.1 |
| d1a6d8a6-522f-3288-92aa-e169aa97ad2f | -2.5802 | -47.571 | 2024-11-17 00:00:00 | GOES-16 | IPIXUNA DO PARÁ | PARÁ | Brasil | 1503457 | 15 | 33 | nan | nan | nan | Amazônia | 94.9 |
| 06f4fb13-e35c-3a77-a8e4-f85a8b200124 | -2.6231 | -46.0299 | 2024-11-17 00:00:00 | GOES-16 | MARANHÃOZINHO | MARANHÃO | Brasil | 2106375 | 21 | 33 | nan | nan | nan | Amazônia | 66.9 |
| 2e2a236f-bb0b-305c-a575-a4f07ee151ff | -2.88 | -46.73 | 2024-11-17 00:00:00 | GOES-16 | PARAGOMINAS | PARÁ | Brasil | 1505502 | 15 | 33 | nan | nan | nan | Amazônia | 129.8 |
| ede856ca-e025-3a82-8765-b439484b066c | -4.5616 | -47.9925 | 2024-11-17 00:00:00 | GOES-16 | RONDON DO PARÁ | PARÁ | Brasil | 1506187 | 15 | 33 | nan | nan | nan | Amazônia | 61.9 |
| 81daaab6-cc94-3d8d-a5e7-87b141156fb3 | -8.42 | -44.17 | 2024-11-17 00:00:00 | MSG-03 | ALVORADA DO GURGUÉIA | PIAUÍ | Brasil | 2200459 | 22 | 33 | nan | nan | nan | Cerrado | nan |
| 7bb287f8-7635-393a-ac56-884194e47147 | -2.6594 | -46.2287 | 2024-11-17 00:00:00 | GOES-16 | CENTRO NOVO DO MARANHÃO | MARANHÃO | Brasil | 2103174 | 21 | 33 | nan | nan | nan | Amazônia | 59.6 |
| 24c1a7a5-be26-352e-9773-2a78aa7097e6 | -3.5678 | -50.2534 | 2024-11-17 00:00:00 | GOES-16 | PACAJÁ | PARÁ | Brasil | 1505486 | 15 | 33 | nan | nan | nan | Amazônia | 83.8 |
| 5ae8b307-9095-31b8-abc6-f800d24ba3c1 | -3.7745 | -46.0305 | 2024-11-17 00:00:00 | GOES-16 | ALTO ALEGRE DO PINDARÉ | MARANHÃO | Brasil | 2100477 | 21 | 33 | nan | nan | nan | Amazônia | 103.3 |
| a5d6a4f5-d90b-371b-8dac-f4598337577c | -1.8007 | -48.4543 | 2024-11-17 00:00:00 | GOES-16 | MOJU | PARÁ | Brasil | 1504703 | 15 | 33 | nan | nan | nan | Amazônia | 109.2 |
| a3cfcc4f-edda-3563-9724-d3cdc7479459 | -1.7823 | -48.4332 | 2024-11-17 00:00:00 | GOES-16 | ACARÁ | PARÁ | Brasil | 1500206 | 15 | 33 | nan | nan | nan | Amazônia | 57.4 |
| f28e1069-8f79-31e2-aa67-a7edae3dea31 | -3.4784 | -53.9955 | 2024-11-17 00:00:00 | GOES-16 | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | 50.4 |
| 01fd5909-c20a-390e-b4f5-cf3eedb11654 | -4.2049 | -48.6995 | 2024-11-17 00:00:00 | GOES-16 | RONDON DO PARÁ | PARÁ | Brasil | 1506187 | 15 | 33 | nan | nan | nan | Amazônia | 54.9 |
| 18ca7a3c-827b-3eb8-b806-9a86357d986b | 0.6159 | -51.7881 | 2024-11-17 00:00:00 | GOES-16 | PORTO GRANDE | AMAPÁ | Brasil | 1600535 | 16 | 33 | nan | nan | nan | Amazônia | 42.2 |
| be338df7-fd5c-3ec8-b3d8-0c1a71b80667 | -2.5988 | -47.5488 | 2024-11-17 00:00:00 | GOES-16 | IPIXUNA DO PARÁ | PARÁ | Brasil | 1503457 | 15 | 33 | nan | nan | nan | Amazônia | 125.2 |
| c9983d90-4ba1-3965-a342-4fcb6d472fcd | -2.6141 | -54.1575 | 2024-11-17 00:00:00 | GOES-16 | PRAINHA | PARÁ | Brasil | 1506005 | 15 | 33 | nan | nan | nan | Amazônia | 73.6 |
| bdf75a34-ea03-3b70-8c71-f35bd700eadf | 0.6159 | -51.7676 | 2024-11-17 00:00:00 | GOES-16 | PORTO GRANDE | AMAPÁ | Brasil | 1600535 | 16 | 33 | nan | nan | nan | Amazônia | 62.3 |
| 665a627b-7dd3-35e0-81c6-30017a25d282 | -8.45 | -44.22 | 2024-11-17 00:00:00 | MSG-03 | ALVORADA DO GURGUÉIA | PIAUÍ | Brasil | 2200459 | 22 | 33 | nan | nan | nan | Cerrado | nan |
| fe26f983-ba07-30e8-83f9-05013066dc26 | -8.42 | -44.21 | 2024-11-17 00:00:00 | MSG-03 | ALVORADA DO GURGUÉIA | PIAUÍ | Brasil | 2200459 | 22 | 33 | nan | nan | nan | Cerrado | nan |
| a3c38f33-da85-33e8-bbf6-46d10e8499ce | -1.79 | -48.44 | 2024-11-17 00:00:00 | MSG-03 | ACARÁ | PARÁ | Brasil | 1500206 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| 75bd3fac-1c64-3fc7-9414-166c3cb3ff94 | -8.45 | -44.17 | 2024-11-17 00:00:00 | MSG-03 | ALVORADA DO GURGUÉIA | PIAUÍ | Brasil | 2200459 | 22 | 33 | nan | nan | nan | Cerrado | nan |
| 648b64d5-f5d6-3c84-998d-64e7f11b16d8 | -2.5987 | -47.5705 | 2024-11-17 00:10:00 | GOES-16 | IPIXUNA DO PARÁ | PARÁ | Brasil | 1503457 | 15 | 33 | nan | nan | nan | Amazônia | 55.1 |
| 8801907f-6786-3bcf-a133-9aa5e4c5b3f1 | -3.5851 | -50.5255 | 2024-11-17 00:10:00 | GOES-16 | PACAJÁ | PARÁ | Brasil | 1505486 | 15 | 33 | nan | nan | nan | Amazônia | 75.3 |
| e3b1f988-865e-31fb-bc8c-882ac29173ef | -8.4525 | -44.1999 | 2024-11-17 00:10:00 | GOES-16 | ALVORADA DO GURGUÉIA | PIAUÍ | Brasil | 2200459 | 22 | 33 | nan | nan | nan | Cerrado | 391.2 |
| 8c2a5cdc-9131-3795-b222-a0453b3998e2 | -2.6322 | -48.5634 | 2024-11-17 00:10:00 | GOES-16 | TAILÂNDIA | PARÁ | Brasil | 1507953 | 15 | 33 | nan | nan | nan | Amazônia | 125.0 |
| a56bd228-fd6b-3826-b95a-eafcd0ca8125 | -1.9167 | -46.5584 | 2024-11-17 00:10:00 | GOES-16 | CACHOEIRA DO PIRIÁ | PARÁ | Brasil | 1501956 | 15 | 33 | nan | nan | nan | Amazônia | 57.1 |
| 9fd9fd26-b382-3c10-a444-ceab82b0dd4e | -5.2725 | -44.913 | 2024-11-17 00:10:00 | GOES-16 | BARRA DO CORDA | MARANHÃO | Brasil | 2101608 | 21 | 33 | nan | nan | nan | Cerrado | 59.9 |
| fe228726-a800-314e-a721-7c8169ec96f9 | -2.88 | -46.73 | 2024-11-17 00:10:00 | GOES-16 | PARAGOMINAS | PARÁ | Brasil | 1505502 | 15 | 33 | nan | nan | nan | Amazônia | 76.8 |
| 227c8dd6-2328-3a3a-93e5-36d4930ead0d | -8.4336 | -44.2019 | 2024-11-17 00:10:00 | GOES-16 | ALVORADA DO GURGUÉIA | PIAUÍ | Brasil | 2200459 | 22 | 33 | nan | nan | nan | Cerrado | 269.1 |
| 3abf13ae-e1bc-3ba2-a841-ad3cab351e7b | -9.4008 | -40.3225 | 2024-11-17 00:10:00 | GOES-16 | JUAZEIRO | BAHIA | Brasil | 2918407 | 29 | 33 | nan | nan | nan | Caatinga | 90.2 |
| df975f9c-ad17-3ce9-a9aa-d1e6708ef7dd | -8.4333 | -44.2251 | 2024-11-17 00:10:00 | GOES-16 | ALVORADA DO GURGUÉIA | PIAUÍ | Brasil | 2200459 | 22 | 33 | nan | nan | nan | Cerrado | 81.3 |
| ce63f8c1-af94-3829-b1e5-7864c6c57a2a | -2.8615 | -46.7086 | 2024-11-17 00:10:00 | GOES-16 | PARAGOMINAS | PARÁ | Brasil | 1505502 | 15 | 33 | nan | nan | nan | Amazônia | 97.1 |
| ae3ce32a-c979-334a-b017-ef032eb139eb | -3.4968 | -53.995 | 2024-11-17 00:10:00 | GOES-16 | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | 71.0 |
| 85e34fe0-fd46-3695-b4fb-1e9f3e2ad3ec | -3.793 | -46.052 | 2024-11-17 00:10:00 | GOES-16 | ALTO ALEGRE DO PINDARÉ | MARANHÃO | Brasil | 2100477 | 21 | 33 | nan | nan | nan | Amazônia | 99.9 |
| 064d902d-35cd-3028-aa3a-caf175439755 | -2.5138 | -45.4747 | 2024-11-17 00:10:00 | GOES-16 | PRESIDENTE SARNEY | MARANHÃO | Brasil | 2109270 | 21 | 33 | nan | nan | nan | Amazônia | 65.3 |
| b204b605-4cb9-3310-8a79-4c6e973ec6a8 | 0.6159 | -51.7881 | 2024-11-17 00:10:00 | GOES-16 | PORTO GRANDE | AMAPÁ | Brasil | 1600535 | 16 | 33 | nan | nan | nan | Amazônia | 46.6 |
| b550c38b-f6b7-3978-9594-c328a3e19ccd | -2.5988 | -47.5488 | 2024-11-17 00:10:00 | GOES-16 | IPIXUNA DO PARÁ | PARÁ | Brasil | 1503457 | 15 | 33 | nan | nan | nan | Amazônia | 106.5 |
| 0c768a97-ba98-33d7-9127-c74540652e26 | -3.7931 | -46.0297 | 2024-11-17 00:10:00 | GOES-16 | ALTO ALEGRE DO PINDARÉ | MARANHÃO | Brasil | 2100477 | 21 | 33 | nan | nan | nan | Amazônia | 115.6 |
| 7bc90029-7b48-37fd-a118-7c3f9f39cb13 | -3.7744 | -46.0528 | 2024-11-17 00:10:00 | GOES-16 | ALTO ALEGRE DO PINDARÉ | MARANHÃO | Brasil | 2100477 | 21 | 33 | nan | nan | nan | Amazônia | 77.0 |
| 417a8ec8-3503-33d4-a650-dadc7462790e | -2.6595 | -46.2065 | 2024-11-17 00:10:00 | GOES-16 | CENTRO NOVO DO MARANHÃO | MARANHÃO | Brasil | 2103174 | 21 | 33 | nan | nan | nan | Amazônia | 93.8 |
| 3a32bba7-ec9f-3464-94dd-10e49d4f3758 | -1.4888 | -47.3999 | 2024-11-17 00:10:00 | GOES-16 | SÃO MIGUEL DO GUAMÁ | PARÁ | Brasil | 1507607 | 15 | 33 | nan | nan | nan | Amazônia | 55.9 |
| ec28f7da-db02-3136-bd43-84a46c8bebb0 | -2.514 | -45.4298 | 2024-11-17 00:10:00 | GOES-16 | PRESIDENTE SARNEY | MARANHÃO | Brasil | 2109270 | 21 | 33 | nan | nan | nan | Amazônia | 81.7 |
| 711daeb1-8b30-30f9-ad8c-5450ba4932c3 | -4.5614 | -48.0141 | 2024-11-17 00:10:00 | GOES-16 | RONDON DO PARÁ | PARÁ | Brasil | 1506187 | 15 | 33 | nan | nan | nan | Amazônia | 45.6 |
| 681e1e6b-b1de-3946-b08f-a8ea0564009c | -4.2049 | -48.6995 | 2024-11-17 00:10:00 | GOES-16 | RONDON DO PARÁ | PARÁ | Brasil | 1506187 | 15 | 33 | nan | nan | nan | Amazônia | 45.3 |
| 07d91f0b-d26b-3569-9935-9db7053beeac | -3.5678 | -50.2534 | 2024-11-17 00:10:00 | GOES-16 | PACAJÁ | PARÁ | Brasil | 1505486 | 15 | 33 | nan | nan | nan | Amazônia | 75.9 |
| 000249bc-0074-30b5-a2a2-ef7b6e1f3b55 | -4.2234 | -48.6986 | 2024-11-17 00:10:00 | GOES-16 | RONDON DO PARÁ | PARÁ | Brasil | 1506187 | 15 | 33 | nan | nan | nan | Amazônia | 40.0 |
| edc57076-67bc-3606-8339-e3faf876020c | -1.9166 | -46.5804 | 2024-11-17 00:10:00 | GOES-16 | CACHOEIRA DO PIRIÁ | PARÁ | Brasil | 1501956 | 15 | 33 | nan | nan | nan | Amazônia | 71.3 |
| 43a41570-6fdd-34a5-8f23-df4ad6d01f80 | -12.4004 | -57.5127 | 2024-11-17 00:10:00 | GOES-16 | NOVA MARINGÁ | MATO GROSSO | Brasil | 5108907 | 51 | 33 | nan | nan | nan | Amazônia | 74.7 |
| af3849f1-380e-37d0-bdc5-907e1c23d10a | -3.5124 | -50.2553 | 2024-11-17 00:10:00 | GOES-16 | PACAJÁ | PARÁ | Brasil | 1505486 | 15 | 33 | nan | nan | nan | Amazônia | 67.7 |
| bc568f36-b0a7-3572-9028-98c796967b8b | -4.5616 | -47.9925 | 2024-11-17 00:10:00 | GOES-16 | RONDON DO PARÁ | PARÁ | Brasil | 1506187 | 15 | 33 | nan | nan | nan | Amazônia | 47.4 |
| ef78beec-eecc-3057-9741-2527a4885f99 | -2.5139 | -45.4522 | 2024-11-17 00:10:00 | GOES-16 | PRESIDENTE SARNEY | MARANHÃO | Brasil | 2109270 | 21 | 33 | nan | nan | nan | Amazônia | 273.4 |
| 81f4357c-30a1-3d4b-b352-c6ea72648bb1 | -2.678 | -46.2281 | 2024-11-17 00:10:00 | GOES-16 | CENTRO NOVO DO MARANHÃO | MARANHÃO | Brasil | 2103174 | 21 | 33 | nan | nan | nan | Amazônia | 65.6 |
| 59a2b486-1196-3b2e-8b9c-2eed75081400 | -2.8614 | -46.7306 | 2024-11-17 00:10:00 | GOES-16 | PARAGOMINAS | PARÁ | Brasil | 1505502 | 15 | 33 | nan | nan | nan | Amazônia | 130.5 |
| baa9367a-0587-3fad-90c7-944887b207a0 | -8.4522 | -44.223 | 2024-11-17 00:10:00 | GOES-16 | ALVORADA DO GURGUÉIA | PIAUÍ | Brasil | 2200459 | 22 | 33 | nan | nan | nan | Cerrado | 107.8 |
| 7ad15b0f-2973-3b9d-86a7-3fd64a72909f | -3.5309 | -50.2547 | 2024-11-17 00:10:00 | GOES-16 | PACAJÁ | PARÁ | Brasil | 1505486 | 15 | 33 | nan | nan | nan | Amazônia | 107.9 |
| 89934840-2658-39ab-9029-7b840890bb7f | -2.8801 | -46.7079 | 2024-11-17 00:10:00 | GOES-16 | PARAGOMINAS | PARÁ | Brasil | 1505502 | 15 | 33 | nan | nan | nan | Amazônia | 66.4 |
| 1f746a3d-f646-3cca-8afe-d287e32b7d09 | -3.7745 | -46.0305 | 2024-11-17 00:10:00 | GOES-16 | ALTO ALEGRE DO PINDARÉ | MARANHÃO | Brasil | 2100477 | 21 | 33 | nan | nan | nan | Amazônia | 84.5 |
| 0d410061-efb3-3117-9e8b-4bd4bf220f55 | -4.4681 | -48.1054 | 2024-11-17 00:10:00 | GOES-16 | RONDON DO PARÁ | PARÁ | Brasil | 1506187 | 15 | 33 | nan | nan | nan | Amazônia | 37.5 |
| 5b928230-6111-39fa-90b1-baedb48572e1 | -8.4339 | -44.1788 | 2024-11-17 00:10:00 | GOES-16 | ALVORADA DO GURGUÉIA | PIAUÍ | Brasil | 2200459 | 22 | 33 | nan | nan | nan | Cerrado | 147.9 |
| 3c7fae3c-65d4-3387-8b07-fad0a830037c | -2.6231 | -46.0299 | 2024-11-17 00:10:00 | GOES-16 | MARANHÃOZINHO | MARANHÃO | Brasil | 2106375 | 21 | 33 | nan | nan | nan | Amazônia | 75.4 |
| 572d9e8e-5500-3211-8f73-cccf0ded2df3 | -2.678 | -46.2059 | 2024-11-17 00:10:00 | GOES-16 | CENTRO NOVO DO MARANHÃO | MARANHÃO | Brasil | 2103174 | 21 | 33 | nan | nan | nan | Amazônia | 119.1 |
| 0c6f1287-1f10-3617-847d-87d5a66cce83 | -8.4528 | -44.1767 | 2024-11-17 00:10:00 | GOES-16 | ALVORADA DO GURGUÉIA | PIAUÍ | Brasil | 2200459 | 22 | 33 | nan | nan | nan | Cerrado | 217.0 |
| d9416412-6ad4-3c03-aa8e-9232ba708a41 | 0.6159 | -51.7676 | 2024-11-17 00:10:00 | GOES-16 | PORTO GRANDE | AMAPÁ | Brasil | 1600535 | 16 | 33 | nan | nan | nan | Amazônia | 77.2 |
| e96ecfa7-e146-3cb4-8104-fb0d9a453260 | -3.5494 | -50.254 | 2024-11-17 00:20:00 | GOES-16 | PACAJÁ | PARÁ | Brasil | 1505486 | 15 | 33 | nan | nan | nan | Amazônia | 82.4 |
| 1c9765a6-418f-3c82-a797-8192e6040351 | -8.4333 | -44.2251 | 2024-11-17 00:20:00 | GOES-16 | ALVORADA DO GURGUÉIA | PIAUÍ | Brasil | 2200459 | 22 | 33 | nan | nan | nan | Cerrado | 102.1 |
| f9413fbf-8906-3f2b-ac0d-072c18dfae2c | -2.5139 | -45.4522 | 2024-11-17 00:20:00 | GOES-16 | PRESIDENTE SARNEY | MARANHÃO | Brasil | 2109270 | 21 | 33 | nan | nan | nan | Amazônia | 101.2 |
| 6df90029-3740-33a8-920b-314a2f3ab650 | -8.4522 | -44.223 | 2024-11-17 00:20:00 | GOES-16 | ALVORADA DO GURGUÉIA | PIAUÍ | Brasil | 2200459 | 22 | 33 | nan | nan | nan | Cerrado | 128.2 |
| 91a94de9-0d4b-34f0-afd4-ec28aefba378 | -2.8615 | -46.7086 | 2024-11-17 00:20:00 | GOES-16 | PARAGOMINAS | PARÁ | Brasil | 1505502 | 15 | 33 | nan | nan | nan | Amazônia | 96.0 |
| 0f166319-c838-3d04-ae53-527dc4893e17 | -2.6595 | -46.2065 | 2024-11-17 00:20:00 | GOES-16 | CENTRO NOVO DO MARANHÃO | MARANHÃO | Brasil | 2103174 | 21 | 33 | nan | nan | nan | Amazônia | 96.5 |
| 0820e4e3-b7b3-3b61-9afe-3ee0c1194965 | -4.58 | -48.0132 | 2024-11-17 00:20:00 | GOES-16 | RONDON DO PARÁ | PARÁ | Brasil | 1506187 | 15 | 33 | nan | nan | nan | Amazônia | 38.6 |


[Clique aqui para ver as próximas entradas](README2.md)
