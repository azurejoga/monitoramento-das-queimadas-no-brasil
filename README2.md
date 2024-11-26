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
| 968dc1bb-6bb1-399f-99a5-1602ebb50327 | -2.8198 | -53.0222 | 2024-11-26 00:20:00 | GOES-16 | MEDICILÂNDIA | PARÁ | Brasil | 1504455 | 15 | 33 | nan | nan | nan | Amazônia | 77.6 |
| 4ca09989-647b-39a8-b872-b3192f63084b | -3.3939 | -44.1492 | 2024-11-26 00:20:00 | GOES-16 | ITAPECURU MIRIM | MARANHÃO | Brasil | 2105401 | 21 | 33 | nan | nan | nan | Cerrado | 54.0 |
| c2b19bd2-d429-35cf-88c0-80e28a869d99 | 2.6718 | -60.4304 | 2024-11-26 00:20:00 | GOES-16 | CANTÁ | RORAIMA | Brasil | 1400175 | 14 | 33 | nan | nan | nan | Amazônia | 68.1 |
| d91491cf-5429-34a9-96a0-2c2b06c7bd86 | -1.4951 | -53.8146 | 2024-11-26 00:20:00 | GOES-16 | PRAINHA | PARÁ | Brasil | 1506005 | 15 | 33 | nan | nan | nan | Amazônia | 66.7 |
| a9e1c67a-cba9-3ef8-86cd-efde133d612b | -21.31941 | -47.40544 | 2024-11-26 00:24:00 | TERRA_M-M | SANTA CRUZ DA ESPERANÇA | SÃO PAULO | Brasil | 3546256 | 35 | 33 | nan | nan | nan | Cerrado | 21.2 |
| 3d28148a-165c-30b5-b29a-684c93ac6024 | -20.45195 | -44.1787 | 2024-11-26 00:24:00 | TERRA_M-M | PIEDADE DOS GERAIS | MINAS GERAIS | Brasil | 3150406 | 31 | 33 | nan | nan | nan | Mata Atlântica | 18.0 |
| 6a1b7ed5-090d-3d96-9321-27126e43436b | -20.32275 | -48.82756 | 2024-11-26 00:24:00 | TERRA_M-M | COLÔMBIA | SÃO PAULO | Brasil | 3512100 | 35 | 33 | nan | nan | nan | Cerrado | 38.9 |
| 1f37fec3-73b0-31cf-9498-1588b8a8236e | -20.33162 | -48.82182 | 2024-11-26 00:24:00 | TERRA_M-M | COLÔMBIA | SÃO PAULO | Brasil | 3512100 | 35 | 33 | nan | nan | nan | Cerrado | 28.4 |
| 42f853c0-0d9b-39cb-b5a3-bcb393d2efec | -22.09911 | -49.61769 | 2024-11-26 00:24:00 | TERRA_M-M | PIRAJUÍ | SÃO PAULO | Brasil | 3538907 | 35 | 33 | nan | nan | nan | Mata Atlântica | 67.9 |
| cf74b2da-b98b-3258-b2bf-3cda71649c23 | -22.09697 | -49.62506 | 2024-11-26 00:24:00 | TERRA_M-M | GARÇA | SÃO PAULO | Brasil | 3516705 | 35 | 33 | nan | nan | nan | Mata Atlântica | 64.0 |
| e4f1d607-76ca-3f38-aea2-f6c304031ae5 | -21.44156 | -42.53771 | 2024-11-26 00:24:00 | TERRA_M-M | LEOPOLDINA | MINAS GERAIS | Brasil | 3138401 | 31 | 33 | nan | nan | nan | Mata Atlântica | 5.9 |
| 9a0f7567-ce7b-39d4-800f-127410b1cd9a | -6.85491 | -35.28016 | 2024-11-26 00:28:00 | TERRA_M-M | CUITÉ DE MAMANGUAPE | PARAÍBA | Brasil | 2505238 | 25 | 33 | nan | nan | nan | Caatinga | 16.3 |
| b63eb1b4-1f62-3e69-bc00-28935cc865b3 | -5.66618 | -45.8592 | 2024-11-26 00:28:00 | TERRA_M-M | GRAJAÚ | MARANHÃO | Brasil | 2104800 | 21 | 33 | nan | nan | nan | Cerrado | 5.7 |
| 9295cf9c-c868-3d93-90a3-7a2db33fad16 | -6.06532 | -39.18112 | 2024-11-26 00:28:00 | TERRA_M-M | ACOPIARA | CEARÁ | Brasil | 2300309 | 23 | 33 | nan | nan | nan | Caatinga | 8.8 |
| 45d6d826-5ebf-381c-a40e-917fa52e4773 | -4.95933 | -38.52465 | 2024-11-26 00:28:00 | TERRA_M-M | IBICUITINGA | CEARÁ | Brasil | 2305332 | 23 | 33 | nan | nan | nan | Caatinga | 5.8 |
| 9451c49a-eeae-3183-bcc3-994e16d8141d | -5.94979 | -39.6673 | 2024-11-26 00:28:00 | TERRA_M-M | MOMBAÇA | CEARÁ | Brasil | 2308500 | 23 | 33 | nan | nan | nan | Caatinga | 31.5 |
| 76f6faf9-2b38-386c-b03a-9dd2fd538fd9 | -5.19465 | -47.81957 | 2024-11-26 00:28:00 | TERRA_M-M | CIDELÂNDIA | MARANHÃO | Brasil | 2103257 | 21 | 33 | nan | nan | nan | Amazônia | 18.8 |
| f271f67b-c39d-3b13-80b3-2fed5f52c518 | -5.65172 | -44.32697 | 2024-11-26 00:28:00 | TERRA_M-M | SÃO DOMINGOS DO MARANHÃO | MARANHÃO | Brasil | 2110708 | 21 | 33 | nan | nan | nan | Cerrado | 9.2 |
| 152e1ddf-1652-3e51-b066-5c5af1bf99a5 | -4.25222 | -40.68657 | 2024-11-26 00:28:00 | TERRA_M-M | PIRES FERREIRA | CEARÁ | Brasil | 2310951 | 23 | 33 | nan | nan | nan | Caatinga | 6.7 |
| fc40aa84-9582-3467-a479-6f35317a02e2 | -4.76332 | -45.59256 | 2024-11-26 00:28:00 | TERRA_M-M | MARAJÁ DO SENA | MARANHÃO | Brasil | 2106359 | 21 | 33 | nan | nan | nan | Cerrado | 5.7 |
| c0e970ef-9252-353f-982b-de249ea55f03 | -5.65306 | -44.33673 | 2024-11-26 00:28:00 | TERRA_M-M | SÃO DOMINGOS DO MARANHÃO | MARANHÃO | Brasil | 2110708 | 21 | 33 | nan | nan | nan | Cerrado | 9.1 |
| ca2af827-b566-3206-8ced-abf031d707ed | -9.86317 | -44.1182 | 2024-11-26 00:28:00 | TERRA_M-M | MORRO CABEÇA NO TEMPO | PIAUÍ | Brasil | 2206654 | 22 | 33 | nan | nan | nan | Cerrado | 6.3 |
| f7223d81-a2a4-34b7-83a2-e970c7755f1f | -4.81306 | -43.31239 | 2024-11-26 00:28:00 | TERRA_M-M | CAXIAS | MARANHÃO | Brasil | 2103000 | 21 | 33 | nan | nan | nan | Cerrado | 11.4 |
| 28fbbe69-c174-3bc6-bc57-6f2f76b1d68f | -5.28091 | -45.12156 | 2024-11-26 00:28:00 | TERRA_M-M | BARRA DO CORDA | MARANHÃO | Brasil | 2101608 | 21 | 33 | nan | nan | nan | Cerrado | 5.3 |
| 6a3b5204-2fd3-3005-ba37-922f9e652833 | -5.45129 | -36.88004 | 2024-11-26 00:28:00 | TERRA_M-M | AÇU | RIO GRANDE DO NORTE | Brasil | 2400208 | 24 | 33 | nan | nan | nan | Caatinga | 11.8 |
| 03af7c5f-8408-3eef-85fb-f2b714363b1a | -5.85525 | -39.42567 | 2024-11-26 00:28:00 | TERRA_M-M | PIQUET CARNEIRO | CEARÁ | Brasil | 2310902 | 23 | 33 | nan | nan | nan | Caatinga | 15.2 |
| f8383dc3-f167-38a7-84a0-5fbfb4c97688 | -6.07709 | -48.03494 | 2024-11-26 00:28:00 | TERRA_M-M | SÃO BENTO DO TOCANTINS | TOCANTINS | Brasil | 1720101 | 17 | 33 | nan | nan | nan | Cerrado | 268.8 |
| 60b4b22e-782d-31ee-8ce4-50d2ff80fe3b | -4.51107 | -42.0747 | 2024-11-26 00:28:00 | TERRA_M-M | BOQUEIRÃO DO PIAUÍ | PIAUÍ | Brasil | 2201945 | 22 | 33 | nan | nan | nan | Caatinga | 7.2 |
| e9dc27e9-5d67-319e-94c7-ae072e2914be | -4.95257 | -45.79132 | 2024-11-26 00:28:00 | TERRA_M-M | ARAME | MARANHÃO | Brasil | 2100956 | 21 | 33 | nan | nan | nan | Amazônia | 14.0 |
| be5d925b-d7b5-3632-b3a3-c4e7e6bd53f5 | -5.22403 | -44.91664 | 2024-11-26 00:28:00 | TERRA_M-M | BARRA DO CORDA | MARANHÃO | Brasil | 2101608 | 21 | 33 | nan | nan | nan | Cerrado | 10.4 |
| 5c087188-e0b8-30e7-b72a-d69c26530149 | -6.16165 | -46.81857 | 2024-11-26 00:28:00 | TERRA_M-M | LAJEADO NOVO | MARANHÃO | Brasil | 2105989 | 21 | 33 | nan | nan | nan | Cerrado | 7.7 |
| 31a25e6c-b25b-3fb4-bb93-836b1ba80d6a | -6.07052 | -48.02378 | 2024-11-26 00:28:00 | TERRA_M-M | SÃO BENTO DO TOCANTINS | TOCANTINS | Brasil | 1720101 | 17 | 33 | nan | nan | nan | Cerrado | 208.0 |
| a2f29233-1978-38ec-b621-501ac9cfd7e0 | -5.31437 | -43.0837 | 2024-11-26 00:28:00 | TERRA_M-M | TIMON | MARANHÃO | Brasil | 2112209 | 21 | 33 | nan | nan | nan | Cerrado | 4.0 |
| 46924e6b-da20-3505-906c-226e1d02e1e2 | -6.06702 | -39.19252 | 2024-11-26 00:28:00 | TERRA_M-M | ACOPIARA | CEARÁ | Brasil | 2300309 | 23 | 33 | nan | nan | nan | Caatinga | 5.6 |
| 3370476b-4659-3379-8dfa-4f6dff755e83 | -5.36822 | -43.40587 | 2024-11-26 00:28:00 | TERRA_M-M | MATÕES | MARANHÃO | Brasil | 2106607 | 21 | 33 | nan | nan | nan | Cerrado | 3.5 |
| 6706dceb-51e7-3d0f-8106-85f2c5926862 | -5.75911 | -46.26463 | 2024-11-26 00:28:00 | TERRA_M-M | GRAJAÚ | MARANHÃO | Brasil | 2104800 | 21 | 33 | nan | nan | nan | Cerrado | 4.6 |
| 26307ac9-ffff-37d2-8966-42ef017cc9fc | -6.98963 | -35.02747 | 2024-11-26 00:28:00 | TERRA_M-M | SANTA RITA | PARAÍBA | Brasil | 2513703 | 25 | 33 | nan | nan | nan | Mata Atlântica | 20.1 |
| 653beed9-e196-3e1d-8c9b-674121454dac | -9.44656 | -43.21195 | 2024-11-26 00:28:00 | TERRA_M-M | CAMPO ALEGRE DE LOURDES | BAHIA | Brasil | 2905909 | 29 | 33 | nan | nan | nan | Caatinga | 14.4 |
| bc9ae6a1-e317-38d5-8f6a-5f630fef406e | -5.69992 | -43.14194 | 2024-11-26 00:28:00 | TERRA_M-M | PARNARAMA | MARANHÃO | Brasil | 2107803 | 21 | 33 | nan | nan | nan | Caatinga | 4.9 |
| cf883b04-1206-36c5-af6d-4a270c1e0d19 | -6.07491 | -48.01762 | 2024-11-26 00:28:00 | TERRA_M-M | SÃO BENTO DO TOCANTINS | TOCANTINS | Brasil | 1720101 | 17 | 33 | nan | nan | nan | Cerrado | 58.4 |
| c03b3724-7086-3308-bc32-b6e7159b3977 | -5.50302 | -35.59275 | 2024-11-26 00:28:00 | TERRA_M-M | TAIPU | RIO GRANDE DO NORTE | Brasil | 2413904 | 24 | 33 | nan | nan | nan | Caatinga | 26.7 |
| d8233ba8-97e9-37d0-b0b8-d3c28d0b3fcd | -9.43741 | -43.21322 | 2024-11-26 00:28:00 | TERRA_M-M | CAMPO ALEGRE DE LOURDES | BAHIA | Brasil | 2905909 | 29 | 33 | nan | nan | nan | Caatinga | 7.4 |
| 6f302ec1-74c2-31d3-ae60-206c69ffb688 | -4.8025 | -43.31103 | 2024-11-26 00:28:00 | TERRA_M-M | CAXIAS | MARANHÃO | Brasil | 2103000 | 21 | 33 | nan | nan | nan | Cerrado | 6.7 |
| 2fd7153c-b975-342c-8372-faf3fd47acff | -6.18989 | -43.42085 | 2024-11-26 00:28:00 | TERRA_M-M | LAGOA DO MATO | MARANHÃO | Brasil | 2105922 | 21 | 33 | nan | nan | nan | Cerrado | 6.4 |
| ac7ecbb3-cf02-383a-af1b-5229f870607c | -4.95483 | -38.53296 | 2024-11-26 00:28:00 | TERRA_M-M | IBICUITINGA | CEARÁ | Brasil | 2305332 | 23 | 33 | nan | nan | nan | Caatinga | 13.6 |
| c4d54b3e-9330-35f9-8a73-bdd6a5bc3723 | -6.20705 | -39.74073 | 2024-11-26 00:28:00 | TERRA_M-M | ACOPIARA | CEARÁ | Brasil | 2300309 | 23 | 33 | nan | nan | nan | Caatinga | 6.3 |
| 6c6f7974-1e1f-3b16-88b3-99f0fa928463 | -4.95101 | -45.77999 | 2024-11-26 00:28:00 | TERRA_M-M | ARAME | MARANHÃO | Brasil | 2100956 | 21 | 33 | nan | nan | nan | Amazônia | 10.5 |
| c10d45ed-6aff-3145-964a-336f56ff1854 | -6.99697 | -35.02053 | 2024-11-26 00:28:00 | TERRA_M-M | SANTA RITA | PARAÍBA | Brasil | 2513703 | 25 | 33 | nan | nan | nan | Mata Atlântica | 25.2 |
| 389dd97f-41dd-37bc-a949-f6979513f2d5 | -5.76406 | -46.30279 | 2024-11-26 00:28:00 | TERRA_M-M | GRAJAÚ | MARANHÃO | Brasil | 2104800 | 21 | 33 | nan | nan | nan | Cerrado | 8.4 |
| a7b0f52f-5d94-3ece-96b6-a8a856f81234 | -6.07285 | -48.04127 | 2024-11-26 00:28:00 | TERRA_M-M | SÃO BENTO DO TOCANTINS | TOCANTINS | Brasil | 1720101 | 17 | 33 | nan | nan | nan | Cerrado | 184.4 |
| 68bda3be-0444-36e0-9694-64eabb07c5ef | -5.95656 | -44.46733 | 2024-11-26 00:28:00 | TERRA_M-M | COLINAS | MARANHÃO | Brasil | 2103505 | 21 | 33 | nan | nan | nan | Cerrado | 6.0 |
| f647810f-206f-3e7c-806a-cf9845df19e5 | -5.75649 | -43.08199 | 2024-11-26 00:28:00 | TERRA_M-M | PALMEIRAIS | PIAUÍ | Brasil | 2207504 | 22 | 33 | nan | nan | nan | Caatinga | 4.1 |
| 6f28a9cb-ff31-36b6-9e2b-9fe0d5e3925a | -6.63185 | -38.30308 | 2024-11-26 00:28:00 | TERRA_M-M | SOUSA | PARAÍBA | Brasil | 2516201 | 25 | 33 | nan | nan | nan | Caatinga | 7.6 |
| a68c3739-3f93-3046-af18-602c23297e28 | -5.94673 | -43.79441 | 2024-11-26 00:28:00 | TERRA_M-M | BURITI BRAVO | MARANHÃO | Brasil | 2102309 | 21 | 33 | nan | nan | nan | Cerrado | 7.9 |
| a5a1eea5-01ef-3bf5-b608-89f4c7a98b97 | -5.65852 | -46.64971 | 2024-11-26 00:28:00 | TERRA_M-M | AMARANTE DO MARANHÃO | MARANHÃO | Brasil | 2100600 | 21 | 33 | nan | nan | nan | Cerrado | 9.7 |
| a2b639d9-f4d9-3562-8d99-1fb6d67bea71 | -5.19562 | -47.73765 | 2024-11-26 00:28:00 | TERRA_M-M | CIDELÂNDIA | MARANHÃO | Brasil | 2103257 | 21 | 33 | nan | nan | nan | Amazônia | 16.8 |
| b779c0d3-2e09-306b-9856-bab2a7a981c7 | -6.19946 | -44.4355 | 2024-11-26 00:28:00 | TERRA_M-M | MIRADOR | MARANHÃO | Brasil | 2106706 | 21 | 33 | nan | nan | nan | Cerrado | 5.0 |
| ccc05f2c-398d-30f2-a482-aefeb4d87979 | -5.66459 | -45.84742 | 2024-11-26 00:28:00 | TERRA_M-M | GRAJAÚ | MARANHÃO | Brasil | 2104800 | 21 | 33 | nan | nan | nan | Cerrado | 6.2 |
| 5aa2324b-0b0f-3f65-b353-a807f6daa4d3 | -6.18863 | -43.41175 | 2024-11-26 00:28:00 | TERRA_M-M | LAGOA DO MATO | MARANHÃO | Brasil | 2105922 | 21 | 33 | nan | nan | nan | Cerrado | 17.0 |
| 7cc94c87-7553-3d18-a0b5-82c87f34b8c9 | -6.06564 | -39.18735 | 2024-11-26 00:28:00 | TERRA_M-M | ACOPIARA | CEARÁ | Brasil | 2300309 | 23 | 33 | nan | nan | nan | Caatinga | 11.6 |
| 1664a452-d840-3d06-9f25-f73f4972e111 | -6.84595 | -35.2873 | 2024-11-26 00:28:00 | TERRA_M-M | ITAPOROROCA | PARAÍBA | Brasil | 2507101 | 25 | 33 | nan | nan | nan | Caatinga | 13.4 |
| 9d2c7727-0851-3061-8b69-35f8cf3e121d | -4.96188 | -45.78395 | 2024-11-26 00:28:00 | TERRA_M-M | ARAME | MARANHÃO | Brasil | 2100956 | 21 | 33 | nan | nan | nan | Amazônia | 7.2 |
| df9b3ed9-16e2-367a-9b98-1c401ec793f8 | -6.84267 | -35.26588 | 2024-11-26 00:28:00 | TERRA_M-M | ITAPOROROCA | PARAÍBA | Brasil | 2507101 | 25 | 33 | nan | nan | nan | Caatinga | 22.0 |
| 32eebb66-df3e-334a-968f-246e45a0a301 | -1.4768 | -53.8148 | 2024-11-26 00:30:00 | GOES-16 | PRAINHA | PARÁ | Brasil | 1506005 | 15 | 33 | nan | nan | nan | Amazônia | 83.8 |
| 3e1f05db-fedb-3316-ac80-62a97537d696 | -2.8014 | -53.0024 | 2024-11-26 00:30:00 | GOES-16 | MEDICILÂNDIA | PARÁ | Brasil | 1504455 | 15 | 33 | nan | nan | nan | Amazônia | 72.5 |
| f2f51fd4-75a1-3af1-a378-ae357705a420 | -3.5856 | -50.3997 | 2024-11-26 00:30:00 | GOES-16 | PACAJÁ | PARÁ | Brasil | 1505486 | 15 | 33 | nan | nan | nan | Amazônia | 122.9 |
| ea4e8178-8890-3386-bb7d-73f08e233ee7 | -2.8198 | -53.0222 | 2024-11-26 00:30:00 | GOES-16 | MEDICILÂNDIA | PARÁ | Brasil | 1504455 | 15 | 33 | nan | nan | nan | Amazônia | 67.6 |
| 8512d0e6-1c04-3475-8c9a-91c7d6bff677 | -1.4952 | -53.7945 | 2024-11-26 00:30:00 | GOES-16 | PRAINHA | PARÁ | Brasil | 1506005 | 15 | 33 | nan | nan | nan | Amazônia | 65.1 |
| 22d793a7-ef69-3d03-b27e-48f5385e862d | -3.9859 | -48.0843 | 2024-11-26 00:30:00 | GOES-16 | DOM ELISEU | PARÁ | Brasil | 1502939 | 15 | 33 | nan | nan | nan | Amazônia | 70.4 |
| 4f6a2ca8-b6f2-3418-8380-926e69d6ba3e | -2.1965 | -45.9754 | 2024-11-26 00:30:00 | GOES-16 | GOVERNADOR NUNES FREIRE | MARANHÃO | Brasil | 2104677 | 21 | 33 | nan | nan | nan | Amazônia | 45.7 |
| 992a0326-8841-3ee8-8136-0187e21490ec | -3.5857 | -50.3787 | 2024-11-26 00:30:00 | GOES-16 | PACAJÁ | PARÁ | Brasil | 1505486 | 15 | 33 | nan | nan | nan | Amazônia | 228.0 |
| 46b62354-9884-3257-b38f-9a9dd904f856 | -2.8014 | -53.0227 | 2024-11-26 00:30:00 | GOES-16 | MEDICILÂNDIA | PARÁ | Brasil | 1504455 | 15 | 33 | nan | nan | nan | Amazônia | 126.9 |
| 1e58db6d-0e68-309a-970e-2641ec2953aa | -3.9265 | -42.4246 | 2024-11-26 00:30:00 | GOES-16 | CAMPO LARGO DO PIAUÍ | PIAUÍ | Brasil | 2202174 | 22 | 33 | nan | nan | nan | Caatinga | 96.8 |
| fd01f7f2-4f8d-3034-bf8c-07cf48e4122d | -3.6041 | -50.3991 | 2024-11-26 00:30:00 | GOES-16 | PACAJÁ | PARÁ | Brasil | 1505486 | 15 | 33 | nan | nan | nan | Amazônia | 170.8 |
| 3ba94bee-234a-38a0-8ab3-da7146e46d07 | -17.6453 | -57.5874 | 2024-11-26 00:30:00 | GOES-16 | POCONÉ | MATO GROSSO | Brasil | 5106505 | 51 | 33 | nan | nan | nan | Pantanal | 54.3 |
| 6bbcb956-603b-3632-96d7-5ca7a4d020d3 | -1.4951 | -53.8146 | 2024-11-26 00:30:00 | GOES-16 | PRAINHA | PARÁ | Brasil | 1506005 | 15 | 33 | nan | nan | nan | Amazônia | 93.4 |
| 8daa2d7f-ff92-3a25-99bf-d99d083082e6 | -3.9674 | -48.0851 | 2024-11-26 00:30:00 | GOES-16 | DOM ELISEU | PARÁ | Brasil | 1502939 | 15 | 33 | nan | nan | nan | Amazônia | 52.9 |
| 3b4f23d7-f1fc-353c-a01c-d130ec957dd3 | -3.3938 | -44.1722 | 2024-11-26 00:30:00 | GOES-16 | ITAPECURU MIRIM | MARANHÃO | Brasil | 2105401 | 21 | 33 | nan | nan | nan | Cerrado | 91.3 |
| 86fae92d-2f33-34cc-886d-ee356f9558dc | -3.1692 | -48.4179 | 2024-11-26 00:30:00 | GOES-16 | TOMÉ-AÇU | PARÁ | Brasil | 1508001 | 15 | 33 | nan | nan | nan | Amazônia | 70.4 |
| 10228970-b12c-3180-9333-e05edf222940 | -3.9078 | -42.4256 | 2024-11-26 00:30:00 | GOES-16 | CAMPO LARGO DO PIAUÍ | PIAUÍ | Brasil | 2202174 | 22 | 33 | nan | nan | nan | Caatinga | 118.1 |
| 8d8a6816-d3a0-3f6b-b655-892ec51d1ea0 | 2.6718 | -60.4304 | 2024-11-26 00:30:00 | GOES-16 | CANTÁ | RORAIMA | Brasil | 1400175 | 14 | 33 | nan | nan | nan | Amazônia | 73.7 |
| 1f143892-a100-31ce-ab2a-a2a8ea88810a | -3.986 | -48.0626 | 2024-11-26 00:30:00 | GOES-16 | DOM ELISEU | PARÁ | Brasil | 1502939 | 15 | 33 | nan | nan | nan | Amazônia | 79.3 |
| 45bc1d3b-8d85-3654-a692-f996d373d8e5 | -3.1876 | -48.4387 | 2024-11-26 00:30:00 | GOES-16 | TOMÉ-AÇU | PARÁ | Brasil | 1508001 | 15 | 33 | nan | nan | nan | Amazônia | 373.5 |
| 5bcb1de5-804f-3a59-afbb-57bdda705e9f | -3.1691 | -48.4394 | 2024-11-26 00:30:00 | GOES-16 | TOMÉ-AÇU | PARÁ | Brasil | 1508001 | 15 | 33 | nan | nan | nan | Amazônia | 155.7 |
| 2ccf5231-e1da-3544-8655-0870fe1ff0fd | -3.9267 | -42.401 | 2024-11-26 00:30:00 | GOES-16 | CAMPO LARGO DO PIAUÍ | PIAUÍ | Brasil | 2202174 | 22 | 33 | nan | nan | nan | Caatinga | 59.8 |
| 822416ee-0fb7-3814-848e-c82ad8debaa5 | -3.1875 | -48.4603 | 2024-11-26 00:30:00 | GOES-16 | TOMÉ-AÇU | PARÁ | Brasil | 1508001 | 15 | 33 | nan | nan | nan | Amazônia | 69.5 |
| 198dfac6-3969-35c5-90ea-02f6d04f2e34 | -6.0676 | -48.0352 | 2024-11-26 00:30:00 | GOES-16 | SÃO BENTO DO TOCANTINS | TOCANTINS | Brasil | 1720101 | 17 | 33 | nan | nan | nan | Cerrado | 106.4 |
| 6c92fdbd-92cd-3e6c-ac3d-c8cfc1a599dc | 3.8257 | -59.5896 | 2024-11-26 00:30:00 | GOES-16 | NORMANDIA | RORAIMA | Brasil | 1400407 | 14 | 33 | nan | nan | nan | Amazônia | 73.1 |
| 9116f999-91fb-3ad8-b099-1e2d3f2fd83c | 2.6901 | -60.4301 | 2024-11-26 00:30:00 | GOES-16 | CANTÁ | RORAIMA | Brasil | 1400175 | 14 | 33 | nan | nan | nan | Amazônia | 62.5 |
| 9d2f2390-a98e-39b8-9506-716d2d8f7eda | -3.9675 | -48.0634 | 2024-11-26 00:30:00 | GOES-16 | DOM ELISEU | PARÁ | Brasil | 1502939 | 15 | 33 | nan | nan | nan | Amazônia | 56.3 |
| b48dd82b-011e-344c-be34-b4633f6ef61f | -3.6042 | -50.3781 | 2024-11-26 00:30:00 | GOES-16 | PACAJÁ | PARÁ | Brasil | 1505486 | 15 | 33 | nan | nan | nan | Amazônia | 341.4 |
| 14f0248f-fc9d-386a-8122-ea3b3a41a157 | -3.3939 | -44.1492 | 2024-11-26 00:30:00 | GOES-16 | ITAPECURU MIRIM | MARANHÃO | Brasil | 2105401 | 21 | 33 | nan | nan | nan | Cerrado | 39.6 |
| 78a50015-c40e-391f-b235-17922db48a8e | -3.908 | -42.402 | 2024-11-26 00:30:00 | GOES-16 | CAMPO LARGO DO PIAUÍ | PIAUÍ | Brasil | 2202174 | 22 | 33 | nan | nan | nan | Caatinga | 81.8 |
| 22b7d9ba-37e3-32a7-ab60-2665b20fb8ab | -3.3752 | -44.173 | 2024-11-26 00:30:00 | GOES-16 | ITAPECURU MIRIM | MARANHÃO | Brasil | 2105401 | 21 | 33 | nan | nan | nan | Cerrado | 64.5 |
| 452d2842-275d-3fac-8495-7dfe6302447a | -4.6547 | -47.9444 | 2024-11-26 00:30:00 | GOES-16 | RONDON DO PARÁ | PARÁ | Brasil | 1506187 | 15 | 33 | nan | nan | nan | Amazônia | 93.0 |
| ba611778-f326-38d7-8764-dffe617aefc6 | -3.1877 | -48.4172 | 2024-11-26 00:30:00 | GOES-16 | TOMÉ-AÇU | PARÁ | Brasil | 1508001 | 15 | 33 | nan | nan | nan | Amazônia | 152.8 |
| 9dff3984-b36b-3822-b884-8c169fd95f35 | -4.6733 | -47.9434 | 2024-11-26 00:30:00 | GOES-16 | RONDON DO PARÁ | PARÁ | Brasil | 1506187 | 15 | 33 | nan | nan | nan | Amazônia | 101.0 |
| 4bc3e017-99aa-3c39-b5ce-fa4861eac8a4 | -2.46831 | -45.47709 | 2024-11-26 00:30:00 | TERRA_M-M | SANTA HELENA | MARANHÃO | Brasil | 2109809 | 21 | 33 | nan | nan | nan | Amazônia | 4.5 |
| b2a9ff41-2267-3dcd-b121-2539d2f47c79 | -2.98823 | -49.59484 | 2024-11-26 00:30:00 | TERRA_M-M | MOJU | PARÁ | Brasil | 1504703 | 15 | 33 | nan | nan | nan | Amazônia | 15.8 |
| 14ba8b64-b859-3383-999d-e83f90e4703c | -3.68866 | -40.74355 | 2024-11-26 00:30:00 | TERRA_M-M | COREAÚ | CEARÁ | Brasil | 2304004 | 23 | 33 | nan | nan | nan | Caatinga | 11.3 |


[Clique aqui para ver as próximas entradas](README3.md)
