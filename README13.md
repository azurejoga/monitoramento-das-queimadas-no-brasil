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
| afe3c5a8-9cb1-3ce7-b9cf-3127b4e89be2 | -8.50915 | -51.36069 | 2025-09-08 00:52:00 | TERRA_M-M | CUMARU DO NORTE | PARÁ | Brasil | 1502764 | 15 | 33 | nan | nan | nan | Amazônia | 8.3 |
| 38a88f2a-0cbf-35ef-91ca-90da9a997e38 | -3.30824 | -48.71097 | 2025-09-08 00:52:00 | TERRA_M-M | IPIXUNA DO PARÁ | PARÁ | Brasil | 1503457 | 15 | 33 | nan | nan | nan | Amazônia | 59.7 |
| 2c54f153-2b6a-3698-b6a2-b501b78e5e3c | -5.92003 | -50.00267 | 2025-09-08 00:52:00 | TERRA_M-M | PARAUAPEBAS | PARÁ | Brasil | 1505536 | 15 | 33 | nan | nan | nan | Amazônia | 7.6 |
| c8100917-c2f4-3e65-bdfc-54d9e47457eb | -9.44173 | -59.20064 | 2025-09-08 00:52:00 | TERRA_M-M | COLNIZA | MATO GROSSO | Brasil | 5103254 | 51 | 33 | nan | nan | nan | Amazônia | 24.3 |
| 712da7c4-c386-3b87-819b-f4a0fc7e9ffa | -5.88485 | -52.10073 | 2025-09-08 00:52:00 | TERRA_M-M | SÃO FÉLIX DO XINGU | PARÁ | Brasil | 1507300 | 15 | 33 | nan | nan | nan | Amazônia | 5.1 |
| 8f90e714-b07a-35e0-ab0c-f86dfaafc0ac | -7.06555 | -50.86191 | 2025-09-08 00:52:00 | TERRA_M-M | OURILÂNDIA DO NORTE | PARÁ | Brasil | 1505437 | 15 | 33 | nan | nan | nan | Amazônia | 5.8 |
| d04d0318-a010-325d-b3e0-67e09cde429d | -7.42809 | -49.25632 | 2025-09-08 00:52:00 | TERRA_M-M | PAU D'ARCO | TOCANTINS | Brasil | 1716307 | 17 | 33 | nan | nan | nan | Amazônia | 12.2 |
| 7f14d292-f76d-3a4d-a69e-b9b17bb6c11c | -9.45888 | -56.06133 | 2025-09-08 00:52:00 | TERRA_M-M | ALTA FLORESTA | MATO GROSSO | Brasil | 5100250 | 51 | 33 | nan | nan | nan | Amazônia | 6.8 |
| ccfa4ec9-2008-3b9c-9e86-cc12bef522ae | -4.42975 | -55.17096 | 2025-09-08 00:52:00 | TERRA_M-M | RURÓPOLIS | PARÁ | Brasil | 1506195 | 15 | 33 | nan | nan | nan | Amazônia | 6.6 |
| f1423de1-5bb7-376c-a165-bc3b3477b5eb | -8.21976 | -44.77589 | 2025-09-08 00:52:00 | TERRA_M-M | URUÇUÍ | PIAUÍ | Brasil | 2211209 | 22 | 33 | nan | nan | nan | Cerrado | 47.4 |
| fb4ba068-3352-3d68-81a5-e456d8a35295 | -5.78767 | -45.63606 | 2025-09-08 00:52:00 | TERRA_M-M | GRAJAÚ | MARANHÃO | Brasil | 2104800 | 21 | 33 | nan | nan | nan | Cerrado | 24.2 |
| 5ac56d0f-a0e9-3511-962c-36bcf725b89e | -8.38834 | -52.53593 | 2025-09-08 00:52:00 | TERRA_M-M | SÃO FÉLIX DO XINGU | PARÁ | Brasil | 1507300 | 15 | 33 | nan | nan | nan | Amazônia | 12.2 |
| 3640a1e1-4a08-371b-b200-4adb539f778f | -10.04919 | -59.38348 | 2025-09-08 00:52:00 | TERRA_M-M | ARIPUANÃ | MATO GROSSO | Brasil | 5101407 | 51 | 33 | nan | nan | nan | Amazônia | 35.0 |
| 400fecbd-b291-3cd7-95a8-97b9c2d3e345 | -6.46244 | -43.93958 | 2025-09-08 00:52:00 | TERRA_M-M | PARAIBANO | MARANHÃO | Brasil | 2107704 | 21 | 33 | nan | nan | nan | Cerrado | 71.8 |
| 755b4685-dc35-34a8-b42a-ba537f8f9e16 | -3.31054 | -48.72683 | 2025-09-08 00:52:00 | TERRA_M-M | TAILÂNDIA | PARÁ | Brasil | 1507953 | 15 | 33 | nan | nan | nan | Amazônia | 55.3 |
| 4a561cc4-aa2c-3136-b797-1d454ad6dab5 | -10.0682 | -59.3536 | 2025-09-08 01:00:00 | GOES-19 | ARIPUANÃ | MATO GROSSO | Brasil | 5101407 | 51 | 33 | nan | nan | nan | Amazônia | 54.3 |
| 78310230-7942-37db-82c9-048b0913d089 | -17.1564 | -44.4266 | 2025-09-08 01:00:00 | GOES-19 | JEQUITAÍ | MINAS GERAIS | Brasil | 3135605 | 31 | 33 | nan | nan | nan | Cerrado | 82.1 |
| 690bcc8a-60e8-3a9e-9cfc-159b8fa6a483 | -12.9286 | -54.7949 | 2025-09-08 01:00:00 | GOES-19 | NOVA UBIRATÃ | MATO GROSSO | Brasil | 5106240 | 51 | 33 | nan | nan | nan | Cerrado | 52.4 |
| 99f9e0a5-c4d1-3475-9a7e-ddd7d4146869 | -15.1454 | -47.9692 | 2025-09-08 01:00:00 | GOES-19 | PLANALTINA | GOIÁS | Brasil | 5217609 | 52 | 33 | nan | nan | nan | Cerrado | 89.1 |
| 5f8c7aff-82ac-36f9-9fd8-06867261c0b4 | -11.2007 | -54.9992 | 2025-09-08 01:00:00 | GOES-19 | CLÁUDIA | MATO GROSSO | Brasil | 5103056 | 51 | 33 | nan | nan | nan | Amazônia | 120.7 |
| f596380e-6140-359e-9985-ecce38eb4aee | -12.9474 | -54.8135 | 2025-09-08 01:00:00 | GOES-19 | NOVA UBIRATÃ | MATO GROSSO | Brasil | 5106240 | 51 | 33 | nan | nan | nan | Cerrado | 60.2 |
| ee47c23c-a9dc-3bc0-b7bb-813f902fb8d4 | -10.0493 | -59.3742 | 2025-09-08 01:00:00 | GOES-19 | ARIPUANÃ | MATO GROSSO | Brasil | 5101407 | 51 | 33 | nan | nan | nan | Amazônia | 66.2 |
| 5c79f556-b56d-38af-b65c-8e1a91f79371 | -12.6156 | -56.9541 | 2025-09-08 01:00:00 | GOES-19 | NOVA MARINGÁ | MATO GROSSO | Brasil | 5108907 | 51 | 33 | nan | nan | nan | Amazônia | 73.4 |
| e770df02-301e-3e5e-b006-364c9319bf34 | -9.4345 | -61.8156 | 2025-09-08 01:00:00 | GOES-19 | MACHADINHO D'OESTE | RONDÔNIA | Brasil | 1100130 | 11 | 33 | nan | nan | nan | Amazônia | 66.8 |
| 2fce7657-0a4c-3d81-8808-a8036b4223a4 | -13.6593 | -43.7983 | 2025-09-08 01:00:00 | GOES-19 | SERRA DO RAMALHO | BAHIA | Brasil | 2930154 | 29 | 33 | nan | nan | nan | Cerrado | 65.9 |
| eaab8d8f-fe5b-3953-b6f3-39391ea4778a | -9.481 | -60.4902 | 2025-09-08 01:00:00 | GOES-19 | ARIPUANÃ | MATO GROSSO | Brasil | 5101407 | 51 | 33 | nan | nan | nan | Amazônia | 104.8 |
| e1f87d8a-a1c1-3852-9ca8-b32ab2eba01f | -12.948 | -54.7724 | 2025-09-08 01:00:00 | GOES-19 | NOVA UBIRATÃ | MATO GROSSO | Brasil | 5106240 | 51 | 33 | nan | nan | nan | Amazônia | 60.1 |
| f93868ca-ea24-300a-b930-0d193f89f9f3 | -11.3745 | -50.3997 | 2025-09-08 01:00:00 | GOES-19 | LAGOA DA CONFUSÃO | TOCANTINS | Brasil | 1711902 | 17 | 33 | nan | nan | nan | Cerrado | 64.0 |
| e94e252b-a62b-3c36-9db6-8acadbeabc18 | -11.2005 | -55.0195 | 2025-09-08 01:00:00 | GOES-19 | CLÁUDIA | MATO GROSSO | Brasil | 5103056 | 51 | 33 | nan | nan | nan | Amazônia | 64.6 |
| 5fdad454-aab6-3cc7-9f99-d96ee8a06aaf | -12.6153 | -56.9742 | 2025-09-08 01:00:00 | GOES-19 | NOVA MARINGÁ | MATO GROSSO | Brasil | 5108907 | 51 | 33 | nan | nan | nan | Amazônia | 283.2 |
| f534e608-b41b-3322-b4fc-4899ccfc63c2 | -5.211 | -43.2833 | 2025-09-08 01:00:00 | GOES-19 | MATÕES | MARANHÃO | Brasil | 2106607 | 21 | 33 | nan | nan | nan | Cerrado | 93.3 |
| d2e90cb3-bdbc-3389-bec7-17f5dda56b2b | -14.5266 | -48.7833 | 2025-09-08 01:00:00 | GOES-19 | NIQUELÂNDIA | GOIÁS | Brasil | 5214606 | 52 | 33 | nan | nan | nan | Cerrado | 96.3 |
| 9730ecaf-3c7c-35a2-90c6-d451deec712e | -12.9477 | -54.793 | 2025-09-08 01:00:00 | GOES-19 | NOVA UBIRATÃ | MATO GROSSO | Brasil | 5106240 | 51 | 33 | nan | nan | nan | Amazônia | 98.2 |
| cad9fe7f-2c0f-334e-bee2-23c6606f7ab3 | -9.4531 | -61.8147 | 2025-09-08 01:00:00 | GOES-19 | MACHADINHO D'OESTE | RONDÔNIA | Brasil | 1100130 | 11 | 33 | nan | nan | nan | Amazônia | 65.0 |
| d181db29-2a0d-3b20-bfa0-cc7cc7b403e4 | -7.3982 | -61.6536 | 2025-09-08 01:00:00 | GOES-19 | MANICORÉ | AMAZONAS | Brasil | 1302702 | 13 | 33 | nan | nan | nan | Amazônia | 63.6 |
| 6ccee2c1-e6d8-3eee-a6f9-d11b0a80d7da | -12.6341 | -56.9926 | 2025-09-08 01:00:00 | GOES-19 | NOVA MARINGÁ | MATO GROSSO | Brasil | 5108907 | 51 | 33 | nan | nan | nan | Amazônia | 95.6 |
| 7953bcde-7ce5-39e9-8388-6a5fe235de3d | -14.5067 | -48.8085 | 2025-09-08 01:00:00 | GOES-19 | NIQUELÂNDIA | GOIÁS | Brasil | 5214606 | 52 | 33 | nan | nan | nan | Cerrado | 229.8 |
| e0aed02c-f7e9-3c7b-a827-25e2dfe4fed5 | -14.5262 | -48.8055 | 2025-09-08 01:00:00 | GOES-19 | NIQUELÂNDIA | GOIÁS | Brasil | 5214606 | 52 | 33 | nan | nan | nan | Cerrado | 66.8 |
| 3c8c088b-51a3-3c44-854b-a0de3a7ceb1f | -10.0495 | -59.3547 | 2025-09-08 01:00:00 | GOES-19 | ARIPUANÃ | MATO GROSSO | Brasil | 5101407 | 51 | 33 | nan | nan | nan | Amazônia | 73.6 |
| 8a494287-48ab-38be-bbcd-3f6010f14d47 | -12.6343 | -56.9725 | 2025-09-08 01:00:00 | GOES-19 | NOVA MARINGÁ | MATO GROSSO | Brasil | 5108907 | 51 | 33 | nan | nan | nan | Amazônia | 256.9 |
| d1c0ebc8-4081-3714-bcea-8e4aca8bb55c | -7.3984 | -61.6156 | 2025-09-08 01:00:00 | GOES-19 | MANICORÉ | AMAZONAS | Brasil | 1302702 | 13 | 33 | nan | nan | nan | Amazônia | 78.2 |
| 6bf81b9c-3829-3d4e-b535-c52718695345 | -7.4168 | -61.6339 | 2025-09-08 01:00:00 | GOES-19 | MANICORÉ | AMAZONAS | Brasil | 1302702 | 13 | 33 | nan | nan | nan | Amazônia | 120.7 |
| 08655543-b3a3-39ca-99bf-ebad1d3641df | -7.3799 | -61.6353 | 2025-09-08 01:00:00 | GOES-19 | MANICORÉ | AMAZONAS | Brasil | 1302702 | 13 | 33 | nan | nan | nan | Amazônia | 64.1 |
| 0eee8c6c-f183-3906-9e1e-ccc744e80fc3 | -3.316 | -48.7134 | 2025-09-08 01:00:00 | GOES-19 | IPIXUNA DO PARÁ | PARÁ | Brasil | 1503457 | 15 | 33 | nan | nan | nan | Amazônia | 73.5 |
| 4f948eb5-8ed4-35ec-874b-3ecdbcd89e2f | -11.0234 | -46.0184 | 2025-09-08 01:00:00 | GOES-19 | FORMOSA DO RIO PRETO | BAHIA | Brasil | 2911105 | 29 | 33 | nan | nan | nan | Cerrado | 53.7 |
| 7e00855a-83b0-32d3-b506-bbbf613120dc | -9.4624 | -60.4912 | 2025-09-08 01:00:00 | GOES-19 | ARIPUANÃ | MATO GROSSO | Brasil | 5101407 | 51 | 33 | nan | nan | nan | Amazônia | 72.5 |
| bc9e073f-3a4c-3370-b5bf-2b31d9bdf8d0 | -12.6346 | -56.9524 | 2025-09-08 01:00:00 | GOES-19 | NOVA MARINGÁ | MATO GROSSO | Brasil | 5108907 | 51 | 33 | nan | nan | nan | Amazônia | 62.7 |
| 12520ec2-1227-3d63-8600-8b65d8575711 | -9.4344 | -61.8347 | 2025-09-08 01:00:00 | GOES-19 | MACHADINHO D'OESTE | RONDÔNIA | Brasil | 1100130 | 11 | 33 | nan | nan | nan | Amazônia | 59.9 |
| b3f178ef-63db-30a9-a2f6-bdd645c16da8 | -14.5072 | -48.7863 | 2025-09-08 01:00:00 | GOES-19 | NIQUELÂNDIA | GOIÁS | Brasil | 5214606 | 52 | 33 | nan | nan | nan | Cerrado | 173.7 |
| 3635875b-8c10-34fc-974e-57792f968744 | -11.3742 | -50.4212 | 2025-09-08 01:00:00 | GOES-19 | LAGOA DA CONFUSÃO | TOCANTINS | Brasil | 1711902 | 17 | 33 | nan | nan | nan | Cerrado | 106.6 |
| 42f67251-84d0-3cc2-9caa-57f425adaf33 | -15.1649 | -47.9659 | 2025-09-08 01:00:00 | GOES-19 | PLANALTINA | GOIÁS | Brasil | 5217609 | 52 | 33 | nan | nan | nan | Cerrado | 76.4 |
| e8377532-47cd-31c4-9000-a4c262b2ffc2 | -8.8821 | -64.2238 | 2025-09-08 01:00:00 | GOES-19 | CANUTAMA | AMAZONAS | Brasil | 1300904 | 13 | 33 | nan | nan | nan | Amazônia | 61.4 |
| 12da3eeb-998b-3b3e-918a-eab74537390e | -8.6219 | -40.2058 | 2025-09-08 01:00:00 | GOES-19 | LAGOA GRANDE | PERNAMBUCO | Brasil | 2608750 | 26 | 33 | nan | nan | nan | Caatinga | 97.2 |
| 827e8ca5-5e4b-3c4b-907e-eae6b0100140 | -12.6151 | -56.9943 | 2025-09-08 01:00:00 | GOES-19 | NOVA MARINGÁ | MATO GROSSO | Brasil | 5108907 | 51 | 33 | nan | nan | nan | Amazônia | 96.6 |
| e3572e04-c11e-3222-9803-31ab8911e663 | -6.6384 | -53.3566 | 2025-09-08 01:00:00 | GOES-19 | SÃO FÉLIX DO XINGU | PARÁ | Brasil | 1507300 | 15 | 33 | nan | nan | nan | Amazônia | 62.7 |
| 984d08e9-118d-3500-b3cc-24ff08230d0b | -7.3983 | -61.6346 | 2025-09-08 01:00:00 | GOES-19 | MANICORÉ | AMAZONAS | Brasil | 1302702 | 13 | 33 | nan | nan | nan | Amazônia | 196.0 |
| 58559400-f513-3b59-90b1-1ad346fc1394 | -6.4605 | -43.9532 | 2025-09-08 01:00:00 | GOES-19 | PARAIBANO | MARANHÃO | Brasil | 2107704 | 21 | 33 | nan | nan | nan | Cerrado | 67.6 |
| cade9881-aa06-361d-b049-1663a7c5a8eb | -12.9286 | -54.7949 | 2025-09-08 01:10:00 | GOES-19 | NOVA UBIRATÃ | MATO GROSSO | Brasil | 5106240 | 51 | 33 | nan | nan | nan | Cerrado | 49.7 |
| 305350c1-c8ba-394a-adee-82c3e0c8672e | -6.6384 | -53.3566 | 2025-09-08 01:10:00 | GOES-19 | SÃO FÉLIX DO XINGU | PARÁ | Brasil | 1507300 | 15 | 33 | nan | nan | nan | Amazônia | 59.3 |
| 674f82bd-85cf-3e5a-8fdc-4676a080c245 | -9.4624 | -60.4912 | 2025-09-08 01:10:00 | GOES-19 | ARIPUANÃ | MATO GROSSO | Brasil | 5101407 | 51 | 33 | nan | nan | nan | Amazônia | 65.3 |
| c9484d67-cb24-3e0e-912f-6f330dca6e56 | -12.6153 | -56.9742 | 2025-09-08 01:10:00 | GOES-19 | NOVA MARINGÁ | MATO GROSSO | Brasil | 5108907 | 51 | 33 | nan | nan | nan | Amazônia | 247.3 |
| cbcb24a3-5b04-35eb-a0af-9afba6681d0f | -14.5072 | -48.7863 | 2025-09-08 01:10:00 | GOES-19 | NIQUELÂNDIA | GOIÁS | Brasil | 5214606 | 52 | 33 | nan | nan | nan | Cerrado | 139.9 |
| be856c97-0a37-3941-b686-c2de06a4eedb | -11.3558 | -50.3804 | 2025-09-08 01:10:00 | GOES-19 | LAGOA DA CONFUSÃO | TOCANTINS | Brasil | 1711902 | 17 | 33 | nan | nan | nan | Cerrado | 68.0 |
| 8334eea2-8d72-3b6d-b3cd-efb75ce4f359 | -8.6219 | -40.2058 | 2025-09-08 01:10:00 | GOES-19 | LAGOA GRANDE | PERNAMBUCO | Brasil | 2608750 | 26 | 33 | nan | nan | nan | Caatinga | 76.6 |
| c177856f-803e-3072-a157-cbf73d2a7e19 | -14.5262 | -48.8055 | 2025-09-08 01:10:00 | GOES-19 | NIQUELÂNDIA | GOIÁS | Brasil | 5214606 | 52 | 33 | nan | nan | nan | Cerrado | 84.4 |
| 608bcae4-3de8-3617-9576-789b7c162f56 | -7.4168 | -61.6339 | 2025-09-08 01:10:00 | GOES-19 | MANICORÉ | AMAZONAS | Brasil | 1302702 | 13 | 33 | nan | nan | nan | Amazônia | 103.4 |
| d7e7428a-d0b8-3368-b5d9-5a2a60852e19 | -11.2007 | -54.9992 | 2025-09-08 01:10:00 | GOES-19 | CLÁUDIA | MATO GROSSO | Brasil | 5103056 | 51 | 33 | nan | nan | nan | Amazônia | 120.9 |
| 09a441f4-bb19-3e31-9396-82cf11d407bc | -22.3306 | -52.2665 | 2025-09-08 01:10:00 | GOES-19 | TEODORO SAMPAIO | SÃO PAULO | Brasil | 3554300 | 35 | 33 | nan | nan | nan | Mata Atlântica | 84.8 |
| e02824d0-5eba-309a-a29a-60f0b5543401 | -12.6341 | -56.9926 | 2025-09-08 01:10:00 | GOES-19 | NOVA MARINGÁ | MATO GROSSO | Brasil | 5108907 | 51 | 33 | nan | nan | nan | Amazônia | 75.5 |
| f98bd856-be8c-3799-9aec-bb68bc0e82fb | -9.481 | -60.4902 | 2025-09-08 01:10:00 | GOES-19 | ARIPUANÃ | MATO GROSSO | Brasil | 5101407 | 51 | 33 | nan | nan | nan | Amazônia | 119.5 |
| 83d8b5c1-6aee-314e-aa81-64a27d50203d | -11.2831 | -46.4591 | 2025-09-08 01:10:00 | GOES-19 | FORMOSA DO RIO PRETO | BAHIA | Brasil | 2911105 | 29 | 33 | nan | nan | nan | Cerrado | 60.9 |
| 322c2245-4dd6-3f43-a2ff-074c7edaa1ec | -12.9477 | -54.793 | 2025-09-08 01:10:00 | GOES-19 | NOVA UBIRATÃ | MATO GROSSO | Brasil | 5106240 | 51 | 33 | nan | nan | nan | Amazônia | 95.7 |
| b4bd5003-12ff-3aea-bdd4-b93796c61618 | -7.4169 | -61.6149 | 2025-09-08 01:10:00 | GOES-19 | MANICORÉ | AMAZONAS | Brasil | 1302702 | 13 | 33 | nan | nan | nan | Amazônia | 61.8 |
| 212723b8-7bbb-3080-8343-cb9bca10e480 | -9.4345 | -61.8156 | 2025-09-08 01:10:00 | GOES-19 | MACHADINHO D'OESTE | RONDÔNIA | Brasil | 1100130 | 11 | 33 | nan | nan | nan | Amazônia | 77.7 |
| cc7bd289-1f0a-3640-9427-fc14cdd0f92c | -11.2005 | -55.0195 | 2025-09-08 01:10:00 | GOES-19 | CLÁUDIA | MATO GROSSO | Brasil | 5103056 | 51 | 33 | nan | nan | nan | Amazônia | 64.5 |
| c750dc79-4171-3ac9-a28a-f6421f337816 | -14.4873 | -48.8115 | 2025-09-08 01:10:00 | GOES-19 | NIQUELÂNDIA | GOIÁS | Brasil | 5214606 | 52 | 33 | nan | nan | nan | Cerrado | 58.5 |
| 310b8b83-4bf7-35e0-b800-db8ad0031927 | -12.6151 | -56.9943 | 2025-09-08 01:10:00 | GOES-19 | NOVA MARINGÁ | MATO GROSSO | Brasil | 5108907 | 51 | 33 | nan | nan | nan | Amazônia | 65.6 |
| d5b5da75-f1bf-346a-b60e-b3357e44268c | -14.5067 | -48.8085 | 2025-09-08 01:10:00 | GOES-19 | NIQUELÂNDIA | GOIÁS | Brasil | 5214606 | 52 | 33 | nan | nan | nan | Cerrado | 231.2 |
| 385581bc-9ceb-3db7-8eeb-483dee25d680 | -12.6343 | -56.9725 | 2025-09-08 01:10:00 | GOES-19 | NOVA MARINGÁ | MATO GROSSO | Brasil | 5108907 | 51 | 33 | nan | nan | nan | Amazônia | 247.8 |
| 3bd8c550-03b5-39f1-ad01-1c050ea554c6 | -9.4531 | -61.8147 | 2025-09-08 01:10:00 | GOES-19 | MACHADINHO D'OESTE | RONDÔNIA | Brasil | 1100130 | 11 | 33 | nan | nan | nan | Amazônia | 72.4 |
| 7a9a6152-4906-3dbc-bfad-2f4caf67e833 | -12.9474 | -54.8135 | 2025-09-08 01:10:00 | GOES-19 | NOVA UBIRATÃ | MATO GROSSO | Brasil | 5106240 | 51 | 33 | nan | nan | nan | Cerrado | 54.9 |
| e17faf8c-553b-3ef6-b4e9-733c656336e4 | -7.3799 | -61.6353 | 2025-09-08 01:10:00 | GOES-19 | MANICORÉ | AMAZONAS | Brasil | 1302702 | 13 | 33 | nan | nan | nan | Amazônia | 61.4 |
| 6bc709b5-f53a-31c0-83e5-d57a4f0a7b29 | -3.316 | -48.7134 | 2025-09-08 01:10:00 | GOES-19 | IPIXUNA DO PARÁ | PARÁ | Brasil | 1503457 | 15 | 33 | nan | nan | nan | Amazônia | 69.2 |
| e8fba367-fedf-3547-b393-b8ab78e7f389 | -14.5266 | -48.7833 | 2025-09-08 01:10:00 | GOES-19 | NIQUELÂNDIA | GOIÁS | Brasil | 5214606 | 52 | 33 | nan | nan | nan | Cerrado | 102.0 |
| 6ac6a453-ae52-353f-81a0-5dab65903206 | -7.3983 | -61.6346 | 2025-09-08 01:10:00 | GOES-19 | MANICORÉ | AMAZONAS | Brasil | 1302702 | 13 | 33 | nan | nan | nan | Amazônia | 192.2 |
| 72546574-19e4-321f-aaf8-cb3a3321a7f7 | -12.948 | -54.7724 | 2025-09-08 01:10:00 | GOES-19 | NOVA UBIRATÃ | MATO GROSSO | Brasil | 5106240 | 51 | 33 | nan | nan | nan | Amazônia | 62.3 |
| 1081483e-2ab6-3702-9c2d-2745a88185a3 | -7.3984 | -61.6156 | 2025-09-08 01:10:00 | GOES-19 | MANICORÉ | AMAZONAS | Brasil | 1302702 | 13 | 33 | nan | nan | nan | Amazônia | 98.0 |
| e092e35c-9db7-3074-8cd8-9631276ed587 | -12.3105 | -57.048199 | 2025-09-08 01:14:00 | METOP-B | NOVA MARINGÁ | MATO GROSSO | Brasil | 5108907 | 51 | 33 | nan | nan | nan | Amazônia | nan |
| 86fc63fc-5ab6-3a10-afdc-cecf30599628 | -8.8879 | -65.966599 | 2025-09-08 01:14:00 | METOP-B | LÁBREA | AMAZONAS | Brasil | 1302405 | 13 | 33 | nan | nan | nan | Amazônia | nan |
| 50deead0-10b4-3ee2-9022-3d540d368d5e | -9.6283 | -60.204201 | 2025-09-08 01:14:00 | METOP-B | ARIPUANÃ | MATO GROSSO | Brasil | 5101407 | 51 | 33 | nan | nan | nan | Amazônia | nan |
| c03c897e-7a2d-397a-b006-d6868cece2c3 | -7.0852 | -61.6917 | 2025-09-08 01:14:00 | METOP-B | MANICORÉ | AMAZONAS | Brasil | 1302702 | 13 | 33 | nan | nan | nan | Amazônia | nan |
| e4dc258f-b1a1-3f16-a6b2-6f5cd5bf7d52 | -9.9588 | -63.221802 | 2025-09-08 01:14:00 | METOP-B | ARIQUEMES | RONDÔNIA | Brasil | 1100023 | 11 | 33 | nan | nan | nan | Amazônia | nan |
| 3daebd6e-2012-3de6-a2ab-3fd2d203fe51 | -6.3057 | -53.437 | 2025-09-08 01:14:00 | METOP-B | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| 73099ab3-d245-3b12-b7f3-37e5e60e6431 | -8.7668 | -64.572502 | 2025-09-08 01:14:00 | METOP-B | LÁBREA | AMAZONAS | Brasil | 1302405 | 13 | 33 | nan | nan | nan | Amazônia | nan |
| 3bca30f9-a488-3b64-bb9f-d6b3cee2d5e3 | -8.8863 | -65.959198 | 2025-09-08 01:14:00 | METOP-B | LÁBREA | AMAZONAS | Brasil | 1302405 | 13 | 33 | nan | nan | nan | Amazônia | nan |
| 74360abd-ef10-3b90-84e4-78147f07fbad | -12.3172 | -57.033401 | 2025-09-08 01:14:00 | METOP-B | NOVA MARINGÁ | MATO GROSSO | Brasil | 5108907 | 51 | 33 | nan | nan | nan | Amazônia | nan |
| 1b4e706e-8209-3fe4-b438-ccc3ca9cbee5 | -9.1503 | -60.543201 | 2025-09-08 01:14:00 | METOP-B | COLNIZA | MATO GROSSO | Brasil | 5103254 | 51 | 33 | nan | nan | nan | Amazônia | nan |
| 6f0d8269-ede6-3c6f-8251-0fe1525cded1 | -10.2595 | -61.322701 | 2025-09-08 01:14:00 | METOP-B | RONDOLÂNDIA | MATO GROSSO | Brasil | 5107578 | 51 | 33 | nan | nan | nan | Amazônia | nan |
| 61d9f065-aed3-305c-9504-79fc18ba631b | -8.7683 | -64.579498 | 2025-09-08 01:14:00 | METOP-B | LÁBREA | AMAZONAS | Brasil | 1302405 | 13 | 33 | nan | nan | nan | Amazônia | nan |
| 3d3d99a3-116d-3fde-bc5f-457e4a2d0d64 | -10.1856 | -57.861599 | 2025-09-08 01:14:00 | METOP-B | NOVA BANDEIRANTES | MATO GROSSO | Brasil | 5106158 | 51 | 33 | nan | nan | nan | Amazônia | nan |


[Clique aqui para ver as próximas entradas](README14.md)
