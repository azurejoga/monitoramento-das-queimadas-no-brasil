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

## Dados Diários - Página 41

| ID | Latitude | Longitude | Data/Hora GMT | Satélite | Município | Estado | País | Município ID | Estado ID | País ID | Dias sem Chuva | Precipitação | Risco de Fogo | Bioma | FRP |
|----|----------|-----------|---------------|----------|-----------|--------|------|--------------|-----------|---------|----------------|--------------|----------------|-------|-----|
| 9c4a3c6d-09f9-320a-b4bf-5c3c6ce0697f | -3.41634 | -48.87694 | 2025-08-21 04:38:00 | NOAA-20 | IPIXUNA DO PARÁ | PARÁ | Brasil | 1503457 | 15 | 33 | nan | nan | nan | Amazônia | 0.7 |
| 9cce3953-bd8e-3246-979a-b5b3c8ff06f1 | -3.36514 | -43.36537 | 2025-08-21 04:38:00 | NOAA-20 | URBANO SANTOS | MARANHÃO | Brasil | 2112605 | 21 | 33 | nan | nan | nan | Cerrado | 0.7 |
| a4f1ec8c-0a71-3d13-b303-caa66bc77c47 | -4.71537 | -47.219 | 2025-08-21 04:38:00 | NOAA-20 | AÇAILÂNDIA | MARANHÃO | Brasil | 2100055 | 21 | 33 | nan | nan | nan | Amazônia | 1.0 |
| e52b026e-68ce-3d40-af6b-052efc4f5108 | -6.10181 | -44.6404 | 2025-08-21 04:38:00 | NOAA-20 | MIRADOR | MARANHÃO | Brasil | 2106706 | 21 | 33 | nan | nan | nan | Cerrado | 1.3 |
| 8bd421f9-d75a-3c6c-80ac-3aacab731682 | -5.93296 | -47.3151 | 2025-08-21 04:38:00 | NOAA-20 | RIBAMAR FIQUENE | MARANHÃO | Brasil | 2109551 | 21 | 33 | nan | nan | nan | Cerrado | 1.1 |
| c38e5cc0-249a-3152-a955-685ecf7e02b8 | -7.88965 | -46.72946 | 2025-08-21 04:38:00 | NOAA-20 | RIACHÃO | MARANHÃO | Brasil | 2109502 | 21 | 33 | nan | nan | nan | Cerrado | 3.5 |
| 0d01d3ed-1710-318d-b86a-a69feeecc67d | -5.08954 | -47.71649 | 2025-08-21 04:38:00 | NOAA-20 | CIDELÂNDIA | MARANHÃO | Brasil | 2103257 | 21 | 33 | nan | nan | nan | Amazônia | 2.6 |
| 7a33ffdf-5ad3-3f50-bfb1-794b7b588920 | -6.96543 | -44.15283 | 2025-08-21 04:38:00 | NOAA-20 | PORTO ALEGRE DO PIAUÍ | PIAUÍ | Brasil | 2208551 | 22 | 33 | nan | nan | nan | Cerrado | 1.7 |
| 81925339-1600-3df0-b968-93dade41e0ef | -6.551 | -44.48793 | 2025-08-21 04:38:00 | NOAA-20 | SUCUPIRA DO NORTE | MARANHÃO | Brasil | 2111904 | 21 | 33 | nan | nan | nan | Cerrado | 1.1 |
| 6c79c3d6-3c38-31f9-a603-43b07b8d6160 | -2.93452 | -53.69718 | 2025-08-21 04:38:00 | NOAA-20 | MEDICILÂNDIA | PARÁ | Brasil | 1504455 | 15 | 33 | nan | nan | nan | Amazônia | 1.7 |
| e820f6e7-2666-396e-a73b-29def26fbf88 | -6.45269 | -53.38287 | 2025-08-21 04:38:00 | NOAA-20 | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 1.5 |
| dc5961e1-9c2b-3d2c-b023-f873da2af3f0 | -8.42837 | -49.57498 | 2025-08-21 04:38:00 | NOAA-20 | CONCEIÇÃO DO ARAGUAIA | PARÁ | Brasil | 1502707 | 15 | 33 | nan | nan | nan | Amazônia | 1.6 |
| aefff4fd-ce76-3d8d-8daf-d17db3aa235b | -7.42063 | -46.86975 | 2025-08-21 04:38:00 | NOAA-20 | RIACHÃO | MARANHÃO | Brasil | 2109502 | 21 | 33 | nan | nan | nan | Cerrado | 1.0 |
| 2e905acc-cb71-3ad1-b0aa-aaca412bb2c7 | -4.86318 | -42.54231 | 2025-08-21 04:38:00 | NOAA-20 | JOSÉ DE FREITAS | PIAUÍ | Brasil | 2205508 | 22 | 33 | nan | nan | nan | Caatinga | 1.5 |
| 25176e31-582c-3ad4-b7c7-04365453ae00 | -3.97933 | -51.06651 | 2025-08-21 04:38:00 | NOAA-20 | PACAJÁ | PARÁ | Brasil | 1505486 | 15 | 33 | nan | nan | nan | Amazônia | 1.7 |
| 63e45db4-bf1e-33e9-be5f-0d3cd9260b41 | -7.01905 | -44.61344 | 2025-08-21 04:38:00 | NOAA-20 | BENEDITO LEITE | MARANHÃO | Brasil | 2101806 | 21 | 33 | nan | nan | nan | Cerrado | 17.8 |
| 6ca59eee-6dbb-3aab-8138-ffafb0812ab6 | -5.97093 | -44.13674 | 2025-08-21 04:38:00 | NOAA-20 | COLINAS | MARANHÃO | Brasil | 2103505 | 21 | 33 | nan | nan | nan | Cerrado | 2.6 |
| b3f2cb40-aa62-39f5-b145-8f2965aa53fb | -5.88146 | -50.15232 | 2025-08-21 04:38:00 | NOAA-20 | MARABÁ | PARÁ | Brasil | 1504208 | 15 | 33 | nan | nan | nan | Amazônia | 1.0 |
| d487d4cb-2a7d-3cc1-b306-3db7725f625f | -6.01601 | -42.82622 | 2025-08-21 04:38:00 | NOAA-20 | PALMEIRAIS | PIAUÍ | Brasil | 2207504 | 22 | 33 | nan | nan | nan | Caatinga | 1.8 |
| 1d4c134f-4899-3992-aaa9-b0f19f6b0a44 | -5.95955 | -44.13563 | 2025-08-21 04:38:00 | NOAA-20 | COLINAS | MARANHÃO | Brasil | 2103505 | 21 | 33 | nan | nan | nan | Cerrado | 6.8 |
| 579faff7-01ee-35b1-922a-630a3e29609d | -5.13094 | -43.09641 | 2025-08-21 04:38:00 | NOAA-20 | TIMON | MARANHÃO | Brasil | 2112209 | 21 | 33 | nan | nan | nan | Cerrado | 0.9 |
| 3963e0aa-2205-3997-a8ca-b88dae1ec5f5 | -8.34456 | -47.50047 | 2025-08-21 04:38:00 | NOAA-20 | GOIATINS | TOCANTINS | Brasil | 1709005 | 17 | 33 | nan | nan | nan | Cerrado | 1.5 |
| 66821d3d-86db-393e-8cd3-da35db6fc437 | -4.86845 | -45.04877 | 2025-08-21 04:38:00 | NOAA-20 | POÇÃO DE PEDRAS | MARANHÃO | Brasil | 2108900 | 21 | 33 | nan | nan | nan | Cerrado | 1.2 |
| aa1aa4d6-8f6b-3f32-8c3c-54967aaa3da0 | -3.9857 | -47.88638 | 2025-08-21 04:38:00 | NOAA-20 | ULIANÓPOLIS | PARÁ | Brasil | 1508126 | 15 | 33 | nan | nan | nan | Amazônia | 1.2 |
| d0d7930e-0018-3452-b7b1-96c0779ea36b | -2.58219 | -51.91206 | 2025-08-21 04:38:00 | NOAA-20 | SENADOR JOSÉ PORFÍRIO | PARÁ | Brasil | 1507805 | 15 | 33 | nan | nan | nan | Amazônia | 2.5 |
| 63d62a99-7b4f-34ae-bcd6-3a17383ae586 | -7.59606 | -55.4739 | 2025-08-21 04:38:00 | NOAA-20 | NOVO PROGRESSO | PARÁ | Brasil | 1505031 | 15 | 33 | nan | nan | nan | Amazônia | 1.7 |
| 13da11ef-3251-3754-af92-179642968411 | -6.177 | -44.73515 | 2025-08-21 04:38:00 | NOAA-20 | MIRADOR | MARANHÃO | Brasil | 2106706 | 21 | 33 | nan | nan | nan | Cerrado | 2.2 |
| 7489dd07-3505-3f73-9191-fbdbb79b366b | -6.49633 | -43.10328 | 2025-08-21 04:38:00 | NOAA-20 | BARÃO DE GRAJAÚ | MARANHÃO | Brasil | 2101509 | 21 | 33 | nan | nan | nan | Cerrado | 2.8 |
| 8533c5e5-a297-335c-92d2-2870e00844d3 | -7.38303 | -47.04855 | 2025-08-21 04:38:00 | NOAA-20 | CAROLINA | MARANHÃO | Brasil | 2102804 | 21 | 33 | nan | nan | nan | Cerrado | 0.5 |
| b991ddd6-8eb9-39d5-a5e5-9cb65f9b1b05 | -6.10852 | -45.90266 | 2025-08-21 04:38:00 | NOAA-20 | GRAJAÚ | MARANHÃO | Brasil | 2104800 | 21 | 33 | nan | nan | nan | Cerrado | 1.0 |
| c2709ac1-42ee-32db-a72e-85d7b7b53c4b | -3.991 | -42.51389 | 2025-08-21 04:38:00 | NOAA-20 | CAMPO LARGO DO PIAUÍ | PIAUÍ | Brasil | 2202174 | 22 | 33 | nan | nan | nan | Caatinga | 1.4 |
| 30647b64-57e4-30fd-93f4-33cfa9902c73 | -4.01702 | -49.50427 | 2025-08-21 04:38:00 | NOAA-20 | BREU BRANCO | PARÁ | Brasil | 1501782 | 15 | 33 | nan | nan | nan | Amazônia | 3.0 |
| df65b6d0-c5c8-339e-a7be-b27c2287edac | -2.25619 | -47.85072 | 2025-08-21 04:38:00 | NOAA-20 | AURORA DO PARÁ | PARÁ | Brasil | 1500958 | 15 | 33 | nan | nan | nan | Amazônia | 1.5 |
| 4d3e7f71-42db-3776-9c7c-e28513d83ab0 | -6.71231 | -44.32376 | 2025-08-21 04:38:00 | NOAA-20 | PASTOS BONS | MARANHÃO | Brasil | 2108009 | 21 | 33 | nan | nan | nan | Cerrado | 0.6 |
| d08e4c79-6256-360b-9755-ab7f8d05a938 | -6.07064 | -44.13649 | 2025-08-21 04:38:00 | NOAA-20 | COLINAS | MARANHÃO | Brasil | 2103505 | 21 | 33 | nan | nan | nan | Cerrado | 1.0 |
| 51d5b47d-2526-31ea-aaae-d6e4b9af5e7a | -5.78621 | -45.06901 | 2025-08-21 04:38:00 | NOAA-20 | BARRA DO CORDA | MARANHÃO | Brasil | 2101608 | 21 | 33 | nan | nan | nan | Cerrado | 3.8 |
| bdf9dec4-a729-3f64-9b10-4aa023591977 | -7.20676 | -46.24807 | 2025-08-21 04:38:00 | NOAA-20 | NOVA COLINAS | MARANHÃO | Brasil | 2107258 | 21 | 33 | nan | nan | nan | Cerrado | 2.0 |
| db1381e8-3c1e-3991-90d6-9e9cc7b4c3b8 | -4.13203 | -48.01714 | 2025-08-21 04:38:00 | NOAA-20 | DOM ELISEU | PARÁ | Brasil | 1502939 | 15 | 33 | nan | nan | nan | Amazônia | 2.8 |
| f1d3e865-501f-3e8e-b6d7-b03990cf2b03 | -7.85572 | -45.18727 | 2025-08-21 04:38:00 | NOAA-20 | BAIXA GRANDE DO RIBEIRO | PIAUÍ | Brasil | 2201150 | 22 | 33 | nan | nan | nan | Cerrado | 1.7 |
| 0757be81-3187-3b9c-8acf-4ca6614bd2ca | -4.78112 | -45.3188 | 2025-08-21 04:38:00 | NOAA-20 | LAGO DA PEDRA | MARANHÃO | Brasil | 2105708 | 21 | 33 | nan | nan | nan | Cerrado | 1.2 |
| e300d6a8-6641-3868-b09a-ce09e49fda95 | -4.71195 | -47.21846 | 2025-08-21 04:38:00 | NOAA-20 | AÇAILÂNDIA | MARANHÃO | Brasil | 2100055 | 21 | 33 | nan | nan | nan | Amazônia | 6.0 |
| e6d50b8d-8c3c-38fe-9778-258ec75495fd | -3.96648 | -47.88312 | 2025-08-21 04:38:00 | NOAA-20 | ULIANÓPOLIS | PARÁ | Brasil | 1508126 | 15 | 33 | nan | nan | nan | Amazônia | 0.5 |
| a352fe39-11ab-3577-b949-2edf6049195e | -5.96219 | -44.13922 | 2025-08-21 04:38:00 | NOAA-20 | COLINAS | MARANHÃO | Brasil | 2103505 | 21 | 33 | nan | nan | nan | Cerrado | 1.4 |
| 051aec56-2667-3324-abc2-5b4b2e58f0f4 | -3.81944 | -41.56076 | 2025-08-21 04:38:00 | NOAA-20 | PIRACURUCA | PIAUÍ | Brasil | 2208304 | 22 | 33 | nan | nan | nan | Caatinga | 2.2 |
| 520535cc-8559-3ed6-820d-62b0f7c8391c | -7.14594 | -44.17884 | 2025-08-21 04:38:00 | NOAA-20 | ANTÔNIO ALMEIDA | PIAUÍ | Brasil | 2200806 | 22 | 33 | nan | nan | nan | Cerrado | 1.5 |
| fe1d2bf0-7ff5-3e0d-96dd-472e20ec5780 | -4.30938 | -48.09813 | 2025-08-21 04:38:00 | NOAA-20 | RONDON DO PARÁ | PARÁ | Brasil | 1506187 | 15 | 33 | nan | nan | nan | Amazônia | 0.6 |
| dec0ba96-b835-383e-aee2-5da915c39d6e | -8.37949 | -44.60131 | 2025-08-21 04:38:00 | NOAA-20 | PALMEIRA DO PIAUÍ | PIAUÍ | Brasil | 2207405 | 22 | 33 | nan | nan | nan | Cerrado | 1.5 |
| 41d58f80-c2df-390e-9947-c7c795e1993f | -6.21604 | -43.33451 | 2025-08-21 04:38:00 | NOAA-20 | LAGOA DO MATO | MARANHÃO | Brasil | 2105922 | 21 | 33 | nan | nan | nan | Cerrado | 2.5 |
| caba1a28-9981-33b3-a7a3-eaf9849cee51 | -5.87204 | -50.14731 | 2025-08-21 04:38:00 | NOAA-20 | MARABÁ | PARÁ | Brasil | 1504208 | 15 | 33 | nan | nan | nan | Amazônia | 1.0 |
| 34d1b406-eaa6-3446-b1c4-b3e300bd00a8 | -7.60474 | -44.38562 | 2025-08-21 04:38:00 | NOAA-20 | URUÇUÍ | PIAUÍ | Brasil | 2211209 | 22 | 33 | nan | nan | nan | Cerrado | 1.4 |
| 9e287a8a-ef41-318c-9a11-44a75e7deb6c | -6.07161 | -44.13655 | 2025-08-21 04:38:00 | NOAA-20 | COLINAS | MARANHÃO | Brasil | 2103505 | 21 | 33 | nan | nan | nan | Cerrado | 1.1 |
| a7e93bec-17c2-3a1b-b55d-0a614ca83c3b | -6.5648 | -44.47867 | 2025-08-21 04:38:00 | NOAA-20 | SUCUPIRA DO NORTE | MARANHÃO | Brasil | 2111904 | 21 | 33 | nan | nan | nan | Cerrado | 1.5 |
| a9c5dc18-e2a0-30f9-aaee-22652a904e6e | -4.64845 | -41.40794 | 2025-08-21 04:38:00 | NOAA-20 | MILTON BRANDÃO | PIAUÍ | Brasil | 2206357 | 22 | 33 | nan | nan | nan | Caatinga | 2.9 |
| 8d0c76ff-69a7-3792-9b10-bd0df4f01032 | -7.23396 | -44.70587 | 2025-08-21 04:38:00 | NOAA-20 | SÃO FÉLIX DE BALSAS | MARANHÃO | Brasil | 2110807 | 21 | 33 | nan | nan | nan | Cerrado | 1.5 |
| 161d04a8-edff-3033-ba00-44a5107d2214 | -3.36098 | -43.36478 | 2025-08-21 04:38:00 | NOAA-20 | URBANO SANTOS | MARANHÃO | Brasil | 2112605 | 21 | 33 | nan | nan | nan | Cerrado | 0.7 |
| fa6548e2-3f56-39f5-9f7f-4355a54b89d7 | -6.01807 | -44.35357 | 2025-08-21 04:38:00 | NOAA-20 | MIRADOR | MARANHÃO | Brasil | 2106706 | 21 | 33 | nan | nan | nan | Cerrado | 0.9 |
| 3dc6d08d-4115-3efd-b079-09265e726600 | -2.38497 | -47.66013 | 2025-08-21 04:38:00 | NOAA-20 | IPIXUNA DO PARÁ | PARÁ | Brasil | 1503457 | 15 | 33 | nan | nan | nan | Amazônia | 2.0 |
| 628acf78-59b4-310c-af62-30bc48d48316 | -9.33405 | -48.51998 | 2025-08-21 04:38:00 | NOAA-20 | RIO DOS BOIS | TOCANTINS | Brasil | 1718709 | 17 | 33 | nan | nan | nan | Cerrado | 2.5 |
| 984eb425-5782-3b5b-b05d-6c2bda9a86f2 | -6.26894 | -43.71502 | 2025-08-21 04:38:00 | NOAA-20 | PASSAGEM FRANCA | MARANHÃO | Brasil | 2107902 | 21 | 33 | nan | nan | nan | Cerrado | 1.3 |
| b70b81b1-fc1a-3aa4-ba54-ea303c457900 | -8.8359 | -52.0495 | 2025-08-21 04:38:00 | NOAA-20 | SÃO FÉLIX DO XINGU | PARÁ | Brasil | 1507300 | 15 | 33 | nan | nan | nan | Amazônia | 4.3 |
| 3e5e6e04-cc05-3238-bf88-4d02e7bbd849 | -2.73152 | -47.44293 | 2025-08-21 04:38:00 | NOAA-20 | IPIXUNA DO PARÁ | PARÁ | Brasil | 1503457 | 15 | 33 | nan | nan | nan | Amazônia | 1.3 |
| adfae3c7-d3ec-3d64-bc2e-fa80ea5f7543 | -2.44588 | -47.33028 | 2025-08-21 04:38:00 | NOAA-20 | CAPITÃO POÇO | PARÁ | Brasil | 1502301 | 15 | 33 | nan | nan | nan | Amazônia | 1.7 |
| ebd03144-48e3-3da8-930f-423f358f7a78 | -7.64673 | -45.25 | 2025-08-21 04:38:00 | NOAA-20 | RIBEIRO GONÇALVES | PIAUÍ | Brasil | 2208908 | 22 | 33 | nan | nan | nan | Cerrado | 2.1 |
| 441b34b0-f2c5-33c5-b67c-119f03695e00 | -7.723 | -46.61714 | 2025-08-21 04:38:00 | NOAA-20 | RIACHÃO | MARANHÃO | Brasil | 2109502 | 21 | 33 | nan | nan | nan | Cerrado | 1.4 |
| bacb8bb7-f4b0-3087-bfe7-28360ff00b6f | -6.07374 | -44.11497 | 2025-08-21 04:38:00 | NOAA-20 | COLINAS | MARANHÃO | Brasil | 2103505 | 21 | 33 | nan | nan | nan | Cerrado | 1.3 |
| 0f0c7f3b-43a0-39d2-ade3-0d9bee90bc2f | -3.72198 | -50.94213 | 2025-08-21 04:38:00 | NOAA-20 | PACAJÁ | PARÁ | Brasil | 1505486 | 15 | 33 | nan | nan | nan | Amazônia | 1.3 |
| 41e7fa4b-3b39-3a20-bf39-60c77bf09a4b | -5.89913 | -45.55238 | 2025-08-21 04:38:00 | NOAA-20 | GRAJAÚ | MARANHÃO | Brasil | 2104800 | 21 | 33 | nan | nan | nan | Cerrado | 0.8 |
| 667c2693-4458-3ac5-9ed3-009bdc78328f | -6.42591 | -44.6691 | 2025-08-21 04:38:00 | NOAA-20 | MIRADOR | MARANHÃO | Brasil | 2106706 | 21 | 33 | nan | nan | nan | Cerrado | 2.0 |
| 1863795c-14aa-32e4-a2e7-4a912a77fc8a | -4.58936 | -48.78269 | 2025-08-21 04:38:00 | NOAA-20 | RONDON DO PARÁ | PARÁ | Brasil | 1506187 | 15 | 33 | nan | nan | nan | Amazônia | 0.9 |
| 8011c2c8-5709-3004-8b94-170fcc0e8329 | -8.26066 | -47.29172 | 2025-08-21 04:38:00 | NOAA-20 | GOIATINS | TOCANTINS | Brasil | 1709005 | 17 | 33 | nan | nan | nan | Cerrado | 1.3 |
| e44df694-3d92-39b7-a3c4-8ce292fb45bd | -9.29581 | -48.4236 | 2025-08-21 04:38:00 | NOAA-20 | RIO DOS BOIS | TOCANTINS | Brasil | 1718709 | 17 | 33 | nan | nan | nan | Cerrado | 1.7 |
| ad89ee6b-5335-3abf-a412-659e2c4efc25 | -2.90682 | -48.25016 | 2025-08-21 04:38:00 | NOAA-20 | TOMÉ-AÇU | PARÁ | Brasil | 1508001 | 15 | 33 | nan | nan | nan | Amazônia | 1.8 |
| 2cbef510-4aa6-329b-b665-1403ff81455b | -6.02498 | -42.8275 | 2025-08-21 04:38:00 | NOAA-20 | PALMEIRAIS | PIAUÍ | Brasil | 2207504 | 22 | 33 | nan | nan | nan | Caatinga | 1.3 |
| 778bb6b0-c7e6-3ce8-b5ee-a69a90690dba | -7.65023 | -46.25481 | 2025-08-21 04:38:00 | NOAA-20 | BALSAS | MARANHÃO | Brasil | 2101400 | 21 | 33 | nan | nan | nan | Cerrado | 1.5 |
| d4788105-8357-3c38-a212-a5b074f64d82 | -2.58376 | -51.92525 | 2025-08-21 04:38:00 | NOAA-20 | SENADOR JOSÉ PORFÍRIO | PARÁ | Brasil | 1507805 | 15 | 33 | nan | nan | nan | Amazônia | 1.3 |
| 473c090c-31d3-32d7-99d8-50a57924b348 | -5.95684 | -44.15356 | 2025-08-21 04:38:00 | NOAA-20 | COLINAS | MARANHÃO | Brasil | 2103505 | 21 | 33 | nan | nan | nan | Cerrado | 1.0 |
| a27168ba-be00-3a82-b2e2-e657eb90f6e8 | -6.52735 | -45.4602 | 2025-08-21 04:38:00 | NOAA-20 | MIRADOR | MARANHÃO | Brasil | 2106706 | 21 | 33 | nan | nan | nan | Cerrado | 0.7 |
| f4f021d3-6cd1-3fdb-a202-5ea1e5337dda | -2.38831 | -47.66064 | 2025-08-21 04:38:00 | NOAA-20 | IPIXUNA DO PARÁ | PARÁ | Brasil | 1503457 | 15 | 33 | nan | nan | nan | Amazônia | 2.0 |
| 8c8d1691-438b-35ed-9da7-fcf4ea6d7515 | -3.98655 | -42.51324 | 2025-08-21 04:38:00 | NOAA-20 | CAMPO LARGO DO PIAUÍ | PIAUÍ | Brasil | 2202174 | 22 | 33 | nan | nan | nan | Caatinga | 1.4 |
| ed9bfce9-aede-3957-8a79-d157a6ea1298 | -6.26303 | -43.72601 | 2025-08-21 04:38:00 | NOAA-20 | PASSAGEM FRANCA | MARANHÃO | Brasil | 2107902 | 21 | 33 | nan | nan | nan | Cerrado | 1.7 |
| af1a1140-08ea-3f98-8985-b6458707b077 | -7.02257 | -44.61756 | 2025-08-21 04:38:00 | NOAA-20 | BENEDITO LEITE | MARANHÃO | Brasil | 2101806 | 21 | 33 | nan | nan | nan | Cerrado | 23.3 |
| cce6297a-e2e4-3363-ac8f-841b5c752247 | -5.13462 | -56.97875 | 2025-08-21 04:38:00 | NOAA-20 | ITAITUBA | PARÁ | Brasil | 1503606 | 15 | 33 | nan | nan | nan | Amazônia | 3.1 |
| 9dcae49b-3de7-35c7-8899-74a3e5787f35 | -4.54903 | -50.45853 | 2025-08-21 04:38:00 | NOAA-20 | NOVO REPARTIMENTO | PARÁ | Brasil | 1505064 | 15 | 33 | nan | nan | nan | Amazônia | 0.8 |
| 8ca3bc1b-fd84-3d43-bdd2-04d776e97057 | -6.5601 | -42.99592 | 2025-08-21 04:38:00 | NOAA-20 | BARÃO DE GRAJAÚ | MARANHÃO | Brasil | 2101509 | 21 | 33 | nan | nan | nan | Cerrado | 1.6 |
| 63710597-162d-33e6-8ba2-3a0a9736338d | -5.96989 | -44.14389 | 2025-08-21 04:38:00 | NOAA-20 | COLINAS | MARANHÃO | Brasil | 2103505 | 21 | 33 | nan | nan | nan | Cerrado | 2.1 |
| 917d78be-0959-3b00-8ed9-e0f6669d5c00 | -6.29675 | -43.87803 | 2025-08-21 04:38:00 | NOAA-20 | PARAIBANO | MARANHÃO | Brasil | 2107704 | 21 | 33 | nan | nan | nan | Cerrado | 1.4 |
| 2e577ce0-52f7-32c9-8ab4-3f53b95ea1ed | -3.74062 | -48.93106 | 2025-08-21 04:38:00 | NOAA-20 | GOIANÉSIA DO PARÁ | PARÁ | Brasil | 1503093 | 15 | 33 | nan | nan | nan | Amazônia | 1.6 |
| 796702ac-3d95-38eb-a9d9-8b15d2804a2a | -8.83487 | -52.03414 | 2025-08-21 04:38:00 | NOAA-20 | SÃO FÉLIX DO XINGU | PARÁ | Brasil | 1507300 | 15 | 33 | nan | nan | nan | Amazônia | 2.6 |
| 32e52f36-b513-371a-a129-5045b0a2fdf2 | -6.74181 | -43.93429 | 2025-08-21 04:38:00 | NOAA-20 | NOVA IORQUE | MARANHÃO | Brasil | 2107308 | 21 | 33 | nan | nan | nan | Cerrado | 1.2 |
| 6dbf7723-922d-3236-8bd7-96e49fb25146 | -6.26469 | -43.71448 | 2025-08-21 04:38:00 | NOAA-20 | PASSAGEM FRANCA | MARANHÃO | Brasil | 2107902 | 21 | 33 | nan | nan | nan | Cerrado | 1.3 |
| 7401937e-c582-385f-bc53-7c9657f1260b | -7.01957 | -44.60987 | 2025-08-21 04:38:00 | NOAA-20 | BENEDITO LEITE | MARANHÃO | Brasil | 2101806 | 21 | 33 | nan | nan | nan | Cerrado | 17.8 |
| 0f7be36b-e73c-320c-8255-5127bf45f439 | -6.56429 | -44.48573 | 2025-08-21 04:38:00 | NOAA-20 | SUCUPIRA DO NORTE | MARANHÃO | Brasil | 2111904 | 21 | 33 | nan | nan | nan | Cerrado | 1.3 |
| 9a95e937-fb78-3f9c-b58b-dc43bb1e6634 | -7.56847 | -44.40334 | 2025-08-21 04:38:00 | NOAA-20 | URUÇUÍ | PIAUÍ | Brasil | 2211209 | 22 | 33 | nan | nan | nan | Cerrado | 1.5 |
| 1747dd59-1a36-315e-a0bb-88dad6ef1947 | -7.02099 | -44.62834 | 2025-08-21 04:38:00 | NOAA-20 | BENEDITO LEITE | MARANHÃO | Brasil | 2101806 | 21 | 33 | nan | nan | nan | Cerrado | 124.3 |
| b968521e-e860-38d0-9391-49183e83cbb8 | -8.14023 | -47.3466 | 2025-08-21 04:38:00 | NOAA-20 | GOIATINS | TOCANTINS | Brasil | 1709005 | 17 | 33 | nan | nan | nan | Cerrado | 2.0 |
| 131c95b2-a5c8-32a8-af22-8b1a98db54ab | -7.2757 | -43.67706 | 2025-08-21 04:38:00 | NOAA-20 | CANAVIEIRA | PIAUÍ | Brasil | 2202251 | 22 | 33 | nan | nan | nan | Cerrado | 1.1 |
| fefb110d-10bd-3830-9247-5aecf293b7e3 | -6.2873 | -43.88405 | 2025-08-21 04:38:00 | NOAA-20 | PASSAGEM FRANCA | MARANHÃO | Brasil | 2107902 | 21 | 33 | nan | nan | nan | Cerrado | 1.2 |
| 977d9ef1-a848-3d8e-91dc-d51ae541a474 | -7.60835 | -44.38983 | 2025-08-21 04:38:00 | NOAA-20 | URUÇUÍ | PIAUÍ | Brasil | 2211209 | 22 | 33 | nan | nan | nan | Cerrado | 1.3 |
| 7a927b24-5a8c-3bbf-8ed4-3b5e2e89fb58 | -6.7462 | -43.93837 | 2025-08-21 04:38:00 | NOAA-20 | NOVA IORQUE | MARANHÃO | Brasil | 2107308 | 21 | 33 | nan | nan | nan | Cerrado | 1.5 |
| f7b1eb44-b076-3c57-ad04-7a32092e4146 | -4.17065 | -42.03083 | 2025-08-21 04:38:00 | NOAA-20 | BATALHA | PIAUÍ | Brasil | 2201507 | 22 | 33 | nan | nan | nan | Caatinga | 9.1 |


[Clique aqui para ver as próximas entradas](README42.md)
