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

## Dados Diários - Página 96

| ID | Latitude | Longitude | Data/Hora GMT | Satélite | Município | Estado | País | Município ID | Estado ID | País ID | Dias sem Chuva | Precipitação | Risco de Fogo | Bioma | FRP |
|----|----------|-----------|---------------|----------|-----------|--------|------|--------------|-----------|---------|----------------|--------------|----------------|-------|-----|
| 9e6c1081-3221-331e-9941-8754c973affc | -12.87621 | -44.62453 | 2024-10-05 04:38:00 | NOAA-20 | SÃO DESIDÉRIO | BAHIA | Brasil | 2928901 | 29 | 33 | nan | nan | nan | Cerrado | 2.5 |
| d3645529-8656-3977-a943-120aca081152 | -12.86374 | -44.61848 | 2024-10-05 04:38:00 | NOAA-20 | SÃO DESIDÉRIO | BAHIA | Brasil | 2928901 | 29 | 33 | nan | nan | nan | Cerrado | 6.1 |
| dfd58ab2-2d00-341b-ab9d-3de017704cc8 | -12.82354 | -44.60983 | 2024-10-05 04:38:00 | NOAA-20 | SÃO DESIDÉRIO | BAHIA | Brasil | 2928901 | 29 | 33 | nan | nan | nan | Cerrado | 0.7 |
| 84b4092a-d1bd-333e-b0bf-32f448be275d | -12.73027 | -43.4795 | 2024-10-05 04:38:00 | NOAA-20 | SÍTIO DO MATO | BAHIA | Brasil | 2930758 | 29 | 33 | nan | nan | nan | Cerrado | 1.5 |
| 5cf3f35c-9c96-32b9-a5d8-2c2f5f2174c6 | -12.347 | -44.62632 | 2024-10-05 04:38:00 | NOAA-20 | BAIANÓPOLIS | BAHIA | Brasil | 2902500 | 29 | 33 | nan | nan | nan | Cerrado | 2.2 |
| df1fd542-8257-30e0-a029-b7765e787e3a | -14.04254 | -45.17968 | 2024-10-05 04:38:00 | NOAA-20 | JABORANDI | BAHIA | Brasil | 2917359 | 29 | 33 | nan | nan | nan | Cerrado | 1.2 |
| 323f2fe0-d8b1-3382-91a0-76fa890c9396 | -14.042 | -45.18377 | 2024-10-05 04:38:00 | NOAA-20 | JABORANDI | BAHIA | Brasil | 2917359 | 29 | 33 | nan | nan | nan | Cerrado | 1.2 |
| 1aced6cc-fde8-3db0-9400-88f4f2995ee2 | -13.9931 | -44.03151 | 2024-10-05 04:38:00 | NOAA-20 | CARINHANHA | BAHIA | Brasil | 2907103 | 29 | 33 | nan | nan | nan | Cerrado | 1.4 |
| 4083ea6b-c22b-3ccd-b633-cba01e2276e6 | -13.99284 | -44.0337 | 2024-10-05 04:38:00 | NOAA-20 | CARINHANHA | BAHIA | Brasil | 2907103 | 29 | 33 | nan | nan | nan | Cerrado | 2.6 |
| 38c6661a-066c-3026-ac25-7d7863faa1f0 | -13.9925 | -44.03635 | 2024-10-05 04:38:00 | NOAA-20 | CARINHANHA | BAHIA | Brasil | 2907103 | 29 | 33 | nan | nan | nan | Cerrado | 1.4 |
| 693e9177-5293-38b8-8f0e-6a08ebfc7df7 | -8.773 | -44.8167 | 2024-10-05 04:38:00 | NOAA-20 | CURRAIS | PIAUÍ | Brasil | 2203230 | 22 | 33 | nan | nan | nan | Cerrado | 7.9 |
| 0bd9bb87-90a5-39dd-b3b8-2dbb457f095c | -6.50153 | -44.1517 | 2024-10-05 04:38:00 | NOAA-20 | PASTOS BONS | MARANHÃO | Brasil | 2108009 | 21 | 33 | nan | nan | nan | Cerrado | 1.3 |
| ed00953e-ed89-387a-8b30-12b0961e5f97 | -6.42818 | -44.48475 | 2024-10-05 04:38:00 | NOAA-20 | MIRADOR | MARANHÃO | Brasil | 2106706 | 21 | 33 | nan | nan | nan | Cerrado | 2.3 |
| 8dcb5ade-3bb0-332a-a3a8-4261b11b58da | -6.42768 | -44.70881 | 2024-10-05 04:38:00 | NOAA-20 | MIRADOR | MARANHÃO | Brasil | 2106706 | 21 | 33 | nan | nan | nan | Cerrado | 2.4 |
| 0cf91f0b-4448-3b7f-9b27-d76f6aec39df | -7.18173 | -45.05169 | 2024-10-05 04:38:00 | NOAA-20 | LORETO | MARANHÃO | Brasil | 2106102 | 21 | 33 | nan | nan | nan | Cerrado | 1.6 |
| 0f852079-e83c-325f-96d0-e3004572642a | -7.17784 | -45.05111 | 2024-10-05 04:38:00 | NOAA-20 | LORETO | MARANHÃO | Brasil | 2106102 | 21 | 33 | nan | nan | nan | Cerrado | 1.6 |
| 647fa381-c853-3b3e-8333-8d28613443f2 | -7.50264 | -44.83416 | 2024-10-05 04:38:00 | NOAA-20 | URUÇUÍ | PIAUÍ | Brasil | 2211209 | 22 | 33 | nan | nan | nan | Cerrado | 4.5 |
| df04785e-a00e-34f2-8bc4-80d766ff225a | -7.47105 | -43.98918 | 2024-10-05 04:38:00 | NOAA-20 | SEBASTIÃO LEAL | PIAUÍ | Brasil | 2210631 | 22 | 33 | nan | nan | nan | Cerrado | 1.3 |
| 786d85ab-2004-36d5-8e85-482a60ca9f88 | -7.43912 | -43.99654 | 2024-10-05 04:38:00 | NOAA-20 | SEBASTIÃO LEAL | PIAUÍ | Brasil | 2210631 | 22 | 33 | nan | nan | nan | Cerrado | 1.0 |
| 24bb7cac-fe2e-35d7-920b-e64cd26c0552 | -7.50588 | -44.83971 | 2024-10-05 04:38:00 | NOAA-20 | URUÇUÍ | PIAUÍ | Brasil | 2211209 | 22 | 33 | nan | nan | nan | Cerrado | 4.5 |
| 52c5c761-5391-3220-af94-68a78146f453 | -6.68301 | -43.99517 | 2024-10-05 04:38:00 | NOAA-20 | NOVA IORQUE | MARANHÃO | Brasil | 2107308 | 21 | 33 | nan | nan | nan | Cerrado | 1.8 |
| 7d4f52e3-156a-3ef9-bbea-bf392da0565b | -7.17916 | -45.04793 | 2024-10-05 04:38:00 | NOAA-20 | LORETO | MARANHÃO | Brasil | 2106102 | 21 | 33 | nan | nan | nan | Cerrado | 3.5 |
| 530d5021-48be-362b-b99e-71ca08b9a06f | -7.163 | -45.04391 | 2024-10-05 04:38:00 | NOAA-20 | LORETO | MARANHÃO | Brasil | 2106102 | 21 | 33 | nan | nan | nan | Cerrado | 4.2 |
| 0e991d92-4571-3210-8141-10c973e1c625 | -7.09541 | -44.43879 | 2024-10-05 04:38:00 | NOAA-20 | BENEDITO LEITE | MARANHÃO | Brasil | 2101806 | 21 | 33 | nan | nan | nan | Cerrado | 1.6 |
| e433c308-fd8d-3f0b-a315-174de2101d85 | -7.09488 | -44.44239 | 2024-10-05 04:38:00 | NOAA-20 | BENEDITO LEITE | MARANHÃO | Brasil | 2101806 | 21 | 33 | nan | nan | nan | Cerrado | 1.6 |
| 77b8e4d4-08ff-39a2-a19b-46023a63996a | -7.08696 | -44.41141 | 2024-10-05 04:38:00 | NOAA-20 | BENEDITO LEITE | MARANHÃO | Brasil | 2101806 | 21 | 33 | nan | nan | nan | Cerrado | 0.7 |
| 716ebc77-39f0-3b32-a93f-2dd861647d77 | -7.05906 | -44.40402 | 2024-10-05 04:38:00 | NOAA-20 | BENEDITO LEITE | MARANHÃO | Brasil | 2101806 | 21 | 33 | nan | nan | nan | Cerrado | 1.7 |
| 16d054a0-05da-3b6e-9e3a-b6cf2b8906bf | -7.0139 | -44.39775 | 2024-10-05 04:38:00 | NOAA-20 | BENEDITO LEITE | MARANHÃO | Brasil | 2101806 | 21 | 33 | nan | nan | nan | Cerrado | 2.7 |
| 3b4d4279-8e92-3bee-bb1a-d1ee9b066334 | -6.71062 | -44.53381 | 2024-10-05 04:38:00 | NOAA-20 | SUCUPIRA DO NORTE | MARANHÃO | Brasil | 2111904 | 21 | 33 | nan | nan | nan | Cerrado | 2.9 |
| 6673a12c-22e6-33f8-aee4-8ae5decec3c0 | -6.68158 | -44.83293 | 2024-10-05 04:38:00 | NOAA-20 | MIRADOR | MARANHÃO | Brasil | 2106706 | 21 | 33 | nan | nan | nan | Cerrado | 1.8 |
| b9d9fe28-762c-3880-bb27-794083d4c01c | -6.68109 | -44.83678 | 2024-10-05 04:38:00 | NOAA-20 | MIRADOR | MARANHÃO | Brasil | 2106706 | 21 | 33 | nan | nan | nan | Cerrado | 2.7 |
| d844016d-d144-3d84-996e-5f90126d1f81 | -6.68085 | -44.83794 | 2024-10-05 04:38:00 | NOAA-20 | MIRADOR | MARANHÃO | Brasil | 2106706 | 21 | 33 | nan | nan | nan | Cerrado | 2.1 |
| 3ebd12b5-37d2-3fbc-a05f-ae83ab88640b | -6.66118 | -44.05679 | 2024-10-05 04:38:00 | NOAA-20 | PASTOS BONS | MARANHÃO | Brasil | 2108009 | 21 | 33 | nan | nan | nan | Cerrado | 2.4 |
| 88c67ad7-007e-3b6e-ab46-170b21471053 | -6.5815 | -44.64548 | 2024-10-05 04:38:00 | NOAA-20 | MIRADOR | MARANHÃO | Brasil | 2106706 | 21 | 33 | nan | nan | nan | Cerrado | 2.0 |
| 0d70623b-d61b-3118-ab36-cdb536f80410 | -6.5801 | -44.18132 | 2024-10-05 04:38:00 | NOAA-20 | PASTOS BONS | MARANHÃO | Brasil | 2108009 | 21 | 33 | nan | nan | nan | Cerrado | 1.7 |
| bf57e321-5839-372d-bf1d-a19f4a0bae6d | -6.57652 | -44.17725 | 2024-10-05 04:38:00 | NOAA-20 | PASTOS BONS | MARANHÃO | Brasil | 2108009 | 21 | 33 | nan | nan | nan | Cerrado | 2.7 |
| 3c76ed25-d2c5-3a27-b136-1592f7bddda7 | -6.51688 | -44.50493 | 2024-10-05 04:38:00 | NOAA-20 | MIRADOR | MARANHÃO | Brasil | 2106706 | 21 | 33 | nan | nan | nan | Cerrado | 1.4 |
| e16b581b-cadd-3896-98cd-f652c65ca050 | -7.54509 | -45.1441 | 2024-10-05 04:38:00 | NOAA-20 | RIBEIRO GONÇALVES | PIAUÍ | Brasil | 2208908 | 22 | 33 | nan | nan | nan | Cerrado | 2.5 |
| 3c5d6737-0cae-3371-be14-eb7422845da3 | -7.52253 | -44.97167 | 2024-10-05 04:38:00 | NOAA-20 | URUÇUÍ | PIAUÍ | Brasil | 2211209 | 22 | 33 | nan | nan | nan | Cerrado | 3.9 |
| 51b29063-fddd-3179-9894-eb7476aa8998 | -7.49475 | -44.83275 | 2024-10-05 04:38:00 | NOAA-20 | URUÇUÍ | PIAUÍ | Brasil | 2211209 | 22 | 33 | nan | nan | nan | Cerrado | 3.6 |
| 4009d671-e422-3ca1-9849-dd003bd0d3d6 | -7.43965 | -43.99973 | 2024-10-05 04:38:00 | NOAA-20 | SEBASTIÃO LEAL | PIAUÍ | Brasil | 2210631 | 22 | 33 | nan | nan | nan | Cerrado | 1.4 |
| bbf63252-9038-37b7-bea7-089ab80e934e | -7.52256 | -44.96855 | 2024-10-05 04:38:00 | NOAA-20 | URUÇUÍ | PIAUÍ | Brasil | 2211209 | 22 | 33 | nan | nan | nan | Cerrado | 5.2 |
| 6d1edfa3-1a7d-3902-86be-ac445e4c9dbd | -7.4987 | -44.83345 | 2024-10-05 04:38:00 | NOAA-20 | URUÇUÍ | PIAUÍ | Brasil | 2211209 | 22 | 33 | nan | nan | nan | Cerrado | 3.6 |
| 4a5dce36-045f-3e6b-98b1-d749eeaba65a | -7.43855 | -44.00039 | 2024-10-05 04:38:00 | NOAA-20 | SEBASTIÃO LEAL | PIAUÍ | Brasil | 2210631 | 22 | 33 | nan | nan | nan | Cerrado | 1.0 |
| 405a2ce1-fdd9-3928-b33e-2307862a5002 | -7.22676 | -44.93927 | 2024-10-05 04:38:00 | NOAA-20 | SÃO FÉLIX DE BALSAS | MARANHÃO | Brasil | 2110807 | 21 | 33 | nan | nan | nan | Cerrado | 3.7 |
| 53800e6e-d450-38c3-8cce-1d5e89883f3e | -7.09103 | -44.4119 | 2024-10-05 04:38:00 | NOAA-20 | BENEDITO LEITE | MARANHÃO | Brasil | 2101806 | 21 | 33 | nan | nan | nan | Cerrado | 0.6 |
| cbd9f820-6bb6-3cc4-a11b-5a678e3dc2fc | -7.05853 | -44.4038 | 2024-10-05 04:38:00 | NOAA-20 | BENEDITO LEITE | MARANHÃO | Brasil | 2101806 | 21 | 33 | nan | nan | nan | Cerrado | 2.8 |
| 8f8870c5-14c5-3e4e-b4c1-700cf3a16b50 | -7.01793 | -44.3985 | 2024-10-05 04:38:00 | NOAA-20 | BENEDITO LEITE | MARANHÃO | Brasil | 2101806 | 21 | 33 | nan | nan | nan | Cerrado | 1.2 |
| e6bdca1d-d4cf-386f-85ac-774f428b6a8a | -7.01338 | -44.40136 | 2024-10-05 04:38:00 | NOAA-20 | BENEDITO LEITE | MARANHÃO | Brasil | 2101806 | 21 | 33 | nan | nan | nan | Cerrado | 2.7 |
| 9cce230c-f188-3afb-8ac9-a2db71e72bbe | -6.67223 | -44.51727 | 2024-10-05 04:38:00 | NOAA-20 | SUCUPIRA DO NORTE | MARANHÃO | Brasil | 2111904 | 21 | 33 | nan | nan | nan | Cerrado | 2.1 |
| 1808f803-39ef-30b9-99a0-047dbcf046c9 | -6.66825 | -44.51657 | 2024-10-05 04:38:00 | NOAA-20 | SUCUPIRA DO NORTE | MARANHÃO | Brasil | 2111904 | 21 | 33 | nan | nan | nan | Cerrado | 2.1 |
| 2c1f0f4d-e123-399e-8fe1-ca361c22b67f | -6.66775 | -44.51996 | 2024-10-05 04:38:00 | NOAA-20 | SUCUPIRA DO NORTE | MARANHÃO | Brasil | 2111904 | 21 | 33 | nan | nan | nan | Cerrado | 1.9 |
| a9abafa0-bc32-3d41-b5df-1049f9bbb4a0 | -6.66029 | -44.51514 | 2024-10-05 04:38:00 | NOAA-20 | SUCUPIRA DO NORTE | MARANHÃO | Brasil | 2111904 | 21 | 33 | nan | nan | nan | Cerrado | 1.9 |
| 21f7a1a3-48d1-3a8b-8d24-6accc5d715c9 | -6.65978 | -44.5186 | 2024-10-05 04:38:00 | NOAA-20 | SUCUPIRA DO NORTE | MARANHÃO | Brasil | 2111904 | 21 | 33 | nan | nan | nan | Cerrado | 1.9 |
| e1ae3efe-cbe9-3276-9d21-9fa132a21d42 | -6.57223 | -44.2357 | 2024-10-05 04:38:00 | NOAA-20 | PASTOS BONS | MARANHÃO | Brasil | 2108009 | 21 | 33 | nan | nan | nan | Cerrado | 2.2 |
| 13e3fb08-668a-33a6-840e-8cf216d5d66f | -6.56817 | -44.23507 | 2024-10-05 04:38:00 | NOAA-20 | PASTOS BONS | MARANHÃO | Brasil | 2108009 | 21 | 33 | nan | nan | nan | Cerrado | 2.2 |
| 0dd6e95e-bc44-3539-87a6-a967894c246b | -6.56549 | -44.6171 | 2024-10-05 04:38:00 | NOAA-20 | MIRADOR | MARANHÃO | Brasil | 2106706 | 21 | 33 | nan | nan | nan | Cerrado | 0.8 |
| 1c545bd9-9abf-3cc4-bb78-ad815d6735bb | -8.77603 | -44.82433 | 2024-10-05 04:38:00 | NOAA-20 | CURRAIS | PIAUÍ | Brasil | 2203230 | 22 | 33 | nan | nan | nan | Cerrado | 3.5 |
| 19d26b79-ea33-38e6-ad12-d6a5a834cc66 | -8.77553 | -44.82785 | 2024-10-05 04:38:00 | NOAA-20 | CURRAIS | PIAUÍ | Brasil | 2203230 | 22 | 33 | nan | nan | nan | Cerrado | 2.9 |
| 69ebefbb-b81d-3803-bf00-8b97574f352b | -8.76896 | -44.81612 | 2024-10-05 04:38:00 | NOAA-20 | CURRAIS | PIAUÍ | Brasil | 2203230 | 22 | 33 | nan | nan | nan | Cerrado | 7.9 |
| 43e0763e-7bdb-3fc6-9c84-b243c09d023e | -8.76795 | -44.82318 | 2024-10-05 04:38:00 | NOAA-20 | CURRAIS | PIAUÍ | Brasil | 2203230 | 22 | 33 | nan | nan | nan | Cerrado | 5.8 |
| 8a09396f-64b7-3bdd-91aa-374203333672 | -8.76391 | -44.82259 | 2024-10-05 04:38:00 | NOAA-20 | CURRAIS | PIAUÍ | Brasil | 2203230 | 22 | 33 | nan | nan | nan | Cerrado | 11.5 |
| 1c03cdf1-2523-36fa-8f49-757c854e4d00 | -8.76341 | -44.8261 | 2024-10-05 04:38:00 | NOAA-20 | CURRAIS | PIAUÍ | Brasil | 2203230 | 22 | 33 | nan | nan | nan | Cerrado | 10.7 |
| b6ac3851-6a1b-3191-9339-1251e7a73ec5 | -8.75937 | -44.82553 | 2024-10-05 04:38:00 | NOAA-20 | CURRAIS | PIAUÍ | Brasil | 2203230 | 22 | 33 | nan | nan | nan | Cerrado | 10.7 |
| 3de979f0-7ee7-31c9-a787-f010f33d087e | -8.77704 | -44.81727 | 2024-10-05 04:38:00 | NOAA-20 | CURRAIS | PIAUÍ | Brasil | 2203230 | 22 | 33 | nan | nan | nan | Cerrado | 3.3 |
| 1ac9a37c-88df-3b38-b5ad-3ddecd8d6074 | -8.76946 | -44.81257 | 2024-10-05 04:38:00 | NOAA-20 | CURRAIS | PIAUÍ | Brasil | 2203230 | 22 | 33 | nan | nan | nan | Cerrado | 7.9 |
| 3619e9a0-5c1b-322e-8218-916f8f5987d7 | -8.76845 | -44.81965 | 2024-10-05 04:38:00 | NOAA-20 | CURRAIS | PIAUÍ | Brasil | 2203230 | 22 | 33 | nan | nan | nan | Cerrado | 5.8 |
| 18f3630f-c0a9-3627-b163-296a98703a44 | -8.76745 | -44.82671 | 2024-10-05 04:38:00 | NOAA-20 | CURRAIS | PIAUÍ | Brasil | 2203230 | 22 | 33 | nan | nan | nan | Cerrado | 33.4 |
| 9e7861b7-178f-327f-8a3b-8c4d0aa0f73b | -8.76695 | -44.83021 | 2024-10-05 04:38:00 | NOAA-20 | CURRAIS | PIAUÍ | Brasil | 2203230 | 22 | 33 | nan | nan | nan | Cerrado | 33.4 |
| 00bb6ee5-2a3b-3d86-89cd-61a5a6a7a1aa | -8.15409 | -44.40929 | 2024-10-05 04:38:00 | NOAA-20 | URUÇUÍ | PIAUÍ | Brasil | 2211209 | 22 | 33 | nan | nan | nan | Cerrado | 1.3 |
| dab66ae6-b9a7-3e22-af31-897cf833b27a | -8.77249 | -44.82023 | 2024-10-05 04:38:00 | NOAA-20 | CURRAIS | PIAUÍ | Brasil | 2203230 | 22 | 33 | nan | nan | nan | Cerrado | 5.8 |
| 21680062-5c74-3601-80d0-bd2d8ea96945 | -8.77148 | -44.8273 | 2024-10-05 04:38:00 | NOAA-20 | CURRAIS | PIAUÍ | Brasil | 2203230 | 22 | 33 | nan | nan | nan | Cerrado | 33.4 |
| 12e2aa8c-6495-3b95-ade6-f28b7a9279fc | -8.75987 | -44.822 | 2024-10-05 04:38:00 | NOAA-20 | CURRAIS | PIAUÍ | Brasil | 2203230 | 22 | 33 | nan | nan | nan | Cerrado | 11.5 |
| c4934589-1847-3b3f-bad5-2c100e3c40b2 | -8.56999 | -44.08709 | 2024-10-05 04:38:00 | NOAA-20 | ALVORADA DO GURGUÉIA | PIAUÍ | Brasil | 2200459 | 22 | 33 | nan | nan | nan | Cerrado | 2.8 |
| a5b26d6c-784d-3baa-bd09-0279afeaa5e5 | -8.15821 | -44.40986 | 2024-10-05 04:38:00 | NOAA-20 | URUÇUÍ | PIAUÍ | Brasil | 2211209 | 22 | 33 | nan | nan | nan | Cerrado | 1.3 |
| 535aacc6-dce7-3d73-a1c1-4c0766ced5d8 | -8.99396 | -45.20501 | 2024-10-05 04:38:00 | NOAA-20 | BAIXA GRANDE DO RIBEIRO | PIAUÍ | Brasil | 2201150 | 22 | 33 | nan | nan | nan | Cerrado | 3.4 |
| 46560d96-3939-3b47-a21e-5490f78a9038 | -8.77199 | -44.82377 | 2024-10-05 04:38:00 | NOAA-20 | CURRAIS | PIAUÍ | Brasil | 2203230 | 22 | 33 | nan | nan | nan | Cerrado | 5.8 |
| ed21ea61-040c-33da-802f-30f2a5849189 | -8.76441 | -44.81906 | 2024-10-05 04:38:00 | NOAA-20 | CURRAIS | PIAUÍ | Brasil | 2203230 | 22 | 33 | nan | nan | nan | Cerrado | 11.5 |
| cef46a7a-acfe-31e6-97de-f90b6f7becfc | -10.77313 | -45.54757 | 2024-10-05 04:38:00 | NOAA-20 | FORMOSA DO RIO PRETO | BAHIA | Brasil | 2911105 | 29 | 33 | nan | nan | nan | Cerrado | 2.1 |
| 214645a9-165e-30dc-ab24-cad0b7f381b8 | -10.74241 | -44.61607 | 2024-10-05 04:38:00 | NOAA-20 | SANTA RITA DE CÁSSIA | BAHIA | Brasil | 2928406 | 29 | 33 | nan | nan | nan | Cerrado | 1.1 |
| c4e236ac-05a9-3446-9bf1-52687d39de26 | -10.74051 | -45.60608 | 2024-10-05 04:38:00 | NOAA-20 | FORMOSA DO RIO PRETO | BAHIA | Brasil | 2911105 | 29 | 33 | nan | nan | nan | Cerrado | 2.7 |
| 9f9d0c6e-32f6-3fb3-9896-4eceea1a86dc | -10.7358 | -45.61087 | 2024-10-05 04:38:00 | NOAA-20 | FORMOSA DO RIO PRETO | BAHIA | Brasil | 2911105 | 29 | 33 | nan | nan | nan | Cerrado | 0.9 |
| 1da6b3ec-3d95-30a2-9df2-9231fe3ede4f | -10.73505 | -45.61614 | 2024-10-05 04:38:00 | NOAA-20 | FORMOSA DO RIO PRETO | BAHIA | Brasil | 2911105 | 29 | 33 | nan | nan | nan | Cerrado | 0.9 |
| a3f368a2-b229-3e66-8563-1357b8ffc447 | -10.63598 | -45.20526 | 2024-10-05 04:38:00 | NOAA-20 | CRISTALÂNDIA DO PIAUÍ | PIAUÍ | Brasil | 2203008 | 22 | 33 | nan | nan | nan | Cerrado | 1.2 |
| 900e784e-56ba-353b-9b4f-80b4a6f0078d | -10.63547 | -45.20891 | 2024-10-05 04:38:00 | NOAA-20 | CRISTALÂNDIA DO PIAUÍ | PIAUÍ | Brasil | 2203008 | 22 | 33 | nan | nan | nan | Cerrado | 1.3 |
| abba467f-db10-3d7f-b4b8-f8d469514664 | -10.62127 | -45.19219 | 2024-10-05 04:38:00 | NOAA-20 | CRISTALÂNDIA DO PIAUÍ | PIAUÍ | Brasil | 2203008 | 22 | 33 | nan | nan | nan | Cerrado | 2.4 |
| 85adf729-8187-307e-acc1-cf91a7825e47 | -10.62065 | -45.19186 | 2024-10-05 04:38:00 | NOAA-20 | CRISTALÂNDIA DO PIAUÍ | PIAUÍ | Brasil | 2203008 | 22 | 33 | nan | nan | nan | Cerrado | 1.2 |
| 86586c07-ec2b-3598-a899-f14bb05e1bae | -10.62012 | -45.19553 | 2024-10-05 04:38:00 | NOAA-20 | CRISTALÂNDIA DO PIAUÍ | PIAUÍ | Brasil | 2203008 | 22 | 33 | nan | nan | nan | Cerrado | 1.2 |
| 591c59c6-3991-3459-a419-fff4c432f4b8 | -10.61772 | -45.18793 | 2024-10-05 04:38:00 | NOAA-20 | CRISTALÂNDIA DO PIAUÍ | PIAUÍ | Brasil | 2203008 | 22 | 33 | nan | nan | nan | Cerrado | 1.3 |
| 4c75996b-a8d1-3cc8-9c2a-e73d08d921fd | -10.61714 | -45.18761 | 2024-10-05 04:38:00 | NOAA-20 | CRISTALÂNDIA DO PIAUÍ | PIAUÍ | Brasil | 2203008 | 22 | 33 | nan | nan | nan | Cerrado | 0.9 |
| 7c05a1f6-ad59-3bff-8025-011706f19a8e | -10.27946 | -45.46984 | 2024-10-05 04:38:00 | NOAA-20 | SÃO GONÇALO DO GURGUÉIA | PIAUÍ | Brasil | 2209757 | 22 | 33 | nan | nan | nan | Cerrado | 2.6 |
| 2274474a-c40b-3c33-a94a-50d87cade55c | -10.27875 | -45.47497 | 2024-10-05 04:38:00 | NOAA-20 | SÃO GONÇALO DO GURGUÉIA | PIAUÍ | Brasil | 2209757 | 22 | 33 | nan | nan | nan | Cerrado | 5.7 |
| a6dd5937-13c0-3447-a61c-868e6d6c0fb5 | -10.27629 | -45.46367 | 2024-10-05 04:38:00 | NOAA-20 | SÃO GONÇALO DO GURGUÉIA | PIAUÍ | Brasil | 2209757 | 22 | 33 | nan | nan | nan | Cerrado | 6.7 |
| 9820660e-9cbf-3e08-9e29-e9a0e7792e87 | -10.27595 | -45.43712 | 2024-10-05 04:38:00 | NOAA-20 | CORRENTE | PIAUÍ | Brasil | 2202901 | 22 | 33 | nan | nan | nan | Cerrado | 3.4 |
| 05260bfa-1b5f-334a-8ba3-95e6a637af64 | -10.27557 | -45.4688 | 2024-10-05 04:38:00 | NOAA-20 | SÃO GONÇALO DO GURGUÉIA | PIAUÍ | Brasil | 2209757 | 22 | 33 | nan | nan | nan | Cerrado | 6.7 |
| 4aa6d20f-65ef-3662-a150-5bd2724a2f31 | -10.27486 | -45.47392 | 2024-10-05 04:38:00 | NOAA-20 | SÃO GONÇALO DO GURGUÉIA | PIAUÍ | Brasil | 2209757 | 22 | 33 | nan | nan | nan | Cerrado | 7.2 |
| ccf5eb86-88e5-3030-8b21-5180428339d6 | -10.27169 | -45.46769 | 2024-10-05 04:38:00 | NOAA-20 | SÃO GONÇALO DO GURGUÉIA | PIAUÍ | Brasil | 2209757 | 22 | 33 | nan | nan | nan | Cerrado | 6.7 |
| 6901f86d-8d0e-3a62-b000-2531278eae2c | -11.72785 | -44.96516 | 2024-10-05 04:38:00 | NOAA-20 | RIACHÃO DAS NEVES | BAHIA | Brasil | 2926202 | 29 | 33 | nan | nan | nan | Cerrado | 2.1 |
| dc000c56-c720-388d-a9ba-8c13e568305b | -11.67398 | -45.25778 | 2024-10-05 04:38:00 | NOAA-20 | RIACHÃO DAS NEVES | BAHIA | Brasil | 2926202 | 29 | 33 | nan | nan | nan | Cerrado | 1.5 |
| 6df66faa-f365-3171-98c4-ec8ef82c3032 | -11.67348 | -45.26135 | 2024-10-05 04:38:00 | NOAA-20 | RIACHÃO DAS NEVES | BAHIA | Brasil | 2926202 | 29 | 33 | nan | nan | nan | Cerrado | 1.5 |


[Clique aqui para ver as próximas entradas](README97.md)
