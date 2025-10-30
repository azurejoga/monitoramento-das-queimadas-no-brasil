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

## Dados Diários - Página 24

| ID | Latitude | Longitude | Data/Hora GMT | Satélite | Município | Estado | País | Município ID | Estado ID | País ID | Dias sem Chuva | Precipitação | Risco de Fogo | Bioma | FRP |
|----|----------|-----------|---------------|----------|-----------|--------|------|--------------|-----------|---------|----------------|--------------|----------------|-------|-----|
| 4b635c75-0fe2-3c53-a445-ec54503a1b2c | -5.75905 | -42.8602 | 2025-10-30 04:04:00 | NPP-375D | SÃO PEDRO DO PIAUÍ | PIAUÍ | Brasil | 2210508 | 22 | 33 | nan | nan | nan | Caatinga | 6.1 |
| ac269142-74fb-3ffa-b671-3b5bda7bbb45 | -5.6108 | -47.12296 | 2025-10-30 04:04:00 | NPP-375D | BURITIRANA | MARANHÃO | Brasil | 2102358 | 21 | 33 | nan | nan | nan | Cerrado | 2.9 |
| 54e1d18a-aaec-3289-b647-fc527b3936a5 | -7.65013 | -42.2495 | 2025-10-30 04:04:00 | NPP-375D | SIMPLÍCIO MENDES | PIAUÍ | Brasil | 2210805 | 22 | 33 | nan | nan | nan | Caatinga | 0.8 |
| 3187793c-6365-37e0-bfc1-335a8deb51fa | -3.84143 | -49.37807 | 2025-10-30 04:04:00 | NPP-375D | BREU BRANCO | PARÁ | Brasil | 1501782 | 15 | 33 | nan | nan | nan | Amazônia | 4.5 |
| 2987a7c1-820b-3155-a807-e352fc33351c | -6.15962 | -41.61279 | 2025-10-30 04:04:00 | NPP-375D | PIMENTEIRAS | PIAUÍ | Brasil | 2208106 | 22 | 33 | nan | nan | nan | Caatinga | 0.9 |
| f40a6c38-fea4-3dad-a375-ca5b89a003e7 | -4.48815 | -43.43397 | 2025-10-30 04:04:00 | NPP-375D | ALDEIAS ALTAS | MARANHÃO | Brasil | 2100303 | 21 | 33 | nan | nan | nan | Cerrado | 2.0 |
| 8ddd0312-c70c-34d5-8e94-961361062ea1 | -6.12328 | -41.86209 | 2025-10-30 04:04:00 | NPP-375D | AROAZES | PIAUÍ | Brasil | 2200905 | 22 | 33 | nan | nan | nan | Caatinga | 4.0 |
| faaa50fb-eb47-3037-9762-4946f9b8e255 | -6.1421 | -41.5912 | 2025-10-30 04:04:00 | NPP-375D | PIMENTEIRAS | PIAUÍ | Brasil | 2208106 | 22 | 33 | nan | nan | nan | Caatinga | 1.3 |
| a8f7c7f0-506d-355a-886e-ba82299c3b72 | -6.1781 | -41.67219 | 2025-10-30 04:04:00 | NPP-375D | PIMENTEIRAS | PIAUÍ | Brasil | 2208106 | 22 | 33 | nan | nan | nan | Caatinga | 0.8 |
| 94cd6c27-8d2e-371b-bf69-271b4720b1a6 | -7.00348 | -39.12034 | 2025-10-30 04:04:00 | NPP-375D | AURORA | CEARÁ | Brasil | 2301703 | 23 | 33 | nan | nan | nan | Caatinga | 1.0 |
| f4269a07-02b8-3b7f-b83e-1d04ca1d15e6 | -5.7943 | -40.82114 | 2025-10-30 04:04:00 | NPP-375D | QUITERIANÓPOLIS | CEARÁ | Brasil | 2311264 | 23 | 33 | nan | nan | nan | Caatinga | 1.9 |
| b3ca35cf-f978-36c9-8182-541b2511275f | -7.8682 | -44.23839 | 2025-10-30 04:04:00 | NPP-375D | SEBASTIÃO LEAL | PIAUÍ | Brasil | 2210631 | 22 | 33 | nan | nan | nan | Cerrado | 2.0 |
| 49ed1d5c-4511-30b0-920f-85fc4692b2f7 | -4.98135 | -45.03843 | 2025-10-30 04:04:00 | NPP-375D | SÃO ROBERTO | MARANHÃO | Brasil | 2111672 | 21 | 33 | nan | nan | nan | Cerrado | 1.4 |
| 9b47ff36-895e-3411-8fae-9950bf47808c | -7.38424 | -43.01252 | 2025-10-30 04:04:00 | NPP-375D | ITAUEIRA | PIAUÍ | Brasil | 2205102 | 22 | 33 | nan | nan | nan | Caatinga | 2.7 |
| cecca168-cb02-3791-8d26-126e8db6545a | -4.84332 | -45.4226 | 2025-10-30 04:04:00 | NPP-375D | LAGOA GRANDE DO MARANHÃO | MARANHÃO | Brasil | 2105963 | 21 | 33 | nan | nan | nan | Cerrado | 4.2 |
| 205c77ad-cb93-3af0-bec7-221ca2f65f72 | -5.51267 | -46.23686 | 2025-10-30 04:04:00 | NPP-375D | GRAJAÚ | MARANHÃO | Brasil | 2104800 | 21 | 33 | nan | nan | nan | Amazônia | 1.7 |
| 592ab7ea-1c70-3dea-bdef-7ee6a6828caa | -4.67063 | -43.26398 | 2025-10-30 04:04:00 | NPP-375D | ALDEIAS ALTAS | MARANHÃO | Brasil | 2100303 | 21 | 33 | nan | nan | nan | Cerrado | 2.4 |
| 52e28e1d-8777-3004-8f6a-57e8e73c714b | -5.63568 | -41.54962 | 2025-10-30 04:04:00 | NPP-375D | SÃO MIGUEL DO TAPUIO | PIAUÍ | Brasil | 2210409 | 22 | 33 | nan | nan | nan | Caatinga | 1.1 |
| 51b410c4-0f70-36a9-be17-67bd1cd165c4 | -4.35979 | -48.19736 | 2025-10-30 04:04:00 | NPP-375D | RONDON DO PARÁ | PARÁ | Brasil | 1506187 | 15 | 33 | nan | nan | nan | Amazônia | 0.6 |
| 54f69f22-363c-3ab1-883c-9c067d5e6998 | -5.13366 | -43.81116 | 2025-10-30 04:04:00 | NPP-375D | SÃO JOÃO DO SOTER | MARANHÃO | Brasil | 2111078 | 21 | 33 | nan | nan | nan | Cerrado | 1.2 |
| 77eb4186-0862-3bcf-8dc9-2426b7dd6e9d | -6.12035 | -41.70479 | 2025-10-30 04:04:00 | NPP-375D | AROAZES | PIAUÍ | Brasil | 2200905 | 22 | 33 | nan | nan | nan | Caatinga | 2.0 |
| c3cac980-338e-3508-b90e-9141e582fc04 | -6.16503 | -41.66662 | 2025-10-30 04:04:00 | NPP-375D | PIMENTEIRAS | PIAUÍ | Brasil | 2208106 | 22 | 33 | nan | nan | nan | Caatinga | 1.7 |
| 181fa022-756e-3806-9a2e-3a4f581603fe | -3.12358 | -45.70677 | 2025-10-30 04:04:00 | NPP-375D | ZÉ DOCA | MARANHÃO | Brasil | 2114007 | 21 | 33 | nan | nan | nan | Amazônia | 0.9 |
| 6ff67738-8458-387f-8b25-aef0bcb2aaf1 | -3.67411 | -47.62662 | 2025-10-30 04:04:00 | NPP-375D | ULIANÓPOLIS | PARÁ | Brasil | 1508126 | 15 | 33 | nan | nan | nan | Amazônia | 3.2 |
| 7142bf6e-d9d8-3c26-81cd-4add9ca8f7ee | -6.70976 | -38.21753 | 2025-10-30 04:04:00 | NPP-375D | SOUSA | PARAÍBA | Brasil | 2516201 | 25 | 33 | nan | nan | nan | Caatinga | 1.7 |
| 0266ef45-5154-38c8-9b63-dc001210d665 | -3.80187 | -43.90209 | 2025-10-30 04:04:00 | NPP-375D | VARGEM GRANDE | MARANHÃO | Brasil | 2112704 | 21 | 33 | nan | nan | nan | Cerrado | 4.0 |
| 2b4e6dc6-1730-3135-8aae-d024bace1d97 | -7.32857 | -42.49141 | 2025-10-30 04:04:00 | NPP-375D | SÃO FRANCISCO DO PIAUÍ | PIAUÍ | Brasil | 2209708 | 22 | 33 | nan | nan | nan | Caatinga | 4.1 |
| f5e48f9e-d1fb-3809-a3d5-fdad840017b3 | -6.13463 | -41.70324 | 2025-10-30 04:04:00 | NPP-375D | AROAZES | PIAUÍ | Brasil | 2200905 | 22 | 33 | nan | nan | nan | Caatinga | 3.0 |
| 1a884599-6606-3905-b67b-ddb6038821b9 | -5.43618 | -45.33817 | 2025-10-30 04:04:00 | NPP-375D | BARRA DO CORDA | MARANHÃO | Brasil | 2101608 | 21 | 33 | nan | nan | nan | Cerrado | 4.0 |
| 975525dd-2e88-3688-b714-80e397330d8d | -4.25899 | -43.70217 | 2025-10-30 04:04:00 | NPP-375D | CODÓ | MARANHÃO | Brasil | 2103307 | 21 | 33 | nan | nan | nan | Cerrado | 66.3 |
| 50120924-0f45-35b8-babf-1d13ca710a33 | -6.31108 | -44.05529 | 2025-10-30 04:04:00 | NPP-375D | COLINAS | MARANHÃO | Brasil | 2103505 | 21 | 33 | nan | nan | nan | Cerrado | 1.7 |
| eca86488-e66f-3bc8-82be-0c68178feed6 | -6.48482 | -42.22036 | 2025-10-30 04:04:00 | NPP-375D | VÁRZEA GRANDE | PIAUÍ | Brasil | 2211407 | 22 | 33 | nan | nan | nan | Caatinga | 1.7 |
| 4dc053b5-d0d2-3c05-80b1-4cd38bbe6fd9 | -6.7485 | -44.61082 | 2025-10-30 04:04:00 | NPP-375D | SÃO DOMINGOS DO AZEITÃO | MARANHÃO | Brasil | 2110658 | 21 | 33 | nan | nan | nan | Cerrado | 2.6 |
| d7017eaa-ad3a-38a6-8149-c67dfb3fa7e5 | -7.29165 | -45.66493 | 2025-10-30 04:04:00 | NPP-375D | SÃO RAIMUNDO DAS MANGABEIRAS | MARANHÃO | Brasil | 2111607 | 21 | 33 | nan | nan | nan | Cerrado | 2.6 |
| 51363048-2822-3544-8796-ee370b64d67f | -4.94567 | -45.61609 | 2025-10-30 04:04:00 | NPP-375D | ARAME | MARANHÃO | Brasil | 2100956 | 21 | 33 | nan | nan | nan | Amazônia | 0.7 |
| 4298e227-4d50-3548-8170-a638be3df310 | -5.9456 | -46.65054 | 2025-10-30 04:04:00 | NPP-375D | SÍTIO NOVO | MARANHÃO | Brasil | 2111805 | 21 | 33 | nan | nan | nan | Cerrado | 1.3 |
| 695a1516-38c8-3b11-88d0-af57e26423c8 | -4.55946 | -46.33664 | 2025-10-30 04:04:00 | NPP-375D | BURITICUPU | MARANHÃO | Brasil | 2102325 | 21 | 33 | nan | nan | nan | Amazônia | 1.9 |
| e3463fc6-bdc8-3ada-89a0-71e4d3fa0697 | -5.89716 | -44.96024 | 2025-10-30 04:04:00 | NPP-375D | FERNANDO FALCÃO | MARANHÃO | Brasil | 2104081 | 21 | 33 | nan | nan | nan | Cerrado | 3.2 |
| 5d5bae6c-4e32-3b2d-869c-a8e410884713 | -4.76075 | -46.853 | 2025-10-30 04:04:00 | NPP-375D | BOM JESUS DAS SELVAS | MARANHÃO | Brasil | 2102036 | 21 | 33 | nan | nan | nan | Amazônia | 2.7 |
| d3230f36-ae06-35c2-8172-47f929861f72 | -7.34845 | -43.90238 | 2025-10-30 04:04:00 | NPP-375D | LANDRI SALES | PIAUÍ | Brasil | 2205607 | 22 | 33 | nan | nan | nan | Cerrado | 1.7 |
| f81abb72-ede4-3cac-8330-a5f0ba16906f | -7.50608 | -41.23245 | 2025-10-30 04:04:00 | NPP-375D | MASSAPÊ DO PIAUÍ | PIAUÍ | Brasil | 2206050 | 22 | 33 | nan | nan | nan | Caatinga | 0.8 |
| d3d9873b-90d6-32f0-a34e-4a914aae5218 | -2.57204 | -45.80278 | 2025-10-30 04:04:00 | NPP-375D | SANTA LUZIA DO PARUÁ | MARANHÃO | Brasil | 2110039 | 21 | 33 | nan | nan | nan | Amazônia | 6.7 |
| 2e5e93c9-8e37-3e6d-a17d-8773f9e66cc0 | -7.96108 | -43.79273 | 2025-10-30 04:04:00 | NPP-375D | BERTOLÍNIA | PIAUÍ | Brasil | 2201705 | 22 | 33 | nan | nan | nan | Caatinga | 1.7 |
| d939f46c-fae1-3d5f-a36d-27b709f0a094 | -3.64178 | -39.37547 | 2025-10-30 04:04:00 | NPP-375D | TURURU | CEARÁ | Brasil | 2313559 | 23 | 33 | nan | nan | nan | Caatinga | 1.0 |
| d7e0fb10-b809-320c-ad2e-3fc90cfb6e03 | -6.29532 | -42.88395 | 2025-10-30 04:04:00 | NPP-375D | SÃO FRANCISCO DO MARANHÃO | MARANHÃO | Brasil | 2110906 | 21 | 33 | nan | nan | nan | Cerrado | 4.2 |
| 661638bb-71a9-3de5-a631-c6d64a6f463c | -4.66067 | -41.59877 | 2025-10-30 04:04:00 | NPP-375D | MILTON BRANDÃO | PIAUÍ | Brasil | 2206357 | 22 | 33 | nan | nan | nan | Caatinga | 0.9 |
| e93ff6cb-c65b-3f4c-820d-66997a8492d4 | -4.91325 | -45.67774 | 2025-10-30 04:04:00 | NPP-375D | ARAME | MARANHÃO | Brasil | 2100956 | 21 | 33 | nan | nan | nan | Amazônia | 0.8 |
| fe7fe802-70ca-3421-9833-59e1a3bff53f | -6.0919 | -41.77234 | 2025-10-30 04:04:00 | NPP-375D | AROAZES | PIAUÍ | Brasil | 2200905 | 22 | 33 | nan | nan | nan | Caatinga | 1.3 |
| 0769a325-9958-3995-920c-714e28e20d3d | -3.47561 | -49.92251 | 2025-10-30 04:04:00 | NPP-375D | PACAJÁ | PARÁ | Brasil | 1505486 | 15 | 33 | nan | nan | nan | Amazônia | 0.4 |
| 6ababfef-c4b0-300d-a1d6-69bf5d278181 | -7.78729 | -46.45242 | 2025-10-30 04:04:00 | NPP-375D | RIACHÃO | MARANHÃO | Brasil | 2109502 | 21 | 33 | nan | nan | nan | Cerrado | 1.7 |
| d702a9fc-9a7a-3387-9db5-49dcb904e788 | -5.23103 | -46.13852 | 2025-10-30 04:04:00 | NPP-375D | ARAME | MARANHÃO | Brasil | 2100956 | 21 | 33 | nan | nan | nan | Amazônia | 1.4 |
| 2e57fd9a-cee1-3e94-b342-09069c53b7f3 | -6.42143 | -42.3248 | 2025-10-30 04:04:00 | NPP-375D | REGENERAÇÃO | PIAUÍ | Brasil | 2208809 | 22 | 33 | nan | nan | nan | Caatinga | 1.2 |
| a4ea30a6-e6b2-3554-934f-32b0b9fbf08f | -6.91206 | -42.2568 | 2025-10-30 04:04:00 | NPP-375D | OEIRAS | PIAUÍ | Brasil | 2207009 | 22 | 33 | nan | nan | nan | Caatinga | 3.7 |
| 910b1d2c-de5b-3fd7-8063-a6040499a61e | -6.85667 | -42.13889 | 2025-10-30 04:04:00 | NPP-375D | OEIRAS | PIAUÍ | Brasil | 2207009 | 22 | 33 | nan | nan | nan | Caatinga | 1.5 |
| 12d23a23-3dfc-3c80-9b79-6a92415b3bb1 | -6.13942 | -41.56438 | 2025-10-30 04:04:00 | NPP-375D | PIMENTEIRAS | PIAUÍ | Brasil | 2208106 | 22 | 33 | nan | nan | nan | Caatinga | 1.1 |
| 5f18a8b8-db2f-3783-b859-c49d78fadb45 | -7.16083 | -39.46235 | 2025-10-30 04:04:00 | NPP-375D | CRATO | CEARÁ | Brasil | 2304202 | 23 | 33 | nan | nan | nan | Caatinga | 1.7 |
| a8ec00ab-c687-3a47-839d-6a403ca73c4c | -6.3117 | -42.1045 | 2025-10-30 04:04:00 | NPP-375D | ELESBÃO VELOSO | PIAUÍ | Brasil | 2203503 | 22 | 33 | nan | nan | nan | Caatinga | 2.7 |
| cdef6df1-b318-3260-a942-d356827072a3 | -8.35814 | -39.89089 | 2025-10-30 04:04:00 | NPP-375D | PARNAMIRIM | PERNAMBUCO | Brasil | 2610400 | 26 | 33 | nan | nan | nan | Caatinga | 0.8 |
| 6621f747-7223-3edc-aa90-672a3a5fb464 | -5.79374 | -40.82465 | 2025-10-30 04:04:00 | NPP-375D | QUITERIANÓPOLIS | CEARÁ | Brasil | 2311264 | 23 | 33 | nan | nan | nan | Caatinga | 1.9 |
| d3fb8198-8f4d-3ff5-a631-e20d259ec7d9 | -7.34115 | -39.71334 | 2025-10-30 04:04:00 | NPP-375D | EXU | PERNAMBUCO | Brasil | 2605301 | 26 | 33 | nan | nan | nan | Caatinga | 1.9 |
| 3e1e1c37-6c2e-35d3-a335-022c736e4a29 | -6.15442 | -45.7169 | 2025-10-30 04:04:00 | NPP-375D | GRAJAÚ | MARANHÃO | Brasil | 2104800 | 21 | 33 | nan | nan | nan | Cerrado | 1.3 |
| 74afe6c5-2394-34cf-9c80-0cf29d550bce | -7.34667 | -39.32977 | 2025-10-30 04:04:00 | NPP-375D | BARBALHA | CEARÁ | Brasil | 2301901 | 23 | 33 | nan | nan | nan | Caatinga | 1.3 |
| 19bd021c-f3a7-3cd0-9dff-4a46d3addb2d | -7.06352 | -44.94857 | 2025-10-30 04:04:00 | NPP-375D | SÃO FÉLIX DE BALSAS | MARANHÃO | Brasil | 2110807 | 21 | 33 | nan | nan | nan | Cerrado | 3.8 |
| e96d1391-c078-39fc-939d-96d80bcd4d4c | -7.08219 | -44.93512 | 2025-10-30 04:04:00 | NPP-375D | SÃO FÉLIX DE BALSAS | MARANHÃO | Brasil | 2110807 | 21 | 33 | nan | nan | nan | Cerrado | 9.2 |
| a58f8a61-b714-310e-b881-6438baad84f5 | -6.70805 | -38.20594 | 2025-10-30 04:04:00 | NPP-375D | SOUSA | PARAÍBA | Brasil | 2516201 | 25 | 33 | nan | nan | nan | Caatinga | 1.4 |
| 7bfea51b-d00a-367c-a4c2-2b0c96be458b | -6.18957 | -41.51268 | 2025-10-30 04:04:00 | NPP-375D | PIMENTEIRAS | PIAUÍ | Brasil | 2208106 | 22 | 33 | nan | nan | nan | Caatinga | 1.1 |
| 9889e01f-cb4f-30cc-a7d5-d31a61478df3 | -2.57741 | -45.80109 | 2025-10-30 04:04:00 | NPP-375D | SANTA LUZIA DO PARUÁ | MARANHÃO | Brasil | 2110039 | 21 | 33 | nan | nan | nan | Amazônia | 16.7 |
| aeb8232f-1f93-3731-98a3-066dab65a88c | -6.11374 | -42.44097 | 2025-10-30 04:04:00 | NPP-375D | HUGO NAPOLEÃO | PIAUÍ | Brasil | 2204600 | 22 | 33 | nan | nan | nan | Caatinga | 2.3 |
| efc1b067-1390-37b1-a2f0-f2cf02736db6 | -6.71149 | -38.20644 | 2025-10-30 04:04:00 | NPP-375D | SOUSA | PARAÍBA | Brasil | 2516201 | 25 | 33 | nan | nan | nan | Caatinga | 1.4 |
| 00096b56-6b4a-35d0-a71f-c592cdd930dc | -5.43075 | -45.34491 | 2025-10-30 04:04:00 | NPP-375D | BARRA DO CORDA | MARANHÃO | Brasil | 2101608 | 21 | 33 | nan | nan | nan | Cerrado | 2.4 |
| 7d935728-91a0-3193-bbee-b95b57ac5bb2 | -7.0721 | -44.47071 | 2025-10-30 04:04:00 | NPP-375D | BENEDITO LEITE | MARANHÃO | Brasil | 2101806 | 21 | 33 | nan | nan | nan | Cerrado | 5.0 |
| 93017769-b3b1-386d-a3f5-ff29cb5843f3 | -6.14609 | -41.58814 | 2025-10-30 04:04:00 | NPP-375D | PIMENTEIRAS | PIAUÍ | Brasil | 2208106 | 22 | 33 | nan | nan | nan | Caatinga | 1.2 |
| a980832f-09f5-351d-81f8-843435069f6e | -7.89104 | -45.68001 | 2025-10-30 04:04:00 | NPP-375D | TASSO FRAGOSO | MARANHÃO | Brasil | 2112001 | 21 | 33 | nan | nan | nan | Cerrado | 3.2 |
| 587038b6-b770-3f1f-8309-60583492f671 | -5.03488 | -43.61174 | 2025-10-30 04:04:00 | NPP-375D | SÃO JOÃO DO SOTER | MARANHÃO | Brasil | 2111078 | 21 | 33 | nan | nan | nan | Cerrado | 9.4 |
| 14feaff4-37c8-3947-af86-ccea3be593bf | -4.89121 | -45.44231 | 2025-10-30 04:04:00 | NPP-375D | LAGOA GRANDE DO MARANHÃO | MARANHÃO | Brasil | 2105963 | 21 | 33 | nan | nan | nan | Cerrado | 1.0 |
| 33c1f469-7c06-3eec-af49-c2c9e98ff01c | -7.14179 | -40.4582 | 2025-10-30 04:04:00 | NPP-375D | SALITRE | CEARÁ | Brasil | 2311959 | 23 | 33 | nan | nan | nan | Caatinga | 1.1 |
| 28de8452-a92e-380a-a2fc-81ba6f003d2b | -3.12144 | -45.10112 | 2025-10-30 04:04:00 | NPP-375D | VIANA | MARANHÃO | Brasil | 2112803 | 21 | 33 | nan | nan | nan | Amazônia | 1.3 |
| c0df6a3b-6ab0-342f-850b-34cc5b38afaa | -4.4874 | -43.43852 | 2025-10-30 04:04:00 | NPP-375D | ALDEIAS ALTAS | MARANHÃO | Brasil | 2100303 | 21 | 33 | nan | nan | nan | Cerrado | 5.5 |
| d735f1da-bb7e-3512-9c0b-c48720b31cd9 | -5.41436 | -46.01339 | 2025-10-30 04:04:00 | NPP-375D | GRAJAÚ | MARANHÃO | Brasil | 2104800 | 21 | 33 | nan | nan | nan | Cerrado | 2.3 |
| 3b8f7333-7a11-321e-bd69-9c4c245b44b1 | -5.67801 | -45.88744 | 2025-10-30 04:04:00 | NPP-375D | GRAJAÚ | MARANHÃO | Brasil | 2104800 | 21 | 33 | nan | nan | nan | Cerrado | 0.4 |
| 7d07c02a-e8de-323b-a207-70abfe01324b | -7.29759 | -44.96561 | 2025-10-30 04:04:00 | NPP-375D | SÃO FÉLIX DE BALSAS | MARANHÃO | Brasil | 2110807 | 21 | 33 | nan | nan | nan | Cerrado | 1.9 |
| cc4cfc2c-b20b-3909-8372-c4853a954be1 | -5.0117 | -41.04114 | 2025-10-30 04:04:00 | NPP-375D | IPAPORANGA | CEARÁ | Brasil | 2305654 | 23 | 33 | nan | nan | nan | Caatinga | 1.2 |
| 5311a452-9f28-32cb-af05-9def5aeb0515 | -6.1775 | -41.67587 | 2025-10-30 04:04:00 | NPP-375D | PIMENTEIRAS | PIAUÍ | Brasil | 2208106 | 22 | 33 | nan | nan | nan | Caatinga | 0.8 |
| 4366a428-0cd6-3389-8752-c37593c528eb | -7.29361 | -44.96498 | 2025-10-30 04:04:00 | NPP-375D | SÃO FÉLIX DE BALSAS | MARANHÃO | Brasil | 2110807 | 21 | 33 | nan | nan | nan | Cerrado | 1.9 |
| fe4264d8-4997-3da1-bc2a-a842c296e3a7 | -3.2955 | -46.04993 | 2025-10-30 04:04:00 | NPP-375D | ZÉ DOCA | MARANHÃO | Brasil | 2114007 | 21 | 33 | nan | nan | nan | Amazônia | 0.8 |
| 46933b88-5b01-3779-8d97-5cb3c1f2703a | -6.15514 | -41.59713 | 2025-10-30 04:04:00 | NPP-375D | PIMENTEIRAS | PIAUÍ | Brasil | 2208106 | 22 | 33 | nan | nan | nan | Caatinga | 1.4 |
| 996ba612-46ef-3001-bd61-21a540f81f02 | -6.13745 | -41.70756 | 2025-10-30 04:04:00 | NPP-375D | AROAZES | PIAUÍ | Brasil | 2200905 | 22 | 33 | nan | nan | nan | Caatinga | 3.0 |
| af11bbcc-4d7c-317c-9e79-919ff8923611 | -7.32222 | -42.48644 | 2025-10-30 04:04:00 | NPP-375D | SÃO FRANCISCO DO PIAUÍ | PIAUÍ | Brasil | 2209708 | 22 | 33 | nan | nan | nan | Caatinga | 2.6 |
| 240a6e70-fb67-38ef-97a7-14fd8ad1f6e7 | -3.29033 | -46.05138 | 2025-10-30 04:04:00 | NPP-375D | ZÉ DOCA | MARANHÃO | Brasil | 2114007 | 21 | 33 | nan | nan | nan | Amazônia | 1.3 |
| f1326e96-6a1a-3df6-8ef1-a37f74c69d5f | -5.4817 | -44.10767 | 2025-10-30 04:04:00 | NPP-375D | GOVERNADOR LUIZ ROCHA | MARANHÃO | Brasil | 2104628 | 21 | 33 | nan | nan | nan | Cerrado | 2.1 |
| 41bff8c6-729f-3d51-bd0a-5e1491b93fef | -7.27649 | -46.06377 | 2025-10-30 04:04:00 | NPP-375D | BALSAS | MARANHÃO | Brasil | 2101400 | 21 | 33 | nan | nan | nan | Cerrado | 4.1 |
| bc751b3f-08be-34ca-9fa7-4c1d7275ecdf | -7.02066 | -46.43315 | 2025-10-30 04:04:00 | NPP-375D | FEIRA NOVA DO MARANHÃO | MARANHÃO | Brasil | 2104073 | 21 | 33 | nan | nan | nan | Cerrado | 1.4 |
| e50e3207-7c40-314b-a89a-2949e57f2b5f | -7.58085 | -43.64977 | 2025-10-30 04:04:00 | NPP-375D | CANAVIEIRA | PIAUÍ | Brasil | 2202251 | 22 | 33 | nan | nan | nan | Cerrado | 3.2 |
| d39fbfbf-3f60-3331-966c-50e9bd5198cf | -6.1502 | -41.67172 | 2025-10-30 04:04:00 | NPP-375D | PIMENTEIRAS | PIAUÍ | Brasil | 2208106 | 22 | 33 | nan | nan | nan | Caatinga | 0.9 |
| bb72a75c-21c4-36bd-8411-3666d1f00788 | -5.24369 | -38.42267 | 2025-10-30 04:04:00 | NPP-375D | MORADA NOVA | CEARÁ | Brasil | 2308708 | 23 | 33 | nan | nan | nan | Caatinga | 0.7 |
| e5749e38-30e9-350b-8177-a31fecec6b8b | -5.67 | -42.87664 | 2025-10-30 04:04:00 | NPP-375D | CURRALINHOS | PIAUÍ | Brasil | 2203255 | 22 | 33 | nan | nan | nan | Caatinga | 2.5 |
| 2300a01c-a1fc-38f2-b451-1dc1ae11a795 | -2.25503 | -47.02537 | 2025-10-30 04:04:00 | NPP-375D | GARRAFÃO DO NORTE | PARÁ | Brasil | 1503077 | 15 | 33 | nan | nan | nan | Amazônia | 2.0 |
| e21ab661-ac48-3c20-874b-787c2b9ceb81 | -7.62472 | -43.61259 | 2025-10-30 04:04:00 | NPP-375D | CANAVIEIRA | PIAUÍ | Brasil | 2202251 | 22 | 33 | nan | nan | nan | Cerrado | 4.9 |
| 6864f0b6-a548-3dfa-9bcd-94b14c43b8fb | -6.1065 | -41.7254 | 2025-10-30 04:04:00 | NPP-375D | AROAZES | PIAUÍ | Brasil | 2200905 | 22 | 33 | nan | nan | nan | Caatinga | 2.9 |
| 74c0e6e5-ad8f-3d59-be72-d98ddb900515 | -7.29101 | -45.66868 | 2025-10-30 04:04:00 | NPP-375D | SÃO RAIMUNDO DAS MANGABEIRAS | MARANHÃO | Brasil | 2111607 | 21 | 33 | nan | nan | nan | Cerrado | 4.9 |


[Clique aqui para ver as próximas entradas](README25.md)
