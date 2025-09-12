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

## Dados Diários - Página 22

| ID | Latitude | Longitude | Data/Hora GMT | Satélite | Município | Estado | País | Município ID | Estado ID | País ID | Dias sem Chuva | Precipitação | Risco de Fogo | Bioma | FRP |
|----|----------|-----------|---------------|----------|-----------|--------|------|--------------|-----------|---------|----------------|--------------|----------------|-------|-----|
| 96fb1839-4d8b-311f-a439-861f1bb98324 | -21.9679 | -47.5525 | 2025-09-12 03:40:00 | GOES-19 | DESCALVADO | SÃO PAULO | Brasil | 3513702 | 35 | 33 | nan | nan | nan | Cerrado | 65.9 |
| 4b76e7d9-c0c1-382e-9c8f-c2ad7db6dba2 | -12.9101 | -54.7558 | 2025-09-12 03:40:00 | GOES-19 | NOVA UBIRATÃ | MATO GROSSO | Brasil | 5106240 | 51 | 33 | nan | nan | nan | Amazônia | 177.5 |
| cbbc4410-65a0-3df5-badc-0da9f9a39b59 | -11.6813 | -46.6084 | 2025-09-12 03:40:00 | GOES-19 | NOVO JARDIM | TOCANTINS | Brasil | 1715259 | 17 | 33 | nan | nan | nan | Cerrado | 49.3 |
| 09629d24-d0d4-3794-859e-1e069f0852ec | -15.5427 | -48.5523 | 2025-09-12 03:40:00 | GOES-19 | PADRE BERNARDO | GOIÁS | Brasil | 5215603 | 52 | 33 | nan | nan | nan | Cerrado | 45.1 |
| edc4f48f-95c7-32c4-95ff-4ed976d581ef | -11.5425 | -50.5947 | 2025-09-12 03:40:00 | GOES-19 | LAGOA DA CONFUSÃO | TOCANTINS | Brasil | 1711902 | 17 | 33 | nan | nan | nan | Cerrado | 77.2 |
| ccdfb19f-92d2-3d80-899c-3ac958cc7400 | -21.2061 | -47.5296 | 2025-09-12 03:40:00 | GOES-19 | SERRA AZUL | SÃO PAULO | Brasil | 3551405 | 35 | 33 | nan | nan | nan | Cerrado | 143.0 |
| 81562f40-cb72-30e0-8895-2d82db86767c | -13.9177 | -48.2552 | 2025-09-12 03:40:00 | GOES-19 | COLINAS DO SUL | GOIÁS | Brasil | 5205521 | 52 | 33 | nan | nan | nan | Cerrado | 114.0 |
| 684ccfa5-ee35-3323-a2f0-a892a691c50d | -12.9294 | -54.7333 | 2025-09-12 03:40:00 | GOES-19 | NOVA UBIRATÃ | MATO GROSSO | Brasil | 5106240 | 51 | 33 | nan | nan | nan | Amazônia | 123.4 |
| 819047b7-ef59-372b-a220-86a2243e09b9 | -13.8983 | -48.2581 | 2025-09-12 03:40:00 | GOES-19 | COLINAS DO SUL | GOIÁS | Brasil | 5205521 | 52 | 33 | nan | nan | nan | Cerrado | 108.6 |
| e99ac5f7-773f-3585-8641-02a4147f3c32 | -22.83828 | -47.46292 | 2025-09-12 03:40:00 | NOAA-21 | SANTA BÁRBARA D'OESTE | SÃO PAULO | Brasil | 3545803 | 35 | 33 | nan | nan | nan | Mata Atlântica | 0.7 |
| 9e66ba94-48da-345e-a534-e3fdc09cbf21 | -17.3361 | -46.67342 | 2025-09-12 03:40:00 | NOAA-21 | PARACATU | MINAS GERAIS | Brasil | 3147006 | 31 | 33 | nan | nan | nan | Cerrado | 2.9 |
| 2f2a9fa2-303d-37ae-bf93-de8ab4cbfb15 | -18.05545 | -45.43046 | 2025-09-12 03:40:00 | NOAA-21 | SÃO GONÇALO DO ABAETÉ | MINAS GERAIS | Brasil | 3161700 | 31 | 33 | nan | nan | nan | Cerrado | 2.3 |
| f427f780-2b00-33db-96a8-d9ab4474fcf7 | -18.61441 | -48.24944 | 2025-09-12 03:40:00 | NOAA-21 | ARAGUARI | MINAS GERAIS | Brasil | 3103504 | 31 | 33 | nan | nan | nan | Mata Atlântica | 1.4 |
| 11142898-0bc0-37f1-bbea-77c34a37b865 | -16.65181 | -47.62532 | 2025-09-12 03:40:00 | NOAA-21 | CRISTALINA | GOIÁS | Brasil | 5206206 | 52 | 33 | nan | nan | nan | Cerrado | 1.9 |
| 4417984a-bd60-3eb2-af0b-b2d7c80af129 | -22.33851 | -48.81256 | 2025-09-12 03:40:00 | NOAA-21 | PEDERNEIRAS | SÃO PAULO | Brasil | 3536703 | 35 | 33 | nan | nan | nan | Cerrado | 6.7 |
| e33a7752-476d-3981-8750-277174775540 | -20.65108 | -46.53346 | 2025-09-12 03:40:00 | NOAA-21 | SÃO JOÃO BATISTA DO GLÓRIA | MINAS GERAIS | Brasil | 3162203 | 31 | 33 | nan | nan | nan | Cerrado | 0.8 |
| f9524047-985c-320b-9f44-7a4f139b7f9c | -18.05713 | -45.44794 | 2025-09-12 03:40:00 | NOAA-21 | SÃO GONÇALO DO ABAETÉ | MINAS GERAIS | Brasil | 3161700 | 31 | 33 | nan | nan | nan | Cerrado | 1.7 |
| 3a9c78f2-6736-3e2a-a845-17c24954dc48 | -18.61796 | -48.25072 | 2025-09-12 03:40:00 | NOAA-21 | ARAGUARI | MINAS GERAIS | Brasil | 3103504 | 31 | 33 | nan | nan | nan | Mata Atlântica | 1.5 |
| 42641ba6-e8eb-3132-8d5d-18883055b9b0 | -19.75711 | -46.09031 | 2025-09-12 03:40:00 | NOAA-21 | CÓRREGO DANTA | MINAS GERAIS | Brasil | 3119807 | 31 | 33 | nan | nan | nan | Cerrado | 3.0 |
| 91315f17-3f56-3515-b550-67904526e87b | -17.43686 | -49.23225 | 2025-09-12 03:40:00 | NOAA-21 | PROFESSOR JAMIL | GOIÁS | Brasil | 5218391 | 52 | 33 | nan | nan | nan | Cerrado | 2.4 |
| a87f8677-3287-39f8-a9a5-04fa94ad10f5 | -17.33415 | -46.67449 | 2025-09-12 03:40:00 | NOAA-21 | PARACATU | MINAS GERAIS | Brasil | 3147006 | 31 | 33 | nan | nan | nan | Cerrado | 2.6 |
| 11cba2fb-599d-3135-9d07-f89db7a6c0da | -16.43748 | -49.03606 | 2025-09-12 03:40:00 | NOAA-21 | TEREZÓPOLIS DE GOIÁS | GOIÁS | Brasil | 5221197 | 52 | 33 | nan | nan | nan | Cerrado | 7.6 |
| a86d3630-e760-3af0-a99d-982f00d68a56 | -19.99647 | -46.92595 | 2025-09-12 03:40:00 | NOAA-21 | TAPIRA | MINAS GERAIS | Brasil | 3168101 | 31 | 33 | nan | nan | nan | Cerrado | 2.8 |
| 116b3078-f4cd-3651-9eb3-0e6d8e9766da | -20.26374 | -42.12826 | 2025-09-12 03:40:00 | NOAA-21 | MANHUAÇU | MINAS GERAIS | Brasil | 3139409 | 31 | 33 | nan | nan | nan | Mata Atlântica | 10.6 |
| d63128a1-9666-338a-8fd0-2a3efcbd9d75 | -21.9454 | -47.54984 | 2025-09-12 03:40:00 | NOAA-21 | DESCALVADO | SÃO PAULO | Brasil | 3513702 | 35 | 33 | nan | nan | nan | Cerrado | 2.0 |
| 12b713d0-3227-3350-a05b-34049a426813 | -20.66609 | -44.26101 | 2025-09-12 03:40:00 | NOAA-21 | DESTERRO DE ENTRE RIOS | MINAS GERAIS | Brasil | 3121407 | 31 | 33 | nan | nan | nan | Mata Atlântica | 6.4 |
| e3afa398-280f-3ca7-91ed-e8a45d2fb2f1 | -18.08854 | -45.42408 | 2025-09-12 03:40:00 | NOAA-21 | SÃO GONÇALO DO ABAETÉ | MINAS GERAIS | Brasil | 3161700 | 31 | 33 | nan | nan | nan | Cerrado | 0.6 |
| 5dc8f84c-31d6-323f-9dff-e82456f7ffaf | -19.23867 | -48.03553 | 2025-09-12 03:40:00 | NOAA-21 | UBERLÂNDIA | MINAS GERAIS | Brasil | 3170206 | 31 | 33 | nan | nan | nan | Cerrado | 7.6 |
| d2adeb7f-8ae3-3227-8f2a-120afd898726 | -16.42829 | -49.04663 | 2025-09-12 03:40:00 | NOAA-21 | TEREZÓPOLIS DE GOIÁS | GOIÁS | Brasil | 5221197 | 52 | 33 | nan | nan | nan | Cerrado | 8.0 |
| e70ba298-cf0d-394c-97ab-6e420176a853 | -20.15836 | -43.68052 | 2025-09-12 03:40:00 | NOAA-21 | ITABIRITO | MINAS GERAIS | Brasil | 3131901 | 31 | 33 | nan | nan | nan | Mata Atlântica | 3.7 |
| 9012bf05-0278-3ebd-96b3-c3155881f75c | -17.91498 | -45.71173 | 2025-09-12 03:40:00 | NOAA-21 | JOÃO PINHEIRO | MINAS GERAIS | Brasil | 3136306 | 31 | 33 | nan | nan | nan | Cerrado | 4.2 |
| 9ed97d45-ea8b-385a-b8ce-b1f2e489cfda | -17.90717 | -44.60512 | 2025-09-12 03:40:00 | NOAA-21 | LASSANCE | MINAS GERAIS | Brasil | 3138104 | 31 | 33 | nan | nan | nan | Cerrado | 2.9 |
| 07acae0e-f354-324b-9769-98a19f1e6874 | -20.00892 | -47.65071 | 2025-09-12 03:40:00 | NOAA-21 | CONQUISTA | MINAS GERAIS | Brasil | 3118205 | 31 | 33 | nan | nan | nan | Cerrado | 1.3 |
| f2aa291f-ff7f-3830-b1eb-3cf8fd06a6ab | -19.95537 | -44.46074 | 2025-09-12 03:40:00 | NOAA-21 | MATEUS LEME | MINAS GERAIS | Brasil | 3140704 | 31 | 33 | nan | nan | nan | Mata Atlântica | 4.4 |
| 848af02a-442c-3f35-9f85-253c1611cb68 | -21.19305 | -47.52322 | 2025-09-12 03:40:00 | NOAA-21 | ALTINÓPOLIS | SÃO PAULO | Brasil | 3501004 | 35 | 33 | nan | nan | nan | Cerrado | 41.3 |
| d33180b5-3f5d-3a19-9a08-f287ed448136 | -21.13046 | -44.45358 | 2025-09-12 03:40:00 | NOAA-21 | CONCEIÇÃO DA BARRA DE MINAS | MINAS GERAIS | Brasil | 3115201 | 31 | 33 | nan | nan | nan | Mata Atlântica | 2.1 |
| f7e09f4c-81c8-3c53-8b0d-32a918a6e1d7 | -22.68679 | -45.52679 | 2025-09-12 03:40:00 | NOAA-21 | CAMPOS DO JORDÃO | SÃO PAULO | Brasil | 3509700 | 35 | 33 | nan | nan | nan | Mata Atlântica | 1.2 |
| ece22252-736c-3890-8d70-dab33df8b8d7 | -17.91563 | -45.70858 | 2025-09-12 03:40:00 | NOAA-21 | JOÃO PINHEIRO | MINAS GERAIS | Brasil | 3136306 | 31 | 33 | nan | nan | nan | Cerrado | 4.2 |
| 667fbb3e-1519-32db-9708-db04a0d5d070 | -22.22836 | -49.60318 | 2025-09-12 03:40:00 | NOAA-21 | GARÇA | SÃO PAULO | Brasil | 3516705 | 35 | 33 | nan | nan | nan | Mata Atlântica | 3.9 |
| e64e599f-03a4-32ce-8cdf-f8dd5896f3b0 | -21.19391 | -47.51939 | 2025-09-12 03:40:00 | NOAA-21 | ALTINÓPOLIS | SÃO PAULO | Brasil | 3501004 | 35 | 33 | nan | nan | nan | Cerrado | 41.3 |
| 98e0d849-a47d-3304-a6f9-b1341b562949 | -18.77091 | -48.54284 | 2025-09-12 03:40:00 | NOAA-21 | TUPACIGUARA | MINAS GERAIS | Brasil | 3169604 | 31 | 33 | nan | nan | nan | Cerrado | 4.0 |
| 8bf299c2-f776-38b6-8254-eff5417df620 | -17.77366 | -43.45396 | 2025-09-12 03:40:00 | NOAA-21 | DIAMANTINA | MINAS GERAIS | Brasil | 3121605 | 31 | 33 | nan | nan | nan | Cerrado | 0.9 |
| 7c6841c5-dcaf-38d8-b54b-c273213433e8 | -21.36928 | -45.16784 | 2025-09-12 03:40:00 | NOAA-21 | CARMO DA CACHOEIRA | MINAS GERAIS | Brasil | 3113909 | 31 | 33 | nan | nan | nan | Mata Atlântica | 7.4 |
| a7e9ffd0-3785-34d6-8145-5f2a5dee5f7f | -15.5297 | -48.55124 | 2025-09-12 03:40:00 | NOAA-21 | PADRE BERNARDO | GOIÁS | Brasil | 5215603 | 52 | 33 | nan | nan | nan | Cerrado | 3.6 |
| 5a817902-06b4-35d1-9e69-1f82e1ac2bde | -22.18499 | -49.59849 | 2025-09-12 03:40:00 | NOAA-21 | GARÇA | SÃO PAULO | Brasil | 3516705 | 35 | 33 | nan | nan | nan | Mata Atlântica | 2.0 |
| f2a262f4-54b2-3867-bd01-64f0366ae281 | -22.69541 | -46.21795 | 2025-09-12 03:40:00 | NOAA-21 | ITAPEVA | MINAS GERAIS | Brasil | 3133600 | 31 | 33 | nan | nan | nan | Mata Atlântica | 4.4 |
| 59b5a1aa-a2ba-386b-8ad7-7f2a805d201b | -17.82145 | -46.7316 | 2025-09-12 03:40:00 | NOAA-21 | VAZANTE | MINAS GERAIS | Brasil | 3171006 | 31 | 33 | nan | nan | nan | Cerrado | 2.7 |
| 65724e19-e7ca-3fa5-8017-a6704aa4e283 | -17.94178 | -46.92549 | 2025-09-12 03:40:00 | NOAA-21 | VAZANTE | MINAS GERAIS | Brasil | 3171006 | 31 | 33 | nan | nan | nan | Cerrado | 2.0 |
| 2d062a4b-815d-347d-99a8-9cd199493540 | -21.19218 | -47.52708 | 2025-09-12 03:40:00 | NOAA-21 | ALTINÓPOLIS | SÃO PAULO | Brasil | 3501004 | 35 | 33 | nan | nan | nan | Cerrado | 26.6 |
| 39e368bf-3afb-3a4a-aba6-9c8597c3bcc3 | -22.17808 | -49.73581 | 2025-09-12 03:40:00 | NOAA-21 | GARÇA | SÃO PAULO | Brasil | 3516705 | 35 | 33 | nan | nan | nan | Mata Atlântica | 6.8 |
| 64fc789e-8459-3864-8fd4-e5cadcbe101d | -17.93942 | -46.92607 | 2025-09-12 03:40:00 | NOAA-21 | VAZANTE | MINAS GERAIS | Brasil | 3171006 | 31 | 33 | nan | nan | nan | Cerrado | 2.9 |
| 71414141-ba84-33a8-bd36-e73e95e62e09 | -21.64718 | -46.40963 | 2025-09-12 03:40:00 | NOAA-21 | BOTELHOS | MINAS GERAIS | Brasil | 3108404 | 31 | 33 | nan | nan | nan | Mata Atlântica | 0.9 |
| 16de1668-c48e-3f10-b366-7e3bb7bef9fb | -22.27882 | -45.38223 | 2025-09-12 03:40:00 | NOAA-21 | MARIA DA FÉ | MINAS GERAIS | Brasil | 3139904 | 31 | 33 | nan | nan | nan | Mata Atlântica | 1.4 |
| b654b7c0-7873-3b2c-bfd2-315d1f2dba14 | -19.9767 | -47.59535 | 2025-09-12 03:40:00 | NOAA-21 | CONQUISTA | MINAS GERAIS | Brasil | 3118205 | 31 | 33 | nan | nan | nan | Cerrado | 1.0 |
| bb0ebe33-7655-37a2-820a-1ae14f74856e | -22.61071 | -47.23093 | 2025-09-12 03:40:00 | NOAA-21 | COSMÓPOLIS | SÃO PAULO | Brasil | 3512803 | 35 | 33 | nan | nan | nan | Cerrado | 1.4 |
| 8df2b342-eb9c-3552-b7b1-1f9cb9bb45f8 | -19.75201 | -46.08908 | 2025-09-12 03:40:00 | NOAA-21 | CÓRREGO DANTA | MINAS GERAIS | Brasil | 3119807 | 31 | 33 | nan | nan | nan | Cerrado | 3.0 |
| 46babfca-fbdc-3b40-a6fb-a4ae2c353fb9 | -20.006 | -46.92263 | 2025-09-12 03:40:00 | NOAA-21 | TAPIRA | MINAS GERAIS | Brasil | 3168101 | 31 | 33 | nan | nan | nan | Cerrado | 2.7 |
| f1038537-71ce-38d3-b159-07f89fecfc0b | -23.34735 | -47.14973 | 2025-09-12 03:40:00 | NOAA-21 | ITU | SÃO PAULO | Brasil | 3523909 | 35 | 33 | nan | nan | nan | Mata Atlântica | 0.6 |
| 3986690e-ce93-3950-9c40-a4f9024d3a6d | -23.38474 | -47.01397 | 2025-09-12 03:40:00 | NOAA-21 | PIRAPORA DO BOM JESUS | SÃO PAULO | Brasil | 3539103 | 35 | 33 | nan | nan | nan | Mata Atlântica | 1.0 |
| e2b92b3c-688c-3514-96fb-ba9e5b30c18c | -17.73606 | -44.42041 | 2025-09-12 03:40:00 | NOAA-21 | LASSANCE | MINAS GERAIS | Brasil | 3138104 | 31 | 33 | nan | nan | nan | Cerrado | 1.1 |
| 4deffa16-0175-39d5-a83a-3ea0d1dadb01 | -17.3631 | -46.70244 | 2025-09-12 03:40:00 | NOAA-21 | PARACATU | MINAS GERAIS | Brasil | 3147006 | 31 | 33 | nan | nan | nan | Cerrado | 1.4 |
| b5873c3a-0c87-3044-b481-63a58f0090ff | -19.75487 | -46.09112 | 2025-09-12 03:40:00 | NOAA-21 | CÓRREGO DANTA | MINAS GERAIS | Brasil | 3119807 | 31 | 33 | nan | nan | nan | Cerrado | 3.0 |
| 878f4de9-55fe-333e-ac98-a27fc5fa61dc | -18.77688 | -48.54457 | 2025-09-12 03:40:00 | NOAA-21 | TUPACIGUARA | MINAS GERAIS | Brasil | 3169604 | 31 | 33 | nan | nan | nan | Cerrado | 3.2 |
| efef6de1-54df-3563-a3cf-cf61fee15209 | -22.61146 | -47.22755 | 2025-09-12 03:40:00 | NOAA-21 | COSMÓPOLIS | SÃO PAULO | Brasil | 3512803 | 35 | 33 | nan | nan | nan | Cerrado | 1.4 |
| 26f3f73b-63ad-3a8a-b1a5-c58add6afaff | -20.23603 | -49.25294 | 2025-09-12 03:40:00 | NOAA-21 | FRONTEIRA | MINAS GERAIS | Brasil | 3127008 | 31 | 33 | nan | nan | nan | Cerrado | 40.0 |
| 81d92be1-d043-3a07-a35a-b66e3bf71a90 | -21.84903 | -46.51267 | 2025-09-12 03:40:00 | NOAA-21 | POÇOS DE CALDAS | MINAS GERAIS | Brasil | 3151800 | 31 | 33 | nan | nan | nan | Mata Atlântica | 0.8 |
| ba329d1c-2a40-305a-92ff-122010dca32f | -23.13561 | -47.15469 | 2025-09-12 03:40:00 | NOAA-21 | INDAIATUBA | SÃO PAULO | Brasil | 3520509 | 35 | 33 | nan | nan | nan | Mata Atlântica | 7.6 |
| bc6ae27c-2e11-3d95-ad4e-ccea31b67416 | -22.40248 | -46.75356 | 2025-09-12 03:40:00 | NOAA-21 | ITAPIRA | SÃO PAULO | Brasil | 3522604 | 35 | 33 | nan | nan | nan | Mata Atlântica | 11.7 |
| ac088655-25d6-3c44-828e-239259e350bc | -18.59546 | -47.18687 | 2025-09-12 03:40:00 | NOAA-21 | COROMANDEL | MINAS GERAIS | Brasil | 3119302 | 31 | 33 | nan | nan | nan | Cerrado | 8.0 |
| 6360b995-ce4a-3a2e-8630-5e6ae8108448 | -16.43471 | -49.04844 | 2025-09-12 03:40:00 | NOAA-21 | TEREZÓPOLIS DE GOIÁS | GOIÁS | Brasil | 5221197 | 52 | 33 | nan | nan | nan | Cerrado | 8.0 |
| 6ca81b13-eeb8-319f-82b6-b7175a27e978 | -19.05829 | -48.34025 | 2025-09-12 03:40:00 | NOAA-21 | UBERLÂNDIA | MINAS GERAIS | Brasil | 3170206 | 31 | 33 | nan | nan | nan | Cerrado | 3.0 |
| d932b8d2-b280-3552-b5d2-9798095e261b | -17.82065 | -46.73537 | 2025-09-12 03:40:00 | NOAA-21 | VAZANTE | MINAS GERAIS | Brasil | 3171006 | 31 | 33 | nan | nan | nan | Cerrado | 2.7 |
| a31149be-c696-3b17-9608-428b0d387eb1 | -17.47815 | -43.73522 | 2025-09-12 03:40:00 | NOAA-21 | OLHOS-D'ÁGUA | MINAS GERAIS | Brasil | 3145455 | 31 | 33 | nan | nan | nan | Cerrado | 3.1 |
| 6aff47d2-1935-37fe-9400-f93eb4e09bc7 | -23.10383 | -47.50208 | 2025-09-12 03:40:00 | NOAA-21 | PORTO FELIZ | SÃO PAULO | Brasil | 3540606 | 35 | 33 | nan | nan | nan | Mata Atlântica | 1.3 |
| bc9113f9-6a6e-392f-a943-7c4d7c66552b | -20.86852 | -46.50777 | 2025-09-12 03:40:00 | NOAA-21 | PASSOS | MINAS GERAIS | Brasil | 3147907 | 31 | 33 | nan | nan | nan | Cerrado | 1.0 |
| 714a86ad-8c1d-3cf0-8dce-80e681db9bee | -23.11215 | -47.48934 | 2025-09-12 03:40:00 | NOAA-21 | PORTO FELIZ | SÃO PAULO | Brasil | 3540606 | 35 | 33 | nan | nan | nan | Mata Atlântica | 1.6 |
| 87090720-846e-384d-bec7-66d389307071 | -21.96197 | -47.56109 | 2025-09-12 03:40:00 | NOAA-21 | DESCALVADO | SÃO PAULO | Brasil | 3513702 | 35 | 33 | nan | nan | nan | Cerrado | 5.8 |
| f984a9e1-2a5d-3a6c-9d7c-26a1da7fd153 | -21.94499 | -47.56129 | 2025-09-12 03:40:00 | NOAA-21 | DESCALVADO | SÃO PAULO | Brasil | 3513702 | 35 | 33 | nan | nan | nan | Cerrado | 9.6 |
| 50d66f8f-de7e-35dc-9bca-afb7399b24e4 | -23.43324 | -47.02621 | 2025-09-12 03:40:00 | NOAA-21 | PIRAPORA DO BOM JESUS | SÃO PAULO | Brasil | 3539103 | 35 | 33 | nan | nan | nan | Mata Atlântica | 8.3 |
| 9c4f4294-50c2-3e5e-bad6-4a123d3fafcc | -21.9504 | -47.56237 | 2025-09-12 03:40:00 | NOAA-21 | DESCALVADO | SÃO PAULO | Brasil | 3513702 | 35 | 33 | nan | nan | nan | Cerrado | 9.6 |
| 086ef6bf-8ae6-301b-9ed9-5aa4a8aa44ba | -21.95819 | -47.55281 | 2025-09-12 03:40:00 | NOAA-21 | DESCALVADO | SÃO PAULO | Brasil | 3513702 | 35 | 33 | nan | nan | nan | Cerrado | 2.2 |
| 2a5549fc-f188-3412-b748-d539d2fa5f87 | -20.57161 | -43.77999 | 2025-09-12 03:40:00 | NOAA-21 | CONSELHEIRO LAFAIETE | MINAS GERAIS | Brasil | 3118304 | 31 | 33 | nan | nan | nan | Mata Atlântica | 2.4 |
| 8ec02745-7e18-39b4-8f1a-8270b56c33dc | -19.19015 | -48.01167 | 2025-09-12 03:40:00 | NOAA-21 | UBERLÂNDIA | MINAS GERAIS | Brasil | 3170206 | 31 | 33 | nan | nan | nan | Cerrado | 19.8 |
| 1a24ce3c-a832-3c02-aa5a-bcbf15cc8935 | -15.88664 | -48.18433 | 2025-09-12 03:40:00 | NOAA-21 | BRASÍLIA | DISTRITO FEDERAL | Brasil | 5300108 | 53 | 33 | nan | nan | nan | Cerrado | 2.5 |
| 1f616a04-0a5b-3372-a679-c453504c381b | -22.79418 | -47.80664 | 2025-09-12 03:40:00 | NOAA-21 | PIRACICABA | SÃO PAULO | Brasil | 3538709 | 35 | 33 | nan | nan | nan | Cerrado | 4.9 |
| e15105fe-c196-3ac9-b95b-e35b21c2fc8d | -18.62401 | -48.2624 | 2025-09-12 03:40:00 | NOAA-21 | ARAGUARI | MINAS GERAIS | Brasil | 3103504 | 31 | 33 | nan | nan | nan | Mata Atlântica | 1.5 |
| 05fcba81-a91c-3e27-bb6b-1ba962178dd7 | -22.78124 | -47.12532 | 2025-09-12 03:40:00 | NOAA-21 | PAULÍNIA | SÃO PAULO | Brasil | 3536505 | 35 | 33 | nan | nan | nan | Cerrado | 1.3 |
| 5b2992b5-a3a4-323f-a353-655f7bfc8312 | -20.86779 | -46.51123 | 2025-09-12 03:40:00 | NOAA-21 | PASSOS | MINAS GERAIS | Brasil | 3147907 | 31 | 33 | nan | nan | nan | Cerrado | 0.7 |
| 258f5c62-b3b3-375e-beb8-667703f6d639 | -18.5384 | -48.41083 | 2025-09-12 03:40:00 | NOAA-21 | ARAGUARI | MINAS GERAIS | Brasil | 3103504 | 31 | 33 | nan | nan | nan | Mata Atlântica | 16.9 |
| 8ee9592b-46ba-3eef-8510-bb996065bb57 | -22.39745 | -46.75225 | 2025-09-12 03:40:00 | NOAA-21 | ITAPIRA | SÃO PAULO | Brasil | 3522604 | 35 | 33 | nan | nan | nan | Mata Atlântica | 11.7 |
| 71ebcec6-6f66-3d9f-9630-dc0065b630c9 | -22.33752 | -48.81681 | 2025-09-12 03:40:00 | NOAA-21 | PEDERNEIRAS | SÃO PAULO | Brasil | 3536703 | 35 | 33 | nan | nan | nan | Cerrado | 6.7 |
| 47407a18-ec8e-3a98-871f-24d8e2477bc8 | -23.25555 | -47.51017 | 2025-09-12 03:40:00 | NOAA-21 | PORTO FELIZ | SÃO PAULO | Brasil | 3540606 | 35 | 33 | nan | nan | nan | Mata Atlântica | 1.3 |
| 52eb7de2-3fb3-30fd-97b9-6f5bf69f1319 | -21.7073 | -46.25297 | 2025-09-12 03:40:00 | NOAA-21 | CAMPESTRE | MINAS GERAIS | Brasil | 3111002 | 31 | 33 | nan | nan | nan | Mata Atlântica | 1.1 |
| 3f700090-75c6-3ba0-b6c6-300a70c20c57 | -23.38854 | -47.01257 | 2025-09-12 03:40:00 | NOAA-21 | PIRAPORA DO BOM JESUS | SÃO PAULO | Brasil | 3539103 | 35 | 33 | nan | nan | nan | Mata Atlântica | 1.6 |
| 3327c08e-fc42-3a62-9b81-a0786169d5b1 | -22.82141 | -46.42922 | 2025-09-12 03:40:00 | NOAA-21 | VARGEM | SÃO PAULO | Brasil | 3556354 | 35 | 33 | nan | nan | nan | Mata Atlântica | 5.7 |
| a5f1f28e-0baa-3761-9d10-15d27bca5822 | -21.95282 | -47.55159 | 2025-09-12 03:40:00 | NOAA-21 | DESCALVADO | SÃO PAULO | Brasil | 3513702 | 35 | 33 | nan | nan | nan | Cerrado | 8.4 |
| 6b8e158c-d30a-3401-969e-0bc6d9e23797 | -21.32695 | -45.0086 | 2025-09-12 03:40:00 | NOAA-21 | LAVRAS | MINAS GERAIS | Brasil | 3138203 | 31 | 33 | nan | nan | nan | Mata Atlântica | 6.3 |
| c7920249-5053-3cd0-8b5b-4ed1e0eb8613 | -17.36012 | -46.68912 | 2025-09-12 03:40:00 | NOAA-21 | PARACATU | MINAS GERAIS | Brasil | 3147006 | 31 | 33 | nan | nan | nan | Cerrado | 1.6 |
| eb8bb719-0aff-3b8a-bbc6-fda17374da0f | -22.61034 | -47.28223 | 2025-09-12 03:40:00 | NOAA-21 | LIMEIRA | SÃO PAULO | Brasil | 3526902 | 35 | 33 | nan | nan | nan | Cerrado | 1.1 |
| d8a881a4-ce54-31e6-9812-1d4b828387af | -18.05644 | -45.45127 | 2025-09-12 03:40:00 | NOAA-21 | SÃO GONÇALO DO ABAETÉ | MINAS GERAIS | Brasil | 3161700 | 31 | 33 | nan | nan | nan | Cerrado | 1.4 |


[Clique aqui para ver as próximas entradas](README23.md)
