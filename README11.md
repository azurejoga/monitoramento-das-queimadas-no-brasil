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

## Dados Diários - Página 11

| ID | Latitude | Longitude | Data/Hora GMT | Satélite | Município | Estado | País | Município ID | Estado ID | País ID | Dias sem Chuva | Precipitação | Risco de Fogo | Bioma | FRP |
|----|----------|-----------|---------------|----------|-----------|--------|------|--------------|-----------|---------|----------------|--------------|----------------|-------|-----|
| 70b62727-4f13-393d-9877-aa0a566465a7 | -8.7424 | -45.140301 | 2026-10-09 00:06:00 | METOP-B | BAIXA GRANDE DO RIBEIRO | PIAUÍ | Brasil | 2201150 | 22 | 33 | nan | nan | nan | Cerrado | nan |
| 844565dc-2a82-34fb-a60e-0852d64557a5 | -14.9823 | -47.540501 | 2026-10-09 00:06:00 | METOP-B | FORMOSA | GOIÁS | Brasil | 5208004 | 52 | 33 | nan | nan | nan | Cerrado | nan |
| 37808aba-a2a5-3920-bb43-662bfc88e7b8 | -9.9218 | -44.7981 | 2026-10-09 00:06:00 | METOP-B | RIACHO FRIO | PIAUÍ | Brasil | 2208858 | 22 | 33 | nan | nan | nan | Cerrado | nan |
| da2be7e5-859e-3607-adbf-a5fbae570528 | -4.5389 | -49.669102 | 2026-10-09 00:06:00 | METOP-B | NOVO REPARTIMENTO | PARÁ | Brasil | 1505064 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| 8db36735-4a9f-33de-a7ac-de33018c8415 | -1.0547 | -53.5961 | 2026-10-09 00:06:00 | METOP-B | ALMEIRIM | PARÁ | Brasil | 1500503 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| 42ecfef6-9ef3-3077-aeb4-6932b1b45c48 | -3.0533 | -53.9361 | 2026-10-09 00:06:00 | METOP-B | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| fdb31bf1-d86a-368d-84df-896f3791c9d3 | -5.9863 | -40.9818 | 2026-10-09 00:06:00 | METOP-B | ASSUNÇÃO DO PIAUÍ | PIAUÍ | Brasil | 2201051 | 22 | 33 | nan | nan | nan | Caatinga | nan |
| 51836e24-e4e3-300f-9d76-1a27059bbf1a | -4.6655 | -49.225498 | 2026-10-09 00:06:00 | METOP-B | JACUNDÁ | PARÁ | Brasil | 1503804 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| 0a2f1028-2f4c-3d07-b1bc-1feddd63a052 | -3.9163 | -52.132099 | 2026-10-09 00:06:00 | METOP-B | SENADOR JOSÉ PORFÍRIO | PARÁ | Brasil | 1507805 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| 3861b6d5-46ef-3665-a096-5ac347892271 | -8.9731 | -47.530701 | 2026-10-09 00:06:00 | METOP-B | CENTENÁRIO | TOCANTINS | Brasil | 1704105 | 17 | 33 | nan | nan | nan | Cerrado | nan |
| b8f24f53-ad25-3381-b64e-26a671302f2c | -3.1881 | -50.581501 | 2026-10-09 00:06:00 | METOP-B | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| dd537ef4-2fd4-32ba-aa91-dbc1a42ecde8 | -3.925 | -56.027699 | 2026-10-09 00:06:00 | METOP-B | ITAITUBA | PARÁ | Brasil | 1503606 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| f797c1bd-730f-37df-8af1-505d2ea9ab7d | -2.575 | -56.1689 | 2026-10-09 00:06:00 | METOP-B | JURUTI | PARÁ | Brasil | 1503903 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| ab141b17-ea42-35df-bfb8-2d1576927f14 | -3.5947 | -54.6656 | 2026-10-09 00:06:00 | METOP-B | PLACAS | PARÁ | Brasil | 1505650 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| bdaf13b0-afad-3735-9d6f-126c02f62066 | -17.938999 | -43.950901 | 2026-10-09 00:06:00 | METOP-B | BUENÓPOLIS | MINAS GERAIS | Brasil | 3109204 | 31 | 33 | nan | nan | nan | Cerrado | nan |
| b686c36d-bc9c-3e30-b723-2659bdfc4ccc | -11.6523 | -43.685299 | 2026-10-09 00:06:00 | METOP-B | BARRA | BAHIA | Brasil | 2902708 | 29 | 33 | nan | nan | nan | Cerrado | nan |
| 3475835b-be76-3581-9ce7-5913df93c870 | -2.7861 | -54.0737 | 2026-10-09 00:06:00 | METOP-B | PRAINHA | PARÁ | Brasil | 1506005 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| 3f6b27f6-f4fa-3c8e-bcd3-84212e8c965e | -6.9128 | -45.880901 | 2026-10-09 00:06:00 | METOP-B | SÃO RAIMUNDO DAS MANGABEIRAS | MARANHÃO | Brasil | 2111607 | 21 | 33 | nan | nan | nan | Cerrado | nan |
| 6a675810-27aa-346b-9a52-c890d40bd2bd | -15.7822 | -44.678101 | 2026-10-09 00:06:00 | METOP-B | PEDRAS DE MARIA DA CRUZ | MINAS GERAIS | Brasil | 3149150 | 31 | 33 | nan | nan | nan | Cerrado | nan |
| b78780c4-1fe4-3bd4-857f-afde9e9f5939 | -3.563 | -54.6614 | 2026-10-09 00:06:00 | METOP-B | PLACAS | PARÁ | Brasil | 1505650 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| 0abfd49b-2691-37aa-8d3a-6b2c0a679223 | -14.3923 | -43.8176 | 2026-10-09 00:06:00 | METOP-B | MALHADA | BAHIA | Brasil | 2920205 | 29 | 33 | nan | nan | nan | Cerrado | nan |
| ad8d7388-88a7-3285-9f8e-77f8aec1e73e | -11.8485 | -43.597698 | 2026-10-09 00:06:00 | METOP-B | BARRA | BAHIA | Brasil | 2902708 | 29 | 33 | nan | nan | nan | Cerrado | nan |
| e8b0913c-2b58-31b8-87e8-69036e9a2f27 | -5.9869 | -55.357498 | 2026-10-09 00:06:00 | METOP-B | ITAITUBA | PARÁ | Brasil | 1503606 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| 695a0345-5471-3cc0-b54b-5944b339075e | -4.0897 | -44.118099 | 2026-10-09 00:06:00 | METOP-B | COROATÁ | MARANHÃO | Brasil | 2103604 | 21 | 33 | nan | nan | nan | Cerrado | nan |
| 9dd57fc7-6cf8-38fe-9fc8-1a3bee2e0b0d | -2.7379 | -54.134201 | 2026-10-09 00:06:00 | METOP-B | SANTARÉM | PARÁ | Brasil | 1506807 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| 65e03986-df32-3c0f-845c-60d07b49208c | -5.6875 | -53.455101 | 2026-10-09 00:06:00 | METOP-B | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| 3d04f3b7-7d80-361a-a2c4-818adf33e877 | -2.933 | -54.041599 | 2026-10-09 00:06:00 | METOP-B | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| 301c3ef1-e910-398a-94e1-a861d613b6f7 | -3.2622 | -54.275501 | 2026-10-09 00:06:00 | METOP-B | MOJUÍ DOS CAMPOS | PARÁ | Brasil | 1504752 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| 4b77bb88-49a4-3533-b40f-82bc3ccc409d | -1.2081 | -55.693199 | 2026-10-09 00:06:00 | METOP-B | ÓBIDOS | PARÁ | Brasil | 1505106 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| dde2c0fa-90ab-3f59-857c-2a89142a939f | -3.0079 | -54.7486 | 2026-10-09 00:06:00 | METOP-B | MOJUÍ DOS CAMPOS | PARÁ | Brasil | 1504752 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| 279d7e84-2b57-304c-8dbf-089b1838ded7 | -4.6321 | -50.957298 | 2026-10-09 00:06:00 | METOP-B | ANAPU | PARÁ | Brasil | 1500859 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| f095af3d-3e67-36c0-9e03-977908c95bca | -5.1056 | -46.228802 | 2026-10-09 00:06:00 | METOP-B | AMARANTE DO MARANHÃO | MARANHÃO | Brasil | 2100600 | 21 | 33 | nan | nan | nan | Amazônia | nan |
| feb14b49-a805-3de9-8c48-f9ec21423e6a | 3.5261 | -51.2523 | 2026-10-09 00:06:00 | METOP-B | OIAPOQUE | AMAPÁ | Brasil | 1600501 | 16 | 33 | nan | nan | nan | Amazônia | nan |
| 41a52f3c-b154-3b08-ace3-69d0117bd9d6 | -3.5505 | -54.697498 | 2026-10-09 00:06:00 | METOP-B | PLACAS | PARÁ | Brasil | 1505650 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| fa748ba4-65d0-3d8e-b2b5-4e57e56b7114 | -8.6139 | -48.911499 | 2026-10-09 00:06:00 | METOP-B | PEQUIZEIRO | TOCANTINS | Brasil | 1716653 | 17 | 33 | nan | nan | nan | Cerrado | nan |
| 6a11261a-b22f-35b5-9d2c-2e2cc0d7139a | -3.2898 | -53.983898 | 2026-10-09 00:06:00 | METOP-B | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| 9cd3dc62-5feb-3306-9ea0-cac2bba48a13 | -9.0514 | -47.739799 | 2026-10-09 00:06:00 | METOP-B | BOM JESUS DO TOCANTINS | TOCANTINS | Brasil | 1703305 | 17 | 33 | nan | nan | nan | Cerrado | nan |
| bb1be25d-abd8-3a75-8169-7950269d41d5 | -2.9913 | -53.841801 | 2026-10-09 00:06:00 | METOP-B | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| 35ab56c4-39ab-3f69-86f4-29cbeb629d38 | -3.1119 | -54.153801 | 2026-10-09 00:06:00 | METOP-B | SANTARÉM | PARÁ | Brasil | 1506807 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| 3ec4e672-1b32-32f4-8455-b54dae655929 | -3.2907 | -54.033901 | 2026-10-09 00:06:00 | METOP-B | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| 9086a69b-04e5-36cb-a07a-05407fc17200 | -13.8812 | -43.799 | 2026-10-09 00:06:00 | METOP-B | CARINHANHA | BAHIA | Brasil | 2907103 | 29 | 33 | nan | nan | nan | Cerrado | nan |
| ec1e7565-c9c6-3297-b089-fb2406d07ff0 | -7.5934 | -42.3899 | 2026-10-09 00:06:00 | METOP-B | SÃO MIGUEL DO FIDALGO | PIAUÍ | Brasil | 2210391 | 22 | 33 | nan | nan | nan | Caatinga | nan |
| 19a2ef23-eb9b-3182-a06a-732656c07840 | -1.4318 | -46.8368 | 2026-10-09 00:06:00 | METOP-B | BRAGANÇA | PARÁ | Brasil | 1501709 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| 10684344-eaa8-33e5-8d22-44f8e59319aa | -13.6347 | -44.419498 | 2026-10-09 00:06:00 | METOP-B | CORIBE | BAHIA | Brasil | 2909109 | 29 | 33 | nan | nan | nan | Cerrado | nan |
| 1fdf93a0-5605-33aa-b5fc-e45e9b6f7672 | -11.7648 | -44.949799 | 2026-10-09 00:06:00 | METOP-B | RIACHÃO DAS NEVES | BAHIA | Brasil | 2926202 | 29 | 33 | nan | nan | nan | Cerrado | nan |
| 904172b8-7ff4-32cf-ad19-9ebbb68a4950 | -3.0412 | -54.159 | 2026-10-09 00:06:00 | METOP-B | SANTARÉM | PARÁ | Brasil | 1506807 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| 827ebcf1-298d-3cc1-bcf7-85a9f4a56cc5 | -2.7882 | -54.083199 | 2026-10-09 00:06:00 | METOP-B | PRAINHA | PARÁ | Brasil | 1506005 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| de52609c-6741-3095-98a8-ed09841e2b55 | -6.2186 | -44.147301 | 2026-10-09 00:06:00 | METOP-B | COLINAS | MARANHÃO | Brasil | 2103505 | 21 | 33 | nan | nan | nan | Cerrado | nan |
| 0992592f-e7b9-32d4-913d-c703835a5d72 | -6.1584 | -47.9422 | 2026-10-09 00:06:00 | METOP-B | CACHOEIRINHA | TOCANTINS | Brasil | 1703826 | 17 | 33 | nan | nan | nan | Cerrado | nan |
| 6535a6a1-b138-3b24-9668-697b8be6da80 | -9.5679 | -46.835899 | 2026-10-09 00:06:00 | METOP-B | LIZARDA | TOCANTINS | Brasil | 1712405 | 17 | 33 | nan | nan | nan | Cerrado | nan |
| 0ce57bae-8396-30f5-a643-9fc8175a291c | -12.0085 | -43.488602 | 2026-10-09 00:06:00 | METOP-B | MUQUÉM DO SÃO FRANCISCO | BAHIA | Brasil | 2922250 | 29 | 33 | nan | nan | nan | Cerrado | nan |
| f20721a3-92a7-33bb-a2da-4db9ae185fb3 | -6.0057 | -40.9771 | 2026-10-09 00:06:00 | METOP-B | ASSUNÇÃO DO PIAUÍ | PIAUÍ | Brasil | 2201051 | 22 | 33 | nan | nan | nan | Caatinga | nan |
| 41d668d5-df96-3f4a-9cbb-f9ff991648a1 | -3.077 | -53.9506 | 2026-10-09 00:06:00 | METOP-B | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| 466d6853-f7b7-359c-bdd7-439f013a6a9b | -13.7027 | -49.083401 | 2026-10-09 00:06:00 | METOP-B | SANTA TEREZA DE GOIÁS | GOIÁS | Brasil | 5219605 | 52 | 33 | nan | nan | nan | Cerrado | nan |
| f1717bfe-d3ce-3890-b03a-028707f32133 | -14.9741 | -47.5499 | 2026-10-09 00:06:00 | METOP-B | FORMOSA | GOIÁS | Brasil | 5208004 | 52 | 33 | nan | nan | nan | Cerrado | nan |
| 6ea58a4a-9d52-3782-b77c-0104f3cfd30f | -7.2709 | -48.3465 | 2026-10-09 00:06:00 | METOP-B | ARAGUAÍNA | TOCANTINS | Brasil | 1702109 | 17 | 33 | nan | nan | nan | Amazônia | nan |
| b0c38fcc-c745-3aa3-81d0-474391d4cc68 | -4.5039 | -45.811001 | 2026-10-09 00:06:00 | METOP-B | SANTA LUZIA | MARANHÃO | Brasil | 2110005 | 21 | 33 | nan | nan | nan | Amazônia | nan |
| fe14530d-b01b-38a2-b24f-edfa2a944b12 | -11.7653 | -46.791401 | 2026-10-09 00:06:00 | METOP-B | DIANÓPOLIS | TOCANTINS | Brasil | 1707009 | 17 | 33 | nan | nan | nan | Cerrado | nan |
| e3901e55-b2d4-3dc7-b91c-76636de4d6cb | -2.4016 | -51.299198 | 2026-10-09 00:06:00 | METOP-B | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| 5f121862-97ed-3cdf-bf05-4464819af495 | -11.0795 | -44.0574 | 2026-10-09 00:06:00 | METOP-B | MANSIDÃO | BAHIA | Brasil | 2920452 | 29 | 33 | nan | nan | nan | Cerrado | nan |
| c59a20c9-3f8a-35b9-b0e7-487fddad2c23 | -10.4175 | -48.872501 | 2026-10-09 00:06:00 | METOP-B | PUGMIL | TOCANTINS | Brasil | 1718451 | 17 | 33 | nan | nan | nan | Cerrado | nan |
| 7ac1ef00-4d20-3469-a25f-371eb199946e | -2.9522 | -54.1278 | 2026-10-09 00:06:00 | METOP-B | SANTARÉM | PARÁ | Brasil | 1506807 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| 251639bc-4f7b-3e7f-9c12-90c9d5896502 | -3.2117 | -42.959801 | 2026-10-09 00:06:00 | METOP-B | SANTA QUITÉRIA DO MARANHÃO | MARANHÃO | Brasil | 2110104 | 21 | 33 | nan | nan | nan | Cerrado | nan |
| 55479c0c-abf8-3b64-b0d7-0ba50b025892 | -9.9002 | -44.794201 | 2026-10-09 00:06:00 | METOP-B | RIACHO FRIO | PIAUÍ | Brasil | 2208858 | 22 | 33 | nan | nan | nan | Cerrado | nan |
| 2dfe11c6-9cf7-37bb-b32c-7e06a213f1b5 | -12.2121 | -57.0826 | 2026-10-09 00:06:00 | METOP-B | NOVA MARINGÁ | MATO GROSSO | Brasil | 5108907 | 51 | 33 | nan | nan | nan | Amazônia | nan |
| ae79cf67-1c31-3e4a-b535-5173c4a5c3c3 | -7.5625 | -46.684101 | 2026-10-09 00:06:00 | METOP-B | RIACHÃO | MARANHÃO | Brasil | 2109502 | 21 | 33 | nan | nan | nan | Cerrado | nan |
| bc463c25-c1a7-33d9-bcbb-8dab7acb6a78 | -7.0635 | -47.387699 | 2026-10-09 00:06:00 | METOP-B | CAROLINA | MARANHÃO | Brasil | 2102804 | 21 | 33 | nan | nan | nan | Cerrado | nan |
| cc32b1f1-e055-3828-aaf4-69f6f3cde5b9 | -4.0883 | -48.9524 | 2026-10-09 00:06:00 | METOP-B | GOIANÉSIA DO PARÁ | PARÁ | Brasil | 1503093 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| 18441895-d0b9-368f-af1f-d8925d23014f | -2.9185 | -54.114899 | 2026-10-09 00:06:00 | METOP-B | SANTARÉM | PARÁ | Brasil | 1506807 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| b2850dcb-20f1-3fbb-97c5-1783e178d373 | -5.5029 | -42.864799 | 2026-10-09 00:06:00 | METOP-B | NAZÁRIA | PIAUÍ | Brasil | 2206720 | 22 | 33 | nan | nan | nan | Caatinga | nan |
| 25eaf1e0-e520-35c7-96cd-586fce29c43a | -15.5694 | -44.517601 | 2026-10-09 00:06:00 | METOP-B | JANUÁRIA | MINAS GERAIS | Brasil | 3135209 | 31 | 33 | nan | nan | nan | Cerrado | nan |
| 5edcbe0d-0d0c-3d29-89e9-40e270b2dfb4 | -3.1141 | -54.163502 | 2026-10-09 00:06:00 | METOP-B | SANTARÉM | PARÁ | Brasil | 1506807 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| 0fa60b04-71ff-39cf-8cf5-084316261fda | -3.0693 | -53.9622 | 2026-10-09 00:06:00 | METOP-B | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| 1dfe2996-4f0c-30f6-879c-5b9cbc185772 | -4.3961 | -49.127899 | 2026-10-09 00:06:00 | METOP-B | JACUNDÁ | PARÁ | Brasil | 1503804 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| 7c6d5581-0c8c-3f84-a81e-b2b9d14583ae | -8.2877 | -45.713799 | 2026-10-09 00:06:00 | METOP-B | TASSO FRAGOSO | MARANHÃO | Brasil | 2112001 | 21 | 33 | nan | nan | nan | Cerrado | nan |
| 1e705839-9eb4-3136-8fe6-bf1b34368e5a | -11.9867 | -43.4841 | 2026-10-09 00:06:00 | METOP-B | MUQUÉM DO SÃO FRANCISCO | BAHIA | Brasil | 2922250 | 29 | 33 | nan | nan | nan | Cerrado | nan |
| 2518da8c-dfb3-36e1-9839-f1290e7f49b3 | -11.4099 | -46.679699 | 2026-10-09 00:06:00 | METOP-B | RIO DA CONCEIÇÃO | TOCANTINS | Brasil | 1718659 | 17 | 33 | nan | nan | nan | Cerrado | nan |
| 51087e8d-9220-3d7f-a698-5276bc6c6b0b | -3.1022 | -53.9254 | 2026-10-09 00:06:00 | METOP-B | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| 47bca4fb-b226-36fe-a265-799b2adcf894 | -2.9372 | -53.922001 | 2026-10-09 00:06:00 | METOP-B | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| 522f0aea-6faa-346f-9b59-bda71dec0fe4 | -6.4515 | -55.477299 | 2026-10-09 00:06:00 | METOP-B | ITAITUBA | PARÁ | Brasil | 1503606 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| 04c2afbf-817f-3a23-9282-27c141063c8c | -3.3017 | -49.1208 | 2026-10-09 00:06:00 | METOP-B | MOJU | PARÁ | Brasil | 1504703 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| bc258ffc-e5c5-36ad-a6cf-196efa54e8d9 | -2.5624 | -56.1581 | 2026-10-09 00:06:00 | METOP-B | JURUTI | PARÁ | Brasil | 1503903 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| 44947a8a-6599-3983-ae94-4054b26cc516 | -2.8883 | -54.0714 | 2026-10-09 00:06:00 | METOP-B | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| c4e1b34e-45af-3886-997c-1a9b0c0b4991 | -8.7884 | -47.2626 | 2026-10-09 00:06:00 | METOP-B | RECURSOLÂNDIA | TOCANTINS | Brasil | 1718501 | 17 | 33 | nan | nan | nan | Cerrado | nan |
| 5e9e9825-00bc-3440-b831-28c69d24f80a | -10.4726 | -47.231201 | 2026-10-09 00:06:00 | METOP-B | PONTE ALTA DO TOCANTINS | TOCANTINS | Brasil | 1717909 | 17 | 33 | nan | nan | nan | Cerrado | nan |
| 7210c6f7-7375-391d-97b8-59a42647d1ac | -11.0056 | -45.4151 | 2026-10-09 00:06:00 | METOP-B | FORMOSA DO RIO PRETO | BAHIA | Brasil | 2911105 | 29 | 33 | nan | nan | nan | Cerrado | nan |
| 7784fc53-ba6a-3115-8872-ef6792ac7586 | -2.9785 | -54.061699 | 2026-10-09 00:06:00 | METOP-B | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| 2e777577-0d6b-31d2-ab36-8f15670385ec | -3.0238 | -54.173 | 2026-10-09 00:06:00 | METOP-B | SANTARÉM | PARÁ | Brasil | 1506807 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| 9bfdce93-b573-3aec-ac2c-0c9ab96e114e | -11.251 | -46.300098 | 2026-10-09 00:06:00 | METOP-B | FORMOSA DO RIO PRETO | BAHIA | Brasil | 2911105 | 29 | 33 | nan | nan | nan | Cerrado | nan |
| 4b0bd22d-de76-3917-86bc-d5075cf9625b | -8.1874 | -46.350601 | 2026-10-09 00:06:00 | METOP-B | BALSAS | MARANHÃO | Brasil | 2101400 | 21 | 33 | nan | nan | nan | Cerrado | nan |
| 053aec8b-490d-3d11-9c28-a717b378c9b9 | -8.6123 | -48.904499 | 2026-10-09 00:06:00 | METOP-B | PEQUIZEIRO | TOCANTINS | Brasil | 1716653 | 17 | 33 | nan | nan | nan | Cerrado | nan |
| 4fc342ee-837d-3e8f-87b1-1d84c2552c2c | -2.9206 | -54.124599 | 2026-10-09 00:06:00 | METOP-B | SANTARÉM | PARÁ | Brasil | 1506807 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| c2a6e3e3-27f6-3900-b857-56a63b8b154d | -4.5524 | -54.967098 | 2026-10-09 00:06:00 | METOP-B | RURÓPOLIS | PARÁ | Brasil | 1506195 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| c8a28d17-4146-3e1c-bfe7-d449d1f57144 | 0.9404 | -50.1926 | 2026-10-09 00:06:00 | METOP-B | MACAPÁ | AMAPÁ | Brasil | 1600303 | 16 | 33 | nan | nan | nan | Amazônia | nan |
| 19424934-7da4-3540-9fef-75e0bc986341 | -8.9829 | -45.907799 | 2026-10-09 00:06:00 | METOP-B | SANTA FILOMENA | PIAUÍ | Brasil | 2209203 | 22 | 33 | nan | nan | nan | Cerrado | nan |
| 9cc6f27c-7494-356d-9d2d-90485fcd9b89 | -14.0144 | -48.765301 | 2026-10-09 00:06:00 | METOP-B | URUAÇU | GOIÁS | Brasil | 5221601 | 52 | 33 | nan | nan | nan | Cerrado | nan |
| 9945ccfd-eccf-3665-80a7-cdb83f12e24a | -7.2233 | -55.1241 | 2026-10-09 00:06:00 | METOP-B | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| 8964963e-0b6b-3fb0-a553-8bf6264500ad | -15.4228 | -43.235699 | 2026-10-09 00:06:00 | METOP-B | PAI PEDRO | MINAS GERAIS | Brasil | 3146552 | 31 | 33 | nan | nan | nan | Caatinga | nan |
| 3677095c-7e59-34d1-887e-60e60845feee | -9.0369 | -46.8601 | 2026-10-09 00:06:00 | METOP-B | BALSAS | MARANHÃO | Brasil | 2101400 | 21 | 33 | nan | nan | nan | Cerrado | nan |
| cc00bdae-69dc-3914-8fa9-975827debbab | -4.4969 | -43.616199 | 2026-10-09 00:06:00 | METOP-B | ALDEIAS ALTAS | MARANHÃO | Brasil | 2100303 | 21 | 33 | nan | nan | nan | Cerrado | nan |


[Clique aqui para ver as próximas entradas](README12.md)
