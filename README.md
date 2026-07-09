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
| 20c19f90-c849-361c-81b0-872a72243740 | -12.9337 | -49.4744 | 2026-07-09 00:00:00 | GOES-19 | ARAGUAÇU | TOCANTINS | Brasil | 1702000 | 17 | 33 | nan | nan | nan | Cerrado | 57.3 |
| 2f7b587a-6503-3f26-92b4-a9bb57cbdd86 | -12.7741 | -44.5396 | 2026-07-09 00:00:00 | GOES-19 | BAIANÓPOLIS | BAHIA | Brasil | 2902500 | 29 | 33 | nan | nan | nan | Cerrado | 45.0 |
| 10cdde49-7778-3abc-8a96-75ea845dc574 | -14.9343 | -43.4113 | 2026-07-09 00:00:00 | GOES-19 | GAMELEIRAS | MINAS GERAIS | Brasil | 3127339 | 31 | 33 | nan | nan | nan | Caatinga | 59.9 |
| dea52210-1b0c-392c-86a2-e67fcde4d4dc | -12.7746 | -44.5162 | 2026-07-09 00:00:00 | GOES-19 | BAIANÓPOLIS | BAHIA | Brasil | 2902500 | 29 | 33 | nan | nan | nan | Cerrado | 67.6 |
| daacb0ab-dc31-3be5-905c-8dfd65878b91 | -8.7208 | -48.3441 | 2026-07-09 00:00:00 | GOES-19 | GUARAÍ | TOCANTINS | Brasil | 1709302 | 17 | 33 | nan | nan | nan | Cerrado | 51.7 |
| 89c49b39-ce91-3f21-83be-13cd9b6d0d5c | -9.0156 | -63.5223 | 2026-07-09 00:00:00 | GOES-19 | CANDEIAS DO JAMARI | RONDÔNIA | Brasil | 1100809 | 11 | 33 | nan | nan | nan | Amazônia | 41.0 |
| 996a44de-38b3-3d76-8a44-10a91e27e8e7 | -14.9338 | -43.4354 | 2026-07-09 00:00:00 | GOES-19 | GAMELEIRAS | MINAS GERAIS | Brasil | 3127339 | 31 | 33 | nan | nan | nan | Caatinga | 59.2 |
| 40ea4778-15e9-3670-83e8-64c0e3dba48c | -12.7548 | -44.5428 | 2026-07-09 00:00:00 | GOES-19 | BAIANÓPOLIS | BAHIA | Brasil | 2902500 | 29 | 33 | nan | nan | nan | Cerrado | 117.5 |
| 994187fe-d638-30ec-a867-1ac3586ced4d | -12.3561 | -47.413 | 2026-07-09 00:00:00 | GOES-19 | CONCEIÇÃO DO TOCANTINS | TOCANTINS | Brasil | 1705607 | 17 | 33 | nan | nan | nan | Cerrado | 75.4 |
| 7888de3f-897c-3c7c-9922-9238414cde27 | -4.3402 | -47.7645 | 2026-07-09 00:00:00 | GOES-19 | DOM ELISEU | PARÁ | Brasil | 1502939 | 15 | 33 | nan | nan | nan | Amazônia | 73.7 |
| e1e43aec-3914-3ded-a6fe-cd1b0dbd0aa5 | -14.9147 | -43.4152 | 2026-07-09 00:00:00 | GOES-19 | GAMELEIRAS | MINAS GERAIS | Brasil | 3127339 | 31 | 33 | nan | nan | nan | Caatinga | 96.4 |
| 4fe75a82-0c93-37bd-b963-4de12c74e355 | -9.0155 | -63.5411 | 2026-07-09 00:00:00 | GOES-19 | CANDEIAS DO JAMARI | RONDÔNIA | Brasil | 1100809 | 11 | 33 | nan | nan | nan | Amazônia | 86.2 |
| b16df15c-2209-31ff-9b9c-eb8cd0b03958 | -14.9141 | -43.4394 | 2026-07-09 00:00:00 | GOES-19 | GAMELEIRAS | MINAS GERAIS | Brasil | 3127339 | 31 | 33 | nan | nan | nan | Caatinga | 95.2 |
| 1f19a795-ab76-37dd-aa62-4f15642066fb | -12.7553 | -44.5194 | 2026-07-09 00:00:00 | GOES-19 | BAIANÓPOLIS | BAHIA | Brasil | 2902500 | 29 | 33 | nan | nan | nan | Cerrado | 180.5 |
| 902a743e-d315-339d-9716-3d8bafc120b5 | -5.6188 | -47.091499 | 2026-07-09 00:06:00 | METOP-B | BURITIRANA | MARANHÃO | Brasil | 2102358 | 21 | 33 | nan | nan | nan | Cerrado | nan |
| bb4e8480-c51e-32e9-91f1-46a18dc2cbf4 | -21.2036 | -49.195499 | 2026-07-09 00:06:00 | METOP-B | URUPÊS | SÃO PAULO | Brasil | 3556008 | 35 | 33 | nan | nan | nan | Mata Atlântica | nan |
| 1474a913-b04e-3453-a1a2-a91d7b0491ae | -13.3517 | -54.358002 | 2026-07-09 00:06:00 | METOP-B | PARANATINGA | MATO GROSSO | Brasil | 5106307 | 51 | 33 | nan | nan | nan | Amazônia | nan |
| 18d59e18-c7d2-33a1-bd1e-153c63352ccf | -13.2939 | -54.320801 | 2026-07-09 00:06:00 | METOP-B | PARANATINGA | MATO GROSSO | Brasil | 5106307 | 51 | 33 | nan | nan | nan | Amazônia | nan |
| d43712fe-8596-3320-9ce9-16423a794669 | -7.2836 | -46.2551 | 2026-07-09 00:06:00 | METOP-B | NOVA COLINAS | MARANHÃO | Brasil | 2107258 | 21 | 33 | nan | nan | nan | Cerrado | nan |
| e1e04f79-51b7-3710-802c-c9573d78d3f0 | -11.8394 | -48.227901 | 2026-07-09 00:06:00 | METOP-B | SÃO VALÉRIO | TOCANTINS | Brasil | 1720499 | 17 | 33 | nan | nan | nan | Cerrado | nan |
| e2131a16-c57c-33b4-8b22-52ebee99c5d3 | -8.7245 | -48.337002 | 2026-07-09 00:06:00 | METOP-B | GUARAÍ | TOCANTINS | Brasil | 1709302 | 17 | 33 | nan | nan | nan | Cerrado | nan |
| 7b7caeb8-efda-3078-9926-ba82368202a4 | -10.8514 | -45.036999 | 2026-07-09 00:06:00 | METOP-B | CRISTALÂNDIA DO PIAUÍ | PIAUÍ | Brasil | 2203008 | 22 | 33 | nan | nan | nan | Cerrado | nan |
| 917ddc3a-67db-35c7-9f48-fbb73d2d2f17 | -19.8179 | -43.118999 | 2026-07-09 00:06:00 | METOP-B | JOÃO MONLEVADE | MINAS GERAIS | Brasil | 3136207 | 31 | 33 | nan | nan | nan | Mata Atlântica | nan |
| c20421b5-34da-3f23-aeda-35963282e89a | -20.6625 | -50.095299 | 2026-07-09 00:06:00 | METOP-B | NHANDEARA | SÃO PAULO | Brasil | 3532603 | 35 | 33 | nan | nan | nan | Mata Atlântica | nan |
| 619331ad-6148-38a0-90c6-27b14fc633d4 | -12.3596 | -47.413601 | 2026-07-09 00:06:00 | METOP-B | CONCEIÇÃO DO TOCANTINS | TOCANTINS | Brasil | 1705607 | 17 | 33 | nan | nan | nan | Cerrado | nan |
| ddd601c4-2041-3499-85c6-fbcf05e99ad7 | -7.8993 | -48.239399 | 2026-07-09 00:06:00 | METOP-B | PALMEIRANTE | TOCANTINS | Brasil | 1715705 | 17 | 33 | nan | nan | nan | Cerrado | nan |
| d44c3edc-5d32-3d8f-8771-80a414c533dd | -12.1717 | -43.443401 | 2026-07-09 00:06:00 | METOP-B | MUQUÉM DO SÃO FRANCISCO | BAHIA | Brasil | 2922250 | 29 | 33 | nan | nan | nan | Cerrado | nan |
| 13b4520a-1218-353e-94d1-43576fe500f7 | -17.797701 | -43.8591 | 2026-07-09 00:06:00 | METOP-B | BUENÓPOLIS | MINAS GERAIS | Brasil | 3109204 | 31 | 33 | nan | nan | nan | Cerrado | nan |
| cb89ccef-d13f-329b-b5d4-20e2337ffbb6 | -22.922501 | -49.197201 | 2026-07-09 00:06:00 | METOP-B | ÁGUAS DE SANTA BÁRBARA | SÃO PAULO | Brasil | 3500550 | 35 | 33 | nan | nan | nan | Cerrado | nan |
| 59678b7a-f7b2-34c4-9336-810b195d8b91 | -8.7147 | -48.339199 | 2026-07-09 00:06:00 | METOP-B | GUARAÍ | TOCANTINS | Brasil | 1709302 | 17 | 33 | nan | nan | nan | Cerrado | nan |
| dce5db22-a61c-3e77-bd4b-ce3f19ade5a9 | 0.8807 | -59.676701 | 2026-07-09 00:06:00 | METOP-B | CAROEBE | RORAIMA | Brasil | 1400233 | 14 | 33 | nan | nan | nan | Amazônia | nan |
| 895daa8f-e455-33cf-ae3f-70828a8f6232 | -7.7119 | -45.161598 | 2026-07-09 00:06:00 | METOP-B | RIBEIRO GONÇALVES | PIAUÍ | Brasil | 2208908 | 22 | 33 | nan | nan | nan | Cerrado | nan |
| b9bb1bb4-664f-314b-9c20-3ecedfe0bf9d | -8.7214 | -48.3232 | 2026-07-09 00:06:00 | METOP-B | GUARAÍ | TOCANTINS | Brasil | 1709302 | 17 | 33 | nan | nan | nan | Cerrado | nan |
| 434457fc-3303-3536-96a1-e51c6aa7044c | -9.7998 | -48.916 | 2026-07-09 00:06:00 | METOP-B | BARROLÂNDIA | TOCANTINS | Brasil | 1703107 | 17 | 33 | nan | nan | nan | Cerrado | nan |
| ffdd7dcf-d063-37bd-99ef-9f04cb5165cf | -3.2996 | -49.044201 | 2026-07-09 00:06:00 | METOP-B | MOJU | PARÁ | Brasil | 1504703 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| 148fa288-772a-3e53-9921-921649f6beff | -8.8621 | -50.170898 | 2026-07-09 00:06:00 | METOP-B | SANTA MARIA DAS BARREIRAS | PARÁ | Brasil | 1506583 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| 5a42a12b-13d4-3506-b3ae-6cfc9ca09f84 | -15.8118 | -41.887699 | 2026-07-09 00:06:00 | METOP-B | TAIOBEIRAS | MINAS GERAIS | Brasil | 3168002 | 31 | 33 | nan | nan | nan | Cerrado | nan |
| d1a3bf90-4e97-3ac7-ad5c-de4d23d9d667 | -7.5383 | -46.016998 | 2026-07-09 00:06:00 | METOP-B | BALSAS | MARANHÃO | Brasil | 2101400 | 21 | 33 | nan | nan | nan | Cerrado | nan |
| 82730ac3-c00d-320a-8e82-8a4287b725a0 | -13.3486 | -54.3423 | 2026-07-09 00:06:00 | METOP-B | PARANATINGA | MATO GROSSO | Brasil | 5106307 | 51 | 33 | nan | nan | nan | Amazônia | nan |
| 12b829a0-b4ba-3ec8-88a3-584be770a81e | -8.3542 | -45.3951 | 2026-07-09 00:06:00 | METOP-B | RIBEIRO GONÇALVES | PIAUÍ | Brasil | 2208908 | 22 | 33 | nan | nan | nan | Cerrado | nan |
| 0863505b-40db-331d-a067-d99d4ec894dc | -9.3622 | -44.715 | 2026-07-09 00:06:00 | METOP-B | REDENÇÃO DO GURGUÉIA | PIAUÍ | Brasil | 2208700 | 22 | 33 | nan | nan | nan | Cerrado | nan |
| 8c146400-c8ec-3210-8002-f42f4b0781b4 | -7.2918 | -46.245499 | 2026-07-09 00:06:00 | METOP-B | NOVA COLINAS | MARANHÃO | Brasil | 2107258 | 21 | 33 | nan | nan | nan | Cerrado | nan |
| 7a4eb594-b63e-3f98-897d-7b353862597e | -10.6007 | -50.044601 | 2026-07-09 00:06:00 | METOP-B | LAGOA DA CONFUSÃO | TOCANTINS | Brasil | 1711902 | 17 | 33 | nan | nan | nan | Cerrado | nan |
| 05546462-e519-3b46-b339-c1ae8e2390cf | -6.673 | -47.509998 | 2026-07-09 00:06:00 | METOP-B | PALMEIRAS DO TOCANTINS | TOCANTINS | Brasil | 1713809 | 17 | 33 | nan | nan | nan | Cerrado | nan |
| 174a1a23-8f50-3789-a0f8-009b961c4f4e | -7.8258 | -49.294399 | 2026-07-09 00:06:00 | METOP-B | CONCEIÇÃO DO ARAGUAIA | PARÁ | Brasil | 1502707 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| 241ab08e-470c-39d0-87d9-536b6669a48b | -7.9008 | -48.2463 | 2026-07-09 00:06:00 | METOP-B | PALMEIRANTE | TOCANTINS | Brasil | 1715705 | 17 | 33 | nan | nan | nan | Cerrado | nan |
| d5f70fee-d553-362f-85d9-158a57ccffad | -8.7132 | -48.332298 | 2026-07-09 00:06:00 | METOP-B | GUARAÍ | TOCANTINS | Brasil | 1709302 | 17 | 33 | nan | nan | nan | Cerrado | nan |
| 7692d94c-8522-3972-a9fc-465284dea675 | -17.589001 | -46.675098 | 2026-07-09 00:06:00 | METOP-B | VAZANTE | MINAS GERAIS | Brasil | 3171006 | 31 | 33 | nan | nan | nan | Cerrado | nan |
| 788f8e8b-b885-3163-855c-0c6afb02c565 | -8.9599 | -48.008202 | 2026-07-09 00:06:00 | METOP-B | BOM JESUS DO TOCANTINS | TOCANTINS | Brasil | 1703305 | 17 | 33 | nan | nan | nan | Cerrado | nan |
| 4b3a7e54-5c71-37bb-92c8-dba5dfa26202 | -22.644899 | -47.950401 | 2026-07-09 00:06:00 | METOP-B | SÃO PEDRO | SÃO PAULO | Brasil | 3550407 | 35 | 33 | nan | nan | nan | Cerrado | nan |
| bc1bb422-a6e5-36f4-81f3-361f62ce73a5 | -10.4783 | -50.238602 | 2026-07-09 00:06:00 | METOP-B | PIUM | TOCANTINS | Brasil | 1717503 | 17 | 33 | nan | nan | nan | Cerrado | nan |
| c38dd89c-274e-3a7c-8d72-1be6d53038cf | -10.9729 | -44.671398 | 2026-07-09 00:06:00 | METOP-B | SANTA RITA DE CÁSSIA | BAHIA | Brasil | 2928406 | 29 | 33 | nan | nan | nan | Cerrado | nan |
| 2225d716-a3b1-363f-a255-7010e4521d5f | -7.7398 | -49.463001 | 2026-07-09 00:06:00 | METOP-B | FLORESTA DO ARAGUAIA | PARÁ | Brasil | 1503044 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| ac0e1716-0cd3-3771-9676-4dcb593ee686 | -13.2774 | -45.172798 | 2026-07-09 00:06:00 | METOP-B | CORRENTINA | BAHIA | Brasil | 2909307 | 29 | 33 | nan | nan | nan | Cerrado | nan |
| f94cd705-fc23-35e3-9f99-5b2f82ef775a | -22.6467 | -47.9594 | 2026-07-09 00:06:00 | METOP-B | SÃO PEDRO | SÃO PAULO | Brasil | 3550407 | 35 | 33 | nan | nan | nan | Cerrado | nan |
| 0f8bb2e0-e992-3b9c-9a9c-13df3dbfe1ff | -9.3377 | -47.901299 | 2026-07-09 00:06:00 | METOP-B | PEDRO AFONSO | TOCANTINS | Brasil | 1716505 | 17 | 33 | nan | nan | nan | Cerrado | nan |
| 1a63a7c4-fcab-3b03-b7e3-a272bb6f269e | -15.1082 | -43.978699 | 2026-07-09 00:06:00 | METOP-B | JAÍBA | MINAS GERAIS | Brasil | 3135050 | 31 | 33 | nan | nan | nan | Cerrado | nan |
| 06b3bbd1-5b00-3869-87d0-74f6c0a535de | 0.8858 | -59.6548 | 2026-07-09 00:06:00 | METOP-B | CAROEBE | RORAIMA | Brasil | 1400233 | 14 | 33 | nan | nan | nan | Amazônia | nan |
| 3a704e72-c79d-34d3-a2fd-6523ef6b84eb | -7.6367 | -50.020199 | 2026-07-09 00:06:00 | METOP-B | RIO MARIA | PARÁ | Brasil | 1506161 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| 4ec67d2e-774c-3a04-b301-99cb6b5e9f88 | -8.3705 | -48.227699 | 2026-07-09 00:06:00 | METOP-B | TUPIRATINS | TOCANTINS | Brasil | 1721307 | 17 | 33 | nan | nan | nan | Cerrado | nan |
| 1ee980a8-1bdc-37f0-b502-bd3a0868701e | -7.282 | -46.2477 | 2026-07-09 00:06:00 | METOP-B | NOVA COLINAS | MARANHÃO | Brasil | 2107258 | 21 | 33 | nan | nan | nan | Cerrado | nan |
| 6ffa9e09-9c80-315d-98f3-204eaf3a2bf9 | -10.7544 | -45.019402 | 2026-07-09 00:06:00 | METOP-B | CRISTALÂNDIA DO PIAUÍ | PIAUÍ | Brasil | 2203008 | 22 | 33 | nan | nan | nan | Cerrado | nan |
| 7db8b34c-9295-3659-8800-9c353f68c00d | -22.2927 | -46.844501 | 2026-07-09 00:06:00 | METOP-B | MOGI GUAÇU | SÃO PAULO | Brasil | 3530706 | 35 | 33 | nan | nan | nan | Cerrado | nan |
| 4ac22448-c0d1-352c-bf91-7eca77eaf03c | -8.3426 | -45.389599 | 2026-07-09 00:06:00 | METOP-B | BAIXA GRANDE DO RIBEIRO | PIAUÍ | Brasil | 2201150 | 22 | 33 | nan | nan | nan | Cerrado | nan |
| 328fdcb8-56c7-32c4-a4ed-c51f21740f00 | -8.7297 | -48.313999 | 2026-07-09 00:06:00 | METOP-B | GUARAÍ | TOCANTINS | Brasil | 1709302 | 17 | 33 | nan | nan | nan | Cerrado | nan |
| ac9578a1-7ae4-3df0-8670-3d437ba78c16 | -7.5366 | -46.009499 | 2026-07-09 00:06:00 | METOP-B | BALSAS | MARANHÃO | Brasil | 2101400 | 21 | 33 | nan | nan | nan | Cerrado | nan |
| 56745885-5575-30bb-b407-921fc4951c42 | -3.1984 | -49.052399 | 2026-07-09 00:06:00 | METOP-B | MOJU | PARÁ | Brasil | 1504703 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| 21e5252d-caa6-3354-b2ae-f094901d8668 | -14.9065 | -43.425499 | 2026-07-09 00:06:00 | METOP-B | GAMELEIRAS | MINAS GERAIS | Brasil | 3127339 | 31 | 33 | nan | nan | nan | Caatinga | nan |
| 025b608e-38da-3a8d-9c05-a307a48af8f2 | -9.2349 | -50.137901 | 2026-07-09 00:06:00 | METOP-B | SANTANA DO ARAGUAIA | PARÁ | Brasil | 1506708 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| e3cb4e54-6516-3c17-adcb-59a8ee35422f | -8.9615 | -48.015099 | 2026-07-09 00:06:00 | METOP-B | BOM JESUS DO TOCANTINS | TOCANTINS | Brasil | 1703305 | 17 | 33 | nan | nan | nan | Cerrado | nan |
| 14c5c0e1-e026-36d6-aa67-afd076a77a8d | -9.5718 | -49.094898 | 2026-07-09 00:06:00 | METOP-B | DOIS IRMÃOS DO TOCANTINS | TOCANTINS | Brasil | 1707207 | 17 | 33 | nan | nan | nan | Cerrado | nan |
| 3e21b52e-e99d-37bf-8745-964acab50739 | -6.5837 | -51.681 | 2026-07-09 00:06:00 | METOP-B | SÃO FÉLIX DO XINGU | PARÁ | Brasil | 1507300 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| 8d35ed2f-ea4c-3fe9-aae6-14d6d57ecde5 | -5.6205 | -47.098598 | 2026-07-09 00:06:00 | METOP-B | BURITIRANA | MARANHÃO | Brasil | 2102358 | 21 | 33 | nan | nan | nan | Cerrado | nan |
| 617e91ea-ed55-3743-bd61-b090fd5d627b | -12.7528 | -44.510201 | 2026-07-09 00:06:00 | METOP-B | BAIANÓPOLIS | BAHIA | Brasil | 2902500 | 29 | 33 | nan | nan | nan | Cerrado | nan |
| b702abfa-6193-3549-be13-bc55a1a3dfd0 | -12.9311 | -49.476898 | 2026-07-09 00:06:00 | METOP-B | ARAGUAÇU | TOCANTINS | Brasil | 1702000 | 17 | 33 | nan | nan | nan | Cerrado | nan |
| c362311c-0703-360e-891d-91393de5842e | -23.5662 | -47.493099 | 2026-07-09 00:06:00 | METOP-B | SOROCABA | SÃO PAULO | Brasil | 3552205 | 35 | 33 | nan | nan | nan | Mata Atlântica | nan |
| f32931f6-8559-3435-a871-a7c026fab1d2 | -11.8409 | -48.235001 | 2026-07-09 00:06:00 | METOP-B | SÃO VALÉRIO | TOCANTINS | Brasil | 1720499 | 17 | 33 | nan | nan | nan | Cerrado | nan |
| 8e5c9787-333f-3592-bad9-28592e3c8b18 | -4.3475 | -47.7561 | 2026-07-09 00:06:00 | METOP-B | DOM ELISEU | PARÁ | Brasil | 1502939 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| 044b2d30-16e3-3bc3-9523-d369a9120fdb | -10.0136 | -48.5326 | 2026-07-09 00:06:00 | METOP-B | MIRACEMA DO TOCANTINS | TOCANTINS | Brasil | 1713205 | 17 | 33 | nan | nan | nan | Cerrado | nan |
| 739b9fbe-03f3-36c4-a228-25447fe20578 | -23.5679 | -47.5019 | 2026-07-09 00:06:00 | METOP-B | SOROCABA | SÃO PAULO | Brasil | 3552205 | 35 | 33 | nan | nan | nan | Mata Atlântica | nan |
| 95c1f18a-1d45-3556-a6a0-2c6210b628b5 | -3.3358 | -49.021801 | 2026-07-09 00:06:00 | METOP-B | MOJU | PARÁ | Brasil | 1504703 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| b4d853ba-cedc-3b1a-9b03-03636743a8e3 | -10.8496 | -45.029301 | 2026-07-09 00:06:00 | METOP-B | CRISTALÂNDIA DO PIAUÍ | PIAUÍ | Brasil | 2203008 | 22 | 33 | nan | nan | nan | Cerrado | nan |
| 18042bf5-c796-32fb-bd18-7ec8b878ac08 | -12.7546 | -44.518002 | 2026-07-09 00:06:00 | METOP-B | BAIANÓPOLIS | BAHIA | Brasil | 2902500 | 29 | 33 | nan | nan | nan | Cerrado | nan |
| 3b8aa075-c84a-3423-a583-2015496102b0 | -12.3581 | -47.406601 | 2026-07-09 00:06:00 | METOP-B | CONCEIÇÃO DO TOCANTINS | TOCANTINS | Brasil | 1705607 | 17 | 33 | nan | nan | nan | Cerrado | nan |
| 601a2677-5f94-3d6f-a8dc-4c9f42b041ae | -22.294399 | -46.8526 | 2026-07-09 00:06:00 | METOP-B | MOGI GUAÇU | SÃO PAULO | Brasil | 3530706 | 35 | 33 | nan | nan | nan | Cerrado | nan |
| b98dafd6-5112-3e7a-82c9-a8ab500deda7 | -13.3104 | -43.714199 | 2026-07-09 00:06:00 | METOP-B | SERRA DO RAMALHO | BAHIA | Brasil | 2930154 | 29 | 33 | nan | nan | nan | Cerrado | nan |
| 1cd92b49-ff01-30ea-85f8-8bfb6a32b997 | -12.9294 | -49.468899 | 2026-07-09 00:06:00 | METOP-B | ARAGUAÇU | TOCANTINS | Brasil | 1702000 | 17 | 33 | nan | nan | nan | Cerrado | nan |
| 9c61cedf-1c58-3a94-ad50-6ed6ea5c55e5 | -8.723 | -48.330101 | 2026-07-09 00:06:00 | METOP-B | GUARAÍ | TOCANTINS | Brasil | 1709302 | 17 | 33 | nan | nan | nan | Cerrado | nan |
| 746d8da0-5c7b-392a-ae65-def12e694166 | -4.3459 | -47.7491 | 2026-07-09 00:06:00 | METOP-B | DOM ELISEU | PARÁ | Brasil | 1502939 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| 84a55a09-94b7-3af6-a669-a023812e2c4a | -10.8651 | -47.592098 | 2026-07-09 00:06:00 | METOP-B | PONTE ALTA DO TOCANTINS | TOCANTINS | Brasil | 1717909 | 17 | 33 | nan | nan | nan | Cerrado | nan |
| 2a01740c-00f3-368b-b2eb-7f6674805581 | -6.6746 | -47.516899 | 2026-07-09 00:06:00 | METOP-B | PALMEIRAS DO TOCANTINS | TOCANTINS | Brasil | 1713809 | 17 | 33 | nan | nan | nan | Cerrado | nan |
| 6978bacc-216b-32b3-8ca3-6110ba72c24c | -21.2054 | -49.205299 | 2026-07-09 00:06:00 | METOP-B | URUPÊS | SÃO PAULO | Brasil | 3556008 | 35 | 33 | nan | nan | nan | Mata Atlântica | nan |
| 002cf8e0-8f0c-39cb-b574-cb4c1c0d8a3b | -14.9045 | -43.417198 | 2026-07-09 00:06:00 | METOP-B | GAMELEIRAS | MINAS GERAIS | Brasil | 3127339 | 31 | 33 | nan | nan | nan | Caatinga | nan |
| a67a55d4-5309-3b72-87f4-8fc5c218ccd9 | -8.9584 | -48.001301 | 2026-07-09 00:06:00 | METOP-B | BOM JESUS DO TOCANTINS | TOCANTINS | Brasil | 1703305 | 17 | 33 | nan | nan | nan | Cerrado | nan |
| 9a13bd8c-689c-333e-be12-27e8839e360d | -17.5875 | -46.6679 | 2026-07-09 00:06:00 | METOP-B | VAZANTE | MINAS GERAIS | Brasil | 3171006 | 31 | 33 | nan | nan | nan | Cerrado | nan |
| 2ca37fdf-77a8-313f-a8bb-6d88ad15260b | -6.7407 | -47.127499 | 2026-07-09 00:06:00 | METOP-B | ESTREITO | MARANHÃO | Brasil | 2104057 | 21 | 33 | nan | nan | nan | Cerrado | nan |
| 68d3d011-7903-368f-8165-d83658a7e856 | -13.3065 | -43.697601 | 2026-07-09 00:06:00 | METOP-B | SERRA DO RAMALHO | BAHIA | Brasil | 2930154 | 29 | 33 | nan | nan | nan | Cerrado | nan |
| 1c82ffbc-e55f-320d-bb87-e0a13d1c0e67 | -7.829 | -49.308601 | 2026-07-09 00:06:00 | METOP-B | CONCEIÇÃO DO ARAGUAIA | PARÁ | Brasil | 1502707 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| efad6dac-95fc-3b5a-a64d-bcdddd7536a5 | -13.3084 | -43.705898 | 2026-07-09 00:06:00 | METOP-B | SERRA DO RAMALHO | BAHIA | Brasil | 2930154 | 29 | 33 | nan | nan | nan | Cerrado | nan |
| ce76d2da-a972-302a-b7bd-028189e62e0a | -7.6351 | -50.012798 | 2026-07-09 00:06:00 | METOP-B | RIO MARIA | PARÁ | Brasil | 1506161 | 15 | 33 | nan | nan | nan | Amazônia | nan |


[Clique aqui para ver as próximas entradas](README2.md)
