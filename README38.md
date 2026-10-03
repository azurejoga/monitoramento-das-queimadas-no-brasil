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

## Dados Diários - Página 38

| ID | Latitude | Longitude | Data/Hora GMT | Satélite | Município | Estado | País | Município ID | Estado ID | País ID | Dias sem Chuva | Precipitação | Risco de Fogo | Bioma | FRP |
|----|----------|-----------|---------------|----------|-----------|--------|------|--------------|-----------|---------|----------------|--------------|----------------|-------|-----|
| aa192eae-fd49-3e5a-9fd5-b64ba255e00e | -2.98455 | -53.26459 | 2026-10-03 05:16:00 | NPP-375D | MEDICILÂNDIA | PARÁ | Brasil | 1504455 | 15 | 33 | nan | nan | nan | Amazônia | 0.5 |
| 263c0c65-461d-3f70-b9ad-5a933ea03a2c | -3.17759 | -54.08609 | 2026-10-03 05:16:00 | NPP-375D | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | 2.3 |
| 6607f7c8-331c-33e0-8eb1-2ee630b0f4f2 | -2.90127 | -54.08228 | 2026-10-03 05:16:00 | NPP-375D | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | 1.5 |
| 8f5d8eab-d1e5-3a68-8250-69bd9f9c9404 | -3.29486 | -53.84397 | 2026-10-03 05:16:00 | NPP-375D | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | 1.3 |
| 4fc51d66-9bd5-3995-90a6-4085d0dd3127 | -2.25211 | -51.92683 | 2026-10-03 05:16:00 | NPP-375D | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 0.8 |
| 392dc723-b825-35f0-9326-f478dc8214c1 | -3.61207 | -55.50876 | 2026-10-03 05:16:00 | NPP-375D | AVEIRO | PARÁ | Brasil | 1501006 | 15 | 33 | nan | nan | nan | Amazônia | 0.7 |
| 47b073d8-309a-3838-88e4-f03ed68766f3 | -3.0427 | -53.87347 | 2026-10-03 05:16:00 | NPP-375D | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | 0.7 |
| 5f705375-4de4-3924-ad55-db165ace6fc4 | -6.02215 | -53.53918 | 2026-10-03 05:16:00 | NPP-375D | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 2.0 |
| fd32d36f-6da5-372c-aa80-135e34d6a68a | -2.97772 | -53.26357 | 2026-10-03 05:16:00 | NPP-375D | MEDICILÂNDIA | PARÁ | Brasil | 1504455 | 15 | 33 | nan | nan | nan | Amazônia | 1.0 |
| 32a6751d-45ee-3c4d-9c24-ceac3fdccefb | -6.06463 | -53.47152 | 2026-10-03 05:16:00 | NPP-375D | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 3.2 |
| 8fb934f5-c832-3d97-bdfb-c2b96b17891f | -3.10803 | -50.28634 | 2026-10-03 05:16:00 | NPP-375D | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 1.0 |
| 5fb39c6d-5b4d-3c40-b067-28377dc9da5b | -3.00742 | -53.87885 | 2026-10-03 05:16:00 | NPP-375D | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | 1.2 |
| 77ffe7ff-5bb6-325f-8ed5-e0a093b82620 | -3.1051 | -50.28947 | 2026-10-03 05:16:00 | NPP-375D | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 1.3 |
| eb6bcddf-9351-3179-94e1-b5fe12d62e4c | -2.92304 | -54.09645 | 2026-10-03 05:16:00 | NPP-375D | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | 2.3 |
| 70d4791a-d2e0-3638-ae8f-438db4602a57 | -5.96264 | -55.34445 | 2026-10-03 05:16:00 | NPP-375D | ITAITUBA | PARÁ | Brasil | 1503606 | 15 | 33 | nan | nan | nan | Amazônia | 2.3 |
| 943deea2-5b44-35b2-8c0e-91c2fcbd45a2 | -2.85603 | -51.2855 | 2026-10-03 05:16:00 | NPP-375D | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 1.2 |
| fe09e493-dd44-3255-98a6-c25e11af9da4 | -6.25063 | -52.68695 | 2026-10-03 05:16:00 | NPP-375D | SÃO FÉLIX DO XINGU | PARÁ | Brasil | 1507300 | 15 | 33 | nan | nan | nan | Amazônia | 2.7 |
| 49d31f4b-8083-35ec-adca-fe6224005f13 | -2.17182 | -49.76384 | 2026-10-03 05:16:00 | NPP-375D | CAMETÁ | PARÁ | Brasil | 1502103 | 15 | 33 | nan | nan | nan | Amazônia | 1.3 |
| fac9204b-e884-37e8-a554-0307b27ad58b | -2.85283 | -51.28736 | 2026-10-03 05:16:00 | NPP-375D | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 1.3 |
| b37e7032-cd27-3fd5-9eba-7da6bf208263 | -2.8874 | -54.12675 | 2026-10-03 05:16:00 | NPP-375D | SANTARÉM | PARÁ | Brasil | 1506807 | 15 | 33 | nan | nan | nan | Amazônia | 1.0 |
| e2d9179e-cd41-30ac-bc78-6106a65ca2a7 | -5.64033 | -44.36645 | 2026-10-03 05:16:00 | NPP-375D | SÃO DOMINGOS DO MARANHÃO | MARANHÃO | Brasil | 2110708 | 21 | 33 | nan | nan | nan | Cerrado | 1.7 |
| 8bca640c-ba77-3705-8608-ff8e276b7b19 | -1.77084 | -55.02661 | 2026-10-03 05:16:00 | NPP-375D | ALENQUER | PARÁ | Brasil | 1500404 | 15 | 33 | nan | nan | nan | Amazônia | 1.3 |
| dfbe2fd7-cc24-3ece-9b8a-16e65e13e9bc | -3.18879 | -54.1022 | 2026-10-03 05:16:00 | NPP-375D | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | 1.8 |
| 14d8e4b1-8e44-3802-86ca-8fe3e249a510 | -5.97542 | -55.3714 | 2026-10-03 05:16:00 | NPP-375D | ITAITUBA | PARÁ | Brasil | 1503606 | 15 | 33 | nan | nan | nan | Amazônia | 1.2 |
| 90fa4a06-0150-372d-aec7-8da0649f0598 | -3.17259 | -54.09612 | 2026-10-03 05:16:00 | NPP-375D | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | 0.7 |
| 591b39e7-9ac6-3bdd-8e3e-42f8c6a836d2 | -2.89467 | -54.1458 | 2026-10-03 05:16:00 | NPP-375D | SANTARÉM | PARÁ | Brasil | 1506807 | 15 | 33 | nan | nan | nan | Amazônia | 0.9 |
| a104abee-535b-335e-ac82-60804c889db6 | -2.23065 | -51.92348 | 2026-10-03 05:16:00 | NPP-375D | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 1.3 |
| acd7975b-2ed9-3dd6-901e-72006be8ab74 | -3.11997 | -53.73972 | 2026-10-03 05:16:00 | NPP-375D | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | 12.3 |
| af7801e3-ae2a-3f26-9869-9f57faada3f4 | -2.85655 | -51.28794 | 2026-10-03 05:16:00 | NPP-375D | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 0.9 |
| d9858531-7ae2-3634-8574-dc7b6e0415f4 | -3.07759 | -51.27467 | 2026-10-03 05:16:00 | NPP-375D | ANAPU | PARÁ | Brasil | 1500859 | 15 | 33 | nan | nan | nan | Amazônia | 2.5 |
| b9821fb8-701d-305e-ada7-571c2ba42b6f | -4.2666 | -50.75603 | 2026-10-03 05:16:00 | NPP-375D | NOVO REPARTIMENTO | PARÁ | Brasil | 1505064 | 15 | 33 | nan | nan | nan | Amazônia | 3.4 |
| 1ecc019b-664a-3bd4-b2d9-98985966cdc8 | -4.41285 | -55.75301 | 2026-10-03 05:16:00 | NPP-375D | ITAITUBA | PARÁ | Brasil | 1503606 | 15 | 33 | nan | nan | nan | Amazônia | 1.6 |
| f3eee847-1083-3fbd-bc8a-156a913de888 | -2.89627 | -54.09226 | 2026-10-03 05:16:00 | NPP-375D | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | 1.3 |
| d0e5d1a9-814c-3d46-a0e3-c60ec891be03 | -3.12393 | -53.75859 | 2026-10-03 05:16:00 | NPP-375D | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | 2.5 |
| dadffa84-9239-34e9-a123-e1121e1660c3 | -3.01078 | -53.87937 | 2026-10-03 05:16:00 | NPP-375D | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | 1.8 |
| 0986bbce-1fb2-3353-abb8-db8b204e53ba | -3.11959 | -53.73638 | 2026-10-03 05:16:00 | NPP-375D | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | 7.0 |
| b7261b06-51b5-3b41-aadb-74e851fc38d9 | -3.32055 | -54.16917 | 2026-10-03 05:16:00 | NPP-375D | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | 1.1 |
| 2e4ba423-d2a3-3469-9751-3b563b59f11b | -2.33877 | -57.98416 | 2026-10-03 05:16:00 | NPP-375D | SÃO SEBASTIÃO DO UATUMÃ | AMAZONAS | Brasil | 1303957 | 13 | 33 | nan | nan | nan | Amazônia | 0.7 |
| 95f64bd5-abec-3011-9205-15964e7792d5 | -2.94156 | -54.18891 | 2026-10-03 05:16:00 | NPP-375D | SANTARÉM | PARÁ | Brasil | 1506807 | 15 | 33 | nan | nan | nan | Amazônia | 1.0 |
| 53da2ce2-1e92-3bc8-b47e-5211f0d9ee98 | -2.88135 | -51.0281 | 2026-10-03 05:16:00 | NPP-375D | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 2.0 |
| 6f919c0d-3547-3ee3-9aaa-86307a4892cb | -4.26567 | -50.7357 | 2026-10-03 05:16:00 | NPP-375D | NOVO REPARTIMENTO | PARÁ | Brasil | 1505064 | 15 | 33 | nan | nan | nan | Amazônia | 3.5 |
| e86ce2f3-9920-3358-849a-365a87452d76 | -4.90793 | -45.70902 | 2026-10-03 05:16:00 | NPP-375D | ARAME | MARANHÃO | Brasil | 2100956 | 21 | 33 | nan | nan | nan | Amazônia | 1.1 |
| e3f84191-f3a0-3e2d-ad41-70e89ab3804d | -5.60095 | -44.90593 | 2026-10-03 05:16:00 | NPP-375D | TUNTUM | MARANHÃO | Brasil | 2112308 | 21 | 33 | nan | nan | nan | Cerrado | 2.0 |
| 88df8442-6727-3aac-b011-d738f82f3129 | -1.22283 | -54.53701 | 2026-10-03 05:16:00 | NPP-375D | MONTE ALEGRE | PARÁ | Brasil | 1504802 | 15 | 33 | nan | nan | nan | Amazônia | 2.7 |
| ebf4a402-baa7-331c-ab19-175d10cc98b3 | -3.12505 | -53.75146 | 2026-10-03 05:16:00 | NPP-375D | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | 3.1 |
| a77cd85d-4cc9-3275-ab77-d8faa6cc2408 | -3.11384 | -50.28559 | 2026-10-03 05:16:00 | NPP-375D | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 1.9 |
| 8f6d4270-87e5-3d65-8930-5cee06374095 | -3.28589 | -53.85711 | 2026-10-03 05:16:00 | NPP-375D | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | 0.4 |
| a69bbb33-8499-3de3-ac53-5660695ac7c7 | -5.85475 | -53.47598 | 2026-10-03 05:16:00 | NPP-375D | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 2.9 |
| 40f67b8f-f6b1-3c87-8236-b8092c2926b3 | -5.25889 | -55.92252 | 2026-10-03 05:16:00 | NPP-375D | TRAIRÃO | PARÁ | Brasil | 1508050 | 15 | 33 | nan | nan | nan | Amazônia | 1.2 |
| 445e4cfd-3b2f-39c2-857b-c62155f49557 | -3.21368 | -53.94364 | 2026-10-03 05:16:00 | NPP-375D | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | 6.7 |
| ada52dd5-41b9-33c0-81d7-bb5b73e113c0 | -4.11359 | -55.01361 | 2026-10-03 05:16:00 | NPP-375D | RURÓPOLIS | PARÁ | Brasil | 1506195 | 15 | 33 | nan | nan | nan | Amazônia | 0.6 |
| 0fa6dca8-5fbb-320e-80a2-3d0c3be5cd20 | -7.46721 | -54.9951 | 2026-10-03 05:16:00 | NPP-375D | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 1.0 |
| e8b21e4d-7e21-3cfd-bc60-051ae7145f9b | -5.25945 | -55.91904 | 2026-10-03 05:16:00 | NPP-375D | TRAIRÃO | PARÁ | Brasil | 1508050 | 15 | 33 | nan | nan | nan | Amazônia | 1.2 |
| 9f4dec7f-349e-3fa6-9e42-4ae2ac8c9288 | -3.89415 | -56.0326 | 2026-10-03 05:16:00 | NPP-375D | ITAITUBA | PARÁ | Brasil | 1503606 | 15 | 33 | nan | nan | nan | Amazônia | 0.6 |
| 6550b143-e796-3c40-8e04-d58de8a24aa1 | -4.42926 | -55.75212 | 2026-10-03 05:16:00 | NPP-375D | ITAITUBA | PARÁ | Brasil | 1503606 | 15 | 33 | nan | nan | nan | Amazônia | 1.7 |
| 1afff832-8aef-33a6-9ca4-d1e47919ac7e | -5.85131 | -53.47533 | 2026-10-03 05:16:00 | NPP-375D | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 3.0 |
| 9b991fdd-171c-3eff-a8b8-a910b589c71f | -4.44923 | -47.92801 | 2026-10-03 05:16:00 | NPP-375D | DOM ELISEU | PARÁ | Brasil | 1502939 | 15 | 33 | nan | nan | nan | Amazônia | 6.3 |
| 0a9e446f-fd56-38a5-bf98-d6cbcd652acc | -3.02943 | -48.41579 | 2026-10-03 05:16:00 | NPP-375D | TOMÉ-AÇU | PARÁ | Brasil | 1508001 | 15 | 33 | nan | nan | nan | Amazônia | 0.9 |
| 5f65adf2-4ac7-373f-a590-fa160dffabfd | -3.11941 | -53.74329 | 2026-10-03 05:16:00 | NPP-375D | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | 12.3 |
| 5cb279b8-1d8f-3c7f-9e07-ca3180ef8a05 | -2.87178 | -54.11714 | 2026-10-03 05:16:00 | NPP-375D | SANTARÉM | PARÁ | Brasil | 1506807 | 15 | 33 | nan | nan | nan | Amazônia | 1.0 |
| c0186eb3-e87d-35b1-8c01-663f0b396c7c | -3.14077 | -53.73931 | 2026-10-03 05:16:00 | NPP-375D | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | 1.8 |
| 2fc4f907-3ef1-3e65-9dcb-db5825c3294d | -1.99473 | -49.65013 | 2026-10-03 05:16:00 | NPP-375D | LIMOEIRO DO AJURU | PARÁ | Brasil | 1504000 | 15 | 33 | nan | nan | nan | Amazônia | 0.8 |
| 6740aaf8-14ca-39a5-8ae5-0054581bb323 | -5.85592 | -53.46848 | 2026-10-03 05:16:00 | NPP-375D | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 2.9 |
| 6f055f77-bbfa-31ba-bf9a-eafdec692305 | -2.97123 | -53.26328 | 2026-10-03 05:16:00 | NPP-375D | MEDICILÂNDIA | PARÁ | Brasil | 1504455 | 15 | 33 | nan | nan | nan | Amazônia | 3.1 |
| 4127c17f-3678-3a76-b85a-c3356b5b079f | -2.90407 | -54.0863 | 2026-10-03 05:16:00 | NPP-375D | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | 2.5 |
| 078976a1-6ef2-305b-8160-39bff406d3db | -2.93586 | -54.10204 | 2026-10-03 05:16:00 | NPP-375D | SANTARÉM | PARÁ | Brasil | 1506807 | 15 | 33 | nan | nan | nan | Amazônia | 0.8 |
| 6ebd4785-07a4-3175-9af6-ec953de10a16 | -5.29853 | -45.80293 | 2026-10-03 05:16:00 | NPP-375D | ITAIPAVA DO GRAJAÚ | MARANHÃO | Brasil | 2105351 | 21 | 33 | nan | nan | nan | Cerrado | 1.7 |
| 83841c94-abcf-3039-8a67-feffe1b673a4 | -3.16341 | -54.07619 | 2026-10-03 05:16:00 | NPP-375D | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | 0.9 |
| 3e9f41e4-9110-3256-a8bb-f5491dd3fcad | -3.10748 | -50.30018 | 2026-10-03 05:16:00 | NPP-375D | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 1.3 |
| 0616555f-5dec-3718-8dcb-37079f934d40 | -4.45423 | -47.92749 | 2026-10-03 05:16:00 | NPP-375D | DOM ELISEU | PARÁ | Brasil | 1502939 | 15 | 33 | nan | nan | nan | Amazônia | 9.1 |
| 269d1cc5-e661-364b-80ed-50e60c337b48 | -3.112 | -50.28694 | 2026-10-03 05:16:00 | NPP-375D | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 1.0 |
| aba42201-c25f-3f7c-a379-5dcd1b38afc5 | -1.7383 | -57.17295 | 2026-10-03 05:16:00 | NPP-375D | NHAMUNDÁ | AMAZONAS | Brasil | 1303007 | 13 | 33 | nan | nan | nan | Amazônia | 5.3 |
| 703432c3-1aa7-3166-bb57-4b24e66221dd | -5.97764 | -55.37888 | 2026-10-03 05:16:00 | NPP-375D | ITAITUBA | PARÁ | Brasil | 1503606 | 15 | 33 | nan | nan | nan | Amazônia | 0.7 |
| 6194e0d8-b866-3234-bd82-77cc45413dbb | -4.98636 | -45.64038 | 2026-10-03 05:16:00 | NPP-375D | ARAME | MARANHÃO | Brasil | 2100956 | 21 | 33 | nan | nan | nan | Amazônia | 1.0 |
| dd5a0946-cabe-38f5-8b60-047ec899bd7e | -2.97258 | -54.10058 | 2026-10-03 05:16:00 | NPP-375D | SANTARÉM | PARÁ | Brasil | 1506807 | 15 | 33 | nan | nan | nan | Amazônia | 1.8 |
| 76ea45a5-d14a-3c80-a37d-91716fb3d938 | -2.73562 | -49.46131 | 2026-10-03 05:16:00 | NPP-375D | MOJU | PARÁ | Brasil | 1504703 | 15 | 33 | nan | nan | nan | Amazônia | 0.6 |
| 5a0ec069-af94-356b-a0a0-d3885ecc058b | -1.76364 | -55.02903 | 2026-10-03 05:16:00 | NPP-375D | ALENQUER | PARÁ | Brasil | 1500404 | 15 | 33 | nan | nan | nan | Amazônia | 0.7 |
| d8bd2521-dfd0-3b03-9a1b-c05c9f5ad699 | -2.88063 | -51.03267 | 2026-10-03 05:16:00 | NPP-375D | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 1.4 |
| e3e1d2db-9939-36c4-a010-caed34eead72 | -1.14965 | -54.18547 | 2026-10-03 05:16:00 | NPP-375D | MONTE ALEGRE | PARÁ | Brasil | 1504802 | 15 | 33 | nan | nan | nan | Amazônia | 0.8 |
| c2b3ef4c-3e27-3d6c-896c-5d040858e8b0 | -4.90844 | -45.70546 | 2026-10-03 05:16:00 | NPP-375D | ARAME | MARANHÃO | Brasil | 2100956 | 21 | 33 | nan | nan | nan | Amazônia | 0.8 |
| 882dbbf9-8424-3d67-b7b1-1760ddfa2815 | -3.12223 | -53.74737 | 2026-10-03 05:16:00 | NPP-375D | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | 3.5 |
| 421658f5-f131-39f3-ba9c-7f7e25163480 | -1.64351 | -55.14503 | 2026-10-03 05:16:00 | NPP-375D | CURUÁ | PARÁ | Brasil | 1502855 | 15 | 33 | nan | nan | nan | Amazônia | 1.2 |
| 4075fbbd-7c16-342b-9db2-077de781c336 | -5.74381 | -45.14119 | 2026-10-03 05:16:00 | NPP-375D | BARRA DO CORDA | MARANHÃO | Brasil | 2101608 | 21 | 33 | nan | nan | nan | Cerrado | 1.7 |
| 47e5453a-5d54-39a2-bbe6-8996785d9f27 | -3.00486 | -54.75346 | 2026-10-03 05:16:00 | NPP-375D | MOJUÍ DOS CAMPOS | PARÁ | Brasil | 1504752 | 15 | 33 | nan | nan | nan | Amazônia | 0.6 |
| da1fba35-a4b5-382b-8469-513ef8aa3ce8 | -2.64682 | -54.23592 | 2026-10-03 05:16:00 | NPP-375D | SANTARÉM | PARÁ | Brasil | 1506807 | 15 | 33 | nan | nan | nan | Amazônia | 0.8 |
| d20563fd-c950-30b8-a561-70c2b12716c3 | -2.91131 | -54.08384 | 2026-10-03 05:16:00 | NPP-375D | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | 1.9 |
| 844db112-3453-3c7e-9a54-06456745dd42 | -3.85011 | -55.80287 | 2026-10-03 05:16:00 | NPP-375D | AVEIRO | PARÁ | Brasil | 1501006 | 15 | 33 | nan | nan | nan | Amazônia | 1.2 |
| 86d52d54-c785-361d-975c-36424e7b1479 | -2.96644 | -54.09603 | 2026-10-03 05:16:00 | NPP-375D | SANTARÉM | PARÁ | Brasil | 1506807 | 15 | 33 | nan | nan | nan | Amazônia | 1.6 |
| b5cc1d5b-a10a-3e73-8e66-b87d14dc867d | -3.28645 | -53.85357 | 2026-10-03 05:16:00 | NPP-375D | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | 0.4 |
| f88195b9-4f04-3108-9d06-c926d940edc5 | -2.95864 | -54.10199 | 2026-10-03 05:16:00 | NPP-375D | SANTARÉM | PARÁ | Brasil | 1506807 | 15 | 33 | nan | nan | nan | Amazônia | 0.8 |
| 669c9024-83c3-3755-a71a-854d2bf6ede2 | -1.26011 | -54.55326 | 2026-10-03 05:16:00 | NPP-375D | MONTE ALEGRE | PARÁ | Brasil | 1504802 | 15 | 33 | nan | nan | nan | Amazônia | 0.8 |
| a42dc361-ced5-3482-9f46-92f6eeaa7d33 | -7.46361 | -54.98756 | 2026-10-03 05:16:00 | NPP-375D | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 1.0 |
| 38489810-9f04-3c5b-965b-6ea0c4ce57a8 | -4.41512 | -49.9668 | 2026-10-03 05:16:00 | NPP-375D | NOVO REPARTIMENTO | PARÁ | Brasil | 1505064 | 15 | 33 | nan | nan | nan | Amazônia | 0.7 |
| 872cb7fc-be69-3f8b-ac7e-1b801d9376c7 | -2.32414 | -60.06514 | 2026-10-03 05:16:00 | NPP-375D | MANAUS | AMAZONAS | Brasil | 1302603 | 13 | 33 | nan | nan | nan | Amazônia | 0.9 |
| 38a5b0d5-ff9b-3d50-8d63-290c77cdb044 | -3.01919 | -53.89156 | 2026-10-03 05:16:00 | NPP-375D | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | 2.4 |
| 3a738d75-7448-36cf-8800-577f052fae85 | -1.2195 | -54.53648 | 2026-10-03 05:16:00 | NPP-375D | MONTE ALEGRE | PARÁ | Brasil | 1504802 | 15 | 33 | nan | nan | nan | Amazônia | 5.5 |
| 99101f7e-e8e1-3c43-bf79-3e305a3d2ecb | -6.06582 | -53.46388 | 2026-10-03 05:16:00 | NPP-375D | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 1.9 |
| aaea6416-49cb-3c42-a15c-a23a0bb7fe9c | -6.21982 | -53.2631 | 2026-10-03 05:16:00 | NPP-375D | SÃO FÉLIX DO XINGU | PARÁ | Brasil | 1507300 | 15 | 33 | nan | nan | nan | Amazônia | 2.5 |
| 33673ada-16ad-3ad8-80b9-c15f6a58fcc5 | -3.0076 | -54.73617 | 2026-10-03 05:16:00 | NPP-375D | MOJUÍ DOS CAMPOS | PARÁ | Brasil | 1504752 | 15 | 33 | nan | nan | nan | Amazônia | 0.6 |
| c1c6e82b-7559-35de-88fa-c219703f9453 | -3.12672 | -53.74078 | 2026-10-03 05:16:00 | NPP-375D | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | 2.2 |


[Clique aqui para ver as próximas entradas](README39.md)
