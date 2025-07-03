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
| aa102446-686f-3ee6-9f47-2a876de2a512 | -11.14456 | -43.32827 | 2025-07-03 04:36:00 | NPP-375D | BARRA | BAHIA | Brasil | 2902708 | 29 | 33 | nan | nan | nan | Caatinga | 8.4 |
| 81ebe0bb-4f94-3649-9373-a6d52222683e | -11.53724 | -47.30973 | 2025-07-03 04:36:00 | NPP-375D | ALMAS | TOCANTINS | Brasil | 1700400 | 17 | 33 | nan | nan | nan | Cerrado | 1.9 |
| 5c4c2593-2c17-388b-9f37-e45a8ebfe01d | -10.29857 | -57.13415 | 2025-07-03 04:36:00 | NPP-375D | NOVA MONTE VERDE | MATO GROSSO | Brasil | 5108956 | 51 | 33 | nan | nan | nan | Amazônia | 0.8 |
| d0d776bf-234c-3cf1-94f3-57b5c21107b5 | -12.16442 | -45.53238 | 2025-07-03 04:36:00 | NPP-375D | BARREIRAS | BAHIA | Brasil | 2903201 | 29 | 33 | nan | nan | nan | Cerrado | 2.1 |
| 101e38ef-b04e-3d51-9d4e-e6ac31210a02 | -10.93036 | -47.24031 | 2025-07-03 04:36:00 | NPP-375D | PONTE ALTA DO TOCANTINS | TOCANTINS | Brasil | 1717909 | 17 | 33 | nan | nan | nan | Cerrado | 0.7 |
| 7f122f32-a2cb-3bff-827d-7b3320a27daa | -10.08622 | -52.74209 | 2025-07-03 04:36:00 | NPP-375D | SANTA CRUZ DO XINGU | MATO GROSSO | Brasil | 5107743 | 51 | 33 | nan | nan | nan | Amazônia | 1.1 |
| e5959a04-928a-3433-bec9-64ddf597c884 | -10.37802 | -49.88947 | 2025-07-03 04:36:00 | NPP-375D | PIUM | TOCANTINS | Brasil | 1717503 | 17 | 33 | nan | nan | nan | Cerrado | 0.9 |
| 43bcc9ed-1c8c-3bf7-a0f5-a48bc19b5168 | -11.85817 | -44.85081 | 2025-07-03 04:36:00 | NPP-375D | RIACHÃO DAS NEVES | BAHIA | Brasil | 2926202 | 29 | 33 | nan | nan | nan | Cerrado | 1.4 |
| 3105db43-5e79-3b29-82aa-ddf50cf248f9 | -10.08896 | -47.99332 | 2025-07-03 04:36:00 | NPP-375D | APARECIDA DO RIO NEGRO | TOCANTINS | Brasil | 1701101 | 17 | 33 | nan | nan | nan | Cerrado | 2.1 |
| d9705704-b9f5-3377-aa92-afb9324f6639 | -11.84201 | -47.55291 | 2025-07-03 04:36:00 | NPP-375D | NATIVIDADE | TOCANTINS | Brasil | 1714203 | 17 | 33 | nan | nan | nan | Cerrado | 1.3 |
| 5a29024e-a2c7-3b39-905d-aaff00d820ae | -11.54123 | -47.30652 | 2025-07-03 04:36:00 | NPP-375D | ALMAS | TOCANTINS | Brasil | 1700400 | 17 | 33 | nan | nan | nan | Cerrado | 1.9 |
| 41d03e2e-8d72-38e7-803f-a217b0ed3b42 | -10.66456 | -49.45087 | 2025-07-03 04:36:00 | NPP-375D | CRISTALÂNDIA | TOCANTINS | Brasil | 1706100 | 17 | 33 | nan | nan | nan | Cerrado | 1.1 |
| b245626e-fa5c-30ca-96e4-f801c15228a6 | -9.79503 | -47.75128 | 2025-07-03 04:36:00 | NPP-375D | RIO SONO | TOCANTINS | Brasil | 1718758 | 17 | 33 | nan | nan | nan | Cerrado | 1.6 |
| 5ae00e60-95f5-3663-88d9-e45a3907486b | -11.66302 | -44.59836 | 2025-07-03 04:36:00 | NPP-375D | COTEGIPE | BAHIA | Brasil | 2909406 | 29 | 33 | nan | nan | nan | Cerrado | 12.3 |
| 448c0f11-7126-39cd-a0fa-ee3bd6e15490 | -11.79576 | -48.08242 | 2025-07-03 04:36:00 | NPP-375D | SÃO VALÉRIO | TOCANTINS | Brasil | 1720499 | 17 | 33 | nan | nan | nan | Cerrado | 0.8 |
| cb9b8c8e-1b59-3f5e-ac4b-0b4e090154df | -11.63932 | -48.0725 | 2025-07-03 04:36:00 | NPP-375D | CHAPADA DA NATIVIDADE | TOCANTINS | Brasil | 1705102 | 17 | 33 | nan | nan | nan | Cerrado | 4.4 |
| 977eab0f-0ddd-3dfc-820b-8cff45c00e3f | -10.30358 | -57.13517 | 2025-07-03 04:36:00 | NPP-375D | NOVA MONTE VERDE | MATO GROSSO | Brasil | 5108956 | 51 | 33 | nan | nan | nan | Amazônia | 0.8 |
| 4a4821b9-7d94-3ea7-8634-ac0421c92eff | -12.55098 | -43.9545 | 2025-07-03 04:36:00 | NPP-375D | BREJOLÂNDIA | BAHIA | Brasil | 2904407 | 29 | 33 | nan | nan | nan | Cerrado | 1.2 |
| 7694b9cc-c127-3f0c-abdf-c4c843243825 | -10.08562 | -47.99279 | 2025-07-03 04:36:00 | NPP-375D | APARECIDA DO RIO NEGRO | TOCANTINS | Brasil | 1701101 | 17 | 33 | nan | nan | nan | Cerrado | 2.1 |
| 0abb50f8-92c2-3ed5-8311-0fe1c0cec720 | -10.08617 | -47.98925 | 2025-07-03 04:36:00 | NPP-375D | APARECIDA DO RIO NEGRO | TOCANTINS | Brasil | 1701101 | 17 | 33 | nan | nan | nan | Cerrado | 2.8 |
| 2ad11808-9469-33ed-9bc1-8bd5bc8d3b1b | -10.95946 | -48.22485 | 2025-07-03 04:36:00 | NPP-375D | MONTE DO CARMO | TOCANTINS | Brasil | 1713601 | 17 | 33 | nan | nan | nan | Cerrado | 0.7 |
| 1862d599-5816-3be3-b9ea-a5cbca121a80 | -9.81076 | -48.38888 | 2025-07-03 04:36:00 | NPP-375D | MIRACEMA DO TOCANTINS | TOCANTINS | Brasil | 1713205 | 17 | 33 | nan | nan | nan | Cerrado | 0.9 |
| 185d60c4-c8e8-36e9-8c9c-59d20a6ff64c | -11.65412 | -44.57676 | 2025-07-03 04:36:00 | NPP-375D | COTEGIPE | BAHIA | Brasil | 2909406 | 29 | 33 | nan | nan | nan | Cerrado | 1.7 |
| 6f4a748c-fa37-3bff-b85c-d5e6003738bd | -11.14404 | -43.33215 | 2025-07-03 04:36:00 | NPP-375D | BARRA | BAHIA | Brasil | 2902708 | 29 | 33 | nan | nan | nan | Caatinga | 8.4 |
| 49cd0f27-c4c1-33b4-a8d7-d1b855405e3a | -9.87354 | -48.45965 | 2025-07-03 04:36:00 | NPP-375D | MIRACEMA DO TOCANTINS | TOCANTINS | Brasil | 1713205 | 17 | 33 | nan | nan | nan | Cerrado | 0.9 |
| b902df46-de17-36f5-9c3e-b87fa1d58daa | -9.83012 | -48.37402 | 2025-07-03 04:36:00 | NPP-375D | MIRACEMA DO TOCANTINS | TOCANTINS | Brasil | 1713205 | 17 | 33 | nan | nan | nan | Cerrado | 1.3 |
| e4183049-aaf2-3e47-b359-0f3bb4919ceb | -10.67795 | -49.4892 | 2025-07-03 04:36:00 | NPP-375D | CRISTALÂNDIA | TOCANTINS | Brasil | 1706100 | 17 | 33 | nan | nan | nan | Cerrado | 0.7 |
| b772719d-7c14-3124-a7d9-678ca915924c | -10.99323 | -45.19592 | 2025-07-03 04:36:00 | NPP-375D | FORMOSA DO RIO PRETO | BAHIA | Brasil | 2911105 | 29 | 33 | nan | nan | nan | Cerrado | 2.8 |
| 0a569395-2beb-35d9-9932-f0287479e4b1 | -11.14508 | -43.32438 | 2025-07-03 04:36:00 | NPP-375D | BARRA | BAHIA | Brasil | 2902708 | 29 | 33 | nan | nan | nan | Caatinga | 4.8 |
| 492e9ae2-02dd-30dc-a908-4780ffba258d | -11.54657 | -47.31422 | 2025-07-03 04:36:00 | NPP-375D | ALMAS | TOCANTINS | Brasil | 1700400 | 17 | 33 | nan | nan | nan | Cerrado | 1.6 |
| 3966d4f5-6018-3f51-babf-235b46611ce6 | -11.14019 | -43.32488 | 2025-07-03 04:36:00 | NPP-375D | BARRA | BAHIA | Brasil | 2902708 | 29 | 33 | nan | nan | nan | Caatinga | 7.0 |
| 0ea972f2-f04f-33fa-9b42-274c2e1da146 | -11.14438 | -43.3255 | 2025-07-03 04:36:00 | NPP-375D | BARRA | BAHIA | Brasil | 2902708 | 29 | 33 | nan | nan | nan | Caatinga | 7.0 |
| b596079d-9eb2-31a4-a7dd-74e0354d4133 | -11.83805 | -47.55608 | 2025-07-03 04:36:00 | NPP-375D | NATIVIDADE | TOCANTINS | Brasil | 1714203 | 17 | 33 | nan | nan | nan | Cerrado | 2.3 |
| 42a646cf-9caf-315f-90e5-cfb36e533b70 | -9.8113 | -48.03635 | 2025-07-03 04:36:00 | NPP-375D | TOCANTÍNIA | TOCANTINS | Brasil | 1721109 | 17 | 33 | nan | nan | nan | Cerrado | 0.7 |
| fe67a4a6-476d-3627-917c-c0a9131c648d | -9.70471 | -56.18239 | 2025-07-03 04:36:00 | NPP-375D | ALTA FLORESTA | MATO GROSSO | Brasil | 5100250 | 51 | 33 | nan | nan | nan | Amazônia | 1.3 |
| 2000c941-1044-3a67-909b-655d4e71225c | -11.31439 | -46.21096 | 2025-07-03 04:36:00 | NPP-375D | FORMOSA DO RIO PRETO | BAHIA | Brasil | 2911105 | 29 | 33 | nan | nan | nan | Cerrado | 0.9 |
| fba118b3-b126-3afa-8640-0c20dc1adad6 | -9.87686 | -48.46018 | 2025-07-03 04:36:00 | NPP-375D | MIRACEMA DO TOCANTINS | TOCANTINS | Brasil | 1713205 | 17 | 33 | nan | nan | nan | Cerrado | 0.7 |
| aa633f28-ddfa-3a89-a903-e986ad909aaa | -10.29804 | -57.13705 | 2025-07-03 04:36:00 | NPP-375D | NOVA MONTE VERDE | MATO GROSSO | Brasil | 5108956 | 51 | 33 | nan | nan | nan | Amazônia | 0.8 |
| 62bb77e6-c572-34eb-80b3-1de679138d74 | -11.50076 | -48.9581 | 2025-07-03 04:36:00 | NPP-375D | ALIANÇA DO TOCANTINS | TOCANTINS | Brasil | 1700350 | 17 | 33 | nan | nan | nan | Cerrado | 2.7 |
| d7f9b5de-6ccb-38f9-acef-78ab0c6d0100 | -11.63485 | -48.07913 | 2025-07-03 04:36:00 | NPP-375D | CHAPADA DA NATIVIDADE | TOCANTINS | Brasil | 1705102 | 17 | 33 | nan | nan | nan | Cerrado | 4.6 |
| ded94b90-00cc-316b-9cbd-1d12c35699da | -11.54371 | -47.30996 | 2025-07-03 04:36:00 | NPP-375D | ALMAS | TOCANTINS | Brasil | 1700400 | 17 | 33 | nan | nan | nan | Cerrado | 2.3 |
| 2a93e68f-2473-35bc-8dd8-016e059cd09c | -10.12786 | -58.21675 | 2025-07-03 04:36:00 | NPP-375D | NOVA BANDEIRANTES | MATO GROSSO | Brasil | 5106158 | 51 | 33 | nan | nan | nan | Amazônia | 0.9 |
| 1d70f1bb-d971-3b16-b7dd-7f9ef532ea79 | -11.5403 | -47.30944 | 2025-07-03 04:36:00 | NPP-375D | ALMAS | TOCANTINS | Brasil | 1700400 | 17 | 33 | nan | nan | nan | Cerrado | 2.3 |
| 177fd4e5-6008-3a21-932a-a1d983bb8a16 | -11.65133 | -44.59663 | 2025-07-03 04:36:00 | NPP-375D | COTEGIPE | BAHIA | Brasil | 2909406 | 29 | 33 | nan | nan | nan | Cerrado | 25.8 |
| 4229af8e-08fb-3da7-93f5-0ca5dc296485 | -11.59278 | -44.6408 | 2025-07-03 04:36:00 | NPP-375D | COTEGIPE | BAHIA | Brasil | 2909406 | 29 | 33 | nan | nan | nan | Cerrado | 0.8 |
| 717625ba-4f56-3643-9bbf-75a0691e94a4 | -10.65052 | -44.48554 | 2025-07-03 04:36:00 | NPP-375D | SANTA RITA DE CÁSSIA | BAHIA | Brasil | 2928406 | 29 | 33 | nan | nan | nan | Cerrado | 9.9 |
| c296f121-490a-32af-bbaa-49861e508d50 | -11.14328 | -43.33325 | 2025-07-03 04:36:00 | NPP-375D | BARRA | BAHIA | Brasil | 2902708 | 29 | 33 | nan | nan | nan | Caatinga | 9.0 |
| 81123594-b359-391b-86cd-73de00eb8f88 | -11.50131 | -48.95458 | 2025-07-03 04:36:00 | NPP-375D | ALIANÇA DO TOCANTINS | TOCANTINS | Brasil | 1700350 | 17 | 33 | nan | nan | nan | Cerrado | 2.7 |
| 3ba8e55c-ba59-3d41-bfbf-9f6991376a3e | -11.54066 | -47.31026 | 2025-07-03 04:36:00 | NPP-375D | ALMAS | TOCANTINS | Brasil | 1700400 | 17 | 33 | nan | nan | nan | Cerrado | 1.9 |
| 25d14252-fd5a-379b-b70d-f1cd0054793b | -10.9285 | -49.27709 | 2025-07-03 04:36:00 | NPP-375D | SANTA RITA DO TOCANTINS | TOCANTINS | Brasil | 1718899 | 17 | 33 | nan | nan | nan | Cerrado | 1.4 |
| d982e0e1-a45c-34e8-b058-f2f2e118d6b2 | -10.99654 | -45.19423 | 2025-07-03 04:36:00 | NPP-375D | FORMOSA DO RIO PRETO | BAHIA | Brasil | 2911105 | 29 | 33 | nan | nan | nan | Cerrado | 2.2 |
| 908d8ba5-c258-38bb-a4cb-9bdc2e6f5f9b | -10.99215 | -45.19815 | 2025-07-03 04:36:00 | NPP-375D | FORMOSA DO RIO PRETO | BAHIA | Brasil | 2911105 | 29 | 33 | nan | nan | nan | Cerrado | 2.2 |
| f3958c97-62de-3ea9-9a8a-fc0c18c7533f | -10.66066 | -49.45387 | 2025-07-03 04:36:00 | NPP-375D | CRISTALÂNDIA | TOCANTINS | Brasil | 1706100 | 17 | 33 | nan | nan | nan | Cerrado | 1.5 |
| ad708f88-a6dd-3815-be41-086e3d2fa18a | -11.66122 | -44.58288 | 2025-07-03 04:36:00 | NPP-375D | COTEGIPE | BAHIA | Brasil | 2909406 | 29 | 33 | nan | nan | nan | Cerrado | 1.3 |
| db189687-ace6-3a2a-8fbb-347d6825a757 | -10.99696 | -45.19646 | 2025-07-03 04:36:00 | NPP-375D | FORMOSA DO RIO PRETO | BAHIA | Brasil | 2911105 | 29 | 33 | nan | nan | nan | Cerrado | 2.8 |
| ae4ba28b-0438-315f-964f-5cfe80d815d7 | -10.30806 | -57.13912 | 2025-07-03 04:36:00 | NPP-375D | NOVA MONTE VERDE | MATO GROSSO | Brasil | 5108956 | 51 | 33 | nan | nan | nan | Amazônia | 0.4 |
| ee22b3c6-b9ab-38f9-a9b6-b80adb541696 | -10.68128 | -49.48975 | 2025-07-03 04:36:00 | NPP-375D | CRISTALÂNDIA | TOCANTINS | Brasil | 1706100 | 17 | 33 | nan | nan | nan | Cerrado | 0.8 |
| cb810078-04c7-3378-aac9-6587c7d9c87e | -11.47795 | -47.92567 | 2025-07-03 04:36:00 | NPP-375D | CHAPADA DA NATIVIDADE | TOCANTINS | Brasil | 1705102 | 17 | 33 | nan | nan | nan | Cerrado | 2.9 |
| 38b0e14e-7927-3889-8c14-53da7ce28811 | -10.71019 | -49.67273 | 2025-07-03 04:36:00 | NPP-375D | LAGOA DA CONFUSÃO | TOCANTINS | Brasil | 1711902 | 17 | 33 | nan | nan | nan | Cerrado | 1.8 |
| ec1c540b-c5e7-39b8-8ea8-2d6d33004a25 | -12.11435 | -44.98791 | 2025-07-03 04:36:00 | NPP-375D | BARREIRAS | BAHIA | Brasil | 2903201 | 29 | 33 | nan | nan | nan | Cerrado | 2.3 |
| 43817d69-6cb4-3611-bcb5-c1c78ffe678e | -9.87077 | -48.45562 | 2025-07-03 04:36:00 | NPP-375D | MIRACEMA DO TOCANTINS | TOCANTINS | Brasil | 1713205 | 17 | 33 | nan | nan | nan | Cerrado | 0.9 |
| 38633010-1e87-3c55-a39c-c69824dcd0c4 | -12.11051 | -44.98746 | 2025-07-03 04:36:00 | NPP-375D | BARREIRAS | BAHIA | Brasil | 2903201 | 29 | 33 | nan | nan | nan | Cerrado | 0.9 |
| 9f6a65d1-74ad-30ed-81dd-e33b9c0b6d79 | -10.68462 | -49.4903 | 2025-07-03 04:36:00 | NPP-375D | CRISTALÂNDIA | TOCANTINS | Brasil | 1706100 | 17 | 33 | nan | nan | nan | Cerrado | 0.8 |
| 43c53f4f-b590-3871-a926-5b4f50c4c328 | -9.60878 | -49.02367 | 2025-07-03 04:36:00 | NPP-375D | ABREULÂNDIA | TOCANTINS | Brasil | 1700251 | 17 | 33 | nan | nan | nan | Cerrado | 0.8 |
| 25d3e438-a959-396a-bfa0-038900660bb6 | -11.36057 | -48.72631 | 2025-07-03 04:36:00 | NPP-375D | GURUPI | TOCANTINS | Brasil | 1709500 | 17 | 33 | nan | nan | nan | Cerrado | 0.9 |
| da838b96-54ec-37ab-81a4-f5c6d51701d4 | -9.83067 | -48.37052 | 2025-07-03 04:36:00 | NPP-375D | MIRACEMA DO TOCANTINS | TOCANTINS | Brasil | 1713205 | 17 | 33 | nan | nan | nan | Cerrado | 1.3 |
| 190c1c6e-7907-3b58-a0a4-366a7486f11f | -9.79613 | -47.74419 | 2025-07-03 04:36:00 | NPP-375D | RIO SONO | TOCANTINS | Brasil | 1718758 | 17 | 33 | nan | nan | nan | Cerrado | 1.4 |
| 346707b4-b7ed-30e2-8623-eef60393ba81 | -11.54315 | -47.31369 | 2025-07-03 04:36:00 | NPP-375D | ALMAS | TOCANTINS | Brasil | 1700400 | 17 | 33 | nan | nan | nan | Cerrado | 1.8 |
| 50556176-9426-3be0-8651-e5ba1af07ce7 | -9.61322 | -49.01719 | 2025-07-03 04:36:00 | NPP-375D | ABREULÂNDIA | TOCANTINS | Brasil | 1700251 | 17 | 33 | nan | nan | nan | Cerrado | 1.0 |
| d5b63841-0f83-3256-98b2-e97583a1769e | -11.65982 | -44.59282 | 2025-07-03 04:36:00 | NPP-375D | COTEGIPE | BAHIA | Brasil | 2909406 | 29 | 33 | nan | nan | nan | Cerrado | 27.5 |
| 404d9f0a-faf0-3a32-895c-6954a7d5cd85 | -11.63987 | -48.06891 | 2025-07-03 04:36:00 | NPP-375D | CHAPADA DA NATIVIDADE | TOCANTINS | Brasil | 1705102 | 17 | 33 | nan | nan | nan | Cerrado | 4.4 |
| b6b471f3-8b95-34d3-a276-00f473e54797 | -12.16071 | -45.53179 | 2025-07-03 04:36:00 | NPP-375D | BARREIRAS | BAHIA | Brasil | 2903201 | 29 | 33 | nan | nan | nan | Cerrado | 2.1 |
| 55567011-e586-3dcd-95c5-43d48a4da72c | -11.64018 | -48.07646 | 2025-07-03 04:36:00 | NPP-375D | CHAPADA DA NATIVIDADE | TOCANTINS | Brasil | 1705102 | 17 | 33 | nan | nan | nan | Cerrado | 6.3 |
| 26d0b42b-c631-3b42-b694-7229f669dd21 | -11.64128 | -48.06928 | 2025-07-03 04:36:00 | NPP-375D | CHAPADA DA NATIVIDADE | TOCANTINS | Brasil | 1705102 | 17 | 33 | nan | nan | nan | Cerrado | 5.7 |
| 01b7a202-4b22-3f96-9cf4-8d5d21e8a775 | -10.70628 | -49.67574 | 2025-07-03 04:36:00 | NPP-375D | LAGOA DA CONFUSÃO | TOCANTINS | Brasil | 1711902 | 17 | 33 | nan | nan | nan | Cerrado | 1.8 |
| 31979e3e-2f18-3556-b71a-5a17e5e2ad4b | -11.83861 | -47.55239 | 2025-07-03 04:36:00 | NPP-375D | NATIVIDADE | TOCANTINS | Brasil | 1714203 | 17 | 33 | nan | nan | nan | Cerrado | 1.7 |
| 08ffc957-b06c-3c14-aab9-602fbd0a3133 | -9.72896 | -49.05745 | 2025-07-03 04:36:00 | NPP-375D | DIVINÓPOLIS DO TOCANTINS | TOCANTINS | Brasil | 1707108 | 17 | 33 | nan | nan | nan | Cerrado | 1.4 |
| 81dae548-a971-3c97-9d10-c0b2f9615a4c | -11.5633 | -47.45738 | 2025-07-03 04:36:00 | NPP-375D | NATIVIDADE | TOCANTINS | Brasil | 1714203 | 17 | 33 | nan | nan | nan | Cerrado | 1.5 |
| 2a3b40d5-834f-3889-ae74-5247ad9a2c79 | -11.63541 | -48.07555 | 2025-07-03 04:36:00 | NPP-375D | CHAPADA DA NATIVIDADE | TOCANTINS | Brasil | 1705102 | 17 | 33 | nan | nan | nan | Cerrado | 4.6 |
| 312538af-0745-3eb6-a533-ac24180d5f0e | -10.66123 | -49.45033 | 2025-07-03 04:36:00 | NPP-375D | CRISTALÂNDIA | TOCANTINS | Brasil | 1706100 | 17 | 33 | nan | nan | nan | Cerrado | 1.1 |
| 4cdfdaec-ac85-3795-b26c-d64ee8ca8dff | -10.94708 | -51.37178 | 2025-07-03 04:36:00 | NPP-375D | PORTO ALEGRE DO NORTE | MATO GROSSO | Brasil | 5106778 | 51 | 33 | nan | nan | nan | Cerrado | 1.8 |
| 6c8589b9-6ce7-3a9a-9336-eeab43a9be59 | -11.64073 | -48.07287 | 2025-07-03 04:36:00 | NPP-375D | CHAPADA DA NATIVIDADE | TOCANTINS | Brasil | 1705102 | 17 | 33 | nan | nan | nan | Cerrado | 5.7 |
| 198176bf-b442-3b9c-9afb-51dd332c1274 | -10.2975 | -57.13998 | 2025-07-03 04:36:00 | NPP-375D | NOVA MONTE VERDE | MATO GROSSO | Brasil | 5108956 | 51 | 33 | nan | nan | nan | Amazônia | 2.0 |
| 5f329682-77ae-3531-811a-909318b7ffe0 | -10.29962 | -57.12834 | 2025-07-03 04:36:00 | NPP-375D | NOVA MONTE VERDE | MATO GROSSO | Brasil | 5108956 | 51 | 33 | nan | nan | nan | Amazônia | 3.7 |
| 3da11282-be32-3b99-aac2-9544b83913f4 | -11.1112 | -48.87038 | 2025-07-03 04:36:00 | NPP-375D | CRIXÁS DO TOCANTINS | TOCANTINS | Brasil | 1706258 | 17 | 33 | nan | nan | nan | Cerrado | 2.2 |
| 1d33bfe0-df27-3109-921a-377b0d13e1cb | -10.66179 | -49.44678 | 2025-07-03 04:36:00 | NPP-375D | CRISTALÂNDIA | TOCANTINS | Brasil | 1706100 | 17 | 33 | nan | nan | nan | Cerrado | 1.1 |
| 17464d96-401a-357a-8897-65c8bda4c4ca | -11.85433 | -44.85022 | 2025-07-03 04:36:00 | NPP-375D | RIACHÃO DAS NEVES | BAHIA | Brasil | 2926202 | 29 | 33 | nan | nan | nan | Cerrado | 3.9 |
| 7c98befe-7d52-3f5b-8a8d-b5a07a32632f | -11.64952 | -44.58115 | 2025-07-03 04:36:00 | NPP-375D | COTEGIPE | BAHIA | Brasil | 2909406 | 29 | 33 | nan | nan | nan | Cerrado | 2.9 |
| 2ecef053-d57f-38a0-938a-b551ee5c38e9 | -11.65842 | -44.60274 | 2025-07-03 04:36:00 | NPP-375D | COTEGIPE | BAHIA | Brasil | 2909406 | 29 | 33 | nan | nan | nan | Cerrado | 6.3 |
| f2cdb117-288e-3918-bbd4-51e597d8b999 | -21.88464 | -56.11422 | 2025-07-03 04:38:00 | NPP-375D | BELA VISTA | MATO GROSSO DO SUL | Brasil | 5002100 | 50 | 33 | nan | nan | nan | Cerrado | 1.3 |
| c50ce5c2-f536-37c1-aa3a-dc6c29da9ff2 | -17.65247 | -46.83365 | 2025-07-03 04:38:00 | NPP-375D | VAZANTE | MINAS GERAIS | Brasil | 3171006 | 31 | 33 | nan | nan | nan | Cerrado | 0.8 |
| 6dda2660-9659-366b-8204-60e8e5715a8f | -15.7076 | -49.79714 | 2025-07-03 04:38:00 | NPP-375D | HEITORAÍ | GOIÁS | Brasil | 5209606 | 52 | 33 | nan | nan | nan | Cerrado | 0.6 |
| 34430048-8864-3e4e-be58-ce8645fe508f | -18.21099 | -51.35618 | 2025-07-03 04:38:00 | NPP-375D | APARECIDA DO RIO DOCE | GOIÁS | Brasil | 5201454 | 52 | 33 | nan | nan | nan | Cerrado | 2.0 |
| 48c09505-4b5b-39b1-be5f-763f877cb69f | -21.8853 | -56.11642 | 2025-07-03 04:38:00 | NPP-375D | BELA VISTA | MATO GROSSO DO SUL | Brasil | 5002100 | 50 | 33 | nan | nan | nan | Cerrado | 1.9 |
| bfa0f860-99e3-306e-a2dd-98bab2a2b2eb | -18.66351 | -55.75373 | 2025-07-03 04:38:00 | NPP-375D | CORUMBÁ | MATO GROSSO DO SUL | Brasil | 5003207 | 50 | 33 | nan | nan | nan | Pantanal | 2.1 |
| 3ae746dc-95f4-3a5d-90f4-b74551ac528f | -21.6127 | -57.56401 | 2025-07-03 04:38:00 | NPP-375D | PORTO MURTINHO | MATO GROSSO DO SUL | Brasil | 5006903 | 50 | 33 | nan | nan | nan | Cerrado | 1.3 |
| a2378661-509a-338f-ae7f-750813e4c3e7 | -17.09464 | -43.80482 | 2025-07-03 04:38:00 | NPP-375D | BOCAIÚVA | MINAS GERAIS | Brasil | 3107307 | 31 | 33 | nan | nan | nan | Cerrado | 0.9 |
| 674c3836-615b-3b41-9392-e198ee73279a | -18.21277 | -51.3452 | 2025-07-03 04:38:00 | NPP-375D | APARECIDA DO RIO DOCE | GOIÁS | Brasil | 5201454 | 52 | 33 | nan | nan | nan | Cerrado | 2.3 |
| 7aeb8f78-2db2-30ca-b7c0-3c7e1d9c285d | -18.6536 | -55.74057 | 2025-07-03 04:38:00 | NPP-375D | CORUMBÁ | MATO GROSSO DO SUL | Brasil | 5003207 | 50 | 33 | nan | nan | nan | Pantanal | 4.5 |
| c54156e3-5ad4-36c2-a5e1-285d15a65596 | -17.8642 | -44.57034 | 2025-07-03 04:38:00 | NPP-375D | LASSANCE | MINAS GERAIS | Brasil | 3138104 | 31 | 33 | nan | nan | nan | Cerrado | 1.3 |


[Clique aqui para ver as próximas entradas](README18.md)
