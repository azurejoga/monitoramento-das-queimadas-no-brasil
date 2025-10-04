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

## Dados Diários - Página 27

| ID | Latitude | Longitude | Data/Hora GMT | Satélite | Município | Estado | País | Município ID | Estado ID | País ID | Dias sem Chuva | Precipitação | Risco de Fogo | Bioma | FRP |
|----|----------|-----------|---------------|----------|-----------|--------|------|--------------|-----------|---------|----------------|--------------|----------------|-------|-----|
| e1e3ad93-9d5f-341d-925e-50e7e89d172c | -9.99723 | -48.27379 | 2025-10-04 03:51:00 | NPP-375D | PALMAS | TOCANTINS | Brasil | 1721000 | 17 | 33 | nan | nan | nan | Cerrado | 1.2 |
| 25f72f97-fd10-398d-b4f8-fc14ea380f8f | -6.36883 | -42.88649 | 2025-10-04 03:51:00 | NPP-375D | SÃO FRANCISCO DO MARANHÃO | MARANHÃO | Brasil | 2110906 | 21 | 33 | nan | nan | nan | Caatinga | 1.4 |
| 62d26b93-aed6-33ec-91cb-601c4340e7b8 | -8.21733 | -46.81073 | 2025-10-04 03:51:00 | NPP-375D | CAMPOS LINDOS | TOCANTINS | Brasil | 1703842 | 17 | 33 | nan | nan | nan | Cerrado | 2.0 |
| b1bf56a3-87d7-31d2-8077-51acfa91aafd | -6.27097 | -42.44967 | 2025-10-04 03:51:00 | NPP-375D | REGENERAÇÃO | PIAUÍ | Brasil | 2208809 | 22 | 33 | nan | nan | nan | Caatinga | 3.8 |
| b5679208-82a1-3f79-9b58-d6756a5e6455 | -7.70044 | -42.58371 | 2025-10-04 03:51:00 | NPP-375D | SOCORRO DO PIAUÍ | PIAUÍ | Brasil | 2210904 | 22 | 33 | nan | nan | nan | Caatinga | 2.1 |
| 1297a971-b89d-3b45-9e77-395b0e68aa2e | -6.669 | -42.82034 | 2025-10-04 03:51:00 | NPP-375D | FRANCISCO AYRES | PIAUÍ | Brasil | 2204105 | 22 | 33 | nan | nan | nan | Caatinga | 3.2 |
| 4866e38d-db39-33b1-abdb-52f11e0a8e4d | -6.22156 | -44.27974 | 2025-10-04 03:51:00 | NPP-375D | MIRADOR | MARANHÃO | Brasil | 2106706 | 21 | 33 | nan | nan | nan | Cerrado | 6.7 |
| a29c2642-68a8-36d3-af1a-1f86cf79b86a | -5.26657 | -39.25907 | 2025-10-04 03:51:00 | NPP-375D | QUIXERAMOBIM | CEARÁ | Brasil | 2311405 | 23 | 33 | nan | nan | nan | Caatinga | 1.2 |
| 537d1f25-038e-3177-ab62-4f8ad87d463a | -6.28496 | -42.44385 | 2025-10-04 03:51:00 | NPP-375D | REGENERAÇÃO | PIAUÍ | Brasil | 2208809 | 22 | 33 | nan | nan | nan | Caatinga | 1.5 |
| 37f4a4f4-424f-30a6-84b5-5dcc513f66b4 | -6.23089 | -44.65561 | 2025-10-04 03:51:00 | NPP-375D | MIRADOR | MARANHÃO | Brasil | 2106706 | 21 | 33 | nan | nan | nan | Cerrado | 5.8 |
| c95aa912-3cef-3cb1-91cb-8f0d3e4befdb | -6.07403 | -42.51915 | 2025-10-04 03:51:00 | NPP-375D | JARDIM DO MULATO | PIAUÍ | Brasil | 2205250 | 22 | 33 | nan | nan | nan | Caatinga | 39.2 |
| 31b93b03-cebf-3a36-9125-fdf66a04578a | -6.36017 | -42.88491 | 2025-10-04 03:51:00 | NPP-375D | SÃO FRANCISCO DO MARANHÃO | MARANHÃO | Brasil | 2110906 | 21 | 33 | nan | nan | nan | Caatinga | 2.9 |
| 65f84169-6cde-3a76-90c4-f58573954fc5 | -4.4368 | -43.24021 | 2025-10-04 03:51:00 | NPP-375D | ALDEIAS ALTAS | MARANHÃO | Brasil | 2100303 | 21 | 33 | nan | nan | nan | Cerrado | 6.1 |
| 39e6f6f7-eb8f-3b77-8fb3-5aafea188caa | -5.52717 | -44.39365 | 2025-10-04 03:51:00 | NPP-375D | SÃO DOMINGOS DO MARANHÃO | MARANHÃO | Brasil | 2110708 | 21 | 33 | nan | nan | nan | Cerrado | 1.7 |
| 6050cb2c-848c-306d-bc1c-e30828df4679 | -4.64325 | -43.18292 | 2025-10-04 03:51:00 | NPP-375D | CAXIAS | MARANHÃO | Brasil | 2103000 | 21 | 33 | nan | nan | nan | Cerrado | 1.9 |
| 76b5a8c2-6be8-3fec-a8f4-15c518f87b9f | -11.46921 | -45.13818 | 2025-10-04 03:51:00 | NPP-375D | RIACHÃO DAS NEVES | BAHIA | Brasil | 2926202 | 29 | 33 | nan | nan | nan | Cerrado | 1.6 |
| 9c073954-6888-351d-85b9-3461db399353 | -7.24628 | -48.48052 | 2025-10-04 03:51:00 | NPP-375D | ARAGUAÍNA | TOCANTINS | Brasil | 1702109 | 17 | 33 | nan | nan | nan | Cerrado | 1.2 |
| 9af5941b-c336-37f1-b1c4-6d3a09576817 | -7.86377 | -48.20646 | 2025-10-04 03:51:00 | NPP-375D | PALMEIRANTE | TOCANTINS | Brasil | 1715705 | 17 | 33 | nan | nan | nan | Cerrado | 2.6 |
| 01f96f77-5f51-3dce-a0bf-d460b75011fb | -6.87701 | -47.24385 | 2025-10-04 03:51:00 | NPP-375D | ESTREITO | MARANHÃO | Brasil | 2104057 | 21 | 33 | nan | nan | nan | Cerrado | 14.3 |
| 19e55110-6285-37ed-91cf-1fcf0a448c40 | -11.47768 | -45.01562 | 2025-10-04 03:51:00 | NPP-375D | RIACHÃO DAS NEVES | BAHIA | Brasil | 2926202 | 29 | 33 | nan | nan | nan | Cerrado | 3.8 |
| 94441154-e564-3035-8446-d06a24a74678 | -5.30738 | -45.56211 | 2025-10-04 03:51:00 | NPP-375D | JENIPAPO DOS VIEIRAS | MARANHÃO | Brasil | 2105476 | 21 | 33 | nan | nan | nan | Cerrado | 1.7 |
| ce39e8e9-2885-346f-8d2a-aa40dd53c0e6 | -5.48636 | -44.10969 | 2025-10-04 03:51:00 | NPP-375D | GOVERNADOR LUIZ ROCHA | MARANHÃO | Brasil | 2104628 | 21 | 33 | nan | nan | nan | Cerrado | 10.1 |
| 0f40b902-7e18-3c88-872e-9efd11827817 | -6.2473 | -45.33973 | 2025-10-04 03:51:00 | NPP-375D | FERNANDO FALCÃO | MARANHÃO | Brasil | 2104081 | 21 | 33 | nan | nan | nan | Cerrado | 3.5 |
| cd08c6da-4399-3e42-9258-944e8595f12e | -6.15956 | -44.61922 | 2025-10-04 03:51:00 | NPP-375D | MIRADOR | MARANHÃO | Brasil | 2106706 | 21 | 33 | nan | nan | nan | Cerrado | 2.0 |
| 28904d9d-265e-39f3-aa22-63d30253708e | -7.16159 | -44.99726 | 2025-10-04 03:51:00 | NPP-375D | SÃO FÉLIX DE BALSAS | MARANHÃO | Brasil | 2110807 | 21 | 33 | nan | nan | nan | Cerrado | 8.3 |
| baf8702f-47d6-32f2-969e-ebedf0154cbb | -7.05204 | -42.78426 | 2025-10-04 03:51:00 | NPP-375D | NAZARÉ DO PIAUÍ | PIAUÍ | Brasil | 2206704 | 22 | 33 | nan | nan | nan | Caatinga | 2.2 |
| 02edf23f-75c0-397d-92b5-25df3af8707a | -11.43928 | -43.49762 | 2025-10-04 03:51:00 | NPP-375D | BARRA | BAHIA | Brasil | 2902708 | 29 | 33 | nan | nan | nan | Cerrado | 0.9 |
| 60fb3cbb-8129-3958-ab21-98ae3c819444 | -6.34677 | -43.45415 | 2025-10-04 03:51:00 | NPP-375D | SUCUPIRA DO RIACHÃO | MARANHÃO | Brasil | 2111953 | 21 | 33 | nan | nan | nan | Cerrado | 1.5 |
| fed23b2c-9a33-3c43-b398-1b0521e3b09d | -7.76727 | -42.51792 | 2025-10-04 03:51:00 | NPP-375D | SÃO JOSÉ DO PEIXE | PIAUÍ | Brasil | 2210102 | 22 | 33 | nan | nan | nan | Caatinga | 1.0 |
| 84b7e53c-7d38-3e6f-9924-3f7fbbcd9de0 | -9.94584 | -43.74828 | 2025-10-04 03:51:00 | NPP-375D | MORRO CABEÇA NO TEMPO | PIAUÍ | Brasil | 2206654 | 22 | 33 | nan | nan | nan | Caatinga | 1.6 |
| 78b99805-0e73-3f2d-9694-8f824135906a | -8.5632 | -44.6451 | 2025-10-04 03:51:00 | NPP-375D | PALMEIRA DO PIAUÍ | PIAUÍ | Brasil | 2207405 | 22 | 33 | nan | nan | nan | Cerrado | 1.4 |
| 99de334d-fb2c-3521-954e-f6441a799583 | -7.0442 | -42.77883 | 2025-10-04 03:51:00 | NPP-375D | NAZARÉ DO PIAUÍ | PIAUÍ | Brasil | 2206704 | 22 | 33 | nan | nan | nan | Caatinga | 2.5 |
| b82a15b0-ae0c-3419-aa7d-04213a451df5 | -6.87382 | -44.49822 | 2025-10-04 03:51:00 | NPP-375D | SÃO DOMINGOS DO AZEITÃO | MARANHÃO | Brasil | 2110658 | 21 | 33 | nan | nan | nan | Cerrado | 5.7 |
| 594971bd-aa2a-3471-bc2d-9596c9e1126b | -7.31534 | -42.89334 | 2025-10-04 03:51:00 | NPP-375D | FLORIANO | PIAUÍ | Brasil | 2203909 | 22 | 33 | nan | nan | nan | Caatinga | 0.8 |
| c2abf623-fe7b-3175-81b6-257a3b837eb4 | -6.1654 | -44.61448 | 2025-10-04 03:51:00 | NPP-375D | MIRADOR | MARANHÃO | Brasil | 2106706 | 21 | 33 | nan | nan | nan | Cerrado | 2.0 |
| e2cdcd53-a9f1-3be9-971e-ddf91973af50 | -9.34661 | -45.76892 | 2025-10-04 03:51:00 | NPP-375D | SANTA FILOMENA | PIAUÍ | Brasil | 2209203 | 22 | 33 | nan | nan | nan | Cerrado | 3.4 |
| eabdba94-780a-35f0-a06e-9f00842a0bb0 | -11.71959 | -44.43979 | 2025-10-04 03:51:00 | NPP-375D | COTEGIPE | BAHIA | Brasil | 2909406 | 29 | 33 | nan | nan | nan | Cerrado | 1.2 |
| 60d1244a-85b5-3416-8e57-e65070c25014 | -8.17301 | -34.98017 | 2025-10-04 03:51:00 | NPP-375D | JABOATÃO DOS GUARARAPES | PERNAMBUCO | Brasil | 2607901 | 26 | 33 | nan | nan | nan | Mata Atlântica | 0.5 |
| c369124b-5d4b-3e35-8478-0bb4048362e1 | -7.75326 | -42.55015 | 2025-10-04 03:51:00 | NPP-375D | SÃO JOSÉ DO PEIXE | PIAUÍ | Brasil | 2210102 | 22 | 33 | nan | nan | nan | Caatinga | 3.9 |
| c111e61c-733d-3d1d-b592-3180515d01f1 | -5.82549 | -42.88165 | 2025-10-04 03:51:00 | NPP-375D | PALMEIRAIS | PIAUÍ | Brasil | 2207504 | 22 | 33 | nan | nan | nan | Caatinga | 2.4 |
| c335256c-fb80-35ca-962f-befa57c477c2 | -9.33574 | -45.65869 | 2025-10-04 03:51:00 | NPP-375D | SANTA FILOMENA | PIAUÍ | Brasil | 2209203 | 22 | 33 | nan | nan | nan | Cerrado | 4.8 |
| 61f94075-3983-3ed8-99e0-00911b5fb1b8 | -10.53591 | -44.51062 | 2025-10-04 03:51:00 | NPP-375D | PARNAGUÁ | PIAUÍ | Brasil | 2207603 | 22 | 33 | nan | nan | nan | Cerrado | 0.4 |
| f7321b3a-55a1-3a05-8f3c-2d9fc0e89901 | -5.68941 | -42.83599 | 2025-10-04 03:51:00 | NPP-375D | SÃO PEDRO DO PIAUÍ | PIAUÍ | Brasil | 2210508 | 22 | 33 | nan | nan | nan | Caatinga | 4.6 |
| 930e9a23-e00f-36cf-b343-d6fc9c918edd | -5.72488 | -42.68124 | 2025-10-04 03:51:00 | NPP-375D | MIGUEL LEÃO | PIAUÍ | Brasil | 2206308 | 22 | 33 | nan | nan | nan | Caatinga | 2.7 |
| bd83a725-f750-33f7-8ed1-f782576ee5db | -6.34889 | -43.46144 | 2025-10-04 03:51:00 | NPP-375D | SUCUPIRA DO RIACHÃO | MARANHÃO | Brasil | 2111953 | 21 | 33 | nan | nan | nan | Cerrado | 7.1 |
| 2bd14a24-56d1-3003-94ae-70ca093c3a8c | -9.95312 | -43.65557 | 2025-10-04 03:51:00 | NPP-375D | PILÃO ARCADO | BAHIA | Brasil | 2924405 | 29 | 33 | nan | nan | nan | Cerrado | 2.2 |
| 435af6b1-2079-39b3-99b3-3a134af97cb2 | -6.34225 | -43.45345 | 2025-10-04 03:51:00 | NPP-375D | SUCUPIRA DO RIACHÃO | MARANHÃO | Brasil | 2111953 | 21 | 33 | nan | nan | nan | Cerrado | 1.5 |
| 757742e9-279e-3eb9-9b28-b161c475666e | -11.07898 | -47.72378 | 2025-10-04 03:51:00 | NPP-375D | SILVANÓPOLIS | TOCANTINS | Brasil | 1720655 | 17 | 33 | nan | nan | nan | Cerrado | 1.6 |
| 68bde844-19bb-3e62-abc2-a5b82e3bc33e | -7.70787 | -42.56557 | 2025-10-04 03:51:00 | NPP-375D | SÃO JOSÉ DO PEIXE | PIAUÍ | Brasil | 2210102 | 22 | 33 | nan | nan | nan | Caatinga | 2.6 |
| 48345644-d27e-3949-8e28-af3179a1d23c | -10.98622 | -46.66992 | 2025-10-04 03:51:00 | NPP-375D | MATEIROS | TOCANTINS | Brasil | 1712702 | 17 | 33 | nan | nan | nan | Cerrado | 1.0 |
| cfc6efed-5291-356f-9154-e387e5475f1a | -7.78282 | -42.50148 | 2025-10-04 03:51:00 | NPP-375D | SÃO JOSÉ DO PEIXE | PIAUÍ | Brasil | 2210102 | 22 | 33 | nan | nan | nan | Caatinga | 2.7 |
| 9e7a9ef6-514f-3f7e-8eef-bcafe50ce33d | -7.74124 | -46.31582 | 2025-10-04 03:51:00 | NPP-375D | BALSAS | MARANHÃO | Brasil | 2101400 | 21 | 33 | nan | nan | nan | Cerrado | 19.1 |
| 180ab6d2-788d-3953-9dd7-2f408e562ae9 | -11.08265 | -47.88266 | 2025-10-04 03:51:00 | NPP-375D | MONTE DO CARMO | TOCANTINS | Brasil | 1713601 | 17 | 33 | nan | nan | nan | Cerrado | 3.2 |
| 1e022d39-3cd1-332b-b094-9dd0f602b0b6 | -6.66511 | -44.20143 | 2025-10-04 03:51:00 | NPP-375D | PASTOS BONS | MARANHÃO | Brasil | 2108009 | 21 | 33 | nan | nan | nan | Cerrado | 2.0 |
| 7e8f2a32-4899-37e0-a5a3-5507e28676f8 | -10.0291 | -44.02152 | 2025-10-04 03:51:00 | NPP-375D | AVELINO LOPES | PIAUÍ | Brasil | 2201101 | 22 | 33 | nan | nan | nan | Cerrado | 2.0 |
| 0ee2ccc3-1296-3923-b810-43388229ee7c | -6.23497 | -45.3499 | 2025-10-04 03:51:00 | NPP-375D | FERNANDO FALCÃO | MARANHÃO | Brasil | 2104081 | 21 | 33 | nan | nan | nan | Cerrado | 1.7 |
| 05f4b768-cbb4-3e7c-93b7-4640eff955a8 | -6.66248 | -42.82107 | 2025-10-04 03:51:00 | NPP-375D | FRANCISCO AYRES | PIAUÍ | Brasil | 2204105 | 22 | 33 | nan | nan | nan | Caatinga | 3.9 |
| 11cbdda6-c84e-3110-ad23-4761f4a0d7f6 | -9.08532 | -48.02836 | 2025-10-04 03:51:00 | NPP-375D | BOM JESUS DO TOCANTINS | TOCANTINS | Brasil | 1703305 | 17 | 33 | nan | nan | nan | Cerrado | 2.0 |
| 1fe7882a-5656-3a34-a19e-45048025c448 | -5.83932 | -42.87977 | 2025-10-04 03:51:00 | NPP-375D | PALMEIRAIS | PIAUÍ | Brasil | 2207504 | 22 | 33 | nan | nan | nan | Caatinga | 1.7 |
| f1746013-64f8-32fa-a44d-cbdb87962e2e | -6.71676 | -42.79976 | 2025-10-04 03:51:00 | NPP-375D | FRANCISCO AYRES | PIAUÍ | Brasil | 2204105 | 22 | 33 | nan | nan | nan | Caatinga | 2.3 |
| 714f9555-4ceb-35b9-b8c9-115996c928e2 | -8.90578 | -46.59994 | 2025-10-04 03:51:00 | NPP-375D | BALSAS | MARANHÃO | Brasil | 2101400 | 21 | 33 | nan | nan | nan | Cerrado | 1.8 |
| 78cc9a44-135f-3f89-915c-39961a9b77c0 | -6.8714 | -47.24036 | 2025-10-04 03:51:00 | NPP-375D | ESTREITO | MARANHÃO | Brasil | 2104057 | 21 | 33 | nan | nan | nan | Cerrado | 4.7 |
| 9ce10dff-4d1b-3c9b-9ddc-f997a734b2f4 | -9.90685 | -43.7413 | 2025-10-04 03:51:00 | NPP-375D | MORRO CABEÇA NO TEMPO | PIAUÍ | Brasil | 2206654 | 22 | 33 | nan | nan | nan | Caatinga | 3.7 |
| ef805e24-b1d3-306b-9ab9-607149a28e26 | -6.23755 | -45.34488 | 2025-10-04 03:51:00 | NPP-375D | FERNANDO FALCÃO | MARANHÃO | Brasil | 2104081 | 21 | 33 | nan | nan | nan | Cerrado | 1.1 |
| a6a289ee-f128-3cf8-b58d-5e91dde0836f | -5.95575 | -43.48958 | 2025-10-04 03:51:00 | NPP-375D | LAGOA DO MATO | MARANHÃO | Brasil | 2105922 | 21 | 33 | nan | nan | nan | Cerrado | 3.8 |
| 68a339bc-96e4-356a-a7f5-489f6563e817 | -5.22821 | -43.70769 | 2025-10-04 03:51:00 | NPP-375D | CAXIAS | MARANHÃO | Brasil | 2103000 | 21 | 33 | nan | nan | nan | Cerrado | 4.3 |
| f576413c-073f-33ef-824d-6e046b9b7987 | -7.78758 | -42.4985 | 2025-10-04 03:51:00 | NPP-375D | SÃO JOSÉ DO PEIXE | PIAUÍ | Brasil | 2210102 | 22 | 33 | nan | nan | nan | Caatinga | 2.7 |
| cfbfcd84-e818-3915-9f23-8b27f26baa62 | -5.83496 | -42.87893 | 2025-10-04 03:51:00 | NPP-375D | PALMEIRAIS | PIAUÍ | Brasil | 2207504 | 22 | 33 | nan | nan | nan | Caatinga | 4.0 |
| 6e411101-1dd3-3e8f-a7f7-a641a18aa53c | -4.48085 | -42.86303 | 2025-10-04 03:51:00 | NPP-375D | CAXIAS | MARANHÃO | Brasil | 2103000 | 21 | 33 | nan | nan | nan | Cerrado | 5.8 |
| c01a0599-14df-3ab9-9482-d226d952d974 | -6.66909 | -42.83448 | 2025-10-04 03:51:00 | NPP-375D | AMARANTE | PIAUÍ | Brasil | 2200509 | 22 | 33 | nan | nan | nan | Caatinga | 2.7 |
| 72a91913-5619-3cea-9ca5-d3e9469a41e7 | -8.52765 | -47.2135 | 2025-10-04 03:51:00 | NPP-375D | RECURSOLÂNDIA | TOCANTINS | Brasil | 1718501 | 17 | 33 | nan | nan | nan | Cerrado | 1.0 |
| ba6d7f2a-653a-358d-a74e-e0d9ca3e44de | -7.74912 | -42.54939 | 2025-10-04 03:51:00 | NPP-375D | SÃO JOSÉ DO PEIXE | PIAUÍ | Brasil | 2210102 | 22 | 33 | nan | nan | nan | Caatinga | 3.9 |
| 7c775b66-f728-37c6-88d9-41f2e9e933ef | -6.99868 | -42.80015 | 2025-10-04 03:51:00 | NPP-375D | NAZARÉ DO PIAUÍ | PIAUÍ | Brasil | 2206704 | 22 | 33 | nan | nan | nan | Caatinga | 1.2 |
| 651c154b-d0e0-368d-808c-c9e81f46596d | -5.68433 | -42.83951 | 2025-10-04 03:51:00 | NPP-375D | SÃO PEDRO DO PIAUÍ | PIAUÍ | Brasil | 2210508 | 22 | 33 | nan | nan | nan | Caatinga | 3.6 |
| 542b93dc-5767-396f-b3ed-0ecefa659835 | -6.99442 | -42.79938 | 2025-10-04 03:51:00 | NPP-375D | NAZARÉ DO PIAUÍ | PIAUÍ | Brasil | 2206704 | 22 | 33 | nan | nan | nan | Caatinga | 1.2 |
| f43d6a23-4ff5-3b10-a35e-be636603ddc7 | -7.78077 | -42.58972 | 2025-10-04 03:51:00 | NPP-375D | SOCORRO DO PIAUÍ | PIAUÍ | Brasil | 2210904 | 22 | 33 | nan | nan | nan | Caatinga | 3.5 |
| b06ce483-fb14-3a95-a1bb-a5019e51b4f4 | -7.55945 | -42.39426 | 2025-10-04 03:51:00 | NPP-375D | SÃO MIGUEL DO FIDALGO | PIAUÍ | Brasil | 2210391 | 22 | 33 | nan | nan | nan | Caatinga | 1.6 |
| a7da7916-3d97-3a15-b135-2ed95e739db3 | -10.32054 | -50.34107 | 2025-10-04 03:51:00 | NPP-375D | PIUM | TOCANTINS | Brasil | 1717503 | 17 | 33 | nan | nan | nan | Cerrado | 17.6 |
| 2af83dd9-d706-3df6-87c5-fe791ce669c5 | -4.70069 | -45.60378 | 2025-10-04 03:51:00 | NPP-375D | MARAJÁ DO SENA | MARANHÃO | Brasil | 2106359 | 21 | 33 | nan | nan | nan | Cerrado | 1.1 |
| fe3ecf60-e554-32cb-b371-79156cdf8af8 | -11.15201 | -43.38414 | 2025-10-04 03:51:00 | NPP-375D | BARRA | BAHIA | Brasil | 2902708 | 29 | 33 | nan | nan | nan | Caatinga | 1.3 |
| 52b3eb31-b6ec-3bcb-a766-c97eb753bef6 | -9.99057 | -48.28379 | 2025-10-04 03:51:00 | NPP-375D | PALMAS | TOCANTINS | Brasil | 1721000 | 17 | 33 | nan | nan | nan | Cerrado | 1.3 |
| 1217a8d2-b35e-3b01-b2c3-cad944e6a949 | -11.08203 | -47.88589 | 2025-10-04 03:51:00 | NPP-375D | MONTE DO CARMO | TOCANTINS | Brasil | 1713601 | 17 | 33 | nan | nan | nan | Cerrado | 3.1 |
| 5c18d021-ee22-3ff3-9a96-ea4905b3a3a6 | -6.35039 | -43.45244 | 2025-10-04 03:51:00 | NPP-375D | SUCUPIRA DO RIACHÃO | MARANHÃO | Brasil | 2111953 | 21 | 33 | nan | nan | nan | Cerrado | 2.6 |
| 1a40e499-fad2-34b3-96d8-3cd77a2686a5 | -10.53426 | -44.51978 | 2025-10-04 03:51:00 | NPP-375D | PARNAGUÁ | PIAUÍ | Brasil | 2207603 | 22 | 33 | nan | nan | nan | Cerrado | 1.2 |
| 87fd47b3-257d-3bd2-9947-e59088b33201 | -11.0613 | -47.78471 | 2025-10-04 03:51:00 | NPP-375D | SILVANÓPOLIS | TOCANTINS | Brasil | 1720655 | 17 | 33 | nan | nan | nan | Cerrado | 2.1 |
| 432f650a-74ae-3841-97ac-ca8e12c18b6e | -11.43233 | -43.48858 | 2025-10-04 03:51:00 | NPP-375D | BARRA | BAHIA | Brasil | 2902708 | 29 | 33 | nan | nan | nan | Cerrado | 2.1 |
| 263b9c59-d9cc-375c-bf28-aff54bc90324 | -5.72798 | -42.68349 | 2025-10-04 03:51:00 | NPP-375D | MIGUEL LEÃO | PIAUÍ | Brasil | 2206308 | 22 | 33 | nan | nan | nan | Caatinga | 5.4 |
| 8266e55f-dff7-333e-b41d-d82c5960c662 | -11.0574 | -40.93396 | 2025-10-04 03:51:00 | NPP-375D | VÁRZEA NOVA | BAHIA | Brasil | 2933158 | 29 | 33 | nan | nan | nan | Caatinga | 0.8 |
| a34318f8-9a75-3ed4-bc57-b16ba9c83e12 | -4.64249 | -43.18753 | 2025-10-04 03:51:00 | NPP-375D | CAXIAS | MARANHÃO | Brasil | 2103000 | 21 | 33 | nan | nan | nan | Cerrado | 2.0 |
| 8bb798cd-6b7b-3d9a-874e-6b9fc230951e | -7.04777 | -42.78355 | 2025-10-04 03:51:00 | NPP-375D | NAZARÉ DO PIAUÍ | PIAUÍ | Brasil | 2206704 | 22 | 33 | nan | nan | nan | Caatinga | 2.5 |
| 74d6f52a-c1b8-3072-bf4b-d79ad22aa74e | -6.98589 | -42.79781 | 2025-10-04 03:51:00 | NPP-375D | NAZARÉ DO PIAUÍ | PIAUÍ | Brasil | 2206704 | 22 | 33 | nan | nan | nan | Caatinga | 3.3 |
| 26b813e4-5188-3929-9875-c99f283062a1 | -8.91986 | -46.61372 | 2025-10-04 03:51:00 | NPP-375D | BALSAS | MARANHÃO | Brasil | 2101400 | 21 | 33 | nan | nan | nan | Cerrado | 0.9 |
| 235afe18-b518-30bd-b47a-1164c6321af8 | -5.69167 | -42.84951 | 2025-10-04 03:51:00 | NPP-375D | SÃO PEDRO DO PIAUÍ | PIAUÍ | Brasil | 2210508 | 22 | 33 | nan | nan | nan | Caatinga | 6.8 |
| f9366021-5035-32af-a269-ddda83f45d57 | -5.89763 | -38.48736 | 2025-10-04 03:51:00 | NPP-375D | PEREIRO | CEARÁ | Brasil | 2310803 | 23 | 33 | nan | nan | nan | Caatinga | 0.8 |
| bc9dfb15-cf35-32ed-9ef0-b96a4281976c | -11.46832 | -45.14293 | 2025-10-04 03:51:00 | NPP-375D | RIACHÃO DAS NEVES | BAHIA | Brasil | 2926202 | 29 | 33 | nan | nan | nan | Cerrado | 2.1 |
| 6419e1ac-c79c-369a-9e57-05a423be14a3 | -6.27584 | -42.44651 | 2025-10-04 03:51:00 | NPP-375D | REGENERAÇÃO | PIAUÍ | Brasil | 2208809 | 22 | 33 | nan | nan | nan | Caatinga | 2.2 |
| 9867cbbb-e4c7-3d31-8422-048afaee6908 | -9.66273 | -42.93712 | 2025-10-04 03:51:00 | NPP-375D | CAMPO ALEGRE DE LOURDES | BAHIA | Brasil | 2905909 | 29 | 33 | nan | nan | nan | Caatinga | 2.4 |
| 79528538-cbb3-3934-a99e-2f189c33dad8 | -9.34325 | -45.78747 | 2025-10-04 03:51:00 | NPP-375D | SANTA FILOMENA | PIAUÍ | Brasil | 2209203 | 22 | 33 | nan | nan | nan | Cerrado | 5.8 |
| 70b93fe1-1862-3f1b-b7ff-d51156b092e3 | -4.71777 | -46.13118 | 2025-10-04 03:51:00 | NPP-375D | SANTA LUZIA | MARANHÃO | Brasil | 2110005 | 21 | 33 | nan | nan | nan | Amazônia | 1.7 |
| 208ec4eb-00b0-3a6a-9e36-b4b6aa74d4e3 | -7.79541 | -42.55336 | 2025-10-04 03:51:00 | NPP-375D | SOCORRO DO PIAUÍ | PIAUÍ | Brasil | 2210904 | 22 | 33 | nan | nan | nan | Caatinga | 1.3 |


[Clique aqui para ver as próximas entradas](README28.md)
