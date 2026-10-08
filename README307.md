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

## Dados Diários - Página 307

| ID | Latitude | Longitude | Data/Hora GMT | Satélite | Município | Estado | País | Município ID | Estado ID | País ID | Dias sem Chuva | Precipitação | Risco de Fogo | Bioma | FRP |
|----|----------|-----------|---------------|----------|-----------|--------|------|--------------|-----------|---------|----------------|--------------|----------------|-------|-----|
| 11ed858c-f413-369a-8e7b-11665921c756 | -21.86327 | -44.20619 | 2026-10-08 16:35:00 | NOAA-20 | ARANTINA | MINAS GERAIS | Brasil | 3103603 | 31 | 33 | nan | nan | nan | Mata Atlântica | 1.8 |
| eae2482d-b49b-322f-904f-93ffd5c089af | -16.2409 | -52.48463 | 2026-10-08 16:35:00 | NOAA-20 | BALIZA | GOIÁS | Brasil | 5203104 | 52 | 33 | nan | nan | nan | Cerrado | 3.2 |
| 2c3eed56-8f7f-39af-92ca-cb15813265dd | -15.82628 | -45.41337 | 2026-10-08 16:35:00 | NOAA-20 | CHAPADA GAÚCHA | MINAS GERAIS | Brasil | 3116159 | 31 | 33 | nan | nan | nan | Cerrado | 5.8 |
| 1cc27f4a-0566-3552-9148-53b6ea9c8940 | -15.69164 | -40.46743 | 2026-10-08 16:35:00 | NOAA-20 | MACARANI | BAHIA | Brasil | 2919702 | 29 | 33 | nan | nan | nan | Mata Atlântica | 18.7 |
| 2677a949-0644-3155-8c54-7d55adc47e12 | -14.60253 | -40.01957 | 2026-10-08 16:35:00 | NOAA-20 | IGUAÍ | BAHIA | Brasil | 2913507 | 29 | 33 | nan | nan | nan | Mata Atlântica | 11.0 |
| a1c21f6b-3dab-3f32-af31-87f0f5860b99 | -16.13224 | -43.74903 | 2026-10-08 16:35:00 | NOAA-20 | CAPITÃO ENÉAS | MINAS GERAIS | Brasil | 3112703 | 31 | 33 | nan | nan | nan | Cerrado | 12.1 |
| 01b90ec5-127e-3bec-ab9b-ddad332854bf | -16.76335 | -40.99258 | 2026-10-08 16:35:00 | NOAA-20 | JOAÍMA | MINAS GERAIS | Brasil | 3136009 | 31 | 33 | nan | nan | nan | Mata Atlântica | 13.6 |
| 77678efd-d3f6-3534-a1ce-718cdcc91b88 | -14.27088 | -40.39177 | 2026-10-08 16:35:00 | NOAA-20 | MIRANTE | BAHIA | Brasil | 2921450 | 29 | 33 | nan | nan | nan | Caatinga | 26.2 |
| 5ad0a8c3-ad08-31c0-a604-39eb8bdfc6af | -13.96305 | -44.85593 | 2026-10-08 16:35:00 | NOAA-20 | COCOS | BAHIA | Brasil | 2908101 | 29 | 33 | nan | nan | nan | Cerrado | 15.4 |
| f86c59b2-88fe-3642-bb6b-081f19432c63 | -20.27676 | -41.33222 | 2026-10-08 16:35:00 | NOAA-20 | MUNIZ FREIRE | ESPÍRITO SANTO | Brasil | 3203700 | 32 | 33 | nan | nan | nan | Mata Atlântica | 6.8 |
| c2038e00-db56-3d8d-ac93-9079feb98916 | -15.88406 | -40.78413 | 2026-10-08 16:35:00 | NOAA-20 | ALMENARA | MINAS GERAIS | Brasil | 3101706 | 31 | 33 | nan | nan | nan | Mata Atlântica | 24.1 |
| dc7d2b35-a5c1-3ad3-93f7-34621bc89ee1 | -16.67233 | -39.66838 | 2026-10-08 16:35:00 | NOAA-20 | ITABELA | BAHIA | Brasil | 2914653 | 29 | 33 | nan | nan | nan | Mata Atlântica | 2.7 |
| 2a8738bc-19c8-3525-b7e1-c23efe2ad4be | -14.67616 | -40.80827 | 2026-10-08 16:35:00 | NOAA-20 | VITÓRIA DA CONQUISTA | BAHIA | Brasil | 2933307 | 29 | 33 | nan | nan | nan | Mata Atlântica | 6.3 |
| 4d16ec78-38b0-3821-a3ab-8b8a322c0019 | -13.95534 | -44.84985 | 2026-10-08 16:35:00 | NOAA-20 | COCOS | BAHIA | Brasil | 2908101 | 29 | 33 | nan | nan | nan | Cerrado | 14.0 |
| 3eab3900-dce8-385e-97cb-78f46ef426b4 | -16.97992 | -41.22699 | 2026-10-08 16:35:00 | NOAA-20 | JOAÍMA | MINAS GERAIS | Brasil | 3136009 | 31 | 33 | nan | nan | nan | Mata Atlântica | 2.6 |
| 99faa918-a65f-393a-b0f3-a99b551174e0 | -17.36755 | -45.44608 | 2026-10-08 16:35:00 | NOAA-20 | BURITIZEIRO | MINAS GERAIS | Brasil | 3109402 | 31 | 33 | nan | nan | nan | Cerrado | 5.5 |
| 1442377c-8747-337d-b351-a213721a3319 | -15.40222 | -44.32491 | 2026-10-08 16:35:00 | NOAA-20 | JANUÁRIA | MINAS GERAIS | Brasil | 3135209 | 31 | 33 | nan | nan | nan | Cerrado | 11.9 |
| 9e9c267c-c831-3be9-a274-98a83b3f9b87 | -16.19793 | -44.56813 | 2026-10-08 16:35:00 | NOAA-20 | LUISLÂNDIA | MINAS GERAIS | Brasil | 3138682 | 31 | 33 | nan | nan | nan | Cerrado | 7.2 |
| c1c88267-5974-3635-98e1-24196ce36374 | -14.41611 | -41.28828 | 2026-10-08 16:35:00 | NOAA-20 | ARACATU | BAHIA | Brasil | 2902005 | 29 | 33 | nan | nan | nan | Caatinga | 3.5 |
| d8168cf9-b80d-3935-8f24-b3688ce17d6e | -16.11086 | -40.79523 | 2026-10-08 16:35:00 | NOAA-20 | ALMENARA | MINAS GERAIS | Brasil | 3101706 | 31 | 33 | nan | nan | nan | Mata Atlântica | 6.8 |
| e6b0b3cc-be1f-3250-a610-e6974dee630f | -15.33254 | -39.63491 | 2026-10-08 16:35:00 | NOAA-20 | PAU BRASIL | BAHIA | Brasil | 2923902 | 29 | 33 | nan | nan | nan | Mata Atlântica | 13.7 |
| b6f50340-6a74-317d-8f76-4f06720716c1 | -15.8803 | -42.25135 | 2026-10-08 16:35:00 | NOAA-20 | TAIOBEIRAS | MINAS GERAIS | Brasil | 3168002 | 31 | 33 | nan | nan | nan | Mata Atlântica | 7.7 |
| 6e614999-7991-3937-aebe-b13fed030a86 | -17.11282 | -41.35254 | 2026-10-08 16:35:00 | NOAA-20 | CARAÍ | MINAS GERAIS | Brasil | 3113008 | 31 | 33 | nan | nan | nan | Mata Atlântica | 7.4 |
| f37b5751-677b-300a-8b8d-c37b7048f9c4 | -19.98542 | -40.83179 | 2026-10-08 16:35:00 | NOAA-20 | ITARANA | ESPÍRITO SANTO | Brasil | 3202900 | 32 | 33 | nan | nan | nan | Mata Atlântica | 3.4 |
| 82d5c552-3c13-31e2-b551-7279723e9bc1 | -15.40276 | -44.32848 | 2026-10-08 16:35:00 | NOAA-20 | JANUÁRIA | MINAS GERAIS | Brasil | 3135209 | 31 | 33 | nan | nan | nan | Cerrado | 28.1 |
| ee799b6d-6c48-30b6-a37f-643a4808e652 | -15.68158 | -50.57572 | 2026-10-08 16:35:00 | NOAA-20 | GOIÁS | GOIÁS | Brasil | 5208905 | 52 | 33 | nan | nan | nan | Cerrado | 8.1 |
| 06a48f0b-21da-33c1-ba6d-b73b9795bc6f | -16.12838 | -43.74599 | 2026-10-08 16:35:00 | NOAA-20 | CAPITÃO ENÉAS | MINAS GERAIS | Brasil | 3112703 | 31 | 33 | nan | nan | nan | Cerrado | 12.1 |
| b80bbbcc-2fd6-3179-8355-f46ec4f8bf64 | -13.68963 | -39.9297 | 2026-10-08 16:35:00 | NOAA-20 | JEQUIÉ | BAHIA | Brasil | 2918001 | 29 | 33 | nan | nan | nan | Mata Atlântica | 7.2 |
| 093bf3f0-3106-3f9b-9659-4f90c2affeab | -23.12405 | -52.33769 | 2026-10-08 16:35:00 | NOAA-20 | ALTO PARANÁ | PARANÁ | Brasil | 4100608 | 41 | 33 | nan | nan | nan | Mata Atlântica | 20.5 |
| 394d2b7d-fc83-3b2b-af13-a76f181fc6f0 | -15.70854 | -40.59581 | 2026-10-08 16:35:00 | NOAA-20 | MACARANI | BAHIA | Brasil | 2919702 | 29 | 33 | nan | nan | nan | Mata Atlântica | 10.4 |
| b0196476-f67e-37fe-9008-a2289eeb8dc7 | -15.97598 | -40.70634 | 2026-10-08 16:35:00 | NOAA-20 | BANDEIRA | MINAS GERAIS | Brasil | 3105202 | 31 | 33 | nan | nan | nan | Mata Atlântica | 15.6 |
| c3d6acc6-b8ff-37a4-bfb4-b73bef816a77 | -14.44302 | -43.92851 | 2026-10-08 16:35:00 | NOAA-20 | JUVENÍLIA | MINAS GERAIS | Brasil | 3136959 | 31 | 33 | nan | nan | nan | Cerrado | 64.2 |
| c53b4ade-e317-3341-829f-8c2f4eac0673 | -22.5674 | -46.59594 | 2026-10-08 16:35:00 | NOAA-20 | SOCORRO | SÃO PAULO | Brasil | 3552106 | 35 | 33 | nan | nan | nan | Mata Atlântica | 4.0 |
| 73a94da7-788c-31d1-a0db-c8a9392833d1 | -15.56477 | -44.52656 | 2026-10-08 16:35:00 | NOAA-20 | JANUÁRIA | MINAS GERAIS | Brasil | 3135209 | 31 | 33 | nan | nan | nan | Cerrado | 12.0 |
| de4e938f-9675-340b-9be5-d997effa8dbe | -14.99883 | -44.05837 | 2026-10-08 16:35:00 | NOAA-20 | ITACARAMBI | MINAS GERAIS | Brasil | 3132107 | 31 | 33 | nan | nan | nan | Caatinga | 53.1 |
| 59d4c73f-f460-3fbb-a543-c5ce2011c085 | -16.20366 | -41.3739 | 2026-10-08 16:35:00 | NOAA-20 | MEDINA | MINAS GERAIS | Brasil | 3141405 | 31 | 33 | nan | nan | nan | Mata Atlântica | 3.5 |
| 2afb7489-91d8-35a1-b70f-8a6632e60e01 | -15.9587 | -41.10023 | 2026-10-08 16:35:00 | NOAA-20 | PEDRA AZUL | MINAS GERAIS | Brasil | 3148707 | 31 | 33 | nan | nan | nan | Mata Atlântica | 32.9 |
| 9b15ae51-9f7e-305f-8a0b-cb3c7f47b7d3 | -16.7894 | -43.9006 | 2026-10-08 16:35:00 | NOAA-20 | MONTES CLAROS | MINAS GERAIS | Brasil | 3143302 | 31 | 33 | nan | nan | nan | Cerrado | 3.3 |
| 6154a21a-d83c-3e72-86ae-043ae305cf7b | -15.01284 | -51.41861 | 2026-10-08 16:35:00 | NOAA-20 | JUSSARA | GOIÁS | Brasil | 5212204 | 52 | 33 | nan | nan | nan | Cerrado | 9.5 |
| 6c45fbfc-5108-38ca-8edb-d1957372bae8 | -15.10935 | -39.40247 | 2026-10-08 16:35:00 | NOAA-20 | SÃO JOSÉ DA VITÓRIA | BAHIA | Brasil | 2929354 | 29 | 33 | nan | nan | nan | Mata Atlântica | 4.1 |
| dc5bd517-b062-3c5e-b50d-cd164dc3d2f0 | -14.43935 | -40.78809 | 2026-10-08 16:35:00 | NOAA-20 | ANAGÉ | BAHIA | Brasil | 2901205 | 29 | 33 | nan | nan | nan | Caatinga | 18.8 |
| 99c7c033-1980-3e26-8af0-77dd57e1e4f9 | -14.53601 | -41.773 | 2026-10-08 16:35:00 | NOAA-20 | PRESIDENTE JÂNIO QUADROS | BAHIA | Brasil | 2925709 | 29 | 33 | nan | nan | nan | Caatinga | 7.6 |
| 9600a20b-9e8b-36fe-a741-49b17a3f87e9 | -16.75913 | -53.37981 | 2026-10-08 16:35:00 | NOAA-20 | ALTO GARÇAS | MATO GROSSO | Brasil | 5100409 | 51 | 33 | nan | nan | nan | Cerrado | 5.9 |
| a59624ab-98f9-3ccb-8cfd-bd6eeb581ade | -14.53034 | -41.67311 | 2026-10-08 16:35:00 | NOAA-20 | PRESIDENTE JÂNIO QUADROS | BAHIA | Brasil | 2925709 | 29 | 33 | nan | nan | nan | Caatinga | 59.3 |
| f9c956d5-9621-3332-b63e-ba0dd74aecd7 | -15.95803 | -41.09617 | 2026-10-08 16:35:00 | NOAA-20 | PEDRA AZUL | MINAS GERAIS | Brasil | 3148707 | 31 | 33 | nan | nan | nan | Mata Atlântica | 32.9 |
| d52dc5c8-7ff8-37a9-8f2e-ccfe44bb1c2b | -13.64411 | -40.09256 | 2026-10-08 16:35:00 | NOAA-20 | JAGUAQUARA | BAHIA | Brasil | 2917607 | 29 | 33 | nan | nan | nan | Mata Atlântica | 4.8 |
| 610eb41b-107a-396c-95cf-0473af3d5e25 | -17.40641 | -42.90121 | 2026-10-08 16:35:00 | NOAA-20 | CARBONITA | MINAS GERAIS | Brasil | 3113503 | 31 | 33 | nan | nan | nan | Cerrado | 4.3 |
| 0c1230d6-e36f-3931-b3ad-b2ec3bd23316 | -14.53098 | -41.67703 | 2026-10-08 16:35:00 | NOAA-20 | PRESIDENTE JÂNIO QUADROS | BAHIA | Brasil | 2925709 | 29 | 33 | nan | nan | nan | Caatinga | 24.3 |
| a5d65029-7203-36fb-a895-7ddb05900d1d | -15.50846 | -40.7009 | 2026-10-08 16:35:00 | NOAA-20 | RIBEIRÃO DO LARGO | BAHIA | Brasil | 2926657 | 29 | 33 | nan | nan | nan | Mata Atlântica | 1.6 |
| 1a0c7638-ad7a-3fac-b170-95b680fa13a3 | -15.00799 | -40.81736 | 2026-10-08 16:35:00 | NOAA-20 | VITÓRIA DA CONQUISTA | BAHIA | Brasil | 2933307 | 29 | 33 | nan | nan | nan | Mata Atlântica | 3.9 |
| 81e2ac57-c985-3678-bb32-3d4c6c4fb837 | -14.75964 | -41.32581 | 2026-10-08 16:35:00 | NOAA-20 | CARAÍBAS | BAHIA | Brasil | 2906899 | 29 | 33 | nan | nan | nan | Caatinga | 12.7 |
| b5a40e76-a23b-36fc-bbb7-b14101cffab6 | -16.0502 | -40.64504 | 2026-10-08 16:35:00 | NOAA-20 | ALMENARA | MINAS GERAIS | Brasil | 3101706 | 31 | 33 | nan | nan | nan | Mata Atlântica | 8.9 |
| dcb1753a-f1c7-39a9-9311-5796d609c4fe | -13.97698 | -44.83546 | 2026-10-08 16:35:00 | NOAA-20 | COCOS | BAHIA | Brasil | 2908101 | 29 | 33 | nan | nan | nan | Cerrado | 20.9 |
| dfc50d28-a359-3db9-9c2e-ab611217b27e | -21.18266 | -43.79642 | 2026-10-08 16:35:00 | NOAA-20 | BARBACENA | MINAS GERAIS | Brasil | 3105608 | 31 | 33 | nan | nan | nan | Mata Atlântica | 4.8 |
| d49f429f-023e-32b5-ac3e-376306e30be1 | -14.73273 | -41.60268 | 2026-10-08 16:35:00 | NOAA-20 | PRESIDENTE JÂNIO QUADROS | BAHIA | Brasil | 2925709 | 29 | 33 | nan | nan | nan | Caatinga | 24.3 |
| 70db977c-7087-3152-9b44-8ba91eb1bdd1 | -13.69571 | -42.69277 | 2026-10-08 16:35:00 | NOAA-20 | IGAPORÃ | BAHIA | Brasil | 2913408 | 29 | 33 | nan | nan | nan | Caatinga | 25.3 |
| 82b15012-f95b-37d2-a562-e28a845bb499 | -17.64645 | -44.28323 | 2026-10-08 16:35:00 | NOAA-20 | FRANCISCO DUMONT | MINAS GERAIS | Brasil | 3126604 | 31 | 33 | nan | nan | nan | Cerrado | 4.2 |
| fedc8283-afee-33a2-875b-1e9abe5f8000 | -14.79653 | -41.61192 | 2026-10-08 16:35:00 | NOAA-20 | PRESIDENTE JÂNIO QUADROS | BAHIA | Brasil | 2925709 | 29 | 33 | nan | nan | nan | Caatinga | 6.1 |
| 413fac61-7cb5-3f9a-96c2-27fb8f48866f | -16.05448 | -40.64866 | 2026-10-08 16:35:00 | NOAA-20 | ALMENARA | MINAS GERAIS | Brasil | 3101706 | 31 | 33 | nan | nan | nan | Mata Atlântica | 8.9 |
| 217f9455-cc4d-3594-b125-8029636b3af4 | -14.95671 | -41.79353 | 2026-10-08 16:35:00 | NOAA-20 | CORDEIROS | BAHIA | Brasil | 2909000 | 29 | 33 | nan | nan | nan | Caatinga | 5.1 |
| 41d02e76-c940-3891-9c7c-16babe4b66bc | -14.44898 | -41.20182 | 2026-10-08 16:35:00 | NOAA-20 | ARACATU | BAHIA | Brasil | 2902005 | 29 | 33 | nan | nan | nan | Caatinga | 38.7 |
| 6a111b9b-487e-387c-9689-330aa471fe3f | -14.49813 | -40.82322 | 2026-10-08 16:35:00 | NOAA-20 | ANAGÉ | BAHIA | Brasil | 2901205 | 29 | 33 | nan | nan | nan | Caatinga | 23.0 |
| 6db2c537-429c-3047-b018-8114c3ad4e2d | -14.44247 | -43.92496 | 2026-10-08 16:35:00 | NOAA-20 | JUVENÍLIA | MINAS GERAIS | Brasil | 3136959 | 31 | 33 | nan | nan | nan | Cerrado | 64.2 |
| e4699dba-33b2-3235-b3f6-c73436b40872 | -16.48943 | -39.11233 | 2026-10-08 16:35:00 | NOAA-20 | PORTO SEGURO | BAHIA | Brasil | 2925303 | 29 | 33 | nan | nan | nan | Mata Atlântica | 10.0 |
| 99ef21b3-fab5-37b5-907a-d7900f8f476c | -14.35709 | -40.47434 | 2026-10-08 16:35:00 | NOAA-20 | BOM JESUS DA SERRA | BAHIA | Brasil | 2903953 | 29 | 33 | nan | nan | nan | Caatinga | 2.3 |
| de6a3c58-b2ac-3747-be0c-ed44f142f077 | -15.78971 | -40.69624 | 2026-10-08 16:35:00 | NOAA-20 | MATA VERDE | MINAS GERAIS | Brasil | 3140555 | 31 | 33 | nan | nan | nan | Mata Atlântica | 2.9 |
| da8cc557-d44f-3a1e-acbe-41b4ed1597fc | -14.50517 | -40.37761 | 2026-10-08 16:35:00 | NOAA-20 | POÇÕES | BAHIA | Brasil | 2925105 | 29 | 33 | nan | nan | nan | Mata Atlântica | 14.3 |
| d814ec47-ef7c-3a76-b845-9d04e0c91631 | -16.11444 | -40.79482 | 2026-10-08 16:35:00 | NOAA-20 | ALMENARA | MINAS GERAIS | Brasil | 3101706 | 31 | 33 | nan | nan | nan | Mata Atlântica | 6.8 |
| 9b711c31-814e-375f-a1b3-1da42e2952de | -15.79089 | -44.67909 | 2026-10-08 16:35:00 | NOAA-20 | SÃO FRANCISCO | MINAS GERAIS | Brasil | 3161106 | 31 | 33 | nan | nan | nan | Cerrado | 193.5 |
| 06a99ad7-3eb0-3249-a67e-bf9fc0f851d3 | -16.19847 | -44.57177 | 2026-10-08 16:35:00 | NOAA-20 | LUISLÂNDIA | MINAS GERAIS | Brasil | 3138682 | 31 | 33 | nan | nan | nan | Cerrado | 7.2 |
| acc144ad-399c-32fb-a6e6-8f3750cea73d | -14.52969 | -41.66918 | 2026-10-08 16:35:00 | NOAA-20 | PRESIDENTE JÂNIO QUADROS | BAHIA | Brasil | 2925709 | 29 | 33 | nan | nan | nan | Caatinga | 59.3 |
| e13f6d98-ae2e-3876-9453-ed941d531ca1 | -15.38096 | -40.76599 | 2026-10-08 16:35:00 | NOAA-20 | RIBEIRÃO DO LARGO | BAHIA | Brasil | 2926657 | 29 | 33 | nan | nan | nan | Mata Atlântica | 4.8 |
| d8abb45f-9bcf-3c8e-9e65-213e0da167dc | -14.98633 | -41.1628 | 2026-10-08 16:35:00 | NOAA-20 | BELO CAMPO | BAHIA | Brasil | 2903508 | 29 | 33 | nan | nan | nan | Mata Atlântica | 9.2 |
| b725b39d-b01b-3573-90cb-bbd6f017e030 | -16.93289 | -42.11036 | 2026-10-08 16:35:00 | NOAA-20 | ARAÇUAÍ | MINAS GERAIS | Brasil | 3103405 | 31 | 33 | nan | nan | nan | Mata Atlântica | 7.2 |
| 5e4146d6-6e47-32e3-8715-bbe07f6be593 | -16.15017 | -43.11705 | 2026-10-08 16:35:00 | NOAA-20 | RIACHO DOS MACHADOS | MINAS GERAIS | Brasil | 3154507 | 31 | 33 | nan | nan | nan | Cerrado | 6.6 |
| 7c0d449d-9618-366f-b59d-47805c53eea1 | -15.93218 | -38.94794 | 2026-10-08 16:35:00 | NOAA-20 | BELMONTE | BAHIA | Brasil | 2903409 | 29 | 33 | nan | nan | nan | Mata Atlântica | 6.6 |
| 10965a1c-894a-3f91-9f33-bd3caae7a3c4 | -16.05377 | -40.64441 | 2026-10-08 16:35:00 | NOAA-20 | ALMENARA | MINAS GERAIS | Brasil | 3101706 | 31 | 33 | nan | nan | nan | Mata Atlântica | 8.9 |
| 4a9465d1-f5c3-3c7e-b61f-27a138bead66 | -16.13046 | -48.94268 | 2026-10-08 16:35:00 | NOAA-20 | PIRENÓPOLIS | GOIÁS | Brasil | 5217302 | 52 | 33 | nan | nan | nan | Cerrado | 2.2 |
| b4682470-8c40-36e0-8847-53e6b1d9664d | -14.44909 | -43.92389 | 2026-10-08 16:35:00 | NOAA-20 | JUVENÍLIA | MINAS GERAIS | Brasil | 3136959 | 31 | 33 | nan | nan | nan | Cerrado | 20.4 |
| 7b24a063-a34f-38ab-95f5-9fe91fec423d | -23.16305 | -47.02871 | 2026-10-08 16:35:00 | NOAA-20 | ITUPEVA | SÃO PAULO | Brasil | 3524006 | 35 | 33 | nan | nan | nan | Mata Atlântica | 8.5 |
| 22352c03-c799-30b5-9f9c-13c26ee46a06 | -15.60392 | -40.50347 | 2026-10-08 16:35:00 | NOAA-20 | RIBEIRÃO DO LARGO | BAHIA | Brasil | 2926657 | 29 | 33 | nan | nan | nan | Mata Atlântica | 10.5 |
| 533d1560-627d-30c3-9c1c-caeb15a36e06 | -16.9398 | -42.07871 | 2026-10-08 16:35:00 | NOAA-20 | ARAÇUAÍ | MINAS GERAIS | Brasil | 3103405 | 31 | 33 | nan | nan | nan | Mata Atlântica | 11.0 |
| 9fdc7e2e-e3e3-3be4-88b1-84b1300dbd32 | -15.50031 | -48.42049 | 2026-10-08 16:35:00 | NOAA-20 | PADRE BERNARDO | GOIÁS | Brasil | 5215603 | 52 | 33 | nan | nan | nan | Cerrado | 3.6 |
| a591480d-b537-3d9a-963c-71171140c398 | -19.60066 | -40.10367 | 2026-10-08 16:35:00 | NOAA-20 | ARACRUZ | ESPÍRITO SANTO | Brasil | 3200607 | 32 | 33 | nan | nan | nan | Mata Atlântica | 4.9 |
| 771b5351-13df-3429-9a92-a77647d4fe05 | -22.08312 | -46.63393 | 2026-10-08 16:35:00 | NOAA-20 | ANDRADAS | MINAS GERAIS | Brasil | 3102605 | 31 | 33 | nan | nan | nan | Mata Atlântica | 2.6 |
| 8f634d16-f3db-34ed-853e-4933deb1590e | -13.97365 | -44.83598 | 2026-10-08 16:35:00 | NOAA-20 | COCOS | BAHIA | Brasil | 2908101 | 29 | 33 | nan | nan | nan | Cerrado | 20.9 |
| a6f647f7-0eed-38d8-9fba-a2ef245636e3 | -15.3421 | -50.57706 | 2026-10-08 16:35:00 | NOAA-20 | FAINA | GOIÁS | Brasil | 5207535 | 52 | 33 | nan | nan | nan | Cerrado | 8.7 |
| 8906e55e-a0f0-3e7e-92e7-40378dc3d876 | -14.05788 | -43.82917 | 2026-10-08 16:35:00 | NOAA-20 | CARINHANHA | BAHIA | Brasil | 2907103 | 29 | 33 | nan | nan | nan | Cerrado | 278.1 |
| d3041841-232b-3a95-af3d-82127ab1b15f | -15.95386 | -41.09277 | 2026-10-08 16:35:00 | NOAA-20 | PEDRA AZUL | MINAS GERAIS | Brasil | 3148707 | 31 | 33 | nan | nan | nan | Mata Atlântica | 15.2 |
| 40e1996e-2ec1-3ed2-89c6-8bc93b6d8ff1 | -16.99289 | -42.30208 | 2026-10-08 16:35:00 | NOAA-20 | FRANCISCO BADARÓ | MINAS GERAIS | Brasil | 3126505 | 31 | 33 | nan | nan | nan | Cerrado | 3.6 |
| 9322e125-02da-30f4-a732-5fc1b3291847 | -20.95481 | -44.7722 | 2026-10-08 16:35:00 | NOAA-20 | BOM SUCESSO | MINAS GERAIS | Brasil | 3108008 | 31 | 33 | nan | nan | nan | Mata Atlântica | 6.5 |
| 120bb94e-25d6-3684-9a74-cb439b0332a4 | -16.31948 | -44.56373 | 2026-10-08 16:35:00 | NOAA-20 | BRASÍLIA DE MINAS | MINAS GERAIS | Brasil | 3108602 | 31 | 33 | nan | nan | nan | Cerrado | 47.4 |
| a1e29da1-4504-3507-8ea9-cd5d261bfbab | -15.56531 | -44.53016 | 2026-10-08 16:35:00 | NOAA-20 | JANUÁRIA | MINAS GERAIS | Brasil | 3135209 | 31 | 33 | nan | nan | nan | Cerrado | 14.1 |
| 6be0e584-7b6a-39b8-8d76-97d977359667 | -14.44855 | -43.92033 | 2026-10-08 16:35:00 | NOAA-20 | JUVENÍLIA | MINAS GERAIS | Brasil | 3136959 | 31 | 33 | nan | nan | nan | Cerrado | 6.7 |
| ea49725a-2d34-3972-8cd4-840f23dd61ac | -14.05402 | -43.82615 | 2026-10-08 16:35:00 | NOAA-20 | CARINHANHA | BAHIA | Brasil | 2907103 | 29 | 33 | nan | nan | nan | Cerrado | 120.6 |
| c1aa1b4d-2455-39f5-a4c1-a76589770880 | -15.56423 | -44.52295 | 2026-10-08 16:35:00 | NOAA-20 | JANUÁRIA | MINAS GERAIS | Brasil | 3135209 | 31 | 33 | nan | nan | nan | Cerrado | 12.0 |
| ad0c865b-b20d-3e55-aae0-dd4ad12917b3 | -15.39721 | -44.33672 | 2026-10-08 16:35:00 | NOAA-20 | JANUÁRIA | MINAS GERAIS | Brasil | 3135209 | 31 | 33 | nan | nan | nan | Cerrado | 11.2 |
| 7a21dccb-0ef1-3db5-b8ba-8831cc88dc5e | -19.60418 | -40.10302 | 2026-10-08 16:35:00 | NOAA-20 | ARACRUZ | ESPÍRITO SANTO | Brasil | 3200607 | 32 | 33 | nan | nan | nan | Mata Atlântica | 4.9 |
| 045dfb8f-3e73-3c88-80c6-d78ad82cf7ef | -23.19634 | -51.55774 | 2026-10-08 16:35:00 | NOAA-20 | PITANGUEIRAS | PARANÁ | Brasil | 4119657 | 41 | 33 | nan | nan | nan | Mata Atlântica | 2.6 |
| 38b59845-1022-3ba6-b4b2-bb4fc8208bf7 | -15.95454 | -41.09686 | 2026-10-08 16:35:00 | NOAA-20 | PEDRA AZUL | MINAS GERAIS | Brasil | 3148707 | 31 | 33 | nan | nan | nan | Mata Atlântica | 7.2 |


[Clique aqui para ver as próximas entradas](README308.md)
