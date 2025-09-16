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

## Dados Diários - Página 23

| ID | Latitude | Longitude | Data/Hora GMT | Satélite | Município | Estado | País | Município ID | Estado ID | País ID | Dias sem Chuva | Precipitação | Risco de Fogo | Bioma | FRP |
|----|----------|-----------|---------------|----------|-----------|--------|------|--------------|-----------|---------|----------------|--------------|----------------|-------|-----|
| 744090f3-4c86-30e6-b044-a4651f8b3dd1 | -18.87251 | -43.35177 | 2025-09-16 04:04:00 | NOAA-21 | CONCEIÇÃO DO MATO DENTRO | MINAS GERAIS | Brasil | 3117504 | 31 | 33 | nan | nan | nan | Mata Atlântica | 3.6 |
| 539a2a6e-d5db-3daf-86e0-6a3f79c8e211 | -13.20128 | -47.30758 | 2025-09-16 04:04:00 | NOAA-21 | ARRAIAS | TOCANTINS | Brasil | 1702406 | 17 | 33 | nan | nan | nan | Cerrado | 5.4 |
| 1070426f-f559-3a5f-a633-38546d1dbad7 | -12.61303 | -47.98883 | 2025-09-16 04:04:00 | NOAA-21 | PARANÃ | TOCANTINS | Brasil | 1716208 | 17 | 33 | nan | nan | nan | Cerrado | 15.4 |
| 94b8a544-b1e7-3800-bfae-f94dc61de954 | -12.79748 | -47.25787 | 2025-09-16 04:04:00 | NOAA-21 | ARRAIAS | TOCANTINS | Brasil | 1702406 | 17 | 33 | nan | nan | nan | Cerrado | 3.7 |
| ecae8d6d-6699-3cc2-acd1-6143c7359716 | -20.10064 | -43.20115 | 2025-09-16 04:04:00 | NOAA-21 | ALVINÓPOLIS | MINAS GERAIS | Brasil | 3102308 | 31 | 33 | nan | nan | nan | Mata Atlântica | 2.3 |
| 1f04dcd4-acb2-3f75-85b2-ef1ce6440064 | -12.61418 | -47.9575 | 2025-09-16 04:04:00 | NOAA-21 | PARANÃ | TOCANTINS | Brasil | 1716208 | 17 | 33 | nan | nan | nan | Cerrado | 2.7 |
| ba1d0fe2-031d-314c-ac87-ceb2e147dac5 | -12.92101 | -47.96752 | 2025-09-16 04:04:00 | NOAA-21 | PARANÃ | TOCANTINS | Brasil | 1716208 | 17 | 33 | nan | nan | nan | Cerrado | 2.5 |
| 983d08f4-43fd-3fec-b408-eca3fbdff75f | -12.62992 | -45.75586 | 2025-09-16 04:04:00 | NOAA-21 | SÃO DESIDÉRIO | BAHIA | Brasil | 2928901 | 29 | 33 | nan | nan | nan | Cerrado | 4.4 |
| 8190915e-3195-3112-a62e-80947b4846f0 | -14.80979 | -51.67111 | 2025-09-16 04:04:00 | NOAA-21 | ARAGUAIANA | MATO GROSSO | Brasil | 5101001 | 51 | 33 | nan | nan | nan | Cerrado | 3.2 |
| 544af673-c26e-37cb-8d50-a1578c85300a | -12.79311 | -44.7627 | 2025-09-16 04:04:00 | NOAA-21 | SÃO DESIDÉRIO | BAHIA | Brasil | 2928901 | 29 | 33 | nan | nan | nan | Cerrado | 0.7 |
| fc29c23c-a97c-370a-86ed-36a1c2eac52a | -14.87622 | -51.67397 | 2025-09-16 04:04:00 | NOAA-21 | ARAGUAIANA | MATO GROSSO | Brasil | 5101001 | 51 | 33 | nan | nan | nan | Cerrado | 2.4 |
| 5ea0f5c6-811f-34c6-bc44-1fbac0392aa7 | -12.76756 | -47.9617 | 2025-09-16 04:04:00 | NOAA-21 | PARANÃ | TOCANTINS | Brasil | 1716208 | 17 | 33 | nan | nan | nan | Cerrado | 3.7 |
| 52b64f34-536b-3bdb-8891-405bc970a9ba | -14.63987 | -46.37878 | 2025-09-16 04:04:00 | NOAA-21 | SÍTIO D'ABADIA | GOIÁS | Brasil | 5220702 | 52 | 33 | nan | nan | nan | Cerrado | 6.2 |
| 666e93c3-d703-35e0-941d-31d4b6a47f6c | -15.82461 | -53.47355 | 2025-09-16 04:04:00 | NOAA-21 | TESOURO | MATO GROSSO | Brasil | 5108105 | 51 | 33 | nan | nan | nan | Cerrado | 4.4 |
| 4d3ad0d5-c9f3-3580-991b-8249c4979463 | -14.52584 | -47.34938 | 2025-09-16 04:04:00 | NOAA-21 | SÃO JOÃO D'ALIANÇA | GOIÁS | Brasil | 5220009 | 52 | 33 | nan | nan | nan | Cerrado | 1.6 |
| 7990d470-ea45-3c2a-80cb-b16d50f11eb1 | -12.66608 | -47.71967 | 2025-09-16 04:04:00 | NOAA-21 | PARANÃ | TOCANTINS | Brasil | 1716208 | 17 | 33 | nan | nan | nan | Cerrado | 1.7 |
| 35f98e86-076e-3370-a445-a64206084db1 | -15.79722 | -53.45749 | 2025-09-16 04:04:00 | NOAA-21 | TESOURO | MATO GROSSO | Brasil | 5108105 | 51 | 33 | nan | nan | nan | Cerrado | 4.3 |
| 08aae896-7d59-359f-a816-2880a5570d8a | -14.51317 | -47.37523 | 2025-09-16 04:04:00 | NOAA-21 | SÃO JOÃO D'ALIANÇA | GOIÁS | Brasil | 5220009 | 52 | 33 | nan | nan | nan | Cerrado | 2.5 |
| ef5f9b36-ba74-3ead-b8d2-442531202d3f | -13.23562 | -40.93903 | 2025-09-16 04:04:00 | NOAA-21 | ITAETÉ | BAHIA | Brasil | 2915007 | 29 | 33 | nan | nan | nan | Caatinga | 0.3 |
| 6c1db104-deed-3053-bcf8-83e78e32267a | -12.77032 | -47.97357 | 2025-09-16 04:04:00 | NOAA-21 | PARANÃ | TOCANTINS | Brasil | 1716208 | 17 | 33 | nan | nan | nan | Cerrado | 4.5 |
| 42ed87e3-17ae-37b1-8d18-d59b19b18e44 | -15.81381 | -53.46634 | 2025-09-16 04:04:00 | NOAA-21 | TESOURO | MATO GROSSO | Brasil | 5108105 | 51 | 33 | nan | nan | nan | Cerrado | 2.0 |
| ab4548ef-5796-3034-a754-1b5d0227b5c9 | -16.78436 | -40.94258 | 2025-09-16 04:04:00 | NOAA-21 | JOAÍMA | MINAS GERAIS | Brasil | 3136009 | 31 | 33 | nan | nan | nan | Mata Atlântica | 0.7 |
| a0c63d13-012d-319c-b49b-556aefea680a | -14.51331 | -47.37183 | 2025-09-16 04:04:00 | NOAA-21 | SÃO JOÃO D'ALIANÇA | GOIÁS | Brasil | 5220009 | 52 | 33 | nan | nan | nan | Cerrado | 0.8 |
| b2a61367-26fe-3a9c-899d-a359a49b3918 | -16.71784 | -49.23274 | 2025-09-16 04:04:00 | NOAA-21 | GOIÂNIA | GOIÁS | Brasil | 5208707 | 52 | 33 | nan | nan | nan | Cerrado | 2.3 |
| 4e4ead5d-03c2-3906-a4e8-6cbb2950dd3d | -17.0793 | -45.8341 | 2025-09-16 04:04:00 | NOAA-21 | BRASILÂNDIA DE MINAS | MINAS GERAIS | Brasil | 3108552 | 31 | 33 | nan | nan | nan | Cerrado | 8.9 |
| 455a0aaf-9b88-38f8-a0b0-547adaaaf228 | -16.51871 | -43.5511 | 2025-09-16 04:04:00 | NOAA-21 | FRANCISCO SÁ | MINAS GERAIS | Brasil | 3126703 | 31 | 33 | nan | nan | nan | Cerrado | 16.4 |
| 9dad75ac-2dfe-314e-8333-3fa26d00e400 | -16.28418 | -45.68478 | 2025-09-16 04:04:00 | NOAA-21 | SÃO ROMÃO | MINAS GERAIS | Brasil | 3164209 | 31 | 33 | nan | nan | nan | Cerrado | 2.0 |
| dbe7564d-6815-3200-81e8-4d403525966a | -12.61102 | -47.9749 | 2025-09-16 04:04:00 | NOAA-21 | PARANÃ | TOCANTINS | Brasil | 1716208 | 17 | 33 | nan | nan | nan | Cerrado | 3.2 |
| 90508159-bfa4-3d14-b266-60ba56c0fdc9 | -14.91214 | -51.67479 | 2025-09-16 04:04:00 | NOAA-21 | ARAGUAIANA | MATO GROSSO | Brasil | 5101001 | 51 | 33 | nan | nan | nan | Cerrado | 1.1 |
| fcec707f-7ded-395d-ba11-0eb7f8565eb7 | -12.6221 | -45.73726 | 2025-09-16 04:04:00 | NOAA-21 | SÃO DESIDÉRIO | BAHIA | Brasil | 2928901 | 29 | 33 | nan | nan | nan | Cerrado | 7.7 |
| 80cb8648-ad38-3618-95bd-9a281f9ecbdb | -17.73042 | -46.77461 | 2025-09-16 04:04:00 | NOAA-21 | VAZANTE | MINAS GERAIS | Brasil | 3171006 | 31 | 33 | nan | nan | nan | Cerrado | 2.4 |
| 985a3363-c149-3bc2-8572-866b099ce588 | -12.80822 | -47.1881 | 2025-09-16 04:04:00 | NOAA-21 | ARRAIAS | TOCANTINS | Brasil | 1702406 | 17 | 33 | nan | nan | nan | Cerrado | 1.4 |
| e116e5c3-b586-3d32-b9d2-3d1eb0680d9a | -14.513 | -47.32871 | 2025-09-16 04:04:00 | NOAA-21 | SÃO JOÃO D'ALIANÇA | GOIÁS | Brasil | 5220009 | 52 | 33 | nan | nan | nan | Cerrado | 6.4 |
| a18ae8c9-0ef0-3e1b-92ec-976bbbff6856 | -18.16456 | -49.20638 | 2025-09-16 04:04:00 | NOAA-21 | BURITI ALEGRE | GOIÁS | Brasil | 5203906 | 52 | 33 | nan | nan | nan | Mata Atlântica | 2.5 |
| f9051301-c99f-3faf-a91a-8f7f348be925 | -15.83366 | -53.47818 | 2025-09-16 04:04:00 | NOAA-21 | TESOURO | MATO GROSSO | Brasil | 5108105 | 51 | 33 | nan | nan | nan | Cerrado | 3.9 |
| bf790493-fd48-318f-80e0-5804f490726e | -12.68169 | -47.98653 | 2025-09-16 04:04:00 | NOAA-21 | PARANÃ | TOCANTINS | Brasil | 1716208 | 17 | 33 | nan | nan | nan | Cerrado | 3.8 |
| 68793d5f-3ce6-35d2-aab9-2d8408b58a2a | -16.68184 | -49.76305 | 2025-09-16 04:04:00 | NOAA-21 | PALMEIRAS DE GOIÁS | GOIÁS | Brasil | 5215702 | 52 | 33 | nan | nan | nan | Cerrado | 1.6 |
| c0a38fd5-3eba-3bdc-b42c-704b0f4b8962 | -12.80787 | -47.94123 | 2025-09-16 04:04:00 | NOAA-21 | PARANÃ | TOCANTINS | Brasil | 1716208 | 17 | 33 | nan | nan | nan | Cerrado | 1.9 |
| 1217169a-dc08-39e2-b32a-34a302f266a0 | -14.47535 | -46.35686 | 2025-09-16 04:04:00 | NOAA-21 | SÍTIO D'ABADIA | GOIÁS | Brasil | 5220702 | 52 | 33 | nan | nan | nan | Cerrado | 1.1 |
| ef79a747-7a28-370c-880b-72a8eeb2d0de | -13.02494 | -47.97028 | 2025-09-16 04:04:00 | NOAA-21 | PARANÃ | TOCANTINS | Brasil | 1716208 | 17 | 33 | nan | nan | nan | Cerrado | 0.9 |
| 38e7f34c-b116-312d-869a-909c85e77ce9 | -13.93213 | -44.79055 | 2025-09-16 04:04:00 | NOAA-21 | COCOS | BAHIA | Brasil | 2908101 | 29 | 33 | nan | nan | nan | Cerrado | 1.0 |
| 192467ff-3316-3daa-a2c8-b6524facef53 | -12.62727 | -45.75306 | 2025-09-16 04:04:00 | NOAA-21 | SÃO DESIDÉRIO | BAHIA | Brasil | 2928901 | 29 | 33 | nan | nan | nan | Cerrado | 2.2 |
| 5c959743-114e-338d-9613-0a71bc11bb8c | -12.67076 | -48.02121 | 2025-09-16 04:04:00 | NOAA-21 | PARANÃ | TOCANTINS | Brasil | 1716208 | 17 | 33 | nan | nan | nan | Cerrado | 2.4 |
| 5c9c6f96-bdfb-323f-aedf-3de9d46bb846 | -13.20982 | -47.28342 | 2025-09-16 04:04:00 | NOAA-21 | ARRAIAS | TOCANTINS | Brasil | 1702406 | 17 | 33 | nan | nan | nan | Cerrado | 1.5 |
| 0312db28-7d22-377e-b0d4-c603bf3c387d | -12.79233 | -44.74509 | 2025-09-16 04:04:00 | NOAA-21 | SÃO DESIDÉRIO | BAHIA | Brasil | 2928901 | 29 | 33 | nan | nan | nan | Cerrado | 0.9 |
| 28ec6ac0-e8ea-340d-aea4-8795cea1f9b6 | -17.73125 | -46.76996 | 2025-09-16 04:04:00 | NOAA-21 | VAZANTE | MINAS GERAIS | Brasil | 3171006 | 31 | 33 | nan | nan | nan | Cerrado | 2.4 |
| b7fb86c4-7c60-3e59-82c4-58a6d879c240 | -16.40635 | -44.04629 | 2025-09-16 04:04:00 | NOAA-21 | MONTES CLAROS | MINAS GERAIS | Brasil | 3143302 | 31 | 33 | nan | nan | nan | Cerrado | 0.8 |
| 5d96bd0b-7970-3b80-8333-b88cea39c0b8 | -14.92247 | -51.65141 | 2025-09-16 04:04:00 | NOAA-21 | ARAGUAIANA | MATO GROSSO | Brasil | 5101001 | 51 | 33 | nan | nan | nan | Cerrado | 2.1 |
| 21fa3b07-9d5d-35b5-b75c-f3e811316ea5 | -14.5249 | -47.33154 | 2025-09-16 04:04:00 | NOAA-21 | SÃO JOÃO D'ALIANÇA | GOIÁS | Brasil | 5220009 | 52 | 33 | nan | nan | nan | Cerrado | 2.4 |
| 049a1814-e507-3110-bfcf-e75872b665be | -15.98953 | -47.95076 | 2025-09-16 04:04:00 | NOAA-21 | BRASÍLIA | DISTRITO FEDERAL | Brasil | 5300108 | 53 | 33 | nan | nan | nan | Cerrado | 1.3 |
| addf49cf-9a2f-30a7-adf8-daac1ae6dcb9 | -14.52538 | -47.39798 | 2025-09-16 04:04:00 | NOAA-21 | SÃO JOÃO D'ALIANÇA | GOIÁS | Brasil | 5220009 | 52 | 33 | nan | nan | nan | Cerrado | 2.9 |
| a2019620-ba11-37f3-b692-5da8c8938d74 | -12.81224 | -47.94196 | 2025-09-16 04:04:00 | NOAA-21 | PARANÃ | TOCANTINS | Brasil | 1716208 | 17 | 33 | nan | nan | nan | Cerrado | 1.9 |
| 51feda68-3594-3ec2-b8bc-d939699b56dc | -13.21676 | -47.29268 | 2025-09-16 04:04:00 | NOAA-21 | ARRAIAS | TOCANTINS | Brasil | 1702406 | 17 | 33 | nan | nan | nan | Cerrado | 6.0 |
| 186cf67e-833c-3042-8129-371b2228c7ba | -12.77622 | -47.9661 | 2025-09-16 04:04:00 | NOAA-21 | PARANÃ | TOCANTINS | Brasil | 1716208 | 17 | 33 | nan | nan | nan | Cerrado | 3.2 |
| a471cc3c-78a9-3e88-817e-b79046d8a181 | -18.58571 | -48.14699 | 2025-09-16 04:04:00 | NOAA-21 | ARAGUARI | MINAS GERAIS | Brasil | 3103504 | 31 | 33 | nan | nan | nan | Cerrado | 1.5 |
| 87a4c45d-90d5-3ce6-8014-467c8c7cfa18 | -12.85397 | -47.91035 | 2025-09-16 04:04:00 | NOAA-21 | PARANÃ | TOCANTINS | Brasil | 1716208 | 17 | 33 | nan | nan | nan | Cerrado | 1.5 |
| 4f4e4a15-e2b8-3406-adc6-71a06bbe413a | -19.15895 | -48.72618 | 2025-09-16 04:04:00 | NOAA-21 | UBERLÂNDIA | MINAS GERAIS | Brasil | 3170206 | 31 | 33 | nan | nan | nan | Cerrado | 6.4 |
| d74136ed-157f-37db-abf8-bdcfdbbe3831 | -18.17332 | -45.19292 | 2025-09-16 04:04:00 | NOAA-21 | TRÊS MARIAS | MINAS GERAIS | Brasil | 3169356 | 31 | 33 | nan | nan | nan | Cerrado | 5.0 |
| b89a3823-3507-3f51-8b0b-12e9a76ddc74 | -12.62907 | -45.76068 | 2025-09-16 04:04:00 | NOAA-21 | SÃO DESIDÉRIO | BAHIA | Brasil | 2928901 | 29 | 33 | nan | nan | nan | Cerrado | 4.4 |
| cd04adea-af77-3160-8e19-7af1516a4b9d | -17.08011 | -45.82143 | 2025-09-16 04:04:00 | NOAA-21 | BRASILÂNDIA DE MINAS | MINAS GERAIS | Brasil | 3108552 | 31 | 33 | nan | nan | nan | Cerrado | 5.4 |
| b0e3cf6c-e338-3095-8067-6b1d353c0b22 | -12.80796 | -47.2476 | 2025-09-16 04:04:00 | NOAA-21 | ARRAIAS | TOCANTINS | Brasil | 1702406 | 17 | 33 | nan | nan | nan | Cerrado | 2.8 |
| 017e0b57-4bd9-39bf-88a6-12a5e95026b5 | -12.68244 | -47.98241 | 2025-09-16 04:04:00 | NOAA-21 | PARANÃ | TOCANTINS | Brasil | 1716208 | 17 | 33 | nan | nan | nan | Cerrado | 3.8 |
| 636a2d76-f502-3b80-81d8-ed29193c68f4 | -12.61496 | -47.95319 | 2025-09-16 04:04:00 | NOAA-21 | PARANÃ | TOCANTINS | Brasil | 1716208 | 17 | 33 | nan | nan | nan | Cerrado | 2.7 |
| 1d0dade1-1be1-32ff-94cb-a48936404530 | -12.67014 | -47.92664 | 2025-09-16 04:04:00 | NOAA-21 | PARANÃ | TOCANTINS | Brasil | 1716208 | 17 | 33 | nan | nan | nan | Cerrado | 7.4 |
| caf323c0-0901-34a7-b5b1-1eb67c4f001f | -12.79125 | -47.26067 | 2025-09-16 04:04:00 | NOAA-21 | ARRAIAS | TOCANTINS | Brasil | 1702406 | 17 | 33 | nan | nan | nan | Cerrado | 2.8 |
| 2d15c040-45af-32ee-adde-bc6667864123 | -16.37019 | -42.64966 | 2025-09-16 04:04:00 | NOAA-21 | GRÃO MOGOL | MINAS GERAIS | Brasil | 3127800 | 31 | 33 | nan | nan | nan | Cerrado | 0.9 |
| 7940fee6-2e37-3639-a47b-c7220ae0a6bf | -12.77631 | -47.96322 | 2025-09-16 04:04:00 | NOAA-21 | PARANÃ | TOCANTINS | Brasil | 1716208 | 17 | 33 | nan | nan | nan | Cerrado | 6.3 |
| 94f6d2dc-2a7a-345e-86d2-343d387dfc55 | -17.078 | -45.82039 | 2025-09-16 04:04:00 | NOAA-21 | BRASILÂNDIA DE MINAS | MINAS GERAIS | Brasil | 3108552 | 31 | 33 | nan | nan | nan | Cerrado | 3.5 |
| 87a83971-ffe3-3e73-98e0-e69fc68f9a92 | -15.90035 | -47.31015 | 2025-09-16 04:04:00 | NOAA-21 | FORMOSA | GOIÁS | Brasil | 5208004 | 52 | 33 | nan | nan | nan | Cerrado | 1.9 |
| bd549933-2283-3545-ae63-cc45b72db33d | -19.19468 | -47.20047 | 2025-09-16 04:04:00 | NOAA-21 | PERDIZES | MINAS GERAIS | Brasil | 3149804 | 31 | 33 | nan | nan | nan | Cerrado | 1.8 |
| 9556af36-d2ec-338f-92a8-6951435a4e73 | -15.09569 | -52.48206 | 2025-09-16 04:04:00 | NOAA-21 | BARRA DO GARÇAS | MATO GROSSO | Brasil | 5101803 | 51 | 33 | nan | nan | nan | Cerrado | 4.2 |
| b170d243-ef7f-3b8b-bed8-da3788f0efdb | -14.94073 | -46.59615 | 2025-09-16 04:04:00 | NOAA-21 | FLORES DE GOIÁS | GOIÁS | Brasil | 5207907 | 52 | 33 | nan | nan | nan | Cerrado | 1.9 |
| 09879082-9f3d-31dc-9e32-5cd2466a4dce | -19.84376 | -46.45008 | 2025-09-16 04:04:00 | NOAA-21 | PRATINHA | MINAS GERAIS | Brasil | 3153004 | 31 | 33 | nan | nan | nan | Cerrado | 5.2 |
| 8a38a515-e33d-37e9-afdf-3d3a4ceb327f | -19.84656 | -46.45522 | 2025-09-16 04:04:00 | NOAA-21 | PRATINHA | MINAS GERAIS | Brasil | 3153004 | 31 | 33 | nan | nan | nan | Cerrado | 5.2 |
| 676234ec-2fbb-3fe1-ad8d-d9e14c26fe0c | -16.51931 | -43.54744 | 2025-09-16 04:04:00 | NOAA-21 | FRANCISCO SÁ | MINAS GERAIS | Brasil | 3126703 | 31 | 33 | nan | nan | nan | Cerrado | 16.4 |
| 3c18e06d-663c-35fa-b93b-39a87ec861c5 | -12.79924 | -47.19048 | 2025-09-16 04:04:00 | NOAA-21 | ARRAIAS | TOCANTINS | Brasil | 1702406 | 17 | 33 | nan | nan | nan | Cerrado | 1.6 |
| f97df278-23b5-39fc-a345-0dea1dab9036 | -16.75202 | -49.19765 | 2025-09-16 04:04:00 | NOAA-21 | GOIÂNIA | GOIÁS | Brasil | 5208707 | 52 | 33 | nan | nan | nan | Cerrado | 2.7 |
| 35861f1f-4bd1-312f-a4ee-85f6289db70d | -12.61665 | -45.74627 | 2025-09-16 04:04:00 | NOAA-21 | SÃO DESIDÉRIO | BAHIA | Brasil | 2928901 | 29 | 33 | nan | nan | nan | Cerrado | 9.0 |
| 2d7a6f7e-3643-3734-9197-c8e185fc8345 | -12.66932 | -47.92713 | 2025-09-16 04:04:00 | NOAA-21 | PARANÃ | TOCANTINS | Brasil | 1716208 | 17 | 33 | nan | nan | nan | Cerrado | 7.6 |
| 519e23b9-1035-3898-8927-31d573ca3fc9 | -14.8273 | -51.66741 | 2025-09-16 04:04:00 | NOAA-21 | ARAGUAIANA | MATO GROSSO | Brasil | 5101001 | 51 | 33 | nan | nan | nan | Cerrado | 4.2 |
| 43f235da-7f5f-39a2-ad69-92e936de2dd1 | -12.8531 | -47.13991 | 2025-09-16 04:04:00 | NOAA-21 | ARRAIAS | TOCANTINS | Brasil | 1702406 | 17 | 33 | nan | nan | nan | Cerrado | 4.1 |
| 965bce64-c631-388c-9fe5-ca9b511be98d | -13.21706 | -43.42057 | 2025-09-16 04:04:00 | NOAA-21 | BOM JESUS DA LAPA | BAHIA | Brasil | 2903904 | 29 | 33 | nan | nan | nan | Cerrado | 1.7 |
| 6fd3cf9c-ddbf-3ed2-a5a5-3e6f4766da19 | -13.19014 | -47.29782 | 2025-09-16 04:04:00 | NOAA-21 | ARRAIAS | TOCANTINS | Brasil | 1702406 | 17 | 33 | nan | nan | nan | Cerrado | 2.2 |
| f9900bbc-4dbe-335f-bd2f-3cc55660707e | -13.28639 | -54.23921 | 2025-09-16 04:04:00 | NOAA-21 | PARANATINGA | MATO GROSSO | Brasil | 5106307 | 51 | 33 | nan | nan | nan | Amazônia | 4.8 |
| f3abda4f-8c47-3dd7-9324-9fbf074302b0 | -15.77259 | -53.45764 | 2025-09-16 04:04:00 | NOAA-21 | TESOURO | MATO GROSSO | Brasil | 5108105 | 51 | 33 | nan | nan | nan | Cerrado | 5.3 |
| 8e051c85-e9fb-31ae-b2df-1fdd16e9e8eb | -12.65077 | -47.9552 | 2025-09-16 04:04:00 | NOAA-21 | PARANÃ | TOCANTINS | Brasil | 1716208 | 17 | 33 | nan | nan | nan | Cerrado | 2.2 |
| 5e94639f-3a11-323c-9f9b-6d4e82eeacc8 | -12.44388 | -49.69749 | 2025-09-16 04:04:00 | NOAA-21 | SANDOLÂNDIA | TOCANTINS | Brasil | 1718840 | 17 | 33 | nan | nan | nan | Cerrado | 5.9 |
| 60144beb-7a36-3919-a79c-985439d29530 | -12.41988 | -47.80318 | 2025-09-16 04:04:00 | NOAA-21 | PARANÃ | TOCANTINS | Brasil | 1716208 | 17 | 33 | nan | nan | nan | Cerrado | 2.5 |
| 061b88f4-831d-3176-b1c5-606213acdd52 | -19.8709 | -46.74188 | 2025-09-16 04:04:00 | NOAA-21 | TAPIRA | MINAS GERAIS | Brasil | 3168101 | 31 | 33 | nan | nan | nan | Cerrado | 4.2 |
| 6e18c704-6208-347c-bb36-99da69f186a6 | -12.96407 | -47.97838 | 2025-09-16 04:04:00 | NOAA-21 | PARANÃ | TOCANTINS | Brasil | 1716208 | 17 | 33 | nan | nan | nan | Cerrado | 3.5 |
| 9b9e1094-492d-3f26-8c26-093a0011af90 | -12.98688 | -47.95145 | 2025-09-16 04:04:00 | NOAA-21 | PARANÃ | TOCANTINS | Brasil | 1716208 | 17 | 33 | nan | nan | nan | Cerrado | 3.0 |
| 2e637f23-b4d1-3a22-b115-7c5653b3dfca | -16.13143 | -42.33065 | 2025-09-16 04:04:00 | NOAA-21 | SALINAS | MINAS GERAIS | Brasil | 3157005 | 31 | 33 | nan | nan | nan | Mata Atlântica | 3.1 |
| 6f12c74c-3ed0-35f0-9314-9325f875838f | -17.07863 | -45.83012 | 2025-09-16 04:04:00 | NOAA-21 | BRASILÂNDIA DE MINAS | MINAS GERAIS | Brasil | 3108552 | 31 | 33 | nan | nan | nan | Cerrado | 10.9 |
| 1c25b664-3dd1-3c72-9685-dfaac442efdb | -19.35748 | -44.29464 | 2025-09-16 04:04:00 | NOAA-21 | SETE LAGOAS | MINAS GERAIS | Brasil | 3167202 | 31 | 33 | nan | nan | nan | Cerrado | 0.4 |
| f8ca86ab-1671-3f02-8730-6e966142abef | -12.44684 | -49.70211 | 2025-09-16 04:04:00 | NOAA-21 | SANDOLÂNDIA | TOCANTINS | Brasil | 1718840 | 17 | 33 | nan | nan | nan | Cerrado | 13.7 |
| 9c3ddd54-5d78-32c7-adaf-b3242016a029 | -14.91285 | -51.67129 | 2025-09-16 04:04:00 | NOAA-21 | ARAGUAIANA | MATO GROSSO | Brasil | 5101001 | 51 | 33 | nan | nan | nan | Cerrado | 1.1 |
| 4be5e726-fbbb-3259-b4c4-2660fd027f52 | -18.17956 | -45.17738 | 2025-09-16 04:04:00 | NOAA-21 | TRÊS MARIAS | MINAS GERAIS | Brasil | 3169356 | 31 | 33 | nan | nan | nan | Cerrado | 0.7 |
| bd212620-2d68-32e9-a342-8f283b24527d | -13.00075 | -47.94916 | 2025-09-16 04:04:00 | NOAA-21 | PARANÃ | TOCANTINS | Brasil | 1716208 | 17 | 33 | nan | nan | nan | Cerrado | 3.8 |
| 60d1f242-10fc-350d-b0e3-c27ea38cd139 | -15.78267 | -47.72756 | 2025-09-16 04:04:00 | NOAA-21 | BRASÍLIA | DISTRITO FEDERAL | Brasil | 5300108 | 53 | 33 | nan | nan | nan | Cerrado | 1.4 |
| 91f4ca44-3b2d-30da-9a5c-c63af8bae44d | -14.5408 | -47.35967 | 2025-09-16 04:04:00 | NOAA-21 | SÃO JOÃO D'ALIANÇA | GOIÁS | Brasil | 5220009 | 52 | 33 | nan | nan | nan | Cerrado | 2.9 |


[Clique aqui para ver as próximas entradas](README24.md)
