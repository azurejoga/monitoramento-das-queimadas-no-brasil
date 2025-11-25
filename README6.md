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

## Dados Diários - Página 6

| ID | Latitude | Longitude | Data/Hora GMT | Satélite | Município | Estado | País | Município ID | Estado ID | País ID | Dias sem Chuva | Precipitação | Risco de Fogo | Bioma | FRP |
|----|----------|-----------|---------------|----------|-----------|--------|------|--------------|-----------|---------|----------------|--------------|----------------|-------|-----|
| 87ac6e61-9ad7-33e6-95d7-3e62c91b47e7 | -3.178 | -48.0277 | 2025-11-25 04:16:00 | NPP-375D | PARAGOMINAS | PARÁ | Brasil | 1505502 | 15 | 33 | nan | nan | nan | Amazônia | 1.2 |
| 54a777df-ed1e-329e-b4c6-c35e3fc51ec5 | -5.42502 | -38.797 | 2025-11-25 04:16:00 | NPP-375D | JAGUARETAMA | CEARÁ | Brasil | 2306702 | 23 | 33 | nan | nan | nan | Caatinga | 0.8 |
| 8595f16e-4982-3cdc-b62d-0dd939acb8db | -3.20923 | -46.83934 | 2025-11-25 04:16:00 | NPP-375D | PARAGOMINAS | PARÁ | Brasil | 1505502 | 15 | 33 | nan | nan | nan | Amazônia | 2.8 |
| c4d0eee8-36ca-3749-90cc-d269d16a2717 | -3.83422 | -43.99372 | 2025-11-25 04:16:00 | NPP-375D | VARGEM GRANDE | MARANHÃO | Brasil | 2112704 | 21 | 33 | nan | nan | nan | Cerrado | 1.1 |
| a3bbcf69-ff9a-3b18-bfc0-b67deb44290c | -5.11833 | -40.72812 | 2025-11-25 04:16:00 | NPP-375D | CRATEÚS | CEARÁ | Brasil | 2304103 | 23 | 33 | nan | nan | nan | Caatinga | 0.9 |
| 591db9f0-5d6f-3318-9148-724fdd65a1bf | -4.18206 | -43.8284 | 2025-11-25 04:16:00 | NPP-375D | TIMBIRAS | MARANHÃO | Brasil | 2112100 | 21 | 33 | nan | nan | nan | Cerrado | 2.5 |
| df1d4459-55d0-3b69-9c32-55ec0b1906bc | -4.66198 | -44.14963 | 2025-11-25 04:16:00 | NPP-375D | CODÓ | MARANHÃO | Brasil | 2103307 | 21 | 33 | nan | nan | nan | Cerrado | 1.4 |
| 7a5d6199-c92d-3041-b9de-92320e5a5737 | -1.96511 | -54.71289 | 2025-11-25 04:16:00 | NPP-375D | ALENQUER | PARÁ | Brasil | 1500404 | 15 | 33 | nan | nan | nan | Amazônia | 5.6 |
| 7c2391ca-2200-3986-ba88-6b5df3dba862 | -3.41638 | -45.45512 | 2025-11-25 04:16:00 | NPP-375D | MONÇÃO | MARANHÃO | Brasil | 2106904 | 21 | 33 | nan | nan | nan | Amazônia | 0.5 |
| b9ad5f17-43db-32e1-9649-5d289daf6248 | -3.81048 | -49.98311 | 2025-11-25 04:16:00 | NPP-375D | PACAJÁ | PARÁ | Brasil | 1505486 | 15 | 33 | nan | nan | nan | Amazônia | 0.9 |
| 6c1a72f4-eb97-3ab1-8dfe-39e334445962 | -3.88816 | -42.58506 | 2025-11-25 04:16:00 | NPP-375D | CAMPO LARGO DO PIAUÍ | PIAUÍ | Brasil | 2202174 | 22 | 33 | nan | nan | nan | Caatinga | 0.9 |
| 775565ab-34e7-3140-89fb-df2e356139a2 | -4.1787 | -43.82787 | 2025-11-25 04:16:00 | NPP-375D | TIMBIRAS | MARANHÃO | Brasil | 2112100 | 21 | 33 | nan | nan | nan | Cerrado | 2.5 |
| 121a3907-f9d9-32a7-a5cb-0f05f6e40e45 | -3.0289 | -51.03526 | 2025-11-25 04:16:00 | NPP-375D | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 2.2 |
| 1fafb2d5-d267-3ab9-8767-d002c7c91be5 | -2.93352 | -48.2336 | 2025-11-25 04:16:00 | NPP-375D | TOMÉ-AÇU | PARÁ | Brasil | 1508001 | 15 | 33 | nan | nan | nan | Amazônia | 3.8 |
| 52f6ce02-2077-385c-bbc2-03a8dc1859a7 | -2.88146 | -51.80311 | 2025-11-25 04:16:00 | NPP-375D | SENADOR JOSÉ PORFÍRIO | PARÁ | Brasil | 1507805 | 15 | 33 | nan | nan | nan | Amazônia | 1.2 |
| f9877421-763e-3f73-a59e-5f7210f28371 | -3.57024 | -43.81279 | 2025-11-25 04:16:00 | NPP-375D | VARGEM GRANDE | MARANHÃO | Brasil | 2112704 | 21 | 33 | nan | nan | nan | Cerrado | 1.0 |
| ea44df09-6624-376f-a545-71a2b85fe149 | -3.82256 | -48.87043 | 2025-11-25 04:16:00 | NPP-375D | GOIANÉSIA DO PARÁ | PARÁ | Brasil | 1503093 | 15 | 33 | nan | nan | nan | Amazônia | 5.2 |
| 82406b8e-c1c3-3241-a16e-4ac0fc1eeb51 | -3.21162 | -46.82473 | 2025-11-25 04:16:00 | NPP-375D | PARAGOMINAS | PARÁ | Brasil | 1505502 | 15 | 33 | nan | nan | nan | Amazônia | 6.5 |
| 8a76b87a-8ecb-3611-9286-3b54ddd7f1d6 | -3.77361 | -44.04705 | 2025-11-25 04:16:00 | NPP-375D | PIRAPEMAS | MARANHÃO | Brasil | 2108801 | 21 | 33 | nan | nan | nan | Cerrado | 1.4 |
| dad9c803-45f1-3df1-9ec7-834428f572f4 | -3.57865 | -45.23472 | 2025-11-25 04:16:00 | NPP-375D | MONÇÃO | MARANHÃO | Brasil | 2106904 | 21 | 33 | nan | nan | nan | Amazônia | 1.2 |
| 3577f0b1-4ead-368b-b94e-7a2b5017b76e | -1.33567 | -53.15743 | 2025-11-25 04:16:00 | NPP-375D | ALMEIRIM | PARÁ | Brasil | 1500503 | 15 | 33 | nan | nan | nan | Amazônia | 1.0 |
| 774019be-827c-399f-a523-9bfb80fecaac | -3.17378 | -48.02705 | 2025-11-25 04:16:00 | NPP-375D | PARAGOMINAS | PARÁ | Brasil | 1505502 | 15 | 33 | nan | nan | nan | Amazônia | 1.2 |
| 14ba089e-bd01-31b2-9e3a-70e156d88fa0 | -4.60033 | -44.88084 | 2025-11-25 04:16:00 | NPP-375D | IGARAPÉ GRANDE | MARANHÃO | Brasil | 2105203 | 21 | 33 | nan | nan | nan | Cerrado | 3.6 |
| e978dfd2-e27a-3fcb-96e1-9592166bf5bd | -4.392 | -40.68026 | 2025-11-25 04:16:00 | NPP-375D | IPU | CEARÁ | Brasil | 2305803 | 23 | 33 | nan | nan | nan | Caatinga | 1.0 |
| 2a055fa5-89b3-3688-832d-9ac1b108e812 | -3.41705 | -45.45104 | 2025-11-25 04:16:00 | NPP-375D | MONÇÃO | MARANHÃO | Brasil | 2106904 | 21 | 33 | nan | nan | nan | Amazônia | 0.5 |
| 9ea23bdc-d5d4-3c74-a7c1-424e36c1cdba | -3.77759 | -44.04395 | 2025-11-25 04:16:00 | NPP-375D | PIRAPEMAS | MARANHÃO | Brasil | 2108801 | 21 | 33 | nan | nan | nan | Cerrado | 3.9 |
| 5d5de9c2-9418-3bd6-90c6-75c5f7e9b832 | -4.53708 | -45.79117 | 2025-11-25 04:16:00 | NPP-375D | SANTA LUZIA | MARANHÃO | Brasil | 2110005 | 21 | 33 | nan | nan | nan | Amazônia | 0.8 |
| 79608dbf-ae7d-3a73-84bf-788a6d2dc88c | -2.93287 | -48.23766 | 2025-11-25 04:16:00 | NPP-375D | TOMÉ-AÇU | PARÁ | Brasil | 1508001 | 15 | 33 | nan | nan | nan | Amazônia | 2.5 |
| 44702648-22c5-3fe4-8e64-81131a7f97af | -3.50308 | -45.72335 | 2025-11-25 04:16:00 | NPP-375D | BOM JARDIM | MARANHÃO | Brasil | 2102002 | 21 | 33 | nan | nan | nan | Amazônia | 1.2 |
| 1c344ce1-637b-3c53-9c84-949ea11c6bda | -3.27324 | -46.0165 | 2025-11-25 04:16:00 | NPP-375D | ZÉ DOCA | MARANHÃO | Brasil | 2114007 | 21 | 33 | nan | nan | nan | Amazônia | 2.5 |
| d2b8ca71-2233-3019-b295-9eaa495ec41b | -2.99207 | -51.06438 | 2025-11-25 04:16:00 | NPP-375D | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 0.8 |
| 27f15cc5-7bbb-39dc-9f3f-04a8c972f413 | -4.19341 | -41.63691 | 2025-11-25 04:16:00 | NPP-375D | BRASILEIRA | PIAUÍ | Brasil | 2201960 | 22 | 33 | nan | nan | nan | Caatinga | 2.1 |
| 0298992c-9b94-3515-a096-b8bc1f0aabc9 | -3.59438 | -40.98414 | 2025-11-25 04:16:00 | NPP-375D | VIÇOSA DO CEARÁ | CEARÁ | Brasil | 2314102 | 23 | 33 | nan | nan | nan | Caatinga | 1.4 |
| 0aa28c5a-fd8f-3fae-a42d-36eec2e51e1a | -1.34181 | -53.15833 | 2025-11-25 04:16:00 | NPP-375D | ALMEIRIM | PARÁ | Brasil | 1500503 | 15 | 33 | nan | nan | nan | Amazônia | 2.4 |
| f5685b89-567e-322a-83a0-747bb7539934 | -4.82246 | -43.82383 | 2025-11-25 04:16:00 | NPP-375D | SÃO JOÃO DO SOTER | MARANHÃO | Brasil | 2111078 | 21 | 33 | nan | nan | nan | Cerrado | 3.2 |
| fb2e0ce1-0f59-3d10-b4ba-5e81b3892a3d | -1.96996 | -54.70824 | 2025-11-25 04:16:00 | NPP-375D | ALENQUER | PARÁ | Brasil | 1500404 | 15 | 33 | nan | nan | nan | Amazônia | 2.2 |
| f1aee61d-711b-34b3-adf4-db932604a853 | -3.20693 | -46.82897 | 2025-11-25 04:16:00 | NPP-375D | PARAGOMINAS | PARÁ | Brasil | 1505502 | 15 | 33 | nan | nan | nan | Amazônia | 2.2 |
| d53d8c70-9469-31a8-b1c4-6e313677159b | -3.02421 | -51.03126 | 2025-11-25 04:16:00 | NPP-375D | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 0.9 |
| 128dc24b-25c5-3b9c-b6b7-2c892ba86565 | -3.03024 | -51.02911 | 2025-11-25 04:16:00 | NPP-375D | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 2.3 |
| 58983b40-d902-3055-9392-56eaeeb1ea52 | -3.77022 | -44.0465 | 2025-11-25 04:16:00 | NPP-375D | PIRAPEMAS | MARANHÃO | Brasil | 2108801 | 21 | 33 | nan | nan | nan | Cerrado | 1.4 |
| c8a92dde-0b1c-35b3-94aa-04c8682b4849 | -4.55035 | -43.29614 | 2025-11-25 04:16:00 | NPP-375D | ALDEIAS ALTAS | MARANHÃO | Brasil | 2100303 | 21 | 33 | nan | nan | nan | Cerrado | 9.0 |
| 6cef318b-a6d0-3453-bce7-55d2cd1d3a77 | -2.8754 | -51.80574 | 2025-11-25 04:16:00 | NPP-375D | SENADOR JOSÉ PORFÍRIO | PARÁ | Brasil | 1507805 | 15 | 33 | nan | nan | nan | Amazônia | 1.5 |
| dc5abcd1-a5f2-32d8-a946-c48652fd6c0d | -2.93846 | -48.23024 | 2025-11-25 04:16:00 | NPP-375D | TOMÉ-AÇU | PARÁ | Brasil | 1508001 | 15 | 33 | nan | nan | nan | Amazônia | 3.8 |
| 99927d26-ee87-373d-9afa-4772fdb86227 | -2.96031 | -41.55701 | 2025-11-25 04:16:00 | NPP-375D | LUÍS CORREIA | PIAUÍ | Brasil | 2205706 | 22 | 33 | nan | nan | nan | Cerrado | 1.0 |
| cc19dfaa-9d0f-38b4-b82f-c72fc3c629e7 | -3.87273 | -50.16605 | 2025-11-25 04:16:00 | NPP-375D | PACAJÁ | PARÁ | Brasil | 1505486 | 15 | 33 | nan | nan | nan | Amazônia | 1.1 |
| a92a1735-1a3f-3d7c-8871-9ea15c10f681 | -1.6751 | -52.094 | 2025-11-25 04:16:00 | NPP-375D | PORTO DE MOZ | PARÁ | Brasil | 1505908 | 15 | 33 | nan | nan | nan | Amazônia | 0.8 |
| 6df390e2-ddea-3a1d-81ca-3e110647f2f1 | -2.8803 | -51.81021 | 2025-11-25 04:16:00 | NPP-375D | SENADOR JOSÉ PORFÍRIO | PARÁ | Brasil | 1507805 | 15 | 33 | nan | nan | nan | Amazônia | 2.3 |
| dc989833-5525-3716-b329-d9bf11cf39a0 | -4.74654 | -44.45316 | 2025-11-25 04:16:00 | NPP-375D | SANTO ANTÔNIO DOS LOPES | MARANHÃO | Brasil | 2110302 | 21 | 33 | nan | nan | nan | Cerrado | 0.9 |
| a8ed1397-827b-392f-8ad7-81b9f4593835 | -1.29329 | -53.14828 | 2025-11-25 04:16:00 | NPP-375D | ALMEIRIM | PARÁ | Brasil | 1500503 | 15 | 33 | nan | nan | nan | Amazônia | 0.7 |
| 480314ad-f7eb-38db-949e-6acbee4e7ae9 | -2.8431 | -46.77641 | 2025-11-25 04:16:00 | NPP-375D | PARAGOMINAS | PARÁ | Brasil | 1505502 | 15 | 33 | nan | nan | nan | Amazônia | 1.1 |
| 98f42999-64fb-3517-9f9e-283719a6a221 | -3.82542 | -40.69083 | 2025-11-25 04:16:00 | NPP-375D | SOBRAL | CEARÁ | Brasil | 2312908 | 23 | 33 | nan | nan | nan | Caatinga | 1.5 |
| 2e00fcc9-0c45-3472-afb5-7858be171bc8 | -3.88793 | -47.23948 | 2025-11-25 04:16:00 | NPP-375D | ULIANÓPOLIS | PARÁ | Brasil | 1508126 | 15 | 33 | nan | nan | nan | Amazônia | 1.3 |
| 719b3d9c-8355-3009-bc4c-cb7572471679 | -5.31283 | -40.86831 | 2025-11-25 04:16:00 | NPP-375D | CRATEÚS | CEARÁ | Brasil | 2304103 | 23 | 33 | nan | nan | nan | Caatinga | 0.9 |
| 2581d420-a2da-399c-8602-4ad52fb23d04 | -2.93781 | -48.2343 | 2025-11-25 04:16:00 | NPP-375D | TOMÉ-AÇU | PARÁ | Brasil | 1508001 | 15 | 33 | nan | nan | nan | Amazônia | 3.8 |
| c33a399e-766b-3c32-8f4f-a09dc8adf5c7 | -4.32925 | -45.76368 | 2025-11-25 04:16:00 | NPP-375D | BREJO DE AREIA | MARANHÃO | Brasil | 2102150 | 21 | 33 | nan | nan | nan | Amazônia | 1.6 |
| 611ff1fd-4e2f-300a-9cf0-f044a7f0c13e | -5.31569 | -40.87258 | 2025-11-25 04:16:00 | NPP-375D | CRATEÚS | CEARÁ | Brasil | 2304103 | 23 | 33 | nan | nan | nan | Caatinga | 2.5 |
| 6bd16eb1-05e2-3d12-b4db-8edf9ad62eb9 | -4.16719 | -41.62921 | 2025-11-25 04:16:00 | NPP-375D | BRASILEIRA | PIAUÍ | Brasil | 2201960 | 22 | 33 | nan | nan | nan | Caatinga | 1.9 |
| 2169a14f-2b42-3708-9656-25877edefc36 | -4.06668 | -44.59815 | 2025-11-25 04:16:00 | NPP-375D | SÃO MATEUS DO MARANHÃO | MARANHÃO | Brasil | 2111508 | 21 | 33 | nan | nan | nan | Cerrado | 0.9 |
| b7c064ec-5744-34f1-a5dd-a97ae128ac25 | -2.84231 | -46.78133 | 2025-11-25 04:16:00 | NPP-375D | PARAGOMINAS | PARÁ | Brasil | 1505502 | 15 | 33 | nan | nan | nan | Amazônia | 1.1 |
| 5e84dcb3-7965-3d5c-99cc-3e1aff364d30 | -1.67573 | -52.09005 | 2025-11-25 04:16:00 | NPP-375D | PORTO DE MOZ | PARÁ | Brasil | 1505908 | 15 | 33 | nan | nan | nan | Amazônia | 0.8 |
| edc304b9-4d5b-3da2-bb34-2046b3f9c166 | -3.10429 | -44.49956 | 2025-11-25 04:16:00 | NPP-375D | SANTA RITA | MARANHÃO | Brasil | 2110203 | 21 | 33 | nan | nan | nan | Amazônia | 0.5 |
| d44c905e-a474-3d1b-9754-6879a52f3bad | -4.13745 | -42.91109 | 2025-11-25 04:16:00 | NPP-375D | DUQUE BACELAR | MARANHÃO | Brasil | 2103901 | 21 | 33 | nan | nan | nan | Cerrado | 4.7 |
| b375750f-f151-33a8-9b97-b2da60469250 | -4.17053 | -41.62973 | 2025-11-25 04:16:00 | NPP-375D | BRASILEIRA | PIAUÍ | Brasil | 2201960 | 22 | 33 | nan | nan | nan | Caatinga | 1.9 |
| 48810481-1cdc-3490-a1ae-8c803e35908f | -3.73825 | -40.03091 | 2025-11-25 04:16:00 | NPP-375D | SOBRAL | CEARÁ | Brasil | 2312908 | 23 | 33 | nan | nan | nan | Caatinga | 1.0 |
| f33d5efc-0056-3431-97e0-154b41d9c4d4 | -4.95155 | -42.71014 | 2025-11-25 04:16:00 | NPP-375D | TERESINA | PIAUÍ | Brasil | 2211001 | 22 | 33 | nan | nan | nan | Cerrado | 4.4 |
| 8ac93391-06b3-35fe-a777-8c5e445ae2ca | -3.82464 | -43.9885 | 2025-11-25 04:16:00 | NPP-375D | VARGEM GRANDE | MARANHÃO | Brasil | 2112704 | 21 | 33 | nan | nan | nan | Cerrado | 1.2 |
| 86213cc6-80f5-3045-ba19-5e965fa3bf27 | -3.77701 | -44.04757 | 2025-11-25 04:16:00 | NPP-375D | PIRAPEMAS | MARANHÃO | Brasil | 2108801 | 21 | 33 | nan | nan | nan | Cerrado | 5.1 |
| 513218f0-e53a-3905-b988-5b2367d52bec | -4.82189 | -43.82737 | 2025-11-25 04:16:00 | NPP-375D | SÃO JOÃO DO SOTER | MARANHÃO | Brasil | 2111078 | 21 | 33 | nan | nan | nan | Cerrado | 3.2 |
| bfc43ca4-0a1d-37ad-bbd2-a1f4f7b13d7e | -1.4876 | -47.8088 | 2025-11-25 04:16:00 | NPP-375D | SÃO MIGUEL DO GUAMÁ | PARÁ | Brasil | 1507607 | 15 | 33 | nan | nan | nan | Amazônia | 0.9 |
| 6aa81fbb-539f-31df-b43b-ef52ce5e96f9 | -3.88876 | -47.23445 | 2025-11-25 04:16:00 | NPP-375D | ULIANÓPOLIS | PARÁ | Brasil | 1508126 | 15 | 33 | nan | nan | nan | Amazônia | 1.3 |
| 4b255e44-ee26-307d-b55a-90b61863b6f6 | -4.83535 | -37.76721 | 2025-11-25 04:16:00 | NPP-375D | JAGUARUANA | CEARÁ | Brasil | 2307007 | 23 | 33 | nan | nan | nan | Caatinga | 0.6 |
| aa8f8bfa-f57a-3af7-b8b2-3ea2b9230d01 | -4.81406 | -43.83338 | 2025-11-25 04:16:00 | NPP-375D | SÃO JOÃO DO SOTER | MARANHÃO | Brasil | 2111078 | 21 | 33 | nan | nan | nan | Cerrado | 4.3 |
| 54bbd941-d3be-3da9-bc7e-33002ea5090f | -4.02438 | -47.77031 | 2025-11-25 04:16:00 | NPP-375D | ULIANÓPOLIS | PARÁ | Brasil | 1508126 | 15 | 33 | nan | nan | nan | Amazônia | 0.8 |
| e0b5bfb1-8403-37cc-bed1-1ea635043907 | -3.02918 | -51.03534 | 2025-11-25 04:16:00 | NPP-375D | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 2.1 |
| 89f7388a-8f00-33fe-8267-974ad5dc6d00 | -3.02321 | -51.03745 | 2025-11-25 04:16:00 | NPP-375D | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 1.8 |
| 58c44d9c-11d0-3918-909d-3891dde58825 | -3.02399 | -51.03445 | 2025-11-25 04:16:00 | NPP-375D | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 1.0 |
| 76dc637c-6885-352a-9b14-ec2e1009ab4d | -2.99259 | -51.06127 | 2025-11-25 04:16:00 | NPP-375D | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 0.4 |
| 8e7c1dcb-ac3e-3010-a979-98e0463b4f6b | -4.04544 | -42.51055 | 2025-11-25 04:16:00 | NPP-375D | BARRAS | PIAUÍ | Brasil | 2201200 | 22 | 33 | nan | nan | nan | Caatinga | 0.9 |
| f86c2e2b-6f33-3f53-8084-7183e14380c4 | -4.538 | -45.78978 | 2025-11-25 04:16:00 | NPP-375D | SANTA LUZIA | MARANHÃO | Brasil | 2110005 | 21 | 33 | nan | nan | nan | Amazônia | 0.6 |
| c6e4e756-2757-30e7-b860-30b510e369a2 | -1.96239 | -54.71252 | 2025-11-25 04:16:00 | NPP-375D | ALENQUER | PARÁ | Brasil | 1500404 | 15 | 33 | nan | nan | nan | Amazônia | 2.2 |
| 591fa455-b8cd-3cea-b478-17eb6a929711 | -1.64033 | -52.05599 | 2025-11-25 04:16:00 | NPP-375D | PORTO DE MOZ | PARÁ | Brasil | 1505908 | 15 | 33 | nan | nan | nan | Amazônia | 0.9 |
| 9193247a-f7b9-37de-966c-880c739ed3c1 | -4.58252 | -40.82469 | 2025-11-25 04:16:00 | NPP-375D | IPUEIRAS | CEARÁ | Brasil | 2305902 | 23 | 33 | nan | nan | nan | Caatinga | 0.5 |
| e2715507-a429-315b-a22c-101ddc88e2c6 | -4.67633 | -45.01319 | 2025-11-25 04:16:00 | NPP-375D | LAGO DOS RODRIGUES | MARANHÃO | Brasil | 2105948 | 21 | 33 | nan | nan | nan | Cerrado | 1.4 |
| 4c2292bb-d161-39c5-9696-9ba7b49cd879 | -3.02991 | -51.02901 | 2025-11-25 04:16:00 | NPP-375D | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 2.3 |
| 9cfa1b7b-b845-35cb-8b20-bfcb5ecd20c4 | -4.2001 | -41.63794 | 2025-11-25 04:16:00 | NPP-375D | BRASILEIRA | PIAUÍ | Brasil | 2201960 | 22 | 33 | nan | nan | nan | Caatinga | 2.1 |
| 96c31a60-c9f2-3225-a49c-baf3603ec923 | -3.76964 | -44.05013 | 2025-11-25 04:16:00 | NPP-375D | PIRAPEMAS | MARANHÃO | Brasil | 2108801 | 21 | 33 | nan | nan | nan | Cerrado | 1.4 |
| 9457a535-3350-3bfb-b2f3-507c346cbcb2 | -5.00419 | -41.96794 | 2025-11-25 04:16:00 | NPP-375D | JATOBÁ DO PIAUÍ | PIAUÍ | Brasil | 2205276 | 22 | 33 | nan | nan | nan | Caatinga | 0.9 |
| ed345a9c-2afd-3c82-9453-c1e2e19246bc | -1.49186 | -47.80948 | 2025-11-25 04:16:00 | NPP-375D | SÃO MIGUEL DO GUAMÁ | PARÁ | Brasil | 1507607 | 15 | 33 | nan | nan | nan | Amazônia | 2.0 |
| b67df0c6-55bc-3a2e-806e-cf8f1cfcfa13 | -4.06727 | -44.5944 | 2025-11-25 04:16:00 | NPP-375D | SÃO MATEUS DO MARANHÃO | MARANHÃO | Brasil | 2111508 | 21 | 33 | nan | nan | nan | Cerrado | 0.9 |
| f353a86b-4442-37ff-ad00-cbcf1f23482e | -3.27819 | -42.18179 | 2025-11-25 04:16:00 | NPP-375D | MAGALHÃES DE ALMEIDA | MARANHÃO | Brasil | 2106300 | 21 | 33 | nan | nan | nan | Cerrado | 2.0 |
| 11cc651d-533c-3e83-a541-47cb9ca93feb | -4.32856 | -45.76784 | 2025-11-25 04:16:00 | NPP-375D | BREJO DE AREIA | MARANHÃO | Brasil | 2102150 | 21 | 33 | nan | nan | nan | Amazônia | 1.6 |
| 4c2dae00-c67c-3145-8279-12767bbf33fa | -4.33647 | -44.32902 | 2025-11-25 04:16:00 | NPP-375D | PERITORÓ | MARANHÃO | Brasil | 2108454 | 21 | 33 | nan | nan | nan | Cerrado | 1.9 |
| f2d57b58-0ec3-37f5-8645-d4ebbaca707b | -4.17385 | -41.60859 | 2025-11-25 04:16:00 | NPP-375D | BRASILEIRA | PIAUÍ | Brasil | 2201960 | 22 | 33 | nan | nan | nan | Caatinga | 1.3 |
| 06352308-e0b0-3362-8b92-e8f1117cffa4 | -4.9421 | -41.15983 | 2025-11-25 04:16:00 | NPP-375D | PORANGA | CEARÁ | Brasil | 2311009 | 23 | 33 | nan | nan | nan | Caatinga | 1.1 |
| 7e54249e-2c58-3205-9f6d-aae60a616111 | -4.72876 | -44.73446 | 2025-11-25 04:16:00 | NPP-375D | POÇÃO DE PEDRAS | MARANHÃO | Brasil | 2108900 | 21 | 33 | nan | nan | nan | Cerrado | 1.3 |
| 245635f7-1a1e-39de-b785-d2bd9fca624a | -4.34135 | -44.3412 | 2025-11-25 04:16:00 | NPP-375D | PERITORÓ | MARANHÃO | Brasil | 2108454 | 21 | 33 | nan | nan | nan | Cerrado | 1.4 |
| 22b84921-d2c5-3f41-b41e-99008e812201 | -3.8057 | -49.9824 | 2025-11-25 04:16:00 | NPP-375D | PACAJÁ | PARÁ | Brasil | 1505486 | 15 | 33 | nan | nan | nan | Amazônia | 0.9 |
| 1c8a21a0-dacd-3024-a20a-8d51ae9d9db9 | -2.87598 | -51.80219 | 2025-11-25 04:16:00 | NPP-375D | SENADOR JOSÉ PORFÍRIO | PARÁ | Brasil | 1507805 | 15 | 33 | nan | nan | nan | Amazônia | 1.8 |
| c93d25a5-a1b9-3cf5-a9b1-ee587cedbc59 | -4.33248 | -44.33213 | 2025-11-25 04:16:00 | NPP-375D | PERITORÓ | MARANHÃO | Brasil | 2108454 | 21 | 33 | nan | nan | nan | Cerrado | 1.4 |
| f2a7df74-07d0-3897-a6bd-b2807c7c3331 | -4.16774 | -41.62569 | 2025-11-25 04:16:00 | NPP-375D | BRASILEIRA | PIAUÍ | Brasil | 2201960 | 22 | 33 | nan | nan | nan | Caatinga | 1.9 |


[Clique aqui para ver as próximas entradas](README7.md)
