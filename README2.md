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

## Dados Diários - Página 2

| ID | Latitude | Longitude | Data/Hora GMT | Satélite | Município | Estado | País | Município ID | Estado ID | País ID | Dias sem Chuva | Precipitação | Risco de Fogo | Bioma | FRP |
|----|----------|-----------|---------------|----------|-----------|--------|------|--------------|-----------|---------|----------------|--------------|----------------|-------|-----|
| 55dc0250-8e44-3e27-9e10-9cf72e161c2a | -2.7602 | -54.4349 | 2024-11-03 00:15:22 | GOES-16 | SANTARÉM | PARÁ | Brasil | 1506807 | 15 | 33 | nan | nan | nan | Amazônia | 191.2 |
| 0b9646a5-2c30-34a6-b184-382b4ba95348 | -2.7603 | -54.4149 | 2024-11-03 00:15:22 | GOES-16 | SANTARÉM | PARÁ | Brasil | 1506807 | 15 | 33 | nan | nan | nan | Amazônia | 174.8 |
| d1169478-9b70-385c-b572-d7f86c4f2ccb | -2.7876 | -51.6099 | 2024-11-03 00:15:22 | GOES-16 | ANAPU | PARÁ | Brasil | 1500859 | 15 | 33 | nan | nan | nan | Amazônia | 84.6 |
| 12642a91-a344-37c7-9e69-adc4d7c734c8 | -3.055 | -54.1675 | 2024-11-03 00:15:23 | GOES-16 | SANTARÉM | PARÁ | Brasil | 1506807 | 15 | 33 | nan | nan | nan | Amazônia | 66.2 |
| b9319732-23c1-3a14-ae13-e14afb6b21a0 | -3.0365 | -54.2081 | 2024-11-03 00:15:23 | GOES-16 | SANTARÉM | PARÁ | Brasil | 1506807 | 15 | 33 | nan | nan | nan | Amazônia | 54.3 |
| 60147fb2-a862-34d1-9dfc-f3dce96421b9 | -3.0397 | -53.2603 | 2024-11-03 00:15:23 | GOES-16 | MEDICILÂNDIA | PARÁ | Brasil | 1504455 | 15 | 33 | nan | nan | nan | Amazônia | 66.8 |
| 8a425658-6035-383a-abee-cce3bf58016c | -3.0732 | -45.0275 | 2024-11-03 00:15:23 | GOES-16 | MATINHA | MARANHÃO | Brasil | 2106508 | 21 | 33 | nan | nan | nan | Amazônia | 67.3 |
| 7a672e4a-f515-3a8d-8b85-7a20576ae37c | -3.055 | -54.1474 | 2024-11-03 00:15:23 | GOES-16 | SANTARÉM | PARÁ | Brasil | 1506807 | 15 | 33 | nan | nan | nan | Amazônia | 118.7 |
| 77780b16-9c92-3c32-a736-9969326d86cc | -3.0734 | -54.167 | 2024-11-03 00:15:24 | GOES-16 | SANTARÉM | PARÁ | Brasil | 1506807 | 15 | 33 | nan | nan | nan | Amazônia | 122.0 |
| 9c7d8e20-c36a-369b-aba8-5618e0a0e031 | -3.0734 | -54.147 | 2024-11-03 00:15:24 | GOES-16 | SANTARÉM | PARÁ | Brasil | 1506807 | 15 | 33 | nan | nan | nan | Amazônia | 192.3 |
| c7b42b07-b5ea-3c4b-87a0-a03d1c67f25e | -3.0917 | -54.1666 | 2024-11-03 00:15:24 | GOES-16 | SANTARÉM | PARÁ | Brasil | 1506807 | 15 | 33 | nan | nan | nan | Amazônia | 53.0 |
| e26ac81b-4046-3ac0-aba9-7384c0abd6ef | -3.0918 | -54.1465 | 2024-11-03 00:15:24 | GOES-16 | SANTARÉM | PARÁ | Brasil | 1506807 | 15 | 33 | nan | nan | nan | Amazônia | 67.2 |
| d71374ae-cdb0-3baa-9905-95e5d7fef6cb | -3.106 | -50.2896 | 2024-11-03 00:15:24 | GOES-16 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 52.3 |
| 3db2ad11-34a8-3e8b-b13a-9ef8ae0cffcc | -3.1212 | -51.1244 | 2024-11-03 00:15:24 | GOES-16 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 64.7 |
| 31328d55-b6b3-311c-be86-a38b12e7b105 | -3.1213 | -51.1036 | 2024-11-03 00:15:24 | GOES-16 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 73.7 |
| 051adb5e-a8fe-3664-96c2-2d1f2997ba7b | -3.1282 | -54.2459 | 2024-11-03 00:15:24 | GOES-16 | MOJUÍ DOS CAMPOS | PARÁ | Brasil | 1504752 | 15 | 33 | nan | nan | nan | Amazônia | 62.3 |
| c6b4a809-ab89-3ddf-a168-591befdf6b74 | -3.2415 | -53.3967 | 2024-11-03 00:15:24 | GOES-16 | MEDICILÂNDIA | PARÁ | Brasil | 1504455 | 15 | 33 | nan | nan | nan | Amazônia | 61.0 |
| 33bc66dd-fc23-3093-a1d0-4f94d77bf04b | -3.2599 | -53.4164 | 2024-11-03 00:15:25 | GOES-16 | MEDICILÂNDIA | PARÁ | Brasil | 1504455 | 15 | 33 | nan | nan | nan | Amazônia | 68.2 |
| 10399373-56d0-346b-ac1d-b4ab1a8a18ac | -3.2624 | -52.746 | 2024-11-03 00:15:25 | GOES-16 | BRASIL NOVO | PARÁ | Brasil | 1501725 | 15 | 33 | nan | nan | nan | Amazônia | 55.7 |
| 3b627dd7-e5f5-359e-a03f-ec97a101ccf6 | -3.2624 | -52.7256 | 2024-11-03 00:15:25 | GOES-16 | BRASIL NOVO | PARÁ | Brasil | 1501725 | 15 | 33 | nan | nan | nan | Amazônia | 64.2 |
| aa47c31a-1ebf-3c9d-ba9f-fcafd3f162f1 | -3.2808 | -52.7455 | 2024-11-03 00:15:25 | GOES-16 | MEDICILÂNDIA | PARÁ | Brasil | 1504455 | 15 | 33 | nan | nan | nan | Amazônia | 99.9 |
| 4a584c96-1c1d-321b-b2ab-e102bc5bdb36 | -3.2808 | -52.7251 | 2024-11-03 00:15:25 | GOES-16 | BRASIL NOVO | PARÁ | Brasil | 1501725 | 15 | 33 | nan | nan | nan | Amazônia | 131.4 |
| a5229154-d149-3e5c-aba7-358757571ba7 | -3.3276 | -50.2825 | 2024-11-03 00:15:25 | GOES-16 | PACAJÁ | PARÁ | Brasil | 1505486 | 15 | 33 | nan | nan | nan | Amazônia | 110.3 |
| e870d202-16f1-336e-892f-d540c03bf614 | -3.3277 | -50.2615 | 2024-11-03 00:15:25 | GOES-16 | PACAJÁ | PARÁ | Brasil | 1505486 | 15 | 33 | nan | nan | nan | Amazônia | 106.6 |
| f5fcfe79-c1e9-3160-9453-b9a48688fdfc | -3.3461 | -50.2819 | 2024-11-03 00:15:25 | GOES-16 | PACAJÁ | PARÁ | Brasil | 1505486 | 15 | 33 | nan | nan | nan | Amazônia | 65.5 |
| 48f6c4a8-384b-36b3-aada-b04700aa5014 | -3.3461 | -50.2609 | 2024-11-03 00:15:25 | GOES-16 | PACAJÁ | PARÁ | Brasil | 1505486 | 15 | 33 | nan | nan | nan | Amazônia | 71.8 |
| 788d6140-c8a2-3bae-998c-dd4729025f84 | -3.4749 | -50.3826 | 2024-11-03 00:15:26 | GOES-16 | PACAJÁ | PARÁ | Brasil | 1505486 | 15 | 33 | nan | nan | nan | Amazônia | 130.0 |
| 561cc222-db1c-338b-8ee0-dc52071f5ae5 | -3.5466 | -50.8611 | 2024-11-03 00:15:26 | GOES-16 | PACAJÁ | PARÁ | Brasil | 1505486 | 15 | 33 | nan | nan | nan | Amazônia | 63.7 |
| dea3b0a5-2f8f-33b2-a8b0-0f43acf8c933 | -3.967 | -48.15 | 2024-11-03 00:15:28 | GOES-16 | DOM ELISEU | PARÁ | Brasil | 1502939 | 15 | 33 | nan | nan | nan | Amazônia | 63.5 |
| 1a506dcd-8ce0-3c2e-9e45-a7e91c5c28cf | -4.0283 | -47.146 | 2024-11-03 00:15:29 | GOES-16 | ITINGA DO MARANHÃO | MARANHÃO | Brasil | 2105427 | 21 | 33 | nan | nan | nan | Amazônia | 65.4 |
| ef5b9e73-b339-3874-a20d-e9db0babd564 | -4.8723 | -48.7318 | 2024-11-03 00:15:34 | GOES-16 | BOM JESUS DO TOCANTINS | PARÁ | Brasil | 1501576 | 15 | 33 | nan | nan | nan | Amazônia | 62.7 |
| e093fc95-ea2d-34cb-85e7-2f570a59bf9f | -8.7059 | -48.0181 | 2024-11-03 00:15:55 | GOES-16 | SANTA MARIA DO TOCANTINS | TOCANTINS | Brasil | 1718881 | 17 | 33 | nan | nan | nan | Cerrado | 65.9 |
| 0247f613-64ae-313c-b25b-c251d9ad0cfc | -8.7062 | -47.9962 | 2024-11-03 00:15:55 | GOES-16 | SANTA MARIA DO TOCANTINS | TOCANTINS | Brasil | 1718881 | 17 | 33 | nan | nan | nan | Cerrado | 47.6 |
| 60575812-9661-3ae2-a313-3532b5ae99d8 | -8.7247 | -48.0163 | 2024-11-03 00:15:55 | GOES-16 | SANTA MARIA DO TOCANTINS | TOCANTINS | Brasil | 1718881 | 17 | 33 | nan | nan | nan | Cerrado | 87.8 |
| 22d619b0-0268-3bd8-a8cc-691e5e8f1bb4 | -8.725 | -47.9944 | 2024-11-03 00:15:55 | GOES-16 | SANTA MARIA DO TOCANTINS | TOCANTINS | Brasil | 1718881 | 17 | 33 | nan | nan | nan | Cerrado | 59.5 |
| 0cc54a06-afb8-3d5f-8b83-c6046f0b6615 | -10.8426 | -49.1453 | 2024-11-03 00:16:07 | GOES-16 | SANTA RITA DO TOCANTINS | TOCANTINS | Brasil | 1718899 | 17 | 33 | nan | nan | nan | Cerrado | 56.0 |
| fe126331-0a07-3b24-a901-13cb9f63c85e | -10.8815 | -49.0757 | 2024-11-03 00:16:08 | GOES-16 | SANTA RITA DO TOCANTINS | TOCANTINS | Brasil | 1718899 | 17 | 33 | nan | nan | nan | Cerrado | 62.2 |
| 22251d97-c9ef-3b55-8102-1e63825cfb15 | -11.2819 | -56.144 | 2024-11-03 00:16:10 | GOES-16 | TABAPORÃ | MATO GROSSO | Brasil | 5107941 | 51 | 33 | nan | nan | nan | Amazônia | 77.8 |
| 334807a2-4d61-35c7-86cb-e79eec6fc84e | -15.3969 | -39.1493 | 2024-11-03 00:21:56 | METOP-C | UNA | BAHIA | Brasil | 2932507 | 29 | 33 | nan | nan | nan | Mata Atlântica | nan |
| 914934fe-c657-39a9-a7f0-c3983af07158 | -15.9514 | -43.5569 | 2024-11-03 00:22:02 | METOP-C | CAPITÃO ENÉAS | MINAS GERAIS | Brasil | 3112703 | 31 | 33 | nan | nan | nan | Cerrado | nan |
| 9e4aef06-f06a-325e-a3c6-3610233bea65 | -15.3857 | -43.0588 | 2024-11-03 00:22:10 | METOP-C | CATUTI | MINAS GERAIS | Brasil | 3115474 | 31 | 33 | nan | nan | nan | Caatinga | nan |
| 27942b74-8bb3-33b9-8928-50a20c16e4c3 | -15.2269 | -43.325401 | 2024-11-03 00:22:13 | METOP-C | JAÍBA | MINAS GERAIS | Brasil | 3135050 | 31 | 33 | nan | nan | nan | Caatinga | nan |
| 8ece949b-e2ec-34c8-b8f5-94a6b16173bb | -15.2286 | -43.333698 | 2024-11-03 00:22:13 | METOP-C | JAÍBA | MINAS GERAIS | Brasil | 3135050 | 31 | 33 | nan | nan | nan | Caatinga | nan |
| d95c20b1-66d5-3871-a090-ae4b6987d4e0 | -13.5414 | -39.789799 | 2024-11-03 00:22:28 | METOP-C | WENCESLAU GUIMARÃES | BAHIA | Brasil | 2933505 | 29 | 33 | nan | nan | nan | Mata Atlântica | nan |
| 8b1ed97e-0a00-3e88-8e56-d22b2ceddd21 | -13.543 | -39.796902 | 2024-11-03 00:22:28 | METOP-C | ITAQUARA | BAHIA | Brasil | 2916708 | 29 | 33 | nan | nan | nan | Mata Atlântica | nan |
| 792c1cfd-d1e2-39f7-bc16-4f706049aec8 | -13.8768 | -43.341 | 2024-11-03 00:22:35 | METOP-C | RIACHO DE SANTANA | BAHIA | Brasil | 2926400 | 29 | 33 | nan | nan | nan | Caatinga | nan |
| 2404654e-8404-3575-bdab-19757803a8f7 | -11.5388 | -40.416599 | 2024-11-03 00:23:03 | METOP-C | MIGUEL CALMON | BAHIA | Brasil | 2921203 | 29 | 33 | nan | nan | nan | Caatinga | nan |
| 8522ea4c-fab1-3a57-8f76-966fc71de8bb | -11.5372 | -40.409599 | 2024-11-03 00:23:03 | METOP-C | MIGUEL CALMON | BAHIA | Brasil | 2921203 | 29 | 33 | nan | nan | nan | Caatinga | nan |
| 40341b97-a053-3cd5-b395-f75c29d259df | -10.0837 | -36.373798 | 2024-11-03 00:23:11 | METOP-C | CORURIPE | ALAGOAS | Brasil | 2702306 | 27 | 33 | nan | nan | nan | Caatinga | nan |
| 10cd9667-0a19-3cc6-8296-35efe36fc2d2 | -10.0811 | -36.362999 | 2024-11-03 00:23:11 | METOP-C | CORURIPE | ALAGOAS | Brasil | 2702306 | 27 | 33 | nan | nan | nan | Caatinga | nan |
| d641be24-cde3-3e5f-b35e-30c91a2640c5 | -11.8077 | -48.070702 | 2024-11-03 00:23:25 | METOP-C | SÃO VALÉRIO | TOCANTINS | Brasil | 1720499 | 17 | 33 | nan | nan | nan | Cerrado | nan |
| f60a9596-56c4-3f16-9d5f-f522e9a49818 | -11.7979 | -48.072701 | 2024-11-03 00:23:25 | METOP-C | SÃO VALÉRIO | TOCANTINS | Brasil | 1720499 | 17 | 33 | nan | nan | nan | Cerrado | nan |
| d418ecb9-e21a-3ce4-9911-866871628243 | -11.0497 | -45.362598 | 2024-11-03 00:23:28 | METOP-C | FORMOSA DO RIO PRETO | BAHIA | Brasil | 2911105 | 29 | 33 | nan | nan | nan | Cerrado | nan |
| 41a7294b-c73a-3431-a6fd-f40753db0b65 | -11.0517 | -45.371899 | 2024-11-03 00:23:28 | METOP-C | FORMOSA DO RIO PRETO | BAHIA | Brasil | 2911105 | 29 | 33 | nan | nan | nan | Cerrado | nan |
| 366845b9-b801-3e9e-b44c-20947e0884da | -11.0537 | -45.381199 | 2024-11-03 00:23:28 | METOP-C | FORMOSA DO RIO PRETO | BAHIA | Brasil | 2911105 | 29 | 33 | nan | nan | nan | Cerrado | nan |
| e1e2f0ba-4c4b-3003-bfc4-291969898e84 | -10.8007 | -44.491901 | 2024-11-03 00:23:29 | METOP-C | SANTA RITA DE CÁSSIA | BAHIA | Brasil | 2928406 | 29 | 33 | nan | nan | nan | Cerrado | nan |
| b59bcf18-87fe-35f9-9803-e59419b76a82 | -10.8025 | -44.500198 | 2024-11-03 00:23:29 | METOP-C | SANTA RITA DE CÁSSIA | BAHIA | Brasil | 2928406 | 29 | 33 | nan | nan | nan | Cerrado | nan |
| 11fba6c6-d1a6-32c3-8918-0e8139040593 | -9.7922 | -43.8727 | 2024-11-03 00:23:43 | METOP-C | MORRO CABEÇA NO TEMPO | PIAUÍ | Brasil | 2206654 | 22 | 33 | nan | nan | nan | Cerrado | nan |
| d12c3e02-b8ce-3bc4-bc5c-fdeb05003592 | -10.9126 | -49.263699 | 2024-11-03 00:23:44 | METOP-C | SANTA RITA DO TOCANTINS | TOCANTINS | Brasil | 1718899 | 17 | 33 | nan | nan | nan | Cerrado | nan |
| 4c7c367f-77b6-372c-8f69-d332176344e0 | -10.8636 | -49.071602 | 2024-11-03 00:23:44 | METOP-C | SANTA RITA DO TOCANTINS | TOCANTINS | Brasil | 1718899 | 17 | 33 | nan | nan | nan | Cerrado | nan |
| 4bede886-598c-3ec6-b710-e9214e2c2173 | -10.8668 | -49.087601 | 2024-11-03 00:23:44 | METOP-C | SANTA RITA DO TOCANTINS | TOCANTINS | Brasil | 1718899 | 17 | 33 | nan | nan | nan | Cerrado | nan |
| cd35aae0-657a-3dd5-9f2e-11443a84a43a | -10.857 | -49.0896 | 2024-11-03 00:23:44 | METOP-C | SANTA RITA DO TOCANTINS | TOCANTINS | Brasil | 1718899 | 17 | 33 | nan | nan | nan | Cerrado | nan |
| 1af32ee2-f3d0-359e-ad57-984cdd15a44d | -8.6047 | -40.5378 | 2024-11-03 00:23:50 | METOP-C | DORMENTES | PERNAMBUCO | Brasil | 2605152 | 26 | 33 | nan | nan | nan | Caatinga | nan |
| d5785d9a-9f1c-3bd9-b8cf-7a8c9fa7d61d | -9.1052 | -43.188801 | 2024-11-03 00:23:52 | METOP-C | JUREMA | PIAUÍ | Brasil | 2205532 | 22 | 33 | nan | nan | nan | Caatinga | nan |
| a8ba1531-163a-3fbf-90ee-f1f8735b5726 | -8.4099 | -40.454601 | 2024-11-03 00:23:53 | METOP-C | DORMENTES | PERNAMBUCO | Brasil | 2605152 | 26 | 33 | nan | nan | nan | Caatinga | nan |
| 5184109d-7ef3-3ceb-8587-9901316f7a22 | -8.4116 | -40.4618 | 2024-11-03 00:23:53 | METOP-C | DORMENTES | PERNAMBUCO | Brasil | 2605152 | 26 | 33 | nan | nan | nan | Caatinga | nan |
| 944545d1-5790-30db-8cff-2576895dac71 | -8.4872 | -42.0938 | 2024-11-03 00:23:58 | METOP-C | CAPITÃO GERVÁSIO OLIVEIRA | PIAUÍ | Brasil | 2202455 | 22 | 33 | nan | nan | nan | Caatinga | nan |
| d45d1b78-5cbd-3963-926a-0a9124124751 | -8.4888 | -42.100601 | 2024-11-03 00:23:58 | METOP-C | CAPITÃO GERVÁSIO OLIVEIRA | PIAUÍ | Brasil | 2202455 | 22 | 33 | nan | nan | nan | Caatinga | nan |
| edabd7b0-c024-3a91-916a-1000f0957c54 | -7.8595 | -39.555698 | 2024-11-03 00:23:59 | METOP-C | SERRITA | PERNAMBUCO | Brasil | 2614006 | 26 | 33 | nan | nan | nan | Caatinga | nan |
| abb698a0-6604-3432-93bd-559d4c90973c | -7.8613 | -39.5634 | 2024-11-03 00:23:59 | METOP-C | SERRITA | PERNAMBUCO | Brasil | 2614006 | 26 | 33 | nan | nan | nan | Caatinga | nan |
| 216a5cdf-ed61-31bd-a4f6-7d625b28dbc2 | -8.3365 | -43.571499 | 2024-11-03 00:24:06 | METOP-C | CANTO DO BURITI | PIAUÍ | Brasil | 2202307 | 22 | 33 | nan | nan | nan | Cerrado | nan |
| 4cffed41-6353-3930-ac7f-b93c6f35475f | -8.3381 | -43.5788 | 2024-11-03 00:24:06 | METOP-C | CANTO DO BURITI | PIAUÍ | Brasil | 2202307 | 22 | 33 | nan | nan | nan | Cerrado | nan |
| 89829d24-1c62-35a1-89cf-14d3fd928db0 | -8.3267 | -43.5737 | 2024-11-03 00:24:06 | METOP-C | CANTO DO BURITI | PIAUÍ | Brasil | 2202307 | 22 | 33 | nan | nan | nan | Cerrado | nan |
| a7fe1d9f-e1d4-374b-9edd-2bd4ba764d5f | -8.3283 | -43.581001 | 2024-11-03 00:24:06 | METOP-C | CANTO DO BURITI | PIAUÍ | Brasil | 2202307 | 22 | 33 | nan | nan | nan | Cerrado | nan |
| bcd119f1-6594-3eb8-adc1-89bbec181a77 | -8.3299 | -43.5882 | 2024-11-03 00:24:06 | METOP-C | CANTO DO BURITI | PIAUÍ | Brasil | 2202307 | 22 | 33 | nan | nan | nan | Cerrado | nan |
| 0862ac1a-e855-3ae6-a3ea-b0f41a69b439 | -6.7722 | -37.5397 | 2024-11-03 00:24:09 | METOP-C | SÃO JOSÉ DE ESPINHARAS | PARAÍBA | Brasil | 2514404 | 25 | 33 | nan | nan | nan | Caatinga | nan |
| f95351ec-fe76-3754-8a1a-380023ed6617 | -6.6941 | -37.472198 | 2024-11-03 00:24:10 | METOP-C | SERRA NEGRA DO NORTE | RIO GRANDE DO NORTE | Brasil | 2413409 | 24 | 33 | nan | nan | nan | Caatinga | nan |
| 2b237448-0913-3c48-afb2-efe0dad5ca00 | -6.6966 | -37.482399 | 2024-11-03 00:24:10 | METOP-C | PAULISTA | PARAÍBA | Brasil | 2510907 | 25 | 33 | nan | nan | nan | Caatinga | nan |
| 286ab90c-04b0-3737-bb58-c994f428640a | -7.9975 | -43.345501 | 2024-11-03 00:24:11 | METOP-C | PAVUSSU | PIAUÍ | Brasil | 2207850 | 22 | 33 | nan | nan | nan | Caatinga | nan |
| 9518be72-907d-37f0-a7df-37b3922a089d | -7.9991 | -43.3526 | 2024-11-03 00:24:11 | METOP-C | PAVUSSU | PIAUÍ | Brasil | 2207850 | 22 | 33 | nan | nan | nan | Caatinga | nan |
| 20e5a8bd-731a-3732-8850-bb7475cf222b | -6.4372 | -37.132599 | 2024-11-03 00:24:12 | METOP-C | CAICÓ | RIO GRANDE DO NORTE | Brasil | 2402006 | 24 | 33 | nan | nan | nan | Caatinga | nan |
| a3b17d50-b75b-368c-9da1-d41fdf03ce9a | -6.4275 | -37.134899 | 2024-11-03 00:24:13 | METOP-C | CAICÓ | RIO GRANDE DO NORTE | Brasil | 2402006 | 24 | 33 | nan | nan | nan | Caatinga | nan |
| bdb1400e-1ef1-340c-acff-b17cde778330 | -8.8329 | -47.725601 | 2024-11-03 00:24:13 | METOP-C | SANTA MARIA DO TOCANTINS | TOCANTINS | Brasil | 1718881 | 17 | 33 | nan | nan | nan | Cerrado | nan |
| 701fb840-a55f-36ea-9918-9ec2b034220b | -7.1756 | -40.918701 | 2024-11-03 00:24:15 | METOP-C | VILA NOVA DO PIAUÍ | PIAUÍ | Brasil | 2211605 | 22 | 33 | nan | nan | nan | Caatinga | nan |
| b799a390-6fdd-371a-a0c0-451b9e37eadf | -8.7064 | -47.994701 | 2024-11-03 00:24:16 | METOP-C | SANTA MARIA DO TOCANTINS | TOCANTINS | Brasil | 1718881 | 17 | 33 | nan | nan | nan | Cerrado | nan |
| 53ead3ef-ded7-3083-b2f6-a45bb3a65f8b | -8.7091 | -48.007099 | 2024-11-03 00:24:16 | METOP-C | SANTA MARIA DO TOCANTINS | TOCANTINS | Brasil | 1718881 | 17 | 33 | nan | nan | nan | Cerrado | nan |
| 9774dc63-090d-3973-8ee0-1f3715ca55d5 | -8.7117 | -48.0196 | 2024-11-03 00:24:16 | METOP-C | SANTA MARIA DO TOCANTINS | TOCANTINS | Brasil | 1718881 | 17 | 33 | nan | nan | nan | Cerrado | nan |
| 28dedf91-55de-34f1-bb67-84d629a864c9 | -8.6993 | -48.009201 | 2024-11-03 00:24:16 | METOP-C | SANTA MARIA DO TOCANTINS | TOCANTINS | Brasil | 1718881 | 17 | 33 | nan | nan | nan | Cerrado | nan |
| e544de09-1204-3ce0-8b6e-8856bc50fee9 | -7.1126 | -42.577 | 2024-11-03 00:24:22 | METOP-C | SÃO FRANCISCO DO PIAUÍ | PIAUÍ | Brasil | 2209708 | 22 | 33 | nan | nan | nan | Caatinga | nan |
| 5822bb86-c9f3-3b15-ac10-c86fb3efdcc5 | -7.1111 | -42.570099 | 2024-11-03 00:24:22 | METOP-C | SÃO FRANCISCO DO PIAUÍ | PIAUÍ | Brasil | 2209708 | 22 | 33 | nan | nan | nan | Caatinga | nan |
| 77bb8b10-9954-3c41-9f67-468ae2be5e80 | -6.2905 | -39.513 | 2024-11-03 00:24:24 | METOP-C | ACOPIARA | CEARÁ | Brasil | 2300309 | 23 | 33 | nan | nan | nan | Caatinga | nan |
| e569a7fd-b70d-3cae-bde1-9222f2c4f68d | -7.4112 | -44.727299 | 2024-11-03 00:24:25 | METOP-C | URUÇUÍ | PIAUÍ | Brasil | 2211209 | 22 | 33 | nan | nan | nan | Cerrado | nan |
| 1aeac4e6-ceda-3cf2-b73c-18756f476182 | -7.4424 | -44.7286 | 2024-11-03 00:24:25 | METOP-C | URUÇUÍ | PIAUÍ | Brasil | 2211209 | 22 | 33 | nan | nan | nan | Cerrado | nan |
| 43a5d3f3-4ba4-3c2a-a67a-d5dfe547b436 | -7.421 | -44.725101 | 2024-11-03 00:24:25 | METOP-C | URUÇUÍ | PIAUÍ | Brasil | 2211209 | 22 | 33 | nan | nan | nan | Cerrado | nan |
| a70897b7-6344-38b7-b648-fbc213862988 | -7.4228 | -44.732899 | 2024-11-03 00:24:25 | METOP-C | URUÇUÍ | PIAUÍ | Brasil | 2211209 | 22 | 33 | nan | nan | nan | Cerrado | nan |
| 5cc4b567-e2b9-33ea-8de7-e67bf7803a82 | -7.413 | -44.7351 | 2024-11-03 00:24:25 | METOP-C | URUÇUÍ | PIAUÍ | Brasil | 2211209 | 22 | 33 | nan | nan | nan | Cerrado | nan |
| b86e1b94-717b-3c28-ab06-e87d3ebe7c3c | -7.4014 | -44.729401 | 2024-11-03 00:24:25 | METOP-C | URUÇUÍ | PIAUÍ | Brasil | 2211209 | 22 | 33 | nan | nan | nan | Cerrado | nan |
| a4819ec2-4bdf-3b64-b47a-ab170476cff5 | -7.4406 | -44.720798 | 2024-11-03 00:24:25 | METOP-C | URUÇUÍ | PIAUÍ | Brasil | 2211209 | 22 | 33 | nan | nan | nan | Cerrado | nan |
| 8f77f955-1672-3b34-ba91-761f50f25030 | -6.5213 | -41.481499 | 2024-11-03 00:24:28 | METOP-C | LAGOA DO SÍTIO | PIAUÍ | Brasil | 2205599 | 22 | 33 | nan | nan | nan | Caatinga | nan |
| b72be08e-fd4a-3072-bafb-cd5d4f33aa75 | -6.5229 | -41.488499 | 2024-11-03 00:24:28 | METOP-C | LAGOA DO SÍTIO | PIAUÍ | Brasil | 2205599 | 22 | 33 | nan | nan | nan | Caatinga | nan |


[Clique aqui para ver as próximas entradas](README3.md)
