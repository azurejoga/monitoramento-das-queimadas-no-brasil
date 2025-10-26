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

## Dados Diários - Página 55

| ID | Latitude | Longitude | Data/Hora GMT | Satélite | Município | Estado | País | Município ID | Estado ID | País ID | Dias sem Chuva | Precipitação | Risco de Fogo | Bioma | FRP |
|----|----------|-----------|---------------|----------|-----------|--------|------|--------------|-----------|---------|----------------|--------------|----------------|-------|-----|
| 082607cf-c004-3a85-81e1-a1b880c716a9 | -8.44882 | -45.12065 | 2025-10-26 12:00:00 | TERRA_M-T | BAIXA GRANDE DO RIBEIRO | PIAUÍ | Brasil | 2201150 | 22 | 33 | nan | nan | nan | Cerrado | 9.0 |
| 364ac25b-95cf-3e0c-87bf-77f652714c0a | -7.8816 | -45.7069 | 2025-10-26 12:00:00 | TERRA_M-T | TASSO FRAGOSO | MARANHÃO | Brasil | 2112001 | 21 | 33 | nan | nan | nan | Cerrado | 17.6 |
| 13c03559-6c42-3b72-97e1-6d0b37d30559 | -10.8843 | -47.95145 | 2025-10-26 12:00:00 | TERRA_M-T | MONTE DO CARMO | TOCANTINS | Brasil | 1713601 | 17 | 33 | nan | nan | nan | Cerrado | 19.2 |
| 59a80fd4-d006-3e6a-813c-536d1286b951 | -12.70017 | -42.29885 | 2025-10-26 12:00:00 | TERRA_M-T | IBITIARA | BAHIA | Brasil | 2913002 | 29 | 33 | nan | nan | nan | Caatinga | 63.7 |
| f08bbe84-68fc-33c8-a281-b493acdc3c91 | -7.88002 | -45.71754 | 2025-10-26 12:00:00 | TERRA_M-T | TASSO FRAGOSO | MARANHÃO | Brasil | 2112001 | 21 | 33 | nan | nan | nan | Cerrado | 8.3 |
| 28668016-633f-36d6-8872-118be754ad3c | -7.45016 | -47.20875 | 2025-10-26 12:00:00 | TERRA_M-T | CAROLINA | MARANHÃO | Brasil | 2102804 | 21 | 33 | nan | nan | nan | Cerrado | 16.5 |
| 188425aa-e3ab-3957-89da-7136dd66d93c | -6.25827 | -43.56068 | 2025-10-26 12:00:00 | TERRA_M-T | LAGOA DO MATO | MARANHÃO | Brasil | 2105922 | 21 | 33 | nan | nan | nan | Cerrado | 11.1 |
| c78e8704-4e9e-3c9a-9c43-a28e6507eb41 | -8.31975 | -46.8126 | 2025-10-26 12:00:00 | TERRA_M-T | CAMPOS LINDOS | TOCANTINS | Brasil | 1703842 | 17 | 33 | nan | nan | nan | Cerrado | 20.5 |
| 17b56704-fdef-3a51-93a5-3a1737c383de | -6.62659 | -44.63979 | 2025-10-26 12:00:00 | TERRA_M-T | MIRADOR | MARANHÃO | Brasil | 2106706 | 21 | 33 | nan | nan | nan | Cerrado | 7.7 |
| 8ab0a9f7-ef82-3da2-b951-4bbe64b79b82 | -10.88753 | -47.95833 | 2025-10-26 12:00:00 | TERRA_M-T | MONTE DO CARMO | TOCANTINS | Brasil | 1713601 | 17 | 33 | nan | nan | nan | Cerrado | 29.8 |
| 92057d6b-5dbb-3163-baa4-1270a7cb1f1c | -11.39903 | -46.06271 | 2025-10-26 12:00:00 | TERRA_M-T | FORMOSA DO RIO PRETO | BAHIA | Brasil | 2911105 | 29 | 33 | nan | nan | nan | Cerrado | 29.4 |
| 88b21918-7e16-3582-a410-9f72d6d738c5 | -6.63356 | -42.23618 | 2025-10-26 12:00:00 | TERRA_M-T | TANQUE DO PIAUÍ | PIAUÍ | Brasil | 2210979 | 22 | 33 | nan | nan | nan | Caatinga | 17.2 |
| 5c825f60-0231-3d0b-a11d-43665316a697 | -6.39325 | -45.79009 | 2025-10-26 12:00:00 | TERRA_M-T | FERNANDO FALCÃO | MARANHÃO | Brasil | 2104081 | 21 | 33 | nan | nan | nan | Cerrado | 51.5 |
| b4cdd35f-50f3-3741-84fc-89eef520f9fc | -6.43296 | -42.0328 | 2025-10-26 12:00:00 | TERRA_M-T | NOVO ORIENTE DO PIAUÍ | PIAUÍ | Brasil | 2206902 | 22 | 33 | nan | nan | nan | Caatinga | 12.9 |
| 8cdeacfd-f7c5-34e2-ab41-fc2dedc5b1fd | -8.44636 | -47.63492 | 2025-10-26 12:00:00 | TERRA_M-T | ITACAJÁ | TOCANTINS | Brasil | 1710508 | 17 | 33 | nan | nan | nan | Cerrado | 9.8 |
| 055bb311-de47-322a-85aa-176438749b6a | -13.88621 | -43.11438 | 2025-10-26 12:00:00 | TERRA_M-T | MATINA | BAHIA | Brasil | 2921054 | 29 | 33 | nan | nan | nan | Caatinga | 5.4 |
| b93dcd76-54b5-3777-9cf5-5ecd826f306d | -8.32769 | -45.35774 | 2025-10-26 12:00:00 | TERRA_M-T | BAIXA GRANDE DO RIBEIRO | PIAUÍ | Brasil | 2201150 | 22 | 33 | nan | nan | nan | Cerrado | 9.9 |
| 489d549e-2455-36eb-a1c1-a979a9fb935e | -10.22071 | -49.85258 | 2025-10-26 12:00:00 | TERRA_M-T | PIUM | TOCANTINS | Brasil | 1717503 | 17 | 33 | nan | nan | nan | Cerrado | 21.9 |
| 8aa804c9-eb14-3988-8587-827cc9491cdf | -13.89827 | -48.46178 | 2025-10-26 12:00:00 | TERRA_M-T | CAMPINAÇU | GOIÁS | Brasil | 5204656 | 52 | 33 | nan | nan | nan | Cerrado | 23.8 |
| 096899cd-e177-39d3-b9cc-4b3f21721bfa | -9.5729 | -46.93042 | 2025-10-26 12:00:00 | TERRA_M-T | LIZARDA | TOCANTINS | Brasil | 1712405 | 17 | 33 | nan | nan | nan | Cerrado | 10.4 |
| 96af0ab2-f1b6-3167-909d-27a516f7ed50 | -6.40476 | -45.78053 | 2025-10-26 12:00:00 | TERRA_M-T | FERNANDO FALCÃO | MARANHÃO | Brasil | 2104081 | 21 | 33 | nan | nan | nan | Cerrado | 72.3 |
| 52290d65-4bfb-380b-929a-ddc2135756fe | -15.74422 | -43.93534 | 2025-10-26 12:00:00 | TERRA_M-T | VARZELÂNDIA | MINAS GERAIS | Brasil | 3170909 | 31 | 33 | nan | nan | nan | Cerrado | 8.7 |
| c77f9d1a-31dd-3eb8-8667-c0ea47989276 | -6.55157 | -41.58125 | 2025-10-26 12:00:00 | TERRA_M-T | LAGOA DO SÍTIO | PIAUÍ | Brasil | 2205599 | 22 | 33 | nan | nan | nan | Caatinga | 6.6 |
| e2ee79bd-44fa-3480-96cb-d2b8aedba1a7 | -13.32672 | -47.92505 | 2025-10-26 12:00:00 | TERRA_M-T | CAVALCANTE | GOIÁS | Brasil | 5205307 | 52 | 33 | nan | nan | nan | Cerrado | 14.3 |
| 6cc6d4e0-7b03-3fcf-9611-179d00fa03e1 | -10.94977 | -48.07571 | 2025-10-26 12:00:00 | TERRA_M-T | MONTE DO CARMO | TOCANTINS | Brasil | 1713601 | 17 | 33 | nan | nan | nan | Cerrado | 131.2 |
| ea7d8965-9036-32cd-a175-d08ff2e72d06 | -8.05378 | -46.74161 | 2025-10-26 12:00:00 | TERRA_M-T | CAMPOS LINDOS | TOCANTINS | Brasil | 1703842 | 17 | 33 | nan | nan | nan | Cerrado | 23.3 |
| 80efceb7-f236-355d-8b52-b59b1d59ee33 | -10.40803 | -45.34804 | 2025-10-26 12:00:00 | TERRA_M-T | CORRENTE | PIAUÍ | Brasil | 2202901 | 22 | 33 | nan | nan | nan | Cerrado | 11.3 |
| 329a1941-0b2f-3b51-94c8-78309c13256b | -7.41113 | -45.98221 | 2025-10-26 12:00:00 | TERRA_M-T | BALSAS | MARANHÃO | Brasil | 2101400 | 21 | 33 | nan | nan | nan | Cerrado | 13.4 |
| 6fa01146-bf03-398e-809d-e8e9ffb4f743 | -14.22547 | -42.31362 | 2025-10-26 12:00:00 | TERRA_M-T | IBIASSUCÊ | BAHIA | Brasil | 2912004 | 29 | 33 | nan | nan | nan | Caatinga | 10.1 |
| cb860a1c-00e8-351c-a70c-372cd513e2e5 | -6.39659 | -45.76752 | 2025-10-26 12:00:00 | TERRA_M-T | FERNANDO FALCÃO | MARANHÃO | Brasil | 2104081 | 21 | 33 | nan | nan | nan | Cerrado | 15.9 |
| 54b4930b-754c-3b2b-b7ca-d359a288c98f | -9.9797 | -47.09311 | 2025-10-26 12:00:00 | TERRA_M-T | LIZARDA | TOCANTINS | Brasil | 1712405 | 17 | 33 | nan | nan | nan | Cerrado | 68.0 |
| 30f52b17-8ae1-3fb0-8939-4a8ac7abec73 | -13.88758 | -48.46069 | 2025-10-26 12:00:00 | TERRA_M-T | CAMPINAÇU | GOIÁS | Brasil | 5204656 | 52 | 33 | nan | nan | nan | Cerrado | 21.6 |
| a324c6ce-a257-3ed1-9077-bd4e9d54181c | -9.20101 | -46.35236 | 2025-10-26 12:00:00 | TERRA_M-T | ALTO PARNAÍBA | MARANHÃO | Brasil | 2100501 | 21 | 33 | nan | nan | nan | Cerrado | 9.4 |
| a81724c7-fbf5-3413-b7ab-cc262a9ab609 | -10.61593 | -46.61673 | 2025-10-26 12:00:00 | TERRA_M-T | MATEIROS | TOCANTINS | Brasil | 1712702 | 17 | 33 | nan | nan | nan | Cerrado | 39.3 |
| a0481f87-6464-3b9b-8a36-914f3fcc5e09 | -8.33589 | -46.17005 | 2025-10-26 12:00:00 | TERRA_M-T | BALSAS | MARANHÃO | Brasil | 2101400 | 21 | 33 | nan | nan | nan | Cerrado | 10.9 |
| 612d7145-6278-32e2-9d9d-99ce950e6665 | -10.51219 | -46.55891 | 2025-10-26 12:00:00 | TERRA_M-T | MATEIROS | TOCANTINS | Brasil | 1712702 | 17 | 33 | nan | nan | nan | Cerrado | 8.8 |
| 6196f538-8e5d-34a3-8d96-0a4dd7180745 | -13.08459 | -45.97173 | 2025-10-26 12:00:00 | TERRA_M-T | SÃO DESIDÉRIO | BAHIA | Brasil | 2928901 | 29 | 33 | nan | nan | nan | Cerrado | 54.9 |
| e3f896cf-1b3a-32ec-a829-55f02469a475 | -14.42383 | -46.27489 | 2025-10-26 12:00:00 | TERRA_M-T | BURITINÓPOLIS | GOIÁS | Brasil | 5203962 | 52 | 33 | nan | nan | nan | Cerrado | 20.5 |
| a2bee5b2-6032-32fa-9f57-d5153840b1d3 | -13.90094 | -42.13065 | 2025-10-26 12:00:00 | TERRA_M-T | LIVRAMENTO DE NOSSA SENHORA | BAHIA | Brasil | 2919504 | 29 | 33 | nan | nan | nan | Caatinga | 19.5 |
| 772744bc-3d36-328f-8d26-80631e0b2714 | -13.18837 | -46.8504 | 2025-10-26 12:00:00 | TERRA_M-T | MONTE ALEGRE DE GOIÁS | GOIÁS | Brasil | 5213509 | 52 | 33 | nan | nan | nan | Cerrado | 10.4 |
| 0d85a71f-6df9-37f7-a69e-e08a46c34b1c | -15.56044 | -42.99614 | 2025-10-26 12:00:00 | TERRA_M-T | PORTEIRINHA | MINAS GERAIS | Brasil | 3152204 | 31 | 33 | nan | nan | nan | Caatinga | 5.6 |
| 867a2fc7-1dfe-315b-8c63-f74f766119d8 | -13.07214 | -45.92968 | 2025-10-26 12:00:00 | TERRA_M-T | SÃO DESIDÉRIO | BAHIA | Brasil | 2928901 | 29 | 33 | nan | nan | nan | Cerrado | 166.8 |
| 44dc4c55-5d9c-3856-b987-3d6333d71ccd | -13.08607 | -45.9619 | 2025-10-26 12:00:00 | TERRA_M-T | SÃO DESIDÉRIO | BAHIA | Brasil | 2928901 | 29 | 33 | nan | nan | nan | Cerrado | 56.9 |
| d5aa1ed9-2571-34ab-ae5c-06559ff69366 | -6.43416 | -42.34011 | 2025-10-26 12:00:00 | TERRA_M-T | REGENERAÇÃO | PIAUÍ | Brasil | 2208809 | 22 | 33 | nan | nan | nan | Caatinga | 8.3 |
| c9d39d9c-1345-39ce-8237-f5626d945f81 | -13.32875 | -47.9123 | 2025-10-26 12:00:00 | TERRA_M-T | CAVALCANTE | GOIÁS | Brasil | 5205307 | 52 | 33 | nan | nan | nan | Cerrado | 9.7 |
| e0e3c1b4-b97d-3e66-845a-c67ab4dcdbdb | -10.35411 | -47.12634 | 2025-10-26 12:00:00 | TERRA_M-T | NOVO ACORDO | TOCANTINS | Brasil | 1715101 | 17 | 33 | nan | nan | nan | Cerrado | 35.7 |
| 2c1bc1bb-f5f3-3b61-a61e-33205106022a | -9.38392 | -40.22014 | 2025-10-26 12:00:00 | TERRA_M-T | JUAZEIRO | BAHIA | Brasil | 2918407 | 29 | 33 | nan | nan | nan | Caatinga | 13.5 |
| fb9cd017-6539-3bb3-9dde-6c2ff619f131 | -7.40327 | -45.13313 | 2025-10-26 12:00:00 | TERRA_M-T | LORETO | MARANHÃO | Brasil | 2106102 | 21 | 33 | nan | nan | nan | Cerrado | 8.1 |
| 3878ebc2-8c08-389a-9703-93f03bdea1b1 | -8.04158 | -46.75238 | 2025-10-26 12:00:00 | TERRA_M-T | CAMPOS LINDOS | TOCANTINS | Brasil | 1703842 | 17 | 33 | nan | nan | nan | Cerrado | 273.4 |
| a020cd9d-ba17-3401-a16f-67a67e93646a | -7.0908 | -39.56828 | 2025-10-26 12:00:00 | TERRA_M-T | CRATO | CEARÁ | Brasil | 2304202 | 23 | 33 | nan | nan | nan | Caatinga | 10.0 |
| bf3caaba-ff53-39f6-8591-88c193146902 | -8.54655 | -47.20538 | 2025-10-26 12:00:00 | TERRA_M-T | RECURSOLÂNDIA | TOCANTINS | Brasil | 1718501 | 17 | 33 | nan | nan | nan | Cerrado | 19.0 |
| 344cbd2d-c0ae-300a-a375-8bbf17b3b61f | -9.25669 | -46.3839 | 2025-10-26 12:00:00 | TERRA_M-T | ALTO PARNAÍBA | MARANHÃO | Brasil | 2100501 | 21 | 33 | nan | nan | nan | Cerrado | 14.3 |
| 05b809cc-2572-3a68-b32d-310d86fb0441 | -7.14316 | -38.78959 | 2025-10-26 12:00:00 | TERRA_M-T | BARRO | CEARÁ | Brasil | 2302008 | 23 | 33 | nan | nan | nan | Caatinga | 11.7 |
| e1c129e5-4df4-3ab4-908b-9418aba1ffc2 | -8.38855 | -44.83793 | 2025-10-26 12:00:00 | TERRA_M-T | BAIXA GRANDE DO RIBEIRO | PIAUÍ | Brasil | 2201150 | 22 | 33 | nan | nan | nan | Cerrado | 6.3 |
| b599b0a2-a37d-3c0c-a6e1-f66208fb0b31 | -13.65682 | -45.4157 | 2025-10-26 12:00:00 | TERRA_M-T | CORRENTINA | BAHIA | Brasil | 2909307 | 29 | 33 | nan | nan | nan | Cerrado | 9.2 |
| 2a278d86-0d25-3223-9ca8-be93d41d5150 | -10.94753 | -48.06851 | 2025-10-26 12:00:00 | TERRA_M-T | MONTE DO CARMO | TOCANTINS | Brasil | 1713601 | 17 | 33 | nan | nan | nan | Cerrado | 192.2 |
| 51412ac1-b514-36c6-af55-ee1773821a64 | -14.49104 | -47.89473 | 2025-10-26 12:00:00 | TERRA_M-T | NIQUELÂNDIA | GOIÁS | Brasil | 5214606 | 52 | 33 | nan | nan | nan | Cerrado | 12.5 |
| 8e8ded67-d584-3a04-be7b-87c04cbc7fba | -7.85778 | -45.37589 | 2025-10-26 12:00:00 | TERRA_M-T | RIBEIRO GONÇALVES | PIAUÍ | Brasil | 2208908 | 22 | 33 | nan | nan | nan | Cerrado | 14.8 |
| f8393c42-7146-3f40-a733-bc0865fd8e4e | -8.36546 | -46.17445 | 2025-10-26 12:00:00 | TERRA_M-T | BALSAS | MARANHÃO | Brasil | 2101400 | 21 | 33 | nan | nan | nan | Cerrado | 12.8 |
| 7afc679c-f874-338f-ae15-8e360986ed8e | -11.4225 | -46.03459 | 2025-10-26 12:00:00 | TERRA_M-T | FORMOSA DO RIO PRETO | BAHIA | Brasil | 2911105 | 29 | 33 | nan | nan | nan | Cerrado | 9.5 |
| afefb145-b427-3463-bd3d-3e5f254cb137 | -7.84348 | -46.44281 | 2025-10-26 12:00:00 | TERRA_M-T | RIACHÃO | MARANHÃO | Brasil | 2109502 | 21 | 33 | nan | nan | nan | Cerrado | 34.5 |
| 6b65c731-5bde-38a2-81e7-c6074bce7daf | -10.10481 | -45.33488 | 2025-10-26 12:00:00 | TERRA_M-T | SÃO GONÇALO DO GURGUÉIA | PIAUÍ | Brasil | 2209757 | 22 | 33 | nan | nan | nan | Cerrado | 6.3 |
| 6b20c982-7682-3b26-a430-51a015f446e4 | -6.24939 | -44.62993 | 2025-10-26 12:00:00 | TERRA_M-T | MIRADOR | MARANHÃO | Brasil | 2106706 | 21 | 33 | nan | nan | nan | Cerrado | 12.2 |
| fe331f81-124a-3acf-82b5-4df3e75819ba | -7.55326 | -42.52354 | 2025-10-26 12:00:00 | TERRA_M-T | SÃO JOSÉ DO PEIXE | PIAUÍ | Brasil | 2210102 | 22 | 33 | nan | nan | nan | Caatinga | 7.3 |
| eadedf61-f5d3-3e7c-9737-8521486a7df7 | -13.66579 | -45.41706 | 2025-10-26 12:00:00 | TERRA_M-T | CORRENTINA | BAHIA | Brasil | 2909307 | 29 | 33 | nan | nan | nan | Cerrado | 15.1 |
| e159138e-757a-3de5-8748-9e256de38ba0 | -6.54896 | -41.59953 | 2025-10-26 12:00:00 | TERRA_M-T | LAGOA DO SÍTIO | PIAUÍ | Brasil | 2205599 | 22 | 33 | nan | nan | nan | Caatinga | 14.0 |
| 531bbb7a-3796-33dc-9149-d030e6f50915 | -7.3603 | -42.4416 | 2025-10-26 12:00:00 | TERRA_M-T | SÃO FRANCISCO DO PIAUÍ | PIAUÍ | Brasil | 2209708 | 22 | 33 | nan | nan | nan | Caatinga | 7.0 |
| be84efb0-308c-37bc-9a48-1d9a943dcd75 | -7.79006 | -45.37648 | 2025-10-26 12:00:00 | TERRA_M-T | RIBEIRO GONÇALVES | PIAUÍ | Brasil | 2208908 | 22 | 33 | nan | nan | nan | Cerrado | 12.7 |
| 04682e74-9a7d-3214-968b-5859946df013 | -11.41156 | -46.04348 | 2025-10-26 12:00:00 | TERRA_M-T | FORMOSA DO RIO PRETO | BAHIA | Brasil | 2911105 | 29 | 33 | nan | nan | nan | Cerrado | 20.3 |
| 5c879709-edad-351e-b6ca-b29a21b2a1a8 | -14.49258 | -47.88865 | 2025-10-26 12:00:00 | TERRA_M-T | NIQUELÂNDIA | GOIÁS | Brasil | 5214606 | 52 | 33 | nan | nan | nan | Cerrado | 10.5 |
| 864e7887-9df4-3dac-8cab-fd3cfca72e83 | -6.7307 | -45.3796 | 2025-10-26 12:00:00 | TERRA_M-T | MIRADOR | MARANHÃO | Brasil | 2106706 | 21 | 33 | nan | nan | nan | Cerrado | 14.7 |
| 781f1be1-5da4-3d50-aed0-80633baa762f | -15.97651 | -48.30523 | 2025-10-26 12:00:00 | TERRA_M-T | SANTO ANTÔNIO DO DESCOBERTO | GOIÁS | Brasil | 5219753 | 52 | 33 | nan | nan | nan | Cerrado | 10.5 |
| db2b5bea-cf13-364d-9d0a-4e4dadfac870 | -11.7383 | -50.23494 | 2025-10-26 12:00:00 | TERRA_M-T | FORMOSO DO ARAGUAIA | TOCANTINS | Brasil | 1708205 | 17 | 33 | nan | nan | nan | Cerrado | 31.7 |
| 369e0fb8-ff5b-32e8-9df6-286cdbce4e4a | -12.32059 | -47.47433 | 2025-10-26 12:00:00 | TERRA_M-T | CONCEIÇÃO DO TOCANTINS | TOCANTINS | Brasil | 1705607 | 17 | 33 | nan | nan | nan | Cerrado | 18.3 |
| 3564a9ce-dadd-3dd5-ac27-06fcbc25b154 | -7.69474 | -42.17671 | 2025-10-26 12:00:00 | TERRA_M-T | SIMPLÍCIO MENDES | PIAUÍ | Brasil | 2210805 | 22 | 33 | nan | nan | nan | Caatinga | 6.6 |
| 77754f95-2170-33a6-8755-353d6e0346c5 | -14.43321 | -48.06882 | 2025-10-26 12:00:00 | TERRA_M-T | NIQUELÂNDIA | GOIÁS | Brasil | 5214606 | 52 | 33 | nan | nan | nan | Cerrado | 14.9 |
| b786f165-1888-396e-af83-634b77e1ff16 | -6.62802 | -44.63015 | 2025-10-26 12:00:00 | TERRA_M-T | MIRADOR | MARANHÃO | Brasil | 2106706 | 21 | 33 | nan | nan | nan | Cerrado | 8.3 |
| 264b022d-d5e2-322c-8f5e-829e6b1f39cb | -6.57877 | -41.45445 | 2025-10-26 12:00:00 | TERRA_M-T | SÃO JOÃO DA CANABRAVA | PIAUÍ | Brasil | 2209856 | 22 | 33 | nan | nan | nan | Caatinga | 5.5 |
| 3fc53b01-1fbc-3d7c-9863-c4b10b6cdd4a | -12.90565 | -42.28012 | 2025-10-26 12:00:00 | TERRA_M-T | IBIPITANGA | BAHIA | Brasil | 2912509 | 29 | 33 | nan | nan | nan | Caatinga | 69.8 |
| 6f3b9402-994f-3f50-84be-9d008f864635 | -8.32118 | -45.36132 | 2025-10-26 12:00:00 | TERRA_M-T | BAIXA GRANDE DO RIBEIRO | PIAUÍ | Brasil | 2201150 | 22 | 33 | nan | nan | nan | Cerrado | 14.0 |
| a1ef4f31-cb9f-373d-9a67-3023f7ada8f9 | -9.28655 | -45.18676 | 2025-10-26 12:00:00 | TERRA_M-T | BOM JESUS | PIAUÍ | Brasil | 2201903 | 22 | 33 | nan | nan | nan | Cerrado | 12.2 |
| 5d782d83-e845-3d36-a1cc-4aa5dca2adca | -16.35219 | -46.64745 | 2025-10-26 12:00:00 | TERRA_M-T | UNAÍ | MINAS GERAIS | Brasil | 3170404 | 31 | 33 | nan | nan | nan | Cerrado | 6.8 |
| e7260af5-d3dc-3b54-9663-9157796f3ad8 | -13.33073 | -47.89983 | 2025-10-26 12:00:00 | TERRA_M-T | CAVALCANTE | GOIÁS | Brasil | 5205307 | 52 | 33 | nan | nan | nan | Cerrado | 34.5 |
| 2a7a35ec-1ee7-33e8-b060-ff2ac08217b7 | -7.1563 | -45.29297 | 2025-10-26 12:00:00 | TERRA_M-T | LORETO | MARANHÃO | Brasil | 2106102 | 21 | 33 | nan | nan | nan | Cerrado | 7.4 |
| d67709a0-29e6-320e-b742-743f1dff2d1d | -9.57479 | -46.9183 | 2025-10-26 12:00:00 | TERRA_M-T | LIZARDA | TOCANTINS | Brasil | 1712405 | 17 | 33 | nan | nan | nan | Cerrado | 21.1 |
| 2b8935b2-7486-3f15-9d08-2f2cb1e071a8 | -6.2801 | -42.70758 | 2025-10-26 12:00:00 | TERRA_M-T | AMARANTE | PIAUÍ | Brasil | 2200509 | 22 | 33 | nan | nan | nan | Caatinga | 6.8 |
| 96eadc40-c942-35d6-a595-dabe299edce5 | -8.3573 | -46.16171 | 2025-10-26 12:00:00 | TERRA_M-T | BALSAS | MARANHÃO | Brasil | 2101400 | 21 | 33 | nan | nan | nan | Cerrado | 193.7 |
| 8d98b48a-4f83-3962-9960-7e06d1fbc3f6 | -8.36716 | -46.16307 | 2025-10-26 12:00:00 | TERRA_M-T | BALSAS | MARANHÃO | Brasil | 2101400 | 21 | 33 | nan | nan | nan | Cerrado | 17.9 |
| 52c7dd32-54eb-353b-9c00-b924dde7bec8 | -12.88961 | -47.90286 | 2025-10-26 12:00:00 | TERRA_M-T | PARANÃ | TOCANTINS | Brasil | 1716208 | 17 | 33 | nan | nan | nan | Cerrado | 8.5 |
| 64f27abc-3486-30a7-9610-8af471449ec1 | -10.10629 | -45.3251 | 2025-10-26 12:00:00 | TERRA_M-T | SÃO GONÇALO DO GURGUÉIA | PIAUÍ | Brasil | 2209757 | 22 | 33 | nan | nan | nan | Cerrado | 21.7 |
| 97823880-a62a-34ab-9f0c-74d9d05635c8 | -13.23241 | -47.73938 | 2025-10-26 12:00:00 | TERRA_M-T | PARANÃ | TOCANTINS | Brasil | 1716208 | 17 | 33 | nan | nan | nan | Cerrado | 8.1 |
| 1e1d14d4-682b-3547-8660-c80ac70d9df8 | -7.16351 | -45.63907 | 2025-10-26 12:00:00 | TERRA_M-T | SÃO RAIMUNDO DAS MANGABEIRAS | MARANHÃO | Brasil | 2111607 | 21 | 33 | nan | nan | nan | Cerrado | 9.7 |
| 0436d0bc-42db-38e8-a797-5227278bbd1c | -8.35557 | -46.17323 | 2025-10-26 12:00:00 | TERRA_M-T | BALSAS | MARANHÃO | Brasil | 2101400 | 21 | 33 | nan | nan | nan | Cerrado | 129.4 |
| 51f08226-c45e-3cfb-9111-413c777cae2e | -13.04502 | -45.86952 | 2025-10-26 12:00:00 | TERRA_M-T | SÃO DESIDÉRIO | BAHIA | Brasil | 2928901 | 29 | 33 | nan | nan | nan | Cerrado | 4.5 |
| dfa970a4-37f0-34ce-9e92-342ea160729d | -6.78964 | -45.40565 | 2025-10-26 12:00:00 | TERRA_M-T | SÃO RAIMUNDO DAS MANGABEIRAS | MARANHÃO | Brasil | 2111607 | 21 | 33 | nan | nan | nan | Cerrado | 9.7 |
| f672aa1f-9e8d-3aa9-a750-64e7b936253a | -6.70796 | -42.04449 | 2025-10-26 12:00:00 | TERRA_M-T | OEIRAS | PIAUÍ | Brasil | 2207009 | 22 | 33 | nan | nan | nan | Caatinga | 14.8 |
| 79f6735e-ba44-395c-9ddc-9c3295b77f8b | -7.80937 | -44.00547 | 2025-10-26 12:00:00 | TERRA_M-T | SEBASTIÃO LEAL | PIAUÍ | Brasil | 2210631 | 22 | 33 | nan | nan | nan | Cerrado | 19.5 |
| c502a0db-56cd-3a12-afed-35c43210dbbe | -7.80744 | -45.3895 | 2025-10-26 12:00:00 | TERRA_M-T | RIBEIRO GONÇALVES | PIAUÍ | Brasil | 2208908 | 22 | 33 | nan | nan | nan | Cerrado | 17.1 |
| be0d1364-da96-346b-a83d-1ea8c079ce46 | -12.35096 | -48.1164 | 2025-10-26 12:00:00 | TERRA_M-T | PARANÃ | TOCANTINS | Brasil | 1716208 | 17 | 33 | nan | nan | nan | Cerrado | 40.3 |
| dbc77f0d-90ea-3852-836b-bd64562658ed | -9.43899 | -46.33224 | 2025-10-26 12:00:00 | TERRA_M-T | ALTO PARNAÍBA | MARANHÃO | Brasil | 2100501 | 21 | 33 | nan | nan | nan | Cerrado | 10.4 |


[Clique aqui para ver as próximas entradas](README56.md)
