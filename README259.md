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

## Dados Diários - Página 259

| ID | Latitude | Longitude | Data/Hora GMT | Satélite | Município | Estado | País | Município ID | Estado ID | País ID | Dias sem Chuva | Precipitação | Risco de Fogo | Bioma | FRP |
|----|----------|-----------|---------------|----------|-----------|--------|------|--------------|-----------|---------|----------------|--------------|----------------|-------|-----|
| 5995d13b-8797-3571-8e9b-87a533b56c36 | -4.3471 | -43.8021 | 2026-10-07 19:20:00 | GOES-19 | CODÓ | MARANHÃO | Brasil | 2103307 | 21 | 33 | nan | nan | nan | Cerrado | 97.0 |
| 63d1628c-240a-3b24-ab52-ef25468d8863 | -4.0947 | -52.0635 | 2026-10-07 19:20:00 | GOES-19 | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 58.7 |
| ffe44e77-829a-39da-ac91-07df08476bba | -5.2094 | -48.326 | 2026-10-07 19:20:00 | GOES-19 | SÃO SEBASTIÃO DO TOCANTINS | TOCANTINS | Brasil | 1720309 | 17 | 33 | nan | nan | nan | Amazônia | 49.5 |
| 1a48834c-d827-3ba8-a44d-2949e4a45fdc | -3.328 | -50.1775 | 2026-10-07 19:20:00 | GOES-19 | PACAJÁ | PARÁ | Brasil | 1505486 | 15 | 33 | nan | nan | nan | Amazônia | 147.0 |
| af73f7e3-372d-3413-b8b2-71517a76f1bc | -3.2451 | -57.8693 | 2026-10-07 19:20:00 | GOES-19 | BOA VISTA DO RAMOS | AMAZONAS | Brasil | 1300680 | 13 | 33 | nan | nan | nan | Amazônia | 75.6 |
| 1019d3bd-ff5d-309e-ab6d-f542ee60b3f9 | -3.443 | -49.2641 | 2026-10-07 19:20:00 | GOES-19 | BREU BRANCO | PARÁ | Brasil | 1501782 | 15 | 33 | nan | nan | nan | Amazônia | 70.0 |
| 9b19c3a9-517d-3a63-903e-4a21d98e693b | -6.1484 | -51.927 | 2026-10-07 19:20:00 | GOES-19 | SÃO FÉLIX DO XINGU | PARÁ | Brasil | 1507300 | 15 | 33 | nan | nan | nan | Amazônia | 199.6 |
| 9f037769-74c7-30cf-b02c-49a45ccda632 | -5.7191 | -45.132 | 2026-10-07 19:20:00 | GOES-19 | BARRA DO CORDA | MARANHÃO | Brasil | 2101608 | 21 | 33 | nan | nan | nan | Cerrado | 65.1 |
| 968ff771-ff3b-3d99-b5eb-cdf33e2c572e | -2.9271 | -53.9295 | 2026-10-07 19:20:00 | GOES-19 | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | 81.8 |
| 020cbc03-79f4-339f-aa79-ca26be69e79d | -7.0267 | -45.4367 | 2026-10-07 19:20:00 | GOES-19 | SÃO RAIMUNDO DAS MANGABEIRAS | MARANHÃO | Brasil | 2111607 | 21 | 33 | nan | nan | nan | Cerrado | 61.9 |
| f20a06ee-ebbb-30c0-a96b-09bd6159cc21 | -3.2267 | -57.889 | 2026-10-07 19:20:00 | GOES-19 | BOA VISTA DO RAMOS | AMAZONAS | Brasil | 1300680 | 13 | 33 | nan | nan | nan | Amazônia | 69.2 |
| a4e190da-102a-328e-82fc-8e22c8a2bb1b | -11.2333 | -44.8678 | 2026-10-07 19:20:00 | GOES-19 | SANTA RITA DE CÁSSIA | BAHIA | Brasil | 2928406 | 29 | 33 | nan | nan | nan | Cerrado | 132.6 |
| 4b526192-58fa-30d1-96f4-4f20e986f5cb | -8.5183 | -67.0139 | 2026-10-07 19:20:00 | GOES-19 | LÁBREA | AMAZONAS | Brasil | 1302405 | 13 | 33 | nan | nan | nan | Amazônia | 145.0 |
| 2bb5691f-2ede-35b2-9d1e-97673449a9d9 | -7.6767 | -72.3142 | 2026-10-07 19:20:00 | GOES-19 | CRUZEIRO DO SUL | ACRE | Brasil | 1200203 | 12 | 33 | nan | nan | nan | Amazônia | 175.5 |
| e87ddbc9-78df-3aa7-b07e-f10e1f338ccc | -7.3749 | -46.1937 | 2026-10-07 19:20:00 | GOES-19 | RIACHÃO | MARANHÃO | Brasil | 2109502 | 21 | 33 | nan | nan | nan | Cerrado | 69.0 |
| c85c2d49-4274-34a5-a86e-b511364cf10e | -5.9512 | -46.3727 | 2026-10-07 19:20:00 | GOES-19 | GRAJAÚ | MARANHÃO | Brasil | 2104800 | 21 | 33 | nan | nan | nan | Cerrado | 105.6 |
| c1b07735-2182-3c1e-94e0-dfd23b74a323 | -10.9762 | -45.4094 | 2026-10-07 19:20:00 | GOES-19 | FORMOSA DO RIO PRETO | BAHIA | Brasil | 2911105 | 29 | 33 | nan | nan | nan | Cerrado | 101.6 |
| 6e545370-f67c-3a1f-8d34-441e61d3bfa3 | -3.5678 | -54.6547 | 2026-10-07 19:20:00 | GOES-19 | PLACAS | PARÁ | Brasil | 1505650 | 15 | 33 | nan | nan | nan | Amazônia | 216.2 |
| 5ab30fd0-5721-350f-b9ab-2c9d4bd22929 | -6.0074 | -53.5325 | 2026-10-07 19:20:00 | GOES-19 | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 63.8 |
| c08c4d4a-8ad0-3738-99c1-3813fba0d07a | -2.9271 | -53.9496 | 2026-10-07 19:20:00 | GOES-19 | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | 60.8 |
| 67f70187-9416-376f-afb0-9269b511030d | -5.9699 | -46.3714 | 2026-10-07 19:20:00 | GOES-19 | GRAJAÚ | MARANHÃO | Brasil | 2104800 | 21 | 33 | nan | nan | nan | Cerrado | 79.4 |
| 3ec3abac-0b9f-3624-bb25-441eedc5a959 | -9.5468 | -64.8196 | 2026-10-07 19:20:00 | GOES-19 | PORTO VELHO | RONDÔNIA | Brasil | 1100205 | 11 | 33 | nan | nan | nan | Amazônia | 117.3 |
| c6bdbee1-2390-3897-b6aa-0bdd5196a1de | -3.55 | -54.4952 | 2026-10-07 19:20:00 | GOES-19 | PLACAS | PARÁ | Brasil | 1505650 | 15 | 33 | nan | nan | nan | Amazônia | 53.0 |
| 18f06d48-7928-368e-9cf2-a4d04aa0c207 | -3.203 | -53.8823 | 2026-10-07 19:20:00 | GOES-19 | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | 50.1 |
| 1303bd96-2a5c-34d1-8fec-07a6abbed8c8 | -3.891 | -52.2147 | 2026-10-07 19:20:00 | GOES-19 | SENADOR JOSÉ PORFÍRIO | PARÁ | Brasil | 1507805 | 15 | 33 | nan | nan | nan | Amazônia | 90.1 |
| 118740d7-5fd3-33a6-b091-7539084395a7 | -2.7043 | -49.0533 | 2026-10-07 19:20:00 | GOES-19 | MOJU | PARÁ | Brasil | 1504703 | 15 | 33 | nan | nan | nan | Amazônia | 60.4 |
| 55e81eb9-d9b2-3f1c-b6ad-dfe41c8e9689 | -5.6934 | -53.4667 | 2026-10-07 19:20:00 | GOES-19 | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 84.9 |
| 5b55012b-2b6b-30b5-9b2a-e2c21878fd85 | -3.269 | -51.0575 | 2026-10-07 19:20:00 | GOES-19 | PACAJÁ | PARÁ | Brasil | 1505486 | 15 | 33 | nan | nan | nan | Amazônia | 196.3 |
| ba8be51d-744d-328b-9723-811411fdd163 | -1.4571 | -54.6365 | 2026-10-07 19:20:00 | GOES-19 | ALENQUER | PARÁ | Brasil | 1500404 | 15 | 33 | nan | nan | nan | Amazônia | 85.3 |
| 4d5300de-9355-3119-82a7-396e3e917a48 | -3.2357 | -50.1805 | 2026-10-07 19:20:00 | GOES-19 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 53.3 |
| ae7b3eef-ead2-372c-812a-1abf44c8dc62 | -13.3671 | -43.8742 | 2026-10-07 19:20:00 | GOES-19 | SERRA DO RAMALHO | BAHIA | Brasil | 2930154 | 29 | 33 | nan | nan | nan | Cerrado | 165.5 |
| 2cc3dae6-2955-38bf-aeb0-da59704c81e9 | -11.8503 | -43.5598 | 2026-10-07 19:20:00 | GOES-19 | BARRA | BAHIA | Brasil | 2902708 | 29 | 33 | nan | nan | nan | Cerrado | 125.6 |
| c63722ec-34d8-3be5-9b2f-5ed49cc16ffe | -3.0069 | -57.9129 | 2026-10-07 19:20:00 | GOES-19 | BOA VISTA DO RAMOS | AMAZONAS | Brasil | 1300680 | 13 | 33 | nan | nan | nan | Amazônia | 95.4 |
| 895b24d2-0d42-3d9b-8b58-e8ab0c1520cb | -7.1827 | -52.6078 | 2026-10-07 19:20:00 | GOES-19 | SÃO FÉLIX DO XINGU | PARÁ | Brasil | 1507300 | 15 | 33 | nan | nan | nan | Amazônia | 121.7 |
| d0a7238f-3155-320a-8c96-8fa961d4b223 | -4.1406 | -54.0353 | 2026-10-07 19:20:00 | GOES-19 | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | 49.9 |
| 2c562c1b-bb23-3ad5-8a26-3bf4edfcffc2 | -6.6753 | -44.9674 | 2026-10-07 19:20:00 | GOES-19 | MIRADOR | MARANHÃO | Brasil | 2106706 | 21 | 33 | nan | nan | nan | Cerrado | 68.8 |
| 7b401cd5-2cca-3fac-bd77-866e33f6b207 | -6.6039 | -53.0116 | 2026-10-07 19:20:00 | GOES-19 | SÃO FÉLIX DO XINGU | PARÁ | Brasil | 1507300 | 15 | 33 | nan | nan | nan | Amazônia | 126.6 |
| e13a6ccb-e9b6-30c3-a089-7ee5529edbe0 | -6.0447 | -53.49 | 2026-10-07 19:20:00 | GOES-19 | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 77.0 |
| 955791d7-af98-39a5-9754-c99352a10237 | -3.3134 | -53.8592 | 2026-10-07 19:20:00 | GOES-19 | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | 203.6 |
| d6c3a0dd-3433-32f2-9920-1fe0c63fd88d | -5.4958 | -42.8413 | 2026-10-07 19:20:00 | GOES-19 | TERESINA | PIAUÍ | Brasil | 2211001 | 22 | 33 | nan | nan | nan | Caatinga | 171.8 |
| b7f7dbe4-cb7d-36c8-a826-46af247039c4 | -5.2092 | -48.3476 | 2026-10-07 19:20:00 | GOES-19 | SÃO SEBASTIÃO DO TOCANTINS | TOCANTINS | Brasil | 1720309 | 17 | 33 | nan | nan | nan | Amazônia | 62.4 |
| 5c6d13fc-ac6b-35c7-a222-35b64985ddc6 | -7.1825 | -52.6283 | 2026-10-07 19:20:00 | GOES-19 | SÃO FÉLIX DO XINGU | PARÁ | Brasil | 1507300 | 15 | 33 | nan | nan | nan | Amazônia | 142.7 |
| b84d8bdb-26a6-33c8-a8f0-d6dc9ee00b22 | -3.4245 | -49.2648 | 2026-10-07 19:20:00 | GOES-19 | BREU BRANCO | PARÁ | Brasil | 1501782 | 15 | 33 | nan | nan | nan | Amazônia | 128.1 |
| 6f196a3b-3c23-314c-9e01-81dc27396564 | -5.2274 | -48.4113 | 2026-10-07 19:20:00 | GOES-19 | SÃO SEBASTIÃO DO TOCANTINS | TOCANTINS | Brasil | 1720309 | 17 | 33 | nan | nan | nan | Amazônia | 59.3 |
| f317c3d3-530d-35b3-8e56-cba70ddafca7 | -3.4762 | -50.0883 | 2026-10-07 19:20:00 | GOES-19 | PACAJÁ | PARÁ | Brasil | 1505486 | 15 | 33 | nan | nan | nan | Amazônia | 196.1 |
| d231725a-ec40-3431-81ae-6fb395c6e5ac | -3.2957 | -49.1202 | 2026-10-07 19:20:00 | GOES-19 | MOJU | PARÁ | Brasil | 1504703 | 15 | 33 | nan | nan | nan | Amazônia | 61.1 |
| 14b380b5-f9e0-34dd-aab4-ead98a05be41 | -3.1951 | -42.9538 | 2026-10-07 19:20:00 | GOES-19 | SANTA QUITÉRIA DO MARANHÃO | MARANHÃO | Brasil | 2110104 | 21 | 33 | nan | nan | nan | Cerrado | 137.5 |
| e5a2ff12-4a05-3999-81d6-a60013d36847 | -8.5368 | -67.0135 | 2026-10-07 19:20:00 | GOES-19 | LÁBREA | AMAZONAS | Brasil | 1302405 | 13 | 33 | nan | nan | nan | Amazônia | 174.4 |
| f46bddf9-1b42-341a-80c6-1071f93c3ed3 | -6.1244 | -47.9227 | 2026-10-07 19:20:00 | GOES-19 | CACHOEIRINHA | TOCANTINS | Brasil | 1703826 | 17 | 33 | nan | nan | nan | Cerrado | 70.8 |
| e5fa1245-aeab-37d8-a755-05a425c8dc53 | -11.7335 | -43.649 | 2026-10-07 19:20:00 | GOES-19 | BARRA | BAHIA | Brasil | 2902708 | 29 | 33 | nan | nan | nan | Cerrado | 95.4 |
| c81fba83-c8f8-38ca-9540-450d1244f7e6 | -5.2461 | -48.3887 | 2026-10-07 19:20:00 | GOES-19 | SÃO SEBASTIÃO DO TOCANTINS | TOCANTINS | Brasil | 1720309 | 17 | 33 | nan | nan | nan | Amazônia | 49.8 |
| 89e12207-d873-3f25-840e-e1d8453aabab | -8.5552 | -67.0315 | 2026-10-07 19:20:00 | GOES-19 | LÁBREA | AMAZONAS | Brasil | 1302405 | 13 | 33 | nan | nan | nan | Amazônia | 113.9 |
| da8021e3-02c9-3e8a-827d-81e42a99c499 | -9.5004 | -66.7831 | 2026-10-07 19:20:00 | GOES-19 | LÁBREA | AMAZONAS | Brasil | 1302405 | 13 | 33 | nan | nan | nan | Amazônia | 97.9 |
| 1f0a0f96-6ea8-3f26-a935-ab55f27f0438 | -0.5993 | -49.4293 | 2026-10-07 19:20:00 | GOES-19 | SANTA CRUZ DO ARARI | PARÁ | Brasil | 1506401 | 15 | 33 | nan | nan | nan | Amazônia | 104.6 |
| 5aaed4c5-46c3-32a8-8c8a-cad4228415ec | -3.1788 | -50.5388 | 2026-10-07 19:20:00 | GOES-19 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 75.2 |
| b0547b59-2e8e-3956-8f85-60e251edfea4 | -5.496 | -42.8178 | 2026-10-07 19:20:00 | GOES-19 | NAZÁRIA | PIAUÍ | Brasil | 2206720 | 22 | 33 | nan | nan | nan | Caatinga | 66.8 |
| 50453811-46e9-365d-841b-f3c3a6264fde | -3.1972 | -50.5592 | 2026-10-07 19:20:00 | GOES-19 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 345.3 |
| f7acb4fa-9c2c-391d-890e-5797af3e75a6 | -3.2214 | -53.8818 | 2026-10-07 19:20:00 | GOES-19 | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | 81.7 |
| fcd4fc14-ab87-39af-8ea6-772f086cbd01 | -11.7143 | -43.652 | 2026-10-07 19:20:00 | GOES-19 | BARRA | BAHIA | Brasil | 2902708 | 29 | 33 | nan | nan | nan | Cerrado | 128.4 |
| 82e6e730-8269-3cb0-a8e2-38173722ad60 | -9.0406 | -65.9401 | 2026-10-07 19:20:00 | GOES-19 | LÁBREA | AMAZONAS | Brasil | 1302405 | 13 | 33 | nan | nan | nan | Amazônia | 148.3 |
| f77c269c-6c98-361c-8201-3bb1607738ab | -4.2859 | -50.7916 | 2026-10-07 19:20:00 | GOES-19 | NOVO REPARTIMENTO | PARÁ | Brasil | 1505064 | 15 | 33 | nan | nan | nan | Amazônia | 49.7 |
| d2a5b96f-8a8c-3d27-b639-555dc6032ab5 | -8.5367 | -67.032 | 2026-10-07 19:20:00 | GOES-19 | LÁBREA | AMAZONAS | Brasil | 1302405 | 13 | 33 | nan | nan | nan | Amazônia | 118.3 |
| 8534c8fe-21f1-37bf-9ddd-04faaa93d11d | -8.2184 | -46.3396 | 2026-10-07 19:20:00 | GOES-19 | BALSAS | MARANHÃO | Brasil | 2101400 | 21 | 33 | nan | nan | nan | Cerrado | 111.7 |
| 31f54284-4394-3e5c-8910-1e1709118a53 | -7.3747 | -46.2161 | 2026-10-07 19:20:00 | GOES-19 | RIACHÃO | MARANHÃO | Brasil | 2109502 | 21 | 33 | nan | nan | nan | Cerrado | 61.0 |
| a4b131e8-ae09-33ce-8d50-55f1b0f6d655 | -9.475 | -64.3525 | 2026-10-07 19:20:00 | GOES-19 | PORTO VELHO | RONDÔNIA | Brasil | 1100205 | 11 | 33 | nan | nan | nan | Amazônia | 217.7 |
| 8ccaf346-3388-3f59-86ac-5332f1d3be90 | -3.1697 | -58.6244 | 2026-10-07 19:20:00 | GOES-19 | ITACOATIARA | AMAZONAS | Brasil | 1301902 | 13 | 33 | nan | nan | nan | Amazônia | 99.0 |
| c0baa273-03e5-335f-b922-bbcd17f6a985 | -2.9327 | -58.3204 | 2026-10-07 19:20:00 | GOES-19 | SILVES | AMAZONAS | Brasil | 1304005 | 13 | 33 | nan | nan | nan | Amazônia | 131.7 |
| 45aa2072-a41b-365e-a791-ae8b14a9b688 | -9.4751 | -64.3336 | 2026-10-07 19:20:00 | GOES-19 | PORTO VELHO | RONDÔNIA | Brasil | 1100205 | 11 | 33 | nan | nan | nan | Amazônia | 99.3 |
| fdbd43ce-5f0e-3230-ae5b-06db146af750 | -3.5862 | -54.6541 | 2026-10-07 19:20:00 | GOES-19 | PLACAS | PARÁ | Brasil | 1505650 | 15 | 33 | nan | nan | nan | Amazônia | 347.7 |
| 85e4e247-ff02-3c40-8650-af2eb5ce631b | -6.1482 | -51.9477 | 2026-10-07 19:20:00 | GOES-19 | SÃO FÉLIX DO XINGU | PARÁ | Brasil | 1507300 | 15 | 33 | nan | nan | nan | Amazônia | 119.3 |
| 9166443d-6d4c-37c1-9e42-9f13af75cdff | -16.0101 | -43.5966 | 2026-10-07 19:20:00 | GOES-19 | CAPITÃO ENÉAS | MINAS GERAIS | Brasil | 3112703 | 31 | 33 | nan | nan | nan | Cerrado | 101.2 |
| a05f25b1-9833-3564-9423-85e3ffb4a3ae | -3.1102 | -54.146 | 2026-10-07 19:20:00 | GOES-19 | SANTARÉM | PARÁ | Brasil | 1506807 | 15 | 33 | nan | nan | nan | Amazônia | 197.2 |
| 335684fa-c495-3a95-b374-c0d1ebe8f4b0 | -4.2744 | -46.3846 | 2026-10-07 19:20:00 | GOES-19 | BURITICUPU | MARANHÃO | Brasil | 2102325 | 21 | 33 | nan | nan | nan | Amazônia | 189.1 |
| 17e09776-fec4-374b-970d-0ff1e673c6a8 | -9.96 | -43.481 | 2026-10-07 19:20:00 | GOES-19 | PILÃO ARCADO | BAHIA | Brasil | 2924405 | 29 | 33 | nan | nan | nan | Cerrado | 135.9 |
| 1213462b-318b-361c-b197-9084af51b57c | -3.1787 | -50.5597 | 2026-10-07 19:20:00 | GOES-19 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 146.3 |
| f6d6564d-a77e-3d28-b82d-676bf260a3d1 | -4.067 | -54.0378 | 2026-10-07 19:20:00 | GOES-19 | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | 70.1 |
| 60d767be-f2c5-3c2f-8f14-0b90b856ff7d | -3.5873 | -54.3739 | 2026-10-07 19:20:00 | GOES-19 | PLACAS | PARÁ | Brasil | 1505650 | 15 | 33 | nan | nan | nan | Amazônia | 69.2 |
| c5b7173c-ebca-3835-a624-450ee61c9a7a | 1.3347 | -50.8294 | 2026-10-07 19:20:00 | GOES-19 | TARTARUGALZINHO | AMAPÁ | Brasil | 1600709 | 16 | 33 | nan | nan | nan | Amazônia | 59.2 |
| bcc9078c-3d84-376b-b0a1-78d86e722740 | 1.7488 | -55.5861 | 2026-10-07 19:20:00 | GOES-19 | ÓBIDOS | PARÁ | Brasil | 1505106 | 15 | 33 | nan | nan | nan | Amazônia | 71.5 |
| 78caa0b0-21f5-3a86-985a-83c9f4ae9c14 | -8.5184 | -66.9954 | 2026-10-07 19:20:00 | GOES-19 | LÁBREA | AMAZONAS | Brasil | 1302405 | 13 | 33 | nan | nan | nan | Amazônia | 114.7 |
| 9c23e1a4-3765-3624-a7f1-d3faf0efa43c | -5.372 | -44.1751 | 2026-10-07 19:20:00 | GOES-19 | GOVERNADOR EUGÊNIO BARROS | MARANHÃO | Brasil | 2104602 | 21 | 33 | nan | nan | nan | Cerrado | 183.7 |
| d1f9f35b-99be-33f8-b8ed-e1747fbbd4c1 | -6.0075 | -53.5122 | 2026-10-07 19:20:00 | GOES-19 | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 67.1 |
| fbecdfb9-7fe6-3526-bd9b-bb0c7cb3aeb0 | -6.5853 | -53.0127 | 2026-10-07 19:20:00 | GOES-19 | SÃO FÉLIX DO XINGU | PARÁ | Brasil | 1507300 | 15 | 33 | nan | nan | nan | Amazônia | 109.4 |
| fadfb4bb-dfe4-3b7d-8477-a485db4d9a51 | -3.2398 | -53.8813 | 2026-10-07 19:20:00 | GOES-19 | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | 47.5 |
| 8619dc55-5c4b-3ae8-bf5f-96bbcd4dec7f | -6.6599 | -52.9675 | 2026-10-07 19:20:00 | GOES-19 | SÃO FÉLIX DO XINGU | PARÁ | Brasil | 1507300 | 15 | 33 | nan | nan | nan | Amazônia | 99.1 |
| ba6deb83-a8c9-3867-ae6d-bf4b4a9fe5c4 | -5.9514 | -46.3504 | 2026-10-07 19:20:00 | GOES-19 | GRAJAÚ | MARANHÃO | Brasil | 2104800 | 21 | 33 | nan | nan | nan | Cerrado | 63.7 |
| 07607feb-13ee-38c5-be0f-fb1ab9a192e8 | -3.5691 | -54.3143 | 2026-10-07 19:20:00 | GOES-19 | PLACAS | PARÁ | Brasil | 1505650 | 15 | 33 | nan | nan | nan | Amazônia | 48.7 |
| d280edf5-f023-338c-95af-088ec78eb08f | -8.6106 | -67.0486 | 2026-10-07 19:20:00 | GOES-19 | LÁBREA | AMAZONAS | Brasil | 1302405 | 13 | 33 | nan | nan | nan | Amazônia | 170.1 |
| 530874a2-e8ba-3c1d-9245-c797ae8caf68 | -3.4761 | -50.1094 | 2026-10-07 19:20:00 | GOES-19 | PACAJÁ | PARÁ | Brasil | 1505486 | 15 | 33 | nan | nan | nan | Amazônia | 54.3 |
| db124329-822d-3dfd-9341-fa550f9fbf24 | -3.6603 | -54.512 | 2026-10-07 19:20:00 | GOES-19 | PLACAS | PARÁ | Brasil | 1505650 | 15 | 33 | nan | nan | nan | Amazônia | 75.2 |
| 7db61e4e-bfbd-3ca2-8285-0113d85e7c94 | -4.7585 | -55.7308 | 2026-10-07 19:20:00 | GOES-19 | TRAIRÃO | PARÁ | Brasil | 1508050 | 15 | 33 | nan | nan | nan | Amazônia | 70.0 |
| a87f7b92-2509-3e34-83c3-9ce97ef1909e | -8.5551 | -67.0686 | 2026-10-07 19:20:00 | GOES-19 | BOCA DO ACRE | AMAZONAS | Brasil | 1300706 | 13 | 33 | nan | nan | nan | Amazônia | 107.9 |
| f30999de-d2c0-33c1-b221-fe20460ffbcb | -6.5852 | -53.0331 | 2026-10-07 19:20:00 | GOES-19 | SÃO FÉLIX DO XINGU | PARÁ | Brasil | 1507300 | 15 | 33 | nan | nan | nan | Amazônia | 105.0 |
| a520a903-634a-3de9-8034-bbf58babf49f | -2.6859 | -49.0539 | 2026-10-07 19:20:00 | GOES-19 | MOJU | PARÁ | Brasil | 1504703 | 15 | 33 | nan | nan | nan | Amazônia | 100.1 |
| 6dc6eca2-fd05-3124-955a-021c1ed35fe9 | -8.2184 | -46.3396 | 2026-10-07 19:30:00 | GOES-19 | BALSAS | MARANHÃO | Brasil | 2101400 | 21 | 33 | nan | nan | nan | Cerrado | 220.3 |
| 776cecd5-d7a1-3fd2-be24-4ac6e51857f8 | -3.5866 | -54.5542 | 2026-10-07 19:30:00 | GOES-19 | PLACAS | PARÁ | Brasil | 1505650 | 15 | 33 | nan | nan | nan | Amazônia | 74.7 |
| 0972af03-7e75-37b1-880f-ae1d4a1f3207 | -8.629 | -67.0667 | 2026-10-07 19:30:00 | GOES-19 | LÁBREA | AMAZONAS | Brasil | 1302405 | 13 | 33 | nan | nan | nan | Amazônia | 124.5 |
| 64920fab-63d4-3f98-897a-9f81e7dbdea8 | -3.383 | -42.7111 | 2026-10-07 19:30:00 | GOES-19 | SANTA QUITÉRIA DO MARANHÃO | MARANHÃO | Brasil | 2110104 | 21 | 33 | nan | nan | nan | Cerrado | 82.3 |
| f5bbaef8-49b2-3207-aa42-52128735afba | -5.9699 | -53.5953 | 2026-10-07 19:30:00 | GOES-19 | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 73.0 |
| 4d92787e-f82a-3294-9c80-2ee0f3d7b580 | -2.9271 | -53.9496 | 2026-10-07 19:30:00 | GOES-19 | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | 61.2 |


[Clique aqui para ver as próximas entradas](README260.md)
