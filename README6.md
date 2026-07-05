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
| 77d56ffc-68b7-3c27-a9b5-af96058dbc08 | -20.58787 | -43.89394 | 2026-07-05 04:29:00 | NOAA-21 | CONGONHAS | MINAS GERAIS | Brasil | 3118007 | 31 | 33 | nan | nan | nan | Mata Atlântica | 0.7 |
| bbb661dd-ad3a-323d-aab6-b06a29adf5e8 | -17.00691 | -48.28518 | 2026-07-05 04:29:00 | NOAA-21 | ORIZONA | GOIÁS | Brasil | 5215306 | 52 | 33 | nan | nan | nan | Cerrado | 2.3 |
| 110c0d3f-3417-3750-8b27-dd1a448f918e | -16.48677 | -48.98103 | 2026-07-05 04:29:00 | NOAA-21 | LEOPOLDO DE BULHÕES | GOIÁS | Brasil | 5212303 | 52 | 33 | nan | nan | nan | Cerrado | 0.6 |
| 8c1f1ee4-bb35-3a2a-b5a4-854675207a4f | -17.79724 | -50.60442 | 2026-07-05 04:29:00 | NOAA-21 | SANTA HELENA DE GOIÁS | GOIÁS | Brasil | 5219308 | 52 | 33 | nan | nan | nan | Cerrado | 0.4 |
| 67133c3a-5f6d-3d2b-bf16-b2242161a511 | -18.56 | -41.20308 | 2026-07-05 04:29:00 | NOAA-21 | ITABIRINHA | MINAS GERAIS | Brasil | 3131802 | 31 | 33 | nan | nan | nan | Mata Atlântica | 0.9 |
| 53d20f4c-b6bf-3174-b2ad-f4caa53074fa | -17.68998 | -48.63929 | 2026-07-05 04:29:00 | NOAA-21 | CALDAS NOVAS | GOIÁS | Brasil | 5204508 | 52 | 33 | nan | nan | nan | Cerrado | 1.6 |
| f80445ab-05ca-30ee-8bb6-ee1e62686dc9 | -18.52303 | -42.72948 | 2026-07-05 04:29:00 | NOAA-21 | SÃO JOÃO EVANGELISTA | MINAS GERAIS | Brasil | 3162807 | 31 | 33 | nan | nan | nan | Mata Atlântica | 0.7 |
| 83716940-113c-3c84-b3ae-58eee752df50 | -20.12763 | -41.30728 | 2026-07-05 04:29:00 | NOAA-21 | BREJETUBA | ESPÍRITO SANTO | Brasil | 3201159 | 32 | 33 | nan | nan | nan | Mata Atlântica | 3.6 |
| 430c3cc1-7192-3000-8fd4-e82de1dad3c7 | -16.1614 | -48.10183 | 2026-07-05 04:29:00 | NOAA-21 | NOVO GAMA | GOIÁS | Brasil | 5215231 | 52 | 33 | nan | nan | nan | Cerrado | 0.9 |
| 89a848cc-1473-301f-bfe8-175fba22762d | -10.9401 | -43.0355 | 2026-07-05 04:30:00 | GOES-19 | BARRA | BAHIA | Brasil | 2902708 | 29 | 33 | nan | nan | nan | Cerrado | 231.4 |
| a5fe93ae-05bc-32f5-b019-179290d5f15b | -10.9397 | -43.0593 | 2026-07-05 04:30:00 | GOES-19 | BARRA | BAHIA | Brasil | 2902708 | 29 | 33 | nan | nan | nan | Cerrado | 88.8 |
| 9012339a-12c6-3541-805d-5fa8b2b72f1c | -10.9209 | -43.0384 | 2026-07-05 04:30:00 | GOES-19 | BARRA | BAHIA | Brasil | 2902708 | 29 | 33 | nan | nan | nan | Cerrado | 57.3 |
| 700de618-b536-384d-a7b7-23ddafaf6d1e | -21.28918 | -56.87409 | 2026-07-05 04:32:00 | NOAA-21 | PORTO MURTINHO | MATO GROSSO DO SUL | Brasil | 5006903 | 50 | 33 | nan | nan | nan | Cerrado | 0.7 |
| 6a57d0e9-31a3-3dbf-a65e-2762f2bbe7ee | -21.29123 | -56.87711 | 2026-07-05 04:32:00 | NOAA-21 | PORTO MURTINHO | MATO GROSSO DO SUL | Brasil | 5006903 | 50 | 33 | nan | nan | nan | Cerrado | 0.8 |
| f9537b93-70c8-32e0-9e17-ef40fd91c9d8 | -10.9397 | -43.0593 | 2026-07-05 04:40:00 | GOES-19 | BARRA | BAHIA | Brasil | 2902708 | 29 | 33 | nan | nan | nan | Cerrado | 97.9 |
| 3c4deb6c-2d95-3630-a8e5-6389a2615c66 | -10.9209 | -43.0384 | 2026-07-05 04:40:00 | GOES-19 | BARRA | BAHIA | Brasil | 2902708 | 29 | 33 | nan | nan | nan | Cerrado | 51.9 |
| c2e7482f-4177-300b-a308-d3fc70693421 | -10.9401 | -43.0355 | 2026-07-05 04:40:00 | GOES-19 | BARRA | BAHIA | Brasil | 2902708 | 29 | 33 | nan | nan | nan | Cerrado | 193.8 |
| 95a8c434-f378-378b-abf6-cab548d0cd67 | -10.9401 | -43.0355 | 2026-07-05 04:50:00 | GOES-19 | BARRA | BAHIA | Brasil | 2902708 | 29 | 33 | nan | nan | nan | Cerrado | 198.9 |
| 174395af-f97f-3162-964a-625073238579 | -10.9397 | -43.0593 | 2026-07-05 04:50:00 | GOES-19 | BARRA | BAHIA | Brasil | 2902708 | 29 | 33 | nan | nan | nan | Cerrado | 77.9 |
| e14a4dad-c2ec-3066-b6bc-d176fb8a8eac | -10.9401 | -43.0355 | 2026-07-05 05:00:00 | GOES-19 | BARRA | BAHIA | Brasil | 2902708 | 29 | 33 | nan | nan | nan | Cerrado | 144.7 |
| a517dbf9-a518-3f9a-bda3-4240cd05e88a | -10.9397 | -43.0593 | 2026-07-05 05:00:00 | GOES-19 | BARRA | BAHIA | Brasil | 2902708 | 29 | 33 | nan | nan | nan | Cerrado | 52.6 |
| 2193669d-70b1-3933-bb3b-7194dc0fb4f6 | -10.9209 | -43.0384 | 2026-07-05 05:00:00 | GOES-19 | BARRA | BAHIA | Brasil | 2902708 | 29 | 33 | nan | nan | nan | Cerrado | 59.1 |
| c33004c7-045f-30b1-9b8b-df9cacd52d2f | -9.63449 | -47.3482 | 2026-07-05 05:01:00 | NPP-375D | RIO SONO | TOCANTINS | Brasil | 1718758 | 17 | 33 | nan | nan | nan | Cerrado | 0.9 |
| 8bbfdf8f-021a-36ed-b09b-6bfe54f9136a | -7.40578 | -46.8293 | 2026-07-05 05:01:00 | NPP-375D | RIACHÃO | MARANHÃO | Brasil | 2109502 | 21 | 33 | nan | nan | nan | Cerrado | 1.1 |
| 5f45dd8d-c9e5-3cfc-8510-e02e5c06f6b3 | -8.71931 | -54.54859 | 2026-07-05 05:01:00 | NPP-375D | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 1.3 |
| 53d5daf0-0c86-3e0f-89fd-661fead40b66 | -8.89707 | -47.7698 | 2026-07-05 05:01:00 | NPP-375D | SANTA MARIA DO TOCANTINS | TOCANTINS | Brasil | 1718881 | 17 | 33 | nan | nan | nan | Cerrado | 1.2 |
| 0dea0ade-e271-3a03-92c3-b1207abcf197 | -9.26921 | -50.45046 | 2026-07-05 05:01:00 | NPP-375D | SANTANA DO ARAGUAIA | PARÁ | Brasil | 1506708 | 15 | 33 | nan | nan | nan | Amazônia | 1.8 |
| 9797e3e6-63ac-39dd-92c0-7b44aa25cb00 | -6.42792 | -55.79822 | 2026-07-05 05:01:00 | NPP-375D | ITAITUBA | PARÁ | Brasil | 1503606 | 15 | 33 | nan | nan | nan | Amazônia | 2.7 |
| 30f73bb5-ac6f-3a68-aad4-f51ef10f53b8 | -8.71816 | -54.55577 | 2026-07-05 05:01:00 | NPP-375D | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 1.0 |
| 36acd86b-df6c-39ab-bbe6-9a9f18fe7801 | -6.90464 | -43.71755 | 2026-07-05 05:01:00 | NPP-375D | GUADALUPE | PIAUÍ | Brasil | 2204501 | 22 | 33 | nan | nan | nan | Cerrado | 1.9 |
| f1c4ccad-7063-342a-9d68-c98f62d1f66a | -6.89665 | -43.71247 | 2026-07-05 05:01:00 | NPP-375D | GUADALUPE | PIAUÍ | Brasil | 2204501 | 22 | 33 | nan | nan | nan | Cerrado | 2.6 |
| 5e7665e1-b0da-3097-a025-ac26f6c6fd48 | -6.93886 | -43.72563 | 2026-07-05 05:01:00 | NPP-375D | GUADALUPE | PIAUÍ | Brasil | 2204501 | 22 | 33 | nan | nan | nan | Cerrado | 2.8 |
| c41c99c9-ea62-3040-ae3a-c9c645f687ad | -10.92756 | -43.04221 | 2026-07-05 05:01:00 | NPP-375D | BARRA | BAHIA | Brasil | 2902708 | 29 | 33 | nan | nan | nan | Cerrado | 6.8 |
| 60d52733-5b04-33a7-9a3c-278537e2d9f2 | -6.10445 | -49.34403 | 2026-07-05 05:01:00 | NPP-375D | ELDORADO DO CARAJÁS | PARÁ | Brasil | 1502954 | 15 | 33 | nan | nan | nan | Amazônia | 1.4 |
| 1b439f20-9751-3619-ac68-81180ae0de38 | -7.02741 | -55.44014 | 2026-07-05 05:01:00 | NPP-375D | NOVO PROGRESSO | PARÁ | Brasil | 1505031 | 15 | 33 | nan | nan | nan | Amazônia | 1.0 |
| ae5266b5-8f90-350a-934b-e043b58e772b | -3.81901 | -50.63227 | 2026-07-05 05:01:00 | NPP-375D | PACAJÁ | PARÁ | Brasil | 1505486 | 15 | 33 | nan | nan | nan | Amazônia | 0.4 |
| c0682dda-f03d-37b4-896e-5d67a7d8f4ee | -6.89081 | -43.71503 | 2026-07-05 05:01:00 | NPP-375D | GUADALUPE | PIAUÍ | Brasil | 2204501 | 22 | 33 | nan | nan | nan | Cerrado | 0.5 |
| 740fa48f-dc63-3106-a40e-36ca63881e4b | -6.90203 | -43.71337 | 2026-07-05 05:01:00 | NPP-375D | GUADALUPE | PIAUÍ | Brasil | 2204501 | 22 | 33 | nan | nan | nan | Cerrado | 2.6 |
| 3298e691-b3c6-37e2-a9c0-13ad2639a24a | -8.0553 | -46.70034 | 2026-07-05 05:01:00 | NPP-375D | CAMPOS LINDOS | TOCANTINS | Brasil | 1703842 | 17 | 33 | nan | nan | nan | Cerrado | 2.1 |
| 129c4831-e521-377b-8fce-298f6710bbda | -8.13874 | -47.11572 | 2026-07-05 05:01:00 | NPP-375D | GOIATINS | TOCANTINS | Brasil | 1709005 | 17 | 33 | nan | nan | nan | Cerrado | 1.5 |
| 39538f6a-61f8-3796-affe-c69e7e56fbff | -7.9025 | -48.25219 | 2026-07-05 05:01:00 | NPP-375D | PALMEIRANTE | TOCANTINS | Brasil | 1715705 | 17 | 33 | nan | nan | nan | Cerrado | 1.4 |
| 7e534598-f223-3b7c-ac7f-925a0cd9e11c | -3.21649 | -53.02476 | 2026-07-05 05:01:00 | NPP-375D | MEDICILÂNDIA | PARÁ | Brasil | 1504455 | 15 | 33 | nan | nan | nan | Amazônia | 1.4 |
| 394222b5-8b46-3432-bcc6-644ed38b715e | -6.93441 | -43.71805 | 2026-07-05 05:01:00 | NPP-375D | GUADALUPE | PIAUÍ | Brasil | 2204501 | 22 | 33 | nan | nan | nan | Cerrado | 1.9 |
| 7ec54ef6-056d-3627-8146-0893934557f1 | -6.90512 | -43.71417 | 2026-07-05 05:01:00 | NPP-375D | GUADALUPE | PIAUÍ | Brasil | 2204501 | 22 | 33 | nan | nan | nan | Cerrado | 1.9 |
| 77589e17-8e3e-3308-9750-9e712efcac73 | -8.90073 | -47.77434 | 2026-07-05 05:01:00 | NPP-375D | SANTA MARIA DO TOCANTINS | TOCANTINS | Brasil | 1718881 | 17 | 33 | nan | nan | nan | Cerrado | 1.2 |
| ca0854ab-ab96-31f0-a488-abb829d866ad | -6.99097 | -55.8887 | 2026-07-05 05:01:00 | NPP-375D | NOVO PROGRESSO | PARÁ | Brasil | 1505031 | 15 | 33 | nan | nan | nan | Amazônia | 3.2 |
| 2a3607e8-2c0d-3d84-a1ac-c8c1560b62e3 | -6.90157 | -43.71678 | 2026-07-05 05:01:00 | NPP-375D | GUADALUPE | PIAUÍ | Brasil | 2204501 | 22 | 33 | nan | nan | nan | Cerrado | 2.6 |
| fa237f21-5334-3c73-b651-96e0aa2d8e3c | -7.90702 | -48.24932 | 2026-07-05 05:01:00 | NPP-375D | PALMEIRANTE | TOCANTINS | Brasil | 1715705 | 17 | 33 | nan | nan | nan | Cerrado | 1.6 |
| 6404ff7c-50a2-34bc-a079-6b32dcc8fc89 | -4.50208 | -50.92599 | 2026-07-05 05:01:00 | NPP-375D | ANAPU | PARÁ | Brasil | 1500859 | 15 | 33 | nan | nan | nan | Amazônia | 0.6 |
| 2f613e27-8d3f-3f9f-a7de-592b31dc3bce | -8.08273 | -46.7 | 2026-07-05 05:01:00 | NPP-375D | CAMPOS LINDOS | TOCANTINS | Brasil | 1703842 | 17 | 33 | nan | nan | nan | Cerrado | 0.6 |
| 5588df59-5131-3a7a-9633-5fa47c4bc034 | -6.42499 | -55.79355 | 2026-07-05 05:01:00 | NPP-375D | ITAITUBA | PARÁ | Brasil | 1503606 | 15 | 33 | nan | nan | nan | Amazônia | 0.7 |
| bcd85b09-4a69-3558-87c5-88a7eedfe643 | -8.89665 | -47.77083 | 2026-07-05 05:01:00 | NPP-375D | SANTA MARIA DO TOCANTINS | TOCANTINS | Brasil | 1718881 | 17 | 33 | nan | nan | nan | Cerrado | 0.9 |
| 00bd7eba-8fe2-3140-bd29-bdc45eb5d21b | -5.52279 | -50.02396 | 2026-07-05 05:01:00 | NPP-375D | MARABÁ | PARÁ | Brasil | 1504208 | 15 | 33 | nan | nan | nan | Amazônia | 0.8 |
| 1c7078a0-69cb-34c5-b150-ebb9260608c1 | -6.89925 | -43.71671 | 2026-07-05 05:01:00 | NPP-375D | GUADALUPE | PIAUÍ | Brasil | 2204501 | 22 | 33 | nan | nan | nan | Cerrado | 1.9 |
| abb4d8f9-d9dd-35ce-a4dd-60db1f4124ff | -7.92001 | -45.43342 | 2026-07-05 05:01:00 | NPP-375D | RIBEIRO GONÇALVES | PIAUÍ | Brasil | 2208908 | 22 | 33 | nan | nan | nan | Cerrado | 1.7 |
| a27a78c1-bec0-3712-ace4-c241e15dca4b | -6.89436 | -43.71243 | 2026-07-05 05:01:00 | NPP-375D | GUADALUPE | PIAUÍ | Brasil | 2204501 | 22 | 33 | nan | nan | nan | Cerrado | 1.8 |
| c0e302ee-5bad-39fc-8c6a-35015915b8c4 | -7.38751 | -55.49213 | 2026-07-05 05:01:00 | NPP-375D | NOVO PROGRESSO | PARÁ | Brasil | 1505031 | 15 | 33 | nan | nan | nan | Amazônia | 0.9 |
| 6d3048a6-6a47-3bdb-b973-75e587b04274 | -9.26983 | -50.44632 | 2026-07-05 05:01:00 | NPP-375D | SANTANA DO ARAGUAIA | PARÁ | Brasil | 1506708 | 15 | 33 | nan | nan | nan | Amazônia | 1.0 |
| 2491ec3a-6fa9-3e7d-b965-716283a60d51 | -5.27256 | -49.33444 | 2026-07-05 05:01:00 | NPP-375D | MARABÁ | PARÁ | Brasil | 1504208 | 15 | 33 | nan | nan | nan | Amazônia | 0.6 |
| 59965c99-6779-38d5-b820-63c12599d7f9 | -5.2762 | -49.33501 | 2026-07-05 05:01:00 | NPP-375D | MARABÁ | PARÁ | Brasil | 1504208 | 15 | 33 | nan | nan | nan | Amazônia | 1.4 |
| 78057d11-8722-30a5-843a-ae93e22d313d | -6.98878 | -55.89128 | 2026-07-05 05:01:00 | NPP-375D | NOVO PROGRESSO | PARÁ | Brasil | 1505031 | 15 | 33 | nan | nan | nan | Amazônia | 2.0 |
| dbc26297-ca10-349e-a4bc-3abee0fe272a | -5.93645 | -45.38643 | 2026-07-05 05:01:00 | NPP-375D | FERNANDO FALCÃO | MARANHÃO | Brasil | 2104081 | 21 | 33 | nan | nan | nan | Cerrado | 0.8 |
| 0c5c1dcf-86c2-38ca-9ceb-f9ef95925b83 | -6.42858 | -55.79413 | 2026-07-05 05:01:00 | NPP-375D | ITAITUBA | PARÁ | Brasil | 1503606 | 15 | 33 | nan | nan | nan | Amazônia | 0.7 |
| b87085f4-b253-36c3-b78d-04e84f720073 | -8.9447 | -44.2118 | 2026-07-05 05:01:00 | NPP-375D | SANTA LUZ | PIAUÍ | Brasil | 2209302 | 22 | 33 | nan | nan | nan | Cerrado | 1.8 |
| 6f0d510d-470d-3c86-88db-20b14f4fadf3 | -6.89387 | -43.71585 | 2026-07-05 05:01:00 | NPP-375D | GUADALUPE | PIAUÍ | Brasil | 2204501 | 22 | 33 | nan | nan | nan | Cerrado | 1.8 |
| 5b54df92-3722-323c-b00e-8fa97dfec5f1 | -6.99304 | -55.88783 | 2026-07-05 05:01:00 | NPP-375D | NOVO PROGRESSO | PARÁ | Brasil | 1505031 | 15 | 33 | nan | nan | nan | Amazônia | 0.7 |
| 61ad526f-0742-3e75-877c-07d5657283e3 | -7.02391 | -55.43952 | 2026-07-05 05:01:00 | NPP-375D | NOVO PROGRESSO | PARÁ | Brasil | 1505031 | 15 | 33 | nan | nan | nan | Amazônia | 1.0 |
| 41e561a1-29f0-3c7b-a45c-36d687b06237 | -8.14852 | -47.10927 | 2026-07-05 05:01:00 | NPP-375D | GOIATINS | TOCANTINS | Brasil | 1709005 | 17 | 33 | nan | nan | nan | Cerrado | 1.0 |
| 1624b1ac-6f58-33ef-9b94-a341b60bf9ad | -6.93488 | -43.71461 | 2026-07-05 05:01:00 | NPP-375D | GUADALUPE | PIAUÍ | Brasil | 2204501 | 22 | 33 | nan | nan | nan | Cerrado | 2.0 |
| d1e194b3-619e-354d-8a76-b4edb0589c8a | -9.45339 | -51.82506 | 2026-07-05 05:01:00 | NPP-375D | SÃO FÉLIX DO XINGU | PARÁ | Brasil | 1507300 | 15 | 33 | nan | nan | nan | Amazônia | 1.1 |
| 89d2af28-d5db-3bb0-b325-3771dea4d039 | -10.927 | -43.04654 | 2026-07-05 05:01:00 | NPP-375D | BARRA | BAHIA | Brasil | 2902708 | 29 | 33 | nan | nan | nan | Cerrado | 5.8 |
| d27b3ea0-5a27-3660-bf02-e459e6e2f005 | -3.21314 | -53.02423 | 2026-07-05 05:01:00 | NPP-375D | MEDICILÂNDIA | PARÁ | Brasil | 1504455 | 15 | 33 | nan | nan | nan | Amazônia | 0.8 |
| deab4495-67fd-358c-a0b8-5c27e1d5cb92 | -7.91521 | -45.43229 | 2026-07-05 05:01:00 | NPP-375D | RIBEIRO GONÇALVES | PIAUÍ | Brasil | 2208908 | 22 | 33 | nan | nan | nan | Cerrado | 1.7 |
| 2de69474-fb23-33fa-858b-db1232669c6a | -5.86884 | -51.73927 | 2026-07-05 05:01:00 | NPP-375D | SÃO FÉLIX DO XINGU | PARÁ | Brasil | 1507300 | 15 | 33 | nan | nan | nan | Amazônia | 7.1 |
| 5203d112-3dfd-3852-a613-976b72227faf | -6.89619 | -43.7159 | 2026-07-05 05:01:00 | NPP-375D | GUADALUPE | PIAUÍ | Brasil | 2204501 | 22 | 33 | nan | nan | nan | Cerrado | 2.6 |
| 91c46edb-9e9e-3d79-90fa-552d258638fe | -3.21593 | -53.02826 | 2026-07-05 05:01:00 | NPP-375D | MEDICILÂNDIA | PARÁ | Brasil | 1504455 | 15 | 33 | nan | nan | nan | Amazônia | 1.4 |
| 36373159-9f0c-3fbd-b5cc-f0a8828a6290 | -6.93933 | -43.72223 | 2026-07-05 05:01:00 | NPP-375D | GUADALUPE | PIAUÍ | Brasil | 2204501 | 22 | 33 | nan | nan | nan | Cerrado | 1.6 |
| b73002af-c30f-3888-b7a9-4509020f72ca | -6.89974 | -43.71331 | 2026-07-05 05:01:00 | NPP-375D | GUADALUPE | PIAUÍ | Brasil | 2204501 | 22 | 33 | nan | nan | nan | Cerrado | 1.9 |
| 956b62fe-dc11-3b7c-90b7-629d799a70fd | -8.08719 | -46.70076 | 2026-07-05 05:01:00 | NPP-375D | CAMPOS LINDOS | TOCANTINS | Brasil | 1703842 | 17 | 33 | nan | nan | nan | Cerrado | 0.6 |
| 1cffdc65-e86b-341a-bb59-2a710084db99 | -7.90753 | -48.24585 | 2026-07-05 05:01:00 | NPP-375D | PALMEIRANTE | TOCANTINS | Brasil | 1715705 | 17 | 33 | nan | nan | nan | Cerrado | 1.6 |
| 67785bd9-8f67-338d-8055-38a06329f8d5 | -1.96297 | -54.05951 | 2026-07-05 05:01:00 | NPP-375D | MONTE ALEGRE | PARÁ | Brasil | 1504802 | 15 | 33 | nan | nan | nan | Amazônia | 1.0 |
| dad84638-6fe4-3585-a35b-12f5aec0574a | -6.98947 | -55.88718 | 2026-07-05 05:01:00 | NPP-375D | NOVO PROGRESSO | PARÁ | Brasil | 1505031 | 15 | 33 | nan | nan | nan | Amazônia | 1.8 |
| 56df2d38-fb22-31d8-8d0d-978215b526d7 | -5.86939 | -51.73574 | 2026-07-05 05:01:00 | NPP-375D | SÃO FÉLIX DO XINGU | PARÁ | Brasil | 1507300 | 15 | 33 | nan | nan | nan | Amazônia | 2.1 |
| e2b3d411-ac5c-32a1-bfe0-50f80099d89b | -6.93981 | -43.7188 | 2026-07-05 05:01:00 | NPP-375D | GUADALUPE | PIAUÍ | Brasil | 2204501 | 22 | 33 | nan | nan | nan | Cerrado | 1.6 |
| 7c46bb7c-0eb0-36db-88d6-a38b9b711e8f | -7.40642 | -46.82497 | 2026-07-05 05:01:00 | NPP-375D | RIACHÃO | MARANHÃO | Brasil | 2109502 | 21 | 33 | nan | nan | nan | Cerrado | 0.4 |
| 4972177d-f81a-3cbf-b161-4aefeabb156f | -8.08434 | -46.70239 | 2026-07-05 05:01:00 | NPP-375D | CAMPOS LINDOS | TOCANTINS | Brasil | 1703842 | 17 | 33 | nan | nan | nan | Cerrado | 1.9 |
| 3db92fa4-677c-3f22-b65b-f5aec1967072 | -11.4552 | -46.54838 | 2026-07-05 05:04:00 | NPP-375D | DIANÓPOLIS | TOCANTINS | Brasil | 1707009 | 17 | 33 | nan | nan | nan | Cerrado | 2.0 |
| 27ff77ff-680b-36a8-905e-2752d0a90b33 | -11.9242 | -43.38584 | 2026-07-05 05:04:00 | NPP-375D | MUQUÉM DO SÃO FRANCISCO | BAHIA | Brasil | 2922250 | 29 | 33 | nan | nan | nan | Cerrado | 1.3 |
| 29c1e98d-b540-3141-98a4-c87b12f604fa | -11.66562 | -46.75422 | 2026-07-05 05:04:00 | NPP-375D | DIANÓPOLIS | TOCANTINS | Brasil | 1707009 | 17 | 33 | nan | nan | nan | Cerrado | 1.0 |
| be5d8dbf-322c-34fe-ac70-18e29eb24d17 | -13.22383 | -54.33035 | 2026-07-05 05:04:00 | NPP-375D | PARANATINGA | MATO GROSSO | Brasil | 5106307 | 51 | 33 | nan | nan | nan | Amazônia | 0.9 |
| 926d6631-b8c3-3182-b042-f8b529004d82 | -10.90314 | -56.85271 | 2026-07-05 05:04:00 | NPP-375D | JUARA | MATO GROSSO | Brasil | 5105101 | 51 | 33 | nan | nan | nan | Amazônia | 1.2 |
| 59b45609-22c7-358b-b3df-0b2f807b626d | -13.24157 | -54.32601 | 2026-07-05 05:04:00 | NPP-375D | PARANATINGA | MATO GROSSO | Brasil | 5106307 | 51 | 33 | nan | nan | nan | Amazônia | 2.0 |
| 7743bf98-0a39-3846-b34b-a3e971dc5650 | -13.20108 | -54.30874 | 2026-07-05 05:04:00 | NPP-375D | PARANATINGA | MATO GROSSO | Brasil | 5106307 | 51 | 33 | nan | nan | nan | Amazônia | 2.9 |
| 35734f49-fe69-39e0-972e-638857dd2f53 | -13.23436 | -54.32845 | 2026-07-05 05:04:00 | NPP-375D | PARANATINGA | MATO GROSSO | Brasil | 5106307 | 51 | 33 | nan | nan | nan | Amazônia | 2.0 |
| 3ec5756d-7dfb-399e-b5c8-ba04adf7f450 | -10.65481 | -49.71829 | 2026-07-05 05:04:00 | NPP-375D | LAGOA DA CONFUSÃO | TOCANTINS | Brasil | 1711902 | 17 | 33 | nan | nan | nan | Cerrado | 1.4 |
| d6117db5-2924-3774-85bd-c3d8a7b9b98a | -8.85216 | -62.21397 | 2026-07-05 05:04:00 | NPP-375D | MACHADINHO D'OESTE | RONDÔNIA | Brasil | 1100130 | 11 | 33 | nan | nan | nan | Amazônia | 4.0 |
| 31426b74-d1c6-328b-b3a8-a155c8267ec6 | -13.21497 | -54.32162 | 2026-07-05 05:04:00 | NPP-375D | PARANATINGA | MATO GROSSO | Brasil | 5106307 | 51 | 33 | nan | nan | nan | Amazônia | 0.8 |
| 4a825a5a-c55e-3bf6-9402-1d5cc58c1c13 | -8.85159 | -62.21709 | 2026-07-05 05:04:00 | NPP-375D | MACHADINHO D'OESTE | RONDÔNIA | Brasil | 1100130 | 11 | 33 | nan | nan | nan | Amazônia | 2.7 |
| 8a419998-3026-32b8-9958-06a1b5d51284 | -10.12307 | -52.09594 | 2026-07-05 05:04:00 | NPP-375D | SANTA CRUZ DO XINGU | MATO GROSSO | Brasil | 5107743 | 51 | 33 | nan | nan | nan | Amazônia | 1.7 |
| 6d854da2-b4dc-32cd-a360-94c46d1aa1fe | -11.43911 | -46.59746 | 2026-07-05 05:04:00 | NPP-375D | DIANÓPOLIS | TOCANTINS | Brasil | 1707009 | 17 | 33 | nan | nan | nan | Cerrado | 2.7 |


[Clique aqui para ver as próximas entradas](README7.md)
