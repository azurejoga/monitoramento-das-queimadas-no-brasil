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

## Dados Diários - Página 14

| ID | Latitude | Longitude | Data/Hora GMT | Satélite | Município | Estado | País | Município ID | Estado ID | País ID | Dias sem Chuva | Precipitação | Risco de Fogo | Bioma | FRP |
|----|----------|-----------|---------------|----------|-----------|--------|------|--------------|-----------|---------|----------------|--------------|----------------|-------|-----|
| fe283049-c831-3be9-8495-d37c950311c0 | -2.5716 | -51.853901 | 2024-10-14 00:39:34 | METOP-C | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| 51abd7e0-2c52-3a5b-856b-abd40fd8e3e6 | -2.9513 | -54.634499 | 2024-10-14 00:39:38 | METOP-C | MOJUÍ DOS CAMPOS | PARÁ | Brasil | 1504752 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| b31dffad-369f-3b8f-b6c1-7290c9818536 | -2.955 | -54.651199 | 2024-10-14 00:39:38 | METOP-C | MOJUÍ DOS CAMPOS | PARÁ | Brasil | 1504752 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| 739558e9-e366-3509-9a7e-ef5f2e771c51 | -1.9261 | -52.085701 | 2024-10-14 00:39:45 | METOP-C | PORTO DE MOZ | PARÁ | Brasil | 1505908 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| 0c54800d-6396-3057-a83c-5879dd532770 | -1.9286 | -52.0965 | 2024-10-14 00:39:45 | METOP-C | PORTO DE MOZ | PARÁ | Brasil | 1505908 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| 6d77b729-38e3-3bb8-a0a3-ac17e35497b2 | -2.3172 | -54.582901 | 2024-10-14 00:39:48 | METOP-C | SANTARÉM | PARÁ | Brasil | 1506807 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| 4571aa6d-84e6-3cb9-8d09-3ddaf9f2b04f | -1.6433 | -55.078999 | 2024-10-14 00:40:01 | METOP-C | ALENQUER | PARÁ | Brasil | 1500404 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| 830ebb55-21fd-3f07-9a3d-8d5328704bdf | -1.6335 | -55.0812 | 2024-10-14 00:40:01 | METOP-C | ALENQUER | PARÁ | Brasil | 1500404 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| 1f6e1023-3c5e-3906-9e60-c442d6fdc05a | -2.4344 | -46.9195 | 2024-10-14 00:45:20 | GOES-16 | PARAGOMINAS | PARÁ | Brasil | 1505502 | 15 | 33 | nan | nan | nan | Amazônia | 69.1 |
| e100ff48-d270-34e1-b2c0-3064c65d4393 | -2.4529 | -46.919 | 2024-10-14 00:45:20 | GOES-16 | PARAGOMINAS | PARÁ | Brasil | 1505502 | 15 | 33 | nan | nan | nan | Amazônia | 82.8 |
| 6ded7888-58df-3598-a171-3cea10b91b8f | -2.6117 | -49.1198 | 2024-10-14 00:45:21 | GOES-16 | MOJU | PARÁ | Brasil | 1504703 | 15 | 33 | nan | nan | nan | Amazônia | 56.4 |
| 6e3a825c-c8a5-3ab8-8ba7-f6d5a50ba32a | -2.6118 | -49.0985 | 2024-10-14 00:45:21 | GOES-16 | MOJU | PARÁ | Brasil | 1504703 | 15 | 33 | nan | nan | nan | Amazônia | 53.5 |
| 48a95805-64f6-3c74-9688-ca71997aeb19 | -2.6119 | -49.0772 | 2024-10-14 00:45:21 | GOES-16 | MOJU | PARÁ | Brasil | 1504703 | 15 | 33 | nan | nan | nan | Amazônia | 38.4 |
| 3279420c-c6c1-317f-bc70-b024d0089bcc | -3.2889 | -42.8561 | 2024-10-14 00:45:25 | GOES-16 | SANTA QUITÉRIA DO MARANHÃO | MARANHÃO | Brasil | 2110104 | 21 | 33 | nan | nan | nan | Cerrado | 64.6 |
| e14077bb-9e0b-364f-82f9-fad4108ed553 | -3.289 | -42.8327 | 2024-10-14 00:45:25 | GOES-16 | SANTA QUITÉRIA DO MARANHÃO | MARANHÃO | Brasil | 2110104 | 21 | 33 | nan | nan | nan | Cerrado | 124.0 |
| e504f8f3-35b4-3285-89e5-11adc8293ebe | -3.3076 | -42.8553 | 2024-10-14 00:45:25 | GOES-16 | SANTA QUITÉRIA DO MARANHÃO | MARANHÃO | Brasil | 2110104 | 21 | 33 | nan | nan | nan | Cerrado | 173.4 |
| 62139a83-9286-3253-8a0a-cd1f7afb1b29 | -3.3077 | -42.8318 | 2024-10-14 00:45:25 | GOES-16 | SANTA QUITÉRIA DO MARANHÃO | MARANHÃO | Brasil | 2110104 | 21 | 33 | nan | nan | nan | Cerrado | 333.1 |
| ee4c7542-01f8-3492-b197-2b66aca78a1f | -3.1982 | -50.3077 | 2024-10-14 00:45:25 | GOES-16 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 28.8 |
| 20a62ccc-6f59-384a-91f1-4a0a922e8355 | -3.3274 | -50.3245 | 2024-10-14 00:45:25 | GOES-16 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 33.3 |
| fd76396c-fec7-308b-9b25-2808f642d805 | -3.8723 | -52.2769 | 2024-10-14 00:45:28 | GOES-16 | SENADOR JOSÉ PORFÍRIO | PARÁ | Brasil | 1507805 | 15 | 33 | nan | nan | nan | Amazônia | 51.2 |
| 9ceab853-0497-3f03-9d70-e5b604a79726 | -3.9103 | -48.3466 | 2024-10-14 00:45:29 | GOES-16 | DOM ELISEU | PARÁ | Brasil | 1502939 | 15 | 33 | nan | nan | nan | Amazônia | 61.2 |
| 1ba4c11f-6f88-38ce-949f-f1733c58a177 | -4.1145 | -48.2947 | 2024-10-14 00:45:30 | GOES-16 | DOM ELISEU | PARÁ | Brasil | 1502939 | 15 | 33 | nan | nan | nan | Amazônia | 74.0 |
| 3bf85fe4-f9cd-319e-92f7-02b24e2ad0fe | -4.1146 | -48.2731 | 2024-10-14 00:45:30 | GOES-16 | DOM ELISEU | PARÁ | Brasil | 1502939 | 15 | 33 | nan | nan | nan | Amazônia | 85.8 |
| 8ce9554d-bb9c-3c6c-a496-27cd0b0932bd | -4.3428 | -50.5172 | 2024-10-14 00:45:31 | GOES-16 | NOVO REPARTIMENTO | PARÁ | Brasil | 1505064 | 15 | 33 | nan | nan | nan | Amazônia | 80.1 |
| 80bb6e8f-b665-3fc1-8233-89aa0c3617e3 | -4.3613 | -50.5164 | 2024-10-14 00:45:31 | GOES-16 | NOVO REPARTIMENTO | PARÁ | Brasil | 1505064 | 15 | 33 | nan | nan | nan | Amazônia | 71.6 |
| 56f0609c-2737-3994-bd37-8409e5a06c5d | -4.6197 | -44.8626 | 2024-10-14 00:45:32 | GOES-16 | IGARAPÉ GRANDE | MARANHÃO | Brasil | 2105203 | 21 | 33 | nan | nan | nan | Cerrado | 107.4 |
| 2f41bfc6-3aac-358f-ab17-ef1ec9e365c0 | -4.6384 | -44.8615 | 2024-10-14 00:45:33 | GOES-16 | IGARAPÉ GRANDE | MARANHÃO | Brasil | 2105203 | 21 | 33 | nan | nan | nan | Cerrado | 124.2 |
| e48e8b08-feb4-34e4-b47f-bd0b1615c50b | -4.7224 | -46.1608 | 2024-10-14 00:45:33 | GOES-16 | SANTA LUZIA | MARANHÃO | Brasil | 2110005 | 21 | 33 | nan | nan | nan | Amazônia | 78.5 |
| cecb5f5d-e802-3216-9f26-f5abf5ebdc78 | -4.7226 | -46.1385 | 2024-10-14 00:45:33 | GOES-16 | SANTA LUZIA | MARANHÃO | Brasil | 2110005 | 21 | 33 | nan | nan | nan | Amazônia | 64.9 |
| d1b9bad9-ae18-352f-9993-b158b962fdb5 | -5.0627 | -48.0528 | 2024-10-14 00:45:35 | GOES-16 | VILA NOVA DOS MARTÍRIOS | MARANHÃO | Brasil | 2112852 | 21 | 33 | nan | nan | nan | Amazônia | 27.8 |
| 68e7c158-6e29-3941-b350-e2f9e7aef9e8 | -6.3749 | -59.9936 | 2024-10-14 00:45:43 | GOES-16 | NOVO ARIPUANÃ | AMAZONAS | Brasil | 1303304 | 13 | 33 | nan | nan | nan | Amazônia | 49.4 |
| acd5fdfc-3ae8-39cf-9a89-4256a223c589 | -6.3933 | -59.9929 | 2024-10-14 00:45:43 | GOES-16 | NOVO ARIPUANÃ | AMAZONAS | Brasil | 1303304 | 13 | 33 | nan | nan | nan | Amazônia | 65.4 |
| a5bdac6c-7af5-3ca1-86eb-ebac5788f686 | -7.9437 | -49.0623 | 2024-10-14 00:45:51 | GOES-16 | BERNARDO SAYÃO | TOCANTINS | Brasil | 1703206 | 17 | 33 | nan | nan | nan | Amazônia | 88.3 |
| b421cbe3-cf71-3500-a448-91a3e1237ac2 | -7.9623 | -49.0823 | 2024-10-14 00:45:52 | GOES-16 | BERNARDO SAYÃO | TOCANTINS | Brasil | 1703206 | 17 | 33 | nan | nan | nan | Amazônia | 71.3 |
| 68b7c1b2-3f78-3266-862c-408ab7efb6a8 | -7.9625 | -49.0607 | 2024-10-14 00:45:52 | GOES-16 | BERNARDO SAYÃO | TOCANTINS | Brasil | 1703206 | 17 | 33 | nan | nan | nan | Amazônia | 151.9 |
| 44c21d7c-aa13-36f7-a7bc-2b9f04b148f8 | -7.9418 | -63.6365 | 2024-10-14 00:45:52 | GOES-16 | CANUTAMA | AMAZONAS | Brasil | 1300904 | 13 | 33 | nan | nan | nan | Amazônia | 92.2 |
| fe47f3e3-6abc-3c37-8612-d0ff1176b7d5 | -7.9419 | -63.6177 | 2024-10-14 00:45:52 | GOES-16 | HUMAITÁ | AMAZONAS | Brasil | 1301704 | 13 | 33 | nan | nan | nan | Amazônia | 81.2 |
| 0ae6f439-a8c3-39d4-9101-1c6ccd4c6d8e | -7.9603 | -63.6359 | 2024-10-14 00:45:52 | GOES-16 | CANUTAMA | AMAZONAS | Brasil | 1300904 | 13 | 33 | nan | nan | nan | Amazônia | 69.1 |
| dd82bca8-96c0-3735-8719-54c70afc7ed7 | -7.9604 | -63.6171 | 2024-10-14 00:45:52 | GOES-16 | HUMAITÁ | AMAZONAS | Brasil | 1301704 | 13 | 33 | nan | nan | nan | Amazônia | 61.7 |
| 42bbbb83-7d9d-39a2-bc63-3c77d2ca40f2 | -8.3207 | -42.7394 | 2024-10-14 00:45:53 | GOES-16 | BREJO DO PIAUÍ | PIAUÍ | Brasil | 2201988 | 22 | 33 | nan | nan | nan | Caatinga | 68.8 |
| ae6f1f9c-7579-378f-8510-e99ee28a3660 | -8.4921 | -48.6259 | 2024-10-14 00:45:54 | GOES-16 | PRESIDENTE KENNEDY | TOCANTINS | Brasil | 1718402 | 17 | 33 | nan | nan | nan | Amazônia | 88.4 |
| 032aa00b-1b1b-3128-8467-c60e6058de46 | -8.7377 | -63.4952 | 2024-10-14 00:45:57 | GOES-16 | CANDEIAS DO JAMARI | RONDÔNIA | Brasil | 1100809 | 11 | 33 | nan | nan | nan | Amazônia | 50.6 |
| d595d238-7ce7-3d06-83b9-aadd160ffbe1 | -8.7378 | -63.4763 | 2024-10-14 00:45:57 | GOES-16 | CANDEIAS DO JAMARI | RONDÔNIA | Brasil | 1100809 | 11 | 33 | nan | nan | nan | Amazônia | 49.0 |
| 7183a5c5-5c72-3437-a560-e250c85a712d | -9.1021 | -47.9355 | 2024-10-14 00:45:58 | GOES-16 | BOM JESUS DO TOCANTINS | TOCANTINS | Brasil | 1703305 | 17 | 33 | nan | nan | nan | Cerrado | 96.7 |
| a76bc5ce-f0ce-3064-a8f3-939f2071dcab | -9.1042 | -61.1811 | 2024-10-14 00:45:59 | GOES-16 | COLNIZA | MATO GROSSO | Brasil | 5103254 | 51 | 33 | nan | nan | nan | Amazônia | 75.3 |
| 379e1c2b-0a32-315f-b294-16b9930901ca | -9.1043 | -61.162 | 2024-10-14 00:45:59 | GOES-16 | COLNIZA | MATO GROSSO | Brasil | 5103254 | 51 | 33 | nan | nan | nan | Amazônia | 91.8 |
| 4f4334bb-0ed7-35b3-95a0-93c8f8f0e7f2 | -9.4699 | -45.8249 | 2024-10-14 00:46:00 | GOES-16 | ALTO PARNAÍBA | MARANHÃO | Brasil | 2100501 | 21 | 33 | nan | nan | nan | Cerrado | 89.5 |
| 34c3a454-3887-3010-81e6-4ae6c5164218 | -9.6928 | -47.4774 | 2024-10-14 00:46:01 | GOES-16 | RIO SONO | TOCANTINS | Brasil | 1718758 | 17 | 33 | nan | nan | nan | Cerrado | 132.6 |
| 562e41b8-2e8d-355c-a454-8d849867b99f | -9.7117 | -47.4754 | 2024-10-14 00:46:01 | GOES-16 | RIO SONO | TOCANTINS | Brasil | 1718758 | 17 | 33 | nan | nan | nan | Cerrado | 92.9 |
| 7f8a565f-02b9-3798-b0b1-8451ba6717e6 | -10.0816 | -44.2133 | 2024-10-14 00:46:03 | GOES-16 | CURIMATÁ | PIAUÍ | Brasil | 2203206 | 22 | 33 | nan | nan | nan | Cerrado | 262.0 |
| 4a1b19a8-cb21-347d-b973-e0c3d2f3f720 | -10.0622 | -44.2391 | 2024-10-14 00:46:03 | GOES-16 | CURIMATÁ | PIAUÍ | Brasil | 2203206 | 22 | 33 | nan | nan | nan | Cerrado | 149.2 |
| f1cafe7d-afe1-3653-8e83-2ed36298d91a | -10.0626 | -44.2158 | 2024-10-14 00:46:03 | GOES-16 | CURIMATÁ | PIAUÍ | Brasil | 2203206 | 22 | 33 | nan | nan | nan | Cerrado | 125.3 |
| f0b0c166-5032-3131-8dc5-40fa4070ee64 | -10.0809 | -44.2599 | 2024-10-14 00:46:03 | GOES-16 | CURIMATÁ | PIAUÍ | Brasil | 2203206 | 22 | 33 | nan | nan | nan | Cerrado | 98.4 |
| aede9d34-ba03-309e-86e7-e47f50a8c2ba | -10.0813 | -44.2366 | 2024-10-14 00:46:03 | GOES-16 | CURIMATÁ | PIAUÍ | Brasil | 2203206 | 22 | 33 | nan | nan | nan | Cerrado | 440.2 |
| 10235e43-3f3e-3937-8e40-c27c871051b9 | -9.9973 | -47.3329 | 2024-10-14 00:46:03 | GOES-16 | RIO SONO | TOCANTINS | Brasil | 1718758 | 17 | 33 | nan | nan | nan | Cerrado | 102.1 |
| 4018cf30-93ef-38e8-85c3-f28fc410831e | -9.9976 | -47.3107 | 2024-10-14 00:46:03 | GOES-16 | RIO SONO | TOCANTINS | Brasil | 1718758 | 17 | 33 | nan | nan | nan | Cerrado | 106.2 |
| 9dc4e7b0-9da1-3937-9116-a39ae29d86cf | -10.016 | -47.353 | 2024-10-14 00:46:03 | GOES-16 | RIO SONO | TOCANTINS | Brasil | 1718758 | 17 | 33 | nan | nan | nan | Cerrado | 97.2 |
| 372a62fa-78a5-3131-aa5a-e6244234da2f | -10.0163 | -47.3308 | 2024-10-14 00:46:03 | GOES-16 | RIO SONO | TOCANTINS | Brasil | 1718758 | 17 | 33 | nan | nan | nan | Cerrado | 214.9 |
| 9cc79cde-69b4-31e4-90d0-ca8b808fb181 | -10.0166 | -47.3085 | 2024-10-14 00:46:03 | GOES-16 | RIO SONO | TOCANTINS | Brasil | 1718758 | 17 | 33 | nan | nan | nan | Cerrado | 120.6 |
| 62de733d-a3f7-35d9-b0a4-c0156a080c59 | -10.0352 | -47.3286 | 2024-10-14 00:46:03 | GOES-16 | RIO SONO | TOCANTINS | Brasil | 1718758 | 17 | 33 | nan | nan | nan | Cerrado | 102.1 |
| 044aff87-8878-3a28-9b93-3bc215c3bfa1 | -10.4918 | -42.433 | 2024-10-14 00:46:05 | GOES-16 | XIQUE-XIQUE | BAHIA | Brasil | 2933604 | 29 | 33 | nan | nan | nan | Caatinga | 93.5 |
| c20dc649-45ea-3f5a-be7a-73f8153ec80e | -10.3303 | -46.58 | 2024-10-14 00:46:05 | GOES-16 | MATEIROS | TOCANTINS | Brasil | 1712702 | 17 | 33 | nan | nan | nan | Cerrado | 82.7 |
| e8976804-912d-3b34-80e3-2928fd99dffd | -11.17 | -39.9192 | 2024-10-14 00:46:09 | GOES-16 | QUEIMADAS | BAHIA | Brasil | 2925808 | 29 | 33 | nan | nan | nan | Caatinga | 74.8 |
| a62d522a-0fb0-353c-b84e-f305049d963e | -11.1705 | -39.894 | 2024-10-14 00:46:09 | GOES-16 | QUEIMADAS | BAHIA | Brasil | 2925808 | 29 | 33 | nan | nan | nan | Caatinga | 106.4 |
| 32d93095-a420-37e0-876d-00dbf1a13489 | -11.1898 | -39.8906 | 2024-10-14 00:46:09 | GOES-16 | QUEIMADAS | BAHIA | Brasil | 2925808 | 29 | 33 | nan | nan | nan | Caatinga | 69.3 |
| 810513fa-6cdd-3bff-a219-faa3d19009e0 | -12.4981 | -63.0148 | 2024-10-14 00:46:18 | GOES-16 | SÃO FRANCISCO DO GUAPORÉ | RONDÔNIA | Brasil | 1101492 | 11 | 33 | nan | nan | nan | Amazônia | 69.0 |
| c5130a0b-5ed0-393f-8ac5-a2d48d37c065 | -12.4983 | -62.9956 | 2024-10-14 00:46:18 | GOES-16 | SÃO FRANCISCO DO GUAPORÉ | RONDÔNIA | Brasil | 1101492 | 11 | 33 | nan | nan | nan | Amazônia | 58.5 |
| b1f896e9-80d0-308c-9bd1-713ae28c004e | -12.8699 | -53.5423 | 2024-10-14 00:46:19 | GOES-16 | GAÚCHA DO NORTE | MATO GROSSO | Brasil | 5103858 | 51 | 33 | nan | nan | nan | Amazônia | 65.1 |
| 0e6b329c-ce63-3871-8355-6e470a426a4c | -12.8702 | -53.5215 | 2024-10-14 00:46:19 | GOES-16 | GAÚCHA DO NORTE | MATO GROSSO | Brasil | 5103858 | 51 | 33 | nan | nan | nan | Amazônia | 64.6 |
| 4729fb64-d206-30f5-b05d-5bf7b94bb9f4 | -12.889 | -53.5402 | 2024-10-14 00:46:19 | GOES-16 | GAÚCHA DO NORTE | MATO GROSSO | Brasil | 5103858 | 51 | 33 | nan | nan | nan | Amazônia | 96.7 |
| 150bee32-ed61-3a58-b774-52b6e19f0f66 | -12.8893 | -53.5194 | 2024-10-14 00:46:19 | GOES-16 | GAÚCHA DO NORTE | MATO GROSSO | Brasil | 5103858 | 51 | 33 | nan | nan | nan | Amazônia | 78.7 |
| 1e46795c-767d-3cc7-8491-b960eec2ae07 | -17.0004 | -57.4176 | 2024-10-14 00:46:42 | GOES-16 | CÁCERES | MATO GROSSO | Brasil | 5102504 | 51 | 33 | nan | nan | nan | Pantanal | 62.0 |
| 6f3abc67-a215-3f75-9ee5-741674ab32b2 | -17.02 | -57.4153 | 2024-10-14 00:46:42 | GOES-16 | CÁCERES | MATO GROSSO | Brasil | 5102504 | 51 | 33 | nan | nan | nan | Pantanal | 55.7 |
| c1a997f1-11f3-3d3d-8201-cc1cfa323dcd | -17.1957 | -57.4562 | 2024-10-14 00:46:43 | GOES-16 | CÁCERES | MATO GROSSO | Brasil | 5102504 | 51 | 33 | nan | nan | nan | Pantanal | 68.7 |
| e0276ca2-2e61-3c63-ac49-3b1f0d7ec00f | -17.196 | -57.4357 | 2024-10-14 00:46:43 | GOES-16 | CÁCERES | MATO GROSSO | Brasil | 5102504 | 51 | 33 | nan | nan | nan | Pantanal | 60.2 |
| 54d3b29a-826a-3ec8-8ad0-754201ba7c43 | -17.6471 | -56.3084 | 2024-10-14 00:46:46 | GOES-16 | CORUMBÁ | MATO GROSSO DO SUL | Brasil | 5003207 | 50 | 33 | nan | nan | nan | Pantanal | 71.4 |
| f727ba5d-53a6-339e-9019-2eeda640dddf | -17.6474 | -56.2876 | 2024-10-14 00:46:46 | GOES-16 | CORUMBÁ | MATO GROSSO DO SUL | Brasil | 5003207 | 50 | 33 | nan | nan | nan | Pantanal | 63.0 |
| a19013e8-cee3-3863-b73f-9464921bc959 | -17.6876 | -56.2409 | 2024-10-14 00:46:46 | GOES-16 | CORUMBÁ | MATO GROSSO DO SUL | Brasil | 5003207 | 50 | 33 | nan | nan | nan | Pantanal | 70.3 |
| 258e3f3b-1e42-38c4-8874-850adbd23560 | -17.7264 | -56.2774 | 2024-10-14 00:46:46 | GOES-16 | CORUMBÁ | MATO GROSSO DO SUL | Brasil | 5003207 | 50 | 33 | nan | nan | nan | Pantanal | 66.5 |
| c155a8eb-e3be-3dbd-9415-13a8d4e67813 | -19.0724 | -48.3148 | 2024-10-14 00:46:52 | GOES-16 | UBERLÂNDIA | MINAS GERAIS | Brasil | 3170206 | 31 | 33 | nan | nan | nan | Cerrado | 82.4 |
| 7d1e5384-09e6-3d06-980c-792d37af18fc | -21.8842 | -48.9765 | 2024-10-14 00:47:07 | GOES-16 | IACANGA | SÃO PAULO | Brasil | 3519105 | 35 | 33 | nan | nan | nan | Mata Atlântica | 58.0 |
| 0b74dc4d-eb8a-3ac3-a787-823e481aa44a | -21.8849 | -48.9531 | 2024-10-14 00:47:07 | GOES-16 | IACANGA | SÃO PAULO | Brasil | 3519105 | 35 | 33 | nan | nan | nan | Mata Atlântica | 63.3 |
| 19f0a79b-a41b-3522-83d6-89597e18c255 | -2.4344 | -46.9195 | 2024-10-14 00:55:20 | GOES-16 | PARAGOMINAS | PARÁ | Brasil | 1505502 | 15 | 33 | nan | nan | nan | Amazônia | 101.7 |
| c5c24480-8514-354a-8d64-644fad084849 | -2.4529 | -46.919 | 2024-10-14 00:55:20 | GOES-16 | PARAGOMINAS | PARÁ | Brasil | 1505502 | 15 | 33 | nan | nan | nan | Amazônia | 84.7 |
| 7e1890d1-e909-3610-8720-283660997e48 | -2.6117 | -49.1198 | 2024-10-14 00:55:21 | GOES-16 | MOJU | PARÁ | Brasil | 1504703 | 15 | 33 | nan | nan | nan | Amazônia | 32.6 |
| 68f56241-7742-34e9-b47f-085de7a3d788 | -2.6118 | -49.0985 | 2024-10-14 00:55:21 | GOES-16 | MOJU | PARÁ | Brasil | 1504703 | 15 | 33 | nan | nan | nan | Amazônia | 29.1 |
| 5769aceb-e54b-33fd-a12f-7a00c6fe33db | -2.6052 | -57.5711 | 2024-10-14 00:55:21 | GOES-16 | URUCURITUBA | AMAZONAS | Brasil | 1304401 | 13 | 33 | nan | nan | nan | Amazônia | 50.7 |
| 9edca452-4335-377f-b0c0-b81535cf3de4 | -3.2889 | -42.8561 | 2024-10-14 00:55:25 | GOES-16 | SANTA QUITÉRIA DO MARANHÃO | MARANHÃO | Brasil | 2110104 | 21 | 33 | nan | nan | nan | Cerrado | 58.8 |
| 328e8b2e-fed5-35ba-b815-605f739b85ea | -3.289 | -42.8327 | 2024-10-14 00:55:25 | GOES-16 | SANTA QUITÉRIA DO MARANHÃO | MARANHÃO | Brasil | 2110104 | 21 | 33 | nan | nan | nan | Cerrado | 106.4 |
| e63f5046-0266-3b53-9913-25563ef62e02 | -3.3076 | -42.8553 | 2024-10-14 00:55:25 | GOES-16 | SANTA QUITÉRIA DO MARANHÃO | MARANHÃO | Brasil | 2110104 | 21 | 33 | nan | nan | nan | Cerrado | 216.5 |
| a7c9cba3-a841-3db7-866e-e8c6ea95943c | -3.3077 | -42.8318 | 2024-10-14 00:55:25 | GOES-16 | SANTA QUITÉRIA DO MARANHÃO | MARANHÃO | Brasil | 2110104 | 21 | 33 | nan | nan | nan | Cerrado | 298.5 |
| 8b2a6448-c0f9-3dfb-85a1-f1c6907d83c4 | -3.3274 | -50.3245 | 2024-10-14 00:55:25 | GOES-16 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 35.5 |
| c23bf3ef-63d5-3cba-a9f9-ca07b62ca4c6 | -3.3275 | -50.3035 | 2024-10-14 00:55:25 | GOES-16 | PACAJÁ | PARÁ | Brasil | 1505486 | 15 | 33 | nan | nan | nan | Amazônia | 33.9 |
| 53da8c48-8ae9-3b51-ad6f-7c89ee0e71b1 | -3.3643 | -50.3233 | 2024-10-14 00:55:25 | GOES-16 | PACAJÁ | PARÁ | Brasil | 1505486 | 15 | 33 | nan | nan | nan | Amazônia | 33.5 |
| 61e5ceaf-5f10-3fd6-b8c7-05ba16fec5fc | -3.8723 | -52.2769 | 2024-10-14 00:55:28 | GOES-16 | SENADOR JOSÉ PORFÍRIO | PARÁ | Brasil | 1507805 | 15 | 33 | nan | nan | nan | Amazônia | 48.4 |
| c7b4de5c-2ebf-3eaf-8550-bd94accd0f0c | -4.1145 | -48.2947 | 2024-10-14 00:55:30 | GOES-16 | DOM ELISEU | PARÁ | Brasil | 1502939 | 15 | 33 | nan | nan | nan | Amazônia | 67.1 |
| 87744206-9ca4-3106-ab47-e0a26a2f7ecc | -4.1146 | -48.2731 | 2024-10-14 00:55:30 | GOES-16 | DOM ELISEU | PARÁ | Brasil | 1502939 | 15 | 33 | nan | nan | nan | Amazônia | 82.2 |
| 8dd0f5e6-8964-301c-a33e-cd4695d4d723 | -4.3428 | -50.5172 | 2024-10-14 00:55:31 | GOES-16 | NOVO REPARTIMENTO | PARÁ | Brasil | 1505064 | 15 | 33 | nan | nan | nan | Amazônia | 120.8 |
| f37b448e-d0b0-3138-99c9-7d00d7fd65d2 | -4.343 | -50.4962 | 2024-10-14 00:55:31 | GOES-16 | NOVO REPARTIMENTO | PARÁ | Brasil | 1505064 | 15 | 33 | nan | nan | nan | Amazônia | 88.8 |
| 82c38634-3264-3b43-82f3-2c6949cb8d30 | -4.6197 | -44.8626 | 2024-10-14 00:55:32 | GOES-16 | IGARAPÉ GRANDE | MARANHÃO | Brasil | 2105203 | 21 | 33 | nan | nan | nan | Cerrado | 109.1 |


[Clique aqui para ver as próximas entradas](README15.md)
