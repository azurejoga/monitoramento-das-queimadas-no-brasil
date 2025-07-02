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

## Dados Diários - Página 5

| ID | Latitude | Longitude | Data/Hora GMT | Satélite | Município | Estado | País | Município ID | Estado ID | País ID | Dias sem Chuva | Precipitação | Risco de Fogo | Bioma | FRP |
|----|----------|-----------|---------------|----------|-----------|--------|------|--------------|-----------|---------|----------------|--------------|----------------|-------|-----|
| 0f6aeb24-800e-3eec-9e38-30334a4189ef | -15.9208 | -43.51984 | 2025-07-02 03:17:00 | NPP-375D | JANAÚBA | MINAS GERAIS | Brasil | 3135100 | 31 | 33 | nan | nan | nan | Cerrado | 5.0 |
| e28d8f63-7881-3f7d-ab70-ad2d8acf1b00 | -19.52266 | -43.60577 | 2025-07-02 03:17:00 | NPP-375D | JABOTICATUBAS | MINAS GERAIS | Brasil | 3134608 | 31 | 33 | nan | nan | nan | Cerrado | 7.9 |
| b29859e7-e6c6-3a9f-9a76-a5f7bbcd0cf2 | -15.89186 | -43.46189 | 2025-07-02 03:17:00 | NPP-375D | JANAÚBA | MINAS GERAIS | Brasil | 3135100 | 31 | 33 | nan | nan | nan | Cerrado | 9.4 |
| e4595ac2-1495-3c1a-9f4c-7bafd57fb43b | -15.92773 | -43.5215 | 2025-07-02 03:17:00 | NPP-375D | JANAÚBA | MINAS GERAIS | Brasil | 3135100 | 31 | 33 | nan | nan | nan | Cerrado | 2.5 |
| 9de73a5e-1ad8-33b9-972b-e82c78d08bfc | -15.8955 | -43.4523 | 2025-07-02 03:20:00 | GOES-19 | JANAÚBA | MINAS GERAIS | Brasil | 3135100 | 31 | 33 | nan | nan | nan | Cerrado | 69.4 |
| eb8110e4-b10f-313d-a994-94c8327adc8e | -7.7947 | -44.0145 | 2025-07-02 03:20:00 | GOES-19 | SEBASTIÃO LEAL | PIAUÍ | Brasil | 2210631 | 22 | 33 | nan | nan | nan | Cerrado | 191.7 |
| 898024de-f858-3c06-ae24-ca880b68dc1f | -7.8133 | -44.0358 | 2025-07-02 03:20:00 | GOES-19 | SEBASTIÃO LEAL | PIAUÍ | Brasil | 2210631 | 22 | 33 | nan | nan | nan | Cerrado | 119.6 |
| 0cd5fc07-c92f-3351-af11-cf79e5b6a4e9 | -7.2217 | -43.0917 | 2025-07-02 03:20:00 | GOES-19 | FLORIANO | PIAUÍ | Brasil | 2203909 | 22 | 33 | nan | nan | nan | Caatinga | 90.1 |
| 48ae35a1-62f2-3ec4-8888-032c6d08edce | -7.7944 | -44.0377 | 2025-07-02 03:20:00 | GOES-19 | SEBASTIÃO LEAL | PIAUÍ | Brasil | 2210631 | 22 | 33 | nan | nan | nan | Cerrado | 100.9 |
| 08ec5e69-6155-3e99-a78a-9af32ee373c9 | -7.0943 | -44.3819 | 2025-07-02 03:20:00 | GOES-19 | BENEDITO LEITE | MARANHÃO | Brasil | 2101806 | 21 | 33 | nan | nan | nan | Cerrado | 59.6 |
| e5cbe9d4-5a30-34a9-986a-87d78b4df325 | -7.8135 | -44.0126 | 2025-07-02 03:20:00 | GOES-19 | SEBASTIÃO LEAL | PIAUÍ | Brasil | 2210631 | 22 | 33 | nan | nan | nan | Cerrado | 172.2 |
| 45c28b58-0899-3a7a-a8c6-c8c3c49fdca9 | -6.7093 | -51.4165 | 2025-07-02 03:20:00 | GOES-19 | TUCUMÃ | PARÁ | Brasil | 1508084 | 15 | 33 | nan | nan | nan | Amazônia | 37.4 |
| e22dfd06-02e3-3093-9b9e-c5602bf5c492 | -7.2028 | -43.0936 | 2025-07-02 03:20:00 | GOES-19 | FLORIANO | PIAUÍ | Brasil | 2203909 | 22 | 33 | nan | nan | nan | Caatinga | 77.5 |
| 2f54ed04-2c71-3184-bed6-2fa60f7fa5e0 | -7.7947 | -44.0145 | 2025-07-02 03:30:00 | GOES-19 | SEBASTIÃO LEAL | PIAUÍ | Brasil | 2210631 | 22 | 33 | nan | nan | nan | Cerrado | 196.5 |
| ec85e4c6-679d-3337-a31c-68acb1d92254 | -7.2217 | -43.0917 | 2025-07-02 03:30:00 | GOES-19 | FLORIANO | PIAUÍ | Brasil | 2203909 | 22 | 33 | nan | nan | nan | Caatinga | 83.8 |
| 357549e6-43f0-32bf-9d49-5db3b73e8a2d | -15.8955 | -43.4523 | 2025-07-02 03:30:00 | GOES-19 | JANAÚBA | MINAS GERAIS | Brasil | 3135100 | 31 | 33 | nan | nan | nan | Cerrado | 75.0 |
| 49541560-e831-3324-865e-ec85ae9008ee | -7.7944 | -44.0377 | 2025-07-02 03:30:00 | GOES-19 | SEBASTIÃO LEAL | PIAUÍ | Brasil | 2210631 | 22 | 33 | nan | nan | nan | Cerrado | 91.3 |
| 754bb773-f521-371b-80f2-25e48e332053 | -7.2028 | -43.0936 | 2025-07-02 03:30:00 | GOES-19 | FLORIANO | PIAUÍ | Brasil | 2203909 | 22 | 33 | nan | nan | nan | Caatinga | 67.4 |
| 62994dd0-7b4c-38ab-9ebd-f6bf63da293a | -7.0943 | -44.3819 | 2025-07-02 03:30:00 | GOES-19 | BENEDITO LEITE | MARANHÃO | Brasil | 2101806 | 21 | 33 | nan | nan | nan | Cerrado | 65.7 |
| a11f5c28-a696-3f32-b9ab-da6ffa30cc01 | -7.8133 | -44.0358 | 2025-07-02 03:30:00 | GOES-19 | SEBASTIÃO LEAL | PIAUÍ | Brasil | 2210631 | 22 | 33 | nan | nan | nan | Cerrado | 113.4 |
| e9760c33-4190-3e92-8809-5213f0cba557 | -7.8135 | -44.0126 | 2025-07-02 03:30:00 | GOES-19 | SEBASTIÃO LEAL | PIAUÍ | Brasil | 2210631 | 22 | 33 | nan | nan | nan | Cerrado | 177.3 |
| f995fc5b-fe8d-3f44-8359-faf6bc02ce13 | -6.27342 | -43.67987 | 2025-07-02 03:34:00 | NOAA-20 | PASSAGEM FRANCA | MARANHÃO | Brasil | 2107902 | 21 | 33 | nan | nan | nan | Cerrado | 10.0 |
| 1cf89d64-10cf-328f-9b5f-e9af7def75ec | -6.95458 | -42.89129 | 2025-07-02 03:34:00 | NOAA-20 | FLORIANO | PIAUÍ | Brasil | 2203909 | 22 | 33 | nan | nan | nan | Caatinga | 10.1 |
| 48eca8ea-c45d-3ae9-80e3-8b83bdc75432 | -6.2847 | -43.6817 | 2025-07-02 03:34:00 | NOAA-20 | PASSAGEM FRANCA | MARANHÃO | Brasil | 2107902 | 21 | 33 | nan | nan | nan | Cerrado | 8.9 |
| 3563c397-6940-3e11-bcfd-fb4876c99e5e | -4.8273 | -37.90705 | 2025-07-02 03:34:00 | NOAA-20 | RUSSAS | CEARÁ | Brasil | 2311801 | 23 | 33 | nan | nan | nan | Caatinga | 1.2 |
| 156cb6c5-9f0a-376b-b0ff-ad2fe328b82e | -6.95517 | -42.88799 | 2025-07-02 03:34:00 | NOAA-20 | FLORIANO | PIAUÍ | Brasil | 2203909 | 22 | 33 | nan | nan | nan | Caatinga | 6.0 |
| d6203101-df07-3f41-9732-37d90058171a | -5.91203 | -43.45258 | 2025-07-02 03:34:00 | NOAA-20 | LAGOA DO MATO | MARANHÃO | Brasil | 2105922 | 21 | 33 | nan | nan | nan | Cerrado | 6.5 |
| 4d255b32-d890-3474-98c9-4aec4cab02ac | -7.20949 | -40.24598 | 2025-07-02 03:34:00 | NOAA-20 | ARARIPE | CEARÁ | Brasil | 2301307 | 23 | 33 | nan | nan | nan | Caatinga | 4.6 |
| 9e593472-cb2a-3913-9ca1-389eddcc08af | -6.29662 | -43.67999 | 2025-07-02 03:34:00 | NOAA-20 | PASSAGEM FRANCA | MARANHÃO | Brasil | 2107902 | 21 | 33 | nan | nan | nan | Cerrado | 5.4 |
| 30107835-be91-3774-9840-cc4d40e50840 | -6.66015 | -43.84555 | 2025-07-02 03:34:00 | NOAA-20 | NOVA IORQUE | MARANHÃO | Brasil | 2107308 | 21 | 33 | nan | nan | nan | Cerrado | 1.8 |
| ef8497ee-0d36-3e66-964e-f65f31567187 | -6.95807 | -42.90224 | 2025-07-02 03:34:00 | NOAA-20 | FLORIANO | PIAUÍ | Brasil | 2203909 | 22 | 33 | nan | nan | nan | Caatinga | 1.6 |
| c6a25139-57d1-3399-917b-788ab46fd496 | -6.27838 | -43.68457 | 2025-07-02 03:34:00 | NOAA-20 | PASSAGEM FRANCA | MARANHÃO | Brasil | 2107902 | 21 | 33 | nan | nan | nan | Cerrado | 10.0 |
| 09011c79-f1d3-30f8-9df5-d7240b60abcb | -6.95338 | -42.89796 | 2025-07-02 03:34:00 | NOAA-20 | FLORIANO | PIAUÍ | Brasil | 2203909 | 22 | 33 | nan | nan | nan | Caatinga | 1.6 |
| 7d70872e-e0be-39c2-82a6-caeac0631192 | -6.27272 | -43.6837 | 2025-07-02 03:34:00 | NOAA-20 | PASSAGEM FRANCA | MARANHÃO | Brasil | 2107902 | 21 | 33 | nan | nan | nan | Cerrado | 10.0 |
| ad3b053a-8c07-3200-a672-2c9bbf9cb446 | -6.84255 | -42.79229 | 2025-07-02 03:34:00 | NOAA-20 | NAZARÉ DO PIAUÍ | PIAUÍ | Brasil | 2206704 | 22 | 33 | nan | nan | nan | Caatinga | 1.2 |
| 9c49f0b4-0d2b-3401-bff0-73ef9d9fb637 | -6.29101 | -43.67889 | 2025-07-02 03:34:00 | NOAA-20 | PASSAGEM FRANCA | MARANHÃO | Brasil | 2107902 | 21 | 33 | nan | nan | nan | Cerrado | 14.2 |
| cdabd48d-c0e6-3ee6-84ce-c9cdc25842d2 | -6.66241 | -43.847 | 2025-07-02 03:34:00 | NOAA-20 | NOVA IORQUE | MARANHÃO | Brasil | 2107308 | 21 | 33 | nan | nan | nan | Cerrado | 3.6 |
| d2412117-3226-341c-b089-0e9b54e46c52 | -6.8435 | -42.79065 | 2025-07-02 03:34:00 | NOAA-20 | NAZARÉ DO PIAUÍ | PIAUÍ | Brasil | 2206704 | 22 | 33 | nan | nan | nan | Caatinga | 2.4 |
| 31ce5c9c-b608-3053-9c2c-ce62894274a1 | -5.62368 | -44.26797 | 2025-07-02 03:34:00 | NOAA-20 | SÃO DOMINGOS DO MARANHÃO | MARANHÃO | Brasil | 2110708 | 21 | 33 | nan | nan | nan | Cerrado | 2.2 |
| 77da7828-baa2-3494-ac05-1dd4c5c2524b | -5.91136 | -43.45641 | 2025-07-02 03:34:00 | NOAA-20 | PARNARAMA | MARANHÃO | Brasil | 2107803 | 21 | 33 | nan | nan | nan | Cerrado | 7.2 |
| aab13260-5ec9-3f82-8a03-a357ff39eacf | -6.95866 | -42.8989 | 2025-07-02 03:34:00 | NOAA-20 | FLORIANO | PIAUÍ | Brasil | 2203909 | 22 | 33 | nan | nan | nan | Caatinga | 1.6 |
| cbc81900-4fd9-3620-944d-1dc2bd35ec1c | -6.2103 | -44.19608 | 2025-07-02 03:34:00 | NOAA-20 | COLINAS | MARANHÃO | Brasil | 2103505 | 21 | 33 | nan | nan | nan | Cerrado | 3.4 |
| 19801df9-7475-38c1-8d90-463799d6ac35 | -6.84313 | -42.78912 | 2025-07-02 03:34:00 | NOAA-20 | NAZARÉ DO PIAUÍ | PIAUÍ | Brasil | 2206704 | 22 | 33 | nan | nan | nan | Caatinga | 1.2 |
| f4dadd42-e21f-30f2-a91c-dd18726e2984 | -6.95277 | -42.90136 | 2025-07-02 03:34:00 | NOAA-20 | FLORIANO | PIAUÍ | Brasil | 2203909 | 22 | 33 | nan | nan | nan | Caatinga | 1.6 |
| 0bb71f6b-5fff-3e6f-8649-b1081fd6fab6 | -6.20948 | -44.20067 | 2025-07-02 03:34:00 | NOAA-20 | COLINAS | MARANHÃO | Brasil | 2103505 | 21 | 33 | nan | nan | nan | Cerrado | 3.4 |
| e7f2b4e8-bb77-3910-ab7c-7dbdd5d434ce | -7.21024 | -40.24168 | 2025-07-02 03:34:00 | NOAA-20 | ARARIPE | CEARÁ | Brasil | 2301307 | 23 | 33 | nan | nan | nan | Caatinga | 2.0 |
| 239df56e-3e6b-32fd-b35b-82d747233699 | -6.29031 | -43.68277 | 2025-07-02 03:34:00 | NOAA-20 | PASSAGEM FRANCA | MARANHÃO | Brasil | 2107902 | 21 | 33 | nan | nan | nan | Cerrado | 8.9 |
| 21dbd401-6178-3397-a37b-b3166833c86d | -5.06898 | -43.72936 | 2025-07-02 03:34:00 | NOAA-20 | SÃO JOÃO DO SOTER | MARANHÃO | Brasil | 2111078 | 21 | 33 | nan | nan | nan | Cerrado | 1.8 |
| db5af86f-4caf-320f-a715-d5cf07ae272e | -6.28401 | -43.68554 | 2025-07-02 03:34:00 | NOAA-20 | PASSAGEM FRANCA | MARANHÃO | Brasil | 2107902 | 21 | 33 | nan | nan | nan | Cerrado | 8.9 |
| 05432b74-af42-3acb-98f9-69cad9d3e655 | -7.20584 | -40.24094 | 2025-07-02 03:34:00 | NOAA-20 | ARARIPE | CEARÁ | Brasil | 2301307 | 23 | 33 | nan | nan | nan | Caatinga | 2.0 |
| 17ea369f-eed1-3f94-a9ee-83228ac63a6a | -6.66577 | -43.8468 | 2025-07-02 03:34:00 | NOAA-20 | NOVA IORQUE | MARANHÃO | Brasil | 2107308 | 21 | 33 | nan | nan | nan | Cerrado | 1.8 |
| 5fa69298-8d41-3a44-b45e-f671ac1aa16d | -3.21089 | -41.84161 | 2025-07-02 03:34:00 | NOAA-20 | BURITI DOS LOPES | PIAUÍ | Brasil | 2202000 | 22 | 33 | nan | nan | nan | Cerrado | 1.1 |
| 38126f97-14a0-34c3-b4a2-227fee3bf892 | -4.80297 | -43.2239 | 2025-07-02 03:34:00 | NOAA-20 | CAXIAS | MARANHÃO | Brasil | 2103000 | 21 | 33 | nan | nan | nan | Cerrado | 0.8 |
| 128c4676-bd62-3972-9de4-a5d1ad0a171e | -6.28538 | -43.67791 | 2025-07-02 03:34:00 | NOAA-20 | PASSAGEM FRANCA | MARANHÃO | Brasil | 2107902 | 21 | 33 | nan | nan | nan | Cerrado | 14.2 |
| 10f3774f-008f-3478-9069-365547403dbe | -3.21036 | -41.84485 | 2025-07-02 03:34:00 | NOAA-20 | BURITI DOS LOPES | PIAUÍ | Brasil | 2202000 | 22 | 33 | nan | nan | nan | Cerrado | 1.3 |
| 21b7fd3b-a3de-302b-bbbb-133e7868c317 | -4.8079 | -43.22879 | 2025-07-02 03:34:00 | NOAA-20 | CAXIAS | MARANHÃO | Brasil | 2103000 | 21 | 33 | nan | nan | nan | Cerrado | 1.1 |
| aaf92b5c-bb4a-3ca1-ae85-25a003f4f2b7 | -7.20738 | -43.08385 | 2025-07-02 03:36:00 | NOAA-20 | FLORIANO | PIAUÍ | Brasil | 2203909 | 22 | 33 | nan | nan | nan | Caatinga | 14.0 |
| c8a344ef-8936-364b-b0b6-244e86f5e0c8 | -7.22102 | -43.10018 | 2025-07-02 03:36:00 | NOAA-20 | FLORIANO | PIAUÍ | Brasil | 2203909 | 22 | 33 | nan | nan | nan | Caatinga | 1.9 |
| b0476dc1-a1da-3bea-b0e8-ac6d5b66942e | -7.79021 | -44.01779 | 2025-07-02 03:36:00 | NOAA-20 | SEBASTIÃO LEAL | PIAUÍ | Brasil | 2210631 | 22 | 33 | nan | nan | nan | Cerrado | 7.9 |
| 247733cb-54d9-3988-b40d-c6864e83adb2 | -7.80566 | -44.02855 | 2025-07-02 03:36:00 | NOAA-20 | SEBASTIÃO LEAL | PIAUÍ | Brasil | 2210631 | 22 | 33 | nan | nan | nan | Cerrado | 25.7 |
| 91f2f8e7-44cf-36b8-85ff-4126769d9b3d | -7.80555 | -44.01691 | 2025-07-02 03:36:00 | NOAA-20 | SEBASTIÃO LEAL | PIAUÍ | Brasil | 2210631 | 22 | 33 | nan | nan | nan | Cerrado | 33.5 |
| a5db33f7-a74d-3d01-a08e-fa97a68cd3d2 | -7.21001 | -43.08772 | 2025-07-02 03:36:00 | NOAA-20 | FLORIANO | PIAUÍ | Brasil | 2203909 | 22 | 33 | nan | nan | nan | Caatinga | 16.4 |
| 67c553b8-89d7-3e40-88a9-52ab71c4ffd3 | -7.78882 | -44.02549 | 2025-07-02 03:36:00 | NOAA-20 | SEBASTIÃO LEAL | PIAUÍ | Brasil | 2210631 | 22 | 33 | nan | nan | nan | Cerrado | 5.3 |
| 703cb69f-611b-3450-b28b-5e2e5f413484 | -7.20679 | -43.08718 | 2025-07-02 03:36:00 | NOAA-20 | FLORIANO | PIAUÍ | Brasil | 2203909 | 22 | 33 | nan | nan | nan | Caatinga | 14.0 |
| 23af01e3-1bab-3271-a7f2-c1b46fefde43 | -7.79219 | -44.02635 | 2025-07-02 03:36:00 | NOAA-20 | SEBASTIÃO LEAL | PIAUÍ | Brasil | 2210631 | 22 | 33 | nan | nan | nan | Cerrado | 8.6 |
| 66ed1cc1-e6e2-3cc6-9db0-d3dbc8331fd3 | -9.85003 | -44.70074 | 2025-07-02 03:36:00 | NOAA-20 | RIACHO FRIO | PIAUÍ | Brasil | 2208858 | 22 | 33 | nan | nan | nan | Cerrado | 1.7 |
| 51fc3070-e085-349b-87a3-484dd8812a55 | -12.11053 | -43.65326 | 2025-07-02 03:36:00 | NOAA-20 | MUQUÉM DO SÃO FRANCISCO | BAHIA | Brasil | 2922250 | 29 | 33 | nan | nan | nan | Cerrado | 0.9 |
| 6e244046-4acc-3f3e-94c2-1b225a76e37c | -11.31022 | -46.20031 | 2025-07-02 03:36:00 | NOAA-20 | FORMOSA DO RIO PRETO | BAHIA | Brasil | 2911105 | 29 | 33 | nan | nan | nan | Cerrado | 4.5 |
| 6c417f51-9306-3f85-bb55-19a80b45bf23 | -7.80413 | -44.02454 | 2025-07-02 03:36:00 | NOAA-20 | SEBASTIÃO LEAL | PIAUÍ | Brasil | 2210631 | 22 | 33 | nan | nan | nan | Cerrado | 24.4 |
| e06ab003-98b7-3173-989f-158bb09b4358 | -10.64452 | -44.48851 | 2025-07-02 03:36:00 | NOAA-20 | PARNAGUÁ | PIAUÍ | Brasil | 2207603 | 22 | 33 | nan | nan | nan | Cerrado | 1.4 |
| 0f9331a3-72bb-3588-ab52-a4d774dbf1c7 | -9.85248 | -44.70108 | 2025-07-02 03:36:00 | NOAA-20 | RIACHO FRIO | PIAUÍ | Brasil | 2208858 | 22 | 33 | nan | nan | nan | Cerrado | 1.9 |
| ccd8e791-1839-3b15-b927-c90d1f70642c | -9.84436 | -44.69971 | 2025-07-02 03:36:00 | NOAA-20 | RIACHO FRIO | PIAUÍ | Brasil | 2208858 | 22 | 33 | nan | nan | nan | Cerrado | 1.7 |
| 1f5b2496-daef-3665-9850-8ea96832dad9 | -11.14028 | -43.32959 | 2025-07-02 03:36:00 | NOAA-20 | BARRA | BAHIA | Brasil | 2902708 | 29 | 33 | nan | nan | nan | Caatinga | 3.3 |
| d6948af6-c725-3e9e-959e-8dd868c35cd0 | -7.81535 | -44.02657 | 2025-07-02 03:36:00 | NOAA-20 | SEBASTIÃO LEAL | PIAUÍ | Brasil | 2210631 | 22 | 33 | nan | nan | nan | Cerrado | 7.2 |
| 1d6f692a-2dbd-345d-816e-d9fe852b4b3c | -11.83794 | -43.80392 | 2025-07-02 03:36:00 | NOAA-20 | WANDERLEY | BAHIA | Brasil | 2933455 | 29 | 33 | nan | nan | nan | Cerrado | 0.8 |
| 408855db-9677-3aac-9f26-7a109153bb33 | -7.81689 | -44.03061 | 2025-07-02 03:36:00 | NOAA-20 | SEBASTIÃO LEAL | PIAUÍ | Brasil | 2210631 | 22 | 33 | nan | nan | nan | Cerrado | 9.2 |
| 41ead480-c338-3c6b-8426-1580210a9183 | -7.20561 | -43.09393 | 2025-07-02 03:36:00 | NOAA-20 | FLORIANO | PIAUÍ | Brasil | 2203909 | 22 | 33 | nan | nan | nan | Caatinga | 3.2 |
| 6b7a17bf-89a4-3bbc-a812-f7618ee48b0b | -7.21473 | -43.09201 | 2025-07-02 03:36:00 | NOAA-20 | FLORIANO | PIAUÍ | Brasil | 2203909 | 22 | 33 | nan | nan | nan | Caatinga | 9.0 |
| 5a9cf248-a185-3473-aab8-56f305907dac | -7.18596 | -43.17427 | 2025-07-02 03:36:00 | NOAA-20 | FLORIANO | PIAUÍ | Brasil | 2203909 | 22 | 33 | nan | nan | nan | Caatinga | 0.9 |
| 3005a38a-7b72-37f9-a33e-a99ba7f2f918 | -7.79513 | -44.02266 | 2025-07-02 03:36:00 | NOAA-20 | SEBASTIÃO LEAL | PIAUÍ | Brasil | 2210631 | 22 | 33 | nan | nan | nan | Cerrado | 5.3 |
| d5dd5b70-0622-3931-a7ef-7e614b7bef09 | -7.80974 | -44.02554 | 2025-07-02 03:36:00 | NOAA-20 | SEBASTIÃO LEAL | PIAUÍ | Brasil | 2210631 | 22 | 33 | nan | nan | nan | Cerrado | 24.4 |
| b144d88c-2823-3af5-9fd3-f2f6b2ad3fea | -7.79434 | -44.01487 | 2025-07-02 03:36:00 | NOAA-20 | SEBASTIÃO LEAL | PIAUÍ | Brasil | 2210631 | 22 | 33 | nan | nan | nan | Cerrado | 29.2 |
| b43fed5b-f7b5-3d82-9e03-9e9e3d2f4d83 | -11.14534 | -43.33056 | 2025-07-02 03:36:00 | NOAA-20 | BARRA | BAHIA | Brasil | 2902708 | 29 | 33 | nan | nan | nan | Caatinga | 0.7 |
| 4afebd41-fcc3-3e3b-b4e1-4a8f31302bf2 | -7.80142 | -44.01987 | 2025-07-02 03:36:00 | NOAA-20 | SEBASTIÃO LEAL | PIAUÍ | Brasil | 2210631 | 22 | 33 | nan | nan | nan | Cerrado | 42.7 |
| ede9c2fd-580f-37dc-8c5e-16c959653803 | -7.21211 | -43.0882 | 2025-07-02 03:36:00 | NOAA-20 | FLORIANO | PIAUÍ | Brasil | 2203909 | 22 | 33 | nan | nan | nan | Caatinga | 11.2 |
| 6fe28eb5-3ed6-3c5a-bf15-49582c4f06bf | -7.20878 | -43.09442 | 2025-07-02 03:36:00 | NOAA-20 | FLORIANO | PIAUÍ | Brasil | 2203909 | 22 | 33 | nan | nan | nan | Caatinga | 9.0 |
| 1c5dfde8-0f96-30b9-8cf0-fb241fee6323 | -10.64384 | -44.49216 | 2025-07-02 03:36:00 | NOAA-20 | PARNAGUÁ | PIAUÍ | Brasil | 2207603 | 22 | 33 | nan | nan | nan | Cerrado | 1.4 |
| 2fd1d143-900b-3f8a-9d6c-785569a3b02c | -7.2062 | -43.09054 | 2025-07-02 03:36:00 | NOAA-20 | FLORIANO | PIAUÍ | Brasil | 2203909 | 22 | 33 | nan | nan | nan | Caatinga | 3.2 |
| ca22e3f2-660f-33dc-808d-9fbc8fce41b0 | -9.79483 | -47.75323 | 2025-07-02 03:36:00 | NOAA-20 | RIO SONO | TOCANTINS | Brasil | 1718758 | 17 | 33 | nan | nan | nan | Cerrado | 4.8 |
| 365eccff-bc27-371f-ac83-feedfe9075ad | -7.1913 | -43.17538 | 2025-07-02 03:36:00 | NOAA-20 | FLORIANO | PIAUÍ | Brasil | 2203909 | 22 | 33 | nan | nan | nan | Caatinga | 0.9 |
| b8099fbb-06a7-3987-8e4d-9600c3bba81b | -7.80771 | -44.01709 | 2025-07-02 03:36:00 | NOAA-20 | SEBASTIÃO LEAL | PIAUÍ | Brasil | 2210631 | 22 | 33 | nan | nan | nan | Cerrado | 42.7 |
| 7edf5de6-82b8-3289-bb00-d53735133c4e | -7.79291 | -44.02251 | 2025-07-02 03:36:00 | NOAA-20 | SEBASTIÃO LEAL | PIAUÍ | Brasil | 2210631 | 22 | 33 | nan | nan | nan | Cerrado | 8.6 |
| b6b9eb7b-cfe0-3885-83e1-a602f464377c | -7.80703 | -44.0209 | 2025-07-02 03:36:00 | NOAA-20 | SEBASTIÃO LEAL | PIAUÍ | Brasil | 2210631 | 22 | 33 | nan | nan | nan | Cerrado | 42.7 |
| 63cf55a0-60d9-3d6e-90e2-d61f06fd150c | -11.84183 | -43.80421 | 2025-07-02 03:36:00 | NOAA-20 | WANDERLEY | BAHIA | Brasil | 2933455 | 29 | 33 | nan | nan | nan | Cerrado | 1.1 |
| 5f8db0ba-279f-3825-b591-2543376bf4d0 | -8.10222 | -42.99629 | 2025-07-02 03:36:00 | NOAA-20 | CANTO DO BURITI | PIAUÍ | Brasil | 2202307 | 22 | 33 | nan | nan | nan | Caatinga | 0.5 |
| aae2a917-0155-35b8-adf4-2d04585e43ac | -7.21744 | -43.08914 | 2025-07-02 03:36:00 | NOAA-20 | FLORIANO | PIAUÍ | Brasil | 2203909 | 22 | 33 | nan | nan | nan | Caatinga | 11.2 |
| 099b987f-2ec6-3694-9cf4-63952c581cf4 | -7.21627 | -43.09584 | 2025-07-02 03:36:00 | NOAA-20 | FLORIANO | PIAUÍ | Brasil | 2203909 | 22 | 33 | nan | nan | nan | Caatinga | 9.5 |
| 2f9504b5-559b-3204-ab46-7a9f8aa3b7a2 | -7.81757 | -44.02679 | 2025-07-02 03:36:00 | NOAA-20 | SEBASTIÃO LEAL | PIAUÍ | Brasil | 2210631 | 22 | 33 | nan | nan | nan | Cerrado | 9.2 |
| 4bc23afb-fea9-3ce4-917b-862aee5ba192 | -7.79444 | -44.02651 | 2025-07-02 03:36:00 | NOAA-20 | SEBASTIÃO LEAL | PIAUÍ | Brasil | 2210631 | 22 | 33 | nan | nan | nan | Cerrado | 5.3 |
| 39008716-9396-3954-b855-6d9abaad0953 | -7.78952 | -44.02164 | 2025-07-02 03:36:00 | NOAA-20 | SEBASTIÃO LEAL | PIAUÍ | Brasil | 2210631 | 22 | 33 | nan | nan | nan | Cerrado | 5.3 |


[Clique aqui para ver as próximas entradas](README6.md)
