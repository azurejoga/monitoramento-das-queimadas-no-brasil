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

## Dados Diários - Página 2

| ID | Latitude | Longitude | Data/Hora GMT | Satélite | Município | Estado | País | Município ID | Estado ID | País ID | Dias sem Chuva | Precipitação | Risco de Fogo | Bioma | FRP |
|----|----------|-----------|---------------|----------|-----------|--------|------|--------------|-----------|---------|----------------|--------------|----------------|-------|-----|
| 5f2c9e2d-6488-37aa-8630-6e09f28ce990 | -8.6538 | -54.6707 | 2026-07-06 02:20:00 | GOES-19 | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 58.3 |
| f7230871-9577-3d9e-98a0-0e8ef7ef9051 | -8.6727 | -54.6492 | 2026-07-06 02:20:00 | GOES-19 | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 119.2 |
| 7edc79e1-8a33-3f51-898f-352a332ba100 | -10.9205 | -43.0622 | 2026-07-06 02:20:00 | GOES-19 | BARRA | BAHIA | Brasil | 2902708 | 29 | 33 | nan | nan | nan | Cerrado | 73.6 |
| d3b25b4e-85f4-3084-9389-3d7126b4457f | -8.654 | -54.6505 | 2026-07-06 02:20:00 | GOES-19 | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 43.8 |
| 72db0359-7de3-30e4-a5aa-79bdb60b6974 | -8.6725 | -54.6695 | 2026-07-06 02:20:00 | GOES-19 | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 152.6 |
| 300301fa-495e-339e-bdbc-8aa9d50e08c9 | -8.6725 | -54.6695 | 2026-07-06 02:30:00 | GOES-19 | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 85.5 |
| ba0f412b-f6eb-3b2d-9e02-27d6cf7a6527 | -8.6727 | -54.6492 | 2026-07-06 02:30:00 | GOES-19 | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 45.6 |
| ce1d324e-087e-35ab-8735-5c57ca489d04 | -10.9205 | -43.0622 | 2026-07-06 02:30:00 | GOES-19 | BARRA | BAHIA | Brasil | 2902708 | 29 | 33 | nan | nan | nan | Cerrado | 62.8 |
| 21513e2d-3b46-3f6e-a8c3-5ce776dc97f9 | -8.7294 | -54.5645 | 2026-07-06 02:30:00 | GOES-19 | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 57.2 |
| 416d63f4-c226-3ff8-ad82-26e0e3754e3e | -10.9205 | -43.0622 | 2026-07-06 02:40:00 | GOES-19 | BARRA | BAHIA | Brasil | 2902708 | 29 | 33 | nan | nan | nan | Cerrado | 67.7 |
| 33c19842-4efe-30fa-b642-e65062cc77b9 | -8.6725 | -54.6695 | 2026-07-06 02:40:00 | GOES-19 | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 64.1 |
| 28d68589-8dff-32e4-9d4d-4cbde2130f2b | -8.7294 | -54.5645 | 2026-07-06 02:40:00 | GOES-19 | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 45.6 |
| 5cf27fa3-8906-39e0-ab90-a029db96cdac | -9.361 | -40.4273 | 2026-07-06 02:40:00 | GOES-19 | JUAZEIRO | BAHIA | Brasil | 2918407 | 29 | 33 | nan | nan | nan | Caatinga | 67.1 |
| 455bddb6-9bff-3403-88c2-9be7bf63b9b8 | -8.6727 | -54.6492 | 2026-07-06 02:40:00 | GOES-19 | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 57.8 |
| f370f412-18ed-38cc-a3c1-9d399d52241a | -8.7294 | -54.5645 | 2026-07-06 02:50:00 | GOES-19 | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 52.4 |
| ee4854da-9bb2-3f63-950a-9a7da2d47228 | -8.6725 | -54.6695 | 2026-07-06 03:00:00 | GOES-19 | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 45.6 |
| 2725e403-c0e9-35d9-a432-3b3b4c3650aa | -11.9305 | -43.3812 | 2026-07-06 03:10:00 | GOES-19 | MUQUÉM DO SÃO FRANCISCO | BAHIA | Brasil | 2922250 | 29 | 33 | nan | nan | nan | Cerrado | 66.0 |
| 0afcc2d3-ccf1-3109-a37f-852163632c4e | -10.9205 | -43.0622 | 2026-07-06 03:20:00 | GOES-19 | BARRA | BAHIA | Brasil | 2902708 | 29 | 33 | nan | nan | nan | Cerrado | 62.9 |
| 42baef33-e275-3d03-a88a-44dfb8c6f920 | -11.92332 | -43.38046 | 2026-07-06 03:21:00 | NOAA-20 | MUQUÉM DO SÃO FRANCISCO | BAHIA | Brasil | 2922250 | 29 | 33 | nan | nan | nan | Cerrado | 25.1 |
| 861a1e4a-cfcf-306c-b07d-76690541e036 | -10.92168 | -43.06311 | 2026-07-06 03:21:00 | NOAA-20 | BARRA | BAHIA | Brasil | 2902708 | 29 | 33 | nan | nan | nan | Cerrado | 8.1 |
| 1ee4ea54-27ff-307d-b651-ca8cc97d4281 | -11.91674 | -43.37849 | 2026-07-06 03:21:00 | NOAA-20 | MUQUÉM DO SÃO FRANCISCO | BAHIA | Brasil | 2922250 | 29 | 33 | nan | nan | nan | Cerrado | 7.2 |
| 6e6eaa44-4b49-311a-83cd-c824f94584b6 | -9.36429 | -40.42352 | 2026-07-06 03:21:00 | NOAA-20 | JUAZEIRO | BAHIA | Brasil | 2918407 | 29 | 33 | nan | nan | nan | Caatinga | 2.1 |
| 90d1e053-c838-3429-96e4-84e6a63a71a8 | -10.92959 | -43.05853 | 2026-07-06 03:21:00 | NOAA-20 | BARRA | BAHIA | Brasil | 2902708 | 29 | 33 | nan | nan | nan | Cerrado | 12.3 |
| f76bfb3f-e9b6-3cb3-9699-107deee55f5b | -11.92461 | -43.37428 | 2026-07-06 03:21:00 | NOAA-20 | MUQUÉM DO SÃO FRANCISCO | BAHIA | Brasil | 2922250 | 29 | 33 | nan | nan | nan | Cerrado | 25.1 |
| c54ba258-1bb5-3e3a-91f7-08f046a2cc9f | -10.92292 | -43.05705 | 2026-07-06 03:21:00 | NOAA-20 | BARRA | BAHIA | Brasil | 2902708 | 29 | 33 | nan | nan | nan | Cerrado | 8.1 |
| 4831ec24-f0de-3206-bdd7-e89c3a31a60a | -10.92836 | -43.06456 | 2026-07-06 03:21:00 | NOAA-20 | BARRA | BAHIA | Brasil | 2902708 | 29 | 33 | nan | nan | nan | Cerrado | 12.3 |
| 7ea5a628-e9a4-31ff-bc6f-aa85a6c9e201 | -9.36285 | -40.42256 | 2026-07-06 03:21:00 | NOAA-20 | JUAZEIRO | BAHIA | Brasil | 2918407 | 29 | 33 | nan | nan | nan | Caatinga | 2.2 |
| 8c7283cd-a6e2-3e9b-bbb2-a467d75aeb38 | -4.58693 | -37.80788 | 2026-07-06 04:06:00 | NOAA-21 | ARACATI | CEARÁ | Brasil | 2301109 | 23 | 33 | nan | nan | nan | Caatinga | 2.4 |
| d98b5a30-0971-39d2-aaf3-494e32817c42 | -8.77624 | -47.40742 | 2026-07-06 04:08:00 | NOAA-21 | ITACAJÁ | TOCANTINS | Brasil | 1710508 | 17 | 33 | nan | nan | nan | Cerrado | 2.0 |
| 4f97ea5d-08e5-341d-96f5-a074c9e61f4c | -6.93582 | -43.70941 | 2026-07-06 04:08:00 | NOAA-21 | GUADALUPE | PIAUÍ | Brasil | 2204501 | 22 | 33 | nan | nan | nan | Cerrado | 1.0 |
| 5412ae05-3060-321c-baec-e211073677b3 | -6.93804 | -43.71751 | 2026-07-06 04:08:00 | NOAA-21 | GUADALUPE | PIAUÍ | Brasil | 2204501 | 22 | 33 | nan | nan | nan | Cerrado | 1.3 |
| d34feafd-f4df-355c-937e-ef8187bb264d | -8.11287 | -47.12259 | 2026-07-06 04:08:00 | NOAA-21 | GOIATINS | TOCANTINS | Brasil | 1709005 | 17 | 33 | nan | nan | nan | Cerrado | 3.6 |
| 297aec29-1ef2-33d0-a54d-d6c952a7298c | -7.00194 | -43.86444 | 2026-07-06 04:08:00 | NOAA-21 | MARCOS PARENTE | PIAUÍ | Brasil | 2206001 | 22 | 33 | nan | nan | nan | Cerrado | 1.0 |
| 58a9b687-d371-3136-aadf-0d4e41e10b9b | -6.94088 | -43.72184 | 2026-07-06 04:08:00 | NOAA-21 | GUADALUPE | PIAUÍ | Brasil | 2204501 | 22 | 33 | nan | nan | nan | Cerrado | 1.3 |
| fdc2a0c5-fbe6-3171-be40-0cd1750c7cf4 | -5.75303 | -43.26284 | 2026-07-06 04:08:00 | NOAA-21 | PARNARAMA | MARANHÃO | Brasil | 2107803 | 21 | 33 | nan | nan | nan | Cerrado | 1.9 |
| 31132378-d611-3ba9-bbd5-015a28e04294 | -10.92775 | -43.0577 | 2026-07-06 04:08:00 | NOAA-21 | BARRA | BAHIA | Brasil | 2902708 | 29 | 33 | nan | nan | nan | Cerrado | 42.2 |
| cc8305b5-bfee-38e8-bc23-639b3f039ce9 | -8.09569 | -46.70289 | 2026-07-06 04:08:00 | NOAA-21 | CAMPOS LINDOS | TOCANTINS | Brasil | 1703842 | 17 | 33 | nan | nan | nan | Cerrado | 0.9 |
| 37c0750a-940e-361d-95b2-85d598aa45af | -6.94149 | -43.71806 | 2026-07-06 04:08:00 | NOAA-21 | GUADALUPE | PIAUÍ | Brasil | 2204501 | 22 | 33 | nan | nan | nan | Cerrado | 1.3 |
| d2bcacfd-8636-3f9a-830f-d954c2cf5044 | -6.93865 | -43.71374 | 2026-07-06 04:08:00 | NOAA-21 | GUADALUPE | PIAUÍ | Brasil | 2204501 | 22 | 33 | nan | nan | nan | Cerrado | 1.0 |
| c80abce5-c5da-398b-91ac-31ed93536b5e | -6.90363 | -43.71202 | 2026-07-06 04:08:00 | NOAA-21 | GUADALUPE | PIAUÍ | Brasil | 2204501 | 22 | 33 | nan | nan | nan | Cerrado | 3.3 |
| 8e3f8b65-f8df-300a-80c2-5780aaf9b695 | -7.5418 | -39.03605 | 2026-07-06 04:08:00 | NOAA-21 | BREJO SANTO | CEARÁ | Brasil | 2302503 | 23 | 33 | nan | nan | nan | Caatinga | 0.6 |
| 9dcbad55-1d7a-3bfd-b767-acf2a954737d | -9.50183 | -42.99178 | 2026-07-06 04:08:00 | NOAA-21 | CAMPO ALEGRE DE LOURDES | BAHIA | Brasil | 2905909 | 29 | 33 | nan | nan | nan | Caatinga | 2.9 |
| 4cb165be-616d-3bc6-9f13-d30b189733af | -6.90019 | -43.71149 | 2026-07-06 04:08:00 | NOAA-21 | GUADALUPE | PIAUÍ | Brasil | 2204501 | 22 | 33 | nan | nan | nan | Cerrado | 3.3 |
| b9406612-30c0-3356-a95a-13c3b8a45491 | -5.3191 | -43.55894 | 2026-07-06 04:08:00 | NOAA-21 | MATÕES | MARANHÃO | Brasil | 2106607 | 21 | 33 | nan | nan | nan | Cerrado | 1.0 |
| 2c39ef19-0827-3525-8e69-99c1134d7ff6 | -10.01813 | -42.36983 | 2026-07-06 04:08:00 | NOAA-21 | PILÃO ARCADO | BAHIA | Brasil | 2924405 | 29 | 33 | nan | nan | nan | Caatinga | 1.9 |
| 830137e0-81f2-3914-989b-5c77e52c1858 | -7.06206 | -46.73267 | 2026-07-06 04:08:00 | NOAA-21 | FEIRA NOVA DO MARANHÃO | MARANHÃO | Brasil | 2104073 | 21 | 33 | nan | nan | nan | Cerrado | 0.8 |
| a7df1c19-9f2f-32a5-b240-3ecdabe7c6d9 | -10.9305 | -43.06175 | 2026-07-06 04:08:00 | NOAA-21 | BARRA | BAHIA | Brasil | 2902708 | 29 | 33 | nan | nan | nan | Cerrado | 14.6 |
| 8a8dd432-c450-33fb-a158-29c44157a3e6 | -8.911 | -47.76983 | 2026-07-06 04:08:00 | NOAA-21 | SANTA MARIA DO TOCANTINS | TOCANTINS | Brasil | 1718881 | 17 | 33 | nan | nan | nan | Cerrado | 1.2 |
| e8785381-e2d4-3380-8bca-c1ea891a4b6e | -6.89268 | -43.7142 | 2026-07-06 04:08:00 | NOAA-21 | GUADALUPE | PIAUÍ | Brasil | 2204501 | 22 | 33 | nan | nan | nan | Cerrado | 1.1 |
| 5b34f4ed-19a0-3efb-a6c0-b9a936313719 | -7.23602 | -43.21834 | 2026-07-06 04:08:00 | NOAA-21 | FLORIANO | PIAUÍ | Brasil | 2203909 | 22 | 33 | nan | nan | nan | Caatinga | 0.9 |
| 88d55635-7027-3a37-8cec-438183147f1a | -5.75244 | -43.26656 | 2026-07-06 04:08:00 | NOAA-21 | PARNARAMA | MARANHÃO | Brasil | 2107803 | 21 | 33 | nan | nan | nan | Cerrado | 1.9 |
| 48fff6e3-f2f4-3b06-bfc0-c75962d6f623 | -8.73546 | -54.55989 | 2026-07-06 04:08:00 | NOAA-21 | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 2.8 |
| c5e3cc14-b6ef-37a4-89a8-fcf9df08dea5 | -5.67437 | -48.09954 | 2026-07-06 04:08:00 | NOAA-21 | ARAGUATINS | TOCANTINS | Brasil | 1702208 | 17 | 33 | nan | nan | nan | Amazônia | 3.6 |
| b7689b70-9eca-3161-b7b1-9cbd213e4d72 | -7.90492 | -48.25367 | 2026-07-06 04:08:00 | NOAA-21 | PALMEIRANTE | TOCANTINS | Brasil | 1715705 | 17 | 33 | nan | nan | nan | Cerrado | 2.5 |
| 8c260967-6c83-3018-b9ee-382c6baf1fd8 | -6.89674 | -43.71095 | 2026-07-06 04:08:00 | NOAA-21 | GUADALUPE | PIAUÍ | Brasil | 2204501 | 22 | 33 | nan | nan | nan | Cerrado | 1.1 |
| c81ea150-6df4-3181-ac70-122b860e331e | -7.04169 | -37.26707 | 2026-07-06 04:08:00 | NOAA-21 | PATOS | PARAÍBA | Brasil | 2510808 | 25 | 33 | nan | nan | nan | Caatinga | 0.7 |
| 60b9d53f-7a31-3fd1-b4e3-221379d76d23 | -8.13369 | -43.58223 | 2026-07-06 04:08:00 | NOAA-21 | ELISEU MARTINS | PIAUÍ | Brasil | 2203602 | 22 | 33 | nan | nan | nan | Cerrado | 1.0 |
| 033652b2-e532-3b7c-a0a6-52322e5d6748 | -8.09171 | -46.70229 | 2026-07-06 04:08:00 | NOAA-21 | CAMPOS LINDOS | TOCANTINS | Brasil | 1703842 | 17 | 33 | nan | nan | nan | Cerrado | 0.9 |
| 3301981f-ad8c-3203-8e24-288c6f672705 | -8.11694 | -47.12333 | 2026-07-06 04:08:00 | NOAA-21 | GOIATINS | TOCANTINS | Brasil | 1709005 | 17 | 33 | nan | nan | nan | Cerrado | 3.6 |
| 5efbd57f-6f3c-3272-8b3a-075d7e72e967 | -8.72997 | -54.55316 | 2026-07-06 04:08:00 | NOAA-21 | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 1.0 |
| 53e9180c-edec-3438-87b3-ed4c72944e05 | -8.08093 | -46.69356 | 2026-07-06 04:08:00 | NOAA-21 | CAMPOS LINDOS | TOCANTINS | Brasil | 1703842 | 17 | 33 | nan | nan | nan | Cerrado | 1.4 |
| 2903510a-24bd-3454-9e88-ffb688051139 | -8.11758 | -47.11955 | 2026-07-06 04:08:00 | NOAA-21 | GOIATINS | TOCANTINS | Brasil | 1709005 | 17 | 33 | nan | nan | nan | Cerrado | 3.9 |
| cb7d117f-e6e6-39d0-aee2-7bd6869887a5 | -10.92719 | -43.06122 | 2026-07-06 04:08:00 | NOAA-21 | BARRA | BAHIA | Brasil | 2902708 | 29 | 33 | nan | nan | nan | Cerrado | 14.6 |
| 0459b2ac-8b06-3ccd-a1ca-5760b4e2e4b1 | -9.75158 | -48.18984 | 2026-07-06 04:08:00 | NOAA-21 | TOCANTÍNIA | TOCANTINS | Brasil | 1721109 | 17 | 33 | nan | nan | nan | Cerrado | 2.4 |
| 341cfa47-0c9f-32df-9a3f-d01a04fd7c43 | -9.44554 | -40.52717 | 2026-07-06 04:08:00 | NOAA-21 | JUAZEIRO | BAHIA | Brasil | 2918407 | 29 | 33 | nan | nan | nan | Caatinga | 0.6 |
| cf3e9633-bd05-33da-a753-8bdf0f7ed47f | -8.71902 | -54.53965 | 2026-07-06 04:08:00 | NOAA-21 | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 5.9 |
| a9936b95-c0b3-3731-8946-6dd091956ed4 | -6.5931 | -51.69773 | 2026-07-06 04:08:00 | NOAA-21 | SÃO FÉLIX DO XINGU | PARÁ | Brasil | 1507300 | 15 | 33 | nan | nan | nan | Amazônia | 1.0 |
| d9227e17-af99-3e80-a511-3cb382dde9b8 | -3.97471 | -47.20716 | 2026-07-06 04:08:00 | NOAA-21 | ULIANÓPOLIS | PARÁ | Brasil | 1508126 | 15 | 33 | nan | nan | nan | Amazônia | 1.1 |
| 14d1f4b8-717c-39bd-9eb7-56c6e04bede9 | -6.90708 | -43.71256 | 2026-07-06 04:08:00 | NOAA-21 | GUADALUPE | PIAUÍ | Brasil | 2204501 | 22 | 33 | nan | nan | nan | Cerrado | 2.8 |
| b2e3addb-a1ee-3a2a-a888-a405fa8400de | -6.89305 | -43.71479 | 2026-07-06 04:08:00 | NOAA-21 | GUADALUPE | PIAUÍ | Brasil | 2204501 | 22 | 33 | nan | nan | nan | Cerrado | 1.8 |
| 650efee4-4087-3031-aa39-91b250dd87b1 | -4.52131 | -38.54874 | 2026-07-06 04:08:00 | NOAA-21 | OCARA | CEARÁ | Brasil | 2309458 | 23 | 33 | nan | nan | nan | Caatinga | 1.3 |
| 8ee2788f-6e41-3685-80c1-50b6465a1e38 | -8.121 | -47.12414 | 2026-07-06 04:08:00 | NOAA-21 | GOIATINS | TOCANTINS | Brasil | 1709005 | 17 | 33 | nan | nan | nan | Cerrado | 4.9 |
| 5963071b-1136-32de-aedc-7d4d5ebcd956 | -8.37582 | -46.88044 | 2026-07-06 04:08:00 | NOAA-21 | CAMPOS LINDOS | TOCANTINS | Brasil | 1703842 | 17 | 33 | nan | nan | nan | Cerrado | 3.0 |
| 0756a353-edce-355c-9f99-4103026c8f6d | -8.08491 | -46.69418 | 2026-07-06 04:08:00 | NOAA-21 | CAMPOS LINDOS | TOCANTINS | Brasil | 1703842 | 17 | 33 | nan | nan | nan | Cerrado | 0.8 |
| db82246d-e100-3c2b-89a8-b2dab08f2465 | -9.75229 | -48.18578 | 2026-07-06 04:08:00 | NOAA-21 | TOCANTÍNIA | TOCANTINS | Brasil | 1721109 | 17 | 33 | nan | nan | nan | Cerrado | 2.4 |
| bd241aa8-8d86-3fe1-8f58-23175d94e82e | -8.73438 | -54.5655 | 2026-07-06 04:08:00 | NOAA-21 | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 2.8 |
| e01e8f9f-eb66-3826-a8bf-a01d81cd4adc | -6.94371 | -43.72617 | 2026-07-06 04:08:00 | NOAA-21 | GUADALUPE | PIAUÍ | Brasil | 2204501 | 22 | 33 | nan | nan | nan | Cerrado | 1.8 |
| fdb26f31-158f-394c-93dd-989956bc7fe5 | -4.51782 | -38.54822 | 2026-07-06 04:08:00 | NOAA-21 | OCARA | CEARÁ | Brasil | 2309458 | 23 | 33 | nan | nan | nan | Caatinga | 1.3 |
| ef0a486f-f555-31f2-947e-e8db11568f13 | -6.59879 | -51.69868 | 2026-07-06 04:08:00 | NOAA-21 | SÃO FÉLIX DO XINGU | PARÁ | Brasil | 1507300 | 15 | 33 | nan | nan | nan | Amazônia | 0.8 |
| d73dd0be-62e8-3f62-8826-39cb4bfaaf6a | -6.89613 | -43.71473 | 2026-07-06 04:08:00 | NOAA-21 | GUADALUPE | PIAUÍ | Brasil | 2204501 | 22 | 33 | nan | nan | nan | Cerrado | 1.1 |
| 4d92c39b-81cf-3029-9571-9a60f932c55a | -7.0054 | -43.865 | 2026-07-06 04:08:00 | NOAA-21 | MARCOS PARENTE | PIAUÍ | Brasil | 2206001 | 22 | 33 | nan | nan | nan | Cerrado | 1.2 |
| 5cce04a8-00eb-3db6-aa45-f9b25def3d26 | -10.01759 | -42.37331 | 2026-07-06 04:08:00 | NOAA-21 | PILÃO ARCADO | BAHIA | Brasil | 2924405 | 29 | 33 | nan | nan | nan | Caatinga | 1.9 |
| 388b3d6c-5212-3c1a-a896-7f59126b8385 | -6.90646 | -43.71635 | 2026-07-06 04:08:00 | NOAA-21 | GUADALUPE | PIAUÍ | Brasil | 2204501 | 22 | 33 | nan | nan | nan | Cerrado | 2.8 |
| 161390cc-c20b-32f2-bd63-ca635ae48b47 | -6.93906 | -42.19421 | 2026-07-06 04:08:00 | NOAA-21 | OEIRAS | PIAUÍ | Brasil | 2207009 | 22 | 33 | nan | nan | nan | Caatinga | 1.3 |
| 43115b51-5bda-3bae-8a5b-b1d0a2facb4b | -13.24195 | -54.32388 | 2026-07-06 04:10:00 | NOAA-21 | PARANATINGA | MATO GROSSO | Brasil | 5106307 | 51 | 33 | nan | nan | nan | Amazônia | 2.7 |
| 71da91df-fe8e-3991-82cd-fc2c966baa6c | -13.20697 | -54.30009 | 2026-07-06 04:10:00 | NOAA-21 | PARANATINGA | MATO GROSSO | Brasil | 5106307 | 51 | 33 | nan | nan | nan | Amazônia | 1.2 |
| e8881159-3a32-325e-821b-f9c9fe798f99 | -13.24109 | -54.31594 | 2026-07-06 04:10:00 | NOAA-21 | PARANATINGA | MATO GROSSO | Brasil | 5106307 | 51 | 33 | nan | nan | nan | Amazônia | 1.8 |
| 709dd81c-ef3f-3954-8f79-0f3bbc95fe29 | -17.0103 | -48.28407 | 2026-07-06 04:10:00 | NOAA-21 | ORIZONA | GOIÁS | Brasil | 5215306 | 52 | 33 | nan | nan | nan | Cerrado | 0.9 |
| 40c9dd0c-1de1-37ff-867e-f6be25170fde | -11.43912 | -46.61686 | 2026-07-06 04:10:00 | NOAA-21 | DIANÓPOLIS | TOCANTINS | Brasil | 1707009 | 17 | 33 | nan | nan | nan | Cerrado | 2.6 |
| 2a94915c-3afb-3e43-a610-0aa86a5f89fd | -13.30816 | -54.36555 | 2026-07-06 04:10:00 | NOAA-21 | PARANATINGA | MATO GROSSO | Brasil | 5106307 | 51 | 33 | nan | nan | nan | Amazônia | 2.7 |
| 6d900ca9-6048-3831-89b4-311240acaa6d | -11.61141 | -46.83614 | 2026-07-06 04:10:00 | NOAA-21 | DIANÓPOLIS | TOCANTINS | Brasil | 1707009 | 17 | 33 | nan | nan | nan | Cerrado | 1.2 |
| f126cbbf-ced5-30ad-9682-88d613ee6511 | -13.29619 | -54.36311 | 2026-07-06 04:10:00 | NOAA-21 | PARANATINGA | MATO GROSSO | Brasil | 5106307 | 51 | 33 | nan | nan | nan | Amazônia | 3.6 |
| 86698d32-5465-374d-a3ad-944c5d19f9ab | -13.20099 | -54.29892 | 2026-07-06 04:10:00 | NOAA-21 | PARANATINGA | MATO GROSSO | Brasil | 5106307 | 51 | 33 | nan | nan | nan | Amazônia | 1.6 |
| 8886e763-e56a-32f5-9e83-e43f49641397 | -11.43995 | -46.6121 | 2026-07-06 04:10:00 | NOAA-21 | DIANÓPOLIS | TOCANTINS | Brasil | 1707009 | 17 | 33 | nan | nan | nan | Cerrado | 1.0 |
| 7cb22f51-c350-3446-bce6-09513a2d09b9 | -12.33947 | -48.22426 | 2026-07-06 04:10:00 | NOAA-21 | PARANÃ | TOCANTINS | Brasil | 1716208 | 17 | 33 | nan | nan | nan | Cerrado | 1.9 |
| c2ced734-63c4-31ed-b540-124b853c73de | -11.45259 | -46.6286 | 2026-07-06 04:10:00 | NOAA-21 | DIANÓPOLIS | TOCANTINS | Brasil | 1707009 | 17 | 33 | nan | nan | nan | Cerrado | 1.5 |
| 3a8887bd-1dfe-3a64-90ac-b8ee79593641 | -11.91437 | -43.38144 | 2026-07-06 04:10:00 | NOAA-21 | MUQUÉM DO SÃO FRANCISCO | BAHIA | Brasil | 2922250 | 29 | 33 | nan | nan | nan | Cerrado | 1.0 |
| deefcac8-8f96-3975-897e-e65170f26c6a | -15.1411 | -42.84658 | 2026-07-06 04:10:00 | NOAA-21 | MONTE AZUL | MINAS GERAIS | Brasil | 3142908 | 31 | 33 | nan | nan | nan | Cerrado | 0.7 |
| 0ac2a1e0-e101-3eb0-8522-336f18fb29dd | -12.75673 | -44.53411 | 2026-07-06 04:10:00 | NOAA-21 | BAIANÓPOLIS | BAHIA | Brasil | 2902500 | 29 | 33 | nan | nan | nan | Cerrado | 0.7 |
| e38fa560-e5be-3cf2-9009-5adc467fb268 | -13.29934 | -54.37825 | 2026-07-06 04:10:00 | NOAA-21 | PARANATINGA | MATO GROSSO | Brasil | 5106307 | 51 | 33 | nan | nan | nan | Amazônia | 2.4 |


[Clique aqui para ver as próximas entradas](README3.md)
