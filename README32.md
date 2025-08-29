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

## Dados Diários - Página 32

| ID | Latitude | Longitude | Data/Hora GMT | Satélite | Município | Estado | País | Município ID | Estado ID | País ID | Dias sem Chuva | Precipitação | Risco de Fogo | Bioma | FRP |
|----|----------|-----------|---------------|----------|-----------|--------|------|--------------|-----------|---------|----------------|--------------|----------------|-------|-----|
| cb65a643-70fd-319a-8ba8-9906670e03d2 | -13.90547 | -43.87988 | 2025-08-29 03:49:00 | NOAA-20 | CARINHANHA | BAHIA | Brasil | 2907103 | 29 | 33 | nan | nan | nan | Cerrado | 1.0 |
| 5ff09c75-7722-3ec3-97a3-40a7459679d5 | -6.55048 | -43.92334 | 2025-08-29 03:49:00 | NOAA-20 | PASTOS BONS | MARANHÃO | Brasil | 2108009 | 21 | 33 | nan | nan | nan | Cerrado | 4.4 |
| 85ffff6f-2950-3542-ac21-3b86e5028dbe | -5.69965 | -45.9643 | 2025-08-29 03:49:00 | NOAA-20 | GRAJAÚ | MARANHÃO | Brasil | 2104800 | 21 | 33 | nan | nan | nan | Cerrado | 1.1 |
| 98c94a94-9bb5-3d3b-84e1-84d1876516cf | -6.43593 | -44.5704 | 2025-08-29 03:49:00 | NOAA-20 | MIRADOR | MARANHÃO | Brasil | 2106706 | 21 | 33 | nan | nan | nan | Cerrado | 3.4 |
| a338c97d-bf87-3e03-8150-063ebde12d83 | -13.54983 | -46.93987 | 2025-08-29 03:49:00 | NOAA-20 | MONTE ALEGRE DE GOIÁS | GOIÁS | Brasil | 5213509 | 52 | 33 | nan | nan | nan | Cerrado | 4.9 |
| 5d27b374-82fa-33f4-b593-0f3a7c3ecf91 | -12.69912 | -48.14829 | 2025-08-29 03:49:00 | NOAA-20 | PARANÃ | TOCANTINS | Brasil | 1716208 | 17 | 33 | nan | nan | nan | Cerrado | 2.8 |
| afae9bf4-0c43-32be-b6ba-48b92bc39b7e | -13.4529 | -46.96138 | 2025-08-29 03:49:00 | NOAA-20 | MONTE ALEGRE DE GOIÁS | GOIÁS | Brasil | 5213509 | 52 | 33 | nan | nan | nan | Cerrado | 7.2 |
| c1ab98fe-0308-349a-97d6-d1ef2ac5f42b | -13.40593 | -46.96198 | 2025-08-29 03:49:00 | NOAA-20 | MONTE ALEGRE DE GOIÁS | GOIÁS | Brasil | 5213509 | 52 | 33 | nan | nan | nan | Cerrado | 1.0 |
| 4d5e8bb4-7bf1-3363-ad2f-b99336832b5c | -12.70398 | -48.15262 | 2025-08-29 03:49:00 | NOAA-20 | PARANÃ | TOCANTINS | Brasil | 1716208 | 17 | 33 | nan | nan | nan | Cerrado | 7.3 |
| f29797f6-0026-3548-add0-199326546353 | -11.26667 | -45.4943 | 2025-08-29 03:49:00 | NOAA-20 | FORMOSA DO RIO PRETO | BAHIA | Brasil | 2911105 | 29 | 33 | nan | nan | nan | Cerrado | 3.5 |
| c89f5577-d1df-398e-bfeb-98ec2bb84cf9 | -12.70155 | -48.19473 | 2025-08-29 03:49:00 | NOAA-20 | PARANÃ | TOCANTINS | Brasil | 1716208 | 17 | 33 | nan | nan | nan | Cerrado | 11.6 |
| 71cb2dfa-dd46-3383-8425-0c71dfa9a0c4 | -5.69427 | -45.96335 | 2025-08-29 03:49:00 | NOAA-20 | GRAJAÚ | MARANHÃO | Brasil | 2104800 | 21 | 33 | nan | nan | nan | Cerrado | 1.1 |
| 03e74539-d4b1-3372-afef-b40d031a92b6 | -17.76532 | -44.49478 | 2025-08-29 03:49:00 | NOAA-20 | LASSANCE | MINAS GERAIS | Brasil | 3138104 | 31 | 33 | nan | nan | nan | Cerrado | 1.5 |
| 3f6a636c-50fb-39ec-baf4-880f68672810 | -5.92486 | -43.34299 | 2025-08-29 03:49:00 | NOAA-20 | LAGOA DO MATO | MARANHÃO | Brasil | 2105922 | 21 | 33 | nan | nan | nan | Cerrado | 3.0 |
| 4b7aa6c8-490b-3c4f-8b27-a5558f3bca1f | -6.53324 | -44.11084 | 2025-08-29 03:49:00 | NOAA-20 | PASTOS BONS | MARANHÃO | Brasil | 2108009 | 21 | 33 | nan | nan | nan | Cerrado | 4.3 |
| 03639e3b-9e49-3fe8-ae55-ab9edb6c11ae | -6.48831 | -44.40704 | 2025-08-29 03:49:00 | NOAA-20 | SUCUPIRA DO NORTE | MARANHÃO | Brasil | 2111904 | 21 | 33 | nan | nan | nan | Cerrado | 3.8 |
| 98e8133d-56b5-3fa3-824d-73e0111efa46 | -12.82531 | -48.17342 | 2025-08-29 03:49:00 | NOAA-20 | PARANÃ | TOCANTINS | Brasil | 1716208 | 17 | 33 | nan | nan | nan | Cerrado | 3.2 |
| 3065edb2-ebf0-3f8f-bdbf-f7f8a33d4467 | -3.9842 | -47.96232 | 2025-08-29 03:49:00 | NOAA-20 | DOM ELISEU | PARÁ | Brasil | 1502939 | 15 | 33 | nan | nan | nan | Amazônia | 1.1 |
| 7a39fe7c-871a-34d5-8989-336725645348 | -6.1958 | -43.3213 | 2025-08-29 03:49:00 | NOAA-20 | LAGOA DO MATO | MARANHÃO | Brasil | 2105922 | 21 | 33 | nan | nan | nan | Cerrado | 1.2 |
| 74319a1f-70c9-33da-9002-6b0094194049 | -11.26102 | -45.49855 | 2025-08-29 03:49:00 | NOAA-20 | FORMOSA DO RIO PRETO | BAHIA | Brasil | 2911105 | 29 | 33 | nan | nan | nan | Cerrado | 1.0 |
| cdc9cc80-4d31-3b27-857c-17d4d10e2b70 | -11.90289 | -46.71691 | 2025-08-29 03:49:00 | NOAA-20 | NOVO JARDIM | TOCANTINS | Brasil | 1715259 | 17 | 33 | nan | nan | nan | Cerrado | 1.1 |
| df639336-5ded-326f-980f-a00b965d6a7e | -6.36767 | -40.63867 | 2025-08-29 03:49:00 | NOAA-20 | PARAMBU | CEARÁ | Brasil | 2310308 | 23 | 33 | nan | nan | nan | Caatinga | 1.1 |
| c75bacb4-c452-36b9-836c-ae9c362e8fe4 | -12.82524 | -48.17278 | 2025-08-29 03:49:00 | NOAA-20 | PARANÃ | TOCANTINS | Brasil | 1716208 | 17 | 33 | nan | nan | nan | Cerrado | 2.6 |
| 52af4bc8-b74b-3e8b-bc85-427f2c41359b | -15.16829 | -52.33958 | 2025-08-29 03:49:00 | NOAA-20 | BARRA DO GARÇAS | MATO GROSSO | Brasil | 5101803 | 51 | 33 | nan | nan | nan | Cerrado | 2.5 |
| b94893b8-6723-30cb-8f03-7b6fd5263179 | -7.15329 | -39.42036 | 2025-08-29 03:49:00 | NOAA-20 | CRATO | CEARÁ | Brasil | 2304202 | 23 | 33 | nan | nan | nan | Caatinga | 2.3 |
| a71b09a1-aeec-3d08-9d7b-61cb5d322205 | -6.43017 | -44.57494 | 2025-08-29 03:49:00 | NOAA-20 | MIRADOR | MARANHÃO | Brasil | 2106706 | 21 | 33 | nan | nan | nan | Cerrado | 3.4 |
| 4fdeac5e-4e3a-305d-adb0-160c944d6027 | -5.62035 | -45.00674 | 2025-08-29 03:49:00 | NOAA-20 | BARRA DO CORDA | MARANHÃO | Brasil | 2101608 | 21 | 33 | nan | nan | nan | Cerrado | 6.4 |
| 266640b1-9b23-3352-b590-2ac4e9d8a79c | -12.70001 | -48.20274 | 2025-08-29 03:49:00 | NOAA-20 | PARANÃ | TOCANTINS | Brasil | 1716208 | 17 | 33 | nan | nan | nan | Cerrado | 27.1 |
| a093fa52-1b17-3e0f-9d3b-1f89a800be33 | -3.42002 | -49.0489 | 2025-08-29 03:49:00 | NOAA-20 | BREU BRANCO | PARÁ | Brasil | 1501782 | 15 | 33 | nan | nan | nan | Amazônia | 8.4 |
| 2b3009b1-c375-33e3-9584-36c1b19ee686 | -15.12417 | -48.12493 | 2025-08-29 03:49:00 | NOAA-20 | MIMOSO DE GOIÁS | GOIÁS | Brasil | 5213053 | 52 | 33 | nan | nan | nan | Cerrado | 1.8 |
| d1486b71-bcf0-33ab-b043-d0fef58f344d | -17.53884 | -46.62595 | 2025-08-29 03:49:00 | NOAA-20 | VAZANTE | MINAS GERAIS | Brasil | 3171006 | 31 | 33 | nan | nan | nan | Cerrado | 2.0 |
| 38e9481d-22f5-3e14-b603-5c1310c546b1 | -13.98733 | -46.32982 | 2025-08-29 03:49:00 | NOAA-20 | GUARANI DE GOIÁS | GOIÁS | Brasil | 5209408 | 52 | 33 | nan | nan | nan | Cerrado | 1.0 |
| adf87d07-f359-3dc2-b268-f14d0d3306c5 | -6.54509 | -43.92709 | 2025-08-29 03:49:00 | NOAA-20 | PASTOS BONS | MARANHÃO | Brasil | 2108009 | 21 | 33 | nan | nan | nan | Cerrado | 27.5 |
| b99bd27e-b767-3805-b504-e2a1039576d0 | -14.46614 | -48.37966 | 2025-08-29 03:49:00 | NOAA-20 | NIQUELÂNDIA | GOIÁS | Brasil | 5214606 | 52 | 33 | nan | nan | nan | Cerrado | 2.0 |
| 810a267a-1359-3ab7-9b2f-23a41695f38b | -12.92422 | -46.34319 | 2025-08-29 03:49:00 | NOAA-20 | LAVANDEIRA | TOCANTINS | Brasil | 1712157 | 17 | 33 | nan | nan | nan | Cerrado | 6.1 |
| c506dbc9-8c36-333a-bd26-23fbfc5ca30f | -12.70353 | -48.15465 | 2025-08-29 03:49:00 | NOAA-20 | PARANÃ | TOCANTINS | Brasil | 1716208 | 17 | 33 | nan | nan | nan | Cerrado | 7.1 |
| d93e3893-e0e5-345c-8666-d962abc3e66c | -12.85674 | -48.10034 | 2025-08-29 03:49:00 | NOAA-20 | PARANÃ | TOCANTINS | Brasil | 1716208 | 17 | 33 | nan | nan | nan | Cerrado | 1.7 |
| ccb81756-dcdf-38c7-b2ac-07334bff8d0a | -12.84527 | -48.101 | 2025-08-29 03:49:00 | NOAA-20 | PARANÃ | TOCANTINS | Brasil | 1716208 | 17 | 33 | nan | nan | nan | Cerrado | 6.8 |
| cb0dda1d-e958-3087-92b1-5b223293bdc1 | -12.82603 | -48.16884 | 2025-08-29 03:49:00 | NOAA-20 | PARANÃ | TOCANTINS | Brasil | 1716208 | 17 | 33 | nan | nan | nan | Cerrado | 2.6 |
| dcdf0191-4a2b-3f96-8703-8a06fe782ff3 | -11.61262 | -46.20842 | 2025-08-29 03:49:00 | NOAA-20 | DIANÓPOLIS | TOCANTINS | Brasil | 1707009 | 17 | 33 | nan | nan | nan | Cerrado | 1.5 |
| 97e2979a-775e-3505-8bf9-c4030d729a45 | -10.02784 | -48.06906 | 2025-08-29 03:49:00 | NOAA-20 | APARECIDA DO RIO NEGRO | TOCANTINS | Brasil | 1701101 | 17 | 33 | nan | nan | nan | Cerrado | 4.2 |
| 9d81f075-dd01-3af5-a577-1b70bed45d01 | -6.50468 | -42.93261 | 2025-08-29 03:49:00 | NOAA-20 | BARÃO DE GRAJAÚ | MARANHÃO | Brasil | 2101509 | 21 | 33 | nan | nan | nan | Cerrado | 2.8 |
| 6962b1f2-4b0b-3be6-ac84-bced91ba005d | -14.33729 | -48.65117 | 2025-08-29 03:49:00 | NOAA-20 | NIQUELÂNDIA | GOIÁS | Brasil | 5214606 | 52 | 33 | nan | nan | nan | Cerrado | 1.9 |
| 168c05fa-a4f2-3200-9ace-891cad8ddf97 | -13.4144 | -46.97203 | 2025-08-29 03:49:00 | NOAA-20 | MONTE ALEGRE DE GOIÁS | GOIÁS | Brasil | 5213509 | 52 | 33 | nan | nan | nan | Cerrado | 4.5 |
| 5a4619f4-cb82-3918-be3a-cd577aaf1174 | -12.92187 | -48.14453 | 2025-08-29 03:49:00 | NOAA-20 | PARANÃ | TOCANTINS | Brasil | 1716208 | 17 | 33 | nan | nan | nan | Cerrado | 1.6 |
| 3f6994fb-3089-3f4a-a73c-9b2def3f7294 | -6.14398 | -44.43373 | 2025-08-29 03:49:00 | NOAA-20 | MIRADOR | MARANHÃO | Brasil | 2106706 | 21 | 33 | nan | nan | nan | Cerrado | 4.2 |
| a01ba7ef-248b-3143-8033-2575cddc7d54 | -11.6137 | -46.20266 | 2025-08-29 03:49:00 | NOAA-20 | DIANÓPOLIS | TOCANTINS | Brasil | 1707009 | 17 | 33 | nan | nan | nan | Cerrado | 1.5 |
| dd5e8755-f459-34b8-bf71-1e1850f8db54 | -11.2408 | -45.00733 | 2025-08-29 03:49:00 | NOAA-20 | FORMOSA DO RIO PRETO | BAHIA | Brasil | 2911105 | 29 | 33 | nan | nan | nan | Cerrado | 1.2 |
| 61dd4921-50be-3ca4-a5f5-e6e37fec991c | -13.67021 | -46.87859 | 2025-08-29 03:49:00 | NOAA-20 | NOVA ROMA | GOIÁS | Brasil | 5214903 | 52 | 33 | nan | nan | nan | Cerrado | 2.9 |
| 8ca54ef1-41a6-3721-804d-52ce00a0ac9b | -13.40821 | -46.84335 | 2025-08-29 03:49:00 | NOAA-20 | MONTE ALEGRE DE GOIÁS | GOIÁS | Brasil | 5213509 | 52 | 33 | nan | nan | nan | Cerrado | 2.4 |
| 0a156a86-095b-3405-84ec-917625566b1a | -11.02754 | -45.06748 | 2025-08-29 03:49:00 | NOAA-20 | FORMOSA DO RIO PRETO | BAHIA | Brasil | 2911105 | 29 | 33 | nan | nan | nan | Cerrado | 4.4 |
| a4892c5c-6e38-3de6-93ba-a0726ed5796a | -15.04137 | -48.13203 | 2025-08-29 03:49:00 | NOAA-20 | MIMOSO DE GOIÁS | GOIÁS | Brasil | 5213053 | 52 | 33 | nan | nan | nan | Cerrado | 3.2 |
| 903d395d-b840-390b-a806-64f7871f074a | -11.3198 | -43.55316 | 2025-08-29 03:49:00 | NOAA-20 | BARRA | BAHIA | Brasil | 2902708 | 29 | 33 | nan | nan | nan | Cerrado | 0.9 |
| e4b12d11-48fe-31ce-964b-bb7b9dc9f3bf | -4.49092 | -47.6896 | 2025-08-29 03:49:00 | NOAA-20 | DOM ELISEU | PARÁ | Brasil | 1502939 | 15 | 33 | nan | nan | nan | Amazônia | 0.9 |
| 0aa4f7a1-e09d-3b4c-a2d8-8ddda96b4654 | -6.54391 | -43.10513 | 2025-08-29 03:49:00 | NOAA-20 | BARÃO DE GRAJAÚ | MARANHÃO | Brasil | 2101509 | 21 | 33 | nan | nan | nan | Cerrado | 1.5 |
| 01fd3631-2eed-3b41-941a-0e8819d50ecb | -12.83805 | -48.10709 | 2025-08-29 03:49:00 | NOAA-20 | PARANÃ | TOCANTINS | Brasil | 1716208 | 17 | 33 | nan | nan | nan | Cerrado | 3.4 |
| 2dfe5817-aa4b-3c1c-a560-15acf1ef8d51 | -13.5398 | -46.88448 | 2025-08-29 03:49:00 | NOAA-20 | MONTE ALEGRE DE GOIÁS | GOIÁS | Brasil | 5213509 | 52 | 33 | nan | nan | nan | Cerrado | 13.4 |
| 288256df-d784-38c0-8c1e-94ebac0158cd | -17.96415 | -43.98886 | 2025-08-29 03:49:00 | NOAA-20 | BUENÓPOLIS | MINAS GERAIS | Brasil | 3109204 | 31 | 33 | nan | nan | nan | Cerrado | 0.8 |
| 26874f6c-9b01-3392-bd99-7562f50d407e | -12.83233 | -48.16652 | 2025-08-29 03:49:00 | NOAA-20 | PARANÃ | TOCANTINS | Brasil | 1716208 | 17 | 33 | nan | nan | nan | Cerrado | 5.3 |
| e54eb598-4148-3c2a-a1d8-50ae91448fdb | -12.91405 | -48.12626 | 2025-08-29 03:49:00 | NOAA-20 | PARANÃ | TOCANTINS | Brasil | 1716208 | 17 | 33 | nan | nan | nan | Cerrado | 3.1 |
| e14e1206-2588-34fb-a2aa-8ee901d3ab4a | -10.03279 | -48.07417 | 2025-08-29 03:49:00 | NOAA-20 | APARECIDA DO RIO NEGRO | TOCANTINS | Brasil | 1701101 | 17 | 33 | nan | nan | nan | Cerrado | 3.3 |
| 9a59224d-dba2-384e-bf1a-28fc7125fcc6 | -13.36995 | -46.88157 | 2025-08-29 03:49:00 | NOAA-20 | MONTE ALEGRE DE GOIÁS | GOIÁS | Brasil | 5213509 | 52 | 33 | nan | nan | nan | Cerrado | 1.7 |
| cc0e649b-2347-3aa6-b360-247426f8245d | -14.62064 | -41.74155 | 2025-08-29 03:49:00 | NOAA-20 | PRESIDENTE JÂNIO QUADROS | BAHIA | Brasil | 2925709 | 29 | 33 | nan | nan | nan | Caatinga | 1.4 |
| b1829f7c-d927-30c4-a580-b7c1b367bc83 | -12.89962 | -48.14205 | 2025-08-29 03:49:00 | NOAA-20 | PARANÃ | TOCANTINS | Brasil | 1716208 | 17 | 33 | nan | nan | nan | Cerrado | 2.4 |
| fae2840a-9cb3-3cc5-8f74-8c7475941a2b | -12.83914 | -48.16029 | 2025-08-29 03:49:00 | NOAA-20 | PARANÃ | TOCANTINS | Brasil | 1716208 | 17 | 33 | nan | nan | nan | Cerrado | 2.0 |
| 51195274-bfcc-3e26-aa05-d4362d3f5594 | -13.54936 | -46.94232 | 2025-08-29 03:49:00 | NOAA-20 | MONTE ALEGRE DE GOIÁS | GOIÁS | Brasil | 5213509 | 52 | 33 | nan | nan | nan | Cerrado | 4.9 |
| f569a70b-eca6-3a1d-ad5a-143354827102 | -3.98504 | -47.95743 | 2025-08-29 03:49:00 | NOAA-20 | DOM ELISEU | PARÁ | Brasil | 1502939 | 15 | 33 | nan | nan | nan | Amazônia | 1.2 |
| 9e3ed3a2-1f55-3a21-9982-21ef36e208b8 | -5.65865 | -37.87991 | 2025-08-29 03:49:00 | NOAA-20 | APODI | RIO GRANDE DO NORTE | Brasil | 2401008 | 24 | 33 | nan | nan | nan | Caatinga | 0.6 |
| 8bdc0718-8413-3267-8b6f-2d3aed29233a | -11.57419 | -49.51934 | 2025-08-29 03:49:00 | NOAA-20 | FORMOSO DO ARAGUAIA | TOCANTINS | Brasil | 1708205 | 17 | 33 | nan | nan | nan | Cerrado | 1.4 |
| ffc7d066-fab6-3fac-88aa-297127256e9e | -11.06928 | -44.75826 | 2025-08-29 03:49:00 | NOAA-20 | SANTA RITA DE CÁSSIA | BAHIA | Brasil | 2928406 | 29 | 33 | nan | nan | nan | Cerrado | 1.3 |
| db6cafa4-630c-316b-b673-aa7c08c7293c | -5.61768 | -44.99946 | 2025-08-29 03:49:00 | NOAA-20 | BARRA DO CORDA | MARANHÃO | Brasil | 2101608 | 21 | 33 | nan | nan | nan | Cerrado | 10.1 |
| 849b0537-9a81-3089-8481-a99174a54b60 | -6.31202 | -43.53059 | 2025-08-29 03:49:00 | NOAA-20 | SUCUPIRA DO RIACHÃO | MARANHÃO | Brasil | 2111953 | 21 | 33 | nan | nan | nan | Cerrado | 3.4 |
| 051f7412-e451-3381-bd9a-9ede8ef0b6b9 | -10.01994 | -48.07914 | 2025-08-29 03:49:00 | NOAA-20 | APARECIDA DO RIO NEGRO | TOCANTINS | Brasil | 1701101 | 17 | 33 | nan | nan | nan | Cerrado | 3.3 |
| 2dc50424-534f-347e-a66e-212272bb1cfb | -13.47521 | -46.84454 | 2025-08-29 03:49:00 | NOAA-20 | MONTE ALEGRE DE GOIÁS | GOIÁS | Brasil | 5213509 | 52 | 33 | nan | nan | nan | Cerrado | 10.4 |
| 1ec4095f-09a6-3970-ac9f-3ff9d4820f6c | -12.87194 | -48.1383 | 2025-08-29 03:49:00 | NOAA-20 | PARANÃ | TOCANTINS | Brasil | 1716208 | 17 | 33 | nan | nan | nan | Cerrado | 1.2 |
| 6a37c58f-6388-3538-9d86-68b194b6685c | -13.41298 | -46.84587 | 2025-08-29 03:49:00 | NOAA-20 | MONTE ALEGRE DE GOIÁS | GOIÁS | Brasil | 5213509 | 52 | 33 | nan | nan | nan | Cerrado | 3.5 |
| d2da0f88-208d-3c85-83d7-c20f4fb49214 | -6.19951 | -43.32645 | 2025-08-29 03:49:00 | NOAA-20 | LAGOA DO MATO | MARANHÃO | Brasil | 2105922 | 21 | 33 | nan | nan | nan | Cerrado | 1.7 |
| 555d2d80-ed53-319c-b52c-1f6fc78e4a72 | -13.53362 | -46.94316 | 2025-08-29 03:49:00 | NOAA-20 | MONTE ALEGRE DE GOIÁS | GOIÁS | Brasil | 5213509 | 52 | 33 | nan | nan | nan | Cerrado | 0.8 |
| 5d672438-6fa6-3dbd-85e8-3ef470f3f2d4 | -13.62768 | -48.20806 | 2025-08-29 03:49:00 | NOAA-20 | MINAÇU | GOIÁS | Brasil | 5213087 | 52 | 33 | nan | nan | nan | Cerrado | 3.2 |
| bf260e0e-b92e-38be-9bad-b76f6e13efcd | -12.94579 | -46.14817 | 2025-08-29 03:49:00 | NOAA-20 | CAMPOS BELOS | GOIÁS | Brasil | 5204904 | 52 | 33 | nan | nan | nan | Cerrado | 1.3 |
| 30ea4a03-4083-3e68-87fc-8e3678a8b376 | -12.84544 | -48.09818 | 2025-08-29 03:49:00 | NOAA-20 | PARANÃ | TOCANTINS | Brasil | 1716208 | 17 | 33 | nan | nan | nan | Cerrado | 4.4 |
| f661eb4a-b4dd-3267-b88c-7d58a4874c65 | -12.92531 | -46.33736 | 2025-08-29 03:49:00 | NOAA-20 | LAVANDEIRA | TOCANTINS | Brasil | 1712157 | 17 | 33 | nan | nan | nan | Cerrado | 2.1 |
| 920acc97-c9c8-34f9-a686-d1e424f42ba6 | -6.20462 | -43.00288 | 2025-08-29 03:49:00 | NOAA-20 | SÃO FRANCISCO DO MARANHÃO | MARANHÃO | Brasil | 2110906 | 21 | 33 | nan | nan | nan | Cerrado | 3.8 |
| 7fe6079f-9036-3265-a1d3-8329928957bb | -13.41158 | -46.95973 | 2025-08-29 03:49:00 | NOAA-20 | MONTE ALEGRE DE GOIÁS | GOIÁS | Brasil | 5213509 | 52 | 33 | nan | nan | nan | Cerrado | 1.6 |
| 41a041cb-0ad6-32d1-9cac-22d4545c558c | -3.42493 | -49.04959 | 2025-08-29 03:49:00 | NOAA-20 | BREU BRANCO | PARÁ | Brasil | 1501782 | 15 | 33 | nan | nan | nan | Amazônia | 10.0 |
| 79820320-66b7-3077-b16f-6cbdea219a70 | -11.56509 | -46.37881 | 2025-08-29 03:49:00 | NOAA-20 | DIANÓPOLIS | TOCANTINS | Brasil | 1707009 | 17 | 33 | nan | nan | nan | Cerrado | 1.2 |
| 6688ef6a-04f1-3ac0-9abd-c44b1cae9cd6 | -12.82711 | -48.10502 | 2025-08-29 03:49:00 | NOAA-20 | PARANÃ | TOCANTINS | Brasil | 1716208 | 17 | 33 | nan | nan | nan | Cerrado | 1.5 |
| 8588a9f2-a8de-3b74-8906-712e2fae3cd1 | -12.68599 | -48.15715 | 2025-08-29 03:49:00 | NOAA-20 | PARANÃ | TOCANTINS | Brasil | 1716208 | 17 | 33 | nan | nan | nan | Cerrado | 2.4 |
| 0ae06289-3744-33f0-ae65-d6f7de505e62 | -12.39976 | -46.49501 | 2025-08-29 03:49:00 | NOAA-20 | TAGUATINGA | TOCANTINS | Brasil | 1720903 | 17 | 33 | nan | nan | nan | Cerrado | 3.3 |
| a7b6dae8-712c-3d37-b2ca-3d09733be75a | -5.88279 | -43.19712 | 2025-08-29 03:49:00 | NOAA-20 | PARNARAMA | MARANHÃO | Brasil | 2107803 | 21 | 33 | nan | nan | nan | Caatinga | 3.1 |
| 5c6ee373-11ec-3c98-8df6-952248ba4f3e | -12.44935 | -47.99866 | 2025-08-29 03:49:00 | NOAA-20 | PARANÃ | TOCANTINS | Brasil | 1716208 | 17 | 33 | nan | nan | nan | Cerrado | 0.4 |
| e56878fa-eaf5-3f54-908e-d8c38fd62d23 | -13.54831 | -46.94777 | 2025-08-29 03:49:00 | NOAA-20 | MONTE ALEGRE DE GOIÁS | GOIÁS | Brasil | 5213509 | 52 | 33 | nan | nan | nan | Cerrado | 5.1 |
| 6fe769d3-f97e-39b0-ae85-fdad37c07569 | -12.90597 | -48.10953 | 2025-08-29 03:49:00 | NOAA-20 | PARANÃ | TOCANTINS | Brasil | 1716208 | 17 | 33 | nan | nan | nan | Cerrado | 1.2 |
| 0442effc-039b-3ac7-a467-8a700a19a925 | -13.37544 | -46.87991 | 2025-08-29 03:49:00 | NOAA-20 | MONTE ALEGRE DE GOIÁS | GOIÁS | Brasil | 5213509 | 52 | 33 | nan | nan | nan | Cerrado | 7.7 |
| 0fecf38f-9bb8-3646-b757-52257ea463e9 | -6.51615 | -43.00579 | 2025-08-29 03:49:00 | NOAA-20 | BARÃO DE GRAJAÚ | MARANHÃO | Brasil | 2101509 | 21 | 33 | nan | nan | nan | Cerrado | 1.9 |
| 969830ae-d453-3115-bd89-85c2cf6b30f5 | -15.83853 | -41.85288 | 2025-08-29 03:49:00 | NOAA-20 | CURRAL DE DENTRO | MINAS GERAIS | Brasil | 3120870 | 31 | 33 | nan | nan | nan | Cerrado | 4.4 |
| 203df6d4-75ad-3d67-a9dd-32d66efa4afe | -12.70273 | -48.15909 | 2025-08-29 03:49:00 | NOAA-20 | PARANÃ | TOCANTINS | Brasil | 1716208 | 17 | 33 | nan | nan | nan | Cerrado | 3.3 |
| 606c2410-a6cc-3727-940b-2c6912babf66 | -7.15268 | -39.42413 | 2025-08-29 03:49:00 | NOAA-20 | CRATO | CEARÁ | Brasil | 2304202 | 23 | 33 | nan | nan | nan | Caatinga | 0.9 |
| e4331cf0-d872-3f86-b86d-0d8f6c2997b6 | -15.0421 | -48.12842 | 2025-08-29 03:49:00 | NOAA-20 | MIMOSO DE GOIÁS | GOIÁS | Brasil | 5213053 | 52 | 33 | nan | nan | nan | Cerrado | 3.2 |
| 15190ed3-24fc-3e52-8e64-c245295ad179 | -12.69534 | -48.1973 | 2025-08-29 03:49:00 | NOAA-20 | PARANÃ | TOCANTINS | Brasil | 1716208 | 17 | 33 | nan | nan | nan | Cerrado | 6.6 |


[Clique aqui para ver as próximas entradas](README33.md)
