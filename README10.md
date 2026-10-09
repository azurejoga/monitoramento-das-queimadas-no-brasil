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
| 69932661-f900-3a07-a624-28187e6651a3 | -2.5141 | -56.2635 | 2026-10-09 00:06:00 | METOP-B | JURUTI | PARÁ | Brasil | 1503903 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| 83be89a8-4231-3cda-b6b8-73d588447f5d | -3.0989 | -54.2798 | 2026-10-09 00:06:00 | METOP-B | MOJUÍ DOS CAMPOS | PARÁ | Brasil | 1504752 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| c281cc54-c625-32fa-816d-057f603fe62d | -3.3549 | -50.406799 | 2026-10-09 00:06:00 | METOP-B | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| 5a8753d3-a7eb-3c0c-b06e-d86cba087a8b | -1.5903 | -47.351398 | 2026-10-09 00:06:00 | METOP-B | SÃO MIGUEL DO GUAMÁ | PARÁ | Brasil | 1507607 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| 6443cec3-3d0f-3c40-a5d1-9e8cf4927732 | -2.9369 | -54.151402 | 2026-10-09 00:06:00 | METOP-B | SANTARÉM | PARÁ | Brasil | 1506807 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| 8390bcfc-c8b7-3ccb-93f5-5f484bc65ca9 | -9.1306 | -45.832401 | 2026-10-09 00:06:00 | METOP-B | SANTA FILOMENA | PIAUÍ | Brasil | 2209203 | 22 | 33 | nan | nan | nan | Cerrado | nan |
| c4f0eb5d-0713-3753-8005-587b003b4d51 | -17.369301 | -48.172901 | 2026-10-09 00:06:00 | METOP-B | URUTAÍ | GOIÁS | Brasil | 5221809 | 52 | 33 | nan | nan | nan | Cerrado | nan |
| 0ed38229-8037-3bff-84b2-1531a64502b8 | -16.5814 | -46.7584 | 2026-10-09 00:06:00 | METOP-B | UNAÍ | MINAS GERAIS | Brasil | 3170404 | 31 | 33 | nan | nan | nan | Cerrado | nan |
| 8c263a1b-dd55-30f2-b849-5a9797ce550a | -3.3932 | -50.210701 | 2026-10-09 00:06:00 | METOP-B | PACAJÁ | PARÁ | Brasil | 1505486 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| 6dc33cb9-4cb0-3e88-9e63-a2186e5cbf27 | -3.1979 | -50.5793 | 2026-10-09 00:06:00 | METOP-B | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| 72e0a6d1-39db-3daf-9a98-0ae694086a6d | -13.6249 | -44.421902 | 2026-10-09 00:06:00 | METOP-B | CORIBE | BAHIA | Brasil | 2909109 | 29 | 33 | nan | nan | nan | Cerrado | nan |
| 48bd3f30-7d42-32c3-9779-9a221bf2aac5 | -13.1695 | -54.295399 | 2026-10-09 00:06:00 | METOP-B | PARANATINGA | MATO GROSSO | Brasil | 5106307 | 51 | 33 | nan | nan | nan | Amazônia | nan |
| ab6ad75d-d558-39e4-9b66-a8030cb930a4 | -3.1587 | -50.588001 | 2026-10-09 00:06:00 | METOP-B | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| e6e01b97-f08d-3db5-a4f9-fc18c9ef888c | -3.0016 | -53.888302 | 2026-10-09 00:06:00 | METOP-B | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| aa117cfd-1841-3756-8df2-7dc27efa7716 | -2.4912 | -56.160099 | 2026-10-09 00:06:00 | METOP-B | JURUTI | PARÁ | Brasil | 1503903 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| 03686516-5ce7-3fc2-a81f-cbc7d0cc5b1f | -11.844 | -43.578999 | 2026-10-09 00:06:00 | METOP-B | BARRA | BAHIA | Brasil | 2902708 | 29 | 33 | nan | nan | nan | Cerrado | nan |
| 87cf3a1e-53d2-3ffd-8bad-a957e56bec33 | -5.0194 | -50.940102 | 2026-10-09 00:06:00 | METOP-B | ANAPU | PARÁ | Brasil | 1500859 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| 1a0c370f-daa4-3aae-9b05-5f881f050e17 | -8.2624 | -46.901501 | 2026-10-09 00:06:00 | METOP-B | CAMPOS LINDOS | TOCANTINS | Brasil | 1703842 | 17 | 33 | nan | nan | nan | Cerrado | nan |
| f926b76d-3c34-38b5-be94-a96cf69779de | -1.153 | -54.2155 | 2026-10-09 00:06:00 | METOP-B | MONTE ALEGRE | PARÁ | Brasil | 1504802 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| 3fff1852-27c3-31b6-a2bf-17c8640cc9ad | -14.5259 | -48.0415 | 2026-10-09 00:06:00 | METOP-B | NIQUELÂNDIA | GOIÁS | Brasil | 5214606 | 52 | 33 | nan | nan | nan | Cerrado | nan |
| 76979a4f-7128-3842-bffa-b97995428ba3 | -4.9779 | -46.032902 | 2026-10-09 00:06:00 | METOP-B | ARAME | MARANHÃO | Brasil | 2100956 | 21 | 33 | nan | nan | nan | Amazônia | nan |
| 26d7ed6d-010f-3a19-99f8-f81a32c43ed6 | -14.9539 | -41.434601 | 2026-10-09 00:06:00 | METOP-B | TREMEDAL | BAHIA | Brasil | 2931806 | 29 | 33 | nan | nan | nan | Caatinga | nan |
| 7f9b173c-2ef6-3b7c-8012-daa76b690fce | -10.0119 | -48.575699 | 2026-10-09 00:06:00 | METOP-B | MIRACEMA DO TOCANTINS | TOCANTINS | Brasil | 1713205 | 17 | 33 | nan | nan | nan | Cerrado | nan |
| 225514c8-029c-3776-9064-94ecc292ea37 | -7.2222 | -55.070702 | 2026-10-09 00:06:00 | METOP-B | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| 4a1d7acf-ddde-31bb-be47-4efe7fac1465 | -3.2515 | -54.0424 | 2026-10-09 00:06:00 | METOP-B | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| ed7ac1ba-5beb-3c92-9ed2-12d68f317f36 | -6.5059 | -55.3018 | 2026-10-09 00:06:00 | METOP-B | ITAITUBA | PARÁ | Brasil | 1503606 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| 6065f839-e9ff-323a-8c81-19b40aeee82f | -7.4668 | -42.849201 | 2026-10-09 00:06:00 | METOP-B | ITAUEIRA | PIAUÍ | Brasil | 2205102 | 22 | 33 | nan | nan | nan | Caatinga | nan |
| 621401cc-940e-3955-8196-56dae50639bc | -11.9095 | -46.563301 | 2026-10-09 00:06:00 | METOP-B | PONTE ALTA DO BOM JESUS | TOCANTINS | Brasil | 1717800 | 17 | 33 | nan | nan | nan | Cerrado | nan |
| 9b89475a-ac81-3049-9ed9-780c55e85e15 | -9.3 | -47.426601 | 2026-10-09 00:06:00 | METOP-B | RIO SONO | TOCANTINS | Brasil | 1718758 | 17 | 33 | nan | nan | nan | Cerrado | nan |
| 78c66504-6acc-3557-8097-f9581da1bcd1 | -5.8737 | -49.877701 | 2026-10-09 00:06:00 | METOP-B | MARABÁ | PARÁ | Brasil | 1504208 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| e98f5d2f-f05e-3b1b-abdb-e5a0efa7e5f6 | -6.5058 | -55.396999 | 2026-10-09 00:06:00 | METOP-B | NOVO PROGRESSO | PARÁ | Brasil | 1505031 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| fb683bd5-614e-3899-9c0b-42ea6a0f7425 | -16.965799 | -46.352901 | 2026-10-09 00:06:00 | METOP-B | PARACATU | MINAS GERAIS | Brasil | 3147006 | 31 | 33 | nan | nan | nan | Cerrado | nan |
| 52b6745b-1526-3bd5-81c4-3e0bd25716b1 | -11.2296 | -45.312302 | 2026-10-09 00:06:00 | METOP-B | FORMOSA DO RIO PRETO | BAHIA | Brasil | 2911105 | 29 | 33 | nan | nan | nan | Cerrado | nan |
| b4c0f605-4551-3056-a535-15161b5ab151 | -13.5524 | -49.148102 | 2026-10-09 00:06:00 | METOP-B | PORANGATU | GOIÁS | Brasil | 5218003 | 52 | 33 | nan | nan | nan | Cerrado | nan |
| 19ed0dca-b813-3503-a31e-9c4e98795d2f | -3.0357 | -54.2729 | 2026-10-09 00:06:00 | METOP-B | MOJUÍ DOS CAMPOS | PARÁ | Brasil | 1504752 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| 05e6d740-e918-32db-841e-0d2bfd83bfb3 | -8.2312 | -54.727299 | 2026-10-09 00:06:00 | METOP-B | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| 66b8b6d7-5ca2-3ec5-84f6-a76c05c785b9 | -3.0749 | -53.9412 | 2026-10-09 00:06:00 | METOP-B | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| ca3a8ed1-4e67-3bd8-9adc-7d95f0ee1d41 | -4.7639 | -44.007801 | 2026-10-09 00:06:00 | METOP-B | CODÓ | MARANHÃO | Brasil | 2103307 | 21 | 33 | nan | nan | nan | Cerrado | nan |
| d4440594-9409-363b-b39b-5510eb54e67d | -6.8932 | -45.885502 | 2026-10-09 00:06:00 | METOP-B | SÃO RAIMUNDO DAS MANGABEIRAS | MARANHÃO | Brasil | 2111607 | 21 | 33 | nan | nan | nan | Cerrado | nan |
| 648a825f-0a4f-39a3-bdc5-c7e3397cd05f | -10.412 | -47.282001 | 2026-10-09 00:06:00 | METOP-B | PONTE ALTA DO TOCANTINS | TOCANTINS | Brasil | 1717909 | 17 | 33 | nan | nan | nan | Cerrado | nan |
| 4b5c3c4c-291d-32d4-91a3-4fd4ee7270c3 | -3.1897 | -50.588402 | 2026-10-09 00:06:00 | METOP-B | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| f7e8395d-b725-399f-a97d-b0a159d9e810 | -4.1362 | -54.8908 | 2026-10-09 00:06:00 | METOP-B | RURÓPOLIS | PARÁ | Brasil | 1506195 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| ba98242e-d09b-30df-91bc-047a747cd2fa | -3.0966 | -53.946301 | 2026-10-09 00:06:00 | METOP-B | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| d8d15325-6c14-3cdf-b9a2-8bbf5d829fd8 | -11.856 | -43.585899 | 2026-10-09 00:06:00 | METOP-B | BARRA | BAHIA | Brasil | 2902708 | 29 | 33 | nan | nan | nan | Cerrado | nan |
| 383dcd07-121c-35c0-9af2-7b6decbdfa84 | -8.9747 | -47.537701 | 2026-10-09 00:06:00 | METOP-B | CENTENÁRIO | TOCANTINS | Brasil | 1704105 | 17 | 33 | nan | nan | nan | Cerrado | nan |
| 7145d865-9cb1-3d4e-bb62-ccfd509eec86 | -3.2894 | -54.074501 | 2026-10-09 00:06:00 | METOP-B | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| e7011b71-6d82-32ef-8503-a80da880972c | -13.8735 | -43.810001 | 2026-10-09 00:06:00 | METOP-B | CARINHANHA | BAHIA | Brasil | 2907103 | 29 | 33 | nan | nan | nan | Cerrado | nan |
| ccf42bde-1954-3eb3-b648-6762c9bc0fa7 | -6.1438 | -47.923401 | 2026-10-09 00:06:00 | METOP-B | CACHOEIRINHA | TOCANTINS | Brasil | 1703826 | 17 | 33 | nan | nan | nan | Cerrado | nan |
| f97ee498-aa80-3a48-ad38-364db45b5531 | -3.2613 | -54.040298 | 2026-10-09 00:06:00 | METOP-B | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| d93afe0e-3eb9-3725-ad4d-d2f7973c5b29 | -3.8744 | -55.983501 | 2026-10-09 00:06:00 | METOP-B | ITAITUBA | PARÁ | Brasil | 1503606 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| 2e42e355-adf8-30b6-be03-3b55dd779786 | -5.4374 | -43.4571 | 2026-10-09 00:06:00 | METOP-B | MATÕES | MARANHÃO | Brasil | 2106607 | 21 | 33 | nan | nan | nan | Cerrado | nan |
| 01d58aa9-afb3-3164-a044-94b9444ea4d4 | -3.0868 | -53.948399 | 2026-10-09 00:06:00 | METOP-B | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| 4da0f988-5af9-3e47-ae5b-84566372183d | -10.6953 | -44.486 | 2026-10-09 00:06:00 | METOP-B | SANTA RITA DE CÁSSIA | BAHIA | Brasil | 2928406 | 29 | 33 | nan | nan | nan | Cerrado | nan |
| 3e24511c-71a3-30fd-8a78-42d6cfa249a4 | -5.0883 | -46.198399 | 2026-10-09 00:06:00 | METOP-B | AMARANTE DO MARANHÃO | MARANHÃO | Brasil | 2100600 | 21 | 33 | nan | nan | nan | Amazônia | nan |
| 4049eb91-fe30-3d0f-9a0e-ddf8388ac7e0 | -10.0234 | -48.028 | 2026-10-09 00:06:00 | METOP-B | APARECIDA DO RIO NEGRO | TOCANTINS | Brasil | 1701101 | 17 | 33 | nan | nan | nan | Cerrado | nan |
| 8c044265-7899-319a-a1bc-d133075f3bbb | -6.4934 | -55.290901 | 2026-10-09 00:06:00 | METOP-B | ITAITUBA | PARÁ | Brasil | 1503606 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| 1510fea1-987b-3f99-bd8b-40a7064feac0 | -13.2057 | -54.376202 | 2026-10-09 00:06:00 | METOP-B | PARANATINGA | MATO GROSSO | Brasil | 5106307 | 51 | 33 | nan | nan | nan | Amazônia | nan |
| 9fb71e81-3c62-35c5-9324-38d696fd5364 | -22.000601 | -47.1157 | 2026-10-09 00:06:00 | METOP-B | AGUAÍ | SÃO PAULO | Brasil | 3500303 | 35 | 33 | nan | nan | nan | Cerrado | nan |
| b0ace063-6406-3b31-9e3c-e9f69fbc1fa2 | -14.4021 | -43.815201 | 2026-10-09 00:06:00 | METOP-B | MALHADA | BAHIA | Brasil | 2920205 | 29 | 33 | nan | nan | nan | Cerrado | nan |
| 3b4e763a-c58c-3d99-af36-b1a4f9c15512 | -10.4218 | -47.279701 | 2026-10-09 00:06:00 | METOP-B | PONTE ALTA DO TOCANTINS | TOCANTINS | Brasil | 1717909 | 17 | 33 | nan | nan | nan | Cerrado | nan |
| 2e8ef186-f577-3f27-ad0c-a0055a652782 | -7.504 | -45.7607 | 2026-10-09 00:06:00 | METOP-B | SAMBAÍBA | MARANHÃO | Brasil | 2109700 | 21 | 33 | nan | nan | nan | Cerrado | nan |
| 03a8916c-6fff-3a4a-bd92-1e5ff2866f59 | -3.1932 | -50.558498 | 2026-10-09 00:06:00 | METOP-B | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| 99d1c6d7-2fc0-3c54-b970-f03264e2ee81 | -13.6481 | -49.403599 | 2026-10-09 00:06:00 | METOP-B | PORANGATU | GOIÁS | Brasil | 5218003 | 52 | 33 | nan | nan | nan | Cerrado | nan |
| 4aa5e381-1222-3e0a-a9bc-5280772feffc | -13.408 | -43.721901 | 2026-10-09 00:06:00 | METOP-B | SERRA DO RAMALHO | BAHIA | Brasil | 2930154 | 29 | 33 | nan | nan | nan | Cerrado | nan |
| 1a3a248c-d6ba-3b4a-bee0-bd948174c6db | -9.8466 | -49.037102 | 2026-10-09 00:06:00 | METOP-B | DIVINÓPOLIS DO TOCANTINS | TOCANTINS | Brasil | 1707108 | 17 | 33 | nan | nan | nan | Cerrado | nan |
| b4d5ccae-5cb0-38ed-bbf4-fae28b92a66e | -5.684 | -53.486 | 2026-10-09 00:06:00 | METOP-B | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| 55643995-89bd-3eeb-aa93-155d6f41923a | -7.9001 | -54.705399 | 2026-10-09 00:06:00 | METOP-B | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| 09776dec-e101-39d9-91a7-0c1f97a12de7 | -8.7209 | -45.136501 | 2026-10-09 00:06:00 | METOP-B | BAIXA GRANDE DO RIBEIRO | PIAUÍ | Brasil | 2201150 | 22 | 33 | nan | nan | nan | Cerrado | nan |
| 040e61d2-6f4d-358e-a955-802bab3f0eaf | -7.2857 | -46.154701 | 2026-10-09 00:06:00 | METOP-B | BALSAS | MARANHÃO | Brasil | 2101400 | 21 | 33 | nan | nan | nan | Cerrado | nan |
| 3b097e1e-a009-3fe9-b6ef-07ec2ab63172 | -6.503 | -55.3839 | 2026-10-09 00:06:00 | METOP-B | NOVO PROGRESSO | PARÁ | Brasil | 1505031 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| 35774caf-d23e-3ff2-8fb3-c0858f8db680 | -5.6938 | -53.483898 | 2026-10-09 00:06:00 | METOP-B | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| ce59323a-5721-384d-8ea4-064818ae2d81 | -9.1059 | -48.808399 | 2026-10-09 00:06:00 | METOP-B | DOIS IRMÃOS DO TOCANTINS | TOCANTINS | Brasil | 1707207 | 17 | 33 | nan | nan | nan | Amazônia | nan |
| 5db0d1c7-12b7-332e-b9bd-8e56e6fdf287 | -10.7551 | -46.613701 | 2026-10-09 00:06:00 | METOP-B | MATEIROS | TOCANTINS | Brasil | 1712702 | 17 | 33 | nan | nan | nan | Cerrado | nan |
| 30ff8d67-3e3b-37dd-9000-8daac80b27b6 | -10.908 | -45.5284 | 2026-10-09 00:06:00 | METOP-B | FORMOSA DO RIO PRETO | BAHIA | Brasil | 2911105 | 29 | 33 | nan | nan | nan | Cerrado | nan |
| 2bd9a3df-808a-352d-a0b1-ad101fc6907a | -4.2824 | -49.081501 | 2026-10-09 00:06:00 | METOP-B | GOIANÉSIA DO PARÁ | PARÁ | Brasil | 1503093 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| 04d51d4b-3643-3c33-8212-d0e724ab5188 | -3.5873 | -54.678398 | 2026-10-09 00:06:00 | METOP-B | PLACAS | PARÁ | Brasil | 1505650 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| e2c8ee70-302e-37df-8848-a118a0832d11 | -11.2723 | -45.185699 | 2026-10-09 00:06:00 | METOP-B | FORMOSA DO RIO PRETO | BAHIA | Brasil | 2911105 | 29 | 33 | nan | nan | nan | Cerrado | nan |
| 2182ed05-d225-393f-9236-9072bd84ab0a | -2.4616 | -56.073299 | 2026-10-09 00:06:00 | METOP-B | JURUTI | PARÁ | Brasil | 1503903 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| d538aab5-5d0e-3da0-b333-76df47c48586 | -11.215 | -45.249401 | 2026-10-09 00:06:00 | METOP-B | FORMOSA DO RIO PRETO | BAHIA | Brasil | 2911105 | 29 | 33 | nan | nan | nan | Cerrado | nan |
| d74f3821-05aa-353d-bc0d-8d73356343de | -3.9062 | -55.895 | 2026-10-09 00:06:00 | METOP-B | AVEIRO | PARÁ | Brasil | 1501006 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| b97adbe6-ee6c-3a2e-baee-55135179ae69 | -11.2168 | -45.257301 | 2026-10-09 00:06:00 | METOP-B | FORMOSA DO RIO PRETO | BAHIA | Brasil | 2911105 | 29 | 33 | nan | nan | nan | Cerrado | nan |
| eaf18ee1-c249-34b4-9f65-9552f2a24b10 | -6.7165 | -55.044899 | 2026-10-09 00:06:00 | METOP-B | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| 88c45a71-71f9-303e-b50b-7fa2fdfd6151 | -3.0589 | -53.9151 | 2026-10-09 00:06:00 | METOP-B | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| a98915a9-2ae9-36ec-8563-585d1a4bcadd | -3.185 | -50.5676 | 2026-10-09 00:06:00 | METOP-B | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| 4972b36e-8d84-37d3-a0ce-e7d37561352e | -5.9618 | -55.336102 | 2026-10-09 00:06:00 | METOP-B | ITAITUBA | PARÁ | Brasil | 1503606 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| 9d60d069-2048-30b4-b636-1f4845698612 | -8.9048 | -45.172699 | 2026-10-09 00:06:00 | METOP-B | BAIXA GRANDE DO RIBEIRO | PIAUÍ | Brasil | 2201150 | 22 | 33 | nan | nan | nan | Cerrado | nan |
| d3101f38-b74f-3eb2-b1f2-8ea57a3893b4 | -8.2163 | -46.835602 | 2026-10-09 00:06:00 | METOP-B | CAMPOS LINDOS | TOCANTINS | Brasil | 1703842 | 17 | 33 | nan | nan | nan | Cerrado | nan |
| 1cbc1a51-597d-3ca7-bdfe-d88a2a9a95bb | -5.9272 | -51.832901 | 2026-10-09 00:06:00 | METOP-B | SÃO FÉLIX DO XINGU | PARÁ | Brasil | 1507300 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| e19e6671-b4bf-3654-a2bf-cac49296e2cf | -6.1454 | -51.936401 | 2026-10-09 00:06:00 | METOP-B | SÃO FÉLIX DO XINGU | PARÁ | Brasil | 1507300 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| 1bcece3a-2db5-39b8-a5c7-5993f646ea7b | -3.2753 | -54.0574 | 2026-10-09 00:06:00 | METOP-B | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| c471ccb0-c5f3-328e-86b4-29bce81faa49 | -12.2024 | -57.084499 | 2026-10-09 00:06:00 | METOP-B | NOVA MARINGÁ | MATO GROSSO | Brasil | 5108907 | 51 | 33 | nan | nan | nan | Amazônia | nan |
| c3023d11-314e-3797-83b7-cc1740b3b970 | -2.826 | -54.115002 | 2026-10-09 00:06:00 | METOP-B | SANTARÉM | PARÁ | Brasil | 1506807 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| 32fb9334-0df6-3f3b-8f35-c182871a091e | -3.2252 | -54.293999 | 2026-10-09 00:06:00 | METOP-B | MOJUÍ DOS CAMPOS | PARÁ | Brasil | 1504752 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| 7c8daa7f-c579-3576-81de-5ddb7b1823eb | -4.7918 | -45.7631 | 2026-10-09 00:06:00 | METOP-B | ARAME | MARANHÃO | Brasil | 2100956 | 21 | 33 | nan | nan | nan | Amazônia | nan |
| 5cb8e1d9-5156-39eb-aea4-16bf8606141a | -3.6617 | -54.272499 | 2026-10-09 00:06:00 | METOP-B | PLACAS | PARÁ | Brasil | 1505650 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| e9d04d7b-d9f8-3564-9bd3-82f036dfd403 | -2.3902 | -51.2943 | 2026-10-09 00:06:00 | METOP-B | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| e31a0b03-44c5-34cf-b82a-6d34da688c4e | -15.427 | -43.253502 | 2026-10-09 00:06:00 | METOP-B | PAI PEDRO | MINAS GERAIS | Brasil | 3146552 | 31 | 33 | nan | nan | nan | Caatinga | nan |
| 6f998ba1-cc76-3990-a7d4-1d8fdb3f7329 | -10.044 | -48.212101 | 2026-10-09 00:06:00 | METOP-B | PALMAS | TOCANTINS | Brasil | 1721000 | 17 | 33 | nan | nan | nan | Cerrado | nan |
| d464bf20-49d6-3005-ab9b-7a46c334c44e | -3.1917 | -50.551601 | 2026-10-09 00:06:00 | METOP-B | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| b100527e-a95b-31db-967d-7b1d7764d608 | -13.6366 | -44.4277 | 2026-10-09 00:06:00 | METOP-B | CORIBE | BAHIA | Brasil | 2909109 | 29 | 33 | nan | nan | nan | Cerrado | nan |


[Clique aqui para ver as próximas entradas](README11.md)
