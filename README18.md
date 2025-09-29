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

## Dados Diários - Página 18

| ID | Latitude | Longitude | Data/Hora GMT | Satélite | Município | Estado | País | Município ID | Estado ID | País ID | Dias sem Chuva | Precipitação | Risco de Fogo | Bioma | FRP |
|----|----------|-----------|---------------|----------|-----------|--------|------|--------------|-----------|---------|----------------|--------------|----------------|-------|-----|
| 8df556ca-5fd8-3ee3-9628-d2e5cc4864bd | -15.90926 | -46.21344 | 2025-09-29 03:47:00 | NPP-375D | ARINOS | MINAS GERAIS | Brasil | 3104502 | 31 | 33 | nan | nan | nan | Cerrado | 2.5 |
| fdd25494-1b6c-3644-914c-2c1449fd1485 | -19.96883 | -41.73756 | 2025-09-29 03:47:00 | NPP-375D | CONCEIÇÃO DE IPANEMA | MINAS GERAIS | Brasil | 3117405 | 31 | 33 | nan | nan | nan | Mata Atlântica | 1.6 |
| 21ba9f9b-31f6-3aa8-9bcb-c7196e523668 | -6.68982 | -42.78425 | 2025-09-29 03:47:00 | NPP-375D | FRANCISCO AYRES | PIAUÍ | Brasil | 2204105 | 22 | 33 | nan | nan | nan | Caatinga | 2.7 |
| aef6a1dc-7174-384c-afbc-01d51140fd8e | -11.36051 | -45.08015 | 2025-09-29 03:47:00 | NPP-375D | FORMOSA DO RIO PRETO | BAHIA | Brasil | 2911105 | 29 | 33 | nan | nan | nan | Cerrado | 6.6 |
| 64df639e-1bc8-3cab-9948-9e2b031d289c | -12.23163 | -46.77344 | 2025-09-29 03:47:00 | NPP-375D | PONTE ALTA DO BOM JESUS | TOCANTINS | Brasil | 1717800 | 17 | 33 | nan | nan | nan | Cerrado | 1.5 |
| 999b3bfc-c069-3f7a-b775-d25f54fce3ab | -15.28963 | -49.50984 | 2025-09-29 03:47:00 | NPP-375D | SANTA ISABEL | GOIÁS | Brasil | 5219357 | 52 | 33 | nan | nan | nan | Cerrado | 14.2 |
| f965e6df-fdd3-31b5-b3d8-9105467135ba | -15.68818 | -46.2646 | 2025-09-29 03:47:00 | NPP-375D | ARINOS | MINAS GERAIS | Brasil | 3104502 | 31 | 33 | nan | nan | nan | Cerrado | 0.8 |
| 9ec9f8d3-8265-39b9-bbf4-b5534546cb93 | -7.57165 | -42.40482 | 2025-09-29 03:47:00 | NPP-375D | SÃO MIGUEL DO FIDALGO | PIAUÍ | Brasil | 2210391 | 22 | 33 | nan | nan | nan | Caatinga | 1.1 |
| b33ed2ed-4ed7-3087-8f83-1711cf5b4336 | -15.4703 | -47.93515 | 2025-09-29 03:47:00 | NPP-375D | PLANALTINA | GOIÁS | Brasil | 5217609 | 52 | 33 | nan | nan | nan | Cerrado | 3.9 |
| e8903d6e-736a-3d02-8433-0088f145f565 | -9.77346 | -46.19783 | 2025-09-29 03:47:00 | NPP-375D | ALTO PARNAÍBA | MARANHÃO | Brasil | 2100501 | 21 | 33 | nan | nan | nan | Cerrado | 2.1 |
| 9b93f152-0bfd-3a9b-a073-d20ce9b15abd | -17.39486 | -47.11453 | 2025-09-29 03:47:00 | NPP-375D | PARACATU | MINAS GERAIS | Brasil | 3147006 | 31 | 33 | nan | nan | nan | Cerrado | 1.0 |
| 3e0de0d2-bfdd-3dda-a68d-253b4dfc6673 | -11.27045 | -47.19531 | 2025-09-29 03:47:00 | NPP-375D | ALMAS | TOCANTINS | Brasil | 1700400 | 17 | 33 | nan | nan | nan | Cerrado | 2.8 |
| 92fd6391-4254-3d76-8c0d-6c580f86498f | -12.96235 | -45.19786 | 2025-09-29 03:47:00 | NPP-375D | SÃO DESIDÉRIO | BAHIA | Brasil | 2928901 | 29 | 33 | nan | nan | nan | Cerrado | 1.5 |
| d6d5c1e3-0806-330b-863f-64e92e05792c | -11.45465 | -44.98608 | 2025-09-29 03:47:00 | NPP-375D | RIACHÃO DAS NEVES | BAHIA | Brasil | 2926202 | 29 | 33 | nan | nan | nan | Cerrado | 2.7 |
| 431bb317-6a32-311d-888d-3803e2c69725 | -15.28412 | -46.42159 | 2025-09-29 03:47:00 | NPP-375D | BURITIS | MINAS GERAIS | Brasil | 3109303 | 31 | 33 | nan | nan | nan | Cerrado | 2.3 |
| 084a227f-657e-343f-a7a8-916e3caf938f | -15.49097 | -45.87686 | 2025-09-29 03:47:00 | NPP-375D | ARINOS | MINAS GERAIS | Brasil | 3104502 | 31 | 33 | nan | nan | nan | Cerrado | 2.0 |
| 68bb0f71-58e6-3766-9e2c-0b60d7286b3e | -7.28803 | -42.83755 | 2025-09-29 03:47:00 | NPP-375D | FLORIANO | PIAUÍ | Brasil | 2203909 | 22 | 33 | nan | nan | nan | Caatinga | 1.9 |
| 04bc0bb8-ab51-3502-8c60-ebd8cf079720 | -17.23504 | -44.10783 | 2025-09-29 03:47:00 | NPP-375D | ENGENHEIRO NAVARRO | MINAS GERAIS | Brasil | 3123809 | 31 | 33 | nan | nan | nan | Cerrado | 0.8 |
| 18f097db-407b-3ebe-9016-b81a677631d8 | -7.24604 | -43.01676 | 2025-09-29 03:47:00 | NPP-375D | FLORIANO | PIAUÍ | Brasil | 2203909 | 22 | 33 | nan | nan | nan | Caatinga | 3.5 |
| 32e8048b-02c5-3a38-86fa-38cdeb41d171 | -11.45801 | -44.99621 | 2025-09-29 03:47:00 | NPP-375D | RIACHÃO DAS NEVES | BAHIA | Brasil | 2926202 | 29 | 33 | nan | nan | nan | Cerrado | 0.9 |
| bc7f162d-0faf-36e8-b5f7-ac40973dc952 | -5.67333 | -45.29361 | 2025-09-29 03:47:00 | NPP-375D | BARRA DO CORDA | MARANHÃO | Brasil | 2101608 | 21 | 33 | nan | nan | nan | Cerrado | 2.7 |
| f1e14511-efbb-3960-844c-63f78ff7bbf1 | -6.74395 | -43.37997 | 2025-09-29 03:47:00 | NPP-375D | BARÃO DE GRAJAÚ | MARANHÃO | Brasil | 2101509 | 21 | 33 | nan | nan | nan | Caatinga | 9.4 |
| 110fcba1-7645-3777-bcf2-4c9cec97f9cf | -11.41892 | -44.90937 | 2025-09-29 03:47:00 | NPP-375D | RIACHÃO DAS NEVES | BAHIA | Brasil | 2926202 | 29 | 33 | nan | nan | nan | Cerrado | 2.1 |
| 194217ed-cea3-3575-a308-d38a79c2e479 | -12.00566 | -46.61959 | 2025-09-29 03:47:00 | NPP-375D | PONTE ALTA DO BOM JESUS | TOCANTINS | Brasil | 1717800 | 17 | 33 | nan | nan | nan | Cerrado | 2.4 |
| a6015060-8498-36ee-80e7-17bca4f3bc70 | -15.18703 | -48.48153 | 2025-09-29 03:47:00 | NPP-375D | PADRE BERNARDO | GOIÁS | Brasil | 5215603 | 52 | 33 | nan | nan | nan | Cerrado | 4.3 |
| 239e6d35-a5e7-3d21-924d-92d75520bbd1 | -15.42457 | -48.24445 | 2025-09-29 03:47:00 | NPP-375D | PADRE BERNARDO | GOIÁS | Brasil | 5215603 | 52 | 33 | nan | nan | nan | Cerrado | 1.0 |
| cc294761-a4ad-3d4e-98a3-bb6bbbddb420 | -5.90768 | -45.85733 | 2025-09-29 03:47:00 | NPP-375D | GRAJAÚ | MARANHÃO | Brasil | 2104800 | 21 | 33 | nan | nan | nan | Cerrado | 2.3 |
| 60c2c075-2fc1-3beb-8c64-4bebca71b152 | -7.22739 | -44.79194 | 2025-09-29 03:47:00 | NPP-375D | SÃO FÉLIX DE BALSAS | MARANHÃO | Brasil | 2110807 | 21 | 33 | nan | nan | nan | Cerrado | 10.8 |
| 9ff0b97c-1fb9-37eb-8731-19773d848d8c | -11.9404 | -43.92061 | 2025-09-29 03:47:00 | NPP-375D | WANDERLEY | BAHIA | Brasil | 2933455 | 29 | 33 | nan | nan | nan | Cerrado | 3.8 |
| 91e77527-e04f-3a01-8931-6371190f4587 | -6.8966 | -44.52829 | 2025-09-29 03:47:00 | NPP-375D | SÃO DOMINGOS DO AZEITÃO | MARANHÃO | Brasil | 2110658 | 21 | 33 | nan | nan | nan | Cerrado | 2.4 |
| 7480a238-045a-3e05-8557-b9b076a025de | -9.99931 | -45.41274 | 2025-09-29 03:47:00 | NPP-375D | SÃO GONÇALO DO GURGUÉIA | PIAUÍ | Brasil | 2209757 | 22 | 33 | nan | nan | nan | Cerrado | 2.1 |
| a847146b-c606-34a2-a9ae-e9567e336b59 | -17.40332 | -47.11911 | 2025-09-29 03:47:00 | NPP-375D | PARACATU | MINAS GERAIS | Brasil | 3147006 | 31 | 33 | nan | nan | nan | Cerrado | 1.4 |
| 54fe50f0-8bec-3743-9bc5-95521e1e765f | -5.82598 | -42.79551 | 2025-09-29 03:47:00 | NPP-375D | SÃO PEDRO DO PIAUÍ | PIAUÍ | Brasil | 2210508 | 22 | 33 | nan | nan | nan | Caatinga | 2.2 |
| ebbe87b9-64d8-3210-b562-dae60fff7fef | -15.91482 | -46.21215 | 2025-09-29 03:47:00 | NPP-375D | ARINOS | MINAS GERAIS | Brasil | 3104502 | 31 | 33 | nan | nan | nan | Cerrado | 3.7 |
| e58be19d-50bd-3db8-9a41-0f0d721c6e7b | -10.81173 | -46.67037 | 2025-09-29 03:47:00 | NPP-375D | MATEIROS | TOCANTINS | Brasil | 1712702 | 17 | 33 | nan | nan | nan | Cerrado | 4.2 |
| 2a810e6d-9182-39a6-a2c4-43e104d96a2c | -17.74743 | -48.77393 | 2025-09-29 03:47:00 | NPP-375D | RIO QUENTE | GOIÁS | Brasil | 5218789 | 52 | 33 | nan | nan | nan | Cerrado | 10.7 |
| 340adbef-3c5d-32ce-bd2d-b8eaa203e26f | -8.27371 | -45.50359 | 2025-09-29 03:47:00 | NPP-375D | RIBEIRO GONÇALVES | PIAUÍ | Brasil | 2208908 | 22 | 33 | nan | nan | nan | Cerrado | 50.7 |
| cfbe733b-48ff-3d4f-ab3a-52abd25ca3c7 | -11.44596 | -44.97626 | 2025-09-29 03:47:00 | NPP-375D | RIACHÃO DAS NEVES | BAHIA | Brasil | 2926202 | 29 | 33 | nan | nan | nan | Cerrado | 1.7 |
| 8ba4b100-a1a6-3d0b-9673-2132f00573a2 | -6.14028 | -42.65114 | 2025-09-29 03:47:00 | NPP-375D | JARDIM DO MULATO | PIAUÍ | Brasil | 2205250 | 22 | 33 | nan | nan | nan | Caatinga | 2.1 |
| 0edd321c-c3ae-3323-987d-db92980be6c8 | -17.12326 | -46.98323 | 2025-09-29 03:47:00 | NPP-375D | PARACATU | MINAS GERAIS | Brasil | 3147006 | 31 | 33 | nan | nan | nan | Cerrado | 0.9 |
| 45fc2ce6-11f4-36ff-95c4-91190d1c9655 | -9.27641 | -45.73433 | 2025-09-29 03:47:00 | NPP-375D | SANTA FILOMENA | PIAUÍ | Brasil | 2209203 | 22 | 33 | nan | nan | nan | Cerrado | 1.2 |
| 0c9f0311-6160-3200-a718-97451f4b3230 | -15.50477 | -45.88626 | 2025-09-29 03:47:00 | NPP-375D | ARINOS | MINAS GERAIS | Brasil | 3104502 | 31 | 33 | nan | nan | nan | Cerrado | 6.1 |
| f5003b2b-c1b7-3c50-87c7-a8ec300943cc | -11.93211 | -48.03087 | 2025-09-29 03:47:00 | NPP-375D | SÃO VALÉRIO | TOCANTINS | Brasil | 1720499 | 17 | 33 | nan | nan | nan | Cerrado | 10.3 |
| c37c4f33-7571-3a37-9ca6-60fa90ebab16 | -8.30468 | -45.49168 | 2025-09-29 03:47:00 | NPP-375D | RIBEIRO GONÇALVES | PIAUÍ | Brasil | 2208908 | 22 | 33 | nan | nan | nan | Cerrado | 2.2 |
| 0cceaad5-a68c-321e-a01c-614cb76e6650 | -6.83016 | -44.83302 | 2025-09-29 03:47:00 | NPP-375D | SÃO FÉLIX DE BALSAS | MARANHÃO | Brasil | 2110807 | 21 | 33 | nan | nan | nan | Cerrado | 11.4 |
| 61e4de0f-93ad-3b1d-bfd0-ca0f839eb4b6 | -6.06213 | -42.4791 | 2025-09-29 03:47:00 | NPP-375D | HUGO NAPOLEÃO | PIAUÍ | Brasil | 2204600 | 22 | 33 | nan | nan | nan | Caatinga | 3.6 |
| ee989ce8-c7c8-3acc-a984-de209217e8f9 | -7.84924 | -44.59195 | 2025-09-29 03:47:00 | NPP-375D | URUÇUÍ | PIAUÍ | Brasil | 2211209 | 22 | 33 | nan | nan | nan | Cerrado | 1.7 |
| 1c444bed-8de9-3cfb-bd62-e4c214a7edb5 | -7.58254 | -44.80376 | 2025-09-29 03:47:00 | NPP-375D | URUÇUÍ | PIAUÍ | Brasil | 2211209 | 22 | 33 | nan | nan | nan | Cerrado | 3.6 |
| 8a4cce16-ab36-3b25-b7df-6730a4afdaff | -11.98098 | -46.58115 | 2025-09-29 03:47:00 | NPP-375D | PONTE ALTA DO BOM JESUS | TOCANTINS | Brasil | 1717800 | 17 | 33 | nan | nan | nan | Cerrado | 2.1 |
| add52727-5c46-34bb-8017-ae6bdc0455bb | -19.20085 | -43.98634 | 2025-09-29 03:47:00 | NPP-375D | JEQUITIBÁ | MINAS GERAIS | Brasil | 3135704 | 31 | 33 | nan | nan | nan | Cerrado | 1.2 |
| c3ce4ea0-b655-3ed2-8c98-29d8054276bf | -10.82104 | -47.93761 | 2025-09-29 03:47:00 | NPP-375D | MONTE DO CARMO | TOCANTINS | Brasil | 1713601 | 17 | 33 | nan | nan | nan | Cerrado | 5.3 |
| 77e1e3e5-8d20-39b3-ad96-b57a71b693bb | -12.64953 | -46.92826 | 2025-09-29 03:47:00 | NPP-375D | ARRAIAS | TOCANTINS | Brasil | 1702406 | 17 | 33 | nan | nan | nan | Cerrado | 1.4 |
| 454dcdde-1e04-3d57-9d68-c959f45bd378 | -8.25967 | -45.48596 | 2025-09-29 03:47:00 | NPP-375D | RIBEIRO GONÇALVES | PIAUÍ | Brasil | 2208908 | 22 | 33 | nan | nan | nan | Cerrado | 2.0 |
| 71f67708-2d4e-355f-8205-f25c828509e8 | -7.7647 | -45.74577 | 2025-09-29 03:47:00 | NPP-375D | SAMBAÍBA | MARANHÃO | Brasil | 2109700 | 21 | 33 | nan | nan | nan | Cerrado | 3.6 |
| 39a54287-b6be-3098-8fed-2a85432bbdbf | -6.07208 | -42.47248 | 2025-09-29 03:47:00 | NPP-375D | HUGO NAPOLEÃO | PIAUÍ | Brasil | 2204600 | 22 | 33 | nan | nan | nan | Caatinga | 2.4 |
| 72ab5faa-d891-3795-a4f2-19e8a8375fbd | -11.66445 | -45.3262 | 2025-09-29 03:47:00 | NPP-375D | RIACHÃO DAS NEVES | BAHIA | Brasil | 2926202 | 29 | 33 | nan | nan | nan | Cerrado | 0.9 |
| 813e8c13-7e8f-322f-bac1-42ffc5467d67 | -6.11281 | -43.44978 | 2025-09-29 03:47:00 | NPP-375D | LAGOA DO MATO | MARANHÃO | Brasil | 2105922 | 21 | 33 | nan | nan | nan | Cerrado | 4.7 |
| 17f9db48-97de-3a13-8df2-2bf2d7f22f90 | -6.11237 | -43.47361 | 2025-09-29 03:47:00 | NPP-375D | LAGOA DO MATO | MARANHÃO | Brasil | 2105922 | 21 | 33 | nan | nan | nan | Cerrado | 3.1 |
| 65bd8555-560d-3931-92f5-735a1bd3f406 | -6.27331 | -43.64576 | 2025-09-29 03:47:00 | NPP-375D | PASSAGEM FRANCA | MARANHÃO | Brasil | 2107902 | 21 | 33 | nan | nan | nan | Cerrado | 1.5 |
| 60604213-de8d-3fe2-a572-f10ef750dc19 | -6.25941 | -43.63495 | 2025-09-29 03:47:00 | NPP-375D | PASSAGEM FRANCA | MARANHÃO | Brasil | 2107902 | 21 | 33 | nan | nan | nan | Cerrado | 2.3 |
| 2bbb26de-ea84-3f7d-ac4d-8e62f1cb32d1 | -11.98518 | -46.58955 | 2025-09-29 03:47:00 | NPP-375D | PONTE ALTA DO BOM JESUS | TOCANTINS | Brasil | 1717800 | 17 | 33 | nan | nan | nan | Cerrado | 4.7 |
| c3256b35-af13-3672-afbe-11cb676f868e | -6.75028 | -44.74397 | 2025-09-29 03:47:00 | NPP-375D | SÃO DOMINGOS DO AZEITÃO | MARANHÃO | Brasil | 2110658 | 21 | 33 | nan | nan | nan | Cerrado | 2.3 |
| 79c2c0a0-0dfd-3ed3-a081-0dff423355bb | -11.94026 | -43.91794 | 2025-09-29 03:47:00 | NPP-375D | WANDERLEY | BAHIA | Brasil | 2933455 | 29 | 33 | nan | nan | nan | Cerrado | 3.4 |
| c860d113-6584-39c8-81f4-965e4a01a2dc | -6.74 | -43.3732 | 2025-09-29 03:47:00 | NPP-375D | BARÃO DE GRAJAÚ | MARANHÃO | Brasil | 2101509 | 21 | 33 | nan | nan | nan | Caatinga | 3.9 |
| 4dc59dff-6af5-3646-b7d6-1ca88d3acdc6 | -12.89063 | -45.21729 | 2025-09-29 03:47:00 | NPP-375D | SÃO DESIDÉRIO | BAHIA | Brasil | 2928901 | 29 | 33 | nan | nan | nan | Cerrado | 4.4 |
| 09cb364e-8297-3b7a-8335-009cd77984f3 | -6.08535 | -42.45764 | 2025-09-29 03:47:00 | NPP-375D | HUGO NAPOLEÃO | PIAUÍ | Brasil | 2204600 | 22 | 33 | nan | nan | nan | Caatinga | 4.1 |
| 2a9b8766-589a-3a43-a2a0-f426b8e1d691 | -11.75934 | -47.56376 | 2025-09-29 03:47:00 | NPP-375D | NATIVIDADE | TOCANTINS | Brasil | 1714203 | 17 | 33 | nan | nan | nan | Cerrado | 1.5 |
| a6d163af-4d7c-3f8b-a572-64631529b626 | -6.0548 | -42.45951 | 2025-09-29 03:47:00 | NPP-375D | HUGO NAPOLEÃO | PIAUÍ | Brasil | 2204600 | 22 | 33 | nan | nan | nan | Caatinga | 2.3 |
| 54ff5100-5a30-3f7a-ad9f-4e7a6858db88 | -19.26621 | -41.17556 | 2025-09-29 03:47:00 | NPP-375D | RESPLENDOR | MINAS GERAIS | Brasil | 3154309 | 31 | 33 | nan | nan | nan | Mata Atlântica | 0.5 |
| 067c5274-68f4-3fe9-9391-b13318b8a4ba | -7.46711 | -46.29383 | 2025-09-29 03:47:00 | NPP-375D | BALSAS | MARANHÃO | Brasil | 2101400 | 21 | 33 | nan | nan | nan | Cerrado | 1.5 |
| 3343fe34-551f-364a-9228-685d1ac02621 | -19.6744 | -43.76889 | 2025-09-29 03:47:00 | NPP-375D | SANTA LUZIA | MINAS GERAIS | Brasil | 3157807 | 31 | 33 | nan | nan | nan | Cerrado | 1.3 |
| 35fd8383-1235-3785-af92-a19855b9a2cd | -20.05104 | -41.33552 | 2025-09-29 03:47:00 | NPP-375D | MUTUM | MINAS GERAIS | Brasil | 3144003 | 31 | 33 | nan | nan | nan | Mata Atlântica | 12.8 |
| 442bd4e7-e67c-3b2f-ab51-048ccdc5a62b | -8.8816 | -45.02935 | 2025-09-29 03:47:00 | NPP-375D | BAIXA GRANDE DO RIBEIRO | PIAUÍ | Brasil | 2201150 | 22 | 33 | nan | nan | nan | Cerrado | 1.0 |
| b2b64bae-fb7c-3fa3-b511-10dcdbacffcc | -6.14652 | -43.88501 | 2025-09-29 03:47:00 | NPP-375D | PASSAGEM FRANCA | MARANHÃO | Brasil | 2107902 | 21 | 33 | nan | nan | nan | Cerrado | 4.2 |
| 818dae8f-744a-31aa-a270-d053d30fd443 | -15.28236 | -49.50161 | 2025-09-29 03:47:00 | NPP-375D | SANTA ISABEL | GOIÁS | Brasil | 5219357 | 52 | 33 | nan | nan | nan | Cerrado | 2.5 |
| 98cdf1b5-3a95-3165-b77f-42c8785f6bfa | -6.11387 | -43.46516 | 2025-09-29 03:47:00 | NPP-375D | LAGOA DO MATO | MARANHÃO | Brasil | 2105922 | 21 | 33 | nan | nan | nan | Cerrado | 2.8 |
| 8fb7ffe9-d594-3c2b-b392-f71437782bd8 | -17.39873 | -47.11489 | 2025-09-29 03:47:00 | NPP-375D | PARACATU | MINAS GERAIS | Brasil | 3147006 | 31 | 33 | nan | nan | nan | Cerrado | 1.4 |
| fccd54b1-4142-3663-b9d8-928650549663 | -6.26409 | -43.63831 | 2025-09-29 03:47:00 | NPP-375D | PASSAGEM FRANCA | MARANHÃO | Brasil | 2107902 | 21 | 33 | nan | nan | nan | Cerrado | 2.7 |
| 3033877e-907f-3dac-9595-6a15532be3ef | -19.2016 | -43.98248 | 2025-09-29 03:47:00 | NPP-375D | JEQUITIBÁ | MINAS GERAIS | Brasil | 3135704 | 31 | 33 | nan | nan | nan | Cerrado | 1.2 |
| 010ff2ac-0366-35b2-82aa-0437ec06b23a | -15.28044 | -49.52173 | 2025-09-29 03:47:00 | NPP-375D | RIALMA | GOIÁS | Brasil | 5218607 | 52 | 33 | nan | nan | nan | Cerrado | 2.7 |
| b3646529-3726-3242-94bf-f6748b4af755 | -6.45822 | -44.00858 | 2025-09-29 03:47:00 | NPP-375D | PASTOS BONS | MARANHÃO | Brasil | 2108009 | 21 | 33 | nan | nan | nan | Cerrado | 2.0 |
| a90318f4-e6c9-3b1c-9562-d35288386e09 | -15.28471 | -46.41865 | 2025-09-29 03:47:00 | NPP-375D | BURITIS | MINAS GERAIS | Brasil | 3109303 | 31 | 33 | nan | nan | nan | Cerrado | 2.4 |
| 7f6af36c-e10e-3789-bc2f-54f1c184f87e | -16.34447 | -49.95097 | 2025-09-29 03:47:00 | NPP-375D | ANICUNS | GOIÁS | Brasil | 5201306 | 52 | 33 | nan | nan | nan | Cerrado | 1.1 |
| 846150cb-273d-3dca-b0e7-f8498b2842ed | -6.21553 | -44.19434 | 2025-09-29 03:47:00 | NPP-375D | COLINAS | MARANHÃO | Brasil | 2103505 | 21 | 33 | nan | nan | nan | Cerrado | 1.6 |
| aa7bc7f8-2b0b-3c06-9540-5f14beedb679 | -9.10066 | -45.85106 | 2025-09-29 03:47:00 | NPP-375D | SANTA FILOMENA | PIAUÍ | Brasil | 2209203 | 22 | 33 | nan | nan | nan | Cerrado | 4.3 |
| ad8111f8-fa3f-3004-8363-8f568b0639ff | -16.60342 | -45.13385 | 2025-09-29 03:47:00 | NPP-375D | BURITIZEIRO | MINAS GERAIS | Brasil | 3109402 | 31 | 33 | nan | nan | nan | Cerrado | 1.1 |
| d7089561-6bbe-34c7-9dfe-55f62e0be33c | -11.26964 | -47.19942 | 2025-09-29 03:47:00 | NPP-375D | ALMAS | TOCANTINS | Brasil | 1700400 | 17 | 33 | nan | nan | nan | Cerrado | 3.6 |
| e60cd232-38d3-3d95-93f6-027b8f00ed66 | -11.45354 | -44.99188 | 2025-09-29 03:47:00 | NPP-375D | RIACHÃO DAS NEVES | BAHIA | Brasil | 2926202 | 29 | 33 | nan | nan | nan | Cerrado | 1.9 |
| 4641f74c-8fe0-3d04-8c14-12d5f3423f2a | -7.50405 | -44.29416 | 2025-09-29 03:47:00 | NPP-375D | URUÇUÍ | PIAUÍ | Brasil | 2211209 | 22 | 33 | nan | nan | nan | Cerrado | 2.2 |
| 44ac7491-cd0d-3405-b9c8-17822e565cca | -11.44545 | -45.03435 | 2025-09-29 03:47:00 | NPP-375D | RIACHÃO DAS NEVES | BAHIA | Brasil | 2926202 | 29 | 33 | nan | nan | nan | Cerrado | 0.7 |
| fc919ba6-bf4d-3373-84ed-c688fbc398e0 | -12.66781 | -46.90487 | 2025-09-29 03:47:00 | NPP-375D | ARRAIAS | TOCANTINS | Brasil | 1702406 | 17 | 33 | nan | nan | nan | Cerrado | 2.4 |
| 40ebbe81-9df4-32ab-afb4-c2444029cb3f | -15.42862 | -48.24412 | 2025-09-29 03:47:00 | NPP-375D | PADRE BERNARDO | GOIÁS | Brasil | 5215603 | 52 | 33 | nan | nan | nan | Cerrado | 1.5 |
| a8c81d30-34ac-31fc-8c5d-3898d75d1d7c | -6.42459 | -43.51369 | 2025-09-29 03:47:00 | NPP-375D | SUCUPIRA DO RIACHÃO | MARANHÃO | Brasil | 2111953 | 21 | 33 | nan | nan | nan | Cerrado | 3.6 |
| 69ad9a31-2425-3f2a-acbc-a03d07af4f1f | -16.41156 | -47.02772 | 2025-09-29 03:47:00 | NPP-375D | UNAÍ | MINAS GERAIS | Brasil | 3170404 | 31 | 33 | nan | nan | nan | Cerrado | 0.8 |
| 94ed5898-e8dd-3c56-82a2-2a5f34c0264a | -11.34732 | -45.06543 | 2025-09-29 03:47:00 | NPP-375D | FORMOSA DO RIO PRETO | BAHIA | Brasil | 2911105 | 29 | 33 | nan | nan | nan | Cerrado | 0.6 |
| a2484917-41b3-3723-a4cf-6537e4e21f92 | -7.24734 | -43.01523 | 2025-09-29 03:47:00 | NPP-375D | FLORIANO | PIAUÍ | Brasil | 2203909 | 22 | 33 | nan | nan | nan | Caatinga | 3.0 |
| e3172457-c742-35c5-b68f-9d01700a3cbc | -11.36985 | -44.97434 | 2025-09-29 03:47:00 | NPP-375D | SANTA RITA DE CÁSSIA | BAHIA | Brasil | 2928406 | 29 | 33 | nan | nan | nan | Cerrado | 2.6 |
| 8a94e79e-8535-3817-91ae-2abf6b60fe3e | -7.86535 | -41.06052 | 2025-09-29 03:47:00 | NPP-375D | JACOBINA DO PIAUÍ | PIAUÍ | Brasil | 2205151 | 22 | 33 | nan | nan | nan | Caatinga | 1.7 |
| 6731d557-1676-35f3-a3a0-ea5780ed50d0 | -17.74022 | -46.69497 | 2025-09-29 03:47:00 | NPP-375D | VAZANTE | MINAS GERAIS | Brasil | 3171006 | 31 | 33 | nan | nan | nan | Cerrado | 0.6 |
| 3f9dc09c-74d8-362c-b7e5-8f9f0c66d53f | -6.57903 | -45.09447 | 2025-09-29 03:47:00 | NPP-375D | MIRADOR | MARANHÃO | Brasil | 2106706 | 21 | 33 | nan | nan | nan | Cerrado | 0.7 |


[Clique aqui para ver as próximas entradas](README19.md)
