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

## Dados Diários - Página 51

| ID | Latitude | Longitude | Data/Hora GMT | Satélite | Município | Estado | País | Município ID | Estado ID | País ID | Dias sem Chuva | Precipitação | Risco de Fogo | Bioma | FRP |
|----|----------|-----------|---------------|----------|-----------|--------|------|--------------|-----------|---------|----------------|--------------|----------------|-------|-----|
| fb2c780b-1d70-3c01-9875-08f94394236b | -10.90817 | -50.23228 | 2025-10-27 04:34:00 | NOAA-21 | LAGOA DA CONFUSÃO | TOCANTINS | Brasil | 1711902 | 17 | 33 | nan | nan | nan | Cerrado | 1.8 |
| 9bbd2792-4047-31b9-a8f5-d127a61f8e32 | -12.52957 | -47.56049 | 2025-10-27 04:34:00 | NOAA-21 | PARANÃ | TOCANTINS | Brasil | 1716208 | 17 | 33 | nan | nan | nan | Cerrado | 4.5 |
| 6b62e844-f239-37dc-a978-86db38f9b8ac | -11.02417 | -47.85692 | 2025-10-27 04:34:00 | NOAA-21 | SILVANÓPOLIS | TOCANTINS | Brasil | 1720655 | 17 | 33 | nan | nan | nan | Cerrado | 1.7 |
| d757a754-0a6d-3d50-954c-521920f67b69 | -14.63006 | -48.4128 | 2025-10-27 04:34:00 | NOAA-21 | NIQUELÂNDIA | GOIÁS | Brasil | 5214606 | 52 | 33 | nan | nan | nan | Cerrado | 1.6 |
| 4a77bfae-1406-34ea-a791-e6a25c8f4424 | -12.22253 | -46.49398 | 2025-10-27 04:34:00 | NOAA-21 | TAGUATINGA | TOCANTINS | Brasil | 1720903 | 17 | 33 | nan | nan | nan | Cerrado | 2.4 |
| 866e0b8f-a498-3ff2-966e-bd18967d73ac | -14.40535 | -51.54724 | 2025-10-27 04:34:00 | NOAA-21 | COCALINHO | MATO GROSSO | Brasil | 5103106 | 51 | 33 | nan | nan | nan | Cerrado | 1.2 |
| dd1e5c51-2ccb-3918-a8fd-87b3854386a6 | -17.52064 | -45.10398 | 2025-10-27 04:34:00 | NOAA-21 | BURITIZEIRO | MINAS GERAIS | Brasil | 3109402 | 31 | 33 | nan | nan | nan | Cerrado | 1.1 |
| 408a48e5-ffe7-3fdd-9ff4-3712a6b073d9 | -11.42446 | -46.09349 | 2025-10-27 04:34:00 | NOAA-21 | FORMOSA DO RIO PRETO | BAHIA | Brasil | 2911105 | 29 | 33 | nan | nan | nan | Cerrado | 0.8 |
| a34978c8-e4a8-3199-a256-68bfdd103db9 | -13.36895 | -47.66716 | 2025-10-27 04:34:00 | NOAA-21 | PARANÃ | TOCANTINS | Brasil | 1716208 | 17 | 33 | nan | nan | nan | Cerrado | 3.9 |
| 98c7f858-9b67-3169-b52e-a650498d1a92 | -15.1919 | -47.21933 | 2025-10-27 04:34:00 | NOAA-21 | FORMOSA | GOIÁS | Brasil | 5208004 | 52 | 33 | nan | nan | nan | Cerrado | 0.9 |
| 99e3218c-cc7a-36f7-a68d-273639acc771 | -10.95834 | -48.06359 | 2025-10-27 04:34:00 | NOAA-21 | MONTE DO CARMO | TOCANTINS | Brasil | 1713601 | 17 | 33 | nan | nan | nan | Cerrado | 5.1 |
| a2f8c8d7-db32-3763-a525-dd600de3369f | -10.82907 | -47.62145 | 2025-10-27 04:34:00 | NOAA-21 | PONTE ALTA DO TOCANTINS | TOCANTINS | Brasil | 1717909 | 17 | 33 | nan | nan | nan | Cerrado | 0.4 |
| 4fff8f3c-36ad-38e9-b043-6b5f1af29636 | -13.44185 | -47.38605 | 2025-10-27 04:34:00 | NOAA-21 | CAVALCANTE | GOIÁS | Brasil | 5205307 | 52 | 33 | nan | nan | nan | Cerrado | 1.6 |
| 4da638ac-45cf-3e43-af5e-902ed63c9402 | -12.90307 | -48.59415 | 2025-10-27 04:34:00 | NOAA-21 | JAÚ DO TOCANTINS | TOCANTINS | Brasil | 1711506 | 17 | 33 | nan | nan | nan | Cerrado | 1.6 |
| 2c43b82b-c6a3-3c74-b3a1-f343ef818610 | -13.28592 | -54.39704 | 2025-10-27 04:34:00 | NOAA-21 | PARANATINGA | MATO GROSSO | Brasil | 5106307 | 51 | 33 | nan | nan | nan | Amazônia | 3.8 |
| d53bd453-8e22-3e1e-82e2-118e7ea578d7 | -11.02632 | -47.82079 | 2025-10-27 04:34:00 | NOAA-21 | SILVANÓPOLIS | TOCANTINS | Brasil | 1720655 | 17 | 33 | nan | nan | nan | Cerrado | 4.4 |
| a542d3c8-19ac-356a-a11a-a4df262a73f2 | -11.75217 | -48.18542 | 2025-10-27 04:34:00 | NOAA-21 | SÃO VALÉRIO | TOCANTINS | Brasil | 1720499 | 17 | 33 | nan | nan | nan | Cerrado | 1.3 |
| 4da18d1d-a018-30fb-b72b-0f0870e959e2 | -12.08819 | -46.40139 | 2025-10-27 04:34:00 | NOAA-21 | PONTE ALTA DO BOM JESUS | TOCANTINS | Brasil | 1717800 | 17 | 33 | nan | nan | nan | Cerrado | 2.1 |
| e1b443d6-cb02-33f3-8893-5d157c633404 | -13.64377 | -47.60679 | 2025-10-27 04:34:00 | NOAA-21 | CAVALCANTE | GOIÁS | Brasil | 5205307 | 52 | 33 | nan | nan | nan | Cerrado | 1.1 |
| 27d91973-0885-31e4-b736-d30901c147a3 | -14.56702 | -47.99574 | 2025-10-27 04:34:00 | NOAA-21 | NIQUELÂNDIA | GOIÁS | Brasil | 5214606 | 52 | 33 | nan | nan | nan | Cerrado | 1.8 |
| 7a66a0cc-94a6-3cc3-824c-2861980e2ba6 | -12.34037 | -50.1572 | 2025-10-27 04:34:00 | NOAA-21 | FORMOSO DO ARAGUAIA | TOCANTINS | Brasil | 1708205 | 17 | 33 | nan | nan | nan | Cerrado | 0.6 |
| d1a35022-fb95-33b6-a52d-d2f1e077ef31 | -17.41385 | -46.87835 | 2025-10-27 04:34:00 | NOAA-21 | PARACATU | MINAS GERAIS | Brasil | 3147006 | 31 | 33 | nan | nan | nan | Cerrado | 0.6 |
| 91ab7bd2-a917-3d82-bf6a-7869b45b1620 | -13.28193 | -54.39635 | 2025-10-27 04:34:00 | NOAA-21 | PARANATINGA | MATO GROSSO | Brasil | 5106307 | 51 | 33 | nan | nan | nan | Amazônia | 2.1 |
| 782091e3-e34b-3990-953e-119ad62d2c5c | -20.6481 | -47.23123 | 2025-10-27 04:36:00 | NOAA-21 | ITIRAPUÃ | SÃO PAULO | Brasil | 3523701 | 35 | 33 | nan | nan | nan | Cerrado | 2.8 |
| 81ee958e-e085-3620-9f7f-c78fd49e3de0 | -22.36297 | -45.17715 | 2025-10-27 04:36:00 | NOAA-21 | VIRGÍNIA | MINAS GERAIS | Brasil | 3171709 | 31 | 33 | nan | nan | nan | Mata Atlântica | 0.7 |
| 8dbb287c-32c9-375b-9180-564771ee43d7 | -20.4858 | -46.27628 | 2025-10-27 04:36:00 | NOAA-21 | VARGEM BONITA | MINAS GERAIS | Brasil | 3170602 | 31 | 33 | nan | nan | nan | Cerrado | 2.1 |
| e1960d88-8b71-3d73-9434-d08eb9a34f56 | -21.665 | -44.51747 | 2025-10-27 04:36:00 | NOAA-21 | SÃO VICENTE DE MINAS | MINAS GERAIS | Brasil | 3165305 | 31 | 33 | nan | nan | nan | Mata Atlântica | 1.2 |
| 369fdec4-6063-3555-ba4f-cc1902b2c0c8 | -22.54645 | -47.02302 | 2025-10-27 04:36:00 | NOAA-21 | MOGI MIRIM | SÃO PAULO | Brasil | 3530805 | 35 | 33 | nan | nan | nan | Cerrado | 1.0 |
| d0feb6c8-3354-3a8f-9c6d-4ee2aed8cb38 | -21.47974 | -43.86293 | 2025-10-27 04:36:00 | NOAA-21 | IBERTIOGA | MINAS GERAIS | Brasil | 3129400 | 31 | 33 | nan | nan | nan | Mata Atlântica | 1.9 |
| 1a8307d4-889a-3361-b823-da3b9c6ae308 | -19.36149 | -43.69063 | 2025-10-27 04:36:00 | NOAA-21 | JABOTICATUBAS | MINAS GERAIS | Brasil | 3134608 | 31 | 33 | nan | nan | nan | Cerrado | 0.9 |
| d426fb04-6a4a-3f41-93a6-15e302eb3d0e | -17.9954 | -48.18688 | 2025-10-27 04:36:00 | NOAA-21 | GOIANDIRA | GOIÁS | Brasil | 5208509 | 52 | 33 | nan | nan | nan | Cerrado | 2.7 |
| b36b0629-741f-3c81-8d62-037027e856e6 | -20.97628 | -44.32503 | 2025-10-27 04:36:00 | NOAA-21 | RITÁPOLIS | MINAS GERAIS | Brasil | 3156106 | 31 | 33 | nan | nan | nan | Mata Atlântica | 1.9 |
| 18d42966-8643-3c89-a38d-84440a94eb9a | -20.90444 | -43.43383 | 2025-10-27 04:36:00 | NOAA-21 | RIO ESPERA | MINAS GERAIS | Brasil | 3155207 | 31 | 33 | nan | nan | nan | Mata Atlântica | 1.2 |
| 163c6e86-5cbd-3d7a-a4c4-8c279825dfaf | -18.63191 | -43.06651 | 2025-10-27 04:36:00 | NOAA-21 | SABINÓPOLIS | MINAS GERAIS | Brasil | 3156809 | 31 | 33 | nan | nan | nan | Mata Atlântica | 2.5 |
| 970a7917-f096-35e6-9438-a64dd70398ee | -18.26205 | -45.36654 | 2025-10-27 04:36:00 | NOAA-21 | SÃO GONÇALO DO ABAETÉ | MINAS GERAIS | Brasil | 3161700 | 31 | 33 | nan | nan | nan | Cerrado | 1.0 |
| 1e4e294a-0028-3866-a6ee-a2a10b02403d | -21.37825 | -43.59896 | 2025-10-27 04:36:00 | NOAA-21 | SANTOS DUMONT | MINAS GERAIS | Brasil | 3160702 | 31 | 33 | nan | nan | nan | Mata Atlântica | 2.2 |
| 5a629b5b-2a3d-3af7-801b-857730a22412 | -22.12353 | -42.98428 | 2025-10-27 04:36:00 | NOAA-21 | TRÊS RIOS | RIO DE JANEIRO | Brasil | 3306008 | 33 | 33 | nan | nan | nan | Mata Atlântica | 5.2 |
| 270355ae-7ede-343d-b6bf-4b0e21e43b74 | -21.11589 | -43.95553 | 2025-10-27 04:36:00 | NOAA-21 | DORES DE CAMPOS | MINAS GERAIS | Brasil | 3123007 | 31 | 33 | nan | nan | nan | Mata Atlântica | 1.4 |
| 29b98dac-f332-3b39-9a2a-ec6588232041 | -20.72298 | -42.77983 | 2025-10-27 04:36:00 | NOAA-21 | VIÇOSA | MINAS GERAIS | Brasil | 3171303 | 31 | 33 | nan | nan | nan | Mata Atlântica | 2.8 |
| 0ff1a222-f8a0-3a44-a41c-a4388ab4cb10 | -21.66856 | -44.52048 | 2025-10-27 04:36:00 | NOAA-21 | SÃO VICENTE DE MINAS | MINAS GERAIS | Brasil | 3165305 | 31 | 33 | nan | nan | nan | Mata Atlântica | 1.0 |
| ec1f3b24-cf54-3ffc-a163-a306e37a550a | -21.66413 | -44.51987 | 2025-10-27 04:36:00 | NOAA-21 | SÃO VICENTE DE MINAS | MINAS GERAIS | Brasil | 3165305 | 31 | 33 | nan | nan | nan | Mata Atlântica | 1.0 |
| e57bf9a8-bb4b-3f5e-9bc5-6f7745cd1b9f | -20.97681 | -44.32031 | 2025-10-27 04:36:00 | NOAA-21 | RITÁPOLIS | MINAS GERAIS | Brasil | 3156106 | 31 | 33 | nan | nan | nan | Mata Atlântica | 0.8 |
| 8b1bff67-d9e4-3a46-81f4-1658c8d9b110 | -18.84011 | -47.6821 | 2025-10-27 04:36:00 | NOAA-21 | ESTRELA DO SUL | MINAS GERAIS | Brasil | 3124807 | 31 | 33 | nan | nan | nan | Cerrado | 0.7 |
| cd59c1bb-fc6a-37ce-b809-f54a638b305f | -18.5861 | -43.18974 | 2025-10-27 04:36:00 | NOAA-21 | SANTO ANTÔNIO DO ITAMBÉ | MINAS GERAIS | Brasil | 3160207 | 31 | 33 | nan | nan | nan | Mata Atlântica | 1.2 |
| 5022c99c-c6b7-3477-9270-75c3d803888f | -22.55029 | -47.02357 | 2025-10-27 04:36:00 | NOAA-21 | MOGI MIRIM | SÃO PAULO | Brasil | 3530805 | 35 | 33 | nan | nan | nan | Cerrado | 1.0 |
| 8027de55-df76-3c12-9987-c869e357c9d2 | -20.93536 | -43.28607 | 2025-10-27 04:36:00 | NOAA-21 | CIPOTÂNEA | MINAS GERAIS | Brasil | 3116308 | 31 | 33 | nan | nan | nan | Mata Atlântica | 0.9 |
| 612af842-b65f-3c30-a722-1ba8cec15ec9 | -19.6426 | -45.39236 | 2025-10-27 04:36:00 | NOAA-21 | BOM DESPACHO | MINAS GERAIS | Brasil | 3107406 | 31 | 33 | nan | nan | nan | Cerrado | 4.1 |
| e4d6f8af-f034-3004-99a1-863b5cf58765 | -19.57448 | -44.74665 | 2025-10-27 04:36:00 | NOAA-21 | MARAVILHAS | MINAS GERAIS | Brasil | 3139706 | 31 | 33 | nan | nan | nan | Mata Atlântica | 1.2 |
| 013d77b1-e082-32a3-af6f-63f56d60a92f | -20.6652 | -42.74195 | 2025-10-27 04:36:00 | NOAA-21 | PEDRA DO ANTA | MINAS GERAIS | Brasil | 3148806 | 31 | 33 | nan | nan | nan | Mata Atlântica | 1.6 |
| 7c7fc65b-97e6-3625-a57c-1281f50974dd | -22.08862 | -42.98431 | 2025-10-27 04:36:00 | NOAA-21 | TRÊS RIOS | RIO DE JANEIRO | Brasil | 3306008 | 33 | 33 | nan | nan | nan | Mata Atlântica | 10.7 |
| a13a38dc-765d-377a-84bc-b2667e1198fe | -18.68205 | -43.72469 | 2025-10-27 04:36:00 | NOAA-21 | CONCEIÇÃO DO MATO DENTRO | MINAS GERAIS | Brasil | 3117504 | 31 | 33 | nan | nan | nan | Cerrado | 0.9 |
| 5dc3e9ea-ecdc-36f5-bbe0-232e2a6100ec | -22.08921 | -42.97863 | 2025-10-27 04:36:00 | NOAA-21 | TRÊS RIOS | RIO DE JANEIRO | Brasil | 3306008 | 33 | 33 | nan | nan | nan | Mata Atlântica | 6.0 |
| 18430e6a-dfe1-3de8-9cec-cdb94863360f | -20.66031 | -42.74117 | 2025-10-27 04:36:00 | NOAA-21 | PEDRA DO ANTA | MINAS GERAIS | Brasil | 3148806 | 31 | 33 | nan | nan | nan | Mata Atlântica | 1.6 |
| 5873afb8-1275-39d2-91e3-4b5a8136220c | -22.87279 | -53.53278 | 2025-10-27 04:36:00 | NOAA-21 | TAQUARUSSU | MATO GROSSO DO SUL | Brasil | 5007976 | 50 | 33 | nan | nan | nan | Mata Atlântica | 0.3 |
| d6cdd089-1e56-3b41-a3dd-b86f970f685a | -20.13249 | -45.68488 | 2025-10-27 04:36:00 | NOAA-21 | IGUATAMA | MINAS GERAIS | Brasil | 3130309 | 31 | 33 | nan | nan | nan | Cerrado | 0.6 |
| 5d0ad767-8121-3773-af99-5cc40a89c4af | -21.58176 | -43.50162 | 2025-10-27 04:36:00 | NOAA-21 | JUIZ DE FORA | MINAS GERAIS | Brasil | 3136702 | 31 | 33 | nan | nan | nan | Mata Atlântica | 3.6 |
| 9d3e5b25-93ea-38b5-a3cd-2904ee7a1dd4 | -19.66628 | -44.66233 | 2025-10-27 04:36:00 | NOAA-21 | PEQUI | MINAS GERAIS | Brasil | 3149606 | 31 | 33 | nan | nan | nan | Mata Atlântica | 4.4 |
| 2ddbe109-73fd-30ed-8731-f00a67196c48 | -21.66908 | -44.51577 | 2025-10-27 04:36:00 | NOAA-21 | SÃO VICENTE DE MINAS | MINAS GERAIS | Brasil | 3165305 | 31 | 33 | nan | nan | nan | Mata Atlântica | 2.4 |
| 9053fb29-2da2-34f6-bcba-a3fa809107ce | -19.98444 | -43.74541 | 2025-10-27 04:36:00 | NOAA-21 | RAPOSOS | MINAS GERAIS | Brasil | 3153905 | 31 | 33 | nan | nan | nan | Mata Atlântica | 0.9 |
| bf400cbc-af3c-31f4-94f8-3e3eb340b229 | -20.75282 | -43.22861 | 2025-10-27 04:36:00 | NOAA-21 | PRESIDENTE BERNARDES | MINAS GERAIS | Brasil | 3153103 | 31 | 33 | nan | nan | nan | Mata Atlântica | 1.5 |
| aa1661a1-4736-3f39-a2b9-7bacacb89255 | -21.58921 | -43.49219 | 2025-10-27 04:36:00 | NOAA-21 | JUIZ DE FORA | MINAS GERAIS | Brasil | 3136702 | 31 | 33 | nan | nan | nan | Mata Atlântica | 4.7 |
| 72ddfcf3-63b9-39b4-8783-ab7a3845519e | -19.92292 | -44.81475 | 2025-10-27 04:36:00 | NOAA-21 | IGARATINGA | MINAS GERAIS | Brasil | 3130200 | 31 | 33 | nan | nan | nan | Cerrado | 1.2 |
| 835dba7e-b903-3cb6-8638-103f8e588a18 | -17.99884 | -48.18747 | 2025-10-27 04:36:00 | NOAA-21 | GOIANDIRA | GOIÁS | Brasil | 5208509 | 52 | 33 | nan | nan | nan | Cerrado | 5.3 |
| d6241853-16d0-34cb-aa86-0cc11e185b61 | -19.92719 | -44.81515 | 2025-10-27 04:36:00 | NOAA-21 | SÃO GONÇALO DO PARÁ | MINAS GERAIS | Brasil | 3161809 | 31 | 33 | nan | nan | nan | Cerrado | 1.2 |
| a0429f1b-a737-360e-b8a5-75da412acb45 | -18.26607 | -45.36703 | 2025-10-27 04:36:00 | NOAA-21 | SÃO GONÇALO DO ABAETÉ | MINAS GERAIS | Brasil | 3161700 | 31 | 33 | nan | nan | nan | Cerrado | 7.2 |
| 7a245050-7853-39b2-bdd1-742ef3063f4b | -22.09411 | -42.9794 | 2025-10-27 04:36:00 | NOAA-21 | TRÊS RIOS | RIO DE JANEIRO | Brasil | 3306008 | 33 | 33 | nan | nan | nan | Mata Atlântica | 6.0 |
| dbd6f2c7-f014-39f1-be6a-ae7fbbdaf2c4 | -20.85766 | -43.55551 | 2025-10-27 04:36:00 | NOAA-21 | RIO ESPERA | MINAS GERAIS | Brasil | 3155207 | 31 | 33 | nan | nan | nan | Mata Atlântica | 8.7 |
| 4507fcff-2acd-3ef8-9e20-c8f35b3e8623 | -20.6518 | -47.23182 | 2025-10-27 04:36:00 | NOAA-21 | ITIRAPUÃ | SÃO PAULO | Brasil | 3523701 | 35 | 33 | nan | nan | nan | Cerrado | 1.9 |
| 72aff855-eb9a-3e0e-9097-868a4929a311 | -21.66999 | -44.51334 | 2025-10-27 04:36:00 | NOAA-21 | SÃO VICENTE DE MINAS | MINAS GERAIS | Brasil | 3165305 | 31 | 33 | nan | nan | nan | Mata Atlântica | 1.2 |
| 10edfb00-9d43-38e3-9108-102cc58f149a | -18.26913 | -45.37497 | 2025-10-27 04:36:00 | NOAA-21 | SÃO GONÇALO DO ABAETÉ | MINAS GERAIS | Brasil | 3161700 | 31 | 33 | nan | nan | nan | Cerrado | 1.7 |
| 21ab49db-dd90-3923-abd7-e35968621c33 | -19.88471 | -44.37316 | 2025-10-27 04:36:00 | NOAA-21 | FLORESTAL | MINAS GERAIS | Brasil | 3126000 | 31 | 33 | nan | nan | nan | Cerrado | 1.7 |
| 18f10a72-37f2-31c5-a913-605e512d9466 | -19.92243 | -44.81894 | 2025-10-27 04:36:00 | NOAA-21 | SÃO GONÇALO DO PARÁ | MINAS GERAIS | Brasil | 3161809 | 31 | 33 | nan | nan | nan | Cerrado | 1.2 |
| 82e9aa18-979d-3d6c-b4eb-847caa9c3122 | -19.63899 | -45.38806 | 2025-10-27 04:36:00 | NOAA-21 | BOM DESPACHO | MINAS GERAIS | Brasil | 3107406 | 31 | 33 | nan | nan | nan | Cerrado | 2.3 |
| 1c3a02d5-20e1-33ac-a13b-8e88cd6d0408 | -19.44151 | -43.03795 | 2025-10-27 04:36:00 | NOAA-21 | ANTÔNIO DIAS | MINAS GERAIS | Brasil | 3103009 | 31 | 33 | nan | nan | nan | Mata Atlântica | 4.7 |
| dd201a58-2f75-3444-9634-9af4e89072a3 | -19.64352 | -45.38494 | 2025-10-27 04:36:00 | NOAA-21 | BOM DESPACHO | MINAS GERAIS | Brasil | 3107406 | 31 | 33 | nan | nan | nan | Cerrado | 2.3 |
| 7ce98f49-0e23-3081-906b-bd64e74711f5 | -21.58864 | -43.4976 | 2025-10-27 04:36:00 | NOAA-21 | JUIZ DE FORA | MINAS GERAIS | Brasil | 3136702 | 31 | 33 | nan | nan | nan | Mata Atlântica | 4.7 |
| b215968c-93a7-3b13-b312-621763eadbc2 | -20.66095 | -42.7353 | 2025-10-27 04:36:00 | NOAA-21 | PEDRA DO ANTA | MINAS GERAIS | Brasil | 3148806 | 31 | 33 | nan | nan | nan | Mata Atlântica | 2.7 |
| affa00dd-4f83-325c-b301-4f2e71ede7a4 | -21.66323 | -43.52971 | 2025-10-27 04:36:00 | NOAA-21 | JUIZ DE FORA | MINAS GERAIS | Brasil | 3136702 | 31 | 33 | nan | nan | nan | Mata Atlântica | 1.7 |
| 1718448a-f932-384b-8e07-18c531919c09 | -21.58337 | -43.50211 | 2025-10-27 04:36:00 | NOAA-21 | JUIZ DE FORA | MINAS GERAIS | Brasil | 3136702 | 31 | 33 | nan | nan | nan | Mata Atlântica | 10.9 |
| 95adb21f-e2f7-3766-9965-50b149f033be | -21.5881 | -43.50265 | 2025-10-27 04:36:00 | NOAA-21 | JUIZ DE FORA | MINAS GERAIS | Brasil | 3136702 | 31 | 33 | nan | nan | nan | Mata Atlântica | 0.4 |
| c907a89f-6366-3e80-9b73-84aa1384873b | -19.55177 | -44.16106 | 2025-10-27 04:36:00 | NOAA-21 | CAPIM BRANCO | MINAS GERAIS | Brasil | 3112505 | 31 | 33 | nan | nan | nan | Cerrado | 2.5 |
| 4619e7e8-7768-3e99-83e1-f6e76ed47305 | -21.66943 | -44.51807 | 2025-10-27 04:36:00 | NOAA-21 | SÃO VICENTE DE MINAS | MINAS GERAIS | Brasil | 3165305 | 31 | 33 | nan | nan | nan | Mata Atlântica | 1.2 |
| 4985366d-04c0-3c22-88a1-81255c0da455 | -21.34649 | -45.23756 | 2025-10-27 04:36:00 | NOAA-21 | NEPOMUCENO | MINAS GERAIS | Brasil | 3144607 | 31 | 33 | nan | nan | nan | Mata Atlântica | 1.3 |
| ea779457-e261-399d-a9fa-bffbfcb9bef3 | -18.35004 | -43.96102 | 2025-10-27 04:36:00 | NOAA-21 | DIAMANTINA | MINAS GERAIS | Brasil | 3121605 | 31 | 33 | nan | nan | nan | Cerrado | 1.5 |
| 241a8471-eb75-35a9-9e0c-c1edcd196274 | -19.64306 | -45.38866 | 2025-10-27 04:36:00 | NOAA-21 | BOM DESPACHO | MINAS GERAIS | Brasil | 3107406 | 31 | 33 | nan | nan | nan | Cerrado | 2.3 |
| 60ef6891-2bd9-3f5e-8571-5506e001f423 | -22.57761 | -44.74009 | 2025-10-27 04:36:00 | NOAA-21 | QUELUZ | SÃO PAULO | Brasil | 3541901 | 35 | 33 | nan | nan | nan | Mata Atlântica | 0.9 |
| 51a24cfe-81e3-3990-9972-e37d7fe69019 | -20.58249 | -45.29406 | 2025-10-27 04:36:00 | NOAA-21 | FORMIGA | MINAS GERAIS | Brasil | 3126109 | 31 | 33 | nan | nan | nan | Mata Atlântica | 0.8 |
| a01a5d90-28b7-3707-9c28-d5cdd2255b48 | -20.48613 | -46.27765 | 2025-10-27 04:36:00 | NOAA-21 | VARGEM BONITA | MINAS GERAIS | Brasil | 3170602 | 31 | 33 | nan | nan | nan | Cerrado | 2.0 |
| 20eb053c-042c-37db-9b01-30dc228d8e1f | -22.54911 | -47.01966 | 2025-10-27 04:36:00 | NOAA-21 | MOGI MIRIM | SÃO PAULO | Brasil | 3530805 | 35 | 33 | nan | nan | nan | Cerrado | 3.0 |
| 16b49a93-8d0d-3045-99f8-0f6caf8fece3 | -20.97575 | -44.3297 | 2025-10-27 04:36:00 | NOAA-21 | RITÁPOLIS | MINAS GERAIS | Brasil | 3156106 | 31 | 33 | nan | nan | nan | Mata Atlântica | 1.9 |
| 1b92ea3b-aeed-34ce-9718-46a3cf34428e | -21.66855 | -45.27711 | 2025-10-27 04:36:00 | NOAA-21 | TRÊS CORAÇÕES | MINAS GERAIS | Brasil | 3169307 | 31 | 33 | nan | nan | nan | Mata Atlântica | 2.0 |
| ed018416-27d7-3e45-84a5-1ccafd752917 | -18.63394 | -43.06608 | 2025-10-27 04:36:00 | NOAA-21 | SABINÓPOLIS | MINAS GERAIS | Brasil | 3156809 | 31 | 33 | nan | nan | nan | Mata Atlântica | 1.9 |
| 10b6670c-0675-381f-9812-b1c94fd9f3b7 | -19.92294 | -44.81596 | 2025-10-27 04:36:00 | NOAA-21 | SÃO GONÇALO DO PARÁ | MINAS GERAIS | Brasil | 3161809 | 31 | 33 | nan | nan | nan | Cerrado | 2.2 |
| 9eee1334-c837-32ad-8256-7c1c23815358 | -20.13542 | -45.68537 | 2025-10-27 04:36:00 | NOAA-21 | IGUATAMA | MINAS GERAIS | Brasil | 3130309 | 31 | 33 | nan | nan | nan | Cerrado | 1.3 |
| f4d27a0a-7d80-3485-9872-5b3a0003c03b | -20.66155 | -42.72972 | 2025-10-27 04:36:00 | NOAA-21 | PEDRA DO ANTA | MINAS GERAIS | Brasil | 3148806 | 31 | 33 | nan | nan | nan | Mata Atlântica | 2.7 |
| d7f40a8f-238e-3266-869d-5193bad57d01 | -20.13652 | -45.68542 | 2025-10-27 04:36:00 | NOAA-21 | IGUATAMA | MINAS GERAIS | Brasil | 3130309 | 31 | 33 | nan | nan | nan | Cerrado | 0.6 |
| 075f6a01-e656-3abc-8227-b218d09e7ad2 | -20.80215 | -43.30643 | 2025-10-27 04:36:00 | NOAA-21 | SENHORA DE OLIVEIRA | MINAS GERAIS | Brasil | 3166006 | 31 | 33 | nan | nan | nan | Mata Atlântica | 1.4 |
| 952cb488-44e5-3e55-a57b-f8fc729102c4 | -20.98022 | -44.32992 | 2025-10-27 04:36:00 | NOAA-21 | RITÁPOLIS | MINAS GERAIS | Brasil | 3156106 | 31 | 33 | nan | nan | nan | Mata Atlântica | 5.7 |
| 22f2bcf4-8b3a-3343-82c5-ac918b443ed2 | -21.07138 | -43.64322 | 2025-10-27 04:36:00 | NOAA-21 | SENHORA DOS REMÉDIOS | MINAS GERAIS | Brasil | 3166204 | 31 | 33 | nan | nan | nan | Mata Atlântica | 2.3 |
| 8bd27e9c-7ad6-3d8b-9f93-8220e742c221 | -19.87183 | -44.17929 | 2025-10-27 04:36:00 | NOAA-21 | BETIM | MINAS GERAIS | Brasil | 3106705 | 31 | 33 | nan | nan | nan | Cerrado | 2.8 |


[Clique aqui para ver as próximas entradas](README52.md)
