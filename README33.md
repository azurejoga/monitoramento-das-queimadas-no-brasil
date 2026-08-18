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

## Dados Diários - Página 33

| ID | Latitude | Longitude | Data/Hora GMT | Satélite | Município | Estado | País | Município ID | Estado ID | País ID | Dias sem Chuva | Precipitação | Risco de Fogo | Bioma | FRP |
|----|----------|-----------|---------------|----------|-----------|--------|------|--------------|-----------|---------|----------------|--------------|----------------|-------|-----|
| f31d8328-41d5-3f56-a4d7-7eaa0aa3ddda | -11.1178 | -47.2654 | 2026-08-18 04:50:00 | GOES-19 | ALMAS | TOCANTINS | Brasil | 1700400 | 17 | 33 | nan | nan | nan | Cerrado | 46.6 |
| c1123680-8f83-3627-ac88-bb04105cefab | -14.8233 | -46.619 | 2026-08-18 04:50:00 | GOES-19 | FLORES DE GOIÁS | GOIÁS | Brasil | 5207907 | 52 | 33 | nan | nan | nan | Cerrado | 69.3 |
| 0af1b642-cc1e-36a5-bf9b-924e2a8755bd | -6.7478 | -59.1716 | 2026-08-18 04:50:00 | GOES-19 | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 76.1 |
| 20d5662b-6968-329d-a3e2-6639910918dd | -6.841 | -59.0132 | 2026-08-18 04:50:00 | GOES-19 | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 38.8 |
| dd88cef1-e8b7-30a0-b6f8-5c584b7984cc | -6.748 | -59.1523 | 2026-08-18 04:50:00 | GOES-19 | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 38.5 |
| 945cac87-2488-3296-b57d-2b94895ba8dd | -14.8228 | -46.6419 | 2026-08-18 04:50:00 | GOES-19 | FLORES DE GOIÁS | GOIÁS | Brasil | 5207907 | 52 | 33 | nan | nan | nan | Cerrado | 91.6 |
| c0fcc20c-0361-3ba2-99cd-68fb4b43b370 | -14.8033 | -46.6453 | 2026-08-18 04:50:00 | GOES-19 | FLORES DE GOIÁS | GOIÁS | Brasil | 5207907 | 52 | 33 | nan | nan | nan | Cerrado | 87.2 |
| e22bc7c8-45a3-3847-8fa4-e9de7f912f2c | 2.15831 | -50.72319 | 2026-08-18 04:53:00 | NOAA-20 | CALÇOENE | AMAPÁ | Brasil | 1600204 | 16 | 33 | nan | nan | nan | Amazônia | 3.0 |
| a0c4c935-9088-37e9-95cc-d46516e88eb3 | 2.15777 | -50.71976 | 2026-08-18 04:53:00 | NOAA-20 | CALÇOENE | AMAPÁ | Brasil | 1600204 | 16 | 33 | nan | nan | nan | Amazônia | 2.8 |
| 4ec0283c-7650-3214-be30-b9af8dd0e7fe | 2.11112 | -50.96301 | 2026-08-18 04:53:00 | NOAA-20 | AMAPÁ | AMAPÁ | Brasil | 1600105 | 16 | 33 | nan | nan | nan | Amazônia | 1.3 |
| 1ebfa562-e5f2-3b0a-bbce-c20f40c2e2cb | -6.52969 | -43.12614 | 2026-08-18 04:55:00 | NOAA-20 | BARÃO DE GRAJAÚ | MARANHÃO | Brasil | 2101509 | 21 | 33 | nan | nan | nan | Cerrado | 3.4 |
| 054e22ff-e30f-347e-9845-6c8231328867 | -3.26495 | -49.52276 | 2026-08-18 04:55:00 | NOAA-20 | BAIÃO | PARÁ | Brasil | 1501204 | 15 | 33 | nan | nan | nan | Amazônia | 2.3 |
| a479e1bc-9941-389c-8cf0-8299f4b356d8 | -4.96917 | -42.2177 | 2026-08-18 04:55:00 | NOAA-20 | CAMPO MAIOR | PIAUÍ | Brasil | 2202208 | 22 | 33 | nan | nan | nan | Caatinga | 2.1 |
| 9b6f3394-344a-361b-a17e-678d26e89455 | -2.49951 | -48.13938 | 2026-08-18 04:55:00 | NOAA-20 | TOMÉ-AÇU | PARÁ | Brasil | 1508001 | 15 | 33 | nan | nan | nan | Amazônia | 2.4 |
| 892d3415-5d82-33ca-8622-5005125a7344 | -2.32356 | -60.06565 | 2026-08-18 04:55:00 | NOAA-20 | MANAUS | AMAZONAS | Brasil | 1302603 | 13 | 33 | nan | nan | nan | Amazônia | 1.1 |
| ae587b5b-9bc4-3626-9d03-049d92637629 | -5.26768 | -49.05112 | 2026-08-18 04:55:00 | NOAA-20 | MARABÁ | PARÁ | Brasil | 1504208 | 15 | 33 | nan | nan | nan | Amazônia | 1.8 |
| 82f72e65-ac18-37ea-9c2e-c5dd2f8e3661 | -6.53174 | -43.11174 | 2026-08-18 04:55:00 | NOAA-20 | BARÃO DE GRAJAÚ | MARANHÃO | Brasil | 2101509 | 21 | 33 | nan | nan | nan | Cerrado | 3.1 |
| 501be318-4443-3817-83b3-77250099af8c | -5.57322 | -47.45026 | 2026-08-18 04:55:00 | NOAA-20 | IMPERATRIZ | MARANHÃO | Brasil | 2105302 | 21 | 33 | nan | nan | nan | Cerrado | 1.5 |
| d594b76b-6409-3115-afd4-fddfcc7b1adf | -6.27133 | -43.28054 | 2026-08-18 04:55:00 | NOAA-20 | SÃO FRANCISCO DO MARANHÃO | MARANHÃO | Brasil | 2110906 | 21 | 33 | nan | nan | nan | Cerrado | 2.5 |
| e274ecb5-aac7-37d8-961b-4f79e3db3a64 | -4.49356 | -42.56522 | 2026-08-18 04:55:00 | NOAA-20 | LAGOA ALEGRE | PIAUÍ | Brasil | 2205557 | 22 | 33 | nan | nan | nan | Caatinga | 1.2 |
| 5dcb0504-a955-3c9c-b7c9-a76670f9e597 | -4.53007 | -42.93307 | 2026-08-18 04:55:00 | NOAA-20 | CAXIAS | MARANHÃO | Brasil | 2103000 | 21 | 33 | nan | nan | nan | Cerrado | 1.6 |
| 9531868d-c175-3979-b748-b217963791fb | -6.17995 | -47.78294 | 2026-08-18 04:55:00 | NOAA-20 | LUZINÓPOLIS | TOCANTINS | Brasil | 1712454 | 17 | 33 | nan | nan | nan | Cerrado | 1.5 |
| 3ed7ae94-857f-318b-9760-14e6d615e4cc | -2.70734 | -54.22524 | 2026-08-18 04:55:00 | NOAA-20 | SANTARÉM | PARÁ | Brasil | 1506807 | 15 | 33 | nan | nan | nan | Amazônia | 1.2 |
| f0644721-e344-321f-95a9-81be7c7e6382 | -4.71788 | -42.7686 | 2026-08-18 04:55:00 | NOAA-20 | UNIÃO | PIAUÍ | Brasil | 2211100 | 22 | 33 | nan | nan | nan | Cerrado | 1.7 |
| 80247b80-2ff9-3826-a50a-cb4d87e2bc14 | -1.39721 | -50.73635 | 2026-08-18 04:55:00 | NOAA-20 | BREVES | PARÁ | Brasil | 1501808 | 15 | 33 | nan | nan | nan | Amazônia | 0.8 |
| d5fc4535-8019-346c-8b91-82eeb6531378 | -3.42482 | -51.51607 | 2026-08-18 04:55:00 | NOAA-20 | ANAPU | PARÁ | Brasil | 1500859 | 15 | 33 | nan | nan | nan | Amazônia | 2.1 |
| 81e08ee2-c252-306b-ac91-11ab002280f7 | -6.16702 | -47.75973 | 2026-08-18 04:55:00 | NOAA-20 | LUZINÓPOLIS | TOCANTINS | Brasil | 1712454 | 17 | 33 | nan | nan | nan | Cerrado | 0.7 |
| 5c5b8b3d-80c5-3bae-9dbb-843ffd81589a | -3.68653 | -47.6486 | 2026-08-18 04:55:00 | NOAA-20 | ULIANÓPOLIS | PARÁ | Brasil | 1508126 | 15 | 33 | nan | nan | nan | Amazônia | 6.0 |
| 7740ec8e-bec8-365c-853f-4989ffe2b14d | -3.20688 | -49.05648 | 2026-08-18 04:55:00 | NOAA-20 | MOJU | PARÁ | Brasil | 1504703 | 15 | 33 | nan | nan | nan | Amazônia | 1.1 |
| dfab985a-5a84-3e13-b56d-bee26ceaabd6 | -6.15829 | -47.79042 | 2026-08-18 04:55:00 | NOAA-20 | LUZINÓPOLIS | TOCANTINS | Brasil | 1712454 | 17 | 33 | nan | nan | nan | Cerrado | 1.6 |
| 2845f096-1a26-39d6-afd3-ff778e554e18 | 0.49631 | -60.5915 | 2026-08-18 04:55:00 | NOAA-20 | RORAINÓPOLIS | RORAIMA | Brasil | 1400472 | 14 | 33 | nan | nan | nan | Amazônia | 0.6 |
| 7d27f228-d0f6-3e5a-ac02-ac266b5968af | -4.4885 | -42.56069 | 2026-08-18 04:55:00 | NOAA-20 | LAGOA ALEGRE | PIAUÍ | Brasil | 2205557 | 22 | 33 | nan | nan | nan | Caatinga | 1.2 |
| c2488620-de01-3386-af8f-bd0319d21d8a | -4.9706 | -42.21296 | 2026-08-18 04:55:00 | NOAA-20 | CAMPO MAIOR | PIAUÍ | Brasil | 2202208 | 22 | 33 | nan | nan | nan | Caatinga | 2.4 |
| 02a60d78-c679-3d73-9499-7fa93abc8665 | -6.53501 | -43.12263 | 2026-08-18 04:55:00 | NOAA-20 | BARÃO DE GRAJAÚ | MARANHÃO | Brasil | 2101509 | 21 | 33 | nan | nan | nan | Cerrado | 4.9 |
| 18dc8b00-0488-3d15-950f-836da8ab269e | -3.50273 | -48.03477 | 2026-08-18 04:55:00 | NOAA-20 | PARAGOMINAS | PARÁ | Brasil | 1505502 | 15 | 33 | nan | nan | nan | Amazônia | 1.9 |
| 1978d1ea-ce42-336a-92fc-cdfb705de2d0 | -4.32007 | -49.99421 | 2026-08-18 04:55:00 | NOAA-20 | NOVO REPARTIMENTO | PARÁ | Brasil | 1505064 | 15 | 33 | nan | nan | nan | Amazônia | 0.8 |
| beb5c14f-9c7c-3b45-8bec-c0fa40e7b2ed | -5.56915 | -47.44967 | 2026-08-18 04:55:00 | NOAA-20 | IMPERATRIZ | MARANHÃO | Brasil | 2105302 | 21 | 33 | nan | nan | nan | Cerrado | 1.5 |
| 0dfea953-f47b-3113-afa9-b6d255448c4c | -2.49965 | -56.07605 | 2026-08-18 04:55:00 | NOAA-20 | JURUTI | PARÁ | Brasil | 1503903 | 15 | 33 | nan | nan | nan | Amazônia | 1.0 |
| 3ff1b385-4aa7-363a-b63e-2bdfe53e929d | -6.17942 | -47.78642 | 2026-08-18 04:55:00 | NOAA-20 | LUZINÓPOLIS | TOCANTINS | Brasil | 1712454 | 17 | 33 | nan | nan | nan | Cerrado | 1.5 |
| 2b8c9025-ab32-3822-8215-904ef208de79 | -6.52945 | -43.12188 | 2026-08-18 04:55:00 | NOAA-20 | BARÃO DE GRAJAÚ | MARANHÃO | Brasil | 2101509 | 21 | 33 | nan | nan | nan | Cerrado | 1.5 |
| 81926610-57ad-3492-9e17-a91ba11851a1 | -3.50653 | -48.03541 | 2026-08-18 04:55:00 | NOAA-20 | PARAGOMINAS | PARÁ | Brasil | 1505502 | 15 | 33 | nan | nan | nan | Amazônia | 2.7 |
| 17aab064-38cd-349f-a2f4-2ec78e1b6658 | -4.53552 | -42.93391 | 2026-08-18 04:55:00 | NOAA-20 | CAXIAS | MARANHÃO | Brasil | 2103000 | 21 | 33 | nan | nan | nan | Cerrado | 1.8 |
| 7b90530e-b314-3268-90d1-f7eaf33926e3 | -6.53679 | -43.11608 | 2026-08-18 04:55:00 | NOAA-20 | BARÃO DE GRAJAÚ | MARANHÃO | Brasil | 2101509 | 21 | 33 | nan | nan | nan | Cerrado | 2.1 |
| 3a029b7b-8afe-32c4-a057-a4f24a314824 | -6.16127 | -47.79792 | 2026-08-18 04:55:00 | NOAA-20 | LUZINÓPOLIS | TOCANTINS | Brasil | 1712454 | 17 | 33 | nan | nan | nan | Cerrado | 1.7 |
| dd07a08f-2720-3d31-a4d5-680d0b610a41 | -4.01511 | -48.90623 | 2026-08-18 04:55:00 | NOAA-20 | GOIANÉSIA DO PARÁ | PARÁ | Brasil | 1503093 | 15 | 33 | nan | nan | nan | Amazônia | 17.4 |
| 70001f3f-0648-39cd-9ce8-8cf0816d2534 | -3.26434 | -49.52666 | 2026-08-18 04:55:00 | NOAA-20 | BAIÃO | PARÁ | Brasil | 1501204 | 15 | 33 | nan | nan | nan | Amazônia | 1.8 |
| 7a55e404-3bd4-3f88-920d-0cc34f731206 | -6.1803 | -47.81888 | 2026-08-18 04:55:00 | NOAA-20 | LUZINÓPOLIS | TOCANTINS | Brasil | 1712454 | 17 | 33 | nan | nan | nan | Cerrado | 6.0 |
| fc831b90-b5ce-3d35-9581-645731eda89b | -4.49012 | -42.56152 | 2026-08-18 04:55:00 | NOAA-20 | LAGOA ALEGRE | PIAUÍ | Brasil | 2205557 | 22 | 33 | nan | nan | nan | Caatinga | 1.2 |
| 1d28789d-1523-3f83-b400-38634887398e | -2.87782 | -48.85527 | 2026-08-18 04:55:00 | NOAA-20 | TAILÂNDIA | PARÁ | Brasil | 1507953 | 15 | 33 | nan | nan | nan | Amazônia | 3.8 |
| d842bfe3-e890-3fa9-8ebe-5862c6f26a22 | -4.48956 | -42.56521 | 2026-08-18 04:55:00 | NOAA-20 | LAGOA ALEGRE | PIAUÍ | Brasil | 2205557 | 22 | 33 | nan | nan | nan | Caatinga | 1.2 |
| 431b3358-5dc7-3637-b4ba-01924ab9799f | -6.27182 | -43.27708 | 2026-08-18 04:55:00 | NOAA-20 | SÃO FRANCISCO DO MARANHÃO | MARANHÃO | Brasil | 2110906 | 21 | 33 | nan | nan | nan | Cerrado | 2.5 |
| c972b06c-6a2f-3c2c-8c07-c36e44f9e131 | -3.21047 | -49.05705 | 2026-08-18 04:55:00 | NOAA-20 | MOJU | PARÁ | Brasil | 1504703 | 15 | 33 | nan | nan | nan | Amazônia | 1.6 |
| 31451b09-4df5-34f6-9cbe-cb43ce64aff5 | -4.49409 | -42.56152 | 2026-08-18 04:55:00 | NOAA-20 | LAGOA ALEGRE | PIAUÍ | Brasil | 2205557 | 22 | 33 | nan | nan | nan | Caatinga | 1.2 |
| 1edb00e1-c161-3a9e-ae48-c9e76b5bda1c | -4.48345 | -42.55606 | 2026-08-18 04:55:00 | NOAA-20 | LAGOA ALEGRE | PIAUÍ | Brasil | 2205557 | 22 | 33 | nan | nan | nan | Caatinga | 1.0 |
| 64d7e54c-5ea8-3b6f-b13f-fd1fc9887ddb | -3.46158 | -56.80384 | 2026-08-18 04:55:00 | NOAA-20 | AVEIRO | PARÁ | Brasil | 1501006 | 15 | 33 | nan | nan | nan | Amazônia | 1.3 |
| f9ba1569-da2e-3896-984f-07e80b39b505 | -6.53452 | -43.12625 | 2026-08-18 04:55:00 | NOAA-20 | BARÃO DE GRAJAÚ | MARANHÃO | Brasil | 2101509 | 21 | 33 | nan | nan | nan | Cerrado | 4.9 |
| e019a198-c133-3502-8fcb-3c734495b41f | -2.30685 | -48.63326 | 2026-08-18 04:55:00 | NOAA-20 | ACARÁ | PARÁ | Brasil | 1500206 | 15 | 33 | nan | nan | nan | Amazônia | 0.9 |
| eec9fafc-3387-3b52-bac2-c0b1b8eddef8 | -5.32036 | -50.94831 | 2026-08-18 04:55:00 | NOAA-20 | SÃO FÉLIX DO XINGU | PARÁ | Brasil | 1507300 | 15 | 33 | nan | nan | nan | Amazônia | 0.4 |
| d09e254e-48b1-3a05-8dd9-2102d194920e | -6.18533 | -47.81249 | 2026-08-18 04:55:00 | NOAA-20 | LUZINÓPOLIS | TOCANTINS | Brasil | 1712454 | 17 | 33 | nan | nan | nan | Cerrado | 2.4 |
| ee2d9cec-2511-3f17-a09c-fd24472bc130 | -6.1792 | -47.81487 | 2026-08-18 04:55:00 | NOAA-20 | LUZINÓPOLIS | TOCANTINS | Brasil | 1712454 | 17 | 33 | nan | nan | nan | Cerrado | 2.3 |
| 88a4ccae-09cf-3deb-888d-c45fce6ea9cd | -3.4607 | -56.80613 | 2026-08-18 04:55:00 | NOAA-20 | AVEIRO | PARÁ | Brasil | 1501006 | 15 | 33 | nan | nan | nan | Amazônia | 2.2 |
| 6b26ef36-3340-3a5d-8d2e-4c4dfe79d2ae | -6.52896 | -43.12549 | 2026-08-18 04:55:00 | NOAA-20 | BARÃO DE GRAJAÚ | MARANHÃO | Brasil | 2101509 | 21 | 33 | nan | nan | nan | Cerrado | 1.5 |
| 0ad5d518-bf0b-30cb-9984-c53e82ea9b52 | -6.53627 | -43.11966 | 2026-08-18 04:55:00 | NOAA-20 | BARÃO DE GRAJAÚ | MARANHÃO | Brasil | 2101509 | 21 | 33 | nan | nan | nan | Cerrado | 2.1 |
| 9cb17641-c259-3f7a-a832-f46c3480f976 | -2.50028 | -56.0782 | 2026-08-18 04:55:00 | NOAA-20 | JURUTI | PARÁ | Brasil | 1503903 | 15 | 33 | nan | nan | nan | Amazônia | 1.6 |
| a3c947c1-d6b9-3fff-8e20-1828b407acb7 | -3.51033 | -48.03603 | 2026-08-18 04:55:00 | NOAA-20 | PARAGOMINAS | PARÁ | Brasil | 1505502 | 15 | 33 | nan | nan | nan | Amazônia | 2.7 |
| 2812f29a-ae62-3443-8a6c-08583c1bc977 | -3.42869 | -51.51313 | 2026-08-18 04:55:00 | NOAA-20 | ANAPU | PARÁ | Brasil | 1500859 | 15 | 33 | nan | nan | nan | Amazônia | 3.2 |
| e4ac80c0-112d-3981-be42-76c7c58c32c2 | -6.53092 | -43.11106 | 2026-08-18 04:55:00 | NOAA-20 | BARÃO DE GRAJAÚ | MARANHÃO | Brasil | 2101509 | 21 | 33 | nan | nan | nan | Cerrado | 2.4 |
| b3fc3aa3-a0a6-37ee-ad60-8334024acfeb | 0.49802 | -60.5915 | 2026-08-18 04:55:00 | NOAA-20 | RORAINÓPOLIS | RORAIMA | Brasil | 1400472 | 14 | 33 | nan | nan | nan | Amazônia | 0.6 |
| abcdc75b-c09b-3586-939d-edc406343e69 | -4.53072 | -42.93745 | 2026-08-18 04:55:00 | NOAA-20 | CAXIAS | MARANHÃO | Brasil | 2103000 | 21 | 33 | nan | nan | nan | Cerrado | 1.3 |
| dc0570d7-9e4a-303e-8b29-2578927a5cf3 | -6.1752 | -47.81421 | 2026-08-18 04:55:00 | NOAA-20 | LUZINÓPOLIS | TOCANTINS | Brasil | 1712454 | 17 | 33 | nan | nan | nan | Cerrado | 2.5 |
| 5231d13d-1b2e-3b3c-bfee-ce6657ab23fa | -2.57955 | -49.44167 | 2026-08-18 04:55:00 | NOAA-20 | MOCAJUBA | PARÁ | Brasil | 1504604 | 15 | 33 | nan | nan | nan | Amazônia | 1.3 |
| 1b96d699-894c-32a7-a013-be9f1d3ba793 | -3.67871 | -47.64743 | 2026-08-18 04:55:00 | NOAA-20 | ULIANÓPOLIS | PARÁ | Brasil | 1508126 | 15 | 33 | nan | nan | nan | Amazônia | 2.1 |
| 2b3dea2c-33b5-3d17-8e3f-477dad2ce3cf | -3.67796 | -47.65232 | 2026-08-18 04:55:00 | NOAA-20 | ULIANÓPOLIS | PARÁ | Brasil | 1508126 | 15 | 33 | nan | nan | nan | Amazônia | 2.1 |
| aeeba7cd-33c1-39d6-b3c6-a6826dc310ba | -6.1808 | -47.81544 | 2026-08-18 04:55:00 | NOAA-20 | LUZINÓPOLIS | TOCANTINS | Brasil | 1712454 | 17 | 33 | nan | nan | nan | Cerrado | 2.4 |
| bac1d5ab-2e56-340a-b5c9-4d9998fc4648 | -3.81739 | -50.63387 | 2026-08-18 04:55:00 | NOAA-20 | PACAJÁ | PARÁ | Brasil | 1505486 | 15 | 33 | nan | nan | nan | Amazônia | 0.8 |
| 7b0fdf70-0c47-36db-8f11-9d578d8ce2e5 | -6.53524 | -43.12689 | 2026-08-18 04:55:00 | NOAA-20 | BARÃO DE GRAJAÚ | MARANHÃO | Brasil | 2101509 | 21 | 33 | nan | nan | nan | Cerrado | 3.4 |
| 18572794-52bf-3c09-a8ab-12728cda7e82 | -2.79161 | -49.52073 | 2026-08-18 04:55:00 | NOAA-20 | BAIÃO | PARÁ | Brasil | 1501204 | 15 | 33 | nan | nan | nan | Amazônia | 0.6 |
| 6a54e1dc-a172-3042-b2a4-b3ee7664a6ff | -4.53173 | -42.93032 | 2026-08-18 04:55:00 | NOAA-20 | CAXIAS | MARANHÃO | Brasil | 2103000 | 21 | 33 | nan | nan | nan | Cerrado | 1.2 |
| a6ad24ca-5d44-3240-9967-e329b7c1f63d | -2.50347 | -56.07663 | 2026-08-18 04:55:00 | NOAA-20 | JURUTI | PARÁ | Brasil | 1503903 | 15 | 33 | nan | nan | nan | Amazônia | 1.0 |
| 2a003ba8-42ba-371e-a162-e642dac97f55 | 0.49311 | -60.59574 | 2026-08-18 04:55:00 | NOAA-20 | RORAINÓPOLIS | RORAIMA | Brasil | 1400472 | 14 | 33 | nan | nan | nan | Amazônia | 0.6 |
| 881ed174-2498-3189-a0fd-20aecf7653d4 | -6.53042 | -43.1147 | 2026-08-18 04:55:00 | NOAA-20 | BARÃO DE GRAJAÚ | MARANHÃO | Brasil | 2101509 | 21 | 33 | nan | nan | nan | Cerrado | 1.5 |
| 751144fd-b044-3387-9177-5f117fd6e0d3 | -4.20544 | -59.99328 | 2026-08-18 04:55:00 | NOAA-20 | AUTAZES | AMAZONAS | Brasil | 1300300 | 13 | 33 | nan | nan | nan | Amazônia | 2.9 |
| 19b67984-802b-32f1-a6ad-aa6951d68af2 | -4.48509 | -42.55692 | 2026-08-18 04:55:00 | NOAA-20 | LAGOA ALEGRE | PIAUÍ | Brasil | 2205557 | 22 | 33 | nan | nan | nan | Caatinga | 3.8 |
| 6ab8042e-f394-35b5-a4cf-bbf6678c6a4d | -4.71734 | -42.77234 | 2026-08-18 04:55:00 | NOAA-20 | UNIÃO | PIAUÍ | Brasil | 2211100 | 22 | 33 | nan | nan | nan | Cerrado | 1.2 |
| 52213e76-9d94-30e0-845a-5bed3565e8ff | -3.68262 | -47.64803 | 2026-08-18 04:55:00 | NOAA-20 | ULIANÓPOLIS | PARÁ | Brasil | 1508126 | 15 | 33 | nan | nan | nan | Amazônia | 6.0 |
| 3d8ada69-2a2b-36e6-8605-d44e12a7876f | -3.85647 | -54.08118 | 2026-08-18 04:55:00 | NOAA-20 | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | 0.7 |
| 3e4620c3-e4e5-34ae-a3f7-a4c38c4705cd | -6.30632 | -47.89124 | 2026-08-18 04:55:00 | NOAA-20 | NAZARÉ | TOCANTINS | Brasil | 1714302 | 17 | 33 | nan | nan | nan | Cerrado | 1.7 |
| 6fa84d05-b5d7-3513-b585-34b6b44a7ceb | -6.17868 | -47.81829 | 2026-08-18 04:55:00 | NOAA-20 | LUZINÓPOLIS | TOCANTINS | Brasil | 1712454 | 17 | 33 | nan | nan | nan | Cerrado | 4.2 |
| 941d23e2-5c0a-36c9-8274-58a39090dd1a | -5.26834 | -49.0468 | 2026-08-18 04:55:00 | NOAA-20 | MARABÁ | PARÁ | Brasil | 1504208 | 15 | 33 | nan | nan | nan | Amazônia | 1.8 |
| 228fc9c0-d6d8-3856-8d83-a8cb33d07ca3 | -6.26636 | -43.27624 | 2026-08-18 04:55:00 | NOAA-20 | SÃO FRANCISCO DO MARANHÃO | MARANHÃO | Brasil | 2110906 | 21 | 33 | nan | nan | nan | Cerrado | 3.4 |
| 88188670-47db-36d5-a82b-0bcca914aa3b | -3.68187 | -47.65291 | 2026-08-18 04:55:00 | NOAA-20 | ULIANÓPOLIS | PARÁ | Brasil | 1508126 | 15 | 33 | nan | nan | nan | Amazônia | 6.0 |
| 1468fcb3-6a0e-3a03-9f32-f233917e567c | -6.53071 | -43.11895 | 2026-08-18 04:55:00 | NOAA-20 | BARÃO DE GRAJAÚ | MARANHÃO | Brasil | 2101509 | 21 | 33 | nan | nan | nan | Cerrado | 2.1 |
| 32038d16-2d4d-3257-821a-1d6b2915cd38 | -4.32824 | -48.71504 | 2026-08-18 04:55:00 | NOAA-20 | RONDON DO PARÁ | PARÁ | Brasil | 1506187 | 15 | 33 | nan | nan | nan | Amazônia | 2.1 |
| 174d4965-da62-3c91-8b56-df674aa7fbc5 | -4.53123 | -42.93389 | 2026-08-18 04:55:00 | NOAA-20 | CAXIAS | MARANHÃO | Brasil | 2103000 | 21 | 33 | nan | nan | nan | Cerrado | 1.2 |
| 21568f82-ea87-39a9-ab0e-e0e2605b081e | -6.53576 | -43.12328 | 2026-08-18 04:55:00 | NOAA-20 | BARÃO DE GRAJAÚ | MARANHÃO | Brasil | 2101509 | 21 | 33 | nan | nan | nan | Cerrado | 3.4 |
| c76abf08-1c54-3489-af85-b0fe67e476bf | -5.54549 | -52.22203 | 2026-08-18 04:55:00 | NOAA-20 | SÃO FÉLIX DO XINGU | PARÁ | Brasil | 1507300 | 15 | 33 | nan | nan | nan | Amazônia | 0.4 |
| 8cc8607d-4a86-3907-9d30-2bb245b7cb70 | -6.5355 | -43.11901 | 2026-08-18 04:55:00 | NOAA-20 | BARÃO DE GRAJAÚ | MARANHÃO | Brasil | 2101509 | 21 | 33 | nan | nan | nan | Cerrado | 2.6 |
| 61f2c0fc-833a-345d-a88c-85f93dfeecab | -3.87696 | -50.31722 | 2026-08-18 04:55:00 | NOAA-20 | PACAJÁ | PARÁ | Brasil | 1505486 | 15 | 33 | nan | nan | nan | Amazônia | 1.2 |
| b2fc4d3d-6497-35e2-bf5a-4f250fb8f0be | -6.52848 | -43.1291 | 2026-08-18 04:55:00 | NOAA-20 | BARÃO DE GRAJAÚ | MARANHÃO | Brasil | 2101509 | 21 | 33 | nan | nan | nan | Cerrado | 2.0 |
| 39c076b1-bcfd-3b96-abcf-9df90a849f3c | -2.83268 | -49.14072 | 2026-08-18 04:55:00 | NOAA-20 | MOJU | PARÁ | Brasil | 1504703 | 15 | 33 | nan | nan | nan | Amazônia | 0.4 |


[Clique aqui para ver as próximas entradas](README34.md)
