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

## Dados Diários - Página 40

| ID | Latitude | Longitude | Data/Hora GMT | Satélite | Município | Estado | País | Município ID | Estado ID | País ID | Dias sem Chuva | Precipitação | Risco de Fogo | Bioma | FRP |
|----|----------|-----------|---------------|----------|-----------|--------|------|--------------|-----------|---------|----------------|--------------|----------------|-------|-----|
| 62bc3145-3b42-312f-9a77-67f0f4b6d003 | -3.852 | -46.95026 | 2024-11-23 04:18:00 | NOAA-20 | ITINGA DO MARANHÃO | MARANHÃO | Brasil | 2105427 | 21 | 33 | nan | nan | nan | Amazônia | 1.2 |
| 492b986f-17c0-3fcf-a84e-c4f0689683c7 | -4.10661 | -46.80886 | 2024-11-23 04:18:00 | NOAA-20 | BOM JARDIM | MARANHÃO | Brasil | 2102002 | 21 | 33 | nan | nan | nan | Amazônia | 1.2 |
| 5dbe26f7-3403-3299-b620-3fc09c3135a7 | -4.28511 | -44.81279 | 2024-11-23 04:18:00 | NOAA-20 | BACABAL | MARANHÃO | Brasil | 2101202 | 21 | 33 | nan | nan | nan | Amazônia | 1.9 |
| af8360a5-091c-39d6-8f51-5dec62410df5 | -5.66326 | -44.19579 | 2024-11-23 04:18:00 | NOAA-20 | SÃO DOMINGOS DO MARANHÃO | MARANHÃO | Brasil | 2110708 | 21 | 33 | nan | nan | nan | Cerrado | 1.1 |
| e0a8aa82-392e-397d-9d5d-2def064def95 | -3.71063 | -47.61466 | 2024-11-23 04:18:00 | NOAA-20 | ULIANÓPOLIS | PARÁ | Brasil | 1508126 | 15 | 33 | nan | nan | nan | Amazônia | 1.6 |
| 7a798420-bad3-306b-bea0-463f5e8ded26 | -3.96718 | -46.73015 | 2024-11-23 04:18:00 | NOAA-20 | BOM JARDIM | MARANHÃO | Brasil | 2102002 | 21 | 33 | nan | nan | nan | Amazônia | 1.6 |
| d8038e25-1167-35fc-b5ab-f961a535ebe8 | -3.22751 | -54.24624 | 2024-11-23 04:18:00 | NOAA-20 | SANTARÉM | PARÁ | Brasil | 1506807 | 15 | 33 | nan | nan | nan | Amazônia | 1.1 |
| a991053a-fc90-3c36-9441-32f51a2e6498 | -4.52636 | -43.90781 | 2024-11-23 04:18:00 | NOAA-20 | CODÓ | MARANHÃO | Brasil | 2103307 | 21 | 33 | nan | nan | nan | Cerrado | 1.8 |
| b73de0f8-7f4d-35b6-87de-3058240996e1 | -4.12598 | -43.23082 | 2024-11-23 04:18:00 | NOAA-20 | AFONSO CUNHA | MARANHÃO | Brasil | 2100105 | 21 | 33 | nan | nan | nan | Cerrado | 2.5 |
| 24582fd0-6b75-30ee-99c1-a1fffe12bfe0 | -3.79323 | -46.68433 | 2024-11-23 04:18:00 | NOAA-20 | BOM JARDIM | MARANHÃO | Brasil | 2102002 | 21 | 33 | nan | nan | nan | Amazônia | 1.8 |
| f1740359-750d-3e9f-989d-1a19c0c9ec91 | -5.92525 | -44.60461 | 2024-11-23 04:18:00 | NOAA-20 | TUNTUM | MARANHÃO | Brasil | 2112308 | 21 | 33 | nan | nan | nan | Cerrado | 1.7 |
| fbbb78ae-ea64-3aac-86d0-418b54276450 | -4.62098 | -50.50591 | 2024-11-23 04:18:00 | NOAA-20 | NOVO REPARTIMENTO | PARÁ | Brasil | 1505064 | 15 | 33 | nan | nan | nan | Amazônia | 1.5 |
| 077fcffa-7398-3bd7-ae2c-089964066725 | -5.33076 | -42.71497 | 2024-11-23 04:18:00 | NOAA-20 | DEMERVAL LOBÃO | PIAUÍ | Brasil | 2203305 | 22 | 33 | nan | nan | nan | Caatinga | 2.0 |
| 41c62eb7-247c-3fb4-b560-f8e0ee3b718e | -5.29329 | -45.35437 | 2024-11-23 04:18:00 | NOAA-20 | BARRA DO CORDA | MARANHÃO | Brasil | 2101608 | 21 | 33 | nan | nan | nan | Cerrado | 0.7 |
| 194597ed-02c8-3984-a628-17c07d9a37ec | -3.21458 | -54.25267 | 2024-11-23 04:18:00 | NOAA-20 | MOJUÍ DOS CAMPOS | PARÁ | Brasil | 1504752 | 15 | 33 | nan | nan | nan | Amazônia | 1.2 |
| 361f1ab0-712b-30da-81bb-dd1c8670e7cc | -3.24892 | -50.12517 | 2024-11-23 04:18:00 | NOAA-20 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 6.2 |
| 54f8ff50-ceb7-36c5-9003-109bf6730f2d | -4.6659 | -45.67344 | 2024-11-23 04:18:00 | NOAA-20 | MARAJÁ DO SENA | MARANHÃO | Brasil | 2106359 | 21 | 33 | nan | nan | nan | Amazônia | 3.8 |
| 0d3acb48-95c2-3093-b11b-ed30662a1289 | -4.6317 | -49.54215 | 2024-11-23 04:18:00 | NOAA-20 | NOVO REPARTIMENTO | PARÁ | Brasil | 1505064 | 15 | 33 | nan | nan | nan | Amazônia | 1.5 |
| 4eef5ff4-33f9-358e-8ffc-cdda91fd9a9f | -4.11037 | -48.25439 | 2024-11-23 04:18:00 | NOAA-20 | DOM ELISEU | PARÁ | Brasil | 1502939 | 15 | 33 | nan | nan | nan | Amazônia | 0.9 |
| 467cda78-575f-3196-866a-04481137aee6 | -4.55719 | -45.74841 | 2024-11-23 04:18:00 | NOAA-20 | SANTA LUZIA | MARANHÃO | Brasil | 2110005 | 21 | 33 | nan | nan | nan | Amazônia | 0.6 |
| 3a0f557d-888b-3b30-9a90-f2615129d1a3 | -4.83721 | -48.63971 | 2024-11-23 04:18:00 | NOAA-20 | BOM JESUS DO TOCANTINS | PARÁ | Brasil | 1501576 | 15 | 33 | nan | nan | nan | Amazônia | 0.8 |
| 09474d1f-c262-3080-982a-88d905a63fd9 | -3.77276 | -46.67712 | 2024-11-23 04:18:00 | NOAA-20 | BOM JARDIM | MARANHÃO | Brasil | 2102002 | 21 | 33 | nan | nan | nan | Amazônia | 1.6 |
| fb97d631-043a-3ca3-8ca7-67c3bd04aa12 | -5.75413 | -46.26476 | 2024-11-23 04:18:00 | NOAA-20 | GRAJAÚ | MARANHÃO | Brasil | 2104800 | 21 | 33 | nan | nan | nan | Cerrado | 1.9 |
| 2993e26c-a451-35e8-b2f8-7df22847fb71 | -4.2376 | -48.63836 | 2024-11-23 04:18:00 | NOAA-20 | RONDON DO PARÁ | PARÁ | Brasil | 1506187 | 15 | 33 | nan | nan | nan | Amazônia | 1.5 |
| 2ccfd320-ee24-3cb0-a44d-983dd3282975 | -5.06574 | -44.2359 | 2024-11-23 04:18:00 | NOAA-20 | GOVERNADOR ARCHER | MARANHÃO | Brasil | 2104503 | 21 | 33 | nan | nan | nan | Cerrado | 1.6 |
| b283733f-7d8f-356f-9206-87158dc9dce1 | -5.95026 | -44.46716 | 2024-11-23 04:18:00 | NOAA-20 | COLINAS | MARANHÃO | Brasil | 2103505 | 21 | 33 | nan | nan | nan | Cerrado | 4.6 |
| 8091eea3-3d3e-3e09-ba2f-5c2a544b15ca | -6.14735 | -46.67622 | 2024-11-23 04:18:00 | NOAA-20 | SÍTIO NOVO | MARANHÃO | Brasil | 2111805 | 21 | 33 | nan | nan | nan | Cerrado | 1.6 |
| 3f56fbe4-97f4-3eef-96e8-4e33e5773d2e | -2.74546 | -54.0258 | 2024-11-23 04:18:00 | NOAA-20 | PRAINHA | PARÁ | Brasil | 1506005 | 15 | 33 | nan | nan | nan | Amazônia | 0.9 |
| a617962b-e54a-3a48-84e0-d28931622bb6 | -4.28702 | -48.21575 | 2024-11-23 04:18:00 | NOAA-20 | RONDON DO PARÁ | PARÁ | Brasil | 1506187 | 15 | 33 | nan | nan | nan | Amazônia | 2.7 |
| b81ac1aa-11a7-3f82-af42-fd8e4fc3af2e | -3.79963 | -51.76694 | 2024-11-23 04:18:00 | NOAA-20 | SENADOR JOSÉ PORFÍRIO | PARÁ | Brasil | 1507805 | 15 | 33 | nan | nan | nan | Amazônia | 2.2 |
| a05fb4b7-946f-392b-8874-f0c6a7784078 | -3.86925 | -51.25348 | 2024-11-23 04:18:00 | NOAA-20 | PACAJÁ | PARÁ | Brasil | 1505486 | 15 | 33 | nan | nan | nan | Amazônia | 1.3 |
| a099d5ca-4b69-393e-a94f-d17bc15c462c | -3.86398 | -44.68264 | 2024-11-23 04:18:00 | NOAA-20 | CONCEIÇÃO DO LAGO-AÇU | MARANHÃO | Brasil | 2103554 | 21 | 33 | nan | nan | nan | Amazônia | 0.6 |
| 6024fde5-5a4a-3361-9dc3-a0b4c7105909 | -4.39387 | -49.77337 | 2024-11-23 04:18:00 | NOAA-20 | NOVO REPARTIMENTO | PARÁ | Brasil | 1505064 | 15 | 33 | nan | nan | nan | Amazônia | 1.4 |
| 04e691b1-9c36-36cb-b8f7-87118258c7be | -4.56269 | -48.02295 | 2024-11-23 04:18:00 | NOAA-20 | RONDON DO PARÁ | PARÁ | Brasil | 1506187 | 15 | 33 | nan | nan | nan | Amazônia | 1.0 |
| 2c672e02-f4a5-3976-9070-08c100c63fbd | -10.58273 | -36.98488 | 2024-11-23 04:18:00 | NOAA-20 | JAPARATUBA | SERGIPE | Brasil | 2803302 | 28 | 33 | nan | nan | nan | Mata Atlântica | 1.0 |
| ec71629a-6f04-35b7-b65b-39368d81fc68 | -3.08569 | -53.26023 | 2024-11-23 04:18:00 | NOAA-20 | MEDICILÂNDIA | PARÁ | Brasil | 1504455 | 15 | 33 | nan | nan | nan | Amazônia | 1.5 |
| 2c3ce7ba-5b47-343e-a499-23d92ea1473e | -3.74901 | -50.0114 | 2024-11-23 04:18:00 | NOAA-20 | PACAJÁ | PARÁ | Brasil | 1505486 | 15 | 33 | nan | nan | nan | Amazônia | 0.9 |
| 43a6f33f-b140-3690-a7e8-34f763c5068f | -3.96935 | -46.65027 | 2024-11-23 04:18:00 | NOAA-20 | BOM JARDIM | MARANHÃO | Brasil | 2102002 | 21 | 33 | nan | nan | nan | Amazônia | 2.0 |
| a2f471a5-0da7-3014-9392-292017138b5e | -4.09717 | -51.06379 | 2024-11-23 04:18:00 | NOAA-20 | PACAJÁ | PARÁ | Brasil | 1505486 | 15 | 33 | nan | nan | nan | Amazônia | 3.3 |
| 13e041b6-f07d-3419-93fd-a6a0c3f90a68 | -4.90014 | -47.14485 | 2024-11-23 04:18:00 | NOAA-20 | AÇAILÂNDIA | MARANHÃO | Brasil | 2100055 | 21 | 33 | nan | nan | nan | Amazônia | 2.0 |
| e19c15ac-1ead-3d83-bebd-e92d0401045e | -6.27008 | -44.54963 | 2024-11-23 04:18:00 | NOAA-20 | MIRADOR | MARANHÃO | Brasil | 2106706 | 21 | 33 | nan | nan | nan | Cerrado | 1.2 |
| 34736c57-52c1-3181-8d99-26630eaf9ecc | -3.88822 | -46.6581 | 2024-11-23 04:18:00 | NOAA-20 | BOM JARDIM | MARANHÃO | Brasil | 2102002 | 21 | 33 | nan | nan | nan | Amazônia | 1.4 |
| 5ad87282-8c9f-3c0f-8501-b89dfb51d984 | -4.09046 | -45.96724 | 2024-11-23 04:18:00 | NOAA-20 | SANTA LUZIA | MARANHÃO | Brasil | 2110005 | 21 | 33 | nan | nan | nan | Amazônia | 1.2 |
| aa13bd47-641b-3bbb-8e70-925a20d6a076 | -3.97614 | -49.01109 | 2024-11-23 04:18:00 | NOAA-20 | GOIANÉSIA DO PARÁ | PARÁ | Brasil | 1503093 | 15 | 33 | nan | nan | nan | Amazônia | 1.7 |
| ad821377-abb6-310c-a272-f92d1c0e0bb1 | -4.61497 | -46.50494 | 2024-11-23 04:18:00 | NOAA-20 | BOM JESUS DAS SELVAS | MARANHÃO | Brasil | 2102036 | 21 | 33 | nan | nan | nan | Amazônia | 18.7 |
| f7a0cb77-c892-38e5-a0ce-0f28f47f8899 | -4.0103 | -44.33819 | 2024-11-23 04:18:00 | NOAA-20 | COROATÁ | MARANHÃO | Brasil | 2103604 | 21 | 33 | nan | nan | nan | Cerrado | 1.4 |
| 11da608b-0632-3124-89db-95ed0cb06223 | -3.20957 | -54.24718 | 2024-11-23 04:18:00 | NOAA-20 | SANTARÉM | PARÁ | Brasil | 1506807 | 15 | 33 | nan | nan | nan | Amazônia | 0.9 |
| 639e5ba8-f765-38c8-93d1-6db142b8cf3b | -4.26003 | -48.69735 | 2024-11-23 04:18:00 | NOAA-20 | RONDON DO PARÁ | PARÁ | Brasil | 1506187 | 15 | 33 | nan | nan | nan | Amazônia | 9.1 |
| f9fb569d-0414-36d3-a74e-12d4e2a5c06d | -4.50886 | -44.55771 | 2024-11-23 04:18:00 | NOAA-20 | LIMA CAMPOS | MARANHÃO | Brasil | 2106003 | 21 | 33 | nan | nan | nan | Cerrado | 1.4 |
| 465b2443-09d0-3a68-a51c-745f9c9ab0c2 | -4.01085 | -44.33475 | 2024-11-23 04:18:00 | NOAA-20 | COROATÁ | MARANHÃO | Brasil | 2103604 | 21 | 33 | nan | nan | nan | Cerrado | 2.7 |
| e0a3c2d9-4321-3816-a39f-fe22dfdc605a | -3.90256 | -47.93331 | 2024-11-23 04:18:00 | NOAA-20 | ULIANÓPOLIS | PARÁ | Brasil | 1508126 | 15 | 33 | nan | nan | nan | Amazônia | 4.4 |
| 628fd3c2-05ef-37bd-a396-a0ebded53a15 | -5.43911 | -46.5896 | 2024-11-23 04:18:00 | NOAA-20 | AMARANTE DO MARANHÃO | MARANHÃO | Brasil | 2100600 | 21 | 33 | nan | nan | nan | Cerrado | 1.8 |
| 9fc82dec-19f5-3a8a-9ba2-73333641f1ea | -3.25062 | -54.24976 | 2024-11-23 04:18:00 | NOAA-20 | MOJUÍ DOS CAMPOS | PARÁ | Brasil | 1504752 | 15 | 33 | nan | nan | nan | Amazônia | 1.7 |
| 8a2a955b-6ea8-3d5b-a087-a2b82734ead9 | -6.77722 | -44.0862 | 2024-11-23 04:18:00 | NOAA-20 | NOVA IORQUE | MARANHÃO | Brasil | 2107308 | 21 | 33 | nan | nan | nan | Cerrado | 1.0 |
| 01f42ce4-0696-3e98-9556-f2a0a7d09724 | -2.89421 | -53.04894 | 2024-11-23 04:18:00 | NOAA-20 | MEDICILÂNDIA | PARÁ | Brasil | 1504455 | 15 | 33 | nan | nan | nan | Amazônia | 2.1 |
| 6626dd13-41e5-31ae-9fec-d17228210303 | -7.76094 | -46.22243 | 2024-11-23 04:18:00 | NOAA-20 | BALSAS | MARANHÃO | Brasil | 2101400 | 21 | 33 | nan | nan | nan | Cerrado | 1.0 |
| 594213be-8a0a-34ad-a9dd-0942ebee8a5a | -4.15241 | -50.08585 | 2024-11-23 04:18:00 | NOAA-20 | NOVO REPARTIMENTO | PARÁ | Brasil | 1505064 | 15 | 33 | nan | nan | nan | Amazônia | 2.9 |
| 5823f2a8-218f-3d2c-902e-ef5e8432ed5d | -5.07944 | -44.21333 | 2024-11-23 04:18:00 | NOAA-20 | GOVERNADOR ARCHER | MARANHÃO | Brasil | 2104503 | 21 | 33 | nan | nan | nan | Cerrado | 0.9 |
| 566a5c4f-3013-36cc-9266-fa724e35742a | -6.50446 | -41.4886 | 2024-11-23 04:18:00 | NOAA-20 | LAGOA DO SÍTIO | PIAUÍ | Brasil | 2205599 | 22 | 33 | nan | nan | nan | Caatinga | 0.7 |
| 9f413db0-4f52-3e46-8c6f-61bfb4698fa4 | -4.42983 | -45.76996 | 2024-11-23 04:18:00 | NOAA-20 | BREJO DE AREIA | MARANHÃO | Brasil | 2102150 | 21 | 33 | nan | nan | nan | Amazônia | 1.4 |
| 62815648-0f66-30b5-9710-83bdad3e0d3e | -7.24483 | -46.13639 | 2024-11-23 04:18:00 | NOAA-20 | BALSAS | MARANHÃO | Brasil | 2101400 | 21 | 33 | nan | nan | nan | Cerrado | 1.1 |
| 36bbed72-10a3-3a48-b2d0-403c71f45e1c | -5.75529 | -46.25743 | 2024-11-23 04:18:00 | NOAA-20 | GRAJAÚ | MARANHÃO | Brasil | 2104800 | 21 | 33 | nan | nan | nan | Cerrado | 2.2 |
| 63fd6a21-88ac-32d2-8400-49e3e5956b8f | -5.10447 | -43.16212 | 2024-11-23 04:18:00 | NOAA-20 | CAXIAS | MARANHÃO | Brasil | 2103000 | 21 | 33 | nan | nan | nan | Cerrado | 8.6 |
| c06e63a5-c526-3e26-8698-d5805ed0130b | -3.53496 | -45.21958 | 2024-11-23 04:18:00 | NOAA-20 | MONÇÃO | MARANHÃO | Brasil | 2106904 | 21 | 33 | nan | nan | nan | Amazônia | 3.3 |
| f021b62e-b545-3675-9abf-c576bc9cb77a | -3.17326 | -54.32138 | 2024-11-23 04:18:00 | NOAA-20 | MOJUÍ DOS CAMPOS | PARÁ | Brasil | 1504752 | 15 | 33 | nan | nan | nan | Amazônia | 2.6 |
| d7aa09db-3ce5-35d7-a550-7386a391d5fd | -5.57167 | -46.28847 | 2024-11-23 04:18:00 | NOAA-20 | GRAJAÚ | MARANHÃO | Brasil | 2104800 | 21 | 33 | nan | nan | nan | Cerrado | 4.6 |
| 080982d6-f4cf-3f31-a208-66938a67d4ee | -4.7238 | -45.66796 | 2024-11-23 04:18:00 | NOAA-20 | MARAJÁ DO SENA | MARANHÃO | Brasil | 2106359 | 21 | 33 | nan | nan | nan | Amazônia | 0.8 |
| 6ada18df-aaca-3c31-b537-1f2505c74b0c | -3.79522 | -46.60472 | 2024-11-23 04:18:00 | NOAA-20 | BOM JARDIM | MARANHÃO | Brasil | 2102002 | 21 | 33 | nan | nan | nan | Amazônia | 1.6 |
| 98f59ee6-5ebd-365d-b666-c249a09aa237 | -3.17978 | -54.31812 | 2024-11-23 04:18:00 | NOAA-20 | MOJUÍ DOS CAMPOS | PARÁ | Brasil | 1504752 | 15 | 33 | nan | nan | nan | Amazônia | 2.0 |
| ddc05ee0-7837-38f0-b6dc-13156e90be89 | -5.44599 | -45.58853 | 2024-11-23 04:18:00 | NOAA-20 | JENIPAPO DOS VIEIRAS | MARANHÃO | Brasil | 2105476 | 21 | 33 | nan | nan | nan | Cerrado | 1.2 |
| 7fcbc763-bb7b-3496-9e56-691bc6ee6306 | -4.53904 | -42.91529 | 2024-11-23 04:18:00 | NOAA-20 | CAXIAS | MARANHÃO | Brasil | 2103000 | 21 | 33 | nan | nan | nan | Cerrado | 1.8 |
| 88a6fb17-171a-3223-8455-2b1d5673a2b7 | -4.08912 | -47.03173 | 2024-11-23 04:18:00 | NOAA-20 | ITINGA DO MARANHÃO | MARANHÃO | Brasil | 2105427 | 21 | 33 | nan | nan | nan | Amazônia | 2.9 |
| c6fc0b24-4f4b-3251-a88d-5ce9c962cb0d | -9.73559 | -37.02979 | 2024-11-23 04:18:00 | NOAA-20 | BATALHA | ALAGOAS | Brasil | 2700706 | 27 | 33 | nan | nan | nan | Caatinga | 0.4 |
| a0d95e4c-360d-351c-a557-8c95301532fe | -3.404 | -46.24468 | 2024-11-23 04:18:00 | NOAA-20 | GOVERNADOR NEWTON BELLO | MARANHÃO | Brasil | 2104651 | 21 | 33 | nan | nan | nan | Amazônia | 1.3 |
| d0da833a-36d3-320c-a215-c47e7b457243 | -3.84906 | -43.93516 | 2024-11-23 04:18:00 | NOAA-20 | VARGEM GRANDE | MARANHÃO | Brasil | 2112704 | 21 | 33 | nan | nan | nan | Cerrado | 2.5 |
| c40ecd35-c5d6-3356-a78d-57204c5b69c9 | -7.30375 | -39.6175 | 2024-11-23 04:18:00 | NOAA-20 | SANTANA DO CARIRI | CEARÁ | Brasil | 2312106 | 23 | 33 | nan | nan | nan | Caatinga | 1.2 |
| c81d27e0-0b8f-325b-936c-7b512ed5d77c | -3.9486 | -45.97601 | 2024-11-23 04:18:00 | NOAA-20 | ALTO ALEGRE DO PINDARÉ | MARANHÃO | Brasil | 2100477 | 21 | 33 | nan | nan | nan | Amazônia | 1.5 |
| 784c3015-a65c-3b55-92e0-030b64c6111c | -4.21781 | -46.15795 | 2024-11-23 04:18:00 | NOAA-20 | SANTA LUZIA | MARANHÃO | Brasil | 2110005 | 21 | 33 | nan | nan | nan | Amazônia | 4.5 |
| 73b2b3a0-bb4f-3e3b-bf19-341609a77899 | -3.83522 | -52.25573 | 2024-11-23 04:18:00 | NOAA-20 | SENADOR JOSÉ PORFÍRIO | PARÁ | Brasil | 1507805 | 15 | 33 | nan | nan | nan | Amazônia | 1.0 |
| ede5e0fc-7217-3b4d-aac4-369472c3cb3e | -4.51812 | -46.73009 | 2024-11-23 04:18:00 | NOAA-20 | BOM JESUS DAS SELVAS | MARANHÃO | Brasil | 2102036 | 21 | 33 | nan | nan | nan | Amazônia | 1.2 |
| 6d90dd35-993c-360d-8e5f-c6eda6f00339 | -4.37264 | -47.83179 | 2024-11-23 04:18:00 | NOAA-20 | DOM ELISEU | PARÁ | Brasil | 1502939 | 15 | 33 | nan | nan | nan | Amazônia | 2.3 |
| 40533575-d954-328c-8b81-64f4a81e2a10 | -2.68394 | -52.07325 | 2024-11-23 04:18:00 | NOAA-20 | PORTO DE MOZ | PARÁ | Brasil | 1505908 | 15 | 33 | nan | nan | nan | Amazônia | 7.1 |
| 5b470eff-140c-3d08-a596-8ad21d61f2bf | -5.65931 | -45.80777 | 2024-11-23 04:18:00 | NOAA-20 | GRAJAÚ | MARANHÃO | Brasil | 2104800 | 21 | 33 | nan | nan | nan | Cerrado | 1.6 |
| cb19b22f-4e87-36f8-b6da-4071b47a4375 | -3.89289 | -46.60685 | 2024-11-23 04:18:00 | NOAA-20 | BOM JARDIM | MARANHÃO | Brasil | 2102002 | 21 | 33 | nan | nan | nan | Amazônia | 0.9 |
| b559acef-ec1c-3427-a8e3-2e8a9f09c91a | -3.47138 | -47.69005 | 2024-11-23 04:18:00 | NOAA-20 | PARAGOMINAS | PARÁ | Brasil | 1505502 | 15 | 33 | nan | nan | nan | Amazônia | 2.1 |
| 8d5d4883-106e-3a63-82dc-5134d8f50ea1 | -3.89881 | -47.93274 | 2024-11-23 04:18:00 | NOAA-20 | ULIANÓPOLIS | PARÁ | Brasil | 1508126 | 15 | 33 | nan | nan | nan | Amazônia | 3.2 |
| fe55b9af-64f2-35bb-843d-4287f12f8e4a | -4.14955 | -48.01065 | 2024-11-23 04:18:00 | NOAA-20 | DOM ELISEU | PARÁ | Brasil | 1502939 | 15 | 33 | nan | nan | nan | Amazônia | 1.2 |
| 2da25b15-9400-3b0a-95ee-169391fc1b1c | -4.59203 | -46.07512 | 2024-11-23 04:18:00 | NOAA-20 | SANTA LUZIA | MARANHÃO | Brasil | 2110005 | 21 | 33 | nan | nan | nan | Amazônia | 0.9 |
| 3d97c665-c280-3892-841c-1121906f7174 | -2.99219 | -51.45682 | 2024-11-23 04:18:00 | NOAA-20 | ANAPU | PARÁ | Brasil | 1500859 | 15 | 33 | nan | nan | nan | Amazônia | 4.7 |
| b50bde75-f997-361e-a19f-63d09f44d428 | -3.74966 | -50.00735 | 2024-11-23 04:18:00 | NOAA-20 | PACAJÁ | PARÁ | Brasil | 1505486 | 15 | 33 | nan | nan | nan | Amazônia | 0.9 |
| c99b5919-c3e9-32d8-b7c7-fb757b55de1c | -5.4914 | -46.41743 | 2024-11-23 04:18:00 | NOAA-20 | AMARANTE DO MARANHÃO | MARANHÃO | Brasil | 2100600 | 21 | 33 | nan | nan | nan | Cerrado | 0.9 |
| 187413f5-0083-3257-b36a-49e698bc14f7 | -3.97224 | -46.65463 | 2024-11-23 04:18:00 | NOAA-20 | BOM JARDIM | MARANHÃO | Brasil | 2102002 | 21 | 33 | nan | nan | nan | Amazônia | 1.0 |
| e1a5b39d-6210-3ca2-b5d1-f6e6fe073174 | -3.88985 | -46.67034 | 2024-11-23 04:18:00 | NOAA-20 | BOM JARDIM | MARANHÃO | Brasil | 2102002 | 21 | 33 | nan | nan | nan | Amazônia | 1.2 |
| 33200400-baa3-3678-9962-238717b98a9e | -3.95674 | -46.72545 | 2024-11-23 04:18:00 | NOAA-20 | BOM JARDIM | MARANHÃO | Brasil | 2102002 | 21 | 33 | nan | nan | nan | Amazônia | 1.6 |
| 15995aff-65ee-30cd-8c19-b144423c219c | -4.55896 | -48.02233 | 2024-11-23 04:18:00 | NOAA-20 | RONDON DO PARÁ | PARÁ | Brasil | 1506187 | 15 | 33 | nan | nan | nan | Amazônia | 12.2 |
| 5916b771-53b7-34ca-9b7b-2b30c2c3fbbd | -5.22548 | -43.7373 | 2024-11-23 04:18:00 | NOAA-20 | CAXIAS | MARANHÃO | Brasil | 2103000 | 21 | 33 | nan | nan | nan | Cerrado | 1.7 |
| a7b5bc41-42f9-327e-bbb0-be7afe89c65f | -4.24768 | -49.69154 | 2024-11-23 04:18:00 | NOAA-20 | NOVO REPARTIMENTO | PARÁ | Brasil | 1505064 | 15 | 33 | nan | nan | nan | Amazônia | 4.2 |
| 390bda61-daa8-354f-85f5-a71d86672177 | -4.69357 | -44.39995 | 2024-11-23 04:18:00 | NOAA-20 | CAPINZAL DO NORTE | MARANHÃO | Brasil | 2102754 | 21 | 33 | nan | nan | nan | Cerrado | 1.6 |
| 03cb823a-9b52-325a-8651-4691863b7565 | -4.03597 | -46.66066 | 2024-11-23 04:18:00 | NOAA-20 | BOM JARDIM | MARANHÃO | Brasil | 2102002 | 21 | 33 | nan | nan | nan | Amazônia | 1.0 |
| f0a27b68-ca0a-364a-aa4c-6af39c425492 | -4.34921 | -46.01506 | 2024-11-23 04:18:00 | NOAA-20 | SANTA LUZIA | MARANHÃO | Brasil | 2110005 | 21 | 33 | nan | nan | nan | Amazônia | 1.2 |


[Clique aqui para ver as próximas entradas](README41.md)
