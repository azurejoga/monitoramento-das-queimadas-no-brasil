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

## Dados Diários - Página 6

| ID | Latitude | Longitude | Data/Hora GMT | Satélite | Município | Estado | País | Município ID | Estado ID | País ID | Dias sem Chuva | Precipitação | Risco de Fogo | Bioma | FRP |
|----|----------|-----------|---------------|----------|-----------|--------|------|--------------|-----------|---------|----------------|--------------|----------------|-------|-----|
| 4dc39381-06a2-3f79-9f47-45023f60a6ce | -12.03273 | -47.80402 | 2026-06-11 04:12:00 | NPP-375D | NATIVIDADE | TOCANTINS | Brasil | 1714203 | 17 | 33 | nan | nan | nan | Cerrado | 1.3 |
| de92bb42-5943-3234-aed8-205486afda0b | -11.87294 | -47.10036 | 2026-06-11 04:12:00 | NPP-375D | DIANÓPOLIS | TOCANTINS | Brasil | 1707009 | 17 | 33 | nan | nan | nan | Cerrado | 1.9 |
| a7c75070-0184-3998-9af2-609779a95b89 | -17.70074 | -45.52052 | 2026-06-11 04:14:00 | NPP-375D | JOÃO PINHEIRO | MINAS GERAIS | Brasil | 3136306 | 31 | 33 | nan | nan | nan | Cerrado | 1.0 |
| 66481f72-4944-3f3c-ad02-56689461d3b4 | -13.53446 | -47.80628 | 2026-06-11 04:14:00 | NPP-375D | CAVALCANTE | GOIÁS | Brasil | 5205307 | 52 | 33 | nan | nan | nan | Cerrado | 0.3 |
| ffa8b55d-0c2f-3437-a496-a51473bd2eec | -20.61582 | -42.89152 | 2026-06-11 04:14:00 | NPP-375D | TEIXEIRAS | MINAS GERAIS | Brasil | 3168507 | 31 | 33 | nan | nan | nan | Mata Atlântica | 0.6 |
| 4a802f5e-e0ac-3f4d-b9b3-5534239e89d5 | -14.99875 | -39.71182 | 2026-06-11 04:14:00 | NPP-375D | ITAJU DO COLÔNIA | BAHIA | Brasil | 2915403 | 29 | 33 | nan | nan | nan | Mata Atlântica | 1.0 |
| 507f7feb-4233-36fd-9a5f-3819aaa594e9 | -17.797 | -44.5737 | 2026-06-11 04:14:00 | NPP-375D | LASSANCE | MINAS GERAIS | Brasil | 3138104 | 31 | 33 | nan | nan | nan | Cerrado | 2.1 |
| 29fb14df-b7c8-39f8-9796-7aa7e0160ef2 | -13.53872 | -47.80716 | 2026-06-11 04:14:00 | NPP-375D | CAVALCANTE | GOIÁS | Brasil | 5205307 | 52 | 33 | nan | nan | nan | Cerrado | 1.2 |
| 1ee3676f-c0d0-3cf1-8fb7-f28691f70aaf | -19.0749 | -42.0004 | 2026-06-11 04:14:00 | NPP-375D | ENGENHEIRO CALDAS | MINAS GERAIS | Brasil | 3123700 | 31 | 33 | nan | nan | nan | Mata Atlântica | 0.8 |
| 69b1d7d0-21b1-38c0-b2c3-3520f9ddb0ba | -17.60208 | -44.61049 | 2026-06-11 04:14:00 | NPP-375D | VÁRZEA DA PALMA | MINAS GERAIS | Brasil | 3170800 | 31 | 33 | nan | nan | nan | Cerrado | 0.5 |
| c7b6c88b-96f1-3a0b-b24f-93a50455b033 | -20.2568 | -41.85368 | 2026-06-11 04:14:00 | NPP-375D | MARTINS SOARES | MINAS GERAIS | Brasil | 3140530 | 31 | 33 | nan | nan | nan | Mata Atlântica | 0.5 |
| 3c4fb111-374b-37b4-85a4-4684d4ef867e | -14.72215 | -43.12455 | 2026-06-11 04:14:00 | NPP-375D | ESPINOSA | MINAS GERAIS | Brasil | 3124302 | 31 | 33 | nan | nan | nan | Caatinga | 0.6 |
| cea259d3-a76f-3f61-9cc8-e8bc63ac9a1c | -13.94741 | -46.17541 | 2026-06-11 04:14:00 | NPP-375D | CORRENTINA | BAHIA | Brasil | 2909307 | 29 | 33 | nan | nan | nan | Cerrado | 2.5 |
| da398691-b8e0-358f-93d3-09f79ea2704d | -15.18017 | -43.8492 | 2026-06-11 04:14:00 | NPP-375D | JAÍBA | MINAS GERAIS | Brasil | 3135050 | 31 | 33 | nan | nan | nan | Cerrado | 1.5 |
| 20feea29-9e28-39e6-9514-a0bdef08006e | -20.03975 | -43.37705 | 2026-06-11 04:14:00 | NPP-375D | CATAS ALTAS | MINAS GERAIS | Brasil | 3115359 | 31 | 33 | nan | nan | nan | Mata Atlântica | 0.8 |
| e6809094-ce90-352f-b49a-79b5a376ae40 | -13.53375 | -47.8102 | 2026-06-11 04:14:00 | NPP-375D | CAVALCANTE | GOIÁS | Brasil | 5205307 | 52 | 33 | nan | nan | nan | Cerrado | 1.1 |
| b6b24b38-02a5-3dcc-a6c5-a1e3f35fc884 | -15.17613 | -43.85236 | 2026-06-11 04:14:00 | NPP-375D | JAÍBA | MINAS GERAIS | Brasil | 3135050 | 31 | 33 | nan | nan | nan | Cerrado | 1.1 |
| 28e17765-f921-3244-a180-b291350bca6f | -17.79358 | -44.57306 | 2026-06-11 04:14:00 | NPP-375D | LASSANCE | MINAS GERAIS | Brasil | 3138104 | 31 | 33 | nan | nan | nan | Cerrado | 2.1 |
| 55fe8f55-e9cf-3f50-847d-d9a4429db622 | -14.99817 | -39.71578 | 2026-06-11 04:14:00 | NPP-375D | ITAJU DO COLÔNIA | BAHIA | Brasil | 2915403 | 29 | 33 | nan | nan | nan | Mata Atlântica | 0.6 |
| 32f2299d-27a0-35b5-a637-1a4a8d2b59a5 | -13.54648 | -47.81297 | 2026-06-11 04:14:00 | NPP-375D | CAVALCANTE | GOIÁS | Brasil | 5205307 | 52 | 33 | nan | nan | nan | Cerrado | 3.2 |
| c3d4aa01-ea66-329f-97e2-f760092d31ca | -15.17954 | -43.85296 | 2026-06-11 04:14:00 | NPP-375D | JAÍBA | MINAS GERAIS | Brasil | 3135050 | 31 | 33 | nan | nan | nan | Cerrado | 1.1 |
| 31964deb-2604-3f2b-87d4-4752eec84420 | -19.05423 | -40.2591 | 2026-06-11 04:14:00 | NPP-375D | SOORETAMA | ESPÍRITO SANTO | Brasil | 3205010 | 32 | 33 | nan | nan | nan | Mata Atlântica | 1.1 |
| ec615cdb-e627-3c6b-968c-53e688c9ff0f | -13.96018 | -46.19284 | 2026-06-11 04:14:00 | NPP-375D | CORRENTINA | BAHIA | Brasil | 2909307 | 29 | 33 | nan | nan | nan | Cerrado | 1.0 |
| 09c30ab7-0350-3913-8428-90e647849ef2 | -13.54296 | -47.80811 | 2026-06-11 04:14:00 | NPP-375D | CAVALCANTE | GOIÁS | Brasil | 5205307 | 52 | 33 | nan | nan | nan | Cerrado | 1.2 |
| f5caf4ee-9281-3cc0-b8c8-9effea5a006a | -9.3234 | -45.4787 | 2026-06-11 04:20:00 | GOES-19 | SANTA FILOMENA | PIAUÍ | Brasil | 2209203 | 22 | 33 | nan | nan | nan | Cerrado | 66.8 |
| 1f4b4d23-70a5-3bd0-8be6-24f6cc1f9922 | -5.52083 | -37.48286 | 2026-06-11 04:27:00 | NOAA-20 | GOVERNADOR DIX-SEPT ROSADO | RIO GRANDE DO NORTE | Brasil | 2404309 | 24 | 33 | nan | nan | nan | Caatinga | 1.6 |
| 1b16c90a-2baf-36ca-b8cd-2b825efeddc1 | -0.08985 | -51.27912 | 2026-06-11 04:27:00 | NOAA-20 | MAZAGÃO | AMAPÁ | Brasil | 1600402 | 16 | 33 | nan | nan | nan | Amazônia | 1.4 |
| 0f8275a8-6f9c-3ee8-a200-09fea1ceffa7 | -4.42282 | -41.63476 | 2026-06-11 04:27:00 | NOAA-20 | PIRIPIRI | PIAUÍ | Brasil | 2208403 | 22 | 33 | nan | nan | nan | Caatinga | 2.0 |
| 01048ea4-953a-3ebe-b237-20bc0cafa2fb | -5.61051 | -37.53119 | 2026-06-11 04:27:00 | NOAA-20 | CARAÚBAS | RIO GRANDE DO NORTE | Brasil | 2402303 | 24 | 33 | nan | nan | nan | Caatinga | 1.5 |
| 38af8ef0-5ec5-3f4b-b9bd-ddeee13d181d | -5.52039 | -37.48598 | 2026-06-11 04:27:00 | NOAA-20 | GOVERNADOR DIX-SEPT ROSADO | RIO GRANDE DO NORTE | Brasil | 2404309 | 24 | 33 | nan | nan | nan | Caatinga | 1.6 |
| 5496a595-e8c9-3e3c-b901-eb9be11ae277 | -5.93341 | -43.48719 | 2026-06-11 04:29:00 | NOAA-20 | LAGOA DO MATO | MARANHÃO | Brasil | 2105922 | 21 | 33 | nan | nan | nan | Cerrado | 4.9 |
| a36f2542-b831-33b7-8f1b-ea3b09b45f22 | -5.93402 | -43.48322 | 2026-06-11 04:29:00 | NOAA-20 | LAGOA DO MATO | MARANHÃO | Brasil | 2105922 | 21 | 33 | nan | nan | nan | Cerrado | 4.0 |
| d36cd2c2-ef53-3826-b7d8-a5e92bdf6d2b | -5.11048 | -46.94835 | 2026-06-11 04:29:00 | NOAA-20 | JOÃO LISBOA | MARANHÃO | Brasil | 2105500 | 21 | 33 | nan | nan | nan | Amazônia | 1.2 |
| 51768080-44dd-3838-9642-2ec9189e68a7 | -6.19382 | -44.86347 | 2026-06-11 04:29:00 | NOAA-20 | MIRADOR | MARANHÃO | Brasil | 2106706 | 21 | 33 | nan | nan | nan | Cerrado | 0.9 |
| 45078c16-d04d-335b-be17-d7bc869aeabd | -6.72706 | -39.27568 | 2026-06-11 04:29:00 | NOAA-20 | VÁRZEA ALEGRE | CEARÁ | Brasil | 2314003 | 23 | 33 | nan | nan | nan | Caatinga | 3.0 |
| fa8ddf21-c9f9-3f97-8518-66898ecad912 | -6.57643 | -47.91634 | 2026-06-11 04:29:00 | NOAA-20 | DARCINÓPOLIS | TOCANTINS | Brasil | 1706506 | 17 | 33 | nan | nan | nan | Cerrado | 1.8 |
| 18300e17-6057-3656-8f3b-49b1f4b12741 | -5.72894 | -49.10223 | 2026-06-11 04:29:00 | NOAA-20 | MARABÁ | PARÁ | Brasil | 1504208 | 15 | 33 | nan | nan | nan | Amazônia | 2.0 |
| 6509c2db-bd16-3583-aae8-0d08a7b051b5 | -6.19045 | -44.86294 | 2026-06-11 04:29:00 | NOAA-20 | MIRADOR | MARANHÃO | Brasil | 2106706 | 21 | 33 | nan | nan | nan | Cerrado | 2.0 |
| d52917ac-388c-3385-b7c5-88f8662a2a57 | -6.46446 | -46.8956 | 2026-06-11 04:29:00 | NOAA-20 | SÃO JOÃO DO PARAÍSO | MARANHÃO | Brasil | 2111052 | 21 | 33 | nan | nan | nan | Cerrado | 0.6 |
| c9396577-41d1-3a26-a262-bc3293624a97 | -6.4365 | -44.56627 | 2026-06-11 04:29:00 | NOAA-20 | MIRADOR | MARANHÃO | Brasil | 2106706 | 21 | 33 | nan | nan | nan | Cerrado | 1.1 |
| ed5df9b1-a6dc-30b2-8740-d30dbb00172d | -6.56687 | -47.91103 | 2026-06-11 04:29:00 | NOAA-20 | DARCINÓPOLIS | TOCANTINS | Brasil | 1706506 | 17 | 33 | nan | nan | nan | Cerrado | 4.3 |
| 9dccbaeb-4377-33b5-ad02-f9b1423ae001 | -6.44103 | -44.55951 | 2026-06-11 04:29:00 | NOAA-20 | MIRADOR | MARANHÃO | Brasil | 2106706 | 21 | 33 | nan | nan | nan | Cerrado | 3.5 |
| 7864ec69-3a02-388b-9381-ce8090023f67 | -6.72861 | -39.27314 | 2026-06-11 04:29:00 | NOAA-20 | VÁRZEA ALEGRE | CEARÁ | Brasil | 2314003 | 23 | 33 | nan | nan | nan | Caatinga | 4.4 |
| 42d58f7d-8f96-34d2-b037-77a6296273a8 | -6.95729 | -44.55013 | 2026-06-11 04:29:00 | NOAA-20 | SÃO DOMINGOS DO AZEITÃO | MARANHÃO | Brasil | 2110658 | 21 | 33 | nan | nan | nan | Cerrado | 3.9 |
| bd18c783-192b-38e6-9ee4-3119ec2063bc | -5.95064 | -49.42313 | 2026-06-11 04:29:00 | NOAA-20 | ELDORADO DO CARAJÁS | PARÁ | Brasil | 1502954 | 15 | 33 | nan | nan | nan | Amazônia | 1.5 |
| b92442e7-526b-3952-9fb9-0a85b2c58426 | -6.95387 | -44.54962 | 2026-06-11 04:29:00 | NOAA-20 | SÃO DOMINGOS DO AZEITÃO | MARANHÃO | Brasil | 2110658 | 21 | 33 | nan | nan | nan | Cerrado | 3.9 |
| 6f243de8-a83d-38ae-80a2-b99583cf6daf | -5.16034 | -45.21666 | 2026-06-11 04:29:00 | NOAA-20 | BARRA DO CORDA | MARANHÃO | Brasil | 2101608 | 21 | 33 | nan | nan | nan | Cerrado | 0.8 |
| 8fc1be99-190f-3b84-b1c4-b36a3b491f76 | -6.44726 | -44.56426 | 2026-06-11 04:29:00 | NOAA-20 | MIRADOR | MARANHÃO | Brasil | 2106706 | 21 | 33 | nan | nan | nan | Cerrado | 3.5 |
| 0c7ab756-2d68-385f-97b1-75a7ae6ec7c5 | -5.7296 | -49.09816 | 2026-06-11 04:29:00 | NOAA-20 | MARABÁ | PARÁ | Brasil | 1504208 | 15 | 33 | nan | nan | nan | Amazônia | 2.0 |
| 0ad58cfc-6818-3268-a958-c9a08c5d8e46 | -5.04497 | -43.2664 | 2026-06-11 04:29:00 | NOAA-20 | CAXIAS | MARANHÃO | Brasil | 2103000 | 21 | 33 | nan | nan | nan | Cerrado | 1.4 |
| 59ae5074-52fe-361a-a3af-5fa5c240f08b | -6.2566 | -47.34807 | 2026-06-11 04:29:00 | NOAA-20 | PORTO FRANCO | MARANHÃO | Brasil | 2109007 | 21 | 33 | nan | nan | nan | Cerrado | 1.1 |
| 327d562c-717a-3f68-ab60-d2697a31b498 | -6.44783 | -44.56059 | 2026-06-11 04:29:00 | NOAA-20 | MIRADOR | MARANHÃO | Brasil | 2106706 | 21 | 33 | nan | nan | nan | Cerrado | 3.5 |
| 31330049-f4b6-386c-a4ec-4c1fec5d5030 | -6.57305 | -47.9158 | 2026-06-11 04:29:00 | NOAA-20 | DARCINÓPOLIS | TOCANTINS | Brasil | 1706506 | 17 | 33 | nan | nan | nan | Cerrado | 1.8 |
| 6e4962b5-0e03-339c-9241-8c1dc014f8e8 | -6.4399 | -44.56682 | 2026-06-11 04:29:00 | NOAA-20 | MIRADOR | MARANHÃO | Brasil | 2106706 | 21 | 33 | nan | nan | nan | Cerrado | 1.1 |
| 54ec5d68-7ddc-3b7d-95b6-626daf661f99 | -6.57245 | -47.91949 | 2026-06-11 04:29:00 | NOAA-20 | DARCINÓPOLIS | TOCANTINS | Brasil | 1706506 | 17 | 33 | nan | nan | nan | Cerrado | 1.5 |
| 0f2db1bc-c452-359b-b90c-a217a26878c9 | -6.44046 | -44.56316 | 2026-06-11 04:29:00 | NOAA-20 | MIRADOR | MARANHÃO | Brasil | 2106706 | 21 | 33 | nan | nan | nan | Cerrado | 3.5 |
| a3839dec-a92c-39bf-b2ea-165771347d1c | -6.18709 | -44.8624 | 2026-06-11 04:29:00 | NOAA-20 | MIRADOR | MARANHÃO | Brasil | 2106706 | 21 | 33 | nan | nan | nan | Cerrado | 2.0 |
| e4bda6dd-2df3-3c74-9c36-b9178279f096 | -6.43707 | -44.56261 | 2026-06-11 04:29:00 | NOAA-20 | MIRADOR | MARANHÃO | Brasil | 2106706 | 21 | 33 | nan | nan | nan | Cerrado | 3.5 |
| 303012da-239b-314e-b58a-278fc4937999 | -5.04205 | -43.26189 | 2026-06-11 04:29:00 | NOAA-20 | CAXIAS | MARANHÃO | Brasil | 2103000 | 21 | 33 | nan | nan | nan | Cerrado | 3.1 |
| 64e0c4ce-9971-3789-aaa2-9de8e258bc3f | -6.44443 | -44.56005 | 2026-06-11 04:29:00 | NOAA-20 | MIRADOR | MARANHÃO | Brasil | 2106706 | 21 | 33 | nan | nan | nan | Cerrado | 3.5 |
| 07a38d2f-c50f-3d07-aaba-46e0d2f959d1 | -6.72775 | -39.27075 | 2026-06-11 04:29:00 | NOAA-20 | VÁRZEA ALEGRE | CEARÁ | Brasil | 2314003 | 23 | 33 | nan | nan | nan | Caatinga | 3.1 |
| ccfd0394-28ac-3be4-9f10-3e89fa43cc48 | -6.99684 | -43.86258 | 2026-06-11 04:29:00 | NOAA-20 | MARCOS PARENTE | PIAUÍ | Brasil | 2206001 | 22 | 33 | nan | nan | nan | Cerrado | 2.1 |
| 24eff6e9-bcc3-3a75-ac6d-9a87e749ab8e | -5.83588 | -43.4858 | 2026-06-11 04:29:00 | NOAA-20 | PARNARAMA | MARANHÃO | Brasil | 2107803 | 21 | 33 | nan | nan | nan | Cerrado | 1.2 |
| 7b045336-fcdb-3df6-b9ad-8812b45c9d62 | -6.95445 | -44.54588 | 2026-06-11 04:29:00 | NOAA-20 | SÃO DOMINGOS DO AZEITÃO | MARANHÃO | Brasil | 2110658 | 21 | 33 | nan | nan | nan | Cerrado | 3.9 |
| 9b1a1598-559a-32f4-964d-4cba813acb4d | -6.57702 | -47.91267 | 2026-06-11 04:29:00 | NOAA-20 | DARCINÓPOLIS | TOCANTINS | Brasil | 1706506 | 17 | 33 | nan | nan | nan | Cerrado | 1.8 |
| 22ac6ef1-0beb-3ad4-a420-f03e1c4d24f6 | -6.44386 | -44.56371 | 2026-06-11 04:29:00 | NOAA-20 | MIRADOR | MARANHÃO | Brasil | 2106706 | 21 | 33 | nan | nan | nan | Cerrado | 3.5 |
| 7b6f27ae-9918-3338-a11c-4e8077a54dd6 | -6.44329 | -44.56737 | 2026-06-11 04:29:00 | NOAA-20 | MIRADOR | MARANHÃO | Brasil | 2106706 | 21 | 33 | nan | nan | nan | Cerrado | 1.1 |
| 1cf036c4-79a7-368e-bd03-23445607f229 | -6.44669 | -44.56792 | 2026-06-11 04:29:00 | NOAA-20 | MIRADOR | MARANHÃO | Brasil | 2106706 | 21 | 33 | nan | nan | nan | Cerrado | 1.1 |
| 200fbc21-0735-320d-9864-75cb16ca4e36 | -6.43763 | -44.55896 | 2026-06-11 04:29:00 | NOAA-20 | MIRADOR | MARANHÃO | Brasil | 2106706 | 21 | 33 | nan | nan | nan | Cerrado | 3.5 |
| fe8040e9-f404-3de3-98b7-c5740a07dce0 | -5.83648 | -43.48185 | 2026-06-11 04:29:00 | NOAA-20 | PARNARAMA | MARANHÃO | Brasil | 2107803 | 21 | 33 | nan | nan | nan | Cerrado | 1.2 |
| 05db3c11-3ec8-3a4d-842a-5846e3c9a5fe | -5.16312 | -45.22067 | 2026-06-11 04:29:00 | NOAA-20 | BARRA DO CORDA | MARANHÃO | Brasil | 2101608 | 21 | 33 | nan | nan | nan | Cerrado | 0.8 |
| d2ff4acd-47d1-3a3f-bc47-4f8f769ec205 | -6.45065 | -44.5648 | 2026-06-11 04:29:00 | NOAA-20 | MIRADOR | MARANHÃO | Brasil | 2106706 | 21 | 33 | nan | nan | nan | Cerrado | 1.3 |
| f5bd56a6-6cd3-3e46-90cb-c18b1ccdc0b3 | -5.29399 | -43.95724 | 2026-06-11 04:29:00 | NOAA-20 | SENADOR ALEXANDRE COSTA | MARANHÃO | Brasil | 2111748 | 21 | 33 | nan | nan | nan | Cerrado | 1.8 |
| db9369b8-048c-3a6e-a7e9-6459505dec10 | -9.29933 | -45.46876 | 2026-06-11 04:29:00 | NOAA-20 | SANTA FILOMENA | PIAUÍ | Brasil | 2209203 | 22 | 33 | nan | nan | nan | Cerrado | 0.7 |
| 7a5b06e2-f75e-3554-863d-4d110d093f1c | -7.62843 | -50.04395 | 2026-06-11 04:29:00 | NOAA-20 | RIO MARIA | PARÁ | Brasil | 1506161 | 15 | 33 | nan | nan | nan | Amazônia | 1.7 |
| 2d305637-8f27-3475-95d8-82db6f500931 | -9.31055 | -48.96839 | 2026-06-11 04:29:00 | NOAA-20 | DOIS IRMÃOS DO TOCANTINS | TOCANTINS | Brasil | 1707207 | 17 | 33 | nan | nan | nan | Cerrado | 2.3 |
| ea15c1a0-5974-35cd-a9f2-815319385c0e | -10.38943 | -46.6282 | 2026-06-11 04:29:00 | NOAA-20 | MATEIROS | TOCANTINS | Brasil | 1712702 | 17 | 33 | nan | nan | nan | Cerrado | 0.8 |
| 50ae0d95-1446-377f-89ef-60e992dcc376 | -7.60208 | -46.47016 | 2026-06-11 04:29:00 | NOAA-20 | RIACHÃO | MARANHÃO | Brasil | 2109502 | 21 | 33 | nan | nan | nan | Cerrado | 2.5 |
| 965acf8b-f59d-3624-b1a1-29731dbca5a4 | -9.21399 | -47.9146 | 2026-06-11 04:29:00 | NOAA-20 | PEDRO AFONSO | TOCANTINS | Brasil | 1716505 | 17 | 33 | nan | nan | nan | Cerrado | 4.8 |
| b1dad07a-2490-32de-82c9-00f9aecd61bd | -9.32747 | -45.488 | 2026-06-11 04:29:00 | NOAA-20 | SANTA FILOMENA | PIAUÍ | Brasil | 2209203 | 22 | 33 | nan | nan | nan | Cerrado | 2.5 |
| 0ed4b231-d8f4-36bd-85a0-5ab4838ba189 | -9.62502 | -49.01983 | 2026-06-11 04:29:00 | NOAA-20 | ABREULÂNDIA | TOCANTINS | Brasil | 1700251 | 17 | 33 | nan | nan | nan | Cerrado | 0.9 |
| 34f85775-5544-3d27-a113-7e6678afb0b5 | -9.21342 | -47.91815 | 2026-06-11 04:29:00 | NOAA-20 | PEDRO AFONSO | TOCANTINS | Brasil | 1716505 | 17 | 33 | nan | nan | nan | Cerrado | 2.0 |
| 29774447-e305-3c47-ae87-fc66b4b8acbc | -8.98382 | -48.0925 | 2026-06-11 04:29:00 | NOAA-20 | BOM JESUS DO TOCANTINS | TOCANTINS | Brasil | 1703305 | 17 | 33 | nan | nan | nan | Cerrado | 5.1 |
| 282e5a55-6210-3a95-af46-5b3698bf46c1 | -9.32859 | -45.48073 | 2026-06-11 04:29:00 | NOAA-20 | SANTA FILOMENA | PIAUÍ | Brasil | 2209203 | 22 | 33 | nan | nan | nan | Cerrado | 1.6 |
| d33b89e1-f049-3766-a19b-1e2cd5b452c9 | -7.24732 | -49.54008 | 2026-06-11 04:29:00 | NOAA-20 | RIO MARIA | PARÁ | Brasil | 1506161 | 15 | 33 | nan | nan | nan | Amazônia | 0.6 |
| a2477d36-038c-3d67-90b7-618e11f5cbf6 | -9.53145 | -47.75541 | 2026-06-11 04:29:00 | NOAA-20 | RIO SONO | TOCANTINS | Brasil | 1718758 | 17 | 33 | nan | nan | nan | Cerrado | 1.6 |
| 8bb23657-dd83-38b8-84ec-db4fc7b571fd | -10.3828 | -46.62712 | 2026-06-11 04:29:00 | NOAA-20 | MATEIROS | TOCANTINS | Brasil | 1712702 | 17 | 33 | nan | nan | nan | Cerrado | 1.3 |
| 4aec09a1-a8b9-3181-a7a6-dc67961668ac | -9.11358 | -47.96378 | 2026-06-11 04:29:00 | NOAA-20 | BOM JESUS DO TOCANTINS | TOCANTINS | Brasil | 1703305 | 17 | 33 | nan | nan | nan | Cerrado | 1.0 |
| 1f9dc2d1-6643-3729-8465-55b4f752c336 | -7.87255 | -47.10017 | 2026-06-11 04:29:00 | NOAA-20 | CAROLINA | MARANHÃO | Brasil | 2102804 | 21 | 33 | nan | nan | nan | Cerrado | 0.9 |
| d118c983-4914-3e49-9a2b-0b7a6e23014a | -9.32634 | -45.47293 | 2026-06-11 04:29:00 | NOAA-20 | SANTA FILOMENA | PIAUÍ | Brasil | 2209203 | 22 | 33 | nan | nan | nan | Cerrado | 0.9 |
| 77684b59-78fa-3dcf-94d6-446e8f399390 | -9.11415 | -47.96024 | 2026-06-11 04:29:00 | NOAA-20 | BOM JESUS DO TOCANTINS | TOCANTINS | Brasil | 1703305 | 17 | 33 | nan | nan | nan | Cerrado | 1.0 |
| fe88db7f-afed-39f5-8f7b-ed0a020b3e2e | -9.32073 | -45.48695 | 2026-06-11 04:29:00 | NOAA-20 | SANTA FILOMENA | PIAUÍ | Brasil | 2209203 | 22 | 33 | nan | nan | nan | Cerrado | 7.0 |
| 7ab1f388-c1cc-3789-9433-6978870c1a1b | -9.46907 | -49.1338 | 2026-06-11 04:29:00 | NOAA-20 | DOIS IRMÃOS DO TOCANTINS | TOCANTINS | Brasil | 1707207 | 17 | 33 | nan | nan | nan | Cerrado | 0.5 |
| b714ae08-c863-38a5-8ebb-f32e4d0992ea | -9.31903 | -45.47552 | 2026-06-11 04:29:00 | NOAA-20 | SANTA FILOMENA | PIAUÍ | Brasil | 2209203 | 22 | 33 | nan | nan | nan | Cerrado | 12.1 |
| 07941618-6e41-338d-9faa-e668ddb582e5 | -9.32466 | -45.48384 | 2026-06-11 04:29:00 | NOAA-20 | SANTA FILOMENA | PIAUÍ | Brasil | 2209203 | 22 | 33 | nan | nan | nan | Cerrado | 7.0 |
| 667929ed-f51e-3b74-aaae-5d5299e28d6f | -7.62915 | -50.03962 | 2026-06-11 04:29:00 | NOAA-20 | RIO MARIA | PARÁ | Brasil | 1506161 | 15 | 33 | nan | nan | nan | Amazônia | 1.7 |
| 635c827e-e250-3339-a646-bafe2fca9f76 | -9.31565 | -45.47499 | 2026-06-11 04:29:00 | NOAA-20 | SANTA FILOMENA | PIAUÍ | Brasil | 2209203 | 22 | 33 | nan | nan | nan | Cerrado | 12.1 |
| 35cb6a46-2f92-3c20-b3aa-f3834e1dc430 | -7.59877 | -46.46964 | 2026-06-11 04:29:00 | NOAA-20 | RIACHÃO | MARANHÃO | Brasil | 2109502 | 21 | 33 | nan | nan | nan | Cerrado | 2.5 |
| cbe2b915-08fe-36b1-9eea-95cdbecf2aeb | -9.30608 | -45.4698 | 2026-06-11 04:29:00 | NOAA-20 | SANTA FILOMENA | PIAUÍ | Brasil | 2209203 | 22 | 33 | nan | nan | nan | Cerrado | 2.8 |
| ebdecd0d-0c94-3c8f-bbfb-30ed43615b8e | -9.30552 | -45.47343 | 2026-06-11 04:29:00 | NOAA-20 | SANTA FILOMENA | PIAUÍ | Brasil | 2209203 | 22 | 33 | nan | nan | nan | Cerrado | 2.2 |


[Clique aqui para ver as próximas entradas](README7.md)
