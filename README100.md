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

## Dados Diários - Página 100

| ID | Latitude | Longitude | Data/Hora GMT | Satélite | Município | Estado | País | Município ID | Estado ID | País ID | Dias sem Chuva | Precipitação | Risco de Fogo | Bioma | FRP |
|----|----------|-----------|---------------|----------|-----------|--------|------|--------------|-----------|---------|----------------|--------------|----------------|-------|-----|
| f156c6c4-1b12-3f54-9bd8-bbc0be1f2928 | -6.4683 | -43.1848 | 2025-09-08 14:10:00 | GOES-19 | BARÃO DE GRAJAÚ | MARANHÃO | Brasil | 2101509 | 21 | 33 | nan | nan | nan | Cerrado | 99.5 |
| 8807aded-7bf6-37a9-baf2-7400b03cdb6e | -7.2394 | -44.8498 | 2025-09-08 14:10:00 | GOES-19 | SÃO FÉLIX DE BALSAS | MARANHÃO | Brasil | 2110807 | 21 | 33 | nan | nan | nan | Cerrado | 106.1 |
| 96520af2-9e2f-3549-83a4-e8cb98da71f7 | -16.3073 | -58.0852 | 2025-09-08 14:10:00 | GOES-19 | CÁCERES | MATO GROSSO | Brasil | 5102504 | 51 | 33 | nan | nan | nan | Pantanal | 126.2 |
| 03aa9322-1d99-31b7-bd74-d2414703971e | -12.9477 | -54.793 | 2025-09-08 14:10:00 | GOES-19 | NOVA UBIRATÃ | MATO GROSSO | Brasil | 5106240 | 51 | 33 | nan | nan | nan | Amazônia | 74.3 |
| f729ec07-a8ea-3b51-9ac4-607b0e6ab81b | -14.3681 | -60.3228 | 2025-09-08 14:10:00 | GOES-19 | VILA BELA DA SANTÍSSIMA TRINDADE | MATO GROSSO | Brasil | 5105507 | 51 | 33 | nan | nan | nan | Amazônia | 145.1 |
| 758808e2-1ff7-3cab-8d60-e56ade4294ac | -4.8825 | -42.2239 | 2025-09-08 14:10:00 | GOES-19 | CAMPO MAIOR | PIAUÍ | Brasil | 2202208 | 22 | 33 | nan | nan | nan | Caatinga | 166.3 |
| 2ca5a080-16a3-35d1-adbf-42f1a18ada0e | -14.3492 | -60.3046 | 2025-09-08 14:10:00 | GOES-19 | VILA BELA DA SANTÍSSIMA TRINDADE | MATO GROSSO | Brasil | 5105507 | 51 | 33 | nan | nan | nan | Amazônia | 104.9 |
| ed5e8b6f-b9fc-3f6e-8c35-5f6d4e966bf7 | -11.2831 | -46.4591 | 2025-09-08 14:10:00 | GOES-19 | FORMOSA DO RIO PRETO | BAHIA | Brasil | 2911105 | 29 | 33 | nan | nan | nan | Cerrado | 140.6 |
| b43cca82-161d-37b6-86e9-65c40f28e8ff | -16.3149 | -52.9415 | 2025-09-08 14:10:00 | GOES-19 | TORIXORÉU | MATO GROSSO | Brasil | 5108204 | 51 | 33 | nan | nan | nan | Cerrado | 49.1 |
| 4c17fc69-0394-3ce7-99a5-f87f633ef301 | -6.1024 | -44.144 | 2025-09-08 14:10:00 | GOES-19 | COLINAS | MARANHÃO | Brasil | 2103505 | 21 | 33 | nan | nan | nan | Cerrado | 95.7 |
| b7626543-d1ce-3990-befe-7d364eb76206 | -12.948 | -54.7724 | 2025-09-08 14:10:00 | GOES-19 | NOVA UBIRATÃ | MATO GROSSO | Brasil | 5106240 | 51 | 33 | nan | nan | nan | Amazônia | 184.2 |
| 0645c8cc-52fa-328b-a1ad-ee1a8b7e39ab | -15.2141 | -44.0015 | 2025-09-08 14:10:00 | GOES-19 | JAÍBA | MINAS GERAIS | Brasil | 3135050 | 31 | 33 | nan | nan | nan | Cerrado | 117.4 |
| c22648f7-a719-3f2f-8bb0-47b0e099f5c1 | -6.2929 | -43.8284 | 2025-09-08 14:10:00 | GOES-19 | SÃO JOÃO DOS PATOS | MARANHÃO | Brasil | 2111102 | 21 | 33 | nan | nan | nan | Cerrado | 142.5 |
| ba83331f-ff1d-3c90-bcea-8d7d216121af | -7.6559 | -47.9593 | 2025-09-08 14:10:00 | GOES-19 | PALMEIRANTE | TOCANTINS | Brasil | 1715705 | 17 | 33 | nan | nan | nan | Cerrado | 112.3 |
| 56fec4d7-fc9a-374d-9e0d-12f98d49a9a5 | -15.2302 | -53.7641 | 2025-09-08 14:10:00 | GOES-19 | NOVO SÃO JOAQUIM | MATO GROSSO | Brasil | 5106281 | 51 | 33 | nan | nan | nan | Cerrado | 82.2 |
| 8893367c-5717-3d56-b7d2-00830f985088 | -11.2827 | -46.4817 | 2025-09-08 14:10:00 | GOES-19 | FORMOSA DO RIO PRETO | BAHIA | Brasil | 2911105 | 29 | 33 | nan | nan | nan | Cerrado | 140.9 |
| d809f3c3-1fe2-3f95-a4db-d0318e8ee1b7 | -12.6343 | -56.9725 | 2025-09-08 14:10:00 | GOES-19 | NOVA MARINGÁ | MATO GROSSO | Brasil | 5108907 | 51 | 33 | nan | nan | nan | Amazônia | 79.4 |
| f4d335a9-50d5-3959-8103-a17aa5352107 | -16.9615 | -45.8411 | 2025-09-08 14:10:00 | GOES-19 | BRASILÂNDIA DE MINAS | MINAS GERAIS | Brasil | 3108552 | 31 | 33 | nan | nan | nan | Cerrado | 130.5 |
| a91dab1a-49e2-38d8-8d84-faebbe52bbec | -16.307 | -58.1055 | 2025-09-08 14:10:00 | GOES-19 | CÁCERES | MATO GROSSO | Brasil | 5102504 | 51 | 33 | nan | nan | nan | Pantanal | 290.9 |
| 83160e52-3ddb-3d14-b484-3bfbdb8b99f9 | -11.7703 | -50.6115 | 2025-09-08 14:10:00 | GOES-19 | FORMOSO DO ARAGUAIA | TOCANTINS | Brasil | 1708205 | 17 | 33 | nan | nan | nan | Cerrado | 81.3 |
| 6d0809ee-6244-3f8d-857f-7fa8718adabd | -16.3265 | -58.1034 | 2025-09-08 14:10:00 | GOES-19 | CÁCERES | MATO GROSSO | Brasil | 5102504 | 51 | 33 | nan | nan | nan | Pantanal | 68.0 |
| 5a502520-edf6-3883-a33a-b07b30fead0b | -5.211 | -43.2833 | 2025-09-08 14:10:00 | GOES-19 | MATÕES | MARANHÃO | Brasil | 2106607 | 21 | 33 | nan | nan | nan | Cerrado | 121.2 |
| 23319efe-4717-3d4a-ae0f-b096d6ef2681 | -11.2007 | -54.9992 | 2025-09-08 14:10:00 | GOES-19 | CLÁUDIA | MATO GROSSO | Brasil | 5103056 | 51 | 33 | nan | nan | nan | Amazônia | 80.5 |
| 0c73c4c3-9d42-3cd5-8005-ac31b8864eb8 | -5.7113 | -43.8972 | 2025-09-08 14:10:00 | GOES-19 | BURITI BRAVO | MARANHÃO | Brasil | 2102309 | 21 | 33 | nan | nan | nan | Cerrado | 109.9 |
| 6b3709ab-006a-3422-b9f2-adc3f4cbd1cc | -14.4359 | -48.4644 | 2025-09-08 14:10:00 | GOES-19 | NIQUELÂNDIA | GOIÁS | Brasil | 5214606 | 52 | 33 | nan | nan | nan | Cerrado | 154.5 |
| e76d18df-cc3a-30cc-a640-07daad8b63ad | -7.5035 | -48.2116 | 2025-09-08 14:10:00 | GOES-19 | NOVA OLINDA | TOCANTINS | Brasil | 1714880 | 17 | 33 | nan | nan | nan | Cerrado | 117.1 |
| f1faf774-efc1-36f2-94ec-e3fdfe07d346 | -6.3117 | -43.8268 | 2025-09-08 14:10:00 | GOES-19 | SÃO JOÃO DOS PATOS | MARANHÃO | Brasil | 2111102 | 21 | 33 | nan | nan | nan | Cerrado | 120.3 |
| cc8ebbb0-0514-372f-a3dd-fdbecda1a262 | -9.5124 | -48.2659 | 2025-09-08 14:10:00 | GOES-19 | TOCANTÍNIA | TOCANTINS | Brasil | 1721109 | 17 | 33 | nan | nan | nan | Cerrado | 85.3 |
| 5b5f1029-bb7e-3b6e-a8bb-4ea36f368288 | -5.3671 | -44.7703 | 2025-09-08 14:10:00 | GOES-19 | TUNTUM | MARANHÃO | Brasil | 2112308 | 21 | 33 | nan | nan | nan | Cerrado | 88.1 |
| c7562a51-0c73-3aab-8eeb-f7ac5196a57e | -12.6153 | -56.9742 | 2025-09-08 14:10:00 | GOES-19 | NOVA MARINGÁ | MATO GROSSO | Brasil | 5108907 | 51 | 33 | nan | nan | nan | Amazônia | 87.1 |
| 2b18e58d-651b-3554-a0ba-2765447ca43d | -8.0592 | -45.4998 | 2025-09-08 14:10:00 | GOES-19 | RIBEIRO GONÇALVES | PIAUÍ | Brasil | 2208908 | 22 | 33 | nan | nan | nan | Cerrado | 473.2 |
| ac531a8a-0b73-3405-a203-ae9a5f56c5b3 | -12.967 | -54.7705 | 2025-09-08 14:10:00 | GOES-19 | NOVA UBIRATÃ | MATO GROSSO | Brasil | 5106240 | 51 | 33 | nan | nan | nan | Amazônia | 85.0 |
| 8116e1dd-e57e-3535-a3e3-d9b07696d752 | -15.0635 | -50.1089 | 2025-09-08 14:10:00 | GOES-19 | CRIXÁS | GOIÁS | Brasil | 5206404 | 52 | 33 | nan | nan | nan | Cerrado | 152.8 |
| aeaa700a-e247-3b34-8ad2-66fbd70cede1 | -11.4268 | -43.649 | 2025-09-08 14:10:00 | GOES-19 | BARRA | BAHIA | Brasil | 2902708 | 29 | 33 | nan | nan | nan | Cerrado | 155.1 |
| 3adb0dcd-6d4f-37bc-92af-6276d1cc7be8 | -7.9928 | -46.3388 | 2025-09-08 14:10:00 | GOES-19 | BALSAS | MARANHÃO | Brasil | 2101400 | 21 | 33 | nan | nan | nan | Cerrado | 74.0 |
| 9b0b485d-3820-3df4-9ebf-c4ccd8f8eb66 | -9.481 | -60.4902 | 2025-09-08 14:10:00 | GOES-19 | ARIPUANÃ | MATO GROSSO | Brasil | 5101407 | 51 | 33 | nan | nan | nan | Amazônia | 107.4 |
| 011b57c5-8954-3e1a-bf12-8b8b6cd5df1f | -14.349 | -60.3243 | 2025-09-08 14:10:00 | GOES-19 | VILA BELA DA SANTÍSSIMA TRINDADE | MATO GROSSO | Brasil | 5105507 | 51 | 33 | nan | nan | nan | Amazônia | 76.9 |
| c2169523-22df-37b0-9ee8-0fe18796042a | -9.9971 | -51.6629 | 2025-09-08 14:10:00 | GOES-19 | VILA RICA | MATO GROSSO | Brasil | 5108600 | 51 | 33 | nan | nan | nan | Amazônia | 75.8 |
| aed2b862-a72c-3ccb-9ecb-33b292bd850c | -12.9482 | -54.7519 | 2025-09-08 14:10:00 | GOES-19 | NOVA UBIRATÃ | MATO GROSSO | Brasil | 5106240 | 51 | 33 | nan | nan | nan | Amazônia | 112.0 |
| afe8ef62-ad40-3f29-aeb0-1775246bc928 | -9.9251 | -49.8898 | 2025-09-08 14:10:00 | GOES-19 | PIUM | TOCANTINS | Brasil | 1717503 | 17 | 33 | nan | nan | nan | Cerrado | 64.6 |
| 4c0b640a-cd78-37ed-bd50-317f5dfbd0e0 | -8.3179 | -47.4621 | 2025-09-08 14:10:00 | GOES-19 | GOIATINS | TOCANTINS | Brasil | 1709005 | 17 | 33 | nan | nan | nan | Cerrado | 110.7 |
| 475c927b-b793-3954-b4b2-920746e1fed4 | -10.8911 | -55.7131 | 2025-09-08 14:10:00 | GOES-19 | NOVA CANAÃ DO NORTE | MATO GROSSO | Brasil | 5106216 | 51 | 33 | nan | nan | nan | Amazônia | 125.9 |
| 1adda2c7-28be-3dcc-ac7d-cbc1a44fa772 | -15.044 | -50.1118 | 2025-09-08 14:10:00 | GOES-19 | CRIXÁS | GOIÁS | Brasil | 5206404 | 52 | 33 | nan | nan | nan | Cerrado | 209.0 |
| 3c95e1f5-f821-3e47-ba7d-257a33e01070 | -12.8411 | -52.8994 | 2025-09-08 14:10:00 | GOES-19 | GAÚCHA DO NORTE | MATO GROSSO | Brasil | 5103858 | 51 | 33 | nan | nan | nan | Amazônia | 264.1 |
| 5e4c56de-c517-33f5-96d2-f80f2f3e5ecb | -8.1998 | -44.7794 | 2025-09-08 14:10:00 | GOES-19 | URUÇUÍ | PIAUÍ | Brasil | 2211209 | 22 | 33 | nan | nan | nan | Cerrado | 130.2 |
| 67a68501-cc87-3d9b-83b2-d877f2528abe | -9.4623 | -60.5104 | 2025-09-08 14:10:00 | GOES-19 | ARIPUANÃ | MATO GROSSO | Brasil | 5101407 | 51 | 33 | nan | nan | nan | Amazônia | 54.0 |
| 63f2539e-5670-3b29-81ac-8e9304a10426 | -9.4611 | -46.4566 | 2025-09-08 14:10:00 | GOES-19 | ALTO PARNAÍBA | MARANHÃO | Brasil | 2100501 | 21 | 33 | nan | nan | nan | Cerrado | 200.3 |
| bbe132f8-6cb8-3b1c-a8e9-c713f0382efe | -10.7762 | -46.0054 | 2025-09-08 14:10:00 | GOES-19 | FORMOSA DO RIO PRETO | BAHIA | Brasil | 2911105 | 29 | 33 | nan | nan | nan | Cerrado | 74.8 |
| eb0e41d0-022b-314a-b4dc-829e3471bbb9 | -14.714 | -60.2551 | 2025-09-08 14:10:00 | GOES-19 | VILA BELA DA SANTÍSSIMA TRINDADE | MATO GROSSO | Brasil | 5105507 | 51 | 33 | nan | nan | nan | Amazônia | 64.6 |
| 7dc645b3-0461-341c-a4e1-411ba4b9f4eb | -6.2036 | -43.3709 | 2025-09-08 14:10:00 | GOES-19 | LAGOA DO MATO | MARANHÃO | Brasil | 2105922 | 21 | 33 | nan | nan | nan | Cerrado | 99.9 |
| e5c29653-911b-3de0-8e4c-fcc307609084 | -10.7758 | -46.0281 | 2025-09-08 14:10:00 | GOES-19 | FORMOSA DO RIO PRETO | BAHIA | Brasil | 2911105 | 29 | 33 | nan | nan | nan | Cerrado | 115.2 |
| c5601e79-fc92-34cd-991e-93f84daf5d68 | -12.9477 | -54.793 | 2025-09-08 14:20:00 | GOES-19 | NOVA UBIRATÃ | MATO GROSSO | Brasil | 5106240 | 51 | 33 | nan | nan | nan | Amazônia | 74.5 |
| cc1e0aca-7503-3112-8942-f6d32eafb950 | -10.7555 | -48.6109 | 2025-09-08 14:20:00 | GOES-19 | PORTO NACIONAL | TOCANTINS | Brasil | 1718204 | 17 | 33 | nan | nan | nan | Cerrado | 67.8 |
| 8584fcc3-0270-377a-844e-bc06351288cb | -6.2036 | -43.3709 | 2025-09-08 14:20:00 | GOES-19 | LAGOA DO MATO | MARANHÃO | Brasil | 2105922 | 21 | 33 | nan | nan | nan | Cerrado | 92.9 |
| d0da143f-1f05-31ce-bdbe-0ed6aa66d0b9 | -15.044 | -50.1118 | 2025-09-08 14:20:00 | GOES-19 | CRIXÁS | GOIÁS | Brasil | 5206404 | 52 | 33 | nan | nan | nan | Cerrado | 196.2 |
| 7f14722d-428d-3c37-bb59-038b189cc5cb | -9.4611 | -46.4566 | 2025-09-08 14:20:00 | GOES-19 | ALTO PARNAÍBA | MARANHÃO | Brasil | 2100501 | 21 | 33 | nan | nan | nan | Cerrado | 131.7 |
| f05b59c5-8d89-37c2-8a96-1831bdb066c6 | -9.4624 | -60.4912 | 2025-09-08 14:20:00 | GOES-19 | ARIPUANÃ | MATO GROSSO | Brasil | 5101407 | 51 | 33 | nan | nan | nan | Amazônia | 69.3 |
| d1be7d69-e71a-3dd4-b5d1-73ce023db462 | -16.9814 | -45.837 | 2025-09-08 14:20:00 | GOES-19 | BRASILÂNDIA DE MINAS | MINAS GERAIS | Brasil | 3108552 | 31 | 33 | nan | nan | nan | Cerrado | 83.7 |
| a0d6c865-74a3-3267-96e8-c87dc791c290 | -12.8405 | -52.9413 | 2025-09-08 14:20:00 | GOES-19 | GAÚCHA DO NORTE | MATO GROSSO | Brasil | 5103858 | 51 | 33 | nan | nan | nan | Amazônia | 129.2 |
| 3ddd4790-0fb3-3ce9-a3b2-5476e75a4524 | -9.8278 | -53.2976 | 2025-09-08 14:20:00 | GOES-19 | PEIXOTO DE AZEVEDO | MATO GROSSO | Brasil | 5106422 | 51 | 33 | nan | nan | nan | Amazônia | 76.9 |
| 5c5196cf-a5dc-3031-8ace-33202a65ca09 | -14.3681 | -60.3228 | 2025-09-08 14:20:00 | GOES-19 | VILA BELA DA SANTÍSSIMA TRINDADE | MATO GROSSO | Brasil | 5105507 | 51 | 33 | nan | nan | nan | Amazônia | 109.1 |
| 04ae1604-8295-377d-b5fd-03d5c4eabe38 | -11.3905 | -43.5365 | 2025-09-08 14:20:00 | GOES-19 | BARRA | BAHIA | Brasil | 2902708 | 29 | 33 | nan | nan | nan | Cerrado | 111.0 |
| b11d82fd-a353-3f0b-a39a-2a0b2b84e6d9 | -9.481 | -60.4902 | 2025-09-08 14:20:00 | GOES-19 | ARIPUANÃ | MATO GROSSO | Brasil | 5101407 | 51 | 33 | nan | nan | nan | Amazônia | 118.8 |
| c0fd69c2-b209-38c2-88d7-6b39c2b6c3ec | -8.3179 | -47.4621 | 2025-09-08 14:20:00 | GOES-19 | GOIATINS | TOCANTINS | Brasil | 1709005 | 17 | 33 | nan | nan | nan | Cerrado | 104.8 |
| 400d10b3-b0c1-3831-ac79-db60b52b31c8 | -6.62 | -53.3373 | 2025-09-08 14:20:00 | GOES-19 | SÃO FÉLIX DO XINGU | PARÁ | Brasil | 1507300 | 15 | 33 | nan | nan | nan | Amazônia | 75.6 |
| 3926bd29-808f-3eb3-8247-fdd766d7e01b | -15.0635 | -50.1089 | 2025-09-08 14:20:00 | GOES-19 | CRIXÁS | GOIÁS | Brasil | 5206404 | 52 | 33 | nan | nan | nan | Cerrado | 127.3 |
| cf46e387-e449-379e-a0fb-a2b8ec225ac2 | -12.8411 | -52.8994 | 2025-09-08 14:20:00 | GOES-19 | GAÚCHA DO NORTE | MATO GROSSO | Brasil | 5103858 | 51 | 33 | nan | nan | nan | Amazônia | 140.3 |
| 70672744-ec65-300f-8b8b-776944a33df5 | -6.1211 | -44.1425 | 2025-09-08 14:20:00 | GOES-19 | COLINAS | MARANHÃO | Brasil | 2103505 | 21 | 33 | nan | nan | nan | Cerrado | 100.2 |
| 7e8c6f33-cb4d-30d4-8670-b3db387cc759 | -6.209 | -40.9894 | 2025-09-08 14:20:00 | GOES-19 | PIMENTEIRAS | PIAUÍ | Brasil | 2208106 | 22 | 33 | nan | nan | nan | Caatinga | 162.8 |
| b56df427-c1e8-3fce-96bd-1cb1656f0f68 | -12.948 | -54.7724 | 2025-09-08 14:20:00 | GOES-19 | NOVA UBIRATÃ | MATO GROSSO | Brasil | 5106240 | 51 | 33 | nan | nan | nan | Amazônia | 244.7 |
| 453e235b-4e60-385b-93ef-56ed835b8993 | -11.883 | -50.7053 | 2025-09-08 14:20:00 | GOES-19 | NOVO SANTO ANTÔNIO | MATO GROSSO | Brasil | 5106315 | 51 | 33 | nan | nan | nan | Cerrado | 69.9 |
| ca93e5e2-25b8-3b39-a7a8-b2635ba40c82 | -15.6359 | -53.8586 | 2025-09-08 14:20:00 | GOES-19 | GENERAL CARNEIRO | MATO GROSSO | Brasil | 5103908 | 51 | 33 | nan | nan | nan | Cerrado | 84.0 |
| dfe767cc-78a0-38fd-9df5-cf01f0caed23 | -11.2007 | -54.9992 | 2025-09-08 14:20:00 | GOES-19 | CLÁUDIA | MATO GROSSO | Brasil | 5103056 | 51 | 33 | nan | nan | nan | Amazônia | 76.8 |
| 0c208a47-0577-3e21-ac86-0b07c5bbcdde | -5.7113 | -43.8972 | 2025-09-08 14:20:00 | GOES-19 | BURITI BRAVO | MARANHÃO | Brasil | 2102309 | 21 | 33 | nan | nan | nan | Cerrado | 100.1 |
| 5900fa35-7e4f-310c-86ca-271ef8c3af84 | -5.6792 | -45.4286 | 2025-09-08 14:20:00 | GOES-19 | BARRA DO CORDA | MARANHÃO | Brasil | 2101608 | 21 | 33 | nan | nan | nan | Cerrado | 108.5 |
| fa5f7b59-5146-3e38-9c69-0379dfa88461 | -5.8354 | -42.6265 | 2025-09-08 14:20:00 | GOES-19 | LAGOINHA DO PIAUÍ | PIAUÍ | Brasil | 2205540 | 22 | 33 | nan | nan | nan | Caatinga | 122.5 |
| 1657b4a2-fb90-3e2b-a8eb-36e2a28ed946 | -16.307 | -58.1055 | 2025-09-08 14:20:00 | GOES-19 | CÁCERES | MATO GROSSO | Brasil | 5102504 | 51 | 33 | nan | nan | nan | Pantanal | 127.5 |
| 19f2a9b7-f154-327f-a458-378687f2acdb | -5.8081 | -45.6448 | 2025-09-08 14:20:00 | GOES-19 | GRAJAÚ | MARANHÃO | Brasil | 2104800 | 21 | 33 | nan | nan | nan | Cerrado | 107.5 |
| 9c3a8915-c195-3784-952e-6242e4cd42d0 | -16.3403 | -43.0394 | 2025-09-08 14:20:00 | GOES-19 | GRÃO MOGOL | MINAS GERAIS | Brasil | 3127800 | 31 | 33 | nan | nan | nan | Cerrado | 223.9 |
| 15944d79-137d-3d62-99b9-c2576ede2847 | -7.6559 | -47.9593 | 2025-09-08 14:20:00 | GOES-19 | PALMEIRANTE | TOCANTINS | Brasil | 1715705 | 17 | 33 | nan | nan | nan | Cerrado | 115.1 |
| a1e3b5c8-6140-3f59-8ffb-032e602bfc8c | -11.4272 | -43.6254 | 2025-09-08 14:20:00 | GOES-19 | BARRA | BAHIA | Brasil | 2902708 | 29 | 33 | nan | nan | nan | Cerrado | 85.5 |
| 1c628324-c44f-3a46-aa1f-34491da96ff6 | -6.2087 | -41.0137 | 2025-09-08 14:20:00 | GOES-19 | PIMENTEIRAS | PIAUÍ | Brasil | 2208106 | 22 | 33 | nan | nan | nan | Caatinga | 131.2 |
| 212e4463-3e0f-3876-b35e-e3057e4688fe | -9.5127 | -48.244 | 2025-09-08 14:20:00 | GOES-19 | TOCANTÍNIA | TOCANTINS | Brasil | 1721109 | 17 | 33 | nan | nan | nan | Cerrado | 75.7 |
| cd56ce5d-c852-3bab-8fc8-bf3c766bd3cd | -11.4268 | -43.649 | 2025-09-08 14:20:00 | GOES-19 | BARRA | BAHIA | Brasil | 2902708 | 29 | 33 | nan | nan | nan | Cerrado | 267.5 |
| 48b240df-86e8-3412-8c46-70298b9e92f9 | -9.7589 | -51.1383 | 2025-09-08 14:20:00 | GOES-19 | SANTANA DO ARAGUAIA | PARÁ | Brasil | 1506708 | 15 | 33 | nan | nan | nan | Amazônia | 180.4 |
| 50a20d5b-a8aa-3db4-b807-8e001e76f9d5 | -12.8651 | -62.1074 | 2025-09-08 14:20:00 | GOES-19 | ALTA FLORESTA D'OESTE | RONDÔNIA | Brasil | 1100015 | 11 | 33 | nan | nan | nan | Amazônia | 66.6 |
| 98d13bae-2f97-3838-be49-bfd140a04d03 | -5.6605 | -45.43 | 2025-09-08 14:20:00 | GOES-19 | BARRA DO CORDA | MARANHÃO | Brasil | 2101608 | 21 | 33 | nan | nan | nan | Cerrado | 150.2 |
| ca7675f3-5700-3f68-9605-6ef493ba721a | -14.741 | -47.7668 | 2025-09-08 14:20:00 | GOES-19 | ÁGUA FRIA DE GOIÁS | GOIÁS | Brasil | 5200175 | 52 | 33 | nan | nan | nan | Cerrado | 82.7 |
| a21dba66-1a39-344a-b73e-42f0290d2817 | -16.9615 | -45.8411 | 2025-09-08 14:20:00 | GOES-19 | BRASILÂNDIA DE MINAS | MINAS GERAIS | Brasil | 3108552 | 31 | 33 | nan | nan | nan | Cerrado | 107.1 |
| 98a2218d-0c2a-388d-94ef-c1533d7ec48b | -14.4359 | -48.4644 | 2025-09-08 14:20:00 | GOES-19 | NIQUELÂNDIA | GOIÁS | Brasil | 5214606 | 52 | 33 | nan | nan | nan | Cerrado | 160.3 |
| 3620dfce-af7d-3d26-ae3a-26317290d05a | -6.1848 | -43.3724 | 2025-09-08 14:20:00 | GOES-19 | LAGOA DO MATO | MARANHÃO | Brasil | 2105922 | 21 | 33 | nan | nan | nan | Cerrado | 90.2 |
| dba83c49-b8e2-3a4c-9a6c-9e55199fe90a | -10.8722 | -55.7147 | 2025-09-08 14:20:00 | GOES-19 | NOVA CANAÃ DO NORTE | MATO GROSSO | Brasil | 5106216 | 51 | 33 | nan | nan | nan | Amazônia | 56.6 |
| 0f40facc-1057-3544-b7ab-505cea8f3868 | -11.8637 | -50.7289 | 2025-09-08 14:20:00 | GOES-19 | NOVO SANTO ANTÔNIO | MATO GROSSO | Brasil | 5106315 | 51 | 33 | nan | nan | nan | Cerrado | 65.3 |
| 32b2d264-d391-3bfb-9929-b091bdd3fa37 | -5.211 | -43.2833 | 2025-09-08 14:20:00 | GOES-19 | MATÕES | MARANHÃO | Brasil | 2106607 | 21 | 33 | nan | nan | nan | Cerrado | 93.3 |
| 0e5eea55-ae43-369c-b4c6-329fe1c20285 | -9.9971 | -51.6629 | 2025-09-08 14:20:00 | GOES-19 | VILA RICA | MATO GROSSO | Brasil | 5108600 | 51 | 33 | nan | nan | nan | Amazônia | 71.0 |
| c251791c-35ae-3e20-884b-d65f1ffd85b3 | -15.7583 | -53.5268 | 2025-09-08 14:20:00 | GOES-19 | TESOURO | MATO GROSSO | Brasil | 5108105 | 51 | 33 | nan | nan | nan | Cerrado | 99.7 |
| 1944ac2b-eb26-3f55-80a8-04c5ad724593 | -7.6314 | -46.7507 | 2025-09-08 14:20:00 | GOES-19 | RIACHÃO | MARANHÃO | Brasil | 2109502 | 21 | 33 | nan | nan | nan | Cerrado | 95.9 |
| 0ef05849-79cc-3f66-8bdc-7fdfdfeae51f | -5.6607 | -45.4074 | 2025-09-08 14:20:00 | GOES-19 | BARRA DO CORDA | MARANHÃO | Brasil | 2101608 | 21 | 33 | nan | nan | nan | Cerrado | 85.3 |
| 84e76952-5a52-3bfa-b293-041f31679bf1 | -11.4089 | -43.581 | 2025-09-08 14:20:00 | GOES-19 | BARRA | BAHIA | Brasil | 2902708 | 29 | 33 | nan | nan | nan | Cerrado | 120.5 |
| a4f644fe-ae2b-38ab-9191-c6170578e499 | -5.679 | -45.4512 | 2025-09-08 14:20:00 | GOES-19 | BARRA DO CORDA | MARANHÃO | Brasil | 2101608 | 21 | 33 | nan | nan | nan | Cerrado | 152.3 |


[Clique aqui para ver as próximas entradas](README101.md)
