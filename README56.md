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

## Dados Diários - Página 56

| ID | Latitude | Longitude | Data/Hora GMT | Satélite | Município | Estado | País | Município ID | Estado ID | País ID | Dias sem Chuva | Precipitação | Risco de Fogo | Bioma | FRP |
|----|----------|-----------|---------------|----------|-----------|--------|------|--------------|-----------|---------|----------------|--------------|----------------|-------|-----|
| efd1437f-0ed7-3a75-8970-552d7121d2b8 | -19.52 | -56.76 | 2024-11-01 12:03:36 | MSG-03 | CORUMBÁ | MATO GROSSO DO SUL | Brasil | 5003207 | 50 | 33 | nan | nan | nan | Pantanal | nan |
| 593cc9be-f15f-3a5f-a167-6049ffdbaa3f | -1.4244 | -52.2118 | 2024-11-01 12:05:14 | GOES-16 | ALMEIRIM | PARÁ | Brasil | 1500503 | 15 | 33 | nan | nan | nan | Amazônia | 67.5 |
| fe015ec7-ea40-332a-97e2-403b53dabffa | -17.6467 | -57.5051 | 2024-11-01 12:06:45 | GOES-16 | POCONÉ | MATO GROSSO | Brasil | 5106505 | 51 | 33 | nan | nan | nan | Pantanal | 132.5 |
| 5b70c1a3-1e3c-39e4-870e-75e72e0e9b8e | -17.6664 | -57.5028 | 2024-11-01 12:06:46 | GOES-16 | POCONÉ | MATO GROSSO | Brasil | 5106505 | 51 | 33 | nan | nan | nan | Pantanal | 220.8 |
| e476e18f-cca6-3f5d-ab67-8442dc91dfc1 | -1.4244 | -52.2118 | 2024-11-01 12:15:14 | GOES-16 | ALMEIRIM | PARÁ | Brasil | 1500503 | 15 | 33 | nan | nan | nan | Amazônia | 72.0 |
| 62c36bc1-4257-388c-8b55-4c261def00ad | -1.4244 | -52.1913 | 2024-11-01 12:15:14 | GOES-16 | ALMEIRIM | PARÁ | Brasil | 1500503 | 15 | 33 | nan | nan | nan | Amazônia | 68.9 |
| 9c69e5a3-3849-3ce0-b7f6-33a652697946 | -17.6467 | -57.5051 | 2024-11-01 12:16:45 | GOES-16 | POCONÉ | MATO GROSSO | Brasil | 5106505 | 51 | 33 | nan | nan | nan | Pantanal | 138.7 |
| dee7f42b-658f-3a87-afab-4e4e78a060a7 | -17.6664 | -57.5028 | 2024-11-01 12:16:46 | GOES-16 | POCONÉ | MATO GROSSO | Brasil | 5106505 | 51 | 33 | nan | nan | nan | Pantanal | 245.5 |
| d855a562-fc96-391d-b46a-07648463a04a | -17.6861 | -57.5004 | 2024-11-01 12:16:46 | GOES-16 | POCONÉ | MATO GROSSO | Brasil | 5106505 | 51 | 33 | nan | nan | nan | Pantanal | 130.0 |
| f2a7439e-a497-312e-a099-8a359653f5e5 | -1.4244 | -52.2118 | 2024-11-01 12:25:14 | GOES-16 | ALMEIRIM | PARÁ | Brasil | 1500503 | 15 | 33 | nan | nan | nan | Amazônia | 77.9 |
| f4ec1d7f-ba1a-3a36-b217-6a06ff4fa9bf | -1.4244 | -52.1913 | 2024-11-01 12:25:14 | GOES-16 | ALMEIRIM | PARÁ | Brasil | 1500503 | 15 | 33 | nan | nan | nan | Amazônia | 66.3 |
| a7515f39-c09e-304b-9fe8-313b032781f3 | -2.2931 | -50.6668 | 2024-11-01 12:25:19 | GOES-16 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 167.7 |
| f23025b7-bc40-324f-ae86-596afcb3c806 | -3.3889 | -41.6441 | 2024-11-01 12:25:25 | GOES-16 | COCAL | PIAUÍ | Brasil | 2202703 | 22 | 33 | nan | nan | nan | Caatinga | 90.8 |
| 0a94eb61-f608-361b-9aed-34c7ab325f3d | -17.6467 | -57.5051 | 2024-11-01 12:26:45 | GOES-16 | POCONÉ | MATO GROSSO | Brasil | 5106505 | 51 | 33 | nan | nan | nan | Pantanal | 141.9 |
| 2a636bcc-d7a7-30a2-a4c3-18ee8fa4f7b0 | -17.6664 | -57.5028 | 2024-11-01 12:26:46 | GOES-16 | POCONÉ | MATO GROSSO | Brasil | 5106505 | 51 | 33 | nan | nan | nan | Pantanal | 233.5 |
| 7823dd3a-bde9-3230-9bd8-7b0330b9e769 | -1.63987 | -47.25245 | 2024-11-01 12:34:00 | TERRA_M-T | CAPITÃO POÇO | PARÁ | Brasil | 1502301 | 15 | 33 | nan | nan | nan | Amazônia | 16.3 |
| a566cf7f-2321-367e-b5a7-133fe4d147d7 | -3.2328 | -44.62591 | 2024-11-01 12:34:00 | TERRA_M-T | ANAJATUBA | MARANHÃO | Brasil | 2100709 | 21 | 33 | nan | nan | nan | Amazônia | 16.1 |
| 3a41d8fb-eba0-36dd-9919-71d7b7a3b353 | -2.95375 | -44.89153 | 2024-11-01 12:34:00 | TERRA_M-T | SÃO JOÃO BATISTA | MARANHÃO | Brasil | 2111003 | 21 | 33 | nan | nan | nan | Amazônia | 20.5 |
| ff30aba2-3b0d-39eb-a82e-26b9e9a84b95 | -2.95248 | -44.90032 | 2024-11-01 12:34:00 | TERRA_M-T | SÃO JOÃO BATISTA | MARANHÃO | Brasil | 2111003 | 21 | 33 | nan | nan | nan | Amazônia | 42.8 |
| eab0bb07-7042-37c7-baa4-f67210335614 | -2.94363 | -44.89908 | 2024-11-01 12:34:00 | TERRA_M-T | SÃO JOÃO BATISTA | MARANHÃO | Brasil | 2111003 | 21 | 33 | nan | nan | nan | Amazônia | 11.5 |
| 341399e1-79c7-312c-ad23-b38917060905 | -2.92816 | -46.77768 | 2024-11-01 12:34:00 | TERRA_M-T | PARAGOMINAS | PARÁ | Brasil | 1505502 | 15 | 33 | nan | nan | nan | Amazônia | 33.2 |
| e82d05b0-2576-3ea1-ae3e-c2a576bc90a6 | -2.80924 | -44.36486 | 2024-11-01 12:34:00 | TERRA_M-T | BACABEIRA | MARANHÃO | Brasil | 2101251 | 21 | 33 | nan | nan | nan | Amazônia | 9.7 |
| c286d3aa-c92d-3f95-9fff-07417a88e80f | -2.67691 | -46.73354 | 2024-11-01 12:34:00 | TERRA_M-T | PARAGOMINAS | PARÁ | Brasil | 1505502 | 15 | 33 | nan | nan | nan | Amazônia | 22.7 |
| dd216843-2da0-3063-86ac-c1864fad29d5 | -2.66906 | -45.27094 | 2024-11-01 12:34:00 | TERRA_M-T | PRESIDENTE SARNEY | MARANHÃO | Brasil | 2109270 | 21 | 33 | nan | nan | nan | Amazônia | 11.8 |
| b09743ec-721c-3ab5-86d8-d773ac86ceb2 | -2.41208 | -46.45988 | 2024-11-01 12:34:00 | TERRA_M-T | NOVA ESPERANÇA DO PIRIÁ | PARÁ | Brasil | 1504950 | 15 | 33 | nan | nan | nan | Amazônia | 10.7 |
| 905ceabc-df1c-3eb5-a9a3-9e2589052a93 | -2.41067 | -46.46942 | 2024-11-01 12:34:00 | TERRA_M-T | NOVA ESPERANÇA DO PIRIÁ | PARÁ | Brasil | 1504950 | 15 | 33 | nan | nan | nan | Amazônia | 15.1 |
| 1142b240-ca86-3d01-b8ea-203c2fd0bb95 | -2.36842 | -44.92477 | 2024-11-01 12:34:00 | TERRA_M-T | PINHEIRO | MARANHÃO | Brasil | 2108603 | 21 | 33 | nan | nan | nan | Amazônia | 8.6 |
| 475f76f5-98ac-38de-98a1-1b7a940aa804 | -2.36155 | -46.49578 | 2024-11-01 12:34:00 | TERRA_M-T | CACHOEIRA DO PIRIÁ | PARÁ | Brasil | 1501956 | 15 | 33 | nan | nan | nan | Amazônia | 7.4 |
| 3f7fa3c5-c62e-3861-8d82-579910f5c378 | -2.34883 | -48.6785 | 2024-11-01 12:34:00 | TERRA_M-T | ACARÁ | PARÁ | Brasil | 1500206 | 15 | 33 | nan | nan | nan | Amazônia | 18.6 |
| 442cba8c-767a-3ec5-bd2b-a53ea390b2b1 | -2.33198 | -46.12787 | 2024-11-01 12:34:00 | TERRA_M-T | CENTRO DO GUILHERME | MARANHÃO | Brasil | 2103158 | 21 | 33 | nan | nan | nan | Amazônia | 14.2 |
| 3793a57e-a6da-3752-831d-4b215cb5e72b | -2.32032 | -47.08267 | 2024-11-01 12:34:00 | TERRA_M-T | GARRAFÃO DO NORTE | PARÁ | Brasil | 1503077 | 15 | 33 | nan | nan | nan | Amazônia | 9.1 |
| f4f45501-9f7f-3638-b762-ff7ad3ad5209 | -2.31259 | -46.50846 | 2024-11-01 12:34:00 | TERRA_M-T | CACHOEIRA DO PIRIÁ | PARÁ | Brasil | 1501956 | 15 | 33 | nan | nan | nan | Amazônia | 7.5 |
| 21f3e725-22d3-38b1-a153-8c95d3ce8710 | -2.30663 | -46.23891 | 2024-11-01 12:34:00 | TERRA_M-T | CENTRO NOVO DO MARANHÃO | MARANHÃO | Brasil | 2103174 | 21 | 33 | nan | nan | nan | Amazônia | 6.7 |
| e9287792-cdbb-33f0-897c-8501dc64868f | -2.30402 | -46.82691 | 2024-11-01 12:34:00 | TERRA_M-T | NOVA ESPERANÇA DO PIRIÁ | PARÁ | Brasil | 1504950 | 15 | 33 | nan | nan | nan | Amazônia | 8.3 |
| 4cb34bd1-275b-321d-94dc-ca2f5a139805 | -2.26969 | -46.67088 | 2024-11-01 12:34:00 | TERRA_M-T | NOVA ESPERANÇA DO PIRIÁ | PARÁ | Brasil | 1504950 | 15 | 33 | nan | nan | nan | Amazônia | 10.6 |
| 6aee9823-9f67-3685-b813-42843bb9dff4 | -2.26418 | -46.66347 | 2024-11-01 12:34:00 | TERRA_M-T | NOVA ESPERANÇA DO PIRIÁ | PARÁ | Brasil | 1504950 | 15 | 33 | nan | nan | nan | Amazônia | 16.1 |
| dd7fc170-ddaf-3bd3-a32b-e80f95b3d867 | -2.25487 | -46.66217 | 2024-11-01 12:34:00 | TERRA_M-T | NOVA ESPERANÇA DO PIRIÁ | PARÁ | Brasil | 1504950 | 15 | 33 | nan | nan | nan | Amazônia | 12.7 |
| 414b1ca7-b561-3741-b7ac-db7d88ef1ad6 | -2.17993 | -48.72132 | 2024-11-01 12:34:00 | TERRA_M-T | MOJU | PARÁ | Brasil | 1504703 | 15 | 33 | nan | nan | nan | Amazônia | 30.3 |
| f8240916-b010-3347-8e2b-06a55efc7283 | -1.97217 | -45.62183 | 2024-11-01 12:34:00 | TERRA_M-T | TURIAÇU | MARANHÃO | Brasil | 2112407 | 21 | 33 | nan | nan | nan | Amazônia | 11.0 |
| 5f391d66-cd1c-37f4-ba11-30d6ba6ecb13 | -1.96585 | -45.60252 | 2024-11-01 12:34:00 | TERRA_M-T | TURIAÇU | MARANHÃO | Brasil | 2112407 | 21 | 33 | nan | nan | nan | Amazônia | 15.6 |
| e8b3bad0-b62c-3125-99c4-79923b30d4c1 | -3.54352 | -42.13771 | 2024-11-01 12:34:00 | TERRA_M-T | JOAQUIM PIRES | PIAUÍ | Brasil | 2205409 | 22 | 33 | nan | nan | nan | Caatinga | 10.9 |
| d23911e7-ffce-3570-b98d-003639135fa7 | -3.39961 | -41.64033 | 2024-11-01 12:34:00 | TERRA_M-T | COCAL | PIAUÍ | Brasil | 2202703 | 22 | 33 | nan | nan | nan | Caatinga | 114.2 |
| 2961c66a-42d7-3cdc-80fe-b31e46a41bf7 | -3.398 | -41.65179 | 2024-11-01 12:34:00 | TERRA_M-T | COCAL | PIAUÍ | Brasil | 2202703 | 22 | 33 | nan | nan | nan | Caatinga | 12.3 |
| af57eb2f-9275-3a0e-8941-768499b2dc3b | -3.39119 | -41.62736 | 2024-11-01 12:34:00 | TERRA_M-T | COCAL | PIAUÍ | Brasil | 2202703 | 22 | 33 | nan | nan | nan | Caatinga | 38.7 |
| cc287432-192d-34fd-8cb1-6ce40ffd4611 | -3.36631 | -41.65913 | 2024-11-01 12:34:00 | TERRA_M-T | COCAL | PIAUÍ | Brasil | 2202703 | 22 | 33 | nan | nan | nan | Caatinga | 8.8 |
| 6eeb40ff-dcd8-31f6-94ce-e6df2557b848 | -3.3164 | -42.30049 | 2024-11-01 12:34:00 | TERRA_M-T | SÃO BERNARDO | MARANHÃO | Brasil | 2110609 | 21 | 33 | nan | nan | nan | Cerrado | 69.0 |
| 54f858fe-45f9-3d33-9556-6e44409fee06 | -3.31491 | -42.31095 | 2024-11-01 12:34:00 | TERRA_M-T | SÃO BERNARDO | MARANHÃO | Brasil | 2110609 | 21 | 33 | nan | nan | nan | Cerrado | 71.7 |
| 9d54bcdf-74e5-3256-971b-370cab3a8ae5 | -3.30171 | -43.24712 | 2024-11-01 12:34:00 | TERRA_M-T | URBANO SANTOS | MARANHÃO | Brasil | 2112605 | 21 | 33 | nan | nan | nan | Cerrado | 10.3 |
| 00fd2efd-084b-3e95-9abc-93beeff8dd24 | -3.14916 | -42.3186 | 2024-11-01 12:34:00 | TERRA_M-T | SÃO BERNARDO | MARANHÃO | Brasil | 2110609 | 21 | 33 | nan | nan | nan | Cerrado | 7.1 |
| b0ae524e-1f41-3f1d-8cde-198f4fbec168 | -3.14767 | -42.32901 | 2024-11-01 12:34:00 | TERRA_M-T | SÃO BERNARDO | MARANHÃO | Brasil | 2110609 | 21 | 33 | nan | nan | nan | Cerrado | 263.1 |
| 47e23715-cc2e-3642-b680-37f9d562f222 | -3.14618 | -42.33939 | 2024-11-01 12:34:00 | TERRA_M-T | SÃO BERNARDO | MARANHÃO | Brasil | 2110609 | 21 | 33 | nan | nan | nan | Cerrado | 140.3 |
| e99334ce-1ee4-39e4-8d89-bc185036fe46 | -1.96453 | -45.61155 | 2024-11-01 12:34:00 | TERRA_M-T | TURIAÇU | MARANHÃO | Brasil | 2112407 | 21 | 33 | nan | nan | nan | Amazônia | 26.5 |
| 3b5398fa-efd7-33aa-8bda-fb6c6b5aa7b5 | -1.85561 | -52.31104 | 2024-11-01 12:34:00 | TERRA_M-T | PORTO DE MOZ | PARÁ | Brasil | 1505908 | 15 | 33 | nan | nan | nan | Amazônia | 44.1 |
| 804f35f1-559a-361f-aaf8-855aab3fc667 | -1.4244 | -52.1913 | 2024-11-01 12:35:14 | GOES-16 | ALMEIRIM | PARÁ | Brasil | 1500503 | 15 | 33 | nan | nan | nan | Amazônia | 77.6 |
| 028371db-4f44-3ea0-ab04-30cd6709b925 | -1.4244 | -52.2118 | 2024-11-01 12:35:14 | GOES-16 | ALMEIRIM | PARÁ | Brasil | 1500503 | 15 | 33 | nan | nan | nan | Amazônia | 75.2 |
| 3d5b74ff-2002-3b91-9259-743966a73774 | -3.3891 | -41.6201 | 2024-11-01 12:35:25 | GOES-16 | COCAL | PIAUÍ | Brasil | 2202703 | 22 | 33 | nan | nan | nan | Caatinga | 95.1 |
| cc03887c-86be-3242-8695-03982f001dfa | -3.98711 | -49.0276 | 2024-11-01 12:36:00 | TERRA_M-T | GOIANÉSIA DO PARÁ | PARÁ | Brasil | 1503093 | 15 | 33 | nan | nan | nan | Amazônia | 19.9 |
| 828b5b3e-da30-394d-be58-fe6be901780f | -3.93565 | -48.34469 | 2024-11-01 12:36:00 | TERRA_M-T | DOM ELISEU | PARÁ | Brasil | 1502939 | 15 | 33 | nan | nan | nan | Amazônia | 12.3 |
| 24d9ec41-c77b-3e24-98c6-56739147118c | -3.90881 | -45.75042 | 2024-11-01 12:36:00 | TERRA_M-T | SANTA LUZIA | MARANHÃO | Brasil | 2110005 | 21 | 33 | nan | nan | nan | Amazônia | 7.7 |
| 36cc52b5-ffc7-3d74-8a6f-43666765b8ac | -3.90838 | -44.93189 | 2024-11-01 12:36:00 | TERRA_M-T | CONCEIÇÃO DO LAGO-AÇU | MARANHÃO | Brasil | 2103554 | 21 | 33 | nan | nan | nan | Amazônia | 9.4 |
| 33d27ff0-e86d-3d54-a9c9-b3273db82f52 | -3.90751 | -45.75935 | 2024-11-01 12:36:00 | TERRA_M-T | SANTA LUZIA | MARANHÃO | Brasil | 2110005 | 21 | 33 | nan | nan | nan | Amazônia | 8.0 |
| 3a4a2d86-ef80-3a5f-9097-93668a2e407f | -3.8681 | -47.54698 | 2024-11-01 12:36:00 | TERRA_M-T | ULIANÓPOLIS | PARÁ | Brasil | 1508126 | 15 | 33 | nan | nan | nan | Amazônia | 12.7 |
| 8fd0b708-d440-3bff-9d28-65a4ae555caf | -3.84297 | -45.94553 | 2024-11-01 12:36:00 | TERRA_M-T | ALTO ALEGRE DO PINDARÉ | MARANHÃO | Brasil | 2100477 | 21 | 33 | nan | nan | nan | Amazônia | 36.2 |
| 274c6e23-be1e-3663-9d99-d72c80c48c03 | -3.83756 | -44.14053 | 2024-11-01 12:36:00 | TERRA_M-T | COROATÁ | MARANHÃO | Brasil | 2103604 | 21 | 33 | nan | nan | nan | Cerrado | 32.1 |
| bf8b341c-35c0-3cd4-80be-081143578aca | -3.83628 | -44.14949 | 2024-11-01 12:36:00 | TERRA_M-T | PIRAPEMAS | MARANHÃO | Brasil | 2108801 | 21 | 33 | nan | nan | nan | Cerrado | 13.1 |
| 0fbcf1e3-72f0-3f33-a2a5-a3858cce5757 | -3.81674 | -44.72688 | 2024-11-01 12:36:00 | TERRA_M-T | CONCEIÇÃO DO LAGO-AÇU | MARANHÃO | Brasil | 2103554 | 21 | 33 | nan | nan | nan | Amazônia | 24.1 |
| 61dd6132-55d1-3cbd-9a28-082e7d9b6116 | -3.81179 | -45.72125 | 2024-11-01 12:36:00 | TERRA_M-T | SANTA LUZIA | MARANHÃO | Brasil | 2110005 | 21 | 33 | nan | nan | nan | Amazônia | 35.4 |
| 5094df8a-2468-3792-b375-1cda907687d2 | -3.74237 | -44.66546 | 2024-11-01 12:36:00 | TERRA_M-T | ARARI | MARANHÃO | Brasil | 2101004 | 21 | 33 | nan | nan | nan | Amazônia | 10.6 |
| e8b60973-c906-3d4e-a60c-239f8af985d1 | -3.68116 | -45.15104 | 2024-11-01 12:36:00 | TERRA_M-T | IGARAPÉ DO MEIO | MARANHÃO | Brasil | 2105153 | 21 | 33 | nan | nan | nan | Amazônia | 17.0 |
| b2ab9061-ed9c-3ef1-895b-3dd7429775a1 | -3.53991 | -45.87502 | 2024-11-01 12:36:00 | TERRA_M-T | BOM JARDIM | MARANHÃO | Brasil | 2102002 | 21 | 33 | nan | nan | nan | Amazônia | 7.4 |
| 71235b6d-5e5e-3415-899f-0fc6bc6679fd | -3.53663 | -44.75018 | 2024-11-01 12:36:00 | TERRA_M-T | ARARI | MARANHÃO | Brasil | 2101004 | 21 | 33 | nan | nan | nan | Amazônia | 12.7 |
| 76f6e3df-ffcb-3b0f-995f-a11b8e2c9f35 | -3.53535 | -44.75898 | 2024-11-01 12:36:00 | TERRA_M-T | ARARI | MARANHÃO | Brasil | 2101004 | 21 | 33 | nan | nan | nan | Amazônia | 8.1 |
| 8151cdb8-bfc9-3194-9aef-c788bd362c74 | -3.49233 | -44.80685 | 2024-11-01 12:36:00 | TERRA_M-T | ARARI | MARANHÃO | Brasil | 2101004 | 21 | 33 | nan | nan | nan | Amazônia | 15.3 |
| b3547d85-4fa5-349a-b9cb-1be73a815ed6 | -3.32219 | -44.7077 | 2024-11-01 12:36:00 | TERRA_M-T | ANAJATUBA | MARANHÃO | Brasil | 2100709 | 21 | 33 | nan | nan | nan | Amazônia | 10.5 |
| f1327c1d-569d-34e5-b57d-7ab8b46d597c | -3.27332 | -50.34732 | 2024-11-01 12:36:00 | TERRA_M-T | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 67.8 |
| c7f9517f-49d9-3d13-ba94-ee089c03dcb7 | -3.26388 | -50.32904 | 2024-11-01 12:36:00 | TERRA_M-T | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 43.6 |
| e64dc80a-a38b-3abb-b513-3764ed8c7b13 | -3.26142 | -50.34562 | 2024-11-01 12:36:00 | TERRA_M-T | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 87.8 |
| db5d0a40-ea10-3870-91c0-aabd16d3a342 | -3.24953 | -50.34389 | 2024-11-01 12:36:00 | TERRA_M-T | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 31.7 |
| 812dde82-c786-3441-8e5e-439a9539bcb0 | -3.17483 | -50.59447 | 2024-11-01 12:36:00 | TERRA_M-T | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 12.9 |
| 14d86d5a-f229-31a9-8ef3-d37d9ec1c23b | -3.1711 | -50.5872 | 2024-11-01 12:36:00 | TERRA_M-T | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 15.8 |
| 597274e0-0def-327d-b416-c6aac048eac4 | -3.12286 | -54.26075 | 2024-11-01 12:36:00 | TERRA_M-T | MOJUÍ DOS CAMPOS | PARÁ | Brasil | 1504752 | 15 | 33 | nan | nan | nan | Amazônia | 46.1 |
| 1c607e3f-5197-30c6-a07d-b09d3929754f | -3.05521 | -49.49021 | 2024-11-01 12:36:00 | TERRA_M-T | MOJU | PARÁ | Brasil | 1504703 | 15 | 33 | nan | nan | nan | Amazônia | 25.9 |
| 196841fd-ae1a-38ea-b4fa-d1b70981acbd | -5.57876 | -42.88839 | 2024-11-01 12:36:00 | TERRA_M-T | CURRALINHOS | PIAUÍ | Brasil | 2203255 | 22 | 33 | nan | nan | nan | Caatinga | 33.4 |
| d723df03-e7a5-3a83-9788-97e5d78ad215 | -3.05502 | -49.48424 | 2024-11-01 12:36:00 | TERRA_M-T | MOJU | PARÁ | Brasil | 1504703 | 15 | 33 | nan | nan | nan | Amazônia | 38.1 |
| 948775af-3401-3909-ba5f-8e69cb4f5a61 | -3.04627 | -49.47424 | 2024-11-01 12:36:00 | TERRA_M-T | MOJU | PARÁ | Brasil | 1504703 | 15 | 33 | nan | nan | nan | Amazônia | 71.3 |
| 824ad1fa-fa75-36aa-b77d-736eabcbdb6f | -3.04597 | -49.46828 | 2024-11-01 12:36:00 | TERRA_M-T | MOJU | PARÁ | Brasil | 1504703 | 15 | 33 | nan | nan | nan | Amazônia | 53.3 |
| 1a178f9e-0d4c-34df-b0a4-3838655f7d30 | -3.04481 | -48.76941 | 2024-11-01 12:36:00 | TERRA_M-T | TAILÂNDIA | PARÁ | Brasil | 1507953 | 15 | 33 | nan | nan | nan | Amazônia | 70.1 |
| 73f9a42a-8da7-37c9-95ec-7456657b135e | -3.04407 | -49.48859 | 2024-11-01 12:36:00 | TERRA_M-T | MOJU | PARÁ | Brasil | 1504703 | 15 | 33 | nan | nan | nan | Amazônia | 71.1 |
| 47966f2c-87a0-3450-90cb-a59cba42cd6d | -3.04389 | -49.48258 | 2024-11-01 12:36:00 | TERRA_M-T | MOJU | PARÁ | Brasil | 1504703 | 15 | 33 | nan | nan | nan | Amazônia | 106.7 |
| d44cdb97-8995-3a17-98a2-c1530fa42f12 | -3.04172 | -50.42188 | 2024-11-01 12:36:00 | TERRA_M-T | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 14.2 |
| a4c60925-9561-3843-bd01-86ff802ca181 | -2.8669 | -48.65333 | 2024-11-01 12:36:00 | TERRA_M-T | TAILÂNDIA | PARÁ | Brasil | 1507953 | 15 | 33 | nan | nan | nan | Amazônia | 29.0 |
| 28246725-5ae8-3638-b0e3-881df90fc091 | -2.86504 | -48.666 | 2024-11-01 12:36:00 | TERRA_M-T | TAILÂNDIA | PARÁ | Brasil | 1507953 | 15 | 33 | nan | nan | nan | Amazônia | 19.5 |
| cf4163b4-5d30-3707-a5f8-d948ebb1c29f | -2.86114 | -53.33995 | 2024-11-01 12:36:00 | TERRA_M-T | MEDICILÂNDIA | PARÁ | Brasil | 1504455 | 15 | 33 | nan | nan | nan | Amazônia | 32.5 |
| 4ddcbc8d-3aef-3fcc-bd33-1f87065cdcf3 | -2.79238 | -49.55294 | 2024-11-01 12:36:00 | TERRA_M-T | BAIÃO | PARÁ | Brasil | 1501204 | 15 | 33 | nan | nan | nan | Amazônia | 14.9 |
| 4ea8fb30-1470-3e08-b6dd-ae7363a21ad2 | -2.77566 | -48.64715 | 2024-11-01 12:36:00 | TERRA_M-T | TAILÂNDIA | PARÁ | Brasil | 1507953 | 15 | 33 | nan | nan | nan | Amazônia | 9.2 |
| cd32d6e9-8028-3880-95b2-8ac647657d22 | -7.36523 | -41.0258 | 2024-11-01 12:36:00 | TERRA_M-T | JAICÓS | PIAUÍ | Brasil | 2205201 | 22 | 33 | nan | nan | nan | Caatinga | 13.5 |
| 0b542331-daab-3757-b04b-6c65de3a51c4 | -6.12474 | -41.80705 | 2024-11-01 12:36:00 | TERRA_M-T | AROAZES | PIAUÍ | Brasil | 2200905 | 22 | 33 | nan | nan | nan | Caatinga | 31.7 |
| ceea594d-eeda-3c64-98c2-d414e44f5b11 | -6.12374 | -42.70221 | 2024-11-01 12:36:00 | TERRA_M-T | ANGICAL DO PIAUÍ | PIAUÍ | Brasil | 2200608 | 22 | 33 | nan | nan | nan | Caatinga | 11.5 |
| 1340ddb5-9470-31e9-bae7-51afa5e86f25 | -6.12307 | -41.81937 | 2024-11-01 12:36:00 | TERRA_M-T | AROAZES | PIAUÍ | Brasil | 2200905 | 22 | 33 | nan | nan | nan | Caatinga | 64.4 |
| c32d7d36-b40a-3080-b4a7-6d03deb78cfc | -5.95086 | -43.27628 | 2024-11-01 12:36:00 | TERRA_M-T | SÃO FRANCISCO DO MARANHÃO | MARANHÃO | Brasil | 2110906 | 21 | 33 | nan | nan | nan | Caatinga | 12.6 |


[Clique aqui para ver as próximas entradas](README57.md)
