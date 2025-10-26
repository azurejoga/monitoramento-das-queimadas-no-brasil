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

## Dados Diários - Página 35

| ID | Latitude | Longitude | Data/Hora GMT | Satélite | Município | Estado | País | Município ID | Estado ID | País ID | Dias sem Chuva | Precipitação | Risco de Fogo | Bioma | FRP |
|----|----------|-----------|---------------|----------|-----------|--------|------|--------------|-----------|---------|----------------|--------------|----------------|-------|-----|
| b2942c68-6946-3573-8283-1ca1b47ced94 | -6.70784 | -42.04681 | 2025-10-26 04:49:00 | NOAA-21 | OEIRAS | PIAUÍ | Brasil | 2207009 | 22 | 33 | nan | nan | nan | Caatinga | 9.1 |
| d66dadee-ff2e-36f9-a80a-e2e22cc96083 | 1.61018 | -55.79538 | 2025-10-26 04:49:00 | NOAA-21 | ÓBIDOS | PARÁ | Brasil | 1505106 | 15 | 33 | nan | nan | nan | Amazônia | 0.8 |
| bee2cffb-4a8e-3c12-a1c5-deb2fae758cb | -4.22456 | -48.36217 | 2025-10-26 04:49:00 | NOAA-21 | RONDON DO PARÁ | PARÁ | Brasil | 1506187 | 15 | 33 | nan | nan | nan | Amazônia | 0.9 |
| 72daf2b9-147f-38ed-880e-9f53d94fb7ed | -2.06835 | -56.87298 | 2025-10-26 04:49:00 | NOAA-21 | NHAMUNDÁ | AMAZONAS | Brasil | 1303007 | 13 | 33 | nan | nan | nan | Amazônia | 1.9 |
| 6bcaae22-f977-3207-80b6-72c443ac3f44 | -7.0156 | -44.68682 | 2025-10-26 04:49:00 | NOAA-21 | BENEDITO LEITE | MARANHÃO | Brasil | 2101806 | 21 | 33 | nan | nan | nan | Cerrado | 4.7 |
| f1891547-9c94-32f8-92cf-d3286c7f61e1 | -6.02251 | -43.30883 | 2025-10-26 04:49:00 | NOAA-21 | SÃO FRANCISCO DO MARANHÃO | MARANHÃO | Brasil | 2110906 | 21 | 33 | nan | nan | nan | Caatinga | 2.3 |
| 8ec9c643-b07e-3942-a882-2c232c5ebbbb | -4.80605 | -50.93589 | 2025-10-26 04:49:00 | NOAA-21 | ANAPU | PARÁ | Brasil | 1500859 | 15 | 33 | nan | nan | nan | Amazônia | 1.5 |
| 331da6ed-0b76-3cef-a67f-125a308f154d | -6.2134 | -42.54294 | 2025-10-26 04:49:00 | NOAA-21 | REGENERAÇÃO | PIAUÍ | Brasil | 2208809 | 22 | 33 | nan | nan | nan | Caatinga | 2.1 |
| a3abce54-778e-3a37-8aff-e3f20a008587 | -6.52701 | -43.57335 | 2025-10-26 04:49:00 | NOAA-21 | SÃO JOÃO DOS PATOS | MARANHÃO | Brasil | 2111102 | 21 | 33 | nan | nan | nan | Cerrado | 2.1 |
| 6480f757-73c2-3b57-bf35-03da359a2bc6 | -3.11074 | -51.20461 | 2025-10-26 04:49:00 | NOAA-21 | ANAPU | PARÁ | Brasil | 1500859 | 15 | 33 | nan | nan | nan | Amazônia | 1.0 |
| 98c0c6b5-4a23-33d9-b178-4c40c2ba7d70 | -3.78926 | -43.40818 | 2025-10-26 04:49:00 | NOAA-21 | CHAPADINHA | MARANHÃO | Brasil | 2103208 | 21 | 33 | nan | nan | nan | Cerrado | 1.6 |
| ef827836-c44e-33b5-89c1-63b73f55ca21 | -3.6934 | -49.94135 | 2025-10-26 04:49:00 | NOAA-21 | TUCURUÍ | PARÁ | Brasil | 1508100 | 15 | 33 | nan | nan | nan | Amazônia | 0.8 |
| 61d7cad3-6f8b-36ee-ad67-a108b2bba80f | -6.4972 | -47.59927 | 2025-10-26 04:49:00 | NOAA-21 | PALMEIRAS DO TOCANTINS | TOCANTINS | Brasil | 1713809 | 17 | 33 | nan | nan | nan | Cerrado | 2.2 |
| ffaa0883-5e21-328a-bead-beb3238eb3c3 | -2.80709 | -49.13945 | 2025-10-26 04:49:00 | NOAA-21 | MOJU | PARÁ | Brasil | 1504703 | 15 | 33 | nan | nan | nan | Amazônia | 1.0 |
| dc31e283-c8d3-30c9-ae8f-4ae246202da7 | -3.93035 | -52.25167 | 2025-10-26 04:49:00 | NOAA-21 | SENADOR JOSÉ PORFÍRIO | PARÁ | Brasil | 1507805 | 15 | 33 | nan | nan | nan | Amazônia | 1.6 |
| c00205ac-5f1f-3e9e-a7ad-ad08cd6e7766 | -4.60571 | -48.7829 | 2025-10-26 04:49:00 | NOAA-21 | RONDON DO PARÁ | PARÁ | Brasil | 1506187 | 15 | 33 | nan | nan | nan | Amazônia | 1.7 |
| b22f0b83-93c0-3a91-9788-b6486b04269f | -5.41598 | -46.33361 | 2025-10-26 04:49:00 | NOAA-21 | AMARANTE DO MARANHÃO | MARANHÃO | Brasil | 2100600 | 21 | 33 | nan | nan | nan | Amazônia | 1.7 |
| 52050db1-fc9d-30c2-8fd4-ee0fc8486727 | -4.58095 | -46.50573 | 2025-10-26 04:49:00 | NOAA-21 | BOM JESUS DAS SELVAS | MARANHÃO | Brasil | 2102036 | 21 | 33 | nan | nan | nan | Amazônia | 1.5 |
| 7ef8cad7-46fa-3264-ad1f-4bbade163d21 | -4.82402 | -50.68699 | 2025-10-26 04:49:00 | NOAA-21 | NOVO REPARTIMENTO | PARÁ | Brasil | 1505064 | 15 | 33 | nan | nan | nan | Amazônia | 1.4 |
| 951b0fc6-5da9-3c26-ba1c-3a6d72238c04 | -4.89083 | -43.23055 | 2025-10-26 04:49:00 | NOAA-21 | CAXIAS | MARANHÃO | Brasil | 2103000 | 21 | 33 | nan | nan | nan | Cerrado | 4.4 |
| dc7b2e33-9709-303a-b175-2fa2e44d82bd | -3.76821 | -48.92355 | 2025-10-26 04:49:00 | NOAA-21 | GOIANÉSIA DO PARÁ | PARÁ | Brasil | 1503093 | 15 | 33 | nan | nan | nan | Amazônia | 1.7 |
| 2c6178cf-d5ae-3ddb-a7aa-3c5cfd345201 | -5.11061 | -43.19672 | 2025-10-26 04:49:00 | NOAA-21 | CAXIAS | MARANHÃO | Brasil | 2103000 | 21 | 33 | nan | nan | nan | Cerrado | 4.7 |
| ed1997fe-103d-3dae-99b1-e2ded61e1546 | -3.31129 | -50.79099 | 2025-10-26 04:49:00 | NOAA-21 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 0.7 |
| 607f535d-981f-3086-9fc7-dd3ee1a0c794 | -5.65345 | -48.45769 | 2025-10-26 04:49:00 | NOAA-21 | BREJO GRANDE DO ARAGUAIA | PARÁ | Brasil | 1501758 | 15 | 33 | nan | nan | nan | Amazônia | 2.5 |
| 6708eb17-64c3-31f2-b0ba-c345848c2ca6 | -4.78389 | -48.67217 | 2025-10-26 04:49:00 | NOAA-21 | BOM JESUS DO TOCANTINS | PARÁ | Brasil | 1501576 | 15 | 33 | nan | nan | nan | Amazônia | 1.2 |
| fcc023ab-aef9-3747-a11b-178e1fa701ee | -4.87337 | -48.6484 | 2025-10-26 04:49:00 | NOAA-21 | BOM JESUS DO TOCANTINS | PARÁ | Brasil | 1501576 | 15 | 33 | nan | nan | nan | Amazônia | 2.5 |
| 3ae943f5-e196-3cd2-b112-0f171aad848f | -3.46693 | -47.6888 | 2025-10-26 04:49:00 | NOAA-21 | PARAGOMINAS | PARÁ | Brasil | 1505502 | 15 | 33 | nan | nan | nan | Amazônia | 2.5 |
| 27d351c2-61ce-3992-9c08-39685019c698 | -5.60771 | -51.31547 | 2025-10-26 04:49:00 | NOAA-21 | SÃO FÉLIX DO XINGU | PARÁ | Brasil | 1507300 | 15 | 33 | nan | nan | nan | Amazônia | 0.8 |
| 99453cdc-f6aa-333a-9563-29c934645846 | -4.59082 | -48.56179 | 2025-10-26 04:49:00 | NOAA-21 | RONDON DO PARÁ | PARÁ | Brasil | 1506187 | 15 | 33 | nan | nan | nan | Amazônia | 2.6 |
| d7466c36-90e3-37fb-8148-c33381707029 | -3.9034 | -47.72564 | 2025-10-26 04:49:00 | NOAA-21 | ULIANÓPOLIS | PARÁ | Brasil | 1508126 | 15 | 33 | nan | nan | nan | Amazônia | 3.3 |
| fe78a04c-36dd-39dc-a6f6-19283a4f3b92 | -5.1066 | -43.18203 | 2025-10-26 04:49:00 | NOAA-21 | CAXIAS | MARANHÃO | Brasil | 2103000 | 21 | 33 | nan | nan | nan | Cerrado | 0.7 |
| 1586f596-4b6d-3d5d-b9e3-a7a8e5f6fc74 | -3.09742 | -49.46171 | 2025-10-26 04:49:00 | NOAA-21 | MOJU | PARÁ | Brasil | 1504703 | 15 | 33 | nan | nan | nan | Amazônia | 2.3 |
| 0961c483-4ac8-3721-b310-19b2b237b0a8 | -4.26604 | -50.50945 | 2025-10-26 04:49:00 | NOAA-21 | NOVO REPARTIMENTO | PARÁ | Brasil | 1505064 | 15 | 33 | nan | nan | nan | Amazônia | 2.9 |
| bbee41bd-1d88-345b-ad01-2dfb324cc378 | 0.68998 | -51.46094 | 2025-10-26 04:49:00 | NOAA-21 | PORTO GRANDE | AMAPÁ | Brasil | 1600535 | 16 | 33 | nan | nan | nan | Amazônia | 1.3 |
| dad3cd75-34b2-3d7c-9694-0bf5c9132bd8 | -2.32457 | -48.58134 | 2025-10-26 04:49:00 | NOAA-21 | ACARÁ | PARÁ | Brasil | 1500206 | 15 | 33 | nan | nan | nan | Amazônia | 13.4 |
| c7f519e5-3efa-33a9-889b-c91442eed437 | -4.8344 | -50.92543 | 2025-10-26 04:49:00 | NOAA-21 | ANAPU | PARÁ | Brasil | 1500859 | 15 | 33 | nan | nan | nan | Amazônia | 1.5 |
| e8c32ee8-5344-3f73-87ef-893b6259ad5f | -4.64036 | -42.51327 | 2025-10-26 04:49:00 | NOAA-21 | JOSÉ DE FREITAS | PIAUÍ | Brasil | 2205508 | 22 | 33 | nan | nan | nan | Caatinga | 1.5 |
| 28cba72d-abac-3b60-bc56-bae00df9ee5d | -5.01234 | -46.85629 | 2025-10-26 04:49:00 | NOAA-21 | AMARANTE DO MARANHÃO | MARANHÃO | Brasil | 2100600 | 21 | 33 | nan | nan | nan | Amazônia | 1.1 |
| a08a2fa8-3e6c-3eaa-aa5f-f20d537c1634 | -2.37919 | -55.96535 | 2025-10-26 04:49:00 | NOAA-21 | JURUTI | PARÁ | Brasil | 1503903 | 15 | 33 | nan | nan | nan | Amazônia | 1.3 |
| d07cf53b-107f-3632-9e2e-0e1d1b5f59ed | 1.60479 | -55.75991 | 2025-10-26 04:49:00 | NOAA-21 | ÓBIDOS | PARÁ | Brasil | 1505106 | 15 | 33 | nan | nan | nan | Amazônia | 2.7 |
| cdcdd3f2-b592-308d-a609-29133f6dc335 | -4.91099 | -48.62301 | 2025-10-26 04:49:00 | NOAA-21 | BOM JESUS DO TOCANTINS | PARÁ | Brasil | 1501576 | 15 | 33 | nan | nan | nan | Amazônia | 3.0 |
| 45569ecb-f3c6-31e3-aae1-4fd47eebef40 | -3.10291 | -49.46555 | 2025-10-26 04:49:00 | NOAA-21 | MOJU | PARÁ | Brasil | 1504703 | 15 | 33 | nan | nan | nan | Amazônia | 1.4 |
| 91c5fe35-9374-30dd-916a-34cbaa03f186 | -6.38868 | -45.77453 | 2025-10-26 04:49:00 | NOAA-21 | FERNANDO FALCÃO | MARANHÃO | Brasil | 2104081 | 21 | 33 | nan | nan | nan | Cerrado | 3.4 |
| de58170e-863d-3a2a-aada-960f1c7160c3 | -3.86293 | -53.94883 | 2025-10-26 04:49:00 | NOAA-21 | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | 0.6 |
| e6cf5d6b-fe69-3855-8901-af4c5cb641bd | -3.09801 | -49.4579 | 2025-10-26 04:49:00 | NOAA-21 | MOJU | PARÁ | Brasil | 1504703 | 15 | 33 | nan | nan | nan | Amazônia | 3.7 |
| 50f4c3e4-43ec-37e0-9c68-0757b1eb737f | -3.28875 | -52.54583 | 2025-10-26 04:49:00 | NOAA-21 | BRASIL NOVO | PARÁ | Brasil | 1501725 | 15 | 33 | nan | nan | nan | Amazônia | 1.6 |
| a3207f69-a3cc-377c-aeb4-3d0ec80f4129 | -4.25329 | -47.16887 | 2025-10-26 04:49:00 | NOAA-21 | ITINGA DO MARANHÃO | MARANHÃO | Brasil | 2105427 | 21 | 33 | nan | nan | nan | Amazônia | 1.8 |
| e35df93d-63e0-3381-9916-9cd3dc3d04dd | -3.14059 | -50.15718 | 2025-10-26 04:49:00 | NOAA-21 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 5.5 |
| 07b89e00-a515-3491-bc61-f0510a64b29f | -3.46424 | -52.23049 | 2025-10-26 04:49:00 | NOAA-21 | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 0.7 |
| 7e763f71-d6f9-3156-9311-a5f89dde84d3 | -5.70869 | -49.31312 | 2025-10-26 04:49:00 | NOAA-21 | MARABÁ | PARÁ | Brasil | 1504208 | 15 | 33 | nan | nan | nan | Amazônia | 2.3 |
| 47e9e85e-edb0-303f-aed4-aefde5d2301c | -3.12011 | -51.20959 | 2025-10-26 04:49:00 | NOAA-21 | ANAPU | PARÁ | Brasil | 1500859 | 15 | 33 | nan | nan | nan | Amazônia | 2.1 |
| 455047af-6cd1-3b65-840b-b657d9ef97f3 | -5.80761 | -50.15635 | 2025-10-26 04:49:00 | NOAA-21 | MARABÁ | PARÁ | Brasil | 1504208 | 15 | 33 | nan | nan | nan | Amazônia | 0.5 |
| 8d95e892-53af-3777-a4bd-fcc8f2f298fa | -3.11725 | -49.10445 | 2025-10-26 04:49:00 | NOAA-21 | MOJU | PARÁ | Brasil | 1504703 | 15 | 33 | nan | nan | nan | Amazônia | 1.1 |
| 89efe62d-f806-322f-9ebd-046e261e89dd | -3.26993 | -50.04704 | 2025-10-26 04:49:00 | NOAA-21 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 4.0 |
| 4faf0167-a20e-31ba-bb54-539e44185cfb | -5.88797 | -49.65699 | 2025-10-26 04:49:00 | NOAA-21 | MARABÁ | PARÁ | Brasil | 1504208 | 15 | 33 | nan | nan | nan | Amazônia | 2.2 |
| 03e5c93c-e6b5-3cf5-887b-901c4a1deb6d | -4.26548 | -50.51306 | 2025-10-26 04:49:00 | NOAA-21 | NOVO REPARTIMENTO | PARÁ | Brasil | 1505064 | 15 | 33 | nan | nan | nan | Amazônia | 1.0 |
| ce4ee5c9-9c3a-331f-a0bf-7c78b44e6aff | -4.25278 | -48.64265 | 2025-10-26 04:49:00 | NOAA-21 | RONDON DO PARÁ | PARÁ | Brasil | 1506187 | 15 | 33 | nan | nan | nan | Amazônia | 2.0 |
| a59f2d64-783a-377e-82a2-db850d19f057 | -4.29496 | -49.29427 | 2025-10-26 04:49:00 | NOAA-21 | GOIANÉSIA DO PARÁ | PARÁ | Brasil | 1503093 | 15 | 33 | nan | nan | nan | Amazônia | 0.7 |
| 1277b989-6b6e-3c1f-b918-a56ca476171a | -6.02346 | -43.30213 | 2025-10-26 04:49:00 | NOAA-21 | SÃO FRANCISCO DO MARANHÃO | MARANHÃO | Brasil | 2110906 | 21 | 33 | nan | nan | nan | Caatinga | 2.5 |
| b24c8bc5-1c2f-31a2-8add-2c805425ebf3 | -4.5975 | -49.58685 | 2025-10-26 04:49:00 | NOAA-21 | NOVO REPARTIMENTO | PARÁ | Brasil | 1505064 | 15 | 33 | nan | nan | nan | Amazônia | 2.1 |
| 129e4456-0d3a-3594-960b-8be491c7fc7d | -3.54481 | -53.3173 | 2025-10-26 04:49:00 | NOAA-21 | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | 3.4 |
| 423e0699-5452-38b1-955c-b325709c13f7 | -6.15953 | -43.13456 | 2025-10-26 04:49:00 | NOAA-21 | SÃO FRANCISCO DO MARANHÃO | MARANHÃO | Brasil | 2110906 | 21 | 33 | nan | nan | nan | Caatinga | 2.2 |
| 7655c25b-343f-35bc-afcc-326b85a00368 | -1.80109 | -54.17944 | 2025-10-26 04:49:00 | NOAA-21 | MONTE ALEGRE | PARÁ | Brasil | 1504802 | 15 | 33 | nan | nan | nan | Amazônia | 1.2 |
| a14eef61-2a16-371e-9c87-fcb6e427097e | -3.75876 | -47.57513 | 2025-10-26 04:49:00 | NOAA-21 | ULIANÓPOLIS | PARÁ | Brasil | 1508126 | 15 | 33 | nan | nan | nan | Amazônia | 1.1 |
| 08edb89e-1667-3a9b-8ab7-58bafb59e5a8 | -4.10727 | -47.28647 | 2025-10-26 04:49:00 | NOAA-21 | ITINGA DO MARANHÃO | MARANHÃO | Brasil | 2105427 | 21 | 33 | nan | nan | nan | Amazônia | 2.8 |
| ed8f1c4d-456f-3938-b30e-9f1e1bad2030 | -2.32814 | -48.58189 | 2025-10-26 04:49:00 | NOAA-21 | ACARÁ | PARÁ | Brasil | 1500206 | 15 | 33 | nan | nan | nan | Amazônia | 5.8 |
| 9727aee1-16fc-3509-9cf9-cc47ce43a84e | -4.21715 | -48.36109 | 2025-10-26 04:49:00 | NOAA-21 | RONDON DO PARÁ | PARÁ | Brasil | 1506187 | 15 | 33 | nan | nan | nan | Amazônia | 1.7 |
| 222e40d1-2c8c-35ce-a6c9-cbc6556650bc | -5.69453 | -46.28715 | 2025-10-26 04:49:00 | NOAA-21 | GRAJAÚ | MARANHÃO | Brasil | 2104800 | 21 | 33 | nan | nan | nan | Cerrado | 2.0 |
| 746b9789-2436-3430-8ea1-2ecb00791bf8 | -3.14717 | -53.14178 | 2025-10-26 04:49:00 | NOAA-21 | MEDICILÂNDIA | PARÁ | Brasil | 1504455 | 15 | 33 | nan | nan | nan | Amazônia | 2.0 |
| 4d212fb7-1553-3e6c-a02c-3ff387b0e946 | -4.09388 | -51.05256 | 2025-10-26 04:49:00 | NOAA-21 | PACAJÁ | PARÁ | Brasil | 1505486 | 15 | 33 | nan | nan | nan | Amazônia | 1.1 |
| ffa7d0df-ab9f-3a8d-83d0-4a7bc57791f7 | -5.8689 | -48.25665 | 2025-10-26 04:49:00 | NOAA-21 | ARAGUATINS | TOCANTINS | Brasil | 1702208 | 17 | 33 | nan | nan | nan | Amazônia | 2.0 |
| 1b77e59c-76ad-3d04-89d0-0f9808b60725 | -6.84351 | -44.00544 | 2025-10-26 04:49:00 | NOAA-21 | PORTO ALEGRE DO PIAUÍ | PIAUÍ | Brasil | 2208551 | 22 | 33 | nan | nan | nan | Cerrado | 1.8 |
| 5c8c9d0a-3d85-3135-a5bc-a1d5ccdc5d27 | -6.6296 | -44.63929 | 2025-10-26 04:49:00 | NOAA-21 | MIRADOR | MARANHÃO | Brasil | 2106706 | 21 | 33 | nan | nan | nan | Cerrado | 3.3 |
| c68b3ecf-cc65-3203-8601-068bb72bb19a | -4.29911 | -49.29081 | 2025-10-26 04:49:00 | NOAA-21 | GOIANÉSIA DO PARÁ | PARÁ | Brasil | 1503093 | 15 | 33 | nan | nan | nan | Amazônia | 1.2 |
| 97841d43-1413-3188-a662-8e9eabfdd4fa | -6.70143 | -42.05025 | 2025-10-26 04:49:00 | NOAA-21 | OEIRAS | PIAUÍ | Brasil | 2207009 | 22 | 33 | nan | nan | nan | Caatinga | 12.1 |
| 18a94eff-4522-33a0-9050-c95cb4cea908 | -6.43725 | -42.03326 | 2025-10-26 04:49:00 | NOAA-21 | NOVO ORIENTE DO PIAUÍ | PIAUÍ | Brasil | 2206902 | 22 | 33 | nan | nan | nan | Caatinga | 2.2 |
| ce6a26ec-b13b-37e9-808a-1c8e43673dde | -6.39128 | -45.78868 | 2025-10-26 04:49:00 | NOAA-21 | FERNANDO FALCÃO | MARANHÃO | Brasil | 2104081 | 21 | 33 | nan | nan | nan | Cerrado | 13.4 |
| 291a1698-0f02-3d73-ace7-effc12fcefef | -2.97638 | -51.19388 | 2025-10-26 04:49:00 | NOAA-21 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 0.8 |
| b86a322c-143d-3220-837d-e10f31f5653c | -4.36288 | -48.6578 | 2025-10-26 04:49:00 | NOAA-21 | RONDON DO PARÁ | PARÁ | Brasil | 1506187 | 15 | 33 | nan | nan | nan | Amazônia | 3.2 |
| f6a38a69-1fa9-3239-82fe-fe19900fe44e | -4.48068 | -48.67046 | 2025-10-26 04:49:00 | NOAA-21 | RONDON DO PARÁ | PARÁ | Brasil | 1506187 | 15 | 33 | nan | nan | nan | Amazônia | 2.2 |
| 858981f5-4377-3313-8a3a-8a4e7a98459f | -3.3922 | -52.44852 | 2025-10-26 04:49:00 | NOAA-21 | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 1.2 |
| f0aa573a-0a94-36fe-9420-5b2254f3ad64 | 1.63106 | -55.71635 | 2025-10-26 04:49:00 | NOAA-21 | ÓBIDOS | PARÁ | Brasil | 1505106 | 15 | 33 | nan | nan | nan | Amazônia | 1.5 |
| 23f9df37-d623-3245-acad-75d653187f4b | -4.83289 | -48.54687 | 2025-10-26 04:49:00 | NOAA-21 | ABEL FIGUEIREDO | PARÁ | Brasil | 1500131 | 15 | 33 | nan | nan | nan | Amazônia | 0.9 |
| 9c822c4f-d38d-3285-ae60-d1e12d318a42 | -6.78646 | -45.41299 | 2025-10-26 04:49:00 | NOAA-21 | SÃO RAIMUNDO DAS MANGABEIRAS | MARANHÃO | Brasil | 2111607 | 21 | 33 | nan | nan | nan | Cerrado | 6.4 |
| ad97350d-dd69-33f2-90ab-de8694df97dc | -3.45785 | -49.69261 | 2025-10-26 04:49:00 | NOAA-21 | BAIÃO | PARÁ | Brasil | 1501204 | 15 | 33 | nan | nan | nan | Amazônia | 1.2 |
| 83b9ac5b-9b85-3350-81ac-4e5fc1a67725 | -5.19583 | -49.91454 | 2025-10-26 04:49:00 | NOAA-21 | ITUPIRANGA | PARÁ | Brasil | 1503705 | 15 | 33 | nan | nan | nan | Amazônia | 0.6 |
| c706d0cc-bac8-3785-97f0-93e7d35b1393 | -4.02778 | -46.0645 | 2025-10-26 04:49:00 | NOAA-21 | SANTA LUZIA | MARANHÃO | Brasil | 2110005 | 21 | 33 | nan | nan | nan | Amazônia | 1.3 |
| 1f31e5ad-d1bb-3681-a289-a0782948fb83 | -4.2985 | -49.29479 | 2025-10-26 04:49:00 | NOAA-21 | GOIANÉSIA DO PARÁ | PARÁ | Brasil | 1503093 | 15 | 33 | nan | nan | nan | Amazônia | 0.7 |
| 8a149955-1017-38c5-aab9-fdb96a08c51d | -3.38426 | -52.36956 | 2025-10-26 04:49:00 | NOAA-21 | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 2.9 |
| bf7e32ba-b7f5-3988-b1c8-578e29fb3e45 | -1.94324 | -56.82391 | 2025-10-26 04:49:00 | NOAA-21 | FARO | PARÁ | Brasil | 1503002 | 15 | 33 | nan | nan | nan | Amazônia | 1.2 |
| b0a3af06-e0aa-347d-9637-5097b31d4fe4 | -3.75635 | -51.75655 | 2025-10-26 04:49:00 | NOAA-21 | SENADOR JOSÉ PORFÍRIO | PARÁ | Brasil | 1507805 | 15 | 33 | nan | nan | nan | Amazônia | 1.5 |
| cd03d768-b424-3e6c-b6ef-8c5d7d569b6a | -3.38418 | -50.16842 | 2025-10-26 04:49:00 | NOAA-21 | PACAJÁ | PARÁ | Brasil | 1505486 | 15 | 33 | nan | nan | nan | Amazônia | 0.5 |
| 07ad8942-bb74-32c3-b1b0-956cb41d8546 | -3.0998 | -49.44645 | 2025-10-26 04:49:00 | NOAA-21 | MOJU | PARÁ | Brasil | 1504703 | 15 | 33 | nan | nan | nan | Amazônia | 1.6 |
| 257bde58-e363-33fe-bf3c-08b1a6d4b077 | -4.1028 | -50.44765 | 2025-10-26 04:49:00 | NOAA-21 | NOVO REPARTIMENTO | PARÁ | Brasil | 1505064 | 15 | 33 | nan | nan | nan | Amazônia | 1.2 |
| 7845a87c-84fb-38e9-87f0-0b46ee0b3ae5 | -5.5648 | -46.52494 | 2025-10-26 04:49:00 | NOAA-21 | AMARANTE DO MARANHÃO | MARANHÃO | Brasil | 2100600 | 21 | 33 | nan | nan | nan | Cerrado | 1.5 |
| 5041d968-3c84-34e9-a6fa-dc5791a92896 | -3.10114 | -54.67513 | 2025-10-26 04:49:00 | NOAA-21 | MOJUÍ DOS CAMPOS | PARÁ | Brasil | 1504752 | 15 | 33 | nan | nan | nan | Amazônia | 1.0 |
| b1e12c3b-cca0-3b45-b736-08c81e261212 | 1.63855 | -55.71164 | 2025-10-26 04:49:00 | NOAA-21 | ÓBIDOS | PARÁ | Brasil | 1505106 | 15 | 33 | nan | nan | nan | Amazônia | 1.3 |
| 0aeea5b0-636b-30ca-8c23-f8ccb477911e | -3.38703 | -52.37352 | 2025-10-26 04:49:00 | NOAA-21 | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 1.2 |
| 87bb83f8-9f53-3472-a3c8-0872e14e9488 | -5.11102 | -43.1892 | 2025-10-26 04:49:00 | NOAA-21 | CAXIAS | MARANHÃO | Brasil | 2103000 | 21 | 33 | nan | nan | nan | Cerrado | 0.9 |
| 602993c1-0375-3866-b211-1cfb62b2c326 | -6.72662 | -39.27508 | 2025-10-26 04:49:00 | NOAA-21 | VÁRZEA ALEGRE | CEARÁ | Brasil | 2314003 | 23 | 33 | nan | nan | nan | Caatinga | 11.0 |


[Clique aqui para ver as próximas entradas](README36.md)
