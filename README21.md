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

## Dados Diários - Página 21

| ID | Latitude | Longitude | Data/Hora GMT | Satélite | Município | Estado | País | Município ID | Estado ID | País ID | Dias sem Chuva | Precipitação | Risco de Fogo | Bioma | FRP |
|----|----------|-----------|---------------|----------|-----------|--------|------|--------------|-----------|---------|----------------|--------------|----------------|-------|-----|
| 4f3ef676-4f5d-3c09-840b-4242ac2843ef | -15.90652 | -46.20061 | 2025-09-29 03:47:00 | NPP-375D | ARINOS | MINAS GERAIS | Brasil | 3104502 | 31 | 33 | nan | nan | nan | Cerrado | 1.8 |
| 3e90bcb5-1ddf-3538-943e-ef917d32102d | -15.27862 | -49.51934 | 2025-09-29 03:47:00 | NPP-375D | RIALMA | GOIÁS | Brasil | 5218607 | 52 | 33 | nan | nan | nan | Cerrado | 3.2 |
| b8c41875-dd3c-3cad-a963-5e70fe7c83fc | -11.70701 | -44.4367 | 2025-09-29 03:47:00 | NPP-375D | COTEGIPE | BAHIA | Brasil | 2909406 | 29 | 33 | nan | nan | nan | Cerrado | 4.3 |
| ab42e552-c2bb-3007-9888-194550c33fbe | -11.26454 | -47.19421 | 2025-09-29 03:47:00 | NPP-375D | ALMAS | TOCANTINS | Brasil | 1700400 | 17 | 33 | nan | nan | nan | Cerrado | 2.8 |
| 1ce15065-6154-3288-9791-58730fcd77c8 | -7.43838 | -46.99125 | 2025-09-29 03:47:00 | NPP-375D | RIACHÃO | MARANHÃO | Brasil | 2109502 | 21 | 33 | nan | nan | nan | Cerrado | 1.4 |
| 6bf386df-feec-38f8-a262-3436937a12fc | -7.18292 | -41.70354 | 2025-09-29 03:47:00 | NPP-375D | PAQUETÁ | PIAUÍ | Brasil | 2207553 | 22 | 33 | nan | nan | nan | Caatinga | 1.7 |
| dafdad75-4e00-38fd-8dac-c3857e051cb4 | -9.45716 | -45.49672 | 2025-09-29 03:47:00 | NPP-375D | SANTA FILOMENA | PIAUÍ | Brasil | 2209203 | 22 | 33 | nan | nan | nan | Cerrado | 0.6 |
| 21aa0777-89ca-303b-9378-2245b03eed6e | -11.43573 | -44.96082 | 2025-09-29 03:47:00 | NPP-375D | RIACHÃO DAS NEVES | BAHIA | Brasil | 2926202 | 29 | 33 | nan | nan | nan | Cerrado | 1.5 |
| 15ed2767-8758-3c96-886a-f38d58847ee6 | -9.78339 | -46.94051 | 2025-09-29 03:47:00 | NPP-375D | LIZARDA | TOCANTINS | Brasil | 1712405 | 17 | 33 | nan | nan | nan | Cerrado | 2.6 |
| 87c897bb-263a-3375-b410-529ed25b8b88 | -15.5428 | -47.87391 | 2025-09-29 03:47:00 | NPP-375D | BRASÍLIA | DISTRITO FEDERAL | Brasil | 5300108 | 53 | 33 | nan | nan | nan | Cerrado | 3.8 |
| 1429177f-097b-3bf2-a83c-1cbaad2c7941 | -6.26818 | -43.64506 | 2025-09-29 03:47:00 | NPP-375D | PASSAGEM FRANCA | MARANHÃO | Brasil | 2107902 | 21 | 33 | nan | nan | nan | Cerrado | 1.5 |
| 46f6d008-348b-31bf-ab01-91275ae26bc4 | -11.35748 | -45.06796 | 2025-09-29 03:47:00 | NPP-375D | FORMOSA DO RIO PRETO | BAHIA | Brasil | 2911105 | 29 | 33 | nan | nan | nan | Cerrado | 2.3 |
| b3f14a0e-aeb6-3902-ba31-603b8a7a228b | -7.46632 | -46.29814 | 2025-09-29 03:47:00 | NPP-375D | BALSAS | MARANHÃO | Brasil | 2101400 | 21 | 33 | nan | nan | nan | Cerrado | 1.7 |
| 736dd29b-5079-38e8-93f6-073647f527eb | -7.45876 | -46.30578 | 2025-09-29 03:47:00 | NPP-375D | BALSAS | MARANHÃO | Brasil | 2101400 | 21 | 33 | nan | nan | nan | Cerrado | 1.7 |
| d360676e-dbc5-32be-bf3e-8b48b5b6c60a | -8.71958 | -50.0448 | 2025-09-29 03:47:00 | NPP-375D | SANTA MARIA DAS BARREIRAS | PARÁ | Brasil | 1506583 | 15 | 33 | nan | nan | nan | Amazônia | 3.0 |
| 61f444af-7767-3601-8d13-5d4cf9656bee | -8.16063 | -46.40054 | 2025-09-29 03:47:00 | NPP-375D | BALSAS | MARANHÃO | Brasil | 2101400 | 21 | 33 | nan | nan | nan | Cerrado | 6.1 |
| a2aea0d1-65e8-3a4c-973e-8dbdf45619e4 | -6.12137 | -43.48171 | 2025-09-29 03:47:00 | NPP-375D | LAGOA DO MATO | MARANHÃO | Brasil | 2105922 | 21 | 33 | nan | nan | nan | Cerrado | 3.3 |
| 6209836a-964c-3b9d-97f9-938ac3b3eb78 | -16.34358 | -49.9504 | 2025-09-29 03:47:00 | NPP-375D | ANICUNS | GOIÁS | Brasil | 5201306 | 52 | 33 | nan | nan | nan | Cerrado | 2.5 |
| 63a946b4-eea8-3a92-982a-bef1a45fb4ae | -12.16672 | -47.77622 | 2025-09-29 03:47:00 | NPP-375D | PARANÃ | TOCANTINS | Brasil | 1716208 | 17 | 33 | nan | nan | nan | Cerrado | 2.1 |
| 6ee6e2d8-421c-37b7-94e2-e00763095ef5 | -9.3063 | -45.72839 | 2025-09-29 03:47:00 | NPP-375D | SANTA FILOMENA | PIAUÍ | Brasil | 2209203 | 22 | 33 | nan | nan | nan | Cerrado | 2.4 |
| 33f111f0-9601-3ad0-8267-83d099bdf65a | -11.99879 | -47.10885 | 2025-09-29 03:47:00 | NPP-375D | TAIPAS DO TOCANTINS | TOCANTINS | Brasil | 1720937 | 17 | 33 | nan | nan | nan | Cerrado | 1.9 |
| a092d71f-09e1-34bf-a56a-28285485f3d5 | -6.36566 | -43.92319 | 2025-09-29 03:47:00 | NPP-375D | PARAIBANO | MARANHÃO | Brasil | 2107704 | 21 | 33 | nan | nan | nan | Cerrado | 2.7 |
| 88458484-f7c0-36a3-b189-44adc4652992 | -6.27545 | -42.49277 | 2025-09-29 03:47:00 | NPP-375D | REGENERAÇÃO | PIAUÍ | Brasil | 2208809 | 22 | 33 | nan | nan | nan | Caatinga | 2.1 |
| aca98f62-0e64-364d-9952-4ca2d6b45c45 | -6.1213 | -41.81408 | 2025-09-29 03:47:00 | NPP-375D | AROAZES | PIAUÍ | Brasil | 2200905 | 22 | 33 | nan | nan | nan | Caatinga | 1.7 |
| a4f08957-41bb-38d5-928a-61a6d8c0fbe2 | -9.50901 | -47.69338 | 2025-09-29 03:47:00 | NPP-375D | RIO SONO | TOCANTINS | Brasil | 1718758 | 17 | 33 | nan | nan | nan | Cerrado | 1.7 |
| 8e496290-28d4-3215-bec1-7e3cd82044bc | -6.4686 | -44.01065 | 2025-09-29 03:47:00 | NPP-375D | PASTOS BONS | MARANHÃO | Brasil | 2108009 | 21 | 33 | nan | nan | nan | Cerrado | 6.6 |
| fca69f88-07cc-344d-b9b3-079b829b77f5 | -5.9107 | -45.85835 | 2025-09-29 03:47:00 | NPP-375D | GRAJAÚ | MARANHÃO | Brasil | 2104800 | 21 | 33 | nan | nan | nan | Cerrado | 2.5 |
| 4e659d0e-5201-357a-a6a5-e7b989072d7f | -20.05542 | -41.3315 | 2025-09-29 03:47:00 | NPP-375D | MUTUM | MINAS GERAIS | Brasil | 3144003 | 31 | 33 | nan | nan | nan | Mata Atlântica | 12.8 |
| ee048354-4882-3974-8c80-a3b961cf411b | -7.58793 | -44.80474 | 2025-09-29 03:47:00 | NPP-375D | URUÇUÍ | PIAUÍ | Brasil | 2211209 | 22 | 33 | nan | nan | nan | Cerrado | 1.5 |
| 863b6c04-5088-31b4-bb10-fbd527058b41 | -11.27127 | -47.19115 | 2025-09-29 03:47:00 | NPP-375D | ALMAS | TOCANTINS | Brasil | 1700400 | 17 | 33 | nan | nan | nan | Cerrado | 2.8 |
| 91867cb7-90f8-3a48-9eda-352295af1401 | -8.15668 | -46.4039 | 2025-09-29 03:47:00 | NPP-375D | RIACHÃO | MARANHÃO | Brasil | 2109502 | 21 | 33 | nan | nan | nan | Cerrado | 4.3 |
| 0299165d-2cde-34b4-b676-d0014a504139 | -9.99395 | -45.41164 | 2025-09-29 03:47:00 | NPP-375D | SÃO GONÇALO DO GURGUÉIA | PIAUÍ | Brasil | 2209757 | 22 | 33 | nan | nan | nan | Cerrado | 2.1 |
| 5633bbc8-1137-3eb7-99b9-3e52b24ffa6a | -6.46911 | -43.94751 | 2025-09-29 03:47:00 | NPP-375D | PARAIBANO | MARANHÃO | Brasil | 2107704 | 21 | 33 | nan | nan | nan | Cerrado | 2.0 |
| 9dc6d749-b198-30a2-91e6-e5142e376b3a | -12.57914 | -41.28794 | 2025-09-29 03:47:00 | NPP-375D | ANDARAÍ | BAHIA | Brasil | 2901304 | 29 | 33 | nan | nan | nan | Caatinga | 3.0 |
| 65cd5a25-a0eb-30fc-bc8e-5b5f03fbd488 | -10.39507 | -48.15876 | 2025-09-29 03:47:00 | NPP-375D | PALMAS | TOCANTINS | Brasil | 1721000 | 17 | 33 | nan | nan | nan | Cerrado | 2.6 |
| 84824720-01e2-3818-b315-b312b26e0d6f | -16.99816 | -43.50952 | 2025-09-29 03:47:00 | NPP-375D | ITACAMBIRA | MINAS GERAIS | Brasil | 3132008 | 31 | 33 | nan | nan | nan | Cerrado | 0.8 |
| 46032cd5-0bc0-35f8-9994-1e4201fbfde5 | -7.22864 | -44.78495 | 2025-09-29 03:47:00 | NPP-375D | SÃO FÉLIX DE BALSAS | MARANHÃO | Brasil | 2110807 | 21 | 33 | nan | nan | nan | Cerrado | 24.2 |
| 1921c657-8d13-3994-af24-618c1e17ab83 | -11.92499 | -48.03466 | 2025-09-29 03:47:00 | NPP-375D | SÃO VALÉRIO | TOCANTINS | Brasil | 1720499 | 17 | 33 | nan | nan | nan | Cerrado | 10.9 |
| 9882ce3c-958a-3278-bf25-03163e142770 | -6.74819 | -44.75138 | 2025-09-29 03:47:00 | NPP-375D | SÃO DOMINGOS DO AZEITÃO | MARANHÃO | Brasil | 2110658 | 21 | 33 | nan | nan | nan | Cerrado | 5.6 |
| 02662881-c566-3fdd-862e-3a9a97801257 | -11.9424 | -46.54034 | 2025-09-29 03:47:00 | NPP-375D | PONTE ALTA DO BOM JESUS | TOCANTINS | Brasil | 1717800 | 17 | 33 | nan | nan | nan | Cerrado | 6.3 |
| e2b18836-5ba1-3588-8932-a2855ddfed99 | -8.86751 | -46.61629 | 2025-09-29 03:47:00 | NPP-375D | BALSAS | MARANHÃO | Brasil | 2101400 | 21 | 33 | nan | nan | nan | Cerrado | 8.6 |
| 04e5a7db-b91f-3462-a186-f78d51263bf8 | -9.99331 | -45.41502 | 2025-09-29 03:47:00 | NPP-375D | SÃO GONÇALO DO GURGUÉIA | PIAUÍ | Brasil | 2209757 | 22 | 33 | nan | nan | nan | Cerrado | 2.1 |
| 0efb6932-5890-34e5-96af-ba6e1ca3a770 | -12.89005 | -45.22025 | 2025-09-29 03:47:00 | NPP-375D | SÃO DESIDÉRIO | BAHIA | Brasil | 2928901 | 29 | 33 | nan | nan | nan | Cerrado | 9.0 |
| 4d578086-aa3d-3557-947b-d3d808fd80dc | -12.95847 | -45.19089 | 2025-09-29 03:47:00 | NPP-375D | SÃO DESIDÉRIO | BAHIA | Brasil | 2928901 | 29 | 33 | nan | nan | nan | Cerrado | 1.3 |
| 51a2f040-48a4-3fba-be74-f0215d2ac4db | -12.69765 | -46.90245 | 2025-09-29 03:47:00 | NPP-375D | ARRAIAS | TOCANTINS | Brasil | 1702406 | 17 | 33 | nan | nan | nan | Cerrado | 2.8 |
| 552377de-f132-347b-a5d8-24e80b229e1c | -16.99401 | -43.50848 | 2025-09-29 03:47:00 | NPP-375D | ITACAMBIRA | MINAS GERAIS | Brasil | 3132008 | 31 | 33 | nan | nan | nan | Cerrado | 0.8 |
| f8582ace-0fb4-3555-92ca-841635cb4fbf | -11.94496 | -43.91888 | 2025-09-29 03:47:00 | NPP-375D | WANDERLEY | BAHIA | Brasil | 2933455 | 29 | 33 | nan | nan | nan | Cerrado | 3.4 |
| 2532c3be-35e5-3480-87ac-bae990b0e5fe | -6.49649 | -44.25304 | 2025-09-29 03:47:00 | NPP-375D | SUCUPIRA DO NORTE | MARANHÃO | Brasil | 2111904 | 21 | 33 | nan | nan | nan | Cerrado | 1.3 |
| 0333d088-7403-3890-9872-d549c4f5ff89 | -12.20658 | -43.74655 | 2025-09-29 03:47:00 | NPP-375D | MUQUÉM DO SÃO FRANCISCO | BAHIA | Brasil | 2922250 | 29 | 33 | nan | nan | nan | Cerrado | 2.3 |
| 1b57fcf1-e026-3cf9-9d85-ea64cfbdfb95 | -6.89323 | -44.53506 | 2025-09-29 03:47:00 | NPP-375D | SÃO DOMINGOS DO AZEITÃO | MARANHÃO | Brasil | 2110658 | 21 | 33 | nan | nan | nan | Cerrado | 2.2 |
| 1c821896-a497-3bd5-9f02-06d872ff060c | -15.68238 | -46.26693 | 2025-09-29 03:47:00 | NPP-375D | BURITIS | MINAS GERAIS | Brasil | 3109303 | 31 | 33 | nan | nan | nan | Cerrado | 0.7 |
| c95b81ec-786a-3876-a320-4f3a58f066b4 | -10.83109 | -45.39718 | 2025-09-29 03:47:00 | NPP-375D | FORMOSA DO RIO PRETO | BAHIA | Brasil | 2911105 | 29 | 33 | nan | nan | nan | Cerrado | 3.9 |
| 9a50de2b-bb63-3995-b607-6aa0d619017d | -9.28973 | -45.69406 | 2025-09-29 03:47:00 | NPP-375D | SANTA FILOMENA | PIAUÍ | Brasil | 2209203 | 22 | 33 | nan | nan | nan | Cerrado | 5.0 |
| 2c350699-3b01-3ce6-8de0-6e683f4d74f0 | -7.21654 | -44.79005 | 2025-09-29 03:47:00 | NPP-375D | SÃO FÉLIX DE BALSAS | MARANHÃO | Brasil | 2110807 | 21 | 33 | nan | nan | nan | Cerrado | 9.2 |
| fa0c9af5-74db-3d6f-9211-f0131b21c9c3 | -11.67026 | -44.29821 | 2025-09-29 03:47:00 | NPP-375D | COTEGIPE | BAHIA | Brasil | 2909406 | 29 | 33 | nan | nan | nan | Cerrado | 1.3 |
| 5480a016-4483-3f56-8f1d-771c1303c854 | -17.09324 | -48.57411 | 2025-09-29 03:47:00 | NPP-375D | VIANÓPOLIS | GOIÁS | Brasil | 5222005 | 52 | 33 | nan | nan | nan | Cerrado | 15.5 |
| 31b3b594-fe2b-354f-916d-b797e1b5fef1 | -7.44456 | -46.99258 | 2025-09-29 03:47:00 | NPP-375D | RIACHÃO | MARANHÃO | Brasil | 2109502 | 21 | 33 | nan | nan | nan | Cerrado | 1.4 |
| ea600d6b-14bf-34df-8ac8-e1bbb23888a2 | -12.59002 | -41.29519 | 2025-09-29 03:47:00 | NPP-375D | ANDARAÍ | BAHIA | Brasil | 2901304 | 29 | 33 | nan | nan | nan | Caatinga | 1.0 |
| 53600fec-80bb-38bd-ae03-8b05904be391 | -6.44906 | -44.02973 | 2025-09-29 03:47:00 | NPP-375D | PASTOS BONS | MARANHÃO | Brasil | 2108009 | 21 | 33 | nan | nan | nan | Cerrado | 1.3 |
| 8e187f71-f17e-3d93-b5a6-fc898a967abb | -7.29919 | -42.82716 | 2025-09-29 03:47:00 | NPP-375D | FLORIANO | PIAUÍ | Brasil | 2203909 | 22 | 33 | nan | nan | nan | Caatinga | 1.2 |
| 9603518f-2205-3a80-b7dc-0b94a2a96628 | -11.92174 | -48.04634 | 2025-09-29 03:47:00 | NPP-375D | SÃO VALÉRIO | TOCANTINS | Brasil | 1720499 | 17 | 33 | nan | nan | nan | Cerrado | 3.6 |
| 7e5891a5-77fe-353a-a7c2-60eac17072b6 | -15.26105 | -48.75993 | 2025-09-29 03:47:00 | NPP-375D | VILA PROPÍCIO | GOIÁS | Brasil | 5222302 | 52 | 33 | nan | nan | nan | Cerrado | 10.6 |
| fb3c5d35-2d2f-349e-a5b6-ae7149455178 | -7.30863 | -43.81461 | 2025-09-29 03:47:00 | NPP-375D | LANDRI SALES | PIAUÍ | Brasil | 2205607 | 22 | 33 | nan | nan | nan | Cerrado | 1.3 |
| ef9420b4-658c-35e2-ad55-80bd19488548 | -10.68147 | -46.75702 | 2025-09-29 03:47:00 | NPP-375D | MATEIROS | TOCANTINS | Brasil | 1712702 | 17 | 33 | nan | nan | nan | Cerrado | 0.8 |
| 3dc63ddf-c6f6-3625-a76d-3c331ea53ca6 | -11.95012 | -47.11161 | 2025-09-29 03:47:00 | NPP-375D | TAIPAS DO TOCANTINS | TOCANTINS | Brasil | 1720937 | 17 | 33 | nan | nan | nan | Cerrado | 1.0 |
| 94882dd3-b605-3d49-8831-c28dabe32bd2 | -16.40748 | -43.72228 | 2025-09-29 03:47:00 | NPP-375D | CAPITÃO ENÉAS | MINAS GERAIS | Brasil | 3112703 | 31 | 33 | nan | nan | nan | Cerrado | 1.1 |
| 9da91f66-4030-3978-a40b-eb12a0bb191a | -6.49392 | -44.25568 | 2025-09-29 03:47:00 | NPP-375D | SUCUPIRA DO NORTE | MARANHÃO | Brasil | 2111904 | 21 | 33 | nan | nan | nan | Cerrado | 1.4 |
| 337c936a-21bf-32fe-ad99-39fd0be8f7a8 | -8.86442 | -45.03247 | 2025-09-29 03:47:00 | NPP-375D | BAIXA GRANDE DO RIBEIRO | PIAUÍ | Brasil | 2201150 | 22 | 33 | nan | nan | nan | Cerrado | 1.5 |
| d8aeca76-98ff-35d3-a28c-5d9ff5702d3d | -8.71886 | -47.9839 | 2025-09-29 03:47:00 | NPP-375D | SANTA MARIA DO TOCANTINS | TOCANTINS | Brasil | 1718881 | 17 | 33 | nan | nan | nan | Cerrado | 3.0 |
| 589fcac5-3307-3522-88f1-80dbaa4f0c3e | -11.70592 | -44.33409 | 2025-09-29 03:47:00 | NPP-375D | COTEGIPE | BAHIA | Brasil | 2909406 | 29 | 33 | nan | nan | nan | Cerrado | 2.9 |
| 263b1460-65cf-359b-bc1b-750e0903eba9 | -10.79131 | -46.68315 | 2025-09-29 03:47:00 | NPP-375D | MATEIROS | TOCANTINS | Brasil | 1712702 | 17 | 33 | nan | nan | nan | Cerrado | 3.1 |
| 1590d239-5fe6-310a-a1c1-a06063c9570e | -8.29205 | -45.43481 | 2025-09-29 03:47:00 | NPP-375D | BAIXA GRANDE DO RIBEIRO | PIAUÍ | Brasil | 2201150 | 22 | 33 | nan | nan | nan | Cerrado | 1.4 |
| 9b60af38-0e9e-3188-afba-648fa843f107 | -15.32405 | -47.91662 | 2025-09-29 03:47:00 | NPP-375D | PLANALTINA | GOIÁS | Brasil | 5217609 | 52 | 33 | nan | nan | nan | Cerrado | 2.0 |
| 5999c1ba-37e1-39d5-9040-1ef3d9a824e0 | -7.58517 | -44.80934 | 2025-09-29 03:47:00 | NPP-375D | URUÇUÍ | PIAUÍ | Brasil | 2211209 | 22 | 33 | nan | nan | nan | Cerrado | 3.3 |
| 36db16fb-0767-373c-955d-45662aac2375 | -18.8607 | -41.99116 | 2025-09-29 03:47:00 | NPP-375D | GOVERNADOR VALADARES | MINAS GERAIS | Brasil | 3127701 | 31 | 33 | nan | nan | nan | Mata Atlântica | 3.3 |
| a52492f9-df14-3d49-a021-073c9cbf9de6 | -18.90441 | -41.13084 | 2025-09-29 03:47:00 | NPP-375D | CUPARAQUE | MINAS GERAIS | Brasil | 3120839 | 31 | 33 | nan | nan | nan | Mata Atlântica | 1.3 |
| 1fbc0bc4-f7e8-30b8-b792-2f053015be23 | -6.62513 | -44.96661 | 2025-09-29 03:47:00 | NPP-375D | MIRADOR | MARANHÃO | Brasil | 2106706 | 21 | 33 | nan | nan | nan | Cerrado | 2.0 |
| 28f6c553-3813-3ca7-9b01-58e398dfc618 | -12.67166 | -46.87513 | 2025-09-29 03:47:00 | NPP-375D | ARRAIAS | TOCANTINS | Brasil | 1702406 | 17 | 33 | nan | nan | nan | Cerrado | 0.9 |
| 8c581907-96cd-3dc8-96bb-40d77545412b | -6.05397 | -42.46447 | 2025-09-29 03:47:00 | NPP-375D | HUGO NAPOLEÃO | PIAUÍ | Brasil | 2204600 | 22 | 33 | nan | nan | nan | Caatinga | 2.3 |
| fa8bd663-c548-34a8-9e3a-e12d0716597b | -6.49511 | -44.24908 | 2025-09-29 03:47:00 | NPP-375D | SUCUPIRA DO NORTE | MARANHÃO | Brasil | 2111904 | 21 | 33 | nan | nan | nan | Cerrado | 1.3 |
| 6c7907fc-e5e6-3f81-905b-991e0920e27c | -8.29693 | -45.43951 | 2025-09-29 03:47:00 | NPP-375D | BAIXA GRANDE DO RIBEIRO | PIAUÍ | Brasil | 2201150 | 22 | 33 | nan | nan | nan | Cerrado | 2.0 |
| e6a3c8d0-90b9-32a2-880c-3382f4eaef3d | -7.39357 | -44.46058 | 2025-09-29 03:47:00 | NPP-375D | URUÇUÍ | PIAUÍ | Brasil | 2211209 | 22 | 33 | nan | nan | nan | Cerrado | 1.1 |
| 60aa9529-6cbb-3a39-b450-14d0cb8034d7 | -10.82825 | -47.93377 | 2025-09-29 03:47:00 | NPP-375D | MONTE DO CARMO | TOCANTINS | Brasil | 1713601 | 17 | 33 | nan | nan | nan | Cerrado | 6.3 |
| 320d81e3-1009-3078-8dd1-f54abaf4cc7c | -7.58672 | -44.81128 | 2025-09-29 03:47:00 | NPP-375D | URUÇUÍ | PIAUÍ | Brasil | 2211209 | 22 | 33 | nan | nan | nan | Cerrado | 1.2 |
| e6954462-4860-3843-a8d5-f1a29cd5c2f1 | -17.73081 | -46.68926 | 2025-09-29 03:47:00 | NPP-375D | VAZANTE | MINAS GERAIS | Brasil | 3171006 | 31 | 33 | nan | nan | nan | Cerrado | 2.7 |
| 5cd07971-b6c9-3374-b6cf-4872f715ed82 | -6.82956 | -44.83644 | 2025-09-29 03:47:00 | NPP-375D | SÃO FÉLIX DE BALSAS | MARANHÃO | Brasil | 2110807 | 21 | 33 | nan | nan | nan | Cerrado | 11.4 |
| 26a8e964-e201-3aa1-a83c-9208325a870c | -6.11074 | -41.82148 | 2025-09-29 03:47:00 | NPP-375D | AROAZES | PIAUÍ | Brasil | 2200905 | 22 | 33 | nan | nan | nan | Caatinga | 2.1 |
| 063e6f7a-04b7-3262-bec0-20c7453e56a6 | -10.68063 | -46.7613 | 2025-09-29 03:47:00 | NPP-375D | MATEIROS | TOCANTINS | Brasil | 1712702 | 17 | 33 | nan | nan | nan | Cerrado | 0.8 |
| dd444b5b-f202-3638-aee7-fa424d44c8d8 | -11.51072 | -44.85642 | 2025-09-29 03:47:00 | NPP-375D | RIACHÃO DAS NEVES | BAHIA | Brasil | 2926202 | 29 | 33 | nan | nan | nan | Cerrado | 3.3 |
| 239303a9-95f5-3e89-b52b-16c5afba54dd | -11.37086 | -44.94104 | 2025-09-29 03:47:00 | NPP-375D | RIACHÃO DAS NEVES | BAHIA | Brasil | 2926202 | 29 | 33 | nan | nan | nan | Cerrado | 0.7 |
| 082971c2-3577-3a13-954a-d29c47d5bb0d | -15.42773 | -48.24831 | 2025-09-29 03:47:00 | NPP-375D | PADRE BERNARDO | GOIÁS | Brasil | 5215603 | 52 | 33 | nan | nan | nan | Cerrado | 1.5 |
| 2cbd130e-7d05-3f30-9037-523af198ad05 | -10.28325 | -45.19279 | 2025-09-29 03:47:00 | NPP-375D | CORRENTE | PIAUÍ | Brasil | 2202901 | 22 | 33 | nan | nan | nan | Cerrado | 1.8 |
| be15fe0a-07d6-3fa4-b921-3ae143e988e7 | -7.76612 | -45.73809 | 2025-09-29 03:47:00 | NPP-375D | SAMBAÍBA | MARANHÃO | Brasil | 2109700 | 21 | 33 | nan | nan | nan | Cerrado | 2.6 |
| 4448f479-8cd7-357a-a13d-06e4be52afe1 | -11.98251 | -47.12454 | 2025-09-29 03:47:00 | NPP-375D | TAIPAS DO TOCANTINS | TOCANTINS | Brasil | 1720937 | 17 | 33 | nan | nan | nan | Cerrado | 2.5 |
| 512d0223-30b9-3106-9c1f-5f7d14b5e98b | -14.56835 | -48.28069 | 2025-09-29 03:49:00 | NPP-375D | NIQUELÂNDIA | GOIÁS | Brasil | 5214606 | 52 | 33 | nan | nan | nan | Cerrado | 3.9 |
| f162ad0f-b666-3aee-8c68-1e859e8ebd72 | -14.65121 | -48.15941 | 2025-09-29 03:49:00 | NPP-375D | NIQUELÂNDIA | GOIÁS | Brasil | 5214606 | 52 | 33 | nan | nan | nan | Cerrado | 3.2 |
| eef1c34c-ff9c-34bc-8c84-2d77d578173c | -15.5361 | -44.32991 | 2025-09-29 03:49:00 | NPP-375D | PEDRAS DE MARIA DA CRUZ | MINAS GERAIS | Brasil | 3149150 | 31 | 33 | nan | nan | nan | Caatinga | 0.6 |
| 4f874857-bb55-38e7-98d4-bc96cbce5b5b | -21.42387 | -43.76972 | 2025-09-29 03:49:00 | NPP-375D | ANTÔNIO CARLOS | MINAS GERAIS | Brasil | 3102902 | 31 | 33 | nan | nan | nan | Mata Atlântica | 1.1 |
| e4797ba8-330b-3934-bc30-345a51519015 | -19.94387 | -43.66755 | 2025-09-29 03:49:00 | NPP-375D | CAETÉ | MINAS GERAIS | Brasil | 3110004 | 31 | 33 | nan | nan | nan | Mata Atlântica | 5.8 |
| 6c314fa5-8b3c-3fff-a8e9-7be03279830f | -19.94247 | -43.67497 | 2025-09-29 03:49:00 | NPP-375D | CAETÉ | MINAS GERAIS | Brasil | 3110004 | 31 | 33 | nan | nan | nan | Mata Atlântica | 4.1 |


[Clique aqui para ver as próximas entradas](README22.md)
