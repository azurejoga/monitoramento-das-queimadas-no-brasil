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

## Dados Diários - Página 2

| ID | Latitude | Longitude | Data/Hora GMT | Satélite | Município | Estado | País | Município ID | Estado ID | País ID | Dias sem Chuva | Precipitação | Risco de Fogo | Bioma | FRP |
|----|----------|-----------|---------------|----------|-----------|--------|------|--------------|-----------|---------|----------------|--------------|----------------|-------|-----|
| 6b2aeba0-eea7-3d6b-bb86-d8fc27205a49 | -3.3367 | -44.4034 | 2025-11-18 00:10:00 | GOES-19 | ITAPECURU MIRIM | MARANHÃO | Brasil | 2105401 | 21 | 33 | nan | nan | nan | Cerrado | 60.8 |
| f8ed5a50-dff1-361b-9daa-275219881b70 | -5.4192 | -43.0347 | 2025-11-18 00:10:00 | GOES-19 | MATÕES | MARANHÃO | Brasil | 2106607 | 21 | 33 | nan | nan | nan | Cerrado | 158.6 |
| e93694ab-7160-3a8e-a580-73edbdd355c5 | -4.195 | -44.2247 | 2025-11-18 00:10:00 | GOES-19 | COROATÁ | MARANHÃO | Brasil | 2103604 | 21 | 33 | nan | nan | nan | Cerrado | 290.0 |
| cc7797c1-63a9-3581-a3b2-fe34de98c6cd | -8.3043 | -43.9842 | 2025-11-18 00:10:00 | GOES-19 | MANOEL EMÍDIO | PIAUÍ | Brasil | 2205904 | 22 | 33 | nan | nan | nan | Cerrado | 45.4 |
| eefdb7c7-94d3-30c6-91af-f0df8d9fd7c7 | -3.4584 | -46.0664 | 2025-11-18 00:10:00 | GOES-19 | GOVERNADOR NEWTON BELLO | MARANHÃO | Brasil | 2104651 | 21 | 33 | nan | nan | nan | Amazônia | 101.5 |
| b3a27cc3-54a7-3440-a4d3-af76861244f1 | -8.304 | -44.0075 | 2025-11-18 00:10:00 | GOES-19 | MANOEL EMÍDIO | PIAUÍ | Brasil | 2205904 | 22 | 33 | nan | nan | nan | Cerrado | 155.3 |
| 8673d9bf-2cce-3fce-9041-a36526635198 | -3.0236 | -47.8396 | 2025-11-18 00:10:00 | GOES-19 | PARAGOMINAS | PARÁ | Brasil | 1505502 | 15 | 33 | nan | nan | nan | Amazônia | 69.8 |
| 6c6f6f9f-a8c6-32c0-b76e-56b66bd60f69 | -4.1762 | -44.2486 | 2025-11-18 00:10:00 | GOES-19 | COROATÁ | MARANHÃO | Brasil | 2103604 | 21 | 33 | nan | nan | nan | Cerrado | 298.1 |
| cba183aa-b908-3fcd-85cb-41ec7e73ed40 | -9.1127 | -44.3102 | 2025-11-18 00:10:00 | GOES-19 | BOM JESUS | PIAUÍ | Brasil | 2201903 | 22 | 33 | nan | nan | nan | Cerrado | 105.9 |
| d89d4fc7-3203-3cb6-890a-1e233e92aeb7 | -15.4693 | -43.1804 | 2025-11-18 00:10:00 | GOES-19 | PAI PEDRO | MINAS GERAIS | Brasil | 3146552 | 31 | 33 | nan | nan | nan | Caatinga | 75.9 |
| be831a06-77bd-3d45-8b39-8bdad8a02cc5 | -3.4729 | -46.054298 | 2025-11-18 00:11:00 | METOP-B | GOVERNADOR NEWTON BELLO | MARANHÃO | Brasil | 2104651 | 21 | 33 | nan | nan | nan | Amazônia | nan |
| e75ee0f7-99ce-34b8-a822-3d7304db65a2 | -4.1017 | -45.611 | 2025-11-18 00:11:00 | METOP-B | SANTA LUZIA | MARANHÃO | Brasil | 2110005 | 21 | 33 | nan | nan | nan | Amazônia | nan |
| 7f9514b7-d625-3c45-b0d7-e3471e8a7847 | -6.2185 | -46.875 | 2025-11-18 00:11:00 | METOP-B | PORTO FRANCO | MARANHÃO | Brasil | 2109007 | 21 | 33 | nan | nan | nan | Cerrado | nan |
| 139e258e-4fb2-3125-9070-570bfc5a4893 | -3.6461 | -50.1521 | 2025-11-18 00:11:00 | METOP-B | PACAJÁ | PARÁ | Brasil | 1505486 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| 78aaf4f5-a1f7-34de-8cf5-e8f1b6b1cddc | -3.7851 | -49.264301 | 2025-11-18 00:11:00 | METOP-B | BREU BRANCO | PARÁ | Brasil | 1501782 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| 30eb47b4-00e0-3e31-baae-aaad87be1d84 | -3.522 | -50.3325 | 2025-11-18 00:11:00 | METOP-B | PACAJÁ | PARÁ | Brasil | 1505486 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| 70d0a3e4-59dc-35e6-85a9-edac84db8c67 | -2.2868 | -47.2131 | 2025-11-18 00:11:00 | METOP-B | GARRAFÃO DO NORTE | PARÁ | Brasil | 1503077 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| f2b90694-5ed6-35e0-b508-e7b695a8e786 | -2.4793 | -50.230701 | 2025-11-18 00:11:00 | METOP-B | BAGRE | PARÁ | Brasil | 1501105 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| deedb372-dc0a-367e-aeb2-75846657de78 | -10.8604 | -44.2598 | 2025-11-18 00:11:00 | METOP-B | SANTA RITA DE CÁSSIA | BAHIA | Brasil | 2928406 | 29 | 33 | nan | nan | nan | Cerrado | nan |
| efbac79c-e825-3114-9106-f67271e9b6bc | -2.5253 | -47.805199 | 2025-11-18 00:11:00 | METOP-B | IPIXUNA DO PARÁ | PARÁ | Brasil | 1503457 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| 8657d598-f7ae-3f6b-8cf4-5344eb71d3e3 | -10.8839 | -44.621899 | 2025-11-18 00:11:00 | METOP-B | SANTA RITA DE CÁSSIA | BAHIA | Brasil | 2928406 | 29 | 33 | nan | nan | nan | Cerrado | nan |
| 2a632353-cf23-3136-a2f7-9943972bb3d0 | -3.3622 | -50.1717 | 2025-11-18 00:11:00 | METOP-B | PACAJÁ | PARÁ | Brasil | 1505486 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| 1f807385-e2fa-350c-bec3-b94ce8a55bc6 | -2.3672 | -45.725101 | 2025-11-18 00:11:00 | METOP-B | PRESIDENTE MÉDICI | MARANHÃO | Brasil | 2109239 | 21 | 33 | nan | nan | nan | Amazônia | nan |
| fd546cda-b9d8-3273-8d8e-8fe50c355e69 | -2.9159 | -49.566002 | 2025-11-18 00:11:00 | METOP-B | BAIÃO | PARÁ | Brasil | 1501204 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| 4d603d8c-4f29-3811-bf59-c68e64f23101 | -3.467 | -46.073399 | 2025-11-18 00:11:00 | METOP-B | GOVERNADOR NEWTON BELLO | MARANHÃO | Brasil | 2104651 | 21 | 33 | nan | nan | nan | Amazônia | nan |
| 3c847753-23ad-3ebb-a737-ff5e5223ecaf | -4.1788 | -44.219101 | 2025-11-18 00:11:00 | METOP-B | COROATÁ | MARANHÃO | Brasil | 2103604 | 21 | 33 | nan | nan | nan | Cerrado | nan |
| 48c7c7a7-a10c-35fb-b88f-2233185351de | -6.2168 | -46.867599 | 2025-11-18 00:11:00 | METOP-B | PORTO FRANCO | MARANHÃO | Brasil | 2109007 | 21 | 33 | nan | nan | nan | Cerrado | nan |
| 947cae63-96d4-3d9e-9a4a-b8b196d013a7 | -4.1724 | -50.202499 | 2025-11-18 00:11:00 | METOP-B | NOVO REPARTIMENTO | PARÁ | Brasil | 1505064 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| d30d041b-deae-30af-8a51-3bdf8b745a72 | -10.8389 | -46.7439 | 2025-11-18 00:11:00 | METOP-B | MATEIROS | TOCANTINS | Brasil | 1712702 | 17 | 33 | nan | nan | nan | Cerrado | nan |
| d310f195-d4cc-3ffc-b2f0-3fff6baf5838 | -5.3364 | -43.756802 | 2025-11-18 00:11:00 | METOP-B | PARNARAMA | MARANHÃO | Brasil | 2107803 | 21 | 33 | nan | nan | nan | Cerrado | nan |
| 164e19b9-cbc5-338f-9431-49739cac50fc | -5.1642 | -44.337502 | 2025-11-18 00:11:00 | METOP-B | GONÇALVES DIAS | MARANHÃO | Brasil | 2104404 | 21 | 33 | nan | nan | nan | Cerrado | nan |
| 1b61fb8f-3c12-3882-8688-25e54ceebd81 | -11.6805 | -44.716301 | 2025-11-18 00:11:00 | METOP-B | RIACHÃO DAS NEVES | BAHIA | Brasil | 2926202 | 29 | 33 | nan | nan | nan | Cerrado | nan |
| 00a59056-dc14-38e0-abed-31b72a37d6e8 | -10.3495 | -48.920799 | 2025-11-18 00:11:00 | METOP-B | PUGMIL | TOCANTINS | Brasil | 1718451 | 17 | 33 | nan | nan | nan | Cerrado | nan |
| 829df749-8bd3-3d46-99b1-e8ee76a056bd | -3.3867 | -46.127201 | 2025-11-18 00:11:00 | METOP-B | GOVERNADOR NEWTON BELLO | MARANHÃO | Brasil | 2104651 | 21 | 33 | nan | nan | nan | Amazônia | nan |
| 6552e48a-5a5e-3508-b5f9-e9857f444005 | -3.5138 | -50.341499 | 2025-11-18 00:11:00 | METOP-B | PACAJÁ | PARÁ | Brasil | 1505486 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| 66b946c4-0491-3ed8-b6b9-d7bcb202a4c8 | -3.7772 | -47.736599 | 2025-11-18 00:11:00 | METOP-B | ULIANÓPOLIS | PARÁ | Brasil | 1508126 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| ffc1246f-279f-314d-bf2f-b34d1e679d87 | -11.2079 | -49.410999 | 2025-11-18 00:11:00 | METOP-B | DUERÉ | TOCANTINS | Brasil | 1707306 | 17 | 33 | nan | nan | nan | Cerrado | nan |
| 63e5a82f-6629-33a0-adbf-298449d9c56c | -6.9264 | -39.619999 | 2025-11-18 00:11:00 | METOP-B | ASSARÉ | CEARÁ | Brasil | 2301604 | 23 | 33 | nan | nan | nan | Caatinga | nan |
| 533b3edf-c030-340f-a58a-b1487706aafb | -2.3353 | -55.762901 | 2025-11-18 00:11:00 | METOP-B | SANTARÉM | PARÁ | Brasil | 1506807 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| ee8afe7d-dc4c-3f4d-b3e8-6e90acecd2f4 | -7.4348 | -45.183601 | 2025-11-18 00:11:00 | METOP-B | LORETO | MARANHÃO | Brasil | 2106102 | 21 | 33 | nan | nan | nan | Cerrado | nan |
| fc5ecf07-b773-3c71-86fb-dce67adc49f2 | -7.9208 | -46.029999 | 2025-11-18 00:11:00 | METOP-B | BALSAS | MARANHÃO | Brasil | 2101400 | 21 | 33 | nan | nan | nan | Cerrado | nan |
| 86e64991-5089-332b-8cb1-1817dd54fa2a | -13.3303 | -43.1791 | 2025-11-18 00:11:00 | METOP-B | BOM JESUS DA LAPA | BAHIA | Brasil | 2903904 | 29 | 33 | nan | nan | nan | Caatinga | nan |
| 70e08be6-df5a-3c0f-89de-9e32f7799c44 | -5.1294 | -43.839699 | 2025-11-18 00:11:00 | METOP-B | SÃO JOÃO DO SOTER | MARANHÃO | Brasil | 2111078 | 21 | 33 | nan | nan | nan | Cerrado | nan |
| d14438a1-dc92-3793-8f8c-a06a0a8b020f | -8.7962 | -44.392101 | 2025-11-18 00:11:00 | METOP-B | CURRAIS | PIAUÍ | Brasil | 2203230 | 22 | 33 | nan | nan | nan | Cerrado | nan |
| 3d083d5c-d023-388d-9c57-0f06afada654 | -3.176 | -46.598701 | 2025-11-18 00:11:00 | METOP-B | CENTRO NOVO DO MARANHÃO | MARANHÃO | Brasil | 2103174 | 21 | 33 | nan | nan | nan | Amazônia | nan |
| 447e5178-a2f5-3c5e-9c33-67cf07647d2e | -11.6786 | -44.708199 | 2025-11-18 00:11:00 | METOP-B | RIACHÃO DAS NEVES | BAHIA | Brasil | 2926202 | 29 | 33 | nan | nan | nan | Cerrado | nan |
| a384c938-2742-37f6-8768-d614713d3da7 | -9.3864 | -48.432098 | 2025-11-18 00:11:00 | METOP-B | MIRACEMA DO TOCANTINS | TOCANTINS | Brasil | 1713205 | 17 | 33 | nan | nan | nan | Cerrado | nan |
| e3726e90-6944-3ca0-bc42-fda90de5cb13 | -10.6081 | -42.306801 | 2025-11-18 00:11:00 | METOP-B | ITAGUAÇU DA BAHIA | BAHIA | Brasil | 2915353 | 29 | 33 | nan | nan | nan | Caatinga | nan |
| a3dbbb47-78e6-3189-8d4f-9d983493f1eb | -6.1151 | -42.959999 | 2025-11-18 00:11:00 | METOP-B | PALMEIRAIS | PIAUÍ | Brasil | 2207504 | 22 | 33 | nan | nan | nan | Caatinga | nan |
| ffc05877-ff10-3758-92dd-1e8a49ec265a | -12.8443 | -41.483002 | 2025-11-18 00:11:00 | METOP-B | MUCUGÊ | BAHIA | Brasil | 2921906 | 29 | 33 | nan | nan | nan | Caatinga | nan |
| ee121777-a794-3256-97b0-8701024be76f | -3.0799 | -50.335999 | 2025-11-18 00:11:00 | METOP-B | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| ee581242-110a-3a03-89be-3ee42d1be208 | -4.1708 | -50.195599 | 2025-11-18 00:11:00 | METOP-B | NOVO REPARTIMENTO | PARÁ | Brasil | 1505064 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| 6fdfb084-0a72-3d9b-a38f-0c6c5c0e8ebc | -4.1838 | -50.207298 | 2025-11-18 00:11:00 | METOP-B | NOVO REPARTIMENTO | PARÁ | Brasil | 1505064 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| 25effe51-c12b-3ff9-805e-a3fece2b9ef6 | -5.3313 | -43.735001 | 2025-11-18 00:11:00 | METOP-B | MATÕES | MARANHÃO | Brasil | 2106607 | 21 | 33 | nan | nan | nan | Cerrado | nan |
| 93a365f1-adc8-39c1-858e-a04d6e748746 | -3.4814 | -52.3494 | 2025-11-18 00:11:00 | METOP-B | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| 24fc02d8-7bc0-3dee-83c9-476105f83f27 | -11.6884 | -44.705799 | 2025-11-18 00:11:00 | METOP-B | RIACHÃO DAS NEVES | BAHIA | Brasil | 2926202 | 29 | 33 | nan | nan | nan | Cerrado | nan |
| b6b0690a-343b-318e-9115-5503a1103b3b | -7.545 | -47.0387 | 2025-11-18 00:11:00 | METOP-B | RIACHÃO | MARANHÃO | Brasil | 2109502 | 21 | 33 | nan | nan | nan | Cerrado | nan |
| d64cab93-b146-3686-ba94-0920b5cd7535 | -11.8531 | -49.2132 | 2025-11-18 00:11:00 | METOP-B | CARIRI DO TOCANTINS | TOCANTINS | Brasil | 1703867 | 17 | 33 | nan | nan | nan | Cerrado | nan |
| de3a216a-4c62-3531-a6bb-9c952e57c070 | -10.7269 | -44.437302 | 2025-11-18 00:11:00 | METOP-B | SANTA RITA DE CÁSSIA | BAHIA | Brasil | 2928406 | 29 | 33 | nan | nan | nan | Cerrado | nan |
| 05f65705-b270-3e92-94e6-7f1bf0129733 | -11.8433 | -49.215401 | 2025-11-18 00:11:00 | METOP-B | CARIRI DO TOCANTINS | TOCANTINS | Brasil | 1703867 | 17 | 33 | nan | nan | nan | Cerrado | nan |
| e65d586a-22ac-3087-ac3b-e7d4476aaa8f | -7.7921 | -42.607101 | 2025-11-18 00:11:00 | METOP-B | RIBEIRA DO PIAUÍ | PIAUÍ | Brasil | 2208874 | 22 | 33 | nan | nan | nan | Caatinga | nan |
| 74026fff-dc52-39a8-a5ea-79f4234c6da3 | -2.8211 | -46.712799 | 2025-11-18 00:11:00 | METOP-B | PARAGOMINAS | PARÁ | Brasil | 1505502 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| d03f5fa2-cadc-3964-91df-82872fc4e300 | -3.2792 | -52.410801 | 2025-11-18 00:11:00 | METOP-B | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| 8a4ce9b9-84a8-3c62-8ba5-4b8ede85dd62 | -7.5482 | -47.053001 | 2025-11-18 00:11:00 | METOP-B | RIACHÃO | MARANHÃO | Brasil | 2109502 | 21 | 33 | nan | nan | nan | Cerrado | nan |
| dd4aab48-5867-3810-92c5-1e97b401931f | -5.4229 | -43.035801 | 2025-11-18 00:11:00 | METOP-B | MATÕES | MARANHÃO | Brasil | 2106607 | 21 | 33 | nan | nan | nan | Cerrado | nan |
| a9a25f21-35e7-3879-a547-2d3bf4f9e803 | -6.4086 | -47.433701 | 2025-11-18 00:11:00 | METOP-B | TOCANTINÓPOLIS | TOCANTINS | Brasil | 1721208 | 17 | 33 | nan | nan | nan | Cerrado | nan |
| 981fa2ba-52be-35e4-9602-001637d52860 | -3.2741 | -50.010601 | 2025-11-18 00:11:00 | METOP-B | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| bafb5d34-52d9-36cb-ba16-b0dd4e2e4793 | -4.6493 | -47.944302 | 2025-11-18 00:11:00 | METOP-B | RONDON DO PARÁ | PARÁ | Brasil | 1506187 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| ef8605f0-1232-3e4d-9b24-d1e92e78df3c | -3.6684 | -50.2052 | 2025-11-18 00:11:00 | METOP-B | PACAJÁ | PARÁ | Brasil | 1505486 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| 0fbc3466-be2a-368f-82b0-998703494550 | -2.7162 | -45.141899 | 2025-11-18 00:11:00 | METOP-B | PINHEIRO | MARANHÃO | Brasil | 2108603 | 21 | 33 | nan | nan | nan | Amazônia | nan |
| 4c5d5e33-2fae-3ab1-94a4-09f618bc1176 | -4.4426 | -44.202301 | 2025-11-18 00:11:00 | METOP-B | PERITORÓ | MARANHÃO | Brasil | 2108454 | 21 | 33 | nan | nan | nan | Cerrado | nan |
| b2fdabae-f0e0-379d-aedb-9a5f85157358 | -10.0923 | -44.767601 | 2025-11-18 00:11:00 | METOP-B | PARNAGUÁ | PIAUÍ | Brasil | 2207603 | 22 | 33 | nan | nan | nan | Cerrado | nan |
| 4da544f1-1de5-322b-92c7-968f51e59412 | -7.7949 | -42.6189 | 2025-11-18 00:11:00 | METOP-B | RIBEIRA DO PIAUÍ | PIAUÍ | Brasil | 2208874 | 22 | 33 | nan | nan | nan | Caatinga | nan |
| f18dc834-4b3c-3c12-ac68-cede55bf8c0f | -11.297 | -48.507099 | 2025-11-18 00:11:00 | METOP-B | BREJINHO DE NAZARÉ | TOCANTINS | Brasil | 1703701 | 17 | 33 | nan | nan | nan | Cerrado | nan |
| a71c5a9e-e269-3eaf-b2c3-2be27f0578cf | -13.5232 | -42.992199 | 2025-11-18 00:11:00 | METOP-B | RIACHO DE SANTANA | BAHIA | Brasil | 2926400 | 29 | 33 | nan | nan | nan | Caatinga | nan |
| 520608b7-b1c3-3f73-a514-339615eba18e | -3.0244 | -44.474602 | 2025-11-18 00:11:00 | METOP-B | BACABEIRA | MARANHÃO | Brasil | 2101251 | 21 | 33 | nan | nan | nan | Amazônia | nan |
| 179e5fdf-3eb0-39b2-b493-c1d744721124 | -3.9247 | -50.017601 | 2025-11-18 00:11:00 | METOP-B | TUCURUÍ | PARÁ | Brasil | 1508100 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| 1a3dad0b-8507-37f8-b8cd-f4134ca63456 | -3.6477 | -50.159 | 2025-11-18 00:11:00 | METOP-B | PACAJÁ | PARÁ | Brasil | 1505486 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| 2f952dab-caac-397f-8ad4-84e133197ae3 | -7.354 | -46.209999 | 2025-11-18 00:11:00 | METOP-B | RIACHÃO | MARANHÃO | Brasil | 2109502 | 21 | 33 | nan | nan | nan | Cerrado | nan |
| 42ac7a46-3ee9-3fa9-9e0e-dfc8cb9ca11a | -2.4695 | -50.232899 | 2025-11-18 00:11:00 | METOP-B | BAGRE | PARÁ | Brasil | 1501105 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| 42502727-f2e8-341d-ab7d-41b7eeb3f3f8 | -7.5352 | -47.040901 | 2025-11-18 00:11:00 | METOP-B | RIACHÃO | MARANHÃO | Brasil | 2109502 | 21 | 33 | nan | nan | nan | Cerrado | nan |
| c131b4e8-195c-3022-860f-aa39541fe99c | -4.1765 | -44.252998 | 2025-11-18 00:11:00 | METOP-B | COROATÁ | MARANHÃO | Brasil | 2103604 | 21 | 33 | nan | nan | nan | Cerrado | nan |
| 0bc621f3-5269-3ac1-bf2b-da0e7bb56725 | -10.858 | -44.075298 | 2025-11-18 00:11:00 | METOP-B | MANSIDÃO | BAHIA | Brasil | 2920452 | 29 | 33 | nan | nan | nan | Cerrado | nan |
| 51241370-b20f-3cd2-b7e3-82c30ee7502f | -3.8046 | -50.1241 | 2025-11-18 00:11:00 | METOP-B | PACAJÁ | PARÁ | Brasil | 1505486 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| 79c47035-714d-3211-8c0e-4651a4fdba1d | -8.7941 | -44.383099 | 2025-11-18 00:11:00 | METOP-B | CURRAIS | PIAUÍ | Brasil | 2203230 | 22 | 33 | nan | nan | nan | Cerrado | nan |
| 1390427f-391f-3577-80e2-2cb30c0fbd03 | -3.3539 | -44.3876 | 2025-11-18 00:11:00 | METOP-B | ITAPECURU MIRIM | MARANHÃO | Brasil | 2105401 | 21 | 33 | nan | nan | nan | Cerrado | nan |
| 0599f607-6e4e-3508-9d6e-bbf8e258da42 | -9.0497 | -45.427502 | 2025-11-18 00:11:00 | METOP-B | BAIXA GRANDE DO RIBEIRO | PIAUÍ | Brasil | 2201150 | 22 | 33 | nan | nan | nan | Cerrado | nan |
| 52236c92-40ed-399a-9822-46b74cd5328a | -10.8524 | -44.095299 | 2025-11-18 00:11:00 | METOP-B | MANSIDÃO | BAHIA | Brasil | 2920452 | 29 | 33 | nan | nan | nan | Cerrado | nan |
| e5dbb07d-1491-32ea-bf38-7981b85d9df0 | -3.4748 | -46.062698 | 2025-11-18 00:11:00 | METOP-B | GOVERNADOR NEWTON BELLO | MARANHÃO | Brasil | 2104651 | 21 | 33 | nan | nan | nan | Amazônia | nan |
| d8c09a3d-4541-316a-8499-1eadcbfe363d | -2.6891 | -49.1572 | 2025-11-18 00:11:00 | METOP-B | MOJU | PARÁ | Brasil | 1504703 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| 20a922f5-0bb4-31b9-8b2b-6f76ac5df926 | -3.4607 | -50.1063 | 2025-11-18 00:11:00 | METOP-B | PACAJÁ | PARÁ | Brasil | 1505486 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| e5b1c28a-7785-3ac7-b792-a52c7ac83149 | -6.1123 | -42.948101 | 2025-11-18 00:11:00 | METOP-B | PALMEIRAIS | PIAUÍ | Brasil | 2207504 | 22 | 33 | nan | nan | nan | Caatinga | nan |
| 5256c683-3109-3b0e-9351-09aa28907a43 | -9.0306 | -47.449402 | 2025-11-18 00:11:00 | METOP-B | CENTENÁRIO | TOCANTINS | Brasil | 1704105 | 17 | 33 | nan | nan | nan | Cerrado | nan |
| a0967cdf-2f95-35db-961e-0805bd4440f3 | -9.3911 | -48.4529 | 2025-11-18 00:11:00 | METOP-B | MIRACEMA DO TOCANTINS | TOCANTINS | Brasil | 1713205 | 17 | 33 | nan | nan | nan | Cerrado | nan |
| b97142f9-4552-3bd0-a5f4-d352791dcb16 | -7.427 | -45.194302 | 2025-11-18 00:11:00 | METOP-B | LORETO | MARANHÃO | Brasil | 2106102 | 21 | 33 | nan | nan | nan | Cerrado | nan |
| f9883564-2735-374e-92dc-7ce399c9a232 | -2.5236 | -47.797901 | 2025-11-18 00:11:00 | METOP-B | IPIXUNA DO PARÁ | PARÁ | Brasil | 1503457 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| 073dc1ca-7467-315f-888f-f29e29140d37 | -4.1806 | -50.193401 | 2025-11-18 00:11:00 | METOP-B | NOVO REPARTIMENTO | PARÁ | Brasil | 1505064 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| 30fa604d-e613-378a-a419-b27a0ca54f19 | -7.5466 | -47.045799 | 2025-11-18 00:11:00 | METOP-B | RIACHÃO | MARANHÃO | Brasil | 2109502 | 21 | 33 | nan | nan | nan | Cerrado | nan |
| 8ca048f9-0120-3178-85ec-2060366d08c9 | -3.9232 | -50.0107 | 2025-11-18 00:11:00 | METOP-B | TUCURUÍ | PARÁ | Brasil | 1508100 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| 02bc5b9b-ddaf-3986-aed3-abdf318dec38 | -3.2384 | -50.490398 | 2025-11-18 00:11:00 | METOP-B | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | nan |


[Clique aqui para ver as próximas entradas](README3.md)
