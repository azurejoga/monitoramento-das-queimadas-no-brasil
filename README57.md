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

## Dados Diários - Página 57

| ID | Latitude | Longitude | Data/Hora GMT | Satélite | Município | Estado | País | Município ID | Estado ID | País ID | Dias sem Chuva | Precipitação | Risco de Fogo | Bioma | FRP |
|----|----------|-----------|---------------|----------|-----------|--------|------|--------------|-----------|---------|----------------|--------------|----------------|-------|-----|
| 45cc6fc8-9496-3733-a094-e259e6f03904 | -23.71394 | -47.39994 | 2025-09-12 04:08:00 | NPP-375D | PIEDADE | SÃO PAULO | Brasil | 3537800 | 35 | 33 | nan | nan | nan | Mata Atlântica | 0.7 |
| 0adfa518-1656-3b8a-ae4c-610b0561d239 | -21.95196 | -47.54615 | 2025-09-12 04:08:00 | NPP-375D | DESCALVADO | SÃO PAULO | Brasil | 3513702 | 35 | 33 | nan | nan | nan | Cerrado | 0.9 |
| 49c43932-39c6-38cd-a4db-c1d0971e9046 | -19.99128 | -47.6377 | 2025-09-12 04:08:00 | NPP-375D | CONQUISTA | MINAS GERAIS | Brasil | 3118205 | 31 | 33 | nan | nan | nan | Cerrado | 1.3 |
| a934b654-00ed-3aa3-9e3e-2e33b21477f4 | -17.83196 | -52.05244 | 2025-09-12 04:08:00 | NPP-375D | JATAÍ | GOIÁS | Brasil | 5211909 | 52 | 33 | nan | nan | nan | Cerrado | 2.0 |
| f1952c83-74ec-3839-b53e-796cbf78f32f | -18.65253 | -47.65474 | 2025-09-12 04:08:00 | NPP-375D | ESTRELA DO SUL | MINAS GERAIS | Brasil | 3124807 | 31 | 33 | nan | nan | nan | Cerrado | 2.8 |
| b24dceb4-1c93-366a-9868-3031f16e4a97 | -23.12174 | -47.48754 | 2025-09-12 04:08:00 | NPP-375D | PORTO FELIZ | SÃO PAULO | Brasil | 3540606 | 35 | 33 | nan | nan | nan | Mata Atlântica | 0.7 |
| 3576de7f-c4ca-39a9-9057-eb454348a0c0 | -22.61069 | -47.28606 | 2025-09-12 04:08:00 | NPP-375D | LIMEIRA | SÃO PAULO | Brasil | 3526902 | 35 | 33 | nan | nan | nan | Cerrado | 1.3 |
| 81b130d7-0d78-3434-b395-83e6e3e4e3ca | -21.95397 | -47.55629 | 2025-09-12 04:08:00 | NPP-375D | DESCALVADO | SÃO PAULO | Brasil | 3513702 | 35 | 33 | nan | nan | nan | Cerrado | 3.2 |
| fe4f0d48-59ff-3664-b542-7139703b4091 | -23.19292 | -49.65021 | 2025-09-12 04:08:00 | NPP-375D | TIMBURI | SÃO PAULO | Brasil | 3554607 | 35 | 33 | nan | nan | nan | Mata Atlântica | 2.1 |
| d82e434f-26f5-338b-96f8-fd2e448ed7f9 | -17.37328 | -52.92421 | 2025-09-12 04:08:00 | NPP-375D | MINEIROS | GOIÁS | Brasil | 5213103 | 52 | 33 | nan | nan | nan | Cerrado | 2.0 |
| 81642026-49bb-3c1d-ad56-96ead74dd870 | -21.42883 | -45.47177 | 2025-09-12 04:08:00 | NPP-375D | TRÊS PONTAS | MINAS GERAIS | Brasil | 3169406 | 31 | 33 | nan | nan | nan | Mata Atlântica | 0.9 |
| a2f96591-c97f-3a23-b7f9-23e7241c776b | -23.54597 | -47.59952 | 2025-09-12 04:08:00 | NPP-375D | ARAÇOIABA DA SERRA | SÃO PAULO | Brasil | 3502903 | 35 | 33 | nan | nan | nan | Mata Atlântica | 0.6 |
| 59f68261-02cf-31b5-a528-6a0d6b5f27bd | -19.99416 | -47.64376 | 2025-09-12 04:08:00 | NPP-375D | CONQUISTA | MINAS GERAIS | Brasil | 3118205 | 31 | 33 | nan | nan | nan | Cerrado | 4.5 |
| dee08826-011f-3251-a39d-64efb20bca5e | -19.99804 | -47.64438 | 2025-09-12 04:08:00 | NPP-375D | CONQUISTA | MINAS GERAIS | Brasil | 3118205 | 31 | 33 | nan | nan | nan | Cerrado | 4.5 |
| dd2fc37d-e148-31e8-9024-15bc294b090f | -23.64402 | -47.05978 | 2025-09-12 04:08:00 | NPP-375D | COTIA | SÃO PAULO | Brasil | 3513009 | 35 | 33 | nan | nan | nan | Mata Atlântica | 0.4 |
| 7c0ec283-7a00-3fb4-b27b-df159ac51b6d | -18.45007 | -49.56331 | 2025-09-12 04:08:00 | NPP-375D | CACHOEIRA DOURADA | GOIÁS | Brasil | 5204250 | 52 | 33 | nan | nan | nan | Mata Atlântica | 2.2 |
| 659b61da-09d7-355c-98ab-5fc1317948d5 | -23.34941 | -47.19646 | 2025-09-12 04:08:00 | NPP-375D | ITU | SÃO PAULO | Brasil | 3523909 | 35 | 33 | nan | nan | nan | Mata Atlântica | 2.6 |
| 10083b57-2c30-3e8e-b2fa-b93fbcda9ca3 | -19.30809 | -47.50335 | 2025-09-12 04:08:00 | NPP-375D | SANTA JULIANA | MINAS GERAIS | Brasil | 3157708 | 31 | 33 | nan | nan | nan | Cerrado | 1.6 |
| 771c11e2-66b5-3c10-92b5-fb2e7670c02d | -23.31113 | -47.3475 | 2025-09-12 04:08:00 | NPP-375D | ITU | SÃO PAULO | Brasil | 3523909 | 35 | 33 | nan | nan | nan | Mata Atlântica | 0.8 |
| e68668c8-fe1d-38ab-a3d4-96922f48a5f2 | -21.26054 | -45.45762 | 2025-09-12 04:08:00 | NPP-375D | SANTANA DA VARGEM | MINAS GERAIS | Brasil | 3158300 | 31 | 33 | nan | nan | nan | Mata Atlântica | 0.6 |
| ade2a561-eee7-3e1e-a318-309114495e58 | -23.35012 | -47.15068 | 2025-09-12 04:08:00 | NPP-375D | ITU | SÃO PAULO | Brasil | 3523909 | 35 | 33 | nan | nan | nan | Mata Atlântica | 0.8 |
| c1925e1e-efed-309d-8681-49152e7da852 | -20.35092 | -48.39914 | 2025-09-12 04:08:00 | NPP-375D | GUAÍRA | SÃO PAULO | Brasil | 3517406 | 35 | 33 | nan | nan | nan | Cerrado | 0.8 |
| d26e4d48-27e6-3161-b3c6-931e8dc9ae13 | -21.18009 | -54.97125 | 2025-09-12 04:08:00 | NPP-375D | SIDROLÂNDIA | MATO GROSSO DO SUL | Brasil | 5007901 | 50 | 33 | nan | nan | nan | Cerrado | 0.4 |
| ee43332b-2f42-3962-b45a-4139f0cc7b00 | -22.35574 | -47.54773 | 2025-09-12 04:08:00 | NPP-375D | RIO CLARO | SÃO PAULO | Brasil | 3543907 | 35 | 33 | nan | nan | nan | Mata Atlântica | 1.2 |
| 5126f92f-5657-3a3f-8a84-572ab4e2b2b6 | -20.03824 | -41.74878 | 2025-09-12 04:08:00 | NPP-375D | SÃO JOSÉ DO MANTIMENTO | MINAS GERAIS | Brasil | 3163607 | 31 | 33 | nan | nan | nan | Mata Atlântica | 4.1 |
| 95b388f1-8e39-3a8e-b535-7709e2542760 | -23.34941 | -47.23834 | 2025-09-12 04:08:00 | NPP-375D | ITU | SÃO PAULO | Brasil | 3523909 | 35 | 33 | nan | nan | nan | Mata Atlântica | 2.6 |
| ffe18d57-1bbc-3cc8-9916-a853a52c4c55 | -20.55504 | -46.35732 | 2025-09-12 04:08:00 | NPP-375D | SÃO JOÃO BATISTA DO GLÓRIA | MINAS GERAIS | Brasil | 3162203 | 31 | 33 | nan | nan | nan | Cerrado | 0.4 |
| 6a24d6a2-8209-38cd-ad92-905ea57c622e | -20.1609 | -46.59635 | 2025-09-12 04:08:00 | NPP-375D | SÃO ROQUE DE MINAS | MINAS GERAIS | Brasil | 3164308 | 31 | 33 | nan | nan | nan | Cerrado | 1.1 |
| e5d722ce-d18f-3561-9e7d-078339a6ceb3 | -18.87772 | -48.12239 | 2025-09-12 04:08:00 | NPP-375D | UBERLÂNDIA | MINAS GERAIS | Brasil | 3170206 | 31 | 33 | nan | nan | nan | Cerrado | 0.7 |
| d379b9f1-d853-3e41-b525-0b5b328ff6c5 | -19.75497 | -46.09382 | 2025-09-12 04:08:00 | NPP-375D | CÓRREGO DANTA | MINAS GERAIS | Brasil | 3119807 | 31 | 33 | nan | nan | nan | Cerrado | 1.0 |
| 0c88bc3d-da5e-3a54-ae5f-24799a2101ec | -20.08192 | -44.47751 | 2025-09-12 04:08:00 | NPP-375D | ITAÚNA | MINAS GERAIS | Brasil | 3133808 | 31 | 33 | nan | nan | nan | Mata Atlântica | 2.6 |
| 73fa7cab-88d0-3b05-bd62-20f4b3e3b6bf | -18.31544 | -52.07418 | 2025-09-12 04:08:00 | NPP-375D | SERRANÓPOLIS | GOIÁS | Brasil | 5220504 | 52 | 33 | nan | nan | nan | Cerrado | 0.3 |
| 0c1fedcb-b31a-3606-9688-19d7d972392b | -19.86653 | -44.93156 | 2025-09-12 04:08:00 | NPP-375D | NOVA SERRANA | MINAS GERAIS | Brasil | 3145208 | 31 | 33 | nan | nan | nan | Cerrado | 0.8 |
| d4a15647-4bc8-3852-b030-d8b779ef2743 | -21.32318 | -45.00274 | 2025-09-12 04:08:00 | NPP-375D | LAVRAS | MINAS GERAIS | Brasil | 3138203 | 31 | 33 | nan | nan | nan | Mata Atlântica | 1.8 |
| de71fb09-1165-38e0-b968-7ef56595db34 | -17.83127 | -52.05576 | 2025-09-12 04:08:00 | NPP-375D | JATAÍ | GOIÁS | Brasil | 5211909 | 52 | 33 | nan | nan | nan | Cerrado | 2.6 |
| bb1b34f4-0512-31dc-ad8a-fed4dd8c85a8 | -24.68917 | -48.95684 | 2025-09-12 04:08:00 | NPP-375D | ADRIANÓPOLIS | PARANÁ | Brasil | 4100202 | 41 | 33 | nan | nan | nan | Mata Atlântica | 0.9 |
| f7e7e8be-182b-32f9-b3ce-0ad360046332 | -19.66337 | -44.90614 | 2025-09-12 04:08:00 | NPP-375D | PITANGUI | MINAS GERAIS | Brasil | 3151404 | 31 | 33 | nan | nan | nan | Mata Atlântica | 1.6 |
| 1f6603c0-144c-32ad-8fb4-8e3e2e16799c | -22.78152 | -47.12484 | 2025-09-12 04:08:00 | NPP-375D | PAULÍNIA | SÃO PAULO | Brasil | 3536505 | 35 | 33 | nan | nan | nan | Cerrado | 2.1 |
| a685c1b3-2d00-3477-abb9-5323109d276f | -20.01059 | -47.6414 | 2025-09-12 04:08:00 | NPP-375D | CONQUISTA | MINAS GERAIS | Brasil | 3118205 | 31 | 33 | nan | nan | nan | Cerrado | 4.2 |
| d4f8d34f-766b-38c8-bbc6-8b8b6fc35dba | -20.2668 | -42.12752 | 2025-09-12 04:08:00 | NPP-375D | MANHUAÇU | MINAS GERAIS | Brasil | 3139409 | 31 | 33 | nan | nan | nan | Mata Atlântica | 8.9 |
| 2967d859-5c2d-3974-9767-cebd290e67ec | -22.19004 | -49.59433 | 2025-09-12 04:08:00 | NPP-375D | GARÇA | SÃO PAULO | Brasil | 3516705 | 35 | 33 | nan | nan | nan | Mata Atlântica | 1.5 |
| 1572bc93-cc22-3b19-8e75-aed08db248f9 | -20.26623 | -42.13125 | 2025-09-12 04:08:00 | NPP-375D | MANHUAÇU | MINAS GERAIS | Brasil | 3139409 | 31 | 33 | nan | nan | nan | Mata Atlântica | 3.4 |
| 60ad16fe-de16-3180-8af7-211e4e83bce6 | -19.99901 | -47.6391 | 2025-09-12 04:08:00 | NPP-375D | CONQUISTA | MINAS GERAIS | Brasil | 3118205 | 31 | 33 | nan | nan | nan | Cerrado | 2.0 |
| 53622857-c4a1-31d7-8ccb-25215e2f1613 | -20.00872 | -47.65158 | 2025-09-12 04:08:00 | NPP-375D | CONQUISTA | MINAS GERAIS | Brasil | 3118205 | 31 | 33 | nan | nan | nan | Cerrado | 2.4 |
| c209984d-d1b8-3ca4-92ff-1cbfc65b1b55 | -21.94366 | -47.54927 | 2025-09-12 04:08:00 | NPP-375D | DESCALVADO | SÃO PAULO | Brasil | 3513702 | 35 | 33 | nan | nan | nan | Cerrado | 1.2 |
| d9caab04-7051-3ba1-b6cd-aa3419e46550 | -23.14144 | -48.25396 | 2025-09-12 04:08:00 | NPP-375D | BOFETE | SÃO PAULO | Brasil | 3506904 | 35 | 33 | nan | nan | nan | Mata Atlântica | 5.4 |
| 011a5952-380e-326c-9ebd-190420e24306 | -18.76333 | -48.19805 | 2025-09-12 04:08:00 | NPP-375D | UBERLÂNDIA | MINAS GERAIS | Brasil | 3170206 | 31 | 33 | nan | nan | nan | Cerrado | 2.1 |
| 51a5da08-b47a-387f-815f-f9096022e935 | -23.12008 | -47.49686 | 2025-09-12 04:08:00 | NPP-375D | PORTO FELIZ | SÃO PAULO | Brasil | 3540606 | 35 | 33 | nan | nan | nan | Mata Atlântica | 1.0 |
| 190b50c5-e7f2-3f3f-aae2-4202beeca49a | -21.33691 | -45.02534 | 2025-09-12 04:08:00 | NPP-375D | LAVRAS | MINAS GERAIS | Brasil | 3138203 | 31 | 33 | nan | nan | nan | Mata Atlântica | 3.9 |
| d307ea4a-ab98-30e4-acbe-463ffa7a60fa | -19.96604 | -41.60534 | 2025-09-12 04:08:00 | NPP-375D | MUTUM | MINAS GERAIS | Brasil | 3144003 | 31 | 33 | nan | nan | nan | Mata Atlântica | 1.2 |
| 6216a0fa-ec3b-391b-a287-70cbd25cbfbf | -22.2611 | -49.56346 | 2025-09-12 04:08:00 | NPP-375D | GÁLIA | SÃO PAULO | Brasil | 3516606 | 35 | 33 | nan | nan | nan | Mata Atlântica | 1.0 |
| d4ae3e9b-a34c-321b-95d3-5b2b835337cd | -22.79388 | -47.80306 | 2025-09-12 04:08:00 | NPP-375D | PIRACICABA | SÃO PAULO | Brasil | 3538709 | 35 | 33 | nan | nan | nan | Cerrado | 2.2 |
| f80d4d87-32e5-358e-86b6-a6e311479bcd | -23.30007 | -46.55046 | 2025-09-12 04:08:00 | NPP-375D | MAIRIPORÃ | SÃO PAULO | Brasil | 3528502 | 35 | 33 | nan | nan | nan | Mata Atlântica | 3.3 |
| 9261bad0-db4c-39c8-8994-483af236d2e2 | -24.12045 | -48.70739 | 2025-09-12 04:08:00 | NPP-375D | ITAPEVA | SÃO PAULO | Brasil | 3522406 | 35 | 33 | nan | nan | nan | Mata Atlântica | 5.9 |
| 753634d1-ef8d-3188-acbc-3f990c42862a | -18.84012 | -46.84722 | 2025-09-12 04:08:00 | NPP-375D | PATROCÍNIO | MINAS GERAIS | Brasil | 3148103 | 31 | 33 | nan | nan | nan | Cerrado | 1.0 |
| bf4d068b-2e0e-3943-921f-8bec36f32279 | -21.33155 | -45.03641 | 2025-09-12 04:08:00 | NPP-375D | LAVRAS | MINAS GERAIS | Brasil | 3138203 | 31 | 33 | nan | nan | nan | Mata Atlântica | 1.0 |
| 9707f930-481c-3347-a5fc-ae2aaef93ab5 | -20.11755 | -42.35149 | 2025-09-12 04:08:00 | NPP-375D | RAUL SOARES | MINAS GERAIS | Brasil | 3154002 | 31 | 33 | nan | nan | nan | Mata Atlântica | 1.4 |
| 6f3410b6-1399-39ad-8755-4fbb8797fa3e | -20.57605 | -44.36371 | 2025-09-12 04:08:00 | NPP-375D | PIRACEMA | MINAS GERAIS | Brasil | 3150604 | 31 | 33 | nan | nan | nan | Mata Atlântica | 1.2 |
| 93966a04-21d3-3d6c-8553-b8df4e8c6970 | -23.30656 | -46.61673 | 2025-09-12 04:08:00 | NPP-375D | MAIRIPORÃ | SÃO PAULO | Brasil | 3528502 | 35 | 33 | nan | nan | nan | Mata Atlântica | 1.8 |
| b9f56bdb-e91d-3b44-826b-7c0844418cda | -23.1357 | -47.15614 | 2025-09-12 04:08:00 | NPP-375D | INDAIATUBA | SÃO PAULO | Brasil | 3520509 | 35 | 33 | nan | nan | nan | Mata Atlântica | 9.3 |
| d6f8f171-c93b-3321-8aa0-0f922bb31b6c | -21.33834 | -45.03772 | 2025-09-12 04:08:00 | NPP-375D | LAVRAS | MINAS GERAIS | Brasil | 3138203 | 31 | 33 | nan | nan | nan | Mata Atlântica | 1.9 |
| 4412744b-7e6d-3bfa-9eac-11e1f0bc8703 | -21.94848 | -47.56511 | 2025-09-12 04:08:00 | NPP-375D | DESCALVADO | SÃO PAULO | Brasil | 3513702 | 35 | 33 | nan | nan | nan | Cerrado | 1.6 |
| 8ce65dad-0b44-3415-aa23-4c18499c79e8 | -21.91891 | -47.91801 | 2025-09-12 04:08:00 | NPP-375D | SÃO CARLOS | SÃO PAULO | Brasil | 3548906 | 35 | 33 | nan | nan | nan | Cerrado | 1.1 |
| 36506247-9e15-3f03-9d35-0b3442a7ba43 | -21.18459 | -45.1182 | 2025-09-12 04:08:00 | NPP-375D | LAVRAS | MINAS GERAIS | Brasil | 3138203 | 31 | 33 | nan | nan | nan | Mata Atlântica | 0.5 |
| b385c28b-0fdc-3760-bb4f-0434f61b7e52 | -19.19043 | -48.01196 | 2025-09-12 04:08:00 | NPP-375D | UBERLÂNDIA | MINAS GERAIS | Brasil | 3170206 | 31 | 33 | nan | nan | nan | Cerrado | 15.7 |
| 69486277-8fe3-33ec-8882-ba44d4a2ba0f | -19.24497 | -48.0359 | 2025-09-12 04:08:00 | NPP-375D | UBERABA | MINAS GERAIS | Brasil | 3170107 | 31 | 33 | nan | nan | nan | Cerrado | 5.8 |
| 15a5cae6-1729-399c-bb93-8b629ce545d0 | -20.65184 | -46.53139 | 2025-09-12 04:08:00 | NPP-375D | SÃO JOÃO BATISTA DO GLÓRIA | MINAS GERAIS | Brasil | 3162203 | 31 | 33 | nan | nan | nan | Cerrado | 0.5 |
| 97db6f5e-17a9-3e0d-8e37-8ef2d0ea7478 | -23.73113 | -47.22219 | 2025-09-12 04:08:00 | NPP-375D | IBIÚNA | SÃO PAULO | Brasil | 3519709 | 35 | 33 | nan | nan | nan | Mata Atlântica | 0.4 |
| 3ad55d8b-cc9b-3043-bf26-9dfdaf9019d3 | -18.68211 | -47.67158 | 2025-09-12 04:08:00 | NPP-375D | ESTRELA DO SUL | MINAS GERAIS | Brasil | 3124807 | 31 | 33 | nan | nan | nan | Cerrado | 2.9 |
| eab3e445-4e01-3d78-a0ee-5de2d93c2532 | -20.00773 | -47.65704 | 2025-09-12 04:08:00 | NPP-375D | CONQUISTA | MINAS GERAIS | Brasil | 3118205 | 31 | 33 | nan | nan | nan | Cerrado | 3.8 |
| e419a813-48da-3feb-ae02-50dde1952b3b | -20.26288 | -42.13065 | 2025-09-12 04:08:00 | NPP-375D | MANHUAÇU | MINAS GERAIS | Brasil | 3139409 | 31 | 33 | nan | nan | nan | Mata Atlântica | 3.4 |
| 8aa197c1-046c-3604-911e-b6cd9cc52690 | -19.23599 | -48.03959 | 2025-09-12 04:08:00 | NPP-375D | UBERLÂNDIA | MINAS GERAIS | Brasil | 3170206 | 31 | 33 | nan | nan | nan | Cerrado | 13.1 |
| e39ba486-ab85-37ce-b1d0-8b2c618df518 | -22.5275 | -45.09736 | 2025-09-12 04:08:00 | NPP-375D | CRUZEIRO | SÃO PAULO | Brasil | 3513405 | 35 | 33 | nan | nan | nan | Mata Atlântica | 3.5 |
| 0bb241d8-9367-3f12-90a5-31de42122ef7 | -19.30795 | -47.50154 | 2025-09-12 04:08:00 | NPP-375D | SANTA JULIANA | MINAS GERAIS | Brasil | 3157708 | 31 | 33 | nan | nan | nan | Cerrado | 0.9 |
| 8e0b8ee5-8cd5-3db3-858e-685f68ca4acb | -20.39862 | -42.19585 | 2025-09-12 04:08:00 | NPP-375D | SANTA MARGARIDA | MINAS GERAIS | Brasil | 3157906 | 31 | 33 | nan | nan | nan | Mata Atlântica | 0.9 |
| 4c2aba27-d2b9-31f0-b9c6-507c43cb4ca3 | -21.95311 | -47.56101 | 2025-09-12 04:08:00 | NPP-375D | DESCALVADO | SÃO PAULO | Brasil | 3513702 | 35 | 33 | nan | nan | nan | Cerrado | 1.6 |
| fc574c54-3871-3cbf-ac30-a22368000963 | -20.35021 | -48.40284 | 2025-09-12 04:08:00 | NPP-375D | GUAÍRA | SÃO PAULO | Brasil | 3517406 | 35 | 33 | nan | nan | nan | Cerrado | 0.8 |
| 3b8055e6-6979-3020-a8b7-590b78854521 | -22.84807 | -47.33836 | 2025-09-12 04:08:00 | NPP-375D | SUMARÉ | SÃO PAULO | Brasil | 3552403 | 35 | 33 | nan | nan | nan | Mata Atlântica | 0.8 |
| aea71ebc-f2aa-37a8-87dc-53df09744117 | -18.77574 | -48.53957 | 2025-09-12 04:08:00 | NPP-375D | TUPACIGUARA | MINAS GERAIS | Brasil | 3169604 | 31 | 33 | nan | nan | nan | Cerrado | 3.8 |
| 44441c28-ae7f-3f1d-8d1e-cd5d27543b9a | -18.68603 | -47.67253 | 2025-09-12 04:08:00 | NPP-375D | ESTRELA DO SUL | MINAS GERAIS | Brasil | 3124807 | 31 | 33 | nan | nan | nan | Cerrado | 0.8 |
| 5236bcb5-5cfb-30e4-8f91-8ccff9a39e46 | -23.35457 | -47.18843 | 2025-09-12 04:08:00 | NPP-375D | ITU | SÃO PAULO | Brasil | 3523909 | 35 | 33 | nan | nan | nan | Mata Atlântica | 0.8 |
| d12a1c29-c3aa-3ff7-a898-12bc7a3b3f1b | -23.10381 | -47.50296 | 2025-09-12 04:08:00 | NPP-375D | PORTO FELIZ | SÃO PAULO | Brasil | 3540606 | 35 | 33 | nan | nan | nan | Mata Atlântica | 0.7 |
| b8357465-263f-37c9-99eb-85b2d1bed496 | -21.19555 | -47.5216 | 2025-09-12 04:08:00 | NPP-375D | ALTINÓPOLIS | SÃO PAULO | Brasil | 3501004 | 35 | 33 | nan | nan | nan | Cerrado | 17.2 |
| f544dbb2-b9ac-3084-9361-9dbd6cb9b9a6 | -20.8094 | -46.88864 | 2025-09-12 04:08:00 | NPP-375D | PRATÁPOLIS | MINAS GERAIS | Brasil | 3152907 | 31 | 33 | nan | nan | nan | Mata Atlântica | 1.3 |
| 4d38093c-8ba6-34da-90c1-07677d252547 | -18.65546 | -47.66096 | 2025-09-12 04:08:00 | NPP-375D | ESTRELA DO SUL | MINAS GERAIS | Brasil | 3124807 | 31 | 33 | nan | nan | nan | Cerrado | 2.7 |
| 53b4fad1-11e0-32bd-9c73-2ec251873f2f | -22.61115 | -46.41531 | 2025-09-12 04:08:00 | NPP-375D | SOCORRO | SÃO PAULO | Brasil | 3552106 | 35 | 33 | nan | nan | nan | Mata Atlântica | 0.8 |
| 42b2a698-fd7d-384c-940b-3f98d4430a79 | -20.69841 | -46.07634 | 2025-09-12 04:08:00 | NPP-375D | GUAPÉ | MINAS GERAIS | Brasil | 3128105 | 31 | 33 | nan | nan | nan | Cerrado | 1.8 |
| d2cc1e53-1155-31db-bad0-cf4d3aa55d0d | -22.61398 | -46.41997 | 2025-09-12 04:08:00 | NPP-375D | SOCORRO | SÃO PAULO | Brasil | 3552106 | 35 | 33 | nan | nan | nan | Mata Atlântica | 3.3 |
| bc99dee7-a49c-33e0-bc0f-a3e07ee69e38 | -21.95568 | -47.54694 | 2025-09-12 04:08:00 | NPP-375D | DESCALVADO | SÃO PAULO | Brasil | 3513702 | 35 | 33 | nan | nan | nan | Cerrado | 0.9 |
| 1c348c2d-fd98-3fa1-b674-57b5599f4962 | -19.95163 | -44.46129 | 2025-09-12 04:08:00 | NPP-375D | MATEUS LEME | MINAS GERAIS | Brasil | 3140704 | 31 | 33 | nan | nan | nan | Mata Atlântica | 1.6 |
| c56c2efb-92aa-3d97-a671-05b2f44ace9b | -23.10912 | -47.49449 | 2025-09-12 04:08:00 | NPP-375D | PORTO FELIZ | SÃO PAULO | Brasil | 3540606 | 35 | 33 | nan | nan | nan | Mata Atlântica | 2.3 |
| 1920a824-68d0-32a8-86d4-35d70b37632e | -22.22676 | -49.60633 | 2025-09-12 04:08:00 | NPP-375D | GARÇA | SÃO PAULO | Brasil | 3516705 | 35 | 33 | nan | nan | nan | Mata Atlântica | 1.1 |
| c3037217-a0b6-3906-aec2-0b5f79c2bf79 | -23.35371 | -47.15141 | 2025-09-12 04:08:00 | NPP-375D | ITU | SÃO PAULO | Brasil | 3523909 | 35 | 33 | nan | nan | nan | Mata Atlântica | 0.8 |
| 7ad6c78e-c89a-388b-a668-598536057ffd | -21.33208 | -45.01229 | 2025-09-12 04:08:00 | NPP-375D | LAVRAS | MINAS GERAIS | Brasil | 3138203 | 31 | 33 | nan | nan | nan | Mata Atlântica | 0.7 |
| 21fa7b97-a7e9-33f2-a181-d87ba3b52e66 | -19.06848 | -48.73586 | 2025-09-12 04:08:00 | NPP-375D | MONTE ALEGRE DE MINAS | MINAS GERAIS | Brasil | 3142809 | 31 | 33 | nan | nan | nan | Cerrado | 1.2 |
| 35b36cdc-ad72-349c-be82-51b329a563c7 | -23.49106 | -47.2644 | 2025-09-12 04:08:00 | NPP-375D | MAIRINQUE | SÃO PAULO | Brasil | 3528403 | 35 | 33 | nan | nan | nan | Mata Atlântica | 1.8 |
| bc78aa2e-15de-3e92-acca-06c8c630f757 | -20.00065 | -44.22898 | 2025-09-12 04:08:00 | NPP-375D | BETIM | MINAS GERAIS | Brasil | 3106705 | 31 | 33 | nan | nan | nan | Mata Atlântica | 3.7 |
| 07f147cf-43af-3ba7-8e46-7e332ba270e1 | -21.32529 | -45.01103 | 2025-09-12 04:08:00 | NPP-375D | LAVRAS | MINAS GERAIS | Brasil | 3138203 | 31 | 33 | nan | nan | nan | Mata Atlântica | 2.7 |
| ea2510e0-050a-33a3-b262-7577dd15db47 | -17.80236 | -50.00308 | 2025-09-12 04:08:00 | NPP-375D | GOIATUBA | GOIÁS | Brasil | 5209101 | 52 | 33 | nan | nan | nan | Cerrado | 1.4 |
| 4ca36de3-7f4b-3b82-ae61-d2958187cf7b | -19.05793 | -48.33859 | 2025-09-12 04:08:00 | NPP-375D | UBERLÂNDIA | MINAS GERAIS | Brasil | 3170206 | 31 | 33 | nan | nan | nan | Cerrado | 2.9 |


[Clique aqui para ver as próximas entradas](README58.md)
