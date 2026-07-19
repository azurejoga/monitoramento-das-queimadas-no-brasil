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

## Dados Diários - Página 2

| ID | Latitude | Longitude | Data/Hora GMT | Satélite | Município | Estado | País | Município ID | Estado ID | País ID | Dias sem Chuva | Precipitação | Risco de Fogo | Bioma | FRP |
|----|----------|-----------|---------------|----------|-----------|--------|------|--------------|-----------|---------|----------------|--------------|----------------|-------|-----|
| 2d31f5ca-423a-3809-abcd-184f6e4155c2 | -18.821 | -51.216 | 2026-07-19 01:10:00 | GOES-19 | ITARUMÃ | GOIÁS | Brasil | 5211305 | 52 | 33 | nan | nan | nan | Cerrado | 55.8 |
| b2e3c7ad-e57c-3d92-9e1c-5a35b20dc2db | -22.22897 | -56.00713 | 2026-07-19 01:13:00 | TERRA_M-M | ANTÔNIO JOÃO | MATO GROSSO DO SUL | Brasil | 5000906 | 50 | 33 | nan | nan | nan | Cerrado | 41.9 |
| ccb0cee2-032f-34b5-a9cf-148c64c56620 | -22.24029 | -56.02275 | 2026-07-19 01:13:00 | TERRA_M-M | ANTÔNIO JOÃO | MATO GROSSO DO SUL | Brasil | 5000906 | 50 | 33 | nan | nan | nan | Cerrado | 67.2 |
| c54fd312-2622-3fcd-8f50-530deda56e1a | -22.2583 | -55.97029 | 2026-07-19 01:13:00 | TERRA_M-M | ANTÔNIO JOÃO | MATO GROSSO DO SUL | Brasil | 5000906 | 50 | 33 | nan | nan | nan | Cerrado | 18.8 |
| 7967ff1b-a78e-3fb7-a1ce-0f174559e758 | -22.23586 | -55.99972 | 2026-07-19 01:13:00 | TERRA_M-M | ANTÔNIO JOÃO | MATO GROSSO DO SUL | Brasil | 5000906 | 50 | 33 | nan | nan | nan | Cerrado | 16.8 |
| be4fdab8-3fdc-3834-b0e8-2e91a953c80e | -22.23322 | -56.03005 | 2026-07-19 01:13:00 | TERRA_M-M | ANTÔNIO JOÃO | MATO GROSSO DO SUL | Brasil | 5000906 | 50 | 33 | nan | nan | nan | Cerrado | 57.9 |
| fa34a3e9-20e4-3c0f-9774-214dce8ed42e | -15.34733 | -59.98544 | 2026-07-19 01:15:00 | TERRA_M-M | VILA BELA DA SANTÍSSIMA TRINDADE | MATO GROSSO | Brasil | 5105507 | 51 | 33 | nan | nan | nan | Amazônia | 11.3 |
| c5fbd317-7521-35ba-ab95-c37bccea2486 | -15.35839 | -59.99403 | 2026-07-19 01:15:00 | TERRA_M-M | VILA BELA DA SANTÍSSIMA TRINDADE | MATO GROSSO | Brasil | 5105507 | 51 | 33 | nan | nan | nan | Amazônia | 8.2 |
| f50f94c0-e418-389b-a92f-b0358d70c97f | -9.49471 | -64.0703 | 2026-07-19 01:17:00 | TERRA_M-M | PORTO VELHO | RONDÔNIA | Brasil | 1100205 | 11 | 33 | nan | nan | nan | Amazônia | 4.8 |
| 321a3f09-2e6b-372d-aa05-1f23b1f85f9d | -9.50568 | -64.07923 | 2026-07-19 01:17:00 | TERRA_M-M | PORTO VELHO | RONDÔNIA | Brasil | 1100205 | 11 | 33 | nan | nan | nan | Amazônia | 9.6 |
| 5521295b-f376-3f45-bf7a-dc88f2a4d606 | -9.5042 | -64.06891 | 2026-07-19 01:17:00 | TERRA_M-M | PORTO VELHO | RONDÔNIA | Brasil | 1100205 | 11 | 33 | nan | nan | nan | Amazônia | 18.1 |
| 23c9de4f-08e6-36ea-ba9d-3c49485bc0e7 | -7.81128 | -63.83044 | 2026-07-19 01:17:00 | TERRA_M-M | CANUTAMA | AMAZONAS | Brasil | 1300904 | 13 | 33 | nan | nan | nan | Amazônia | 6.2 |
| 3374cbe3-9658-3187-a3c2-885d92f8ffe6 | -18.8009 | -51.2196 | 2026-07-19 01:20:00 | GOES-19 | ITARUMÃ | GOIÁS | Brasil | 5211305 | 52 | 33 | nan | nan | nan | Cerrado | 99.5 |
| 8c9b3749-00f4-3d1d-8316-81cbb9a91bd6 | -18.8004 | -51.2417 | 2026-07-19 01:20:00 | GOES-19 | ITARUMÃ | GOIÁS | Brasil | 5211305 | 52 | 33 | nan | nan | nan | Cerrado | 216.5 |
| 15853ab5-974d-3c49-845f-4e0a094f0616 | -18.8205 | -51.2381 | 2026-07-19 01:20:00 | GOES-19 | ITARUMÃ | GOIÁS | Brasil | 5211305 | 52 | 33 | nan | nan | nan | Cerrado | 177.4 |
| e67ed5ee-e0af-3bd7-ad3a-0666f5ec10d7 | -17.3816 | -42.7228 | 2026-07-19 01:20:00 | GOES-19 | VEREDINHA | MINAS GERAIS | Brasil | 3171071 | 31 | 33 | nan | nan | nan | Cerrado | 53.0 |
| 41528c8e-6a7c-366b-aca7-39d296da5a99 | -18.821 | -51.216 | 2026-07-19 01:20:00 | GOES-19 | ITARUMÃ | GOIÁS | Brasil | 5211305 | 52 | 33 | nan | nan | nan | Cerrado | 83.5 |
| 2bcd8afc-83fe-3149-94d0-e9ab486b5c1c | -18.8004 | -51.2417 | 2026-07-19 01:30:00 | GOES-19 | ITARUMÃ | GOIÁS | Brasil | 5211305 | 52 | 33 | nan | nan | nan | Cerrado | 68.3 |
| 2ce44c6a-a7be-348b-98a2-f76ed27bb97e | -17.3816 | -42.7228 | 2026-07-19 01:40:00 | GOES-19 | VEREDINHA | MINAS GERAIS | Brasil | 3171071 | 31 | 33 | nan | nan | nan | Cerrado | 62.5 |
| 7575b439-567e-39b7-894f-9ddb01ff71e2 | -12.0923 | -53.3548 | 2026-07-19 01:40:00 | GOES-19 | GAÚCHA DO NORTE | MATO GROSSO | Brasil | 5103858 | 51 | 33 | nan | nan | nan | Amazônia | 51.3 |
| c4e726e3-4a07-3480-ab7b-e10cda86ac3a | -11.6401 | -47.9537 | 2026-07-19 01:40:00 | GOES-19 | CHAPADA DA NATIVIDADE | TOCANTINS | Brasil | 1705102 | 17 | 33 | nan | nan | nan | Cerrado | 58.4 |
| 3d56abda-adc4-3ab5-8690-d00ffc9a54bb | -17.3816 | -42.7228 | 2026-07-19 01:50:00 | GOES-19 | VEREDINHA | MINAS GERAIS | Brasil | 3171071 | 31 | 33 | nan | nan | nan | Cerrado | 66.4 |
| f90282b9-a4c1-3134-b36d-47e5a3616453 | -17.3615 | -42.7277 | 2026-07-19 01:50:00 | GOES-19 | VEREDINHA | MINAS GERAIS | Brasil | 3171071 | 31 | 33 | nan | nan | nan | Cerrado | 53.4 |
| 7c55072d-9e0d-3175-973c-aec2ff03db2d | -11.6401 | -47.9537 | 2026-07-19 01:50:00 | GOES-19 | CHAPADA DA NATIVIDADE | TOCANTINS | Brasil | 1705102 | 17 | 33 | nan | nan | nan | Cerrado | 61.7 |
| efc201c3-6f66-3ef1-9a64-2b749acb6ce7 | -11.621 | -47.9561 | 2026-07-19 01:50:00 | GOES-19 | CHAPADA DA NATIVIDADE | TOCANTINS | Brasil | 1705102 | 17 | 33 | nan | nan | nan | Cerrado | 67.6 |
| 5bf1ef2f-d2e5-335f-9c76-12e93a908cea | -12.0732 | -53.3567 | 2026-07-19 01:50:00 | GOES-19 | QUERÊNCIA | MATO GROSSO | Brasil | 5107065 | 51 | 33 | nan | nan | nan | Amazônia | 50.8 |
| 176e9c34-5165-3437-8f8b-a2db17f64272 | -22.5719 | -48.1543 | 2026-07-19 01:50:00 | GOES-19 | SANTA MARIA DA SERRA | SÃO PAULO | Brasil | 3547007 | 35 | 33 | nan | nan | nan | Cerrado | 54.3 |
| 70151207-27f6-3572-9470-ac2ddc57b976 | -11.6401 | -47.9537 | 2026-07-19 02:00:00 | GOES-19 | CHAPADA DA NATIVIDADE | TOCANTINS | Brasil | 1705102 | 17 | 33 | nan | nan | nan | Cerrado | 57.5 |
| 5565540d-1b45-3365-9f26-2852465da3af | -17.3615 | -42.7277 | 2026-07-19 02:00:00 | GOES-19 | VEREDINHA | MINAS GERAIS | Brasil | 3171071 | 31 | 33 | nan | nan | nan | Cerrado | 55.3 |
| d00a2d18-0a51-3668-84bc-51936fbe01b9 | -17.3816 | -42.7228 | 2026-07-19 02:00:00 | GOES-19 | VEREDINHA | MINAS GERAIS | Brasil | 3171071 | 31 | 33 | nan | nan | nan | Cerrado | 50.4 |
| 8296af7d-df8a-33b8-9255-9f5d3e908a50 | -17.3615 | -42.7277 | 2026-07-19 02:10:00 | GOES-19 | VEREDINHA | MINAS GERAIS | Brasil | 3171071 | 31 | 33 | nan | nan | nan | Cerrado | 61.3 |
| 401860b9-bd59-3b79-95fd-f6b2c44d1d6d | -17.3816 | -42.7228 | 2026-07-19 02:10:00 | GOES-19 | VEREDINHA | MINAS GERAIS | Brasil | 3171071 | 31 | 33 | nan | nan | nan | Cerrado | 67.0 |
| fdf6fdab-3710-3fc5-bf57-e19adb85a9d4 | -17.3816 | -42.7228 | 2026-07-19 02:20:00 | GOES-19 | VEREDINHA | MINAS GERAIS | Brasil | 3171071 | 31 | 33 | nan | nan | nan | Cerrado | 62.8 |
| e4b7dc4f-d8c8-380c-9e23-4aae24b8483e | -11.6401 | -47.9537 | 2026-07-19 02:30:00 | GOES-19 | CHAPADA DA NATIVIDADE | TOCANTINS | Brasil | 1705102 | 17 | 33 | nan | nan | nan | Cerrado | 50.0 |
| eb260067-d6be-3079-999d-dc4d0fe989c7 | -17.3816 | -42.7228 | 2026-07-19 02:30:00 | GOES-19 | VEREDINHA | MINAS GERAIS | Brasil | 3171071 | 31 | 33 | nan | nan | nan | Cerrado | 49.6 |
| 3c8ed2db-d316-3631-a413-4362e6102039 | -17.3816 | -42.7228 | 2026-07-19 02:40:00 | GOES-19 | VEREDINHA | MINAS GERAIS | Brasil | 3171071 | 31 | 33 | nan | nan | nan | Cerrado | 56.2 |
| eaf881ef-0254-352b-82d4-1caf37d4323b | -13.6764 | -48.7786 | 2026-07-19 02:40:00 | GOES-19 | FORMOSO | GOIÁS | Brasil | 5208103 | 52 | 33 | nan | nan | nan | Cerrado | 73.2 |
| 231e99fe-3d50-3bde-bb37-351717f7a233 | -17.3816 | -42.7228 | 2026-07-19 02:50:00 | GOES-19 | VEREDINHA | MINAS GERAIS | Brasil | 3171071 | 31 | 33 | nan | nan | nan | Cerrado | 53.6 |
| e052ef87-b7d8-30bc-89b8-1ee8c99090db | -11.621 | -47.9561 | 2026-07-19 02:50:00 | GOES-19 | CHAPADA DA NATIVIDADE | TOCANTINS | Brasil | 1705102 | 17 | 33 | nan | nan | nan | Cerrado | 50.0 |
| 3825ab80-07c9-386e-81d3-5a91a062b4a3 | -13.6764 | -48.7786 | 2026-07-19 02:50:00 | GOES-19 | FORMOSO | GOIÁS | Brasil | 5208103 | 52 | 33 | nan | nan | nan | Cerrado | 69.3 |
| 3f38f0ce-fe52-32ca-a608-32d8c93f9633 | -10.8273 | -50.2244 | 2026-07-19 03:00:00 | GOES-19 | LAGOA DA CONFUSÃO | TOCANTINS | Brasil | 1711902 | 17 | 33 | nan | nan | nan | Cerrado | 87.3 |
| b60451f4-863a-35d2-848c-e1296f4cddad | -10.8271 | -50.2458 | 2026-07-19 03:00:00 | GOES-19 | LAGOA DA CONFUSÃO | TOCANTINS | Brasil | 1711902 | 17 | 33 | nan | nan | nan | Cerrado | 114.6 |
| 385cdeb2-5e41-366e-b2a5-c8223160bf4f | -13.6764 | -48.7786 | 2026-07-19 03:00:00 | GOES-19 | FORMOSO | GOIÁS | Brasil | 5208103 | 52 | 33 | nan | nan | nan | Cerrado | 73.7 |
| e999cfab-66df-3396-9884-dd14b898ae20 | -13.6764 | -48.7786 | 2026-07-19 03:10:00 | GOES-19 | FORMOSO | GOIÁS | Brasil | 5208103 | 52 | 33 | nan | nan | nan | Cerrado | 60.7 |
| cec02b12-b8dd-3da8-9d14-b7b7cbcc6716 | -10.8271 | -50.2458 | 2026-07-19 03:10:00 | GOES-19 | LAGOA DA CONFUSÃO | TOCANTINS | Brasil | 1711902 | 17 | 33 | nan | nan | nan | Cerrado | 58.3 |
| 57d225d1-0ba3-37e2-bc34-8fa48848cfc2 | -10.8273 | -50.2244 | 2026-07-19 03:10:00 | GOES-19 | LAGOA DA CONFUSÃO | TOCANTINS | Brasil | 1711902 | 17 | 33 | nan | nan | nan | Cerrado | 51.0 |
| 30d6d7bc-1512-36bf-9ff1-17503b498628 | -7.11642 | -44.04939 | 2026-07-19 03:23:00 | NOAA-21 | PORTO ALEGRE DO PIAUÍ | PIAUÍ | Brasil | 2208551 | 22 | 33 | nan | nan | nan | Cerrado | 1.9 |
| da3f6766-d683-3fd5-99a4-9eec2c34330e | -9.59685 | -40.61327 | 2026-07-19 03:23:00 | NOAA-21 | JUAZEIRO | BAHIA | Brasil | 2918407 | 29 | 33 | nan | nan | nan | Caatinga | 3.4 |
| 73cba215-1d99-3bc2-980f-c6cc76b6707d | -5.10793 | -38.06688 | 2026-07-19 03:23:00 | NOAA-21 | LIMOEIRO DO NORTE | CEARÁ | Brasil | 2307601 | 23 | 33 | nan | nan | nan | Caatinga | 15.5 |
| 9897f05f-281b-34db-a7b1-8ca6fa3f6ffd | -9.59749 | -40.60978 | 2026-07-19 03:23:00 | NOAA-21 | JUAZEIRO | BAHIA | Brasil | 2918407 | 29 | 33 | nan | nan | nan | Caatinga | 3.6 |
| 5dc0c01e-8d38-3730-840b-e7fcf69fa96e | -7.11826 | -44.04245 | 2026-07-19 03:23:00 | NOAA-21 | PORTO ALEGRE DO PIAUÍ | PIAUÍ | Brasil | 2208551 | 22 | 33 | nan | nan | nan | Cerrado | 1.3 |
| 3cddc791-9894-34a9-b4be-3629c08c5fcb | -9.59416 | -40.60969 | 2026-07-19 03:23:00 | NOAA-21 | JUAZEIRO | BAHIA | Brasil | 2918407 | 29 | 33 | nan | nan | nan | Caatinga | 8.1 |
| 258279fb-fe82-3452-afbf-6d8a9403ba8a | -9.59349 | -40.61318 | 2026-07-19 03:23:00 | NOAA-21 | JUAZEIRO | BAHIA | Brasil | 2918407 | 29 | 33 | nan | nan | nan | Caatinga | 5.5 |
| e5b44a23-9f8d-3fca-ac54-9785d2e15d4c | -9.59146 | -40.61229 | 2026-07-19 03:23:00 | NOAA-21 | JUAZEIRO | BAHIA | Brasil | 2918407 | 29 | 33 | nan | nan | nan | Caatinga | 3.4 |
| 4e2127b3-5c97-3dc8-a7cb-3538dcc89bd8 | -7.11705 | -44.04895 | 2026-07-19 03:23:00 | NOAA-21 | PORTO ALEGRE DO PIAUÍ | PIAUÍ | Brasil | 2208551 | 22 | 33 | nan | nan | nan | Cerrado | 1.3 |
| 91b731dd-ecc7-375a-a549-14be4246c0e3 | -5.93052 | -43.64937 | 2026-07-19 03:23:00 | NOAA-21 | LAGOA DO MATO | MARANHÃO | Brasil | 2105922 | 21 | 33 | nan | nan | nan | Cerrado | 3.7 |
| f274ab73-828c-3aac-95dc-18ef40b842c4 | -9.5921 | -40.60878 | 2026-07-19 03:23:00 | NOAA-21 | JUAZEIRO | BAHIA | Brasil | 2918407 | 29 | 33 | nan | nan | nan | Caatinga | 3.6 |
| ee4dcaa6-2a22-3ecb-8ea3-4e9c3c317e4e | -7.11766 | -44.04295 | 2026-07-19 03:23:00 | NOAA-21 | PORTO ALEGRE DO PIAUÍ | PIAUÍ | Brasil | 2208551 | 22 | 33 | nan | nan | nan | Cerrado | 2.5 |
| 840e8c38-73c0-3463-b20f-86ddf97ffd58 | -5.93753 | -43.65013 | 2026-07-19 03:23:00 | NOAA-21 | LAGOA DO MATO | MARANHÃO | Brasil | 2105922 | 21 | 33 | nan | nan | nan | Cerrado | 1.1 |
| 933ade0d-c3b0-3275-ab04-369c0dc98d0f | -7.64851 | -37.27062 | 2026-07-19 03:23:00 | NOAA-21 | TUPARETAMA | PERNAMBUCO | Brasil | 2615904 | 26 | 33 | nan | nan | nan | Caatinga | 1.4 |
| a680842f-0111-3fd8-9530-fffaf1a8cef9 | -5.93061 | -43.64899 | 2026-07-19 03:23:00 | NOAA-21 | LAGOA DO MATO | MARANHÃO | Brasil | 2105922 | 21 | 33 | nan | nan | nan | Cerrado | 1.7 |
| c8292858-a006-328e-8225-1d902c963008 | -17.36616 | -42.73447 | 2026-07-19 03:25:00 | NOAA-21 | VEREDINHA | MINAS GERAIS | Brasil | 3171071 | 31 | 33 | nan | nan | nan | Cerrado | 1.6 |
| 79e63247-404c-310e-bbd9-2d899d75bc8a | -17.37377 | -42.72479 | 2026-07-19 03:25:00 | NOAA-21 | VEREDINHA | MINAS GERAIS | Brasil | 3171071 | 31 | 33 | nan | nan | nan | Cerrado | 11.8 |
| 1e47e942-8819-3e02-ae97-88febe159ed7 | -17.37518 | -42.71801 | 2026-07-19 03:25:00 | NOAA-21 | VEREDINHA | MINAS GERAIS | Brasil | 3171071 | 31 | 33 | nan | nan | nan | Cerrado | 3.8 |
| 77e19bc8-a345-310f-86a9-62b072f91127 | -17.36908 | -42.72044 | 2026-07-19 03:25:00 | NOAA-21 | VEREDINHA | MINAS GERAIS | Brasil | 3171071 | 31 | 33 | nan | nan | nan | Cerrado | 11.8 |
| 1ac34bc6-329e-35de-b591-f951e8b6740a | -11.60345 | -43.11394 | 2026-07-19 03:25:00 | NOAA-21 | MORPARÁ | BAHIA | Brasil | 2921609 | 29 | 33 | nan | nan | nan | Caatinga | 2.9 |
| 66f34658-6c7a-3d5a-9354-7c6fefd4c4ba | -17.36692 | -42.73083 | 2026-07-19 03:25:00 | NOAA-21 | VEREDINHA | MINAS GERAIS | Brasil | 3171071 | 31 | 33 | nan | nan | nan | Cerrado | 4.4 |
| 05f493b2-aa97-33f7-a3ab-345a86eea82e | -17.36837 | -42.72387 | 2026-07-19 03:25:00 | NOAA-21 | VEREDINHA | MINAS GERAIS | Brasil | 3171071 | 31 | 33 | nan | nan | nan | Cerrado | 11.8 |
| 4d7559d4-6104-389f-830c-403bc9df9e1e | -17.3723 | -42.73186 | 2026-07-19 03:25:00 | NOAA-21 | VEREDINHA | MINAS GERAIS | Brasil | 3171071 | 31 | 33 | nan | nan | nan | Cerrado | 4.4 |
| 3e90d575-132d-39fd-897e-3519e1f00016 | -17.36977 | -42.71712 | 2026-07-19 03:25:00 | NOAA-21 | VEREDINHA | MINAS GERAIS | Brasil | 3171071 | 31 | 33 | nan | nan | nan | Cerrado | 3.8 |
| 4d660ce6-4305-3808-bd4f-b0d153f87aee | -11.60349 | -43.11595 | 2026-07-19 03:25:00 | NOAA-21 | MORPARÁ | BAHIA | Brasil | 2921609 | 29 | 33 | nan | nan | nan | Caatinga | 2.7 |
| 3ddc210b-2971-367f-86c6-58cf8d6dfaef | -17.36765 | -42.72731 | 2026-07-19 03:25:00 | NOAA-21 | VEREDINHA | MINAS GERAIS | Brasil | 3171071 | 31 | 33 | nan | nan | nan | Cerrado | 4.4 |
| 2e835588-4cd6-3efe-bf00-338468231143 | -17.37304 | -42.72828 | 2026-07-19 03:25:00 | NOAA-21 | VEREDINHA | MINAS GERAIS | Brasil | 3171071 | 31 | 33 | nan | nan | nan | Cerrado | 4.4 |
| fe3c12d5-90d3-3db5-a0f9-e09b7f3382c6 | -17.37449 | -42.72133 | 2026-07-19 03:25:00 | NOAA-21 | VEREDINHA | MINAS GERAIS | Brasil | 3171071 | 31 | 33 | nan | nan | nan | Cerrado | 11.8 |
| f2174845-3ab6-360d-888b-db555cc6110b | -19.72338 | -48.02705 | 2026-07-19 03:28:00 | NOAA-21 | UBERABA | MINAS GERAIS | Brasil | 3170107 | 31 | 33 | nan | nan | nan | Cerrado | 5.2 |
| d04cbad9-a826-3570-b24c-21098928dc12 | -19.17554 | -47.35447 | 2026-07-19 03:28:00 | NOAA-21 | PERDIZES | MINAS GERAIS | Brasil | 3149804 | 31 | 33 | nan | nan | nan | Cerrado | 2.7 |
| 42ab10e7-4936-3c28-bc4a-fed88d3f571f | -22.72537 | -43.4809 | 2026-07-19 03:28:00 | NOAA-21 | NOVA IGUAÇU | RIO DE JANEIRO | Brasil | 3303500 | 33 | 33 | nan | nan | nan | Mata Atlântica | 0.9 |
| de3b0d3a-e43d-3cfc-9d93-3bae6d3a37b8 | -19.98771 | -43.97407 | 2026-07-19 03:28:00 | NOAA-21 | BELO HORIZONTE | MINAS GERAIS | Brasil | 3106200 | 31 | 33 | nan | nan | nan | Mata Atlântica | 1.5 |
| f5244cf1-b412-322a-b34d-71665dde7fe6 | -21.53304 | -46.76418 | 2026-07-19 03:28:00 | NOAA-21 | TAPIRATIBA | SÃO PAULO | Brasil | 3553609 | 35 | 33 | nan | nan | nan | Mata Atlântica | 6.2 |
| fa70f211-220b-387e-b17e-fb900e3cb654 | -20.74342 | -42.04924 | 2026-07-19 03:28:00 | NOAA-21 | FARIA LEMOS | MINAS GERAIS | Brasil | 3125309 | 31 | 33 | nan | nan | nan | Mata Atlântica | 3.4 |
| 9e460821-45cf-3539-a0b8-a9fc8cf3c76f | -20.74196 | -42.05026 | 2026-07-19 03:28:00 | NOAA-21 | FARIA LEMOS | MINAS GERAIS | Brasil | 3125309 | 31 | 33 | nan | nan | nan | Mata Atlântica | 2.2 |
| dbf35075-aa8f-3399-b277-25aead7e1cd4 | -22.72354 | -43.47977 | 2026-07-19 03:28:00 | NOAA-21 | NOVA IGUAÇU | RIO DE JANEIRO | Brasil | 3303500 | 33 | 33 | nan | nan | nan | Mata Atlântica | 1.6 |
| 20c2ad0f-9f82-30e7-a71b-e3f813de007f | -19.98726 | -43.97366 | 2026-07-19 03:28:00 | NOAA-21 | BELO HORIZONTE | MINAS GERAIS | Brasil | 3106200 | 31 | 33 | nan | nan | nan | Mata Atlântica | 1.6 |
| eb4fe853-ae31-3932-95a4-cbe0feb1464f | -22.90942 | -43.44575 | 2026-07-19 03:28:00 | NOAA-21 | RIO DE JANEIRO | RIO DE JANEIRO | Brasil | 3304557 | 33 | 33 | nan | nan | nan | Mata Atlântica | 2.3 |
| f646ecf9-96d7-3106-a96f-0cef3674e668 | -19.72836 | -48.02962 | 2026-07-19 03:28:00 | NOAA-21 | UBERABA | MINAS GERAIS | Brasil | 3170107 | 31 | 33 | nan | nan | nan | Cerrado | 2.5 |
| 4b8fc0c6-465c-35ad-b83b-70610f9e9d80 | -19.72158 | -48.02731 | 2026-07-19 03:28:00 | NOAA-21 | UBERABA | MINAS GERAIS | Brasil | 3170107 | 31 | 33 | nan | nan | nan | Cerrado | 3.7 |
| a41993af-dfbd-33d5-8b8e-2fde4eb6fcef | -22.26227 | -44.35045 | 2026-07-19 03:28:00 | NOAA-21 | RESENDE | RIO DE JANEIRO | Brasil | 3304201 | 33 | 33 | nan | nan | nan | Mata Atlântica | 1.5 |
| 18097edc-0561-3b75-b663-4ae0c0b3ba90 | -21.52922 | -46.76487 | 2026-07-19 03:28:00 | NOAA-21 | TAPIRATIBA | SÃO PAULO | Brasil | 3553609 | 35 | 33 | nan | nan | nan | Mata Atlântica | 3.0 |
| 67b1f1d3-dd5d-3ff2-9aad-0a70430f4b21 | -19.81857 | -47.95699 | 2026-07-19 03:28:00 | NOAA-21 | UBERABA | MINAS GERAIS | Brasil | 3170107 | 31 | 33 | nan | nan | nan | Cerrado | 2.7 |
| 18dd1c8c-2b17-3246-b9a5-7f28bb830982 | -20.74297 | -42.04545 | 2026-07-19 03:28:00 | NOAA-21 | CARANGOLA | MINAS GERAIS | Brasil | 3113305 | 31 | 33 | nan | nan | nan | Mata Atlântica | 2.2 |
| 93d2f98e-1585-3458-af9f-011fe5acc32e | -23.71206 | -46.8953 | 2026-07-19 03:28:00 | NOAA-21 | ITAPECERICA DA SERRA | SÃO PAULO | Brasil | 3522208 | 35 | 33 | nan | nan | nan | Mata Atlântica | 2.2 |
| 9072cfce-4e84-3f65-a499-d8dff23d8507 | -22.18879 | -45.82387 | 2026-07-19 03:28:00 | NOAA-21 | SÃO SEBASTIÃO DA BELA VISTA | MINAS GERAIS | Brasil | 3164407 | 31 | 33 | nan | nan | nan | Mata Atlântica | 1.9 |
| 25725e57-38c2-3421-8521-9e2feabe63db | -22.46532 | -43.0855 | 2026-07-19 03:28:00 | NOAA-21 | PETRÓPOLIS | RIO DE JANEIRO | Brasil | 3303906 | 33 | 33 | nan | nan | nan | Mata Atlântica | 8.2 |
| dbe01bef-ee1d-3d43-85d6-c70f6c06bd07 | -21.53527 | -46.76729 | 2026-07-19 03:28:00 | NOAA-21 | TAPIRATIBA | SÃO PAULO | Brasil | 3553609 | 35 | 33 | nan | nan | nan | Mata Atlântica | 3.4 |
| 65546059-ef30-3b00-91f2-4b1ff94d813a | -23.7119 | -46.89807 | 2026-07-19 03:28:00 | NOAA-21 | ITAPECERICA DA SERRA | SÃO PAULO | Brasil | 3522208 | 35 | 33 | nan | nan | nan | Mata Atlântica | 1.3 |
| ef90d217-6489-324e-9f94-476b096c7b91 | -19.81924 | -47.95767 | 2026-07-19 03:28:00 | NOAA-21 | UBERABA | MINAS GERAIS | Brasil | 3170107 | 31 | 33 | nan | nan | nan | Cerrado | 4.6 |
| 0c0ca41d-dce5-3d70-b209-3c8fc4418de5 | -22.72036 | -43.47951 | 2026-07-19 03:28:00 | NOAA-21 | NOVA IGUAÇU | RIO DE JANEIRO | Brasil | 3303500 | 33 | 33 | nan | nan | nan | Mata Atlântica | 0.9 |
| 4617d9b5-995f-3806-8112-69acb1568062 | -23.71307 | -46.89328 | 2026-07-19 03:28:00 | NOAA-21 | ITAPECERICA DA SERRA | SÃO PAULO | Brasil | 3522208 | 35 | 33 | nan | nan | nan | Mata Atlântica | 1.3 |
| f413558d-15b5-3ae7-8046-179c7efad98c | -23.72528 | -46.5214 | 2026-07-19 03:28:00 | NOAA-21 | SÃO BERNARDO DO CAMPO | SÃO PAULO | Brasil | 3548708 | 35 | 33 | nan | nan | nan | Mata Atlântica | 3.1 |
| 0cba14e8-a6e2-3e84-93b8-5c7bc8d32ace | -23.28991 | -46.15336 | 2026-07-19 03:28:00 | NOAA-21 | SANTA ISABEL | SÃO PAULO | Brasil | 3546801 | 35 | 33 | nan | nan | nan | Mata Atlântica | 2.4 |


[Clique aqui para ver as próximas entradas](README3.md)
