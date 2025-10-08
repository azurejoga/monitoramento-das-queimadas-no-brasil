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

## Dados Diários - Página 10

| ID | Latitude | Longitude | Data/Hora GMT | Satélite | Município | Estado | País | Município ID | Estado ID | País ID | Dias sem Chuva | Precipitação | Risco de Fogo | Bioma | FRP |
|----|----------|-----------|---------------|----------|-----------|--------|------|--------------|-----------|---------|----------------|--------------|----------------|-------|-----|
| 4cc55013-9812-3765-b924-d52e515e6ca7 | -9.6104 | -40.342 | 2025-10-08 01:30:00 | GOES-19 | JUAZEIRO | BAHIA | Brasil | 2918407 | 29 | 33 | nan | nan | nan | Caatinga | 196.0 |
| 838b9b6b-1960-35ee-9fe9-83f4feb5582e | -11.3497 | -55.1689 | 2025-10-08 01:30:00 | GOES-19 | CLÁUDIA | MATO GROSSO | Brasil | 5103056 | 51 | 33 | nan | nan | nan | Amazônia | 66.0 |
| e5f0eb54-d10d-3279-9cc9-9f268ac3acbd | -9.1718 | -46.9123 | 2025-10-08 01:30:00 | GOES-19 | LIZARDA | TOCANTINS | Brasil | 1712405 | 17 | 33 | nan | nan | nan | Cerrado | 71.8 |
| 77ba033c-4c9a-360e-b988-df5ffb1ce30e | -17.3048 | -42.6182 | 2025-10-08 01:30:00 | GOES-19 | MINAS NOVAS | MINAS GERAIS | Brasil | 3141801 | 31 | 33 | nan | nan | nan | Cerrado | 84.2 |
| 4bcd5c32-dc38-365e-bfd2-fd6c6940e89b | -11.4531 | -50.2195 | 2025-10-08 01:30:00 | GOES-19 | LAGOA DA CONFUSÃO | TOCANTINS | Brasil | 1711902 | 17 | 33 | nan | nan | nan | Cerrado | 145.4 |
| df6b3e16-d499-3be7-86d5-782154552a0f | -11.7079 | -50.9811 | 2025-10-08 01:30:00 | GOES-19 | SÃO FÉLIX DO ARAGUAIA | MATO GROSSO | Brasil | 5107859 | 51 | 33 | nan | nan | nan | Cerrado | 149.6 |
| fd687977-8bf9-3b66-9372-fc5158f40301 | -11.1644 | -54.8804 | 2025-10-08 01:30:00 | GOES-19 | NOVA SANTA HELENA | MATO GROSSO | Brasil | 5106190 | 51 | 33 | nan | nan | nan | Amazônia | 200.0 |
| 103815a3-8118-33e3-b103-100f0a268350 | -7.0359 | -42.8744 | 2025-10-08 01:30:00 | GOES-19 | NAZARÉ DO PIAUÍ | PIAUÍ | Brasil | 2206704 | 22 | 33 | nan | nan | nan | Caatinga | 159.8 |
| a4932a12-dc48-3129-84fd-a142896f27de | -12.0314 | -45.1901 | 2025-10-08 01:30:00 | GOES-19 | BARREIRAS | BAHIA | Brasil | 2903201 | 29 | 33 | nan | nan | nan | Cerrado | 56.5 |
| 5ae6aa19-aca4-3357-8db0-e46c7bffa874 | -15.9568 | -42.5876 | 2025-10-08 01:40:00 | GOES-19 | RIO PARDO DE MINAS | MINAS GERAIS | Brasil | 3155603 | 31 | 33 | nan | nan | nan | Mata Atlântica | 111.9 |
| f0dc975b-87e5-3d6c-93c1-bdab9ecb16ba | -6.1299 | -47.2884 | 2025-10-08 01:40:00 | GOES-19 | CAMPESTRE DO MARANHÃO | MARANHÃO | Brasil | 2102556 | 21 | 33 | nan | nan | nan | Cerrado | 97.2 |
| 1aa04403-2925-3d33-bb95-1d9e54987123 | -7.017 | -42.8762 | 2025-10-08 01:40:00 | GOES-19 | FLORIANO | PIAUÍ | Brasil | 2203909 | 22 | 33 | nan | nan | nan | Caatinga | 204.6 |
| 11262dfe-f908-3abc-bd6a-f2f03853feef | -15.6393 | -52.5688 | 2025-10-08 01:40:00 | GOES-19 | BARRA DO GARÇAS | MATO GROSSO | Brasil | 5101803 | 51 | 33 | nan | nan | nan | Cerrado | 73.4 |
| cf441d9e-e05c-315c-87d4-a234869c1847 | -11.6888 | -50.9833 | 2025-10-08 01:40:00 | GOES-19 | SÃO FÉLIX DO ARAGUAIA | MATO GROSSO | Brasil | 5107859 | 51 | 33 | nan | nan | nan | Cerrado | 147.1 |
| d15d44ca-89ed-3e8f-8682-981658715435 | -15.937 | -42.592 | 2025-10-08 01:40:00 | GOES-19 | RIO PARDO DE MINAS | MINAS GERAIS | Brasil | 3155603 | 31 | 33 | nan | nan | nan | Mata Atlântica | 58.0 |
| fb6f7144-02a8-36e9-a980-ba1e5f9c9ef1 | -7.0167 | -42.8998 | 2025-10-08 01:40:00 | GOES-19 | FLORIANO | PIAUÍ | Brasil | 2203909 | 22 | 33 | nan | nan | nan | Caatinga | 120.6 |
| 0a09b802-0e67-34f9-8d85-38ce527a0b24 | -6.9982 | -42.878 | 2025-10-08 01:40:00 | GOES-19 | FLORIANO | PIAUÍ | Brasil | 2203909 | 22 | 33 | nan | nan | nan | Caatinga | 89.9 |
| cbc977e3-db91-3678-a461-0025510d123a | -7.5874 | -64.5097 | 2025-10-08 01:40:00 | GOES-19 | LÁBREA | AMAZONAS | Brasil | 1302405 | 13 | 33 | nan | nan | nan | Amazônia | 52.2 |
| fea6561e-c048-3834-aba4-4f9f1610f51a | -11.1833 | -54.8787 | 2025-10-08 01:40:00 | GOES-19 | NOVA SANTA HELENA | MATO GROSSO | Brasil | 5106190 | 51 | 33 | nan | nan | nan | Amazônia | 262.1 |
| e8771162-da23-3a15-9bdf-57a45d0afb1e | -9.1907 | -46.9104 | 2025-10-08 01:40:00 | GOES-19 | LIZARDA | TOCANTINS | Brasil | 1712405 | 17 | 33 | nan | nan | nan | Cerrado | 80.1 |
| b73c095e-ace1-3b86-bbbc-31466f325f5d | -9.6108 | -40.3171 | 2025-10-08 01:40:00 | GOES-19 | JUAZEIRO | BAHIA | Brasil | 2918407 | 29 | 33 | nan | nan | nan | Caatinga | 67.4 |
| 5509074b-55cb-38d8-910b-06d59447a55d | -11.1642 | -54.9007 | 2025-10-08 01:40:00 | GOES-19 | NOVA SANTA HELENA | MATO GROSSO | Brasil | 5106190 | 51 | 33 | nan | nan | nan | Amazônia | 104.6 |
| eae2afbb-323d-3a44-a910-d4b2eee8b711 | -4.4978 | -46.3509 | 2025-10-08 01:40:00 | GOES-19 | BURITICUPU | MARANHÃO | Brasil | 2102325 | 21 | 33 | nan | nan | nan | Amazônia | 72.8 |
| e689c063-f2d5-3036-b59c-ff346c2ec7ec | -5.1416 | -44.9443 | 2025-10-08 01:40:00 | GOES-19 | BARRA DO CORDA | MARANHÃO | Brasil | 2101608 | 21 | 33 | nan | nan | nan | Cerrado | 97.4 |
| 6903a72f-281b-3d73-afb8-0226e72c88d5 | -11.7076 | -51.0024 | 2025-10-08 01:40:00 | GOES-19 | SÃO FÉLIX DO ARAGUAIA | MATO GROSSO | Brasil | 5107859 | 51 | 33 | nan | nan | nan | Cerrado | 99.2 |
| 3cfea8cc-dd2a-3164-a2db-03b8dd1f40ea | -9.6104 | -40.342 | 2025-10-08 01:40:00 | GOES-19 | JUAZEIRO | BAHIA | Brasil | 2918407 | 29 | 33 | nan | nan | nan | Caatinga | 86.5 |
| e1fd229d-8010-33b8-b584-935800d7307d | -5.1414 | -44.967 | 2025-10-08 01:40:00 | GOES-19 | BARRA DO CORDA | MARANHÃO | Brasil | 2101608 | 21 | 33 | nan | nan | nan | Cerrado | 225.2 |
| 12faac6e-997d-3eb4-bee1-877ca637f5a1 | -15.9562 | -42.6123 | 2025-10-08 01:40:00 | GOES-19 | FRUTA DE LEITE | MINAS GERAIS | Brasil | 3127073 | 31 | 33 | nan | nan | nan | Mata Atlântica | 80.8 |
| b8ee2784-1ad8-3c70-a6f0-4f71f2a9dc4d | -11.183 | -54.8991 | 2025-10-08 01:40:00 | GOES-19 | NOVA SANTA HELENA | MATO GROSSO | Brasil | 5106190 | 51 | 33 | nan | nan | nan | Amazônia | 161.8 |
| 66d0abd2-9769-3f73-ae32-3d001dc0aeed | -5.1227 | -44.9682 | 2025-10-08 01:40:00 | GOES-19 | BARRA DO CORDA | MARANHÃO | Brasil | 2101608 | 21 | 33 | nan | nan | nan | Cerrado | 114.4 |
| 1d96da72-7bcd-3a24-8e06-49548c7b7f23 | -5.2601 | -44.1368 | 2025-10-08 01:40:00 | GOES-19 | GOVERNADOR EUGÊNIO BARROS | MARANHÃO | Brasil | 2104602 | 21 | 33 | nan | nan | nan | Cerrado | 70.7 |
| 8eafac72-b74b-32d6-98c3-cd95c4681001 | -11.1646 | -54.86 | 2025-10-08 01:40:00 | GOES-19 | NOVA SANTA HELENA | MATO GROSSO | Brasil | 5106190 | 51 | 33 | nan | nan | nan | Amazônia | 82.5 |
| 9f410eba-b456-3366-a437-981aa79247ac | -12.3971 | -63.8811 | 2025-10-08 01:40:00 | GOES-19 | COSTA MARQUES | RONDÔNIA | Brasil | 1100080 | 11 | 33 | nan | nan | nan | Amazônia | 56.7 |
| bf0df701-dcf0-37be-939b-e7ad09c3c0e8 | -4.6873 | -45.8504 | 2025-10-08 01:40:00 | GOES-19 | MARAJÁ DO SENA | MARANHÃO | Brasil | 2106359 | 21 | 33 | nan | nan | nan | Amazônia | 73.2 |
| c2e3c952-58dc-3b7a-b4b3-d285017541d6 | -11.4531 | -50.2195 | 2025-10-08 01:40:00 | GOES-19 | LAGOA DA CONFUSÃO | TOCANTINS | Brasil | 1711902 | 17 | 33 | nan | nan | nan | Cerrado | 82.2 |
| d9a6bd6a-405a-3506-a3e2-6df643b9d661 | -7.6474 | -63.4584 | 2025-10-08 01:40:00 | GOES-19 | CANUTAMA | AMAZONAS | Brasil | 1300904 | 13 | 33 | nan | nan | nan | Amazônia | 64.6 |
| 36f533c7-b6a3-36ef-b7d7-147c38050675 | -11.1455 | -54.882 | 2025-10-08 01:40:00 | GOES-19 | NOVA SANTA HELENA | MATO GROSSO | Brasil | 5106190 | 51 | 33 | nan | nan | nan | Amazônia | 115.8 |
| 9ba393c8-1ee4-30da-9edc-8364df979944 | -4.6875 | -45.828 | 2025-10-08 01:40:00 | GOES-19 | MARAJÁ DO SENA | MARANHÃO | Brasil | 2106359 | 21 | 33 | nan | nan | nan | Amazônia | 69.6 |
| f6d5431e-c851-3671-a1d0-880adfada6cc | -11.1644 | -54.8804 | 2025-10-08 01:40:00 | GOES-19 | NOVA SANTA HELENA | MATO GROSSO | Brasil | 5106190 | 51 | 33 | nan | nan | nan | Amazônia | 213.4 |
| 7113e612-3bc7-36d7-98fd-b2a441e6b1c3 | -11.7079 | -50.9811 | 2025-10-08 01:40:00 | GOES-19 | SÃO FÉLIX DO ARAGUAIA | MATO GROSSO | Brasil | 5107859 | 51 | 33 | nan | nan | nan | Cerrado | 194.6 |
| ff83f649-d242-3ca2-8603-0573696dbd03 | -9.6295 | -40.3392 | 2025-10-08 01:40:00 | GOES-19 | JUAZEIRO | BAHIA | Brasil | 2918407 | 29 | 33 | nan | nan | nan | Caatinga | 60.1 |
| 1ef5158c-4a37-3f24-a908-f87c537c506a | -11.3684 | -55.1875 | 2025-10-08 01:40:00 | GOES-19 | CLÁUDIA | MATO GROSSO | Brasil | 5103056 | 51 | 33 | nan | nan | nan | Amazônia | 79.2 |
| fe067a38-ad32-341b-85a2-64f6fedebe43 | -6.1485 | -47.2871 | 2025-10-08 01:40:00 | GOES-19 | CAMPESTRE DO MARANHÃO | MARANHÃO | Brasil | 2102556 | 21 | 33 | nan | nan | nan | Cerrado | 62.3 |
| 78d07e14-0f46-34ec-967d-5ff4f924857f | -7.0359 | -42.8744 | 2025-10-08 01:40:00 | GOES-19 | NAZARÉ DO PIAUÍ | PIAUÍ | Brasil | 2206704 | 22 | 33 | nan | nan | nan | Caatinga | 98.3 |
| e9ba1a8a-ec27-32a0-b6be-37c0675f511e | -4.5331 | -43.9067 | 2025-10-08 01:40:00 | GOES-19 | CODÓ | MARANHÃO | Brasil | 2103307 | 21 | 33 | nan | nan | nan | Cerrado | 37.4 |
| cccf1db8-16dc-3225-aad2-79165c4ed6cd | -9.6104 | -40.342 | 2025-10-08 01:50:00 | GOES-19 | JUAZEIRO | BAHIA | Brasil | 2918407 | 29 | 33 | nan | nan | nan | Caatinga | 59.8 |
| a74a0b74-0d13-3ae5-8235-b8e21ea508ea | -11.6888 | -50.9833 | 2025-10-08 01:50:00 | GOES-19 | SÃO FÉLIX DO ARAGUAIA | MATO GROSSO | Brasil | 5107859 | 51 | 33 | nan | nan | nan | Cerrado | 103.4 |
| 1daea52c-b14c-345a-babe-1ffad5fd517b | -7.017 | -42.8762 | 2025-10-08 01:50:00 | GOES-19 | FLORIANO | PIAUÍ | Brasil | 2203909 | 22 | 33 | nan | nan | nan | Caatinga | 164.9 |
| f70212cd-5741-3a5d-ac42-18b3882b8d89 | -6.9982 | -42.878 | 2025-10-08 01:50:00 | GOES-19 | FLORIANO | PIAUÍ | Brasil | 2203909 | 22 | 33 | nan | nan | nan | Caatinga | 86.4 |
| 74137e92-16f8-35e2-83be-e3f47e67281c | -7.0359 | -42.8744 | 2025-10-08 01:50:00 | GOES-19 | NAZARÉ DO PIAUÍ | PIAUÍ | Brasil | 2206704 | 22 | 33 | nan | nan | nan | Caatinga | 81.8 |
| 9bc1fee4-9f5e-3aa6-a75d-61b3b8819dfc | -11.7079 | -50.9811 | 2025-10-08 01:50:00 | GOES-19 | SÃO FÉLIX DO ARAGUAIA | MATO GROSSO | Brasil | 5107859 | 51 | 33 | nan | nan | nan | Cerrado | 192.1 |
| dd67acc6-b52c-392b-bc43-f8b0f71965ff | -4.6873 | -45.8504 | 2025-10-08 01:50:00 | GOES-19 | MARAJÁ DO SENA | MARANHÃO | Brasil | 2106359 | 21 | 33 | nan | nan | nan | Amazônia | 67.4 |
| 37025a4a-543b-397b-98cd-49db48712f18 | -17.284 | -42.6479 | 2025-10-08 01:50:00 | GOES-19 | MINAS NOVAS | MINAS GERAIS | Brasil | 3141801 | 31 | 33 | nan | nan | nan | Cerrado | 379.4 |
| a8f826cc-397b-35b2-8fea-4335a82e7a7f | -12.3971 | -63.8811 | 2025-10-08 01:50:00 | GOES-19 | COSTA MARQUES | RONDÔNIA | Brasil | 1100080 | 11 | 33 | nan | nan | nan | Amazônia | 58.8 |
| ad1fa53e-f831-33f7-aaed-a5387402a106 | -11.1455 | -54.882 | 2025-10-08 01:50:00 | GOES-19 | NOVA SANTA HELENA | MATO GROSSO | Brasil | 5106190 | 51 | 33 | nan | nan | nan | Amazônia | 103.5 |
| 9a5bbe74-c60e-3a10-8a63-efb5727c531a | -7.5874 | -64.5097 | 2025-10-08 01:50:00 | GOES-19 | LÁBREA | AMAZONAS | Brasil | 1302405 | 13 | 33 | nan | nan | nan | Amazônia | 58.5 |
| 038116f2-eafa-3130-b8df-d002820f0141 | -11.1646 | -54.86 | 2025-10-08 01:50:00 | GOES-19 | NOVA SANTA HELENA | MATO GROSSO | Brasil | 5106190 | 51 | 33 | nan | nan | nan | Amazônia | 81.9 |
| 1f6c9c93-c38d-327a-964c-195c0dfd21d7 | -11.7082 | -50.9598 | 2025-10-08 01:50:00 | GOES-19 | SÃO FÉLIX DO ARAGUAIA | MATO GROSSO | Brasil | 5107859 | 51 | 33 | nan | nan | nan | Cerrado | 96.0 |
| a5f06688-8e31-3760-8a25-cf4b04150128 | -19.514 | -44.0768 | 2025-10-08 01:50:00 | GOES-19 | MATOZINHOS | MINAS GERAIS | Brasil | 3141108 | 31 | 33 | nan | nan | nan | Cerrado | 75.2 |
| 5633fd22-a06d-3484-b52f-06770f8b3df9 | -15.9568 | -42.5876 | 2025-10-08 01:50:00 | GOES-19 | RIO PARDO DE MINAS | MINAS GERAIS | Brasil | 3155603 | 31 | 33 | nan | nan | nan | Mata Atlântica | 160.7 |
| bc0e154e-d8f0-3a51-bbf5-1a161a65e2dd | -11.1642 | -54.9007 | 2025-10-08 01:50:00 | GOES-19 | NOVA SANTA HELENA | MATO GROSSO | Brasil | 5106190 | 51 | 33 | nan | nan | nan | Amazônia | 106.2 |
| 757326e6-51d8-3096-b3c7-16d3fdc62a92 | -9.6108 | -40.3171 | 2025-10-08 01:50:00 | GOES-19 | JUAZEIRO | BAHIA | Brasil | 2918407 | 29 | 33 | nan | nan | nan | Caatinga | 69.4 |
| aa3a1243-2733-3384-a62b-3b452a70ee2e | -11.1833 | -54.8787 | 2025-10-08 01:50:00 | GOES-19 | NOVA SANTA HELENA | MATO GROSSO | Brasil | 5106190 | 51 | 33 | nan | nan | nan | Amazônia | 223.7 |
| b294bddc-3f09-372d-8dfb-c81e6f3dfef0 | -15.9562 | -42.6123 | 2025-10-08 01:50:00 | GOES-19 | FRUTA DE LEITE | MINAS GERAIS | Brasil | 3127073 | 31 | 33 | nan | nan | nan | Mata Atlântica | 109.1 |
| 749114d3-2eec-3673-a493-276fa7f580ab | -17.2639 | -42.6527 | 2025-10-08 01:50:00 | GOES-19 | MINAS NOVAS | MINAS GERAIS | Brasil | 3141801 | 31 | 33 | nan | nan | nan | Cerrado | 100.3 |
| 40ae1aad-d92f-3dec-a082-f5b80c4dd7a1 | -4.6875 | -45.828 | 2025-10-08 01:50:00 | GOES-19 | MARAJÁ DO SENA | MARANHÃO | Brasil | 2106359 | 21 | 33 | nan | nan | nan | Amazônia | 72.7 |
| ff5a0c15-6724-334b-86ae-d5a3ad4551fb | -4.4978 | -46.3509 | 2025-10-08 01:50:00 | GOES-19 | BURITICUPU | MARANHÃO | Brasil | 2102325 | 21 | 33 | nan | nan | nan | Amazônia | 82.7 |
| 48798441-22b2-3c80-b544-57a318c54c99 | -5.1414 | -44.967 | 2025-10-08 01:50:00 | GOES-19 | BARRA DO CORDA | MARANHÃO | Brasil | 2101608 | 21 | 33 | nan | nan | nan | Cerrado | 177.7 |
| 50990330-8b34-37d8-95b6-7b54326f857a | -5.1227 | -44.9682 | 2025-10-08 01:50:00 | GOES-19 | BARRA DO CORDA | MARANHÃO | Brasil | 2101608 | 21 | 33 | nan | nan | nan | Cerrado | 108.5 |
| bc5bc37e-81a4-33c5-9646-64f70363264b | -7.0167 | -42.8998 | 2025-10-08 01:50:00 | GOES-19 | FLORIANO | PIAUÍ | Brasil | 2203909 | 22 | 33 | nan | nan | nan | Caatinga | 118.5 |
| 5e26784e-2777-3212-ac0c-fe1ae42b455e | -15.937 | -42.592 | 2025-10-08 01:50:00 | GOES-19 | RIO PARDO DE MINAS | MINAS GERAIS | Brasil | 3155603 | 31 | 33 | nan | nan | nan | Mata Atlântica | 69.1 |
| ca4962d2-919b-3dd5-80b0-bad5a6f7d9fe | -17.3041 | -42.643 | 2025-10-08 01:50:00 | GOES-19 | MINAS NOVAS | MINAS GERAIS | Brasil | 3141801 | 31 | 33 | nan | nan | nan | Cerrado | 208.7 |
| 70fb855f-3ea6-3fc6-b2c1-14df5c5edec1 | -5.1416 | -44.9443 | 2025-10-08 01:50:00 | GOES-19 | BARRA DO CORDA | MARANHÃO | Brasil | 2101608 | 21 | 33 | nan | nan | nan | Cerrado | 88.9 |
| 40df39cd-b38a-3dfa-b104-95acf4ad5bb1 | -11.1644 | -54.8804 | 2025-10-08 01:50:00 | GOES-19 | NOVA SANTA HELENA | MATO GROSSO | Brasil | 5106190 | 51 | 33 | nan | nan | nan | Amazônia | 186.9 |
| b20e5f91-6a03-3291-be09-eef5ff52f263 | -11.183 | -54.8991 | 2025-10-08 01:50:00 | GOES-19 | NOVA SANTA HELENA | MATO GROSSO | Brasil | 5106190 | 51 | 33 | nan | nan | nan | Amazônia | 165.7 |
| 2a433b7d-50f5-334f-9918-f89da0775277 | -20.5056 | -46.9936 | 2025-10-08 01:50:00 | GOES-19 | CÁSSIA | MINAS GERAIS | Brasil | 3115102 | 31 | 33 | nan | nan | nan | Cerrado | 64.4 |
| 3e5d69ec-9d3a-3dfa-939b-00a7ab515d43 | -17.2847 | -42.623 | 2025-10-08 01:50:00 | GOES-19 | MINAS NOVAS | MINAS GERAIS | Brasil | 3141801 | 31 | 33 | nan | nan | nan | Cerrado | 94.3 |
| 077d83a0-9efb-31e5-a203-3f7c0520ac62 | -5.2601 | -44.1368 | 2025-10-08 01:50:00 | GOES-19 | GOVERNADOR EUGÊNIO BARROS | MARANHÃO | Brasil | 2104602 | 21 | 33 | nan | nan | nan | Cerrado | 118.0 |
| f211d4f6-8661-3160-b9a0-872c9d148429 | -11.1642 | -54.9007 | 2025-10-08 02:00:00 | GOES-19 | NOVA SANTA HELENA | MATO GROSSO | Brasil | 5106190 | 51 | 33 | nan | nan | nan | Amazônia | 86.8 |
| 806d353a-a2d4-3bc8-b64a-b941698fb6dd | -5.1416 | -44.9443 | 2025-10-08 02:00:00 | GOES-19 | BARRA DO CORDA | MARANHÃO | Brasil | 2101608 | 21 | 33 | nan | nan | nan | Cerrado | 72.8 |
| ef489ca5-5743-3169-9ad4-349b6ff4bf0c | -4.5331 | -43.9067 | 2025-10-08 02:00:00 | GOES-19 | CODÓ | MARANHÃO | Brasil | 2103307 | 21 | 33 | nan | nan | nan | Cerrado | 56.2 |
| c4a0c21b-f1c8-3645-b832-0b463517bc93 | -17.2639 | -42.6527 | 2025-10-08 02:00:00 | GOES-19 | MINAS NOVAS | MINAS GERAIS | Brasil | 3141801 | 31 | 33 | nan | nan | nan | Cerrado | 72.5 |
| 96201a29-01dd-37ec-a04a-8df3858c8a3b | -11.1646 | -54.86 | 2025-10-08 02:00:00 | GOES-19 | NOVA SANTA HELENA | MATO GROSSO | Brasil | 5106190 | 51 | 33 | nan | nan | nan | Amazônia | 77.3 |
| 42a82243-0865-3f7b-a725-ed02410b9f48 | -11.7079 | -50.9811 | 2025-10-08 02:00:00 | GOES-19 | SÃO FÉLIX DO ARAGUAIA | MATO GROSSO | Brasil | 5107859 | 51 | 33 | nan | nan | nan | Cerrado | 178.6 |
| 59b240e9-004e-3937-ba60-9f3708628a33 | -15.9568 | -42.5876 | 2025-10-08 02:00:00 | GOES-19 | RIO PARDO DE MINAS | MINAS GERAIS | Brasil | 3155603 | 31 | 33 | nan | nan | nan | Mata Atlântica | 89.2 |
| bbcac472-68f3-3fdc-b51e-faf4dcf8f07a | -17.284 | -42.6479 | 2025-10-08 02:00:00 | GOES-19 | MINAS NOVAS | MINAS GERAIS | Brasil | 3141801 | 31 | 33 | nan | nan | nan | Cerrado | 307.9 |
| df7b36a8-3605-313a-b0a6-357149aacab8 | -7.0359 | -42.8744 | 2025-10-08 02:00:00 | GOES-19 | NAZARÉ DO PIAUÍ | PIAUÍ | Brasil | 2206704 | 22 | 33 | nan | nan | nan | Caatinga | 77.4 |
| 22db6226-de97-3b71-ae08-6bbd600df3be | -7.0167 | -42.8998 | 2025-10-08 02:00:00 | GOES-19 | FLORIANO | PIAUÍ | Brasil | 2203909 | 22 | 33 | nan | nan | nan | Caatinga | 96.6 |
| 73c9f286-9502-33fc-a5e5-95fa70e15674 | -7.5874 | -64.5097 | 2025-10-08 02:00:00 | GOES-19 | LÁBREA | AMAZONAS | Brasil | 1302405 | 13 | 33 | nan | nan | nan | Amazônia | 55.6 |
| f9c6252a-d207-380c-83dc-21a77fa7e570 | -7.017 | -42.8762 | 2025-10-08 02:00:00 | GOES-19 | FLORIANO | PIAUÍ | Brasil | 2203909 | 22 | 33 | nan | nan | nan | Caatinga | 158.5 |
| ae1ca40d-27de-327d-aedd-af97135cb868 | -19.5148 | -44.0522 | 2025-10-08 02:00:00 | GOES-19 | MATOZINHOS | MINAS GERAIS | Brasil | 3141108 | 31 | 33 | nan | nan | nan | Cerrado | 85.5 |
| 708bac6d-c44b-3a12-b466-134b13e70202 | -4.4978 | -46.3509 | 2025-10-08 02:00:00 | GOES-19 | BURITICUPU | MARANHÃO | Brasil | 2102325 | 21 | 33 | nan | nan | nan | Amazônia | 76.7 |
| 6fe8a5ee-bc68-3992-b1ef-f0ed9268306a | -11.1455 | -54.882 | 2025-10-08 02:00:00 | GOES-19 | NOVA SANTA HELENA | MATO GROSSO | Brasil | 5106190 | 51 | 33 | nan | nan | nan | Amazônia | 104.1 |
| e40858e2-576b-3f66-ae16-c699da985538 | -19.514 | -44.0768 | 2025-10-08 02:00:00 | GOES-19 | MATOZINHOS | MINAS GERAIS | Brasil | 3141108 | 31 | 33 | nan | nan | nan | Cerrado | 109.9 |
| 053ad55e-3aa9-317a-a020-6937ed1b26bc | -11.7082 | -50.9598 | 2025-10-08 02:00:00 | GOES-19 | SÃO FÉLIX DO ARAGUAIA | MATO GROSSO | Brasil | 5107859 | 51 | 33 | nan | nan | nan | Cerrado | 87.0 |
| 225ab68b-cf24-35b0-bba1-0b4b1978910b | -11.183 | -54.8991 | 2025-10-08 02:00:00 | GOES-19 | NOVA SANTA HELENA | MATO GROSSO | Brasil | 5106190 | 51 | 33 | nan | nan | nan | Amazônia | 149.9 |
| c07cc0b9-4df6-3bda-9aaa-5e2542e30944 | -11.1644 | -54.8804 | 2025-10-08 02:00:00 | GOES-19 | NOVA SANTA HELENA | MATO GROSSO | Brasil | 5106190 | 51 | 33 | nan | nan | nan | Amazônia | 182.6 |
| 7f9de402-2a28-3c75-950e-4a073b2ecc53 | -6.9982 | -42.878 | 2025-10-08 02:00:00 | GOES-19 | FLORIANO | PIAUÍ | Brasil | 2203909 | 22 | 33 | nan | nan | nan | Caatinga | 84.4 |
| cd12fb00-e841-3884-ab1d-6685ad252fe0 | -5.2601 | -44.1368 | 2025-10-08 02:00:00 | GOES-19 | GOVERNADOR EUGÊNIO BARROS | MARANHÃO | Brasil | 2104602 | 21 | 33 | nan | nan | nan | Cerrado | 94.1 |
| bc035cb0-46a9-37f8-8f6c-2b5465f6ca46 | -5.1414 | -44.967 | 2025-10-08 02:00:00 | GOES-19 | BARRA DO CORDA | MARANHÃO | Brasil | 2101608 | 21 | 33 | nan | nan | nan | Cerrado | 181.8 |


[Clique aqui para ver as próximas entradas](README11.md)
