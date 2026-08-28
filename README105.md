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

## Dados Diários - Página 105

| ID | Latitude | Longitude | Data/Hora GMT | Satélite | Município | Estado | País | Município ID | Estado ID | País ID | Dias sem Chuva | Precipitação | Risco de Fogo | Bioma | FRP |
|----|----------|-----------|---------------|----------|-----------|--------|------|--------------|-----------|---------|----------------|--------------|----------------|-------|-----|
| fa52eba3-81b3-32da-8f15-b357c686110d | -21.90637 | -55.42597 | 2026-08-28 17:24:00 | NPP-375 | PONTA PORÃ | MATO GROSSO DO SUL | Brasil | 5006606 | 50 | 33 | nan | nan | nan | Cerrado | 2.7 |
| 1c765a94-d33f-3622-add8-41c6ce8da6b9 | -20.69628 | -50.47918 | 2026-08-28 17:24:00 | NPP-375 | GENERAL SALGADO | SÃO PAULO | Brasil | 3516903 | 35 | 33 | nan | nan | nan | Mata Atlântica | 7.0 |
| 876f12de-fd28-3d0b-9ef9-a5fd7cae05ef | -19.23172 | -57.66574 | 2026-08-28 17:24:00 | NPP-375 | CORUMBÁ | MATO GROSSO DO SUL | Brasil | 5003207 | 50 | 33 | nan | nan | nan | Pantanal | 7.7 |
| cb3c013e-e6d4-3f6e-8e2c-30a41a223096 | -23.12699 | -48.30661 | 2026-08-28 17:24:00 | NPP-375 | BOFETE | SÃO PAULO | Brasil | 3506904 | 35 | 33 | nan | nan | nan | Mata Atlântica | 4.8 |
| 3a17c4ef-3d23-3278-8665-0eeec6001ac1 | -23.53627 | -47.31274 | 2026-08-28 17:24:00 | NPP-375 | SOROCABA | SÃO PAULO | Brasil | 3552205 | 35 | 33 | nan | nan | nan | Mata Atlântica | 5.2 |
| 8256f764-bd4a-3c91-8390-111600672820 | -19.06245 | -57.39795 | 2026-08-28 17:24:00 | NPP-375 | CORUMBÁ | MATO GROSSO DO SUL | Brasil | 5003207 | 50 | 33 | nan | nan | nan | Pantanal | 14.2 |
| 7c1f1459-f3e9-3654-8cf4-c4fcea4437fd | -22.27364 | -56.08784 | 2026-08-28 17:24:00 | NPP-375 | ANTÔNIO JOÃO | MATO GROSSO DO SUL | Brasil | 5000906 | 50 | 33 | nan | nan | nan | Cerrado | 2.4 |
| a94beb64-ebf3-3a4a-8343-7440512c889e | -22.01117 | -46.689 | 2026-08-28 17:24:00 | NPP-375 | SÃO JOÃO DA BOA VISTA | SÃO PAULO | Brasil | 3549102 | 35 | 33 | nan | nan | nan | Mata Atlântica | 8.5 |
| eb4dc084-db90-32aa-b760-096a0b87c99c | -17.30375 | -46.58315 | 2026-08-28 17:24:00 | NPP-375 | PARACATU | MINAS GERAIS | Brasil | 3147006 | 31 | 33 | nan | nan | nan | Cerrado | 8.3 |
| 6d1f9cdb-81be-3b2c-b092-0a13b1672075 | -17.74695 | -44.296 | 2026-08-28 17:24:00 | NPP-375 | LASSANCE | MINAS GERAIS | Brasil | 3138104 | 31 | 33 | nan | nan | nan | Cerrado | 2.7 |
| 8fba7707-bb2c-3bbe-9c5b-ee375ef3463a | -21.2063 | -44.12736 | 2026-08-28 17:24:00 | NPP-375 | SÃO JOÃO DEL REI | MINAS GERAIS | Brasil | 3162500 | 31 | 33 | nan | nan | nan | Mata Atlântica | 6.7 |
| 1d27d77e-fe06-3540-bdf9-0b1a593fa697 | -23.40033 | -51.99873 | 2026-08-28 17:24:00 | NPP-375 | MARINGÁ | PARANÁ | Brasil | 4115200 | 41 | 33 | nan | nan | nan | Mata Atlântica | 4.7 |
| 4f2438a1-dbd9-33f9-a6b0-a64403ed3693 | -20.93922 | -57.62063 | 2026-08-28 17:24:00 | NPP-375 | PORTO MURTINHO | MATO GROSSO DO SUL | Brasil | 5006903 | 50 | 33 | nan | nan | nan | Pantanal | 4.1 |
| 5f680305-d214-3739-82f5-0f94098983b0 | -17.34139 | -42.82325 | 2026-08-28 17:24:00 | NPP-375 | TURMALINA | MINAS GERAIS | Brasil | 3169703 | 31 | 33 | nan | nan | nan | Cerrado | 3.2 |
| f0a5befc-916b-3b2d-b92a-9cc8a5e8b1dc | -21.20579 | -44.12303 | 2026-08-28 17:24:00 | NPP-375 | SÃO JOÃO DEL REI | MINAS GERAIS | Brasil | 3162500 | 31 | 33 | nan | nan | nan | Mata Atlântica | 14.0 |
| 5a7bf77d-57e5-34dd-ae98-826534fc7c6d | -20.68912 | -50.48059 | 2026-08-28 17:24:00 | NPP-375 | AURIFLAMA | SÃO PAULO | Brasil | 3504206 | 35 | 33 | nan | nan | nan | Mata Atlântica | 93.7 |
| 5b115b26-c0cf-3115-a14e-8617b06b3dad | -16.55116 | -42.40748 | 2026-08-28 17:24:00 | NPP-375 | VIRGEM DA LAPA | MINAS GERAIS | Brasil | 3171600 | 31 | 33 | nan | nan | nan | Cerrado | 2.1 |
| 1e4c87b8-3bda-37d2-9c60-e1572cddf0f0 | -17.29792 | -46.57871 | 2026-08-28 17:24:00 | NPP-375 | PARACATU | MINAS GERAIS | Brasil | 3147006 | 31 | 33 | nan | nan | nan | Cerrado | 6.0 |
| 399faa0c-55b3-3dfe-84f1-d5a263ee693b | -19.2299 | -57.6521 | 2026-08-28 17:24:00 | NPP-375 | CORUMBÁ | MATO GROSSO DO SUL | Brasil | 5003207 | 50 | 33 | nan | nan | nan | Pantanal | 10.3 |
| d830f12e-c89f-3fb0-ba45-7d258b7658e3 | -23.12638 | -48.3035 | 2026-08-28 17:24:00 | NPP-375 | BOFETE | SÃO PAULO | Brasil | 3506904 | 35 | 33 | nan | nan | nan | Mata Atlântica | 3.8 |
| a16b4859-9666-3c60-a5ee-3674aa1779cc | -19.23111 | -57.66119 | 2026-08-28 17:24:00 | NPP-375 | CORUMBÁ | MATO GROSSO DO SUL | Brasil | 5003207 | 50 | 33 | nan | nan | nan | Pantanal | 7.5 |
| 9f33d20a-835c-3233-87e7-7a99984ec2b8 | -18.45961 | -40.57123 | 2026-08-28 17:24:00 | NPP-375 | ECOPORANGA | ESPÍRITO SANTO | Brasil | 3202108 | 32 | 33 | nan | nan | nan | Mata Atlântica | 9.4 |
| 86e81b35-4816-3d90-9888-30c3b3e4c050 | -21.05266 | -44.43202 | 2026-08-28 17:24:00 | NPP-375 | CONCEIÇÃO DA BARRA DE MINAS | MINAS GERAIS | Brasil | 3115201 | 31 | 33 | nan | nan | nan | Mata Atlântica | 4.2 |
| f9731f3e-ad1f-3973-a95a-e5103f43f7d9 | -19.06671 | -57.40186 | 2026-08-28 17:24:00 | NPP-375 | CORUMBÁ | MATO GROSSO DO SUL | Brasil | 5003207 | 50 | 33 | nan | nan | nan | Pantanal | 52.3 |
| c0d51d8f-45d9-3387-9ed7-58b4ea7dcba1 | -18.43806 | -43.91365 | 2026-08-28 17:24:00 | NPP-375 | MONJOLOS | MINAS GERAIS | Brasil | 3142502 | 31 | 33 | nan | nan | nan | Cerrado | 3.3 |
| f8ec67f8-f680-3daa-bb5f-542142c28fb6 | -21.90291 | -55.42653 | 2026-08-28 17:24:00 | NPP-375 | PONTA PORÃ | MATO GROSSO DO SUL | Brasil | 5006606 | 50 | 33 | nan | nan | nan | Cerrado | 2.7 |
| 8aa9352e-23a5-3a23-9c53-ea10c432f9f8 | -19.15022 | -48.90748 | 2026-08-28 17:24:00 | NPP-375 | PRATA | MINAS GERAIS | Brasil | 3152808 | 31 | 33 | nan | nan | nan | Cerrado | 2.4 |
| 35b7a56a-a734-3922-802a-230d64bd9271 | -21.90693 | -55.42999 | 2026-08-28 17:24:00 | NPP-375 | PONTA PORÃ | MATO GROSSO DO SUL | Brasil | 5006606 | 50 | 33 | nan | nan | nan | Cerrado | 4.8 |
| d2b38ff8-1149-3310-8181-acdaacbec27e | -21.04066 | -57.84499 | 2026-08-28 17:24:00 | NPP-375 | PORTO MURTINHO | MATO GROSSO DO SUL | Brasil | 5006903 | 50 | 33 | nan | nan | nan | Pantanal | 24.2 |
| 8acd18ad-17ea-3b77-846d-d5176f42efbc | -17.9788 | -50.19253 | 2026-08-28 17:24:00 | NPP-375 | PORTEIRÃO | GOIÁS | Brasil | 5218052 | 52 | 33 | nan | nan | nan | Cerrado | 10.6 |
| c47aa51f-f68d-3f89-8418-cfd83057f091 | -18.37779 | -46.01271 | 2026-08-28 17:24:00 | NPP-375 | VARJÃO DE MINAS | MINAS GERAIS | Brasil | 3170750 | 31 | 33 | nan | nan | nan | Cerrado | 3.9 |
| 1d0f5c40-c35a-353d-94e9-8e0a75285fd0 | -20.46897 | -48.78711 | 2026-08-28 17:24:00 | NPP-375 | BARRETOS | SÃO PAULO | Brasil | 3505500 | 35 | 33 | nan | nan | nan | Mata Atlântica | 19.1 |
| 14f89999-99ea-3df4-8275-5d1b4ade599b | -24.21387 | -53.29186 | 2026-08-28 17:24:00 | NPP-375 | FORMOSA DO OESTE | PARANÁ | Brasil | 4108205 | 41 | 33 | nan | nan | nan | Mata Atlântica | 0.6 |
| f91adc95-37d3-34fb-a27a-9171a4e13c40 | -19.22677 | -57.65702 | 2026-08-28 17:24:00 | NPP-375 | CORUMBÁ | MATO GROSSO DO SUL | Brasil | 5003207 | 50 | 33 | nan | nan | nan | Pantanal | 21.7 |
| 9aa9c9d6-7178-340e-a44d-8616f1b08d3d | -23.54445 | -47.31139 | 2026-08-28 17:24:00 | NPP-375 | SOROCABA | SÃO PAULO | Brasil | 3552205 | 35 | 33 | nan | nan | nan | Mata Atlântica | 9.0 |
| c05cb51d-4484-3ec6-ae0a-d4c60a778abc | -17.27169 | -42.30617 | 2026-08-28 17:24:00 | NPP-375 | MINAS NOVAS | MINAS GERAIS | Brasil | 3141801 | 31 | 33 | nan | nan | nan | Mata Atlântica | 3.0 |
| 7ede0806-9632-3af4-adf5-c24d1c3a60c8 | -23.25573 | -46.75871 | 2026-08-28 17:24:00 | NPP-375 | FRANCISCO MORATO | SÃO PAULO | Brasil | 3516309 | 35 | 33 | nan | nan | nan | Mata Atlântica | 5.7 |
| bee94a66-0f97-3343-8718-eb4ea599d8f2 | -17.98174 | -50.18708 | 2026-08-28 17:24:00 | NPP-375 | PORTEIRÃO | GOIÁS | Brasil | 5218052 | 52 | 33 | nan | nan | nan | Cerrado | 10.6 |
| fca1f830-20cb-31d8-8a3d-9c1413ac3e95 | -17.29316 | -46.57969 | 2026-08-28 17:24:00 | NPP-375 | PARACATU | MINAS GERAIS | Brasil | 3147006 | 31 | 33 | nan | nan | nan | Cerrado | 6.4 |
| 428ed1e4-eb7e-35c0-ad68-d6a2199b2c55 | -23.8815 | -51.45014 | 2026-08-28 17:24:00 | NPP-375 | FAXINAL | PARANÁ | Brasil | 4107603 | 41 | 33 | nan | nan | nan | Mata Atlântica | 3.0 |
| 749374fd-b74e-3079-8f18-5b20ba60a4bb | -20.01497 | -52.99401 | 2026-08-28 17:24:00 | NPP-375 | ÁGUA CLARA | MATO GROSSO DO SUL | Brasil | 5000203 | 50 | 33 | nan | nan | nan | Cerrado | 5.5 |
| 52fba684-2555-3e2d-8792-5b773fc07d4f | -18.79342 | -50.92185 | 2026-08-28 17:24:00 | NPP-375 | CACHOEIRA ALTA | GOIÁS | Brasil | 5204102 | 52 | 33 | nan | nan | nan | Mata Atlântica | 13.8 |
| fd249e45-4b61-37d0-b0e8-c8ff44d81d5e | -20.01477 | -52.99854 | 2026-08-28 17:24:00 | NPP-375 | ÁGUA CLARA | MATO GROSSO DO SUL | Brasil | 5000203 | 50 | 33 | nan | nan | nan | Cerrado | 4.7 |
| c30c1539-febd-38cc-b9d8-997f4449a90b | -20.68442 | -50.48069 | 2026-08-28 17:24:00 | NPP-375 | AURIFLAMA | SÃO PAULO | Brasil | 3504206 | 35 | 33 | nan | nan | nan | Mata Atlântica | 115.1 |
| 8d42553d-4649-39a9-ab88-512cf2fbd25a | -21.91039 | -55.42944 | 2026-08-28 17:24:00 | NPP-375 | PONTA PORÃ | MATO GROSSO DO SUL | Brasil | 5006606 | 50 | 33 | nan | nan | nan | Cerrado | 7.2 |
| e1ca4001-19ac-395d-987d-e0b3da8f5d97 | -20.59979 | -56.98482 | 2026-08-28 17:24:00 | NPP-375 | PORTO MURTINHO | MATO GROSSO DO SUL | Brasil | 5006903 | 50 | 33 | nan | nan | nan | Cerrado | 6.2 |
| 0505a0ec-b803-35f5-9085-b02b0ca5e806 | -20.90972 | -57.57085 | 2026-08-28 17:24:00 | NPP-375 | PORTO MURTINHO | MATO GROSSO DO SUL | Brasil | 5006903 | 50 | 33 | nan | nan | nan | Pantanal | 9.9 |
| 9cfb4580-f501-3c5c-a2b1-768188dcee5d | -18.45874 | -40.57305 | 2026-08-28 17:24:00 | NPP-375 | ECOPORANGA | ESPÍRITO SANTO | Brasil | 3202108 | 32 | 33 | nan | nan | nan | Mata Atlântica | 6.4 |
| 95dff1c1-b20e-3eb2-bfd3-1308dd7ae37a | -20.91034 | -57.57565 | 2026-08-28 17:24:00 | NPP-375 | PORTO MURTINHO | MATO GROSSO DO SUL | Brasil | 5006903 | 50 | 33 | nan | nan | nan | Pantanal | 7.9 |
| af9848bb-62d2-3c60-a161-b6904a4de59d | -20.01556 | -52.99774 | 2026-08-28 17:24:00 | NPP-375 | ÁGUA CLARA | MATO GROSSO DO SUL | Brasil | 5000203 | 50 | 33 | nan | nan | nan | Cerrado | 5.5 |
| 4cc3a267-0528-3134-b7ea-03a80ce5ec11 | -19.23232 | -57.67025 | 2026-08-28 17:24:00 | NPP-375 | CORUMBÁ | MATO GROSSO DO SUL | Brasil | 5003207 | 50 | 33 | nan | nan | nan | Pantanal | 7.7 |
| d14d83b7-ce56-383a-b30a-b6aa0100a837 | -20.68988 | -50.48495 | 2026-08-28 17:24:00 | NPP-375 | AURIFLAMA | SÃO PAULO | Brasil | 3504206 | 35 | 33 | nan | nan | nan | Mata Atlântica | 93.7 |
| dc5fe78a-0651-32d8-bc25-a9349429b033 | -21.04833 | -57.84389 | 2026-08-28 17:24:00 | NPP-375 | PORTO MURTINHO | MATO GROSSO DO SUL | Brasil | 5006903 | 50 | 33 | nan | nan | nan | Pantanal | 7.8 |
| 132a9aef-1581-3132-9c9d-12555add9862 | -20.9091 | -57.56603 | 2026-08-28 17:24:00 | NPP-375 | PORTO MURTINHO | MATO GROSSO DO SUL | Brasil | 5006903 | 50 | 33 | nan | nan | nan | Pantanal | 9.9 |
| 837348b6-575b-37e7-aae5-f066dca225aa | -23.37068 | -52.94023 | 2026-08-28 17:24:00 | NPP-375 | CIDADE GAÚCHA | PARANÁ | Brasil | 4105607 | 41 | 33 | nan | nan | nan | Mata Atlântica | 2.1 |
| 4dcf9615-8b16-344f-93aa-552462c65452 | -22.17493 | -50.38935 | 2026-08-28 17:24:00 | NPP-375 | QUINTANA | SÃO PAULO | Brasil | 3542008 | 35 | 33 | nan | nan | nan | Mata Atlântica | 8.6 |
| 728b214a-675e-3364-a501-bc287bd68c6c | -17.80949 | -44.32521 | 2026-08-28 17:24:00 | NPP-375 | LASSANCE | MINAS GERAIS | Brasil | 3138104 | 31 | 33 | nan | nan | nan | Cerrado | 6.2 |
| 6ce9649a-b413-3899-b215-fef49f9fdb6e | -19.18474 | -44.91573 | 2026-08-28 17:24:00 | NPP-375 | POMPÉU | MINAS GERAIS | Brasil | 3152006 | 31 | 33 | nan | nan | nan | Cerrado | 8.1 |
| 57da43f3-a4fb-394c-8901-76689ff44601 | -21.89797 | -55.36561 | 2026-08-28 17:24:00 | NPP-375 | DOURADOS | MATO GROSSO DO SUL | Brasil | 5003702 | 50 | 33 | nan | nan | nan | Cerrado | 4.1 |
| 1dc68fc5-8699-346f-bc17-3afcf5e822c2 | -13.4091 | -51.77144 | 2026-08-28 17:26:00 | NPP-375 | RIBEIRÃO CASCALHEIRA | MATO GROSSO | Brasil | 5107180 | 51 | 33 | nan | nan | nan | Cerrado | 11.0 |
| 5ccf1d25-f474-3d1e-a92e-07245e46fa03 | -9.79551 | -46.33306 | 2026-08-28 17:26:00 | NPP-375 | ALTO PARNAÍBA | MARANHÃO | Brasil | 2100501 | 21 | 33 | nan | nan | nan | Cerrado | 6.4 |
| e9549257-ace4-3b88-bb15-6dd44437a6d5 | -11.24371 | -45.074 | 2026-08-28 17:26:00 | NPP-375 | FORMOSA DO RIO PRETO | BAHIA | Brasil | 2911105 | 29 | 33 | nan | nan | nan | Cerrado | 6.7 |
| 76b74ce9-d7af-3933-8113-75f42a3cc7a0 | -10.24743 | -47.99832 | 2026-08-28 17:26:00 | NPP-375 | PALMAS | TOCANTINS | Brasil | 1721000 | 17 | 33 | nan | nan | nan | Cerrado | 12.2 |
| eefef117-0f90-3ecc-b3f9-1a0fc547033d | -10.07786 | -48.66714 | 2026-08-28 17:26:00 | NPP-375 | MIRACEMA DO TOCANTINS | TOCANTINS | Brasil | 1713205 | 17 | 33 | nan | nan | nan | Cerrado | 23.3 |
| 3fae090d-844b-37f9-ad58-a19269980704 | -8.96403 | -42.70063 | 2026-08-28 17:26:00 | NPP-375 | SÃO RAIMUNDO NONATO | PIAUÍ | Brasil | 2210607 | 22 | 33 | nan | nan | nan | Caatinga | 12.1 |
| 5335324b-ff4d-3372-95fa-f46453e6dae5 | -16.19765 | -57.75943 | 2026-08-28 17:26:00 | NPP-375 | CÁCERES | MATO GROSSO | Brasil | 5102504 | 51 | 33 | nan | nan | nan | Pantanal | 6.4 |
| 55baf301-4be5-31df-8443-a805340479cd | -12.91259 | -45.85901 | 2026-08-28 17:26:00 | NPP-375 | SÃO DESIDÉRIO | BAHIA | Brasil | 2928901 | 29 | 33 | nan | nan | nan | Cerrado | 4.2 |
| f2da7c07-28af-3bbc-8a23-e6d020d9f8e2 | -11.20629 | -53.99006 | 2026-08-28 17:26:00 | NPP-375 | MARCELÂNDIA | MATO GROSSO | Brasil | 5105580 | 51 | 33 | nan | nan | nan | Amazônia | 9.1 |
| 43b1afe5-95a6-3ed4-b98b-171b9d26f8af | -14.45906 | -53.37375 | 2026-08-28 17:26:00 | NPP-375 | CAMPINÁPOLIS | MATO GROSSO | Brasil | 5102603 | 51 | 33 | nan | nan | nan | Cerrado | 9.0 |
| 4c3dbade-87bf-3b3e-9266-a69b20235fbe | -11.27646 | -54.03265 | 2026-08-28 17:26:00 | NPP-375 | UNIÃO DO SUL | MATO GROSSO | Brasil | 5108303 | 51 | 33 | nan | nan | nan | Amazônia | 14.9 |
| 1fb65d3d-378e-36d9-a53d-0d22640c1957 | -11.69873 | -47.62064 | 2026-08-28 17:26:00 | NPP-375 | NATIVIDADE | TOCANTINS | Brasil | 1714203 | 17 | 33 | nan | nan | nan | Cerrado | 12.5 |
| 2745b6a0-f472-3174-a421-c041f2bce961 | -10.83129 | -50.51686 | 2026-08-28 17:26:00 | NPP-375 | LAGOA DA CONFUSÃO | TOCANTINS | Brasil | 1711902 | 17 | 33 | nan | nan | nan | Cerrado | 12.3 |
| c13caaae-4255-3ecc-9190-2cd4ea3110d4 | -11.9609 | -45.50506 | 2026-08-28 17:26:00 | NPP-375 | BARREIRAS | BAHIA | Brasil | 2903201 | 29 | 33 | nan | nan | nan | Cerrado | 12.7 |
| 1614f46f-2916-3dcf-86d7-e98fdb5590fe | -13.5891 | -45.77871 | 2026-08-28 17:26:00 | NPP-375 | CORRENTINA | BAHIA | Brasil | 2909307 | 29 | 33 | nan | nan | nan | Cerrado | 20.7 |
| 5693373a-3168-31fa-8444-f614c3c0d6b6 | -15.77017 | -56.44481 | 2026-08-28 17:26:00 | NPP-375 | NOSSA SENHORA DO LIVRAMENTO | MATO GROSSO | Brasil | 5106109 | 51 | 33 | nan | nan | nan | Cerrado | 5.2 |
| 56d73f8d-f2d0-3bd6-95c0-c9574dd3f712 | -14.46553 | -58.51677 | 2026-08-28 17:26:00 | NPP-375 | TANGARÁ DA SERRA | MATO GROSSO | Brasil | 5107958 | 51 | 33 | nan | nan | nan | Cerrado | 15.9 |
| 0013fefb-becc-3120-8247-86b8d4ac1b7f | -14.90312 | -56.32312 | 2026-08-28 17:26:00 | NPP-375 | ROSÁRIO OESTE | MATO GROSSO | Brasil | 5107701 | 51 | 33 | nan | nan | nan | Cerrado | 5.7 |
| cb677933-af9a-3ed1-9e39-003e5aa6f24f | -15.4679 | -53.96669 | 2026-08-28 17:26:00 | NPP-375 | POXORÉU | MATO GROSSO | Brasil | 5107008 | 51 | 33 | nan | nan | nan | Cerrado | 18.1 |
| 2da9729a-1483-31e5-ab58-bb3407bc6c75 | -9.69557 | -46.55341 | 2026-08-28 17:26:00 | NPP-375 | ALTO PARNAÍBA | MARANHÃO | Brasil | 2100501 | 21 | 33 | nan | nan | nan | Cerrado | 28.4 |
| 4fe40cdf-f7c8-369b-b00d-f47f9052fa45 | -11.48148 | -46.939 | 2026-08-28 17:26:00 | NPP-375 | DIANÓPOLIS | TOCANTINS | Brasil | 1707009 | 17 | 33 | nan | nan | nan | Cerrado | 7.4 |
| 839f841a-1b8f-3415-b845-4894186424a1 | -11.71259 | -54.54375 | 2026-08-28 17:26:00 | NPP-375 | UNIÃO DO SUL | MATO GROSSO | Brasil | 5108303 | 51 | 33 | nan | nan | nan | Amazônia | 7.0 |
| 8ebe8b09-769a-3fce-9a75-edea9995bff3 | -11.65738 | -46.72667 | 2026-08-28 17:26:00 | NPP-375 | DIANÓPOLIS | TOCANTINS | Brasil | 1707009 | 17 | 33 | nan | nan | nan | Cerrado | 5.6 |
| ec75c0ef-d10a-3f2d-8043-4c196245cd50 | -13.87918 | -54.11584 | 2026-08-28 17:26:00 | NPP-375 | PARANATINGA | MATO GROSSO | Brasil | 5106307 | 51 | 33 | nan | nan | nan | Cerrado | 4.8 |
| 7b978c93-14f7-3ad1-a958-2f5f553af9d1 | -11.00818 | -49.6519 | 2026-08-28 17:26:00 | NPP-375 | SANTA RITA DO TOCANTINS | TOCANTINS | Brasil | 1718899 | 17 | 33 | nan | nan | nan | Cerrado | 14.6 |
| b9000cc8-9170-39ce-bc02-c913ddb994f0 | -14.80878 | -43.55922 | 2026-08-28 17:26:00 | NPP-375 | MATIAS CARDOSO | MINAS GERAIS | Brasil | 3140852 | 31 | 33 | nan | nan | nan | Cerrado | 8.1 |
| 26fd24de-b789-343a-b152-5fba1febfeb9 | -14.63392 | -57.00747 | 2026-08-28 17:26:00 | NPP-375 | DENISE | MATO GROSSO | Brasil | 5103452 | 51 | 33 | nan | nan | nan | Amazônia | 22.6 |
| d1eb9767-d9bd-3bfd-9611-4d2068e0ac34 | -14.19597 | -52.84904 | 2026-08-28 17:26:00 | NPP-375 | ÁGUA BOA | MATO GROSSO | Brasil | 5100201 | 51 | 33 | nan | nan | nan | Cerrado | 14.1 |
| 9204ba6d-c3b6-37a4-8397-793c666d0aa4 | -11.79983 | -47.66801 | 2026-08-28 17:26:00 | NPP-375 | NATIVIDADE | TOCANTINS | Brasil | 1714203 | 17 | 33 | nan | nan | nan | Cerrado | 18.2 |
| c27eff61-adff-3106-a9e8-f97b8bbeed6c | -14.87794 | -52.60304 | 2026-08-28 17:26:00 | NPP-375 | NOVA XAVANTINA | MATO GROSSO | Brasil | 5106257 | 51 | 33 | nan | nan | nan | Cerrado | 9.7 |
| 51b489e0-3d89-3ec2-9ac1-525fb96b8c53 | -9.69625 | -46.55698 | 2026-08-28 17:26:00 | NPP-375 | ALTO PARNAÍBA | MARANHÃO | Brasil | 2100501 | 21 | 33 | nan | nan | nan | Cerrado | 28.4 |
| 185c7e6e-c7b9-31e9-a42c-3f0343f4caa3 | -11.26945 | -54.01063 | 2026-08-28 17:26:00 | NPP-375 | UNIÃO DO SUL | MATO GROSSO | Brasil | 5108303 | 51 | 33 | nan | nan | nan | Amazônia | 13.5 |
| 20017baf-8b26-3a07-9b0c-2bdb8152cd00 | -11.01759 | -49.65475 | 2026-08-28 17:26:00 | NPP-375 | SANTA RITA DO TOCANTINS | TOCANTINS | Brasil | 1718899 | 17 | 33 | nan | nan | nan | Cerrado | 9.6 |
| e30a8d5d-2ee3-3bff-bfa3-d288ea30c77c | -11.00505 | -49.63505 | 2026-08-28 17:26:00 | NPP-375 | SANTA RITA DO TOCANTINS | TOCANTINS | Brasil | 1718899 | 17 | 33 | nan | nan | nan | Cerrado | 7.2 |
| e80ba3bd-bc43-3559-8ba7-f4255eccd5fb | -10.29449 | -49.95083 | 2026-08-28 17:26:00 | NPP-375 | PIUM | TOCANTINS | Brasil | 1717503 | 17 | 33 | nan | nan | nan | Cerrado | 5.3 |
| 88b605af-b6f0-36f1-ab16-943a66de4b14 | -11.203 | -55.09583 | 2026-08-28 17:26:00 | NPP-375 | ITAÚBA | MATO GROSSO | Brasil | 5104559 | 51 | 33 | nan | nan | nan | Amazônia | 3.1 |
| a51043a7-1d8e-36f9-8ba6-5da2c42c45e9 | -11.22583 | -45.04528 | 2026-08-28 17:26:00 | NPP-375 | FORMOSA DO RIO PRETO | BAHIA | Brasil | 2911105 | 29 | 33 | nan | nan | nan | Cerrado | 10.0 |
| 761ffad9-7c80-3ca4-8e62-f13e06fcd4d8 | -15.09918 | -48.15314 | 2026-08-28 17:26:00 | NPP-375 | MIMOSO DE GOIÁS | GOIÁS | Brasil | 5213053 | 52 | 33 | nan | nan | nan | Cerrado | 2.9 |
| 90696de1-545d-3a38-b2fe-8b3fb0ae6225 | -11.24511 | -45.06951 | 2026-08-28 17:26:00 | NPP-375 | FORMOSA DO RIO PRETO | BAHIA | Brasil | 2911105 | 29 | 33 | nan | nan | nan | Cerrado | 9.8 |
| c71e35fe-00e7-354a-97ff-f10675901edb | -13.64788 | -49.01462 | 2026-08-28 17:26:00 | NPP-375 | SANTA TEREZA DE GOIÁS | GOIÁS | Brasil | 5219605 | 52 | 33 | nan | nan | nan | Cerrado | 3.0 |
| d983a609-3a14-3eb1-80f9-21e1fc6edab6 | -16.92194 | -46.63669 | 2026-08-28 17:26:00 | NPP-375 | PARACATU | MINAS GERAIS | Brasil | 3147006 | 31 | 33 | nan | nan | nan | Cerrado | 9.2 |


[Clique aqui para ver as próximas entradas](README106.md)
