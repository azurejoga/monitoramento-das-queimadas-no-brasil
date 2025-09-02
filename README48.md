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

## Dados Diários - Página 48

| ID | Latitude | Longitude | Data/Hora GMT | Satélite | Município | Estado | País | Município ID | Estado ID | País ID | Dias sem Chuva | Precipitação | Risco de Fogo | Bioma | FRP |
|----|----------|-----------|---------------|----------|-----------|--------|------|--------------|-----------|---------|----------------|--------------|----------------|-------|-----|
| a381bf41-fb5c-35dd-b737-b5fb9accb461 | -20.70279 | -46.29789 | 2025-09-02 04:17:00 | NOAA-20 | SÃO JOSÉ DA BARRA | MINAS GERAIS | Brasil | 3162948 | 31 | 33 | nan | nan | nan | Cerrado | 1.4 |
| 453caa7f-73d2-35ef-8b88-827eb3ae4de0 | -20.07648 | -45.56624 | 2025-09-02 04:17:00 | NOAA-20 | LAGOA DA PRATA | MINAS GERAIS | Brasil | 3137205 | 31 | 33 | nan | nan | nan | Cerrado | 0.7 |
| 554bc52f-e656-330b-81d8-a9797136a16e | -12.92574 | -56.96545 | 2025-09-02 04:17:00 | NOAA-20 | NOVA MARINGÁ | MATO GROSSO | Brasil | 5108907 | 51 | 33 | nan | nan | nan | Amazônia | 3.4 |
| d87fe711-43d8-362c-a785-33dc38c7dc89 | -12.93264 | -56.95713 | 2025-09-02 04:17:00 | NOAA-20 | NOVA MARINGÁ | MATO GROSSO | Brasil | 5108907 | 51 | 33 | nan | nan | nan | Amazônia | 2.9 |
| 960c691d-d407-3350-9b05-1baf2ea855e8 | -12.92689 | -56.95999 | 2025-09-02 04:17:00 | NOAA-20 | NOVA MARINGÁ | MATO GROSSO | Brasil | 5108907 | 51 | 33 | nan | nan | nan | Amazônia | 3.4 |
| ad497091-5f49-380d-9e94-57e8620ec72b | -20.48291 | -49.69033 | 2025-09-02 04:17:00 | NOAA-20 | TANABI | SÃO PAULO | Brasil | 3553401 | 35 | 33 | nan | nan | nan | Cerrado | 0.9 |
| 9b5101fb-4b20-37c6-8010-c31e9b0a458e | -14.78879 | -48.20433 | 2025-09-02 04:17:00 | NOAA-20 | NIQUELÂNDIA | GOIÁS | Brasil | 5214606 | 52 | 33 | nan | nan | nan | Cerrado | 2.8 |
| 31d79205-b9f7-36e5-9738-900471ce5950 | -15.57153 | -48.34283 | 2025-09-02 04:17:00 | NOAA-20 | PADRE BERNARDO | GOIÁS | Brasil | 5215603 | 52 | 33 | nan | nan | nan | Cerrado | 11.0 |
| 221e6a9e-6ed5-3c08-a5d4-1c68ebe95509 | -14.49007 | -45.93996 | 2025-09-02 04:17:00 | NOAA-20 | JABORANDI | BAHIA | Brasil | 2917359 | 29 | 33 | nan | nan | nan | Cerrado | 2.1 |
| a2acc0a4-c5bb-375d-9d7c-88590d250ce4 | -14.63316 | -48.03629 | 2025-09-02 04:17:00 | NOAA-20 | NIQUELÂNDIA | GOIÁS | Brasil | 5214606 | 52 | 33 | nan | nan | nan | Cerrado | 4.5 |
| 39575d1e-de87-3805-813b-c5aad01f895e | -15.5665 | -48.37202 | 2025-09-02 04:17:00 | NOAA-20 | PADRE BERNARDO | GOIÁS | Brasil | 5215603 | 52 | 33 | nan | nan | nan | Cerrado | 5.6 |
| a20288ac-fec9-3cfa-a841-0ae19308b16a | -15.72786 | -49.02583 | 2025-09-02 04:17:00 | NOAA-20 | PIRENÓPOLIS | GOIÁS | Brasil | 5217302 | 52 | 33 | nan | nan | nan | Cerrado | 2.3 |
| 18e52183-f6ec-32bc-9e39-aa685041ebde | -18.06737 | -45.95809 | 2025-09-02 04:17:00 | NOAA-20 | JOÃO PINHEIRO | MINAS GERAIS | Brasil | 3136306 | 31 | 33 | nan | nan | nan | Cerrado | 0.9 |
| f8673d3d-a340-341b-8d82-83e9739fee90 | -20.70496 | -46.30581 | 2025-09-02 04:17:00 | NOAA-20 | SÃO JOSÉ DA BARRA | MINAS GERAIS | Brasil | 3162948 | 31 | 33 | nan | nan | nan | Cerrado | 0.6 |
| 7e24ad92-c4d0-3185-9849-0bba1a97048b | -14.59636 | -48.04527 | 2025-09-02 04:17:00 | NOAA-20 | NIQUELÂNDIA | GOIÁS | Brasil | 5214606 | 52 | 33 | nan | nan | nan | Cerrado | 3.5 |
| 9aeae828-5aab-3e87-b86d-4aa75bd2e8e4 | -14.21586 | -48.05959 | 2025-09-02 04:17:00 | NOAA-20 | NIQUELÂNDIA | GOIÁS | Brasil | 5214606 | 52 | 33 | nan | nan | nan | Cerrado | 3.1 |
| 991215f6-f185-3a3b-a9c3-08b118119264 | -15.55788 | -49.75317 | 2025-09-02 04:17:00 | NOAA-20 | ITAPURANGA | GOIÁS | Brasil | 5211206 | 52 | 33 | nan | nan | nan | Cerrado | 1.0 |
| b641a92f-2d53-302b-83d5-4eabdc319d55 | -15.71678 | -49.02383 | 2025-09-02 04:17:00 | NOAA-20 | PIRENÓPOLIS | GOIÁS | Brasil | 5217302 | 52 | 33 | nan | nan | nan | Cerrado | 2.7 |
| 7cd0cf71-bcf2-3153-a6ed-d2affebb0d8e | -14.72365 | -46.75034 | 2025-09-02 04:17:00 | NOAA-20 | FLORES DE GOIÁS | GOIÁS | Brasil | 5207907 | 52 | 33 | nan | nan | nan | Cerrado | 1.9 |
| 830a9fc9-a927-3f92-9ad8-fa5206504e68 | -14.58443 | -54.56164 | 2025-09-02 04:17:00 | NOAA-20 | PLANALTO DA SERRA | MATO GROSSO | Brasil | 5106455 | 51 | 33 | nan | nan | nan | Cerrado | 1.2 |
| 0b35c2d5-26c3-3fcd-9a61-44568221af45 | -14.75452 | -48.15741 | 2025-09-02 04:17:00 | NOAA-20 | NIQUELÂNDIA | GOIÁS | Brasil | 5214606 | 52 | 33 | nan | nan | nan | Cerrado | 1.5 |
| 6ce29603-f666-33d0-a1ed-43f4f2b96018 | -17.17458 | -46.08384 | 2025-09-02 04:17:00 | NOAA-20 | JOÃO PINHEIRO | MINAS GERAIS | Brasil | 3136306 | 31 | 33 | nan | nan | nan | Cerrado | 1.7 |
| 47191f03-985d-3256-b991-80fdd80418ca | -17.19462 | -46.06496 | 2025-09-02 04:17:00 | NOAA-20 | JOÃO PINHEIRO | MINAS GERAIS | Brasil | 3136306 | 31 | 33 | nan | nan | nan | Cerrado | 0.7 |
| 5aad141a-02ca-3e76-a591-82f1800c8e05 | -14.74126 | -46.74936 | 2025-09-02 04:17:00 | NOAA-20 | FLORES DE GOIÁS | GOIÁS | Brasil | 5207907 | 52 | 33 | nan | nan | nan | Cerrado | 0.8 |
| 3d39b067-8917-3141-999b-c63b0d697ead | -15.1192 | -48.18377 | 2025-09-02 04:17:00 | NOAA-20 | MIMOSO DE GOIÁS | GOIÁS | Brasil | 5213053 | 52 | 33 | nan | nan | nan | Cerrado | 2.4 |
| c1daa509-701d-32eb-a0ab-b6ec9bdde139 | -20.11561 | -46.01584 | 2025-09-02 04:17:00 | NOAA-20 | BAMBUÍ | MINAS GERAIS | Brasil | 3105103 | 31 | 33 | nan | nan | nan | Cerrado | 0.8 |
| 7a31d1ce-9f81-30ce-95db-9c39068a8312 | -14.23191 | -51.65942 | 2025-09-02 04:17:00 | NOAA-20 | COCALINHO | MATO GROSSO | Brasil | 5103106 | 51 | 33 | nan | nan | nan | Cerrado | 2.1 |
| e000f7bb-58f1-3c6c-b0e2-264e42d00d62 | -17.174 | -46.0875 | 2025-09-02 04:17:00 | NOAA-20 | JOÃO PINHEIRO | MINAS GERAIS | Brasil | 3136306 | 31 | 33 | nan | nan | nan | Cerrado | 1.7 |
| 8469acf3-6448-3fc6-80e5-eb6979170856 | -14.73044 | -46.75148 | 2025-09-02 04:17:00 | NOAA-20 | FLORES DE GOIÁS | GOIÁS | Brasil | 5207907 | 52 | 33 | nan | nan | nan | Cerrado | 1.8 |
| bb59643d-c3ef-3c50-aa9d-684ddba2636a | -21.46246 | -47.41225 | 2025-09-02 04:17:00 | NOAA-20 | SANTA ROSA DE VITERBO | SÃO PAULO | Brasil | 3547601 | 35 | 33 | nan | nan | nan | Cerrado | 0.3 |
| c6b74354-35b1-3b63-8118-368d2a82dfd4 | -17.21297 | -46.8937 | 2025-09-02 04:17:00 | NOAA-20 | PARACATU | MINAS GERAIS | Brasil | 3147006 | 31 | 33 | nan | nan | nan | Cerrado | 0.8 |
| aa6bfa8f-d7b1-3dae-a329-e6e98dc113e8 | -16.85744 | -49.576 | 2025-09-02 04:17:00 | NOAA-20 | GUAPÓ | GOIÁS | Brasil | 5209200 | 52 | 33 | nan | nan | nan | Cerrado | 16.4 |
| e43a44a5-5918-3575-8b0e-cc73342f3473 | -14.59567 | -48.04932 | 2025-09-02 04:17:00 | NOAA-20 | NIQUELÂNDIA | GOIÁS | Brasil | 5214606 | 52 | 33 | nan | nan | nan | Cerrado | 2.3 |
| 4b0f7af0-cd81-3273-9753-7fcf6e122518 | -12.92274 | -56.94817 | 2025-09-02 04:17:00 | NOAA-20 | NOVA MARINGÁ | MATO GROSSO | Brasil | 5108907 | 51 | 33 | nan | nan | nan | Amazônia | 3.1 |
| 74967901-5381-3f8b-87f0-5c3e665d142e | -14.59707 | -48.04098 | 2025-09-02 04:17:00 | NOAA-20 | NIQUELÂNDIA | GOIÁS | Brasil | 5214606 | 52 | 33 | nan | nan | nan | Cerrado | 3.5 |
| 2770c1e9-e2b7-35af-818e-06f0301c92d3 | -19.75478 | -47.88898 | 2025-09-02 04:17:00 | NOAA-20 | UBERABA | MINAS GERAIS | Brasil | 3170107 | 31 | 33 | nan | nan | nan | Cerrado | 2.5 |
| 8f9cc115-a6de-3f1d-b160-dc75b17d4f33 | -15.70875 | -48.8731 | 2025-09-02 04:17:00 | NOAA-20 | PIRENÓPOLIS | GOIÁS | Brasil | 5217302 | 52 | 33 | nan | nan | nan | Cerrado | 0.8 |
| 04392d8a-1335-31a0-8ef4-b165f32b2b5b | -14.49891 | -45.94888 | 2025-09-02 04:17:00 | NOAA-20 | JABORANDI | BAHIA | Brasil | 2917359 | 29 | 33 | nan | nan | nan | Cerrado | 0.7 |
| 8ace377e-9b71-347b-a4c3-1f51f4f0d3d4 | -14.79236 | -48.20507 | 2025-09-02 04:17:00 | NOAA-20 | NIQUELÂNDIA | GOIÁS | Brasil | 5214606 | 52 | 33 | nan | nan | nan | Cerrado | 1.0 |
| aac386dd-be91-3145-8572-f1ad7c10731c | -14.59215 | -48.07032 | 2025-09-02 04:17:00 | NOAA-20 | NIQUELÂNDIA | GOIÁS | Brasil | 5214606 | 52 | 33 | nan | nan | nan | Cerrado | 1.7 |
| f2fb2a8c-3a78-3d47-8fba-356d1c32e0da | -14.21082 | -48.06749 | 2025-09-02 04:17:00 | NOAA-20 | NIQUELÂNDIA | GOIÁS | Brasil | 5214606 | 52 | 33 | nan | nan | nan | Cerrado | 1.0 |
| ef09bb9b-c387-3aeb-9844-b367693d81e3 | -14.81112 | -48.35386 | 2025-09-02 04:17:00 | NOAA-20 | NIQUELÂNDIA | GOIÁS | Brasil | 5214606 | 52 | 33 | nan | nan | nan | Cerrado | 1.0 |
| 434f9162-7fff-3f1a-ab59-27a44603bf5e | -15.59221 | -48.37281 | 2025-09-02 04:17:00 | NOAA-20 | PADRE BERNARDO | GOIÁS | Brasil | 5215603 | 52 | 33 | nan | nan | nan | Cerrado | 2.2 |
| f9707470-e904-3399-9b0b-6732b3fa4aed | -15.56796 | -48.3422 | 2025-09-02 04:17:00 | NOAA-20 | PADRE BERNARDO | GOIÁS | Brasil | 5215603 | 52 | 33 | nan | nan | nan | Cerrado | 11.0 |
| fc389a8f-db85-3ef4-95fd-2e545529f946 | -15.33546 | -46.11294 | 2025-09-02 04:17:00 | NOAA-20 | FORMOSO | MINAS GERAIS | Brasil | 3126208 | 31 | 33 | nan | nan | nan | Cerrado | 1.0 |
| 281d3b74-eee6-3d6a-8f15-cdb3450f31a6 | -17.19404 | -46.06858 | 2025-09-02 04:17:00 | NOAA-20 | JOÃO PINHEIRO | MINAS GERAIS | Brasil | 3136306 | 31 | 33 | nan | nan | nan | Cerrado | 0.7 |
| 11ca8e50-075a-3fef-b914-10453e6bb46b | -14.21944 | -51.65223 | 2025-09-02 04:17:00 | NOAA-20 | COCALINHO | MATO GROSSO | Brasil | 5103106 | 51 | 33 | nan | nan | nan | Cerrado | 3.8 |
| d8e32041-d60a-3dbf-8e30-0d65eb2ac43a | -20.70222 | -46.30156 | 2025-09-02 04:17:00 | NOAA-20 | SÃO JOSÉ DA BARRA | MINAS GERAIS | Brasil | 3162948 | 31 | 33 | nan | nan | nan | Cerrado | 1.5 |
| 009d0ac6-e3dc-31ad-b363-c7c6091fd5bc | -14.58576 | -48.06452 | 2025-09-02 04:17:00 | NOAA-20 | NIQUELÂNDIA | GOIÁS | Brasil | 5214606 | 52 | 33 | nan | nan | nan | Cerrado | 7.8 |
| 9349306a-7cf0-3272-8974-7c29d020b4ce | -14.71878 | -49.43913 | 2025-09-02 04:17:00 | NOAA-20 | HIDROLINA | GOIÁS | Brasil | 5209804 | 52 | 33 | nan | nan | nan | Cerrado | 1.2 |
| d3927570-fd2b-3319-b133-c6438f3804d2 | -19.81878 | -45.0077 | 2025-09-02 04:17:00 | NOAA-20 | NOVA SERRANA | MINAS GERAIS | Brasil | 3145208 | 31 | 33 | nan | nan | nan | Cerrado | 4.5 |
| 694dc660-f054-39b9-98a2-5f79ed63a29b | -13.89771 | -48.09816 | 2025-09-02 04:17:00 | NOAA-20 | COLINAS DO SUL | GOIÁS | Brasil | 5205521 | 52 | 33 | nan | nan | nan | Cerrado | 1.6 |
| 65fd3715-0827-316e-89e5-ca292ba0fc6b | -14.59807 | -48.06927 | 2025-09-02 04:17:00 | NOAA-20 | NIQUELÂNDIA | GOIÁS | Brasil | 5214606 | 52 | 33 | nan | nan | nan | Cerrado | 3.2 |
| 9a0cfca6-41d6-34d4-8457-45f2ecb9b1bb | -12.93155 | -56.96251 | 2025-09-02 04:17:00 | NOAA-20 | NOVA MARINGÁ | MATO GROSSO | Brasil | 5108907 | 51 | 33 | nan | nan | nan | Amazônia | 2.9 |
| 5e24523c-3aa5-3101-86fb-bbffa0c23882 | -17.8903 | -47.1649 | 2025-09-02 04:17:00 | NOAA-20 | GUARDA-MOR | MINAS GERAIS | Brasil | 3128600 | 31 | 33 | nan | nan | nan | Cerrado | 13.9 |
| 9fe4b9af-d79f-3f1b-a8be-726a9b8f7dfc | -13.99804 | -46.31387 | 2025-09-02 04:17:00 | NOAA-20 | GUARANI DE GOIÁS | GOIÁS | Brasil | 5209408 | 52 | 33 | nan | nan | nan | Cerrado | 1.1 |
| e66be740-f3c8-36b8-89fc-d3d58d9422c1 | -15.34436 | -43.84422 | 2025-09-02 04:17:00 | NOAA-20 | JAÍBA | MINAS GERAIS | Brasil | 3135050 | 31 | 33 | nan | nan | nan | Cerrado | 0.8 |
| 6d1b1649-afc8-3d59-9666-32bed301a25b | -15.56579 | -48.37617 | 2025-09-02 04:17:00 | NOAA-20 | PADRE BERNARDO | GOIÁS | Brasil | 5215603 | 52 | 33 | nan | nan | nan | Cerrado | 18.5 |
| f3f1e44a-5870-3e6b-9448-16f13a6a677d | -17.70413 | -46.8881 | 2025-09-02 04:17:00 | NOAA-20 | VAZANTE | MINAS GERAIS | Brasil | 3171006 | 31 | 33 | nan | nan | nan | Cerrado | 16.6 |
| ec66808b-7d7e-37ea-8116-d75b63f84264 | -14.74516 | -48.14744 | 2025-09-02 04:17:00 | NOAA-20 | NIQUELÂNDIA | GOIÁS | Brasil | 5214606 | 52 | 33 | nan | nan | nan | Cerrado | 2.3 |
| df9e5a1c-4f7e-3c25-9d46-0487edbb46b9 | -12.92342 | -56.97647 | 2025-09-02 04:17:00 | NOAA-20 | NOVA MARINGÁ | MATO GROSSO | Brasil | 5108907 | 51 | 33 | nan | nan | nan | Amazônia | 2.8 |
| 8c4f2f5b-dd47-3b69-aacb-5c6a6f977c3c | -20.7061 | -46.29847 | 2025-09-02 04:17:00 | NOAA-20 | SÃO JOSÉ DA BARRA | MINAS GERAIS | Brasil | 3162948 | 31 | 33 | nan | nan | nan | Cerrado | 0.6 |
| 521c3c46-1fb3-3ebb-ae69-626093ab2a85 | -14.21514 | -48.06383 | 2025-09-02 04:17:00 | NOAA-20 | COLINAS DO SUL | GOIÁS | Brasil | 5205521 | 52 | 33 | nan | nan | nan | Cerrado | 3.3 |
| f5216f33-1c6b-3dff-9d04-7cc3e11e37a4 | -20.48214 | -49.69471 | 2025-09-02 04:17:00 | NOAA-20 | TANABI | SÃO PAULO | Brasil | 3553401 | 35 | 33 | nan | nan | nan | Cerrado | 1.0 |
| 450e17a2-8e11-3b98-b74a-cf947c1c2214 | -15.56174 | -49.75385 | 2025-09-02 04:17:00 | NOAA-20 | ITAPURANGA | GOIÁS | Brasil | 5211206 | 52 | 33 | nan | nan | nan | Cerrado | 1.6 |
| d65e52d3-eb0e-35ce-b0fc-23356279c06a | -15.58791 | -48.37635 | 2025-09-02 04:17:00 | NOAA-20 | PADRE BERNARDO | GOIÁS | Brasil | 5215603 | 52 | 33 | nan | nan | nan | Cerrado | 1.3 |
| 18f76450-0227-3637-94f0-d24095b27b29 | -17.28753 | -49.20803 | 2025-09-02 04:17:00 | NOAA-20 | PROFESSOR JAMIL | GOIÁS | Brasil | 5218391 | 52 | 33 | nan | nan | nan | Cerrado | 0.8 |
| 726e66df-81c3-392e-9af9-8b45d8d458b7 | -16.06897 | -49.45822 | 2025-09-02 04:17:00 | NOAA-20 | SANTA ROSA DE GOIÁS | GOIÁS | Brasil | 5219506 | 52 | 33 | nan | nan | nan | Cerrado | 0.5 |
| 2df6cc53-882a-343b-9bf1-ed46d1808964 | -15.43088 | -43.31625 | 2025-09-02 04:17:00 | NOAA-20 | JANAÚBA | MINAS GERAIS | Brasil | 3135100 | 31 | 33 | nan | nan | nan | Caatinga | 0.9 |
| 24f1c441-b54d-3a89-9b15-b06cfab23489 | -18.59179 | -44.51325 | 2025-09-02 04:17:00 | NOAA-20 | CORINTO | MINAS GERAIS | Brasil | 3119104 | 31 | 33 | nan | nan | nan | Cerrado | 5.6 |
| 0cbe4b7e-eba9-3d56-8851-0f7b6bdafd2d | -14.59814 | -48.04763 | 2025-09-02 04:17:00 | NOAA-20 | NIQUELÂNDIA | GOIÁS | Brasil | 5214606 | 52 | 33 | nan | nan | nan | Cerrado | 2.7 |
| c4ac764a-b60c-3963-9384-83816e3a5ed1 | -15.55862 | -48.35354 | 2025-09-02 04:17:00 | NOAA-20 | PADRE BERNARDO | GOIÁS | Brasil | 5215603 | 52 | 33 | nan | nan | nan | Cerrado | 2.9 |
| 07b0da07-79ff-3ea1-a348-a5352d4fc282 | -14.59319 | -48.05497 | 2025-09-02 04:17:00 | NOAA-20 | NIQUELÂNDIA | GOIÁS | Brasil | 5214606 | 52 | 33 | nan | nan | nan | Cerrado | 2.5 |
| c7a3adf5-29ee-3044-8ce7-579f6bc045d0 | -15.33604 | -46.10935 | 2025-09-02 04:17:00 | NOAA-20 | FORMOSO | MINAS GERAIS | Brasil | 3126208 | 31 | 33 | nan | nan | nan | Cerrado | 0.7 |
| 6914386c-fc92-3ec1-919f-cc0f32f22b37 | -13.82183 | -49.38289 | 2025-09-02 04:17:00 | NOAA-20 | AMARALINA | GOIÁS | Brasil | 5200829 | 52 | 33 | nan | nan | nan | Cerrado | 5.1 |
| c1af0400-139c-3f33-9966-b404b6f95a70 | -15.78438 | -42.13268 | 2025-09-02 04:17:00 | NOAA-20 | TAIOBEIRAS | MINAS GERAIS | Brasil | 3168002 | 31 | 33 | nan | nan | nan | Cerrado | 2.8 |
| f4ac0b9c-438a-3435-b208-d7df61a9d5e2 | -14.59604 | -48.03856 | 2025-09-02 04:17:00 | NOAA-20 | NIQUELÂNDIA | GOIÁS | Brasil | 5214606 | 52 | 33 | nan | nan | nan | Cerrado | 3.4 |
| 08346f0f-68d7-3663-a2d3-044b403d7e3e | -15.11741 | -48.18087 | 2025-09-02 04:17:00 | NOAA-20 | MIMOSO DE GOIÁS | GOIÁS | Brasil | 5213053 | 52 | 33 | nan | nan | nan | Cerrado | 3.5 |
| 097dfb2a-40bf-33a7-9039-21aa9b0fbf9f | -20.70107 | -46.3089 | 2025-09-02 04:17:00 | NOAA-20 | SÃO JOSÉ DA BARRA | MINAS GERAIS | Brasil | 3162948 | 31 | 33 | nan | nan | nan | Cerrado | 6.6 |
| 1dc33e1f-2b22-34e2-97e5-0dadd39b9e72 | -15.71969 | -49.02903 | 2025-09-02 04:17:00 | NOAA-20 | PIRENÓPOLIS | GOIÁS | Brasil | 5217302 | 52 | 33 | nan | nan | nan | Cerrado | 3.6 |
| 6f6087e3-3dfc-31b6-88fe-3a05ffff79b1 | -15.56791 | -48.38531 | 2025-09-02 04:17:00 | NOAA-20 | PADRE BERNARDO | GOIÁS | Brasil | 5215603 | 52 | 33 | nan | nan | nan | Cerrado | 3.5 |
| c39a1dcd-af1a-319c-b8aa-006a9f01cd94 | -15.58079 | -48.37481 | 2025-09-02 04:17:00 | NOAA-20 | PADRE BERNARDO | GOIÁS | Brasil | 5215603 | 52 | 33 | nan | nan | nan | Cerrado | 0.8 |
| 90b1930a-7f46-3624-9251-57451b236f7d | -14.81186 | -48.34957 | 2025-09-02 04:17:00 | NOAA-20 | NIQUELÂNDIA | GOIÁS | Brasil | 5214606 | 52 | 33 | nan | nan | nan | Cerrado | 1.0 |
| 8c2d5d84-6ed5-3f2f-a702-7fbb7403aa48 | -14.21245 | -51.66503 | 2025-09-02 04:17:00 | NOAA-20 | COCALINHO | MATO GROSSO | Brasil | 5103106 | 51 | 33 | nan | nan | nan | Cerrado | 2.1 |
| e5301c2d-5711-3993-8892-1d9cdcd114e1 | -17.21357 | -46.89001 | 2025-09-02 04:17:00 | NOAA-20 | PARACATU | MINAS GERAIS | Brasil | 3147006 | 31 | 33 | nan | nan | nan | Cerrado | 0.9 |
| 457e7644-a5f1-34ae-b671-d25634d3957b | -15.4343 | -43.31679 | 2025-09-02 04:17:00 | NOAA-20 | JANAÚBA | MINAS GERAIS | Brasil | 3135100 | 31 | 33 | nan | nan | nan | Caatinga | 0.9 |
| 875be888-28d2-3a43-a8ac-472a283ee61e | -20.10171 | -47.33786 | 2025-09-02 04:17:00 | NOAA-20 | SACRAMENTO | MINAS GERAIS | Brasil | 3156908 | 31 | 33 | nan | nan | nan | Cerrado | 0.6 |
| fd10135e-5eca-33ad-9a26-ead3eb202a07 | -14.76096 | -45.37162 | 2025-09-02 04:17:00 | NOAA-20 | COCOS | BAHIA | Brasil | 2908101 | 29 | 33 | nan | nan | nan | Cerrado | 0.6 |
| 582723d1-d520-3f7b-adf5-2e4532b0dc37 | -15.56506 | -48.38039 | 2025-09-02 04:17:00 | NOAA-20 | PADRE BERNARDO | GOIÁS | Brasil | 5215603 | 52 | 33 | nan | nan | nan | Cerrado | 18.5 |
| e8ece49d-5b88-35ef-8bea-2ea0725f28fa | -13.79306 | -48.48879 | 2025-09-02 04:17:00 | NOAA-20 | CAMPINAÇU | GOIÁS | Brasil | 5204656 | 52 | 33 | nan | nan | nan | Cerrado | 1.0 |
| ef4561b1-1dd8-3562-9e88-62e0675ce512 | -13.89759 | -48.07705 | 2025-09-02 04:17:00 | NOAA-20 | COLINAS DO SUL | GOIÁS | Brasil | 5205521 | 52 | 33 | nan | nan | nan | Cerrado | 0.7 |
| 270ac664-08dc-3cc0-938c-28412074fae8 | -14.97607 | -48.17789 | 2025-09-02 04:17:00 | NOAA-20 | MIMOSO DE GOIÁS | GOIÁS | Brasil | 5213053 | 52 | 33 | nan | nan | nan | Cerrado | 1.5 |
| a9f5d732-7606-3b6d-a213-c232a2312b2a | -14.58503 | -48.06885 | 2025-09-02 04:17:00 | NOAA-20 | NIQUELÂNDIA | GOIÁS | Brasil | 5214606 | 52 | 33 | nan | nan | nan | Cerrado | 7.8 |
| 7d3f58ba-ec37-38bb-8466-5258ebbd22d1 | -17.23923 | -43.75693 | 2025-09-02 04:17:00 | NOAA-20 | OLHOS-D'ÁGUA | MINAS GERAIS | Brasil | 3145455 | 31 | 33 | nan | nan | nan | Cerrado | 0.4 |
| 140e5293-abf6-3135-8911-a7c0fd789d9e | -23.93581 | -48.8458 | 2025-09-02 04:17:00 | NOAA-20 | ITAPEVA | SÃO PAULO | Brasil | 3522406 | 35 | 33 | nan | nan | nan | Cerrado | 7.2 |
| e112e0c0-1704-3c5d-8c31-b62b70779513 | -13.89842 | -48.09399 | 2025-09-02 04:17:00 | NOAA-20 | COLINAS DO SUL | GOIÁS | Brasil | 5205521 | 52 | 33 | nan | nan | nan | Cerrado | 4.1 |
| 39a91405-b61a-3a34-b332-ccc1f5dc55b1 | -16.30061 | -52.9488 | 2025-09-02 04:17:00 | NOAA-20 | TORIXORÉU | MATO GROSSO | Brasil | 5108204 | 51 | 33 | nan | nan | nan | Cerrado | 4.0 |
| 717de90d-8781-3533-84d8-2ce8346f724b | -17.61092 | -46.64491 | 2025-09-02 04:17:00 | NOAA-20 | VAZANTE | MINAS GERAIS | Brasil | 3171006 | 31 | 33 | nan | nan | nan | Cerrado | 1.0 |
| e2c4bb80-bd44-381d-b3e0-81f3cf5df711 | -17.89305 | -47.16926 | 2025-09-02 04:17:00 | NOAA-20 | GUARDA-MOR | MINAS GERAIS | Brasil | 3128600 | 31 | 33 | nan | nan | nan | Cerrado | 13.9 |
| 6e396468-0b63-3606-a191-252ede31c526 | -20.69775 | -46.30833 | 2025-09-02 04:17:00 | NOAA-20 | SÃO JOSÉ DA BARRA | MINAS GERAIS | Brasil | 3162948 | 31 | 33 | nan | nan | nan | Cerrado | 6.6 |


[Clique aqui para ver as próximas entradas](README49.md)
