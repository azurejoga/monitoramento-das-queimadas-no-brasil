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

## Dados Diários - Página 128

| ID | Latitude | Longitude | Data/Hora GMT | Satélite | Município | Estado | País | Município ID | Estado ID | País ID | Dias sem Chuva | Precipitação | Risco de Fogo | Bioma | FRP |
|----|----------|-----------|---------------|----------|-----------|--------|------|--------------|-----------|---------|----------------|--------------|----------------|-------|-----|
| cba8a9d9-14a4-3d67-8cbc-bcd3c3a5d0f7 | -19.91757 | -40.74313 | 2026-09-28 17:05:00 | NOAA-21 | SANTA TERESA | ESPÍRITO SANTO | Brasil | 3204609 | 32 | 33 | nan | nan | nan | Mata Atlântica | 7.4 |
| 0b316555-9834-38e7-ad15-7f4705cdebab | -20.96939 | -43.80192 | 2026-09-28 17:05:00 | NOAA-21 | CARANDAÍ | MINAS GERAIS | Brasil | 3113206 | 31 | 33 | nan | nan | nan | Mata Atlântica | 6.9 |
| b3a7b582-d64a-3b32-891f-51f0073ed06f | -21.21409 | -46.70706 | 2026-09-28 17:05:00 | NOAA-21 | GUAXUPÉ | MINAS GERAIS | Brasil | 3128709 | 31 | 33 | nan | nan | nan | Mata Atlântica | 7.7 |
| 57c2c63c-bda3-3822-b3f4-528acca4a26e | -20.66858 | -42.28435 | 2026-09-28 17:05:00 | NOAA-21 | FERVEDOURO | MINAS GERAIS | Brasil | 3125952 | 31 | 33 | nan | nan | nan | Mata Atlântica | 5.8 |
| 169b07b6-0891-34ff-b568-b4fae1ae377f | -20.76906 | -51.30375 | 2026-09-28 17:05:00 | NOAA-21 | ANDRADINA | SÃO PAULO | Brasil | 3502101 | 35 | 33 | nan | nan | nan | Mata Atlântica | 35.5 |
| 169c9085-fd28-39ea-b1af-2a18cf1bceb7 | -20.46322 | -46.23246 | 2026-09-28 17:05:00 | NOAA-21 | VARGEM BONITA | MINAS GERAIS | Brasil | 3170602 | 31 | 33 | nan | nan | nan | Cerrado | 5.0 |
| eef3a3b2-ae0c-3df8-bf06-c09230192c46 | -23.05239 | -51.16136 | 2026-09-28 17:05:00 | NOAA-21 | SERTANÓPOLIS | PARANÁ | Brasil | 4126504 | 41 | 33 | nan | nan | nan | Mata Atlântica | 5.6 |
| adf13108-5b71-36fa-b8c9-1029e70eb6e2 | -21.86098 | -45.46669 | 2026-09-28 17:05:00 | NOAA-21 | CAMPANHA | MINAS GERAIS | Brasil | 3110905 | 31 | 33 | nan | nan | nan | Mata Atlântica | 3.2 |
| 638c66db-4d60-31d2-a44f-1692d5a8885f | -20.3531 | -46.3885 | 2026-09-28 17:05:00 | NOAA-21 | VARGEM BONITA | MINAS GERAIS | Brasil | 3170602 | 31 | 33 | nan | nan | nan | Cerrado | 8.3 |
| 786d2263-a879-3943-99b8-e62571b482ae | -19.97457 | -44.47746 | 2026-09-28 17:05:00 | NOAA-21 | MATEUS LEME | MINAS GERAIS | Brasil | 3140704 | 31 | 33 | nan | nan | nan | Mata Atlântica | 10.5 |
| 3ed5ca71-bb9d-395d-803c-09551392c0ef | -23.30848 | -51.4116 | 2026-09-28 17:05:00 | NOAA-21 | ROLÂNDIA | PARANÁ | Brasil | 4122404 | 41 | 33 | nan | nan | nan | Mata Atlântica | 2.5 |
| 71f35ced-7b0c-35ea-bcca-5d00028ac5d4 | -23.32019 | -50.91536 | 2026-09-28 17:05:00 | NOAA-21 | JATAIZINHO | PARANÁ | Brasil | 4112702 | 41 | 33 | nan | nan | nan | Mata Atlântica | 9.2 |
| 0c17c831-4ddd-3258-8270-b92c43c3d0f4 | -20.45679 | -46.22108 | 2026-09-28 17:05:00 | NOAA-21 | VARGEM BONITA | MINAS GERAIS | Brasil | 3170602 | 31 | 33 | nan | nan | nan | Cerrado | 15.1 |
| a5f96f99-7b0f-382f-a07c-b905293ce37c | -19.59039 | -45.0314 | 2026-09-28 17:05:00 | NOAA-21 | LEANDRO FERREIRA | MINAS GERAIS | Brasil | 3138302 | 31 | 33 | nan | nan | nan | Cerrado | 12.1 |
| 02c172b1-e0b7-34ea-8333-a2413a9229c9 | -19.5958 | -44.86642 | 2026-09-28 17:05:00 | NOAA-21 | PITANGUI | MINAS GERAIS | Brasil | 3151404 | 31 | 33 | nan | nan | nan | Cerrado | 9.7 |
| 31d8c6d8-ea96-3890-9bf7-de59599286ce | -20.75967 | -51.30925 | 2026-09-28 17:05:00 | NOAA-21 | ANDRADINA | SÃO PAULO | Brasil | 3502101 | 35 | 33 | nan | nan | nan | Mata Atlântica | 6.9 |
| 7b48e3c2-ad66-33d4-99cf-671b2e2b345b | -21.08966 | -43.26111 | 2026-09-28 17:05:00 | NOAA-21 | MERCÊS | MINAS GERAIS | Brasil | 3141603 | 31 | 33 | nan | nan | nan | Mata Atlântica | 12.7 |
| e93b9f41-26ee-35d5-a27f-228d23f0a6c3 | -20.04437 | -48.05577 | 2026-09-28 17:05:00 | NOAA-21 | ÁGUA COMPRIDA | MINAS GERAIS | Brasil | 3100708 | 31 | 33 | nan | nan | nan | Cerrado | 44.6 |
| 78ea4133-7498-3a8e-a216-097fe54ee396 | -20.66934 | -42.28796 | 2026-09-28 17:05:00 | NOAA-21 | FERVEDOURO | MINAS GERAIS | Brasil | 3125952 | 31 | 33 | nan | nan | nan | Mata Atlântica | 6.0 |
| 209cf5c4-cb32-37c0-8bcc-60b38ba06062 | -21.85748 | -43.09945 | 2026-09-28 17:05:00 | NOAA-21 | MAR DE ESPANHA | MINAS GERAIS | Brasil | 3139805 | 31 | 33 | nan | nan | nan | Mata Atlântica | 7.0 |
| b0295611-176b-357c-ae6f-3472ae182e4f | -19.96998 | -44.47892 | 2026-09-28 17:05:00 | NOAA-21 | MATEUS LEME | MINAS GERAIS | Brasil | 3140704 | 31 | 33 | nan | nan | nan | Mata Atlântica | 10.5 |
| d8a620ef-dfcc-3ec3-9c6f-569d7095df19 | -20.75185 | -42.91412 | 2026-09-28 17:05:00 | NOAA-21 | VIÇOSA | MINAS GERAIS | Brasil | 3171303 | 31 | 33 | nan | nan | nan | Mata Atlântica | 3.3 |
| b5cb19f4-fe80-3d34-81e5-1b32ae4f95ec | -20.97081 | -43.80353 | 2026-09-28 17:05:00 | NOAA-21 | CARANDAÍ | MINAS GERAIS | Brasil | 3113206 | 31 | 33 | nan | nan | nan | Mata Atlântica | 9.8 |
| c55f37b0-b39b-32b6-8bc8-0a75abcec224 | -21.06036 | -55.52395 | 2026-09-28 17:05:00 | NOAA-21 | NIOAQUE | MATO GROSSO DO SUL | Brasil | 5005806 | 50 | 33 | nan | nan | nan | Cerrado | 3.5 |
| e805bcab-dbc7-3d48-84a8-565124d860d9 | -20.859 | -44.89309 | 2026-09-28 17:05:00 | NOAA-21 | SANTO ANTÔNIO DO AMPARO | MINAS GERAIS | Brasil | 3159902 | 31 | 33 | nan | nan | nan | Mata Atlântica | 6.7 |
| 81b10cb0-a1a6-38a6-aaca-264d45d4a5f7 | -20.0632 | -40.36872 | 2026-09-28 17:05:00 | NOAA-21 | SERRA | ESPÍRITO SANTO | Brasil | 3205002 | 32 | 33 | nan | nan | nan | Mata Atlântica | 12.2 |
| 81771259-a09e-31d4-a20c-e5dc9945383c | -22.25216 | -44.66906 | 2026-09-28 17:05:00 | NOAA-21 | ITAMONTE | MINAS GERAIS | Brasil | 3133006 | 31 | 33 | nan | nan | nan | Mata Atlântica | 16.3 |
| 9ffba03d-ed53-3eb4-a4a6-e82f9a41d5f1 | -20.77629 | -51.30627 | 2026-09-28 17:05:00 | NOAA-21 | ANDRADINA | SÃO PAULO | Brasil | 3502101 | 35 | 33 | nan | nan | nan | Mata Atlântica | 18.5 |
| 049b3f2b-17f1-3f4b-871c-8c136d30a4e9 | -19.85111 | -42.0799 | 2026-09-28 17:05:00 | NOAA-21 | SANTA RITA DE MINAS | MINAS GERAIS | Brasil | 3159357 | 31 | 33 | nan | nan | nan | Mata Atlântica | 2.8 |
| 96e53a3b-d709-3991-bd51-166a351a6505 | -20.43907 | -47.24936 | 2026-09-28 17:05:00 | NOAA-21 | CLARAVAL | MINAS GERAIS | Brasil | 3116407 | 31 | 33 | nan | nan | nan | Cerrado | 7.5 |
| 5e6904fe-4ef9-3d30-99b0-8ee167f67d2f | -21.60726 | -46.53784 | 2026-09-28 17:05:00 | NOAA-21 | CACONDE | SÃO PAULO | Brasil | 3508702 | 35 | 33 | nan | nan | nan | Mata Atlântica | 9.5 |
| 0fdaa11a-5b6e-3389-9552-c88d18e4aead | -19.15702 | -43.82369 | 2026-09-28 17:05:00 | NOAA-21 | BALDIM | MINAS GERAIS | Brasil | 3105004 | 31 | 33 | nan | nan | nan | Cerrado | 4.1 |
| dd6ddbb3-9202-37db-9024-6edee48c4c5d | -20.05634 | -41.93892 | 2026-09-28 17:05:00 | NOAA-21 | SANTANA DO MANHUAÇU | MINAS GERAIS | Brasil | 3158904 | 31 | 33 | nan | nan | nan | Mata Atlântica | 1.6 |
| 02584a67-6090-301c-959e-aeb3f77a18f1 | -20.06174 | -41.93733 | 2026-09-28 17:05:00 | NOAA-21 | SANTANA DO MANHUAÇU | MINAS GERAIS | Brasil | 3158904 | 31 | 33 | nan | nan | nan | Mata Atlântica | 3.3 |
| 5a54587e-64b6-3417-9b86-9179e674990b | -19.88337 | -45.87212 | 2026-09-28 17:05:00 | NOAA-21 | CÓRREGO DANTA | MINAS GERAIS | Brasil | 3119807 | 31 | 33 | nan | nan | nan | Cerrado | 2.3 |
| 6efedf4c-9ffb-3ef1-b6a1-8b783ef52880 | -19.92609 | -45.07051 | 2026-09-28 17:05:00 | NOAA-21 | PERDIGÃO | MINAS GERAIS | Brasil | 3149705 | 31 | 33 | nan | nan | nan | Cerrado | 4.7 |
| 87445159-76e5-3713-8568-855e6a7e9743 | -21.55317 | -46.40382 | 2026-09-28 17:05:00 | NOAA-21 | CABO VERDE | MINAS GERAIS | Brasil | 3109501 | 31 | 33 | nan | nan | nan | Mata Atlântica | 5.6 |
| 5f615b66-5920-3ebb-a186-3cc1b406fa20 | -20.46283 | -45.57761 | 2026-09-28 17:05:00 | NOAA-21 | CÓRREGO FUNDO | MINAS GERAIS | Brasil | 3119955 | 31 | 33 | nan | nan | nan | Cerrado | 6.4 |
| 53306253-50d1-3ba5-add4-f6ed5fd1b464 | -21.64214 | -43.66381 | 2026-09-28 17:05:00 | NOAA-21 | JUIZ DE FORA | MINAS GERAIS | Brasil | 3136702 | 31 | 33 | nan | nan | nan | Mata Atlântica | 16.3 |
| 6caeae2f-eb70-31d2-aeec-55ac6342a8fa | -23.13369 | -50.9181 | 2026-09-28 17:05:00 | NOAA-21 | RANCHO ALEGRE | PARANÁ | Brasil | 4121307 | 41 | 33 | nan | nan | nan | Mata Atlântica | 16.1 |
| 9a1a5575-8e71-34de-9569-c1a388caaac8 | -19.27875 | -44.12151 | 2026-09-28 17:05:00 | NOAA-21 | JEQUITIBÁ | MINAS GERAIS | Brasil | 3135704 | 31 | 33 | nan | nan | nan | Cerrado | 5.6 |
| dfbe8c0b-0bb7-3069-a65d-b8262e31d127 | -21.23501 | -45.62099 | 2026-09-28 17:05:00 | NOAA-21 | CAMPOS GERAIS | MINAS GERAIS | Brasil | 3111606 | 31 | 33 | nan | nan | nan | Mata Atlântica | 4.4 |
| 0dd2b0d0-ea51-3612-b9ec-9223ed563baf | -20.20474 | -48.57116 | 2026-09-28 17:05:00 | NOAA-21 | GUAÍRA | SÃO PAULO | Brasil | 3517406 | 35 | 33 | nan | nan | nan | Cerrado | 41.3 |
| bfca483a-aa6b-3666-86f0-8d98eaca7ced | -19.44269 | -41.94067 | 2026-09-28 17:05:00 | NOAA-21 | INHAPIM | MINAS GERAIS | Brasil | 3130903 | 31 | 33 | nan | nan | nan | Mata Atlântica | 7.4 |
| abefcd5d-3f8d-3962-ae8d-24cb894e121b | -21.25475 | -46.07054 | 2026-09-28 17:05:00 | NOAA-21 | ALTEROSA | MINAS GERAIS | Brasil | 3102001 | 31 | 33 | nan | nan | nan | Mata Atlântica | 5.2 |
| 68a411eb-c3d2-38ba-ab7e-07bdf9a1305d | -22.63271 | -54.94989 | 2026-09-28 17:05:00 | NOAA-21 | CAARAPÓ | MATO GROSSO DO SUL | Brasil | 5002407 | 50 | 33 | nan | nan | nan | Mata Atlântica | 49.2 |
| 4ef2deff-ebd1-3b10-b029-0c51c522c4bf | -23.13945 | -50.91395 | 2026-09-28 17:05:00 | NOAA-21 | RANCHO ALEGRE | PARANÁ | Brasil | 4121307 | 41 | 33 | nan | nan | nan | Mata Atlântica | 5.2 |
| bdcb8731-dfad-3251-b2fc-d456edc1e144 | -19.10581 | -43.95626 | 2026-09-28 17:05:00 | NOAA-21 | SANTANA DE PIRAPAMA | MINAS GERAIS | Brasil | 3158508 | 31 | 33 | nan | nan | nan | Cerrado | 12.3 |
| 82f13ad8-437f-3312-bc03-ea4c6610ef18 | -20.31155 | -41.74226 | 2026-09-28 17:05:00 | NOAA-21 | IÚNA | ESPÍRITO SANTO | Brasil | 3203007 | 32 | 33 | nan | nan | nan | Mata Atlântica | 5.5 |
| 6041858c-ad10-3a5e-a0b5-64bca72c76a0 | -21.33213 | -43.97196 | 2026-09-28 17:05:00 | NOAA-21 | BARBACENA | MINAS GERAIS | Brasil | 3105608 | 31 | 33 | nan | nan | nan | Mata Atlântica | 9.2 |
| a7b8f60f-fe50-34bd-a9ce-ed7927c24d38 | -20.43515 | -47.25012 | 2026-09-28 17:05:00 | NOAA-21 | CLARAVAL | MINAS GERAIS | Brasil | 3116407 | 31 | 33 | nan | nan | nan | Cerrado | 8.9 |
| 9f29da93-d1e3-3c19-b83d-b24f83ebe6c5 | -20.75635 | -51.30984 | 2026-09-28 17:05:00 | NOAA-21 | ANDRADINA | SÃO PAULO | Brasil | 3502101 | 35 | 33 | nan | nan | nan | Mata Atlântica | 11.7 |
| fc61d44b-dcac-3066-902b-11b432179ce5 | -21.47125 | -43.77507 | 2026-09-28 17:05:00 | NOAA-21 | ANTÔNIO CARLOS | MINAS GERAIS | Brasil | 3102902 | 31 | 33 | nan | nan | nan | Mata Atlântica | 9.2 |
| 70d17977-8779-3103-8b78-1679475ed60f | -21.53934 | -45.61446 | 2026-09-28 17:05:00 | NOAA-21 | ELÓI MENDES | MINAS GERAIS | Brasil | 3123601 | 31 | 33 | nan | nan | nan | Mata Atlântica | 13.5 |
| a8129cdc-29fb-38da-877b-2fc2e35c27bb | -20.77962 | -51.30568 | 2026-09-28 17:05:00 | NOAA-21 | ANDRADINA | SÃO PAULO | Brasil | 3502101 | 35 | 33 | nan | nan | nan | Mata Atlântica | 18.7 |
| da383ce8-14cc-3237-b4bb-1f29e2affefc | -22.12082 | -46.5837 | 2026-09-28 17:05:00 | NOAA-21 | ANDRADAS | MINAS GERAIS | Brasil | 3102605 | 31 | 33 | nan | nan | nan | Mata Atlântica | 5.0 |
| e38d14d7-e281-38f8-aa70-614891a11f6b | -21.35859 | -51.50778 | 2026-09-28 17:05:00 | NOAA-21 | TUPI PAULISTA | SÃO PAULO | Brasil | 3555109 | 35 | 33 | nan | nan | nan | Mata Atlântica | 4.0 |
| ae3ae4ea-7877-3ae9-bebd-7e7819fb0132 | -20.04151 | -42.98374 | 2026-09-28 17:05:00 | NOAA-21 | ALVINÓPOLIS | MINAS GERAIS | Brasil | 3102308 | 31 | 33 | nan | nan | nan | Mata Atlântica | 3.6 |
| 0e5b81c2-edd7-33b0-9f60-96573a4ae093 | -20.31271 | -41.74302 | 2026-09-28 17:05:00 | NOAA-21 | IÚNA | ESPÍRITO SANTO | Brasil | 3203007 | 32 | 33 | nan | nan | nan | Mata Atlântica | 5.2 |
| 8b6592bd-102f-3a1c-9e82-73cd0a30529d | -20.76965 | -51.30746 | 2026-09-28 17:05:00 | NOAA-21 | ANDRADINA | SÃO PAULO | Brasil | 3502101 | 35 | 33 | nan | nan | nan | Mata Atlântica | 35.5 |
| 41d492e0-c4fc-35fc-ae23-723d24f174c8 | -20.03703 | -47.73167 | 2026-09-28 17:05:00 | NOAA-21 | IGARAPAVA | SÃO PAULO | Brasil | 3520103 | 35 | 33 | nan | nan | nan | Cerrado | 21.3 |
| 9e743630-873f-378c-b7fc-2b95d64f8086 | -19.58994 | -45.02875 | 2026-09-28 17:05:00 | NOAA-21 | LEANDRO FERREIRA | MINAS GERAIS | Brasil | 3138302 | 31 | 33 | nan | nan | nan | Mata Atlântica | 19.7 |
| 859a9c1f-dd4b-3de5-9f9f-847e778fed23 | -20.80735 | -51.74583 | 2026-09-28 17:05:00 | NOAA-21 | TRÊS LAGOAS | MATO GROSSO DO SUL | Brasil | 5008305 | 50 | 33 | nan | nan | nan | Cerrado | 5.4 |
| cc0d49da-29e8-3f9b-b245-ad441f5ed5c8 | -18.80994 | -40.23679 | 2026-09-28 17:05:00 | NOAA-21 | SÃO MATEUS | ESPÍRITO SANTO | Brasil | 3204906 | 32 | 33 | nan | nan | nan | Mata Atlântica | 5.1 |
| a425c010-3d28-3565-9072-758e64b12ba4 | -20.29807 | -46.0957 | 2026-09-28 17:05:00 | NOAA-21 | BAMBUÍ | MINAS GERAIS | Brasil | 3105103 | 31 | 33 | nan | nan | nan | Cerrado | 6.4 |
| 95b281c6-337c-360a-bc03-456f574f42d7 | -23.07021 | -50.88324 | 2026-09-28 17:05:00 | NOAA-21 | RANCHO ALEGRE | PARANÁ | Brasil | 4121307 | 41 | 33 | nan | nan | nan | Mata Atlântica | 1.6 |
| 158c6ae1-538a-38f3-acfa-5c4a277b48f6 | -18.79987 | -42.23101 | 2026-09-28 17:05:00 | NOAA-21 | GOVERNADOR VALADARES | MINAS GERAIS | Brasil | 3127701 | 31 | 33 | nan | nan | nan | Mata Atlântica | 9.3 |
| 1e10fd82-cedc-33f7-8997-cf8693fac476 | -23.32351 | -50.91475 | 2026-09-28 17:05:00 | NOAA-21 | JATAIZINHO | PARANÁ | Brasil | 4112702 | 41 | 33 | nan | nan | nan | Mata Atlântica | 3.7 |
| eaaecb0a-f8a1-33f5-8ba8-1c59ce796f85 | -11.66429 | -43.52908 | 2026-09-28 17:07:00 | NOAA-21 | BARRA | BAHIA | Brasil | 2902708 | 29 | 33 | nan | nan | nan | Cerrado | 18.5 |
| 45173571-186c-379c-a056-f3a41c67f1bd | -11.9997 | -44.92871 | 2026-09-28 17:07:00 | NOAA-21 | RIACHÃO DAS NEVES | BAHIA | Brasil | 2926202 | 29 | 33 | nan | nan | nan | Cerrado | 6.5 |
| da29adc3-0ff8-3449-8e15-7bd7afa7bd52 | -18.3219 | -44.32154 | 2026-09-28 17:07:00 | NOAA-21 | CURVELO | MINAS GERAIS | Brasil | 3120904 | 31 | 33 | nan | nan | nan | Cerrado | 9.2 |
| 9be6ebc0-f715-36e9-bb90-35833f4c1e8e | -18.75014 | -46.22765 | 2026-09-28 17:07:00 | NOAA-21 | LAGOA FORMOSA | MINAS GERAIS | Brasil | 3137502 | 31 | 33 | nan | nan | nan | Cerrado | 9.2 |
| 5bc37eaf-09f3-3a2a-8aa5-0471c8dfd8af | -14.48389 | -53.63955 | 2026-09-28 17:07:00 | NOAA-21 | PARANATINGA | MATO GROSSO | Brasil | 5106307 | 51 | 33 | nan | nan | nan | Cerrado | 5.9 |
| 91a53cbf-74ad-3838-9a8d-1be073039f97 | -11.3981 | -43.42438 | 2026-09-28 17:07:00 | NOAA-21 | BARRA | BAHIA | Brasil | 2902708 | 29 | 33 | nan | nan | nan | Cerrado | 125.3 |
| 413f783b-9da0-39a2-8cb8-ffbf66771ed0 | -11.95836 | -44.88455 | 2026-09-28 17:07:00 | NOAA-21 | RIACHÃO DAS NEVES | BAHIA | Brasil | 2926202 | 29 | 33 | nan | nan | nan | Cerrado | 8.6 |
| 031a90ad-23c5-36a1-9fba-f07805e1d413 | -12.10177 | -47.3992 | 2026-09-28 17:07:00 | NOAA-21 | CONCEIÇÃO DO TOCANTINS | TOCANTINS | Brasil | 1705607 | 17 | 33 | nan | nan | nan | Cerrado | 13.7 |
| 9acc0df0-fcac-33e5-ba79-2ec92470df6c | -11.38897 | -43.4401 | 2026-09-28 17:07:00 | NOAA-21 | BARRA | BAHIA | Brasil | 2902708 | 29 | 33 | nan | nan | nan | Cerrado | 19.3 |
| c56fe34b-63dc-3339-8394-1e636861a2f6 | -11.689 | -43.44012 | 2026-09-28 17:07:00 | NOAA-21 | BARRA | BAHIA | Brasil | 2902708 | 29 | 33 | nan | nan | nan | Cerrado | 7.4 |
| b2d7dd5b-986f-343b-9515-393ac7efa549 | -24.73697 | -49.49202 | 2026-09-28 17:07:00 | NOAA-21 | CERRO AZUL | PARANÁ | Brasil | 4105201 | 41 | 33 | nan | nan | nan | Mata Atlântica | 8.3 |
| d64d62ee-7c94-3924-a335-d3a6f6a90810 | -12.87833 | -44.81496 | 2026-09-28 17:07:00 | NOAA-21 | SÃO DESIDÉRIO | BAHIA | Brasil | 2928901 | 29 | 33 | nan | nan | nan | Cerrado | 14.8 |
| c4bbcd5b-2494-3884-a949-22f1e37fa428 | -12.76839 | -50.98504 | 2026-09-28 17:07:00 | NOAA-21 | RIBEIRÃO CASCALHEIRA | MATO GROSSO | Brasil | 5107180 | 51 | 33 | nan | nan | nan | Cerrado | 8.3 |
| 59993db1-18d4-3173-bc9c-5bf912420957 | -11.36796 | -43.42617 | 2026-09-28 17:07:00 | NOAA-21 | BARRA | BAHIA | Brasil | 2902708 | 29 | 33 | nan | nan | nan | Cerrado | 13.8 |
| dd714b5a-e537-338a-8620-d13421c7ee40 | -15.55755 | -47.92841 | 2026-09-28 17:07:00 | NOAA-21 | BRASÍLIA | DISTRITO FEDERAL | Brasil | 5300108 | 53 | 33 | nan | nan | nan | Cerrado | 19.7 |
| 206492e5-7b1b-36fb-9f07-40a976d2b0f6 | -14.83919 | -41.47223 | 2026-09-28 17:07:00 | NOAA-21 | TREMEDAL | BAHIA | Brasil | 2931806 | 29 | 33 | nan | nan | nan | Caatinga | 6.7 |
| 010a90a3-8e91-389a-bd96-d27d88bcf87b | -15.02357 | -41.65826 | 2026-09-28 17:07:00 | NOAA-21 | PIRIPÁ | BAHIA | Brasil | 2924702 | 29 | 33 | nan | nan | nan | Mata Atlântica | 3.6 |
| 4fd28fde-0dd0-3469-9f51-e2f27a78056c | -12.46308 | -45.19687 | 2026-09-28 17:07:00 | NOAA-21 | SÃO DESIDÉRIO | BAHIA | Brasil | 2928901 | 29 | 33 | nan | nan | nan | Cerrado | 4.4 |
| 30bb5045-e14a-3fdf-a460-5632c4c3751e | -12.67001 | -46.98726 | 2026-09-28 17:07:00 | NOAA-21 | ARRAIAS | TOCANTINS | Brasil | 1702406 | 17 | 33 | nan | nan | nan | Cerrado | 8.6 |
| 70364990-4aa8-3d09-9e42-fedb1bdbd78f | -14.86753 | -41.02606 | 2026-09-28 17:07:00 | NOAA-21 | VITÓRIA DA CONQUISTA | BAHIA | Brasil | 2933307 | 29 | 33 | nan | nan | nan | Mata Atlântica | 21.9 |
| e301d7a6-c2d2-3912-8dd8-055875ce1f76 | -18.08345 | -44.53937 | 2026-09-28 17:07:00 | NOAA-21 | CORINTO | MINAS GERAIS | Brasil | 3119104 | 31 | 33 | nan | nan | nan | Cerrado | 8.1 |
| 50334459-b0b6-3bba-9025-7ec1ad02316f | -17.81364 | -44.42891 | 2026-09-28 17:07:00 | NOAA-21 | LASSANCE | MINAS GERAIS | Brasil | 3138104 | 31 | 33 | nan | nan | nan | Cerrado | 18.2 |
| f8673663-f78c-3f54-a64d-9693af9c3f02 | -11.37468 | -43.42934 | 2026-09-28 17:07:00 | NOAA-21 | BARRA | BAHIA | Brasil | 2902708 | 29 | 33 | nan | nan | nan | Cerrado | 22.1 |
| 09be324f-891f-3c6a-a04a-6f1f99b85e76 | -18.76589 | -47.61292 | 2026-09-28 17:07:00 | NOAA-21 | MONTE CARMELO | MINAS GERAIS | Brasil | 3143104 | 31 | 33 | nan | nan | nan | Cerrado | 19.0 |
| 6796dbce-416c-34e4-912a-392e39844a63 | -12.49179 | -44.7237 | 2026-09-28 17:07:00 | NOAA-21 | BAIANÓPOLIS | BAHIA | Brasil | 2902500 | 29 | 33 | nan | nan | nan | Cerrado | 22.0 |
| 588596d5-02a9-3e8c-835e-f39681abcc8d | -17.68322 | -44.75432 | 2026-09-28 17:07:00 | NOAA-21 | VÁRZEA DA PALMA | MINAS GERAIS | Brasil | 3170800 | 31 | 33 | nan | nan | nan | Cerrado | 14.5 |
| 09a00812-1c07-3e4c-ba00-19be3f52e703 | -16.63269 | -48.47313 | 2026-09-28 17:07:00 | NOAA-21 | SILVÂNIA | GOIÁS | Brasil | 5220603 | 52 | 33 | nan | nan | nan | Cerrado | 16.3 |
| fb86d441-349b-3868-8a8c-7c50ed69dc95 | -15.15082 | -44.02691 | 2026-09-28 17:07:00 | NOAA-21 | JAÍBA | MINAS GERAIS | Brasil | 3135050 | 31 | 33 | nan | nan | nan | Cerrado | 4.7 |
| 9ff52b3c-a7ff-3ba8-b459-72a6792f1305 | -16.34881 | -42.57874 | 2026-09-28 17:07:00 | NOAA-21 | PADRE CARVALHO | MINAS GERAIS | Brasil | 3146255 | 31 | 33 | nan | nan | nan | Cerrado | 25.6 |
| f76382c9-0b97-395f-9566-be2e35554eba | -17.57771 | -46.90994 | 2026-09-28 17:07:00 | NOAA-21 | GUARDA-MOR | MINAS GERAIS | Brasil | 3128600 | 31 | 33 | nan | nan | nan | Cerrado | 6.5 |
| 51f88daa-1e78-3dfa-b633-66d4f080f40c | -12.95344 | -43.36184 | 2026-09-28 17:07:00 | NOAA-21 | BOM JESUS DA LAPA | BAHIA | Brasil | 2903904 | 29 | 33 | nan | nan | nan | Cerrado | 57.0 |
| defcf246-9572-39e7-a25c-fbcc69e54101 | -15.42923 | -39.09779 | 2026-09-28 17:07:00 | NOAA-21 | SANTA LUZIA | BAHIA | Brasil | 2928059 | 29 | 33 | nan | nan | nan | Mata Atlântica | 9.9 |


[Clique aqui para ver as próximas entradas](README129.md)
