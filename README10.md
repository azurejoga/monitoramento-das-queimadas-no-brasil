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

## Dados Diários - Página 10

| ID | Latitude | Longitude | Data/Hora GMT | Satélite | Município | Estado | País | Município ID | Estado ID | País ID | Dias sem Chuva | Precipitação | Risco de Fogo | Bioma | FRP |
|----|----------|-----------|---------------|----------|-----------|--------|------|--------------|-----------|---------|----------------|--------------|----------------|-------|-----|
| 2543398e-af9d-387d-8b43-67c466c7cae7 | -4.0405 | -46.9496 | 2024-10-18 00:55:28 | METOP-C | ITINGA DO MARANHÃO | MARANHÃO | Brasil | 2105427 | 21 | 33 | nan | nan | nan | Amazônia | nan |
| 5a2e3c79-eb90-3ddc-bf80-33d59a0a5b17 | -4.2672 | -48.007 | 2024-10-18 00:55:28 | METOP-C | DOM ELISEU | PARÁ | Brasil | 1502939 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| 556500cc-d82d-3097-a72b-af410fc98472 | -4.2691 | -48.0149 | 2024-10-18 00:55:28 | METOP-C | DOM ELISEU | PARÁ | Brasil | 1502939 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| 48f2d3d5-a421-3e5b-8205-e667509363c3 | -4.2204 | -47.850498 | 2024-10-18 00:55:28 | METOP-C | DOM ELISEU | PARÁ | Brasil | 1502939 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| 2130b109-a9b7-3c0c-9cfd-bca56e98a2cb | -4.5981 | -49.522099 | 2024-10-18 00:55:29 | METOP-C | NOVO REPARTIMENTO | PARÁ | Brasil | 1505064 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| 273bbe08-c59f-31e3-8086-bcd31d2897b8 | -3.7016 | -45.9044 | 2024-10-18 00:55:29 | METOP-C | ALTO ALEGRE DO PINDARÉ | MARANHÃO | Brasil | 2100477 | 21 | 33 | nan | nan | nan | Amazônia | nan |
| 4115f471-8a0d-34a8-9645-2c375588b929 | -3.7041 | -45.914799 | 2024-10-18 00:55:29 | METOP-C | ALTO ALEGRE DO PINDARÉ | MARANHÃO | Brasil | 2100477 | 21 | 33 | nan | nan | nan | Amazônia | nan |
| e4a64304-3368-3326-bbe5-a7c71a4d7a79 | -3.7065 | -45.925201 | 2024-10-18 00:55:29 | METOP-C | ALTO ALEGRE DO PINDARÉ | MARANHÃO | Brasil | 2100477 | 21 | 33 | nan | nan | nan | Amazônia | nan |
| 1e683e20-24af-3353-95d6-86a97f799475 | -3.6919 | -45.9067 | 2024-10-18 00:55:30 | METOP-C | ALTO ALEGRE DO PINDARÉ | MARANHÃO | Brasil | 2100477 | 21 | 33 | nan | nan | nan | Amazônia | nan |
| 747dac8f-2f55-39aa-84ff-a6135e79c20d | -3.6943 | -45.917099 | 2024-10-18 00:55:30 | METOP-C | ALTO ALEGRE DO PINDARÉ | MARANHÃO | Brasil | 2100477 | 21 | 33 | nan | nan | nan | Amazônia | nan |
| 511b0b36-be73-3c9d-89eb-7ec759f5a22b | -4.4072 | -45.9773 | 2024-10-18 00:55:31 | GOES-16 | SANTA LUZIA | MARANHÃO | Brasil | 2110005 | 21 | 33 | nan | nan | nan | Amazônia | 93.7 |
| dd745944-8d52-3db8-8ec9-897bdf730f3a | -4.4258 | -45.9763 | 2024-10-18 00:55:31 | GOES-16 | SANTA LUZIA | MARANHÃO | Brasil | 2110005 | 21 | 33 | nan | nan | nan | Amazônia | 243.6 |
| 197820ef-dde8-30a4-820b-2474e2b6ce85 | -4.426 | -45.954 | 2024-10-18 00:55:31 | GOES-16 | SANTA LUZIA | MARANHÃO | Brasil | 2110005 | 21 | 33 | nan | nan | nan | Amazônia | 138.2 |
| 83bc24d5-82bc-30f3-befb-73a888813943 | -3.5447 | -45.7635 | 2024-10-18 00:55:31 | METOP-C | BOM JARDIM | MARANHÃO | Brasil | 2102002 | 21 | 33 | nan | nan | nan | Amazônia | nan |
| 8f22cd82-9ada-3349-8a0d-0cf946e5534e | -4.5614 | -48.0141 | 2024-10-18 00:55:32 | GOES-16 | RONDON DO PARÁ | PARÁ | Brasil | 1506187 | 15 | 33 | nan | nan | nan | Amazônia | 76.8 |
| 445fc738-c6bd-3b87-8caa-a1f1b85203d5 | -4.58 | -48.0132 | 2024-10-18 00:55:32 | GOES-16 | RONDON DO PARÁ | PARÁ | Brasil | 1506187 | 15 | 33 | nan | nan | nan | Amazônia | 62.3 |
| 2d1c8176-bd1f-32f2-aef6-40255eaad251 | -4.1829 | -48.5756 | 2024-10-18 00:55:32 | METOP-C | RONDON DO PARÁ | PARÁ | Brasil | 1506187 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| 8418d82b-5d72-3f42-bb44-6e5b308dae73 | -3.9236 | -48.347401 | 2024-10-18 00:55:35 | METOP-C | DOM ELISEU | PARÁ | Brasil | 1502939 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| f1f4ad0b-90eb-317f-9690-a5159174ac9d | -3.912 | -48.3419 | 2024-10-18 00:55:35 | METOP-C | DOM ELISEU | PARÁ | Brasil | 1502939 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| b6d2064e-d521-3c46-b5e1-d37aab70c1f9 | -3.9173 | -48.364899 | 2024-10-18 00:55:35 | METOP-C | DOM ELISEU | PARÁ | Brasil | 1502939 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| 5dd15ff5-5d26-3f39-b029-1ffbe57d1e0c | -3.9004 | -48.336399 | 2024-10-18 00:55:35 | METOP-C | DOM ELISEU | PARÁ | Brasil | 1502939 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| d5fcdcb2-5546-31ee-aba3-cea09ab0d9ac | -3.9022 | -48.344101 | 2024-10-18 00:55:35 | METOP-C | DOM ELISEU | PARÁ | Brasil | 1502939 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| c1e4c845-62c8-3b05-96d7-4d2c4f44ecbd | -3.9075 | -48.3671 | 2024-10-18 00:55:35 | METOP-C | DOM ELISEU | PARÁ | Brasil | 1502939 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| 4ee453d7-44b6-30ef-af86-853331775b22 | -3.896 | -48.361801 | 2024-10-18 00:55:36 | METOP-C | DOM ELISEU | PARÁ | Brasil | 1502939 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| 09b63b3d-4019-34c3-b99c-f8aa47ab5a28 | -3.8977 | -48.3694 | 2024-10-18 00:55:36 | METOP-C | DOM ELISEU | PARÁ | Brasil | 1502939 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| 588f1977-334f-35f0-9691-31bf79051630 | -4.0329 | -48.9519 | 2024-10-18 00:55:36 | METOP-C | GOIANÉSIA DO PARÁ | PARÁ | Brasil | 1503093 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| dbfac3e2-79b7-39c4-a143-061f276ad58b | -4.388 | -50.806301 | 2024-10-18 00:55:37 | METOP-C | NOVO REPARTIMENTO | PARÁ | Brasil | 1505064 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| 9938b420-d050-3462-88e6-f06c9c64600f | -4.3895 | -50.813202 | 2024-10-18 00:55:37 | METOP-C | NOVO REPARTIMENTO | PARÁ | Brasil | 1505064 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| 02b6482c-0e96-352b-9a24-5814695b0b12 | -4.2607 | -50.296398 | 2024-10-18 00:55:37 | METOP-C | NOVO REPARTIMENTO | PARÁ | Brasil | 1505064 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| c7e39dc6-cb49-35e9-8877-a821213ab8f4 | -4.2622 | -50.3032 | 2024-10-18 00:55:37 | METOP-C | NOVO REPARTIMENTO | PARÁ | Brasil | 1505064 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| 35869242-66a9-327f-a44c-42581b4f3fca | -3.2872 | -47.1227 | 2024-10-18 00:55:41 | METOP-C | PARAGOMINAS | PARÁ | Brasil | 1505502 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| b3d43eb7-fa31-306c-a74e-5117148f1fb0 | -3.2893 | -47.131599 | 2024-10-18 00:55:41 | METOP-C | PARAGOMINAS | PARÁ | Brasil | 1505502 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| 39a176ea-df29-31fe-8ec4-c7b945824cff | -3.2774 | -47.124901 | 2024-10-18 00:55:41 | METOP-C | PARAGOMINAS | PARÁ | Brasil | 1505502 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| 845d9687-78e3-356a-8051-6beceee40127 | -3.2795 | -47.133801 | 2024-10-18 00:55:41 | METOP-C | PARAGOMINAS | PARÁ | Brasil | 1505502 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| 6fa6e124-6ccd-3c40-9ae3-643a7be4ceeb | -4.0458 | -50.438202 | 2024-10-18 00:55:41 | METOP-C | NOVO REPARTIMENTO | PARÁ | Brasil | 1505064 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| ae588151-58f6-3c0c-a47f-3c9d4abbf5ea | -4.0665 | -50.978699 | 2024-10-18 00:55:43 | METOP-C | PACAJÁ | PARÁ | Brasil | 1505486 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| fde9c0d4-23d9-36e4-be38-f6176a8384a9 | -4.0681 | -50.9855 | 2024-10-18 00:55:43 | METOP-C | PACAJÁ | PARÁ | Brasil | 1505486 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| 25f6be88-9fb9-3649-868a-b922c945e336 | -4.0668 | -51.115002 | 2024-10-18 00:55:43 | METOP-C | PACAJÁ | PARÁ | Brasil | 1505486 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| d0ee50c5-70e6-3536-8253-fb1a24ec37ea | -4.0684 | -51.121899 | 2024-10-18 00:55:43 | METOP-C | PACAJÁ | PARÁ | Brasil | 1505486 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| 29ea32fb-5886-37af-8d1c-5fb5cac9f72b | -4.07 | -51.1287 | 2024-10-18 00:55:43 | METOP-C | PACAJÁ | PARÁ | Brasil | 1505486 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| 90ad4467-0842-3375-a123-519ce8286640 | -4.0715 | -51.135502 | 2024-10-18 00:55:43 | METOP-C | PACAJÁ | PARÁ | Brasil | 1505486 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| 094b4f9e-f1b4-3e13-8590-69ef02f86fbf | -6.6703 | -70.1174 | 2024-10-18 00:55:44 | GOES-16 | EIRUNEPÉ | AMAZONAS | Brasil | 1301407 | 13 | 33 | nan | nan | nan | Amazônia | 51.9 |
| 4af8244b-3d1f-394b-b01d-569ed0e25e92 | -6.6886 | -70.1171 | 2024-10-18 00:55:45 | GOES-16 | EIRUNEPÉ | AMAZONAS | Brasil | 1301407 | 13 | 33 | nan | nan | nan | Amazônia | 67.2 |
| b8ffcd8f-18bf-3fd8-8e6d-20396b553074 | -3.5911 | -50.165401 | 2024-10-18 00:55:47 | METOP-C | PACAJÁ | PARÁ | Brasil | 1505486 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| cdcd3ea5-72a7-3f11-9ae4-582bf120bac9 | -3.3455 | -49.145802 | 2024-10-18 00:55:47 | METOP-C | MOJU | PARÁ | Brasil | 1504703 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| c0da0ca0-66e4-3559-a7bf-f2c3a5bf93fd | -3.5895 | -50.158501 | 2024-10-18 00:55:47 | METOP-C | PACAJÁ | PARÁ | Brasil | 1505486 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| 600b93af-bb32-3713-94a4-c46b396790be | -3.2698 | -49.0863 | 2024-10-18 00:55:48 | METOP-C | MOJU | PARÁ | Brasil | 1504703 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| ace9ec5c-3119-3f55-8a4c-16b3fdd19e50 | -3.2715 | -49.093601 | 2024-10-18 00:55:48 | METOP-C | MOJU | PARÁ | Brasil | 1504703 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| afb9c076-9b8e-38b9-b98d-c0a75ad0b78f | -3.2111 | -48.9216 | 2024-10-18 00:55:49 | METOP-C | TAILÂNDIA | PARÁ | Brasil | 1507953 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| f7e3c693-ec01-380a-a39e-b9e1b17ecb40 | -3.2128 | -48.929001 | 2024-10-18 00:55:49 | METOP-C | TAILÂNDIA | PARÁ | Brasil | 1507953 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| ef59a73d-a4a3-39fc-84a4-cc6a007b3896 | -3.7083 | -51.080299 | 2024-10-18 00:55:49 | METOP-C | PACAJÁ | PARÁ | Brasil | 1505486 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| 83e353f4-a0a3-331b-8306-c883c7a9b326 | -3.7099 | -51.087101 | 2024-10-18 00:55:49 | METOP-C | PACAJÁ | PARÁ | Brasil | 1505486 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| 5ae0d8bb-37e8-3163-bdaf-db868837ca0f | -3.1457 | -48.684399 | 2024-10-18 00:55:49 | METOP-C | TAILÂNDIA | PARÁ | Brasil | 1507953 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| 3d8dd1b3-abb2-3453-9871-f0d0491f8e2f | -3.1475 | -48.692001 | 2024-10-18 00:55:49 | METOP-C | TAILÂNDIA | PARÁ | Brasil | 1507953 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| 7234b4b2-aa66-3953-bda6-77576e945b05 | -3.5813 | -50.571201 | 2024-10-18 00:55:49 | METOP-C | PACAJÁ | PARÁ | Brasil | 1505486 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| f2c8be34-0f02-39c1-ba1e-20840ee78dd6 | -3.5828 | -50.577999 | 2024-10-18 00:55:49 | METOP-C | PACAJÁ | PARÁ | Brasil | 1505486 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| 278ba94f-25c2-38dd-81bd-9e2b02cf96fd | -3.1272 | -48.6488 | 2024-10-18 00:55:49 | METOP-C | TAILÂNDIA | PARÁ | Brasil | 1507953 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| 1bee0457-1e1d-3a8a-9eb7-b76a5b0b3ac8 | -3.1289 | -48.656399 | 2024-10-18 00:55:49 | METOP-C | TAILÂNDIA | PARÁ | Brasil | 1507953 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| e21c2940-a8f8-3781-ae12-d56b137dc6d5 | -3.1342 | -48.6791 | 2024-10-18 00:55:49 | METOP-C | TAILÂNDIA | PARÁ | Brasil | 1507953 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| 0bacdc64-36c5-38bc-adb2-7df4dcc9ca6e | -3.1359 | -48.686699 | 2024-10-18 00:55:49 | METOP-C | TAILÂNDIA | PARÁ | Brasil | 1507953 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| 2093be66-bce2-3741-ad92-cd634b938796 | -3.1377 | -48.694302 | 2024-10-18 00:55:49 | METOP-C | TAILÂNDIA | PARÁ | Brasil | 1507953 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| f5ffb1e6-39b7-3fcf-aa18-cd070f5ca192 | -3.7351 | -51.332901 | 2024-10-18 00:55:49 | METOP-C | ANAPU | PARÁ | Brasil | 1500859 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| 82c2e7a6-d525-3b45-a5e8-670d3617a5fd | -3.7367 | -51.339699 | 2024-10-18 00:55:49 | METOP-C | ANAPU | PARÁ | Brasil | 1500859 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| d60b0604-3375-37fb-b433-9c41e9c8aa3c | -3.1314 | -48.9785 | 2024-10-18 00:55:50 | METOP-C | MOJU | PARÁ | Brasil | 1504703 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| 9a5f444e-bb4b-3525-8fc8-f1fea0e3c1b2 | -3.1331 | -48.985901 | 2024-10-18 00:55:50 | METOP-C | MOJU | PARÁ | Brasil | 1504703 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| 03ece981-60e0-35b4-91bb-b1f22f6d64f2 | -3.7654 | -51.826199 | 2024-10-18 00:55:51 | METOP-C | SENADOR JOSÉ PORFÍRIO | PARÁ | Brasil | 1507805 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| 358c70ca-b73b-305a-9778-5247cb4b0afe | -3.767 | -51.833199 | 2024-10-18 00:55:51 | METOP-C | SENADOR JOSÉ PORFÍRIO | PARÁ | Brasil | 1507805 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| 4c3646c8-568b-3664-a958-171d38124945 | -3.4553 | -50.606499 | 2024-10-18 00:55:51 | METOP-C | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| 98c1dd2b-0016-3177-a24b-65005faa015f | -3.4569 | -50.6133 | 2024-10-18 00:55:51 | METOP-C | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| ef515724-c9ea-32cb-98c4-37feaa9cf95a | -3.3633 | -50.296001 | 2024-10-18 00:55:51 | METOP-C | PACAJÁ | PARÁ | Brasil | 1505486 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| d4f90c89-8409-3a47-8101-0e22d0f05fb3 | -3.3648 | -50.302898 | 2024-10-18 00:55:51 | METOP-C | PACAJÁ | PARÁ | Brasil | 1505486 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| c299e88e-b225-3eac-aa7f-bf300c4f63c2 | -3.3664 | -50.309799 | 2024-10-18 00:55:51 | METOP-C | PACAJÁ | PARÁ | Brasil | 1505486 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| 56343332-85b8-3d79-bc41-169ec97f5dad | -3.3535 | -50.298199 | 2024-10-18 00:55:52 | METOP-C | PACAJÁ | PARÁ | Brasil | 1505486 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| 244f7841-d0ae-3b52-bc57-fe6ce8deac59 | -3.355 | -50.305099 | 2024-10-18 00:55:52 | METOP-C | PACAJÁ | PARÁ | Brasil | 1505486 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| a1382cc5-3319-3205-90a3-222624e0f2ed | -3.3566 | -50.312 | 2024-10-18 00:55:52 | METOP-C | PACAJÁ | PARÁ | Brasil | 1505486 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| a6ec89c3-01f8-3942-8429-122569e88373 | -3.2279 | -50.021702 | 2024-10-18 00:55:53 | METOP-C | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| d75f3a23-53a7-3064-91bf-f52b9ec8e8bf | -3.7729 | -52.402401 | 2024-10-18 00:55:53 | METOP-C | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| 623208fb-362e-32f8-83df-07a33cd271a2 | -2.5368 | -47.2187 | 2024-10-18 00:55:53 | METOP-C | CAPITÃO POÇO | PARÁ | Brasil | 1502301 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| b6f4b401-adf6-3dcd-973c-aa806c3ee71b | -2.5389 | -47.2276 | 2024-10-18 00:55:53 | METOP-C | CAPITÃO POÇO | PARÁ | Brasil | 1502301 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| 06576517-e67b-347a-ad78-1416934009a2 | -2.3425 | -46.474998 | 2024-10-18 00:55:54 | METOP-C | CACHOEIRA DO PIRIÁ | PARÁ | Brasil | 1501956 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| 81433eb4-e0c7-3d56-892e-37276cb6647f | -2.3448 | -46.485001 | 2024-10-18 00:55:54 | METOP-C | CACHOEIRA DO PIRIÁ | PARÁ | Brasil | 1501956 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| 945a7111-62e9-3e7a-84ba-9d1d04437421 | -2.3471 | -46.4949 | 2024-10-18 00:55:54 | METOP-C | CACHOEIRA DO PIRIÁ | PARÁ | Brasil | 1501956 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| 8fe355fd-4793-3e50-93a9-d894d6c116e2 | -2.3327 | -46.4772 | 2024-10-18 00:55:54 | METOP-C | CACHOEIRA DO PIRIÁ | PARÁ | Brasil | 1501956 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| 09885162-4ce4-3b1c-85ac-ec70a38bde39 | -2.3351 | -46.487202 | 2024-10-18 00:55:54 | METOP-C | CACHOEIRA DO PIRIÁ | PARÁ | Brasil | 1501956 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| a8c19c3b-fe4c-3ca3-ae9e-c0c298af697e | -2.9716 | -49.268501 | 2024-10-18 00:55:54 | METOP-C | MOJU | PARÁ | Brasil | 1504703 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| 6570947e-6983-3012-bd89-d47e02ce0503 | -2.9732 | -49.2757 | 2024-10-18 00:55:54 | METOP-C | MOJU | PARÁ | Brasil | 1504703 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| da3259de-84f0-3fd1-8a58-d805286111a6 | -3.2225 | -50.356602 | 2024-10-18 00:55:54 | METOP-C | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| 7798e666-0e60-3e7e-9765-fa49835079e2 | -3.2241 | -50.363499 | 2024-10-18 00:55:54 | METOP-C | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| 0301e3cd-9c3f-37e6-a7f7-6deddadbb88a | -3.5155 | -51.634602 | 2024-10-18 00:55:54 | METOP-C | ANAPU | PARÁ | Brasil | 1500859 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| 8c96a55c-158e-31ad-b771-270b97ccc22b | -2.9668 | -49.2924 | 2024-10-18 00:55:54 | METOP-C | MOJU | PARÁ | Brasil | 1504703 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| 9a96c65c-4b79-39f5-b250-703f35c287cd | -3.2127 | -50.358799 | 2024-10-18 00:55:54 | METOP-C | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| bcb0b273-b69a-3429-96c6-e0783244ebe5 | -3.2143 | -50.3657 | 2024-10-18 00:55:54 | METOP-C | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| 83628317-4446-3e54-8683-52563b08accc | -3.2721 | -50.6619 | 2024-10-18 00:55:54 | METOP-C | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| 6da14caa-8cd0-3b32-b5d3-d95ced23ac67 | -3.2736 | -50.668701 | 2024-10-18 00:55:54 | METOP-C | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| 6cfe7fde-9873-3021-a654-9207f663ad0f | -3.4939 | -51.675598 | 2024-10-18 00:55:54 | METOP-C | ANAPU | PARÁ | Brasil | 1500859 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| ad19343a-f544-3d4b-9cf3-19c958b2a4f7 | -3.4955 | -51.682499 | 2024-10-18 00:55:54 | METOP-C | ANAPU | PARÁ | Brasil | 1500859 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| 260ebfcb-dfed-3232-a8d8-9853c72e34e1 | -3.4841 | -51.677799 | 2024-10-18 00:55:55 | METOP-C | ANAPU | PARÁ | Brasil | 1500859 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| b14e1963-cc32-3670-b1f1-92954593424c | -3.1029 | -50.195301 | 2024-10-18 00:55:55 | METOP-C | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| 667474a1-b87f-312f-bb34-4b7de936b7ef | -2.8368 | -49.533199 | 2024-10-18 00:55:57 | METOP-C | BAIÃO | PARÁ | Brasil | 1501204 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| 807fc632-fd35-38eb-a259-ffd25d742aff | -2.8385 | -49.540401 | 2024-10-18 00:55:57 | METOP-C | BAIÃO | PARÁ | Brasil | 1501204 | 15 | 33 | nan | nan | nan | Amazônia | nan |


[Clique aqui para ver as próximas entradas](README11.md)
