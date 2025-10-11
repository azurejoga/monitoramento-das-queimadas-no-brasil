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

## Dados Diários - Página 14

| ID | Latitude | Longitude | Data/Hora GMT | Satélite | Município | Estado | País | Município ID | Estado ID | País ID | Dias sem Chuva | Precipitação | Risco de Fogo | Bioma | FRP |
|----|----------|-----------|---------------|----------|-----------|--------|------|--------------|-----------|---------|----------------|--------------|----------------|-------|-----|
| 65280c2c-f920-3fa4-9fd6-09a24bddb332 | -13.24027 | -46.47961 | 2025-10-11 03:45:00 | NOAA-20 | DIVINÓPOLIS DE GOIÁS | GOIÁS | Brasil | 5208301 | 52 | 33 | nan | nan | nan | Cerrado | 1.6 |
| 57670b3d-2c95-33ac-b790-33370f89d8a2 | -14.92481 | -46.75946 | 2025-10-11 03:45:00 | NOAA-20 | FLORES DE GOIÁS | GOIÁS | Brasil | 5207907 | 52 | 33 | nan | nan | nan | Cerrado | 1.3 |
| 05768a60-8c8b-31db-bc3d-c6cc9ddcf543 | -15.69731 | -46.63006 | 2025-10-11 03:45:00 | NOAA-20 | BURITIS | MINAS GERAIS | Brasil | 3109303 | 31 | 33 | nan | nan | nan | Cerrado | 2.2 |
| a4711728-ad33-3f92-b91d-e331d9dd338b | -16.53442 | -46.73235 | 2025-10-11 03:45:00 | NOAA-20 | UNAÍ | MINAS GERAIS | Brasil | 3170404 | 31 | 33 | nan | nan | nan | Cerrado | 0.3 |
| 1cc4816c-1472-3ec1-82dd-c2b902575b35 | -15.3101 | -40.94384 | 2025-10-11 03:45:00 | NOAA-20 | VITÓRIA DA CONQUISTA | BAHIA | Brasil | 2933307 | 29 | 33 | nan | nan | nan | Mata Atlântica | 1.0 |
| fb9ae083-cb40-3727-a5be-413fe254bb9c | -15.60612 | -42.67196 | 2025-10-11 03:45:00 | NOAA-20 | RIO PARDO DE MINAS | MINAS GERAIS | Brasil | 3155603 | 31 | 33 | nan | nan | nan | Cerrado | 2.9 |
| f97225d8-f6a5-32c0-a500-bbe23dcc858b | -17.26491 | -46.90808 | 2025-10-11 03:45:00 | NOAA-20 | PARACATU | MINAS GERAIS | Brasil | 3147006 | 31 | 33 | nan | nan | nan | Cerrado | 7.3 |
| 2ce9c24d-401f-31a5-a87c-cfd8ff11f94e | -16.2963 | -47.17451 | 2025-10-11 03:45:00 | NOAA-20 | UNAÍ | MINAS GERAIS | Brasil | 3170404 | 31 | 33 | nan | nan | nan | Cerrado | 2.8 |
| 396c5580-b867-37b1-9696-1ed802719a13 | -14.74012 | -46.12312 | 2025-10-11 03:45:00 | NOAA-20 | SÍTIO D'ABADIA | GOIÁS | Brasil | 5220702 | 52 | 33 | nan | nan | nan | Cerrado | 1.0 |
| 024fb81a-d508-3cfa-a0d6-cc1ad8364a67 | -17.7128 | -42.61748 | 2025-10-11 03:45:00 | NOAA-20 | ITAMARANDIBA | MINAS GERAIS | Brasil | 3132503 | 31 | 33 | nan | nan | nan | Mata Atlântica | 0.9 |
| 853084d0-5d18-3bb4-b0fe-28680d746239 | -17.26555 | -46.90495 | 2025-10-11 03:45:00 | NOAA-20 | PARACATU | MINAS GERAIS | Brasil | 3147006 | 31 | 33 | nan | nan | nan | Cerrado | 21.0 |
| 465f0889-388c-3d0b-b9a7-de811d1be8f1 | -15.31326 | -46.18857 | 2025-10-11 03:45:00 | NOAA-20 | FORMOSO | MINAS GERAIS | Brasil | 3126208 | 31 | 33 | nan | nan | nan | Cerrado | 0.7 |
| 010485c1-076b-3603-aa96-d62755508787 | -13.31165 | -47.12706 | 2025-10-11 03:45:00 | NOAA-20 | MONTE ALEGRE DE GOIÁS | GOIÁS | Brasil | 5213509 | 52 | 33 | nan | nan | nan | Cerrado | 1.9 |
| 0259fbbd-24e7-3cac-a41c-e04f9a65e3fc | -14.94363 | -46.75023 | 2025-10-11 03:45:00 | NOAA-20 | FLORES DE GOIÁS | GOIÁS | Brasil | 5207907 | 52 | 33 | nan | nan | nan | Cerrado | 6.1 |
| 4433e2b6-f2dc-3d47-bd04-fd7649cd36f9 | -15.82777 | -42.02512 | 2025-10-11 03:45:00 | NOAA-20 | TAIOBEIRAS | MINAS GERAIS | Brasil | 3168002 | 31 | 33 | nan | nan | nan | Mata Atlântica | 0.4 |
| cb044211-a663-3630-921a-27a795a769de | -13.45218 | -48.09962 | 2025-10-11 03:45:00 | NOAA-20 | CAVALCANTE | GOIÁS | Brasil | 5205307 | 52 | 33 | nan | nan | nan | Cerrado | 5.2 |
| ea0d690a-171a-320d-9744-17650c8ca615 | -15.22039 | -47.91119 | 2025-10-11 03:45:00 | NOAA-20 | PLANALTINA | GOIÁS | Brasil | 5217609 | 52 | 33 | nan | nan | nan | Cerrado | 4.4 |
| d7167ca2-8af2-3ec7-ab5b-9c41b3daff46 | -15.32578 | -43.19061 | 2025-10-11 03:45:00 | NOAA-20 | CATUTI | MINAS GERAIS | Brasil | 3115474 | 31 | 33 | nan | nan | nan | Caatinga | 0.9 |
| 1562bd0f-719c-3177-9ae2-15ae8366a157 | -13.32333 | -47.12812 | 2025-10-11 03:45:00 | NOAA-20 | MONTE ALEGRE DE GOIÁS | GOIÁS | Brasil | 5213509 | 52 | 33 | nan | nan | nan | Cerrado | 4.8 |
| be0f5586-5ef7-357c-9017-64ddc22e7003 | -17.39871 | -46.86576 | 2025-10-11 03:45:00 | NOAA-20 | PARACATU | MINAS GERAIS | Brasil | 3147006 | 31 | 33 | nan | nan | nan | Cerrado | 1.6 |
| 7b6e743d-eba5-384d-b1aa-33c15d3f1af7 | -14.26807 | -45.87658 | 2025-10-11 03:45:00 | NOAA-20 | JABORANDI | BAHIA | Brasil | 2917359 | 29 | 33 | nan | nan | nan | Cerrado | 1.3 |
| 11b421e4-388e-32cc-9ffd-ce2f9c8d580e | -16.31098 | -47.15816 | 2025-10-11 03:45:00 | NOAA-20 | UNAÍ | MINAS GERAIS | Brasil | 3170404 | 31 | 33 | nan | nan | nan | Cerrado | 2.4 |
| ae704af1-4d4e-35e5-aff0-16d82288f1c4 | -16.30635 | -47.15324 | 2025-10-11 03:45:00 | NOAA-20 | UNAÍ | MINAS GERAIS | Brasil | 3170404 | 31 | 33 | nan | nan | nan | Cerrado | 2.4 |
| d42ad671-d497-3785-980e-54a73fcec5e1 | -17.20786 | -47.65599 | 2025-10-11 03:45:00 | NOAA-20 | IPAMERI | GOIÁS | Brasil | 5210109 | 52 | 33 | nan | nan | nan | Cerrado | 4.7 |
| d59aaa8d-953b-3106-af54-e18358d5b670 | -13.45354 | -48.09827 | 2025-10-11 03:45:00 | NOAA-20 | CAVALCANTE | GOIÁS | Brasil | 5205307 | 52 | 33 | nan | nan | nan | Cerrado | 4.6 |
| 158e28a1-ede2-330e-8c08-72bac608376d | -13.84234 | -45.80693 | 2025-10-11 03:45:00 | NOAA-20 | JABORANDI | BAHIA | Brasil | 2917359 | 29 | 33 | nan | nan | nan | Cerrado | 1.1 |
| 542b83ef-4425-3d42-ba0f-518aee9438c1 | -12.74902 | -48.64696 | 2025-10-11 03:45:00 | NOAA-20 | JAÚ DO TOCANTINS | TOCANTINS | Brasil | 1711506 | 17 | 33 | nan | nan | nan | Cerrado | 5.1 |
| 1fb50b3f-6af3-32ea-9415-e0753740dfe9 | -13.65962 | -48.74745 | 2025-10-11 03:45:00 | NOAA-20 | FORMOSO | GOIÁS | Brasil | 5208103 | 52 | 33 | nan | nan | nan | Cerrado | 2.3 |
| 15ccb55e-df95-3859-9aa7-5c7d8879ade4 | -14.01271 | -47.05757 | 2025-10-11 03:45:00 | NOAA-20 | NOVA ROMA | GOIÁS | Brasil | 5214903 | 52 | 33 | nan | nan | nan | Cerrado | 1.4 |
| 2d40dfd6-a3b6-37d5-bb35-1b68555c8f76 | -16.30246 | -47.17205 | 2025-10-11 03:45:00 | NOAA-20 | UNAÍ | MINAS GERAIS | Brasil | 3170404 | 31 | 33 | nan | nan | nan | Cerrado | 5.5 |
| 6415dd96-3cd6-37b1-8646-944e5a851540 | -16.59127 | -41.11346 | 2025-10-11 03:45:00 | NOAA-20 | JEQUITINHONHA | MINAS GERAIS | Brasil | 3135803 | 31 | 33 | nan | nan | nan | Mata Atlântica | 3.1 |
| 9b6c0b35-534c-3065-b958-12b1c64d6f46 | -14.74023 | -46.12213 | 2025-10-11 03:45:00 | NOAA-20 | SÍTIO D'ABADIA | GOIÁS | Brasil | 5220702 | 52 | 33 | nan | nan | nan | Cerrado | 1.2 |
| 3efefa58-32ae-3682-84d3-f75a675eba1a | -14.94291 | -46.75377 | 2025-10-11 03:45:00 | NOAA-20 | FLORES DE GOIÁS | GOIÁS | Brasil | 5207907 | 52 | 33 | nan | nan | nan | Cerrado | 6.1 |
| 1675c732-4e95-3a20-9d0a-1f32d51d1659 | -12.74295 | -48.64442 | 2025-10-11 03:45:00 | NOAA-20 | JAÚ DO TOCANTINS | TOCANTINS | Brasil | 1711506 | 17 | 33 | nan | nan | nan | Cerrado | 6.1 |
| 53ca3885-6f03-3aa6-b1fc-30b3a761c378 | -19.08648 | -46.41298 | 2025-10-11 03:45:00 | NOAA-20 | RIO PARANAÍBA | MINAS GERAIS | Brasil | 3155504 | 31 | 33 | nan | nan | nan | Cerrado | 3.8 |
| 7fd5faa3-f864-3271-a555-4161cbe2226a | -14.74269 | -46.13731 | 2025-10-11 03:45:00 | NOAA-20 | SÍTIO D'ABADIA | GOIÁS | Brasil | 5220702 | 52 | 33 | nan | nan | nan | Cerrado | 0.8 |
| 77c04641-5d4c-3d46-b7c2-e518145b13b9 | -17.66973 | -46.81798 | 2025-10-11 03:45:00 | NOAA-20 | VAZANTE | MINAS GERAIS | Brasil | 3171006 | 31 | 33 | nan | nan | nan | Cerrado | 1.6 |
| f9f64776-bc58-3848-907e-7b48d8d35b15 | -15.01434 | -47.57051 | 2025-10-11 03:45:00 | NOAA-20 | FORMOSA | GOIÁS | Brasil | 5208004 | 52 | 33 | nan | nan | nan | Cerrado | 1.9 |
| 546ace38-4a62-33bc-ad73-9e005cc23301 | -13.41934 | -47.25211 | 2025-10-11 03:45:00 | NOAA-20 | MONTE ALEGRE DE GOIÁS | GOIÁS | Brasil | 5213509 | 52 | 33 | nan | nan | nan | Cerrado | 3.0 |
| 85f2e43e-f5d0-3856-9628-2006483126c2 | -15.01549 | -47.565 | 2025-10-11 03:45:00 | NOAA-20 | FORMOSA | GOIÁS | Brasil | 5208004 | 52 | 33 | nan | nan | nan | Cerrado | 1.8 |
| 0e5f471c-3941-36a3-af62-a61eb2117464 | -13.77925 | -45.41687 | 2025-10-11 03:45:00 | NOAA-20 | JABORANDI | BAHIA | Brasil | 2917359 | 29 | 33 | nan | nan | nan | Cerrado | 3.6 |
| 0aa66e0e-d10d-3c0c-882c-8375d99c7255 | -18.45807 | -43.16445 | 2025-10-11 03:45:00 | NOAA-20 | SERRA AZUL DE MINAS | MINAS GERAIS | Brasil | 3166501 | 31 | 33 | nan | nan | nan | Mata Atlântica | 0.8 |
| 06cbf254-5633-34d9-8c54-24c5d099b332 | -16.29702 | -47.17107 | 2025-10-11 03:45:00 | NOAA-20 | UNAÍ | MINAS GERAIS | Brasil | 3170404 | 31 | 33 | nan | nan | nan | Cerrado | 4.2 |
| 1f9ac3c4-f4b6-3d35-b5b1-6aae0b715bbb | -13.25506 | -46.49115 | 2025-10-11 03:45:00 | NOAA-20 | DIVINÓPOLIS DE GOIÁS | GOIÁS | Brasil | 5208301 | 52 | 33 | nan | nan | nan | Cerrado | 1.8 |
| f131403d-ca4d-39cf-9bcd-c7dee66dae54 | -18.13475 | -44.34198 | 2025-10-11 03:45:00 | NOAA-20 | AUGUSTO DE LIMA | MINAS GERAIS | Brasil | 3104809 | 31 | 33 | nan | nan | nan | Cerrado | 1.5 |
| 023f11ce-3700-3de5-9758-8f9711ed4e91 | -15.29055 | -46.30186 | 2025-10-11 03:45:00 | NOAA-20 | FORMOSO | MINAS GERAIS | Brasil | 3126208 | 31 | 33 | nan | nan | nan | Cerrado | 1.8 |
| b6f12355-598f-3d1d-b532-af641fcc6dc5 | -13.24576 | -46.48069 | 2025-10-11 03:45:00 | NOAA-20 | DIVINÓPOLIS DE GOIÁS | GOIÁS | Brasil | 5208301 | 52 | 33 | nan | nan | nan | Cerrado | 1.6 |
| 842be253-91da-3248-88fe-32fcd612360e | -13.78089 | -45.4188 | 2025-10-11 03:45:00 | NOAA-20 | JABORANDI | BAHIA | Brasil | 2917359 | 29 | 33 | nan | nan | nan | Cerrado | 2.4 |
| 4a7d7271-acd3-3b5c-a9d1-a67f41369579 | -13.4889 | -48.10997 | 2025-10-11 03:45:00 | NOAA-20 | CAVALCANTE | GOIÁS | Brasil | 5205307 | 52 | 33 | nan | nan | nan | Cerrado | 3.0 |
| 8255d5d9-7d65-361e-b0c8-56dda1c97481 | -14.01386 | -47.066 | 2025-10-11 03:45:00 | NOAA-20 | NOVA ROMA | GOIÁS | Brasil | 5214903 | 52 | 33 | nan | nan | nan | Cerrado | 1.1 |
| b7a3afd8-8c49-3235-9774-556c6861fa5b | -14.27919 | -45.90204 | 2025-10-11 03:45:00 | NOAA-20 | JABORANDI | BAHIA | Brasil | 2917359 | 29 | 33 | nan | nan | nan | Cerrado | 3.6 |
| 89e48204-3d36-3aad-923e-63a0ef4ba604 | -14.07721 | -47.11459 | 2025-10-11 03:45:00 | NOAA-20 | NOVA ROMA | GOIÁS | Brasil | 5214903 | 52 | 33 | nan | nan | nan | Cerrado | 0.9 |
| 82714cc6-2e94-3be3-9c19-1e4c9ad8a9f0 | -16.36842 | -40.75566 | 2025-10-11 03:45:00 | NOAA-20 | JEQUITINHONHA | MINAS GERAIS | Brasil | 3135803 | 31 | 33 | nan | nan | nan | Mata Atlântica | 0.9 |
| ca0a99a3-c28a-3423-86f1-207da4d48e8f | -13.83065 | -45.78427 | 2025-10-11 03:45:00 | NOAA-20 | JABORANDI | BAHIA | Brasil | 2917359 | 29 | 33 | nan | nan | nan | Cerrado | 1.2 |
| 63a4521a-292e-3e2b-ac66-a34fa698b5a8 | -13.30621 | -47.12457 | 2025-10-11 03:45:00 | NOAA-20 | MONTE ALEGRE DE GOIÁS | GOIÁS | Brasil | 5213509 | 52 | 33 | nan | nan | nan | Cerrado | 2.3 |
| 38be6370-801a-3aa3-a9ab-0bfb5031b2cd | -16.30707 | -47.14977 | 2025-10-11 03:45:00 | NOAA-20 | UNAÍ | MINAS GERAIS | Brasil | 3170404 | 31 | 33 | nan | nan | nan | Cerrado | 2.7 |
| 46fc4438-802d-391c-8f09-13dd0f9b6f1a | -15.6027 | -42.67548 | 2025-10-11 03:45:00 | NOAA-20 | RIO PARDO DE MINAS | MINAS GERAIS | Brasil | 3155603 | 31 | 33 | nan | nan | nan | Mata Atlântica | 3.0 |
| 0fb86f3d-590f-3fbe-9822-6e8ec2ce1c2a | -14.27793 | -45.9084 | 2025-10-11 03:45:00 | NOAA-20 | JABORANDI | BAHIA | Brasil | 2917359 | 29 | 33 | nan | nan | nan | Cerrado | 2.1 |
| 8aea05ce-0b19-38a2-9b65-16a4d83c3f30 | -16.30561 | -47.15683 | 2025-10-11 03:45:00 | NOAA-20 | UNAÍ | MINAS GERAIS | Brasil | 3170404 | 31 | 33 | nan | nan | nan | Cerrado | 2.4 |
| 43c9201d-b6c3-3363-81c9-8a0d3020a2cd | -15.7049 | -46.63897 | 2025-10-11 03:45:00 | NOAA-20 | BURITIS | MINAS GERAIS | Brasil | 3109303 | 31 | 33 | nan | nan | nan | Cerrado | 3.4 |
| e9146ca1-d398-31fa-9af5-22360fef7f15 | -14.92104 | -46.77773 | 2025-10-11 03:45:00 | NOAA-20 | FLORES DE GOIÁS | GOIÁS | Brasil | 5207907 | 52 | 33 | nan | nan | nan | Cerrado | 1.6 |
| 75f0164c-e1d6-3288-91a7-cd578c3f5d86 | -15.70659 | -46.63877 | 2025-10-11 03:45:00 | NOAA-20 | BURITIS | MINAS GERAIS | Brasil | 3109303 | 31 | 33 | nan | nan | nan | Cerrado | 2.6 |
| 1c3d7f87-56db-3009-8265-b046d813a616 | -14.95117 | -45.59279 | 2025-10-11 03:45:00 | NOAA-20 | COCOS | BAHIA | Brasil | 2908101 | 29 | 33 | nan | nan | nan | Cerrado | 0.5 |
| 6b608051-af87-3c4a-b210-e4b974eec08a | -15.57921 | -44.01891 | 2025-10-11 03:45:00 | NOAA-20 | VARZELÂNDIA | MINAS GERAIS | Brasil | 3170909 | 31 | 33 | nan | nan | nan | Cerrado | 1.9 |
| 701a1196-d3ef-3747-9da3-cc19a8a50436 | -15.38625 | -47.29098 | 2025-10-11 03:45:00 | NOAA-20 | FORMOSA | GOIÁS | Brasil | 5208004 | 52 | 33 | nan | nan | nan | Cerrado | 1.3 |
| decb1b9f-66fa-3091-a06d-da170c0b0103 | -17.51399 | -44.28662 | 2025-10-11 03:45:00 | NOAA-20 | FRANCISCO DUMONT | MINAS GERAIS | Brasil | 3126604 | 31 | 33 | nan | nan | nan | Cerrado | 1.5 |
| 730346be-c4f7-392a-9e4c-83e7e3a83af2 | -15.60678 | -42.6764 | 2025-10-11 03:45:00 | NOAA-20 | RIO PARDO DE MINAS | MINAS GERAIS | Brasil | 3155603 | 31 | 33 | nan | nan | nan | Cerrado | 4.0 |
| 51627f41-3e1d-37fe-9147-9d52df986927 | -13.41543 | -47.24207 | 2025-10-11 03:45:00 | NOAA-20 | MONTE ALEGRE DE GOIÁS | GOIÁS | Brasil | 5213509 | 52 | 33 | nan | nan | nan | Cerrado | 1.8 |
| e509247b-8da3-3b62-a596-9c0f4c794daf | -14.01451 | -47.06271 | 2025-10-11 03:45:00 | NOAA-20 | NOVA ROMA | GOIÁS | Brasil | 5214903 | 52 | 33 | nan | nan | nan | Cerrado | 1.1 |
| 257ddbcd-8aa7-34e6-9f6a-dca62d1a4413 | -15.7072 | -46.63575 | 2025-10-11 03:45:00 | NOAA-20 | BURITIS | MINAS GERAIS | Brasil | 3109303 | 31 | 33 | nan | nan | nan | Cerrado | 3.4 |
| 89cbbdda-c80d-39c3-9197-8806305384f4 | -16.7428 | -43.97618 | 2025-10-11 03:45:00 | NOAA-20 | MONTES CLAROS | MINAS GERAIS | Brasil | 3143302 | 31 | 33 | nan | nan | nan | Cerrado | 1.0 |
| 767f4945-2427-3ca9-824b-1eca2385d946 | -16.18818 | -43.6721 | 2025-10-11 03:45:00 | NOAA-20 | CAPITÃO ENÉAS | MINAS GERAIS | Brasil | 3112703 | 31 | 33 | nan | nan | nan | Cerrado | 1.0 |
| ac92a93a-ef16-3a63-8e92-978cde918af6 | -17.26621 | -46.90173 | 2025-10-11 03:45:00 | NOAA-20 | PARACATU | MINAS GERAIS | Brasil | 3147006 | 31 | 33 | nan | nan | nan | Cerrado | 21.0 |
| 2a0fa5c5-9692-3dda-8f9e-3958a0e5c701 | -15.25351 | -44.34451 | 2025-10-11 03:45:00 | NOAA-20 | JANUÁRIA | MINAS GERAIS | Brasil | 3135209 | 31 | 33 | nan | nan | nan | Cerrado | 0.9 |
| a8cec451-cc1c-322e-be76-e4292d477dda | -13.07157 | -46.80552 | 2025-10-11 03:45:00 | NOAA-20 | CAMPOS BELOS | GOIÁS | Brasil | 5204904 | 52 | 33 | nan | nan | nan | Cerrado | 1.4 |
| 590b4d4c-abbc-3747-aef1-694f9f328202 | -16.19192 | -43.67078 | 2025-10-11 03:45:00 | NOAA-20 | CAPITÃO ENÉAS | MINAS GERAIS | Brasil | 3112703 | 31 | 33 | nan | nan | nan | Cerrado | 1.0 |
| 205cb4a1-61c2-36e1-8d1a-05181a8eed50 | -18.22109 | -42.37926 | 2025-10-11 03:45:00 | NOAA-20 | SANTA MARIA DO SUAÇUÍ | MINAS GERAIS | Brasil | 3158201 | 31 | 33 | nan | nan | nan | Mata Atlântica | 1.5 |
| 6edee8e1-2287-382f-bfe7-74c0a05c4609 | -15.58556 | -44.50727 | 2025-10-11 03:45:00 | NOAA-20 | JANUÁRIA | MINAS GERAIS | Brasil | 3135209 | 31 | 33 | nan | nan | nan | Cerrado | 1.7 |
| b7cc342d-b101-3562-99d5-fb49eda0234a | -14.99132 | -45.56887 | 2025-10-11 03:45:00 | NOAA-20 | JANUÁRIA | MINAS GERAIS | Brasil | 3135209 | 31 | 33 | nan | nan | nan | Cerrado | 0.8 |
| 568ca557-64e1-36ed-bd35-d3ef40d83f13 | -14.01828 | -47.05892 | 2025-10-11 03:45:00 | NOAA-20 | NOVA ROMA | GOIÁS | Brasil | 5214903 | 52 | 33 | nan | nan | nan | Cerrado | 1.4 |
| e940f49f-153f-3b4d-89e4-4ad7406cc49f | -14.07643 | -47.11847 | 2025-10-11 03:45:00 | NOAA-20 | NOVA ROMA | GOIÁS | Brasil | 5214903 | 52 | 33 | nan | nan | nan | Cerrado | 2.6 |
| c5894ff1-3295-3e68-9365-e6c0442ec47e | -20.46372 | -42.44945 | 2025-10-11 03:45:00 | NOAA-20 | SERICITA | MINAS GERAIS | Brasil | 3166303 | 31 | 33 | nan | nan | nan | Mata Atlântica | 0.5 |
| 836f2f35-29f7-389f-805d-0512bc2c7881 | -15.29111 | -46.2991 | 2025-10-11 03:45:00 | NOAA-20 | FORMOSO | MINAS GERAIS | Brasil | 3126208 | 31 | 33 | nan | nan | nan | Cerrado | 1.3 |
| 35a0ba62-c458-3b00-88f1-694aa6e6dd1b | -15.38696 | -47.28755 | 2025-10-11 03:45:00 | NOAA-20 | FORMOSA | GOIÁS | Brasil | 5208004 | 52 | 33 | nan | nan | nan | Cerrado | 1.3 |
| 9b23969e-d252-3698-9ea1-8c9d7aa7e4de | -12.74159 | -48.65099 | 2025-10-11 03:45:00 | NOAA-20 | JAÚ DO TOCANTINS | TOCANTINS | Brasil | 1711506 | 17 | 33 | nan | nan | nan | Cerrado | 6.1 |
| 5760ed76-f698-3b7a-873e-d08125e6d201 | -14.6982 | -47.44176 | 2025-10-11 03:45:00 | NOAA-20 | SÃO JOÃO D'ALIANÇA | GOIÁS | Brasil | 5220009 | 52 | 33 | nan | nan | nan | Cerrado | 1.0 |
| d3ae11a2-792e-3043-8c7c-64ef8eadc72e | -14.94221 | -46.75718 | 2025-10-11 03:45:00 | NOAA-20 | FLORES DE GOIÁS | GOIÁS | Brasil | 5207907 | 52 | 33 | nan | nan | nan | Cerrado | 3.2 |
| 59acd2ef-466d-31ac-809e-ce08555f650d | -14.01762 | -47.06215 | 2025-10-11 03:45:00 | NOAA-20 | NOVA ROMA | GOIÁS | Brasil | 5214903 | 52 | 33 | nan | nan | nan | Cerrado | 0.9 |
| f0fd8a02-bc43-3545-bc75-347d1c683308 | -14.9203 | -46.78133 | 2025-10-11 03:45:00 | NOAA-20 | FLORES DE GOIÁS | GOIÁS | Brasil | 5207907 | 52 | 33 | nan | nan | nan | Cerrado | 1.6 |
| cbcb5bb8-b897-36aa-a9da-0f75b51593cd | -14.93794 | -46.75049 | 2025-10-11 03:45:00 | NOAA-20 | FLORES DE GOIÁS | GOIÁS | Brasil | 5207907 | 52 | 33 | nan | nan | nan | Cerrado | 2.7 |
| 2fede13d-6ff3-3f23-8e31-1c9788165f77 | -14.27982 | -45.89885 | 2025-10-11 03:45:00 | NOAA-20 | JABORANDI | BAHIA | Brasil | 2917359 | 29 | 33 | nan | nan | nan | Cerrado | 3.4 |
| 4c1b50ca-bf77-3e7b-bc21-07ac29cbef53 | -12.74776 | -48.65305 | 2025-10-11 03:45:00 | NOAA-20 | JAÚ DO TOCANTINS | TOCANTINS | Brasil | 1711506 | 17 | 33 | nan | nan | nan | Cerrado | 5.1 |
| 42a452d0-a12f-318e-86ec-28d665ac90ec | -16.73845 | -43.97522 | 2025-10-11 03:45:00 | NOAA-20 | MONTES CLAROS | MINAS GERAIS | Brasil | 3143302 | 31 | 33 | nan | nan | nan | Cerrado | 1.0 |
| 81d2ade5-6b19-36ae-a445-0b3178171279 | -14.28492 | -45.90034 | 2025-10-11 03:45:00 | NOAA-20 | JABORANDI | BAHIA | Brasil | 2917359 | 29 | 33 | nan | nan | nan | Cerrado | 3.4 |
| 0b46e36c-f88d-3ddb-92de-7f65a459fa3f | -15.2203 | -47.91066 | 2025-10-11 03:45:00 | NOAA-20 | PLANALTINA | GOIÁS | Brasil | 5217609 | 52 | 33 | nan | nan | nan | Cerrado | 5.2 |
| 4bd4c7c2-b912-332f-be78-d9b3c6a20e48 | -15.00944 | -41.8162 | 2025-10-11 03:45:00 | NOAA-20 | PIRIPÁ | BAHIA | Brasil | 2924702 | 29 | 33 | nan | nan | nan | Caatinga | 3.3 |
| fc8110f2-a65b-3371-97fa-1d7fe3dd1392 | -13.32428 | -47.12333 | 2025-10-11 03:45:00 | NOAA-20 | MONTE ALEGRE DE GOIÁS | GOIÁS | Brasil | 5213509 | 52 | 33 | nan | nan | nan | Cerrado | 3.4 |
| 11ee6ceb-562a-39e3-86d4-f4d05ef7f084 | -14.28044 | -45.89572 | 2025-10-11 03:45:00 | NOAA-20 | JABORANDI | BAHIA | Brasil | 2917359 | 29 | 33 | nan | nan | nan | Cerrado | 3.4 |
| 18ea2cf8-e3ba-32ca-af39-606ce37ba443 | -13.83975 | -45.79278 | 2025-10-11 03:45:00 | NOAA-20 | JABORANDI | BAHIA | Brasil | 2917359 | 29 | 33 | nan | nan | nan | Cerrado | 0.8 |
| d6f0c2b8-11ad-3d85-902b-3900109ca4f9 | -14.53318 | -44.00396 | 2025-10-11 03:45:00 | NOAA-20 | JUVENÍLIA | MINAS GERAIS | Brasil | 3136959 | 31 | 33 | nan | nan | nan | Caatinga | 1.2 |


[Clique aqui para ver as próximas entradas](README15.md)
