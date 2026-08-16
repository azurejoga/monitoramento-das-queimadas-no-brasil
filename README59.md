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

## Dados Diários - Página 59

| ID | Latitude | Longitude | Data/Hora GMT | Satélite | Município | Estado | País | Município ID | Estado ID | País ID | Dias sem Chuva | Precipitação | Risco de Fogo | Bioma | FRP |
|----|----------|-----------|---------------|----------|-----------|--------|------|--------------|-----------|---------|----------------|--------------|----------------|-------|-----|
| 1f1f1e92-e05a-3af4-93fc-d5c1d8a5a5be | -8.9787 | -60.5156 | 2026-08-16 09:20:00 | GOES-19 | COLNIZA | MATO GROSSO | Brasil | 5103254 | 51 | 33 | nan | nan | nan | Amazônia | 54.1 |
| 875461a1-ab20-327f-b1c6-8aeae919a166 | -8.9601 | -60.5165 | 2026-08-16 09:20:00 | GOES-19 | COLNIZA | MATO GROSSO | Brasil | 5103254 | 51 | 33 | nan | nan | nan | Amazônia | 65.8 |
| ab756c3e-5848-37ae-9415-dce8e10dc965 | -8.96 | -60.5358 | 2026-08-16 09:20:00 | GOES-19 | COLNIZA | MATO GROSSO | Brasil | 5103254 | 51 | 33 | nan | nan | nan | Amazônia | 53.9 |
| b32cf221-a216-3750-b9c6-43a0132cc4e2 | -6.1107 | -57.723 | 2026-08-16 09:20:00 | GOES-19 | JACAREACANGA | PARÁ | Brasil | 1503754 | 15 | 33 | nan | nan | nan | Amazônia | 49.8 |
| 05b992ac-a3c2-3201-8752-7956e1bf7f85 | -8.9601 | -60.5165 | 2026-08-16 09:30:00 | GOES-19 | COLNIZA | MATO GROSSO | Brasil | 5103254 | 51 | 33 | nan | nan | nan | Amazônia | 63.2 |
| 73ad55c9-dd6e-342b-8f6a-70662a94cda5 | -8.9787 | -60.5156 | 2026-08-16 09:30:00 | GOES-19 | COLNIZA | MATO GROSSO | Brasil | 5103254 | 51 | 33 | nan | nan | nan | Amazônia | 53.2 |
| 84aa4f7c-938c-3ecc-a6ff-75a0b25c79b8 | -8.96 | -60.5358 | 2026-08-16 09:30:00 | GOES-19 | COLNIZA | MATO GROSSO | Brasil | 5103254 | 51 | 33 | nan | nan | nan | Amazônia | 54.6 |
| 2b61ee56-802d-3cff-a7f1-23483d0d585e | -12.0091 | -46.4498 | 2026-08-16 10:30:00 | GOES-19 | PONTE ALTA DO BOM JESUS | TOCANTINS | Brasil | 1717800 | 17 | 33 | nan | nan | nan | Cerrado | 89.8 |
| 424d0064-9342-32c2-a67e-f23f41e17df4 | -11.8101 | -51.7957 | 2026-08-16 10:40:00 | GOES-19 | ALTO BOA VISTA | MATO GROSSO | Brasil | 5100359 | 51 | 33 | nan | nan | nan | Amazônia | 87.6 |
| 805a2d66-5089-31c8-81d5-e23137a2c0a6 | -12.0091 | -46.4498 | 2026-08-16 10:50:00 | GOES-19 | PONTE ALTA DO BOM JESUS | TOCANTINS | Brasil | 1717800 | 17 | 33 | nan | nan | nan | Cerrado | 93.5 |
| edeee5c4-4bd8-3974-a9eb-0ca803a0620b | -12.0091 | -46.4498 | 2026-08-16 11:00:00 | GOES-19 | PONTE ALTA DO BOM JESUS | TOCANTINS | Brasil | 1717800 | 17 | 33 | nan | nan | nan | Cerrado | 99.2 |
| 1ae4b37c-330a-32e9-b168-fc1dfd4e8934 | -12.0091 | -46.4498 | 2026-08-16 11:10:00 | GOES-19 | PONTE ALTA DO BOM JESUS | TOCANTINS | Brasil | 1717800 | 17 | 33 | nan | nan | nan | Cerrado | 107.2 |
| e052e0af-0b92-381e-a7c6-01313cccf6a9 | -12.7017 | -48.4753 | 2026-08-16 11:20:00 | GOES-19 | SÃO SALVADOR DO TOCANTINS | TOCANTINS | Brasil | 1720259 | 17 | 33 | nan | nan | nan | Cerrado | 120.8 |
| 169eec9e-46aa-3f6c-8d90-7ec76f3c2a5e | -11.8101 | -51.7957 | 2026-08-16 11:20:00 | GOES-19 | ALTO BOA VISTA | MATO GROSSO | Brasil | 5100359 | 51 | 33 | nan | nan | nan | Amazônia | 109.6 |
| de0b643e-7cad-3d14-9ab0-71a44ba4242d | -11.8101 | -51.7957 | 2026-08-16 11:30:00 | GOES-19 | ALTO BOA VISTA | MATO GROSSO | Brasil | 5100359 | 51 | 33 | nan | nan | nan | Amazônia | 128.6 |
| c9d41660-8024-3950-84b5-9b72d3cc57e7 | -11.8291 | -51.7937 | 2026-08-16 11:30:00 | GOES-19 | ALTO BOA VISTA | MATO GROSSO | Brasil | 5100359 | 51 | 33 | nan | nan | nan | Amazônia | 119.1 |
| dc545240-e44b-348a-b9af-64eef67ea531 | -12.7017 | -48.4753 | 2026-08-16 11:30:00 | GOES-19 | SÃO SALVADOR DO TOCANTINS | TOCANTINS | Brasil | 1720259 | 17 | 33 | nan | nan | nan | Cerrado | 77.4 |
| bfde13c4-f3f0-33c4-9ea0-521b81542227 | -11.8291 | -51.7937 | 2026-08-16 11:40:00 | GOES-19 | ALTO BOA VISTA | MATO GROSSO | Brasil | 5100359 | 51 | 33 | nan | nan | nan | Amazônia | 207.9 |
| 8b2e03db-dca9-3df9-94af-26428c5033e2 | -6.6854 | -43.9802 | 2026-08-16 11:40:00 | GOES-19 | NOVA IORQUE | MARANHÃO | Brasil | 2107308 | 21 | 33 | nan | nan | nan | Cerrado | 104.4 |
| 39469f30-5931-3a81-a49d-88eb047df12c | -11.8101 | -51.7957 | 2026-08-16 11:40:00 | GOES-19 | ALTO BOA VISTA | MATO GROSSO | Brasil | 5100359 | 51 | 33 | nan | nan | nan | Amazônia | 202.2 |
| 61539c67-5f6e-3f96-a9ba-ccf22bc151c3 | -12.7017 | -48.4753 | 2026-08-16 11:50:00 | GOES-19 | SÃO SALVADOR DO TOCANTINS | TOCANTINS | Brasil | 1720259 | 17 | 33 | nan | nan | nan | Cerrado | 89.4 |
| 0819e94e-5b10-3c5b-a25d-152c5262581b | -12.0091 | -46.4498 | 2026-08-16 11:50:00 | GOES-19 | PONTE ALTA DO BOM JESUS | TOCANTINS | Brasil | 1717800 | 17 | 33 | nan | nan | nan | Cerrado | 73.5 |
| 824facfb-e6aa-3fd9-a1b7-80ac8a1e2041 | -11.0796 | -47.2702 | 2026-08-16 11:50:00 | GOES-19 | ALMAS | TOCANTINS | Brasil | 1700400 | 17 | 33 | nan | nan | nan | Cerrado | 81.3 |
| 9b8d4ef6-0406-32d1-bac3-43ec1d03f28a | -6.6854 | -43.9802 | 2026-08-16 11:50:00 | GOES-19 | NOVA IORQUE | MARANHÃO | Brasil | 2107308 | 21 | 33 | nan | nan | nan | Cerrado | 212.8 |
| 98ed93a1-9877-32ed-961f-ff2f683211a2 | -6.6852 | -44.0033 | 2026-08-16 11:50:00 | GOES-19 | NOVA IORQUE | MARANHÃO | Brasil | 2107308 | 21 | 33 | nan | nan | nan | Cerrado | 124.9 |
| 7a2eeb9e-5017-35d1-a9f7-cc0bceba98ee | -11.0609 | -47.2503 | 2026-08-16 11:50:00 | GOES-19 | ALMAS | TOCANTINS | Brasil | 1700400 | 17 | 33 | nan | nan | nan | Cerrado | 82.7 |
| fa962d68-5d82-392c-a2ef-f584e9b95748 | -12.7013 | -48.4974 | 2026-08-16 11:50:00 | GOES-19 | SÃO SALVADOR DO TOCANTINS | TOCANTINS | Brasil | 1720259 | 17 | 33 | nan | nan | nan | Cerrado | 73.8 |
| 230a9de4-0a75-35ea-b6a5-40cb1f1647d1 | -6.6852 | -44.0033 | 2026-08-16 12:00:00 | GOES-19 | NOVA IORQUE | MARANHÃO | Brasil | 2107308 | 21 | 33 | nan | nan | nan | Cerrado | 210.9 |
| 054d7349-1929-3dfb-b11a-0d0733fb8766 | -11.0606 | -47.2726 | 2026-08-16 12:00:00 | GOES-19 | ALMAS | TOCANTINS | Brasil | 1700400 | 17 | 33 | nan | nan | nan | Cerrado | 69.2 |
| 5d0e389a-60f9-3063-bb6d-afb00e16c438 | -11.0609 | -47.2503 | 2026-08-16 12:00:00 | GOES-19 | ALMAS | TOCANTINS | Brasil | 1700400 | 17 | 33 | nan | nan | nan | Cerrado | 89.5 |
| 674d11c9-6cbc-34f3-af8f-e006c8708c19 | -12.7017 | -48.4753 | 2026-08-16 12:00:00 | GOES-19 | SÃO SALVADOR DO TOCANTINS | TOCANTINS | Brasil | 1720259 | 17 | 33 | nan | nan | nan | Cerrado | 126.7 |
| 0915affe-0eeb-3501-8bee-41eeaa692eb5 | -12.7013 | -48.4974 | 2026-08-16 12:00:00 | GOES-19 | SÃO SALVADOR DO TOCANTINS | TOCANTINS | Brasil | 1720259 | 17 | 33 | nan | nan | nan | Cerrado | 216.8 |
| 4dd99a87-a0b4-3d17-90ff-2d208732a2a1 | -11.08 | -47.2479 | 2026-08-16 12:00:00 | GOES-19 | ALMAS | TOCANTINS | Brasil | 1700400 | 17 | 33 | nan | nan | nan | Cerrado | 84.4 |
| a11c02a5-467a-3179-a022-2734ecd7517f | -12.0095 | -46.4271 | 2026-08-16 12:00:00 | GOES-19 | PONTE ALTA DO BOM JESUS | TOCANTINS | Brasil | 1717800 | 17 | 33 | nan | nan | nan | Cerrado | 80.0 |
| fb96b12f-e348-35f1-809c-fa8394b85dbb | -11.0796 | -47.2702 | 2026-08-16 12:00:00 | GOES-19 | ALMAS | TOCANTINS | Brasil | 1700400 | 17 | 33 | nan | nan | nan | Cerrado | 98.7 |
| bde6d453-af00-3c01-aec8-8f60066bbffa | -6.6666 | -43.9818 | 2026-08-16 12:00:00 | GOES-19 | NOVA IORQUE | MARANHÃO | Brasil | 2107308 | 21 | 33 | nan | nan | nan | Cerrado | 75.9 |
| 74c6ee7b-b9f8-32fb-87f3-6a0bd8d56287 | -12.0091 | -46.4498 | 2026-08-16 12:00:00 | GOES-19 | PONTE ALTA DO BOM JESUS | TOCANTINS | Brasil | 1717800 | 17 | 33 | nan | nan | nan | Cerrado | 110.1 |
| 9534e73d-8438-3615-a047-c7c0cb9d2bbc | -6.6854 | -43.9802 | 2026-08-16 12:00:00 | GOES-19 | NOVA IORQUE | MARANHÃO | Brasil | 2107308 | 21 | 33 | nan | nan | nan | Cerrado | 342.2 |
| 749f624e-2f53-3bfb-99ff-7aa69dc77260 | -12.7017 | -48.4753 | 2026-08-16 12:10:00 | GOES-19 | SÃO SALVADOR DO TOCANTINS | TOCANTINS | Brasil | 1720259 | 17 | 33 | nan | nan | nan | Cerrado | 110.2 |
| 8d012f43-4e9a-3fd4-86fe-e1c8ad1de15b | -12.0095 | -46.4271 | 2026-08-16 12:10:00 | GOES-19 | PONTE ALTA DO BOM JESUS | TOCANTINS | Brasil | 1717800 | 17 | 33 | nan | nan | nan | Cerrado | 79.6 |
| 00784de9-7eef-323a-973f-99a5372b08e3 | -12.7013 | -48.4974 | 2026-08-16 12:10:00 | GOES-19 | SÃO SALVADOR DO TOCANTINS | TOCANTINS | Brasil | 1720259 | 17 | 33 | nan | nan | nan | Cerrado | 160.7 |
| 0faea692-8efd-324c-a9b3-10c54c4234ff | -11.0609 | -47.2503 | 2026-08-16 12:10:00 | GOES-19 | ALMAS | TOCANTINS | Brasil | 1700400 | 17 | 33 | nan | nan | nan | Cerrado | 69.7 |
| 1bf28ce4-0316-3454-8ac7-bc87e1abd395 | -12.0091 | -46.4498 | 2026-08-16 12:10:00 | GOES-19 | PONTE ALTA DO BOM JESUS | TOCANTINS | Brasil | 1717800 | 17 | 33 | nan | nan | nan | Cerrado | 102.4 |
| 09558513-f880-3120-9794-a46d06df15ac | -11.06467 | -47.23378 | 2026-08-16 12:14:00 | TERRA_M-T | ALMAS | TOCANTINS | Brasil | 1700400 | 17 | 33 | nan | nan | nan | Cerrado | 44.0 |
| ce3b6e35-540a-393f-b8b1-0608865b1e01 | -7.41733 | -60.00259 | 2026-08-16 12:14:00 | TERRA_M-T | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 16.3 |
| c519f1eb-e90d-31a8-876d-2b3d2bc01adc | -7.38292 | -46.8403 | 2026-08-16 12:14:00 | TERRA_M-T | RIACHÃO | MARANHÃO | Brasil | 2109502 | 21 | 33 | nan | nan | nan | Cerrado | 27.6 |
| c88762b0-9ffa-34fb-b752-755e9fdf8616 | -11.06163 | -47.25862 | 2026-08-16 12:14:00 | TERRA_M-T | ALMAS | TOCANTINS | Brasil | 1700400 | 17 | 33 | nan | nan | nan | Cerrado | 50.0 |
| f7f15158-b93d-3497-b370-a7a9c709a0d5 | -10.88455 | -50.54356 | 2026-08-16 12:14:00 | TERRA_M-T | LAGOA DA CONFUSÃO | TOCANTINS | Brasil | 1711902 | 17 | 33 | nan | nan | nan | Cerrado | 13.0 |
| 27bff478-0f9f-376e-bdce-b79429242e2c | -6.68376 | -43.9564 | 2026-08-16 12:14:00 | TERRA_M-T | NOVA IORQUE | MARANHÃO | Brasil | 2107308 | 21 | 33 | nan | nan | nan | Cerrado | 161.6 |
| eb51434f-5536-326b-94e6-969835d43eda | -2.96212 | -49.27009 | 2026-08-16 12:14:00 | TERRA_M-T | MOJU | PARÁ | Brasil | 1504703 | 15 | 33 | nan | nan | nan | Amazônia | 10.2 |
| 2bf8b64d-8050-350c-8813-62fff4a4f83c | -6.67605 | -43.98736 | 2026-08-16 12:14:00 | TERRA_M-T | NOVA IORQUE | MARANHÃO | Brasil | 2107308 | 21 | 33 | nan | nan | nan | Cerrado | 241.2 |
| 40df016d-b9d5-3919-bb9d-b924b15250e3 | -6.60323 | -58.9966 | 2026-08-16 12:14:00 | TERRA_M-T | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 11.5 |
| 166f01d6-b099-36a5-8460-02ce748b344b | -6.10492 | -57.71329 | 2026-08-16 12:14:00 | TERRA_M-T | JACAREACANGA | PARÁ | Brasil | 1503754 | 15 | 33 | nan | nan | nan | Amazônia | 39.1 |
| b74eb41d-c8df-3983-9f95-b224c4443877 | -9.98196 | -53.94257 | 2026-08-16 12:14:00 | TERRA_M-T | PEIXOTO DE AZEVEDO | MATO GROSSO | Brasil | 5106422 | 51 | 33 | nan | nan | nan | Amazônia | 6.7 |
| 6f1c7d53-469c-37b2-8c17-5d08f440330f | -6.7841 | -55.84152 | 2026-08-16 12:14:00 | TERRA_M-T | NOVO PROGRESSO | PARÁ | Brasil | 1505031 | 15 | 33 | nan | nan | nan | Amazônia | 5.7 |
| 627242cd-a64f-3263-b434-acb2351a8a54 | -6.70082 | -43.95804 | 2026-08-16 12:14:00 | TERRA_M-T | NOVA IORQUE | MARANHÃO | Brasil | 2107308 | 21 | 33 | nan | nan | nan | Cerrado | 220.9 |
| cf7cf672-88b3-3d9c-b2fb-bd524160b6e2 | -11.06903 | -47.2414 | 2026-08-16 12:14:00 | TERRA_M-T | ALMAS | TOCANTINS | Brasil | 1700400 | 17 | 33 | nan | nan | nan | Cerrado | 40.6 |
| 8c464548-297e-31be-bcd1-86c5cfd8a27f | -6.69779 | -43.95102 | 2026-08-16 12:14:00 | TERRA_M-T | NOVA IORQUE | MARANHÃO | Brasil | 2107308 | 21 | 33 | nan | nan | nan | Cerrado | 184.1 |
| a701c2a3-ab87-3f7c-8734-d4dee8cf36f5 | -6.22476 | -47.74845 | 2026-08-16 12:14:00 | TERRA_M-T | LUZINÓPOLIS | TOCANTINS | Brasil | 1712454 | 17 | 33 | nan | nan | nan | Cerrado | 24.5 |
| 85d9f250-8d60-3cb5-9445-5ae970c9e709 | -11.32221 | -47.00058 | 2026-08-16 12:14:00 | TERRA_M-T | ALMAS | TOCANTINS | Brasil | 1700400 | 17 | 33 | nan | nan | nan | Cerrado | 32.8 |
| 626cebb5-6835-3755-83af-eb8e9b039525 | -6.22101 | -47.76011 | 2026-08-16 12:14:00 | TERRA_M-T | LUZINÓPOLIS | TOCANTINS | Brasil | 1712454 | 17 | 33 | nan | nan | nan | Cerrado | 17.3 |
| de5c25fd-5006-383c-ae91-aa9fe2684323 | -6.86161 | -58.96936 | 2026-08-16 12:14:00 | TERRA_M-T | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 24.3 |
| 5499f494-c6d0-399f-a01b-5a5650879fb5 | -6.02252 | -57.83223 | 2026-08-16 12:14:00 | TERRA_M-T | JACAREACANGA | PARÁ | Brasil | 1503754 | 15 | 33 | nan | nan | nan | Amazônia | 9.1 |
| 6a99032e-a2ca-351a-807a-6ca6e3315fc0 | -6.22345 | -47.74177 | 2026-08-16 12:14:00 | TERRA_M-T | LUZINÓPOLIS | TOCANTINS | Brasil | 1712454 | 17 | 33 | nan | nan | nan | Cerrado | 21.7 |
| 65af8f13-d0d1-3dc4-9771-00fccc013bac | -7.38587 | -46.81651 | 2026-08-16 12:14:00 | TERRA_M-T | RIACHÃO | MARANHÃO | Brasil | 2109502 | 21 | 33 | nan | nan | nan | Cerrado | 27.8 |
| f14c825a-868d-3fe9-848b-3fda0d4e97a0 | -10.48328 | -50.38381 | 2026-08-16 12:14:00 | TERRA_M-T | PIUM | TOCANTINS | Brasil | 1717503 | 17 | 33 | nan | nan | nan | Cerrado | 13.4 |
| 740caaec-e9b0-31c6-abe8-aec82e7de917 | -7.42014 | -60.00994 | 2026-08-16 12:14:00 | TERRA_M-T | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 15.2 |
| fdf3d34e-95ec-3d8a-8e8e-64687e3d43e8 | -11.08023 | -47.26796 | 2026-08-16 12:14:00 | TERRA_M-T | ALMAS | TOCANTINS | Brasil | 1700400 | 17 | 33 | nan | nan | nan | Cerrado | 61.7 |
| 8cda5955-95b2-33da-a115-3d682b465ea3 | -10.72074 | -52.10589 | 2026-08-16 12:14:00 | TERRA_M-T | PORTO ALEGRE DO NORTE | MATO GROSSO | Brasil | 5106778 | 51 | 33 | nan | nan | nan | Amazônia | 11.8 |
| 3bd3c8c9-d97f-3d02-8a3a-fdaa5976f98e | -8.98099 | -60.51394 | 2026-08-16 12:14:00 | TERRA_M-T | COLNIZA | MATO GROSSO | Brasil | 5103254 | 51 | 33 | nan | nan | nan | Amazônia | 44.0 |
| 90b3638b-2a7b-3a64-ae18-989fbde9ede9 | -10.53732 | -50.21979 | 2026-08-16 12:14:00 | TERRA_M-T | PIUM | TOCANTINS | Brasil | 1717503 | 17 | 33 | nan | nan | nan | Cerrado | 10.2 |
| d77ce7c5-174c-32fd-9205-2729bb50ee9f | -6.63053 | -59.04857 | 2026-08-16 12:14:00 | TERRA_M-T | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 19.8 |
| 152f6f22-50be-3825-9a9d-0a7f43ae461a | -8.96856 | -60.51208 | 2026-08-16 12:14:00 | TERRA_M-T | COLNIZA | MATO GROSSO | Brasil | 5103254 | 51 | 33 | nan | nan | nan | Amazônia | 41.8 |
| a1c27433-4894-3739-bd85-8396bc9a52c9 | -10.48501 | -50.36998 | 2026-08-16 12:14:00 | TERRA_M-T | PIUM | TOCANTINS | Brasil | 1717503 | 17 | 33 | nan | nan | nan | Cerrado | 9.0 |
| 3caf8ab0-4988-383b-b61a-cad39319ab06 | -6.96012 | -59.30202 | 2026-08-16 12:14:00 | TERRA_M-T | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 13.3 |
| 876ef83b-7f69-31ca-ad94-32183a6d0e53 | -10.96858 | -50.51854 | 2026-08-16 12:14:00 | TERRA_M-T | LAGOA DA CONFUSÃO | TOCANTINS | Brasil | 1711902 | 17 | 33 | nan | nan | nan | Cerrado | 27.9 |
| f74aaa51-1df9-350d-848b-b08f2eb8423b | -6.71776 | -58.92623 | 2026-08-16 12:14:00 | TERRA_M-T | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 23.5 |
| b0b37950-2ca3-34c8-8547-9ccfa3bcc091 | -7.44387 | -55.30932 | 2026-08-16 12:14:00 | TERRA_M-T | NOVO PROGRESSO | PARÁ | Brasil | 1505031 | 15 | 33 | nan | nan | nan | Amazônia | 6.8 |
| 74c3dcc8-e6c8-3108-b926-b7f6f6177cbe | -6.85936 | -58.97598 | 2026-08-16 12:14:00 | TERRA_M-T | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 24.1 |
| 23958c86-68fb-3e2f-b1bc-c2c912b85e07 | -11.32481 | -47.00616 | 2026-08-16 12:14:00 | TERRA_M-T | ALMAS | TOCANTINS | Brasil | 1700400 | 17 | 33 | nan | nan | nan | Cerrado | 23.9 |
| 1f5ba436-83bf-3f90-9e2d-ba912299eecb | -6.69635 | -43.99593 | 2026-08-16 12:14:00 | TERRA_M-T | NOVA IORQUE | MARANHÃO | Brasil | 2107308 | 21 | 33 | nan | nan | nan | Cerrado | 529.3 |
| 5d5518a7-b210-30d0-a5cf-89825e3ef599 | -6.67932 | -43.99449 | 2026-08-16 12:14:00 | TERRA_M-T | NOVA IORQUE | MARANHÃO | Brasil | 2107308 | 21 | 33 | nan | nan | nan | Cerrado | 420.8 |
| a4975390-6135-335f-a085-d332cb1221f9 | -6.63835 | -56.39592 | 2026-08-16 12:14:00 | TERRA_M-T | ITAITUBA | PARÁ | Brasil | 1503606 | 15 | 33 | nan | nan | nan | Amazônia | 6.6 |
| d14cd9e7-fdf1-35bd-b432-cdaaf8d24db5 | -8.96561 | -60.53067 | 2026-08-16 12:14:00 | TERRA_M-T | COLNIZA | MATO GROSSO | Brasil | 5103254 | 51 | 33 | nan | nan | nan | Amazônia | 44.0 |
| d74a9b45-f1cc-39dd-b294-dec7af4391ae | -2.77252 | -48.57016 | 2026-08-16 12:14:00 | TERRA_M-T | TAILÂNDIA | PARÁ | Brasil | 1507953 | 15 | 33 | nan | nan | nan | Amazônia | 9.8 |
| 26a88355-72f4-36a0-acf7-678a50467090 | -9.30001 | -56.81204 | 2026-08-16 12:14:00 | TERRA_M-T | PARANAÍTA | MATO GROSSO | Brasil | 5106299 | 51 | 33 | nan | nan | nan | Amazônia | 11.4 |
| ba040e8a-9298-3907-bbf9-6ee52fb705f6 | -10.48067 | -50.37704 | 2026-08-16 12:14:00 | TERRA_M-T | PIUM | TOCANTINS | Brasil | 1717503 | 17 | 33 | nan | nan | nan | Cerrado | 21.9 |
| 06071715-e13c-3aa8-ba0d-9c995aa823c5 | -6.7 | -43.98 | 2026-08-16 12:15:00 | MSG-03 | NOVA IORQUE | MARANHÃO | Brasil | 2107308 | 21 | 33 | nan | nan | nan | Cerrado | nan |
| 414a363e-31b0-3513-94f3-d5e8c0cc6334 | -6.67 | -43.98 | 2026-08-16 12:15:00 | MSG-03 | NOVA IORQUE | MARANHÃO | Brasil | 2107308 | 21 | 33 | nan | nan | nan | Cerrado | nan |
| 246b0f0e-ca9e-33bb-aa09-b37b7093c284 | -15.07009 | -47.01889 | 2026-08-16 12:17:00 | TERRA_M-T | VILA BOA | GOIÁS | Brasil | 5222203 | 52 | 33 | nan | nan | nan | Cerrado | 27.0 |
| 7f5d44e6-6597-3224-a1c7-4b05a66b762c | -14.46897 | -51.99502 | 2026-08-16 12:17:00 | TERRA_M-T | NOVA NAZARÉ | MATO GROSSO | Brasil | 5106174 | 51 | 33 | nan | nan | nan | Cerrado | 16.4 |
| 9c46b233-a47c-3f31-a2da-1fde24275215 | -15.16129 | -48.66176 | 2026-08-16 12:17:00 | TERRA_M-T | VILA PROPÍCIO | GOIÁS | Brasil | 5222302 | 52 | 33 | nan | nan | nan | Cerrado | 22.3 |
| b19d93fe-426d-3c62-aa1e-e154e0608a6e | -11.82338 | -51.78687 | 2026-08-16 12:17:00 | TERRA_M-T | ALTO BOA VISTA | MATO GROSSO | Brasil | 5100359 | 51 | 33 | nan | nan | nan | Amazônia | 21.2 |
| e906c35c-d5f7-33f7-a0c0-b357e870a312 | -12.70509 | -48.50095 | 2026-08-16 12:17:00 | TERRA_M-T | SÃO SALVADOR DO TOCANTINS | TOCANTINS | Brasil | 1720259 | 17 | 33 | nan | nan | nan | Cerrado | 141.6 |
| 537a3327-fc5d-3a60-88be-a0729baf5369 | -13.80206 | -53.82477 | 2026-08-16 12:17:00 | TERRA_M-T | PARANATINGA | MATO GROSSO | Brasil | 5106307 | 51 | 33 | nan | nan | nan | Cerrado | 13.6 |
| c08026fe-e7af-3fb9-82d4-c6c16f2af57a | -15.14421 | -50.04905 | 2026-08-16 12:17:00 | TERRA_M-T | ARAGUAPAZ | GOIÁS | Brasil | 5202155 | 52 | 33 | nan | nan | nan | Cerrado | 54.6 |
| 1e2f8281-9ecc-359c-bcce-3921b0e0584b | -14.28146 | -51.94566 | 2026-08-16 12:17:00 | TERRA_M-T | NOVA NAZARÉ | MATO GROSSO | Brasil | 5106174 | 51 | 33 | nan | nan | nan | Cerrado | 12.5 |
| 7679300f-cad0-3fa9-a224-6ae2db341691 | -12.02216 | -46.44488 | 2026-08-16 12:17:00 | TERRA_M-T | PONTE ALTA DO BOM JESUS | TOCANTINS | Brasil | 1717800 | 17 | 33 | nan | nan | nan | Cerrado | 52.0 |
| 9dd824f1-cce2-374c-a85d-1bbaa2d3af1a | -15.03123 | -52.69064 | 2026-08-16 12:17:00 | TERRA_M-T | BARRA DO GARÇAS | MATO GROSSO | Brasil | 5101803 | 51 | 33 | nan | nan | nan | Cerrado | 5.9 |
| 159ea506-03bc-35c9-88cf-b28c25c13eb1 | -12.01975 | -46.45037 | 2026-08-16 12:17:00 | TERRA_M-T | PONTE ALTA DO BOM JESUS | TOCANTINS | Brasil | 1717800 | 17 | 33 | nan | nan | nan | Cerrado | 51.9 |


[Clique aqui para ver as próximas entradas](README60.md)
