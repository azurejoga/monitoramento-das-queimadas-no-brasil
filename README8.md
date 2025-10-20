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

## Dados Diários - Página 8

| ID | Latitude | Longitude | Data/Hora GMT | Satélite | Município | Estado | País | Município ID | Estado ID | País ID | Dias sem Chuva | Precipitação | Risco de Fogo | Bioma | FRP |
|----|----------|-----------|---------------|----------|-----------|--------|------|--------------|-----------|---------|----------------|--------------|----------------|-------|-----|
| 591dea43-8904-34c4-a71b-52589c093b57 | -6.09258 | -44.02156 | 2025-10-20 03:51:00 | NPP-375D | COLINAS | MARANHÃO | Brasil | 2103505 | 21 | 33 | nan | nan | nan | Cerrado | 2.5 |
| ee24db4f-dfdf-32d4-9543-ab781be6ff83 | -5.23508 | -46.14371 | 2025-10-20 03:51:00 | NPP-375D | ARAME | MARANHÃO | Brasil | 2100956 | 21 | 33 | nan | nan | nan | Amazônia | 1.3 |
| 973cdc10-3b44-3765-b2ca-0fefc0cd7d0c | -4.82694 | -42.74394 | 2025-10-20 03:51:00 | NPP-375D | TERESINA | PIAUÍ | Brasil | 2211001 | 22 | 33 | nan | nan | nan | Cerrado | 4.8 |
| 2cd611c7-0069-3075-ae78-c538d5d30cc4 | -5.33835 | -42.93402 | 2025-10-20 03:51:00 | NPP-375D | TIMON | MARANHÃO | Brasil | 2112209 | 21 | 33 | nan | nan | nan | Caatinga | 1.0 |
| 641ec51f-bd2c-3997-83ea-7122740031fe | -4.85459 | -45.11787 | 2025-10-20 03:51:00 | NPP-375D | POÇÃO DE PEDRAS | MARANHÃO | Brasil | 2108900 | 21 | 33 | nan | nan | nan | Cerrado | 0.4 |
| 1beecdd0-83b7-33b0-aa7e-b475f7f87475 | -6.09876 | -44.0195 | 2025-10-20 03:51:00 | NPP-375D | COLINAS | MARANHÃO | Brasil | 2103505 | 21 | 33 | nan | nan | nan | Cerrado | 3.5 |
| f91443d3-634e-3dd5-a2dd-1e5fe4339af8 | -4.42696 | -40.17366 | 2025-10-20 03:51:00 | NPP-375D | SANTA QUITÉRIA | CEARÁ | Brasil | 2312205 | 23 | 33 | nan | nan | nan | Caatinga | 1.1 |
| 54fbf775-48f0-3759-94ea-8d153951aa1b | -8.42619 | -44.1314 | 2025-10-20 03:51:00 | NPP-375D | ALVORADA DO GURGUÉIA | PIAUÍ | Brasil | 2200459 | 22 | 33 | nan | nan | nan | Cerrado | 8.8 |
| 697cac55-05ec-31b1-a90d-f934e56db59f | -7.043 | -39.22129 | 2025-10-20 03:51:00 | NPP-375D | CARIRIAÇU | CEARÁ | Brasil | 2303204 | 23 | 33 | nan | nan | nan | Caatinga | 7.4 |
| 15d1bc4d-1148-37fe-b426-7782c5f16f30 | -7.30155 | -39.27105 | 2025-10-20 03:51:00 | NPP-375D | BARBALHA | CEARÁ | Brasil | 2301901 | 23 | 33 | nan | nan | nan | Caatinga | 3.1 |
| 227be660-e471-3649-a35b-189e99c79f28 | -4.86033 | -45.11547 | 2025-10-20 03:51:00 | NPP-375D | POÇÃO DE PEDRAS | MARANHÃO | Brasil | 2108900 | 21 | 33 | nan | nan | nan | Cerrado | 1.0 |
| ca3acd20-c9fb-396f-af9e-cd1ffcb2e06a | -9.56316 | -40.33475 | 2025-10-20 03:51:00 | NPP-375D | JUAZEIRO | BAHIA | Brasil | 2918407 | 29 | 33 | nan | nan | nan | Caatinga | 41.3 |
| 27537d26-4946-300b-ac34-1d09597e9675 | -4.25131 | -44.28456 | 2025-10-20 03:51:00 | NPP-375D | ALTO ALEGRE DO MARANHÃO | MARANHÃO | Brasil | 2100436 | 21 | 33 | nan | nan | nan | Cerrado | 2.4 |
| 45e80f6a-30bd-3133-8a12-c281890de3cc | -5.54056 | -41.34166 | 2025-10-20 03:51:00 | NPP-375D | SÃO MIGUEL DO TAPUIO | PIAUÍ | Brasil | 2210409 | 22 | 33 | nan | nan | nan | Caatinga | 1.6 |
| 3a26e9c2-eb26-3dfb-b9c4-26dd7f37961e | -8.0735 | -48.0128 | 2025-10-20 03:51:00 | NPP-375D | PALMEIRANTE | TOCANTINS | Brasil | 1715705 | 17 | 33 | nan | nan | nan | Cerrado | 2.3 |
| 103565be-0a54-3d70-9987-3a6e738b8833 | -7.5366 | -46.09681 | 2025-10-20 03:51:00 | NPP-375D | BALSAS | MARANHÃO | Brasil | 2101400 | 21 | 33 | nan | nan | nan | Cerrado | 9.4 |
| 96013d35-3af7-34b9-bff1-3142594279c4 | -6.96175 | -46.9776 | 2025-10-20 03:51:00 | NPP-375D | ESTREITO | MARANHÃO | Brasil | 2104057 | 21 | 33 | nan | nan | nan | Cerrado | 1.2 |
| deb19867-a54f-334c-b36b-9639882c10bd | -6.11444 | -41.79411 | 2025-10-20 03:51:00 | NPP-375D | AROAZES | PIAUÍ | Brasil | 2200905 | 22 | 33 | nan | nan | nan | Caatinga | 6.0 |
| e83d5800-2185-38e6-8015-12e005e8c50d | -8.00042 | -39.6316 | 2025-10-20 03:51:00 | NPP-375D | PARNAMIRIM | PERNAMBUCO | Brasil | 2610400 | 26 | 33 | nan | nan | nan | Caatinga | 6.5 |
| bb739929-bbef-30b5-8b69-aef686bb9964 | -7.13664 | -44.25043 | 2025-10-20 03:51:00 | NPP-375D | ANTÔNIO ALMEIDA | PIAUÍ | Brasil | 2200806 | 22 | 33 | nan | nan | nan | Cerrado | 1.9 |
| 2914cf5f-8696-36d3-99bf-3314d15fd863 | -5.83313 | -40.80624 | 2025-10-20 03:51:00 | NPP-375D | QUITERIANÓPOLIS | CEARÁ | Brasil | 2311264 | 23 | 33 | nan | nan | nan | Caatinga | 0.9 |
| 289cd246-1c27-3c56-9747-5cbd753a1b2a | -4.42562 | -43.89244 | 2025-10-20 03:51:00 | NPP-375D | CODÓ | MARANHÃO | Brasil | 2103307 | 21 | 33 | nan | nan | nan | Cerrado | 5.1 |
| f8bbcb32-018e-3686-a3ab-a187993ac5c0 | -5.61809 | -43.65739 | 2025-10-20 03:51:00 | NPP-375D | PARNARAMA | MARANHÃO | Brasil | 2107803 | 21 | 33 | nan | nan | nan | Cerrado | 1.3 |
| 97f830bf-47ac-3932-913b-b4b9530808f7 | -8.42989 | -44.13715 | 2025-10-20 03:51:00 | NPP-375D | ALVORADA DO GURGUÉIA | PIAUÍ | Brasil | 2200459 | 22 | 33 | nan | nan | nan | Cerrado | 36.2 |
| 8aa14193-427b-37a8-a38a-6e73cdae1c3c | -7.1272 | -44.24909 | 2025-10-20 03:51:00 | NPP-375D | ANTÔNIO ALMEIDA | PIAUÍ | Brasil | 2200806 | 22 | 33 | nan | nan | nan | Cerrado | 2.2 |
| 714bd9b9-291b-3a13-b17f-17d0d8800940 | -8.43068 | -44.1326 | 2025-10-20 03:51:00 | NPP-375D | ALVORADA DO GURGUÉIA | PIAUÍ | Brasil | 2200459 | 22 | 33 | nan | nan | nan | Cerrado | 36.2 |
| 95d8e48c-1351-303c-bbae-2301664a7014 | -9.76685 | -41.91732 | 2025-10-20 03:51:00 | NPP-375D | SENTO SÉ | BAHIA | Brasil | 2930204 | 29 | 33 | nan | nan | nan | Caatinga | 2.5 |
| cfd22e67-42a8-3906-9dbf-00e99556c875 | -6.89483 | -43.5989 | 2025-10-20 03:51:00 | NPP-375D | GUADALUPE | PIAUÍ | Brasil | 2204501 | 22 | 33 | nan | nan | nan | Cerrado | 3.2 |
| a884b45d-df22-3edb-832d-d1ba2ae329bc | -7.99818 | -39.62321 | 2025-10-20 03:51:00 | NPP-375D | PARNAMIRIM | PERNAMBUCO | Brasil | 2610400 | 26 | 33 | nan | nan | nan | Caatinga | 2.5 |
| eff3bbd9-3322-3062-8f19-4b675967446f | -5.08607 | -45.89516 | 2025-10-20 03:51:00 | NPP-375D | ARAME | MARANHÃO | Brasil | 2100956 | 21 | 33 | nan | nan | nan | Amazônia | 3.1 |
| 56c5507b-eaeb-30a1-a7c6-df0ba4b2c723 | -7.07227 | -45.21146 | 2025-10-20 03:51:00 | NPP-375D | LORETO | MARANHÃO | Brasil | 2106102 | 21 | 33 | nan | nan | nan | Cerrado | 2.2 |
| 9b235427-4937-3193-a1e8-7e7e84d8dc91 | -8.00105 | -39.62769 | 2025-10-20 03:51:00 | NPP-375D | PARNAMIRIM | PERNAMBUCO | Brasil | 2610400 | 26 | 33 | nan | nan | nan | Caatinga | 2.5 |
| 99cf7628-3f7f-3514-91ec-b44099c12116 | -5.10159 | -43.19665 | 2025-10-20 03:51:00 | NPP-375D | CAXIAS | MARANHÃO | Brasil | 2103000 | 21 | 33 | nan | nan | nan | Cerrado | 2.2 |
| b7fce068-3a1a-38ac-afa0-2e9f047b6878 | -6.89914 | -39.74796 | 2025-10-20 03:51:00 | NPP-375D | ASSARÉ | CEARÁ | Brasil | 2301604 | 23 | 33 | nan | nan | nan | Caatinga | 1.1 |
| 035b4186-3239-3f57-9c15-016a044edf2c | -6.10192 | -44.02362 | 2025-10-20 03:51:00 | NPP-375D | COLINAS | MARANHÃO | Brasil | 2103505 | 21 | 33 | nan | nan | nan | Cerrado | 2.3 |
| b919a940-12f7-3132-8bcb-a706e194d1ae | -4.49432 | -43.12952 | 2025-10-20 03:51:00 | NPP-375D | ALDEIAS ALTAS | MARANHÃO | Brasil | 2100303 | 21 | 33 | nan | nan | nan | Cerrado | 1.2 |
| 2c544b8d-1479-322c-bf6e-e45b69b8ba3e | -6.20466 | -41.53448 | 2025-10-20 03:51:00 | NPP-375D | PIMENTEIRAS | PIAUÍ | Brasil | 2208106 | 22 | 33 | nan | nan | nan | Caatinga | 3.2 |
| 874875a5-a00a-316e-867b-2c636c7d7bfd | -6.20703 | -40.97325 | 2025-10-20 03:51:00 | NPP-375D | PIMENTEIRAS | PIAUÍ | Brasil | 2208106 | 22 | 33 | nan | nan | nan | Caatinga | 1.6 |
| ded0f181-1026-3132-8d75-d71dabe0c0cf | -4.83856 | -43.02873 | 2025-10-20 03:51:00 | NPP-375D | CAXIAS | MARANHÃO | Brasil | 2103000 | 21 | 33 | nan | nan | nan | Cerrado | 2.0 |
| 95a4bc71-9ed7-37c9-950f-583c725403dd | -7.50349 | -38.8203 | 2025-10-20 03:51:00 | NPP-375D | MAURITI | CEARÁ | Brasil | 2308104 | 23 | 33 | nan | nan | nan | Caatinga | 1.1 |
| 929dbe16-9c6b-3883-a8b5-e4e32e7bcacd | -8.07862 | -48.01832 | 2025-10-20 03:51:00 | NPP-375D | PALMEIRANTE | TOCANTINS | Brasil | 1715705 | 17 | 33 | nan | nan | nan | Cerrado | 3.1 |
| 92a6e662-ae4e-3d9b-bc2a-65b9c53c5227 | -6.49989 | -39.72104 | 2025-10-20 03:51:00 | NPP-375D | JUCÁS | CEARÁ | Brasil | 2307403 | 23 | 33 | nan | nan | nan | Caatinga | 2.0 |
| 547d6049-6327-3d3a-aeda-f1721ec0d0fb | -6.39809 | -38.28536 | 2025-10-20 03:51:00 | NPP-375D | PARANÁ | RIO GRANDE DO NORTE | Brasil | 2408607 | 24 | 33 | nan | nan | nan | Caatinga | 3.3 |
| 29ce79ad-f126-3575-827e-d5694018d4e0 | -5.62055 | -43.65091 | 2025-10-20 03:51:00 | NPP-375D | PARNARAMA | MARANHÃO | Brasil | 2107803 | 21 | 33 | nan | nan | nan | Cerrado | 1.5 |
| 517a08ba-44af-3127-a1fb-c9dea938d8ee | -4.42623 | -40.17815 | 2025-10-20 03:51:00 | NPP-375D | SANTA QUITÉRIA | CEARÁ | Brasil | 2312205 | 23 | 33 | nan | nan | nan | Caatinga | 1.2 |
| f4bde9ed-1166-3764-85f4-9e392215a8d2 | -6.95935 | -39.6417 | 2025-10-20 03:51:00 | NPP-375D | ALTANEIRA | CEARÁ | Brasil | 2300606 | 23 | 33 | nan | nan | nan | Caatinga | 1.4 |
| b3ea237b-6c14-3767-938b-825e3d3e6b91 | -5.65303 | -46.81175 | 2025-10-20 03:51:00 | NPP-375D | AMARANTE DO MARANHÃO | MARANHÃO | Brasil | 2100600 | 21 | 33 | nan | nan | nan | Cerrado | 2.1 |
| c21b4080-4a26-3d82-bd7b-197b1dc80bae | -5.49041 | -44.1937 | 2025-10-20 03:51:00 | NPP-375D | GOVERNADOR LUIZ ROCHA | MARANHÃO | Brasil | 2104628 | 21 | 33 | nan | nan | nan | Cerrado | 2.1 |
| 9f6f02a7-6b36-31c9-9465-4dd11470ff1d | -8.07192 | -48.02144 | 2025-10-20 03:51:00 | NPP-375D | PALMEIRANTE | TOCANTINS | Brasil | 1715705 | 17 | 33 | nan | nan | nan | Cerrado | 3.1 |
| aaf1fc8e-28b3-37f8-a05e-62030fb34995 | -5.23993 | -46.14839 | 2025-10-20 03:51:00 | NPP-375D | ARAME | MARANHÃO | Brasil | 2100956 | 21 | 33 | nan | nan | nan | Amazônia | 1.0 |
| 6af3069f-a7f1-3db7-9dbb-f227e68b2e51 | -9.34392 | -40.66118 | 2025-10-20 03:51:00 | NPP-375D | PETROLINA | PERNAMBUCO | Brasil | 2611101 | 26 | 33 | nan | nan | nan | Caatinga | 1.2 |
| 470a7f05-f236-376d-9d8c-73d8ffb2fe54 | -6.21391 | -40.97929 | 2025-10-20 03:51:00 | NPP-375D | PIMENTEIRAS | PIAUÍ | Brasil | 2208106 | 22 | 33 | nan | nan | nan | Caatinga | 4.5 |
| 52b4cc3e-a257-3ffa-84a0-1a51c867c648 | -5.1106 | -43.19831 | 2025-10-20 03:51:00 | NPP-375D | CAXIAS | MARANHÃO | Brasil | 2103000 | 21 | 33 | nan | nan | nan | Cerrado | 3.3 |
| 967b75a7-88a2-316f-8a15-86d7a9b14a05 | -3.58493 | -41.65651 | 2025-10-20 03:51:00 | NPP-375D | COCAL | PIAUÍ | Brasil | 2202703 | 22 | 33 | nan | nan | nan | Caatinga | 0.7 |
| 9d0079fb-53cb-3375-b6ee-1d29316c90c5 | -5.62135 | -43.64609 | 2025-10-20 03:51:00 | NPP-375D | PARNARAMA | MARANHÃO | Brasil | 2107803 | 21 | 33 | nan | nan | nan | Cerrado | 0.7 |
| f990f05f-a0ee-3bae-816b-86c845e4c56d | -4.63478 | -45.05141 | 2025-10-20 03:51:00 | NPP-375D | LAGO DO JUNCO | MARANHÃO | Brasil | 2105807 | 21 | 33 | nan | nan | nan | Cerrado | 1.2 |
| 977ee9ee-e747-36f3-8e48-de679ab23ed2 | -6.46914 | -43.73129 | 2025-10-20 03:51:00 | NPP-375D | SÃO JOÃO DOS PATOS | MARANHÃO | Brasil | 2111102 | 21 | 33 | nan | nan | nan | Cerrado | 0.6 |
| baf22a94-3364-300c-8221-9a6c4ac016cb | -5.28603 | -41.20671 | 2025-10-20 03:51:00 | NPP-375D | BURITI DOS MONTES | PIAUÍ | Brasil | 2202026 | 22 | 33 | nan | nan | nan | Caatinga | 0.9 |
| 18c4c516-91e2-3c55-89b3-0bea55cce9b5 | -5.28689 | -41.20163 | 2025-10-20 03:51:00 | NPP-375D | BURITI DOS MONTES | PIAUÍ | Brasil | 2202026 | 22 | 33 | nan | nan | nan | Caatinga | 0.9 |
| 54a3cccb-9012-3513-9280-8d1215877c4b | -5.39593 | -42.80775 | 2025-10-20 03:51:00 | NPP-375D | NAZÁRIA | PIAUÍ | Brasil | 2206720 | 22 | 33 | nan | nan | nan | Caatinga | 3.0 |
| 5bb06769-c6ac-3a4f-8ec6-f56f507bdf18 | -7.13837 | -44.24073 | 2025-10-20 03:51:00 | NPP-375D | ANTÔNIO ALMEIDA | PIAUÍ | Brasil | 2200806 | 22 | 33 | nan | nan | nan | Cerrado | 1.8 |
| 8e81bd4b-47cb-36c6-a8d5-4b8cff26a7cc | -6.23656 | -44.68938 | 2025-10-20 03:51:00 | NPP-375D | MIRADOR | MARANHÃO | Brasil | 2106706 | 21 | 33 | nan | nan | nan | Cerrado | 1.2 |
| 7df4a782-9bdc-3525-a162-3400c4b3b22b | -7.13218 | -44.24209 | 2025-10-20 03:51:00 | NPP-375D | ANTÔNIO ALMEIDA | PIAUÍ | Brasil | 2200806 | 22 | 33 | nan | nan | nan | Cerrado | 8.8 |
| d50d5f0f-6f61-3df6-9e55-d96408aec54a | -4.83573 | -42.74552 | 2025-10-20 03:51:00 | NPP-375D | TERESINA | PIAUÍ | Brasil | 2211001 | 22 | 33 | nan | nan | nan | Cerrado | 14.8 |
| 1ca490e0-7307-301f-a538-70187f8a3bef | -13.01547 | -43.97552 | 2025-10-20 03:53:00 | NPP-375D | SANTANA | BAHIA | Brasil | 2928208 | 29 | 33 | nan | nan | nan | Cerrado | 3.4 |
| b3dd3f6c-b268-321d-a22c-85d90b97262b | -13.36439 | -44.77391 | 2025-10-20 03:53:00 | NPP-375D | CORRENTINA | BAHIA | Brasil | 2909307 | 29 | 33 | nan | nan | nan | Cerrado | 2.8 |
| 1a76887c-4538-36e8-a0c8-fb0c9ba588cc | -14.30192 | -51.87254 | 2025-10-20 03:53:00 | NPP-375D | NOVA NAZARÉ | MATO GROSSO | Brasil | 5106174 | 51 | 33 | nan | nan | nan | Cerrado | 2.3 |
| 7a5e73a0-3e87-35a8-8af2-91eff0a0d656 | -14.30059 | -51.87859 | 2025-10-20 03:53:00 | NPP-375D | NOVA NAZARÉ | MATO GROSSO | Brasil | 5106174 | 51 | 33 | nan | nan | nan | Cerrado | 2.3 |
| db5894c6-7932-31b4-a826-06866b02b4c7 | -10.76861 | -47.33624 | 2025-10-20 03:53:00 | NPP-375D | PONTE ALTA DO TOCANTINS | TOCANTINS | Brasil | 1717909 | 17 | 33 | nan | nan | nan | Cerrado | 2.6 |
| c621bc0c-f9ce-35c4-958e-482749d98773 | -12.85429 | -43.81475 | 2025-10-20 03:53:00 | NPP-375D | SERRA DOURADA | BAHIA | Brasil | 2930303 | 29 | 33 | nan | nan | nan | Cerrado | 0.5 |
| 369babf1-9636-3b0e-ba63-154d81cfabec | -12.8536 | -43.81854 | 2025-10-20 03:53:00 | NPP-375D | SERRA DOURADA | BAHIA | Brasil | 2930303 | 29 | 33 | nan | nan | nan | Cerrado | 0.5 |
| d2e88bbc-f434-39d0-83b1-c24f3d94f1e3 | -12.24376 | -42.33326 | 2025-10-20 03:53:00 | NPP-375D | BROTAS DE MACAÚBAS | BAHIA | Brasil | 2904506 | 29 | 33 | nan | nan | nan | Caatinga | 3.7 |
| 081cb8bd-fa16-3ece-ab05-dc0ad30a69c0 | -13.01615 | -43.97165 | 2025-10-20 03:53:00 | NPP-375D | SANTANA | BAHIA | Brasil | 2928208 | 29 | 33 | nan | nan | nan | Cerrado | 3.4 |
| d5e0e492-82e2-358b-ac3a-e4f7f9ec93b7 | -13.36517 | -44.76967 | 2025-10-20 03:53:00 | NPP-375D | CORRENTINA | BAHIA | Brasil | 2909307 | 29 | 33 | nan | nan | nan | Cerrado | 2.5 |
| 0b5191f9-3250-394a-b51f-7d5abccd0f67 | -10.8712 | -47.45539 | 2025-10-20 03:53:00 | NPP-375D | PONTE ALTA DO TOCANTINS | TOCANTINS | Brasil | 1717909 | 17 | 33 | nan | nan | nan | Cerrado | 1.1 |
| f673e576-575a-3b8a-a9d4-ea4d2902c6d9 | -10.76995 | -47.3363 | 2025-10-20 03:53:00 | NPP-375D | PONTE ALTA DO TOCANTINS | TOCANTINS | Brasil | 1717909 | 17 | 33 | nan | nan | nan | Cerrado | 1.7 |
| 57d22114-d5ea-3062-9602-d6587b731a2d | -10.7619 | -47.34208 | 2025-10-20 03:53:00 | NPP-375D | PONTE ALTA DO TOCANTINS | TOCANTINS | Brasil | 1717909 | 17 | 33 | nan | nan | nan | Cerrado | 1.4 |
| 4be73f60-3717-3954-b0fa-a75a7e58ea67 | -10.8713 | -47.45458 | 2025-10-20 03:53:00 | NPP-375D | PONTE ALTA DO TOCANTINS | TOCANTINS | Brasil | 1717909 | 17 | 33 | nan | nan | nan | Cerrado | 1.2 |
| 2bba56e2-d3fd-31f1-b585-1a351660fad7 | -13.01198 | -43.97091 | 2025-10-20 03:53:00 | NPP-375D | SANTANA | BAHIA | Brasil | 2928208 | 29 | 33 | nan | nan | nan | Cerrado | 1.2 |
| 0bdb80af-9bbc-3eb5-aeea-447748a10cbf | -10.87197 | -47.451 | 2025-10-20 03:53:00 | NPP-375D | PONTE ALTA DO TOCANTINS | TOCANTINS | Brasil | 1717909 | 17 | 33 | nan | nan | nan | Cerrado | 1.2 |
| 614dda00-279c-3a3a-b214-9a05afa608f4 | -10.86409 | -43.9074 | 2025-10-20 03:53:00 | NPP-375D | BARRA | BAHIA | Brasil | 2902708 | 29 | 33 | nan | nan | nan | Cerrado | 0.6 |
| a53010df-2b57-306c-8af7-3d0112a730fb | -10.87189 | -47.45184 | 2025-10-20 03:53:00 | NPP-375D | PONTE ALTA DO TOCANTINS | TOCANTINS | Brasil | 1717909 | 17 | 33 | nan | nan | nan | Cerrado | 1.1 |
| 64d94dec-e8c8-3a0e-b84e-293ceb1485ad | -10.87053 | -47.45885 | 2025-10-20 03:53:00 | NPP-375D | PONTE ALTA DO TOCANTINS | TOCANTINS | Brasil | 1717909 | 17 | 33 | nan | nan | nan | Cerrado | 0.6 |
| 84e55e79-d541-365e-af09-ea2d3bde6ff4 | -10.75107 | -47.33998 | 2025-10-20 03:53:00 | NPP-375D | PONTE ALTA DO TOCANTINS | TOCANTINS | Brasil | 1717909 | 17 | 33 | nan | nan | nan | Cerrado | 1.1 |
| ff831cb4-7a75-3c3c-aff7-b9ba0d74aa31 | -10.87066 | -47.45805 | 2025-10-20 03:53:00 | NPP-375D | PONTE ALTA DO TOCANTINS | TOCANTINS | Brasil | 1717909 | 17 | 33 | nan | nan | nan | Cerrado | 1.3 |
| 8c849dfc-71b4-3c15-90b4-51aa87d0c090 | -10.86481 | -43.90331 | 2025-10-20 03:53:00 | NPP-375D | BARRA | BAHIA | Brasil | 2902708 | 29 | 33 | nan | nan | nan | Cerrado | 0.6 |
| 25e6b51e-f5ad-3077-8da0-4f7110ad119d | -10.87259 | -47.44823 | 2025-10-20 03:53:00 | NPP-375D | PONTE ALTA DO TOCANTINS | TOCANTINS | Brasil | 1717909 | 17 | 33 | nan | nan | nan | Cerrado | 1.0 |
| 944e6341-9a97-334d-91bf-6d0912cd7119 | -20.60175 | -45.91828 | 2025-10-20 03:55:00 | NPP-375D | PIMENTA | MINAS GERAIS | Brasil | 3150505 | 31 | 33 | nan | nan | nan | Cerrado | 0.9 |
| c8deee1f-6e54-351a-b7c7-701ca4a6b0c5 | -17.67851 | -52.24002 | 2025-10-20 03:55:00 | NPP-375D | MINEIROS | GOIÁS | Brasil | 5213103 | 52 | 33 | nan | nan | nan | Cerrado | 1.1 |
| 43f146d1-41fb-3dfc-8e4c-4893daf3e1fb | -19.0382 | -49.69737 | 2025-10-20 03:55:00 | NPP-375D | GURINHATÃ | MINAS GERAIS | Brasil | 3129103 | 31 | 33 | nan | nan | nan | Cerrado | 5.3 |
| 347f0bdb-d321-3e8e-91b2-ad71fd28a21b | -17.6835 | -52.24783 | 2025-10-20 03:55:00 | NPP-375D | MINEIROS | GOIÁS | Brasil | 5213103 | 52 | 33 | nan | nan | nan | Cerrado | 1.8 |
| f5f296eb-8087-3b09-9f8b-389b32c7bfa4 | -21.73712 | -43.44411 | 2025-10-20 03:55:00 | NPP-375D | JUIZ DE FORA | MINAS GERAIS | Brasil | 3136702 | 31 | 33 | nan | nan | nan | Mata Atlântica | 1.6 |
| 43a5c31a-225e-35d0-9a4f-ece38cd3ed86 | -20.60102 | -45.92201 | 2025-10-20 03:55:00 | NPP-375D | PIMENTA | MINAS GERAIS | Brasil | 3150505 | 31 | 33 | nan | nan | nan | Cerrado | 0.6 |
| 7d9e4d2b-d585-3029-9249-305234abfaca | -19.03745 | -49.70091 | 2025-10-20 03:55:00 | NPP-375D | GURINHATÃ | MINAS GERAIS | Brasil | 3129103 | 31 | 33 | nan | nan | nan | Cerrado | 7.3 |
| b37027e1-77b2-3f6b-b4d3-61b6b79f07ec | -23.6754 | -51.51157 | 2025-10-20 03:57:00 | NPP-375D | CAMBIRA | PARANÁ | Brasil | 4103800 | 41 | 33 | nan | nan | nan | Mata Atlântica | 1.1 |
| e1f19a4f-d1eb-3fa0-82d8-cc2dc45f9b52 | -23.67453 | -51.5153 | 2025-10-20 03:57:00 | NPP-375D | CAMBIRA | PARANÁ | Brasil | 4103800 | 41 | 33 | nan | nan | nan | Mata Atlântica | 2.5 |
| af7b087d-170a-3bca-9d2b-4f4281637288 | -9.5725 | -40.3227 | 2025-10-20 04:00:00 | GOES-19 | JUAZEIRO | BAHIA | Brasil | 2918407 | 29 | 33 | nan | nan | nan | Caatinga | 98.4 |
| abf0589f-dcf7-348f-b90c-88a092102212 | -2.2527 | -51.9108 | 2025-10-20 04:00:00 | GOES-19 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 98.5 |
| 8dcd4db6-2820-384b-a955-5cfa134523ab | -6.8962 | -43.5902 | 2025-10-20 04:00:00 | GOES-19 | GUADALUPE | PIAUÍ | Brasil | 2204501 | 22 | 33 | nan | nan | nan | Cerrado | 73.9 |
| 8cff1d72-a11b-3b29-adcb-75344321352b | -2.2527 | -51.9313 | 2025-10-20 04:00:00 | GOES-19 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 48.1 |


[Clique aqui para ver as próximas entradas](README9.md)
