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

## Dados Diários - Página 7

| ID | Latitude | Longitude | Data/Hora GMT | Satélite | Município | Estado | País | Município ID | Estado ID | País ID | Dias sem Chuva | Precipitação | Risco de Fogo | Bioma | FRP |
|----|----------|-----------|---------------|----------|-----------|--------|------|--------------|-----------|---------|----------------|--------------|----------------|-------|-----|
| 0bafd164-3010-3a14-8f10-eb42bf52ac18 | -7.37895 | -44.3535 | 2025-09-14 03:25:00 | NPP-375D | SEBASTIÃO LEAL | PIAUÍ | Brasil | 2210631 | 22 | 33 | nan | nan | nan | Cerrado | 3.0 |
| 03e99227-0f49-301d-85b4-ed8846ef22b5 | -5.79633 | -43.89614 | 2025-09-14 03:25:00 | NPP-375D | BURITI BRAVO | MARANHÃO | Brasil | 2102309 | 21 | 33 | nan | nan | nan | Cerrado | 2.4 |
| 1a945fc2-f323-34a9-8ffc-4a02bcc53510 | -8.08085 | -44.51479 | 2025-09-14 03:25:00 | NPP-375D | URUÇUÍ | PIAUÍ | Brasil | 2211209 | 22 | 33 | nan | nan | nan | Cerrado | 2.5 |
| 333f7df1-6e72-34f5-b1b7-5032afc2a4a5 | -6.17768 | -41.16084 | 2025-09-14 03:25:00 | NPP-375D | PIMENTEIRAS | PIAUÍ | Brasil | 2208106 | 22 | 33 | nan | nan | nan | Caatinga | 1.2 |
| 86187109-46af-3009-b818-316112ad1e0d | -6.539 | -39.51267 | 2025-09-14 03:25:00 | NPP-375D | CARIÚS | CEARÁ | Brasil | 2303303 | 23 | 33 | nan | nan | nan | Caatinga | 5.1 |
| 1d7d07fd-2c6a-3fab-af52-1858fb4d6d9c | -5.39851 | -40.34983 | 2025-09-14 03:25:00 | NPP-375D | INDEPENDÊNCIA | CEARÁ | Brasil | 2305605 | 23 | 33 | nan | nan | nan | Caatinga | 1.3 |
| ab2d9470-16e8-3b7e-8f40-9259da39891e | -8.62291 | -40.20053 | 2025-09-14 03:25:00 | NPP-375D | LAGOA GRANDE | PERNAMBUCO | Brasil | 2608750 | 26 | 33 | nan | nan | nan | Caatinga | 5.7 |
| a5bff9dd-2a4d-314f-b7d0-8aafda7f1ff0 | -5.67959 | -37.21745 | 2025-09-14 03:25:00 | NPP-375D | UPANEMA | RIO GRANDE DO NORTE | Brasil | 2414605 | 24 | 33 | nan | nan | nan | Caatinga | 1.6 |
| 2ebdcd4e-f2fa-3379-b6b6-7af212d30eb4 | -5.66188 | -37.21716 | 2025-09-14 03:25:00 | NPP-375D | UPANEMA | RIO GRANDE DO NORTE | Brasil | 2414605 | 24 | 33 | nan | nan | nan | Caatinga | 6.8 |
| 792d2498-3df8-3c5d-8c3d-3fa8abc08793 | -7.72238 | -44.85586 | 2025-09-14 03:25:00 | NPP-375D | URUÇUÍ | PIAUÍ | Brasil | 2211209 | 22 | 33 | nan | nan | nan | Cerrado | 4.5 |
| b5a1f20b-069b-3193-b887-b8d3c47669f6 | -6.42426 | -42.62072 | 2025-09-14 03:25:00 | NPP-375D | AMARANTE | PIAUÍ | Brasil | 2200509 | 22 | 33 | nan | nan | nan | Caatinga | 3.5 |
| a017e6ad-37a7-367c-ab67-6c08e353b5b1 | -6.75371 | -35.2226 | 2025-09-14 03:25:00 | NPP-375D | MAMANGUAPE | PARAÍBA | Brasil | 2508901 | 25 | 33 | nan | nan | nan | Caatinga | 1.4 |
| dd7f26e0-f8ce-3f4a-92ec-9c860feaf376 | -9.62592 | -40.62142 | 2025-09-14 03:25:00 | NPP-375D | JUAZEIRO | BAHIA | Brasil | 2918407 | 29 | 33 | nan | nan | nan | Caatinga | 13.6 |
| 123a5bd3-2107-3c60-a643-a5eeb1e675a2 | -6.17516 | -41.15333 | 2025-09-14 03:25:00 | NPP-375D | PIMENTEIRAS | PIAUÍ | Brasil | 2208106 | 22 | 33 | nan | nan | nan | Caatinga | 1.8 |
| fe532634-7fff-3186-8ac4-a50b9091fd79 | -6.18128 | -41.17529 | 2025-09-14 03:25:00 | NPP-375D | PIMENTEIRAS | PIAUÍ | Brasil | 2208106 | 22 | 33 | nan | nan | nan | Caatinga | 1.1 |
| fe011f26-13e9-3c28-97fa-58876dff7bd8 | -7.37468 | -44.33743 | 2025-09-14 03:25:00 | NPP-375D | SEBASTIÃO LEAL | PIAUÍ | Brasil | 2210631 | 22 | 33 | nan | nan | nan | Cerrado | 1.9 |
| 43e9010c-0118-3b88-a5b1-c0a2eec8d77c | -8.49143 | -44.72188 | 2025-09-14 03:25:00 | NPP-375D | PALMEIRA DO PIAUÍ | PIAUÍ | Brasil | 2207405 | 22 | 33 | nan | nan | nan | Cerrado | 1.0 |
| c7ddd23f-61d3-3709-8521-5891dcd7c83b | -8.13625 | -43.66553 | 2025-09-14 03:25:00 | NPP-375D | ELISEU MARTINS | PIAUÍ | Brasil | 2203602 | 22 | 33 | nan | nan | nan | Cerrado | 1.4 |
| ae29e72c-f5d6-3dba-b1d8-4883cd1b2d97 | -4.66129 | -37.46495 | 2025-09-14 03:25:00 | NPP-375D | ICAPUÍ | CEARÁ | Brasil | 2305357 | 23 | 33 | nan | nan | nan | Caatinga | 1.2 |
| 347231ea-3a5b-3459-bc30-8f634d537a42 | -5.39349 | -40.34486 | 2025-09-14 03:25:00 | NPP-375D | INDEPENDÊNCIA | CEARÁ | Brasil | 2305605 | 23 | 33 | nan | nan | nan | Caatinga | 0.6 |
| de44c92b-1a48-352c-bd6f-a3a9df75ba69 | -6.32941 | -43.88121 | 2025-09-14 03:25:00 | NPP-375D | PARAIBANO | MARANHÃO | Brasil | 2107704 | 21 | 33 | nan | nan | nan | Cerrado | 14.8 |
| 117e8d5f-a461-3d74-90cc-98934cd451f4 | -7.38292 | -44.35431 | 2025-09-14 03:25:00 | NPP-375D | SEBASTIÃO LEAL | PIAUÍ | Brasil | 2210631 | 22 | 33 | nan | nan | nan | Cerrado | 2.5 |
| 6c05e24d-d4fe-3cbd-bff1-c4c93a1685f0 | -7.72084 | -44.86388 | 2025-09-14 03:25:00 | NPP-375D | URUÇUÍ | PIAUÍ | Brasil | 2211209 | 22 | 33 | nan | nan | nan | Cerrado | 8.8 |
| 4e8fc325-aa58-3d22-88fe-a9df23f8672e | -5.95542 | -42.78415 | 2025-09-14 03:25:00 | NPP-375D | PALMEIRAIS | PIAUÍ | Brasil | 2207504 | 22 | 33 | nan | nan | nan | Caatinga | 3.3 |
| 9be81738-d372-36c6-a559-f350cf3d5f26 | -5.79054 | -43.8879 | 2025-09-14 03:25:00 | NPP-375D | BURITI BRAVO | MARANHÃO | Brasil | 2102309 | 21 | 33 | nan | nan | nan | Cerrado | 2.4 |
| 14d4b614-8e79-39e6-8ab2-869a75c5cb1a | -9.42738 | -40.31064 | 2025-09-14 03:25:00 | NPP-375D | JUAZEIRO | BAHIA | Brasil | 2918407 | 29 | 33 | nan | nan | nan | Caatinga | 3.1 |
| ffb5cb13-555b-3b36-a70f-5ecf90be0347 | -8.14298 | -43.66669 | 2025-09-14 03:25:00 | NPP-375D | ELISEU MARTINS | PIAUÍ | Brasil | 2203602 | 22 | 33 | nan | nan | nan | Cerrado | 1.4 |
| a140c558-238b-396a-93b7-f748d7a3089c | -5.06739 | -40.47277 | 2025-09-14 03:25:00 | NPP-375D | CRATEÚS | CEARÁ | Brasil | 2304103 | 23 | 33 | nan | nan | nan | Caatinga | 1.5 |
| 6a4a2223-21c4-36e8-b214-4587db7b0d24 | -6.33197 | -43.86717 | 2025-09-14 03:25:00 | NPP-375D | PARAIBANO | MARANHÃO | Brasil | 2107704 | 21 | 33 | nan | nan | nan | Cerrado | 7.9 |
| 654c4c55-1d06-31b1-8b55-ba7d00ca0855 | -9.43012 | -40.3117 | 2025-09-14 03:25:00 | NPP-375D | JUAZEIRO | BAHIA | Brasil | 2918407 | 29 | 33 | nan | nan | nan | Caatinga | 7.4 |
| df52f29b-c5f3-3b9c-b5c7-acbdebf7e4d9 | -7.30941 | -43.93415 | 2025-09-14 03:25:00 | NPP-375D | LANDRI SALES | PIAUÍ | Brasil | 2205607 | 22 | 33 | nan | nan | nan | Cerrado | 5.3 |
| 5e5bac5b-8eff-3f5b-a08c-943c916c512b | -9.42799 | -40.30732 | 2025-09-14 03:25:00 | NPP-375D | JUAZEIRO | BAHIA | Brasil | 2918407 | 29 | 33 | nan | nan | nan | Caatinga | 3.1 |
| 01139661-b2a9-3bd8-b157-f40ba61214a7 | -9.63132 | -40.62253 | 2025-09-14 03:25:00 | NPP-375D | JUAZEIRO | BAHIA | Brasil | 2918407 | 29 | 33 | nan | nan | nan | Caatinga | 49.3 |
| 3f722058-6933-36ec-a083-c108486b4e1b | -8.14117 | -43.66241 | 2025-09-14 03:25:00 | NPP-375D | ELISEU MARTINS | PIAUÍ | Brasil | 2203602 | 22 | 33 | nan | nan | nan | Cerrado | 1.7 |
| bf4bab35-00cb-3250-ad45-de13b92df742 | -6.17537 | -41.17399 | 2025-09-14 03:25:00 | NPP-375D | PIMENTEIRAS | PIAUÍ | Brasil | 2208106 | 22 | 33 | nan | nan | nan | Caatinga | 0.8 |
| ba75c892-0f54-3681-8fc5-d997b02317d3 | -7.30815 | -43.94075 | 2025-09-14 03:25:00 | NPP-375D | LANDRI SALES | PIAUÍ | Brasil | 2205607 | 22 | 33 | nan | nan | nan | Cerrado | 5.3 |
| 56cc8229-1509-3b9e-bd78-a6488ae55253 | -7.37739 | -44.34517 | 2025-09-14 03:25:00 | NPP-375D | SEBASTIÃO LEAL | PIAUÍ | Brasil | 2210631 | 22 | 33 | nan | nan | nan | Cerrado | 2.5 |
| edd44ed1-20bf-3b3b-bce5-5c4365f33ed1 | -9.43074 | -40.30839 | 2025-09-14 03:25:00 | NPP-375D | JUAZEIRO | BAHIA | Brasil | 2918407 | 29 | 33 | nan | nan | nan | Caatinga | 7.4 |
| 2840a249-c39e-3151-9d35-2fbc03196e72 | -6.17614 | -41.16959 | 2025-09-14 03:25:00 | NPP-375D | PIMENTEIRAS | PIAUÍ | Brasil | 2208106 | 22 | 33 | nan | nan | nan | Caatinga | 0.8 |
| 40e1b258-1d80-30b3-a2ed-22e8446c744a | -9.43271 | -40.31168 | 2025-09-14 03:25:00 | NPP-375D | JUAZEIRO | BAHIA | Brasil | 2918407 | 29 | 33 | nan | nan | nan | Caatinga | 3.7 |
| d40fb5d8-3742-3126-a1ed-a52c67a83285 | -7.37333 | -44.34454 | 2025-09-14 03:25:00 | NPP-375D | SEBASTIÃO LEAL | PIAUÍ | Brasil | 2210631 | 22 | 33 | nan | nan | nan | Cerrado | 1.9 |
| ad4767b6-f0cb-30d3-a17e-71bc536dabea | -7.37756 | -44.36082 | 2025-09-14 03:25:00 | NPP-375D | URUÇUÍ | PIAUÍ | Brasil | 2211209 | 22 | 33 | nan | nan | nan | Cerrado | 3.0 |
| 2178a715-ffcf-3c9e-94d6-0a69676e267c | -5.66108 | -37.22195 | 2025-09-14 03:25:00 | NPP-375D | UPANEMA | RIO GRANDE DO NORTE | Brasil | 2414605 | 24 | 33 | nan | nan | nan | Caatinga | 6.8 |
| 3de4bad0-a8d2-372a-bbfc-d3048cd9c136 | -8.50044 | -44.72888 | 2025-09-14 03:25:00 | NPP-375D | PALMEIRA DO PIAUÍ | PIAUÍ | Brasil | 2207405 | 22 | 33 | nan | nan | nan | Cerrado | 1.5 |
| 81417d31-e735-3d96-8a8d-db119c15b686 | -9.0204 | -40.34773 | 2025-09-14 03:25:00 | NPP-375D | PETROLINA | PERNAMBUCO | Brasil | 2611101 | 26 | 33 | nan | nan | nan | Caatinga | 0.7 |
| 4a264cbf-2c16-3137-8ed9-12520ec32e61 | -6.33546 | -43.87375 | 2025-09-14 03:25:00 | NPP-375D | PARAIBANO | MARANHÃO | Brasil | 2107704 | 21 | 33 | nan | nan | nan | Cerrado | 13.6 |
| 199b3051-6565-3746-8833-90685f1a954a | -8.08927 | -44.50921 | 2025-09-14 03:25:00 | NPP-375D | URUÇUÍ | PIAUÍ | Brasil | 2211209 | 22 | 33 | nan | nan | nan | Cerrado | 2.7 |
| 37bfeeb5-8833-3920-859b-903242b0bdab | -6.53367 | -39.51183 | 2025-09-14 03:25:00 | NPP-375D | CARIÚS | CEARÁ | Brasil | 2303303 | 23 | 33 | nan | nan | nan | Caatinga | 5.1 |
| 5dea75d0-a40b-3b57-b9c3-c545d1badc85 | -5.79764 | -43.88891 | 2025-09-14 03:25:00 | NPP-375D | BURITI BRAVO | MARANHÃO | Brasil | 2102309 | 21 | 33 | nan | nan | nan | Cerrado | 2.4 |
| 1539b605-acfd-3865-a40c-3937b597136e | -7.37446 | -44.3601 | 2025-09-14 03:25:00 | NPP-375D | URUÇUÍ | PIAUÍ | Brasil | 2211209 | 22 | 33 | nan | nan | nan | Cerrado | 2.8 |
| a24b4583-f6f4-3caa-93e4-50b744ca8448 | -8.08526 | -44.51041 | 2025-09-14 03:25:00 | NPP-375D | URUÇUÍ | PIAUÍ | Brasil | 2211209 | 22 | 33 | nan | nan | nan | Cerrado | 3.5 |
| ab74a3f4-d708-30ac-a975-b853f4a3b22d | -9.01502 | -40.34674 | 2025-09-14 03:25:00 | NPP-375D | PETROLINA | PERNAMBUCO | Brasil | 2611101 | 26 | 33 | nan | nan | nan | Caatinga | 0.7 |
| ab5a3aeb-9372-3e2a-8bd7-fee6e72e0d3a | -7.31636 | -43.93521 | 2025-09-14 03:25:00 | NPP-375D | LANDRI SALES | PIAUÍ | Brasil | 2205607 | 22 | 33 | nan | nan | nan | Cerrado | 1.4 |
| 68e6d545-9bcf-3592-9c8c-d09bf4694824 | -6.17437 | -41.15766 | 2025-09-14 03:25:00 | NPP-375D | PIMENTEIRAS | PIAUÍ | Brasil | 2208106 | 22 | 33 | nan | nan | nan | Caatinga | 1.5 |
| 5f4b03c9-8fcc-3bec-9b8f-ff9810d21504 | -6.75768 | -35.22327 | 2025-09-14 03:25:00 | NPP-375D | MAMANGUAPE | PARAÍBA | Brasil | 2508901 | 25 | 33 | nan | nan | nan | Caatinga | 1.4 |
| cbe6443d-486f-30b1-9da1-99d522cd40fc | -6.53424 | -39.50856 | 2025-09-14 03:25:00 | NPP-375D | CARIÚS | CEARÁ | Brasil | 2303303 | 23 | 33 | nan | nan | nan | Caatinga | 6.6 |
| 09ad90e3-e699-3025-82f6-dc1c9a3861c6 | -7.30686 | -43.94752 | 2025-09-14 03:25:00 | NPP-375D | LANDRI SALES | PIAUÍ | Brasil | 2205607 | 22 | 33 | nan | nan | nan | Cerrado | 11.5 |
| dafa2da7-0e70-32ce-bf46-a8177434bdbd | -8.62353 | -40.19718 | 2025-09-14 03:25:00 | NPP-375D | LAGOA GRANDE | PERNAMBUCO | Brasil | 2608750 | 26 | 33 | nan | nan | nan | Caatinga | 4.5 |
| 6435ec11-2a7d-3bd5-bcd0-ce9fa7518c26 | -5.68037 | -37.22023 | 2025-09-14 03:25:00 | NPP-375D | UPANEMA | RIO GRANDE DO NORTE | Brasil | 2414605 | 24 | 33 | nan | nan | nan | Caatinga | 1.2 |
| 6ca633ec-534d-3fe1-8851-6723dcbcbb1c | -5.6665 | -37.21794 | 2025-09-14 03:25:00 | NPP-375D | UPANEMA | RIO GRANDE DO NORTE | Brasil | 2414605 | 24 | 33 | nan | nan | nan | Caatinga | 2.7 |
| 5c7e774c-a558-35ed-b9c1-bad92366e620 | -9.63199 | -40.61899 | 2025-09-14 03:25:00 | NPP-375D | JUAZEIRO | BAHIA | Brasil | 2918407 | 29 | 33 | nan | nan | nan | Caatinga | 33.3 |
| f5741bba-63e3-3610-8eb2-23f8643a8ab5 | -7.11117 | -36.48917 | 2025-09-14 03:25:00 | NPP-375D | JUAZEIRINHO | PARAÍBA | Brasil | 2507705 | 25 | 33 | nan | nan | nan | Caatinga | 4.1 |
| 3c536ddd-b802-3d4a-af7f-4d8ea2b43d69 | -8.08402 | -44.51685 | 2025-09-14 03:25:00 | NPP-375D | URUÇUÍ | PIAUÍ | Brasil | 2211209 | 22 | 33 | nan | nan | nan | Cerrado | 2.9 |
| b6b14bed-64a1-3717-82ec-663dd0a45db8 | -7.06737 | -38.54374 | 2025-09-14 03:25:00 | NPP-375D | SÃO JOSÉ DE PIRANHAS | PARAÍBA | Brasil | 2514503 | 25 | 33 | nan | nan | nan | Caatinga | 2.8 |
| 39d22373-0cce-3b6c-bbee-4bb24842ca70 | -11.24964 | -44.774 | 2025-09-14 03:28:00 | NPP-375D | SANTA RITA DE CÁSSIA | BAHIA | Brasil | 2928406 | 29 | 33 | nan | nan | nan | Cerrado | 4.7 |
| dd0b4798-f65e-32b2-8e4d-9474ec9f6a2c | -16.28355 | -45.68744 | 2025-09-14 03:28:00 | NPP-375D | SÃO ROMÃO | MINAS GERAIS | Brasil | 3164209 | 31 | 33 | nan | nan | nan | Cerrado | 3.1 |
| d7a3a677-f3ea-3c53-8676-7e58b4ec3c60 | -10.60026 | -44.33276 | 2025-09-14 03:28:00 | NPP-375D | SANTA RITA DE CÁSSIA | BAHIA | Brasil | 2928406 | 29 | 33 | nan | nan | nan | Cerrado | 10.5 |
| 46783794-c1c9-3161-bae9-877a69f3da10 | -14.63603 | -46.37053 | 2025-09-14 03:28:00 | NPP-375D | SÍTIO D'ABADIA | GOIÁS | Brasil | 5220702 | 52 | 33 | nan | nan | nan | Cerrado | 3.4 |
| 44936df1-e7c3-3fca-a87d-d4534c769a07 | -17.69568 | -42.5588 | 2025-09-14 03:28:00 | NPP-375D | CAPELINHA | MINAS GERAIS | Brasil | 3112307 | 31 | 33 | nan | nan | nan | Mata Atlântica | 5.5 |
| c8c20d9a-d4b0-33af-94e1-d462f2fb1e2f | -14.98905 | -42.23935 | 2025-09-14 03:28:00 | NPP-375D | MORTUGABA | BAHIA | Brasil | 2921807 | 29 | 33 | nan | nan | nan | Caatinga | 1.2 |
| e85a0f2e-6a4a-3048-87dc-07765de6d556 | -10.59547 | -44.34346 | 2025-09-14 03:28:00 | NPP-375D | SANTA RITA DE CÁSSIA | BAHIA | Brasil | 2928406 | 29 | 33 | nan | nan | nan | Cerrado | 7.3 |
| 311343f6-9ff4-3c87-a42f-91cc9ad700b4 | -17.35685 | -42.62434 | 2025-09-14 03:28:00 | NPP-375D | MINAS NOVAS | MINAS GERAIS | Brasil | 3141801 | 31 | 33 | nan | nan | nan | Cerrado | 1.6 |
| fd562332-9471-3f85-b4af-8a6ef5bf61df | -14.31939 | -46.09821 | 2025-09-14 03:28:00 | NPP-375D | MAMBAÍ | GOIÁS | Brasil | 5212709 | 52 | 33 | nan | nan | nan | Cerrado | 2.9 |
| 3a7e2234-1785-33db-9108-30f6f90af5bf | -13.9311 | -44.84235 | 2025-09-14 03:28:00 | NPP-375D | COCOS | BAHIA | Brasil | 2908101 | 29 | 33 | nan | nan | nan | Cerrado | 3.2 |
| d8e6e734-aff2-32a1-995c-bb8fedbf7cc7 | -17.58908 | -42.73756 | 2025-09-14 03:28:00 | NPP-375D | VEREDINHA | MINAS GERAIS | Brasil | 3171071 | 31 | 33 | nan | nan | nan | Cerrado | 2.2 |
| db596fe8-f3b5-39bf-95b4-22511d0da430 | -14.20227 | -46.17412 | 2025-09-14 03:28:00 | NPP-375D | POSSE | GOIÁS | Brasil | 5218300 | 52 | 33 | nan | nan | nan | Cerrado | 1.6 |
| a822139f-293b-3135-87ea-240da26874b4 | -16.18691 | -43.13362 | 2025-09-14 03:28:00 | NPP-375D | RIACHO DOS MACHADOS | MINAS GERAIS | Brasil | 3154507 | 31 | 33 | nan | nan | nan | Cerrado | 3.8 |
| c1992b22-4d3c-3dcb-b162-b22518c13bbc | -10.59671 | -44.33721 | 2025-09-14 03:28:00 | NPP-375D | SANTA RITA DE CÁSSIA | BAHIA | Brasil | 2928406 | 29 | 33 | nan | nan | nan | Cerrado | 7.3 |
| f997399e-390e-3d5e-935b-611ac53c9815 | -14.98801 | -42.24202 | 2025-09-14 03:28:00 | NPP-375D | MORTUGABA | BAHIA | Brasil | 2921807 | 29 | 33 | nan | nan | nan | Caatinga | 1.3 |
| b8aea7ef-13db-31bf-95fa-c1fdc3cb38a8 | -13.93231 | -44.83658 | 2025-09-14 03:28:00 | NPP-375D | COCOS | BAHIA | Brasil | 2908101 | 29 | 33 | nan | nan | nan | Cerrado | 3.2 |
| e5ffd657-81bb-366e-9c31-a0bdbbf63246 | -10.75635 | -44.7854 | 2025-09-14 03:28:00 | NPP-375D | SEBASTIÃO BARROS | PIAUÍ | Brasil | 2210623 | 22 | 33 | nan | nan | nan | Cerrado | 8.2 |
| c3fa66b2-51b0-3edb-98ab-34e9df509472 | -11.24386 | -44.76942 | 2025-09-14 03:28:00 | NPP-375D | SANTA RITA DE CÁSSIA | BAHIA | Brasil | 2928406 | 29 | 33 | nan | nan | nan | Cerrado | 2.6 |
| 1b2d6c89-f1b8-343e-9c3c-fc83520e7e37 | -13.93633 | -44.8499 | 2025-09-14 03:28:00 | NPP-375D | COCOS | BAHIA | Brasil | 2908101 | 29 | 33 | nan | nan | nan | Cerrado | 5.2 |
| a11846e3-d546-3d59-93a9-32a139594ff0 | -13.9336 | -44.85643 | 2025-09-14 03:28:00 | NPP-375D | COCOS | BAHIA | Brasil | 2908101 | 29 | 33 | nan | nan | nan | Cerrado | 4.5 |
| 4eb0c12b-576b-34ff-955b-26a18fbe17bf | -15.436 | -47.34736 | 2025-09-14 03:28:00 | NPP-375D | FORMOSA | GOIÁS | Brasil | 5208004 | 52 | 33 | nan | nan | nan | Cerrado | 2.0 |
| 2aa862b1-7ae0-320b-b9f0-ebc6131ed780 | -11.44085 | -43.55991 | 2025-09-14 03:28:00 | NPP-375D | BARRA | BAHIA | Brasil | 2902708 | 29 | 33 | nan | nan | nan | Cerrado | 2.7 |
| 5e7a1958-c60b-3e52-b96b-3edc6e60dc48 | -13.38914 | -41.40111 | 2025-09-14 03:28:00 | NPP-375D | IBICOARA | BAHIA | Brasil | 2912202 | 29 | 33 | nan | nan | nan | Caatinga | 1.4 |
| 671323bd-ff42-3fac-a051-6047420035d3 | -14.20403 | -46.33227 | 2025-09-14 03:28:00 | NPP-375D | POSSE | GOIÁS | Brasil | 5218300 | 52 | 33 | nan | nan | nan | Cerrado | 6.9 |
| 0c7345c3-f824-3fdd-be1a-4a6f7ae42528 | -16.18773 | -43.12967 | 2025-09-14 03:28:00 | NPP-375D | RIACHO DOS MACHADOS | MINAS GERAIS | Brasil | 3154507 | 31 | 33 | nan | nan | nan | Cerrado | 1.7 |
| 46f87879-032e-370c-9735-b5c777a299a9 | -13.93472 | -44.82502 | 2025-09-14 03:28:00 | NPP-375D | COCOS | BAHIA | Brasil | 2908101 | 29 | 33 | nan | nan | nan | Cerrado | 3.3 |
| e14d7193-563a-3f65-bee8-f8fc0f7687ec | -13.92865 | -44.85405 | 2025-09-14 03:28:00 | NPP-375D | COCOS | BAHIA | Brasil | 2908101 | 29 | 33 | nan | nan | nan | Cerrado | 5.2 |
| c8d79fa5-298f-3576-8847-da32dc91bd5a | -11.45237 | -43.56792 | 2025-09-14 03:28:00 | NPP-375D | BARRA | BAHIA | Brasil | 2902708 | 29 | 33 | nan | nan | nan | Cerrado | 2.1 |
| 0dc29966-54a4-30e8-bc7f-af2c33f4c82a | -14.16026 | -46.24695 | 2025-09-14 03:28:00 | NPP-375D | POSSE | GOIÁS | Brasil | 5218300 | 52 | 33 | nan | nan | nan | Cerrado | 1.4 |
| e29b07fc-3fbf-3ac7-9f18-52d3f12a3e3e | -15.63778 | -44.38098 | 2025-09-14 03:28:00 | NPP-375D | PEDRAS DE MARIA DA CRUZ | MINAS GERAIS | Brasil | 3149150 | 31 | 33 | nan | nan | nan | Cerrado | 1.3 |
| 14ec9ee6-02fd-34fa-94ea-d6ed25c94280 | -13.92964 | -44.84319 | 2025-09-14 03:28:00 | NPP-375D | COCOS | BAHIA | Brasil | 2908101 | 29 | 33 | nan | nan | nan | Cerrado | 4.5 |
| b00b5d60-01f5-3e58-9e90-88c668b4841f | -14.18295 | -46.16232 | 2025-09-14 03:28:00 | NPP-375D | POSSE | GOIÁS | Brasil | 5218300 | 52 | 33 | nan | nan | nan | Cerrado | 1.6 |
| 7ebc7de5-1e10-3437-a8bd-b4137d89fa94 | -13.93862 | -44.83314 | 2025-09-14 03:28:00 | NPP-375D | COCOS | BAHIA | Brasil | 2908101 | 29 | 33 | nan | nan | nan | Cerrado | 3.4 |
| a52f45eb-062d-3e85-b901-68f3f937448c | -15.47322 | -47.32153 | 2025-09-14 03:28:00 | NPP-375D | FORMOSA | GOIÁS | Brasil | 5208004 | 52 | 33 | nan | nan | nan | Cerrado | 5.0 |
| 83ad8e3f-4d03-37ad-b82a-449e998c791f | -16.91566 | -39.44042 | 2025-09-14 03:28:00 | NPP-375D | PRADO | BAHIA | Brasil | 2925501 | 29 | 33 | nan | nan | nan | Mata Atlântica | 1.2 |
| b0190a7b-16eb-36e8-b23d-463644d00c19 | -11.24287 | -44.7725 | 2025-09-14 03:28:00 | NPP-375D | SANTA RITA DE CÁSSIA | BAHIA | Brasil | 2928406 | 29 | 33 | nan | nan | nan | Cerrado | 4.7 |


[Clique aqui para ver as próximas entradas](README8.md)
