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

## Dados Diários - Página 11

| ID | Latitude | Longitude | Data/Hora GMT | Satélite | Município | Estado | País | Município ID | Estado ID | País ID | Dias sem Chuva | Precipitação | Risco de Fogo | Bioma | FRP |
|----|----------|-----------|---------------|----------|-----------|--------|------|--------------|-----------|---------|----------------|--------------|----------------|-------|-----|
| 46d38891-d4a8-3d1f-bb15-3d0214558153 | -20.83042 | -41.63468 | 2024-09-28 00:22:00 | TERRA_M-M | GUAÇUÍ | ESPÍRITO SANTO | Brasil | 3202306 | 32 | 33 | nan | nan | nan | Mata Atlântica | 10.4 |
| 75734355-ea33-3e97-87ac-d31fa2123b37 | -20.8288 | -41.62035 | 2024-09-28 00:22:00 | TERRA_M-M | ALEGRE | ESPÍRITO SANTO | Brasil | 3200201 | 32 | 33 | nan | nan | nan | Mata Atlântica | 39.2 |
| 0d397a37-6322-3ff9-a2d0-7bcb24e0a669 | -20.82383 | -41.62709 | 2024-09-28 00:22:00 | TERRA_M-M | GUAÇUÍ | ESPÍRITO SANTO | Brasil | 3202306 | 32 | 33 | nan | nan | nan | Mata Atlântica | 42.7 |
| 0807eebb-afea-3978-b108-cdb87f3bb3c8 | -20.82353 | -43.31933 | 2024-09-28 00:22:00 | TERRA_M-M | SENHORA DE OLIVEIRA | MINAS GERAIS | Brasil | 3166006 | 31 | 33 | nan | nan | nan | Mata Atlântica | 14.4 |
| 049c0b60-9015-336b-ae67-6ca073c34a79 | -20.82214 | -41.61302 | 2024-09-28 00:22:00 | TERRA_M-M | ALEGRE | ESPÍRITO SANTO | Brasil | 3200201 | 32 | 33 | nan | nan | nan | Mata Atlântica | 7.6 |
| 967fd516-d37e-3434-bb93-5f1a0957d760 | -20.70354 | -43.86718 | 2024-09-28 00:22:00 | TERRA_M-M | QUELUZITO | MINAS GERAIS | Brasil | 3153806 | 31 | 33 | nan | nan | nan | Mata Atlântica | 20.1 |
| 0a5400cb-2120-39c3-83ea-f0bc01cdc90f | -20.70142 | -43.87318 | 2024-09-28 00:22:00 | TERRA_M-M | QUELUZITO | MINAS GERAIS | Brasil | 3153806 | 31 | 33 | nan | nan | nan | Mata Atlântica | 14.7 |
| fef9c538-fad0-3b09-ade6-9ef6c3839f0b | -20.63827 | -42.26884 | 2024-09-28 00:22:00 | TERRA_M-M | FERVEDOURO | MINAS GERAIS | Brasil | 3125952 | 31 | 33 | nan | nan | nan | Mata Atlântica | 9.8 |
| dd0f9029-e41c-31d6-aa32-ae07d45a9423 | -20.62574 | -41.35065 | 2024-09-28 00:22:00 | TERRA_M-M | CACHOEIRO DE ITAPEMIRIM | ESPÍRITO SANTO | Brasil | 3201209 | 32 | 33 | nan | nan | nan | Mata Atlântica | 5.9 |
| bb4d1207-a4dc-34b2-9822-e4835196d346 | -20.62445 | -41.25005 | 2024-09-28 00:22:00 | TERRA_M-M | CASTELO | ESPÍRITO SANTO | Brasil | 3201407 | 32 | 33 | nan | nan | nan | Mata Atlântica | 12.1 |
| b09bb2d9-1482-32e8-be2e-399ae41b63d1 | -20.6229 | -41.23679 | 2024-09-28 00:22:00 | TERRA_M-M | CASTELO | ESPÍRITO SANTO | Brasil | 3201407 | 32 | 33 | nan | nan | nan | Mata Atlântica | 21.6 |
| 049c8b9b-4756-3bee-a59c-37b2510c96a2 | -20.62142 | -41.22416 | 2024-09-28 00:22:00 | TERRA_M-M | CASTELO | ESPÍRITO SANTO | Brasil | 3201407 | 32 | 33 | nan | nan | nan | Mata Atlântica | 19.0 |
| 7d3fdf9b-a805-3c24-926e-448d0e6771ec | -20.61419 | -41.25131 | 2024-09-28 00:22:00 | TERRA_M-M | CASTELO | ESPÍRITO SANTO | Brasil | 3201407 | 32 | 33 | nan | nan | nan | Mata Atlântica | 11.6 |
| 3958bc3e-2d85-3bb1-8c7c-51eaa698d954 | -20.61262 | -41.23777 | 2024-09-28 00:22:00 | TERRA_M-M | CASTELO | ESPÍRITO SANTO | Brasil | 3201407 | 32 | 33 | nan | nan | nan | Mata Atlântica | 16.6 |
| 8e49d993-80a5-32ad-95ef-31de91bc19ac | -20.59972 | -42.02064 | 2024-09-28 00:22:00 | TERRA_M-M | ESPERA FELIZ | MINAS GERAIS | Brasil | 3124203 | 31 | 33 | nan | nan | nan | Mata Atlântica | 50.1 |
| ff8e1d56-6039-32e2-9d04-2cdb063c77a5 | -20.59678 | -42.02692 | 2024-09-28 00:22:00 | TERRA_M-M | ESPERA FELIZ | MINAS GERAIS | Brasil | 3124203 | 31 | 33 | nan | nan | nan | Mata Atlântica | 31.7 |
| e1b50113-fb42-382d-8df0-addb1027d2bd | -20.5952 | -42.01339 | 2024-09-28 00:22:00 | TERRA_M-M | ESPERA FELIZ | MINAS GERAIS | Brasil | 3124203 | 31 | 33 | nan | nan | nan | Mata Atlântica | 25.8 |
| c315ee4a-8299-3139-a71a-ff327b9dbd47 | -20.59338 | -41.23352 | 2024-09-28 00:22:00 | TERRA_M-M | CASTELO | ESPÍRITO SANTO | Brasil | 3201407 | 32 | 33 | nan | nan | nan | Mata Atlântica | 6.1 |
| 926fd0c0-f1bc-3964-b8b3-71e74975109a | -20.54631 | -40.93263 | 2024-09-28 00:22:00 | TERRA_M-M | ALFREDO CHAVES | ESPÍRITO SANTO | Brasil | 3200300 | 32 | 33 | nan | nan | nan | Mata Atlântica | 5.7 |
| 84e0da3d-8ebb-3625-bf66-9758bc932655 | -20.53607 | -41.18818 | 2024-09-28 00:22:00 | TERRA_M-M | CASTELO | ESPÍRITO SANTO | Brasil | 3201407 | 32 | 33 | nan | nan | nan | Mata Atlântica | 10.9 |
| 43842d88-3bd5-3541-9f29-33fe6e631f3a | -20.43759 | -42.00843 | 2024-09-28 00:22:00 | TERRA_M-M | ALTO JEQUITIBÁ | MINAS GERAIS | Brasil | 3153509 | 31 | 33 | nan | nan | nan | Mata Atlântica | 22.7 |
| e308f761-9c51-34c6-84ec-018d0bbb8e72 | -20.29027 | -41.43064 | 2024-09-28 00:22:00 | TERRA_M-M | MUNIZ FREIRE | ESPÍRITO SANTO | Brasil | 3203700 | 32 | 33 | nan | nan | nan | Mata Atlântica | 7.1 |
| ba278c92-b1c6-345f-8d94-bde03152f350 | -20.26495 | -41.30407 | 2024-09-28 00:22:00 | TERRA_M-M | BREJETUBA | ESPÍRITO SANTO | Brasil | 3201159 | 32 | 33 | nan | nan | nan | Mata Atlântica | 11.5 |
| 34283253-7d01-3373-9bbf-9fe460671cc8 | -10.57391 | -46.0542 | 2024-09-28 00:24:00 | TERRA_M-M | MATEIROS | TOCANTINS | Brasil | 1712702 | 17 | 33 | nan | nan | nan | Cerrado | 88.0 |
| acf0d103-c711-3aa7-8288-d4a8cb50d916 | -10.57147 | -46.03481 | 2024-09-28 00:24:00 | TERRA_M-M | MATEIROS | TOCANTINS | Brasil | 1712702 | 17 | 33 | nan | nan | nan | Cerrado | 50.5 |
| 1475b330-ab0d-3f9c-a1b8-86843a1330ac | -10.56172 | -46.05044 | 2024-09-28 00:24:00 | TERRA_M-M | MATEIROS | TOCANTINS | Brasil | 1712702 | 17 | 33 | nan | nan | nan | Cerrado | 42.0 |
| e45bf092-745f-347c-ad0a-4d948fa6c56a | -10.56127 | -46.05604 | 2024-09-28 00:24:00 | TERRA_M-M | MATEIROS | TOCANTINS | Brasil | 1712702 | 17 | 33 | nan | nan | nan | Cerrado | 24.5 |
| d30e0cf5-80e7-3b86-8999-02a68acd5c7c | -10.55885 | -46.03655 | 2024-09-28 00:24:00 | TERRA_M-M | MATEIROS | TOCANTINS | Brasil | 1712702 | 17 | 33 | nan | nan | nan | Cerrado | 26.3 |
| 7e04d235-106b-3765-b15e-94cca32f6f1c | -20.58361 | -46.29926 | 2024-09-28 00:24:00 | TERRA_M-M | CAPITÓLIO | MINAS GERAIS | Brasil | 3112802 | 31 | 33 | nan | nan | nan | Cerrado | 20.4 |
| b5375e7e-553a-3499-b11d-4d3954e7f301 | -20.58272 | -46.29385 | 2024-09-28 00:24:00 | TERRA_M-M | CAPITÓLIO | MINAS GERAIS | Brasil | 3112802 | 31 | 33 | nan | nan | nan | Cerrado | 29.7 |
| ab416612-07c0-3263-8b5d-77427dd5b89f | -20.56858 | -46.30027 | 2024-09-28 00:24:00 | TERRA_M-M | CAPITÓLIO | MINAS GERAIS | Brasil | 3112802 | 31 | 33 | nan | nan | nan | Cerrado | 30.2 |
| bae43624-f8be-3def-b4b9-4ccf985cc6fd | -20.56587 | -46.27127 | 2024-09-28 00:24:00 | TERRA_M-M | CAPITÓLIO | MINAS GERAIS | Brasil | 3112802 | 31 | 33 | nan | nan | nan | Cerrado | 34.4 |
| 6f5cfbac-e52a-372a-875e-faf6b01d0ea6 | -20.50183 | -45.90527 | 2024-09-28 00:24:00 | TERRA_M-M | PIUMHI | MINAS GERAIS | Brasil | 3151503 | 31 | 33 | nan | nan | nan | Cerrado | 27.4 |
| e1534bfc-855e-3be8-b95d-409e41941886 | -20.49935 | -45.87877 | 2024-09-28 00:24:00 | TERRA_M-M | PIMENTA | MINAS GERAIS | Brasil | 3150505 | 31 | 33 | nan | nan | nan | Cerrado | 27.9 |
| 1d7fade6-3826-3bb8-8913-a250f1f72c67 | -20.1841 | -43.52597 | 2024-09-28 00:24:00 | TERRA_M-M | OURO PRETO | MINAS GERAIS | Brasil | 3146107 | 31 | 33 | nan | nan | nan | Mata Atlântica | 14.9 |
| 9542c895-f3ba-31b6-a2ab-e548d892fca6 | -20.12263 | -43.46355 | 2024-09-28 00:24:00 | TERRA_M-M | CATAS ALTAS | MINAS GERAIS | Brasil | 3115359 | 31 | 33 | nan | nan | nan | Mata Atlântica | 11.1 |
| df5709f0-64dd-3ad9-a2b4-8fcfcf235927 | -20.1203 | -43.44292 | 2024-09-28 00:24:00 | TERRA_M-M | CATAS ALTAS | MINAS GERAIS | Brasil | 3115359 | 31 | 33 | nan | nan | nan | Mata Atlântica | 13.4 |
| 70fb8497-4b75-30bb-b240-0a5bec148f7a | -20.11604 | -43.45674 | 2024-09-28 00:24:00 | TERRA_M-M | CATAS ALTAS | MINAS GERAIS | Brasil | 3115359 | 31 | 33 | nan | nan | nan | Mata Atlântica | 17.8 |
| 68819ec0-79aa-3a11-9f77-611ae0b4fbf9 | -19.99199 | -42.419 | 2024-09-28 00:24:00 | TERRA_M-M | RAUL SOARES | MINAS GERAIS | Brasil | 3154002 | 31 | 33 | nan | nan | nan | Mata Atlântica | 11.1 |
| 23873a02-57e5-3661-b96f-7be3abbb76ff | -19.99022 | -42.40382 | 2024-09-28 00:24:00 | TERRA_M-M | RAUL SOARES | MINAS GERAIS | Brasil | 3154002 | 31 | 33 | nan | nan | nan | Mata Atlântica | 9.7 |
| 30012091-e24e-3c5b-b069-b4ca0e1e7409 | -19.98541 | -42.14474 | 2024-09-28 00:24:00 | TERRA_M-M | SANTA BÁRBARA DO LESTE | MINAS GERAIS | Brasil | 3157252 | 31 | 33 | nan | nan | nan | Mata Atlântica | 12.3 |
| 95b13acc-8f11-3a88-9ef7-6bffb142802c | -19.98249 | -42.15064 | 2024-09-28 00:24:00 | TERRA_M-M | SANTA BÁRBARA DO LESTE | MINAS GERAIS | Brasil | 3157252 | 31 | 33 | nan | nan | nan | Mata Atlântica | 6.6 |
| b5593aae-f25e-351a-b5d4-1a66bf53f7e6 | -19.93942 | -41.79211 | 2024-09-28 00:24:00 | TERRA_M-M | CONCEIÇÃO DE IPANEMA | MINAS GERAIS | Brasil | 3117405 | 31 | 33 | nan | nan | nan | Mata Atlântica | 9.0 |
| 2e7d73b5-9783-3a54-abec-95e81982ba3a | -19.93406 | -41.78729 | 2024-09-28 00:24:00 | TERRA_M-M | CONCEIÇÃO DE IPANEMA | MINAS GERAIS | Brasil | 3117405 | 31 | 33 | nan | nan | nan | Mata Atlântica | 10.0 |
| c63a834a-eb32-3d84-b855-825f08f76d36 | -19.92689 | -42.1438 | 2024-09-28 00:24:00 | TERRA_M-M | SANTA BÁRBARA DO LESTE | MINAS GERAIS | Brasil | 3157252 | 31 | 33 | nan | nan | nan | Mata Atlântica | 18.2 |
| 8656f2e9-160f-33ea-90b8-74e9d3695487 | -19.92528 | -42.12981 | 2024-09-28 00:24:00 | TERRA_M-M | SANTA BÁRBARA DO LESTE | MINAS GERAIS | Brasil | 3157252 | 31 | 33 | nan | nan | nan | Mata Atlântica | 9.6 |
| 1841f849-b51a-3e3e-9340-8b7f14038782 | -19.9161 | -42.14514 | 2024-09-28 00:24:00 | TERRA_M-M | SANTA BÁRBARA DO LESTE | MINAS GERAIS | Brasil | 3157252 | 31 | 33 | nan | nan | nan | Mata Atlântica | 14.4 |
| 1be74b3e-2274-3e3d-ab80-b81a50262039 | -19.91451 | -42.13129 | 2024-09-28 00:24:00 | TERRA_M-M | SANTA BÁRBARA DO LESTE | MINAS GERAIS | Brasil | 3157252 | 31 | 33 | nan | nan | nan | Mata Atlântica | 9.3 |
| 4be4c56a-166d-33a4-985b-1f9a5a85ce56 | -19.88057 | -42.15577 | 2024-09-28 00:24:00 | TERRA_M-M | SANTA RITA DE MINAS | MINAS GERAIS | Brasil | 3159357 | 31 | 33 | nan | nan | nan | Mata Atlântica | 10.6 |
| 2ec5d3d1-e095-33c3-a41e-a469b182a142 | -19.87437 | -43.19345 | 2024-09-28 00:24:00 | TERRA_M-M | RIO PIRACICABA | MINAS GERAIS | Brasil | 3155702 | 31 | 33 | nan | nan | nan | Mata Atlântica | 11.1 |
| bb144c72-c34b-3d2f-b50d-d3b230ca0978 | -19.87262 | -43.17765 | 2024-09-28 00:24:00 | TERRA_M-M | RIO PIRACICABA | MINAS GERAIS | Brasil | 3155702 | 31 | 33 | nan | nan | nan | Mata Atlântica | 36.1 |
| cb9ae3a3-1725-39bf-ac01-2d05b735662e | -19.87159 | -42.17245 | 2024-09-28 00:24:00 | TERRA_M-M | CARATINGA | MINAS GERAIS | Brasil | 3113404 | 31 | 33 | nan | nan | nan | Mata Atlântica | 9.8 |
| e7f7a23f-ccbc-32a2-8143-a9512a515579 | -19.86976 | -42.15705 | 2024-09-28 00:24:00 | TERRA_M-M | CARATINGA | MINAS GERAIS | Brasil | 3113404 | 31 | 33 | nan | nan | nan | Mata Atlântica | 10.7 |
| 0363c9b4-11be-38a1-af16-b7153a20469c | -19.82211 | -42.41715 | 2024-09-28 00:24:00 | TERRA_M-M | CÓRREGO NOVO | MINAS GERAIS | Brasil | 3120003 | 31 | 33 | nan | nan | nan | Mata Atlântica | 13.7 |
| f7a2fbea-1d77-386b-9a9b-89f9ba659dc8 | -19.82045 | -42.40212 | 2024-09-28 00:24:00 | TERRA_M-M | CÓRREGO NOVO | MINAS GERAIS | Brasil | 3120003 | 31 | 33 | nan | nan | nan | Mata Atlântica | 9.9 |
| 8532f186-f0f2-3fc4-8770-7b4969aa33eb | -19.81915 | -42.40827 | 2024-09-28 00:24:00 | TERRA_M-M | CÓRREGO NOVO | MINAS GERAIS | Brasil | 3120003 | 31 | 33 | nan | nan | nan | Mata Atlântica | 16.2 |
| 33a3d99d-75f3-302e-857d-922449c7448d | -19.79204 | -41.95613 | 2024-09-28 00:24:00 | TERRA_M-M | CARATINGA | MINAS GERAIS | Brasil | 3113404 | 31 | 33 | nan | nan | nan | Mata Atlântica | 8.4 |
| adcb69a0-2028-3454-ad88-2724b01d9096 | -19.74633 | -44.28837 | 2024-09-28 00:24:00 | TERRA_M-M | ESMERALDAS | MINAS GERAIS | Brasil | 3124104 | 31 | 33 | nan | nan | nan | Cerrado | 10.8 |
| 1d7dc860-68fc-3799-9341-7b8d2ce7075b | -19.74597 | -44.29504 | 2024-09-28 00:24:00 | TERRA_M-M | ESMERALDAS | MINAS GERAIS | Brasil | 3124104 | 31 | 33 | nan | nan | nan | Cerrado | 15.6 |
| 12f30a71-7745-3694-86b3-1ee21b921ef4 | -19.64252 | -45.88887 | 2024-09-28 00:24:00 | TERRA_M-M | ESTRELA DO INDAIÁ | MINAS GERAIS | Brasil | 3124708 | 31 | 33 | nan | nan | nan | Cerrado | 35.3 |
| 276d1875-932d-3262-8f39-60e0559230fa | -19.6396 | -45.89478 | 2024-09-28 00:24:00 | TERRA_M-M | ESTRELA DO INDAIÁ | MINAS GERAIS | Brasil | 3124708 | 31 | 33 | nan | nan | nan | Cerrado | 44.6 |
| e6efeff4-c930-308a-a7ca-7da6a7fbecff | -19.62992 | -42.84502 | 2024-09-28 00:24:00 | TERRA_M-M | ANTÔNIO DIAS | MINAS GERAIS | Brasil | 3103009 | 31 | 33 | nan | nan | nan | Mata Atlântica | 12.0 |
| d658d0b0-d14b-368b-bd3c-ded4b98a1c5f | -19.61414 | -39.88485 | 2024-09-28 00:24:00 | TERRA_M-M | LINHARES | ESPÍRITO SANTO | Brasil | 3203205 | 32 | 33 | nan | nan | nan | Mata Atlântica | 7.7 |
| ac586320-4d96-3881-a002-93d483a2045b | -19.60223 | -42.80194 | 2024-09-28 00:24:00 | TERRA_M-M | ANTÔNIO DIAS | MINAS GERAIS | Brasil | 3103009 | 31 | 33 | nan | nan | nan | Mata Atlântica | 8.9 |
| 1834817a-0b89-318d-adb5-a26261025703 | -19.53612 | -42.72117 | 2024-09-28 00:24:00 | TERRA_M-M | ANTÔNIO DIAS | MINAS GERAIS | Brasil | 3103009 | 31 | 33 | nan | nan | nan | Mata Atlântica | 10.5 |
| 28f4de42-ff51-336f-99ef-52dc3257fd73 | -19.5233 | -41.55436 | 2024-09-28 00:24:00 | TERRA_M-M | POCRANE | MINAS GERAIS | Brasil | 3151909 | 31 | 33 | nan | nan | nan | Mata Atlântica | 8.2 |
| c456ec96-4c36-3790-b5a0-cddb20f12397 | -19.52111 | -42.89437 | 2024-09-28 00:24:00 | TERRA_M-M | ANTÔNIO DIAS | MINAS GERAIS | Brasil | 3103009 | 31 | 33 | nan | nan | nan | Mata Atlântica | 14.1 |
| 20e7f076-584f-3c5c-8c0e-6ded253c4b14 | -19.41017 | -42.32159 | 2024-09-28 00:24:00 | TERRA_M-M | BUGRE | MINAS GERAIS | Brasil | 3109253 | 31 | 33 | nan | nan | nan | Mata Atlântica | 9.9 |
| 5f455085-18db-3bae-ab4c-48fa3e9dcb46 | -19.40748 | -42.5897 | 2024-09-28 00:24:00 | TERRA_M-M | IPATINGA | MINAS GERAIS | Brasil | 3131307 | 31 | 33 | nan | nan | nan | Mata Atlântica | 12.3 |
| f94e590e-508c-3ee4-8903-68971d6f8f56 | -19.40583 | -42.57499 | 2024-09-28 00:24:00 | TERRA_M-M | IPATINGA | MINAS GERAIS | Brasil | 3131307 | 31 | 33 | nan | nan | nan | Mata Atlântica | 15.9 |
| 9cd0ee5f-ba0f-3e02-9d41-8b133af4b57d | -19.39627 | -42.58985 | 2024-09-28 00:24:00 | TERRA_M-M | SANTANA DO PARAÍSO | MINAS GERAIS | Brasil | 3158953 | 31 | 33 | nan | nan | nan | Mata Atlântica | 23.9 |
| c537e2df-04a2-3a36-87d2-fb369f8c25c3 | -19.39545 | -42.5963 | 2024-09-28 00:24:00 | TERRA_M-M | IPATINGA | MINAS GERAIS | Brasil | 3131307 | 31 | 33 | nan | nan | nan | Mata Atlântica | 19.7 |
| 9a6c73d9-2524-36df-b4ed-327af0e6248a | -19.39376 | -42.582 | 2024-09-28 00:24:00 | TERRA_M-M | SANTANA DO PARAÍSO | MINAS GERAIS | Brasil | 3158953 | 31 | 33 | nan | nan | nan | Mata Atlântica | 18.5 |
| e2443a56-0bf4-30a8-b45b-809be38afaa5 | -19.39324 | -43.28665 | 2024-09-28 00:24:00 | TERRA_M-M | ITAMBÉ DO MATO DENTRO | MINAS GERAIS | Brasil | 3132800 | 31 | 33 | nan | nan | nan | Mata Atlântica | 15.7 |
| 6fa3cf46-f824-3031-ab0d-7fc6c25acc67 | -19.3851 | -42.59025 | 2024-09-28 00:24:00 | TERRA_M-M | SANTANA DO PARAÍSO | MINAS GERAIS | Brasil | 3158953 | 31 | 33 | nan | nan | nan | Mata Atlântica | 31.4 |
| c41f4a57-3c39-34db-9229-b3e8d835da03 | -19.38421 | -42.59639 | 2024-09-28 00:24:00 | TERRA_M-M | IPATINGA | MINAS GERAIS | Brasil | 3131307 | 31 | 33 | nan | nan | nan | Mata Atlântica | 27.3 |
| 7eb495aa-ff7e-388a-a4c1-0b8c21040f18 | -19.38254 | -42.58214 | 2024-09-28 00:24:00 | TERRA_M-M | SANTANA DO PARAÍSO | MINAS GERAIS | Brasil | 3158953 | 31 | 33 | nan | nan | nan | Mata Atlântica | 18.9 |
| 4f2768fc-681f-39e8-9f8e-9d8795d95431 | -19.37313 | -42.59766 | 2024-09-28 00:24:00 | TERRA_M-M | SANTANA DO PARAÍSO | MINAS GERAIS | Brasil | 3158953 | 31 | 33 | nan | nan | nan | Mata Atlântica | 25.1 |
| 2d01551a-85fc-34b1-8262-b8aebcb0ef6a | -19.37144 | -42.58314 | 2024-09-28 00:24:00 | TERRA_M-M | SANTANA DO PARAÍSO | MINAS GERAIS | Brasil | 3158953 | 31 | 33 | nan | nan | nan | Mata Atlântica | 27.3 |
| a4af9f2a-4a79-3971-9518-1f2927d7b9a7 | -19.36987 | -42.56967 | 2024-09-28 00:24:00 | TERRA_M-M | SANTANA DO PARAÍSO | MINAS GERAIS | Brasil | 3158953 | 31 | 33 | nan | nan | nan | Mata Atlântica | 47.9 |
| 8f0d79bf-83e5-376b-bc25-6aa797d1e95d | -19.36215 | -42.59979 | 2024-09-28 00:24:00 | TERRA_M-M | SANTANA DO PARAÍSO | MINAS GERAIS | Brasil | 3158953 | 31 | 33 | nan | nan | nan | Mata Atlântica | 16.9 |
| 23524484-2789-332a-addf-96daf46b1138 | -19.36053 | -42.58575 | 2024-09-28 00:24:00 | TERRA_M-M | SANTANA DO PARAÍSO | MINAS GERAIS | Brasil | 3158953 | 31 | 33 | nan | nan | nan | Mata Atlântica | 15.4 |
| fab874e4-afaf-3a25-b94d-e0b7b679125c | -19.35892 | -42.5718 | 2024-09-28 00:24:00 | TERRA_M-M | SANTANA DO PARAÍSO | MINAS GERAIS | Brasil | 3158953 | 31 | 33 | nan | nan | nan | Mata Atlântica | 19.0 |
| a6527be0-0420-34af-a9d3-bbb55c90f5d4 | -19.21468 | -43.71284 | 2024-09-28 00:24:00 | TERRA_M-M | SANTANA DO RIACHO | MINAS GERAIS | Brasil | 3159001 | 31 | 33 | nan | nan | nan | Cerrado | 14.3 |
| b3265126-d7c5-3004-b8dd-99e79cf60a35 | -19.09411 | -43.4502 | 2024-09-28 00:24:00 | TERRA_M-M | CONCEIÇÃO DO MATO DENTRO | MINAS GERAIS | Brasil | 3117504 | 31 | 33 | nan | nan | nan | Mata Atlântica | 13.4 |
| 68d46c17-3108-33e8-a6a3-88278a60b4ea | -18.95135 | -41.28898 | 2024-09-28 00:24:00 | TERRA_M-M | CONSELHEIRO PENA | MINAS GERAIS | Brasil | 3118403 | 31 | 33 | nan | nan | nan | Mata Atlântica | 19.7 |
| 10d79cda-f0e3-3d4b-bc2b-5c1a86ae7c6d | -18.82906 | -46.69411 | 2024-09-28 00:24:00 | TERRA_M-M | GUIMARÂNIA | MINAS GERAIS | Brasil | 3128907 | 31 | 33 | nan | nan | nan | Cerrado | 30.0 |
| 9399466b-c7a1-311d-9e22-819552cd8ce1 | -18.69988 | -42.08997 | 2024-09-28 00:24:00 | TERRA_M-M | GOVERNADOR VALADARES | MINAS GERAIS | Brasil | 3127701 | 31 | 33 | nan | nan | nan | Mata Atlântica | 36.0 |
| ca3b8953-614a-3cfe-b927-3d839d67ef36 | -18.69835 | -42.07684 | 2024-09-28 00:24:00 | TERRA_M-M | GOVERNADOR VALADARES | MINAS GERAIS | Brasil | 3127701 | 31 | 33 | nan | nan | nan | Mata Atlântica | 18.2 |
| e89b4bd0-d041-382d-9642-52acac19c658 | -18.69506 | -42.09677 | 2024-09-28 00:24:00 | TERRA_M-M | GOVERNADOR VALADARES | MINAS GERAIS | Brasil | 3127701 | 31 | 33 | nan | nan | nan | Mata Atlântica | 17.1 |
| 0697b524-e1f2-39a8-8601-c8edb31dff47 | -18.69339 | -42.08318 | 2024-09-28 00:24:00 | TERRA_M-M | GOVERNADOR VALADARES | MINAS GERAIS | Brasil | 3127701 | 31 | 33 | nan | nan | nan | Mata Atlântica | 16.4 |
| b43c7049-5407-3038-9b2e-0df82d7ae5d4 | -18.52048 | -43.02322 | 2024-09-28 00:24:00 | TERRA_M-M | SABINÓPOLIS | MINAS GERAIS | Brasil | 3156809 | 31 | 33 | nan | nan | nan | Mata Atlântica | 10.3 |
| 9bc387cc-cb15-387e-94a4-551a43f4504d | -18.49422 | -42.21635 | 2024-09-28 00:24:00 | TERRA_M-M | NACIP RAYDAN | MINAS GERAIS | Brasil | 3144201 | 31 | 33 | nan | nan | nan | Mata Atlântica | 33.1 |
| 4b59dcb8-c7ad-3f28-b6ea-875f7c336619 | -18.49267 | -42.20338 | 2024-09-28 00:24:00 | TERRA_M-M | NACIP RAYDAN | MINAS GERAIS | Brasil | 3144201 | 31 | 33 | nan | nan | nan | Mata Atlântica | 19.6 |
| c2681e5d-0613-3051-9526-0be6ac6a471f | -18.4837 | -42.21857 | 2024-09-28 00:24:00 | TERRA_M-M | NACIP RAYDAN | MINAS GERAIS | Brasil | 3144201 | 31 | 33 | nan | nan | nan | Mata Atlântica | 21.7 |
| f89fe5f9-497b-3c5e-a66f-e84f00c753ac | -18.48209 | -42.20501 | 2024-09-28 00:24:00 | TERRA_M-M | NACIP RAYDAN | MINAS GERAIS | Brasil | 3144201 | 31 | 33 | nan | nan | nan | Mata Atlântica | 21.5 |
| b39fd32f-b9ce-3999-adfd-cf8c004e2985 | -18.48042 | -42.19097 | 2024-09-28 00:24:00 | TERRA_M-M | NACIP RAYDAN | MINAS GERAIS | Brasil | 3144201 | 31 | 33 | nan | nan | nan | Mata Atlântica | 29.8 |
| 06c8993f-ca64-32f7-a3ed-754681e8c2ec | -18.36501 | -42.76392 | 2024-09-28 00:24:00 | TERRA_M-M | SÃO JOÃO EVANGELISTA | MINAS GERAIS | Brasil | 3162807 | 31 | 33 | nan | nan | nan | Mata Atlântica | 54.4 |
| cf38792d-0d8d-36ce-9adb-ecffb485f942 | -18.36336 | -42.74974 | 2024-09-28 00:24:00 | TERRA_M-M | SÃO JOÃO EVANGELISTA | MINAS GERAIS | Brasil | 3162807 | 31 | 33 | nan | nan | nan | Mata Atlântica | 9.9 |
| 14e6ff76-31e8-338f-82cc-0d6e98181802 | -18.35401 | -42.76563 | 2024-09-28 00:24:00 | TERRA_M-M | SÃO JOÃO EVANGELISTA | MINAS GERAIS | Brasil | 3162807 | 31 | 33 | nan | nan | nan | Mata Atlântica | 7.9 |


[Clique aqui para ver as próximas entradas](README12.md)
