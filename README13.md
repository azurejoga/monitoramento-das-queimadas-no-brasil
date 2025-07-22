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

## Dados Diários - Página 13

| ID | Latitude | Longitude | Data/Hora GMT | Satélite | Município | Estado | País | Município ID | Estado ID | País ID | Dias sem Chuva | Precipitação | Risco de Fogo | Bioma | FRP |
|----|----------|-----------|---------------|----------|-----------|--------|------|--------------|-----------|---------|----------------|--------------|----------------|-------|-----|
| b1586a83-f27a-324d-91c1-d16d2a787ee5 | -9.57578 | -44.51698 | 2025-07-22 04:51:00 | NOAA-21 | REDENÇÃO DO GURGUÉIA | PIAUÍ | Brasil | 2208700 | 22 | 33 | nan | nan | nan | Cerrado | 3.4 |
| b6e834ef-e673-3626-9542-ca818e5d2658 | -6.21208 | -44.29613 | 2025-07-22 04:51:00 | NOAA-21 | MIRADOR | MARANHÃO | Brasil | 2106706 | 21 | 33 | nan | nan | nan | Cerrado | 1.2 |
| e0f1e27c-4435-362c-be8e-67fb90d33820 | -8.8861 | -50.15783 | 2025-07-22 04:51:00 | NOAA-21 | SANTA MARIA DAS BARREIRAS | PARÁ | Brasil | 1506583 | 15 | 33 | nan | nan | nan | Amazônia | 0.9 |
| cf95c041-bbe9-375e-b01f-7da2c95564e3 | -8.10361 | -46.8286 | 2025-07-22 04:51:00 | NOAA-21 | CAMPOS LINDOS | TOCANTINS | Brasil | 1703842 | 17 | 33 | nan | nan | nan | Cerrado | 2.0 |
| ab5e042d-1f8e-3083-8858-cd7d37eb416f | -4.80855 | -45.26133 | 2025-07-22 04:51:00 | NOAA-21 | LAGO DA PEDRA | MARANHÃO | Brasil | 2105708 | 21 | 33 | nan | nan | nan | Cerrado | 1.1 |
| c4a3e961-efd5-3fcf-86fa-ea67b0c67b26 | -10.63031 | -45.22865 | 2025-07-22 04:51:00 | NOAA-21 | CRISTALÂNDIA DO PIAUÍ | PIAUÍ | Brasil | 2203008 | 22 | 33 | nan | nan | nan | Cerrado | 4.3 |
| 6aa62bf6-d523-3da4-b5ac-218896e911ad | -7.27459 | -60.17699 | 2025-07-22 04:51:00 | NOAA-21 | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 5.9 |
| 491cb456-c508-3816-94f3-7cd8085d5121 | -4.38699 | -43.28827 | 2025-07-22 04:51:00 | NOAA-21 | ALDEIAS ALTAS | MARANHÃO | Brasil | 2100303 | 21 | 33 | nan | nan | nan | Cerrado | 5.2 |
| 1ab8cfb4-f857-39e6-90dc-e526a1a9c32b | -10.61352 | -45.23863 | 2025-07-22 04:51:00 | NOAA-21 | CRISTALÂNDIA DO PIAUÍ | PIAUÍ | Brasil | 2203008 | 22 | 33 | nan | nan | nan | Cerrado | 3.1 |
| 18287fb2-14a2-3907-8fcb-f588ba891081 | -7.97119 | -55.2991 | 2025-07-22 04:51:00 | NOAA-21 | NOVO PROGRESSO | PARÁ | Brasil | 1505031 | 15 | 33 | nan | nan | nan | Amazônia | 2.6 |
| fe50371e-cdc3-31dc-bc32-cd2090163694 | -7.26911 | -60.18099 | 2025-07-22 04:51:00 | NOAA-21 | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 5.9 |
| f2e0fffd-cc94-3023-967c-3deaae6ee872 | -7.17801 | -44.14691 | 2025-07-22 04:51:00 | NOAA-21 | ANTÔNIO ALMEIDA | PIAUÍ | Brasil | 2200806 | 22 | 33 | nan | nan | nan | Cerrado | 2.4 |
| 4cbc6a0d-b4a7-374c-981f-6db9306dd21c | -8.6916 | -50.83558 | 2025-07-22 04:51:00 | NOAA-21 | SANTA MARIA DAS BARREIRAS | PARÁ | Brasil | 1506583 | 15 | 33 | nan | nan | nan | Amazônia | 1.1 |
| 3ec7d6b1-2dc7-39d0-9cc2-e3d895da2210 | -5.88656 | -45.2048 | 2025-07-22 04:51:00 | NOAA-21 | BARRA DO CORDA | MARANHÃO | Brasil | 2101608 | 21 | 33 | nan | nan | nan | Cerrado | 4.9 |
| f041125b-ca42-3062-9c81-c933c9fe2023 | -4.2723 | -48.66033 | 2025-07-22 04:51:00 | NOAA-21 | RONDON DO PARÁ | PARÁ | Brasil | 1506187 | 15 | 33 | nan | nan | nan | Amazônia | 0.6 |
| a81bc085-950b-3316-b055-613f714c5170 | -7.97402 | -55.30344 | 2025-07-22 04:51:00 | NOAA-21 | NOVO PROGRESSO | PARÁ | Brasil | 1505031 | 15 | 33 | nan | nan | nan | Amazônia | 1.0 |
| af23e16c-5fd8-355c-adce-5e451d2ef5b3 | -7.20811 | -45.33371 | 2025-07-22 04:51:00 | NOAA-21 | SAMBAÍBA | MARANHÃO | Brasil | 2109700 | 21 | 33 | nan | nan | nan | Cerrado | 3.5 |
| b7474867-491b-388b-9486-cbd733de2c1b | -8.89095 | -50.14998 | 2025-07-22 04:51:00 | NOAA-21 | SANTA MARIA DAS BARREIRAS | PARÁ | Brasil | 1506583 | 15 | 33 | nan | nan | nan | Amazônia | 1.5 |
| ceec4668-6dd6-33dc-83e8-036e8e316672 | -7.14944 | -46.09082 | 2025-07-22 04:51:00 | NOAA-21 | NOVA COLINAS | MARANHÃO | Brasil | 2107258 | 21 | 33 | nan | nan | nan | Cerrado | 1.6 |
| c5beb446-0b12-32c1-8a16-96318bd20fc7 | -9.91788 | -47.82979 | 2025-07-22 04:51:00 | NOAA-21 | NOVO ACORDO | TOCANTINS | Brasil | 1715101 | 17 | 33 | nan | nan | nan | Cerrado | 2.4 |
| a9683dde-b702-3522-b3e8-d60b460c6de6 | -3.97904 | -47.8809 | 2025-07-22 04:51:00 | NOAA-21 | ULIANÓPOLIS | PARÁ | Brasil | 1508126 | 15 | 33 | nan | nan | nan | Amazônia | 0.9 |
| fc92d5c8-6b6b-3346-890b-d552d3ab9edc | -4.54535 | -48.008 | 2025-07-22 04:51:00 | NOAA-21 | RONDON DO PARÁ | PARÁ | Brasil | 1506187 | 15 | 33 | nan | nan | nan | Amazônia | 1.6 |
| 77a5ca11-4c3a-3975-9027-c52c11a73c59 | -7.28472 | -60.17372 | 2025-07-22 04:51:00 | NOAA-21 | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 2.7 |
| 0432f90c-21e8-37f9-b639-3b4b3f5370b6 | -8.58439 | -44.32365 | 2025-07-22 04:51:00 | NOAA-21 | PALMEIRA DO PIAUÍ | PIAUÍ | Brasil | 2207405 | 22 | 33 | nan | nan | nan | Cerrado | 1.4 |
| 1afd80aa-d20c-3936-bf88-83ae497fd94c | -7.23446 | -60.19695 | 2025-07-22 04:51:00 | NOAA-21 | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 1.9 |
| 94614e2e-3519-320b-81d2-29c40650f943 | -10.23179 | -48.06313 | 2025-07-22 04:51:00 | NOAA-21 | PALMAS | TOCANTINS | Brasil | 1721000 | 17 | 33 | nan | nan | nan | Cerrado | 2.1 |
| 177ec414-02e9-3702-be37-9a4220310073 | -7.23864 | -60.19099 | 2025-07-22 04:51:00 | NOAA-21 | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 1.6 |
| a68ce960-805c-3301-a773-7969b15ec385 | -5.8434 | -48.15716 | 2025-07-22 04:51:00 | NOAA-21 | ARAGUATINS | TOCANTINS | Brasil | 1702208 | 17 | 33 | nan | nan | nan | Amazônia | 2.5 |
| 3f02fc60-d00c-3a0e-b8a6-1f4aaa8623d9 | -6.21663 | -57.77528 | 2025-07-22 04:51:00 | NOAA-21 | JACAREACANGA | PARÁ | Brasil | 1503754 | 15 | 33 | nan | nan | nan | Amazônia | 5.4 |
| b9669436-927a-3415-81a5-f7b18b52095f | -3.24725 | -50.25988 | 2025-07-22 04:51:00 | NOAA-21 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 1.1 |
| dbe111f6-5a3b-325c-8ada-16c7c1f2c12d | -10.61427 | -45.23267 | 2025-07-22 04:51:00 | NOAA-21 | CRISTALÂNDIA DO PIAUÍ | PIAUÍ | Brasil | 2203008 | 22 | 33 | nan | nan | nan | Cerrado | 1.7 |
| 3a9f0336-5620-389e-a7b3-3e3d34d9126c | -5.71383 | -51.12377 | 2025-07-22 04:51:00 | NOAA-21 | SÃO FÉLIX DO XINGU | PARÁ | Brasil | 1507300 | 15 | 33 | nan | nan | nan | Amazônia | 0.4 |
| 75d19d3f-c514-33d0-a5e1-4352e97d3d03 | -9.53599 | -58.33844 | 2025-07-22 04:51:00 | NOAA-21 | COTRIGUAÇU | MATO GROSSO | Brasil | 5103379 | 51 | 33 | nan | nan | nan | Amazônia | 0.8 |
| dc8074c6-6cf3-3996-90e2-335bb487178d | -6.57029 | -45.61774 | 2025-07-22 04:51:00 | NOAA-21 | MIRADOR | MARANHÃO | Brasil | 2106706 | 21 | 33 | nan | nan | nan | Cerrado | 1.9 |
| 68286e01-313d-3338-90f1-4709c43b677f | -8.29736 | -44.96215 | 2025-07-22 04:51:00 | NOAA-21 | BAIXA GRANDE DO RIBEIRO | PIAUÍ | Brasil | 2201150 | 22 | 33 | nan | nan | nan | Cerrado | 1.0 |
| af67d28d-1a3e-3288-882a-f2b1f162ae85 | -8.51366 | -43.3095 | 2025-07-22 04:51:00 | NOAA-21 | CANTO DO BURITI | PIAUÍ | Brasil | 2202307 | 22 | 33 | nan | nan | nan | Caatinga | 56.8 |
| 4700b8c8-3ff6-389f-b6e7-982cb7b6d407 | -9.01487 | -59.53603 | 2025-07-22 04:51:00 | NOAA-21 | COLNIZA | MATO GROSSO | Brasil | 5103254 | 51 | 33 | nan | nan | nan | Amazônia | 1.2 |
| 73605ce1-1e0f-38fa-b1bd-084686d2752f | -6.641 | -49.7595 | 2025-07-22 04:51:00 | NOAA-21 | CANAÃ DOS CARAJÁS | PARÁ | Brasil | 1502152 | 15 | 33 | nan | nan | nan | Amazônia | 1.8 |
| c569099f-9aa2-3e32-a616-59ea45b669b6 | -8.29234 | -44.96153 | 2025-07-22 04:51:00 | NOAA-21 | BAIXA GRANDE DO RIBEIRO | PIAUÍ | Brasil | 2201150 | 22 | 33 | nan | nan | nan | Cerrado | 1.0 |
| f1866edf-2d67-3daa-be40-16857c5d7aae | -5.56617 | -45.21189 | 2025-07-22 04:51:00 | NOAA-21 | BARRA DO CORDA | MARANHÃO | Brasil | 2101608 | 21 | 33 | nan | nan | nan | Cerrado | 3.5 |
| b34b0d06-e728-330b-b57f-73a06c44cd0e | -9.50264 | -40.57199 | 2025-07-22 04:51:00 | NOAA-21 | JUAZEIRO | BAHIA | Brasil | 2918407 | 29 | 33 | nan | nan | nan | Caatinga | 3.8 |
| 4793105a-c943-360e-b8d3-402d10d64b84 | -8.30766 | -55.11003 | 2025-07-22 04:51:00 | NOAA-21 | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 0.8 |
| e2b8fabf-bdc1-3dd8-a1fd-83b6f914703b | -9.69031 | -56.1086 | 2025-07-22 04:51:00 | NOAA-21 | ALTA FLORESTA | MATO GROSSO | Brasil | 5100250 | 51 | 33 | nan | nan | nan | Amazônia | 0.8 |
| 63a2a4c7-d322-334a-a80f-3504a8cbcc71 | -4.38604 | -43.29484 | 2025-07-22 04:51:00 | NOAA-21 | ALDEIAS ALTAS | MARANHÃO | Brasil | 2100303 | 21 | 33 | nan | nan | nan | Cerrado | 6.5 |
| e510916f-209e-366c-8016-e3b7d6323164 | -7.25812 | -60.18916 | 2025-07-22 04:51:00 | NOAA-21 | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 3.8 |
| d15c9453-c756-3863-a308-cd037e627567 | -7.97464 | -55.29966 | 2025-07-22 04:51:00 | NOAA-21 | NOVO PROGRESSO | PARÁ | Brasil | 1505031 | 15 | 33 | nan | nan | nan | Amazônia | 1.0 |
| 240b432d-492a-3870-907c-7616d5a94c58 | -7.23996 | -60.19267 | 2025-07-22 04:51:00 | NOAA-21 | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 1.9 |
| 2dce7222-9fe1-3e83-a8da-445911c0efb3 | -9.3365 | -58.83833 | 2025-07-22 04:51:00 | NOAA-21 | COTRIGUAÇU | MATO GROSSO | Brasil | 5103379 | 51 | 33 | nan | nan | nan | Amazônia | 0.8 |
| dae1c5ef-9e75-3d26-9ee0-8192eeabcd27 | -9.33586 | -58.842 | 2025-07-22 04:51:00 | NOAA-21 | COTRIGUAÇU | MATO GROSSO | Brasil | 5103379 | 51 | 33 | nan | nan | nan | Amazônia | 0.9 |
| 8d1128f0-099a-3fe8-8519-0f9761e5db7e | -4.48392 | -46.075 | 2025-07-22 04:51:00 | NOAA-21 | SANTA LUZIA | MARANHÃO | Brasil | 2110005 | 21 | 33 | nan | nan | nan | Amazônia | 1.9 |
| db7070b5-3f32-3e42-9edc-c8231feeb2f0 | -7.27544 | -60.17212 | 2025-07-22 04:51:00 | NOAA-21 | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 4.8 |
| 90c5d101-2a79-3e83-ba6d-eaf9a67281fb | -7.60861 | -49.94391 | 2025-07-22 04:51:00 | NOAA-21 | RIO MARIA | PARÁ | Brasil | 1506161 | 15 | 33 | nan | nan | nan | Amazônia | 0.7 |
| 98402d75-94a1-3e55-af34-b2909288c18e | -3.8269 | -47.73929 | 2025-07-22 04:51:00 | NOAA-21 | ULIANÓPOLIS | PARÁ | Brasil | 1508126 | 15 | 33 | nan | nan | nan | Amazônia | 4.1 |
| 442c0d68-524a-3d6b-9cba-68ef95efcd95 | -5.89059 | -45.21071 | 2025-07-22 04:51:00 | NOAA-21 | BARRA DO CORDA | MARANHÃO | Brasil | 2101608 | 21 | 33 | nan | nan | nan | Cerrado | 3.6 |
| 2710d0ed-94e1-3926-8acc-04b4ce547467 | -7.25897 | -60.18427 | 2025-07-22 04:51:00 | NOAA-21 | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 3.8 |
| 1944707f-c478-3959-8362-64dfc7eb3944 | -11.57112 | -44.84468 | 2025-07-22 04:51:00 | NOAA-21 | RIACHÃO DAS NEVES | BAHIA | Brasil | 2926202 | 29 | 33 | nan | nan | nan | Cerrado | 2.2 |
| 0383f181-f6a6-35ff-9f6b-dc046e9ae9c5 | -5.56643 | -45.2197 | 2025-07-22 04:51:00 | NOAA-21 | BARRA DO CORDA | MARANHÃO | Brasil | 2101608 | 21 | 33 | nan | nan | nan | Cerrado | 5.2 |
| 4514e1b3-d6f8-35c9-8949-ac90e1bd3e0a | -8.51241 | -43.30508 | 2025-07-22 04:51:00 | NOAA-21 | CANTO DO BURITI | PIAUÍ | Brasil | 2202307 | 22 | 33 | nan | nan | nan | Caatinga | 29.8 |
| e81f2ceb-d2c7-3ff3-aaae-345468a62aa2 | -9.06476 | -45.06658 | 2025-07-22 04:51:00 | NOAA-21 | BOM JESUS | PIAUÍ | Brasil | 2201903 | 22 | 33 | nan | nan | nan | Cerrado | 1.8 |
| 4c5c81d2-1db6-3512-9f09-7001a517350e | -3.40703 | -49.53329 | 2025-07-22 04:51:00 | NOAA-21 | BAIÃO | PARÁ | Brasil | 1501204 | 15 | 33 | nan | nan | nan | Amazônia | 1.6 |
| ef11a2be-c98a-344b-b84c-d1a2b61a9e68 | -10.62444 | -45.23413 | 2025-07-22 04:51:00 | NOAA-21 | CRISTALÂNDIA DO PIAUÍ | PIAUÍ | Brasil | 2203008 | 22 | 33 | nan | nan | nan | Cerrado | 2.6 |
| 40bedc35-ee56-32ad-a684-913a01124791 | -9.4959 | -40.57098 | 2025-07-22 04:51:00 | NOAA-21 | JUAZEIRO | BAHIA | Brasil | 2918407 | 29 | 33 | nan | nan | nan | Caatinga | 3.8 |
| 9824b7bc-7571-3d41-8393-79665770e3a1 | -8.08973 | -50.09656 | 2025-07-22 04:51:00 | NOAA-21 | REDENÇÃO | PARÁ | Brasil | 1506138 | 15 | 33 | nan | nan | nan | Amazônia | 3.3 |
| 60ef7f76-2c37-34a8-8e79-9578d9241c73 | -5.0009 | -56.2947 | 2025-07-22 04:51:00 | NOAA-21 | TRAIRÃO | PARÁ | Brasil | 1508050 | 15 | 33 | nan | nan | nan | Amazônia | 1.5 |
| b3660e61-c583-3a58-82a5-d89d1fd50180 | -8.58464 | -44.32247 | 2025-07-22 04:51:00 | NOAA-21 | PALMEIRA DO PIAUÍ | PIAUÍ | Brasil | 2207405 | 22 | 33 | nan | nan | nan | Cerrado | 1.4 |
| c3e7ef98-638b-3dfa-917d-cbc34e643aeb | -4.38073 | -43.29411 | 2025-07-22 04:51:00 | NOAA-21 | ALDEIAS ALTAS | MARANHÃO | Brasil | 2100303 | 21 | 33 | nan | nan | nan | Cerrado | 5.8 |
| 4ba689d4-9d51-34c1-9fcc-adc81c4a555e | -9.49406 | -40.56325 | 2025-07-22 04:51:00 | NOAA-21 | JUAZEIRO | BAHIA | Brasil | 2918407 | 29 | 33 | nan | nan | nan | Caatinga | 4.9 |
| 95470894-bf38-3813-983a-1016aff12f9b | -8.10421 | -46.82434 | 2025-07-22 04:51:00 | NOAA-21 | CAMPOS LINDOS | TOCANTINS | Brasil | 1703842 | 17 | 33 | nan | nan | nan | Cerrado | 2.0 |
| 9863c346-b7c4-3fcd-862a-93d7c2387285 | -9.06515 | -45.06366 | 2025-07-22 04:51:00 | NOAA-21 | BOM JESUS | PIAUÍ | Brasil | 2201903 | 22 | 33 | nan | nan | nan | Cerrado | 1.8 |
| df8e0ae0-f585-3826-ba46-d0dbfa02a0aa | -7.29022 | -60.16956 | 2025-07-22 04:51:00 | NOAA-21 | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 2.8 |
| bd7ef971-d4ce-36fd-b68e-5a5ac5d95c44 | -7.28007 | -60.17294 | 2025-07-22 04:51:00 | NOAA-21 | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 2.7 |
| 4aef4883-3b88-3057-8a55-f8f51524044c | -4.82263 | -47.31614 | 2025-07-22 04:51:00 | NOAA-21 | AÇAILÂNDIA | MARANHÃO | Brasil | 2100055 | 21 | 33 | nan | nan | nan | Amazônia | 2.1 |
| 689349ec-929c-31d9-b27b-020827c4d67e | -7.2872 | -44.35984 | 2025-07-22 04:51:00 | NOAA-21 | URUÇUÍ | PIAUÍ | Brasil | 2211209 | 22 | 33 | nan | nan | nan | Cerrado | 1.4 |
| 5753f317-f21b-39cd-a0d3-8ed71851da51 | -8.51852 | -43.30203 | 2025-07-22 04:51:00 | NOAA-21 | CANTO DO BURITI | PIAUÍ | Brasil | 2202307 | 22 | 33 | nan | nan | nan | Caatinga | 14.4 |
| 6c55e497-9598-3401-88bf-c9489e0cba3f | -8.58401 | -55.33491 | 2025-07-22 04:51:00 | NOAA-21 | NOVO PROGRESSO | PARÁ | Brasil | 1505031 | 15 | 33 | nan | nan | nan | Amazônia | 0.7 |
| 7017a05e-1354-3913-aee5-c3b95bc293dd | -4.59701 | -43.31982 | 2025-07-22 04:51:00 | NOAA-21 | ALDEIAS ALTAS | MARANHÃO | Brasil | 2100303 | 21 | 33 | nan | nan | nan | Cerrado | 1.7 |
| f7c3210c-1cf7-37eb-a7f2-80441cb39a3e | -7.26446 | -60.18023 | 2025-07-22 04:51:00 | NOAA-21 | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 5.1 |
| 00bd7096-75dc-3f09-9495-da27eeca836a | -6.97745 | -42.80045 | 2025-07-22 04:51:00 | NOAA-21 | NAZARÉ DO PIAUÍ | PIAUÍ | Brasil | 2206704 | 22 | 33 | nan | nan | nan | Caatinga | 2.0 |
| b5ab1cc5-0ccd-3d4b-a9a8-200f0a1390e2 | -7.35964 | -50.81437 | 2025-07-22 04:51:00 | NOAA-21 | BANNACH | PARÁ | Brasil | 1501253 | 15 | 33 | nan | nan | nan | Amazônia | 0.6 |
| bf7def1a-5409-3e73-8f52-6504558679ac | -4.68043 | -48.26873 | 2025-07-22 04:51:00 | NOAA-21 | RONDON DO PARÁ | PARÁ | Brasil | 1506187 | 15 | 33 | nan | nan | nan | Amazônia | 2.6 |
| bdd3c767-aea1-3450-8bc5-31661ff08d5b | -7.23775 | -60.19603 | 2025-07-22 04:51:00 | NOAA-21 | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 1.6 |
| a517f4ce-ed13-3204-9156-129c1e552212 | -8.91378 | -47.35818 | 2025-07-22 04:51:00 | NOAA-21 | CENTENÁRIO | TOCANTINS | Brasil | 1704105 | 17 | 33 | nan | nan | nan | Cerrado | 1.2 |
| a17b32e1-127f-38de-9ba0-bd56362ecd45 | -10.55872 | -50.37897 | 2025-07-22 04:51:00 | NOAA-21 | PIUM | TOCANTINS | Brasil | 1717503 | 17 | 33 | nan | nan | nan | Cerrado | 5.0 |
| b8e127a7-0f05-3446-86b5-4280e85ceb0b | -8.89456 | -50.15051 | 2025-07-22 04:51:00 | NOAA-21 | SANTA MARIA DAS BARREIRAS | PARÁ | Brasil | 1506583 | 15 | 33 | nan | nan | nan | Amazônia | 1.2 |
| 1bae3496-69aa-3c0f-863e-6cec64188735 | -3.24668 | -50.26355 | 2025-07-22 04:51:00 | NOAA-21 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 0.9 |
| 99c54df8-32c1-3c93-ad96-4117d3faecfe | -7.25432 | -60.1835 | 2025-07-22 04:51:00 | NOAA-21 | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 2.4 |
| d97d652a-d99c-368f-8495-36448f3796bd | -7.23308 | -60.19534 | 2025-07-22 04:51:00 | NOAA-21 | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 2.2 |
| 3078f702-cea8-3d56-84e1-f07849905a77 | -8.08674 | -50.09203 | 2025-07-22 04:51:00 | NOAA-21 | REDENÇÃO | PARÁ | Brasil | 1506138 | 15 | 33 | nan | nan | nan | Amazônia | 2.0 |
| 9f0cb7f9-fe61-3675-8051-4e4a4e01e539 | -8.87888 | -50.15676 | 2025-07-22 04:51:00 | NOAA-21 | SANTA MARIA DAS BARREIRAS | PARÁ | Brasil | 1506583 | 15 | 33 | nan | nan | nan | Amazônia | 7.3 |
| 7f12b982-d87c-31cc-8ea6-a8f20ad7ba53 | -5.13573 | -60.36341 | 2025-07-22 04:51:00 | NOAA-21 | NOVO ARIPUANÃ | AMAZONAS | Brasil | 1303304 | 13 | 33 | nan | nan | nan | Amazônia | 3.1 |
| a2764af9-b86c-38ce-af07-04f822d0e776 | -7.14326 | -46.09685 | 2025-07-22 04:51:00 | NOAA-21 | NOVA COLINAS | MARANHÃO | Brasil | 2107258 | 21 | 33 | nan | nan | nan | Cerrado | 2.4 |
| 8cfaffc2-441b-32f0-aa7b-60f082192d0c | -6.64459 | -49.76004 | 2025-07-22 04:51:00 | NOAA-21 | CANAÃ DOS CARAJÁS | PARÁ | Brasil | 1502152 | 15 | 33 | nan | nan | nan | Amazônia | 1.8 |
| 36800971-df52-33ef-8bdb-87d8eb10da6f | -4.31969 | -47.98835 | 2025-07-22 04:51:00 | NOAA-21 | DOM ELISEU | PARÁ | Brasil | 1502939 | 15 | 33 | nan | nan | nan | Amazônia | 2.5 |
| b29f90ac-0499-3430-a14c-0801a263c2ea | -5.56467 | -45.22202 | 2025-07-22 04:51:00 | NOAA-21 | BARRA DO CORDA | MARANHÃO | Brasil | 2101608 | 21 | 33 | nan | nan | nan | Cerrado | 2.8 |
| 5025c09c-4141-3135-a0c5-619e259406ea | -7.24881 | -60.18764 | 2025-07-22 04:51:00 | NOAA-21 | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 2.4 |
| 487f4da2-76d1-379a-b6b1-7667b4264215 | -8.09035 | -50.09244 | 2025-07-22 04:51:00 | NOAA-21 | REDENÇÃO | PARÁ | Brasil | 1506138 | 15 | 33 | nan | nan | nan | Amazônia | 2.0 |
| 90254691-0748-3cf8-9e75-83a27f209ae6 | -6.57337 | -45.61551 | 2025-07-22 04:51:00 | NOAA-21 | MIRADOR | MARANHÃO | Brasil | 2106706 | 21 | 33 | nan | nan | nan | Cerrado | 1.6 |
| 7b58866d-07e5-32eb-8c54-28cc9d7f42cd | -4.34646 | -55.77313 | 2025-07-22 04:51:00 | NOAA-21 | ITAITUBA | PARÁ | Brasil | 1503606 | 15 | 33 | nan | nan | nan | Amazônia | 1.6 |
| e5b47c95-e613-34b0-9aa6-46215ebb61d8 | -7.28036 | -50.32496 | 2025-07-22 04:51:00 | NOAA-21 | RIO MARIA | PARÁ | Brasil | 1506161 | 15 | 33 | nan | nan | nan | Amazônia | 0.4 |
| cd18ca43-1b90-3e73-a8c7-34ddb17220bd | -8.47423 | -49.60315 | 2025-07-22 04:51:00 | NOAA-21 | CONCEIÇÃO DO ARAGUAIA | PARÁ | Brasil | 1502707 | 15 | 33 | nan | nan | nan | Amazônia | 1.3 |


[Clique aqui para ver as próximas entradas](README14.md)
