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

## Dados Diários - Página 94

| ID | Latitude | Longitude | Data/Hora GMT | Satélite | Município | Estado | País | Município ID | Estado ID | País ID | Dias sem Chuva | Precipitação | Risco de Fogo | Bioma | FRP |
|----|----------|-----------|---------------|----------|-----------|--------|------|--------------|-----------|---------|----------------|--------------|----------------|-------|-----|
| 03bd735d-a105-30ef-b8f4-518812bb5a91 | -5.5756 | -42.3157 | 2026-09-24 14:00:00 | GOES-19 | BENEDITINOS | PIAUÍ | Brasil | 2201606 | 22 | 33 | nan | nan | nan | Caatinga | 137.6 |
| 0ae90019-a1e6-3658-a488-5079d5f77180 | -8.3761 | -47.3023 | 2026-09-24 14:00:00 | GOES-19 | GOIATINS | TOCANTINS | Brasil | 1709005 | 17 | 33 | nan | nan | nan | Cerrado | 342.0 |
| 93b22242-646e-34ab-a466-62e5a66275a5 | -6.9686 | -47.468 | 2026-09-24 14:00:00 | GOES-19 | CAROLINA | MARANHÃO | Brasil | 2102804 | 21 | 33 | nan | nan | nan | Cerrado | 64.4 |
| 2ee71a59-d545-3631-8fbb-5e566792a2c5 | -6.2038 | -43.3475 | 2026-09-24 14:00:00 | GOES-19 | LAGOA DO MATO | MARANHÃO | Brasil | 2105922 | 21 | 33 | nan | nan | nan | Cerrado | 65.4 |
| 8a18a6d7-fd6a-3281-8b1f-dba3a7d4ed4f | -6.6815 | -55.0703 | 2026-09-24 14:00:00 | GOES-19 | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 74.7 |
| 4880dd71-c96e-3ea9-b2ed-99758c8af1a3 | -9.0158 | -60.5138 | 2026-09-24 14:00:00 | GOES-19 | COLNIZA | MATO GROSSO | Brasil | 5103254 | 51 | 33 | nan | nan | nan | Amazônia | 56.6 |
| 997d4823-e2e8-3236-9360-78c993431ac8 | -5.6016 | -60.211 | 2026-09-24 14:00:00 | GOES-19 | NOVO ARIPUANÃ | AMAZONAS | Brasil | 1303304 | 13 | 33 | nan | nan | nan | Amazônia | 73.2 |
| 788efd5f-9c90-314f-b281-9a8a668bc185 | -6.9416 | -42.8834 | 2026-09-24 14:00:00 | GOES-19 | FLORIANO | PIAUÍ | Brasil | 2203909 | 22 | 33 | nan | nan | nan | Caatinga | 73.1 |
| 054c0fce-c6ed-3f8c-a839-b31b70d7c4b0 | -6.185 | -43.3491 | 2026-09-24 14:00:00 | GOES-19 | LAGOA DO MATO | MARANHÃO | Brasil | 2105922 | 21 | 33 | nan | nan | nan | Cerrado | 65.6 |
| 22912e0c-fdbf-368a-8330-9dd1c1edcfb7 | -13.2249 | -51.5679 | 2026-09-24 14:00:00 | GOES-19 | RIBEIRÃO CASCALHEIRA | MATO GROSSO | Brasil | 5107180 | 51 | 33 | nan | nan | nan | Cerrado | 88.1 |
| 72190554-3916-38c5-b065-bc4a606bcc7f | -8.6817 | -45.4359 | 2026-09-24 14:00:00 | GOES-19 | SANTA FILOMENA | PIAUÍ | Brasil | 2209203 | 22 | 33 | nan | nan | nan | Cerrado | 65.3 |
| fa418a1a-a4b3-3466-b8fe-cbe9ef2dfca7 | -13.2061 | -51.549 | 2026-09-24 14:00:00 | GOES-19 | RIBEIRÃO CASCALHEIRA | MATO GROSSO | Brasil | 5107180 | 51 | 33 | nan | nan | nan | Cerrado | 69.0 |
| 3901c659-a33f-33cd-bc11-8d258e7bdbe1 | -3.5467 | -43.4735 | 2026-09-24 14:00:00 | GOES-19 | CHAPADINHA | MARANHÃO | Brasil | 2103208 | 21 | 33 | nan | nan | nan | Cerrado | 74.5 |
| bc24cd5d-fdc7-3d37-bfd4-fae921defb72 | -9.6108 | -43.9477 | 2026-09-24 14:00:00 | GOES-19 | MORRO CABEÇA NO TEMPO | PIAUÍ | Brasil | 2206654 | 22 | 33 | nan | nan | nan | Caatinga | 89.5 |
| 43c687be-9dfe-37f8-bb45-d62ce80a6a5d | -5.6016 | -60.1919 | 2026-09-24 14:00:00 | GOES-19 | NOVO ARIPUANÃ | AMAZONAS | Brasil | 1303304 | 13 | 33 | nan | nan | nan | Amazônia | 116.0 |
| 03562de8-0f91-37eb-8743-b6c8dbb990aa | -8.3022 | -44.1467 | 2026-09-24 14:00:00 | GOES-19 | MANOEL EMÍDIO | PIAUÍ | Brasil | 2205904 | 22 | 33 | nan | nan | nan | Cerrado | 88.7 |
| 304a95aa-5053-367e-9897-4becadbd58cf | -8.7003 | -45.4567 | 2026-09-24 14:00:00 | GOES-19 | SANTA FILOMENA | PIAUÍ | Brasil | 2209203 | 22 | 33 | nan | nan | nan | Cerrado | 64.0 |
| b77aa10b-9a22-3289-abe7-30ddabef1cc0 | -8.3764 | -47.2802 | 2026-09-24 14:00:00 | GOES-19 | GOIATINS | TOCANTINS | Brasil | 1709005 | 17 | 33 | nan | nan | nan | Cerrado | 184.8 |
| 21a27ab1-3d95-32eb-854d-5e5b87fd7926 | -13.2057 | -51.5703 | 2026-09-24 14:00:00 | GOES-19 | RIBEIRÃO CASCALHEIRA | MATO GROSSO | Brasil | 5107180 | 51 | 33 | nan | nan | nan | Cerrado | 102.5 |
| 041a67c6-1067-351e-b459-1206af55615f | -13.1872 | -51.53 | 2026-09-24 14:00:00 | GOES-19 | RIBEIRÃO CASCALHEIRA | MATO GROSSO | Brasil | 5107180 | 51 | 33 | nan | nan | nan | Cerrado | 93.8 |
| eb810369-7c29-3382-a52a-8f9366ffbced | -13.168 | -51.5324 | 2026-09-24 14:00:00 | GOES-19 | RIBEIRÃO CASCALHEIRA | MATO GROSSO | Brasil | 5107180 | 51 | 33 | nan | nan | nan | Cerrado | 108.6 |
| c833df08-7227-32d3-9452-9f6ab0525b9b | -3.9169 | -59.6641 | 2026-09-24 14:00:00 | GOES-19 | AUTAZES | AMAZONAS | Brasil | 1300300 | 13 | 33 | nan | nan | nan | Amazônia | 100.5 |
| 0cd19f33-3d12-39cb-a69c-98b2490b8d35 | -6.9416 | -42.8834 | 2026-09-24 14:10:00 | GOES-19 | FLORIANO | PIAUÍ | Brasil | 2203909 | 22 | 33 | nan | nan | nan | Caatinga | 67.6 |
| 826e038a-adb5-3c24-b105-59dbe03c801a | -11.1358 | -42.7914 | 2026-09-24 14:10:00 | GOES-19 | GENTIO DO OURO | BAHIA | Brasil | 2911303 | 29 | 33 | nan | nan | nan | Caatinga | 118.6 |
| b1e0d846-17f9-3412-8c67-3302858a0bf4 | -5.9152 | -59.933 | 2026-09-24 14:10:00 | GOES-19 | NOVO ARIPUANÃ | AMAZONAS | Brasil | 1303304 | 13 | 33 | nan | nan | nan | Amazônia | 64.9 |
| 163b34b9-32c9-34bf-a3f6-5f9bce884b8f | -13.1872 | -51.53 | 2026-09-24 14:10:00 | GOES-19 | RIBEIRÃO CASCALHEIRA | MATO GROSSO | Brasil | 5107180 | 51 | 33 | nan | nan | nan | Cerrado | 94.3 |
| 2db1088c-0011-3068-91f4-6e2fff809cd7 | -7.4092 | -44.7885 | 2026-09-24 14:10:00 | GOES-19 | URUÇUÍ | PIAUÍ | Brasil | 2211209 | 22 | 33 | nan | nan | nan | Cerrado | 71.6 |
| d4a780af-71be-3655-a021-1abd4046d796 | -10.8567 | -57.1767 | 2026-09-24 14:10:00 | GOES-19 | JUARA | MATO GROSSO | Brasil | 5105101 | 51 | 33 | nan | nan | nan | Amazônia | 53.3 |
| 39b63bcf-eaff-3880-aec2-4f18495861a6 | -13.1677 | -51.5537 | 2026-09-24 14:10:00 | GOES-19 | RIBEIRÃO CASCALHEIRA | MATO GROSSO | Brasil | 5107180 | 51 | 33 | nan | nan | nan | Cerrado | 85.5 |
| 068ad3cb-af98-3fef-841a-ebe75d5e4f50 | -7.6765 | -46.0771 | 2026-09-24 14:10:00 | GOES-19 | BALSAS | MARANHÃO | Brasil | 2101400 | 21 | 33 | nan | nan | nan | Cerrado | 80.3 |
| 929c4977-53c9-3be9-a8ae-48b3a453491c | -6.9683 | -47.4899 | 2026-09-24 14:10:00 | GOES-19 | CAROLINA | MARANHÃO | Brasil | 2102804 | 21 | 33 | nan | nan | nan | Cerrado | 77.9 |
| 443475c1-09aa-3a0a-8e40-00e28d6b621b | -6.2038 | -43.3475 | 2026-09-24 14:10:00 | GOES-19 | LAGOA DO MATO | MARANHÃO | Brasil | 2105922 | 21 | 33 | nan | nan | nan | Cerrado | 127.8 |
| cd92468c-e0f5-3147-97a7-e252432061e3 | -12.0096 | -52.4675 | 2026-09-24 14:10:00 | GOES-19 | QUERÊNCIA | MATO GROSSO | Brasil | 5107065 | 51 | 33 | nan | nan | nan | Amazônia | 84.4 |
| f0d32cb5-7075-32da-9ed0-077bb92c170f | -8.9016 | -45.933 | 2026-09-24 14:10:00 | GOES-19 | SANTA FILOMENA | PIAUÍ | Brasil | 2209203 | 22 | 33 | nan | nan | nan | Cerrado | 73.6 |
| 22be4d1f-c132-367e-88f2-41b5dcdcf7e0 | -9.275 | -46.2527 | 2026-09-24 14:10:00 | GOES-19 | ALTO PARNAÍBA | MARANHÃO | Brasil | 2100501 | 21 | 33 | nan | nan | nan | Cerrado | 72.1 |
| 75ce3da4-c04a-37cb-8ef7-2524f0c48f30 | -13.2057 | -51.5703 | 2026-09-24 14:10:00 | GOES-19 | RIBEIRÃO CASCALHEIRA | MATO GROSSO | Brasil | 5107180 | 51 | 33 | nan | nan | nan | Cerrado | 88.5 |
| 330762c7-be1c-3597-8f51-46632d2e8b9a | -11.1733 | -42.8335 | 2026-09-24 14:10:00 | GOES-19 | GENTIO DO OURO | BAHIA | Brasil | 2911303 | 29 | 33 | nan | nan | nan | Caatinga | 115.5 |
| 0af5f452-3df0-30b1-9355-d1d782727229 | -6.4414 | -55.0024 | 2026-09-24 14:10:00 | GOES-19 | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 60.9 |
| fb5b374e-ca7a-3126-a979-9c46319b76f0 | -13.168 | -51.5324 | 2026-09-24 14:10:00 | GOES-19 | RIBEIRÃO CASCALHEIRA | MATO GROSSO | Brasil | 5107180 | 51 | 33 | nan | nan | nan | Cerrado | 140.6 |
| babe47dd-2e9f-3c83-b4c1-b7d395621225 | -9.6111 | -43.9243 | 2026-09-24 14:10:00 | GOES-19 | MORRO CABEÇA NO TEMPO | PIAUÍ | Brasil | 2206654 | 22 | 33 | nan | nan | nan | Caatinga | 117.9 |
| 3dcc5f2f-a0e2-3349-833c-363f3827bf29 | -7.7629 | -46.7389 | 2026-09-24 14:10:00 | GOES-19 | RIACHÃO | MARANHÃO | Brasil | 2109502 | 21 | 33 | nan | nan | nan | Cerrado | 81.8 |
| 0bb1f0c4-646e-3daa-a5e3-cb563d75bf6d | -8.8261 | -45.9411 | 2026-09-24 14:10:00 | GOES-19 | SANTA FILOMENA | PIAUÍ | Brasil | 2209203 | 22 | 33 | nan | nan | nan | Cerrado | 78.7 |
| 6d8bafc8-5c51-33d1-ac5a-eecc1a4d4bff | -11.155 | -42.7885 | 2026-09-24 14:10:00 | GOES-19 | GENTIO DO OURO | BAHIA | Brasil | 2911303 | 29 | 33 | nan | nan | nan | Caatinga | 110.3 |
| 832bbda4-1fa1-3fb2-bcb9-88d3392493af | -7.1088 | -43.0792 | 2026-09-24 14:10:00 | GOES-19 | FLORIANO | PIAUÍ | Brasil | 2203909 | 22 | 33 | nan | nan | nan | Caatinga | 76.0 |
| 7bc03dca-6c12-3250-b5b6-b863636ed736 | -9.0158 | -60.5138 | 2026-09-24 14:10:00 | GOES-19 | COLNIZA | MATO GROSSO | Brasil | 5103254 | 51 | 33 | nan | nan | nan | Amazônia | 79.9 |
| 0d29d7e0-1caa-3d10-9f00-552309a9749f | -5.6016 | -60.1919 | 2026-09-24 14:10:00 | GOES-19 | NOVO ARIPUANÃ | AMAZONAS | Brasil | 1303304 | 13 | 33 | nan | nan | nan | Amazônia | 140.8 |
| 02e60d67-2ad5-3f08-9891-24daf0a3449d | -6.9225 | -42.9088 | 2026-09-24 14:10:00 | GOES-19 | FLORIANO | PIAUÍ | Brasil | 2203909 | 22 | 33 | nan | nan | nan | Caatinga | 71.2 |
| 58f7f642-3018-302b-9969-fb1e85176338 | -9.2563 | -46.2323 | 2026-09-24 14:10:00 | GOES-19 | ALTO PARNAÍBA | MARANHÃO | Brasil | 2100501 | 21 | 33 | nan | nan | nan | Cerrado | 72.3 |
| 1ce31b57-86f2-3843-b869-4a02d28397c7 | -7.6196 | -46.1271 | 2026-09-24 14:10:00 | GOES-19 | BALSAS | MARANHÃO | Brasil | 2101400 | 21 | 33 | nan | nan | nan | Cerrado | 67.7 |
| 630cd0f9-cbfc-3b38-bb0a-74576d7dc4b0 | -6.185 | -43.3491 | 2026-09-24 14:10:00 | GOES-19 | LAGOA DO MATO | MARANHÃO | Brasil | 2105922 | 21 | 33 | nan | nan | nan | Cerrado | 74.1 |
| 88d8dc1d-4110-352e-9214-db873595c275 | -9.256 | -46.2548 | 2026-09-24 14:10:00 | GOES-19 | ALTO PARNAÍBA | MARANHÃO | Brasil | 2100501 | 21 | 33 | nan | nan | nan | Cerrado | 72.7 |
| 5ee91396-bf28-3907-bb3c-7e6c5b670a89 | -6.6816 | -55.0502 | 2026-09-24 14:10:00 | GOES-19 | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 99.3 |
| 9517b896-936a-3e97-8e68-529afe90a532 | -11.7162 | -54.5654 | 2026-09-24 14:10:00 | GOES-19 | UNIÃO DO SUL | MATO GROSSO | Brasil | 5108303 | 51 | 33 | nan | nan | nan | Amazônia | 58.2 |
| 62a25907-97d5-3a11-b28d-5069223c60d7 | -8.9394 | -45.929 | 2026-09-24 14:10:00 | GOES-19 | SANTA FILOMENA | PIAUÍ | Brasil | 2209203 | 22 | 33 | nan | nan | nan | Cerrado | 67.2 |
| 0efd6b69-5abc-3b50-8558-52a851120960 | -11.1541 | -42.8364 | 2026-09-24 14:10:00 | GOES-19 | XIQUE-XIQUE | BAHIA | Brasil | 2933604 | 29 | 33 | nan | nan | nan | Caatinga | 104.2 |
| 464dcb57-2464-3c13-8288-50907c009a3a | -6.2026 | -47.5026 | 2026-09-24 14:10:00 | GOES-19 | TOCANTINÓPOLIS | TOCANTINS | Brasil | 1721208 | 17 | 33 | nan | nan | nan | Cerrado | 63.3 |
| f9bcdcea-1feb-38bf-b8f0-660400c1ab48 | -13.7993 | -54.0617 | 2026-09-24 14:10:00 | GOES-19 | GAÚCHA DO NORTE | MATO GROSSO | Brasil | 5103858 | 51 | 33 | nan | nan | nan | Cerrado | 74.5 |
| 7ca2d273-ff4f-3255-ac1a-570096bbee74 | -8.8827 | -45.935 | 2026-09-24 14:10:00 | GOES-19 | SANTA FILOMENA | PIAUÍ | Brasil | 2209203 | 22 | 33 | nan | nan | nan | Cerrado | 76.1 |
| b03cf22b-5d79-38e2-a531-3941bcfec20d | -7.7444 | -46.7184 | 2026-09-24 14:10:00 | GOES-19 | RIACHÃO | MARANHÃO | Brasil | 2109502 | 21 | 33 | nan | nan | nan | Cerrado | 69.5 |
| 8d5253c4-a74c-3c51-8291-0ebefa52ad09 | -13.2249 | -51.5679 | 2026-09-24 14:10:00 | GOES-19 | RIBEIRÃO CASCALHEIRA | MATO GROSSO | Brasil | 5107180 | 51 | 33 | nan | nan | nan | Cerrado | 87.9 |
| 1321dcad-cc30-3b0a-bb62-cd26d6275801 | -5.5756 | -42.3157 | 2026-09-24 14:10:00 | GOES-19 | BENEDITINOS | PIAUÍ | Brasil | 2201606 | 22 | 33 | nan | nan | nan | Caatinga | 149.3 |
| bfa03f65-6ac9-3823-9e28-37b8f2c1b5a3 | -3.4635 | -58.3096 | 2026-09-24 14:10:00 | GOES-19 | ITACOATIARA | AMAZONAS | Brasil | 1301902 | 13 | 33 | nan | nan | nan | Amazônia | 78.8 |
| 22865c2e-2af7-3073-9a72-cc9e50f8c09c | -6.8817 | -55.5592 | 2026-09-24 14:10:00 | GOES-19 | NOVO PROGRESSO | PARÁ | Brasil | 1505031 | 15 | 33 | nan | nan | nan | Amazônia | 62.2 |
| a6edcfca-c329-314a-9a53-3a36054b2364 | -9.0273 | -45.0105 | 2026-09-24 14:10:00 | GOES-19 | CURRAIS | PIAUÍ | Brasil | 2203230 | 22 | 33 | nan | nan | nan | Cerrado | 68.0 |
| 9654f639-fbd0-39e8-a187-d067f0a42659 | -17.7756 | -46.6272 | 2026-09-24 14:10:00 | GOES-19 | LAGAMAR | MINAS GERAIS | Brasil | 3137106 | 31 | 33 | nan | nan | nan | Cerrado | 63.3 |
| 03cb812a-0539-3370-ba21-cf2949c4a6d0 | -5.5833 | -60.1924 | 2026-09-24 14:10:00 | GOES-19 | NOVO ARIPUANÃ | AMAZONAS | Brasil | 1303304 | 13 | 33 | nan | nan | nan | Amazônia | 69.9 |
| a39efd55-3ca5-3857-8843-fad23c846bbb | -10.08 | -50.21 | 2026-09-24 14:15:00 | MSG-03 | PIUM | TOCANTINS | Brasil | 1717503 | 17 | 33 | nan | nan | nan | Cerrado | nan |
| a91823ec-ce72-38ad-82b0-597d92ac1d66 | -9.64 | -43.95 | 2026-09-24 14:15:00 | MSG-03 | MORRO CABEÇA NO TEMPO | PIAUÍ | Brasil | 2206654 | 22 | 33 | nan | nan | nan | Caatinga | nan |
| 520b103e-8e9f-35c9-91f3-6886f176ec6b | -11.68 | -43.45 | 2026-09-24 14:15:00 | MSG-03 | BARRA | BAHIA | Brasil | 2902708 | 29 | 33 | nan | nan | nan | Cerrado | nan |
| 442c7697-a3f8-31d8-b453-0bfe86bd7843 | -11.43 | -44.17 | 2026-09-24 14:15:00 | MSG-03 | MANSIDÃO | BAHIA | Brasil | 2920452 | 29 | 33 | nan | nan | nan | Cerrado | nan |
| 4865d985-6abe-36e4-839d-6cb8ea024711 | -11.46 | -44.18 | 2026-09-24 14:15:00 | MSG-03 | COTEGIPE | BAHIA | Brasil | 2909406 | 29 | 33 | nan | nan | nan | Cerrado | nan |
| 905fa58d-656c-3447-b3f4-d67efd43e01d | -11.44 | -44.22 | 2026-09-24 14:15:00 | MSG-03 | MANSIDÃO | BAHIA | Brasil | 2920452 | 29 | 33 | nan | nan | nan | Cerrado | nan |
| 035c03b3-789d-3ec6-9523-8d9bc532dcd0 | -11.65 | -43.49 | 2026-09-24 14:15:00 | MSG-03 | BARRA | BAHIA | Brasil | 2902708 | 29 | 33 | nan | nan | nan | Cerrado | nan |
| ccd36dd2-a37f-3603-99b0-8fe2be816eaf | -11.68 | -43.41 | 2026-09-24 14:15:00 | MSG-03 | BARRA | BAHIA | Brasil | 2902708 | 29 | 33 | nan | nan | nan | Cerrado | nan |
| f021a291-a58c-3e0d-a447-b30532efd28f | -11.47 | -44.22 | 2026-09-24 14:15:00 | MSG-03 | COTEGIPE | BAHIA | Brasil | 2909406 | 29 | 33 | nan | nan | nan | Cerrado | nan |
| 789404d3-e6e6-3bbb-b689-97110919e04f | -7.5086 | -44.3201 | 2026-09-24 14:20:00 | GOES-19 | URUÇUÍ | PIAUÍ | Brasil | 2211209 | 22 | 33 | nan | nan | nan | Cerrado | 68.8 |
| 2d476f57-9886-3513-a608-f15ea8e3520a | -6.9223 | -42.9323 | 2026-09-24 14:20:00 | GOES-19 | FLORIANO | PIAUÍ | Brasil | 2203909 | 22 | 33 | nan | nan | nan | Caatinga | 75.5 |
| a102350f-d4c8-3d00-b68b-80a6d06b10fa | -6.9029 | -46.5456 | 2026-09-24 14:20:00 | GOES-19 | FEIRA NOVA DO MARANHÃO | MARANHÃO | Brasil | 2104073 | 21 | 33 | nan | nan | nan | Cerrado | 66.3 |
| 087c792f-9d05-3ca1-82cc-8d4dd1bc0e62 | -11.7165 | -54.5449 | 2026-09-24 14:20:00 | GOES-19 | UNIÃO DO SUL | MATO GROSSO | Brasil | 5108303 | 51 | 33 | nan | nan | nan | Amazônia | 62.1 |
| 2178584b-c5b0-3790-adaf-0c8571b435c9 | -6.2038 | -43.3475 | 2026-09-24 14:20:00 | GOES-19 | LAGOA DO MATO | MARANHÃO | Brasil | 2105922 | 21 | 33 | nan | nan | nan | Cerrado | 77.5 |
| 3599116a-12f0-3bb7-829d-bb9d371fcddb | -10.8567 | -57.1767 | 2026-09-24 14:20:00 | GOES-19 | JUARA | MATO GROSSO | Brasil | 5105101 | 51 | 33 | nan | nan | nan | Amazônia | 62.8 |
| 59507eb1-cbb2-3b0e-903c-145f76b1d738 | -6.8985 | -41.6976 | 2026-09-24 14:20:00 | GOES-19 | IPIRANGA DO PIAUÍ | PIAUÍ | Brasil | 2204808 | 22 | 33 | nan | nan | nan | Caatinga | 83.4 |
| 78480160-9e08-39fb-903c-24b8a85c9940 | -5.5756 | -42.3157 | 2026-09-24 14:20:00 | GOES-19 | BENEDITINOS | PIAUÍ | Brasil | 2201606 | 22 | 33 | nan | nan | nan | Caatinga | 167.9 |
| cda56b77-65ef-3721-bc05-01b36e8a75d5 | -6.9414 | -42.907 | 2026-09-24 14:20:00 | GOES-19 | FLORIANO | PIAUÍ | Brasil | 2203909 | 22 | 33 | nan | nan | nan | Caatinga | 69.2 |
| 88f04471-c3e3-3438-8eaa-3ceaa6af84fa | -6.9683 | -47.4899 | 2026-09-24 14:20:00 | GOES-19 | CAROLINA | MARANHÃO | Brasil | 2102804 | 21 | 33 | nan | nan | nan | Cerrado | 79.8 |
| 79c3e68f-e7e1-3980-90a8-c6a9c04a0ee6 | -7.3659 | -42.058 | 2026-09-24 14:20:00 | GOES-19 | COLÔNIA DO PIAUÍ | PIAUÍ | Brasil | 2202778 | 22 | 33 | nan | nan | nan | Caatinga | 63.6 |
| 044c3ad5-4a59-306a-bb0d-9404b4c6bb83 | -11.9906 | -52.4695 | 2026-09-24 14:20:00 | GOES-19 | QUERÊNCIA | MATO GROSSO | Brasil | 5107065 | 51 | 33 | nan | nan | nan | Amazônia | 62.1 |
| 42c9ad88-d057-38d8-9096-ed0a91b1ab76 | -10.8569 | -57.1568 | 2026-09-24 14:20:00 | GOES-19 | JUARA | MATO GROSSO | Brasil | 5105101 | 51 | 33 | nan | nan | nan | Amazônia | 58.6 |
| 973fc13b-0430-3f1f-9984-8051452bdf0d | -8.4831 | -44.7495 | 2026-09-24 14:20:00 | GOES-19 | PALMEIRA DO PIAUÍ | PIAUÍ | Brasil | 2207405 | 22 | 33 | nan | nan | nan | Cerrado | 59.4 |
| b313fd43-31ba-3c75-b844-637791834d1a | -13.2249 | -51.5679 | 2026-09-24 14:20:00 | GOES-19 | RIBEIRÃO CASCALHEIRA | MATO GROSSO | Brasil | 5107180 | 51 | 33 | nan | nan | nan | Cerrado | 89.4 |
| 1b4f081d-af9e-3cdf-922f-28c41d3a531e | -7.7629 | -46.7389 | 2026-09-24 14:20:00 | GOES-19 | RIACHÃO | MARANHÃO | Brasil | 2109502 | 21 | 33 | nan | nan | nan | Cerrado | 86.2 |
| 4d4daf58-c0fa-3002-8a7a-22e7630243b8 | -5.1948 | -42.9805 | 2026-09-24 14:20:00 | GOES-19 | TIMON | MARANHÃO | Brasil | 2112209 | 21 | 33 | nan | nan | nan | Caatinga | 72.2 |
| 8bace65a-ddf0-361d-a10b-3c6740323eaf | -6.9225 | -42.9088 | 2026-09-24 14:20:00 | GOES-19 | FLORIANO | PIAUÍ | Brasil | 2203909 | 22 | 33 | nan | nan | nan | Caatinga | 72.5 |
| 5ed53300-acd5-3342-a7ef-913170f68fa8 | -6.1653 | -47.5052 | 2026-09-24 14:20:00 | GOES-19 | TOCANTINÓPOLIS | TOCANTINS | Brasil | 1721208 | 17 | 33 | nan | nan | nan | Cerrado | 66.1 |
| 0c97a59a-33c9-361b-a702-dcc2cb524f35 | -3.4791 | -59.1948 | 2026-09-24 14:20:00 | GOES-19 | AUTAZES | AMAZONAS | Brasil | 1300300 | 13 | 33 | nan | nan | nan | Amazônia | 81.4 |
| 2c754569-a767-3054-942e-ccaed616bbe1 | -13.2057 | -51.5703 | 2026-09-24 14:20:00 | GOES-19 | RIBEIRÃO CASCALHEIRA | MATO GROSSO | Brasil | 5107180 | 51 | 33 | nan | nan | nan | Cerrado | 88.7 |
| 5136125f-0146-3eab-b898-2551300fe56c | -8.0486 | -44.8178 | 2026-09-24 14:20:00 | GOES-19 | URUÇUÍ | PIAUÍ | Brasil | 2211209 | 22 | 33 | nan | nan | nan | Cerrado | 65.2 |
| 6b02a4a5-d6c4-30a8-a5c5-e723463d1153 | -9.0344 | -60.5129 | 2026-09-24 14:20:00 | GOES-19 | COLNIZA | MATO GROSSO | Brasil | 5103254 | 51 | 33 | nan | nan | nan | Amazônia | 52.7 |
| 16e58cd8-9116-36ee-8fcf-6ed1dc5c537d | -9.6111 | -43.9243 | 2026-09-24 14:20:00 | GOES-19 | MORRO CABEÇA NO TEMPO | PIAUÍ | Brasil | 2206654 | 22 | 33 | nan | nan | nan | Caatinga | 146.5 |
| faf663ff-ba40-3fb8-859f-cac0688123cb | -6.2026 | -47.5026 | 2026-09-24 14:20:00 | GOES-19 | TOCANTINÓPOLIS | TOCANTINS | Brasil | 1721208 | 17 | 33 | nan | nan | nan | Cerrado | 62.5 |


[Clique aqui para ver as próximas entradas](README95.md)
