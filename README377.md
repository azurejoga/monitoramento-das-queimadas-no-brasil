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

## Dados Diários - Página 377

| ID | Latitude | Longitude | Data/Hora GMT | Satélite | Município | Estado | País | Município ID | Estado ID | País ID | Dias sem Chuva | Precipitação | Risco de Fogo | Bioma | FRP |
|----|----------|-----------|---------------|----------|-----------|--------|------|--------------|-----------|---------|----------------|--------------|----------------|-------|-----|
| 38cf339d-d0d1-33e4-8985-8a20bed2a9a2 | -6.45195 | -52.69518 | 2026-10-08 16:39:00 | NOAA-20 | SÃO FÉLIX DO XINGU | PARÁ | Brasil | 1507300 | 15 | 33 | nan | nan | nan | Amazônia | 8.1 |
| 9cf7ccdf-0bb7-360d-8fa7-389d080f659f | -3.02346 | -43.34341 | 2026-10-08 16:39:00 | NOAA-20 | BELÁGUA | MARANHÃO | Brasil | 2101731 | 21 | 33 | nan | nan | nan | Cerrado | 12.7 |
| f441cbf6-f864-3fbf-9666-4f367520f74e | -3.73739 | -51.20369 | 2026-10-08 16:39:00 | NOAA-20 | PACAJÁ | PARÁ | Brasil | 1505486 | 15 | 33 | nan | nan | nan | Amazônia | 14.9 |
| 5fc1693d-0e07-3e72-8455-00930438a620 | -3.15206 | -43.04116 | 2026-10-08 16:39:00 | NOAA-20 | SANTA QUITÉRIA DO MARANHÃO | MARANHÃO | Brasil | 2110104 | 21 | 33 | nan | nan | nan | Cerrado | 20.1 |
| d4a42b8b-2136-3b42-8703-8177c95446e2 | -2.4988 | -58.07903 | 2026-10-08 16:39:00 | NOAA-20 | SÃO SEBASTIÃO DO UATUMÃ | AMAZONAS | Brasil | 1303957 | 13 | 33 | nan | nan | nan | Amazônia | 9.6 |
| af36cbc2-74e9-3207-bfa7-5e506dd109b2 | -4.96358 | -55.12205 | 2026-10-08 16:39:00 | NOAA-20 | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 4.6 |
| aaa16f06-011f-3be2-aabc-cfde0cde5443 | -3.20029 | -41.14093 | 2026-10-08 16:39:00 | NOAA-20 | GRANJA | CEARÁ | Brasil | 2304707 | 23 | 33 | nan | nan | nan | Caatinga | 7.4 |
| 9a42d25e-73aa-3740-ba61-743bc746557f | -3.11519 | -41.1696 | 2026-10-08 16:39:00 | NOAA-20 | CHAVAL | CEARÁ | Brasil | 2303907 | 23 | 33 | nan | nan | nan | Caatinga | 7.8 |
| 0cab0805-50d4-3a47-9cc5-176451ca5c5d | -3.05364 | -53.95502 | 2026-10-08 16:39:00 | NOAA-20 | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | 10.6 |
| 4819a95f-2d08-393c-8389-f5b81bb943c4 | -2.89192 | -54.18522 | 2026-10-08 16:39:00 | NOAA-20 | SANTARÉM | PARÁ | Brasil | 1506807 | 15 | 33 | nan | nan | nan | Amazônia | 16.5 |
| 05800798-d246-3255-8afb-55d5f442abe0 | -5.02248 | -42.44369 | 2026-10-08 16:39:00 | NOAA-20 | ALTOS | PIAUÍ | Brasil | 2200400 | 22 | 33 | nan | nan | nan | Caatinga | 25.3 |
| daefb68e-eb64-3cf8-9505-daa65f89e196 | -4.06102 | -55.32962 | 2026-10-08 16:39:00 | NOAA-20 | AVEIRO | PARÁ | Brasil | 1501006 | 15 | 33 | nan | nan | nan | Amazônia | 5.1 |
| d83ce853-cec7-3b3c-94b8-c7cdd6b0599f | -3.00278 | -53.9021 | 2026-10-08 16:39:00 | NOAA-20 | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | 150.4 |
| cd309b74-21d4-3e48-8366-71e91a1f7259 | -7.08209 | -52.68353 | 2026-10-08 16:39:00 | NOAA-20 | SÃO FÉLIX DO XINGU | PARÁ | Brasil | 1507300 | 15 | 33 | nan | nan | nan | Amazônia | 34.8 |
| c4c76e18-e223-3e04-9898-514173c80ed2 | -6.67958 | -52.03066 | 2026-10-08 16:39:00 | NOAA-20 | SÃO FÉLIX DO XINGU | PARÁ | Brasil | 1507300 | 15 | 33 | nan | nan | nan | Amazônia | 6.1 |
| c0b97a94-a208-3970-aa02-2877d9dd9a49 | -4.08602 | -44.11505 | 2026-10-08 16:39:00 | NOAA-20 | COROATÁ | MARANHÃO | Brasil | 2103604 | 21 | 33 | nan | nan | nan | Cerrado | 35.6 |
| 1bd66989-3470-33d0-a0f0-3fb03da7cde3 | -6.0473 | -53.49051 | 2026-10-08 16:39:00 | NOAA-20 | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 7.5 |
| 3baa0234-2c27-3448-bdd8-aed6d493c41a | -2.85835 | -57.46539 | 2026-10-08 16:39:00 | NOAA-20 | BARREIRINHA | AMAZONAS | Brasil | 1300508 | 13 | 33 | nan | nan | nan | Amazônia | 7.1 |
| 0c0bff53-28b8-3ea5-a547-a24863012542 | -4.74781 | -40.50008 | 2026-10-08 16:39:00 | NOAA-20 | NOVA RUSSAS | CEARÁ | Brasil | 2309300 | 23 | 33 | nan | nan | nan | Caatinga | 5.9 |
| 7210723b-deed-332d-99b2-5b32b30f99fb | -6.18177 | -52.83189 | 2026-10-08 16:39:00 | NOAA-20 | SÃO FÉLIX DO XINGU | PARÁ | Brasil | 1507300 | 15 | 33 | nan | nan | nan | Amazônia | 10.4 |
| 1ab8a781-3c04-376a-8cbd-18c9fd3a94cd | -5.35016 | -45.68923 | 2026-10-08 16:39:00 | NOAA-20 | JENIPAPO DOS VIEIRAS | MARANHÃO | Brasil | 2105476 | 21 | 33 | nan | nan | nan | Cerrado | 5.5 |
| d8ac6085-b53d-38e2-9119-ad794437350a | -2.99273 | -54.07386 | 2026-10-08 16:39:00 | NOAA-20 | SANTARÉM | PARÁ | Brasil | 1506807 | 15 | 33 | nan | nan | nan | Amazônia | 9.4 |
| 367d82f9-f859-36fc-85b2-3cef0a57479c | -0.08735 | -49.48114 | 2026-10-08 16:39:00 | NOAA-20 | CHAVES | PARÁ | Brasil | 1502509 | 15 | 33 | nan | nan | nan | Amazônia | 27.0 |
| 0abc74de-6d0d-3b4a-a6eb-88cfe7899539 | -6.16662 | -53.43199 | 2026-10-08 16:39:00 | NOAA-20 | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 26.2 |
| e13bd32a-afb8-3044-85b6-27a8aaa19ca4 | -3.18133 | -58.64355 | 2026-10-08 16:39:00 | NOAA-20 | ITACOATIARA | AMAZONAS | Brasil | 1301902 | 13 | 33 | nan | nan | nan | Amazônia | 45.7 |
| 630439a2-d8bc-34e2-b893-cc267d8dc96d | -6.61968 | -51.15742 | 2026-10-08 16:39:00 | NOAA-20 | SÃO FÉLIX DO XINGU | PARÁ | Brasil | 1507300 | 15 | 33 | nan | nan | nan | Amazônia | 4.2 |
| 40ce9570-b828-39d3-8f9d-2c1523d20be9 | -4.45746 | -55.40213 | 2026-10-08 16:39:00 | NOAA-20 | RURÓPOLIS | PARÁ | Brasil | 1506195 | 15 | 33 | nan | nan | nan | Amazônia | 6.7 |
| 21cd3d88-393e-3317-9d7e-23ec1d1c2fda | -3.89797 | -44.13174 | 2026-10-08 16:39:00 | NOAA-20 | COROATÁ | MARANHÃO | Brasil | 2103604 | 21 | 33 | nan | nan | nan | Cerrado | 14.9 |
| f199ff1f-18df-3974-891c-2f9df14f51a9 | -3.66149 | -59.15905 | 2026-10-08 16:39:00 | NOAA-20 | AUTAZES | AMAZONAS | Brasil | 1300300 | 13 | 33 | nan | nan | nan | Amazônia | 11.4 |
| 7cb74928-f9b0-3e21-920f-97eb99bc3118 | -7.22978 | -55.09578 | 2026-10-08 16:39:00 | NOAA-20 | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 12.9 |
| 6aa3fead-191f-3108-81d2-d3ff3f16f49b | -5.95172 | -45.69576 | 2026-10-08 16:39:00 | NOAA-20 | GRAJAÚ | MARANHÃO | Brasil | 2104800 | 21 | 33 | nan | nan | nan | Cerrado | 20.1 |
| 24f0f069-44a9-30c5-81ac-b673e9ff8c80 | -2.50543 | -56.12657 | 2026-10-08 16:39:00 | NOAA-20 | JURUTI | PARÁ | Brasil | 1503903 | 15 | 33 | nan | nan | nan | Amazônia | 7.8 |
| 285ac716-3a5c-3437-8d15-4ee03ce03c4d | -1.41405 | -52.72422 | 2026-10-08 16:39:00 | NOAA-20 | ALMEIRIM | PARÁ | Brasil | 1500503 | 15 | 33 | nan | nan | nan | Amazônia | 9.8 |
| c6f01a7e-eb4c-3554-a424-da0d33905c8b | -1.15335 | -54.21672 | 2026-10-08 16:39:00 | NOAA-20 | MONTE ALEGRE | PARÁ | Brasil | 1504802 | 15 | 33 | nan | nan | nan | Amazônia | 73.7 |
| e4f145e0-cda8-3489-9e89-1b8948726685 | -4.93831 | -55.80826 | 2026-10-08 16:39:00 | NOAA-20 | TRAIRÃO | PARÁ | Brasil | 1508050 | 15 | 33 | nan | nan | nan | Amazônia | 8.7 |
| 5c6feaf3-0e49-3cf2-93d6-76c06361b56e | -1.33642 | -52.4425 | 2026-10-08 16:39:00 | NOAA-20 | ALMEIRIM | PARÁ | Brasil | 1500503 | 15 | 33 | nan | nan | nan | Amazônia | 7.6 |
| 45edcda8-d701-3a9a-892e-1c096e15d9c7 | -3.08014 | -57.50271 | 2026-10-08 16:39:00 | NOAA-20 | BOA VISTA DO RAMOS | AMAZONAS | Brasil | 1300680 | 13 | 33 | nan | nan | nan | Amazônia | 5.9 |
| b5936c5e-d86d-37ef-9c2f-fe4663f80ca9 | -3.40872 | -58.00868 | 2026-10-08 16:39:00 | NOAA-20 | MAUÉS | AMAZONAS | Brasil | 1302900 | 13 | 33 | nan | nan | nan | Amazônia | 11.3 |
| c643a0ec-5530-3927-b59b-7e1af092b4b9 | -4.37097 | -55.32299 | 2026-10-08 16:39:00 | NOAA-20 | RURÓPOLIS | PARÁ | Brasil | 1506195 | 15 | 33 | nan | nan | nan | Amazônia | 16.8 |
| b6fb5811-96d3-332a-ad8c-b4a2e20fecee | -3.39565 | -58.00566 | 2026-10-08 16:39:00 | NOAA-20 | MAUÉS | AMAZONAS | Brasil | 1302900 | 13 | 33 | nan | nan | nan | Amazônia | 5.9 |
| c983557b-75e5-3b7d-b45c-dbc2652d9223 | -6.14886 | -52.64365 | 2026-10-08 16:39:00 | NOAA-20 | SÃO FÉLIX DO XINGU | PARÁ | Brasil | 1507300 | 15 | 33 | nan | nan | nan | Amazônia | 17.8 |
| 8110cdee-b634-30df-b081-2881eba4f303 | -2.07422 | -46.57287 | 2026-10-08 16:39:00 | NOAA-20 | CACHOEIRA DO PIRIÁ | PARÁ | Brasil | 1501956 | 15 | 33 | nan | nan | nan | Amazônia | 10.8 |
| 5bbd4d21-66de-3342-ac1e-6ff040b70c83 | -6.22946 | -52.87305 | 2026-10-08 16:39:00 | NOAA-20 | SÃO FÉLIX DO XINGU | PARÁ | Brasil | 1507300 | 15 | 33 | nan | nan | nan | Amazônia | 34.0 |
| 621f01ac-ce1e-3dae-88b0-318d714dd17e | -5.21432 | -44.27604 | 2026-10-08 16:39:00 | NOAA-20 | GONÇALVES DIAS | MARANHÃO | Brasil | 2104404 | 21 | 33 | nan | nan | nan | Cerrado | 1.8 |
| 37c7a51a-b08b-3b7d-8b32-07984beef8be | -4.69007 | -42.92355 | 2026-10-08 16:39:00 | NOAA-20 | UNIÃO | PIAUÍ | Brasil | 2211100 | 22 | 33 | nan | nan | nan | Cerrado | 14.4 |
| 127691b9-1ff1-360f-afc4-b4b044fc33f7 | -3.53106 | -59.55786 | 2026-10-08 16:39:00 | NOAA-20 | CAREIRO DA VÁRZEA | AMAZONAS | Brasil | 1301159 | 13 | 33 | nan | nan | nan | Amazônia | 31.8 |
| 4ea37b96-36c0-3e12-b964-d9d9bd0ec3c7 | -3.73827 | -45.07907 | 2026-10-08 16:39:00 | NOAA-20 | PIO XII | MARANHÃO | Brasil | 2108702 | 21 | 33 | nan | nan | nan | Amazônia | 1.4 |
| 438e2bef-babd-3508-af29-cccf3d9b367b | -2.08022 | -45.857 | 2026-10-08 16:39:00 | NOAA-20 | GOVERNADOR NUNES FREIRE | MARANHÃO | Brasil | 2104677 | 21 | 33 | nan | nan | nan | Amazônia | 6.4 |
| 2b5804ab-d7cb-3765-a242-8c1e5ddc9a24 | -3.51639 | -59.21643 | 2026-10-08 16:39:00 | NOAA-20 | AUTAZES | AMAZONAS | Brasil | 1300300 | 13 | 33 | nan | nan | nan | Amazônia | 5.7 |
| f830df9d-bc4c-3e6c-b851-6256a3d5adf5 | -1.71817 | -48.24883 | 2026-10-08 16:39:00 | NOAA-20 | ACARÁ | PARÁ | Brasil | 1500206 | 15 | 33 | nan | nan | nan | Amazônia | 9.5 |
| 111bb610-1418-322c-b1c1-c90357d4606a | -5.74018 | -53.4556 | 2026-10-08 16:39:00 | NOAA-20 | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 10.8 |
| 09df1b75-7786-3d48-97cf-81908d141fe8 | -5.78201 | -45.38548 | 2026-10-08 16:39:00 | NOAA-20 | BARRA DO CORDA | MARANHÃO | Brasil | 2101608 | 21 | 33 | nan | nan | nan | Cerrado | 39.0 |
| d2abd6d8-ba57-3385-a52d-5509f68afc04 | -6.19779 | -51.43376 | 2026-10-08 16:39:00 | NOAA-20 | SÃO FÉLIX DO XINGU | PARÁ | Brasil | 1507300 | 15 | 33 | nan | nan | nan | Amazônia | 31.4 |
| 155c60a7-93f0-3dda-aea0-d5351650f666 | -1.81831 | -57.1062 | 2026-10-08 16:39:00 | NOAA-20 | NHAMUNDÁ | AMAZONAS | Brasil | 1303007 | 13 | 33 | nan | nan | nan | Amazônia | 8.0 |
| 4d489b6a-7b2a-39bb-8cee-b78e175226fa | -3.8136 | -44.59661 | 2026-10-08 16:39:00 | NOAA-20 | MATÕES DO NORTE | MARANHÃO | Brasil | 2106631 | 21 | 33 | nan | nan | nan | Cerrado | 22.1 |
| 444402ae-72b4-33e1-abbb-d713ce54aca4 | -1.89531 | -54.39066 | 2026-10-08 16:39:00 | NOAA-20 | MONTE ALEGRE | PARÁ | Brasil | 1504802 | 15 | 33 | nan | nan | nan | Amazônia | 9.7 |
| 2f5e6109-0567-37ca-8db7-9a84d9b0c783 | -2.56116 | -57.43063 | 2026-10-08 16:39:00 | NOAA-20 | URUCURITUBA | AMAZONAS | Brasil | 1304401 | 13 | 33 | nan | nan | nan | Amazônia | 7.9 |
| 000ba9d8-c0dd-304b-a449-a26b1793d63d | -7.22846 | -55.08621 | 2026-10-08 16:39:00 | NOAA-20 | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 5.9 |
| 76a7da69-8ffd-3783-a8b4-8726dab2e593 | -7.60622 | -55.71568 | 2026-10-08 16:39:00 | NOAA-20 | NOVO PROGRESSO | PARÁ | Brasil | 1505031 | 15 | 33 | nan | nan | nan | Amazônia | 11.9 |
| b368de0d-6a0a-38f0-90e4-e99167e4eb0a | -6.14593 | -45.12656 | 2026-10-08 16:39:00 | NOAA-20 | FERNANDO FALCÃO | MARANHÃO | Brasil | 2104081 | 21 | 33 | nan | nan | nan | Cerrado | 6.9 |
| 4928a3e7-96a5-3a62-a7c8-3f14bea1c498 | -3.77645 | -59.24549 | 2026-10-08 16:39:00 | NOAA-20 | AUTAZES | AMAZONAS | Brasil | 1300300 | 13 | 33 | nan | nan | nan | Amazônia | 11.6 |
| 53fa9b8d-8767-3b07-b2e5-1be15dbc348c | -6.38707 | -52.72761 | 2026-10-08 16:39:00 | NOAA-20 | SÃO FÉLIX DO XINGU | PARÁ | Brasil | 1507300 | 15 | 33 | nan | nan | nan | Amazônia | 8.2 |
| 9a5d8e79-5cf8-3e39-8fbf-623de67a6b7b | -5.34863 | -45.76741 | 2026-10-08 16:39:00 | NOAA-20 | JENIPAPO DOS VIEIRAS | MARANHÃO | Brasil | 2105476 | 21 | 33 | nan | nan | nan | Cerrado | 7.7 |
| 15b51d7a-f1d4-3249-9188-68e86010658c | -2.03004 | -57.05291 | 2026-10-08 16:39:00 | NOAA-20 | NHAMUNDÁ | AMAZONAS | Brasil | 1303007 | 13 | 33 | nan | nan | nan | Amazônia | 5.5 |
| b8544eba-70ba-34aa-b601-15cecfc1dc28 | -5.17697 | -42.68742 | 2026-10-08 16:39:00 | NOAA-20 | TERESINA | PIAUÍ | Brasil | 2211001 | 22 | 33 | nan | nan | nan | Cerrado | 11.3 |
| f0de1ee6-3dae-336d-b5f8-0da5af3ffd5d | -3.00293 | -54.06982 | 2026-10-08 16:39:00 | NOAA-20 | SANTARÉM | PARÁ | Brasil | 1506807 | 15 | 33 | nan | nan | nan | Amazônia | 15.1 |
| 546a4cd6-d4d7-328d-af18-167e9f3dcc82 | -6.85032 | -59.39162 | 2026-10-08 16:39:00 | NOAA-20 | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 20.4 |
| 35958d05-6c7b-33ae-aa20-d61c78919ad2 | -4.9227 | -55.85662 | 2026-10-08 16:39:00 | NOAA-20 | TRAIRÃO | PARÁ | Brasil | 1508050 | 15 | 33 | nan | nan | nan | Amazônia | 6.6 |
| 7037130a-bc41-3388-aaa6-05b077a91a64 | -4.36041 | -55.32436 | 2026-10-08 16:39:00 | NOAA-20 | RURÓPOLIS | PARÁ | Brasil | 1506195 | 15 | 33 | nan | nan | nan | Amazônia | 4.4 |
| 2949c9b7-99a2-38a4-a7ee-b1f914b3ac1b | -2.08625 | -46.58514 | 2026-10-08 16:39:00 | NOAA-20 | CACHOEIRA DO PIRIÁ | PARÁ | Brasil | 1501956 | 15 | 33 | nan | nan | nan | Amazônia | 20.5 |
| fb6700be-3a38-350f-9c1f-2dfe968dc031 | -3.06554 | -44.34158 | 2026-10-08 16:39:00 | NOAA-20 | BACABEIRA | MARANHÃO | Brasil | 2101251 | 21 | 33 | nan | nan | nan | Amazônia | 7.4 |
| c3eb4977-e14b-37e4-a173-1eccbaf56da3 | -3.11368 | -54.16301 | 2026-10-08 16:39:00 | NOAA-20 | SANTARÉM | PARÁ | Brasil | 1506807 | 15 | 33 | nan | nan | nan | Amazônia | 40.3 |
| 0a87ee55-8fe5-36e7-84cf-ec7eb9f417e8 | -2.89116 | -54.18015 | 2026-10-08 16:39:00 | NOAA-20 | SANTARÉM | PARÁ | Brasil | 1506807 | 15 | 33 | nan | nan | nan | Amazônia | 8.9 |
| 01d0de1b-9047-3452-a04a-24466c7c3c52 | -3.04883 | -57.47461 | 2026-10-08 16:39:00 | NOAA-20 | BOA VISTA DO RAMOS | AMAZONAS | Brasil | 1300680 | 13 | 33 | nan | nan | nan | Amazônia | 9.0 |
| 21906183-0067-3501-8f52-399b192abaa4 | -5.47832 | -44.6021 | 2026-10-08 16:39:00 | NOAA-20 | SANTA FILOMENA DO MARANHÃO | MARANHÃO | Brasil | 2109759 | 21 | 33 | nan | nan | nan | Cerrado | 11.5 |
| 24d2e9fe-17aa-3f1e-80fe-4e9f3a4dc602 | -4.79645 | -43.33458 | 2026-10-08 16:39:00 | NOAA-20 | CAXIAS | MARANHÃO | Brasil | 2103000 | 21 | 33 | nan | nan | nan | Cerrado | 7.4 |
| 2824dbb6-eb62-3b7f-a12f-6b794999a0b9 | -3.087 | -57.64993 | 2026-10-08 16:39:00 | NOAA-20 | BOA VISTA DO RAMOS | AMAZONAS | Brasil | 1300680 | 13 | 33 | nan | nan | nan | Amazônia | 6.6 |
| f6c1bcef-8ae5-387e-ba3a-d265194a48a9 | -2.8936 | -54.16405 | 2026-10-08 16:39:00 | NOAA-20 | SANTARÉM | PARÁ | Brasil | 1506807 | 15 | 33 | nan | nan | nan | Amazônia | 10.0 |
| 2bd1f71c-e008-34a9-b507-735cb7fda4b5 | -3.25797 | -57.87312 | 2026-10-08 16:39:00 | NOAA-20 | BOA VISTA DO RAMOS | AMAZONAS | Brasil | 1300680 | 13 | 33 | nan | nan | nan | Amazônia | 30.8 |
| 7843aa95-f9e7-375e-856f-018a904a636b | -2.75367 | -54.10956 | 2026-10-08 16:39:00 | NOAA-20 | PRAINHA | PARÁ | Brasil | 1506005 | 15 | 33 | nan | nan | nan | Amazônia | 11.2 |
| 4425520b-5eb3-3ce0-ac6e-df31692c7b1f | -3.2271 | -54.29915 | 2026-10-08 16:39:00 | NOAA-20 | MOJUÍ DOS CAMPOS | PARÁ | Brasil | 1504752 | 15 | 33 | nan | nan | nan | Amazônia | 9.8 |
| 39d5e4f9-37b0-381b-8935-a1e40f91888a | -5.70433 | -53.48319 | 2026-10-08 16:39:00 | NOAA-20 | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 31.9 |
| 7ba0741c-87d0-327e-83cd-5e0cc92682ef | -2.50108 | -56.66473 | 2026-10-08 16:39:00 | NOAA-20 | PARINTINS | AMAZONAS | Brasil | 1303403 | 13 | 33 | nan | nan | nan | Amazônia | 7.3 |
| beb4c8a6-f771-32bf-add0-2f3541987c47 | -5.88183 | -45.94823 | 2026-10-08 16:39:00 | NOAA-20 | GRAJAÚ | MARANHÃO | Brasil | 2104800 | 21 | 33 | nan | nan | nan | Cerrado | 9.0 |
| cddffce6-b2fd-3cbb-8a2e-bc07238ca329 | -5.88078 | -45.94133 | 2026-10-08 16:39:00 | NOAA-20 | GRAJAÚ | MARANHÃO | Brasil | 2104800 | 21 | 33 | nan | nan | nan | Cerrado | 3.9 |
| 1d8d1080-31ba-315e-a2c8-4741bb5e2783 | -3.0768 | -57.74836 | 2026-10-08 16:39:00 | NOAA-20 | BOA VISTA DO RAMOS | AMAZONAS | Brasil | 1300680 | 13 | 33 | nan | nan | nan | Amazônia | 20.1 |
| e1feb3dc-1d24-371b-a9cd-efaef19caa63 | -2.51625 | -57.24467 | 2026-10-08 16:39:00 | NOAA-20 | PARINTINS | AMAZONAS | Brasil | 1303403 | 13 | 33 | nan | nan | nan | Amazônia | 6.8 |
| 96af6b5d-f481-327e-b8e4-56c2f4f1fd48 | -2.43548 | -55.97148 | 2026-10-08 16:39:00 | NOAA-20 | JURUTI | PARÁ | Brasil | 1503903 | 15 | 33 | nan | nan | nan | Amazônia | 8.5 |
| fcfec8bc-20a6-3fd9-946c-55938308144e | -3.88904 | -41.59909 | 2026-10-08 16:39:00 | NOAA-20 | PIRACURUCA | PIAUÍ | Brasil | 2208304 | 22 | 33 | nan | nan | nan | Caatinga | 45.0 |
| d5245422-9802-3696-b130-bf69efe948ea | -2.43874 | -58.01542 | 2026-10-08 16:39:00 | NOAA-20 | SÃO SEBASTIÃO DO UATUMÃ | AMAZONAS | Brasil | 1303957 | 13 | 33 | nan | nan | nan | Amazônia | 5.8 |
| 88da2ebd-f716-3532-b6f8-6f224953ff7a | -4.36195 | -55.22163 | 2026-10-08 16:39:00 | NOAA-20 | RURÓPOLIS | PARÁ | Brasil | 1506195 | 15 | 33 | nan | nan | nan | Amazônia | 9.1 |
| 22b6f58b-085d-3b16-91cb-e8f448573534 | -6.14709 | -47.93278 | 2026-10-08 16:39:00 | NOAA-20 | CACHOEIRINHA | TOCANTINS | Brasil | 1703826 | 17 | 33 | nan | nan | nan | Cerrado | 9.8 |
| 51667062-65c6-38d7-891e-731df9c24602 | -5.72727 | -45.22927 | 2026-10-08 16:39:00 | NOAA-20 | BARRA DO CORDA | MARANHÃO | Brasil | 2101608 | 21 | 33 | nan | nan | nan | Cerrado | 3.4 |
| d82e8e1e-ebd6-3cb4-9843-b069a69e71a1 | -3.16893 | -50.45327 | 2026-10-08 16:39:00 | NOAA-20 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 13.6 |
| 5d90d7a4-5561-3629-b9c1-86ef25e6f5a4 | -3.67647 | -54.27096 | 2026-10-08 16:39:00 | NOAA-20 | PLACAS | PARÁ | Brasil | 1505650 | 15 | 33 | nan | nan | nan | Amazônia | 5.8 |
| 9933636f-1304-3472-8d41-e18dcb7c852c | -7.50333 | -54.9938 | 2026-10-08 16:39:00 | NOAA-20 | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 3.4 |
| 77aa5dd9-a8cc-3435-a2d0-06a3025e011d | -2.41709 | -56.85846 | 2026-10-08 16:39:00 | NOAA-20 | NHAMUNDÁ | AMAZONAS | Brasil | 1303007 | 13 | 33 | nan | nan | nan | Amazônia | 48.9 |
| b9b31f6a-6dde-35aa-a59f-c345c5860973 | -3.52765 | -59.3415 | 2026-10-08 16:39:00 | NOAA-20 | AUTAZES | AMAZONAS | Brasil | 1300300 | 13 | 33 | nan | nan | nan | Amazônia | 32.0 |
| c51b6483-0a3a-3834-a90f-31f52e5270df | -3.00271 | -57.74979 | 2026-10-08 16:39:00 | NOAA-20 | BOA VISTA DO RAMOS | AMAZONAS | Brasil | 1300680 | 13 | 33 | nan | nan | nan | Amazônia | 11.8 |
| e606e44f-0858-3189-9541-23f26dfedbda | -2.51247 | -47.37714 | 2026-10-08 16:39:00 | NOAA-20 | CAPITÃO POÇO | PARÁ | Brasil | 1502301 | 15 | 33 | nan | nan | nan | Amazônia | 6.7 |


[Clique aqui para ver as próximas entradas](README378.md)
