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

## Dados Diários - Página 8

| ID | Latitude | Longitude | Data/Hora GMT | Satélite | Município | Estado | País | Município ID | Estado ID | País ID | Dias sem Chuva | Precipitação | Risco de Fogo | Bioma | FRP |
|----|----------|-----------|---------------|----------|-----------|--------|------|--------------|-----------|---------|----------------|--------------|----------------|-------|-----|
| 6510c9f6-9002-3818-b694-203c210fa67d | -2.8014 | -53.0227 | 2024-11-26 01:10:00 | GOES-16 | MEDICILÂNDIA | PARÁ | Brasil | 1504455 | 15 | 33 | nan | nan | nan | Amazônia | 124.6 |
| a6098e5a-775a-323b-a528-885afc452560 | -6.0676 | -48.0352 | 2024-11-26 01:10:00 | GOES-16 | SÃO BENTO DO TOCANTINS | TOCANTINS | Brasil | 1720101 | 17 | 33 | nan | nan | nan | Cerrado | 77.4 |
| ccf27a5e-d0ab-33b0-9b44-9b1a26e29ee2 | -3.5856 | -50.3997 | 2024-11-26 01:10:00 | GOES-16 | PACAJÁ | PARÁ | Brasil | 1505486 | 15 | 33 | nan | nan | nan | Amazônia | 107.7 |
| d2a67c42-c803-38f8-bf82-191292fa0413 | -2.8014 | -53.0024 | 2024-11-26 01:10:00 | GOES-16 | MEDICILÂNDIA | PARÁ | Brasil | 1504455 | 15 | 33 | nan | nan | nan | Amazônia | 68.6 |
| 2569596c-fae5-3105-b1f9-d819b5374495 | -3.5857 | -50.3787 | 2024-11-26 01:10:00 | GOES-16 | PACAJÁ | PARÁ | Brasil | 1505486 | 15 | 33 | nan | nan | nan | Amazônia | 172.4 |
| 663b86c8-8421-3803-89c0-6c6441332f28 | -3.1691 | -48.4394 | 2024-11-26 01:10:00 | GOES-16 | TOMÉ-AÇU | PARÁ | Brasil | 1508001 | 15 | 33 | nan | nan | nan | Amazônia | 58.0 |
| 09c0985c-160a-392b-8723-8e904bbecee0 | -2.8198 | -53.0222 | 2024-11-26 01:10:00 | GOES-16 | MEDICILÂNDIA | PARÁ | Brasil | 1504455 | 15 | 33 | nan | nan | nan | Amazônia | 78.7 |
| ee62e74f-6991-3ce8-a16c-85ef74fb9933 | -3.6042 | -50.3781 | 2024-11-26 01:10:00 | GOES-16 | PACAJÁ | PARÁ | Brasil | 1505486 | 15 | 33 | nan | nan | nan | Amazônia | 274.9 |
| 86c4c0e9-ed86-35e3-97dd-c045e5f1777f | -2.5319 | -45.6086 | 2024-11-26 01:10:00 | GOES-16 | SANTA LUZIA DO PARUÁ | MARANHÃO | Brasil | 2110039 | 21 | 33 | nan | nan | nan | Amazônia | 34.0 |
| e9497a48-4033-3d7c-966a-5937f6313e8d | -3.2603 | -53.2949 | 2024-11-26 01:10:00 | GOES-16 | MEDICILÂNDIA | PARÁ | Brasil | 1504455 | 15 | 33 | nan | nan | nan | Amazônia | 68.4 |
| daab4eba-a197-3253-9693-6bf4ca2de462 | -4.6733 | -47.9434 | 2024-11-26 01:10:00 | GOES-16 | RONDON DO PARÁ | PARÁ | Brasil | 1506187 | 15 | 33 | nan | nan | nan | Amazônia | 64.7 |
| 9e5c2442-8bd3-34aa-8bdb-a2d11492f05e | -3.5858 | -50.3577 | 2024-11-26 01:10:00 | GOES-16 | PACAJÁ | PARÁ | Brasil | 1505486 | 15 | 33 | nan | nan | nan | Amazônia | 51.9 |
| baca3cd7-2edf-3f1e-b5d8-dd1286502195 | 2.6901 | -60.4301 | 2024-11-26 01:10:00 | GOES-16 | CANTÁ | RORAIMA | Brasil | 1400175 | 14 | 33 | nan | nan | nan | Amazônia | 55.9 |
| ccf0c857-1bff-30ef-9f8f-68ea413b64ce | -3.6043 | -50.3571 | 2024-11-26 01:10:00 | GOES-16 | PACAJÁ | PARÁ | Brasil | 1505486 | 15 | 33 | nan | nan | nan | Amazônia | 65.5 |
| 565569be-f0ba-373e-a91d-c976829c13bc | -3.9267 | -42.401 | 2024-11-26 01:10:00 | GOES-16 | CAMPO LARGO DO PIAUÍ | PIAUÍ | Brasil | 2202174 | 22 | 33 | nan | nan | nan | Caatinga | 51.6 |
| 32ff3608-5e28-3f45-b6a1-be86c2e68267 | -4.6547 | -47.9444 | 2024-11-26 01:10:00 | GOES-16 | RONDON DO PARÁ | PARÁ | Brasil | 1506187 | 15 | 33 | nan | nan | nan | Amazônia | 73.5 |
| ded76f5f-611d-37c5-8edf-972efd146292 | -3.9265 | -42.4246 | 2024-11-26 01:10:00 | GOES-16 | CAMPO LARGO DO PIAUÍ | PIAUÍ | Brasil | 2202174 | 22 | 33 | nan | nan | nan | Caatinga | 72.4 |
| 430cb4d6-453e-3eb8-abb2-41c7142c3a2f | -2.783 | -53.0231 | 2024-11-26 01:10:00 | GOES-16 | MEDICILÂNDIA | PARÁ | Brasil | 1504455 | 15 | 33 | nan | nan | nan | Amazônia | 60.8 |
| 4f00f24a-16df-38ef-865c-59b5db51c531 | -2.8017 | -52.921 | 2024-11-26 01:10:00 | GOES-16 | MEDICILÂNDIA | PARÁ | Brasil | 1504455 | 15 | 33 | nan | nan | nan | Amazônia | 53.2 |
| 3dd55dc4-98ae-3d35-b56a-20afce004423 | -3.3938 | -44.1722 | 2024-11-26 01:10:00 | GOES-16 | ITAPECURU MIRIM | MARANHÃO | Brasil | 2105401 | 21 | 33 | nan | nan | nan | Cerrado | 114.3 |
| a6d28bab-a27c-37db-a4b1-a4c89bcf03e4 | -3.9078 | -42.4256 | 2024-11-26 01:20:00 | GOES-16 | CAMPO LARGO DO PIAUÍ | PIAUÍ | Brasil | 2202174 | 22 | 33 | nan | nan | nan | Caatinga | 66.0 |
| 1abbab67-7727-3e62-b91c-63c12f59fb05 | -4.6547 | -47.9444 | 2024-11-26 01:20:00 | GOES-16 | RONDON DO PARÁ | PARÁ | Brasil | 1506187 | 15 | 33 | nan | nan | nan | Amazônia | 59.9 |
| 7fa0ab8f-8197-3b14-a6c0-fe16bb52ee55 | -6.0676 | -48.0352 | 2024-11-26 01:20:00 | GOES-16 | SÃO BENTO DO TOCANTINS | TOCANTINS | Brasil | 1720101 | 17 | 33 | nan | nan | nan | Cerrado | 65.0 |
| 88a9bea5-a70a-3ac7-8a80-afba8781bb34 | -2.783 | -53.0231 | 2024-11-26 01:20:00 | GOES-16 | MEDICILÂNDIA | PARÁ | Brasil | 1504455 | 15 | 33 | nan | nan | nan | Amazônia | 53.1 |
| 41dbdc22-1ebe-3c12-857e-f08ec60a7676 | 2.6901 | -60.4301 | 2024-11-26 01:20:00 | GOES-16 | CANTÁ | RORAIMA | Brasil | 1400175 | 14 | 33 | nan | nan | nan | Amazônia | 56.3 |
| c979531c-682b-3437-9aa1-0352d57082f6 | -3.5856 | -50.3997 | 2024-11-26 01:20:00 | GOES-16 | PACAJÁ | PARÁ | Brasil | 1505486 | 15 | 33 | nan | nan | nan | Amazônia | 93.5 |
| 4fd50169-1ebe-3bd8-8be1-d071fac2fa63 | -2.8013 | -53.043 | 2024-11-26 01:20:00 | GOES-16 | MEDICILÂNDIA | PARÁ | Brasil | 1504455 | 15 | 33 | nan | nan | nan | Amazônia | 54.8 |
| 642ea210-72fa-31a3-aaf7-9ccac6c76d68 | -3.6042 | -50.3781 | 2024-11-26 01:20:00 | GOES-16 | PACAJÁ | PARÁ | Brasil | 1505486 | 15 | 33 | nan | nan | nan | Amazônia | 178.7 |
| 8d7be4e1-f42f-3d2c-858f-34fe0cf8b03e | -3.1876 | -48.4387 | 2024-11-26 01:20:00 | GOES-16 | TOMÉ-AÇU | PARÁ | Brasil | 1508001 | 15 | 33 | nan | nan | nan | Amazônia | 221.1 |
| 7609faf4-12a9-3f59-b737-c2bf1bb81dee | -2.5319 | -45.6086 | 2024-11-26 01:20:00 | GOES-16 | SANTA LUZIA DO PARUÁ | MARANHÃO | Brasil | 2110039 | 21 | 33 | nan | nan | nan | Amazônia | 44.9 |
| 2aa68ef6-d777-3dda-a4ec-81097a982b7e | -3.3938 | -44.1722 | 2024-11-26 01:20:00 | GOES-16 | ITAPECURU MIRIM | MARANHÃO | Brasil | 2105401 | 21 | 33 | nan | nan | nan | Cerrado | 144.9 |
| 2114d08f-7b55-3eb5-b026-9577d6b161b7 | -3.1691 | -48.4394 | 2024-11-26 01:20:00 | GOES-16 | TOMÉ-AÇU | PARÁ | Brasil | 1508001 | 15 | 33 | nan | nan | nan | Amazônia | 134.7 |
| b3016218-4851-3633-84ab-d34fd923faa4 | -3.2061 | -48.4381 | 2024-11-26 01:20:00 | GOES-16 | TOMÉ-AÇU | PARÁ | Brasil | 1508001 | 15 | 33 | nan | nan | nan | Amazônia | 61.6 |
| d00799ab-f1bc-3a1d-aabe-865d9710ae9f | -3.9265 | -42.4246 | 2024-11-26 01:20:00 | GOES-16 | CAMPO LARGO DO PIAUÍ | PIAUÍ | Brasil | 2202174 | 22 | 33 | nan | nan | nan | Caatinga | 45.0 |
| cb8c08a5-e570-320c-a95f-aacd76100f2a | -2.532 | -45.5862 | 2024-11-26 01:20:00 | GOES-16 | SANTA LUZIA DO PARUÁ | MARANHÃO | Brasil | 2110039 | 21 | 33 | nan | nan | nan | Amazônia | 38.7 |
| 7864908b-4923-3c17-aece-4704cb624fe7 | -3.2419 | -53.2954 | 2024-11-26 01:20:00 | GOES-16 | MEDICILÂNDIA | PARÁ | Brasil | 1504455 | 15 | 33 | nan | nan | nan | Amazônia | 51.6 |
| 42b03701-056a-3c5d-a7d3-83b61e632e8e | -2.8198 | -53.0222 | 2024-11-26 01:20:00 | GOES-16 | MEDICILÂNDIA | PARÁ | Brasil | 1504455 | 15 | 33 | nan | nan | nan | Amazônia | 69.7 |
| 4923f00a-e92a-36ea-b2b1-173d3ef61d38 | -2.8014 | -53.0024 | 2024-11-26 01:20:00 | GOES-16 | MEDICILÂNDIA | PARÁ | Brasil | 1504455 | 15 | 33 | nan | nan | nan | Amazônia | 63.0 |
| 4eb94d61-6d90-3a0d-b3ec-a7d0c049d6b3 | -3.3937 | -44.1951 | 2024-11-26 01:20:00 | GOES-16 | ITAPECURU MIRIM | MARANHÃO | Brasil | 2105401 | 21 | 33 | nan | nan | nan | Cerrado | 46.3 |
| 68e697fb-ea5e-3313-8e4f-5b303c6f1b83 | -3.908 | -42.402 | 2024-11-26 01:20:00 | GOES-16 | CAMPO LARGO DO PIAUÍ | PIAUÍ | Brasil | 2202174 | 22 | 33 | nan | nan | nan | Caatinga | 40.5 |
| 03a8281c-ffde-3e79-bf21-21c421ae80dc | -3.5857 | -50.3787 | 2024-11-26 01:20:00 | GOES-16 | PACAJÁ | PARÁ | Brasil | 1505486 | 15 | 33 | nan | nan | nan | Amazônia | 174.5 |
| e4bfe3e1-6658-3c73-b11f-cbb507b8ec36 | -6.0862 | -48.0339 | 2024-11-26 01:20:00 | GOES-16 | SÃO BENTO DO TOCANTINS | TOCANTINS | Brasil | 1720101 | 17 | 33 | nan | nan | nan | Cerrado | 65.7 |
| 00c7dd94-f7eb-3866-be1f-07884283af49 | -2.8017 | -52.921 | 2024-11-26 01:20:00 | GOES-16 | MEDICILÂNDIA | PARÁ | Brasil | 1504455 | 15 | 33 | nan | nan | nan | Amazônia | 51.0 |
| fcd88ab8-2f9b-3739-b633-2f7b61a27982 | -3.8691 | -49.1415 | 2024-11-26 01:20:00 | GOES-16 | GOIANÉSIA DO PARÁ | PARÁ | Brasil | 1503093 | 15 | 33 | nan | nan | nan | Amazônia | 93.6 |
| f9c38da4-1d3e-3ce3-8412-a10ae3648991 | -3.1877 | -48.4172 | 2024-11-26 01:20:00 | GOES-16 | TOMÉ-AÇU | PARÁ | Brasil | 1508001 | 15 | 33 | nan | nan | nan | Amazônia | 95.3 |
| a6989e8e-a84a-3390-8bc3-683a692b9799 | -3.1692 | -48.4179 | 2024-11-26 01:20:00 | GOES-16 | TOMÉ-AÇU | PARÁ | Brasil | 1508001 | 15 | 33 | nan | nan | nan | Amazônia | 61.2 |
| 916f7cb8-85fc-3ded-a4d0-2f312049c6b3 | -3.1875 | -48.4603 | 2024-11-26 01:20:00 | GOES-16 | TOMÉ-AÇU | PARÁ | Brasil | 1508001 | 15 | 33 | nan | nan | nan | Amazônia | 52.5 |
| 9b02e72b-43f4-3e0f-9ea6-102348ab8538 | -3.6041 | -50.3991 | 2024-11-26 01:20:00 | GOES-16 | PACAJÁ | PARÁ | Brasil | 1505486 | 15 | 33 | nan | nan | nan | Amazônia | 91.8 |
| 76cd299b-dac5-38ec-88bf-28c2a9e8fc82 | -17.6453 | -57.5874 | 2024-11-26 01:20:00 | GOES-16 | POCONÉ | MATO GROSSO | Brasil | 5106505 | 51 | 33 | nan | nan | nan | Pantanal | 71.0 |
| 032a2fc3-ac7c-3048-9593-b6f38469d36d | -3.8506 | -49.1422 | 2024-11-26 01:20:00 | GOES-16 | BREU BRANCO | PARÁ | Brasil | 1501782 | 15 | 33 | nan | nan | nan | Amazônia | 87.4 |
| a391b4ab-b1c2-3a2b-bbfb-aed1292fb87b | -2.8014 | -53.0227 | 2024-11-26 01:20:00 | GOES-16 | MEDICILÂNDIA | PARÁ | Brasil | 1504455 | 15 | 33 | nan | nan | nan | Amazônia | 110.2 |
| e24adb44-362d-3ee8-b4b4-5e2e9fe5de80 | -17.6381 | -57.5821 | 2024-11-26 01:20:00 | METOP-B | POCONÉ | MATO GROSSO | Brasil | 5106505 | 51 | 33 | nan | nan | nan | Pantanal | nan |
| 0cff8799-3e36-356e-80b9-0561e1864725 | -16.087 | -60.101398 | 2024-11-26 01:20:00 | METOP-B | VILA BELA DA SANTÍSSIMA TRINDADE | MATO GROSSO | Brasil | 5105507 | 51 | 33 | nan | nan | nan | Amazônia | nan |
| 62a54776-ec75-3f5b-8bf3-ff76fe401b4b | -17.6479 | -57.579601 | 2024-11-26 01:20:00 | METOP-B | POCONÉ | MATO GROSSO | Brasil | 5106505 | 51 | 33 | nan | nan | nan | Pantanal | nan |
| de04dbbd-114b-39d6-afb6-f17287b14e94 | -10.126 | -65.017197 | 2024-11-26 01:20:00 | METOP-B | NOVA MAMORÉ | RONDÔNIA | Brasil | 1100338 | 11 | 33 | nan | nan | nan | Amazônia | nan |
| 15d070ad-dc24-32a1-adbf-826deddb2852 | -10.1242 | -65.009102 | 2024-11-26 01:20:00 | METOP-B | NOVA MAMORÉ | RONDÔNIA | Brasil | 1100338 | 11 | 33 | nan | nan | nan | Amazônia | nan |
| 4b2ea8f3-0aaa-3538-b252-3ae8dc4e9c13 | -9.9292 | -59.922199 | 2024-11-26 01:20:00 | METOP-B | ARIPUANÃ | MATO GROSSO | Brasil | 5101407 | 51 | 33 | nan | nan | nan | Amazônia | nan |
| cf8d2001-7e9b-3425-b5ad-e49f6a3be8c7 | -17.6362 | -57.573898 | 2024-11-26 01:20:00 | METOP-B | POCONÉ | MATO GROSSO | Brasil | 5106505 | 51 | 33 | nan | nan | nan | Pantanal | nan |
| a054f526-309e-3f4c-80ab-0c212b863496 | -16.0854 | -60.0942 | 2024-11-26 01:20:00 | METOP-B | VILA BELA DA SANTÍSSIMA TRINDADE | MATO GROSSO | Brasil | 5105507 | 51 | 33 | nan | nan | nan | Amazônia | nan |
| bd842558-1ade-39f0-942b-208fd3440366 | -17.6499 | -57.587799 | 2024-11-26 01:20:00 | METOP-B | POCONÉ | MATO GROSSO | Brasil | 5106505 | 51 | 33 | nan | nan | nan | Pantanal | nan |
| 8f7851c0-530b-32a7-9204-a2047e93fc94 | -17.646 | -57.5714 | 2024-11-26 01:20:00 | METOP-B | POCONÉ | MATO GROSSO | Brasil | 5106505 | 51 | 33 | nan | nan | nan | Pantanal | nan |
| 6ca7321c-06a3-3e11-a5ef-982136da0758 | -21.566401 | -54.192402 | 2024-11-26 01:20:00 | METOP-B | NOVA ALVORADA DO SUL | MATO GROSSO DO SUL | Brasil | 5006002 | 50 | 33 | nan | nan | nan | Cerrado | nan |
| 5e332609-d9c7-31fc-a614-8b99a29b9a91 | 2.686 | -60.425098 | 2024-11-26 01:22:00 | METOP-B | CANTÁ | RORAIMA | Brasil | 1400175 | 14 | 33 | nan | nan | nan | Amazônia | nan |
| 3306aebc-95e4-3c0e-9bbe-7020467bf2bf | 3.669 | -60.388199 | 2024-11-26 01:22:00 | METOP-B | NORMANDIA | RORAIMA | Brasil | 1400407 | 14 | 33 | nan | nan | nan | Amazônia | nan |
| 8a3772b9-a052-3204-a1be-f13fa3f422c9 | 1.9448 | -60.8465 | 2024-11-26 01:22:00 | METOP-B | CARACARAÍ | RORAIMA | Brasil | 1400209 | 14 | 33 | nan | nan | nan | Amazônia | nan |
| 11ade9c2-926a-3ad6-95f2-0a162b1966d4 | 2.6783 | -60.413101 | 2024-11-26 01:22:00 | METOP-B | CANTÁ | RORAIMA | Brasil | 1400175 | 14 | 33 | nan | nan | nan | Amazônia | nan |
| 8acd5ce4-9ed9-366b-912d-4aa40c4a8c6e | 1.9457 | -55.709702 | 2024-11-26 01:22:00 | METOP-B | ÓBIDOS | PARÁ | Brasil | 1505106 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| e433ca2d-3b22-3dc3-92f2-0697210f1db9 | 3.8235 | -59.593899 | 2024-11-26 01:22:00 | METOP-B | NORMANDIA | RORAIMA | Brasil | 1400407 | 14 | 33 | nan | nan | nan | Amazônia | nan |
| ab16a2e3-903d-31ee-a768-0598f69aafe9 | 1.9361 | -55.7076 | 2024-11-26 01:22:00 | METOP-B | ÓBIDOS | PARÁ | Brasil | 1505106 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| dcfb15b5-b050-39bf-bb04-f6e584c94c83 | 3.8333 | -59.596001 | 2024-11-26 01:22:00 | METOP-B | NORMANDIA | RORAIMA | Brasil | 1400407 | 14 | 33 | nan | nan | nan | Amazônia | nan |
| 791c518f-b562-3d8f-b36e-99c67dde7079 | 2.6762 | -60.423 | 2024-11-26 01:22:00 | METOP-B | CANTÁ | RORAIMA | Brasil | 1400175 | 14 | 33 | nan | nan | nan | Amazônia | nan |
| bf7a23c4-a326-3bdc-aa24-8224b45bab84 | 3.6207 | -60.0495 | 2024-11-26 01:22:00 | METOP-B | NORMANDIA | RORAIMA | Brasil | 1400407 | 14 | 33 | nan | nan | nan | Amazônia | nan |
| 6257a2e9-a7fc-319d-98c8-12a9487b9f5e | 3.6713 | -60.377998 | 2024-11-26 01:22:00 | METOP-B | NORMANDIA | RORAIMA | Brasil | 1400407 | 14 | 33 | nan | nan | nan | Amazônia | nan |
| 45a21169-90e3-3a2b-97f6-b58b83b7b6e6 | 2.6903 | -60.405399 | 2024-11-26 01:22:00 | METOP-B | CANTÁ | RORAIMA | Brasil | 1400175 | 14 | 33 | nan | nan | nan | Amazônia | nan |
| 21966aeb-dd31-3530-af6d-7da0536d5203 | -2.7943 | -53.004501 | 2024-11-26 01:22:00 | METOP-B | MEDICILÂNDIA | PARÁ | Brasil | 1504455 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| b654e85d-6ed9-378f-8965-e6f69b1b08a9 | 1.9316 | -55.7276 | 2024-11-26 01:22:00 | METOP-B | ÓBIDOS | PARÁ | Brasil | 1505106 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| 3832d3e9-3d7f-34a1-be33-2e7e97f591a3 | 4.2934 | -60.207001 | 2024-11-26 01:22:00 | METOP-B | UIRAMUTÃ | RORAIMA | Brasil | 1400704 | 14 | 33 | nan | nan | nan | Amazônia | nan |
| c457c21d-a958-3587-8b7e-81153b3aa284 | 2.6881 | -60.415199 | 2024-11-26 01:22:00 | METOP-B | CANTÁ | RORAIMA | Brasil | 1400175 | 14 | 33 | nan | nan | nan | Amazônia | nan |
| 661d12f2-d64d-3326-b6bb-e571c889628f | 3.8163 | -59.5802 | 2024-11-26 01:22:00 | METOP-B | NORMANDIA | RORAIMA | Brasil | 1400407 | 14 | 33 | nan | nan | nan | Amazônia | nan |
| 581f7a4f-5958-357f-8f65-f00563852636 | 4.2957 | -60.196301 | 2024-11-26 01:22:00 | METOP-B | UIRAMUTÃ | RORAIMA | Brasil | 1400704 | 14 | 33 | nan | nan | nan | Amazônia | nan |
| cce4b538-87cc-3745-83c2-1150c622c6f6 | 3.8261 | -59.582401 | 2024-11-26 01:22:00 | METOP-B | NORMANDIA | RORAIMA | Brasil | 1400407 | 14 | 33 | nan | nan | nan | Amazônia | nan |
| 035d1e4c-5985-3d39-b170-97ffebc49888 | -3.3752 | -44.173 | 2024-11-26 01:30:00 | GOES-16 | ITAPECURU MIRIM | MARANHÃO | Brasil | 2105401 | 21 | 33 | nan | nan | nan | Cerrado | 48.1 |
| e7f4ad6d-77a5-3fcc-9253-1cd436b2bb9b | -3.1691 | -48.4394 | 2024-11-26 01:30:00 | GOES-16 | TOMÉ-AÇU | PARÁ | Brasil | 1508001 | 15 | 33 | nan | nan | nan | Amazônia | 57.1 |
| 39b6cd10-0d11-360c-8e2d-bb79968fc97a | -3.1876 | -48.4387 | 2024-11-26 01:30:00 | GOES-16 | TOMÉ-AÇU | PARÁ | Brasil | 1508001 | 15 | 33 | nan | nan | nan | Amazônia | 107.7 |
| 1ae3b115-68eb-3402-98a7-64bc74b9eb3d | -3.6042 | -50.3781 | 2024-11-26 01:30:00 | GOES-16 | PACAJÁ | PARÁ | Brasil | 1505486 | 15 | 33 | nan | nan | nan | Amazônia | 142.5 |
| ff3d923d-d5e8-332c-96b8-40a9b8f6dc7d | -3.9265 | -42.4246 | 2024-11-26 01:30:00 | GOES-16 | CAMPO LARGO DO PIAUÍ | PIAUÍ | Brasil | 2202174 | 22 | 33 | nan | nan | nan | Caatinga | 47.5 |
| b1bedc64-5b78-35fc-b214-add54c01f52c | -2.8017 | -52.921 | 2024-11-26 01:30:00 | GOES-16 | MEDICILÂNDIA | PARÁ | Brasil | 1504455 | 15 | 33 | nan | nan | nan | Amazônia | 50.8 |
| b7abf5f1-fa44-387d-90dd-3ff07d1d89b2 | -3.5856 | -50.3997 | 2024-11-26 01:30:00 | GOES-16 | PACAJÁ | PARÁ | Brasil | 1505486 | 15 | 33 | nan | nan | nan | Amazônia | 61.0 |
| 78b19d35-ff60-3724-bf1e-f1d30ce2d390 | -3.9078 | -42.4256 | 2024-11-26 01:30:00 | GOES-16 | CAMPO LARGO DO PIAUÍ | PIAUÍ | Brasil | 2202174 | 22 | 33 | nan | nan | nan | Caatinga | 42.2 |
| 56121b96-6d5e-3172-81e8-8f970497bb8a | -2.532 | -45.5862 | 2024-11-26 01:30:00 | GOES-16 | SANTA LUZIA DO PARUÁ | MARANHÃO | Brasil | 2110039 | 21 | 33 | nan | nan | nan | Amazônia | 99.3 |
| d658843d-8584-3590-805c-586508faeccc | -3.5857 | -50.3787 | 2024-11-26 01:30:00 | GOES-16 | PACAJÁ | PARÁ | Brasil | 1505486 | 15 | 33 | nan | nan | nan | Amazônia | 74.3 |
| 0d81b273-b707-33d3-9cec-f5b48b532731 | -4.5376 | -43.2807 | 2024-11-26 01:30:00 | GOES-16 | ALDEIAS ALTAS | MARANHÃO | Brasil | 2100303 | 21 | 33 | nan | nan | nan | Cerrado | 49.0 |
| 2c24f787-acfe-3825-a65e-4ee5853e4df1 | -3.8691 | -49.1415 | 2024-11-26 01:30:00 | GOES-16 | GOIANÉSIA DO PARÁ | PARÁ | Brasil | 1503093 | 15 | 33 | nan | nan | nan | Amazônia | 88.8 |
| 268a90f4-a0d9-33f9-85da-35b98a030087 | -3.8506 | -49.1422 | 2024-11-26 01:30:00 | GOES-16 | BREU BRANCO | PARÁ | Brasil | 1501782 | 15 | 33 | nan | nan | nan | Amazônia | 66.0 |
| 100f591d-c230-3a93-95d4-2181ce2b09f8 | -3.2419 | -53.2954 | 2024-11-26 01:30:00 | GOES-16 | MEDICILÂNDIA | PARÁ | Brasil | 1504455 | 15 | 33 | nan | nan | nan | Amazônia | 55.7 |
| d8cf6eea-f419-32b7-b8ab-6a6b24b01119 | -3.6041 | -50.3991 | 2024-11-26 01:30:00 | GOES-16 | PACAJÁ | PARÁ | Brasil | 1505486 | 15 | 33 | nan | nan | nan | Amazônia | 104.6 |
| c2b0de4b-8a4d-3612-a4cc-d307123a160c | -4.5375 | -43.304 | 2024-11-26 01:30:00 | GOES-16 | ALDEIAS ALTAS | MARANHÃO | Brasil | 2100303 | 21 | 33 | nan | nan | nan | Cerrado | 47.6 |
| 9ad29160-4429-39c7-b28b-eaefd2602352 | -2.5504 | -45.608 | 2024-11-26 01:30:00 | GOES-16 | SANTA LUZIA DO PARUÁ | MARANHÃO | Brasil | 2110039 | 21 | 33 | nan | nan | nan | Amazônia | 34.4 |
| d6d3a1f7-1b50-3977-9aec-adc82235f3db | -2.8198 | -53.0222 | 2024-11-26 01:30:00 | GOES-16 | MEDICILÂNDIA | PARÁ | Brasil | 1504455 | 15 | 33 | nan | nan | nan | Amazônia | 71.7 |
| 59dfc890-a334-3ef1-82ec-322bb5f352e6 | -3.3938 | -44.1722 | 2024-11-26 01:30:00 | GOES-16 | ITAPECURU MIRIM | MARANHÃO | Brasil | 2105401 | 21 | 33 | nan | nan | nan | Cerrado | 155.6 |


[Clique aqui para ver as próximas entradas](README9.md)
