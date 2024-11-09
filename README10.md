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

## Dados Diários - Página 10

| ID | Latitude | Longitude | Data/Hora GMT | Satélite | Município | Estado | País | Município ID | Estado ID | País ID | Dias sem Chuva | Precipitação | Risco de Fogo | Bioma | FRP |
|----|----------|-----------|---------------|----------|-----------|--------|------|--------------|-----------|---------|----------------|--------------|----------------|-------|-----|
| 3cf348bc-9b21-3167-b95f-9157de4d8ff5 | -3.60026 | -47.35154 | 2024-11-09 00:39:00 | TERRA_M-M | ULIANÓPOLIS | PARÁ | Brasil | 1508126 | 15 | 33 | nan | nan | nan | Amazônia | 2052.4 |
| 597586a3-5360-3d88-aa22-313414838be8 | -3.01876 | -51.05088 | 2024-11-09 00:39:00 | TERRA_M-M | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 17.1 |
| 69c37fc3-b961-3cdf-a0a0-d12d917c6f2a | -1.76405 | -45.61357 | 2024-11-09 00:39:00 | TERRA_M-M | TURIAÇU | MARANHÃO | Brasil | 2112407 | 21 | 33 | nan | nan | nan | Amazônia | 12.3 |
| 0ddb2e63-8d52-3902-bc98-87b50203367f | -3.60464 | -47.38285 | 2024-11-09 00:39:00 | TERRA_M-M | ULIANÓPOLIS | PARÁ | Brasil | 1508126 | 15 | 33 | nan | nan | nan | Amazônia | 13.6 |
| c76d8d84-7af8-3ace-aeca-52ab748220e8 | -3.11993 | -45.95634 | 2024-11-09 00:39:00 | TERRA_M-M | ZÉ DOCA | MARANHÃO | Brasil | 2114007 | 21 | 33 | nan | nan | nan | Amazônia | 11.8 |
| bc258726-c9dc-32d6-a83b-9bfdcf161167 | -1.56781 | -51.18459 | 2024-11-09 00:39:00 | TERRA_M-M | MELGAÇO | PARÁ | Brasil | 1504505 | 15 | 33 | nan | nan | nan | Amazônia | 12.0 |
| 191cc381-0d31-3b5a-878b-72f48df07d69 | -2.6034 | -48.19256 | 2024-11-09 00:39:00 | TERRA_M-M | TOMÉ-AÇU | PARÁ | Brasil | 1508001 | 15 | 33 | nan | nan | nan | Amazônia | 8.7 |
| 67394e6d-9396-34c5-9bcd-4aaa85bbcb8e | -2.17451 | -46.44466 | 2024-11-09 00:39:00 | TERRA_M-M | CACHOEIRA DO PIRIÁ | PARÁ | Brasil | 1501956 | 15 | 33 | nan | nan | nan | Amazônia | 6.0 |
| 7cc36418-2ff0-3e71-8ff5-7d4f93e2b8f5 | -3.15471 | -52.99597 | 2024-11-09 00:39:00 | TERRA_M-M | MEDICILÂNDIA | PARÁ | Brasil | 1504455 | 15 | 33 | nan | nan | nan | Amazônia | 122.4 |
| b6818426-db3b-3927-993f-2d5a623b6a8d | -1.6315 | -46.11574 | 2024-11-09 00:39:00 | TERRA_M-M | CARUTAPERA | MARANHÃO | Brasil | 2102903 | 21 | 33 | nan | nan | nan | Amazônia | 5.7 |
| f7fa4105-09d1-375c-af0a-e99e5b1e0ac0 | 0.03145 | -49.46082 | 2024-11-09 00:39:00 | TERRA_M-M | CHAVES | PARÁ | Brasil | 1502509 | 15 | 33 | nan | nan | nan | Amazônia | 7.4 |
| 1109f5ca-f1f7-3596-b517-e214d2355173 | -2.46086 | -50.39493 | 2024-11-09 00:39:00 | TERRA_M-M | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 9.2 |
| 006d2223-fc2b-3ecf-99b5-d300ac757873 | -4.20786 | -48.56146 | 2024-11-09 00:39:00 | TERRA_M-M | RONDON DO PARÁ | PARÁ | Brasil | 1506187 | 15 | 33 | nan | nan | nan | Amazônia | 17.3 |
| 2e093bf2-12c4-31d1-9100-515c16a6ba30 | -4.18332 | -46.58806 | 2024-11-09 00:39:00 | TERRA_M-M | BOM JARDIM | MARANHÃO | Brasil | 2102002 | 21 | 33 | nan | nan | nan | Amazônia | 5.9 |
| 13dc973f-be79-3f07-8ca4-558bd3c3df33 | -5.44276 | -43.25317 | 2024-11-09 00:39:00 | TERRA_M-M | MATÕES | MARANHÃO | Brasil | 2106607 | 21 | 33 | nan | nan | nan | Cerrado | 14.5 |
| b36c55f8-717d-3b60-a1f2-e142a1e8efea | -2.19032 | -53.62717 | 2024-11-09 00:39:00 | TERRA_M-M | PRAINHA | PARÁ | Brasil | 1506005 | 15 | 33 | nan | nan | nan | Amazônia | 36.2 |
| 8878d782-4823-3904-aeb8-da092a656a19 | -2.2718 | -46.4812 | 2024-11-09 00:39:00 | TERRA_M-M | CACHOEIRA DO PIRIÁ | PARÁ | Brasil | 1501956 | 15 | 33 | nan | nan | nan | Amazônia | 6.4 |
| 44fc9c19-ecbb-334d-bb0c-54992aa0a6b1 | -2.22919 | -46.44011 | 2024-11-09 00:39:00 | TERRA_M-M | CACHOEIRA DO PIRIÁ | PARÁ | Brasil | 1501956 | 15 | 33 | nan | nan | nan | Amazônia | 5.7 |
| aa9521f8-cb6b-3e92-a759-cd713ef800ce | -4.164 | -45.37369 | 2024-11-09 00:39:00 | TERRA_M-M | ALTAMIRA DO MARANHÃO | MARANHÃO | Brasil | 2100402 | 21 | 33 | nan | nan | nan | Amazônia | 4.7 |
| fabf1313-8342-3e82-8ddb-c596e898dfd6 | -5.81291 | -44.12189 | 2024-11-09 00:39:00 | TERRA_M-M | FORTUNA | MARANHÃO | Brasil | 2104206 | 21 | 33 | nan | nan | nan | Cerrado | 32.3 |
| cb7baca5-55ea-32ea-86a6-a7291791027a | -2.28922 | -48.72634 | 2024-11-09 00:39:00 | TERRA_M-M | ACARÁ | PARÁ | Brasil | 1500206 | 15 | 33 | nan | nan | nan | Amazônia | 8.0 |
| 8a2a96a3-25f0-3310-9d18-6aa938439e26 | -3.5462 | -43.5663 | 2024-11-09 00:40:00 | GOES-16 | CHAPADINHA | MARANHÃO | Brasil | 2103208 | 21 | 33 | nan | nan | nan | Cerrado | 100.7 |
| 1281aee8-2baa-3d05-97ba-0b89347ddb1a | -6.9747 | -40.0297 | 2024-11-09 00:40:00 | GOES-16 | ASSARÉ | CEARÁ | Brasil | 2301604 | 23 | 33 | nan | nan | nan | Caatinga | 71.1 |
| cfff122e-b4c3-38c7-9702-7e9d24a2225c | -3.1511 | -52.9731 | 2024-11-09 00:40:00 | GOES-16 | MEDICILÂNDIA | PARÁ | Brasil | 1504455 | 15 | 33 | nan | nan | nan | Amazônia | 285.6 |
| 7766b6ef-967b-38bf-86b4-9ecdea4f6cfd | -3.4466 | -52.7202 | 2024-11-09 00:40:00 | GOES-16 | MEDICILÂNDIA | PARÁ | Brasil | 1504455 | 15 | 33 | nan | nan | nan | Amazônia | 79.5 |
| 7b5b310c-3cad-39b6-afc6-0d78d68e6db0 | -5.4701 | -43.6371 | 2024-11-09 00:40:00 | GOES-16 | PARNARAMA | MARANHÃO | Brasil | 2107803 | 21 | 33 | nan | nan | nan | Cerrado | 149.7 |
| c25d110c-18de-3e19-aca9-1dc4d0074306 | -4.2219 | -45.8529 | 2024-11-09 00:40:00 | GOES-16 | SANTA LUZIA | MARANHÃO | Brasil | 2110005 | 21 | 33 | nan | nan | nan | Amazônia | 129.4 |
| 48a8e771-8bcd-3ba8-9c52-35ff19843ea8 | -5.4546 | -43.2659 | 2024-11-09 00:40:00 | GOES-16 | MATÕES | MARANHÃO | Brasil | 2106607 | 21 | 33 | nan | nan | nan | Cerrado | 85.3 |
| afaafbda-498c-3c57-bda9-76e4494ddb38 | -7.2536 | -38.9209 | 2024-11-09 00:40:00 | GOES-16 | MILAGRES | CEARÁ | Brasil | 2308302 | 23 | 33 | nan | nan | nan | Caatinga | 79.7 |
| 909aab46-ce81-34f2-aa1c-86118aac6919 | -4.2058 | -48.5491 | 2024-11-09 00:40:00 | GOES-16 | RONDON DO PARÁ | PARÁ | Brasil | 1506187 | 15 | 33 | nan | nan | nan | Amazônia | 175.7 |
| a4e9b0ec-fbb4-34c2-a570-847ac28103f9 | -5.4512 | -43.6616 | 2024-11-09 00:40:00 | GOES-16 | PARNARAMA | MARANHÃO | Brasil | 2107803 | 21 | 33 | nan | nan | nan | Cerrado | 66.5 |
| 46f9265e-5e39-3e28-bb3a-a7466903220c | -3.2808 | -52.7455 | 2024-11-09 00:40:00 | GOES-16 | MEDICILÂNDIA | PARÁ | Brasil | 1504455 | 15 | 33 | nan | nan | nan | Amazônia | 78.4 |
| 51ea80d3-69b2-367a-bc9f-f0d349ca6399 | -3.5649 | -43.5654 | 2024-11-09 00:40:00 | GOES-16 | CHAPADINHA | MARANHÃO | Brasil | 2103208 | 21 | 33 | nan | nan | nan | Cerrado | 83.6 |
| 2323f823-e0db-3556-90af-59b683fb9e81 | -7.2346 | -38.9231 | 2024-11-09 00:40:00 | GOES-16 | MILAGRES | CEARÁ | Brasil | 2308302 | 23 | 33 | nan | nan | nan | Caatinga | 99.1 |
| 32b17762-d00a-34e0-9a35-af53095af9cf | -3.1326 | -52.9939 | 2024-11-09 00:40:00 | GOES-16 | MEDICILÂNDIA | PARÁ | Brasil | 1504455 | 15 | 33 | nan | nan | nan | Amazônia | 92.8 |
| 8f3edbcf-7e03-3a85-8833-575cefd6e79e | -2.2295 | -53.7631 | 2024-11-09 00:40:00 | GOES-16 | PRAINHA | PARÁ | Brasil | 1506005 | 15 | 33 | nan | nan | nan | Amazônia | 57.0 |
| 7cf6cfc7-138f-333a-a106-2e0f0a638b2e | -5.4699 | -43.6603 | 2024-11-09 00:40:00 | GOES-16 | PARNARAMA | MARANHÃO | Brasil | 2107803 | 21 | 33 | nan | nan | nan | Cerrado | 257.0 |
| edf77f95-9550-3711-af70-856fe3dc64d5 | -1.5078 | -47.1813 | 2024-11-09 00:40:00 | GOES-16 | OURÉM | PARÁ | Brasil | 1505403 | 15 | 33 | nan | nan | nan | Amazônia | 151.5 |
| 301212ec-da47-383e-87af-fcb6a233112d | -4.2486 | -47.5729 | 2024-11-09 00:40:00 | GOES-16 | DOM ELISEU | PARÁ | Brasil | 1502939 | 15 | 33 | nan | nan | nan | Amazônia | 318.0 |
| 93ea15ad-ad3e-3659-b298-2498135e4e59 | -5.4889 | -43.6357 | 2024-11-09 00:40:00 | GOES-16 | PARNARAMA | MARANHÃO | Brasil | 2107803 | 21 | 33 | nan | nan | nan | Cerrado | 85.2 |
| e40b048d-e679-39f6-9297-9a8525c9d8ab | -2.2479 | -53.7627 | 2024-11-09 00:40:00 | GOES-16 | PRAINHA | PARÁ | Brasil | 1506005 | 15 | 33 | nan | nan | nan | Amazônia | 79.3 |
| caf3a936-8b76-3793-b1cd-8f4ecc099d8d | -5.6281 | -44.8433 | 2024-11-09 00:40:00 | GOES-16 | TUNTUM | MARANHÃO | Brasil | 2112308 | 21 | 33 | nan | nan | nan | Cerrado | 73.1 |
| 89a3ea0c-871c-32e6-b2f0-f458f5fc246a | -3.1327 | -52.9736 | 2024-11-09 00:40:00 | GOES-16 | MEDICILÂNDIA | PARÁ | Brasil | 1504455 | 15 | 33 | nan | nan | nan | Amazônia | 254.2 |
| 372af66c-e852-3667-b3c4-d5526aedab4f | -5.5804 | -41.791 | 2024-11-09 00:40:00 | GOES-16 | SÃO MIGUEL DO TAPUIO | PIAUÍ | Brasil | 2210409 | 22 | 33 | nan | nan | nan | Caatinga | 103.7 |
| f5a02df3-1513-32ad-89b4-9dd41de4c2d6 | -3.735 | -54.2292 | 2024-11-09 00:40:00 | GOES-16 | PLACAS | PARÁ | Brasil | 1505650 | 15 | 33 | nan | nan | nan | Amazônia | 66.2 |
| 65849a37-52f5-3024-aae1-004df4399384 | -4.2671 | -47.572 | 2024-11-09 00:40:00 | GOES-16 | DOM ELISEU | PARÁ | Brasil | 1502939 | 15 | 33 | nan | nan | nan | Amazônia | 68.1 |
| 30856381-d2ee-389f-93d4-565647ec7fa0 | -4.2484 | -47.5947 | 2024-11-09 00:40:00 | GOES-16 | DOM ELISEU | PARÁ | Brasil | 1502939 | 15 | 33 | nan | nan | nan | Amazônia | 88.5 |
| ab1ed9fe-8a9e-3e3b-a5fd-634ca1b041d2 | -3.1512 | -52.9527 | 2024-11-09 00:40:00 | GOES-16 | MEDICILÂNDIA | PARÁ | Brasil | 1504455 | 15 | 33 | nan | nan | nan | Amazônia | 78.4 |
| 59df2570-6234-3823-9ac2-9aba5a64ce00 | -3.151 | -52.9934 | 2024-11-09 00:40:00 | GOES-16 | MEDICILÂNDIA | PARÁ | Brasil | 1504455 | 15 | 33 | nan | nan | nan | Amazônia | 103.1 |
| 04828ef4-59d5-3537-94d5-e64be2393188 | -4.2059 | -48.5275 | 2024-11-09 00:40:00 | GOES-16 | RONDON DO PARÁ | PARÁ | Brasil | 1506187 | 15 | 33 | nan | nan | nan | Amazônia | 49.3 |
| 0726eba2-6fdc-3180-8a1a-b3ef61270d1e | -2.2479 | -53.7829 | 2024-11-09 00:40:00 | GOES-16 | PRAINHA | PARÁ | Brasil | 1506005 | 15 | 33 | nan | nan | nan | Amazônia | 91.7 |
| d1a8c356-862b-368e-a3d2-0b26a3184101 | -23.9095 | -54.0606 | 2024-11-09 00:40:00 | GOES-16 | ALTÔNIA | PARANÁ | Brasil | 4100509 | 41 | 33 | nan | nan | nan | Mata Atlântica | 61.7 |
| 0687e986-391c-3ab7-8a43-76c5514dd8e6 | -3.1328 | -52.9532 | 2024-11-09 00:40:00 | GOES-16 | MEDICILÂNDIA | PARÁ | Brasil | 1504455 | 15 | 33 | nan | nan | nan | Amazônia | 63.4 |
| 3adc467b-0876-365d-8d36-7879ea50e131 | -1.5078 | -47.1595 | 2024-11-09 00:40:00 | GOES-16 | OURÉM | PARÁ | Brasil | 1505403 | 15 | 33 | nan | nan | nan | Amazônia | 67.5 |
| cb757c16-4e24-3f90-a8b0-96c50b9a565f | -1.4893 | -47.1816 | 2024-11-09 00:40:00 | GOES-16 | OURÉM | PARÁ | Brasil | 1505403 | 15 | 33 | nan | nan | nan | Amazônia | 50.7 |
| 4b90c7c6-ae0a-3394-9e3f-3a0effcbe6a4 | -1.1467 | -53.6573 | 2024-11-09 00:40:00 | GOES-16 | PRAINHA | PARÁ | Brasil | 1506005 | 15 | 33 | nan | nan | nan | Amazônia | 48.8 |
| 710d9f91-7e1e-32e1-85f6-0cffbf359774 | -2.5448 | -47.1356 | 2024-11-09 00:40:00 | GOES-16 | GARRAFÃO DO NORTE | PARÁ | Brasil | 1503077 | 15 | 33 | nan | nan | nan | Amazônia | 49.0 |
| 2d0fe57a-97af-3fb0-a920-e804ac806855 | -1.5163 | -52.1901 | 2024-11-09 00:40:00 | GOES-16 | GURUPÁ | PARÁ | Brasil | 1503101 | 15 | 33 | nan | nan | nan | Amazônia | 47.9 |
| 23a6ee8a-856f-331c-964b-8c83ac26106f | -5.4887 | -43.6589 | 2024-11-09 00:40:00 | GOES-16 | PARNARAMA | MARANHÃO | Brasil | 2107803 | 21 | 33 | nan | nan | nan | Cerrado | 155.4 |
| 95100b8e-6449-38a6-a626-c1bcb12f34f8 | -3.967 | -48.15 | 2024-11-09 00:40:00 | GOES-16 | DOM ELISEU | PARÁ | Brasil | 1502939 | 15 | 33 | nan | nan | nan | Amazônia | 54.7 |
| 795fb9a2-cc07-3f3b-80fd-b4b2a23d04d0 | -6.9937 | -40.0277 | 2024-11-09 00:40:00 | GOES-16 | ASSARÉ | CEARÁ | Brasil | 2301604 | 23 | 33 | nan | nan | nan | Caatinga | 86.0 |
| cb17c9b3-6122-3e9b-a8b5-6c10cfe07d77 | -3.0864 | -50.5835 | 2024-11-09 00:40:00 | GOES-16 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 53.0 |
| 3b6b7145-8c47-34fd-a118-81c1a57b8956 | -4.2033 | -45.8538 | 2024-11-09 00:40:00 | GOES-16 | SANTA LUZIA | MARANHÃO | Brasil | 2110005 | 21 | 33 | nan | nan | nan | Amazônia | 221.4 |
| 3b799513-5eff-362a-af66-a96891555744 | -4.2243 | -48.5482 | 2024-11-09 00:40:00 | GOES-16 | RONDON DO PARÁ | PARÁ | Brasil | 1506187 | 15 | 33 | nan | nan | nan | Amazônia | 55.4 |
| baf8caaa-1139-3043-b924-ed475605be49 | -3.1641 | -54.4854 | 2024-11-09 00:40:00 | GOES-16 | MOJUÍ DOS CAMPOS | PARÁ | Brasil | 1504752 | 15 | 33 | nan | nan | nan | Amazônia | 64.5 |
| 4b1bfd29-3717-38c2-b3dd-4d94108c56a0 | -3.9853 | -48.1924 | 2024-11-09 00:40:00 | GOES-16 | DOM ELISEU | PARÁ | Brasil | 1502939 | 15 | 33 | nan | nan | nan | Amazônia | 56.3 |
| 2eec5df1-d44b-33f4-97f0-92036dcb0f52 | -4.346 | -46.8231 | 2024-11-09 00:40:00 | GOES-16 | BOM JARDIM | MARANHÃO | Brasil | 2102002 | 21 | 33 | nan | nan | nan | Amazônia | 57.0 |
| 920d6fea-5241-323c-809b-62359c982657 | -3.0947 | -53.3196 | 2024-11-09 00:40:00 | GOES-16 | MEDICILÂNDIA | PARÁ | Brasil | 1504455 | 15 | 33 | nan | nan | nan | Amazônia | 63.7 |
| 60ea3df2-7166-37a5-ac41-abb45552a225 | -3.465 | -52.7197 | 2024-11-09 00:40:00 | GOES-16 | MEDICILÂNDIA | PARÁ | Brasil | 1504455 | 15 | 33 | nan | nan | nan | Amazônia | 71.4 |
| cb32aa85-207b-3c52-b8e3-9e33df841b51 | -3.9669 | -48.1716 | 2024-11-09 00:40:00 | GOES-16 | DOM ELISEU | PARÁ | Brasil | 1502939 | 15 | 33 | nan | nan | nan | Amazônia | 235.5 |
| 2fce4f40-1dbc-360b-9f9d-edc5b7b4b365 | -2.6764 | -51.8189 | 2024-11-09 00:40:00 | GOES-16 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 64.6 |
| 4b0731ec-d421-3a4f-9970-5c95978a5eb6 | -4.23 | -47.5738 | 2024-11-09 00:40:00 | GOES-16 | DOM ELISEU | PARÁ | Brasil | 1502939 | 15 | 33 | nan | nan | nan | Amazônia | 49.6 |
| 5d1d988b-2962-3bf5-8420-d093d18e98e2 | -3.068 | -50.5631 | 2024-11-09 00:40:00 | GOES-16 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 56.3 |
| 390ebcc8-fd7a-3ee9-9329-1194bb812a43 | -2.2295 | -53.7832 | 2024-11-09 00:40:00 | GOES-16 | PRAINHA | PARÁ | Brasil | 1506005 | 15 | 33 | nan | nan | nan | Amazônia | 67.3 |
| c3dc0cc6-ad69-32ee-8e9e-0dd61e7b99d8 | -3.2624 | -52.746 | 2024-11-09 00:40:00 | GOES-16 | BRASIL NOVO | PARÁ | Brasil | 1501725 | 15 | 33 | nan | nan | nan | Amazônia | 75.9 |
| d427deba-9243-398d-87e6-479fd5fd84b5 | -4.2218 | -45.8753 | 2024-11-09 00:40:00 | GOES-16 | SANTA LUZIA | MARANHÃO | Brasil | 2110005 | 21 | 33 | nan | nan | nan | Amazônia | 83.5 |
| ffa896fb-d51c-3980-9c17-961f0e023903 | -3.9854 | -48.1708 | 2024-11-09 00:40:00 | GOES-16 | DOM ELISEU | PARÁ | Brasil | 1502939 | 15 | 33 | nan | nan | nan | Amazônia | 96.8 |
| 2b8dd7e3-dfc8-388a-bf2c-bc9a31197056 | -5.6283 | -44.8205 | 2024-11-09 00:40:00 | GOES-16 | TUNTUM | MARANHÃO | Brasil | 2112308 | 21 | 33 | nan | nan | nan | Cerrado | 73.4 |
| 4aaf6203-cc7e-34ce-a24b-68473f225139 | -2.4104 | -48.5265 | 2024-11-09 00:40:00 | GOES-16 | ACARÁ | PARÁ | Brasil | 1500206 | 15 | 33 | nan | nan | nan | Amazônia | 55.8 |
| 6e226c41-7d85-3550-9e0b-6a9416885ec7 | -3.0865 | -50.5625 | 2024-11-09 00:40:00 | GOES-16 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 112.2 |
| dc8ba2ed-f140-3a0c-a51f-31be5c0018d2 | -4.2032 | -45.8762 | 2024-11-09 00:40:00 | GOES-16 | SANTA LUZIA | MARANHÃO | Brasil | 2110005 | 21 | 33 | nan | nan | nan | Amazônia | 135.4 |
| c09b9edb-9912-36d7-b162-312d9e719114 | -1.5164 | -52.1696 | 2024-11-09 00:40:00 | GOES-16 | GURUPÁ | PARÁ | Brasil | 1503101 | 15 | 33 | nan | nan | nan | Amazônia | 73.1 |
| 2dfe1af0-c69f-3fd8-9be9-99e2a3ee60d6 | -4.2487 | -47.5511 | 2024-11-09 00:40:00 | GOES-16 | DOM ELISEU | PARÁ | Brasil | 1502939 | 15 | 33 | nan | nan | nan | Amazônia | 69.3 |
| 9cfd6fbc-071c-3eca-befc-c0ae490ed519 | -3.2353 | -50.2645 | 2024-11-09 00:40:00 | GOES-16 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 57.0 |
| e22721a6-8f6a-3983-95e1-4eddc8970bdc | -3.9483 | -48.1724 | 2024-11-09 00:40:00 | GOES-16 | DOM ELISEU | PARÁ | Brasil | 1502939 | 15 | 33 | nan | nan | nan | Amazônia | 57.8 |
| ec2c8ae9-20f4-3ab3-985a-e0042587e1f5 | -3.2715 | -46.3182 | 2024-11-09 00:40:00 | GOES-16 | ZÉ DOCA | MARANHÃO | Brasil | 2114007 | 21 | 33 | nan | nan | nan | Amazônia | 88.9 |
| 95cd7017-290a-3b4b-a829-7fa6eab476bd | -1.5529 | -52.2715 | 2024-11-09 00:40:00 | GOES-16 | PORTO DE MOZ | PARÁ | Brasil | 1505908 | 15 | 33 | nan | nan | nan | Amazônia | 49.3 |
| 985fcefc-185c-3e00-ad58-c9d72af98933 | -2.5448 | -47.1137 | 2024-11-09 00:40:00 | GOES-16 | GARRAFÃO DO NORTE | PARÁ | Brasil | 1503077 | 15 | 33 | nan | nan | nan | Amazônia | 55.6 |
| dcfd740f-def2-348c-94f0-9b8a4de95b8c | -3.9668 | -48.1932 | 2024-11-09 00:40:00 | GOES-16 | DOM ELISEU | PARÁ | Brasil | 1502939 | 15 | 33 | nan | nan | nan | Amazônia | 118.3 |
| 263a6abe-ef12-3426-946e-5d0ffd4ba469 | -4.2032 | -45.8762 | 2024-11-09 00:50:00 | GOES-16 | SANTA LUZIA | MARANHÃO | Brasil | 2110005 | 21 | 33 | nan | nan | nan | Amazônia | 169.6 |
| ded25cf4-142a-30dc-8110-94d7b3a65ad8 | -5.4887 | -43.6589 | 2024-11-09 00:50:00 | GOES-16 | PARNARAMA | MARANHÃO | Brasil | 2107803 | 21 | 33 | nan | nan | nan | Cerrado | 91.3 |
| d3056af4-274f-3d25-8ff2-205b12ce734c | -4.2033 | -45.8538 | 2024-11-09 00:50:00 | GOES-16 | SANTA LUZIA | MARANHÃO | Brasil | 2110005 | 21 | 33 | nan | nan | nan | Amazônia | 262.9 |
| 8f9a4e79-c980-3a1d-aac7-1fe9b4ec1689 | -1.5164 | -52.1696 | 2024-11-09 00:50:00 | GOES-16 | GURUPÁ | PARÁ | Brasil | 1503101 | 15 | 33 | nan | nan | nan | Amazônia | 86.3 |
| 3411cc6e-d4a1-3b7a-b71b-a3a25a686541 | -1.5078 | -47.1595 | 2024-11-09 00:50:00 | GOES-16 | OURÉM | PARÁ | Brasil | 1505403 | 15 | 33 | nan | nan | nan | Amazônia | 141.2 |
| 89b28248-d547-3cb8-aed7-252bf3996b70 | -3.2353 | -50.2645 | 2024-11-09 00:50:00 | GOES-16 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 65.6 |
| f4a653d0-d90b-3e43-be43-279e16d901ee | -3.4465 | -52.7406 | 2024-11-09 00:50:00 | GOES-16 | MEDICILÂNDIA | PARÁ | Brasil | 1504455 | 15 | 33 | nan | nan | nan | Amazônia | 62.7 |
| fc525d4a-9e4d-3df7-a8a8-71cc8f0fbffa | -4.2671 | -47.572 | 2024-11-09 00:50:00 | GOES-16 | DOM ELISEU | PARÁ | Brasil | 1502939 | 15 | 33 | nan | nan | nan | Amazônia | 104.5 |
| c50de6bd-bfd4-3c87-945b-73a1eba6960b | -2.2295 | -53.7832 | 2024-11-09 00:50:00 | GOES-16 | PRAINHA | PARÁ | Brasil | 1506005 | 15 | 33 | nan | nan | nan | Amazônia | 97.1 |
| c7364780-0054-3a57-829c-6d00186a750f | -3.9483 | -48.1724 | 2024-11-09 00:50:00 | GOES-16 | DOM ELISEU | PARÁ | Brasil | 1502939 | 15 | 33 | nan | nan | nan | Amazônia | 68.9 |
| 2727e9f8-df64-3551-a3eb-c0cf924658c7 | -3.0865 | -50.5625 | 2024-11-09 00:50:00 | GOES-16 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 100.5 |


[Clique aqui para ver as próximas entradas](README11.md)
