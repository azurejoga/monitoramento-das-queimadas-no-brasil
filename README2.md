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
| 840e2388-fac2-3943-99f9-588d65fba049 | -10.7345 | -44.9049 | 2024-10-30 00:05:56 | METOP-C | SEBASTIÃO BARROS | PIAUÍ | Brasil | 2210623 | 22 | 33 | nan | nan | nan | Cerrado | nan |
| b314dbe7-b8a6-35b0-969f-e2d6f975d926 | -10.7379 | -44.921299 | 2024-10-30 00:05:56 | METOP-C | CRISTALÂNDIA DO PIAUÍ | PIAUÍ | Brasil | 2203008 | 22 | 33 | nan | nan | nan | Cerrado | nan |
| e1406d2d-44c2-334a-90fc-6e6b1eb80ed1 | -8.5652 | -35.0616 | 2024-10-30 00:05:56 | METOP-C | IPOJUCA | PERNAMBUCO | Brasil | 2607208 | 26 | 33 | nan | nan | nan | Mata Atlântica | nan |
| c82c1982-ee94-3314-a523-f102e0cc0ad2 | -10.7214 | -44.890499 | 2024-10-30 00:05:56 | METOP-C | SEBASTIÃO BARROS | PIAUÍ | Brasil | 2210623 | 22 | 33 | nan | nan | nan | Cerrado | nan |
| 385416a5-523e-33c5-9835-a9c37e1df6bd | -10.7247 | -44.906799 | 2024-10-30 00:05:56 | METOP-C | SEBASTIÃO BARROS | PIAUÍ | Brasil | 2210623 | 22 | 33 | nan | nan | nan | Cerrado | nan |
| 0fe9994e-3ad7-3fb6-a8c0-89659d7a68fb | -10.7281 | -44.923199 | 2024-10-30 00:05:56 | METOP-C | CRISTALÂNDIA DO PIAUÍ | PIAUÍ | Brasil | 2203008 | 22 | 33 | nan | nan | nan | Cerrado | nan |
| 3c7e2115-7039-3566-a90e-773b98409240 | -10.6274 | -44.926601 | 2024-10-30 00:05:58 | METOP-C | SEBASTIÃO BARROS | PIAUÍ | Brasil | 2210623 | 22 | 33 | nan | nan | nan | Cerrado | nan |
| 756fb232-9465-3c74-ae76-d2e007b5d451 | -8.4598 | -35.272499 | 2024-10-30 00:05:59 | METOP-C | ESCADA | PERNAMBUCO | Brasil | 2605202 | 26 | 33 | nan | nan | nan | Mata Atlântica | nan |
| b2f661c7-4f81-3a72-8ff1-91ee653cd3bc | -9.4848 | -62.6701 | 2024-10-30 00:06:00 | GOES-16 | CUJUBIM | RONDÔNIA | Brasil | 1100940 | 11 | 33 | nan | nan | nan | Amazônia | 49.5 |
| 282fd401-90b4-3062-a817-2e2e17f857ee | -9.5563 | -63.1411 | 2024-10-30 00:06:01 | GOES-16 | ALTO PARAÍSO | RONDÔNIA | Brasil | 1100403 | 11 | 33 | nan | nan | nan | Amazônia | 63.7 |
| 39f35b8a-f12e-3dd7-8df7-492880c6f985 | -10.7171 | -44.9391 | 2024-10-30 00:06:06 | GOES-16 | CRISTALÂNDIA DO PIAUÍ | PIAUÍ | Brasil | 2203008 | 22 | 33 | nan | nan | nan | Cerrado | 106.6 |
| 9df35c54-767b-30cc-9cf9-a66db2570b31 | -10.7175 | -44.916 | 2024-10-30 00:06:06 | GOES-16 | SEBASTIÃO BARROS | PIAUÍ | Brasil | 2210623 | 22 | 33 | nan | nan | nan | Cerrado | 167.0 |
| bad94ba5-97dc-366c-aba5-2c83d7b32885 | -7.6346 | -34.880699 | 2024-10-30 00:06:10 | METOP-C | GOIANA | PERNAMBUCO | Brasil | 2606200 | 26 | 33 | nan | nan | nan | Mata Atlântica | nan |
| e2f8ab28-9e22-3da2-8fc1-895762985127 | -12.6953 | -48.8503 | 2024-10-30 00:06:17 | GOES-16 | TALISMÃ | TOCANTINS | Brasil | 1720978 | 17 | 33 | nan | nan | nan | Cerrado | 58.8 |
| b8f6955a-246f-35c7-b5b8-eb1ac73931f5 | -12.899 | -45.0549 | 2024-10-30 00:06:18 | GOES-16 | SÃO DESIDÉRIO | BAHIA | Brasil | 2928901 | 29 | 33 | nan | nan | nan | Cerrado | 91.9 |
| 4e4a129c-92c6-3e2d-82e9-609846371a69 | -8.3159 | -40.534801 | 2024-10-30 00:06:20 | METOP-C | SANTA FILOMENA | PERNAMBUCO | Brasil | 2612554 | 26 | 33 | nan | nan | nan | Caatinga | nan |
| 56491949-3e55-3a2e-b74d-2de7b45eed76 | -13.6887 | -46.1247 | 2024-10-30 00:06:22 | GOES-16 | CORRENTINA | BAHIA | Brasil | 2909307 | 29 | 33 | nan | nan | nan | Cerrado | 92.2 |
| 6bbd8afe-744e-3cba-b088-e5732ba47050 | -13.6891 | -46.1017 | 2024-10-30 00:06:22 | GOES-16 | CORRENTINA | BAHIA | Brasil | 2909307 | 29 | 33 | nan | nan | nan | Cerrado | 195.0 |
| 8d5b085d-af7f-3d27-8b79-bd33131be59a | -13.6896 | -46.0787 | 2024-10-30 00:06:22 | GOES-16 | CORRENTINA | BAHIA | Brasil | 2909307 | 29 | 33 | nan | nan | nan | Cerrado | 75.7 |
| c028ee21-e079-30fd-a453-fcaea6deff01 | -6.9849 | -35.191502 | 2024-10-30 00:06:22 | METOP-C | SAPÉ | PARAÍBA | Brasil | 2515302 | 25 | 33 | nan | nan | nan | Mata Atlântica | nan |
| 445333da-82a6-346d-ab42-637bb48a93df | -6.9868 | -35.199402 | 2024-10-30 00:06:22 | METOP-C | SAPÉ | PARAÍBA | Brasil | 2515302 | 25 | 33 | nan | nan | nan | Mata Atlântica | nan |
| 35c70b13-aa9a-32e4-8933-cf500c9d8557 | -6.9886 | -35.207298 | 2024-10-30 00:06:22 | METOP-C | SAPÉ | PARAÍBA | Brasil | 2515302 | 25 | 33 | nan | nan | nan | Mata Atlântica | nan |
| 49bdbdaa-2a15-3742-aabf-2abce90a25f5 | -6.8185 | -35.230099 | 2024-10-30 00:06:25 | METOP-C | ITAPOROROCA | PARAÍBA | Brasil | 2507101 | 25 | 33 | nan | nan | nan | Caatinga | nan |
| b47682bd-eccf-326a-bb10-3892c4a538df | -6.8204 | -35.237999 | 2024-10-30 00:06:25 | METOP-C | ITAPOROROCA | PARAÍBA | Brasil | 2507101 | 25 | 33 | nan | nan | nan | Caatinga | nan |
| 4517354d-5faa-384b-ae0e-2ba757018497 | -7.5864 | -38.7425 | 2024-10-30 00:06:26 | METOP-C | MAURITI | CEARÁ | Brasil | 2308104 | 23 | 33 | nan | nan | nan | Caatinga | nan |
| 521399ba-2731-3c92-a936-8e61c8ad6985 | -7.5879 | -38.7495 | 2024-10-30 00:06:26 | METOP-C | MAURITI | CEARÁ | Brasil | 2308104 | 23 | 33 | nan | nan | nan | Caatinga | nan |
| 3e932e58-577a-33c2-9988-44a84d9dc0f3 | -7.5797 | -38.758701 | 2024-10-30 00:06:26 | METOP-C | MAURITI | CEARÁ | Brasil | 2308104 | 23 | 33 | nan | nan | nan | Caatinga | nan |
| 58e70814-cb09-3ffa-a073-2dd2d8672c26 | -7.5683 | -38.753899 | 2024-10-30 00:06:26 | METOP-C | MAURITI | CEARÁ | Brasil | 2308104 | 23 | 33 | nan | nan | nan | Caatinga | nan |
| 8993cd4c-40b5-3ec2-94f3-5d274ce4f22e | -7.7092 | -39.517399 | 2024-10-30 00:06:26 | METOP-C | MOREILÂNDIA | PERNAMBUCO | Brasil | 2614303 | 26 | 33 | nan | nan | nan | Caatinga | nan |
| 0353a210-cdf4-3a48-81bf-af459a0f165b | -7.7109 | -39.5247 | 2024-10-30 00:06:26 | METOP-C | MOREILÂNDIA | PERNAMBUCO | Brasil | 2614303 | 26 | 33 | nan | nan | nan | Caatinga | nan |
| dd473183-b70f-3b92-9da4-cb91ffe0ecfd | -7.4006 | -38.6959 | 2024-10-30 00:06:28 | METOP-C | MAURITI | CEARÁ | Brasil | 2308104 | 23 | 33 | nan | nan | nan | Caatinga | nan |
| e78bbf91-a130-3e9a-ae0e-6db2c5dbe5fa | -6.5663 | -35.255402 | 2024-10-30 00:06:29 | METOP-C | JACARAÚ | PARAÍBA | Brasil | 2507309 | 25 | 33 | nan | nan | nan | Caatinga | nan |
| 5cbb3c39-4036-3cce-9b50-cc52060063ed | -6.5682 | -35.263302 | 2024-10-30 00:06:29 | METOP-C | JACARAÚ | PARAÍBA | Brasil | 2507309 | 25 | 33 | nan | nan | nan | Caatinga | nan |
| ec79651e-7b5f-3f6c-936c-540cde3730c9 | -6.7866 | -37.539299 | 2024-10-30 00:06:34 | METOP-C | MALTA | PARAÍBA | Brasil | 2508802 | 25 | 33 | nan | nan | nan | Caatinga | nan |
| f1149fa0-4131-35ab-8696-38c9612496d8 | -7.9355 | -42.8311 | 2024-10-30 00:06:35 | METOP-C | PAJEÚ DO PIAUÍ | PIAUÍ | Brasil | 2207355 | 22 | 33 | nan | nan | nan | Caatinga | nan |
| c9d1d680-49ab-36f6-80ac-5b2fa1b73850 | -6.7331 | -37.486301 | 2024-10-30 00:06:35 | METOP-C | SÃO JOSÉ DE ESPINHARAS | PARAÍBA | Brasil | 2514404 | 25 | 33 | nan | nan | nan | Caatinga | nan |
| ec85f890-0c7c-31d0-b434-6cf3d36e0ef3 | -6.7347 | -37.493198 | 2024-10-30 00:06:35 | METOP-C | SÃO JOSÉ DE ESPINHARAS | PARAÍBA | Brasil | 2514404 | 25 | 33 | nan | nan | nan | Caatinga | nan |
| 31701831-01d5-38cc-a044-be7dc483e2a7 | -6.7217 | -37.481602 | 2024-10-30 00:06:35 | METOP-C | SÃO JOSÉ DE ESPINHARAS | PARAÍBA | Brasil | 2514404 | 25 | 33 | nan | nan | nan | Caatinga | nan |
| 3ff3bd30-569c-32a0-820e-9692f543a430 | -6.7233 | -37.488499 | 2024-10-30 00:06:35 | METOP-C | SÃO JOSÉ DE ESPINHARAS | PARAÍBA | Brasil | 2514404 | 25 | 33 | nan | nan | nan | Caatinga | nan |
| fe420ae1-6b3a-3d55-97c3-ba4688790166 | -6.7249 | -37.495399 | 2024-10-30 00:06:35 | METOP-C | SÃO JOSÉ DE ESPINHARAS | PARAÍBA | Brasil | 2514404 | 25 | 33 | nan | nan | nan | Caatinga | nan |
| abc6e95b-f6a0-32f9-ae90-160ef4fe0bec | -6.6958 | -37.458599 | 2024-10-30 00:06:35 | METOP-C | SERRA NEGRA DO NORTE | RIO GRANDE DO NORTE | Brasil | 2413409 | 24 | 33 | nan | nan | nan | Caatinga | nan |
| e20ee4ef-7ef1-3e84-9039-38f310cc4509 | -6.6974 | -37.4655 | 2024-10-30 00:06:35 | METOP-C | SERRA NEGRA DO NORTE | RIO GRANDE DO NORTE | Brasil | 2413409 | 24 | 33 | nan | nan | nan | Caatinga | nan |
| ac611f11-c5eb-36b9-a761-9b8636b7b156 | -6.699 | -37.472301 | 2024-10-30 00:06:35 | METOP-C | SERRA NEGRA DO NORTE | RIO GRANDE DO NORTE | Brasil | 2413409 | 24 | 33 | nan | nan | nan | Caatinga | nan |
| ba8cb49f-29a5-36de-bafa-f1ed16e9eb70 | -7.3538 | -41.854301 | 2024-10-30 00:06:41 | METOP-C | SANTO INÁCIO DO PIAUÍ | PIAUÍ | Brasil | 2209500 | 22 | 33 | nan | nan | nan | Caatinga | nan |
| 52864273-1aab-37dd-8966-f91f508da830 | -7.342 | -41.847198 | 2024-10-30 00:06:41 | METOP-C | SANTO INÁCIO DO PIAUÍ | PIAUÍ | Brasil | 2209500 | 22 | 33 | nan | nan | nan | Caatinga | nan |
| 5ae7bda0-0e15-349b-84f1-4c8084806537 | -7.344 | -41.8564 | 2024-10-30 00:06:41 | METOP-C | SANTO INÁCIO DO PIAUÍ | PIAUÍ | Brasil | 2209500 | 22 | 33 | nan | nan | nan | Caatinga | nan |
| f6ee9183-a883-331f-b46b-0db360ee0176 | -7.3461 | -41.8657 | 2024-10-30 00:06:41 | METOP-C | SANTO INÁCIO DO PIAUÍ | PIAUÍ | Brasil | 2209500 | 22 | 33 | nan | nan | nan | Caatinga | nan |
| ada376a3-d1bd-3376-a82b-238a9035dafb | -7.3363 | -41.867802 | 2024-10-30 00:06:41 | METOP-C | SANTO INÁCIO DO PIAUÍ | PIAUÍ | Brasil | 2209500 | 22 | 33 | nan | nan | nan | Caatinga | nan |
| 9446f22f-232e-3947-bb29-6d04b2504229 | -7.0075 | -41.307598 | 2024-10-30 00:06:44 | METOP-C | SANTO ANTÔNIO DE LISBOA | PIAUÍ | Brasil | 2209401 | 22 | 33 | nan | nan | nan | Caatinga | nan |
| f6ae55b2-522c-326f-8dd2-f5647331cc41 | -7.0094 | -41.316101 | 2024-10-30 00:06:44 | METOP-C | SUSSUAPARA | PIAUÍ | Brasil | 2210938 | 22 | 33 | nan | nan | nan | Caatinga | nan |
| bfd769ea-3118-3aea-8bc6-e04c544dadd7 | -6.9996 | -41.318298 | 2024-10-30 00:06:44 | METOP-C | BOCAINA | PIAUÍ | Brasil | 2201804 | 22 | 33 | nan | nan | nan | Caatinga | nan |
| 4ce3c98c-9d37-3056-baa6-cb824c429e98 | -7.0015 | -41.3269 | 2024-10-30 00:06:44 | METOP-C | SUSSUAPARA | PIAUÍ | Brasil | 2210938 | 22 | 33 | nan | nan | nan | Caatinga | nan |
| e0f612db-2d37-3a2b-b9fa-eaa35d7a3126 | -7.0034 | -41.3354 | 2024-10-30 00:06:44 | METOP-C | SUSSUAPARA | PIAUÍ | Brasil | 2210938 | 22 | 33 | nan | nan | nan | Caatinga | nan |
| c29efa9f-32e0-34b2-9ace-fc8961707cab | -7.0052 | -41.344002 | 2024-10-30 00:06:44 | METOP-C | SUSSUAPARA | PIAUÍ | Brasil | 2210938 | 22 | 33 | nan | nan | nan | Caatinga | nan |
| 940cfa20-540e-332b-bbe8-4ccd7b594edb | -6.9917 | -41.328999 | 2024-10-30 00:06:45 | METOP-C | BOCAINA | PIAUÍ | Brasil | 2201804 | 22 | 33 | nan | nan | nan | Caatinga | nan |
| 86a0412e-fb2f-3505-b520-6aac526bd1ea | -6.4167 | -38.901001 | 2024-10-30 00:06:45 | METOP-C | ICÓ | CEARÁ | Brasil | 2305407 | 23 | 33 | nan | nan | nan | Caatinga | nan |
| dd43789a-5267-3543-903c-d4cfa95827c6 | -6.4069 | -38.903198 | 2024-10-30 00:06:45 | METOP-C | ICÓ | CEARÁ | Brasil | 2305407 | 23 | 33 | nan | nan | nan | Caatinga | nan |
| 1c12e366-b00a-3168-bd9f-58f749c05b4c | -5.5762 | -35.567001 | 2024-10-30 00:06:46 | METOP-C | TAIPU | RIO GRANDE DO NORTE | Brasil | 2413904 | 24 | 33 | nan | nan | nan | Caatinga | nan |
| fd0f85f7-1f14-34d9-9c6a-a1bb73c2f31f | -5.578 | -35.574799 | 2024-10-30 00:06:46 | METOP-C | TAIPU | RIO GRANDE DO NORTE | Brasil | 2413904 | 24 | 33 | nan | nan | nan | Caatinga | nan |
| 01e097b4-d9d1-3ceb-b2aa-682278a30efd | -5.5798 | -35.5826 | 2024-10-30 00:06:46 | METOP-C | TAIPU | RIO GRANDE DO NORTE | Brasil | 2413904 | 24 | 33 | nan | nan | nan | Caatinga | nan |
| 3f314e9c-22ea-30c2-ae89-ab940fca7c91 | -18.2454 | -55.9793 | 2024-10-30 00:06:48 | GOES-16 | CORUMBÁ | MATO GROSSO DO SUL | Brasil | 5003207 | 50 | 33 | nan | nan | nan | Pantanal | 62.4 |
| 28fdbeb4-4e9d-3511-bb97-19b40c59c74d | -6.736 | -41.102699 | 2024-10-30 00:06:48 | METOP-C | PIMENTEIRAS | PIAUÍ | Brasil | 2208106 | 22 | 33 | nan | nan | nan | Caatinga | nan |
| 60f03497-3a59-33bc-8a9c-233fc5350583 | -6.4048 | -39.6688 | 2024-10-30 00:06:48 | METOP-C | JUCÁS | CEARÁ | Brasil | 2307403 | 23 | 33 | nan | nan | nan | Caatinga | nan |
| 9d4db040-7f93-309d-94d5-4a7fc77e39c9 | -6.4326 | -39.792198 | 2024-10-30 00:06:48 | METOP-C | SABOEIRO | CEARÁ | Brasil | 2311900 | 23 | 33 | nan | nan | nan | Caatinga | nan |
| 8c9b5ac9-8ebb-3eb5-bec6-bd339c2c430f | -6.4343 | -39.7995 | 2024-10-30 00:06:48 | METOP-C | SABOEIRO | CEARÁ | Brasil | 2311900 | 23 | 33 | nan | nan | nan | Caatinga | nan |
| f3910610-48ef-3800-977d-f23e07e19351 | -5.4513 | -35.562698 | 2024-10-30 00:06:48 | METOP-C | PUREZA | RIO GRANDE DO NORTE | Brasil | 2410405 | 24 | 33 | nan | nan | nan | Caatinga | nan |
| 8b4e5ba1-fa47-3f44-8c7f-22d8a4e45fd7 | -5.4532 | -35.570599 | 2024-10-30 00:06:48 | METOP-C | PUREZA | RIO GRANDE DO NORTE | Brasil | 2410405 | 24 | 33 | nan | nan | nan | Caatinga | nan |
| bdf64820-c77f-30dc-bc06-9d23b5fe2420 | -6.9762 | -42.517101 | 2024-10-30 00:06:49 | METOP-C | OEIRAS | PIAUÍ | Brasil | 2207009 | 22 | 33 | nan | nan | nan | Caatinga | nan |
| 642f8649-fe8b-3462-9e3a-e0cb8f291347 | -7.8876 | -46.8787 | 2024-10-30 00:06:49 | METOP-C | CAROLINA | MARANHÃO | Brasil | 2102804 | 21 | 33 | nan | nan | nan | Cerrado | nan |
| 38beb868-3b63-31a6-8de2-299d7d98bfdf | -7.8918 | -46.898998 | 2024-10-30 00:06:49 | METOP-C | CAROLINA | MARANHÃO | Brasil | 2102804 | 21 | 33 | nan | nan | nan | Cerrado | nan |
| f98fedd8-2cf5-3ed4-b8f4-8b4b11e9b8df | -7.8737 | -46.8605 | 2024-10-30 00:06:50 | METOP-C | CAROLINA | MARANHÃO | Brasil | 2102804 | 21 | 33 | nan | nan | nan | Cerrado | nan |
| 855c9a1a-85f8-3269-9d02-aaf9a98bfcf5 | -7.8779 | -46.880699 | 2024-10-30 00:06:50 | METOP-C | CAROLINA | MARANHÃO | Brasil | 2102804 | 21 | 33 | nan | nan | nan | Cerrado | nan |
| 1f0a9aa0-b018-3d56-8635-d335f1a821e8 | -7.8821 | -46.900902 | 2024-10-30 00:06:50 | METOP-C | CAROLINA | MARANHÃO | Brasil | 2102804 | 21 | 33 | nan | nan | nan | Cerrado | nan |
| 1715ad4f-7089-3a80-865e-b8334361db95 | -6.1619 | -39.4594 | 2024-10-30 00:06:51 | METOP-C | ACOPIARA | CEARÁ | Brasil | 2300309 | 23 | 33 | nan | nan | nan | Caatinga | nan |
| a51a0080-83ca-395b-845a-a5108594c7ed | -6.548 | -41.551701 | 2024-10-30 00:06:53 | METOP-C | LAGOA DO SÍTIO | PIAUÍ | Brasil | 2205599 | 22 | 33 | nan | nan | nan | Caatinga | nan |
| ed233691-6152-3408-82e9-6de6e8ebfc08 | -6.5499 | -41.560398 | 2024-10-30 00:06:53 | METOP-C | LAGOA DO SÍTIO | PIAUÍ | Brasil | 2205599 | 22 | 33 | nan | nan | nan | Caatinga | nan |
| 4a04dbf7-7f22-3a74-9622-62843829e256 | -19.5862 | -56.7136 | 2024-10-30 00:06:55 | GOES-16 | AQUIDAUANA | MATO GROSSO DO SUL | Brasil | 5001102 | 50 | 33 | nan | nan | nan | Pantanal | 67.5 |
| 296da1b2-8667-333d-897b-ab8c5e59745d | -19.6063 | -56.7108 | 2024-10-30 00:06:55 | GOES-16 | AQUIDAUANA | MATO GROSSO DO SUL | Brasil | 5001102 | 50 | 33 | nan | nan | nan | Pantanal | 67.1 |
| 24dc6396-0156-37a5-946e-c885be624c63 | -6.7108 | -43.036701 | 2024-10-30 00:06:55 | METOP-C | BARÃO DE GRAJAÚ | MARANHÃO | Brasil | 2101509 | 21 | 33 | nan | nan | nan | Cerrado | nan |
| fcdbb1ff-04a7-36ef-9abf-abeda82f6d5c | -6.7131 | -43.047298 | 2024-10-30 00:06:55 | METOP-C | BARÃO DE GRAJAÚ | MARANHÃO | Brasil | 2101509 | 21 | 33 | nan | nan | nan | Cerrado | nan |
| 406ff34c-9cd5-3c60-bc1a-ff387edaaefc | -6.3928 | -41.731998 | 2024-10-30 00:06:56 | METOP-C | VALENÇA DO PIAUÍ | PIAUÍ | Brasil | 2211308 | 22 | 33 | nan | nan | nan | Caatinga | nan |
| 5208e13c-c619-3575-904f-5a58eead31d9 | -6.3482 | -41.577 | 2024-10-30 00:06:56 | METOP-C | LAGOA DO SÍTIO | PIAUÍ | Brasil | 2205599 | 22 | 33 | nan | nan | nan | Caatinga | nan |
| c5e91d20-9927-3593-a536-1346c827f80b | -5.4689 | -38.045502 | 2024-10-30 00:06:57 | METOP-C | ALTO SANTO | CEARÁ | Brasil | 2300705 | 23 | 33 | nan | nan | nan | Caatinga | nan |
| 8d986354-b998-3b4f-a43f-cd056f232244 | -6.2521 | -41.606998 | 2024-10-30 00:06:58 | METOP-C | PIMENTEIRAS | PIAUÍ | Brasil | 2208106 | 22 | 33 | nan | nan | nan | Caatinga | nan |
| 2405161f-186d-3094-b8e5-b87ea0a5c9c7 | -5.2457 | -37.612701 | 2024-10-30 00:06:59 | METOP-C | BARAÚNA | RIO GRANDE DO NORTE | Brasil | 2401453 | 24 | 33 | nan | nan | nan | Caatinga | nan |
| 666cd73c-5180-3f52-b6cb-6d8420bc1c1b | -5.6953 | -39.901901 | 2024-10-30 00:07:00 | METOP-C | MOMBAÇA | CEARÁ | Brasil | 2308500 | 23 | 33 | nan | nan | nan | Caatinga | nan |
| 74c8ed75-ffdd-31ac-88cf-be450ce8ceff | -5.697 | -39.9091 | 2024-10-30 00:07:00 | METOP-C | MOMBAÇA | CEARÁ | Brasil | 2308500 | 23 | 33 | nan | nan | nan | Caatinga | nan |
| 8bbfda7a-702b-3946-bf58-3f54d2e6d971 | -6.6804 | -44.685398 | 2024-10-30 00:07:02 | METOP-C | MIRADOR | MARANHÃO | Brasil | 2106706 | 21 | 33 | nan | nan | nan | Cerrado | nan |
| e8605451-216b-3e77-874d-c68a2c8bc694 | -5.4915 | -39.638 | 2024-10-30 00:07:03 | METOP-C | PEDRA BRANCA | CEARÁ | Brasil | 2310506 | 23 | 33 | nan | nan | nan | Caatinga | nan |
| 4abe02ee-0a6f-38a3-bc1d-7b87ede556d0 | -6.1024 | -43.5322 | 2024-10-30 00:07:07 | METOP-C | LAGOA DO MATO | MARANHÃO | Brasil | 2105922 | 21 | 33 | nan | nan | nan | Cerrado | nan |
| b598dbf9-8ced-3ae5-b99f-e313c7ba987a | -6.1049 | -43.5434 | 2024-10-30 00:07:07 | METOP-C | LAGOA DO MATO | MARANHÃO | Brasil | 2105922 | 21 | 33 | nan | nan | nan | Cerrado | nan |
| 9f0cdec3-d7a6-353d-964c-83116694ac8a | -5.629 | -41.7155 | 2024-10-30 00:07:08 | METOP-C | SÃO MIGUEL DO TAPUIO | PIAUÍ | Brasil | 2210409 | 22 | 33 | nan | nan | nan | Caatinga | nan |
| 44f3328b-2f66-3eb9-af84-bb78412174dc | -5.4544 | -41.026299 | 2024-10-30 00:07:08 | METOP-C | SÃO MIGUEL DO TAPUIO | PIAUÍ | Brasil | 2210409 | 22 | 33 | nan | nan | nan | Caatinga | nan |
| b577791e-04f2-3024-b215-3670aae6fbd6 | -5.4562 | -41.034302 | 2024-10-30 00:07:08 | METOP-C | SÃO MIGUEL DO TAPUIO | PIAUÍ | Brasil | 2210409 | 22 | 33 | nan | nan | nan | Caatinga | nan |
| c3d69bd7-995c-3e65-b2da-6e14728518a0 | -5.4445 | -41.0285 | 2024-10-30 00:07:09 | METOP-C | SÃO MIGUEL DO TAPUIO | PIAUÍ | Brasil | 2210409 | 22 | 33 | nan | nan | nan | Caatinga | nan |
| 365fabc0-22f4-3293-aa95-ac1a6eeb2b6b | -5.4463 | -41.036499 | 2024-10-30 00:07:09 | METOP-C | SÃO MIGUEL DO TAPUIO | PIAUÍ | Brasil | 2210409 | 22 | 33 | nan | nan | nan | Caatinga | nan |
| 5595aa0f-716f-3656-8699-ab56f59791db | -5.9462 | -43.66 | 2024-10-30 00:07:10 | METOP-C | LAGOA DO MATO | MARANHÃO | Brasil | 2105922 | 21 | 33 | nan | nan | nan | Cerrado | nan |
| d9583f7b-75bf-31be-9474-c52a86f4b5cb | -5.9487 | -43.671299 | 2024-10-30 00:07:10 | METOP-C | LAGOA DO MATO | MARANHÃO | Brasil | 2105922 | 21 | 33 | nan | nan | nan | Cerrado | nan |
| 4af005b6-8545-3b8e-82b8-16953788ea6b | -5.4184 | -41.416599 | 2024-10-30 00:07:10 | METOP-C | CASTELO DO PIAUÍ | PIAUÍ | Brasil | 2202604 | 22 | 33 | nan | nan | nan | Caatinga | nan |
| 07f567aa-df07-3ffe-9788-fe2677bdbf24 | -5.2924 | -41.221401 | 2024-10-30 00:07:12 | METOP-C | BURITI DOS MONTES | PIAUÍ | Brasil | 2202026 | 22 | 33 | nan | nan | nan | Caatinga | nan |


[Clique aqui para ver as próximas entradas](README3.md)
