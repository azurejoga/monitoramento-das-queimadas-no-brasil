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

## Dados Diários - Página 230

| ID | Latitude | Longitude | Data/Hora GMT | Satélite | Município | Estado | País | Município ID | Estado ID | País ID | Dias sem Chuva | Precipitação | Risco de Fogo | Bioma | FRP |
|----|----------|-----------|---------------|----------|-----------|--------|------|--------------|-----------|---------|----------------|--------------|----------------|-------|-----|
| 9cc3aaa7-18d2-3c98-835b-4de01aa6887f | -14.48054 | -40.71792 | 2026-10-08 15:39:00 | NOAA-21 | ANAGÉ | BAHIA | Brasil | 2901205 | 29 | 33 | nan | nan | nan | Caatinga | 16.5 |
| b6763abc-5d3b-3d79-806b-74b9526b6e97 | -14.4088 | -41.28215 | 2026-10-08 15:39:00 | NOAA-21 | ARACATU | BAHIA | Brasil | 2902005 | 29 | 33 | nan | nan | nan | Caatinga | 173.5 |
| 0d6b00ed-94fb-3c51-b324-e76e674b621f | -11.73549 | -43.64323 | 2026-10-08 15:39:00 | NOAA-21 | BARRA | BAHIA | Brasil | 2902708 | 29 | 33 | nan | nan | nan | Cerrado | 16.5 |
| 1c3e60ae-bec6-36f1-89f7-b3f7f995c51c | -15.57427 | -42.90005 | 2026-10-08 15:39:00 | NOAA-21 | PORTEIRINHA | MINAS GERAIS | Brasil | 3152204 | 31 | 33 | nan | nan | nan | Cerrado | 10.4 |
| 47409841-f6bb-3436-b363-b5b235b67851 | -13.07143 | -40.97827 | 2026-10-08 15:39:00 | NOAA-21 | ITAETÉ | BAHIA | Brasil | 2915007 | 29 | 33 | nan | nan | nan | Caatinga | 1.8 |
| bac9a47d-1dee-3bb8-9964-b8c850ea0b53 | -12.19463 | -44.82162 | 2026-10-08 15:39:00 | NOAA-21 | BARREIRAS | BAHIA | Brasil | 2903201 | 29 | 33 | nan | nan | nan | Cerrado | 143.1 |
| 1355c984-e7ff-3908-9e41-7e7d2d98c02c | -16.21074 | -40.36561 | 2026-10-08 15:39:00 | NOAA-21 | JACINTO | MINAS GERAIS | Brasil | 3134707 | 31 | 33 | nan | nan | nan | Mata Atlântica | 7.5 |
| 66d84828-5824-36ef-b039-c08a66d358e2 | -14.75352 | -39.81329 | 2026-10-08 15:39:00 | NOAA-21 | SANTA CRUZ DA VITÓRIA | BAHIA | Brasil | 2927804 | 29 | 33 | nan | nan | nan | Mata Atlântica | 5.6 |
| 2b2b2569-84d4-3b40-8025-45a4548b75b3 | -11.64277 | -43.71172 | 2026-10-08 15:39:00 | NOAA-21 | BARRA | BAHIA | Brasil | 2902708 | 29 | 33 | nan | nan | nan | Cerrado | 15.8 |
| 1852682b-4705-323a-88e7-8a51150a6c75 | -14.44143 | -40.78944 | 2026-10-08 15:39:00 | NOAA-21 | ANAGÉ | BAHIA | Brasil | 2901205 | 29 | 33 | nan | nan | nan | Caatinga | 6.9 |
| 5662822c-084d-3f3e-b9fb-f51292943cbe | -17.22223 | -39.38518 | 2026-10-08 15:39:00 | NOAA-21 | PRADO | BAHIA | Brasil | 2925501 | 29 | 33 | nan | nan | nan | Mata Atlântica | 5.7 |
| 549166d4-5d28-3e2a-987f-20289d5a353f | -15.53489 | -41.72305 | 2026-10-08 15:39:00 | NOAA-21 | SÃO JOÃO DO PARAÍSO | MINAS GERAIS | Brasil | 3162708 | 31 | 33 | nan | nan | nan | Mata Atlântica | 7.5 |
| c0be6b8f-b02a-3a46-b6c7-a5099be97a86 | -14.47066 | -40.72605 | 2026-10-08 15:39:00 | NOAA-21 | ANAGÉ | BAHIA | Brasil | 2901205 | 29 | 33 | nan | nan | nan | Caatinga | 121.7 |
| 440ad7a6-3584-341d-8106-67c41aed9037 | -15.61982 | -40.41693 | 2026-10-08 15:39:00 | NOAA-21 | MACARANI | BAHIA | Brasil | 2919702 | 29 | 33 | nan | nan | nan | Mata Atlântica | 1.9 |
| 86f73111-adb6-351a-8ea0-eef9714d0a41 | -18.16597 | -42.613 | 2026-10-08 15:39:00 | NOAA-21 | SÃO SEBASTIÃO DO MARANHÃO | MINAS GERAIS | Brasil | 3164506 | 31 | 33 | nan | nan | nan | Mata Atlântica | 3.1 |
| db3fee40-19af-3436-b6b0-72602253adee | -13.72259 | -40.34958 | 2026-10-08 15:39:00 | NOAA-21 | JEQUIÉ | BAHIA | Brasil | 2918001 | 29 | 33 | nan | nan | nan | Caatinga | 6.1 |
| ae040fab-0c78-3b28-a586-82c3f519ef39 | -12.22828 | -44.75811 | 2026-10-08 15:39:00 | NOAA-21 | CATOLÂNDIA | BAHIA | Brasil | 2907400 | 29 | 33 | nan | nan | nan | Cerrado | 132.5 |
| 3180822b-c2c6-3e8f-9e8e-13cf68968841 | -11.77104 | -45.56772 | 2026-10-08 15:39:00 | NOAA-21 | RIACHÃO DAS NEVES | BAHIA | Brasil | 2926202 | 29 | 33 | nan | nan | nan | Cerrado | 63.9 |
| 772854ab-8151-35eb-8f4e-8f55dbd6f6e4 | -14.0504 | -43.81969 | 2026-10-08 15:39:00 | NOAA-21 | CARINHANHA | BAHIA | Brasil | 2907103 | 29 | 33 | nan | nan | nan | Cerrado | 91.5 |
| 275e6962-474e-3214-a8db-991b35dd6077 | -14.89614 | -39.72696 | 2026-10-08 15:39:00 | NOAA-21 | FLORESTA AZUL | BAHIA | Brasil | 2911006 | 29 | 33 | nan | nan | nan | Mata Atlântica | 11.3 |
| 22201141-5ab7-3025-a5d4-2dd0b3a41227 | -16.49204 | -41.80933 | 2026-10-08 15:39:00 | NOAA-21 | ITINGA | MINAS GERAIS | Brasil | 3134004 | 31 | 33 | nan | nan | nan | Mata Atlântica | 13.1 |
| ccbea2be-e3b1-3b2f-aecc-ff094785cffe | -14.425 | -41.13577 | 2026-10-08 15:39:00 | NOAA-21 | ARACATU | BAHIA | Brasil | 2902005 | 29 | 33 | nan | nan | nan | Caatinga | 47.0 |
| 2323d4b8-327c-33be-ad8e-216c540adb40 | -12.15229 | -44.72106 | 2026-10-08 15:39:00 | NOAA-21 | BARREIRAS | BAHIA | Brasil | 2903201 | 29 | 33 | nan | nan | nan | Cerrado | 24.5 |
| 58bd6283-61be-30f1-94c4-c5276da33804 | -14.53704 | -41.27558 | 2026-10-08 15:39:00 | NOAA-21 | CARAÍBAS | BAHIA | Brasil | 2906899 | 29 | 33 | nan | nan | nan | Caatinga | 9.1 |
| 1ca818fb-f2b7-3a61-bc39-9f2816e81d61 | -13.37001 | -43.88137 | 2026-10-08 15:39:00 | NOAA-21 | SERRA DO RAMALHO | BAHIA | Brasil | 2930154 | 29 | 33 | nan | nan | nan | Cerrado | 144.5 |
| 667356df-144d-360a-b677-c2d49ab858e9 | -16.5884 | -42.43318 | 2026-10-08 15:39:00 | NOAA-21 | JOSENÓPOLIS | MINAS GERAIS | Brasil | 3136579 | 31 | 33 | nan | nan | nan | Cerrado | 8.0 |
| 4af2f9f4-9e9f-302e-b728-6242af4bec4a | -14.22486 | -41.99028 | 2026-10-08 15:39:00 | NOAA-21 | RIO DO ANTÔNIO | BAHIA | Brasil | 2926806 | 29 | 33 | nan | nan | nan | Caatinga | 7.0 |
| f8bf1c53-8f8c-3f55-a2e4-66488d149499 | -11.61704 | -43.65104 | 2026-10-08 15:39:00 | NOAA-21 | BARRA | BAHIA | Brasil | 2902708 | 29 | 33 | nan | nan | nan | Cerrado | 21.3 |
| 9f81c256-29d5-3cec-b6ac-3d19bd10848c | -11.03743 | -38.9808 | 2026-10-08 15:39:00 | NOAA-21 | TUCANO | BAHIA | Brasil | 2931905 | 29 | 33 | nan | nan | nan | Caatinga | 5.2 |
| 9e30a03a-a1ff-3bea-8437-4c96206a4c1f | -12.15698 | -44.72278 | 2026-10-08 15:39:00 | NOAA-21 | BARREIRAS | BAHIA | Brasil | 2903201 | 29 | 33 | nan | nan | nan | Cerrado | 41.5 |
| 975fbc41-3ff9-3b30-acaa-e97a0f4faac7 | -12.15411 | -44.75915 | 2026-10-08 15:39:00 | NOAA-21 | BARREIRAS | BAHIA | Brasil | 2903201 | 29 | 33 | nan | nan | nan | Cerrado | 24.1 |
| 12fdb2a1-8663-31af-9b6e-b75756fd972c | -14.41476 | -41.28531 | 2026-10-08 15:39:00 | NOAA-21 | ARACATU | BAHIA | Brasil | 2902005 | 29 | 33 | nan | nan | nan | Caatinga | 231.0 |
| 34387a76-46f4-3ea8-9845-65e2b7ef106f | -13.74271 | -43.51999 | 2026-10-08 15:39:00 | NOAA-21 | MALHADA | BAHIA | Brasil | 2920205 | 29 | 33 | nan | nan | nan | Cerrado | 15.3 |
| f0732d55-6fec-3d3d-99e3-7bb3c94c0858 | -11.60046 | -43.66454 | 2026-10-08 15:39:00 | NOAA-21 | BARRA | BAHIA | Brasil | 2902708 | 29 | 33 | nan | nan | nan | Cerrado | 53.3 |
| ea5098f2-9d15-3134-825a-28e95e5a028c | -11.63606 | -43.69918 | 2026-10-08 15:39:00 | NOAA-21 | BARRA | BAHIA | Brasil | 2902708 | 29 | 33 | nan | nan | nan | Cerrado | 33.4 |
| f6775618-332e-393d-b37c-4c81c83ef81c | -15.65153 | -40.04835 | 2026-10-08 15:39:00 | NOAA-21 | ITARANTIM | BAHIA | Brasil | 2916807 | 29 | 33 | nan | nan | nan | Mata Atlântica | 1.9 |
| 667aac8a-7e03-341e-aaa1-fbb4190ee74a | -11.97189 | -39.04001 | 2026-10-08 15:39:00 | NOAA-21 | SANTA BÁRBARA | BAHIA | Brasil | 2927507 | 29 | 33 | nan | nan | nan | Caatinga | 10.2 |
| 538218b0-5c21-3c21-8271-94cde2069c7e | -11.86225 | -43.55967 | 2026-10-08 15:39:00 | NOAA-21 | BARRA | BAHIA | Brasil | 2902708 | 29 | 33 | nan | nan | nan | Cerrado | 15.8 |
| 8d36d31f-ec7c-3c92-842d-ee617ee9a95c | -13.02067 | -41.05128 | 2026-10-08 15:39:00 | NOAA-21 | ITAETÉ | BAHIA | Brasil | 2915007 | 29 | 33 | nan | nan | nan | Caatinga | 3.6 |
| 20371b34-1911-3044-8562-7890b1aa3d37 | -16.97483 | -41.22987 | 2026-10-08 15:39:00 | NOAA-21 | JOAÍMA | MINAS GERAIS | Brasil | 3136009 | 31 | 33 | nan | nan | nan | Mata Atlântica | 16.8 |
| 07755889-25ef-3344-9bb6-5d331160abb8 | -11.74018 | -43.63886 | 2026-10-08 15:39:00 | NOAA-21 | BARRA | BAHIA | Brasil | 2902708 | 29 | 33 | nan | nan | nan | Cerrado | 20.1 |
| a3c70847-4073-3ba6-b8e2-ccb537eac799 | -11.60382 | -43.63984 | 2026-10-08 15:39:00 | NOAA-21 | BARRA | BAHIA | Brasil | 2902708 | 29 | 33 | nan | nan | nan | Cerrado | 138.2 |
| 659c3389-ea34-319d-bedf-0a586d99b80a | -12.17579 | -44.80891 | 2026-10-08 15:39:00 | NOAA-21 | BARREIRAS | BAHIA | Brasil | 2903201 | 29 | 33 | nan | nan | nan | Cerrado | 98.1 |
| fa391ae9-c3c3-3c16-b0bb-3c60b10f7c17 | -13.95686 | -44.85815 | 2026-10-08 15:39:00 | NOAA-21 | COCOS | BAHIA | Brasil | 2908101 | 29 | 33 | nan | nan | nan | Cerrado | 63.5 |
| 3a7bebd5-67b9-3e2e-86aa-6ed40e25bdda | -17.00612 | -42.38228 | 2026-10-08 15:39:00 | NOAA-21 | FRANCISCO BADARÓ | MINAS GERAIS | Brasil | 3126505 | 31 | 33 | nan | nan | nan | Cerrado | 13.5 |
| def0583d-7cd9-3ed8-b4b7-48d48344d843 | -17.00686 | -42.38025 | 2026-10-08 15:39:00 | NOAA-21 | FRANCISCO BADARÓ | MINAS GERAIS | Brasil | 3126505 | 31 | 33 | nan | nan | nan | Cerrado | 19.2 |
| 54b5f47a-ad60-357e-b27a-838871840c3f | -11.77007 | -45.56523 | 2026-10-08 15:39:00 | NOAA-21 | RIACHÃO DAS NEVES | BAHIA | Brasil | 2926202 | 29 | 33 | nan | nan | nan | Cerrado | 33.5 |
| 045f5e82-11f4-3fc2-b56f-6e41a13241a8 | -17.20548 | -39.27918 | 2026-10-08 15:39:00 | NOAA-21 | PRADO | BAHIA | Brasil | 2925501 | 29 | 33 | nan | nan | nan | Mata Atlântica | 9.6 |
| 4c176e3c-91ee-3477-bf52-a49c994c7167 | -14.4305 | -41.13546 | 2026-10-08 15:39:00 | NOAA-21 | ARACATU | BAHIA | Brasil | 2902005 | 29 | 33 | nan | nan | nan | Caatinga | 47.0 |
| aee56670-5b35-3472-8616-0ad0eb300e5e | -13.97538 | -44.83708 | 2026-10-08 15:39:00 | NOAA-21 | COCOS | BAHIA | Brasil | 2908101 | 29 | 33 | nan | nan | nan | Cerrado | 14.4 |
| 5105b1e9-c725-360a-ab7f-a47470d63b2b | -11.35399 | -43.14912 | 2026-10-08 15:39:00 | NOAA-21 | XIQUE-XIQUE | BAHIA | Brasil | 2933604 | 29 | 33 | nan | nan | nan | Caatinga | 20.9 |
| 85a5a9df-b607-347a-b4c0-10eb958ddfb7 | -12.61977 | -44.54661 | 2026-10-08 15:39:00 | NOAA-21 | BAIANÓPOLIS | BAHIA | Brasil | 2902500 | 29 | 33 | nan | nan | nan | Cerrado | 31.8 |
| e4dd7c72-7226-35fa-8a5d-2714c637c48c | -11.32996 | -41.98674 | 2026-10-08 15:39:00 | NOAA-21 | PRESIDENTE DUTRA | BAHIA | Brasil | 2925600 | 29 | 33 | nan | nan | nan | Caatinga | 10.0 |
| 58de1768-a328-30b5-94a9-9ebe8430247d | -12.15828 | -44.71452 | 2026-10-08 15:39:00 | NOAA-21 | BARREIRAS | BAHIA | Brasil | 2903201 | 29 | 33 | nan | nan | nan | Cerrado | 24.5 |
| 03e23f1b-69cd-303c-af86-7cb00099703f | -11.76481 | -45.57479 | 2026-10-08 15:39:00 | NOAA-21 | RIACHÃO DAS NEVES | BAHIA | Brasil | 2926202 | 29 | 33 | nan | nan | nan | Cerrado | 71.7 |
| 80835841-c3b5-3af9-b455-a0a17c872b88 | -16.9381 | -42.07961 | 2026-10-08 15:39:00 | NOAA-21 | ARAÇUAÍ | MINAS GERAIS | Brasil | 3103405 | 31 | 33 | nan | nan | nan | Mata Atlântica | 9.0 |
| 5b08223c-e798-3da8-a2cd-26faa4447a4a | -11.45473 | -43.38197 | 2026-10-08 15:39:00 | NOAA-21 | BARRA | BAHIA | Brasil | 2902708 | 29 | 33 | nan | nan | nan | Cerrado | 37.3 |
| 67f09a8e-d617-3e0e-8d76-685d0ad05eb3 | -13.76917 | -40.60891 | 2026-10-08 15:39:00 | NOAA-21 | MARACÁS | BAHIA | Brasil | 2920502 | 29 | 33 | nan | nan | nan | Caatinga | 7.4 |
| cc9766c8-1f28-3259-b944-1dab9faab20f | -13.18923 | -43.50304 | 2026-10-08 15:39:00 | NOAA-21 | BOM JESUS DA LAPA | BAHIA | Brasil | 2903904 | 29 | 33 | nan | nan | nan | Cerrado | 11.3 |
| dfad7057-4eb4-3848-b560-29df4e293664 | -15.76395 | -41.7749 | 2026-10-08 15:39:00 | NOAA-21 | CURRAL DE DENTRO | MINAS GERAIS | Brasil | 3120870 | 31 | 33 | nan | nan | nan | Mata Atlântica | 6.8 |
| 3efe6906-2c4e-312e-807b-3fc6f9828fe5 | -12.7119 | -45.81248 | 2026-10-08 15:39:00 | NOAA-21 | SÃO DESIDÉRIO | BAHIA | Brasil | 2928901 | 29 | 33 | nan | nan | nan | Cerrado | 132.5 |
| f042d1a6-3211-3e7b-a7df-6dbf16e53cd1 | -15.51729 | -42.65829 | 2026-10-08 15:39:00 | NOAA-21 | RIO PARDO DE MINAS | MINAS GERAIS | Brasil | 3155603 | 31 | 33 | nan | nan | nan | Mata Atlântica | 22.2 |
| eaf8c094-c521-3ab3-8118-45f88c6ea604 | -13.97055 | -44.84447 | 2026-10-08 15:39:00 | NOAA-21 | COCOS | BAHIA | Brasil | 2908101 | 29 | 33 | nan | nan | nan | Cerrado | 25.2 |
| c794a62d-a2f7-373c-b448-28d1e7a31616 | -11.60101 | -43.66915 | 2026-10-08 15:39:00 | NOAA-21 | BARRA | BAHIA | Brasil | 2902708 | 29 | 33 | nan | nan | nan | Cerrado | 53.3 |
| 17d5d6cb-8180-3079-9d3a-3c037261b8c8 | -16.24866 | -41.73684 | 2026-10-08 15:39:00 | NOAA-21 | COMERCINHO | MINAS GERAIS | Brasil | 3117009 | 31 | 33 | nan | nan | nan | Mata Atlântica | 21.9 |
| 3d207d76-ce12-36b8-84b6-5f3c0fbe71b2 | -17.19607 | -40.07735 | 2026-10-08 15:39:00 | NOAA-21 | VEREDA | BAHIA | Brasil | 2933257 | 29 | 33 | nan | nan | nan | Mata Atlântica | 3.3 |
| b00cf277-dd16-39de-914e-488ab348a609 | -14.27153 | -40.80259 | 2026-10-08 15:39:00 | NOAA-21 | CAETANOS | BAHIA | Brasil | 2905156 | 29 | 33 | nan | nan | nan | Caatinga | 2.3 |
| 8a0bc80a-c080-3e6e-83e1-83e526b4083e | -13.85401 | -40.64726 | 2026-10-08 15:39:00 | NOAA-21 | MANOEL VITORINO | BAHIA | Brasil | 2920403 | 29 | 33 | nan | nan | nan | Caatinga | 8.7 |
| 89e90574-9fdb-34b8-bd90-de50067cfdf9 | -16.23445 | -40.15248 | 2026-10-08 15:39:00 | NOAA-21 | SANTA MARIA DO SALTO | MINAS GERAIS | Brasil | 3158102 | 31 | 33 | nan | nan | nan | Mata Atlântica | 11.9 |
| 7fc616ed-ece1-3bf3-801e-2be765030f06 | -15.31582 | -40.6465 | 2026-10-08 15:39:00 | NOAA-21 | RIBEIRÃO DO LARGO | BAHIA | Brasil | 2926657 | 29 | 33 | nan | nan | nan | Mata Atlântica | 13.4 |
| 6784a5d9-a501-324e-b5a7-da502fb64b06 | -15.94999 | -41.0951 | 2026-10-08 15:39:00 | NOAA-21 | PEDRA AZUL | MINAS GERAIS | Brasil | 3148707 | 31 | 33 | nan | nan | nan | Mata Atlântica | 42.2 |
| 1477a741-9ef6-39fc-8196-4d09132bd3a4 | -11.83352 | -43.5261 | 2026-10-08 15:39:00 | NOAA-21 | BARRA | BAHIA | Brasil | 2902708 | 29 | 33 | nan | nan | nan | Cerrado | 19.9 |
| 9c27d35e-026f-3ff9-97b2-d7f97f4dbbc2 | -14.858 | -42.06432 | 2026-10-08 15:39:00 | NOAA-21 | CONDEÚBA | BAHIA | Brasil | 2908705 | 29 | 33 | nan | nan | nan | Caatinga | 23.8 |
| 23d387fd-8f9a-3f90-9e27-6844657ae300 | -13.45361 | -41.92348 | 2026-10-08 15:39:00 | NOAA-21 | RIO DE CONTAS | BAHIA | Brasil | 2926707 | 29 | 33 | nan | nan | nan | Caatinga | 9.4 |
| c2148040-5810-316d-b4c9-dc0175faf82b | -12.13351 | -43.31615 | 2026-10-08 15:39:00 | NOAA-21 | MUQUÉM DO SÃO FRANCISCO | BAHIA | Brasil | 2922250 | 29 | 33 | nan | nan | nan | Cerrado | 56.5 |
| fd929565-ee44-3e64-8773-6b3d66077695 | -17.94451 | -42.31698 | 2026-10-08 15:39:00 | NOAA-21 | ÁGUA BOA | MINAS GERAIS | Brasil | 3100609 | 31 | 33 | nan | nan | nan | Mata Atlântica | 6.4 |
| ab756684-db3a-3a85-b1d2-6652d0840fc1 | -11.76586 | -45.52666 | 2026-10-08 15:39:00 | NOAA-21 | RIACHÃO DAS NEVES | BAHIA | Brasil | 2926202 | 29 | 33 | nan | nan | nan | Cerrado | 35.7 |
| 72e133b0-c57c-3ceb-a6c9-a5cdd8440143 | -16.46109 | -41.25727 | 2026-10-08 15:39:00 | NOAA-21 | JEQUITINHONHA | MINAS GERAIS | Brasil | 3135803 | 31 | 33 | nan | nan | nan | Mata Atlântica | 14.2 |
| be8d653d-6418-3362-ab4f-41a17f495d97 | -15.06671 | -41.35195 | 2026-10-08 15:39:00 | NOAA-21 | TREMEDAL | BAHIA | Brasil | 2931806 | 29 | 33 | nan | nan | nan | Mata Atlântica | 9.7 |
| 5cf40e10-3b54-313f-b3bb-d198c2f24457 | -12.32769 | -38.93459 | 2026-10-08 15:39:00 | NOAA-21 | FEIRA DE SANTANA | BAHIA | Brasil | 2910800 | 29 | 33 | nan | nan | nan | Mata Atlântica | 2.7 |
| d296a753-9caf-3b71-b7db-57805cf69f32 | -11.77293 | -45.52706 | 2026-10-08 15:39:00 | NOAA-21 | RIACHÃO DAS NEVES | BAHIA | Brasil | 2926202 | 29 | 33 | nan | nan | nan | Cerrado | 35.7 |
| 0232a56a-8d35-33a3-ad77-5901529c6337 | -13.96987 | -44.85032 | 2026-10-08 15:39:00 | NOAA-21 | COCOS | BAHIA | Brasil | 2908101 | 29 | 33 | nan | nan | nan | Cerrado | 13.7 |
| 5a22f847-2e53-3bac-927f-d0b68a716eeb | -11.76791 | -45.54544 | 2026-10-08 15:39:00 | NOAA-21 | RIACHÃO DAS NEVES | BAHIA | Brasil | 2926202 | 29 | 33 | nan | nan | nan | Cerrado | 38.7 |
| ed9fd060-a56f-37ea-9aab-cf325f565b94 | -14.63013 | -43.6851 | 2026-10-08 15:39:00 | NOAA-21 | MALHADA | BAHIA | Brasil | 2920205 | 29 | 33 | nan | nan | nan | Cerrado | 18.5 |
| b68bca3e-0252-317b-8d9d-0db1844f2b3f | -12.029 | -43.43945 | 2026-10-08 15:39:00 | NOAA-21 | MUQUÉM DO SÃO FRANCISCO | BAHIA | Brasil | 2922250 | 29 | 33 | nan | nan | nan | Cerrado | 130.3 |
| b4425369-7de4-395c-97e1-c53018629ede | -11.60769 | -43.67247 | 2026-10-08 15:39:00 | NOAA-21 | BARRA | BAHIA | Brasil | 2902708 | 29 | 33 | nan | nan | nan | Cerrado | 25.3 |
| b5bc54ef-9c85-3262-bf0e-7a66d9561916 | -14.61635 | -41.73967 | 2026-10-08 15:39:00 | NOAA-21 | PRESIDENTE JÂNIO QUADROS | BAHIA | Brasil | 2925709 | 29 | 33 | nan | nan | nan | Caatinga | 6.4 |
| df864530-73ea-3568-958c-778374e45da3 | -13.34215 | -38.98424 | 2026-10-08 15:39:00 | NOAA-21 | VALENÇA | BAHIA | Brasil | 2932903 | 29 | 33 | nan | nan | nan | Mata Atlântica | 8.0 |
| 737cfecd-8249-3d3d-b5bd-4be588a86880 | -11.61563 | -43.63372 | 2026-10-08 15:39:00 | NOAA-21 | BARRA | BAHIA | Brasil | 2902708 | 29 | 33 | nan | nan | nan | Cerrado | 35.4 |
| eebeb5e6-b037-347c-a05d-39554dba03b4 | -17.69636 | -39.16853 | 2026-10-08 15:39:00 | NOAA-21 | CARAVELAS | BAHIA | Brasil | 2906907 | 29 | 33 | nan | nan | nan | Mata Atlântica | 6.8 |
| 47619294-a846-36f3-a09f-cb3300737c24 | -11.82383 | -39.19275 | 2026-10-08 15:39:00 | NOAA-21 | CANDEAL | BAHIA | Brasil | 2906402 | 29 | 33 | nan | nan | nan | Caatinga | 13.3 |
| 590c383b-9f11-3158-8d97-ded278ada449 | -12.8329 | -44.44527 | 2026-10-08 15:39:00 | NOAA-21 | BAIANÓPOLIS | BAHIA | Brasil | 2902500 | 29 | 33 | nan | nan | nan | Cerrado | 24.0 |
| 6fb1a671-364a-327d-b2ad-1dfb9babef85 | -15.11154 | -43.63274 | 2026-10-08 15:39:00 | NOAA-21 | JAÍBA | MINAS GERAIS | Brasil | 3135050 | 31 | 33 | nan | nan | nan | Caatinga | 23.7 |
| 5f9ea079-5e9f-3024-8e63-68bf901b21f1 | -14.98081 | -41.23912 | 2026-10-08 15:39:00 | NOAA-21 | TREMEDAL | BAHIA | Brasil | 2931806 | 29 | 33 | nan | nan | nan | Mata Atlântica | 8.5 |
| 1dee732a-7514-366d-b616-8e6a623e7312 | -11.70951 | -40.58662 | 2026-10-08 15:39:00 | NOAA-21 | PIRITIBA | BAHIA | Brasil | 2924801 | 29 | 33 | nan | nan | nan | Caatinga | 2.1 |
| 2b38d41e-49c4-3153-9d15-4b3f97433576 | -14.09664 | -42.48051 | 2026-10-08 15:39:00 | NOAA-21 | CAETITÉ | BAHIA | Brasil | 2905206 | 29 | 33 | nan | nan | nan | Caatinga | 3.7 |
| fc915b7a-fecc-3b7f-8882-021216f5c480 | -14.09739 | -41.19942 | 2026-10-08 15:39:00 | NOAA-21 | TANHAÇU | BAHIA | Brasil | 2931004 | 29 | 33 | nan | nan | nan | Caatinga | 3.3 |
| 977df213-0fcf-3c6d-b3ba-89280c3de94a | -12.13891 | -43.31503 | 2026-10-08 15:39:00 | NOAA-21 | MUQUÉM DO SÃO FRANCISCO | BAHIA | Brasil | 2922250 | 29 | 33 | nan | nan | nan | Cerrado | 21.5 |
| 7fdcad58-9073-340d-8130-5e798ec46ed5 | -11.85363 | -43.53904 | 2026-10-08 15:39:00 | NOAA-21 | BARRA | BAHIA | Brasil | 2902708 | 29 | 33 | nan | nan | nan | Cerrado | 41.3 |
| f14f464c-c273-3eb1-a410-7df72c9aa489 | -16.11359 | -40.79683 | 2026-10-08 15:39:00 | NOAA-21 | ALMENARA | MINAS GERAIS | Brasil | 3101706 | 31 | 33 | nan | nan | nan | Mata Atlântica | 3.3 |


[Clique aqui para ver as próximas entradas](README231.md)
