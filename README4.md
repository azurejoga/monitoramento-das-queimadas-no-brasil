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

## Dados Diários - Página 4

| ID | Latitude | Longitude | Data/Hora GMT | Satélite | Município | Estado | País | Município ID | Estado ID | País ID | Dias sem Chuva | Precipitação | Risco de Fogo | Bioma | FRP |
|----|----------|-----------|---------------|----------|-----------|--------|------|--------------|-----------|---------|----------------|--------------|----------------|-------|-----|
| 540bae5e-51ad-3602-978b-53932dd2d1d6 | -3.99204 | -42.50769 | 2025-08-21 00:30:00 | TERRA_M-M | CAMPO LARGO DO PIAUÍ | PIAUÍ | Brasil | 2202174 | 22 | 33 | nan | nan | nan | Caatinga | 31.4 |
| 39e5ec5e-58b6-334c-a78b-89a6ac51dfd8 | -5.79494 | -45.07955 | 2025-08-21 00:30:00 | TERRA_M-M | BARRA DO CORDA | MARANHÃO | Brasil | 2101608 | 21 | 33 | nan | nan | nan | Cerrado | 22.4 |
| ea5d12fd-556a-3f44-97b1-09bf81eb9d07 | -4.30931 | -48.08535 | 2025-08-21 00:30:00 | TERRA_M-M | RONDON DO PARÁ | PARÁ | Brasil | 1506187 | 15 | 33 | nan | nan | nan | Amazônia | 22.3 |
| 40c39330-53dc-321b-8e76-5e9f53d6907e | -6.13174 | -44.7201 | 2025-08-21 00:30:00 | TERRA_M-M | MIRADOR | MARANHÃO | Brasil | 2106706 | 21 | 33 | nan | nan | nan | Cerrado | 17.3 |
| aec7c153-6c96-3f38-8a2c-683fe7fa9011 | -6.1754 | -44.73022 | 2025-08-21 00:30:00 | TERRA_M-M | MIRADOR | MARANHÃO | Brasil | 2106706 | 21 | 33 | nan | nan | nan | Cerrado | 17.4 |
| 8a33294c-6da8-3d18-be9a-9154f6ef6ee7 | -8.37733 | -55.01743 | 2025-08-21 00:30:00 | TERRA_M-M | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 18.1 |
| 639684c1-3649-323b-9a04-ce03b5111faa | -6.9563 | -42.86429 | 2025-08-21 00:30:00 | TERRA_M-M | FLORIANO | PIAUÍ | Brasil | 2203909 | 22 | 33 | nan | nan | nan | Caatinga | 60.8 |
| 21f576ce-ae44-3836-89cf-a215c6ef58ed | -7.27728 | -50.17899 | 2025-08-21 00:30:00 | TERRA_M-M | RIO MARIA | PARÁ | Brasil | 1506161 | 15 | 33 | nan | nan | nan | Amazônia | 31.5 |
| ade84e04-dadc-3c95-8296-ef19f2a74d0f | -6.62486 | -43.88562 | 2025-08-21 00:30:00 | TERRA_M-M | NOVA IORQUE | MARANHÃO | Brasil | 2107308 | 21 | 33 | nan | nan | nan | Cerrado | 20.0 |
| ca5e8d6a-56eb-3ff1-a540-35ac268c2254 | -4.91806 | -45.32263 | 2025-08-21 00:30:00 | TERRA_M-M | LAGOA GRANDE DO MARANHÃO | MARANHÃO | Brasil | 2105963 | 21 | 33 | nan | nan | nan | Cerrado | 25.3 |
| 4d02e56e-f554-32ad-9116-aad8934e35a6 | -6.54078 | -45.5197 | 2025-08-21 00:30:00 | TERRA_M-M | MIRADOR | MARANHÃO | Brasil | 2106706 | 21 | 33 | nan | nan | nan | Cerrado | 7.9 |
| af21e5ac-b5e7-3efb-8d63-2eaf6d2ea6ec | -6.61461 | -43.88721 | 2025-08-21 00:30:00 | TERRA_M-M | NOVA IORQUE | MARANHÃO | Brasil | 2107308 | 21 | 33 | nan | nan | nan | Cerrado | 25.1 |
| c3df6a73-ada3-3268-a782-92284ad41d52 | -6.80489 | -50.08848 | 2025-08-21 00:30:00 | TERRA_M-M | ÁGUA AZUL DO NORTE | PARÁ | Brasil | 1500347 | 15 | 33 | nan | nan | nan | Amazônia | 27.4 |
| 6c2e884b-826d-3ef0-b0cd-e56a9b163167 | -6.95479 | -44.18025 | 2025-08-21 00:30:00 | TERRA_M-M | PORTO ALEGRE DO PIAUÍ | PIAUÍ | Brasil | 2208551 | 22 | 33 | nan | nan | nan | Cerrado | 10.6 |
| 68556e18-b98a-3fc1-9de9-c3a4c5d173c9 | -4.86123 | -42.54204 | 2025-08-21 00:30:00 | TERRA_M-M | JOSÉ DE FREITAS | PIAUÍ | Brasil | 2205508 | 22 | 33 | nan | nan | nan | Caatinga | 36.1 |
| a9d06893-2275-3bb5-8163-09b2ea7eb1a2 | -6.49882 | -43.10964 | 2025-08-21 00:30:00 | TERRA_M-M | BARÃO DE GRAJAÚ | MARANHÃO | Brasil | 2101509 | 21 | 33 | nan | nan | nan | Cerrado | 14.3 |
| 402c04c7-330b-3708-93ca-69aad067975a | -7.59982 | -44.38651 | 2025-08-21 00:30:00 | TERRA_M-M | URUÇUÍ | PIAUÍ | Brasil | 2211209 | 22 | 33 | nan | nan | nan | Cerrado | 10.1 |
| 2fffdac7-84a2-3fda-9760-2d47ee046381 | -7.69907 | -44.01975 | 2025-08-21 00:30:00 | TERRA_M-M | SEBASTIÃO LEAL | PIAUÍ | Brasil | 2210631 | 22 | 33 | nan | nan | nan | Cerrado | 16.9 |
| 08857315-b98c-329a-88b5-9a5393460c97 | -7.86225 | -46.72511 | 2025-08-21 00:30:00 | TERRA_M-M | RIACHÃO | MARANHÃO | Brasil | 2109502 | 21 | 33 | nan | nan | nan | Cerrado | 49.6 |
| 00b49cf4-e7f5-3a14-8ce1-3081f13aa277 | -3.99853 | -42.51226 | 2025-08-21 00:30:00 | TERRA_M-M | CAMPO LARGO DO PIAUÍ | PIAUÍ | Brasil | 2202174 | 22 | 33 | nan | nan | nan | Caatinga | 12.3 |
| aeb7f029-487f-3f51-b04e-27246f7bb2c7 | -4.9085 | -45.32403 | 2025-08-21 00:30:00 | TERRA_M-M | LAGOA GRANDE DO MARANHÃO | MARANHÃO | Brasil | 2105963 | 21 | 33 | nan | nan | nan | Cerrado | 15.6 |
| e7686b21-c551-3bce-9eb9-8dc4aaf57706 | -7.01822 | -44.61678 | 2025-08-21 00:30:00 | TERRA_M-M | BENEDITO LEITE | MARANHÃO | Brasil | 2101806 | 21 | 33 | nan | nan | nan | Cerrado | 150.9 |
| d05e18e0-60a6-3efb-a94c-e250fb678b33 | -7.99287 | -47.34023 | 2025-08-21 00:30:00 | TERRA_M-M | GOIATINS | TOCANTINS | Brasil | 1709005 | 17 | 33 | nan | nan | nan | Cerrado | 6.8 |
| 2ff5f206-1c2f-3373-89eb-dc7c69e2b5f2 | -7.38157 | -47.04854 | 2025-08-21 00:30:00 | TERRA_M-M | CAROLINA | MARANHÃO | Brasil | 2102804 | 21 | 33 | nan | nan | nan | Cerrado | 7.4 |
| 69726a68-620c-3d47-b10a-46ddff3cd95b | -6.45219 | -53.37234 | 2025-08-21 00:30:00 | TERRA_M-M | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 21.8 |
| 290e376c-afd4-3dd3-826e-5d52e345c646 | -8.04934 | -47.00344 | 2025-08-21 00:30:00 | TERRA_M-M | CAROLINA | MARANHÃO | Brasil | 2102804 | 21 | 33 | nan | nan | nan | Cerrado | 11.8 |
| 76fd785c-9d89-3b7d-ab23-96b26199a629 | -6.22041 | -43.34362 | 2025-08-21 00:30:00 | TERRA_M-M | LAGOA DO MATO | MARANHÃO | Brasil | 2105922 | 21 | 33 | nan | nan | nan | Cerrado | 10.7 |
| 51298cf4-bf28-3330-8644-0ddc5c6d041b | -7.21027 | -45.31103 | 2025-08-21 00:30:00 | TERRA_M-M | LORETO | MARANHÃO | Brasil | 2106102 | 21 | 33 | nan | nan | nan | Cerrado | 13.1 |
| 9c8af137-6ab1-33cf-9ddc-d0e185b33c8b | -5.1035 | -46.18093 | 2025-08-21 00:30:00 | TERRA_M-M | ARAME | MARANHÃO | Brasil | 2100956 | 21 | 33 | nan | nan | nan | Amazônia | 6.6 |
| bdb648de-b767-3fe7-ab42-f7d08cab162d | -6.42243 | -44.66424 | 2025-08-21 00:30:00 | TERRA_M-M | MIRADOR | MARANHÃO | Brasil | 2106706 | 21 | 33 | nan | nan | nan | Cerrado | 12.5 |
| fdfcda1c-c41c-3397-bdbf-809f97225c1d | -5.75414 | -45.30376 | 2025-08-21 00:30:00 | TERRA_M-M | BARRA DO CORDA | MARANHÃO | Brasil | 2101608 | 21 | 33 | nan | nan | nan | Cerrado | 16.8 |
| 0baf5a20-f15e-37c9-8392-f087a1ab06ed | -7.70077 | -44.03154 | 2025-08-21 00:30:00 | TERRA_M-M | SEBASTIÃO LEAL | PIAUÍ | Brasil | 2210631 | 22 | 33 | nan | nan | nan | Cerrado | 10.2 |
| 4b59a7c3-b286-3cd3-86fc-66c423bb33e3 | -7.27923 | -50.17295 | 2025-08-21 00:30:00 | TERRA_M-M | RIO MARIA | PARÁ | Brasil | 1506161 | 15 | 33 | nan | nan | nan | Amazônia | 8.6 |
| 4f796d7e-e6fc-3800-9506-d2aa13403b32 | -5.78382 | -45.07038 | 2025-08-21 00:30:00 | TERRA_M-M | BARRA DO CORDA | MARANHÃO | Brasil | 2101608 | 21 | 33 | nan | nan | nan | Cerrado | 29.1 |
| 446c1bc5-e66c-35a9-a2c1-4900d2d07d1f | -6.42574 | -45.49159 | 2025-08-21 00:30:00 | TERRA_M-M | MIRADOR | MARANHÃO | Brasil | 2106706 | 21 | 33 | nan | nan | nan | Cerrado | 13.1 |
| 49213530-134e-38cc-ae5a-d6f74ec1a056 | -5.87818 | -42.41879 | 2025-08-21 00:30:00 | TERRA_M-M | PASSAGEM FRANCA DO PIAUÍ | PIAUÍ | Brasil | 2207751 | 22 | 33 | nan | nan | nan | Caatinga | 25.9 |
| f670975e-ff22-33e6-a768-1258c24b69ea | -7.01979 | -44.62764 | 2025-08-21 00:30:00 | TERRA_M-M | BENEDITO LEITE | MARANHÃO | Brasil | 2101806 | 21 | 33 | nan | nan | nan | Cerrado | 31.7 |
| 5d77db16-b966-35d9-95fe-e4f0a6188992 | -5.96569 | -44.13222 | 2025-08-21 00:30:00 | TERRA_M-M | COLINAS | MARANHÃO | Brasil | 2103505 | 21 | 33 | nan | nan | nan | Cerrado | 19.5 |
| f804ab52-8c80-3d37-9d30-2cad27400ae4 | -8.43532 | -49.57985 | 2025-08-21 00:30:00 | TERRA_M-M | CONCEIÇÃO DO ARAGUAIA | PARÁ | Brasil | 1502707 | 15 | 33 | nan | nan | nan | Amazônia | 16.2 |
| 1030b9aa-a7d0-3345-be5b-0cb53593f222 | -5.96737 | -44.14399 | 2025-08-21 00:30:00 | TERRA_M-M | COLINAS | MARANHÃO | Brasil | 2103505 | 21 | 33 | nan | nan | nan | Cerrado | 20.6 |
| e677e2ef-2b0f-3c84-95e2-ffabb5733925 | -6.20014 | -43.57686 | 2025-08-21 00:30:00 | TERRA_M-M | PASSAGEM FRANCA | MARANHÃO | Brasil | 2107902 | 21 | 33 | nan | nan | nan | Cerrado | 12.6 |
| c5f64592-806f-3068-a4b7-fa799333e7e0 | -6.94528 | -42.86592 | 2025-08-21 00:30:00 | TERRA_M-M | FLORIANO | PIAUÍ | Brasil | 2203909 | 22 | 33 | nan | nan | nan | Caatinga | 48.8 |
| a7c6c664-4901-3fa6-a577-bed6e61c4fb6 | -5.40487 | -46.2248 | 2025-08-21 00:30:00 | TERRA_M-M | GRAJAÚ | MARANHÃO | Brasil | 2104800 | 21 | 33 | nan | nan | nan | Amazônia | 5.7 |
| 61364a3f-4f79-36f3-b244-1400cada4bda | -7.39039 | -45.99288 | 2025-08-21 00:30:00 | TERRA_M-M | BALSAS | MARANHÃO | Brasil | 2101400 | 21 | 33 | nan | nan | nan | Cerrado | 5.8 |
| afab3e63-d77b-3f75-8db3-fbbb2be9f955 | -7.61795 | -45.27082 | 2025-08-21 00:30:00 | TERRA_M-M | RIBEIRO GONÇALVES | PIAUÍ | Brasil | 2208908 | 22 | 33 | nan | nan | nan | Cerrado | 22.1 |
| a57f968f-8d22-3808-ab2a-9c36705a2c50 | -5.78534 | -45.08094 | 2025-08-21 00:30:00 | TERRA_M-M | BARRA DO CORDA | MARANHÃO | Brasil | 2101608 | 21 | 33 | nan | nan | nan | Cerrado | 7.2 |
| f9ea06de-7244-3a52-8729-0b6eea276681 | -5.87176 | -48.12132 | 2025-08-21 00:30:00 | TERRA_M-M | ARAGUATINS | TOCANTINS | Brasil | 1702208 | 17 | 33 | nan | nan | nan | Cerrado | 12.1 |
| efee5cdb-a69c-300a-be4c-47961d96996a | -8.43393 | -49.56944 | 2025-08-21 00:30:00 | TERRA_M-M | CONCEIÇÃO DO ARAGUAIA | PARÁ | Brasil | 1502707 | 15 | 33 | nan | nan | nan | Amazônia | 14.2 |
| bbd1d74c-dd58-3bfb-ad8e-23d485ab3fdd | -3.98659 | -42.51408 | 2025-08-21 00:30:00 | TERRA_M-M | CAMPO LARGO DO PIAUÍ | PIAUÍ | Brasil | 2202174 | 22 | 33 | nan | nan | nan | Caatinga | 48.6 |
| 224260f0-58c3-3190-b042-1794595ebda9 | -5.16572 | -37.99448 | 2025-08-21 00:30:00 | TERRA_M-M | LIMOEIRO DO NORTE | CEARÁ | Brasil | 2307601 | 23 | 33 | nan | nan | nan | Caatinga | 41.3 |
| 1bbabd1b-d976-381b-95ab-10bf69ec8613 | -3.65291 | -48.32769 | 2025-08-21 00:33:00 | TERRA_M-M | PARAGOMINAS | PARÁ | Brasil | 1505502 | 15 | 33 | nan | nan | nan | Amazônia | 4.9 |
| 2ce42254-2252-3285-9965-a725ba5abc7a | -3.04089 | -49.43512 | 2025-08-21 00:33:00 | TERRA_M-M | MOJU | PARÁ | Brasil | 1504703 | 15 | 33 | nan | nan | nan | Amazônia | 6.6 |
| f05f6a1c-32d5-3a4e-b69d-993a329675ed | -2.69704 | -48.20976 | 2025-08-21 00:33:00 | TERRA_M-M | TOMÉ-AÇU | PARÁ | Brasil | 1508001 | 15 | 33 | nan | nan | nan | Amazônia | 17.3 |
| 823e2a45-e1a7-34cf-853c-38a7a12f8837 | -2.29842 | -47.99438 | 2025-08-21 00:33:00 | TERRA_M-M | AURORA DO PARÁ | PARÁ | Brasil | 1500958 | 15 | 33 | nan | nan | nan | Amazônia | 6.3 |
| ec859f97-fc01-3ca7-a7ae-69f9208e681e | -3.04214 | -49.44428 | 2025-08-21 00:33:00 | TERRA_M-M | MOJU | PARÁ | Brasil | 1504703 | 15 | 33 | nan | nan | nan | Amazônia | 11.5 |
| b6409afb-560c-3216-be10-cd1df79f8fec | -3.96881 | -47.8825 | 2025-08-21 00:33:00 | TERRA_M-M | ULIANÓPOLIS | PARÁ | Brasil | 1508126 | 15 | 33 | nan | nan | nan | Amazônia | 5.1 |
| b66149ba-9906-3828-9a3c-f84917b1fde3 | -0.75242 | -47.75362 | 2025-08-21 00:33:00 | TERRA_M-M | MARAPANIM | PARÁ | Brasil | 1504406 | 15 | 33 | nan | nan | nan | Amazônia | 5.6 |
| 8a2fdb04-0dd5-3011-b80a-f59beca5c974 | -2.25754 | -47.84429 | 2025-08-21 00:33:00 | TERRA_M-M | AURORA DO PARÁ | PARÁ | Brasil | 1500958 | 15 | 33 | nan | nan | nan | Amazônia | 5.0 |
| daf2f1a9-75c1-3dfb-a4eb-91c401b0e29a | -3.82824 | -47.72903 | 2025-08-21 00:33:00 | TERRA_M-M | ULIANÓPOLIS | PARÁ | Brasil | 1508126 | 15 | 33 | nan | nan | nan | Amazônia | 6.3 |
| ae452448-052f-3aa1-91e8-2346392b3c42 | -2.444 | -47.32523 | 2025-08-21 00:33:00 | TERRA_M-M | CAPITÃO POÇO | PARÁ | Brasil | 1502301 | 15 | 33 | nan | nan | nan | Amazônia | 8.7 |
| 30b9c5d9-d393-3e7d-8f5a-684c5c9c8fb4 | -2.55396 | -47.71478 | 2025-08-21 00:33:00 | TERRA_M-M | IPIXUNA DO PARÁ | PARÁ | Brasil | 1503457 | 15 | 33 | nan | nan | nan | Amazônia | 22.9 |
| 5b19a6e1-e5a8-30f6-9c60-e5a53633e0a0 | -5.13539 | -56.96074 | 2025-08-21 00:33:00 | TERRA_M-M | ITAITUBA | PARÁ | Brasil | 1503606 | 15 | 33 | nan | nan | nan | Amazônia | 32.0 |
| f6ef2dc3-98c8-3c38-9db8-2fb5c456bda6 | -4.29076 | -48.27637 | 2025-08-21 00:33:00 | TERRA_M-M | RONDON DO PARÁ | PARÁ | Brasil | 1506187 | 15 | 33 | nan | nan | nan | Amazônia | 10.1 |
| f1cc7b6d-99a9-3827-ac1a-e683a99f7c1b | -3.82947 | -47.73785 | 2025-08-21 00:33:00 | TERRA_M-M | ULIANÓPOLIS | PARÁ | Brasil | 1508126 | 15 | 33 | nan | nan | nan | Amazônia | 12.4 |
| e364cd12-94a5-3dab-b4ac-db2710378fef | -5.13222 | -56.98812 | 2025-08-21 00:33:00 | TERRA_M-M | ITAITUBA | PARÁ | Brasil | 1503606 | 15 | 33 | nan | nan | nan | Amazônia | 22.6 |
| 9aeab93e-0e6c-3f6c-a3ac-1bf74f4e12aa | -2.92088 | -48.30025 | 2025-08-21 00:33:00 | TERRA_M-M | TOMÉ-AÇU | PARÁ | Brasil | 1508001 | 15 | 33 | nan | nan | nan | Amazônia | 12.8 |
| cb64d077-2355-3e3c-8fd2-4d84e14521ba | -2.69826 | -48.21854 | 2025-08-21 00:33:00 | TERRA_M-M | TOMÉ-AÇU | PARÁ | Brasil | 1508001 | 15 | 33 | nan | nan | nan | Amazônia | 5.2 |
| cea8b01c-4d1e-3a8e-8ce1-7f2eaed29c19 | -2.82245 | -47.72165 | 2025-08-21 00:33:00 | TERRA_M-M | PARAGOMINAS | PARÁ | Brasil | 1505502 | 15 | 33 | nan | nan | nan | Amazônia | 7.9 |
| 296b64f3-6cb8-3e06-96a3-9a31b49c9ad9 | -2.90476 | -48.24883 | 2025-08-21 00:33:00 | TERRA_M-M | TOMÉ-AÇU | PARÁ | Brasil | 1508001 | 15 | 33 | nan | nan | nan | Amazônia | 6.1 |
| 0d022040-aafb-304a-ab6b-eb5f9b550c62 | -2.91327 | -48.31027 | 2025-08-21 00:33:00 | TERRA_M-M | TOMÉ-AÇU | PARÁ | Brasil | 1508001 | 15 | 33 | nan | nan | nan | Amazônia | 12.1 |
| 268a56b0-170f-3e15-b1ee-994c121d0b86 | -2.91206 | -48.30149 | 2025-08-21 00:33:00 | TERRA_M-M | TOMÉ-AÇU | PARÁ | Brasil | 1508001 | 15 | 33 | nan | nan | nan | Amazônia | 24.3 |
| 333abe46-7fdb-391d-be82-38267efa490d | -2.55273 | -47.70591 | 2025-08-21 00:33:00 | TERRA_M-M | IPIXUNA DO PARÁ | PARÁ | Brasil | 1503457 | 15 | 33 | nan | nan | nan | Amazônia | 21.6 |
| 993fe53f-d252-3e9b-b114-2c1dd28236b3 | -3.45589 | -48.96954 | 2025-08-21 00:33:00 | TERRA_M-M | IPIXUNA DO PARÁ | PARÁ | Brasil | 1503457 | 15 | 33 | nan | nan | nan | Amazônia | 6.4 |
| 21c5f5a4-6328-360f-8f92-b78b733ac6c2 | -2.37898 | -47.65188 | 2025-08-21 00:33:00 | TERRA_M-M | IPIXUNA DO PARÁ | PARÁ | Brasil | 1503457 | 15 | 33 | nan | nan | nan | Amazônia | 8.1 |
| fe13a13a-0a15-3f46-b817-5546fc873e40 | -2.39034 | -47.66845 | 2025-08-21 00:33:00 | TERRA_M-M | IPIXUNA DO PARÁ | PARÁ | Brasil | 1503457 | 15 | 33 | nan | nan | nan | Amazônia | 10.3 |
| 84f8c6d8-8cbe-356b-a08b-50ec4fa7b2b6 | -2.3891 | -47.65953 | 2025-08-21 00:33:00 | TERRA_M-M | IPIXUNA DO PARÁ | PARÁ | Brasil | 1503457 | 15 | 33 | nan | nan | nan | Amazônia | 26.3 |
| 01d3a612-8e42-33ee-aa7a-52937811a712 | -3.73597 | -48.93015 | 2025-08-21 00:33:00 | TERRA_M-M | GOIANÉSIA DO PARÁ | PARÁ | Brasil | 1503093 | 15 | 33 | nan | nan | nan | Amazônia | 15.8 |
| 9294b209-ff16-3aed-a149-4a67ace23764 | -4.13581 | -48.01706 | 2025-08-21 00:33:00 | TERRA_M-M | DOM ELISEU | PARÁ | Brasil | 1502939 | 15 | 33 | nan | nan | nan | Amazônia | 7.7 |
| bf5a941f-9772-3015-8882-f2f4a027e135 | -2.25876 | -47.85316 | 2025-08-21 00:33:00 | TERRA_M-M | AURORA DO PARÁ | PARÁ | Brasil | 1500958 | 15 | 33 | nan | nan | nan | Amazônia | 13.2 |
| 61e74d13-7db9-3f18-9e63-c37e7a895dbc | -2.38022 | -47.6608 | 2025-08-21 00:33:00 | TERRA_M-M | IPIXUNA DO PARÁ | PARÁ | Brasil | 1503457 | 15 | 33 | nan | nan | nan | Amazônia | 30.8 |
| 35356022-e743-3f66-9e14-7fa7808f691f | -14.507 | -45.9396 | 2025-08-21 00:40:00 | GOES-19 | JABORANDI | BAHIA | Brasil | 2917359 | 29 | 33 | nan | nan | nan | Cerrado | 40.6 |
| 3e051026-56df-3c6f-8c24-38d8d4457f7a | -15.0193 | -54.832 | 2025-08-21 00:40:00 | GOES-19 | NOVA BRASILÂNDIA | MATO GROSSO | Brasil | 5106208 | 51 | 33 | nan | nan | nan | Cerrado | 67.9 |
| 69b1605e-5139-3f6c-b58a-9d5574cec039 | -15.8845 | -49.0299 | 2025-08-21 00:40:00 | GOES-19 | PIRENÓPOLIS | GOIÁS | Brasil | 5217302 | 52 | 33 | nan | nan | nan | Cerrado | 46.9 |
| ae659aea-fa88-3fff-b790-3c5660b4a88c | -7.0354 | -44.6167 | 2025-08-21 00:40:00 | GOES-19 | BENEDITO LEITE | MARANHÃO | Brasil | 2101806 | 21 | 33 | nan | nan | nan | Cerrado | 72.5 |
| 65ecc0f3-9c8a-3cd9-bcc5-3fefeaefbcb0 | -5.9713 | -44.1312 | 2025-08-21 00:40:00 | GOES-19 | COLINAS | MARANHÃO | Brasil | 2103505 | 21 | 33 | nan | nan | nan | Cerrado | 59.8 |
| 1aeb2f81-2b0f-3dd4-ac81-6ffc1554de22 | -13.1367 | -54.9171 | 2025-08-21 00:40:00 | GOES-19 | NOVA UBIRATÃ | MATO GROSSO | Brasil | 5106240 | 51 | 33 | nan | nan | nan | Amazônia | 58.5 |
| 0fb73a65-6f0a-38ac-a398-8484ff124a25 | -14.8538 | -47.9504 | 2025-08-21 00:40:00 | GOES-19 | ÁGUA FRIA DE GOIÁS | GOIÁS | Brasil | 5200175 | 52 | 33 | nan | nan | nan | Cerrado | 70.5 |
| d9d15ef4-44ee-3e8a-8c1d-3282dc4321a7 | -12.9537 | -46.219 | 2025-08-21 00:40:00 | GOES-19 | LAVANDEIRA | TOCANTINS | Brasil | 1712157 | 17 | 33 | nan | nan | nan | Cerrado | 117.9 |
| 21dbe7a0-7f3a-38e9-a553-c6f86badd2e7 | -14.8738 | -47.9246 | 2025-08-21 00:40:00 | GOES-19 | ÁGUA FRIA DE GOIÁS | GOIÁS | Brasil | 5200175 | 52 | 33 | nan | nan | nan | Cerrado | 44.6 |
| 31508367-2aa3-372b-8034-86ecd6a0db21 | -7.0166 | -44.6184 | 2025-08-21 00:40:00 | GOES-19 | BENEDITO LEITE | MARANHÃO | Brasil | 2101806 | 21 | 33 | nan | nan | nan | Cerrado | 161.6 |
| d55dedac-e3d2-3c46-9e79-e0d9267b01a9 | -8.6716 | -62.0971 | 2025-08-21 00:40:00 | GOES-19 | HUMAITÁ | AMAZONAS | Brasil | 1301704 | 13 | 33 | nan | nan | nan | Amazônia | 51.3 |
| 7859ff73-88d5-3c22-ab9c-a44507c6b82d | -15.9046 | -49.0043 | 2025-08-21 00:40:00 | GOES-19 | PIRENÓPOLIS | GOIÁS | Brasil | 5217302 | 52 | 33 | nan | nan | nan | Cerrado | 59.2 |
| c8dcf42e-7457-33d8-b5f9-0caf5b3b630e | -12.9533 | -46.2419 | 2025-08-21 00:40:00 | GOES-19 | LAVANDEIRA | TOCANTINS | Brasil | 1712157 | 17 | 33 | nan | nan | nan | Cerrado | 132.8 |
| 68f16ffd-5b84-3da2-81df-0a78221f12d7 | -8.6344 | -62.1177 | 2025-08-21 00:40:00 | GOES-19 | HUMAITÁ | AMAZONAS | Brasil | 1301704 | 13 | 33 | nan | nan | nan | Amazônia | 68.8 |
| 04ba7db3-72c5-3e00-b931-ccb11b287d26 | -14.8733 | -47.9472 | 2025-08-21 00:40:00 | GOES-19 | ÁGUA FRIA DE GOIÁS | GOIÁS | Brasil | 5200175 | 52 | 33 | nan | nan | nan | Cerrado | 45.4 |
| 95996755-1753-39bf-aaa3-d28c4905853d | -8.6343 | -62.1367 | 2025-08-21 00:40:00 | GOES-19 | HUMAITÁ | AMAZONAS | Brasil | 1301704 | 13 | 33 | nan | nan | nan | Amazônia | 73.8 |
| 32f87aa5-c28b-35b1-ba44-4a3d5de1ebb1 | -14.8543 | -47.9279 | 2025-08-21 00:40:00 | GOES-19 | ÁGUA FRIA DE GOIÁS | GOIÁS | Brasil | 5200175 | 52 | 33 | nan | nan | nan | Cerrado | 76.3 |
| dfb834eb-0347-3166-a3c9-24c70fbecfb3 | -15.8849 | -49.0076 | 2025-08-21 00:40:00 | GOES-19 | PIRENÓPOLIS | GOIÁS | Brasil | 5217302 | 52 | 33 | nan | nan | nan | Cerrado | 108.1 |
| db34dde1-041d-3aa3-94c1-d6afd7d5c14c | -8.6901 | -62.0963 | 2025-08-21 00:40:00 | GOES-19 | HUMAITÁ | AMAZONAS | Brasil | 1301704 | 13 | 33 | nan | nan | nan | Amazônia | 73.1 |
| 9703ae62-66f2-3230-a691-69bfebc9e716 | -14.9999 | -54.8343 | 2025-08-21 00:40:00 | GOES-19 | NOVA BRASILÂNDIA | MATO GROSSO | Brasil | 5106208 | 51 | 33 | nan | nan | nan | Cerrado | 75.0 |


[Clique aqui para ver as próximas entradas](README5.md)
