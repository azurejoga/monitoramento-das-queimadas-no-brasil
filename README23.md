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

## Dados Diários - Página 23

| ID | Latitude | Longitude | Data/Hora GMT | Satélite | Município | Estado | País | Município ID | Estado ID | País ID | Dias sem Chuva | Precipitação | Risco de Fogo | Bioma | FRP |
|----|----------|-----------|---------------|----------|-----------|--------|------|--------------|-----------|---------|----------------|--------------|----------------|-------|-----|
| 80bf9f37-0bc0-37ed-8657-d4314a34e8b0 | -2.67753 | -57.56975 | 2026-09-14 04:32:00 | NPP-375D | URUCURITUBA | AMAZONAS | Brasil | 1304401 | 13 | 33 | nan | nan | nan | Amazônia | 4.3 |
| a3a3416c-a10f-37b9-87bf-1a99d1c5af79 | -7.07787 | -43.54615 | 2026-09-14 04:32:00 | NPP-375D | JERUMENHA | PIAUÍ | Brasil | 2205300 | 22 | 33 | nan | nan | nan | Cerrado | 2.8 |
| a64fa34a-3e18-3241-9251-247e7cdab471 | -9.39589 | -50.16578 | 2026-09-14 04:32:00 | NPP-375D | SANTANA DO ARAGUAIA | PARÁ | Brasil | 1506708 | 15 | 33 | nan | nan | nan | Amazônia | 74.6 |
| 6b38cde3-def6-33ba-92e5-e97d01b987eb | -2.90429 | -50.39573 | 2026-09-14 04:32:00 | NPP-375D | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 20.5 |
| a13aeed8-e159-39c2-8cd7-e52c83ed5b67 | -10.0533 | -45.49141 | 2026-09-14 04:32:00 | NPP-375D | SÃO GONÇALO DO GURGUÉIA | PIAUÍ | Brasil | 2209757 | 22 | 33 | nan | nan | nan | Cerrado | 3.2 |
| 3db3bb9d-07ea-313a-ace8-fdde72a85124 | -4.36134 | -50.85587 | 2026-09-14 04:32:00 | NPP-375D | NOVO REPARTIMENTO | PARÁ | Brasil | 1505064 | 15 | 33 | nan | nan | nan | Amazônia | 1.2 |
| b7cd955c-3327-3d13-84e0-c224c22cd6c6 | -6.58195 | -58.8493 | 2026-09-14 04:32:00 | NPP-375D | MAUÉS | AMAZONAS | Brasil | 1302900 | 13 | 33 | nan | nan | nan | Amazônia | 4.8 |
| 14d3c108-a08e-371e-8fe1-f9fbac4f0d1e | -3.35473 | -51.29654 | 2026-09-14 04:32:00 | NPP-375D | ANAPU | PARÁ | Brasil | 1500859 | 15 | 33 | nan | nan | nan | Amazônia | 2.0 |
| ae5540a8-a457-30c0-873c-3aff3c848417 | -9.36596 | -50.14997 | 2026-09-14 04:32:00 | NPP-375D | SANTANA DO ARAGUAIA | PARÁ | Brasil | 1506708 | 15 | 33 | nan | nan | nan | Amazônia | 1.6 |
| 0f628da2-2547-3160-891f-c79a209ef372 | -8.11813 | -54.79788 | 2026-09-14 04:32:00 | NPP-375D | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 1.9 |
| 1a483790-5ef2-348f-8939-3de2babb6d15 | -6.32373 | -44.17554 | 2026-09-14 04:32:00 | NPP-375D | SUCUPIRA DO NORTE | MARANHÃO | Brasil | 2111904 | 21 | 33 | nan | nan | nan | Cerrado | 1.5 |
| 92337e4a-1b0b-3502-8c0f-004b8d53fe56 | -6.23203 | -51.68041 | 2026-09-14 04:32:00 | NPP-375D | SÃO FÉLIX DO XINGU | PARÁ | Brasil | 1507300 | 15 | 33 | nan | nan | nan | Amazônia | 1.9 |
| 349b475c-c7ff-37fd-9339-41819269c2f5 | -3.2274 | -43.03146 | 2026-09-14 04:32:00 | NPP-375D | SANTA QUITÉRIA DO MARANHÃO | MARANHÃO | Brasil | 2110104 | 21 | 33 | nan | nan | nan | Cerrado | 0.8 |
| 78ad2c26-7307-3a69-beba-746c4738815e | -2.93336 | -50.42639 | 2026-09-14 04:32:00 | NPP-375D | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 4.2 |
| d79122ed-d236-3db5-b062-feca878b165b | -9.13768 | -51.57352 | 2026-09-14 04:32:00 | NPP-375D | CUMARU DO NORTE | PARÁ | Brasil | 1502764 | 15 | 33 | nan | nan | nan | Amazônia | 1.6 |
| 20cf08e1-2455-3d0b-90e0-10e39fbac1cc | -4.34555 | -54.7851 | 2026-09-14 04:32:00 | NPP-375D | PLACAS | PARÁ | Brasil | 1505650 | 15 | 33 | nan | nan | nan | Amazônia | 3.7 |
| 60e1c55f-9bfb-34af-b424-842cd9246902 | -7.09026 | -41.79732 | 2026-09-14 04:32:00 | NPP-375D | SANTA CRUZ DO PIAUÍ | PIAUÍ | Brasil | 2209104 | 22 | 33 | nan | nan | nan | Caatinga | 1.0 |
| 814a3582-ad0b-37e7-9110-40d6a18119aa | -8.04611 | -45.54477 | 2026-09-14 04:32:00 | NPP-375D | RIBEIRO GONÇALVES | PIAUÍ | Brasil | 2208908 | 22 | 33 | nan | nan | nan | Cerrado | 6.1 |
| f1e0e027-e8fc-33c9-aadf-12aca54f7b58 | -9.36685 | -50.14486 | 2026-09-14 04:32:00 | NPP-375D | SANTANA DO ARAGUAIA | PARÁ | Brasil | 1506708 | 15 | 33 | nan | nan | nan | Amazônia | 1.6 |
| 89a3b4db-2b4e-3e41-82b2-33277bb64466 | -2.64992 | -48.57563 | 2026-09-14 04:32:00 | NPP-375D | TAILÂNDIA | PARÁ | Brasil | 1507953 | 15 | 33 | nan | nan | nan | Amazônia | 1.7 |
| c9a71fc9-159d-3117-8b16-f5428e435e5f | -10.316 | -45.28527 | 2026-09-14 04:32:00 | NPP-375D | CORRENTE | PIAUÍ | Brasil | 2202901 | 22 | 33 | nan | nan | nan | Cerrado | 1.2 |
| 2b62ca05-d970-3900-9cb5-9f4f374d124b | -9.53528 | -45.4333 | 2026-09-14 04:32:00 | NPP-375D | GILBUÉS | PIAUÍ | Brasil | 2204402 | 22 | 33 | nan | nan | nan | Cerrado | 1.9 |
| 7cd563c4-9e7c-3828-ac8d-7776549a1894 | -7.1115 | -42.1 | 2026-09-14 04:32:00 | NPP-375D | OEIRAS | PIAUÍ | Brasil | 2207009 | 22 | 33 | nan | nan | nan | Caatinga | 0.8 |
| d1098137-5dcb-3c4e-85cf-5b38533a3deb | -5.81694 | -53.79751 | 2026-09-14 04:32:00 | NPP-375D | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 1.4 |
| 617ab856-da42-374f-9adc-deb60db868c0 | -9.16423 | -49.9948 | 2026-09-14 04:32:00 | NPP-375D | SANTANA DO ARAGUAIA | PARÁ | Brasil | 1506708 | 15 | 33 | nan | nan | nan | Amazônia | 2.0 |
| 605eab05-23a5-31f6-9eb2-0433f51cacb8 | -9.50921 | -45.49011 | 2026-09-14 04:32:00 | NPP-375D | GILBUÉS | PIAUÍ | Brasil | 2204402 | 22 | 33 | nan | nan | nan | Cerrado | 1.0 |
| f39fd0d0-bec2-3139-b8d1-133a6d94d6b3 | -2.90358 | -50.40011 | 2026-09-14 04:32:00 | NPP-375D | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 6.9 |
| 5bac764c-ac06-3cda-8c18-8e54a228ff8c | -3.78894 | -48.92989 | 2026-09-14 04:32:00 | NPP-375D | GOIANÉSIA DO PARÁ | PARÁ | Brasil | 1503093 | 15 | 33 | nan | nan | nan | Amazônia | 4.0 |
| 1074cc80-5d42-3198-89a9-0abbbb73baea | -2.91398 | -50.43231 | 2026-09-14 04:32:00 | NPP-375D | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 274.4 |
| 10285ddd-2aff-3c53-8692-294137332868 | -5.80917 | -53.81005 | 2026-09-14 04:32:00 | NPP-375D | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 2.0 |
| 682aa310-d8cd-3fba-990f-433056c76944 | -2.92848 | -50.44505 | 2026-09-14 04:32:00 | NPP-375D | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 7.4 |
| 69032598-3fb1-3b48-8f5d-483c2a78be3e | -3.79104 | -44.10619 | 2026-09-14 04:32:00 | NPP-375D | PIRAPEMAS | MARANHÃO | Brasil | 2108801 | 21 | 33 | nan | nan | nan | Cerrado | 1.1 |
| abb78e27-234c-3781-98b3-cba96a14066a | -6.33513 | -43.36578 | 2026-09-14 04:32:00 | NPP-375D | SUCUPIRA DO RIACHÃO | MARANHÃO | Brasil | 2111953 | 21 | 33 | nan | nan | nan | Cerrado | 17.9 |
| e3eb80b9-a399-31e8-88a3-3a7b51bf9b9f | -5.84239 | -52.09909 | 2026-09-14 04:32:00 | NPP-375D | SÃO FÉLIX DO XINGU | PARÁ | Brasil | 1507300 | 15 | 33 | nan | nan | nan | Amazônia | 4.2 |
| 4cb2d9fc-6e3c-30f8-a535-c87da87b4deb | -10.20395 | -45.26762 | 2026-09-14 04:32:00 | NPP-375D | CORRENTE | PIAUÍ | Brasil | 2202901 | 22 | 33 | nan | nan | nan | Cerrado | 1.3 |
| 68a2a048-32a5-314a-9f72-03b74caa16f7 | -5.85342 | -51.94861 | 2026-09-14 04:32:00 | NPP-375D | SÃO FÉLIX DO XINGU | PARÁ | Brasil | 1507300 | 15 | 33 | nan | nan | nan | Amazônia | 1.5 |
| 22e64aca-c69f-35a8-b6f1-21f0c2867eda | -2.61364 | -54.75704 | 2026-09-14 04:32:00 | NPP-375D | SANTARÉM | PARÁ | Brasil | 1506807 | 15 | 33 | nan | nan | nan | Amazônia | 3.1 |
| 00b27cb2-c7f2-3559-b040-051a4b0e7c46 | -8.54084 | -54.7154 | 2026-09-14 04:32:00 | NPP-375D | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 1.7 |
| b017f71c-cda8-3f9d-904e-366fc113585c | -5.52557 | -45.66897 | 2026-09-14 04:32:00 | NPP-375D | JENIPAPO DOS VIEIRAS | MARANHÃO | Brasil | 2105476 | 21 | 33 | nan | nan | nan | Cerrado | 1.4 |
| a864aa20-a7c2-3e54-bb7e-d82e82c7209e | -3.38858 | -50.755 | 2026-09-14 04:32:00 | NPP-375D | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 1.4 |
| 523ea526-1a0c-3e57-b9a3-0f593e9dacff | -2.92825 | -50.41778 | 2026-09-14 04:32:00 | NPP-375D | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 6.6 |
| 36159fee-db70-31b9-ad06-b7c92f003ed4 | -2.93625 | -50.39642 | 2026-09-14 04:32:00 | NPP-375D | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 3.5 |
| f84a504e-772b-304f-897f-49f115cc3249 | -2.95562 | -50.40294 | 2026-09-14 04:32:00 | NPP-375D | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 3.1 |
| d9fc4b90-0244-3662-b8ff-b96b0e2fe5ff | -6.91504 | -55.63596 | 2026-09-14 04:32:00 | NPP-375D | NOVO PROGRESSO | PARÁ | Brasil | 1505031 | 15 | 33 | nan | nan | nan | Amazônia | 1.0 |
| a368a126-6351-3d38-a012-2d114d337a06 | -6.80248 | -43.1844 | 2026-09-14 04:32:00 | NPP-375D | FLORIANO | PIAUÍ | Brasil | 2203909 | 22 | 33 | nan | nan | nan | Caatinga | 1.1 |
| 3345f139-8a2e-3ab1-ad0f-22561c2e3da5 | -9.37341 | -50.17766 | 2026-09-14 04:32:00 | NPP-375D | SANTANA DO ARAGUAIA | PARÁ | Brasil | 1506708 | 15 | 33 | nan | nan | nan | Amazônia | 5.1 |
| 8357054a-44ef-331e-ac63-df410f72fea3 | -2.91995 | -50.4242 | 2026-09-14 04:32:00 | NPP-375D | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 135.7 |
| 567d7840-69f3-3c40-9e72-490923e78e52 | -6.65885 | -43.65765 | 2026-09-14 04:32:00 | NPP-375D | SÃO JOÃO DOS PATOS | MARANHÃO | Brasil | 2111102 | 21 | 33 | nan | nan | nan | Cerrado | 0.5 |
| be7dcf74-a508-3063-bea1-b68abbad2586 | -2.92962 | -50.4213 | 2026-09-14 04:32:00 | NPP-375D | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 30.3 |
| eefc3068-b99e-38ec-bab2-a7555b618152 | -1.46125 | -52.96297 | 2026-09-14 04:32:00 | NPP-375D | ALMEIRIM | PARÁ | Brasil | 1500503 | 15 | 33 | nan | nan | nan | Amazônia | 0.8 |
| f108c322-d77f-3a77-b9ff-de334701678d | -6.29514 | -41.69044 | 2026-09-14 04:32:00 | NPP-375D | VALENÇA DO PIAUÍ | PIAUÍ | Brasil | 2211308 | 22 | 33 | nan | nan | nan | Caatinga | 1.4 |
| 65184f05-4723-368a-8fac-bf99dc057e5c | -2.91057 | -50.44212 | 2026-09-14 04:32:00 | NPP-375D | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 83.4 |
| 0bb80f74-52ab-3cda-92d7-d8d4828269b7 | -2.91627 | -50.4067 | 2026-09-14 04:32:00 | NPP-375D | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 28.0 |
| 5acbe87a-2db5-3d94-a62e-2658f63d6c9a | -2.90734 | -50.40523 | 2026-09-14 04:32:00 | NPP-375D | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 6.9 |
| dfe4f756-229b-342a-b4f2-4131daf12678 | -2.90466 | -50.45024 | 2026-09-14 04:32:00 | NPP-375D | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 18.0 |
| 6bbc85f0-4b99-3e88-873f-e6e180dbd42a | -9.37779 | -50.1996 | 2026-09-14 04:32:00 | NPP-375D | SANTANA DO ARAGUAIA | PARÁ | Brasil | 1506708 | 15 | 33 | nan | nan | nan | Amazônia | 1.4 |
| 445a2d2b-a4f6-3bac-8a30-51f19333da95 | -4.38717 | -55.20398 | 2026-09-14 04:32:00 | NPP-375D | RURÓPOLIS | PARÁ | Brasil | 1506195 | 15 | 33 | nan | nan | nan | Amazônia | 2.2 |
| dac540c7-a80d-3702-bbb5-4a5903d6b39b | -6.58332 | -58.84196 | 2026-09-14 04:32:00 | NPP-375D | MAUÉS | AMAZONAS | Brasil | 1302900 | 13 | 33 | nan | nan | nan | Amazônia | 3.3 |
| 9c17d253-bb55-3be9-a869-9f3e91bb0261 | -2.90287 | -50.40451 | 2026-09-14 04:32:00 | NPP-375D | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 6.9 |
| 638b7c69-4a68-3a5b-8444-b72f545e4e48 | -3.38783 | -50.75962 | 2026-09-14 04:32:00 | NPP-375D | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 1.4 |
| 77934803-e8fe-3991-8eb3-8743ab608029 | -8.54188 | -54.70465 | 2026-09-14 04:32:00 | NPP-375D | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 1.6 |
| 8192071c-d843-3d38-95ca-bb8de92e773f | -8.53518 | -54.71067 | 2026-09-14 04:32:00 | NPP-375D | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 1.5 |
| b6eb7631-da39-3cef-ae54-b87b61437858 | -2.92885 | -50.39856 | 2026-09-14 04:32:00 | NPP-375D | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 3.6 |
| 493b98c0-106f-3874-aae7-279adf4ba489 | -3.60696 | -53.85046 | 2026-09-14 04:32:00 | NPP-375D | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | 1.2 |
| 18479032-8bb5-327d-a21b-dd6eb75354c5 | -9.40602 | -50.17812 | 2026-09-14 04:32:00 | NPP-375D | SANTANA DO ARAGUAIA | PARÁ | Brasil | 1506708 | 15 | 33 | nan | nan | nan | Amazônia | 6.7 |
| 00f602eb-d7fb-3e57-bb10-dd150280e412 | -9.40381 | -50.16718 | 2026-09-14 04:32:00 | NPP-375D | SANTANA DO ARAGUAIA | PARÁ | Brasil | 1506708 | 15 | 33 | nan | nan | nan | Amazônia | 42.7 |
| cca6891b-cb17-3c62-af18-1b03d54588f5 | -7.07282 | -43.55643 | 2026-09-14 04:32:00 | NPP-375D | JERUMENHA | PIAUÍ | Brasil | 2205300 | 22 | 33 | nan | nan | nan | Cerrado | 1.2 |
| f063a2ca-5cc8-3753-acc9-8d17742706b0 | -6.85343 | -47.42356 | 2026-09-14 04:32:00 | NPP-375D | ESTREITO | MARANHÃO | Brasil | 2104057 | 21 | 33 | nan | nan | nan | Cerrado | 1.4 |
| 05fd2784-2130-3344-8b9a-4423f73fe696 | -6.34525 | -44.10378 | 2026-09-14 04:32:00 | NPP-375D | COLINAS | MARANHÃO | Brasil | 2103505 | 21 | 33 | nan | nan | nan | Cerrado | 0.9 |
| 13aca342-416c-3945-a610-c106a1e50d46 | -6.59498 | -58.86494 | 2026-09-14 04:32:00 | NPP-375D | MAUÉS | AMAZONAS | Brasil | 1302900 | 13 | 33 | nan | nan | nan | Amazônia | 2.7 |
| 5466d20b-29f5-3413-80b6-702a0ea70ed0 | -9.36645 | -50.12374 | 2026-09-14 04:32:00 | NPP-375D | SANTANA DO ARAGUAIA | PARÁ | Brasil | 1506708 | 15 | 33 | nan | nan | nan | Amazônia | 1.7 |
| 59221df8-a254-3060-8558-fa62f9c662bf | -9.45008 | -47.85349 | 2026-09-14 04:32:00 | NPP-375D | RIO SONO | TOCANTINS | Brasil | 1718758 | 17 | 33 | nan | nan | nan | Cerrado | 2.7 |
| b07ea9fc-c476-3595-a2b8-35a370fb8c1d | -2.96226 | -50.39055 | 2026-09-14 04:32:00 | NPP-375D | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 2.5 |
| e3a844da-1ada-3de9-b656-cb02c0f65da5 | -7.46691 | -45.96423 | 2026-09-14 04:32:00 | NPP-375D | BALSAS | MARANHÃO | Brasil | 2101400 | 21 | 33 | nan | nan | nan | Cerrado | 2.6 |
| 3bcffd19-9a02-31c1-8a1d-961041dc53c8 | -2.8882 | -50.4383 | 2026-09-14 04:32:00 | NPP-375D | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 27.7 |
| e46310fb-cf84-37da-adb0-c7ad2ee09410 | -2.93202 | -50.42294 | 2026-09-14 04:32:00 | NPP-375D | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 19.0 |
| 58007583-167e-3d14-b2e2-418989f6e728 | -8.49146 | -44.56689 | 2026-09-14 04:32:00 | NPP-375D | PALMEIRA DO PIAUÍ | PIAUÍ | Brasil | 2207405 | 22 | 33 | nan | nan | nan | Cerrado | 1.1 |
| a2169fcb-60b8-3f36-8012-f3a679be6fa8 | -1.46068 | -52.96643 | 2026-09-14 04:32:00 | NPP-375D | ALMEIRIM | PARÁ | Brasil | 1500503 | 15 | 33 | nan | nan | nan | Amazônia | 0.8 |
| 18a68575-9801-3419-a362-884d72cfb174 | -2.90162 | -50.4406 | 2026-09-14 04:32:00 | NPP-375D | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 74.5 |
| 20998026-0b4b-3c00-b202-d4a5b99b5bd2 | -9.37518 | -50.16742 | 2026-09-14 04:32:00 | NPP-375D | SANTANA DO ARAGUAIA | PARÁ | Brasil | 1506708 | 15 | 33 | nan | nan | nan | Amazônia | 5.9 |
| b2b53d1b-ecd4-37ba-acac-ac87195035c5 | -2.91475 | -50.45504 | 2026-09-14 04:32:00 | NPP-375D | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 6.3 |
| 9019b110-4606-3375-b0d4-92c458d49c33 | -5.77227 | -47.16999 | 2026-09-14 04:32:00 | NPP-375D | MONTES ALTOS | MARANHÃO | Brasil | 2107001 | 21 | 33 | nan | nan | nan | Cerrado | 1.0 |
| 91bf3354-c437-34a9-833b-7302dcf834df | -4.34394 | -48.96233 | 2026-09-14 04:32:00 | NPP-375D | GOIANÉSIA DO PARÁ | PARÁ | Brasil | 1503093 | 15 | 33 | nan | nan | nan | Amazônia | 1.9 |
| b97ccbf9-854e-39b6-9edb-2f37943f911d | -2.91771 | -50.41025 | 2026-09-14 04:32:00 | NPP-375D | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 192.3 |
| 6a6eaf42-0ab7-30eb-8def-918e473a8ce7 | -7.02116 | -44.64578 | 2026-09-14 04:32:00 | NPP-375D | BENEDITO LEITE | MARANHÃO | Brasil | 2101806 | 21 | 33 | nan | nan | nan | Cerrado | 1.9 |
| 1aa34797-ba2f-3f31-81b0-a51ae40e1125 | -10.29882 | -45.30768 | 2026-09-14 04:32:00 | NPP-375D | CORRENTE | PIAUÍ | Brasil | 2202901 | 22 | 33 | nan | nan | nan | Cerrado | 0.9 |
| 22a9d322-a8d1-3c9d-b530-3d06209101b9 | -7.96829 | -43.98172 | 2026-09-14 04:32:00 | NPP-375D | SEBASTIÃO LEAL | PIAUÍ | Brasil | 2210631 | 22 | 33 | nan | nan | nan | Cerrado | 1.8 |
| 758b658c-7678-3e7a-aa6f-a1e65e38f538 | -7.96717 | -43.98885 | 2026-09-14 04:32:00 | NPP-375D | SEBASTIÃO LEAL | PIAUÍ | Brasil | 2210631 | 22 | 33 | nan | nan | nan | Cerrado | 2.0 |
| 4f42e287-3a0f-32ca-bc07-ec15b55212ed | -6.59496 | -58.8596 | 2026-09-14 04:32:00 | NPP-375D | MAUÉS | AMAZONAS | Brasil | 1302900 | 13 | 33 | nan | nan | nan | Amazônia | 2.0 |
| 78bee140-32a5-3aa6-a3ba-7769fc8f7ef6 | -5.92507 | -45.03056 | 2026-09-14 04:32:00 | NPP-375D | FERNANDO FALCÃO | MARANHÃO | Brasil | 2104081 | 21 | 33 | nan | nan | nan | Cerrado | 0.5 |
| 0feb5476-42e4-3673-bded-b25adc2ab4f7 | -4.3824 | -55.20543 | 2026-09-14 04:32:00 | NPP-375D | RURÓPOLIS | PARÁ | Brasil | 1506195 | 15 | 33 | nan | nan | nan | Amazônia | 1.7 |
| 7c5f08e8-4e0d-392f-b4d7-55a9c11fbb7b | -2.95344 | -50.41608 | 2026-09-14 04:32:00 | NPP-375D | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 1.9 |
| fa57becc-55ac-38dd-b282-7189c5c9deec | -9.4464 | -50.13253 | 2026-09-14 04:32:00 | NPP-375D | SANTANA DO ARAGUAIA | PARÁ | Brasil | 1506708 | 15 | 33 | nan | nan | nan | Amazônia | 6.9 |
| f05c7f62-bca2-3a6e-a3b5-4c63cca26f97 | -2.89554 | -50.42139 | 2026-09-14 04:32:00 | NPP-375D | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 42.1 |
| 1e829981-91d2-34c3-a411-3c1e35757da0 | -3.79714 | -44.11068 | 2026-09-14 04:32:00 | NPP-375D | PIRAPEMAS | MARANHÃO | Brasil | 2108801 | 21 | 33 | nan | nan | nan | Cerrado | 1.8 |
| 019c76e2-e878-3cc2-9b35-b35a99026586 | -5.63598 | -40.85078 | 2026-09-14 04:32:00 | NPP-375D | NOVO ORIENTE | CEARÁ | Brasil | 2309409 | 23 | 33 | nan | nan | nan | Caatinga | 2.8 |
| 890e551c-0255-3c6c-b782-901b4da26350 | -2.92215 | -50.39863 | 2026-09-14 04:32:00 | NPP-375D | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 4.2 |
| 05c7eda6-c252-30e6-98bd-f8d294bef739 | -6.31272 | -55.28096 | 2026-09-14 04:32:00 | NPP-375D | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 0.9 |
| 4c542238-abf3-3dd2-bb04-9317836023ac | -7.10377 | -42.10292 | 2026-09-14 04:32:00 | NPP-375D | OEIRAS | PIAUÍ | Brasil | 2207009 | 22 | 33 | nan | nan | nan | Caatinga | 1.7 |
| 8b1c18f7-b0f6-35aa-9380-095800e071f6 | -6.28797 | -55.28396 | 2026-09-14 04:32:00 | NPP-375D | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 1.2 |


[Clique aqui para ver as próximas entradas](README24.md)
