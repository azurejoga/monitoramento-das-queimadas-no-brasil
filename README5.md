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
| e0be789d-fe50-3e84-a434-71d4d52ec5ab | -1.9112 | -46.57869 | 2025-09-17 00:13:00 | TERRA_M-M | CACHOEIRA DO PIRIÁ | PARÁ | Brasil | 1501956 | 15 | 33 | nan | nan | nan | Amazônia | 4.6 |
| 701f197e-9e43-3028-bca2-e979c273c751 | -4.76884 | -50.7008 | 2025-09-17 00:13:00 | TERRA_M-M | NOVO REPARTIMENTO | PARÁ | Brasil | 1505064 | 15 | 33 | nan | nan | nan | Amazônia | 20.1 |
| aa6d078b-bc3c-3c49-8156-710e1475e377 | -5.82107 | -46.35698 | 2025-09-17 00:13:00 | TERRA_M-M | GRAJAÚ | MARANHÃO | Brasil | 2104800 | 21 | 33 | nan | nan | nan | Cerrado | 17.8 |
| ceecc121-f793-3313-a47a-9dd3a3919a87 | -5.04821 | -46.01036 | 2025-09-17 00:13:00 | TERRA_M-M | ARAME | MARANHÃO | Brasil | 2100956 | 21 | 33 | nan | nan | nan | Amazônia | 5.8 |
| 54364f6e-f390-3440-aa36-2e51112f70f4 | -3.68809 | -49.01347 | 2025-09-17 00:13:00 | TERRA_M-M | GOIANÉSIA DO PARÁ | PARÁ | Brasil | 1503093 | 15 | 33 | nan | nan | nan | Amazônia | 39.8 |
| 5f41af81-7918-3a1c-b738-a8c5e864c61a | -3.39242 | -50.26512 | 2025-09-17 00:13:00 | TERRA_M-M | PACAJÁ | PARÁ | Brasil | 1505486 | 15 | 33 | nan | nan | nan | Amazônia | 15.0 |
| 69d03a04-c301-3686-a539-581150bfa8f2 | -4.66686 | -46.31439 | 2025-09-17 00:13:00 | TERRA_M-M | BURITICUPU | MARANHÃO | Brasil | 2102325 | 21 | 33 | nan | nan | nan | Amazônia | 10.3 |
| 25e9addd-b899-301c-8b6c-d82ee393ebed | -4.23225 | -43.69533 | 2025-09-17 00:13:00 | TERRA_M-M | TIMBIRAS | MARANHÃO | Brasil | 2112100 | 21 | 33 | nan | nan | nan | Cerrado | 11.6 |
| e2012c48-3cc7-3c4d-8445-db096a277cb0 | -5.81709 | -46.36335 | 2025-09-17 00:13:00 | TERRA_M-M | GRAJAÚ | MARANHÃO | Brasil | 2104800 | 21 | 33 | nan | nan | nan | Cerrado | 49.7 |
| 54be0f66-2896-37f3-8944-5144184041db | -2.9252 | -48.31518 | 2025-09-17 00:13:00 | TERRA_M-M | TOMÉ-AÇU | PARÁ | Brasil | 1508001 | 15 | 33 | nan | nan | nan | Amazônia | 13.5 |
| 83348b3a-374f-35dc-9a16-10a2bf482030 | -4.22465 | -43.70541 | 2025-09-17 00:13:00 | TERRA_M-M | TIMBIRAS | MARANHÃO | Brasil | 2112100 | 21 | 33 | nan | nan | nan | Cerrado | 10.2 |
| 54298f2e-d59e-3ea2-8642-beb6fb96c9e2 | -3.68788 | -49.01979 | 2025-09-17 00:13:00 | TERRA_M-M | GOIANÉSIA DO PARÁ | PARÁ | Brasil | 1503093 | 15 | 33 | nan | nan | nan | Amazônia | 46.3 |
| 4da8074c-32fb-3ba1-9a83-c7475271def5 | -4.05108 | -47.50196 | 2025-09-17 00:13:00 | TERRA_M-M | ULIANÓPOLIS | PARÁ | Brasil | 1508126 | 15 | 33 | nan | nan | nan | Amazônia | 54.6 |
| f935affe-8444-342e-8a9c-421cc69c7c60 | -2.3819 | -47.64003 | 2025-09-17 00:13:00 | TERRA_M-M | IPIXUNA DO PARÁ | PARÁ | Brasil | 1503457 | 15 | 33 | nan | nan | nan | Amazônia | 39.5 |
| 644ef39b-cfa8-332e-ad8b-5cfed84bff33 | -5.79928 | -45.70028 | 2025-09-17 00:13:00 | TERRA_M-M | GRAJAÚ | MARANHÃO | Brasil | 2104800 | 21 | 33 | nan | nan | nan | Cerrado | 5.9 |
| 485062aa-5f86-3464-a6ba-e5ba0c38737f | -3.80062 | -44.10078 | 2025-09-17 00:13:00 | TERRA_M-M | PIRAPEMAS | MARANHÃO | Brasil | 2108801 | 21 | 33 | nan | nan | nan | Cerrado | 8.8 |
| cf6efe01-fa91-3003-906a-0f20756bea13 | -2.96221 | -48.58452 | 2025-09-17 00:13:00 | TERRA_M-M | TAILÂNDIA | PARÁ | Brasil | 1507953 | 15 | 33 | nan | nan | nan | Amazônia | 10.7 |
| 2d5ebd4e-956a-3b17-b3c3-27ca94349697 | -4.09158 | -44.13997 | 2025-09-17 00:13:00 | TERRA_M-M | COROATÁ | MARANHÃO | Brasil | 2103604 | 21 | 33 | nan | nan | nan | Cerrado | 7.3 |
| 99e45125-9a47-317f-8bd8-d6db3d1ed767 | -4.9801 | -43.1708 | 2025-09-17 00:13:00 | TERRA_M-M | CAXIAS | MARANHÃO | Brasil | 2103000 | 21 | 33 | nan | nan | nan | Cerrado | 4.7 |
| 76f027cf-4dd7-3eb7-a0fe-02d8f6ff74c7 | -5.48905 | -43.98521 | 2025-09-17 00:13:00 | TERRA_M-M | GOVERNADOR LUIZ ROCHA | MARANHÃO | Brasil | 2104628 | 21 | 33 | nan | nan | nan | Cerrado | 46.1 |
| af47d7ff-1425-34fd-a79e-ef87933e7101 | -4.01198 | -43.23197 | 2025-09-17 00:13:00 | TERRA_M-M | CHAPADINHA | MARANHÃO | Brasil | 2103208 | 21 | 33 | nan | nan | nan | Cerrado | 12.8 |
| 90cdca2d-bf8f-348e-abc0-290061cf5569 | -4.03908 | -49.06743 | 2025-09-17 00:13:00 | TERRA_M-M | GOIANÉSIA DO PARÁ | PARÁ | Brasil | 1503093 | 15 | 33 | nan | nan | nan | Amazônia | 10.7 |
| 4b5176ac-1c06-33a6-9a47-67794933589d | -3.23816 | -46.78387 | 2025-09-17 00:13:00 | TERRA_M-M | PARAGOMINAS | PARÁ | Brasil | 1505502 | 15 | 33 | nan | nan | nan | Amazônia | 22.1 |
| 5c0eec95-7d06-3993-9107-fcd38acc444c | -6.16475 | -44.53201 | 2025-09-17 00:13:00 | TERRA_M-M | MIRADOR | MARANHÃO | Brasil | 2106706 | 21 | 33 | nan | nan | nan | Cerrado | 6.0 |
| 92cb84af-1132-3d52-91c0-2b673ef7a612 | -5.67276 | -43.51026 | 2025-09-17 00:13:00 | TERRA_M-M | PARNARAMA | MARANHÃO | Brasil | 2107803 | 21 | 33 | nan | nan | nan | Cerrado | 6.9 |
| 6e2a0998-788d-3a42-bd26-a621147845c1 | -1.69229 | -47.07023 | 2025-09-17 00:13:00 | TERRA_M-M | CAPITÃO POÇO | PARÁ | Brasil | 1502301 | 15 | 33 | nan | nan | nan | Amazônia | 5.9 |
| b7441ed3-f272-339e-a547-f1488bfb3dec | -3.80562 | -47.57761 | 2025-09-17 00:13:00 | TERRA_M-M | ULIANÓPOLIS | PARÁ | Brasil | 1508126 | 15 | 33 | nan | nan | nan | Amazônia | 7.1 |
| f5da537c-6bdf-3baf-9d92-c3545f322725 | -4.23347 | -43.70415 | 2025-09-17 00:13:00 | TERRA_M-M | TIMBIRAS | MARANHÃO | Brasil | 2112100 | 21 | 33 | nan | nan | nan | Cerrado | 27.2 |
| fe567967-58c0-363f-b362-66d60bf56b48 | -5.76413 | -43.69772 | 2025-09-17 00:13:00 | TERRA_M-M | BURITI BRAVO | MARANHÃO | Brasil | 2102309 | 21 | 33 | nan | nan | nan | Cerrado | 5.9 |
| 2540b564-ff59-3dd9-9042-0be496580614 | -5.59587 | -45.35847 | 2025-09-17 00:13:00 | TERRA_M-M | BARRA DO CORDA | MARANHÃO | Brasil | 2101608 | 21 | 33 | nan | nan | nan | Cerrado | 35.9 |
| c859593d-fe54-322a-815e-7772233023e7 | -3.42854 | -43.15408 | 2025-09-17 00:13:00 | TERRA_M-M | SANTA QUITÉRIA DO MARANHÃO | MARANHÃO | Brasil | 2110104 | 21 | 33 | nan | nan | nan | Cerrado | 4.3 |
| 4c14114a-da49-3083-aaed-825cdfe561f4 | -4.92798 | -45.59504 | 2025-09-17 00:13:00 | TERRA_M-M | ARAME | MARANHÃO | Brasil | 2100956 | 21 | 33 | nan | nan | nan | Amazônia | 7.7 |
| 4b86bfd6-78f2-3c0a-8b90-a5497c91ccbe | -5.32599 | -45.00343 | 2025-09-17 00:13:00 | TERRA_M-M | BARRA DO CORDA | MARANHÃO | Brasil | 2101608 | 21 | 33 | nan | nan | nan | Cerrado | 10.7 |
| 1ba37458-fc58-367c-a690-01df8b26b849 | -4.9957 | -44.87518 | 2025-09-17 00:13:00 | TERRA_M-M | JOSELÂNDIA | MARANHÃO | Brasil | 2105609 | 21 | 33 | nan | nan | nan | Cerrado | 9.8 |
| e226c474-751c-3375-9bc9-8baa6355b839 | -4.04111 | -49.08234 | 2025-09-17 00:13:00 | TERRA_M-M | BREU BRANCO | PARÁ | Brasil | 1501782 | 15 | 33 | nan | nan | nan | Amazônia | 11.2 |
| c99b676b-2ea9-3dc4-8e3b-a6c09fc799fb | -5.98506 | -45.85017 | 2025-09-17 00:13:00 | TERRA_M-M | GRAJAÚ | MARANHÃO | Brasil | 2104800 | 21 | 33 | nan | nan | nan | Cerrado | 5.3 |
| a71b4406-510e-394c-8bc3-5429702bbc09 | -5.21279 | -45.18248 | 2025-09-17 00:13:00 | TERRA_M-M | BARRA DO CORDA | MARANHÃO | Brasil | 2101608 | 21 | 33 | nan | nan | nan | Cerrado | 6.5 |
| 2ff69099-f6ae-3ab0-ab27-6efc5e0a9957 | -4.5548 | -44.02604 | 2025-09-17 00:13:00 | TERRA_M-M | CODÓ | MARANHÃO | Brasil | 2103307 | 21 | 33 | nan | nan | nan | Cerrado | 6.3 |
| c8bb322a-27ab-39a9-9de9-8dbb7bd7266a | -4.51694 | -38.55364 | 2025-09-17 00:13:00 | TERRA_M-M | OCARA | CEARÁ | Brasil | 2309458 | 23 | 33 | nan | nan | nan | Caatinga | 33.5 |
| 635501fd-0831-31f8-9dc5-0f84c164a56d | -3.17613 | -48.80317 | 2025-09-17 00:13:00 | TERRA_M-M | TAILÂNDIA | PARÁ | Brasil | 1507953 | 15 | 33 | nan | nan | nan | Amazônia | 16.8 |
| 212420ec-b395-38db-bf8e-3a111154de87 | -5.12991 | -45.11683 | 2025-09-17 00:13:00 | TERRA_M-M | BARRA DO CORDA | MARANHÃO | Brasil | 2101608 | 21 | 33 | nan | nan | nan | Cerrado | 3.7 |
| fe23fdbe-cf5b-3dc3-b603-b973f1e81898 | -5.47487 | -45.34959 | 2025-09-17 00:13:00 | TERRA_M-M | BARRA DO CORDA | MARANHÃO | Brasil | 2101608 | 21 | 33 | nan | nan | nan | Cerrado | 8.2 |
| 678a44f7-8b8e-353d-b288-2ecbbfdadbad | -5.57025 | -45.03405 | 2025-09-17 00:13:00 | TERRA_M-M | BARRA DO CORDA | MARANHÃO | Brasil | 2101608 | 21 | 33 | nan | nan | nan | Cerrado | 8.3 |
| 425c956b-1cae-310f-abb3-a3af48bef463 | -3.877 | -50.77608 | 2025-09-17 00:13:00 | TERRA_M-M | PACAJÁ | PARÁ | Brasil | 1505486 | 15 | 33 | nan | nan | nan | Amazônia | 16.4 |
| 8877f8d8-d682-3666-88c3-add991e300dd | -5.31983 | -48.68573 | 2025-09-17 00:13:00 | TERRA_M-M | ESPERANTINA | TOCANTINS | Brasil | 1707405 | 17 | 33 | nan | nan | nan | Amazônia | 13.5 |
| 357da554-bb0d-30d3-aa04-42b8cce1571f | -5.24658 | -49.86108 | 2025-09-17 00:13:00 | TERRA_M-M | ITUPIRANGA | PARÁ | Brasil | 1503705 | 15 | 33 | nan | nan | nan | Amazônia | 15.6 |
| b461bc2d-3f7b-36ec-9853-dc283ba1c4a0 | -5.6049 | -45.35716 | 2025-09-17 00:13:00 | TERRA_M-M | BARRA DO CORDA | MARANHÃO | Brasil | 2101608 | 21 | 33 | nan | nan | nan | Cerrado | 7.5 |
| dd90a682-b094-314f-b938-e5ee708e9142 | -3.17801 | -48.81686 | 2025-09-17 00:13:00 | TERRA_M-M | TAILÂNDIA | PARÁ | Brasil | 1507953 | 15 | 33 | nan | nan | nan | Amazônia | 40.9 |
| 5f73216f-ce60-373a-82fa-0f3071a09322 | -6.09871 | -45.93874 | 2025-09-17 00:13:00 | TERRA_M-M | GRAJAÚ | MARANHÃO | Brasil | 2104800 | 21 | 33 | nan | nan | nan | Cerrado | 8.3 |
| e83add5e-1bfe-3a89-a13e-bab90ada7c99 | -5.30537 | -43.05404 | 2025-09-17 00:13:00 | TERRA_M-M | TIMON | MARANHÃO | Brasil | 2112209 | 21 | 33 | nan | nan | nan | Cerrado | 5.3 |
| 193e558a-13c1-3d6e-b321-9c6634577e0f | -5.80023 | -43.48896 | 2025-09-17 00:13:00 | TERRA_M-M | PARNARAMA | MARANHÃO | Brasil | 2107803 | 21 | 33 | nan | nan | nan | Cerrado | 18.2 |
| a2f3caff-ff5a-302d-977b-c842b27bf192 | -6.10006 | -45.94868 | 2025-09-17 00:13:00 | TERRA_M-M | GRAJAÚ | MARANHÃO | Brasil | 2104800 | 21 | 33 | nan | nan | nan | Cerrado | 9.5 |
| 3ecb1488-f9d6-3ee2-821e-cb3855df4a0d | -4.06105 | -47.5004 | 2025-09-17 00:13:00 | TERRA_M-M | ULIANÓPOLIS | PARÁ | Brasil | 1508126 | 15 | 33 | nan | nan | nan | Amazônia | 166.0 |
| a2ca24ce-06f4-3119-b987-bfdc56af745a | -2.83907 | -48.83974 | 2025-09-17 00:13:00 | TERRA_M-M | TAILÂNDIA | PARÁ | Brasil | 1507953 | 15 | 33 | nan | nan | nan | Amazônia | 8.9 |
| ec5935da-04db-37f3-8b78-5096e5eb34a6 | -0.75911 | -47.7515 | 2025-09-17 00:13:00 | TERRA_M-M | MARAPANIM | PARÁ | Brasil | 1504406 | 15 | 33 | nan | nan | nan | Amazônia | 6.7 |
| fe1a3514-5c49-3a15-8684-63feb073883e | -4.52206 | -38.54705 | 2025-09-17 00:13:00 | TERRA_M-M | OCARA | CEARÁ | Brasil | 2309458 | 23 | 33 | nan | nan | nan | Caatinga | 23.1 |
| 9eb6d6ed-813f-3a9e-813a-964b4f588c4a | -11.0201 | -45.059 | 2025-09-17 00:20:00 | GOES-19 | FORMOSA DO RIO PRETO | BAHIA | Brasil | 2911105 | 29 | 33 | nan | nan | nan | Cerrado | 63.5 |
| 65a2cd6f-0756-3af1-89d1-8555c85fce38 | -11.0167 | -48.9079 | 2025-09-17 00:20:00 | GOES-19 | SANTA RITA DO TOCANTINS | TOCANTINS | Brasil | 1718899 | 17 | 33 | nan | nan | nan | Cerrado | 78.7 |
| 5287fbe1-19ac-3edf-90cc-5e030b6ad0f6 | -7.5807 | -44.589 | 2025-09-17 00:20:00 | GOES-19 | URUÇUÍ | PIAUÍ | Brasil | 2211209 | 22 | 33 | nan | nan | nan | Cerrado | 160.9 |
| 711464b3-582f-3459-ad2e-770738b0c338 | -8.6693 | -46.4067 | 2025-09-17 00:20:00 | GOES-19 | BALSAS | MARANHÃO | Brasil | 2101400 | 21 | 33 | nan | nan | nan | Cerrado | 81.0 |
| 8e0950ba-3ba3-3460-b36e-6d7106399669 | -2.3763 | -47.6419 | 2025-09-17 00:20:00 | GOES-19 | IPIXUNA DO PARÁ | PARÁ | Brasil | 1503457 | 15 | 33 | nan | nan | nan | Amazônia | 48.8 |
| cf6a045c-0342-3809-80bc-ff33094a2a75 | -7.581 | -44.566 | 2025-09-17 00:20:00 | GOES-19 | URUÇUÍ | PIAUÍ | Brasil | 2211209 | 22 | 33 | nan | nan | nan | Cerrado | 164.9 |
| 6ef8294d-0056-3853-8d30-2f75114438d0 | -6.6316 | -45.5825 | 2025-09-17 00:20:00 | GOES-19 | MIRADOR | MARANHÃO | Brasil | 2106706 | 21 | 33 | nan | nan | nan | Cerrado | 118.5 |
| 21e5492f-cd8e-3071-97b2-18db08f2ae11 | -6.8922 | -43.9619 | 2025-09-17 00:20:00 | GOES-19 | PORTO ALEGRE DO PIAUÍ | PIAUÍ | Brasil | 2208551 | 22 | 33 | nan | nan | nan | Cerrado | 85.9 |
| 153923c5-1e69-3e24-b771-a2f061838cd1 | -4.0634 | -47.4943 | 2025-09-17 00:20:00 | GOES-19 | ULIANÓPOLIS | PARÁ | Brasil | 1508126 | 15 | 33 | nan | nan | nan | Amazônia | 111.9 |
| 9126f425-6e41-33da-9923-521fef6225a6 | -15.4192 | -46.144 | 2025-09-17 00:20:00 | GOES-19 | ARINOS | MINAS GERAIS | Brasil | 3104502 | 31 | 33 | nan | nan | nan | Cerrado | 233.5 |
| 8ae8fd46-f376-3eb9-95f8-471488c9e07f | -4.0633 | -47.5161 | 2025-09-17 00:20:00 | GOES-19 | ULIANÓPOLIS | PARÁ | Brasil | 1508126 | 15 | 33 | nan | nan | nan | Amazônia | 64.9 |
| b3ff4750-96f9-3d9d-b19d-0468d70ada7d | -18.3462 | -43.2967 | 2025-09-17 00:20:00 | GOES-19 | SERRA AZUL DE MINAS | MINAS GERAIS | Brasil | 3166501 | 31 | 33 | nan | nan | nan | Mata Atlântica | 78.0 |
| 2bda0ca6-3d1c-3b81-b588-eb0d3231f8bb | -15.3996 | -46.1477 | 2025-09-17 00:20:00 | GOES-19 | FORMOSO | MINAS GERAIS | Brasil | 3126208 | 31 | 33 | nan | nan | nan | Cerrado | 142.3 |
| 6feaf24d-bb6a-374e-9dba-23bdef28208d | -17.0593 | -45.891 | 2025-09-17 00:20:00 | GOES-19 | BRASILÂNDIA DE MINAS | MINAS GERAIS | Brasil | 3108552 | 31 | 33 | nan | nan | nan | Cerrado | 100.8 |
| 5146a119-7109-3e8b-8e2a-3c61741cce37 | -8.1572 | -46.747 | 2025-09-17 00:20:00 | GOES-19 | CAMPOS LINDOS | TOCANTINS | Brasil | 1703842 | 17 | 33 | nan | nan | nan | Cerrado | 87.6 |
| d5b347ee-1891-395b-ad22-2a768a4213b2 | -6.6808 | -46.2961 | 2025-09-17 00:20:00 | GOES-19 | FORMOSA DA SERRA NEGRA | MARANHÃO | Brasil | 2104099 | 21 | 33 | nan | nan | nan | Cerrado | 172.6 |
| 629f49b5-088f-3dae-b5cc-81ef1007cff1 | -6.6806 | -46.3184 | 2025-09-17 00:20:00 | GOES-19 | FORMOSA DA SERRA NEGRA | MARANHÃO | Brasil | 2104099 | 21 | 33 | nan | nan | nan | Cerrado | 144.0 |
| a5c3ad4d-6f8e-3a55-9080-f1940ba7d467 | -18.326 | -43.3018 | 2025-09-17 00:20:00 | GOES-19 | SERRO | MINAS GERAIS | Brasil | 3167103 | 31 | 33 | nan | nan | nan | Mata Atlântica | 84.1 |
| f1a34a20-bbab-3a67-9915-6177421dc917 | -7.5998 | -44.5642 | 2025-09-17 00:20:00 | GOES-19 | URUÇUÍ | PIAUÍ | Brasil | 2211209 | 22 | 33 | nan | nan | nan | Cerrado | 77.4 |
| 646f49f6-b942-31e2-8264-a69c0fb7cfc8 | -6.8734 | -43.9636 | 2025-09-17 00:20:00 | GOES-19 | PORTO ALEGRE DO PIAUÍ | PIAUÍ | Brasil | 2208551 | 22 | 33 | nan | nan | nan | Cerrado | 102.8 |
| 84222f9d-cf7c-3a36-8bfd-1dbdc46db3ce | -7.5996 | -44.5872 | 2025-09-17 00:20:00 | GOES-19 | URUÇUÍ | PIAUÍ | Brasil | 2211209 | 22 | 33 | nan | nan | nan | Cerrado | 132.6 |
| 2de8ec1c-f6f5-3ffe-88e8-0bd42c4ee768 | -6.6314 | -45.6051 | 2025-09-17 00:20:00 | GOES-19 | MIRADOR | MARANHÃO | Brasil | 2106706 | 21 | 33 | nan | nan | nan | Cerrado | 71.0 |
| 1355a931-8d4f-34ca-bc82-3bf6bf7c9ba4 | -6.6129 | -45.584 | 2025-09-17 00:20:00 | GOES-19 | MIRADOR | MARANHÃO | Brasil | 2106706 | 21 | 33 | nan | nan | nan | Cerrado | 68.0 |
| 473db425-c97e-31fd-ac4b-e42c381fd25e | -11.0164 | -48.9297 | 2025-09-17 00:20:00 | GOES-19 | SANTA RITA DO TOCANTINS | TOCANTINS | Brasil | 1718899 | 17 | 33 | nan | nan | nan | Cerrado | 112.1 |
| 30dd689b-f056-3eee-93c8-fa4d400157f2 | -6.6806 | -46.3184 | 2025-09-17 00:30:00 | GOES-19 | FORMOSA DA SERRA NEGRA | MARANHÃO | Brasil | 2104099 | 21 | 33 | nan | nan | nan | Cerrado | 128.8 |
| 026b6ee4-f092-3b1c-a140-74aa52a41709 | -2.3763 | -47.6419 | 2025-09-17 00:30:00 | GOES-19 | IPIXUNA DO PARÁ | PARÁ | Brasil | 1503457 | 15 | 33 | nan | nan | nan | Amazônia | 46.9 |
| d032160d-f4d0-3410-92a8-3999ae47c953 | -6.6316 | -45.5825 | 2025-09-17 00:30:00 | GOES-19 | MIRADOR | MARANHÃO | Brasil | 2106706 | 21 | 33 | nan | nan | nan | Cerrado | 115.7 |
| 118090b3-884c-30d6-b52f-41bffdb600bf | -9.1715 | -46.9346 | 2025-09-17 00:30:00 | GOES-19 | LIZARDA | TOCANTINS | Brasil | 1712405 | 17 | 33 | nan | nan | nan | Cerrado | 71.3 |
| e279a9ab-f510-3c51-a0ff-fba81deeeb7c | -10.6537 | -46.5403 | 2025-09-17 00:30:00 | GOES-19 | MATEIROS | TOCANTINS | Brasil | 1712702 | 17 | 33 | nan | nan | nan | Cerrado | 38.7 |
| 78bcf299-5f65-3be4-8376-0a9644536203 | -15.4187 | -46.1672 | 2025-09-17 00:30:00 | GOES-19 | ARINOS | MINAS GERAIS | Brasil | 3104502 | 31 | 33 | nan | nan | nan | Cerrado | 91.7 |
| 7449a5d3-6780-30f6-bc65-63b6ac50af44 | -7.5998 | -44.5642 | 2025-09-17 00:30:00 | GOES-19 | URUÇUÍ | PIAUÍ | Brasil | 2211209 | 22 | 33 | nan | nan | nan | Cerrado | 69.1 |
| 5e500bf1-e472-3050-b316-0d302c1b51a8 | -4.0633 | -47.5161 | 2025-09-17 00:30:00 | GOES-19 | ULIANÓPOLIS | PARÁ | Brasil | 1508126 | 15 | 33 | nan | nan | nan | Amazônia | 59.9 |
| 83c4110f-cf0a-3ef7-9d13-138f0e1e2e03 | -8.6693 | -46.4067 | 2025-09-17 00:30:00 | GOES-19 | BALSAS | MARANHÃO | Brasil | 2101400 | 21 | 33 | nan | nan | nan | Cerrado | 77.4 |
| 21ad0ee5-0983-34bb-b0be-94cfd0b357b3 | -15.4192 | -46.144 | 2025-09-17 00:30:00 | GOES-19 | ARINOS | MINAS GERAIS | Brasil | 3104502 | 31 | 33 | nan | nan | nan | Cerrado | 272.8 |
| 8b2edb8e-fe68-39f0-a968-a786cb790299 | -7.5996 | -44.5872 | 2025-09-17 00:30:00 | GOES-19 | URUÇUÍ | PIAUÍ | Brasil | 2211209 | 22 | 33 | nan | nan | nan | Cerrado | 101.4 |
| 1c541c16-1262-305d-969e-95e67abe58fb | -6.8734 | -43.9636 | 2025-09-17 00:30:00 | GOES-19 | PORTO ALEGRE DO PIAUÍ | PIAUÍ | Brasil | 2208551 | 22 | 33 | nan | nan | nan | Cerrado | 98.2 |
| b14f65e7-039f-3767-bbc1-c3e75a33aa6c | -7.5622 | -44.5678 | 2025-09-17 00:30:00 | GOES-19 | URUÇUÍ | PIAUÍ | Brasil | 2211209 | 22 | 33 | nan | nan | nan | Cerrado | 62.3 |
| e903a05d-4753-32bc-a8e9-6e9ec63af95f | -8.1572 | -46.747 | 2025-09-17 00:30:00 | GOES-19 | CAMPOS LINDOS | TOCANTINS | Brasil | 1703842 | 17 | 33 | nan | nan | nan | Cerrado | 83.3 |
| e1cfaa1f-60e2-3c21-a647-c9a44f507da9 | -15.4389 | -46.1404 | 2025-09-17 00:30:00 | GOES-19 | ARINOS | MINAS GERAIS | Brasil | 3104502 | 31 | 33 | nan | nan | nan | Cerrado | 77.9 |
| 7d433aab-9f1d-3980-99e6-59020973a898 | -6.6129 | -45.584 | 2025-09-17 00:30:00 | GOES-19 | MIRADOR | MARANHÃO | Brasil | 2106706 | 21 | 33 | nan | nan | nan | Cerrado | 90.0 |
| 1884335a-df21-3ac2-b860-1a85f60a4d37 | -11.0164 | -48.9297 | 2025-09-17 00:30:00 | GOES-19 | SANTA RITA DO TOCANTINS | TOCANTINS | Brasil | 1718899 | 17 | 33 | nan | nan | nan | Cerrado | 108.3 |
| 18756377-e97b-3517-b268-fa4b54116fa0 | -4.0449 | -47.4951 | 2025-09-17 00:30:00 | GOES-19 | ULIANÓPOLIS | PARÁ | Brasil | 1508126 | 15 | 33 | nan | nan | nan | Amazônia | 53.7 |
| 8e139222-5aa9-3066-bf01-ddf4fe3b5edf | -7.5361 | -63.6123 | 2025-09-17 00:30:00 | GOES-19 | CANUTAMA | AMAZONAS | Brasil | 1300904 | 13 | 33 | nan | nan | nan | Amazônia | 51.5 |
| 7baf3a25-1124-35eb-b770-2c6936224f0d | -10.7115 | -46.488 | 2025-09-17 00:30:00 | GOES-19 | MATEIROS | TOCANTINS | Brasil | 1712702 | 17 | 33 | nan | nan | nan | Cerrado | 48.3 |


[Clique aqui para ver as próximas entradas](README6.md)
