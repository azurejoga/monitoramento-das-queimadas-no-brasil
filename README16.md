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

## Dados Diários - Página 16

| ID | Latitude | Longitude | Data/Hora GMT | Satélite | Município | Estado | País | Município ID | Estado ID | País ID | Dias sem Chuva | Precipitação | Risco de Fogo | Bioma | FRP |
|----|----------|-----------|---------------|----------|-----------|--------|------|--------------|-----------|---------|----------------|--------------|----------------|-------|-----|
| 4dcdb500-c853-35eb-9b65-7df7f33a0512 | -8.66378 | -66.56875 | 2026-07-18 05:59:00 | NPP-375D | LÁBREA | AMAZONAS | Brasil | 1302405 | 13 | 33 | nan | nan | nan | Amazônia | 1.0 |
| d078d5ff-cf8b-3002-aa21-796bf8a98f67 | -9.48261 | -57.32473 | 2026-07-18 05:59:00 | NPP-375D | APIACÁS | MATO GROSSO | Brasil | 5100805 | 51 | 33 | nan | nan | nan | Amazônia | 0.5 |
| 37899a6d-f4c8-3afc-acf8-1943bc4dd946 | -9.47678 | -57.32389 | 2026-07-18 05:59:00 | NPP-375D | APIACÁS | MATO GROSSO | Brasil | 5100805 | 51 | 33 | nan | nan | nan | Amazônia | 0.5 |
| 212a5588-a9b6-3094-af60-d127aca6770f | -13.3221 | -45.1246 | 2026-07-18 06:00:00 | GOES-19 | CORRENTINA | BAHIA | Brasil | 2909307 | 29 | 33 | nan | nan | nan | Cerrado | 129.2 |
| f742335f-1935-3756-907e-6973cef43632 | -13.3028 | -45.1278 | 2026-07-18 06:00:00 | GOES-19 | CORRENTINA | BAHIA | Brasil | 2909307 | 29 | 33 | nan | nan | nan | Cerrado | 93.4 |
| 3d99570a-d0d8-3527-8fba-5bb9a033cf3a | -18.7364 | -54.1988 | 2026-07-18 06:00:00 | GOES-19 | FIGUEIRÃO | MATO GROSSO DO SUL | Brasil | 5003900 | 50 | 33 | nan | nan | nan | Cerrado | 73.5 |
| a8c821eb-310c-3d53-9d98-7d3f91f3acbc | -13.3023 | -45.1511 | 2026-07-18 06:00:00 | GOES-19 | CORRENTINA | BAHIA | Brasil | 2909307 | 29 | 33 | nan | nan | nan | Cerrado | 136.8 |
| 723628b3-e965-38ec-a958-f7d31307ddad | -13.3217 | -45.1479 | 2026-07-18 06:00:00 | GOES-19 | CORRENTINA | BAHIA | Brasil | 2909307 | 29 | 33 | nan | nan | nan | Cerrado | 184.4 |
| 6344456d-eafe-3a40-8723-a7d2faafbc2a | -19.86907 | -57.95819 | 2026-07-18 06:01:00 | NPP-375D | CORUMBÁ | MATO GROSSO DO SUL | Brasil | 5003207 | 50 | 33 | nan | nan | nan | Pantanal | 1.9 |
| ca041dbe-405d-364b-b31a-c4bf47a333a9 | -19.83174 | -57.9977 | 2026-07-18 06:01:00 | NPP-375D | CORUMBÁ | MATO GROSSO DO SUL | Brasil | 5003207 | 50 | 33 | nan | nan | nan | Pantanal | 1.3 |
| e4e5a51f-4430-336e-8f41-95af17101332 | -19.81798 | -57.93715 | 2026-07-18 06:01:00 | NPP-375D | CORUMBÁ | MATO GROSSO DO SUL | Brasil | 5003207 | 50 | 33 | nan | nan | nan | Pantanal | 2.9 |
| 14079e12-4bf0-3f04-aa73-0a7aaa6d79dc | -19.81907 | -57.99637 | 2026-07-18 06:01:00 | NPP-375D | CORUMBÁ | MATO GROSSO DO SUL | Brasil | 5003207 | 50 | 33 | nan | nan | nan | Pantanal | 4.8 |
| f5a46622-abd9-3aec-93d1-72114c628845 | -10.94205 | -68.74915 | 2026-07-18 06:01:00 | NPP-375D | BRASILÉIA | ACRE | Brasil | 1200104 | 12 | 33 | nan | nan | nan | Amazônia | 0.7 |
| ae3dd312-edce-34f8-8ae6-ed4cc3fdad46 | -19.8121 | -57.93114 | 2026-07-18 06:01:00 | NPP-375D | CORUMBÁ | MATO GROSSO DO SUL | Brasil | 5003207 | 50 | 33 | nan | nan | nan | Pantanal | 2.9 |
| e356c4c0-be1b-33f5-9e8b-8553b403e934 | -19.81368 | -57.9851 | 2026-07-18 06:01:00 | NPP-375D | CORUMBÁ | MATO GROSSO DO SUL | Brasil | 5003207 | 50 | 33 | nan | nan | nan | Pantanal | 1.5 |
| f9b94632-5ecf-32c6-a558-0204dcc412ad | -19.82588 | -57.99173 | 2026-07-18 06:01:00 | NPP-375D | CORUMBÁ | MATO GROSSO DO SUL | Brasil | 5003207 | 50 | 33 | nan | nan | nan | Pantanal | 3.5 |
| 351543a1-7446-389e-b7b6-de50398ab3cc | -10.94262 | -68.74562 | 2026-07-18 06:01:00 | NPP-375D | BRASILÉIA | ACRE | Brasil | 1200104 | 12 | 33 | nan | nan | nan | Amazônia | 0.4 |
| 6275a25d-9b5b-32ed-bff2-4f27e5ef7e14 | -19.81846 | -57.93181 | 2026-07-18 06:01:00 | NPP-375D | CORUMBÁ | MATO GROSSO DO SUL | Brasil | 5003207 | 50 | 33 | nan | nan | nan | Pantanal | 2.9 |
| cd001e4a-251a-3804-b74b-a03e898f31b5 | -19.81954 | -57.99107 | 2026-07-18 06:01:00 | NPP-375D | CORUMBÁ | MATO GROSSO DO SUL | Brasil | 5003207 | 50 | 33 | nan | nan | nan | Pantanal | 3.5 |
| de2e9e22-7c4f-3394-8406-f3032f4c6848 | -19.81162 | -57.93649 | 2026-07-18 06:01:00 | NPP-375D | CORUMBÁ | MATO GROSSO DO SUL | Brasil | 5003207 | 50 | 33 | nan | nan | nan | Pantanal | 2.9 |
| 54573d19-b1e9-3c62-b761-24ea676b7dd9 | -19.82541 | -57.99704 | 2026-07-18 06:01:00 | NPP-375D | CORUMBÁ | MATO GROSSO DO SUL | Brasil | 5003207 | 50 | 33 | nan | nan | nan | Pantanal | 4.8 |
| 6927c4ee-079a-3f66-9786-24f6e2fe9b36 | -13.3217 | -45.1479 | 2026-07-18 06:10:00 | GOES-19 | CORRENTINA | BAHIA | Brasil | 2909307 | 29 | 33 | nan | nan | nan | Cerrado | 175.7 |
| 6c4f39ed-350e-37cd-bd49-af46b5bc1eb4 | -18.7364 | -54.1988 | 2026-07-18 06:10:00 | GOES-19 | FIGUEIRÃO | MATO GROSSO DO SUL | Brasil | 5003900 | 50 | 33 | nan | nan | nan | Cerrado | 61.5 |
| 191ab99d-f51c-3b2e-9f86-14d84e042121 | -13.3023 | -45.1511 | 2026-07-18 06:10:00 | GOES-19 | CORRENTINA | BAHIA | Brasil | 2909307 | 29 | 33 | nan | nan | nan | Cerrado | 83.9 |
| 52cfd595-8e98-3917-9a24-d146593e4e73 | -13.3221 | -45.1246 | 2026-07-18 06:10:00 | GOES-19 | CORRENTINA | BAHIA | Brasil | 2909307 | 29 | 33 | nan | nan | nan | Cerrado | 112.2 |
| f5eb9644-899a-3940-b3a6-8fa8a932c586 | -13.3028 | -45.1278 | 2026-07-18 06:10:00 | GOES-19 | CORRENTINA | BAHIA | Brasil | 2909307 | 29 | 33 | nan | nan | nan | Cerrado | 55.6 |
| 2c5b3969-e94d-3d3d-a6ae-e7b658298709 | -13.3 | -45.14 | 2026-07-18 06:15:00 | MSG-03 | CORRENTINA | BAHIA | Brasil | 2909307 | 29 | 33 | nan | nan | nan | Cerrado | nan |
| 4fe3413e-11cb-387c-be71-9ad89af9c26d | -13.3217 | -45.1479 | 2026-07-18 06:20:00 | GOES-19 | CORRENTINA | BAHIA | Brasil | 2909307 | 29 | 33 | nan | nan | nan | Cerrado | 155.0 |
| d801408c-45e0-354e-9b0e-9d4e33ea57b9 | -18.7364 | -54.1988 | 2026-07-18 06:20:00 | GOES-19 | FIGUEIRÃO | MATO GROSSO DO SUL | Brasil | 5003900 | 50 | 33 | nan | nan | nan | Cerrado | 54.6 |
| 24663b26-3d4b-3c7e-a803-08440a74ae1f | -13.3221 | -45.1246 | 2026-07-18 06:20:00 | GOES-19 | CORRENTINA | BAHIA | Brasil | 2909307 | 29 | 33 | nan | nan | nan | Cerrado | 97.8 |
| 9c6362de-394f-32e0-ade5-f1947dc9eb5d | -13.3023 | -45.1511 | 2026-07-18 06:20:00 | GOES-19 | CORRENTINA | BAHIA | Brasil | 2909307 | 29 | 33 | nan | nan | nan | Cerrado | 61.9 |
| b2fd2143-a245-3a22-bd0e-4084f6e352e9 | -18.7364 | -54.1988 | 2026-07-18 06:30:00 | GOES-19 | FIGUEIRÃO | MATO GROSSO DO SUL | Brasil | 5003900 | 50 | 33 | nan | nan | nan | Cerrado | 63.3 |
| 221b93f6-5871-3d87-95a5-f14bb208c694 | -15.556 | -55.1612 | 2026-07-18 06:30:00 | GOES-19 | CAMPO VERDE | MATO GROSSO | Brasil | 5102678 | 51 | 33 | nan | nan | nan | Cerrado | 44.7 |
| 6734a081-6020-376d-a746-f67e2233c101 | -13.3217 | -45.1479 | 2026-07-18 06:30:00 | GOES-19 | CORRENTINA | BAHIA | Brasil | 2909307 | 29 | 33 | nan | nan | nan | Cerrado | 114.8 |
| 48308f6a-3bb7-39e6-a628-8f5b24ad234c | -13.3023 | -45.1511 | 2026-07-18 06:30:00 | GOES-19 | CORRENTINA | BAHIA | Brasil | 2909307 | 29 | 33 | nan | nan | nan | Cerrado | 49.1 |
| e4dc939b-4716-3355-b49f-431d3fd64f21 | -13.3221 | -45.1246 | 2026-07-18 06:30:00 | GOES-19 | CORRENTINA | BAHIA | Brasil | 2909307 | 29 | 33 | nan | nan | nan | Cerrado | 81.6 |
| 9155e3d0-15a2-34ed-8f03-420feb00ff3f | -13.3217 | -45.1479 | 2026-07-18 06:40:00 | GOES-19 | CORRENTINA | BAHIA | Brasil | 2909307 | 29 | 33 | nan | nan | nan | Cerrado | 109.7 |
| c7293cca-b80c-3dc0-8893-29417b64350d | -13.3221 | -45.1246 | 2026-07-18 06:40:00 | GOES-19 | CORRENTINA | BAHIA | Brasil | 2909307 | 29 | 33 | nan | nan | nan | Cerrado | 67.8 |
| 2d5bef0e-c0ca-32e2-b9a3-4ec52da0b632 | -13.3023 | -45.1511 | 2026-07-18 06:40:00 | GOES-19 | CORRENTINA | BAHIA | Brasil | 2909307 | 29 | 33 | nan | nan | nan | Cerrado | 43.6 |
| c8b11947-36ad-38c6-99da-3dea37d2e512 | -2.04235 | -48.02932 | 2026-07-18 06:46:00 | AQUA_M-M | CONCÓRDIA DO PARÁ | PARÁ | Brasil | 1502756 | 15 | 33 | nan | nan | nan | Amazônia | 4.6 |
| b7d965b5-1dd2-39a7-a456-94782205cda0 | -9.07238 | -50.5888 | 2026-07-18 06:46:00 | AQUA_M-M | SANTANA DO ARAGUAIA | PARÁ | Brasil | 1506708 | 15 | 33 | nan | nan | nan | Amazônia | 4.5 |
| 32139513-f83f-3ca0-9fd0-afa2b1eba8f8 | -5.92916 | -43.63715 | 2026-07-18 06:46:00 | AQUA_M-M | LAGOA DO MATO | MARANHÃO | Brasil | 2105922 | 21 | 33 | nan | nan | nan | Cerrado | 33.4 |
| d2dceecf-3e01-3776-b1c9-1989980fa66b | -2.76832 | -49.46437 | 2026-07-18 06:46:00 | AQUA_M-M | MOJU | PARÁ | Brasil | 1504703 | 15 | 33 | nan | nan | nan | Amazônia | 6.7 |
| 056c7dd2-537c-3487-88fb-76267c5b2f01 | -8.94233 | -47.60679 | 2026-07-18 06:46:00 | AQUA_M-M | BOM JESUS DO TOCANTINS | TOCANTINS | Brasil | 1703305 | 17 | 33 | nan | nan | nan | Cerrado | 12.9 |
| efe5166b-b013-3e34-93fd-3390e476434b | -7.9151 | -48.25633 | 2026-07-18 06:46:00 | AQUA_M-M | PALMEIRANTE | TOCANTINS | Brasil | 1715705 | 17 | 33 | nan | nan | nan | Cerrado | 6.3 |
| f60983a8-1027-3e72-a5a8-2b032427b67d | -9.52486 | -47.12005 | 2026-07-18 06:46:00 | AQUA_M-M | RIO SONO | TOCANTINS | Brasil | 1718758 | 17 | 33 | nan | nan | nan | Cerrado | 6.4 |
| d76b7df3-ecce-3f6a-9ad1-43c3c014fb8a | -13.31379 | -45.13023 | 2026-07-18 06:48:00 | AQUA_M-M | CORRENTINA | BAHIA | Brasil | 2909307 | 29 | 33 | nan | nan | nan | Cerrado | 105.2 |
| 278a8c46-2088-3f5b-b710-d99a88bbace0 | -13.31141 | -45.149 | 2026-07-18 06:48:00 | AQUA_M-M | CORRENTINA | BAHIA | Brasil | 2909307 | 29 | 33 | nan | nan | nan | Cerrado | 127.6 |
| 86ea991c-7114-3fdf-b3f4-a68f6d46c2fd | -15.55128 | -55.15599 | 2026-07-18 06:48:00 | AQUA_M-M | CAMPO VERDE | MATO GROSSO | Brasil | 5102678 | 51 | 33 | nan | nan | nan | Cerrado | 18.2 |
| dfc0e222-4229-3180-8c73-5bbfc0ba2f19 | -15.54931 | -55.16783 | 2026-07-18 06:48:00 | AQUA_M-M | CAMPO VERDE | MATO GROSSO | Brasil | 5102678 | 51 | 33 | nan | nan | nan | Cerrado | 31.5 |
| f2a023cd-5976-334c-a68f-a34eaa4b2596 | -13.3221 | -45.1246 | 2026-07-18 06:50:00 | GOES-19 | CORRENTINA | BAHIA | Brasil | 2909307 | 29 | 33 | nan | nan | nan | Cerrado | 62.7 |
| 8cfd09a2-500c-3209-9221-65ab15eb8052 | -18.7364 | -54.1988 | 2026-07-18 06:50:00 | GOES-19 | FIGUEIRÃO | MATO GROSSO DO SUL | Brasil | 5003900 | 50 | 33 | nan | nan | nan | Cerrado | 62.7 |
| 269a8b8d-974b-3fe9-a551-94c24d52c738 | -13.3217 | -45.1479 | 2026-07-18 06:50:00 | GOES-19 | CORRENTINA | BAHIA | Brasil | 2909307 | 29 | 33 | nan | nan | nan | Cerrado | 74.4 |
| 8fe1baab-4056-3fb2-be1e-6287dbfcd8d7 | -18.72597 | -54.1953 | 2026-07-18 06:50:00 | AQUA_M-M | FIGUEIRÃO | MATO GROSSO DO SUL | Brasil | 5003900 | 50 | 33 | nan | nan | nan | Cerrado | 18.1 |
| df294b0f-c1ed-3d9c-b360-9076e1709439 | -18.73506 | -54.19682 | 2026-07-18 06:50:00 | AQUA_M-M | FIGUEIRÃO | MATO GROSSO DO SUL | Brasil | 5003900 | 50 | 33 | nan | nan | nan | Cerrado | 50.3 |
| 54b3a630-3a52-3744-8ff5-9c52804b249f | -18.73346 | -54.20675 | 2026-07-18 06:50:00 | AQUA_M-M | FIGUEIRÃO | MATO GROSSO DO SUL | Brasil | 5003900 | 50 | 33 | nan | nan | nan | Cerrado | 20.8 |
| 8cc6dbed-456b-321e-97ad-e55a2eb784cd | -18.72436 | -54.20526 | 2026-07-18 06:50:00 | AQUA_M-M | FIGUEIRÃO | MATO GROSSO DO SUL | Brasil | 5003900 | 50 | 33 | nan | nan | nan | Cerrado | 6.9 |
| ee76c43c-9bfd-3711-9245-16cc68be8118 | -19.82262 | -57.99036 | 2026-07-18 06:52:00 | AQUA_M-M | CORUMBÁ | MATO GROSSO DO SUL | Brasil | 5003207 | 50 | 33 | nan | nan | nan | Pantanal | 10.3 |
| c3c28435-be13-3c87-a1c2-2b7be4c8ba9b | -19.80946 | -57.93252 | 2026-07-18 06:52:00 | AQUA_M-M | CORUMBÁ | MATO GROSSO DO SUL | Brasil | 5003207 | 50 | 33 | nan | nan | nan | Pantanal | 13.9 |
| 18d371fd-1ee0-3319-9e69-16b85886a3cf | -31.91068 | -51.88221 | 2026-07-18 06:54:00 | AQUA_M-M | SÃO JOSÉ DO NORTE | RIO GRANDE DO SUL | Brasil | 4318507 | 43 | 33 | nan | nan | nan | Pampa | 8.0 |
| cae5c582-9e6a-3521-b087-fdd7a9cbe368 | -31.92074 | -51.88383 | 2026-07-18 06:54:00 | AQUA_M-M | SÃO JOSÉ DO NORTE | RIO GRANDE DO SUL | Brasil | 4318507 | 43 | 33 | nan | nan | nan | Pampa | 13.4 |
| 735c0f56-aef5-3bec-9df5-9ef20f1a7071 | -13.3221 | -45.1246 | 2026-07-18 07:00:00 | GOES-19 | CORRENTINA | BAHIA | Brasil | 2909307 | 29 | 33 | nan | nan | nan | Cerrado | 55.0 |
| 55fa345d-e7f3-3a21-ad65-a4da226fe26f | -13.3217 | -45.1479 | 2026-07-18 07:00:00 | GOES-19 | CORRENTINA | BAHIA | Brasil | 2909307 | 29 | 33 | nan | nan | nan | Cerrado | 75.3 |
| d9681b8e-bedd-32cf-a599-54e62a89e8ce | -13.3221 | -45.1246 | 2026-07-18 07:10:00 | GOES-19 | CORRENTINA | BAHIA | Brasil | 2909307 | 29 | 33 | nan | nan | nan | Cerrado | 56.1 |
| a151947c-5256-38ea-a6d8-cc36af7d0c28 | -13.3217 | -45.1479 | 2026-07-18 07:10:00 | GOES-19 | CORRENTINA | BAHIA | Brasil | 2909307 | 29 | 33 | nan | nan | nan | Cerrado | 61.0 |
| 66976acc-a7e5-3967-88e8-2cf60151498f | -13.3217 | -45.1479 | 2026-07-18 07:20:00 | GOES-19 | CORRENTINA | BAHIA | Brasil | 2909307 | 29 | 33 | nan | nan | nan | Cerrado | 47.3 |
| 6ef3b1fb-e63a-30d2-94cb-57ff51bfce78 | -18.7364 | -54.1988 | 2026-07-18 07:20:00 | GOES-19 | FIGUEIRÃO | MATO GROSSO DO SUL | Brasil | 5003900 | 50 | 33 | nan | nan | nan | Cerrado | 58.6 |
| ebcf2c43-23e5-3b65-bc86-e86642585a44 | -13.3217 | -45.1479 | 2026-07-18 07:30:00 | GOES-19 | CORRENTINA | BAHIA | Brasil | 2909307 | 29 | 33 | nan | nan | nan | Cerrado | 49.5 |
| cce0ee97-e574-3e87-a6bf-d9443e1043a8 | -13.3221 | -45.1246 | 2026-07-18 07:30:00 | GOES-19 | CORRENTINA | BAHIA | Brasil | 2909307 | 29 | 33 | nan | nan | nan | Cerrado | 44.3 |
| 854191b9-ff52-3145-ba73-0b3c9e1e6654 | -13.3217 | -45.1479 | 2026-07-18 07:40:00 | GOES-19 | CORRENTINA | BAHIA | Brasil | 2909307 | 29 | 33 | nan | nan | nan | Cerrado | 51.8 |
| 8d200551-c7dd-3792-bdf9-4abdc1f04129 | -9.05949 | -44.84388 | 2026-07-18 11:23:00 | TERRA_M-M | BOM JESUS | PIAUÍ | Brasil | 2201903 | 22 | 33 | nan | nan | nan | Cerrado | 7.3 |
| 25531162-628d-34e5-82f4-05e04845a477 | -10.48086 | -42.47337 | 2026-07-18 11:23:00 | TERRA_M-M | XIQUE-XIQUE | BAHIA | Brasil | 2933604 | 29 | 33 | nan | nan | nan | Caatinga | 5.9 |
| 3545ab2c-e9f1-3aac-a9e7-bea67611b041 | -11.40868 | -47.52999 | 2026-07-18 11:23:00 | TERRA_M-M | NATIVIDADE | TOCANTINS | Brasil | 1714203 | 17 | 33 | nan | nan | nan | Cerrado | 12.7 |
| fff6a893-f76a-3f4a-90d6-d4039a90ec5b | -10.57232 | -44.32523 | 2026-07-18 11:23:00 | TERRA_M-M | SANTA RITA DE CÁSSIA | BAHIA | Brasil | 2928406 | 29 | 33 | nan | nan | nan | Cerrado | 5.5 |
| 30698ffb-7eca-3e3e-849e-b8e4addd53f0 | -10.70667 | -46.57317 | 2026-07-18 11:23:00 | TERRA_M-M | MATEIROS | TOCANTINS | Brasil | 1712702 | 17 | 33 | nan | nan | nan | Cerrado | 102.4 |
| cf925395-e8a6-382d-9424-94c22929d802 | -10.71321 | -46.58094 | 2026-07-18 11:23:00 | TERRA_M-M | MATEIROS | TOCANTINS | Brasil | 1712702 | 17 | 33 | nan | nan | nan | Cerrado | 45.6 |
| b5b8cb9c-d57b-3304-af83-de5db9e3b56e | -9.05589 | -44.83591 | 2026-07-18 11:23:00 | TERRA_M-M | BOM JESUS | PIAUÍ | Brasil | 2201903 | 22 | 33 | nan | nan | nan | Cerrado | 16.5 |
| fc13e1b7-a328-3557-afc2-3387e8e8d3c0 | -10.57408 | -44.31369 | 2026-07-18 11:23:00 | TERRA_M-M | SANTA RITA DE CÁSSIA | BAHIA | Brasil | 2928406 | 29 | 33 | nan | nan | nan | Cerrado | 6.9 |
| afdcee38-00df-3e39-b9f8-e39118050769 | -5.92928 | -43.63268 | 2026-07-18 11:23:00 | TERRA_M-M | LAGOA DO MATO | MARANHÃO | Brasil | 2105922 | 21 | 33 | nan | nan | nan | Cerrado | 13.3 |
| b46b9e1a-99f5-3510-9660-ca10662ec547 | -10.70927 | -46.55672 | 2026-07-18 11:23:00 | TERRA_M-M | MATEIROS | TOCANTINS | Brasil | 1712702 | 17 | 33 | nan | nan | nan | Cerrado | 10.7 |
| 4fd366ae-465a-3f15-b784-995e45215982 | -10.71591 | -46.56455 | 2026-07-18 11:23:00 | TERRA_M-M | MATEIROS | TOCANTINS | Brasil | 1712702 | 17 | 33 | nan | nan | nan | Cerrado | 28.1 |
| 6f4fdf9f-bc3b-3b98-9110-6d3556542033 | -9.06145 | -44.83081 | 2026-07-18 11:23:00 | TERRA_M-M | BOM JESUS | PIAUÍ | Brasil | 2201903 | 22 | 33 | nan | nan | nan | Cerrado | 5.9 |
| 4369ad25-5c32-3ad8-9c39-75c88711c2e5 | -5.92746 | -43.64466 | 2026-07-18 11:23:00 | TERRA_M-M | LAGOA DO MATO | MARANHÃO | Brasil | 2105922 | 21 | 33 | nan | nan | nan | Cerrado | 34.9 |
| ee4cbda1-3f7b-3019-be75-3ec007a26928 | -9.49459 | -46.66309 | 2026-07-18 11:23:00 | TERRA_M-M | LIZARDA | TOCANTINS | Brasil | 1712405 | 17 | 33 | nan | nan | nan | Cerrado | 14.4 |
| 7446e3a6-0598-3e2e-93d3-330617e10475 | -12.00451 | -50.57629 | 2026-07-18 11:25:00 | TERRA_M-M | FORMOSO DO ARAGUAIA | TOCANTINS | Brasil | 1708205 | 17 | 33 | nan | nan | nan | Cerrado | 37.4 |
| a1604e69-4877-3e8a-b03b-a7678d8f5be0 | -13.3185 | -45.145 | 2026-07-18 11:25:00 | TERRA_M-M | CORRENTINA | BAHIA | Brasil | 2909307 | 29 | 33 | nan | nan | nan | Cerrado | 15.2 |
| 3715798a-4acf-396d-af5d-4d846eefb196 | -15.71097 | -43.3768 | 2026-07-18 11:25:00 | TERRA_M-M | JANAÚBA | MINAS GERAIS | Brasil | 3135100 | 31 | 33 | nan | nan | nan | Cerrado | 49.2 |
| f0824442-47a8-37f3-a998-987e52c63dc5 | -12.01028 | -50.5715 | 2026-07-18 11:25:00 | TERRA_M-M | FORMOSO DO ARAGUAIA | TOCANTINS | Brasil | 1708205 | 17 | 33 | nan | nan | nan | Cerrado | 31.3 |
| f2b2f9cd-8a4f-310e-99f0-a5f6d71cb6ae | -15.70958 | -43.38621 | 2026-07-18 11:25:00 | TERRA_M-M | JANAÚBA | MINAS GERAIS | Brasil | 3135100 | 31 | 33 | nan | nan | nan | Cerrado | 26.0 |
| 1d1d142d-766b-346a-87be-58774909992d | -13.30846 | -45.14329 | 2026-07-18 11:25:00 | TERRA_M-M | CORRENTINA | BAHIA | Brasil | 2909307 | 29 | 33 | nan | nan | nan | Cerrado | 12.5 |
| 6a83618c-1b08-31d6-9f71-08cd5ca2d633 | -20.75241 | -40.76854 | 2026-07-18 11:28:00 | TERRA_M-M | ANCHIETA | ESPÍRITO SANTO | Brasil | 3200409 | 32 | 33 | nan | nan | nan | Mata Atlântica | 6.9 |
| 138f954d-1205-34b0-a055-de63af1580f7 | -20.751 | -40.77968 | 2026-07-18 11:28:00 | TERRA_M-M | ANCHIETA | ESPÍRITO SANTO | Brasil | 3200409 | 32 | 33 | nan | nan | nan | Mata Atlântica | 6.9 |
| 6e387435-8999-369c-a35b-873b2e2b1fef | -28.22344 | -48.95847 | 2026-07-18 11:30:00 | TERRA_M-M | SÃO MARTINHO | SANTA CATARINA | Brasil | 4217105 | 42 | 33 | nan | nan | nan | Mata Atlântica | 13.4 |
| d937ff25-7a29-3634-bf6b-d9d2890feab3 | -9.9018 | -53.3942 | 2026-07-18 12:50:00 | GOES-19 | PEIXOTO DE AZEVEDO | MATO GROSSO | Brasil | 5106422 | 51 | 33 | nan | nan | nan | Amazônia | 86.0 |
| bd72bb8c-1d2f-3e50-8ff4-537b7bd3293d | -15.7203 | -43.369 | 2026-07-18 12:50:00 | GOES-19 | JANAÚBA | MINAS GERAIS | Brasil | 3135100 | 31 | 33 | nan | nan | nan | Cerrado | 107.2 |
| 2d2a1d74-c20e-3d8a-b378-1eec13b4f833 | -10.7101 | -46.5782 | 2026-07-18 12:50:00 | GOES-19 | MATEIROS | TOCANTINS | Brasil | 1712702 | 17 | 33 | nan | nan | nan | Cerrado | 119.6 |
| fbda4f13-ddb3-33a6-8d72-f36a5fba1f20 | -10.7101 | -46.5782 | 2026-07-18 13:00:00 | GOES-19 | MATEIROS | TOCANTINS | Brasil | 1712702 | 17 | 33 | nan | nan | nan | Cerrado | 69.7 |
| c949db2a-8bc0-3406-ba94-4f6f07b2fe06 | -15.7005 | -43.3732 | 2026-07-18 13:00:00 | GOES-19 | JANAÚBA | MINAS GERAIS | Brasil | 3135100 | 31 | 33 | nan | nan | nan | Cerrado | 97.5 |
| 1cc91a90-3faa-3d30-b10a-8b5008f89045 | -10.4718 | -42.4839 | 2026-07-18 13:10:00 | GOES-19 | XIQUE-XIQUE | BAHIA | Brasil | 2933604 | 29 | 33 | nan | nan | nan | Caatinga | 96.3 |
| 551eb7a2-a01f-3398-ace4-f0c417ae6091 | -10.7101 | -46.5782 | 2026-07-18 13:10:00 | GOES-19 | MATEIROS | TOCANTINS | Brasil | 1712702 | 17 | 33 | nan | nan | nan | Cerrado | 68.2 |


[Clique aqui para ver as próximas entradas](README17.md)
