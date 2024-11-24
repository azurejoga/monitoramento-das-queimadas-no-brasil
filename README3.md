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

## Dados Diários - Página 3

| ID | Latitude | Longitude | Data/Hora GMT | Satélite | Município | Estado | País | Município ID | Estado ID | País ID | Dias sem Chuva | Precipitação | Risco de Fogo | Bioma | FRP |
|----|----------|-----------|---------------|----------|-----------|--------|------|--------------|-----------|---------|----------------|--------------|----------------|-------|-----|
| 5a8a3f59-387f-354b-9693-9c9da7feb9d5 | -1.8584 | -47.9245 | 2024-11-24 00:21:00 | METOP-B | CONCÓRDIA DO PARÁ | PARÁ | Brasil | 1502756 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| c3b83f47-68b9-3a3f-a893-ae0f6c4f530d | -2.3801 | -49.092701 | 2024-11-24 00:21:00 | METOP-B | MOJU | PARÁ | Brasil | 1504703 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| 6ee80ff9-6a7d-33d1-a9d1-d24cf1899b7d | -2.37 | -50.376301 | 2024-11-24 00:21:00 | METOP-B | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| 4caf9ef3-6966-342b-a294-f58eddcc60d4 | -2.2623 | -47.387001 | 2024-11-24 00:21:00 | METOP-B | CAPITÃO POÇO | PARÁ | Brasil | 1502301 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| 5a2123c1-1272-3f88-ad5e-2e8b68f256d5 | -2.8548 | -51.806198 | 2024-11-24 00:21:00 | METOP-B | SENADOR JOSÉ PORFÍRIO | PARÁ | Brasil | 1507805 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| 44a2edef-c9fe-3310-b276-0d97b5fb5339 | -3.1645 | -45.289101 | 2024-11-24 00:21:00 | METOP-B | PENALVA | MARANHÃO | Brasil | 2108306 | 21 | 33 | nan | nan | nan | Amazônia | nan |
| 27a77b42-061f-3e9d-a565-3b9f25ab1a42 | -2.1619 | -53.7682 | 2024-11-24 00:21:00 | METOP-B | PRAINHA | PARÁ | Brasil | 1506005 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| 9ffd7bd7-745d-37ab-91fb-09cde3a5ce6e | -2.0469 | -49.718201 | 2024-11-24 00:21:00 | METOP-B | LIMOEIRO DO AJURU | PARÁ | Brasil | 1504000 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| 23a14f8e-a00c-35e3-8fa7-ba0b987b6171 | -3.5002 | -50.457199 | 2024-11-24 00:21:00 | METOP-B | PACAJÁ | PARÁ | Brasil | 1505486 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| 39ace161-72d9-321e-9bd2-256a54f3fa9f | -2.39 | -50.327499 | 2024-11-24 00:21:00 | METOP-B | BAGRE | PARÁ | Brasil | 1501105 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| df3925ac-af21-3a49-b27a-ec0926b29084 | -2.5837 | -49.2192 | 2024-11-24 00:21:00 | METOP-B | MOJU | PARÁ | Brasil | 1504703 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| 360259bd-9780-324d-92a6-c02ed52184b2 | -3.2439 | -54.207199 | 2024-11-24 00:21:00 | METOP-B | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| 93ef0bbc-e00c-3da4-b9bf-a1eb6ef69641 | -2.1722 | -53.630501 | 2024-11-24 00:21:00 | METOP-B | PRAINHA | PARÁ | Brasil | 1506005 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| 09635425-1729-3eb9-b600-cfc3678e5ec4 | -3.0938 | -51.310101 | 2024-11-24 00:21:00 | METOP-B | ANAPU | PARÁ | Brasil | 1500859 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| b4f97675-66d2-3004-98d2-f287821ba9a2 | -3.1685 | -45.306301 | 2024-11-24 00:21:00 | METOP-B | PENALVA | MARANHÃO | Brasil | 2108306 | 21 | 33 | nan | nan | nan | Amazônia | nan |
| 1ba3e0c6-34a0-3544-871f-4166a32efdad | -2.2132 | -49.8619 | 2024-11-24 00:21:00 | METOP-B | OEIRAS DO PARÁ | PARÁ | Brasil | 1505205 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| 794ca324-be2a-31c6-8536-cf131ca9d053 | -1.9555 | -46.852699 | 2024-11-24 00:21:00 | METOP-B | SANTA LUZIA DO PARÁ | PARÁ | Brasil | 1506559 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| 5c23bed0-545c-3131-8b86-e77ffd932356 | -2.0675 | -48.940498 | 2024-11-24 00:21:00 | METOP-B | MOJU | PARÁ | Brasil | 1504703 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| 2ffb27e0-6b9c-34d7-a5f9-45eb5220d888 | -3.308 | -45.690399 | 2024-11-24 00:21:00 | METOP-B | ZÉ DOCA | MARANHÃO | Brasil | 2114007 | 21 | 33 | nan | nan | nan | Amazônia | nan |
| b6af3fb8-28d1-3731-a213-2680364d6262 | -1.8153 | -46.643902 | 2024-11-24 00:21:00 | METOP-B | VISEU | PARÁ | Brasil | 1508308 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| 6e6da97e-fa47-30a6-a767-b393f4103d18 | -3.4789 | -51.977402 | 2024-11-24 00:21:00 | METOP-B | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| 74c8aedc-7c7c-38d5-86a5-2b9e370de601 | -2.158 | -46.655899 | 2024-11-24 00:21:00 | METOP-B | VISEU | PARÁ | Brasil | 1508308 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| f4084aa4-9e8c-33d2-813f-ea426c2bb73f | -3.2365 | -54.220299 | 2024-11-24 00:21:00 | METOP-B | SANTARÉM | PARÁ | Brasil | 1506807 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| 2986b1b2-e118-3648-9c52-d3c3b5eeac89 | -2.0831 | -47.051601 | 2024-11-24 00:21:00 | METOP-B | GARRAFÃO DO NORTE | PARÁ | Brasil | 1503077 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| 43987435-4d1d-3f9a-9be5-bb90229d6cd4 | -2.2373 | -46.8685 | 2024-11-24 00:21:00 | METOP-B | NOVA ESPERANÇA DO PIRIÁ | PARÁ | Brasil | 1504950 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| f8c8f4b6-ae01-3464-8b37-fd62246fe826 | -1.1271 | -48.335899 | 2024-11-24 00:21:00 | METOP-B | BELÉM | PARÁ | Brasil | 1501402 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| 5b199fdc-66f0-37b4-8ccb-b739ec3c0f67 | -2.3104 | -49.058201 | 2024-11-24 00:21:00 | METOP-B | MOJU | PARÁ | Brasil | 1504703 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| b040507a-b4e4-36b5-8c2b-8e53b9637320 | -3.2482 | -53.252998 | 2024-11-24 00:21:00 | METOP-B | MEDICILÂNDIA | PARÁ | Brasil | 1504455 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| f4eed8e4-208c-34bc-aa56-cd6e11505820 | -2.2691 | -50.339298 | 2024-11-24 00:21:00 | METOP-B | BAGRE | PARÁ | Brasil | 1501105 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| beceddcc-2e45-3422-bd04-1f48c33edc55 | -2.2889 | -49.191502 | 2024-11-24 00:21:00 | METOP-B | IGARAPÉ-MIRI | PARÁ | Brasil | 1503309 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| ca6080ed-4586-39c6-86d7-8970c5a5ec27 | -3.1363 | -52.979301 | 2024-11-24 00:21:00 | METOP-B | MEDICILÂNDIA | PARÁ | Brasil | 1504455 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| c5f242f7-fa0f-3712-9cda-9b0367504939 | -1.0149 | -48.067699 | 2024-11-24 00:21:00 | METOP-B | SÃO CAETANO DE ODIVELAS | PARÁ | Brasil | 1507102 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| 10db8f9f-d999-35ec-a638-089654d16816 | -3.0857 | -51.319901 | 2024-11-24 00:21:00 | METOP-B | ANAPU | PARÁ | Brasil | 1500859 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| 1a463a9f-3a57-3777-af58-49261eca3c8e | -2.4472 | -49.070702 | 2024-11-24 00:21:00 | METOP-B | MOJU | PARÁ | Brasil | 1504703 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| 314ed2fb-07ae-3f69-a28e-bc824473f676 | -3.2465 | -50.6576 | 2024-11-24 00:21:00 | METOP-B | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| ca863cef-0372-3223-bb50-7da7c94b2d0d | -2.1451 | -49.101898 | 2024-11-24 00:21:00 | METOP-B | IGARAPÉ-MIRI | PARÁ | Brasil | 1503309 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| 3b242995-8fbe-3b38-b585-e2aa256f0cc9 | -3.084 | -51.312199 | 2024-11-24 00:21:00 | METOP-B | ANAPU | PARÁ | Brasil | 1500859 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| 2a1c73ba-7489-3c54-a302-be44fbfc2e8c | -2.4576 | -49.025501 | 2024-11-24 00:21:00 | METOP-B | MOJU | PARÁ | Brasil | 1504703 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| 19098c2b-abda-3c6b-82b8-864d0d30a58a | -1.4019 | -46.864899 | 2024-11-24 00:21:00 | METOP-B | BRAGANÇA | PARÁ | Brasil | 1501709 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| aa4b8ee8-fb01-3e75-98b5-53c1437e9f53 | -3.1029 | -53.9869 | 2024-11-24 00:21:00 | METOP-B | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| 7d2c7ff9-a89d-3923-a74f-2546e8856cbd | -3.2067 | -52.556198 | 2024-11-24 00:21:00 | METOP-B | BRASIL NOVO | PARÁ | Brasil | 1501725 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| 6104becf-6193-33d4-9c3d-400eef0f937a | -2.615 | -51.791698 | 2024-11-24 00:21:00 | METOP-B | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| 096aa3f9-612f-3c08-aced-952afddd5a43 | -21.120501 | -50.5676 | 2024-11-24 00:21:00 | METOP-B | ARAÇATUBA | SÃO PAULO | Brasil | 3502804 | 35 | 33 | nan | nan | nan | Mata Atlântica | nan |
| 5106a6cc-a688-33ef-bf8e-188d81e087d9 | -3.2175 | -49.792702 | 2024-11-24 00:21:00 | METOP-B | BAIÃO | PARÁ | Brasil | 1501204 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| c2e78441-46d2-36a6-9e4c-bdbf207c1e6d | -2.2835 | -47.298901 | 2024-11-24 00:21:00 | METOP-B | CAPITÃO POÇO | PARÁ | Brasil | 1502301 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| 6e21c859-ceee-300f-b84d-775f9735ea34 | -1.9823 | -46.426899 | 2024-11-24 00:21:00 | METOP-B | CACHOEIRA DO PIRIÁ | PARÁ | Brasil | 1501956 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| de91829f-622a-3cff-91b8-aafa3c86bb27 | -3.7814 | -52.275398 | 2024-11-24 00:21:00 | METOP-B | SENADOR JOSÉ PORFÍRIO | PARÁ | Brasil | 1507805 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| fcde3ae0-d9ec-3464-93bb-806d2dbcfbe7 | -1.8331 | -46.631802 | 2024-11-24 00:21:00 | METOP-B | VISEU | PARÁ | Brasil | 1508308 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| a2162de2-b110-3f7b-823c-561499915b59 | -1.9032 | -48.669102 | 2024-11-24 00:21:00 | METOP-B | MOJU | PARÁ | Brasil | 1504703 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| 1c2a1a0f-ec00-3f88-a7d3-f0f333eebf5c | -3.552 | -51.5201 | 2024-11-24 00:21:00 | METOP-B | ANAPU | PARÁ | Brasil | 1500859 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| ded80492-076e-3780-a6cb-8d92ae1d993f | -1.8198 | -46.618599 | 2024-11-24 00:21:00 | METOP-B | CACHOEIRA DO PIRIÁ | PARÁ | Brasil | 1501956 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| 47032043-12a8-3d64-a83f-f93901e41576 | -3.2915 | -50.352402 | 2024-11-24 00:21:00 | METOP-B | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| 0e203fc4-c6b4-368b-a9fd-66964f2bd255 | -2.128 | -46.6143 | 2024-11-24 00:21:00 | METOP-B | VISEU | PARÁ | Brasil | 1508308 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| 31a1ec40-a8e4-3c2b-85b8-5d9ea810bc31 | -1.0133 | -48.060699 | 2024-11-24 00:21:00 | METOP-B | SÃO CAETANO DE ODIVELAS | PARÁ | Brasil | 1507102 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| d4c14d46-4c41-33c2-a15e-01e416d6608d | -2.7563 | -48.658901 | 2024-11-24 00:21:00 | METOP-B | TAILÂNDIA | PARÁ | Brasil | 1507953 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| 8423dddf-dede-3966-baac-9a9c36f4982e | -2.1641 | -53.778301 | 2024-11-24 00:21:00 | METOP-B | PRAINHA | PARÁ | Brasil | 1506005 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| d2644c92-0f1b-3954-9fd4-08c5ad24ef00 | -3.3061 | -45.682201 | 2024-11-24 00:21:00 | METOP-B | ZÉ DOCA | MARANHÃO | Brasil | 2114007 | 21 | 33 | nan | nan | nan | Amazônia | nan |
| 07605f07-e2b6-31d3-930a-14c74770e4ea | -1.4609 | -46.036598 | 2024-11-24 00:21:00 | METOP-B | CARUTAPERA | MARANHÃO | Brasil | 2102903 | 21 | 33 | nan | nan | nan | Amazônia | nan |
| 5b9016f9-dd9e-3920-8a7e-f47586816bd9 | -2.4503 | -49.084301 | 2024-11-24 00:21:00 | METOP-B | MOJU | PARÁ | Brasil | 1504703 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| 09d97e39-c626-33ab-94df-280c9c50a27a | -3.2931 | -50.359501 | 2024-11-24 00:21:00 | METOP-B | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| aa4a0374-fb36-34d2-96a1-36db52702da6 | -2.0749 | -47.061199 | 2024-11-24 00:21:00 | METOP-B | GARRAFÃO DO NORTE | PARÁ | Brasil | 1503077 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| ac3dd614-8ed2-3c75-af5a-356e30feae30 | -2.2082 | -53.653702 | 2024-11-24 00:21:00 | METOP-B | PRAINHA | PARÁ | Brasil | 1506005 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| 7d0fdbf5-8518-3541-aec8-a8a82ef7ee84 | -3.2406 | -53.264801 | 2024-11-24 00:21:00 | METOP-B | MEDICILÂNDIA | PARÁ | Brasil | 1504455 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| 7c1f5e87-4498-3799-808c-d15121576567 | -2.0846 | -48.879501 | 2024-11-24 00:21:00 | METOP-B | MOJU | PARÁ | Brasil | 1504703 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| 24164b60-8276-3847-9488-a04bced74aea | -1.9538 | -46.8451 | 2024-11-24 00:21:00 | METOP-B | NOVA ESPERANÇA DO PIRIÁ | PARÁ | Brasil | 1504950 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| 0072060a-f062-3fb3-894d-18f51852e041 | -3.6308 | -52.244999 | 2024-11-24 00:21:00 | METOP-B | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| 579f4993-888d-3847-8281-75a1f04ab26f | -3.6705 | -51.729301 | 2024-11-24 00:21:00 | METOP-B | SENADOR JOSÉ PORFÍRIO | PARÁ | Brasil | 1507805 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| 2f8a0579-981a-3277-8cba-237c763e1456 | -2.7383 | -54.099602 | 2024-11-24 00:21:00 | METOP-B | PRAINHA | PARÁ | Brasil | 1506005 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| 0929b0e6-cf0f-3b49-8d04-afd4d9b67d9c | -1.4707 | -46.034401 | 2024-11-24 00:21:00 | METOP-B | CARUTAPERA | MARANHÃO | Brasil | 2102903 | 21 | 33 | nan | nan | nan | Amazônia | nan |
| f3106101-f5e7-3e85-a278-492e638a81e0 | -2.1928 | -49.542198 | 2024-11-24 00:21:00 | METOP-B | CAMETÁ | PARÁ | Brasil | 1502103 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| 0a2d55b0-f208-3a13-810c-cbebc4d2c4e9 | -1.962 | -48.382599 | 2024-11-24 00:21:00 | METOP-B | ACARÁ | PARÁ | Brasil | 1500206 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| 20edbe74-7118-300a-85e1-3c2500220e52 | -3.5538 | -51.528 | 2024-11-24 00:21:00 | METOP-B | ANAPU | PARÁ | Brasil | 1500859 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| 637715ea-19a8-302d-a09b-b06bf6db8dab | -3.1127 | -53.984798 | 2024-11-24 00:21:00 | METOP-B | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| ad51714f-6a2b-3211-82e5-027941a1097b | -1.4726 | -46.042702 | 2024-11-24 00:21:00 | METOP-B | CARUTAPERA | MARANHÃO | Brasil | 2102903 | 21 | 33 | nan | nan | nan | Amazônia | nan |
| 663cac6a-79d1-3a04-b65e-c85d95b314b1 | -2.1716 | -53.766102 | 2024-11-24 00:21:00 | METOP-B | PRAINHA | PARÁ | Brasil | 1506005 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| c35d1ac3-e174-3425-8275-ad33e8d489ca | -2.7465 | -48.661098 | 2024-11-24 00:21:00 | METOP-B | TAILÂNDIA | PARÁ | Brasil | 1507953 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| 5f102e87-22d8-3e53-a0d6-9e59160a6030 | -2.1383 | -46.433102 | 2024-11-24 00:21:00 | METOP-B | CACHOEIRA DO PIRIÁ | PARÁ | Brasil | 1501956 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| 6bd63591-e5b0-36d2-a998-613b40f76de1 | -2.5912 | -54.222099 | 2024-11-24 00:21:00 | METOP-B | PRAINHA | PARÁ | Brasil | 1506005 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| 74215a9a-23f5-3ac6-8a73-92f778f42f1d | -3.2223 | -50.917702 | 2024-11-24 00:21:00 | METOP-B | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| a4a1b44d-3de8-341a-9e38-0a52e29258be | -3.0735 | -50.942501 | 2024-11-24 00:21:00 | METOP-B | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| efbd2435-c3f1-3ab8-968a-13c440e20ea9 | -2.2194 | -46.382099 | 2024-11-24 00:21:00 | METOP-B | CACHOEIRA DO PIRIÁ | PARÁ | Brasil | 1501956 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| 0fcb908d-f825-3c33-b24b-ed4b308e9328 | -2.3089 | -49.051399 | 2024-11-24 00:21:00 | METOP-B | MOJU | PARÁ | Brasil | 1504703 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| 6f21c968-11eb-3ffc-a4d7-d14310581b16 | -3.1989 | -52.5672 | 2024-11-24 00:21:00 | METOP-B | BRASIL NOVO | PARÁ | Brasil | 1501725 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| aeaa3b8f-1afd-39e9-ac35-9562ce3f9994 | -1.4217 | -46.045399 | 2024-11-24 00:21:00 | METOP-B | CARUTAPERA | MARANHÃO | Brasil | 2102903 | 21 | 33 | nan | nan | nan | Amazônia | nan |
| 46c8d1bb-65c6-3971-8b68-65ad92d0dcfc | -7.6832 | -42.9655 | 2024-11-24 00:21:00 | METOP-B | FLORES DO PIAUÍ | PIAUÍ | Brasil | 2203800 | 22 | 33 | nan | nan | nan | Caatinga | nan |
| e1398425-c30a-369f-b650-ddac5defe89a | -1.9703 | -48.373501 | 2024-11-24 00:21:00 | METOP-B | ACARÁ | PARÁ | Brasil | 1500206 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| 69e1e876-3859-3afb-9cb2-fa1a3ff59bc0 | -2.3565 | -49.033699 | 2024-11-24 00:21:00 | METOP-B | MOJU | PARÁ | Brasil | 1504703 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| 4f8ee9ab-445f-3fb6-a3d4-e177a11e7957 | -1.8135 | -46.6362 | 2024-11-24 00:21:00 | METOP-B | VISEU | PARÁ | Brasil | 1508308 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| e40ccff4-6708-30cf-8d29-5412f19ce228 | -2.2877 | -49.048901 | 2024-11-24 00:21:00 | METOP-B | MOJU | PARÁ | Brasil | 1504703 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| 037ff679-7423-3176-9092-46931d2450b3 | -1.1286 | -48.3428 | 2024-11-24 00:21:00 | METOP-B | BELÉM | PARÁ | Brasil | 1501402 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| fcf0352a-411e-3a3f-9c08-a9ffb8e6f95c | -2.4766 | -48.835499 | 2024-11-24 00:21:00 | METOP-B | ACARÁ | PARÁ | Brasil | 1500206 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| 1f2c8ab1-e5dc-3418-906f-53bf416ce773 | -3.5525 | -52.031101 | 2024-11-24 00:21:00 | METOP-B | SENADOR JOSÉ PORFÍRIO | PARÁ | Brasil | 1507805 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| a1d6fcc0-c3d4-31e3-8094-f2d5d6f9941a | -2.4484 | -49.213402 | 2024-11-24 00:21:00 | METOP-B | MOCAJUBA | PARÁ | Brasil | 1504604 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| 9aa7a7e8-fe28-3959-8ce3-7655628332ee | -2.177 | -49.152 | 2024-11-24 00:21:00 | METOP-B | IGARAPÉ-MIRI | PARÁ | Brasil | 1503309 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| 2e882a0b-fbcb-33e6-8444-b2e5c9239f7c | -3.5146 | -53.808701 | 2024-11-24 00:21:00 | METOP-B | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| 8e58fd1f-2c15-3539-a5c7-04ab0f8d3d03 | -2.7375 | -47.528599 | 2024-11-24 00:21:00 | METOP-B | IPIXUNA DO PARÁ | PARÁ | Brasil | 1503457 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| f1f48036-653a-3cec-9eb4-5136aa043d0c | -3.2596 | -52.933102 | 2024-11-24 00:21:00 | METOP-B | MEDICILÂNDIA | PARÁ | Brasil | 1504455 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| 920db818-83af-35dc-b378-f0fe0db74c66 | -1.8697 | -48.156399 | 2024-11-24 00:21:00 | METOP-B | ACARÁ | PARÁ | Brasil | 1500206 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| e5f2b2cc-a87c-3534-8724-6fe3512d9f93 | -3.0344 | -54.001701 | 2024-11-24 00:21:00 | METOP-B | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| ce2f1345-6769-3071-b0f1-4598b821c1e4 | -2.4641 | -49.145599 | 2024-11-24 00:21:00 | METOP-B | MOJU | PARÁ | Brasil | 1504703 | 15 | 33 | nan | nan | nan | Amazônia | nan |


[Clique aqui para ver as próximas entradas](README4.md)
