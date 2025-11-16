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

## Dados Diários - Página 18

| ID | Latitude | Longitude | Data/Hora GMT | Satélite | Município | Estado | País | Município ID | Estado ID | País ID | Dias sem Chuva | Precipitação | Risco de Fogo | Bioma | FRP |
|----|----------|-----------|---------------|----------|-----------|--------|------|--------------|-----------|---------|----------------|--------------|----------------|-------|-----|
| 5ce53333-6592-3b54-ba24-a458b0f68308 | -4.22714 | -44.64482 | 2025-11-16 03:46:00 | NPP-375D | BACABAL | MARANHÃO | Brasil | 2101202 | 21 | 33 | nan | nan | nan | Cerrado | 2.3 |
| e69f98e4-6fd0-3dc6-b8e3-c26973b2f2e0 | -6.53134 | -39.64989 | 2025-11-16 03:46:00 | NPP-375D | JUCÁS | CEARÁ | Brasil | 2307403 | 23 | 33 | nan | nan | nan | Caatinga | 1.9 |
| 4fd7e6f8-b6cd-3f30-91c4-c57c3a840495 | -10.16659 | -44.49017 | 2025-11-16 03:46:00 | NPP-375D | PARNAGUÁ | PIAUÍ | Brasil | 2207603 | 22 | 33 | nan | nan | nan | Cerrado | 2.5 |
| deff5a4c-95fb-3a91-90d7-15d30ab10d71 | -7.12809 | -41.66368 | 2025-11-16 03:46:00 | NPP-375D | PAQUETÁ | PIAUÍ | Brasil | 2207553 | 22 | 33 | nan | nan | nan | Caatinga | 2.4 |
| 930cc123-0833-35c2-97ab-8b0bc7b1c659 | -9.05766 | -44.79664 | 2025-11-16 03:46:00 | NPP-375D | BOM JESUS | PIAUÍ | Brasil | 2201903 | 22 | 33 | nan | nan | nan | Cerrado | 1.9 |
| f7df6ef4-35cf-31ee-b4ca-37826fbf5954 | -5.63138 | -43.93129 | 2025-11-16 03:46:00 | NPP-375D | FORTUNA | MARANHÃO | Brasil | 2104206 | 21 | 33 | nan | nan | nan | Cerrado | 2.4 |
| 267e02c2-f68d-39c3-9cb7-fcfdd1e930ed | -6.9437 | -41.53224 | 2025-11-16 03:46:00 | NPP-375D | SANTANA DO PIAUÍ | PIAUÍ | Brasil | 2209351 | 22 | 33 | nan | nan | nan | Caatinga | 1.6 |
| 6299f322-ce3b-31f2-b8b0-c0b605d2691c | -10.00762 | -44.78498 | 2025-11-16 03:46:00 | NPP-375D | RIACHO FRIO | PIAUÍ | Brasil | 2208858 | 22 | 33 | nan | nan | nan | Cerrado | 1.7 |
| 0c41ecfc-135a-3ec0-b9a3-1e3353976927 | -7.26237 | -48.03042 | 2025-11-16 03:46:00 | NPP-375D | BABAÇULÂNDIA | TOCANTINS | Brasil | 1703008 | 17 | 33 | nan | nan | nan | Cerrado | 3.0 |
| 725786e2-eca7-3b1e-8062-10498409f3ba | -5.53572 | -41.77542 | 2025-11-16 03:46:00 | NPP-375D | SÃO JOÃO DA SERRA | PIAUÍ | Brasil | 2209906 | 22 | 33 | nan | nan | nan | Caatinga | 1.4 |
| 275234f2-770d-3e0c-a6aa-06123be1b317 | -7.40743 | -40.06411 | 2025-11-16 03:46:00 | NPP-375D | BODOCÓ | PERNAMBUCO | Brasil | 2602001 | 26 | 33 | nan | nan | nan | Caatinga | 11.0 |
| f4b4b913-4f74-3f84-b866-17b726217512 | -2.51391 | -47.81076 | 2025-11-16 03:46:00 | NPP-375D | IPIXUNA DO PARÁ | PARÁ | Brasil | 1503457 | 15 | 33 | nan | nan | nan | Amazônia | 4.2 |
| 48635358-0812-3833-9551-574aad9c1139 | -8.20922 | -43.56735 | 2025-11-16 03:46:00 | NPP-375D | COLÔNIA DO GURGUÉIA | PIAUÍ | Brasil | 2202752 | 22 | 33 | nan | nan | nan | Cerrado | 2.9 |
| 3fa14b6e-e552-3825-991b-587da746fcda | -4.64436 | -47.95359 | 2025-11-16 03:46:00 | NPP-375D | RONDON DO PARÁ | PARÁ | Brasil | 1506187 | 15 | 33 | nan | nan | nan | Amazônia | 3.1 |
| 397cf3b2-e118-3135-9ab0-14e81f89ee8c | -4.6981 | -46.31652 | 2025-11-16 03:46:00 | NPP-375D | BURITICUPU | MARANHÃO | Brasil | 2102325 | 21 | 33 | nan | nan | nan | Amazônia | 7.4 |
| 6bfa7dc4-d875-313e-86de-9eb001400880 | -9.16179 | -37.91217 | 2025-11-16 03:46:00 | NPP-375D | ÁGUA BRANCA | ALAGOAS | Brasil | 2700102 | 27 | 33 | nan | nan | nan | Caatinga | 0.9 |
| 8259a137-a51c-307b-a6c9-a787b22e2d88 | -4.42657 | -43.41026 | 2025-11-16 03:46:00 | NPP-375D | ALDEIAS ALTAS | MARANHÃO | Brasil | 2100303 | 21 | 33 | nan | nan | nan | Cerrado | 0.9 |
| 83f72720-f1e9-3dc9-8df9-ee5d4301db46 | -6.51677 | -39.52261 | 2025-11-16 03:46:00 | NPP-375D | JUCÁS | CEARÁ | Brasil | 2307403 | 23 | 33 | nan | nan | nan | Caatinga | 1.5 |
| 4e1fce1f-5ef4-3ea7-b158-6822deed60d3 | -2.51732 | -47.80934 | 2025-11-16 03:46:00 | NPP-375D | IPIXUNA DO PARÁ | PARÁ | Brasil | 1503457 | 15 | 33 | nan | nan | nan | Amazônia | 15.1 |
| 0d5cb408-95f1-3f21-88a8-f0d161e264a5 | -4.23004 | -44.64598 | 2025-11-16 03:46:00 | NPP-375D | BACABAL | MARANHÃO | Brasil | 2101202 | 21 | 33 | nan | nan | nan | Cerrado | 2.4 |
| f0b15283-16ba-3a16-ad9a-34167c7d32bf | -6.62771 | -43.69804 | 2025-11-16 03:46:00 | NPP-375D | SÃO JOÃO DOS PATOS | MARANHÃO | Brasil | 2111102 | 21 | 33 | nan | nan | nan | Cerrado | 0.7 |
| 8dbc3261-d917-3444-9e28-cf74ef5ccefc | -6.85782 | -42.84166 | 2025-11-16 03:46:00 | NPP-375D | FLORIANO | PIAUÍ | Brasil | 2203909 | 22 | 33 | nan | nan | nan | Caatinga | 12.9 |
| 1751655b-491a-3b54-bf34-71431cb49f73 | -7.37084 | -43.31871 | 2025-11-16 03:46:00 | NPP-375D | JERUMENHA | PIAUÍ | Brasil | 2205300 | 22 | 33 | nan | nan | nan | Cerrado | 3.6 |
| 6ddd42fc-ff0a-3ee6-a9fe-afa917232a99 | -3.58632 | -41.66269 | 2025-11-16 03:46:00 | NPP-375D | COCAL | PIAUÍ | Brasil | 2202703 | 22 | 33 | nan | nan | nan | Caatinga | 5.9 |
| f4f16345-3a4a-312b-9d3c-2f476a1328a7 | -6.92865 | -39.62389 | 2025-11-16 03:46:00 | NPP-375D | ASSARÉ | CEARÁ | Brasil | 2301604 | 23 | 33 | nan | nan | nan | Caatinga | 3.8 |
| 16816378-328b-3440-b43b-ec065680e2a4 | -7.27219 | -48.03127 | 2025-11-16 03:46:00 | NPP-375D | BABAÇULÂNDIA | TOCANTINS | Brasil | 1703008 | 17 | 33 | nan | nan | nan | Cerrado | 3.0 |
| 8f775486-72f9-3b9a-b616-815ec9b0c8df | -9.85324 | -44.72014 | 2025-11-16 03:46:00 | NPP-375D | RIACHO FRIO | PIAUÍ | Brasil | 2208858 | 22 | 33 | nan | nan | nan | Cerrado | 1.8 |
| 613684cb-2f2b-3f70-a25b-910e73db271c | -6.78233 | -43.54419 | 2025-11-16 03:46:00 | NPP-375D | SÃO JOÃO DOS PATOS | MARANHÃO | Brasil | 2111102 | 21 | 33 | nan | nan | nan | Cerrado | 1.5 |
| aded940c-7bd9-347a-be24-1fadf0666164 | -5.52377 | -40.99265 | 2025-11-16 03:46:00 | NPP-375D | SÃO MIGUEL DO TAPUIO | PIAUÍ | Brasil | 2210409 | 22 | 33 | nan | nan | nan | Caatinga | 2.6 |
| bf4545de-77e3-3ff3-beb3-8e2eee6065d3 | -8.05661 | -43.10453 | 2025-11-16 03:46:00 | NPP-375D | CANTO DO BURITI | PIAUÍ | Brasil | 2202307 | 22 | 33 | nan | nan | nan | Caatinga | 22.4 |
| 0ef6f3f9-a6c3-391e-889f-e89fd64df8d5 | -4.62968 | -47.40691 | 2025-11-16 03:46:00 | NPP-375D | ITINGA DO MARANHÃO | MARANHÃO | Brasil | 2105427 | 21 | 33 | nan | nan | nan | Amazônia | 4.2 |
| 71641c01-182e-3ca9-aa4b-9da8a57897b8 | -10.16849 | -44.49187 | 2025-11-16 03:46:00 | NPP-375D | PARNAGUÁ | PIAUÍ | Brasil | 2207603 | 22 | 33 | nan | nan | nan | Cerrado | 1.3 |
| 2d05cf12-6da1-3401-9c88-42ba075f7413 | -5.11089 | -39.056 | 2025-11-16 03:46:00 | NPP-375D | QUIXADÁ | CEARÁ | Brasil | 2311306 | 23 | 33 | nan | nan | nan | Caatinga | 3.3 |
| e36959fa-53b5-3b44-ac24-671b4517628a | -7.29622 | -45.10651 | 2025-11-16 03:46:00 | NPP-375D | LORETO | MARANHÃO | Brasil | 2106102 | 21 | 33 | nan | nan | nan | Cerrado | 1.3 |
| 9fccc90a-d5bf-3dbc-b99c-ba80a79e3c00 | -7.02109 | -45.16701 | 2025-11-16 03:46:00 | NPP-375D | LORETO | MARANHÃO | Brasil | 2106102 | 21 | 33 | nan | nan | nan | Cerrado | 1.2 |
| a6f9210a-a04b-3f2c-a279-6f4f8147231d | -5.32638 | -35.93472 | 2025-11-16 03:46:00 | NPP-375D | JOÃO CÂMARA | RIO GRANDE DO NORTE | Brasil | 2405801 | 24 | 33 | nan | nan | nan | Caatinga | 4.9 |
| c910fd27-c3c5-3659-afc0-e1c047519e6d | -5.63111 | -43.92836 | 2025-11-16 03:46:00 | NPP-375D | FORTUNA | MARANHÃO | Brasil | 2104206 | 21 | 33 | nan | nan | nan | Cerrado | 3.2 |
| 3b8b0031-7b78-327f-9dc3-0849a75c20ab | -4.89275 | -45.02216 | 2025-11-16 03:46:00 | NPP-375D | ESPERANTINÓPOLIS | MARANHÃO | Brasil | 2104008 | 21 | 33 | nan | nan | nan | Cerrado | 2.1 |
| 5904a935-fda3-3921-9ef6-4f96fc613568 | -9.99599 | -44.76706 | 2025-11-16 03:46:00 | NPP-375D | RIACHO FRIO | PIAUÍ | Brasil | 2208858 | 22 | 33 | nan | nan | nan | Cerrado | 2.8 |
| bbe50674-24e8-3c4e-93f1-04a3bfd007ce | -4.74383 | -46.38565 | 2025-11-16 03:46:00 | NPP-375D | BURITICUPU | MARANHÃO | Brasil | 2102325 | 21 | 33 | nan | nan | nan | Amazônia | 4.9 |
| 95167212-7697-3985-9720-66def2a96b41 | -6.81253 | -39.14334 | 2025-11-16 03:46:00 | NPP-375D | LAVRAS DA MANGABEIRA | CEARÁ | Brasil | 2307502 | 23 | 33 | nan | nan | nan | Caatinga | 3.1 |
| 7e87e6a4-d0fb-3075-a9f9-94a272e2bcde | -5.28741 | -44.29731 | 2025-11-16 03:46:00 | NPP-375D | GONÇALVES DIAS | MARANHÃO | Brasil | 2104404 | 21 | 33 | nan | nan | nan | Cerrado | 1.0 |
| 0dc1a8e2-6f7a-3ed7-a5f0-e9c6e0e16cbd | -6.36273 | -39.62736 | 2025-11-16 03:46:00 | NPP-375D | JUCÁS | CEARÁ | Brasil | 2307403 | 23 | 33 | nan | nan | nan | Caatinga | 2.5 |
| 7f4c3994-57d0-3b2e-80ca-6d27b652c80a | -7.5341 | -38.7332 | 2025-11-16 03:46:00 | NPP-375D | MAURITI | CEARÁ | Brasil | 2308104 | 23 | 33 | nan | nan | nan | Caatinga | 2.3 |
| 7c952d33-238d-3482-8e11-00d7713295c7 | -9.72476 | -43.9595 | 2025-11-16 03:46:00 | NPP-375D | MORRO CABEÇA NO TEMPO | PIAUÍ | Brasil | 2206654 | 22 | 33 | nan | nan | nan | Caatinga | 6.4 |
| 8d47755e-d412-398b-957c-b84a80150148 | -5.52582 | -41.77856 | 2025-11-16 03:46:00 | NPP-375D | SÃO JOÃO DA SERRA | PIAUÍ | Brasil | 2209906 | 22 | 33 | nan | nan | nan | Caatinga | 1.7 |
| ece342e5-8322-3e8b-ab2a-8e6cd7f3f31b | -5.47732 | -40.96829 | 2025-11-16 03:46:00 | NPP-375D | SÃO MIGUEL DO TAPUIO | PIAUÍ | Brasil | 2210409 | 22 | 33 | nan | nan | nan | Caatinga | 3.5 |
| f2900575-3eb6-307d-ba64-d5e0060be32a | -7.71768 | -42.9417 | 2025-11-16 03:46:00 | NPP-375D | FLORES DO PIAUÍ | PIAUÍ | Brasil | 2203800 | 22 | 33 | nan | nan | nan | Caatinga | 2.2 |
| d14cfa39-be11-32a4-9c8e-c2322974c26f | -6.0255 | -48.1859 | 2025-11-16 03:46:00 | NPP-375D | SÃO BENTO DO TOCANTINS | TOCANTINS | Brasil | 1720101 | 17 | 33 | nan | nan | nan | Amazônia | 0.7 |
| 56655221-4609-3f7c-be09-b181b380a0ba | -5.42032 | -44.63297 | 2025-11-16 03:46:00 | NPP-375D | SANTA FILOMENA DO MARANHÃO | MARANHÃO | Brasil | 2109759 | 21 | 33 | nan | nan | nan | Cerrado | 0.8 |
| 934cea60-df61-306d-8ff6-5f6b05b1bc33 | -9.74833 | -43.97713 | 2025-11-16 03:46:00 | NPP-375D | MORRO CABEÇA NO TEMPO | PIAUÍ | Brasil | 2206654 | 22 | 33 | nan | nan | nan | Cerrado | 6.5 |
| db7ef64a-b2f7-3f28-92b6-f5173cc419aa | -4.09784 | -43.35038 | 2025-11-16 03:46:00 | NPP-375D | CHAPADINHA | MARANHÃO | Brasil | 2103208 | 21 | 33 | nan | nan | nan | Cerrado | 0.6 |
| f5f5e189-24dc-3e5b-8fc6-42a9a19395bf | -6.63279 | -43.69901 | 2025-11-16 03:46:00 | NPP-375D | SÃO JOÃO DOS PATOS | MARANHÃO | Brasil | 2111102 | 21 | 33 | nan | nan | nan | Cerrado | 0.6 |
| 39da60a9-4a8a-37b2-9019-07522351b5bc | -5.32694 | -35.93118 | 2025-11-16 03:46:00 | NPP-375D | JOÃO CÂMARA | RIO GRANDE DO NORTE | Brasil | 2405801 | 24 | 33 | nan | nan | nan | Caatinga | 4.0 |
| 3a365498-baad-3162-953b-5c01beb84034 | -3.59564 | -41.6643 | 2025-11-16 03:46:00 | NPP-375D | COCAL | PIAUÍ | Brasil | 2202703 | 22 | 33 | nan | nan | nan | Caatinga | 3.1 |
| d6b3153f-e632-3dc0-b281-ec01b7af17c6 | -10.11956 | -43.91033 | 2025-11-16 03:46:00 | NPP-375D | AVELINO LOPES | PIAUÍ | Brasil | 2201101 | 22 | 33 | nan | nan | nan | Cerrado | 1.8 |
| 62867fc8-1eec-3c7b-9056-42bb464cfa64 | -9.8444 | -44.1799 | 2025-11-16 03:46:00 | NPP-375D | CURIMATÁ | PIAUÍ | Brasil | 2203206 | 22 | 33 | nan | nan | nan | Cerrado | 2.3 |
| 4ca26fb0-fb98-377a-ad9a-8e8e30ce123a | -3.66705 | -44.81746 | 2025-11-16 03:46:00 | NPP-375D | VITÓRIA DO MEARIM | MARANHÃO | Brasil | 2112902 | 21 | 33 | nan | nan | nan | Amazônia | 1.3 |
| 0776f422-54b3-339b-89a0-4bf017e82140 | -4.61093 | -43.30243 | 2025-11-16 03:46:00 | NPP-375D | ALDEIAS ALTAS | MARANHÃO | Brasil | 2100303 | 21 | 33 | nan | nan | nan | Cerrado | 0.9 |
| 53b8d8e6-4f1f-3454-bf76-dfa4896ca062 | -5.59229 | -41.06693 | 2025-11-16 03:46:00 | NPP-375D | SÃO MIGUEL DO TAPUIO | PIAUÍ | Brasil | 2210409 | 22 | 33 | nan | nan | nan | Caatinga | 1.4 |
| 2d6e5356-cb6b-3e84-9d7c-016386daa571 | -3.95862 | -44.84887 | 2025-11-16 03:46:00 | NPP-375D | LAGO VERDE | MARANHÃO | Brasil | 2105906 | 21 | 33 | nan | nan | nan | Amazônia | 7.0 |
| a65705a1-8681-3302-9847-83e2ef0eb181 | -8.75336 | -45.64754 | 2025-11-16 03:46:00 | NPP-375D | SANTA FILOMENA | PIAUÍ | Brasil | 2209203 | 22 | 33 | nan | nan | nan | Cerrado | 1.6 |
| d82d4d94-a70f-3eda-9677-465463ea3efb | -7.05305 | -43.94719 | 2025-11-16 03:46:00 | NPP-375D | MARCOS PARENTE | PIAUÍ | Brasil | 2206001 | 22 | 33 | nan | nan | nan | Cerrado | 2.0 |
| 457a7412-0d08-3237-abe8-fa0dfe4b2e08 | -4.09836 | -43.34728 | 2025-11-16 03:46:00 | NPP-375D | CHAPADINHA | MARANHÃO | Brasil | 2103208 | 21 | 33 | nan | nan | nan | Cerrado | 0.6 |
| 0533bca7-4737-3f86-9363-ac35497ea631 | -5.99611 | -41.9104 | 2025-11-16 03:46:00 | NPP-375D | SANTA CRUZ DOS MILAGRES | PIAUÍ | Brasil | 2209153 | 22 | 33 | nan | nan | nan | Caatinga | 1.4 |
| 58dd138b-b99f-3f5b-994f-546adeb9b4a6 | -4.0264 | -42.07538 | 2025-11-16 03:46:00 | NPP-375D | BATALHA | PIAUÍ | Brasil | 2201507 | 22 | 33 | nan | nan | nan | Caatinga | 1.9 |
| eb4aec27-0621-3482-8dc6-ac18ef691671 | -9.999 | -44.77355 | 2025-11-16 03:46:00 | NPP-375D | RIACHO FRIO | PIAUÍ | Brasil | 2208858 | 22 | 33 | nan | nan | nan | Cerrado | 2.8 |
| ad82850b-f1b2-3904-b88b-9d3f84f16ae5 | -6.03232 | -48.18719 | 2025-11-16 03:46:00 | NPP-375D | SÃO BENTO DO TOCANTINS | TOCANTINS | Brasil | 1720101 | 17 | 33 | nan | nan | nan | Amazônia | 0.5 |
| b141c02d-9edc-3522-bf04-cb48b60a6b72 | -7.15211 | -41.76148 | 2025-11-16 03:46:00 | NPP-375D | SANTA CRUZ DO PIAUÍ | PIAUÍ | Brasil | 2209104 | 22 | 33 | nan | nan | nan | Caatinga | 7.2 |
| 7744e26c-a1c0-34ca-a4ef-4b8604fc6c23 | -7.72018 | -47.29773 | 2025-11-16 03:46:00 | NPP-375D | CAROLINA | MARANHÃO | Brasil | 2102804 | 21 | 33 | nan | nan | nan | Cerrado | 1.1 |
| 035c4662-1677-365d-bcb0-c3ef7cd9c1fb | -9.85441 | -44.71384 | 2025-11-16 03:46:00 | NPP-375D | RIACHO FRIO | PIAUÍ | Brasil | 2208858 | 22 | 33 | nan | nan | nan | Cerrado | 1.4 |
| 56df4d59-e3e4-3835-a5fd-8648c8657582 | -8.58884 | -46.05849 | 2025-11-16 03:46:00 | NPP-375D | TASSO FRAGOSO | MARANHÃO | Brasil | 2112001 | 21 | 33 | nan | nan | nan | Cerrado | 1.0 |
| 0ec2b896-5ec5-3437-92ce-fa2dfc759c0e | -5.28139 | -44.29974 | 2025-11-16 03:46:00 | NPP-375D | GONÇALVES DIAS | MARANHÃO | Brasil | 2104404 | 21 | 33 | nan | nan | nan | Cerrado | 1.0 |
| f398a90b-44dd-32ca-a82b-09725ee79796 | -7.09773 | -42.73026 | 2025-11-16 03:46:00 | NPP-375D | NAZARÉ DO PIAUÍ | PIAUÍ | Brasil | 2206704 | 22 | 33 | nan | nan | nan | Caatinga | 1.6 |
| 5b421dde-08fb-3b2c-a8d7-a8241c7e3107 | -7.71299 | -47.30138 | 2025-11-16 03:46:00 | NPP-375D | CAROLINA | MARANHÃO | Brasil | 2102804 | 21 | 33 | nan | nan | nan | Cerrado | 3.0 |
| 3c9000f9-458f-3941-b1b3-510c5fd839f0 | -6.03212 | -48.18762 | 2025-11-16 03:46:00 | NPP-375D | SÃO BENTO DO TOCANTINS | TOCANTINS | Brasil | 1720101 | 17 | 33 | nan | nan | nan | Amazônia | 1.2 |
| 78e7d50f-a76d-3c56-b76a-b863b5d08c34 | -9.99957 | -44.77039 | 2025-11-16 03:46:00 | NPP-375D | RIACHO FRIO | PIAUÍ | Brasil | 2208858 | 22 | 33 | nan | nan | nan | Cerrado | 3.2 |
| aa4508ce-7b27-3c52-b143-0fbb289770b1 | -5.96359 | -43.74924 | 2025-11-16 03:46:00 | NPP-375D | BURITI BRAVO | MARANHÃO | Brasil | 2102309 | 21 | 33 | nan | nan | nan | Cerrado | 1.3 |
| b205d2f6-844e-3075-be8b-ac9cd64dc87d | -5.64576 | -47.74516 | 2025-11-16 03:46:00 | NPP-375D | AXIXÁ DO TOCANTINS | TOCANTINS | Brasil | 1702901 | 17 | 33 | nan | nan | nan | Cerrado | 2.9 |
| 6b2ae8f4-8a63-321b-a729-f652f9358fd2 | -3.3084 | -42.65171 | 2025-11-16 03:46:00 | NPP-375D | SANTANA DO MARANHÃO | MARANHÃO | Brasil | 2110237 | 21 | 33 | nan | nan | nan | Cerrado | 4.8 |
| 9ccb6afc-7647-3f59-b8c7-8c63d37dd29c | -7.36787 | -43.3284 | 2025-11-16 03:46:00 | NPP-375D | JERUMENHA | PIAUÍ | Brasil | 2205300 | 22 | 33 | nan | nan | nan | Cerrado | 4.1 |
| 9ae1afb7-d29b-3ff6-96fc-e317a5ea30c0 | -9.73655 | -43.95029 | 2025-11-16 03:46:00 | NPP-375D | MORRO CABEÇA NO TEMPO | PIAUÍ | Brasil | 2206654 | 22 | 33 | nan | nan | nan | Caatinga | 2.4 |
| eaa61d6f-c385-31fd-973c-41df8ffb12fd | -8.20823 | -43.57286 | 2025-11-16 03:46:00 | NPP-375D | COLÔNIA DO GURGUÉIA | PIAUÍ | Brasil | 2202752 | 22 | 33 | nan | nan | nan | Cerrado | 2.9 |
| b14a2b14-f027-354b-be66-5e66cea61353 | -9.33883 | -46.57832 | 2025-11-16 03:46:00 | NPP-375D | ALTO PARNAÍBA | MARANHÃO | Brasil | 2100501 | 21 | 33 | nan | nan | nan | Cerrado | 1.1 |
| dbcaf5d9-0e38-3e42-97ae-4653ea6ec06e | -3.56639 | -41.72442 | 2025-11-16 03:46:00 | NPP-375D | CARAÚBAS DO PIAUÍ | PIAUÍ | Brasil | 2202539 | 22 | 33 | nan | nan | nan | Caatinga | 2.0 |
| 4265c1a0-33c0-359b-8062-1108946bbc3b | -7.72112 | -47.29263 | 2025-11-16 03:46:00 | NPP-375D | CAROLINA | MARANHÃO | Brasil | 2102804 | 21 | 33 | nan | nan | nan | Cerrado | 0.7 |
| 18181297-18f2-3da0-bdf3-e1e1020a051a | -7.36497 | -43.32322 | 2025-11-16 03:46:00 | NPP-375D | JERUMENHA | PIAUÍ | Brasil | 2205300 | 22 | 33 | nan | nan | nan | Cerrado | 5.5 |
| 05ce0e90-8795-3e6c-ab62-250bf85d180c | -3.84072 | -40.78337 | 2025-11-16 03:46:00 | NPP-375D | COREAÚ | CEARÁ | Brasil | 2304004 | 23 | 33 | nan | nan | nan | Caatinga | 1.5 |
| 0e482d23-ee88-367c-b04e-cbcdba3b9045 | -6.08921 | -41.61152 | 2025-11-16 03:46:00 | NPP-375D | PIMENTEIRAS | PIAUÍ | Brasil | 2208106 | 22 | 33 | nan | nan | nan | Caatinga | 1.5 |
| 41289ff8-5cc6-3d05-8185-4f89ab8c750c | -9.05963 | -44.75675 | 2025-11-16 03:46:00 | NPP-375D | BOM JESUS | PIAUÍ | Brasil | 2201903 | 22 | 33 | nan | nan | nan | Cerrado | 3.9 |
| f8b52beb-cd68-335b-814b-bfada0b52597 | -6.68035 | -42.05023 | 2025-11-16 03:46:00 | NPP-375D | OEIRAS | PIAUÍ | Brasil | 2207009 | 22 | 33 | nan | nan | nan | Caatinga | 4.1 |
| fade3a34-3b1d-3361-8d2c-7d6092a6f107 | -5.23359 | -44.34819 | 2025-11-16 03:46:00 | NPP-375D | GONÇALVES DIAS | MARANHÃO | Brasil | 2104404 | 21 | 33 | nan | nan | nan | Cerrado | 1.4 |
| 2646fb3a-9116-349e-bdf1-1b8b4c2eacdd | -10.00414 | -44.7747 | 2025-11-16 03:46:00 | NPP-375D | RIACHO FRIO | PIAUÍ | Brasil | 2208858 | 22 | 33 | nan | nan | nan | Cerrado | 2.3 |
| 9dc0f20e-96b5-3c2c-a266-ad9e0a0020c1 | -6.77628 | -43.544 | 2025-11-16 03:46:00 | NPP-375D | SÃO JOÃO DOS PATOS | MARANHÃO | Brasil | 2111102 | 21 | 33 | nan | nan | nan | Cerrado | 1.4 |
| e57ba3a0-b162-3add-8f28-1363b4accbbf | -6.13577 | -48.04721 | 2025-11-16 03:46:00 | NPP-375D | ANANÁS | TOCANTINS | Brasil | 1701002 | 17 | 33 | nan | nan | nan | Cerrado | 1.9 |
| 58dca58f-1afa-3b66-85fe-a0611fd0a786 | -4.73673 | -46.38935 | 2025-11-16 03:46:00 | NPP-375D | BURITICUPU | MARANHÃO | Brasil | 2102325 | 21 | 33 | nan | nan | nan | Amazônia | 4.9 |
| 5424ceb0-c3b5-3ed4-a0be-b0688d1aef44 | -7.28431 | -46.71874 | 2025-11-16 03:46:00 | NPP-375D | RIACHÃO | MARANHÃO | Brasil | 2109502 | 21 | 33 | nan | nan | nan | Cerrado | 3.5 |
| bc04a905-1df1-354e-b8fb-9bd0284121c5 | -6.90605 | -38.87885 | 2025-11-16 03:46:00 | NPP-375D | AURORA | CEARÁ | Brasil | 2301703 | 23 | 33 | nan | nan | nan | Caatinga | 1.7 |
| 84ead533-30c2-33b1-9f4b-0b370626c133 | -7.35615 | -43.33773 | 2025-11-16 03:46:00 | NPP-375D | JERUMENHA | PIAUÍ | Brasil | 2205300 | 22 | 33 | nan | nan | nan | Cerrado | 2.4 |
| c4aa699b-8eb3-38aa-ad77-61eabeac6897 | -5.48483 | -44.84243 | 2025-11-16 03:46:00 | NPP-375D | TUNTUM | MARANHÃO | Brasil | 2112308 | 21 | 33 | nan | nan | nan | Cerrado | 5.0 |


[Clique aqui para ver as próximas entradas](README19.md)
