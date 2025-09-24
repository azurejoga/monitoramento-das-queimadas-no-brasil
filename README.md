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
| 657efd74-4cef-303f-b328-39c437e31ef2 | -17.4124 | -46.0509 | 2025-09-24 00:00:00 | GOES-19 | JOÃO PINHEIRO | MINAS GERAIS | Brasil | 3136306 | 31 | 33 | nan | nan | nan | Cerrado | 75.7 |
| dd59eb8d-f99a-35cd-b36d-e6665c522482 | -18.4105 | -51.7275 | 2025-09-24 00:00:00 | GOES-19 | SERRANÓPOLIS | GOIÁS | Brasil | 5220504 | 52 | 33 | nan | nan | nan | Cerrado | 66.3 |
| d3406100-14b5-3e8a-bdde-43bec12050bd | -14.3073 | -41.8117 | 2025-09-24 00:00:00 | GOES-19 | MALHADA DE PEDRAS | BAHIA | Brasil | 2920304 | 29 | 33 | nan | nan | nan | Caatinga | 184.9 |
| c046f1e5-3c7b-3f0c-9820-de0889b9f833 | -5.6393 | -45.7239 | 2025-09-24 00:00:00 | GOES-19 | GRAJAÚ | MARANHÃO | Brasil | 2104800 | 21 | 33 | nan | nan | nan | Cerrado | 452.8 |
| 58cc487b-fd2e-3b51-a9e3-6cdb6668e5d7 | -14.3061 | -41.8612 | 2025-09-24 00:00:00 | GOES-19 | MALHADA DE PEDRAS | BAHIA | Brasil | 2920304 | 29 | 33 | nan | nan | nan | Caatinga | 181.8 |
| 3e33fc6d-e202-314c-8dd5-378f0442a392 | -6.4317 | -43.0942 | 2025-09-24 00:00:00 | GOES-19 | BARÃO DE GRAJAÚ | MARANHÃO | Brasil | 2101509 | 21 | 33 | nan | nan | nan | Cerrado | 87.8 |
| c471f3cb-8acd-3ff2-b3a0-82e05d3c2eef | -5.6361 | -43.9258 | 2025-09-24 00:00:00 | GOES-19 | FORTUNA | MARANHÃO | Brasil | 2104206 | 21 | 33 | nan | nan | nan | Cerrado | 47.2 |
| 2e647c88-6e74-39f0-bb2c-e9bf16e02e5b | -10.5788 | -44.0767 | 2025-09-24 00:00:00 | GOES-19 | JÚLIO BORGES | PIAUÍ | Brasil | 2205524 | 22 | 33 | nan | nan | nan | Cerrado | 88.4 |
| fdfd90a6-97dc-3af3-b1cb-684b7caec9bc | -6.4319 | -43.0707 | 2025-09-24 00:00:00 | GOES-19 | SÃO FRANCISCO DO MARANHÃO | MARANHÃO | Brasil | 2110906 | 21 | 33 | nan | nan | nan | Cerrado | 40.3 |
| 703ede26-fafa-39ca-b143-402704e15efb | -9.5351 | -63.5771 | 2025-09-24 00:00:00 | GOES-19 | PORTO VELHO | RONDÔNIA | Brasil | 1100205 | 11 | 33 | nan | nan | nan | Amazônia | 77.3 |
| 401c8663-2935-31d9-a38a-c20101466319 | -11.0448 | -45.8793 | 2025-09-24 00:00:00 | GOES-19 | FORMOSA DO RIO PRETO | BAHIA | Brasil | 2911105 | 29 | 33 | nan | nan | nan | Cerrado | 94.8 |
| 7f67a23e-6a9d-3641-a56e-a08d66700828 | -6.4131 | -43.0724 | 2025-09-24 00:00:00 | GOES-19 | SÃO FRANCISCO DO MARANHÃO | MARANHÃO | Brasil | 2110906 | 21 | 33 | nan | nan | nan | Cerrado | 49.6 |
| 53026277-039f-3632-bc9a-aaec68bc28b0 | -10.9944 | -44.3217 | 2025-09-24 00:00:00 | GOES-19 | SANTA RITA DE CÁSSIA | BAHIA | Brasil | 2928406 | 29 | 33 | nan | nan | nan | Cerrado | 140.5 |
| fb50f91e-d676-3ca7-840f-a3dedb341d55 | -14.2877 | -41.8157 | 2025-09-24 00:00:00 | GOES-19 | MALHADA DE PEDRAS | BAHIA | Brasil | 2920304 | 29 | 33 | nan | nan | nan | Caatinga | 267.4 |
| 69ae9f46-95a6-315a-bf53-2146d8de2d1d | -14.3067 | -41.8364 | 2025-09-24 00:00:00 | GOES-19 | MALHADA DE PEDRAS | BAHIA | Brasil | 2920304 | 29 | 33 | nan | nan | nan | Caatinga | 837.9 |
| 3c605459-476b-3999-ac45-5b5eb917e402 | -17.4118 | -46.0744 | 2025-09-24 00:00:00 | GOES-19 | JOÃO PINHEIRO | MINAS GERAIS | Brasil | 3136306 | 31 | 33 | nan | nan | nan | Cerrado | 109.5 |
| 5549da9d-30fd-3578-8166-6c4a963dff80 | -14.2865 | -41.8652 | 2025-09-24 00:00:00 | GOES-19 | MALHADA DE PEDRAS | BAHIA | Brasil | 2920304 | 29 | 33 | nan | nan | nan | Caatinga | 261.4 |
| 0e3ca970-2c43-370f-884e-b7ce075008e2 | -3.1861 | -48.8035 | 2025-09-24 00:00:00 | GOES-19 | TAILÂNDIA | PARÁ | Brasil | 1507953 | 15 | 33 | nan | nan | nan | Amazônia | 78.1 |
| f3085156-b207-3f1f-8595-1525d49d321d | -5.6392 | -45.7463 | 2025-09-24 00:00:00 | GOES-19 | GRAJAÚ | MARANHÃO | Brasil | 2104800 | 21 | 33 | nan | nan | nan | Cerrado | 146.1 |
| eb9b308d-15bd-332a-91a7-d318f64ed62e | -11.0257 | -45.8819 | 2025-09-24 00:00:00 | GOES-19 | FORMOSA DO RIO PRETO | BAHIA | Brasil | 2911105 | 29 | 33 | nan | nan | nan | Cerrado | 77.0 |
| 76a2c64f-079a-3b59-97d2-d3df7c71a1bd | -11.5225 | -43.658 | 2025-09-24 00:00:00 | GOES-19 | BARRA | BAHIA | Brasil | 2902708 | 29 | 33 | nan | nan | nan | Cerrado | 85.5 |
| 8c39d64f-2526-3c62-b7c5-741a4b92b6fc | -5.6205 | -45.7476 | 2025-09-24 00:00:00 | GOES-19 | GRAJAÚ | MARANHÃO | Brasil | 2104800 | 21 | 33 | nan | nan | nan | Cerrado | 77.6 |
| 4479b4f2-004d-3152-a520-8a689982c801 | -5.6207 | -45.7252 | 2025-09-24 00:00:00 | GOES-19 | GRAJAÚ | MARANHÃO | Brasil | 2104800 | 21 | 33 | nan | nan | nan | Cerrado | 192.2 |
| 67b465eb-ed6d-3e4b-bcb2-b12b27b2b97e | -9.5598 | -47.536 | 2025-09-24 00:00:00 | GOES-19 | RIO SONO | TOCANTINS | Brasil | 1718758 | 17 | 33 | nan | nan | nan | Cerrado | 58.4 |
| bfd606bf-0aa0-39b9-8393-b47b9415c296 | -17.4323 | -46.0466 | 2025-09-24 00:00:00 | GOES-19 | JOÃO PINHEIRO | MINAS GERAIS | Brasil | 3136306 | 31 | 33 | nan | nan | nan | Cerrado | 94.2 |
| b8b12851-ab62-3b63-8a50-aa3f2a9ab2f7 | -17.4317 | -46.0702 | 2025-09-24 00:00:00 | GOES-19 | JOÃO PINHEIRO | MINAS GERAIS | Brasil | 3136306 | 31 | 33 | nan | nan | nan | Cerrado | 147.8 |
| 738545c9-b919-3392-96af-b8da8362b455 | -6.4129 | -43.0958 | 2025-09-24 00:00:00 | GOES-19 | SÃO FRANCISCO DO MARANHÃO | MARANHÃO | Brasil | 2110906 | 21 | 33 | nan | nan | nan | Cerrado | 68.8 |
| 99e217d1-9568-3a37-9976-279817a5e317 | -11.0444 | -45.9021 | 2025-09-24 00:00:00 | GOES-19 | FORMOSA DO RIO PRETO | BAHIA | Brasil | 2911105 | 29 | 33 | nan | nan | nan | Cerrado | 101.6 |
| 9db60905-ae82-3624-af23-c068e095eea8 | -10.9948 | -44.2984 | 2025-09-24 00:00:00 | GOES-19 | SANTA RITA DE CÁSSIA | BAHIA | Brasil | 2928406 | 29 | 33 | nan | nan | nan | Cerrado | 99.1 |
| 0c04215d-27e9-3d17-bce3-9a76321e99d8 | -14.2871 | -41.8405 | 2025-09-24 00:00:00 | GOES-19 | MALHADA DE PEDRAS | BAHIA | Brasil | 2920304 | 29 | 33 | nan | nan | nan | Caatinga | 1445.6 |
| 5767085a-32cc-3a1a-919c-6ad08e59b9ff | -11.0253 | -45.9046 | 2025-09-24 00:00:00 | GOES-19 | FORMOSA DO RIO PRETO | BAHIA | Brasil | 2911105 | 29 | 33 | nan | nan | nan | Cerrado | 67.2 |
| c5a9a66a-fcd8-3abc-bbf5-9846f5819375 | -5.6363 | -43.9027 | 2025-09-24 00:00:00 | GOES-19 | FORTUNA | MARANHÃO | Brasil | 2104206 | 21 | 33 | nan | nan | nan | Cerrado | 51.8 |
| ce2d2c67-c107-3116-8885-2783a030dd31 | -18.3905 | -51.7309 | 2025-09-24 00:10:00 | GOES-19 | SERRANÓPOLIS | GOIÁS | Brasil | 5220504 | 52 | 33 | nan | nan | nan | Cerrado | 75.5 |
| d310a3f6-0baa-3f57-899e-4c8f0c9cd907 | -9.5784 | -47.5561 | 2025-09-24 00:10:00 | GOES-19 | RIO SONO | TOCANTINS | Brasil | 1718758 | 17 | 33 | nan | nan | nan | Cerrado | 75.5 |
| 8fdbcedd-8622-351e-8c7b-baad7f92828d | -7.9442 | -44.115 | 2025-09-24 00:10:00 | GOES-19 | SEBASTIÃO LEAL | PIAUÍ | Brasil | 2210631 | 22 | 33 | nan | nan | nan | Cerrado | 72.4 |
| 693a7e27-bb1b-3989-a70b-a01109feea43 | -6.4129 | -43.0958 | 2025-09-24 00:10:00 | GOES-19 | SÃO FRANCISCO DO MARANHÃO | MARANHÃO | Brasil | 2110906 | 21 | 33 | nan | nan | nan | Cerrado | 71.8 |
| cafb20d9-e534-3aec-82b7-cd734c0b8bf1 | -11.0448 | -45.8793 | 2025-09-24 00:10:00 | GOES-19 | FORMOSA DO RIO PRETO | BAHIA | Brasil | 2911105 | 29 | 33 | nan | nan | nan | Cerrado | 122.2 |
| 8316c63c-8aae-3fd3-ad16-8f4bc2e17e2a | -6.4317 | -43.0942 | 2025-09-24 00:10:00 | GOES-19 | BARÃO DE GRAJAÚ | MARANHÃO | Brasil | 2101509 | 21 | 33 | nan | nan | nan | Cerrado | 78.2 |
| c7c46614-cde1-3558-a586-e42ca66984b7 | -11.0257 | -45.8819 | 2025-09-24 00:10:00 | GOES-19 | FORMOSA DO RIO PRETO | BAHIA | Brasil | 2911105 | 29 | 33 | nan | nan | nan | Cerrado | 87.0 |
| 9ca60e8f-73e9-3abe-a931-78f22124d000 | -10.9944 | -44.3217 | 2025-09-24 00:10:00 | GOES-19 | SANTA RITA DE CÁSSIA | BAHIA | Brasil | 2928406 | 29 | 33 | nan | nan | nan | Cerrado | 102.0 |
| 915e1d00-63a9-3744-9f8a-68f4f8a06f3b | -7.9445 | -44.0918 | 2025-09-24 00:10:00 | GOES-19 | SEBASTIÃO LEAL | PIAUÍ | Brasil | 2210631 | 22 | 33 | nan | nan | nan | Cerrado | 67.4 |
| 4bf3c8eb-22e5-32ee-8a00-375e9324b849 | -10.3001 | -46.0656 | 2025-09-24 00:10:00 | GOES-19 | MATEIROS | TOCANTINS | Brasil | 1712702 | 17 | 33 | nan | nan | nan | Cerrado | 69.8 |
| 19afa332-e0c3-3b17-b4cd-e5f6a8cf02da | -11.0253 | -45.9046 | 2025-09-24 00:10:00 | GOES-19 | FORMOSA DO RIO PRETO | BAHIA | Brasil | 2911105 | 29 | 33 | nan | nan | nan | Cerrado | 113.0 |
| 36195044-a481-34ee-b435-05bd77445892 | -3.186 | -48.8249 | 2025-09-24 00:10:00 | GOES-19 | TAILÂNDIA | PARÁ | Brasil | 1507953 | 15 | 33 | nan | nan | nan | Amazônia | 69.4 |
| fc2f11b7-3c87-3f44-805f-444d33ae96f7 | -7.3659 | -47.0394 | 2025-09-24 00:10:00 | GOES-19 | CAROLINA | MARANHÃO | Brasil | 2102804 | 21 | 33 | nan | nan | nan | Cerrado | 71.3 |
| 7189f990-fb68-313c-b332-9bd2955fd584 | -5.6392 | -45.7463 | 2025-09-24 00:10:00 | GOES-19 | GRAJAÚ | MARANHÃO | Brasil | 2104800 | 21 | 33 | nan | nan | nan | Cerrado | 144.6 |
| 44e02c84-26f2-30b6-94d8-0a22b97f3b74 | -17.4118 | -46.0744 | 2025-09-24 00:10:00 | GOES-19 | JOÃO PINHEIRO | MINAS GERAIS | Brasil | 3136306 | 31 | 33 | nan | nan | nan | Cerrado | 72.7 |
| 4382fed3-3d82-30b9-985e-2e38b7b9ee1d | -11.0444 | -45.9021 | 2025-09-24 00:10:00 | GOES-19 | FORMOSA DO RIO PRETO | BAHIA | Brasil | 2911105 | 29 | 33 | nan | nan | nan | Cerrado | 164.3 |
| fe35db3b-e380-3a2b-add0-6553a25e8031 | -10.5788 | -44.0767 | 2025-09-24 00:10:00 | GOES-19 | JÚLIO BORGES | PIAUÍ | Brasil | 2205524 | 22 | 33 | nan | nan | nan | Cerrado | 101.0 |
| 24a388d2-0341-3534-b5cb-d3d3d3af23af | -10.9752 | -44.3244 | 2025-09-24 00:10:00 | GOES-19 | SANTA RITA DE CÁSSIA | BAHIA | Brasil | 2928406 | 29 | 33 | nan | nan | nan | Cerrado | 83.3 |
| 398ef0e3-b284-32e6-abd3-2a5339f7d361 | -3.1861 | -48.8035 | 2025-09-24 00:10:00 | GOES-19 | TAILÂNDIA | PARÁ | Brasil | 1507953 | 15 | 33 | nan | nan | nan | Amazônia | 78.0 |
| 132a1f94-6dcd-31ca-8a7f-1fa8f542ca44 | -5.6207 | -45.7252 | 2025-09-24 00:10:00 | GOES-19 | GRAJAÚ | MARANHÃO | Brasil | 2104800 | 21 | 33 | nan | nan | nan | Cerrado | 139.9 |
| cde8ed39-af10-3bc4-9823-e81283d1e65b | -5.6393 | -45.7239 | 2025-09-24 00:10:00 | GOES-19 | GRAJAÚ | MARANHÃO | Brasil | 2104800 | 21 | 33 | nan | nan | nan | Cerrado | 426.2 |
| 772ce89c-52f8-3790-a0ff-df05b1bcc097 | -11.0253 | -45.9046 | 2025-09-24 00:20:00 | GOES-19 | FORMOSA DO RIO PRETO | BAHIA | Brasil | 2911105 | 29 | 33 | nan | nan | nan | Cerrado | 126.9 |
| 39a98ee3-e4f8-3562-a25f-0c1196a040d4 | -10.9944 | -44.3217 | 2025-09-24 00:20:00 | GOES-19 | SANTA RITA DE CÁSSIA | BAHIA | Brasil | 2928406 | 29 | 33 | nan | nan | nan | Cerrado | 93.9 |
| b9348cb5-071e-3dcc-9e21-eec0483807d5 | -10.9526 | -45.6867 | 2025-09-24 00:20:00 | GOES-19 | FORMOSA DO RIO PRETO | BAHIA | Brasil | 2911105 | 29 | 33 | nan | nan | nan | Cerrado | 81.7 |
| a7c08d6d-ead2-3b2a-be94-c2f1403a225f | -9.5595 | -47.5581 | 2025-09-24 00:20:00 | GOES-19 | RIO SONO | TOCANTINS | Brasil | 1718758 | 17 | 33 | nan | nan | nan | Cerrado | 74.9 |
| 07f374be-4040-3a4b-892e-64dcae87e3d8 | -5.6207 | -45.7252 | 2025-09-24 00:20:00 | GOES-19 | GRAJAÚ | MARANHÃO | Brasil | 2104800 | 21 | 33 | nan | nan | nan | Cerrado | 193.7 |
| 3a448d42-f562-3de1-aee5-0a1e5c413649 | -11.0257 | -45.8819 | 2025-09-24 00:20:00 | GOES-19 | FORMOSA DO RIO PRETO | BAHIA | Brasil | 2911105 | 29 | 33 | nan | nan | nan | Cerrado | 81.6 |
| 1ce2105b-40ef-3198-8286-bd486e442c22 | -5.6205 | -45.7476 | 2025-09-24 00:20:00 | GOES-19 | GRAJAÚ | MARANHÃO | Brasil | 2104800 | 21 | 33 | nan | nan | nan | Cerrado | 76.0 |
| 7504612c-c528-374d-93f9-8e5a763d353c | -11.0444 | -45.9021 | 2025-09-24 00:20:00 | GOES-19 | FORMOSA DO RIO PRETO | BAHIA | Brasil | 2911105 | 29 | 33 | nan | nan | nan | Cerrado | 71.0 |
| b2a828a7-7135-31f2-a4f0-4f031e18433b | -11.0062 | -45.9072 | 2025-09-24 00:20:00 | GOES-19 | FORMOSA DO RIO PRETO | BAHIA | Brasil | 2911105 | 29 | 33 | nan | nan | nan | Cerrado | 105.6 |
| 211f41aa-b56c-3c2b-827d-2585c0ad934c | -7.9445 | -44.0918 | 2025-09-24 00:20:00 | GOES-19 | SEBASTIÃO LEAL | PIAUÍ | Brasil | 2210631 | 22 | 33 | nan | nan | nan | Cerrado | 51.1 |
| 9a8a63fb-e897-3999-9f06-afd68a3696a2 | -9.5784 | -47.5561 | 2025-09-24 00:20:00 | GOES-19 | RIO SONO | TOCANTINS | Brasil | 1718758 | 17 | 33 | nan | nan | nan | Cerrado | 80.3 |
| 49c579f1-a5e7-32e5-9256-48c6d7494dbd | -5.6392 | -45.7463 | 2025-09-24 00:20:00 | GOES-19 | GRAJAÚ | MARANHÃO | Brasil | 2104800 | 21 | 33 | nan | nan | nan | Cerrado | 98.4 |
| 68c4a0ef-dadf-32df-9a0b-a3e3a114986f | -3.1861 | -48.8035 | 2025-09-24 00:20:00 | GOES-19 | TAILÂNDIA | PARÁ | Brasil | 1507953 | 15 | 33 | nan | nan | nan | Amazônia | 70.4 |
| 8eca0914-5a91-3934-91ee-51c0c2d76ddc | -11.0066 | -45.8844 | 2025-09-24 00:20:00 | GOES-19 | FORMOSA DO RIO PRETO | BAHIA | Brasil | 2911105 | 29 | 33 | nan | nan | nan | Cerrado | 88.1 |
| dcd54953-7ec7-3ab8-8b4e-5b81ae5cf92c | -5.6393 | -45.7239 | 2025-09-24 00:20:00 | GOES-19 | GRAJAÚ | MARANHÃO | Brasil | 2104800 | 21 | 33 | nan | nan | nan | Cerrado | 266.3 |
| 0036be17-b834-3c96-8aae-67fc6e61ba27 | -9.5598 | -47.536 | 2025-09-24 00:20:00 | GOES-19 | RIO SONO | TOCANTINS | Brasil | 1718758 | 17 | 33 | nan | nan | nan | Cerrado | 74.3 |
| 5d7c01d3-cb70-326b-a4d5-0ac916e277d3 | -10.5788 | -44.0767 | 2025-09-24 00:20:00 | GOES-19 | JÚLIO BORGES | PIAUÍ | Brasil | 2205524 | 22 | 33 | nan | nan | nan | Cerrado | 84.7 |
| 9a4e44c3-d9e3-3b41-a63f-7829d58f7869 | -9.5351 | -63.5771 | 2025-09-24 00:20:00 | GOES-19 | PORTO VELHO | RONDÔNIA | Brasil | 1100205 | 11 | 33 | nan | nan | nan | Amazônia | 70.8 |
| 630bbdca-065d-3f03-b3b5-55ebce7543c1 | -9.7241 | -35.9991 | 2025-09-24 00:20:00 | GOES-19 | SÃO MIGUEL DOS CAMPOS | ALAGOAS | Brasil | 2708600 | 27 | 33 | nan | nan | nan | Mata Atlântica | 71.8 |
| 83d05b80-6ce8-37cf-9d95-beed732f2eb5 | -5.6207 | -45.7252 | 2025-09-24 00:30:00 | GOES-19 | GRAJAÚ | MARANHÃO | Brasil | 2104800 | 21 | 33 | nan | nan | nan | Cerrado | 140.1 |
| 34ae8d26-02ad-3e60-99e4-62320e734310 | -11.0253 | -45.9046 | 2025-09-24 00:30:00 | GOES-19 | FORMOSA DO RIO PRETO | BAHIA | Brasil | 2911105 | 29 | 33 | nan | nan | nan | Cerrado | 62.8 |
| 22181ebd-61bc-3e18-9e8a-bb09564c793b | -6.4317 | -43.0942 | 2025-09-24 00:30:00 | GOES-19 | BARÃO DE GRAJAÚ | MARANHÃO | Brasil | 2101509 | 21 | 33 | nan | nan | nan | Cerrado | 143.0 |
| 65fa3e66-cafd-3502-9827-4b31b28f250d | -6.4129 | -43.0958 | 2025-09-24 00:30:00 | GOES-19 | SÃO FRANCISCO DO MARANHÃO | MARANHÃO | Brasil | 2110906 | 21 | 33 | nan | nan | nan | Cerrado | 117.2 |
| 66d5a33c-b1e1-3ffd-8309-3b22744aedaa | -7.3659 | -47.0394 | 2025-09-24 00:30:00 | GOES-19 | CAROLINA | MARANHÃO | Brasil | 2102804 | 21 | 33 | nan | nan | nan | Cerrado | 57.7 |
| 71ec089e-6f0b-359d-8bbe-79e51d6e834d | -3.1861 | -48.8035 | 2025-09-24 00:30:00 | GOES-19 | TAILÂNDIA | PARÁ | Brasil | 1507953 | 15 | 33 | nan | nan | nan | Amazônia | 65.4 |
| f789bd66-e323-38db-a5b2-ad0f5e51f6be | -6.4131 | -43.0724 | 2025-09-24 00:30:00 | GOES-19 | SÃO FRANCISCO DO MARANHÃO | MARANHÃO | Brasil | 2110906 | 21 | 33 | nan | nan | nan | Cerrado | 69.8 |
| 16ecadf2-8fb2-3a3f-b594-592cd400dafa | -9.5784 | -47.5561 | 2025-09-24 00:30:00 | GOES-19 | RIO SONO | TOCANTINS | Brasil | 1718758 | 17 | 33 | nan | nan | nan | Cerrado | 67.7 |
| 378583f5-725f-32d0-a049-d3d17de94a29 | -11.0066 | -45.8844 | 2025-09-24 00:30:00 | GOES-19 | FORMOSA DO RIO PRETO | BAHIA | Brasil | 2911105 | 29 | 33 | nan | nan | nan | Cerrado | 120.8 |
| 4ffeabff-63fc-3678-8406-328379b65625 | -6.4319 | -43.0707 | 2025-09-24 00:30:00 | GOES-19 | SÃO FRANCISCO DO MARANHÃO | MARANHÃO | Brasil | 2110906 | 21 | 33 | nan | nan | nan | Cerrado | 71.3 |
| 73ed9f6b-4980-3e14-a6bf-27b6ae43cec7 | -11.0257 | -45.8819 | 2025-09-24 00:30:00 | GOES-19 | FORMOSA DO RIO PRETO | BAHIA | Brasil | 2911105 | 29 | 33 | nan | nan | nan | Cerrado | 71.1 |
| 276a8fe8-e2d2-3921-a08e-6da60b410a87 | -9.5781 | -47.5782 | 2025-09-24 00:30:00 | GOES-19 | RIO SONO | TOCANTINS | Brasil | 1718758 | 17 | 33 | nan | nan | nan | Cerrado | 54.0 |
| 416187b5-315e-3c49-8e23-d8895bf403a2 | -10.9944 | -44.3217 | 2025-09-24 00:30:00 | GOES-19 | SANTA RITA DE CÁSSIA | BAHIA | Brasil | 2928406 | 29 | 33 | nan | nan | nan | Cerrado | 94.0 |
| 5ce8e3ad-483c-30bc-b51b-10d35fa82564 | -5.6393 | -45.7239 | 2025-09-24 00:30:00 | GOES-19 | GRAJAÚ | MARANHÃO | Brasil | 2104800 | 21 | 33 | nan | nan | nan | Cerrado | 255.5 |
| abc4417f-4ec0-3fb6-8ed6-7bd8f08e3259 | -11.0062 | -45.9072 | 2025-09-24 00:30:00 | GOES-19 | FORMOSA DO RIO PRETO | BAHIA | Brasil | 2911105 | 29 | 33 | nan | nan | nan | Cerrado | 105.3 |
| c5e9cfe8-0e93-3d48-b3ad-ef54153a928f | -7.3847 | -47.0378 | 2025-09-24 00:30:00 | GOES-19 | CAROLINA | MARANHÃO | Brasil | 2102804 | 21 | 33 | nan | nan | nan | Cerrado | 49.3 |
| f71d5b12-bd0f-36ca-bf6a-0b579d776147 | -5.6392 | -45.7463 | 2025-09-24 00:30:00 | GOES-19 | GRAJAÚ | MARANHÃO | Brasil | 2104800 | 21 | 33 | nan | nan | nan | Cerrado | 94.0 |
| 30ef9cb3-13f8-3dff-8c13-2c160c476798 | -7.9445 | -44.0918 | 2025-09-24 00:30:00 | GOES-19 | SEBASTIÃO LEAL | PIAUÍ | Brasil | 2210631 | 22 | 33 | nan | nan | nan | Cerrado | 53.9 |
| b2ac528d-18e0-37a8-8bd8-b8e2cd8a2fdc | -11.0066 | -45.8844 | 2025-09-24 00:40:00 | GOES-19 | FORMOSA DO RIO PRETO | BAHIA | Brasil | 2911105 | 29 | 33 | nan | nan | nan | Cerrado | 88.6 |
| 90e499a4-2042-37db-bdd4-c2e7a90d1285 | -5.854 | -42.6486 | 2025-09-24 00:40:00 | GOES-19 | LAGOINHA DO PIAUÍ | PIAUÍ | Brasil | 2205540 | 22 | 33 | nan | nan | nan | Caatinga | 78.4 |
| 8a0cc50d-500d-38fa-b8e1-2b50eec7f95a | -11.0062 | -45.9072 | 2025-09-24 00:40:00 | GOES-19 | FORMOSA DO RIO PRETO | BAHIA | Brasil | 2911105 | 29 | 33 | nan | nan | nan | Cerrado | 74.6 |
| 3fd049f5-8e77-3af7-bb21-8c472687ac4f | -6.4317 | -43.0942 | 2025-09-24 00:40:00 | GOES-19 | BARÃO DE GRAJAÚ | MARANHÃO | Brasil | 2101509 | 21 | 33 | nan | nan | nan | Cerrado | 151.8 |
| 4d7fd8fe-81c3-3c00-ac71-736268e5ef72 | -11.6508 | -50.9875 | 2025-09-24 00:40:00 | GOES-19 | SÃO FÉLIX DO ARAGUAIA | MATO GROSSO | Brasil | 5107859 | 51 | 33 | nan | nan | nan | Cerrado | 95.0 |
| 4f1334c4-a9da-383b-b40d-3a2c88db238c | -11.0257 | -45.8819 | 2025-09-24 00:40:00 | GOES-19 | FORMOSA DO RIO PRETO | BAHIA | Brasil | 2911105 | 29 | 33 | nan | nan | nan | Cerrado | 71.7 |
| 5d3dfa5a-f90d-30fa-9a43-4f9befd68bb6 | -6.4131 | -43.0724 | 2025-09-24 00:40:00 | GOES-19 | SÃO FRANCISCO DO MARANHÃO | MARANHÃO | Brasil | 2110906 | 21 | 33 | nan | nan | nan | Cerrado | 72.4 |
| e87daa5e-1e40-3962-bc08-a6cb618e312f | -5.6392 | -45.7463 | 2025-09-24 00:40:00 | GOES-19 | GRAJAÚ | MARANHÃO | Brasil | 2104800 | 21 | 33 | nan | nan | nan | Cerrado | 79.5 |
| 525d09e8-70ed-3a5e-b6ca-365e4d6b4534 | -7.3659 | -47.0394 | 2025-09-24 00:40:00 | GOES-19 | CAROLINA | MARANHÃO | Brasil | 2102804 | 21 | 33 | nan | nan | nan | Cerrado | 54.6 |
| c2da20e9-8dbe-3fc7-98de-d606e0d69fd4 | -6.4129 | -43.0958 | 2025-09-24 00:40:00 | GOES-19 | SÃO FRANCISCO DO MARANHÃO | MARANHÃO | Brasil | 2110906 | 21 | 33 | nan | nan | nan | Cerrado | 129.0 |


[Clique aqui para ver as próximas entradas](README2.md)
