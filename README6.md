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
| f55f8d16-8999-3291-8108-4e230a5d55ed | -8.68174 | -40.42206 | 2025-10-11 03:19:00 | NPP-375D | PETROLINA | PERNAMBUCO | Brasil | 2611101 | 26 | 33 | nan | nan | nan | Caatinga | 2.6 |
| 414b876a-5dd6-3e0d-ae62-d0b41f10258a | -8.14694 | -43.33435 | 2025-10-11 03:19:00 | NPP-375D | CANTO DO BURITI | PIAUÍ | Brasil | 2202307 | 22 | 33 | nan | nan | nan | Caatinga | 4.1 |
| 34045eae-9201-3db2-bb54-413a0742dcc1 | -5.59268 | -41.10986 | 2025-10-11 03:19:00 | NPP-375D | SÃO MIGUEL DO TAPUIO | PIAUÍ | Brasil | 2210409 | 22 | 33 | nan | nan | nan | Caatinga | 1.2 |
| aacca961-3d54-3032-abf5-1322afe91698 | -7.67236 | -42.57573 | 2025-10-11 03:19:00 | NPP-375D | SÃO JOSÉ DO PEIXE | PIAUÍ | Brasil | 2210102 | 22 | 33 | nan | nan | nan | Caatinga | 2.0 |
| f7f096d0-6d2b-3da0-84a5-184c1ac8814d | -8.19374 | -43.32324 | 2025-10-11 03:19:00 | NPP-375D | CANTO DO BURITI | PIAUÍ | Brasil | 2202307 | 22 | 33 | nan | nan | nan | Caatinga | 12.7 |
| 6a7e1c30-8e09-3349-97e1-00ece94503a7 | -3.13113 | -41.00226 | 2025-10-11 03:19:00 | NPP-375D | GRANJA | CEARÁ | Brasil | 2304707 | 23 | 33 | nan | nan | nan | Caatinga | 1.4 |
| d59f75c7-57c9-3c4f-aabf-ba3db4ed4025 | -7.36657 | -38.76217 | 2025-10-11 03:19:00 | NPP-375D | MAURITI | CEARÁ | Brasil | 2308104 | 23 | 33 | nan | nan | nan | Caatinga | 5.3 |
| dff96cf4-76b0-30c3-b066-c782cf082ee7 | -5.86737 | -42.86015 | 2025-10-11 03:19:00 | NPP-375D | PALMEIRAIS | PIAUÍ | Brasil | 2207504 | 22 | 33 | nan | nan | nan | Caatinga | 47.7 |
| d91a890d-2486-3c9d-acf9-1c4f68677060 | -7.6573 | -42.57938 | 2025-10-11 03:19:00 | NPP-375D | SÃO JOSÉ DO PEIXE | PIAUÍ | Brasil | 2210102 | 22 | 33 | nan | nan | nan | Caatinga | 2.4 |
| ab51e766-1a69-3453-a46e-660300701037 | -4.08952 | -38.65987 | 2025-10-11 03:19:00 | NPP-375D | GUAIÚBA | CEARÁ | Brasil | 2304954 | 23 | 33 | nan | nan | nan | Caatinga | 1.2 |
| a309e99d-9120-3a0c-9d14-a86f6db76439 | -5.58593 | -41.11974 | 2025-10-11 03:19:00 | NPP-375D | SÃO MIGUEL DO TAPUIO | PIAUÍ | Brasil | 2210409 | 22 | 33 | nan | nan | nan | Caatinga | 2.3 |
| 47094db0-09b6-3ee0-a92c-f035197143fd | -8.19949 | -43.33184 | 2025-10-11 03:19:00 | NPP-375D | CANTO DO BURITI | PIAUÍ | Brasil | 2202307 | 22 | 33 | nan | nan | nan | Caatinga | 14.4 |
| 05637191-a52b-35a9-bdca-d6a1e2d66866 | -4.44377 | -40.77195 | 2025-10-11 03:19:00 | NPP-375D | IPUEIRAS | CEARÁ | Brasil | 2305902 | 23 | 33 | nan | nan | nan | Caatinga | 1.2 |
| 453c0687-9fa9-38f2-a19a-607aefe3dcdf | -6.03921 | -42.51284 | 2025-10-11 03:19:00 | NPP-375D | HUGO NAPOLEÃO | PIAUÍ | Brasil | 2204600 | 22 | 33 | nan | nan | nan | Caatinga | 2.4 |
| d92e26a6-035d-37e4-813f-db2b4a117ce6 | -7.65706 | -42.58555 | 2025-10-11 03:19:00 | NPP-375D | RIBEIRA DO PIAUÍ | PIAUÍ | Brasil | 2208874 | 22 | 33 | nan | nan | nan | Caatinga | 2.4 |
| af7eb116-2325-3926-aafe-b95afba5c244 | -8.20173 | -43.33054 | 2025-10-11 03:19:00 | NPP-375D | CANTO DO BURITI | PIAUÍ | Brasil | 2202307 | 22 | 33 | nan | nan | nan | Caatinga | 12.8 |
| b19785f1-e507-364c-9ad7-b889de31b5a4 | -5.86142 | -42.84409 | 2025-10-11 03:19:00 | NPP-375D | SÃO PEDRO DO PIAUÍ | PIAUÍ | Brasil | 2210508 | 22 | 33 | nan | nan | nan | Caatinga | 21.6 |
| 6e33beb1-2aec-346d-be37-86c3d2b58744 | -5.1477 | -38.06066 | 2025-10-11 03:19:00 | NPP-375D | LIMOEIRO DO NORTE | CEARÁ | Brasil | 2307601 | 23 | 33 | nan | nan | nan | Caatinga | 0.5 |
| e5ba1897-0a6b-3cb9-a57b-1a874bfa919b | -5.85434 | -42.85006 | 2025-10-11 03:19:00 | NPP-375D | SÃO PEDRO DO PIAUÍ | PIAUÍ | Brasil | 2210508 | 22 | 33 | nan | nan | nan | Caatinga | 28.7 |
| 436cfa80-f632-3122-b107-a0d144414bda | -7.36182 | -38.76234 | 2025-10-11 03:19:00 | NPP-375D | MAURITI | CEARÁ | Brasil | 2308104 | 23 | 33 | nan | nan | nan | Caatinga | 3.2 |
| b664bd9a-5fb2-3dcf-8f55-4303922f7966 | -5.85861 | -42.8593 | 2025-10-11 03:19:00 | NPP-375D | PALMEIRAIS | PIAUÍ | Brasil | 2207504 | 22 | 33 | nan | nan | nan | Caatinga | 39.1 |
| b30c4a9b-a112-38a4-9cab-7bc6b97067a4 | -8.19455 | -43.32925 | 2025-10-11 03:19:00 | NPP-375D | CANTO DO BURITI | PIAUÍ | Brasil | 2202307 | 22 | 33 | nan | nan | nan | Caatinga | 12.8 |
| 0545200c-dd23-319f-9db6-8ca7eb07ad1a | -8.49827 | -40.75632 | 2025-10-11 03:19:00 | NPP-375D | DORMENTES | PERNAMBUCO | Brasil | 2605152 | 26 | 33 | nan | nan | nan | Caatinga | 1.2 |
| a0fb53cd-9889-3098-836f-cd57312e03da | -8.20601 | -43.34621 | 2025-10-11 03:19:00 | NPP-375D | CANTO DO BURITI | PIAUÍ | Brasil | 2202307 | 22 | 33 | nan | nan | nan | Caatinga | 10.7 |
| 8842244b-cf9f-3810-8a25-f6ee75395346 | -4.45037 | -40.7728 | 2025-10-11 03:19:00 | NPP-375D | IPUEIRAS | CEARÁ | Brasil | 2305902 | 23 | 33 | nan | nan | nan | Caatinga | 1.2 |
| b970a1bf-5acb-393a-9898-b8f2b3213f58 | -8.67578 | -40.4208 | 2025-10-11 03:19:00 | NPP-375D | PETROLINA | PERNAMBUCO | Brasil | 2611101 | 26 | 33 | nan | nan | nan | Caatinga | 2.6 |
| cf72e980-1a4c-3547-899f-3641620e5c6a | -7.66539 | -42.57463 | 2025-10-11 03:19:00 | NPP-375D | SÃO JOSÉ DO PEIXE | PIAUÍ | Brasil | 2210102 | 22 | 33 | nan | nan | nan | Caatinga | 2.4 |
| 8059733e-4465-3526-9c85-be6f3a3ec8a1 | -13.2252 | -42.3414 | 2025-10-11 03:20:00 | GOES-19 | CATURAMA | BAHIA | Brasil | 2907558 | 29 | 33 | nan | nan | nan | Caatinga | 203.3 |
| 10c5c60f-0186-3828-a82d-ed5eb33edc82 | -13.2057 | -42.345 | 2025-10-11 03:20:00 | GOES-19 | CATURAMA | BAHIA | Brasil | 2907558 | 29 | 33 | nan | nan | nan | Caatinga | 150.5 |
| 693df0b7-d36b-3419-90af-f7fe642df44b | -5.8522 | -42.8372 | 2025-10-11 03:20:00 | GOES-19 | SÃO PEDRO DO PIAUÍ | PIAUÍ | Brasil | 2210508 | 22 | 33 | nan | nan | nan | Caatinga | 90.0 |
| 06bba5b2-8d69-33f8-a976-ee7ab4a25882 | -12.7371 | -48.6468 | 2025-10-11 03:20:00 | GOES-19 | JAÚ DO TOCANTINS | TOCANTINS | Brasil | 1711506 | 17 | 33 | nan | nan | nan | Cerrado | 50.4 |
| 3009a410-d577-3530-83d4-f5d2fb1b0b61 | -13.2257 | -42.317 | 2025-10-11 03:20:00 | GOES-19 | CATURAMA | BAHIA | Brasil | 2907558 | 29 | 33 | nan | nan | nan | Caatinga | 89.8 |
| 2bf6c0b2-555a-3a0d-915a-4ac85f1d09cc | -5.8708 | -42.8593 | 2025-10-11 03:20:00 | GOES-19 | PALMEIRAIS | PIAUÍ | Brasil | 2207504 | 22 | 33 | nan | nan | nan | Caatinga | 115.4 |
| 79688207-1eb4-3aa9-af1c-6b2f121f54c2 | -17.2722 | -46.8932 | 2025-10-11 03:20:00 | GOES-19 | PARACATU | MINAS GERAIS | Brasil | 3147006 | 31 | 33 | nan | nan | nan | Cerrado | 95.0 |
| f558d75c-3bdd-3364-a503-65344d1ea154 | -5.852 | -42.8608 | 2025-10-11 03:20:00 | GOES-19 | PALMEIRAIS | PIAUÍ | Brasil | 2207504 | 22 | 33 | nan | nan | nan | Caatinga | 105.6 |
| 6d5e5063-ae01-3c85-843c-babc761bd95f | -5.871 | -42.8357 | 2025-10-11 03:20:00 | GOES-19 | PALMEIRAIS | PIAUÍ | Brasil | 2207504 | 22 | 33 | nan | nan | nan | Caatinga | 90.4 |
| 9bb76fcd-02b4-3710-a477-b4bc443f8032 | -11.75882 | -43.32513 | 2025-10-11 03:21:00 | NPP-375D | IBOTIRAMA | BAHIA | Brasil | 2913200 | 29 | 33 | nan | nan | nan | Cerrado | 3.7 |
| 75955c1f-fdc4-3466-a7be-538df529d274 | -13.20587 | -42.33973 | 2025-10-11 03:21:00 | NPP-375D | CATURAMA | BAHIA | Brasil | 2907558 | 29 | 33 | nan | nan | nan | Caatinga | 3.2 |
| a46d3c21-74df-305b-8e71-ae6c71845aee | -16.59152 | -41.1111 | 2025-10-11 03:21:00 | NPP-375D | JEQUITINHONHA | MINAS GERAIS | Brasil | 3135803 | 31 | 33 | nan | nan | nan | Mata Atlântica | 1.5 |
| bbf724d2-fb54-36dc-bdbb-a9a2097f3d4f | -11.76031 | -43.32625 | 2025-10-11 03:21:00 | NPP-375D | IBOTIRAMA | BAHIA | Brasil | 2913200 | 29 | 33 | nan | nan | nan | Cerrado | 3.0 |
| d6038374-90dd-361e-aac6-aa83a87aa6dd | -11.75208 | -43.32361 | 2025-10-11 03:21:00 | NPP-375D | IBOTIRAMA | BAHIA | Brasil | 2913200 | 29 | 33 | nan | nan | nan | Cerrado | 3.7 |
| c805f335-602a-3527-986c-ff37315a7475 | -9.40084 | -42.67298 | 2025-10-11 03:21:00 | NPP-375D | FARTURA DO PIAUÍ | PIAUÍ | Brasil | 2203750 | 22 | 33 | nan | nan | nan | Caatinga | 3.6 |
| 7b4ee554-0a12-30e7-abfc-154da7f9c3cc | -11.91481 | -44.17581 | 2025-10-11 03:21:00 | NPP-375D | COTEGIPE | BAHIA | Brasil | 2909406 | 29 | 33 | nan | nan | nan | Cerrado | 6.7 |
| bd28aee2-d9a2-3761-8d26-97308a65c249 | -13.37469 | -44.34601 | 2025-10-11 03:21:00 | NPP-375D | SANTA MARIA DA VITÓRIA | BAHIA | Brasil | 2928109 | 29 | 33 | nan | nan | nan | Cerrado | 0.8 |
| 8c00f8d9-0d73-3a4c-8e3f-f945093c9414 | -11.76133 | -43.31281 | 2025-10-11 03:21:00 | NPP-375D | IBOTIRAMA | BAHIA | Brasil | 2913200 | 29 | 33 | nan | nan | nan | Cerrado | 1.5 |
| 027aec28-948d-3280-bd48-e479b3b951f9 | -11.44835 | -43.48481 | 2025-10-11 03:21:00 | NPP-375D | BARRA | BAHIA | Brasil | 2902708 | 29 | 33 | nan | nan | nan | Cerrado | 3.9 |
| 50df512f-0113-383f-bcf3-2b1bbd0f46f4 | -13.48689 | -42.01817 | 2025-10-11 03:21:00 | NPP-375D | ÉRICO CARDOSO | BAHIA | Brasil | 2900504 | 29 | 33 | nan | nan | nan | Caatinga | 0.6 |
| 2aac382d-bb02-3d82-8c31-87fc3be12702 | -13.21932 | -42.33746 | 2025-10-11 03:21:00 | NPP-375D | CATURAMA | BAHIA | Brasil | 2907558 | 29 | 33 | nan | nan | nan | Caatinga | 29.7 |
| 5c40391c-bb2e-3af3-a70c-5a4a8e60f2c1 | -14.96031 | -41.69206 | 2025-10-11 03:21:00 | NPP-375D | PIRIPÁ | BAHIA | Brasil | 2924702 | 29 | 33 | nan | nan | nan | Caatinga | 2.2 |
| 0cd8308a-fea8-33d2-9cba-022743c9ea4f | -15.10823 | -42.47105 | 2025-10-11 03:21:00 | NPP-375D | MONTEZUMA | MINAS GERAIS | Brasil | 3143450 | 31 | 33 | nan | nan | nan | Mata Atlântica | 1.3 |
| 83a0fc0a-cbcf-3746-be75-35bf1e4ecfda | -13.20382 | -42.34967 | 2025-10-11 03:21:00 | NPP-375D | CATURAMA | BAHIA | Brasil | 2907558 | 29 | 33 | nan | nan | nan | Caatinga | 6.5 |
| a243cbce-412b-3dad-9211-e2b76164a155 | -13.21537 | -42.34391 | 2025-10-11 03:21:00 | NPP-375D | CATURAMA | BAHIA | Brasil | 2907558 | 29 | 33 | nan | nan | nan | Caatinga | 51.5 |
| b674a0f0-ba5d-3862-8112-cdfa613b4184 | -16.36757 | -40.75526 | 2025-10-11 03:21:00 | NPP-375D | JEQUITINHONHA | MINAS GERAIS | Brasil | 3135803 | 31 | 33 | nan | nan | nan | Mata Atlântica | 1.3 |
| 9657671f-f7a1-31a6-8832-7c9940455fa0 | -13.21829 | -42.34249 | 2025-10-11 03:21:00 | NPP-375D | CATURAMA | BAHIA | Brasil | 2907558 | 29 | 33 | nan | nan | nan | Caatinga | 29.7 |
| ac85afdb-ccf9-3e79-aca3-608bb1dc741d | -14.96788 | -41.68468 | 2025-10-11 03:21:00 | NPP-375D | PIRIPÁ | BAHIA | Brasil | 2924702 | 29 | 33 | nan | nan | nan | Caatinga | 1.2 |
| a361afbc-84e0-3a2b-8237-e6c99e4696e8 | -10.87493 | -44.18959 | 2025-10-11 03:21:00 | NPP-375D | SANTA RITA DE CÁSSIA | BAHIA | Brasil | 2928406 | 29 | 33 | nan | nan | nan | Cerrado | 12.4 |
| cfc94c00-e27d-3d23-8c1e-5e9599b53986 | -16.37295 | -40.75616 | 2025-10-11 03:21:00 | NPP-375D | JEQUITINHONHA | MINAS GERAIS | Brasil | 3135803 | 31 | 33 | nan | nan | nan | Mata Atlântica | 1.0 |
| 9c547703-6dff-3027-8fd1-fa4949434304 | -11.7616 | -43.32012 | 2025-10-11 03:21:00 | NPP-375D | IBOTIRAMA | BAHIA | Brasil | 2913200 | 29 | 33 | nan | nan | nan | Cerrado | 1.8 |
| 840a4000-6d9a-3da0-b33f-277a1fde2b25 | -16.37088 | -40.75198 | 2025-10-11 03:21:00 | NPP-375D | JEQUITINHONHA | MINAS GERAIS | Brasil | 3135803 | 31 | 33 | nan | nan | nan | Mata Atlântica | 1.2 |
| c6283aaa-e1f0-3bb5-acb9-fef9c725f334 | -11.75617 | -43.31249 | 2025-10-11 03:21:00 | NPP-375D | IBOTIRAMA | BAHIA | Brasil | 2913200 | 29 | 33 | nan | nan | nan | Cerrado | 4.2 |
| 8e6eda2b-65d3-3b99-b7eb-73c1cd298b40 | -9.39977 | -42.67369 | 2025-10-11 03:21:00 | NPP-375D | FARTURA DO PIAUÍ | PIAUÍ | Brasil | 2203750 | 22 | 33 | nan | nan | nan | Caatinga | 4.5 |
| d99c9a14-1c8c-3749-9fd6-4bd6d6da87e5 | -13.22157 | -42.34531 | 2025-10-11 03:21:00 | NPP-375D | CATURAMA | BAHIA | Brasil | 2907558 | 29 | 33 | nan | nan | nan | Caatinga | 51.5 |
| 6c4accbe-afd3-36ca-8e7b-f9604703e3b6 | -11.91332 | -44.18278 | 2025-10-11 03:21:00 | NPP-375D | COTEGIPE | BAHIA | Brasil | 2909406 | 29 | 33 | nan | nan | nan | Cerrado | 6.7 |
| ce506aab-e271-3ada-a24e-286144408b8f | -11.75487 | -43.31863 | 2025-10-11 03:21:00 | NPP-375D | IBOTIRAMA | BAHIA | Brasil | 2913200 | 29 | 33 | nan | nan | nan | Cerrado | 4.2 |
| d6b4449c-fdaa-3aa5-9079-26359fc5bb9b | -13.49272 | -42.02063 | 2025-10-11 03:21:00 | NPP-375D | ÉRICO CARDOSO | BAHIA | Brasil | 2900504 | 29 | 33 | nan | nan | nan | Caatinga | 0.8 |
| ccca758f-2d52-371b-9d8b-3d1564e39a0b | -11.75358 | -43.32476 | 2025-10-11 03:21:00 | NPP-375D | IBOTIRAMA | BAHIA | Brasil | 2913200 | 29 | 33 | nan | nan | nan | Cerrado | 5.8 |
| aaad564d-7919-3bac-b876-5c685c169879 | -10.87343 | -44.19679 | 2025-10-11 03:21:00 | NPP-375D | SANTA RITA DE CÁSSIA | BAHIA | Brasil | 2928406 | 29 | 33 | nan | nan | nan | Cerrado | 14.5 |
| 59d509b5-383d-3940-88fe-a449e281379d | -13.22265 | -42.34025 | 2025-10-11 03:21:00 | NPP-375D | CATURAMA | BAHIA | Brasil | 2907558 | 29 | 33 | nan | nan | nan | Caatinga | 21.5 |
| 3dfc350a-83fd-3a1b-b069-258c02c85720 | -11.7629 | -43.31397 | 2025-10-11 03:21:00 | NPP-375D | IBOTIRAMA | BAHIA | Brasil | 2913200 | 29 | 33 | nan | nan | nan | Cerrado | 1.8 |
| bd756d8d-7043-3bdb-a9e5-859d7142898b | -14.96625 | -41.69257 | 2025-10-11 03:21:00 | NPP-375D | PIRIPÁ | BAHIA | Brasil | 2924702 | 29 | 33 | nan | nan | nan | Caatinga | 2.2 |
| 067a6fa4-70a4-3d78-9681-1576a4aa7470 | -13.21107 | -42.34603 | 2025-10-11 03:21:00 | NPP-375D | CATURAMA | BAHIA | Brasil | 2907558 | 29 | 33 | nan | nan | nan | Caatinga | 39.2 |
| 5de83786-bb2c-3608-aa6e-d7c34baf507b | -11.7546 | -43.3113 | 2025-10-11 03:21:00 | NPP-375D | IBOTIRAMA | BAHIA | Brasil | 2913200 | 29 | 33 | nan | nan | nan | Cerrado | 1.5 |
| f56b1007-ef31-3d0b-bf26-fd8b8c57832b | -16.59084 | -41.11444 | 2025-10-11 03:21:00 | NPP-375D | JEQUITINHONHA | MINAS GERAIS | Brasil | 3135803 | 31 | 33 | nan | nan | nan | Mata Atlântica | 1.5 |
| ee87c5a5-8694-35b8-8c4e-d06e8a497425 | -12.22316 | -43.79897 | 2025-10-11 03:21:00 | NPP-375D | MUQUÉM DO SÃO FRANCISCO | BAHIA | Brasil | 2922250 | 29 | 33 | nan | nan | nan | Cerrado | 2.5 |
| b7d1bfe1-6ef8-3033-8f08-604b47c0df96 | -13.20903 | -42.35594 | 2025-10-11 03:21:00 | NPP-375D | CATURAMA | BAHIA | Brasil | 2907558 | 29 | 33 | nan | nan | nan | Caatinga | 8.3 |
| 02b3d256-a560-3d8e-a12c-28f8af6337b3 | -13.21328 | -42.35374 | 2025-10-11 03:21:00 | NPP-375D | CATURAMA | BAHIA | Brasil | 2907558 | 29 | 33 | nan | nan | nan | Caatinga | 17.7 |
| 73ca836f-fa14-3487-91ab-349a1b1afd9c | -15.60362 | -42.67793 | 2025-10-11 03:21:00 | NPP-375D | RIO PARDO DE MINAS | MINAS GERAIS | Brasil | 3155603 | 31 | 33 | nan | nan | nan | Mata Atlântica | 3.2 |
| 5744339e-db31-3d7c-b8ac-21a1a62cb8fa | -13.21433 | -42.34882 | 2025-10-11 03:21:00 | NPP-375D | CATURAMA | BAHIA | Brasil | 2907558 | 29 | 33 | nan | nan | nan | Caatinga | 51.5 |
| ff7fccf1-30c5-32cc-a182-7874fea78d49 | -16.37373 | -40.75224 | 2025-10-11 03:21:00 | NPP-375D | JEQUITINHONHA | MINAS GERAIS | Brasil | 3135803 | 31 | 33 | nan | nan | nan | Mata Atlântica | 0.8 |
| dda8c2e1-1150-35f3-b69a-3833443304f1 | -12.70925 | -44.94229 | 2025-10-11 03:21:00 | NPP-375D | SÃO DESIDÉRIO | BAHIA | Brasil | 2928901 | 29 | 33 | nan | nan | nan | Cerrado | 1.9 |
| 9792a467-e03b-3a12-ac2d-c108d32639a7 | -16.59697 | -41.11217 | 2025-10-11 03:21:00 | NPP-375D | JEQUITINHONHA | MINAS GERAIS | Brasil | 3135803 | 31 | 33 | nan | nan | nan | Mata Atlântica | 1.5 |
| 0090b268-9d15-3ab1-8333-def42ad0d2f4 | -11.76007 | -43.31897 | 2025-10-11 03:21:00 | NPP-375D | IBOTIRAMA | BAHIA | Brasil | 2913200 | 29 | 33 | nan | nan | nan | Cerrado | 3.7 |
| bbd8ee80-6f86-370d-84e3-1b28a1aa3a6e | -12.71718 | -44.94346 | 2025-10-11 03:21:00 | NPP-375D | SÃO DESIDÉRIO | BAHIA | Brasil | 2928901 | 29 | 33 | nan | nan | nan | Cerrado | 1.6 |
| 5e0aebd6-7e84-334c-a9e6-3f536527ee92 | -14.9611 | -41.6882 | 2025-10-11 03:21:00 | NPP-375D | PIRIPÁ | BAHIA | Brasil | 2924702 | 29 | 33 | nan | nan | nan | Caatinga | 1.2 |
| d95577f0-51b5-3de7-9e2f-4c12bc1df6db | -13.21642 | -42.33897 | 2025-10-11 03:21:00 | NPP-375D | CATURAMA | BAHIA | Brasil | 2907558 | 29 | 33 | nan | nan | nan | Caatinga | 21.5 |
| beefad20-8528-3d4d-a63e-6bda9b08613c | -12.71646 | -44.94411 | 2025-10-11 03:21:00 | NPP-375D | SÃO DESIDÉRIO | BAHIA | Brasil | 2928901 | 29 | 33 | nan | nan | nan | Cerrado | 1.9 |
| 0eb1cafa-3284-35a9-b849-cccc76000823 | -11.75175 | -43.39442 | 2025-10-11 03:21:00 | NPP-375D | BARRA | BAHIA | Brasil | 2902708 | 29 | 33 | nan | nan | nan | Cerrado | 1.0 |
| cc24f708-9195-3010-a9d1-dc8c42fe6f42 | -13.21626 | -42.35236 | 2025-10-11 03:21:00 | NPP-375D | CATURAMA | BAHIA | Brasil | 2907558 | 29 | 33 | nan | nan | nan | Caatinga | 39.2 |
| 5eb01b30-8559-3411-999d-4d7a2e310747 | -11.91709 | -44.18574 | 2025-10-11 03:21:00 | NPP-375D | COTEGIPE | BAHIA | Brasil | 2909406 | 29 | 33 | nan | nan | nan | Cerrado | 7.9 |
| 85e7c817-558c-3596-9cfe-2cecdf47fdf9 | -13.21208 | -42.34112 | 2025-10-11 03:21:00 | NPP-375D | CATURAMA | BAHIA | Brasil | 2907558 | 29 | 33 | nan | nan | nan | Caatinga | 29.7 |
| 944ec548-7522-30c2-86af-493687c18d62 | -16.59626 | -41.11565 | 2025-10-11 03:21:00 | NPP-375D | JEQUITINHONHA | MINAS GERAIS | Brasil | 3135803 | 31 | 33 | nan | nan | nan | Mata Atlântica | 1.5 |
| 9d27a54f-ec47-3d3a-ac18-39b22bbd7378 | -13.2245 | -42.34383 | 2025-10-11 03:21:00 | NPP-375D | CATURAMA | BAHIA | Brasil | 2907558 | 29 | 33 | nan | nan | nan | Caatinga | 3.3 |
| 8934100e-657d-3645-871d-8713df033f99 | -11.91004 | -44.18415 | 2025-10-11 03:21:00 | NPP-375D | COTEGIPE | BAHIA | Brasil | 2909406 | 29 | 33 | nan | nan | nan | Cerrado | 7.9 |
| 06299728-39a8-37d5-9c47-b8b0cca9fe21 | -16.37007 | -40.75584 | 2025-10-11 03:21:00 | NPP-375D | JEQUITINHONHA | MINAS GERAIS | Brasil | 3135803 | 31 | 33 | nan | nan | nan | Mata Atlântica | 2.1 |
| 65e73b4a-997e-3d11-9ea5-42a4ad5a1f59 | -11.91149 | -44.17717 | 2025-10-11 03:21:00 | NPP-375D | COTEGIPE | BAHIA | Brasil | 2909406 | 29 | 33 | nan | nan | nan | Cerrado | 7.5 |
| 38fb1406-b47e-30d5-9bd8-2675f19c48bf | -14.9595 | -41.69597 | 2025-10-11 03:21:00 | NPP-375D | PIRIPÁ | BAHIA | Brasil | 2924702 | 29 | 33 | nan | nan | nan | Caatinga | 2.2 |
| d33fd248-4b3b-36fa-b79d-b6928d129605 | -13.21727 | -42.34745 | 2025-10-11 03:21:00 | NPP-375D | CATURAMA | BAHIA | Brasil | 2907558 | 29 | 33 | nan | nan | nan | Caatinga | 39.2 |
| 145518c4-9ed9-37cd-b162-10af9bac8f72 | -12.22448 | -43.79275 | 2025-10-11 03:21:00 | NPP-375D | MUQUÉM DO SÃO FRANCISCO | BAHIA | Brasil | 2922250 | 29 | 33 | nan | nan | nan | Cerrado | 2.5 |
| dc7e216a-1a7c-39c5-b270-043848bcc618 | -12.70996 | -44.94167 | 2025-10-11 03:21:00 | NPP-375D | SÃO DESIDÉRIO | BAHIA | Brasil | 2928901 | 29 | 33 | nan | nan | nan | Cerrado | 1.6 |
| 57c32a98-8a16-3d5a-9eeb-c78d82e0a329 | -13.20484 | -42.34472 | 2025-10-11 03:21:00 | NPP-375D | CATURAMA | BAHIA | Brasil | 2907558 | 29 | 33 | nan | nan | nan | Caatinga | 6.5 |


[Clique aqui para ver as próximas entradas](README7.md)
