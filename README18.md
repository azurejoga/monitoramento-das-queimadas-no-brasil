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

## Dados Diários - Página 18

| ID | Latitude | Longitude | Data/Hora GMT | Satélite | Município | Estado | País | Município ID | Estado ID | País ID | Dias sem Chuva | Precipitação | Risco de Fogo | Bioma | FRP |
|----|----------|-----------|---------------|----------|-----------|--------|------|--------------|-----------|---------|----------------|--------------|----------------|-------|-----|
| 4b280f6a-8fa2-37f1-8c99-5181fb89f585 | -17.8038 | -57.5273 | 2024-10-25 02:26:45 | GOES-16 | POCONÉ | MATO GROSSO | Brasil | 5106505 | 51 | 33 | nan | nan | nan | Pantanal | 84.3 |
| 490abc01-37da-3ce2-828f-721f1bee7776 | -17.8042 | -57.5067 | 2024-10-25 02:26:45 | GOES-16 | POCONÉ | MATO GROSSO | Brasil | 5106505 | 51 | 33 | nan | nan | nan | Pantanal | 96.3 |
| 9d63653f-569c-3452-a023-1f1b5af425a4 | -17.9272 | -57.224 | 2024-10-25 02:26:46 | GOES-16 | CORUMBÁ | MATO GROSSO DO SUL | Brasil | 5003207 | 50 | 33 | nan | nan | nan | Pantanal | 87.9 |
| 061c18e3-f306-3997-a47d-ce3cd3bacc0b | -18.1619 | -57.3597 | 2024-10-25 02:26:47 | GOES-16 | CORUMBÁ | MATO GROSSO DO SUL | Brasil | 5003207 | 50 | 33 | nan | nan | nan | Pantanal | 77.7 |
| 077760b5-8a8b-3442-8b21-9aef24ec36d9 | -18.1421 | -57.3622 | 2024-10-25 02:26:47 | GOES-16 | CORUMBÁ | MATO GROSSO DO SUL | Brasil | 5003207 | 50 | 33 | nan | nan | nan | Pantanal | 154.3 |
| c24d1908-2ed8-3045-83e0-6de1b1e8401c | -18.1226 | -57.344 | 2024-10-25 02:26:47 | GOES-16 | CORUMBÁ | MATO GROSSO DO SUL | Brasil | 5003207 | 50 | 33 | nan | nan | nan | Pantanal | 69.0 |
| ad559e67-e282-3052-8560-88eaf2c67b3a | -18.1223 | -57.3647 | 2024-10-25 02:26:47 | GOES-16 | CORUMBÁ | MATO GROSSO DO SUL | Brasil | 5003207 | 50 | 33 | nan | nan | nan | Pantanal | 94.9 |
| b061a1a0-6424-34ca-8d05-baff745b20a1 | -18.0847 | -57.2456 | 2024-10-25 02:26:47 | GOES-16 | CORUMBÁ | MATO GROSSO DO SUL | Brasil | 5003207 | 50 | 33 | nan | nan | nan | Pantanal | 83.0 |
| 6f38f50a-7457-35bd-b659-c82b368f668e | -18.0844 | -57.2663 | 2024-10-25 02:26:47 | GOES-16 | CORUMBÁ | MATO GROSSO DO SUL | Brasil | 5003207 | 50 | 33 | nan | nan | nan | Pantanal | 92.5 |
| 5de56344-0b60-3d37-96df-cd5072e001e2 | -18.0452 | -57.2506 | 2024-10-25 02:26:47 | GOES-16 | CORUMBÁ | MATO GROSSO DO SUL | Brasil | 5003207 | 50 | 33 | nan | nan | nan | Pantanal | 85.8 |
| a87444b2-9f06-34d3-96d0-31262c8a8078 | -18.0441 | -57.3126 | 2024-10-25 02:26:47 | GOES-16 | CORUMBÁ | MATO GROSSO DO SUL | Brasil | 5003207 | 50 | 33 | nan | nan | nan | Pantanal | 132.8 |
| 399eea22-7a72-3ddd-8127-da574570e653 | -18.0434 | -57.3539 | 2024-10-25 02:26:47 | GOES-16 | CORUMBÁ | MATO GROSSO DO SUL | Brasil | 5003207 | 50 | 33 | nan | nan | nan | Pantanal | 87.4 |
| 798587a9-a719-36b4-8d0e-9524d3a742d7 | -18.0431 | -57.3745 | 2024-10-25 02:26:47 | GOES-16 | CORUMBÁ | MATO GROSSO DO SUL | Brasil | 5003207 | 50 | 33 | nan | nan | nan | Pantanal | 84.5 |
| 846ef612-4546-3fb9-8d66-5e12a7a86566 | -1.0445 | -47.6237 | 2024-10-25 02:35:11 | GOES-16 | MARAPANIM | PARÁ | Brasil | 1504406 | 15 | 33 | nan | nan | nan | Amazônia | 63.7 |
| 2d8bba8d-7cf7-3d3d-b366-79b3440a9d45 | -1.211 | -47.5999 | 2024-10-25 02:35:12 | GOES-16 | IGARAPÉ-AÇU | PARÁ | Brasil | 1503200 | 15 | 33 | nan | nan | nan | Amazônia | 34.9 |
| 316d69eb-4081-3b4b-8013-5ae4e05acf8a | -1.1925 | -47.6002 | 2024-10-25 02:35:12 | GOES-16 | IGARAPÉ-AÇU | PARÁ | Brasil | 1503200 | 15 | 33 | nan | nan | nan | Amazônia | 33.2 |
| 5b1bf60c-a112-3b5d-80d6-b6f34be9402e | -2.6297 | -49.247 | 2024-10-25 02:35:20 | GOES-16 | MOJU | PARÁ | Brasil | 1504703 | 15 | 33 | nan | nan | nan | Amazônia | 59.6 |
| 6feff133-4838-3d00-8660-edf1e05b6418 | -2.8145 | -49.2418 | 2024-10-25 02:35:21 | GOES-16 | MOJU | PARÁ | Brasil | 1504703 | 15 | 33 | nan | nan | nan | Amazônia | 79.9 |
| f996d405-47cc-3000-9dbe-0ab543310fab | -2.8144 | -49.2631 | 2024-10-25 02:35:21 | GOES-16 | MOJU | PARÁ | Brasil | 1504703 | 15 | 33 | nan | nan | nan | Amazônia | 62.0 |
| aed19bc1-8a1d-35cd-bd60-fc4500a4564e | -2.796 | -49.2424 | 2024-10-25 02:35:21 | GOES-16 | MOJU | PARÁ | Brasil | 1504703 | 15 | 33 | nan | nan | nan | Amazônia | 59.6 |
| 89ebcc04-d596-302a-9ec7-cc50c41f2fb4 | -2.9578 | -50.4198 | 2024-10-25 02:35:22 | GOES-16 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 55.0 |
| 8d8c4bcc-3c5e-35c1-aad6-75b1015b2357 | -3.2135 | -46.8063 | 2024-10-25 02:35:23 | GOES-16 | PARAGOMINAS | PARÁ | Brasil | 1505502 | 15 | 33 | nan | nan | nan | Amazônia | 121.5 |
| b190f0e0-df1a-3cea-8140-47216de53088 | -3.1949 | -46.807 | 2024-10-25 02:35:23 | GOES-16 | PARAGOMINAS | PARÁ | Brasil | 1505502 | 15 | 33 | nan | nan | nan | Amazônia | 97.8 |
| d9c23b10-9f5a-3426-8397-447f6f24338f | -3.9581 | -46.422 | 2024-10-25 02:35:28 | GOES-16 | BOM JARDIM | MARANHÃO | Brasil | 2102002 | 21 | 33 | nan | nan | nan | Amazônia | 63.6 |
| 03e419e9-854d-32b9-bce7-01e8d27635b5 | -4.2429 | -48.5474 | 2024-10-25 02:35:29 | GOES-16 | RONDON DO PARÁ | PARÁ | Brasil | 1506187 | 15 | 33 | nan | nan | nan | Amazônia | 54.6 |
| dd6f6419-60f9-34c1-8a85-79fca274e368 | -4.5231 | -48.2108 | 2024-10-25 02:35:31 | GOES-16 | RONDON DO PARÁ | PARÁ | Brasil | 1506187 | 15 | 33 | nan | nan | nan | Amazônia | 54.2 |
| b7ece575-9b3c-33d0-87ac-5caf153c7edd | -4.5045 | -48.2117 | 2024-10-25 02:35:31 | GOES-16 | RONDON DO PARÁ | PARÁ | Brasil | 1506187 | 15 | 33 | nan | nan | nan | Amazônia | 51.3 |
| adfc0c51-6563-307e-a8d6-f0033ca2d4bf | -5.9788 | -45.3621 | 2024-10-25 02:35:39 | GOES-16 | FERNANDO FALCÃO | MARANHÃO | Brasil | 2104081 | 21 | 33 | nan | nan | nan | Cerrado | 43.0 |
| 5fca91f3-7d9a-3079-81e1-5a1b8726adba | -6.5219 | -60.0457 | 2024-10-25 02:35:43 | GOES-16 | NOVO ARIPUANÃ | AMAZONAS | Brasil | 1303304 | 13 | 33 | nan | nan | nan | Amazônia | 72.5 |
| e8d1a110-31bd-310d-a0be-d323f4240997 | -11.9824 | -63.9022 | 2024-10-25 02:36:14 | GOES-16 | SÃO FRANCISCO DO GUAPORÉ | RONDÔNIA | Brasil | 1101492 | 11 | 33 | nan | nan | nan | Amazônia | 99.4 |
| 3c4a3580-0522-3965-bf85-74ed0e5b5978 | -11.9822 | -63.9213 | 2024-10-25 02:36:14 | GOES-16 | SÃO FRANCISCO DO GUAPORÉ | RONDÔNIA | Brasil | 1101492 | 11 | 33 | nan | nan | nan | Amazônia | 60.1 |
| 0ef3f7fb-1901-3920-9484-5ebd1110a041 | -12.0011 | -63.9203 | 2024-10-25 02:36:14 | GOES-16 | SÃO FRANCISCO DO GUAPORÉ | RONDÔNIA | Brasil | 1101492 | 11 | 33 | nan | nan | nan | Amazônia | 75.0 |
| 9b3c3e2c-029b-3e27-811c-f4c6d34399cd | -12.0012 | -63.9013 | 2024-10-25 02:36:14 | GOES-16 | SÃO FRANCISCO DO GUAPORÉ | RONDÔNIA | Brasil | 1101492 | 11 | 33 | nan | nan | nan | Amazônia | 141.6 |
| a604bf2d-3c50-3018-91cc-551860b5d90c | -12.3782 | -63.8821 | 2024-10-25 02:36:16 | GOES-16 | COSTA MARQUES | RONDÔNIA | Brasil | 1100080 | 11 | 33 | nan | nan | nan | Amazônia | 71.3 |
| 82958bae-4fbd-34c5-90d9-f51355cc45c5 | -12.4589 | -63.1895 | 2024-10-25 02:36:16 | GOES-16 | SÃO FRANCISCO DO GUAPORÉ | RONDÔNIA | Brasil | 1101492 | 11 | 33 | nan | nan | nan | Amazônia | 57.2 |
| 4855e6e0-57a9-37c7-aa26-01d0f15f9a6a | -12.4591 | -63.1704 | 2024-10-25 02:36:16 | GOES-16 | SÃO FRANCISCO DO GUAPORÉ | RONDÔNIA | Brasil | 1101492 | 11 | 33 | nan | nan | nan | Amazônia | 77.0 |
| 2174142c-1999-338e-987a-fdf36df6422f | -12.478 | -63.1693 | 2024-10-25 02:36:16 | GOES-16 | SÃO FRANCISCO DO GUAPORÉ | RONDÔNIA | Brasil | 1101492 | 11 | 33 | nan | nan | nan | Amazônia | 59.0 |
| fe90e128-ddf1-3f85-8b02-da4343863c20 | -12.5356 | -63.051 | 2024-10-25 02:36:17 | GOES-16 | SÃO FRANCISCO DO GUAPORÉ | RONDÔNIA | Brasil | 1101492 | 11 | 33 | nan | nan | nan | Amazônia | 60.0 |
| f978d00d-0681-3d57-8c8e-1b2c6248cc16 | -13.4957 | -61.6398 | 2024-10-25 02:36:22 | GOES-16 | PIMENTEIRAS DO OESTE | RONDÔNIA | Brasil | 1101468 | 11 | 33 | nan | nan | nan | Amazônia | 53.2 |
| 6f1d8fef-1c6b-33d4-9953-9ca362aed1be | -13.4959 | -61.6203 | 2024-10-25 02:36:22 | GOES-16 | PIMENTEIRAS DO OESTE | RONDÔNIA | Brasil | 1101468 | 11 | 33 | nan | nan | nan | Amazônia | 89.0 |
| 16b24b33-7c37-3e0b-9a00-7fa8a04557d0 | -13.4769 | -61.6217 | 2024-10-25 02:36:22 | GOES-16 | PIMENTEIRAS DO OESTE | RONDÔNIA | Brasil | 1101468 | 11 | 33 | nan | nan | nan | Amazônia | 57.7 |
| a603832f-ce2b-34ae-a189-b3d4f07337c6 | -16.9596 | -57.5245 | 2024-10-25 02:36:41 | GOES-16 | CÁCERES | MATO GROSSO | Brasil | 5102504 | 51 | 33 | nan | nan | nan | Pantanal | 139.3 |
| 5fd4c80f-a197-3d46-b4f4-6189147561f1 | -16.9792 | -57.5223 | 2024-10-25 02:36:41 | GOES-16 | CÁCERES | MATO GROSSO | Brasil | 5102504 | 51 | 33 | nan | nan | nan | Pantanal | 110.4 |
| ee97bfcd-22cd-38bb-ae30-862f57685e71 | -17.0014 | -57.3561 | 2024-10-25 02:36:41 | GOES-16 | POCONÉ | MATO GROSSO | Brasil | 5106505 | 51 | 33 | nan | nan | nan | Pantanal | 89.1 |
| 99a22837-ee17-361f-81fc-9eb7547001a8 | -17.0381 | -57.5155 | 2024-10-25 02:36:41 | GOES-16 | CÁCERES | MATO GROSSO | Brasil | 5102504 | 51 | 33 | nan | nan | nan | Pantanal | 106.5 |
| 9a9651a7-6877-3c75-9827-6ceb59de9946 | -17.039 | -57.454 | 2024-10-25 02:36:41 | GOES-16 | CÁCERES | MATO GROSSO | Brasil | 5102504 | 51 | 33 | nan | nan | nan | Pantanal | 95.6 |
| ed917ec9-5914-3507-b6a2-fb671415917c | -17.0586 | -57.4517 | 2024-10-25 02:36:41 | GOES-16 | CÁCERES | MATO GROSSO | Brasil | 5102504 | 51 | 33 | nan | nan | nan | Pantanal | 95.7 |
| f5c7bd2d-30d0-31c0-a81e-8eb07e995aa9 | -17.0786 | -57.429 | 2024-10-25 02:36:41 | GOES-16 | CÁCERES | MATO GROSSO | Brasil | 5102504 | 51 | 33 | nan | nan | nan | Pantanal | 87.1 |
| 1efe309f-e7b9-361a-8a7a-94e76cd5dd4e | -17.2186 | -57.2485 | 2024-10-25 02:36:42 | GOES-16 | POCONÉ | MATO GROSSO | Brasil | 5106505 | 51 | 33 | nan | nan | nan | Pantanal | 82.9 |
| f1709284-cc33-3dab-aef4-55891149dffd | -17.2386 | -57.2256 | 2024-10-25 02:36:42 | GOES-16 | POCONÉ | MATO GROSSO | Brasil | 5106505 | 51 | 33 | nan | nan | nan | Pantanal | 101.9 |
| 2526b120-f5b2-3fe2-b249-1baf7c31de1a | -17.2537 | -57.5108 | 2024-10-25 02:36:42 | GOES-16 | CÁCERES | MATO GROSSO | Brasil | 5102504 | 51 | 33 | nan | nan | nan | Pantanal | 104.3 |
| 86f7df3e-a139-3528-b71d-42fa728c8213 | -17.7644 | -57.532 | 2024-10-25 02:36:45 | GOES-16 | POCONÉ | MATO GROSSO | Brasil | 5106505 | 51 | 33 | nan | nan | nan | Pantanal | 87.6 |
| 61fb6e41-a36c-3dce-b94f-f6e24e9f3c4a | -17.7671 | -57.3673 | 2024-10-25 02:36:45 | GOES-16 | POCONÉ | MATO GROSSO | Brasil | 5106505 | 51 | 33 | nan | nan | nan | Pantanal | 84.3 |
| a818709b-0566-31ec-bd5e-59fe7e7513d9 | -17.8038 | -57.5273 | 2024-10-25 02:36:45 | GOES-16 | POCONÉ | MATO GROSSO | Brasil | 5106505 | 51 | 33 | nan | nan | nan | Pantanal | 85.7 |
| 5b3fe410-fc1d-3ad4-90bf-8ab7c21d6e39 | -17.8042 | -57.5067 | 2024-10-25 02:36:45 | GOES-16 | POCONÉ | MATO GROSSO | Brasil | 5106505 | 51 | 33 | nan | nan | nan | Pantanal | 88.2 |
| c62ac42d-aeab-3336-8b43-ead38bc2f24c | -17.9272 | -57.224 | 2024-10-25 02:36:46 | GOES-16 | CORUMBÁ | MATO GROSSO DO SUL | Brasil | 5003207 | 50 | 33 | nan | nan | nan | Pantanal | 90.3 |
| 121872e7-c8e3-3523-b23b-b42663de4248 | -17.9071 | -57.2472 | 2024-10-25 02:36:46 | GOES-16 | CORUMBÁ | MATO GROSSO DO SUL | Brasil | 5003207 | 50 | 33 | nan | nan | nan | Pantanal | 84.3 |
| f3dc0893-0cd7-37d8-b937-8235d2480117 | -18.1421 | -57.3622 | 2024-10-25 02:36:47 | GOES-16 | CORUMBÁ | MATO GROSSO DO SUL | Brasil | 5003207 | 50 | 33 | nan | nan | nan | Pantanal | 105.0 |
| 483c1191-dd7c-372f-bc8c-a887467975e4 | -18.1226 | -57.344 | 2024-10-25 02:36:47 | GOES-16 | CORUMBÁ | MATO GROSSO DO SUL | Brasil | 5003207 | 50 | 33 | nan | nan | nan | Pantanal | 61.6 |
| 3e55a685-844d-3204-842f-f29e129a5b7b | -18.1223 | -57.3647 | 2024-10-25 02:36:47 | GOES-16 | CORUMBÁ | MATO GROSSO DO SUL | Brasil | 5003207 | 50 | 33 | nan | nan | nan | Pantanal | 82.4 |
| c64c73dc-55c4-3e2f-aee8-83fd9d5a1a8e | -18.0847 | -57.2456 | 2024-10-25 02:36:47 | GOES-16 | CORUMBÁ | MATO GROSSO DO SUL | Brasil | 5003207 | 50 | 33 | nan | nan | nan | Pantanal | 93.8 |
| 83233c32-c855-3698-8b0a-36e32a8370ee | -18.0844 | -57.2663 | 2024-10-25 02:36:47 | GOES-16 | CORUMBÁ | MATO GROSSO DO SUL | Brasil | 5003207 | 50 | 33 | nan | nan | nan | Pantanal | 98.0 |
| 9569c64e-75f8-3b7d-981b-4879614b8570 | -18.065 | -57.2481 | 2024-10-25 02:36:47 | GOES-16 | CORUMBÁ | MATO GROSSO DO SUL | Brasil | 5003207 | 50 | 33 | nan | nan | nan | Pantanal | 81.5 |
| 7c4803ab-b87f-3e4b-ada5-2aac14a8f199 | -18.0452 | -57.2506 | 2024-10-25 02:36:47 | GOES-16 | CORUMBÁ | MATO GROSSO DO SUL | Brasil | 5003207 | 50 | 33 | nan | nan | nan | Pantanal | 90.1 |
| c39dd300-0b35-3f1b-b53a-d0ceb2486f11 | -18.0441 | -57.3126 | 2024-10-25 02:36:47 | GOES-16 | CORUMBÁ | MATO GROSSO DO SUL | Brasil | 5003207 | 50 | 33 | nan | nan | nan | Pantanal | 126.9 |
| 8eb08cd6-e119-3048-8a85-1f3ff44c9983 | -18.0438 | -57.3332 | 2024-10-25 02:36:47 | GOES-16 | CORUMBÁ | MATO GROSSO DO SUL | Brasil | 5003207 | 50 | 33 | nan | nan | nan | Pantanal | 82.6 |
| 415e9af2-a5ce-315c-ab2e-1e8c9596c627 | -18.0434 | -57.3539 | 2024-10-25 02:36:47 | GOES-16 | CORUMBÁ | MATO GROSSO DO SUL | Brasil | 5003207 | 50 | 33 | nan | nan | nan | Pantanal | 85.3 |
| a435d2a7-75af-3344-acae-775ef277d10d | -18.0431 | -57.3745 | 2024-10-25 02:36:47 | GOES-16 | CORUMBÁ | MATO GROSSO DO SUL | Brasil | 5003207 | 50 | 33 | nan | nan | nan | Pantanal | 87.6 |
| b9ef9388-f113-39ab-b359-fd99e86ff459 | -18.3401 | -56.2168 | 2024-10-25 02:36:48 | GOES-16 | CORUMBÁ | MATO GROSSO DO SUL | Brasil | 5003207 | 50 | 33 | nan | nan | nan | Pantanal | 56.4 |
| 106d6e14-527f-3101-832b-2733d0365012 | -18.3398 | -56.2377 | 2024-10-25 02:36:48 | GOES-16 | CORUMBÁ | MATO GROSSO DO SUL | Brasil | 5003207 | 50 | 33 | nan | nan | nan | Pantanal | 71.7 |
| 8086d822-f1f0-39d6-86d8-d10f869c0709 | -18.3012 | -56.1804 | 2024-10-25 02:36:48 | GOES-16 | CORUMBÁ | MATO GROSSO DO SUL | Brasil | 5003207 | 50 | 33 | nan | nan | nan | Pantanal | 59.1 |
| 97deafc1-aa42-398f-b25f-4ea317892871 | -1.211 | -47.5999 | 2024-10-25 02:45:12 | GOES-16 | IGARAPÉ-AÇU | PARÁ | Brasil | 1503200 | 15 | 33 | nan | nan | nan | Amazônia | 41.2 |
| add38364-22e6-3fab-a134-9c889e13c503 | -1.1925 | -47.6002 | 2024-10-25 02:45:12 | GOES-16 | IGARAPÉ-AÇU | PARÁ | Brasil | 1503200 | 15 | 33 | nan | nan | nan | Amazônia | 26.2 |
| 934a4149-34ad-3d9c-a28e-1d62f3766fb6 | -1.1834 | -53.6569 | 2024-10-25 02:45:12 | GOES-16 | PRAINHA | PARÁ | Brasil | 1506005 | 15 | 33 | nan | nan | nan | Amazônia | 44.6 |
| 9b63ba06-ba00-3703-9a82-9efe3347146d | -2.8145 | -49.2418 | 2024-10-25 02:45:21 | GOES-16 | MOJU | PARÁ | Brasil | 1504703 | 15 | 33 | nan | nan | nan | Amazônia | 68.2 |
| c19cdb66-21fb-3469-b0f9-91c52fac45be | -2.8144 | -49.2631 | 2024-10-25 02:45:21 | GOES-16 | MOJU | PARÁ | Brasil | 1504703 | 15 | 33 | nan | nan | nan | Amazônia | 59.8 |
| f64e04ce-38af-305b-8d9c-8fa82e336516 | -2.796 | -49.2424 | 2024-10-25 02:45:21 | GOES-16 | MOJU | PARÁ | Brasil | 1504703 | 15 | 33 | nan | nan | nan | Amazônia | 59.5 |
| c56f9cfb-ffe1-3d18-9208-eaeb19f53b32 | -3.1949 | -46.807 | 2024-10-25 02:45:23 | GOES-16 | PARAGOMINAS | PARÁ | Brasil | 1505502 | 15 | 33 | nan | nan | nan | Amazônia | 74.7 |
| c2f01593-3c47-334a-a25e-668510f1cb31 | -3.2135 | -46.8063 | 2024-10-25 02:45:23 | GOES-16 | PARAGOMINAS | PARÁ | Brasil | 1505502 | 15 | 33 | nan | nan | nan | Amazônia | 146.1 |
| 05e282e3-8698-3873-b870-8f5a94888f8f | -3.9581 | -46.422 | 2024-10-25 02:45:28 | GOES-16 | BOM JARDIM | MARANHÃO | Brasil | 2102002 | 21 | 33 | nan | nan | nan | Amazônia | 72.3 |
| 84d49d2b-1d2e-3aea-be9d-fbfbf83d8197 | -3.958 | -46.4442 | 2024-10-25 02:45:28 | GOES-16 | BOM JARDIM | MARANHÃO | Brasil | 2102002 | 21 | 33 | nan | nan | nan | Amazônia | 59.8 |
| 2d161b1a-0ff8-3db4-84c9-16320c1f26b6 | -4.7686 | -47.5686 | 2024-10-25 02:45:32 | GOES-16 | AÇAILÂNDIA | MARANHÃO | Brasil | 2100055 | 21 | 33 | nan | nan | nan | Amazônia | 29.1 |
| 44520bc8-643f-3052-ad76-7f9b3b1a1cb4 | -5.9788 | -45.3621 | 2024-10-25 02:45:39 | GOES-16 | FERNANDO FALCÃO | MARANHÃO | Brasil | 2104081 | 21 | 33 | nan | nan | nan | Cerrado | 32.2 |
| 09ffb826-6091-3810-8071-9072bb120b2b | -6.5219 | -60.0457 | 2024-10-25 02:45:43 | GOES-16 | NOVO ARIPUANÃ | AMAZONAS | Brasil | 1303304 | 13 | 33 | nan | nan | nan | Amazônia | 75.7 |
| 46a868b0-0f5f-3b4c-b358-12fc32cda626 | -9.5343 | -40.3282 | 2024-10-25 02:45:58 | GOES-16 | JUAZEIRO | BAHIA | Brasil | 2918407 | 29 | 33 | nan | nan | nan | Caatinga | 96.2 |
| 65391154-74e6-3cba-9f9f-c3e4e1148029 | -9.5339 | -40.3531 | 2024-10-25 02:45:58 | GOES-16 | JUAZEIRO | BAHIA | Brasil | 2918407 | 29 | 33 | nan | nan | nan | Caatinga | 76.2 |
| ec20d1ae-6d4a-3653-b413-d9035573ff17 | -12.0012 | -63.9013 | 2024-10-25 02:46:14 | GOES-16 | SÃO FRANCISCO DO GUAPORÉ | RONDÔNIA | Brasil | 1101492 | 11 | 33 | nan | nan | nan | Amazônia | 115.9 |
| 0a55a3c9-c95a-35e1-a556-f7062761f6ed | -12.0011 | -63.9203 | 2024-10-25 02:46:14 | GOES-16 | SÃO FRANCISCO DO GUAPORÉ | RONDÔNIA | Brasil | 1101492 | 11 | 33 | nan | nan | nan | Amazônia | 69.9 |
| 0ebcce40-fafa-34c0-a621-7fccfb94fd88 | -11.9824 | -63.9022 | 2024-10-25 02:46:14 | GOES-16 | SÃO FRANCISCO DO GUAPORÉ | RONDÔNIA | Brasil | 1101492 | 11 | 33 | nan | nan | nan | Amazônia | 73.9 |
| de49a2d8-e1bc-3a70-9562-91b833eb25b2 | -11.9822 | -63.9213 | 2024-10-25 02:46:14 | GOES-16 | SÃO FRANCISCO DO GUAPORÉ | RONDÔNIA | Brasil | 1101492 | 11 | 33 | nan | nan | nan | Amazônia | 50.8 |
| b1e74be8-3f44-392e-ad78-cae6f02d623b | -12.4589 | -63.1895 | 2024-10-25 02:46:16 | GOES-16 | SÃO FRANCISCO DO GUAPORÉ | RONDÔNIA | Brasil | 1101492 | 11 | 33 | nan | nan | nan | Amazônia | 55.5 |
| c56e4798-5a3e-3fa5-b972-cc791cb160ee | -12.3782 | -63.8821 | 2024-10-25 02:46:16 | GOES-16 | COSTA MARQUES | RONDÔNIA | Brasil | 1100080 | 11 | 33 | nan | nan | nan | Amazônia | 69.4 |
| 9d2f6996-f0be-38cc-aad0-8f391ed7feb8 | -12.4591 | -63.1704 | 2024-10-25 02:46:16 | GOES-16 | SÃO FRANCISCO DO GUAPORÉ | RONDÔNIA | Brasil | 1101492 | 11 | 33 | nan | nan | nan | Amazônia | 76.3 |
| 62bd6e11-7cc0-3394-9bf1-4201e657af3e | -12.478 | -63.1693 | 2024-10-25 02:46:16 | GOES-16 | SÃO FRANCISCO DO GUAPORÉ | RONDÔNIA | Brasil | 1101492 | 11 | 33 | nan | nan | nan | Amazônia | 64.6 |
| 69f38e13-373a-36c8-b071-92cbe98e3226 | -12.5356 | -63.051 | 2024-10-25 02:46:17 | GOES-16 | SÃO FRANCISCO DO GUAPORÉ | RONDÔNIA | Brasil | 1101492 | 11 | 33 | nan | nan | nan | Amazônia | 53.7 |
| 38d14f68-1564-34d1-8b61-30d1290db516 | -13.4959 | -61.6203 | 2024-10-25 02:46:22 | GOES-16 | PIMENTEIRAS DO OESTE | RONDÔNIA | Brasil | 1101468 | 11 | 33 | nan | nan | nan | Amazônia | 82.9 |
| 2a478de1-4637-3e6c-ae0e-57b0a239fe5d | -13.4769 | -61.6217 | 2024-10-25 02:46:22 | GOES-16 | PIMENTEIRAS DO OESTE | RONDÔNIA | Brasil | 1101468 | 11 | 33 | nan | nan | nan | Amazônia | 52.9 |
| 304fea7f-2964-35dd-a1bd-dbef41459b68 | -16.94 | -57.5268 | 2024-10-25 02:46:41 | GOES-16 | CÁCERES | MATO GROSSO | Brasil | 5102504 | 51 | 33 | nan | nan | nan | Pantanal | 78.1 |
| c8f1a2b1-01b0-30fc-812b-ad72036f88b3 | -16.9596 | -57.5245 | 2024-10-25 02:46:41 | GOES-16 | CÁCERES | MATO GROSSO | Brasil | 5102504 | 51 | 33 | nan | nan | nan | Pantanal | 137.8 |
| 73778351-e483-34cc-908c-a41e1e7c5318 | -16.9792 | -57.5223 | 2024-10-25 02:46:41 | GOES-16 | CÁCERES | MATO GROSSO | Brasil | 5102504 | 51 | 33 | nan | nan | nan | Pantanal | 117.1 |


[Clique aqui para ver as próximas entradas](README19.md)
