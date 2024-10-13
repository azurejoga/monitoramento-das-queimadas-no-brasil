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

## Dados Diários - Página 62

| ID | Latitude | Longitude | Data/Hora GMT | Satélite | Município | Estado | País | Município ID | Estado ID | País ID | Dias sem Chuva | Precipitação | Risco de Fogo | Bioma | FRP |
|----|----------|-----------|---------------|----------|-----------|--------|------|--------------|-----------|---------|----------------|--------------|----------------|-------|-----|
| 6ebddb92-162c-37fa-a8a5-610bc82964d3 | -10.31926 | -46.48996 | 2024-10-13 04:40:00 | NOAA-21 | MATEIROS | TOCANTINS | Brasil | 1712702 | 17 | 33 | nan | nan | nan | Cerrado | 1.9 |
| 39ee833f-a858-3112-ba8a-028589ff8010 | -10.26313 | -46.23586 | 2024-10-13 04:40:00 | NOAA-21 | MATEIROS | TOCANTINS | Brasil | 1712702 | 17 | 33 | nan | nan | nan | Cerrado | 1.2 |
| 033d00f6-0135-3152-a589-56be4be769ca | -10.17832 | -46.28966 | 2024-10-13 04:40:00 | NOAA-21 | ALTO PARNAÍBA | MARANHÃO | Brasil | 2100501 | 21 | 33 | nan | nan | nan | Cerrado | 4.9 |
| 16948460-37ef-3ce8-929e-62913c707534 | -10.17806 | -46.28705 | 2024-10-13 04:40:00 | NOAA-21 | ALTO PARNAÍBA | MARANHÃO | Brasil | 2100501 | 21 | 33 | nan | nan | nan | Cerrado | 5.0 |
| 6f13f51a-3ed4-3fdc-adbd-a445aacc98c5 | -10.17295 | -46.29561 | 2024-10-13 04:40:00 | NOAA-21 | ALTO PARNAÍBA | MARANHÃO | Brasil | 2100501 | 21 | 33 | nan | nan | nan | Cerrado | 9.7 |
| 68d5ce9b-555f-3d2b-993a-1d431e3ad328 | -10.16784 | -46.30423 | 2024-10-13 04:40:00 | NOAA-21 | ALTO PARNAÍBA | MARANHÃO | Brasil | 2100501 | 21 | 33 | nan | nan | nan | Cerrado | 5.4 |
| 1bc05fd2-a825-3710-b7a8-cdd8c5055ce4 | -9.95146 | -47.27296 | 2024-10-13 04:40:00 | NOAA-21 | RIO SONO | TOCANTINS | Brasil | 1718758 | 17 | 33 | nan | nan | nan | Cerrado | 2.1 |
| ebdb7727-fb86-3457-aed0-2363309dd234 | -9.94492 | -47.26777 | 2024-10-13 04:40:00 | NOAA-21 | RIO SONO | TOCANTINS | Brasil | 1718758 | 17 | 33 | nan | nan | nan | Cerrado | 1.3 |
| 04c0c7b0-96a4-3410-ae37-e7df485fc312 | -9.94016 | -47.27547 | 2024-10-13 04:40:00 | NOAA-21 | RIO SONO | TOCANTINS | Brasil | 1718758 | 17 | 33 | nan | nan | nan | Cerrado | 1.0 |
| b3645d8c-1808-3940-8c74-9fa444c8ca07 | -9.83816 | -46.99158 | 2024-10-13 04:40:00 | NOAA-21 | LIZARDA | TOCANTINS | Brasil | 1712405 | 17 | 33 | nan | nan | nan | Cerrado | 2.3 |
| b06ab581-1246-3cea-89c8-2f0225c12d01 | -9.7386 | -46.9567 | 2024-10-13 04:40:00 | NOAA-21 | LIZARDA | TOCANTINS | Brasil | 1712405 | 17 | 33 | nan | nan | nan | Cerrado | 2.2 |
| 83dcbe5f-7781-32ec-9a5f-dabc56121a6a | -9.73798 | -46.96092 | 2024-10-13 04:40:00 | NOAA-21 | LIZARDA | TOCANTINS | Brasil | 1712405 | 17 | 33 | nan | nan | nan | Cerrado | 2.2 |
| 16521a9c-52d7-3e26-8b98-0490138c3aa2 | -9.73688 | -46.94343 | 2024-10-13 04:40:00 | NOAA-21 | LIZARDA | TOCANTINS | Brasil | 1712405 | 17 | 33 | nan | nan | nan | Cerrado | 4.1 |
| 9a1c0694-e6fb-3964-b2ca-8b1b9812aa0b | -9.73673 | -46.96929 | 2024-10-13 04:40:00 | NOAA-21 | LIZARDA | TOCANTINS | Brasil | 1712405 | 17 | 33 | nan | nan | nan | Cerrado | 1.3 |
| 654ea26e-ae3d-3344-8236-30a9fe38ffa4 | -9.73562 | -46.95192 | 2024-10-13 04:40:00 | NOAA-21 | LIZARDA | TOCANTINS | Brasil | 1712405 | 17 | 33 | nan | nan | nan | Cerrado | 2.8 |
| 5b1ccc4a-3d39-30c5-9b26-fdcee34d6ed1 | -9.73263 | -46.94712 | 2024-10-13 04:40:00 | NOAA-21 | LIZARDA | TOCANTINS | Brasil | 1712405 | 17 | 33 | nan | nan | nan | Cerrado | 2.8 |
| c8e04ba3-7919-38c8-97a3-45bd066fbd11 | -9.73201 | -46.95136 | 2024-10-13 04:40:00 | NOAA-21 | LIZARDA | TOCANTINS | Brasil | 1712405 | 17 | 33 | nan | nan | nan | Cerrado | 2.8 |
| 4cdca3f6-b78a-3d98-8cfd-cc044d0616c5 | -9.69789 | -46.88133 | 2024-10-13 04:40:00 | NOAA-21 | LIZARDA | TOCANTINS | Brasil | 1712405 | 17 | 33 | nan | nan | nan | Cerrado | 1.0 |
| 3972e2bf-6aea-3e38-8e27-3902415ddaab | -9.52575 | -46.14224 | 2024-10-13 04:40:00 | NOAA-21 | ALTO PARNAÍBA | MARANHÃO | Brasil | 2100501 | 21 | 33 | nan | nan | nan | Cerrado | 1.1 |
| ab8905bd-2d39-306c-a80b-4f573b5794c8 | -12.28161 | -46.78335 | 2024-10-13 04:40:00 | NOAA-21 | PONTE ALTA DO BOM JESUS | TOCANTINS | Brasil | 1717800 | 17 | 33 | nan | nan | nan | Cerrado | 1.3 |
| 20a4cf95-5ac3-3446-a3ce-175535807060 | -12.28045 | -46.78606 | 2024-10-13 04:40:00 | NOAA-21 | PONTE ALTA DO BOM JESUS | TOCANTINS | Brasil | 1717800 | 17 | 33 | nan | nan | nan | Cerrado | 1.3 |
| af3b9e8d-86d4-3006-b462-d9dd84bc3c27 | -12.26348 | -47.15606 | 2024-10-13 04:40:00 | NOAA-21 | CONCEIÇÃO DO TOCANTINS | TOCANTINS | Brasil | 1705607 | 17 | 33 | nan | nan | nan | Cerrado | 3.4 |
| 3c58e98c-0ead-3223-a363-57bfcdb262d6 | -12.19526 | -47.11203 | 2024-10-13 04:40:00 | NOAA-21 | CONCEIÇÃO DO TOCANTINS | TOCANTINS | Brasil | 1705607 | 17 | 33 | nan | nan | nan | Cerrado | 2.5 |
| 67957f36-f177-3005-a008-a24fce7c7afc | -12.18027 | -46.73334 | 2024-10-13 04:40:00 | NOAA-21 | PONTE ALTA DO BOM JESUS | TOCANTINS | Brasil | 1717800 | 17 | 33 | nan | nan | nan | Cerrado | 2.2 |
| 07be8228-cfa3-3758-853c-5bc7f28007c5 | -12.18013 | -46.73143 | 2024-10-13 04:40:00 | NOAA-21 | PONTE ALTA DO BOM JESUS | TOCANTINS | Brasil | 1717800 | 17 | 33 | nan | nan | nan | Cerrado | 1.0 |
| 8005ebea-1091-3f9d-be15-8e7a46a4fdda | -12.17962 | -46.738 | 2024-10-13 04:40:00 | NOAA-21 | PONTE ALTA DO BOM JESUS | TOCANTINS | Brasil | 1717800 | 17 | 33 | nan | nan | nan | Cerrado | 2.2 |
| 9eb718b7-b395-3475-a442-2cdf1f849c00 | -12.17945 | -46.73608 | 2024-10-13 04:40:00 | NOAA-21 | PONTE ALTA DO BOM JESUS | TOCANTINS | Brasil | 1717800 | 17 | 33 | nan | nan | nan | Cerrado | 4.6 |
| 4e4df9df-f5d2-3ae0-a629-f9abf1a63a7e | -12.17649 | -46.73279 | 2024-10-13 04:40:00 | NOAA-21 | PONTE ALTA DO BOM JESUS | TOCANTINS | Brasil | 1717800 | 17 | 33 | nan | nan | nan | Cerrado | 2.7 |
| f944305b-7c10-3691-9e65-57b4df563a94 | -12.17636 | -46.7309 | 2024-10-13 04:40:00 | NOAA-21 | PONTE ALTA DO BOM JESUS | TOCANTINS | Brasil | 1717800 | 17 | 33 | nan | nan | nan | Cerrado | 1.9 |
| 81f1d592-8bf8-353e-a99f-25ad678f3975 | -12.17585 | -46.73746 | 2024-10-13 04:40:00 | NOAA-21 | PONTE ALTA DO BOM JESUS | TOCANTINS | Brasil | 1717800 | 17 | 33 | nan | nan | nan | Cerrado | 2.7 |
| 3ebb5bc7-3c38-3d7d-8153-5e118db85e60 | -12.17568 | -46.73555 | 2024-10-13 04:40:00 | NOAA-21 | PONTE ALTA DO BOM JESUS | TOCANTINS | Brasil | 1717800 | 17 | 33 | nan | nan | nan | Cerrado | 2.8 |
| 627022f5-d693-33fe-b74c-2f8fde30b5f1 | -12.17501 | -46.7402 | 2024-10-13 04:40:00 | NOAA-21 | PONTE ALTA DO BOM JESUS | TOCANTINS | Brasil | 1717800 | 17 | 33 | nan | nan | nan | Cerrado | 2.8 |
| 51580695-7efa-32e8-8dbe-1e4861ec84ba | -12.17272 | -46.73226 | 2024-10-13 04:40:00 | NOAA-21 | PONTE ALTA DO BOM JESUS | TOCANTINS | Brasil | 1717800 | 17 | 33 | nan | nan | nan | Cerrado | 2.7 |
| c50d5252-571c-3127-9329-643c8f0ca99f | -12.17208 | -46.73692 | 2024-10-13 04:40:00 | NOAA-21 | PONTE ALTA DO BOM JESUS | TOCANTINS | Brasil | 1717800 | 17 | 33 | nan | nan | nan | Cerrado | 2.7 |
| b5f69425-4139-3ff8-9095-c8a742eacc9c | -12.17191 | -46.73502 | 2024-10-13 04:40:00 | NOAA-21 | PONTE ALTA DO BOM JESUS | TOCANTINS | Brasil | 1717800 | 17 | 33 | nan | nan | nan | Cerrado | 2.8 |
| f63d375e-8caf-353c-b178-b5c9b0e0792d | -12.16078 | -47.52811 | 2024-10-13 04:40:00 | NOAA-21 | NATIVIDADE | TOCANTINS | Brasil | 1714203 | 17 | 33 | nan | nan | nan | Cerrado | 2.1 |
| c7ecf275-7942-3518-b4fa-f74912c8c01a | -12.16015 | -47.53237 | 2024-10-13 04:40:00 | NOAA-21 | NATIVIDADE | TOCANTINS | Brasil | 1714203 | 17 | 33 | nan | nan | nan | Cerrado | 2.1 |
| e1f86c6e-591d-342f-b437-4e3d1afad36d | -12.15718 | -47.52756 | 2024-10-13 04:40:00 | NOAA-21 | NATIVIDADE | TOCANTINS | Brasil | 1714203 | 17 | 33 | nan | nan | nan | Cerrado | 2.1 |
| 90938c02-4d48-38af-8169-ade022375b07 | -11.99547 | -46.53701 | 2024-10-13 04:40:00 | NOAA-21 | PONTE ALTA DO BOM JESUS | TOCANTINS | Brasil | 1717800 | 17 | 33 | nan | nan | nan | Cerrado | 2.0 |
| 537ace89-fc77-3467-82c3-49ea2c2264ce | -11.99536 | -46.53402 | 2024-10-13 04:40:00 | NOAA-21 | PONTE ALTA DO BOM JESUS | TOCANTINS | Brasil | 1717800 | 17 | 33 | nan | nan | nan | Cerrado | 1.7 |
| a123a217-1f4f-3125-9bef-1986ccaa5705 | -12.53193 | -46.81599 | 2024-10-13 04:40:00 | NOAA-21 | ARRAIAS | TOCANTINS | Brasil | 1702406 | 17 | 33 | nan | nan | nan | Cerrado | 2.0 |
| 21d2e123-aabc-3422-8cc8-0ebfdabe1ad4 | -12.52816 | -46.81543 | 2024-10-13 04:40:00 | NOAA-21 | ARRAIAS | TOCANTINS | Brasil | 1702406 | 17 | 33 | nan | nan | nan | Cerrado | 1.9 |
| 3960c9ea-d508-32cc-b54f-2c09ef53a4e9 | -12.52751 | -46.82008 | 2024-10-13 04:40:00 | NOAA-21 | ARRAIAS | TOCANTINS | Brasil | 1702406 | 17 | 33 | nan | nan | nan | Cerrado | 1.9 |
| adb8f901-eda5-33b4-9c86-e7eb63c7c5d6 | -12.52686 | -46.82471 | 2024-10-13 04:40:00 | NOAA-21 | ARRAIAS | TOCANTINS | Brasil | 1702406 | 17 | 33 | nan | nan | nan | Cerrado | 1.5 |
| 6a5e30ad-db78-3724-8635-64e560d5cd6f | -12.52375 | -46.8195 | 2024-10-13 04:40:00 | NOAA-21 | ARRAIAS | TOCANTINS | Brasil | 1702406 | 17 | 33 | nan | nan | nan | Cerrado | 1.9 |
| fc2fd272-7f6f-3193-a029-7fa169eed78f | -12.5231 | -46.82413 | 2024-10-13 04:40:00 | NOAA-21 | ARRAIAS | TOCANTINS | Brasil | 1702406 | 17 | 33 | nan | nan | nan | Cerrado | 1.5 |
| 0ebe8366-c45f-3fe4-86dc-876a8970f7bf | -12.38617 | -47.31705 | 2024-10-13 04:40:00 | NOAA-21 | CONCEIÇÃO DO TOCANTINS | TOCANTINS | Brasil | 1705607 | 17 | 33 | nan | nan | nan | Cerrado | 5.1 |
| 07aeb88e-2db8-3710-9ccf-1c863369d106 | -12.38188 | -47.32088 | 2024-10-13 04:40:00 | NOAA-21 | CONCEIÇÃO DO TOCANTINS | TOCANTINS | Brasil | 1705607 | 17 | 33 | nan | nan | nan | Cerrado | 4.4 |
| c84a171e-2f12-326b-a8d6-af68ce06dd27 | -12.28549 | -47.65617 | 2024-10-13 04:40:00 | NOAA-21 | PARANÃ | TOCANTINS | Brasil | 1716208 | 17 | 33 | nan | nan | nan | Cerrado | 2.8 |
| 3c3fb53d-cc0e-3cc8-8dc5-f7b678eff0c9 | -12.28488 | -47.66035 | 2024-10-13 04:40:00 | NOAA-21 | PARANÃ | TOCANTINS | Brasil | 1716208 | 17 | 33 | nan | nan | nan | Cerrado | 2.8 |
| ef373fe8-3e8e-3cf6-bd87-dd4e82a2920b | -12.28249 | -47.65143 | 2024-10-13 04:40:00 | NOAA-21 | PARANÃ | TOCANTINS | Brasil | 1716208 | 17 | 33 | nan | nan | nan | Cerrado | 2.0 |
| 33473975-a321-33f3-8d83-4443531bb6fb | -12.28189 | -47.65564 | 2024-10-13 04:40:00 | NOAA-21 | PARANÃ | TOCANTINS | Brasil | 1716208 | 17 | 33 | nan | nan | nan | Cerrado | 2.8 |
| 0c861d39-2466-300a-bf18-bacec7bd2413 | -12.28129 | -47.6598 | 2024-10-13 04:40:00 | NOAA-21 | PARANÃ | TOCANTINS | Brasil | 1716208 | 17 | 33 | nan | nan | nan | Cerrado | 2.8 |
| e21c6bf7-05e5-3cb1-a75a-211c17e95bc8 | -12.2783 | -47.65511 | 2024-10-13 04:40:00 | NOAA-21 | PARANÃ | TOCANTINS | Brasil | 1716208 | 17 | 33 | nan | nan | nan | Cerrado | 4.9 |
| 6b456cfc-d3be-3bab-9e75-b7714b68a734 | -12.2777 | -47.65926 | 2024-10-13 04:40:00 | NOAA-21 | PARANÃ | TOCANTINS | Brasil | 1716208 | 17 | 33 | nan | nan | nan | Cerrado | 4.9 |
| 5210dff9-7c8c-31c5-96af-f960b98f8112 | -12.27591 | -47.64616 | 2024-10-13 04:40:00 | NOAA-21 | PARANÃ | TOCANTINS | Brasil | 1716208 | 17 | 33 | nan | nan | nan | Cerrado | 3.1 |
| 3519a80e-6f8f-3b60-9170-b671ab2ead4c | -12.27531 | -47.65037 | 2024-10-13 04:40:00 | NOAA-21 | PARANÃ | TOCANTINS | Brasil | 1716208 | 17 | 33 | nan | nan | nan | Cerrado | 3.1 |
| 9f2faa3f-a9f0-36ae-a1bf-074b80a644ec | -12.27471 | -47.65456 | 2024-10-13 04:40:00 | NOAA-21 | PARANÃ | TOCANTINS | Brasil | 1716208 | 17 | 33 | nan | nan | nan | Cerrado | 4.9 |
| 44d14897-ecd4-3ea0-b523-95e3ab58242b | -12.27231 | -47.64565 | 2024-10-13 04:40:00 | NOAA-21 | PARANÃ | TOCANTINS | Brasil | 1716208 | 17 | 33 | nan | nan | nan | Cerrado | 3.9 |
| efe395bd-0adf-35f0-9a4a-2c858261cafe | -12.27171 | -47.64984 | 2024-10-13 04:40:00 | NOAA-21 | PARANÃ | TOCANTINS | Brasil | 1716208 | 17 | 33 | nan | nan | nan | Cerrado | 3.9 |
| cc411582-6cf6-36e4-bdb6-9b63eac13303 | -12.27112 | -47.65402 | 2024-10-13 04:40:00 | NOAA-21 | PARANÃ | TOCANTINS | Brasil | 1716208 | 17 | 33 | nan | nan | nan | Cerrado | 3.0 |
| 34629b59-18e4-323f-8a42-62b0e33a96b6 | -12.26872 | -47.64512 | 2024-10-13 04:40:00 | NOAA-21 | PARANÃ | TOCANTINS | Brasil | 1716208 | 17 | 33 | nan | nan | nan | Cerrado | 3.9 |
| 85c11809-c749-33dc-bc69-bd1b3113d7cd | -12.26812 | -47.6493 | 2024-10-13 04:40:00 | NOAA-21 | PARANÃ | TOCANTINS | Brasil | 1716208 | 17 | 33 | nan | nan | nan | Cerrado | 3.9 |
| cba5a98a-8ce1-3d4a-81ce-53030db0666a | -12.26753 | -47.65346 | 2024-10-13 04:40:00 | NOAA-21 | PARANÃ | TOCANTINS | Brasil | 1716208 | 17 | 33 | nan | nan | nan | Cerrado | 3.0 |
| 36e6f06d-c135-3b9a-825b-d1c34787669c | -12.26672 | -47.64573 | 2024-10-13 04:40:00 | NOAA-21 | PARANÃ | TOCANTINS | Brasil | 1716208 | 17 | 33 | nan | nan | nan | Cerrado | 1.8 |
| 4f983066-36c5-3e8b-a22f-b08e281fab4a | -4.99967 | -46.49675 | 2024-10-13 04:40:00 | NOAA-21 | AMARANTE DO MARANHÃO | MARANHÃO | Brasil | 2100600 | 21 | 33 | nan | nan | nan | Amazônia | 1.7 |
| 78ea7f1d-d54d-348a-9b15-d1e997f3ff2d | -4.98062 | -46.80658 | 2024-10-13 04:40:00 | NOAA-21 | AMARANTE DO MARANHÃO | MARANHÃO | Brasil | 2100600 | 21 | 33 | nan | nan | nan | Amazônia | 1.8 |
| 0c776d55-3013-3c5b-90ae-da9e8707a1c6 | -4.97774 | -46.80227 | 2024-10-13 04:40:00 | NOAA-21 | AMARANTE DO MARANHÃO | MARANHÃO | Brasil | 2100600 | 21 | 33 | nan | nan | nan | Amazônia | 3.3 |
| e188fb0f-2d55-314a-844c-7d1eee973fa5 | -4.97716 | -46.80604 | 2024-10-13 04:40:00 | NOAA-21 | AMARANTE DO MARANHÃO | MARANHÃO | Brasil | 2100600 | 21 | 33 | nan | nan | nan | Amazônia | 3.3 |
| 692fb37f-f9c0-3fa5-9742-ad82fb777e2f | -4.91544 | -46.69864 | 2024-10-13 04:40:00 | NOAA-21 | AMARANTE DO MARANHÃO | MARANHÃO | Brasil | 2100600 | 21 | 33 | nan | nan | nan | Amazônia | 1.9 |
| afd054b2-f895-37c6-854e-eb0ee0d6d3ba | -4.83652 | -46.9207 | 2024-10-13 04:40:00 | NOAA-21 | AÇAILÂNDIA | MARANHÃO | Brasil | 2100055 | 21 | 33 | nan | nan | nan | Amazônia | 0.7 |
| 0beda81c-b956-3d5e-b0e6-d4276cd3db76 | -4.82799 | -46.7921 | 2024-10-13 04:40:00 | NOAA-21 | BOM JESUS DAS SELVAS | MARANHÃO | Brasil | 2102036 | 21 | 33 | nan | nan | nan | Amazônia | 0.6 |
| e52d4ffe-87a7-36b5-a756-183a096470a1 | -4.81989 | -46.86823 | 2024-10-13 04:40:00 | NOAA-21 | BOM JESUS DAS SELVAS | MARANHÃO | Brasil | 2102036 | 21 | 33 | nan | nan | nan | Amazônia | 3.2 |
| 97772df7-1d25-3018-aeb1-8fe25bd1fef1 | -4.81931 | -46.872 | 2024-10-13 04:40:00 | NOAA-21 | BOM JESUS DAS SELVAS | MARANHÃO | Brasil | 2102036 | 21 | 33 | nan | nan | nan | Amazônia | 1.6 |
| 8ea715b7-7479-388c-92a7-7198c678d16e | -4.90107 | -47.666 | 2024-10-13 04:40:00 | NOAA-21 | AÇAILÂNDIA | MARANHÃO | Brasil | 2100055 | 21 | 33 | nan | nan | nan | Amazônia | 4.2 |
| 36be754d-8afe-355c-b84e-288980acfa6c | -4.85263 | -47.74278 | 2024-10-13 04:40:00 | NOAA-21 | AÇAILÂNDIA | MARANHÃO | Brasil | 2100055 | 21 | 33 | nan | nan | nan | Amazônia | 2.6 |
| 88518fb3-dd9d-317b-a5ee-e95cff2ef268 | -4.84928 | -47.74223 | 2024-10-13 04:40:00 | NOAA-21 | AÇAILÂNDIA | MARANHÃO | Brasil | 2100055 | 21 | 33 | nan | nan | nan | Amazônia | 2.6 |
| d52cc883-4671-384e-bc75-6a6242a51747 | -4.76516 | -47.42773 | 2024-10-13 04:40:00 | NOAA-21 | AÇAILÂNDIA | MARANHÃO | Brasil | 2100055 | 21 | 33 | nan | nan | nan | Amazônia | 1.6 |
| 8e07000c-9901-304b-a536-313269f34e08 | -5.0718 | -46.85092 | 2024-10-13 04:40:00 | NOAA-21 | AMARANTE DO MARANHÃO | MARANHÃO | Brasil | 2100600 | 21 | 33 | nan | nan | nan | Amazônia | 1.5 |
| 7b6ecbed-de4a-3613-a9be-a02eb9775edd | -5.06893 | -46.84658 | 2024-10-13 04:40:00 | NOAA-21 | AMARANTE DO MARANHÃO | MARANHÃO | Brasil | 2100600 | 21 | 33 | nan | nan | nan | Amazônia | 1.5 |
| 61cb9899-3b9a-3f65-a5b8-c4f45ba2d420 | -5.06834 | -46.85038 | 2024-10-13 04:40:00 | NOAA-21 | AMARANTE DO MARANHÃO | MARANHÃO | Brasil | 2100600 | 21 | 33 | nan | nan | nan | Amazônia | 1.5 |
| 0ea989d4-8edb-3414-aa79-745a5cc5345a | -5.96518 | -47.58693 | 2024-10-13 04:40:00 | NOAA-21 | MAURILÂNDIA DO TOCANTINS | TOCANTINS | Brasil | 1712801 | 17 | 33 | nan | nan | nan | Cerrado | 0.3 |
| 43ee0170-aa68-3531-885b-826c173200e8 | -5.76503 | -46.51331 | 2024-10-13 04:40:00 | NOAA-21 | SÍTIO NOVO | MARANHÃO | Brasil | 2111805 | 21 | 33 | nan | nan | nan | Cerrado | 2.2 |
| d54988ae-f30e-3980-aae4-aa6ba4c87d6b | -5.71117 | -46.63084 | 2024-10-13 04:40:00 | NOAA-21 | AMARANTE DO MARANHÃO | MARANHÃO | Brasil | 2100600 | 21 | 33 | nan | nan | nan | Cerrado | 1.4 |
| 55b0d97f-35ee-3af1-82b5-e95a5872ca20 | -5.6907 | -46.59949 | 2024-10-13 04:40:00 | NOAA-21 | AMARANTE DO MARANHÃO | MARANHÃO | Brasil | 2100600 | 21 | 33 | nan | nan | nan | Cerrado | 1.1 |
| 113570fb-0168-38f4-96b1-1503f6e463e8 | -5.68993 | -46.60054 | 2024-10-13 04:40:00 | NOAA-21 | AMARANTE DO MARANHÃO | MARANHÃO | Brasil | 2100600 | 21 | 33 | nan | nan | nan | Cerrado | 1.4 |
| f0d4cdb9-15ec-3a9b-9f88-d8fc55e41c16 | -5.67002 | -46.58953 | 2024-10-13 04:40:00 | NOAA-21 | AMARANTE DO MARANHÃO | MARANHÃO | Brasil | 2100600 | 21 | 33 | nan | nan | nan | Cerrado | 1.2 |
| 21c3b6ea-052f-3a66-85cb-32ce14703b6f | -5.6665 | -46.589 | 2024-10-13 04:40:00 | NOAA-21 | AMARANTE DO MARANHÃO | MARANHÃO | Brasil | 2100600 | 21 | 33 | nan | nan | nan | Cerrado | 1.2 |
| 2f337319-6074-30eb-a543-734a023add02 | -5.52968 | -47.1122 | 2024-10-13 04:40:00 | NOAA-21 | BURITIRANA | MARANHÃO | Brasil | 2102358 | 21 | 33 | nan | nan | nan | Cerrado | 3.7 |
| 92d612e4-e482-3361-b747-0274b76e6347 | -5.49797 | -46.79213 | 2024-10-13 04:40:00 | NOAA-21 | AMARANTE DO MARANHÃO | MARANHÃO | Brasil | 2100600 | 21 | 33 | nan | nan | nan | Cerrado | 1.9 |
| ad5b0cfd-b6dc-316b-adb8-05a04a040cbe | -5.46547 | -47.25581 | 2024-10-13 04:40:00 | NOAA-21 | SENADOR LA ROCQUE | MARANHÃO | Brasil | 2111763 | 21 | 33 | nan | nan | nan | Cerrado | 1.0 |
| 0ead9a94-7802-3233-8dfd-577ff249bd4a | -5.40793 | -47.92985 | 2024-10-13 04:40:00 | NOAA-21 | AUGUSTINÓPOLIS | TOCANTINS | Brasil | 1702554 | 17 | 33 | nan | nan | nan | Cerrado | 1.0 |
| 5b540108-eca8-39dc-ad57-316fdd5ebdd9 | -5.32425 | -46.60009 | 2024-10-13 04:40:00 | NOAA-21 | AMARANTE DO MARANHÃO | MARANHÃO | Brasil | 2100600 | 21 | 33 | nan | nan | nan | Cerrado | 2.3 |
| c95a8f15-ca34-3b31-a1f2-edc46f658d40 | -5.15222 | -47.60497 | 2024-10-13 04:40:00 | NOAA-21 | CIDELÂNDIA | MARANHÃO | Brasil | 2103257 | 21 | 33 | nan | nan | nan | Amazônia | 0.6 |
| c414a9b2-3be9-3ee2-bc02-ff11b37ccb87 | -5.12821 | -47.34873 | 2024-10-13 04:40:00 | NOAA-21 | SÃO FRANCISCO DO BREJÃO | MARANHÃO | Brasil | 2110856 | 21 | 33 | nan | nan | nan | Amazônia | 2.3 |
| ccf30044-160a-3de6-a84a-e6e9b2d17882 | -5.12481 | -47.3482 | 2024-10-13 04:40:00 | NOAA-21 | SÃO FRANCISCO DO BREJÃO | MARANHÃO | Brasil | 2110856 | 21 | 33 | nan | nan | nan | Amazônia | 1.5 |
| a91383a2-12fc-3e6a-bec5-3bcf01687a6b | -5.12141 | -47.34768 | 2024-10-13 04:40:00 | NOAA-21 | SÃO FRANCISCO DO BREJÃO | MARANHÃO | Brasil | 2110856 | 21 | 33 | nan | nan | nan | Amazônia | 1.5 |
| bf5cab65-894d-37dd-99e5-009b67ff4293 | -6.29923 | -47.17144 | 2024-10-13 04:40:00 | NOAA-21 | PORTO FRANCO | MARANHÃO | Brasil | 2109007 | 21 | 33 | nan | nan | nan | Cerrado | 0.8 |
| deef1eb4-1904-34bc-a5ee-eecfa94954c7 | -6.24144 | -47.38983 | 2024-10-13 04:40:00 | NOAA-21 | TOCANTINÓPOLIS | TOCANTINS | Brasil | 1721208 | 17 | 33 | nan | nan | nan | Cerrado | 5.1 |
| bd657fe9-5336-34f4-8975-91a24e6bca33 | -6.24087 | -47.39359 | 2024-10-13 04:40:00 | NOAA-21 | TOCANTINÓPOLIS | TOCANTINS | Brasil | 1721208 | 17 | 33 | nan | nan | nan | Cerrado | 5.1 |


[Clique aqui para ver as próximas entradas](README63.md)
