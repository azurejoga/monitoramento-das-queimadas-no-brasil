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

## Dados Diários - Página 12

| ID | Latitude | Longitude | Data/Hora GMT | Satélite | Município | Estado | País | Município ID | Estado ID | País ID | Dias sem Chuva | Precipitação | Risco de Fogo | Bioma | FRP |
|----|----------|-----------|---------------|----------|-----------|--------|------|--------------|-----------|---------|----------------|--------------|----------------|-------|-----|
| b1756641-0f2f-37dd-95aa-2fb4629f51a0 | -16.779 | -57.8306 | 2024-10-03 00:16:40 | GOES-16 | CÁCERES | MATO GROSSO | Brasil | 5102504 | 51 | 33 | nan | nan | nan | Pantanal | 110.8 |
| 7c10b6a2-2e4b-34cf-9217-a8f20a0e7d62 | -16.7793 | -57.8102 | 2024-10-03 00:16:40 | GOES-16 | CÁCERES | MATO GROSSO | Brasil | 5102504 | 51 | 33 | nan | nan | nan | Pantanal | 109.6 |
| 3941a123-babb-36c6-ad25-8ca94f118764 | -16.7985 | -57.8284 | 2024-10-03 00:16:41 | GOES-16 | CÁCERES | MATO GROSSO | Brasil | 5102504 | 51 | 33 | nan | nan | nan | Pantanal | 49.4 |
| ae3c4290-7959-3f9a-9bef-10706077f511 | -17.6873 | -53.1003 | 2024-10-03 00:16:45 | GOES-16 | MINEIROS | GOIÁS | Brasil | 5213103 | 52 | 33 | nan | nan | nan | Cerrado | 57.6 |
| baabbf9a-ba43-3c31-a5b7-f5e023d20f6c | -17.8403 | -57.7076 | 2024-10-03 00:16:46 | GOES-16 | CORUMBÁ | MATO GROSSO DO SUL | Brasil | 5003207 | 50 | 33 | nan | nan | nan | Pantanal | 101.9 |
| fa63b2fe-cbf0-32a3-aa78-b87fbd85d8bb | -17.8407 | -57.6871 | 2024-10-03 00:16:46 | GOES-16 | CORUMBÁ | MATO GROSSO DO SUL | Brasil | 5003207 | 50 | 33 | nan | nan | nan | Pantanal | 88.9 |
| 266b3044-91a7-3cbc-a27e-dc626586d919 | -18.8927 | -41.2248 | 2024-10-03 00:16:50 | GOES-16 | CONSELHEIRO PENA | MINAS GERAIS | Brasil | 3118403 | 31 | 33 | nan | nan | nan | Mata Atlântica | 105.5 |
| 509b9519-38b2-3b71-a012-1ac39d91eaf8 | -18.8935 | -41.199 | 2024-10-03 00:16:50 | GOES-16 | CONSELHEIRO PENA | MINAS GERAIS | Brasil | 3118403 | 31 | 33 | nan | nan | nan | Mata Atlântica | 85.5 |
| f3de0f23-e8be-3057-abd6-2bab7a11c20e | -18.7172 | -57.3305 | 2024-10-03 00:16:51 | GOES-16 | CORUMBÁ | MATO GROSSO DO SUL | Brasil | 5003207 | 50 | 33 | nan | nan | nan | Pantanal | 98.0 |
| 2aa0256c-1064-3adb-9a6b-e3236e9e6836 | -18.7372 | -57.3279 | 2024-10-03 00:16:51 | GOES-16 | CORUMBÁ | MATO GROSSO DO SUL | Brasil | 5003207 | 50 | 33 | nan | nan | nan | Pantanal | 78.4 |
| 72232e6a-c40d-3795-9163-394a23f48f6b | -19.0344 | -43.1944 | 2024-10-03 00:16:51 | GOES-16 | CARMÉSIA | MINAS GERAIS | Brasil | 3113800 | 31 | 33 | nan | nan | nan | Mata Atlântica | 67.5 |
| d803bcf6-8b6c-3cec-a0dc-f2f55de26b1b | -18.8899 | -54.4947 | 2024-10-03 00:16:51 | GOES-16 | RIO VERDE DE MATO GROSSO | MATO GROSSO DO SUL | Brasil | 5007406 | 50 | 33 | nan | nan | nan | Cerrado | 78.8 |
| ac741d66-9b3d-3877-a278-3a75d4cae232 | -20.6617 | -42.0115 | 2024-10-03 00:16:59 | GOES-16 | CARANGOLA | MINAS GERAIS | Brasil | 3113305 | 31 | 33 | nan | nan | nan | Mata Atlântica | 192.8 |
| 473fbe5b-bf72-37cb-9845-7b20047e8981 | -20.6625 | -41.9858 | 2024-10-03 00:16:59 | GOES-16 | CARANGOLA | MINAS GERAIS | Brasil | 3113305 | 31 | 33 | nan | nan | nan | Mata Atlântica | 174.6 |
| a8f06b05-55f3-378f-8025-511553c193e6 | -20.6824 | -42.0053 | 2024-10-03 00:16:59 | GOES-16 | CARANGOLA | MINAS GERAIS | Brasil | 3113305 | 31 | 33 | nan | nan | nan | Mata Atlântica | 80.2 |
| 8d36bb5f-f430-3724-8b39-ae4f8ce1fe47 | -20.6833 | -41.9796 | 2024-10-03 00:16:59 | GOES-16 | CARANGOLA | MINAS GERAIS | Brasil | 3113305 | 31 | 33 | nan | nan | nan | Mata Atlântica | 93.3 |
| 5ca672d4-78d4-377a-af75-0f85bfe8d64d | -21.306 | -47.6227 | 2024-10-03 00:17:03 | GOES-16 | SERRA AZUL | SÃO PAULO | Brasil | 3551405 | 35 | 33 | nan | nan | nan | Cerrado | 91.5 |
| 70bb42cf-d374-3c13-94bf-2224256451ce | -21.3067 | -47.599 | 2024-10-03 00:17:03 | GOES-16 | SERRA AZUL | SÃO PAULO | Brasil | 3551405 | 35 | 33 | nan | nan | nan | Cerrado | 97.9 |
| 2d659625-5132-3492-b410-937fa8674106 | -21.3868 | -47.6734 | 2024-10-03 00:17:04 | GOES-16 | SÃO SIMÃO | SÃO PAULO | Brasil | 3550902 | 35 | 33 | nan | nan | nan | Cerrado | 88.8 |
| 23018e86-38c4-3666-99d5-d8826e85f8cd | -21.3875 | -47.6497 | 2024-10-03 00:17:04 | GOES-16 | SÃO SIMÃO | SÃO PAULO | Brasil | 3550902 | 35 | 33 | nan | nan | nan | Cerrado | 85.2 |
| f91f7f40-25c6-3e28-9741-95b43f6b229b | -21.3882 | -47.6261 | 2024-10-03 00:17:04 | GOES-16 | SÃO SIMÃO | SÃO PAULO | Brasil | 3550902 | 35 | 33 | nan | nan | nan | Cerrado | 69.5 |
| fd5f1a0a-636e-31ad-ad63-060887636f7a | -21.3456 | -55.6841 | 2024-10-03 00:17:04 | GOES-16 | MARACAJU | MATO GROSSO DO SUL | Brasil | 5005400 | 50 | 33 | nan | nan | nan | Cerrado | 137.5 |
| 4de7288e-a99c-39a0-a96c-71a51831bfaa | -21.346 | -55.6626 | 2024-10-03 00:17:04 | GOES-16 | NIOAQUE | MATO GROSSO DO SUL | Brasil | 5005806 | 50 | 33 | nan | nan | nan | Cerrado | 301.5 |
| 04af1802-a2f0-305f-a756-7a37a0f4f29c | -21.3465 | -55.6411 | 2024-10-03 00:17:04 | GOES-16 | MARACAJU | MATO GROSSO DO SUL | Brasil | 5005400 | 50 | 33 | nan | nan | nan | Cerrado | 84.4 |
| 1b58a83a-74c3-35ac-85e1-72a93c9d8ff8 | -21.8792 | -48.443 | 2024-10-03 00:17:06 | GOES-16 | BOA ESPERANÇA DO SUL | SÃO PAULO | Brasil | 3506706 | 35 | 33 | nan | nan | nan | Cerrado | 118.1 |
| fc4ed4d9-70ed-3fd3-9069-30b1dd305d16 | -22.2307 | -48.4507 | 2024-10-03 00:17:08 | GOES-16 | JAÚ | SÃO PAULO | Brasil | 3525300 | 35 | 33 | nan | nan | nan | Cerrado | 123.0 |
| 83a1fced-612e-33a3-939f-96a9538b6bee | -22.2314 | -48.4272 | 2024-10-03 00:17:08 | GOES-16 | JAÚ | SÃO PAULO | Brasil | 3525300 | 35 | 33 | nan | nan | nan | Cerrado | 127.1 |
| 603f84da-bf8b-33ec-aa38-8270c8c0c5c5 | -22.2515 | -48.4456 | 2024-10-03 00:17:08 | GOES-16 | JAÚ | SÃO PAULO | Brasil | 3525300 | 35 | 33 | nan | nan | nan | Cerrado | 119.2 |
| 03ac898a-f301-3bcb-b7b9-857d502a17c0 | -22.2522 | -48.422 | 2024-10-03 00:17:08 | GOES-16 | JAÚ | SÃO PAULO | Brasil | 3525300 | 35 | 33 | nan | nan | nan | Cerrado | 99.8 |
| af373e59-e3b1-395c-b0e1-aa0e14cb2faf | -22.3495 | -47.9515 | 2024-10-03 00:17:09 | GOES-16 | ITIRAPINA | SÃO PAULO | Brasil | 3523602 | 35 | 33 | nan | nan | nan | Cerrado | 75.2 |
| ab62ffa5-56c4-3a4b-94b5-3134f2081d11 | -22.3502 | -47.9278 | 2024-10-03 00:17:09 | GOES-16 | ITIRAPINA | SÃO PAULO | Brasil | 3523602 | 35 | 33 | nan | nan | nan | Cerrado | 107.4 |
| cab140de-6cce-373a-a341-f1c62dc7e8ca | -22.3704 | -47.9462 | 2024-10-03 00:17:09 | GOES-16 | ITIRAPINA | SÃO PAULO | Brasil | 3523602 | 35 | 33 | nan | nan | nan | Cerrado | 78.6 |
| 317719d4-dccd-3322-be02-c229fb6a5a05 | -22.3711 | -47.9225 | 2024-10-03 00:17:09 | GOES-16 | ITIRAPINA | SÃO PAULO | Brasil | 3523602 | 35 | 33 | nan | nan | nan | Cerrado | 115.0 |
| 6934b31e-705b-3112-abfe-d21bba72ddaa | -22.446 | -46.8576 | 2024-10-03 00:17:09 | GOES-16 | ITAPIRA | SÃO PAULO | Brasil | 3522604 | 35 | 33 | nan | nan | nan | Cerrado | 81.0 |
| adbeb6e9-29fc-3119-85db-89132d3a7132 | -23.1015 | -46.6069 | 2024-10-03 00:17:12 | GOES-16 | ATIBAIA | SÃO PAULO | Brasil | 3504107 | 35 | 33 | nan | nan | nan | Mata Atlântica | 78.4 |
| 965d0796-535f-3930-ae96-fb47fc2080fc | -1.7509 | -54.4531 | 2024-10-03 00:25:16 | GOES-16 | ALENQUER | PARÁ | Brasil | 1500404 | 15 | 33 | nan | nan | nan | Amazônia | 80.9 |
| df1f39ad-5bac-327d-a645-75682ab9c5c0 | -1.7692 | -54.4528 | 2024-10-03 00:25:16 | GOES-16 | ALENQUER | PARÁ | Brasil | 1500404 | 15 | 33 | nan | nan | nan | Amazônia | 57.5 |
| 14179c13-49a9-3332-a371-2c953fd370ba | -3.3854 | -42.2866 | 2024-10-03 00:25:25 | GOES-16 | SÃO BERNARDO | MARANHÃO | Brasil | 2110609 | 21 | 33 | nan | nan | nan | Cerrado | 124.9 |
| 79e44abc-db80-35f1-a3e8-2f406476ec57 | -3.3855 | -42.263 | 2024-10-03 00:25:25 | GOES-16 | MAGALHÃES DE ALMEIDA | MARANHÃO | Brasil | 2106300 | 21 | 33 | nan | nan | nan | Cerrado | 65.1 |
| 3e6e6ad5-d0de-3de7-bfb5-6350cbacebfa | -3.404 | -42.2858 | 2024-10-03 00:25:25 | GOES-16 | SÃO BERNARDO | MARANHÃO | Brasil | 2110609 | 21 | 33 | nan | nan | nan | Cerrado | 425.5 |
| 8c6ce6ef-b01e-3e62-8e8f-5210ffd1b411 | -3.4042 | -42.2621 | 2024-10-03 00:25:25 | GOES-16 | MAGALHÃES DE ALMEIDA | MARANHÃO | Brasil | 2106300 | 21 | 33 | nan | nan | nan | Cerrado | 220.1 |
| 4aaeb46f-640f-3b2c-92e2-246e6a6c9597 | -3.802 | -47.8104 | 2024-10-03 00:25:27 | GOES-16 | ULIANÓPOLIS | PARÁ | Brasil | 1508126 | 15 | 33 | nan | nan | nan | Amazônia | 51.5 |
| 374ee1fa-62b7-37d9-a597-f91d41f2e3cc | -4.0949 | -48.4894 | 2024-10-03 00:25:29 | GOES-16 | RONDON DO PARÁ | PARÁ | Brasil | 1506187 | 15 | 33 | nan | nan | nan | Amazônia | 100.9 |
| c1e1a32e-1dce-348e-b3cf-d00e024f251b | -4.095 | -48.4679 | 2024-10-03 00:25:29 | GOES-16 | RONDON DO PARÁ | PARÁ | Brasil | 1506187 | 15 | 33 | nan | nan | nan | Amazônia | 94.5 |
| 6d841c32-21d0-33d2-b0e2-52e039623204 | -4.1134 | -48.4886 | 2024-10-03 00:25:29 | GOES-16 | RONDON DO PARÁ | PARÁ | Brasil | 1506187 | 15 | 33 | nan | nan | nan | Amazônia | 53.1 |
| a093c362-ec7c-341f-9e6f-fe4f49888208 | -4.4657 | -42.8877 | 2024-10-03 00:25:31 | GOES-16 | CAXIAS | MARANHÃO | Brasil | 2103000 | 21 | 33 | nan | nan | nan | Cerrado | 107.4 |
| d7730b27-9054-3551-8054-f0f222f853d9 | -4.4844 | -42.8866 | 2024-10-03 00:25:31 | GOES-16 | CAXIAS | MARANHÃO | Brasil | 2103000 | 21 | 33 | nan | nan | nan | Cerrado | 81.2 |
| 33d18ae1-c759-3df3-af1d-e20599ded161 | -4.5375 | -43.304 | 2024-10-03 00:25:31 | GOES-16 | ALDEIAS ALTAS | MARANHÃO | Brasil | 2100303 | 21 | 33 | nan | nan | nan | Cerrado | 111.4 |
| d7569647-0293-3f76-9fb5-8236d0ee480d | -4.58 | -48.0132 | 2024-10-03 00:25:32 | GOES-16 | RONDON DO PARÁ | PARÁ | Brasil | 1506187 | 15 | 33 | nan | nan | nan | Amazônia | 65.1 |
| 7c7b6713-a531-356d-b773-a9fed72fe196 | -4.9264 | -43.79 | 2024-10-03 00:25:34 | GOES-16 | SÃO JOÃO DO SOTER | MARANHÃO | Brasil | 2111078 | 21 | 33 | nan | nan | nan | Cerrado | 74.2 |
| 0c50da14-4280-3c49-98f7-ba7138c4024e | -4.9265 | -43.7669 | 2024-10-03 00:25:34 | GOES-16 | SÃO JOÃO DO SOTER | MARANHÃO | Brasil | 2111078 | 21 | 33 | nan | nan | nan | Cerrado | 95.7 |
| 58117c42-e12c-3aa2-9ed2-d580346b7d76 | -4.9452 | -43.7657 | 2024-10-03 00:25:34 | GOES-16 | SÃO JOÃO DO SOTER | MARANHÃO | Brasil | 2111078 | 21 | 33 | nan | nan | nan | Cerrado | 60.8 |
| 8de36b61-f1ba-348b-b60f-b067285e5cc0 | -5.2253 | -43.8164 | 2024-10-03 00:25:35 | GOES-16 | SÃO JOÃO DO SOTER | MARANHÃO | Brasil | 2111078 | 21 | 33 | nan | nan | nan | Cerrado | 107.2 |
| 5a633e0c-b6e9-30e3-a40e-3b9fe73f7896 | -5.2255 | -43.7932 | 2024-10-03 00:25:35 | GOES-16 | SÃO JOÃO DO SOTER | MARANHÃO | Brasil | 2111078 | 21 | 33 | nan | nan | nan | Cerrado | 132.1 |
| aba46c67-8851-39f5-84a5-604b761526be | -5.2441 | -43.8151 | 2024-10-03 00:25:35 | GOES-16 | SÃO JOÃO DO SOTER | MARANHÃO | Brasil | 2111078 | 21 | 33 | nan | nan | nan | Cerrado | 272.8 |
| 7f52d4a9-d839-3615-8de0-4cf17499e548 | -5.2443 | -43.792 | 2024-10-03 00:25:35 | GOES-16 | SÃO JOÃO DO SOTER | MARANHÃO | Brasil | 2111078 | 21 | 33 | nan | nan | nan | Cerrado | 344.6 |
| 533103f5-ca1b-3d6d-bbf4-aaf8eab776a6 | -5.263 | -43.7907 | 2024-10-03 00:25:36 | GOES-16 | SÃO JOÃO DO SOTER | MARANHÃO | Brasil | 2111078 | 21 | 33 | nan | nan | nan | Cerrado | 63.5 |
| 590c45f4-bd35-3d9e-8b82-e2faa1863eb3 | -5.8358 | -44.6231 | 2024-10-03 00:25:39 | GOES-16 | TUNTUM | MARANHÃO | Brasil | 2112308 | 21 | 33 | nan | nan | nan | Cerrado | 52.9 |
| 702c8c73-8103-39b8-817a-8e481f077617 | -5.836 | -44.6002 | 2024-10-03 00:25:39 | GOES-16 | COLINAS | MARANHÃO | Brasil | 2103505 | 21 | 33 | nan | nan | nan | Cerrado | 80.4 |
| c1249793-3aa6-34a1-bd4a-d171f2789aaf | -5.8545 | -44.6217 | 2024-10-03 00:25:39 | GOES-16 | TUNTUM | MARANHÃO | Brasil | 2112308 | 21 | 33 | nan | nan | nan | Cerrado | 217.6 |
| 03d7e333-d6db-3b4b-92d1-c20000aef0b7 | -5.8547 | -44.5988 | 2024-10-03 00:25:39 | GOES-16 | COLINAS | MARANHÃO | Brasil | 2103505 | 21 | 33 | nan | nan | nan | Cerrado | 499.4 |
| 805570e6-7217-39dc-8593-bf73f3681713 | -6.8772 | -43.6152 | 2024-10-03 00:25:45 | GOES-16 | GUADALUPE | PIAUÍ | Brasil | 2204501 | 22 | 33 | nan | nan | nan | Cerrado | 60.9 |
| 8f346906-8a1a-3a75-b673-19009f897e54 | -6.8777 | -59.0504 | 2024-10-03 00:25:45 | GOES-16 | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 62.8 |
| d0294ee9-b8aa-3373-87d8-4e81506beb98 | -6.8778 | -59.031 | 2024-10-03 00:25:45 | GOES-16 | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 64.0 |
| 9341c75d-d5c0-3a50-9a07-842e714a21dd | -7.1871 | -59.7893 | 2024-10-03 00:25:47 | GOES-16 | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 52.8 |
| a9da2e69-49ad-395d-ad52-1a632db2db6a | -7.2056 | -59.7886 | 2024-10-03 00:25:47 | GOES-16 | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 51.7 |
| 90a6a5a9-d91c-35d6-836c-a1d9bef7285b | -7.3726 | -68.0177 | 2024-10-03 00:25:48 | GOES-16 | PAUINI | AMAZONAS | Brasil | 1303502 | 13 | 33 | nan | nan | nan | Amazônia | 46.3 |
| e39ed857-e2f5-3e63-93f8-168d04b12d3b | -7.8785 | -72.805 | 2024-10-03 00:25:51 | GOES-16 | RODRIGUES ALVES | ACRE | Brasil | 1200427 | 12 | 33 | nan | nan | nan | Amazônia | 44.3 |
| 221499e8-7904-3b66-ab39-1838a6954824 | -8.8506 | -45.5086 | 2024-10-03 00:25:56 | GOES-16 | SANTA FILOMENA | PIAUÍ | Brasil | 2209203 | 22 | 33 | nan | nan | nan | Cerrado | 39.2 |
| b6387ebd-b253-372a-8581-12dc25b63d6b | -8.8926 | -62.3348 | 2024-10-03 00:25:57 | GOES-16 | CUJUBIM | RONDÔNIA | Brasil | 1100940 | 11 | 33 | nan | nan | nan | Amazônia | 95.2 |
| 0dc395fb-1714-3c28-a327-6be8555072ed | -8.9594 | -63.6187 | 2024-10-03 00:25:57 | GOES-16 | CANDEIAS DO JAMARI | RONDÔNIA | Brasil | 1100809 | 11 | 33 | nan | nan | nan | Amazônia | 44.3 |
| bdb5531f-5335-3e74-a770-aca7c74ee0f9 | -8.9791 | -67.4099 | 2024-10-03 00:25:58 | GOES-16 | BOCA DO ACRE | AMAZONAS | Brasil | 1300706 | 13 | 33 | nan | nan | nan | Amazônia | 54.4 |
| 0070ae0e-6deb-3506-a089-211ea7315c60 | -8.9976 | -67.4094 | 2024-10-03 00:25:58 | GOES-16 | BOCA DO ACRE | AMAZONAS | Brasil | 1300706 | 13 | 33 | nan | nan | nan | Amazônia | 56.6 |
| 9db1d2ec-1634-3eed-868a-6ed9947274ce | -9.0149 | -67.7423 | 2024-10-03 00:25:58 | GOES-16 | BOCA DO ACRE | AMAZONAS | Brasil | 1300706 | 13 | 33 | nan | nan | nan | Amazônia | 121.4 |
| 3febb146-43f1-38d5-a3ee-e37af0815a08 | -9.0334 | -67.7419 | 2024-10-03 00:25:58 | GOES-16 | BOCA DO ACRE | AMAZONAS | Brasil | 1300706 | 13 | 33 | nan | nan | nan | Amazônia | 35.4 |
| 40b90daa-8a78-3f32-bcbf-e13bef5c6970 | -9.0515 | -67.871 | 2024-10-03 00:25:58 | GOES-16 | BOCA DO ACRE | AMAZONAS | Brasil | 1300706 | 13 | 33 | nan | nan | nan | Amazônia | 47.9 |
| 39f65194-252e-3a0a-af19-fb4938ec8713 | -9.0516 | -67.8525 | 2024-10-03 00:25:58 | GOES-16 | BOCA DO ACRE | AMAZONAS | Brasil | 1300706 | 13 | 33 | nan | nan | nan | Amazônia | 29.0 |
| eb93aad0-be24-302d-9d51-d3ca502f19fb | -9.1566 | -61.6758 | 2024-10-03 00:25:58 | GOES-16 | MACHADINHO D'OESTE | RONDÔNIA | Brasil | 1100130 | 11 | 33 | nan | nan | nan | Amazônia | 131.4 |
| a40f3800-ed45-3d91-b69b-9c4008213b3e | -9.1568 | -61.6567 | 2024-10-03 00:25:58 | GOES-16 | MACHADINHO D'OESTE | RONDÔNIA | Brasil | 1100130 | 11 | 33 | nan | nan | nan | Amazônia | 75.0 |
| d9e8a534-d2c7-3855-b2a5-fd39a0e5ab96 | -9.1752 | -61.6749 | 2024-10-03 00:25:59 | GOES-16 | MACHADINHO D'OESTE | RONDÔNIA | Brasil | 1100130 | 11 | 33 | nan | nan | nan | Amazônia | 96.3 |
| 185e83d5-9f08-3a63-a0d7-41dc9f54b687 | -9.2739 | -67.8286 | 2024-10-03 00:25:59 | GOES-16 | BOCA DO ACRE | AMAZONAS | Brasil | 1300706 | 13 | 33 | nan | nan | nan | Amazônia | 42.4 |
| 25bd1c78-12a4-3e9d-8e71-0de8f535d594 | -9.3839 | -61.0526 | 2024-10-03 00:26:00 | GOES-16 | COLNIZA | MATO GROSSO | Brasil | 5103254 | 51 | 33 | nan | nan | nan | Amazônia | 113.2 |
| aafb8b41-6b1b-31d8-bb91-274df6b38fb2 | -9.3652 | -68.1965 | 2024-10-03 00:26:00 | GOES-16 | BUJARI | ACRE | Brasil | 1200138 | 12 | 33 | nan | nan | nan | Amazônia | 11.1 |
| ea4a55b3-5631-3395-8fb2-acfa6d6b93bf | -9.4025 | -61.0517 | 2024-10-03 00:26:00 | GOES-16 | COLNIZA | MATO GROSSO | Brasil | 5103254 | 51 | 33 | nan | nan | nan | Amazônia | 97.2 |
| 650ce9b8-4cbd-3927-85ae-c78356c7ab87 | -9.3833 | -68.3256 | 2024-10-03 00:26:00 | GOES-16 | BUJARI | ACRE | Brasil | 1200138 | 12 | 33 | nan | nan | nan | Amazônia | 36.8 |
| 1893ed00-a5c6-3c8c-8ea2-96f5751a2b51 | -9.4244 | -67.2313 | 2024-10-03 00:26:00 | GOES-16 | LÁBREA | AMAZONAS | Brasil | 1302405 | 13 | 33 | nan | nan | nan | Amazônia | 44.7 |
| 037b201d-af1e-3bad-b913-b039c2bba43f | -9.4368 | -64.5419 | 2024-10-03 00:26:00 | GOES-16 | PORTO VELHO | RONDÔNIA | Brasil | 1100205 | 11 | 33 | nan | nan | nan | Amazônia | 104.7 |
| 28e19115-4b71-3a81-9549-f0f5ce0c6842 | -9.4554 | -64.5412 | 2024-10-03 00:26:00 | GOES-16 | PORTO VELHO | RONDÔNIA | Brasil | 1100205 | 11 | 33 | nan | nan | nan | Amazônia | 51.7 |
| bf39ac5b-2c0f-3d6a-97ff-57f9b923df80 | -9.468 | -62.3857 | 2024-10-03 00:26:00 | GOES-16 | MACHADINHO D'OESTE | RONDÔNIA | Brasil | 1100130 | 11 | 33 | nan | nan | nan | Amazônia | 82.9 |
| 9408ab84-cfae-311f-952a-dedb4b1d4f21 | -9.4865 | -62.4039 | 2024-10-03 00:26:00 | GOES-16 | MACHADINHO D'OESTE | RONDÔNIA | Brasil | 1100130 | 11 | 33 | nan | nan | nan | Amazônia | 73.0 |
| cb6636e8-efe2-33eb-8bf5-5305b6b4b746 | -9.4866 | -62.3849 | 2024-10-03 00:26:00 | GOES-16 | MACHADINHO D'OESTE | RONDÔNIA | Brasil | 1100130 | 11 | 33 | nan | nan | nan | Amazônia | 124.5 |
| 5d076a2d-6bfe-34ea-b7f1-41f6a9f7b384 | -23.08555 | -46.61002 | 2024-10-03 00:26:00 | TERRA_M-M | ATIBAIA | SÃO PAULO | Brasil | 3504107 | 35 | 33 | nan | nan | nan | Mata Atlântica | 49.9 |
| 212c96d2-f84a-3942-be0b-aa4f1dd0e50a | -22.71489 | -46.6699 | 2024-10-03 00:26:00 | TERRA_M-M | MONTE ALEGRE DO SUL | SÃO PAULO | Brasil | 3531209 | 35 | 33 | nan | nan | nan | Mata Atlântica | 28.7 |
| 5bef210e-34e4-3130-b1ca-37c186800573 | -22.71343 | -46.67724 | 2024-10-03 00:26:00 | TERRA_M-M | MONTE ALEGRE DO SUL | SÃO PAULO | Brasil | 3531209 | 35 | 33 | nan | nan | nan | Mata Atlântica | 33.6 |
| 0ac521af-1f63-3bc7-9020-83b61d582f15 | -22.70049 | -46.67336 | 2024-10-03 00:26:00 | TERRA_M-M | MONTE ALEGRE DO SUL | SÃO PAULO | Brasil | 3531209 | 35 | 33 | nan | nan | nan | Mata Atlântica | 48.9 |
| d40002db-e573-33bc-8704-d83fb98a40c3 | -22.69898 | -46.68004 | 2024-10-03 00:26:00 | TERRA_M-M | MONTE ALEGRE DO SUL | SÃO PAULO | Brasil | 3531209 | 35 | 33 | nan | nan | nan | Mata Atlântica | 35.7 |
| 9a50137b-b388-324f-9ff0-23959f9d64b5 | -22.66537 | -46.79792 | 2024-10-03 00:26:00 | TERRA_M-M | AMPARO | SÃO PAULO | Brasil | 3501905 | 35 | 33 | nan | nan | nan | Mata Atlântica | 22.6 |
| fad67716-9b4c-3bd1-a6b4-71166161e927 | -22.59202 | -42.16397 | 2024-10-03 00:26:00 | TERRA_M-M | ARARUAMA | RIO DE JANEIRO | Brasil | 3300209 | 33 | 33 | nan | nan | nan | Mata Atlântica | 13.1 |
| 20f80c23-c8a4-322a-9eec-6c423e3fb2cb | -22.59052 | -42.15065 | 2024-10-03 00:26:00 | TERRA_M-M | CABO FRIO | RIO DE JANEIRO | Brasil | 3300704 | 33 | 33 | nan | nan | nan | Mata Atlântica | 27.6 |
| 2cb2e1d1-c520-3b52-b25b-83000903b0eb | -22.58425 | -42.15791 | 2024-10-03 00:26:00 | TERRA_M-M | CABO FRIO | RIO DE JANEIRO | Brasil | 3300704 | 33 | 33 | nan | nan | nan | Mata Atlântica | 50.2 |


[Clique aqui para ver as próximas entradas](README13.md)
