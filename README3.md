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

## Dados Diários - Página 3

| ID | Latitude | Longitude | Data/Hora GMT | Satélite | Município | Estado | País | Município ID | Estado ID | País ID | Dias sem Chuva | Precipitação | Risco de Fogo | Bioma | FRP |
|----|----------|-----------|---------------|----------|-----------|--------|------|--------------|-----------|---------|----------------|--------------|----------------|-------|-----|
| 0f65a2e4-b1db-3765-9d96-42cb8c76de32 | -19.18057 | -44.51775 | 2025-08-26 00:26:00 | TERRA_M-M | PARAOPEBA | MINAS GERAIS | Brasil | 3147402 | 31 | 33 | nan | nan | nan | Cerrado | 5.8 |
| f0df4b15-ce8d-32d4-a525-10daa0e5ac12 | -21.61119 | -49.69906 | 2025-08-26 00:26:00 | TERRA_M-M | LINS | SÃO PAULO | Brasil | 3527108 | 35 | 33 | nan | nan | nan | Mata Atlântica | 21.5 |
| a66af5db-578c-30d4-9dc4-69e7f20f99a1 | -17.38518 | -48.13988 | 2025-08-26 00:26:00 | TERRA_M-M | URUTAÍ | GOIÁS | Brasil | 5221809 | 52 | 33 | nan | nan | nan | Cerrado | 16.3 |
| c572e464-4861-3150-85ef-0e6ab3ee8701 | -19.91486 | -44.62899 | 2025-08-26 00:26:00 | TERRA_M-M | PARÁ DE MINAS | MINAS GERAIS | Brasil | 3147105 | 31 | 33 | nan | nan | nan | Mata Atlântica | 4.1 |
| b0fab7ae-263d-3fc3-b7c0-9ed9f3b71884 | -20.88795 | -49.0293 | 2025-08-26 00:26:00 | TERRA_M-M | TABAPUÃ | SÃO PAULO | Brasil | 3552601 | 35 | 33 | nan | nan | nan | Mata Atlântica | 32.7 |
| 700d4075-30de-3ed4-89d5-9fe9c037afba | -18.87261 | -47.00165 | 2025-08-26 00:26:00 | TERRA_M-M | PATROCÍNIO | MINAS GERAIS | Brasil | 3148103 | 31 | 33 | nan | nan | nan | Cerrado | 12.2 |
| 93c1986d-946b-32b3-a29d-455d2fb3bf5d | -21.42795 | -45.46877 | 2025-08-26 00:26:00 | TERRA_M-M | TRÊS PONTAS | MINAS GERAIS | Brasil | 3169406 | 31 | 33 | nan | nan | nan | Mata Atlântica | 5.7 |
| d34c5851-6ea0-3f5d-b850-cd6c9dd323cd | -18.85547 | -47.0147 | 2025-08-26 00:26:00 | TERRA_M-M | PATROCÍNIO | MINAS GERAIS | Brasil | 3148103 | 31 | 33 | nan | nan | nan | Cerrado | 9.2 |
| 01a618f1-8eb0-30c2-ba29-bbdf32418af6 | -23.0286 | -45.34004 | 2025-08-26 00:26:00 | TERRA_M-M | PINDAMONHANGABA | SÃO PAULO | Brasil | 3538006 | 35 | 33 | nan | nan | nan | Mata Atlântica | 5.7 |
| 07d36bf1-b485-3b1a-b1f6-849d94bf0fd2 | -22.89714 | -49.06195 | 2025-08-26 00:26:00 | TERRA_M-M | IARAS | SÃO PAULO | Brasil | 3519253 | 35 | 33 | nan | nan | nan | Cerrado | 20.4 |
| 82b2afc4-038f-396b-b288-b6f8c423b610 | -17.78522 | -44.48762 | 2025-08-26 00:26:00 | TERRA_M-M | LASSANCE | MINAS GERAIS | Brasil | 3138104 | 31 | 33 | nan | nan | nan | Cerrado | 4.6 |
| b993767a-0c11-3e7d-9c7d-6740106e69f3 | -21.04913 | -41.9826 | 2025-08-26 00:26:00 | TERRA_M-M | NATIVIDADE | RIO DE JANEIRO | Brasil | 3303104 | 33 | 33 | nan | nan | nan | Mata Atlântica | 8.5 |
| 3f5dfeff-8e07-389e-8e5d-68bf617ef731 | -17.37815 | -48.08489 | 2025-08-26 00:26:00 | TERRA_M-M | URUTAÍ | GOIÁS | Brasil | 5221809 | 52 | 33 | nan | nan | nan | Cerrado | 8.6 |
| 2c0c2abc-651a-3261-8bd2-6f1a2b3c95dd | -18.85412 | -47.00421 | 2025-08-26 00:26:00 | TERRA_M-M | PATROCÍNIO | MINAS GERAIS | Brasil | 3148103 | 31 | 33 | nan | nan | nan | Cerrado | 8.9 |
| 5ba2dc24-0cb1-3a00-9b09-3e5286ce2b47 | -22.35395 | -48.40083 | 2025-08-26 00:26:00 | TERRA_M-M | DOIS CÓRREGOS | SÃO PAULO | Brasil | 3514106 | 35 | 33 | nan | nan | nan | Mata Atlântica | 20.8 |
| be7307de-3313-31c1-b989-25dddc6fa979 | -17.66464 | -40.19481 | 2025-08-26 00:26:00 | TERRA_M-M | IBIRAPUÃ | BAHIA | Brasil | 2912806 | 29 | 33 | nan | nan | nan | Mata Atlântica | 137.8 |
| 888dc568-0764-329a-8735-d76e8f80a74a | -17.81733 | -42.82719 | 2025-08-26 00:26:00 | TERRA_M-M | ITAMARANDIBA | MINAS GERAIS | Brasil | 3132503 | 31 | 33 | nan | nan | nan | Cerrado | 39.8 |
| beb904d3-b895-3063-bde4-982a3f9a04ab | -20.38679 | -42.19343 | 2025-08-26 00:26:00 | TERRA_M-M | SANTA MARGARIDA | MINAS GERAIS | Brasil | 3157906 | 31 | 33 | nan | nan | nan | Mata Atlântica | 8.7 |
| 402b73f6-d365-3664-b3ee-885577c7eafb | -19.03555 | -46.91406 | 2025-08-26 00:26:00 | TERRA_M-M | PATROCÍNIO | MINAS GERAIS | Brasil | 3148103 | 31 | 33 | nan | nan | nan | Cerrado | 17.0 |
| 1391660e-47db-3c24-badd-f61b82dce064 | -20.73001 | -40.66371 | 2025-08-26 00:26:00 | TERRA_M-M | ANCHIETA | ESPÍRITO SANTO | Brasil | 3200409 | 32 | 33 | nan | nan | nan | Mata Atlântica | 9.0 |
| 0acfc90e-7f2b-3271-ab79-927d92ec13a2 | -19.92371 | -44.62759 | 2025-08-26 00:26:00 | TERRA_M-M | PARÁ DE MINAS | MINAS GERAIS | Brasil | 3147105 | 31 | 33 | nan | nan | nan | Mata Atlântica | 10.7 |
| b72ee1bb-82fb-37b2-aefb-083064756ce7 | -22.90821 | -49.06046 | 2025-08-26 00:26:00 | TERRA_M-M | IARAS | SÃO PAULO | Brasil | 3519253 | 35 | 33 | nan | nan | nan | Cerrado | 14.2 |
| 7962df87-3686-3c73-ac17-883a3441a4af | -17.61197 | -46.70985 | 2025-08-26 00:26:00 | TERRA_M-M | VAZANTE | MINAS GERAIS | Brasil | 3171006 | 31 | 33 | nan | nan | nan | Cerrado | 5.4 |
| 9edbfb9f-9edb-3ce3-bd76-29c4288afa44 | -20.96252 | -42.8863 | 2025-08-26 00:26:00 | TERRA_M-M | VISCONDE DO RIO BRANCO | MINAS GERAIS | Brasil | 3172004 | 31 | 33 | nan | nan | nan | Mata Atlântica | 15.7 |
| 6336cd2e-861e-357c-8d2e-3ef48141edae | -17.87275 | -42.24613 | 2025-08-26 00:26:00 | TERRA_M-M | MALACACHETA | MINAS GERAIS | Brasil | 3139201 | 31 | 33 | nan | nan | nan | Mata Atlântica | 7.8 |
| 38994023-9a43-3df2-aa5e-a85da8a7ce15 | -21.00161 | -46.99169 | 2025-08-26 00:26:00 | TERRA_M-M | SÃO SEBASTIÃO DO PARAÍSO | MINAS GERAIS | Brasil | 3164704 | 31 | 33 | nan | nan | nan | Cerrado | 9.0 |
| 72fa92c0-8d61-39e0-a43f-d36948c1c834 | -20.37879 | -42.20463 | 2025-08-26 00:26:00 | TERRA_M-M | SANTA MARGARIDA | MINAS GERAIS | Brasil | 3157906 | 31 | 33 | nan | nan | nan | Mata Atlântica | 9.6 |
| 0d055a6e-7105-3158-a4a5-49dd50ca3848 | -17.60943 | -46.6905 | 2025-08-26 00:26:00 | TERRA_M-M | VAZANTE | MINAS GERAIS | Brasil | 3171006 | 31 | 33 | nan | nan | nan | Cerrado | 25.0 |
| 4efd500f-b537-3364-a400-061a359c8b6f | -17.6107 | -46.70016 | 2025-08-26 00:26:00 | TERRA_M-M | VAZANTE | MINAS GERAIS | Brasil | 3171006 | 31 | 33 | nan | nan | nan | Cerrado | 10.1 |
| 7dd2be33-80e5-39d5-a69c-58b05d225dd5 | -21.33536 | -43.85832 | 2025-08-26 00:26:00 | TERRA_M-M | ANTÔNIO CARLOS | MINAS GERAIS | Brasil | 3102902 | 31 | 33 | nan | nan | nan | Mata Atlântica | 6.0 |
| 5d163a92-ae07-3814-a88c-4111b251614a | -17.39481 | -48.13851 | 2025-08-26 00:26:00 | TERRA_M-M | URUTAÍ | GOIÁS | Brasil | 5221809 | 52 | 33 | nan | nan | nan | Cerrado | 12.5 |
| e297f503-ccd4-3e2a-88e5-028916c1e051 | -18.8081 | -47.59353 | 2025-08-26 00:26:00 | TERRA_M-M | MONTE CARMELO | MINAS GERAIS | Brasil | 3143104 | 31 | 33 | nan | nan | nan | Cerrado | 13.0 |
| fcb281c7-bd12-3cb8-8baf-db93b8e02478 | -22.16527 | -47.07351 | 2025-08-26 00:26:00 | TERRA_M-M | MOGI GUAÇU | SÃO PAULO | Brasil | 3530706 | 35 | 33 | nan | nan | nan | Cerrado | 6.1 |
| b63e12ba-58dd-3e7b-b968-82794dfd7ff2 | -22.99119 | -45.47506 | 2025-08-26 00:26:00 | TERRA_M-M | PINDAMONHANGABA | SÃO PAULO | Brasil | 3538006 | 35 | 33 | nan | nan | nan | Mata Atlântica | 6.4 |
| ad726ff3-462c-35df-9c62-423b85019528 | -17.81893 | -42.83773 | 2025-08-26 00:26:00 | TERRA_M-M | ITAMARANDIBA | MINAS GERAIS | Brasil | 3132503 | 31 | 33 | nan | nan | nan | Cerrado | 15.5 |
| 8af92a16-8385-3339-a336-63878be6c7eb | -20.37727 | -42.19476 | 2025-08-26 00:26:00 | TERRA_M-M | SANTA MARGARIDA | MINAS GERAIS | Brasil | 3157906 | 31 | 33 | nan | nan | nan | Mata Atlântica | 24.7 |
| 72a423d0-2e24-3d10-9ec8-e87df2ff549f | -21.42925 | -45.47846 | 2025-08-26 00:26:00 | TERRA_M-M | TRÊS PONTAS | MINAS GERAIS | Brasil | 3169406 | 31 | 33 | nan | nan | nan | Mata Atlântica | 6.6 |
| 7e628ffb-baaa-3ddc-a927-2d8fe063693f | -20.88444 | -49.0359 | 2025-08-26 00:26:00 | TERRA_M-M | TABAPUÃ | SÃO PAULO | Brasil | 3552601 | 35 | 33 | nan | nan | nan | Mata Atlântica | 9.8 |
| 9960a98d-4379-3362-ba37-7e54b9c07c98 | -20.85647 | -48.46881 | 2025-08-26 00:26:00 | TERRA_M-M | BEBEDOURO | SÃO PAULO | Brasil | 3506102 | 35 | 33 | nan | nan | nan | Cerrado | 33.9 |
| ef617aa8-9fcd-3389-a6c0-57b364c96418 | -18.80943 | -47.60432 | 2025-08-26 00:26:00 | TERRA_M-M | MONTE CARMELO | MINAS GERAIS | Brasil | 3143104 | 31 | 33 | nan | nan | nan | Cerrado | 16.6 |
| ce0411f6-9a33-308b-a53f-f4b89811299f | -22.5496 | -46.82246 | 2025-08-26 00:26:00 | TERRA_M-M | ITAPIRA | SÃO PAULO | Brasil | 3522604 | 35 | 33 | nan | nan | nan | Mata Atlântica | 7.3 |
| aa878617-77e3-3d71-b4d5-ab69df0e4ae0 | -21.72758 | -46.81 | 2025-08-26 00:26:00 | TERRA_M-M | SÃO SEBASTIÃO DA GRAMA | SÃO PAULO | Brasil | 3550803 | 35 | 33 | nan | nan | nan | Mata Atlântica | 7.7 |
| 68173dd3-bddc-3ef7-b79b-dd13dc1d8274 | -17.66725 | -40.21043 | 2025-08-26 00:26:00 | TERRA_M-M | IBIRAPUÃ | BAHIA | Brasil | 2912806 | 29 | 33 | nan | nan | nan | Mata Atlântica | 208.2 |
| 1d5eb4a2-b41e-363b-8735-a4e88df01690 | -20.20355 | -47.01493 | 2025-08-26 00:26:00 | TERRA_M-M | DELFINÓPOLIS | MINAS GERAIS | Brasil | 3121209 | 31 | 33 | nan | nan | nan | Cerrado | 11.5 |
| ddb74736-05b3-3c26-b7ff-5810736a297e | -17.20004 | -44.32759 | 2025-08-26 00:26:00 | TERRA_M-M | JEQUITAÍ | MINAS GERAIS | Brasil | 3135605 | 31 | 33 | nan | nan | nan | Cerrado | 28.3 |
| 8bdb27ad-2c55-3958-b383-d6b291b78b27 | -20.858 | -48.48197 | 2025-08-26 00:26:00 | TERRA_M-M | BEBEDOURO | SÃO PAULO | Brasil | 3506102 | 35 | 33 | nan | nan | nan | Cerrado | 15.0 |
| 851bbf44-6897-35cd-9217-b7957ba7c72a | -20.19402 | -44.58493 | 2025-08-26 00:26:00 | TERRA_M-M | ITAÚNA | MINAS GERAIS | Brasil | 3133808 | 31 | 33 | nan | nan | nan | Mata Atlântica | 4.6 |
| baf67152-a2a7-3bfa-90a3-a9f5b5aa6c8a | -19.03686 | -46.92421 | 2025-08-26 00:26:00 | TERRA_M-M | PATROCÍNIO | MINAS GERAIS | Brasil | 3148103 | 31 | 33 | nan | nan | nan | Cerrado | 6.2 |
| 46765c63-6013-358d-b747-e41aaaab69d2 | -19.97891 | -41.81599 | 2025-08-26 00:26:00 | TERRA_M-M | SANTANA DO MANHUAÇU | MINAS GERAIS | Brasil | 3158904 | 31 | 33 | nan | nan | nan | Mata Atlântica | 7.2 |
| ecc90844-65a9-31ad-b9f9-97b9cd1e3b09 | -20.04961 | -44.47052 | 2025-08-26 00:26:00 | TERRA_M-M | MATEUS LEME | MINAS GERAIS | Brasil | 3140704 | 31 | 33 | nan | nan | nan | Mata Atlântica | 5.6 |
| b3a0e4d1-b070-3935-9a33-24a14decb661 | -21.33672 | -43.86783 | 2025-08-26 00:26:00 | TERRA_M-M | ANTÔNIO CARLOS | MINAS GERAIS | Brasil | 3102902 | 31 | 33 | nan | nan | nan | Mata Atlântica | 11.2 |
| b5b19628-2b95-3c6a-8166-f8108e8ff0f7 | -18.5304 | -46.28666 | 2025-08-26 00:26:00 | TERRA_M-M | PRESIDENTE OLEGÁRIO | MINAS GERAIS | Brasil | 3153400 | 31 | 33 | nan | nan | nan | Cerrado | 6.3 |
| a4fe09be-4c7e-31c6-9032-b013116dde06 | -20.8172 | -42.78275 | 2025-08-26 00:26:00 | TERRA_M-M | CAJURI | MINAS GERAIS | Brasil | 3110202 | 31 | 33 | nan | nan | nan | Mata Atlântica | 8.0 |
| dcf336c6-2a80-378b-abd2-3767f84db02c | -18.84623 | -47.01608 | 2025-08-26 00:26:00 | TERRA_M-M | PATROCÍNIO | MINAS GERAIS | Brasil | 3148103 | 31 | 33 | nan | nan | nan | Cerrado | 10.5 |
| 449f7a4e-68e4-34de-807c-4ee586e1d74a | -22.89775 | -49.05558 | 2025-08-26 00:26:00 | TERRA_M-M | IARAS | SÃO PAULO | Brasil | 3519253 | 35 | 33 | nan | nan | nan | Cerrado | 23.4 |
| 9dfd7e44-48e0-3d14-b34d-ef8f9eef315e | -11.14918 | -44.75876 | 2025-08-26 00:28:00 | TERRA_M-M | SANTA RITA DE CÁSSIA | BAHIA | Brasil | 2928406 | 29 | 33 | nan | nan | nan | Cerrado | 130.1 |
| d5b08cc8-743e-3f09-b1cb-c32daa68fac6 | -13.44741 | -46.8724 | 2025-08-26 00:28:00 | TERRA_M-M | MONTE ALEGRE DE GOIÁS | GOIÁS | Brasil | 5213509 | 52 | 33 | nan | nan | nan | Cerrado | 5.5 |
| 103bff22-e16d-3091-ac9f-1baf07e73511 | -12.44137 | -48.70953 | 2025-08-26 00:28:00 | TERRA_M-M | JAÚ DO TOCANTINS | TOCANTINS | Brasil | 1711506 | 17 | 33 | nan | nan | nan | Cerrado | 22.1 |
| e566fa78-f1f0-3c58-ae4c-ff7f7ea66b50 | -12.43037 | -45.97097 | 2025-08-26 00:28:00 | TERRA_M-M | LUÍS EDUARDO MAGALHÃES | BAHIA | Brasil | 2919553 | 29 | 33 | nan | nan | nan | Cerrado | 22.4 |
| cf941394-17ed-386b-9f9f-54ff9ce913c0 | -15.83959 | -42.63025 | 2025-08-26 00:28:00 | TERRA_M-M | RIO PARDO DE MINAS | MINAS GERAIS | Brasil | 3155603 | 31 | 33 | nan | nan | nan | Mata Atlântica | 7.8 |
| 4e7cedb0-38e4-387c-a438-c2cb3fd9cc4e | -11.15991 | -44.76729 | 2025-08-26 00:28:00 | TERRA_M-M | SANTA RITA DE CÁSSIA | BAHIA | Brasil | 2928406 | 29 | 33 | nan | nan | nan | Cerrado | 78.6 |
| df14dfda-6068-30cf-aa18-5da0bc7e950a | -11.43971 | -47.33411 | 2025-08-26 00:28:00 | TERRA_M-M | ALMAS | TOCANTINS | Brasil | 1700400 | 17 | 33 | nan | nan | nan | Cerrado | 8.3 |
| 1f0e5463-7784-36db-913b-639818d4ea2a | -11.63086 | -46.38982 | 2025-08-26 00:28:00 | TERRA_M-M | NOVO JARDIM | TOCANTINS | Brasil | 1715259 | 17 | 33 | nan | nan | nan | Cerrado | 17.7 |
| cc203c7c-be80-33c0-94a1-0bf0e3c22735 | -12.74721 | -48.16438 | 2025-08-26 00:28:00 | TERRA_M-M | PARANÃ | TOCANTINS | Brasil | 1716208 | 17 | 33 | nan | nan | nan | Cerrado | 11.4 |
| 484a6f57-7fb4-3764-8886-18457089b693 | -11.92873 | -46.73986 | 2025-08-26 00:28:00 | TERRA_M-M | NOVO JARDIM | TOCANTINS | Brasil | 1715259 | 17 | 33 | nan | nan | nan | Cerrado | 8.2 |
| 9b2437bf-a355-35cf-82b4-1fa551ac0951 | -12.38126 | -46.55126 | 2025-08-26 00:28:00 | TERRA_M-M | TAGUATINGA | TOCANTINS | Brasil | 1720903 | 17 | 33 | nan | nan | nan | Cerrado | 4.7 |
| a20ab38f-3a5a-3e31-adbb-d21b969a68b0 | -13.44616 | -46.86326 | 2025-08-26 00:28:00 | TERRA_M-M | MONTE ALEGRE DE GOIÁS | GOIÁS | Brasil | 5213509 | 52 | 33 | nan | nan | nan | Cerrado | 6.7 |
| ada65a41-1b8d-3a06-9621-bb963767419f | -13.44707 | -47.00271 | 2025-08-26 00:28:00 | TERRA_M-M | MONTE ALEGRE DE GOIÁS | GOIÁS | Brasil | 5213509 | 52 | 33 | nan | nan | nan | Cerrado | 9.8 |
| b7373a85-1811-36ed-9cc5-c7bd1aa1b830 | -12.41146 | -46.49508 | 2025-08-26 00:28:00 | TERRA_M-M | TAGUATINGA | TOCANTINS | Brasil | 1720903 | 17 | 33 | nan | nan | nan | Cerrado | 6.1 |
| 2cbd4380-b87a-31cd-b741-ebda50bd087b | -10.75025 | -47.07227 | 2025-08-26 00:28:00 | TERRA_M-M | PONTE ALTA DO TOCANTINS | TOCANTINS | Brasil | 1717909 | 17 | 33 | nan | nan | nan | Cerrado | 58.1 |
| bb97b485-a3ac-368c-9602-6e5efff47b3d | -10.82674 | -48.31691 | 2025-08-26 00:28:00 | TERRA_M-M | PORTO NACIONAL | TOCANTINS | Brasil | 1718204 | 17 | 33 | nan | nan | nan | Cerrado | 14.4 |
| e4c17ad7-fb21-3d0f-810f-b6db5406f306 | -13.4144 | -46.89575 | 2025-08-26 00:28:00 | TERRA_M-M | MONTE ALEGRE DE GOIÁS | GOIÁS | Brasil | 5213509 | 52 | 33 | nan | nan | nan | Cerrado | 6.8 |
| e5386b35-0b79-3b83-8fad-5fabe6f37325 | -13.51651 | -46.90265 | 2025-08-26 00:28:00 | TERRA_M-M | MONTE ALEGRE DE GOIÁS | GOIÁS | Brasil | 5213509 | 52 | 33 | nan | nan | nan | Cerrado | 7.7 |
| 0483092e-5b46-3dc1-87df-eaf9bde40f78 | -15.50612 | -47.88806 | 2025-08-26 00:28:00 | TERRA_M-M | BRASÍLIA | DISTRITO FEDERAL | Brasil | 5300108 | 53 | 33 | nan | nan | nan | Cerrado | 6.6 |
| 2766ce3e-c2eb-36b4-a8cf-8f003d23cc6b | -10.80857 | -48.31946 | 2025-08-26 00:28:00 | TERRA_M-M | PORTO NACIONAL | TOCANTINS | Brasil | 1718204 | 17 | 33 | nan | nan | nan | Cerrado | 14.9 |
| 8cf3bdd0-ed32-3c45-93ac-387bdf2c2427 | -11.6353 | -44.86538 | 2025-08-26 00:28:00 | TERRA_M-M | RIACHÃO DAS NEVES | BAHIA | Brasil | 2926202 | 29 | 33 | nan | nan | nan | Cerrado | 29.2 |
| 9fe4043d-f894-3b0c-b819-4d0a68c18125 | -10.45932 | -48.80109 | 2025-08-26 00:28:00 | TERRA_M-M | PUGMIL | TOCANTINS | Brasil | 1718451 | 17 | 33 | nan | nan | nan | Cerrado | 15.5 |
| 2e4a71ee-6b5c-3689-b9e8-47b858823dd5 | -10.51547 | -46.77232 | 2025-08-26 00:28:00 | TERRA_M-M | MATEIROS | TOCANTINS | Brasil | 1712702 | 17 | 33 | nan | nan | nan | Cerrado | 18.6 |
| a25475b7-c42a-30a7-9e26-40a4bed2950a | -10.67943 | -47.16186 | 2025-08-26 00:28:00 | TERRA_M-M | PONTE ALTA DO TOCANTINS | TOCANTINS | Brasil | 1717909 | 17 | 33 | nan | nan | nan | Cerrado | 6.4 |
| 57704854-06bb-3b79-8e89-4f0b458414ae | -12.70903 | -47.87587 | 2025-08-26 00:28:00 | TERRA_M-M | PARANÃ | TOCANTINS | Brasil | 1716208 | 17 | 33 | nan | nan | nan | Cerrado | 8.6 |
| b64f0ab2-cc9e-305e-901d-24124bbe5d5d | -14.23804 | -44.11963 | 2025-08-26 00:28:00 | TERRA_M-M | FEIRA DA MATA | BAHIA | Brasil | 2910776 | 29 | 33 | nan | nan | nan | Cerrado | 12.7 |
| 59f59014-6754-35e4-a310-b139fa8012e0 | -11.15698 | -44.74732 | 2025-08-26 00:28:00 | TERRA_M-M | SANTA RITA DE CÁSSIA | BAHIA | Brasil | 2928406 | 29 | 33 | nan | nan | nan | Cerrado | 62.3 |
| 25ae0e53-eb9b-3ec8-a5c2-9bfa95bc4102 | -12.74591 | -48.15454 | 2025-08-26 00:28:00 | TERRA_M-M | PARANÃ | TOCANTINS | Brasil | 1716208 | 17 | 33 | nan | nan | nan | Cerrado | 23.7 |
| 403ac6c7-ab46-3afe-994d-ac9d563743c9 | -11.61569 | -46.41034 | 2025-08-26 00:28:00 | TERRA_M-M | DIANÓPOLIS | TOCANTINS | Brasil | 1707009 | 17 | 33 | nan | nan | nan | Cerrado | 9.7 |
| 6c30430a-ee22-391d-a5e4-f8d66457a0e7 | -11.56942 | -52.11943 | 2025-08-26 00:28:00 | TERRA_M-M | SÃO FÉLIX DO ARAGUAIA | MATO GROSSO | Brasil | 5107859 | 51 | 33 | nan | nan | nan | Amazônia | 24.4 |
| 94990e84-e27a-3af4-a7ea-43f7b7ce9e4d | -11.63336 | -46.40774 | 2025-08-26 00:28:00 | TERRA_M-M | NOVO JARDIM | TOCANTINS | Brasil | 1715259 | 17 | 33 | nan | nan | nan | Cerrado | 8.5 |
| 432ba0d7-976a-3621-b91c-5fc127ebbd45 | -13.05778 | -46.31097 | 2025-08-26 00:28:00 | TERRA_M-M | CAMPOS BELOS | GOIÁS | Brasil | 5204904 | 52 | 33 | nan | nan | nan | Cerrado | 18.5 |
| 7c98af82-c416-390a-8d0c-9a7646b18f51 | -13.17071 | -45.28067 | 2025-08-26 00:28:00 | TERRA_M-M | CORRENTINA | BAHIA | Brasil | 2909307 | 29 | 33 | nan | nan | nan | Cerrado | 9.4 |
| 13dc0256-5739-316f-b19f-d01d00912b4b | -12.73671 | -48.1556 | 2025-08-26 00:28:00 | TERRA_M-M | PARANÃ | TOCANTINS | Brasil | 1716208 | 17 | 33 | nan | nan | nan | Cerrado | 12.3 |
| 17f092a8-11c0-3823-bbfc-85d119b6ad30 | -11.55567 | -52.10423 | 2025-08-26 00:28:00 | TERRA_M-M | SÃO FÉLIX DO ARAGUAIA | MATO GROSSO | Brasil | 5107859 | 51 | 33 | nan | nan | nan | Amazônia | 40.2 |
| 4c15f74a-6274-3b42-ba9a-2f45dd597261 | -12.94058 | -46.32536 | 2025-08-26 00:28:00 | TERRA_M-M | LAVANDEIRA | TOCANTINS | Brasil | 1712157 | 17 | 33 | nan | nan | nan | Cerrado | 11.4 |
| 2ae31572-84f3-361f-bef5-60e19c9161f0 | -11.91759 | -47.5982 | 2025-08-26 00:28:00 | TERRA_M-M | NATIVIDADE | TOCANTINS | Brasil | 1714203 | 17 | 33 | nan | nan | nan | Cerrado | 6.8 |
| 06cd6f13-425a-3e2d-94a3-8f601ccf30fe | -11.55083 | -52.12805 | 2025-08-26 00:28:00 | TERRA_M-M | SÃO FÉLIX DO ARAGUAIA | MATO GROSSO | Brasil | 5107859 | 51 | 33 | nan | nan | nan | Amazônia | 306.9 |
| ae81f8e7-e68a-3a5c-a6ef-f2eea1f8c073 | -12.42909 | -45.96191 | 2025-08-26 00:28:00 | TERRA_M-M | LUÍS EDUARDO MAGALHÃES | BAHIA | Brasil | 2919553 | 29 | 33 | nan | nan | nan | Cerrado | 11.1 |
| 703aea3f-e541-3ccd-b584-25c4e27211d6 | -12.94183 | -46.33437 | 2025-08-26 00:28:00 | TERRA_M-M | LAVANDEIRA | TOCANTINS | Brasil | 1712157 | 17 | 33 | nan | nan | nan | Cerrado | 36.0 |
| af332948-7efc-32f7-846d-dbbc559c419f | -17.00416 | -48.66522 | 2025-08-26 00:28:00 | TERRA_M-M | SÃO MIGUEL DO PASSA QUATRO | GOIÁS | Brasil | 5220264 | 52 | 33 | nan | nan | nan | Cerrado | 6.9 |
| d976bec9-271d-3d60-aaed-04fd5b2997a9 | -11.03744 | -49.14582 | 2025-08-26 00:28:00 | TERRA_M-M | SANTA RITA DO TOCANTINS | TOCANTINS | Brasil | 1718899 | 17 | 33 | nan | nan | nan | Cerrado | 9.0 |
| a77cd33c-bd05-3fbd-8a27-7955407f5573 | -14.36974 | -51.90756 | 2025-08-26 00:28:00 | TERRA_M-M | NOVA NAZARÉ | MATO GROSSO | Brasil | 5106174 | 51 | 33 | nan | nan | nan | Cerrado | 20.1 |
| 900b4a6a-f989-3d26-8b73-c7f447922179 | -12.4427 | -48.71978 | 2025-08-26 00:28:00 | TERRA_M-M | JAÚ DO TOCANTINS | TOCANTINS | Brasil | 1711506 | 17 | 33 | nan | nan | nan | Cerrado | 28.8 |
| 4583e93e-de24-3817-ae01-f69c23cb8797 | -13.48696 | -47.01905 | 2025-08-26 00:28:00 | TERRA_M-M | MONTE ALEGRE DE GOIÁS | GOIÁS | Brasil | 5213509 | 52 | 33 | nan | nan | nan | Cerrado | 5.2 |


[Clique aqui para ver as próximas entradas](README4.md)
