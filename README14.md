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

## Dados Diários - Página 14

| ID | Latitude | Longitude | Data/Hora GMT | Satélite | Município | Estado | País | Município ID | Estado ID | País ID | Dias sem Chuva | Precipitação | Risco de Fogo | Bioma | FRP |
|----|----------|-----------|---------------|----------|-----------|--------|------|--------------|-----------|---------|----------------|--------------|----------------|-------|-----|
| 5522232b-6bec-3b20-a8d2-f6ccd05db7a6 | -8.16492 | -46.76053 | 2025-09-17 03:45:00 | NOAA-21 | CAMPOS LINDOS | TOCANTINS | Brasil | 1703842 | 17 | 33 | nan | nan | nan | Cerrado | 2.6 |
| 1ed51182-5a9a-3f79-96f6-7f98ffd47674 | -8.96851 | -46.0102 | 2025-09-17 03:45:00 | NOAA-21 | ALTO PARNAÍBA | MARANHÃO | Brasil | 2100501 | 21 | 33 | nan | nan | nan | Cerrado | 4.7 |
| 5a9fd5c9-816e-317b-b0ae-23e0c3e1be4f | -7.88793 | -48.16872 | 2025-09-17 03:45:00 | NOAA-21 | PALMEIRANTE | TOCANTINS | Brasil | 1715705 | 17 | 33 | nan | nan | nan | Cerrado | 2.4 |
| 203feea2-a8c5-3875-814a-74c9a50d41a2 | -12.24738 | -46.75823 | 2025-09-17 03:45:00 | NOAA-21 | PONTE ALTA DO BOM JESUS | TOCANTINS | Brasil | 1717800 | 17 | 33 | nan | nan | nan | Cerrado | 3.8 |
| b7f2e9be-2160-3351-a774-d8402115fe8b | -14.85716 | -45.12537 | 2025-09-17 03:45:00 | NOAA-21 | BONITO DE MINAS | MINAS GERAIS | Brasil | 3108255 | 31 | 33 | nan | nan | nan | Cerrado | 1.5 |
| 76286336-4214-30c3-8b1a-be72ddd857c5 | -9.1093 | -44.85354 | 2025-09-17 03:45:00 | NOAA-21 | BOM JESUS | PIAUÍ | Brasil | 2201903 | 22 | 33 | nan | nan | nan | Cerrado | 4.9 |
| 7b188c78-cc0d-346f-99cf-ad2e6b21fc54 | -15.32854 | -42.05171 | 2025-09-17 03:45:00 | NOAA-21 | SÃO JOÃO DO PARAÍSO | MINAS GERAIS | Brasil | 3162708 | 31 | 33 | nan | nan | nan | Mata Atlântica | 2.7 |
| a2704892-39ad-301e-b2f5-f22bcb9dabb9 | -12.71496 | -47.98285 | 2025-09-17 03:45:00 | NOAA-21 | PARANÃ | TOCANTINS | Brasil | 1716208 | 17 | 33 | nan | nan | nan | Cerrado | 2.4 |
| b0061548-6d48-38f0-94c8-151292432499 | -7.37836 | -47.0449 | 2025-09-17 03:45:00 | NOAA-21 | CAROLINA | MARANHÃO | Brasil | 2102804 | 21 | 33 | nan | nan | nan | Cerrado | 3.4 |
| 78ad8d43-3a2a-3031-ae8e-0a947e00b50d | -11.02861 | -45.05928 | 2025-09-17 03:45:00 | NOAA-21 | FORMOSA DO RIO PRETO | BAHIA | Brasil | 2911105 | 29 | 33 | nan | nan | nan | Cerrado | 4.7 |
| 501c919b-9a78-303a-a430-1fd2d51c3dbb | -8.66312 | -46.39921 | 2025-09-17 03:45:00 | NOAA-21 | BALSAS | MARANHÃO | Brasil | 2101400 | 21 | 33 | nan | nan | nan | Cerrado | 2.5 |
| 97b94f47-6cac-30af-a640-6948d641e8e1 | -11.07463 | -49.76076 | 2025-09-17 03:45:00 | NOAA-21 | DUERÉ | TOCANTINS | Brasil | 1707306 | 17 | 33 | nan | nan | nan | Cerrado | 4.4 |
| 29777430-94a4-3ce6-8d68-947508257afc | -7.7228 | -45.2946 | 2025-09-17 03:45:00 | NOAA-21 | RIBEIRO GONÇALVES | PIAUÍ | Brasil | 2208908 | 22 | 33 | nan | nan | nan | Cerrado | 1.9 |
| 589e4751-8142-38a8-a7d0-0744b26c2f7c | -8.47116 | -44.7277 | 2025-09-17 03:45:00 | NOAA-21 | PALMEIRA DO PIAUÍ | PIAUÍ | Brasil | 2207405 | 22 | 33 | nan | nan | nan | Cerrado | 1.2 |
| 72e4fad3-6715-31ad-b81d-e930b56cfb3a | -11.50311 | -43.70847 | 2025-09-17 03:45:00 | NOAA-21 | BARRA | BAHIA | Brasil | 2902708 | 29 | 33 | nan | nan | nan | Cerrado | 3.4 |
| ae0c1ae9-1415-33e2-808d-bd2a9875a0d5 | -9.06522 | -44.94522 | 2025-09-17 03:45:00 | NOAA-21 | BOM JESUS | PIAUÍ | Brasil | 2201903 | 22 | 33 | nan | nan | nan | Cerrado | 1.3 |
| 25e120f7-5f02-3365-9e6d-fde87489c67d | -14.20213 | -47.00879 | 2025-09-17 03:45:00 | NOAA-21 | FLORES DE GOIÁS | GOIÁS | Brasil | 5207907 | 52 | 33 | nan | nan | nan | Cerrado | 1.0 |
| c5ca239d-acbf-3dda-86e4-dadb0f9d58b8 | -8.92829 | -46.26939 | 2025-09-17 03:45:00 | NOAA-21 | ALTO PARNAÍBA | MARANHÃO | Brasil | 2100501 | 21 | 33 | nan | nan | nan | Cerrado | 1.2 |
| 36ddfbb2-2939-3bc6-9fd4-93279e2c6f85 | -13.75622 | -42.61208 | 2025-09-17 03:45:00 | NOAA-21 | CAETITÉ | BAHIA | Brasil | 2905206 | 29 | 33 | nan | nan | nan | Caatinga | 0.5 |
| 93c2dce4-37a2-39b2-a14b-5360c630f092 | -13.83714 | -42.44593 | 2025-09-17 03:45:00 | NOAA-21 | CAETITÉ | BAHIA | Brasil | 2905206 | 29 | 33 | nan | nan | nan | Caatinga | 0.6 |
| 57016d8b-5e15-336f-999f-635a736650dd | -8.67591 | -46.36248 | 2025-09-17 03:45:00 | NOAA-21 | BALSAS | MARANHÃO | Brasil | 2101400 | 21 | 33 | nan | nan | nan | Cerrado | 1.6 |
| 9409be32-0e1e-35b8-bc53-7e3f7f695144 | -7.72281 | -45.29667 | 2025-09-17 03:45:00 | NOAA-21 | RIBEIRO GONÇALVES | PIAUÍ | Brasil | 2208908 | 22 | 33 | nan | nan | nan | Cerrado | 1.8 |
| c4c3f8b1-b660-351b-83ec-4b43adf65d9d | -12.60974 | -47.98146 | 2025-09-17 03:45:00 | NOAA-21 | PARANÃ | TOCANTINS | Brasil | 1716208 | 17 | 33 | nan | nan | nan | Cerrado | 1.1 |
| 828fdcfa-442b-32d9-9b01-2a2456d82de1 | -12.06302 | -46.53421 | 2025-09-17 03:45:00 | NOAA-21 | PONTE ALTA DO BOM JESUS | TOCANTINS | Brasil | 1717800 | 17 | 33 | nan | nan | nan | Cerrado | 1.8 |
| b1fa69d3-3738-3d3a-b34e-13ca5823ddb0 | -14.62172 | -46.38894 | 2025-09-17 03:45:00 | NOAA-21 | SÍTIO D'ABADIA | GOIÁS | Brasil | 5220702 | 52 | 33 | nan | nan | nan | Cerrado | 2.0 |
| 27e5c419-a1de-37bb-8e07-696545ab07e7 | -12.35261 | -47.055 | 2025-09-17 03:45:00 | NOAA-21 | TAIPAS DO TOCANTINS | TOCANTINS | Brasil | 1720937 | 17 | 33 | nan | nan | nan | Cerrado | 1.1 |
| afbea20a-f91d-3302-a149-2304f931138e | -13.89304 | -48.33175 | 2025-09-17 03:45:00 | NOAA-21 | COLINAS DO SUL | GOIÁS | Brasil | 5205521 | 52 | 33 | nan | nan | nan | Cerrado | 3.9 |
| 21fd01f9-b325-3a20-8eeb-8dc8d57e361b | -12.71184 | -44.67418 | 2025-09-17 03:45:00 | NOAA-21 | SÃO DESIDÉRIO | BAHIA | Brasil | 2928901 | 29 | 33 | nan | nan | nan | Cerrado | 2.3 |
| 41068a3d-fd4d-3531-a5f9-fae909fc3023 | -8.61833 | -45.71467 | 2025-09-17 03:45:00 | NOAA-21 | SANTA FILOMENA | PIAUÍ | Brasil | 2209203 | 22 | 33 | nan | nan | nan | Cerrado | 2.1 |
| dc789012-79a9-3b67-b991-77ee43e78192 | -8.57781 | -46.34213 | 2025-09-17 03:45:00 | NOAA-21 | BALSAS | MARANHÃO | Brasil | 2101400 | 21 | 33 | nan | nan | nan | Cerrado | 0.5 |
| 866ec4cf-7a55-33fe-9674-2dc435f93162 | -12.72471 | -48.02766 | 2025-09-17 03:45:00 | NOAA-21 | PARANÃ | TOCANTINS | Brasil | 1716208 | 17 | 33 | nan | nan | nan | Cerrado | 2.4 |
| 2ba0548e-0413-364b-824a-16eb0016d8b8 | -8.65654 | -46.40238 | 2025-09-17 03:45:00 | NOAA-21 | BALSAS | MARANHÃO | Brasil | 2101400 | 21 | 33 | nan | nan | nan | Cerrado | 2.6 |
| 530ac3f6-74bf-3174-8922-b602d5f6061f | -9.54522 | -46.30075 | 2025-09-17 03:45:00 | NOAA-21 | ALTO PARNAÍBA | MARANHÃO | Brasil | 2100501 | 21 | 33 | nan | nan | nan | Cerrado | 2.4 |
| 098289eb-8487-3e1f-873e-057646e98dec | -9.12474 | -44.88648 | 2025-09-17 03:45:00 | NOAA-21 | BOM JESUS | PIAUÍ | Brasil | 2201903 | 22 | 33 | nan | nan | nan | Cerrado | 1.3 |
| 24eb15e6-afbc-3469-811a-9a7a4b12f16d | -12.69566 | -47.95536 | 2025-09-17 03:45:00 | NOAA-21 | PARANÃ | TOCANTINS | Brasil | 1716208 | 17 | 33 | nan | nan | nan | Cerrado | 4.6 |
| 151f384e-ac3b-3f0a-a5b7-ac39de837001 | -8.1547 | -46.74899 | 2025-09-17 03:45:00 | NOAA-21 | CAMPOS LINDOS | TOCANTINS | Brasil | 1703842 | 17 | 33 | nan | nan | nan | Cerrado | 5.5 |
| 4ef5f4e5-34ef-3d20-acd4-66e388f9ce61 | -12.70588 | -47.95077 | 2025-09-17 03:45:00 | NOAA-21 | PARANÃ | TOCANTINS | Brasil | 1716208 | 17 | 33 | nan | nan | nan | Cerrado | 11.3 |
| 483665ac-01b5-31a5-b4a8-abf6957bee81 | -7.48525 | -46.126 | 2025-09-17 03:45:00 | NOAA-21 | BALSAS | MARANHÃO | Brasil | 2101400 | 21 | 33 | nan | nan | nan | Cerrado | 2.0 |
| 51d9a238-6871-3375-9fc5-3bb2af997d6d | -12.35747 | -47.06011 | 2025-09-17 03:45:00 | NOAA-21 | TAIPAS DO TOCANTINS | TOCANTINS | Brasil | 1720937 | 17 | 33 | nan | nan | nan | Cerrado | 1.8 |
| cc084718-a6aa-3c18-8535-0a10dab11eac | -8.90344 | -47.88035 | 2025-09-17 03:45:00 | NOAA-21 | SANTA MARIA DO TOCANTINS | TOCANTINS | Brasil | 1718881 | 17 | 33 | nan | nan | nan | Cerrado | 4.3 |
| 9498ee5b-871a-38af-a263-adfee403d233 | -12.72668 | -48.0307 | 2025-09-17 03:45:00 | NOAA-21 | PARANÃ | TOCANTINS | Brasil | 1716208 | 17 | 33 | nan | nan | nan | Cerrado | 1.7 |
| 2adeb175-7c38-34c1-a018-de8174b27917 | -8.79042 | -47.80617 | 2025-09-17 03:45:00 | NOAA-21 | SANTA MARIA DO TOCANTINS | TOCANTINS | Brasil | 1718881 | 17 | 33 | nan | nan | nan | Cerrado | 4.1 |
| 26e75a3f-aafb-30f3-9d97-6217d11a7606 | -11.33197 | -43.4816 | 2025-09-17 03:45:00 | NOAA-21 | BARRA | BAHIA | Brasil | 2902708 | 29 | 33 | nan | nan | nan | Cerrado | 1.0 |
| 764933b3-a6ed-3084-9075-5fbeb99fe783 | -8.1341 | -43.6469 | 2025-09-17 03:45:00 | NOAA-21 | ELISEU MARTINS | PIAUÍ | Brasil | 2203602 | 22 | 33 | nan | nan | nan | Cerrado | 4.9 |
| 376ca7f2-71a2-38b6-9e68-9747431d5883 | -14.60513 | -46.39069 | 2025-09-17 03:45:00 | NOAA-21 | SÍTIO D'ABADIA | GOIÁS | Brasil | 5220702 | 52 | 33 | nan | nan | nan | Cerrado | 2.1 |
| aa7db48f-c9d5-358c-a9c3-f051fab852fe | -11.59965 | -49.82153 | 2025-09-17 03:45:00 | NOAA-21 | FORMOSO DO ARAGUAIA | TOCANTINS | Brasil | 1708205 | 17 | 33 | nan | nan | nan | Cerrado | 5.1 |
| a406a219-de64-3844-9c2d-09da5241410a | -8.63761 | -46.40741 | 2025-09-17 03:45:00 | NOAA-21 | BALSAS | MARANHÃO | Brasil | 2101400 | 21 | 33 | nan | nan | nan | Cerrado | 0.9 |
| 777badca-1676-3703-a96a-8a0015aa86f2 | -14.61319 | -46.40474 | 2025-09-17 03:45:00 | NOAA-21 | SÍTIO D'ABADIA | GOIÁS | Brasil | 5220702 | 52 | 33 | nan | nan | nan | Cerrado | 3.2 |
| 2c5f0fc3-8f23-33ad-a975-64e0f33976fc | -9.081 | -44.94772 | 2025-09-17 03:45:00 | NOAA-21 | BOM JESUS | PIAUÍ | Brasil | 2201903 | 22 | 33 | nan | nan | nan | Cerrado | 1.1 |
| 0b71a4ac-a8ac-35b5-a228-0ce38c29f64a | -8.92756 | -46.27323 | 2025-09-17 03:45:00 | NOAA-21 | ALTO PARNAÍBA | MARANHÃO | Brasil | 2100501 | 21 | 33 | nan | nan | nan | Cerrado | 1.2 |
| 88bdb4d7-7d5b-36bd-8f24-27bb5e66ba13 | -12.72763 | -48.02605 | 2025-09-17 03:45:00 | NOAA-21 | PARANÃ | TOCANTINS | Brasil | 1716208 | 17 | 33 | nan | nan | nan | Cerrado | 2.0 |
| 3c7f3ece-cbbc-3091-9743-8dea63549520 | -12.69651 | -47.95109 | 2025-09-17 03:45:00 | NOAA-21 | PARANÃ | TOCANTINS | Brasil | 1716208 | 17 | 33 | nan | nan | nan | Cerrado | 4.6 |
| d2831807-57a1-3ab1-b380-75f92536049c | -8.96799 | -44.19029 | 2025-09-17 03:45:00 | NOAA-21 | SANTA LUZ | PIAUÍ | Brasil | 2209302 | 22 | 33 | nan | nan | nan | Cerrado | 3.8 |
| eba7ff93-a509-35fe-9357-76dc58e076de | -12.94742 | -47.96314 | 2025-09-17 03:45:00 | NOAA-21 | PARANÃ | TOCANTINS | Brasil | 1716208 | 17 | 33 | nan | nan | nan | Cerrado | 4.6 |
| bb984d9c-66c8-3f6d-9242-b150ec323dbc | -9.06949 | -44.95143 | 2025-09-17 03:45:00 | NOAA-21 | BOM JESUS | PIAUÍ | Brasil | 2201903 | 22 | 33 | nan | nan | nan | Cerrado | 2.0 |
| 551acfc5-4dad-3370-913b-eb69a22e7633 | -13.35917 | -39.78979 | 2025-09-17 03:45:00 | NOAA-21 | SANTA INÊS | BAHIA | Brasil | 2927903 | 29 | 33 | nan | nan | nan | Mata Atlântica | 1.9 |
| 71e6d7d2-0d5c-3839-a6bf-e03d3c207b03 | -8.90667 | -46.28181 | 2025-09-17 03:45:00 | NOAA-21 | ALTO PARNAÍBA | MARANHÃO | Brasil | 2100501 | 21 | 33 | nan | nan | nan | Cerrado | 3.7 |
| a99ba409-0142-36b2-8ae9-07f66087d678 | -13.62788 | -45.37457 | 2025-09-17 03:45:00 | NOAA-21 | CORRENTINA | BAHIA | Brasil | 2909307 | 29 | 33 | nan | nan | nan | Cerrado | 8.4 |
| 1e79abce-06fd-358f-9e4b-f4a74c55871c | -9.23944 | -45.64953 | 2025-09-17 03:45:00 | NOAA-21 | SANTA FILOMENA | PIAUÍ | Brasil | 2209203 | 22 | 33 | nan | nan | nan | Cerrado | 1.7 |
| f3621cdb-33fe-3ca8-9376-b8d0ab74b67f | -7.88351 | -48.15636 | 2025-09-17 03:45:00 | NOAA-21 | PALMEIRANTE | TOCANTINS | Brasil | 1715705 | 17 | 33 | nan | nan | nan | Cerrado | 2.5 |
| 0aae4318-a677-36d3-ad32-6029b65404e9 | -8.47171 | -44.72464 | 2025-09-17 03:45:00 | NOAA-21 | PALMEIRA DO PIAUÍ | PIAUÍ | Brasil | 2207405 | 22 | 33 | nan | nan | nan | Cerrado | 1.2 |
| 0f1fb8e0-0365-36df-ba63-d852e81f509d | -8.54175 | -48.97536 | 2025-09-17 03:45:00 | NOAA-21 | PEQUIZEIRO | TOCANTINS | Brasil | 1716653 | 17 | 33 | nan | nan | nan | Cerrado | 1.8 |
| 99a8798a-fd07-30c7-8b60-680b37517d92 | -13.32554 | -43.10276 | 2025-09-17 03:45:00 | NOAA-21 | RIACHO DE SANTANA | BAHIA | Brasil | 2926400 | 29 | 33 | nan | nan | nan | Caatinga | 2.5 |
| 63c4bae1-dc4d-3866-b28a-3980fae93d68 | -9.07533 | -44.94912 | 2025-09-17 03:45:00 | NOAA-21 | BOM JESUS | PIAUÍ | Brasil | 2201903 | 22 | 33 | nan | nan | nan | Cerrado | 2.1 |
| 1b39ef0f-9af2-3b24-9cc5-38808a7029cd | -15.72494 | -39.3209 | 2025-09-17 03:45:00 | NOAA-21 | CANAVIEIRAS | BAHIA | Brasil | 2906303 | 29 | 33 | nan | nan | nan | Mata Atlântica | 1.5 |
| 0e489194-fbd2-3abd-aadb-81dfda210612 | -9.12416 | -44.88964 | 2025-09-17 03:45:00 | NOAA-21 | BOM JESUS | PIAUÍ | Brasil | 2201903 | 22 | 33 | nan | nan | nan | Cerrado | 0.9 |
| bc0387de-926f-3d24-8afe-54d1cdea2379 | -9.0868 | -44.94551 | 2025-09-17 03:45:00 | NOAA-21 | BOM JESUS | PIAUÍ | Brasil | 2201903 | 22 | 33 | nan | nan | nan | Cerrado | 1.1 |
| 6f1b4c34-ece9-3018-bf4c-86ed13a7bf35 | -8.97341 | -46.01516 | 2025-09-17 03:45:00 | NOAA-21 | ALTO PARNAÍBA | MARANHÃO | Brasil | 2100501 | 21 | 33 | nan | nan | nan | Cerrado | 0.9 |
| 93a73c5f-1711-3a4a-a6bd-8c0919196509 | -13.86247 | -44.89173 | 2025-09-17 03:45:00 | NOAA-21 | JABORANDI | BAHIA | Brasil | 2917359 | 29 | 33 | nan | nan | nan | Cerrado | 0.8 |
| 40c91e41-01c2-370c-a768-8ca6b91e024b | -12.7213 | -47.99632 | 2025-09-17 03:45:00 | NOAA-21 | PARANÃ | TOCANTINS | Brasil | 1716208 | 17 | 33 | nan | nan | nan | Cerrado | 11.5 |
| 3722079a-6083-38e0-a17c-f924176b0f70 | -9.07009 | -44.94823 | 2025-09-17 03:45:00 | NOAA-21 | BOM JESUS | PIAUÍ | Brasil | 2201903 | 22 | 33 | nan | nan | nan | Cerrado | 2.1 |
| 6a41cdb2-3702-3888-aad3-8a5cc65ae5a9 | -12.71405 | -47.98746 | 2025-09-17 03:45:00 | NOAA-21 | PARANÃ | TOCANTINS | Brasil | 1716208 | 17 | 33 | nan | nan | nan | Cerrado | 2.4 |
| 9ba98ba9-0c62-31b8-aca0-6d9dfb54692e | -13.85853 | -44.88887 | 2025-09-17 03:45:00 | NOAA-21 | JABORANDI | BAHIA | Brasil | 2917359 | 29 | 33 | nan | nan | nan | Cerrado | 3.6 |
| 6c827613-6dd8-3de9-bb28-208312787495 | -8.90739 | -46.2779 | 2025-09-17 03:45:00 | NOAA-21 | ALTO PARNAÍBA | MARANHÃO | Brasil | 2100501 | 21 | 33 | nan | nan | nan | Cerrado | 2.4 |
| 450f4f8a-50a6-3d16-8ee3-a1cee6c18236 | -13.70994 | -49.85328 | 2025-09-17 03:45:00 | NOAA-21 | AMARALINA | GOIÁS | Brasil | 5200829 | 52 | 33 | nan | nan | nan | Cerrado | 2.8 |
| 43b1bc7c-e193-3762-bf2f-213f2d127dda | -13.20839 | -46.77655 | 2025-09-17 03:45:00 | NOAA-21 | MONTE ALEGRE DE GOIÁS | GOIÁS | Brasil | 5213509 | 52 | 33 | nan | nan | nan | Cerrado | 0.6 |
| 0643367a-7761-301e-b965-424b8439c095 | -12.70848 | -47.95312 | 2025-09-17 03:45:00 | NOAA-21 | PARANÃ | TOCANTINS | Brasil | 1716208 | 17 | 33 | nan | nan | nan | Cerrado | 8.6 |
| 08bd9d2e-8b70-300e-8393-3257dd127961 | -13.32748 | -43.10414 | 2025-09-17 03:45:00 | NOAA-21 | RIACHO DE SANTANA | BAHIA | Brasil | 2926400 | 29 | 33 | nan | nan | nan | Caatinga | 2.2 |
| 2697de2d-f479-3608-adce-1a727a12f81f | -12.72539 | -48.00664 | 2025-09-17 03:45:00 | NOAA-21 | PARANÃ | TOCANTINS | Brasil | 1716208 | 17 | 33 | nan | nan | nan | Cerrado | 6.0 |
| c3f83863-d51b-359e-bd2b-41431eb2cbad | -12.70931 | -47.94899 | 2025-09-17 03:45:00 | NOAA-21 | PARANÃ | TOCANTINS | Brasil | 1716208 | 17 | 33 | nan | nan | nan | Cerrado | 6.3 |
| 6c973144-a75b-3b32-8da1-4f563bf213df | -8.90239 | -47.88583 | 2025-09-17 03:45:00 | NOAA-21 | SANTA MARIA DO TOCANTINS | TOCANTINS | Brasil | 1718881 | 17 | 33 | nan | nan | nan | Cerrado | 4.6 |
| 174199ee-87de-35ef-b80a-3de97273847c | -7.48602 | -46.12183 | 2025-09-17 03:45:00 | NOAA-21 | BALSAS | MARANHÃO | Brasil | 2101400 | 21 | 33 | nan | nan | nan | Cerrado | 2.0 |
| df9eb540-38f9-3774-931b-74bddd545e45 | -12.72035 | -48.00094 | 2025-09-17 03:45:00 | NOAA-21 | PARANÃ | TOCANTINS | Brasil | 1716208 | 17 | 33 | nan | nan | nan | Cerrado | 6.0 |
| b0b2404a-8b19-3be0-81ca-13d0d12ad12a | -15.26766 | -40.58357 | 2025-09-17 03:45:00 | NOAA-21 | ITAMBÉ | BAHIA | Brasil | 2915809 | 29 | 33 | nan | nan | nan | Mata Atlântica | 6.7 |
| 25e3a2e5-1b61-3451-b625-1e207e9b45b1 | -11.21615 | -41.6045 | 2025-09-17 03:45:00 | NOAA-21 | JOÃO DOURADO | BAHIA | Brasil | 2918357 | 29 | 33 | nan | nan | nan | Caatinga | 1.1 |
| a73628a6-8404-3532-99cb-a6b9dacf2cbd | -12.85898 | -47.13189 | 2025-09-17 03:45:00 | NOAA-21 | ARRAIAS | TOCANTINS | Brasil | 1702406 | 17 | 33 | nan | nan | nan | Cerrado | 2.5 |
| 3ed04c80-41fc-3641-9e1d-0c01571b8de7 | -8.66234 | -46.40345 | 2025-09-17 03:45:00 | NOAA-21 | BALSAS | MARANHÃO | Brasil | 2101400 | 21 | 33 | nan | nan | nan | Cerrado | 2.5 |
| 365c16f2-2e64-34d0-97c4-f7dd47ad0cd5 | -15.32376 | -42.056 | 2025-09-17 03:45:00 | NOAA-21 | SÃO JOÃO DO PARAÍSO | MINAS GERAIS | Brasil | 3162708 | 31 | 33 | nan | nan | nan | Mata Atlântica | 2.7 |
| 6c2a8e2a-1cd4-352d-902f-db8615fcdc06 | -12.0053 | -46.68908 | 2025-09-17 03:45:00 | NOAA-21 | NOVO JARDIM | TOCANTINS | Brasil | 1715259 | 17 | 33 | nan | nan | nan | Cerrado | 1.5 |
| fbd65a4f-d034-3d8c-ac99-752eabb6a183 | -12.95923 | -47.95226 | 2025-09-17 03:45:00 | NOAA-21 | PARANÃ | TOCANTINS | Brasil | 1716208 | 17 | 33 | nan | nan | nan | Cerrado | 2.2 |
| 4a2e71da-fb35-349e-a02d-9acc53aab19b | -13.22144 | -47.28222 | 2025-09-17 03:45:00 | NOAA-21 | ARRAIAS | TOCANTINS | Brasil | 1702406 | 17 | 33 | nan | nan | nan | Cerrado | 2.8 |
| 9bc14d6b-840a-3f85-8cdf-d445b8e604a0 | -8.92662 | -46.26991 | 2025-09-17 03:45:00 | NOAA-21 | ALTO PARNAÍBA | MARANHÃO | Brasil | 2100501 | 21 | 33 | nan | nan | nan | Cerrado | 1.3 |
| 9cb13bb5-3619-3f78-b7bc-0077a24abd2e | -14.59987 | -46.3899 | 2025-09-17 03:45:00 | NOAA-21 | SÍTIO D'ABADIA | GOIÁS | Brasil | 5220702 | 52 | 33 | nan | nan | nan | Cerrado | 2.1 |
| 07e72835-e679-3584-97e1-e9b2bf3bd1c1 | -11.46081 | -43.55293 | 2025-09-17 03:45:00 | NOAA-21 | BARRA | BAHIA | Brasil | 2902708 | 29 | 33 | nan | nan | nan | Cerrado | 2.2 |
| 1144d140-a153-380a-a690-83d53ed5d7c5 | -12.35552 | -47.05828 | 2025-09-17 03:45:00 | NOAA-21 | TAIPAS DO TOCANTINS | TOCANTINS | Brasil | 1720937 | 17 | 33 | nan | nan | nan | Cerrado | 1.4 |
| 3f001389-d5e7-3662-9e5e-f8c5611c74e7 | -15.05124 | -42.47737 | 2025-09-17 03:45:00 | NOAA-21 | MONTEZUMA | MINAS GERAIS | Brasil | 3143450 | 31 | 33 | nan | nan | nan | Mata Atlântica | 0.6 |
| 7156199f-c1ac-3e72-b954-71cbe7c1b7e1 | -7.87698 | -48.15515 | 2025-09-17 03:45:00 | NOAA-21 | PALMEIRANTE | TOCANTINS | Brasil | 1715705 | 17 | 33 | nan | nan | nan | Cerrado | 2.5 |
| 1a8fd877-20c6-3658-b053-f2fbfb309e83 | -8.91953 | -46.27631 | 2025-09-17 03:45:00 | NOAA-21 | ALTO PARNAÍBA | MARANHÃO | Brasil | 2100501 | 21 | 33 | nan | nan | nan | Cerrado | 2.8 |
| ec09b5a5-265c-3816-85e9-a59336b03886 | -8.61207 | -45.71741 | 2025-09-17 03:45:00 | NOAA-21 | SANTA FILOMENA | PIAUÍ | Brasil | 2209203 | 22 | 33 | nan | nan | nan | Cerrado | 2.5 |
| 0ad9fb33-04d7-3cd1-90e4-ad3baef234c2 | -12.64343 | -44.85952 | 2025-09-17 03:45:00 | NOAA-21 | SÃO DESIDÉRIO | BAHIA | Brasil | 2928901 | 29 | 33 | nan | nan | nan | Cerrado | 1.1 |


[Clique aqui para ver as próximas entradas](README15.md)
