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

## Dados Diários - Página 54

| ID | Latitude | Longitude | Data/Hora GMT | Satélite | Município | Estado | País | Município ID | Estado ID | País ID | Dias sem Chuva | Precipitação | Risco de Fogo | Bioma | FRP |
|----|----------|-----------|---------------|----------|-----------|--------|------|--------------|-----------|---------|----------------|--------------|----------------|-------|-----|
| 6db57ce7-8854-3b5d-b18b-b399114f2e57 | -7.6007 | -44.4952 | 2025-09-21 14:00:00 | GOES-19 | URUÇUÍ | PIAUÍ | Brasil | 2211209 | 22 | 33 | nan | nan | nan | Cerrado | 98.9 |
| e8dbb83d-f158-3139-b29f-7b2334f54e00 | -12.3399 | -44.0946 | 2025-09-21 14:00:00 | GOES-19 | TABOCAS DO BREJO VELHO | BAHIA | Brasil | 2930907 | 29 | 33 | nan | nan | nan | Cerrado | 401.0 |
| 1a38b58b-b316-3602-bd37-406bde8fc6c0 | -9.086 | -44.8663 | 2025-09-21 14:00:00 | GOES-19 | BOM JESUS | PIAUÍ | Brasil | 2201903 | 22 | 33 | nan | nan | nan | Cerrado | 63.3 |
| 9dc8ae7b-d268-39fa-9e88-a6a42cf4975e | -7.714 | -44.4612 | 2025-09-21 14:00:00 | GOES-19 | URUÇUÍ | PIAUÍ | Brasil | 2211209 | 22 | 33 | nan | nan | nan | Cerrado | 178.0 |
| 0b11c3b7-2f5e-320c-9f47-8621c8699f68 | -9.8822 | -46.116 | 2025-09-21 14:00:00 | GOES-19 | ALTO PARNAÍBA | MARANHÃO | Brasil | 2100501 | 21 | 33 | nan | nan | nan | Cerrado | 76.7 |
| a6b55984-9cd3-3d94-afdf-b5a09c5d5287 | -12.2794 | -45.2679 | 2025-09-21 14:00:00 | GOES-19 | BARREIRAS | BAHIA | Brasil | 2903201 | 29 | 33 | nan | nan | nan | Cerrado | 130.5 |
| 33939379-083d-345c-b7ce-8e4ddcec0006 | -9.8819 | -46.1386 | 2025-09-21 14:00:00 | GOES-19 | ALTO PARNAÍBA | MARANHÃO | Brasil | 2100501 | 21 | 33 | nan | nan | nan | Cerrado | 82.5 |
| 7bff457a-947c-3bd1-8a05-aadd13509ff4 | -12.6088 | -45.1244 | 2025-09-21 14:00:00 | GOES-19 | SÃO DESIDÉRIO | BAHIA | Brasil | 2928901 | 29 | 33 | nan | nan | nan | Cerrado | 460.1 |
| 165b7f5b-94c3-3578-99e1-f64b018c39ae | -7.5818 | -44.4971 | 2025-09-21 14:00:00 | GOES-19 | URUÇUÍ | PIAUÍ | Brasil | 2211209 | 22 | 33 | nan | nan | nan | Cerrado | 88.9 |
| eb9740ad-7e98-3ebe-8fdc-97e07a015cee | -11.215 | -49.6224 | 2025-09-21 14:00:00 | GOES-19 | DUERÉ | TOCANTINS | Brasil | 1707306 | 17 | 33 | nan | nan | nan | Cerrado | 82.8 |
| 4c21c279-2914-360e-8a05-bd876623be0e | -10.598 | -46.4573 | 2025-09-21 14:00:00 | GOES-19 | MATEIROS | TOCANTINS | Brasil | 1712702 | 17 | 33 | nan | nan | nan | Cerrado | 99.5 |
| 0a183d49-8fba-36d6-848e-d7e50f6d1aee | -10.2621 | -46.0703 | 2025-09-21 14:00:00 | GOES-19 | MATEIROS | TOCANTINS | Brasil | 1712702 | 17 | 33 | nan | nan | nan | Cerrado | 86.4 |
| 42ffa9e3-76e9-34fa-af8f-afcb79da28a9 | -12.2918 | -50.1417 | 2025-09-21 14:00:00 | GOES-19 | FORMOSO DO ARAGUAIA | TOCANTINS | Brasil | 1708205 | 17 | 33 | nan | nan | nan | Cerrado | 79.6 |
| d0245dde-bb7b-39f2-87cc-fb7d8ed31b3f | -11.1 | -49.7003 | 2025-09-21 14:10:00 | GOES-19 | DUERÉ | TOCANTINS | Brasil | 1707306 | 17 | 33 | nan | nan | nan | Cerrado | 83.5 |
| b7df500a-059a-398c-8747-7a7848102a60 | -5.5773 | -42.1255 | 2025-09-21 14:10:00 | GOES-19 | ALTO LONGÁ | PIAUÍ | Brasil | 2200301 | 22 | 33 | nan | nan | nan | Caatinga | 85.9 |
| 6cb80da2-eb2c-3105-b17f-723d73de3e78 | -5.5583 | -42.1507 | 2025-09-21 14:10:00 | GOES-19 | ALTO LONGÁ | PIAUÍ | Brasil | 2200301 | 22 | 33 | nan | nan | nan | Caatinga | 100.4 |
| e6647578-9941-383e-a795-c8231126091e | -8.8467 | -43.0326 | 2025-09-21 14:10:00 | GOES-19 | SÃO BRAZ DO PIAUÍ | PIAUÍ | Brasil | 2209559 | 22 | 33 | nan | nan | nan | Caatinga | 65.3 |
| 4dcf09a7-6fd0-359c-9d21-7ef43fb2140d | -12.6921 | -46.8482 | 2025-09-21 14:10:00 | GOES-19 | ARRAIAS | TOCANTINS | Brasil | 1702406 | 17 | 33 | nan | nan | nan | Cerrado | 101.8 |
| 6936b53d-6ae3-35ba-80d6-79b431d2fcac | -9.771 | -45.9484 | 2025-09-21 14:10:00 | GOES-19 | ALTO PARNAÍBA | MARANHÃO | Brasil | 2100501 | 21 | 33 | nan | nan | nan | Cerrado | 69.3 |
| c206f2b8-a2d3-3a9c-a7a2-2d65b4873dd7 | -12.711 | -46.868 | 2025-09-21 14:10:00 | GOES-19 | ARRAIAS | TOCANTINS | Brasil | 1702406 | 17 | 33 | nan | nan | nan | Cerrado | 114.5 |
| 1d2fa803-961d-378c-8640-a0b5c56b3654 | -14.8675 | -45.481 | 2025-09-21 14:10:00 | GOES-19 | COCOS | BAHIA | Brasil | 2908101 | 29 | 33 | nan | nan | nan | Cerrado | 206.5 |
| 636f000f-7cd2-3d53-9008-f44bd7ce18ae | -14.7877 | -51.3836 | 2025-09-21 14:10:00 | GOES-19 | COCALINHO | MATO GROSSO | Brasil | 5103106 | 51 | 33 | nan | nan | nan | Cerrado | 58.8 |
| 8223ed26-93ab-3374-b048-82ec659ab115 | -9.8629 | -46.1408 | 2025-09-21 14:10:00 | GOES-19 | ALTO PARNAÍBA | MARANHÃO | Brasil | 2100501 | 21 | 33 | nan | nan | nan | Cerrado | 76.0 |
| 859d82ca-e372-3dcc-be25-8141dc1ffa01 | -17.1173 | -45.9491 | 2025-09-21 14:10:00 | GOES-19 | BRASILÂNDIA DE MINAS | MINAS GERAIS | Brasil | 3108552 | 31 | 33 | nan | nan | nan | Cerrado | 122.5 |
| db37847c-1910-3802-9f8b-4a3c8088b675 | -7.714 | -44.4612 | 2025-09-21 14:10:00 | GOES-19 | URUÇUÍ | PIAUÍ | Brasil | 2211209 | 22 | 33 | nan | nan | nan | Cerrado | 139.8 |
| fe04464f-33a0-3acc-af64-303417aa9b0d | -9.165 | -44.6273 | 2025-09-21 14:10:00 | GOES-19 | BOM JESUS | PIAUÍ | Brasil | 2201903 | 22 | 33 | nan | nan | nan | Cerrado | 77.9 |
| eab3aa73-bfb8-3ef3-a8c0-65b897e8b59d | -7.9468 | -43.9061 | 2025-09-21 14:10:00 | GOES-19 | BERTOLÍNIA | PIAUÍ | Brasil | 2201705 | 22 | 33 | nan | nan | nan | Cerrado | 64.6 |
| 4ce1bbb4-521d-32b8-b6cb-d6f0f55c931f | -14.8071 | -51.3809 | 2025-09-21 14:10:00 | GOES-19 | COCALINHO | MATO GROSSO | Brasil | 5103106 | 51 | 33 | nan | nan | nan | Cerrado | 68.3 |
| 859246e4-f645-315b-90f0-daf112d0395c | -10.0128 | -46.2583 | 2025-09-21 14:10:00 | GOES-19 | ALTO PARNAÍBA | MARANHÃO | Brasil | 2100501 | 21 | 33 | nan | nan | nan | Cerrado | 73.3 |
| 8d77169e-0e7d-3d32-a04e-3ce194dd4259 | -9.8822 | -46.116 | 2025-09-21 14:10:00 | GOES-19 | ALTO PARNAÍBA | MARANHÃO | Brasil | 2100501 | 21 | 33 | nan | nan | nan | Cerrado | 72.6 |
| fa138d58-0708-35dc-8ca6-70d012853594 | -4.388 | -43.2896 | 2025-09-21 14:10:00 | GOES-19 | ALDEIAS ALTAS | MARANHÃO | Brasil | 2100303 | 21 | 33 | nan | nan | nan | Cerrado | 80.6 |
| 6b53b3b8-3021-36c1-85cd-8eda0a170dec | -10.0317 | -46.2561 | 2025-09-21 14:10:00 | GOES-19 | ALTO PARNAÍBA | MARANHÃO | Brasil | 2100501 | 21 | 33 | nan | nan | nan | Cerrado | 121.6 |
| b85ae546-30fa-3904-bae2-c94969c82bd0 | -16.8926 | -43.8849 | 2025-09-21 14:10:00 | GOES-19 | MONTES CLAROS | MINAS GERAIS | Brasil | 3143302 | 31 | 33 | nan | nan | nan | Cerrado | 66.4 |
| ccc03143-7a96-3065-9823-98089258cbec | -6.704 | -44.0017 | 2025-09-21 14:10:00 | GOES-19 | NOVA IORQUE | MARANHÃO | Brasil | 2107308 | 21 | 33 | nan | nan | nan | Cerrado | 134.5 |
| 4853f1ec-b63a-386e-a637-bd904916002f | -12.7302 | -46.8651 | 2025-09-21 14:10:00 | GOES-19 | ARRAIAS | TOCANTINS | Brasil | 1702406 | 17 | 33 | nan | nan | nan | Cerrado | 74.1 |
| 9bb7707a-291d-30d7-b4c0-622fbc3a1247 | -12.7294 | -47.9845 | 2025-09-21 14:10:00 | GOES-19 | PARANÃ | TOCANTINS | Brasil | 1716208 | 17 | 33 | nan | nan | nan | Cerrado | 92.1 |
| 83718d6c-cc42-3f11-9882-bd75632a209f | -9.0078 | -45.0584 | 2025-09-21 14:10:00 | GOES-19 | CURRAIS | PIAUÍ | Brasil | 2203230 | 22 | 33 | nan | nan | nan | Cerrado | 67.2 |
| dd237dd4-4959-3eeb-8786-17f22cabfd1e | -8.8801 | -46.138 | 2025-09-21 14:10:00 | GOES-19 | ALTO PARNAÍBA | MARANHÃO | Brasil | 2100501 | 21 | 33 | nan | nan | nan | Cerrado | 57.8 |
| c12aa625-e64e-3e81-b8c8-e6b8627f4125 | -2.9903 | -42.8689 | 2025-09-21 14:10:00 | GOES-19 | BARREIRINHAS | MARANHÃO | Brasil | 2101707 | 21 | 33 | nan | nan | nan | Cerrado | 86.1 |
| d5b78263-98ad-393a-9dd1-b087dcfdaaa2 | -12.279 | -45.291 | 2025-09-21 14:10:00 | GOES-19 | BARREIRAS | BAHIA | Brasil | 2903201 | 29 | 33 | nan | nan | nan | Cerrado | 164.5 |
| 432fa388-c32a-3074-82cf-f3fb91dc5d93 | -9.1744 | -45.3135 | 2025-09-21 14:10:00 | GOES-19 | BAIXA GRANDE DO RIBEIRO | PIAUÍ | Brasil | 2201150 | 22 | 33 | nan | nan | nan | Cerrado | 84.2 |
| bfbb2afa-13f2-339a-82a2-400c08d4659c | -12.8969 | -50.5398 | 2025-09-21 14:10:00 | GOES-19 | COCALINHO | MATO GROSSO | Brasil | 5103106 | 51 | 33 | nan | nan | nan | Cerrado | 92.2 |
| 34ed17b7-cf8f-372a-8e8a-066761e6ddba | -10.2811 | -46.0679 | 2025-09-21 14:10:00 | GOES-19 | MATEIROS | TOCANTINS | Brasil | 1712702 | 17 | 33 | nan | nan | nan | Cerrado | 112.7 |
| aa776bbf-1bbf-3d4b-8890-2871fb8f3bbe | -12.8965 | -50.5614 | 2025-09-21 14:10:00 | GOES-19 | COCALINHO | MATO GROSSO | Brasil | 5103106 | 51 | 33 | nan | nan | nan | Cerrado | 72.0 |
| f96a7e71-9c79-3e9d-9a79-8b87b7d86f0e | -12.2794 | -45.2679 | 2025-09-21 14:10:00 | GOES-19 | BARREIRAS | BAHIA | Brasil | 2903201 | 29 | 33 | nan | nan | nan | Cerrado | 203.4 |
| 7d46ea7b-50bf-3d68-8cca-4a6046687e91 | -12.0767 | -44.8131 | 2025-09-21 14:10:00 | GOES-19 | ANGICAL | BAHIA | Brasil | 2901403 | 29 | 33 | nan | nan | nan | Cerrado | 98.5 |
| b8949996-d1fd-3aa2-b7a3-760de54c3701 | -10.0547 | -45.9824 | 2025-09-21 14:10:00 | GOES-19 | ALTO PARNAÍBA | MARANHÃO | Brasil | 2100501 | 21 | 33 | nan | nan | nan | Cerrado | 67.3 |
| 673c4d65-4e73-379b-a194-181b82ba494b | -12.2983 | -45.2881 | 2025-09-21 14:10:00 | GOES-19 | BARREIRAS | BAHIA | Brasil | 2903201 | 29 | 33 | nan | nan | nan | Cerrado | 593.3 |
| effd77d4-5cda-3d11-8910-32cc57a32f83 | -10.8805 | -46.6241 | 2025-09-21 14:10:00 | GOES-19 | MATEIROS | TOCANTINS | Brasil | 1712702 | 17 | 33 | nan | nan | nan | Cerrado | 91.6 |
| ec635cf4-acc6-3627-8d3f-925535b3d272 | -12.3133 | -49.9881 | 2025-09-21 14:10:00 | GOES-19 | SANDOLÂNDIA | TOCANTINS | Brasil | 1718840 | 17 | 33 | nan | nan | nan | Cerrado | 72.7 |
| b5c90b77-5b64-3d6b-8bb9-d808dc6abbe0 | -7.5275 | -44.3182 | 2025-09-21 14:10:00 | GOES-19 | URUÇUÍ | PIAUÍ | Brasil | 2211209 | 22 | 33 | nan | nan | nan | Cerrado | 78.9 |
| d89a011c-5232-3924-99c9-e4d61ab695ca | -10.0314 | -46.2786 | 2025-09-21 14:10:00 | GOES-19 | ALTO PARNAÍBA | MARANHÃO | Brasil | 2100501 | 21 | 33 | nan | nan | nan | Cerrado | 78.3 |
| 233497af-523e-3f2e-861b-b0e0bd5a7b5f | -10.2621 | -46.0703 | 2025-09-21 14:10:00 | GOES-19 | MATEIROS | TOCANTINS | Brasil | 1712702 | 17 | 33 | nan | nan | nan | Cerrado | 83.7 |
| 4022d789-0b0e-3aa7-ae7d-5da41db8cb57 | -2.953 | -42.8704 | 2025-09-21 14:10:00 | GOES-19 | BARREIRINHAS | MARANHÃO | Brasil | 2101707 | 21 | 33 | nan | nan | nan | Cerrado | 84.1 |
| ad994d63-22fe-3f2e-a166-1704e55d5fc7 | -9.184 | -44.6251 | 2025-09-21 14:10:00 | GOES-19 | BOM JESUS | PIAUÍ | Brasil | 2201903 | 22 | 33 | nan | nan | nan | Cerrado | 158.6 |
| f145bd44-28c3-307b-8852-f2f950dd24fb | -14.6047 | -49.7624 | 2025-09-21 14:10:00 | GOES-19 | GUARINOS | GOIÁS | Brasil | 5209457 | 52 | 33 | nan | nan | nan | Cerrado | 50.4 |
| 529337f3-b56c-344e-a1da-fa33e86b86b4 | -18.8431 | -42.1747 | 2025-09-21 14:10:00 | GOES-19 | GOVERNADOR VALADARES | MINAS GERAIS | Brasil | 3127701 | 31 | 33 | nan | nan | nan | Mata Atlântica | 107.5 |
| ae200515-d6fc-335c-aef1-f7436aa013c0 | -5.3711 | -42.0937 | 2025-09-21 14:10:00 | GOES-19 | ALTO LONGÁ | PIAUÍ | Brasil | 2200301 | 22 | 33 | nan | nan | nan | Caatinga | 102.1 |
| 49ba9e9e-9555-326e-9599-7486d0348f96 | -12.1344 | -44.8042 | 2025-09-21 14:10:00 | GOES-19 | BARREIRAS | BAHIA | Brasil | 2903201 | 29 | 33 | nan | nan | nan | Cerrado | 156.2 |
| a6757b9a-dcc8-3840-8b99-cc249ba7d031 | -10.598 | -46.4573 | 2025-09-21 14:10:00 | GOES-19 | MATEIROS | TOCANTINS | Brasil | 1712702 | 17 | 33 | nan | nan | nan | Cerrado | 180.3 |
| 8d26bf48-d1a6-3932-b458-4b994ad0ffa3 | -12.2918 | -50.1417 | 2025-09-21 14:10:00 | GOES-19 | FORMOSO DO ARAGUAIA | TOCANTINS | Brasil | 1708205 | 17 | 33 | nan | nan | nan | Cerrado | 75.0 |
| 19e736d6-59df-38af-8ea2-0387b38dc605 | -11.215 | -49.6224 | 2025-09-21 14:10:00 | GOES-19 | DUERÉ | TOCANTINS | Brasil | 1707306 | 17 | 33 | nan | nan | nan | Cerrado | 85.7 |
| c61395a8-a5a2-3bd9-982f-af3315cc4903 | -9.1837 | -44.6482 | 2025-09-21 14:10:00 | GOES-19 | BOM JESUS | PIAUÍ | Brasil | 2201903 | 22 | 33 | nan | nan | nan | Cerrado | 75.3 |
| faabf70a-e4be-3074-bada-dd8ecd8e60a9 | -12.1156 | -44.7839 | 2025-09-21 14:10:00 | GOES-19 | BARREIRAS | BAHIA | Brasil | 2903201 | 29 | 33 | nan | nan | nan | Cerrado | 120.2 |
| 14d8f6a6-f729-307e-9a72-dd31377c446f | -14.8479 | -45.4846 | 2025-09-21 14:10:00 | GOES-19 | COCOS | BAHIA | Brasil | 2908101 | 29 | 33 | nan | nan | nan | Cerrado | 188.7 |
| ebd555dd-a54d-32af-824e-3df4a28bdb58 | -10.6932 | -46.4453 | 2025-09-21 14:10:00 | GOES-19 | MATEIROS | TOCANTINS | Brasil | 1712702 | 17 | 33 | nan | nan | nan | Cerrado | 264.6 |
| 57665156-a858-3bcd-871d-ed6d56ea8357 | -12.144 | -44.2899 | 2025-09-21 14:10:00 | GOES-19 | CRISTÓPOLIS | BAHIA | Brasil | 2909703 | 29 | 33 | nan | nan | nan | Cerrado | 78.0 |
| 329c8d8f-5056-3b49-8229-93d86ecc440e | -9.1937 | -45.2886 | 2025-09-21 14:10:00 | GOES-19 | BAIXA GRANDE DO RIBEIRO | PIAUÍ | Brasil | 2201150 | 22 | 33 | nan | nan | nan | Cerrado | 86.6 |
| 2e7f6e3a-15a4-326f-8d4e-02be1d876b9c | -7.5272 | -44.3413 | 2025-09-21 14:10:00 | GOES-19 | URUÇUÍ | PIAUÍ | Brasil | 2211209 | 22 | 33 | nan | nan | nan | Cerrado | 94.7 |
| 58dfb7d8-ef0a-3684-b8b0-a2098ddbe432 | -12.8777 | -50.5422 | 2025-09-21 14:10:00 | GOES-19 | COCALINHO | MATO GROSSO | Brasil | 5103106 | 51 | 33 | nan | nan | nan | Cerrado | 83.0 |
| 23229663-152d-3e0c-911c-4385e4336bbc | -12.8781 | -50.5207 | 2025-09-21 14:10:00 | GOES-19 | COCALINHO | MATO GROSSO | Brasil | 5103106 | 51 | 33 | nan | nan | nan | Cerrado | 133.5 |
| 26f027a7-cd1a-323e-b92c-0223391867e5 | -11.2306 | -46.1722 | 2025-09-21 14:10:00 | GOES-19 | FORMOSA DO RIO PRETO | BAHIA | Brasil | 2911105 | 29 | 33 | nan | nan | nan | Cerrado | 195.9 |
| 29e74dcf-ec9d-3212-8040-54cd56d62607 | -12.2987 | -45.2649 | 2025-09-21 14:10:00 | GOES-19 | BARREIRAS | BAHIA | Brasil | 2903201 | 29 | 33 | nan | nan | nan | Cerrado | 614.8 |
| b2cd9046-f5ef-3f8a-b733-0463da4938fa | -12.9157 | -50.5589 | 2025-09-21 14:10:00 | GOES-19 | COCALINHO | MATO GROSSO | Brasil | 5103106 | 51 | 33 | nan | nan | nan | Cerrado | 85.5 |
| d125f004-7712-3eee-ab6f-a72b38ba828f | -15.0508 | -55.283 | 2025-09-21 14:10:00 | GOES-19 | CHAPADA DOS GUIMARÃES | MATO GROSSO | Brasil | 5103007 | 51 | 33 | nan | nan | nan | Cerrado | 127.4 |
| e183926b-9bcd-3dcd-a03e-b2a1112912e8 | -10.617 | -46.4549 | 2025-09-21 14:10:00 | GOES-19 | MATEIROS | TOCANTINS | Brasil | 1712702 | 17 | 33 | nan | nan | nan | Cerrado | 118.0 |
| 25fb84d2-e161-31dd-a154-4ba60035f5f2 | 4.3344 | -60.7406 | 2025-09-21 14:10:00 | GOES-19 | PACARAIMA | RORAIMA | Brasil | 1400456 | 14 | 33 | nan | nan | nan | Amazônia | 57.0 |
| 55117e94-d4cf-363a-9ac5-5b2a54a346df | -9.1747 | -45.2907 | 2025-09-21 14:10:00 | GOES-19 | BAIXA GRANDE DO RIBEIRO | PIAUÍ | Brasil | 2201150 | 22 | 33 | nan | nan | nan | Cerrado | 86.0 |
| bdf8eff3-8660-33fb-80d6-c38875613203 | -7.9471 | -43.8828 | 2025-09-21 14:10:00 | GOES-19 | BERTOLÍNIA | PIAUÍ | Brasil | 2201705 | 22 | 33 | nan | nan | nan | Cerrado | 67.4 |
| 02723568-9de6-372f-9b8f-44fa4243bc09 | -12.7114 | -46.8454 | 2025-09-21 14:10:00 | GOES-19 | ARRAIAS | TOCANTINS | Brasil | 1702406 | 17 | 33 | nan | nan | nan | Cerrado | 190.0 |
| 7e2093de-fe5e-3136-9841-d969c0d85449 | -8.8615 | -46.1175 | 2025-09-21 14:10:00 | GOES-19 | ALTO PARNAÍBA | MARANHÃO | Brasil | 2100501 | 21 | 33 | nan | nan | nan | Cerrado | 58.5 |
| e2dcce2b-7551-3606-8e5e-80a4220edc6a | -2.9528 | -42.8938 | 2025-09-21 14:10:00 | GOES-19 | BARREIRINHAS | MARANHÃO | Brasil | 2101707 | 21 | 33 | nan | nan | nan | Cerrado | 99.2 |
| 15550e78-2940-33ac-8e0b-287ce4e95f9f | -7.6007 | -44.4952 | 2025-09-21 14:10:00 | GOES-19 | URUÇUÍ | PIAUÍ | Brasil | 2211209 | 22 | 33 | nan | nan | nan | Cerrado | 97.3 |
| 34a22a8e-1b17-33ec-a671-e676b7031b99 | -12.3399 | -44.0946 | 2025-09-21 14:10:00 | GOES-19 | TABOCAS DO BREJO VELHO | BAHIA | Brasil | 2930907 | 29 | 33 | nan | nan | nan | Cerrado | 87.4 |
| 8dae4f5f-69d6-3e7d-8022-8fd6a8e81970 | -8.8993 | -46.1135 | 2025-09-21 14:10:00 | GOES-19 | ALTO PARNAÍBA | MARANHÃO | Brasil | 2100501 | 21 | 33 | nan | nan | nan | Cerrado | 62.2 |
| 924f45cc-4a8b-32a8-b9e9-dd00385b0c48 | -7.966 | -43.8809 | 2025-09-21 14:10:00 | GOES-19 | BERTOLÍNIA | PIAUÍ | Brasil | 2201705 | 22 | 33 | nan | nan | nan | Cerrado | 68.5 |
| 671b47d2-88aa-3a78-90fb-e0fdad0a5dba | -12.7341 | -47.7168 | 2025-09-21 14:10:00 | GOES-19 | PARANÃ | TOCANTINS | Brasil | 1716208 | 17 | 33 | nan | nan | nan | Cerrado | 130.3 |
| 0412e1f1-afea-39a9-9df5-fc31f15d5dbc | -5.5771 | -42.1493 | 2025-09-21 14:10:00 | GOES-19 | ALTO LONGÁ | PIAUÍ | Brasil | 2200301 | 22 | 33 | nan | nan | nan | Caatinga | 109.7 |
| fe298949-7475-3227-aec2-802a3e809164 | -15.0511 | -55.2624 | 2025-09-21 14:10:00 | GOES-19 | CHAPADA DOS GUIMARÃES | MATO GROSSO | Brasil | 5103007 | 51 | 33 | nan | nan | nan | Cerrado | 64.6 |
| c1a105a9-7663-3ee0-8fe1-c18b25fe87dc | -10.0507 | -46.2538 | 2025-09-21 14:10:00 | GOES-19 | ALTO PARNAÍBA | MARANHÃO | Brasil | 2100501 | 21 | 33 | nan | nan | nan | Cerrado | 66.4 |
| aeee436a-1fb3-3477-a6f9-60ab8960927a | -14.3136 | -47.7913 | 2025-09-21 14:10:00 | GOES-19 | ALTO PARAÍSO DE GOIÁS | GOIÁS | Brasil | 5200605 | 52 | 33 | nan | nan | nan | Cerrado | 46.2 |
| 9f00296c-5f2c-3aca-9c2e-bb69a512844a | -12.8589 | -50.5231 | 2025-09-21 14:10:00 | GOES-19 | COCALINHO | MATO GROSSO | Brasil | 5103106 | 51 | 33 | nan | nan | nan | Cerrado | 119.3 |
| 4b7924ef-73bb-3c03-a71d-dcf2a58e911d | -12.2726 | -50.1441 | 2025-09-21 14:10:00 | GOES-19 | FORMOSO DO ARAGUAIA | TOCANTINS | Brasil | 1708205 | 17 | 33 | nan | nan | nan | Cerrado | 72.5 |
| 94bbf442-7ede-3fbd-a620-85075d087689 | -10.6741 | -46.4477 | 2025-09-21 14:10:00 | GOES-19 | MATEIROS | TOCANTINS | Brasil | 1712702 | 17 | 33 | nan | nan | nan | Cerrado | 131.5 |
| f983c1f6-0543-37f4-a1fe-dac404374c12 | -12.4056 | -51.4113 | 2025-09-21 14:10:00 | GOES-19 | BOM JESUS DO ARAGUAIA | MATO GROSSO | Brasil | 5101852 | 51 | 33 | nan | nan | nan | Cerrado | 71.9 |
| d04cbb68-e108-3bbc-95cc-446d96b9e2a4 | -9.184 | -44.6251 | 2025-09-21 14:20:00 | GOES-19 | BOM JESUS | PIAUÍ | Brasil | 2201903 | 22 | 33 | nan | nan | nan | Cerrado | 76.9 |
| 8d075be2-54b3-3361-8844-db71ec93383c | -22.2409 | -55.9863 | 2025-09-21 14:20:00 | GOES-19 | ANTÔNIO JOÃO | MATO GROSSO DO SUL | Brasil | 5000906 | 50 | 33 | nan | nan | nan | Cerrado | 70.0 |
| 64439802-a48a-3c38-beb1-db44ea862373 | -12.6921 | -46.8482 | 2025-09-21 14:20:00 | GOES-19 | ARRAIAS | TOCANTINS | Brasil | 1702406 | 17 | 33 | nan | nan | nan | Cerrado | 85.5 |
| de69e2b5-b69e-3191-9c89-d9b142edbda8 | -12.2987 | -45.2649 | 2025-09-21 14:20:00 | GOES-19 | BARREIRAS | BAHIA | Brasil | 2903201 | 29 | 33 | nan | nan | nan | Cerrado | 317.4 |
| f6157f67-0868-33f8-a727-8d907b549cc0 | -11.215 | -49.6224 | 2025-09-21 14:20:00 | GOES-19 | DUERÉ | TOCANTINS | Brasil | 1707306 | 17 | 33 | nan | nan | nan | Cerrado | 90.8 |


[Clique aqui para ver as próximas entradas](README55.md)
