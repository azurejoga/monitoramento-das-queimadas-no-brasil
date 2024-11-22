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

## Dados Diários - Página 47

| ID | Latitude | Longitude | Data/Hora GMT | Satélite | Município | Estado | País | Município ID | Estado ID | País ID | Dias sem Chuva | Precipitação | Risco de Fogo | Bioma | FRP |
|----|----------|-----------|---------------|----------|-----------|--------|------|--------------|-----------|---------|----------------|--------------|----------------|-------|-----|
| 1db77653-ad81-37d4-a1f2-a910e587efae | -2.18695 | -50.46699 | 2024-11-22 04:36:00 | NOAA-20 | BAGRE | PARÁ | Brasil | 1501105 | 15 | 33 | nan | nan | nan | Amazônia | 1.6 |
| 7ea8b35a-bd1f-3285-bbc5-8c7cee8125f0 | -4.23214 | -40.38708 | 2024-11-22 04:36:00 | NOAA-20 | SANTA QUITÉRIA | CEARÁ | Brasil | 2312205 | 23 | 33 | nan | nan | nan | Caatinga | 1.1 |
| 42e8c490-9312-3860-8309-7557a7a124a9 | -4.0086 | -49.92191 | 2024-11-22 04:36:00 | NOAA-20 | TUCURUÍ | PARÁ | Brasil | 1508100 | 15 | 33 | nan | nan | nan | Amazônia | 1.4 |
| 005f8b34-6814-33ac-9e0f-b67399dcbd1a | -3.23837 | -54.24983 | 2024-11-22 04:36:00 | NOAA-20 | MOJUÍ DOS CAMPOS | PARÁ | Brasil | 1504752 | 15 | 33 | nan | nan | nan | Amazônia | 12.9 |
| 508930d2-7c7d-35b3-af1f-2462b87cc494 | -5.10471 | -43.16498 | 2024-11-22 04:36:00 | NOAA-20 | CAXIAS | MARANHÃO | Brasil | 2103000 | 21 | 33 | nan | nan | nan | Cerrado | 7.4 |
| 2f31ad11-808d-3ac8-97e0-343a920c8c9b | -1.27419 | -52.97979 | 2024-11-22 04:36:00 | NOAA-20 | ALMEIRIM | PARÁ | Brasil | 1500503 | 15 | 33 | nan | nan | nan | Amazônia | 2.5 |
| cd741092-124b-3274-bc31-f115bc3f370f | -4.01194 | -49.92243 | 2024-11-22 04:36:00 | NOAA-20 | TUCURUÍ | PARÁ | Brasil | 1508100 | 15 | 33 | nan | nan | nan | Amazônia | 1.9 |
| 55981706-b0f0-3206-b8d2-6a68a0313577 | -2.32173 | -48.57465 | 2024-11-22 04:36:00 | NOAA-20 | ACARÁ | PARÁ | Brasil | 1500206 | 15 | 33 | nan | nan | nan | Amazônia | 1.3 |
| 4eb6e1d4-fdb1-306f-bf18-ef8ea51ec194 | -2.41147 | -46.06755 | 2024-11-22 04:36:00 | NOAA-20 | CENTRO DO GUILHERME | MARANHÃO | Brasil | 2103158 | 21 | 33 | nan | nan | nan | Amazônia | 1.3 |
| 3accb8e6-acd4-3c85-87bd-c8655e5e1643 | -3.8325 | -52.25866 | 2024-11-22 04:36:00 | NOAA-20 | SENADOR JOSÉ PORFÍRIO | PARÁ | Brasil | 1507805 | 15 | 33 | nan | nan | nan | Amazônia | 7.4 |
| 76fe7b38-2fc4-3322-9650-686e1f329ce0 | -1.14184 | -53.40369 | 2024-11-22 04:36:00 | NOAA-20 | ALMEIRIM | PARÁ | Brasil | 1500503 | 15 | 33 | nan | nan | nan | Amazônia | 1.8 |
| be9f2815-ad77-3cc1-9086-44450feb0347 | -2.82924 | -54.04987 | 2024-11-22 04:36:00 | NOAA-20 | PRAINHA | PARÁ | Brasil | 1506005 | 15 | 33 | nan | nan | nan | Amazônia | 0.8 |
| 36c636a3-0d17-354d-8f52-afe29fa0c76f | -0.84865 | -47.52734 | 2024-11-22 04:36:00 | NOAA-20 | MARACANÃ | PARÁ | Brasil | 1504307 | 15 | 33 | nan | nan | nan | Amazônia | 0.8 |
| f33f5e9b-27a3-3848-b0b1-0b05e2dbe78c | -2.22779 | -48.37366 | 2024-11-22 04:36:00 | NOAA-20 | ACARÁ | PARÁ | Brasil | 1500206 | 15 | 33 | nan | nan | nan | Amazônia | 1.3 |
| db0e06d6-9617-3e92-bada-676d33d6421e | -3.51729 | -54.68581 | 2024-11-22 04:36:00 | NOAA-20 | PLACAS | PARÁ | Brasil | 1505650 | 15 | 33 | nan | nan | nan | Amazônia | 2.0 |
| 093b8ecf-7b73-3028-9cee-406639cacdcf | -2.69438 | -46.08924 | 2024-11-22 04:36:00 | NOAA-20 | CENTRO NOVO DO MARANHÃO | MARANHÃO | Brasil | 2103174 | 21 | 33 | nan | nan | nan | Amazônia | 1.6 |
| 9f639f57-398a-3ffe-8d2a-ef1a7372767a | -1.14996 | -53.59173 | 2024-11-22 04:36:00 | NOAA-20 | ALMEIRIM | PARÁ | Brasil | 1500503 | 15 | 33 | nan | nan | nan | Amazônia | 1.8 |
| a583ad3e-0780-34d8-94d3-23dfc8fcd168 | -3.57986 | -54.51712 | 2024-11-22 04:36:00 | NOAA-20 | PLACAS | PARÁ | Brasil | 1505650 | 15 | 33 | nan | nan | nan | Amazônia | 3.6 |
| 9dc5a576-6964-3610-b6b0-3dfd0ee2ad7d | -0.26711 | -51.56033 | 2024-11-22 04:36:00 | NOAA-20 | MAZAGÃO | AMAPÁ | Brasil | 1600402 | 16 | 33 | nan | nan | nan | Amazônia | 1.3 |
| 1e8520cb-7347-3a24-a8c7-5fe5172407c2 | -2.15891 | -53.79268 | 2024-11-22 04:36:00 | NOAA-20 | PRAINHA | PARÁ | Brasil | 1506005 | 15 | 33 | nan | nan | nan | Amazônia | 3.0 |
| 99c99b0e-7df2-346a-b85a-cd1dde211fb4 | -4.59765 | -46.34491 | 2024-11-22 04:36:00 | NOAA-20 | BURITICUPU | MARANHÃO | Brasil | 2102325 | 21 | 33 | nan | nan | nan | Amazônia | 0.7 |
| 30f16acb-42e8-3b08-837d-b3dc4f0e9af3 | -2.15892 | -50.46639 | 2024-11-22 04:36:00 | NOAA-20 | BAGRE | PARÁ | Brasil | 1501105 | 15 | 33 | nan | nan | nan | Amazônia | 2.2 |
| a2ae535e-1d42-36f2-99ac-1ba56a88b290 | 0.61459 | -51.77434 | 2024-11-22 04:36:00 | NOAA-20 | PORTO GRANDE | AMAPÁ | Brasil | 1600535 | 16 | 33 | nan | nan | nan | Amazônia | 1.6 |
| eb4547dd-876a-3f73-b23e-9f0135a5c891 | -3.5027 | -53.80933 | 2024-11-22 04:36:00 | NOAA-20 | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | 5.5 |
| d2dd280b-f35a-3cc8-a303-e956eca2cbac | -2.53454 | -46.37785 | 2024-11-22 04:36:00 | NOAA-20 | CENTRO NOVO DO MARANHÃO | MARANHÃO | Brasil | 2103174 | 21 | 33 | nan | nan | nan | Amazônia | 0.8 |
| 035b700f-8c3d-3fe7-88cd-5113c15f9aa4 | -2.75053 | -51.8802 | 2024-11-22 04:36:00 | NOAA-20 | SENADOR JOSÉ PORFÍRIO | PARÁ | Brasil | 1507805 | 15 | 33 | nan | nan | nan | Amazônia | 4.3 |
| 65779083-9940-30f0-9fb7-0a1b7d8c40d5 | -1.96029 | -48.38737 | 2024-11-22 04:36:00 | NOAA-20 | ACARÁ | PARÁ | Brasil | 1500206 | 15 | 33 | nan | nan | nan | Amazônia | 1.3 |
| 7ac2aa78-09be-3af2-b882-439f7d3a074f | -1.34163 | -52.14758 | 2024-11-22 04:36:00 | NOAA-20 | ALMEIRIM | PARÁ | Brasil | 1500503 | 15 | 33 | nan | nan | nan | Amazônia | 0.7 |
| 9e90b0eb-de2c-3c01-a5fc-3cf827c17951 | -2.68703 | -54.99183 | 2024-11-22 04:36:00 | NOAA-20 | BELTERRA | PARÁ | Brasil | 1501451 | 15 | 33 | nan | nan | nan | Amazônia | 3.1 |
| ea981522-41c8-360b-b00a-48d4d9091761 | -2.69687 | -46.23523 | 2024-11-22 04:36:00 | NOAA-20 | CENTRO NOVO DO MARANHÃO | MARANHÃO | Brasil | 2103174 | 21 | 33 | nan | nan | nan | Amazônia | 2.2 |
| c9e959fd-ba4f-354f-b1ad-ccd0e3841051 | -4.21159 | -50.69925 | 2024-11-22 04:36:00 | NOAA-20 | PACAJÁ | PARÁ | Brasil | 1505486 | 15 | 33 | nan | nan | nan | Amazônia | 1.7 |
| af19f94b-8798-3f05-8472-ce247360ecc3 | -3.95614 | -46.72363 | 2024-11-22 04:36:00 | NOAA-20 | BOM JARDIM | MARANHÃO | Brasil | 2102002 | 21 | 33 | nan | nan | nan | Amazônia | 2.0 |
| 91d71600-c019-3d80-b5c3-d907865d586d | -2.10213 | -50.35938 | 2024-11-22 04:36:00 | NOAA-20 | BAGRE | PARÁ | Brasil | 1501105 | 15 | 33 | nan | nan | nan | Amazônia | 2.6 |
| 48ae957f-abe0-3484-9a8b-2c1325fed577 | -2.67965 | -46.16207 | 2024-11-22 04:36:00 | NOAA-20 | CENTRO DO GUILHERME | MARANHÃO | Brasil | 2103158 | 21 | 33 | nan | nan | nan | Amazônia | 1.4 |
| bbb86f6e-f388-3775-b1fe-8842374334fb | -2.50836 | -54.15253 | 2024-11-22 04:36:00 | NOAA-20 | PRAINHA | PARÁ | Brasil | 1506005 | 15 | 33 | nan | nan | nan | Amazônia | 6.1 |
| 7282964f-44aa-36c1-ab1f-c3c2e78722ad | -5.95563 | -48.05878 | 2024-11-22 04:36:00 | NOAA-20 | SÃO BENTO DO TOCANTINS | TOCANTINS | Brasil | 1720101 | 17 | 33 | nan | nan | nan | Cerrado | 2.8 |
| e1a027a8-582d-364d-8a3a-04dd5a360a8a | -2.54764 | -46.20955 | 2024-11-22 04:36:00 | NOAA-20 | CENTRO DO GUILHERME | MARANHÃO | Brasil | 2103158 | 21 | 33 | nan | nan | nan | Amazônia | 1.1 |
| eb319960-7f9a-3f8c-a992-0f61e5c28061 | -5.15998 | -44.85642 | 2024-11-22 04:36:00 | NOAA-20 | BARRA DO CORDA | MARANHÃO | Brasil | 2101608 | 21 | 33 | nan | nan | nan | Cerrado | 1.4 |
| 3f07d415-aa95-35d7-b505-c1f00aa44a2d | -1.7616 | -52.66961 | 2024-11-22 04:36:00 | NOAA-20 | PORTO DE MOZ | PARÁ | Brasil | 1505908 | 15 | 33 | nan | nan | nan | Amazônia | 1.7 |
| cf1ac397-97ee-37ab-bf31-aeee5f07ad57 | -1.27732 | -51.82196 | 2024-11-22 04:36:00 | NOAA-20 | GURUPÁ | PARÁ | Brasil | 1503101 | 15 | 33 | nan | nan | nan | Amazônia | 2.0 |
| 1f894afe-6086-322c-8dd0-ff2a314f05f8 | -1.78396 | -47.10662 | 2024-11-22 04:36:00 | NOAA-20 | CAPITÃO POÇO | PARÁ | Brasil | 1502301 | 15 | 33 | nan | nan | nan | Amazônia | 2.8 |
| 31631ce5-b5b3-3711-8ed6-b3ef8756058d | -2.67148 | -51.88491 | 2024-11-22 04:36:00 | NOAA-20 | SENADOR JOSÉ PORFÍRIO | PARÁ | Brasil | 1507805 | 15 | 33 | nan | nan | nan | Amazônia | 1.6 |
| 9c181498-3668-3bde-92c0-90575dd6e688 | -0.95748 | -47.89292 | 2024-11-22 04:36:00 | NOAA-20 | TERRA ALTA | PARÁ | Brasil | 1507961 | 15 | 33 | nan | nan | nan | Amazônia | 0.8 |
| 332e3a41-4259-3dbf-96c8-70a295a2cf54 | -2.1601 | -50.45895 | 2024-11-22 04:36:00 | NOAA-20 | BAGRE | PARÁ | Brasil | 1501105 | 15 | 33 | nan | nan | nan | Amazônia | 1.3 |
| 4fdda3a6-d2b9-391e-8640-abd8ad7d5056 | -2.22873 | -50.51122 | 2024-11-22 04:36:00 | NOAA-20 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 1.9 |
| 5749335d-8f8b-3672-9069-cf1c61a72236 | -5.07119 | -50.58809 | 2024-11-22 04:36:00 | NOAA-20 | NOVO REPARTIMENTO | PARÁ | Brasil | 1505064 | 15 | 33 | nan | nan | nan | Amazônia | 0.5 |
| 2b1aba70-0604-3604-9486-ec85798500f1 | -2.55646 | -47.29439 | 2024-11-22 04:36:00 | NOAA-20 | CAPITÃO POÇO | PARÁ | Brasil | 1502301 | 15 | 33 | nan | nan | nan | Amazônia | 0.6 |
| 9282c13f-19aa-3ae1-a3bb-e0fef7dc9576 | -2.9196 | -46.83397 | 2024-11-22 04:36:00 | NOAA-20 | PARAGOMINAS | PARÁ | Brasil | 1505502 | 15 | 33 | nan | nan | nan | Amazônia | 1.6 |
| 1e67d70a-4101-3b96-9a64-418e99145213 | -3.32488 | -53.19017 | 2024-11-22 04:36:00 | NOAA-20 | MEDICILÂNDIA | PARÁ | Brasil | 1504455 | 15 | 33 | nan | nan | nan | Amazônia | 0.8 |
| eb4c3fb6-8807-38bb-9f40-30e36496f2c9 | -2.01666 | -51.18058 | 2024-11-22 04:36:00 | NOAA-20 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 0.9 |
| 03b72be4-bca7-31a2-a896-c0372d4a4c24 | -3.39411 | -54.27388 | 2024-11-22 04:36:00 | NOAA-20 | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | 1.7 |
| 07808d64-fb9f-3db1-a00b-e9d1d020c7ad | -0.81301 | -51.61083 | 2024-11-22 04:36:00 | NOAA-20 | GURUPÁ | PARÁ | Brasil | 1503101 | 15 | 33 | nan | nan | nan | Amazônia | 1.5 |
| 09741acb-5422-3678-89bf-29e8ddb01180 | -2.50033 | -48.99328 | 2024-11-22 04:36:00 | NOAA-20 | MOJU | PARÁ | Brasil | 1504703 | 15 | 33 | nan | nan | nan | Amazônia | 1.1 |
| 6cdd8125-6635-36de-a6af-9b87714f2a79 | -2.79509 | -45.94889 | 2024-11-22 04:36:00 | NOAA-20 | NOVA OLINDA DO MARANHÃO | MARANHÃO | Brasil | 2107357 | 21 | 33 | nan | nan | nan | Amazônia | 1.6 |
| ca7b1e9a-3620-3328-9307-06492dfc9a41 | -2.42534 | -46.51817 | 2024-11-22 04:36:00 | NOAA-20 | NOVA ESPERANÇA DO PIRIÁ | PARÁ | Brasil | 1504950 | 15 | 33 | nan | nan | nan | Amazônia | 1.0 |
| e8b2ac59-c120-3f53-beec-f3962b13e4aa | -1.51577 | -51.18871 | 2024-11-22 04:36:00 | NOAA-20 | MELGAÇO | PARÁ | Brasil | 1504505 | 15 | 33 | nan | nan | nan | Amazônia | 2.3 |
| c9176df4-7e35-31fd-97a9-51e8acdbe981 | -2.07195 | -48.88735 | 2024-11-22 04:36:00 | NOAA-20 | MOJU | PARÁ | Brasil | 1504703 | 15 | 33 | nan | nan | nan | Amazônia | 0.8 |
| 13d6c316-8047-3033-a0a0-a34d608833c0 | -2.69787 | -46.08979 | 2024-11-22 04:36:00 | NOAA-20 | CENTRO NOVO DO MARANHÃO | MARANHÃO | Brasil | 2103174 | 21 | 33 | nan | nan | nan | Amazônia | 1.6 |
| 91453281-d932-3599-ac14-1b89ea0cb16c | -3.22743 | -54.25623 | 2024-11-22 04:36:00 | NOAA-20 | MOJUÍ DOS CAMPOS | PARÁ | Brasil | 1504752 | 15 | 33 | nan | nan | nan | Amazônia | 6.0 |
| d26db667-6678-3974-a98e-0bd387cb6f43 | -1.21522 | -51.74242 | 2024-11-22 04:36:00 | NOAA-20 | GURUPÁ | PARÁ | Brasil | 1503101 | 15 | 33 | nan | nan | nan | Amazônia | 2.4 |
| 5f3afd3d-437a-381b-8a8e-e773b0d02e08 | -2.38471 | -50.39118 | 2024-11-22 04:36:00 | NOAA-20 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 2.0 |
| 470d8665-2d7a-378e-bff7-0980b7f64002 | -3.84185 | -51.14407 | 2024-11-22 04:36:00 | NOAA-20 | PACAJÁ | PARÁ | Brasil | 1505486 | 15 | 33 | nan | nan | nan | Amazônia | 2.7 |
| b8383bbf-9571-3ed1-89eb-e4bfd0743322 | -5.7774 | -46.43191 | 2024-11-22 04:36:00 | NOAA-20 | GRAJAÚ | MARANHÃO | Brasil | 2104800 | 21 | 33 | nan | nan | nan | Cerrado | 0.8 |
| d294c9f8-cf09-3f3d-a089-1cbdb0a523a0 | -2.93022 | -48.05346 | 2024-11-22 04:36:00 | NOAA-20 | IPIXUNA DO PARÁ | PARÁ | Brasil | 1503457 | 15 | 33 | nan | nan | nan | Amazônia | 1.8 |
| 36c9841b-22bc-3f0a-a315-6a8e995e7a9a | -3.34149 | -53.33512 | 2024-11-22 04:36:00 | NOAA-20 | MEDICILÂNDIA | PARÁ | Brasil | 1504455 | 15 | 33 | nan | nan | nan | Amazônia | 5.7 |
| 27c6e65f-1795-31e4-aae3-e0234e148ca3 | -1.23789 | -51.79041 | 2024-11-22 04:36:00 | NOAA-20 | GURUPÁ | PARÁ | Brasil | 1503101 | 15 | 33 | nan | nan | nan | Amazônia | 1.3 |
| 42353cfb-dcb7-3216-8c5a-c7ff339a4fa4 | -2.2108 | -49.87698 | 2024-11-22 04:36:00 | NOAA-20 | OEIRAS DO PARÁ | PARÁ | Brasil | 1505205 | 15 | 33 | nan | nan | nan | Amazônia | 0.7 |
| 859cf0de-5e0b-3530-bcd4-6a03bbc798da | -4.54142 | -42.98069 | 2024-11-22 04:36:00 | NOAA-20 | CAXIAS | MARANHÃO | Brasil | 2103000 | 21 | 33 | nan | nan | nan | Cerrado | 1.1 |
| fa74e0f4-8328-3c9c-ba10-15edfa754d89 | -3.02593 | -51.52695 | 2024-11-22 04:36:00 | NOAA-20 | ANAPU | PARÁ | Brasil | 1500859 | 15 | 33 | nan | nan | nan | Amazônia | 1.6 |
| 631025df-afe5-3960-98d3-024af566fe9f | -4.13348 | -46.70719 | 2024-11-22 04:36:00 | NOAA-20 | BOM JARDIM | MARANHÃO | Brasil | 2102002 | 21 | 33 | nan | nan | nan | Amazônia | 0.9 |
| bb9735bb-5fc1-3813-b84b-f8720e6056e2 | -2.15951 | -53.78899 | 2024-11-22 04:36:00 | NOAA-20 | PRAINHA | PARÁ | Brasil | 1506005 | 15 | 33 | nan | nan | nan | Amazônia | 3.0 |
| 19356df3-a370-3d41-a211-98438daa9965 | -4.24645 | -49.08101 | 2024-11-22 04:36:00 | NOAA-20 | GOIANÉSIA DO PARÁ | PARÁ | Brasil | 1503093 | 15 | 33 | nan | nan | nan | Amazônia | 2.5 |
| d151e2e8-9631-370f-b9de-40542b3e746e | -1.63526 | -52.621 | 2024-11-22 04:36:00 | NOAA-20 | PORTO DE MOZ | PARÁ | Brasil | 1505908 | 15 | 33 | nan | nan | nan | Amazônia | 2.2 |
| 7838d98d-8560-3fa3-aa88-57f7de085155 | -2.55379 | -46.54919 | 2024-11-22 04:36:00 | NOAA-20 | PARAGOMINAS | PARÁ | Brasil | 1505502 | 15 | 33 | nan | nan | nan | Amazônia | 1.8 |
| 05329911-a59b-3c93-b98b-66948da2aa0d | -1.13718 | -53.40676 | 2024-11-22 04:36:00 | NOAA-20 | ALMEIRIM | PARÁ | Brasil | 1500503 | 15 | 33 | nan | nan | nan | Amazônia | 8.9 |
| 9ede6148-875e-37a3-972a-a9144eabe350 | -2.49594 | -48.99966 | 2024-11-22 04:36:00 | NOAA-20 | MOJU | PARÁ | Brasil | 1504703 | 15 | 33 | nan | nan | nan | Amazônia | 2.0 |
| 1e2f0058-e9c1-393e-b3b2-fe26d0eb6b49 | -3.76104 | -46.11545 | 2024-11-22 04:36:00 | NOAA-20 | ALTO ALEGRE DO PINDARÉ | MARANHÃO | Brasil | 2100477 | 21 | 33 | nan | nan | nan | Amazônia | 0.8 |
| c9e6b143-a773-3abb-ae00-d1885eceff76 | -4.60283 | -49.57906 | 2024-11-22 04:36:00 | NOAA-20 | NOVO REPARTIMENTO | PARÁ | Brasil | 1505064 | 15 | 33 | nan | nan | nan | Amazônia | 1.0 |
| 95e183ca-91e9-3728-8509-dd1c571a36e9 | -1.26179 | -52.06401 | 2024-11-22 04:36:00 | NOAA-20 | ALMEIRIM | PARÁ | Brasil | 1500503 | 15 | 33 | nan | nan | nan | Amazônia | 2.1 |
| 84ee55ef-9550-348b-9e96-8d528766117a | -2.08074 | -48.8746 | 2024-11-22 04:36:00 | NOAA-20 | MOJU | PARÁ | Brasil | 1504703 | 15 | 33 | nan | nan | nan | Amazônia | 0.7 |
| 617e9f26-ded9-35c1-87a7-0709fced2001 | -2.61911 | -48.19512 | 2024-11-22 04:36:00 | NOAA-20 | TOMÉ-AÇU | PARÁ | Brasil | 1508001 | 15 | 33 | nan | nan | nan | Amazônia | 0.6 |
| 35d37a48-ac60-373f-8f8b-dac49a0f317c | -2.84072 | -46.68637 | 2024-11-22 04:36:00 | NOAA-20 | PARAGOMINAS | PARÁ | Brasil | 1505502 | 15 | 33 | nan | nan | nan | Amazônia | 1.9 |
| 4c1dab61-a389-352a-8701-02f2887281cd | -0.30985 | -51.54686 | 2024-11-22 04:36:00 | NOAA-20 | MAZAGÃO | AMAPÁ | Brasil | 1600402 | 16 | 33 | nan | nan | nan | Amazônia | 2.6 |
| 542b2cc9-4e12-3c5c-adb9-cc939d456b2d | -4.20005 | -53.49201 | 2024-11-22 04:36:00 | NOAA-20 | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 1.7 |
| 069ee72a-2598-362b-bc25-c6b18cc02a2b | -4.63203 | -49.54461 | 2024-11-22 04:36:00 | NOAA-20 | NOVO REPARTIMENTO | PARÁ | Brasil | 1505064 | 15 | 33 | nan | nan | nan | Amazônia | 2.9 |
| d21c8e23-5f53-3178-a6c2-eb6f996b87ed | -3.7531 | -46.11929 | 2024-11-22 04:36:00 | NOAA-20 | ALTO ALEGRE DO PINDARÉ | MARANHÃO | Brasil | 2100477 | 21 | 33 | nan | nan | nan | Amazônia | 3.2 |
| ccafba8e-ed17-38fa-9dda-1685efb2b97e | -2.90575 | -48.31802 | 2024-11-22 04:36:00 | NOAA-20 | TOMÉ-AÇU | PARÁ | Brasil | 1508001 | 15 | 33 | nan | nan | nan | Amazônia | 1.0 |
| bc4047ff-a724-3523-a83a-a41b18da17fc | -2.4954 | -49.00311 | 2024-11-22 04:36:00 | NOAA-20 | MOJU | PARÁ | Brasil | 1504703 | 15 | 33 | nan | nan | nan | Amazônia | 2.0 |
| 6cb1a55d-810c-3f0f-85a0-1604fffe2e22 | -3.2522 | -54.24393 | 2024-11-22 04:36:00 | NOAA-20 | SANTARÉM | PARÁ | Brasil | 1506807 | 15 | 33 | nan | nan | nan | Amazônia | 7.3 |
| de64c6a6-729d-323b-b3e4-a5c4c7b1662b | -2.66379 | -46.60733 | 2024-11-22 04:36:00 | NOAA-20 | CENTRO NOVO DO MARANHÃO | MARANHÃO | Brasil | 2103174 | 21 | 33 | nan | nan | nan | Amazônia | 1.0 |
| 234e7eaa-3ddb-3c98-a792-e9e6c2163d35 | -3.26955 | -53.83395 | 2024-11-22 04:36:00 | NOAA-20 | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | 2.7 |
| ecbeb5dc-611a-355d-ba3b-1f771d22f19d | -1.13925 | -51.67921 | 2024-11-22 04:36:00 | NOAA-20 | GURUPÁ | PARÁ | Brasil | 1503101 | 15 | 33 | nan | nan | nan | Amazônia | 2.6 |
| 86b11c50-fae7-3300-911e-3e8ec2f87199 | -4.41125 | -49.65205 | 2024-11-22 04:36:00 | NOAA-20 | NOVO REPARTIMENTO | PARÁ | Brasil | 1505064 | 15 | 33 | nan | nan | nan | Amazônia | 0.9 |
| 5c0794c1-bd4a-39a9-84e3-5cf26b1d207f | -0.97212 | -51.7161 | 2024-11-22 04:36:00 | NOAA-20 | VITÓRIA DO JARI | AMAPÁ | Brasil | 1600808 | 16 | 33 | nan | nan | nan | Amazônia | 1.3 |
| 6bd86f82-b6c6-3eec-9069-36a491706b36 | -1.2532 | -51.76039 | 2024-11-22 04:36:00 | NOAA-20 | GURUPÁ | PARÁ | Brasil | 1503101 | 15 | 33 | nan | nan | nan | Amazônia | 3.9 |
| a50491fc-c9d0-3147-b72a-47bfc50b09e0 | -2.22346 | -53.73104 | 2024-11-22 04:36:00 | NOAA-20 | PRAINHA | PARÁ | Brasil | 1506005 | 15 | 33 | nan | nan | nan | Amazônia | 1.7 |
| cbd41e4a-d077-3dda-91d7-8fddc8f68a4c | -2.40466 | -49.14816 | 2024-11-22 04:36:00 | NOAA-20 | MOJU | PARÁ | Brasil | 1504703 | 15 | 33 | nan | nan | nan | Amazônia | 1.2 |
| b28d501e-2ff5-39e4-9d30-6063774f382a | -1.51437 | -51.15139 | 2024-11-22 04:36:00 | NOAA-20 | MELGAÇO | PARÁ | Brasil | 1504505 | 15 | 33 | nan | nan | nan | Amazônia | 3.1 |
| 72967566-40ba-3068-b016-db65af270602 | -3.40407 | -46.24424 | 2024-11-22 04:36:00 | NOAA-20 | GOVERNADOR NEWTON BELLO | MARANHÃO | Brasil | 2104651 | 21 | 33 | nan | nan | nan | Amazônia | 1.2 |
| 5fb27130-6a7f-3445-9805-b3c5e7853a8e | -2.61194 | -48.37006 | 2024-11-22 04:36:00 | NOAA-20 | TOMÉ-AÇU | PARÁ | Brasil | 1508001 | 15 | 33 | nan | nan | nan | Amazônia | 1.3 |


[Clique aqui para ver as próximas entradas](README48.md)
