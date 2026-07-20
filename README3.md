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

## Dados Diários - Página 3

| ID | Latitude | Longitude | Data/Hora GMT | Satélite | Município | Estado | País | Município ID | Estado ID | País ID | Dias sem Chuva | Precipitação | Risco de Fogo | Bioma | FRP |
|----|----------|-----------|---------------|----------|-----------|--------|------|--------------|-----------|---------|----------------|--------------|----------------|-------|-----|
| 6d762b96-179f-3ea7-8d99-8babf17d4afa | -14.11801 | -46.35128 | 2026-07-20 04:02:00 | NOAA-20 | POSSE | GOIÁS | Brasil | 5218300 | 52 | 33 | nan | nan | nan | Cerrado | 0.7 |
| 459e73a1-152d-35ad-a937-bfe0731642f9 | -10.79809 | -50.23206 | 2026-07-20 04:02:00 | NOAA-20 | LAGOA DA CONFUSÃO | TOCANTINS | Brasil | 1711902 | 17 | 33 | nan | nan | nan | Cerrado | 2.1 |
| 0fac1516-cedd-3c25-9120-6477838197fc | -22.49217 | -43.49767 | 2026-07-20 04:04:00 | NOAA-20 | MIGUEL PEREIRA | RIO DE JANEIRO | Brasil | 3302908 | 33 | 33 | nan | nan | nan | Mata Atlântica | 0.5 |
| 51b915a0-8dc2-3466-bad9-609cedb12230 | -21.41074 | -44.256 | 2026-07-20 04:04:00 | NOAA-20 | MADRE DE DEUS DE MINAS | MINAS GERAIS | Brasil | 3139102 | 31 | 33 | nan | nan | nan | Mata Atlântica | 0.7 |
| fd069f3c-a826-3240-bb65-3057585878ac | -22.69239 | -48.68665 | 2026-07-20 04:04:00 | NOAA-20 | AREIÓPOLIS | SÃO PAULO | Brasil | 3503604 | 35 | 33 | nan | nan | nan | Cerrado | 3.0 |
| e17cb2a3-8c79-3663-bd2a-3996346ab1ec | -23.0579 | -46.88842 | 2026-07-20 04:04:00 | NOAA-20 | ITATIBA | SÃO PAULO | Brasil | 3523404 | 35 | 33 | nan | nan | nan | Mata Atlântica | 4.6 |
| 14bb0acf-588a-316a-be3a-15c94c57905e | -22.90958 | -43.4692 | 2026-07-20 04:04:00 | NOAA-20 | RIO DE JANEIRO | RIO DE JANEIRO | Brasil | 3304557 | 33 | 33 | nan | nan | nan | Mata Atlântica | 0.8 |
| 87c1e869-3ae6-3b3b-9015-c8a21fd9fd52 | -18.35594 | -49.90471 | 2026-07-20 04:04:00 | NOAA-20 | ITUMBIARA | GOIÁS | Brasil | 5211503 | 52 | 33 | nan | nan | nan | Cerrado | 1.3 |
| 858a4398-15e0-3215-8e3c-7a526a7f0066 | -21.45843 | -43.60205 | 2026-07-20 04:04:00 | NOAA-20 | SANTOS DUMONT | MINAS GERAIS | Brasil | 3160702 | 31 | 33 | nan | nan | nan | Mata Atlântica | 1.0 |
| 52af52c9-18c3-3b8f-9f77-63bebcbbe40f | -22.89179 | -42.95288 | 2026-07-20 04:04:00 | NOAA-20 | SÃO GONÇALO | RIO DE JANEIRO | Brasil | 3304904 | 33 | 33 | nan | nan | nan | Mata Atlântica | 1.5 |
| dfea9e8f-b980-3a12-af6a-36d254f3c24c | -22.38062 | -45.35791 | 2026-07-20 04:04:00 | NOAA-20 | ITAJUBÁ | MINAS GERAIS | Brasil | 3132404 | 31 | 33 | nan | nan | nan | Mata Atlântica | 1.0 |
| e7c5d59e-bb78-3cc5-8aae-55a8dce60fe3 | -21.01565 | -43.35419 | 2026-07-20 04:04:00 | NOAA-20 | ALTO RIO DOCE | MINAS GERAIS | Brasil | 3102100 | 31 | 33 | nan | nan | nan | Mata Atlântica | 0.6 |
| 66f8c713-35d4-3531-a0cf-26b074455fe0 | -22.67344 | -43.47674 | 2026-07-20 04:04:00 | NOAA-20 | NOVA IGUAÇU | RIO DE JANEIRO | Brasil | 3303500 | 33 | 33 | nan | nan | nan | Mata Atlântica | 0.4 |
| 13fb35ae-dbf6-3b58-8947-06d8917e9a96 | -20.50036 | -42.37115 | 2026-07-20 04:04:00 | NOAA-20 | PEDRA BONITA | MINAS GERAIS | Brasil | 3148756 | 31 | 33 | nan | nan | nan | Mata Atlântica | 2.3 |
| df303037-548c-39db-a44e-a9265bad9c74 | -19.93089 | -44.07108 | 2026-07-20 04:04:00 | NOAA-20 | CONTAGEM | MINAS GERAIS | Brasil | 3118601 | 31 | 33 | nan | nan | nan | Mata Atlântica | 1.2 |
| d42d1e94-3786-3377-93a1-3c46da58b422 | -23.40571 | -46.42423 | 2026-07-20 04:04:00 | NOAA-20 | GUARULHOS | SÃO PAULO | Brasil | 3518800 | 35 | 33 | nan | nan | nan | Mata Atlântica | 0.4 |
| bb99ccea-fb14-3883-a814-4b4b7e5a1aaa | -20.96403 | -40.97607 | 2026-07-20 04:04:00 | NOAA-20 | ITAPEMIRIM | ESPÍRITO SANTO | Brasil | 3202801 | 32 | 33 | nan | nan | nan | Mata Atlântica | 3.8 |
| 62626332-fd91-3212-8b53-702388fc307a | -22.69154 | -48.69093 | 2026-07-20 04:04:00 | NOAA-20 | LENÇÓIS PAULISTA | SÃO PAULO | Brasil | 3526803 | 35 | 33 | nan | nan | nan | Cerrado | 2.4 |
| 28302d47-df0e-3bf8-88ec-093131d42d8e | -21.22779 | -45.01491 | 2026-07-20 04:04:00 | NOAA-20 | LAVRAS | MINAS GERAIS | Brasil | 3138203 | 31 | 33 | nan | nan | nan | Mata Atlântica | 1.0 |
| 2b7ad1be-d672-3cec-8abe-df04a6c702f7 | -21.62385 | -41.23373 | 2026-07-20 04:04:00 | NOAA-20 | CAMPOS DOS GOYTACAZES | RIO DE JANEIRO | Brasil | 3301009 | 33 | 33 | nan | nan | nan | Mata Atlântica | 0.7 |
| ebd4945a-9d2f-3330-899c-017a04563b9b | -21.61 | -46.61433 | 2026-07-20 04:04:00 | NOAA-20 | CACONDE | SÃO PAULO | Brasil | 3508702 | 35 | 33 | nan | nan | nan | Mata Atlântica | 3.8 |
| 8ff5afe3-1c56-3548-a26b-e429dcc58bcf | -21.46181 | -43.60265 | 2026-07-20 04:04:00 | NOAA-20 | SANTOS DUMONT | MINAS GERAIS | Brasil | 3160702 | 31 | 33 | nan | nan | nan | Mata Atlântica | 0.7 |
| d1abe448-af90-3d94-b3c3-d1abf143669d | -20.96012 | -40.97923 | 2026-07-20 04:04:00 | NOAA-20 | ITAPEMIRIM | ESPÍRITO SANTO | Brasil | 3202801 | 32 | 33 | nan | nan | nan | Mata Atlântica | 2.2 |
| 58375f0d-960e-3832-b00c-8ceb3a68bb3b | -22.57804 | -42.06267 | 2026-07-20 04:04:00 | NOAA-20 | CABO FRIO | RIO DE JANEIRO | Brasil | 3300704 | 33 | 33 | nan | nan | nan | Mata Atlântica | 1.9 |
| baafcf44-3285-3edd-af64-872cdb1285d8 | -22.66718 | -43.66107 | 2026-07-20 04:04:00 | NOAA-20 | SEROPÉDICA | RIO DE JANEIRO | Brasil | 3305554 | 33 | 33 | nan | nan | nan | Mata Atlântica | 1.1 |
| bd628267-fab6-39ef-9918-df84eeaea0ee | -22.90257 | -43.32347 | 2026-07-20 04:04:00 | NOAA-20 | RIO DE JANEIRO | RIO DE JANEIRO | Brasil | 3304557 | 33 | 33 | nan | nan | nan | Mata Atlântica | 0.5 |
| 8ccc6cce-b45f-3fd5-b209-72a9846bf245 | -21.87073 | -49.24762 | 2026-07-20 04:04:00 | NOAA-20 | PIRAJUÍ | SÃO PAULO | Brasil | 3538907 | 35 | 33 | nan | nan | nan | Mata Atlântica | 1.0 |
| 8f944e0d-f8aa-398d-8e26-07d4be1537fc | -22.74723 | -46.60643 | 2026-07-20 04:04:00 | NOAA-20 | PINHALZINHO | SÃO PAULO | Brasil | 3538204 | 35 | 33 | nan | nan | nan | Mata Atlântica | 1.4 |
| 3eb3e5bc-9f07-3fe8-bca8-e870dbe736e5 | -21.60734 | -46.61737 | 2026-07-20 04:04:00 | NOAA-20 | CACONDE | SÃO PAULO | Brasil | 3508702 | 35 | 33 | nan | nan | nan | Mata Atlântica | 4.1 |
| 5fa594f2-84cf-3bb8-917b-c97e452a896c | -23.33117 | -45.69888 | 2026-07-20 04:04:00 | NOAA-20 | PARAIBUNA | SÃO PAULO | Brasil | 3535606 | 35 | 33 | nan | nan | nan | Mata Atlântica | 1.1 |
| e9e01a65-b345-37de-bd01-54e146933b54 | -22.90195 | -43.32722 | 2026-07-20 04:04:00 | NOAA-20 | RIO DE JANEIRO | RIO DE JANEIRO | Brasil | 3304557 | 33 | 33 | nan | nan | nan | Mata Atlântica | 1.2 |
| 1755035a-9d5f-372b-863f-040e2521f1b0 | -21.53901 | -41.23455 | 2026-07-20 04:04:00 | NOAA-20 | SÃO FRANCISCO DE ITABAPOANA | RIO DE JANEIRO | Brasil | 3304755 | 33 | 33 | nan | nan | nan | Mata Atlântica | 0.4 |
| 467371ac-c259-3712-abd1-6f09bfef6f74 | -21.60829 | -46.61212 | 2026-07-20 04:04:00 | NOAA-20 | CACONDE | SÃO PAULO | Brasil | 3508702 | 35 | 33 | nan | nan | nan | Mata Atlântica | 4.1 |
| 960fe057-7a5b-38bf-8e09-4b68a8efd51f | -19.77171 | -44.29927 | 2026-07-20 04:04:00 | NOAA-20 | ESMERALDAS | MINAS GERAIS | Brasil | 3124104 | 31 | 33 | nan | nan | nan | Cerrado | 2.3 |
| 17b5980b-8e3f-32e4-b610-cd8a8cae9e9a | -19.76819 | -44.57045 | 2026-07-20 04:04:00 | NOAA-20 | SÃO JOSÉ DA VARGINHA | MINAS GERAIS | Brasil | 3163102 | 31 | 33 | nan | nan | nan | Mata Atlântica | 0.9 |
| d4bf9780-3c82-3f5e-b6d3-a3f220d0110b | -22.1047 | -44.59471 | 2026-07-20 04:04:00 | NOAA-20 | AIURUOCA | MINAS GERAIS | Brasil | 3101201 | 31 | 33 | nan | nan | nan | Mata Atlântica | 0.5 |
| be03e019-641b-37e5-85f6-e887856f542b | -22.80125 | -47.20433 | 2026-07-20 04:04:00 | NOAA-20 | SUMARÉ | SÃO PAULO | Brasil | 3552403 | 35 | 33 | nan | nan | nan | Mata Atlântica | 1.2 |
| dc131fa9-ea29-3449-aa80-45c12da84f37 | -18.85304 | -48.29233 | 2026-07-20 04:04:00 | NOAA-20 | UBERLÂNDIA | MINAS GERAIS | Brasil | 3170206 | 31 | 33 | nan | nan | nan | Cerrado | 2.6 |
| b49397c7-e829-3e34-a869-eec59b800452 | -22.38342 | -45.36278 | 2026-07-20 04:04:00 | NOAA-20 | ITAJUBÁ | MINAS GERAIS | Brasil | 3132404 | 31 | 33 | nan | nan | nan | Mata Atlântica | 1.0 |
| e1b08f7c-9951-37a9-9b81-2f51b8d17d6d | -23.33193 | -45.6946 | 2026-07-20 04:04:00 | NOAA-20 | PARAIBUNA | SÃO PAULO | Brasil | 3535606 | 35 | 33 | nan | nan | nan | Mata Atlântica | 1.1 |
| bf00a57a-63cf-361e-a062-7386448c30d1 | -21.86912 | -49.24518 | 2026-07-20 04:04:00 | NOAA-20 | PIRAJUÍ | SÃO PAULO | Brasil | 3538907 | 35 | 33 | nan | nan | nan | Mata Atlântica | 2.3 |
| 9b16fd66-98dc-38cf-9938-7285d5d71a29 | -20.88523 | -42.91068 | 2026-07-20 04:04:00 | NOAA-20 | SÃO GERALDO | MINAS GERAIS | Brasil | 3161502 | 31 | 33 | nan | nan | nan | Mata Atlântica | 0.6 |
| 7b829462-cf07-304b-b96a-6cd637e3771e | -22.72792 | -43.76355 | 2026-07-20 04:04:00 | NOAA-20 | ITAGUAÍ | RIO DE JANEIRO | Brasil | 3302007 | 33 | 33 | nan | nan | nan | Mata Atlântica | 0.7 |
| f3e055a5-422b-3084-8961-6f5a6b7a85b4 | -23.35741 | -46.97576 | 2026-07-20 04:04:00 | NOAA-20 | PIRAPORA DO BOM JESUS | SÃO PAULO | Brasil | 3539103 | 35 | 33 | nan | nan | nan | Mata Atlântica | 0.9 |
| ed613e82-8ace-3795-b189-c70fd5e82c85 | -20.28682 | -46.41841 | 2026-07-20 04:04:00 | NOAA-20 | SÃO ROQUE DE MINAS | MINAS GERAIS | Brasil | 3164308 | 31 | 33 | nan | nan | nan | Cerrado | 2.2 |
| f794ec63-1aa7-3510-ae0d-4d3bef41aa50 | -21.39646 | -45.5106 | 2026-07-20 04:04:00 | NOAA-20 | TRÊS PONTAS | MINAS GERAIS | Brasil | 3169406 | 31 | 33 | nan | nan | nan | Mata Atlântica | 1.0 |
| d68cfbfe-2de9-3b2e-8a0c-accb33b0ccfa | -22.52206 | -43.5671 | 2026-07-20 04:04:00 | NOAA-20 | MIGUEL PEREIRA | RIO DE JANEIRO | Brasil | 3302908 | 33 | 33 | nan | nan | nan | Mata Atlântica | 0.4 |
| fe203821-1d88-3e0a-b10a-862a62b4b5f0 | -21.13283 | -47.45797 | 2026-07-20 04:04:00 | NOAA-20 | ALTINÓPOLIS | SÃO PAULO | Brasil | 3501004 | 35 | 33 | nan | nan | nan | Cerrado | 5.5 |
| 5f587386-c8db-37d0-b51b-78ce87f9f150 | -20.76726 | -48.56886 | 2026-07-20 04:04:00 | NOAA-20 | COLINA | SÃO PAULO | Brasil | 3512001 | 35 | 33 | nan | nan | nan | Cerrado | 1.4 |
| 8fcee627-aed2-306f-93f2-4819c66be424 | -21.10246 | -45.80066 | 2026-07-20 04:04:00 | NOAA-20 | CAMPO DO MEIO | MINAS GERAIS | Brasil | 3111309 | 31 | 33 | nan | nan | nan | Mata Atlântica | 1.1 |
| 05561f3b-dabe-36af-b6fa-b93e442b3364 | -22.91575 | -43.43178 | 2026-07-20 04:04:00 | NOAA-20 | RIO DE JANEIRO | RIO DE JANEIRO | Brasil | 3304557 | 33 | 33 | nan | nan | nan | Mata Atlântica | 0.3 |
| 2d05a2fc-5e8c-3c0d-abbb-8a7f5723b837 | -21.13208 | -47.46183 | 2026-07-20 04:04:00 | NOAA-20 | ALTINÓPOLIS | SÃO PAULO | Brasil | 3501004 | 35 | 33 | nan | nan | nan | Cerrado | 5.5 |
| 6ecfe8e8-e6b1-3eeb-bfb4-629363996946 | -23.30151 | -46.17392 | 2026-07-20 04:04:00 | NOAA-20 | SANTA ISABEL | SÃO PAULO | Brasil | 3546801 | 35 | 33 | nan | nan | nan | Mata Atlântica | 1.8 |
| 60e5df37-9d35-37ac-b7e0-c933350279d7 | -21.86628 | -49.24664 | 2026-07-20 04:04:00 | NOAA-20 | PIRAJUÍ | SÃO PAULO | Brasil | 3538907 | 35 | 33 | nan | nan | nan | Mata Atlântica | 1.0 |
| 7c0abcea-322e-338d-83d2-d46015e4ac41 | -21.61098 | -46.60911 | 2026-07-20 04:04:00 | NOAA-20 | CACONDE | SÃO PAULO | Brasil | 3508702 | 35 | 33 | nan | nan | nan | Mata Atlântica | 3.8 |
| 13bc2b76-863c-3db5-b155-739fe1bcba57 | -24.06598 | -48.92786 | 2026-07-20 04:04:00 | NOAA-20 | ITAPEVA | SÃO PAULO | Brasil | 3522406 | 35 | 33 | nan | nan | nan | Cerrado | 0.9 |
| 466baf78-ad8c-3072-ae47-2c71bf6efc0d | -21.10435 | -45.79953 | 2026-07-20 04:04:00 | NOAA-20 | CAMPO DO MEIO | MINAS GERAIS | Brasil | 3111309 | 31 | 33 | nan | nan | nan | Mata Atlântica | 1.1 |
| aae370b7-12f5-3afa-be0b-5b0194536df1 | -22.48885 | -43.49691 | 2026-07-20 04:04:00 | NOAA-20 | MIGUEL PEREIRA | RIO DE JANEIRO | Brasil | 3302908 | 33 | 33 | nan | nan | nan | Mata Atlântica | 0.4 |
| ed88a11a-01c8-3965-8222-0c78adbb0fcf | -20.00292 | -48.90977 | 2026-07-20 04:04:00 | NOAA-20 | FRUTAL | MINAS GERAIS | Brasil | 3127107 | 31 | 33 | nan | nan | nan | Cerrado | 0.8 |
| 0509dd69-d783-325f-9899-0343d36554e5 | -22.38063 | -45.36398 | 2026-07-20 04:04:00 | NOAA-20 | ITAJUBÁ | MINAS GERAIS | Brasil | 3132404 | 31 | 33 | nan | nan | nan | Mata Atlântica | 1.7 |
| eed5545b-6ff0-3f89-87ba-ceb095b0e734 | -21.60715 | -46.60842 | 2026-07-20 04:04:00 | NOAA-20 | CACONDE | SÃO PAULO | Brasil | 3508702 | 35 | 33 | nan | nan | nan | Mata Atlântica | 5.5 |
| ec4d70f8-3244-3886-8d9f-e150c90fd877 | -20.96069 | -40.97549 | 2026-07-20 04:04:00 | NOAA-20 | ITAPEMIRIM | ESPÍRITO SANTO | Brasil | 3202801 | 32 | 33 | nan | nan | nan | Mata Atlântica | 2.2 |
| 17897745-b5c5-33b7-bc92-c0600318c5ce | -21.40731 | -44.25532 | 2026-07-20 04:04:00 | NOAA-20 | MADRE DE DEUS DE MINAS | MINAS GERAIS | Brasil | 3139102 | 31 | 33 | nan | nan | nan | Mata Atlântica | 4.0 |
| 3846373c-d61e-3ecb-ba9e-b0a1ae00af8a | -22.90622 | -43.46875 | 2026-07-20 04:04:00 | NOAA-20 | RIO DE JANEIRO | RIO DE JANEIRO | Brasil | 3304557 | 33 | 33 | nan | nan | nan | Mata Atlântica | 0.8 |
| eff4e590-e363-3e5f-8043-f404ab20786e | -20.28207 | -46.42245 | 2026-07-20 04:04:00 | NOAA-20 | SÃO ROQUE DE MINAS | MINAS GERAIS | Brasil | 3164308 | 31 | 33 | nan | nan | nan | Cerrado | 2.0 |
| 8271d4a5-6fbf-365c-8308-753e937613b1 | -22.23917 | -49.91784 | 2026-07-20 04:04:00 | NOAA-20 | MARÍLIA | SÃO PAULO | Brasil | 3529005 | 35 | 33 | nan | nan | nan | Mata Atlântica | 0.8 |
| 77e780e9-8789-39c4-b74c-b781e997549d | -21.61116 | -46.6181 | 2026-07-20 04:04:00 | NOAA-20 | CACONDE | SÃO PAULO | Brasil | 3508702 | 35 | 33 | nan | nan | nan | Mata Atlântica | 5.8 |
| 803c2489-38f1-3a33-a289-d649dcb3b471 | -26.34884 | -48.81863 | 2026-07-20 04:06:00 | NOAA-20 | JOINVILLE | SANTA CATARINA | Brasil | 4209102 | 42 | 33 | nan | nan | nan | Mata Atlântica | 0.5 |
| 28a3fc6f-f18d-3d38-bad4-ab1ec9fec829 | -2.79617 | -49.52254 | 2026-07-20 04:44:00 | NOAA-21 | BAIÃO | PARÁ | Brasil | 1501204 | 15 | 33 | nan | nan | nan | Amazônia | 4.6 |
| ef6d4ca7-e375-3b33-82c5-bb7dc68515b2 | -2.79285 | -49.52203 | 2026-07-20 04:44:00 | NOAA-21 | BAIÃO | PARÁ | Brasil | 1501204 | 15 | 33 | nan | nan | nan | Amazônia | 4.6 |
| 0f351539-033b-3b80-a847-99c616d026f8 | -2.78544 | -49.46061 | 2026-07-20 04:44:00 | NOAA-21 | MOJU | PARÁ | Brasil | 1504703 | 15 | 33 | nan | nan | nan | Amazônia | 2.9 |
| 128844d1-d7e1-392a-a3e5-6a761d760afc | -2.8261 | -52.29741 | 2026-07-20 04:44:00 | NOAA-21 | BRASIL NOVO | PARÁ | Brasil | 1501725 | 15 | 33 | nan | nan | nan | Amazônia | 1.1 |
| a56b11a9-7952-39e2-8301-48fce15f3fef | -2.78267 | -49.45663 | 2026-07-20 04:44:00 | NOAA-21 | MOJU | PARÁ | Brasil | 1504703 | 15 | 33 | nan | nan | nan | Amazônia | 2.9 |
| e0a44e93-7fc3-38db-ad3b-72cded9e3246 | -3.84205 | -49.05183 | 2026-07-20 04:44:00 | NOAA-21 | GOIANÉSIA DO PARÁ | PARÁ | Brasil | 1503093 | 15 | 33 | nan | nan | nan | Amazônia | 1.0 |
| c352d0f4-7179-33db-9d10-db5a59726730 | -2.8333 | -48.86472 | 2026-07-20 04:44:00 | NOAA-21 | TAILÂNDIA | PARÁ | Brasil | 1507953 | 15 | 33 | nan | nan | nan | Amazônia | 2.6 |
| 95e6831b-c6d8-339d-9530-189d00aae535 | -2.7944 | -54.1559 | 2026-07-20 04:44:00 | NOAA-21 | SANTARÉM | PARÁ | Brasil | 1506807 | 15 | 33 | nan | nan | nan | Amazônia | 0.7 |
| 25bca4d1-b5e8-3d77-90c1-63f9a133b92e | -2.57713 | -49.11477 | 2026-07-20 04:44:00 | NOAA-21 | MOJU | PARÁ | Brasil | 1504703 | 15 | 33 | nan | nan | nan | Amazônia | 0.9 |
| 84218a1a-a438-3885-9a45-d0aca21c72fe | -2.82994 | -48.8642 | 2026-07-20 04:44:00 | NOAA-21 | TAILÂNDIA | PARÁ | Brasil | 1507953 | 15 | 33 | nan | nan | nan | Amazônia | 2.2 |
| 6fd09b32-8bf4-34ce-80e9-188bbe2293ae | -3.45742 | -49.38296 | 2026-07-20 04:44:00 | NOAA-21 | BREU BRANCO | PARÁ | Brasil | 1501782 | 15 | 33 | nan | nan | nan | Amazônia | 1.0 |
| aa6e34a2-6aea-3133-9f06-149e9436859c | -3.45294 | -52.73011 | 2026-07-20 04:44:00 | NOAA-21 | MEDICILÂNDIA | PARÁ | Brasil | 1504455 | 15 | 33 | nan | nan | nan | Amazônia | 0.8 |
| 646002ae-4e76-339c-90c8-1142f959ab71 | -3.26477 | -49.52833 | 2026-07-20 04:44:00 | NOAA-21 | BAIÃO | PARÁ | Brasil | 1501204 | 15 | 33 | nan | nan | nan | Amazônia | 1.4 |
| 59f1c119-7f57-34ef-b39b-96aee8d480d3 | -3.84818 | -49.03451 | 2026-07-20 04:44:00 | NOAA-21 | GOIANÉSIA DO PARÁ | PARÁ | Brasil | 1503093 | 15 | 33 | nan | nan | nan | Amazônia | 1.2 |
| 7d6d25ab-74bd-38ab-8186-56a5d210cf5a | -3.84762 | -49.03811 | 2026-07-20 04:44:00 | NOAA-21 | GOIANÉSIA DO PARÁ | PARÁ | Brasil | 1503093 | 15 | 33 | nan | nan | nan | Amazônia | 1.1 |
| e1979078-8100-36d0-8616-2f5e4c02536f | -3.97608 | -49.48132 | 2026-07-20 04:44:00 | NOAA-21 | BREU BRANCO | PARÁ | Brasil | 1501782 | 15 | 33 | nan | nan | nan | Amazônia | 0.7 |
| 31b6a2d7-fa0a-3b3a-8506-4fa482ab2a9a | -2.85327 | -48.56715 | 2026-07-20 04:44:00 | NOAA-21 | TAILÂNDIA | PARÁ | Brasil | 1507953 | 15 | 33 | nan | nan | nan | Amazônia | 1.2 |
| a8ad212f-eeb5-3448-9b2f-abd878e14864 | -2.83049 | -48.86064 | 2026-07-20 04:44:00 | NOAA-21 | TAILÂNDIA | PARÁ | Brasil | 1507953 | 15 | 33 | nan | nan | nan | Amazônia | 2.2 |
| 72621d07-7fed-30cc-94d4-077bceea3e2d | -3.26423 | -49.53179 | 2026-07-20 04:44:00 | NOAA-21 | BAIÃO | PARÁ | Brasil | 1501204 | 15 | 33 | nan | nan | nan | Amazônia | 1.3 |
| fd2a36b8-6960-3932-b3c4-e515322fdc1e | -3.41649 | -49.12143 | 2026-07-20 04:44:00 | NOAA-21 | BREU BRANCO | PARÁ | Brasil | 1501782 | 15 | 33 | nan | nan | nan | Amazônia | 2.7 |
| 9703e834-29a4-37da-82b9-a0ec1c2bf6d3 | -11.83366 | -44.77131 | 2026-07-20 04:46:00 | NOAA-21 | RIACHÃO DAS NEVES | BAHIA | Brasil | 2926202 | 29 | 33 | nan | nan | nan | Cerrado | 1.7 |
| cced2d83-bd95-3347-be65-eafbe2e6b7d2 | -10.4656 | -49.09598 | 2026-07-20 04:46:00 | NOAA-21 | PIUM | TOCANTINS | Brasil | 1717503 | 17 | 33 | nan | nan | nan | Cerrado | 3.8 |
| 7cbcba96-8016-3e6a-94fc-c01e686df9b9 | -8.93109 | -47.60037 | 2026-07-20 04:46:00 | NOAA-21 | BOM JESUS DO TOCANTINS | TOCANTINS | Brasil | 1703305 | 17 | 33 | nan | nan | nan | Cerrado | 1.4 |
| 921e2e39-9f21-3c0a-afda-66026db1e851 | -5.675 | -43.57332 | 2026-07-20 04:46:00 | NOAA-21 | PARNARAMA | MARANHÃO | Brasil | 2107803 | 21 | 33 | nan | nan | nan | Cerrado | 5.6 |
| 5399946c-1a7b-30ef-8922-bee6bffcf337 | -8.94548 | -47.60721 | 2026-07-20 04:46:00 | NOAA-21 | BOM JESUS DO TOCANTINS | TOCANTINS | Brasil | 1703305 | 17 | 33 | nan | nan | nan | Cerrado | 3.4 |
| 0e2eb0c4-cbbe-3203-b8b7-39223c839f00 | -8.93929 | -47.59689 | 2026-07-20 04:46:00 | NOAA-21 | BOM JESUS DO TOCANTINS | TOCANTINS | Brasil | 1703305 | 17 | 33 | nan | nan | nan | Cerrado | 1.4 |
| 34904f27-d3ac-38f7-9da8-be848d386bc5 | -9.10127 | -59.40317 | 2026-07-20 04:46:00 | NOAA-21 | COLNIZA | MATO GROSSO | Brasil | 5103254 | 51 | 33 | nan | nan | nan | Amazônia | 4.4 |
| c8f6bd49-5da6-3994-a61b-67d6be428c9d | -9.2849 | -50.32983 | 2026-07-20 04:46:00 | NOAA-21 | SANTANA DO ARAGUAIA | PARÁ | Brasil | 1506708 | 15 | 33 | nan | nan | nan | Amazônia | 2.3 |
| 24ff1947-ccc2-3efc-8620-6469687d827c | -6.59239 | -51.70572 | 2026-07-20 04:46:00 | NOAA-21 | SÃO FÉLIX DO XINGU | PARÁ | Brasil | 1507300 | 15 | 33 | nan | nan | nan | Amazônia | 0.8 |
| fc236feb-4e23-391d-a954-99e43c5e40fc | -11.97611 | -47.10844 | 2026-07-20 04:46:00 | NOAA-21 | TAIPAS DO TOCANTINS | TOCANTINS | Brasil | 1720937 | 17 | 33 | nan | nan | nan | Cerrado | 0.6 |
| e95d09ce-c0db-3e0d-8b64-e2c6fb5976de | -11.38304 | -47.50058 | 2026-07-20 04:46:00 | NOAA-21 | NATIVIDADE | TOCANTINS | Brasil | 1714203 | 17 | 33 | nan | nan | nan | Cerrado | 2.0 |
| c4a209d5-7fd5-3502-9342-db4ca552b220 | -10.55646 | -56.33154 | 2026-07-20 04:46:00 | NOAA-21 | ALTA FLORESTA | MATO GROSSO | Brasil | 5100250 | 51 | 33 | nan | nan | nan | Amazônia | 1.9 |


[Clique aqui para ver as próximas entradas](README4.md)
