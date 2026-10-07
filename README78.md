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

## Dados Diários - Página 78

| ID | Latitude | Longitude | Data/Hora GMT | Satélite | Município | Estado | País | Município ID | Estado ID | País ID | Dias sem Chuva | Precipitação | Risco de Fogo | Bioma | FRP |
|----|----------|-----------|---------------|----------|-----------|--------|------|--------------|-----------|---------|----------------|--------------|----------------|-------|-----|
| 72e57f0f-b13b-3cab-be10-77e27efe2506 | -3.25059 | -53.87586 | 2026-10-07 05:04:00 | NOAA-21 | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | 0.9 |
| 93d1976b-816a-3025-bca8-108994f8fed8 | -3.29614 | -54.02473 | 2026-10-07 05:04:00 | NOAA-21 | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | 12.1 |
| 34b523ca-1bdb-3cdc-b282-92c903c3d660 | -4.45613 | -47.9221 | 2026-10-07 05:04:00 | NOAA-21 | DOM ELISEU | PARÁ | Brasil | 1502939 | 15 | 33 | nan | nan | nan | Amazônia | 22.7 |
| 2a5b4da1-5075-3ec0-985c-42e27e746e6c | -3.35994 | -50.76509 | 2026-10-07 05:04:00 | NOAA-21 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 5.9 |
| afc8a76e-4a19-38e9-88c3-8b1541c056a2 | -4.76755 | -55.67382 | 2026-10-07 05:04:00 | NOAA-21 | TRAIRÃO | PARÁ | Brasil | 1508050 | 15 | 33 | nan | nan | nan | Amazônia | 1.6 |
| dc142553-e534-395a-abd3-dc4501ab0c6c | -5.72753 | -45.15854 | 2026-10-07 05:04:00 | NOAA-21 | BARRA DO CORDA | MARANHÃO | Brasil | 2101608 | 21 | 33 | nan | nan | nan | Cerrado | 6.4 |
| 8889763f-77d9-3419-8391-08be9138cef7 | -3.09828 | -53.7205 | 2026-10-07 05:04:00 | NOAA-21 | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | 1.0 |
| 6f6588ec-3cf7-3a03-8367-633d15166179 | -3.32961 | -58.15405 | 2026-10-07 05:04:00 | NOAA-21 | ITACOATIARA | AMAZONAS | Brasil | 1301902 | 13 | 33 | nan | nan | nan | Amazônia | 1.0 |
| 61c5ba44-c7db-3841-8274-18963e0bf437 | -2.10357 | -52.06381 | 2026-10-07 05:04:00 | NOAA-21 | PORTO DE MOZ | PARÁ | Brasil | 1505908 | 15 | 33 | nan | nan | nan | Amazônia | 2.8 |
| 35eaaa53-9687-317a-84c3-ccd89549f132 | -2.94747 | -54.16565 | 2026-10-07 05:04:00 | NOAA-21 | SANTARÉM | PARÁ | Brasil | 1506807 | 15 | 33 | nan | nan | nan | Amazônia | 2.3 |
| bb3ca681-c10b-3cbe-b4db-6b610389850e | -2.76679 | -54.10148 | 2026-10-07 05:04:00 | NOAA-21 | PRAINHA | PARÁ | Brasil | 1506005 | 15 | 33 | nan | nan | nan | Amazônia | 18.5 |
| ba2730dd-da2a-371d-8283-8ba227f32ef1 | -2.99766 | -54.12652 | 2026-10-07 05:04:00 | NOAA-21 | SANTARÉM | PARÁ | Brasil | 1506807 | 15 | 33 | nan | nan | nan | Amazônia | 1.0 |
| cc88f35a-4c82-3cec-b4d9-105d0b24bfb7 | -3.76668 | -59.32301 | 2026-10-07 05:04:00 | NOAA-21 | AUTAZES | AMAZONAS | Brasil | 1300300 | 13 | 33 | nan | nan | nan | Amazônia | 2.2 |
| 63e246eb-8d17-3c26-9c06-375416148d22 | -2.48283 | -56.09595 | 2026-10-07 05:04:00 | NOAA-21 | JURUTI | PARÁ | Brasil | 1503903 | 15 | 33 | nan | nan | nan | Amazônia | 1.8 |
| beb07bb6-bfdd-3ba5-ab84-88fd2ebff4f8 | -3.54681 | -50.09204 | 2026-10-07 05:04:00 | NOAA-21 | PACAJÁ | PARÁ | Brasil | 1505486 | 15 | 33 | nan | nan | nan | Amazônia | 2.8 |
| fb6e54ff-f4db-3c21-9b19-e38cdb63d7d1 | -2.99704 | -54.10843 | 2026-10-07 05:04:00 | NOAA-21 | SANTARÉM | PARÁ | Brasil | 1506807 | 15 | 33 | nan | nan | nan | Amazônia | 4.1 |
| 92c2dda0-d9b5-3020-8809-367876d465f2 | -8.70096 | -45.21375 | 2026-10-07 05:04:00 | NOAA-21 | BAIXA GRANDE DO RIBEIRO | PIAUÍ | Brasil | 2201150 | 22 | 33 | nan | nan | nan | Cerrado | 7.9 |
| 29e17d06-ff20-3b0e-9289-e73f8ad14c5e | -2.48337 | -55.76516 | 2026-10-07 05:04:00 | NOAA-21 | SANTARÉM | PARÁ | Brasil | 1506807 | 15 | 33 | nan | nan | nan | Amazônia | 2.0 |
| c274bbc6-d46f-3885-9c42-a5fd428c1875 | -1.9525 | -54.04381 | 2026-10-07 05:04:00 | NOAA-21 | MONTE ALEGRE | PARÁ | Brasil | 1504802 | 15 | 33 | nan | nan | nan | Amazônia | 2.7 |
| 105b88e8-00d4-3fb4-a68a-2d3a40b0ef90 | -3.68377 | -55.9472 | 2026-10-07 05:04:00 | NOAA-21 | AVEIRO | PARÁ | Brasil | 1501006 | 15 | 33 | nan | nan | nan | Amazônia | 2.0 |
| 0fda3f34-4d53-3797-a89b-b2e26bc04e57 | -3.76627 | -59.32023 | 2026-10-07 05:04:00 | NOAA-21 | AUTAZES | AMAZONAS | Brasil | 1300300 | 13 | 33 | nan | nan | nan | Amazônia | 1.9 |
| 7448ac5f-949d-3f21-9714-abc4244f3d5f | -6.21474 | -52.68656 | 2026-10-07 05:04:00 | NOAA-21 | SÃO FÉLIX DO XINGU | PARÁ | Brasil | 1507300 | 15 | 33 | nan | nan | nan | Amazônia | 1.3 |
| 0f9f8a12-99df-372d-8ea9-38a6f6c4206a | -1.1048 | -54.15713 | 2026-10-07 05:04:00 | NOAA-21 | MONTE ALEGRE | PARÁ | Brasil | 1504802 | 15 | 33 | nan | nan | nan | Amazônia | 1.8 |
| 85b456c4-5423-314c-abbd-ab5f033c9570 | -7.18635 | -52.62571 | 2026-10-07 05:04:00 | NOAA-21 | SÃO FÉLIX DO XINGU | PARÁ | Brasil | 1507300 | 15 | 33 | nan | nan | nan | Amazônia | 1.8 |
| bfe34108-8e29-3511-a4bd-7cdbb42620d9 | -2.8918 | -54.10685 | 2026-10-07 05:04:00 | NOAA-21 | SANTARÉM | PARÁ | Brasil | 1506807 | 15 | 33 | nan | nan | nan | Amazônia | 2.4 |
| 64bd9d5f-9efe-33b6-93dd-845518bbc08e | -2.90206 | -54.01839 | 2026-10-07 05:04:00 | NOAA-21 | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | 2.0 |
| e01c66a1-f95c-3ab6-81b9-b52b6d85b8a6 | -7.21705 | -55.17037 | 2026-10-07 05:04:00 | NOAA-21 | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 2.5 |
| e30ef5e8-0e9c-3dbf-aeef-a72deaeec0f8 | -3.07549 | -54.26045 | 2026-10-07 05:04:00 | NOAA-21 | MOJUÍ DOS CAMPOS | PARÁ | Brasil | 1504752 | 15 | 33 | nan | nan | nan | Amazônia | 2.7 |
| b3c5c08b-29a7-3f65-b410-d997bef53bbe | -4.77467 | -50.81489 | 2026-10-07 05:04:00 | NOAA-21 | NOVO REPARTIMENTO | PARÁ | Brasil | 1505064 | 15 | 33 | nan | nan | nan | Amazônia | 1.5 |
| 262f2a15-a9f2-31e9-b2bc-fb7a18d1005d | -7.71446 | -45.44405 | 2026-10-07 05:04:00 | NOAA-21 | RIBEIRO GONÇALVES | PIAUÍ | Brasil | 2208908 | 22 | 33 | nan | nan | nan | Cerrado | 9.7 |
| 5b301af5-e241-3e1c-a496-adb8108307c7 | -1.10694 | -54.14334 | 2026-10-07 05:04:00 | NOAA-21 | MONTE ALEGRE | PARÁ | Brasil | 1504802 | 15 | 33 | nan | nan | nan | Amazônia | 1.7 |
| 0d3b218e-c524-39be-91bd-8a7bcfd2a1fe | -2.9837 | -54.10638 | 2026-10-07 05:04:00 | NOAA-21 | SANTARÉM | PARÁ | Brasil | 1506807 | 15 | 33 | nan | nan | nan | Amazônia | 2.9 |
| 824b8a6e-1a26-3ef1-bddd-efb927f847db | -2.99293 | -54.04654 | 2026-10-07 05:04:00 | NOAA-21 | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | 2.4 |
| 91e52888-3bdc-3866-af32-4ed119755c5e | -3.37773 | -58.19452 | 2026-10-07 05:04:00 | NOAA-21 | ITACOATIARA | AMAZONAS | Brasil | 1301902 | 13 | 33 | nan | nan | nan | Amazônia | 3.1 |
| 86bbd44e-aa4e-3ad1-9ee1-da0cfd726e65 | -3.90707 | -55.89064 | 2026-10-07 05:04:00 | NOAA-21 | AVEIRO | PARÁ | Brasil | 1501006 | 15 | 33 | nan | nan | nan | Amazônia | 1.9 |
| 6ab3a697-c797-3ea3-8227-61dee02fb1c8 | -3.16435 | -50.59985 | 2026-10-07 05:04:00 | NOAA-21 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 3.0 |
| 3204457b-6665-3e1d-a142-cf0644f7218a | -2.8681 | -54.14982 | 2026-10-07 05:04:00 | NOAA-21 | SANTARÉM | PARÁ | Brasil | 1506807 | 15 | 33 | nan | nan | nan | Amazônia | 2.5 |
| 9277bc70-34f9-334b-a7e0-6a15a879870c | -3.56171 | -54.48228 | 2026-10-07 05:04:00 | NOAA-21 | PLACAS | PARÁ | Brasil | 1505650 | 15 | 33 | nan | nan | nan | Amazônia | 1.7 |
| 4e3fa11c-c3f9-369b-a2ae-b450ad6415cf | -3.42526 | -52.54507 | 2026-10-07 05:04:00 | NOAA-21 | BRASIL NOVO | PARÁ | Brasil | 1501725 | 15 | 33 | nan | nan | nan | Amazônia | 1.2 |
| a94ec5f1-ce11-3327-8e5c-ff83c829fbab | -2.9827 | -54.13498 | 2026-10-07 05:04:00 | NOAA-21 | SANTARÉM | PARÁ | Brasil | 1506807 | 15 | 33 | nan | nan | nan | Amazônia | 1.8 |
| fe30c78c-6777-3a2c-a635-686264fea0f8 | -4.11239 | -54.02187 | 2026-10-07 05:04:00 | NOAA-21 | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | 3.5 |
| b18c984d-8a70-3efb-9c4c-ded5876b6519 | -2.02031 | -56.89242 | 2026-10-07 05:04:00 | NOAA-21 | NHAMUNDÁ | AMAZONAS | Brasil | 1303007 | 13 | 33 | nan | nan | nan | Amazônia | 2.0 |
| 651fa58a-82ce-379a-8c76-6c8120ba9878 | -3.50457 | -54.63011 | 2026-10-07 05:04:00 | NOAA-21 | PLACAS | PARÁ | Brasil | 1505650 | 15 | 33 | nan | nan | nan | Amazônia | 1.8 |
| 05457ed4-70d8-3a97-8e5a-47bf185b3ad0 | -2.67462 | -56.45786 | 2026-10-07 05:04:00 | NOAA-21 | JURUTI | PARÁ | Brasil | 1503903 | 15 | 33 | nan | nan | nan | Amazônia | 0.9 |
| 07fce9cf-5d49-386e-9d53-45273b7a2978 | -2.06298 | -56.86506 | 2026-10-07 05:04:00 | NOAA-21 | NHAMUNDÁ | AMAZONAS | Brasil | 1303007 | 13 | 33 | nan | nan | nan | Amazônia | 1.4 |
| ab43f282-7073-3ab9-8ac9-3ddc47b494a9 | -2.77399 | -54.099 | 2026-10-07 05:04:00 | NOAA-21 | PRAINHA | PARÁ | Brasil | 1506005 | 15 | 33 | nan | nan | nan | Amazônia | 12.7 |
| 99d95007-61dd-381c-8c60-3fbbbde27356 | -3.136 | -51.02999 | 2026-10-07 05:04:00 | NOAA-21 | PACAJÁ | PARÁ | Brasil | 1505486 | 15 | 33 | nan | nan | nan | Amazônia | 5.0 |
| 960508db-253d-3c3b-a4a7-ec6005bfb465 | -3.06766 | -54.37693 | 2026-10-07 05:04:00 | NOAA-21 | MOJUÍ DOS CAMPOS | PARÁ | Brasil | 1504752 | 15 | 33 | nan | nan | nan | Amazônia | 1.0 |
| e6db5af4-d678-3456-8e44-38cad6f30761 | -7.87539 | -44.19006 | 2026-10-07 05:04:00 | NOAA-21 | SEBASTIÃO LEAL | PIAUÍ | Brasil | 2210631 | 22 | 33 | nan | nan | nan | Cerrado | 9.2 |
| 7df4b422-cd1c-399c-818e-8f314bd990d4 | -3.05373 | -54.22488 | 2026-10-07 05:04:00 | NOAA-21 | SANTARÉM | PARÁ | Brasil | 1506807 | 15 | 33 | nan | nan | nan | Amazônia | 1.7 |
| 4dfd5312-a970-3dc1-aa01-84f1644fb040 | -2.77066 | -54.09849 | 2026-10-07 05:04:00 | NOAA-21 | PRAINHA | PARÁ | Brasil | 1506005 | 15 | 33 | nan | nan | nan | Amazônia | 18.5 |
| da91a260-bba8-39a6-a553-5fc2957e2551 | -3.1649 | -50.43806 | 2026-10-07 05:04:00 | NOAA-21 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 1.4 |
| af32cf1c-992a-38f0-8da5-6057d20703c3 | -5.97035 | -55.35829 | 2026-10-07 05:04:00 | NOAA-21 | ITAITUBA | PARÁ | Brasil | 1503606 | 15 | 33 | nan | nan | nan | Amazônia | 1.6 |
| 0af8c9ac-c203-3b0f-bee0-98e2f88c0fbd | -3.05652 | -54.2289 | 2026-10-07 05:04:00 | NOAA-21 | SANTARÉM | PARÁ | Brasil | 1506807 | 15 | 33 | nan | nan | nan | Amazônia | 1.5 |
| ce0fbeaf-37dd-3b0a-8509-896816fa0044 | -3.1045 | -53.76917 | 2026-10-07 05:04:00 | NOAA-21 | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | 3.5 |
| b723cca0-406c-39cf-bd7f-0100286785b4 | -5.9891 | -55.36832 | 2026-10-07 05:04:00 | NOAA-21 | ITAITUBA | PARÁ | Brasil | 1503606 | 15 | 33 | nan | nan | nan | Amazônia | 2.0 |
| 388c79ed-601d-3a51-9cdb-4a05fa578b88 | -3.79368 | -58.29342 | 2026-10-07 05:04:00 | NOAA-21 | NOVA OLINDA DO NORTE | AMAZONAS | Brasil | 1303106 | 13 | 33 | nan | nan | nan | Amazônia | 2.5 |
| aca442de-f45e-30ed-892d-75aa4a9e145e | -3.52238 | -58.7499 | 2026-10-07 05:04:00 | NOAA-21 | ITACOATIARA | AMAZONAS | Brasil | 1301902 | 13 | 33 | nan | nan | nan | Amazônia | 1.3 |
| 0928d1bf-9326-3380-9fd1-b02cac7fc653 | -3.90066 | -55.4738 | 2026-10-07 05:04:00 | NOAA-21 | AVEIRO | PARÁ | Brasil | 1501006 | 15 | 33 | nan | nan | nan | Amazônia | 1.5 |
| d8707887-ccc3-3aab-be9a-95e97c043e06 | -3.6559 | -59.16094 | 2026-10-07 05:04:00 | NOAA-21 | AUTAZES | AMAZONAS | Brasil | 1300300 | 13 | 33 | nan | nan | nan | Amazônia | 1.9 |
| f025a2e5-2aa8-3ef6-9ec1-989bad59f465 | -3.8129 | -51.03962 | 2026-10-07 05:04:00 | NOAA-21 | PACAJÁ | PARÁ | Brasil | 1505486 | 15 | 33 | nan | nan | nan | Amazônia | 3.3 |
| 3e07553c-5065-3b45-a6a0-75026d8b55b0 | -3.28897 | -54.07068 | 2026-10-07 05:04:00 | NOAA-21 | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | 15.5 |
| 29e246c8-8a01-31a9-9289-d29e75004a77 | -3.81363 | -51.03475 | 2026-10-07 05:04:00 | NOAA-21 | PACAJÁ | PARÁ | Brasil | 1505486 | 15 | 33 | nan | nan | nan | Amazônia | 3.3 |
| a61418b3-e5c3-3e1c-97ef-190719a672bb | 0.68597 | -60.07692 | 2026-10-07 05:04:00 | NOAA-21 | SÃO LUIZ | RORAIMA | Brasil | 1400605 | 14 | 33 | nan | nan | nan | Amazônia | 1.6 |
| 628db91c-3cca-33f7-ab02-a34a94d852ab | -4.75428 | -55.65067 | 2026-10-07 05:04:00 | NOAA-21 | TRAIRÃO | PARÁ | Brasil | 1508050 | 15 | 33 | nan | nan | nan | Amazônia | 1.5 |
| 35737a2b-1d18-310b-87fb-e90e55b2bc62 | -8.70214 | -45.20438 | 2026-10-07 05:04:00 | NOAA-21 | BAIXA GRANDE DO RIBEIRO | PIAUÍ | Brasil | 2201150 | 22 | 33 | nan | nan | nan | Cerrado | 9.4 |
| 88ebbbbb-e3f6-3b3f-9b81-69cc840eb3d5 | -3.50111 | -51.69085 | 2026-10-07 05:04:00 | NOAA-21 | ANAPU | PARÁ | Brasil | 1500859 | 15 | 33 | nan | nan | nan | Amazônia | 2.5 |
| 00a948e8-6977-34bf-904a-cedc34db2ff7 | -2.95784 | -54.16347 | 2026-10-07 05:04:00 | NOAA-21 | SANTARÉM | PARÁ | Brasil | 1506807 | 15 | 33 | nan | nan | nan | Amazônia | 2.0 |
| 07abb412-056a-3689-8b98-13e53c39a49f | -3.55495 | -59.47682 | 2026-10-07 05:04:00 | NOAA-21 | AUTAZES | AMAZONAS | Brasil | 1300300 | 13 | 33 | nan | nan | nan | Amazônia | 6.5 |
| 2fd47504-9520-3864-8fd6-e063b81ab0c9 | -2.9508 | -54.16616 | 2026-10-07 05:04:00 | NOAA-21 | SANTARÉM | PARÁ | Brasil | 1506807 | 15 | 33 | nan | nan | nan | Amazônia | 2.3 |
| cbe9fcd7-0ea1-3b66-88e8-762cc4d62f02 | -3.18485 | -50.56857 | 2026-10-07 05:04:00 | NOAA-21 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 13.4 |
| fafac88b-2061-3690-b813-f8fb9bfd17b0 | -5.89647 | -53.64206 | 2026-10-07 05:04:00 | NOAA-21 | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 1.1 |
| 65d0d63e-fcf6-3be4-baa6-8ef87b0a6b04 | -2.93279 | -53.84153 | 2026-10-07 05:04:00 | NOAA-21 | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | 1.0 |
| fa35e494-f6a5-3874-9297-5322dde2c769 | -3.21084 | -53.87316 | 2026-10-07 05:04:00 | NOAA-21 | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | 3.2 |
| 589b27a9-2dd8-36a7-b4b7-970ae4235847 | -3.03764 | -53.91219 | 2026-10-07 05:04:00 | NOAA-21 | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | 2.3 |
| 525936be-013a-3ae4-9740-a4c90b1fbd26 | -4.38342 | -59.90211 | 2026-10-07 05:04:00 | NOAA-21 | BORBA | AMAZONAS | Brasil | 1300805 | 13 | 33 | nan | nan | nan | Amazônia | 2.7 |
| 1d171d4c-8124-34ca-bf48-f4d06a7e2cc9 | -2.90151 | -54.02192 | 2026-10-07 05:04:00 | NOAA-21 | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | 2.0 |
| c33e0e0c-3a07-3f79-822d-9a244dba6011 | -3.06992 | -54.25242 | 2026-10-07 05:04:00 | NOAA-21 | MOJUÍ DOS CAMPOS | PARÁ | Brasil | 1504752 | 15 | 33 | nan | nan | nan | Amazônia | 4.7 |
| bf41f47c-7e0f-3ff7-bca0-a8c7cbfdd686 | -3.48209 | -59.47224 | 2026-10-07 05:04:00 | NOAA-21 | CAREIRO DA VÁRZEA | AMAZONAS | Brasil | 1301159 | 13 | 33 | nan | nan | nan | Amazônia | 2.2 |
| 5752e1b9-6647-330d-9863-7240e0f731b2 | -6.04791 | -53.47604 | 2026-10-07 05:04:00 | NOAA-21 | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 1.6 |
| 74ed4126-1564-3426-ac2f-ad08d4a5afd3 | -5.6809 | -53.48916 | 2026-10-07 05:04:00 | NOAA-21 | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 2.2 |
| 61c038f8-ce88-345a-9049-7506d3d8cfb0 | -3.05492 | -54.1533 | 2026-10-07 05:04:00 | NOAA-21 | SANTARÉM | PARÁ | Brasil | 1506807 | 15 | 33 | nan | nan | nan | Amazônia | 2.2 |
| 822cd1f5-25b3-3a64-aef5-4684db9b6118 | -3.11234 | -53.76305 | 2026-10-07 05:04:00 | NOAA-21 | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | 1.8 |
| 36737b34-e308-3a0e-ba6b-ba70ab36d3a3 | -2.93972 | -54.17164 | 2026-10-07 05:04:00 | NOAA-21 | SANTARÉM | PARÁ | Brasil | 1506807 | 15 | 33 | nan | nan | nan | Amazônia | 4.1 |
| 9d9ac51f-cdca-3b76-8546-00910f0f3e1a | -2.49103 | -58.06627 | 2026-10-07 05:04:00 | NOAA-21 | SÃO SEBASTIÃO DO UATUMÃ | AMAZONAS | Brasil | 1303957 | 13 | 33 | nan | nan | nan | Amazônia | 1.7 |
| 4af259bf-78a2-345f-aa68-a08bfceae8b6 | -2.98291 | -54.04499 | 2026-10-07 05:04:00 | NOAA-21 | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | 1.0 |
| d31d4db3-f59f-3db9-921f-14f338d73382 | -3.00541 | -54.12052 | 2026-10-07 05:04:00 | NOAA-21 | SANTARÉM | PARÁ | Brasil | 1506807 | 15 | 33 | nan | nan | nan | Amazônia | 9.7 |
| 73a65f5e-af89-314c-9c5a-2de05dc2e5d0 | -3.27036 | -54.2979 | 2026-10-07 05:04:00 | NOAA-21 | MOJUÍ DOS CAMPOS | PARÁ | Brasil | 1504752 | 15 | 33 | nan | nan | nan | Amazônia | 0.9 |
| 9e4604dd-4d68-33b7-a81a-f10dab7dbd4d | -3.2651 | -50.41135 | 2026-10-07 05:04:00 | NOAA-21 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 2.3 |
| bd8baabf-9758-37d2-aaf6-e17c574728cd | -3.06903 | -54.16983 | 2026-10-07 05:04:00 | NOAA-21 | SANTARÉM | PARÁ | Brasil | 1506807 | 15 | 33 | nan | nan | nan | Amazônia | 2.5 |
| 02929c7f-1104-3e08-a241-35b4f66e508e | -3.24052 | -53.87432 | 2026-10-07 05:04:00 | NOAA-21 | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | 2.8 |
| 0e0e9785-88cd-3724-9ded-2a5d9fb9d1a8 | -3.47754 | -54.6295 | 2026-10-07 05:04:00 | NOAA-21 | PLACAS | PARÁ | Brasil | 1505650 | 15 | 33 | nan | nan | nan | Amazônia | 2.4 |
| bf941cf2-6130-380b-ba89-4acc69552518 | -2.77237 | -54.10951 | 2026-10-07 05:04:00 | NOAA-21 | PRAINHA | PARÁ | Brasil | 1506005 | 15 | 33 | nan | nan | nan | Amazônia | 39.8 |
| 6e5ce41b-e803-3f47-9dd0-be201b46175e | -3.04549 | -53.92794 | 2026-10-07 05:04:00 | NOAA-21 | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | 2.0 |
| cbc2d1b6-b14a-3add-bc0e-6a43003006d0 | -3.10165 | -53.72102 | 2026-10-07 05:04:00 | NOAA-21 | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | 1.0 |
| 9b41ce0d-9c30-34a9-8a1c-fcf6ab3eff78 | -3.99663 | -56.25175 | 2026-10-07 05:04:00 | NOAA-21 | AVEIRO | PARÁ | Brasil | 1501006 | 15 | 33 | nan | nan | nan | Amazônia | 1.1 |
| 790e5d5e-933a-3fa8-afed-a2f5e563f422 | -2.78703 | -51.68334 | 2026-10-07 05:04:00 | NOAA-21 | ANAPU | PARÁ | Brasil | 1500859 | 15 | 33 | nan | nan | nan | Amazônia | 12.5 |
| b0895fca-00aa-3d4a-8154-c6d829a02574 | -3.58998 | -55.5654 | 2026-10-07 05:04:00 | NOAA-21 | AVEIRO | PARÁ | Brasil | 1501006 | 15 | 33 | nan | nan | nan | Amazônia | 2.9 |
| 6128488b-cac2-3d1e-8f41-1b69e346c9fb | -3.16039 | -50.44102 | 2026-10-07 05:04:00 | NOAA-21 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 1.4 |
| 649da8bd-1ce7-3d1f-98f8-cb3ff522a36b | -5.88348 | -52.04356 | 2026-10-07 05:04:00 | NOAA-21 | SÃO FÉLIX DO XINGU | PARÁ | Brasil | 1507300 | 15 | 33 | nan | nan | nan | Amazônia | 0.8 |


[Clique aqui para ver as próximas entradas](README79.md)
