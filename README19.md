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

## Dados Diários - Página 19

| ID | Latitude | Longitude | Data/Hora GMT | Satélite | Município | Estado | País | Município ID | Estado ID | País ID | Dias sem Chuva | Precipitação | Risco de Fogo | Bioma | FRP |
|----|----------|-----------|---------------|----------|-----------|--------|------|--------------|-----------|---------|----------------|--------------|----------------|-------|-----|
| 13908012-b7cf-3136-acd1-561cfdaadb18 | -6.42222 | -43.09732 | 2025-09-24 05:40:00 | AQUA_M-M | SÃO FRANCISCO DO MARANHÃO | MARANHÃO | Brasil | 2110906 | 21 | 33 | nan | nan | nan | Cerrado | 6.3 |
| c6865167-1a76-3513-adc7-28633121690b | -4.31686 | -48.08782 | 2025-09-24 05:40:00 | AQUA_M-M | RONDON DO PARÁ | PARÁ | Brasil | 1506187 | 15 | 33 | nan | nan | nan | Amazônia | 51.6 |
| 9e4bc7d2-c9e8-3ca0-af0d-89cfd95b8d93 | -5.91824 | -43.85207 | 2025-09-24 05:40:00 | AQUA_M-M | BURITI BRAVO | MARANHÃO | Brasil | 2102309 | 21 | 33 | nan | nan | nan | Cerrado | 5.1 |
| e68b7f8e-35eb-38fd-895c-414198129991 | -7.6464 | -45.21178 | 2025-09-24 05:40:00 | AQUA_M-M | RIBEIRO GONÇALVES | PIAUÍ | Brasil | 2208908 | 22 | 33 | nan | nan | nan | Cerrado | 5.2 |
| 31821f29-dda9-37db-a3c2-8ef1ccf40f37 | -5.63933 | -43.91674 | 2025-09-24 05:40:00 | AQUA_M-M | FORTUNA | MARANHÃO | Brasil | 2104206 | 21 | 33 | nan | nan | nan | Cerrado | 23.4 |
| 6e77175c-24e7-385c-ab17-83e3c8abf1fd | -8.52917 | -45.01968 | 2025-09-24 05:40:00 | AQUA_M-M | BAIXA GRANDE DO RIBEIRO | PIAUÍ | Brasil | 2201150 | 22 | 33 | nan | nan | nan | Cerrado | 19.4 |
| 06c20018-2ceb-3225-91ce-0ea0b9ff1a62 | -5.90815 | -43.85413 | 2025-09-24 05:40:00 | AQUA_M-M | BURITI BRAVO | MARANHÃO | Brasil | 2102309 | 21 | 33 | nan | nan | nan | Cerrado | 14.3 |
| dd92bda4-880e-304a-815e-3d8a6333dd54 | 0.15963 | -60.67955 | 2025-09-24 05:40:00 | NOAA-20 | RORAINÓPOLIS | RORAIMA | Brasil | 1400472 | 14 | 33 | nan | nan | nan | Amazônia | 1.1 |
| 7b175fd3-d156-3a8f-afdd-662eca753c2d | -5.64078 | -43.90735 | 2025-09-24 05:40:00 | AQUA_M-M | FORTUNA | MARANHÃO | Brasil | 2104206 | 21 | 33 | nan | nan | nan | Cerrado | 15.6 |
| a22904c0-4a6a-3a75-b935-8a94c08cbf27 | -6.952 | -44.64388 | 2025-09-24 05:40:00 | AQUA_M-M | SÃO DOMINGOS DO AZEITÃO | MARANHÃO | Brasil | 2110658 | 21 | 33 | nan | nan | nan | Cerrado | 5.2 |
| 7d66ce45-247b-33b8-8e65-cae16af6b2f1 | -7.16968 | -42.23687 | 2025-09-24 05:40:00 | AQUA_M-M | COLÔNIA DO PIAUÍ | PIAUÍ | Brasil | 2202778 | 22 | 33 | nan | nan | nan | Caatinga | 7.9 |
| a72b1ea2-e0c4-35f5-84b8-4c4f0644c9ec | -4.79333 | -43.52649 | 2025-09-24 05:40:00 | AQUA_M-M | CAXIAS | MARANHÃO | Brasil | 2103000 | 21 | 33 | nan | nan | nan | Cerrado | 10.3 |
| 4f77a1c8-1150-3c0b-beb9-0185753e0298 | -4.31404 | -48.08215 | 2025-09-24 05:40:00 | AQUA_M-M | RONDON DO PARÁ | PARÁ | Brasil | 1506187 | 15 | 33 | nan | nan | nan | Amazônia | 44.1 |
| 2b45a790-3d0e-3593-8168-966b3a5ef1c3 | -7.37318 | -47.03691 | 2025-09-24 05:40:00 | AQUA_M-M | CAROLINA | MARANHÃO | Brasil | 2102804 | 21 | 33 | nan | nan | nan | Cerrado | 9.0 |
| 4fc5d0f1-117c-31f2-b9d2-a959c13d6ecd | -8.52762 | -45.02956 | 2025-09-24 05:40:00 | AQUA_M-M | BAIXA GRANDE DO RIBEIRO | PIAUÍ | Brasil | 2201150 | 22 | 33 | nan | nan | nan | Cerrado | 25.7 |
| c65fd298-6ef2-3c1a-92b2-c98db6894f04 | -3.41531 | -52.67857 | 2025-09-24 05:40:00 | NOAA-20 | BRASIL NOVO | PARÁ | Brasil | 1501725 | 15 | 33 | nan | nan | nan | Amazônia | 11.4 |
| 9e5f8a8e-4bcd-3aa3-9af5-92b805c706ff | -4.79115 | -42.76114 | 2025-09-24 05:40:00 | AQUA_M-M | JOSÉ DE FREITAS | PIAUÍ | Brasil | 2205508 | 22 | 33 | nan | nan | nan | Cerrado | 26.4 |
| ad0fe17a-92bb-3ecf-8d58-b3dd9d46a40e | -6.41475 | -43.08712 | 2025-09-24 05:40:00 | AQUA_M-M | SÃO FRANCISCO DO MARANHÃO | MARANHÃO | Brasil | 2110906 | 21 | 33 | nan | nan | nan | Cerrado | 59.0 |
| aeac0b84-0e6d-3288-9813-26af46357b17 | -4.77917 | -42.7627 | 2025-09-24 05:40:00 | AQUA_M-M | JOSÉ DE FREITAS | PIAUÍ | Brasil | 2205508 | 22 | 33 | nan | nan | nan | Cerrado | 40.6 |
| 04f788d8-361b-3b9d-888a-829d4cad81d2 | -9.3686 | -68.33672 | 2025-09-24 05:42:00 | NOAA-20 | BUJARI | ACRE | Brasil | 1200138 | 12 | 33 | nan | nan | nan | Amazônia | 0.8 |
| 0c9b3349-8816-37d5-b681-697f5df5a980 | -10.30619 | -46.0558 | 2025-09-24 05:42:00 | AQUA_M-M | MATEIROS | TOCANTINS | Brasil | 1712702 | 17 | 33 | nan | nan | nan | Cerrado | 157.1 |
| f2608b28-880f-3e4f-9a53-6e0e2d07fc1d | -9.81778 | -67.02777 | 2025-09-24 05:42:00 | NOAA-20 | ACRELÂNDIA | ACRE | Brasil | 1200013 | 12 | 33 | nan | nan | nan | Amazônia | 0.9 |
| ce616ba9-f981-3954-a39c-6e0f463b7bbf | -8.73384 | -67.19834 | 2025-09-24 05:42:00 | NOAA-20 | BOCA DO ACRE | AMAZONAS | Brasil | 1300706 | 13 | 33 | nan | nan | nan | Amazônia | 1.0 |
| 3810b169-bb66-3a87-b668-4c9946bc9852 | -11.51454 | -43.65051 | 2025-09-24 05:42:00 | AQUA_M-M | BARRA | BAHIA | Brasil | 2902708 | 29 | 33 | nan | nan | nan | Cerrado | 4.0 |
| 155849fb-9447-3a82-924b-b6367f6e5f0a | -9.78947 | -57.40933 | 2025-09-24 05:42:00 | NOAA-20 | NOVA MONTE VERDE | MATO GROSSO | Brasil | 5108956 | 51 | 33 | nan | nan | nan | Amazônia | 1.2 |
| 11459270-9e30-3672-99c1-7a161c606d31 | -9.37208 | -68.3373 | 2025-09-24 05:42:00 | NOAA-20 | BUJARI | ACRE | Brasil | 1200138 | 12 | 33 | nan | nan | nan | Amazônia | 0.8 |
| 74003d8c-e646-3793-8756-48570b6e8fe1 | -9.78691 | -57.40649 | 2025-09-24 05:42:00 | NOAA-20 | NOVA MONTE VERDE | MATO GROSSO | Brasil | 5108956 | 51 | 33 | nan | nan | nan | Amazônia | 0.9 |
| f7b97a08-5276-385c-9fe1-e94bba847edd | -10.29039 | -45.23077 | 2025-09-24 05:42:00 | AQUA_M-M | CORRENTE | PIAUÍ | Brasil | 2202901 | 22 | 33 | nan | nan | nan | Cerrado | 11.7 |
| afe4fc43-0d39-3198-b89e-25756e10a3b3 | -11.52065 | -43.66967 | 2025-09-24 05:42:00 | AQUA_M-M | BARRA | BAHIA | Brasil | 2902708 | 29 | 33 | nan | nan | nan | Cerrado | 20.8 |
| 05bfcce3-6b02-3ffb-86ae-853368e3a857 | -9.63922 | -57.01675 | 2025-09-24 05:42:00 | NOAA-20 | NOVA MONTE VERDE | MATO GROSSO | Brasil | 5108956 | 51 | 33 | nan | nan | nan | Amazônia | 2.0 |
| 678b8a07-9fe7-395f-896c-dfc7619ce613 | -10.58111 | -44.06734 | 2025-09-24 05:42:00 | AQUA_M-M | BURITIRAMA | BAHIA | Brasil | 2904753 | 29 | 33 | nan | nan | nan | Cerrado | 7.2 |
| 7fa5fba4-5401-3bf8-80e3-ea53da95947e | -10.53611 | -67.77061 | 2025-09-24 05:42:00 | NOAA-20 | CAPIXABA | ACRE | Brasil | 1200179 | 12 | 33 | nan | nan | nan | Amazônia | 0.5 |
| 7279de2f-8b38-3f77-b8a8-7d789ae828ee | -9.35135 | -66.50301 | 2025-09-24 05:42:00 | NOAA-20 | LÁBREA | AMAZONAS | Brasil | 1302405 | 13 | 33 | nan | nan | nan | Amazônia | 1.6 |
| b41e1012-5896-39af-b1ac-11e18491d60c | -11.15174 | -54.13136 | 2025-09-24 05:42:00 | NOAA-20 | MARCELÂNDIA | MATO GROSSO | Brasil | 5105580 | 51 | 33 | nan | nan | nan | Amazônia | 0.9 |
| cf185d49-3739-34b1-b801-bbf55a358c47 | -10.17928 | -68.16804 | 2025-09-24 05:42:00 | NOAA-20 | RIO BRANCO | ACRE | Brasil | 1200401 | 12 | 33 | nan | nan | nan | Amazônia | 1.1 |
| 1f289b33-6d8f-31d4-8bf2-07459efa2176 | -9.22729 | -65.7425 | 2025-09-24 05:42:00 | NOAA-20 | LÁBREA | AMAZONAS | Brasil | 1302405 | 13 | 33 | nan | nan | nan | Amazônia | 1.7 |
| ba104d71-e190-3a89-a0c8-c7323a6e41b3 | -10.56782 | -67.93882 | 2025-09-24 05:42:00 | NOAA-20 | CAPIXABA | ACRE | Brasil | 1200179 | 12 | 33 | nan | nan | nan | Amazônia | 1.1 |
| e54e9348-ed0d-3ed4-9148-86e0c95d0a04 | -9.55097 | -47.55492 | 2025-09-24 05:42:00 | AQUA_M-M | RIO SONO | TOCANTINS | Brasil | 1718758 | 17 | 33 | nan | nan | nan | Cerrado | 16.2 |
| 061d4aa6-7ab1-34ea-992b-2da3ef639d6c | -14.46877 | -45.53585 | 2025-09-24 05:42:00 | AQUA_M-M | COCOS | BAHIA | Brasil | 2908101 | 29 | 33 | nan | nan | nan | Cerrado | 11.7 |
| 173803f5-f68b-3f78-8e4f-65a83b55ad2b | -10.28114 | -45.22964 | 2025-09-24 05:42:00 | AQUA_M-M | CORRENTE | PIAUÍ | Brasil | 2202901 | 22 | 33 | nan | nan | nan | Cerrado | 6.9 |
| d91e1668-6f78-3d99-a1e6-5aaffe2bd8cc | -9.96035 | -66.77418 | 2025-09-24 05:42:00 | NOAA-20 | ACRELÂNDIA | ACRE | Brasil | 1200013 | 12 | 33 | nan | nan | nan | Amazônia | 0.9 |
| a80bee28-6d6c-3c64-be90-0f39eb5e91a1 | -9.13557 | -65.30921 | 2025-09-24 05:42:00 | NOAA-20 | LÁBREA | AMAZONAS | Brasil | 1302405 | 13 | 33 | nan | nan | nan | Amazônia | 1.2 |
| 53c65908-0a8c-3de3-a095-e502e5575b7b | -16.51637 | -43.54028 | 2025-09-24 05:42:00 | AQUA_M-M | FRANCISCO SÁ | MINAS GERAIS | Brasil | 3126703 | 31 | 33 | nan | nan | nan | Cerrado | 7.1 |
| 7b639a2f-1901-36af-8999-f198acb10633 | -8.73442 | -67.19473 | 2025-09-24 05:42:00 | NOAA-20 | BOCA DO ACRE | AMAZONAS | Brasil | 1300706 | 13 | 33 | nan | nan | nan | Amazônia | 1.0 |
| 1c204573-6808-30dd-80f3-f796c319ab12 | -11.5132 | -43.65942 | 2025-09-24 05:42:00 | AQUA_M-M | BARRA | BAHIA | Brasil | 2902708 | 29 | 33 | nan | nan | nan | Cerrado | 13.4 |
| 0ae6fd16-ef5a-3055-b136-911eecbe54a5 | -9.63963 | -57.01357 | 2025-09-24 05:42:00 | NOAA-20 | NOVA MONTE VERDE | MATO GROSSO | Brasil | 5108956 | 51 | 33 | nan | nan | nan | Amazônia | 3.0 |
| f1474567-c2a2-3f0e-bb19-5944397bbb94 | -11.8134 | -45.30933 | 2025-09-24 05:42:00 | AQUA_M-M | BARREIRAS | BAHIA | Brasil | 2903201 | 29 | 33 | nan | nan | nan | Cerrado | 4.4 |
| 50c35a7a-6629-363e-81b2-2261c5a81a89 | -10.14473 | -68.70374 | 2025-09-24 05:42:00 | NOAA-20 | RIO BRANCO | ACRE | Brasil | 1200401 | 12 | 33 | nan | nan | nan | Amazônia | 1.0 |
| b4d6d4cd-c4cf-37bd-98bb-a5de67f42ec8 | -10.62377 | -64.99467 | 2025-09-24 05:42:00 | NOAA-20 | GUAJARÁ-MIRIM | RONDÔNIA | Brasil | 1100106 | 11 | 33 | nan | nan | nan | Amazônia | 1.8 |
| 8945d86d-326d-3657-a94b-782bc90080fb | -9.96367 | -66.77473 | 2025-09-24 05:42:00 | NOAA-20 | ACRELÂNDIA | ACRE | Brasil | 1200013 | 12 | 33 | nan | nan | nan | Amazônia | 0.6 |
| 4a2e43ff-a434-393a-9f00-a164ab4b53ff | -9.6384 | -57.02305 | 2025-09-24 05:42:00 | NOAA-20 | NOVA MONTE VERDE | MATO GROSSO | Brasil | 5108956 | 51 | 33 | nan | nan | nan | Amazônia | 1.5 |
| dc2232dd-b77f-3ba6-ba53-bbd9d50f7aef | -9.05068 | -65.76401 | 2025-09-24 05:42:00 | NOAA-20 | LÁBREA | AMAZONAS | Brasil | 1302405 | 13 | 33 | nan | nan | nan | Amazônia | 0.9 |
| b6967615-9780-3501-9ada-40088c642554 | -9.75836 | -64.99525 | 2025-09-24 05:42:00 | NOAA-20 | PORTO VELHO | RONDÔNIA | Brasil | 1100205 | 11 | 33 | nan | nan | nan | Amazônia | 3.0 |
| 938b2caf-d3d0-3b66-ad41-7a7f0aa2d914 | -9.93934 | -66.75629 | 2025-09-24 05:42:00 | NOAA-20 | ACRELÂNDIA | ACRE | Brasil | 1200013 | 12 | 33 | nan | nan | nan | Amazônia | 1.0 |
| 98f7868e-7330-3fbf-834f-bac21f888908 | -11.52199 | -43.66076 | 2025-09-24 05:42:00 | AQUA_M-M | BARRA | BAHIA | Brasil | 2902708 | 29 | 33 | nan | nan | nan | Cerrado | 10.9 |
| 648c1646-5131-337d-ae58-8ca456f14dcf | -9.78165 | -64.88935 | 2025-09-24 05:42:00 | NOAA-20 | PORTO VELHO | RONDÔNIA | Brasil | 1100205 | 11 | 33 | nan | nan | nan | Amazônia | 0.8 |
| f4f0c9d2-43eb-3a59-8257-41d832500ca1 | -14.29689 | -41.83934 | 2025-09-24 05:42:00 | AQUA_M-M | MALHADA DE PEDRAS | BAHIA | Brasil | 2920304 | 29 | 33 | nan | nan | nan | Caatinga | 17.5 |
| 062ed52b-5764-36dd-a6ea-655dad27e3bf | -10.57974 | -44.07635 | 2025-09-24 05:42:00 | AQUA_M-M | JÚLIO BORGES | PIAUÍ | Brasil | 2205524 | 22 | 33 | nan | nan | nan | Cerrado | 5.0 |
| 27d1f2c9-d6ed-3d60-9d54-7bb7983cb64a | -10.54769 | -67.74239 | 2025-09-24 05:42:00 | NOAA-20 | CAPIXABA | ACRE | Brasil | 1200179 | 12 | 33 | nan | nan | nan | Amazônia | 0.8 |
| b5db0e49-e386-3f5a-8339-1dbce57c5156 | -10.59306 | -68.84472 | 2025-09-24 05:42:00 | NOAA-20 | XAPURI | ACRE | Brasil | 1200708 | 12 | 33 | nan | nan | nan | Amazônia | 0.4 |
| 4d656dac-64b7-3924-b4e7-cc4fb5b1de83 | -9.71098 | -64.96958 | 2025-09-24 05:42:00 | NOAA-20 | PORTO VELHO | RONDÔNIA | Brasil | 1100205 | 11 | 33 | nan | nan | nan | Amazônia | 0.8 |
| 62ff93a3-fbfd-3944-bdf7-aac142b5f062 | -11.14528 | -54.13057 | 2025-09-24 05:42:00 | NOAA-20 | MARCELÂNDIA | MATO GROSSO | Brasil | 5105580 | 51 | 33 | nan | nan | nan | Amazônia | 0.9 |
| 6582bbb7-36f2-3882-b3ce-3ab7630f06f1 | -9.63881 | -57.01989 | 2025-09-24 05:42:00 | NOAA-20 | NOVA MONTE VERDE | MATO GROSSO | Brasil | 5108956 | 51 | 33 | nan | nan | nan | Amazônia | 2.0 |
| e1e7d619-41ed-3ba7-a67c-0c69ce0b99ed | -10.17492 | -55.39317 | 2025-09-24 05:42:00 | NOAA-20 | NOVA GUARITA | MATO GROSSO | Brasil | 5108808 | 51 | 33 | nan | nan | nan | Amazônia | 1.8 |
| 3fa49879-a5a4-346e-98fc-01f0b3d3cf5f | -16.51501 | -43.5497 | 2025-09-24 05:42:00 | AQUA_M-M | FRANCISCO SÁ | MINAS GERAIS | Brasil | 3126703 | 31 | 33 | nan | nan | nan | Cerrado | 23.0 |
| a57c3a9e-68be-32b6-8f15-469fab65f5bf | -10.27961 | -45.2394 | 2025-09-24 05:42:00 | AQUA_M-M | CORRENTE | PIAUÍ | Brasil | 2202901 | 22 | 33 | nan | nan | nan | Cerrado | 3.9 |
| 58e72e68-8987-3ddb-b087-4d1bd5d67af4 | -9.37144 | -68.34119 | 2025-09-24 05:42:00 | NOAA-20 | BUJARI | ACRE | Brasil | 1200138 | 12 | 33 | nan | nan | nan | Amazônia | 0.8 |
| 4c778e05-16d3-3451-8cbe-606e7f1390f4 | -9.34803 | -66.50248 | 2025-09-24 05:42:00 | NOAA-20 | LÁBREA | AMAZONAS | Brasil | 1302405 | 13 | 33 | nan | nan | nan | Amazônia | 1.6 |
| 4063ea21-f634-3116-a4ae-c33c83945655 | -9.35411 | -66.50706 | 2025-09-24 05:42:00 | NOAA-20 | LÁBREA | AMAZONAS | Brasil | 1302405 | 13 | 33 | nan | nan | nan | Amazônia | 0.7 |
| ef8eea55-97f6-3abb-bfe6-1713e6f1c8ff | -9.13888 | -65.30973 | 2025-09-24 05:42:00 | NOAA-20 | LÁBREA | AMAZONAS | Brasil | 1302405 | 13 | 33 | nan | nan | nan | Amazônia | 1.2 |
| c4d5c96f-99a4-31cb-a6e3-439c4171987d | -10.29657 | -46.05424 | 2025-09-24 05:42:00 | AQUA_M-M | MATEIROS | TOCANTINS | Brasil | 1712702 | 17 | 33 | nan | nan | nan | Cerrado | 51.3 |
| e60c2666-bb82-3d29-ab4b-0141f8a8d031 | -10.30444 | -46.06672 | 2025-09-24 05:42:00 | AQUA_M-M | MATEIROS | TOCANTINS | Brasil | 1712702 | 17 | 33 | nan | nan | nan | Cerrado | 55.0 |
| b3fd8c4b-9f94-3687-8e17-c353946025c9 | -10.29481 | -46.06512 | 2025-09-24 05:42:00 | AQUA_M-M | MATEIROS | TOCANTINS | Brasil | 1712702 | 17 | 33 | nan | nan | nan | Cerrado | 28.4 |
| 112c948c-33e5-35ad-bd32-f5936c852e8a | -9.7783 | -64.88883 | 2025-09-24 05:42:00 | NOAA-20 | PORTO VELHO | RONDÔNIA | Brasil | 1100205 | 11 | 33 | nan | nan | nan | Amazônia | 0.8 |
| 6f92c992-f114-3a8d-b417-139489848911 | -9.13943 | -65.30624 | 2025-09-24 05:42:00 | NOAA-20 | LÁBREA | AMAZONAS | Brasil | 1302405 | 13 | 33 | nan | nan | nan | Amazônia | 1.4 |
| d2cb52f4-582d-3b9f-a708-8c41d5260757 | -9.7617 | -64.99578 | 2025-09-24 05:42:00 | NOAA-20 | PORTO VELHO | RONDÔNIA | Brasil | 1100205 | 11 | 33 | nan | nan | nan | Amazônia | 0.8 |
| 10231a55-1ca9-3a87-98f3-2878dfab383e | -9.56403 | -47.54284 | 2025-09-24 05:42:00 | AQUA_M-M | RIO SONO | TOCANTINS | Brasil | 1718758 | 17 | 33 | nan | nan | nan | Cerrado | 11.5 |
| a1d80b30-7236-3bb7-adfe-a7b3fea58c2f | -9.55321 | -47.54107 | 2025-09-24 05:42:00 | AQUA_M-M | RIO SONO | TOCANTINS | Brasil | 1718758 | 17 | 33 | nan | nan | nan | Cerrado | 35.3 |
| 8772db8c-1d08-369d-b44e-759df3dcd445 | -9.41591 | -67.62254 | 2025-09-24 05:42:00 | NOAA-20 | BOCA DO ACRE | AMAZONAS | Brasil | 1300706 | 13 | 33 | nan | nan | nan | Amazônia | 0.4 |
| 122640f0-d09b-31f9-b03a-ad2509037478 | -10.00382 | -67.50034 | 2025-09-24 05:42:00 | NOAA-20 | RIO BRANCO | ACRE | Brasil | 1200401 | 12 | 33 | nan | nan | nan | Amazônia | 0.4 |
| 79e8412f-b2ae-3707-807f-c6e4e56f8d9d | -11.42749 | -44.93504 | 2025-09-24 05:42:00 | AQUA_M-M | RIACHÃO DAS NEVES | BAHIA | Brasil | 2926202 | 29 | 33 | nan | nan | nan | Cerrado | 3.9 |
| 91942bf4-4e7d-345a-8764-f088b0936999 | -9.78651 | -57.4096 | 2025-09-24 05:42:00 | NOAA-20 | NOVA MONTE VERDE | MATO GROSSO | Brasil | 5108956 | 51 | 33 | nan | nan | nan | Amazônia | 1.8 |
| 4205d212-5286-3a36-8e5f-68a9e837e58a | -9.96286 | -45.3126 | 2025-09-24 05:42:00 | AQUA_M-M | GILBUÉS | PIAUÍ | Brasil | 2204402 | 22 | 33 | nan | nan | nan | Cerrado | 6.5 |
| df4523f9-6769-3401-8c14-a34a0da191a7 | -14.29835 | -41.82894 | 2025-09-24 05:42:00 | AQUA_M-M | MALHADA DE PEDRAS | BAHIA | Brasil | 2920304 | 29 | 33 | nan | nan | nan | Caatinga | 6.4 |
| 350d8c4d-04e5-3478-899f-be8a5ab52f2a | -10.0072 | -67.50089 | 2025-09-24 05:42:00 | NOAA-20 | RIO BRANCO | ACRE | Brasil | 1200401 | 12 | 33 | nan | nan | nan | Amazônia | 0.4 |
| c88106cf-b14a-3fd4-a40e-b99b666caec0 | -11.41851 | -44.93348 | 2025-09-24 05:42:00 | AQUA_M-M | RIACHÃO DAS NEVES | BAHIA | Brasil | 2926202 | 29 | 33 | nan | nan | nan | Cerrado | 3.9 |
| 9001b85d-60c3-30c7-94b2-a9fcf346cc61 | -13.81946 | -43.85732 | 2025-09-24 05:42:00 | AQUA_M-M | CARINHANHA | BAHIA | Brasil | 2907103 | 29 | 33 | nan | nan | nan | Cerrado | 6.5 |
| 114ac063-38db-3608-bc34-1a78e6e8bbbe | -9.78905 | -57.41243 | 2025-09-24 05:42:00 | NOAA-20 | NOVA MONTE VERDE | MATO GROSSO | Brasil | 5108956 | 51 | 33 | nan | nan | nan | Amazônia | 1.2 |
| ae642d52-ca29-3aab-bba8-cd39db1c148e | -17.94674 | -55.86033 | 2025-09-24 05:44:00 | NOAA-20 | CORUMBÁ | MATO GROSSO DO SUL | Brasil | 5003207 | 50 | 33 | nan | nan | nan | Pantanal | 3.4 |
| 76e39c17-8a4b-3330-b074-d5cc27bc62f5 | -17.9565 | -55.86408 | 2025-09-24 05:44:00 | NOAA-20 | CORUMBÁ | MATO GROSSO DO SUL | Brasil | 5003207 | 50 | 33 | nan | nan | nan | Pantanal | 0.9 |
| 90c1a25e-4238-3dd0-836c-c6394357a78a | -15.78332 | -59.48893 | 2025-09-24 05:44:00 | NOAA-20 | PONTES E LACERDA | MATO GROSSO | Brasil | 5106752 | 51 | 33 | nan | nan | nan | Amazônia | 2.1 |
| 9e5065aa-14f4-34a3-abf9-7a86427e5781 | -17.94874 | -55.87893 | 2025-09-24 05:44:00 | NOAA-20 | CORUMBÁ | MATO GROSSO DO SUL | Brasil | 5003207 | 50 | 33 | nan | nan | nan | Pantanal | 1.2 |
| a2ae2057-ede2-3185-9b41-774ef1ef24a1 | -17.95069 | -55.85822 | 2025-09-24 05:44:00 | NOAA-20 | CORUMBÁ | MATO GROSSO DO SUL | Brasil | 5003207 | 50 | 33 | nan | nan | nan | Pantanal | 1.7 |
| 335407cc-0de0-3179-939e-896c64259fc8 | -15.90598 | -59.35923 | 2025-09-24 05:44:00 | NOAA-20 | PONTES E LACERDA | MATO GROSSO | Brasil | 5106752 | 51 | 33 | nan | nan | nan | Amazônia | 1.6 |
| 0b9d6044-69a4-39e7-bc70-10015f11bec3 | -17.9502 | -55.8634 | 2025-09-24 05:44:00 | NOAA-20 | CORUMBÁ | MATO GROSSO DO SUL | Brasil | 5003207 | 50 | 33 | nan | nan | nan | Pantanal | 1.7 |
| 556b9516-21d6-3126-be4f-978afab3e2e6 | -15.83824 | -59.59607 | 2025-09-24 05:44:00 | NOAA-20 | PONTES E LACERDA | MATO GROSSO | Brasil | 5106752 | 51 | 33 | nan | nan | nan | Amazônia | 1.2 |
| 10ed0bae-c663-3c2d-a4ca-719c4ec343b4 | -15.90048 | -59.3636 | 2025-09-24 05:44:00 | NOAA-20 | PONTES E LACERDA | MATO GROSSO | Brasil | 5106752 | 51 | 33 | nan | nan | nan | Amazônia | 2.3 |
| 5149c4bd-e2a0-3e4d-9e09-9d25c6ac7a8f | -15.77913 | -59.48285 | 2025-09-24 05:44:00 | NOAA-20 | PONTES E LACERDA | MATO GROSSO | Brasil | 5106752 | 51 | 33 | nan | nan | nan | Amazônia | 2.0 |
| 3bb968f0-5c8e-3642-8505-ef8fbf6c8049 | -17.94923 | -55.87375 | 2025-09-24 05:44:00 | NOAA-20 | CORUMBÁ | MATO GROSSO DO SUL | Brasil | 5003207 | 50 | 33 | nan | nan | nan | Pantanal | 1.4 |
| 80b0645e-9909-31fb-9e9d-cbec80d45136 | -15.83356 | -59.59871 | 2025-09-24 05:44:00 | NOAA-20 | PONTES E LACERDA | MATO GROSSO | Brasil | 5106752 | 51 | 33 | nan | nan | nan | Amazônia | 3.8 |


[Clique aqui para ver as próximas entradas](README20.md)
