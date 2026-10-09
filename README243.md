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

## Dados Diários - Página 243

| ID | Latitude | Longitude | Data/Hora GMT | Satélite | Município | Estado | País | Município ID | Estado ID | País ID | Dias sem Chuva | Precipitação | Risco de Fogo | Bioma | FRP |
|----|----------|-----------|---------------|----------|-----------|--------|------|--------------|-----------|---------|----------------|--------------|----------------|-------|-----|
| 202a7a8b-8073-3ef5-85de-a73329f14f76 | -14.4535 | -43.9359 | 2026-10-09 14:20:00 | GOES-19 | JUVENÍLIA | MINAS GERAIS | Brasil | 3136959 | 31 | 33 | nan | nan | nan | Cerrado | 189.3 |
| 5e86bc06-dd7d-3964-8e7f-08fd1fdc0e36 | -9.8798 | -50.4918 | 2026-10-09 14:20:00 | GOES-19 | SANTA TEREZINHA | MATO GROSSO | Brasil | 5107776 | 51 | 33 | nan | nan | nan | Amazônia | 67.4 |
| 2f3bffe8-13ce-327c-9ede-041cb61a4657 | -11.2259 | -45.3064 | 2026-10-09 14:20:00 | GOES-19 | FORMOSA DO RIO PRETO | BAHIA | Brasil | 2911105 | 29 | 33 | nan | nan | nan | Cerrado | 238.8 |
| b3c7e5f9-d2d5-3704-8781-d4bbb3b9880c | -8.9964 | -45.9002 | 2026-10-09 14:20:00 | GOES-19 | SANTA FILOMENA | PIAUÍ | Brasil | 2209203 | 22 | 33 | nan | nan | nan | Cerrado | 123.3 |
| ee0dbec4-685f-352e-8afc-9a1b2aeab205 | -11.7674 | -44.9522 | 2026-10-09 14:20:00 | GOES-19 | RIACHÃO DAS NEVES | BAHIA | Brasil | 2926202 | 29 | 33 | nan | nan | nan | Cerrado | 99.7 |
| f40a881c-03c0-3711-a6a4-c02506751c16 | 3.9309 | -61.0906 | 2026-10-09 14:20:00 | GOES-19 | AMAJARI | RORAIMA | Brasil | 1400027 | 14 | 33 | nan | nan | nan | Amazônia | 63.3 |
| 4a4732f8-5465-3df7-b34e-1b89bf1ffaa9 | -18.3327 | -42.3849 | 2026-10-09 14:20:00 | GOES-19 | SANTA MARIA DO SUAÇUÍ | MINAS GERAIS | Brasil | 3158201 | 31 | 33 | nan | nan | nan | Mata Atlântica | 160.7 |
| 9dcf6b40-2499-3ab0-86be-0b7eaed892b5 | -3.8786 | -44.1265 | 2026-10-09 14:20:00 | GOES-19 | COROATÁ | MARANHÃO | Brasil | 2103604 | 21 | 33 | nan | nan | nan | Cerrado | 93.4 |
| 0c5d5814-b1cd-317f-8605-87a726f6b4b0 | -7.4694 | -42.8551 | 2026-10-09 14:20:00 | GOES-19 | ITAUEIRA | PIAUÍ | Brasil | 2205102 | 22 | 33 | nan | nan | nan | Caatinga | 131.6 |
| d8025a4a-183b-393e-a23d-2f276194a178 | -4.0835 | -44.1618 | 2026-10-09 14:20:00 | GOES-19 | COROATÁ | MARANHÃO | Brasil | 2103604 | 21 | 33 | nan | nan | nan | Cerrado | 178.9 |
| 31431557-7483-3830-8d6e-cf1c38d58ee0 | -12.8582 | -50.5662 | 2026-10-09 14:20:00 | GOES-19 | COCALINHO | MATO GROSSO | Brasil | 5103106 | 51 | 33 | nan | nan | nan | Cerrado | 44.4 |
| e1c7768e-ed46-312a-bbcf-bb75ebf66005 | -7.4886 | -42.8295 | 2026-10-09 14:20:00 | GOES-19 | ITAUEIRA | PIAUÍ | Brasil | 2205102 | 22 | 33 | nan | nan | nan | Caatinga | 128.0 |
| 90bd350c-3983-32e7-b3ac-75633120fe8b | -6.4568 | -55.4609 | 2026-10-09 14:20:00 | GOES-19 | ITAITUBA | PARÁ | Brasil | 1503606 | 15 | 33 | nan | nan | nan | Amazônia | 59.3 |
| 72c15b48-18a2-354b-b765-29d9bdf64b26 | -15.2541 | -42.3495 | 2026-10-09 14:20:00 | GOES-19 | MONTEZUMA | MINAS GERAIS | Brasil | 3143450 | 31 | 33 | nan | nan | nan | Mata Atlântica | 169.6 |
| 5a724d8e-5a86-3387-8fcc-f7b4c6807342 | -6.7365 | -55.1474 | 2026-10-09 14:20:00 | GOES-19 | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 80.4 |
| a00c620b-1646-3be1-9976-9237c07648e9 | -6.7366 | -55.1274 | 2026-10-09 14:20:00 | GOES-19 | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 65.5 |
| 52e6dad0-492a-368b-a972-f6f7528b44ae | 1.6754 | -55.6463 | 2026-10-09 14:20:00 | GOES-19 | ÓBIDOS | PARÁ | Brasil | 1505106 | 15 | 33 | nan | nan | nan | Amazônia | 63.4 |
| 266feb46-6cf7-34e0-b7b8-189a5e83dcad | -14.0238 | -48.7714 | 2026-10-09 14:20:00 | GOES-19 | URUAÇU | GOIÁS | Brasil | 5221601 | 52 | 33 | nan | nan | nan | Cerrado | 156.9 |
| 3808c5f7-42a9-3b5f-a277-78b977830ef6 | -9.1012 | -45.1393 | 2026-10-09 14:20:00 | GOES-19 | BOM JESUS | PIAUÍ | Brasil | 2201903 | 22 | 33 | nan | nan | nan | Cerrado | 123.1 |
| 5911c77f-4ce6-31b3-b9ee-f8be10af2dde | -10.8789 | -45.5368 | 2026-10-09 14:20:00 | GOES-19 | FORMOSA DO RIO PRETO | BAHIA | Brasil | 2911105 | 29 | 33 | nan | nan | nan | Cerrado | 101.5 |
| 3f63d3c8-9f0c-39a5-8009-2b6fd28e7463 | -3.8198 | -44.6095 | 2026-10-09 14:20:00 | GOES-19 | MATÕES DO NORTE | MARANHÃO | Brasil | 2106631 | 21 | 33 | nan | nan | nan | Cerrado | 105.5 |
| 57bcee0e-28d8-3c59-ac26-de1c75718bbb | -11.245 | -45.3037 | 2026-10-09 14:20:00 | GOES-19 | FORMOSA DO RIO PRETO | BAHIA | Brasil | 2911105 | 29 | 33 | nan | nan | nan | Cerrado | 322.2 |
| 9a2f0649-3c33-3eca-945f-df8b0836423a | -4.0838 | -44.1159 | 2026-10-09 14:20:00 | GOES-19 | COROATÁ | MARANHÃO | Brasil | 2103604 | 21 | 33 | nan | nan | nan | Cerrado | 96.8 |
| e29f87a6-941e-3b71-bcdf-67bd14db87be | -10.472 | -47.2556 | 2026-10-09 14:20:00 | GOES-19 | PONTE ALTA DO TOCANTINS | TOCANTINS | Brasil | 1717909 | 17 | 33 | nan | nan | nan | Cerrado | 122.8 |
| e10da5b8-2c97-3c3b-b136-2d8dca07ab1c | -6.4413 | -55.0224 | 2026-10-09 14:20:00 | GOES-19 | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 56.8 |
| c1e048d8-52f7-39a2-8d9a-fbb2beb40127 | -9.9398 | -43.5542 | 2026-10-09 14:20:00 | GOES-19 | PILÃO ARCADO | BAHIA | Brasil | 2924405 | 29 | 33 | nan | nan | nan | Cerrado | 140.2 |
| b7f116c8-542b-30da-bd58-dfab1fb61829 | -12.1964 | -57.1303 | 2026-10-09 14:20:00 | GOES-19 | NOVA MARINGÁ | MATO GROSSO | Brasil | 5108907 | 51 | 33 | nan | nan | nan | Amazônia | 66.3 |
| 1fc88adb-f936-315c-a128-e75de071eaa0 | -12.2149 | -44.6057 | 2026-10-09 14:20:00 | GOES-19 | CATOLÂNDIA | BAHIA | Brasil | 2907400 | 29 | 33 | nan | nan | nan | Cerrado | 213.1 |
| 3df00319-7a8f-320f-ba4e-dcf8c68aef9a | -8.9775 | -45.9023 | 2026-10-09 14:20:00 | GOES-19 | SANTA FILOMENA | PIAUÍ | Brasil | 2209203 | 22 | 33 | nan | nan | nan | Cerrado | 165.6 |
| 3a354ef4-3bb5-336a-9792-aede5d44a804 | -14.3608 | -55.032 | 2026-10-09 14:20:00 | GOES-19 | ROSÁRIO OESTE | MATO GROSSO | Brasil | 5107701 | 51 | 33 | nan | nan | nan | Cerrado | 157.0 |
| 7a709cf9-4723-36d9-9497-be4d9351017b | -4.0837 | -44.1389 | 2026-10-09 14:20:00 | GOES-19 | COROATÁ | MARANHÃO | Brasil | 2103604 | 21 | 33 | nan | nan | nan | Cerrado | 124.8 |
| 7c013768-3717-3a5b-acf9-f267c53d76cc | -12.1967 | -57.1103 | 2026-10-09 14:20:00 | GOES-19 | NOVA MARINGÁ | MATO GROSSO | Brasil | 5108907 | 51 | 33 | nan | nan | nan | Amazônia | 59.5 |
| 2297b759-8ef2-37ea-9c89-2018b1043bc0 | -9.8817 | -44.8632 | 2026-10-09 14:20:00 | GOES-19 | RIACHO FRIO | PIAUÍ | Brasil | 2208858 | 22 | 33 | nan | nan | nan | Cerrado | 152.2 |
| a4968dec-4085-3d6f-a064-bfb359bfdd55 | -6.9328 | -43.6799 | 2026-10-09 14:20:00 | GOES-19 | GUADALUPE | PIAUÍ | Brasil | 2204501 | 22 | 33 | nan | nan | nan | Cerrado | 120.0 |
| 54d618fb-16f0-39b2-9748-33cfd5e25244 | -8.5124 | -46.9128 | 2026-10-09 14:20:00 | GOES-19 | RECURSOLÂNDIA | TOCANTINS | Brasil | 1718501 | 17 | 33 | nan | nan | nan | Cerrado | 62.7 |
| c7eb126e-3993-3839-9d56-1ae3caf539ec | -14.4345 | -43.9157 | 2026-10-09 14:20:00 | GOES-19 | JUVENÍLIA | MINAS GERAIS | Brasil | 3136959 | 31 | 33 | nan | nan | nan | Cerrado | 128.2 |
| 45a90408-2c63-38af-9c95-2a7b9c196bf5 | -9.9794 | -45.9462 | 2026-10-09 14:20:00 | GOES-19 | ALTO PARNAÍBA | MARANHÃO | Brasil | 2100501 | 21 | 33 | nan | nan | nan | Cerrado | 114.7 |
| 219537ab-09b1-36c0-9119-333b58dfd300 | -3.86 | -44.1274 | 2026-10-09 14:20:00 | GOES-19 | COROATÁ | MARANHÃO | Brasil | 2103604 | 21 | 33 | nan | nan | nan | Cerrado | 100.6 |
| 4cf0759f-f1be-36c5-b324-0648474170f5 | -11.8779 | -47.4115 | 2026-10-09 14:20:00 | GOES-19 | ALMAS | TOCANTINS | Brasil | 1700400 | 17 | 33 | nan | nan | nan | Cerrado | 111.8 |
| 1bbdd6e9-a7a2-317f-9e08-c74094d1566a | -8.5313 | -46.911 | 2026-10-09 14:20:00 | GOES-19 | RECURSOLÂNDIA | TOCANTINS | Brasil | 1718501 | 17 | 33 | nan | nan | nan | Cerrado | 84.3 |
| 312a6132-414e-33b2-b918-0b462b652199 | -6.8615 | -55.799 | 2026-10-09 14:20:00 | GOES-19 | NOVO PROGRESSO | PARÁ | Brasil | 1505031 | 15 | 33 | nan | nan | nan | Amazônia | 59.7 |
| 81e1dc91-af5b-3e76-9e69-447720caa620 | -7.1151 | -42.5358 | 2026-10-09 14:20:00 | GOES-19 | SÃO FRANCISCO DO PIAUÍ | PIAUÍ | Brasil | 2209708 | 22 | 33 | nan | nan | nan | Caatinga | 104.6 |
| b4a32f61-0419-34a7-a5ca-1f8429b48eae | -11.6787 | -46.7664 | 2026-10-09 14:20:00 | GOES-19 | DIANÓPOLIS | TOCANTINS | Brasil | 1707009 | 17 | 33 | nan | nan | nan | Cerrado | 82.3 |
| d5d5dfc0-255a-3183-b83b-68c15ff0a531 | -7.3054 | -43.9931 | 2026-10-09 14:20:00 | GOES-19 | LANDRI SALES | PIAUÍ | Brasil | 2205607 | 22 | 33 | nan | nan | nan | Cerrado | 120.4 |
| 0e96ffb5-eee7-319a-89f7-3b89332a7c30 | -14.3611 | -55.0114 | 2026-10-09 14:20:00 | GOES-19 | ROSÁRIO OESTE | MATO GROSSO | Brasil | 5107701 | 51 | 33 | nan | nan | nan | Cerrado | 118.5 |
| b063ad08-97ee-3a03-b6b5-955d5b6f2c7e | -3.8788 | -44.1035 | 2026-10-09 14:20:00 | GOES-19 | COROATÁ | MARANHÃO | Brasil | 2103604 | 21 | 33 | nan | nan | nan | Cerrado | 103.1 |
| 76a12255-f153-3a93-8fab-5fae2ecccd5f | -6.4598 | -55.0215 | 2026-10-09 14:20:00 | GOES-19 | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 57.3 |
| 62576c63-28f5-36d0-891e-0dec131a04b9 | -7.3909 | -44.7445 | 2026-10-09 14:20:00 | GOES-19 | URUÇUÍ | PIAUÍ | Brasil | 2211209 | 22 | 33 | nan | nan | nan | Cerrado | 82.2 |
| 34e02f88-6d6a-3b53-99aa-624800ca4518 | -12.0054 | -43.4878 | 2026-10-09 14:20:00 | GOES-19 | MUQUÉM DO SÃO FRANCISCO | BAHIA | Brasil | 2922250 | 29 | 33 | nan | nan | nan | Cerrado | 178.6 |
| 891070fa-5d74-3177-a0e5-7ac4705f1cc9 | 1.6754 | -55.6266 | 2026-10-09 14:20:00 | GOES-19 | ÓBIDOS | PARÁ | Brasil | 1505106 | 15 | 33 | nan | nan | nan | Amazônia | 107.9 |
| 8d1db2de-6770-35e3-9a5b-80550c78e337 | -12.2311 | -44.7661 | 2026-10-09 14:20:00 | GOES-19 | CATOLÂNDIA | BAHIA | Brasil | 2907400 | 29 | 33 | nan | nan | nan | Cerrado | 99.0 |
| 5374b4bc-7643-3775-954b-99011b4c8488 | -14.3415 | -55.0341 | 2026-10-09 14:20:00 | GOES-19 | ROSÁRIO OESTE | MATO GROSSO | Brasil | 5107701 | 51 | 33 | nan | nan | nan | Cerrado | 79.8 |
| edd6e3dc-e85e-3aa4-a13e-9b4980366a0c | -6.021 | -40.9577 | 2026-10-09 14:30:00 | GOES-19 | ASSUNÇÃO DO PIAUÍ | PIAUÍ | Brasil | 2201051 | 22 | 33 | nan | nan | nan | Caatinga | 362.5 |
| 8e1834e8-d99f-378e-9e15-e961910f61e3 | -6.8602 | -41.7494 | 2026-10-09 14:30:00 | GOES-19 | IPIRANGA DO PIAUÍ | PIAUÍ | Brasil | 2204808 | 22 | 33 | nan | nan | nan | Caatinga | 101.0 |
| 31865c08-e830-33ce-9ba1-c89a41d175d9 | -12.1541 | -44.778 | 2026-10-09 14:30:00 | GOES-19 | BARREIRAS | BAHIA | Brasil | 2903201 | 29 | 33 | nan | nan | nan | Cerrado | 136.9 |
| d7518519-dbe8-332f-8d97-e1f6a720ba60 | -9.1012 | -45.1393 | 2026-10-09 14:30:00 | GOES-19 | BOM JESUS | PIAUÍ | Brasil | 2201903 | 22 | 33 | nan | nan | nan | Cerrado | 107.8 |
| d2d71bdc-9660-3ba9-bc58-d1239b2330c8 | -9.0829 | -45.0957 | 2026-10-09 14:30:00 | GOES-19 | BOM JESUS | PIAUÍ | Brasil | 2201903 | 22 | 33 | nan | nan | nan | Cerrado | 107.9 |
| 80a2c0c3-9189-33d5-92ea-617add3b17c9 | -11.245 | -45.3037 | 2026-10-09 14:30:00 | GOES-19 | FORMOSA DO RIO PRETO | BAHIA | Brasil | 2911105 | 29 | 33 | nan | nan | nan | Cerrado | 286.5 |
| 0994670d-77a6-3d0b-88d1-b0a31a608748 | -12.0256 | -43.4371 | 2026-10-09 14:30:00 | GOES-19 | MUQUÉM DO SÃO FRANCISCO | BAHIA | Brasil | 2922250 | 29 | 33 | nan | nan | nan | Cerrado | 231.8 |
| fcfb7e89-c65c-31a2-bc22-016805e7c930 | -9.7177 | -45.7055 | 2026-10-09 14:30:00 | GOES-19 | GILBUÉS | PIAUÍ | Brasil | 2204402 | 22 | 33 | nan | nan | nan | Cerrado | 117.4 |
| 7fa1d3b7-8dfb-35f9-941a-6e4fe7254a0c | -5.4958 | -42.8413 | 2026-10-09 14:30:00 | GOES-19 | TERESINA | PIAUÍ | Brasil | 2211001 | 22 | 33 | nan | nan | nan | Caatinga | 128.9 |
| ce5cf797-e711-35c9-ad61-946d45c8e4e6 | -3.8786 | -44.1265 | 2026-10-09 14:30:00 | GOES-19 | COROATÁ | MARANHÃO | Brasil | 2103604 | 21 | 33 | nan | nan | nan | Cerrado | 92.1 |
| 3e2282e9-5aa9-36fc-959a-1b8930bb7f0e | -10.8909 | -44.8001 | 2026-10-09 14:30:00 | GOES-19 | SANTA RITA DE CÁSSIA | BAHIA | Brasil | 2928406 | 29 | 33 | nan | nan | nan | Cerrado | 214.9 |
| cd5c218c-f6c3-3197-97da-44ae6d11bc29 | -10.8789 | -45.5368 | 2026-10-09 14:30:00 | GOES-19 | FORMOSA DO RIO PRETO | BAHIA | Brasil | 2911105 | 29 | 33 | nan | nan | nan | Cerrado | 353.3 |
| 22a6ab92-9498-30cf-a022-7525717a9c13 | -10.491 | -47.2533 | 2026-10-09 14:30:00 | GOES-19 | PONTE ALTA DO TOCANTINS | TOCANTINS | Brasil | 1717909 | 17 | 33 | nan | nan | nan | Cerrado | 154.0 |
| 677da6f3-5a12-36bc-95cb-2e23c00cf9de | -15.2738 | -42.3452 | 2026-10-09 14:30:00 | GOES-19 | VARGEM GRANDE DO RIO PARDO | MINAS GERAIS | Brasil | 3170651 | 31 | 33 | nan | nan | nan | Mata Atlântica | 242.7 |
| e81076e8-2b11-3b63-8580-2ebe097eba05 | -7.5571 | -46.6906 | 2026-10-09 14:30:00 | GOES-19 | RIACHÃO | MARANHÃO | Brasil | 2109502 | 21 | 33 | nan | nan | nan | Cerrado | 60.2 |
| 66bbac0f-a26d-3a90-918c-d0ceac529b76 | 3.5829 | -61.3243 | 2026-10-09 14:30:00 | GOES-19 | AMAJARI | RORAIMA | Brasil | 1400027 | 14 | 33 | nan | nan | nan | Amazônia | 56.8 |
| dcc66635-582d-303a-bd26-e7588f2bfea3 | 4.0595 | -60.8985 | 2026-10-09 14:30:00 | GOES-19 | PACARAIMA | RORAIMA | Brasil | 1400456 | 14 | 33 | nan | nan | nan | Amazônia | 68.1 |
| 314a23e5-e0f9-3ca1-8d6a-c42fc9f734d5 | -11.8779 | -47.4115 | 2026-10-09 14:30:00 | GOES-19 | ALMAS | TOCANTINS | Brasil | 1700400 | 17 | 33 | nan | nan | nan | Cerrado | 191.5 |
| e9146a3e-f1b5-3cb2-9cb8-656dbbf1db80 | -14.3608 | -55.032 | 2026-10-09 14:30:00 | GOES-19 | ROSÁRIO OESTE | MATO GROSSO | Brasil | 5107701 | 51 | 33 | nan | nan | nan | Cerrado | 132.7 |
| b18b227b-e940-39e5-b682-101617db22c4 | -5.7315 | -41.7069 | 2026-10-09 14:30:00 | GOES-19 | SÃO MIGUEL DO TAPUIO | PIAUÍ | Brasil | 2210409 | 22 | 33 | nan | nan | nan | Caatinga | 89.4 |
| c1392359-c5fd-3ecd-8939-df5d96efdf24 | -7.3909 | -44.7445 | 2026-10-09 14:30:00 | GOES-19 | URUÇUÍ | PIAUÍ | Brasil | 2211209 | 22 | 33 | nan | nan | nan | Cerrado | 81.2 |
| ef3e0bcd-cce8-37c1-ab40-ee7f54c1d80c | -15.3838 | -41.878 | 2026-10-09 14:30:00 | GOES-19 | SÃO JOÃO DO PARAÍSO | MINAS GERAIS | Brasil | 3162708 | 31 | 33 | nan | nan | nan | Mata Atlântica | 493.1 |
| 7f3d0942-9d96-3254-957a-4897e6fed375 | -1.4939 | -54.5563 | 2026-10-09 14:30:00 | GOES-19 | MONTE ALEGRE | PARÁ | Brasil | 1504802 | 15 | 33 | nan | nan | nan | Amazônia | 87.5 |
| 81c2f956-597a-351a-8e60-4f8a2d7e2956 | -14.4345 | -43.9157 | 2026-10-09 14:30:00 | GOES-19 | JUVENÍLIA | MINAS GERAIS | Brasil | 3136959 | 31 | 33 | nan | nan | nan | Cerrado | 162.8 |
| 3eb11725-3393-339b-a112-49d61d4df5eb | -12.2149 | -44.6057 | 2026-10-09 14:30:00 | GOES-19 | CATOLÂNDIA | BAHIA | Brasil | 2907400 | 29 | 33 | nan | nan | nan | Cerrado | 140.0 |
| e463ddde-f01f-3bb6-83ea-80ee4d2e9852 | -3.8974 | -44.1026 | 2026-10-09 14:30:00 | GOES-19 | COROATÁ | MARANHÃO | Brasil | 2103604 | 21 | 33 | nan | nan | nan | Cerrado | 90.0 |
| 75838e5c-1cb4-3af6-a56a-1724620a1c5c | 3.5493 | -60.2442 | 2026-10-09 14:30:00 | GOES-19 | NORMANDIA | RORAIMA | Brasil | 1400407 | 14 | 33 | nan | nan | nan | Amazônia | 70.3 |
| 8ef5dd14-29c9-361a-978b-92fb0f6967b3 | -11.8787 | -47.3668 | 2026-10-09 14:30:00 | GOES-19 | ALMAS | TOCANTINS | Brasil | 1700400 | 17 | 33 | nan | nan | nan | Cerrado | 184.1 |
| 9fa60406-d187-3550-b78c-ddf6c5955841 | -1.383 | -55.1944 | 2026-10-09 14:30:00 | GOES-19 | ALENQUER | PARÁ | Brasil | 1500404 | 15 | 33 | nan | nan | nan | Amazônia | 72.5 |
| b6bbf763-e4e1-3681-a9d1-64e11a45398e | -12.2154 | -57.1287 | 2026-10-09 14:30:00 | GOES-19 | NOVA MARINGÁ | MATO GROSSO | Brasil | 5108907 | 51 | 33 | nan | nan | nan | Amazônia | 137.5 |
| 3b9bbc33-3bf8-31b7-a514-f533240b3496 | -4.0838 | -44.1159 | 2026-10-09 14:30:00 | GOES-19 | COROATÁ | MARANHÃO | Brasil | 2103604 | 21 | 33 | nan | nan | nan | Cerrado | 102.0 |
| fa4f2180-fd83-319b-9bfc-6fed164b9860 | -1.4753 | -54.756 | 2026-10-09 14:30:00 | GOES-19 | ALENQUER | PARÁ | Brasil | 1500404 | 15 | 33 | nan | nan | nan | Amazônia | 68.9 |
| 6300c962-2f62-3662-8de5-751ddef2addf | -1.1094 | -54.1601 | 2026-10-09 14:30:00 | GOES-19 | MONTE ALEGRE | PARÁ | Brasil | 1504802 | 15 | 33 | nan | nan | nan | Amazônia | 59.9 |
| 5bed593b-2970-380b-a719-06ee539b5dab | -1.3277 | -55.4525 | 2026-10-09 14:30:00 | GOES-19 | ÓBIDOS | PARÁ | Brasil | 1505106 | 15 | 33 | nan | nan | nan | Amazônia | 55.8 |
| f49fcde3-1c0a-36e6-b175-1c090bdc8248 | -9.9398 | -43.5542 | 2026-10-09 14:30:00 | GOES-19 | PILÃO ARCADO | BAHIA | Brasil | 2924405 | 29 | 33 | nan | nan | nan | Cerrado | 149.7 |
| 9831d5f5-2597-3403-8c67-7e64cc6fd7d8 | -8.655 | -54.5494 | 2026-10-09 14:30:00 | GOES-19 | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 62.7 |
| c5d663b7-c649-3f22-95f5-85e274be46e9 | -15.2535 | -42.3741 | 2026-10-09 14:30:00 | GOES-19 | MONTEZUMA | MINAS GERAIS | Brasil | 3143450 | 31 | 33 | nan | nan | nan | Mata Atlântica | 495.6 |
| 1bcc86cc-7856-3a9b-81e7-75c872be2ff5 | -3.8601 | -44.1044 | 2026-10-09 14:30:00 | GOES-19 | COROATÁ | MARANHÃO | Brasil | 2103604 | 21 | 33 | nan | nan | nan | Cerrado | 85.9 |
| 80c01bcd-e6d7-342f-a39b-cb2b98729277 | -11.2259 | -45.3064 | 2026-10-09 14:30:00 | GOES-19 | FORMOSA DO RIO PRETO | BAHIA | Brasil | 2911105 | 29 | 33 | nan | nan | nan | Cerrado | 253.0 |
| 6bb39650-12aa-3bfd-9360-6934d24f96ef | -6.7366 | -55.1274 | 2026-10-09 14:30:00 | GOES-19 | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 72.3 |
| 964e1d9a-173d-34bb-8692-53dfca4ba869 | -8.9775 | -45.9023 | 2026-10-09 14:30:00 | GOES-19 | SANTA FILOMENA | PIAUÍ | Brasil | 2209203 | 22 | 33 | nan | nan | nan | Cerrado | 144.0 |
| c0b4d991-e1c3-3eff-b699-ce737399a570 | -7.1151 | -42.5358 | 2026-10-09 14:30:00 | GOES-19 | SÃO FRANCISCO DO PIAUÍ | PIAUÍ | Brasil | 2209708 | 22 | 33 | nan | nan | nan | Caatinga | 101.7 |
| 5fad7647-c7d4-3442-99fe-333e50ea72a8 | -8.9687 | -45.1542 | 2026-10-09 14:30:00 | GOES-19 | BAIXA GRANDE DO RIBEIRO | PIAUÍ | Brasil | 2201150 | 22 | 33 | nan | nan | nan | Cerrado | 140.1 |
| 60df854b-bbae-35fa-bf81-a01054859a31 | -8.0766 | -45.6112 | 2026-10-09 14:30:00 | GOES-19 | TASSO FRAGOSO | MARANHÃO | Brasil | 2112001 | 21 | 33 | nan | nan | nan | Cerrado | 82.1 |
| 02b40073-8ed4-3a50-ae34-c48bb827d76b | -8.6514 | -44.8689 | 2026-10-09 14:30:00 | GOES-19 | CURRAIS | PIAUÍ | Brasil | 2203230 | 22 | 33 | nan | nan | nan | Cerrado | 117.6 |
| 6f280928-5ab9-312c-bfdc-b6544ee14380 | -4.0837 | -44.1389 | 2026-10-09 14:30:00 | GOES-19 | COROATÁ | MARANHÃO | Brasil | 2103604 | 21 | 33 | nan | nan | nan | Cerrado | 120.1 |
| 22a86227-bb6f-3eed-b2dd-a829a2bcc362 | -10.7475 | -46.6184 | 2026-10-09 14:30:00 | GOES-19 | MATEIROS | TOCANTINS | Brasil | 1712702 | 17 | 33 | nan | nan | nan | Cerrado | 216.3 |
| 95275781-25c4-3fd7-aa97-2d2d4888b54b | -12.2316 | -44.7427 | 2026-10-09 14:30:00 | GOES-19 | CATOLÂNDIA | BAHIA | Brasil | 2907400 | 29 | 33 | nan | nan | nan | Cerrado | 156.9 |


[Clique aqui para ver as próximas entradas](README244.md)
