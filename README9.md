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

## Dados Diários - Página 9

| ID | Latitude | Longitude | Data/Hora GMT | Satélite | Município | Estado | País | Município ID | Estado ID | País ID | Dias sem Chuva | Precipitação | Risco de Fogo | Bioma | FRP |
|----|----------|-----------|---------------|----------|-----------|--------|------|--------------|-----------|---------|----------------|--------------|----------------|-------|-----|
| d882d6a8-52f6-3ce4-ad3a-df66b9a20c38 | -5.8868 | -46.280499 | 2024-10-05 00:23:55 | METOP-C | GRAJAÚ | MARANHÃO | Brasil | 2104800 | 21 | 33 | nan | nan | nan | Cerrado | nan |
| 01714f5a-51da-30bb-a8c7-2b55079cf301 | -5.8888 | -46.289501 | 2024-10-05 00:23:55 | METOP-C | GRAJAÚ | MARANHÃO | Brasil | 2104800 | 21 | 33 | nan | nan | nan | Cerrado | nan |
| df0e4e97-28ff-3626-b205-777feb389de2 | -5.968 | -46.6464 | 2024-10-05 00:23:55 | METOP-C | SÍTIO NOVO | MARANHÃO | Brasil | 2111805 | 21 | 33 | nan | nan | nan | Cerrado | nan |
| 61e1769a-f0a7-3789-a482-adcc3f11680a | -5.9701 | -46.6558 | 2024-10-05 00:23:55 | METOP-C | SÍTIO NOVO | MARANHÃO | Brasil | 2111805 | 21 | 33 | nan | nan | nan | Cerrado | nan |
| 21de934d-4c83-3b8f-9bfb-32bf62033e8e | -5.0502 | -42.664902 | 2024-10-05 00:23:56 | METOP-C | TERESINA | PIAUÍ | Brasil | 2211001 | 22 | 33 | nan | nan | nan | Cerrado | nan |
| e48e0783-f0b1-3e6b-8396-e51a9953542e | -5.106 | -43.315399 | 2024-10-05 00:23:57 | METOP-C | CAXIAS | MARANHÃO | Brasil | 2103000 | 21 | 33 | nan | nan | nan | Cerrado | nan |
| 30dfe655-f2a3-3378-a3cb-7919e3e87748 | -5.1076 | -43.3223 | 2024-10-05 00:23:57 | METOP-C | CAXIAS | MARANHÃO | Brasil | 2103000 | 21 | 33 | nan | nan | nan | Cerrado | nan |
| 6ec5f124-191f-3828-ae12-b747c948765a | -5.9919 | -47.450802 | 2024-10-05 00:23:58 | METOP-C | MAURILÂNDIA DO TOCANTINS | TOCANTINS | Brasil | 1712801 | 17 | 33 | nan | nan | nan | Cerrado | nan |
| 7bddc39f-6b41-3110-8d16-6881acc29c30 | -5.9942 | -47.4613 | 2024-10-05 00:23:58 | METOP-C | MAURILÂNDIA DO TOCANTINS | TOCANTINS | Brasil | 1712801 | 17 | 33 | nan | nan | nan | Cerrado | nan |
| 6ebbfd83-6129-3262-b390-97655ffde7f0 | -4.9412 | -43.768002 | 2024-10-05 00:24:02 | METOP-C | SÃO JOÃO DO SOTER | MARANHÃO | Brasil | 2111078 | 21 | 33 | nan | nan | nan | Cerrado | nan |
| 6d8093ad-5405-3f63-afa3-a1f216a5f984 | -4.9428 | -43.775002 | 2024-10-05 00:24:02 | METOP-C | SÃO JOÃO DO SOTER | MARANHÃO | Brasil | 2111078 | 21 | 33 | nan | nan | nan | Cerrado | nan |
| d9e26a82-045c-3939-b64d-cb4aa54b69e9 | -4.9444 | -43.782001 | 2024-10-05 00:24:02 | METOP-C | SÃO JOÃO DO SOTER | MARANHÃO | Brasil | 2111078 | 21 | 33 | nan | nan | nan | Cerrado | nan |
| dfeac0f7-d69d-3aa8-b52f-7b0d8b3389e7 | -4.9314 | -43.770199 | 2024-10-05 00:24:02 | METOP-C | SÃO JOÃO DO SOTER | MARANHÃO | Brasil | 2111078 | 21 | 33 | nan | nan | nan | Cerrado | nan |
| 1067e47d-4863-3866-89d0-35b628c77661 | -4.933 | -43.777199 | 2024-10-05 00:24:02 | METOP-C | SÃO JOÃO DO SOTER | MARANHÃO | Brasil | 2111078 | 21 | 33 | nan | nan | nan | Cerrado | nan |
| 80300158-9e7b-3308-837e-1a73c39ae264 | -4.9346 | -43.784199 | 2024-10-05 00:24:02 | METOP-C | SÃO JOÃO DO SOTER | MARANHÃO | Brasil | 2111078 | 21 | 33 | nan | nan | nan | Cerrado | nan |
| 2f56f5d9-e903-316e-a7d0-c220f014e7ba | -4.6945 | -43.1833 | 2024-10-05 00:24:03 | METOP-C | CAXIAS | MARANHÃO | Brasil | 2103000 | 21 | 33 | nan | nan | nan | Cerrado | nan |
| d03bc98c-e3c6-36bf-915c-44abda0436d0 | -4.6961 | -43.190201 | 2024-10-05 00:24:03 | METOP-C | CAXIAS | MARANHÃO | Brasil | 2103000 | 21 | 33 | nan | nan | nan | Cerrado | nan |
| 23bbf1c9-bf6e-3ffc-8553-9a12a4bfeec0 | -5.6882 | -47.374802 | 2024-10-05 00:24:03 | METOP-C | GOVERNADOR EDISON LOBÃO | MARANHÃO | Brasil | 2104552 | 21 | 33 | nan | nan | nan | Cerrado | nan |
| 080d23e3-c967-37f8-87d6-5bbd9d56b9a4 | -5.1485 | -45.2309 | 2024-10-05 00:24:04 | METOP-C | BARRA DO CORDA | MARANHÃO | Brasil | 2101608 | 21 | 33 | nan | nan | nan | Cerrado | nan |
| 25660c1c-0962-3b49-952e-a822b4c72cce | -5.1503 | -45.238701 | 2024-10-05 00:24:04 | METOP-C | BARRA DO CORDA | MARANHÃO | Brasil | 2101608 | 21 | 33 | nan | nan | nan | Cerrado | nan |
| c9c328b2-e08f-3ca7-8411-8dd384189761 | -5.3836 | -46.418098 | 2024-10-05 00:24:04 | METOP-C | AMARANTE DO MARANHÃO | MARANHÃO | Brasil | 2100600 | 21 | 33 | nan | nan | nan | Amazônia | nan |
| f4a63df2-20b8-3e8c-954a-5005ba430272 | -5.3856 | -46.427101 | 2024-10-05 00:24:04 | METOP-C | AMARANTE DO MARANHÃO | MARANHÃO | Brasil | 2100600 | 21 | 33 | nan | nan | nan | Amazônia | nan |
| cf37f443-5ef1-3243-b227-c60b969f3fe7 | -5.3718 | -46.411301 | 2024-10-05 00:24:04 | METOP-C | AMARANTE DO MARANHÃO | MARANHÃO | Brasil | 2100600 | 21 | 33 | nan | nan | nan | Amazônia | nan |
| 7586481f-8906-387c-9b42-d04f567451ed | -5.3738 | -46.4203 | 2024-10-05 00:24:04 | METOP-C | AMARANTE DO MARANHÃO | MARANHÃO | Brasil | 2100600 | 21 | 33 | nan | nan | nan | Amazônia | nan |
| 42e95691-a248-3fd3-b257-986cea7dd8c9 | -5.3758 | -46.429199 | 2024-10-05 00:24:04 | METOP-C | AMARANTE DO MARANHÃO | MARANHÃO | Brasil | 2100600 | 21 | 33 | nan | nan | nan | Amazônia | nan |
| a5c684e4-c1f5-3222-aceb-48863a73880d | -4.6847 | -43.185501 | 2024-10-05 00:24:04 | METOP-C | CAXIAS | MARANHÃO | Brasil | 2103000 | 21 | 33 | nan | nan | nan | Cerrado | nan |
| 2f1379f5-c649-3c72-a5a1-33fb168064e9 | -4.6863 | -43.192402 | 2024-10-05 00:24:04 | METOP-C | CAXIAS | MARANHÃO | Brasil | 2103000 | 21 | 33 | nan | nan | nan | Cerrado | nan |
| 97bcd6e7-6359-3830-8324-652a92b6cc04 | -4.7254 | -43.589298 | 2024-10-05 00:24:04 | METOP-C | CAXIAS | MARANHÃO | Brasil | 2103000 | 21 | 33 | nan | nan | nan | Cerrado | nan |
| 31159a1c-64c2-343e-80f4-b2d69a6ed6d8 | -4.4692 | -42.874199 | 2024-10-05 00:24:06 | METOP-C | CAXIAS | MARANHÃO | Brasil | 2103000 | 21 | 33 | nan | nan | nan | Cerrado | nan |
| 3e566e84-8a05-39bf-b277-20af990c3578 | -4.4594 | -42.8764 | 2024-10-05 00:24:06 | METOP-C | UNIÃO | PIAUÍ | Brasil | 2211100 | 22 | 33 | nan | nan | nan | Cerrado | nan |
| 82dc0075-5fd6-30aa-9cac-b3539a77a0ce | -4.461 | -42.883202 | 2024-10-05 00:24:06 | METOP-C | CAXIAS | MARANHÃO | Brasil | 2103000 | 21 | 33 | nan | nan | nan | Cerrado | nan |
| 345d5b72-2c85-3285-9523-5639e7864198 | -4.6589 | -43.750099 | 2024-10-05 00:24:06 | METOP-C | CODÓ | MARANHÃO | Brasil | 2103307 | 21 | 33 | nan | nan | nan | Cerrado | nan |
| 3496581f-471e-3b49-b009-6b3f8245167e | -4.6605 | -43.757099 | 2024-10-05 00:24:06 | METOP-C | CODÓ | MARANHÃO | Brasil | 2103307 | 21 | 33 | nan | nan | nan | Cerrado | nan |
| a5efa621-751c-3df3-9dfd-2aa5c39faa5d | -5.8186 | -49.1343 | 2024-10-05 00:24:07 | METOP-C | MARABÁ | PARÁ | Brasil | 1504208 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| b51c75b1-cb8a-3522-98de-08d00b33f759 | -5.8059 | -49.122898 | 2024-10-05 00:24:07 | METOP-C | MARABÁ | PARÁ | Brasil | 1504208 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| dff620c8-1bff-3e08-9228-e98173c661c4 | -5.8088 | -49.136398 | 2024-10-05 00:24:07 | METOP-C | MARABÁ | PARÁ | Brasil | 1504208 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| f61481c5-b8fb-3e97-ae69-25983e13a968 | -5.1213 | -46.1175 | 2024-10-05 00:24:07 | METOP-C | ARAME | MARANHÃO | Brasil | 2100956 | 21 | 33 | nan | nan | nan | Amazônia | nan |
| 2fa33e26-646b-347a-b2bd-7ff618a18ae2 | -3.7669 | -40.413502 | 2024-10-05 00:24:08 | METOP-C | SOBRAL | CEARÁ | Brasil | 2312908 | 23 | 33 | nan | nan | nan | Caatinga | nan |
| 186ec2f2-6c20-3bbf-a77d-946c3a6c3ce4 | -3.7687 | -40.4212 | 2024-10-05 00:24:08 | METOP-C | SOBRAL | CEARÁ | Brasil | 2312908 | 23 | 33 | nan | nan | nan | Caatinga | nan |
| 342820ea-308f-3796-bf90-2b9a513c826a | -3.759 | -40.4235 | 2024-10-05 00:24:08 | METOP-C | SOBRAL | CEARÁ | Brasil | 2312908 | 23 | 33 | nan | nan | nan | Caatinga | nan |
| 6738fb42-801d-3f1f-a19c-83ce5fc70d04 | -4.9188 | -45.672901 | 2024-10-05 00:24:09 | METOP-C | ARAME | MARANHÃO | Brasil | 2100956 | 21 | 33 | nan | nan | nan | Amazônia | nan |
| 58ba65ef-03a2-364a-89d1-88a6dd1beccd | -4.7835 | -45.2542 | 2024-10-05 00:24:10 | METOP-C | LAGO DA PEDRA | MARANHÃO | Brasil | 2105708 | 21 | 33 | nan | nan | nan | Cerrado | nan |
| 19b07d04-435b-3f72-89fe-2ae0192b9752 | -5.6457 | -49.698799 | 2024-10-05 00:24:12 | METOP-C | MARABÁ | PARÁ | Brasil | 1504208 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| 0ccfa4fd-81cb-3567-aec8-cbc13ffd25bc | -5.0432 | -47.147499 | 2024-10-05 00:24:12 | METOP-C | AÇAILÂNDIA | MARANHÃO | Brasil | 2100055 | 21 | 33 | nan | nan | nan | Amazônia | nan |
| 863ac68d-fae5-3fa9-afcc-c5de908cab32 | -5.0334 | -47.149601 | 2024-10-05 00:24:12 | METOP-C | AÇAILÂNDIA | MARANHÃO | Brasil | 2100055 | 21 | 33 | nan | nan | nan | Amazônia | nan |
| cd797a28-eb23-36bf-8396-2a9918137e6f | -3.7901 | -41.581001 | 2024-10-05 00:24:12 | METOP-C | PIRACURUCA | PIAUÍ | Brasil | 2208304 | 22 | 33 | nan | nan | nan | Caatinga | nan |
| 52ac547d-2150-3315-9b42-2415c2e48c45 | -3.7917 | -41.5881 | 2024-10-05 00:24:12 | METOP-C | PIRACURUCA | PIAUÍ | Brasil | 2208304 | 22 | 33 | nan | nan | nan | Caatinga | nan |
| 0cc77a13-ed2e-37c8-8681-207a2827ede9 | -3.7933 | -41.5952 | 2024-10-05 00:24:12 | METOP-C | PIRACURUCA | PIAUÍ | Brasil | 2208304 | 22 | 33 | nan | nan | nan | Caatinga | nan |
| c0c78e2f-e667-3c33-b93b-8abd6b2ca776 | -4.841 | -46.517601 | 2024-10-05 00:24:13 | METOP-C | BOM JESUS DAS SELVAS | MARANHÃO | Brasil | 2102036 | 21 | 33 | nan | nan | nan | Amazônia | nan |
| f1957983-3554-3d1b-b370-09eadc46a680 | -4.6855 | -45.869701 | 2024-10-05 00:24:13 | METOP-C | ARAME | MARANHÃO | Brasil | 2100956 | 21 | 33 | nan | nan | nan | Amazônia | nan |
| 0b07203b-c2f9-3f1d-b674-399e636da5c3 | -4.5924 | -45.592899 | 2024-10-05 00:24:14 | METOP-C | PAULO RAMOS | MARANHÃO | Brasil | 2108108 | 21 | 33 | nan | nan | nan | Cerrado | nan |
| d154a1a9-6a0d-34ca-8587-2f44dbb038c4 | -4.5942 | -45.600899 | 2024-10-05 00:24:14 | METOP-C | PAULO RAMOS | MARANHÃO | Brasil | 2108108 | 21 | 33 | nan | nan | nan | Cerrado | nan |
| 86be37ac-b810-3e00-8fee-9458d066b41d | -4.596 | -45.608799 | 2024-10-05 00:24:14 | METOP-C | MARAJÁ DO SENA | MARANHÃO | Brasil | 2106359 | 21 | 33 | nan | nan | nan | Cerrado | nan |
| e0d7adf0-47b8-3000-a8ea-7c18282a6d35 | -3.9959 | -43.238701 | 2024-10-05 00:24:15 | METOP-C | CHAPADINHA | MARANHÃO | Brasil | 2103208 | 21 | 33 | nan | nan | nan | Cerrado | nan |
| ce0d747d-849b-3f2e-8ee0-83afd9dfb1bf | -3.9975 | -43.245499 | 2024-10-05 00:24:15 | METOP-C | CHAPADINHA | MARANHÃO | Brasil | 2103208 | 21 | 33 | nan | nan | nan | Cerrado | nan |
| e6e30e6e-f60f-3c88-937b-8d42b429be39 | -3.9991 | -43.2523 | 2024-10-05 00:24:15 | METOP-C | CHAPADINHA | MARANHÃO | Brasil | 2103208 | 21 | 33 | nan | nan | nan | Cerrado | nan |
| 9f98aa4f-56ed-3b17-b785-d5932f52fdf2 | -3.9877 | -43.2477 | 2024-10-05 00:24:15 | METOP-C | CHAPADINHA | MARANHÃO | Brasil | 2103208 | 21 | 33 | nan | nan | nan | Cerrado | nan |
| 0aebccf8-c94f-36d4-81ae-5ff385fef76c | -3.9893 | -43.254501 | 2024-10-05 00:24:15 | METOP-C | CHAPADINHA | MARANHÃO | Brasil | 2103208 | 21 | 33 | nan | nan | nan | Cerrado | nan |
| 5508badb-b71a-3454-9d50-2b4e73e2e33f | -4.014 | -43.227402 | 2024-10-05 00:24:15 | METOP-C | CHAPADINHA | MARANHÃO | Brasil | 2103208 | 21 | 33 | nan | nan | nan | Cerrado | nan |
| f3fdb0ce-7eb1-384d-9c80-b9b2ef153998 | -4.0155 | -43.234299 | 2024-10-05 00:24:15 | METOP-C | CHAPADINHA | MARANHÃO | Brasil | 2103208 | 21 | 33 | nan | nan | nan | Cerrado | nan |
| 9573a043-07d0-3859-b652-0717c0b4746a | -4.0057 | -43.2365 | 2024-10-05 00:24:15 | METOP-C | CHAPADINHA | MARANHÃO | Brasil | 2103208 | 21 | 33 | nan | nan | nan | Cerrado | nan |
| 155ef538-c76f-348c-9cb3-72179b10bfda | -4.0073 | -43.243301 | 2024-10-05 00:24:15 | METOP-C | CHAPADINHA | MARANHÃO | Brasil | 2103208 | 21 | 33 | nan | nan | nan | Cerrado | nan |
| 6a84651d-abd7-3911-b758-ac654c57b06b | -4.0089 | -43.250099 | 2024-10-05 00:24:15 | METOP-C | CHAPADINHA | MARANHÃO | Brasil | 2103208 | 21 | 33 | nan | nan | nan | Cerrado | nan |
| 9b223ea0-0ad2-399b-ac69-5a5314b4d7b0 | -4.4081 | -45.369301 | 2024-10-05 00:24:16 | METOP-C | VITORINO FREIRE | MARANHÃO | Brasil | 2113009 | 21 | 33 | nan | nan | nan | Amazônia | nan |
| 20a56d42-f1c4-375a-b05a-b2cb527b91a8 | -4.4099 | -45.377102 | 2024-10-05 00:24:16 | METOP-C | VITORINO FREIRE | MARANHÃO | Brasil | 2113009 | 21 | 33 | nan | nan | nan | Amazônia | nan |
| 8087fc78-38b0-35fa-b7f5-c60b8f565f77 | -4.0441 | -44.307999 | 2024-10-05 00:24:18 | METOP-C | COROATÁ | MARANHÃO | Brasil | 2103604 | 21 | 33 | nan | nan | nan | Cerrado | nan |
| a2e667f1-24a3-32d0-af2e-3dc7bd7efc45 | -4.0457 | -44.315102 | 2024-10-05 00:24:18 | METOP-C | COROATÁ | MARANHÃO | Brasil | 2103604 | 21 | 33 | nan | nan | nan | Cerrado | nan |
| aaa72a6d-0829-38f7-8117-97fe88a8fb9b | -4.3807 | -46.297501 | 2024-10-05 00:24:20 | METOP-C | BURITICUPU | MARANHÃO | Brasil | 2102325 | 21 | 33 | nan | nan | nan | Amazônia | nan |
| 9c3c0c2a-8e05-35e3-aa0d-b71e877d1a95 | -4.3165 | -46.697899 | 2024-10-05 00:24:22 | METOP-C | BOM JARDIM | MARANHÃO | Brasil | 2102002 | 21 | 33 | nan | nan | nan | Amazônia | nan |
| 098b8b5d-6ec7-31dc-b757-331a8e5c9089 | -4.3185 | -46.706799 | 2024-10-05 00:24:22 | METOP-C | BOM JARDIM | MARANHÃO | Brasil | 2102002 | 21 | 33 | nan | nan | nan | Amazônia | nan |
| 666a9e98-4eab-3437-a0cd-45b711dbd5fd | -4.3205 | -46.715801 | 2024-10-05 00:24:22 | METOP-C | BOM JARDIM | MARANHÃO | Brasil | 2102002 | 21 | 33 | nan | nan | nan | Amazônia | nan |
| 3a62c8e8-9b38-3655-bb2b-ec48fadc90f8 | -3.4663 | -43.356899 | 2024-10-05 00:24:24 | METOP-C | URBANO SANTOS | MARANHÃO | Brasil | 2112605 | 21 | 33 | nan | nan | nan | Cerrado | nan |
| 1091f322-e59d-3701-95db-26b259861170 | -4.1585 | -46.817699 | 2024-10-05 00:24:25 | METOP-C | BOM JARDIM | MARANHÃO | Brasil | 2102002 | 21 | 33 | nan | nan | nan | Amazônia | nan |
| 5b961980-b87e-3eaa-bebc-6acbc67feaca | -4.1605 | -46.826801 | 2024-10-05 00:24:25 | METOP-C | BOM JARDIM | MARANHÃO | Brasil | 2102002 | 21 | 33 | nan | nan | nan | Amazônia | nan |
| 49df6402-3e80-37ad-aec9-9ff2fa4bb2ee | -3.2118 | -42.696499 | 2024-10-05 00:24:26 | METOP-C | SANTANA DO MARANHÃO | MARANHÃO | Brasil | 2110237 | 21 | 33 | nan | nan | nan | Cerrado | nan |
| 5ff7df9d-c985-3dcd-90d6-ed563fcd91f9 | -4.1487 | -46.819801 | 2024-10-05 00:24:26 | METOP-C | BOM JARDIM | MARANHÃO | Brasil | 2102002 | 21 | 33 | nan | nan | nan | Amazônia | nan |
| 9b2b7a4c-f026-37b7-8bfa-712044c8e697 | -4.1507 | -46.828899 | 2024-10-05 00:24:26 | METOP-C | BOM JARDIM | MARANHÃO | Brasil | 2102002 | 21 | 33 | nan | nan | nan | Amazônia | nan |
| 0567e64f-7312-3d70-9146-753be411955b | -4.3038 | -47.695999 | 2024-10-05 00:24:26 | METOP-C | DOM ELISEU | PARÁ | Brasil | 1502939 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| 8e102959-81d9-3109-a82a-463aa4d23978 | -4.3061 | -47.706299 | 2024-10-05 00:24:26 | METOP-C | DOM ELISEU | PARÁ | Brasil | 1502939 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| f90981dd-94ce-3e7d-bd09-639a6016029f | -4.2329 | -47.562199 | 2024-10-05 00:24:27 | METOP-C | DOM ELISEU | PARÁ | Brasil | 1502939 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| 157273d8-ec12-359b-b0d8-0489d34534a2 | -4.6552 | -49.510399 | 2024-10-05 00:24:27 | METOP-C | NOVO REPARTIMENTO | PARÁ | Brasil | 1505064 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| 6ccb5bda-2b54-308e-954e-87fc13e9a0c7 | -4.6455 | -49.512501 | 2024-10-05 00:24:27 | METOP-C | NOVO REPARTIMENTO | PARÁ | Brasil | 1505064 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| c528b15d-02bc-3952-874d-048647eb73d4 | -4.6485 | -49.526199 | 2024-10-05 00:24:27 | METOP-C | NOVO REPARTIMENTO | PARÁ | Brasil | 1505064 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| ebcf6674-d2a6-3822-a870-885d23679632 | -3.9163 | -46.426201 | 2024-10-05 00:24:28 | METOP-C | BOM JARDIM | MARANHÃO | Brasil | 2102002 | 21 | 33 | nan | nan | nan | Amazônia | nan |
| 6eaf0a28-4aec-3e76-b797-035ab8f966ed | -3.9183 | -46.434799 | 2024-10-05 00:24:28 | METOP-C | BOM JARDIM | MARANHÃO | Brasil | 2102002 | 21 | 33 | nan | nan | nan | Amazônia | nan |
| b2a182ca-b540-31de-81a8-3957a5cb1c29 | -4.0816 | -47.940899 | 2024-10-05 00:24:31 | METOP-C | DOM ELISEU | PARÁ | Brasil | 1502939 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| 255c3418-344a-3fac-ada8-e4ddb898773e | -4.084 | -47.9515 | 2024-10-05 00:24:31 | METOP-C | DOM ELISEU | PARÁ | Brasil | 1502939 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| 226dc50d-4544-3387-a2cb-0fe6c022a990 | -4.0694 | -47.932499 | 2024-10-05 00:24:31 | METOP-C | DOM ELISEU | PARÁ | Brasil | 1502939 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| e89a29ed-72be-37ab-96e7-1ef189a40b6f | -4.0718 | -47.943001 | 2024-10-05 00:24:31 | METOP-C | DOM ELISEU | PARÁ | Brasil | 1502939 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| f11d8bb3-a16b-3d97-aea1-950df6c6e081 | -4.0742 | -47.953602 | 2024-10-05 00:24:31 | METOP-C | DOM ELISEU | PARÁ | Brasil | 1502939 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| b256abfb-abdb-30bb-9f2c-a4195afaa876 | -4.0596 | -47.934601 | 2024-10-05 00:24:31 | METOP-C | DOM ELISEU | PARÁ | Brasil | 1502939 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| 3c4db366-4bf5-307e-9d05-88e4baf5bec8 | -4.062 | -47.945099 | 2024-10-05 00:24:31 | METOP-C | DOM ELISEU | PARÁ | Brasil | 1502939 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| dee123f7-7955-3507-b0d2-2f4e57cef6f1 | -4.0644 | -47.9557 | 2024-10-05 00:24:31 | METOP-C | DOM ELISEU | PARÁ | Brasil | 1502939 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| c855626e-f683-3161-a281-80711a99ac5d | -3.3882 | -45.273602 | 2024-10-05 00:24:32 | METOP-C | MONÇÃO | MARANHÃO | Brasil | 2106904 | 21 | 33 | nan | nan | nan | Amazônia | nan |
| 6e8bdb74-1724-3f97-b063-edcbbf0fada0 | -3.3899 | -45.281101 | 2024-10-05 00:24:32 | METOP-C | MONÇÃO | MARANHÃO | Brasil | 2106904 | 21 | 33 | nan | nan | nan | Amazônia | nan |
| 2f3081e7-2615-3d07-9f18-b24adcf016b8 | -3.6155 | -47.509399 | 2024-10-05 00:24:37 | METOP-C | ULIANÓPOLIS | PARÁ | Brasil | 1508126 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| e6c2b9be-a047-3fae-9b77-19c0cfa44868 | -3.6177 | -47.519199 | 2024-10-05 00:24:37 | METOP-C | ULIANÓPOLIS | PARÁ | Brasil | 1508126 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| 78cda34a-8bdc-3238-b48c-da7d90cb5451 | -3.6036 | -47.501801 | 2024-10-05 00:24:37 | METOP-C | ULIANÓPOLIS | PARÁ | Brasil | 1508126 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| 1b1d7b8d-9ae9-344d-8bb1-b61e962e7038 | -3.6057 | -47.511501 | 2024-10-05 00:24:37 | METOP-C | ULIANÓPOLIS | PARÁ | Brasil | 1508126 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| cb40983e-7ba4-355d-8c37-f38b70767156 | -3.6079 | -47.521301 | 2024-10-05 00:24:37 | METOP-C | ULIANÓPOLIS | PARÁ | Brasil | 1508126 | 15 | 33 | nan | nan | nan | Amazônia | nan |


[Clique aqui para ver as próximas entradas](README10.md)
