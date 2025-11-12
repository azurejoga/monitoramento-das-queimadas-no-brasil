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

## Dados Diários - Página 20

| ID | Latitude | Longitude | Data/Hora GMT | Satélite | Município | Estado | País | Município ID | Estado ID | País ID | Dias sem Chuva | Precipitação | Risco de Fogo | Bioma | FRP |
|----|----------|-----------|---------------|----------|-----------|--------|------|--------------|-----------|---------|----------------|--------------|----------------|-------|-----|
| 54758795-2cf5-3ad3-9098-30a8a1cdcdc9 | -4.0976 | -48.0144 | 2025-11-12 06:20:00 | GOES-19 | DOM ELISEU | PARÁ | Brasil | 1502939 | 15 | 33 | nan | nan | nan | Amazônia | 78.6 |
| e8700bc6-1bbf-32b9-9ed4-9ad61fc72708 | -4.1161 | -48.0136 | 2025-11-12 06:20:00 | GOES-19 | DOM ELISEU | PARÁ | Brasil | 1502939 | 15 | 33 | nan | nan | nan | Amazônia | 65.9 |
| f9da8971-1829-39ca-8571-8c17ebf7b275 | -4.1161 | -48.0136 | 2025-11-12 06:30:00 | GOES-19 | DOM ELISEU | PARÁ | Brasil | 1502939 | 15 | 33 | nan | nan | nan | Amazônia | 61.6 |
| 4c65bd51-f2fc-30c4-8af2-7c354108971c | -4.9643 | -43.7182 | 2025-11-12 06:30:00 | GOES-19 | SÃO JOÃO DO SOTER | MARANHÃO | Brasil | 2111078 | 21 | 33 | nan | nan | nan | Cerrado | 46.4 |
| 230f0579-3f38-35dc-862b-9608cedd04e9 | -4.0976 | -48.0144 | 2025-11-12 06:30:00 | GOES-19 | DOM ELISEU | PARÁ | Brasil | 1502939 | 15 | 33 | nan | nan | nan | Amazônia | 72.5 |
| 8003795a-7cbe-375a-a08f-3fca21cd1712 | -4.0976 | -48.0144 | 2025-11-12 06:40:00 | GOES-19 | DOM ELISEU | PARÁ | Brasil | 1502939 | 15 | 33 | nan | nan | nan | Amazônia | 60.4 |
| 405ce6bd-e40e-3451-b8f3-3b4fd2dd33e3 | -4.1161 | -48.0136 | 2025-11-12 06:40:00 | GOES-19 | DOM ELISEU | PARÁ | Brasil | 1502939 | 15 | 33 | nan | nan | nan | Amazônia | 57.6 |
| a15374e9-e384-35f9-b4e4-95430f851b1f | -4.1161 | -48.0136 | 2025-11-12 06:50:00 | GOES-19 | DOM ELISEU | PARÁ | Brasil | 1502939 | 15 | 33 | nan | nan | nan | Amazônia | 51.3 |
| 97b194c8-d8cb-3972-a08e-794566404349 | -4.0976 | -48.0144 | 2025-11-12 06:50:00 | GOES-19 | DOM ELISEU | PARÁ | Brasil | 1502939 | 15 | 33 | nan | nan | nan | Amazônia | 71.8 |
| 5099d212-be59-339a-97d3-61f4a0b3aaf4 | -3.6836 | -42.4138 | 2025-11-12 06:50:00 | GOES-19 | LUZILÂNDIA | PIAUÍ | Brasil | 2205805 | 22 | 33 | nan | nan | nan | Caatinga | 32.9 |
| eb0bdda5-5615-3ead-93fd-3b6487993dd3 | -4.1161 | -48.0136 | 2025-11-12 07:00:00 | GOES-19 | DOM ELISEU | PARÁ | Brasil | 1502939 | 15 | 33 | nan | nan | nan | Amazônia | 57.4 |
| b50dfaa8-273c-3251-aa62-c9a0643a4255 | -4.0976 | -48.0144 | 2025-11-12 07:00:00 | GOES-19 | DOM ELISEU | PARÁ | Brasil | 1502939 | 15 | 33 | nan | nan | nan | Amazônia | 56.9 |
| 89831770-8d2f-32ea-a469-402b0c663542 | -19.7636 | -57.9815 | 2025-11-12 07:20:00 | GOES-19 | CORUMBÁ | MATO GROSSO DO SUL | Brasil | 5003207 | 50 | 33 | nan | nan | nan | Pantanal | 72.3 |
| 1474461a-4067-3d6b-b707-68c6779497be | -19.7632 | -58.0023 | 2025-11-12 07:20:00 | GOES-19 | CORUMBÁ | MATO GROSSO DO SUL | Brasil | 5003207 | 50 | 33 | nan | nan | nan | Pantanal | 104.8 |
| d962972c-3e05-323e-90fa-f6526e9a3f19 | -5.48903 | -39.16462 | 2025-11-12 11:36:00 | TERRA_M-M | QUIXERAMOBIM | CEARÁ | Brasil | 2311405 | 23 | 33 | nan | nan | nan | Caatinga | 8.9 |
| 0c12963a-e44a-3078-b706-a5ad75135f5d | -5.42503 | -41.24966 | 2025-11-12 11:36:00 | TERRA_M-M | SÃO MIGUEL DO TAPUIO | PIAUÍ | Brasil | 2210409 | 22 | 33 | nan | nan | nan | Caatinga | 8.6 |
| 4a3b9d7f-4292-31f4-a0e4-7fa50da882af | -3.53738 | -39.06365 | 2025-11-12 11:36:00 | TERRA_M-M | PARACURU | CEARÁ | Brasil | 2310209 | 23 | 33 | nan | nan | nan | Caatinga | 23.2 |
| 58adb1fb-105e-32fe-9057-2b65a6c453d6 | -5.04586 | -41.11051 | 2025-11-12 11:36:00 | TERRA_M-M | CRATEÚS | CEARÁ | Brasil | 2304103 | 23 | 33 | nan | nan | nan | Caatinga | 12.9 |
| 0e80e44b-6ac7-33b8-af20-15934c4c0c33 | -5.03746 | -38.13496 | 2025-11-12 11:36:00 | TERRA_M-M | LIMOEIRO DO NORTE | CEARÁ | Brasil | 2307601 | 23 | 33 | nan | nan | nan | Caatinga | 6.3 |
| 0b5c0c66-4710-3f94-82bb-f9da80178999 | -5.49802 | -39.16588 | 2025-11-12 11:36:00 | TERRA_M-M | QUIXERAMOBIM | CEARÁ | Brasil | 2311405 | 23 | 33 | nan | nan | nan | Caatinga | 33.4 |
| 09862886-5c40-3ae0-8e75-67732ea3fb7c | -5.84769 | -38.34064 | 2025-11-12 11:36:00 | TERRA_M-M | IRACEMA | CEARÁ | Brasil | 2306009 | 23 | 33 | nan | nan | nan | Caatinga | 7.7 |
| 97c0fdab-8075-3f3f-8d30-fe62462844f9 | -5.87276 | -36.87842 | 2025-11-12 11:36:00 | TERRA_M-M | SÃO RAFAEL | RIO GRANDE DO NORTE | Brasil | 2412807 | 24 | 33 | nan | nan | nan | Caatinga | 11.6 |
| 444124ca-5169-3eaf-8417-84a27f590494 | -5.87405 | -36.86935 | 2025-11-12 11:36:00 | TERRA_M-M | SÃO RAFAEL | RIO GRANDE DO NORTE | Brasil | 2412807 | 24 | 33 | nan | nan | nan | Caatinga | 35.5 |
| 4487525f-00fc-3804-9d10-2c5b0ee19ce6 | -5.43496 | -39.21652 | 2025-11-12 11:36:00 | TERRA_M-M | QUIXERAMOBIM | CEARÁ | Brasil | 2311405 | 23 | 33 | nan | nan | nan | Caatinga | 31.6 |
| 5af38273-09e7-36fe-b9cc-9c2e026c1f27 | -5.82125 | -38.33693 | 2025-11-12 11:36:00 | TERRA_M-M | IRACEMA | CEARÁ | Brasil | 2306009 | 23 | 33 | nan | nan | nan | Caatinga | 7.9 |
| 0bf37dd1-b0f8-322b-aa11-ce7d3a06bb9e | -5.03585 | -41.10893 | 2025-11-12 11:36:00 | TERRA_M-M | CRATEÚS | CEARÁ | Brasil | 2304103 | 23 | 33 | nan | nan | nan | Caatinga | 27.4 |
| 6eadc6f2-d1aa-3c3d-ac08-9a446b1b5c16 | -7.95031 | -44.11467 | 2025-11-12 11:38:00 | TERRA_M-M | SEBASTIÃO LEAL | PIAUÍ | Brasil | 2210631 | 22 | 33 | nan | nan | nan | Cerrado | 27.1 |
| 8ede1510-828e-3dcf-9ad5-a74ba1003abf | -7.22982 | -37.7143 | 2025-11-12 11:38:00 | TERRA_M-M | OLHO D'ÁGUA | PARAÍBA | Brasil | 2510402 | 25 | 33 | nan | nan | nan | Caatinga | 10.2 |
| 9cfb391f-2ce3-320a-94ac-93d500083935 | -10.38447 | -36.85709 | 2025-11-12 11:38:00 | TERRA_M-M | JAPOATÃ | SERGIPE | Brasil | 2803401 | 28 | 33 | nan | nan | nan | Mata Atlântica | 13.1 |
| c78d50ea-19a4-33ea-903d-f58686f3353d | -6.91938 | -38.27898 | 2025-11-12 11:38:00 | TERRA_M-M | NAZAREZINHO | PARAÍBA | Brasil | 2510006 | 25 | 33 | nan | nan | nan | Caatinga | 10.5 |
| 3c312ffb-ac0b-3002-8915-2588269f8400 | -6.52809 | -37.78939 | 2025-11-12 11:38:00 | TERRA_M-M | JERICÓ | PARAÍBA | Brasil | 2507408 | 25 | 33 | nan | nan | nan | Caatinga | 19.5 |
| 2fc72ecd-25a3-3437-b87e-eef7a1c352ac | -6.33598 | -38.54568 | 2025-11-12 11:38:00 | TERRA_M-M | VENHA-VER | RIO GRANDE DO NORTE | Brasil | 2414753 | 24 | 33 | nan | nan | nan | Caatinga | 11.9 |
| fda39332-136e-30ee-9604-5a1cf8b22079 | -7.54392 | -39.004 | 2025-11-12 11:38:00 | TERRA_M-M | BREJO SANTO | CEARÁ | Brasil | 2302503 | 23 | 33 | nan | nan | nan | Caatinga | 7.6 |
| 343a5ecd-f431-3ad3-95fd-05096ea5a66b | -7.20968 | -40.40326 | 2025-11-12 11:38:00 | TERRA_M-M | SALITRE | CEARÁ | Brasil | 2311959 | 23 | 33 | nan | nan | nan | Caatinga | 8.1 |
| 78ac0f85-7e31-3c2d-b0b5-ba0d334e2b3e | -6.44737 | -37.51934 | 2025-11-12 11:38:00 | TERRA_M-M | SÃO BENTO | PARAÍBA | Brasil | 2513901 | 25 | 33 | nan | nan | nan | Caatinga | 14.3 |
| cff20472-2a1c-35b5-8276-6f398ae94db6 | -7.06143 | -38.69834 | 2025-11-12 11:38:00 | TERRA_M-M | BARRO | CEARÁ | Brasil | 2302008 | 23 | 33 | nan | nan | nan | Caatinga | 9.4 |
| 0362dfbf-de7b-3b71-87ad-2a5e271eade9 | -6.99248 | -38.02002 | 2025-11-12 11:38:00 | TERRA_M-M | COREMAS | PARAÍBA | Brasil | 2504801 | 25 | 33 | nan | nan | nan | Caatinga | 13.1 |
| 262a3873-292b-3862-b656-de1665931c54 | -8.65833 | -36.8129 | 2025-11-12 11:38:00 | TERRA_M-M | VENTUROSA | PERNAMBUCO | Brasil | 2616001 | 26 | 33 | nan | nan | nan | Caatinga | 12.9 |
| 3781d633-f0d7-3b59-8a3c-65e2b113bb0f | -8.86385 | -37.12061 | 2025-11-12 11:38:00 | TERRA_M-M | TUPANATINGA | PERNAMBUCO | Brasil | 2615805 | 26 | 33 | nan | nan | nan | Caatinga | 27.5 |
| 42517a8e-0aff-36b6-a84b-2b234dc9007c | -8.3206 | -36.52536 | 2025-11-12 11:38:00 | TERRA_M-M | SANHARÓ | PERNAMBUCO | Brasil | 2612406 | 26 | 33 | nan | nan | nan | Caatinga | 11.2 |
| 7b8c5b1d-b885-38bf-bc33-cbc2d5fe620e | -6.63167 | -38.22893 | 2025-11-12 11:38:00 | TERRA_M-M | SOUSA | PARAÍBA | Brasil | 2516201 | 25 | 33 | nan | nan | nan | Caatinga | 9.8 |
| 0bd3ecc9-8695-3afd-8dfa-cd2b0f0f2e31 | -7.69316 | -37.25217 | 2025-11-12 11:38:00 | TERRA_M-M | TUPARETAMA | PERNAMBUCO | Brasil | 2615904 | 26 | 33 | nan | nan | nan | Caatinga | 6.8 |
| 3e3a99f4-f90f-3851-9ff3-1d5602a2c1f1 | -8.8729 | -37.12185 | 2025-11-12 11:38:00 | TERRA_M-M | TUPANATINGA | PERNAMBUCO | Brasil | 2615805 | 26 | 33 | nan | nan | nan | Caatinga | 13.2 |
| 35c463ba-0ea7-33cf-b1f4-9ed638f0054c | -6.52683 | -37.7982 | 2025-11-12 11:38:00 | TERRA_M-M | JERICÓ | PARAÍBA | Brasil | 2507408 | 25 | 33 | nan | nan | nan | Caatinga | 5.9 |
| fc028aae-680e-3e3d-874b-0c35f0816d9a | -6.66943 | -38.91749 | 2025-11-12 11:38:00 | TERRA_M-M | LAVRAS DA MANGABEIRA | CEARÁ | Brasil | 2307502 | 23 | 33 | nan | nan | nan | Caatinga | 5.5 |
| bdfe2509-3b34-3822-8410-d2dc657aed7e | -7.00127 | -38.02126 | 2025-11-12 11:38:00 | TERRA_M-M | COREMAS | PARAÍBA | Brasil | 2504801 | 25 | 33 | nan | nan | nan | Caatinga | 21.7 |
| 20146a40-b59d-3c84-8ef6-b95b20743e88 | -6.92065 | -38.27019 | 2025-11-12 11:38:00 | TERRA_M-M | NAZAREZINHO | PARAÍBA | Brasil | 2510006 | 25 | 33 | nan | nan | nan | Caatinga | 10.0 |
| d58f5e29-39a9-366d-b9e8-7aa638ecc229 | -8.55472 | -44.33656 | 2025-11-12 11:38:00 | TERRA_M-M | PALMEIRA DO PIAUÍ | PIAUÍ | Brasil | 2207405 | 22 | 33 | nan | nan | nan | Cerrado | 24.7 |
| 5915ad76-c755-3fda-88df-00a3bd7a61d7 | -6.5017 | -37.26338 | 2025-11-12 11:38:00 | TERRA_M-M | TIMBAÚBA DOS BATISTAS | RIO GRANDE DO NORTE | Brasil | 2414308 | 24 | 33 | nan | nan | nan | Caatinga | 7.8 |
| 5d66a574-7fce-3e89-ac3c-4cbd2f8ac229 | -6.59103 | -37.72624 | 2025-11-12 11:38:00 | TERRA_M-M | PAULISTA | PARAÍBA | Brasil | 2510907 | 25 | 33 | nan | nan | nan | Caatinga | 7.6 |
| d7cdb469-b07b-3a35-9811-63249b9f554a | -7.1269 | -41.85971 | 2025-11-12 11:38:00 | TERRA_M-M | SANTA CRUZ DO PIAUÍ | PIAUÍ | Brasil | 2209104 | 22 | 33 | nan | nan | nan | Caatinga | 16.9 |
| 80b65d18-c988-34c8-9bc4-4f8a8d5ef93b | -6.47032 | -36.23793 | 2025-11-12 11:38:00 | TERRA_M-M | PICUÍ | PARAÍBA | Brasil | 2511400 | 25 | 33 | nan | nan | nan | Caatinga | 12.6 |
| 4b31b435-bac8-3de4-9f82-ce4b8eb20204 | -7.87722 | -37.9091 | 2025-11-12 11:38:00 | TERRA_M-M | FLORES | PERNAMBUCO | Brasil | 2605608 | 26 | 33 | nan | nan | nan | Caatinga | 18.4 |
| 9c92d8b0-cd73-3553-8141-ae162346df3a | -7.61838 | -37.97187 | 2025-11-12 11:38:00 | TERRA_M-M | PRINCESA ISABEL | PARAÍBA | Brasil | 2512309 | 25 | 33 | nan | nan | nan | Caatinga | 6.0 |
| e4ddff83-28e4-389a-b378-29b12b25cb1b | -9.02314 | -37.42954 | 2025-11-12 11:38:00 | TERRA_M-M | CANAPI | ALAGOAS | Brasil | 2701605 | 27 | 33 | nan | nan | nan | Caatinga | 18.9 |
| c7d6b070-d0d7-36aa-9b3a-75037054f572 | -7.43041 | -39.90219 | 2025-11-12 11:38:00 | TERRA_M-M | EXU | PERNAMBUCO | Brasil | 2605301 | 26 | 33 | nan | nan | nan | Caatinga | 11.0 |
| 8ad48a0e-5b4b-3038-b853-e0008dcfc65c | -8.41067 | -42.3765 | 2025-11-12 11:38:00 | TERRA_M-M | JOÃO COSTA | PIAUÍ | Brasil | 2205359 | 22 | 33 | nan | nan | nan | Caatinga | 17.1 |
| 89fc5265-3285-3b4e-a3f3-e09335c13b39 | -7.99442 | -37.98621 | 2025-11-12 11:38:00 | TERRA_M-M | FLORES | PERNAMBUCO | Brasil | 2605608 | 26 | 33 | nan | nan | nan | Caatinga | 5.2 |
| 5f69186f-692a-3751-9121-9b038987622f | -7.7397 | -37.57753 | 2025-11-12 11:38:00 | TERRA_M-M | AFOGADOS DA INGAZEIRA | PERNAMBUCO | Brasil | 2600104 | 26 | 33 | nan | nan | nan | Caatinga | 18.5 |
| bb4f514c-24d6-3131-bcb6-62f190710f6f | -7.00001 | -38.03006 | 2025-11-12 11:38:00 | TERRA_M-M | COREMAS | PARAÍBA | Brasil | 2504801 | 25 | 33 | nan | nan | nan | Caatinga | 11.6 |
| c2d561d4-79cc-3532-8d2a-095ae0983bd2 | -8.94898 | -40.86745 | 2025-11-12 11:38:00 | TERRA_M-M | CASA NOVA | BAHIA | Brasil | 2907202 | 29 | 33 | nan | nan | nan | Caatinga | 16.2 |
| a88c8c33-9efa-323f-a605-0dcaaff03940 | -7.76251 | -37.41564 | 2025-11-12 11:38:00 | TERRA_M-M | INGAZEIRA | PERNAMBUCO | Brasil | 2607109 | 26 | 33 | nan | nan | nan | Caatinga | 8.9 |
| ad7d3d37-5ff7-3c93-a280-6ac47dc3c4c9 | -7.73844 | -37.58649 | 2025-11-12 11:38:00 | TERRA_M-M | AFOGADOS DA INGAZEIRA | PERNAMBUCO | Brasil | 2600104 | 26 | 33 | nan | nan | nan | Caatinga | 5.8 |
| 12af8fd1-470a-3a09-85ca-70d77ed8896e | -7.56679 | -37.49551 | 2025-11-12 11:38:00 | TERRA_M-M | TABIRA | PERNAMBUCO | Brasil | 2614600 | 26 | 33 | nan | nan | nan | Caatinga | 30.1 |
| 1b7a0b63-cde4-3dac-a486-6ba3b71efdd6 | -6.96466 | -37.69509 | 2025-11-12 11:38:00 | TERRA_M-M | CAJAZEIRINHAS | PARAÍBA | Brasil | 2503753 | 25 | 33 | nan | nan | nan | Caatinga | 6.8 |
| 9a5fdbe2-98ab-3df7-87de-8a1adb42f474 | -8.9505 | -40.85733 | 2025-11-12 11:38:00 | TERRA_M-M | CASA NOVA | BAHIA | Brasil | 2907202 | 29 | 33 | nan | nan | nan | Caatinga | 19.5 |
| e4450000-9ad1-3c6b-ad27-1cfa13498ea2 | -6.70796 | -35.53746 | 2025-11-12 11:38:00 | TERRA_M-M | BELÉM | PARAÍBA | Brasil | 2501906 | 25 | 33 | nan | nan | nan | Caatinga | 8.0 |
| 80a32c3c-e5ab-3b12-80f4-105ef94c6778 | -6.54567 | -37.85473 | 2025-11-12 11:38:00 | TERRA_M-M | JERICÓ | PARAÍBA | Brasil | 2507408 | 25 | 33 | nan | nan | nan | Caatinga | 9.3 |
| 880cf0c0-716e-35d6-804a-3f75d1969fb5 | -6.99121 | -38.02882 | 2025-11-12 11:38:00 | TERRA_M-M | COREMAS | PARAÍBA | Brasil | 2504801 | 25 | 33 | nan | nan | nan | Caatinga | 6.6 |
| a9a7305c-727a-3bc5-9f51-e7cd3e5b8ebb | -6.66813 | -38.92644 | 2025-11-12 11:38:00 | TERRA_M-M | LAVRAS DA MANGABEIRA | CEARÁ | Brasil | 2307502 | 23 | 33 | nan | nan | nan | Caatinga | 12.3 |
| aa68ced9-f6fa-37c4-8963-921f32c5ebbe | -6.20664 | -40.18966 | 2025-11-12 11:38:00 | TERRA_M-M | ARNEIROZ | CEARÁ | Brasil | 2301505 | 23 | 33 | nan | nan | nan | Caatinga | 9.0 |
| 69136600-4cac-3a05-9dcf-30596d66ad35 | -8.01059 | -39.09296 | 2025-11-12 11:38:00 | TERRA_M-M | SALGUEIRO | PERNAMBUCO | Brasil | 2612208 | 26 | 33 | nan | nan | nan | Caatinga | 7.9 |
| c53f3cae-a25c-3fea-8a95-88fb2fe65f78 | -8.71869 | -36.97298 | 2025-11-12 11:38:00 | TERRA_M-M | BUÍQUE | PERNAMBUCO | Brasil | 2602803 | 26 | 33 | nan | nan | nan | Caatinga | 6.6 |
| 147057dd-7548-35ce-9eb6-09dbfa1e6c7f | -5.72079 | -39.47209 | 2025-11-12 11:38:00 | TERRA_M-M | PIQUET CARNEIRO | CEARÁ | Brasil | 2310902 | 23 | 33 | nan | nan | nan | Caatinga | 34.2 |
| 28e56521-67ed-321f-98b2-41c0d9b7fcab | -7.72833 | -37.72171 | 2025-11-12 11:38:00 | TERRA_M-M | CARNAÍBA | PERNAMBUCO | Brasil | 2603900 | 26 | 33 | nan | nan | nan | Caatinga | 29.4 |
| 83d581b2-50fb-36ac-8bee-347dbad9f216 | -6.77309 | -37.88692 | 2025-11-12 11:38:00 | TERRA_M-M | POMBAL | PARAÍBA | Brasil | 2512101 | 25 | 33 | nan | nan | nan | Caatinga | 9.6 |
| 7519031a-01d8-3ec1-b679-5350be1e618d | -7.02447 | -38.82897 | 2025-11-12 11:38:00 | TERRA_M-M | BARRO | CEARÁ | Brasil | 2302008 | 23 | 33 | nan | nan | nan | Caatinga | 8.9 |
| 20c63df1-a0e6-36c5-a1b0-01ac910b9194 | -7.72706 | -37.73064 | 2025-11-12 11:38:00 | TERRA_M-M | CARNAÍBA | PERNAMBUCO | Brasil | 2603900 | 26 | 33 | nan | nan | nan | Caatinga | 11.2 |
| a549adb6-f587-35cc-a512-be1fe23854a6 | -6.34885 | -39.09209 | 2025-11-12 11:38:00 | TERRA_M-M | ORÓS | CEARÁ | Brasil | 2309508 | 23 | 33 | nan | nan | nan | Caatinga | 12.3 |
| 7a7f2474-2427-3d0f-afd6-bd43f8288ec5 | -6.28476 | -38.7743 | 2025-11-12 11:38:00 | TERRA_M-M | ICÓ | CEARÁ | Brasil | 2305407 | 23 | 33 | nan | nan | nan | Caatinga | 10.4 |
| 1c24145b-5ca8-3e43-ac6d-619ba6a420d4 | -13.05284 | -43.52798 | 2025-11-12 11:40:00 | TERRA_M-M | SÍTIO DO MATO | BAHIA | Brasil | 2930758 | 29 | 33 | nan | nan | nan | Cerrado | 12.4 |
| 278a6c81-b5a4-381b-a51a-ab1b9cd9b134 | -12.21677 | -42.77971 | 2025-11-12 11:40:00 | TERRA_M-M | OLIVEIRA DOS BREJINHOS | BAHIA | Brasil | 2923209 | 29 | 33 | nan | nan | nan | Caatinga | 21.6 |
| bcf74423-5cc7-3401-8f5f-867892324806 | -13.92031 | -44.22168 | 2025-11-12 11:40:00 | TERRA_M-M | CORIBE | BAHIA | Brasil | 2909109 | 29 | 33 | nan | nan | nan | Cerrado | 17.3 |
| 80c80491-9efa-3612-a5f4-0719401171b6 | -13.69837 | -43.21819 | 2025-11-12 11:40:00 | TERRA_M-M | RIACHO DE SANTANA | BAHIA | Brasil | 2926400 | 29 | 33 | nan | nan | nan | Caatinga | 8.9 |
| 5c4f2347-616d-36ae-b818-f673ae19c7e9 | -12.21657 | -42.7854 | 2025-11-12 11:40:00 | TERRA_M-M | OLIVEIRA DOS BREJINHOS | BAHIA | Brasil | 2923209 | 29 | 33 | nan | nan | nan | Caatinga | 12.1 |
| 16e1a562-730f-3760-bab7-df0acb7aca71 | -13.05493 | -43.51495 | 2025-11-12 11:40:00 | TERRA_M-M | SÍTIO DO MATO | BAHIA | Brasil | 2930758 | 29 | 33 | nan | nan | nan | Cerrado | 10.7 |
| ffcc3d84-b5c4-3c91-8ac1-b943053af1dd | -13.3965 | -42.71829 | 2025-11-12 11:40:00 | TERRA_M-M | MACAÚBAS | BAHIA | Brasil | 2919801 | 29 | 33 | nan | nan | nan | Caatinga | 12.8 |
| c0b1cd8d-110c-3786-bbe1-f63661076964 | -13.04236 | -43.52626 | 2025-11-12 11:40:00 | TERRA_M-M | SÍTIO DO MATO | BAHIA | Brasil | 2930758 | 29 | 33 | nan | nan | nan | Cerrado | 9.4 |
| ed7a51b6-444e-3165-8516-b76ef8b36c80 | -12.21839 | -42.77343 | 2025-11-12 11:40:00 | TERRA_M-M | OLIVEIRA DOS BREJINHOS | BAHIA | Brasil | 2923209 | 29 | 33 | nan | nan | nan | Caatinga | 11.6 |
| be3d9b6b-4a27-36e4-879a-57e98f26d102 | -22.65142 | -42.24001 | 2025-11-12 11:42:00 | TERRA_M-M | ARARUAMA | RIO DE JANEIRO | Brasil | 3300209 | 33 | 33 | nan | nan | nan | Mata Atlântica | 4.5 |
| e4b21778-4c55-340f-b30a-8d2cc8b91b1f | -19.32505 | -40.02494 | 2025-11-12 11:42:00 | TERRA_M-M | LINHARES | ESPÍRITO SANTO | Brasil | 3203205 | 32 | 33 | nan | nan | nan | Mata Atlântica | 5.5 |
| 6ab275b0-489c-3a69-ac56-548755c23740 | -17.62085 | -44.62631 | 2025-11-12 11:42:00 | TERRA_M-M | VÁRZEA DA PALMA | MINAS GERAIS | Brasil | 3170800 | 31 | 33 | nan | nan | nan | Cerrado | 40.9 |
| b14bd5b7-5f74-3ca7-a0d5-e68a584f1906 | -22.86658 | -43.31883 | 2025-11-12 11:42:00 | TERRA_M-M | RIO DE JANEIRO | RIO DE JANEIRO | Brasil | 3304557 | 33 | 33 | nan | nan | nan | Mata Atlântica | 7.1 |
| 7373f58f-b52e-3f52-8e99-8e6b322c8eda | -3.2108 | -43.535 | 2025-11-12 11:50:00 | GOES-19 | BELÁGUA | MARANHÃO | Brasil | 2101731 | 21 | 33 | nan | nan | nan | Cerrado | 102.5 |
| 8d8e6fba-dabd-3ba7-9d01-fdf10695cafa | -3.5388 | -41.6127 | 2025-11-12 12:20:00 | GOES-19 | COCAL | PIAUÍ | Brasil | 2202703 | 22 | 33 | nan | nan | nan | Caatinga | 88.8 |
| 8a78b723-a88b-3fbb-ab49-36c1af53b27b | -3.8716 | -42.2383 | 2025-11-12 12:20:00 | GOES-19 | ESPERANTINA | PIAUÍ | Brasil | 2203701 | 22 | 33 | nan | nan | nan | Caatinga | 84.6 |
| 5d7109f9-ecf0-3597-bab5-96b3b146a85e | -3.8718 | -42.2146 | 2025-11-12 12:20:00 | GOES-19 | ESPERANTINA | PIAUÍ | Brasil | 2203701 | 22 | 33 | nan | nan | nan | Caatinga | 75.8 |
| 36dbd6c0-e3b2-36ba-9323-2e104155d03d | -3.8716 | -42.2383 | 2025-11-12 12:30:00 | GOES-19 | ESPERANTINA | PIAUÍ | Brasil | 2203701 | 22 | 33 | nan | nan | nan | Caatinga | 81.1 |
| 5e1eb702-505b-32ce-9ef6-def834b212f1 | -16.1127 | -45.8492 | 2025-11-12 12:50:00 | GOES-19 | URUCUIA | MINAS GERAIS | Brasil | 3170529 | 31 | 33 | nan | nan | nan | Cerrado | 165.9 |
| e1a27f7e-b9d5-3fbc-b33e-2e35a8819522 | -5.4922 | -39.1751 | 2025-11-12 12:50:00 | GOES-19 | QUIXERAMOBIM | CEARÁ | Brasil | 2311405 | 23 | 33 | nan | nan | nan | Caatinga | 98.6 |


[Clique aqui para ver as próximas entradas](README21.md)
