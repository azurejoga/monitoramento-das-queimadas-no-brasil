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

## Dados Diários - Página 5

| ID | Latitude | Longitude | Data/Hora GMT | Satélite | Município | Estado | País | Município ID | Estado ID | País ID | Dias sem Chuva | Precipitação | Risco de Fogo | Bioma | FRP |
|----|----------|-----------|---------------|----------|-----------|--------|------|--------------|-----------|---------|----------------|--------------|----------------|-------|-----|
| 29cb6501-c99e-3e29-bdda-988191b2d7f2 | -11.91424 | -57.11888 | 2026-06-28 00:41:00 | TERRA_M-M | PORTO DOS GAÚCHOS | MATO GROSSO | Brasil | 5106802 | 51 | 33 | nan | nan | nan | Amazônia | 7.5 |
| 1fff2189-fb33-3984-90d4-06d43dcfe73a | -12.20033 | -52.89645 | 2026-06-28 00:41:00 | TERRA_M-M | QUERÊNCIA | MATO GROSSO | Brasil | 5107065 | 51 | 33 | nan | nan | nan | Amazônia | 96.1 |
| f88fad93-ba63-3296-a633-81a0724ce0a2 | -13.25215 | -54.39769 | 2026-06-28 00:41:00 | TERRA_M-M | PARANATINGA | MATO GROSSO | Brasil | 5106307 | 51 | 33 | nan | nan | nan | Amazônia | 8.6 |
| 33edb67a-757c-316b-be2e-ad564f1ba88d | -11.92493 | -57.40847 | 2026-06-28 00:41:00 | TERRA_M-M | NOVA MARINGÁ | MATO GROSSO | Brasil | 5108907 | 51 | 33 | nan | nan | nan | Amazônia | 6.8 |
| 206749c2-3ebc-33cd-a934-f9da74513820 | -12.07713 | -52.00939 | 2026-06-28 00:41:00 | TERRA_M-M | BOM JESUS DO ARAGUAIA | MATO GROSSO | Brasil | 5101852 | 51 | 33 | nan | nan | nan | Amazônia | 16.4 |
| ad202850-4e0f-3846-9d85-ba02da550122 | -11.66577 | -57.25542 | 2026-06-28 00:41:00 | TERRA_M-M | PORTO DOS GAÚCHOS | MATO GROSSO | Brasil | 5106802 | 51 | 33 | nan | nan | nan | Amazônia | 109.0 |
| 4fc05961-bbf2-395a-b6b3-8339a81bbf4f | -11.21582 | -54.33713 | 2026-06-28 00:41:00 | TERRA_M-M | MARCELÂNDIA | MATO GROSSO | Brasil | 5105580 | 51 | 33 | nan | nan | nan | Amazônia | 9.3 |
| 18bdad3e-3c4e-3219-9809-a3771490b1dc | -12.08629 | -51.99847 | 2026-06-28 00:41:00 | TERRA_M-M | BOM JESUS DO ARAGUAIA | MATO GROSSO | Brasil | 5101852 | 51 | 33 | nan | nan | nan | Amazônia | 47.9 |
| a1e8dd66-870d-3446-a2dc-93f213ffc407 | -12.59725 | -57.88832 | 2026-06-28 00:41:00 | TERRA_M-M | BRASNORTE | MATO GROSSO | Brasil | 5101902 | 51 | 33 | nan | nan | nan | Cerrado | 88.0 |
| b017efd6-103c-3614-a00e-0e9b486837a9 | -12.18391 | -57.15048 | 2026-06-28 00:41:00 | TERRA_M-M | NOVA MARINGÁ | MATO GROSSO | Brasil | 5108907 | 51 | 33 | nan | nan | nan | Amazônia | 21.9 |
| 07683dd0-6da7-3f29-99f3-faf97a214ce0 | -12.45571 | -58.48014 | 2026-06-28 00:41:00 | TERRA_M-M | SAPEZAL | MATO GROSSO | Brasil | 5107875 | 51 | 33 | nan | nan | nan | Cerrado | 10.3 |
| 6c733d6c-09b7-3097-8757-e77463f3f89b | -12.79631 | -54.88614 | 2026-06-28 00:41:00 | TERRA_M-M | NOVA UBIRATÃ | MATO GROSSO | Brasil | 5106240 | 51 | 33 | nan | nan | nan | Amazônia | 18.7 |
| 7e67930f-0fd4-3bbb-ba3f-5af95e6bd595 | -4.28291 | -48.38176 | 2026-06-28 00:43:00 | TERRA_M-M | RONDON DO PARÁ | PARÁ | Brasil | 1506187 | 15 | 33 | nan | nan | nan | Amazônia | 26.6 |
| c3186470-9863-3691-8122-fa4e7fa97acb | -10.2941 | -57.138 | 2026-06-28 00:50:00 | GOES-19 | NOVA MONTE VERDE | MATO GROSSO | Brasil | 5108956 | 51 | 33 | nan | nan | nan | Amazônia | 110.9 |
| 5a8b7784-a722-3faf-a463-016df8360f6b | -12.6048 | -57.8743 | 2026-06-28 00:50:00 | GOES-19 | BRASNORTE | MATO GROSSO | Brasil | 5101902 | 51 | 33 | nan | nan | nan | Cerrado | 101.7 |
| 318b5a37-2453-355d-b200-7babadaa9440 | -10.2942 | -57.1182 | 2026-06-28 00:50:00 | GOES-19 | NOVA MONTE VERDE | MATO GROSSO | Brasil | 5108956 | 51 | 33 | nan | nan | nan | Amazônia | 137.7 |
| 8f2e7f62-6490-31d7-af32-2129a46c62cf | -11.5243 | -54.7872 | 2026-06-28 00:50:00 | GOES-19 | CLÁUDIA | MATO GROSSO | Brasil | 5103056 | 51 | 33 | nan | nan | nan | Amazônia | 78.3 |
| 68b0a4ac-6056-3dce-bbf4-faf18ec0b8a9 | -11.6657 | -57.2536 | 2026-06-28 00:50:00 | GOES-19 | PORTO DOS GAÚCHOS | MATO GROSSO | Brasil | 5106802 | 51 | 33 | nan | nan | nan | Amazônia | 98.3 |
| 118d323d-cf24-381e-aec8-54f6f5988bea | -12.0733 | -51.9987 | 2026-06-28 00:50:00 | GOES-19 | BOM JESUS DO ARAGUAIA | MATO GROSSO | Brasil | 5101852 | 51 | 33 | nan | nan | nan | Amazônia | 61.0 |
| d576edee-fff4-3529-a88b-40bc8b103519 | -18.4795 | -54.1105 | 2026-06-28 00:50:00 | GOES-19 | COXIM | MATO GROSSO DO SUL | Brasil | 5003306 | 50 | 33 | nan | nan | nan | Cerrado | 74.7 |
| 39fd20f7-5fd6-3daa-af27-535287a663ca | -18.48 | -54.0891 | 2026-06-28 00:50:00 | GOES-19 | COXIM | MATO GROSSO DO SUL | Brasil | 5003306 | 50 | 33 | nan | nan | nan | Cerrado | 47.8 |
| cc947fa9-07a0-35c4-88b5-c96d26e3939c | -12.4651 | -58.5009 | 2026-06-28 00:50:00 | GOES-19 | SAPEZAL | MATO GROSSO | Brasil | 5107875 | 51 | 33 | nan | nan | nan | Cerrado | 73.9 |
| 9a4dada5-1bd2-3804-bd9e-19077e465c54 | -12.1111 | -52.0155 | 2026-06-28 00:50:00 | GOES-19 | BOM JESUS DO ARAGUAIA | MATO GROSSO | Brasil | 5101852 | 51 | 33 | nan | nan | nan | Amazônia | 70.2 |
| 2677166c-b27a-323b-98f8-f2bd902b51be | -12.2412 | -56.545 | 2026-06-28 00:50:00 | GOES-19 | ITANHANGÁ | MATO GROSSO | Brasil | 5104542 | 51 | 33 | nan | nan | nan | Amazônia | 44.1 |
| 202040ca-57e4-36e0-b59a-5836492c052c | -17.3041 | -42.643 | 2026-06-28 00:50:00 | GOES-19 | MINAS NOVAS | MINAS GERAIS | Brasil | 3141801 | 31 | 33 | nan | nan | nan | Cerrado | 49.4 |
| cf8a17ca-65ad-35fc-acab-784ce670260f | -12.1775 | -57.1319 | 2026-06-28 00:50:00 | GOES-19 | NOVA MARINGÁ | MATO GROSSO | Brasil | 5108907 | 51 | 33 | nan | nan | nan | Amazônia | 67.3 |
| 56e102a9-9c38-353e-b69d-6fde905d4ea1 | -12.0923 | -51.9966 | 2026-06-28 00:50:00 | GOES-19 | BOM JESUS DO ARAGUAIA | MATO GROSSO | Brasil | 5101852 | 51 | 33 | nan | nan | nan | Amazônia | 113.7 |
| cf522076-32ce-3f99-b115-c6ae05d207d5 | -12.6046 | -57.8942 | 2026-06-28 00:50:00 | GOES-19 | BRASNORTE | MATO GROSSO | Brasil | 5101902 | 51 | 33 | nan | nan | nan | Cerrado | 96.9 |
| 35a2d0cd-9fb4-30e0-9872-97d97f39bf4c | -9.0796 | -59.4098 | 2026-06-28 00:50:00 | GOES-19 | COLNIZA | MATO GROSSO | Brasil | 5103254 | 51 | 33 | nan | nan | nan | Amazônia | 66.3 |
| dd8c9f0a-723d-325a-8f43-a7254725259c | -12.4654 | -58.481 | 2026-06-28 00:50:00 | GOES-19 | SAPEZAL | MATO GROSSO | Brasil | 5107875 | 51 | 33 | nan | nan | nan | Cerrado | 50.2 |
| 4b4bdf44-d009-36fb-811c-6368946743ae | -12.1773 | -57.1519 | 2026-06-28 00:50:00 | GOES-19 | NOVA MARINGÁ | MATO GROSSO | Brasil | 5108907 | 51 | 33 | nan | nan | nan | Amazônia | 61.7 |
| 3ff1b72f-fac4-3d5b-91f0-f5aa81b88f06 | -9.0982 | -59.4088 | 2026-06-28 00:50:00 | GOES-19 | COLNIZA | MATO GROSSO | Brasil | 5103254 | 51 | 33 | nan | nan | nan | Amazônia | 82.1 |
| fe18279a-6c06-35de-9f92-f4e13191a1a7 | -10.313 | -57.1169 | 2026-06-28 00:50:00 | GOES-19 | JUARA | MATO GROSSO | Brasil | 5105101 | 51 | 33 | nan | nan | nan | Amazônia | 69.2 |
| a099b862-031d-364b-b80f-4c7089fdf6f0 | -12.1585 | -57.1335 | 2026-06-28 00:50:00 | GOES-19 | NOVA MARINGÁ | MATO GROSSO | Brasil | 5108907 | 51 | 33 | nan | nan | nan | Amazônia | 46.5 |
| 60c97737-223e-37f3-a729-4354172be516 | -12.073 | -52.0197 | 2026-06-28 00:50:00 | GOES-19 | BOM JESUS DO ARAGUAIA | MATO GROSSO | Brasil | 5101852 | 51 | 33 | nan | nan | nan | Amazônia | 91.7 |
| d7533220-2c58-3a89-bcfc-3322cb47ee8a | -12.092 | -52.0176 | 2026-06-28 00:50:00 | GOES-19 | BOM JESUS DO ARAGUAIA | MATO GROSSO | Brasil | 5101852 | 51 | 33 | nan | nan | nan | Amazônia | 197.4 |
| 21b29905-a905-3049-8707-fbb89c6dda6c | -10.3128 | -57.1367 | 2026-06-28 00:50:00 | GOES-19 | JUARA | MATO GROSSO | Brasil | 5105101 | 51 | 33 | nan | nan | nan | Amazônia | 62.9 |
| 34f06344-fb0c-322c-90cb-24f69f2f1b61 | -10.313 | -57.1169 | 2026-06-28 01:00:00 | GOES-19 | JUARA | MATO GROSSO | Brasil | 5105101 | 51 | 33 | nan | nan | nan | Amazônia | 89.7 |
| 397e9b2b-a9e3-3a70-9dfd-bcdea624358c | -12.1111 | -52.0155 | 2026-06-28 01:00:00 | GOES-19 | BOM JESUS DO ARAGUAIA | MATO GROSSO | Brasil | 5101852 | 51 | 33 | nan | nan | nan | Amazônia | 64.6 |
| a973b0c3-9c27-3386-a20f-6274d03ce6c3 | -12.0923 | -51.9966 | 2026-06-28 01:00:00 | GOES-19 | BOM JESUS DO ARAGUAIA | MATO GROSSO | Brasil | 5101852 | 51 | 33 | nan | nan | nan | Amazônia | 100.0 |
| 877694d7-0641-3a5d-9e1c-a9a00a338800 | -12.073 | -52.0197 | 2026-06-28 01:00:00 | GOES-19 | BOM JESUS DO ARAGUAIA | MATO GROSSO | Brasil | 5101852 | 51 | 33 | nan | nan | nan | Amazônia | 84.4 |
| 4374bfee-e56f-341e-b043-99bd11dd5d43 | -17.3041 | -42.643 | 2026-06-28 01:00:00 | GOES-19 | MINAS NOVAS | MINAS GERAIS | Brasil | 3141801 | 31 | 33 | nan | nan | nan | Cerrado | 54.4 |
| 754b9194-4a95-3412-8866-fb12997b69e2 | -9.0982 | -59.4088 | 2026-06-28 01:00:00 | GOES-19 | COLNIZA | MATO GROSSO | Brasil | 5103254 | 51 | 33 | nan | nan | nan | Amazônia | 66.2 |
| ee7b72f9-e7c1-39d0-81b2-1c05879b2757 | -12.4654 | -58.481 | 2026-06-28 01:00:00 | GOES-19 | SAPEZAL | MATO GROSSO | Brasil | 5107875 | 51 | 33 | nan | nan | nan | Cerrado | 55.3 |
| 90dc11f6-2f32-30b8-804d-123367ed82ac | -18.4795 | -54.1105 | 2026-06-28 01:00:00 | GOES-19 | COXIM | MATO GROSSO DO SUL | Brasil | 5003306 | 50 | 33 | nan | nan | nan | Cerrado | 76.6 |
| 18d9884d-e71f-3a99-a0e0-873aa6a243b4 | -10.2942 | -57.1182 | 2026-06-28 01:00:00 | GOES-19 | NOVA MONTE VERDE | MATO GROSSO | Brasil | 5108956 | 51 | 33 | nan | nan | nan | Amazônia | 109.8 |
| 05a41222-b249-371d-89d3-3a4c6bc7b0f9 | -10.2941 | -57.138 | 2026-06-28 01:00:00 | GOES-19 | NOVA MONTE VERDE | MATO GROSSO | Brasil | 5108956 | 51 | 33 | nan | nan | nan | Amazônia | 87.1 |
| 256f99ab-4b30-3705-8508-144212fbb9a3 | -10.3128 | -57.1367 | 2026-06-28 01:00:00 | GOES-19 | JUARA | MATO GROSSO | Brasil | 5105101 | 51 | 33 | nan | nan | nan | Amazônia | 77.3 |
| 2f32a2b1-29b7-378d-975e-949865b5b916 | -12.1773 | -57.1519 | 2026-06-28 01:00:00 | GOES-19 | NOVA MARINGÁ | MATO GROSSO | Brasil | 5108907 | 51 | 33 | nan | nan | nan | Amazônia | 58.9 |
| 866763f7-190c-3316-b93c-2eb03c27108e | -12.6046 | -57.8942 | 2026-06-28 01:00:00 | GOES-19 | BRASNORTE | MATO GROSSO | Brasil | 5101902 | 51 | 33 | nan | nan | nan | Cerrado | 78.1 |
| 9886d7ca-c3da-3612-987d-b53f0c7bd550 | -9.0796 | -59.4098 | 2026-06-28 01:00:00 | GOES-19 | COLNIZA | MATO GROSSO | Brasil | 5103254 | 51 | 33 | nan | nan | nan | Amazônia | 75.7 |
| 53009e64-3ecd-31de-8d2d-a9f24dffd841 | -12.6048 | -57.8743 | 2026-06-28 01:00:00 | GOES-19 | BRASNORTE | MATO GROSSO | Brasil | 5101902 | 51 | 33 | nan | nan | nan | Cerrado | 92.2 |
| 1061f903-fdee-317b-a462-482b1fd9c868 | -12.1775 | -57.1319 | 2026-06-28 01:00:00 | GOES-19 | NOVA MARINGÁ | MATO GROSSO | Brasil | 5108907 | 51 | 33 | nan | nan | nan | Amazônia | 68.2 |
| 9cb6b14b-4877-303c-bad7-b6db9b2aa926 | -11.5243 | -54.7872 | 2026-06-28 01:00:00 | GOES-19 | CLÁUDIA | MATO GROSSO | Brasil | 5103056 | 51 | 33 | nan | nan | nan | Amazônia | 81.3 |
| 72cb4cb7-2b74-3872-9ced-e672de05ebdb | -11.6657 | -57.2536 | 2026-06-28 01:00:00 | GOES-19 | PORTO DOS GAÚCHOS | MATO GROSSO | Brasil | 5106802 | 51 | 33 | nan | nan | nan | Amazônia | 87.8 |
| 7e50935c-1107-3bac-b922-2543fe7ea521 | -12.092 | -52.0176 | 2026-06-28 01:00:00 | GOES-19 | BOM JESUS DO ARAGUAIA | MATO GROSSO | Brasil | 5101852 | 51 | 33 | nan | nan | nan | Amazônia | 181.9 |
| 3d922d18-126c-3581-a4be-5a3991976a7c | -11.209 | -54.3053 | 2026-06-28 01:00:00 | GOES-19 | MARCELÂNDIA | MATO GROSSO | Brasil | 5105580 | 51 | 33 | nan | nan | nan | Amazônia | 45.6 |
| 5445dfb6-52d8-3778-bd8f-0768cb55c04b | -12.4651 | -58.5009 | 2026-06-28 01:00:00 | GOES-19 | SAPEZAL | MATO GROSSO | Brasil | 5107875 | 51 | 33 | nan | nan | nan | Cerrado | 76.9 |
| 062e17e6-f6fb-3e32-b249-d17a99a1706a | -12.6163 | -57.882 | 2026-06-28 01:00:00 | METOP-C | BRASNORTE | MATO GROSSO | Brasil | 5101902 | 51 | 33 | nan | nan | nan | Cerrado | nan |
| 99aaf587-a264-3f22-a084-27b93372ac06 | -11.9212 | -58.665501 | 2026-06-28 01:00:00 | METOP-C | JUÍNA | MATO GROSSO | Brasil | 5105150 | 51 | 33 | nan | nan | nan | Cerrado | nan |
| 4809149f-f99c-332f-99f9-8b69bf8ac73f | -17.309601 | -42.6525 | 2026-06-28 01:00:00 | METOP-C | MINAS NOVAS | MINAS GERAIS | Brasil | 3141801 | 31 | 33 | nan | nan | nan | Cerrado | nan |
| c574a6e2-de1f-3bc3-aac1-9e29103231d5 | -18.4876 | -54.096699 | 2026-06-28 01:00:00 | METOP-C | COXIM | MATO GROSSO DO SUL | Brasil | 5003306 | 50 | 33 | nan | nan | nan | Cerrado | nan |
| a476abf8-83c1-365a-817c-f2b4ce9a9037 | -12.2283 | -56.553902 | 2026-06-28 01:00:00 | METOP-C | ITANHANGÁ | MATO GROSSO | Brasil | 5104542 | 51 | 33 | nan | nan | nan | Amazônia | nan |
| 3bf94560-ba35-3f9d-ad5d-375f61087eb0 | -12.1761 | -52.9076 | 2026-06-28 01:00:00 | METOP-C | QUERÊNCIA | MATO GROSSO | Brasil | 5107065 | 51 | 33 | nan | nan | nan | Amazônia | nan |
| e6461315-1104-342a-a8e9-5716c08e7e89 | -11.2153 | -53.814999 | 2026-06-28 01:00:00 | METOP-C | MARCELÂNDIA | MATO GROSSO | Brasil | 5105580 | 51 | 33 | nan | nan | nan | Amazônia | nan |
| 1940a2ed-e2ea-3af4-9c69-a76667ce11fd | -18.479601 | -54.107399 | 2026-06-28 01:00:00 | METOP-C | COXIM | MATO GROSSO DO SUL | Brasil | 5003306 | 50 | 33 | nan | nan | nan | Cerrado | nan |
| 93dfacc8-d128-3fb2-aa6f-ec891fbd27ee | -10.7863 | -54.106899 | 2026-06-28 01:00:00 | METOP-C | MARCELÂNDIA | MATO GROSSO | Brasil | 5105580 | 51 | 33 | nan | nan | nan | Amazônia | nan |
| 952af12e-e801-38d0-875a-216d4cc47a36 | -12.4676 | -58.500999 | 2026-06-28 01:00:00 | METOP-C | SAPEZAL | MATO GROSSO | Brasil | 5107875 | 51 | 33 | nan | nan | nan | Cerrado | nan |
| 9d7c4864-bce6-3bad-80eb-f47713be833c | -10.2932 | -57.125 | 2026-06-28 01:00:00 | METOP-C | NOVA MONTE VERDE | MATO GROSSO | Brasil | 5108956 | 51 | 33 | nan | nan | nan | Amazônia | nan |
| 079e4f30-21df-3e6b-b5cd-8c314d926cbd | -12.794 | -54.880299 | 2026-06-28 01:00:00 | METOP-C | NOVA UBIRATÃ | MATO GROSSO | Brasil | 5106240 | 51 | 33 | nan | nan | nan | Amazônia | nan |
| 1bb2ccde-17a7-3d7f-8b80-941f8f8a5c59 | -12.2105 | -52.877701 | 2026-06-28 01:00:00 | METOP-C | QUERÊNCIA | MATO GROSSO | Brasil | 5107065 | 51 | 33 | nan | nan | nan | Amazônia | nan |
| d1967c80-d436-3138-955d-507097de364e | -12.1812 | -52.884399 | 2026-06-28 01:00:00 | METOP-C | QUERÊNCIA | MATO GROSSO | Brasil | 5107065 | 51 | 33 | nan | nan | nan | Amazônia | nan |
| e60eeb9c-af6e-3065-a619-4d46aaabaeb0 | -12.0952 | -52.000599 | 2026-06-28 01:00:00 | METOP-C | BOM JESUS DO ARAGUAIA | MATO GROSSO | Brasil | 5101852 | 51 | 33 | nan | nan | nan | Amazônia | nan |
| 6506e23c-4793-3d79-83e0-09e6eb387c59 | -9.0792 | -59.3983 | 2026-06-28 01:00:00 | METOP-C | COLNIZA | MATO GROSSO | Brasil | 5103254 | 51 | 33 | nan | nan | nan | Amazônia | nan |
| 63c37b72-3ca5-39e3-a0ba-4c82416abf75 | -12.1875 | -52.912399 | 2026-06-28 01:00:00 | METOP-C | QUERÊNCIA | MATO GROSSO | Brasil | 5107065 | 51 | 33 | nan | nan | nan | Amazônia | nan |
| 5e530eff-705f-36a2-a076-0df27e58addc | -17.319201 | -42.6497 | 2026-06-28 01:00:00 | METOP-C | MINAS NOVAS | MINAS GERAIS | Brasil | 3141801 | 31 | 33 | nan | nan | nan | Cerrado | nan |
| e0c484f4-eefd-3daa-9f14-6a7bee9c3c49 | -11.6628 | -57.268299 | 2026-06-28 01:00:00 | METOP-C | PORTO DOS GAÚCHOS | MATO GROSSO | Brasil | 5106802 | 51 | 33 | nan | nan | nan | Amazônia | nan |
| 133f6796-fcc2-3bcc-9726-1f771aebd83b | -16.047199 | -50.5611 | 2026-06-28 01:00:00 | METOP-C | NOVO BRASIL | GOIÁS | Brasil | 5215207 | 52 | 33 | nan | nan | nan | Cerrado | nan |
| 0194248d-ecab-30cb-9ce4-91a0334d7fad | -12.1973 | -52.910198 | 2026-06-28 01:00:00 | METOP-C | QUERÊNCIA | MATO GROSSO | Brasil | 5107065 | 51 | 33 | nan | nan | nan | Amazônia | nan |
| 38bc49a0-c815-320f-902c-2ce2b9187a5c | -11.6607 | -57.258099 | 2026-06-28 01:00:00 | METOP-C | PORTO DOS GAÚCHOS | MATO GROSSO | Brasil | 5106802 | 51 | 33 | nan | nan | nan | Amazônia | nan |
| 52dd5eb9-aad8-31ea-84b6-0fac69dbdf15 | -12.1652 | -57.130501 | 2026-06-28 01:00:00 | METOP-C | NOVA MARINGÁ | MATO GROSSO | Brasil | 5108907 | 51 | 33 | nan | nan | nan | Amazônia | nan |
| 0dbeb215-7f8c-322f-b8c2-80d9a36f0d0b | -11.5226 | -54.791599 | 2026-06-28 01:00:00 | METOP-C | CLÁUDIA | MATO GROSSO | Brasil | 5103056 | 51 | 33 | nan | nan | nan | Amazônia | nan |
| 7a82d153-499f-3584-8bd5-196a4250ca7d | -18.476101 | -54.090302 | 2026-06-28 01:00:00 | METOP-C | COXIM | MATO GROSSO DO SUL | Brasil | 5003306 | 50 | 33 | nan | nan | nan | Cerrado | nan |
| 54e2df95-2a1a-3a6e-80df-0c72e8e10891 | -12.0984 | -52.014599 | 2026-06-28 01:00:00 | METOP-C | BOM JESUS DO ARAGUAIA | MATO GROSSO | Brasil | 5101852 | 51 | 33 | nan | nan | nan | Amazônia | nan |
| 02f95d4b-0754-3282-8f2b-2bf3309dce40 | -12.0886 | -52.016899 | 2026-06-28 01:00:00 | METOP-C | BOM JESUS DO ARAGUAIA | MATO GROSSO | Brasil | 5101852 | 51 | 33 | nan | nan | nan | Amazônia | nan |
| 0e10f2fb-d9ff-3245-9f27-4ea139d3ea4e | -11.5341 | -54.7971 | 2026-06-28 01:00:00 | METOP-C | CLÁUDIA | MATO GROSSO | Brasil | 5103056 | 51 | 33 | nan | nan | nan | Amazônia | nan |
| 32cb79c9-9d33-3ca9-887b-9a062bf3ed9c | -12.1863 | -52.861099 | 2026-06-28 01:00:00 | METOP-C | QUERÊNCIA | MATO GROSSO | Brasil | 5107065 | 51 | 33 | nan | nan | nan | Amazônia | nan |
| bc038131-8d62-3883-a4cf-093edc3924cf | -12.0902 | -52.023899 | 2026-06-28 01:00:00 | METOP-C | BOM JESUS DO ARAGUAIA | MATO GROSSO | Brasil | 5101852 | 51 | 33 | nan | nan | nan | Amazônia | nan |
| 4e1b2fef-9b4f-3cbc-bc81-099d69603870 | -12.4554 | -58.490398 | 2026-06-28 01:00:00 | METOP-C | SAPEZAL | MATO GROSSO | Brasil | 5107875 | 51 | 33 | nan | nan | nan | Cerrado | nan |
| f449ddc3-6a7b-3eb8-a6d2-ca08f731e498 | -12.1911 | -57.156898 | 2026-06-28 01:00:00 | METOP-C | NOVA MARINGÁ | MATO GROSSO | Brasil | 5108907 | 51 | 33 | nan | nan | nan | Amazônia | nan |
| 2d79ddbe-a8bf-34ab-be97-ef8a1f72bcb4 | -11.6683 | -57.2458 | 2026-06-28 01:00:00 | METOP-C | PORTO DOS GAÚCHOS | MATO GROSSO | Brasil | 5106802 | 51 | 33 | nan | nan | nan | Amazônia | nan |
| 63fbf4dc-727d-3ec0-a4d0-ad43895240ab | -11.521 | -54.783901 | 2026-06-28 01:00:00 | METOP-C | CLÁUDIA | MATO GROSSO | Brasil | 5103056 | 51 | 33 | nan | nan | nan | Amazônia | nan |
| cb147519-012a-37fc-bffe-087e150563cf | -12.189 | -57.146702 | 2026-06-28 01:00:00 | METOP-C | NOVA MARINGÁ | MATO GROSSO | Brasil | 5108907 | 51 | 33 | nan | nan | nan | Amazônia | nan |
| 22d29236-b39f-3e19-ac06-04b2f37df70f | -12.0968 | -52.007599 | 2026-06-28 01:00:00 | METOP-C | BOM JESUS DO ARAGUAIA | MATO GROSSO | Brasil | 5101852 | 51 | 33 | nan | nan | nan | Amazônia | nan |
| 5f2135c5-8dd7-31a5-b330-9b7210446fbe | -11.2214 | -54.3078 | 2026-06-28 01:00:00 | METOP-C | MARCELÂNDIA | MATO GROSSO | Brasil | 5105580 | 51 | 33 | nan | nan | nan | Amazônia | nan |
| 879b1d2d-cfea-328c-9bf2-f282e9ac4470 | -11.21 | -54.302601 | 2026-06-28 01:00:00 | METOP-C | MARCELÂNDIA | MATO GROSSO | Brasil | 5105580 | 51 | 33 | nan | nan | nan | Amazônia | nan |
| 5c3b6469-75d3-34c9-b63f-532b6fed5cd8 | -12.0936 | -51.993599 | 2026-06-28 01:00:00 | METOP-C | BOM JESUS DO ARAGUAIA | MATO GROSSO | Brasil | 5101852 | 51 | 33 | nan | nan | nan | Amazônia | nan |
| d3e5c092-987a-30b2-b687-57aa6ca857c6 | -12.1957 | -52.903198 | 2026-06-28 01:00:00 | METOP-C | QUERÊNCIA | MATO GROSSO | Brasil | 5107065 | 51 | 33 | nan | nan | nan | Amazônia | nan |
| 8939a8d9-3782-3f8f-9627-427abb20101c | -11.5243 | -54.799301 | 2026-06-28 01:00:00 | METOP-C | CLÁUDIA | MATO GROSSO | Brasil | 5103056 | 51 | 33 | nan | nan | nan | Amazônia | nan |
| 11cde423-c4d4-3f41-b380-3a215c45da57 | -11.2084 | -54.2953 | 2026-06-28 01:00:00 | METOP-C | MARCELÂNDIA | MATO GROSSO | Brasil | 5105580 | 51 | 33 | nan | nan | nan | Amazônia | nan |


[Clique aqui para ver as próximas entradas](README6.md)
