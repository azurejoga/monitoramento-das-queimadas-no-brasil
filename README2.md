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
| c5303174-80f0-3f36-9646-698a812bdd05 | -4.46082 | -47.91826 | 2026-08-03 03:42:00 | NOAA-21 | DOM ELISEU | PARÁ | Brasil | 1502939 | 15 | 33 | nan | nan | nan | Amazônia | 3.9 |
| ae0bb871-eb20-37e5-a960-97bf21565db2 | -6.76229 | -41.00155 | 2026-08-03 03:42:00 | NOAA-21 | PIO IX | PIAUÍ | Brasil | 2208205 | 22 | 33 | nan | nan | nan | Caatinga | 0.6 |
| fd9d275e-4361-3c2f-8d9c-5e717b2d0b0d | -5.21145 | -38.02853 | 2026-08-03 03:42:00 | NOAA-21 | LIMOEIRO DO NORTE | CEARÁ | Brasil | 2307601 | 23 | 33 | nan | nan | nan | Caatinga | 0.6 |
| a8ad18f5-6784-3cca-beea-2f8133ae5585 | -6.90596 | -43.72652 | 2026-08-03 03:42:00 | NOAA-21 | GUADALUPE | PIAUÍ | Brasil | 2204501 | 22 | 33 | nan | nan | nan | Cerrado | 1.6 |
| a70a3459-cafb-3b2a-a0db-f7c47f572689 | -5.7198 | -44.50089 | 2026-08-03 03:42:00 | NOAA-21 | TUNTUM | MARANHÃO | Brasil | 2112308 | 21 | 33 | nan | nan | nan | Cerrado | 1.4 |
| ed8d44fa-bcd5-37a9-8574-d961e1e9dd82 | -4.26819 | -48.1984 | 2026-08-03 03:42:00 | NOAA-21 | RONDON DO PARÁ | PARÁ | Brasil | 1506187 | 15 | 33 | nan | nan | nan | Amazônia | 5.9 |
| 3d6f3ed7-8280-378b-9dfa-678c682f123d | -3.12383 | -40.10955 | 2026-08-03 03:42:00 | NOAA-21 | MARCO | CEARÁ | Brasil | 2307809 | 23 | 33 | nan | nan | nan | Caatinga | 0.8 |
| 2d3725ed-f7cb-30f2-ada6-519b64a4f534 | -7.80497 | -34.95794 | 2026-08-03 03:42:00 | NOAA-21 | IGARASSU | PERNAMBUCO | Brasil | 2606804 | 26 | 33 | nan | nan | nan | Mata Atlântica | 0.5 |
| 5500e978-7aa5-3ff8-b070-cc5bcf2fc81f | -5.61938 | -47.10442 | 2026-08-03 03:42:00 | NOAA-21 | BURITIRANA | MARANHÃO | Brasil | 2102358 | 21 | 33 | nan | nan | nan | Cerrado | 2.1 |
| a1a3ff32-eb7c-3f64-b9e3-2b3e3e21981a | -6.54739 | -41.83402 | 2026-08-03 03:42:00 | NOAA-21 | VALENÇA DO PIAUÍ | PIAUÍ | Brasil | 2211308 | 22 | 33 | nan | nan | nan | Caatinga | 3.2 |
| c42ff459-490c-31fd-ade8-969eb1c84f6e | -6.99315 | -42.11797 | 2026-08-03 03:42:00 | NOAA-21 | OEIRAS | PIAUÍ | Brasil | 2207009 | 22 | 33 | nan | nan | nan | Caatinga | 1.9 |
| c68d9ad7-e5f9-3f57-b6dd-36bd65f65b53 | -6.08678 | -43.66281 | 2026-08-03 03:42:00 | NOAA-21 | PASSAGEM FRANCA | MARANHÃO | Brasil | 2107902 | 21 | 33 | nan | nan | nan | Cerrado | 0.9 |
| 5a6c9f69-7fbb-37af-ba1f-804e9666964b | -5.72142 | -44.50292 | 2026-08-03 03:42:00 | NOAA-21 | TUNTUM | MARANHÃO | Brasil | 2112308 | 21 | 33 | nan | nan | nan | Cerrado | 2.9 |
| 91c9b56b-b873-30e7-946d-a910545348f9 | -7.0267 | -42.88491 | 2026-08-03 03:42:00 | NOAA-21 | FLORIANO | PIAUÍ | Brasil | 2203909 | 22 | 33 | nan | nan | nan | Caatinga | 2.3 |
| ed4a8d19-deb7-3b13-8b03-40a3ef4d33a6 | -5.20373 | -46.0748 | 2026-08-03 03:42:00 | NOAA-21 | ARAME | MARANHÃO | Brasil | 2100956 | 21 | 33 | nan | nan | nan | Amazônia | 2.2 |
| 321867c5-96f4-3d57-9e1d-7f570289477e | -4.51973 | -38.54955 | 2026-08-03 03:42:00 | NOAA-21 | OCARA | CEARÁ | Brasil | 2309458 | 23 | 33 | nan | nan | nan | Caatinga | 12.0 |
| 3061342d-82f7-390f-96d4-70fcad40111d | -5.62591 | -47.1048 | 2026-08-03 03:42:00 | NOAA-21 | BURITIRANA | MARANHÃO | Brasil | 2102358 | 21 | 33 | nan | nan | nan | Cerrado | 2.1 |
| 72199bf4-411f-3b9b-bf7e-3b3c5e8ec345 | -4.26935 | -48.19186 | 2026-08-03 03:42:00 | NOAA-21 | RONDON DO PARÁ | PARÁ | Brasil | 1506187 | 15 | 33 | nan | nan | nan | Amazônia | 5.8 |
| 775a93d6-958e-3069-8c18-15461046ec1a | -6.0832 | -43.6641 | 2026-08-03 03:42:00 | NOAA-21 | PASSAGEM FRANCA | MARANHÃO | Brasil | 2107902 | 21 | 33 | nan | nan | nan | Cerrado | 1.1 |
| be8211b4-8c7c-3d2a-8f9d-eb12bb54a474 | -5.34603 | -41.00151 | 2026-08-03 03:42:00 | NOAA-21 | BURITI DOS MONTES | PIAUÍ | Brasil | 2202026 | 22 | 33 | nan | nan | nan | Caatinga | 1.9 |
| 68ef1e88-af75-329d-a1d0-a3f272603975 | -5.34794 | -41.00155 | 2026-08-03 03:42:00 | NOAA-21 | BURITI DOS MONTES | PIAUÍ | Brasil | 2202026 | 22 | 33 | nan | nan | nan | Caatinga | 2.1 |
| f8528a0c-1fd9-3317-a92e-1e42e573e704 | -3.89612 | -38.53917 | 2026-08-03 03:42:00 | NOAA-21 | ITAITINGA | CEARÁ | Brasil | 2306256 | 23 | 33 | nan | nan | nan | Caatinga | 1.8 |
| bb3ede94-9cb9-3e21-b77f-6f8944944a6f | -4.2763 | -48.19312 | 2026-08-03 03:42:00 | NOAA-21 | RONDON DO PARÁ | PARÁ | Brasil | 1506187 | 15 | 33 | nan | nan | nan | Amazônia | 0.9 |
| 86d68f1c-8d78-37b0-8995-9aaf8a113c8d | -4.4592 | -47.92074 | 2026-08-03 03:42:00 | NOAA-21 | DOM ELISEU | PARÁ | Brasil | 1502939 | 15 | 33 | nan | nan | nan | Amazônia | 2.6 |
| 6828e102-0469-3bc9-b8f5-67d4630e9a12 | -6.55346 | -41.82534 | 2026-08-03 03:42:00 | NOAA-21 | VALENÇA DO PIAUÍ | PIAUÍ | Brasil | 2211308 | 22 | 33 | nan | nan | nan | Caatinga | 1.4 |
| f3568a97-e7fb-357a-80b6-9656eaba5dbb | -6.30097 | -44.88453 | 2026-08-03 03:42:00 | NOAA-21 | MIRADOR | MARANHÃO | Brasil | 2106706 | 21 | 33 | nan | nan | nan | Cerrado | 3.1 |
| e481d51c-55f1-3dfa-a9ee-8d9793b8fe1f | -5.97124 | -45.01248 | 2026-08-03 03:42:00 | NOAA-21 | FERNANDO FALCÃO | MARANHÃO | Brasil | 2104081 | 21 | 33 | nan | nan | nan | Cerrado | 2.5 |
| c77fdd22-7bea-3231-bdd4-f67abdcbe981 | -6.2961 | -44.8801 | 2026-08-03 03:42:00 | NOAA-21 | MIRADOR | MARANHÃO | Brasil | 2106706 | 21 | 33 | nan | nan | nan | Cerrado | 1.2 |
| ad312576-d06a-3ed9-9d01-bb5273f0ee26 | -3.02547 | -39.96965 | 2026-08-03 03:42:00 | NOAA-21 | ITAREMA | CEARÁ | Brasil | 2306553 | 23 | 33 | nan | nan | nan | Caatinga | 1.3 |
| 4e2c33f9-52d1-3915-ad23-e4d646bdf45d | -6.29549 | -44.88226 | 2026-08-03 03:42:00 | NOAA-21 | MIRADOR | MARANHÃO | Brasil | 2106706 | 21 | 33 | nan | nan | nan | Cerrado | 0.6 |
| 9aa50178-b652-30f6-823e-d009a9fb85c8 | -3.02963 | -39.97031 | 2026-08-03 03:42:00 | NOAA-21 | ITAREMA | CEARÁ | Brasil | 2306553 | 23 | 33 | nan | nan | nan | Caatinga | 1.3 |
| 88759aab-3659-396f-9582-1370f4237f24 | -4.12785 | -38.20943 | 2026-08-03 03:42:00 | NOAA-21 | CASCAVEL | CEARÁ | Brasil | 2303501 | 23 | 33 | nan | nan | nan | Caatinga | 1.6 |
| b47738c6-f4f4-3655-ade6-760bd4f34d07 | -3.81977 | -43.39088 | 2026-08-03 03:42:00 | NOAA-21 | CHAPADINHA | MARANHÃO | Brasil | 2103208 | 21 | 33 | nan | nan | nan | Cerrado | 1.5 |
| 9997a326-53d4-329e-9635-2928473bf1d8 | -5.08843 | -37.98016 | 2026-08-03 03:42:00 | NOAA-21 | QUIXERÉ | CEARÁ | Brasil | 2311504 | 23 | 33 | nan | nan | nan | Caatinga | 1.0 |
| c299f979-b14e-3d88-9ca1-8fdf90c9861b | -6.03718 | -40.32866 | 2026-08-03 03:42:00 | NOAA-21 | TAUÁ | CEARÁ | Brasil | 2313302 | 23 | 33 | nan | nan | nan | Caatinga | 1.2 |
| 3e63b539-e7e9-35e9-a2ff-f8791950302d | -6.90545 | -43.72948 | 2026-08-03 03:42:00 | NOAA-21 | GUADALUPE | PIAUÍ | Brasil | 2204501 | 22 | 33 | nan | nan | nan | Cerrado | 2.2 |
| 10851afb-cc35-3d74-b088-20005544b971 | -5.96431 | -45.01904 | 2026-08-03 03:42:00 | NOAA-21 | FERNANDO FALCÃO | MARANHÃO | Brasil | 2104081 | 21 | 33 | nan | nan | nan | Cerrado | 1.9 |
| 85656ca0-3d21-3f2e-bb5f-c818c8286369 | -4.4603 | -47.91446 | 2026-08-03 03:42:00 | NOAA-21 | DOM ELISEU | PARÁ | Brasil | 1502939 | 15 | 33 | nan | nan | nan | Amazônia | 2.3 |
| c5f56bd2-378b-3970-84f8-437844da1718 | -5.20455 | -46.07008 | 2026-08-03 03:42:00 | NOAA-21 | ARAME | MARANHÃO | Brasil | 2100956 | 21 | 33 | nan | nan | nan | Amazônia | 2.9 |
| 99049135-7ecf-3584-bddc-48b3cf91fbf1 | -5.96604 | -45.01789 | 2026-08-03 03:42:00 | NOAA-21 | FERNANDO FALCÃO | MARANHÃO | Brasil | 2104081 | 21 | 33 | nan | nan | nan | Cerrado | 2.6 |
| 5f2d816d-244d-3e26-8ecb-777c3e5c3d3c | -7.39321 | -45.06639 | 2026-08-03 03:45:00 | NOAA-21 | LORETO | MARANHÃO | Brasil | 2106102 | 21 | 33 | nan | nan | nan | Cerrado | 2.6 |
| e9624c52-fb14-3590-8f28-f80814c283b3 | -7.47423 | -44.89494 | 2026-08-03 03:45:00 | NOAA-21 | URUÇUÍ | PIAUÍ | Brasil | 2211209 | 22 | 33 | nan | nan | nan | Cerrado | 1.1 |
| 1ec304ef-4069-356c-849e-a6dabcecadb5 | -11.70637 | -40.58852 | 2026-08-03 03:45:00 | NOAA-21 | PIRITIBA | BAHIA | Brasil | 2924801 | 29 | 33 | nan | nan | nan | Caatinga | 0.7 |
| 32fb0bc6-efb8-3147-9fcc-084c0fe0a413 | -10.57416 | -46.80154 | 2026-08-03 03:45:00 | NOAA-21 | MATEIROS | TOCANTINS | Brasil | 1712702 | 17 | 33 | nan | nan | nan | Cerrado | 4.4 |
| 0076e6a5-c561-366d-b35b-0aae000be747 | -7.15896 | -44.04638 | 2026-08-03 03:45:00 | NOAA-21 | PORTO ALEGRE DO PIAUÍ | PIAUÍ | Brasil | 2208551 | 22 | 33 | nan | nan | nan | Cerrado | 0.6 |
| 07fe2560-d7b9-3095-8dae-f217748a0777 | -10.56991 | -46.79236 | 2026-08-03 03:45:00 | NOAA-21 | MATEIROS | TOCANTINS | Brasil | 1712702 | 17 | 33 | nan | nan | nan | Cerrado | 7.3 |
| 61fc97f9-2252-37c1-a1f2-a5ada6da50fa | -7.36134 | -43.85959 | 2026-08-03 03:45:00 | NOAA-21 | LANDRI SALES | PIAUÍ | Brasil | 2205607 | 22 | 33 | nan | nan | nan | Cerrado | 3.2 |
| 352ce396-e7d3-3b52-b002-8deafc3ea94b | -7.62778 | -45.30744 | 2026-08-03 03:45:00 | NOAA-21 | RIBEIRO GONÇALVES | PIAUÍ | Brasil | 2208908 | 22 | 33 | nan | nan | nan | Cerrado | 1.1 |
| eed2a476-4443-3fd5-b507-740f034edc4e | -7.55784 | -45.09583 | 2026-08-03 03:45:00 | NOAA-21 | RIBEIRO GONÇALVES | PIAUÍ | Brasil | 2208908 | 22 | 33 | nan | nan | nan | Cerrado | 2.3 |
| ec3a1fce-b1b1-3ce5-928a-c86b4bce4464 | -7.38707 | -45.06917 | 2026-08-03 03:45:00 | NOAA-21 | LORETO | MARANHÃO | Brasil | 2106102 | 21 | 33 | nan | nan | nan | Cerrado | 2.6 |
| 50feea91-ecf3-3e24-a769-cdf6f6f1d710 | -10.58365 | -46.78362 | 2026-08-03 03:45:00 | NOAA-21 | MATEIROS | TOCANTINS | Brasil | 1712702 | 17 | 33 | nan | nan | nan | Cerrado | 2.2 |
| fc49da22-2abd-3de5-b815-505e7259b87a | -7.96532 | -44.92029 | 2026-08-03 03:45:00 | NOAA-21 | BAIXA GRANDE DO RIBEIRO | PIAUÍ | Brasil | 2201150 | 22 | 33 | nan | nan | nan | Cerrado | 1.4 |
| 6bc77ce0-adee-3654-87ea-89d65ad9b946 | -7.35233 | -43.8571 | 2026-08-03 03:45:00 | NOAA-21 | LANDRI SALES | PIAUÍ | Brasil | 2205607 | 22 | 33 | nan | nan | nan | Cerrado | 4.4 |
| cd133030-859e-3e87-ace9-77ec5a2be1e7 | -10.57068 | -46.78831 | 2026-08-03 03:45:00 | NOAA-21 | MATEIROS | TOCANTINS | Brasil | 1712702 | 17 | 33 | nan | nan | nan | Cerrado | 3.4 |
| 2b462753-5a72-33b1-b4ae-1276489af2b9 | -7.9647 | -44.92373 | 2026-08-03 03:45:00 | NOAA-21 | BAIXA GRANDE DO RIBEIRO | PIAUÍ | Brasil | 2201150 | 22 | 33 | nan | nan | nan | Cerrado | 2.4 |
| c416e66b-c6bc-33b3-8be8-f7932a79c5e1 | -7.3608 | -43.86259 | 2026-08-03 03:45:00 | NOAA-21 | LANDRI SALES | PIAUÍ | Brasil | 2205607 | 22 | 33 | nan | nan | nan | Cerrado | 3.2 |
| 2dd2863b-023b-324a-abdc-761f0cd46cad | -7.34503 | -43.8634 | 2026-08-03 03:45:00 | NOAA-21 | LANDRI SALES | PIAUÍ | Brasil | 2205607 | 22 | 33 | nan | nan | nan | Cerrado | 5.4 |
| 6a5726d7-aab9-33d0-ba42-fbc43e4269f7 | -7.55885 | -45.09568 | 2026-08-03 03:45:00 | NOAA-21 | RIBEIRO GONÇALVES | PIAUÍ | Brasil | 2208908 | 22 | 33 | nan | nan | nan | Cerrado | 1.9 |
| df1a37cb-8a1f-3960-b3de-5f1449c22352 | -12.18956 | -39.77143 | 2026-08-03 03:45:00 | NOAA-21 | IPIRÁ | BAHIA | Brasil | 2914000 | 29 | 33 | nan | nan | nan | Caatinga | 1.3 |
| ef657cf0-836b-311b-95bf-86108f6618f4 | -7.35129 | -43.86314 | 2026-08-03 03:45:00 | NOAA-21 | LANDRI SALES | PIAUÍ | Brasil | 2205607 | 22 | 33 | nan | nan | nan | Cerrado | 3.7 |
| e4f5ecf3-a10c-350c-bd19-41949e54c6f0 | -10.57727 | -46.78517 | 2026-08-03 03:45:00 | NOAA-21 | MATEIROS | TOCANTINS | Brasil | 1712702 | 17 | 33 | nan | nan | nan | Cerrado | 3.4 |
| 2e3eedca-ae84-30eb-a815-4c1905a79858 | -7.35626 | -43.85889 | 2026-08-03 03:45:00 | NOAA-21 | LANDRI SALES | PIAUÍ | Brasil | 2205607 | 22 | 33 | nan | nan | nan | Cerrado | 3.2 |
| ba1b090c-fb02-3471-8af6-b48d6ba29b8c | -10.58286 | -46.78764 | 2026-08-03 03:45:00 | NOAA-21 | MATEIROS | TOCANTINS | Brasil | 1712702 | 17 | 33 | nan | nan | nan | Cerrado | 2.7 |
| 86528824-6110-3af7-a632-8b156b40c284 | -9.41109 | -48.57912 | 2026-08-03 03:45:00 | NOAA-21 | RIO DOS BOIS | TOCANTINS | Brasil | 1718709 | 17 | 33 | nan | nan | nan | Cerrado | 4.0 |
| 17506201-d097-3bc8-9450-fad2ad2ff476 | -7.38157 | -45.06836 | 2026-08-03 03:45:00 | NOAA-21 | LORETO | MARANHÃO | Brasil | 2106102 | 21 | 33 | nan | nan | nan | Cerrado | 0.5 |
| 20c466f8-46e0-36fb-b7a1-7073bce86972 | -7.47482 | -44.89157 | 2026-08-03 03:45:00 | NOAA-21 | URUÇUÍ | PIAUÍ | Brasil | 2211209 | 22 | 33 | nan | nan | nan | Cerrado | 1.1 |
| 503e155d-06a9-3ad9-b118-eb25000b5c79 | -10.57571 | -46.79338 | 2026-08-03 03:45:00 | NOAA-21 | MATEIROS | TOCANTINS | Brasil | 1712702 | 17 | 33 | nan | nan | nan | Cerrado | 7.3 |
| e2131eea-757c-3bf5-ad3f-1981aee29bb1 | -7.35517 | -43.86495 | 2026-08-03 03:45:00 | NOAA-21 | LANDRI SALES | PIAUÍ | Brasil | 2205607 | 22 | 33 | nan | nan | nan | Cerrado | 3.8 |
| c8ea9692-e350-3738-aa51-3421eda40131 | -7.47362 | -44.89835 | 2026-08-03 03:45:00 | NOAA-21 | URUÇUÍ | PIAUÍ | Brasil | 2211209 | 22 | 33 | nan | nan | nan | Cerrado | 0.7 |
| da408105-ba1c-3bd2-9cff-b017933731b7 | -7.35571 | -43.8619 | 2026-08-03 03:45:00 | NOAA-21 | LANDRI SALES | PIAUÍ | Brasil | 2205607 | 22 | 33 | nan | nan | nan | Cerrado | 3.2 |
| ffb1a121-4845-3e84-a9ed-cc085d76e6d4 | -12.33884 | -45.71178 | 2026-08-03 03:45:00 | NOAA-21 | LUÍS EDUARDO MAGALHÃES | BAHIA | Brasil | 2919553 | 29 | 33 | nan | nan | nan | Cerrado | 4.6 |
| 55f6cb93-45ab-3c61-a5bf-8af9eb8d79f9 | -6.8615 | -44.79219 | 2026-08-03 03:45:00 | NOAA-21 | SÃO FÉLIX DE BALSAS | MARANHÃO | Brasil | 2110807 | 21 | 33 | nan | nan | nan | Cerrado | 1.0 |
| c478cbdb-5a8b-3832-82a0-4c6ada9965ba | -7.56402 | -45.09274 | 2026-08-03 03:45:00 | NOAA-21 | RIBEIRO GONÇALVES | PIAUÍ | Brasil | 2208908 | 22 | 33 | nan | nan | nan | Cerrado | 2.0 |
| 649213d3-71fd-357b-9b8c-d438633a96b1 | -12.33819 | -45.71515 | 2026-08-03 03:45:00 | NOAA-21 | LUÍS EDUARDO MAGALHÃES | BAHIA | Brasil | 2919553 | 29 | 33 | nan | nan | nan | Cerrado | 4.4 |
| 2ecfe4fb-6cd4-3297-adce-e1c43bd20496 | -8.34595 | -45.9864 | 2026-08-03 03:45:00 | NOAA-21 | TASSO FRAGOSO | MARANHÃO | Brasil | 2112001 | 21 | 33 | nan | nan | nan | Cerrado | 4.5 |
| b96fadf4-334f-3157-98ab-1f2326247afb | -7.56026 | -45.11408 | 2026-08-03 03:45:00 | NOAA-21 | RIBEIRO GONÇALVES | PIAUÍ | Brasil | 2208908 | 22 | 33 | nan | nan | nan | Cerrado | 1.6 |
| ab431c38-6ec6-3d83-8976-93664a0ab655 | -6.85543 | -44.795 | 2026-08-03 03:45:00 | NOAA-21 | SÃO FÉLIX DE BALSAS | MARANHÃO | Brasil | 2110807 | 21 | 33 | nan | nan | nan | Cerrado | 1.0 |
| f8c36a3b-e4d4-3a43-b676-a3231ca31d6b | -7.55951 | -45.0921 | 2026-08-03 03:45:00 | NOAA-21 | RIBEIRO GONÇALVES | PIAUÍ | Brasil | 2208908 | 22 | 33 | nan | nan | nan | Cerrado | 1.6 |
| a3cd7cd1-43ff-3418-81a1-307f7789fb85 | -6.77586 | -47.02365 | 2026-08-03 03:45:00 | NOAA-21 | ESTREITO | MARANHÃO | Brasil | 2104057 | 21 | 33 | nan | nan | nan | Cerrado | 2.2 |
| faab200f-3bb5-3edb-833c-6fd6b961ff41 | -12.1227 | -45.67878 | 2026-08-03 03:45:00 | NOAA-21 | LUÍS EDUARDO MAGALHÃES | BAHIA | Brasil | 2919553 | 29 | 33 | nan | nan | nan | Cerrado | 1.8 |
| 358de1c4-73d7-34c1-8aa8-5b24265f3a3a | -10.62624 | -46.74944 | 2026-08-03 03:45:00 | NOAA-21 | MATEIROS | TOCANTINS | Brasil | 1712702 | 17 | 33 | nan | nan | nan | Cerrado | 1.1 |
| 75180dae-1512-3c47-84cc-913dea5b42b7 | -8.35167 | -45.9874 | 2026-08-03 03:45:00 | NOAA-21 | TASSO FRAGOSO | MARANHÃO | Brasil | 2112001 | 21 | 33 | nan | nan | nan | Cerrado | 4.5 |
| 3cbfdb39-2b15-3c22-b2ac-8ef38f0352b3 | -7.34448 | -43.86642 | 2026-08-03 03:45:00 | NOAA-21 | LANDRI SALES | PIAUÍ | Brasil | 2205607 | 22 | 33 | nan | nan | nan | Cerrado | 5.4 |
| 19d0294c-d219-37ab-976d-f7f16b0a337b | -7.3574 | -43.85784 | 2026-08-03 03:45:00 | NOAA-21 | LANDRI SALES | PIAUÍ | Brasil | 2205607 | 22 | 33 | nan | nan | nan | Cerrado | 4.4 |
| 3ad08b89-5142-3bd3-bfcd-b44a00eb52f4 | -7.15386 | -44.04528 | 2026-08-03 03:45:00 | NOAA-21 | PORTO ALEGRE DO PIAUÍ | PIAUÍ | Brasil | 2208551 | 22 | 33 | nan | nan | nan | Cerrado | 1.4 |
| ffb70955-dd72-38ec-ac04-2be6cf95c185 | -7.35792 | -43.85484 | 2026-08-03 03:45:00 | NOAA-21 | LANDRI SALES | PIAUÍ | Brasil | 2205607 | 22 | 33 | nan | nan | nan | Cerrado | 9.6 |
| 4e1e6b7c-9fe1-3ea1-a789-a3f1b723d247 | -10.54713 | -42.54257 | 2026-08-03 03:45:00 | NOAA-21 | XIQUE-XIQUE | BAHIA | Brasil | 2933604 | 29 | 33 | nan | nan | nan | Caatinga | 3.8 |
| 3d0cbaf1-b804-3584-9b8e-d702f883144b | -8.5002 | -39.65693 | 2026-08-03 03:45:00 | NOAA-21 | SANTA MARIA DA BOA VISTA | PERNAMBUCO | Brasil | 2612604 | 26 | 33 | nan | nan | nan | Caatinga | 0.8 |
| 9867e081-5013-3ae7-9b9e-ce84ef5a19c7 | -7.3457 | -43.86538 | 2026-08-03 03:45:00 | NOAA-21 | LANDRI SALES | PIAUÍ | Brasil | 2205607 | 22 | 33 | nan | nan | nan | Cerrado | 6.5 |
| d0090ca5-68a9-3807-9d78-0e1885c077a2 | -8.49994 | -39.65432 | 2026-08-03 03:45:00 | NOAA-21 | SANTA MARIA DA BOA VISTA | PERNAMBUCO | Brasil | 2612604 | 26 | 33 | nan | nan | nan | Caatinga | 1.4 |
| 1eb06b54-ebae-3f94-aeb2-8413c6a78e30 | -7.35733 | -43.85292 | 2026-08-03 03:45:00 | NOAA-21 | LANDRI SALES | PIAUÍ | Brasil | 2205607 | 22 | 33 | nan | nan | nan | Cerrado | 3.4 |
| 09edea13-e5d0-3acd-89df-347180690002 | -7.35181 | -43.86012 | 2026-08-03 03:45:00 | NOAA-21 | LANDRI SALES | PIAUÍ | Brasil | 2205607 | 22 | 33 | nan | nan | nan | Cerrado | 4.4 |
| a1dd530a-6d56-3bfe-aeed-b852d0de3e62 | -7.34623 | -43.86235 | 2026-08-03 03:45:00 | NOAA-21 | LANDRI SALES | PIAUÍ | Brasil | 2205607 | 22 | 33 | nan | nan | nan | Cerrado | 6.5 |
| 66730fed-9c58-38b4-888e-06c461aed8a9 | -10.56837 | -46.80046 | 2026-08-03 03:45:00 | NOAA-21 | MATEIROS | TOCANTINS | Brasil | 1712702 | 17 | 33 | nan | nan | nan | Cerrado | 4.4 |
| c8f40c55-2b35-3c83-b617-37ebdc79522e | -7.35118 | -43.85815 | 2026-08-03 03:45:00 | NOAA-21 | LANDRI SALES | PIAUÍ | Brasil | 2205607 | 22 | 33 | nan | nan | nan | Cerrado | 4.9 |
| 931db53b-8bf1-3800-a4ca-852f14d3d3e9 | -7.56579 | -45.11472 | 2026-08-03 03:45:00 | NOAA-21 | RIBEIRO GONÇALVES | PIAUÍ | Brasil | 2208908 | 22 | 33 | nan | nan | nan | Cerrado | 1.4 |
| 11a38f12-418f-34d7-96f4-5a5d2fa0ddfc | -7.56113 | -45.11396 | 2026-08-03 03:45:00 | NOAA-21 | RIBEIRO GONÇALVES | PIAUÍ | Brasil | 2208908 | 22 | 33 | nan | nan | nan | Cerrado | 3.4 |
| 668421a7-b06f-310d-9efb-27e713e2b569 | -8.58972 | -39.42127 | 2026-08-03 03:45:00 | NOAA-21 | CURAÇÁ | BAHIA | Brasil | 2909901 | 29 | 33 | nan | nan | nan | Caatinga | 1.6 |
| a31f016c-12f2-3830-a745-08174c3035d6 | -7.34674 | -43.85934 | 2026-08-03 03:45:00 | NOAA-21 | LANDRI SALES | PIAUÍ | Brasil | 2205607 | 22 | 33 | nan | nan | nan | Cerrado | 5.4 |
| 6f05ac7a-9601-3a14-8044-15c50f0e7f46 | -6.85767 | -44.79232 | 2026-08-03 03:45:00 | NOAA-21 | SÃO FÉLIX DE BALSAS | MARANHÃO | Brasil | 2110807 | 21 | 33 | nan | nan | nan | Cerrado | 2.8 |


[Clique aqui para ver as próximas entradas](README3.md)
