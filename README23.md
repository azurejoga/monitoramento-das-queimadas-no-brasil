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
| be953efd-759d-3db3-a8d0-0687934cd719 | -7.19013 | -44.41593 | 2025-09-19 04:46:00 | NOAA-21 | URUÇUÍ | PIAUÍ | Brasil | 2211209 | 22 | 33 | nan | nan | nan | Cerrado | 3.7 |
| f1d90bcd-c185-39d8-b47d-d3d117200077 | -8.92842 | -46.31451 | 2025-09-19 04:46:00 | NOAA-21 | ALTO PARNAÍBA | MARANHÃO | Brasil | 2100501 | 21 | 33 | nan | nan | nan | Cerrado | 1.3 |
| 4854bba7-fb03-3056-875a-960f17231980 | -7.84052 | -46.21659 | 2025-09-19 04:46:00 | NOAA-21 | BALSAS | MARANHÃO | Brasil | 2101400 | 21 | 33 | nan | nan | nan | Cerrado | 2.6 |
| 68a37f6f-563d-319c-af1b-b3da90300fd8 | -9.14386 | -44.85243 | 2025-09-19 04:46:00 | NOAA-21 | BOM JESUS | PIAUÍ | Brasil | 2201903 | 22 | 33 | nan | nan | nan | Cerrado | 6.0 |
| 6128945a-0d3c-351d-8f0f-1100c7bbe03f | -11.57628 | -50.49592 | 2025-09-19 04:46:00 | NOAA-21 | FORMOSO DO ARAGUAIA | TOCANTINS | Brasil | 1708205 | 17 | 33 | nan | nan | nan | Cerrado | 1.9 |
| cea1732c-2252-3f00-935c-58ef6683d98c | -7.30619 | -45.17313 | 2025-09-19 04:46:00 | NOAA-21 | LORETO | MARANHÃO | Brasil | 2106102 | 21 | 33 | nan | nan | nan | Cerrado | 2.3 |
| fabb79bf-74ef-331f-8afa-a2617d1d87d6 | -7.28788 | -43.93253 | 2025-09-19 04:46:00 | NOAA-21 | LANDRI SALES | PIAUÍ | Brasil | 2205607 | 22 | 33 | nan | nan | nan | Cerrado | 5.6 |
| d98f89c7-5212-3207-8114-1ef5bccb357c | -7.55973 | -45.47946 | 2025-09-19 04:46:00 | NOAA-21 | LORETO | MARANHÃO | Brasil | 2106102 | 21 | 33 | nan | nan | nan | Cerrado | 4.6 |
| 18a4331d-9982-36e8-98e3-75af83e33a29 | -11.21192 | -49.62925 | 2025-09-19 04:46:00 | NOAA-21 | DUERÉ | TOCANTINS | Brasil | 1707306 | 17 | 33 | nan | nan | nan | Cerrado | 7.4 |
| 3993a893-fd74-3d63-a92d-5f0c0c471b8c | -7.23306 | -46.60205 | 2025-09-19 04:46:00 | NOAA-21 | RIACHÃO | MARANHÃO | Brasil | 2109502 | 21 | 33 | nan | nan | nan | Cerrado | 1.6 |
| 2c005e32-4b16-3d2a-90bd-9bd6e090e6c9 | -6.26764 | -43.91591 | 2025-09-19 04:46:00 | NOAA-21 | PASSAGEM FRANCA | MARANHÃO | Brasil | 2107902 | 21 | 33 | nan | nan | nan | Cerrado | 62.6 |
| 86e0bf0b-82e5-3262-84fd-42ef1a290d17 | -6.90563 | -44.76847 | 2025-09-19 04:46:00 | NOAA-21 | SÃO FÉLIX DE BALSAS | MARANHÃO | Brasil | 2110807 | 21 | 33 | nan | nan | nan | Cerrado | 13.1 |
| ba688822-76b3-3d00-a219-590b06345f0d | -5.54621 | -51.36703 | 2025-09-19 04:46:00 | NOAA-21 | SÃO FÉLIX DO XINGU | PARÁ | Brasil | 1507300 | 15 | 33 | nan | nan | nan | Amazônia | 0.8 |
| 6edc8d43-15c6-3176-81c1-e2bb100fdfe0 | -7.3578 | -44.59061 | 2025-09-19 04:46:00 | NOAA-21 | URUÇUÍ | PIAUÍ | Brasil | 2211209 | 22 | 33 | nan | nan | nan | Cerrado | 2.5 |
| 1aa40cf8-0ed0-35af-9570-a3e2faee4c97 | -5.96273 | -47.0952 | 2025-09-19 04:46:00 | NOAA-21 | MONTES ALTOS | MARANHÃO | Brasil | 2107001 | 21 | 33 | nan | nan | nan | Cerrado | 2.6 |
| f2c0805a-d603-38a7-b156-c181eb3276e2 | -7.57422 | -45.46959 | 2025-09-19 04:46:00 | NOAA-21 | LORETO | MARANHÃO | Brasil | 2106102 | 21 | 33 | nan | nan | nan | Cerrado | 1.3 |
| dcdf69bf-c7a7-3355-89cb-4142667755a0 | -9.16473 | -44.90324 | 2025-09-19 04:46:00 | NOAA-21 | BOM JESUS | PIAUÍ | Brasil | 2201903 | 22 | 33 | nan | nan | nan | Cerrado | 2.5 |
| b345971f-8189-35f2-97b2-dc12d9d749e9 | -7.90445 | -48.16451 | 2025-09-19 04:46:00 | NOAA-21 | PALMEIRANTE | TOCANTINS | Brasil | 1715705 | 17 | 33 | nan | nan | nan | Cerrado | 7.3 |
| 6e216d4f-37db-3ac1-a3a3-48c6c4c63499 | -8.74939 | -44.23323 | 2025-09-19 04:46:00 | NOAA-21 | PALMEIRA DO PIAUÍ | PIAUÍ | Brasil | 2207405 | 22 | 33 | nan | nan | nan | Cerrado | 1.3 |
| 32593779-1ba7-32b9-a8a3-446a7db1cde2 | -5.43876 | -46.68437 | 2025-09-19 04:46:00 | NOAA-21 | AMARANTE DO MARANHÃO | MARANHÃO | Brasil | 2100600 | 21 | 33 | nan | nan | nan | Cerrado | 1.5 |
| 25bb19e6-0ae4-309b-a7e4-e85c9a7fe420 | -6.17328 | -45.11055 | 2025-09-19 04:46:00 | NOAA-21 | FERNANDO FALCÃO | MARANHÃO | Brasil | 2104081 | 21 | 33 | nan | nan | nan | Cerrado | 1.5 |
| 2fe6102f-e7e1-3531-899f-c0be32725576 | -9.18397 | -45.31404 | 2025-09-19 04:46:00 | NOAA-21 | BAIXA GRANDE DO RIBEIRO | PIAUÍ | Brasil | 2201150 | 22 | 33 | nan | nan | nan | Cerrado | 9.5 |
| 0b6cc130-6201-3a04-b7d4-a40bcc29f5e8 | -8.13837 | -44.46946 | 2025-09-19 04:46:00 | NOAA-21 | URUÇUÍ | PIAUÍ | Brasil | 2211209 | 22 | 33 | nan | nan | nan | Cerrado | 7.1 |
| 9c8e7c80-8e92-32e9-80d4-3c76cbe7628c | -5.8003 | -43.90435 | 2025-09-19 04:46:00 | NOAA-21 | BURITI BRAVO | MARANHÃO | Brasil | 2102309 | 21 | 33 | nan | nan | nan | Cerrado | 2.5 |
| ab8e5f2f-1d3d-3ca2-86a3-734a0dbca153 | -12.09304 | -44.83891 | 2025-09-19 04:46:00 | NOAA-21 | ANGICAL | BAHIA | Brasil | 2901403 | 29 | 33 | nan | nan | nan | Cerrado | 3.2 |
| 1fe36c4c-9133-364d-85c0-d211058e4a69 | -7.29045 | -44.13334 | 2025-09-19 04:46:00 | NOAA-21 | ANTÔNIO ALMEIDA | PIAUÍ | Brasil | 2200806 | 22 | 33 | nan | nan | nan | Cerrado | 3.6 |
| b480e911-9aa3-32d9-bdce-779750ade4fe | -9.7292 | -45.92789 | 2025-09-19 04:46:00 | NOAA-21 | ALTO PARNAÍBA | MARANHÃO | Brasil | 2100501 | 21 | 33 | nan | nan | nan | Cerrado | 1.7 |
| 2963b052-6372-3871-83de-2416fea330a1 | -9.13965 | -44.64062 | 2025-09-19 04:46:00 | NOAA-21 | BOM JESUS | PIAUÍ | Brasil | 2201903 | 22 | 33 | nan | nan | nan | Cerrado | 2.1 |
| d514976e-ea3b-397f-b494-854625129096 | -5.43948 | -46.6796 | 2025-09-19 04:46:00 | NOAA-21 | AMARANTE DO MARANHÃO | MARANHÃO | Brasil | 2100600 | 21 | 33 | nan | nan | nan | Cerrado | 1.5 |
| 937f3fb1-369c-3fea-99aa-6a21dfd23578 | -6.39452 | -43.32561 | 2025-09-19 04:46:00 | NOAA-21 | BARÃO DE GRAJAÚ | MARANHÃO | Brasil | 2101509 | 21 | 33 | nan | nan | nan | Cerrado | 4.2 |
| a588843d-ac40-3018-9a0e-7848872121c7 | -7.18495 | -44.41957 | 2025-09-19 04:46:00 | NOAA-21 | URUÇUÍ | PIAUÍ | Brasil | 2211209 | 22 | 33 | nan | nan | nan | Cerrado | 4.1 |
| c119ac46-968c-351b-a8e5-6d641b301533 | -7.56287 | -45.48795 | 2025-09-19 04:46:00 | NOAA-21 | LORETO | MARANHÃO | Brasil | 2106102 | 21 | 33 | nan | nan | nan | Cerrado | 1.2 |
| afc76255-eeba-3b67-b9dd-dade58f9d767 | -7.65415 | -45.13584 | 2025-09-19 04:46:00 | NOAA-21 | RIBEIRO GONÇALVES | PIAUÍ | Brasil | 2208908 | 22 | 33 | nan | nan | nan | Cerrado | 1.8 |
| 6b826c1f-09d7-32e0-a0bb-c336ed8663da | -5.54182 | -51.37342 | 2025-09-19 04:46:00 | NOAA-21 | SÃO FÉLIX DO XINGU | PARÁ | Brasil | 1507300 | 15 | 33 | nan | nan | nan | Amazônia | 0.8 |
| c48597f8-403e-35a2-a69b-ed1ac6c7d20b | -5.79559 | -45.71359 | 2025-09-19 04:46:00 | NOAA-21 | GRAJAÚ | MARANHÃO | Brasil | 2104800 | 21 | 33 | nan | nan | nan | Cerrado | 1.5 |
| 26c16174-9edb-32b8-bc6e-12f451ab4a41 | -5.87841 | -45.74496 | 2025-09-19 04:46:00 | NOAA-21 | GRAJAÚ | MARANHÃO | Brasil | 2104800 | 21 | 33 | nan | nan | nan | Cerrado | 0.7 |
| 96e6d1d3-aefb-36a5-8e83-a5f326effe31 | -5.82779 | -50.21664 | 2025-09-19 04:46:00 | NOAA-21 | MARABÁ | PARÁ | Brasil | 1504208 | 15 | 33 | nan | nan | nan | Amazônia | 0.7 |
| b89a1c68-748a-3007-866d-4972316054e8 | -5.91841 | -43.23895 | 2025-09-19 04:46:00 | NOAA-21 | SÃO FRANCISCO DO MARANHÃO | MARANHÃO | Brasil | 2110906 | 21 | 33 | nan | nan | nan | Caatinga | 5.9 |
| 4f36bf6a-6f1a-3cf8-9f3d-f4c6a295eebd | -7.81129 | -46.16167 | 2025-09-19 04:46:00 | NOAA-21 | BALSAS | MARANHÃO | Brasil | 2101400 | 21 | 33 | nan | nan | nan | Cerrado | 3.1 |
| c9002cab-d58a-3ac0-9595-2cbeaf23ee0a | -12.72943 | -47.76918 | 2025-09-19 04:46:00 | NOAA-21 | PARANÃ | TOCANTINS | Brasil | 1716208 | 17 | 33 | nan | nan | nan | Cerrado | 2.2 |
| 620429f0-9aa7-3043-86c1-92e62c20beda | -10.48296 | -45.16295 | 2025-09-19 04:46:00 | NOAA-21 | CORRENTE | PIAUÍ | Brasil | 2202901 | 22 | 33 | nan | nan | nan | Cerrado | 2.3 |
| a5cf444b-b4d7-3918-b8b0-e3730d297658 | -5.88974 | -45.72462 | 2025-09-19 04:46:00 | NOAA-21 | GRAJAÚ | MARANHÃO | Brasil | 2104800 | 21 | 33 | nan | nan | nan | Cerrado | 1.1 |
| 3d7f9ab0-d8e8-3f80-a21d-9d6e014be48c | -8.91125 | -46.13318 | 2025-09-19 04:46:00 | NOAA-21 | ALTO PARNAÍBA | MARANHÃO | Brasil | 2100501 | 21 | 33 | nan | nan | nan | Cerrado | 0.9 |
| 8825eb5a-44cc-35ff-8af3-f3826022735b | -10.92367 | -45.65928 | 2025-09-19 04:46:00 | NOAA-21 | FORMOSA DO RIO PRETO | BAHIA | Brasil | 2911105 | 29 | 33 | nan | nan | nan | Cerrado | 1.0 |
| 2a1c8cc0-ce81-3e85-b03b-297d38aa715e | -8.89748 | -46.12878 | 2025-09-19 04:46:00 | NOAA-21 | ALTO PARNAÍBA | MARANHÃO | Brasil | 2100501 | 21 | 33 | nan | nan | nan | Cerrado | 2.4 |
| 25227c0f-63d6-3331-96c8-5168a61c3112 | -8.89802 | -46.12503 | 2025-09-19 04:46:00 | NOAA-21 | ALTO PARNAÍBA | MARANHÃO | Brasil | 2100501 | 21 | 33 | nan | nan | nan | Cerrado | 2.4 |
| 3a478ba6-0a01-3de6-8399-33e3aab3eee8 | -11.54649 | -49.04276 | 2025-09-19 04:46:00 | NOAA-21 | DUERÉ | TOCANTINS | Brasil | 1707306 | 17 | 33 | nan | nan | nan | Cerrado | 3.0 |
| 3ef27b93-61ae-31df-9ea9-c1ef2a87c707 | -8.91001 | -46.13039 | 2025-09-19 04:46:00 | NOAA-21 | ALTO PARNAÍBA | MARANHÃO | Brasil | 2100501 | 21 | 33 | nan | nan | nan | Cerrado | 0.9 |
| 8856ff07-07a0-305c-af13-9c467f370cd1 | -5.98853 | -45.73092 | 2025-09-19 04:46:00 | NOAA-21 | GRAJAÚ | MARANHÃO | Brasil | 2104800 | 21 | 33 | nan | nan | nan | Cerrado | 0.8 |
| 235d258e-a5bd-35a7-8bed-33ce9dbdd8c8 | -7.57623 | -45.48589 | 2025-09-19 04:46:00 | NOAA-21 | LORETO | MARANHÃO | Brasil | 2106102 | 21 | 33 | nan | nan | nan | Cerrado | 3.7 |
| 835aad58-d39f-385c-b7cf-2b3430141479 | -7.21917 | -44.37623 | 2025-09-19 04:46:00 | NOAA-21 | URUÇUÍ | PIAUÍ | Brasil | 2211209 | 22 | 33 | nan | nan | nan | Cerrado | 2.6 |
| 8d6d923e-6737-335f-8ab5-9f82e364838a | -8.38121 | -44.67967 | 2025-09-19 04:46:00 | NOAA-21 | PALMEIRA DO PIAUÍ | PIAUÍ | Brasil | 2207405 | 22 | 33 | nan | nan | nan | Cerrado | 3.5 |
| 4a1bd5cd-9811-3b69-aa49-decf94ff789d | -7.61492 | -44.46139 | 2025-09-19 04:46:00 | NOAA-21 | URUÇUÍ | PIAUÍ | Brasil | 2211209 | 22 | 33 | nan | nan | nan | Cerrado | 1.8 |
| d6082cfa-54ca-3842-b2ce-3819e948786b | -11.08728 | -41.06501 | 2025-09-19 04:46:00 | NOAA-21 | VÁRZEA NOVA | BAHIA | Brasil | 2933158 | 29 | 33 | nan | nan | nan | Caatinga | 9.1 |
| cab40f2d-6a16-337b-bd42-5cf28b9a52de | -7.84477 | -45.63221 | 2025-09-19 04:46:00 | NOAA-21 | TASSO FRAGOSO | MARANHÃO | Brasil | 2112001 | 21 | 33 | nan | nan | nan | Cerrado | 1.8 |
| 1e0ceb78-b4d1-3424-86a4-795799bf39fa | -6.83575 | -41.03857 | 2025-09-19 04:46:00 | NOAA-21 | MONSENHOR HIPÓLITO | PIAUÍ | Brasil | 2206506 | 22 | 33 | nan | nan | nan | Caatinga | 1.7 |
| c3b76dff-c0ec-37cb-99bc-ef77462dcf7a | -6.20989 | -44.05644 | 2025-09-19 04:46:00 | NOAA-21 | COLINAS | MARANHÃO | Brasil | 2103505 | 21 | 33 | nan | nan | nan | Cerrado | 0.9 |
| 04a74eca-a3c6-3590-b8c6-9ac0edededdc | -5.71041 | -49.10071 | 2025-09-19 04:46:00 | NOAA-21 | MARABÁ | PARÁ | Brasil | 1504208 | 15 | 33 | nan | nan | nan | Amazônia | 1.8 |
| 41eb32a0-f1af-356d-9860-bba0ddd69dbc | -11.21543 | -49.62978 | 2025-09-19 04:46:00 | NOAA-21 | DUERÉ | TOCANTINS | Brasil | 1707306 | 17 | 33 | nan | nan | nan | Cerrado | 7.4 |
| 6c277567-9715-3252-a580-859018c82fd5 | -9.14776 | -44.85789 | 2025-09-19 04:46:00 | NOAA-21 | BOM JESUS | PIAUÍ | Brasil | 2201903 | 22 | 33 | nan | nan | nan | Cerrado | 2.1 |
| 69ff61be-3066-3c16-ba84-089bfdf81e18 | -4.94138 | -49.92145 | 2025-09-19 04:46:00 | NOAA-21 | ITUPIRANGA | PARÁ | Brasil | 1503705 | 15 | 33 | nan | nan | nan | Amazônia | 1.6 |
| 38b8a82c-138a-372a-9ebe-3c1720f847e4 | -9.18458 | -45.30964 | 2025-09-19 04:46:00 | NOAA-21 | BAIXA GRANDE DO RIBEIRO | PIAUÍ | Brasil | 2201150 | 22 | 33 | nan | nan | nan | Cerrado | 1.6 |
| 0e40b9b1-5d9b-304e-b2d5-21cc116e2bba | -5.7591 | -43.39704 | 2025-09-19 04:46:00 | NOAA-21 | PARNARAMA | MARANHÃO | Brasil | 2107803 | 21 | 33 | nan | nan | nan | Cerrado | 5.7 |
| b05a3b63-b445-3639-85e9-8d7d2a6bb438 | -7.00997 | -44.6322 | 2025-09-19 04:46:00 | NOAA-21 | BENEDITO LEITE | MARANHÃO | Brasil | 2101806 | 21 | 33 | nan | nan | nan | Cerrado | 2.9 |
| c1810498-aec0-3039-90a3-fa7d4c11f832 | -12.11102 | -44.84584 | 2025-09-19 04:46:00 | NOAA-21 | ANGICAL | BAHIA | Brasil | 2901403 | 29 | 33 | nan | nan | nan | Cerrado | 2.8 |
| 48eb0404-4386-32e7-ac2f-40f8ca1fe6b5 | -5.98264 | -45.85706 | 2025-09-19 04:46:00 | NOAA-21 | GRAJAÚ | MARANHÃO | Brasil | 2104800 | 21 | 33 | nan | nan | nan | Cerrado | 1.1 |
| e7d78f03-ce1e-36cb-ad59-089843b9cb82 | -6.25832 | -43.91446 | 2025-09-19 04:46:00 | NOAA-21 | PASSAGEM FRANCA | MARANHÃO | Brasil | 2107902 | 21 | 33 | nan | nan | nan | Cerrado | 5.9 |
| 4e604299-5598-32fc-b6d1-aaf67d0a1104 | -8.6291 | -45.70782 | 2025-09-19 04:46:00 | NOAA-21 | SANTA FILOMENA | PIAUÍ | Brasil | 2209203 | 22 | 33 | nan | nan | nan | Cerrado | 1.5 |
| 625c04a3-0515-3be8-ac57-2eddfbb90391 | -6.19969 | -43.92569 | 2025-09-19 04:46:00 | NOAA-21 | PASSAGEM FRANCA | MARANHÃO | Brasil | 2107902 | 21 | 33 | nan | nan | nan | Cerrado | 1.3 |
| 71a9a93e-061d-3104-a882-5897821c988a | -7.57994 | -45.49038 | 2025-09-19 04:46:00 | NOAA-21 | LORETO | MARANHÃO | Brasil | 2106102 | 21 | 33 | nan | nan | nan | Cerrado | 4.0 |
| 75c27f58-a2b7-3f51-89da-a3e60c7b0722 | -8.1377 | -44.47431 | 2025-09-19 04:46:00 | NOAA-21 | URUÇUÍ | PIAUÍ | Brasil | 2211209 | 22 | 33 | nan | nan | nan | Cerrado | 7.1 |
| efe6bf4f-fd07-328c-a5f3-7bea79a60874 | -7.57364 | -44.48939 | 2025-09-19 04:46:00 | NOAA-21 | URUÇUÍ | PIAUÍ | Brasil | 2211209 | 22 | 33 | nan | nan | nan | Cerrado | 1.5 |
| 3a2de68f-6557-32e7-b2d4-8deecc4dcd4e | -7.5586 | -45.48731 | 2025-09-19 04:46:00 | NOAA-21 | LORETO | MARANHÃO | Brasil | 2106102 | 21 | 33 | nan | nan | nan | Cerrado | 1.2 |
| 2ae3b0c7-b24f-33de-a939-228c3ae741cc | -5.4586 | -46.68258 | 2025-09-19 04:46:00 | NOAA-21 | AMARANTE DO MARANHÃO | MARANHÃO | Brasil | 2100600 | 21 | 33 | nan | nan | nan | Cerrado | 3.4 |
| 9c3105e0-297e-34b9-abd3-313a503cca87 | -7.3208 | -44.05248 | 2025-09-19 04:46:00 | NOAA-21 | LANDRI SALES | PIAUÍ | Brasil | 2205607 | 22 | 33 | nan | nan | nan | Cerrado | 1.8 |
| 20c5d1a2-8aaa-3352-9f21-372fc2d29f60 | -10.37124 | -42.46421 | 2025-09-19 04:46:00 | NOAA-21 | PILÃO ARCADO | BAHIA | Brasil | 2924405 | 29 | 33 | nan | nan | nan | Caatinga | 10.5 |
| b142f49a-3d85-3877-8cce-9d9a76442d22 | -5.80836 | -45.71211 | 2025-09-19 04:46:00 | NOAA-21 | GRAJAÚ | MARANHÃO | Brasil | 2104800 | 21 | 33 | nan | nan | nan | Cerrado | 1.3 |
| 0313e9bc-da36-3992-9604-18c2a344475d | -5.77807 | -45.97184 | 2025-09-19 04:46:00 | NOAA-21 | GRAJAÚ | MARANHÃO | Brasil | 2104800 | 21 | 33 | nan | nan | nan | Cerrado | 3.4 |
| 5d462814-9975-3707-91e5-de859c458798 | -10.4875 | -45.16364 | 2025-09-19 04:46:00 | NOAA-21 | CORRENTE | PIAUÍ | Brasil | 2202901 | 22 | 33 | nan | nan | nan | Cerrado | 3.5 |
| a8e2d2f9-acbc-3a5d-9c85-d1c5da61db03 | -6.95792 | -42.44063 | 2025-09-19 04:46:00 | NOAA-21 | OEIRAS | PIAUÍ | Brasil | 2207009 | 22 | 33 | nan | nan | nan | Caatinga | 2.3 |
| ffd286e1-0452-34b2-b87e-b96989b6e1d9 | -11.44693 | -43.54431 | 2025-09-19 04:46:00 | NOAA-21 | BARRA | BAHIA | Brasil | 2902708 | 29 | 33 | nan | nan | nan | Cerrado | 0.8 |
| f91fe2a9-abcc-3ed8-91fc-3ee2f5003562 | -6.16943 | -46.387 | 2025-09-19 04:46:00 | NOAA-21 | GRAJAÚ | MARANHÃO | Brasil | 2104800 | 21 | 33 | nan | nan | nan | Cerrado | 1.0 |
| 17c33096-fa58-3dcb-984d-6bedcfd66eb4 | -8.0203 | -45.73564 | 2025-09-19 04:46:00 | NOAA-21 | TASSO FRAGOSO | MARANHÃO | Brasil | 2112001 | 21 | 33 | nan | nan | nan | Cerrado | 2.7 |
| c296068d-5046-30a0-a453-829ece6c7c9c | -7.63915 | -44.45548 | 2025-09-19 04:46:00 | NOAA-21 | URUÇUÍ | PIAUÍ | Brasil | 2211209 | 22 | 33 | nan | nan | nan | Cerrado | 2.5 |
| a6662a3a-f809-33a1-b805-15302465b807 | -9.5164 | -43.06521 | 2025-09-19 04:46:00 | NOAA-21 | CAMPO ALEGRE DE LOURDES | BAHIA | Brasil | 2905909 | 29 | 33 | nan | nan | nan | Caatinga | 4.7 |
| c9769b17-1a4a-3231-beca-ea2b219c453f | -6.5213 | -51.20035 | 2025-09-19 04:46:00 | NOAA-21 | SÃO FÉLIX DO XINGU | PARÁ | Brasil | 1507300 | 15 | 33 | nan | nan | nan | Amazônia | 0.5 |
| 74f36937-2f95-3727-8535-9dea5b20d28f | -10.35457 | -47.87257 | 2025-09-19 04:46:00 | NOAA-21 | MONTE DO CARMO | TOCANTINS | Brasil | 1713601 | 17 | 33 | nan | nan | nan | Cerrado | 4.7 |
| cbd2945b-32eb-32a4-8b88-47da3e0f38a3 | -6.95403 | -42.43762 | 2025-09-19 04:46:00 | NOAA-21 | OEIRAS | PIAUÍ | Brasil | 2207009 | 22 | 33 | nan | nan | nan | Caatinga | 1.8 |
| f94a23d5-4578-3d74-9dd0-8a4848853efe | -9.17955 | -45.3134 | 2025-09-19 04:46:00 | NOAA-21 | BAIXA GRANDE DO RIBEIRO | PIAUÍ | Brasil | 2201150 | 22 | 33 | nan | nan | nan | Cerrado | 4.7 |
| 9bd686ed-7135-3b1c-a977-366a918a8251 | -11.57684 | -50.49218 | 2025-09-19 04:46:00 | NOAA-21 | FORMOSO DO ARAGUAIA | TOCANTINS | Brasil | 1708205 | 17 | 33 | nan | nan | nan | Cerrado | 1.3 |
| 86f1c6dc-4c99-3037-af6a-05a87237dfc2 | -5.79295 | -45.35207 | 2025-09-19 04:46:00 | NOAA-21 | BARRA DO CORDA | MARANHÃO | Brasil | 2101608 | 21 | 33 | nan | nan | nan | Cerrado | 1.2 |
| 425a0f88-424d-3217-b113-96f92ab3201f | -10.32545 | -45.24825 | 2025-09-19 04:46:00 | NOAA-21 | CORRENTE | PIAUÍ | Brasil | 2202901 | 22 | 33 | nan | nan | nan | Cerrado | 1.2 |
| 3b3453d3-0692-3c1e-957e-5477e252792f | -7.65973 | -45.12776 | 2025-09-19 04:46:00 | NOAA-21 | RIBEIRO GONÇALVES | PIAUÍ | Brasil | 2208908 | 22 | 33 | nan | nan | nan | Cerrado | 1.4 |
| 55b77b6d-b6fd-339a-af92-9d5d409d4139 | -7.36292 | -44.58712 | 2025-09-19 04:46:00 | NOAA-21 | URUÇUÍ | PIAUÍ | Brasil | 2211209 | 22 | 33 | nan | nan | nan | Cerrado | 3.3 |
| 74555b6c-5b10-3b42-9420-37947e305897 | -8.05171 | -44.07638 | 2025-09-19 04:46:00 | NOAA-21 | MANOEL EMÍDIO | PIAUÍ | Brasil | 2205904 | 22 | 33 | nan | nan | nan | Cerrado | 1.8 |
| 95f00595-7e5f-3994-af55-ba90615ceb5e | -6.35129 | -45.58498 | 2025-09-19 04:46:00 | NOAA-21 | FERNANDO FALCÃO | MARANHÃO | Brasil | 2104081 | 21 | 33 | nan | nan | nan | Cerrado | 1.6 |
| 9b11a653-c411-3955-99d9-5e8ae2330cb8 | -11.1628 | -45.32416 | 2025-09-19 04:46:00 | NOAA-21 | FORMOSA DO RIO PRETO | BAHIA | Brasil | 2911105 | 29 | 33 | nan | nan | nan | Cerrado | 1.3 |
| 46302c58-006c-3515-b7e1-eb3fddbef277 | -7.71009 | -49.55891 | 2025-09-19 04:46:00 | NOAA-21 | FLORESTA DO ARAGUAIA | PARÁ | Brasil | 1503044 | 15 | 33 | nan | nan | nan | Amazônia | 0.5 |
| 2ad7ef26-fb89-3aaa-bb4a-c72f90579750 | -7.45493 | -46.37756 | 2025-09-19 04:46:00 | NOAA-21 | RIACHÃO | MARANHÃO | Brasil | 2109502 | 21 | 33 | nan | nan | nan | Cerrado | 1.3 |
| 073b4ec3-4924-3c53-8dc5-75d31af79242 | -5.45646 | -46.6968 | 2025-09-19 04:46:00 | NOAA-21 | AMARANTE DO MARANHÃO | MARANHÃO | Brasil | 2100600 | 21 | 33 | nan | nan | nan | Cerrado | 1.9 |


[Clique aqui para ver as próximas entradas](README24.md)
