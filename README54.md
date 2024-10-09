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

## Dados Diários - Página 54

| ID | Latitude | Longitude | Data/Hora GMT | Satélite | Município | Estado | País | Município ID | Estado ID | País ID | Dias sem Chuva | Precipitação | Risco de Fogo | Bioma | FRP |
|----|----------|-----------|---------------|----------|-----------|--------|------|--------------|-----------|---------|----------------|--------------|----------------|-------|-----|
| b3bde1e6-7089-3876-bcf6-2f8d5b5502ba | -10.8754 | -63.9169 | 2024-10-09 02:36:08 | GOES-16 | GUAJARÁ-MIRIM | RONDÔNIA | Brasil | 1100106 | 11 | 33 | nan | nan | nan | Amazônia | 89.6 |
| 5d3be515-b17f-3cfa-b2ab-429fe520ee2d | -10.8755 | -63.8979 | 2024-10-09 02:36:08 | GOES-16 | GUAJARÁ-MIRIM | RONDÔNIA | Brasil | 1100106 | 11 | 33 | nan | nan | nan | Amazônia | 74.1 |
| 52057302-d3cb-32fc-be0a-6503493c9424 | -10.8941 | -63.916 | 2024-10-09 02:36:09 | GOES-16 | GUAJARÁ-MIRIM | RONDÔNIA | Brasil | 1100106 | 11 | 33 | nan | nan | nan | Amazônia | 59.3 |
| b03352dc-543c-3294-8a8a-4e0c04624471 | -11.2771 | -60.3873 | 2024-10-09 02:36:11 | GOES-16 | VILHENA | RONDÔNIA | Brasil | 1100304 | 11 | 33 | nan | nan | nan | Amazônia | 48.9 |
| e8d38626-3b72-32db-8940-19d505aa4c98 | -11.5233 | -65.137 | 2024-10-09 02:36:12 | GOES-16 | GUAJARÁ-MIRIM | RONDÔNIA | Brasil | 1100106 | 11 | 33 | nan | nan | nan | Amazônia | 54.1 |
| 4aade724-0f59-3aae-a5c5-562c307d2ac0 | -11.6806 | -64.0312 | 2024-10-09 02:36:13 | GOES-16 | GUAJARÁ-MIRIM | RONDÔNIA | Brasil | 1100106 | 11 | 33 | nan | nan | nan | Amazônia | 64.0 |
| 012fcea1-295a-32be-bdce-00a97e6d25ff | -11.693 | -65.0163 | 2024-10-09 02:36:13 | GOES-16 | GUAJARÁ-MIRIM | RONDÔNIA | Brasil | 1100106 | 11 | 33 | nan | nan | nan | Amazônia | 99.8 |
| b9f33730-15bc-3e05-9335-ed81b6202339 | -11.6931 | -64.9974 | 2024-10-09 02:36:13 | GOES-16 | GUAJARÁ-MIRIM | RONDÔNIA | Brasil | 1100106 | 11 | 33 | nan | nan | nan | Amazônia | 76.5 |
| f8d2bea8-9f01-352f-8b19-02d9d1584611 | -11.7117 | -65.0155 | 2024-10-09 02:36:13 | GOES-16 | GUAJARÁ-MIRIM | RONDÔNIA | Brasil | 1100106 | 11 | 33 | nan | nan | nan | Amazônia | 99.5 |
| 23357e99-c632-3643-916b-5dfe750d5aec | -11.7119 | -64.9966 | 2024-10-09 02:36:13 | GOES-16 | GUAJARÁ-MIRIM | RONDÔNIA | Brasil | 1100106 | 11 | 33 | nan | nan | nan | Amazônia | 75.6 |
| 99dfa5ab-8163-3caa-bad3-769f592e5f02 | -12.6676 | -63.0819 | 2024-10-09 02:36:18 | GOES-16 | SÃO FRANCISCO DO GUAPORÉ | RONDÔNIA | Brasil | 1101492 | 11 | 33 | nan | nan | nan | Amazônia | 62.6 |
| 1cb78c2c-9b74-3d64-9631-90c4935f5d42 | -12.878 | -62.8007 | 2024-10-09 02:36:20 | GOES-16 | ALTA FLORESTA D'OESTE | RONDÔNIA | Brasil | 1100015 | 11 | 33 | nan | nan | nan | Amazônia | 108.2 |
| 8618a45b-ab06-35d8-aebb-5b939cfd20df | -12.9756 | -62.4673 | 2024-10-09 02:36:20 | GOES-16 | ALTA FLORESTA D'OESTE | RONDÔNIA | Brasil | 1100015 | 11 | 33 | nan | nan | nan | Amazônia | 73.0 |
| f7ecc46f-05f8-3464-9279-577daea47e68 | -13.817 | -44.5961 | 2024-10-09 02:36:23 | GOES-16 | CORIBE | BAHIA | Brasil | 2909109 | 29 | 33 | nan | nan | nan | Cerrado | 243.3 |
| bef758dd-52f8-38e0-b205-ca000c4242e4 | -13.8175 | -44.5726 | 2024-10-09 02:36:23 | GOES-16 | CORIBE | BAHIA | Brasil | 2909109 | 29 | 33 | nan | nan | nan | Cerrado | 81.0 |
| 9ec8d164-c9f2-348c-b6c2-4b476b611ea0 | -13.8364 | -44.5927 | 2024-10-09 02:36:23 | GOES-16 | CORIBE | BAHIA | Brasil | 2909109 | 29 | 33 | nan | nan | nan | Cerrado | 170.5 |
| 2867581a-a5a2-3c75-954a-bef03753bd9a | -13.8369 | -44.5691 | 2024-10-09 02:36:23 | GOES-16 | CORIBE | BAHIA | Brasil | 2909109 | 29 | 33 | nan | nan | nan | Cerrado | 182.1 |
| 7b89d25d-ffab-34ff-85f5-779b2a844700 | -13.8564 | -44.5657 | 2024-10-09 02:36:24 | GOES-16 | CORIBE | BAHIA | Brasil | 2909109 | 29 | 33 | nan | nan | nan | Cerrado | 103.3 |
| bd54ef87-7186-3670-a017-5dfc0887eb6d | -15.7076 | -59.3726 | 2024-10-09 02:36:35 | GOES-16 | PONTES E LACERDA | MATO GROSSO | Brasil | 5106752 | 51 | 33 | nan | nan | nan | Amazônia | 59.2 |
| 6848a42e-5a78-36ff-9c6b-339af9d9c920 | -16.4184 | -55.9455 | 2024-10-09 02:36:39 | GOES-16 | BARÃO DE MELGAÇO | MATO GROSSO | Brasil | 5101605 | 51 | 33 | nan | nan | nan | Pantanal | 86.0 |
| c4de2f64-ea25-39e1-9bb8-08e522c5d936 | -17.0623 | -56.0308 | 2024-10-09 02:36:42 | GOES-16 | BARÃO DE MELGAÇO | MATO GROSSO | Brasil | 5101605 | 51 | 33 | nan | nan | nan | Pantanal | 100.9 |
| 59f120b8-8c48-39d0-81ed-bf826eb07f0e | -17.1467 | -56.8463 | 2024-10-09 02:36:43 | GOES-16 | POCONÉ | MATO GROSSO | Brasil | 5106505 | 51 | 33 | nan | nan | nan | Pantanal | 81.4 |
| 83ef735d-523a-335c-a67d-78f7cfe81f90 | -17.1588 | -56.1222 | 2024-10-09 02:36:43 | GOES-16 | BARÃO DE MELGAÇO | MATO GROSSO | Brasil | 5101605 | 51 | 33 | nan | nan | nan | Pantanal | 95.6 |
| 8509b979-2b7f-3c73-a631-c8854e8bbd63 | -17.335 | -55.0366 | 2024-10-09 02:36:43 | GOES-16 | ITIQUIRA | MATO GROSSO | Brasil | 5104609 | 51 | 33 | nan | nan | nan | Pantanal | 85.0 |
| 394e0259-0c3a-3530-acdd-e2e7dabca333 | -17.3353 | -55.0156 | 2024-10-09 02:36:43 | GOES-16 | ITIQUIRA | MATO GROSSO | Brasil | 5104609 | 51 | 33 | nan | nan | nan | Pantanal | 65.3 |
| 45d9fdca-bf6a-3456-b0de-626f66e2572d | -17.3547 | -55.0339 | 2024-10-09 02:36:44 | GOES-16 | ITIQUIRA | MATO GROSSO | Brasil | 5104609 | 51 | 33 | nan | nan | nan | Pantanal | 97.9 |
| b4946388-ae43-37f0-b69c-8dcda7115ac8 | -17.3551 | -55.0129 | 2024-10-09 02:36:44 | GOES-16 | ITIQUIRA | MATO GROSSO | Brasil | 5104609 | 51 | 33 | nan | nan | nan | Pantanal | 81.5 |
| e61e6536-ddae-3888-aed5-b5b073cf00f6 | -18.5993 | -57.2629 | 2024-10-09 02:36:50 | GOES-16 | CORUMBÁ | MATO GROSSO DO SUL | Brasil | 5003207 | 50 | 33 | nan | nan | nan | Pantanal | 56.6 |
| c1a86111-984c-354d-ba5a-9234fcfce388 | -18.5996 | -57.2422 | 2024-10-09 02:36:50 | GOES-16 | CORUMBÁ | MATO GROSSO DO SUL | Brasil | 5003207 | 50 | 33 | nan | nan | nan | Pantanal | 60.2 |
| d93f6abb-938e-34cd-8c75-df513a8005fb | -20.0122 | -42.4541 | 2024-10-09 02:36:56 | GOES-16 | RAUL SOARES | MINAS GERAIS | Brasil | 3154002 | 31 | 33 | nan | nan | nan | Mata Atlântica | 98.1 |
| 6edaf5b8-4628-3de8-ba16-2f6e967b8d98 | -20.013 | -42.4287 | 2024-10-09 02:36:56 | GOES-16 | RAUL SOARES | MINAS GERAIS | Brasil | 3154002 | 31 | 33 | nan | nan | nan | Mata Atlântica | 105.2 |
| 9f71f24f-295b-3d1c-8fa1-f38c0ebb099e | -20.3352 | -48.7076 | 2024-10-09 02:36:59 | GOES-16 | COLÔMBIA | SÃO PAULO | Brasil | 3512100 | 35 | 33 | nan | nan | nan | Cerrado | 158.2 |
| 6ea3dfd1-5e70-3606-98f1-796d0b455d7e | -20.3346 | -48.7307 | 2024-10-09 02:36:59 | GOES-16 | COLÔMBIA | SÃO PAULO | Brasil | 3512100 | 35 | 33 | nan | nan | nan | Cerrado | 229.1 |
| 521bcbde-0180-3a9b-99a7-c5a901b28095 | -20.3513 | -48.8648 | 2024-10-09 02:36:59 | GOES-16 | COLÔMBIA | SÃO PAULO | Brasil | 3512100 | 35 | 33 | nan | nan | nan | Cerrado | 111.0 |
| a6cbbab5-e79a-34c2-8161-0a9cf79179f6 | -20.3551 | -48.7262 | 2024-10-09 02:36:59 | GOES-16 | COLÔMBIA | SÃO PAULO | Brasil | 3512100 | 35 | 33 | nan | nan | nan | Cerrado | 191.0 |
| 21232502-cd60-3ff8-a68c-9dac1626fd7c | -20.3557 | -48.7031 | 2024-10-09 02:36:59 | GOES-16 | COLÔMBIA | SÃO PAULO | Brasil | 3512100 | 35 | 33 | nan | nan | nan | Cerrado | 127.3 |
| 285864b1-16d1-3323-9368-28066bec5ba8 | -21.0926 | -47.2043 | 2024-10-09 02:37:02 | GOES-16 | SANTO ANTÔNIO DA ALEGRIA | SÃO PAULO | Brasil | 3547908 | 35 | 33 | nan | nan | nan | Cerrado | 75.2 |
| d8e380c2-0b97-32eb-bfe6-62148e8cc564 | -21.572 | -46.9898 | 2024-10-09 02:37:05 | GOES-16 | MOCOCA | SÃO PAULO | Brasil | 3530508 | 35 | 33 | nan | nan | nan | Cerrado | 76.3 |
| ce69cd4a-1861-3a61-830a-b656e02a4f3a | -21.5727 | -46.9659 | 2024-10-09 02:37:05 | GOES-16 | MOCOCA | SÃO PAULO | Brasil | 3530508 | 35 | 33 | nan | nan | nan | Cerrado | 87.7 |
| 927184c6-d924-35cb-aed5-ee0c5b18f226 | -21.5864 | -47.8827 | 2024-10-09 02:37:05 | GOES-16 | LUÍS ANTÔNIO | SÃO PAULO | Brasil | 3527603 | 35 | 33 | nan | nan | nan | Cerrado | 81.9 |
| c146f20f-fe7d-31fa-b198-7bc6a311b839 | -21.8165 | -49.1774 | 2024-10-09 02:37:06 | GOES-16 | REGINÓPOLIS | SÃO PAULO | Brasil | 3542503 | 35 | 33 | nan | nan | nan | Mata Atlântica | 191.3 |
| 7aebdfae-6008-3c58-8bc2-962be3ae780d | -21.8172 | -49.1541 | 2024-10-09 02:37:06 | GOES-16 | REGINÓPOLIS | SÃO PAULO | Brasil | 3542503 | 35 | 33 | nan | nan | nan | Mata Atlântica | 231.1 |
| 8b4fea16-399a-3fb9-b3d8-984b6340415d | -21.8373 | -49.1726 | 2024-10-09 02:37:06 | GOES-16 | REGINÓPOLIS | SÃO PAULO | Brasil | 3542503 | 35 | 33 | nan | nan | nan | Mata Atlântica | 236.2 |
| 38165ac7-edf6-3d5e-85ad-3382a392f408 | -21.838 | -49.1493 | 2024-10-09 02:37:06 | GOES-16 | IACANGA | SÃO PAULO | Brasil | 3519105 | 35 | 33 | nan | nan | nan | Mata Atlântica | 358.3 |
| a0786efb-da2c-33c9-a583-b0ae0a9aa492 | -21.8587 | -49.1444 | 2024-10-09 02:37:06 | GOES-16 | IACANGA | SÃO PAULO | Brasil | 3519105 | 35 | 33 | nan | nan | nan | Mata Atlântica | 102.1 |
| e4cc9418-e201-3552-a504-8a89a7d7a666 | -22.6561 | -50.9566 | 2024-10-09 02:37:11 | GOES-16 | IEPÊ | SÃO PAULO | Brasil | 3519907 | 35 | 33 | nan | nan | nan | Mata Atlântica | 91.2 |
| 246a217f-8e70-3bcb-9e1a-d6ebcac709d1 | -22.6567 | -50.9337 | 2024-10-09 02:37:11 | GOES-16 | RANCHARIA | SÃO PAULO | Brasil | 3542206 | 35 | 33 | nan | nan | nan | Mata Atlântica | 96.0 |
| c744dc9c-54e4-303b-8ec1-eb705171185f | -22.8137 | -48.4225 | 2024-10-09 02:37:11 | GOES-16 | BOTUCATU | SÃO PAULO | Brasil | 3507506 | 35 | 33 | nan | nan | nan | Cerrado | 73.4 |
| 30200084-aed9-3394-9341-156c71a33086 | -22.8348 | -54.4471 | 2024-10-09 02:37:12 | GOES-16 | JUTI | MATO GROSSO DO SUL | Brasil | 5005152 | 50 | 33 | nan | nan | nan | Mata Atlântica | 103.3 |
| c7532a0d-4ce7-3aba-ad6f-b7933d91f3f6 | -23.3764 | -52.0443 | 2024-10-09 02:37:15 | GOES-16 | MARINGÁ | PARANÁ | Brasil | 4115200 | 41 | 33 | nan | nan | nan | Mata Atlântica | 147.9 |
| fa4d192b-1a35-3ef4-986d-cdfe37001364 | -1.11 | -53.6173 | 2024-10-09 02:45:12 | GOES-16 | ALMEIRIM | PARÁ | Brasil | 1500503 | 15 | 33 | nan | nan | nan | Amazônia | 79.6 |
| 857fb34f-fdbb-3afc-99cf-7c332dcd83dc | -3.8196 | -41.5979 | 2024-10-09 02:45:28 | GOES-16 | PIRACURUCA | PIAUÍ | Brasil | 2208304 | 22 | 33 | nan | nan | nan | Caatinga | 53.7 |
| 20d53e29-ae90-3bec-8fa7-deb63a9a74db | -3.9021 | -46.4689 | 2024-10-09 02:45:28 | GOES-16 | BOM JARDIM | MARANHÃO | Brasil | 2102002 | 21 | 33 | nan | nan | nan | Amazônia | 60.9 |
| 96d196d6-7840-3904-9772-c376a00627ad | -3.9023 | -46.4467 | 2024-10-09 02:45:28 | GOES-16 | BOM JARDIM | MARANHÃO | Brasil | 2102002 | 21 | 33 | nan | nan | nan | Amazônia | 52.5 |
| fce87eef-ae47-3e04-ba34-1b445cb25fd5 | -3.9207 | -46.468 | 2024-10-09 02:45:28 | GOES-16 | BOM JARDIM | MARANHÃO | Brasil | 2102002 | 21 | 33 | nan | nan | nan | Amazônia | 49.6 |
| af53a0b8-8ee8-3f87-8be8-1546502a4ccd | -3.9208 | -46.4459 | 2024-10-09 02:45:28 | GOES-16 | BOM JARDIM | MARANHÃO | Brasil | 2102002 | 21 | 33 | nan | nan | nan | Amazônia | 60.3 |
| b2d7ffee-5070-37db-8a36-569447c995bc | -3.9393 | -46.4672 | 2024-10-09 02:45:28 | GOES-16 | BOM JARDIM | MARANHÃO | Brasil | 2102002 | 21 | 33 | nan | nan | nan | Amazônia | 66.5 |
| 788d9b81-4d94-3e39-84c3-e739d6f93671 | -3.9394 | -46.445 | 2024-10-09 02:45:28 | GOES-16 | BOM JARDIM | MARANHÃO | Brasil | 2102002 | 21 | 33 | nan | nan | nan | Amazônia | 94.5 |
| a9ad1728-3687-3e4c-86a8-736b8d8ecb34 | -6.7613 | -60.0751 | 2024-10-09 02:45:45 | GOES-16 | NOVO ARIPUANÃ | AMAZONAS | Brasil | 1303304 | 13 | 33 | nan | nan | nan | Amazônia | 42.6 |
| 9a67907e-da89-39cb-9ec5-afd509500b96 | -6.7614 | -60.0559 | 2024-10-09 02:45:45 | GOES-16 | NOVO ARIPUANÃ | AMAZONAS | Brasil | 1303304 | 13 | 33 | nan | nan | nan | Amazônia | 146.3 |
| 786e6982-795e-3fa5-80d8-ed5633d603d4 | -6.7797 | -60.0744 | 2024-10-09 02:45:45 | GOES-16 | NOVO ARIPUANÃ | AMAZONAS | Brasil | 1303304 | 13 | 33 | nan | nan | nan | Amazônia | 42.2 |
| 1733c1ac-3990-3916-ac78-e4eca101a739 | -6.7798 | -60.0552 | 2024-10-09 02:45:45 | GOES-16 | NOVO ARIPUANÃ | AMAZONAS | Brasil | 1303304 | 13 | 33 | nan | nan | nan | Amazônia | 163.1 |
| cb3741ee-d563-30d3-88ab-e5d4c12c61c1 | -6.7799 | -60.036 | 2024-10-09 02:45:45 | GOES-16 | NOVO ARIPUANÃ | AMAZONAS | Brasil | 1303304 | 13 | 33 | nan | nan | nan | Amazônia | 60.2 |
| 51258690-8859-30ca-8479-9213b3ad0803 | -8.4919 | -48.6476 | 2024-10-09 02:45:54 | GOES-16 | PRESIDENTE KENNEDY | TOCANTINS | Brasil | 1718402 | 17 | 33 | nan | nan | nan | Amazônia | 88.7 |
| 88680c08-d12c-314b-a48d-cd46abbf50bc | -10.3655 | -64.8451 | 2024-10-09 02:46:06 | GOES-16 | NOVA MAMORÉ | RONDÔNIA | Brasil | 1100338 | 11 | 33 | nan | nan | nan | Amazônia | 33.6 |
| 207afedb-e48c-3428-8f48-66a5bc00a5db | -10.3656 | -64.8262 | 2024-10-09 02:46:06 | GOES-16 | NOVA MAMORÉ | RONDÔNIA | Brasil | 1100338 | 11 | 33 | nan | nan | nan | Amazônia | 33.2 |
| 711a3ba8-7d93-39e3-93fb-7ab19aba8690 | -10.3894 | -61.2502 | 2024-10-09 02:46:06 | GOES-16 | RONDOLÂNDIA | MATO GROSSO | Brasil | 5107578 | 51 | 33 | nan | nan | nan | Amazônia | 63.5 |
| ec07207c-5968-3a58-bba1-1e29a4b3ac1f | -10.3895 | -61.231 | 2024-10-09 02:46:06 | GOES-16 | RONDOLÂNDIA | MATO GROSSO | Brasil | 5107578 | 51 | 33 | nan | nan | nan | Amazônia | 50.2 |
| 474bff29-202d-3374-b463-e11ce2468e4d | -10.3842 | -64.8443 | 2024-10-09 02:46:06 | GOES-16 | NOVA MAMORÉ | RONDÔNIA | Brasil | 1100338 | 11 | 33 | nan | nan | nan | Amazônia | 38.6 |
| cb7c56e9-f231-319e-92cb-007abf5c433a | -10.3843 | -64.8255 | 2024-10-09 02:46:06 | GOES-16 | NOVA MAMORÉ | RONDÔNIA | Brasil | 1100338 | 11 | 33 | nan | nan | nan | Amazônia | 41.8 |
| a231082c-6142-3165-9b0a-68b0dc43bdcf | -10.6068 | -55.9169 | 2024-10-09 02:46:07 | GOES-16 | NOVA CANAÃ DO NORTE | MATO GROSSO | Brasil | 5106216 | 51 | 33 | nan | nan | nan | Amazônia | 32.5 |
| 2fb53ca1-ea05-31cf-915e-ec62c93ad0a7 | -10.6253 | -55.9355 | 2024-10-09 02:46:07 | GOES-16 | NOVA CANAÃ DO NORTE | MATO GROSSO | Brasil | 5106216 | 51 | 33 | nan | nan | nan | Amazônia | 36.7 |
| df6e3a7a-6f56-3545-90d1-f48b534155e0 | -10.6256 | -55.9154 | 2024-10-09 02:46:07 | GOES-16 | NOVA CANAÃ DO NORTE | MATO GROSSO | Brasil | 5106216 | 51 | 33 | nan | nan | nan | Amazônia | 76.4 |
| f158a6a6-1a8d-3f09-b39a-93e50023a5bf | -10.6258 | -55.8953 | 2024-10-09 02:46:07 | GOES-16 | NOVA CANAÃ DO NORTE | MATO GROSSO | Brasil | 5106216 | 51 | 33 | nan | nan | nan | Amazônia | 56.6 |
| 4d4b88a9-15f9-3153-8f5b-ceb28428fcf2 | -10.6444 | -55.914 | 2024-10-09 02:46:07 | GOES-16 | NOVA CANAÃ DO NORTE | MATO GROSSO | Brasil | 5106216 | 51 | 33 | nan | nan | nan | Amazônia | 22.0 |
| a1233b1e-bb6e-3f74-9403-b69a713fb1b4 | -10.6446 | -55.8938 | 2024-10-09 02:46:07 | GOES-16 | NOVA CANAÃ DO NORTE | MATO GROSSO | Brasil | 5106216 | 51 | 33 | nan | nan | nan | Amazônia | 24.8 |
| e83a3dc3-b43d-32a5-91d2-7038a6d0d4aa | -10.8567 | -63.9177 | 2024-10-09 02:46:08 | GOES-16 | NOVA MAMORÉ | RONDÔNIA | Brasil | 1100338 | 11 | 33 | nan | nan | nan | Amazônia | 52.7 |
| b87a2273-4e5e-321c-a1f9-1a2c3302cbe3 | -10.8754 | -63.9169 | 2024-10-09 02:46:08 | GOES-16 | GUAJARÁ-MIRIM | RONDÔNIA | Brasil | 1100106 | 11 | 33 | nan | nan | nan | Amazônia | 89.9 |
| ed90153d-2b83-3675-a6a5-a57767804cca | -10.8755 | -63.8979 | 2024-10-09 02:46:08 | GOES-16 | GUAJARÁ-MIRIM | RONDÔNIA | Brasil | 1100106 | 11 | 33 | nan | nan | nan | Amazônia | 65.6 |
| 500adf3a-45f8-3d45-a8b9-1336f7dc2f60 | -10.8941 | -63.916 | 2024-10-09 02:46:09 | GOES-16 | GUAJARÁ-MIRIM | RONDÔNIA | Brasil | 1100106 | 11 | 33 | nan | nan | nan | Amazônia | 55.0 |
| 1e9174e5-4b13-342e-8abe-e6375a9e976f | -11.2583 | -60.3885 | 2024-10-09 02:46:10 | GOES-16 | VILHENA | RONDÔNIA | Brasil | 1100304 | 11 | 33 | nan | nan | nan | Amazônia | 52.4 |
| 782a7cbc-235f-3af9-a43a-453eb35d8afa | -11.6806 | -64.0312 | 2024-10-09 02:46:13 | GOES-16 | GUAJARÁ-MIRIM | RONDÔNIA | Brasil | 1100106 | 11 | 33 | nan | nan | nan | Amazônia | 62.4 |
| cc7118ad-2ac4-31fe-baa9-6610b65967b0 | -11.693 | -65.0163 | 2024-10-09 02:46:13 | GOES-16 | GUAJARÁ-MIRIM | RONDÔNIA | Brasil | 1100106 | 11 | 33 | nan | nan | nan | Amazônia | 90.3 |
| 6576f621-63a6-377f-bd45-258c6ba957b9 | -11.6931 | -64.9974 | 2024-10-09 02:46:13 | GOES-16 | GUAJARÁ-MIRIM | RONDÔNIA | Brasil | 1100106 | 11 | 33 | nan | nan | nan | Amazônia | 61.6 |
| 611e6658-c558-30cc-ade4-05b367b0584e | -11.7117 | -65.0155 | 2024-10-09 02:46:13 | GOES-16 | GUAJARÁ-MIRIM | RONDÔNIA | Brasil | 1100106 | 11 | 33 | nan | nan | nan | Amazônia | 128.3 |
| 8fdcc3c1-2562-3d3b-8512-59b1398b27a5 | -11.7119 | -64.9966 | 2024-10-09 02:46:13 | GOES-16 | GUAJARÁ-MIRIM | RONDÔNIA | Brasil | 1100106 | 11 | 33 | nan | nan | nan | Amazônia | 80.8 |
| 95a1d7c0-a3f5-37ee-a868-6579ce7d7df2 | -11.992 | -51.0553 | 2024-10-09 02:46:14 | GOES-16 | SÃO FÉLIX DO ARAGUAIA | MATO GROSSO | Brasil | 5107859 | 51 | 33 | nan | nan | nan | Cerrado | 92.6 |
| 3206d2db-0b4c-360d-93b7-1606a1d64831 | -12.011 | -51.0531 | 2024-10-09 02:46:14 | GOES-16 | SÃO FÉLIX DO ARAGUAIA | MATO GROSSO | Brasil | 5107859 | 51 | 33 | nan | nan | nan | Cerrado | 118.0 |
| 6b722bc6-95f5-3df6-b171-1420c9ac5a6b | -12.6676 | -63.0819 | 2024-10-09 02:46:18 | GOES-16 | SÃO FRANCISCO DO GUAPORÉ | RONDÔNIA | Brasil | 1101492 | 11 | 33 | nan | nan | nan | Amazônia | 59.2 |
| cede4789-2817-3688-9afc-88aed8a99183 | -12.8591 | -62.8018 | 2024-10-09 02:46:20 | GOES-16 | SÃO FRANCISCO DO GUAPORÉ | RONDÔNIA | Brasil | 1101492 | 11 | 33 | nan | nan | nan | Amazônia | 64.4 |
| da3ba7dc-e7cc-343b-89f9-93d60e88dc00 | -12.878 | -62.8007 | 2024-10-09 02:46:20 | GOES-16 | ALTA FLORESTA D'OESTE | RONDÔNIA | Brasil | 1100015 | 11 | 33 | nan | nan | nan | Amazônia | 87.8 |
| ecfb99ac-0680-36a3-a04a-1d0c3f77644a | -12.9566 | -62.4685 | 2024-10-09 02:46:20 | GOES-16 | ALTA FLORESTA D'OESTE | RONDÔNIA | Brasil | 1100015 | 11 | 33 | nan | nan | nan | Amazônia | 74.8 |
| 2758912b-f098-34bf-92a0-ceb515c768c6 | -12.9568 | -62.4492 | 2024-10-09 02:46:20 | GOES-16 | ALTA FLORESTA D'OESTE | RONDÔNIA | Brasil | 1100015 | 11 | 33 | nan | nan | nan | Amazônia | 59.3 |
| 70f7d6bf-f177-385f-86c0-2729e63ea1ad | -13.817 | -44.5961 | 2024-10-09 02:46:23 | GOES-16 | CORIBE | BAHIA | Brasil | 2909109 | 29 | 33 | nan | nan | nan | Cerrado | 187.7 |
| 3c6fd5e2-7e9c-3419-9d4d-0abfd3b8f317 | -13.8175 | -44.5726 | 2024-10-09 02:46:23 | GOES-16 | CORIBE | BAHIA | Brasil | 2909109 | 29 | 33 | nan | nan | nan | Cerrado | 88.8 |
| ebced507-e3cc-3c11-be96-63c73babfedd | -13.8364 | -44.5927 | 2024-10-09 02:46:23 | GOES-16 | CORIBE | BAHIA | Brasil | 2909109 | 29 | 33 | nan | nan | nan | Cerrado | 183.5 |
| 740436c1-d48f-3e4b-9ef2-13e7a95196ed | -13.8369 | -44.5691 | 2024-10-09 02:46:23 | GOES-16 | CORIBE | BAHIA | Brasil | 2909109 | 29 | 33 | nan | nan | nan | Cerrado | 205.9 |
| 1e63697f-fa53-317d-b48f-b4379ea6aa75 | -13.8564 | -44.5657 | 2024-10-09 02:46:24 | GOES-16 | CORIBE | BAHIA | Brasil | 2909109 | 29 | 33 | nan | nan | nan | Cerrado | 75.1 |
| 259c9452-79b8-3ecd-94d3-250684e90ccc | -15.1744 | -49.4114 | 2024-10-09 02:46:31 | GOES-16 | SANTA ISABEL | GOIÁS | Brasil | 5219357 | 52 | 33 | nan | nan | nan | Cerrado | 118.0 |
| 6b2bea4c-8950-3822-844a-bb9a8a8890e1 | -15.1748 | -49.3893 | 2024-10-09 02:46:31 | GOES-16 | SANTA ISABEL | GOIÁS | Brasil | 5219357 | 52 | 33 | nan | nan | nan | Cerrado | 93.5 |


[Clique aqui para ver as próximas entradas](README55.md)
