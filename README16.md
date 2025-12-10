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

## Dados Diários - Página 16

| ID | Latitude | Longitude | Data/Hora GMT | Satélite | Município | Estado | País | Município ID | Estado ID | País ID | Dias sem Chuva | Precipitação | Risco de Fogo | Bioma | FRP |
|----|----------|-----------|---------------|----------|-----------|--------|------|--------------|-----------|---------|----------------|--------------|----------------|-------|-----|
| 79cdef2b-93b4-3c55-89f2-47b512d559eb | -8.86191 | -43.87572 | 2025-12-10 11:57:00 | TERRA_M-M | CRISTINO CASTRO | PIAUÍ | Brasil | 2203107 | 22 | 33 | nan | nan | nan | Cerrado | 4.4 |
| 2cd09cd0-9e41-3617-9d49-4ae0d66773e7 | -5.65324 | -37.55539 | 2025-12-10 11:57:00 | TERRA_M-M | CARAÚBAS | RIO GRANDE DO NORTE | Brasil | 2402303 | 24 | 33 | nan | nan | nan | Caatinga | 18.5 |
| ee9736d8-e6c5-3b62-a135-8deca0ed3502 | -9.81156 | -43.93742 | 2025-12-10 11:57:00 | TERRA_M-M | MORRO CABEÇA NO TEMPO | PIAUÍ | Brasil | 2206654 | 22 | 33 | nan | nan | nan | Cerrado | 193.7 |
| 48dc3438-ff6d-3523-902b-08251c07e6e6 | -7.91921 | -41.80175 | 2025-12-10 11:57:00 | TERRA_M-M | SIMPLÍCIO MENDES | PIAUÍ | Brasil | 2210805 | 22 | 33 | nan | nan | nan | Caatinga | 9.5 |
| ab3d53a2-ce54-3150-b6c2-c3ee0359ab2d | -12.26769 | -38.8091 | 2025-12-10 11:57:00 | TERRA_M-M | CORAÇÃO DE MARIA | BAHIA | Brasil | 2908903 | 29 | 33 | nan | nan | nan | Caatinga | 21.9 |
| 4e4f3edb-9c08-3871-bd19-6014a35d5494 | -7.34881 | -37.30618 | 2025-12-10 11:57:00 | TERRA_M-M | BREJINHO | PERNAMBUCO | Brasil | 2602506 | 26 | 33 | nan | nan | nan | Caatinga | 21.2 |
| 8051fe61-bc3d-372b-8c79-fb9a96785312 | -8.17426 | -38.76107 | 2025-12-10 11:57:00 | TERRA_M-M | MIRANDIBA | PERNAMBUCO | Brasil | 2609303 | 26 | 33 | nan | nan | nan | Caatinga | 11.4 |
| ce797cf0-83bf-31e5-82a4-e7ad4159aa96 | -5.16736 | -43.12069 | 2025-12-10 11:57:00 | TERRA_M-M | TIMON | MARANHÃO | Brasil | 2112209 | 21 | 33 | nan | nan | nan | Cerrado | 10.0 |
| 123748d9-2c12-3d01-9e0f-91a7542a0008 | -5.65885 | -37.56192 | 2025-12-10 11:57:00 | TERRA_M-M | CARAÚBAS | RIO GRANDE DO NORTE | Brasil | 2402303 | 24 | 33 | nan | nan | nan | Caatinga | 12.5 |
| aa9b54ca-1603-3f4a-944d-c4902c88e085 | -9.81029 | -43.9463 | 2025-12-10 11:57:00 | TERRA_M-M | MORRO CABEÇA NO TEMPO | PIAUÍ | Brasil | 2206654 | 22 | 33 | nan | nan | nan | Cerrado | 34.2 |
| 53057b53-6e75-3f76-af0d-0df9896b26b9 | -5.88913 | -42.5912 | 2025-12-10 11:57:00 | TERRA_M-M | OLHO D'ÁGUA DO PIAUÍ | PIAUÍ | Brasil | 2207108 | 22 | 33 | nan | nan | nan | Caatinga | 48.0 |
| 7a875358-a9b1-39f0-9ed5-19102e038b33 | -5.32594 | -43.56628 | 2025-12-10 11:57:00 | TERRA_M-M | MATÕES | MARANHÃO | Brasil | 2106607 | 21 | 33 | nan | nan | nan | Cerrado | 6.4 |
| 696d3429-d553-3d8f-b9ec-82024c62c32d | -5.32722 | -43.55743 | 2025-12-10 11:57:00 | TERRA_M-M | MATÕES | MARANHÃO | Brasil | 2106607 | 21 | 33 | nan | nan | nan | Cerrado | 15.8 |
| 5b9b86be-81ea-37ac-88a6-b6f917c07378 | -7.60927 | -42.3686 | 2025-12-10 11:57:00 | TERRA_M-M | SÃO MIGUEL DO FIDALGO | PIAUÍ | Brasil | 2210391 | 22 | 33 | nan | nan | nan | Caatinga | 6.2 |
| eef3bdf8-fa90-3720-9108-d36e384eb7c7 | -9.81283 | -43.92854 | 2025-12-10 11:57:00 | TERRA_M-M | MORRO CABEÇA NO TEMPO | PIAUÍ | Brasil | 2206654 | 22 | 33 | nan | nan | nan | Cerrado | 17.3 |
| 66e11ac8-ef3f-30e7-9896-463883d8a4f5 | -8.17505 | -38.75211 | 2025-12-10 11:57:00 | TERRA_M-M | MIRANDIBA | PERNAMBUCO | Brasil | 2609303 | 26 | 33 | nan | nan | nan | Caatinga | 23.9 |
| 017d41eb-f3f8-31cf-b6f7-9d9322393d92 | -8.23046 | -40.95893 | 2025-12-10 11:57:00 | TERRA_M-M | ACAUÃ | PIAUÍ | Brasil | 2200053 | 22 | 33 | nan | nan | nan | Caatinga | 7.3 |
| 1e672bd1-1ff1-3d4f-b639-01e13ab181d6 | -9.80274 | -43.93616 | 2025-12-10 11:57:00 | TERRA_M-M | MORRO CABEÇA NO TEMPO | PIAUÍ | Brasil | 2206654 | 22 | 33 | nan | nan | nan | Cerrado | 5.7 |
| d94a387a-ea8d-3ba7-bc82-417c7049fc20 | -5.93258 | -38.11264 | 2025-12-10 11:57:00 | TERRA_M-M | RODOLFO FERNANDES | RIO GRANDE DO NORTE | Brasil | 2411007 | 24 | 33 | nan | nan | nan | Caatinga | 15.8 |
| 581465c4-0cac-3b1e-a41c-00e02bfbdc54 | -7.52097 | -38.31876 | 2025-12-10 11:57:00 | TERRA_M-M | IBIARA | PARAÍBA | Brasil | 2506608 | 25 | 33 | nan | nan | nan | Caatinga | 21.8 |
| 8924660a-5780-35ec-9bf5-7fb473beabad | -5.93048 | -38.12817 | 2025-12-10 11:57:00 | TERRA_M-M | RODOLFO FERNANDES | RIO GRANDE DO NORTE | Brasil | 2411007 | 24 | 33 | nan | nan | nan | Caatinga | 33.7 |
| 808d7836-1f73-31b9-9220-0d7f17ea64f4 | -6.8113 | -38.75099 | 2025-12-10 11:57:00 | TERRA_M-M | IPAUMIRIM | CEARÁ | Brasil | 2305704 | 23 | 33 | nan | nan | nan | Caatinga | 14.7 |
| 6ba0e3e9-dd78-3645-9f38-ce9333df1c98 | -7.36991 | -38.86098 | 2025-12-10 11:57:00 | TERRA_M-M | MILAGRES | CEARÁ | Brasil | 2308302 | 23 | 33 | nan | nan | nan | Caatinga | 16.9 |
| 190a4cce-7919-3d2f-9483-6ce566d55eaf | -4.44186 | -42.00974 | 2025-12-10 11:57:00 | TERRA_M-M | CAPITÃO DE CAMPOS | PIAUÍ | Brasil | 2202406 | 22 | 33 | nan | nan | nan | Caatinga | 25.1 |
| 08a8e619-1192-390a-adf1-cc032edc0a81 | -5.11594 | -38.21111 | 2025-12-10 11:57:00 | TERRA_M-M | LIMOEIRO DO NORTE | CEARÁ | Brasil | 2307601 | 23 | 33 | nan | nan | nan | Caatinga | 16.6 |
| c27e19ef-3a64-37c9-b78e-16ab9e7d534f | -7.96815 | -37.78612 | 2025-12-10 11:57:00 | TERRA_M-M | FLORES | PERNAMBUCO | Brasil | 2605608 | 26 | 33 | nan | nan | nan | Caatinga | 20.9 |
| e25a2bf2-4377-33fc-a62f-1f4751d0bfba | -5.53319 | -41.66126 | 2025-12-10 11:57:00 | TERRA_M-M | CASTELO DO PIAUÍ | PIAUÍ | Brasil | 2202604 | 22 | 33 | nan | nan | nan | Caatinga | 13.7 |
| 6f19c336-3d45-39be-b2b4-5434d8a9186b | -8.20917 | -37.53019 | 2025-12-10 11:57:00 | TERRA_M-M | SERTÂNIA | PERNAMBUCO | Brasil | 2614105 | 26 | 33 | nan | nan | nan | Caatinga | 24.6 |
| 2af2487d-3d28-32c7-a3ba-331d771821b1 | -7.54627 | -41.17451 | 2025-12-10 11:57:00 | TERRA_M-M | MASSAPÊ DO PIAUÍ | PIAUÍ | Brasil | 2206050 | 22 | 33 | nan | nan | nan | Caatinga | 11.6 |
| fd1883a3-44fd-32b9-bcf5-671b54722011 | -7.54485 | -41.18475 | 2025-12-10 11:57:00 | TERRA_M-M | MASSAPÊ DO PIAUÍ | PIAUÍ | Brasil | 2206050 | 22 | 33 | nan | nan | nan | Caatinga | 7.6 |
| 8a2bf345-2d6c-3a1d-873f-47f400befa66 | -4.8306 | -42.97462 | 2025-12-10 11:57:00 | TERRA_M-M | CAXIAS | MARANHÃO | Brasil | 2103000 | 21 | 33 | nan | nan | nan | Cerrado | 29.0 |
| 79e11067-da82-3a8e-841f-e9e1cf1789ac | -4.98451 | -41.29999 | 2025-12-10 11:57:00 | TERRA_M-M | BURITI DOS MONTES | PIAUÍ | Brasil | 2202026 | 22 | 33 | nan | nan | nan | Caatinga | 19.3 |
| 0f952552-30be-375d-b2ec-e479123b5bcd | -8.69158 | -40.5095 | 2025-12-10 11:57:00 | TERRA_M-M | PETROLINA | PERNAMBUCO | Brasil | 2611101 | 26 | 33 | nan | nan | nan | Caatinga | 8.5 |
| aa3e68f2-b51c-358f-b491-da3698f86d5e | -6.5474 | -43.60262 | 2025-12-10 11:57:00 | TERRA_M-M | SÃO JOÃO DOS PATOS | MARANHÃO | Brasil | 2111102 | 21 | 33 | nan | nan | nan | Cerrado | 5.9 |
| 3a567d69-c29e-3ad2-b6ea-4ed18d7088ed | -5.8904 | -42.58232 | 2025-12-10 11:57:00 | TERRA_M-M | OLHO D'ÁGUA DO PIAUÍ | PIAUÍ | Brasil | 2207108 | 22 | 33 | nan | nan | nan | Caatinga | 49.9 |
| 0190a42a-04da-323b-a202-a1f9900850a3 | -4.77486 | -42.19896 | 2025-12-10 11:57:00 | TERRA_M-M | CAMPO MAIOR | PIAUÍ | Brasil | 2202208 | 22 | 33 | nan | nan | nan | Caatinga | 7.7 |
| 585a51d5-b773-3f64-9e08-f095e98071b2 | -8.2703 | -36.62506 | 2025-12-10 11:57:00 | TERRA_M-M | PESQUEIRA | PERNAMBUCO | Brasil | 2610905 | 26 | 33 | nan | nan | nan | Caatinga | 44.1 |
| 8940e574-9e77-3d0c-9f5a-941b34fece6a | -13.15717 | -43.01632 | 2025-12-10 11:59:00 | TERRA_M-M | BOM JESUS DA LAPA | BAHIA | Brasil | 2903904 | 29 | 33 | nan | nan | nan | Caatinga | 19.4 |
| eda7c012-fd14-3250-a690-e1b05e0383da | -14.02153 | -39.32022 | 2025-12-10 11:59:00 | TERRA_M-M | CAMAMU | BAHIA | Brasil | 2905800 | 29 | 33 | nan | nan | nan | Mata Atlântica | 16.3 |
| d7b28ac7-0c1b-3910-b0bc-6187f36f34f7 | -12.94413 | -42.01063 | 2025-12-10 11:59:00 | TERRA_M-M | PIATÃ | BAHIA | Brasil | 2924306 | 29 | 33 | nan | nan | nan | Caatinga | 5.4 |
| a871f60b-41f2-3cae-a005-547ffba90141 | -12.43272 | -43.72342 | 2025-12-10 11:59:00 | TERRA_M-M | BREJOLÂNDIA | BAHIA | Brasil | 2904407 | 29 | 33 | nan | nan | nan | Cerrado | 9.1 |
| b84d3954-2d41-3a9a-8113-75189f1c91d6 | -3.405 | -42.1199 | 2025-12-10 12:20:00 | GOES-19 | JOAQUIM PIRES | PIAUÍ | Brasil | 2205409 | 22 | 33 | nan | nan | nan | Caatinga | 83.0 |
| a669eda0-7cac-30d4-919a-f2f30fa057ea | -6.8199 | -38.7415 | 2025-12-10 12:40:00 | GOES-19 | IPAUMIRIM | CEARÁ | Brasil | 2305704 | 23 | 33 | nan | nan | nan | Caatinga | 86.3 |
| d04c8e74-394b-33f5-a244-d5d756354a17 | -3.5919 | -42.1107 | 2025-12-10 12:40:00 | GOES-19 | JOAQUIM PIRES | PIAUÍ | Brasil | 2205409 | 22 | 33 | nan | nan | nan | Caatinga | 79.7 |
| 11b4b515-5074-3b90-8e6d-fe8c9fe402bc | -3.5919 | -42.1107 | 2025-12-10 12:50:00 | GOES-19 | JOAQUIM PIRES | PIAUÍ | Brasil | 2205409 | 22 | 33 | nan | nan | nan | Caatinga | 117.0 |
| 8c72ba9f-bf6e-3b4c-88db-9db0756baca4 | -5.9374 | -38.1181 | 2025-12-10 12:50:00 | GOES-19 | RODOLFO FERNANDES | RIO GRANDE DO NORTE | Brasil | 2411007 | 24 | 33 | nan | nan | nan | Caatinga | 95.6 |
| 2b1e7442-ab81-31d2-8d32-3ae1497b32f2 | -5.0026 | -41.3062 | 2025-12-10 13:40:00 | GOES-19 | BURITI DOS MONTES | PIAUÍ | Brasil | 2202026 | 22 | 33 | nan | nan | nan | Caatinga | 92.4 |
| 03a88dd5-41f5-317f-a977-ed59c57b2e8e | -2.9943 | -42.0434 | 2025-12-10 13:40:00 | GOES-19 | ARAIOSES | MARANHÃO | Brasil | 2100907 | 21 | 33 | nan | nan | nan | Cerrado | 99.2 |
| c52fdb28-3649-353c-b7c5-b2292d2b8f5e | -3.4089 | -41.4273 | 2025-12-10 13:40:00 | GOES-19 | COCAL | PIAUÍ | Brasil | 2202703 | 22 | 33 | nan | nan | nan | Caatinga | 87.5 |
| ab27652d-4f20-33b6-b6a5-286c422551a1 | -4.9838 | -41.3076 | 2025-12-10 13:40:00 | GOES-19 | BURITI DOS MONTES | PIAUÍ | Brasil | 2202026 | 22 | 33 | nan | nan | nan | Caatinga | 95.0 |
| 23b2e5ef-22cc-3693-91c2-65c2b69a41d4 | -4.9838 | -41.3076 | 2025-12-10 13:50:00 | GOES-19 | BURITI DOS MONTES | PIAUÍ | Brasil | 2202026 | 22 | 33 | nan | nan | nan | Caatinga | 103.3 |
| 7fd5bb84-810e-3765-9787-ace7f92eba03 | -3.4089 | -41.4273 | 2025-12-10 13:50:00 | GOES-19 | COCAL | PIAUÍ | Brasil | 2202703 | 22 | 33 | nan | nan | nan | Caatinga | 89.0 |
| cdbbe561-ee49-3465-ad68-3393ac78426a | -5.0028 | -41.2821 | 2025-12-10 13:50:00 | GOES-19 | BURITI DOS MONTES | PIAUÍ | Brasil | 2202026 | 22 | 33 | nan | nan | nan | Caatinga | 87.7 |
| b3a3cb96-3992-3e54-bbab-1eefad19635e | -8.8182 | -37.3725 | 2025-12-10 14:00:00 | GOES-19 | ITAÍBA | PERNAMBUCO | Brasil | 2607505 | 26 | 33 | nan | nan | nan | Caatinga | 88.5 |
| 857a92eb-9585-30a0-af2d-8109a6379ce7 | -2.2161 | -45.6624 | 2025-12-10 14:00:00 | GOES-19 | TURILÂNDIA | MARANHÃO | Brasil | 2112456 | 21 | 33 | nan | nan | nan | Amazônia | 98.0 |
| 19aee3ee-4c0b-32d6-803d-56a8eea2b376 | -3.4089 | -41.4273 | 2025-12-10 14:00:00 | GOES-19 | COCAL | PIAUÍ | Brasil | 2202703 | 22 | 33 | nan | nan | nan | Caatinga | 83.2 |
| f5203dae-ebdd-3474-a251-38863228886c | -2.2161 | -45.6624 | 2025-12-10 14:10:00 | GOES-19 | TURILÂNDIA | MARANHÃO | Brasil | 2112456 | 21 | 33 | nan | nan | nan | Amazônia | 89.3 |
| e9ee26f3-f211-3a07-a87e-4d67979e02ed | -2.9949 | -41.9245 | 2025-12-10 14:10:00 | GOES-19 | ARAIOSES | MARANHÃO | Brasil | 2100907 | 21 | 33 | nan | nan | nan | Caatinga | 100.7 |
| 9bdd716d-d77d-3ff2-929d-9d2b769d91e7 | -1.6415 | -45.4295 | 2025-12-10 14:20:00 | GOES-19 | TURIAÇU | MARANHÃO | Brasil | 2112407 | 21 | 33 | nan | nan | nan | Amazônia | 109.7 |
| 98dd2ddd-bbc2-30ee-a5ac-956114010a5c | -2.2704 | -46.0846 | 2025-12-10 14:30:00 | GOES-19 | CENTRO DO GUILHERME | MARANHÃO | Brasil | 2103158 | 21 | 33 | nan | nan | nan | Amazônia | 69.0 |


