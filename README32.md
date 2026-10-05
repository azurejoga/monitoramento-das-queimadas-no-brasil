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

## Dados Diários - Página 32

| ID | Latitude | Longitude | Data/Hora GMT | Satélite | Município | Estado | País | Município ID | Estado ID | País ID | Dias sem Chuva | Precipitação | Risco de Fogo | Bioma | FRP |
|----|----------|-----------|---------------|----------|-----------|--------|------|--------------|-----------|---------|----------------|--------------|----------------|-------|-----|
| 164294d6-8fa7-34b9-b3b0-4ab547a5c44d | -2.88203 | -51.0359 | 2026-10-05 04:57:00 | NOAA-20 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 2.3 |
| 72a28f05-8086-31dc-b6d0-358c6829dc2e | -8.27695 | -47.91565 | 2026-10-05 04:57:00 | NOAA-20 | ITACAJÁ | TOCANTINS | Brasil | 1710508 | 17 | 33 | nan | nan | nan | Cerrado | 0.6 |
| e52dda2c-106d-34a5-af7b-075b65873593 | -3.26987 | -50.39902 | 2026-10-05 04:57:00 | NOAA-20 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 11.6 |
| 64cfa4ed-3d8f-3b61-a91d-75e49bb9c425 | -3.61103 | -50.97652 | 2026-10-05 04:57:00 | NOAA-20 | PACAJÁ | PARÁ | Brasil | 1505486 | 15 | 33 | nan | nan | nan | Amazônia | 1.1 |
| 04135ded-5dfa-3c38-a631-47b603a3ed22 | -2.80409 | -54.12999 | 2026-10-05 04:57:00 | NOAA-20 | SANTARÉM | PARÁ | Brasil | 1506807 | 15 | 33 | nan | nan | nan | Amazônia | 1.2 |
| e4778d18-343a-395f-9955-faa0e0549b90 | -8.66374 | -54.55026 | 2026-10-05 04:57:00 | NOAA-20 | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 3.5 |
| c1eb1050-63ec-39da-b1a8-8f737b34e0cf | -3.18842 | -54.09741 | 2026-10-05 04:57:00 | NOAA-20 | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | 3.0 |
| 127ad36a-953d-3d77-926b-301f99acb656 | -8.66489 | -54.54311 | 2026-10-05 04:57:00 | NOAA-20 | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 3.7 |
| 133eb735-44aa-36f2-8be1-06a0bfeaf5f0 | -2.91982 | -54.10901 | 2026-10-05 04:57:00 | NOAA-20 | SANTARÉM | PARÁ | Brasil | 1506807 | 15 | 33 | nan | nan | nan | Amazônia | 4.0 |
| c3987301-944a-395f-9ee4-e40b534d2b12 | -6.19973 | -52.82957 | 2026-10-05 04:57:00 | NOAA-20 | SÃO FÉLIX DO XINGU | PARÁ | Brasil | 1507300 | 15 | 33 | nan | nan | nan | Amazônia | 0.4 |
| 61ef9b53-2988-3ef6-bc84-b185af05dd17 | -3.10066 | -53.72468 | 2026-10-05 04:57:00 | NOAA-20 | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | 15.2 |
| dec71ecf-c949-32c5-a281-faf12a3b9a5d | -2.16035 | -53.66163 | 2026-10-05 04:57:00 | NOAA-20 | PRAINHA | PARÁ | Brasil | 1506005 | 15 | 33 | nan | nan | nan | Amazônia | 1.2 |
| b0ffadea-b2a3-3d12-b3fc-67c758465ee8 | -5.99703 | -53.63395 | 2026-10-05 04:57:00 | NOAA-20 | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 3.1 |
| 93e07acf-e3f2-343c-aef0-b097e35c81ce | -3.10172 | -53.73978 | 2026-10-05 04:57:00 | NOAA-20 | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | 5.2 |
| 3d6bd7e0-0265-3e31-9b1f-fc2d61263a75 | -2.48193 | -56.09427 | 2026-10-05 04:57:00 | NOAA-20 | JURUTI | PARÁ | Brasil | 1503903 | 15 | 33 | nan | nan | nan | Amazônia | 1.6 |
| cf8a0c2d-bf0b-3526-af9e-290e19416a54 | -2.15694 | -53.66111 | 2026-10-05 04:57:00 | NOAA-20 | PRAINHA | PARÁ | Brasil | 1506005 | 15 | 33 | nan | nan | nan | Amazônia | 1.2 |
| 233a2427-42e2-311d-b755-ad209df05bc2 | -3.13235 | -53.72225 | 2026-10-05 04:57:00 | NOAA-20 | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | 17.0 |
| 7e270ac8-f438-3c05-a261-945ed8c46249 | -6.91574 | -43.68549 | 2026-10-05 04:57:00 | NOAA-20 | GUADALUPE | PIAUÍ | Brasil | 2204501 | 22 | 33 | nan | nan | nan | Cerrado | 1.8 |
| 90dd583b-22bc-358d-b686-6395f1db604f | -6.26169 | -52.84592 | 2026-10-05 04:57:00 | NOAA-20 | SÃO FÉLIX DO XINGU | PARÁ | Brasil | 1507300 | 15 | 33 | nan | nan | nan | Amazônia | 1.2 |
| 4bf08f00-3c9e-392f-8109-4a673776dc41 | -2.9997 | -54.22156 | 2026-10-05 04:57:00 | NOAA-20 | SANTARÉM | PARÁ | Brasil | 1506807 | 15 | 33 | nan | nan | nan | Amazônia | 3.1 |
| def00b64-2bf3-33c9-adab-9f134b19f97d | -6.91671 | -43.67855 | 2026-10-05 04:57:00 | NOAA-20 | GUADALUPE | PIAUÍ | Brasil | 2204501 | 22 | 33 | nan | nan | nan | Cerrado | 1.9 |
| 0e533056-e813-3002-876d-dad91d9a1be4 | -9.83922 | -44.79662 | 2026-10-05 04:57:00 | NOAA-20 | RIACHO FRIO | PIAUÍ | Brasil | 2208858 | 22 | 33 | nan | nan | nan | Cerrado | 0.6 |
| a9fdc7c9-5bf0-3b29-ad22-de66a050f6fa | -6.61794 | -52.99882 | 2026-10-05 04:57:00 | NOAA-20 | SÃO FÉLIX DO XINGU | PARÁ | Brasil | 1507300 | 15 | 33 | nan | nan | nan | Amazônia | 1.3 |
| 355228a1-ad3e-30a2-98e4-04fa9aaf10f3 | -5.98925 | -53.6399 | 2026-10-05 04:57:00 | NOAA-20 | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 2.4 |
| c3d851a9-588f-33fe-a279-e5cc0316a9f6 | -3.06174 | -54.16565 | 2026-10-05 04:57:00 | NOAA-20 | SANTARÉM | PARÁ | Brasil | 1506807 | 15 | 33 | nan | nan | nan | Amazônia | 6.2 |
| adcecf03-de79-3968-9295-a9e7867aea45 | -3.6425 | -52.04961 | 2026-10-05 04:57:00 | NOAA-20 | SENADOR JOSÉ PORFÍRIO | PARÁ | Brasil | 1507805 | 15 | 33 | nan | nan | nan | Amazônia | 1.2 |
| 6ea8e292-a922-392d-8fa8-f47241739ad3 | -2.90768 | -54.1186 | 2026-10-05 04:57:00 | NOAA-20 | SANTARÉM | PARÁ | Brasil | 1506807 | 15 | 33 | nan | nan | nan | Amazônia | 2.4 |
| 84ce9f9e-3490-3e49-91a4-b60d75df9a39 | -3.0577 | -54.16887 | 2026-10-05 04:57:00 | NOAA-20 | SANTARÉM | PARÁ | Brasil | 1506807 | 15 | 33 | nan | nan | nan | Amazônia | 2.1 |
| d6bb5324-f224-3528-8c78-0c4f3b306435 | -7.43849 | -63.56792 | 2026-10-05 04:57:00 | NOAA-20 | CANUTAMA | AMAZONAS | Brasil | 1300904 | 13 | 33 | nan | nan | nan | Amazônia | 2.5 |
| 48e7a9ec-e1b5-3aeb-8704-8a6530ebff2c | -3.11297 | -53.75651 | 2026-10-05 04:57:00 | NOAA-20 | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | 9.2 |
| 776e8097-8d5d-35fc-bd97-515e28e1c5c1 | -4.17632 | -53.66811 | 2026-10-05 04:57:00 | NOAA-20 | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 0.8 |
| ff227bb7-ed7d-3232-ad69-7309f2a88921 | -2.579 | -51.87814 | 2026-10-05 04:57:00 | NOAA-20 | SENADOR JOSÉ PORFÍRIO | PARÁ | Brasil | 1507805 | 15 | 33 | nan | nan | nan | Amazônia | 0.9 |
| 460291f6-69bc-357c-a71d-3fa0143412d7 | -3.83938 | -52.1368 | 2026-10-05 04:57:00 | NOAA-20 | SENADOR JOSÉ PORFÍRIO | PARÁ | Brasil | 1507805 | 15 | 33 | nan | nan | nan | Amazônia | 1.2 |
| 2045e9d0-73ef-3558-821f-53897c541333 | -6.20575 | -52.79157 | 2026-10-05 04:57:00 | NOAA-20 | SÃO FÉLIX DO XINGU | PARÁ | Brasil | 1507300 | 15 | 33 | nan | nan | nan | Amazônia | 0.7 |
| 311a2e6e-9d67-34bb-b26d-2f1e887180c6 | -6.26281 | -52.86026 | 2026-10-05 04:57:00 | NOAA-20 | SÃO FÉLIX DO XINGU | PARÁ | Brasil | 1507300 | 15 | 33 | nan | nan | nan | Amazônia | 0.7 |
| 52d65660-5549-3042-9c11-8120b19d59e2 | -3.77551 | -51.40153 | 2026-10-05 04:57:00 | NOAA-20 | ANAPU | PARÁ | Brasil | 1500859 | 15 | 33 | nan | nan | nan | Amazônia | 1.7 |
| 63ec100c-64cb-34f6-8396-88ec4f179127 | -5.99258 | -53.64045 | 2026-10-05 04:57:00 | NOAA-20 | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 0.9 |
| cbf459e9-f823-372d-ae40-f873c3875519 | -6.01212 | -53.51775 | 2026-10-05 04:57:00 | NOAA-20 | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 3.2 |
| 290b06fc-f514-3acf-93a6-43f112073c1d | -2.78238 | -54.11114 | 2026-10-05 04:57:00 | NOAA-20 | SANTARÉM | PARÁ | Brasil | 1506807 | 15 | 33 | nan | nan | nan | Amazônia | 2.8 |
| 963db19d-b331-379b-8b43-be08448ff5b7 | -3.10676 | -53.75179 | 2026-10-05 04:57:00 | NOAA-20 | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | 3.0 |
| af2eb397-e505-313b-84fb-0a8fa9e52840 | -2.96576 | -54.10866 | 2026-10-05 04:57:00 | NOAA-20 | SANTARÉM | PARÁ | Brasil | 1506807 | 15 | 33 | nan | nan | nan | Amazônia | 1.6 |
| 1bf9c68b-3f19-3aa9-8986-15e4ec6dfe43 | -2.8122 | -54.12356 | 2026-10-05 04:57:00 | NOAA-20 | SANTARÉM | PARÁ | Brasil | 1506807 | 15 | 33 | nan | nan | nan | Amazônia | 1.2 |
| b9c9e85c-c7ae-3158-8c49-331e8eb0ffdc | -2.81401 | -54.11228 | 2026-10-05 04:57:00 | NOAA-20 | SANTARÉM | PARÁ | Brasil | 1506807 | 15 | 33 | nan | nan | nan | Amazônia | 0.9 |
| cfa2211c-e082-3e58-9ad1-0a3cde232946 | -3.51621 | -54.61101 | 2026-10-05 04:57:00 | NOAA-20 | PLACAS | PARÁ | Brasil | 1505650 | 15 | 33 | nan | nan | nan | Amazônia | 1.2 |
| 063f1663-b128-3035-866f-987acc7eb4e4 | -3.27309 | -50.01801 | 2026-10-05 04:57:00 | NOAA-20 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 0.9 |
| 7b01ba41-284e-3f65-8bfa-6d3a5e23a94d | -2.27154 | -55.83897 | 2026-10-05 04:57:00 | NOAA-20 | JURUTI | PARÁ | Brasil | 1503903 | 15 | 33 | nan | nan | nan | Amazônia | 1.6 |
| 46367da0-18ce-3317-bff4-6668432404d9 | -3.60502 | -55.27162 | 2026-10-05 04:57:00 | NOAA-20 | AVEIRO | PARÁ | Brasil | 1501006 | 15 | 33 | nan | nan | nan | Amazônia | 1.0 |
| eb08b61e-efd4-3b8d-a61d-6f7f47880bbb | -3.67366 | -55.51713 | 2026-10-05 04:57:00 | NOAA-20 | AVEIRO | PARÁ | Brasil | 1501006 | 15 | 33 | nan | nan | nan | Amazônia | 1.6 |
| 0044b9fc-5499-3186-a3c7-200c5a9dc63e | -2.87604 | -54.12212 | 2026-10-05 04:57:00 | NOAA-20 | SANTARÉM | PARÁ | Brasil | 1506807 | 15 | 33 | nan | nan | nan | Amazônia | 1.6 |
| 76d3a359-2508-3a4b-a99e-35e07a7fe2b4 | -3.13856 | -53.72697 | 2026-10-05 04:57:00 | NOAA-20 | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | 1.5 |
| cd93121f-c08b-3a13-9b90-b40dfbe147a8 | -4.10938 | -49.07659 | 2026-10-05 04:57:00 | NOAA-20 | GOIANÉSIA DO PARÁ | PARÁ | Brasil | 1503093 | 15 | 33 | nan | nan | nan | Amazônia | 2.0 |
| 76cc64b4-2139-3d31-becc-d2773fc483d2 | -2.93205 | -54.16493 | 2026-10-05 04:57:00 | NOAA-20 | SANTARÉM | PARÁ | Brasil | 1506807 | 15 | 33 | nan | nan | nan | Amazônia | 2.0 |
| 9f836412-0e79-34f5-b038-8a572cc8e0d2 | -3.12093 | -53.7503 | 2026-10-05 04:57:00 | NOAA-20 | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | 0.9 |
| 03320153-4c09-38b9-a3be-4207c081266c | -2.90907 | -54.0881 | 2026-10-05 04:57:00 | NOAA-20 | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | 4.8 |
| 6c3d580a-1010-3e77-83e7-4934546f1128 | -6.81089 | -55.29592 | 2026-10-05 04:57:00 | NOAA-20 | NOVO PROGRESSO | PARÁ | Brasil | 1505031 | 15 | 33 | nan | nan | nan | Amazônia | 1.5 |
| fd44e58a-f7c8-3896-9b55-d9421302425a | -2.78299 | -54.10738 | 2026-10-05 04:57:00 | NOAA-20 | PRAINHA | PARÁ | Brasil | 1506005 | 15 | 33 | nan | nan | nan | Amazônia | 2.8 |
| 0098a8a0-46a0-3d92-9898-f3f65ee5a9e1 | -2.80428 | -54.10688 | 2026-10-05 04:57:00 | NOAA-20 | PRAINHA | PARÁ | Brasil | 1506005 | 15 | 33 | nan | nan | nan | Amazônia | 1.0 |
| ad0752ff-84d6-395c-a63f-895a7c86f3fa | -8.65703 | -54.54915 | 2026-10-05 04:57:00 | NOAA-20 | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 2.0 |
| 3cdb2903-3aaf-3249-bf81-a340e3c199c6 | -2.9819 | -54.09584 | 2026-10-05 04:57:00 | NOAA-20 | SANTARÉM | PARÁ | Brasil | 1506807 | 15 | 33 | nan | nan | nan | Amazônia | 2.2 |
| c04325e7-1887-3fa7-ac1c-935694a6b57f | -3.04238 | -54.22051 | 2026-10-05 04:57:00 | NOAA-20 | SANTARÉM | PARÁ | Brasil | 1506807 | 15 | 33 | nan | nan | nan | Amazônia | 1.4 |
| 0599086d-6115-3ba1-b7ea-b1013e94ab72 | -3.98835 | -55.81853 | 2026-10-05 04:57:00 | NOAA-20 | AVEIRO | PARÁ | Brasil | 1501006 | 15 | 33 | nan | nan | nan | Amazônia | 5.6 |
| 8e50477a-567f-3573-9bff-0f16ac7c9d90 | -3.8498 | -50.31806 | 2026-10-05 04:57:00 | NOAA-20 | PACAJÁ | PARÁ | Brasil | 1505486 | 15 | 33 | nan | nan | nan | Amazônia | 5.1 |
| 6c7ce0ba-935e-3e42-91c6-5457cc9dc2b3 | -7.43931 | -63.5655 | 2026-10-05 04:57:00 | NOAA-20 | CANUTAMA | AMAZONAS | Brasil | 1300904 | 13 | 33 | nan | nan | nan | Amazônia | 3.2 |
| f08a67bd-e5e8-35a0-a0e0-7fd76fde8450 | -3.10861 | -53.71849 | 2026-10-05 04:57:00 | NOAA-20 | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | 3.2 |
| 68ffcaae-44f2-338e-8a89-95fd550045f3 | -1.55321 | -54.7957 | 2026-10-05 04:57:00 | NOAA-20 | ALENQUER | PARÁ | Brasil | 1500404 | 15 | 33 | nan | nan | nan | Amazônia | 1.5 |
| 9a8fb668-9278-3863-a374-6001ba73a794 | -2.90707 | -54.12235 | 2026-10-05 04:57:00 | NOAA-20 | SANTARÉM | PARÁ | Brasil | 1506807 | 15 | 33 | nan | nan | nan | Amazônia | 2.4 |
| 033a8754-2d1b-38cd-a18e-b9e69b1589a6 | -3.19126 | -54.10171 | 2026-10-05 04:57:00 | NOAA-20 | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | 1.2 |
| f1b79109-fba6-3698-a99c-7600a793bd9b | -5.97427 | -55.38528 | 2026-10-05 04:57:00 | NOAA-20 | ITAITUBA | PARÁ | Brasil | 1503606 | 15 | 33 | nan | nan | nan | Amazônia | 1.2 |
| eaeea995-c38d-3220-9028-c2df67a69840 | -6.21843 | -52.79712 | 2026-10-05 04:57:00 | NOAA-20 | SÃO FÉLIX DO XINGU | PARÁ | Brasil | 1507300 | 15 | 33 | nan | nan | nan | Amazônia | 1.1 |
| 5186e553-789e-3084-b0b8-0b3f4312fb82 | -3.83899 | -50.32006 | 2026-10-05 04:57:00 | NOAA-20 | PACAJÁ | PARÁ | Brasil | 1505486 | 15 | 33 | nan | nan | nan | Amazônia | 5.8 |
| 193d50b4-c624-33aa-8aa5-4c9801f5e8ef | -6.90152 | -43.66959 | 2026-10-05 04:57:00 | NOAA-20 | GUADALUPE | PIAUÍ | Brasil | 2204501 | 22 | 33 | nan | nan | nan | Cerrado | 2.8 |
| e4818843-3b89-3e51-9599-e96a09f41481 | -4.26645 | -50.74408 | 2026-10-05 04:57:00 | NOAA-20 | NOVO REPARTIMENTO | PARÁ | Brasil | 1505064 | 15 | 33 | nan | nan | nan | Amazônia | 2.4 |
| 83830539-e56a-305b-8ac4-369b72d3107d | -3.04764 | -54.20974 | 2026-10-05 04:57:00 | NOAA-20 | SANTARÉM | PARÁ | Brasil | 1506807 | 15 | 33 | nan | nan | nan | Amazônia | 3.4 |
| 869e53f5-7621-3884-ab17-0cc635db5dce | -8.65646 | -54.55273 | 2026-10-05 04:57:00 | NOAA-20 | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 2.0 |
| 57318de2-45c2-33ed-ac72-fb18050a215b | -6.06615 | -53.47652 | 2026-10-05 04:57:00 | NOAA-20 | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 0.9 |
| 3063b29b-5808-3b1b-b712-96b24ee53fa4 | -2.98475 | -54.10013 | 2026-10-05 04:57:00 | NOAA-20 | SANTARÉM | PARÁ | Brasil | 1506807 | 15 | 33 | nan | nan | nan | Amazônia | 16.8 |
| f8853ca9-8269-3f57-b164-980e38b74be8 | -2.96292 | -54.10434 | 2026-10-05 04:57:00 | NOAA-20 | SANTARÉM | PARÁ | Brasil | 1506807 | 15 | 33 | nan | nan | nan | Amazônia | 1.6 |
| ba799324-bb02-381b-a10a-7c5defa0c1c0 | -3.40905 | -51.80805 | 2026-10-05 04:57:00 | NOAA-20 | VITÓRIA DO XINGU | PARÁ | Brasil | 1508357 | 15 | 33 | nan | nan | nan | Amazônia | 2.0 |
| ee9207c4-736c-326f-8270-a4e9b38bfcdf | -2.92653 | -54.13318 | 2026-10-05 04:57:00 | NOAA-20 | SANTARÉM | PARÁ | Brasil | 1506807 | 15 | 33 | nan | nan | nan | Amazônia | 2.3 |
| f9b3ff13-fd3c-3511-9718-d38795b65aaf | -3.22461 | -54.37344 | 2026-10-05 04:57:00 | NOAA-20 | MOJUÍ DOS CAMPOS | PARÁ | Brasil | 1504752 | 15 | 33 | nan | nan | nan | Amazônia | 1.5 |
| 2b3fd9f4-5349-371c-9498-6b4687e70d23 | -2.97337 | -54.08297 | 2026-10-05 04:57:00 | NOAA-20 | SANTARÉM | PARÁ | Brasil | 1506807 | 15 | 33 | nan | nan | nan | Amazônia | 0.9 |
| babad8cb-e50e-319e-9576-f6ad9011a25b | -7.49882 | -54.98808 | 2026-10-05 04:57:00 | NOAA-20 | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 2.5 |
| 4b0f9227-07b3-398f-9efd-725f499373a1 | -3.58537 | -54.3124 | 2026-10-05 04:57:00 | NOAA-20 | PLACAS | PARÁ | Brasil | 1505650 | 15 | 33 | nan | nan | nan | Amazônia | 1.2 |
| 3d3cb543-5d31-32db-ad0a-aa4fe394c73c | -7.4451 | -63.56659 | 2026-10-05 04:57:00 | NOAA-20 | CANUTAMA | AMAZONAS | Brasil | 1300904 | 13 | 33 | nan | nan | nan | Amazônia | 3.2 |
| e00c6252-34b1-308a-bb68-7f57a7778a50 | -6.0171 | -53.52926 | 2026-10-05 04:57:00 | NOAA-20 | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 2.3 |
| 73f4ab88-82cb-39d8-b7db-b2926b387209 | -6.17337 | -52.93158 | 2026-10-05 04:57:00 | NOAA-20 | SÃO FÉLIX DO XINGU | PARÁ | Brasil | 1507300 | 15 | 33 | nan | nan | nan | Amazônia | 1.6 |
| d5efd6d8-c3b3-380b-9c4d-68018e9f375c | -2.26703 | -55.84297 | 2026-10-05 04:57:00 | NOAA-20 | JURUTI | PARÁ | Brasil | 1503903 | 15 | 33 | nan | nan | nan | Amazônia | 3.0 |
| d2721efe-6edb-337f-86e4-d849ca67d264 | -3.46087 | -54.5907 | 2026-10-05 04:57:00 | NOAA-20 | PLACAS | PARÁ | Brasil | 1505650 | 15 | 33 | nan | nan | nan | Amazônia | 15.5 |
| de300591-41b5-3d82-8e9a-672c6ba1234f | -1.88437 | -56.28107 | 2026-10-05 04:57:00 | NOAA-20 | ORIXIMINÁ | PARÁ | Brasil | 1505304 | 15 | 33 | nan | nan | nan | Amazônia | 6.4 |
| 156fc195-2654-3afe-8206-25f15d6ec3f0 | -2.80651 | -54.11494 | 2026-10-05 04:57:00 | NOAA-20 | SANTARÉM | PARÁ | Brasil | 1506807 | 15 | 33 | nan | nan | nan | Amazônia | 1.1 |
| 72f9d9b9-17b2-3cb5-8b9a-cec4141a1e2d | -2.77328 | -57.65047 | 2026-10-05 04:57:00 | NOAA-20 | URUCURITUBA | AMAZONAS | Brasil | 1304401 | 13 | 33 | nan | nan | nan | Amazônia | 3.5 |
| d30b4e65-acb4-3a3f-8485-996377ac5fae | -1.47159 | -54.53238 | 2026-10-05 04:57:00 | NOAA-20 | MONTE ALEGRE | PARÁ | Brasil | 1504802 | 15 | 33 | nan | nan | nan | Amazônia | 2.2 |
| 9bb559cf-acb2-3ff8-96c5-a4a100c14900 | -2.55933 | -54.72831 | 2026-10-05 04:57:00 | NOAA-20 | SANTARÉM | PARÁ | Brasil | 1506807 | 15 | 33 | nan | nan | nan | Amazônia | 3.2 |
| 996c04c3-1fd0-3cdc-ac2c-8845a48acf2c | -3.32995 | -53.39253 | 2026-10-05 04:57:00 | NOAA-20 | MEDICILÂNDIA | PARÁ | Brasil | 1504455 | 15 | 33 | nan | nan | nan | Amazônia | 4.8 |
| 310e714f-551f-30c9-ad81-bd12d911f6e9 | -3.28971 | -53.83656 | 2026-10-05 04:57:00 | NOAA-20 | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | 1.7 |
| cfd03f15-e4c0-3a31-8210-067263f04198 | -3.8618 | -55.83532 | 2026-10-05 04:57:00 | NOAA-20 | AVEIRO | PARÁ | Brasil | 1501006 | 15 | 33 | nan | nan | nan | Amazônia | 1.9 |
| 8a20002c-19a9-3fd4-8d82-cd518bb722dc | -2.58063 | -51.86784 | 2026-10-05 04:57:00 | NOAA-20 | SENADOR JOSÉ PORFÍRIO | PARÁ | Brasil | 1507805 | 15 | 33 | nan | nan | nan | Amazônia | 1.6 |
| b55dfccb-75b5-3491-9a0d-8e2da07602de | -2.8726 | -54.12158 | 2026-10-05 04:57:00 | NOAA-20 | SANTARÉM | PARÁ | Brasil | 1506807 | 15 | 33 | nan | nan | nan | Amazônia | 1.6 |
| 09884012-4524-32c1-8d2f-6a74143c1995 | -3.1547 | -50.44066 | 2026-10-05 04:57:00 | NOAA-20 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 15.3 |
| 207e792c-80c3-3950-ada9-5b5dfdecfc7c | -3.1058 | -53.71431 | 2026-10-05 04:57:00 | NOAA-20 | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | 13.1 |


[Clique aqui para ver as próximas entradas](README33.md)
