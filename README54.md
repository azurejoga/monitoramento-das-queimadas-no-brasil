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

## Dados Diários - Página 54

| ID | Latitude | Longitude | Data/Hora GMT | Satélite | Município | Estado | País | Município ID | Estado ID | País ID | Dias sem Chuva | Precipitação | Risco de Fogo | Bioma | FRP |
|----|----------|-----------|---------------|----------|-----------|--------|------|--------------|-----------|---------|----------------|--------------|----------------|-------|-----|
| b01b4824-a35b-3967-a5e7-ee3720b2351c | -4.83232 | -45.33585 | 2025-10-27 04:59:00 | NPP-375D | LAGOA GRANDE DO MARANHÃO | MARANHÃO | Brasil | 2105963 | 21 | 33 | nan | nan | nan | Cerrado | 0.9 |
| 9d39f85d-05f3-3060-a51a-e820a986fc7e | -4.38459 | -43.32192 | 2025-10-27 04:59:00 | NPP-375D | ALDEIAS ALTAS | MARANHÃO | Brasil | 2100303 | 21 | 33 | nan | nan | nan | Cerrado | 3.8 |
| 05bdbc68-5579-3b2b-88ce-9534b97d45df | 1.62166 | -55.72038 | 2025-10-27 04:59:00 | NPP-375D | ÓBIDOS | PARÁ | Brasil | 1505106 | 15 | 33 | nan | nan | nan | Amazônia | 1.4 |
| d3e3973a-8675-337c-8270-83847354ade8 | -3.77301 | -54.29641 | 2025-10-27 04:59:00 | NPP-375D | PLACAS | PARÁ | Brasil | 1505650 | 15 | 33 | nan | nan | nan | Amazônia | 0.8 |
| 54c04037-7ca9-325f-b99f-4373214da7a0 | -3.14692 | -50.33433 | 2025-10-27 04:59:00 | NPP-375D | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 2.4 |
| e9e6eeac-923d-39ca-a975-2e03bb769a16 | -4.22442 | -48.36443 | 2025-10-27 04:59:00 | NPP-375D | RONDON DO PARÁ | PARÁ | Brasil | 1506187 | 15 | 33 | nan | nan | nan | Amazônia | 0.8 |
| a16e0dd0-0abb-3a71-ad9a-8b99591945a0 | -3.04835 | -53.01267 | 2025-10-27 04:59:00 | NPP-375D | MEDICILÂNDIA | PARÁ | Brasil | 1504455 | 15 | 33 | nan | nan | nan | Amazônia | 2.2 |
| 724a0e32-1560-3701-bb54-4f340015f855 | -5.35981 | -45.04835 | 2025-10-27 04:59:00 | NPP-375D | BARRA DO CORDA | MARANHÃO | Brasil | 2101608 | 21 | 33 | nan | nan | nan | Cerrado | 1.3 |
| 8ba8ff7f-0c3d-382d-a171-497124bd46f1 | -3.24207 | -50.65531 | 2025-10-27 04:59:00 | NPP-375D | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 1.5 |
| d03d68ad-0aef-378a-969d-8c0b9e3c5ecf | 1.61205 | -55.73051 | 2025-10-27 04:59:00 | NPP-375D | ÓBIDOS | PARÁ | Brasil | 1505106 | 15 | 33 | nan | nan | nan | Amazônia | 1.2 |
| 4ac853e3-6ec7-3912-8dc6-a4a3c8a51549 | -3.08989 | -49.52324 | 2025-10-27 04:59:00 | NPP-375D | MOJU | PARÁ | Brasil | 1504703 | 15 | 33 | nan | nan | nan | Amazônia | 1.4 |
| 6e20c18f-af3c-3d0c-b426-90c3732d500a | -3.575 | -49.01818 | 2025-10-27 04:59:00 | NPP-375D | GOIANÉSIA DO PARÁ | PARÁ | Brasil | 1503093 | 15 | 33 | nan | nan | nan | Amazônia | 1.2 |
| dd57961c-61a8-391c-8b7f-f261a86c7a5f | -3.70518 | -53.37764 | 2025-10-27 04:59:00 | NPP-375D | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | 0.7 |
| 76fa46c6-998f-3974-9651-4354683c590d | -3.60403 | -49.34735 | 2025-10-27 04:59:00 | NPP-375D | BREU BRANCO | PARÁ | Brasil | 1501782 | 15 | 33 | nan | nan | nan | Amazônia | 0.8 |
| 588ac9f1-c7ce-36b7-9162-e6a9705bf022 | -4.45729 | -43.43138 | 2025-10-27 04:59:00 | NPP-375D | ALDEIAS ALTAS | MARANHÃO | Brasil | 2100303 | 21 | 33 | nan | nan | nan | Cerrado | 1.0 |
| b9fcb06a-c6f8-3736-8f4b-3013bae4882b | -3.10741 | -50.17901 | 2025-10-27 04:59:00 | NPP-375D | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 0.9 |
| 45f6a2bf-01ae-3f5a-83fb-cb200cd0aaa7 | -1.23273 | -55.6909 | 2025-10-27 04:59:00 | NPP-375D | ÓBIDOS | PARÁ | Brasil | 1505106 | 15 | 33 | nan | nan | nan | Amazônia | 0.6 |
| f0d08e5f-924a-338d-ac28-04a2b10aa662 | -4.39106 | -43.31874 | 2025-10-27 04:59:00 | NPP-375D | ALDEIAS ALTAS | MARANHÃO | Brasil | 2100303 | 21 | 33 | nan | nan | nan | Cerrado | 3.8 |
| 96be4e5d-b4d3-33c8-803b-06367b2898cb | 0.16129 | -51.01819 | 2025-10-27 04:59:00 | NPP-375D | MACAPÁ | AMAPÁ | Brasil | 1600303 | 16 | 33 | nan | nan | nan | Amazônia | 0.9 |
| bfadc6f4-1e51-3a9e-a4fb-623634cce165 | -5.59396 | -41.31813 | 2025-10-27 04:59:00 | NPP-375D | SÃO MIGUEL DO TAPUIO | PIAUÍ | Brasil | 2210409 | 22 | 33 | nan | nan | nan | Caatinga | 1.1 |
| dfad1854-aa78-393d-b66c-58867af21136 | -4.45324 | -43.41838 | 2025-10-27 04:59:00 | NPP-375D | ALDEIAS ALTAS | MARANHÃO | Brasil | 2100303 | 21 | 33 | nan | nan | nan | Cerrado | 0.9 |
| 892fffae-e79a-3a92-82d7-4a2cb75d531a | -3.57818 | -49.02377 | 2025-10-27 04:59:00 | NPP-375D | GOIANÉSIA DO PARÁ | PARÁ | Brasil | 1503093 | 15 | 33 | nan | nan | nan | Amazônia | 1.2 |
| 96263da0-156f-31cb-a2c0-027c33dadaf2 | -5.1041 | -43.19975 | 2025-10-27 04:59:00 | NPP-375D | CAXIAS | MARANHÃO | Brasil | 2103000 | 21 | 33 | nan | nan | nan | Cerrado | 2.6 |
| 8d129609-9f48-3b48-b3a5-b5feaadfca51 | -3.5691 | -44.52832 | 2025-10-27 04:59:00 | NPP-375D | MIRANDA DO NORTE | MARANHÃO | Brasil | 2106755 | 21 | 33 | nan | nan | nan | Cerrado | 2.7 |
| e5f5a24f-ef9b-3abc-9b7a-c274c680fef1 | -4.43917 | -45.98213 | 2025-10-27 04:59:00 | NPP-375D | SANTA LUZIA | MARANHÃO | Brasil | 2110005 | 21 | 33 | nan | nan | nan | Amazônia | 13.3 |
| ed62b910-ad39-32ca-92f7-7724559ac092 | -3.46827 | -49.96854 | 2025-10-27 04:59:00 | NPP-375D | PACAJÁ | PARÁ | Brasil | 1505486 | 15 | 33 | nan | nan | nan | Amazônia | 2.6 |
| 58d2f9ad-e9a7-3a61-86a4-64efaaf62f02 | -3.8046 | -49.29293 | 2025-10-27 04:59:00 | NPP-375D | BREU BRANCO | PARÁ | Brasil | 1501782 | 15 | 33 | nan | nan | nan | Amazônia | 3.8 |
| fe5a00f5-2faa-3753-b747-6755e285aa43 | 1.6802 | -55.66548 | 2025-10-27 04:59:00 | NPP-375D | ÓBIDOS | PARÁ | Brasil | 1505106 | 15 | 33 | nan | nan | nan | Amazônia | 0.9 |
| ba74a154-e954-3ed2-8450-1e03e4c2b77e | -4.15762 | -51.14217 | 2025-10-27 04:59:00 | NPP-375D | ANAPU | PARÁ | Brasil | 1500859 | 15 | 33 | nan | nan | nan | Amazônia | 1.9 |
| a49729b1-eeb7-3f8c-a5da-e0d0d31e8876 | -4.16039 | -51.07784 | 2025-10-27 04:59:00 | NPP-375D | PACAJÁ | PARÁ | Brasil | 1505486 | 15 | 33 | nan | nan | nan | Amazônia | 1.5 |
| ab97bd98-2c75-3b2e-9d0d-2bf1f836a812 | -3.32534 | -52.62702 | 2025-10-27 04:59:00 | NPP-375D | BRASIL NOVO | PARÁ | Brasil | 1501725 | 15 | 33 | nan | nan | nan | Amazônia | 3.5 |
| 858521fc-c5c2-3915-b740-0e6e82476b03 | -4.33031 | -48.09171 | 2025-10-27 04:59:00 | NPP-375D | RONDON DO PARÁ | PARÁ | Brasil | 1506187 | 15 | 33 | nan | nan | nan | Amazônia | 1.7 |
| 31243f2f-8c3c-3927-b0cc-7702d45961cb | -4.38983 | -43.32701 | 2025-10-27 04:59:00 | NPP-375D | ALDEIAS ALTAS | MARANHÃO | Brasil | 2100303 | 21 | 33 | nan | nan | nan | Cerrado | 4.5 |
| fbbe22bd-4612-3669-8680-4a7bd0b20641 | -3.09858 | -51.27913 | 2025-10-27 04:59:00 | NPP-375D | ANAPU | PARÁ | Brasil | 1500859 | 15 | 33 | nan | nan | nan | Amazônia | 0.9 |
| 345f4239-d236-3383-aecc-8504e5836cea | -3.24852 | -50.04085 | 2025-10-27 04:59:00 | NPP-375D | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 1.6 |
| 58129461-d457-3e1d-baaa-6cd90f37bb69 | -3.39448 | -50.39536 | 2025-10-27 04:59:00 | NPP-375D | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 1.4 |
| af212770-b2ea-3a76-8d72-d7dd13e3d0ae | -4.4398 | -43.42883 | 2025-10-27 04:59:00 | NPP-375D | ALDEIAS ALTAS | MARANHÃO | Brasil | 2100303 | 21 | 33 | nan | nan | nan | Cerrado | 1.2 |
| afe833b7-97b3-3053-8849-34e1951345f5 | -4.86596 | -43.25341 | 2025-10-27 04:59:00 | NPP-375D | CAXIAS | MARANHÃO | Brasil | 2103000 | 21 | 33 | nan | nan | nan | Cerrado | 5.0 |
| d22dc5c6-ae73-38a5-a3ff-13c0936ca17d | -4.52282 | -44.04392 | 2025-10-27 04:59:00 | NPP-375D | CODÓ | MARANHÃO | Brasil | 2103307 | 21 | 33 | nan | nan | nan | Cerrado | 2.5 |
| d6f8c5a5-9ac8-340b-a7b4-c0add97e8550 | -3.76033 | -47.60981 | 2025-10-27 04:59:00 | NPP-375D | ULIANÓPOLIS | PARÁ | Brasil | 1508126 | 15 | 33 | nan | nan | nan | Amazônia | 0.7 |
| 0491e1ae-7bc6-3d7f-993e-a8307fbc13ff | -3.05059 | -53.02013 | 2025-10-27 04:59:00 | NPP-375D | MEDICILÂNDIA | PARÁ | Brasil | 1504455 | 15 | 33 | nan | nan | nan | Amazônia | 2.9 |
| 637f359e-3637-3035-93f4-b38116b51ee7 | -3.57445 | -44.52915 | 2025-10-27 04:59:00 | NPP-375D | MIRANDA DO NORTE | MARANHÃO | Brasil | 2106755 | 21 | 33 | nan | nan | nan | Cerrado | 1.8 |
| 19fbbca0-4487-3fba-89cb-f8399692565f | -4.47536 | -43.43003 | 2025-10-27 04:59:00 | NPP-375D | ALDEIAS ALTAS | MARANHÃO | Brasil | 2100303 | 21 | 33 | nan | nan | nan | Cerrado | 8.4 |
| 5af0104f-93d1-301e-b276-aa8dbc4e8922 | 1.60609 | -55.74009 | 2025-10-27 04:59:00 | NPP-375D | ÓBIDOS | PARÁ | Brasil | 1505106 | 15 | 33 | nan | nan | nan | Amazônia | 0.9 |
| 97383210-d538-37a5-90a7-b0683fac08a8 | -4.44621 | -43.42567 | 2025-10-27 04:59:00 | NPP-375D | ALDEIAS ALTAS | MARANHÃO | Brasil | 2100303 | 21 | 33 | nan | nan | nan | Cerrado | 1.2 |
| 34a76263-1fbc-348b-a7b0-b981112d71fe | -4.44001 | -45.97662 | 2025-10-27 04:59:00 | NPP-375D | SANTA LUZIA | MARANHÃO | Brasil | 2110005 | 21 | 33 | nan | nan | nan | Amazônia | 3.5 |
| 649adb83-8083-3b50-b93f-834657590351 | -4.46433 | -43.42405 | 2025-10-27 04:59:00 | NPP-375D | ALDEIAS ALTAS | MARANHÃO | Brasil | 2100303 | 21 | 33 | nan | nan | nan | Cerrado | 1.6 |
| 99f07ea7-9b7e-3bb8-89fb-aacbc7ae0208 | -4.20837 | -48.35826 | 2025-10-27 04:59:00 | NPP-375D | RONDON DO PARÁ | PARÁ | Brasil | 1506187 | 15 | 33 | nan | nan | nan | Amazônia | 1.9 |
| 26be16cd-8b27-3918-a43b-a505b440374c | -3.39383 | -50.39957 | 2025-10-27 04:59:00 | NPP-375D | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 2.5 |
| c0cffe88-689e-34fb-bcdb-067c59fc7092 | -3.66842 | -52.51058 | 2025-10-27 04:59:00 | NPP-375D | BRASIL NOVO | PARÁ | Brasil | 1501725 | 15 | 33 | nan | nan | nan | Amazônia | 0.7 |
| 4668e826-4f8a-3b7f-9060-05ee61da61a6 | -3.61032 | -43.56358 | 2025-10-27 04:59:00 | NPP-375D | CHAPADINHA | MARANHÃO | Brasil | 2103208 | 21 | 33 | nan | nan | nan | Cerrado | 1.2 |
| d555e0a6-b5cf-3d00-9b55-8b7237f7342e | -4.15916 | -51.08574 | 2025-10-27 04:59:00 | NPP-375D | PACAJÁ | PARÁ | Brasil | 1505486 | 15 | 33 | nan | nan | nan | Amazônia | 2.3 |
| 7f5c5e00-a09f-3c9e-8bfb-4ccb734c6f46 | -2.32158 | -48.57967 | 2025-10-27 04:59:00 | NPP-375D | ACARÁ | PARÁ | Brasil | 1500206 | 15 | 33 | nan | nan | nan | Amazônia | 3.8 |
| 1c45e91c-a054-3a6a-8bd7-7dbfd0ecaaa7 | 1.62396 | -55.71138 | 2025-10-27 04:59:00 | NPP-375D | ÓBIDOS | PARÁ | Brasil | 1505106 | 15 | 33 | nan | nan | nan | Amazônia | 1.3 |
| dc92b26c-8882-3d66-84e8-037577e4c431 | -3.10058 | -49.45402 | 2025-10-27 04:59:00 | NPP-375D | MOJU | PARÁ | Brasil | 1504703 | 15 | 33 | nan | nan | nan | Amazônia | 1.2 |
| b2f3938f-83e6-3973-a27d-c85b3a3ea073 | -3.11556 | -51.21529 | 2025-10-27 04:59:00 | NPP-375D | ANAPU | PARÁ | Brasil | 1500859 | 15 | 33 | nan | nan | nan | Amazônia | 1.3 |
| d88e07ad-2d3a-3006-9ab0-092c4cd96285 | -3.83787 | -50.20059 | 2025-10-27 04:59:00 | NPP-375D | PACAJÁ | PARÁ | Brasil | 1505486 | 15 | 33 | nan | nan | nan | Amazônia | 1.0 |
| 93605973-27f5-30ba-b083-f46b75d53d85 | -4.45733 | -45.45194 | 2025-10-27 04:59:00 | NPP-375D | PAULO RAMOS | MARANHÃO | Brasil | 2108108 | 21 | 33 | nan | nan | nan | Amazônia | 0.8 |
| 5bbd3469-f660-3bbb-af24-3326d3389b2f | -3.12371 | -51.20873 | 2025-10-27 04:59:00 | NPP-375D | ANAPU | PARÁ | Brasil | 1500859 | 15 | 33 | nan | nan | nan | Amazônia | 1.5 |
| c6d89fa7-27c7-3593-85ae-32e4b2aa326a | -3.07716 | -51.27215 | 2025-10-27 04:59:00 | NPP-375D | ANAPU | PARÁ | Brasil | 1500859 | 15 | 33 | nan | nan | nan | Amazônia | 1.3 |
| aa7a6c09-e63f-3f69-85d8-1e75c12307e4 | -4.35212 | -50.70394 | 2025-10-27 04:59:00 | NPP-375D | NOVO REPARTIMENTO | PARÁ | Brasil | 1505064 | 15 | 33 | nan | nan | nan | Amazônia | 0.8 |
| ff90bc39-0b87-333a-9d0c-2c208e658d3c | -4.87133 | -48.52637 | 2025-10-27 04:59:00 | NPP-375D | ABEL FIGUEIREDO | PARÁ | Brasil | 1500131 | 15 | 33 | nan | nan | nan | Amazônia | 1.6 |
| b335f41d-a047-31c1-b015-1b2b980e68f6 | -3.47131 | -49.9735 | 2025-10-27 04:59:00 | NPP-375D | PACAJÁ | PARÁ | Brasil | 1505486 | 15 | 33 | nan | nan | nan | Amazônia | 2.4 |
| 9db86759-cf25-367b-b917-99a8420a217d | -2.01212 | -56.90071 | 2025-10-27 04:59:00 | NPP-375D | NHAMUNDÁ | AMAZONAS | Brasil | 1303007 | 13 | 33 | nan | nan | nan | Amazônia | 0.8 |
| a12e8aa1-e74b-3c08-ab2a-4c083f158e97 | -4.26066 | -50.50357 | 2025-10-27 04:59:00 | NPP-375D | NOVO REPARTIMENTO | PARÁ | Brasil | 1505064 | 15 | 33 | nan | nan | nan | Amazônia | 1.1 |
| 6771a9c3-6db0-34cd-9d7e-a90e71ebc0c1 | -3.80525 | -51.85566 | 2025-10-27 04:59:00 | NPP-375D | SENADOR JOSÉ PORFÍRIO | PARÁ | Brasil | 1507805 | 15 | 33 | nan | nan | nan | Amazônia | 0.9 |
| a12d4742-4f06-30f7-9b6a-ea21d64a9b30 | -3.10206 | -51.27967 | 2025-10-27 04:59:00 | NPP-375D | ANAPU | PARÁ | Brasil | 1500859 | 15 | 33 | nan | nan | nan | Amazônia | 0.7 |
| e21a841e-8d54-31ba-afd7-3a046ea2729d | -4.45026 | -43.43869 | 2025-10-27 04:59:00 | NPP-375D | ALDEIAS ALTAS | MARANHÃO | Brasil | 2100303 | 21 | 33 | nan | nan | nan | Cerrado | 0.9 |
| 3c05c2cf-4005-3963-ad62-54a999074589 | -3.27215 | -51.62368 | 2025-10-27 04:59:00 | NPP-375D | ANAPU | PARÁ | Brasil | 1500859 | 15 | 33 | nan | nan | nan | Amazônia | 1.0 |
| 281a0d7b-d948-34cd-aefe-1c8e42f60da6 | -3.10202 | -49.4447 | 2025-10-27 04:59:00 | NPP-375D | MOJU | PARÁ | Brasil | 1504703 | 15 | 33 | nan | nan | nan | Amazônia | 1.2 |
| 1e024322-0e79-3a9b-a07d-0a91914a3086 | -4.65853 | -46.39922 | 2025-10-27 04:59:00 | NPP-375D | BURITICUPU | MARANHÃO | Brasil | 2102325 | 21 | 33 | nan | nan | nan | Amazônia | 0.9 |
| aafafb19-2d69-330a-8c91-d1ef87bed2d3 | -1.34983 | -53.48565 | 2025-10-27 04:59:00 | NPP-375D | ALMEIRIM | PARÁ | Brasil | 1500503 | 15 | 33 | nan | nan | nan | Amazônia | 1.0 |
| 9902532a-5fbc-3cfd-8f2a-5f9da06eca5a | -3.13635 | -50.16175 | 2025-10-27 04:59:00 | NPP-375D | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 1.5 |
| 57bd7d60-7068-300b-b22c-aad8cfbdbddf | -4.48004 | -48.67536 | 2025-10-27 04:59:00 | NPP-375D | RONDON DO PARÁ | PARÁ | Brasil | 1506187 | 15 | 33 | nan | nan | nan | Amazônia | 1.0 |
| 0c48bc71-461a-3c8c-bf03-e7d637593b90 | -3.8301 | -51.69615 | 2025-10-27 04:59:00 | NPP-375D | SENADOR JOSÉ PORFÍRIO | PARÁ | Brasil | 1507805 | 15 | 33 | nan | nan | nan | Amazônia | 0.7 |
| 041298cb-3650-35a8-82a0-734061566a55 | 0.43909 | -50.78718 | 2025-10-27 04:59:00 | NPP-375D | MACAPÁ | AMAPÁ | Brasil | 1600303 | 16 | 33 | nan | nan | nan | Amazônia | 0.3 |
| 08689971-90fd-3eb3-9d02-1b86195bfe84 | -4.86664 | -48.52934 | 2025-10-27 04:59:00 | NPP-375D | ABEL FIGUEIREDO | PARÁ | Brasil | 1500131 | 15 | 33 | nan | nan | nan | Amazônia | 1.1 |
| c8f26427-f20b-3131-b2dd-dc28e2618e90 | -1.35586 | -49.16831 | 2025-10-27 04:59:00 | NPP-375D | MUANÁ | PARÁ | Brasil | 1504901 | 15 | 33 | nan | nan | nan | Amazônia | 1.2 |
| 69d3dbf8-a4ae-3b62-a0c1-72ab34576c4d | -2.97765 | -51.03361 | 2025-10-27 04:59:00 | NPP-375D | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 1.8 |
| 36aafa75-bdeb-396e-8676-565659210917 | -4.32241 | -48.0867 | 2025-10-27 04:59:00 | NPP-375D | RONDON DO PARÁ | PARÁ | Brasil | 1506187 | 15 | 33 | nan | nan | nan | Amazônia | 1.8 |
| c5e11754-81b2-388a-9592-9c08d3227d98 | 1.1425 | -51.06044 | 2025-10-27 04:59:00 | NPP-375D | TARTARUGALZINHO | AMAPÁ | Brasil | 1600709 | 16 | 33 | nan | nan | nan | Amazônia | 0.5 |
| ce12e45b-139a-34d3-9cfe-f1178939f4b5 | -4.12835 | -48.81052 | 2025-10-27 04:59:00 | NPP-375D | GOIANÉSIA DO PARÁ | PARÁ | Brasil | 1503093 | 15 | 33 | nan | nan | nan | Amazônia | 1.0 |
| 391f432f-adfb-3806-be99-36f45c0a3f3f | 2.06934 | -55.70178 | 2025-10-27 04:59:00 | NPP-375D | ÓBIDOS | PARÁ | Brasil | 1505106 | 15 | 33 | nan | nan | nan | Amazônia | 0.5 |
| 8e9fedd6-1123-36b7-9f25-a231256d8eef | 0.80997 | -50.8362 | 2025-10-27 04:59:00 | NPP-375D | MACAPÁ | AMAPÁ | Brasil | 1600303 | 16 | 33 | nan | nan | nan | Amazônia | 2.2 |
| 8ed7f98f-a75f-3155-9e09-cda4c5c91d9f | -3.13483 | -53.00483 | 2025-10-27 04:59:00 | NPP-375D | MEDICILÂNDIA | PARÁ | Brasil | 1504455 | 15 | 33 | nan | nan | nan | Amazônia | 0.7 |
| 4a1d2fed-6710-3fd8-8fbc-21f7c1195b21 | -4.45645 | -45.45795 | 2025-10-27 04:59:00 | NPP-375D | PAULO RAMOS | MARANHÃO | Brasil | 2108108 | 21 | 33 | nan | nan | nan | Amazônia | 5.0 |
| ef44faa5-57f7-3bbe-b41b-4cfe9dd20ab3 | -3.05908 | -54.61527 | 2025-10-27 04:59:00 | NPP-375D | MOJUÍ DOS CAMPOS | PARÁ | Brasil | 1504752 | 15 | 33 | nan | nan | nan | Amazônia | 1.2 |
| 908251b4-5d7b-32f0-bdc6-9da8e3a1bbc2 | -3.98972 | -51.03571 | 2025-10-27 04:59:00 | NPP-375D | PACAJÁ | PARÁ | Brasil | 1505486 | 15 | 33 | nan | nan | nan | Amazônia | 3.3 |
| 3183500a-f5da-36f0-a2d9-d4d72c93f114 | -3.23802 | -48.77319 | 2025-10-27 04:59:00 | NPP-375D | TAILÂNDIA | PARÁ | Brasil | 1507953 | 15 | 33 | nan | nan | nan | Amazônia | 1.8 |
| 05ec92dc-34e0-3614-9883-7bf4602df102 | 1.14364 | -51.06764 | 2025-10-27 04:59:00 | NPP-375D | TARTARUGALZINHO | AMAPÁ | Brasil | 1600709 | 16 | 33 | nan | nan | nan | Amazônia | 1.1 |
| e9c3db03-89d5-3554-a36d-21c1d2dd3e1d | -1.69023 | -55.6713 | 2025-10-27 04:59:00 | NPP-375D | ÓBIDOS | PARÁ | Brasil | 1505106 | 15 | 33 | nan | nan | nan | Amazônia | 2.3 |
| 3d56066d-c657-3e64-a447-e73b188f59b0 | 1.24654 | -50.90374 | 2025-10-27 04:59:00 | NPP-375D | TARTARUGALZINHO | AMAPÁ | Brasil | 1600709 | 16 | 33 | nan | nan | nan | Amazônia | 1.8 |
| 735af478-97f6-38f8-9b07-0e6b7b608965 | -3.42715 | -52.62538 | 2025-10-27 04:59:00 | NPP-375D | BRASIL NOVO | PARÁ | Brasil | 1501725 | 15 | 33 | nan | nan | nan | Amazônia | 0.9 |
| f4e3eb0f-2d9d-3277-916b-ccecf180f77a | -3.57224 | -44.52895 | 2025-10-27 04:59:00 | NPP-375D | MIRANDA DO NORTE | MARANHÃO | Brasil | 2106755 | 21 | 33 | nan | nan | nan | Cerrado | 3.8 |
| bf09cdc6-3c57-3c6f-af69-27a86ea019ab | -4.95191 | -44.87964 | 2025-10-27 04:59:00 | NPP-375D | JOSELÂNDIA | MARANHÃO | Brasil | 2105609 | 21 | 33 | nan | nan | nan | Cerrado | 0.7 |
| a2fcd56b-0620-3d64-86ab-2596ae3958e5 | -2.11116 | -52.77753 | 2025-10-27 04:59:00 | NPP-375D | PORTO DE MOZ | PARÁ | Brasil | 1505908 | 15 | 33 | nan | nan | nan | Amazônia | 1.0 |
| 5679309c-9477-3cec-b822-a8c64aed913c | -4.45182 | -45.45406 | 2025-10-27 04:59:00 | NPP-375D | PAULO RAMOS | MARANHÃO | Brasil | 2108108 | 21 | 33 | nan | nan | nan | Amazônia | 5.0 |
| b3d6d3e1-8409-3a1d-a285-f1c052da3d7d | -2.90394 | -53.13572 | 2025-10-27 04:59:00 | NPP-375D | MEDICILÂNDIA | PARÁ | Brasil | 1504455 | 15 | 33 | nan | nan | nan | Amazônia | 2.0 |
| 1d959a00-9338-3703-9d36-916874eb0b45 | -3.90075 | -52.26842 | 2025-10-27 04:59:00 | NPP-375D | SENADOR JOSÉ PORFÍRIO | PARÁ | Brasil | 1507805 | 15 | 33 | nan | nan | nan | Amazônia | 0.9 |
| 939c268c-63a3-3db4-bae7-30f54b6f34db | -4.43018 | -45.9752 | 2025-10-27 04:59:00 | NPP-375D | SANTA LUZIA | MARANHÃO | Brasil | 2110005 | 21 | 33 | nan | nan | nan | Amazônia | 2.2 |


[Clique aqui para ver as próximas entradas](README55.md)
