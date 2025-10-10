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

## Dados Diários - Página 54

| ID | Latitude | Longitude | Data/Hora GMT | Satélite | Município | Estado | País | Município ID | Estado ID | País ID | Dias sem Chuva | Precipitação | Risco de Fogo | Bioma | FRP |
|----|----------|-----------|---------------|----------|-----------|--------|------|--------------|-----------|---------|----------------|--------------|----------------|-------|-----|
| 8c71b467-1998-3435-814a-295fcf1b1c1b | -12.0785 | -47.9849 | 2025-10-10 14:10:00 | GOES-19 | PARANÃ | TOCANTINS | Brasil | 1716208 | 17 | 33 | nan | nan | nan | Cerrado | 70.8 |
| b5d1df06-2288-30f9-84c7-ff935d5c7d0b | -4.0567 | -42.5354 | 2025-10-10 14:10:00 | GOES-19 | NOSSA SENHORA DOS REMÉDIOS | PIAUÍ | Brasil | 2206803 | 22 | 33 | nan | nan | nan | Caatinga | 114.1 |
| f88c88a5-2cdb-38c4-9196-3cbac2391c78 | -15.3938 | -47.2938 | 2025-10-10 14:10:00 | GOES-19 | FORMOSA | GOIÁS | Brasil | 5208004 | 52 | 33 | nan | nan | nan | Cerrado | 169.5 |
| 0452fa2d-ce16-3642-acdb-7ca4f6b54f7c | -10.1707 | -44.5959 | 2025-10-10 14:10:00 | GOES-19 | PARNAGUÁ | PIAUÍ | Brasil | 2207603 | 22 | 33 | nan | nan | nan | Cerrado | 86.9 |
| e0a0ac9d-7818-3e5a-b7d4-22f9d4a8c602 | -13.8496 | -45.8223 | 2025-10-10 14:10:00 | GOES-19 | JABORANDI | BAHIA | Brasil | 2917359 | 29 | 33 | nan | nan | nan | Cerrado | 106.9 |
| 9b915a47-da61-3ea4-972c-4ccceb4d2338 | -12.9179 | -45.075 | 2025-10-10 14:10:00 | GOES-19 | SÃO DESIDÉRIO | BAHIA | Brasil | 2928901 | 29 | 33 | nan | nan | nan | Cerrado | 100.3 |
| f16272e7-36bf-3084-9281-c443800573c7 | -8.1055 | -44.7891 | 2025-10-10 14:10:00 | GOES-19 | URUÇUÍ | PIAUÍ | Brasil | 2211209 | 22 | 33 | nan | nan | nan | Cerrado | 59.2 |
| df2c9bd0-833f-3905-972e-05803ac739cf | -8.5016 | -46.2669 | 2025-10-10 14:10:00 | GOES-19 | BALSAS | MARANHÃO | Brasil | 2101400 | 21 | 33 | nan | nan | nan | Cerrado | 91.6 |
| 978ef93c-598d-37ff-a30a-0503ed2453ef | -12.4705 | -47.4416 | 2025-10-10 14:10:00 | GOES-19 | PARANÃ | TOCANTINS | Brasil | 1716208 | 17 | 33 | nan | nan | nan | Cerrado | 62.4 |
| b6d1df4e-b112-31e9-91e7-87a0e9a7610c | -15.8288 | -43.7555 | 2025-10-10 14:10:00 | GOES-19 | SÃO JOÃO DA PONTE | MINAS GERAIS | Brasil | 3162401 | 31 | 33 | nan | nan | nan | Cerrado | 123.4 |
| a54c0d0e-9e40-3c82-998b-fbac0da18188 | -12.9422 | -46.8335 | 2025-10-10 14:10:00 | GOES-19 | ARRAIAS | TOCANTINS | Brasil | 1702406 | 17 | 33 | nan | nan | nan | Cerrado | 58.5 |
| af712f17-f754-3b2a-b5a1-0af55c84b488 | -16.7511 | -43.9887 | 2025-10-10 14:10:00 | GOES-19 | MONTES CLAROS | MINAS GERAIS | Brasil | 3143302 | 31 | 33 | nan | nan | nan | Cerrado | 125.1 |
| fc839da5-c6d6-352c-97ef-cd6f9edf7eb2 | -16.7505 | -44.0129 | 2025-10-10 14:10:00 | GOES-19 | MONTES CLAROS | MINAS GERAIS | Brasil | 3143302 | 31 | 33 | nan | nan | nan | Cerrado | 116.6 |
| 649c0493-1d31-3f8d-ad71-c7e3920860ff | -11.7585 | -43.3374 | 2025-10-10 14:10:00 | GOES-19 | IBOTIRAMA | BAHIA | Brasil | 2913200 | 29 | 33 | nan | nan | nan | Cerrado | 66.8 |
| 0155f764-4419-345a-bb35-50b74855fadd | -13.3052 | -48.0129 | 2025-10-10 14:10:00 | GOES-19 | CAVALCANTE | GOIÁS | Brasil | 5205307 | 52 | 33 | nan | nan | nan | Cerrado | 64.1 |
| 8c8fe117-7eee-3263-be84-c1f477d95452 | -8.1807 | -43.321 | 2025-10-10 14:10:00 | GOES-19 | CANTO DO BURITI | PIAUÍ | Brasil | 2202307 | 22 | 33 | nan | nan | nan | Caatinga | 237.5 |
| 149010b2-c3e6-35fb-a06e-e38a7f3683ee | -12.5541 | -48.1419 | 2025-10-10 14:10:00 | GOES-19 | PARANÃ | TOCANTINS | Brasil | 1716208 | 17 | 33 | nan | nan | nan | Cerrado | 69.7 |
| ba5d5bd5-c2e2-3be5-a342-73fbd8a9f093 | -9.4674 | -46.006 | 2025-10-10 14:10:00 | GOES-19 | ALTO PARNAÍBA | MARANHÃO | Brasil | 2100501 | 21 | 33 | nan | nan | nan | Cerrado | 83.3 |
| fc05eec0-beea-31b7-9c01-f7f1f0d0c75e | -4.0569 | -42.5118 | 2025-10-10 14:10:00 | GOES-19 | NOSSA SENHORA DOS REMÉDIOS | PIAUÍ | Brasil | 2206803 | 22 | 33 | nan | nan | nan | Caatinga | 163.4 |
| da7a4bae-2baa-3d4a-a601-563e74f55b4e | -8.5602 | -44.6264 | 2025-10-10 14:10:00 | GOES-19 | PALMEIRA DO PIAUÍ | PIAUÍ | Brasil | 2207405 | 22 | 33 | nan | nan | nan | Cerrado | 66.4 |
| f4529443-0b27-3e10-a28f-e2eb6333825f | -12.9377 | -45.0486 | 2025-10-10 14:10:00 | GOES-19 | SÃO DESIDÉRIO | BAHIA | Brasil | 2928901 | 29 | 33 | nan | nan | nan | Cerrado | 113.4 |
| 3b6187d6-3983-39f4-a914-bd75b7e096e1 | -8.9005 | -46.0233 | 2025-10-10 14:10:00 | GOES-19 | ALTO PARNAÍBA | MARANHÃO | Brasil | 2100501 | 21 | 33 | nan | nan | nan | Cerrado | 60.7 |
| 1ce1bc60-d0cd-30c3-ae4d-74b5a5c4d963 | -13.3295 | -47.7417 | 2025-10-10 14:10:00 | GOES-19 | PARANÃ | TOCANTINS | Brasil | 1716208 | 17 | 33 | nan | nan | nan | Cerrado | 64.9 |
| 31cf519c-1500-3e9f-bdf4-0d2762c58829 | -9.2973 | -46.0026 | 2025-10-10 14:10:00 | GOES-19 | ALTO PARNAÍBA | MARANHÃO | Brasil | 2100501 | 21 | 33 | nan | nan | nan | Cerrado | 86.4 |
| 4503722f-c88f-3146-8349-bccac4d09d14 | -14.8884 | -47.2226 | 2025-10-10 14:10:00 | GOES-19 | VILA BOA | GOIÁS | Brasil | 5222203 | 52 | 33 | nan | nan | nan | Cerrado | 122.2 |
| 71f6b5f4-d402-3c55-8a8f-96b695daa998 | -9.6363 | -46.0995 | 2025-10-10 14:10:00 | GOES-19 | ALTO PARNAÍBA | MARANHÃO | Brasil | 2100501 | 21 | 33 | nan | nan | nan | Cerrado | 73.7 |
| 38c75679-3236-3291-a8f5-fc0380a0792a | -8.5027 | -46.177 | 2025-10-10 14:10:00 | GOES-19 | BALSAS | MARANHÃO | Brasil | 2101400 | 21 | 33 | nan | nan | nan | Cerrado | 75.7 |
| 6fb5750f-499d-34dd-b773-e83e23f2871e | -8.199 | -43.3659 | 2025-10-10 14:10:00 | GOES-19 | CANTO DO BURITI | PIAUÍ | Brasil | 2202307 | 22 | 33 | nan | nan | nan | Caatinga | 154.6 |
| f285709c-a527-35ce-87f2-2bc4f6106601 | -14.2744 | -45.911 | 2025-10-10 14:10:00 | GOES-19 | JABORANDI | BAHIA | Brasil | 2917359 | 29 | 33 | nan | nan | nan | Cerrado | 178.7 |
| 7c258766-920d-3700-a4bc-a2543829e2fe | -8.8435 | -46.0519 | 2025-10-10 14:10:00 | GOES-19 | ALTO PARNAÍBA | MARANHÃO | Brasil | 2100501 | 21 | 33 | nan | nan | nan | Cerrado | 56.7 |
| ac6df017-7fa7-30b8-912e-48d47d0f87f0 | -9.4371 | -45.4656 | 2025-10-10 14:10:00 | GOES-19 | SANTA FILOMENA | PIAUÍ | Brasil | 2209203 | 22 | 33 | nan | nan | nan | Cerrado | 89.0 |
| 3113e2f1-d6ee-30d5-9a56-f5befbe107f9 | -14.9567 | -46.7556 | 2025-10-10 14:10:00 | GOES-19 | FLORES DE GOIÁS | GOIÁS | Brasil | 5207907 | 52 | 33 | nan | nan | nan | Cerrado | 113.7 |
| 1bb71719-8981-3ac7-a472-878f69d52b5f | -9.4677 | -45.9834 | 2025-10-10 14:10:00 | GOES-19 | ALTO PARNAÍBA | MARANHÃO | Brasil | 2100501 | 21 | 33 | nan | nan | nan | Cerrado | 76.0 |
| 1b6d2151-4526-3677-9d83-4550d5e265ee | -8.8621 | -46.0724 | 2025-10-10 14:10:00 | GOES-19 | ALTO PARNAÍBA | MARANHÃO | Brasil | 2100501 | 21 | 33 | nan | nan | nan | Cerrado | 81.0 |
| f2ff708a-2889-3023-aefe-ab5ae2b272d5 | -7.5089 | -42.7093 | 2025-10-10 14:10:00 | GOES-19 | FLORES DO PIAUÍ | PIAUÍ | Brasil | 2203800 | 22 | 33 | nan | nan | nan | Caatinga | 162.8 |
| 1be8b2c9-622f-37b4-8f98-c828bb7cc0e0 | -8.1618 | -43.323 | 2025-10-10 14:10:00 | GOES-19 | CANTO DO BURITI | PIAUÍ | Brasil | 2202307 | 22 | 33 | nan | nan | nan | Caatinga | 130.8 |
| fa8691b8-b9b5-3dd6-8392-ad2d7a569b83 | -11.6451 | -44.2966 | 2025-10-10 14:10:00 | GOES-19 | COTEGIPE | BAHIA | Brasil | 2909406 | 29 | 33 | nan | nan | nan | Cerrado | 96.1 |
| d2eecd4e-b2ea-348d-8682-e0d9a8abcef7 | -7.5466 | -44.2933 | 2025-10-10 14:10:00 | GOES-19 | URUÇUÍ | PIAUÍ | Brasil | 2211209 | 22 | 33 | nan | nan | nan | Cerrado | 96.8 |
| 47cb9bd2-ea06-31c8-944a-a4aee337f146 | -13.3057 | -47.9906 | 2025-10-10 14:10:00 | GOES-19 | CAVALCANTE | GOIÁS | Brasil | 5205307 | 52 | 33 | nan | nan | nan | Cerrado | 73.5 |
| 661b23ef-1f12-3ce8-a163-0c08baf48ecd | -12.4701 | -47.464 | 2025-10-10 14:10:00 | GOES-19 | PARANÃ | TOCANTINS | Brasil | 1716208 | 17 | 33 | nan | nan | nan | Cerrado | 67.2 |
| a8d663dd-b556-386c-8ca5-70fb21e8d5ba | -14.4258 | -47.9974 | 2025-10-10 14:10:00 | GOES-19 | NIQUELÂNDIA | GOIÁS | Brasil | 5214606 | 52 | 33 | nan | nan | nan | Cerrado | 87.3 |
| deddeb6b-3a89-3156-82f6-bc25203cbc32 | -14.2749 | -45.8879 | 2025-10-10 14:10:00 | GOES-19 | JABORANDI | BAHIA | Brasil | 2917359 | 29 | 33 | nan | nan | nan | Cerrado | 148.5 |
| 6f6464b6-265c-3c9a-96f0-af4ae9b75e87 | -14.9372 | -46.7591 | 2025-10-10 14:10:00 | GOES-19 | FLORES DE GOIÁS | GOIÁS | Brasil | 5207907 | 52 | 33 | nan | nan | nan | Cerrado | 137.9 |
| d7850962-3b8c-31da-81c9-30b5946f07bd | -8.4824 | -46.2912 | 2025-10-10 14:10:00 | GOES-19 | BALSAS | MARANHÃO | Brasil | 2101400 | 21 | 33 | nan | nan | nan | Cerrado | 68.5 |
| 838aacd1-57ad-325e-96fe-5bd1091860e4 | -10.1517 | -44.5984 | 2025-10-10 14:10:00 | GOES-19 | PARNAGUÁ | PIAUÍ | Brasil | 2207603 | 22 | 33 | nan | nan | nan | Cerrado | 88.1 |
| 41ae9298-03bb-3ca4-8b9b-c66cdd7a002d | -13.2859 | -48.0157 | 2025-10-10 14:10:00 | GOES-19 | CAVALCANTE | GOIÁS | Brasil | 5205307 | 52 | 33 | nan | nan | nan | Cerrado | 75.3 |
| fdb60434-a27c-3dec-bda8-6093350ec0e9 | -8.5055 | -45.9519 | 2025-10-10 14:10:00 | GOES-19 | TASSO FRAGOSO | MARANHÃO | Brasil | 2112001 | 21 | 33 | nan | nan | nan | Cerrado | 67.9 |
| 9909acd3-1f1c-36de-a1e8-45eb0a1d3dc6 | -13.3026 | -47.1174 | 2025-10-10 14:10:00 | GOES-19 | MONTE ALEGRE DE GOIÁS | GOIÁS | Brasil | 5213509 | 52 | 33 | nan | nan | nan | Cerrado | 100.3 |
| 9af8a9fb-4233-31f4-9c60-81ca5be921bd | -7.5086 | -42.7329 | 2025-10-10 14:10:00 | GOES-19 | FLORES DO PIAUÍ | PIAUÍ | Brasil | 2203800 | 22 | 33 | nan | nan | nan | Caatinga | 134.9 |
| 94bebb24-0c84-33b7-99cf-7a9ca8ea240b | -16.7312 | -43.9931 | 2025-10-10 14:10:00 | GOES-19 | MONTES CLAROS | MINAS GERAIS | Brasil | 3143302 | 31 | 33 | nan | nan | nan | Cerrado | 126.1 |
| f403e6b8-4d83-3f39-82d7-b7731e738aa1 | -10.1898 | -44.5934 | 2025-10-10 14:10:00 | GOES-19 | PARNAGUÁ | PIAUÍ | Brasil | 2207603 | 22 | 33 | nan | nan | nan | Cerrado | 134.5 |
| c35cd6b4-c6c0-3f72-a8f5-275c56820cd2 | -7.7924 | -44.1998 | 2025-10-10 14:10:00 | GOES-19 | SEBASTIÃO LEAL | PIAUÍ | Brasil | 2210631 | 22 | 33 | nan | nan | nan | Cerrado | 99.1 |
| d69d8b4f-6626-36b3-9808-035acf319876 | -8.6109 | -45.0792 | 2025-10-10 14:10:00 | GOES-19 | BAIXA GRANDE DO RIBEIRO | PIAUÍ | Brasil | 2201150 | 22 | 33 | nan | nan | nan | Cerrado | 69.4 |
| e90ec701-3013-39fb-8f8e-12b44729aa71 | -15.1548 | -45.73 | 2025-10-10 14:10:00 | GOES-19 | CHAPADA GAÚCHA | MINAS GERAIS | Brasil | 3116159 | 31 | 33 | nan | nan | nan | Cerrado | 83.4 |
| 7ebc10cc-5c70-34f6-97c7-15d518bee260 | -9.0022 | -45.4693 | 2025-10-10 14:10:00 | GOES-19 | BAIXA GRANDE DO RIBEIRO | PIAUÍ | Brasil | 2201150 | 22 | 33 | nan | nan | nan | Cerrado | 128.3 |
| 793e157e-fce6-383c-b2e3-59fb3373dc82 | -11.6852 | -47.5263 | 2025-10-10 14:10:00 | GOES-19 | NATIVIDADE | TOCANTINS | Brasil | 1714203 | 17 | 33 | nan | nan | nan | Cerrado | 53.0 |
| 36ae2767-81d4-3382-bc0e-7f348e6c917f | -8.1618 | -43.323 | 2025-10-10 14:20:00 | GOES-19 | CANTO DO BURITI | PIAUÍ | Brasil | 2202307 | 22 | 33 | nan | nan | nan | Caatinga | 189.5 |
| b70856c7-eead-3589-8df4-d7d76ca3dabc | -10.1707 | -44.5959 | 2025-10-10 14:20:00 | GOES-19 | PARNAGUÁ | PIAUÍ | Brasil | 2207603 | 22 | 33 | nan | nan | nan | Cerrado | 90.5 |
| 9b4aa262-746d-3ba9-b3e1-c07e33a413fd | -8.1429 | -43.3251 | 2025-10-10 14:20:00 | GOES-19 | CANTO DO BURITI | PIAUÍ | Brasil | 2202307 | 22 | 33 | nan | nan | nan | Caatinga | 94.7 |
| efd3d73a-3425-3c1b-9b0c-092e975266dc | -8.8435 | -46.0519 | 2025-10-10 14:20:00 | GOES-19 | ALTO PARNAÍBA | MARANHÃO | Brasil | 2100501 | 21 | 33 | nan | nan | nan | Cerrado | 56.0 |
| 0ffa13ad-1e6c-3538-9366-6330e931e72d | -11.761 | -46.4167 | 2025-10-10 14:20:00 | GOES-19 | NOVO JARDIM | TOCANTINS | Brasil | 1715259 | 17 | 33 | nan | nan | nan | Cerrado | 57.3 |
| 36de86dd-aec1-338f-941a-73dca4c520e7 | -4.0567 | -42.5354 | 2025-10-10 14:20:00 | GOES-19 | NOSSA SENHORA DOS REMÉDIOS | PIAUÍ | Brasil | 2206803 | 22 | 33 | nan | nan | nan | Caatinga | 108.1 |
| 4a83c202-f107-3622-b405-c794b7105105 | -7.8648 | -44.4461 | 2025-10-10 14:20:00 | GOES-19 | URUÇUÍ | PIAUÍ | Brasil | 2211209 | 22 | 33 | nan | nan | nan | Cerrado | 72.3 |
| 8ce3a35d-604e-3207-8787-966cd4b8eaf0 | -8.8432 | -46.0744 | 2025-10-10 14:20:00 | GOES-19 | ALTO PARNAÍBA | MARANHÃO | Brasil | 2100501 | 21 | 33 | nan | nan | nan | Cerrado | 57.2 |
| 381cb011-580b-37f2-a66d-3ff9128329be | -9.4674 | -46.006 | 2025-10-10 14:20:00 | GOES-19 | ALTO PARNAÍBA | MARANHÃO | Brasil | 2100501 | 21 | 33 | nan | nan | nan | Cerrado | 85.1 |
| add84a82-0786-3011-9147-b27971168494 | -7.5041 | -43.1106 | 2025-10-10 14:20:00 | GOES-19 | ITAUEIRA | PIAUÍ | Brasil | 2205102 | 22 | 33 | nan | nan | nan | Caatinga | 93.7 |
| 552a0016-4a33-37a9-a215-5157fe5f43cc | -9.2973 | -46.0026 | 2025-10-10 14:20:00 | GOES-19 | ALTO PARNAÍBA | MARANHÃO | Brasil | 2100501 | 21 | 33 | nan | nan | nan | Cerrado | 89.1 |
| ca371aa9-00ee-3ddf-9fed-f45b9812efc4 | -8.5602 | -44.6264 | 2025-10-10 14:20:00 | GOES-19 | PALMEIRA DO PIAUÍ | PIAUÍ | Brasil | 2207405 | 22 | 33 | nan | nan | nan | Cerrado | 58.9 |
| b07d98b7-2242-3851-af23-6314b13177fb | -13.2859 | -48.0157 | 2025-10-10 14:20:00 | GOES-19 | CAVALCANTE | GOIÁS | Brasil | 5205307 | 52 | 33 | nan | nan | nan | Cerrado | 65.6 |
| 0280bfbf-2c89-3130-9390-09f773032541 | -8.208 | -44.1337 | 2025-10-10 14:20:00 | GOES-19 | SEBASTIÃO LEAL | PIAUÍ | Brasil | 2210631 | 22 | 33 | nan | nan | nan | Cerrado | 103.5 |
| f7e0c906-95b7-3f6a-b492-9a08eff12519 | -4.0569 | -42.5118 | 2025-10-10 14:20:00 | GOES-19 | NOSSA SENHORA DOS REMÉDIOS | PIAUÍ | Brasil | 2206803 | 22 | 33 | nan | nan | nan | Caatinga | 155.1 |
| f259f730-4209-3e3d-b12e-0a1e37c89ed5 | -13.3022 | -47.14 | 2025-10-10 14:20:00 | GOES-19 | MONTE ALEGRE DE GOIÁS | GOIÁS | Brasil | 5213509 | 52 | 33 | nan | nan | nan | Cerrado | 75.3 |
| beb64038-cf31-376b-9e3f-b5a9f3abaa91 | -12.5541 | -48.1419 | 2025-10-10 14:20:00 | GOES-19 | PARANÃ | TOCANTINS | Brasil | 1716208 | 17 | 33 | nan | nan | nan | Cerrado | 68.3 |
| a87b1883-d13b-3283-b0fe-733e20f0972a | -8.2176 | -43.3873 | 2025-10-10 14:20:00 | GOES-19 | CANTO DO BURITI | PIAUÍ | Brasil | 2202307 | 22 | 33 | nan | nan | nan | Caatinga | 73.6 |
| 904fb3aa-1b12-35fb-a3bd-59845eb08c09 | -11.7585 | -43.3374 | 2025-10-10 14:20:00 | GOES-19 | IBOTIRAMA | BAHIA | Brasil | 2913200 | 29 | 33 | nan | nan | nan | Cerrado | 91.2 |
| 0ee799e6-2c8e-3565-b6a5-f037ea84238e | -10.1898 | -44.5934 | 2025-10-10 14:20:00 | GOES-19 | PARNAGUÁ | PIAUÍ | Brasil | 2207603 | 22 | 33 | nan | nan | nan | Cerrado | 136.8 |
| 51c14c8b-551b-3eb8-89d1-cb19d59d5016 | -13.8307 | -45.8024 | 2025-10-10 14:20:00 | GOES-19 | JABORANDI | BAHIA | Brasil | 2917359 | 29 | 33 | nan | nan | nan | Cerrado | 181.3 |
| b5f66fc2-1bd3-36bd-be64-60524496f5fb | -7.5277 | -44.2952 | 2025-10-10 14:20:00 | GOES-19 | URUÇUÍ | PIAUÍ | Brasil | 2211209 | 22 | 33 | nan | nan | nan | Cerrado | 90.9 |
| 415e4d93-9d7c-3f2c-bcf9-c30065eb25ad | -11.6852 | -47.5263 | 2025-10-10 14:20:00 | GOES-19 | NATIVIDADE | TOCANTINS | Brasil | 1714203 | 17 | 33 | nan | nan | nan | Cerrado | 53.5 |
| 7998e3d4-136f-3ec4-86e6-8672d81ef3f5 | -7.5086 | -42.7329 | 2025-10-10 14:20:00 | GOES-19 | FLORES DO PIAUÍ | PIAUÍ | Brasil | 2203800 | 22 | 33 | nan | nan | nan | Caatinga | 138.3 |
| 2e86bcb1-74ab-388d-8378-78c70750b20d | -7.9963 | -44.4788 | 2025-10-10 14:20:00 | GOES-19 | URUÇUÍ | PIAUÍ | Brasil | 2211209 | 22 | 33 | nan | nan | nan | Cerrado | 64.7 |
| addb69b6-1586-38a7-af4f-5160c6f4c445 | 0.9476 | -51.1868 | 2025-10-10 14:20:00 | GOES-19 | FERREIRA GOMES | AMAPÁ | Brasil | 1600238 | 16 | 33 | nan | nan | nan | Amazônia | 79.7 |
| 441ca67c-a2b6-3f68-9f25-3ab52aa33373 | -9.6363 | -46.0995 | 2025-10-10 14:20:00 | GOES-19 | ALTO PARNAÍBA | MARANHÃO | Brasil | 2100501 | 21 | 33 | nan | nan | nan | Cerrado | 66.1 |
| 93fa9185-33aa-3aba-a822-1c5bf043921d | -8.5055 | -45.9519 | 2025-10-10 14:20:00 | GOES-19 | TASSO FRAGOSO | MARANHÃO | Brasil | 2112001 | 21 | 33 | nan | nan | nan | Cerrado | 74.7 |
| fd9a015a-3278-3e7c-aece-2b1bae5c2c96 | -8.2077 | -44.1568 | 2025-10-10 14:20:00 | GOES-19 | SEBASTIÃO LEAL | PIAUÍ | Brasil | 2210631 | 22 | 33 | nan | nan | nan | Cerrado | 112.2 |
| 204f7d92-8d46-3a97-ba7a-99927e8b7a79 | -10.1714 | -44.5496 | 2025-10-10 14:20:00 | GOES-19 | PARNAGUÁ | PIAUÍ | Brasil | 2207603 | 22 | 33 | nan | nan | nan | Cerrado | 93.3 |
| c40eaebc-a144-3385-b7cd-12b68dc20ac2 | -13.3963 | -47.2607 | 2025-10-10 14:20:00 | GOES-19 | MONTE ALEGRE DE GOIÁS | GOIÁS | Brasil | 5213509 | 52 | 33 | nan | nan | nan | Cerrado | 64.8 |
| e943caaa-c5f1-34eb-a653-485da71a92f5 | -7.5089 | -42.7093 | 2025-10-10 14:20:00 | GOES-19 | FLORES DO PIAUÍ | PIAUÍ | Brasil | 2203800 | 22 | 33 | nan | nan | nan | Caatinga | 137.4 |
| e8fcd3e8-445f-383a-b00f-a166ffcfb580 | -16.7511 | -43.9887 | 2025-10-10 14:20:00 | GOES-19 | MONTES CLAROS | MINAS GERAIS | Brasil | 3143302 | 31 | 33 | nan | nan | nan | Cerrado | 141.3 |
| 1c89e079-cbd8-36bf-8ed7-d53694f4d84c | -12.9619 | -46.808 | 2025-10-10 14:20:00 | GOES-19 | ARRAIAS | TOCANTINS | Brasil | 1702406 | 17 | 33 | nan | nan | nan | Cerrado | 67.6 |
| 1d198af0-d3e3-3804-87b9-eda19c5690e9 | -14.8884 | -47.2226 | 2025-10-10 14:20:00 | GOES-19 | VILA BOA | GOIÁS | Brasil | 5222203 | 52 | 33 | nan | nan | nan | Cerrado | 128.6 |
| 69fff272-8dba-3277-b83e-e0f042a0e0e9 | -8.1807 | -43.321 | 2025-10-10 14:20:00 | GOES-19 | CANTO DO BURITI | PIAUÍ | Brasil | 2202307 | 22 | 33 | nan | nan | nan | Caatinga | 207.6 |
| b1b70897-386e-3363-bd4f-1e4f941521ed | -13.3057 | -47.9906 | 2025-10-10 14:20:00 | GOES-19 | CAVALCANTE | GOIÁS | Brasil | 5205307 | 52 | 33 | nan | nan | nan | Cerrado | 87.8 |
| 8420e754-a6ea-3cde-84ad-867d35350100 | -8.8729 | -46.6985 | 2025-10-10 14:20:00 | GOES-19 | BALSAS | MARANHÃO | Brasil | 2101400 | 21 | 33 | nan | nan | nan | Cerrado | 61.2 |
| a6245613-0611-3c3a-9922-818378e19426 | -13.8311 | -45.7793 | 2025-10-10 14:20:00 | GOES-19 | JABORANDI | BAHIA | Brasil | 2917359 | 29 | 33 | nan | nan | nan | Cerrado | 142.5 |
| 87aef78c-0b64-3e35-b94c-37cf7173bcd4 | -12.9426 | -46.8109 | 2025-10-10 14:20:00 | GOES-19 | ARRAIAS | TOCANTINS | Brasil | 1702406 | 17 | 33 | nan | nan | nan | Cerrado | 64.2 |
| 88166ca3-1f98-3e07-8a2a-75b931918284 | -4.1429 | -38.2667 | 2025-10-10 14:20:00 | GOES-19 | CASCAVEL | CEARÁ | Brasil | 2303501 | 23 | 33 | nan | nan | nan | Caatinga | 82.8 |
| 1dca2aa9-838f-3441-8be5-9727140ea166 | -8.2269 | -44.1316 | 2025-10-10 14:20:00 | GOES-19 | SEBASTIÃO LEAL | PIAUÍ | Brasil | 2210631 | 22 | 33 | nan | nan | nan | Cerrado | 78.9 |
| 3a6b75c7-b48b-31d8-8965-37ff057dff3c | -11.6278 | -47.5338 | 2025-10-10 14:20:00 | GOES-19 | NATIVIDADE | TOCANTINS | Brasil | 1714203 | 17 | 33 | nan | nan | nan | Cerrado | 52.4 |
| 07ee772e-e9c2-3544-8a4e-45093e9d21e4 | -14.4253 | -48.0199 | 2025-10-10 14:20:00 | GOES-19 | NIQUELÂNDIA | GOIÁS | Brasil | 5214606 | 52 | 33 | nan | nan | nan | Cerrado | 114.8 |


[Clique aqui para ver as próximas entradas](README55.md)
