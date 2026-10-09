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

## Dados Diários - Página 91

| ID | Latitude | Longitude | Data/Hora GMT | Satélite | Município | Estado | País | Município ID | Estado ID | País ID | Dias sem Chuva | Precipitação | Risco de Fogo | Bioma | FRP |
|----|----------|-----------|---------------|----------|-----------|--------|------|--------------|-----------|---------|----------------|--------------|----------------|-------|-----|
| 4efa29f8-143e-3984-8274-c5cfe1a3b12c | -2.47297 | -56.07153 | 2026-10-09 04:25:00 | NOAA-21 | JURUTI | PARÁ | Brasil | 1503903 | 15 | 33 | nan | nan | nan | Amazônia | 4.8 |
| 6e00b0d3-0c73-396e-aa78-b35ce4ddee73 | -2.83527 | -54.13785 | 2026-10-09 04:25:00 | NOAA-21 | SANTARÉM | PARÁ | Brasil | 1506807 | 15 | 33 | nan | nan | nan | Amazônia | 1.4 |
| e42aaf4c-aa77-3d24-a2af-c46bf244f108 | -6.00048 | -40.96761 | 2026-10-09 04:25:00 | NOAA-21 | ASSUNÇÃO DO PIAUÍ | PIAUÍ | Brasil | 2201051 | 22 | 33 | nan | nan | nan | Caatinga | 6.0 |
| b451654c-60b7-3c1b-a3e0-a1afa55290ee | -4.36209 | -44.35332 | 2026-10-09 04:25:00 | NOAA-21 | PERITORÓ | MARANHÃO | Brasil | 2108454 | 21 | 33 | nan | nan | nan | Cerrado | 1.4 |
| d5c4d5f0-b148-330d-a211-19dcd2dd4db4 | -3.48031 | -50.08635 | 2026-10-09 04:25:00 | NOAA-21 | PACAJÁ | PARÁ | Brasil | 1505486 | 15 | 33 | nan | nan | nan | Amazônia | 1.7 |
| 9d7cd152-e5e7-3cbe-84c1-e73df79c2437 | -6.16828 | -39.44545 | 2026-10-09 04:25:00 | NOAA-21 | ACOPIARA | CEARÁ | Brasil | 2300309 | 23 | 33 | nan | nan | nan | Caatinga | 8.1 |
| 81cb9496-996a-3f4e-bcf7-9014387d8347 | -1.39439 | -48.94671 | 2026-10-09 04:25:00 | NOAA-21 | PONTA DE PEDRAS | PARÁ | Brasil | 1505700 | 15 | 33 | nan | nan | nan | Amazônia | 1.0 |
| 850f55bb-76b6-39aa-a7df-01f6ff2190cc | -3.04493 | -44.69493 | 2026-10-09 04:25:00 | NOAA-21 | SÃO JOÃO BATISTA | MARANHÃO | Brasil | 2111003 | 21 | 33 | nan | nan | nan | Amazônia | 0.3 |
| f5a11230-40bd-3a15-8ebf-d4180d53f513 | -3.83916 | -44.14058 | 2026-10-09 04:25:00 | NOAA-21 | COROATÁ | MARANHÃO | Brasil | 2103604 | 21 | 33 | nan | nan | nan | Cerrado | 1.3 |
| a09fe641-51b9-337e-8315-217813026392 | -6.87618 | -45.89712 | 2026-10-09 04:25:00 | NOAA-21 | SÃO RAIMUNDO DAS MANGABEIRAS | MARANHÃO | Brasil | 2111607 | 21 | 33 | nan | nan | nan | Cerrado | 3.7 |
| 6b5cbd85-18f9-3a52-a3de-646eaba45724 | -5.08792 | -46.2171 | 2026-10-09 04:25:00 | NOAA-21 | AMARANTE DO MARANHÃO | MARANHÃO | Brasil | 2100600 | 21 | 33 | nan | nan | nan | Amazônia | 1.7 |
| 76883f5b-50c4-348e-87f6-417fc87174f0 | -3.5298 | -44.33041 | 2026-10-09 04:25:00 | NOAA-21 | ITAPECURU MIRIM | MARANHÃO | Brasil | 2105401 | 21 | 33 | nan | nan | nan | Cerrado | 1.1 |
| 09f4a7d9-1169-38d9-901c-e7359515897c | -4.75872 | -44.00549 | 2026-10-09 04:25:00 | NOAA-21 | CODÓ | MARANHÃO | Brasil | 2103307 | 21 | 33 | nan | nan | nan | Cerrado | 1.5 |
| 4eab7602-03bc-36a7-8820-dd259fc89bce | -7.18889 | -42.00186 | 2026-10-09 04:25:00 | NOAA-21 | OEIRAS | PIAUÍ | Brasil | 2207009 | 22 | 33 | nan | nan | nan | Caatinga | 2.2 |
| aaaae430-c300-3706-82e6-1aa0cf8190ce | -3.03475 | -54.14294 | 2026-10-09 04:25:00 | NOAA-21 | SANTARÉM | PARÁ | Brasil | 1506807 | 15 | 33 | nan | nan | nan | Amazônia | 4.8 |
| 37294063-a4d7-35e5-89df-24926b673c85 | -2.5532 | -58.03939 | 2026-10-09 04:25:00 | NOAA-21 | SÃO SEBASTIÃO DO UATUMÃ | AMAZONAS | Brasil | 1303957 | 13 | 33 | nan | nan | nan | Amazônia | 2.2 |
| b06133ad-9ea0-30cd-bb70-e63c394e62d4 | -5.515 | -42.83425 | 2026-10-09 04:25:00 | NOAA-21 | TERESINA | PIAUÍ | Brasil | 2211001 | 22 | 33 | nan | nan | nan | Caatinga | 5.6 |
| d1c6acd3-17df-3f28-ae38-1240bfe8b2ca | -7.05826 | -40.95277 | 2026-10-09 04:25:00 | NOAA-21 | ALAGOINHA DO PIAUÍ | PIAUÍ | Brasil | 2200251 | 22 | 33 | nan | nan | nan | Caatinga | 3.7 |
| ff3fd67c-184a-31a7-8981-ec691589b57f | -3.32313 | -50.17858 | 2026-10-09 04:25:00 | NOAA-21 | PACAJÁ | PARÁ | Brasil | 1505486 | 15 | 33 | nan | nan | nan | Amazônia | 1.9 |
| de64fe3a-2551-31ae-828a-ea5217240660 | -5.30375 | -45.72561 | 2026-10-09 04:25:00 | NOAA-21 | JENIPAPO DOS VIEIRAS | MARANHÃO | Brasil | 2105476 | 21 | 33 | nan | nan | nan | Cerrado | 1.0 |
| e9488e01-5959-37c8-a1ac-c35e440480e4 | -5.23663 | -45.41351 | 2026-10-09 04:25:00 | NOAA-21 | JENIPAPO DOS VIEIRAS | MARANHÃO | Brasil | 2105476 | 21 | 33 | nan | nan | nan | Cerrado | 2.5 |
| 00e1f401-d3fc-32f8-b121-89bbdcab1e0d | 0.93975 | -50.19585 | 2026-10-09 04:25:00 | NOAA-21 | MACAPÁ | AMAPÁ | Brasil | 1600303 | 16 | 33 | nan | nan | nan | Amazônia | 4.0 |
| a5e53c95-b2da-3b91-b208-27efaf29cf9a | -6.9586 | -45.27155 | 2026-10-09 04:25:00 | NOAA-21 | SAMBAÍBA | MARANHÃO | Brasil | 2109700 | 21 | 33 | nan | nan | nan | Cerrado | 4.0 |
| 1b101df2-e9d0-3d0d-bdb7-4da424fa6245 | -4.35871 | -44.35279 | 2026-10-09 04:25:00 | NOAA-21 | PERITORÓ | MARANHÃO | Brasil | 2108454 | 21 | 33 | nan | nan | nan | Cerrado | 1.4 |
| 96a7a002-ccea-39c7-918a-0dddad615ab3 | -6.88388 | -45.89117 | 2026-10-09 04:25:00 | NOAA-21 | SÃO RAIMUNDO DAS MANGABEIRAS | MARANHÃO | Brasil | 2111607 | 21 | 33 | nan | nan | nan | Cerrado | 3.3 |
| 8885f9f7-0c26-3a9c-982b-458ce09442c4 | -3.56408 | -54.68706 | 2026-10-09 04:25:00 | NOAA-21 | PLACAS | PARÁ | Brasil | 1505650 | 15 | 33 | nan | nan | nan | Amazônia | 6.2 |
| dfc220e1-a87d-3b47-a58a-8eb2b4dd8b23 | -4.06225 | -49.11084 | 2026-10-09 04:25:00 | NOAA-21 | BREU BRANCO | PARÁ | Brasil | 1501782 | 15 | 33 | nan | nan | nan | Amazônia | 2.1 |
| 475aa178-56df-3043-9e0b-f068146c5728 | -3.08689 | -53.95313 | 2026-10-09 04:25:00 | NOAA-21 | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | 1.0 |
| 2d836c27-5832-3d4f-bfb3-476c102c76ed | -6.4645 | -46.02818 | 2026-10-09 04:25:00 | NOAA-21 | FORMOSA DA SERRA NEGRA | MARANHÃO | Brasil | 2104099 | 21 | 33 | nan | nan | nan | Cerrado | 3.0 |
| ea2224ee-949c-365c-89fc-e1d7698f85da | -5.70021 | -49.08336 | 2026-10-09 04:25:00 | NOAA-21 | MARABÁ | PARÁ | Brasil | 1504208 | 15 | 33 | nan | nan | nan | Amazônia | 5.2 |
| 6845ad0c-4e51-32e4-a847-8046c2489e9a | -2.51234 | -56.15837 | 2026-10-09 04:25:00 | NOAA-21 | JURUTI | PARÁ | Brasil | 1503903 | 15 | 33 | nan | nan | nan | Amazônia | 2.8 |
| ebe12c5b-cbde-3ca4-871f-ee635e4edb5f | -6.70113 | -47.01993 | 2026-10-09 04:25:00 | NOAA-21 | ESTREITO | MARANHÃO | Brasil | 2104057 | 21 | 33 | nan | nan | nan | Cerrado | 1.5 |
| 74d4c483-af5a-3a51-9339-9f90c7391a09 | -5.87897 | -49.87326 | 2026-10-09 04:25:00 | NOAA-21 | PARAUAPEBAS | PARÁ | Brasil | 1505536 | 15 | 33 | nan | nan | nan | Amazônia | 1.7 |
| 87a9e174-dce3-3f6b-afe8-a898f580e3fb | -5.45077 | -42.88977 | 2026-10-09 04:25:00 | NOAA-21 | NAZÁRIA | PIAUÍ | Brasil | 2206720 | 22 | 33 | nan | nan | nan | Caatinga | 3.2 |
| 4e67a650-d7ae-3560-b698-2f84c9ff17b0 | -2.81032 | -58.29303 | 2026-10-09 04:25:00 | NOAA-21 | SILVES | AMAZONAS | Brasil | 1304005 | 13 | 33 | nan | nan | nan | Amazônia | 18.0 |
| 89994cee-dd16-3a08-b752-6843cd938154 | -5.32156 | -45.34809 | 2026-10-09 04:25:00 | NOAA-21 | BARRA DO CORDA | MARANHÃO | Brasil | 2101608 | 21 | 33 | nan | nan | nan | Cerrado | 0.6 |
| 0a34f95b-59c5-3f9e-9344-287758cd8869 | -2.75027 | -49.5274 | 2026-10-09 04:25:00 | NOAA-21 | BAIÃO | PARÁ | Brasil | 1501204 | 15 | 33 | nan | nan | nan | Amazônia | 1.8 |
| 501216ea-415b-395d-b623-0229fbbc6096 | -5.09037 | -46.13655 | 2026-10-09 04:25:00 | NOAA-21 | ARAME | MARANHÃO | Brasil | 2100956 | 21 | 33 | nan | nan | nan | Amazônia | 1.0 |
| d86fc32c-3f7e-3e8e-af99-6dfd0a0eba0f | -3.02549 | -54.10495 | 2026-10-09 04:25:00 | NOAA-21 | SANTARÉM | PARÁ | Brasil | 1506807 | 15 | 33 | nan | nan | nan | Amazônia | 1.3 |
| e3961ceb-ff69-35c2-8d0c-23ff74aa3136 | -3.93852 | -55.71865 | 2026-10-09 04:25:00 | NOAA-21 | AVEIRO | PARÁ | Brasil | 1501006 | 15 | 33 | nan | nan | nan | Amazônia | 1.5 |
| 4e047174-8006-3930-9b86-f154255fa495 | -6.04134 | -44.03169 | 2026-10-09 04:25:00 | NOAA-21 | COLINAS | MARANHÃO | Brasil | 2103505 | 21 | 33 | nan | nan | nan | Cerrado | 6.0 |
| 5885a56b-c499-377d-85ba-b9f3226f9a8b | -6.45513 | -46.02318 | 2026-10-09 04:25:00 | NOAA-21 | FORMOSA DA SERRA NEGRA | MARANHÃO | Brasil | 2104099 | 21 | 33 | nan | nan | nan | Cerrado | 1.0 |
| c54162de-a2ff-379f-b877-2642598fddf1 | -3.17672 | -50.59179 | 2026-10-09 04:25:00 | NOAA-21 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 2.5 |
| 50299cc6-55d4-3884-a276-1ea57763443f | -1.1151 | -54.16792 | 2026-10-09 04:25:00 | NOAA-21 | MONTE ALEGRE | PARÁ | Brasil | 1504802 | 15 | 33 | nan | nan | nan | Amazônia | 4.5 |
| f64e0000-c98d-39a9-a242-6170be9f9acc | -3.31164 | -53.87046 | 2026-10-09 04:25:00 | NOAA-21 | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | 2.7 |
| 30dcfb62-0550-379f-b4ea-e4f7baa37a2d | -5.95579 | -40.92643 | 2026-10-09 04:25:00 | NOAA-21 | ASSUNÇÃO DO PIAUÍ | PIAUÍ | Brasil | 2201051 | 22 | 33 | nan | nan | nan | Caatinga | 1.3 |
| acd1e112-9ed5-3ed4-81ad-735fe2a76a60 | -5.09007 | -46.20336 | 2026-10-09 04:25:00 | NOAA-21 | AMARANTE DO MARANHÃO | MARANHÃO | Brasil | 2100600 | 21 | 33 | nan | nan | nan | Amazônia | 1.7 |
| 38dba20d-3269-37e0-ac11-dcab821a71da | -1.15475 | -54.22327 | 2026-10-09 04:25:00 | NOAA-21 | MONTE ALEGRE | PARÁ | Brasil | 1504802 | 15 | 33 | nan | nan | nan | Amazônia | 3.3 |
| 5c45cb8f-ab96-3b80-ad14-8a4a4ac18770 | -6.67873 | -46.05074 | 2026-10-09 04:25:00 | NOAA-21 | FORTALEZA DOS NOGUEIRAS | MARANHÃO | Brasil | 2104107 | 21 | 33 | nan | nan | nan | Cerrado | 1.1 |
| 7b082703-74f7-3862-811b-ca212c9f9b99 | -2.98588 | -54.06852 | 2026-10-09 04:25:00 | NOAA-21 | SANTARÉM | PARÁ | Brasil | 1506807 | 15 | 33 | nan | nan | nan | Amazônia | 1.9 |
| f5c22d45-1486-3f04-9661-f3970b6708e2 | -3.53592 | -54.66278 | 2026-10-09 04:25:00 | NOAA-21 | PLACAS | PARÁ | Brasil | 1505650 | 15 | 33 | nan | nan | nan | Amazônia | 2.1 |
| e25aaf54-2c44-3f17-929a-16369cbcce01 | -2.89155 | -54.16647 | 2026-10-09 04:25:00 | NOAA-21 | SANTARÉM | PARÁ | Brasil | 1506807 | 15 | 33 | nan | nan | nan | Amazônia | 2.1 |
| 4b3502eb-bade-3feb-add5-572ad2c34ab3 | -1.10363 | -54.17241 | 2026-10-09 04:25:00 | NOAA-21 | MONTE ALEGRE | PARÁ | Brasil | 1504802 | 15 | 33 | nan | nan | nan | Amazônia | 3.0 |
| 171e7893-94ec-3bba-ab3e-330a63068274 | -3.09994 | -54.27449 | 2026-10-09 04:25:00 | NOAA-21 | MOJUÍ DOS CAMPOS | PARÁ | Brasil | 1504752 | 15 | 33 | nan | nan | nan | Amazônia | 1.7 |
| 4f8df172-5454-3462-8127-8c55329d770c | -3.56981 | -54.68478 | 2026-10-09 04:25:00 | NOAA-21 | PLACAS | PARÁ | Brasil | 1505650 | 15 | 33 | nan | nan | nan | Amazônia | 6.2 |
| 106c3ca5-a2ef-3a2e-9874-f2bb3592db42 | -1.44968 | -54.47133 | 2026-10-09 04:25:00 | NOAA-21 | MONTE ALEGRE | PARÁ | Brasil | 1504802 | 15 | 33 | nan | nan | nan | Amazônia | 1.5 |
| 49237867-10da-3bcd-9a06-092b4f92757d | -1.14942 | -54.22322 | 2026-10-09 04:25:00 | NOAA-21 | MONTE ALEGRE | PARÁ | Brasil | 1504802 | 15 | 33 | nan | nan | nan | Amazônia | 3.0 |
| c1a6a5ce-367a-31ab-aa3c-7ff8f01d30d9 | -5.08707 | -46.13604 | 2026-10-09 04:25:00 | NOAA-21 | ARAME | MARANHÃO | Brasil | 2100956 | 21 | 33 | nan | nan | nan | Amazônia | 1.3 |
| 626ebbb6-4160-3abe-94c2-722363d18a24 | -3.17442 | -50.58089 | 2026-10-09 04:25:00 | NOAA-21 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 3.5 |
| f37aa546-6e1d-3b07-97e1-866913205a3c | -5.27654 | -55.95556 | 2026-10-09 04:25:00 | NOAA-21 | TRAIRÃO | PARÁ | Brasil | 1508050 | 15 | 33 | nan | nan | nan | Amazônia | 1.9 |
| b5551a97-a071-3273-9b1b-57a29a9f7edc | -6.22433 | -44.14911 | 2026-10-09 04:25:00 | NOAA-21 | COLINAS | MARANHÃO | Brasil | 2103505 | 21 | 33 | nan | nan | nan | Cerrado | 2.0 |
| 260017c7-c191-32ce-a064-1194ad550921 | -3.10692 | -53.95621 | 2026-10-09 04:25:00 | NOAA-21 | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | 2.5 |
| 9b5b8315-37b6-3e2a-a3e1-ca50b804c90d | -4.36522 | -55.6438 | 2026-10-09 04:25:00 | NOAA-21 | ITAITUBA | PARÁ | Brasil | 1503606 | 15 | 33 | nan | nan | nan | Amazônia | 2.2 |
| 7cd5097e-29dd-3416-8699-7448d7bed2e5 | -4.15237 | -48.55233 | 2026-10-09 04:25:00 | NOAA-21 | RONDON DO PARÁ | PARÁ | Brasil | 1506187 | 15 | 33 | nan | nan | nan | Amazônia | 6.7 |
| 2c1772a4-0458-38a7-8cd0-21a91236ce3e | -3.30887 | -53.70489 | 2026-10-09 04:25:00 | NOAA-21 | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | 4.3 |
| a2b5b252-8771-3962-98e4-f16d10e5fc18 | -5.71063 | -53.45601 | 2026-10-09 04:25:00 | NOAA-21 | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 2.3 |
| 1bc1b444-8fca-3741-8a6c-a484c85eaa9c | -2.55169 | -58.04086 | 2026-10-09 04:25:00 | NOAA-21 | SÃO SEBASTIÃO DO UATUMÃ | AMAZONAS | Brasil | 1303957 | 13 | 33 | nan | nan | nan | Amazônia | 3.7 |
| b3d18996-d121-343b-b835-00164dc4bdeb | -3.3145 | -54.03958 | 2026-10-09 04:25:00 | NOAA-21 | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | 1.6 |
| 6cb85e3a-abbb-3ddf-82f5-822e5c08a9f5 | -3.91325 | -55.89859 | 2026-10-09 04:25:00 | NOAA-21 | AVEIRO | PARÁ | Brasil | 1501006 | 15 | 33 | nan | nan | nan | Amazônia | 3.0 |
| 434acf27-9bc4-3f34-8f07-071558fb2c7e | -6.01289 | -40.9692 | 2026-10-09 04:25:00 | NOAA-21 | ASSUNÇÃO DO PIAUÍ | PIAUÍ | Brasil | 2201051 | 22 | 33 | nan | nan | nan | Caatinga | 33.3 |
| 9c01f57d-f128-324c-8e15-b853e8526fe9 | -5.06147 | -46.19189 | 2026-10-09 04:25:00 | NOAA-21 | AMARANTE DO MARANHÃO | MARANHÃO | Brasil | 2100600 | 21 | 33 | nan | nan | nan | Amazônia | 1.4 |
| 21e86f6f-a7a2-3f3d-86e7-b94726ffa0a3 | -3.12277 | -53.79705 | 2026-10-09 04:25:00 | NOAA-21 | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | 5.3 |
| f2f4d63e-acb5-3998-a9b7-be7a50a6f557 | -2.57855 | -56.18944 | 2026-10-09 04:25:00 | NOAA-21 | JURUTI | PARÁ | Brasil | 1503903 | 15 | 33 | nan | nan | nan | Amazônia | 4.9 |
| 5a341e89-06f4-380b-98f9-10900ea9723a | -6.58751 | -44.29483 | 2026-10-09 04:25:00 | NOAA-21 | PASTOS BONS | MARANHÃO | Brasil | 2108009 | 21 | 33 | nan | nan | nan | Cerrado | 1.4 |
| c4b96887-e08b-31f7-a466-24e74826bdfa | -3.69748 | -47.68164 | 2026-10-09 04:25:00 | NOAA-21 | ULIANÓPOLIS | PARÁ | Brasil | 1508126 | 15 | 33 | nan | nan | nan | Amazônia | 4.6 |
| d442e0c3-feee-3021-9d68-a6909fe266fb | -5.17564 | -45.61008 | 2026-10-09 04:25:00 | NOAA-21 | JENIPAPO DOS VIEIRAS | MARANHÃO | Brasil | 2105476 | 21 | 33 | nan | nan | nan | Cerrado | 1.0 |
| fec32246-c879-37c0-b9cc-8c09878468cb | -6.1577 | -47.91848 | 2026-10-09 04:25:00 | NOAA-21 | LUZINÓPOLIS | TOCANTINS | Brasil | 1712454 | 17 | 33 | nan | nan | nan | Cerrado | 1.3 |
| 369524f3-db5d-31fb-831e-c418de29bc98 | -3.10143 | -53.95839 | 2026-10-09 04:25:00 | NOAA-21 | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | 2.5 |
| b68fa07a-0904-3767-a6a4-db0321b339df | -3.48652 | -50.49451 | 2026-10-09 04:25:00 | NOAA-21 | PACAJÁ | PARÁ | Brasil | 1505486 | 15 | 33 | nan | nan | nan | Amazônia | 3.3 |
| 8a3165aa-e8f9-3fac-bc53-7194532ed257 | -3.2806 | -50.02481 | 2026-10-09 04:25:00 | NOAA-21 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 4.2 |
| 71eacd5e-ee2d-362c-bbf1-5def29440361 | -5.69971 | -53.47113 | 2026-10-09 04:25:00 | NOAA-21 | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 4.3 |
| 73c9f24c-6d14-3f4e-af79-60f47faf4fba | -5.70668 | -53.45781 | 2026-10-09 04:25:00 | NOAA-21 | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 2.4 |
| 5e57742a-6491-32da-93a7-cf220ea56596 | -4.08972 | -48.96359 | 2026-10-09 04:25:00 | NOAA-21 | GOIANÉSIA DO PARÁ | PARÁ | Brasil | 1503093 | 15 | 33 | nan | nan | nan | Amazônia | 4.9 |
| 4457b53c-172c-375f-b1b8-bbae5ddbd425 | -5.70092 | -41.72338 | 2026-10-09 04:25:00 | NOAA-21 | SÃO MIGUEL DO TAPUIO | PIAUÍ | Brasil | 2210409 | 22 | 33 | nan | nan | nan | Caatinga | 1.6 |
| 2ed3347a-c7c4-3aed-94ac-2b0b8e913615 | -3.0798 | -54.28263 | 2026-10-09 04:25:00 | NOAA-21 | MOJUÍ DOS CAMPOS | PARÁ | Brasil | 1504752 | 15 | 33 | nan | nan | nan | Amazônia | 1.8 |
| 306b2009-9efb-3b39-b1a8-15ea26332e65 | -3.82764 | -55.97227 | 2026-10-09 04:25:00 | NOAA-21 | AVEIRO | PARÁ | Brasil | 1501006 | 15 | 33 | nan | nan | nan | Amazônia | 1.9 |
| a658bfcc-e244-39c4-9998-ab93816f2308 | -3.16629 | -50.45722 | 2026-10-09 04:25:00 | NOAA-21 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 3.7 |
| 61db6186-308e-31e1-a6e9-38895ace8859 | -3.56796 | -54.66793 | 2026-10-09 04:25:00 | NOAA-21 | PLACAS | PARÁ | Brasil | 1505650 | 15 | 33 | nan | nan | nan | Amazônia | 2.5 |
| ed5c30f2-a96a-39f6-93a4-e56ac061c48f | -5.61674 | -44.84315 | 2026-10-09 04:25:00 | NOAA-21 | TUNTUM | MARANHÃO | Brasil | 2112308 | 21 | 33 | nan | nan | nan | Cerrado | 4.7 |
| 0710e4da-f35c-30c9-bddb-203ab77e5510 | -3.58874 | -54.5773 | 2026-10-09 04:25:00 | NOAA-21 | PLACAS | PARÁ | Brasil | 1505650 | 15 | 33 | nan | nan | nan | Amazônia | 3.0 |
| e7dc0911-ee7f-3cf5-b9b7-c570fe654791 | -3.01478 | -54.08215 | 2026-10-09 04:25:00 | NOAA-21 | SANTARÉM | PARÁ | Brasil | 1506807 | 15 | 33 | nan | nan | nan | Amazônia | 2.2 |
| 87e7ad43-c62a-3ff6-a58e-35b0e64106d0 | -3.93913 | -55.71513 | 2026-10-09 04:25:00 | NOAA-21 | AVEIRO | PARÁ | Brasil | 1501006 | 15 | 33 | nan | nan | nan | Amazônia | 1.5 |
| 60622a01-82c7-3567-bbb7-dc5fc079e06d | -4.07249 | -59.83598 | 2026-10-09 04:25:00 | NOAA-21 | AUTAZES | AMAZONAS | Brasil | 1300300 | 13 | 33 | nan | nan | nan | Amazônia | 6.1 |
| 352dc2f6-b55e-3522-969f-5b977beb7e23 | -3.21434 | -42.95999 | 2026-10-09 04:25:00 | NOAA-21 | SANTA QUITÉRIA DO MARANHÃO | MARANHÃO | Brasil | 2110104 | 21 | 33 | nan | nan | nan | Cerrado | 1.6 |
| 7d9849f1-3e77-3c8d-83da-f725fb944054 | -6.98064 | -45.0131 | 2026-10-09 04:25:00 | NOAA-21 | LORETO | MARANHÃO | Brasil | 2106102 | 21 | 33 | nan | nan | nan | Cerrado | 2.4 |
| 73197378-d3fc-395a-bb7a-ff516f415a3b | -3.18631 | -58.64816 | 2026-10-09 04:25:00 | NOAA-21 | ITACOATIARA | AMAZONAS | Brasil | 1301902 | 13 | 33 | nan | nan | nan | Amazônia | 7.2 |
| 7afb9018-f7d5-384c-84c5-e458fdb1cfec | -2.73733 | -54.10866 | 2026-10-09 04:25:00 | NOAA-21 | PRAINHA | PARÁ | Brasil | 1506005 | 15 | 33 | nan | nan | nan | Amazônia | 2.1 |
| 09c48985-6905-3925-aeb6-4325e3972892 | -3.73673 | -51.20598 | 2026-10-09 04:25:00 | NOAA-21 | PACAJÁ | PARÁ | Brasil | 1505486 | 15 | 33 | nan | nan | nan | Amazônia | 0.9 |
| 7f8cf3f6-cc1e-3898-8bdf-bd00d2a70537 | -5.97693 | -41.35345 | 2026-10-09 04:25:00 | NOAA-21 | SÃO MIGUEL DO TAPUIO | PIAUÍ | Brasil | 2210409 | 22 | 33 | nan | nan | nan | Caatinga | 0.6 |
| 4d94d111-cfd0-35be-a5f6-a0eb9675f922 | -2.07467 | -46.57196 | 2026-10-09 04:25:00 | NOAA-21 | CACHOEIRA DO PIRIÁ | PARÁ | Brasil | 1501956 | 15 | 33 | nan | nan | nan | Amazônia | 1.2 |


[Clique aqui para ver as próximas entradas](README92.md)
