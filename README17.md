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

## Dados Diários - Página 17

| ID | Latitude | Longitude | Data/Hora GMT | Satélite | Município | Estado | País | Município ID | Estado ID | País ID | Dias sem Chuva | Precipitação | Risco de Fogo | Bioma | FRP |
|----|----------|-----------|---------------|----------|-----------|--------|------|--------------|-----------|---------|----------------|--------------|----------------|-------|-----|
| edcc9d03-111d-3217-bd07-73c90060fbfc | -18.14759 | -45.70392 | 2026-07-21 11:45:00 | TERRA_M-M | JOÃO PINHEIRO | MINAS GERAIS | Brasil | 3136306 | 31 | 33 | nan | nan | nan | Cerrado | 19.4 |
| 0f4321dd-9329-3b23-99b9-42c70391c231 | -17.60068 | -46.68447 | 2026-07-21 11:45:00 | TERRA_M-M | VAZANTE | MINAS GERAIS | Brasil | 3171006 | 31 | 33 | nan | nan | nan | Cerrado | 8.3 |
| 1b3992f9-2b41-31c9-8078-72fb715ad475 | -13.31025 | -45.13496 | 2026-07-21 11:45:00 | TERRA_M-M | CORRENTINA | BAHIA | Brasil | 2909307 | 29 | 33 | nan | nan | nan | Cerrado | 12.9 |
| bd6839b6-f979-34e9-a9cd-72c71268d3f2 | -13.32443 | -51.5896 | 2026-07-21 11:45:00 | TERRA_M-M | RIBEIRÃO CASCALHEIRA | MATO GROSSO | Brasil | 5107180 | 51 | 33 | nan | nan | nan | Cerrado | 17.6 |
| a6d25b1c-5cd3-3663-931c-1ddef4fb5448 | -18.13965 | -45.70659 | 2026-07-21 11:45:00 | TERRA_M-M | JOÃO PINHEIRO | MINAS GERAIS | Brasil | 3136306 | 31 | 33 | nan | nan | nan | Cerrado | 11.3 |
| bf96677a-9d0c-3266-92de-74ec02191700 | -18.14101 | -45.69655 | 2026-07-21 11:45:00 | TERRA_M-M | JOÃO PINHEIRO | MINAS GERAIS | Brasil | 3136306 | 31 | 33 | nan | nan | nan | Cerrado | 16.3 |
| a73735f6-2446-396d-ad8a-312d180c4beb | -11.34935 | -47.99805 | 2026-07-21 11:45:00 | TERRA_M-M | SANTA ROSA DO TOCANTINS | TOCANTINS | Brasil | 1718907 | 17 | 33 | nan | nan | nan | Cerrado | 6.2 |
| 358ad48e-2efb-3a8f-aefa-8a516ebe9367 | -20.4283 | -46.47383 | 2026-07-21 11:45:00 | TERRA_M-M | DELFINÓPOLIS | MINAS GERAIS | Brasil | 3121209 | 31 | 33 | nan | nan | nan | Cerrado | 5.3 |
| e0c7758d-806c-3a02-a30c-cbb92aa5151b | -10.63952 | -50.28385 | 2026-07-21 11:45:00 | TERRA_M-M | LAGOA DA CONFUSÃO | TOCANTINS | Brasil | 1711902 | 17 | 33 | nan | nan | nan | Cerrado | 7.1 |
| ac42ecd1-c604-3c3b-9c6d-454a4f6c034d | -10.55617 | -50.27201 | 2026-07-21 11:45:00 | TERRA_M-M | PIUM | TOCANTINS | Brasil | 1717503 | 17 | 33 | nan | nan | nan | Cerrado | 7.5 |
| f36b1cb5-f8e2-3d71-96f8-1ba6379dff02 | -11.82834 | -46.61398 | 2026-07-21 11:45:00 | TERRA_M-M | NOVO JARDIM | TOCANTINS | Brasil | 1715259 | 17 | 33 | nan | nan | nan | Cerrado | 4.0 |
| 1063bddc-66d3-3f9d-b782-13bd0d2901ef | -17.60375 | -44.59876 | 2026-07-21 11:45:00 | TERRA_M-M | VÁRZEA DA PALMA | MINAS GERAIS | Brasil | 3170800 | 31 | 33 | nan | nan | nan | Cerrado | 8.9 |
| cd9737d8-f5a9-34cc-a8d6-d827dca62727 | -12.51876 | -48.26725 | 2026-07-21 11:45:00 | TERRA_M-M | SÃO SALVADOR DO TOCANTINS | TOCANTINS | Brasil | 1720259 | 17 | 33 | nan | nan | nan | Cerrado | 6.0 |
| fd23e21c-1961-3afb-bdd4-86695c2f406b | -10.37784 | -48.32566 | 2026-07-21 11:45:00 | TERRA_M-M | PALMAS | TOCANTINS | Brasil | 1721000 | 17 | 33 | nan | nan | nan | Cerrado | 8.1 |
| b5f3e37c-dccd-35b2-9731-f31dc31f8d13 | -13.74261 | -45.13908 | 2026-07-21 11:45:00 | TERRA_M-M | JABORANDI | BAHIA | Brasil | 2917359 | 29 | 33 | nan | nan | nan | Cerrado | 4.7 |
| c523df9d-6a63-3533-9c4d-e2b5b882c7ce | -19.36066 | -44.73413 | 2026-07-21 11:45:00 | TERRA_M-M | PAPAGAIOS | MINAS GERAIS | Brasil | 3146909 | 31 | 33 | nan | nan | nan | Cerrado | 17.1 |
| 468b7c79-b497-3fe7-84e6-46f0a54f66d9 | -13.69678 | -45.20405 | 2026-07-21 11:45:00 | TERRA_M-M | CORRENTINA | BAHIA | Brasil | 2909307 | 29 | 33 | nan | nan | nan | Cerrado | 15.4 |
| d53313e4-5b75-3f18-accb-a14c4c65ca6b | -13.02259 | -42.20555 | 2026-07-21 11:45:00 | TERRA_M-M | RIO DO PIRES | BAHIA | Brasil | 2926905 | 29 | 33 | nan | nan | nan | Caatinga | 9.4 |
| 41cee706-5c5f-3037-a4b6-ce0ac9f2c49c | -17.58667 | -47.49966 | 2026-07-21 11:45:00 | TERRA_M-M | CATALÃO | GOIÁS | Brasil | 5205109 | 52 | 33 | nan | nan | nan | Cerrado | 7.2 |
| 3292ebf5-8f04-3071-a0a4-93d2af9ccc87 | -17.58536 | -47.50884 | 2026-07-21 11:45:00 | TERRA_M-M | CATALÃO | GOIÁS | Brasil | 5205109 | 52 | 33 | nan | nan | nan | Cerrado | 10.1 |
| 74b36b84-4a67-363b-bacd-e06f66824847 | -18.14891 | -45.69386 | 2026-07-21 11:45:00 | TERRA_M-M | JOÃO PINHEIRO | MINAS GERAIS | Brasil | 3136306 | 31 | 33 | nan | nan | nan | Cerrado | 5.2 |
| 022946fe-e377-3288-8122-66a4e87ef1de | -12.52965 | -48.24486 | 2026-07-21 11:45:00 | TERRA_M-M | SÃO SALVADOR DO TOCANTINS | TOCANTINS | Brasil | 1720259 | 17 | 33 | nan | nan | nan | Cerrado | 5.9 |
| cc657883-d076-3ab7-a476-6e747b7e6b41 | -19.72412 | -46.16834 | 2026-07-21 11:45:00 | TERRA_M-M | CAMPOS ALTOS | MINAS GERAIS | Brasil | 3111507 | 31 | 33 | nan | nan | nan | Cerrado | 5.3 |
| 768c1e99-7b8f-31b0-a2cb-b54f49ca1fd9 | -11.41882 | -47.52639 | 2026-07-21 11:45:00 | TERRA_M-M | NATIVIDADE | TOCANTINS | Brasil | 1714203 | 17 | 33 | nan | nan | nan | Cerrado | 20.5 |
| 8760b670-4982-31e1-b3bb-7744b18857d4 | -18.19179 | -52.17554 | 2026-07-21 11:45:00 | TERRA_M-M | SERRANÓPOLIS | GOIÁS | Brasil | 5220504 | 52 | 33 | nan | nan | nan | Cerrado | 8.1 |
| f66d42dd-e145-37f8-97c7-1d87d1417045 | -12.52168 | -48.24754 | 2026-07-21 11:45:00 | TERRA_M-M | SÃO SALVADOR DO TOCANTINS | TOCANTINS | Brasil | 1720259 | 17 | 33 | nan | nan | nan | Cerrado | 8.5 |
| 3d678f90-4fde-30cb-bd5d-69a563f77cfe | -10.60366 | -46.53827 | 2026-07-21 11:45:00 | TERRA_M-M | MATEIROS | TOCANTINS | Brasil | 1712702 | 17 | 33 | nan | nan | nan | Cerrado | 4.8 |
| eb1ce9dc-0783-335c-bbe6-01855dfc7eb2 | -11.39592 | -47.49395 | 2026-07-21 11:45:00 | TERRA_M-M | NATIVIDADE | TOCANTINS | Brasil | 1714203 | 17 | 33 | nan | nan | nan | Cerrado | 8.9 |
| d34edbcf-e909-3260-88ec-5cea2e2d972e | -10.63087 | -47.48518 | 2026-07-21 11:45:00 | TERRA_M-M | PONTE ALTA DO TOCANTINS | TOCANTINS | Brasil | 1717909 | 17 | 33 | nan | nan | nan | Cerrado | 5.1 |
| 08e025f6-435f-3541-ae1f-e586a00894fe | -17.60232 | -44.60986 | 2026-07-21 11:45:00 | TERRA_M-M | VÁRZEA DA PALMA | MINAS GERAIS | Brasil | 3170800 | 31 | 33 | nan | nan | nan | Cerrado | 22.3 |
| ed1a6ab8-135b-3b84-b957-d5d93dfbbe5c | -13.01025 | -42.21745 | 2026-07-21 11:45:00 | TERRA_M-M | RIO DO PIRES | BAHIA | Brasil | 2926905 | 29 | 33 | nan | nan | nan | Caatinga | 8.8 |
| 37d8038b-a2f8-31e5-aedd-d632dbd2b54b | -11.42021 | -47.51694 | 2026-07-21 11:45:00 | TERRA_M-M | NATIVIDADE | TOCANTINS | Brasil | 1714203 | 17 | 33 | nan | nan | nan | Cerrado | 8.0 |
| ef610dde-7620-37ce-8e7c-9c3ad4f66783 | -12.52815 | -48.25471 | 2026-07-21 11:45:00 | TERRA_M-M | SÃO SALVADOR DO TOCANTINS | TOCANTINS | Brasil | 1720259 | 17 | 33 | nan | nan | nan | Cerrado | 23.8 |
| 404ccbfb-43c9-3b3b-914b-9aba7e61f320 | -10.59482 | -46.53696 | 2026-07-21 11:45:00 | TERRA_M-M | MATEIROS | TOCANTINS | Brasil | 1712702 | 17 | 33 | nan | nan | nan | Cerrado | 7.5 |
| dada57b3-639d-32fd-9663-0d9c0f0b6f21 | -13.02095 | -42.21869 | 2026-07-21 11:45:00 | TERRA_M-M | RIO DO PIRES | BAHIA | Brasil | 2926905 | 29 | 33 | nan | nan | nan | Caatinga | 8.4 |
| a9f2c69c-93c3-3a9e-9e52-0b6fa2692858 | -17.4612 | -47.14915 | 2026-07-21 11:45:00 | TERRA_M-M | PARACATU | MINAS GERAIS | Brasil | 3147006 | 31 | 33 | nan | nan | nan | Cerrado | 6.5 |
| 2e807244-5fd0-3612-811a-64c2c6ad8709 | -19.60352 | -47.64342 | 2026-07-21 11:45:00 | TERRA_M-M | UBERABA | MINAS GERAIS | Brasil | 3170107 | 31 | 33 | nan | nan | nan | Cerrado | 4.9 |
| 5503db26-1aef-3f5f-a62b-d648e03e8483 | -10.5217 | -50.28066 | 2026-07-21 11:45:00 | TERRA_M-M | PIUM | TOCANTINS | Brasil | 1717503 | 17 | 33 | nan | nan | nan | Cerrado | 12.7 |
| 94b6018a-b38f-3758-93a2-e5e3fc7434f9 | -19.61234 | -47.64478 | 2026-07-21 11:45:00 | TERRA_M-M | UBERABA | MINAS GERAIS | Brasil | 3170107 | 31 | 33 | nan | nan | nan | Cerrado | 6.6 |
| ca58fd16-7eef-3c64-94d5-d234aeb5d87e | -10.55917 | -50.27841 | 2026-07-21 11:45:00 | TERRA_M-M | PIUM | TOCANTINS | Brasil | 1717503 | 17 | 33 | nan | nan | nan | Cerrado | 8.6 |
| 4082852c-0132-3845-ad41-288c64b6a4d8 | -12.83628 | -45.95294 | 2026-07-21 11:45:00 | TERRA_M-M | SÃO DESIDÉRIO | BAHIA | Brasil | 2928901 | 29 | 33 | nan | nan | nan | Cerrado | 5.5 |
| af913669-e1b3-383e-b252-88ab92f7ba37 | -17.57688 | -46.52818 | 2026-07-21 11:45:00 | TERRA_M-M | LAGOA GRANDE | MINAS GERAIS | Brasil | 3137536 | 31 | 33 | nan | nan | nan | Cerrado | 9.1 |
| 7e91b6bc-65cc-38c8-a7f7-2d72cb1e3843 | -21.79859 | -45.30004 | 2026-07-21 11:47:00 | TERRA_M-M | TRÊS CORAÇÕES | MINAS GERAIS | Brasil | 3169307 | 31 | 33 | nan | nan | nan | Mata Atlântica | 13.6 |
| be90e694-d640-3675-b832-c21e060c2433 | -21.10602 | -47.04173 | 2026-07-21 11:47:00 | TERRA_M-M | ITAMOGI | MINAS GERAIS | Brasil | 3132909 | 31 | 33 | nan | nan | nan | Cerrado | 21.2 |
| 79aa7dca-b83f-3d18-904d-c46cfee34403 | -24.49667 | -49.01144 | 2026-07-21 11:47:00 | TERRA_M-M | BARRA DO CHAPÉU | SÃO PAULO | Brasil | 3505351 | 35 | 33 | nan | nan | nan | Mata Atlântica | 8.0 |
| 4cab2989-2e13-31f1-8807-73c5b54bf9f4 | -22.57536 | -47.05846 | 2026-07-21 11:47:00 | TERRA_M-M | HOLAMBRA | SÃO PAULO | Brasil | 3519055 | 35 | 33 | nan | nan | nan | Cerrado | 23.1 |
| 6b83392c-3181-3da0-b4ff-3c71fa6fd75e | -20.70252 | -45.34316 | 2026-07-21 11:47:00 | TERRA_M-M | CANDEIAS | MINAS GERAIS | Brasil | 3112000 | 31 | 33 | nan | nan | nan | Cerrado | 5.0 |
| d214bc11-a1da-3ca9-8558-0ec096e2e16d | -22.57403 | -47.06851 | 2026-07-21 11:47:00 | TERRA_M-M | ARTUR NOGUEIRA | SÃO PAULO | Brasil | 3503802 | 35 | 33 | nan | nan | nan | Cerrado | 18.1 |
| ce950dea-e641-3659-a717-ea7382bfd895 | -21.09703 | -47.04044 | 2026-07-21 11:47:00 | TERRA_M-M | ITAMOGI | MINAS GERAIS | Brasil | 3132909 | 31 | 33 | nan | nan | nan | Cerrado | 7.4 |
| 0954038a-f825-3978-9dd5-021994c35367 | -22.56143 | -43.64632 | 2026-07-21 11:47:00 | TERRA_M-M | PARACAMBI | RIO DE JANEIRO | Brasil | 3303609 | 33 | 33 | nan | nan | nan | Mata Atlântica | 8.8 |
| f902765b-fa1e-3c8a-964e-870524cf128d | -21.46877 | -41.30125 | 2026-07-21 11:47:00 | TERRA_M-M | CAMPOS DOS GOYTACAZES | RIO DE JANEIRO | Brasil | 3301009 | 33 | 33 | nan | nan | nan | Mata Atlântica | 28.3 |
| 3f67ce16-c0fb-3ad4-a455-e1deb3be9df3 | -12.533 | -48.2555 | 2026-07-21 12:00:00 | GOES-19 | SÃO SALVADOR DO TOCANTINS | TOCANTINS | Brasil | 1720259 | 17 | 33 | nan | nan | nan | Cerrado | 99.8 |
| 920714cc-6da4-3cfb-9268-c16509ed3263 | -12.5138 | -48.2581 | 2026-07-21 12:10:00 | GOES-19 | SÃO SALVADOR DO TOCANTINS | TOCANTINS | Brasil | 1720259 | 17 | 33 | nan | nan | nan | Cerrado | 96.9 |
| d1d33280-5a48-3997-abcf-1788fa52431b | -12.5138 | -48.2581 | 2026-07-21 12:20:00 | GOES-19 | SÃO SALVADOR DO TOCANTINS | TOCANTINS | Brasil | 1720259 | 17 | 33 | nan | nan | nan | Cerrado | 88.2 |
| 3860d16c-716b-306e-8cf0-41e1a6931668 | -12.533 | -48.2555 | 2026-07-21 12:20:00 | GOES-19 | SÃO SALVADOR DO TOCANTINS | TOCANTINS | Brasil | 1720259 | 17 | 33 | nan | nan | nan | Cerrado | 116.5 |
| 730fe00e-21d0-3eb3-a3dd-268f26442494 | -12.5138 | -48.2581 | 2026-07-21 12:30:00 | GOES-19 | SÃO SALVADOR DO TOCANTINS | TOCANTINS | Brasil | 1720259 | 17 | 33 | nan | nan | nan | Cerrado | 82.1 |
| 0ed81236-b38a-3cc4-bbee-cc984b361480 | -12.533 | -48.2555 | 2026-07-21 12:30:00 | GOES-19 | SÃO SALVADOR DO TOCANTINS | TOCANTINS | Brasil | 1720259 | 17 | 33 | nan | nan | nan | Cerrado | 130.8 |
| b138bcd4-470b-30fd-bc75-24f71c5d1a97 | -12.3321 | -50.0073 | 2026-07-21 12:40:00 | GOES-19 | SANDOLÂNDIA | TOCANTINS | Brasil | 1718840 | 17 | 33 | nan | nan | nan | Cerrado | 69.1 |
| 91f96962-f82a-3bd0-aaa4-7c58b841f1c0 | -12.533 | -48.2555 | 2026-07-21 12:40:00 | GOES-19 | SÃO SALVADOR DO TOCANTINS | TOCANTINS | Brasil | 1720259 | 17 | 33 | nan | nan | nan | Cerrado | 119.9 |
| 133550d2-a948-38a1-9acd-1a9bafb4bb74 | -12.5138 | -48.2581 | 2026-07-21 12:40:00 | GOES-19 | SÃO SALVADOR DO TOCANTINS | TOCANTINS | Brasil | 1720259 | 17 | 33 | nan | nan | nan | Cerrado | 81.1 |
| 54388ed2-aeda-3ed3-aab0-a3e17a32ad12 | -12.3321 | -50.0073 | 2026-07-21 12:50:00 | GOES-19 | SANDOLÂNDIA | TOCANTINS | Brasil | 1718840 | 17 | 33 | nan | nan | nan | Cerrado | 69.3 |
| 085c54fa-b40e-3fb1-b721-cf7ecc31e514 | -8.8537 | -46.7228 | 2026-07-21 12:50:00 | GOES-19 | BALSAS | MARANHÃO | Brasil | 2101400 | 21 | 33 | nan | nan | nan | Cerrado | 78.1 |
| aad1325a-7540-3ff9-a302-e7d43805effd | -12.5138 | -48.2581 | 2026-07-21 12:50:00 | GOES-19 | SÃO SALVADOR DO TOCANTINS | TOCANTINS | Brasil | 1720259 | 17 | 33 | nan | nan | nan | Cerrado | 91.2 |
| 3ac62a75-dc89-34d8-b070-e2c4d86f753a | -12.533 | -48.2555 | 2026-07-21 12:50:00 | GOES-19 | SÃO SALVADOR DO TOCANTINS | TOCANTINS | Brasil | 1720259 | 17 | 33 | nan | nan | nan | Cerrado | 103.5 |
| 927e9b62-4299-350b-ace7-489e460924fc | -8.8537 | -46.7228 | 2026-07-21 13:00:00 | GOES-19 | BALSAS | MARANHÃO | Brasil | 2101400 | 21 | 33 | nan | nan | nan | Cerrado | 71.7 |
| 4dc89990-1888-32d6-9f93-d0d575160a48 | -12.5138 | -48.2581 | 2026-07-21 13:00:00 | GOES-19 | SÃO SALVADOR DO TOCANTINS | TOCANTINS | Brasil | 1720259 | 17 | 33 | nan | nan | nan | Cerrado | 119.1 |
| c9d5d376-83d7-3906-82ef-4c421f20c8f2 | -12.3321 | -50.0073 | 2026-07-21 13:00:00 | GOES-19 | SANDOLÂNDIA | TOCANTINS | Brasil | 1718840 | 17 | 33 | nan | nan | nan | Cerrado | 78.2 |
| 718b10d0-c693-3a71-a7fe-48c63192ef92 | -12.533 | -48.2555 | 2026-07-21 13:00:00 | GOES-19 | SÃO SALVADOR DO TOCANTINS | TOCANTINS | Brasil | 1720259 | 17 | 33 | nan | nan | nan | Cerrado | 87.6 |
| bb027ef7-9d90-3c32-8a44-a80d07542d84 | -12.5138 | -48.2581 | 2026-07-21 13:10:00 | GOES-19 | SÃO SALVADOR DO TOCANTINS | TOCANTINS | Brasil | 1720259 | 17 | 33 | nan | nan | nan | Cerrado | 88.7 |
| 86ad3d32-b7a2-3397-aaf4-09c7b93abd49 | -12.533 | -48.2555 | 2026-07-21 13:10:00 | GOES-19 | SÃO SALVADOR DO TOCANTINS | TOCANTINS | Brasil | 1720259 | 17 | 33 | nan | nan | nan | Cerrado | 99.4 |
| 62d9b82b-8033-3c56-8389-62257aa5d8d5 | -8.8537 | -46.7228 | 2026-07-21 13:10:00 | GOES-19 | BALSAS | MARANHÃO | Brasil | 2101400 | 21 | 33 | nan | nan | nan | Cerrado | 85.4 |
| dabcae17-c1ad-3806-8f17-6dfa2a41f310 | -12.3321 | -50.0073 | 2026-07-21 13:10:00 | GOES-19 | SANDOLÂNDIA | TOCANTINS | Brasil | 1718840 | 17 | 33 | nan | nan | nan | Cerrado | 72.9 |
| 8a258fea-73e8-3029-92f7-b0def3e2b2e9 | -8.8537 | -46.7228 | 2026-07-21 13:20:00 | GOES-19 | BALSAS | MARANHÃO | Brasil | 2101400 | 21 | 33 | nan | nan | nan | Cerrado | 78.1 |
| 6ddd46b5-15ac-37e9-a258-da15fb84cfb6 | -12.5138 | -48.2581 | 2026-07-21 13:20:00 | GOES-19 | SÃO SALVADOR DO TOCANTINS | TOCANTINS | Brasil | 1720259 | 17 | 33 | nan | nan | nan | Cerrado | 67.1 |
| a2b1457c-ed20-37ee-9161-223d6cfdc611 | -12.533 | -48.2555 | 2026-07-21 13:20:00 | GOES-19 | SÃO SALVADOR DO TOCANTINS | TOCANTINS | Brasil | 1720259 | 17 | 33 | nan | nan | nan | Cerrado | 92.1 |
| 781cd9d8-2d85-39ab-8e2e-ab2dd04acfc2 | -17.0609 | -45.043 | 2026-07-21 13:20:00 | GOES-19 | BURITIZEIRO | MINAS GERAIS | Brasil | 3109402 | 31 | 33 | nan | nan | nan | Cerrado | 89.7 |
| 4aa830da-28f6-3eff-9c36-4f8b7e0fd9cc | -12.5138 | -48.2581 | 2026-07-21 13:30:00 | GOES-19 | SÃO SALVADOR DO TOCANTINS | TOCANTINS | Brasil | 1720259 | 17 | 33 | nan | nan | nan | Cerrado | 78.0 |
| f9603dec-f85e-3781-9e3a-187fa72545aa | -10.3807 | -48.3254 | 2026-07-21 13:30:00 | GOES-19 | PALMAS | TOCANTINS | Brasil | 1721000 | 17 | 33 | nan | nan | nan | Cerrado | 85.9 |
| 68ff0900-6d75-3cfb-a9e6-e78b112ca7f1 | -8.8537 | -46.7228 | 2026-07-21 13:30:00 | GOES-19 | BALSAS | MARANHÃO | Brasil | 2101400 | 21 | 33 | nan | nan | nan | Cerrado | 84.9 |
| f2feb780-6869-3d64-964e-cb9b547de9de | -12.533 | -48.2555 | 2026-07-21 13:30:00 | GOES-19 | SÃO SALVADOR DO TOCANTINS | TOCANTINS | Brasil | 1720259 | 17 | 33 | nan | nan | nan | Cerrado | 88.8 |
| 2c7fd443-8487-3c81-9988-65b085775d7e | -12.533 | -48.2555 | 2026-07-21 13:40:00 | GOES-19 | SÃO SALVADOR DO TOCANTINS | TOCANTINS | Brasil | 1720259 | 17 | 33 | nan | nan | nan | Cerrado | 78.3 |
| 8d14daae-41e4-3ea9-bbdb-4f005d421daa | -8.8537 | -46.7228 | 2026-07-21 13:40:00 | GOES-19 | BALSAS | MARANHÃO | Brasil | 2101400 | 21 | 33 | nan | nan | nan | Cerrado | 74.3 |
| 870a30cb-013c-31b0-ae33-1da2c92b274b | -10.3807 | -48.3254 | 2026-07-21 13:40:00 | GOES-19 | PALMAS | TOCANTINS | Brasil | 1721000 | 17 | 33 | nan | nan | nan | Cerrado | 79.1 |
| 65f50cbf-e295-389d-95ca-8bea54b6c00d | -12.533 | -48.2555 | 2026-07-21 13:50:00 | GOES-19 | SÃO SALVADOR DO TOCANTINS | TOCANTINS | Brasil | 1720259 | 17 | 33 | nan | nan | nan | Cerrado | 68.6 |
| 6e7832db-2e3b-31fb-8f6b-1e880216c4f5 | -12.5138 | -48.2581 | 2026-07-21 13:50:00 | GOES-19 | SÃO SALVADOR DO TOCANTINS | TOCANTINS | Brasil | 1720259 | 17 | 33 | nan | nan | nan | Cerrado | 75.9 |
| cac4afd8-5f50-3662-b6b3-0a394422a332 | -10.3807 | -48.3254 | 2026-07-21 13:50:00 | GOES-19 | PALMAS | TOCANTINS | Brasil | 1721000 | 17 | 33 | nan | nan | nan | Cerrado | 86.7 |
| e6c1f3f2-895b-308c-8149-294f968a9b08 | -12.533 | -48.2555 | 2026-07-21 14:00:00 | GOES-19 | SÃO SALVADOR DO TOCANTINS | TOCANTINS | Brasil | 1720259 | 17 | 33 | nan | nan | nan | Cerrado | 74.3 |
| 01706ce5-cff7-3804-b551-065766d90051 | -10.3807 | -48.3254 | 2026-07-21 14:00:00 | GOES-19 | PALMAS | TOCANTINS | Brasil | 1721000 | 17 | 33 | nan | nan | nan | Cerrado | 91.6 |
| 04ac6099-6900-389e-b3e4-6ea8e2c69758 | -12.5138 | -48.2581 | 2026-07-21 14:00:00 | GOES-19 | SÃO SALVADOR DO TOCANTINS | TOCANTINS | Brasil | 1720259 | 17 | 33 | nan | nan | nan | Cerrado | 91.4 |
| bd0fa691-da09-34e7-a7aa-1d6e076764da | -12.5138 | -48.2581 | 2026-07-21 14:10:00 | GOES-19 | SÃO SALVADOR DO TOCANTINS | TOCANTINS | Brasil | 1720259 | 17 | 33 | nan | nan | nan | Cerrado | 79.5 |
| 2a9571d7-4368-30dc-908e-0e9116ff0289 | -7.6188 | -49.7522 | 2026-07-21 14:10:00 | GOES-19 | FLORESTA DO ARAGUAIA | PARÁ | Brasil | 1503044 | 15 | 33 | nan | nan | nan | Amazônia | 75.3 |
| 98ba0318-bf44-37be-af2c-38850c48a023 | -7.6375 | -49.7507 | 2026-07-21 14:10:00 | GOES-19 | FLORESTA DO ARAGUAIA | PARÁ | Brasil | 1503044 | 15 | 33 | nan | nan | nan | Amazônia | 124.8 |
| 559a0489-18c4-39b1-82de-61756dfb42dd | -10.3807 | -48.3254 | 2026-07-21 14:10:00 | GOES-19 | PALMAS | TOCANTINS | Brasil | 1721000 | 17 | 33 | nan | nan | nan | Cerrado | 101.2 |
| 155c3641-d991-3865-974f-d21af1edcabb | -12.533 | -48.2555 | 2026-07-21 14:10:00 | GOES-19 | SÃO SALVADOR DO TOCANTINS | TOCANTINS | Brasil | 1720259 | 17 | 33 | nan | nan | nan | Cerrado | 103.6 |
| 7b0a1eda-a339-32ad-9b63-7b4599cd3178 | -13.42 | -51.66 | 2026-07-21 14:15:00 | MSG-03 | CANARANA | MATO GROSSO | Brasil | 5102702 | 51 | 33 | nan | nan | nan | Cerrado | nan |
| 05edf670-e5db-309f-9ad2-1d4aec7c3747 | -7.6188 | -49.7522 | 2026-07-21 14:20:00 | GOES-19 | FLORESTA DO ARAGUAIA | PARÁ | Brasil | 1503044 | 15 | 33 | nan | nan | nan | Amazônia | 78.8 |
| f51f3d2d-2d39-350f-9969-61d9e1028a9f | -12.5138 | -48.2581 | 2026-07-21 14:20:00 | GOES-19 | SÃO SALVADOR DO TOCANTINS | TOCANTINS | Brasil | 1720259 | 17 | 33 | nan | nan | nan | Cerrado | 102.7 |
| a3d02735-7be5-31a9-b926-1f564a3b45d6 | -10.6373 | -50.2874 | 2026-07-21 14:20:00 | GOES-19 | LAGOA DA CONFUSÃO | TOCANTINS | Brasil | 1711902 | 17 | 33 | nan | nan | nan | Cerrado | 74.0 |
| cf5e7fd2-ca3f-3c2e-ae43-5a7e1d55011e | -12.533 | -48.2555 | 2026-07-21 14:20:00 | GOES-19 | SÃO SALVADOR DO TOCANTINS | TOCANTINS | Brasil | 1720259 | 17 | 33 | nan | nan | nan | Cerrado | 81.4 |
| 040e59c7-5959-3821-a679-eb26de3d435a | -7.6375 | -49.7507 | 2026-07-21 14:20:00 | GOES-19 | FLORESTA DO ARAGUAIA | PARÁ | Brasil | 1503044 | 15 | 33 | nan | nan | nan | Amazônia | 97.5 |


[Clique aqui para ver as próximas entradas](README18.md)
