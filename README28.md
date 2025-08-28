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

## Dados Diários - Página 28

| ID | Latitude | Longitude | Data/Hora GMT | Satélite | Município | Estado | País | Município ID | Estado ID | País ID | Dias sem Chuva | Precipitação | Risco de Fogo | Bioma | FRP |
|----|----------|-----------|---------------|----------|-----------|--------|------|--------------|-----------|---------|----------------|--------------|----------------|-------|-----|
| aa9efc47-68e4-3250-91a9-61660aa94936 | -12.78846 | -48.16285 | 2025-08-28 03:47:00 | NPP-375D | PARANÃ | TOCANTINS | Brasil | 1716208 | 17 | 33 | nan | nan | nan | Cerrado | 2.0 |
| 2d1c8edf-e07b-3a96-9f05-009f7f60838d | -11.74764 | -49.08789 | 2025-08-28 03:47:00 | NPP-375D | GURUPI | TOCANTINS | Brasil | 1709500 | 17 | 33 | nan | nan | nan | Cerrado | 3.0 |
| 5dbeaf6d-d045-38a8-8569-588cc0bbd7c7 | -11.24414 | -44.97715 | 2025-08-28 03:47:00 | NPP-375D | FORMOSA DO RIO PRETO | BAHIA | Brasil | 2911105 | 29 | 33 | nan | nan | nan | Cerrado | 0.8 |
| b5a37dd2-6c9f-3b21-a623-a3cb3a3206ad | -20.30942 | -46.03284 | 2025-08-28 03:47:00 | NPP-375D | BAMBUÍ | MINAS GERAIS | Brasil | 3105103 | 31 | 33 | nan | nan | nan | Cerrado | 2.6 |
| 2f06b39c-8b72-3f40-a15a-1e1e18f936b5 | -12.40946 | -47.79022 | 2025-08-28 03:47:00 | NPP-375D | PARANÃ | TOCANTINS | Brasil | 1716208 | 17 | 33 | nan | nan | nan | Cerrado | 2.1 |
| 95d47679-8d7a-389e-b237-544308725552 | -12.43115 | -45.96691 | 2025-08-28 03:47:00 | NPP-375D | LUÍS EDUARDO MAGALHÃES | BAHIA | Brasil | 2919553 | 29 | 33 | nan | nan | nan | Cerrado | 5.9 |
| 73d67fd9-4918-3a00-8eba-3e14c67f8d6d | -13.67503 | -46.9068 | 2025-08-28 03:47:00 | NPP-375D | NOVA ROMA | GOIÁS | Brasil | 5214903 | 52 | 33 | nan | nan | nan | Cerrado | 1.0 |
| 0cf6bd4d-9432-3600-83c7-481d6ed464db | -10.70961 | -47.02284 | 2025-08-28 03:47:00 | NPP-375D | PONTE ALTA DO TOCANTINS | TOCANTINS | Brasil | 1717909 | 17 | 33 | nan | nan | nan | Cerrado | 2.6 |
| 863e5cee-b2c8-3c70-8fe4-aa37d85d113c | -16.36889 | -43.78965 | 2025-08-28 03:47:00 | NPP-375D | MONTES CLAROS | MINAS GERAIS | Brasil | 3143302 | 31 | 33 | nan | nan | nan | Cerrado | 4.0 |
| 7ab7d95f-ca18-3139-a404-ea57645fa590 | -21.61193 | -49.703 | 2025-08-28 03:47:00 | NPP-375D | LINS | SÃO PAULO | Brasil | 3527108 | 35 | 33 | nan | nan | nan | Mata Atlântica | 0.7 |
| 9376c604-1b01-3d88-b21f-dfc837fde46c | -9.67953 | -47.06693 | 2025-08-28 03:47:00 | NPP-375D | LIZARDA | TOCANTINS | Brasil | 1712405 | 17 | 33 | nan | nan | nan | Cerrado | 2.9 |
| fc189c75-db5a-3069-b6ca-9a62a8365f63 | -20.135 | -47.37888 | 2025-08-28 03:47:00 | NPP-375D | RIFAINA | SÃO PAULO | Brasil | 3543600 | 35 | 33 | nan | nan | nan | Cerrado | 1.5 |
| d79094f4-91b5-34d2-82d4-58e694f087ff | -13.45318 | -46.85029 | 2025-08-28 03:47:00 | NPP-375D | MONTE ALEGRE DE GOIÁS | GOIÁS | Brasil | 5213509 | 52 | 33 | nan | nan | nan | Cerrado | 1.8 |
| f0b96fa4-b3e6-33c5-9fbf-2c3494edbe51 | -13.67373 | -46.91319 | 2025-08-28 03:47:00 | NPP-375D | NOVA ROMA | GOIÁS | Brasil | 5214903 | 52 | 33 | nan | nan | nan | Cerrado | 1.0 |
| b3fc4df5-c639-36b9-b734-49951e0b3b3e | -21.35603 | -45.25782 | 2025-08-28 03:47:00 | NPP-375D | NEPOMUCENO | MINAS GERAIS | Brasil | 3144607 | 31 | 33 | nan | nan | nan | Mata Atlântica | 1.4 |
| 82dcba9b-b797-3181-a3d7-d2beaae193c1 | -13.98724 | -46.34261 | 2025-08-28 03:47:00 | NPP-375D | GUARANI DE GOIÁS | GOIÁS | Brasil | 5209408 | 52 | 33 | nan | nan | nan | Cerrado | 3.6 |
| a6e50b12-f88d-33ef-8026-cce2dccc6c62 | -13.51807 | -46.87516 | 2025-08-28 03:47:00 | NPP-375D | MONTE ALEGRE DE GOIÁS | GOIÁS | Brasil | 5213509 | 52 | 33 | nan | nan | nan | Cerrado | 2.0 |
| 23cb4cbe-38b3-3d69-8b4c-357027637e6b | -13.44133 | -46.96537 | 2025-08-28 03:47:00 | NPP-375D | MONTE ALEGRE DE GOIÁS | GOIÁS | Brasil | 5213509 | 52 | 33 | nan | nan | nan | Cerrado | 0.9 |
| c1e9c7d7-fa4a-3c4e-990b-45eb8c95290c | -13.61468 | -48.24004 | 2025-08-28 03:47:00 | NPP-375D | MINAÇU | GOIÁS | Brasil | 5213087 | 52 | 33 | nan | nan | nan | Cerrado | 1.6 |
| e281b5ba-44ab-3e21-bd2d-29aa6e3dc382 | -11.243 | -44.98334 | 2025-08-28 03:47:00 | NPP-375D | FORMOSA DO RIO PRETO | BAHIA | Brasil | 2911105 | 29 | 33 | nan | nan | nan | Cerrado | 1.1 |
| d51734bb-6327-387f-9991-2d176a24d5de | -13.43828 | -46.85282 | 2025-08-28 03:47:00 | NPP-375D | MONTE ALEGRE DE GOIÁS | GOIÁS | Brasil | 5213509 | 52 | 33 | nan | nan | nan | Cerrado | 4.9 |
| 84a182a8-01cf-352c-944e-e3a2b3e79899 | -14.23402 | -48.03361 | 2025-08-28 03:47:00 | NPP-375D | NIQUELÂNDIA | GOIÁS | Brasil | 5214606 | 52 | 33 | nan | nan | nan | Cerrado | 0.7 |
| 5ca2e20c-d845-30f8-bbe3-537c5b46a3ba | -11.80003 | -46.78842 | 2025-08-28 03:47:00 | NPP-375D | DIANÓPOLIS | TOCANTINS | Brasil | 1707009 | 17 | 33 | nan | nan | nan | Cerrado | 2.5 |
| 7f2f204b-8838-3f04-ba75-90018a25b2a5 | -11.64582 | -46.38776 | 2025-08-28 03:47:00 | NPP-375D | NOVO JARDIM | TOCANTINS | Brasil | 1715259 | 17 | 33 | nan | nan | nan | Cerrado | 1.1 |
| 26cab99d-aa9a-31c2-85b5-47a068ca8002 | -13.44453 | -46.85069 | 2025-08-28 03:47:00 | NPP-375D | MONTE ALEGRE DE GOIÁS | GOIÁS | Brasil | 5213509 | 52 | 33 | nan | nan | nan | Cerrado | 2.2 |
| ae44ff18-a248-3f45-b90f-864df68b55e8 | -12.80913 | -48.15561 | 2025-08-28 03:47:00 | NPP-375D | PARANÃ | TOCANTINS | Brasil | 1716208 | 17 | 33 | nan | nan | nan | Cerrado | 3.1 |
| 2f124772-0c51-3563-9ede-928ca4d59cc0 | -19.67431 | -49.36592 | 2025-08-28 03:47:00 | NPP-375D | ITAPAGIPE | MINAS GERAIS | Brasil | 3133402 | 31 | 33 | nan | nan | nan | Cerrado | 3.3 |
| 57f5483e-9111-3bd8-81e3-e9c617dbbf79 | -11.32109 | -43.53521 | 2025-08-28 03:47:00 | NPP-375D | BARRA | BAHIA | Brasil | 2902708 | 29 | 33 | nan | nan | nan | Cerrado | 1.4 |
| 08c4de33-9e94-3bbb-8872-1eeed1286326 | -19.54986 | -42.11549 | 2025-08-28 03:49:00 | NPP-375D | INHAPIM | MINAS GERAIS | Brasil | 3130903 | 31 | 33 | nan | nan | nan | Mata Atlântica | 0.6 |
| 70cb047d-2d3b-39fb-9183-2be194e14cdc | -17.90657 | -44.25884 | 2025-08-28 03:49:00 | NPP-375D | BUENÓPOLIS | MINAS GERAIS | Brasil | 3109204 | 31 | 33 | nan | nan | nan | Cerrado | 0.6 |
| c313cd2f-6472-3843-9f79-b29533e2935a | -17.77142 | -44.49207 | 2025-08-28 03:49:00 | NPP-375D | LASSANCE | MINAS GERAIS | Brasil | 3138104 | 31 | 33 | nan | nan | nan | Cerrado | 1.5 |
| 75271c11-3472-3c0e-a553-fb3b20f0aa12 | -18.99513 | -40.29299 | 2025-08-28 03:49:00 | NPP-375D | VILA VALÉRIO | ESPÍRITO SANTO | Brasil | 3205176 | 32 | 33 | nan | nan | nan | Mata Atlântica | 2.2 |
| 0e1f7b0f-f2e7-33d2-a4d3-c828f14fe143 | -19.27925 | -43.74278 | 2025-08-28 03:49:00 | NPP-375D | JABOTICATUBAS | MINAS GERAIS | Brasil | 3134608 | 31 | 33 | nan | nan | nan | Cerrado | 1.5 |
| 5d706880-363c-3884-917e-0ef4ecf0f100 | -18.95326 | -43.83304 | 2025-08-28 03:49:00 | NPP-375D | SANTANA DE PIRAPAMA | MINAS GERAIS | Brasil | 3158508 | 31 | 33 | nan | nan | nan | Cerrado | 1.1 |
| b0df4ba6-1073-394d-a624-c0702a7bd969 | -17.7703 | -44.49786 | 2025-08-28 03:49:00 | NPP-375D | LASSANCE | MINAS GERAIS | Brasil | 3138104 | 31 | 33 | nan | nan | nan | Cerrado | 2.5 |
| dceb2a8d-8283-3fcd-85dc-140df7793a38 | -19.37855 | -44.86108 | 2025-08-28 03:49:00 | NPP-375D | POMPÉU | MINAS GERAIS | Brasil | 3152006 | 31 | 33 | nan | nan | nan | Cerrado | 1.2 |
| 75e11be1-2b26-3b68-8764-39906dcd0d2d | -18.88261 | -43.7234 | 2025-08-28 03:49:00 | NPP-375D | CONGONHAS DO NORTE | MINAS GERAIS | Brasil | 3118106 | 31 | 33 | nan | nan | nan | Cerrado | 0.7 |
| 47d24323-2fd2-3397-ae98-0cdc0f8006ae | -19.88665 | -42.15967 | 2025-08-28 03:49:00 | NPP-375D | SANTA RITA DE MINAS | MINAS GERAIS | Brasil | 3159357 | 31 | 33 | nan | nan | nan | Mata Atlântica | 0.5 |
| 16cb3470-c458-3cef-9f1d-f176103f3a33 | -18.14705 | -44.44514 | 2025-08-28 03:49:00 | NPP-375D | AUGUSTO DE LIMA | MINAS GERAIS | Brasil | 3104809 | 31 | 33 | nan | nan | nan | Cerrado | 2.5 |
| 68346326-b26c-3fb1-94d6-cedcbc5e1437 | -18.07867 | -44.06982 | 2025-08-28 03:49:00 | NPP-375D | AUGUSTO DE LIMA | MINAS GERAIS | Brasil | 3104809 | 31 | 33 | nan | nan | nan | Cerrado | 2.9 |
| a59f4d0a-6712-3cf6-8962-b8b7dce09735 | -19.12099 | -44.02275 | 2025-08-28 03:49:00 | NPP-375D | CORDISBURGO | MINAS GERAIS | Brasil | 3118908 | 31 | 33 | nan | nan | nan | Cerrado | 4.2 |
| 046af3fa-6633-328d-b95b-9fd7c99d9701 | -17.76462 | -44.4795 | 2025-08-28 03:49:00 | NPP-375D | LASSANCE | MINAS GERAIS | Brasil | 3138104 | 31 | 33 | nan | nan | nan | Cerrado | 1.0 |
| a322c5f4-073c-385b-b2ad-7ffa65ecfc1d | -18.12669 | -45.20407 | 2025-08-28 03:49:00 | NPP-375D | TRÊS MARIAS | MINAS GERAIS | Brasil | 3169356 | 31 | 33 | nan | nan | nan | Cerrado | 1.6 |
| aa614bf8-992f-3446-9243-dc27dd863ceb | -17.75916 | -44.48388 | 2025-08-28 03:49:00 | NPP-375D | LASSANCE | MINAS GERAIS | Brasil | 3138104 | 31 | 33 | nan | nan | nan | Cerrado | 6.3 |
| 2b5039c2-7f74-31ca-b329-6a50f9801da8 | -19.17754 | -44.51864 | 2025-08-28 03:49:00 | NPP-375D | PARAOPEBA | MINAS GERAIS | Brasil | 3147402 | 31 | 33 | nan | nan | nan | Cerrado | 1.3 |
| 2170d7c6-d800-3e19-8e4b-1aafbba63cc6 | -19.27776 | -43.74371 | 2025-08-28 03:49:00 | NPP-375D | JABOTICATUBAS | MINAS GERAIS | Brasil | 3134608 | 31 | 33 | nan | nan | nan | Cerrado | 1.5 |
| 505a75d0-a80d-35b0-bafd-f93fd2d69e9e | -17.72563 | -45.52958 | 2025-08-28 03:49:00 | NPP-375D | JOÃO PINHEIRO | MINAS GERAIS | Brasil | 3136306 | 31 | 33 | nan | nan | nan | Cerrado | 1.3 |
| 0251a3b7-9ca8-3b49-99b4-e09f7ee39f2d | -17.73665 | -42.67946 | 2025-08-28 03:49:00 | NPP-375D | ITAMARANDIBA | MINAS GERAIS | Brasil | 3132503 | 31 | 33 | nan | nan | nan | Mata Atlântica | 1.7 |
| 351250fe-0282-39e7-84fe-34df3d486df9 | -18.08066 | -44.05935 | 2025-08-28 03:49:00 | NPP-375D | AUGUSTO DE LIMA | MINAS GERAIS | Brasil | 3104809 | 31 | 33 | nan | nan | nan | Cerrado | 0.9 |
| a5cc3be1-4645-398b-9541-95277cd52319 | -18.17882 | -45.55812 | 2025-08-28 03:49:00 | NPP-375D | SÃO GONÇALO DO ABAETÉ | MINAS GERAIS | Brasil | 3161700 | 31 | 33 | nan | nan | nan | Cerrado | 1.0 |
| 26b36f1f-59a1-3386-af3f-8256c0a64f53 | -17.9673 | -43.98983 | 2025-08-28 03:49:00 | NPP-375D | BUENÓPOLIS | MINAS GERAIS | Brasil | 3109204 | 31 | 33 | nan | nan | nan | Cerrado | 0.7 |
| 57384201-5db4-3ae0-9f60-3048a9d9d1c1 | -19.45672 | -44.31297 | 2025-08-28 03:49:00 | NPP-375D | SETE LAGOAS | MINAS GERAIS | Brasil | 3167202 | 31 | 33 | nan | nan | nan | Cerrado | 0.8 |
| b28e4ffc-ea98-39cc-9b31-e2f03786b01c | -17.81368 | -44.51237 | 2025-08-28 03:49:00 | NPP-375D | LASSANCE | MINAS GERAIS | Brasil | 3138104 | 31 | 33 | nan | nan | nan | Cerrado | 3.5 |
| de4a247b-8c9c-3d3b-b6b6-56cc055d9c95 | -19.25142 | -42.04856 | 2025-08-28 03:49:00 | NPP-375D | TARUMIRIM | MINAS GERAIS | Brasil | 3168408 | 31 | 33 | nan | nan | nan | Mata Atlântica | 4.2 |
| 1fc0b847-0457-359c-9d5f-e5869d8cd177 | -19.11203 | -44.02623 | 2025-08-28 03:49:00 | NPP-375D | JEQUITIBÁ | MINAS GERAIS | Brasil | 3135704 | 31 | 33 | nan | nan | nan | Cerrado | 3.4 |
| 9597003b-eaec-3e4f-9af0-e3b290aaea7b | -17.73039 | -45.53052 | 2025-08-28 03:49:00 | NPP-375D | JOÃO PINHEIRO | MINAS GERAIS | Brasil | 3136306 | 31 | 33 | nan | nan | nan | Cerrado | 1.0 |
| 290d6b98-15e5-3b00-85e3-3362efebe286 | -17.55218 | -46.62877 | 2025-08-28 03:49:00 | NPP-375D | VAZANTE | MINAS GERAIS | Brasil | 3171006 | 31 | 33 | nan | nan | nan | Cerrado | 1.2 |
| db883f79-cddb-374c-a2d8-1c537befb604 | -19.22794 | -44.44361 | 2025-08-28 03:49:00 | NPP-375D | PARAOPEBA | MINAS GERAIS | Brasil | 3147402 | 31 | 33 | nan | nan | nan | Cerrado | 0.6 |
| 275f53d6-08ca-333d-9509-11d66ab71fd7 | -18.37027 | -49.27095 | 2025-08-28 03:49:00 | NPP-375D | ITUMBIARA | GOIÁS | Brasil | 5211503 | 52 | 33 | nan | nan | nan | Cerrado | 1.2 |
| 08913be9-6214-3226-8c66-c809bc2dee25 | -18.88475 | -43.71214 | 2025-08-28 03:49:00 | NPP-375D | CONGONHAS DO NORTE | MINAS GERAIS | Brasil | 3118106 | 31 | 33 | nan | nan | nan | Cerrado | 1.0 |
| a125ef53-24ef-3f5e-9fc6-43ee2b08aaa5 | -19.06853 | -42.1392 | 2025-08-28 03:49:00 | NPP-375D | FERNANDES TOURINHO | MINAS GERAIS | Brasil | 3125804 | 31 | 33 | nan | nan | nan | Mata Atlântica | 1.6 |
| 36ec7962-dfa6-38c4-91b5-ec362a7d8c14 | -19.24763 | -42.0481 | 2025-08-28 03:49:00 | NPP-375D | ENGENHEIRO CALDAS | MINAS GERAIS | Brasil | 3123700 | 31 | 33 | nan | nan | nan | Mata Atlântica | 4.2 |
| 66f7858d-a384-3149-8e5a-e40139326396 | -17.73769 | -42.68176 | 2025-08-28 03:49:00 | NPP-375D | ITAMARANDIBA | MINAS GERAIS | Brasil | 3132503 | 31 | 33 | nan | nan | nan | Mata Atlântica | 2.8 |
| d1ca3dc3-d816-3788-b730-d4df7fadada3 | -17.54707 | -46.62763 | 2025-08-28 03:49:00 | NPP-375D | VAZANTE | MINAS GERAIS | Brasil | 3171006 | 31 | 33 | nan | nan | nan | Cerrado | 1.2 |
| f92ad8b7-4a24-321d-914f-281ac518b62a | -17.91608 | -45.90743 | 2025-08-28 03:49:00 | NPP-375D | JOÃO PINHEIRO | MINAS GERAIS | Brasil | 3136306 | 31 | 33 | nan | nan | nan | Cerrado | 1.5 |
| ab211ed4-98c8-393c-9548-7490aec6ad73 | -19.37326 | -44.86472 | 2025-08-28 03:49:00 | NPP-375D | POMPÉU | MINAS GERAIS | Brasil | 3152006 | 31 | 33 | nan | nan | nan | Cerrado | 1.0 |
| c57bc0fe-56ec-3621-90f6-593b5294fc99 | -18.07966 | -44.06462 | 2025-08-28 03:49:00 | NPP-375D | AUGUSTO DE LIMA | MINAS GERAIS | Brasil | 3104809 | 31 | 33 | nan | nan | nan | Cerrado | 2.9 |
| 46304f94-112d-3cb8-8727-5f38005ef5f8 | -19.11601 | -44.02589 | 2025-08-28 03:49:00 | NPP-375D | JEQUITIBÁ | MINAS GERAIS | Brasil | 3135704 | 31 | 33 | nan | nan | nan | Cerrado | 4.2 |
| facc871a-fcb0-3442-b109-4bf050471c13 | -17.55282 | -46.62563 | 2025-08-28 03:49:00 | NPP-375D | VAZANTE | MINAS GERAIS | Brasil | 3171006 | 31 | 33 | nan | nan | nan | Cerrado | 1.2 |
| bb95adbb-7ca9-362a-b3bc-b2c40f804034 | -17.55031 | -46.61192 | 2025-08-28 03:49:00 | NPP-375D | VAZANTE | MINAS GERAIS | Brasil | 3171006 | 31 | 33 | nan | nan | nan | Cerrado | 0.8 |
| 5f3abd21-11e5-38db-96ce-75c9ccb2f434 | -19.11699 | -44.02309 | 2025-08-28 03:49:00 | NPP-375D | JEQUITIBÁ | MINAS GERAIS | Brasil | 3135704 | 31 | 33 | nan | nan | nan | Cerrado | 3.4 |
| 0d8530c4-fbd4-3560-a586-066a39f0998b | -18.99166 | -40.29234 | 2025-08-28 03:49:00 | NPP-375D | VILA VALÉRIO | ESPÍRITO SANTO | Brasil | 3205176 | 32 | 33 | nan | nan | nan | Mata Atlântica | 1.1 |
| 5b89d315-70d4-3a04-a2b1-90195d7cdfd6 | -19.62077 | -42.77047 | 2025-08-28 03:49:00 | NPP-375D | JAGUARAÇU | MINAS GERAIS | Brasil | 3135001 | 31 | 33 | nan | nan | nan | Mata Atlântica | 0.9 |
| e65809bf-da42-3013-9a9d-6a546c97e670 | -19.16256 | -41.8304 | 2025-08-28 03:49:00 | NPP-375D | ITANHOMI | MINAS GERAIS | Brasil | 3133204 | 31 | 33 | nan | nan | nan | Mata Atlântica | 0.9 |
| 133677d6-7d41-352c-8a66-c7186919da09 | -19.47011 | -42.62543 | 2025-08-28 03:49:00 | NPP-375D | CORONEL FABRICIANO | MINAS GERAIS | Brasil | 3119401 | 31 | 33 | nan | nan | nan | Mata Atlântica | 1.5 |
| ba9dfd78-c3c3-37d7-b40b-d65fbee66a7e | -17.77637 | -48.50292 | 2025-08-28 03:49:00 | NPP-375D | IPAMERI | GOIÁS | Brasil | 5210109 | 52 | 33 | nan | nan | nan | Cerrado | 2.2 |
| 23a41b95-3e6d-34e0-bb23-b8e63631d7ad | -17.81975 | -44.51574 | 2025-08-28 03:49:00 | NPP-375D | LASSANCE | MINAS GERAIS | Brasil | 3138104 | 31 | 33 | nan | nan | nan | Cerrado | 2.2 |
| 66b3e5f8-e89b-3044-86c8-e8efc98e74c0 | -16.64944 | -46.72423 | 2025-08-28 03:49:00 | NPP-375D | UNAÍ | MINAS GERAIS | Brasil | 3170404 | 31 | 33 | nan | nan | nan | Cerrado | 2.3 |
| 43833f7e-3d86-36f0-b6fd-1da956afa434 | -17.54966 | -46.61506 | 2025-08-28 03:49:00 | NPP-375D | VAZANTE | MINAS GERAIS | Brasil | 3171006 | 31 | 33 | nan | nan | nan | Cerrado | 0.8 |
| e23bad86-b998-3404-a006-1b1781066743 | -17.55095 | -46.60879 | 2025-08-28 03:49:00 | NPP-375D | VAZANTE | MINAS GERAIS | Brasil | 3171006 | 31 | 33 | nan | nan | nan | Cerrado | 1.2 |
| c92411b5-2a29-30aa-9ae9-901d62f4fa29 | -18.0754 | -44.06355 | 2025-08-28 03:49:00 | NPP-375D | AUGUSTO DE LIMA | MINAS GERAIS | Brasil | 3104809 | 31 | 33 | nan | nan | nan | Cerrado | 2.9 |
| a05e625b-7dc0-34db-8b4a-155a251ef073 | -18.21194 | -45.56454 | 2025-08-28 03:49:00 | NPP-375D | SÃO GONÇALO DO ABAETÉ | MINAS GERAIS | Brasil | 3161700 | 31 | 33 | nan | nan | nan | Cerrado | 1.2 |
| f45ae006-026e-35ce-8983-5ed7e23a423a | -17.77543 | -48.50439 | 2025-08-28 03:49:00 | NPP-375D | IPAMERI | GOIÁS | Brasil | 5210109 | 52 | 33 | nan | nan | nan | Cerrado | 2.4 |
| 60411003-4096-3809-94c8-60860cd277ad | -19.11623 | -44.02717 | 2025-08-28 03:49:00 | NPP-375D | CORDISBURGO | MINAS GERAIS | Brasil | 3118908 | 31 | 33 | nan | nan | nan | Cerrado | 3.4 |
| 982fb594-fbbc-34c4-9e17-09b81d99d082 | -18.21779 | -44.52394 | 2025-08-28 03:49:00 | NPP-375D | CORINTO | MINAS GERAIS | Brasil | 3119104 | 31 | 33 | nan | nan | nan | Cerrado | 1.0 |
| d8ab32af-eeda-3611-b56e-034cc45d5fca | -17.74063 | -42.68015 | 2025-08-28 03:49:00 | NPP-375D | ITAMARANDIBA | MINAS GERAIS | Brasil | 3132503 | 31 | 33 | nan | nan | nan | Mata Atlântica | 1.0 |
| c91e575b-64cd-37c6-8171-cc8a883f011e | -18.13992 | -44.4586 | 2025-08-28 03:49:00 | NPP-375D | CORINTO | MINAS GERAIS | Brasil | 3119104 | 31 | 33 | nan | nan | nan | Cerrado | 1.7 |
| 98a9833a-0619-33c0-9d27-85a17b88ca8a | -19.11681 | -44.02181 | 2025-08-28 03:49:00 | NPP-375D | JEQUITIBÁ | MINAS GERAIS | Brasil | 3135704 | 31 | 33 | nan | nan | nan | Cerrado | 4.2 |
| 6bdec06e-cd3e-35b7-8aa5-064177754d52 | -18.19498 | -45.22332 | 2025-08-28 03:49:00 | NPP-375D | TRÊS MARIAS | MINAS GERAIS | Brasil | 3169356 | 31 | 33 | nan | nan | nan | Cerrado | 1.2 |
| 290462c5-1c30-365b-8e86-c6f59a1bb6a8 | -19.15882 | -41.82988 | 2025-08-28 03:49:00 | NPP-375D | ITANHOMI | MINAS GERAIS | Brasil | 3133204 | 31 | 33 | nan | nan | nan | Mata Atlântica | 1.4 |
| 2b8dde22-5ec7-31a3-a12b-837b3efd946f | -17.81812 | -44.51331 | 2025-08-28 03:49:00 | NPP-375D | LASSANCE | MINAS GERAIS | Brasil | 3138104 | 31 | 33 | nan | nan | nan | Cerrado | 1.9 |
| c9d97a58-80ce-3aee-8fc1-217fa6a1d970 | -18.88189 | -43.72718 | 2025-08-28 03:49:00 | NPP-375D | CONGONHAS DO NORTE | MINAS GERAIS | Brasil | 3118106 | 31 | 33 | nan | nan | nan | Cerrado | 1.1 |
| 1d3097aa-24b4-3f69-8895-ed5a372a6502 | -17.81532 | -44.5148 | 2025-08-28 03:49:00 | NPP-375D | LASSANCE | MINAS GERAIS | Brasil | 3138104 | 31 | 33 | nan | nan | nan | Cerrado | 2.2 |
| 7f5ffd72-e719-3080-b37b-5ab04541ced9 | -17.77734 | -48.49845 | 2025-08-28 03:49:00 | NPP-375D | IPAMERI | GOIÁS | Brasil | 5210109 | 52 | 33 | nan | nan | nan | Cerrado | 2.2 |
| 58a57a7f-6048-37a9-a07c-69850027b2cc | -18.37375 | -49.2731 | 2025-08-28 03:49:00 | NPP-375D | ITUMBIARA | GOIÁS | Brasil | 5211503 | 52 | 33 | nan | nan | nan | Cerrado | 1.3 |
| 4afe9422-aa0c-392b-8e24-e038dfa6de72 | -19.11262 | -44.02084 | 2025-08-28 03:49:00 | NPP-375D | JEQUITIBÁ | MINAS GERAIS | Brasil | 3135704 | 31 | 33 | nan | nan | nan | Cerrado | 1.7 |
| 6bec19e6-49be-3635-bb42-52fb3b5f66e4 | -19.27522 | -45.12936 | 2025-08-28 03:49:00 | NPP-375D | MARTINHO CAMPOS | MINAS GERAIS | Brasil | 3140506 | 31 | 33 | nan | nan | nan | Cerrado | 1.3 |
| 4f0b902d-dde3-3ed1-a3e1-a762cdf9994b | -18.14546 | -43.09106 | 2025-08-28 03:49:00 | NPP-375D | RIO VERMELHO | MINAS GERAIS | Brasil | 3156007 | 31 | 33 | nan | nan | nan | Mata Atlântica | 0.4 |
| 6d02bd54-ea1a-3ea9-8b17-409bba85a779 | -17.75817 | -44.48899 | 2025-08-28 03:49:00 | NPP-375D | LASSANCE | MINAS GERAIS | Brasil | 3138104 | 31 | 33 | nan | nan | nan | Cerrado | 6.3 |
| e26a1bd0-ef74-3d83-b309-540cffa0e3e4 | -17.7571 | -44.49447 | 2025-08-28 03:49:00 | NPP-375D | LASSANCE | MINAS GERAIS | Brasil | 3138104 | 31 | 33 | nan | nan | nan | Cerrado | 12.6 |


[Clique aqui para ver as próximas entradas](README29.md)
