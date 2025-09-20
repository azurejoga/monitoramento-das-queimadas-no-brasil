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
| 3df7c98c-eefe-3b43-8a98-9b30a19bda67 | -5.7627 | -53.42505 | 2025-09-20 00:35:00 | TERRA_M-M | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 6.4 |
| 7e9501b9-53c5-3f9a-a97c-96389ab2f873 | -4.06798 | -40.47657 | 2025-09-20 00:35:00 | TERRA_M-M | CARIRÉ | CEARÁ | Brasil | 2303105 | 23 | 33 | nan | nan | nan | Caatinga | 38.1 |
| 091208c3-a446-32a3-bd79-30edfa5eb869 | -4.38416 | -43.28666 | 2025-09-20 00:35:00 | TERRA_M-M | ALDEIAS ALTAS | MARANHÃO | Brasil | 2100303 | 21 | 33 | nan | nan | nan | Cerrado | 10.5 |
| 57ac4822-57a4-3bbe-9dbe-b3c715ebbc44 | -4.86663 | -46.83153 | 2025-09-20 00:35:00 | TERRA_M-M | AMARANTE DO MARANHÃO | MARANHÃO | Brasil | 2100600 | 21 | 33 | nan | nan | nan | Amazônia | 8.3 |
| b89201d2-8812-3837-a768-3e71486e6815 | -2.83439 | -48.65172 | 2025-09-20 00:35:00 | TERRA_M-M | TAILÂNDIA | PARÁ | Brasil | 1507953 | 15 | 33 | nan | nan | nan | Amazônia | 4.4 |
| 32c604b7-1231-3010-8928-4602ea4370f8 | -3.97944 | -51.06251 | 2025-09-20 00:35:00 | TERRA_M-M | PACAJÁ | PARÁ | Brasil | 1505486 | 15 | 33 | nan | nan | nan | Amazônia | 4.4 |
| e13ffd76-ad74-39b6-a136-63440a326e6f | -3.23558 | -43.22676 | 2025-09-20 00:35:00 | TERRA_M-M | URBANO SANTOS | MARANHÃO | Brasil | 2112605 | 21 | 33 | nan | nan | nan | Cerrado | 17.6 |
| f389baeb-9a3d-3328-91c5-b9aec1f5b19c | -3.46549 | -51.20959 | 2025-09-20 00:35:00 | TERRA_M-M | ANAPU | PARÁ | Brasil | 1500859 | 15 | 33 | nan | nan | nan | Amazônia | 5.7 |
| 9b94fa0a-0d8e-3acb-9e9b-bb3e56b7a809 | -4.3608 | -46.2841 | 2025-09-20 00:35:00 | TERRA_M-M | BURITICUPU | MARANHÃO | Brasil | 2102325 | 21 | 33 | nan | nan | nan | Amazônia | 203.1 |
| 42d8f935-519b-3af1-bab8-40b74999f403 | -2.26262 | -47.84954 | 2025-09-20 00:35:00 | TERRA_M-M | AURORA DO PARÁ | PARÁ | Brasil | 1500958 | 15 | 33 | nan | nan | nan | Amazônia | 5.3 |
| cdbc668b-14f8-36ac-8261-e2595d929137 | -2.98806 | -52.62955 | 2025-09-20 00:35:00 | TERRA_M-M | BRASIL NOVO | PARÁ | Brasil | 1501725 | 15 | 33 | nan | nan | nan | Amazônia | 8.3 |
| 526d34ed-cc26-3ea6-9f5b-13351649bdeb | -4.87604 | -46.83017 | 2025-09-20 00:35:00 | TERRA_M-M | AMARANTE DO MARANHÃO | MARANHÃO | Brasil | 2100600 | 21 | 33 | nan | nan | nan | Amazônia | 46.5 |
| 67558892-0dba-35db-92c3-11868b0fdbf9 | -3.5171 | -49.43947 | 2025-09-20 00:35:00 | TERRA_M-M | BREU BRANCO | PARÁ | Brasil | 1501782 | 15 | 33 | nan | nan | nan | Amazônia | 4.6 |
| 435c3017-2c53-36aa-87df-7f281852ce6f | -5.19592 | -45.47754 | 2025-09-20 00:35:00 | TERRA_M-M | JENIPAPO DOS VIEIRAS | MARANHÃO | Brasil | 2105476 | 21 | 33 | nan | nan | nan | Cerrado | 48.3 |
| 69bae078-37d1-3a71-9bac-c9c7e5bd4040 | -5.30436 | -45.58924 | 2025-09-20 00:35:00 | TERRA_M-M | JENIPAPO DOS VIEIRAS | MARANHÃO | Brasil | 2105476 | 21 | 33 | nan | nan | nan | Cerrado | 12.1 |
| aed0d3e1-cc55-39c6-a330-f03076bb0558 | -3.45746 | -47.63313 | 2025-09-20 00:35:00 | TERRA_M-M | PARAGOMINAS | PARÁ | Brasil | 1505502 | 15 | 33 | nan | nan | nan | Amazônia | 12.1 |
| 479e9ed6-9fb5-31f8-8fe6-1377c5924056 | -4.07863 | -40.46968 | 2025-09-20 00:35:00 | TERRA_M-M | CARIRÉ | CEARÁ | Brasil | 2303105 | 23 | 33 | nan | nan | nan | Caatinga | 31.8 |
| c6cfdd78-35b1-3bcf-86e6-65179f56f9ca | -5.81222 | -49.84563 | 2025-09-20 00:35:00 | TERRA_M-M | MARABÁ | PARÁ | Brasil | 1504208 | 15 | 33 | nan | nan | nan | Amazônia | 4.7 |
| 37756a0e-c405-3aa4-9a2e-af2ffaf4b178 | -4.99616 | -45.15048 | 2025-09-20 00:35:00 | TERRA_M-M | LAGO DA PEDRA | MARANHÃO | Brasil | 2105708 | 21 | 33 | nan | nan | nan | Cerrado | 10.5 |
| 14ab2cc3-bc03-3fbd-b1ab-f2e15731e3fe | -2.79251 | -47.15573 | 2025-09-20 00:35:00 | TERRA_M-M | PARAGOMINAS | PARÁ | Brasil | 1505502 | 15 | 33 | nan | nan | nan | Amazônia | 16.8 |
| 99a8f9d8-58dc-3e6b-a29d-5551dff9ed80 | -3.34187 | -48.38721 | 2025-09-20 00:35:00 | TERRA_M-M | PARAGOMINAS | PARÁ | Brasil | 1505502 | 15 | 33 | nan | nan | nan | Amazônia | 4.2 |
| 44dab5ce-bc08-3638-8b29-a650dc855f52 | -3.3508 | -48.38594 | 2025-09-20 00:35:00 | TERRA_M-M | PARAGOMINAS | PARÁ | Brasil | 1505502 | 15 | 33 | nan | nan | nan | Amazônia | 5.1 |
| 778b9c84-65b0-3cb0-8421-c6c84051b8a6 | -5.81346 | -49.85464 | 2025-09-20 00:35:00 | TERRA_M-M | MARABÁ | PARÁ | Brasil | 1504208 | 15 | 33 | nan | nan | nan | Amazônia | 4.5 |
| d1f32bae-8b66-3074-8958-9d2560381a85 | -3.51831 | -49.44823 | 2025-09-20 00:35:00 | TERRA_M-M | BREU BRANCO | PARÁ | Brasil | 1501782 | 15 | 33 | nan | nan | nan | Amazônia | 121.2 |
| c6746dbb-36fb-369b-9601-a409c24fee69 | -4.94706 | -49.92704 | 2025-09-20 00:35:00 | TERRA_M-M | ITUPIRANGA | PARÁ | Brasil | 1503705 | 15 | 33 | nan | nan | nan | Amazônia | 8.2 |
| a6da6bcd-5843-3fd4-a701-3c588e416bfb | -5.19767 | -45.48955 | 2025-09-20 00:35:00 | TERRA_M-M | JENIPAPO DOS VIEIRAS | MARANHÃO | Brasil | 2105476 | 21 | 33 | nan | nan | nan | Cerrado | 54.6 |
| 1bd0578e-8f21-35ae-8b18-120eb5d265d6 | -2.82674 | -48.66194 | 2025-09-20 00:35:00 | TERRA_M-M | TAILÂNDIA | PARÁ | Brasil | 1507953 | 15 | 33 | nan | nan | nan | Amazônia | 8.3 |
| 6d706c35-77ba-3a5b-b36c-f69689c194e7 | -5.30266 | -45.57756 | 2025-09-20 00:35:00 | TERRA_M-M | JENIPAPO DOS VIEIRAS | MARANHÃO | Brasil | 2105476 | 21 | 33 | nan | nan | nan | Cerrado | 22.5 |
| 4acbbd17-b3f9-32c9-b8cc-51a1c74f1b76 | -4.67095 | -49.329 | 2025-09-20 00:35:00 | TERRA_M-M | JACUNDÁ | PARÁ | Brasil | 1503804 | 15 | 33 | nan | nan | nan | Amazônia | 7.3 |
| 7804c5e5-6574-35c5-8926-1bde637b19a9 | -3.45764 | -51.22042 | 2025-09-20 00:35:00 | TERRA_M-M | ANAPU | PARÁ | Brasil | 1500859 | 15 | 33 | nan | nan | nan | Amazônia | 30.4 |
| f9cb9874-ba99-3e9e-add2-7c41b4a5bfd1 | -3.45611 | -47.62364 | 2025-09-20 00:35:00 | TERRA_M-M | PARAGOMINAS | PARÁ | Brasil | 1505502 | 15 | 33 | nan | nan | nan | Amazônia | 8.2 |
| 8360a018-7991-3241-8c3e-99080ed45440 | -4.94133 | -45.48317 | 2025-09-20 00:35:00 | TERRA_M-M | LAGOA GRANDE DO MARANHÃO | MARANHÃO | Brasil | 2105963 | 21 | 33 | nan | nan | nan | Cerrado | 28.0 |
| fb0db3e8-1001-3370-8a19-3d317ce03805 | -3.34312 | -48.39625 | 2025-09-20 00:35:00 | TERRA_M-M | PARAGOMINAS | PARÁ | Brasil | 1505502 | 15 | 33 | nan | nan | nan | Amazônia | 6.1 |
| f6079e0d-285e-3ae0-bbe0-5c6d6f99ed9e | -1.1842 | -47.79143 | 2025-09-20 00:35:00 | TERRA_M-M | SÃO FRANCISCO DO PARÁ | PARÁ | Brasil | 1507409 | 15 | 33 | nan | nan | nan | Amazônia | 14.2 |
| d63095e5-570e-3af6-b30e-18c9f2fd297c | -3.16254 | -49.47791 | 2025-09-20 00:35:00 | TERRA_M-M | MOJU | PARÁ | Brasil | 1504703 | 15 | 33 | nan | nan | nan | Amazônia | 5.3 |
| 38c98cc0-c45e-3718-9db1-930208c18630 | -1.17488 | -47.79275 | 2025-09-20 00:35:00 | TERRA_M-M | SÃO FRANCISCO DO PARÁ | PARÁ | Brasil | 1507409 | 15 | 33 | nan | nan | nan | Amazônia | 5.7 |
| ad231040-9841-36ea-b89d-77bddfac24ea | -7.3847 | -47.0378 | 2025-09-20 00:40:00 | GOES-19 | CAROLINA | MARANHÃO | Brasil | 2102804 | 21 | 33 | nan | nan | nan | Cerrado | 63.7 |
| 8a0a2e3c-f0e1-3408-b2a4-0508be76d2f5 | -4.3494 | -46.292 | 2025-09-20 00:40:00 | GOES-19 | BURITICUPU | MARANHÃO | Brasil | 2102325 | 21 | 33 | nan | nan | nan | Amazônia | 76.5 |
| a8e43db2-77fe-302b-bb97-c75deb09c675 | -11.6731 | -44.8736 | 2025-09-20 00:40:00 | GOES-19 | RIACHÃO DAS NEVES | BAHIA | Brasil | 2926202 | 29 | 33 | nan | nan | nan | Cerrado | 91.1 |
| 5a096bb9-a587-3656-87f8-019d27ee7d09 | -7.3844 | -47.0599 | 2025-09-20 00:40:00 | GOES-19 | CAROLINA | MARANHÃO | Brasil | 2102804 | 21 | 33 | nan | nan | nan | Cerrado | 40.5 |
| cda08a85-76e0-3999-ab27-624984dcfedf | -4.368 | -46.291 | 2025-09-20 00:40:00 | GOES-19 | BURITICUPU | MARANHÃO | Brasil | 2102325 | 21 | 33 | nan | nan | nan | Amazônia | 122.2 |
| 81e6b12d-63e4-3219-9c7a-2e9176b46d8b | -5.944 | -45.0704 | 2025-09-20 00:40:00 | GOES-19 | FERNANDO FALCÃO | MARANHÃO | Brasil | 2104081 | 21 | 33 | nan | nan | nan | Cerrado | 77.7 |
| ba301eea-a592-3764-8e20-7d9d31993a75 | -5.1934 | -45.4835 | 2025-09-20 00:40:00 | GOES-19 | JENIPAPO DOS VIEIRAS | MARANHÃO | Brasil | 2105476 | 21 | 33 | nan | nan | nan | Cerrado | 84.2 |
| 2b390653-581c-3333-a36b-d456ed8ab7f2 | -4.3494 | -46.292 | 2025-09-20 00:50:00 | GOES-19 | BURITICUPU | MARANHÃO | Brasil | 2102325 | 21 | 33 | nan | nan | nan | Amazônia | 70.1 |
| 779c9914-7c0a-365f-bdf2-c61e515b8754 | -22.7898 | -45.2828 | 2025-09-20 00:50:00 | GOES-19 | GUARATINGUETÁ | SÃO PAULO | Brasil | 3518404 | 35 | 33 | nan | nan | nan | Mata Atlântica | 71.9 |
| 5e67323d-d886-35e0-affb-3da12f5ff514 | -7.3847 | -47.0378 | 2025-09-20 00:50:00 | GOES-19 | CAROLINA | MARANHÃO | Brasil | 2102804 | 21 | 33 | nan | nan | nan | Cerrado | 38.5 |
| 7369e49e-d993-3ff3-a767-26482002e509 | -16.3204 | -43.0438 | 2025-09-20 00:50:00 | GOES-19 | GRÃO MOGOL | MINAS GERAIS | Brasil | 3127800 | 31 | 33 | nan | nan | nan | Cerrado | 85.1 |
| 92b8dfbe-e179-3ac6-ad09-780d194ee87e | -16.3198 | -43.0684 | 2025-09-20 00:50:00 | GOES-19 | GRÃO MOGOL | MINAS GERAIS | Brasil | 3127800 | 31 | 33 | nan | nan | nan | Cerrado | 116.8 |
| 0db7fad8-2db9-32b7-bf3d-9a57b76523a9 | -5.944 | -45.0704 | 2025-09-20 00:50:00 | GOES-19 | FERNANDO FALCÃO | MARANHÃO | Brasil | 2104081 | 21 | 33 | nan | nan | nan | Cerrado | 73.8 |
| cc1388ca-4490-367b-b410-c62eddb58b29 | -5.9253 | -45.0718 | 2025-09-20 00:50:00 | GOES-19 | FERNANDO FALCÃO | MARANHÃO | Brasil | 2104081 | 21 | 33 | nan | nan | nan | Cerrado | 70.8 |
| 2417142d-b646-38d9-9b9b-99b6ad8136da | -4.368 | -46.291 | 2025-09-20 00:50:00 | GOES-19 | BURITICUPU | MARANHÃO | Brasil | 2102325 | 21 | 33 | nan | nan | nan | Amazônia | 79.3 |
| 8cd808e4-daff-344e-ba2a-8b0ad9022869 | -5.1934 | -45.4835 | 2025-09-20 00:50:00 | GOES-19 | JENIPAPO DOS VIEIRAS | MARANHÃO | Brasil | 2105476 | 21 | 33 | nan | nan | nan | Cerrado | 71.6 |
| 8487718b-c671-339e-96fc-9b7774416be0 | -6.9024 | -44.7656 | 2025-09-20 00:50:00 | GOES-19 | SÃO FÉLIX DE BALSAS | MARANHÃO | Brasil | 2110807 | 21 | 33 | nan | nan | nan | Cerrado | 48.2 |
| 3941553e-639f-30fe-a83f-e892411b2a34 | -3.5161 | -49.4528 | 2025-09-20 00:50:00 | GOES-19 | BREU BRANCO | PARÁ | Brasil | 1501782 | 15 | 33 | nan | nan | nan | Amazônia | 54.2 |
| f3bda6a3-90d2-3b37-9930-fb25c3c0cf23 | -7.2513 | -45.4849 | 2025-09-20 00:50:00 | GOES-19 | SAMBAÍBA | MARANHÃO | Brasil | 2109700 | 21 | 33 | nan | nan | nan | Cerrado | 43.9 |
| 70416549-5494-3a48-aef5-524680a9755a | -22.8109 | -45.2767 | 2025-09-20 00:50:00 | GOES-19 | GUARATINGUETÁ | SÃO PAULO | Brasil | 3518404 | 35 | 33 | nan | nan | nan | Mata Atlântica | 95.3 |
| 94633328-e8c7-32e8-bb8b-425b5b7e6fa7 | -9.2126 | -45.2864 | 2025-09-20 01:00:00 | GOES-19 | BAIXA GRANDE DO RIBEIRO | PIAUÍ | Brasil | 2201150 | 22 | 33 | nan | nan | nan | Cerrado | 48.9 |
| 4e0fa606-49b7-3c1a-aeb2-17415b361c96 | -5.1934 | -45.4835 | 2025-09-20 01:00:00 | GOES-19 | JENIPAPO DOS VIEIRAS | MARANHÃO | Brasil | 2105476 | 21 | 33 | nan | nan | nan | Cerrado | 50.4 |
| b27b5f74-b330-3c89-aa81-4459d60b1db8 | -16.3198 | -43.0684 | 2025-09-20 01:00:00 | GOES-19 | GRÃO MOGOL | MINAS GERAIS | Brasil | 3127800 | 31 | 33 | nan | nan | nan | Cerrado | 81.3 |
| 829b4b90-c7bd-3c01-83c1-cb9a3cdef399 | -9.2123 | -45.3092 | 2025-09-20 01:00:00 | GOES-19 | BAIXA GRANDE DO RIBEIRO | PIAUÍ | Brasil | 2201150 | 22 | 33 | nan | nan | nan | Cerrado | 93.4 |
| a3e525cb-8c88-3ece-b43e-5c21a053fcfd | -4.368 | -46.291 | 2025-09-20 01:00:00 | GOES-19 | BURITICUPU | MARANHÃO | Brasil | 2102325 | 21 | 33 | nan | nan | nan | Amazônia | 60.3 |
| c284a095-a3db-3bc6-be0d-c880a2574f2d | -23.7414 | -51.7363 | 2025-09-20 01:00:00 | GOES-19 | MARUMBI | PARANÁ | Brasil | 4115507 | 41 | 33 | nan | nan | nan | Mata Atlântica | 85.3 |
| a3656c6e-5d5e-30a7-aefd-5137e18d8fcc | -5.9253 | -45.0718 | 2025-09-20 01:00:00 | GOES-19 | FERNANDO FALCÃO | MARANHÃO | Brasil | 2104081 | 21 | 33 | nan | nan | nan | Cerrado | 73.5 |
| 1d3548cd-ddd5-3860-bc1b-8efbcc0dc836 | -9.1933 | -45.3114 | 2025-09-20 01:00:00 | GOES-19 | BAIXA GRANDE DO RIBEIRO | PIAUÍ | Brasil | 2201150 | 22 | 33 | nan | nan | nan | Cerrado | 80.3 |
| 297684b0-cdc8-33a5-b471-29502cbcac7e | -23.7407 | -51.7592 | 2025-09-20 01:00:00 | GOES-19 | BOM SUCESSO | PARANÁ | Brasil | 4103206 | 41 | 33 | nan | nan | nan | Mata Atlântica | 76.1 |
| 8a22e8f1-6b89-3285-ba8a-aed36841042b | -5.944 | -45.0704 | 2025-09-20 01:00:00 | GOES-19 | FERNANDO FALCÃO | MARANHÃO | Brasil | 2104081 | 21 | 33 | nan | nan | nan | Cerrado | 83.1 |
| 8edc1d22-d3fe-36a6-8303-6ba954051e3c | -22.8118 | -45.2519 | 2025-09-20 01:10:00 | GOES-19 | GUARATINGUETÁ | SÃO PAULO | Brasil | 3518404 | 35 | 33 | nan | nan | nan | Mata Atlântica | 76.1 |
| 5d8c41fd-6db0-3f63-9ebc-5dc7550db615 | -22.8109 | -45.2767 | 2025-09-20 01:10:00 | GOES-19 | GUARATINGUETÁ | SÃO PAULO | Brasil | 3518404 | 35 | 33 | nan | nan | nan | Mata Atlântica | 92.2 |
| e73643f0-1fbf-3841-bdd0-41b52bedaf90 | -5.1934 | -45.4835 | 2025-09-20 01:10:00 | GOES-19 | JENIPAPO DOS VIEIRAS | MARANHÃO | Brasil | 2105476 | 21 | 33 | nan | nan | nan | Cerrado | 47.4 |
| 7557aa1c-fe5a-3af1-86dc-629a8bc05419 | -23.329 | -49.3469 | 2025-09-20 01:10:00 | GOES-19 | TEJUPÁ | SÃO PAULO | Brasil | 3554201 | 35 | 33 | nan | nan | nan | Mata Atlântica | 85.0 |
| e736e0fd-4520-3eec-863c-ac65dfbc238b | -7.3847 | -47.0378 | 2025-09-20 01:10:00 | GOES-19 | CAROLINA | MARANHÃO | Brasil | 2102804 | 21 | 33 | nan | nan | nan | Cerrado | 51.7 |
| 30e3ef51-a30c-37cd-90d1-036326481d3f | -5.1934 | -45.4835 | 2025-09-20 01:20:00 | GOES-19 | JENIPAPO DOS VIEIRAS | MARANHÃO | Brasil | 2105476 | 21 | 33 | nan | nan | nan | Cerrado | 39.2 |
| b26caaa4-0d07-3dda-a9d6-df8f618de8bf | -9.165 | -44.6273 | 2025-09-20 01:20:00 | GOES-19 | BOM JESUS | PIAUÍ | Brasil | 2201903 | 22 | 33 | nan | nan | nan | Cerrado | 76.4 |
| fb399d6e-bb88-3071-99f2-9959dec198df | -23.329 | -49.3469 | 2025-09-20 01:20:00 | GOES-19 | TEJUPÁ | SÃO PAULO | Brasil | 3554201 | 35 | 33 | nan | nan | nan | Mata Atlântica | 68.3 |
| c8525154-0a10-3e83-86f2-82d2abc71cef | -22.8109 | -45.2767 | 2025-09-20 01:20:00 | GOES-19 | GUARATINGUETÁ | SÃO PAULO | Brasil | 3518404 | 35 | 33 | nan | nan | nan | Mata Atlântica | 112.1 |
| 57888730-1cbf-3f6e-bd0b-0bb8528140f9 | -9.165 | -44.6273 | 2025-09-20 01:30:00 | GOES-19 | BOM JESUS | PIAUÍ | Brasil | 2201903 | 22 | 33 | nan | nan | nan | Cerrado | 78.6 |
| 34a8c979-bf83-319c-abf3-f2b02ef25fd9 | -22.8109 | -45.2767 | 2025-09-20 01:30:00 | GOES-19 | GUARATINGUETÁ | SÃO PAULO | Brasil | 3518404 | 35 | 33 | nan | nan | nan | Mata Atlântica | 121.2 |
| 031029e7-039d-3915-a9e6-582964c95a0d | -5.1181 | -43.1964 | 2025-09-20 01:30:00 | GOES-19 | CAXIAS | MARANHÃO | Brasil | 2103000 | 21 | 33 | nan | nan | nan | Cerrado | 92.7 |
| c34e0b44-9d34-3267-bf5e-caee082667ca | -23.329 | -49.3469 | 2025-09-20 01:30:00 | GOES-19 | TEJUPÁ | SÃO PAULO | Brasil | 3554201 | 35 | 33 | nan | nan | nan | Mata Atlântica | 68.7 |
| de465d96-7860-3aee-8255-47e1235b24de | -5.1934 | -45.4835 | 2025-09-20 01:30:00 | GOES-19 | JENIPAPO DOS VIEIRAS | MARANHÃO | Brasil | 2105476 | 21 | 33 | nan | nan | nan | Cerrado | 49.9 |
| ab48d7c9-04c8-3b91-8573-f7ae883c3690 | -5.118 | -43.2198 | 2025-09-20 01:30:00 | GOES-19 | CAXIAS | MARANHÃO | Brasil | 2103000 | 21 | 33 | nan | nan | nan | Cerrado | 45.5 |
| 5663f2ab-20b0-39b0-a94d-0d4c4af2791f | -5.0992 | -43.2211 | 2025-09-20 01:30:00 | GOES-19 | CAXIAS | MARANHÃO | Brasil | 2103000 | 21 | 33 | nan | nan | nan | Cerrado | 58.6 |
| 9fbb171f-f785-3d6e-9333-9d26378d92b6 | -5.0994 | -43.1977 | 2025-09-20 01:30:00 | GOES-19 | CAXIAS | MARANHÃO | Brasil | 2103000 | 21 | 33 | nan | nan | nan | Cerrado | 127.9 |
| 60fdc0d8-959b-3954-bd69-a8214a1ffdc7 | -22.8109 | -45.2767 | 2025-09-20 01:40:00 | GOES-19 | GUARATINGUETÁ | SÃO PAULO | Brasil | 3518404 | 35 | 33 | nan | nan | nan | Mata Atlântica | 100.5 |
| 72aac39e-72c2-30c5-abe0-0f3731eac8ce | -5.118 | -43.2198 | 2025-09-20 01:40:00 | GOES-19 | CAXIAS | MARANHÃO | Brasil | 2103000 | 21 | 33 | nan | nan | nan | Cerrado | 91.6 |
| c1ede2ba-3947-3a29-a6af-701e88dac065 | -5.0992 | -43.2211 | 2025-09-20 01:40:00 | GOES-19 | CAXIAS | MARANHÃO | Brasil | 2103000 | 21 | 33 | nan | nan | nan | Cerrado | 54.3 |
| 85ddb0cd-2932-31ac-94de-5c094456c982 | -19.4038 | -51.1527 | 2025-09-20 01:40:00 | GOES-19 | PARANAÍBA | MATO GROSSO DO SUL | Brasil | 5006309 | 50 | 33 | nan | nan | nan | Cerrado | 92.0 |
| e3c6a505-677d-306e-b8a8-a5fd9ec8b40c | -19.4043 | -51.1305 | 2025-09-20 01:40:00 | GOES-19 | PARANAÍBA | MATO GROSSO DO SUL | Brasil | 5006309 | 50 | 33 | nan | nan | nan | Cerrado | 100.1 |
| 467adc00-d3e1-353d-bf80-bbffa6764da2 | -5.0994 | -43.1977 | 2025-09-20 01:40:00 | GOES-19 | CAXIAS | MARANHÃO | Brasil | 2103000 | 21 | 33 | nan | nan | nan | Cerrado | 87.8 |
| 9f7c55b5-95e1-3033-97be-8d71ef0032bb | -5.1181 | -43.1964 | 2025-09-20 01:40:00 | GOES-19 | CAXIAS | MARANHÃO | Brasil | 2103000 | 21 | 33 | nan | nan | nan | Cerrado | 156.3 |
| 4cf39f42-8eb7-3524-b65d-740ea0268111 | -5.1934 | -45.4835 | 2025-09-20 01:40:00 | GOES-19 | JENIPAPO DOS VIEIRAS | MARANHÃO | Brasil | 2105476 | 21 | 33 | nan | nan | nan | Cerrado | 54.5 |
| f971f7f7-d28e-33cd-a652-75328aaaa4d5 | -7.3847 | -47.0378 | 2025-09-20 01:50:00 | GOES-19 | CAROLINA | MARANHÃO | Brasil | 2102804 | 21 | 33 | nan | nan | nan | Cerrado | 65.4 |
| 83b31a4f-aefd-3700-a5b7-e958dd4e8e08 | -5.1181 | -43.1964 | 2025-09-20 01:50:00 | GOES-19 | CAXIAS | MARANHÃO | Brasil | 2103000 | 21 | 33 | nan | nan | nan | Cerrado | 92.7 |
| ed8b5af0-af29-3027-af31-db48e281eca0 | -12.9049 | -46.7713 | 2025-09-20 01:50:00 | GOES-19 | ARRAIAS | TOCANTINS | Brasil | 1702406 | 17 | 33 | nan | nan | nan | Cerrado | 87.5 |
| fca59f0b-912f-3249-b332-6d1988700e66 | -5.0992 | -43.2211 | 2025-09-20 01:50:00 | GOES-19 | CAXIAS | MARANHÃO | Brasil | 2103000 | 21 | 33 | nan | nan | nan | Cerrado | 51.1 |
| d30e4925-f780-3fbc-8c8b-84352bf59e2b | -18.0502 | -50.935 | 2025-09-20 01:50:00 | GOES-19 | RIO VERDE | GOIÁS | Brasil | 5218805 | 52 | 33 | nan | nan | nan | Cerrado | 68.2 |
| 9e9cccaf-a613-3085-ba24-bd179e4732f1 | -12.9045 | -46.794 | 2025-09-20 01:50:00 | GOES-19 | ARRAIAS | TOCANTINS | Brasil | 1702406 | 17 | 33 | nan | nan | nan | Cerrado | 100.8 |
| 7c8fc698-9ec3-3db5-9ef9-95fc243086d0 | -5.0994 | -43.1977 | 2025-09-20 01:50:00 | GOES-19 | CAXIAS | MARANHÃO | Brasil | 2103000 | 21 | 33 | nan | nan | nan | Cerrado | 63.1 |
| 801b355a-6bfc-3934-be35-d3eaec580c2f | -5.118 | -43.2198 | 2025-09-20 01:50:00 | GOES-19 | CAXIAS | MARANHÃO | Brasil | 2103000 | 21 | 33 | nan | nan | nan | Cerrado | 70.4 |
| 99bde4c1-4d2f-3992-84fd-9ad53c73e7db | -18.0303 | -50.9385 | 2025-09-20 01:50:00 | GOES-19 | RIO VERDE | GOIÁS | Brasil | 5218805 | 52 | 33 | nan | nan | nan | Cerrado | 65.9 |


[Clique aqui para ver as próximas entradas](README5.md)
