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

## Dados Diários - Página 1

| ID | Latitude | Longitude | Data/Hora GMT | Satélite | Município | Estado | País | Município ID | Estado ID | País ID | Dias sem Chuva | Precipitação | Risco de Fogo | Bioma | FRP |
|----|----------|-----------|---------------|----------|-----------|--------|------|--------------|-----------|---------|----------------|--------------|----------------|-------|-----|
| 1787967d-2c0c-35c9-b880-90083795a2da | -5.871 | -57.7715 | 2026-08-30 00:00:00 | GOES-19 | JACAREACANGA | PARÁ | Brasil | 1503754 | 15 | 33 | nan | nan | nan | Amazônia | 84.1 |
| 6f7cbd9b-d912-3521-91ee-b41857e1e73b | -13.856 | -54.1175 | 2026-08-30 00:00:00 | GOES-19 | PARANATINGA | MATO GROSSO | Brasil | 5106307 | 51 | 33 | nan | nan | nan | Cerrado | 312.6 |
| 81bf74b2-ae0c-3703-b0a3-3b4972a7853c | -5.8894 | -57.7708 | 2026-08-30 00:00:00 | GOES-19 | JACAREACANGA | PARÁ | Brasil | 1503754 | 15 | 33 | nan | nan | nan | Amazônia | 93.5 |
| b4115249-ad5f-3f9a-b174-8d6e88d5fd06 | -11.2879 | -54.0317 | 2026-08-30 00:00:00 | GOES-19 | UNIÃO DO SUL | MATO GROSSO | Brasil | 5108303 | 51 | 33 | nan | nan | nan | Amazônia | 89.6 |
| fbee1c94-a6ef-33d6-8b57-b05df77e20bb | -7.2933 | -60.5905 | 2026-08-30 00:00:00 | GOES-19 | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 83.1 |
| a163bf09-ea24-39e3-99b1-603453c9a2c3 | -11.4369 | -61.4801 | 2026-08-30 00:00:00 | GOES-19 | CACOAL | RONDÔNIA | Brasil | 1100049 | 11 | 33 | nan | nan | nan | Amazônia | 61.8 |
| aad34f7d-9a38-389e-a7e9-cc1be2e2d23a | -4.1516 | -60.6878 | 2026-08-30 00:00:00 | GOES-19 | CAREIRO | AMAZONAS | Brasil | 1301100 | 13 | 33 | nan | nan | nan | Amazônia | 48.8 |
| 231acdd3-846c-3438-9b4c-7112f4f13e63 | -4.9604 | -55.8424 | 2026-08-30 00:00:00 | GOES-19 | TRAIRÃO | PARÁ | Brasil | 1508050 | 15 | 33 | nan | nan | nan | Amazônia | 50.5 |
| a3fcdd6d-d3ab-3bf7-b284-5de805fa8d79 | -7.5662 | -61.3049 | 2026-08-30 00:00:00 | GOES-19 | MANICORÉ | AMAZONAS | Brasil | 1302702 | 13 | 33 | nan | nan | nan | Amazônia | 61.5 |
| f38c546e-54c1-3474-ad6b-695c49bb52db | -10.8058 | -45.3407 | 2026-08-30 00:00:00 | GOES-19 | FORMOSA DO RIO PRETO | BAHIA | Brasil | 2911105 | 29 | 33 | nan | nan | nan | Cerrado | 73.7 |
| 474426f2-9b27-3a1c-a4aa-c6aeb8c22727 | -7.5661 | -61.3239 | 2026-08-30 00:00:00 | GOES-19 | MANICORÉ | AMAZONAS | Brasil | 1302702 | 13 | 33 | nan | nan | nan | Amazônia | 78.7 |
| 0b6d2c7b-4710-3e63-a665-f02e85ea9358 | -7.5136 | -55.3251 | 2026-08-30 00:00:00 | GOES-19 | NOVO PROGRESSO | PARÁ | Brasil | 1505031 | 15 | 33 | nan | nan | nan | Amazônia | 71.8 |
| bd77e6e0-604c-30be-a196-d9116e63aeee | -6.8568 | -59.4757 | 2026-08-30 00:00:00 | GOES-19 | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 53.0 |
| 9e6108d6-74bf-3057-9765-48990430f889 | -9.043 | -65.4175 | 2026-08-30 00:00:00 | GOES-19 | LÁBREA | AMAZONAS | Brasil | 1302405 | 13 | 33 | nan | nan | nan | Amazônia | 80.8 |
| c4ad2fa3-ba6a-319b-aa3b-d3e1d18769c1 | -13.8368 | -54.1197 | 2026-08-30 00:00:00 | GOES-19 | PARANATINGA | MATO GROSSO | Brasil | 5106307 | 51 | 33 | nan | nan | nan | Cerrado | 57.6 |
| b2225bbd-dffb-3040-8588-14bb655c6ae1 | -7.2932 | -60.6096 | 2026-08-30 00:00:00 | GOES-19 | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 86.6 |
| 9c1dd253-fb1c-39a7-af1e-b4891b412d14 | -9.8927 | -60.2752 | 2026-08-30 00:00:00 | GOES-19 | ARIPUANÃ | MATO GROSSO | Brasil | 5101407 | 51 | 33 | nan | nan | nan | Amazônia | 130.2 |
| 53fd09fb-b83c-3b95-8785-80929382026a | -10.7454 | -50.6812 | 2026-08-30 00:00:00 | GOES-19 | LUCIARA | MATO GROSSO | Brasil | 5105309 | 51 | 33 | nan | nan | nan | Cerrado | 80.8 |
| 00cc1db0-8594-3969-bce5-4ba79f3a1857 | -9.0615 | -65.4169 | 2026-08-30 00:00:00 | GOES-19 | LÁBREA | AMAZONAS | Brasil | 1302405 | 13 | 33 | nan | nan | nan | Amazônia | 95.5 |
| 462666a3-dfc8-3899-9f3d-a0e2c87ea64a | -3.7532 | -59.3423 | 2026-08-30 00:00:00 | GOES-19 | AUTAZES | AMAZONAS | Brasil | 1300300 | 13 | 33 | nan | nan | nan | Amazônia | 52.2 |
| 3ce2f997-94d1-3617-8fd9-d9c35797ea81 | -3.6398 | -60.5656 | 2026-08-30 00:00:00 | GOES-19 | MANAQUIRI | AMAZONAS | Brasil | 1302553 | 13 | 33 | nan | nan | nan | Amazônia | 102.5 |
| 1bc4d35a-bd7b-3d78-88ea-b538cda0c2ef | -9.9468 | -60.5232 | 2026-08-30 00:00:00 | GOES-19 | ARIPUANÃ | MATO GROSSO | Brasil | 5101407 | 51 | 33 | nan | nan | nan | Amazônia | 56.5 |
| 782ef1a0-1841-3c0b-a1d5-2f8a3756b544 | -16.1428 | -43.0347 | 2026-08-30 00:00:00 | GOES-19 | RIACHO DOS MACHADOS | MINAS GERAIS | Brasil | 3154507 | 31 | 33 | nan | nan | nan | Cerrado | 148.2 |
| c6915f32-e558-385c-8d75-876ce6b9b00f | -5.4876 | -57.1416 | 2026-08-30 00:00:00 | GOES-19 | ITAITUBA | PARÁ | Brasil | 1503606 | 15 | 33 | nan | nan | nan | Amazônia | 77.1 |
| 034b079e-87f6-3794-b14f-0a59b6353701 | -10.7457 | -50.6599 | 2026-08-30 00:00:00 | GOES-19 | LUCIARA | MATO GROSSO | Brasil | 5105309 | 51 | 33 | nan | nan | nan | Cerrado | 91.8 |
| 7719365a-1e96-328c-b937-7b9714e53856 | -14.4 | -52.565 | 2026-08-30 00:00:00 | GOES-19 | NOVA XAVANTINA | MATO GROSSO | Brasil | 5106257 | 51 | 33 | nan | nan | nan | Cerrado | 74.2 |
| 285618a3-4e92-342c-9dde-2ee6064d007e | -6.9361 | -55.7157 | 2026-08-30 00:00:00 | GOES-19 | NOVO PROGRESSO | PARÁ | Brasil | 1505031 | 15 | 33 | nan | nan | nan | Amazônia | 106.3 |
| c9fa5c1d-ff68-3e72-9682-a0a5c6830c17 | -7.3118 | -60.5897 | 2026-08-30 00:00:00 | GOES-19 | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 66.0 |
| 191885ba-bdf3-335c-861e-872877d8be42 | -3.6399 | -60.5466 | 2026-08-30 00:00:00 | GOES-19 | MANAQUIRI | AMAZONAS | Brasil | 1302553 | 13 | 33 | nan | nan | nan | Amazônia | 95.7 |
| 7f94e1dc-a0de-31f7-8d66-5182958f00a8 | -16.1421 | -43.0592 | 2026-08-30 00:00:00 | GOES-19 | RIACHO DOS MACHADOS | MINAS GERAIS | Brasil | 3154507 | 31 | 33 | nan | nan | nan | Cerrado | 90.3 |
| 459137ca-dac3-389f-9252-dac06f87b1af | -8.1348 | -45.4696 | 2026-08-30 00:00:00 | GOES-19 | RIBEIRO GONÇALVES | PIAUÍ | Brasil | 2208908 | 22 | 33 | nan | nan | nan | Cerrado | 70.6 |
| 2c872db9-f747-34ad-b3b2-960b7c329e79 | -10.7644 | -50.6792 | 2026-08-30 00:00:00 | GOES-19 | LUCIARA | MATO GROSSO | Brasil | 5105309 | 51 | 33 | nan | nan | nan | Cerrado | 70.6 |
| c4b4702b-a961-3740-b06a-d13ff1ab61e1 | -5.8895 | -57.7513 | 2026-08-30 00:00:00 | GOES-19 | JACAREACANGA | PARÁ | Brasil | 1503754 | 15 | 33 | nan | nan | nan | Amazônia | 53.5 |
| 0dae357d-7e81-3b27-8f92-11171b83b6e9 | -3.7716 | -59.3227 | 2026-08-30 00:00:00 | GOES-19 | AUTAZES | AMAZONAS | Brasil | 1300300 | 13 | 33 | nan | nan | nan | Amazônia | 65.2 |
| 5522d67f-14f3-35a8-a523-d7722eee1726 | -7.3117 | -60.6089 | 2026-08-30 00:00:00 | GOES-19 | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 98.5 |
| c4eba5f4-462a-3afa-a500-801ac06ed10b | -4.858 | -42.9566 | 2026-08-30 00:00:00 | GOES-19 | CAXIAS | MARANHÃO | Brasil | 2103000 | 21 | 33 | nan | nan | nan | Cerrado | 63.4 |
| 88bf4d6b-c256-3c29-a80c-e8fc2a2b555d | -11.3068 | -54.0299 | 2026-08-30 00:00:00 | GOES-19 | UNIÃO DO SUL | MATO GROSSO | Brasil | 5108303 | 51 | 33 | nan | nan | nan | Amazônia | 66.6 |
| ac6fdd7b-38a5-39e8-8eb7-57e5b670889b | -10.9401 | -43.0355 | 2026-08-30 00:00:00 | GOES-19 | BARRA | BAHIA | Brasil | 2902708 | 29 | 33 | nan | nan | nan | Cerrado | 90.5 |
| faedacbe-3321-39a4-ad14-60cda5e410c5 | -3.7715 | -59.3419 | 2026-08-30 00:00:00 | GOES-19 | AUTAZES | AMAZONAS | Brasil | 1300300 | 13 | 33 | nan | nan | nan | Amazônia | 98.3 |
| 452cd908-8d5a-3c77-afda-cffd2b459e5e | -10.7407 | -54.0401 | 2026-08-30 00:00:00 | GOES-19 | MARCELÂNDIA | MATO GROSSO | Brasil | 5105580 | 51 | 33 | nan | nan | nan | Amazônia | 84.3 |
| 9570c25b-e3ef-3461-8be2-c24e6867ab3f | -10.8062 | -45.3178 | 2026-08-30 00:00:00 | GOES-19 | FORMOSA DO RIO PRETO | BAHIA | Brasil | 2911105 | 29 | 33 | nan | nan | nan | Cerrado | 101.5 |
| 23fecb58-0268-3621-9db8-10030f37d890 | -3.6216 | -60.547 | 2026-08-30 00:00:00 | GOES-19 | MANAQUIRI | AMAZONAS | Brasil | 1302553 | 13 | 33 | nan | nan | nan | Amazônia | 63.4 |
| f53c6fe1-b3b5-3661-a855-4c71bac428d9 | -11.2877 | -54.0522 | 2026-08-30 00:00:00 | GOES-19 | UNIÃO DO SUL | MATO GROSSO | Brasil | 5108303 | 51 | 33 | nan | nan | nan | Amazônia | 53.5 |
| 167b729a-1321-37e4-bd2d-20a76401239e | -5.5042 | -44.0277 | 2026-08-30 00:00:00 | GOES-19 | GOVERNADOR LUIZ ROCHA | MARANHÃO | Brasil | 2104628 | 21 | 33 | nan | nan | nan | Cerrado | 53.9 |
| ec2973b0-a9de-37a8-893e-a5e65583e880 | -7.5477 | -61.3247 | 2026-08-30 00:00:00 | GOES-19 | MANICORÉ | AMAZONAS | Brasil | 1302702 | 13 | 33 | nan | nan | nan | Amazônia | 74.0 |
| 6f2b7bbf-12e6-34c1-bc50-443809c4fc2f | -16.3531 | -50.9775 | 2026-08-30 00:00:00 | GOES-19 | ISRAELÂNDIA | GOIÁS | Brasil | 5210307 | 52 | 33 | nan | nan | nan | Cerrado | 127.4 |
| f489b460-66a5-3e3a-8c70-ea53b864ec64 | -13.8557 | -54.1383 | 2026-08-30 00:00:00 | GOES-19 | PARANATINGA | MATO GROSSO | Brasil | 5106307 | 51 | 33 | nan | nan | nan | Cerrado | 385.0 |
| ca471168-9f39-3583-83ed-58ad85fab58a | -13.8749 | -54.1361 | 2026-08-30 00:00:00 | GOES-19 | PARANATINGA | MATO GROSSO | Brasil | 5106307 | 51 | 33 | nan | nan | nan | Cerrado | 216.9 |
| 987c2c97-6205-30b2-831b-e26818d894c6 | -7.5478 | -61.3056 | 2026-08-30 00:00:00 | GOES-19 | MANICORÉ | AMAZONAS | Brasil | 1302702 | 13 | 33 | nan | nan | nan | Amazônia | 55.0 |
| ff2c111e-e955-320c-8bc8-2f1184f1cf5e | -3.6215 | -60.566 | 2026-08-30 00:00:00 | GOES-19 | MANAQUIRI | AMAZONAS | Brasil | 1302553 | 13 | 33 | nan | nan | nan | Amazônia | 49.8 |
| 08a53571-0ad1-324e-b330-88b543105035 | -5.4875 | -57.1611 | 2026-08-30 00:00:00 | GOES-19 | ITAITUBA | PARÁ | Brasil | 1503606 | 15 | 33 | nan | nan | nan | Amazônia | 55.1 |
| 60549e05-8f98-3709-a509-a0fd9863959e | -13.8752 | -54.1153 | 2026-08-30 00:00:00 | GOES-19 | PARANATINGA | MATO GROSSO | Brasil | 5106307 | 51 | 33 | nan | nan | nan | Cerrado | 148.8 |
| 740bb305-f787-3b7a-9519-e332be0ac999 | -6.9363 | -55.6958 | 2026-08-30 00:00:00 | GOES-19 | NOVO PROGRESSO | PARÁ | Brasil | 1505031 | 15 | 33 | nan | nan | nan | Amazônia | 75.5 |
| 5c7aba13-13f3-3fab-96f0-26a6e0c4798e | -10.9593 | -43.0326 | 2026-08-30 00:00:00 | GOES-19 | BARRA | BAHIA | Brasil | 2902708 | 29 | 33 | nan | nan | nan | Cerrado | 119.5 |
| d5295670-b363-3c08-8a63-f32ddb2cea30 | -10.7871 | -45.3203 | 2026-08-30 00:00:00 | GOES-19 | FORMOSA DO RIO PRETO | BAHIA | Brasil | 2911105 | 29 | 33 | nan | nan | nan | Cerrado | 50.6 |
| 0b2e3436-adb1-39fc-ba06-a6af12f4a11d | -10.8062 | -45.3178 | 2026-08-30 00:10:00 | GOES-19 | FORMOSA DO RIO PRETO | BAHIA | Brasil | 2911105 | 29 | 33 | nan | nan | nan | Cerrado | 426.0 |
| c9e273b4-083f-3b30-8738-c00b8ec0c433 | -6.9363 | -55.6958 | 2026-08-30 00:10:00 | GOES-19 | NOVO PROGRESSO | PARÁ | Brasil | 1505031 | 15 | 33 | nan | nan | nan | Amazônia | 70.0 |
| 5152f8f8-8785-3a87-8a13-37124f07320a | -5.4876 | -57.1416 | 2026-08-30 00:10:00 | GOES-19 | ITAITUBA | PARÁ | Brasil | 1503606 | 15 | 33 | nan | nan | nan | Amazônia | 83.4 |
| ad93dac6-2e2f-3c05-8c6c-8c03c913f8d8 | -11.2879 | -54.0317 | 2026-08-30 00:10:00 | GOES-19 | UNIÃO DO SUL | MATO GROSSO | Brasil | 5108303 | 51 | 33 | nan | nan | nan | Amazônia | 89.2 |
| 079238c0-f238-3a2c-9d23-8eb1c81d3838 | -16.1428 | -43.0347 | 2026-08-30 00:10:00 | GOES-19 | RIACHO DOS MACHADOS | MINAS GERAIS | Brasil | 3154507 | 31 | 33 | nan | nan | nan | Cerrado | 98.9 |
| c872a7ad-2789-3485-9bb4-51a6d24e8315 | -4.9604 | -55.8424 | 2026-08-30 00:10:00 | GOES-19 | TRAIRÃO | PARÁ | Brasil | 1508050 | 15 | 33 | nan | nan | nan | Amazônia | 54.9 |
| 141257eb-777e-33a1-b8fd-169e6239769a | -7.4952 | -55.3062 | 2026-08-30 00:10:00 | GOES-19 | NOVO PROGRESSO | PARÁ | Brasil | 1505031 | 15 | 33 | nan | nan | nan | Amazônia | 59.0 |
| 40e7008a-3db2-3eef-b0b1-ad7943183615 | -13.8368 | -54.1197 | 2026-08-30 00:10:00 | GOES-19 | PARANATINGA | MATO GROSSO | Brasil | 5106307 | 51 | 33 | nan | nan | nan | Cerrado | 77.3 |
| d996822d-48fe-3e58-8aa0-0a15b36a5521 | -6.8568 | -59.4757 | 2026-08-30 00:10:00 | GOES-19 | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 58.6 |
| 2d4e9529-dbc4-34a8-a73f-8990f15b025b | -9.0615 | -65.4169 | 2026-08-30 00:10:00 | GOES-19 | LÁBREA | AMAZONAS | Brasil | 1302405 | 13 | 33 | nan | nan | nan | Amazônia | 83.2 |
| d0dc67ca-879d-378a-bd46-e90a15c42c80 | -11.2877 | -54.0522 | 2026-08-30 00:10:00 | GOES-19 | UNIÃO DO SUL | MATO GROSSO | Brasil | 5108303 | 51 | 33 | nan | nan | nan | Amazônia | 71.9 |
| d8773aaf-190e-3c65-b639-152746734064 | -10.8253 | -45.3152 | 2026-08-30 00:10:00 | GOES-19 | FORMOSA DO RIO PRETO | BAHIA | Brasil | 2911105 | 29 | 33 | nan | nan | nan | Cerrado | 46.5 |
| 54f4cbf0-42d7-3a02-a9a6-656584aede55 | -3.6216 | -60.547 | 2026-08-30 00:10:00 | GOES-19 | MANAQUIRI | AMAZONAS | Brasil | 1302553 | 13 | 33 | nan | nan | nan | Amazônia | 78.1 |
| 0a889944-e92b-37c0-b0b8-f62d72bd9d26 | -4.1515 | -60.7068 | 2026-08-30 00:10:00 | GOES-19 | CAREIRO | AMAZONAS | Brasil | 1301100 | 13 | 33 | nan | nan | nan | Amazônia | 42.3 |
| 8306fe58-7304-3c5a-964a-17411c6cda08 | -7.2932 | -60.6096 | 2026-08-30 00:10:00 | GOES-19 | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 52.3 |
| e5e6d3d7-2cae-363c-9dc8-b4be484ea09a | -4.1516 | -60.6878 | 2026-08-30 00:10:00 | GOES-19 | CAREIRO | AMAZONAS | Brasil | 1301100 | 13 | 33 | nan | nan | nan | Amazônia | 53.2 |
| 0ed4ec67-2787-3701-9330-6975fbe22c38 | -7.5477 | -61.3247 | 2026-08-30 00:10:00 | GOES-19 | MANICORÉ | AMAZONAS | Brasil | 1302702 | 13 | 33 | nan | nan | nan | Amazônia | 77.9 |
| c14d110e-3989-30a4-a76f-c67046e99d9e | -3.6399 | -60.5466 | 2026-08-30 00:10:00 | GOES-19 | MANAQUIRI | AMAZONAS | Brasil | 1302553 | 13 | 33 | nan | nan | nan | Amazônia | 48.6 |
| f6dadac8-3084-3f7e-95d8-a8dda28de439 | -6.9361 | -55.7157 | 2026-08-30 00:10:00 | GOES-19 | NOVO PROGRESSO | PARÁ | Brasil | 1505031 | 15 | 33 | nan | nan | nan | Amazônia | 123.2 |
| 33372d1e-8c7d-3d96-b0ec-980708e44091 | -3.7716 | -59.3227 | 2026-08-30 00:10:00 | GOES-19 | AUTAZES | AMAZONAS | Brasil | 1300300 | 13 | 33 | nan | nan | nan | Amazônia | 48.9 |
| ffbb2eae-6928-326a-b729-5d0d239316a9 | -16.3531 | -50.9775 | 2026-08-30 00:10:00 | GOES-19 | ISRAELÂNDIA | GOIÁS | Brasil | 5210307 | 52 | 33 | nan | nan | nan | Cerrado | 106.9 |
| d8704424-a4a6-3d9b-9594-a975557d0ff0 | -7.5661 | -61.3239 | 2026-08-30 00:10:00 | GOES-19 | MANICORÉ | AMAZONAS | Brasil | 1302702 | 13 | 33 | nan | nan | nan | Amazônia | 73.3 |
| e240dbdc-1489-3a39-8f40-4eac3a10dd61 | -10.7644 | -50.6792 | 2026-08-30 00:10:00 | GOES-19 | LUCIARA | MATO GROSSO | Brasil | 5105309 | 51 | 33 | nan | nan | nan | Cerrado | 80.9 |
| 8be28f69-4246-3ff6-8000-9e0fcc9f12b3 | -3.6398 | -60.5656 | 2026-08-30 00:10:00 | GOES-19 | MANAQUIRI | AMAZONAS | Brasil | 1302553 | 13 | 33 | nan | nan | nan | Amazônia | 68.0 |
| 595c6ec3-0d83-3c26-bb52-292d779f67dc | -5.871 | -57.7715 | 2026-08-30 00:10:00 | GOES-19 | JACAREACANGA | PARÁ | Brasil | 1503754 | 15 | 33 | nan | nan | nan | Amazônia | 93.1 |
| e061c857-9740-3a0a-8159-1afe6470f93d | -10.9593 | -43.0326 | 2026-08-30 00:10:00 | GOES-19 | BARRA | BAHIA | Brasil | 2902708 | 29 | 33 | nan | nan | nan | Cerrado | 114.4 |
| 4f23315d-e1f5-387f-b0f4-d4a5692fcafe | -9.8925 | -60.2945 | 2026-08-30 00:10:00 | GOES-19 | ARIPUANÃ | MATO GROSSO | Brasil | 5101407 | 51 | 33 | nan | nan | nan | Amazônia | 49.8 |
| ac601b5e-bbb8-3e87-a166-3da74fd4a9a3 | -9.8927 | -60.2752 | 2026-08-30 00:10:00 | GOES-19 | ARIPUANÃ | MATO GROSSO | Brasil | 5101407 | 51 | 33 | nan | nan | nan | Amazônia | 141.4 |
| 6c5dab37-d214-3adf-9bd7-0facf1b3f2b3 | -13.856 | -54.1175 | 2026-08-30 00:10:00 | GOES-19 | PARANATINGA | MATO GROSSO | Brasil | 5106307 | 51 | 33 | nan | nan | nan | Cerrado | 348.6 |
| ba1ba731-472e-3b64-b55c-a6e0891a1b91 | -13.8749 | -54.1361 | 2026-08-30 00:10:00 | GOES-19 | PARANATINGA | MATO GROSSO | Brasil | 5106307 | 51 | 33 | nan | nan | nan | Cerrado | 159.0 |
| cb1b3c4d-f22f-3c53-a446-ed93ac8f3bf0 | -9.043 | -65.4175 | 2026-08-30 00:10:00 | GOES-19 | LÁBREA | AMAZONAS | Brasil | 1302405 | 13 | 33 | nan | nan | nan | Amazônia | 74.1 |
| a1c8e497-3b86-3c9a-950a-78863f252d5f | -7.3118 | -60.5897 | 2026-08-30 00:10:00 | GOES-19 | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 53.6 |
| cdd27004-a48a-3cd7-a8a6-27431f60107e | -3.6215 | -60.566 | 2026-08-30 00:10:00 | GOES-19 | MANAQUIRI | AMAZONAS | Brasil | 1302553 | 13 | 33 | nan | nan | nan | Amazônia | 93.5 |
| dbf7f8e5-6ef5-3907-97ac-db73d35da3ed | -3.7532 | -59.3423 | 2026-08-30 00:10:00 | GOES-19 | AUTAZES | AMAZONAS | Brasil | 1300300 | 13 | 33 | nan | nan | nan | Amazônia | 57.5 |
| b026035e-7c26-36f2-ba58-476ab9ebe869 | -10.7871 | -45.3203 | 2026-08-30 00:10:00 | GOES-19 | FORMOSA DO RIO PRETO | BAHIA | Brasil | 2911105 | 29 | 33 | nan | nan | nan | Cerrado | 107.2 |
| 298bed58-c4f0-3abf-87e7-4d0916f2d620 | -10.7867 | -45.3433 | 2026-08-30 00:10:00 | GOES-19 | FORMOSA DO RIO PRETO | BAHIA | Brasil | 2911105 | 29 | 33 | nan | nan | nan | Cerrado | 111.4 |
| a49d327b-cc6c-3c2b-bf16-cada6e09729d | -5.4875 | -57.1611 | 2026-08-30 00:10:00 | GOES-19 | ITAITUBA | PARÁ | Brasil | 1503606 | 15 | 33 | nan | nan | nan | Amazônia | 55.2 |
| 8826ec55-8c86-3a6a-a81d-8f8a105d796f | -6.9546 | -55.7147 | 2026-08-30 00:10:00 | GOES-19 | NOVO PROGRESSO | PARÁ | Brasil | 1505031 | 15 | 33 | nan | nan | nan | Amazônia | 56.6 |
| ab740a93-08e1-3d12-a16b-aa84e133e7d5 | -7.5478 | -61.3056 | 2026-08-30 00:10:00 | GOES-19 | MANICORÉ | AMAZONAS | Brasil | 1302702 | 13 | 33 | nan | nan | nan | Amazônia | 47.0 |
| f5e726a9-b1a4-3425-9223-54483e85287d | -10.7454 | -50.6812 | 2026-08-30 00:10:00 | GOES-19 | LUCIARA | MATO GROSSO | Brasil | 5105309 | 51 | 33 | nan | nan | nan | Cerrado | 82.8 |
| 7ee997cf-791c-3318-a2e1-183c79cc0e3c | -3.7715 | -59.3419 | 2026-08-30 00:10:00 | GOES-19 | AUTAZES | AMAZONAS | Brasil | 1300300 | 13 | 33 | nan | nan | nan | Amazônia | 97.4 |
| a7d8b38a-0530-3bfa-a701-c2c166e1fc0f | -16.1421 | -43.0592 | 2026-08-30 00:10:00 | GOES-19 | RIACHO DOS MACHADOS | MINAS GERAIS | Brasil | 3154507 | 31 | 33 | nan | nan | nan | Cerrado | 76.5 |
| 9d888ee4-9d2c-3fd0-bc00-4c3fb442e00b | -7.5136 | -55.3251 | 2026-08-30 00:10:00 | GOES-19 | NOVO PROGRESSO | PARÁ | Brasil | 1505031 | 15 | 33 | nan | nan | nan | Amazônia | 68.9 |
| d68a2a00-e400-3eb8-86a8-b9bef90068e7 | -10.8066 | -45.2948 | 2026-08-30 00:10:00 | GOES-19 | FORMOSA DO RIO PRETO | BAHIA | Brasil | 2911105 | 29 | 33 | nan | nan | nan | Cerrado | 51.5 |
| 60daf6d3-ed0b-3e8a-8490-ad0f8da56461 | -10.9401 | -43.0355 | 2026-08-30 00:10:00 | GOES-19 | BARRA | BAHIA | Brasil | 2902708 | 29 | 33 | nan | nan | nan | Cerrado | 89.5 |


[Clique aqui para ver as próximas entradas](README2.md)
