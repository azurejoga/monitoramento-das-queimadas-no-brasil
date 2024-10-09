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

## Dados Diários - Página 48

| ID | Latitude | Longitude | Data/Hora GMT | Satélite | Município | Estado | País | Município ID | Estado ID | País ID | Dias sem Chuva | Precipitação | Risco de Fogo | Bioma | FRP |
|----|----------|-----------|---------------|----------|-----------|--------|------|--------------|-----------|---------|----------------|--------------|----------------|-------|-----|
| 95bd867c-8d05-3962-9c54-ecd06c7d4353 | -8.5107 | -48.6459 | 2024-10-09 01:45:54 | GOES-16 | PRESIDENTE KENNEDY | TOCANTINS | Brasil | 1718402 | 17 | 33 | nan | nan | nan | Amazônia | 72.8 |
| 30498b95-3d14-3c29-8aa3-075e260a32ca | -9.4635 | -66.7469 | 2024-10-09 01:46:01 | GOES-16 | LÁBREA | AMAZONAS | Brasil | 1302405 | 13 | 33 | nan | nan | nan | Amazônia | 38.9 |
| 411adbf2-a0ed-36df-bfc7-967a09745eb6 | -10.3894 | -61.2502 | 2024-10-09 01:46:06 | GOES-16 | RONDOLÂNDIA | MATO GROSSO | Brasil | 5107578 | 51 | 33 | nan | nan | nan | Amazônia | 76.3 |
| d799fd76-9b0c-38b0-aa2a-06eafe593664 | -10.3895 | -61.231 | 2024-10-09 01:46:06 | GOES-16 | RONDOLÂNDIA | MATO GROSSO | Brasil | 5107578 | 51 | 33 | nan | nan | nan | Amazônia | 65.0 |
| f9ee371d-bb7b-3635-98d5-fedf39311c58 | -10.4287 | -60.9979 | 2024-10-09 01:46:06 | GOES-16 | RONDOLÂNDIA | MATO GROSSO | Brasil | 5107578 | 51 | 33 | nan | nan | nan | Amazônia | 55.8 |
| aea3a3b8-0e92-37cc-8cd0-6aaedda15730 | -10.8567 | -63.9177 | 2024-10-09 01:46:08 | GOES-16 | NOVA MAMORÉ | RONDÔNIA | Brasil | 1100338 | 11 | 33 | nan | nan | nan | Amazônia | 58.8 |
| 30bc260d-768e-337f-9c99-72e2f9cc8cdb | -10.8754 | -63.9169 | 2024-10-09 01:46:08 | GOES-16 | GUAJARÁ-MIRIM | RONDÔNIA | Brasil | 1100106 | 11 | 33 | nan | nan | nan | Amazônia | 103.7 |
| aacc7ce8-af35-3e90-bfa4-f3729dfe63c7 | -10.8755 | -63.8979 | 2024-10-09 01:46:08 | GOES-16 | GUAJARÁ-MIRIM | RONDÔNIA | Brasil | 1100106 | 11 | 33 | nan | nan | nan | Amazônia | 74.6 |
| 9340af49-3769-3b0b-9e79-448ce8b9ac5c | -10.8941 | -63.916 | 2024-10-09 01:46:09 | GOES-16 | GUAJARÁ-MIRIM | RONDÔNIA | Brasil | 1100106 | 11 | 33 | nan | nan | nan | Amazônia | 66.2 |
| acc1fa90-c128-3024-ae46-75125c264b85 | -10.9112 | -64.1615 | 2024-10-09 01:46:09 | GOES-16 | GUAJARÁ-MIRIM | RONDÔNIA | Brasil | 1100106 | 11 | 33 | nan | nan | nan | Amazônia | 103.5 |
| 8651b2e1-6af1-3f7d-a54b-aadeb0562192 | -10.9113 | -64.1426 | 2024-10-09 01:46:09 | GOES-16 | GUAJARÁ-MIRIM | RONDÔNIA | Brasil | 1100106 | 11 | 33 | nan | nan | nan | Amazônia | 93.1 |
| 83ff0c53-813f-3ef7-a11d-78b3ef873d1a | -11.2583 | -60.3885 | 2024-10-09 01:46:10 | GOES-16 | VILHENA | RONDÔNIA | Brasil | 1100304 | 11 | 33 | nan | nan | nan | Amazônia | 54.3 |
| 57bbf98a-8e58-3809-9e54-481358730924 | -11.3838 | -51.0807 | 2024-10-09 01:46:11 | GOES-16 | SÃO FÉLIX DO ARAGUAIA | MATO GROSSO | Brasil | 5107859 | 51 | 33 | nan | nan | nan | Cerrado | 42.1 |
| a584afad-2212-3fa5-8629-c404c907f1b4 | -11.6806 | -64.0312 | 2024-10-09 01:46:13 | GOES-16 | GUAJARÁ-MIRIM | RONDÔNIA | Brasil | 1100106 | 11 | 33 | nan | nan | nan | Amazônia | 69.2 |
| 4823b46e-3b60-3420-ad3d-ad279c6c84e4 | -11.7119 | -64.9966 | 2024-10-09 01:46:13 | GOES-16 | GUAJARÁ-MIRIM | RONDÔNIA | Brasil | 1100106 | 11 | 33 | nan | nan | nan | Amazônia | 61.4 |
| 1771d6c1-0991-3907-a6bb-ec301c67c60d | -11.9917 | -51.0766 | 2024-10-09 01:46:14 | GOES-16 | SÃO FÉLIX DO ARAGUAIA | MATO GROSSO | Brasil | 5107859 | 51 | 33 | nan | nan | nan | Cerrado | 78.6 |
| 3c91101d-ab03-3ba5-b5b1-033ef845150f | -11.992 | -51.0553 | 2024-10-09 01:46:14 | GOES-16 | SÃO FÉLIX DO ARAGUAIA | MATO GROSSO | Brasil | 5107859 | 51 | 33 | nan | nan | nan | Cerrado | 126.1 |
| 7b39a6af-f16e-3ca8-82de-b79550739aa1 | -12.0107 | -51.0744 | 2024-10-09 01:46:14 | GOES-16 | SÃO FÉLIX DO ARAGUAIA | MATO GROSSO | Brasil | 5107859 | 51 | 33 | nan | nan | nan | Cerrado | 120.9 |
| 2c338e25-55cf-3016-aecd-ed8f16fec400 | -12.011 | -51.0531 | 2024-10-09 01:46:14 | GOES-16 | SÃO FÉLIX DO ARAGUAIA | MATO GROSSO | Brasil | 5107859 | 51 | 33 | nan | nan | nan | Cerrado | 194.2 |
| 46745951-0360-3279-96fd-608d17412650 | -12.1895 | -50.5838 | 2024-10-09 01:46:15 | GOES-16 | FORMOSO DO ARAGUAIA | TOCANTINS | Brasil | 1708205 | 17 | 33 | nan | nan | nan | Cerrado | 98.1 |
| 3858b8a6-e608-335e-abfa-ef06be4ace92 | -12.2086 | -50.5815 | 2024-10-09 01:46:15 | GOES-16 | FORMOSO DO ARAGUAIA | TOCANTINS | Brasil | 1708205 | 17 | 33 | nan | nan | nan | Cerrado | 119.8 |
| e31ad130-5919-35f9-8f7f-50a3e3767e19 | -12.6676 | -63.0819 | 2024-10-09 01:46:18 | GOES-16 | SÃO FRANCISCO DO GUAPORÉ | RONDÔNIA | Brasil | 1101492 | 11 | 33 | nan | nan | nan | Amazônia | 76.0 |
| 9a0850f8-16d2-312b-9745-0c78117a91ff | -12.8591 | -62.8018 | 2024-10-09 01:46:20 | GOES-16 | SÃO FRANCISCO DO GUAPORÉ | RONDÔNIA | Brasil | 1101492 | 11 | 33 | nan | nan | nan | Amazônia | 106.3 |
| c8aa7063-261d-3e70-8eff-c75e21d6ea0d | -12.8779 | -62.82 | 2024-10-09 01:46:20 | GOES-16 | ALTA FLORESTA D'OESTE | RONDÔNIA | Brasil | 1100015 | 11 | 33 | nan | nan | nan | Amazônia | 61.1 |
| 4bbef670-8cce-31cc-894e-a61c61260de6 | -12.878 | -62.8007 | 2024-10-09 01:46:20 | GOES-16 | ALTA FLORESTA D'OESTE | RONDÔNIA | Brasil | 1100015 | 11 | 33 | nan | nan | nan | Amazônia | 142.2 |
| 128f7567-e950-3090-800b-d7b3ece084d1 | -12.8782 | -62.7815 | 2024-10-09 01:46:20 | GOES-16 | ALTA FLORESTA D'OESTE | RONDÔNIA | Brasil | 1100015 | 11 | 33 | nan | nan | nan | Amazônia | 63.1 |
| de523eb5-efbe-318e-b55b-4ca8be7e806e | -12.9166 | -62.7214 | 2024-10-09 01:46:20 | GOES-16 | SÃO FRANCISCO DO GUAPORÉ | RONDÔNIA | Brasil | 1101492 | 11 | 33 | nan | nan | nan | Amazônia | 59.3 |
| e010449f-1eca-3541-9c22-be20407acf1c | -12.9377 | -62.4697 | 2024-10-09 01:46:20 | GOES-16 | ALTA FLORESTA D'OESTE | RONDÔNIA | Brasil | 1100015 | 11 | 33 | nan | nan | nan | Amazônia | 34.6 |
| 24363217-3183-31ae-bae9-15be3a374dca | -12.9378 | -62.4504 | 2024-10-09 01:46:20 | GOES-16 | ALTA FLORESTA D'OESTE | RONDÔNIA | Brasil | 1100015 | 11 | 33 | nan | nan | nan | Amazônia | 47.5 |
| 7b2ab3ff-a1b9-39e4-9b08-c850a840a4d6 | -12.9566 | -62.4685 | 2024-10-09 01:46:20 | GOES-16 | ALTA FLORESTA D'OESTE | RONDÔNIA | Brasil | 1100015 | 11 | 33 | nan | nan | nan | Amazônia | 75.6 |
| 33978671-075e-36b3-8b5c-74a8384c6b45 | -12.9568 | -62.4492 | 2024-10-09 01:46:20 | GOES-16 | ALTA FLORESTA D'OESTE | RONDÔNIA | Brasil | 1100015 | 11 | 33 | nan | nan | nan | Amazônia | 83.4 |
| 5b3f1ab8-941f-3b45-ba66-58d1f198f03b | -12.9756 | -62.4673 | 2024-10-09 01:46:20 | GOES-16 | ALTA FLORESTA D'OESTE | RONDÔNIA | Brasil | 1100015 | 11 | 33 | nan | nan | nan | Amazônia | 92.7 |
| f0b16dda-cae6-3766-9d04-191edd98ede6 | -12.9757 | -62.448 | 2024-10-09 01:46:20 | GOES-16 | ALTA FLORESTA D'OESTE | RONDÔNIA | Brasil | 1100015 | 11 | 33 | nan | nan | nan | Amazônia | 73.3 |
| c9e5df7d-ec9c-3822-99c7-708093c9ef12 | -13.2871 | -53.7456 | 2024-10-09 01:46:21 | GOES-16 | GAÚCHA DO NORTE | MATO GROSSO | Brasil | 5103858 | 51 | 33 | nan | nan | nan | Amazônia | 83.4 |
| db9beafa-e06e-3df1-89af-09406111a6d6 | -13.2874 | -53.7248 | 2024-10-09 01:46:21 | GOES-16 | GAÚCHA DO NORTE | MATO GROSSO | Brasil | 5103858 | 51 | 33 | nan | nan | nan | Amazônia | 74.8 |
| 823b63fc-d919-3162-aa93-4ae68386bf81 | -13.3062 | -53.7435 | 2024-10-09 01:46:21 | GOES-16 | GAÚCHA DO NORTE | MATO GROSSO | Brasil | 5103858 | 51 | 33 | nan | nan | nan | Amazônia | 100.3 |
| b9eb725d-130d-3a2b-8a4e-85b317d67926 | -13.3065 | -53.7227 | 2024-10-09 01:46:21 | GOES-16 | GAÚCHA DO NORTE | MATO GROSSO | Brasil | 5103858 | 51 | 33 | nan | nan | nan | Amazônia | 85.7 |
| 3b16e670-f2f2-3154-ac56-92b9b347bd61 | -13.817 | -44.5961 | 2024-10-09 01:46:23 | GOES-16 | CORIBE | BAHIA | Brasil | 2909109 | 29 | 33 | nan | nan | nan | Cerrado | 70.8 |
| 0b66a74b-ea3a-342b-b1ed-7b56aa7d758d | -13.8364 | -44.5927 | 2024-10-09 01:46:23 | GOES-16 | CORIBE | BAHIA | Brasil | 2909109 | 29 | 33 | nan | nan | nan | Cerrado | 80.5 |
| 3e8efa19-5f68-3588-91d7-90605dee3618 | -13.8369 | -44.5691 | 2024-10-09 01:46:23 | GOES-16 | CORIBE | BAHIA | Brasil | 2909109 | 29 | 33 | nan | nan | nan | Cerrado | 91.5 |
| eb5e8bfe-c866-35a9-ac93-e2acfaa118b5 | -13.8564 | -44.5657 | 2024-10-09 01:46:24 | GOES-16 | CORIBE | BAHIA | Brasil | 2909109 | 29 | 33 | nan | nan | nan | Cerrado | 63.4 |
| 7c4e0fe9-1ebb-362d-ab06-6e1073c9209f | -14.1392 | -44.9603 | 2024-10-09 01:46:25 | GOES-16 | COCOS | BAHIA | Brasil | 2908101 | 29 | 33 | nan | nan | nan | Cerrado | 73.1 |
| 6e7537bd-e741-3b5c-88f0-bddd3aaae26e | -15.5996 | -57.3699 | 2024-10-09 01:46:34 | GOES-16 | PORTO ESTRELA | MATO GROSSO | Brasil | 5106851 | 51 | 33 | nan | nan | nan | Cerrado | 94.2 |
| 83ec8267-d04e-3bb7-b155-01bb83a3bee4 | -16.4184 | -55.9455 | 2024-10-09 01:46:39 | GOES-16 | BARÃO DE MELGAÇO | MATO GROSSO | Brasil | 5101605 | 51 | 33 | nan | nan | nan | Pantanal | 87.6 |
| 2c43550d-b2cf-364b-87fa-fa4e3e9b127c | -16.4187 | -55.9248 | 2024-10-09 01:46:39 | GOES-16 | BARÃO DE MELGAÇO | MATO GROSSO | Brasil | 5101605 | 51 | 33 | nan | nan | nan | Pantanal | 75.4 |
| 0092a263-0e45-3553-93c5-60e7637ee5df | -16.4379 | -55.9431 | 2024-10-09 01:46:39 | GOES-16 | BARÃO DE MELGAÇO | MATO GROSSO | Brasil | 5101605 | 51 | 33 | nan | nan | nan | Pantanal | 55.7 |
| 7f44c031-f672-3802-bd01-66da56e19b57 | -16.7067 | -57.4514 | 2024-10-09 01:46:40 | GOES-16 | CÁCERES | MATO GROSSO | Brasil | 5102504 | 51 | 33 | nan | nan | nan | Pantanal | 80.7 |
| 3a055b50-6067-3e7d-ab4e-90039c6c7b13 | -16.8045 | -57.4402 | 2024-10-09 01:46:41 | GOES-16 | CÁCERES | MATO GROSSO | Brasil | 5102504 | 51 | 33 | nan | nan | nan | Pantanal | 48.6 |
| dfb78b2d-21c3-32ac-817b-c601ae8fa830 | -16.8048 | -57.4197 | 2024-10-09 01:46:41 | GOES-16 | CÁCERES | MATO GROSSO | Brasil | 5102504 | 51 | 33 | nan | nan | nan | Pantanal | 43.1 |
| a7e43bc6-29e7-3678-ba87-8cb883e86080 | -16.8743 | -56.7352 | 2024-10-09 01:46:41 | GOES-16 | POCONÉ | MATO GROSSO | Brasil | 5106505 | 51 | 33 | nan | nan | nan | Pantanal | 63.7 |
| 52e0c095-4866-3f43-bd5f-2db4fafc6a00 | -16.9211 | -57.4881 | 2024-10-09 01:46:41 | GOES-16 | CÁCERES | MATO GROSSO | Brasil | 5102504 | 51 | 33 | nan | nan | nan | Pantanal | 70.1 |
| a1ec1a52-c8bf-3011-84d1-5f1a316fa462 | -16.9214 | -57.4676 | 2024-10-09 01:46:41 | GOES-16 | CÁCERES | MATO GROSSO | Brasil | 5102504 | 51 | 33 | nan | nan | nan | Pantanal | 48.9 |
| a15887e7-bdd1-3288-89c2-98dd5d6273e4 | -16.9407 | -57.4859 | 2024-10-09 01:46:42 | GOES-16 | CÁCERES | MATO GROSSO | Brasil | 5102504 | 51 | 33 | nan | nan | nan | Pantanal | 75.9 |
| 3d9a4e95-380a-3416-b553-0da2d8187756 | -16.941 | -57.4654 | 2024-10-09 01:46:42 | GOES-16 | CÁCERES | MATO GROSSO | Brasil | 5102504 | 51 | 33 | nan | nan | nan | Pantanal | 88.8 |
| 84c07ca3-8ee8-3e1b-9de8-9ef14582d4ef | -16.9413 | -57.4449 | 2024-10-09 01:46:42 | GOES-16 | CÁCERES | MATO GROSSO | Brasil | 5102504 | 51 | 33 | nan | nan | nan | Pantanal | 50.5 |
| d42cf8e7-e66c-3bfd-ae47-0db681272990 | -17.0979 | -57.4472 | 2024-10-09 01:46:42 | GOES-16 | CÁCERES | MATO GROSSO | Brasil | 5102504 | 51 | 33 | nan | nan | nan | Pantanal | 53.6 |
| 0410dc29-97a2-3e0a-886a-c39d7346e8f4 | -17.1175 | -57.4449 | 2024-10-09 01:46:43 | GOES-16 | CÁCERES | MATO GROSSO | Brasil | 5102504 | 51 | 33 | nan | nan | nan | Pantanal | 65.9 |
| b4261990-9bca-386d-9d01-9990dadfc1eb | -17.1271 | -56.8486 | 2024-10-09 01:46:43 | GOES-16 | POCONÉ | MATO GROSSO | Brasil | 5106505 | 51 | 33 | nan | nan | nan | Pantanal | 81.5 |
| dc66d4e5-6591-3ccb-8561-a88bf5482add | -17.1467 | -56.8463 | 2024-10-09 01:46:43 | GOES-16 | POCONÉ | MATO GROSSO | Brasil | 5106505 | 51 | 33 | nan | nan | nan | Pantanal | 87.1 |
| 212b3e31-f0af-3ace-a325-a09bd573fafd | -17.1588 | -56.1222 | 2024-10-09 01:46:43 | GOES-16 | BARÃO DE MELGAÇO | MATO GROSSO | Brasil | 5101605 | 51 | 33 | nan | nan | nan | Pantanal | 107.5 |
| 1108759f-2253-334b-ba6a-054a2552d276 | -17.335 | -55.0366 | 2024-10-09 01:46:43 | GOES-16 | ITIQUIRA | MATO GROSSO | Brasil | 5104609 | 51 | 33 | nan | nan | nan | Pantanal | 78.6 |
| b50dc42f-4c2b-3c26-b5bb-9d31f7d6d327 | -17.3353 | -55.0156 | 2024-10-09 01:46:43 | GOES-16 | ITIQUIRA | MATO GROSSO | Brasil | 5104609 | 51 | 33 | nan | nan | nan | Pantanal | 98.6 |
| 3bb80215-0f49-3e30-be64-a6f27d4a7c4f | -17.3547 | -55.0339 | 2024-10-09 01:46:44 | GOES-16 | ITIQUIRA | MATO GROSSO | Brasil | 5104609 | 51 | 33 | nan | nan | nan | Pantanal | 109.3 |
| f851aa48-08b2-3703-a38b-83aa205aa08a | -17.3551 | -55.0129 | 2024-10-09 01:46:44 | GOES-16 | ITIQUIRA | MATO GROSSO | Brasil | 5104609 | 51 | 33 | nan | nan | nan | Pantanal | 115.5 |
| a94986e0-fb73-363f-ac50-b270c4f75abf | -18.5993 | -57.2629 | 2024-10-09 01:46:50 | GOES-16 | CORUMBÁ | MATO GROSSO DO SUL | Brasil | 5003207 | 50 | 33 | nan | nan | nan | Pantanal | 46.6 |
| 1983b10c-4fa8-3fd6-8aec-00f36d796917 | -18.5996 | -57.2422 | 2024-10-09 01:46:50 | GOES-16 | CORUMBÁ | MATO GROSSO DO SUL | Brasil | 5003207 | 50 | 33 | nan | nan | nan | Pantanal | 48.2 |
| 53c80114-d7e6-30c8-81ee-a3c53a648514 | -18.6398 | -57.2163 | 2024-10-09 01:46:51 | GOES-16 | CORUMBÁ | MATO GROSSO DO SUL | Brasil | 5003207 | 50 | 33 | nan | nan | nan | Pantanal | 44.7 |
| 089b6105-367b-32a1-ae4d-2b31cc20cfca | -18.6597 | -57.2137 | 2024-10-09 01:46:51 | GOES-16 | CORUMBÁ | MATO GROSSO DO SUL | Brasil | 5003207 | 50 | 33 | nan | nan | nan | Pantanal | 48.4 |
| bcca1c33-47d6-345f-bdae-2389af5dbeaf | -20.1087 | -48.8261 | 2024-10-09 01:46:57 | GOES-16 | FRUTAL | MINAS GERAIS | Brasil | 3127107 | 31 | 33 | nan | nan | nan | Cerrado | 115.0 |
| 50664a71-3845-32b0-a796-b4429d336608 | -20.1291 | -48.8217 | 2024-10-09 01:46:58 | GOES-16 | FRUTAL | MINAS GERAIS | Brasil | 3127107 | 31 | 33 | nan | nan | nan | Cerrado | 103.8 |
| 7a85887a-3b3d-3f79-976f-65ed53798802 | -20.2915 | -43.9444 | 2024-10-09 01:46:58 | GOES-16 | ITABIRITO | MINAS GERAIS | Brasil | 3131901 | 31 | 33 | nan | nan | nan | Mata Atlântica | 109.8 |
| 41d40c41-ada2-3771-acda-94de7709bd1d | -20.3346 | -48.7307 | 2024-10-09 01:46:59 | GOES-16 | COLÔMBIA | SÃO PAULO | Brasil | 3512100 | 35 | 33 | nan | nan | nan | Cerrado | 277.2 |
| 8750b010-591f-39bd-9762-57ee8bfa7096 | -20.3352 | -48.7076 | 2024-10-09 01:46:59 | GOES-16 | COLÔMBIA | SÃO PAULO | Brasil | 3512100 | 35 | 33 | nan | nan | nan | Cerrado | 325.3 |
| 54142f55-9da9-350f-9b52-61ca1c2f32a3 | -20.3551 | -48.7262 | 2024-10-09 01:46:59 | GOES-16 | COLÔMBIA | SÃO PAULO | Brasil | 3512100 | 35 | 33 | nan | nan | nan | Cerrado | 510.4 |
| e35a1f70-aa65-3551-bdf3-58e7f0355c17 | -20.3557 | -48.7031 | 2024-10-09 01:46:59 | GOES-16 | COLÔMBIA | SÃO PAULO | Brasil | 3512100 | 35 | 33 | nan | nan | nan | Cerrado | 595.1 |
| 19e096b0-4130-3dd4-befb-00fe3651af4e | -20.3755 | -48.7217 | 2024-10-09 01:46:59 | GOES-16 | BARRETOS | SÃO PAULO | Brasil | 3505500 | 35 | 33 | nan | nan | nan | Cerrado | 237.5 |
| dc857168-3d50-3d4e-8abf-cb5333b67625 | -20.3761 | -48.6986 | 2024-10-09 01:46:59 | GOES-16 | BARRETOS | SÃO PAULO | Brasil | 3505500 | 35 | 33 | nan | nan | nan | Cerrado | 239.3 |
| c5b9ca67-5de2-3d8e-bac5-7fd6fcc34e28 | -20.7839 | -47.2559 | 2024-10-09 01:47:01 | GOES-16 | PATROCÍNIO PAULISTA | SÃO PAULO | Brasil | 3536307 | 35 | 33 | nan | nan | nan | Cerrado | 120.8 |
| cdc2cac7-5b46-3cdb-af15-eecc8099bd79 | -20.7846 | -47.2323 | 2024-10-09 01:47:01 | GOES-16 | PATROCÍNIO PAULISTA | SÃO PAULO | Brasil | 3536307 | 35 | 33 | nan | nan | nan | Cerrado | 106.3 |
| 70ea3f9c-390a-3bc4-8874-b8bf9bc98feb | -20.8045 | -47.251 | 2024-10-09 01:47:01 | GOES-16 | PATROCÍNIO PAULISTA | SÃO PAULO | Brasil | 3536307 | 35 | 33 | nan | nan | nan | Cerrado | 81.5 |
| 49f78898-46ca-370a-9455-36adf0383283 | -20.8052 | -47.2273 | 2024-10-09 01:47:01 | GOES-16 | PATROCÍNIO PAULISTA | SÃO PAULO | Brasil | 3536307 | 35 | 33 | nan | nan | nan | Cerrado | 81.0 |
| cae343c0-a6cb-3285-8aa6-1dba95b5acd8 | -21.0408 | -47.5696 | 2024-10-09 01:47:02 | GOES-16 | BRODOWSKI | SÃO PAULO | Brasil | 3507803 | 35 | 33 | nan | nan | nan | Cerrado | 68.5 |
| 39f27dfa-196f-3569-950d-05f8ad216b73 | -21.0926 | -47.2043 | 2024-10-09 01:47:02 | GOES-16 | SANTO ANTÔNIO DA ALEGRIA | SÃO PAULO | Brasil | 3547908 | 35 | 33 | nan | nan | nan | Cerrado | 82.0 |
| d9c975f9-3e0c-3f2e-a5e5-813ccf133f26 | -21.572 | -46.9898 | 2024-10-09 01:47:05 | GOES-16 | MOCOCA | SÃO PAULO | Brasil | 3530508 | 35 | 33 | nan | nan | nan | Cerrado | 98.9 |
| bece436e-59f9-3cbf-87d8-7bcd3781344d | -21.5727 | -46.9659 | 2024-10-09 01:47:05 | GOES-16 | MOCOCA | SÃO PAULO | Brasil | 3530508 | 35 | 33 | nan | nan | nan | Cerrado | 124.1 |
| 74cd3cca-0d2a-36f4-b4ab-1c23afba38ac | -21.5864 | -47.8827 | 2024-10-09 01:47:05 | GOES-16 | LUÍS ANTÔNIO | SÃO PAULO | Brasil | 3527603 | 35 | 33 | nan | nan | nan | Cerrado | 84.2 |
| a5fbfdf0-fd43-3cfc-b75a-9bc41fab3cdc | -22.8137 | -48.4225 | 2024-10-09 01:47:11 | GOES-16 | BOTUCATU | SÃO PAULO | Brasil | 3507506 | 35 | 33 | nan | nan | nan | Cerrado | 79.2 |
| 4f14a7a7-a018-31ee-8906-59f54796ff84 | -1.11 | -53.6173 | 2024-10-09 01:55:12 | GOES-16 | ALMEIRIM | PARÁ | Brasil | 1500503 | 15 | 33 | nan | nan | nan | Amazônia | 98.3 |
| b532c127-1b17-3699-a3f8-d48c58ccde23 | -3.8008 | -41.5989 | 2024-10-09 01:55:27 | GOES-16 | PIRACURUCA | PIAUÍ | Brasil | 2208304 | 22 | 33 | nan | nan | nan | Caatinga | 96.9 |
| 4716ff75-0372-328a-939e-0a9dcab32d28 | -3.8196 | -41.5979 | 2024-10-09 01:55:28 | GOES-16 | PIRACURUCA | PIAUÍ | Brasil | 2208304 | 22 | 33 | nan | nan | nan | Caatinga | 78.4 |
| e96f9f4c-9a4c-3e96-aef6-43ec004f8620 | -3.9021 | -46.4689 | 2024-10-09 01:55:28 | GOES-16 | BOM JARDIM | MARANHÃO | Brasil | 2102002 | 21 | 33 | nan | nan | nan | Amazônia | 61.9 |
| 97aef7e0-c796-3beb-bd15-376fb529e22d | -3.9023 | -46.4467 | 2024-10-09 01:55:28 | GOES-16 | BOM JARDIM | MARANHÃO | Brasil | 2102002 | 21 | 33 | nan | nan | nan | Amazônia | 67.3 |
| 4dcbb26e-1ab8-3c90-8b43-703a417eb604 | -3.9208 | -46.4459 | 2024-10-09 01:55:28 | GOES-16 | BOM JARDIM | MARANHÃO | Brasil | 2102002 | 21 | 33 | nan | nan | nan | Amazônia | 79.8 |
| c953308f-0e34-3b64-854f-0a16973bc5fc | -3.9393 | -46.4672 | 2024-10-09 01:55:28 | GOES-16 | BOM JARDIM | MARANHÃO | Brasil | 2102002 | 21 | 33 | nan | nan | nan | Amazônia | 51.4 |
| b7901ced-4a60-3096-9da3-9117fbcb7903 | -3.9394 | -46.445 | 2024-10-09 01:55:28 | GOES-16 | BOM JARDIM | MARANHÃO | Brasil | 2102002 | 21 | 33 | nan | nan | nan | Amazônia | 122.5 |
| e0cd1b46-3df3-3922-b735-1f2a6ddde3f1 | -6.9825 | -34.9441 | 2024-10-09 01:55:45 | GOES-16 | SANTA RITA | PARAÍBA | Brasil | 2513703 | 25 | 33 | nan | nan | nan | Mata Atlântica | 65.0 |
| 88ea31cb-d6d3-3a85-8ee1-2b0b141f6506 | -6.7613 | -60.0751 | 2024-10-09 01:55:45 | GOES-16 | NOVO ARIPUANÃ | AMAZONAS | Brasil | 1303304 | 13 | 33 | nan | nan | nan | Amazônia | 50.2 |
| a35e2a92-e969-34cb-9df0-ca7b4c0e0aad | -6.7614 | -60.0559 | 2024-10-09 01:55:45 | GOES-16 | NOVO ARIPUANÃ | AMAZONAS | Brasil | 1303304 | 13 | 33 | nan | nan | nan | Amazônia | 195.0 |
| 68720288-480b-3c79-85aa-8056d7397669 | -6.7615 | -60.0367 | 2024-10-09 01:55:45 | GOES-16 | NOVO ARIPUANÃ | AMAZONAS | Brasil | 1303304 | 13 | 33 | nan | nan | nan | Amazônia | 61.9 |
| 1de6abd9-c5fe-376d-abde-c3643b8ca161 | -6.7797 | -60.0744 | 2024-10-09 01:55:45 | GOES-16 | NOVO ARIPUANÃ | AMAZONAS | Brasil | 1303304 | 13 | 33 | nan | nan | nan | Amazônia | 39.7 |


[Clique aqui para ver as próximas entradas](README49.md)
