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

## Dados Diários - Página 267

| ID | Latitude | Longitude | Data/Hora GMT | Satélite | Município | Estado | País | Município ID | Estado ID | País ID | Dias sem Chuva | Precipitação | Risco de Fogo | Bioma | FRP |
|----|----------|-----------|---------------|----------|-----------|--------|------|--------------|-----------|---------|----------------|--------------|----------------|-------|-----|
| 24747904-88a4-34ed-8d37-2a84f74d8c50 | -10.87917 | -47.61031 | 2026-10-08 16:18:00 | NPP-375 | PONTE ALTA DO TOCANTINS | TOCANTINS | Brasil | 1717909 | 17 | 33 | nan | nan | nan | Cerrado | 4.1 |
| 04628ec1-2eb5-3606-ba00-467ddf511377 | -13.99144 | -46.36203 | 2026-10-08 16:18:00 | NPP-375 | GUARANI DE GOIÁS | GOIÁS | Brasil | 5209408 | 52 | 33 | nan | nan | nan | Cerrado | 3.0 |
| 660731da-561b-332e-993d-b20d8f0846e5 | -12.22788 | -43.93258 | 2026-10-08 16:18:00 | NPP-375 | WANDERLEY | BAHIA | Brasil | 2933455 | 29 | 33 | nan | nan | nan | Cerrado | 51.0 |
| 6d526aa1-acdb-3e17-aaae-300cd44bdfae | -11.20687 | -44.86064 | 2026-10-08 16:18:00 | NPP-375 | SANTA RITA DE CÁSSIA | BAHIA | Brasil | 2928406 | 29 | 33 | nan | nan | nan | Cerrado | 5.5 |
| e3a4dbec-3e73-38c8-8d11-d9e12c2fc85e | -11.4064 | -44.96204 | 2026-10-08 16:18:00 | NPP-375 | RIACHÃO DAS NEVES | BAHIA | Brasil | 2926202 | 29 | 33 | nan | nan | nan | Cerrado | 8.1 |
| 2292b54a-7dc6-3412-b97e-484a9dc0161f | -11.7238 | -43.42223 | 2026-10-08 16:18:00 | NPP-375 | BARRA | BAHIA | Brasil | 2902708 | 29 | 33 | nan | nan | nan | Cerrado | 12.1 |
| 7c9b628f-e116-3a9c-a135-ce8d052394d4 | -11.24298 | -45.24372 | 2026-10-08 16:18:00 | NPP-375 | FORMOSA DO RIO PRETO | BAHIA | Brasil | 2911105 | 29 | 33 | nan | nan | nan | Cerrado | 15.9 |
| f91e1a10-135e-34e4-874d-e3e9c0b47278 | -11.07367 | -44.02222 | 2026-10-08 16:18:00 | NPP-375 | MANSIDÃO | BAHIA | Brasil | 2920452 | 29 | 33 | nan | nan | nan | Cerrado | 36.7 |
| 45c9c6dd-7345-3767-9078-2a3affa76b60 | -11.20195 | -49.42343 | 2026-10-08 16:18:00 | NPP-375 | DUERÉ | TOCANTINS | Brasil | 1707306 | 17 | 33 | nan | nan | nan | Cerrado | 17.6 |
| 50fe14c1-5b0e-3add-9b0e-07b204f22bc7 | -9.85413 | -47.85244 | 2026-10-08 16:18:00 | NPP-375 | RIO SONO | TOCANTINS | Brasil | 1718758 | 17 | 33 | nan | nan | nan | Cerrado | 38.2 |
| 7a2d3eae-37d1-3abc-9cc1-5937daaa68b3 | -11.39419 | -47.55569 | 2026-10-08 16:18:00 | NPP-375 | NATIVIDADE | TOCANTINS | Brasil | 1714203 | 17 | 33 | nan | nan | nan | Cerrado | 6.4 |
| 54f62d43-4f5e-3669-ad75-7783cf928110 | -13.36346 | -47.26978 | 2026-10-08 16:18:00 | NPP-375 | MONTE ALEGRE DE GOIÁS | GOIÁS | Brasil | 5213509 | 52 | 33 | nan | nan | nan | Cerrado | 2.6 |
| f2ea368d-ebed-3802-80aa-4d7b97de0f47 | -11.59759 | -43.67304 | 2026-10-08 16:18:00 | NPP-375 | BARRA | BAHIA | Brasil | 2902708 | 29 | 33 | nan | nan | nan | Cerrado | 7.8 |
| 32dca3fa-a052-3720-b857-2d41f5a053ab | -11.63988 | -43.70226 | 2026-10-08 16:18:00 | NPP-375 | BARRA | BAHIA | Brasil | 2902708 | 29 | 33 | nan | nan | nan | Cerrado | 22.7 |
| 72af1859-6dc4-3d9b-900b-10e6ad6cf2c7 | -9.0316 | -44.37318 | 2026-10-08 16:18:00 | NPP-375 | CURRAIS | PIAUÍ | Brasil | 2203230 | 22 | 33 | nan | nan | nan | Cerrado | 89.8 |
| 225be7fa-2d7d-328f-bb2e-19f236fcc1b7 | -11.45129 | -43.38859 | 2026-10-08 16:18:00 | NPP-375 | BARRA | BAHIA | Brasil | 2902708 | 29 | 33 | nan | nan | nan | Cerrado | 35.2 |
| 39ea8e81-629b-3bfb-8357-ac84656957e1 | -11.72144 | -43.64045 | 2026-10-08 16:18:00 | NPP-375 | BARRA | BAHIA | Brasil | 2902708 | 29 | 33 | nan | nan | nan | Cerrado | 20.5 |
| eb994a5d-3f61-3db6-8d5f-783a4614700e | -9.84111 | -47.84804 | 2026-10-08 16:18:00 | NPP-375 | RIO SONO | TOCANTINS | Brasil | 1718758 | 17 | 33 | nan | nan | nan | Cerrado | 9.1 |
| 7ed64aae-ed96-3397-92bd-1afcca307257 | -9.89729 | -44.81136 | 2026-10-08 16:18:00 | NPP-375 | RIACHO FRIO | PIAUÍ | Brasil | 2208858 | 22 | 33 | nan | nan | nan | Cerrado | 18.7 |
| 57869327-7ea6-3fdf-971b-441d6a864900 | -7.02792 | -35.20778 | 2026-10-08 16:18:00 | NPP-375 | SAPÉ | PARAÍBA | Brasil | 2515302 | 25 | 33 | nan | nan | nan | Mata Atlântica | 16.3 |
| 0a31e39f-7e82-3df3-ae7c-78e42774f4e1 | -10.94975 | -45.37956 | 2026-10-08 16:18:00 | NPP-375 | FORMOSA DO RIO PRETO | BAHIA | Brasil | 2911105 | 29 | 33 | nan | nan | nan | Cerrado | 10.0 |
| 493a756a-b282-3d8a-8018-9e8fca4f404c | -9.8862 | -44.8559 | 2026-10-08 16:18:00 | NPP-375 | RIACHO FRIO | PIAUÍ | Brasil | 2208858 | 22 | 33 | nan | nan | nan | Cerrado | 35.2 |
| e3c91656-471d-3ffd-8691-21c2831e4a30 | -11.24983 | -46.25702 | 2026-10-08 16:18:00 | NPP-375 | FORMOSA DO RIO PRETO | BAHIA | Brasil | 2911105 | 29 | 33 | nan | nan | nan | Cerrado | 13.0 |
| 1aba9f4c-2566-3734-9a61-9c2f8c44f1cc | -10.5742 | -46.2942 | 2026-10-08 16:18:00 | NPP-375 | MATEIROS | TOCANTINS | Brasil | 1712702 | 17 | 33 | nan | nan | nan | Cerrado | 11.1 |
| 84aa73f4-5397-3431-b0bb-2954116996e7 | -13.59725 | -48.20649 | 2026-10-08 16:18:00 | NPP-375 | MINAÇU | GOIÁS | Brasil | 5213087 | 52 | 33 | nan | nan | nan | Cerrado | 3.4 |
| bd2897e8-ce12-3b0c-b8d7-9b06d1031def | -9.23201 | -45.30188 | 2026-10-08 16:18:00 | NPP-375 | BAIXA GRANDE DO RIBEIRO | PIAUÍ | Brasil | 2201150 | 22 | 33 | nan | nan | nan | Cerrado | 9.6 |
| ff48831d-8a3f-3785-87cd-02fb48327163 | -9.94198 | -43.558 | 2026-10-08 16:18:00 | NPP-375 | PILÃO ARCADO | BAHIA | Brasil | 2924405 | 29 | 33 | nan | nan | nan | Cerrado | 41.5 |
| ee95c355-27f7-3ddb-8ca7-53316f69f266 | -12.7701 | -44.8684 | 2026-10-08 16:18:00 | NPP-375 | SÃO DESIDÉRIO | BAHIA | Brasil | 2928901 | 29 | 33 | nan | nan | nan | Cerrado | 17.2 |
| bed1dadb-d3d0-3345-af6b-aba659c1405e | -9.94393 | -43.57222 | 2026-10-08 16:18:00 | NPP-375 | PILÃO ARCADO | BAHIA | Brasil | 2924405 | 29 | 33 | nan | nan | nan | Cerrado | 26.9 |
| f984c32f-5435-3605-a691-e6e4eff9d3b6 | -8.2904 | -45.73886 | 2026-10-08 16:18:00 | NPP-375 | TASSO FRAGOSO | MARANHÃO | Brasil | 2112001 | 21 | 33 | nan | nan | nan | Cerrado | 18.3 |
| f2bc04f8-4745-3c03-bd20-0d23b13554ce | -8.97629 | -47.5546 | 2026-10-08 16:18:00 | NPP-375 | CENTENÁRIO | TOCANTINS | Brasil | 1704105 | 17 | 33 | nan | nan | nan | Cerrado | 7.0 |
| 284cc680-fe7f-3ba6-9798-65e8f37d458a | -8.79566 | -47.28229 | 2026-10-08 16:18:00 | NPP-375 | RECURSOLÂNDIA | TOCANTINS | Brasil | 1718501 | 17 | 33 | nan | nan | nan | Cerrado | 1.7 |
| 158a2da6-c5f0-30df-b243-2241782ac138 | -12.99008 | -41.00521 | 2026-10-08 16:18:00 | NPP-375 | ITAETÉ | BAHIA | Brasil | 2915007 | 29 | 33 | nan | nan | nan | Caatinga | 8.5 |
| 0a40508c-25b4-3294-ab13-3a7cd6fd149d | -10.41884 | -47.26754 | 2026-10-08 16:18:00 | NPP-375 | PONTE ALTA DO TOCANTINS | TOCANTINS | Brasil | 1717909 | 17 | 33 | nan | nan | nan | Cerrado | 10.0 |
| 6397de58-8e07-30c1-869c-613ae18ff024 | -11.7714 | -46.76753 | 2026-10-08 16:18:00 | NPP-375 | DIANÓPOLIS | TOCANTINS | Brasil | 1707009 | 17 | 33 | nan | nan | nan | Cerrado | 6.7 |
| 6bd476bb-6cf6-37e2-845b-34a95a61175f | -11.20238 | -44.86131 | 2026-10-08 16:18:00 | NPP-375 | SANTA RITA DE CÁSSIA | BAHIA | Brasil | 2928406 | 29 | 33 | nan | nan | nan | Cerrado | 5.5 |
| a6e9fe28-df8c-3060-abb7-f05a7b508246 | -10.40405 | -36.89006 | 2026-10-08 16:18:00 | NPP-375 | JAPARATUBA | SERGIPE | Brasil | 2803302 | 28 | 33 | nan | nan | nan | Mata Atlântica | 1.6 |
| a2074d05-2c1d-3cf8-8965-64c87ab410f0 | -13.14352 | -46.34319 | 2026-10-08 16:18:00 | NPP-375 | SÃO DOMINGOS | GOIÁS | Brasil | 5219803 | 52 | 33 | nan | nan | nan | Cerrado | 6.9 |
| 0eab4830-333c-330a-b0de-db6b94131756 | -8.94242 | -45.14067 | 2026-10-08 16:18:00 | NPP-375 | BAIXA GRANDE DO RIBEIRO | PIAUÍ | Brasil | 2201150 | 22 | 33 | nan | nan | nan | Cerrado | 53.8 |
| dc01c7ed-5157-33b5-beba-59c4d092d078 | -12.02953 | -43.44339 | 2026-10-08 16:18:00 | NPP-375 | MUQUÉM DO SÃO FRANCISCO | BAHIA | Brasil | 2922250 | 29 | 33 | nan | nan | nan | Cerrado | 59.0 |
| 78853f76-99fe-3cac-a9a5-18ba5fc0afe5 | -11.60639 | -43.67525 | 2026-10-08 16:18:00 | NPP-375 | BARRA | BAHIA | Brasil | 2902708 | 29 | 33 | nan | nan | nan | Cerrado | 7.0 |
| d4cef362-309e-308e-8842-9b594d54af0e | -8.02338 | -36.50488 | 2026-10-08 16:18:00 | NPP-375 | JATAÚBA | PERNAMBUCO | Brasil | 2608008 | 26 | 33 | nan | nan | nan | Caatinga | 8.7 |
| 909ce47c-1448-3f4c-bd7c-f977c8cd8ef8 | -11.20662 | -49.41615 | 2026-10-08 16:18:00 | NPP-375 | DUERÉ | TOCANTINS | Brasil | 1707306 | 17 | 33 | nan | nan | nan | Cerrado | 19.6 |
| b51f1c35-1529-389c-a6b5-e5ca722f0e78 | -11.63676 | -43.71055 | 2026-10-08 16:18:00 | NPP-375 | BARRA | BAHIA | Brasil | 2902708 | 29 | 33 | nan | nan | nan | Cerrado | 29.3 |
| cca86cd2-4c55-37a6-94b6-e26675b9c542 | -11.76814 | -43.5344 | 2026-10-08 16:18:00 | NPP-375 | BARRA | BAHIA | Brasil | 2902708 | 29 | 33 | nan | nan | nan | Cerrado | 158.5 |
| 78400120-5282-3c41-87a7-88c0340d5fc7 | -10.51472 | -47.30935 | 2026-10-08 16:18:00 | NPP-375 | PONTE ALTA DO TOCANTINS | TOCANTINS | Brasil | 1717909 | 17 | 33 | nan | nan | nan | Cerrado | 10.1 |
| 767a55de-0a04-31f4-ab52-fb57728be410 | -11.10968 | -44.00116 | 2026-10-08 16:18:00 | NPP-375 | MANSIDÃO | BAHIA | Brasil | 2920452 | 29 | 33 | nan | nan | nan | Cerrado | 6.6 |
| 4073ab48-2720-3170-9a99-c3b3fa3bb7cf | -8.59301 | -44.87415 | 2026-10-08 16:18:00 | NPP-375 | CURRAIS | PIAUÍ | Brasil | 2203230 | 22 | 33 | nan | nan | nan | Cerrado | 6.8 |
| 2b5aa475-a8d0-35c6-b25c-b0d6daa9ef14 | -11.08267 | -44.02502 | 2026-10-08 16:18:00 | NPP-375 | MANSIDÃO | BAHIA | Brasil | 2920452 | 29 | 33 | nan | nan | nan | Cerrado | 166.9 |
| 2e3aba08-ffc0-3ceb-b085-6fd73e673dbc | -8.96199 | -45.15118 | 2026-10-08 16:18:00 | NPP-375 | BAIXA GRANDE DO RIBEIRO | PIAUÍ | Brasil | 2201150 | 22 | 33 | nan | nan | nan | Cerrado | 184.8 |
| d3101cdd-eac4-3263-879a-70e29bfff3b4 | -9.02793 | -44.37767 | 2026-10-08 16:18:00 | NPP-375 | CURRAIS | PIAUÍ | Brasil | 2203230 | 22 | 33 | nan | nan | nan | Cerrado | 89.8 |
| 610f5ead-37cb-30cf-b433-2a630350f926 | -10.42058 | -47.27671 | 2026-10-08 16:18:00 | NPP-375 | PONTE ALTA DO TOCANTINS | TOCANTINS | Brasil | 1717909 | 17 | 33 | nan | nan | nan | Cerrado | 4.9 |
| 326e4125-a272-3d48-9ba6-904ef4ddeb60 | -11.2482 | -45.24771 | 2026-10-08 16:18:00 | NPP-375 | FORMOSA DO RIO PRETO | BAHIA | Brasil | 2911105 | 29 | 33 | nan | nan | nan | Cerrado | 15.9 |
| 146acdc1-7cb3-3025-a0af-52a7bc242d32 | -11.2552 | -47.74886 | 2026-10-08 16:18:00 | NPP-375 | PINDORAMA DO TOCANTINS | TOCANTINS | Brasil | 1717008 | 17 | 33 | nan | nan | nan | Cerrado | 2.7 |
| a8031dcb-0702-3753-9180-8d7039eb003a | -10.43212 | -47.28846 | 2026-10-08 16:18:00 | NPP-375 | PONTE ALTA DO TOCANTINS | TOCANTINS | Brasil | 1717909 | 17 | 33 | nan | nan | nan | Cerrado | 4.8 |
| 6458de94-f727-305f-8c04-61703d03e2a4 | -12.24219 | -44.73723 | 2026-10-08 16:18:00 | NPP-375 | CATOLÂNDIA | BAHIA | Brasil | 2907400 | 29 | 33 | nan | nan | nan | Cerrado | 18.4 |
| 77f7ccc5-6ffb-33aa-81a6-2b42e4639564 | -8.99571 | -42.33807 | 2026-10-08 16:18:00 | NPP-375 | SÃO RAIMUNDO NONATO | PIAUÍ | Brasil | 2210607 | 22 | 33 | nan | nan | nan | Caatinga | 10.2 |
| 288eafb9-329a-333b-aa5c-872124a71854 | -8.78291 | -47.26511 | 2026-10-08 16:18:00 | NPP-375 | RECURSOLÂNDIA | TOCANTINS | Brasil | 1718501 | 17 | 33 | nan | nan | nan | Cerrado | 15.5 |
| 34d0fef8-9657-3501-9ea8-93af22b55566 | -13.7048 | -49.08422 | 2026-10-08 16:18:00 | NPP-375 | SANTA TEREZA DE GOIÁS | GOIÁS | Brasil | 5219605 | 52 | 33 | nan | nan | nan | Cerrado | 17.4 |
| e9310523-4096-3117-86e4-f722878ede74 | -12.04311 | -47.38358 | 2026-10-08 16:18:00 | NPP-375 | CONCEIÇÃO DO TOCANTINS | TOCANTINS | Brasil | 1705607 | 17 | 33 | nan | nan | nan | Cerrado | 6.4 |
| 88ff3b7e-4a6b-3b62-ac6d-1561a23cff71 | -12.62127 | -47.88977 | 2026-10-08 16:18:00 | NPP-375 | PARANÃ | TOCANTINS | Brasil | 1716208 | 17 | 33 | nan | nan | nan | Cerrado | 11.7 |
| 434f9122-724d-3d79-9b2a-ac73fca4b492 | -11.78057 | -43.53267 | 2026-10-08 16:18:00 | NPP-375 | BARRA | BAHIA | Brasil | 2902708 | 29 | 33 | nan | nan | nan | Cerrado | 29.2 |
| 9111a4c9-eaed-3feb-95e5-77e6f755930f | -9.82302 | -45.68512 | 2026-10-08 16:18:00 | NPP-375 | BARREIRAS DO PIAUÍ | PIAUÍ | Brasil | 2201309 | 22 | 33 | nan | nan | nan | Cerrado | 17.4 |
| 256e45e9-1548-3c79-aaae-a5e147b5c8e4 | -10.3392 | -47.76199 | 2026-10-08 16:18:00 | NPP-375 | SANTA TEREZA DO TOCANTINS | TOCANTINS | Brasil | 1719004 | 17 | 33 | nan | nan | nan | Cerrado | 3.2 |
| 9237ad41-1fc9-3cff-9395-49cd33fe1c5d | -11.85167 | -45.28784 | 2026-10-08 16:18:00 | NPP-375 | BARREIRAS | BAHIA | Brasil | 2903201 | 29 | 33 | nan | nan | nan | Cerrado | 3.7 |
| 68620d23-7827-3c1e-99ec-46a723df15ea | -11.77671 | -45.58353 | 2026-10-08 16:18:00 | NPP-375 | RIACHÃO DAS NEVES | BAHIA | Brasil | 2926202 | 29 | 33 | nan | nan | nan | Cerrado | 31.1 |
| 3d2d5f74-0450-3d25-b4ef-f6c15f7fce94 | -12.1773 | -44.81026 | 2026-10-08 16:18:00 | NPP-375 | BARREIRAS | BAHIA | Brasil | 2903201 | 29 | 33 | nan | nan | nan | Cerrado | 16.7 |
| 3e0a54e2-dcb1-3619-8b68-388d3f9a291e | -11.6276 | -43.07716 | 2026-10-08 16:18:00 | NPP-375 | MORPARÁ | BAHIA | Brasil | 2921609 | 29 | 33 | nan | nan | nan | Caatinga | 10.7 |
| b80ad3b1-ae45-36ac-b423-3dbdaf7a714d | -13.96174 | -44.85983 | 2026-10-08 16:18:00 | NPP-375 | COCOS | BAHIA | Brasil | 2908101 | 29 | 33 | nan | nan | nan | Cerrado | 23.2 |
| b097c7b0-ecfa-3401-9838-2da75d71326c | -9.03214 | -44.37702 | 2026-10-08 16:18:00 | NPP-375 | BOM JESUS | PIAUÍ | Brasil | 2201903 | 22 | 33 | nan | nan | nan | Cerrado | 89.8 |
| 02f8bf5f-83a5-3e93-bacd-1e52df013ac6 | -10.46352 | -47.20037 | 2026-10-08 16:18:00 | NPP-375 | PONTE ALTA DO TOCANTINS | TOCANTINS | Brasil | 1717909 | 17 | 33 | nan | nan | nan | Cerrado | 2.6 |
| e31ee55d-afab-360d-a749-69e390be1c5c | -12.22563 | -43.93654 | 2026-10-08 16:18:00 | NPP-375 | WANDERLEY | BAHIA | Brasil | 2933455 | 29 | 33 | nan | nan | nan | Cerrado | 63.4 |
| c76ac12d-f9a4-3dab-b578-cf56c19f9963 | -9.1426 | -45.82167 | 2026-10-08 16:18:00 | NPP-375 | SANTA FILOMENA | PIAUÍ | Brasil | 2209203 | 22 | 33 | nan | nan | nan | Cerrado | 15.7 |
| da27ae7c-4fb3-3313-b6a2-7e484b111c4a | -10.37738 | -46.3075 | 2026-10-08 16:18:00 | NPP-375 | MATEIROS | TOCANTINS | Brasil | 1712702 | 17 | 33 | nan | nan | nan | Cerrado | 19.6 |
| b072735c-dc53-3db7-8dcd-6fe9a746d6ab | -8.29074 | -45.70949 | 2026-10-08 16:18:00 | NPP-375 | TASSO FRAGOSO | MARANHÃO | Brasil | 2112001 | 21 | 33 | nan | nan | nan | Cerrado | 13.4 |
| 0389df1e-06ed-3a2d-8ead-d92f3b424e6d | -14.17955 | -48.67233 | 2026-10-08 16:18:00 | NPP-375 | NIQUELÂNDIA | GOIÁS | Brasil | 5214606 | 52 | 33 | nan | nan | nan | Cerrado | 7.9 |
| 4b271da5-939f-31bb-b198-81565e6876ca | -12.57767 | -44.6705 | 2026-10-08 16:18:00 | NPP-375 | SÃO DESIDÉRIO | BAHIA | Brasil | 2928901 | 29 | 33 | nan | nan | nan | Cerrado | 10.2 |
| f01dacf3-d399-373b-b4bd-d7a66c8e14ac | -9.82418 | -45.7655 | 2026-10-08 16:18:00 | NPP-375 | BARREIRAS DO PIAUÍ | PIAUÍ | Brasil | 2201309 | 22 | 33 | nan | nan | nan | Cerrado | 19.0 |
| 655d35e2-1769-3cd8-86a7-037d30862233 | -8.28271 | -45.71752 | 2026-10-08 16:18:00 | NPP-375 | TASSO FRAGOSO | MARANHÃO | Brasil | 2112001 | 21 | 33 | nan | nan | nan | Cerrado | 14.6 |
| 3635218a-2aa4-3646-9650-6163b39c97a2 | -9.45619 | -44.62146 | 2026-10-08 16:18:00 | NPP-375 | REDENÇÃO DO GURGUÉIA | PIAUÍ | Brasil | 2208700 | 22 | 33 | nan | nan | nan | Cerrado | 7.2 |
| d23b91df-ffd7-3eb0-9583-5b81045e09d2 | -11.60962 | -43.63662 | 2026-10-08 16:18:00 | NPP-375 | BARRA | BAHIA | Brasil | 2902708 | 29 | 33 | nan | nan | nan | Cerrado | 64.1 |
| 4c016c22-4da8-333d-bd5f-b6872104f908 | -12.19277 | -44.82251 | 2026-10-08 16:18:00 | NPP-375 | BARREIRAS | BAHIA | Brasil | 2903201 | 29 | 33 | nan | nan | nan | Cerrado | 40.6 |
| 0c0ea081-f8b2-3419-943e-eca3e7ae13f2 | -10.45847 | -47.28576 | 2026-10-08 16:18:00 | NPP-375 | PONTE ALTA DO TOCANTINS | TOCANTINS | Brasil | 1717909 | 17 | 33 | nan | nan | nan | Cerrado | 126.5 |
| e57d4f08-40cf-3105-a7db-5df53a5b0104 | -11.24147 | -46.26999 | 2026-10-08 16:18:00 | NPP-375 | FORMOSA DO RIO PRETO | BAHIA | Brasil | 2911105 | 29 | 33 | nan | nan | nan | Cerrado | 12.3 |
| 59077586-43b8-3551-a41c-4c4a240c0e5a | -9.18615 | -46.70714 | 2026-10-08 16:18:00 | NPP-375 | BALSAS | MARANHÃO | Brasil | 2101400 | 21 | 33 | nan | nan | nan | Cerrado | 9.7 |
| 3ecc751f-e3bc-3648-a68b-a6501036d628 | -11.11021 | -44.00512 | 2026-10-08 16:18:00 | NPP-375 | MANSIDÃO | BAHIA | Brasil | 2920452 | 29 | 33 | nan | nan | nan | Cerrado | 30.4 |
| 3249bf91-7320-35d2-bf1e-b0b38c970604 | -10.41892 | -47.26419 | 2026-10-08 16:18:00 | NPP-375 | PONTE ALTA DO TOCANTINS | TOCANTINS | Brasil | 1717909 | 17 | 33 | nan | nan | nan | Cerrado | 6.1 |
| 73928753-6c50-357b-9040-6aa437714591 | -11.21907 | -45.26464 | 2026-10-08 16:18:00 | NPP-375 | FORMOSA DO RIO PRETO | BAHIA | Brasil | 2911105 | 29 | 33 | nan | nan | nan | Cerrado | 25.2 |
| 0eb282cc-96d0-3563-b7fe-82fb64ffd2a8 | -11.24017 | -46.25042 | 2026-10-08 16:18:00 | NPP-375 | FORMOSA DO RIO PRETO | BAHIA | Brasil | 2911105 | 29 | 33 | nan | nan | nan | Cerrado | 21.2 |
| 482fb43f-ec05-3a9d-934e-ba57d1023d1f | -11.36494 | -46.71281 | 2026-10-08 16:18:00 | NPP-375 | RIO DA CONCEIÇÃO | TOCANTINS | Brasil | 1718659 | 17 | 33 | nan | nan | nan | Cerrado | 6.3 |
| 0792f7ec-3482-3343-87a7-211725b47531 | -12.22393 | -44.70225 | 2026-10-08 16:18:00 | NPP-375 | CATOLÂNDIA | BAHIA | Brasil | 2907400 | 29 | 33 | nan | nan | nan | Cerrado | 6.6 |
| 4327e3db-76a0-3c0d-a817-3b729963d422 | -8.55263 | -46.91633 | 2026-10-08 16:18:00 | NPP-375 | RECURSOLÂNDIA | TOCANTINS | Brasil | 1718501 | 17 | 33 | nan | nan | nan | Cerrado | 12.5 |
| af0b4048-a2e6-3a19-9e3c-32dc848aadaa | -10.77286 | -46.57182 | 2026-10-08 16:18:00 | NPP-375 | MATEIROS | TOCANTINS | Brasil | 1712702 | 17 | 33 | nan | nan | nan | Cerrado | 9.5 |
| fed174dd-9770-30aa-984d-bc800ec1e8b4 | -9.39852 | -45.88861 | 2026-10-08 16:18:00 | NPP-375 | ALTO PARNAÍBA | MARANHÃO | Brasil | 2100501 | 21 | 33 | nan | nan | nan | Cerrado | 19.3 |
| 70fe0279-5779-3ad5-8bcd-5a7b322565cc | -13.6643 | -40.34684 | 2026-10-08 16:18:00 | NPP-375 | LAFAIETE COUTINHO | BAHIA | Brasil | 2918704 | 29 | 33 | nan | nan | nan | Caatinga | 3.9 |
| df90a5a8-bc27-324c-8e2a-f7014c8d0c11 | -8.6071 | -45.63753 | 2026-10-08 16:18:00 | NPP-375 | SANTA FILOMENA | PIAUÍ | Brasil | 2209203 | 22 | 33 | nan | nan | nan | Cerrado | 8.4 |
| 0bafc0fe-c162-3a50-8d6a-8a9155bf59c9 | -8.32512 | -45.03856 | 2026-10-08 16:18:00 | NPP-375 | BAIXA GRANDE DO RIBEIRO | PIAUÍ | Brasil | 2201150 | 22 | 33 | nan | nan | nan | Cerrado | 9.9 |
| ec73796c-fe6f-3c2e-9a3a-ae6a5cc0e2e0 | -10.67223 | -47.82601 | 2026-10-08 16:18:00 | NPP-375 | MONTE DO CARMO | TOCANTINS | Brasil | 1713601 | 17 | 33 | nan | nan | nan | Cerrado | 6.9 |
| c47c4706-f027-3e23-bbdd-e5cf112ff060 | -8.29496 | -45.74083 | 2026-10-08 16:18:00 | NPP-375 | TASSO FRAGOSO | MARANHÃO | Brasil | 2112001 | 21 | 33 | nan | nan | nan | Cerrado | 7.7 |
| 69bb9bd6-9f68-31c9-8987-b90e445a9754 | -10.76286 | -46.60411 | 2026-10-08 16:18:00 | NPP-375 | MATEIROS | TOCANTINS | Brasil | 1712702 | 17 | 33 | nan | nan | nan | Cerrado | 9.1 |


[Clique aqui para ver as próximas entradas](README268.md)
