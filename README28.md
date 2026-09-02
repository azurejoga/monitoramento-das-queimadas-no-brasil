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

## Dados Diários - Página 28

| ID | Latitude | Longitude | Data/Hora GMT | Satélite | Município | Estado | País | Município ID | Estado ID | País ID | Dias sem Chuva | Precipitação | Risco de Fogo | Bioma | FRP |
|----|----------|-----------|---------------|----------|-----------|--------|------|--------------|-----------|---------|----------------|--------------|----------------|-------|-----|
| 3e80da75-7d91-361a-83fa-c74dfc30ac1c | -13.41656 | -43.87983 | 2026-09-02 04:21:00 | NOAA-21 | SERRA DO RAMALHO | BAHIA | Brasil | 2930154 | 29 | 33 | nan | nan | nan | Cerrado | 8.2 |
| 5cba3f44-8313-3245-bb83-3506e48ea628 | -10.96524 | -50.49216 | 2026-09-02 04:21:00 | NOAA-21 | LAGOA DA CONFUSÃO | TOCANTINS | Brasil | 1711902 | 17 | 33 | nan | nan | nan | Cerrado | 17.3 |
| ad883ebd-1a55-317a-83ce-e9b6eacca48d | -12.11826 | -47.04975 | 2026-09-02 04:21:00 | NOAA-21 | TAIPAS DO TOCANTINS | TOCANTINS | Brasil | 1720937 | 17 | 33 | nan | nan | nan | Cerrado | 1.1 |
| 412830cd-eee4-3a44-9f49-4c3ec8f06790 | -11.29867 | -45.18032 | 2026-09-02 04:21:00 | NOAA-21 | FORMOSA DO RIO PRETO | BAHIA | Brasil | 2911105 | 29 | 33 | nan | nan | nan | Cerrado | 3.2 |
| d5c579aa-20e9-33e0-bb67-a8953fe36c21 | -9.21988 | -47.98087 | 2026-09-02 04:21:00 | NOAA-21 | PEDRO AFONSO | TOCANTINS | Brasil | 1716505 | 17 | 33 | nan | nan | nan | Cerrado | 1.0 |
| 6f000b19-30c8-3b4a-9ebb-f22d0b6f2d5b | -8.43232 | -54.70557 | 2026-09-02 04:21:00 | NOAA-21 | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 5.4 |
| 2930b124-d0db-3802-ad61-75e130101af1 | -10.89743 | -45.3368 | 2026-09-02 04:21:00 | NOAA-21 | FORMOSA DO RIO PRETO | BAHIA | Brasil | 2911105 | 29 | 33 | nan | nan | nan | Cerrado | 21.6 |
| dc8fb3eb-cf3d-3b1f-8e2e-6df28f317f7c | -14.9652 | -48.11447 | 2026-09-02 04:21:00 | NOAA-21 | MIMOSO DE GOIÁS | GOIÁS | Brasil | 5213053 | 52 | 33 | nan | nan | nan | Cerrado | 6.7 |
| 6c4b2212-e47a-3848-b568-5307c3d36cfd | -11.30253 | -45.17728 | 2026-09-02 04:21:00 | NOAA-21 | FORMOSA DO RIO PRETO | BAHIA | Brasil | 2911105 | 29 | 33 | nan | nan | nan | Cerrado | 5.0 |
| d0204db4-3c73-3e40-b8b9-ff8e42162923 | -15.59792 | -46.45902 | 2026-09-02 04:21:00 | NOAA-21 | BURITIS | MINAS GERAIS | Brasil | 3109303 | 31 | 33 | nan | nan | nan | Cerrado | 1.4 |
| d0addf91-9b69-3bd0-a81e-c86c01d28e68 | -12.14247 | -47.11241 | 2026-09-02 04:21:00 | NOAA-21 | CONCEIÇÃO DO TOCANTINS | TOCANTINS | Brasil | 1705607 | 17 | 33 | nan | nan | nan | Cerrado | 1.9 |
| 7e27f2d5-d05f-37b9-b554-d513c266fbe3 | -12.11435 | -47.05278 | 2026-09-02 04:21:00 | NOAA-21 | TAIPAS DO TOCANTINS | TOCANTINS | Brasil | 1720937 | 17 | 33 | nan | nan | nan | Cerrado | 1.6 |
| 9330b3d9-0bbf-3bdb-b133-bea119923af3 | -8.24948 | -49.5071 | 2026-09-02 04:21:00 | NOAA-21 | CONCEIÇÃO DO ARAGUAIA | PARÁ | Brasil | 1502707 | 15 | 33 | nan | nan | nan | Amazônia | 5.6 |
| 468939f3-5afa-3d93-80db-a608126b819d | -14.98993 | -47.98345 | 2026-09-02 04:21:00 | NOAA-21 | ÁGUA FRIA DE GOIÁS | GOIÁS | Brasil | 5200175 | 52 | 33 | nan | nan | nan | Cerrado | 3.2 |
| eaff4a72-d14f-3939-9139-5466004ad164 | -10.90129 | -45.33381 | 2026-09-02 04:21:00 | NOAA-21 | FORMOSA DO RIO PRETO | BAHIA | Brasil | 2911105 | 29 | 33 | nan | nan | nan | Cerrado | 4.5 |
| 966e2b6d-9ddf-3b13-813a-4a478e0f2833 | -8.44906 | -54.70514 | 2026-09-02 04:21:00 | NOAA-21 | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 1.7 |
| 4674fa3f-f5a5-3b81-9ad4-b40bed566119 | -15.34129 | -47.0386 | 2026-09-02 04:21:00 | NOAA-21 | FORMOSA | GOIÁS | Brasil | 5208004 | 52 | 33 | nan | nan | nan | Cerrado | 0.6 |
| 1c6ab6c3-f230-33b0-8ac8-53b32fc357e8 | -10.49806 | -59.60797 | 2026-09-02 04:21:00 | NOAA-21 | ARIPUANÃ | MATO GROSSO | Brasil | 5101407 | 51 | 33 | nan | nan | nan | Amazônia | 4.9 |
| b185fdb0-4301-3cfb-87c9-c6ed76db15aa | -13.75286 | -43.82981 | 2026-09-02 04:21:00 | NOAA-21 | CARINHANHA | BAHIA | Brasil | 2907103 | 29 | 33 | nan | nan | nan | Cerrado | 3.6 |
| e768cc57-9bd9-36fb-a2dc-f5734f6a0ca3 | -12.0936 | -47.09701 | 2026-09-02 04:21:00 | NOAA-21 | CONCEIÇÃO DO TOCANTINS | TOCANTINS | Brasil | 1705607 | 17 | 33 | nan | nan | nan | Cerrado | 1.6 |
| 2bd70134-a5c8-3bc2-9794-a7632fe2b029 | -8.13134 | -54.95451 | 2026-09-02 04:21:00 | NOAA-21 | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 3.1 |
| 0699977e-d6d7-347a-8e49-8af415feac62 | -12.27823 | -44.54109 | 2026-09-02 04:21:00 | NOAA-21 | BAIANÓPOLIS | BAHIA | Brasil | 2902500 | 29 | 33 | nan | nan | nan | Cerrado | 0.9 |
| 0a3ab2c2-effe-308f-80e3-9ef99c19e14f | -11.30687 | -45.1489 | 2026-09-02 04:21:00 | NOAA-21 | FORMOSA DO RIO PRETO | BAHIA | Brasil | 2911105 | 29 | 33 | nan | nan | nan | Cerrado | 4.1 |
| fe4cf2fc-717e-34cc-bd3d-da0a83fb0c1b | -12.1415 | -47.07553 | 2026-09-02 04:21:00 | NOAA-21 | TAIPAS DO TOCANTINS | TOCANTINS | Brasil | 1720937 | 17 | 33 | nan | nan | nan | Cerrado | 3.2 |
| ef2f5f67-c81e-39db-9e95-7d7a0d87a85f | -7.97655 | -52.09238 | 2026-09-02 04:21:00 | NOAA-21 | OURILÂNDIA DO NORTE | PARÁ | Brasil | 1505437 | 15 | 33 | nan | nan | nan | Amazônia | 1.8 |
| ff801c28-43fb-3c1f-9274-6c976b6b66b4 | -13.75638 | -43.83034 | 2026-09-02 04:21:00 | NOAA-21 | CARINHANHA | BAHIA | Brasil | 2907103 | 29 | 33 | nan | nan | nan | Cerrado | 3.6 |
| a63b1377-5bfb-38aa-bc25-30c203e809a8 | -11.05547 | -51.52947 | 2026-09-02 04:21:00 | NOAA-21 | CANABRAVA DO NORTE | MATO GROSSO | Brasil | 5102694 | 51 | 33 | nan | nan | nan | Cerrado | 1.4 |
| c7912ab1-f465-35ff-8be0-e650c0910b84 | -15.66652 | -45.89662 | 2026-09-02 04:21:00 | NOAA-21 | ARINOS | MINAS GERAIS | Brasil | 3104502 | 31 | 33 | nan | nan | nan | Cerrado | 1.1 |
| caaccf03-75fa-321c-822c-803f484e0d2c | -8.79103 | -46.47502 | 2026-09-02 04:21:00 | NOAA-21 | BALSAS | MARANHÃO | Brasil | 2101400 | 21 | 33 | nan | nan | nan | Cerrado | 1.7 |
| 8b907e0a-f7e8-3f5f-8c53-ca57e2a49980 | -15.17952 | -46.2188 | 2026-09-02 04:21:00 | NOAA-21 | FORMOSO | MINAS GERAIS | Brasil | 3126208 | 31 | 33 | nan | nan | nan | Cerrado | 1.2 |
| e7de8145-cd93-3510-9d77-8ad1d2a4a46a | -12.14409 | -47.12371 | 2026-09-02 04:21:00 | NOAA-21 | CONCEIÇÃO DO TOCANTINS | TOCANTINS | Brasil | 1705607 | 17 | 33 | nan | nan | nan | Cerrado | 2.1 |
| 59b1e502-07d9-30ef-8bcb-4281bde35c1d | -8.47717 | -54.71757 | 2026-09-02 04:21:00 | NOAA-21 | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 21.2 |
| b236da85-a7f7-3e51-8a88-ce731c0586df | -12.14743 | -47.12426 | 2026-09-02 04:21:00 | NOAA-21 | CONCEIÇÃO DO TOCANTINS | TOCANTINS | Brasil | 1705607 | 17 | 33 | nan | nan | nan | Cerrado | 3.0 |
| c75c1488-e0f2-31f0-ad3b-ef9123693594 | -11.67082 | -50.19769 | 2026-09-02 04:21:00 | NOAA-21 | FORMOSO DO ARAGUAIA | TOCANTINS | Brasil | 1708205 | 17 | 33 | nan | nan | nan | Cerrado | 3.6 |
| 97f6c79b-383a-31d0-a8f8-bba92dc6d114 | -8.46872 | -54.7194 | 2026-09-02 04:21:00 | NOAA-21 | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 5.1 |
| 89a3776d-19f9-36f9-a795-ad75e85c4634 | -11.30972 | -45.17476 | 2026-09-02 04:21:00 | NOAA-21 | FORMOSA DO RIO PRETO | BAHIA | Brasil | 2911105 | 29 | 33 | nan | nan | nan | Cerrado | 1.3 |
| 3e220444-733a-38f3-91ff-d66c7c4a6aec | -8.46271 | -54.72198 | 2026-09-02 04:21:00 | NOAA-21 | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 3.7 |
| f997deb5-4a7d-3407-95a6-70cd46cc669e | -12.05384 | -44.99834 | 2026-09-02 04:21:00 | NOAA-21 | BARREIRAS | BAHIA | Brasil | 2903201 | 29 | 33 | nan | nan | nan | Cerrado | 4.7 |
| a37a49e6-4da9-3462-9af6-86c11746ca9a | -12.1176 | -47.07528 | 2026-09-02 04:21:00 | NOAA-21 | TAIPAS DO TOCANTINS | TOCANTINS | Brasil | 1720937 | 17 | 33 | nan | nan | nan | Cerrado | 1.7 |
| 5c70e39f-cbcc-3a24-9cd9-038b0aa1ff8a | -15.65039 | -45.9129 | 2026-09-02 04:21:00 | NOAA-21 | ARINOS | MINAS GERAIS | Brasil | 3104502 | 31 | 33 | nan | nan | nan | Cerrado | 1.1 |
| ef24e868-4ba6-310c-bb56-a5ca53096fe9 | -11.33914 | -50.59069 | 2026-09-02 04:21:00 | NOAA-21 | LAGOA DA CONFUSÃO | TOCANTINS | Brasil | 1711902 | 17 | 33 | nan | nan | nan | Cerrado | 4.7 |
| efed8ba1-a589-387f-948d-5f955afba197 | -8.7688 | -46.44225 | 2026-09-02 04:21:00 | NOAA-21 | BALSAS | MARANHÃO | Brasil | 2101400 | 21 | 33 | nan | nan | nan | Cerrado | 1.8 |
| c22295fe-606d-3198-929f-907801c3c42d | -10.87237 | -50.46872 | 2026-09-02 04:21:00 | NOAA-21 | LAGOA DA CONFUSÃO | TOCANTINS | Brasil | 1711902 | 17 | 33 | nan | nan | nan | Cerrado | 2.2 |
| 00eaf89d-816f-320e-b7af-f1e6f4732306 | -10.96518 | -50.49002 | 2026-09-02 04:21:00 | NOAA-21 | LAGOA DA CONFUSÃO | TOCANTINS | Brasil | 1711902 | 17 | 33 | nan | nan | nan | Cerrado | 41.4 |
| 1b258c6b-ecfb-307e-93e8-65089d0bde98 | -12.05552 | -45.00977 | 2026-09-02 04:21:00 | NOAA-21 | BARREIRAS | BAHIA | Brasil | 2903201 | 29 | 33 | nan | nan | nan | Cerrado | 2.0 |
| 50bfe029-87bb-3344-8f9c-51eb19c6ebd4 | -10.78386 | -44.77212 | 2026-09-02 04:21:00 | NOAA-21 | SEBASTIÃO BARROS | PIAUÍ | Brasil | 2210623 | 22 | 33 | nan | nan | nan | Cerrado | 0.5 |
| 068e0573-9e9b-3470-82f9-d13586d7d71f | -10.90515 | -45.33082 | 2026-09-02 04:21:00 | NOAA-21 | FORMOSA DO RIO PRETO | BAHIA | Brasil | 2911105 | 29 | 33 | nan | nan | nan | Cerrado | 5.2 |
| ee6366b5-ce22-3151-9557-062dd8417e07 | -8.43832 | -54.70311 | 2026-09-02 04:21:00 | NOAA-21 | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 1.8 |
| 284326a8-c531-30c1-a8e1-64d2bc86420c | -8.4329 | -46.90187 | 2026-09-02 04:21:00 | NOAA-21 | CAMPOS LINDOS | TOCANTINS | Brasil | 1703842 | 17 | 33 | nan | nan | nan | Cerrado | 2.3 |
| dbf20afa-3aac-37b9-b409-c9f12022be75 | -13.71286 | -43.88219 | 2026-09-02 04:21:00 | NOAA-21 | SÃO FÉLIX DO CORIBE | BAHIA | Brasil | 2929057 | 29 | 33 | nan | nan | nan | Cerrado | 1.9 |
| 25f12377-10c9-3be2-b597-3797a9438c14 | -11.32615 | -50.61952 | 2026-09-02 04:21:00 | NOAA-21 | LAGOA DA CONFUSÃO | TOCANTINS | Brasil | 1711902 | 17 | 33 | nan | nan | nan | Cerrado | 1.9 |
| e5ab85a6-db03-3590-9967-5929bb86fccf | -7.93843 | -47.24508 | 2026-09-02 04:21:00 | NOAA-21 | GOIATINS | TOCANTINS | Brasil | 1709005 | 17 | 33 | nan | nan | nan | Cerrado | 0.8 |
| 6a2b79f5-dd22-3d99-8a10-423e12e1d37b | -8.45733 | -54.72096 | 2026-09-02 04:21:00 | NOAA-21 | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 3.7 |
| dbb07683-19cb-3970-a346-9b7b4af70288 | -12.87493 | -45.82544 | 2026-09-02 04:21:00 | NOAA-21 | SÃO DESIDÉRIO | BAHIA | Brasil | 2928901 | 29 | 33 | nan | nan | nan | Cerrado | 3.9 |
| 628d60cf-c311-32b8-ba94-686c61259a19 | -13.53832 | -43.3103 | 2026-09-02 04:21:00 | NOAA-21 | BOM JESUS DA LAPA | BAHIA | Brasil | 2903904 | 29 | 33 | nan | nan | nan | Caatinga | 1.5 |
| 92101c7b-f004-37be-9259-203f8495f4c9 | -11.00114 | -45.08256 | 2026-09-02 04:21:00 | NOAA-21 | FORMOSA DO RIO PRETO | BAHIA | Brasil | 2911105 | 29 | 33 | nan | nan | nan | Cerrado | 6.3 |
| 8a1a79b9-f543-3656-9246-86e840167cee | -8.47538 | -54.71321 | 2026-09-02 04:21:00 | NOAA-21 | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 5.1 |
| 594bef9f-fd75-34f6-957f-f173c7d3b8e2 | -9.22816 | -47.97419 | 2026-09-02 04:21:00 | NOAA-21 | PEDRO AFONSO | TOCANTINS | Brasil | 1716505 | 17 | 33 | nan | nan | nan | Cerrado | 1.1 |
| 14bc6602-42d3-3132-97ec-e001e4339442 | -8.45195 | -54.71996 | 2026-09-02 04:21:00 | NOAA-21 | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 2.2 |
| f8a569b5-3702-3025-b9c3-202a3d042797 | -9.70081 | -47.2077 | 2026-09-02 04:21:00 | NOAA-21 | RIO SONO | TOCANTINS | Brasil | 1718758 | 17 | 33 | nan | nan | nan | Cerrado | 1.6 |
| b5ef1beb-d2f8-3f49-99fa-c7615457cd34 | -11.35866 | -45.41027 | 2026-09-02 04:21:00 | NOAA-21 | FORMOSA DO RIO PRETO | BAHIA | Brasil | 2911105 | 29 | 33 | nan | nan | nan | Cerrado | 0.8 |
| 347ddee2-a181-342d-9349-fd6066b24e3a | -11.36529 | -45.41134 | 2026-09-02 04:21:00 | NOAA-21 | FORMOSA DO RIO PRETO | BAHIA | Brasil | 2911105 | 29 | 33 | nan | nan | nan | Cerrado | 0.9 |
| 55c460a1-e5a4-3dca-985e-eb01ce868e0f | -10.76968 | -54.04919 | 2026-09-02 04:21:00 | NOAA-21 | MARCELÂNDIA | MATO GROSSO | Brasil | 5105580 | 51 | 33 | nan | nan | nan | Amazônia | 6.1 |
| 29634434-1d31-3d29-bc4d-221a9ea15a9d | -11.19227 | -55.11334 | 2026-09-02 04:21:00 | NOAA-21 | ITAÚBA | MATO GROSSO | Brasil | 5104559 | 51 | 33 | nan | nan | nan | Amazônia | 1.6 |
| 1dae56d0-bbd6-3409-b460-d5e66a452b02 | -12.63276 | -45.07399 | 2026-09-02 04:21:00 | NOAA-21 | SÃO DESIDÉRIO | BAHIA | Brasil | 2928901 | 29 | 33 | nan | nan | nan | Cerrado | 28.8 |
| 72944c33-173b-3490-84dd-62df8d7b2a24 | -11.34852 | -45.40875 | 2026-09-02 04:21:00 | NOAA-21 | FORMOSA DO RIO PRETO | BAHIA | Brasil | 2911105 | 29 | 33 | nan | nan | nan | Cerrado | 3.7 |
| 524f5e12-af01-3be2-9df5-fba3c2585ee8 | -10.78271 | -44.75731 | 2026-09-02 04:21:00 | NOAA-21 | SEBASTIÃO BARROS | PIAUÍ | Brasil | 2210623 | 22 | 33 | nan | nan | nan | Cerrado | 6.2 |
| ffc9cb82-a9df-3aca-ab1a-0ebdc0a129a6 | -15.35071 | -47.04428 | 2026-09-02 04:21:00 | NOAA-21 | FORMOSA | GOIÁS | Brasil | 5208004 | 52 | 33 | nan | nan | nan | Cerrado | 1.3 |
| 86ed3739-d743-3446-80b0-ebb93860c55b | -10.90791 | -45.33486 | 2026-09-02 04:21:00 | NOAA-21 | FORMOSA DO RIO PRETO | BAHIA | Brasil | 2911105 | 29 | 33 | nan | nan | nan | Cerrado | 5.2 |
| d1ea79bf-acf5-3ca0-a875-18de469ca549 | -11.2251 | -43.24109 | 2026-09-02 04:21:00 | NOAA-21 | BARRA | BAHIA | Brasil | 2902708 | 29 | 33 | nan | nan | nan | Cerrado | 1.0 |
| 2ab64e3e-1eae-3d18-aa29-2bb6227ddc63 | -10.78326 | -44.75374 | 2026-09-02 04:21:00 | NOAA-21 | SEBASTIÃO BARROS | PIAUÍ | Brasil | 2210623 | 22 | 33 | nan | nan | nan | Cerrado | 6.2 |
| 05e93e3d-5d63-39d3-bdbb-32bab18a83e3 | -15.59847 | -46.45544 | 2026-09-02 04:21:00 | NOAA-21 | BURITIS | MINAS GERAIS | Brasil | 3109303 | 31 | 33 | nan | nan | nan | Cerrado | 1.4 |
| 9b39d230-fc17-3dc0-85cb-3283a8de8640 | -8.89514 | -50.56977 | 2026-09-02 04:21:00 | NOAA-21 | SANTA MARIA DAS BARREIRAS | PARÁ | Brasil | 1506583 | 15 | 33 | nan | nan | nan | Amazônia | 2.8 |
| 35a2eacc-26f2-3f85-8b1f-5ba0371e83a6 | -13.39737 | -51.37611 | 2026-09-02 04:21:00 | NOAA-21 | RIBEIRÃO CASCALHEIRA | MATO GROSSO | Brasil | 5107180 | 51 | 33 | nan | nan | nan | Cerrado | 10.5 |
| 6474d9ff-0980-33f7-94a8-8e9dca6dc988 | -11.82657 | -46.05325 | 2026-09-02 04:21:00 | NOAA-21 | BARREIRAS | BAHIA | Brasil | 2903201 | 29 | 33 | nan | nan | nan | Cerrado | 4.9 |
| 43eeba7d-ce2e-31f1-b229-4ecd94e6e34e | -12.1419 | -47.116 | 2026-09-02 04:21:00 | NOAA-21 | CONCEIÇÃO DO TOCANTINS | TOCANTINS | Brasil | 1705607 | 17 | 33 | nan | nan | nan | Cerrado | 1.9 |
| 69617df4-0eed-3785-b411-02c33560a2a0 | -11.32484 | -50.60373 | 2026-09-02 04:21:00 | NOAA-21 | LAGOA DA CONFUSÃO | TOCANTINS | Brasil | 1711902 | 17 | 33 | nan | nan | nan | Cerrado | 2.3 |
| 5842847f-72cc-3cea-953f-c2e4664ff7f7 | -8.4497 | -54.70157 | 2026-09-02 04:21:00 | NOAA-21 | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 2.3 |
| 17da6501-4ba9-3729-836a-7d877c4edc6d | -12.05829 | -45.014 | 2026-09-02 04:21:00 | NOAA-21 | BARREIRAS | BAHIA | Brasil | 2903201 | 29 | 33 | nan | nan | nan | Cerrado | 2.0 |
| 1093d83d-598f-3731-8f5a-5a3f63c829ab | -10.90075 | -45.33732 | 2026-09-02 04:21:00 | NOAA-21 | FORMOSA DO RIO PRETO | BAHIA | Brasil | 2911105 | 29 | 33 | nan | nan | nan | Cerrado | 21.6 |
| 4eb5236e-4ab9-3b4a-91ed-677ee4dd4289 | -8.11386 | -54.95678 | 2026-09-02 04:21:00 | NOAA-21 | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 7.5 |
| f012f7f0-a82f-3314-9452-0ea6dc680015 | -8.42695 | -54.70452 | 2026-09-02 04:21:00 | NOAA-21 | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 5.4 |
| 01161400-94cd-34af-bb0e-e6c2e0903289 | -15.59515 | -46.45489 | 2026-09-02 04:21:00 | NOAA-21 | BURITIS | MINAS GERAIS | Brasil | 3109303 | 31 | 33 | nan | nan | nan | Cerrado | 1.6 |
| e709cb71-874f-3e7f-8e29-d6e767286836 | -12.87439 | -45.82898 | 2026-09-02 04:21:00 | NOAA-21 | SÃO DESIDÉRIO | BAHIA | Brasil | 2928901 | 29 | 33 | nan | nan | nan | Cerrado | 3.9 |
| f2f05810-ba39-3ee5-82f0-ba7376fefb9c | -11.30145 | -45.18438 | 2026-09-02 04:21:00 | NOAA-21 | FORMOSA DO RIO PRETO | BAHIA | Brasil | 2911105 | 29 | 33 | nan | nan | nan | Cerrado | 3.0 |
| 0a720204-b093-3b09-bc0a-ef7c122d2bdf | -10.43794 | -46.72741 | 2026-09-02 04:21:00 | NOAA-21 | MATEIROS | TOCANTINS | Brasil | 1712702 | 17 | 33 | nan | nan | nan | Cerrado | 0.9 |
| 0bf38c72-2e0c-38c4-8dbb-c6cfbb6b85d2 | -8.26735 | -54.95721 | 2026-09-02 04:21:00 | NOAA-21 | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 6.7 |
| cdc22560-56f2-34cf-a615-0d091eb43e9e | -8.45384 | -54.70944 | 2026-09-02 04:21:00 | NOAA-21 | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 1.7 |
| 966dffd6-8e8a-3724-bb93-e132489fd6d1 | -8.45009 | -54.73034 | 2026-09-02 04:21:00 | NOAA-21 | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 2.2 |
| dc14bc55-a7df-3b51-809b-fe3ca5549795 | -10.44071 | -46.73151 | 2026-09-02 04:21:00 | NOAA-21 | MATEIROS | TOCANTINS | Brasil | 1712702 | 17 | 33 | nan | nan | nan | Cerrado | 1.0 |
| 2d7d635d-f2cf-3c64-a962-4aa47845c6af | -10.67543 | -46.23713 | 2026-09-02 04:21:00 | NOAA-21 | MATEIROS | TOCANTINS | Brasil | 1712702 | 17 | 33 | nan | nan | nan | Cerrado | 1.1 |
| 97272e38-e6e3-340b-aad2-ef1deeab0b29 | -12.14905 | -47.13555 | 2026-09-02 04:21:00 | NOAA-21 | CONCEIÇÃO DO TOCANTINS | TOCANTINS | Brasil | 1705607 | 17 | 33 | nan | nan | nan | Cerrado | 3.3 |
| 2a9911ac-a8be-395d-aebb-96b3c7fad79b | -8.46398 | -54.71486 | 2026-09-02 04:21:00 | NOAA-21 | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 13.1 |
| a645d70b-e9ec-3394-9e35-95f7daa95153 | -8.44657 | -54.71899 | 2026-09-02 04:21:00 | NOAA-21 | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 2.2 |
| 193892d7-6ef0-3c4c-863c-793b372e8a11 | -11.8995 | -45.07367 | 2026-09-02 04:21:00 | NOAA-21 | BARREIRAS | BAHIA | Brasil | 2903201 | 29 | 33 | nan | nan | nan | Cerrado | 0.9 |
| 77a2b786-5b59-3173-bf1f-585c8d647b24 | -10.37713 | -49.98523 | 2026-09-02 04:21:00 | NOAA-21 | PIUM | TOCANTINS | Brasil | 1717503 | 17 | 33 | nan | nan | nan | Cerrado | 1.8 |
| f9b6ea57-9a17-3021-a34c-faec92d8e9c7 | -15.8343 | -46.02049 | 2026-09-02 04:23:00 | NOAA-21 | ARINOS | MINAS GERAIS | Brasil | 3104502 | 31 | 33 | nan | nan | nan | Cerrado | 2.3 |
| 9fd30849-68bf-34b5-8b5f-6d45c5db55db | -15.65643 | -48.69834 | 2026-09-02 04:23:00 | NOAA-21 | COCALZINHO DE GOIÁS | GOIÁS | Brasil | 5205513 | 52 | 33 | nan | nan | nan | Cerrado | 3.4 |
| be39903b-ef64-3408-b46d-2da52f3ed453 | -17.18717 | -54.29893 | 2026-09-02 04:23:00 | NOAA-21 | ITIQUIRA | MATO GROSSO | Brasil | 5104609 | 51 | 33 | nan | nan | nan | Cerrado | 2.2 |
| d4e9fdae-dfb9-3c22-9c18-ed1c6b7e8905 | -16.48675 | -46.60071 | 2026-09-02 04:23:00 | NOAA-21 | UNAÍ | MINAS GERAIS | Brasil | 3170404 | 31 | 33 | nan | nan | nan | Cerrado | 1.1 |


[Clique aqui para ver as próximas entradas](README29.md)
