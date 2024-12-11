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

## Dados Diários - Página 31

| ID | Latitude | Longitude | Data/Hora GMT | Satélite | Município | Estado | País | Município ID | Estado ID | País ID | Dias sem Chuva | Precipitação | Risco de Fogo | Bioma | FRP |
|----|----------|-----------|---------------|----------|-----------|--------|------|--------------|-----------|---------|----------------|--------------|----------------|-------|-----|
| 81da3d4e-b4db-309c-b4cb-9ffcde6dab13 | -6.12263 | -42.53679 | 2024-12-11 13:01:00 | TERRA_M-T | JARDIM DO MULATO | PIAUÍ | Brasil | 2205250 | 22 | 33 | nan | nan | nan | Caatinga | 150.1 |
| f53869ff-9a59-3cb5-97ef-8d78b5f6afbc | -11.2145 | -53.8197 | 2024-12-11 13:01:00 | TERRA_M-T | MARCELÂNDIA | MATO GROSSO | Brasil | 5105580 | 51 | 33 | nan | nan | nan | Amazônia | 30.1 |
| 7e5aa7d8-bfe3-34a0-8019-e9987466b45b | -11.0634 | -45.37886 | 2024-12-11 13:01:00 | TERRA_M-T | FORMOSA DO RIO PRETO | BAHIA | Brasil | 2911105 | 29 | 33 | nan | nan | nan | Cerrado | 182.4 |
| 0795d480-acce-35ac-93ac-2286f61bf9b2 | -11.77846 | -54.24439 | 2024-12-11 13:01:00 | TERRA_M-T | UNIÃO DO SUL | MATO GROSSO | Brasil | 5108303 | 51 | 33 | nan | nan | nan | Amazônia | 5.0 |
| 4f28e55c-ee13-3c90-8964-be3130bf5ad1 | -18.71081 | -51.78894 | 2024-12-11 13:03:00 | TERRA_M-T | ITARUMÃ | GOIÁS | Brasil | 5211305 | 52 | 33 | nan | nan | nan | Cerrado | 24.5 |
| 32718de1-5c81-383d-9b5c-9516afb7919e | -18.81255 | -53.4596 | 2024-12-11 13:03:00 | TERRA_M-T | FIGUEIRÃO | MATO GROSSO DO SUL | Brasil | 5003900 | 50 | 33 | nan | nan | nan | Cerrado | 9.2 |
| 32fd6968-eb76-3fa5-bf9d-cf48f7d5677c | -18.0675 | -49.74838 | 2024-12-11 13:03:00 | TERRA_M-T | GOIATUBA | GOIÁS | Brasil | 5209101 | 52 | 33 | nan | nan | nan | Cerrado | 17.4 |
| efee84fc-d099-3200-996d-d16ff3355df3 | -17.73906 | -53.43906 | 2024-12-11 13:03:00 | TERRA_M-T | ALTO TAQUARI | MATO GROSSO | Brasil | 5100607 | 51 | 33 | nan | nan | nan | Cerrado | 10.7 |
| 40b039e8-3a42-31c5-984d-c5f2e39ae74f | -12.43928 | -54.21646 | 2024-12-11 13:03:00 | TERRA_M-T | NOVA UBIRATÃ | MATO GROSSO | Brasil | 5106240 | 51 | 33 | nan | nan | nan | Amazônia | 4.1 |
| 6d875e25-48c1-37c0-ae6c-3b4b80fe4fa0 | -17.61335 | -53.07836 | 2024-12-11 13:03:00 | TERRA_M-T | MINEIROS | GOIÁS | Brasil | 5213103 | 52 | 33 | nan | nan | nan | Cerrado | 12.2 |
| fed2d3cb-fb28-3cd6-8daf-c45c5ce56a60 | -18.8093 | -49.45192 | 2024-12-11 13:03:00 | TERRA_M-T | ITUIUTABA | MINAS GERAIS | Brasil | 3134202 | 31 | 33 | nan | nan | nan | Cerrado | 14.4 |
| 252f08ab-cef3-3ce2-b3e6-bd05a7d88166 | -17.4852 | -52.51892 | 2024-12-11 13:03:00 | TERRA_M-T | MINEIROS | GOIÁS | Brasil | 5213103 | 52 | 33 | nan | nan | nan | Cerrado | 8.3 |
| d8e30498-fe44-3f6d-bf26-cd6e4b2b4a6b | -18.4735 | -53.24376 | 2024-12-11 13:03:00 | TERRA_M-T | COSTA RICA | MATO GROSSO DO SUL | Brasil | 5003256 | 50 | 33 | nan | nan | nan | Cerrado | 13.8 |
| efc955ba-8377-3385-90e7-02e8c642fb2e | -15.57161 | -54.80679 | 2024-12-11 13:03:00 | TERRA_M-T | DOM AQUINO | MATO GROSSO | Brasil | 5103601 | 51 | 33 | nan | nan | nan | Cerrado | 3.8 |
| e243829d-94bf-3010-9f2e-3e17970330a0 | -17.23797 | -54.45178 | 2024-12-11 13:03:00 | TERRA_M-T | ITIQUIRA | MATO GROSSO | Brasil | 5104609 | 51 | 33 | nan | nan | nan | Cerrado | 10.0 |
| 4bd3efd1-c80e-3ffd-be3c-1ea191f23f51 | -18.29452 | -53.27687 | 2024-12-11 13:03:00 | TERRA_M-T | COSTA RICA | MATO GROSSO DO SUL | Brasil | 5003256 | 50 | 33 | nan | nan | nan | Cerrado | 9.9 |
| 5403761f-fb94-34ed-ad09-3b4c64f35ee8 | -17.68601 | -50.06499 | 2024-12-11 13:03:00 | TERRA_M-T | EDÉIA | GOIÁS | Brasil | 5207402 | 52 | 33 | nan | nan | nan | Cerrado | 11.3 |
| 10dfc949-2fbf-3923-b788-41d48481c2dd | -15.69546 | -54.58935 | 2024-12-11 13:03:00 | TERRA_M-T | POXORÉU | MATO GROSSO | Brasil | 5107008 | 51 | 33 | nan | nan | nan | Cerrado | 21.4 |
| c884f3b6-c50b-33d9-ad4d-bed7ba1d435f | -19.21325 | -48.63754 | 2024-12-11 13:03:00 | TERRA_M-T | PRATA | MINAS GERAIS | Brasil | 3152808 | 31 | 33 | nan | nan | nan | Cerrado | 10.2 |
| b9a4586c-9bfc-34d0-8121-36c427f902f7 | -17.53467 | -52.28873 | 2024-12-11 13:03:00 | TERRA_M-T | PEROLÂNDIA | GOIÁS | Brasil | 5216452 | 52 | 33 | nan | nan | nan | Cerrado | 13.2 |
| 8f0d15cd-6145-35af-bdcb-6085d97871a1 | -12.16542 | -55.0009 | 2024-12-11 13:03:00 | TERRA_M-T | SANTA CARMEM | MATO GROSSO | Brasil | 5107248 | 51 | 33 | nan | nan | nan | Amazônia | 5.9 |
| 0c2159ce-baa9-3a89-8cf8-57c4f923ae9d | -18.29585 | -53.26694 | 2024-12-11 13:03:00 | TERRA_M-T | COSTA RICA | MATO GROSSO DO SUL | Brasil | 5003256 | 50 | 33 | nan | nan | nan | Cerrado | 9.5 |
| 29b2c424-3faa-3292-8f16-13462654a75e | -17.05056 | -53.55905 | 2024-12-11 13:03:00 | TERRA_M-T | ALTO GARÇAS | MATO GROSSO | Brasil | 5100409 | 51 | 33 | nan | nan | nan | Cerrado | 7.2 |
| 7e6e7cb6-f9e9-3ffa-904e-aa6f43daf6ed | -17.79264 | -52.97377 | 2024-12-11 13:03:00 | TERRA_M-T | MINEIROS | GOIÁS | Brasil | 5213103 | 52 | 33 | nan | nan | nan | Cerrado | 12.7 |
| 304b6df3-959c-3262-b97c-bec6f611927b | -17.50304 | -53.00563 | 2024-12-11 13:03:00 | TERRA_M-T | MINEIROS | GOIÁS | Brasil | 5213103 | 52 | 33 | nan | nan | nan | Cerrado | 8.0 |
| 53d48fab-0069-3ec1-8a76-278914026ba0 | -16.65622 | -53.81157 | 2024-12-11 13:03:00 | TERRA_M-T | GUIRATINGA | MATO GROSSO | Brasil | 5104203 | 51 | 33 | nan | nan | nan | Cerrado | 4.4 |
| 087a527e-0bc5-31ff-a43f-ad7b36d3699f | -12.87221 | -54.2133 | 2024-12-11 13:03:00 | TERRA_M-T | PARANATINGA | MATO GROSSO | Brasil | 5106307 | 51 | 33 | nan | nan | nan | Amazônia | 6.4 |
| b9d55b5f-f9f7-3881-b9ef-e1d40b3398f5 | -17.24866 | -54.56622 | 2024-12-11 13:03:00 | TERRA_M-T | ITIQUIRA | MATO GROSSO | Brasil | 5104609 | 51 | 33 | nan | nan | nan | Cerrado | 7.8 |
| 392b2d9e-03a4-382a-92de-2eb910a2c92f | -15.7336 | -46.11164 | 2024-12-11 13:03:00 | TERRA_M-T | ARINOS | MINAS GERAIS | Brasil | 3104502 | 31 | 33 | nan | nan | nan | Cerrado | 32.1 |
| 3eb501bb-6aff-3adc-9ec2-071c7d0159a5 | -17.38036 | -55.93322 | 2024-12-11 13:03:00 | TERRA_M-T | CORUMBÁ | MATO GROSSO DO SUL | Brasil | 5003207 | 50 | 33 | nan | nan | nan | Pantanal | 8.9 |
| 956c8e69-b2f1-3213-a803-19dae7df9a63 | -17.5375 | -52.26721 | 2024-12-11 13:03:00 | TERRA_M-T | PEROLÂNDIA | GOIÁS | Brasil | 5216452 | 52 | 33 | nan | nan | nan | Cerrado | 7.9 |
| 6b7d6e99-2bff-3fa6-be8f-4292e78ab031 | -18.89884 | -53.1648 | 2024-12-11 13:03:00 | TERRA_M-T | COSTA RICA | MATO GROSSO DO SUL | Brasil | 5003256 | 50 | 33 | nan | nan | nan | Cerrado | 10.5 |
| ad38d34d-0b67-3328-a158-fbe2b942e866 | -18.25186 | -52.64394 | 2024-12-11 13:03:00 | TERRA_M-T | CHAPADÃO DO CÉU | GOIÁS | Brasil | 5205471 | 52 | 33 | nan | nan | nan | Cerrado | 12.8 |
| a7c23bed-21ce-322e-bc33-36512f492eae | -12.56623 | -57.77051 | 2024-12-11 13:03:00 | TERRA_M-T | BRASNORTE | MATO GROSSO | Brasil | 5101902 | 51 | 33 | nan | nan | nan | Amazônia | 7.3 |
| bb369675-f567-3225-8fb1-822565405594 | -17.4017 | -53.68365 | 2024-12-11 13:03:00 | TERRA_M-T | ALTO ARAGUAIA | MATO GROSSO | Brasil | 5100300 | 51 | 33 | nan | nan | nan | Cerrado | 7.2 |
| 50ba06f9-fb4f-38c4-a442-8952eb2bda4e | -17.06846 | -52.19229 | 2024-12-11 13:03:00 | TERRA_M-T | CAIAPÔNIA | GOIÁS | Brasil | 5204409 | 52 | 33 | nan | nan | nan | Cerrado | 8.6 |
| 1711c97d-bd2f-3026-b31e-e37c631dd333 | -17.96303 | -49.85695 | 2024-12-11 13:03:00 | TERRA_M-T | GOIATUBA | GOIÁS | Brasil | 5209101 | 52 | 33 | nan | nan | nan | Cerrado | 13.7 |
| 63214479-b838-3f70-a60f-22e5f65d2c41 | -18.49681 | -55.12568 | 2024-12-11 13:03:00 | TERRA_M-T | RIO VERDE DE MATO GROSSO | MATO GROSSO DO SUL | Brasil | 5007406 | 50 | 33 | nan | nan | nan | Pantanal | 12.2 |
| 4854ac36-3d4b-3bc8-9cb8-8f36e1a87cda | -15.69413 | -54.59848 | 2024-12-11 13:03:00 | TERRA_M-T | POXORÉU | MATO GROSSO | Brasil | 5107008 | 51 | 33 | nan | nan | nan | Cerrado | 8.0 |
| cf1e074e-30b4-38eb-a6c1-57c705ec943a | -17.53572 | -53.04079 | 2024-12-11 13:03:00 | TERRA_M-T | MINEIROS | GOIÁS | Brasil | 5213103 | 52 | 33 | nan | nan | nan | Cerrado | 12.6 |
| 2798cacc-eb87-3af9-a379-05106fa91116 | -19.43377 | -47.76534 | 2024-12-11 13:03:00 | TERRA_M-T | NOVA PONTE | MINAS GERAIS | Brasil | 3145000 | 31 | 33 | nan | nan | nan | Cerrado | 17.3 |
| 18676b66-416f-3ae6-82d6-5f615fc26760 | -18.59197 | -53.18512 | 2024-12-11 13:03:00 | TERRA_M-T | COSTA RICA | MATO GROSSO DO SUL | Brasil | 5003256 | 50 | 33 | nan | nan | nan | Cerrado | 10.5 |
| 8328716f-a113-3af4-ac51-ca41ba14810b | 2.7627 | -60.6378 | 2024-12-11 13:10:00 | GOES-16 | CANTÁ | RORAIMA | Brasil | 1400175 | 14 | 33 | nan | nan | nan | Amazônia | 68.1 |
| a3252d4c-8f39-38a7-a29c-c1cbfbcd18fd | -6.118 | -42.5323 | 2024-12-11 13:10:00 | GOES-16 | JARDIM DO MULATO | PIAUÍ | Brasil | 2205250 | 22 | 33 | nan | nan | nan | Caatinga | 120.9 |
| af58d9ad-04bb-3b31-81f2-ed50b1ada06f | -6.118 | -42.5323 | 2024-12-11 13:20:00 | GOES-16 | JARDIM DO MULATO | PIAUÍ | Brasil | 2205250 | 22 | 33 | nan | nan | nan | Caatinga | 115.8 |
| 80ba7ce5-d731-3e98-a519-54ac85cb7390 | -6.118 | -42.5323 | 2024-12-11 13:30:00 | GOES-16 | JARDIM DO MULATO | PIAUÍ | Brasil | 2205250 | 22 | 33 | nan | nan | nan | Caatinga | 96.6 |
| a43917fb-7cf8-376d-bd2a-04b111a9b54b | -6.1368 | -42.5307 | 2024-12-11 13:30:00 | GOES-16 | JARDIM DO MULATO | PIAUÍ | Brasil | 2205250 | 22 | 33 | nan | nan | nan | Caatinga | 115.0 |
| 232dc7e2-450a-35eb-8677-bf5e73036b45 | -11.8075 | -43.8026 | 2024-12-11 13:40:00 | GOES-16 | WANDERLEY | BAHIA | Brasil | 2933455 | 29 | 33 | nan | nan | nan | Cerrado | 80.4 |
| c23ef5d1-b4cd-36c5-9921-461462a64805 | -6.1366 | -42.5544 | 2024-12-11 13:50:00 | GOES-16 | JARDIM DO MULATO | PIAUÍ | Brasil | 2205250 | 22 | 33 | nan | nan | nan | Caatinga | 97.4 |
| d8566b30-7d78-3b31-a3bf-3146ee0d6d50 | -6.1368 | -42.5307 | 2024-12-11 13:50:00 | GOES-16 | JARDIM DO MULATO | PIAUÍ | Brasil | 2205250 | 22 | 33 | nan | nan | nan | Caatinga | 108.3 |
| 40df3df5-5abc-33dd-99ba-2de2cd19abec | -6.118 | -42.5323 | 2024-12-11 13:50:00 | GOES-16 | JARDIM DO MULATO | PIAUÍ | Brasil | 2205250 | 22 | 33 | nan | nan | nan | Caatinga | 109.3 |
| dd28d1f2-7b6c-3eb1-813a-263aa8ec8d71 | -6.1368 | -42.5307 | 2024-12-11 14:00:00 | GOES-16 | JARDIM DO MULATO | PIAUÍ | Brasil | 2205250 | 22 | 33 | nan | nan | nan | Caatinga | 99.2 |
| c6972813-c81e-3cdb-a135-ac8e519ec276 | -3.89 | -42.56 | 2024-12-11 14:00:00 | MSG-03 | CAMPO LARGO DO PIAUÍ | PIAUÍ | Brasil | 2202174 | 22 | 33 | nan | nan | nan | Caatinga | nan |
| 219d74d7-029f-306c-ac57-8f12e0b86f30 | -3.89 | -42.52 | 2024-12-11 14:00:00 | MSG-03 | CAMPO LARGO DO PIAUÍ | PIAUÍ | Brasil | 2202174 | 22 | 33 | nan | nan | nan | Caatinga | nan |
| 945dddc9-90ed-3838-a68a-87ef19c96438 | -6.1368 | -42.5307 | 2024-12-11 14:10:00 | GOES-16 | JARDIM DO MULATO | PIAUÍ | Brasil | 2205250 | 22 | 33 | nan | nan | nan | Caatinga | 99.5 |
| b5040937-57e4-3311-8cd4-59e1aa567787 | -18.4993 | -55.125 | 2024-12-11 14:20:00 | GOES-16 | RIO VERDE DE MATO GROSSO | MATO GROSSO DO SUL | Brasil | 5007406 | 50 | 33 | nan | nan | nan | Pantanal | 83.0 |
| 6d7a173d-3538-33b4-996e-0bd3b47af234 | -6.118 | -42.5323 | 2024-12-11 14:30:00 | GOES-16 | JARDIM DO MULATO | PIAUÍ | Brasil | 2205250 | 22 | 33 | nan | nan | nan | Caatinga | 116.5 |
| d6f2c590-a149-358a-b2c9-02612620547d | -6.1366 | -42.5544 | 2024-12-11 14:30:00 | GOES-16 | JARDIM DO MULATO | PIAUÍ | Brasil | 2205250 | 22 | 33 | nan | nan | nan | Caatinga | 122.9 |
| 539f42bc-c6b1-3d8e-bdc8-3a673b2e227f | -6.1368 | -42.5307 | 2024-12-11 14:30:00 | GOES-16 | JARDIM DO MULATO | PIAUÍ | Brasil | 2205250 | 22 | 33 | nan | nan | nan | Caatinga | 145.8 |
| c6c99bcc-fe93-33d3-bd0c-808accbaabd3 | -6.9161 | -43.4952 | 2024-12-11 14:30:00 | GOES-16 | JERUMENHA | PIAUÍ | Brasil | 2205300 | 22 | 33 | nan | nan | nan | Cerrado | 58.7 |


