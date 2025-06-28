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

## Dados Diários - Página 7

| ID | Latitude | Longitude | Data/Hora GMT | Satélite | Município | Estado | País | Município ID | Estado ID | País ID | Dias sem Chuva | Precipitação | Risco de Fogo | Bioma | FRP |
|----|----------|-----------|---------------|----------|-----------|--------|------|--------------|-----------|---------|----------------|--------------|----------------|-------|-----|
| 6729547d-88c6-36dd-b403-8bee682f718c | -6.9416 | -42.8834 | 2025-06-28 01:50:00 | GOES-19 | FLORIANO | PIAUÍ | Brasil | 2203909 | 22 | 33 | nan | nan | nan | Caatinga | 74.8 |
| 5ef4f7af-4ebc-3f9c-bec5-bc7b62a39a13 | -11.2664 | -52.7527 | 2025-06-28 01:50:00 | GOES-19 | SÃO FÉLIX DO ARAGUAIA | MATO GROSSO | Brasil | 5107859 | 51 | 33 | nan | nan | nan | Amazônia | 172.9 |
| abbb5fd6-809c-3d83-a27f-32578f626b60 | -11.2853 | -52.7508 | 2025-06-28 01:50:00 | GOES-19 | SÃO FÉLIX DO ARAGUAIA | MATO GROSSO | Brasil | 5107859 | 51 | 33 | nan | nan | nan | Amazônia | 93.1 |
| eccbf97a-1eb8-356b-a5df-37a7238fc8bb | -12.2715 | -46.7739 | 2025-06-28 01:50:00 | GOES-19 | PONTE ALTA DO BOM JESUS | TOCANTINS | Brasil | 1717800 | 17 | 33 | nan | nan | nan | Cerrado | 61.8 |
| c9605796-deb4-3369-ac37-03db669da27f | -9.7041 | -56.1843 | 2025-06-28 01:50:00 | GOES-19 | ALTA FLORESTA | MATO GROSSO | Brasil | 5100250 | 51 | 33 | nan | nan | nan | Amazônia | 73.7 |
| 18cc6144-3bb5-384d-8a13-e2b704ae186f | -9.7073 | -56.191898 | 2025-06-28 01:52:00 | METOP-C | ALTA FLORESTA | MATO GROSSO | Brasil | 5100250 | 51 | 33 | nan | nan | nan | Amazônia | nan |
| b513157a-9897-342f-abbb-37d0638753d0 | -10.3049 | -57.143002 | 2025-06-28 01:52:00 | METOP-C | NOVA MONTE VERDE | MATO GROSSO | Brasil | 5108956 | 51 | 33 | nan | nan | nan | Amazônia | nan |
| 452310c3-04c5-3459-a273-a8c075760c4c | -10.8354 | -53.7551 | 2025-06-28 01:52:00 | METOP-C | MARCELÂNDIA | MATO GROSSO | Brasil | 5105580 | 51 | 33 | nan | nan | nan | Amazônia | nan |
| 7f3813e6-cff7-3777-bfef-148291723b1b | -11.056 | -55.410099 | 2025-06-28 01:52:00 | METOP-C | ITAÚBA | MATO GROSSO | Brasil | 5104559 | 51 | 33 | nan | nan | nan | Amazônia | nan |
| 81681187-2db4-3d6c-9840-c36044e42ba7 | -11.0593 | -55.383598 | 2025-06-28 01:52:00 | METOP-C | ITAÚBA | MATO GROSSO | Brasil | 5104559 | 51 | 33 | nan | nan | nan | Amazônia | nan |
| 1f606a8c-7a67-3641-bbe6-1cbb4b8a33b9 | -9.7227 | -56.211601 | 2025-06-28 01:52:00 | METOP-C | ALTA FLORESTA | MATO GROSSO | Brasil | 5100250 | 51 | 33 | nan | nan | nan | Amazônia | nan |
| a4bbce90-c444-352c-a810-d4570d57584e | -11.8911 | -58.7384 | 2025-06-28 01:52:00 | METOP-C | JUÍNA | MATO GROSSO | Brasil | 5105150 | 51 | 33 | nan | nan | nan | Cerrado | nan |
| b404e6ab-0438-3f04-8df8-58dc63aaa655 | -11.0529 | -55.359699 | 2025-06-28 01:52:00 | METOP-C | ITAÚBA | MATO GROSSO | Brasil | 5104559 | 51 | 33 | nan | nan | nan | Amazônia | nan |
| 075c7621-e140-33b8-b9a8-d2db83284ebb | -9.7266 | -56.186798 | 2025-06-28 01:52:00 | METOP-C | ALTA FLORESTA | MATO GROSSO | Brasil | 5100250 | 51 | 33 | nan | nan | nan | Amazônia | nan |
| 02546980-c9ae-3abb-871b-60943c623bf5 | -11.0401 | -55.388901 | 2025-06-28 01:52:00 | METOP-C | ITAÚBA | MATO GROSSO | Brasil | 5104559 | 51 | 33 | nan | nan | nan | Amazônia | nan |
| f18e9998-b840-366d-b82c-3a9e3c4429a2 | -11.0433 | -55.362301 | 2025-06-28 01:52:00 | METOP-C | ITAÚBA | MATO GROSSO | Brasil | 5104559 | 51 | 33 | nan | nan | nan | Amazônia | nan |
| eb99eb48-6116-3e18-b10b-dd9125fd8f98 | -11.2929 | -52.807301 | 2025-06-28 01:52:00 | METOP-C | SÃO FÉLIX DO ARAGUAIA | MATO GROSSO | Brasil | 5107859 | 51 | 33 | nan | nan | nan | Amazônia | nan |
| 1e97774c-2204-3312-bc25-d2b5c068803e | -11.0689 | -55.381001 | 2025-06-28 01:52:00 | METOP-C | ITAÚBA | MATO GROSSO | Brasil | 5104559 | 51 | 33 | nan | nan | nan | Amazônia | nan |
| 4829aaa3-8e56-3591-801d-acc6d0bee466 | -9.7169 | -56.1894 | 2025-06-28 01:52:00 | METOP-C | ALTA FLORESTA | MATO GROSSO | Brasil | 5100250 | 51 | 33 | nan | nan | nan | Amazônia | nan |
| fa05d7d5-2ed6-385a-b6d3-c4c859c995c6 | -10.3001 | -57.124199 | 2025-06-28 01:52:00 | METOP-C | NOVA MONTE VERDE | MATO GROSSO | Brasil | 5108956 | 51 | 33 | nan | nan | nan | Amazônia | nan |
| 0e5d48f1-2abe-3968-b008-4695b445ab8c | -11.0656 | -55.407501 | 2025-06-28 01:52:00 | METOP-C | ITAÚBA | MATO GROSSO | Brasil | 5104559 | 51 | 33 | nan | nan | nan | Amazônia | nan |
| eeeecab4-cc4b-3706-ba3b-851093b73b96 | -11.0497 | -55.3862 | 2025-06-28 01:52:00 | METOP-C | ITAÚBA | MATO GROSSO | Brasil | 5104559 | 51 | 33 | nan | nan | nan | Amazônia | nan |
| 28f20b2a-e5b1-337d-97e2-a10644024c7c | -9.7324 | -56.209 | 2025-06-28 01:52:00 | METOP-C | ALTA FLORESTA | MATO GROSSO | Brasil | 5100250 | 51 | 33 | nan | nan | nan | Amazônia | nan |
| 96ccafb7-1fad-30d6-8fc6-51356e762108 | -6.9416 | -42.8834 | 2025-06-28 02:00:00 | GOES-19 | FLORIANO | PIAUÍ | Brasil | 2203909 | 22 | 33 | nan | nan | nan | Caatinga | 83.6 |
| 8eb87e76-4259-37ea-ac7e-f10094b3f2df | -12.2715 | -46.7739 | 2025-06-28 02:00:00 | GOES-19 | PONTE ALTA DO BOM JESUS | TOCANTINS | Brasil | 1717800 | 17 | 33 | nan | nan | nan | Cerrado | 70.3 |
| dffc6dd4-d3d5-38fd-b6e3-25ca547a71f9 | -9.1208 | -49.4743 | 2025-06-28 02:00:00 | GOES-19 | ARAGUACEMA | TOCANTINS | Brasil | 1701903 | 17 | 33 | nan | nan | nan | Cerrado | 95.0 |
| c00a1084-2b6f-31c7-87f3-487c32aacd30 | -9.7228 | -56.183 | 2025-06-28 02:00:00 | GOES-19 | ALTA FLORESTA | MATO GROSSO | Brasil | 5100250 | 51 | 33 | nan | nan | nan | Amazônia | 94.6 |
| 49d42756-3deb-3aaa-87aa-56552ff28486 | -11.0455 | -55.3773 | 2025-06-28 02:00:00 | GOES-19 | ITAÚBA | MATO GROSSO | Brasil | 5104559 | 51 | 33 | nan | nan | nan | Amazônia | 247.2 |
| 37b0c8b8-7515-3c2b-b206-cfadaa96cf51 | -11.2664 | -52.7527 | 2025-06-28 02:00:00 | GOES-19 | SÃO FÉLIX DO ARAGUAIA | MATO GROSSO | Brasil | 5107859 | 51 | 33 | nan | nan | nan | Amazônia | 166.5 |
| 7fe6286e-5163-3d48-9c12-3771c10c63e1 | -11.2666 | -52.7318 | 2025-06-28 02:00:00 | GOES-19 | SÃO FÉLIX DO ARAGUAIA | MATO GROSSO | Brasil | 5107859 | 51 | 33 | nan | nan | nan | Amazônia | 51.2 |
| cddf3fd6-4bb8-37a2-af99-eede5f042972 | -7.2217 | -43.0917 | 2025-06-28 02:00:00 | GOES-19 | FLORIANO | PIAUÍ | Brasil | 2203909 | 22 | 33 | nan | nan | nan | Caatinga | 90.5 |
| 4969458f-580a-390a-89ad-98099c58e9fc | -11.0453 | -55.3976 | 2025-06-28 02:00:00 | GOES-19 | ITAÚBA | MATO GROSSO | Brasil | 5104559 | 51 | 33 | nan | nan | nan | Amazônia | 55.3 |
| 391c0c0d-ab98-3526-8886-ba82fdef4313 | -11.0644 | -55.3757 | 2025-06-28 02:00:00 | GOES-19 | ITAÚBA | MATO GROSSO | Brasil | 5104559 | 51 | 33 | nan | nan | nan | Amazônia | 80.6 |
| 1437f56b-edc4-3b9f-9d81-ecc5be9ea21a | -9.7041 | -56.1843 | 2025-06-28 02:00:00 | GOES-19 | ALTA FLORESTA | MATO GROSSO | Brasil | 5100250 | 51 | 33 | nan | nan | nan | Amazônia | 73.5 |
| 82d93f6f-8008-38fe-98ff-1e6aba9a0bed | -9.1205 | -49.4958 | 2025-06-28 02:00:00 | GOES-19 | ARAGUACEMA | TOCANTINS | Brasil | 1701903 | 17 | 33 | nan | nan | nan | Cerrado | 105.1 |
| c7f85f70-93c4-3983-87b8-fc1c502591e8 | -7.2219 | -43.0682 | 2025-06-28 02:00:00 | GOES-19 | FLORIANO | PIAUÍ | Brasil | 2203909 | 22 | 33 | nan | nan | nan | Caatinga | 105.3 |
| ebcb1976-f987-3c40-b4f2-eee7548ab50e | -11.0457 | -55.3571 | 2025-06-28 02:00:00 | GOES-19 | ITAÚBA | MATO GROSSO | Brasil | 5104559 | 51 | 33 | nan | nan | nan | Amazônia | 88.8 |
| 7f2d8ec6-610b-3d39-a620-9ca433f1b669 | -11.2853 | -52.7508 | 2025-06-28 02:00:00 | GOES-19 | SÃO FÉLIX DO ARAGUAIA | MATO GROSSO | Brasil | 5107859 | 51 | 33 | nan | nan | nan | Amazônia | 66.7 |
| 8eb2d310-55d3-3322-9947-6697f0305c72 | -6.9108 | -43.9834 | 2025-06-28 02:00:00 | GOES-19 | PORTO ALEGRE DO PIAUÍ | PIAUÍ | Brasil | 2208551 | 22 | 33 | nan | nan | nan | Cerrado | 108.7 |
| bdadecf3-8a32-3160-bcab-c06d4f944df8 | -6.892 | -43.9851 | 2025-06-28 02:00:00 | GOES-19 | PORTO ALEGRE DO PIAUÍ | PIAUÍ | Brasil | 2208551 | 22 | 33 | nan | nan | nan | Cerrado | 75.8 |
| 08aae961-25d3-3c17-b455-5a6b7dda382d | -12.2719 | -46.7513 | 2025-06-28 02:00:00 | GOES-19 | TAGUATINGA | TOCANTINS | Brasil | 1720903 | 17 | 33 | nan | nan | nan | Cerrado | 55.9 |
| 024602fd-7d82-3cd0-bb18-cd9fb27a2add | -7.2219 | -43.0682 | 2025-06-28 02:10:00 | GOES-19 | FLORIANO | PIAUÍ | Brasil | 2203909 | 22 | 33 | nan | nan | nan | Caatinga | 92.4 |
| 5b4cafed-f551-3e1b-8c66-56364e146c88 | -11.2853 | -52.7508 | 2025-06-28 02:10:00 | GOES-19 | SÃO FÉLIX DO ARAGUAIA | MATO GROSSO | Brasil | 5107859 | 51 | 33 | nan | nan | nan | Amazônia | 65.5 |
| ee3d1693-c6fc-315b-b0d8-60c974054f00 | -12.2523 | -46.7766 | 2025-06-28 02:10:00 | GOES-19 | PONTE ALTA DO BOM JESUS | TOCANTINS | Brasil | 1717800 | 17 | 33 | nan | nan | nan | Cerrado | 54.9 |
| 5eae93c3-69bd-3d0f-b843-3a0dfb0e7431 | -9.7228 | -56.183 | 2025-06-28 02:10:00 | GOES-19 | ALTA FLORESTA | MATO GROSSO | Brasil | 5100250 | 51 | 33 | nan | nan | nan | Amazônia | 72.4 |
| bf27bb8c-e37b-3e3e-9f74-12705d84250b | -11.0457 | -55.3571 | 2025-06-28 02:10:00 | GOES-19 | ITAÚBA | MATO GROSSO | Brasil | 5104559 | 51 | 33 | nan | nan | nan | Amazônia | 70.2 |
| 6aa60b43-9adc-3a36-a63d-3672e49bbd69 | -11.0455 | -55.3773 | 2025-06-28 02:10:00 | GOES-19 | ITAÚBA | MATO GROSSO | Brasil | 5104559 | 51 | 33 | nan | nan | nan | Amazônia | 263.5 |
| e794da64-8dea-3f6c-8694-78d7f0e0f692 | -6.9416 | -42.8834 | 2025-06-28 02:10:00 | GOES-19 | FLORIANO | PIAUÍ | Brasil | 2203909 | 22 | 33 | nan | nan | nan | Caatinga | 69.9 |
| 1c348592-fbd8-310c-a121-e94ddc896199 | -12.2715 | -46.7739 | 2025-06-28 02:10:00 | GOES-19 | PONTE ALTA DO BOM JESUS | TOCANTINS | Brasil | 1717800 | 17 | 33 | nan | nan | nan | Cerrado | 62.1 |
| 88e30914-2901-3320-bf5e-49defb3bbc7f | -9.1208 | -49.4743 | 2025-06-28 02:10:00 | GOES-19 | ARAGUACEMA | TOCANTINS | Brasil | 1701903 | 17 | 33 | nan | nan | nan | Cerrado | 91.7 |
| cf752853-f656-35d1-ab6a-790f1b4bab3f | -9.7041 | -56.1843 | 2025-06-28 02:10:00 | GOES-19 | ALTA FLORESTA | MATO GROSSO | Brasil | 5100250 | 51 | 33 | nan | nan | nan | Amazônia | 68.3 |
| 20595a00-7ad1-33e6-b36c-ac75d1070dfd | -4.5429 | -48.0151 | 2025-06-28 02:10:00 | GOES-19 | RONDON DO PARÁ | PARÁ | Brasil | 1506187 | 15 | 33 | nan | nan | nan | Amazônia | 62.3 |
| a74fe106-61cb-308b-9ddf-1bd244f39a0c | -11.0266 | -55.3789 | 2025-06-28 02:10:00 | GOES-19 | ITAÚBA | MATO GROSSO | Brasil | 5104559 | 51 | 33 | nan | nan | nan | Amazônia | 58.7 |
| e514f5aa-3784-3c62-8396-5a4a19499bd8 | -6.892 | -43.9851 | 2025-06-28 02:10:00 | GOES-19 | PORTO ALEGRE DO PIAUÍ | PIAUÍ | Brasil | 2208551 | 22 | 33 | nan | nan | nan | Cerrado | 78.5 |
| dc8c99ff-3e75-3415-a336-b8cb4efd75c2 | -11.0644 | -55.3757 | 2025-06-28 02:10:00 | GOES-19 | ITAÚBA | MATO GROSSO | Brasil | 5104559 | 51 | 33 | nan | nan | nan | Amazônia | 70.2 |
| e75cc37b-bbec-3709-92d3-a4e3d1ed3929 | -11.2664 | -52.7527 | 2025-06-28 02:10:00 | GOES-19 | SÃO FÉLIX DO ARAGUAIA | MATO GROSSO | Brasil | 5107859 | 51 | 33 | nan | nan | nan | Amazônia | 161.7 |
| 68ece4d4-03d0-3cf6-abab-7886ac17ac64 | -9.1205 | -49.4958 | 2025-06-28 02:10:00 | GOES-19 | ARAGUACEMA | TOCANTINS | Brasil | 1701903 | 17 | 33 | nan | nan | nan | Cerrado | 94.2 |
| 9ce688d1-65ce-365a-a86a-0bb40a6a23e5 | -6.9108 | -43.9834 | 2025-06-28 02:10:00 | GOES-19 | PORTO ALEGRE DO PIAUÍ | PIAUÍ | Brasil | 2208551 | 22 | 33 | nan | nan | nan | Cerrado | 106.7 |
| 0c596f86-ff13-3db5-bb87-c49cf395c05c | -7.2217 | -43.0917 | 2025-06-28 02:10:00 | GOES-19 | FLORIANO | PIAUÍ | Brasil | 2203909 | 22 | 33 | nan | nan | nan | Caatinga | 92.3 |
| 8d2177e7-b689-3b3a-8c6d-3711015e01b8 | -9.1205 | -49.4958 | 2025-06-28 02:20:00 | GOES-19 | ARAGUACEMA | TOCANTINS | Brasil | 1701903 | 17 | 33 | nan | nan | nan | Cerrado | 80.4 |
| 33ca7ef2-7ed3-3da2-b6d0-ea1e82e70d3d | -16.2958 | -49.9575 | 2025-06-28 02:20:00 | GOES-19 | ANICUNS | GOIÁS | Brasil | 5201306 | 52 | 33 | nan | nan | nan | Cerrado | 43.2 |
| a7efeb51-5d03-33f2-a897-3090d81d842d | -11.0457 | -55.3571 | 2025-06-28 02:20:00 | GOES-19 | ITAÚBA | MATO GROSSO | Brasil | 5104559 | 51 | 33 | nan | nan | nan | Amazônia | 87.9 |
| ef822eb7-266a-382c-9e8e-ac2f1e909cb3 | -11.2664 | -52.7527 | 2025-06-28 02:20:00 | GOES-19 | SÃO FÉLIX DO ARAGUAIA | MATO GROSSO | Brasil | 5107859 | 51 | 33 | nan | nan | nan | Amazônia | 122.9 |
| 81e8dd62-1440-3d07-a942-c903a90818f1 | -4.5429 | -48.0151 | 2025-06-28 02:20:00 | GOES-19 | RONDON DO PARÁ | PARÁ | Brasil | 1506187 | 15 | 33 | nan | nan | nan | Amazônia | 60.8 |
| 56a453d4-0e67-3490-91bb-f0c5e66c5165 | -11.0455 | -55.3773 | 2025-06-28 02:20:00 | GOES-19 | ITAÚBA | MATO GROSSO | Brasil | 5104559 | 51 | 33 | nan | nan | nan | Amazônia | 230.6 |
| b86761f0-c4af-32ee-b0c1-45cb49a93985 | -7.2217 | -43.0917 | 2025-06-28 02:20:00 | GOES-19 | FLORIANO | PIAUÍ | Brasil | 2203909 | 22 | 33 | nan | nan | nan | Caatinga | 75.0 |
| 367d2cdd-728c-34f1-9573-dba5cbcde36d | -9.1208 | -49.4743 | 2025-06-28 02:20:00 | GOES-19 | ARAGUACEMA | TOCANTINS | Brasil | 1701903 | 17 | 33 | nan | nan | nan | Cerrado | 72.2 |
| 3cee0a19-77b0-3f88-8ddf-d3b3fb617930 | -7.2219 | -43.0682 | 2025-06-28 02:20:00 | GOES-19 | FLORIANO | PIAUÍ | Brasil | 2203909 | 22 | 33 | nan | nan | nan | Caatinga | 91.7 |
| ad250de0-7e29-3f04-9f4f-16e8d736d045 | -11.0644 | -55.3757 | 2025-06-28 02:20:00 | GOES-19 | ITAÚBA | MATO GROSSO | Brasil | 5104559 | 51 | 33 | nan | nan | nan | Amazônia | 68.4 |
| edf6a862-33bf-3971-baa7-5d383cc1c9ed | -5.4562 | -43.0788 | 2025-06-28 02:20:00 | GOES-19 | MATÕES | MARANHÃO | Brasil | 2106607 | 21 | 33 | nan | nan | nan | Cerrado | 50.0 |
| 1424e9f8-6cef-3911-89c7-46346fce5d52 | -9.7041 | -56.1843 | 2025-06-28 02:20:00 | GOES-19 | ALTA FLORESTA | MATO GROSSO | Brasil | 5100250 | 51 | 33 | nan | nan | nan | Amazônia | 69.2 |
| 6ece2841-64d2-3de8-a859-796ef3c336d5 | -12.2715 | -46.7739 | 2025-06-28 02:20:00 | GOES-19 | PONTE ALTA DO BOM JESUS | TOCANTINS | Brasil | 1717800 | 17 | 33 | nan | nan | nan | Cerrado | 68.4 |
| 951a8afc-a21b-38f6-bf27-75572eded882 | -6.9416 | -42.8834 | 2025-06-28 02:20:00 | GOES-19 | FLORIANO | PIAUÍ | Brasil | 2203909 | 22 | 33 | nan | nan | nan | Caatinga | 73.7 |
| 1da3715d-c089-3e83-8bcb-25087301259f | -9.7228 | -56.183 | 2025-06-28 02:20:00 | GOES-19 | ALTA FLORESTA | MATO GROSSO | Brasil | 5100250 | 51 | 33 | nan | nan | nan | Amazônia | 78.0 |
| c845585c-9005-342d-9e0d-b2099a8688b4 | -6.9108 | -43.9834 | 2025-06-28 02:20:00 | GOES-19 | PORTO ALEGRE DO PIAUÍ | PIAUÍ | Brasil | 2208551 | 22 | 33 | nan | nan | nan | Cerrado | 94.5 |
| 4dca6ca8-0dff-3b63-a83b-76e565ffca29 | -11.2666 | -52.7318 | 2025-06-28 02:20:00 | GOES-19 | SÃO FÉLIX DO ARAGUAIA | MATO GROSSO | Brasil | 5107859 | 51 | 33 | nan | nan | nan | Amazônia | 45.7 |
| 4b41698e-1368-37d3-bfce-1269a69c966d | -16.2962 | -49.9354 | 2025-06-28 02:20:00 | GOES-19 | ANICUNS | GOIÁS | Brasil | 5201306 | 52 | 33 | nan | nan | nan | Cerrado | 44.9 |
| 9cb39eab-c0a4-3ab4-a0ec-592b9b2b1a77 | -6.892 | -43.9851 | 2025-06-28 02:20:00 | GOES-19 | PORTO ALEGRE DO PIAUÍ | PIAUÍ | Brasil | 2208551 | 22 | 33 | nan | nan | nan | Cerrado | 80.5 |
| 62383af4-6133-336c-bd86-97787344aeee | -6.9416 | -42.8834 | 2025-06-28 02:30:00 | GOES-19 | FLORIANO | PIAUÍ | Brasil | 2203909 | 22 | 33 | nan | nan | nan | Caatinga | 77.2 |
| 8a429423-71d4-3e4a-8968-71c50e0bea8f | -4.5427 | -48.0367 | 2025-06-28 02:30:00 | GOES-19 | RONDON DO PARÁ | PARÁ | Brasil | 1506187 | 15 | 33 | nan | nan | nan | Amazônia | 64.2 |
| d169b9be-a599-399a-ae8b-0ce50f5641ea | -11.0455 | -55.3773 | 2025-06-28 02:30:00 | GOES-19 | ITAÚBA | MATO GROSSO | Brasil | 5104559 | 51 | 33 | nan | nan | nan | Amazônia | 190.4 |
| 92dc57c1-b098-3727-a71e-98f91cd35aa4 | -12.2715 | -46.7739 | 2025-06-28 02:30:00 | GOES-19 | PONTE ALTA DO BOM JESUS | TOCANTINS | Brasil | 1717800 | 17 | 33 | nan | nan | nan | Cerrado | 53.5 |
| 7446b247-388b-37c7-bef4-8b0379dde90c | -11.0457 | -55.3571 | 2025-06-28 02:30:00 | GOES-19 | ITAÚBA | MATO GROSSO | Brasil | 5104559 | 51 | 33 | nan | nan | nan | Amazônia | 84.1 |
| f8ec2e2b-3177-39e4-91df-9fc200464006 | -11.0644 | -55.3757 | 2025-06-28 02:30:00 | GOES-19 | ITAÚBA | MATO GROSSO | Brasil | 5104559 | 51 | 33 | nan | nan | nan | Amazônia | 74.1 |
| c40e8c7f-7557-356d-b6b5-ee683a594380 | -11.2664 | -52.7527 | 2025-06-28 02:30:00 | GOES-19 | SÃO FÉLIX DO ARAGUAIA | MATO GROSSO | Brasil | 5107859 | 51 | 33 | nan | nan | nan | Amazônia | 96.1 |
| 4d8fabe4-034b-3c9e-a32d-577efee81717 | -9.7041 | -56.1843 | 2025-06-28 02:30:00 | GOES-19 | ALTA FLORESTA | MATO GROSSO | Brasil | 5100250 | 51 | 33 | nan | nan | nan | Amazônia | 79.2 |
| 98720945-d0ab-3f84-8cad-e19c1518b299 | -9.1205 | -49.4958 | 2025-06-28 02:30:00 | GOES-19 | ARAGUACEMA | TOCANTINS | Brasil | 1701903 | 17 | 33 | nan | nan | nan | Cerrado | 75.8 |
| 0821bd5e-f8e9-30ed-8846-1eef44acbe3a | -7.2219 | -43.0682 | 2025-06-28 02:30:00 | GOES-19 | FLORIANO | PIAUÍ | Brasil | 2203909 | 22 | 33 | nan | nan | nan | Caatinga | 83.7 |
| 195ee674-ab93-32d9-a5d5-7f9358698e29 | -7.2217 | -43.0917 | 2025-06-28 02:30:00 | GOES-19 | FLORIANO | PIAUÍ | Brasil | 2203909 | 22 | 33 | nan | nan | nan | Caatinga | 68.3 |
| 73ea3183-9a45-32e4-b58d-5ef8d71473de | -6.892 | -43.9851 | 2025-06-28 02:30:00 | GOES-19 | PORTO ALEGRE DO PIAUÍ | PIAUÍ | Brasil | 2208551 | 22 | 33 | nan | nan | nan | Cerrado | 71.2 |
| a469cbcb-f473-3477-be91-bf36c391355b | -9.7228 | -56.183 | 2025-06-28 02:30:00 | GOES-19 | ALTA FLORESTA | MATO GROSSO | Brasil | 5100250 | 51 | 33 | nan | nan | nan | Amazônia | 73.2 |
| 0c047e81-3966-3bbf-98d0-d78533641f25 | -4.5429 | -48.0151 | 2025-06-28 02:30:00 | GOES-19 | RONDON DO PARÁ | PARÁ | Brasil | 1506187 | 15 | 33 | nan | nan | nan | Amazônia | 80.1 |
| 90ff55df-f10d-3677-8d95-8393b7beb63e | -9.1208 | -49.4743 | 2025-06-28 02:30:00 | GOES-19 | ARAGUACEMA | TOCANTINS | Brasil | 1701903 | 17 | 33 | nan | nan | nan | Cerrado | 67.3 |
| 33a2084c-8d37-3c7c-a71a-bcf31b05401d | -6.9108 | -43.9834 | 2025-06-28 02:30:00 | GOES-19 | PORTO ALEGRE DO PIAUÍ | PIAUÍ | Brasil | 2208551 | 22 | 33 | nan | nan | nan | Cerrado | 86.8 |
| d5eec50b-2332-3c8c-89bc-eaeb94b1dd6f | -6.892 | -43.9851 | 2025-06-28 02:40:00 | GOES-19 | PORTO ALEGRE DO PIAUÍ | PIAUÍ | Brasil | 2208551 | 22 | 33 | nan | nan | nan | Cerrado | 64.6 |
| 37e2ff13-9320-3123-9acd-40328d77dafe | -4.5429 | -48.0151 | 2025-06-28 02:40:00 | GOES-19 | RONDON DO PARÁ | PARÁ | Brasil | 1506187 | 15 | 33 | nan | nan | nan | Amazônia | 78.2 |
| c9944028-e08d-3c14-9cde-695338878adf | -6.9108 | -43.9834 | 2025-06-28 02:40:00 | GOES-19 | PORTO ALEGRE DO PIAUÍ | PIAUÍ | Brasil | 2208551 | 22 | 33 | nan | nan | nan | Cerrado | 85.2 |
| 0a73dfed-8572-31ff-9029-f8103669f6ba | -11.2664 | -52.7527 | 2025-06-28 02:40:00 | GOES-19 | SÃO FÉLIX DO ARAGUAIA | MATO GROSSO | Brasil | 5107859 | 51 | 33 | nan | nan | nan | Amazônia | 103.3 |
| 8b2a66d5-9786-361b-bb1e-074153d7e1f9 | -6.9416 | -42.8834 | 2025-06-28 02:40:00 | GOES-19 | FLORIANO | PIAUÍ | Brasil | 2203909 | 22 | 33 | nan | nan | nan | Caatinga | 79.1 |
| 2a0a8f2f-2923-37e4-86e8-fbf5740d91ad | -7.2219 | -43.0682 | 2025-06-28 02:40:00 | GOES-19 | FLORIANO | PIAUÍ | Brasil | 2203909 | 22 | 33 | nan | nan | nan | Caatinga | 73.4 |


[Clique aqui para ver as próximas entradas](README8.md)
