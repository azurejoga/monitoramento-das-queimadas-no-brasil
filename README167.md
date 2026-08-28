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

## Dados Diários - Página 167

| ID | Latitude | Longitude | Data/Hora GMT | Satélite | Município | Estado | País | Município ID | Estado ID | País ID | Dias sem Chuva | Precipitação | Risco de Fogo | Bioma | FRP |
|----|----------|-----------|---------------|----------|-----------|--------|------|--------------|-----------|---------|----------------|--------------|----------------|-------|-----|
| f5119473-6269-3aa6-b760-2b77d305960b | -1.87037 | -47.98301 | 2026-08-28 18:51:00 | AQUA_M-T | CONCÓRDIA DO PARÁ | PARÁ | Brasil | 1502756 | 15 | 33 | nan | nan | nan | Amazônia | 7.9 |
| 4c786aee-2a06-3b14-b2e9-8533d6689b75 | -0.51992 | -51.81293 | 2026-08-28 18:51:00 | AQUA_M-T | MAZAGÃO | AMAPÁ | Brasil | 1600402 | 16 | 33 | nan | nan | nan | Amazônia | 13.1 |
| de6ceeab-8ac7-3a05-bb25-554847132dbe | -2.15557 | -48.78698 | 2026-08-28 18:51:00 | AQUA_M-T | MOJU | PARÁ | Brasil | 1504703 | 15 | 33 | nan | nan | nan | Amazônia | 5.0 |
| b62b7845-fa46-3ac1-a2c7-0a35c12b4e1b | 2.52017 | -50.84952 | 2026-08-28 18:51:00 | AQUA_M-T | CALÇOENE | AMAPÁ | Brasil | 1600204 | 16 | 33 | nan | nan | nan | Amazônia | 18.3 |
| 243778df-5a9d-390d-a779-b534f58347be | -1.46553 | -55.83498 | 2026-08-28 18:51:00 | AQUA_M-T | ORIXIMINÁ | PARÁ | Brasil | 1505304 | 15 | 33 | nan | nan | nan | Amazônia | 23.5 |
| a67020fc-27f0-3957-97ff-55827cedfc3e | -1.36733 | -49.08585 | 2026-08-28 18:51:00 | AQUA_M-T | PONTA DE PEDRAS | PARÁ | Brasil | 1505700 | 15 | 33 | nan | nan | nan | Amazônia | 5.4 |
| bd1a6d24-9e22-3422-958b-ccb91f626625 | 2.23804 | -50.76356 | 2026-08-28 18:51:00 | AQUA_M-T | CALÇOENE | AMAPÁ | Brasil | 1600204 | 16 | 33 | nan | nan | nan | Amazônia | 15.6 |
| a3235f81-373f-3be9-96f7-19f4f33c7de1 | -2.32446 | -45.67194 | 2026-08-28 18:51:00 | AQUA_M-T | TURILÂNDIA | MARANHÃO | Brasil | 2112456 | 21 | 33 | nan | nan | nan | Amazônia | 6.6 |
| a208b5c3-0dd9-35e9-ab5c-8dea4f0f4d9a | -2.12152 | -44.78878 | 2026-08-28 18:51:00 | AQUA_M-T | MIRINZAL | MARANHÃO | Brasil | 2106805 | 21 | 33 | nan | nan | nan | Amazônia | 8.2 |
| bc6e3c60-7756-3452-9638-fa4ef3781cb9 | 2.24716 | -50.76163 | 2026-08-28 18:51:00 | AQUA_M-T | CALÇOENE | AMAPÁ | Brasil | 1600204 | 16 | 33 | nan | nan | nan | Amazônia | 19.6 |
| 43f85ab9-7927-3c9b-80d1-0c43724051bd | -1.08347 | -48.02402 | 2026-08-28 18:51:00 | AQUA_M-T | VIGIA | PARÁ | Brasil | 1508209 | 15 | 33 | nan | nan | nan | Amazônia | 75.1 |
| 7ed219a8-7e63-365c-b0e3-ad70b3c2852a | -2.2176 | -46.87957 | 2026-08-28 18:51:00 | AQUA_M-T | NOVA ESPERANÇA DO PIRIÁ | PARÁ | Brasil | 1504950 | 15 | 33 | nan | nan | nan | Amazônia | 18.4 |
| 3b0a0ad5-c07e-3230-a435-2e3b586857b5 | -0.80975 | -48.73824 | 2026-08-28 18:51:00 | AQUA_M-T | CACHOEIRA DO ARARI | PARÁ | Brasil | 1502004 | 15 | 33 | nan | nan | nan | Amazônia | 6.1 |
| 8070ce33-6a41-3118-bb01-c2d30412d5ad | 1.20191 | -51.00933 | 2026-08-28 18:51:00 | AQUA_M-T | TARTARUGALZINHO | AMAPÁ | Brasil | 1600709 | 16 | 33 | nan | nan | nan | Amazônia | 11.3 |
| 93ad90ab-1ace-347a-8da6-ea257bafd046 | -2.24627 | -52.84391 | 2026-08-28 18:51:00 | AQUA_M-T | PORTO DE MOZ | PARÁ | Brasil | 1505908 | 15 | 33 | nan | nan | nan | Amazônia | 16.1 |
| 1d6bcbc6-5784-3c52-8b65-94e42029bf05 | -1.59538 | -48.18456 | 2026-08-28 18:51:00 | AQUA_M-T | BUJARU | PARÁ | Brasil | 1501907 | 15 | 33 | nan | nan | nan | Amazônia | 4.8 |
| 39e189cb-0e46-3444-8ac9-a0b7a1edae82 | -0.9057 | -46.69437 | 2026-08-28 18:51:00 | AQUA_M-T | BRAGANÇA | PARÁ | Brasil | 1501709 | 15 | 33 | nan | nan | nan | Amazônia | 5.5 |
| 04e9f9c0-32f9-371e-a2b5-d544b6c749fb | -2.03514 | -48.78414 | 2026-08-28 18:51:00 | AQUA_M-T | MOJU | PARÁ | Brasil | 1504703 | 15 | 33 | nan | nan | nan | Amazônia | 45.0 |
| f4cdc298-a04f-363b-ac07-15363896b852 | 2.24572 | -50.7712 | 2026-08-28 18:51:00 | AQUA_M-T | CALÇOENE | AMAPÁ | Brasil | 1600204 | 16 | 33 | nan | nan | nan | Amazônia | 74.2 |
| 793f0004-6318-383d-941c-8e206a0a7266 | -2.74447 | -48.70317 | 2026-08-28 18:51:00 | AQUA_M-T | TAILÂNDIA | PARÁ | Brasil | 1507953 | 15 | 33 | nan | nan | nan | Amazônia | 8.2 |
| 94270ca9-6128-3fac-b09c-7e01780c1bf1 | -1.12178 | -54.08437 | 2026-08-28 18:51:00 | AQUA_M-T | MONTE ALEGRE | PARÁ | Brasil | 1504802 | 15 | 33 | nan | nan | nan | Amazônia | 15.1 |
| 83a71a88-b4dd-3fa8-b4f1-0047e7ebdd20 | -1.08475 | -48.03271 | 2026-08-28 18:51:00 | AQUA_M-T | VIGIA | PARÁ | Brasil | 1508209 | 15 | 33 | nan | nan | nan | Amazônia | 18.4 |
| e287d83c-9af2-3e6e-b8ed-f4894f8db574 | 2.23664 | -50.77314 | 2026-08-28 18:51:00 | AQUA_M-T | CALÇOENE | AMAPÁ | Brasil | 1600204 | 16 | 33 | nan | nan | nan | Amazônia | 12.8 |
| 2af75b29-eb7d-30b3-8acc-dcffa97eeeb9 | -0.8647 | -48.68546 | 2026-08-28 18:51:00 | AQUA_M-T | SALVATERRA | PARÁ | Brasil | 1506302 | 15 | 33 | nan | nan | nan | Amazônia | 7.4 |
| ec3239f4-2b41-31e1-bcbf-09ee6b4be202 | -2.33607 | -48.49893 | 2026-08-28 18:51:00 | AQUA_M-T | ACARÁ | PARÁ | Brasil | 1500206 | 15 | 33 | nan | nan | nan | Amazônia | 11.0 |
| d04a1b52-a7c0-326f-b2d8-c409382c344c | 3.27906 | -51.33815 | 2026-08-28 18:51:00 | AQUA_M-T | OIAPOQUE | AMAPÁ | Brasil | 1600501 | 16 | 33 | nan | nan | nan | Amazônia | 6.0 |
| a1fdbf24-308d-3ec7-af6a-b603e1cd4424 | 4.0313 | -51.63379 | 2026-08-28 18:51:00 | AQUA_M-T | OIAPOQUE | AMAPÁ | Brasil | 1600501 | 16 | 33 | nan | nan | nan | Amazônia | 11.9 |
| 60ddbdd5-fb7a-3772-a2ef-49cd05fd1703 | -2.40205 | -50.59311 | 2026-08-28 18:51:00 | AQUA_M-T | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 5.6 |
| 06a56ca8-e68b-3dae-be24-bf8bbd5b36e8 | 2.24427 | -50.78078 | 2026-08-28 18:51:00 | AQUA_M-T | CALÇOENE | AMAPÁ | Brasil | 1600204 | 16 | 33 | nan | nan | nan | Amazônia | 6.8 |
| 4182b567-3d67-3a25-aeef-4c64550eea4f | -1.40326 | -50.71031 | 2026-08-28 18:51:00 | AQUA_M-T | BREVES | PARÁ | Brasil | 1501808 | 15 | 33 | nan | nan | nan | Amazônia | 23.9 |
| e6d7b66e-8c05-3ccf-b2fa-b50cebc9b490 | -1.58775 | -47.74356 | 2026-08-28 18:51:00 | AQUA_M-T | SÃO MIGUEL DO GUAMÁ | PARÁ | Brasil | 1507607 | 15 | 33 | nan | nan | nan | Amazônia | 32.2 |
| c35f0b20-1405-37b5-9122-a5126668cbec | -1.09817 | -49.19827 | 2026-08-28 18:51:00 | AQUA_M-T | PONTA DE PEDRAS | PARÁ | Brasil | 1505700 | 15 | 33 | nan | nan | nan | Amazônia | 8.2 |
| 291d78bd-5a85-3830-a321-38b8aca5f821 | 4.01256 | -51.63096 | 2026-08-28 18:51:00 | AQUA_M-T | OIAPOQUE | AMAPÁ | Brasil | 1600501 | 16 | 33 | nan | nan | nan | Amazônia | 6.8 |
| e5a25056-ea04-3ad4-a1de-2aaa024ca9e3 | -1.26483 | -49.19809 | 2026-08-28 18:51:00 | AQUA_M-T | MUANÁ | PARÁ | Brasil | 1504901 | 15 | 33 | nan | nan | nan | Amazônia | 6.5 |
| eba20237-26e5-3af6-857f-c60010580c70 | -1.10835 | -49.20592 | 2026-08-28 18:51:00 | AQUA_M-T | PONTA DE PEDRAS | PARÁ | Brasil | 1505700 | 15 | 33 | nan | nan | nan | Amazônia | 9.6 |
| ad6995c0-b34e-31aa-8034-39063f3d918b | -2.03384 | -48.77528 | 2026-08-28 18:51:00 | AQUA_M-T | MOJU | PARÁ | Brasil | 1504703 | 15 | 33 | nan | nan | nan | Amazônia | 11.8 |
| 08dd73c9-ff39-3854-935a-77586614b137 | -3.54518 | -54.48372 | 2026-08-28 18:51:00 | AQUA_M-T | PLACAS | PARÁ | Brasil | 1505650 | 15 | 33 | nan | nan | nan | Amazônia | 13.1 |
| 4c3a7f14-7fc9-30f2-ba1a-290f3b3eb5f3 | -1.52368 | -49.45351 | 2026-08-28 18:51:00 | AQUA_M-T | MUANÁ | PARÁ | Brasil | 1504901 | 15 | 33 | nan | nan | nan | Amazônia | 8.9 |
| 8c4c10ee-ac3f-3c6c-b624-db387f9dd5db | -2.00111 | -47.67573 | 2026-08-28 18:51:00 | AQUA_M-T | AURORA DO PARÁ | PARÁ | Brasil | 1500958 | 15 | 33 | nan | nan | nan | Amazônia | 8.0 |
| 651919b9-1f1b-3062-aa50-4f93361c94c1 | 2.61545 | -50.95916 | 2026-08-28 18:51:00 | AQUA_M-T | CALÇOENE | AMAPÁ | Brasil | 1600204 | 16 | 33 | nan | nan | nan | Amazônia | 10.2 |
| 09d66325-d2d7-35bc-a721-99758b43f799 | -1.35216 | -49.48147 | 2026-08-28 18:51:00 | AQUA_M-T | MUANÁ | PARÁ | Brasil | 1504901 | 15 | 33 | nan | nan | nan | Amazônia | 4.9 |
| e0d1601b-0f84-3f34-bc20-ca5a0cfa5a02 | -1.0986 | -48.0662 | 2026-08-28 18:51:00 | AQUA_M-T | SANTO ANTÔNIO DO TAUÁ | PARÁ | Brasil | 1507003 | 15 | 33 | nan | nan | nan | Amazônia | 7.6 |
| 691425c5-2b1c-3ed9-916a-b8db0df6adb6 | 1.20039 | -51.0194 | 2026-08-28 18:51:00 | AQUA_M-T | TARTARUGALZINHO | AMAPÁ | Brasil | 1600709 | 16 | 33 | nan | nan | nan | Amazônia | 35.8 |
| 4d7063b7-6122-3562-a8c1-d4f6953cafc7 | 2.51872 | -50.85913 | 2026-08-28 18:51:00 | AQUA_M-T | CALÇOENE | AMAPÁ | Brasil | 1600204 | 16 | 33 | nan | nan | nan | Amazônia | 26.2 |
| 6b023c8f-9053-3624-a1d2-1260a5bacdd5 | -1.03288 | -47.55853 | 2026-08-28 18:51:00 | AQUA_M-T | IGARAPÉ-AÇU | PARÁ | Brasil | 1503200 | 15 | 33 | nan | nan | nan | Amazônia | 9.8 |
| f569c5d8-0ee5-3e29-8e55-c044f420ffad | -3.54414 | -54.50077 | 2026-08-28 18:51:00 | AQUA_M-T | PLACAS | PARÁ | Brasil | 1505650 | 15 | 33 | nan | nan | nan | Amazônia | 20.4 |
| 7497acd6-177f-3fce-9979-a54173d904ec | 2.61399 | -50.96887 | 2026-08-28 18:51:00 | AQUA_M-T | CALÇOENE | AMAPÁ | Brasil | 1600204 | 16 | 33 | nan | nan | nan | Amazônia | 9.1 |
| 1f40e7ed-b912-3cf0-a038-bb85c3953b3d | -2.02632 | -48.78545 | 2026-08-28 18:51:00 | AQUA_M-T | MOJU | PARÁ | Brasil | 1504703 | 15 | 33 | nan | nan | nan | Amazônia | 55.0 |
| 4c22ae9c-d2d1-34b1-8f26-ab7c0cafbb59 | 1.79171 | -55.82424 | 2026-08-28 18:51:00 | AQUA_M-T | ÓBIDOS | PARÁ | Brasil | 1505106 | 15 | 33 | nan | nan | nan | Amazônia | 19.9 |
| eced10bf-4ecf-3d0b-87a0-b0c1e83273af | -1.09733 | -48.05751 | 2026-08-28 18:51:00 | AQUA_M-T | SANTO ANTÔNIO DO TAUÁ | PARÁ | Brasil | 1507003 | 15 | 33 | nan | nan | nan | Amazônia | 19.2 |
| f63a49d5-2886-3619-b1c7-af2ac2525746 | -1.57899 | -47.74485 | 2026-08-28 18:51:00 | AQUA_M-T | SÃO MIGUEL DO GUAMÁ | PARÁ | Brasil | 1507607 | 15 | 33 | nan | nan | nan | Amazônia | 38.5 |
| 52697963-947e-38cd-a832-433e0f6cb281 | -1.11513 | -54.09872 | 2026-08-28 18:51:00 | AQUA_M-T | MONTE ALEGRE | PARÁ | Brasil | 1504802 | 15 | 33 | nan | nan | nan | Amazônia | 16.4 |
| f723044f-4d45-3776-bdde-b9f0281c80c3 | -1.10703 | -49.19697 | 2026-08-28 18:51:00 | AQUA_M-T | PONTA DE PEDRAS | PARÁ | Brasil | 1505700 | 15 | 33 | nan | nan | nan | Amazônia | 27.8 |
| f514c0bd-c977-392b-a5b7-9e0f2f1cd501 | -6.1657 | -57.7793 | 2026-08-28 19:00:00 | GOES-19 | JACAREACANGA | PARÁ | Brasil | 1503754 | 15 | 33 | nan | nan | nan | Amazônia | 183.1 |
| 84093c9e-36b4-390b-a327-0db6140af5e1 | -14.9015 | -52.6055 | 2026-08-28 19:00:00 | GOES-19 | NOVA XAVANTINA | MATO GROSSO | Brasil | 5106257 | 51 | 33 | nan | nan | nan | Cerrado | 601.8 |
| 86c24c80-df1b-3b0c-8608-ab05db530160 | -6.8569 | -59.4564 | 2026-08-28 19:00:00 | GOES-19 | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 73.7 |
| 6364d192-fd18-3835-b589-60fc458ad1fa | -14.8624 | -52.6318 | 2026-08-28 19:00:00 | GOES-19 | NOVA XAVANTINA | MATO GROSSO | Brasil | 5106257 | 51 | 33 | nan | nan | nan | Cerrado | 93.8 |
| 4c2f6bdd-0a70-34a4-8dfd-e567f94be587 | -6.1472 | -57.7995 | 2026-08-28 19:00:00 | GOES-19 | JACAREACANGA | PARÁ | Brasil | 1503754 | 15 | 33 | nan | nan | nan | Amazônia | 102.3 |
| 4569db76-6069-39fe-bb8c-a340ce354140 | -6.8358 | -59.9379 | 2026-08-28 19:00:00 | GOES-19 | NOVO ARIPUANÃ | AMAZONAS | Brasil | 1303304 | 13 | 33 | nan | nan | nan | Amazônia | 96.9 |
| 1480e2f7-8a55-3254-b79a-919ba94d29e2 | -9.1713 | -49.9622 | 2026-08-28 19:00:00 | GOES-19 | SANTANA DO ARAGUAIA | PARÁ | Brasil | 1506708 | 15 | 33 | nan | nan | nan | Amazônia | 81.4 |
| d1303dbc-425b-3afd-a397-0835923c8cf9 | -4.3205 | -59.4821 | 2026-08-28 19:00:00 | GOES-19 | BORBA | AMAZONAS | Brasil | 1300805 | 13 | 33 | nan | nan | nan | Amazônia | 61.9 |
| a24f86ef-69c5-3b2c-a430-26016fc4ac18 | -7.4734 | -61.4037 | 2026-08-28 19:00:00 | GOES-19 | MANICORÉ | AMAZONAS | Brasil | 1302702 | 13 | 33 | nan | nan | nan | Amazônia | 108.7 |
| 0bf46359-ad8e-3b58-8e10-118e352f2475 | -11.2128 | -53.9976 | 2026-08-28 19:00:00 | GOES-19 | MARCELÂNDIA | MATO GROSSO | Brasil | 5105580 | 51 | 33 | nan | nan | nan | Amazônia | 94.9 |
| 5d238fb7-748f-3421-a4ec-4736c97cf87e | -6.8542 | -59.9372 | 2026-08-28 19:00:00 | GOES-19 | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 75.5 |
| e249621a-950e-3f23-8986-774e58ee10bf | -9.1976 | -61.1 | 2026-08-28 19:00:00 | GOES-19 | COLNIZA | MATO GROSSO | Brasil | 5103254 | 51 | 33 | nan | nan | nan | Amazônia | 74.8 |
| 906d44af-fbe5-3411-b0d1-66ee66b23b50 | -7.4953 | -55.2862 | 2026-08-28 19:00:00 | GOES-19 | NOVO PROGRESSO | PARÁ | Brasil | 1505031 | 15 | 33 | nan | nan | nan | Amazônia | 153.4 |
| 0241a17b-6b8a-320f-92fb-cfd72e1fff8e | -14.1838 | -52.8245 | 2026-08-28 19:00:00 | GOES-19 | ÁGUA BOA | MATO GROSSO | Brasil | 5100201 | 51 | 33 | nan | nan | nan | Cerrado | 87.2 |
| 3265d8ed-5fdf-35a4-ae24-017039cda9c5 | -13.5991 | -45.772 | 2026-08-28 19:00:00 | GOES-19 | CORRENTINA | BAHIA | Brasil | 2909307 | 29 | 33 | nan | nan | nan | Cerrado | 121.0 |
| ecf1bfff-260a-3553-98b7-709d54d76126 | -7.529 | -61.3635 | 2026-08-28 19:00:00 | GOES-19 | MANICORÉ | AMAZONAS | Brasil | 1302702 | 13 | 33 | nan | nan | nan | Amazônia | 107.3 |
| 8a94dfd4-23c9-38b1-9576-454c90744d8c | -11.2317 | -53.9958 | 2026-08-28 19:00:00 | GOES-19 | MARCELÂNDIA | MATO GROSSO | Brasil | 5105580 | 51 | 33 | nan | nan | nan | Amazônia | 125.2 |
| 572451a9-f250-305b-baa0-b3fb2c37c7c4 | -8.0928 | -45.8354 | 2026-08-28 19:00:00 | GOES-19 | BALSAS | MARANHÃO | Brasil | 2101400 | 21 | 33 | nan | nan | nan | Cerrado | 70.0 |
| 6c921678-f5e4-3a06-ab47-ca597b5d41ec | -9.1978 | -61.0809 | 2026-08-28 19:00:00 | GOES-19 | COLNIZA | MATO GROSSO | Brasil | 5103254 | 51 | 33 | nan | nan | nan | Amazônia | 81.2 |
| 02ea7ad1-2af8-3bfa-be50-3fe3023f7f32 | -5.9996 | -57.8249 | 2026-08-28 19:00:00 | GOES-19 | JACAREACANGA | PARÁ | Brasil | 1503754 | 15 | 33 | nan | nan | nan | Amazônia | 73.7 |
| 7d95f1c8-9cbb-3847-9186-6cad88352d1e | -9.1714 | -59.5793 | 2026-08-28 19:00:00 | GOES-19 | COLNIZA | MATO GROSSO | Brasil | 5103254 | 51 | 33 | nan | nan | nan | Amazônia | 73.3 |
| f29adb62-3dac-325f-8ec4-ee31145c9a78 | -6.9336 | -58.9514 | 2026-08-28 19:00:00 | GOES-19 | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 169.0 |
| ddfdd1df-fdf9-35bc-b2ab-e604927d0ef9 | -14.3372 | -51.7234 | 2026-08-28 19:00:00 | GOES-19 | NOVA NAZARÉ | MATO GROSSO | Brasil | 5106174 | 51 | 33 | nan | nan | nan | Cerrado | 312.3 |
| 5fcbcaeb-a79b-3ee3-95ae-76f129a99e36 | -9.1102 | -60.3166 | 2026-08-28 19:00:00 | GOES-19 | COLNIZA | MATO GROSSO | Brasil | 5103254 | 51 | 33 | nan | nan | nan | Amazônia | 59.1 |
| 6dd40676-d832-3da9-9c44-d8d555ff11f3 | -14.1645 | -52.8269 | 2026-08-28 19:00:00 | GOES-19 | ÁGUA BOA | MATO GROSSO | Brasil | 5100201 | 51 | 33 | nan | nan | nan | Cerrado | 76.1 |
| fc46bae0-d40a-32f0-a055-dd305ce12ac9 | -4.3205 | -59.463 | 2026-08-28 19:00:00 | GOES-19 | BORBA | AMAZONAS | Brasil | 1300805 | 13 | 33 | nan | nan | nan | Amazônia | 55.2 |
| bb88d15a-effb-3d1f-a2bc-29ec9ed68c08 | -15.6139 | -56.4103 | 2026-08-28 19:00:00 | GOES-19 | NOSSA SENHORA DO LIVRAMENTO | MATO GROSSO | Brasil | 5106109 | 51 | 33 | nan | nan | nan | Cerrado | 54.1 |
| 9bfa51b8-3586-3c6e-bd66-c4d843a2c2f9 | -7.0041 | -59.5275 | 2026-08-28 19:00:00 | GOES-19 | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 79.8 |
| e01fbaef-be3b-392f-8ee4-fc9c344b3146 | -13.4707 | -57.0574 | 2026-08-28 19:00:00 | GOES-19 | NOVA MARINGÁ | MATO GROSSO | Brasil | 5108907 | 51 | 33 | nan | nan | nan | Cerrado | 56.1 |
| 590a8ca3-4255-357d-b40b-432c972b18eb | -7.5289 | -61.3825 | 2026-08-28 19:00:00 | GOES-19 | MANICORÉ | AMAZONAS | Brasil | 1302702 | 13 | 33 | nan | nan | nan | Amazônia | 77.9 |
| 7d81fe20-9429-3b66-91dd-2238beca9036 | -10.3202 | -49.9782 | 2026-08-28 19:00:00 | GOES-19 | PIUM | TOCANTINS | Brasil | 1717503 | 17 | 33 | nan | nan | nan | Cerrado | 89.0 |
| 72b09a6b-1047-3a38-a2ed-bfaea11a72bf | -9.0012 | -57.5585 | 2026-08-28 19:00:00 | GOES-19 | APIACÁS | MATO GROSSO | Brasil | 5100805 | 51 | 33 | nan | nan | nan | Amazônia | 97.3 |
| e6df81e3-4270-3a77-9371-68255f57bec2 | -9.8034 | -46.3279 | 2026-08-28 19:00:00 | GOES-19 | ALTO PARNAÍBA | MARANHÃO | Brasil | 2100501 | 21 | 33 | nan | nan | nan | Cerrado | 82.0 |
| 5ec03acd-4090-3548-980f-ea0b98bd4305 | -6.8571 | -59.4179 | 2026-08-28 19:00:00 | GOES-19 | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 74.6 |
| 901aa479-ca77-34e0-bef4-b1c4eb80ef7f | -9.4329 | -51.6926 | 2026-08-28 19:00:00 | GOES-19 | SÃO FÉLIX DO XINGU | PARÁ | Brasil | 1507300 | 15 | 33 | nan | nan | nan | Amazônia | 127.2 |
| 6e06c8fc-c835-3d44-83cc-7ee6a0c482eb | -6.5323 | -55.2378 | 2026-08-28 19:00:00 | GOES-19 | ITAITUBA | PARÁ | Brasil | 1503606 | 15 | 33 | nan | nan | nan | Amazônia | 100.9 |
| ac60f63f-9c98-376f-a8eb-f9a141823060 | -4.3022 | -59.4634 | 2026-08-28 19:00:00 | GOES-19 | BORBA | AMAZONAS | Brasil | 1300805 | 13 | 33 | nan | nan | nan | Amazônia | 81.3 |
| 358b5d8e-ce17-3829-9af5-06c87bdd85cd | -6.0005 | -57.6689 | 2026-08-28 19:00:00 | GOES-19 | JACAREACANGA | PARÁ | Brasil | 1503754 | 15 | 33 | nan | nan | nan | Amazônia | 71.1 |
| 5d021d54-62d7-3129-9fc0-88bff7ab2868 | -9.1711 | -49.9835 | 2026-08-28 19:00:00 | GOES-19 | SANTANA DO ARAGUAIA | PARÁ | Brasil | 1506708 | 15 | 33 | nan | nan | nan | Amazônia | 91.8 |
| c1bf42db-4a1d-3543-b697-88fc445fb6e7 | -14.3376 | -51.702 | 2026-08-28 19:00:00 | GOES-19 | NOVA NAZARÉ | MATO GROSSO | Brasil | 5106174 | 51 | 33 | nan | nan | nan | Cerrado | 341.6 |
| 3e9ef923-b721-39d0-bfdf-ef38207429d6 | -11.0247 | -49.6656 | 2026-08-28 19:00:00 | GOES-19 | SANTA RITA DO TOCANTINS | TOCANTINS | Brasil | 1718899 | 17 | 33 | nan | nan | nan | Cerrado | 63.9 |
| 3e5f89b9-16a2-3035-8a9d-c47c0045df9a | -7.4735 | -61.3846 | 2026-08-28 19:00:00 | GOES-19 | MANICORÉ | AMAZONAS | Brasil | 1302702 | 13 | 33 | nan | nan | nan | Amazônia | 85.5 |
| b91d8ea5-e0b1-3745-bf27-d04687f58750 | -7.3663 | -55.1734 | 2026-08-28 19:00:00 | GOES-19 | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 93.7 |
| 492e6de0-36fe-3031-adc6-226c95094315 | -8.5975 | -54.715 | 2026-08-28 19:00:00 | GOES-19 | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 83.6 |
| 0378aa77-5504-34f8-b403-fed63b43e0cf | -6.1841 | -57.7786 | 2026-08-28 19:00:00 | GOES-19 | JACAREACANGA | PARÁ | Brasil | 1503754 | 15 | 33 | nan | nan | nan | Amazônia | 70.0 |
| de9839a8-2e29-36f9-90b7-3c4ec163d8e3 | -9.1895 | -59.6364 | 2026-08-28 19:00:00 | GOES-19 | COLNIZA | MATO GROSSO | Brasil | 5103254 | 51 | 33 | nan | nan | nan | Amazônia | 74.1 |
| 0f550084-3c98-3e0a-8224-1a1b13970034 | -8.0737 | -45.8598 | 2026-08-28 19:00:00 | GOES-19 | BALSAS | MARANHÃO | Brasil | 2101400 | 21 | 33 | nan | nan | nan | Cerrado | 81.1 |


[Clique aqui para ver as próximas entradas](README168.md)
