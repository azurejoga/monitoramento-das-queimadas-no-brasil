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

## Dados Diários - Página 26

| ID | Latitude | Longitude | Data/Hora GMT | Satélite | Município | Estado | País | Município ID | Estado ID | País ID | Dias sem Chuva | Precipitação | Risco de Fogo | Bioma | FRP |
|----|----------|-----------|---------------|----------|-----------|--------|------|--------------|-----------|---------|----------------|--------------|----------------|-------|-----|
| 825b1126-4e4e-3a3d-826c-7f0004561c42 | -3.47948 | -53.24346 | 2025-11-01 05:08:00 | NPP-375D | MEDICILÂNDIA | PARÁ | Brasil | 1504455 | 15 | 33 | nan | nan | nan | Amazônia | 0.6 |
| ae242003-f62c-362a-be00-101b7c46a081 | -5.07192 | -45.11117 | 2025-11-01 05:08:00 | NPP-375D | SÃO RAIMUNDO DO DOCA BEZERRA | MARANHÃO | Brasil | 2111631 | 21 | 33 | nan | nan | nan | Cerrado | 0.7 |
| 1765ee78-1ecd-368a-9002-4169b889dfe6 | -5.83432 | -44.0621 | 2025-11-01 05:08:00 | NPP-375D | BURITI BRAVO | MARANHÃO | Brasil | 2102309 | 21 | 33 | nan | nan | nan | Cerrado | 6.4 |
| 62a82d87-16ed-3893-a91f-2bfe0e65a9b7 | -3.863 | -51.17196 | 2025-11-01 05:08:00 | NPP-375D | PACAJÁ | PARÁ | Brasil | 1505486 | 15 | 33 | nan | nan | nan | Amazônia | 1.3 |
| aac54c6c-3c9b-3ffe-a671-d76f186c5c1e | -5.90068 | -49.14644 | 2025-11-01 05:08:00 | NPP-375D | ELDORADO DO CARAJÁS | PARÁ | Brasil | 1502954 | 15 | 33 | nan | nan | nan | Amazônia | 2.1 |
| de2549e0-7b08-3508-8f12-a86151ae377a | -4.82786 | -45.7888 | 2025-11-01 05:08:00 | NPP-375D | ARAME | MARANHÃO | Brasil | 2100956 | 21 | 33 | nan | nan | nan | Amazônia | 1.3 |
| 700c65b0-2a7a-3a08-a36e-3c60ebe9ea82 | -4.1814 | -47.64938 | 2025-11-01 05:08:00 | NPP-375D | DOM ELISEU | PARÁ | Brasil | 1502939 | 15 | 33 | nan | nan | nan | Amazônia | 9.8 |
| 23212d11-694b-365f-9f24-928c1c83e127 | -4.61549 | -46.59546 | 2025-11-01 05:08:00 | NPP-375D | BOM JESUS DAS SELVAS | MARANHÃO | Brasil | 2102036 | 21 | 33 | nan | nan | nan | Amazônia | 1.2 |
| d936dce6-7b3b-34c1-93cb-bb532a247192 | -5.45652 | -45.40297 | 2025-11-01 05:08:00 | NPP-375D | BARRA DO CORDA | MARANHÃO | Brasil | 2101608 | 21 | 33 | nan | nan | nan | Cerrado | 1.2 |
| 40fbad0e-d2eb-37d4-836d-aaef68c8638e | -3.01777 | -53.96942 | 2025-11-01 05:08:00 | NPP-375D | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | 4.9 |
| df601433-91ba-3cfd-81ad-9f2ecc5a6dee | -8.85886 | -49.8793 | 2025-11-01 05:08:00 | NPP-375D | SANTA MARIA DAS BARREIRAS | PARÁ | Brasil | 1506583 | 15 | 33 | nan | nan | nan | Amazônia | 13.5 |
| 14a1a171-2edd-364d-a20c-1b8472493eb3 | -10.42378 | -49.36792 | 2025-11-01 05:08:00 | NPP-375D | PIUM | TOCANTINS | Brasil | 1717503 | 17 | 33 | nan | nan | nan | Cerrado | 0.9 |
| 603d55a1-197a-375c-b769-9388d42f4076 | -6.93593 | -49.6319 | 2025-11-01 05:08:00 | NPP-375D | SAPUCAIA | PARÁ | Brasil | 1507755 | 15 | 33 | nan | nan | nan | Amazônia | 1.1 |
| 1b6356fe-c48e-3438-99f5-40ac0306d0b9 | -4.9484 | -48.26342 | 2025-11-01 05:08:00 | NPP-375D | ABEL FIGUEIREDO | PARÁ | Brasil | 1500131 | 15 | 33 | nan | nan | nan | Amazônia | 1.3 |
| 48733e79-6c14-3590-8355-f9d114b28811 | -6.32335 | -43.62901 | 2025-11-01 05:08:00 | NPP-375D | SUCUPIRA DO RIACHÃO | MARANHÃO | Brasil | 2111953 | 21 | 33 | nan | nan | nan | Cerrado | 4.1 |
| 01211fa4-8dd9-39de-a5e6-09232e1ad123 | -7.06786 | -47.36283 | 2025-11-01 05:08:00 | NPP-375D | CAROLINA | MARANHÃO | Brasil | 2102804 | 21 | 33 | nan | nan | nan | Cerrado | 1.0 |
| 5e3497fd-2349-3186-b664-d48bf887ef3d | -4.67276 | -46.52512 | 2025-11-01 05:08:00 | NPP-375D | BOM JESUS DAS SELVAS | MARANHÃO | Brasil | 2102036 | 21 | 33 | nan | nan | nan | Amazônia | 1.1 |
| 4d523542-8300-3ef9-aede-51ced19fbb50 | -5.21301 | -45.83495 | 2025-11-01 05:08:00 | NPP-375D | ITAIPAVA DO GRAJAÚ | MARANHÃO | Brasil | 2105351 | 21 | 33 | nan | nan | nan | Cerrado | 0.8 |
| a0520cb4-2146-3c89-a817-8db9e2880e3d | -7.0691 | -47.00578 | 2025-11-01 05:08:00 | NPP-375D | CAROLINA | MARANHÃO | Brasil | 2102804 | 21 | 33 | nan | nan | nan | Cerrado | 1.2 |
| dda204e3-eeda-3f8b-84bb-d3b593064713 | -2.63479 | -59.60321 | 2025-11-01 05:08:00 | NPP-375D | RIO PRETO DA EVA | AMAZONAS | Brasil | 1303569 | 13 | 33 | nan | nan | nan | Amazônia | 1.1 |
| 7bfa0970-f351-3635-a5f2-877d98ccc098 | -10.6362 | -52.17873 | 2025-11-01 05:08:00 | NPP-375D | PORTO ALEGRE DO NORTE | MATO GROSSO | Brasil | 5106778 | 51 | 33 | nan | nan | nan | Amazônia | 1.4 |
| 74d6a376-f02a-3565-8350-9c286f9cbcff | -4.52576 | -46.40201 | 2025-11-01 05:08:00 | NPP-375D | BURITICUPU | MARANHÃO | Brasil | 2102325 | 21 | 33 | nan | nan | nan | Amazônia | 0.4 |
| fba7c684-e04e-3ec2-87c5-90e2ff6c3292 | -5.83502 | -44.05709 | 2025-11-01 05:08:00 | NPP-375D | BURITI BRAVO | MARANHÃO | Brasil | 2102309 | 21 | 33 | nan | nan | nan | Cerrado | 6.4 |
| c84a24f2-e823-37a3-9d45-7fb4f8d47e61 | -5.80355 | -44.54487 | 2025-11-01 05:08:00 | NPP-375D | TUNTUM | MARANHÃO | Brasil | 2112308 | 21 | 33 | nan | nan | nan | Cerrado | 1.3 |
| 434686d4-85fa-36e0-8953-43df5a7a05b4 | -4.43913 | -46.03713 | 2025-11-01 05:08:00 | NPP-375D | SANTA LUZIA | MARANHÃO | Brasil | 2110005 | 21 | 33 | nan | nan | nan | Amazônia | 1.4 |
| 284dd4a7-2c44-3143-92dc-691ddc2186fe | -4.03264 | -47.77455 | 2025-11-01 05:08:00 | NPP-375D | ULIANÓPOLIS | PARÁ | Brasil | 1508126 | 15 | 33 | nan | nan | nan | Amazônia | 1.3 |
| 4127135c-331a-32ff-95db-772259d45fc0 | -5.21253 | -45.8384 | 2025-11-01 05:08:00 | NPP-375D | ITAIPAVA DO GRAJAÚ | MARANHÃO | Brasil | 2105351 | 21 | 33 | nan | nan | nan | Amazônia | 1.0 |
| 3e08b587-6b01-3bbc-a826-78ab8629080f | -3.66075 | -50.18934 | 2025-11-01 05:08:00 | NPP-375D | PACAJÁ | PARÁ | Brasil | 1505486 | 15 | 33 | nan | nan | nan | Amazônia | 0.7 |
| 3f1a2364-4c82-3fb7-809c-ff78da853546 | -3.60242 | -50.62108 | 2025-11-01 05:08:00 | NPP-375D | PACAJÁ | PARÁ | Brasil | 1505486 | 15 | 33 | nan | nan | nan | Amazônia | 1.9 |
| 178490d6-50bd-3531-9b99-17644e623697 | -3.67502 | -51.75473 | 2025-11-01 05:08:00 | NPP-375D | SENADOR JOSÉ PORFÍRIO | PARÁ | Brasil | 1507805 | 15 | 33 | nan | nan | nan | Amazônia | 0.9 |
| 1828f80c-396c-3447-920e-c18f279eff61 | -4.82181 | -45.79132 | 2025-11-01 05:08:00 | NPP-375D | ARAME | MARANHÃO | Brasil | 2100956 | 21 | 33 | nan | nan | nan | Amazônia | 1.3 |
| f15d758a-7605-31cc-a580-3e6532815c15 | -3.80106 | -51.15059 | 2025-11-01 05:08:00 | NPP-375D | PACAJÁ | PARÁ | Brasil | 1505486 | 15 | 33 | nan | nan | nan | Amazônia | 1.6 |
| 1e7f23a2-8a7a-3c17-8531-a80d01fd57aa | -4.64485 | -47.9498 | 2025-11-01 05:08:00 | NPP-375D | RONDON DO PARÁ | PARÁ | Brasil | 1506187 | 15 | 33 | nan | nan | nan | Amazônia | 3.0 |
| 18ad933f-0252-3f95-b47c-57be66ab1159 | -3.87998 | -51.18887 | 2025-11-01 05:08:00 | NPP-375D | PACAJÁ | PARÁ | Brasil | 1505486 | 15 | 33 | nan | nan | nan | Amazônia | 0.7 |
| 5b596800-1856-3649-8115-9bcfa94591bb | -9.02568 | -47.46 | 2025-11-01 05:08:00 | NPP-375D | CENTENÁRIO | TOCANTINS | Brasil | 1704105 | 17 | 33 | nan | nan | nan | Cerrado | 1.6 |
| c97406ff-26f2-334f-b275-4079f9552628 | -7.07441 | -47.00648 | 2025-11-01 05:08:00 | NPP-375D | CAROLINA | MARANHÃO | Brasil | 2102804 | 21 | 33 | nan | nan | nan | Cerrado | 1.2 |
| 65e5bd00-95fe-316a-b5d0-adc769eab09e | -4.82842 | -45.78493 | 2025-11-01 05:08:00 | NPP-375D | ARAME | MARANHÃO | Brasil | 2100956 | 21 | 33 | nan | nan | nan | Amazônia | 1.2 |
| 881e4a28-69fb-3261-a3d2-4094564cadf5 | -4.6731 | -45.81176 | 2025-11-01 05:08:00 | NPP-375D | MARAJÁ DO SENA | MARANHÃO | Brasil | 2106359 | 21 | 33 | nan | nan | nan | Amazônia | 1.0 |
| cfb9badf-6d16-3f12-8370-16b49010c419 | -4.66781 | -45.81365 | 2025-11-01 05:08:00 | NPP-375D | MARAJÁ DO SENA | MARANHÃO | Brasil | 2106359 | 21 | 33 | nan | nan | nan | Amazônia | 1.1 |
| 932f00b9-9925-3a06-b289-99dd3c0e2869 | -4.17758 | -47.65333 | 2025-11-01 05:08:00 | NPP-375D | DOM ELISEU | PARÁ | Brasil | 1502939 | 15 | 33 | nan | nan | nan | Amazônia | 4.7 |
| b8006552-c873-320c-8585-6798ea7cd28d | -4.9531 | -48.26423 | 2025-11-01 05:08:00 | NPP-375D | ABEL FIGUEIREDO | PARÁ | Brasil | 1500131 | 15 | 33 | nan | nan | nan | Amazônia | 1.3 |
| 88566394-8152-3fa1-9fd3-c6c977a92a83 | -6.77465 | -55.4866 | 2025-11-01 05:08:00 | NPP-375D | NOVO PROGRESSO | PARÁ | Brasil | 1505031 | 15 | 33 | nan | nan | nan | Amazônia | 0.6 |
| 90a6f09e-8da3-361e-baab-7a0e43dc2845 | -5.12365 | -43.38673 | 2025-11-01 05:08:00 | NPP-375D | CAXIAS | MARANHÃO | Brasil | 2103000 | 21 | 33 | nan | nan | nan | Cerrado | 1.4 |
| 12942be4-39f2-3a71-92ad-820936a4a82b | -4.50246 | -45.67363 | 2025-11-01 05:08:00 | NPP-375D | PAULO RAMOS | MARANHÃO | Brasil | 2108108 | 21 | 33 | nan | nan | nan | Amazônia | 1.7 |
| 6ae71992-e654-3548-a0c6-f7c8d790b6d1 | -4.80568 | -48.71497 | 2025-11-01 05:08:00 | NPP-375D | BOM JESUS DO TOCANTINS | PARÁ | Brasil | 1501576 | 15 | 33 | nan | nan | nan | Amazônia | 2.6 |
| 3fc47573-0018-3bf9-817c-f58ab872a56c | -3.64225 | -53.98576 | 2025-11-01 05:08:00 | NPP-375D | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | 0.6 |
| 18649a29-db3e-3ba8-bcbf-66b0664fbdb9 | -3.32289 | -52.62654 | 2025-11-01 05:08:00 | NPP-375D | BRASIL NOVO | PARÁ | Brasil | 1501725 | 15 | 33 | nan | nan | nan | Amazônia | 0.6 |
| 8c548d4f-0870-34d3-b716-efbde7c64888 | -2.91253 | -53.94897 | 2025-11-01 05:08:00 | NPP-375D | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | 0.9 |
| 476f0944-2cba-3a9b-8a27-9d09373f6303 | -3.74265 | -53.39344 | 2025-11-01 05:08:00 | NPP-375D | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | 0.6 |
| a32dd74c-3e66-3677-a527-64daf4f4970b | -4.70565 | -46.44632 | 2025-11-01 05:08:00 | NPP-375D | BURITICUPU | MARANHÃO | Brasil | 2102325 | 21 | 33 | nan | nan | nan | Amazônia | 3.2 |
| b580148a-bafe-3a79-8178-9bbf9839c81e | -3.79907 | -51.61312 | 2025-11-01 05:08:00 | NPP-375D | SENADOR JOSÉ PORFÍRIO | PARÁ | Brasil | 1507805 | 15 | 33 | nan | nan | nan | Amazônia | 0.8 |
| 22169d0e-72fc-3447-9771-33ec31449816 | -6.61947 | -47.1771 | 2025-11-01 05:08:00 | NPP-375D | ESTREITO | MARANHÃO | Brasil | 2104057 | 21 | 33 | nan | nan | nan | Cerrado | 3.3 |
| fac5f8cf-21b2-32f7-9609-0726027f5f33 | -4.53158 | -46.39936 | 2025-11-01 05:08:00 | NPP-375D | BURITICUPU | MARANHÃO | Brasil | 2102325 | 21 | 33 | nan | nan | nan | Amazônia | 0.9 |
| 8e0c2a3e-4900-36d0-b4bf-a6d43d377d7d | -3.98095 | -48.91302 | 2025-11-01 05:08:00 | NPP-375D | GOIANÉSIA DO PARÁ | PARÁ | Brasil | 1503093 | 15 | 33 | nan | nan | nan | Amazônia | 4.1 |
| f2c7a01a-cd27-3ce1-91e7-85a42d89489c | -5.06725 | -45.11311 | 2025-11-01 05:08:00 | NPP-375D | SÃO RAIMUNDO DO DOCA BEZERRA | MARANHÃO | Brasil | 2111631 | 21 | 33 | nan | nan | nan | Cerrado | 0.7 |
| 0bcfeeb4-fcb8-3a0d-aac0-f8fe2533f158 | -10.41196 | -44.32717 | 2025-11-01 05:08:00 | NPP-375D | PARNAGUÁ | PIAUÍ | Brasil | 2207603 | 22 | 33 | nan | nan | nan | Cerrado | 2.7 |
| 144eb04c-fa5c-3254-9906-7c0db5ec2f7b | -4.70653 | -55.98837 | 2025-11-01 05:08:00 | NPP-375D | TRAIRÃO | PARÁ | Brasil | 1508050 | 15 | 33 | nan | nan | nan | Amazônia | 1.5 |
| 063754c0-cf89-37a8-8e60-fefc79b649cb | -3.87616 | -51.18832 | 2025-11-01 05:08:00 | NPP-375D | PACAJÁ | PARÁ | Brasil | 1505486 | 15 | 33 | nan | nan | nan | Amazônia | 0.7 |
| c3e40440-d9f2-3d73-858f-70a53f0db773 | -3.46655 | -50.93867 | 2025-11-01 05:08:00 | NPP-375D | PACAJÁ | PARÁ | Brasil | 1505486 | 15 | 33 | nan | nan | nan | Amazônia | 1.1 |
| 79f4d15a-d31e-31a4-991e-6ec6186a102e | -10.63085 | -52.18818 | 2025-11-01 05:08:00 | NPP-375D | PORTO ALEGRE DO NORTE | MATO GROSSO | Brasil | 5106778 | 51 | 33 | nan | nan | nan | Amazônia | 5.0 |
| 30e3cebc-79bc-368c-98b5-185c7084d438 | -4.4273 | -47.60216 | 2025-11-01 05:08:00 | NPP-375D | DOM ELISEU | PARÁ | Brasil | 1502939 | 15 | 33 | nan | nan | nan | Amazônia | 2.5 |
| 75d4969b-1cfc-3a2b-a113-2dc6536308c1 | -5.07313 | -45.11371 | 2025-11-01 05:08:00 | NPP-375D | SÃO RAIMUNDO DO DOCA BEZERRA | MARANHÃO | Brasil | 2111631 | 21 | 33 | nan | nan | nan | Cerrado | 1.0 |
| cd0b6e2b-aa04-3c3d-b4b6-b3bbcc3c5ced | -3.74242 | -53.39294 | 2025-11-01 05:08:00 | NPP-375D | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | 0.7 |
| c3d67b51-0b1f-3c3e-ab27-dc9a54ad989b | -3.83728 | -51.34433 | 2025-11-01 05:08:00 | NPP-375D | ANAPU | PARÁ | Brasil | 1500859 | 15 | 33 | nan | nan | nan | Amazônia | 1.3 |
| a2cdf667-567d-30c4-8ec9-3aa07ebbe839 | -4.66481 | -41.96076 | 2025-11-01 05:08:00 | NPP-375D | COCAL DE TELHA | PIAUÍ | Brasil | 2202711 | 22 | 33 | nan | nan | nan | Caatinga | 2.5 |
| 4aefd80d-6efb-38cb-8f6a-f5832743d249 | -2.90989 | -54.2935 | 2025-11-01 05:08:00 | NPP-375D | MOJUÍ DOS CAMPOS | PARÁ | Brasil | 1504752 | 15 | 33 | nan | nan | nan | Amazônia | 1.1 |
| 1c07c74b-3699-35a2-8666-830a228a1e99 | -6.45978 | -46.72539 | 2025-11-01 05:08:00 | NPP-375D | SÍTIO NOVO | MARANHÃO | Brasil | 2111805 | 21 | 33 | nan | nan | nan | Cerrado | 1.4 |
| d91ab0e7-d65b-310c-9cc9-71cf7cd3cfc8 | -3.38182 | -52.80096 | 2025-11-01 05:08:00 | NPP-375D | MEDICILÂNDIA | PARÁ | Brasil | 1504455 | 15 | 33 | nan | nan | nan | Amazônia | 0.5 |
| 227ed5d5-196d-3a76-b0c9-95b4475c6b46 | -4.55934 | -46.68748 | 2025-11-01 05:08:00 | NPP-375D | BOM JESUS DAS SELVAS | MARANHÃO | Brasil | 2102036 | 21 | 33 | nan | nan | nan | Amazônia | 1.6 |
| 2eb63d9f-834b-36fa-9446-7126f043a9e1 | -6.88511 | -42.85014 | 2025-11-01 05:08:00 | NPP-375D | FLORIANO | PIAUÍ | Brasil | 2203909 | 22 | 33 | nan | nan | nan | Caatinga | 2.6 |
| d5037da0-03b6-3eaa-b4e2-0ad2a3130e46 | -5.17735 | -56.10913 | 2025-11-01 05:08:00 | NPP-375D | TRAIRÃO | PARÁ | Brasil | 1508050 | 15 | 33 | nan | nan | nan | Amazônia | 0.8 |
| 27367ed9-f44c-3599-a219-dea129ae7c8d | -4.77851 | -46.5045 | 2025-11-01 05:08:00 | NPP-375D | BOM JESUS DAS SELVAS | MARANHÃO | Brasil | 2102036 | 21 | 33 | nan | nan | nan | Amazônia | 0.7 |
| c77a774f-d136-3c79-9959-d46e25eadc75 | -6.46267 | -46.72725 | 2025-11-01 05:08:00 | NPP-375D | SÍTIO NOVO | MARANHÃO | Brasil | 2111805 | 21 | 33 | nan | nan | nan | Cerrado | 1.2 |
| 48e79d26-6b02-353d-a6ea-3e9d52b61f7a | -3.73092 | -51.71 | 2025-11-01 05:08:00 | NPP-375D | SENADOR JOSÉ PORFÍRIO | PARÁ | Brasil | 1507805 | 15 | 33 | nan | nan | nan | Amazônia | 1.7 |
| 603315c8-3e94-33ae-82ff-1aea4f9a114d | -10.62692 | -52.18761 | 2025-11-01 05:08:00 | NPP-375D | PORTO ALEGRE DO NORTE | MATO GROSSO | Brasil | 5106778 | 51 | 33 | nan | nan | nan | Amazônia | 3.8 |
| a5243413-92e3-3241-8e18-b04818b54781 | -4.54614 | -45.80284 | 2025-11-01 05:08:00 | NPP-375D | SANTA LUZIA | MARANHÃO | Brasil | 2110005 | 21 | 33 | nan | nan | nan | Amazônia | 1.4 |
| 3125ba5d-9031-3712-82ef-6d766f93db0f | -7.35087 | -46.21075 | 2025-11-01 05:08:00 | NPP-375D | RIACHÃO | MARANHÃO | Brasil | 2109502 | 21 | 33 | nan | nan | nan | Cerrado | 1.2 |
| 46140be0-04b8-3529-8143-0bb5b5bdc853 | -8.23057 | -46.24881 | 2025-11-01 05:08:00 | NPP-375D | BALSAS | MARANHÃO | Brasil | 2101400 | 21 | 33 | nan | nan | nan | Cerrado | 2.8 |
| b20d202d-04ba-3f84-b728-f7d6b14035b8 | -3.87929 | -51.19351 | 2025-11-01 05:08:00 | NPP-375D | PACAJÁ | PARÁ | Brasil | 1505486 | 15 | 33 | nan | nan | nan | Amazônia | 0.7 |
| 95e41c47-8b28-35bf-a50f-742d42b52801 | -10.62833 | -52.17753 | 2025-11-01 05:08:00 | NPP-375D | PORTO ALEGRE DO NORTE | MATO GROSSO | Brasil | 5106778 | 51 | 33 | nan | nan | nan | Amazônia | 1.6 |
| b4ad59f1-3a79-3ca8-ac14-36f1e8399486 | -10.62298 | -52.18704 | 2025-11-01 05:08:00 | NPP-375D | PORTO ALEGRE DO NORTE | MATO GROSSO | Brasil | 5106778 | 51 | 33 | nan | nan | nan | Amazônia | 3.8 |
| a0aaaec6-1774-3d9e-bacd-55baa47dac02 | -5.18981 | -44.91338 | 2025-11-01 05:08:00 | NPP-375D | BARRA DO CORDA | MARANHÃO | Brasil | 2101608 | 21 | 33 | nan | nan | nan | Cerrado | 1.1 |
| 95f64971-63b0-3c35-a3bd-0317f516ee8e | -10.40942 | -44.34842 | 2025-11-01 05:08:00 | NPP-375D | PARNAGUÁ | PIAUÍ | Brasil | 2207603 | 22 | 33 | nan | nan | nan | Cerrado | 3.5 |
| 7d1d85f8-e230-3e8e-aaf8-95520a2cbfa9 | -10.63227 | -52.17812 | 2025-11-01 05:08:00 | NPP-375D | PORTO ALEGRE DO NORTE | MATO GROSSO | Brasil | 5106778 | 51 | 33 | nan | nan | nan | Amazônia | 1.4 |
| 3b643bbc-9451-3c89-97ad-2fb3084647c1 | -4.54671 | -45.79894 | 2025-11-01 05:08:00 | NPP-375D | SANTA LUZIA | MARANHÃO | Brasil | 2110005 | 21 | 33 | nan | nan | nan | Amazônia | 1.4 |
| 25dfc6a8-73aa-35b8-ae6f-faa9331cd4e4 | -5.12168 | -43.39209 | 2025-11-01 05:08:00 | NPP-375D | CAXIAS | MARANHÃO | Brasil | 2103000 | 21 | 33 | nan | nan | nan | Cerrado | 1.2 |
| 363ea985-9d3c-30f3-9163-2281806fb732 | -5.83366 | -44.06681 | 2025-11-01 05:08:00 | NPP-375D | BURITI BRAVO | MARANHÃO | Brasil | 2102309 | 21 | 33 | nan | nan | nan | Cerrado | 8.6 |
| f5214c60-7ba6-3020-b884-8acee311aab2 | -3.8106 | -51.69881 | 2025-11-01 05:08:00 | NPP-375D | SENADOR JOSÉ PORFÍRIO | PARÁ | Brasil | 1507805 | 15 | 33 | nan | nan | nan | Amazônia | 1.3 |
| c56be9c4-46c8-3ae8-b204-854a7b8d8b10 | -5.25635 | -45.60831 | 2025-11-01 05:08:00 | NPP-375D | JENIPAPO DOS VIEIRAS | MARANHÃO | Brasil | 2105476 | 21 | 33 | nan | nan | nan | Cerrado | 0.6 |
| 05006c20-edcc-3bd3-9deb-458f29db5cf6 | -3.57395 | -50.26527 | 2025-11-01 05:08:00 | NPP-375D | PACAJÁ | PARÁ | Brasil | 1505486 | 15 | 33 | nan | nan | nan | Amazônia | 1.7 |
| 1701e1cd-6556-3193-87ea-1b5a8843e81a | -3.66021 | -50.19283 | 2025-11-01 05:08:00 | NPP-375D | PACAJÁ | PARÁ | Brasil | 1505486 | 15 | 33 | nan | nan | nan | Amazônia | 0.7 |
| 0f01a8be-52b0-39e6-8b57-b284b6960792 | -3.37085 | -51.57631 | 2025-11-01 05:08:00 | NPP-375D | ANAPU | PARÁ | Brasil | 1500859 | 15 | 33 | nan | nan | nan | Amazônia | 1.3 |
| fee64a8a-bf22-3207-870a-3dd3eebef467 | -4.55226 | -45.79974 | 2025-11-01 05:08:00 | NPP-375D | SANTA LUZIA | MARANHÃO | Brasil | 2110005 | 21 | 33 | nan | nan | nan | Amazônia | 1.4 |
| c052d34e-d180-30a1-8698-3e8fc2d8a2be | -8.1208 | -55.31313 | 2025-11-01 05:08:00 | NPP-375D | NOVO PROGRESSO | PARÁ | Brasil | 1505031 | 15 | 33 | nan | nan | nan | Amazônia | 1.0 |
| c12835eb-5290-30de-8347-d80f8c929fff | -6.54246 | -55.04891 | 2025-11-01 05:08:00 | NPP-375D | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 1.2 |
| f78a1e3d-e50b-321c-8138-29ce7a54756b | -10.40474 | -44.33173 | 2025-11-01 05:08:00 | NPP-375D | PARNAGUÁ | PIAUÍ | Brasil | 2207603 | 22 | 33 | nan | nan | nan | Cerrado | 2.4 |
| 6c9d1e2a-29d8-3e8b-ab5a-0cf2af7e6681 | -6.88549 | -42.85033 | 2025-11-01 05:08:00 | NPP-375D | FLORIANO | PIAUÍ | Brasil | 2203909 | 22 | 33 | nan | nan | nan | Caatinga | 5.8 |
| bde283ad-0de3-3db2-a32b-44b0635638b9 | -3.98163 | -48.90861 | 2025-11-01 05:08:00 | NPP-375D | GOIANÉSIA DO PARÁ | PARÁ | Brasil | 1503093 | 15 | 33 | nan | nan | nan | Amazônia | 3.6 |
| c634c3b7-ba25-356e-b8ff-4205bc3809df | -5.83572 | -44.05208 | 2025-11-01 05:08:00 | NPP-375D | BURITI BRAVO | MARANHÃO | Brasil | 2102309 | 21 | 33 | nan | nan | nan | Cerrado | 1.7 |
| d9012829-04fe-3e9b-b968-a229cc6c4753 | -4.91685 | -45.5922 | 2025-11-01 05:08:00 | NPP-375D | ARAME | MARANHÃO | Brasil | 2100956 | 21 | 33 | nan | nan | nan | Amazônia | 2.7 |


[Clique aqui para ver as próximas entradas](README27.md)
