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
| bb3821bb-cc0f-348f-ae36-2e3696e8a416 | -9.6988 | -43.464699 | 2026-09-10 00:28:00 | METOP-C | PILÃO ARCADO | BAHIA | Brasil | 2924405 | 29 | 33 | nan | nan | nan | Cerrado | nan |
| 01b58781-8a29-362f-9795-b8b9c4ee7a29 | -5.7627 | -45.098202 | 2026-09-10 00:28:00 | METOP-C | BARRA DO CORDA | MARANHÃO | Brasil | 2101608 | 21 | 33 | nan | nan | nan | Cerrado | nan |
| 09911eee-db99-38cd-ac4a-ec824800c490 | -7.4845 | -45.274399 | 2026-09-10 00:28:00 | METOP-C | LORETO | MARANHÃO | Brasil | 2106102 | 21 | 33 | nan | nan | nan | Cerrado | nan |
| 5d012030-7147-3b95-a258-ef4102d40857 | -4.3639 | -47.7771 | 2026-09-10 00:28:00 | METOP-C | DOM ELISEU | PARÁ | Brasil | 1502939 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| cb8c1e37-e182-3692-ab42-22e3efe59f1e | -7.9836 | -43.991001 | 2026-09-10 00:28:00 | METOP-C | SEBASTIÃO LEAL | PIAUÍ | Brasil | 2210631 | 22 | 33 | nan | nan | nan | Cerrado | nan |
| 8797d968-c5ba-37a5-82d2-a1c250dabd95 | -4.8668 | -47.404999 | 2026-09-10 00:28:00 | METOP-C | AÇAILÂNDIA | MARANHÃO | Brasil | 2100055 | 21 | 33 | nan | nan | nan | Amazônia | nan |
| d772472d-fbcf-3ec7-adfe-f2546b997dc9 | -10.4618 | -44.945801 | 2026-09-10 00:28:00 | METOP-C | CORRENTE | PIAUÍ | Brasil | 2202901 | 22 | 33 | nan | nan | nan | Cerrado | nan |
| 3a141a20-073e-3267-81e8-f9154f0f6e2a | -5.8041 | -43.805599 | 2026-09-10 00:28:00 | METOP-C | BURITI BRAVO | MARANHÃO | Brasil | 2102309 | 21 | 33 | nan | nan | nan | Cerrado | nan |
| 24a45091-3825-3fc3-9c71-9ddedf044920 | -12.8516 | -44.346199 | 2026-09-10 00:28:00 | METOP-C | BAIANÓPOLIS | BAHIA | Brasil | 2902500 | 29 | 33 | nan | nan | nan | Cerrado | nan |
| 27934de9-704e-3f31-8a06-7b42daea9391 | -12.8387 | -44.334499 | 2026-09-10 00:28:00 | METOP-C | BAIANÓPOLIS | BAHIA | Brasil | 2902500 | 29 | 33 | nan | nan | nan | Cerrado | nan |
| 947845a9-90af-3b6f-bb02-ae2ac6921f7e | -2.7218 | -57.6241 | 2026-09-10 00:28:00 | METOP-C | URUCURITUBA | AMAZONAS | Brasil | 1304401 | 13 | 33 | nan | nan | nan | Amazônia | nan |
| e0b945a7-50c4-38dc-876c-2b50a5103ba0 | -6.8257 | -43.053299 | 2026-09-10 00:28:00 | METOP-C | FLORIANO | PIAUÍ | Brasil | 2203909 | 22 | 33 | nan | nan | nan | Cerrado | nan |
| cfe2ecab-1ebc-31dd-8ffa-952fa2f0de4e | -10.7453 | -45.931301 | 2026-09-10 00:28:00 | METOP-C | FORMOSA DO RIO PRETO | BAHIA | Brasil | 2911105 | 29 | 33 | nan | nan | nan | Cerrado | nan |
| 9f894329-fa60-39dc-aaf3-444045aa0937 | -4.2851 | -46.5256 | 2026-09-10 00:28:00 | METOP-C | BOM JESUS DAS SELVAS | MARANHÃO | Brasil | 2102036 | 21 | 33 | nan | nan | nan | Amazônia | nan |
| 222833cd-b3a4-3465-9663-b2acdad58ebd | -7.9934 | -43.988701 | 2026-09-10 00:28:00 | METOP-C | SEBASTIÃO LEAL | PIAUÍ | Brasil | 2210631 | 22 | 33 | nan | nan | nan | Cerrado | nan |
| bff73455-9d5f-3210-a2d8-2c99a782ab45 | -9.7805 | -43.460899 | 2026-09-10 00:28:00 | METOP-C | PILÃO ARCADO | BAHIA | Brasil | 2924405 | 29 | 33 | nan | nan | nan | Cerrado | nan |
| c2cec340-6d0d-33c7-9a12-587932d9a0fb | -7.514 | -45.2677 | 2026-09-10 00:28:00 | METOP-C | LORETO | MARANHÃO | Brasil | 2106102 | 21 | 33 | nan | nan | nan | Cerrado | nan |
| d07e55d8-0a69-3f07-abc8-c589d98b1404 | -12.8402 | -44.3414 | 2026-09-10 00:28:00 | METOP-C | BAIANÓPOLIS | BAHIA | Brasil | 2902500 | 29 | 33 | nan | nan | nan | Cerrado | nan |
| 7518041f-7b4a-3213-984f-4a1b0d0a1ff6 | -7.0636 | -42.703701 | 2026-09-10 00:28:00 | METOP-C | NAZARÉ DO PIAUÍ | PIAUÍ | Brasil | 2206704 | 22 | 33 | nan | nan | nan | Caatinga | nan |
| b3dec50e-06c9-367d-876b-bf511bd837cf | -10.2638 | -45.209301 | 2026-09-10 00:28:00 | METOP-C | CORRENTE | PIAUÍ | Brasil | 2202901 | 22 | 33 | nan | nan | nan | Cerrado | nan |
| b4419bc1-a4f1-3cc6-b263-a3d3301e4068 | -14.9137 | -44.678501 | 2026-09-10 00:28:00 | METOP-C | CÔNEGO MARINHO | MINAS GERAIS | Brasil | 3117836 | 31 | 33 | nan | nan | nan | Cerrado | nan |
| c210a549-282b-30e1-b5a2-cf1061428d32 | -6.2703 | -46.369701 | 2026-09-10 00:28:00 | METOP-C | FORMOSA DA SERRA NEGRA | MARANHÃO | Brasil | 2104099 | 21 | 33 | nan | nan | nan | Cerrado | nan |
| ea250ff8-0c94-320b-b30f-a684e43f5f5b | 0.2524 | -51.4678 | 2026-09-10 00:28:00 | METOP-C | SANTANA | AMAPÁ | Brasil | 1600600 | 16 | 33 | nan | nan | nan | Amazônia | nan |
| 24bb6465-9432-34b5-98bd-2782f51b6cf8 | -12.6453 | -47.0942 | 2026-09-10 00:28:00 | METOP-C | ARRAIAS | TOCANTINS | Brasil | 1702406 | 17 | 33 | nan | nan | nan | Cerrado | nan |
| 39412449-1629-3764-b7ec-5f1fd252df4f | 1.0146 | -51.109299 | 2026-09-10 00:28:00 | METOP-C | FERREIRA GOMES | AMAPÁ | Brasil | 1600238 | 16 | 33 | nan | nan | nan | Amazônia | nan |
| b6b7ed7f-09b5-3f1d-abad-06b4cdbe252a | -7.4861 | -45.2813 | 2026-09-10 00:28:00 | METOP-C | LORETO | MARANHÃO | Brasil | 2106102 | 21 | 33 | nan | nan | nan | Cerrado | nan |
| f1362f3f-f191-33c2-a4ba-29e99cf30147 | -3.1993 | -43.917301 | 2026-09-10 00:28:00 | METOP-C | CACHOEIRA GRANDE | MARANHÃO | Brasil | 2102374 | 21 | 33 | nan | nan | nan | Cerrado | nan |
| cd21e122-ad19-3376-b4be-43c6e297abad | -5.1174 | -46.016602 | 2026-09-10 00:28:00 | METOP-C | ARAME | MARANHÃO | Brasil | 2100956 | 21 | 33 | nan | nan | nan | Amazônia | nan |
| 493a5d89-1ce8-3aad-89a2-0be9c46ebdbf | -7.9852 | -43.998199 | 2026-09-10 00:28:00 | METOP-C | SEBASTIÃO LEAL | PIAUÍ | Brasil | 2210631 | 22 | 33 | nan | nan | nan | Cerrado | nan |
| 0f648813-a768-3f45-89e5-84d00e66bf72 | -14.2034 | -41.612301 | 2026-09-10 00:28:00 | METOP-C | BRUMADO | BAHIA | Brasil | 2904605 | 29 | 33 | nan | nan | nan | Caatinga | nan |
| fef6e158-48c6-3543-a98c-c59d57daf397 | -5.7678 | -45.075199 | 2026-09-10 00:28:00 | METOP-C | BARRA DO CORDA | MARANHÃO | Brasil | 2101608 | 21 | 33 | nan | nan | nan | Cerrado | nan |
| b15d916b-7ae4-3588-bd3a-276e54dcfa7b | 0.26 | -51.479401 | 2026-09-10 00:28:00 | METOP-C | SANTANA | AMAPÁ | Brasil | 1600600 | 16 | 33 | nan | nan | nan | Amazônia | nan |
| b32450f8-3a35-38e1-b4e1-acf50a081722 | -7.483 | -45.267601 | 2026-09-10 00:28:00 | METOP-C | LORETO | MARANHÃO | Brasil | 2106102 | 21 | 33 | nan | nan | nan | Cerrado | nan |
| 43e09527-d502-3571-bb16-c5b0eed7dadf | -15.3213 | -47.244701 | 2026-09-10 00:28:00 | METOP-C | FORMOSA | GOIÁS | Brasil | 5208004 | 52 | 33 | nan | nan | nan | Cerrado | nan |
| 1b1b58ef-d295-33f1-8a62-6292256e805e | -7.0538 | -42.705898 | 2026-09-10 00:28:00 | METOP-C | NAZARÉ DO PIAUÍ | PIAUÍ | Brasil | 2206704 | 22 | 33 | nan | nan | nan | Caatinga | nan |
| e0096207-fd1f-373e-a036-d12f3db9485d | -9.171 | -45.254002 | 2026-09-10 00:28:00 | METOP-C | BAIXA GRANDE DO RIBEIRO | PIAUÍ | Brasil | 2201150 | 22 | 33 | nan | nan | nan | Cerrado | nan |
| 55dd5b2b-3e29-3e3e-8358-aaf1811df36b | -12.8371 | -44.327499 | 2026-09-10 00:28:00 | METOP-C | BAIANÓPOLIS | BAHIA | Brasil | 2902500 | 29 | 33 | nan | nan | nan | Cerrado | nan |
| 28208758-2167-341d-98da-949bb062250a | -10.692 | -46.1078 | 2026-09-10 00:28:00 | METOP-C | FORMOSA DO RIO PRETO | BAHIA | Brasil | 2911105 | 29 | 33 | nan | nan | nan | Cerrado | nan |
| 9ccbcc24-b48d-3139-a005-374cfff7249e | -7.4944 | -45.272202 | 2026-09-10 00:28:00 | METOP-C | LORETO | MARANHÃO | Brasil | 2106102 | 21 | 33 | nan | nan | nan | Cerrado | nan |
| aba566c6-cbf4-3216-9fab-58d5f06e43ad | -12.8355 | -44.320499 | 2026-09-10 00:28:00 | METOP-C | BAIANÓPOLIS | BAHIA | Brasil | 2902500 | 29 | 33 | nan | nan | nan | Cerrado | nan |
| d0932f6d-f975-3c38-9075-230e91fb2aa5 | -5.4157 | -41.8428 | 2026-09-10 00:28:00 | METOP-C | SÃO JOÃO DA SERRA | PIAUÍ | Brasil | 2209906 | 22 | 33 | nan | nan | nan | Caatinga | nan |
| 3fad1b16-2c75-3cb0-9df9-f11a7b50755b | -9.7771 | -43.4464 | 2026-09-10 00:28:00 | METOP-C | PILÃO ARCADO | BAHIA | Brasil | 2924405 | 29 | 33 | nan | nan | nan | Cerrado | nan |
| f853e671-2a1f-3921-8596-bb2c6bdcf5aa | -6.1658 | -44.653599 | 2026-09-10 00:28:00 | METOP-C | MIRADOR | MARANHÃO | Brasil | 2106706 | 21 | 33 | nan | nan | nan | Cerrado | nan |
| 9f047ae3-3755-37d3-9883-54ff505ac6bf | -10.2328 | -45.209099 | 2026-09-10 00:28:00 | METOP-C | CORRENTE | PIAUÍ | Brasil | 2202901 | 22 | 33 | nan | nan | nan | Cerrado | nan |
| ff3d85d5-8044-3577-8893-34e7d4eb5740 | -5.5896 | -45.377201 | 2026-09-10 00:28:00 | METOP-C | BARRA DO CORDA | MARANHÃO | Brasil | 2101608 | 21 | 33 | nan | nan | nan | Cerrado | nan |
| 92e444da-2305-3887-b8c5-ed997e0125e4 | -10.9118 | -47.856098 | 2026-09-10 00:28:00 | METOP-C | MONTE DO CARMO | TOCANTINS | Brasil | 1713601 | 17 | 33 | nan | nan | nan | Cerrado | nan |
| bedfe4eb-6e71-3226-9d0a-59018df38c6a | -12.8592 | -44.6091 | 2026-09-10 00:28:00 | METOP-C | SÃO DESIDÉRIO | BAHIA | Brasil | 2928901 | 29 | 33 | nan | nan | nan | Cerrado | nan |
| bd04f03b-e971-3199-9da6-4fdf2681cf90 | -9.6584 | -40.632702 | 2026-09-10 00:28:00 | METOP-C | JUAZEIRO | BAHIA | Brasil | 2918407 | 29 | 33 | nan | nan | nan | Caatinga | nan |
| 4791ea5c-81d0-393b-b854-33914a3fcd49 | -7.9917 | -43.981499 | 2026-09-10 00:28:00 | METOP-C | SEBASTIÃO LEAL | PIAUÍ | Brasil | 2210631 | 22 | 33 | nan | nan | nan | Cerrado | nan |
| 4ecba05d-3a78-3721-a962-1d7286ed875b | -7.4976 | -45.285999 | 2026-09-10 00:28:00 | METOP-C | LORETO | MARANHÃO | Brasil | 2106102 | 21 | 33 | nan | nan | nan | Cerrado | nan |
| 5db9e64b-d97d-3d33-b48f-585ce1fa51e8 | -12.8273 | -44.3298 | 2026-09-10 00:28:00 | METOP-C | BAIANÓPOLIS | BAHIA | Brasil | 2902500 | 29 | 33 | nan | nan | nan | Cerrado | nan |
| 4b470086-9c26-3b3a-adb2-d0b5db6cca83 | -6.1626 | -44.639599 | 2026-09-10 00:28:00 | METOP-C | MIRADOR | MARANHÃO | Brasil | 2106706 | 21 | 33 | nan | nan | nan | Cerrado | nan |
| 02c9da91-4674-3c84-82a7-49d2a24f7ef3 | -6.7213 | -45.454201 | 2026-09-10 00:28:00 | METOP-C | MIRADOR | MARANHÃO | Brasil | 2106706 | 21 | 33 | nan | nan | nan | Cerrado | nan |
| 1b310320-2d23-3f55-a1b6-ea90eac91563 | -10.4264 | -37.183998 | 2026-09-10 00:28:00 | METOP-C | NOSSA SENHORA DAS DORES | SERGIPE | Brasil | 2804607 | 28 | 33 | nan | nan | nan | Mata Atlântica | nan |
| 8f9d3966-49a7-3b8e-81d7-c993fdfeb464 | -14.1997 | -41.596699 | 2026-09-10 00:28:00 | METOP-C | BRUMADO | BAHIA | Brasil | 2904605 | 29 | 33 | nan | nan | nan | Caatinga | nan |
| 616cad26-14ac-38e6-8b1a-448c9df29c50 | -15.7852 | -43.550301 | 2026-09-10 00:28:00 | METOP-C | JANAÚBA | MINAS GERAIS | Brasil | 3135100 | 31 | 33 | nan | nan | nan | Cerrado | nan |
| c99e8839-fb42-3dd3-8e95-d82d0dcc1bff | -7.1059 | -42.139 | 2026-09-10 00:28:00 | METOP-C | OEIRAS | PIAUÍ | Brasil | 2207009 | 22 | 33 | nan | nan | nan | Caatinga | nan |
| bee7bfdc-4472-3159-a5c2-5a593fb06b7d | -9.7049 | -43.401901 | 2026-09-10 00:28:00 | METOP-C | PILÃO ARCADO | BAHIA | Brasil | 2924405 | 29 | 33 | nan | nan | nan | Caatinga | nan |
| 88806e22-0842-34e8-be18-b8fc0a0fd2d5 | -9.7163 | -43.406898 | 2026-09-10 00:28:00 | METOP-C | PILÃO ARCADO | BAHIA | Brasil | 2924405 | 29 | 33 | nan | nan | nan | Caatinga | nan |
| f7ae05d2-8bc2-3b5f-bbcc-80d3adf528ea | -12.3492 | -48.201401 | 2026-09-10 00:28:00 | METOP-C | PARANÃ | TOCANTINS | Brasil | 1716208 | 17 | 33 | nan | nan | nan | Cerrado | nan |
| cc620070-5b4c-3b2f-b44c-b376b90d1ddc | -3.96 | -44.351101 | 2026-09-10 00:28:00 | METOP-C | COROATÁ | MARANHÃO | Brasil | 2103604 | 21 | 33 | nan | nan | nan | Cerrado | nan |
| 136226c6-cfa7-3da9-86dd-85a6631b14aa | -5.6135 | -44.853199 | 2026-09-10 00:28:00 | METOP-C | TUNTUM | MARANHÃO | Brasil | 2112308 | 21 | 33 | nan | nan | nan | Cerrado | nan |
| 46375ec7-bbd1-32ca-ab4f-fc0b9ebd5f12 | -6.6398 | -45.9552 | 2026-09-10 00:28:00 | METOP-C | FORTALEZA DOS NOGUEIRAS | MARANHÃO | Brasil | 2104107 | 21 | 33 | nan | nan | nan | Cerrado | nan |
| ff2b19fd-f606-3c4e-bc7d-26fb4d812bac | -12.832 | -44.3507 | 2026-09-10 00:28:00 | METOP-C | BAIANÓPOLIS | BAHIA | Brasil | 2902500 | 29 | 33 | nan | nan | nan | Cerrado | nan |
| b6699c80-3140-3019-ae53-f06b47bf9963 | -5.7693 | -45.0821 | 2026-09-10 00:28:00 | METOP-C | BARRA DO CORDA | MARANHÃO | Brasil | 2101608 | 21 | 33 | nan | nan | nan | Cerrado | nan |
| 02757fb7-83c8-386c-bdd6-a82a00009625 | -10.2344 | -45.216 | 2026-09-10 00:28:00 | METOP-C | CORRENTE | PIAUÍ | Brasil | 2202901 | 22 | 33 | nan | nan | nan | Cerrado | nan |
| 53e49fb3-21ba-3d26-bcb3-2dcf86824265 | -5.925 | -44.951698 | 2026-09-10 00:28:00 | METOP-C | FERNANDO FALCÃO | MARANHÃO | Brasil | 2104081 | 21 | 33 | nan | nan | nan | Cerrado | nan |
| ce3de4b8-8b26-3648-9c5a-5bd02ea4ef3e | -9.7066 | -43.409199 | 2026-09-10 00:28:00 | METOP-C | PILÃO ARCADO | BAHIA | Brasil | 2924405 | 29 | 33 | nan | nan | nan | Caatinga | nan |
| 0ef08237-a4dd-349a-a64e-ca8314a2acd7 | -3.3732 | -50.407101 | 2026-09-10 00:28:00 | METOP-C | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| de43b4f6-683b-30d3-af25-09eac85fc700 | -5.5532 | -43.4375 | 2026-09-10 00:28:00 | METOP-C | PARNARAMA | MARANHÃO | Brasil | 2107803 | 21 | 33 | nan | nan | nan | Cerrado | nan |
| 0b313194-34b7-34ed-a7aa-e6f55b48a15b | -12.6355 | -47.096298 | 2026-09-10 00:28:00 | METOP-C | ARRAIAS | TOCANTINS | Brasil | 1702406 | 17 | 33 | nan | nan | nan | Cerrado | nan |
| a4a7f890-5ac3-388f-ab4c-9b18e721168e | -2.9402 | -50.492599 | 2026-09-10 00:28:00 | METOP-C | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| d2470f29-fee4-389e-b297-bd09f9848c97 | -4.3623 | -47.769901 | 2026-09-10 00:28:00 | METOP-C | DOM ELISEU | PARÁ | Brasil | 1502939 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| 8048038c-3710-3913-bc4e-24203d26e6aa | -8.9454 | -44.402599 | 2026-09-10 00:28:00 | METOP-C | CURRAIS | PIAUÍ | Brasil | 2203230 | 22 | 33 | nan | nan | nan | Cerrado | nan |
| fb0c3ed8-d437-3568-8c9a-700afe869e7b | -2.8907 | -48.2766 | 2026-09-10 00:28:00 | METOP-C | TOMÉ-AÇU | PARÁ | Brasil | 1508001 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| 9c4ffbcb-417b-3abe-8013-3ae3112d3305 | -9.689 | -43.4669 | 2026-09-10 00:28:00 | METOP-C | PILÃO ARCADO | BAHIA | Brasil | 2924405 | 29 | 33 | nan | nan | nan | Caatinga | nan |
| 5a7d10bc-2001-3372-be89-c42a81e545e6 | -15.3231 | -47.253502 | 2026-09-10 00:28:00 | METOP-C | FORMOSA | GOIÁS | Brasil | 5208004 | 52 | 33 | nan | nan | nan | Cerrado | nan |
| 21bd8582-d1f3-34b4-9e3d-15faf9f7c217 | -9.6842 | -43.491001 | 2026-09-10 00:28:00 | METOP-C | PILÃO ARCADO | BAHIA | Brasil | 2924405 | 29 | 33 | nan | nan | nan | Cerrado | nan |
| e596e7a8-26f9-3f03-9fec-d9f076826def | -10.0739 | -45.463699 | 2026-09-10 00:28:00 | METOP-C | SÃO GONÇALO DO GURGUÉIA | PIAUÍ | Brasil | 2209757 | 22 | 33 | nan | nan | nan | Cerrado | nan |
| 1062d164-c771-395d-8b8b-978850442dde | -4.2867 | -46.532398 | 2026-09-10 00:28:00 | METOP-C | BOM JESUS DAS SELVAS | MARANHÃO | Brasil | 2102036 | 21 | 33 | nan | nan | nan | Amazônia | nan |
| 2933723b-77ff-36bd-9079-36f59313fa6f | -6.2719 | -46.376598 | 2026-09-10 00:28:00 | METOP-C | FORMOSA DA SERRA NEGRA | MARANHÃO | Brasil | 2104099 | 21 | 33 | nan | nan | nan | Cerrado | nan |
| 5f2cfc42-eab2-3eef-a41e-3d1f6fb9b35c | -5.5978 | -45.368099 | 2026-09-10 00:28:00 | METOP-C | BARRA DO CORDA | MARANHÃO | Brasil | 2101608 | 21 | 33 | nan | nan | nan | Cerrado | nan |
| f8ec7f49-9161-39d2-b75a-e4ca80582b2e | -5.1761 | -45.4632 | 2026-09-10 00:28:00 | METOP-C | JENIPAPO DOS VIEIRAS | MARANHÃO | Brasil | 2105476 | 21 | 33 | nan | nan | nan | Cerrado | nan |
| acbf2f05-2e2c-3740-abcc-b0dea69d5292 | 2.5181 | -50.847301 | 2026-09-10 00:28:00 | METOP-C | CALÇOENE | AMAPÁ | Brasil | 1600204 | 16 | 33 | nan | nan | nan | Amazônia | nan |
| acc53805-e59f-3616-b2a4-84970808abda | -7.2086 | -43.632 | 2026-09-10 00:28:00 | METOP-C | JERUMENHA | PIAUÍ | Brasil | 2205300 | 22 | 33 | nan | nan | nan | Cerrado | nan |
| a7498b66-12cd-3f2b-9da4-d1c4d9cf3b0c | -2.9145 | -54.117599 | 2026-09-10 00:28:00 | METOP-C | SANTARÉM | PARÁ | Brasil | 1506807 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| e24454f2-5923-3c84-975b-7b8873d479c4 | -3.2604 | -50.089199 | 2026-09-10 00:28:00 | METOP-C | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| b759039b-2586-3871-a7d8-3e35da6a3582 | -5.3787 | -46.302601 | 2026-09-10 00:28:00 | METOP-C | GRAJAÚ | MARANHÃO | Brasil | 2104800 | 21 | 33 | nan | nan | nan | Amazônia | nan |
| 1c4fd718-91b9-351a-90d7-19dbfc61abb1 | -10.5935 | -47.1036 | 2026-09-10 00:28:00 | METOP-C | PONTE ALTA DO TOCANTINS | TOCANTINS | Brasil | 1717909 | 17 | 33 | nan | nan | nan | Cerrado | nan |
| 48daf666-5076-324e-9222-6ce673f2358f | -7.4877 | -45.2882 | 2026-09-10 00:28:00 | METOP-C | LORETO | MARANHÃO | Brasil | 2106102 | 21 | 33 | nan | nan | nan | Cerrado | nan |
| be0a0c29-2303-3c4a-92af-2c2074cd213c | -9.6907 | -43.474201 | 2026-09-10 00:28:00 | METOP-C | PILÃO ARCADO | BAHIA | Brasil | 2924405 | 29 | 33 | nan | nan | nan | Caatinga | nan |
| d1487332-d8c4-3fad-939d-9829d2594d9e | -2.9382 | -50.483601 | 2026-09-10 00:28:00 | METOP-C | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| 7eeb74e1-74f6-38cc-9c9a-3e341fc99c9a | -12.8257 | -44.3228 | 2026-09-10 00:28:00 | METOP-C | BAIANÓPOLIS | BAHIA | Brasil | 2902500 | 29 | 33 | nan | nan | nan | Cerrado | nan |
| c9409e59-405a-3eb2-91ae-8cf96282a8a0 | -13.4384 | -43.841499 | 2026-09-10 00:28:00 | METOP-C | SERRA DO RAMALHO | BAHIA | Brasil | 2930154 | 29 | 33 | nan | nan | nan | Cerrado | nan |
| 46021c95-e417-30e7-8b95-a95f2eb8839d | -10.0786 | -45.4846 | 2026-09-10 00:28:00 | METOP-C | SÃO GONÇALO DO GURGUÉIA | PIAUÍ | Brasil | 2209757 | 22 | 33 | nan | nan | nan | Cerrado | nan |
| bc20ffd5-b5f6-3136-8047-b5729d651e80 | 2.5162 | -50.855499 | 2026-09-10 00:28:00 | METOP-C | CALÇOENE | AMAPÁ | Brasil | 1600204 | 16 | 33 | nan | nan | nan | Amazônia | nan |
| 6d259d44-4d6a-3b2e-be2c-345757e65667 | -9.6839 | -43.445099 | 2026-09-10 00:28:00 | METOP-C | PILÃO ARCADO | BAHIA | Brasil | 2924405 | 29 | 33 | nan | nan | nan | Caatinga | nan |
| f650ab54-4a3b-30f5-b734-590c5ee72a2c | -7.9884 | -43.967201 | 2026-09-10 00:28:00 | METOP-C | BERTOLÍNIA | PIAUÍ | Brasil | 2201705 | 22 | 33 | nan | nan | nan | Cerrado | nan |
| 736a45c8-40f1-3a91-b124-cc924205936f | -5.7662 | -45.068199 | 2026-09-10 00:28:00 | METOP-C | BARRA DO CORDA | MARANHÃO | Brasil | 2101608 | 21 | 33 | nan | nan | nan | Cerrado | nan |
| d1c16564-a47d-3052-aaa2-9951ae08757d | -12.8304 | -44.3437 | 2026-09-10 00:28:00 | METOP-C | BAIANÓPOLIS | BAHIA | Brasil | 2902500 | 29 | 33 | nan | nan | nan | Cerrado | nan |


[Clique aqui para ver as próximas entradas](README6.md)
