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

## Dados Diários - Página 34

| ID | Latitude | Longitude | Data/Hora GMT | Satélite | Município | Estado | País | Município ID | Estado ID | País ID | Dias sem Chuva | Precipitação | Risco de Fogo | Bioma | FRP |
|----|----------|-----------|---------------|----------|-----------|--------|------|--------------|-----------|---------|----------------|--------------|----------------|-------|-----|
| 9d5a41de-29ee-3d1d-9631-0b729dbbab52 | -2.69236 | -51.72868 | 2024-12-01 04:21:00 | NOAA-21 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 4.0 |
| 03f0d264-7685-329e-945b-82b44e333ece | -3.53967 | -51.5046 | 2024-12-01 04:21:00 | NOAA-21 | ANAPU | PARÁ | Brasil | 1500859 | 15 | 33 | nan | nan | nan | Amazônia | 3.0 |
| eec6136b-3c30-3d30-99e2-a33240db650f | -2.5907 | -46.93901 | 2024-12-01 04:21:00 | NOAA-21 | PARAGOMINAS | PARÁ | Brasil | 1505502 | 15 | 33 | nan | nan | nan | Amazônia | 1.3 |
| ffd05e1e-0a13-3539-8728-a9e591dd86d3 | -2.68641 | -51.73124 | 2024-12-01 04:21:00 | NOAA-21 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 4.0 |
| 32742da2-c6c2-3d19-a612-e5f078bed813 | -3.47126 | -50.27119 | 2024-12-01 04:21:00 | NOAA-21 | PACAJÁ | PARÁ | Brasil | 1505486 | 15 | 33 | nan | nan | nan | Amazônia | 11.0 |
| b89da71c-4704-3a51-a59b-7e3900a85e9f | -3.93221 | -46.71958 | 2024-12-01 04:21:00 | NOAA-21 | BOM JARDIM | MARANHÃO | Brasil | 2102002 | 21 | 33 | nan | nan | nan | Amazônia | 1.5 |
| 4517437b-dbe7-302d-89de-d3d00264f239 | -2.99467 | -51.06667 | 2024-12-01 04:21:00 | NOAA-21 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 4.5 |
| 8fedb824-3786-314e-b53f-d04f54e21382 | -2.71391 | -46.12787 | 2024-12-01 04:21:00 | NOAA-21 | CENTRO NOVO DO MARANHÃO | MARANHÃO | Brasil | 2103174 | 21 | 33 | nan | nan | nan | Amazônia | 1.5 |
| 3d334333-b0ba-34b3-98f2-93ccab6abdfd | -3.20843 | -53.12377 | 2024-12-01 04:21:00 | NOAA-21 | MEDICILÂNDIA | PARÁ | Brasil | 1504455 | 15 | 33 | nan | nan | nan | Amazônia | 7.1 |
| f1adf831-22a8-37bd-884c-caeef340b073 | -1.97282 | -46.46737 | 2024-12-01 04:21:00 | NOAA-21 | CACHOEIRA DO PIRIÁ | PARÁ | Brasil | 1501956 | 15 | 33 | nan | nan | nan | Amazônia | 2.5 |
| 64d823a0-968a-36d8-8f27-ce127e955d9a | -2.84054 | -49.88511 | 2024-12-01 04:21:00 | NOAA-21 | BAGRE | PARÁ | Brasil | 1501105 | 15 | 33 | nan | nan | nan | Amazônia | 4.3 |
| 2f676be1-2002-344e-a450-0647f74c4dfb | -3.89173 | -45.00869 | 2024-12-01 04:21:00 | NOAA-21 | PIO XII | MARANHÃO | Brasil | 2108702 | 21 | 33 | nan | nan | nan | Amazônia | 1.4 |
| 9995357b-e917-3d06-8c85-878151e6c9bf | -3.11187 | -53.75674 | 2024-12-01 04:21:00 | NOAA-21 | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | 2.0 |
| 741305c2-dfec-3229-b22e-98f71ce937c6 | -2.88187 | -53.335 | 2024-12-01 04:21:00 | NOAA-21 | MEDICILÂNDIA | PARÁ | Brasil | 1504455 | 15 | 33 | nan | nan | nan | Amazônia | 2.2 |
| 8d117263-15d7-3947-aa8e-7e035dc42b05 | -3.38436 | -50.1142 | 2024-12-01 04:21:00 | NOAA-21 | PACAJÁ | PARÁ | Brasil | 1505486 | 15 | 33 | nan | nan | nan | Amazônia | 1.8 |
| 00648229-7f9b-32de-8398-da323f9e9358 | -3.06798 | -50.32851 | 2024-12-01 04:21:00 | NOAA-21 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 3.0 |
| 93f05b1a-f657-3176-bc44-7ba75b0d99f2 | -2.75331 | -46.0994 | 2024-12-01 04:21:00 | NOAA-21 | CENTRO NOVO DO MARANHÃO | MARANHÃO | Brasil | 2103174 | 21 | 33 | nan | nan | nan | Amazônia | 2.7 |
| f11f760d-840d-394e-b38f-e5e199e36df8 | -2.68592 | -46.285 | 2024-12-01 04:21:00 | NOAA-21 | CENTRO NOVO DO MARANHÃO | MARANHÃO | Brasil | 2103174 | 21 | 33 | nan | nan | nan | Amazônia | 1.2 |
| eead5b0f-7a6a-3ff4-b6ac-1325da5336d1 | -1.43767 | -53.397 | 2024-12-01 04:21:00 | NOAA-21 | ALMEIRIM | PARÁ | Brasil | 1500503 | 15 | 33 | nan | nan | nan | Amazônia | 2.2 |
| 2c361fdc-317e-3dc8-afe2-eaa40b0b8f74 | -1.25775 | -51.78126 | 2024-12-01 04:21:00 | NOAA-21 | GURUPÁ | PARÁ | Brasil | 1503101 | 15 | 33 | nan | nan | nan | Amazônia | 7.4 |
| 7e10dc3b-aacc-35a1-8e8a-e25c0803ace2 | -3.45845 | -44.9301 | 2024-12-01 04:21:00 | NOAA-21 | CAJARI | MARANHÃO | Brasil | 2102507 | 21 | 33 | nan | nan | nan | Amazônia | 1.3 |
| e5dd6b22-56c0-311a-ba9e-9492e4f23357 | -3.99913 | -44.7563 | 2024-12-01 04:21:00 | NOAA-21 | BACABAL | MARANHÃO | Brasil | 2101202 | 21 | 33 | nan | nan | nan | Amazônia | 28.9 |
| 2e3f346f-1699-3222-8c3f-832d310ce756 | -3.9346 | -46.39947 | 2024-12-01 04:21:00 | NOAA-21 | BOM JARDIM | MARANHÃO | Brasil | 2102002 | 21 | 33 | nan | nan | nan | Amazônia | 1.4 |
| 662c1ba3-6aaf-3047-ab07-1e26fc56fe50 | -3.48539 | -50.31931 | 2024-12-01 04:21:00 | NOAA-21 | PACAJÁ | PARÁ | Brasil | 1505486 | 15 | 33 | nan | nan | nan | Amazônia | 7.0 |
| ee38ceae-507a-3373-9e46-90931ddab49a | -1.32962 | -55.84948 | 2024-12-01 04:21:00 | NOAA-21 | ORIXIMINÁ | PARÁ | Brasil | 1505304 | 15 | 33 | nan | nan | nan | Amazônia | 2.5 |
| 9815b3de-72bb-3ff1-b0bd-4fe91f611ddb | -2.52522 | -54.07668 | 2024-12-01 04:21:00 | NOAA-21 | PRAINHA | PARÁ | Brasil | 1506005 | 15 | 33 | nan | nan | nan | Amazônia | 2.5 |
| e8419e39-342a-32d3-b0ec-4abdabdd2e3f | -1.67311 | -52.10042 | 2024-12-01 04:21:00 | NOAA-21 | PORTO DE MOZ | PARÁ | Brasil | 1505908 | 15 | 33 | nan | nan | nan | Amazônia | 3.1 |
| c6aca6c7-087a-386d-a4af-59c0c57bbed2 | -1.64489 | -55.07059 | 2024-12-01 04:21:00 | NOAA-21 | ALENQUER | PARÁ | Brasil | 1500404 | 15 | 33 | nan | nan | nan | Amazônia | 2.5 |
| 64452c07-be70-3010-921d-ba4c414f866f | -6.29276 | -43.84906 | 2024-12-01 04:23:00 | NOAA-21 | SÃO JOÃO DOS PATOS | MARANHÃO | Brasil | 2111102 | 21 | 33 | nan | nan | nan | Cerrado | 5.2 |
| 1156080e-d9dd-3d9a-b452-d99f1cebe178 | -5.31813 | -43.07027 | 2024-12-01 04:23:00 | NOAA-21 | TIMON | MARANHÃO | Brasil | 2112209 | 21 | 33 | nan | nan | nan | Cerrado | 1.3 |
| f1373c1e-3642-3fa9-8ca7-cab3d51942b4 | -3.21761 | -54.17488 | 2024-12-01 04:23:00 | NOAA-21 | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | 2.3 |
| 15f30d1d-f058-3694-98cf-3d466129af4a | -6.79927 | -35.25517 | 2024-12-01 04:23:00 | NOAA-21 | ITAPOROROCA | PARAÍBA | Brasil | 2507101 | 25 | 33 | nan | nan | nan | Caatinga | 2.0 |
| f4f85990-5f42-3948-bffe-cfe879b6090b | -10.65586 | -44.49056 | 2024-12-01 04:23:00 | NOAA-21 | SANTA RITA DE CÁSSIA | BAHIA | Brasil | 2928406 | 29 | 33 | nan | nan | nan | Cerrado | 4.6 |
| 37d45d9e-9956-3efd-b136-20a50e57efaa | -8.83384 | -44.78391 | 2024-12-01 04:23:00 | NOAA-21 | CURRAIS | PIAUÍ | Brasil | 2203230 | 22 | 33 | nan | nan | nan | Cerrado | 1.1 |
| 8c7f21a4-a890-37cd-a389-70da38638bf9 | -3.49991 | -52.12965 | 2024-12-01 04:23:00 | NOAA-21 | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 2.4 |
| ae882086-e068-3721-a84d-ea3d53ee8fad | -3.17913 | -54.33624 | 2024-12-01 04:23:00 | NOAA-21 | MOJUÍ DOS CAMPOS | PARÁ | Brasil | 1504752 | 15 | 33 | nan | nan | nan | Amazônia | 1.7 |
| d35c4844-913e-37e0-81a3-d4275110e1a4 | -3.49474 | -53.83551 | 2024-12-01 04:23:00 | NOAA-21 | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | 4.4 |
| 5c7cb45a-e5fb-3f86-a4f2-f61b5b643e3c | -5.08542 | -49.83354 | 2024-12-01 04:23:00 | NOAA-21 | ITUPIRANGA | PARÁ | Brasil | 1503705 | 15 | 33 | nan | nan | nan | Amazônia | 1.0 |
| 40af0279-8bcd-33f4-82d8-811fa196a7bf | -8.84147 | -44.7564 | 2024-12-01 04:23:00 | NOAA-21 | CURRAIS | PIAUÍ | Brasil | 2203230 | 22 | 33 | nan | nan | nan | Cerrado | 1.7 |
| 9365f631-4d81-3f03-908c-97976d7d3215 | -4.99624 | -50.74221 | 2024-12-01 04:23:00 | NOAA-21 | NOVO REPARTIMENTO | PARÁ | Brasil | 1505064 | 15 | 33 | nan | nan | nan | Amazônia | 1.4 |
| f776986e-a712-3c9e-922c-6202e8f3dcb4 | -3.771 | -51.61858 | 2024-12-01 04:23:00 | NOAA-21 | SENADOR JOSÉ PORFÍRIO | PARÁ | Brasil | 1507805 | 15 | 33 | nan | nan | nan | Amazônia | 3.3 |
| e8d8a5c6-ef47-3092-aa87-abcb1c217269 | -5.18539 | -43.95301 | 2024-12-01 04:23:00 | NOAA-21 | SÃO JOÃO DO SOTER | MARANHÃO | Brasil | 2111078 | 21 | 33 | nan | nan | nan | Cerrado | 1.5 |
| 4ae00805-ca69-304c-abe1-694d74c1c8c7 | -4.55467 | -45.72256 | 2024-12-01 04:23:00 | NOAA-21 | SANTA LUZIA | MARANHÃO | Brasil | 2110005 | 21 | 33 | nan | nan | nan | Amazônia | 23.4 |
| 83eb5787-7d7c-3b1f-8e12-196adbd72301 | -6.30387 | -43.8435 | 2024-12-01 04:23:00 | NOAA-21 | SÃO JOÃO DOS PATOS | MARANHÃO | Brasil | 2111102 | 21 | 33 | nan | nan | nan | Cerrado | 1.2 |
| d90e25b3-c3d1-3542-a391-110cc35e33e3 | -6.00118 | -44.56673 | 2024-12-01 04:23:00 | NOAA-21 | MIRADOR | MARANHÃO | Brasil | 2106706 | 21 | 33 | nan | nan | nan | Cerrado | 1.3 |
| f8bf7f9e-1aa4-3675-8f4a-25efb6cd9767 | -3.30351 | -53.82979 | 2024-12-01 04:23:00 | NOAA-21 | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | 2.3 |
| 3a67c574-c4c2-3f24-9044-84968a558259 | -5.58392 | -45.21512 | 2024-12-01 04:23:00 | NOAA-21 | BARRA DO CORDA | MARANHÃO | Brasil | 2101608 | 21 | 33 | nan | nan | nan | Cerrado | 9.9 |
| 4a6a0c38-02e0-3470-aa46-94ec92ad6862 | -5.50631 | -42.87376 | 2024-12-01 04:23:00 | NOAA-21 | NAZÁRIA | PIAUÍ | Brasil | 2206720 | 22 | 33 | nan | nan | nan | Caatinga | 4.5 |
| 25ce7aa1-3e5b-3976-a73a-ed46df044a9b | -7.54654 | -46.87057 | 2024-12-01 04:23:00 | NOAA-21 | RIACHÃO | MARANHÃO | Brasil | 2109502 | 21 | 33 | nan | nan | nan | Cerrado | 0.5 |
| 5b79e692-59f1-3562-8ce4-367f47ff862d | -4.69412 | -46.80901 | 2024-12-01 04:23:00 | NOAA-21 | BOM JESUS DAS SELVAS | MARANHÃO | Brasil | 2102036 | 21 | 33 | nan | nan | nan | Amazônia | 7.3 |
| 23b3b7f9-bfb2-333a-9fdf-b65d206df307 | -4.19258 | -50.68755 | 2024-12-01 04:23:00 | NOAA-21 | PACAJÁ | PARÁ | Brasil | 1505486 | 15 | 33 | nan | nan | nan | Amazônia | 6.5 |
| defbb1ad-4037-3649-be0f-a13756f0f67f | -10.65977 | -44.48745 | 2024-12-01 04:23:00 | NOAA-21 | SANTA RITA DE CÁSSIA | BAHIA | Brasil | 2928406 | 29 | 33 | nan | nan | nan | Cerrado | 4.6 |
| eb2ef9e7-5405-337b-9f65-af7339a57ef9 | -5.06794 | -46.15863 | 2024-12-01 04:23:00 | NOAA-21 | ARAME | MARANHÃO | Brasil | 2100956 | 21 | 33 | nan | nan | nan | Amazônia | 1.3 |
| af4ae8cf-1923-372e-8572-c818f9b1f497 | -3.26107 | -53.64337 | 2024-12-01 04:23:00 | NOAA-21 | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | 2.4 |
| c57191b5-08e9-35c5-996c-f14b6d6de921 | -3.73147 | -51.31056 | 2024-12-01 04:23:00 | NOAA-21 | ANAPU | PARÁ | Brasil | 1500859 | 15 | 33 | nan | nan | nan | Amazônia | 2.5 |
| 811683d3-a94c-344a-ad66-825174da2b0c | -3.26166 | -53.63989 | 2024-12-01 04:23:00 | NOAA-21 | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | 3.9 |
| 02021129-ea95-3288-8fb0-dc215cc4564c | -7.38088 | -45.83566 | 2024-12-01 04:23:00 | NOAA-21 | BALSAS | MARANHÃO | Brasil | 2101400 | 21 | 33 | nan | nan | nan | Cerrado | 1.1 |
| 7e529712-8846-36f2-85aa-fedfe9487459 | -3.29801 | -53.82894 | 2024-12-01 04:23:00 | NOAA-21 | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | 2.3 |
| 506632f0-c10d-350c-aac9-c24c07af082a | -5.3304 | -45.44223 | 2024-12-01 04:23:00 | NOAA-21 | BARRA DO CORDA | MARANHÃO | Brasil | 2101608 | 21 | 33 | nan | nan | nan | Cerrado | 1.4 |
| b7695b56-da61-3e32-9024-11b0ff2d3283 | -6.92428 | -43.54699 | 2024-12-01 04:23:00 | NOAA-21 | JERUMENHA | PIAUÍ | Brasil | 2205300 | 22 | 33 | nan | nan | nan | Cerrado | 2.8 |
| a11c24e2-90b4-340a-bcb3-06c5b1e6bf28 | -6.28997 | -43.84502 | 2024-12-01 04:23:00 | NOAA-21 | SÃO JOÃO DOS PATOS | MARANHÃO | Brasil | 2111102 | 21 | 33 | nan | nan | nan | Cerrado | 5.2 |
| 8cb727ce-1a66-3a1d-ad03-ecc6ebf9fd07 | -5.58446 | -45.21166 | 2024-12-01 04:23:00 | NOAA-21 | BARRA DO CORDA | MARANHÃO | Brasil | 2101608 | 21 | 33 | nan | nan | nan | Cerrado | 9.9 |
| c617784f-975c-3bd0-a6e7-74d4ec017606 | -3.33976 | -53.37101 | 2024-12-01 04:23:00 | NOAA-21 | MEDICILÂNDIA | PARÁ | Brasil | 1504455 | 15 | 33 | nan | nan | nan | Amazônia | 2.1 |
| 3af80cf6-7cd7-3b57-829a-87bf5e2d8454 | -5.63059 | -45.95424 | 2024-12-01 04:23:00 | NOAA-21 | GRAJAÚ | MARANHÃO | Brasil | 2104800 | 21 | 33 | nan | nan | nan | Cerrado | 2.1 |
| e66e1838-4221-303c-b816-1d160a6bdf8a | -4.55188 | -45.71851 | 2024-12-01 04:23:00 | NOAA-21 | SANTA LUZIA | MARANHÃO | Brasil | 2110005 | 21 | 33 | nan | nan | nan | Amazônia | 1.8 |
| 5e2d9bfc-00ec-359d-9852-94fc6cc3dcba | -4.61544 | -50.36303 | 2024-12-01 04:23:00 | NOAA-21 | NOVO REPARTIMENTO | PARÁ | Brasil | 1505064 | 15 | 33 | nan | nan | nan | Amazônia | 1.5 |
| e64e00cb-e9d7-3536-ad85-ccd462a17847 | -4.55411 | -45.72609 | 2024-12-01 04:23:00 | NOAA-21 | SANTA LUZIA | MARANHÃO | Brasil | 2110005 | 21 | 33 | nan | nan | nan | Amazônia | 23.4 |
| a17bf183-bdb7-312e-95aa-db21a8a91e9d | -4.37025 | -50.92418 | 2024-12-01 04:23:00 | NOAA-21 | NOVO REPARTIMENTO | PARÁ | Brasil | 1505064 | 15 | 33 | nan | nan | nan | Amazônia | 3.1 |
| 3c743471-ea43-39de-9da4-71fab3d15c9f | -4.32217 | -48.08958 | 2024-12-01 04:23:00 | NOAA-21 | RONDON DO PARÁ | PARÁ | Brasil | 1506187 | 15 | 33 | nan | nan | nan | Amazônia | 8.3 |
| 66b5b955-95bf-32f6-afe9-a272771e7b96 | -3.25258 | -53.92967 | 2024-12-01 04:23:00 | NOAA-21 | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | 1.3 |
| 85e460ee-4318-3bdb-b102-d775df70a6b0 | -3.42106 | -54.63962 | 2024-12-01 04:23:00 | NOAA-21 | PLACAS | PARÁ | Brasil | 1505650 | 15 | 33 | nan | nan | nan | Amazônia | 3.4 |
| 7a351558-0f77-333e-a9fd-446b00699210 | -7.01181 | -40.06613 | 2024-12-01 04:23:00 | NOAA-21 | POTENGI | CEARÁ | Brasil | 2311207 | 23 | 33 | nan | nan | nan | Caatinga | 0.7 |
| 71d5de0a-cb9f-36aa-926f-5155af2cf1c3 | -3.21198 | -54.17394 | 2024-12-01 04:23:00 | NOAA-21 | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | 2.3 |
| 9e8c3c7c-ecdf-38d3-b373-cdd6bd6fba55 | -3.84735 | -52.02326 | 2024-12-01 04:23:00 | NOAA-21 | SENADOR JOSÉ PORFÍRIO | PARÁ | Brasil | 1507805 | 15 | 33 | nan | nan | nan | Amazônia | 2.2 |
| 51c93498-a3b0-35fc-930d-d7a1538666c9 | -5.06391 | -50.01402 | 2024-12-01 04:23:00 | NOAA-21 | ITUPIRANGA | PARÁ | Brasil | 1503705 | 15 | 33 | nan | nan | nan | Amazônia | 1.0 |
| 9ede5c22-d37c-3d62-8013-587dc5f15d8d | -4.11928 | -48.53166 | 2024-12-01 04:23:00 | NOAA-21 | RONDON DO PARÁ | PARÁ | Brasil | 1506187 | 15 | 33 | nan | nan | nan | Amazônia | 1.8 |
| 7cb6f3f2-2ca2-3fc9-b8c4-3bf623d71318 | -4.1056 | -48.88703 | 2024-12-01 04:23:00 | NOAA-21 | GOIANÉSIA DO PARÁ | PARÁ | Brasil | 1503093 | 15 | 33 | nan | nan | nan | Amazônia | 4.7 |
| e32b6086-9e0e-3197-b713-9886ba8e392a | -9.31933 | -40.23652 | 2024-12-01 04:23:00 | NOAA-21 | JUAZEIRO | BAHIA | Brasil | 2918407 | 29 | 33 | nan | nan | nan | Caatinga | 0.8 |
| cccb1ee1-d309-3de5-a02b-01b1499c9cb6 | -4.47311 | -50.76869 | 2024-12-01 04:23:00 | NOAA-21 | NOVO REPARTIMENTO | PARÁ | Brasil | 1505064 | 15 | 33 | nan | nan | nan | Amazônia | 2.2 |
| 24359486-0891-31de-960d-99be6c8f2a88 | -6.30666 | -43.84756 | 2024-12-01 04:23:00 | NOAA-21 | SÃO JOÃO DOS PATOS | MARANHÃO | Brasil | 2111102 | 21 | 33 | nan | nan | nan | Cerrado | 2.0 |
| 93b51989-ef99-3475-ae1f-26c5399d61c2 | -6.86929 | -47.24095 | 2024-12-01 04:23:00 | NOAA-21 | ESTREITO | MARANHÃO | Brasil | 2104057 | 21 | 33 | nan | nan | nan | Cerrado | 4.9 |
| 79e8d7bc-5c0b-3d5e-bdb1-ddec4b6f14ac | -3.70984 | -51.06905 | 2024-12-01 04:23:00 | NOAA-21 | PACAJÁ | PARÁ | Brasil | 1505486 | 15 | 33 | nan | nan | nan | Amazônia | 7.7 |
| bbab92b4-ee02-30ae-a854-9323bb442689 | -6.9209 | -43.54647 | 2024-12-01 04:23:00 | NOAA-21 | GUADALUPE | PIAUÍ | Brasil | 2204501 | 22 | 33 | nan | nan | nan | Cerrado | 2.8 |
| eecf096a-bfcb-36f6-81a4-1dfe0ba806a4 | -6.86713 | -39.91149 | 2024-12-01 04:23:00 | NOAA-21 | ASSARÉ | CEARÁ | Brasil | 2301604 | 23 | 33 | nan | nan | nan | Caatinga | 1.1 |
| 9ae9ef17-6515-3f73-87cf-d4249b18b745 | -6.75847 | -46.52473 | 2024-12-01 04:23:00 | NOAA-21 | SÃO PEDRO DOS CRENTES | MARANHÃO | Brasil | 2111573 | 21 | 33 | nan | nan | nan | Cerrado | 1.2 |
| 3c206558-1ef0-3729-92ac-a2225b8d6ec5 | -5.91019 | -43.83679 | 2024-12-01 04:23:00 | NOAA-21 | BURITI BRAVO | MARANHÃO | Brasil | 2102309 | 21 | 33 | nan | nan | nan | Cerrado | 0.8 |
| 6e5d0a1b-490c-31cb-bf52-facf5518b276 | -3.49919 | -54.66993 | 2024-12-01 04:23:00 | NOAA-21 | PLACAS | PARÁ | Brasil | 1505650 | 15 | 33 | nan | nan | nan | Amazônia | 1.9 |
| 92e9aec6-b839-3ba9-9db7-7f701b8465da | -4.47381 | -50.76452 | 2024-12-01 04:23:00 | NOAA-21 | NOVO REPARTIMENTO | PARÁ | Brasil | 1505064 | 15 | 33 | nan | nan | nan | Amazônia | 2.2 |
| 033d4c42-8ae1-3c06-b85d-a2fa98237e29 | -3.24219 | -53.92381 | 2024-12-01 04:23:00 | NOAA-21 | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | 1.8 |
| a69ef40a-1a0b-32b0-a207-587601d025db | -5.91352 | -43.83731 | 2024-12-01 04:23:00 | NOAA-21 | BURITI BRAVO | MARANHÃO | Brasil | 2102309 | 21 | 33 | nan | nan | nan | Cerrado | 0.8 |
| a4dfd6e5-5ef0-368a-ae3b-1d492909efa7 | -5.63003 | -45.95779 | 2024-12-01 04:23:00 | NOAA-21 | GRAJAÚ | MARANHÃO | Brasil | 2104800 | 21 | 33 | nan | nan | nan | Cerrado | 3.3 |
| 90d13ad4-b4a1-3c4f-8645-a0242185db78 | -5.74455 | -46.18407 | 2024-12-01 04:23:00 | NOAA-21 | GRAJAÚ | MARANHÃO | Brasil | 2104800 | 21 | 33 | nan | nan | nan | Cerrado | 2.5 |
| 865f5c9d-e68a-3e12-a58f-eaf4e2034350 | -6.92884 | -43.5509 | 2024-12-01 04:23:00 | NOAA-21 | GUADALUPE | PIAUÍ | Brasil | 2204501 | 22 | 33 | nan | nan | nan | Cerrado | 7.8 |
| 2a7f9b43-3ca0-3b23-82c7-4914f959dd7f | -3.96894 | -49.96611 | 2024-12-01 04:23:00 | NOAA-21 | TUCURUÍ | PARÁ | Brasil | 1508100 | 15 | 33 | nan | nan | nan | Amazônia | 2.7 |
| b0b89af5-689d-3140-9687-4d6b6c85131b | -5.08482 | -49.83715 | 2024-12-01 04:23:00 | NOAA-21 | ITUPIRANGA | PARÁ | Brasil | 1503705 | 15 | 33 | nan | nan | nan | Amazônia | 1.0 |
| 0cde7994-78da-3c5a-b47e-ffbd7202512f | -7.25023 | -39.85125 | 2024-12-01 04:23:00 | NOAA-21 | SANTANA DO CARIRI | CEARÁ | Brasil | 2312106 | 23 | 33 | nan | nan | nan | Caatinga | 2.6 |
| ce218f47-299d-3ba2-923f-fa264ec86b08 | -3.30837 | -53.86749 | 2024-12-01 04:23:00 | NOAA-21 | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | 16.4 |
| acc68b75-e300-3321-acd3-c7f56934e91a | -3.72782 | -54.52563 | 2024-12-01 04:23:00 | NOAA-21 | PLACAS | PARÁ | Brasil | 1505650 | 15 | 33 | nan | nan | nan | Amazônia | 1.1 |
| 693df1cc-1cbb-34b0-ad24-b55b16e46704 | -5.30409 | -45.26302 | 2024-12-01 04:23:00 | NOAA-21 | BARRA DO CORDA | MARANHÃO | Brasil | 2101608 | 21 | 33 | nan | nan | nan | Cerrado | 1.3 |
| b1df0efa-644f-3831-82a2-2ede6a8316e0 | -5.61167 | -45.0601 | 2024-12-01 04:23:00 | NOAA-21 | BARRA DO CORDA | MARANHÃO | Brasil | 2101608 | 21 | 33 | nan | nan | nan | Cerrado | 1.4 |


[Clique aqui para ver as próximas entradas](README35.md)
