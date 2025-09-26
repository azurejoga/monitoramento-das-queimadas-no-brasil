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
| 6368daba-3738-398e-b493-afcf047890cc | -10.9381 | -44.2598 | 2025-09-26 14:20:00 | GOES-19 | SANTA RITA DE CÁSSIA | BAHIA | Brasil | 2928406 | 29 | 33 | nan | nan | nan | Cerrado | 99.4 |
| 96b7f905-1f9c-3819-bf25-b8768d104c80 | -20.7334 | -57.8293 | 2025-09-26 14:20:00 | GOES-19 | CORUMBÁ | MATO GROSSO DO SUL | Brasil | 5003207 | 50 | 33 | nan | nan | nan | Pantanal | 346.6 |
| 8a48ae5c-8640-3433-ab08-fe97fc82b319 | -6.5803 | -45.0889 | 2025-09-26 14:20:00 | GOES-19 | MIRADOR | MARANHÃO | Brasil | 2106706 | 21 | 33 | nan | nan | nan | Cerrado | 60.5 |
| edcffad3-8af9-362c-a6f8-98477ca802bb | -9.8658 | -45.9372 | 2025-09-26 14:20:00 | GOES-19 | ALTO PARNAÍBA | MARANHÃO | Brasil | 2100501 | 21 | 33 | nan | nan | nan | Cerrado | 77.4 |
| 1c0d3c0c-96c5-3ca0-bc2f-6543dac6dda5 | -13.201 | -47.4026 | 2025-09-26 14:20:00 | GOES-19 | ARRAIAS | TOCANTINS | Brasil | 1702406 | 17 | 33 | nan | nan | nan | Cerrado | 67.4 |
| 02e63dc3-0f86-369e-8b4e-94efa5ffd5f6 | -3.45 | -44.1238 | 2025-09-26 14:20:00 | GOES-19 | ITAPECURU MIRIM | MARANHÃO | Brasil | 2105401 | 21 | 33 | nan | nan | nan | Cerrado | 83.4 |
| 91957215-d905-3db3-bf53-a28ea7583475 | -8.8415 | -46.2095 | 2025-09-26 14:20:00 | GOES-19 | ALTO PARNAÍBA | MARANHÃO | Brasil | 2100501 | 21 | 33 | nan | nan | nan | Cerrado | 81.1 |
| 2bb2846e-78c1-395e-92bb-ae39ad366311 | -14.0964 | -51.1564 | 2025-09-26 14:20:00 | GOES-19 | COCALINHO | MATO GROSSO | Brasil | 5103106 | 51 | 33 | nan | nan | nan | Cerrado | 76.6 |
| 15e7d030-540b-3330-ade0-d7580de8befc | -8.8603 | -46.2075 | 2025-09-26 14:20:00 | GOES-19 | ALTO PARNAÍBA | MARANHÃO | Brasil | 2100501 | 21 | 33 | nan | nan | nan | Cerrado | 97.1 |
| 389ad1cd-e57b-3caf-96fe-0a078a1f31f9 | -10.8051 | -45.3866 | 2025-09-26 14:20:00 | GOES-19 | FORMOSA DO RIO PRETO | BAHIA | Brasil | 2911105 | 29 | 33 | nan | nan | nan | Cerrado | 284.9 |
| a0a9b86b-13cc-3ca5-bd1a-6068edf44725 | -17.1743 | -56.3685 | 2025-09-26 14:20:00 | GOES-19 | BARÃO DE MELGAÇO | MATO GROSSO | Brasil | 5101605 | 51 | 33 | nan | nan | nan | Pantanal | 93.2 |
| dd2de4e5-2fe4-3b4b-8c73-e1e52245b722 | -5.3695 | -42.284 | 2025-09-26 14:20:00 | GOES-19 | ALTO LONGÁ | PIAUÍ | Brasil | 2200301 | 22 | 33 | nan | nan | nan | Caatinga | 124.4 |
| 49b11987-a715-36f2-a788-b32cd453a53b | -5.7775 | -42.7961 | 2025-09-26 14:20:00 | GOES-19 | SÃO PEDRO DO PIAUÍ | PIAUÍ | Brasil | 2210508 | 22 | 33 | nan | nan | nan | Caatinga | 87.6 |
| 81ad8e38-8f77-302a-8050-21bdd0611fb9 | -12.6118 | -48.134 | 2025-09-26 14:20:00 | GOES-19 | PARANÃ | TOCANTINS | Brasil | 1716208 | 17 | 33 | nan | nan | nan | Cerrado | 63.5 |
| 950da4f0-5aac-36a3-8e32-9b83c3e55c73 | -9.8921 | -46.7437 | 2025-09-26 14:20:00 | GOES-19 | LIZARDA | TOCANTINS | Brasil | 1712405 | 17 | 33 | nan | nan | nan | Cerrado | 86.4 |
| ce6f12c4-737d-3d93-9c84-a31ecb1b521e | -10.5975 | -44.0975 | 2025-09-26 14:20:00 | GOES-19 | MANSIDÃO | BAHIA | Brasil | 2920452 | 29 | 33 | nan | nan | nan | Cerrado | 74.2 |
| c66fa84d-d472-373a-bfe3-01e8249c81c6 | -7.8735 | -45.2911 | 2025-09-26 14:20:00 | GOES-19 | RIBEIRO GONÇALVES | PIAUÍ | Brasil | 2208908 | 22 | 33 | nan | nan | nan | Cerrado | 193.4 |
| 16ebcdae-ff68-3d37-8c7c-f2d482b54921 | -11.0444 | -45.9021 | 2025-09-26 14:20:00 | GOES-19 | FORMOSA DO RIO PRETO | BAHIA | Brasil | 2911105 | 29 | 33 | nan | nan | nan | Cerrado | 137.4 |
| 21c3ca4d-92f4-3e6b-b3a0-4019201d3e07 | -14.7723 | -60.191 | 2025-09-26 14:20:00 | GOES-19 | VILA BELA DA SANTÍSSIMA TRINDADE | MATO GROSSO | Brasil | 5105507 | 51 | 33 | nan | nan | nan | Amazônia | 57.4 |
| 6258ddef-14a7-384f-97f2-15ba4a993adb | -9.5601 | -47.5139 | 2025-09-26 14:20:00 | GOES-19 | RIO SONO | TOCANTINS | Brasil | 1718758 | 17 | 33 | nan | nan | nan | Cerrado | 70.5 |
| c0e81f5e-7249-3753-9b3f-87d8116a0876 | -14.8855 | -45.5475 | 2025-09-26 14:20:00 | GOES-19 | COCOS | BAHIA | Brasil | 2908101 | 29 | 33 | nan | nan | nan | Cerrado | 79.1 |
| ebad18ff-bfe9-3921-a8f2-e0c636057c50 | -11.6457 | -45.3388 | 2025-09-26 14:20:00 | GOES-19 | RIACHÃO DAS NEVES | BAHIA | Brasil | 2926202 | 29 | 33 | nan | nan | nan | Cerrado | 73.6 |
| 9cb8d3b0-f0ac-3b41-9eed-de6b3c5be2a2 | -10.3938 | -46.1444 | 2025-09-26 14:20:00 | GOES-19 | MATEIROS | TOCANTINS | Brasil | 1712702 | 17 | 33 | nan | nan | nan | Cerrado | 105.8 |
| 2ca71004-335c-385f-aba0-edef9d73b5c9 | -7.6772 | -46.0097 | 2025-09-26 14:20:00 | GOES-19 | BALSAS | MARANHÃO | Brasil | 2101400 | 21 | 33 | nan | nan | nan | Cerrado | 87.2 |
| f067608d-53ee-300b-a567-a357e06808e9 | -20.7338 | -57.8083 | 2025-09-26 14:20:00 | GOES-19 | CORUMBÁ | MATO GROSSO DO SUL | Brasil | 5003207 | 50 | 33 | nan | nan | nan | Pantanal | 551.8 |
| 9fc4b27e-1fa1-3de3-a5da-d0c2f648563d | -5.3091 | -42.761 | 2025-09-26 14:20:00 | GOES-19 | TERESINA | PIAUÍ | Brasil | 2211001 | 22 | 33 | nan | nan | nan | Caatinga | 120.3 |
| b8adf73a-2e52-3d75-82ab-5c527109d8cb | -4.676 | -37.6366 | 2025-09-26 14:20:00 | GOES-19 | ARACATI | CEARÁ | Brasil | 2301109 | 23 | 33 | nan | nan | nan | Caatinga | 120.4 |
| e4858512-c31a-321f-bd85-ae347b2a955b | -10.4125 | -46.1647 | 2025-09-26 14:20:00 | GOES-19 | MATEIROS | TOCANTINS | Brasil | 1712702 | 17 | 33 | nan | nan | nan | Cerrado | 110.7 |
| 723398a3-bf6b-34ee-9bb9-f6c6055623b7 | -8.7708 | -43.0417 | 2025-09-26 14:20:00 | GOES-19 | JUREMA | PIAUÍ | Brasil | 2205532 | 22 | 33 | nan | nan | nan | Caatinga | 108.0 |
| 35a88350-66f8-3cba-a6a0-22a2f43e2bbe | -6.0782 | -44.719 | 2025-09-26 14:20:00 | GOES-19 | MIRADOR | MARANHÃO | Brasil | 2106706 | 21 | 33 | nan | nan | nan | Cerrado | 94.8 |
| 52af23e2-8d49-3b3a-aaf0-f5ebcb3201ef | -20.7342 | -57.7873 | 2025-09-26 14:20:00 | GOES-19 | CORUMBÁ | MATO GROSSO DO SUL | Brasil | 5003207 | 50 | 33 | nan | nan | nan | Pantanal | 98.8 |
| bfa9506f-b313-32a1-ae30-06b9d06d722e | -11.0631 | -45.9223 | 2025-09-26 14:20:00 | GOES-19 | FORMOSA DO RIO PRETO | BAHIA | Brasil | 2911105 | 29 | 33 | nan | nan | nan | Cerrado | 128.0 |
| 5cbada08-af36-350c-ade7-21dee259ec57 | -20.7537 | -57.8265 | 2025-09-26 14:20:00 | GOES-19 | CORUMBÁ | MATO GROSSO DO SUL | Brasil | 5003207 | 50 | 33 | nan | nan | nan | Pantanal | 280.0 |
| 594bf8a9-ae03-3930-8115-ebeef3399774 | -11.044 | -45.9249 | 2025-09-26 14:20:00 | GOES-19 | FORMOSA DO RIO PRETO | BAHIA | Brasil | 2911105 | 29 | 33 | nan | nan | nan | Cerrado | 178.9 |
| 878b0b6f-a2a3-3588-8d2d-d0c8db26ed78 | -10.3935 | -46.167 | 2025-09-26 14:20:00 | GOES-19 | MATEIROS | TOCANTINS | Brasil | 1712702 | 17 | 33 | nan | nan | nan | Cerrado | 80.1 |
| 7aea2625-9190-3b59-8d07-bb14076666c2 | -14.1153 | -51.1753 | 2025-09-26 14:20:00 | GOES-19 | COCALINHO | MATO GROSSO | Brasil | 5103106 | 51 | 33 | nan | nan | nan | Cerrado | 76.2 |
| 3ef6c323-1ef6-31ec-b5d4-05004dff7283 | -6.5036 | -45.2766 | 2025-09-26 14:20:00 | GOES-19 | MIRADOR | MARANHÃO | Brasil | 2106706 | 21 | 33 | nan | nan | nan | Cerrado | 75.0 |
| 8cd6efc8-a13c-3aba-acc9-95a922ac7153 | -9.109 | -48.8933 | 2025-09-26 14:20:00 | GOES-19 | DOIS IRMÃOS DO TOCANTINS | TOCANTINS | Brasil | 1707207 | 17 | 33 | nan | nan | nan | Cerrado | 84.6 |
| f2e02494-cc9f-364c-af99-1e149dee146a | -14.866 | -45.5511 | 2025-09-26 14:20:00 | GOES-19 | COCOS | BAHIA | Brasil | 2908101 | 29 | 33 | nan | nan | nan | Cerrado | 86.5 |
| 1d8a61e4-8fde-361d-bec6-bf42159dfb41 | -15.2761 | -46.4237 | 2025-09-26 14:20:00 | GOES-19 | BURITIS | MINAS GERAIS | Brasil | 3109303 | 31 | 33 | nan | nan | nan | Cerrado | 50.6 |
| c58bf7b9-56b0-3080-aeae-2465ac756ea8 | -11.9659 | -47.8669 | 2025-09-26 14:20:00 | GOES-19 | SÃO VALÉRIO | TOCANTINS | Brasil | 1720499 | 17 | 33 | nan | nan | nan | Cerrado | 98.2 |
| 0afa1c70-7b6f-30b1-9054-5927eade6665 | -3.8465 | -40.3362 | 2025-09-26 14:20:00 | GOES-19 | FORQUILHA | CEARÁ | Brasil | 2304350 | 23 | 33 | nan | nan | nan | Caatinga | 92.8 |
| 2675457a-0f92-3ed9-b275-5e3378cfe2ac | -10.5979 | -44.0741 | 2025-09-26 14:20:00 | GOES-19 | BURITIRAMA | BAHIA | Brasil | 2904753 | 29 | 33 | nan | nan | nan | Cerrado | 92.1 |
| 73799e0e-30e1-3826-9f74-754266efc552 | -7.3559 | -46.2177 | 2025-09-26 14:20:00 | GOES-19 | RIACHÃO | MARANHÃO | Brasil | 2109502 | 21 | 33 | nan | nan | nan | Cerrado | 75.4 |
| 62f73659-4e17-3e41-ba12-9aa034b73baa | -11.0131 | -44.3424 | 2025-09-26 14:20:00 | GOES-19 | SANTA RITA DE CÁSSIA | BAHIA | Brasil | 2928406 | 29 | 33 | nan | nan | nan | Cerrado | 114.6 |
| 9a99e552-dc82-3c0f-a555-335e34be2db2 | -5.5335 | -42.8149 | 2025-09-26 14:20:00 | GOES-19 | CURRALINHOS | PIAUÍ | Brasil | 2203255 | 22 | 33 | nan | nan | nan | Caatinga | 88.3 |
| df64a890-fbff-3405-91f3-c3919834b316 | -13.3463 | -47.8732 | 2025-09-26 14:20:00 | GOES-19 | CAVALCANTE | GOIÁS | Brasil | 5205307 | 52 | 33 | nan | nan | nan | Cerrado | 113.0 |
| 7c890250-fb33-39b0-a8be-184e318dcac7 | -5.4565 | -43.0554 | 2025-09-26 14:30:00 | GOES-19 | MATÕES | MARANHÃO | Brasil | 2106607 | 21 | 33 | nan | nan | nan | Cerrado | 95.8 |
| f0dfef47-9974-3a01-81bc-624dc4c4d546 | -11.0635 | -45.8996 | 2025-09-26 14:30:00 | GOES-19 | FORMOSA DO RIO PRETO | BAHIA | Brasil | 2911105 | 29 | 33 | nan | nan | nan | Cerrado | 134.3 |
| 446bf324-25c9-3af9-93c3-5f6a89f39f00 | -20.7537 | -57.8265 | 2025-09-26 14:30:00 | GOES-19 | CORUMBÁ | MATO GROSSO DO SUL | Brasil | 5003207 | 50 | 33 | nan | nan | nan | Pantanal | 398.8 |
| ac1c2a92-71e2-35ab-842f-deec534004ec | -20.7533 | -57.8474 | 2025-09-26 14:30:00 | GOES-19 | CORUMBÁ | MATO GROSSO DO SUL | Brasil | 5003207 | 50 | 33 | nan | nan | nan | Pantanal | 80.7 |
| 7098c754-5a92-3da5-a84c-d82f11a59a6e | -17.1746 | -56.3478 | 2025-09-26 14:30:00 | GOES-19 | BARÃO DE MELGAÇO | MATO GROSSO | Brasil | 5101605 | 51 | 33 | nan | nan | nan | Pantanal | 47.3 |
| cb96357b-7641-347b-af3f-14c541aa98c2 | -6.0782 | -44.719 | 2025-09-26 14:30:00 | GOES-19 | MIRADOR | MARANHÃO | Brasil | 2106706 | 21 | 33 | nan | nan | nan | Cerrado | 64.8 |
| 88ecba9d-b873-3ab3-aac6-cb8a1e4bd71e | -12.6118 | -48.134 | 2025-09-26 14:30:00 | GOES-19 | PARANÃ | TOCANTINS | Brasil | 1716208 | 17 | 33 | nan | nan | nan | Cerrado | 63.9 |
| cebfcf79-d5f6-3e66-a6f0-97660a094c14 | -10.8051 | -45.3866 | 2025-09-26 14:30:00 | GOES-19 | FORMOSA DO RIO PRETO | BAHIA | Brasil | 2911105 | 29 | 33 | nan | nan | nan | Cerrado | 188.5 |
| fad02100-c167-3aab-9474-eb643746aebb | -11.6425 | -44.4369 | 2025-09-26 14:30:00 | GOES-19 | COTEGIPE | BAHIA | Brasil | 2909406 | 29 | 33 | nan | nan | nan | Cerrado | 87.8 |
| c6fc083f-5dd9-3c38-8601-e70237c79813 | -11.9655 | -47.8891 | 2025-09-26 14:30:00 | GOES-19 | SÃO VALÉRIO | TOCANTINS | Brasil | 1720499 | 17 | 33 | nan | nan | nan | Cerrado | 61.9 |
| c91befc7-ef5b-39aa-b3d8-950201fbabf7 | -11.385 | -44.9386 | 2025-09-26 14:30:00 | GOES-19 | RIACHÃO DAS NEVES | BAHIA | Brasil | 2926202 | 29 | 33 | nan | nan | nan | Cerrado | 122.7 |
| 71993eed-5fed-3112-986d-04c1c2769449 | -3.45 | -44.1238 | 2025-09-26 14:30:00 | GOES-19 | ITAPECURU MIRIM | MARANHÃO | Brasil | 2105401 | 21 | 33 | nan | nan | nan | Cerrado | 92.3 |
| 337f2ace-7352-3c04-acf6-18ede89fd11a | -11.6618 | -44.434 | 2025-09-26 14:30:00 | GOES-19 | COTEGIPE | BAHIA | Brasil | 2909406 | 29 | 33 | nan | nan | nan | Cerrado | 108.5 |
| c21ff0c2-0608-38d7-94a5-bf73d1441835 | -9.8921 | -46.7437 | 2025-09-26 14:30:00 | GOES-19 | LIZARDA | TOCANTINS | Brasil | 1712405 | 17 | 33 | nan | nan | nan | Cerrado | 91.6 |
| e7bfe401-94c6-3bbd-8083-faa6cbbee86a | -8.4936 | -46.9146 | 2025-09-26 14:30:00 | GOES-19 | CAMPOS LINDOS | TOCANTINS | Brasil | 1703842 | 17 | 33 | nan | nan | nan | Cerrado | 114.9 |
| 1c5d9818-f2f4-3350-b7bb-d5d340016cc3 | -9.109 | -48.8933 | 2025-09-26 14:30:00 | GOES-19 | DOIS IRMÃOS DO TOCANTINS | TOCANTINS | Brasil | 1707207 | 17 | 33 | nan | nan | nan | Cerrado | 103.0 |
| 12055229-3415-332b-bbc5-1e154dbe6b0c | -7.3559 | -46.2177 | 2025-09-26 14:30:00 | GOES-19 | RIACHÃO | MARANHÃO | Brasil | 2109502 | 21 | 33 | nan | nan | nan | Cerrado | 81.9 |
| 1bcea952-e250-3cae-a2fc-ce10ca00177e | -14.0964 | -51.1564 | 2025-09-26 14:30:00 | GOES-19 | COCALINHO | MATO GROSSO | Brasil | 5103106 | 51 | 33 | nan | nan | nan | Cerrado | 84.7 |
| 2c706d17-db67-3fb5-8747-5fe6750ddc4c | -11.0631 | -45.9223 | 2025-09-26 14:30:00 | GOES-19 | FORMOSA DO RIO PRETO | BAHIA | Brasil | 2911105 | 29 | 33 | nan | nan | nan | Cerrado | 205.8 |
| e1302cf2-97eb-3a9d-b863-f55328ca1efa | -7.6584 | -46.0114 | 2025-09-26 14:30:00 | GOES-19 | BALSAS | MARANHÃO | Brasil | 2101400 | 21 | 33 | nan | nan | nan | Cerrado | 170.7 |
| 5e2d7aee-64c3-35c0-bf64-e74c47c856b8 | -11.4041 | -44.9359 | 2025-09-26 14:30:00 | GOES-19 | RIACHÃO DAS NEVES | BAHIA | Brasil | 2926202 | 29 | 33 | nan | nan | nan | Cerrado | 109.4 |
| e12139d7-7933-3431-8618-df67d94a1041 | -3.8465 | -40.3362 | 2025-09-26 14:30:00 | GOES-19 | FORQUILHA | CEARÁ | Brasil | 2304350 | 23 | 33 | nan | nan | nan | Caatinga | 107.0 |
| 6e64dcf1-b0ea-3d9e-9983-1dda28737d38 | -6.5801 | -45.1117 | 2025-09-26 14:30:00 | GOES-19 | MIRADOR | MARANHÃO | Brasil | 2106706 | 21 | 33 | nan | nan | nan | Cerrado | 109.7 |
| 47d65213-b271-3282-b359-303fa6026710 | -7.8735 | -45.2911 | 2025-09-26 14:30:00 | GOES-19 | RIBEIRO GONÇALVES | PIAUÍ | Brasil | 2208908 | 22 | 33 | nan | nan | nan | Cerrado | 159.4 |
| 49cfacb1-09d0-334f-a6ca-c4555dcb4894 | -10.9201 | -47.7561 | 2025-09-26 14:30:00 | GOES-19 | SILVANÓPOLIS | TOCANTINS | Brasil | 1720655 | 17 | 33 | nan | nan | nan | Cerrado | 67.4 |
| 36c1fb72-7531-34f0-8616-dad31cd3b743 | -8.6631 | -43.991 | 2025-09-26 14:30:00 | GOES-19 | CRISTINO CASTRO | PIAUÍ | Brasil | 2203107 | 22 | 33 | nan | nan | nan | Cerrado | 100.2 |
| fa3d942d-794d-337c-826e-e0cc40fb7d4e | -8.7708 | -43.0417 | 2025-09-26 14:30:00 | GOES-19 | JUREMA | PIAUÍ | Brasil | 2205532 | 22 | 33 | nan | nan | nan | Caatinga | 95.4 |
| 19120a9c-d4f1-3958-95a4-9769c8ea2fe6 | -11.9659 | -47.8669 | 2025-09-26 14:30:00 | GOES-19 | SÃO VALÉRIO | TOCANTINS | Brasil | 1720499 | 17 | 33 | nan | nan | nan | Cerrado | 83.1 |
| 4c3c2e7a-4bac-3c60-8233-de0f67b15517 | -5.3695 | -42.284 | 2025-09-26 14:30:00 | GOES-19 | ALTO LONGÁ | PIAUÍ | Brasil | 2200301 | 22 | 33 | nan | nan | nan | Caatinga | 162.1 |
| b10da980-a2c9-3534-8191-324adbd151ac | -7.3755 | -44.4478 | 2025-09-26 14:30:00 | GOES-19 | URUÇUÍ | PIAUÍ | Brasil | 2211209 | 22 | 33 | nan | nan | nan | Cerrado | 71.2 |
| 43e10710-2156-31a1-a78e-d9b901babc19 | -14.7723 | -60.191 | 2025-09-26 14:30:00 | GOES-19 | VILA BELA DA SANTÍSSIMA TRINDADE | MATO GROSSO | Brasil | 5105507 | 51 | 33 | nan | nan | nan | Amazônia | 61.7 |
| 2b233f7a-f011-37d1-9284-d3a1132fdc38 | -10.3938 | -46.1444 | 2025-09-26 14:30:00 | GOES-19 | MATEIROS | TOCANTINS | Brasil | 1712702 | 17 | 33 | nan | nan | nan | Cerrado | 96.4 |
| 1e2cecba-af11-3d18-a173-d4f61079fed9 | -6.8008 | -45.5236 | 2025-09-26 14:30:00 | GOES-19 | MIRADOR | MARANHÃO | Brasil | 2106706 | 21 | 33 | nan | nan | nan | Cerrado | 56.8 |
| 8322cef8-f4cb-366d-8207-073be2a179d8 | -11.0444 | -45.9021 | 2025-09-26 14:30:00 | GOES-19 | FORMOSA DO RIO PRETO | BAHIA | Brasil | 2911105 | 29 | 33 | nan | nan | nan | Cerrado | 181.6 |
| 63718006-01a5-3db2-834c-29eb1a9def10 | -5.3693 | -42.3077 | 2025-09-26 14:30:00 | GOES-19 | ALTO LONGÁ | PIAUÍ | Brasil | 2200301 | 22 | 33 | nan | nan | nan | Caatinga | 120.3 |
| 917b6c96-6f34-3386-b64d-7fc676ba26e8 | -10.4129 | -46.142 | 2025-09-26 14:30:00 | GOES-19 | MATEIROS | TOCANTINS | Brasil | 1712702 | 17 | 33 | nan | nan | nan | Cerrado | 93.8 |
| 7858a31f-d80f-3943-8fe3-1abfc00db9bc | -11.643 | -44.4135 | 2025-09-26 14:30:00 | GOES-19 | COTEGIPE | BAHIA | Brasil | 2909406 | 29 | 33 | nan | nan | nan | Cerrado | 107.2 |
| a1b0aa90-7b05-359e-8801-da69b042096c | -10.8055 | -45.3637 | 2025-09-26 14:30:00 | GOES-19 | FORMOSA DO RIO PRETO | BAHIA | Brasil | 2911105 | 29 | 33 | nan | nan | nan | Cerrado | 75.5 |
| ef3020ca-d821-35ce-b255-b887d2c774a1 | -4.1023 | -44.1379 | 2025-09-26 14:30:00 | GOES-19 | COROATÁ | MARANHÃO | Brasil | 2103604 | 21 | 33 | nan | nan | nan | Cerrado | 79.1 |
| 3da7c243-068e-3724-ae7e-b71695cd3119 | -10.9374 | -44.3065 | 2025-09-26 14:30:00 | GOES-19 | SANTA RITA DE CÁSSIA | BAHIA | Brasil | 2928406 | 29 | 33 | nan | nan | nan | Cerrado | 83.5 |
| 85544065-cc2f-32f9-9dcf-62b67bacf5ff | -7.6772 | -46.0097 | 2025-09-26 14:30:00 | GOES-19 | BALSAS | MARANHÃO | Brasil | 2101400 | 21 | 33 | nan | nan | nan | Cerrado | 130.4 |
| 5bafed1f-37ae-36fa-b113-974590c50607 | -13.3463 | -47.8732 | 2025-09-26 14:30:00 | GOES-19 | CAVALCANTE | GOIÁS | Brasil | 5205307 | 52 | 33 | nan | nan | nan | Cerrado | 96.6 |
| e778db71-ea44-39cf-baa5-1e9301422a81 | -10.3877 | -46.5506 | 2025-09-26 14:30:00 | GOES-19 | MATEIROS | TOCANTINS | Brasil | 1712702 | 17 | 33 | nan | nan | nan | Cerrado | 90.8 |
| c039340d-4c18-33a4-a866-c1b8dc1a3624 | -10.4125 | -46.1647 | 2025-09-26 14:30:00 | GOES-19 | MATEIROS | TOCANTINS | Brasil | 1712702 | 17 | 33 | nan | nan | nan | Cerrado | 95.3 |
| dfeef0fc-7f08-39ab-b4fe-47bb51eb4f48 | -7.3371 | -46.2194 | 2025-09-26 14:30:00 | GOES-19 | RIACHÃO | MARANHÃO | Brasil | 2109502 | 21 | 33 | nan | nan | nan | Cerrado | 104.5 |
| 55ec69df-d5de-365a-a832-d09e3fe14380 | -8.4748 | -46.9165 | 2025-09-26 14:30:00 | GOES-19 | CAMPOS LINDOS | TOCANTINS | Brasil | 1703842 | 17 | 33 | nan | nan | nan | Cerrado | 110.6 |
| 111ea638-e06e-3792-be0b-7e5a8f1785a4 | -11.7977 | -47.6449 | 2025-09-26 14:30:00 | GOES-19 | NATIVIDADE | TOCANTINS | Brasil | 1714203 | 17 | 33 | nan | nan | nan | Cerrado | 65.4 |
| 223a645e-3756-3b4e-a28f-0e74457fde07 | -3.7815 | -41.6957 | 2025-09-26 14:30:00 | GOES-19 | SÃO JOSÉ DO DIVINO | PIAUÍ | Brasil | 2210052 | 22 | 33 | nan | nan | nan | Caatinga | 81.3 |
| d88d78c7-26a9-3388-9638-280ba2f6c26a | -11.6622 | -44.4107 | 2025-09-26 14:30:00 | GOES-19 | COTEGIPE | BAHIA | Brasil | 2909406 | 29 | 33 | nan | nan | nan | Cerrado | 118.8 |
| b0069f20-a29f-37f1-89ac-81156df983a4 | -17.1743 | -56.3685 | 2025-09-26 14:30:00 | GOES-19 | BARÃO DE MELGAÇO | MATO GROSSO | Brasil | 5101605 | 51 | 33 | nan | nan | nan | Pantanal | 63.7 |
| a3c7f8cc-cace-305e-9c94-d91ff9b3a72c | -17.1939 | -56.3661 | 2025-09-26 14:30:00 | GOES-19 | BARÃO DE MELGAÇO | MATO GROSSO | Brasil | 5101605 | 51 | 33 | nan | nan | nan | Pantanal | 78.4 |
| 7f3cdf91-1a91-3e08-81d0-2d6a09ef53b7 | -11.6814 | -44.4078 | 2025-09-26 14:30:00 | GOES-19 | COTEGIPE | BAHIA | Brasil | 2909406 | 29 | 33 | nan | nan | nan | Cerrado | 113.8 |
| 4083a2b6-7b64-3cd2-9023-a52efa6aae9c | -12.631 | -48.1313 | 2025-09-26 14:30:00 | GOES-19 | PARANÃ | TOCANTINS | Brasil | 1716208 | 17 | 33 | nan | nan | nan | Cerrado | 115.3 |


[Clique aqui para ver as próximas entradas](README57.md)
