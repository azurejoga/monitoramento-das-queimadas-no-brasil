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

## Dados Diários - Página 15

| ID | Latitude | Longitude | Data/Hora GMT | Satélite | Município | Estado | País | Município ID | Estado ID | País ID | Dias sem Chuva | Precipitação | Risco de Fogo | Bioma | FRP |
|----|----------|-----------|---------------|----------|-----------|--------|------|--------------|-----------|---------|----------------|--------------|----------------|-------|-----|
| c2cbc901-361e-3077-b4c7-6adba898c859 | -5.84435 | -43.41678 | 2025-11-08 04:06:00 | NOAA-21 | PARNARAMA | MARANHÃO | Brasil | 2107803 | 21 | 33 | nan | nan | nan | Cerrado | 2.7 |
| e253415e-306d-3384-ac7c-d248cf1c36b7 | -5.41481 | -44.8276 | 2025-11-08 04:06:00 | NOAA-21 | TUNTUM | MARANHÃO | Brasil | 2112308 | 21 | 33 | nan | nan | nan | Cerrado | 1.9 |
| d6930bd3-7d6e-3e1e-8d68-d74acd7736c7 | -4.807 | -45.39886 | 2025-11-08 04:06:00 | NOAA-21 | LAGOA GRANDE DO MARANHÃO | MARANHÃO | Brasil | 2105963 | 21 | 33 | nan | nan | nan | Cerrado | 1.5 |
| 1027f95d-6459-3828-a01d-8af1ca79e1e0 | -2.98634 | -48.70565 | 2025-11-08 04:06:00 | NOAA-21 | TAILÂNDIA | PARÁ | Brasil | 1507953 | 15 | 33 | nan | nan | nan | Amazônia | 0.9 |
| 051344bf-ae3c-3540-bac9-13096a29ec3c | -3.65471 | -50.26523 | 2025-11-08 04:06:00 | NOAA-21 | PACAJÁ | PARÁ | Brasil | 1505486 | 15 | 33 | nan | nan | nan | Amazônia | 8.6 |
| ee1618b8-c863-3c0a-ada6-feee7639c085 | -3.72929 | -49.6837 | 2025-11-08 04:06:00 | NOAA-21 | TUCURUÍ | PARÁ | Brasil | 1508100 | 15 | 33 | nan | nan | nan | Amazônia | 1.7 |
| 3c6bea78-6fce-3152-9d70-198e9233e4e2 | -7.54441 | -41.66614 | 2025-11-08 04:06:00 | NOAA-21 | ISAÍAS COELHO | PIAUÍ | Brasil | 2204907 | 22 | 33 | nan | nan | nan | Caatinga | 1.9 |
| d6e57273-9311-36d4-b599-f55de0ee3c04 | -6.31933 | -39.69949 | 2025-11-08 04:06:00 | NOAA-21 | ACOPIARA | CEARÁ | Brasil | 2300309 | 23 | 33 | nan | nan | nan | Caatinga | 1.0 |
| ed4d1bbd-ab59-387b-b8a7-a657d466b1d8 | -4.49002 | -46.35938 | 2025-11-08 04:06:00 | NOAA-21 | BURITICUPU | MARANHÃO | Brasil | 2102325 | 21 | 33 | nan | nan | nan | Amazônia | 2.4 |
| 4544d47d-2773-3de5-850c-d1ac61cdb630 | -2.98137 | -48.7048 | 2025-11-08 04:06:00 | NOAA-21 | TAILÂNDIA | PARÁ | Brasil | 1507953 | 15 | 33 | nan | nan | nan | Amazônia | 0.9 |
| 97c33c70-fb88-3560-917b-8b06725d2e87 | -3.9518 | -49.02645 | 2025-11-08 04:06:00 | NOAA-21 | GOIANÉSIA DO PARÁ | PARÁ | Brasil | 1503093 | 15 | 33 | nan | nan | nan | Amazônia | 2.0 |
| 88f9650a-d060-39bb-9611-84af696ebdf0 | -3.90971 | -50.04585 | 2025-11-08 04:06:00 | NOAA-21 | PACAJÁ | PARÁ | Brasil | 1505486 | 15 | 33 | nan | nan | nan | Amazônia | 4.1 |
| 556bbdf9-da06-3686-bf46-3aac097b1e48 | -4.90749 | -46.70389 | 2025-11-08 04:06:00 | NOAA-21 | AMARANTE DO MARANHÃO | MARANHÃO | Brasil | 2100600 | 21 | 33 | nan | nan | nan | Amazônia | 1.0 |
| beda6a71-7003-340d-bd7b-69fff89b0bf0 | -3.03086 | -50.26966 | 2025-11-08 04:06:00 | NOAA-21 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 3.4 |
| 80bc2381-c314-3af5-8d3e-6d0625ee28dc | -3.55829 | -50.81126 | 2025-11-08 04:06:00 | NOAA-21 | PACAJÁ | PARÁ | Brasil | 1505486 | 15 | 33 | nan | nan | nan | Amazônia | 0.9 |
| 29d7567a-15f7-3af4-bd91-417f0bc96a95 | -3.32647 | -53.36404 | 2025-11-08 04:06:00 | NOAA-21 | MEDICILÂNDIA | PARÁ | Brasil | 1504455 | 15 | 33 | nan | nan | nan | Amazônia | 6.9 |
| 95317d46-4830-3d40-b13f-c5876112e33e | -4.68671 | -46.40697 | 2025-11-08 04:06:00 | NOAA-21 | BURITICUPU | MARANHÃO | Brasil | 2102325 | 21 | 33 | nan | nan | nan | Amazônia | 4.4 |
| f372029c-b003-3ab6-8f2f-c24698782a5a | -3.35274 | -53.22752 | 2025-11-08 04:06:00 | NOAA-21 | MEDICILÂNDIA | PARÁ | Brasil | 1504455 | 15 | 33 | nan | nan | nan | Amazônia | 2.2 |
| 0b3c50df-ca1a-3940-8492-2a9e6bad43ba | -3.14981 | -50.30328 | 2025-11-08 04:06:00 | NOAA-21 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 2.1 |
| 43d74347-09f2-3e02-b00e-08fbb7491e02 | -7.3814 | -43.53531 | 2025-11-08 04:06:00 | NOAA-21 | CANAVIEIRA | PIAUÍ | Brasil | 2202251 | 22 | 33 | nan | nan | nan | Cerrado | 1.4 |
| a2cda7b8-40ec-3f95-80bd-851e2d749eb5 | -3.3458 | -50.18053 | 2025-11-08 04:06:00 | NOAA-21 | PACAJÁ | PARÁ | Brasil | 1505486 | 15 | 33 | nan | nan | nan | Amazônia | 2.2 |
| 9334a95e-d48b-300b-afb2-808e00ac678b | -5.84557 | -43.40918 | 2025-11-08 04:06:00 | NOAA-21 | PARNARAMA | MARANHÃO | Brasil | 2107803 | 21 | 33 | nan | nan | nan | Cerrado | 5.3 |
| 1e9229b4-0b0b-3e4f-9093-a506fa36e70d | -3.51742 | -49.26405 | 2025-11-08 04:06:00 | NOAA-21 | BREU BRANCO | PARÁ | Brasil | 1501782 | 15 | 33 | nan | nan | nan | Amazônia | 1.1 |
| e0def7ff-fe14-36ec-9dbc-60a0986f2412 | -5.47691 | -39.77773 | 2025-11-08 04:06:00 | NOAA-21 | PEDRA BRANCA | CEARÁ | Brasil | 2310506 | 23 | 33 | nan | nan | nan | Caatinga | 1.5 |
| 8a7c9f78-4a2f-3fab-be15-27dd516d08ec | -3.28068 | -46.50897 | 2025-11-08 04:06:00 | NOAA-21 | CENTRO NOVO DO MARANHÃO | MARANHÃO | Brasil | 2103174 | 21 | 33 | nan | nan | nan | Amazônia | 0.8 |
| 001597ec-1934-3b50-b95c-7083e82cdea0 | -6.09852 | -41.70853 | 2025-11-08 04:06:00 | NOAA-21 | AROAZES | PIAUÍ | Brasil | 2200905 | 22 | 33 | nan | nan | nan | Caatinga | 1.8 |
| 2ff0da1d-920a-3637-92ab-acb737676f92 | -4.59198 | -45.98832 | 2025-11-08 04:06:00 | NOAA-21 | SANTA LUZIA | MARANHÃO | Brasil | 2110005 | 21 | 33 | nan | nan | nan | Amazônia | 3.2 |
| cb6e34be-ad6c-3777-9880-b4622dbe3bb4 | -4.69697 | -45.85825 | 2025-11-08 04:06:00 | NOAA-21 | ARAME | MARANHÃO | Brasil | 2100956 | 21 | 33 | nan | nan | nan | Amazônia | 1.9 |
| e245532e-636a-3892-87ac-882c06c534ee | -4.11473 | -48.01128 | 2025-11-08 04:06:00 | NOAA-21 | DOM ELISEU | PARÁ | Brasil | 1502939 | 15 | 33 | nan | nan | nan | Amazônia | 5.1 |
| b2135000-25cb-303b-81a6-4dd1223fb5be | -4.11392 | -48.01619 | 2025-11-08 04:06:00 | NOAA-21 | DOM ELISEU | PARÁ | Brasil | 1502939 | 15 | 33 | nan | nan | nan | Amazônia | 5.1 |
| 6e2b907e-7637-3781-b866-a67689e42457 | -4.27861 | -46.4026 | 2025-11-08 04:06:00 | NOAA-21 | BURITICUPU | MARANHÃO | Brasil | 2102325 | 21 | 33 | nan | nan | nan | Amazônia | 3.4 |
| 5833cb48-489b-3b87-bf39-4b4a9e5fd8e3 | -4.03837 | -50.4465 | 2025-11-08 04:06:00 | NOAA-21 | NOVO REPARTIMENTO | PARÁ | Brasil | 1505064 | 15 | 33 | nan | nan | nan | Amazônia | 3.5 |
| ee6cebbc-d664-3a30-beeb-5b3ee6a00a4c | -4.47164 | -45.33294 | 2025-11-08 04:06:00 | NOAA-21 | PAULO RAMOS | MARANHÃO | Brasil | 2108108 | 21 | 33 | nan | nan | nan | Amazônia | 9.4 |
| 883f1d7b-e34f-3dd2-8f07-5752e4aff0fb | -3.03583 | -50.3074 | 2025-11-08 04:06:00 | NOAA-21 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 2.2 |
| 2e68aea4-faaf-3981-9151-1ce8fce52274 | -4.55172 | -46.16107 | 2025-11-08 04:06:00 | NOAA-21 | SANTA LUZIA | MARANHÃO | Brasil | 2110005 | 21 | 33 | nan | nan | nan | Amazônia | 0.7 |
| 9ecb9f95-7513-3d94-a6e3-b55720b8c926 | -5.64881 | -43.01495 | 2025-11-08 04:06:00 | NOAA-21 | PALMEIRAIS | PIAUÍ | Brasil | 2207504 | 22 | 33 | nan | nan | nan | Caatinga | 1.1 |
| d6b9a91b-d834-3ce7-810d-dd7e933e5558 | -3.0493 | -50.2613 | 2025-11-08 04:06:00 | NOAA-21 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 1.8 |
| e3b1ae9f-314f-3c94-8fed-ef294a376faa | -2.93438 | -48.77051 | 2025-11-08 04:06:00 | NOAA-21 | TAILÂNDIA | PARÁ | Brasil | 1507953 | 15 | 33 | nan | nan | nan | Amazônia | 4.1 |
| c810c221-07d9-3392-93ac-8d4ab2b78061 | -3.3228 | -49.13386 | 2025-11-08 04:06:00 | NOAA-21 | MOJU | PARÁ | Brasil | 1504703 | 15 | 33 | nan | nan | nan | Amazônia | 2.2 |
| 5eb41d19-f94b-3ab8-9e3a-6443d55dd531 | -6.10015 | -41.69816 | 2025-11-08 04:06:00 | NOAA-21 | AROAZES | PIAUÍ | Brasil | 2200905 | 22 | 33 | nan | nan | nan | Caatinga | 2.5 |
| 3b66ad57-45ac-3811-80ec-2da883f3f7a8 | -4.82559 | -48.06782 | 2025-11-08 04:06:00 | NOAA-21 | VILA NOVA DOS MARTÍRIOS | MARANHÃO | Brasil | 2112852 | 21 | 33 | nan | nan | nan | Amazônia | 1.7 |
| 5e796e40-b05a-34b5-90e9-43a4732f0101 | -5.90929 | -44.52867 | 2025-11-08 04:06:00 | NOAA-21 | COLINAS | MARANHÃO | Brasil | 2103505 | 21 | 33 | nan | nan | nan | Cerrado | 6.2 |
| 51ea7345-7948-3484-b986-a8be7caf9795 | -3.09064 | -50.31978 | 2025-11-08 04:06:00 | NOAA-21 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 3.2 |
| 2b4dc545-9e0e-3501-a275-f95559c6652b | -5.61219 | -41.08037 | 2025-11-08 04:06:00 | NOAA-21 | SÃO MIGUEL DO TAPUIO | PIAUÍ | Brasil | 2210409 | 22 | 33 | nan | nan | nan | Caatinga | 2.8 |
| 9d6ac45e-ffe8-3d57-8256-09893b6faabe | -7.13212 | -40.64485 | 2025-11-08 04:06:00 | NOAA-21 | FRONTEIRAS | PIAUÍ | Brasil | 2204303 | 22 | 33 | nan | nan | nan | Caatinga | 1.3 |
| f61c51c7-49fd-3983-9416-adf07c6efe0c | -4.22934 | -46.89547 | 2025-11-08 04:06:00 | NOAA-21 | BOM JARDIM | MARANHÃO | Brasil | 2102002 | 21 | 33 | nan | nan | nan | Amazônia | 2.2 |
| 86f6fa66-077d-3441-827b-498adbd70acd | -3.25233 | -50.13586 | 2025-11-08 04:06:00 | NOAA-21 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 1.7 |
| 80f7f731-132f-3d9d-b1fa-2ca62f7e6e3e | -5.93644 | -38.19038 | 2025-11-08 04:06:00 | NOAA-21 | ERERÊ | CEARÁ | Brasil | 2304277 | 23 | 33 | nan | nan | nan | Caatinga | 3.9 |
| 32ebc9da-7e20-355a-b6e9-63ad1843c2d9 | -5.77889 | -40.79592 | 2025-11-08 04:06:00 | NOAA-21 | QUITERIANÓPOLIS | CEARÁ | Brasil | 2311264 | 23 | 33 | nan | nan | nan | Caatinga | 2.3 |
| 8266b4af-5e18-3c6b-a277-543d11e0e8df | -6.15129 | -43.29916 | 2025-11-08 04:06:00 | NOAA-21 | SÃO FRANCISCO DO MARANHÃO | MARANHÃO | Brasil | 2110906 | 21 | 33 | nan | nan | nan | Caatinga | 1.3 |
| 7323f450-86b4-3076-ab5b-ba4b09498366 | -3.33687 | -50.20064 | 2025-11-08 04:06:00 | NOAA-21 | PACAJÁ | PARÁ | Brasil | 1505486 | 15 | 33 | nan | nan | nan | Amazônia | 3.9 |
| 7de9b0b0-0ba8-3000-ae8c-556b1e912f8c | -3.35318 | -50.20884 | 2025-11-08 04:06:00 | NOAA-21 | PACAJÁ | PARÁ | Brasil | 1505486 | 15 | 33 | nan | nan | nan | Amazônia | 6.8 |
| a7252528-1639-3d82-a74b-bb0e2ada9f88 | -5.02046 | -48.36792 | 2025-11-08 04:06:00 | NOAA-21 | ABEL FIGUEIREDO | PARÁ | Brasil | 1500131 | 15 | 33 | nan | nan | nan | Amazônia | 1.5 |
| 37cd08df-39ce-3cb1-b982-3e84a7e0ec62 | -4.9845 | -43.57104 | 2025-11-08 04:06:00 | NOAA-21 | SÃO JOÃO DO SOTER | MARANHÃO | Brasil | 2111078 | 21 | 33 | nan | nan | nan | Cerrado | 2.1 |
| 4426ac91-1fb3-3982-934e-0559fab36393 | -3.0205 | -49.43721 | 2025-11-08 04:06:00 | NOAA-21 | MOJU | PARÁ | Brasil | 1504703 | 15 | 33 | nan | nan | nan | Amazônia | 2.1 |
| 4bc4ca7a-d48c-379c-9a54-52f16528aed0 | -4.5949 | -45.99593 | 2025-11-08 04:06:00 | NOAA-21 | SANTA LUZIA | MARANHÃO | Brasil | 2110005 | 21 | 33 | nan | nan | nan | Amazônia | 28.7 |
| 2899c839-6d8d-3a94-9619-5786cbffe7fe | -3.91031 | -50.0424 | 2025-11-08 04:06:00 | NOAA-21 | PACAJÁ | PARÁ | Brasil | 1505486 | 15 | 33 | nan | nan | nan | Amazônia | 3.7 |
| 41146bd8-cd96-34f2-938c-ec056a9e6f6d | -7.2145 | -35.0152 | 2025-11-08 04:06:00 | NOAA-21 | SANTA RITA | PARAÍBA | Brasil | 2513703 | 25 | 33 | nan | nan | nan | Mata Atlântica | 2.3 |
| 17cdd098-20c7-393a-b6ff-45f909c7f1d8 | -3.78046 | -45.76987 | 2025-11-08 04:06:00 | NOAA-21 | ALTO ALEGRE DO PINDARÉ | MARANHÃO | Brasil | 2100477 | 21 | 33 | nan | nan | nan | Amazônia | 1.8 |
| 3c9d2199-3791-3269-8491-45c0dbb3831c | -6.69778 | -40.77023 | 2025-11-08 04:06:00 | NOAA-21 | PIO IX | PIAUÍ | Brasil | 2208205 | 22 | 33 | nan | nan | nan | Caatinga | 1.3 |
| ccd5bfc8-0e49-320f-881a-c1b736a6cd2d | -4.16655 | -46.71582 | 2025-11-08 04:06:00 | NOAA-21 | BOM JARDIM | MARANHÃO | Brasil | 2102002 | 21 | 33 | nan | nan | nan | Amazônia | 1.0 |
| 6a3ac2fc-c3ab-38d0-b442-a0078dcd9041 | -3.56765 | -50.4136 | 2025-11-08 04:06:00 | NOAA-21 | PACAJÁ | PARÁ | Brasil | 1505486 | 15 | 33 | nan | nan | nan | Amazônia | 2.0 |
| ed6387de-6206-391b-8bd4-42f714140829 | -8.0288 | -38.53275 | 2025-11-08 04:06:00 | NOAA-21 | SERRA TALHADA | PERNAMBUCO | Brasil | 2613909 | 26 | 33 | nan | nan | nan | Caatinga | 18.0 |
| b828781d-c0a2-3c18-ab16-9b6231855a3d | -6.22332 | -47.01748 | 2025-11-08 04:06:00 | NOAA-21 | PORTO FRANCO | MARANHÃO | Brasil | 2109007 | 21 | 33 | nan | nan | nan | Cerrado | 1.0 |
| 7c9aeb01-e25b-3eea-a1d2-e47534a33fd1 | -4.98104 | -44.81945 | 2025-11-08 04:06:00 | NOAA-21 | JOSELÂNDIA | MARANHÃO | Brasil | 2105609 | 21 | 33 | nan | nan | nan | Cerrado | 1.3 |
| 2cc1da7d-fa41-324b-a811-02299716e062 | -5.93898 | -38.18318 | 2025-11-08 04:06:00 | NOAA-21 | ERERÊ | CEARÁ | Brasil | 2304277 | 23 | 33 | nan | nan | nan | Caatinga | 4.3 |
| 09a42f46-ca1e-3672-827d-974af266134b | -7.49064 | -40.12252 | 2025-11-08 04:06:00 | NOAA-21 | BODOCÓ | PERNAMBUCO | Brasil | 2602001 | 26 | 33 | nan | nan | nan | Caatinga | 2.0 |
| adedcdde-d1e1-35cb-8474-47eee59dbfdd | -11.20296 | -53.83442 | 2025-11-08 04:08:00 | NOAA-21 | MARCELÂNDIA | MATO GROSSO | Brasil | 5105580 | 51 | 33 | nan | nan | nan | Amazônia | 2.5 |
| 2220531b-1e94-3e0e-a620-a6703b383aaa | -8.06967 | -47.12411 | 2025-11-08 04:08:00 | NOAA-21 | GOIATINS | TOCANTINS | Brasil | 1709005 | 17 | 33 | nan | nan | nan | Cerrado | 2.3 |
| c7f386d3-175e-3f70-bf33-40ef7375a1b9 | -7.46191 | -46.63703 | 2025-11-08 04:08:00 | NOAA-21 | RIACHÃO | MARANHÃO | Brasil | 2109502 | 21 | 33 | nan | nan | nan | Cerrado | 1.0 |
| 2c9e0d71-fdc8-399f-843d-6f74617a0836 | -7.03833 | -46.98539 | 2025-11-08 04:08:00 | NOAA-21 | CAROLINA | MARANHÃO | Brasil | 2102804 | 21 | 33 | nan | nan | nan | Cerrado | 7.0 |
| e9862211-12ff-3111-8554-0a833f448c65 | -10.81352 | -44.34526 | 2025-11-08 04:08:00 | NOAA-21 | SANTA RITA DE CÁSSIA | BAHIA | Brasil | 2928406 | 29 | 33 | nan | nan | nan | Cerrado | 2.8 |
| 88691551-ed37-3b0e-96b5-a6bef8b95bb9 | -10.9956 | -53.98673 | 2025-11-08 04:08:00 | NOAA-21 | MARCELÂNDIA | MATO GROSSO | Brasil | 5105580 | 51 | 33 | nan | nan | nan | Amazônia | 1.8 |
| cbe1840b-5bb7-346a-86d0-9f50289205fc | -8.20668 | -46.98166 | 2025-11-08 04:08:00 | NOAA-21 | CAMPOS LINDOS | TOCANTINS | Brasil | 1703842 | 17 | 33 | nan | nan | nan | Cerrado | 1.5 |
| e0a7835b-7721-3ace-a4c7-978d768bd0e7 | -9.11404 | -44.67941 | 2025-11-08 04:08:00 | NOAA-21 | BOM JESUS | PIAUÍ | Brasil | 2201903 | 22 | 33 | nan | nan | nan | Cerrado | 1.7 |
| 9b96d806-5841-3a3e-a4a5-c1a84a328444 | -8.06905 | -47.12775 | 2025-11-08 04:08:00 | NOAA-21 | GOIATINS | TOCANTINS | Brasil | 1709005 | 17 | 33 | nan | nan | nan | Cerrado | 2.0 |
| d9b5ab90-facd-39a3-9097-56b0d2e2cae3 | -9.15522 | -51.3032 | 2025-11-08 04:08:00 | NOAA-21 | CUMARU DO NORTE | PARÁ | Brasil | 1502764 | 15 | 33 | nan | nan | nan | Amazônia | 1.3 |
| e97cdc5d-585a-3900-a60b-81d38b04d2e3 | -10.26619 | -49.04449 | 2025-11-08 04:08:00 | NOAA-21 | CHAPADA DE AREIA | TOCANTINS | Brasil | 1704600 | 17 | 33 | nan | nan | nan | Cerrado | 1.4 |
| 75acd9c4-5e1a-3f51-9d74-9ef5ef798f57 | -7.53465 | -47.3853 | 2025-11-08 04:08:00 | NOAA-21 | CAROLINA | MARANHÃO | Brasil | 2102804 | 21 | 33 | nan | nan | nan | Cerrado | 2.4 |
| 67d0d652-10a1-3308-8db8-c267ccb4333b | -8.49306 | -44.72573 | 2025-11-08 04:08:00 | NOAA-21 | PALMEIRA DO PIAUÍ | PIAUÍ | Brasil | 2207405 | 22 | 33 | nan | nan | nan | Cerrado | 1.3 |
| c60be3b8-218a-3550-8c90-c2776441b849 | -8.20728 | -46.97808 | 2025-11-08 04:08:00 | NOAA-21 | CAMPOS LINDOS | TOCANTINS | Brasil | 1703842 | 17 | 33 | nan | nan | nan | Cerrado | 1.5 |
| 173923f0-661f-32f0-a137-a44a593d273d | -9.87883 | -44.57909 | 2025-11-08 04:08:00 | NOAA-21 | PARNAGUÁ | PIAUÍ | Brasil | 2207603 | 22 | 33 | nan | nan | nan | Cerrado | 0.6 |
| cfe0a230-8296-3e2c-94ef-c9d6ea8a2156 | -9.32367 | -47.83101 | 2025-11-08 04:08:00 | NOAA-21 | PEDRO AFONSO | TOCANTINS | Brasil | 1716505 | 17 | 33 | nan | nan | nan | Cerrado | 2.3 |
| f16c951f-5b7e-388a-9d91-6d8056d2ffa2 | -7.11453 | -46.48283 | 2025-11-08 04:08:00 | NOAA-21 | RIACHÃO | MARANHÃO | Brasil | 2109502 | 21 | 33 | nan | nan | nan | Cerrado | 0.9 |
| 380fa71a-df57-36c9-aec5-9af99150523e | -11.19995 | -53.82458 | 2025-11-08 04:08:00 | NOAA-21 | MARCELÂNDIA | MATO GROSSO | Brasil | 5105580 | 51 | 33 | nan | nan | nan | Amazônia | 4.4 |
| 216e8143-2272-3261-951c-23fc8d8821af | -10.11155 | -47.51271 | 2025-11-08 04:08:00 | NOAA-21 | NOVO ACORDO | TOCANTINS | Brasil | 1715101 | 17 | 33 | nan | nan | nan | Cerrado | 1.0 |
| 816824ae-166f-3823-97d8-560d1509e91d | -9.78179 | -42.04178 | 2025-11-08 04:08:00 | NOAA-21 | SENTO SÉ | BAHIA | Brasil | 2930204 | 29 | 33 | nan | nan | nan | Caatinga | 2.0 |
| 5297d29c-e74e-31c8-8c76-cddf232709ba | -8.33585 | -46.25691 | 2025-11-08 04:08:00 | NOAA-21 | BALSAS | MARANHÃO | Brasil | 2101400 | 21 | 33 | nan | nan | nan | Cerrado | 1.2 |
| 77e946a1-9ab6-3c16-9a22-bfe229beba9b | -7.08981 | -48.31199 | 2025-11-08 04:08:00 | NOAA-21 | CARMOLÂNDIA | TOCANTINS | Brasil | 1703883 | 17 | 33 | nan | nan | nan | Amazônia | 3.1 |
| db394f6d-1c8d-33c0-9b88-ddf418935014 | -7.03595 | -46.9854 | 2025-11-08 04:08:00 | NOAA-21 | CAROLINA | MARANHÃO | Brasil | 2102804 | 21 | 33 | nan | nan | nan | Cerrado | 6.8 |
| 65cac947-77f7-3a82-aa29-754cf95e0759 | -10.23075 | -44.80487 | 2025-11-08 04:08:00 | NOAA-21 | RIACHO FRIO | PIAUÍ | Brasil | 2208858 | 22 | 33 | nan | nan | nan | Cerrado | 1.1 |
| 282a2881-8d5f-3b84-aba7-d52d7e7967f4 | -7.56872 | -45.86282 | 2025-11-08 04:08:00 | NOAA-21 | BALSAS | MARANHÃO | Brasil | 2101400 | 21 | 33 | nan | nan | nan | Cerrado | 2.5 |
| 7010c2a1-aae6-3650-b2a4-63dfbb6c308c | -8.91811 | -47.81138 | 2025-11-08 04:08:00 | NOAA-21 | SANTA MARIA DO TOCANTINS | TOCANTINS | Brasil | 1718881 | 17 | 33 | nan | nan | nan | Cerrado | 1.4 |
| 4b432535-89f3-38f2-9de9-02b785feb3cf | -7.55391 | -47.24864 | 2025-11-08 04:08:00 | NOAA-21 | CAROLINA | MARANHÃO | Brasil | 2102804 | 21 | 33 | nan | nan | nan | Cerrado | 1.6 |
| 7d8b86f6-f22f-3bc0-aa83-d8deb2ee123b | -8.93698 | -40.86826 | 2025-11-08 04:08:00 | NOAA-21 | CASA NOVA | BAHIA | Brasil | 2907202 | 29 | 33 | nan | nan | nan | Caatinga | 1.2 |
| a23afce4-4128-343b-9c31-25bfb24eef90 | -11.19867 | -53.82422 | 2025-11-08 04:08:00 | NOAA-21 | MARCELÂNDIA | MATO GROSSO | Brasil | 5105580 | 51 | 33 | nan | nan | nan | Amazônia | 4.4 |
| 810571a7-d2de-3bcc-9134-c8a01025fe51 | -8.3008 | -40.32014 | 2025-11-08 04:08:00 | NOAA-21 | SANTA CRUZ | PERNAMBUCO | Brasil | 2612455 | 26 | 33 | nan | nan | nan | Caatinga | 0.5 |
| 0ae47b8c-5010-34a4-864a-2c5c39f4da1f | -7.79765 | -46.6551 | 2025-11-08 04:08:00 | NOAA-21 | RIACHÃO | MARANHÃO | Brasil | 2109502 | 21 | 33 | nan | nan | nan | Cerrado | 1.6 |
| 7678ebca-b9a7-33f7-8eeb-5fc9bdfdbb6c | -7.42214 | -46.652 | 2025-11-08 04:08:00 | NOAA-21 | RIACHÃO | MARANHÃO | Brasil | 2109502 | 21 | 33 | nan | nan | nan | Cerrado | 1.2 |
| 31137334-dd53-3e75-9b3a-4f0826074b06 | -10.357 | -47.33228 | 2025-11-08 04:08:00 | NOAA-21 | NOVO ACORDO | TOCANTINS | Brasil | 1715101 | 17 | 33 | nan | nan | nan | Cerrado | 1.5 |


[Clique aqui para ver as próximas entradas](README16.md)
