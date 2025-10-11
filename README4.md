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

## Dados Diários - Página 4

| ID | Latitude | Longitude | Data/Hora GMT | Satélite | Município | Estado | País | Município ID | Estado ID | País ID | Dias sem Chuva | Precipitação | Risco de Fogo | Bioma | FRP |
|----|----------|-----------|---------------|----------|-----------|--------|------|--------------|-----------|---------|----------------|--------------|----------------|-------|-----|
| d4c767ac-ea67-344c-bb93-602769a6ad9a | -13.2246 | -42.3657 | 2025-10-11 01:30:00 | GOES-19 | CATURAMA | BAHIA | Brasil | 2907558 | 29 | 33 | nan | nan | nan | Caatinga | 124.5 |
| 08586083-d411-3fd7-9466-4075335cd47b | -8.4034 | -45.0783 | 2025-10-11 01:30:00 | GOES-19 | BAIXA GRANDE DO RIBEIRO | PIAUÍ | Brasil | 2201150 | 22 | 33 | nan | nan | nan | Cerrado | 94.3 |
| b37a2e1f-29af-3c3a-b205-c6f71161b060 | -8.4835 | -46.2014 | 2025-10-11 01:30:00 | GOES-19 | BALSAS | MARANHÃO | Brasil | 2101400 | 21 | 33 | nan | nan | nan | Cerrado | 58.5 |
| 249db326-ded5-39b9-8950-c16832fad890 | -13.2052 | -42.3693 | 2025-10-11 01:30:00 | GOES-19 | CATURAMA | BAHIA | Brasil | 2907558 | 29 | 33 | nan | nan | nan | Caatinga | 106.2 |
| feed4352-1f05-32d0-8a67-c534cfd5e257 | -7.8642 | -44.4922 | 2025-10-11 01:30:00 | GOES-19 | URUÇUÍ | PIAUÍ | Brasil | 2211209 | 22 | 33 | nan | nan | nan | Cerrado | 90.6 |
| 06fd983d-c916-3ef4-a844-136b9638e1ba | -17.2722 | -46.8932 | 2025-10-11 01:30:00 | GOES-19 | PARACATU | MINAS GERAIS | Brasil | 3147006 | 31 | 33 | nan | nan | nan | Cerrado | 107.2 |
| cc35fb5d-652b-3c03-a373-59393abe97e4 | -13.2057 | -42.345 | 2025-10-11 01:30:00 | GOES-19 | CATURAMA | BAHIA | Brasil | 2907558 | 29 | 33 | nan | nan | nan | Caatinga | 421.2 |
| ab8d2e31-4064-36bd-9603-24fc8a4a3d20 | -8.4031 | -45.1012 | 2025-10-11 01:30:00 | GOES-19 | BAIXA GRANDE DO RIBEIRO | PIAUÍ | Brasil | 2201150 | 22 | 33 | nan | nan | nan | Cerrado | 73.1 |
| 6943f5b3-e2af-3259-a7f6-825027c320ae | -7.4616 | -46.8542 | 2025-10-11 01:40:00 | GOES-19 | RIACHÃO | MARANHÃO | Brasil | 2109502 | 21 | 33 | nan | nan | nan | Cerrado | 79.0 |
| f6679caf-d83b-341a-aa7c-ec531d57a4fa | -13.2257 | -42.317 | 2025-10-11 01:40:00 | GOES-19 | CATURAMA | BAHIA | Brasil | 2907558 | 29 | 33 | nan | nan | nan | Caatinga | 138.9 |
| 07275b81-1c9c-327d-af62-e4f5b5948f13 | -8.4034 | -45.0783 | 2025-10-11 01:40:00 | GOES-19 | BAIXA GRANDE DO RIBEIRO | PIAUÍ | Brasil | 2201150 | 22 | 33 | nan | nan | nan | Cerrado | 98.0 |
| dbf070bc-7264-3692-8bf8-b7873be1ea38 | -17.2722 | -46.8932 | 2025-10-11 01:40:00 | GOES-19 | PARACATU | MINAS GERAIS | Brasil | 3147006 | 31 | 33 | nan | nan | nan | Cerrado | 131.7 |
| c8872e66-9615-3e98-9411-54db4a91fd9d | -8.4031 | -45.1012 | 2025-10-11 01:40:00 | GOES-19 | BAIXA GRANDE DO RIBEIRO | PIAUÍ | Brasil | 2201150 | 22 | 33 | nan | nan | nan | Cerrado | 81.8 |
| 475d710f-b161-3201-8709-ab06870a258b | -13.2246 | -42.3657 | 2025-10-11 01:40:00 | GOES-19 | CATURAMA | BAHIA | Brasil | 2907558 | 29 | 33 | nan | nan | nan | Caatinga | 63.3 |
| e356fa18-c80c-33ba-ac7e-82dd1458bb06 | -13.2057 | -42.345 | 2025-10-11 01:40:00 | GOES-19 | CATURAMA | BAHIA | Brasil | 2907558 | 29 | 33 | nan | nan | nan | Caatinga | 277.3 |
| f1670a16-c1df-3512-900f-5bf8616397e3 | -8.1996 | -43.3189 | 2025-10-11 01:40:00 | GOES-19 | CANTO DO BURITI | PIAUÍ | Brasil | 2202307 | 22 | 33 | nan | nan | nan | Caatinga | 99.8 |
| 24104b2d-4c11-33fc-a029-0fc146149fa0 | -13.2252 | -42.3414 | 2025-10-11 01:40:00 | GOES-19 | CATURAMA | BAHIA | Brasil | 2907558 | 29 | 33 | nan | nan | nan | Caatinga | 530.6 |
| 9d7f9ec1-f1b2-39ae-a960-bb3139ee0303 | -13.2062 | -42.3206 | 2025-10-11 01:40:00 | GOES-19 | CATURAMA | BAHIA | Brasil | 2907558 | 29 | 33 | nan | nan | nan | Caatinga | 90.1 |
| b21312ac-79f1-3691-a9a9-7a9907baa142 | -13.2062 | -42.3206 | 2025-10-11 01:50:00 | GOES-19 | CATURAMA | BAHIA | Brasil | 2907558 | 29 | 33 | nan | nan | nan | Caatinga | 80.5 |
| be318f2d-661d-33cc-ace3-4ad8ed7c0b3c | -8.1996 | -43.3189 | 2025-10-11 01:50:00 | GOES-19 | CANTO DO BURITI | PIAUÍ | Brasil | 2202307 | 22 | 33 | nan | nan | nan | Caatinga | 99.8 |
| da3a21a1-5f83-3ff5-8694-eee06ba61af2 | -8.4833 | -46.2239 | 2025-10-11 01:50:00 | GOES-19 | BALSAS | MARANHÃO | Brasil | 2101400 | 21 | 33 | nan | nan | nan | Cerrado | 69.0 |
| 3e26c35d-880d-34c4-813f-7001554ce958 | -13.2252 | -42.3414 | 2025-10-11 01:50:00 | GOES-19 | CATURAMA | BAHIA | Brasil | 2907558 | 29 | 33 | nan | nan | nan | Caatinga | 410.9 |
| 0907b5f1-cb77-33fa-9fe5-b35d97db0428 | -8.4835 | -46.2014 | 2025-10-11 01:50:00 | GOES-19 | BALSAS | MARANHÃO | Brasil | 2101400 | 21 | 33 | nan | nan | nan | Cerrado | 180.8 |
| 3b5f741a-7f4e-38fb-a171-73430033dbf9 | -8.5024 | -46.1995 | 2025-10-11 01:50:00 | GOES-19 | BALSAS | MARANHÃO | Brasil | 2101400 | 21 | 33 | nan | nan | nan | Cerrado | 124.9 |
| 2a61f44a-3b73-30cb-aa9c-04ba9773ffe1 | -8.5021 | -46.222 | 2025-10-11 01:50:00 | GOES-19 | BALSAS | MARANHÃO | Brasil | 2101400 | 21 | 33 | nan | nan | nan | Cerrado | 44.1 |
| 8127a9f8-5ba2-310c-a203-92096d3e14cc | -7.8645 | -44.4692 | 2025-10-11 01:50:00 | GOES-19 | URUÇUÍ | PIAUÍ | Brasil | 2211209 | 22 | 33 | nan | nan | nan | Cerrado | 82.3 |
| 2b4c7402-80be-3f86-9f9c-22fd9587f8b9 | -12.7299 | -45.8422 | 2025-10-11 01:50:00 | GOES-19 | SÃO DESIDÉRIO | BAHIA | Brasil | 2928901 | 29 | 33 | nan | nan | nan | Cerrado | 62.4 |
| be7abce5-8122-30da-9567-c12e58ef016b | -17.2722 | -46.8932 | 2025-10-11 01:50:00 | GOES-19 | PARACATU | MINAS GERAIS | Brasil | 3147006 | 31 | 33 | nan | nan | nan | Cerrado | 89.4 |
| b6f9200b-2612-3a71-9c1d-835873dd73b4 | -7.4616 | -46.8542 | 2025-10-11 01:50:00 | GOES-19 | RIACHÃO | MARANHÃO | Brasil | 2109502 | 21 | 33 | nan | nan | nan | Cerrado | 73.2 |
| 130bb20d-785d-3e79-b9cc-676bd8b88c14 | -13.2257 | -42.317 | 2025-10-11 01:50:00 | GOES-19 | CATURAMA | BAHIA | Brasil | 2907558 | 29 | 33 | nan | nan | nan | Caatinga | 109.7 |
| cef4d3ec-6057-3e9c-81a4-13d74ca7a024 | -13.2057 | -42.345 | 2025-10-11 01:50:00 | GOES-19 | CATURAMA | BAHIA | Brasil | 2907558 | 29 | 33 | nan | nan | nan | Caatinga | 240.8 |
| f87c8322-8f80-36d8-8f45-bc538bbeca62 | -13.2257 | -42.317 | 2025-10-11 02:00:00 | GOES-19 | CATURAMA | BAHIA | Brasil | 2907558 | 29 | 33 | nan | nan | nan | Caatinga | 105.3 |
| 7f2955fc-7ac5-3f1f-82d4-2f8240db4f31 | -8.1993 | -43.3424 | 2025-10-11 02:00:00 | GOES-19 | CANTO DO BURITI | PIAUÍ | Brasil | 2202307 | 22 | 33 | nan | nan | nan | Caatinga | 76.3 |
| b7906f8d-d532-3079-b75d-a51f886e1980 | -13.2246 | -42.3657 | 2025-10-11 02:00:00 | GOES-19 | CATURAMA | BAHIA | Brasil | 2907558 | 29 | 33 | nan | nan | nan | Caatinga | 78.4 |
| 110fbae5-4e93-3f1e-b530-40cbbf9cb982 | -7.4616 | -46.8542 | 2025-10-11 02:00:00 | GOES-19 | RIACHÃO | MARANHÃO | Brasil | 2109502 | 21 | 33 | nan | nan | nan | Cerrado | 79.4 |
| 96d014c5-9c8e-3809-a306-3cdae2215408 | -8.5024 | -46.1995 | 2025-10-11 02:00:00 | GOES-19 | BALSAS | MARANHÃO | Brasil | 2101400 | 21 | 33 | nan | nan | nan | Cerrado | 154.8 |
| 701b2c6e-73ef-30a9-a451-d8fa4baf0bc4 | -8.4835 | -46.2014 | 2025-10-11 02:00:00 | GOES-19 | BALSAS | MARANHÃO | Brasil | 2101400 | 21 | 33 | nan | nan | nan | Cerrado | 266.1 |
| 4cbbda08-f711-3540-9317-dd8ed937b9ee | -8.1996 | -43.3189 | 2025-10-11 02:00:00 | GOES-19 | CANTO DO BURITI | PIAUÍ | Brasil | 2202307 | 22 | 33 | nan | nan | nan | Caatinga | 97.5 |
| e4feab79-9503-3c38-9064-eb01493c0470 | -15.0021 | -45.5725 | 2025-10-11 02:00:00 | GOES-19 | JANUÁRIA | MINAS GERAIS | Brasil | 3135209 | 31 | 33 | nan | nan | nan | Cerrado | 119.6 |
| bdafe809-d12e-3a49-a0a6-275f53a21cee | -8.5021 | -46.222 | 2025-10-11 02:00:00 | GOES-19 | BALSAS | MARANHÃO | Brasil | 2101400 | 21 | 33 | nan | nan | nan | Cerrado | 124.4 |
| cc02e369-25d0-3682-b1cd-7d54b6460e70 | -8.4838 | -46.1789 | 2025-10-11 02:00:00 | GOES-19 | BALSAS | MARANHÃO | Brasil | 2101400 | 21 | 33 | nan | nan | nan | Cerrado | 71.5 |
| bcfd7228-6fd9-3a11-877b-5bf998baa235 | -17.2722 | -46.8932 | 2025-10-11 02:00:00 | GOES-19 | PARACATU | MINAS GERAIS | Brasil | 3147006 | 31 | 33 | nan | nan | nan | Cerrado | 103.3 |
| a6d733f5-7a96-31c1-aa8a-4ddcc5ed5f5e | -8.4833 | -46.2239 | 2025-10-11 02:00:00 | GOES-19 | BALSAS | MARANHÃO | Brasil | 2101400 | 21 | 33 | nan | nan | nan | Cerrado | 232.5 |
| 25da13a8-e7d6-30ca-ab8a-1c3c20a0bff4 | -13.2252 | -42.3414 | 2025-10-11 02:00:00 | GOES-19 | CATURAMA | BAHIA | Brasil | 2907558 | 29 | 33 | nan | nan | nan | Caatinga | 309.2 |
| fc84b86b-a566-3813-9b33-6c9415ce6058 | -13.2062 | -42.3206 | 2025-10-11 02:00:00 | GOES-19 | CATURAMA | BAHIA | Brasil | 2907558 | 29 | 33 | nan | nan | nan | Caatinga | 79.6 |
| d5b97437-ae61-35fb-a78a-d2a2b824e175 | -13.2057 | -42.345 | 2025-10-11 02:00:00 | GOES-19 | CATURAMA | BAHIA | Brasil | 2907558 | 29 | 33 | nan | nan | nan | Caatinga | 199.9 |
| 26684bfe-d61c-389a-82ef-31702fc77911 | -15.0016 | -45.5958 | 2025-10-11 02:00:00 | GOES-19 | JANUÁRIA | MINAS GERAIS | Brasil | 3135209 | 31 | 33 | nan | nan | nan | Cerrado | 75.4 |
| 01aefbeb-1cb3-3f28-bb88-270d2606a277 | -8.4833 | -46.2239 | 2025-10-11 02:10:00 | GOES-19 | BALSAS | MARANHÃO | Brasil | 2101400 | 21 | 33 | nan | nan | nan | Cerrado | 93.8 |
| 16774ff1-f253-357a-888a-f49e54af8387 | -8.4838 | -46.1789 | 2025-10-11 02:10:00 | GOES-19 | BALSAS | MARANHÃO | Brasil | 2101400 | 21 | 33 | nan | nan | nan | Cerrado | 94.9 |
| 10ca7fd6-d2d7-3c18-b25e-defe4863e372 | -13.2057 | -42.345 | 2025-10-11 02:10:00 | GOES-19 | CATURAMA | BAHIA | Brasil | 2907558 | 29 | 33 | nan | nan | nan | Caatinga | 210.5 |
| 27f493e0-47f7-3872-891a-7ffc1a475f03 | -8.4835 | -46.2014 | 2025-10-11 02:10:00 | GOES-19 | BALSAS | MARANHÃO | Brasil | 2101400 | 21 | 33 | nan | nan | nan | Cerrado | 166.1 |
| 96f4ace7-5228-3300-a77d-301118b225ef | -8.1996 | -43.3189 | 2025-10-11 02:10:00 | GOES-19 | CANTO DO BURITI | PIAUÍ | Brasil | 2202307 | 22 | 33 | nan | nan | nan | Caatinga | 108.9 |
| 60606b14-55f8-359c-aed7-5c8a7c657693 | -14.9377 | -46.7361 | 2025-10-11 02:10:00 | GOES-19 | FLORES DE GOIÁS | GOIÁS | Brasil | 5207907 | 52 | 33 | nan | nan | nan | Cerrado | 97.1 |
| 061f0693-e506-3d33-bd2c-43942aed6020 | -8.5029 | -46.1545 | 2025-10-11 02:10:00 | GOES-19 | BALSAS | MARANHÃO | Brasil | 2101400 | 21 | 33 | nan | nan | nan | Cerrado | 68.6 |
| 1ae0a94a-f9b3-3c20-8c52-55bfdf2a8263 | -8.5027 | -46.177 | 2025-10-11 02:10:00 | GOES-19 | BALSAS | MARANHÃO | Brasil | 2101400 | 21 | 33 | nan | nan | nan | Cerrado | 122.7 |
| f5e0b9ad-2e4d-3c7d-a5e1-a6ecbe4d0cbf | -14.9372 | -46.7591 | 2025-10-11 02:10:00 | GOES-19 | FLORES DE GOIÁS | GOIÁS | Brasil | 5207907 | 52 | 33 | nan | nan | nan | Cerrado | 105.1 |
| bfc1e7aa-33d8-374f-80ad-29f1709119bf | -11.7499 | -47.0711 | 2025-10-11 02:10:00 | GOES-19 | DIANÓPOLIS | TOCANTINS | Brasil | 1707009 | 17 | 33 | nan | nan | nan | Cerrado | 56.9 |
| cd4dec64-06a6-3a51-bff9-e40531041fb1 | -17.2722 | -46.8932 | 2025-10-11 02:10:00 | GOES-19 | PARACATU | MINAS GERAIS | Brasil | 3147006 | 31 | 33 | nan | nan | nan | Cerrado | 93.0 |
| ef5ab3c8-4e3c-3b92-8f89-8cee964f3f35 | -8.5024 | -46.1995 | 2025-10-11 02:10:00 | GOES-19 | BALSAS | MARANHÃO | Brasil | 2101400 | 21 | 33 | nan | nan | nan | Cerrado | 140.6 |
| 74d6b962-8b7a-3dfc-8e64-92b3995eae1c | -13.2062 | -42.3206 | 2025-10-11 02:10:00 | GOES-19 | CATURAMA | BAHIA | Brasil | 2907558 | 29 | 33 | nan | nan | nan | Caatinga | 71.4 |
| 2593131b-0436-3d37-a306-72dd9f96be59 | -14.9572 | -46.7327 | 2025-10-11 02:10:00 | GOES-19 | FLORES DE GOIÁS | GOIÁS | Brasil | 5207907 | 52 | 33 | nan | nan | nan | Cerrado | 86.2 |
| a1eaaec2-6d1c-35b3-ab50-51af62ee18ca | -11.7308 | -47.0737 | 2025-10-11 02:10:00 | GOES-19 | DIANÓPOLIS | TOCANTINS | Brasil | 1707009 | 17 | 33 | nan | nan | nan | Cerrado | 62.6 |
| c2a55e97-38eb-3853-8147-ca0593473875 | -13.2252 | -42.3414 | 2025-10-11 02:10:00 | GOES-19 | CATURAMA | BAHIA | Brasil | 2907558 | 29 | 33 | nan | nan | nan | Caatinga | 285.2 |
| 525ebece-99e7-3acd-afb6-e729c204ae74 | -13.2257 | -42.317 | 2025-10-11 02:10:00 | GOES-19 | CATURAMA | BAHIA | Brasil | 2907558 | 29 | 33 | nan | nan | nan | Caatinga | 85.0 |
| 643c0f34-9097-395a-85d3-c8b4bac4a1d9 | -14.9567 | -46.7556 | 2025-10-11 02:10:00 | GOES-19 | FLORES DE GOIÁS | GOIÁS | Brasil | 5207907 | 52 | 33 | nan | nan | nan | Cerrado | 81.9 |
| 59990f78-5783-3cba-a9cc-7ef4ebbfceaf | -8.4835 | -46.2014 | 2025-10-11 02:20:00 | GOES-19 | BALSAS | MARANHÃO | Brasil | 2101400 | 21 | 33 | nan | nan | nan | Cerrado | 106.7 |
| 947a8251-771a-3d21-bb43-c5993699fedd | -8.4838 | -46.1789 | 2025-10-11 02:20:00 | GOES-19 | BALSAS | MARANHÃO | Brasil | 2101400 | 21 | 33 | nan | nan | nan | Cerrado | 93.2 |
| 4f4cbe5b-fcf8-312d-9f5a-65190b209736 | -5.852 | -42.8608 | 2025-10-11 02:20:00 | GOES-19 | PALMEIRAIS | PIAUÍ | Brasil | 2207504 | 22 | 33 | nan | nan | nan | Caatinga | 83.8 |
| 9df21231-3052-3416-9bb1-ccbc407bbd31 | -13.2057 | -42.345 | 2025-10-11 02:20:00 | GOES-19 | CATURAMA | BAHIA | Brasil | 2907558 | 29 | 33 | nan | nan | nan | Caatinga | 195.9 |
| 9f47a227-0ae1-35db-a951-2422417c3853 | -5.871 | -42.8357 | 2025-10-11 02:20:00 | GOES-19 | PALMEIRAIS | PIAUÍ | Brasil | 2207504 | 22 | 33 | nan | nan | nan | Caatinga | 78.7 |
| cb06fbb7-8224-3b94-9ec3-f7bceb6c7a6f | -8.5029 | -46.1545 | 2025-10-11 02:20:00 | GOES-19 | BALSAS | MARANHÃO | Brasil | 2101400 | 21 | 33 | nan | nan | nan | Cerrado | 67.0 |
| 82a9eb11-df75-3071-8964-9c93308c3d1d | -14.9377 | -46.7361 | 2025-10-11 02:20:00 | GOES-19 | FLORES DE GOIÁS | GOIÁS | Brasil | 5207907 | 52 | 33 | nan | nan | nan | Cerrado | 87.9 |
| 02ba8e9e-c5cc-3e50-ab21-b4620c7d6e84 | -8.5024 | -46.1995 | 2025-10-11 02:20:00 | GOES-19 | BALSAS | MARANHÃO | Brasil | 2101400 | 21 | 33 | nan | nan | nan | Cerrado | 83.2 |
| f9e19c93-98b3-38b9-83e8-76021162e3b4 | -17.2722 | -46.8932 | 2025-10-11 02:20:00 | GOES-19 | PARACATU | MINAS GERAIS | Brasil | 3147006 | 31 | 33 | nan | nan | nan | Cerrado | 88.5 |
| 27c6fb33-3388-3954-ba34-504db5b3a70c | -9.8152 | -45.512 | 2025-10-11 02:20:00 | GOES-19 | GILBUÉS | PIAUÍ | Brasil | 2204402 | 22 | 33 | nan | nan | nan | Cerrado | 71.5 |
| 64fe9bf7-33b2-3eb4-82d4-2a0b30c77ac2 | -6.1112 | -47.2897 | 2025-10-11 02:20:00 | GOES-19 | CAMPESTRE DO MARANHÃO | MARANHÃO | Brasil | 2102556 | 21 | 33 | nan | nan | nan | Cerrado | 77.2 |
| 625ab717-761b-3ad7-bbfb-bc02b5adb0e3 | -14.9372 | -46.7591 | 2025-10-11 02:20:00 | GOES-19 | FLORES DE GOIÁS | GOIÁS | Brasil | 5207907 | 52 | 33 | nan | nan | nan | Cerrado | 104.9 |
| 4e32119d-bcad-393f-a84c-49a8db845b00 | -8.5027 | -46.177 | 2025-10-11 02:20:00 | GOES-19 | BALSAS | MARANHÃO | Brasil | 2101400 | 21 | 33 | nan | nan | nan | Cerrado | 90.6 |
| acd6c1b4-8520-30ca-af12-71d5295286e2 | -8.4841 | -46.1564 | 2025-10-11 02:20:00 | GOES-19 | BALSAS | MARANHÃO | Brasil | 2101400 | 21 | 33 | nan | nan | nan | Cerrado | 56.3 |
| 74a694fe-559a-330c-85bb-12312ba4265d | -8.1996 | -43.3189 | 2025-10-11 02:20:00 | GOES-19 | CANTO DO BURITI | PIAUÍ | Brasil | 2202307 | 22 | 33 | nan | nan | nan | Caatinga | 82.6 |
| 404530c0-ea67-348e-b391-b5c0e58e330c | -5.8522 | -42.8372 | 2025-10-11 02:20:00 | GOES-19 | SÃO PEDRO DO PIAUÍ | PIAUÍ | Brasil | 2210508 | 22 | 33 | nan | nan | nan | Caatinga | 71.4 |
| a8d08255-68ff-3394-9190-ef423096d015 | -5.8708 | -42.8593 | 2025-10-11 02:20:00 | GOES-19 | PALMEIRAIS | PIAUÍ | Brasil | 2207504 | 22 | 33 | nan | nan | nan | Caatinga | 90.8 |
| f0ed1773-128e-3319-b6f1-4488078ad1e9 | -13.2257 | -42.317 | 2025-10-11 02:20:00 | GOES-19 | CATURAMA | BAHIA | Brasil | 2907558 | 29 | 33 | nan | nan | nan | Caatinga | 96.2 |
| 0e8824a9-5118-3bb9-a6cd-c8a5e2517645 | -6.111 | -47.3116 | 2025-10-11 02:20:00 | GOES-19 | CAMPESTRE DO MARANHÃO | MARANHÃO | Brasil | 2102556 | 21 | 33 | nan | nan | nan | Cerrado | 88.4 |
| 92d9a29c-6e30-3e85-9665-bc88a401e0c1 | -13.2062 | -42.3206 | 2025-10-11 02:20:00 | GOES-19 | CATURAMA | BAHIA | Brasil | 2907558 | 29 | 33 | nan | nan | nan | Caatinga | 69.3 |
| c2425e7c-c246-300d-b12c-362649093fb3 | -13.2252 | -42.3414 | 2025-10-11 02:20:00 | GOES-19 | CATURAMA | BAHIA | Brasil | 2907558 | 29 | 33 | nan | nan | nan | Caatinga | 232.1 |
| 287f0963-ef0b-31c6-acd8-89fa97d5b983 | -5.8522 | -42.8372 | 2025-10-11 02:30:00 | GOES-19 | SÃO PEDRO DO PIAUÍ | PIAUÍ | Brasil | 2210508 | 22 | 33 | nan | nan | nan | Caatinga | 80.6 |
| f5e528bd-2faa-350e-8d3b-3e5e23338788 | -14.9372 | -46.7591 | 2025-10-11 02:30:00 | GOES-19 | FLORES DE GOIÁS | GOIÁS | Brasil | 5207907 | 52 | 33 | nan | nan | nan | Cerrado | 90.6 |
| 95b7aa58-1663-3a28-9998-48559b22f8ed | -5.871 | -42.8357 | 2025-10-11 02:30:00 | GOES-19 | PALMEIRAIS | PIAUÍ | Brasil | 2207504 | 22 | 33 | nan | nan | nan | Caatinga | 68.5 |
| c7f85aca-4f0d-33ce-b58c-253ff256d3e0 | -5.8708 | -42.8593 | 2025-10-11 02:30:00 | GOES-19 | PALMEIRAIS | PIAUÍ | Brasil | 2207504 | 22 | 33 | nan | nan | nan | Caatinga | 106.3 |
| a1bf0751-6944-30ec-acad-9eb4b354a29d | -8.5024 | -46.1995 | 2025-10-11 02:30:00 | GOES-19 | BALSAS | MARANHÃO | Brasil | 2101400 | 21 | 33 | nan | nan | nan | Cerrado | 138.2 |
| 3d2b4a80-0620-3633-9713-9f128bbebaf4 | -8.5027 | -46.177 | 2025-10-11 02:30:00 | GOES-19 | BALSAS | MARANHÃO | Brasil | 2101400 | 21 | 33 | nan | nan | nan | Cerrado | 122.5 |
| 09f7d487-42ea-32b4-aaa7-26591dcc9801 | -13.2246 | -42.3657 | 2025-10-11 02:30:00 | GOES-19 | CATURAMA | BAHIA | Brasil | 2907558 | 29 | 33 | nan | nan | nan | Caatinga | 64.3 |
| e384b6a5-f383-35dd-be77-4c8fe488febd | -8.4835 | -46.2014 | 2025-10-11 02:30:00 | GOES-19 | BALSAS | MARANHÃO | Brasil | 2101400 | 21 | 33 | nan | nan | nan | Cerrado | 229.3 |
| 33dbdb96-4356-33bb-b096-70ea77a0a299 | -12.2383 | -51.1332 | 2025-10-11 02:30:00 | GOES-19 | NOVO SANTO ANTÔNIO | MATO GROSSO | Brasil | 5106315 | 51 | 33 | nan | nan | nan | Cerrado | 149.3 |
| 7c64ee94-9d01-33dc-a084-ae6b0a731a76 | -9.8152 | -45.512 | 2025-10-11 02:30:00 | GOES-19 | GILBUÉS | PIAUÍ | Brasil | 2204402 | 22 | 33 | nan | nan | nan | Cerrado | 78.6 |
| 64198dfa-1dc6-34e7-85fd-c7ebc82f77aa | -13.2252 | -42.3414 | 2025-10-11 02:30:00 | GOES-19 | CATURAMA | BAHIA | Brasil | 2907558 | 29 | 33 | nan | nan | nan | Caatinga | 209.8 |
| 8db8cbde-84f8-3df0-b34f-a75527d729a4 | -8.5029 | -46.1545 | 2025-10-11 02:30:00 | GOES-19 | BALSAS | MARANHÃO | Brasil | 2101400 | 21 | 33 | nan | nan | nan | Cerrado | 92.1 |
| 3f360b3a-e7e8-3e9e-a554-c5cf039ded17 | -5.852 | -42.8608 | 2025-10-11 02:30:00 | GOES-19 | PALMEIRAIS | PIAUÍ | Brasil | 2207504 | 22 | 33 | nan | nan | nan | Caatinga | 132.9 |
| fda770b7-22c5-3c71-a911-1ab4045fb4b2 | -8.4841 | -46.1564 | 2025-10-11 02:30:00 | GOES-19 | BALSAS | MARANHÃO | Brasil | 2101400 | 21 | 33 | nan | nan | nan | Cerrado | 49.6 |


[Clique aqui para ver as próximas entradas](README5.md)
