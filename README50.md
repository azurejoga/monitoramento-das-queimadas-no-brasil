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

## Dados Diários - Página 50

| ID | Latitude | Longitude | Data/Hora GMT | Satélite | Município | Estado | País | Município ID | Estado ID | País ID | Dias sem Chuva | Precipitação | Risco de Fogo | Bioma | FRP |
|----|----------|-----------|---------------|----------|-----------|--------|------|--------------|-----------|---------|----------------|--------------|----------------|-------|-----|
| 27f00a04-08b2-3b69-a9ad-4f16e7a08d2a | -8.4921 | -48.6259 | 2024-10-09 02:05:54 | GOES-16 | PRESIDENTE KENNEDY | TOCANTINS | Brasil | 1718402 | 17 | 33 | nan | nan | nan | Amazônia | 65.8 |
| b4fd8159-b798-3832-9e95-64eb59f88533 | -8.5107 | -48.6459 | 2024-10-09 02:05:54 | GOES-16 | PRESIDENTE KENNEDY | TOCANTINS | Brasil | 1718402 | 17 | 33 | nan | nan | nan | Amazônia | 73.5 |
| 805599aa-a31c-39eb-a305-2596bc653271 | -10.3894 | -61.2502 | 2024-10-09 02:06:06 | GOES-16 | RONDOLÂNDIA | MATO GROSSO | Brasil | 5107578 | 51 | 33 | nan | nan | nan | Amazônia | 58.5 |
| 139008be-eae5-3da7-90ce-1cfe9516b574 | -10.4287 | -60.9979 | 2024-10-09 02:06:06 | GOES-16 | RONDOLÂNDIA | MATO GROSSO | Brasil | 5107578 | 51 | 33 | nan | nan | nan | Amazônia | 56.3 |
| b4eb7eca-e2a7-3722-a5ad-2a699ee9699a | -10.6068 | -55.9169 | 2024-10-09 02:06:07 | GOES-16 | NOVA CANAÃ DO NORTE | MATO GROSSO | Brasil | 5106216 | 51 | 33 | nan | nan | nan | Amazônia | 29.8 |
| a3daa603-6d58-33d2-801c-552090685021 | -10.6253 | -55.9355 | 2024-10-09 02:06:07 | GOES-16 | NOVA CANAÃ DO NORTE | MATO GROSSO | Brasil | 5106216 | 51 | 33 | nan | nan | nan | Amazônia | 61.8 |
| 78a811f4-69d6-3269-93f6-0f053e7856bd | -10.6256 | -55.9154 | 2024-10-09 02:06:07 | GOES-16 | NOVA CANAÃ DO NORTE | MATO GROSSO | Brasil | 5106216 | 51 | 33 | nan | nan | nan | Amazônia | 131.7 |
| 8d08b67b-f277-358c-89df-d408a0404284 | -10.6258 | -55.8953 | 2024-10-09 02:06:07 | GOES-16 | NOVA CANAÃ DO NORTE | MATO GROSSO | Brasil | 5106216 | 51 | 33 | nan | nan | nan | Amazônia | 63.3 |
| 67a33ff3-ff76-3792-9163-3bc93c0f934a | -10.6444 | -55.914 | 2024-10-09 02:06:07 | GOES-16 | NOVA CANAÃ DO NORTE | MATO GROSSO | Brasil | 5106216 | 51 | 33 | nan | nan | nan | Amazônia | 22.5 |
| 29e46286-5357-3499-bb90-3673b9024be5 | -10.6446 | -55.8938 | 2024-10-09 02:06:07 | GOES-16 | NOVA CANAÃ DO NORTE | MATO GROSSO | Brasil | 5106216 | 51 | 33 | nan | nan | nan | Amazônia | 33.2 |
| 9a1d9dfc-bb3b-39dc-8d48-afee3720a5e5 | -10.8754 | -63.9169 | 2024-10-09 02:06:08 | GOES-16 | GUAJARÁ-MIRIM | RONDÔNIA | Brasil | 1100106 | 11 | 33 | nan | nan | nan | Amazônia | 102.9 |
| 043011b8-2f83-38b4-ba0a-d40ba82cfcdb | -10.8755 | -63.8979 | 2024-10-09 02:06:08 | GOES-16 | GUAJARÁ-MIRIM | RONDÔNIA | Brasil | 1100106 | 11 | 33 | nan | nan | nan | Amazônia | 80.4 |
| 81bd3f6f-48a9-3108-b7c3-029a35fc0a8f | -10.8941 | -63.916 | 2024-10-09 02:06:09 | GOES-16 | GUAJARÁ-MIRIM | RONDÔNIA | Brasil | 1100106 | 11 | 33 | nan | nan | nan | Amazônia | 70.5 |
| d6ce2ca4-5b93-3fe5-96d7-12bd641f47e8 | -10.9112 | -64.1615 | 2024-10-09 02:06:09 | GOES-16 | GUAJARÁ-MIRIM | RONDÔNIA | Brasil | 1100106 | 11 | 33 | nan | nan | nan | Amazônia | 66.0 |
| 85a5683d-8fef-3966-b937-aa57b94cc00b | -11.5233 | -65.137 | 2024-10-09 02:06:12 | GOES-16 | GUAJARÁ-MIRIM | RONDÔNIA | Brasil | 1100106 | 11 | 33 | nan | nan | nan | Amazônia | 59.1 |
| f0c833d0-d9a3-3c09-abc2-1f6dc61ade19 | -11.7119 | -64.9966 | 2024-10-09 02:06:13 | GOES-16 | GUAJARÁ-MIRIM | RONDÔNIA | Brasil | 1100106 | 11 | 33 | nan | nan | nan | Amazônia | 97.0 |
| 3a28019f-b825-37c0-9625-de29ab097ecb | -11.7117 | -65.0155 | 2024-10-09 02:06:13 | GOES-16 | GUAJARÁ-MIRIM | RONDÔNIA | Brasil | 1100106 | 11 | 33 | nan | nan | nan | Amazônia | 88.6 |
| c54367f6-2c55-36fb-b114-3aaf975fc606 | -11.6931 | -64.9974 | 2024-10-09 02:06:13 | GOES-16 | GUAJARÁ-MIRIM | RONDÔNIA | Brasil | 1100106 | 11 | 33 | nan | nan | nan | Amazônia | 60.5 |
| c55b9abc-4a73-39c1-94cd-13f4b85c2b3f | -11.6806 | -64.0312 | 2024-10-09 02:06:13 | GOES-16 | GUAJARÁ-MIRIM | RONDÔNIA | Brasil | 1100106 | 11 | 33 | nan | nan | nan | Amazônia | 69.3 |
| 260ebd73-a2f4-3bac-89aa-63b94a0470a9 | -11.693 | -65.0163 | 2024-10-09 02:06:13 | GOES-16 | GUAJARÁ-MIRIM | RONDÔNIA | Brasil | 1100106 | 11 | 33 | nan | nan | nan | Amazônia | 63.0 |
| 2aaeed70-76de-395c-b91f-4e8bcd84bb45 | -12.2086 | -50.5815 | 2024-10-09 02:06:15 | GOES-16 | FORMOSO DO ARAGUAIA | TOCANTINS | Brasil | 1708205 | 17 | 33 | nan | nan | nan | Cerrado | 82.6 |
| 95a1f22b-ca44-3423-b473-6313870e6393 | -12.1895 | -50.5838 | 2024-10-09 02:06:15 | GOES-16 | FORMOSO DO ARAGUAIA | TOCANTINS | Brasil | 1708205 | 17 | 33 | nan | nan | nan | Cerrado | 79.7 |
| 6fcf8374-5d15-36e9-a299-c2ef08fc7f0b | -12.6676 | -63.0819 | 2024-10-09 02:06:18 | GOES-16 | SÃO FRANCISCO DO GUAPORÉ | RONDÔNIA | Brasil | 1101492 | 11 | 33 | nan | nan | nan | Amazônia | 66.1 |
| 7beada95-2307-3761-bf40-8fe61b67ab28 | -12.7502 | -62.2497 | 2024-10-09 02:06:19 | GOES-16 | ALTA FLORESTA D'OESTE | RONDÔNIA | Brasil | 1100015 | 11 | 33 | nan | nan | nan | Amazônia | 36.0 |
| d4335b18-8d10-3468-946d-7a3f544dd9c0 | -12.7501 | -62.269 | 2024-10-09 02:06:19 | GOES-16 | ALTA FLORESTA D'OESTE | RONDÔNIA | Brasil | 1100015 | 11 | 33 | nan | nan | nan | Amazônia | 47.6 |
| 78a8eba6-5eed-3ffd-aa23-84d4164a6a1f | -12.9756 | -62.4673 | 2024-10-09 02:06:20 | GOES-16 | ALTA FLORESTA D'OESTE | RONDÔNIA | Brasil | 1100015 | 11 | 33 | nan | nan | nan | Amazônia | 71.6 |
| 6f5cd3f0-fec1-315e-af2e-9afc85af3435 | -12.878 | -62.8007 | 2024-10-09 02:06:20 | GOES-16 | ALTA FLORESTA D'OESTE | RONDÔNIA | Brasil | 1100015 | 11 | 33 | nan | nan | nan | Amazônia | 137.1 |
| 5f89561a-2a1e-35ae-8b53-3a4c9be51370 | -12.8779 | -62.82 | 2024-10-09 02:06:20 | GOES-16 | ALTA FLORESTA D'OESTE | RONDÔNIA | Brasil | 1100015 | 11 | 33 | nan | nan | nan | Amazônia | 59.1 |
| 39805533-055c-3b03-9392-bc8ff1dc0f79 | -12.8591 | -62.8018 | 2024-10-09 02:06:20 | GOES-16 | SÃO FRANCISCO DO GUAPORÉ | RONDÔNIA | Brasil | 1101492 | 11 | 33 | nan | nan | nan | Amazônia | 72.8 |
| afc0d3eb-f47c-3fc6-b156-f4342631ea39 | -13.379 | -61.9194 | 2024-10-09 02:06:22 | GOES-16 | PIMENTEIRAS DO OESTE | RONDÔNIA | Brasil | 1101468 | 11 | 33 | nan | nan | nan | Amazônia | 40.0 |
| f8ae40f6-eff8-3ac8-97ab-247a6929d13a | -13.3788 | -61.9388 | 2024-10-09 02:06:22 | GOES-16 | PIMENTEIRAS DO OESTE | RONDÔNIA | Brasil | 1101468 | 11 | 33 | nan | nan | nan | Amazônia | 30.3 |
| f53b70e2-72db-399e-b20b-0150d7949945 | -13.8364 | -44.5927 | 2024-10-09 02:06:23 | GOES-16 | CORIBE | BAHIA | Brasil | 2909109 | 29 | 33 | nan | nan | nan | Cerrado | 83.1 |
| 25e33ff4-4012-3f04-b8d3-0984505c7006 | -13.8369 | -44.5691 | 2024-10-09 02:06:23 | GOES-16 | CORIBE | BAHIA | Brasil | 2909109 | 29 | 33 | nan | nan | nan | Cerrado | 103.0 |
| 473bfdaa-ae37-376d-ad4a-44437638d36e | -13.417 | -61.9169 | 2024-10-09 02:06:23 | GOES-16 | PIMENTEIRAS DO OESTE | RONDÔNIA | Brasil | 1101468 | 11 | 33 | nan | nan | nan | Amazônia | 59.3 |
| a8b99b32-d2c4-341d-8ebf-3720ecf0aec1 | -13.398 | -61.9182 | 2024-10-09 02:06:23 | GOES-16 | PIMENTEIRAS DO OESTE | RONDÔNIA | Brasil | 1101468 | 11 | 33 | nan | nan | nan | Amazônia | 88.4 |
| 747bb3f4-4cad-3d87-855f-01872c1dbbaf | -13.3978 | -61.9376 | 2024-10-09 02:06:23 | GOES-16 | PIMENTEIRAS DO OESTE | RONDÔNIA | Brasil | 1101468 | 11 | 33 | nan | nan | nan | Amazônia | 63.5 |
| 3b1987f6-df63-3f67-8a3e-905fc8a91fa9 | -13.8564 | -44.5657 | 2024-10-09 02:06:24 | GOES-16 | CORIBE | BAHIA | Brasil | 2909109 | 29 | 33 | nan | nan | nan | Cerrado | 86.7 |
| 8e0deb89-794c-3e28-a431-c4dcbfdec217 | -14.1197 | -44.9637 | 2024-10-09 02:06:25 | GOES-16 | COCOS | BAHIA | Brasil | 2908101 | 29 | 33 | nan | nan | nan | Cerrado | 97.0 |
| dab36573-3a5d-356b-8f79-fbe9dab07f94 | -15.5996 | -57.3699 | 2024-10-09 02:06:34 | GOES-16 | PORTO ESTRELA | MATO GROSSO | Brasil | 5106851 | 51 | 33 | nan | nan | nan | Cerrado | 59.2 |
| 65ee1f54-39a5-34d4-864d-d87975c7d8e4 | -16.4187 | -55.9248 | 2024-10-09 02:06:39 | GOES-16 | BARÃO DE MELGAÇO | MATO GROSSO | Brasil | 5101605 | 51 | 33 | nan | nan | nan | Pantanal | 65.3 |
| ded38564-55ef-3c65-9f3d-46fd593db903 | -16.4184 | -55.9455 | 2024-10-09 02:06:39 | GOES-16 | BARÃO DE MELGAÇO | MATO GROSSO | Brasil | 5101605 | 51 | 33 | nan | nan | nan | Pantanal | 84.9 |
| 523ba515-4571-3297-a911-c84c5dfb79b7 | -17.0795 | -57.3674 | 2024-10-09 02:06:42 | GOES-16 | POCONÉ | MATO GROSSO | Brasil | 5106505 | 51 | 33 | nan | nan | nan | Pantanal | 72.3 |
| 0cb6d2c1-db1e-36f8-af05-d6212a500cff | -17.0792 | -57.3879 | 2024-10-09 02:06:42 | GOES-16 | POCONÉ | MATO GROSSO | Brasil | 5106505 | 51 | 33 | nan | nan | nan | Pantanal | 44.6 |
| 45c472ef-4816-325d-a30c-f4d1920f0fb0 | -17.0623 | -56.0308 | 2024-10-09 02:06:42 | GOES-16 | BARÃO DE MELGAÇO | MATO GROSSO | Brasil | 5101605 | 51 | 33 | nan | nan | nan | Pantanal | 95.0 |
| 2caa2a74-d319-327a-9ba7-d6aa6e57a195 | -17.0404 | -55.0345 | 2024-10-09 02:06:42 | GOES-16 | SANTO ANTÔNIO DO LEVERGER | MATO GROSSO | Brasil | 5107800 | 51 | 33 | nan | nan | nan | Cerrado | 76.6 |
| 9611d2f3-e624-3675-bad1-5ed09238bd76 | -17.0207 | -55.0371 | 2024-10-09 02:06:42 | GOES-16 | SANTO ANTÔNIO DO LEVERGER | MATO GROSSO | Brasil | 5107800 | 51 | 33 | nan | nan | nan | Cerrado | 67.3 |
| 3e6f265f-debf-3d0c-a70b-66ee5c6fa5a8 | -17.3353 | -55.0156 | 2024-10-09 02:06:43 | GOES-16 | ITIQUIRA | MATO GROSSO | Brasil | 5104609 | 51 | 33 | nan | nan | nan | Pantanal | 94.8 |
| 77fdae76-1a3e-36db-ad76-63a88412377f | -17.1568 | -57.4403 | 2024-10-09 02:06:43 | GOES-16 | CÁCERES | MATO GROSSO | Brasil | 5102504 | 51 | 33 | nan | nan | nan | Pantanal | 52.6 |
| 47f8aca4-04f5-3f19-8643-cfae5a832162 | -17.1588 | -56.1222 | 2024-10-09 02:06:43 | GOES-16 | BARÃO DE MELGAÇO | MATO GROSSO | Brasil | 5101605 | 51 | 33 | nan | nan | nan | Pantanal | 107.9 |
| 9e0afe17-924c-377a-bdea-27520e1d6675 | -17.1467 | -56.8463 | 2024-10-09 02:06:43 | GOES-16 | POCONÉ | MATO GROSSO | Brasil | 5106505 | 51 | 33 | nan | nan | nan | Pantanal | 90.2 |
| 7bc52fb2-db64-36b2-beb1-cca3a2dde778 | -17.1375 | -57.4221 | 2024-10-09 02:06:43 | GOES-16 | CÁCERES | MATO GROSSO | Brasil | 5102504 | 51 | 33 | nan | nan | nan | Pantanal | 59.4 |
| ff89f559-3a44-3c6c-9052-dafcbcb75272 | -17.1371 | -57.4426 | 2024-10-09 02:06:43 | GOES-16 | CÁCERES | MATO GROSSO | Brasil | 5102504 | 51 | 33 | nan | nan | nan | Pantanal | 84.8 |
| 6c6f4c0f-fad7-3c28-83ab-bb40f0d0f1af | -17.1368 | -57.4631 | 2024-10-09 02:06:43 | GOES-16 | CÁCERES | MATO GROSSO | Brasil | 5102504 | 51 | 33 | nan | nan | nan | Pantanal | 44.1 |
| a9bedc20-c6a8-346d-b5a9-ae8ba4bcbc31 | -17.1271 | -56.8486 | 2024-10-09 02:06:43 | GOES-16 | POCONÉ | MATO GROSSO | Brasil | 5106505 | 51 | 33 | nan | nan | nan | Pantanal | 81.2 |
| 7af55106-269c-383a-a8c6-728d7d64f0ed | -17.1175 | -57.4449 | 2024-10-09 02:06:43 | GOES-16 | CÁCERES | MATO GROSSO | Brasil | 5102504 | 51 | 33 | nan | nan | nan | Pantanal | 63.2 |
| e2122642-8cea-3200-83a3-39722ed83054 | -17.1172 | -57.4654 | 2024-10-09 02:06:43 | GOES-16 | CÁCERES | MATO GROSSO | Brasil | 5102504 | 51 | 33 | nan | nan | nan | Pantanal | 42.6 |
| 675b14a7-3efe-3550-b72b-f5c4263d3e8a | -17.3551 | -55.0129 | 2024-10-09 02:06:44 | GOES-16 | ITIQUIRA | MATO GROSSO | Brasil | 5104609 | 51 | 33 | nan | nan | nan | Pantanal | 114.7 |
| c5894697-6fec-3536-ae7b-7940a41570c7 | -17.3547 | -55.0339 | 2024-10-09 02:06:44 | GOES-16 | ITIQUIRA | MATO GROSSO | Brasil | 5104609 | 51 | 33 | nan | nan | nan | Pantanal | 104.2 |
| 5db1af1c-6fe1-3b63-8951-23cb27a18865 | -18.1193 | -56.3921 | 2024-10-09 02:06:48 | GOES-16 | CORUMBÁ | MATO GROSSO DO SUL | Brasil | 5003207 | 50 | 33 | nan | nan | nan | Pantanal | 70.0 |
| b24bb89d-3320-359a-a43c-163107b0d253 | -18.4922 | -53.4887 | 2024-10-09 02:06:49 | GOES-16 | COSTA RICA | MATO GROSSO DO SUL | Brasil | 5003256 | 50 | 33 | nan | nan | nan | Cerrado | 80.0 |
| 1e245048-c679-3160-8e22-fbdff15f1404 | -20.3346 | -48.7307 | 2024-10-09 02:06:59 | GOES-16 | COLÔMBIA | SÃO PAULO | Brasil | 3512100 | 35 | 33 | nan | nan | nan | Cerrado | 189.4 |
| 86d7fade-c72e-3c56-8e68-551fcf72c81c | -20.3352 | -48.7076 | 2024-10-09 02:06:59 | GOES-16 | COLÔMBIA | SÃO PAULO | Brasil | 3512100 | 35 | 33 | nan | nan | nan | Cerrado | 192.6 |
| fb8d43b2-518c-3ae4-a78c-1e9cef0fb1e4 | -20.3551 | -48.7262 | 2024-10-09 02:06:59 | GOES-16 | COLÔMBIA | SÃO PAULO | Brasil | 3512100 | 35 | 33 | nan | nan | nan | Cerrado | 224.5 |
| 62a79f50-b699-3ea2-a62f-c051f45f2823 | -20.3557 | -48.7031 | 2024-10-09 02:06:59 | GOES-16 | COLÔMBIA | SÃO PAULO | Brasil | 3512100 | 35 | 33 | nan | nan | nan | Cerrado | 183.8 |
| dd96bc26-7cde-3f4e-b574-1abd41f3bdfe | -20.3755 | -48.7217 | 2024-10-09 02:06:59 | GOES-16 | BARRETOS | SÃO PAULO | Brasil | 3505500 | 35 | 33 | nan | nan | nan | Cerrado | 107.7 |
| 689db0b1-d3e0-3e0f-b3e3-9b873623dbb8 | -20.7839 | -47.2559 | 2024-10-09 02:07:01 | GOES-16 | PATROCÍNIO PAULISTA | SÃO PAULO | Brasil | 3536307 | 35 | 33 | nan | nan | nan | Cerrado | 85.4 |
| 2f8ee63d-3647-337e-b82e-b292376929e5 | -20.7846 | -47.2323 | 2024-10-09 02:07:01 | GOES-16 | PATROCÍNIO PAULISTA | SÃO PAULO | Brasil | 3536307 | 35 | 33 | nan | nan | nan | Cerrado | 84.8 |
| a874bf7c-3f62-3021-8ac3-6e292e9a1296 | -20.8052 | -47.2273 | 2024-10-09 02:07:01 | GOES-16 | PATROCÍNIO PAULISTA | SÃO PAULO | Brasil | 3536307 | 35 | 33 | nan | nan | nan | Cerrado | 65.4 |
| 5cd31ee7-d61e-3fb8-8c1c-419112174e4a | -21.0408 | -47.5696 | 2024-10-09 02:07:02 | GOES-16 | BRODOWSKI | SÃO PAULO | Brasil | 3507803 | 35 | 33 | nan | nan | nan | Cerrado | 91.5 |
| f7c4da0e-b96d-30ae-9e71-447312b6cded | -21.1126 | -47.2229 | 2024-10-09 02:07:02 | GOES-16 | SANTO ANTÔNIO DA ALEGRIA | SÃO PAULO | Brasil | 3547908 | 35 | 33 | nan | nan | nan | Cerrado | 88.2 |
| 76027fd8-73bb-33c2-8669-12b123aedcd6 | -21.5727 | -46.9659 | 2024-10-09 02:07:05 | GOES-16 | MOCOCA | SÃO PAULO | Brasil | 3530508 | 35 | 33 | nan | nan | nan | Cerrado | 106.5 |
| 297cf3ba-12d8-371f-83aa-962cfaf2dd77 | -21.5864 | -47.8827 | 2024-10-09 02:07:05 | GOES-16 | LUÍS ANTÔNIO | SÃO PAULO | Brasil | 3527603 | 35 | 33 | nan | nan | nan | Cerrado | 71.3 |
| 72e90975-7885-34d1-aa91-793fcd89e2e7 | -22.1369 | -48.1224 | 2024-10-09 02:07:08 | GOES-16 | RIBEIRÃO BONITO | SÃO PAULO | Brasil | 3542909 | 35 | 33 | nan | nan | nan | Cerrado | 125.9 |
| 465d1d4c-98e7-3b5f-b7ed-39ea43ab628e | -22.1578 | -48.1172 | 2024-10-09 02:07:08 | GOES-16 | RIBEIRÃO BONITO | SÃO PAULO | Brasil | 3542909 | 35 | 33 | nan | nan | nan | Cerrado | 167.1 |
| 621fe3c1-70c5-3ac7-91e1-63ff2c38c22b | -22.1772 | -48.1593 | 2024-10-09 02:07:08 | GOES-16 | BROTAS | SÃO PAULO | Brasil | 3507902 | 35 | 33 | nan | nan | nan | Cerrado | 140.8 |
| 4d4a3805-2591-330e-9ddf-500b72c64cac | -22.1981 | -48.1541 | 2024-10-09 02:07:08 | GOES-16 | BROTAS | SÃO PAULO | Brasil | 3507902 | 35 | 33 | nan | nan | nan | Cerrado | 164.9 |
| 48a73287-a696-3e40-a012-9351aa6764a3 | -22.7927 | -48.4278 | 2024-10-09 02:07:11 | GOES-16 | BOTUCATU | SÃO PAULO | Brasil | 3507506 | 35 | 33 | nan | nan | nan | Cerrado | 70.8 |
| d8f2ca20-e9b1-34fc-9515-403c1885b0b7 | -22.813 | -48.4462 | 2024-10-09 02:07:11 | GOES-16 | BOTUCATU | SÃO PAULO | Brasil | 3507506 | 35 | 33 | nan | nan | nan | Cerrado | 63.9 |
| 4e267626-aa62-3458-afe2-fc50cb4a3202 | -22.8137 | -48.4225 | 2024-10-09 02:07:11 | GOES-16 | BOTUCATU | SÃO PAULO | Brasil | 3507506 | 35 | 33 | nan | nan | nan | Cerrado | 93.6 |
| 89bfeace-cca5-357d-bb48-3447b94e5ab6 | -1.11 | -53.6173 | 2024-10-09 02:15:12 | GOES-16 | ALMEIRIM | PARÁ | Brasil | 1500503 | 15 | 33 | nan | nan | nan | Amazônia | 96.0 |
| c7bf9066-6270-356f-b25f-0084bca1c36b | -3.8008 | -41.5989 | 2024-10-09 02:15:27 | GOES-16 | PIRACURUCA | PIAUÍ | Brasil | 2208304 | 22 | 33 | nan | nan | nan | Caatinga | 74.4 |
| 092a5fe8-cbe4-3c6c-96c9-1d79a7b71609 | -3.8196 | -41.5979 | 2024-10-09 02:15:28 | GOES-16 | PIRACURUCA | PIAUÍ | Brasil | 2208304 | 22 | 33 | nan | nan | nan | Caatinga | 81.9 |
| 971a5126-08e0-3fdc-a924-19a29aa88b09 | -3.9021 | -46.4689 | 2024-10-09 02:15:28 | GOES-16 | BOM JARDIM | MARANHÃO | Brasil | 2102002 | 21 | 33 | nan | nan | nan | Amazônia | 61.8 |
| c3b64343-36eb-3166-a30e-2bd42c2b1dc2 | -3.9023 | -46.4467 | 2024-10-09 02:15:28 | GOES-16 | BOM JARDIM | MARANHÃO | Brasil | 2102002 | 21 | 33 | nan | nan | nan | Amazônia | 67.2 |
| 087ee5fd-3a94-332e-bfa2-bc9153474ff9 | -3.9208 | -46.4459 | 2024-10-09 02:15:28 | GOES-16 | BOM JARDIM | MARANHÃO | Brasil | 2102002 | 21 | 33 | nan | nan | nan | Amazônia | 51.4 |
| 1dc87c78-ce48-3e4b-8063-26b60c37cb6a | -3.9393 | -46.4672 | 2024-10-09 02:15:28 | GOES-16 | BOM JARDIM | MARANHÃO | Brasil | 2102002 | 21 | 33 | nan | nan | nan | Amazônia | 65.6 |
| 98b0fce4-c20b-3c65-b80b-cc3c215b2b10 | -3.9394 | -46.445 | 2024-10-09 02:15:28 | GOES-16 | BOM JARDIM | MARANHÃO | Brasil | 2102002 | 21 | 33 | nan | nan | nan | Amazônia | 112.6 |
| 683e32bb-9f6f-3ee5-ac61-89b5e69a1042 | -5.5858 | -43.2562 | 2024-10-09 02:15:38 | GOES-16 | PARNARAMA | MARANHÃO | Brasil | 2107803 | 21 | 33 | nan | nan | nan | Cerrado | 49.2 |
| 9346c899-632e-3989-9ed5-e50d50ba9bdf | -6.7613 | -60.0751 | 2024-10-09 02:15:45 | GOES-16 | NOVO ARIPUANÃ | AMAZONAS | Brasil | 1303304 | 13 | 33 | nan | nan | nan | Amazônia | 46.6 |
| 7d9e01a3-6773-338c-9335-955591929b2c | -6.7614 | -60.0559 | 2024-10-09 02:15:45 | GOES-16 | NOVO ARIPUANÃ | AMAZONAS | Brasil | 1303304 | 13 | 33 | nan | nan | nan | Amazônia | 180.0 |
| 2d787c84-036a-3102-b996-00709227baa0 | -6.7615 | -60.0367 | 2024-10-09 02:15:45 | GOES-16 | NOVO ARIPUANÃ | AMAZONAS | Brasil | 1303304 | 13 | 33 | nan | nan | nan | Amazônia | 62.6 |
| 89f5464b-aa7c-3e3b-ac8c-0bf93968b0df | -6.7797 | -60.0744 | 2024-10-09 02:15:45 | GOES-16 | NOVO ARIPUANÃ | AMAZONAS | Brasil | 1303304 | 13 | 33 | nan | nan | nan | Amazônia | 42.8 |
| ad947e44-2e29-336f-9bac-664abaa2b9b8 | -6.7798 | -60.0552 | 2024-10-09 02:15:45 | GOES-16 | NOVO ARIPUANÃ | AMAZONAS | Brasil | 1303304 | 13 | 33 | nan | nan | nan | Amazônia | 177.5 |
| 10d0ff65-e76a-3e23-b016-9ae07fb434a6 | -6.7799 | -60.036 | 2024-10-09 02:15:45 | GOES-16 | NOVO ARIPUANÃ | AMAZONAS | Brasil | 1303304 | 13 | 33 | nan | nan | nan | Amazônia | 65.8 |
| b04a0106-6f1c-3e53-a11c-432c1782694d | -8.3217 | -44.0983 | 2024-10-09 02:15:53 | GOES-16 | MANOEL EMÍDIO | PIAUÍ | Brasil | 2205904 | 22 | 33 | nan | nan | nan | Cerrado | 67.5 |
| 13b1afeb-05c2-36c4-8dc7-50cbf5edee91 | -8.4919 | -48.6476 | 2024-10-09 02:15:54 | GOES-16 | PRESIDENTE KENNEDY | TOCANTINS | Brasil | 1718402 | 17 | 33 | nan | nan | nan | Amazônia | 122.8 |
| 93a01722-8446-35c5-8d7f-4ee87f82a3a3 | -8.4921 | -48.6259 | 2024-10-09 02:15:54 | GOES-16 | PRESIDENTE KENNEDY | TOCANTINS | Brasil | 1718402 | 17 | 33 | nan | nan | nan | Amazônia | 84.5 |
| 4aadac99-6346-3826-9bce-89f01d539b54 | -10.3655 | -64.8451 | 2024-10-09 02:16:06 | GOES-16 | NOVA MAMORÉ | RONDÔNIA | Brasil | 1100338 | 11 | 33 | nan | nan | nan | Amazônia | 66.4 |
| cfed258e-2fba-3f3c-8bd0-1691ea88ec0e | -10.3656 | -64.8262 | 2024-10-09 02:16:06 | GOES-16 | NOVA MAMORÉ | RONDÔNIA | Brasil | 1100338 | 11 | 33 | nan | nan | nan | Amazônia | 68.5 |
| 45fec61e-a967-3c9c-8725-ffc3efa26a4d | -10.3894 | -61.2502 | 2024-10-09 02:16:06 | GOES-16 | RONDOLÂNDIA | MATO GROSSO | Brasil | 5107578 | 51 | 33 | nan | nan | nan | Amazônia | 57.9 |


[Clique aqui para ver as próximas entradas](README51.md)
