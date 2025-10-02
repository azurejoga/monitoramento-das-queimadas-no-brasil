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

## Dados Diários - Página 43

| ID | Latitude | Longitude | Data/Hora GMT | Satélite | Município | Estado | País | Município ID | Estado ID | País ID | Dias sem Chuva | Precipitação | Risco de Fogo | Bioma | FRP |
|----|----------|-----------|---------------|----------|-----------|--------|------|--------------|-----------|---------|----------------|--------------|----------------|-------|-----|
| 56051c0d-257a-3f83-a14a-3311d34acc30 | -18.64819 | -48.04036 | 2025-10-02 04:04:00 | NOAA-21 | ARAGUARI | MINAS GERAIS | Brasil | 3103504 | 31 | 33 | nan | nan | nan | Cerrado | 1.7 |
| 9074dcc4-9488-3c49-bb17-0c8c12cb0429 | -14.47268 | -48.42102 | 2025-10-02 04:04:00 | NOAA-21 | NIQUELÂNDIA | GOIÁS | Brasil | 5214606 | 52 | 33 | nan | nan | nan | Cerrado | 3.2 |
| b99bf9b1-8cb2-38c7-addb-d0aa00944c02 | -15.21947 | -47.17858 | 2025-10-02 04:04:00 | NOAA-21 | FORMOSA | GOIÁS | Brasil | 5208004 | 52 | 33 | nan | nan | nan | Cerrado | 3.8 |
| 6db80628-32b6-3ce7-8081-c43d34c670e0 | -14.31369 | -45.99378 | 2025-10-02 04:04:00 | NOAA-21 | MAMBAÍ | GOIÁS | Brasil | 5212709 | 52 | 33 | nan | nan | nan | Cerrado | 13.5 |
| 996f8f4b-321d-3e3b-b951-ad26082e540f | -14.70275 | -48.20541 | 2025-10-02 04:04:00 | NOAA-21 | NIQUELÂNDIA | GOIÁS | Brasil | 5214606 | 52 | 33 | nan | nan | nan | Cerrado | 1.9 |
| d8c4b48a-e1ae-325a-a8c6-d91a6c80aa87 | -17.09402 | -47.11044 | 2025-10-02 04:04:00 | NOAA-21 | PARACATU | MINAS GERAIS | Brasil | 3147006 | 31 | 33 | nan | nan | nan | Cerrado | 1.4 |
| b1bb0eb9-cec8-371b-9a2a-e054bdb23554 | -18.52565 | -45.03632 | 2025-10-02 04:04:00 | NOAA-21 | FELIXLÂNDIA | MINAS GERAIS | Brasil | 3125705 | 31 | 33 | nan | nan | nan | Cerrado | 1.2 |
| 4efbeee7-8908-3834-ba88-6252efb47fbe | -15.32899 | -46.29132 | 2025-10-02 04:04:00 | NOAA-21 | FORMOSO | MINAS GERAIS | Brasil | 3126208 | 31 | 33 | nan | nan | nan | Cerrado | 1.7 |
| 96afe355-93c3-3b49-9d48-47a41c518c6a | -16.13708 | -46.67921 | 2025-10-02 04:04:00 | NOAA-21 | UNAÍ | MINAS GERAIS | Brasil | 3170404 | 31 | 33 | nan | nan | nan | Cerrado | 5.1 |
| 4f7e892b-1d1f-3cb5-8608-e7f19dac0251 | -15.28224 | -46.40543 | 2025-10-02 04:04:00 | NOAA-21 | BURITIS | MINAS GERAIS | Brasil | 3109303 | 31 | 33 | nan | nan | nan | Cerrado | 2.6 |
| a9e5c56a-c839-3bec-a434-964a0e0d358b | -18.84716 | -43.14681 | 2025-10-02 04:04:00 | NOAA-21 | SENHORA DO PORTO | MINAS GERAIS | Brasil | 3166105 | 31 | 33 | nan | nan | nan | Mata Atlântica | 4.0 |
| e0492507-3364-311d-8e06-21b06955d575 | -18.70505 | -43.18569 | 2025-10-02 04:04:00 | NOAA-21 | SABINÓPOLIS | MINAS GERAIS | Brasil | 3156809 | 31 | 33 | nan | nan | nan | Mata Atlântica | 0.7 |
| 2112f9af-62fe-3db0-9261-b4577ce66dd8 | -17.08629 | -47.10897 | 2025-10-02 04:04:00 | NOAA-21 | PARACATU | MINAS GERAIS | Brasil | 3147006 | 31 | 33 | nan | nan | nan | Cerrado | 0.8 |
| 18b5f3dc-f33e-3d19-b73f-8727a611d809 | -14.34365 | -47.15213 | 2025-10-02 04:04:00 | NOAA-21 | FLORES DE GOIÁS | GOIÁS | Brasil | 5207907 | 52 | 33 | nan | nan | nan | Cerrado | 1.5 |
| 0fb6ad05-bd99-3751-b627-8ed0377b66e6 | -13.7514 | -47.99675 | 2025-10-02 04:04:00 | NOAA-21 | CAVALCANTE | GOIÁS | Brasil | 5205307 | 52 | 33 | nan | nan | nan | Cerrado | 3.7 |
| 94469b20-4c21-3be9-9308-5c8a68633bc6 | -20.03719 | -44.535 | 2025-10-02 04:04:00 | NOAA-21 | ITAÚNA | MINAS GERAIS | Brasil | 3133808 | 31 | 33 | nan | nan | nan | Mata Atlântica | 1.1 |
| d49296ac-65ac-31b5-ac6d-4ad98c46cb1f | -15.76269 | -43.66964 | 2025-10-02 04:04:00 | NOAA-21 | SÃO JOÃO DA PONTE | MINAS GERAIS | Brasil | 3162401 | 31 | 33 | nan | nan | nan | Cerrado | 1.3 |
| af9fdb12-7630-36ff-929f-3eedb28482e3 | -13.30965 | -47.85817 | 2025-10-02 04:04:00 | NOAA-21 | PARANÃ | TOCANTINS | Brasil | 1716208 | 17 | 33 | nan | nan | nan | Cerrado | 16.6 |
| 4ced92fe-e67c-381a-96d2-d786735efb93 | -12.94302 | -48.42863 | 2025-10-02 04:04:00 | NOAA-21 | PALMEIRÓPOLIS | TOCANTINS | Brasil | 1715754 | 17 | 33 | nan | nan | nan | Cerrado | 10.1 |
| c333a207-1e62-394b-91a7-a83f952d5ced | -13.91989 | -48.07155 | 2025-10-02 04:04:00 | NOAA-21 | COLINAS DO SUL | GOIÁS | Brasil | 5205521 | 52 | 33 | nan | nan | nan | Cerrado | 2.6 |
| 185c31fb-f8a5-336f-aa5d-38a2f228af67 | -14.87635 | -48.13389 | 2025-10-02 04:04:00 | NOAA-21 | MIMOSO DE GOIÁS | GOIÁS | Brasil | 5213053 | 52 | 33 | nan | nan | nan | Cerrado | 2.2 |
| c09f4591-ed53-3dc3-9fb3-8d7bf355b8bb | -13.23075 | -46.43373 | 2025-10-02 04:04:00 | NOAA-21 | DIVINÓPOLIS DE GOIÁS | GOIÁS | Brasil | 5208301 | 52 | 33 | nan | nan | nan | Cerrado | 2.3 |
| 7b2c176b-6635-38b8-bda1-ccfe4c85735d | -14.6785 | -49.61325 | 2025-10-02 04:04:00 | NOAA-21 | PILAR DE GOIÁS | GOIÁS | Brasil | 5216908 | 52 | 33 | nan | nan | nan | Cerrado | 9.4 |
| 2aac5e6b-25b1-310a-a233-332eb42e902a | -17.67739 | -43.83579 | 2025-10-02 04:04:00 | NOAA-21 | BOCAIÚVA | MINAS GERAIS | Brasil | 3107307 | 31 | 33 | nan | nan | nan | Cerrado | 2.7 |
| 206e6e9b-4669-3340-82f4-c4b9d24feaa0 | -16.41398 | -47.04988 | 2025-10-02 04:04:00 | NOAA-21 | UNAÍ | MINAS GERAIS | Brasil | 3170404 | 31 | 33 | nan | nan | nan | Cerrado | 1.2 |
| fb1b5832-8261-347c-bdd1-bfee0ecd794b | -17.17176 | -47.01928 | 2025-10-02 04:04:00 | NOAA-21 | PARACATU | MINAS GERAIS | Brasil | 3147006 | 31 | 33 | nan | nan | nan | Cerrado | 3.0 |
| 744bd791-b026-3882-aaed-7a5becf5a396 | -16.14274 | -46.66964 | 2025-10-02 04:04:00 | NOAA-21 | UNAÍ | MINAS GERAIS | Brasil | 3170404 | 31 | 33 | nan | nan | nan | Cerrado | 2.7 |
| 062c1cbe-f9fa-35c5-81d7-19842b9929dc | -13.37637 | -47.2925 | 2025-10-02 04:04:00 | NOAA-21 | MONTE ALEGRE DE GOIÁS | GOIÁS | Brasil | 5213509 | 52 | 33 | nan | nan | nan | Cerrado | 2.4 |
| f5c61e8d-c168-364a-842b-dd02e0757822 | -15.34869 | -46.29041 | 2025-10-02 04:04:00 | NOAA-21 | FORMOSO | MINAS GERAIS | Brasil | 3126208 | 31 | 33 | nan | nan | nan | Cerrado | 3.3 |
| 408f1038-e932-3baf-8df7-bbbf10f78ef6 | -15.018 | -42.22525 | 2025-10-02 04:04:00 | NOAA-21 | MORTUGABA | BAHIA | Brasil | 2921807 | 29 | 33 | nan | nan | nan | Caatinga | 0.7 |
| 589c212b-9593-3aa3-a5c9-357444748f28 | -15.63652 | -46.24976 | 2025-10-02 04:04:00 | NOAA-21 | ARINOS | MINAS GERAIS | Brasil | 3104502 | 31 | 33 | nan | nan | nan | Cerrado | 1.6 |
| a4da3b8a-0fd3-3397-823f-42ada6dc49f7 | -12.70362 | -48.57671 | 2025-10-02 04:04:00 | NOAA-21 | JAÚ DO TOCANTINS | TOCANTINS | Brasil | 1711506 | 17 | 33 | nan | nan | nan | Cerrado | 9.9 |
| a860be1f-500d-3461-8e97-60fc9685f65b | -14.47097 | -48.43005 | 2025-10-02 04:04:00 | NOAA-21 | NIQUELÂNDIA | GOIÁS | Brasil | 5214606 | 52 | 33 | nan | nan | nan | Cerrado | 4.5 |
| 913a90f4-8d90-370c-ad64-258b92759fac | -13.86866 | -47.95058 | 2025-10-02 04:04:00 | NOAA-21 | CAVALCANTE | GOIÁS | Brasil | 5205307 | 52 | 33 | nan | nan | nan | Cerrado | 2.0 |
| 01545a00-de21-3733-a629-2492d0feff33 | -13.34359 | -47.33224 | 2025-10-02 04:04:00 | NOAA-21 | MONTE ALEGRE DE GOIÁS | GOIÁS | Brasil | 5213509 | 52 | 33 | nan | nan | nan | Cerrado | 3.8 |
| 27d8e43c-1cd3-37c0-9da0-c26b15d6272c | -14.476 | -48.40347 | 2025-10-02 04:04:00 | NOAA-21 | NIQUELÂNDIA | GOIÁS | Brasil | 5214606 | 52 | 33 | nan | nan | nan | Cerrado | 7.2 |
| 5abdacfd-e21a-3b6f-a5b5-063f23c3148c | -20.1371 | -42.86034 | 2025-10-02 04:04:00 | NOAA-21 | SEM-PEIXE | MINAS GERAIS | Brasil | 3165560 | 31 | 33 | nan | nan | nan | Mata Atlântica | 1.3 |
| 2953362c-2d07-338e-b418-d4865038a94c | -14.40925 | -46.09302 | 2025-10-02 04:04:00 | NOAA-21 | MAMBAÍ | GOIÁS | Brasil | 5212709 | 52 | 33 | nan | nan | nan | Cerrado | 3.1 |
| 15d53c7f-1e8e-30c0-b030-8e853892766b | -13.45768 | -47.2554 | 2025-10-02 04:04:00 | NOAA-21 | CAVALCANTE | GOIÁS | Brasil | 5205307 | 52 | 33 | nan | nan | nan | Cerrado | 4.7 |
| 3607e8dd-3c05-369c-9dd6-7a0a6c1f0192 | -14.90486 | -47.22485 | 2025-10-02 04:04:00 | NOAA-21 | FORMOSA | GOIÁS | Brasil | 5208004 | 52 | 33 | nan | nan | nan | Cerrado | 1.1 |
| 821a1167-e88e-388a-992d-fc89eb470c6c | -16.14182 | -46.67482 | 2025-10-02 04:04:00 | NOAA-21 | UNAÍ | MINAS GERAIS | Brasil | 3170404 | 31 | 33 | nan | nan | nan | Cerrado | 2.7 |
| 789c63a2-be1a-3ea6-b0e9-4c69b80f7cdd | -12.699 | -48.5761 | 2025-10-02 04:04:00 | NOAA-21 | JAÚ DO TOCANTINS | TOCANTINS | Brasil | 1711506 | 17 | 33 | nan | nan | nan | Cerrado | 5.2 |
| 508408d7-a779-3085-9641-e3bcbdee461a | -14.90159 | -48.09313 | 2025-10-02 04:04:00 | NOAA-21 | MIMOSO DE GOIÁS | GOIÁS | Brasil | 5213053 | 52 | 33 | nan | nan | nan | Cerrado | 5.0 |
| d6efc5b0-5c61-3602-8f85-4eb258ba15d4 | -14.47632 | -48.4258 | 2025-10-02 04:04:00 | NOAA-21 | NIQUELÂNDIA | GOIÁS | Brasil | 5214606 | 52 | 33 | nan | nan | nan | Cerrado | 10.0 |
| da102772-27d9-317f-b21e-c9bb730e1a8a | -14.4796 | -48.40843 | 2025-10-02 04:04:00 | NOAA-21 | NIQUELÂNDIA | GOIÁS | Brasil | 5214606 | 52 | 33 | nan | nan | nan | Cerrado | 5.7 |
| cc675e72-0408-374c-803f-eb6fb5410b05 | -18.51016 | -44.04031 | 2025-10-02 04:04:00 | NOAA-21 | MONJOLOS | MINAS GERAIS | Brasil | 3142502 | 31 | 33 | nan | nan | nan | Cerrado | 4.3 |
| d6b242e1-7129-36d5-939c-3dd1ac815a79 | -16.15374 | -45.10713 | 2025-10-02 04:04:00 | NOAA-21 | PINTÓPOLIS | MINAS GERAIS | Brasil | 3150570 | 31 | 33 | nan | nan | nan | Cerrado | 1.4 |
| 6a425202-ed67-3052-9351-c1f2dd9ec0c6 | -16.04619 | -50.86075 | 2025-10-02 04:04:00 | NOAA-21 | FAZENDA NOVA | GOIÁS | Brasil | 5207600 | 52 | 33 | nan | nan | nan | Cerrado | 2.0 |
| 5e102a5c-68c4-3e86-923b-8aebc031a4e3 | -13.16794 | -47.81744 | 2025-10-02 04:04:00 | NOAA-21 | PARANÃ | TOCANTINS | Brasil | 1716208 | 17 | 33 | nan | nan | nan | Cerrado | 6.4 |
| 2c404ca2-864c-3086-a743-5c5ce26b882c | -16.02438 | -50.86581 | 2025-10-02 04:04:00 | NOAA-21 | FAZENDA NOVA | GOIÁS | Brasil | 5207600 | 52 | 33 | nan | nan | nan | Cerrado | 1.6 |
| 01577c0e-1d30-3d05-9e57-997aaa61cae3 | -15.32012 | -46.27526 | 2025-10-02 04:04:00 | NOAA-21 | FORMOSO | MINAS GERAIS | Brasil | 3126208 | 31 | 33 | nan | nan | nan | Cerrado | 1.4 |
| cb074af2-e0ce-3a71-9971-0322248f6851 | -14.65505 | -48.12665 | 2025-10-02 04:04:00 | NOAA-21 | NIQUELÂNDIA | GOIÁS | Brasil | 5214606 | 52 | 33 | nan | nan | nan | Cerrado | 3.3 |
| f03251a1-c28e-38dc-a739-f6d92e90bc83 | -13.57016 | -47.28302 | 2025-10-02 04:04:00 | NOAA-21 | CAVALCANTE | GOIÁS | Brasil | 5205307 | 52 | 33 | nan | nan | nan | Cerrado | 3.4 |
| 99f26e03-bd77-3b62-9163-858e256410a1 | -16.01118 | -50.90605 | 2025-10-02 04:04:00 | NOAA-21 | JUSSARA | GOIÁS | Brasil | 5212204 | 52 | 33 | nan | nan | nan | Cerrado | 7.0 |
| 02272284-9951-324a-8e98-3e48776dcf3f | -19.26676 | -47.42789 | 2025-10-02 04:04:00 | NOAA-21 | PEDRINÓPOLIS | MINAS GERAIS | Brasil | 3149200 | 31 | 33 | nan | nan | nan | Cerrado | 1.2 |
| d2ddcdc4-9a45-34cc-b2b9-05f25c269b5e | -12.70296 | -48.57948 | 2025-10-02 04:04:00 | NOAA-21 | JAÚ DO TOCANTINS | TOCANTINS | Brasil | 1711506 | 17 | 33 | nan | nan | nan | Cerrado | 8.9 |
| fef2e0e8-d818-3b12-ad37-a5fc7ba73293 | -13.64379 | -47.19548 | 2025-10-02 04:04:00 | NOAA-21 | TERESINA DE GOIÁS | GOIÁS | Brasil | 5221080 | 52 | 33 | nan | nan | nan | Cerrado | 2.2 |
| bfa5c75c-a1b4-391a-b428-9c547114c0c6 | -14.45047 | -46.34482 | 2025-10-02 04:04:00 | NOAA-21 | SÍTIO D'ABADIA | GOIÁS | Brasil | 5220702 | 52 | 33 | nan | nan | nan | Cerrado | 2.9 |
| 72e0b34f-be79-3298-9e2a-af1fd3c7ce63 | -20.88304 | -43.20378 | 2025-10-02 04:04:00 | NOAA-21 | BRÁS PIRES | MINAS GERAIS | Brasil | 3108701 | 31 | 33 | nan | nan | nan | Mata Atlântica | 2.7 |
| e87656e7-3d14-38f1-9551-68af7df23ee9 | -13.24293 | -47.3343 | 2025-10-02 04:04:00 | NOAA-21 | ARRAIAS | TOCANTINS | Brasil | 1702406 | 17 | 33 | nan | nan | nan | Cerrado | 3.6 |
| 2409aea1-53cb-3bde-9dc1-ea8f6e9a45d3 | -12.68082 | -48.57125 | 2025-10-02 04:04:00 | NOAA-21 | JAÚ DO TOCANTINS | TOCANTINS | Brasil | 1711506 | 17 | 33 | nan | nan | nan | Cerrado | 5.7 |
| f2826da8-a73a-3b27-82f7-2a1e218bf559 | -13.3276 | -47.32543 | 2025-10-02 04:04:00 | NOAA-21 | MONTE ALEGRE DE GOIÁS | GOIÁS | Brasil | 5213509 | 52 | 33 | nan | nan | nan | Cerrado | 3.0 |
| bab35f03-00a3-3b12-a4e3-827ada69d9f4 | -13.15995 | -47.80125 | 2025-10-02 04:04:00 | NOAA-21 | PARANÃ | TOCANTINS | Brasil | 1716208 | 17 | 33 | nan | nan | nan | Cerrado | 2.7 |
| 60d31fe8-b150-3c83-8ca4-acd72dc1cc13 | -13.53287 | -47.27659 | 2025-10-02 04:04:00 | NOAA-21 | CAVALCANTE | GOIÁS | Brasil | 5205307 | 52 | 33 | nan | nan | nan | Cerrado | 2.0 |
| 28621ec9-183c-369d-a1e0-fd27550f03a5 | -15.19775 | -48.16571 | 2025-10-02 04:04:00 | NOAA-21 | PADRE BERNARDO | GOIÁS | Brasil | 5215603 | 52 | 33 | nan | nan | nan | Cerrado | 1.7 |
| 98e91aec-3d1b-3632-8d6d-c15dd8371dc6 | -20.14351 | -46.34019 | 2025-10-02 04:04:00 | NOAA-21 | SÃO ROQUE DE MINAS | MINAS GERAIS | Brasil | 3164308 | 31 | 33 | nan | nan | nan | Cerrado | 1.7 |
| 69db6fc1-bd9d-3d89-82eb-4bcc5a5688f1 | -15.22134 | -47.16807 | 2025-10-02 04:04:00 | NOAA-21 | FORMOSA | GOIÁS | Brasil | 5208004 | 52 | 33 | nan | nan | nan | Cerrado | 1.4 |
| b1c04858-46d6-3fc4-b24b-8dcdec3a0ca9 | -15.28085 | -49.30201 | 2025-10-02 04:04:00 | NOAA-21 | GOIANÉSIA | GOIÁS | Brasil | 5208608 | 52 | 33 | nan | nan | nan | Cerrado | 2.8 |
| a01a234b-59cc-3550-b36c-bba4bc13131a | -13.61764 | -47.29279 | 2025-10-02 04:04:00 | NOAA-21 | TERESINA DE GOIÁS | GOIÁS | Brasil | 5221080 | 52 | 33 | nan | nan | nan | Cerrado | 1.8 |
| 299bd05a-81ed-333c-8939-9e909489aadb | -14.58911 | -48.32956 | 2025-10-02 04:04:00 | NOAA-21 | NIQUELÂNDIA | GOIÁS | Brasil | 5214606 | 52 | 33 | nan | nan | nan | Cerrado | 6.4 |
| 3d72b780-3b2f-3e33-b3ed-b34c76a6da0d | -12.95047 | -48.43902 | 2025-10-02 04:04:00 | NOAA-21 | PALMEIRÓPOLIS | TOCANTINS | Brasil | 1715754 | 17 | 33 | nan | nan | nan | Cerrado | 5.4 |
| 26ff5e91-a61c-3f22-a972-9de5dd663dea | -13.32157 | -47.00449 | 2025-10-02 04:04:00 | NOAA-21 | MONTE ALEGRE DE GOIÁS | GOIÁS | Brasil | 5213509 | 52 | 33 | nan | nan | nan | Cerrado | 13.5 |
| 6b5dc5c9-8853-3f95-92c0-c40f78a0a5cc | -18.44395 | -43.81486 | 2025-10-02 04:04:00 | NOAA-21 | GOUVEIA | MINAS GERAIS | Brasil | 3127602 | 31 | 33 | nan | nan | nan | Cerrado | 2.4 |
| 90968564-236e-32df-bf00-76d1c293da3f | -14.22035 | -44.9338 | 2025-10-02 04:04:00 | NOAA-21 | COCOS | BAHIA | Brasil | 2908101 | 29 | 33 | nan | nan | nan | Cerrado | 2.7 |
| 6ec215da-2acb-35b5-840c-3c2f2260cb5e | -13.4619 | -47.25568 | 2025-10-02 04:04:00 | NOAA-21 | CAVALCANTE | GOIÁS | Brasil | 5205307 | 52 | 33 | nan | nan | nan | Cerrado | 2.1 |
| 51a6eda6-3372-371b-a662-a370d455bc34 | -14.35641 | -47.12741 | 2025-10-02 04:04:00 | NOAA-21 | FLORES DE GOIÁS | GOIÁS | Brasil | 5207907 | 52 | 33 | nan | nan | nan | Cerrado | 2.2 |
| 737c62be-2506-3862-9f98-ab7aa59b4371 | -14.02669 | -47.98666 | 2025-10-02 04:04:00 | NOAA-21 | COLINAS DO SUL | GOIÁS | Brasil | 5205521 | 52 | 33 | nan | nan | nan | Cerrado | 3.7 |
| 6fd6c62c-baa5-37d0-83ce-e50a3935bf57 | -17.678 | -43.83207 | 2025-10-02 04:04:00 | NOAA-21 | BOCAIÚVA | MINAS GERAIS | Brasil | 3107307 | 31 | 33 | nan | nan | nan | Cerrado | 2.7 |
| 48d66a67-2864-3866-ae71-9db10e0c0249 | -13.70042 | -48.61529 | 2025-10-02 04:04:00 | NOAA-21 | CAMPINAÇU | GOIÁS | Brasil | 5204656 | 52 | 33 | nan | nan | nan | Cerrado | 7.9 |
| f6df9bc5-9fd5-3dc2-86a0-1fa06cd7fcbf | -14.22207 | -44.79206 | 2025-10-02 04:04:00 | NOAA-21 | COCOS | BAHIA | Brasil | 2908101 | 29 | 33 | nan | nan | nan | Cerrado | 2.4 |
| f349c966-fbbd-35f9-af4f-892c199eb99c | -14.48526 | -48.4507 | 2025-10-02 04:04:00 | NOAA-21 | NIQUELÂNDIA | GOIÁS | Brasil | 5214606 | 52 | 33 | nan | nan | nan | Cerrado | 4.0 |
| 74decbd8-2cd3-3ca6-bdbf-c0d7921bd7cb | -15.94654 | -43.33751 | 2025-10-02 04:04:00 | NOAA-21 | JANAÚBA | MINAS GERAIS | Brasil | 3135100 | 31 | 33 | nan | nan | nan | Cerrado | 12.0 |
| 2d1bdd93-5c37-3241-bb05-1632dd2f0656 | -14.97834 | -46.91799 | 2025-10-02 04:04:00 | NOAA-21 | FLORES DE GOIÁS | GOIÁS | Brasil | 5207907 | 52 | 33 | nan | nan | nan | Cerrado | 1.8 |
| 3aaf32cf-f269-3dcf-be65-8dd46a24e71a | -15.1385 | -46.44671 | 2025-10-02 04:04:00 | NOAA-21 | BURITIS | MINAS GERAIS | Brasil | 3109303 | 31 | 33 | nan | nan | nan | Cerrado | 2.1 |
| af2db109-f503-3afb-824c-f6e0ae048a55 | -12.57637 | -49.893 | 2025-10-02 04:04:00 | NOAA-21 | SANDOLÂNDIA | TOCANTINS | Brasil | 1718840 | 17 | 33 | nan | nan | nan | Cerrado | 1.5 |
| f993b66b-c319-3378-ad14-38696d433a76 | -14.00174 | -44.91549 | 2025-10-02 04:04:00 | NOAA-21 | JABORANDI | BAHIA | Brasil | 2917359 | 29 | 33 | nan | nan | nan | Cerrado | 1.7 |
| 5ebd9145-f086-3c75-8323-bb474aa882ab | -14.8979 | -48.33001 | 2025-10-02 04:04:00 | NOAA-21 | NIQUELÂNDIA | GOIÁS | Brasil | 5214606 | 52 | 33 | nan | nan | nan | Cerrado | 2.3 |
| b4ac808e-f64e-326e-9005-8c7a589e317c | -13.24222 | -47.33831 | 2025-10-02 04:04:00 | NOAA-21 | ARRAIAS | TOCANTINS | Brasil | 1702406 | 17 | 33 | nan | nan | nan | Cerrado | 3.8 |
| 7f869fcb-02f3-3386-a58e-fcedeeecae65 | -15.83282 | -42.62483 | 2025-10-02 04:04:00 | NOAA-21 | RIO PARDO DE MINAS | MINAS GERAIS | Brasil | 3155603 | 31 | 33 | nan | nan | nan | Mata Atlântica | 3.2 |
| cf3a3a37-7f7f-30f4-a4eb-ad1385521bda | -13.16724 | -47.82129 | 2025-10-02 04:04:00 | NOAA-21 | PARANÃ | TOCANTINS | Brasil | 1716208 | 17 | 33 | nan | nan | nan | Cerrado | 6.4 |
| 4a700318-0fcc-3ded-819c-2f3ab1a50265 | -14.86891 | -48.29325 | 2025-10-02 04:04:00 | NOAA-21 | NIQUELÂNDIA | GOIÁS | Brasil | 5214606 | 52 | 33 | nan | nan | nan | Cerrado | 3.6 |
| 7c145fbe-161e-3b35-9bb0-3d861b43d676 | -14.47507 | -48.43236 | 2025-10-02 04:04:00 | NOAA-21 | NIQUELÂNDIA | GOIÁS | Brasil | 5214606 | 52 | 33 | nan | nan | nan | Cerrado | 9.5 |
| bf366def-b81e-3668-8408-160135d3a293 | -14.90144 | -48.33512 | 2025-10-02 04:04:00 | NOAA-21 | NIQUELÂNDIA | GOIÁS | Brasil | 5214606 | 52 | 33 | nan | nan | nan | Cerrado | 5.4 |
| b9cc60e3-1eab-3f88-8a8a-bfadb022a590 | -13.91915 | -48.07553 | 2025-10-02 04:04:00 | NOAA-21 | COLINAS DO SUL | GOIÁS | Brasil | 5205521 | 52 | 33 | nan | nan | nan | Cerrado | 2.8 |
| 5a50b39f-2014-34fd-9696-f3fe1be3af35 | -13.86051 | -51.24363 | 2025-10-02 04:04:00 | NOAA-21 | COCALINHO | MATO GROSSO | Brasil | 5103106 | 51 | 33 | nan | nan | nan | Cerrado | 1.4 |
| dab89b91-ab57-3abd-b090-e229098d5115 | -13.93417 | -48.09126 | 2025-10-02 04:04:00 | NOAA-21 | COLINAS DO SUL | GOIÁS | Brasil | 5205521 | 52 | 33 | nan | nan | nan | Cerrado | 2.4 |
| 8050540a-33fa-39f4-b7f7-dc64f39a7589 | -19.71575 | -45.90941 | 2025-10-02 04:04:00 | NOAA-21 | LUZ | MINAS GERAIS | Brasil | 3138807 | 31 | 33 | nan | nan | nan | Cerrado | 2.1 |
| b413f256-3373-34e9-8212-8092b2129942 | -12.58138 | -49.89396 | 2025-10-02 04:04:00 | NOAA-21 | SANDOLÂNDIA | TOCANTINS | Brasil | 1718840 | 17 | 33 | nan | nan | nan | Cerrado | 1.1 |
| 6921005f-0d57-3f6a-8567-2a1c47f83e04 | -13.74409 | -48.70721 | 2025-10-02 04:04:00 | NOAA-21 | CAMPINAÇU | GOIÁS | Brasil | 5204656 | 52 | 33 | nan | nan | nan | Cerrado | 2.6 |
| 899e59e7-0460-30a6-9439-430accd57d6f | -20.49415 | -46.12421 | 2025-10-02 04:04:00 | NOAA-21 | PIUMHI | MINAS GERAIS | Brasil | 3151503 | 31 | 33 | nan | nan | nan | Cerrado | 1.7 |


[Clique aqui para ver as próximas entradas](README44.md)
