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
| 568280a2-fe3c-3fd5-96ce-aee208a96c78 | -5.77292 | -44.38451 | 2025-11-15 04:04:00 | NPP-375D | SÃO DOMINGOS DO MARANHÃO | MARANHÃO | Brasil | 2110708 | 21 | 33 | nan | nan | nan | Cerrado | 0.8 |
| 982a8a08-2bc0-3e1a-af7b-5db2d14f5d08 | -5.08275 | -42.65519 | 2025-11-15 04:04:00 | NPP-375D | TERESINA | PIAUÍ | Brasil | 2211001 | 22 | 33 | nan | nan | nan | Cerrado | 1.8 |
| 8e94dc2e-53e9-3d95-af10-bcb869d2cf9e | -5.33883 | -43.0361 | 2025-11-15 04:04:00 | NPP-375D | TIMON | MARANHÃO | Brasil | 2112209 | 21 | 33 | nan | nan | nan | Cerrado | 3.6 |
| 19f9fba7-e5a2-38be-87bc-9e2d38cd0436 | -4.19305 | -43.80844 | 2025-11-15 04:04:00 | NPP-375D | TIMBIRAS | MARANHÃO | Brasil | 2112100 | 21 | 33 | nan | nan | nan | Cerrado | 1.0 |
| af5d698f-96df-3b41-9bef-e92c0bd05ef0 | -2.8704 | -51.47804 | 2025-11-15 04:04:00 | NPP-375D | ANAPU | PARÁ | Brasil | 1500859 | 15 | 33 | nan | nan | nan | Amazônia | 1.0 |
| 065f8a57-b406-3901-9e99-e07cc8d4d620 | -1.05368 | -48.94595 | 2025-11-15 04:04:00 | NPP-375D | PONTA DE PEDRAS | PARÁ | Brasil | 1505700 | 15 | 33 | nan | nan | nan | Amazônia | 1.2 |
| 325d789b-3332-3f0e-b4c7-376d11e04b63 | -4.26741 | -46.84196 | 2025-11-15 04:04:00 | NPP-375D | BOM JARDIM | MARANHÃO | Brasil | 2102002 | 21 | 33 | nan | nan | nan | Amazônia | 1.0 |
| 7d8df6dc-a5ca-3f1a-9c7b-98b1542a8cee | -2.79568 | -52.97543 | 2025-11-15 04:04:00 | NPP-375D | MEDICILÂNDIA | PARÁ | Brasil | 1504455 | 15 | 33 | nan | nan | nan | Amazônia | 2.3 |
| d8aa177f-2420-322a-a81b-cb3b9bc04130 | -7.07789 | -41.58426 | 2025-11-15 04:04:00 | NPP-375D | PICOS | PIAUÍ | Brasil | 2208007 | 22 | 33 | nan | nan | nan | Caatinga | 1.4 |
| b5b926a0-2f8c-3568-984a-db304108255e | -5.33814 | -43.04037 | 2025-11-15 04:04:00 | NPP-375D | TIMON | MARANHÃO | Brasil | 2112209 | 21 | 33 | nan | nan | nan | Cerrado | 3.6 |
| dfa0f114-a01b-371a-a6d8-d5aae2d0c66d | -3.01446 | -49.43261 | 2025-11-15 04:04:00 | NPP-375D | MOJU | PARÁ | Brasil | 1504703 | 15 | 33 | nan | nan | nan | Amazônia | 1.7 |
| 4f7bb0c3-02bd-3324-a586-e2d8ef10bfe1 | -3.99173 | -44.27648 | 2025-11-15 04:04:00 | NPP-375D | COROATÁ | MARANHÃO | Brasil | 2103604 | 21 | 33 | nan | nan | nan | Cerrado | 1.6 |
| 0e21bf6e-6fc4-35a3-a38b-ace43fe44d3a | -7.40086 | -41.00558 | 2025-11-15 04:04:00 | NPP-375D | BELÉM DO PIAUÍ | PIAUÍ | Brasil | 2201572 | 22 | 33 | nan | nan | nan | Caatinga | 1.8 |
| 68abc913-f167-301b-9b0f-404fffeb2f2d | -4.20029 | -48.56325 | 2025-11-15 04:04:00 | NPP-375D | RONDON DO PARÁ | PARÁ | Brasil | 1506187 | 15 | 33 | nan | nan | nan | Amazônia | 3.0 |
| 0fa86fe8-2042-39b5-8275-ee25c2d1680e | -4.27867 | -46.06544 | 2025-11-15 04:04:00 | NPP-375D | SANTA LUZIA | MARANHÃO | Brasil | 2110005 | 21 | 33 | nan | nan | nan | Amazônia | 0.9 |
| 1d7fe741-51fc-3f4a-94db-94a461d4a750 | -5.52022 | -40.97041 | 2025-11-15 04:04:00 | NPP-375D | SÃO MIGUEL DO TAPUIO | PIAUÍ | Brasil | 2210409 | 22 | 33 | nan | nan | nan | Caatinga | 4.1 |
| 717e9306-f33b-3c8c-8e25-7ea1313e18d6 | -3.76259 | -47.75003 | 2025-11-15 04:04:00 | NPP-375D | ULIANÓPOLIS | PARÁ | Brasil | 1508126 | 15 | 33 | nan | nan | nan | Amazônia | 1.2 |
| 702ffe86-03be-3b74-9e0a-4d571de484f2 | -5.22411 | -44.43439 | 2025-11-15 04:04:00 | NPP-375D | PRESIDENTE DUTRA | MARANHÃO | Brasil | 2109106 | 21 | 33 | nan | nan | nan | Cerrado | 0.9 |
| 861b8113-b565-37ed-aeb0-62fdf53119a7 | -5.97948 | -42.86181 | 2025-11-15 04:04:00 | NPP-375D | PALMEIRAIS | PIAUÍ | Brasil | 2207504 | 22 | 33 | nan | nan | nan | Caatinga | 4.6 |
| 4787aa6a-2236-36e7-8a85-018a45203e27 | -6.28441 | -41.75915 | 2025-11-15 04:04:00 | NPP-375D | VALENÇA DO PIAUÍ | PIAUÍ | Brasil | 2211308 | 22 | 33 | nan | nan | nan | Caatinga | 3.5 |
| e3959b6d-b20f-326e-bf38-992bd6b6722a | -2.51817 | -47.80873 | 2025-11-15 04:04:00 | NPP-375D | IPIXUNA DO PARÁ | PARÁ | Brasil | 1503457 | 15 | 33 | nan | nan | nan | Amazônia | 12.4 |
| faa95576-eadf-39ae-a8d6-9a6d1aa177e4 | -5.22953 | -44.35108 | 2025-11-15 04:04:00 | NPP-375D | GONÇALVES DIAS | MARANHÃO | Brasil | 2104404 | 21 | 33 | nan | nan | nan | Cerrado | 23.4 |
| 38d759f9-c9f4-3125-a542-27f37dbdd015 | -7.49557 | -42.55609 | 2025-11-15 04:04:00 | NPP-375D | SÃO JOSÉ DO PEIXE | PIAUÍ | Brasil | 2210102 | 22 | 33 | nan | nan | nan | Caatinga | 12.7 |
| 0335d3e9-b6be-37ce-ac25-d4a2de255688 | -4.53936 | -46.41484 | 2025-11-15 04:04:00 | NPP-375D | BURITICUPU | MARANHÃO | Brasil | 2102325 | 21 | 33 | nan | nan | nan | Amazônia | 1.3 |
| 2dc7ed86-225b-34fd-8e34-a97519a27e2f | -4.85929 | -43.25554 | 2025-11-15 04:04:00 | NPP-375D | CAXIAS | MARANHÃO | Brasil | 2103000 | 21 | 33 | nan | nan | nan | Cerrado | 7.7 |
| fc28a08f-3fc8-3aec-8f01-3b1745f3a012 | -5.72458 | -42.36454 | 2025-11-15 04:04:00 | NPP-375D | PASSAGEM FRANCA DO PIAUÍ | PIAUÍ | Brasil | 2207751 | 22 | 33 | nan | nan | nan | Caatinga | 1.9 |
| 50cd5388-2bd2-3486-9da8-53f6a3433672 | -5.04088 | -43.60733 | 2025-11-15 04:04:00 | NPP-375D | SÃO JOÃO DO SOTER | MARANHÃO | Brasil | 2111078 | 21 | 33 | nan | nan | nan | Cerrado | 19.4 |
| d3515c5f-4dc4-35f4-bdc6-5da77642c6ad | -2.51715 | -47.81504 | 2025-11-15 04:04:00 | NPP-375D | IPIXUNA DO PARÁ | PARÁ | Brasil | 1503457 | 15 | 33 | nan | nan | nan | Amazônia | 15.9 |
| ecdf5393-067d-3468-b044-d2adfef327a2 | -7.53601 | -41.17254 | 2025-11-15 04:04:00 | NPP-375D | MASSAPÊ DO PIAUÍ | PIAUÍ | Brasil | 2206050 | 22 | 33 | nan | nan | nan | Caatinga | 3.5 |
| c3a2cbc5-9bc0-34b4-8d74-3f8d186b22e1 | -4.85484 | -43.25937 | 2025-11-15 04:04:00 | NPP-375D | CAXIAS | MARANHÃO | Brasil | 2103000 | 21 | 33 | nan | nan | nan | Cerrado | 2.3 |
| 9c969aba-5a43-30d5-989b-06710cdc3c05 | -7.42523 | -45.22967 | 2025-11-15 04:04:00 | NPP-375D | LORETO | MARANHÃO | Brasil | 2106102 | 21 | 33 | nan | nan | nan | Cerrado | 1.6 |
| 801a38e0-aa81-3bfb-9d5a-041a66f866b6 | -6.81769 | -48.82723 | 2025-11-15 04:04:00 | NPP-375D | ARAGOMINAS | TOCANTINS | Brasil | 1701309 | 17 | 33 | nan | nan | nan | Amazônia | 0.8 |
| a22bbe92-f34d-3acc-9f4b-14aecc857f0f | -3.22033 | -45.47835 | 2025-11-15 04:04:00 | NPP-375D | PENALVA | MARANHÃO | Brasil | 2108306 | 21 | 33 | nan | nan | nan | Amazônia | 3.4 |
| 00ef723d-8328-3a8b-be9d-205d55731e53 | -5.35679 | -41.74352 | 2025-11-15 04:04:00 | NPP-375D | CASTELO DO PIAUÍ | PIAUÍ | Brasil | 2202604 | 22 | 33 | nan | nan | nan | Caatinga | 1.2 |
| f75a5aa8-ad34-3b3f-a1de-21ec2b402cc1 | -5.65672 | -35.44265 | 2025-11-15 04:04:00 | NPP-375D | CEARÁ-MIRIM | RIO GRANDE DO NORTE | Brasil | 2402600 | 24 | 33 | nan | nan | nan | Caatinga | 1.5 |
| d37e30f7-e136-3652-88ad-1e9e78092f75 | -3.70678 | -47.63032 | 2025-11-15 04:04:00 | NPP-375D | ULIANÓPOLIS | PARÁ | Brasil | 1508126 | 15 | 33 | nan | nan | nan | Amazônia | 1.9 |
| 96985b99-6af6-3b01-b282-c74fbcd8e874 | -6.15057 | -48.04128 | 2025-11-15 04:04:00 | NPP-375D | ANANÁS | TOCANTINS | Brasil | 1701002 | 17 | 33 | nan | nan | nan | Cerrado | 4.0 |
| 6d5a86a8-bf9b-3422-bf35-1ff84ab21c04 | -7.45761 | -42.76344 | 2025-11-15 04:04:00 | NPP-375D | FLORES DO PIAUÍ | PIAUÍ | Brasil | 2203800 | 22 | 33 | nan | nan | nan | Caatinga | 1.2 |
| 2c999067-f577-36b9-a07c-2c4f7c383acc | -6.10019 | -41.71119 | 2025-11-15 04:04:00 | NPP-375D | AROAZES | PIAUÍ | Brasil | 2200905 | 22 | 33 | nan | nan | nan | Caatinga | 3.1 |
| f54dbb2d-247e-3582-b46f-2ac941e3f543 | -4.27214 | -46.84283 | 2025-11-15 04:04:00 | NPP-375D | BOM JARDIM | MARANHÃO | Brasil | 2102002 | 21 | 33 | nan | nan | nan | Amazônia | 3.1 |
| 9bc7e182-4d02-3e8f-bd04-23abaad9b1bd | -3.47475 | -45.65421 | 2025-11-15 04:04:00 | NPP-375D | GOVERNADOR NEWTON BELLO | MARANHÃO | Brasil | 2104651 | 21 | 33 | nan | nan | nan | Amazônia | 2.0 |
| a1400301-ee26-33f1-a403-26b154d3d8f6 | -3.47102 | -45.64919 | 2025-11-15 04:04:00 | NPP-375D | GOVERNADOR NEWTON BELLO | MARANHÃO | Brasil | 2104651 | 21 | 33 | nan | nan | nan | Amazônia | 1.4 |
| f9585f69-ba8e-3550-adbd-4de60ef70d97 | -4.33013 | -47.57224 | 2025-11-15 04:04:00 | NPP-375D | DOM ELISEU | PARÁ | Brasil | 1502939 | 15 | 33 | nan | nan | nan | Amazônia | 1.7 |
| 4f31e392-e9ac-366d-866e-fa46d8f982b1 | -2.73299 | -45.30161 | 2025-11-15 04:04:00 | NPP-375D | PINHEIRO | MARANHÃO | Brasil | 2108603 | 21 | 33 | nan | nan | nan | Amazônia | 1.1 |
| 031b251c-39e7-35c6-9bef-98430a92d9b5 | -7.12703 | -41.6478 | 2025-11-15 04:04:00 | NPP-375D | PAQUETÁ | PIAUÍ | Brasil | 2207553 | 22 | 33 | nan | nan | nan | Caatinga | 2.1 |
| 611728ab-a94a-3e8d-91a9-476b6684b990 | -2.71555 | -47.39993 | 2025-11-15 04:04:00 | NPP-375D | IPIXUNA DO PARÁ | PARÁ | Brasil | 1503457 | 15 | 33 | nan | nan | nan | Amazônia | 1.2 |
| 769c3d61-ae9b-346a-9fc3-f18339486e1a | -3.14184 | -49.23534 | 2025-11-15 04:04:00 | NPP-375D | MOJU | PARÁ | Brasil | 1504703 | 15 | 33 | nan | nan | nan | Amazônia | 0.6 |
| c1c97bd2-8fb9-31cb-8577-69d25bbaca16 | -3.86111 | -49.13689 | 2025-11-15 04:04:00 | NPP-375D | GOIANÉSIA DO PARÁ | PARÁ | Brasil | 1503093 | 15 | 33 | nan | nan | nan | Amazônia | 1.4 |
| 2dad70ba-1845-38f5-89da-1e8b80acf9a6 | -5.51083 | -40.5458 | 2025-11-15 04:04:00 | NPP-375D | INDEPENDÊNCIA | CEARÁ | Brasil | 2305605 | 23 | 33 | nan | nan | nan | Caatinga | 2.6 |
| 0acde589-7814-3447-9152-bd9f96f993cc | -3.37099 | -41.17051 | 2025-11-15 04:04:00 | NPP-375D | VIÇOSA DO CEARÁ | CEARÁ | Brasil | 2314102 | 23 | 33 | nan | nan | nan | Caatinga | 1.9 |
| c3bdd91d-2a8d-3b16-897f-c213931bd309 | -7.29109 | -45.11546 | 2025-11-15 04:04:00 | NPP-375D | LORETO | MARANHÃO | Brasil | 2106102 | 21 | 33 | nan | nan | nan | Cerrado | 1.1 |
| 3aa0758d-b8cc-3fd9-9195-1e1005623d0a | -3.78426 | -42.44777 | 2025-11-15 04:04:00 | NPP-375D | SÃO JOÃO DO ARRAIAL | PIAUÍ | Brasil | 2209971 | 22 | 33 | nan | nan | nan | Cerrado | 0.7 |
| 508b7056-f87b-3952-bfbd-3778d922e9c5 | -4.1878 | -50.42173 | 2025-11-15 04:04:00 | NPP-375D | NOVO REPARTIMENTO | PARÁ | Brasil | 1505064 | 15 | 33 | nan | nan | nan | Amazônia | 1.0 |
| 0c8339c4-edde-3f2e-83b4-4f6252be30d1 | -7.38472 | -39.6321 | 2025-11-15 04:04:00 | NPP-375D | SANTANA DO CARIRI | CEARÁ | Brasil | 2312106 | 23 | 33 | nan | nan | nan | Caatinga | 1.3 |
| aa901aa8-f844-37b7-b900-adf69b50414b | -4.54816 | -43.21923 | 2025-11-15 04:04:00 | NPP-375D | ALDEIAS ALTAS | MARANHÃO | Brasil | 2100303 | 21 | 33 | nan | nan | nan | Cerrado | 30.6 |
| 5b3e1799-6781-3da4-9686-8255c83ba38b | -5.23743 | -44.35246 | 2025-11-15 04:04:00 | NPP-375D | GONÇALVES DIAS | MARANHÃO | Brasil | 2104404 | 21 | 33 | nan | nan | nan | Cerrado | 33.3 |
| 4a4d414b-3a81-3598-a278-1c409bd2ec2f | -5.16513 | -44.84817 | 2025-11-15 04:04:00 | NPP-375D | BARRA DO CORDA | MARANHÃO | Brasil | 2101608 | 21 | 33 | nan | nan | nan | Cerrado | 1.2 |
| 418f755a-1a54-3bbb-b9b0-115513bc39be | -6.88073 | -41.59318 | 2025-11-15 04:04:00 | NPP-375D | PICOS | PIAUÍ | Brasil | 2208007 | 22 | 33 | nan | nan | nan | Caatinga | 0.8 |
| c6b5f9aa-c33d-3447-99be-c45a4d474d9b | -5.82264 | -46.47808 | 2025-11-15 04:04:00 | NPP-375D | SÍTIO NOVO | MARANHÃO | Brasil | 2111805 | 21 | 33 | nan | nan | nan | Cerrado | 1.6 |
| f6e0f6e3-9b6f-3713-b422-1053e8fd2d6d | -5.61067 | -41.0617 | 2025-11-15 04:04:00 | NPP-375D | SÃO MIGUEL DO TAPUIO | PIAUÍ | Brasil | 2210409 | 22 | 33 | nan | nan | nan | Caatinga | 1.8 |
| a8af880e-3550-3b78-92a4-bbece155ec2f | -5.42188 | -43.26085 | 2025-11-15 04:04:00 | NPP-375D | MATÕES | MARANHÃO | Brasil | 2106607 | 21 | 33 | nan | nan | nan | Cerrado | 6.6 |
| 0ad23f3c-5a6d-37b1-b60c-1a1c254adb2a | -2.95435 | -41.97295 | 2025-11-15 04:04:00 | NPP-375D | ARAIOSES | MARANHÃO | Brasil | 2100907 | 21 | 33 | nan | nan | nan | Caatinga | 1.6 |
| 16223647-7400-357e-af48-39e41eebdf40 | -7.42928 | -45.23037 | 2025-11-15 04:04:00 | NPP-375D | LORETO | MARANHÃO | Brasil | 2106102 | 21 | 33 | nan | nan | nan | Cerrado | 1.4 |
| b3545384-494b-3b01-b439-add51c007086 | -5.42929 | -42.57696 | 2025-11-15 04:04:00 | NPP-375D | LAGOA DO PIAUÍ | PIAUÍ | Brasil | 2205581 | 22 | 33 | nan | nan | nan | Caatinga | 1.9 |
| 893c3c6a-2945-3b36-8e28-80d0ec20c3f0 | -3.86295 | -49.12605 | 2025-11-15 04:04:00 | NPP-375D | GOIANÉSIA DO PARÁ | PARÁ | Brasil | 1503093 | 15 | 33 | nan | nan | nan | Amazônia | 1.4 |
| fa5ed5df-44f8-36a1-a776-a7eb05fef42f | -4.46497 | -45.64606 | 2025-11-15 04:04:00 | NPP-375D | BREJO DE AREIA | MARANHÃO | Brasil | 2102150 | 21 | 33 | nan | nan | nan | Amazônia | 1.4 |
| 9ceeb7ed-a7d8-351b-af7c-72fa796f9720 | -5.85183 | -44.38852 | 2025-11-15 04:04:00 | NPP-375D | JATOBÁ | MARANHÃO | Brasil | 2105450 | 21 | 33 | nan | nan | nan | Cerrado | 1.1 |
| b3d4e80d-1626-3bdd-a9ff-1f793d4f8099 | -3.90969 | -45.79884 | 2025-11-15 04:04:00 | NPP-375D | SANTA LUZIA | MARANHÃO | Brasil | 2110005 | 21 | 33 | nan | nan | nan | Amazônia | 1.1 |
| 2950a891-07b2-3221-9489-107f00b563ec | -6.52981 | -39.06702 | 2025-11-15 04:04:00 | NPP-375D | CEDRO | CEARÁ | Brasil | 2303808 | 23 | 33 | nan | nan | nan | Caatinga | 1.5 |
| 5aa3fed5-da34-322b-89a4-7945b1c46ff3 | -7.45697 | -42.76738 | 2025-11-15 04:04:00 | NPP-375D | FLORES DO PIAUÍ | PIAUÍ | Brasil | 2203800 | 22 | 33 | nan | nan | nan | Caatinga | 1.2 |
| ada9b08d-cd38-3e33-a175-b058e82a693e | -4.24837 | -48.2123 | 2025-11-15 04:04:00 | NPP-375D | RONDON DO PARÁ | PARÁ | Brasil | 1506187 | 15 | 33 | nan | nan | nan | Amazônia | 1.3 |
| d2dd5370-22e6-3c3c-8cbb-c333688d1bd2 | -4.25519 | -48.20365 | 2025-11-15 04:04:00 | NPP-375D | RONDON DO PARÁ | PARÁ | Brasil | 1506187 | 15 | 33 | nan | nan | nan | Amazônia | 2.3 |
| 1504639a-782c-36ce-a107-81b108f7e57e | -3.66001 | -44.81174 | 2025-11-15 04:04:00 | NPP-375D | VITÓRIA DO MEARIM | MARANHÃO | Brasil | 2112902 | 21 | 33 | nan | nan | nan | Amazônia | 3.2 |
| bf486b81-857d-3978-a70b-1f3b38c05c9f | -6.97455 | -38.79359 | 2025-11-15 04:04:00 | NPP-375D | AURORA | CEARÁ | Brasil | 2301703 | 23 | 33 | nan | nan | nan | Caatinga | 2.1 |
| 22416f74-8b1b-35a0-88f8-c516f65961cf | -3.0556 | -47.11565 | 2025-11-15 04:04:00 | NPP-375D | PARAGOMINAS | PARÁ | Brasil | 1505502 | 15 | 33 | nan | nan | nan | Amazônia | 2.3 |
| 7ddb7fa6-46dc-3dba-b796-dc2f81c3f46a | -2.73805 | -45.29821 | 2025-11-15 04:04:00 | NPP-375D | PINHEIRO | MARANHÃO | Brasil | 2108603 | 21 | 33 | nan | nan | nan | Amazônia | 2.9 |
| 647328e0-0dc2-3ca7-b79b-cac8342754f9 | -3.61211 | -43.36892 | 2025-11-15 04:04:00 | NPP-375D | MATA ROMA | MARANHÃO | Brasil | 2106409 | 21 | 33 | nan | nan | nan | Cerrado | 0.9 |
| bb88a2bb-cac1-3d98-b11e-4fded7ad31cb | -3.5717 | -44.55939 | 2025-11-15 04:04:00 | NPP-375D | MIRANDA DO NORTE | MARANHÃO | Brasil | 2106755 | 21 | 33 | nan | nan | nan | Cerrado | 1.0 |
| 70f7621f-b670-3e48-ad6d-db1235cb9a60 | -5.5405 | -42.69397 | 2025-11-15 04:04:00 | NPP-375D | MONSENHOR GIL | PIAUÍ | Brasil | 2206407 | 22 | 33 | nan | nan | nan | Caatinga | 1.1 |
| aef6a6fc-669d-3c50-9ed5-f56f221d231c | -4.60144 | -45.95977 | 2025-11-15 04:04:00 | NPP-375D | SANTA LUZIA | MARANHÃO | Brasil | 2110005 | 21 | 33 | nan | nan | nan | Amazônia | 0.7 |
| dc72b215-f47a-3e0b-8d4b-afc0b4ef8249 | -5.63037 | -43.93202 | 2025-11-15 04:04:00 | NPP-375D | FORTUNA | MARANHÃO | Brasil | 2104206 | 21 | 33 | nan | nan | nan | Cerrado | 0.7 |
| df406a87-47e9-34f2-a9c2-496ce43d8f02 | -4.98379 | -47.24065 | 2025-11-15 04:04:00 | NPP-375D | AÇAILÂNDIA | MARANHÃO | Brasil | 2100055 | 21 | 33 | nan | nan | nan | Amazônia | 2.0 |
| 7ef5359d-e971-3b4a-800c-ba6bdd1ae708 | -4.72806 | -47.15661 | 2025-11-15 04:04:00 | NPP-375D | AÇAILÂNDIA | MARANHÃO | Brasil | 2100055 | 21 | 33 | nan | nan | nan | Amazônia | 25.4 |
| c94c49fe-f992-3d5a-8091-22f9f38257f0 | -7.4464 | -42.76564 | 2025-11-15 04:04:00 | NPP-375D | FLORES DO PIAUÍ | PIAUÍ | Brasil | 2203800 | 22 | 33 | nan | nan | nan | Caatinga | 2.3 |
| e2622b3c-41be-3fa4-980e-4722b0e77078 | -5.77543 | -44.38657 | 2025-11-15 04:04:00 | NPP-375D | SÃO DOMINGOS DO MARANHÃO | MARANHÃO | Brasil | 2110708 | 21 | 33 | nan | nan | nan | Cerrado | 1.6 |
| 1f446b3b-5c9c-3e0b-b28c-5ff2cc249041 | -5.35969 | -44.90254 | 2025-11-15 04:04:00 | NPP-375D | BARRA DO CORDA | MARANHÃO | Brasil | 2101608 | 21 | 33 | nan | nan | nan | Cerrado | 2.0 |
| 9a9d182a-eeff-3742-af1e-fa729991a5e3 | -5.33517 | -43.03549 | 2025-11-15 04:04:00 | NPP-375D | TIMON | MARANHÃO | Brasil | 2112209 | 21 | 33 | nan | nan | nan | Cerrado | 3.6 |
| 7592b681-7ae2-3e10-8233-c7cda0f6ecf4 | -6.88412 | -41.59374 | 2025-11-15 04:04:00 | NPP-375D | PICOS | PIAUÍ | Brasil | 2208007 | 22 | 33 | nan | nan | nan | Caatinga | 0.8 |
| 3e90a0b9-6f3b-3b90-90fd-2e103b8a4fb2 | -3.70861 | -41.63742 | 2025-11-15 04:04:00 | NPP-375D | PIRACURUCA | PIAUÍ | Brasil | 2208304 | 22 | 33 | nan | nan | nan | Caatinga | 1.9 |
| 49521795-4414-3542-acbf-1af2ce95e99b | -7.44223 | -42.76902 | 2025-11-15 04:04:00 | NPP-375D | FLORES DO PIAUÍ | PIAUÍ | Brasil | 2203800 | 22 | 33 | nan | nan | nan | Caatinga | 2.6 |
| 979ec94e-8ff6-3489-bc73-63cbc9497b34 | -6.28175 | -41.73205 | 2025-11-15 04:04:00 | NPP-375D | VALENÇA DO PIAUÍ | PIAUÍ | Brasil | 2211308 | 22 | 33 | nan | nan | nan | Caatinga | 2.5 |
| 8b7fa10d-fd14-33b1-84aa-adb001baa8b2 | -5.25 | -44.86226 | 2025-11-15 04:04:00 | NPP-375D | BARRA DO CORDA | MARANHÃO | Brasil | 2101608 | 21 | 33 | nan | nan | nan | Cerrado | 0.8 |
| 131cf418-7338-36fe-969f-2d6c06149faa | -4.64866 | -47.95084 | 2025-11-15 04:04:00 | NPP-375D | RONDON DO PARÁ | PARÁ | Brasil | 1506187 | 15 | 33 | nan | nan | nan | Amazônia | 1.5 |
| d08ac1b7-fa55-3916-9ae9-0d3090a0af65 | -4.98054 | -43.88947 | 2025-11-15 04:04:00 | NPP-375D | CODÓ | MARANHÃO | Brasil | 2103307 | 21 | 33 | nan | nan | nan | Cerrado | 2.8 |
| 7384899d-80be-3cd2-92bb-7679a9aa70c6 | -4.59483 | -44.31834 | 2025-11-15 04:04:00 | NPP-375D | CAPINZAL DO NORTE | MARANHÃO | Brasil | 2102754 | 21 | 33 | nan | nan | nan | Cerrado | 22.8 |
| 653ab640-e3fe-33da-a886-d30cfce47080 | -4.24944 | -48.20594 | 2025-11-15 04:04:00 | NPP-375D | RONDON DO PARÁ | PARÁ | Brasil | 1506187 | 15 | 33 | nan | nan | nan | Amazônia | 2.3 |
| 37012bc1-89fd-3726-8555-a960ede63919 | -4.11023 | -48.01525 | 2025-11-15 04:04:00 | NPP-375D | DOM ELISEU | PARÁ | Brasil | 1502939 | 15 | 33 | nan | nan | nan | Amazônia | 2.6 |
| 2c75f0a9-7717-36fa-a33a-9969d11334f0 | -3.70518 | -42.75129 | 2025-11-15 04:04:00 | NPP-375D | BREJO | MARANHÃO | Brasil | 2102101 | 21 | 33 | nan | nan | nan | Cerrado | 1.2 |
| ea287e85-0a56-3a0a-ad57-6fb2b7c6fea1 | -5.0929 | -41.47749 | 2025-11-15 04:04:00 | NPP-375D | CASTELO DO PIAUÍ | PIAUÍ | Brasil | 2202604 | 22 | 33 | nan | nan | nan | Caatinga | 2.0 |
| d6b78350-2c5c-34df-be54-e5bcfaaae88c | -6.14459 | -48.04624 | 2025-11-15 04:04:00 | NPP-375D | ANANÁS | TOCANTINS | Brasil | 1701002 | 17 | 33 | nan | nan | nan | Cerrado | 7.2 |


[Clique aqui para ver as próximas entradas](README22.md)
