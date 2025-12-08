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

## Dados Diários - Página 4

| ID | Latitude | Longitude | Data/Hora GMT | Satélite | Município | Estado | País | Município ID | Estado ID | País ID | Dias sem Chuva | Precipitação | Risco de Fogo | Bioma | FRP |
|----|----------|-----------|---------------|----------|-----------|--------|------|--------------|-----------|---------|----------------|--------------|----------------|-------|-----|
| 637e8ebf-4659-38d8-a0f8-a1249371ffcd | -1.93808 | -46.35113 | 2025-12-08 04:44:00 | NOAA-21 | CACHOEIRA DO PIRIÁ | PARÁ | Brasil | 1501956 | 15 | 33 | nan | nan | nan | Amazônia | 2.2 |
| 25a30498-a4db-3d01-b0ab-caca053196e4 | 3.33887 | -51.31279 | 2025-12-08 04:44:00 | NOAA-21 | OIAPOQUE | AMAPÁ | Brasil | 1600501 | 16 | 33 | nan | nan | nan | Amazônia | 1.7 |
| e85d82a8-0d75-37ab-b365-7d389aad9f7d | -3.84945 | -47.82333 | 2025-12-08 04:44:00 | NOAA-21 | ULIANÓPOLIS | PARÁ | Brasil | 1508126 | 15 | 33 | nan | nan | nan | Amazônia | 1.9 |
| e8514bb9-7dc1-3a3c-85c0-5b726cd1148d | -1.1357 | -47.16733 | 2025-12-08 04:44:00 | NOAA-21 | CAPANEMA | PARÁ | Brasil | 1502202 | 15 | 33 | nan | nan | nan | Amazônia | 1.9 |
| 2a96a1ed-babb-3db8-98f7-884f7ef06715 | 3.29741 | -60.83294 | 2025-12-08 04:44:00 | NOAA-21 | BOA VISTA | RORAIMA | Brasil | 1400100 | 14 | 33 | nan | nan | nan | Amazônia | 2.8 |
| cb32aa22-c556-35a3-b014-0e6cddf847b5 | -0.31228 | -51.701 | 2025-12-08 04:44:00 | NOAA-21 | MAZAGÃO | AMAPÁ | Brasil | 1600402 | 16 | 33 | nan | nan | nan | Amazônia | 4.4 |
| 3313f31e-6d8e-3954-b299-c9ae02135591 | -1.01452 | -48.16088 | 2025-12-08 04:44:00 | NOAA-21 | VIGIA | PARÁ | Brasil | 1508209 | 15 | 33 | nan | nan | nan | Amazônia | 0.4 |
| 59abe82e-0089-31ca-ae84-4404bb66cabe | -1.11398 | -46.54676 | 2025-12-08 04:44:00 | NOAA-21 | AUGUSTO CORRÊA | PARÁ | Brasil | 1500909 | 15 | 33 | nan | nan | nan | Amazônia | 1.6 |
| 0970a811-c4d9-3c9f-9f60-eb1cbcaa5efd | -0.30657 | -51.6925 | 2025-12-08 04:44:00 | NOAA-21 | MAZAGÃO | AMAPÁ | Brasil | 1600402 | 16 | 33 | nan | nan | nan | Amazônia | 0.7 |
| 7aaf6241-5cb7-31d1-94c3-34b362f933ed | -2.50543 | -51.79787 | 2025-12-08 04:44:00 | NOAA-21 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 2.2 |
| e309f049-e83c-3d70-bcf7-259b1410ceb5 | -2.35871 | -47.68982 | 2025-12-08 04:44:00 | NOAA-21 | IPIXUNA DO PARÁ | PARÁ | Brasil | 1503457 | 15 | 33 | nan | nan | nan | Amazônia | 1.9 |
| 4050bc4d-b0dc-3e12-837b-4dcf84cca89c | 1.03231 | -50.00488 | 2025-12-08 04:44:00 | NOAA-21 | MACAPÁ | AMAPÁ | Brasil | 1600303 | 16 | 33 | nan | nan | nan | Amazônia | 0.5 |
| 27705f1f-fa3c-3875-b34e-0d9f61c5b2e3 | -1.13612 | -47.16622 | 2025-12-08 04:44:00 | NOAA-21 | CAPANEMA | PARÁ | Brasil | 1502202 | 15 | 33 | nan | nan | nan | Amazônia | 2.0 |
| 6eb2606f-fc95-31e9-9de4-65556cf13020 | -1.67856 | -45.8669 | 2025-12-08 04:44:00 | NOAA-21 | AMAPÁ DO MARANHÃO | MARANHÃO | Brasil | 2100550 | 21 | 33 | nan | nan | nan | Amazônia | 4.2 |
| 610db12e-cef7-3033-bec3-a49b3b0b5a59 | -0.29971 | -51.69144 | 2025-12-08 04:44:00 | NOAA-21 | MAZAGÃO | AMAPÁ | Brasil | 1600402 | 16 | 33 | nan | nan | nan | Amazônia | 2.9 |
| 1634b4fd-53fe-3133-9270-907dd9a6f773 | -2.64207 | -46.96275 | 2025-12-08 04:44:00 | NOAA-21 | PARAGOMINAS | PARÁ | Brasil | 1505502 | 15 | 33 | nan | nan | nan | Amazônia | 24.3 |
| 70e03739-8be3-3fe0-ab56-d989562abef3 | -3.33148 | -42.14325 | 2025-12-08 04:44:00 | NOAA-21 | MAGALHÃES DE ALMEIDA | MARANHÃO | Brasil | 2106300 | 21 | 33 | nan | nan | nan | Caatinga | 1.6 |
| cb83656d-b8ef-37d7-ab2e-e7ce9d0b4245 | -4.4503 | -44.14197 | 2025-12-08 04:44:00 | NOAA-21 | PERITORÓ | MARANHÃO | Brasil | 2108454 | 21 | 33 | nan | nan | nan | Cerrado | 1.9 |
| 6a8ac510-1f6f-3a26-ad7c-92c5a146c45e | -3.22509 | -46.24405 | 2025-12-08 04:44:00 | NOAA-21 | ZÉ DOCA | MARANHÃO | Brasil | 2114007 | 21 | 33 | nan | nan | nan | Amazônia | 1.6 |
| 39792191-e4ce-303b-a739-e51adb819a16 | -1.24012 | -46.5331 | 2025-12-08 04:44:00 | NOAA-21 | AUGUSTO CORRÊA | PARÁ | Brasil | 1500909 | 15 | 33 | nan | nan | nan | Amazônia | 1.5 |
| 5fed11fd-337f-322a-a142-6fd868dd6b98 | 2.08553 | -50.96258 | 2025-12-08 04:44:00 | NOAA-21 | AMAPÁ | AMAPÁ | Brasil | 1600105 | 16 | 33 | nan | nan | nan | Amazônia | 0.9 |
| ef46337a-86c7-3e01-a757-6d7b4990fc2a | -2.64143 | -46.96691 | 2025-12-08 04:44:00 | NOAA-21 | PARAGOMINAS | PARÁ | Brasil | 1505502 | 15 | 33 | nan | nan | nan | Amazônia | 24.3 |
| a4817762-4775-34fb-942a-9f95ddac00aa | -2.50486 | -51.80149 | 2025-12-08 04:44:00 | NOAA-21 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 2.2 |
| c1ad58f1-c138-316f-81c0-801933e9ea90 | -2.31234 | -45.55224 | 2025-12-08 04:44:00 | NOAA-21 | TURILÂNDIA | MARANHÃO | Brasil | 2112456 | 21 | 33 | nan | nan | nan | Amazônia | 2.9 |
| 85dc2b4b-cc20-3b88-aeaa-da341f2a5247 | -2.26908 | -46.24017 | 2025-12-08 04:44:00 | NOAA-21 | CENTRO NOVO DO MARANHÃO | MARANHÃO | Brasil | 2103174 | 21 | 33 | nan | nan | nan | Amazônia | 0.9 |
| 6960daf7-4a6a-3a5a-ba27-36297166842d | -0.98442 | -52.97688 | 2025-12-08 04:44:00 | NOAA-21 | ALMEIRIM | PARÁ | Brasil | 1500503 | 15 | 33 | nan | nan | nan | Amazônia | 1.5 |
| 61b7ec62-01d2-3cd0-b511-bc624a1d9fa0 | -0.81177 | -51.94159 | 2025-12-08 04:44:00 | NOAA-21 | LARANJAL DO JARI | AMAPÁ | Brasil | 1600279 | 16 | 33 | nan | nan | nan | Amazônia | 1.2 |
| d6da38de-84bc-3157-ba45-f6668ea5dcc8 | -3.84883 | -47.82731 | 2025-12-08 04:44:00 | NOAA-21 | ULIANÓPOLIS | PARÁ | Brasil | 1508126 | 15 | 33 | nan | nan | nan | Amazônia | 1.9 |
| 2c15478a-8f83-3ce7-b8ad-eeeb539fd0bc | -0.98505 | -52.97277 | 2025-12-08 04:44:00 | NOAA-21 | ALMEIRIM | PARÁ | Brasil | 1500503 | 15 | 33 | nan | nan | nan | Amazônia | 1.3 |
| daed9d64-094b-39d3-8389-af36ddf28a3e | -0.30314 | -51.69197 | 2025-12-08 04:44:00 | NOAA-21 | MAZAGÃO | AMAPÁ | Brasil | 1600402 | 16 | 33 | nan | nan | nan | Amazônia | 2.9 |
| bf8cdcef-d2a9-3eb9-aa61-e414547dc382 | -3.33649 | -42.14404 | 2025-12-08 04:44:00 | NOAA-21 | MAGALHÃES DE ALMEIDA | MARANHÃO | Brasil | 2106300 | 21 | 33 | nan | nan | nan | Caatinga | 1.6 |
| b30e0d48-ad86-3b18-ac78-2bc07ae9286b | -2.35931 | -47.68597 | 2025-12-08 04:44:00 | NOAA-21 | IPIXUNA DO PARÁ | PARÁ | Brasil | 1503457 | 15 | 33 | nan | nan | nan | Amazônia | 1.9 |
| 48afd393-1880-32a1-bf3e-e9f02620b725 | -2.95762 | -48.07079 | 2025-12-08 04:44:00 | NOAA-21 | IPIXUNA DO PARÁ | PARÁ | Brasil | 1503457 | 15 | 33 | nan | nan | nan | Amazônia | 0.6 |
| 319dd7cc-5781-33aa-96bd-f61d3edd7c65 | -5.44074 | -50.74458 | 2025-12-08 04:46:00 | NOAA-21 | MARABÁ | PARÁ | Brasil | 1504208 | 15 | 33 | nan | nan | nan | Amazônia | 0.7 |
| a29c5b19-2e4c-3441-bef2-0b2626bbffb7 | -6.44528 | -45.73847 | 2025-12-08 04:46:00 | NOAA-21 | FERNANDO FALCÃO | MARANHÃO | Brasil | 2104081 | 21 | 33 | nan | nan | nan | Cerrado | 1.9 |
| 4aa597b6-8ba9-3a9c-aed9-857f0c7bd6be | -6.44191 | -45.73914 | 2025-12-08 04:46:00 | NOAA-21 | FERNANDO FALCÃO | MARANHÃO | Brasil | 2104081 | 21 | 33 | nan | nan | nan | Cerrado | 1.4 |
| acf910e3-d6a3-3a0a-914c-0c99424609a1 | -5.5884 | -51.40851 | 2025-12-08 04:46:00 | NOAA-21 | SÃO FÉLIX DO XINGU | PARÁ | Brasil | 1507300 | 15 | 33 | nan | nan | nan | Amazônia | 0.6 |
| c38da76b-1d69-3b59-9ef8-ebe9657566b0 | -4.50377 | -55.80624 | 2025-12-08 04:46:00 | NOAA-21 | ITAITUBA | PARÁ | Brasil | 1503606 | 15 | 33 | nan | nan | nan | Amazônia | 1.5 |
| 1c6d217a-2b45-3c93-b25c-eec3795dd8c9 | -5.4402 | -50.74802 | 2025-12-08 04:46:00 | NOAA-21 | MARABÁ | PARÁ | Brasil | 1504208 | 15 | 33 | nan | nan | nan | Amazônia | 1.6 |
| d8b009e4-7481-34aa-8c20-d5e0b401b71b | -5.43689 | -50.74751 | 2025-12-08 04:46:00 | NOAA-21 | MARABÁ | PARÁ | Brasil | 1504208 | 15 | 33 | nan | nan | nan | Amazônia | 1.1 |
| b4d7c841-2cbe-37e8-a1ef-081b53fb5877 | -6.43779 | -45.73858 | 2025-12-08 04:46:00 | NOAA-21 | FERNANDO FALCÃO | MARANHÃO | Brasil | 2104081 | 21 | 33 | nan | nan | nan | Cerrado | 1.4 |
| e5507372-8174-356e-a712-cb2691aef4ac | -6.44245 | -45.73548 | 2025-12-08 04:46:00 | NOAA-21 | FERNANDO FALCÃO | MARANHÃO | Brasil | 2104081 | 21 | 33 | nan | nan | nan | Cerrado | 1.4 |
| 4211eea3-d3d6-344f-ac9b-52eb2b0f8567 | -5.58895 | -51.40504 | 2025-12-08 04:46:00 | NOAA-21 | SÃO FÉLIX DO XINGU | PARÁ | Brasil | 1507300 | 15 | 33 | nan | nan | nan | Amazônia | 1.2 |
| 83ce23dc-97df-3758-9cfb-c6aba102c58d | -4.50437 | -55.80261 | 2025-12-08 04:46:00 | NOAA-21 | ITAITUBA | PARÁ | Brasil | 1503606 | 15 | 33 | nan | nan | nan | Amazônia | 1.5 |
| 9db6422d-ba02-3a1e-b924-7dd8c3f228fb | -6.43833 | -45.73494 | 2025-12-08 04:46:00 | NOAA-21 | FERNANDO FALCÃO | MARANHÃO | Brasil | 2104081 | 21 | 33 | nan | nan | nan | Cerrado | 1.4 |
| 88be04d2-65bc-3b0d-a248-d0a0b8f029f9 | -5.43743 | -50.74406 | 2025-12-08 04:46:00 | NOAA-21 | MARABÁ | PARÁ | Brasil | 1504208 | 15 | 33 | nan | nan | nan | Amazônia | 1.3 |
| 81a225f9-c879-3c03-b0b5-f0bf0f3e8cb5 | -25.17822 | -49.40412 | 2025-12-08 04:50:00 | NOAA-21 | ITAPERUÇU | PARANÁ | Brasil | 4111258 | 41 | 33 | nan | nan | nan | Mata Atlântica | 0.6 |
| 75a832d2-ade0-31ce-a7eb-017ce088f6ed | -21.42386 | -46.64273 | 2025-12-08 04:50:00 | NOAA-21 | TAPIRATIBA | SÃO PAULO | Brasil | 3553609 | 35 | 33 | nan | nan | nan | Mata Atlântica | 1.3 |
| f69bdf0d-887b-3b3a-8c3d-27b24e2634f8 | -29.3129 | -50.50587 | 2025-12-08 04:53:00 | NOAA-21 | SÃO FRANCISCO DE PAULA | RIO GRANDE DO SUL | Brasil | 4318200 | 43 | 33 | nan | nan | nan | Mata Atlântica | 2.7 |
| 54dd3ab3-4177-3ebe-8cb7-908857e044b7 | -29.31033 | -50.50835 | 2025-12-08 04:53:00 | NOAA-21 | SÃO FRANCISCO DE PAULA | RIO GRANDE DO SUL | Brasil | 4318200 | 43 | 33 | nan | nan | nan | Mata Atlântica | 2.7 |
| 5ba983e8-5aa6-3722-8510-0ddf93a7fe4f | -29.30875 | -50.50528 | 2025-12-08 04:53:00 | NOAA-21 | SÃO FRANCISCO DE PAULA | RIO GRANDE DO SUL | Brasil | 4318200 | 43 | 33 | nan | nan | nan | Mata Atlântica | 2.7 |
| c3693c44-5481-380d-b26e-bff6f0572899 | -28.85482 | -50.64911 | 2025-12-08 04:53:00 | NOAA-21 | SÃO FRANCISCO DE PAULA | RIO GRANDE DO SUL | Brasil | 4318200 | 43 | 33 | nan | nan | nan | Mata Atlântica | 1.5 |
| f8f8d1b7-d042-305c-aea8-f9d5fbe2e072 | -29.31078 | -50.50412 | 2025-12-08 04:53:00 | NOAA-21 | SÃO FRANCISCO DE PAULA | RIO GRANDE DO SUL | Brasil | 4318200 | 43 | 33 | nan | nan | nan | Mata Atlântica | 3.6 |
| 7e0c0257-0f6f-35fd-b60c-246020699950 | -29.30827 | -50.50949 | 2025-12-08 04:53:00 | NOAA-21 | SÃO FRANCISCO DE PAULA | RIO GRANDE DO SUL | Brasil | 4318200 | 43 | 33 | nan | nan | nan | Mata Atlântica | 2.1 |
| 6fdedd7f-d599-3a94-aa2b-bff6f29d2e5b | 3.3965 | -51.25964 | 2025-12-08 05:12:00 | NPP-375D | OIAPOQUE | AMAPÁ | Brasil | 1600501 | 16 | 33 | nan | nan | nan | Amazônia | 0.9 |
| 3286f69b-9348-3eae-89a5-167c564c72d3 | 3.40672 | -51.256 | 2025-12-08 05:12:00 | NPP-375D | OIAPOQUE | AMAPÁ | Brasil | 1600501 | 16 | 33 | nan | nan | nan | Amazônia | 4.2 |
| b5d67d67-4544-32b1-bead-949e00f595eb | 3.30572 | -60.82752 | 2025-12-08 05:12:00 | NPP-375D | BOA VISTA | RORAIMA | Brasil | 1400100 | 14 | 33 | nan | nan | nan | Amazônia | 0.7 |
| da25a428-fc69-3450-8737-97d7eee659f7 | 3.47785 | -51.23983 | 2025-12-08 05:12:00 | NPP-375D | OIAPOQUE | AMAPÁ | Brasil | 1600501 | 16 | 33 | nan | nan | nan | Amazônia | 1.0 |
| 2f5c2d0b-2c18-3838-83c8-6b8e2c099c4b | 3.39613 | -51.26241 | 2025-12-08 05:12:00 | NPP-375D | OIAPOQUE | AMAPÁ | Brasil | 1600501 | 16 | 33 | nan | nan | nan | Amazônia | 0.9 |
| cf6161f4-f756-3e61-a018-0f0361c5d32d | 3.67144 | -51.38462 | 2025-12-08 05:12:00 | NPP-375D | OIAPOQUE | AMAPÁ | Brasil | 1600501 | 16 | 33 | nan | nan | nan | Amazônia | 1.2 |
| ff533a60-5bba-338b-bf9f-5dab5d16798f | 3.40596 | -51.25142 | 2025-12-08 05:12:00 | NPP-375D | OIAPOQUE | AMAPÁ | Brasil | 1600501 | 16 | 33 | nan | nan | nan | Amazônia | 3.0 |
| 02c3bde9-94d5-3d00-bb61-dab77503e984 | 3.3021 | -60.83201 | 2025-12-08 05:12:00 | NPP-375D | BOA VISTA | RORAIMA | Brasil | 1400100 | 14 | 33 | nan | nan | nan | Amazônia | 1.9 |
| a9b2a2c0-250d-3f0f-bc89-77112e01a7af | 4.35566 | -60.22673 | 2025-12-08 05:12:00 | NPP-375D | UIRAMUTÃ | RORAIMA | Brasil | 1400704 | 14 | 33 | nan | nan | nan | Amazônia | 0.3 |
| 7ee1ac80-d571-3fba-a831-b31157c6e909 | 4.32028 | -60.07716 | 2025-12-08 05:12:00 | NPP-375D | UIRAMUTÃ | RORAIMA | Brasil | 1400704 | 14 | 33 | nan | nan | nan | Amazônia | 1.8 |
| 8fbfa6c0-57ea-31fb-88a3-3a44fb233cc2 | 3.40333 | -51.25383 | 2025-12-08 05:12:00 | NPP-375D | OIAPOQUE | AMAPÁ | Brasil | 1600501 | 16 | 33 | nan | nan | nan | Amazônia | 4.0 |
| 5e40fc05-0bd7-3b4c-a4e3-40cffe96f7da | 3.39915 | -51.25722 | 2025-12-08 05:12:00 | NPP-375D | OIAPOQUE | AMAPÁ | Brasil | 1600501 | 16 | 33 | nan | nan | nan | Amazônia | 3.6 |
| 0cfabacb-43d8-3537-b498-96a9dcb0b020 | 2.3766 | -51.69434 | 2025-12-08 05:12:00 | NPP-375D | CALÇOENE | AMAPÁ | Brasil | 1600204 | 16 | 33 | nan | nan | nan | Amazônia | 0.6 |
| bf39bbf0-d85f-3cfd-92b7-d1d22c05dd17 | 3.42185 | -51.25357 | 2025-12-08 05:12:00 | NPP-375D | OIAPOQUE | AMAPÁ | Brasil | 1600501 | 16 | 33 | nan | nan | nan | Amazônia | 2.8 |
| 159cd080-21f5-3672-b8f5-763f2b4df344 | 1.97071 | -55.68026 | 2025-12-08 05:12:00 | NPP-375D | ÓBIDOS | PARÁ | Brasil | 1505106 | 15 | 33 | nan | nan | nan | Amazônia | 2.1 |
| 35a512cc-78ec-3a6a-be96-23b774fd0d48 | 2.77201 | -60.63832 | 2025-12-08 05:12:00 | NPP-375D | CANTÁ | RORAIMA | Brasil | 1400175 | 14 | 33 | nan | nan | nan | Amazônia | 0.9 |
| b26dbd95-8575-3ee9-9140-d9d82d5d65e7 | 3.41731 | -51.24959 | 2025-12-08 05:12:00 | NPP-375D | OIAPOQUE | AMAPÁ | Brasil | 1600501 | 16 | 33 | nan | nan | nan | Amazônia | 1.2 |
| 9a456ea6-bfb2-369c-b5b0-0cbd0a179f41 | 3.4211 | -51.24899 | 2025-12-08 05:12:00 | NPP-375D | OIAPOQUE | AMAPÁ | Brasil | 1600501 | 16 | 33 | nan | nan | nan | Amazônia | 3.4 |
| a3caa841-76a1-3d92-a8b8-fa65c03ecb86 | 3.40294 | -51.25661 | 2025-12-08 05:12:00 | NPP-375D | OIAPOQUE | AMAPÁ | Brasil | 1600501 | 16 | 33 | nan | nan | nan | Amazônia | 3.6 |
| f6c1f4e8-30c8-38c0-ae05-30330cab5463 | 3.78136 | -60.95417 | 2025-12-08 05:12:00 | NPP-375D | AMAJARI | RORAIMA | Brasil | 1400027 | 14 | 33 | nan | nan | nan | Amazônia | 1.2 |
| 77b49b9f-047f-36df-be04-709b2ce4f71e | 3.33889 | -51.31121 | 2025-12-08 05:12:00 | NPP-375D | OIAPOQUE | AMAPÁ | Brasil | 1600501 | 16 | 33 | nan | nan | nan | Amazônia | 2.2 |
| 931ca385-40e1-307f-ae59-79130e006dc6 | 3.2979 | -60.83266 | 2025-12-08 05:12:00 | NPP-375D | BOA VISTA | RORAIMA | Brasil | 1400100 | 14 | 33 | nan | nan | nan | Amazônia | 1.7 |
| a57ced02-05c9-390d-8066-6001a3f9d593 | 2.01925 | -55.68676 | 2025-12-08 05:12:00 | NPP-375D | ÓBIDOS | PARÁ | Brasil | 1505106 | 15 | 33 | nan | nan | nan | Amazônia | 1.3 |
| e7ac72cb-ff22-3ced-9f81-5b953fabe42c | 3.30152 | -60.82817 | 2025-12-08 05:12:00 | NPP-375D | BOA VISTA | RORAIMA | Brasil | 1400100 | 14 | 33 | nan | nan | nan | Amazônia | 0.7 |
| 60703c1f-2901-352e-b21e-c737cee1a74b | 2.37287 | -51.69495 | 2025-12-08 05:12:00 | NPP-375D | CALÇOENE | AMAPÁ | Brasil | 1600204 | 16 | 33 | nan | nan | nan | Amazônia | 0.6 |
| bcc6ff93-48b4-340b-aa41-385483dc24e3 | 3.39955 | -51.25444 | 2025-12-08 05:12:00 | NPP-375D | OIAPOQUE | AMAPÁ | Brasil | 1600501 | 16 | 33 | nan | nan | nan | Amazônia | 4.0 |
| 791550b8-d91b-3344-9848-36f81a73e253 | 1.97125 | -55.6837 | 2025-12-08 05:12:00 | NPP-375D | ÓBIDOS | PARÁ | Brasil | 1505106 | 15 | 33 | nan | nan | nan | Amazônia | 1.9 |
| d2f2e893-7255-38e2-88d8-e747f2c55f06 | 2.01871 | -55.68332 | 2025-12-08 05:12:00 | NPP-375D | ÓBIDOS | PARÁ | Brasil | 1505106 | 15 | 33 | nan | nan | nan | Amazônia | 1.3 |
| d9322bd8-536a-3b27-9a0c-2472a7a82b55 | 3.40028 | -51.25903 | 2025-12-08 05:12:00 | NPP-375D | OIAPOQUE | AMAPÁ | Brasil | 1600501 | 16 | 33 | nan | nan | nan | Amazônia | 4.0 |
| 8277c7dd-898b-35ee-8028-f8e887571cef | 3.56856 | -51.29782 | 2025-12-08 05:12:00 | NPP-375D | OIAPOQUE | AMAPÁ | Brasil | 1600501 | 16 | 33 | nan | nan | nan | Amazônia | 0.9 |
| 41ac0e64-fcc5-3016-801c-2d93bb8ac59a | 3.67218 | -51.38911 | 2025-12-08 05:12:00 | NPP-375D | OIAPOQUE | AMAPÁ | Brasil | 1600501 | 16 | 33 | nan | nan | nan | Amazônia | 1.2 |
| 452aeb70-099c-3f89-ac0b-d1a6ac920081 | 3.39723 | -51.26423 | 2025-12-08 05:12:00 | NPP-375D | OIAPOQUE | AMAPÁ | Brasil | 1600501 | 16 | 33 | nan | nan | nan | Amazônia | 0.9 |
| 6ff48b62-0729-369c-a2a7-de34045299cd | 1.97456 | -55.68318 | 2025-12-08 05:12:00 | NPP-375D | ÓBIDOS | PARÁ | Brasil | 1505106 | 15 | 33 | nan | nan | nan | Amazônia | 2.3 |
| e51df566-3178-39ac-a98d-d608cfaa0b5d | 3.39991 | -51.2618 | 2025-12-08 05:12:00 | NPP-375D | OIAPOQUE | AMAPÁ | Brasil | 1600501 | 16 | 33 | nan | nan | nan | Amazônia | 3.6 |
| 6a1440c6-036d-33b6-93d9-ae671bb1d7b6 | 3.47859 | -51.24441 | 2025-12-08 05:12:00 | NPP-375D | OIAPOQUE | AMAPÁ | Brasil | 1600501 | 16 | 33 | nan | nan | nan | Amazônia | 0.9 |
| 35d141dd-df30-3f75-95e7-d79e978010ec | 3.66844 | -51.38971 | 2025-12-08 05:12:00 | NPP-375D | OIAPOQUE | AMAPÁ | Brasil | 1600501 | 16 | 33 | nan | nan | nan | Amazônia | 1.2 |
| 55b744d0-2cd8-3ae7-8881-fb82d78403b1 | 3.40975 | -51.25081 | 2025-12-08 05:12:00 | NPP-375D | OIAPOQUE | AMAPÁ | Brasil | 1600501 | 16 | 33 | nan | nan | nan | Amazônia | 3.0 |
| e687628e-5209-3a4e-8e49-cb4ee0d7c7f9 | 4.35096 | -60.22338 | 2025-12-08 05:12:00 | NPP-375D | UIRAMUTÃ | RORAIMA | Brasil | 1400704 | 14 | 33 | nan | nan | nan | Amazônia | 1.4 |
| 098982d0-71bd-3ae6-a04e-384291b74ccd | 1.7301 | -50.75239 | 2025-12-08 05:12:00 | NPP-375D | PRACUÚBA | AMAPÁ | Brasil | 1600550 | 16 | 33 | nan | nan | nan | Amazônia | 1.1 |
| d0b48134-3596-3116-b021-4461a3e7521b | 3.41353 | -51.25021 | 2025-12-08 05:12:00 | NPP-375D | OIAPOQUE | AMAPÁ | Brasil | 1600501 | 16 | 33 | nan | nan | nan | Amazônia | 1.2 |
| 4b604abe-91f1-3d67-acab-3b6865027180 | -0.38122 | -51.96017 | 2025-12-08 05:14:00 | NPP-375D | MAZAGÃO | AMAPÁ | Brasil | 1600402 | 16 | 33 | nan | nan | nan | Amazônia | 2.7 |
| 28ecc706-67a1-35db-bed3-ee9d65331267 | -1.00293 | -52.31795 | 2025-12-08 05:14:00 | NPP-375D | VITÓRIA DO JARI | AMAPÁ | Brasil | 1600808 | 16 | 33 | nan | nan | nan | Amazônia | 1.1 |
| a02c70cd-1b1d-37fc-8199-887b63d8a0bf | -2.64316 | -46.96422 | 2025-12-08 05:14:00 | NPP-375D | PARAGOMINAS | PARÁ | Brasil | 1505502 | 15 | 33 | nan | nan | nan | Amazônia | 5.6 |
| 83907689-ac90-3ab1-8fe4-0aca376ff1f0 | -0.38504 | -51.96077 | 2025-12-08 05:14:00 | NPP-375D | MAZAGÃO | AMAPÁ | Brasil | 1600402 | 16 | 33 | nan | nan | nan | Amazônia | 1.0 |
| 7851e5b4-607c-33c2-a973-bf5f6aa913ed | -3.39323 | -44.16371 | 2025-12-08 05:14:00 | NPP-375D | ITAPECURU MIRIM | MARANHÃO | Brasil | 2105401 | 21 | 33 | nan | nan | nan | Cerrado | 3.5 |
| e609410e-ba04-32e2-9285-a6e3dfc59343 | -2.2576 | -46.11858 | 2025-12-08 05:14:00 | NPP-375D | CENTRO DO GUILHERME | MARANHÃO | Brasil | 2103158 | 21 | 33 | nan | nan | nan | Amazônia | 1.9 |


[Clique aqui para ver as próximas entradas](README5.md)
