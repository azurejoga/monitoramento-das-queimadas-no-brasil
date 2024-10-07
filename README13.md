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

## Dados Diários - Página 13

| ID | Latitude | Longitude | Data/Hora GMT | Satélite | Município | Estado | País | Município ID | Estado ID | País ID | Dias sem Chuva | Precipitação | Risco de Fogo | Bioma | FRP |
|----|----------|-----------|---------------|----------|-----------|--------|------|--------------|-----------|---------|----------------|--------------|----------------|-------|-----|
| a7a1eab5-7985-3d0b-94c7-b23a886092bf | -20.1229 | -49.0518 | 2024-10-07 00:46:57 | GOES-16 | FRUTAL | MINAS GERAIS | Brasil | 3127107 | 31 | 33 | nan | nan | nan | Cerrado | 304.1 |
| 4b674947-87e2-348d-830f-0fddbed54de6 | -20.1236 | -49.0288 | 2024-10-07 00:46:57 | GOES-16 | FRUTAL | MINAS GERAIS | Brasil | 3127107 | 31 | 33 | nan | nan | nan | Cerrado | 117.8 |
| 3279c992-ca12-3770-8a8a-800d24c9a8ac | -20.4661 | -47.6592 | 2024-10-07 00:46:59 | GOES-16 | GUARÁ | SÃO PAULO | Brasil | 3517703 | 35 | 33 | nan | nan | nan | Cerrado | 159.1 |
| 275a9be2-e5a2-32ee-b9f3-ecfac30087fc | -20.4866 | -47.6544 | 2024-10-07 00:46:59 | GOES-16 | GUARÁ | SÃO PAULO | Brasil | 3517703 | 35 | 33 | nan | nan | nan | Cerrado | 108.5 |
| 06876011-b6dd-3559-8fe4-0386ec05a3d8 | -21.0712 | -47.2331 | 2024-10-07 00:47:02 | GOES-16 | SANTO ANTÔNIO DA ALEGRIA | SÃO PAULO | Brasil | 3547908 | 35 | 33 | nan | nan | nan | Cerrado | 157.7 |
| f24ce601-4fa2-30f6-a8f5-65cf4fa81bef | -21.0919 | -47.228 | 2024-10-07 00:47:02 | GOES-16 | SANTO ANTÔNIO DA ALEGRIA | SÃO PAULO | Brasil | 3547908 | 35 | 33 | nan | nan | nan | Cerrado | 161.1 |
| c9fd9a2e-48ab-3ac4-b52e-0b043f063eb6 | -21.0926 | -47.2043 | 2024-10-07 00:47:02 | GOES-16 | SANTO ANTÔNIO DA ALEGRIA | SÃO PAULO | Brasil | 3547908 | 35 | 33 | nan | nan | nan | Cerrado | 46.4 |
| 7c8a4750-06d2-3bef-843e-906352565bb3 | -21.2717 | -47.3959 | 2024-10-07 00:47:03 | GOES-16 | SANTA CRUZ DA ESPERANÇA | SÃO PAULO | Brasil | 3546256 | 35 | 33 | nan | nan | nan | Cerrado | 74.2 |
| bcb7bf8f-0ae5-3afc-bae0-36474b16b705 | -21.2924 | -47.3908 | 2024-10-07 00:47:03 | GOES-16 | SANTA CRUZ DA ESPERANÇA | SÃO PAULO | Brasil | 3546256 | 35 | 33 | nan | nan | nan | Cerrado | 48.0 |
| 4d60770b-c9eb-3092-8835-ef9818451a2c | -21.5843 | -47.9536 | 2024-10-07 00:47:05 | GOES-16 | GUATAPARÁ | SÃO PAULO | Brasil | 3518859 | 35 | 33 | nan | nan | nan | Cerrado | 101.7 |
| bb091e46-28b6-395e-b233-3b4249341448 | -21.605 | -47.9485 | 2024-10-07 00:47:05 | GOES-16 | RINCÃO | SÃO PAULO | Brasil | 3543709 | 35 | 33 | nan | nan | nan | Cerrado | 96.4 |
| b77d1826-087d-3da9-aaeb-4e33ef145670 | -21.6529 | -47.7255 | 2024-10-07 00:47:05 | GOES-16 | LUÍS ANTÔNIO | SÃO PAULO | Brasil | 3527603 | 35 | 33 | nan | nan | nan | Cerrado | 85.2 |
| 74675f0a-00e9-3f1b-a023-f7b9d5ca4830 | -22.1974 | -48.1778 | 2024-10-07 00:47:08 | GOES-16 | BROTAS | SÃO PAULO | Brasil | 3507902 | 35 | 33 | nan | nan | nan | Cerrado | 56.9 |
| d6bb77ed-c232-3e05-899d-dcccefdb9444 | -22.2183 | -48.1726 | 2024-10-07 00:47:08 | GOES-16 | BROTAS | SÃO PAULO | Brasil | 3507902 | 35 | 33 | nan | nan | nan | Cerrado | 52.3 |
| 79a716b9-93db-3364-b9a6-6b1a1e99c827 | -22.7198 | -53.2341 | 2024-10-07 00:47:11 | GOES-16 | BATAYPORÃ | MATO GROSSO DO SUL | Brasil | 5002001 | 50 | 33 | nan | nan | nan | Mata Atlântica | 65.6 |
| bf6f9e8f-527f-3a58-a244-efa8e533f381 | -1.0182 | -53.739 | 2024-10-07 00:55:12 | GOES-16 | PRAINHA | PARÁ | Brasil | 1506005 | 15 | 33 | nan | nan | nan | Amazônia | 80.7 |
| 7de9fa06-ffef-3b2e-8915-32777950b592 | -1.0182 | -53.7189 | 2024-10-07 00:55:12 | GOES-16 | PRAINHA | PARÁ | Brasil | 1506005 | 15 | 33 | nan | nan | nan | Amazônia | 73.4 |
| 42eb6839-c171-3fae-9e72-61d3db2d9bcc | -1.0365 | -53.7389 | 2024-10-07 00:55:12 | GOES-16 | PRAINHA | PARÁ | Brasil | 1506005 | 15 | 33 | nan | nan | nan | Amazônia | 82.6 |
| b9edefd0-8680-3944-b776-34a7f4349f4c | -1.0365 | -53.7187 | 2024-10-07 00:55:12 | GOES-16 | PRAINHA | PARÁ | Brasil | 1506005 | 15 | 33 | nan | nan | nan | Amazônia | 73.0 |
| 5d9844b0-e247-3300-a507-183576b62ab0 | -2.2113 | -53.7029 | 2024-10-07 00:55:19 | GOES-16 | PRAINHA | PARÁ | Brasil | 1506005 | 15 | 33 | nan | nan | nan | Amazônia | 122.1 |
| e5348c61-0b4c-33c4-9bc0-c04a2113c072 | -2.2114 | -53.6828 | 2024-10-07 00:55:19 | GOES-16 | PRAINHA | PARÁ | Brasil | 1506005 | 15 | 33 | nan | nan | nan | Amazônia | 93.3 |
| 1032f436-1773-3f64-9c78-9a6c67809882 | -2.2297 | -53.7026 | 2024-10-07 00:55:19 | GOES-16 | PRAINHA | PARÁ | Brasil | 1506005 | 15 | 33 | nan | nan | nan | Amazônia | 94.9 |
| 1fd96913-3b2b-33c6-83c7-73396f80683d | -2.2297 | -53.6824 | 2024-10-07 00:55:19 | GOES-16 | PRAINHA | PARÁ | Brasil | 1506005 | 15 | 33 | nan | nan | nan | Amazônia | 75.9 |
| 0a511b48-f72c-3915-b05b-ac0015b92284 | -2.8569 | -52.9197 | 2024-10-07 00:55:22 | GOES-16 | MEDICILÂNDIA | PARÁ | Brasil | 1504455 | 15 | 33 | nan | nan | nan | Amazônia | 139.9 |
| cd524b01-4d6b-3138-a6fe-fb7533a48443 | -2.857 | -52.8993 | 2024-10-07 00:55:22 | GOES-16 | MEDICILÂNDIA | PARÁ | Brasil | 1504455 | 15 | 33 | nan | nan | nan | Amazônia | 147.7 |
| 6e4a0e13-ff8d-31f9-bbc3-9d3678a1d5c2 | -2.8753 | -52.9192 | 2024-10-07 00:55:22 | GOES-16 | MEDICILÂNDIA | PARÁ | Brasil | 1504455 | 15 | 33 | nan | nan | nan | Amazônia | 214.5 |
| e12bb8ae-3116-3ed2-bd23-94cd116ec3d9 | -2.8754 | -52.8989 | 2024-10-07 00:55:22 | GOES-16 | MEDICILÂNDIA | PARÁ | Brasil | 1504455 | 15 | 33 | nan | nan | nan | Amazônia | 271.5 |
| 9fe495e4-42c1-3731-b354-1d1ca9b03cdb | -2.8937 | -52.9188 | 2024-10-07 00:55:23 | GOES-16 | MEDICILÂNDIA | PARÁ | Brasil | 1504455 | 15 | 33 | nan | nan | nan | Amazônia | 86.9 |
| bace2fc2-afbd-3f84-89a4-a7c924d72c76 | -2.8937 | -52.8984 | 2024-10-07 00:55:23 | GOES-16 | MEDICILÂNDIA | PARÁ | Brasil | 1504455 | 15 | 33 | nan | nan | nan | Amazônia | 107.2 |
| a93a33f4-1dad-313c-9f93-7602b8c094a7 | -4.2728 | -43.7601 | 2024-10-07 00:55:30 | GOES-16 | CODÓ | MARANHÃO | Brasil | 2103307 | 21 | 33 | nan | nan | nan | Cerrado | 67.9 |
| db307306-7a06-30e2-ac4c-551d69bee888 | -4.2729 | -43.737 | 2024-10-07 00:55:30 | GOES-16 | CODÓ | MARANHÃO | Brasil | 2103307 | 21 | 33 | nan | nan | nan | Cerrado | 140.3 |
| 04a789a4-c1bf-321c-81c5-6b5b0dcd9ddf | -4.2916 | -43.736 | 2024-10-07 00:55:30 | GOES-16 | CODÓ | MARANHÃO | Brasil | 2103307 | 21 | 33 | nan | nan | nan | Cerrado | 96.0 |
| 878dde1d-3b1d-3a4b-99dc-7a3db5b1c5ef | -10.8754 | -63.9169 | 2024-10-07 00:56:08 | GOES-16 | GUAJARÁ-MIRIM | RONDÔNIA | Brasil | 1100106 | 11 | 33 | nan | nan | nan | Amazônia | 49.7 |
| 7ffa05c7-2b19-34d6-b3a0-5329cc6e439b | -11.2467 | -51.3918 | 2024-10-07 00:56:10 | GOES-16 | SÃO FÉLIX DO ARAGUAIA | MATO GROSSO | Brasil | 5107859 | 51 | 33 | nan | nan | nan | Cerrado | 57.7 |
| cc7aec14-8084-3acb-ac47-3bcf6a333f20 | -11.2654 | -51.411 | 2024-10-07 00:56:10 | GOES-16 | SÃO FÉLIX DO ARAGUAIA | MATO GROSSO | Brasil | 5107859 | 51 | 33 | nan | nan | nan | Cerrado | 62.7 |
| 92466989-9d77-3794-903b-4de227e247c4 | -11.2657 | -51.3898 | 2024-10-07 00:56:10 | GOES-16 | SÃO FÉLIX DO ARAGUAIA | MATO GROSSO | Brasil | 5107859 | 51 | 33 | nan | nan | nan | Cerrado | 127.5 |
| 4f1cd919-ffd8-334d-aba5-7cc89f191d94 | -11.266 | -51.3686 | 2024-10-07 00:56:10 | GOES-16 | SÃO FÉLIX DO ARAGUAIA | MATO GROSSO | Brasil | 5107859 | 51 | 33 | nan | nan | nan | Cerrado | 74.8 |
| 8c43a07b-5659-39d5-be06-fba73562f0bc | -11.2844 | -51.409 | 2024-10-07 00:56:10 | GOES-16 | SÃO FÉLIX DO ARAGUAIA | MATO GROSSO | Brasil | 5107859 | 51 | 33 | nan | nan | nan | Cerrado | 58.6 |
| d3eba26a-280b-3eb2-816b-54a1b2453f58 | -11.2847 | -51.3878 | 2024-10-07 00:56:10 | GOES-16 | SÃO FÉLIX DO ARAGUAIA | MATO GROSSO | Brasil | 5107859 | 51 | 33 | nan | nan | nan | Cerrado | 98.7 |
| a36cd392-d2d0-3450-80cf-4683e69130a2 | -12.0585 | -63.7841 | 2024-10-07 00:56:15 | GOES-16 | SÃO FRANCISCO DO GUAPORÉ | RONDÔNIA | Brasil | 1101492 | 11 | 33 | nan | nan | nan | Amazônia | 68.8 |
| b5eebf74-8762-3ee0-ab1b-8f12c15a57fc | -12.0587 | -63.765 | 2024-10-07 00:56:15 | GOES-16 | SÃO FRANCISCO DO GUAPORÉ | RONDÔNIA | Brasil | 1101492 | 11 | 33 | nan | nan | nan | Amazônia | 50.1 |
| 72323230-50ec-3fc8-ad4c-f1e49eba6429 | -12.7089 | -40.2155 | 2024-10-07 00:56:17 | GOES-16 | ITABERABA | BAHIA | Brasil | 2914703 | 29 | 33 | nan | nan | nan | Caatinga | 61.8 |
| 4b98aa1b-cc3d-33be-b44f-1dc55c7f8531 | -13.5719 | -50.3223 | 2024-10-07 00:56:23 | GOES-16 | MUNDO NOVO | GOIÁS | Brasil | 5214051 | 52 | 33 | nan | nan | nan | Cerrado | 91.3 |
| 820169b4-889b-376b-b38d-1e28dd733176 | -13.5911 | -50.3197 | 2024-10-07 00:56:23 | GOES-16 | MUNDO NOVO | GOIÁS | Brasil | 5214051 | 52 | 33 | nan | nan | nan | Cerrado | 91.3 |
| f50cb2d0-3574-3a43-a58c-79bd04ace1c0 | -13.8354 | -44.6398 | 2024-10-07 00:56:23 | GOES-16 | CORIBE | BAHIA | Brasil | 2909109 | 29 | 33 | nan | nan | nan | Cerrado | 74.8 |
| 2abc7fab-b4e0-3ee9-a473-4cf3cd19a933 | -13.8359 | -44.6162 | 2024-10-07 00:56:23 | GOES-16 | CORIBE | BAHIA | Brasil | 2909109 | 29 | 33 | nan | nan | nan | Cerrado | 84.8 |
| 2b6d9c18-d2de-3743-8f90-b8bbcde02f08 | -16.6195 | -55.5892 | 2024-10-07 00:56:40 | GOES-16 | BARÃO DE MELGAÇO | MATO GROSSO | Brasil | 5101605 | 51 | 33 | nan | nan | nan | Pantanal | 117.9 |
| 381feda8-3360-3bdd-934d-22137370cea9 | -16.6199 | -55.5684 | 2024-10-07 00:56:40 | GOES-16 | BARÃO DE MELGAÇO | MATO GROSSO | Brasil | 5101605 | 51 | 33 | nan | nan | nan | Pantanal | 131.6 |
| 68ea5713-6884-30ed-8315-88ebf7beaa05 | -16.992 | -56.721 | 2024-10-07 00:56:42 | GOES-16 | POCONÉ | MATO GROSSO | Brasil | 5106505 | 51 | 33 | nan | nan | nan | Pantanal | 129.3 |
| 006fea55-532c-33b5-98fe-7e6cb2bdbce2 | -16.9924 | -56.7003 | 2024-10-07 00:56:42 | GOES-16 | POCONÉ | MATO GROSSO | Brasil | 5106505 | 51 | 33 | nan | nan | nan | Pantanal | 103.6 |
| 711b3b23-aaa1-3b6a-a892-01e0c4b0e84f | -17.0116 | -56.7186 | 2024-10-07 00:56:42 | GOES-16 | POCONÉ | MATO GROSSO | Brasil | 5106505 | 51 | 33 | nan | nan | nan | Pantanal | 108.3 |
| 88983a2f-25d5-3110-a360-2dac4c9fd135 | -17.012 | -56.698 | 2024-10-07 00:56:42 | GOES-16 | POCONÉ | MATO GROSSO | Brasil | 5106505 | 51 | 33 | nan | nan | nan | Pantanal | 118.7 |
| d5712134-7e14-3d5c-ab9d-69650e34a390 | -17.0123 | -56.6773 | 2024-10-07 00:56:42 | GOES-16 | POCONÉ | MATO GROSSO | Brasil | 5106505 | 51 | 33 | nan | nan | nan | Pantanal | 90.4 |
| 4596d92b-cfd8-3ba2-8197-bbbe1b751257 | -17.1581 | -57.3582 | 2024-10-07 00:56:43 | GOES-16 | POCONÉ | MATO GROSSO | Brasil | 5106505 | 51 | 33 | nan | nan | nan | Pantanal | 102.1 |
| 06a258fa-b4ca-3254-ae38-a9377073c19c | -17.1584 | -57.3377 | 2024-10-07 00:56:43 | GOES-16 | POCONÉ | MATO GROSSO | Brasil | 5106505 | 51 | 33 | nan | nan | nan | Pantanal | 86.2 |
| 985fa401-0d96-386b-a1c9-3e1889b1af75 | -17.6279 | -53.1094 | 2024-10-07 00:56:45 | GOES-16 | SANTA RITA DO ARAGUAIA | GOIÁS | Brasil | 5219407 | 52 | 33 | nan | nan | nan | Cerrado | 104.5 |
| a89a89e6-79ee-34de-923e-1cf414908d9c | -17.6283 | -53.088 | 2024-10-07 00:56:45 | GOES-16 | MINEIROS | GOIÁS | Brasil | 5213103 | 52 | 33 | nan | nan | nan | Cerrado | 92.9 |
| 3cea146b-877b-338f-8c0c-b2c6fad3ea2f | -17.6477 | -53.1064 | 2024-10-07 00:56:45 | GOES-16 | SANTA RITA DO ARAGUAIA | GOIÁS | Brasil | 5219407 | 52 | 33 | nan | nan | nan | Cerrado | 71.7 |
| 0422e454-090e-336a-b1a7-6145c0ab159f | -17.6481 | -53.0849 | 2024-10-07 00:56:45 | GOES-16 | MINEIROS | GOIÁS | Brasil | 5213103 | 52 | 33 | nan | nan | nan | Cerrado | 106.3 |
| ce43205b-5bf6-3853-808b-a986e1853137 | -17.6679 | -53.0819 | 2024-10-07 00:56:45 | GOES-16 | MINEIROS | GOIÁS | Brasil | 5213103 | 52 | 33 | nan | nan | nan | Cerrado | 118.2 |
| a215e79d-dad4-325c-b496-49be2b6c92db | -18.6391 | -57.2578 | 2024-10-07 00:56:51 | GOES-16 | CORUMBÁ | MATO GROSSO DO SUL | Brasil | 5003207 | 50 | 33 | nan | nan | nan | Pantanal | 76.0 |
| 61f1965c-7c23-374a-a9fe-b52e99a18ae8 | -19.8104 | -42.3854 | 2024-10-07 00:56:55 | GOES-16 | CÓRREGO NOVO | MINAS GERAIS | Brasil | 3120003 | 31 | 33 | nan | nan | nan | Mata Atlântica | 97.8 |
| 7da15b8b-046f-333f-bc8c-d9b8831a5aeb | -19.8112 | -42.36 | 2024-10-07 00:56:55 | GOES-16 | CÓRREGO NOVO | MINAS GERAIS | Brasil | 3120003 | 31 | 33 | nan | nan | nan | Mata Atlântica | 259.3 |
| 09d94504-d907-3339-b0c0-824ff695016e | -19.831 | -42.3796 | 2024-10-07 00:56:55 | GOES-16 | CÓRREGO NOVO | MINAS GERAIS | Brasil | 3120003 | 31 | 33 | nan | nan | nan | Mata Atlântica | 118.1 |
| b49821b5-df50-39b1-b374-c3b7e206049a | -19.8318 | -42.3542 | 2024-10-07 00:56:55 | GOES-16 | BOM JESUS DO GALHO | MINAS GERAIS | Brasil | 3107802 | 31 | 33 | nan | nan | nan | Mata Atlântica | 322.7 |
| cd1004fa-ec30-35cb-88dd-7d3126a46668 | -19.8326 | -42.3288 | 2024-10-07 00:56:55 | GOES-16 | BOM JESUS DO GALHO | MINAS GERAIS | Brasil | 3107802 | 31 | 33 | nan | nan | nan | Mata Atlântica | 71.4 |
| 4777962a-84ac-3111-8bf3-fca646f64591 | -19.8524 | -42.3484 | 2024-10-07 00:56:55 | GOES-16 | BOM JESUS DO GALHO | MINAS GERAIS | Brasil | 3107802 | 31 | 33 | nan | nan | nan | Mata Atlântica | 64.6 |
| 794f5f3d-0c92-3232-801f-ad2fb42422bc | -19.883 | -42.6663 | 2024-10-07 00:56:55 | GOES-16 | DIONÍSIO | MINAS GERAIS | Brasil | 3121803 | 31 | 33 | nan | nan | nan | Mata Atlântica | 90.2 |
| 0327c81b-a1bb-37c5-a450-afc715f5ded0 | -19.8838 | -42.641 | 2024-10-07 00:56:55 | GOES-16 | DIONÍSIO | MINAS GERAIS | Brasil | 3121803 | 31 | 33 | nan | nan | nan | Mata Atlântica | 149.6 |
| d4778999-49e5-3a6d-ad10-5bf899cc609c | -19.9036 | -42.6606 | 2024-10-07 00:56:55 | GOES-16 | SÃO JOSÉ DO GOIABAL | MINAS GERAIS | Brasil | 3163409 | 31 | 33 | nan | nan | nan | Mata Atlântica | 70.6 |
| 2c1d96f1-b4cb-3124-8417-90831af5e2f5 | -19.9044 | -42.6353 | 2024-10-07 00:56:55 | GOES-16 | DIONÍSIO | MINAS GERAIS | Brasil | 3121803 | 31 | 33 | nan | nan | nan | Mata Atlântica | 122.2 |
| 632d9e47-cac3-300e-a4ab-f3b2ff239f3d | -20.1026 | -49.0562 | 2024-10-07 00:56:57 | GOES-16 | FRUTAL | MINAS GERAIS | Brasil | 3127107 | 31 | 33 | nan | nan | nan | Cerrado | 223.9 |
| 8bcd95da-d04e-3a80-97bf-f39aa0051b9f | -20.1223 | -49.0748 | 2024-10-07 00:56:57 | GOES-16 | FRUTAL | MINAS GERAIS | Brasil | 3127107 | 31 | 33 | nan | nan | nan | Cerrado | 102.6 |
| 07ecf4fe-7754-3267-9731-df18b4d23beb | -20.1229 | -49.0518 | 2024-10-07 00:56:57 | GOES-16 | FRUTAL | MINAS GERAIS | Brasil | 3127107 | 31 | 33 | nan | nan | nan | Cerrado | 653.1 |
| fba20c86-68dd-3486-989d-7eba1e809a2c | -20.1236 | -49.0288 | 2024-10-07 00:56:57 | GOES-16 | FRUTAL | MINAS GERAIS | Brasil | 3127107 | 31 | 33 | nan | nan | nan | Cerrado | 162.1 |
| 49e31921-5d15-3568-befc-412d72799524 | -20.1433 | -49.0474 | 2024-10-07 00:56:58 | GOES-16 | FRUTAL | MINAS GERAIS | Brasil | 3127107 | 31 | 33 | nan | nan | nan | Cerrado | 105.1 |
| c4f60872-6109-3b73-9209-c014d9671c37 | -20.4661 | -47.6592 | 2024-10-07 00:56:59 | GOES-16 | GUARÁ | SÃO PAULO | Brasil | 3517703 | 35 | 33 | nan | nan | nan | Cerrado | 265.7 |
| 9bc2d892-05bc-3c6e-a8f9-e2305121ba7a | -20.4668 | -47.6357 | 2024-10-07 00:56:59 | GOES-16 | GUARÁ | SÃO PAULO | Brasil | 3517703 | 35 | 33 | nan | nan | nan | Cerrado | 83.3 |
| 1c9a41ba-ed9f-3edc-8bc4-f4d3fd585332 | -20.4866 | -47.6544 | 2024-10-07 00:56:59 | GOES-16 | GUARÁ | SÃO PAULO | Brasil | 3517703 | 35 | 33 | nan | nan | nan | Cerrado | 208.3 |
| 7f6e9ede-b12a-38cb-af8d-44de93f1a96f | -20.4873 | -47.6309 | 2024-10-07 00:56:59 | GOES-16 | SÃO JOSÉ DA BELA VISTA | SÃO PAULO | Brasil | 3549508 | 35 | 33 | nan | nan | nan | Cerrado | 79.1 |
| 04c4b33e-4a63-3fa8-8c8c-243e3bf8b211 | -21.0705 | -47.2568 | 2024-10-07 00:57:02 | GOES-16 | ALTINÓPOLIS | SÃO PAULO | Brasil | 3501004 | 35 | 33 | nan | nan | nan | Cerrado | 49.6 |
| e8fec794-d521-320a-89e5-2ff7ac0274ee | -21.0712 | -47.2331 | 2024-10-07 00:57:02 | GOES-16 | SANTO ANTÔNIO DA ALEGRIA | SÃO PAULO | Brasil | 3547908 | 35 | 33 | nan | nan | nan | Cerrado | 164.1 |
| 392916e9-b918-317f-96db-bd864ecf3543 | -21.0719 | -47.2094 | 2024-10-07 00:57:02 | GOES-16 | SANTO ANTÔNIO DA ALEGRIA | SÃO PAULO | Brasil | 3547908 | 35 | 33 | nan | nan | nan | Cerrado | 55.2 |
| 5f47dfdc-81d3-311b-a97e-90d7492ac1cc | -21.0912 | -47.2518 | 2024-10-07 00:57:02 | GOES-16 | SANTO ANTÔNIO DA ALEGRIA | SÃO PAULO | Brasil | 3547908 | 35 | 33 | nan | nan | nan | Cerrado | 44.8 |
| 381bb56d-f8f3-370f-80a9-a07bdc751196 | -21.0919 | -47.228 | 2024-10-07 00:57:02 | GOES-16 | SANTO ANTÔNIO DA ALEGRIA | SÃO PAULO | Brasil | 3547908 | 35 | 33 | nan | nan | nan | Cerrado | 152.8 |
| 807bc429-1fcc-3dc3-b4da-1d79a966fa42 | -21.0926 | -47.2043 | 2024-10-07 00:57:02 | GOES-16 | SANTO ANTÔNIO DA ALEGRIA | SÃO PAULO | Brasil | 3547908 | 35 | 33 | nan | nan | nan | Cerrado | 43.7 |
| 31984994-ad89-376f-8e1e-8b70801d1ce5 | -21.2924 | -47.3908 | 2024-10-07 00:57:03 | GOES-16 | SANTA CRUZ DA ESPERANÇA | SÃO PAULO | Brasil | 3546256 | 35 | 33 | nan | nan | nan | Cerrado | 52.1 |
| 07490f82-b6eb-3dbd-bc1b-f45736193d5c | -21.5843 | -47.9536 | 2024-10-07 00:57:05 | GOES-16 | GUATAPARÁ | SÃO PAULO | Brasil | 3518859 | 35 | 33 | nan | nan | nan | Cerrado | 133.8 |
| c1176885-0874-3992-aadb-4b6fe3552a27 | -21.585 | -47.93 | 2024-10-07 00:57:05 | GOES-16 | RINCÃO | SÃO PAULO | Brasil | 3543709 | 35 | 33 | nan | nan | nan | Cerrado | 64.6 |
| d9c88026-844b-31b0-bccb-7e4d362e5707 | -21.605 | -47.9485 | 2024-10-07 00:57:05 | GOES-16 | RINCÃO | SÃO PAULO | Brasil | 3543709 | 35 | 33 | nan | nan | nan | Cerrado | 80.2 |
| cd537d14-95b7-3d64-b364-3d1d1fd5f19a | -22.1974 | -48.1778 | 2024-10-07 00:57:08 | GOES-16 | BROTAS | SÃO PAULO | Brasil | 3507902 | 35 | 33 | nan | nan | nan | Cerrado | 101.6 |
| de26e57b-d6d2-365b-b22a-9003c72513d7 | -22.3922 | -48.598 | 2024-10-07 00:57:09 | GOES-16 | JAÚ | SÃO PAULO | Brasil | 3525300 | 35 | 33 | nan | nan | nan | Mata Atlântica | 65.0 |
| 01766150-c3ff-3947-84a9-27c5b86d7f67 | -22.7198 | -53.2341 | 2024-10-07 00:57:11 | GOES-16 | BATAYPORÃ | MATO GROSSO DO SUL | Brasil | 5002001 | 50 | 33 | nan | nan | nan | Mata Atlântica | 62.6 |
| 12585fb1-ee0c-3a6d-a26c-05f75b0664f5 | -21.56 | -47.77 | 2024-10-07 01:03:22 | MSG-03 | LUÍS ANTÔNIO | SÃO PAULO | Brasil | 3527603 | 35 | 33 | nan | nan | nan | Cerrado | nan |
| a7bc5f25-1a85-3f10-b96c-ecba3e73e4c4 | -21.55 | -47.72 | 2024-10-07 01:03:22 | MSG-03 | LUÍS ANTÔNIO | SÃO PAULO | Brasil | 3527603 | 35 | 33 | nan | nan | nan | Cerrado | nan |
| 692ae041-ad6f-388b-aaff-d745dd9bbdc2 | -21.59 | -47.79 | 2024-10-07 01:03:22 | MSG-03 | LUÍS ANTÔNIO | SÃO PAULO | Brasil | 3527603 | 35 | 33 | nan | nan | nan | Cerrado | nan |
| 21d2ff6b-b2b1-3cfa-831e-7e71afeb3a65 | -21.59 | -47.73 | 2024-10-07 01:03:22 | MSG-03 | LUÍS ANTÔNIO | SÃO PAULO | Brasil | 3527603 | 35 | 33 | nan | nan | nan | Cerrado | nan |
| 64989975-1396-3a99-89a2-d292a871edda | -20.1 | -49.09 | 2024-10-07 01:03:30 | MSG-03 | FRUTAL | MINAS GERAIS | Brasil | 3127107 | 31 | 33 | nan | nan | nan | Cerrado | nan |
| 6af10dff-fe0d-36c5-b46e-2afad04ae237 | -20.1 | -49.04 | 2024-10-07 01:03:30 | MSG-03 | FRUTAL | MINAS GERAIS | Brasil | 3127107 | 31 | 33 | nan | nan | nan | Cerrado | nan |
| 8e366009-42e3-32e0-9465-c067722aa4c9 | -20.13 | -49.11 | 2024-10-07 01:03:30 | MSG-03 | FRUTAL | MINAS GERAIS | Brasil | 3127107 | 31 | 33 | nan | nan | nan | Cerrado | nan |


[Clique aqui para ver as próximas entradas](README14.md)
