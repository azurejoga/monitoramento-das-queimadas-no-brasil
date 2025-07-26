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

## Dados Diários - Página 32

| ID | Latitude | Longitude | Data/Hora GMT | Satélite | Município | Estado | País | Município ID | Estado ID | País ID | Dias sem Chuva | Precipitação | Risco de Fogo | Bioma | FRP |
|----|----------|-----------|---------------|----------|-----------|--------|------|--------------|-----------|---------|----------------|--------------|----------------|-------|-----|
| 431b6566-a912-3c68-90e9-945f93608990 | -11.06076 | -46.1221 | 2025-07-26 12:12:00 | TERRA_M-T | FORMOSA DO RIO PRETO | BAHIA | Brasil | 2911105 | 29 | 33 | nan | nan | nan | Cerrado | 9.2 |
| 68480607-620b-3c78-b9c1-888708d78ca1 | -6.77109 | -43.69246 | 2025-07-26 12:12:00 | TERRA_M-T | GUADALUPE | PIAUÍ | Brasil | 2204501 | 22 | 33 | nan | nan | nan | Cerrado | 6.1 |
| 71619f8f-cfd2-3cc8-a1cc-559281fc5dfe | -6.86564 | -43.67605 | 2025-07-26 12:12:00 | TERRA_M-T | GUADALUPE | PIAUÍ | Brasil | 2204501 | 22 | 33 | nan | nan | nan | Cerrado | 22.9 |
| 37fc7a03-83a0-3880-bcef-e8de67db33e7 | -6.99058 | -47.08018 | 2025-07-26 12:12:00 | TERRA_M-T | ESTREITO | MARANHÃO | Brasil | 2104057 | 21 | 33 | nan | nan | nan | Cerrado | 11.9 |
| c8aacb18-189a-3d81-a94b-dc37715e8b90 | -7.79126 | -44.5498 | 2025-07-26 12:12:00 | TERRA_M-T | URUÇUÍ | PIAUÍ | Brasil | 2211209 | 22 | 33 | nan | nan | nan | Cerrado | 43.9 |
| 32117033-acdd-3066-aa5e-eb2b742db398 | -11.56935 | -44.85289 | 2025-07-26 12:12:00 | TERRA_M-T | RIACHÃO DAS NEVES | BAHIA | Brasil | 2926202 | 29 | 33 | nan | nan | nan | Cerrado | 48.1 |
| 6ac043c5-fcbc-3d29-a13f-2756af45d6e5 | -11.57816 | -44.85416 | 2025-07-26 12:12:00 | TERRA_M-T | RIACHÃO DAS NEVES | BAHIA | Brasil | 2926202 | 29 | 33 | nan | nan | nan | Cerrado | 7.6 |
| 6f39669c-b365-3bb2-b13d-b5cab903fa1d | -13.13603 | -41.08242 | 2025-07-26 12:12:00 | TERRA_M-T | ITAETÉ | BAHIA | Brasil | 2915007 | 29 | 33 | nan | nan | nan | Caatinga | 10.8 |
| ac730785-7379-381a-85c1-f1109459ad5a | -8.69598 | -40.63704 | 2025-07-26 12:12:00 | TERRA_M-T | PETROLINA | PERNAMBUCO | Brasil | 2611101 | 26 | 33 | nan | nan | nan | Caatinga | 16.0 |
| 2982a524-e03a-37a1-8e4b-c3d43e346efa | -6.98823 | -43.33578 | 2025-07-26 12:12:00 | TERRA_M-T | JERUMENHA | PIAUÍ | Brasil | 2205300 | 22 | 33 | nan | nan | nan | Caatinga | 5.9 |
| 34444085-de81-35b6-b7bc-05f1796d8555 | -6.76861 | -45.23523 | 2025-07-26 12:12:00 | TERRA_M-T | MIRADOR | MARANHÃO | Brasil | 2106706 | 21 | 33 | nan | nan | nan | Cerrado | 6.9 |
| b2078533-16b7-36b1-8219-38a4820b3278 | -6.6762 | -43.96096 | 2025-07-26 12:12:00 | TERRA_M-T | NOVA IORQUE | MARANHÃO | Brasil | 2107308 | 21 | 33 | nan | nan | nan | Cerrado | 18.0 |
| 1d539f5c-5ccc-33b4-b5aa-c599c4205dad | -9.03906 | -45.36721 | 2025-07-26 12:12:00 | TERRA_M-T | BAIXA GRANDE DO RIBEIRO | PIAUÍ | Brasil | 2201150 | 22 | 33 | nan | nan | nan | Cerrado | 8.3 |
| ea0bb0e6-2cc4-3d6b-b399-7b9d838a6d4f | -7.24653 | -43.07037 | 2025-07-26 12:12:00 | TERRA_M-T | FLORIANO | PIAUÍ | Brasil | 2203909 | 22 | 33 | nan | nan | nan | Caatinga | 22.5 |
| 44fded54-8e2f-3195-b753-1ab8f27b5cb4 | -6.8707 | -43.51386 | 2025-07-26 12:12:00 | TERRA_M-T | JERUMENHA | PIAUÍ | Brasil | 2205300 | 22 | 33 | nan | nan | nan | Cerrado | 7.2 |
| 5709e1e9-666e-3535-9735-709f82bf098b | -7.58981 | -45.36335 | 2025-07-26 12:12:00 | TERRA_M-T | LORETO | MARANHÃO | Brasil | 2106102 | 21 | 33 | nan | nan | nan | Cerrado | 6.6 |
| 7bc05023-405b-358f-9405-f5470bf4bd7c | -6.05727 | -42.93639 | 2025-07-26 12:12:00 | TERRA_M-T | PALMEIRAIS | PIAUÍ | Brasil | 2207504 | 22 | 33 | nan | nan | nan | Caatinga | 5.0 |
| bc752b50-dd12-37ef-abe3-aa74fc40bd71 | -6.88927 | -43.11658 | 2025-07-26 12:12:00 | TERRA_M-T | FLORIANO | PIAUÍ | Brasil | 2203909 | 22 | 33 | nan | nan | nan | Cerrado | 13.7 |
| c62a2341-56a9-372f-a923-68e27f2caac8 | -6.66613 | -43.96853 | 2025-07-26 12:12:00 | TERRA_M-T | NOVA IORQUE | MARANHÃO | Brasil | 2107308 | 21 | 33 | nan | nan | nan | Cerrado | 4.4 |
| ad7e27db-af48-3d42-b5cf-f92c415aad59 | -7.79254 | -44.54097 | 2025-07-26 12:12:00 | TERRA_M-T | URUÇUÍ | PIAUÍ | Brasil | 2211209 | 22 | 33 | nan | nan | nan | Cerrado | 10.0 |
| 7c294f7c-dc9b-3c7c-bd81-9e478017a880 | -13.09571 | -47.33706 | 2025-07-26 12:12:00 | TERRA_M-T | ARRAIAS | TOCANTINS | Brasil | 1702406 | 17 | 33 | nan | nan | nan | Cerrado | 25.7 |
| 9c313037-23dd-3c14-994c-1a2f5501d667 | -12.66188 | -45.26835 | 2025-07-26 12:12:00 | TERRA_M-T | SÃO DESIDÉRIO | BAHIA | Brasil | 2928901 | 29 | 33 | nan | nan | nan | Cerrado | 38.2 |
| 0f30071e-922c-3cb5-95ec-c53e73b1d0f3 | -6.131 | -42.54467 | 2025-07-26 12:12:00 | TERRA_M-T | JARDIM DO MULATO | PIAUÍ | Brasil | 2205250 | 22 | 33 | nan | nan | nan | Caatinga | 7.3 |
| f533dbb5-c884-3ef4-bdd2-df0cf19d51b2 | -7.89577 | -44.73044 | 2025-07-26 12:12:00 | TERRA_M-T | URUÇUÍ | PIAUÍ | Brasil | 2211209 | 22 | 33 | nan | nan | nan | Cerrado | 6.7 |
| 4ddf6ea6-0ec8-38cf-91d5-8ea55e0432d5 | -10.66941 | -46.641 | 2025-07-26 12:12:00 | TERRA_M-T | MATEIROS | TOCANTINS | Brasil | 1712702 | 17 | 33 | nan | nan | nan | Cerrado | 7.2 |
| cf1628a4-97c7-34b2-9f1e-905fc7c4d69f | -12.67068 | -45.26963 | 2025-07-26 12:12:00 | TERRA_M-T | SÃO DESIDÉRIO | BAHIA | Brasil | 2928901 | 29 | 33 | nan | nan | nan | Cerrado | 8.6 |
| aceb2af9-c0f7-3d28-af86-532b1d585c3c | -10.62077 | -44.76691 | 2025-07-26 12:12:00 | TERRA_M-T | SEBASTIÃO BARROS | PIAUÍ | Brasil | 2210623 | 22 | 33 | nan | nan | nan | Cerrado | 11.1 |
| d68187f7-8f02-3065-9d4a-72f40d74d979 | -9.87537 | -44.6921 | 2025-07-26 12:12:00 | TERRA_M-T | RIACHO FRIO | PIAUÍ | Brasil | 2208858 | 22 | 33 | nan | nan | nan | Cerrado | 6.1 |
| 925117c0-f61a-3a80-8119-6f9adfd8d203 | -6.87446 | -43.6773 | 2025-07-26 12:12:00 | TERRA_M-T | GUADALUPE | PIAUÍ | Brasil | 2204501 | 22 | 33 | nan | nan | nan | Cerrado | 13.4 |
| e5647992-a253-3ed0-a4be-d8ac999c6c4e | -5.82093 | -44.5823 | 2025-07-26 12:12:00 | TERRA_M-T | TUNTUM | MARANHÃO | Brasil | 2112308 | 21 | 33 | nan | nan | nan | Cerrado | 14.4 |
| 7556594e-8a1e-3baa-ac4e-9536ea231911 | -6.55101 | -45.58747 | 2025-07-26 12:12:00 | TERRA_M-T | MIRADOR | MARANHÃO | Brasil | 2106706 | 21 | 33 | nan | nan | nan | Cerrado | 8.8 |
| e569d7ba-901b-3eed-9088-8a82e806b0a4 | -5.74238 | -43.97378 | 2025-07-26 12:12:00 | TERRA_M-T | BURITI BRAVO | MARANHÃO | Brasil | 2102309 | 21 | 33 | nan | nan | nan | Cerrado | 5.6 |
| 704421c6-89d1-33d6-a6cb-c53382bc8dd1 | -13.24294 | -40.59546 | 2025-07-26 12:12:00 | TERRA_M-T | MARACÁS | BAHIA | Brasil | 2920502 | 29 | 33 | nan | nan | nan | Caatinga | 10.2 |
| 04e52a16-4eb4-38db-b403-23f1e4e798b1 | -6.72517 | -45.40691 | 2025-07-26 12:12:00 | TERRA_M-T | MIRADOR | MARANHÃO | Brasil | 2106706 | 21 | 33 | nan | nan | nan | Cerrado | 8.5 |
| 0fc61d9f-165c-351f-a20b-9b50eccb95ca | -12.66059 | -45.27732 | 2025-07-26 12:12:00 | TERRA_M-T | SÃO DESIDÉRIO | BAHIA | Brasil | 2928901 | 29 | 33 | nan | nan | nan | Cerrado | 11.9 |
| 13ef954c-de1f-3da9-b3ae-9530a7adf560 | -7.28622 | -44.66356 | 2025-07-26 12:12:00 | TERRA_M-T | BENEDITO LEITE | MARANHÃO | Brasil | 2101806 | 21 | 33 | nan | nan | nan | Cerrado | 4.5 |
| 32ca8726-1a4d-3367-9936-ee64bb8d5e7a | -6.84189 | -45.17794 | 2025-07-26 12:12:00 | TERRA_M-T | LORETO | MARANHÃO | Brasil | 2106102 | 21 | 33 | nan | nan | nan | Cerrado | 4.7 |
| 1a261dda-5dd0-3435-ad82-11d44e2e55b5 | -7.51889 | -44.39359 | 2025-07-26 12:12:00 | TERRA_M-T | URUÇUÍ | PIAUÍ | Brasil | 2211209 | 22 | 33 | nan | nan | nan | Cerrado | 5.3 |
| 6c37c123-bf6f-3884-a1e6-d7b3ea5a23cd | -13.09424 | -47.34677 | 2025-07-26 12:12:00 | TERRA_M-T | ARRAIAS | TOCANTINS | Brasil | 1702406 | 17 | 33 | nan | nan | nan | Cerrado | 10.4 |
| f6e4dc31-268f-3a06-8083-c63e54e61fbc | -6.13232 | -42.53534 | 2025-07-26 12:12:00 | TERRA_M-T | JARDIM DO MULATO | PIAUÍ | Brasil | 2205250 | 22 | 33 | nan | nan | nan | Caatinga | 9.8 |
| 0e441138-2ccb-3110-89de-eca554292251 | -6.9895 | -43.32682 | 2025-07-26 12:12:00 | TERRA_M-T | JERUMENHA | PIAUÍ | Brasil | 2205300 | 22 | 33 | nan | nan | nan | Caatinga | 5.2 |
| 638d2f55-c3e4-30d2-89bc-139fbf17fbd5 | -6.9495 | -43.02012 | 2025-07-26 12:12:00 | TERRA_M-T | FLORIANO | PIAUÍ | Brasil | 2203909 | 22 | 33 | nan | nan | nan | Caatinga | 7.3 |
| 91407641-37e6-39ad-88c1-9736bb683b81 | -7.29174 | -39.62607 | 2025-07-26 12:12:00 | TERRA_M-T | SANTANA DO CARIRI | CEARÁ | Brasil | 2312106 | 23 | 33 | nan | nan | nan | Caatinga | 16.2 |
| 3610c869-c031-3952-afeb-da1e4972578b | -6.15151 | -42.59483 | 2025-07-26 12:12:00 | TERRA_M-T | JARDIM DO MULATO | PIAUÍ | Brasil | 2205250 | 22 | 33 | nan | nan | nan | Caatinga | 6.9 |
| 339666e5-e532-3073-ad2c-4496840ba8a0 | -5.77656 | -43.6112 | 2025-07-26 12:12:00 | TERRA_M-T | LAGOA DO MATO | MARANHÃO | Brasil | 2105922 | 21 | 33 | nan | nan | nan | Cerrado | 6.2 |
| c85af5a7-fba9-37b8-a2a9-be497983b7c9 | -11.57944 | -44.84521 | 2025-07-26 12:12:00 | TERRA_M-T | RIACHÃO DAS NEVES | BAHIA | Brasil | 2926202 | 29 | 33 | nan | nan | nan | Cerrado | 25.5 |
| 9bbb8f70-6af8-3427-9d5e-d9638baeca23 | -6.78611 | -44.10558 | 2025-07-26 12:12:00 | TERRA_M-T | NOVA IORQUE | MARANHÃO | Brasil | 2107308 | 21 | 33 | nan | nan | nan | Cerrado | 6.4 |
| 13a12812-4010-37e8-a111-de6c8edcd6db | -5.74365 | -43.965 | 2025-07-26 12:12:00 | TERRA_M-T | BURITI BRAVO | MARANHÃO | Brasil | 2102309 | 21 | 33 | nan | nan | nan | Cerrado | 7.8 |
| 7fe76887-57cc-3692-abe9-17e507b15ffb | -7.2898 | -39.64035 | 2025-07-26 12:12:00 | TERRA_M-T | SANTANA DO CARIRI | CEARÁ | Brasil | 2312106 | 23 | 33 | nan | nan | nan | Caatinga | 53.2 |
| 81c05293-1594-32e9-9996-b99630c8d7ab | -7.58717 | -45.38144 | 2025-07-26 12:12:00 | TERRA_M-T | LORETO | MARANHÃO | Brasil | 2106102 | 21 | 33 | nan | nan | nan | Cerrado | 9.6 |
| 8055e40d-c164-3cdf-8271-d9619a2914fb | -12.69301 | -47.00599 | 2025-07-26 12:12:00 | TERRA_M-T | ARRAIAS | TOCANTINS | Brasil | 1702406 | 17 | 33 | nan | nan | nan | Cerrado | 8.5 |
| 295a8741-fa58-3db6-b4ec-d5812bed0e7d | -10.84679 | -46.68995 | 2025-07-26 12:12:00 | TERRA_M-T | MATEIROS | TOCANTINS | Brasil | 1712702 | 17 | 33 | nan | nan | nan | Cerrado | 11.6 |
| 93dd2cfd-2ca3-397b-9f71-8b6b2313aeeb | -6.86438 | -43.68489 | 2025-07-26 12:12:00 | TERRA_M-T | GUADALUPE | PIAUÍ | Brasil | 2204501 | 22 | 33 | nan | nan | nan | Cerrado | 24.7 |
| 77be470a-8f1e-38f4-b139-23dc37fa4c0d | -6.53643 | -45.62393 | 2025-07-26 12:12:00 | TERRA_M-T | MIRADOR | MARANHÃO | Brasil | 2106706 | 21 | 33 | nan | nan | nan | Cerrado | 9.3 |
| 291e5cd6-2161-39fd-bc87-fd95af6aad10 | -7.37071 | -43.4323 | 2025-07-26 12:12:00 | TERRA_M-T | CANAVIEIRA | PIAUÍ | Brasil | 2202251 | 22 | 33 | nan | nan | nan | Cerrado | 7.9 |
| 85c4edba-7f97-3bfb-a024-79fc7cf125b9 | -10.65597 | -46.61289 | 2025-07-26 12:12:00 | TERRA_M-T | MATEIROS | TOCANTINS | Brasil | 1712702 | 17 | 33 | nan | nan | nan | Cerrado | 11.3 |
| 07b64d99-da8c-3abf-91f5-35f970856552 | -6.67493 | -43.96976 | 2025-07-26 12:12:00 | TERRA_M-T | NOVA IORQUE | MARANHÃO | Brasil | 2107308 | 21 | 33 | nan | nan | nan | Cerrado | 38.6 |
| 7b957ecf-c383-3e40-8cb7-882507c683d6 | -13.24247 | -40.60112 | 2025-07-26 12:12:00 | TERRA_M-T | MARACÁS | BAHIA | Brasil | 2920502 | 29 | 33 | nan | nan | nan | Caatinga | 9.9 |
| d77cfc2a-2d73-3950-a28a-5ad782a6d558 | -6.16053 | -42.59611 | 2025-07-26 12:12:00 | TERRA_M-T | JARDIM DO MULATO | PIAUÍ | Brasil | 2205250 | 22 | 33 | nan | nan | nan | Caatinga | 10.2 |
| a11d5ff6-5cdb-3cef-a743-5af1eb3417b1 | -12.04841 | -45.43406 | 2025-07-26 12:12:00 | TERRA_M-T | BARREIRAS | BAHIA | Brasil | 2903201 | 29 | 33 | nan | nan | nan | Cerrado | 6.9 |
| 38e4b789-5996-3d27-828c-41cf048499dc | -6.77235 | -43.68362 | 2025-07-26 12:12:00 | TERRA_M-T | GUADALUPE | PIAUÍ | Brasil | 2204501 | 22 | 33 | nan | nan | nan | Cerrado | 6.8 |
| 00b824c7-78eb-3cda-b4b3-ff4cd59a70df | -10.67086 | -46.63142 | 2025-07-26 12:12:00 | TERRA_M-T | MATEIROS | TOCANTINS | Brasil | 1712702 | 17 | 33 | nan | nan | nan | Cerrado | 55.4 |
| 57fc65ce-8423-3f49-b0d3-cfeedf9f27da | -6.72653 | -45.39764 | 2025-07-26 12:12:00 | TERRA_M-T | MIRADOR | MARANHÃO | Brasil | 2106706 | 21 | 33 | nan | nan | nan | Cerrado | 11.9 |
| f8eec45d-7aa4-31cf-ad44-76ced965a847 | -12.6694 | -45.27859 | 2025-07-26 12:12:00 | TERRA_M-T | SÃO DESIDÉRIO | BAHIA | Brasil | 2928901 | 29 | 33 | nan | nan | nan | Cerrado | 6.7 |
| 0b06bad7-53de-31d4-819b-fef81fc8fea4 | -7.37885 | -44.2714 | 2025-07-26 12:12:00 | TERRA_M-T | SEBASTIÃO LEAL | PIAUÍ | Brasil | 2210631 | 22 | 33 | nan | nan | nan | Cerrado | 14.2 |
| 5e1bbc26-88c0-38a2-b3a0-8fd956a64299 | -6.81014 | -43.93838 | 2025-07-26 12:12:00 | TERRA_M-T | PORTO ALEGRE DO PIAUÍ | PIAUÍ | Brasil | 2208551 | 22 | 33 | nan | nan | nan | Cerrado | 3.9 |
| 3c75f089-26b3-3690-b912-93dc156719f8 | -8.81488 | -46.7512 | 2025-07-26 12:12:00 | TERRA_M-T | BALSAS | MARANHÃO | Brasil | 2101400 | 21 | 33 | nan | nan | nan | Cerrado | 8.3 |
| 8bf569ad-9d9e-3183-aab8-73648fe6fb73 | -6.89056 | -43.1075 | 2025-07-26 12:12:00 | TERRA_M-T | FLORIANO | PIAUÍ | Brasil | 2203909 | 22 | 33 | nan | nan | nan | Cerrado | 6.4 |
| 05106f3e-47c7-3111-bf31-ae51f17da22f | -6.8732 | -43.68615 | 2025-07-26 12:12:00 | TERRA_M-T | GUADALUPE | PIAUÍ | Brasil | 2204501 | 22 | 33 | nan | nan | nan | Cerrado | 24.4 |
| 833b8f26-79e3-3a4e-9293-d3e63a38ca8e | -6.53781 | -45.61448 | 2025-07-26 12:12:00 | TERRA_M-T | MIRADOR | MARANHÃO | Brasil | 2106706 | 21 | 33 | nan | nan | nan | Cerrado | 14.2 |
| f54469c6-1db9-3e63-be97-ed2c6b241091 | -8.2257 | -44.92316 | 2025-07-26 12:12:00 | TERRA_M-T | BAIXA GRANDE DO RIBEIRO | PIAUÍ | Brasil | 2201150 | 22 | 33 | nan | nan | nan | Cerrado | 8.3 |
| 80dc626e-c34a-3c1c-82e5-f680ae871450 | -8.37733 | -46.65461 | 2025-07-26 12:12:00 | TERRA_M-T | RIACHÃO | MARANHÃO | Brasil | 2109502 | 21 | 33 | nan | nan | nan | Cerrado | 6.6 |
| 7a7a4244-181d-3ba7-98e7-7ff41ba058ec | -7.23758 | -43.06912 | 2025-07-26 12:12:00 | TERRA_M-T | FLORIANO | PIAUÍ | Brasil | 2203909 | 22 | 33 | nan | nan | nan | Caatinga | 8.8 |
| b256eea4-156b-335f-a388-aa607cabe696 | -10.67231 | -46.62179 | 2025-07-26 12:12:00 | TERRA_M-T | MATEIROS | TOCANTINS | Brasil | 1712702 | 17 | 33 | nan | nan | nan | Cerrado | 30.9 |
| da37e1e6-4463-3718-9a96-2f48d666627d | -9.68376 | -48.24362 | 2025-07-26 12:12:00 | TERRA_M-T | TOCANTÍNIA | TOCANTINS | Brasil | 1721109 | 17 | 33 | nan | nan | nan | Cerrado | 9.2 |
| db24d165-4f6f-35b0-815d-58c573087d3e | -7.08021 | -44.04871 | 2025-07-26 12:12:00 | TERRA_M-T | PORTO ALEGRE DO PIAUÍ | PIAUÍ | Brasil | 2208551 | 22 | 33 | nan | nan | nan | Cerrado | 6.5 |
| 8be9fe18-2f09-3fa1-ac03-25ad4d28be25 | -10.62204 | -44.75801 | 2025-07-26 12:12:00 | TERRA_M-T | SEBASTIÃO BARROS | PIAUÍ | Brasil | 2210623 | 22 | 33 | nan | nan | nan | Cerrado | 20.7 |
| af2d967a-cb32-37ba-88d9-cb36dd5c8291 | -11.57062 | -44.84395 | 2025-07-26 12:12:00 | TERRA_M-T | RIACHÃO DAS NEVES | BAHIA | Brasil | 2926202 | 29 | 33 | nan | nan | nan | Cerrado | 76.3 |
| 318c8e7b-c30b-3c48-bcaf-888449ff093f | -6.56337 | -41.50223 | 2025-07-26 12:12:00 | TERRA_M-T | SÃO JOÃO DA CANABRAVA | PIAUÍ | Brasil | 2209856 | 22 | 33 | nan | nan | nan | Caatinga | 16.8 |
| 9359d8b6-34ae-394e-aa20-67144fc43c63 | -10.44011 | -46.50945 | 2025-07-26 12:12:00 | TERRA_M-T | MATEIROS | TOCANTINS | Brasil | 1712702 | 17 | 33 | nan | nan | nan | Cerrado | 14.0 |
| e14c4f2a-6f41-333f-bb1f-f0eec7b0514e | -7.52769 | -44.39483 | 2025-07-26 12:12:00 | TERRA_M-T | URUÇUÍ | PIAUÍ | Brasil | 2211209 | 22 | 33 | nan | nan | nan | Cerrado | 7.0 |
| 7fcd5e7f-236d-348f-80e8-51a7f18d90dd | -6.76841 | -44.78806 | 2025-07-26 12:12:00 | TERRA_M-T | SÃO FÉLIX DE BALSAS | MARANHÃO | Brasil | 2110807 | 21 | 33 | nan | nan | nan | Cerrado | 12.3 |
| 348a6264-f7a4-369f-a6c4-206cb40b9296 | -7.08274 | -44.03111 | 2025-07-26 12:12:00 | TERRA_M-T | PORTO ALEGRE DO PIAUÍ | PIAUÍ | Brasil | 2208551 | 22 | 33 | nan | nan | nan | Cerrado | 7.1 |
| 83ef8bea-6697-3a37-8c73-f8ea9386fe72 | -7.89705 | -44.72158 | 2025-07-26 12:12:00 | TERRA_M-T | URUÇUÍ | PIAUÍ | Brasil | 2211209 | 22 | 33 | nan | nan | nan | Cerrado | 5.0 |
| 8f7312e7-38ad-38ff-896b-ff05767f7a80 | -18.39122 | -44.18361 | 2025-07-26 12:14:00 | TERRA_M-T | SANTO HIPÓLITO | MINAS GERAIS | Brasil | 3160603 | 31 | 33 | nan | nan | nan | Cerrado | 73.8 |
| 88b19c35-9874-3f23-8a7f-960b03ba0946 | -13.52124 | -45.52045 | 2025-07-26 12:14:00 | TERRA_M-T | CORRENTINA | BAHIA | Brasil | 2909307 | 29 | 33 | nan | nan | nan | Cerrado | 92.8 |
| 5d5ecd6f-56bb-3cf1-b0c9-af65706ddb6c | -16.10824 | -48.05508 | 2025-07-26 12:14:00 | TERRA_M-T | NOVO GAMA | GOIÁS | Brasil | 5215231 | 52 | 33 | nan | nan | nan | Cerrado | 4.6 |
| d5ad98ba-788e-3e98-be1f-ea2ae1c4e44f | -18.52614 | -48.2558 | 2025-07-26 12:14:00 | TERRA_M-T | ARAGUARI | MINAS GERAIS | Brasil | 3103504 | 31 | 33 | nan | nan | nan | Cerrado | 6.6 |
| eb5e013d-15d5-3225-a124-0db656722d39 | -15.01591 | -49.25827 | 2025-07-26 12:14:00 | TERRA_M-T | GOIANÉSIA | GOIÁS | Brasil | 5208608 | 52 | 33 | nan | nan | nan | Cerrado | 5.6 |
| 2b05ea2d-4b98-3b85-a17b-6bb02fece366 | -14.21859 | -43.96009 | 2025-07-26 12:14:00 | TERRA_M-T | CARINHANHA | BAHIA | Brasil | 2907103 | 29 | 33 | nan | nan | nan | Cerrado | 6.5 |
| c01e0ae5-27fe-37dc-9af9-5b8ea184b3b5 | -18.40068 | -44.18494 | 2025-07-26 12:14:00 | TERRA_M-T | SANTO HIPÓLITO | MINAS GERAIS | Brasil | 3160603 | 31 | 33 | nan | nan | nan | Cerrado | 12.9 |
| 0042b622-6c07-3112-89d1-f60964246425 | -22.265 | -55.98047 | 2025-07-26 12:14:00 | TERRA_M-T | ANTÔNIO JOÃO | MATO GROSSO DO SUL | Brasil | 5000906 | 50 | 33 | nan | nan | nan | Cerrado | 25.7 |
| 7a9d91f7-1b61-370f-b41e-4da5c9ff400d | -17.13396 | -47.75029 | 2025-07-26 12:14:00 | TERRA_M-T | IPAMERI | GOIÁS | Brasil | 5210109 | 52 | 33 | nan | nan | nan | Cerrado | 6.1 |
| ec159f08-0f5a-3a4b-8da4-c8bf8b398a2b | -16.12259 | -47.41324 | 2025-07-26 12:14:00 | TERRA_M-T | CRISTALINA | GOIÁS | Brasil | 5206206 | 52 | 33 | nan | nan | nan | Cerrado | 7.0 |
| 0a99e6f2-c7c9-354e-87f9-bd85df1a44b7 | -19.21685 | -44.26728 | 2025-07-26 12:14:00 | TERRA_M-T | ARAÇAÍ | MINAS GERAIS | Brasil | 3103207 | 31 | 33 | nan | nan | nan | Cerrado | 4.1 |
| e8d0a602-fbed-3c33-9d15-0b26e145a0e9 | -15.358 | -43.15226 | 2025-07-26 12:14:00 | TERRA_M-T | CATUTI | MINAS GERAIS | Brasil | 3115474 | 31 | 33 | nan | nan | nan | Caatinga | 12.6 |
| 0ab526ea-2bc5-3b5e-948a-ed36bdcca749 | -14.2439 | -45.50161 | 2025-07-26 12:14:00 | TERRA_M-T | JABORANDI | BAHIA | Brasil | 2917359 | 29 | 33 | nan | nan | nan | Cerrado | 5.7 |
| 6456aca4-a9d3-38c0-a6a4-ec4263a71b4b | -13.69342 | -45.66851 | 2025-07-26 12:14:00 | TERRA_M-T | CORRENTINA | BAHIA | Brasil | 2909307 | 29 | 33 | nan | nan | nan | Cerrado | 4.6 |
| 0a5b89f6-c2ac-3cff-a904-ce4b90d9c2a2 | -13.50621 | -45.49988 | 2025-07-26 12:14:00 | TERRA_M-T | CORRENTINA | BAHIA | Brasil | 2909307 | 29 | 33 | nan | nan | nan | Cerrado | 54.5 |
| f44cdf09-c5b9-3c3c-a734-e0674e6714b7 | -17.03607 | -46.85719 | 2025-07-26 12:14:00 | TERRA_M-T | PARACATU | MINAS GERAIS | Brasil | 3147006 | 31 | 33 | nan | nan | nan | Cerrado | 31.7 |


[Clique aqui para ver as próximas entradas](README33.md)
