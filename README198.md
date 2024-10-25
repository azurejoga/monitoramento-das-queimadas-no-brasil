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

## Dados Diários - Página 198

| ID | Latitude | Longitude | Data/Hora GMT | Satélite | Município | Estado | País | Município ID | Estado ID | País ID | Dias sem Chuva | Precipitação | Risco de Fogo | Bioma | FRP |
|----|----------|-----------|---------------|----------|-----------|--------|------|--------------|-----------|---------|----------------|--------------|----------------|-------|-----|
| 9e33ddeb-d596-322b-b699-eb4e39051b7e | -5.7858 | -41.9179 | 2024-10-25 19:35:38 | GOES-16 | SÃO MIGUEL DO TAPUIO | PIAUÍ | Brasil | 2210409 | 22 | 33 | nan | nan | nan | Caatinga | 66.5 |
| f78cf8ce-da50-3dcc-8224-fda49fd2d3a0 | -5.8323 | -47.1987 | 2024-10-25 19:35:38 | GOES-16 | MONTES ALTOS | MARANHÃO | Brasil | 2107001 | 21 | 33 | nan | nan | nan | Cerrado | 53.9 |
| 287df100-453d-351e-a094-7af116d3f085 | -5.8324 | -47.1767 | 2024-10-25 19:35:38 | GOES-16 | MONTES ALTOS | MARANHÃO | Brasil | 2107001 | 21 | 33 | nan | nan | nan | Cerrado | 54.3 |
| 56672702-85e3-3a1c-94cd-995f5c8184dc | -5.8961 | -44.16 | 2024-10-25 19:35:38 | GOES-16 | JATOBÁ | MARANHÃO | Brasil | 2105450 | 21 | 33 | nan | nan | nan | Cerrado | 85.7 |
| 67af6a83-67b3-3a8f-8a7a-3d2ec3e7b35d | -6.2085 | -48.9973 | 2024-10-25 19:35:40 | GOES-16 | SÃO GERALDO DO ARAGUAIA | PARÁ | Brasil | 1507458 | 15 | 33 | nan | nan | nan | Amazônia | 61.0 |
| 20f3a23e-7788-35d8-89e3-bdeb353bc259 | -6.1324 | -47.0022 | 2024-10-25 19:35:40 | GOES-16 | LAJEADO NOVO | MARANHÃO | Brasil | 2105989 | 21 | 33 | nan | nan | nan | Cerrado | 69.1 |
| a326fe96-6d21-3b0e-8675-a87037dcb7dc | -6.2931 | -47.824 | 2024-10-25 19:35:41 | GOES-16 | NAZARÉ | TOCANTINS | Brasil | 1714302 | 17 | 33 | nan | nan | nan | Cerrado | 306.2 |
| ce098e63-e55f-352b-a25f-35b09eb62375 | -6.2744 | -47.8253 | 2024-10-25 19:35:41 | GOES-16 | NAZARÉ | TOCANTINS | Brasil | 1714302 | 17 | 33 | nan | nan | nan | Cerrado | 100.8 |
| c68cdd50-ffba-388e-bdac-8a127827fd99 | -6.5241 | -47.04 | 2024-10-25 19:35:42 | GOES-16 | SÃO JOÃO DO PARAÍSO | MARANHÃO | Brasil | 2111052 | 21 | 33 | nan | nan | nan | Cerrado | 93.2 |
| 27e64cd6-cdeb-3789-9342-19b74c69adf7 | -6.5297 | -42.7091 | 2024-10-25 19:35:42 | GOES-16 | FRANCISCO AYRES | PIAUÍ | Brasil | 2204105 | 22 | 33 | nan | nan | nan | Caatinga | 77.9 |
| d89ba4b8-c134-3cfa-afb3-676fa9824973 | -6.7045 | -43.9554 | 2024-10-25 19:35:43 | GOES-16 | NOVA IORQUE | MARANHÃO | Brasil | 2107308 | 21 | 33 | nan | nan | nan | Cerrado | 65.9 |
| 610f35a5-2f22-3aa3-be04-2efcb452a084 | -6.7096 | -43.4673 | 2024-10-25 19:35:43 | GOES-16 | SÃO JOÃO DOS PATOS | MARANHÃO | Brasil | 2111102 | 21 | 33 | nan | nan | nan | Cerrado | 108.9 |
| 1a7e5317-26f3-3565-8088-9bca647b846b | -6.8919 | -59.7821 | 2024-10-25 19:35:45 | GOES-16 | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 100.8 |
| 20272362-46fd-3d58-a2e0-1041be7dcb9b | -6.9952 | -46.6714 | 2024-10-25 19:35:45 | GOES-16 | FEIRA NOVA DO MARANHÃO | MARANHÃO | Brasil | 2104073 | 21 | 33 | nan | nan | nan | Cerrado | 58.4 |
| 92b1e9fa-6f1b-3fa0-a581-17363d9bf459 | -6.9275 | -60.0303 | 2024-10-25 19:35:45 | GOES-16 | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 90.6 |
| b15d70ec-75b2-35c9-be2f-13ed1c2da79b | -7.0548 | -46.3327 | 2024-10-25 19:35:45 | GOES-16 | NOVA COLINAS | MARANHÃO | Brasil | 2107258 | 21 | 33 | nan | nan | nan | Cerrado | 54.1 |
| 433833bc-eda6-3e2c-99b0-003760b8c18b | -7.1357 | -49.5111 | 2024-10-25 19:35:46 | GOES-16 | RIO MARIA | PARÁ | Brasil | 1506161 | 15 | 33 | nan | nan | nan | Amazônia | 99.6 |
| 8249502a-b840-34db-a4ce-9c0cbf3621b0 | -7.2943 | -44.9817 | 2024-10-25 19:35:46 | GOES-16 | SÃO FÉLIX DE BALSAS | MARANHÃO | Brasil | 2110807 | 21 | 33 | nan | nan | nan | Cerrado | 82.6 |
| 28fb6527-671f-3ced-a1c6-cc3514bb619a | -7.2946 | -44.9589 | 2024-10-25 19:35:46 | GOES-16 | SÃO FÉLIX DE BALSAS | MARANHÃO | Brasil | 2110807 | 21 | 33 | nan | nan | nan | Cerrado | 64.6 |
| 57386bb8-8749-3363-aef3-3a036af1687c | -7.1673 | -46.3233 | 2024-10-25 19:35:46 | GOES-16 | NOVA COLINAS | MARANHÃO | Brasil | 2107258 | 21 | 33 | nan | nan | nan | Cerrado | 66.3 |
| 3e466539-e133-3ec2-8972-76c20cb2814e | -7.5289 | -45.8434 | 2024-10-25 19:35:48 | GOES-16 | BALSAS | MARANHÃO | Brasil | 2101400 | 21 | 33 | nan | nan | nan | Cerrado | 67.5 |
| a0310f78-1746-3994-beab-a95ce9493dac | -7.6769 | -42.8573 | 2024-10-25 19:35:48 | GOES-16 | FLORES DO PIAUÍ | PIAUÍ | Brasil | 2203800 | 22 | 33 | nan | nan | nan | Caatinga | 97.8 |
| c9208953-1f72-3a56-96b9-b574e9bcbbfe | -7.5559 | -46.8017 | 2024-10-25 19:35:48 | GOES-16 | RIACHÃO | MARANHÃO | Brasil | 2109502 | 21 | 33 | nan | nan | nan | Cerrado | 70.8 |
| 0b1c0833-8dba-36de-a456-0e36e1df3db8 | -7.5477 | -45.8417 | 2024-10-25 19:35:48 | GOES-16 | BALSAS | MARANHÃO | Brasil | 2101400 | 21 | 33 | nan | nan | nan | Cerrado | 149.3 |
| 22836219-a565-3673-a833-8a7016b17a21 | -7.6815 | -47.3213 | 2024-10-25 19:35:49 | GOES-16 | CAROLINA | MARANHÃO | Brasil | 2102804 | 21 | 33 | nan | nan | nan | Cerrado | 78.7 |
| f8b6cf1a-c36e-30c2-b752-ca43c38ec4f0 | -7.6817 | -47.2992 | 2024-10-25 19:35:49 | GOES-16 | CAROLINA | MARANHÃO | Brasil | 2102804 | 21 | 33 | nan | nan | nan | Cerrado | 74.8 |
| 072c7a53-6b9c-33ec-aead-f5ba8300861a | -8.6142 | -44.8271 | 2024-10-25 19:35:54 | GOES-16 | CURRAIS | PIAUÍ | Brasil | 2203230 | 22 | 33 | nan | nan | nan | Cerrado | 76.6 |
| 720c63a1-c893-3ff9-a6bc-63512f886be9 | -9.0635 | -48.0051 | 2024-10-25 19:35:56 | GOES-16 | BOM JESUS DO TOCANTINS | TOCANTINS | Brasil | 1703305 | 17 | 33 | nan | nan | nan | Cerrado | 137.1 |
| 6b6678f8-c339-3357-a5bc-95b780b7fdb5 | -9.0824 | -48.0032 | 2024-10-25 19:35:57 | GOES-16 | BOM JESUS DO TOCANTINS | TOCANTINS | Brasil | 1703305 | 17 | 33 | nan | nan | nan | Cerrado | 169.2 |
| a2a16edb-ca24-35d8-8949-023e3e5a42e2 | -9.5073 | -47.2319 | 2024-10-25 19:35:59 | GOES-16 | RIO SONO | TOCANTINS | Brasil | 1718758 | 17 | 33 | nan | nan | nan | Cerrado | 129.7 |
| 650c4913-4054-38c3-90e4-fb1464255775 | -9.8391 | -47.8365 | 2024-10-25 19:36:01 | GOES-16 | RIO SONO | TOCANTINS | Brasil | 1718758 | 17 | 33 | nan | nan | nan | Cerrado | 105.4 |
| 814777a9-273a-3338-a020-08dc67b6cbb4 | -9.8201 | -47.8386 | 2024-10-25 19:36:01 | GOES-16 | RIO SONO | TOCANTINS | Brasil | 1718758 | 17 | 33 | nan | nan | nan | Cerrado | 146.7 |
| 70d58ae2-2500-3c70-9606-6d338f6c7faf | -10.6046 | -52.816 | 2024-10-25 19:36:05 | GOES-16 | SÃO JOSÉ DO XINGU | MATO GROSSO | Brasil | 5107354 | 51 | 33 | nan | nan | nan | Amazônia | 115.9 |
| 878d1b2e-85e5-3560-8c31-e7f7fff224dd | -10.6249 | -55.9757 | 2024-10-25 19:36:06 | GOES-16 | NOVA CANAÃ DO NORTE | MATO GROSSO | Brasil | 5106216 | 51 | 33 | nan | nan | nan | Amazônia | 117.3 |
| 871cc1e7-98f7-3c89-b735-f0e7a76812d0 | -11.5357 | -43.9853 | 2024-10-25 19:36:10 | GOES-16 | WANDERLEY | BAHIA | Brasil | 2933455 | 29 | 33 | nan | nan | nan | Cerrado | 130.0 |
| f6fffbf0-ef33-3d0d-9e34-20b1db6e05dd | -11.7095 | -43.9119 | 2024-10-25 19:36:11 | GOES-16 | WANDERLEY | BAHIA | Brasil | 2933455 | 29 | 33 | nan | nan | nan | Cerrado | 134.1 |
| a691bf72-96d3-3fb3-9dd2-5359eca56d52 | -11.9642 | -44.6676 | 2024-10-25 19:36:12 | GOES-16 | ANGICAL | BAHIA | Brasil | 2901403 | 29 | 33 | nan | nan | nan | Cerrado | 140.2 |
| 047f4b34-3d5d-3a68-b771-7787ddc61032 | -11.9028 | -43.8348 | 2024-10-25 19:36:12 | GOES-16 | WANDERLEY | BAHIA | Brasil | 2933455 | 29 | 33 | nan | nan | nan | Cerrado | 135.2 |
| 5371c05a-1419-3251-b5f7-4546d82af7b7 | -12.1179 | -43.6354 | 2024-10-25 19:36:13 | GOES-16 | MUQUÉM DO SÃO FRANCISCO | BAHIA | Brasil | 2922250 | 29 | 33 | nan | nan | nan | Cerrado | 99.1 |
| 846e3019-9332-3efc-8965-dbbed6e7c95b | -12.4612 | -43.7921 | 2024-10-25 19:36:15 | GOES-16 | BREJOLÂNDIA | BAHIA | Brasil | 2904407 | 29 | 33 | nan | nan | nan | Cerrado | 152.8 |
| a9177ea8-0982-3cd0-84dd-8bc312c9e7fe | -12.9693 | -43.469 | 2024-10-25 19:36:18 | GOES-16 | SÍTIO DO MATO | BAHIA | Brasil | 2930758 | 29 | 33 | nan | nan | nan | Cerrado | 96.1 |
| c5c116d0-68a4-3bd7-b2ca-3e86a8f9c495 | -13.5754 | -42.2996 | 2024-10-25 19:36:21 | GOES-16 | PARAMIRIM | BAHIA | Brasil | 2923605 | 29 | 33 | nan | nan | nan | Caatinga | 99.4 |
| b8ec59e7-bf35-3e02-a8c0-91b4f8c6909b | -14.7804 | -41.663 | 2024-10-25 19:36:27 | GOES-16 | PRESIDENTE JÂNIO QUADROS | BAHIA | Brasil | 2925709 | 29 | 33 | nan | nan | nan | Caatinga | 109.9 |
| 30208cbe-716d-3338-b808-39769d3cd5e8 | -19.6028 | -56.8996 | 2024-10-25 19:36:55 | GOES-16 | CORUMBÁ | MATO GROSSO DO SUL | Brasil | 5003207 | 50 | 33 | nan | nan | nan | Pantanal | 154.0 |
| 9d27a5b4-f56b-3307-b585-c9d958868d92 | -19.6024 | -56.9206 | 2024-10-25 19:36:55 | GOES-16 | CORUMBÁ | MATO GROSSO DO SUL | Brasil | 5003207 | 50 | 33 | nan | nan | nan | Pantanal | 105.6 |
| 36cc0f41-7ad0-3339-8561-46ed6407959e | -19.6434 | -56.873 | 2024-10-25 19:36:55 | GOES-16 | AQUIDAUANA | MATO GROSSO DO SUL | Brasil | 5001102 | 50 | 33 | nan | nan | nan | Pantanal | 111.1 |
| aa618cdf-b8ae-3c5a-89b0-e39eb5fd2126 | -19.6615 | -56.9751 | 2024-10-25 19:36:55 | GOES-16 | AQUIDAUANA | MATO GROSSO DO SUL | Brasil | 5001102 | 50 | 33 | nan | nan | nan | Pantanal | 111.5 |
| c1230e3c-ed89-3011-9981-5d432c5bd83c | -19.6237 | -56.8549 | 2024-10-25 19:36:55 | GOES-16 | AQUIDAUANA | MATO GROSSO DO SUL | Brasil | 5001102 | 50 | 33 | nan | nan | nan | Pantanal | 95.1 |
| 1a88ace8-a67e-3c73-803c-907d6c30735c | -19.6229 | -56.8968 | 2024-10-25 19:36:55 | GOES-16 | AQUIDAUANA | MATO GROSSO DO SUL | Brasil | 5001102 | 50 | 33 | nan | nan | nan | Pantanal | 162.2 |
| d51f1fdf-b951-36c6-ab8d-36c867275ef2 | -19.6816 | -56.9723 | 2024-10-25 19:36:55 | GOES-16 | AQUIDAUANA | MATO GROSSO DO SUL | Brasil | 5001102 | 50 | 33 | nan | nan | nan | Pantanal | 101.7 |
| 24ce7ebf-ce4c-3908-851d-59ad9b8b85b6 | -19.6225 | -56.9178 | 2024-10-25 19:36:55 | GOES-16 | AQUIDAUANA | MATO GROSSO DO SUL | Brasil | 5001102 | 50 | 33 | nan | nan | nan | Pantanal | 98.9 |
| 4710f7ae-5a62-394b-b331-84e857fe0b1e | -19.6438 | -56.8521 | 2024-10-25 19:36:55 | GOES-16 | AQUIDAUANA | MATO GROSSO DO SUL | Brasil | 5001102 | 50 | 33 | nan | nan | nan | Pantanal | 102.8 |
| 371b627e-688d-325c-8f1c-1927b62638ab | -1.0733 | -53.658 | 2024-10-25 19:45:11 | GOES-16 | ALMEIRIM | PARÁ | Brasil | 1500503 | 15 | 33 | nan | nan | nan | Amazônia | 53.5 |
| 362e1972-f54a-36c9-9c99-9a3a10373586 | -1.0368 | -53.5171 | 2024-10-25 19:45:11 | GOES-16 | ALMEIRIM | PARÁ | Brasil | 1500503 | 15 | 33 | nan | nan | nan | Amazônia | 62.3 |
| a221893a-a8ab-3c1d-ab76-ff674f472692 | -1.382 | -55.847 | 2024-10-25 19:45:13 | GOES-16 | ORIXIMINÁ | PARÁ | Brasil | 1505304 | 15 | 33 | nan | nan | nan | Amazônia | 88.1 |
| 43e87f60-d48e-3675-81e0-47cc27c5946b | -1.8811 | -53.5876 | 2024-10-25 19:45:16 | GOES-16 | PRAINHA | PARÁ | Brasil | 1506005 | 15 | 33 | nan | nan | nan | Amazônia | 62.2 |
| 845c21d8-a596-30bd-947d-1eb0ae7e4f15 | -2.1534 | -54.9256 | 2024-10-25 19:45:17 | GOES-16 | SANTARÉM | PARÁ | Brasil | 1506807 | 15 | 33 | nan | nan | nan | Amazônia | 88.8 |
| 87112cdb-43bc-3931-979c-e00b4fedbbc2 | -2.3628 | -46.1709 | 2024-10-25 19:45:18 | GOES-16 | CENTRO DO GUILHERME | MARANHÃO | Brasil | 2103158 | 21 | 33 | nan | nan | nan | Amazônia | 139.1 |
| 83e806f1-f201-31a4-bd44-f1ad1a776415 | -2.6658 | -49.5008 | 2024-10-25 19:45:20 | GOES-16 | BAIÃO | PARÁ | Brasil | 1501204 | 15 | 33 | nan | nan | nan | Amazônia | 59.8 |
| edeadad0-4c72-3585-80d9-c700368347d1 | -2.6473 | -49.5013 | 2024-10-25 19:45:20 | GOES-16 | MOCAJUBA | PARÁ | Brasil | 1504604 | 15 | 33 | nan | nan | nan | Amazônia | 54.2 |
| cae31694-efd0-35e2-ac73-62b9b39a906c | -2.6657 | -49.522 | 2024-10-25 19:45:20 | GOES-16 | BAIÃO | PARÁ | Brasil | 1501204 | 15 | 33 | nan | nan | nan | Amazônia | 55.9 |
| 168b105d-4aa4-3b25-998d-bbbd6966977b | -2.5933 | -49.099 | 2024-10-25 19:45:20 | GOES-16 | MOJU | PARÁ | Brasil | 1504703 | 15 | 33 | nan | nan | nan | Amazônia | 68.3 |
| edc9ef38-4b8e-35ae-9f3d-99562484d1d4 | -2.798 | -54.0933 | 2024-10-25 19:45:21 | GOES-16 | PRAINHA | PARÁ | Brasil | 1506005 | 15 | 33 | nan | nan | nan | Amazônia | 54.0 |
| 7374173f-7e30-3e15-a4df-eb2073ff204b | -2.8144 | -49.2631 | 2024-10-25 19:45:21 | GOES-16 | MOJU | PARÁ | Brasil | 1504703 | 15 | 33 | nan | nan | nan | Amazônia | 56.4 |
| c07728ee-4838-35d1-85e8-fee59a3a7685 | -2.9578 | -50.4198 | 2024-10-25 19:45:22 | GOES-16 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 146.0 |
| e3de7a4a-98d2-37ed-9412-fc97e9c94d98 | -3.1232 | -50.6033 | 2024-10-25 19:45:23 | GOES-16 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 85.2 |
| 85e286b0-92f3-3046-b3be-a91c99c6e0c2 | -3.1116 | -53.7234 | 2024-10-25 19:45:23 | GOES-16 | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | 115.6 |
| 4796faaf-4b34-39d7-be8d-fbb1f8feb56f | -3.1019 | -51.3531 | 2024-10-25 19:45:23 | GOES-16 | ANAPU | PARÁ | Brasil | 1500859 | 15 | 33 | nan | nan | nan | Amazônia | 68.7 |
| 632e4bbc-06cc-35d1-b24b-eccb5154d118 | -3.0932 | -53.7239 | 2024-10-25 19:45:23 | GOES-16 | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | 99.5 |
| f4682f41-fedd-3b14-bd42-9f0e7cd93ed7 | -3.2172 | -50.1811 | 2024-10-25 19:45:23 | GOES-16 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 65.4 |
| fefd7a27-d866-35f0-bd3a-b73165c02f40 | -3.2357 | -50.1805 | 2024-10-25 19:45:24 | GOES-16 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 79.7 |
| 22f43a6f-618c-37a5-b55f-68af79f94403 | -3.3045 | -47.1761 | 2024-10-25 19:45:24 | GOES-16 | PARAGOMINAS | PARÁ | Brasil | 1505502 | 15 | 33 | nan | nan | nan | Amazônia | 87.5 |
| be98aa89-b074-3a21-941f-b23d57f9db0e | -3.3044 | -47.198 | 2024-10-25 19:45:24 | GOES-16 | PARAGOMINAS | PARÁ | Brasil | 1505502 | 15 | 33 | nan | nan | nan | Amazônia | 107.4 |
| d0671672-f4c0-363c-9c79-c9106e9096d7 | -3.3379 | -44.1746 | 2024-10-25 19:45:24 | GOES-16 | ITAPECURU MIRIM | MARANHÃO | Brasil | 2105401 | 21 | 33 | nan | nan | nan | Cerrado | 61.2 |
| 35ccad3c-974e-32bd-a99a-3934f4a51813 | -3.495 | -54.4567 | 2024-10-25 19:45:25 | GOES-16 | PLACAS | PARÁ | Brasil | 1505650 | 15 | 33 | nan | nan | nan | Amazônia | 95.0 |
| 10f83195-402f-3d00-815e-ba659fd79301 | -3.4767 | -54.4371 | 2024-10-25 19:45:25 | GOES-16 | PLACAS | PARÁ | Brasil | 1505650 | 15 | 33 | nan | nan | nan | Amazônia | 61.0 |
| 285ac678-6964-3938-96d2-4a7bd8771a2f | -3.4211 | -54.5787 | 2024-10-25 19:45:25 | GOES-16 | PLACAS | PARÁ | Brasil | 1505650 | 15 | 33 | nan | nan | nan | Amazônia | 79.0 |
| b431c47f-fa58-3525-ad93-ad312b6e32ef | -3.4951 | -54.4366 | 2024-10-25 19:45:25 | GOES-16 | PLACAS | PARÁ | Brasil | 1505650 | 15 | 33 | nan | nan | nan | Amazônia | 184.2 |
| e4c4f796-9081-3d12-8e78-69554667256f | -3.4653 | -64.9684 | 2024-10-25 19:45:25 | GOES-16 | ALVARÃES | AMAZONAS | Brasil | 1300029 | 13 | 33 | nan | nan | nan | Amazônia | 93.2 |
| d7924af6-4c52-3455-bf8b-5ed55037a863 | -3.7399 | -45.5626 | 2024-10-25 19:45:26 | GOES-16 | TUFILÂNDIA | MARANHÃO | Brasil | 2112274 | 21 | 33 | nan | nan | nan | Amazônia | 112.5 |
| f3929113-b5ed-322c-a007-eae69127627b | -3.7213 | -45.5634 | 2024-10-25 19:45:26 | GOES-16 | TUFILÂNDIA | MARANHÃO | Brasil | 2112274 | 21 | 33 | nan | nan | nan | Amazônia | 272.6 |
| 80246f49-0ddd-3c11-a9e0-d92656574c3d | -3.7788 | -45.2685 | 2024-10-25 19:45:27 | GOES-16 | BELA VISTA DO MARANHÃO | MARANHÃO | Brasil | 2101772 | 21 | 33 | nan | nan | nan | Amazônia | 71.7 |
| 1217c4d8-d9df-3f1e-b1c0-aee7d0cb8810 | -3.8144 | -48.9729 | 2024-10-25 19:45:27 | GOES-16 | GOIANÉSIA DO PARÁ | PARÁ | Brasil | 1503093 | 15 | 33 | nan | nan | nan | Amazônia | 114.2 |
| fe5812b2-c66c-3056-b91c-4a1ccff2bae5 | -4.1416 | -46.8331 | 2024-10-25 19:45:29 | GOES-16 | BOM JARDIM | MARANHÃO | Brasil | 2102002 | 21 | 33 | nan | nan | nan | Amazônia | 97.8 |
| 512ddd5c-1d55-3c43-921a-7396568d240f | -4.1601 | -46.8322 | 2024-10-25 19:45:29 | GOES-16 | BOM JARDIM | MARANHÃO | Brasil | 2102002 | 21 | 33 | nan | nan | nan | Amazônia | 70.3 |
| f27bf3c7-caef-36f5-a809-637cc4141af6 | -4.1609 | -43.7432 | 2024-10-25 19:45:29 | GOES-16 | TIMBIRAS | MARANHÃO | Brasil | 2112100 | 21 | 33 | nan | nan | nan | Cerrado | 64.2 |
| 5ff45898-641b-3d1b-ba2a-ee6bb6a5015a | -4.4844 | -42.8866 | 2024-10-25 19:45:30 | GOES-16 | CAXIAS | MARANHÃO | Brasil | 2103000 | 21 | 33 | nan | nan | nan | Cerrado | 63.6 |
| 294766b1-d5ea-33bd-a096-1f7e37ad2f00 | -4.58 | -48.0132 | 2024-10-25 19:45:31 | GOES-16 | RONDON DO PARÁ | PARÁ | Brasil | 1506187 | 15 | 33 | nan | nan | nan | Amazônia | 296.0 |
| 92a268f2-a4ea-3745-982a-e70ed609e7d0 | -4.5613 | -48.0358 | 2024-10-25 19:45:31 | GOES-16 | RONDON DO PARÁ | PARÁ | Brasil | 1506187 | 15 | 33 | nan | nan | nan | Amazônia | 170.4 |
| bcd3b793-3e7c-3c78-9c28-063822984e34 | -4.5614 | -48.0141 | 2024-10-25 19:45:31 | GOES-16 | RONDON DO PARÁ | PARÁ | Brasil | 1506187 | 15 | 33 | nan | nan | nan | Amazônia | 186.8 |
| 28c4add5-52ab-3ae2-8c3f-b4308af4229a | -4.6961 | -44.6078 | 2024-10-25 19:45:32 | GOES-16 | BERNARDO DO MEARIM | MARANHÃO | Brasil | 2101939 | 21 | 33 | nan | nan | nan | Cerrado | 65.3 |
| 731e5527-b702-35c2-9bf3-7b77ad693c7a | -4.6638 | -46.5636 | 2024-10-25 19:45:32 | GOES-16 | BOM JESUS DAS SELVAS | MARANHÃO | Brasil | 2102036 | 21 | 33 | nan | nan | nan | Amazônia | 121.1 |
| d36733eb-8cab-3fea-8854-d7fc3f810ee5 | -4.7982 | -45.9781 | 2024-10-25 19:45:32 | GOES-16 | ARAME | MARANHÃO | Brasil | 2100956 | 21 | 33 | nan | nan | nan | Amazônia | 87.1 |
| a4f1337f-4f03-37cd-8d32-f9ae992a9840 | -4.6637 | -46.5857 | 2024-10-25 19:45:32 | GOES-16 | BOM JESUS DAS SELVAS | MARANHÃO | Brasil | 2102036 | 21 | 33 | nan | nan | nan | Amazônia | 88.2 |
| ad2c1784-2d3d-32e4-945e-21a4a611acdd | -4.9107 | -45.8822 | 2024-10-25 19:45:33 | GOES-16 | ARAME | MARANHÃO | Brasil | 2100956 | 21 | 33 | nan | nan | nan | Amazônia | 78.8 |
| d3baa343-8981-354c-9551-3fac354f759d | -4.8735 | -48.5598 | 2024-10-25 19:45:33 | GOES-16 | ABEL FIGUEIREDO | PARÁ | Brasil | 1500131 | 15 | 33 | nan | nan | nan | Amazônia | 89.6 |
| d2134566-1c8d-3e4d-b297-965b63aae48e | -4.9241 | -44.0899 | 2024-10-25 19:45:33 | GOES-16 | CODÓ | MARANHÃO | Brasil | 2103307 | 21 | 33 | nan | nan | nan | Cerrado | 185.1 |
| 6944f880-31f0-3218-b05e-179d48273f16 | -4.9108 | -45.8598 | 2024-10-25 19:45:33 | GOES-16 | ARAME | MARANHÃO | Brasil | 2100956 | 21 | 33 | nan | nan | nan | Amazônia | 203.3 |
| b0acba0c-d783-3ee8-aec1-657c7e9e28d4 | -4.9295 | -45.8587 | 2024-10-25 19:45:33 | GOES-16 | ARAME | MARANHÃO | Brasil | 2100956 | 21 | 33 | nan | nan | nan | Amazônia | 119.0 |
| e2e26a64-4b1e-3d4f-9540-75a0afcae482 | -5.2424 | -41.7931 | 2024-10-25 19:45:35 | GOES-16 | CASTELO DO PIAUÍ | PIAUÍ | Brasil | 2202604 | 22 | 33 | nan | nan | nan | Caatinga | 204.6 |


[Clique aqui para ver as próximas entradas](README199.md)
