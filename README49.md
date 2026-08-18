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

## Dados Diários - Página 49

| ID | Latitude | Longitude | Data/Hora GMT | Satélite | Município | Estado | País | Município ID | Estado ID | País ID | Dias sem Chuva | Precipitação | Risco de Fogo | Bioma | FRP |
|----|----------|-----------|---------------|----------|-----------|--------|------|--------------|-----------|---------|----------------|--------------|----------------|-------|-----|
| 9b4819ff-1a84-3808-ac07-455548ca2b5e | -14.0486 | -53.69015 | 2026-08-18 04:59:00 | NOAA-20 | PARANATINGA | MATO GROSSO | Brasil | 5106307 | 51 | 33 | nan | nan | nan | Cerrado | 1.6 |
| d3be3c6d-ec2b-3d5f-9126-19b6999d5d06 | -17.09915 | -46.56561 | 2026-08-18 04:59:00 | NOAA-20 | PARACATU | MINAS GERAIS | Brasil | 3147006 | 31 | 33 | nan | nan | nan | Cerrado | 0.3 |
| 60da8c77-27f0-3467-aca2-1957ac389455 | -15.26532 | -56.48235 | 2026-08-18 04:59:00 | NOAA-20 | JANGADA | MATO GROSSO | Brasil | 5104906 | 51 | 33 | nan | nan | nan | Cerrado | 0.6 |
| f08c17e6-c368-344a-b18e-74492f389b38 | -13.462 | -57.05779 | 2026-08-18 04:59:00 | NOAA-20 | NOVA MARINGÁ | MATO GROSSO | Brasil | 5108907 | 51 | 33 | nan | nan | nan | Cerrado | 2.2 |
| 7d952ff3-4621-3a0f-8ea4-fbc8715c3aa1 | -17.32988 | -54.9379 | 2026-08-18 04:59:00 | NOAA-20 | ITIQUIRA | MATO GROSSO | Brasil | 5104609 | 51 | 33 | nan | nan | nan | Cerrado | 2.7 |
| afec69a7-7648-38f1-8c10-23bba1a7a66a | -15.25641 | -56.48867 | 2026-08-18 04:59:00 | NOAA-20 | JANGADA | MATO GROSSO | Brasil | 5104906 | 51 | 33 | nan | nan | nan | Cerrado | 0.8 |
| 91440f95-39c0-38ce-885b-fc38647455aa | -15.37735 | -52.77893 | 2026-08-18 04:59:00 | NOAA-20 | BARRA DO GARÇAS | MATO GROSSO | Brasil | 5101803 | 51 | 33 | nan | nan | nan | Cerrado | 0.9 |
| e95f6df6-b8e1-3586-9842-ba63796761aa | -14.81158 | -46.65392 | 2026-08-18 04:59:00 | NOAA-20 | FLORES DE GOIÁS | GOIÁS | Brasil | 5207907 | 52 | 33 | nan | nan | nan | Cerrado | 16.5 |
| c5c9db26-064e-3620-ab32-a7c54c068002 | -15.38021 | -52.78331 | 2026-08-18 04:59:00 | NOAA-20 | BARRA DO GARÇAS | MATO GROSSO | Brasil | 5101803 | 51 | 33 | nan | nan | nan | Cerrado | 0.9 |
| 0a1e7560-1c43-3e7a-8045-6be13f8dffba | -16.17341 | -55.94884 | 2026-08-18 04:59:00 | NOAA-20 | BARÃO DE MELGAÇO | MATO GROSSO | Brasil | 5101605 | 51 | 33 | nan | nan | nan | Pantanal | 2.3 |
| de817356-0420-3d64-a051-512030520bfa | -14.18069 | -52.9429 | 2026-08-18 04:59:00 | NOAA-20 | ÁGUA BOA | MATO GROSSO | Brasil | 5100201 | 51 | 33 | nan | nan | nan | Cerrado | 8.2 |
| 38822335-3bfd-384e-9ca8-ac6fe33e3ddb | -15.27698 | -56.49597 | 2026-08-18 04:59:00 | NOAA-20 | JANGADA | MATO GROSSO | Brasil | 5104906 | 51 | 33 | nan | nan | nan | Cerrado | 2.4 |
| c36d6832-348d-396e-8b56-e61940b4f0f9 | -14.35338 | -51.94041 | 2026-08-18 04:59:00 | NOAA-20 | NOVA NAZARÉ | MATO GROSSO | Brasil | 5106174 | 51 | 33 | nan | nan | nan | Cerrado | 0.8 |
| 32adf53d-e276-3145-b3b9-6df39fad82c4 | -16.69134 | -49.33475 | 2026-08-18 04:59:00 | NOAA-20 | GOIÂNIA | GOIÁS | Brasil | 5208707 | 52 | 33 | nan | nan | nan | Cerrado | 2.0 |
| f18bd470-675b-397b-8fc0-99e406f70add | -20.2992 | -46.48035 | 2026-08-18 04:59:00 | NOAA-20 | SÃO ROQUE DE MINAS | MINAS GERAIS | Brasil | 3164308 | 31 | 33 | nan | nan | nan | Cerrado | 5.7 |
| d51bc5bb-e55b-3ff3-9405-5be16458805c | -16.29913 | -53.18658 | 2026-08-18 04:59:00 | NOAA-20 | GUIRATINGA | MATO GROSSO | Brasil | 5104203 | 51 | 33 | nan | nan | nan | Cerrado | 0.8 |
| 4866e776-8064-3499-9c23-7bcf37f1a0f2 | -14.1756 | -52.93068 | 2026-08-18 04:59:00 | NOAA-20 | ÁGUA BOA | MATO GROSSO | Brasil | 5100201 | 51 | 33 | nan | nan | nan | Cerrado | 13.0 |
| b10f9b37-31d4-3afe-85c2-825851014f96 | -15.89246 | -55.56314 | 2026-08-18 04:59:00 | NOAA-20 | SANTO ANTÔNIO DO LEVERGER | MATO GROSSO | Brasil | 5107800 | 51 | 33 | nan | nan | nan | Cerrado | 2.1 |
| b18ffe1b-df56-381f-b2e0-b460608ea7d3 | -15.38879 | -52.79658 | 2026-08-18 04:59:00 | NOAA-20 | BARRA DO GARÇAS | MATO GROSSO | Brasil | 5101803 | 51 | 33 | nan | nan | nan | Cerrado | 1.6 |
| 8f02491e-3880-3a30-93c8-4f697ddceaef | -15.91799 | -55.55283 | 2026-08-18 04:59:00 | NOAA-20 | SANTO ANTÔNIO DO LEVERGER | MATO GROSSO | Brasil | 5107800 | 51 | 33 | nan | nan | nan | Cerrado | 2.0 |
| ea612bce-4841-3c4e-8be4-c98fcae1ba43 | -13.41706 | -57.04236 | 2026-08-18 04:59:00 | NOAA-20 | NOVA MARINGÁ | MATO GROSSO | Brasil | 5108907 | 51 | 33 | nan | nan | nan | Cerrado | 1.0 |
| 784d0460-5d3f-3ae4-9b97-847b949e27bb | -14.35926 | -51.92469 | 2026-08-18 04:59:00 | NOAA-20 | NOVA NAZARÉ | MATO GROSSO | Brasil | 5106174 | 51 | 33 | nan | nan | nan | Cerrado | 1.2 |
| 15d1f723-ab96-3802-90e6-963d196182e5 | -14.51543 | -53.09343 | 2026-08-18 04:59:00 | NOAA-20 | CAMPINÁPOLIS | MATO GROSSO | Brasil | 5102603 | 51 | 33 | nan | nan | nan | Cerrado | 0.8 |
| cd446811-e6ce-35a4-82b0-59048fbb011d | -14.30233 | -47.17985 | 2026-08-18 04:59:00 | NOAA-20 | FLORES DE GOIÁS | GOIÁS | Brasil | 5207907 | 52 | 33 | nan | nan | nan | Cerrado | 2.1 |
| 25686220-95d3-3ff5-bbf8-b7c7e65ce603 | -13.41422 | -57.03775 | 2026-08-18 04:59:00 | NOAA-20 | NOVA MARINGÁ | MATO GROSSO | Brasil | 5108907 | 51 | 33 | nan | nan | nan | Cerrado | 1.0 |
| 5ebc7713-8735-3264-84e0-0dbd9d06a48a | -15.64169 | -54.81203 | 2026-08-18 04:59:00 | NOAA-20 | DOM AQUINO | MATO GROSSO | Brasil | 5103601 | 51 | 33 | nan | nan | nan | Cerrado | 0.9 |
| 8fafc456-433c-3795-a4b1-838b574afd29 | -15.26959 | -56.49851 | 2026-08-18 04:59:00 | NOAA-20 | JANGADA | MATO GROSSO | Brasil | 5104906 | 51 | 33 | nan | nan | nan | Cerrado | 9.7 |
| b3223de7-ba1b-3d0e-9735-e577279416df | -15.38937 | -52.79271 | 2026-08-18 04:59:00 | NOAA-20 | BARRA DO GARÇAS | MATO GROSSO | Brasil | 5101803 | 51 | 33 | nan | nan | nan | Cerrado | 3.7 |
| 80fb9306-688c-39c6-8740-ebcb27005eaf | -15.30325 | -56.44274 | 2026-08-18 04:59:00 | NOAA-20 | JANGADA | MATO GROSSO | Brasil | 5104906 | 51 | 33 | nan | nan | nan | Cerrado | 1.8 |
| a28a4b90-7160-3e31-84bb-b002764f6a19 | -17.32881 | -54.92294 | 2026-08-18 04:59:00 | NOAA-20 | ITIQUIRA | MATO GROSSO | Brasil | 5104609 | 51 | 33 | nan | nan | nan | Cerrado | 1.3 |
| f2edd74e-2c11-3a46-805a-6ac1fbf7c27a | -14.83674 | -46.65241 | 2026-08-18 04:59:00 | NOAA-20 | FLORES DE GOIÁS | GOIÁS | Brasil | 5207907 | 52 | 33 | nan | nan | nan | Cerrado | 1.7 |
| 6a36f0a0-037d-3d1a-8570-b57cc34af0aa | -14.03193 | -53.68742 | 2026-08-18 04:59:00 | NOAA-20 | PARANATINGA | MATO GROSSO | Brasil | 5106307 | 51 | 33 | nan | nan | nan | Cerrado | 2.4 |
| 13658db9-f182-32bc-b378-4f3d547aace2 | -14.17846 | -52.91191 | 2026-08-18 04:59:00 | NOAA-20 | ÁGUA BOA | MATO GROSSO | Brasil | 5100201 | 51 | 33 | nan | nan | nan | Cerrado | 12.9 |
| d9ec9f05-67ae-367c-b68c-a32848d25485 | -14.17619 | -52.90394 | 2026-08-18 04:59:00 | NOAA-20 | ÁGUA BOA | MATO GROSSO | Brasil | 5100201 | 51 | 33 | nan | nan | nan | Cerrado | 39.9 |
| 5670c911-bd47-3d13-849c-99ff0f5825a4 | -13.93379 | -53.92475 | 2026-08-18 04:59:00 | NOAA-20 | PARANATINGA | MATO GROSSO | Brasil | 5106307 | 51 | 33 | nan | nan | nan | Cerrado | 1.3 |
| 75057713-c226-3f97-a5a0-007544db2bc3 | -17.45796 | -47.86706 | 2026-08-18 04:59:00 | NOAA-20 | CAMPO ALEGRE DE GOIÁS | GOIÁS | Brasil | 5204805 | 52 | 33 | nan | nan | nan | Cerrado | 3.7 |
| 7cfeca1c-0f5d-32d7-bc52-1dda0bd82be0 | -14.17449 | -52.91513 | 2026-08-18 04:59:00 | NOAA-20 | ÁGUA BOA | MATO GROSSO | Brasil | 5100201 | 51 | 33 | nan | nan | nan | Cerrado | 1.6 |
| 9f5f80dd-c677-39c9-97e2-0898643fa60e | -16.26981 | -49.3019 | 2026-08-18 04:59:00 | NOAA-20 | DAMOLÂNDIA | GOIÁS | Brasil | 5206800 | 52 | 33 | nan | nan | nan | Cerrado | 5.1 |
| 9607d76b-d959-3d33-a03a-52f1028b58a3 | -15.24317 | -56.46323 | 2026-08-18 04:59:00 | NOAA-20 | JANGADA | MATO GROSSO | Brasil | 5104906 | 51 | 33 | nan | nan | nan | Cerrado | 0.5 |
| aedde429-e8c3-3475-b988-cd3967946840 | -13.01837 | -56.58673 | 2026-08-18 04:59:00 | NOAA-20 | LUCAS DO RIO VERDE | MATO GROSSO | Brasil | 5105259 | 51 | 33 | nan | nan | nan | Amazônia | 1.7 |
| 59cd13ea-8694-36eb-baf5-9680768d8dec | -14.25508 | -51.92218 | 2026-08-18 04:59:00 | NOAA-20 | NOVA NAZARÉ | MATO GROSSO | Brasil | 5106174 | 51 | 33 | nan | nan | nan | Cerrado | 3.2 |
| 6041924f-80f8-3b99-a0e7-344c4b6241ca | -14.17675 | -52.92316 | 2026-08-18 04:59:00 | NOAA-20 | ÁGUA BOA | MATO GROSSO | Brasil | 5100201 | 51 | 33 | nan | nan | nan | Cerrado | 7.2 |
| 7493628a-e1d0-3ae4-b123-78fead76ad23 | -14.44777 | -53.07519 | 2026-08-18 04:59:00 | NOAA-20 | CAMPINÁPOLIS | MATO GROSSO | Brasil | 5102603 | 51 | 33 | nan | nan | nan | Cerrado | 2.4 |
| c24b4b58-9f1c-3e37-90e2-aebb63ccfe57 | -15.82934 | -54.19886 | 2026-08-18 04:59:00 | NOAA-20 | POXORÉU | MATO GROSSO | Brasil | 5107008 | 51 | 33 | nan | nan | nan | Cerrado | 1.1 |
| 915f4400-e8e9-303a-85f6-70b5c3ee508d | -14.18919 | -52.93279 | 2026-08-18 04:59:00 | NOAA-20 | ÁGUA BOA | MATO GROSSO | Brasil | 5100201 | 51 | 33 | nan | nan | nan | Cerrado | 10.6 |
| 13143c5f-a669-3b0a-8613-16183cf304cd | -14.81079 | -48.78191 | 2026-08-18 04:59:00 | NOAA-20 | BARRO ALTO | GOIÁS | Brasil | 5203203 | 52 | 33 | nan | nan | nan | Cerrado | 0.9 |
| 444341bf-e2c6-31e3-9102-66371b1340dc | -17.3476 | -54.93348 | 2026-08-18 04:59:00 | NOAA-20 | ITIQUIRA | MATO GROSSO | Brasil | 5104609 | 51 | 33 | nan | nan | nan | Cerrado | 1.3 |
| d46545ee-64ac-38a8-963e-034a03a91c0c | -15.17267 | -52.86185 | 2026-08-18 04:59:00 | NOAA-20 | BARRA DO GARÇAS | MATO GROSSO | Brasil | 5101803 | 51 | 33 | nan | nan | nan | Cerrado | 0.7 |
| 769c7172-c1ef-3efe-ada0-e7d8d2c08e3f | -16.2305 | -57.65771 | 2026-08-18 04:59:00 | NOAA-20 | CÁCERES | MATO GROSSO | Brasil | 5102504 | 51 | 33 | nan | nan | nan | Pantanal | 1.6 |
| cf4e1b8e-189c-3e34-9126-2830b1218c2c | -13.39916 | -54.34679 | 2026-08-18 04:59:00 | NOAA-20 | PARANATINGA | MATO GROSSO | Brasil | 5106307 | 51 | 33 | nan | nan | nan | Amazônia | 1.1 |
| d919aecb-3028-3988-ad20-bcad55838394 | -12.9438 | -56.63861 | 2026-08-18 04:59:00 | NOAA-20 | NOVA MUTUM | MATO GROSSO | Brasil | 5106224 | 51 | 33 | nan | nan | nan | Amazônia | 1.4 |
| 60992a7b-bb9c-3bbc-8afc-734ac6263bb4 | -14.85515 | -46.63943 | 2026-08-18 04:59:00 | NOAA-20 | FLORES DE GOIÁS | GOIÁS | Brasil | 5207907 | 52 | 33 | nan | nan | nan | Cerrado | 1.9 |
| 1fce7de4-9270-39ec-b98c-bc7255689f81 | -14.17278 | -52.92637 | 2026-08-18 04:59:00 | NOAA-20 | ÁGUA BOA | MATO GROSSO | Brasil | 5100201 | 51 | 33 | nan | nan | nan | Cerrado | 12.1 |
| 9032fa02-92a7-3be1-b5f3-213ac870d259 | -15.21051 | -52.69841 | 2026-08-18 04:59:00 | NOAA-20 | BARRA DO GARÇAS | MATO GROSSO | Brasil | 5101803 | 51 | 33 | nan | nan | nan | Cerrado | 1.5 |
| aa66a870-bbd5-332a-94b4-4b5499b3cc09 | -16.24798 | -57.66089 | 2026-08-18 04:59:00 | NOAA-20 | CÁCERES | MATO GROSSO | Brasil | 5102504 | 51 | 33 | nan | nan | nan | Pantanal | 5.2 |
| 704c1cb3-1672-3234-b68d-a3cb779496b4 | -15.27084 | -56.49103 | 2026-08-18 04:59:00 | NOAA-20 | JANGADA | MATO GROSSO | Brasil | 5104906 | 51 | 33 | nan | nan | nan | Cerrado | 1.2 |
| 89c36979-7983-35d0-be70-566c3d2e9c93 | -14.16599 | -52.90241 | 2026-08-18 04:59:00 | NOAA-20 | ÁGUA BOA | MATO GROSSO | Brasil | 5100201 | 51 | 33 | nan | nan | nan | Cerrado | 2.4 |
| 5389e327-e07d-38cc-92a3-80666f9e9906 | -17.32493 | -54.92598 | 2026-08-18 04:59:00 | NOAA-20 | ITIQUIRA | MATO GROSSO | Brasil | 5104609 | 51 | 33 | nan | nan | nan | Cerrado | 1.6 |
| d5bc0002-9849-39da-b0e3-28278c55679a | -14.16202 | -52.90562 | 2026-08-18 04:59:00 | NOAA-20 | ÁGUA BOA | MATO GROSSO | Brasil | 5100201 | 51 | 33 | nan | nan | nan | Cerrado | 3.4 |
| 7e40f4cc-f8d6-3af6-aa13-a7246e2149a6 | -14.18354 | -52.92424 | 2026-08-18 04:59:00 | NOAA-20 | ÁGUA BOA | MATO GROSSO | Brasil | 5100201 | 51 | 33 | nan | nan | nan | Cerrado | 8.2 |
| 3cc9516d-49b4-3661-a158-6312a922a305 | -15.2404 | -56.50126 | 2026-08-18 04:59:00 | NOAA-20 | JANGADA | MATO GROSSO | Brasil | 5104906 | 51 | 33 | nan | nan | nan | Cerrado | 0.7 |
| 0a96793f-98a9-3d30-b630-c7a530733329 | -14.25743 | -51.93082 | 2026-08-18 04:59:00 | NOAA-20 | NOVA NAZARÉ | MATO GROSSO | Brasil | 5106174 | 51 | 33 | nan | nan | nan | Cerrado | 8.8 |
| 6f34a057-1056-3c08-a101-a51e61d688f1 | -14.03304 | -53.68025 | 2026-08-18 04:59:00 | NOAA-20 | PARANATINGA | MATO GROSSO | Brasil | 5106307 | 51 | 33 | nan | nan | nan | Cerrado | 5.3 |
| e9e7b708-861e-3d8b-8385-533f97f58e3f | -14.8478 | -46.64398 | 2026-08-18 04:59:00 | NOAA-20 | FLORES DE GOIÁS | GOIÁS | Brasil | 5207907 | 52 | 33 | nan | nan | nan | Cerrado | 1.4 |
| 76ef76f1-2f58-375b-9bf4-26984d57bcc4 | -14.17392 | -52.89603 | 2026-08-18 04:59:00 | NOAA-20 | ÁGUA BOA | MATO GROSSO | Brasil | 5100201 | 51 | 33 | nan | nan | nan | Cerrado | 3.0 |
| 6d113c81-654d-30b6-848a-1105167acea4 | -20.29774 | -46.47732 | 2026-08-18 04:59:00 | NOAA-20 | SÃO ROQUE DE MINAS | MINAS GERAIS | Brasil | 3164308 | 31 | 33 | nan | nan | nan | Cerrado | 7.0 |
| 8d20809f-1436-32f9-94d6-697e997f14db | -13.40746 | -54.33727 | 2026-08-18 04:59:00 | NOAA-20 | PARANATINGA | MATO GROSSO | Brasil | 5106307 | 51 | 33 | nan | nan | nan | Amazônia | 1.4 |
| 5100b574-de8a-3149-9b60-9f62c92679d3 | -15.22256 | -57.65165 | 2026-08-18 04:59:00 | NOAA-20 | LAMBARI D'OESTE | MATO GROSSO | Brasil | 5105234 | 51 | 33 | nan | nan | nan | Amazônia | 1.9 |
| 80acdcdf-32c7-39e7-a246-425a88edc168 | -13.57783 | -51.76366 | 2026-08-18 04:59:00 | NOAA-20 | CANARANA | MATO GROSSO | Brasil | 5102702 | 51 | 33 | nan | nan | nan | Cerrado | 1.9 |
| ce029440-bb25-343d-810a-8a3cd54bb798 | -14.12781 | -53.65837 | 2026-08-18 04:59:00 | NOAA-20 | PARANATINGA | MATO GROSSO | Brasil | 5106307 | 51 | 33 | nan | nan | nan | Cerrado | 0.7 |
| d54dded4-6a51-3f02-867f-614076054a7a | -13.00541 | -56.60044 | 2026-08-18 04:59:00 | NOAA-20 | LUCAS DO RIO VERDE | MATO GROSSO | Brasil | 5105259 | 51 | 33 | nan | nan | nan | Amazônia | 1.3 |
| abe10962-83f0-3e35-a846-6dfd0fe33cea | -16.30255 | -53.18713 | 2026-08-18 04:59:00 | NOAA-20 | GUIRATINGA | MATO GROSSO | Brasil | 5104203 | 51 | 33 | nan | nan | nan | Cerrado | 0.8 |
| 40a16e27-c93a-3348-9a8a-3d34327f7965 | -15.30201 | -56.45023 | 2026-08-18 04:59:00 | NOAA-20 | JANGADA | MATO GROSSO | Brasil | 5104906 | 51 | 33 | nan | nan | nan | Cerrado | 1.3 |
| c2b8cddf-da0b-3326-a036-06d2324b16f9 | -15.29186 | -56.44843 | 2026-08-18 04:59:00 | NOAA-20 | JANGADA | MATO GROSSO | Brasil | 5104906 | 51 | 33 | nan | nan | nan | Cerrado | 1.9 |
| 13647a0e-e69d-3ead-a445-6e383fc72e4a | -15.8932 | -55.53738 | 2026-08-18 04:59:00 | NOAA-20 | SANTO ANTÔNIO DO LEVERGER | MATO GROSSO | Brasil | 5107800 | 51 | 33 | nan | nan | nan | Cerrado | 1.9 |
| e38ef3e1-b929-3400-a127-e59f27aa24e0 | -15.22679 | -57.6482 | 2026-08-18 04:59:00 | NOAA-20 | LAMBARI D'OESTE | MATO GROSSO | Brasil | 5105234 | 51 | 33 | nan | nan | nan | Amazônia | 4.6 |
| 71215dd4-c9c6-30e6-9116-1c7582f91cd0 | -14.3634 | -51.87107 | 2026-08-18 04:59:00 | NOAA-20 | NOVA NAZARÉ | MATO GROSSO | Brasil | 5106174 | 51 | 33 | nan | nan | nan | Cerrado | 1.9 |
| dc0aeceb-6838-3593-9bb0-7a20e513aadd | -15.26469 | -56.4861 | 2026-08-18 04:59:00 | NOAA-20 | JANGADA | MATO GROSSO | Brasil | 5104906 | 51 | 33 | nan | nan | nan | Cerrado | 1.3 |
| e2a2b656-b0c8-3331-a9bd-7854642b5f57 | -13.79062 | -53.84293 | 2026-08-18 04:59:00 | NOAA-20 | PARANATINGA | MATO GROSSO | Brasil | 5106307 | 51 | 33 | nan | nan | nan | Cerrado | 2.2 |
| 0d1a253d-8390-371a-8a3d-4f715a313d2a | -17.98312 | -44.43532 | 2026-08-18 04:59:00 | NOAA-20 | LASSANCE | MINAS GERAIS | Brasil | 3138104 | 31 | 33 | nan | nan | nan | Cerrado | 1.7 |
| 725b0553-2849-3281-999c-ef0d5f87ef29 | -13.39804 | -54.35386 | 2026-08-18 04:59:00 | NOAA-20 | PARANATINGA | MATO GROSSO | Brasil | 5106307 | 51 | 33 | nan | nan | nan | Amazônia | 1.3 |
| 818c6fea-52d8-3f0c-a7c9-0c50e118c059 | -13.41355 | -57.04177 | 2026-08-18 04:59:00 | NOAA-20 | NOVA MARINGÁ | MATO GROSSO | Brasil | 5108907 | 51 | 33 | nan | nan | nan | Cerrado | 1.0 |
| 661fb054-ce6d-3a4b-83fc-076e1259e1ac | -13.42062 | -54.38297 | 2026-08-18 04:59:00 | NOAA-20 | PARANATINGA | MATO GROSSO | Brasil | 5106307 | 51 | 33 | nan | nan | nan | Amazônia | 1.6 |
| 81558a31-206a-3850-8fbe-a2ba6bf9db23 | -14.84106 | -46.63176 | 2026-08-18 04:59:00 | NOAA-20 | FLORES DE GOIÁS | GOIÁS | Brasil | 5207907 | 52 | 33 | nan | nan | nan | Cerrado | 1.9 |
| 061e8c0c-c491-3df4-aa82-0cadc5b40af4 | -14.42648 | -51.88497 | 2026-08-18 04:59:00 | NOAA-20 | NOVA NAZARÉ | MATO GROSSO | Brasil | 5106174 | 51 | 33 | nan | nan | nan | Cerrado | 0.9 |
| 2828143a-9eb3-3fce-ba77-a2b0dbbb9f0c | -17.97768 | -44.42984 | 2026-08-18 04:59:00 | NOAA-20 | LASSANCE | MINAS GERAIS | Brasil | 3138104 | 31 | 33 | nan | nan | nan | Cerrado | 1.7 |
| 07988ff6-dded-3f75-be93-2f0f23d2d825 | -14.81297 | -46.64279 | 2026-08-18 04:59:00 | NOAA-20 | FLORES DE GOIÁS | GOIÁS | Brasil | 5207907 | 52 | 33 | nan | nan | nan | Cerrado | 8.5 |
| 9d4ff3fe-ef37-3682-984d-6b9254172bbc | -15.787 | -55.56342 | 2026-08-18 04:59:00 | NOAA-20 | SANTO ANTÔNIO DO LEVERGER | MATO GROSSO | Brasil | 5107800 | 51 | 33 | nan | nan | nan | Cerrado | 1.7 |
| 891c236e-12fe-3c4d-9c47-7d2dc0ca7c68 | -13.41189 | -54.33075 | 2026-08-18 04:59:00 | NOAA-20 | PARANATINGA | MATO GROSSO | Brasil | 5106307 | 51 | 33 | nan | nan | nan | Amazônia | 0.9 |
| 9d06d238-f925-3e9b-ba01-0fd81b7bc4a8 | -14.48162 | -53.10342 | 2026-08-18 04:59:00 | NOAA-20 | CAMPINÁPOLIS | MATO GROSSO | Brasil | 5102603 | 51 | 33 | nan | nan | nan | Cerrado | 2.0 |
| 0398f9f0-977f-3a57-8a34-bab9bcae2f00 | -15.25241 | -56.49182 | 2026-08-18 04:59:00 | NOAA-20 | JANGADA | MATO GROSSO | Brasil | 5104906 | 51 | 33 | nan | nan | nan | Cerrado | 3.9 |
| a93ee029-9b18-30b0-830a-4cdfe1485aed | -14.18862 | -52.9365 | 2026-08-18 04:59:00 | NOAA-20 | ÁGUA BOA | MATO GROSSO | Brasil | 5100201 | 51 | 33 | nan | nan | nan | Cerrado | 10.6 |
| 3ecceb77-010a-3aa2-8e84-7aebd73e1403 | -13.41773 | -57.03834 | 2026-08-18 04:59:00 | NOAA-20 | NOVA MARINGÁ | MATO GROSSO | Brasil | 5108907 | 51 | 33 | nan | nan | nan | Cerrado | 1.0 |
| a07daf80-643c-3f19-8b93-35082fa63aa1 | -16.05691 | -56.53354 | 2026-08-18 04:59:00 | NOAA-20 | POCONÉ | MATO GROSSO | Brasil | 5106505 | 51 | 33 | nan | nan | nan | Cerrado | 0.7 |
| 9f4dd4f8-cd76-3c07-bcc3-8dfcfc95d86c | -14.03527 | -53.68797 | 2026-08-18 04:59:00 | NOAA-20 | PARANATINGA | MATO GROSSO | Brasil | 5106307 | 51 | 33 | nan | nan | nan | Cerrado | 2.4 |
| 8624a5f8-f7ef-375b-a86a-f34e5dc8d539 | -15.01928 | -52.69308 | 2026-08-18 04:59:00 | NOAA-20 | BARRA DO GARÇAS | MATO GROSSO | Brasil | 5101803 | 51 | 33 | nan | nan | nan | Cerrado | 1.7 |
| 65fb9d4d-3d07-3578-b397-787d50359ccf | -13.56253 | -51.76964 | 2026-08-18 04:59:00 | NOAA-20 | CANARANA | MATO GROSSO | Brasil | 5102702 | 51 | 33 | nan | nan | nan | Cerrado | 1.1 |
| 1d215684-907d-32a4-801e-cab13b982234 | -13.78674 | -53.84596 | 2026-08-18 04:59:00 | NOAA-20 | PARANATINGA | MATO GROSSO | Brasil | 5106307 | 51 | 33 | nan | nan | nan | Cerrado | 0.8 |
| a905e165-f2d0-387c-a597-e7dcfcfe48e2 | -15.78309 | -55.56648 | 2026-08-18 04:59:00 | NOAA-20 | SANTO ANTÔNIO DO LEVERGER | MATO GROSSO | Brasil | 5107800 | 51 | 33 | nan | nan | nan | Cerrado | 1.6 |
| 9bfab489-591b-32cf-b97c-991dbef5973f | -15.29925 | -56.44586 | 2026-08-18 04:59:00 | NOAA-20 | JANGADA | MATO GROSSO | Brasil | 5104906 | 51 | 33 | nan | nan | nan | Cerrado | 2.7 |


[Clique aqui para ver as próximas entradas](README50.md)
