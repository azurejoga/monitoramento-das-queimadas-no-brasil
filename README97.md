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

## Dados Diários - Página 97

| ID | Latitude | Longitude | Data/Hora GMT | Satélite | Município | Estado | País | Município ID | Estado ID | País ID | Dias sem Chuva | Precipitação | Risco de Fogo | Bioma | FRP |
|----|----------|-----------|---------------|----------|-----------|--------|------|--------------|-----------|---------|----------------|--------------|----------------|-------|-----|
| 9b00d80d-1906-32e1-8a8f-2dda3a2e2644 | -11.87574 | -46.44995 | 2025-08-30 12:17:00 | TERRA_M-T | PONTE ALTA DO BOM JESUS | TOCANTINS | Brasil | 1717800 | 17 | 33 | nan | nan | nan | Cerrado | 29.4 |
| 0d1bdd7d-1332-30cb-97f2-5a2e13e2c29a | -11.82423 | -46.48206 | 2025-08-30 12:17:00 | TERRA_M-T | PONTE ALTA DO BOM JESUS | TOCANTINS | Brasil | 1717800 | 17 | 33 | nan | nan | nan | Cerrado | 21.5 |
| f404da64-2dd3-3855-80ae-b339edb0d112 | -13.52451 | -46.96614 | 2025-08-30 12:17:00 | TERRA_M-T | MONTE ALEGRE DE GOIÁS | GOIÁS | Brasil | 5213509 | 52 | 33 | nan | nan | nan | Cerrado | 26.7 |
| 06dc4238-cad5-337e-b3e1-6217310c801b | -11.83616 | -51.48064 | 2025-08-30 12:17:00 | TERRA_M-T | ALTO BOA VISTA | MATO GROSSO | Brasil | 5100359 | 51 | 33 | nan | nan | nan | Cerrado | 9.5 |
| 4eefebf7-9ba3-3fc8-85bc-6376b1b4a13c | -13.36811 | -46.97369 | 2025-08-30 12:17:00 | TERRA_M-T | MONTE ALEGRE DE GOIÁS | GOIÁS | Brasil | 5213509 | 52 | 33 | nan | nan | nan | Cerrado | 47.2 |
| 2d1b27f1-47d5-3ff4-812f-4d5c86994133 | -14.59955 | -44.61908 | 2025-08-30 12:17:00 | TERRA_M-T | MONTALVÂNIA | MINAS GERAIS | Brasil | 3142700 | 31 | 33 | nan | nan | nan | Cerrado | 5.1 |
| 7f54f961-61d7-3d2d-b46d-05ecc3f0bbfb | -13.3694 | -46.96467 | 2025-08-30 12:17:00 | TERRA_M-T | MONTE ALEGRE DE GOIÁS | GOIÁS | Brasil | 5213509 | 52 | 33 | nan | nan | nan | Cerrado | 21.6 |
| 75d22456-4ce9-3419-bf42-e636af439795 | -11.35747 | -43.57817 | 2025-08-30 12:17:00 | TERRA_M-T | BARRA | BAHIA | Brasil | 2902708 | 29 | 33 | nan | nan | nan | Cerrado | 20.9 |
| 28187d4c-6668-35aa-8dd4-5832733dc0a6 | -11.88597 | -46.37791 | 2025-08-30 12:17:00 | TERRA_M-T | PONTE ALTA DO BOM JESUS | TOCANTINS | Brasil | 1717800 | 17 | 33 | nan | nan | nan | Cerrado | 388.4 |
| 3e404b0c-74d5-3745-b372-3a9498eb5465 | -12.65865 | -48.16925 | 2025-08-30 12:17:00 | TERRA_M-T | PARANÃ | TOCANTINS | Brasil | 1716208 | 17 | 33 | nan | nan | nan | Cerrado | 43.9 |
| 4f39b323-a809-3938-acbc-c2cf262c75ab | -13.39852 | -46.95045 | 2025-08-30 12:17:00 | TERRA_M-T | MONTE ALEGRE DE GOIÁS | GOIÁS | Brasil | 5213509 | 52 | 33 | nan | nan | nan | Cerrado | 15.5 |
| b359898b-60e5-330c-b632-ba7087411550 | -11.90114 | -46.39845 | 2025-08-30 12:17:00 | TERRA_M-T | PONTE ALTA DO BOM JESUS | TOCANTINS | Brasil | 1717800 | 17 | 33 | nan | nan | nan | Cerrado | 62.6 |
| 87fedf40-acae-3093-8a2b-e9a3ba5a7eef | -12.85182 | -48.17286 | 2025-08-30 12:17:00 | TERRA_M-T | PARANÃ | TOCANTINS | Brasil | 1716208 | 17 | 33 | nan | nan | nan | Cerrado | 19.4 |
| 5338d13e-6430-363b-874f-688d3444fa63 | -13.98711 | -41.38136 | 2025-08-30 12:17:00 | TERRA_M-T | ITUAÇU | BAHIA | Brasil | 2917201 | 29 | 33 | nan | nan | nan | Caatinga | 15.1 |
| 250d6081-1986-3dd4-8ec4-c9d544bd5b76 | -13.34203 | -46.88997 | 2025-08-30 12:17:00 | TERRA_M-T | MONTE ALEGRE DE GOIÁS | GOIÁS | Brasil | 5213509 | 52 | 33 | nan | nan | nan | Cerrado | 41.7 |
| 3ca09a45-913b-39d5-952b-b901ee831a5e | -9.77261 | -49.88748 | 2025-08-30 12:17:00 | TERRA_M-T | MARIANÓPOLIS DO TOCANTINS | TOCANTINS | Brasil | 1712504 | 17 | 33 | nan | nan | nan | Cerrado | 38.3 |
| 885e8826-8edf-322c-bd7c-f9ffc3621726 | -13.47273 | -46.94947 | 2025-08-30 12:17:00 | TERRA_M-T | MONTE ALEGRE DE GOIÁS | GOIÁS | Brasil | 5213509 | 52 | 33 | nan | nan | nan | Cerrado | 11.8 |
| 1ccd27d5-6a1e-33b7-ae3d-c12598e1e81a | -14.01017 | -44.58627 | 2025-08-30 12:17:00 | TERRA_M-T | COCOS | BAHIA | Brasil | 2908101 | 29 | 33 | nan | nan | nan | Cerrado | 31.5 |
| 1481a0f1-a3c3-346a-bf39-9122e7b2fc55 | -13.35669 | -46.99044 | 2025-08-30 12:17:00 | TERRA_M-T | MONTE ALEGRE DE GOIÁS | GOIÁS | Brasil | 5213509 | 52 | 33 | nan | nan | nan | Cerrado | 28.5 |
| c3673a80-fb99-389f-bab7-8f5c533193ab | -11.87446 | -46.45897 | 2025-08-30 12:17:00 | TERRA_M-T | PONTE ALTA DO BOM JESUS | TOCANTINS | Brasil | 1717800 | 17 | 33 | nan | nan | nan | Cerrado | 32.5 |
| 088603c9-63e4-353a-b66f-08d996a4b6cc | -13.5094 | -46.94551 | 2025-08-30 12:17:00 | TERRA_M-T | MONTE ALEGRE DE GOIÁS | GOIÁS | Brasil | 5213509 | 52 | 33 | nan | nan | nan | Cerrado | 8.2 |
| f166a6fa-2acc-3eaa-a7fb-c47eb6ca257f | -11.83949 | -46.43838 | 2025-08-30 12:17:00 | TERRA_M-T | PONTE ALTA DO BOM JESUS | TOCANTINS | Brasil | 1717800 | 17 | 33 | nan | nan | nan | Cerrado | 15.6 |
| 603280b6-e016-3b86-8b74-80268ebd7456 | -11.8771 | -46.37671 | 2025-08-30 12:17:00 | TERRA_M-T | PONTE ALTA DO BOM JESUS | TOCANTINS | Brasil | 1717800 | 17 | 33 | nan | nan | nan | Cerrado | 155.4 |
| f126bb2c-9768-3e76-831f-756e5e2e06da | -12.45147 | -47.69664 | 2025-08-30 12:17:00 | TERRA_M-T | PARANÃ | TOCANTINS | Brasil | 1716208 | 17 | 33 | nan | nan | nan | Cerrado | 39.3 |
| 01fe5ee5-9ce5-3b58-9e51-e1107dc58468 | -10.09775 | -47.00739 | 2025-08-30 12:17:00 | TERRA_M-T | SÃO FÉLIX DO TOCANTINS | TOCANTINS | Brasil | 1720150 | 17 | 33 | nan | nan | nan | Cerrado | 8.2 |
| d6a042e5-73ae-3745-a7d4-9e1f07edb01f | -12.94191 | -42.48767 | 2025-08-30 12:17:00 | TERRA_M-T | MACAÚBAS | BAHIA | Brasil | 2919801 | 29 | 33 | nan | nan | nan | Caatinga | 19.3 |
| abb1b51e-5ef9-3612-b9a0-861fbccac827 | -10.02309 | -48.08474 | 2025-08-30 12:17:00 | TERRA_M-T | APARECIDA DO RIO NEGRO | TOCANTINS | Brasil | 1701101 | 17 | 33 | nan | nan | nan | Cerrado | 9.7 |
| de4de300-2e36-3599-8d36-fcd8d5b249ad | -11.89356 | -46.38819 | 2025-08-30 12:17:00 | TERRA_M-T | PONTE ALTA DO BOM JESUS | TOCANTINS | Brasil | 1717800 | 17 | 33 | nan | nan | nan | Cerrado | 144.1 |
| a6f12209-e183-3566-81cd-86539196015f | -12.93262 | -42.47192 | 2025-08-30 12:17:00 | TERRA_M-T | MACAÚBAS | BAHIA | Brasil | 2919801 | 29 | 33 | nan | nan | nan | Caatinga | 25.4 |
| f4a02168-84e8-3501-ab41-1303f5c97e75 | -12.82287 | -48.12086 | 2025-08-30 12:17:00 | TERRA_M-T | PARANÃ | TOCANTINS | Brasil | 1716208 | 17 | 33 | nan | nan | nan | Cerrado | 4.6 |
| 74085222-95f8-3bd3-936b-7148d7776cbe | -13.98474 | -46.32054 | 2025-08-30 12:17:00 | TERRA_M-T | GUARANI DE GOIÁS | GOIÁS | Brasil | 5209408 | 52 | 33 | nan | nan | nan | Cerrado | 14.3 |
| dc116f18-8b19-3004-aae0-a577a74dfd73 | -12.94088 | -42.48128 | 2025-08-30 12:17:00 | TERRA_M-T | MACAÚBAS | BAHIA | Brasil | 2919801 | 29 | 33 | nan | nan | nan | Caatinga | 70.9 |
| 76b30a5b-23bd-3401-91c7-9a98e41fc2a2 | -12.85455 | -48.15436 | 2025-08-30 12:17:00 | TERRA_M-T | PARANÃ | TOCANTINS | Brasil | 1716208 | 17 | 33 | nan | nan | nan | Cerrado | 7.8 |
| cea09b9d-c60a-3045-8149-8f5fa2818eca | -11.42185 | -46.91796 | 2025-08-30 12:17:00 | TERRA_M-T | DIANÓPOLIS | TOCANTINS | Brasil | 1707009 | 17 | 33 | nan | nan | nan | Cerrado | 11.1 |
| 19a1593e-c8db-3955-aba8-bfd45139da07 | -11.88204 | -46.46924 | 2025-08-30 12:17:00 | TERRA_M-T | PONTE ALTA DO BOM JESUS | TOCANTINS | Brasil | 1717800 | 17 | 33 | nan | nan | nan | Cerrado | 74.4 |
| 95de8fe2-a319-3f3f-a581-d78011b99c70 | -10.59631 | -46.37191 | 2025-08-30 12:17:00 | TERRA_M-T | MATEIROS | TOCANTINS | Brasil | 1712702 | 17 | 33 | nan | nan | nan | Cerrado | 9.5 |
| 3ee9d1fa-326f-374f-a3ce-04a92893dcbc | -11.14869 | -47.14318 | 2025-08-30 12:17:00 | TERRA_M-T | ALMAS | TOCANTINS | Brasil | 1700400 | 17 | 33 | nan | nan | nan | Cerrado | 7.3 |
| d70bc92b-1ec2-36a5-aef5-ec330023a2fa | -13.51697 | -46.95578 | 2025-08-30 12:17:00 | TERRA_M-T | MONTE ALEGRE DE GOIÁS | GOIÁS | Brasil | 5213509 | 52 | 33 | nan | nan | nan | Cerrado | 11.4 |
| edaf4427-1c23-344c-a0a7-344ef61d559c | -11.8916 | -46.71815 | 2025-08-30 12:17:00 | TERRA_M-T | NOVO JARDIM | TOCANTINS | Brasil | 1715259 | 17 | 33 | nan | nan | nan | Cerrado | 9.4 |
| 52e29fda-e4d4-3dfe-9131-1efa97ba174d | -11.31532 | -43.65907 | 2025-08-30 12:17:00 | TERRA_M-T | BARRA | BAHIA | Brasil | 2902708 | 29 | 33 | nan | nan | nan | Cerrado | 18.4 |
| 0b94443e-1700-3906-8a2d-99ff0eb127dc | -12.70005 | -48.13744 | 2025-08-30 12:17:00 | TERRA_M-T | PARANÃ | TOCANTINS | Brasil | 1716208 | 17 | 33 | nan | nan | nan | Cerrado | 6.4 |
| 9fea8e2e-a097-31be-ae85-124a37c4a8fa | -11.83064 | -46.43708 | 2025-08-30 12:17:00 | TERRA_M-T | PONTE ALTA DO BOM JESUS | TOCANTINS | Brasil | 1717800 | 17 | 33 | nan | nan | nan | Cerrado | 16.7 |
| a90514a7-97ee-3eef-af5a-c4070ebc36b2 | -12.40757 | -46.4714 | 2025-08-30 12:17:00 | TERRA_M-T | TAGUATINGA | TOCANTINS | Brasil | 1720903 | 17 | 33 | nan | nan | nan | Cerrado | 8.8 |
| 4ec3c510-6d72-3e45-b0da-e668cadb5aed | -12.84494 | -48.09555 | 2025-08-30 12:17:00 | TERRA_M-T | PARANÃ | TOCANTINS | Brasil | 1716208 | 17 | 33 | nan | nan | nan | Cerrado | 8.8 |
| 3a79d663-2e83-3b9f-99e4-825e44044675 | -10.01958 | -48.04548 | 2025-08-30 12:17:00 | TERRA_M-T | APARECIDA DO RIO NEGRO | TOCANTINS | Brasil | 1701101 | 17 | 33 | nan | nan | nan | Cerrado | 17.3 |
| 06280f21-d4c1-35dd-8ebd-c6168808927f | -11.22226 | -45.00087 | 2025-08-30 12:17:00 | TERRA_M-T | FORMOSA DO RIO PRETO | BAHIA | Brasil | 2911105 | 29 | 33 | nan | nan | nan | Cerrado | 8.9 |
| a60ba14d-268b-3bb9-8793-0b222fe7ea85 | -12.93415 | -48.11579 | 2025-08-30 12:17:00 | TERRA_M-T | PARANÃ | TOCANTINS | Brasil | 1716208 | 17 | 33 | nan | nan | nan | Cerrado | 15.3 |
| 362a579b-9838-3942-8696-84bcb3458e89 | -17.82638 | -46.36371 | 2025-08-30 12:19:00 | TERRA_M-T | LAGOA GRANDE | MINAS GERAIS | Brasil | 3137536 | 31 | 33 | nan | nan | nan | Cerrado | 5.6 |
| e2a71bc9-5b8b-37a9-be39-0c25429e3473 | -18.25569 | -49.80082 | 2025-08-30 12:19:00 | TERRA_M-T | ITUMBIARA | GOIÁS | Brasil | 5211503 | 52 | 33 | nan | nan | nan | Cerrado | 53.0 |
| ea09263d-9b6e-3081-bded-ba2d6e38f688 | -18.1421 | -44.97586 | 2025-08-30 12:19:00 | TERRA_M-T | TRÊS MARIAS | MINAS GERAIS | Brasil | 3169356 | 31 | 33 | nan | nan | nan | Cerrado | 13.4 |
| adeb37c1-ca7c-3af9-a7dd-dda14476ac58 | -18.25718 | -49.79097 | 2025-08-30 12:19:00 | TERRA_M-T | ITUMBIARA | GOIÁS | Brasil | 5211503 | 52 | 33 | nan | nan | nan | Cerrado | 18.2 |
| dbb3a3d9-e200-3c98-a171-da5a52673434 | -19.78735 | -47.83213 | 2025-08-30 12:19:00 | TERRA_M-T | UBERABA | MINAS GERAIS | Brasil | 3170107 | 31 | 33 | nan | nan | nan | Cerrado | 6.2 |
| 0e057944-ea72-3dcb-93c8-df2db1fd6fe6 | -20.47192 | -46.21582 | 2025-08-30 12:19:00 | TERRA_M-T | PIUMHI | MINAS GERAIS | Brasil | 3151503 | 31 | 33 | nan | nan | nan | Cerrado | 5.7 |
| fa4bec80-5b2b-3ae4-8a00-006be4f1e50a | -18.14064 | -44.98761 | 2025-08-30 12:19:00 | TERRA_M-T | TRÊS MARIAS | MINAS GERAIS | Brasil | 3169356 | 31 | 33 | nan | nan | nan | Cerrado | 20.6 |
| 15362550-fe7a-31b1-a686-c403b1baedd6 | -23.02686 | -51.13824 | 2025-08-30 12:19:00 | TERRA_M-T | SERTANÓPOLIS | PARANÁ | Brasil | 4126504 | 41 | 33 | nan | nan | nan | Mata Atlântica | 6.1 |
| 9a17fc55-5ac0-3e1a-ad12-edc126847ac6 | -21.01213 | -47.28572 | 2025-08-30 12:19:00 | TERRA_M-T | ALTINÓPOLIS | SÃO PAULO | Brasil | 3501004 | 35 | 33 | nan | nan | nan | Cerrado | 14.2 |
| d55f780c-e4b1-3e31-83e8-bb6810459941 | -17.81853 | -46.35234 | 2025-08-30 12:19:00 | TERRA_M-T | LAGOA GRANDE | MINAS GERAIS | Brasil | 3137536 | 31 | 33 | nan | nan | nan | Cerrado | 8.5 |
| 9196665a-0db1-3423-88af-35732a1ecc80 | -20.39004 | -45.9837 | 2025-08-30 12:19:00 | TERRA_M-T | PIUMHI | MINAS GERAIS | Brasil | 3151503 | 31 | 33 | nan | nan | nan | Cerrado | 3.3 |
| df6401c3-8a5f-3683-ad5f-6cd8a5004bd6 | -22.59839 | -46.65578 | 2025-08-30 12:19:00 | TERRA_M-T | SERRA NEGRA | SÃO PAULO | Brasil | 3551603 | 35 | 33 | nan | nan | nan | Mata Atlântica | 5.0 |
| 7517f23a-35ba-3f34-ade3-78732ed01b73 | -17.82774 | -46.35368 | 2025-08-30 12:19:00 | TERRA_M-T | LAGOA GRANDE | MINAS GERAIS | Brasil | 3137536 | 31 | 33 | nan | nan | nan | Cerrado | 28.3 |
| 64b3bbc3-603c-3415-90bf-14db12445708 | -24.82217 | -53.38983 | 2025-08-30 12:19:00 | TERRA_M-T | CASCAVEL | PARANÁ | Brasil | 4104808 | 41 | 33 | nan | nan | nan | Mata Atlântica | 5.5 |
| 7d674b9e-9544-34cb-b909-aab53c5acb53 | -18.26479 | -49.80227 | 2025-08-30 12:19:00 | TERRA_M-T | ITUMBIARA | GOIÁS | Brasil | 5211503 | 52 | 33 | nan | nan | nan | Cerrado | 9.3 |
| 737a8cbd-ee20-3041-8fd5-947f954f689b | -27.37346 | -53.56225 | 2025-08-30 12:19:00 | TERRA_M-T | PALMITINHO | RIO GRANDE DO SUL | Brasil | 4313805 | 43 | 33 | nan | nan | nan | Mata Atlântica | 6.7 |
| 8cd546fe-7b22-370b-b2b1-36cf6f6b9591 | -19.99696 | -44.1034 | 2025-08-30 12:19:00 | TERRA_M-T | IBIRITÉ | MINAS GERAIS | Brasil | 3129806 | 31 | 33 | nan | nan | nan | Mata Atlântica | 4.2 |
| 3edee83a-70c5-3ce8-811d-758cbd35c843 | -21.01347 | -47.27574 | 2025-08-30 12:19:00 | TERRA_M-T | ALTINÓPOLIS | SÃO PAULO | Brasil | 3501004 | 35 | 33 | nan | nan | nan | Cerrado | 6.2 |
| d437121b-2bb6-3624-a428-fdbed09cbed2 | -27.37545 | -53.55014 | 2025-08-30 12:19:00 | TERRA_M-T | PALMITINHO | RIO GRANDE DO SUL | Brasil | 4313805 | 43 | 33 | nan | nan | nan | Mata Atlântica | 9.5 |
| ccc55910-0eb4-31c5-ba24-c2690d33c476 | -17.69086 | -47.28201 | 2025-08-30 12:19:00 | TERRA_M-T | GUARDA-MOR | MINAS GERAIS | Brasil | 3128600 | 31 | 33 | nan | nan | nan | Cerrado | 6.3 |
| 6f59db67-7177-3692-8b8f-90d8492d1420 | -24.82254 | -53.38356 | 2025-08-30 12:19:00 | TERRA_M-T | CORBÉLIA | PARANÁ | Brasil | 4106308 | 41 | 33 | nan | nan | nan | Mata Atlântica | 6.5 |
| 6963a273-c14f-3d49-ae59-2d33d1ae99cf | -11.735 | -51.7406 | 2025-08-30 12:20:00 | GOES-19 | ALTO BOA VISTA | MATO GROSSO | Brasil | 5100359 | 51 | 33 | nan | nan | nan | Amazônia | 110.2 |
| 87721188-181d-31e6-8783-aa94240a4384 | -11.3705 | -43.5868 | 2025-08-30 12:20:00 | GOES-19 | BARRA | BAHIA | Brasil | 2902708 | 29 | 33 | nan | nan | nan | Cerrado | 78.4 |
| 67b6bffc-7cd3-3fc1-88c0-3f1bb1c177bd | -6.1665 | -43.3273 | 2025-08-30 12:20:00 | GOES-19 | LAGOA DO MATO | MARANHÃO | Brasil | 2105922 | 21 | 33 | nan | nan | nan | Cerrado | 338.2 |
| 5e63bd73-44b6-3a3e-90e3-29f39412dc5a | -11.8952 | -46.398 | 2025-08-30 12:20:00 | GOES-19 | PONTE ALTA DO BOM JESUS | TOCANTINS | Brasil | 1717800 | 17 | 33 | nan | nan | nan | Cerrado | 182.8 |
| 03af8603-b2cc-374c-a03f-1946ded8f36a | -11.3125 | -43.6191 | 2025-08-30 12:20:00 | GOES-19 | BARRA | BAHIA | Brasil | 2902708 | 29 | 33 | nan | nan | nan | Cerrado | 102.9 |
| fafd85ad-006a-33f5-a8b4-032cea18ad4e | -12.8605 | -48.1657 | 2025-08-30 12:20:00 | GOES-19 | PARANÃ | TOCANTINS | Brasil | 1716208 | 17 | 33 | nan | nan | nan | Cerrado | 67.7 |
| 9a9527fe-0a16-34dd-a559-25954cbf9946 | -13.3632 | -46.9727 | 2025-08-30 12:20:00 | GOES-19 | MONTE ALEGRE DE GOIÁS | GOIÁS | Brasil | 5213509 | 52 | 33 | nan | nan | nan | Cerrado | 77.6 |
| e6f701c7-88f5-3183-afbd-bc32168c6bbc | -14.0118 | -44.5614 | 2025-08-30 12:20:00 | GOES-19 | COCOS | BAHIA | Brasil | 2908101 | 29 | 33 | nan | nan | nan | Cerrado | 102.2 |
| 297edf43-869f-315f-8659-8cc61f2078cd | -11.3513 | -43.5897 | 2025-08-30 12:20:00 | GOES-19 | BARRA | BAHIA | Brasil | 2902708 | 29 | 33 | nan | nan | nan | Cerrado | 125.7 |
| 0361370a-0ce6-3a7d-896b-91642c6d223f | -6.7814 | -43.7865 | 2025-08-30 12:20:00 | GOES-19 | GUADALUPE | PIAUÍ | Brasil | 2204501 | 22 | 33 | nan | nan | nan | Cerrado | 80.1 |
| 3c1f4c16-0d1a-35bd-93e6-bd4eeaf42709 | -13.3817 | -47.015 | 2025-08-30 12:20:00 | GOES-19 | MONTE ALEGRE DE GOIÁS | GOIÁS | Brasil | 5213509 | 52 | 33 | nan | nan | nan | Cerrado | 102.3 |
| 47e7d554-517b-334a-958a-e20d218a1567 | -11.312 | -43.6428 | 2025-08-30 12:20:00 | GOES-19 | BARRA | BAHIA | Brasil | 2902708 | 29 | 33 | nan | nan | nan | Cerrado | 121.5 |
| 3852689c-13b7-322e-98a6-dd2f351dd2e5 | -6.1787 | -43.9995 | 2025-08-30 12:20:00 | GOES-19 | COLINAS | MARANHÃO | Brasil | 2103505 | 21 | 33 | nan | nan | nan | Cerrado | 94.3 |
| e707d86c-a4dc-36d6-ab2c-0e5bb0111972 | -11.3517 | -43.566 | 2025-08-30 12:20:00 | GOES-19 | BARRA | BAHIA | Brasil | 2902708 | 29 | 33 | nan | nan | nan | Cerrado | 82.6 |
| 720d6b11-f088-3a74-806d-277edf19118b | -6.1663 | -43.3506 | 2025-08-30 12:20:00 | GOES-19 | LAGOA DO MATO | MARANHÃO | Brasil | 2105922 | 21 | 33 | nan | nan | nan | Cerrado | 541.9 |
| 89246baf-7c41-396a-b1ff-9d6eb9ca1e6a | -6.1853 | -43.3257 | 2025-08-30 12:20:00 | GOES-19 | LAGOA DO MATO | MARANHÃO | Brasil | 2105922 | 21 | 33 | nan | nan | nan | Cerrado | 231.4 |
| 7bde6382-2d78-3379-abdf-3f10ac6602d5 | -11.3317 | -43.6162 | 2025-08-30 12:20:00 | GOES-19 | BARRA | BAHIA | Brasil | 2902708 | 29 | 33 | nan | nan | nan | Cerrado | 200.9 |
| 5c32137f-62f8-3ae7-aad4-a4ba9adaa84b | -11.876 | -46.4007 | 2025-08-30 12:20:00 | GOES-19 | PONTE ALTA DO BOM JESUS | TOCANTINS | Brasil | 1717800 | 17 | 33 | nan | nan | nan | Cerrado | 221.8 |
| 2c47bd6a-60f4-34af-a4d5-4a50f5e77423 | -7.8541 | -46.9747 | 2025-08-30 12:20:00 | GOES-19 | CAROLINA | MARANHÃO | Brasil | 2102804 | 21 | 33 | nan | nan | nan | Cerrado | 512.9 |
| d87e48e6-6f9d-343e-87ca-317b20dfae6d | -11.1523 | -54.3104 | 2025-08-30 12:20:00 | GOES-19 | MARCELÂNDIA | MATO GROSSO | Brasil | 5105580 | 51 | 33 | nan | nan | nan | Amazônia | 81.5 |
| 44d371e0-1db7-35b0-9723-4a8eeebfbd56 | -13.3619 | -47.0406 | 2025-08-30 12:20:00 | GOES-19 | MONTE ALEGRE DE GOIÁS | GOIÁS | Brasil | 5213509 | 52 | 33 | nan | nan | nan | Cerrado | 74.8 |
| dc511b06-746f-3aa0-9df2-8e6208cea729 | -13.3812 | -47.0377 | 2025-08-30 12:20:00 | GOES-19 | MONTE ALEGRE DE GOIÁS | GOIÁS | Brasil | 5213509 | 52 | 33 | nan | nan | nan | Cerrado | 132.4 |
| 252a5666-21b2-3f29-b684-8e502c0daab7 | -13.3623 | -47.018 | 2025-08-30 12:20:00 | GOES-19 | MONTE ALEGRE DE GOIÁS | GOIÁS | Brasil | 5213509 | 52 | 33 | nan | nan | nan | Cerrado | 70.1 |
| 55ab1287-b1cc-30e8-9b0b-a11cca82caf5 | -11.8764 | -46.378 | 2025-08-30 12:20:00 | GOES-19 | PONTE ALTA DO BOM JESUS | TOCANTINS | Brasil | 1717800 | 17 | 33 | nan | nan | nan | Cerrado | 573.7 |
| 279ad9b6-0d21-343f-aae9-689a54f2e69e | -6.185 | -43.3491 | 2025-08-30 12:20:00 | GOES-19 | LAGOA DO MATO | MARANHÃO | Brasil | 2105922 | 21 | 33 | nan | nan | nan | Cerrado | 285.7 |
| 7e77a413-c8e2-3242-8b76-89e12219b40c | -11.3312 | -43.6399 | 2025-08-30 12:20:00 | GOES-19 | BARRA | BAHIA | Brasil | 2902708 | 29 | 33 | nan | nan | nan | Cerrado | 235.2 |
| 1b821a5b-e465-344c-a576-dcd067b3bae3 | -13.3628 | -46.9953 | 2025-08-30 12:20:00 | GOES-19 | MONTE ALEGRE DE GOIÁS | GOIÁS | Brasil | 5213509 | 52 | 33 | nan | nan | nan | Cerrado | 72.4 |
| 6f1114b5-e1d0-3776-89ab-bfea86b927ee | -28.72012 | -55.58792 | 2025-08-30 12:21:00 | TERRA_M-T | SÃO BORJA | RIO GRANDE DO SUL | Brasil | 4318002 | 43 | 33 | nan | nan | nan | Pampa | 26.2 |
| 15f182b9-c8a6-3e11-8b73-7a75cf102b0b | -29.28628 | -51.36504 | 2025-08-30 12:21:00 | TERRA_M-T | FARROUPILHA | RIO GRANDE DO SUL | Brasil | 4307906 | 43 | 33 | nan | nan | nan | Mata Atlântica | 4.6 |
| a4215928-d8ec-33cf-9531-d724cdbafdee | -28.72256 | -55.63603 | 2025-08-30 12:21:00 | TERRA_M-T | SÃO BORJA | RIO GRANDE DO SUL | Brasil | 4318002 | 43 | 33 | nan | nan | nan | Pampa | 46.8 |
| 48c8a269-2b8d-376d-89af-49401d9f950f | -28.71975 | -55.65147 | 2025-08-30 12:21:00 | TERRA_M-T | SÃO BORJA | RIO GRANDE DO SUL | Brasil | 4318002 | 43 | 33 | nan | nan | nan | Pampa | 43.0 |
| 8b1d0efc-4085-3346-9dbe-fb537527d650 | -6.185 | -43.3491 | 2025-08-30 12:30:00 | GOES-19 | LAGOA DO MATO | MARANHÃO | Brasil | 2105922 | 21 | 33 | nan | nan | nan | Cerrado | 283.4 |


[Clique aqui para ver as próximas entradas](README98.md)
