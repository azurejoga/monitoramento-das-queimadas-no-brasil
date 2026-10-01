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

## Dados Diários - Página 110

| ID | Latitude | Longitude | Data/Hora GMT | Satélite | Município | Estado | País | Município ID | Estado ID | País ID | Dias sem Chuva | Precipitação | Risco de Fogo | Bioma | FRP |
|----|----------|-----------|---------------|----------|-----------|--------|------|--------------|-----------|---------|----------------|--------------|----------------|-------|-----|
| 63f3dcaa-a3cf-380d-abc8-7c2d0d300428 | -15.15674 | -46.14072 | 2026-10-01 16:11:00 | NOAA-21 | FORMOSO | MINAS GERAIS | Brasil | 3126208 | 31 | 33 | nan | nan | nan | Cerrado | 9.4 |
| 5caedb34-191a-3b8d-83dd-4b9f7e83ee21 | -15.76756 | -40.77797 | 2026-10-01 16:11:00 | NOAA-21 | DIVISÓPOLIS | MINAS GERAIS | Brasil | 3122454 | 31 | 33 | nan | nan | nan | Mata Atlântica | 10.8 |
| 455420f1-e108-3949-a862-903ab23e83b4 | -14.36987 | -44.75998 | 2026-10-01 16:11:00 | NOAA-21 | COCOS | BAHIA | Brasil | 2908101 | 29 | 33 | nan | nan | nan | Cerrado | 7.9 |
| cffbe13e-c409-32d4-b83c-96d82765d0ea | -14.50722 | -41.35723 | 2026-10-01 16:11:00 | NOAA-21 | ARACATU | BAHIA | Brasil | 2902005 | 29 | 33 | nan | nan | nan | Caatinga | 10.4 |
| 4c4cf166-2a81-31f1-b4cc-19ae29cd76cb | -14.65555 | -41.00586 | 2026-10-01 16:11:00 | NOAA-21 | ANAGÉ | BAHIA | Brasil | 2901205 | 29 | 33 | nan | nan | nan | Caatinga | 8.7 |
| 23b2c8a7-2a7b-3d65-8b1c-0e041577c2b4 | -14.88298 | -40.4087 | 2026-10-01 16:11:00 | NOAA-21 | CAATIBA | BAHIA | Brasil | 2904803 | 29 | 33 | nan | nan | nan | Mata Atlântica | 4.9 |
| a3300c6d-fd57-3c1c-8939-baa38e0f2112 | -15.97428 | -41.77487 | 2026-10-01 16:11:00 | NOAA-21 | SANTA CRUZ DE SALINAS | MINAS GERAIS | Brasil | 3157377 | 31 | 33 | nan | nan | nan | Mata Atlântica | 12.0 |
| dc138f4a-39c0-3be3-adcd-feeb87249c94 | -15.9738 | -41.77456 | 2026-10-01 16:11:00 | NOAA-21 | SANTA CRUZ DE SALINAS | MINAS GERAIS | Brasil | 3157377 | 31 | 33 | nan | nan | nan | Mata Atlântica | 13.6 |
| 4f002740-3bda-3414-bc66-e077e0754183 | -16.55954 | -44.80357 | 2026-10-01 16:11:00 | NOAA-21 | PONTO CHIQUE | MINAS GERAIS | Brasil | 3152131 | 31 | 33 | nan | nan | nan | Cerrado | 26.2 |
| c684b20e-1765-3411-aaf5-384acb0b5869 | -15.76664 | -46.04851 | 2026-10-01 16:11:00 | NOAA-21 | ARINOS | MINAS GERAIS | Brasil | 3104502 | 31 | 33 | nan | nan | nan | Cerrado | 10.1 |
| 94027853-fc64-3787-92f1-a23e9953b142 | -15.41816 | -41.21959 | 2026-10-01 16:11:00 | NOAA-21 | CÂNDIDO SALES | BAHIA | Brasil | 2906709 | 29 | 33 | nan | nan | nan | Mata Atlântica | 102.4 |
| 92ba27b1-6ef2-37a5-b919-5d6d8bad10b7 | -15.65272 | -44.71366 | 2026-10-01 16:11:00 | NOAA-21 | JANUÁRIA | MINAS GERAIS | Brasil | 3135209 | 31 | 33 | nan | nan | nan | Cerrado | 15.2 |
| 81f8132c-8009-3bb8-a9bb-93ab4f23f5af | -15.62657 | -49.26714 | 2026-10-01 16:11:00 | NOAA-21 | JARAGUÁ | GOIÁS | Brasil | 5211800 | 52 | 33 | nan | nan | nan | Cerrado | 72.3 |
| e4841f17-c75a-3686-ba31-42472208fc05 | -14.36578 | -44.76054 | 2026-10-01 16:11:00 | NOAA-21 | COCOS | BAHIA | Brasil | 2908101 | 29 | 33 | nan | nan | nan | Cerrado | 7.9 |
| d4ee854a-32f3-3d38-aeb6-c04ff5dc4a72 | -14.11807 | -40.01497 | 2026-10-01 16:11:00 | NOAA-21 | ITAGI | BAHIA | Brasil | 2915106 | 29 | 33 | nan | nan | nan | Mata Atlântica | 15.4 |
| 0b29be4b-7c1d-3b54-a757-e5460effda66 | -15.66053 | -44.70867 | 2026-10-01 16:11:00 | NOAA-21 | JANUÁRIA | MINAS GERAIS | Brasil | 3135209 | 31 | 33 | nan | nan | nan | Cerrado | 80.0 |
| 4f9c1e99-1e40-3f3e-a5f4-3d0138ae4082 | -15.59927 | -41.16566 | 2026-10-01 16:11:00 | NOAA-21 | ENCRUZILHADA | BAHIA | Brasil | 2910404 | 29 | 33 | nan | nan | nan | Mata Atlântica | 9.2 |
| 57c78f06-0044-34b4-bfc3-8853e2d971b3 | -14.72807 | -41.92752 | 2026-10-01 16:11:00 | NOAA-21 | CONDEÚBA | BAHIA | Brasil | 2908705 | 29 | 33 | nan | nan | nan | Caatinga | 29.0 |
| 867da4d5-d09c-3c66-a2bf-8d11c1a2f956 | -15.59616 | -49.19895 | 2026-10-01 16:11:00 | NOAA-21 | JARAGUÁ | GOIÁS | Brasil | 5211800 | 52 | 33 | nan | nan | nan | Cerrado | 34.8 |
| f83200e7-68e8-3c1d-bef9-3ae867f58c79 | -14.32579 | -44.98934 | 2026-10-01 16:11:00 | NOAA-21 | COCOS | BAHIA | Brasil | 2908101 | 29 | 33 | nan | nan | nan | Cerrado | 5.2 |
| 911d0820-0ff1-3406-8554-fef8e8063218 | -15.15611 | -46.13586 | 2026-10-01 16:11:00 | NOAA-21 | FORMOSO | MINAS GERAIS | Brasil | 3126208 | 31 | 33 | nan | nan | nan | Cerrado | 4.8 |
| f66cd9d0-04c7-3442-94a2-f84fb426d76f | -14.77724 | -40.33567 | 2026-10-01 16:11:00 | NOAA-21 | PLANALTO | BAHIA | Brasil | 2925006 | 29 | 33 | nan | nan | nan | Mata Atlântica | 10.5 |
| 5095a73f-e29d-3bad-ae4b-49d348800b6b | -15.72576 | -41.19324 | 2026-10-01 16:11:00 | NOAA-21 | ENCRUZILHADA | BAHIA | Brasil | 2910404 | 29 | 33 | nan | nan | nan | Mata Atlântica | 21.5 |
| 0403237a-dc71-3a6b-91a5-05e1cdbdb8fe | -15.68108 | -40.59599 | 2026-10-01 16:11:00 | NOAA-21 | ENCRUZILHADA | BAHIA | Brasil | 2910404 | 29 | 33 | nan | nan | nan | Mata Atlântica | 12.4 |
| 0f51908a-2a99-3370-afe9-9d7d7c667119 | -14.67513 | -44.68377 | 2026-10-01 16:11:00 | NOAA-21 | CÔNEGO MARINHO | MINAS GERAIS | Brasil | 3117836 | 31 | 33 | nan | nan | nan | Cerrado | 3.4 |
| fe4650d6-bd62-33a0-acc9-2581346898b1 | -14.50626 | -45.21306 | 2026-10-01 16:11:00 | NOAA-21 | COCOS | BAHIA | Brasil | 2908101 | 29 | 33 | nan | nan | nan | Cerrado | 7.7 |
| 8cf0db60-d5ac-3023-861d-1bb3080699d0 | -15.85299 | -41.7121 | 2026-10-01 16:11:00 | NOAA-21 | CURRAL DE DENTRO | MINAS GERAIS | Brasil | 3120870 | 31 | 33 | nan | nan | nan | Mata Atlântica | 3.3 |
| fe71730b-431c-32cd-b0b5-a09dfa3c5ae7 | -16.20174 | -42.87184 | 2026-10-01 16:11:00 | NOAA-21 | GRÃO MOGOL | MINAS GERAIS | Brasil | 3127800 | 31 | 33 | nan | nan | nan | Cerrado | 6.9 |
| 661994ac-124c-3ac5-bbe7-15a00c5a321c | -15.64759 | -44.70649 | 2026-10-01 16:11:00 | NOAA-21 | JANUÁRIA | MINAS GERAIS | Brasil | 3135209 | 31 | 33 | nan | nan | nan | Cerrado | 17.7 |
| 99c1a588-2c4d-38be-8c29-6328d896f2c0 | -15.96144 | -40.5223 | 2026-10-01 16:11:00 | NOAA-21 | ALMENARA | MINAS GERAIS | Brasil | 3101706 | 31 | 33 | nan | nan | nan | Mata Atlântica | 25.5 |
| 95afe1c6-b7e3-3c6e-a591-faa8946d7376 | -14.36007 | -44.78075 | 2026-10-01 16:11:00 | NOAA-21 | COCOS | BAHIA | Brasil | 2908101 | 29 | 33 | nan | nan | nan | Cerrado | 12.8 |
| 559f593d-f64c-3748-b956-3d18e755c5d3 | -14.88843 | -41.65329 | 2026-10-01 16:11:00 | NOAA-21 | PRESIDENTE JÂNIO QUADROS | BAHIA | Brasil | 2925709 | 29 | 33 | nan | nan | nan | Caatinga | 151.8 |
| fc8e555c-4c7d-3bd5-961d-337264d0046f | -14.97208 | -46.26254 | 2026-10-01 16:11:00 | NOAA-21 | FORMOSO | MINAS GERAIS | Brasil | 3126208 | 31 | 33 | nan | nan | nan | Cerrado | 15.2 |
| 6f68fd06-2653-3216-9937-bbf469c4de40 | -15.25078 | -40.90736 | 2026-10-01 16:11:00 | NOAA-21 | VITÓRIA DA CONQUISTA | BAHIA | Brasil | 2933307 | 29 | 33 | nan | nan | nan | Mata Atlântica | 8.3 |
| 7a4ae61a-9772-37d2-a290-36e4def60eaf | -15.09845 | -44.00712 | 2026-10-01 16:11:00 | NOAA-21 | JAÍBA | MINAS GERAIS | Brasil | 3135050 | 31 | 33 | nan | nan | nan | Cerrado | 17.0 |
| 7de524a5-d1a2-31fe-8168-d0702e7408b9 | -15.0918 | -41.35914 | 2026-10-01 16:11:00 | NOAA-21 | TREMEDAL | BAHIA | Brasil | 2931806 | 29 | 33 | nan | nan | nan | Mata Atlântica | 3.5 |
| 71f10cb0-cf28-3568-b875-c5bd9222435f | -15.77485 | -46.03096 | 2026-10-01 16:11:00 | NOAA-21 | ARINOS | MINAS GERAIS | Brasil | 3104502 | 31 | 33 | nan | nan | nan | Cerrado | 9.7 |
| bdea9ed2-8002-322e-9ada-d507281e7ba5 | -15.85733 | -41.71267 | 2026-10-01 16:11:00 | NOAA-21 | CURRAL DE DENTRO | MINAS GERAIS | Brasil | 3120870 | 31 | 33 | nan | nan | nan | Mata Atlântica | 17.9 |
| fdc54213-b1e8-33b2-878f-811bef084145 | -15.24743 | -46.15493 | 2026-10-01 16:11:00 | NOAA-21 | FORMOSO | MINAS GERAIS | Brasil | 3126208 | 31 | 33 | nan | nan | nan | Cerrado | 34.6 |
| 8190fab0-67f6-312e-83c5-972737862c32 | -14.48238 | -41.54898 | 2026-10-01 16:11:00 | NOAA-21 | ARACATU | BAHIA | Brasil | 2902005 | 29 | 33 | nan | nan | nan | Caatinga | 6.3 |
| e140e0cd-7538-3a9c-a693-6304a96ee2e8 | -15.25341 | -46.15528 | 2026-10-01 16:11:00 | NOAA-21 | FORMOSO | MINAS GERAIS | Brasil | 3126208 | 31 | 33 | nan | nan | nan | Cerrado | 32.7 |
| df7c8cd1-9918-3d89-a32a-31cbea22a24c | -14.77833 | -40.34293 | 2026-10-01 16:11:00 | NOAA-21 | PLANALTO | BAHIA | Brasil | 2925006 | 29 | 33 | nan | nan | nan | Mata Atlântica | 4.4 |
| 365e8517-335b-35ee-8cd6-dc4ec420960d | -14.66857 | -40.70713 | 2026-10-01 16:11:00 | NOAA-21 | VITÓRIA DA CONQUISTA | BAHIA | Brasil | 2933307 | 29 | 33 | nan | nan | nan | Mata Atlântica | 10.5 |
| a373d941-8da8-3de4-badb-28d59b609cbf | -15.4216 | -41.21909 | 2026-10-01 16:11:00 | NOAA-21 | CÂNDIDO SALES | BAHIA | Brasil | 2906709 | 29 | 33 | nan | nan | nan | Mata Atlântica | 102.4 |
| dbc23712-7798-35ed-8e1e-1605161f0ee2 | -14.37964 | -40.35834 | 2026-10-01 16:11:00 | NOAA-21 | BOA NOVA | BAHIA | Brasil | 2903706 | 29 | 33 | nan | nan | nan | Mata Atlântica | 6.0 |
| 2421365b-77e2-35fc-a6cf-12b7740c8c73 | -14.37104 | -44.7371 | 2026-10-01 16:11:00 | NOAA-21 | COCOS | BAHIA | Brasil | 2908101 | 29 | 33 | nan | nan | nan | Cerrado | 20.6 |
| 1bc17d1f-3136-3ade-bfb9-a7f496f76a57 | -14.41684 | -40.35617 | 2026-10-01 16:11:00 | NOAA-21 | POÇÕES | BAHIA | Brasil | 2925105 | 29 | 33 | nan | nan | nan | Mata Atlântica | 3.5 |
| b8b86d9a-c13b-3715-8fdc-fc9401b3e4cc | -14.42671 | -43.83766 | 2026-10-01 16:11:00 | NOAA-21 | MANGA | MINAS GERAIS | Brasil | 3139300 | 31 | 33 | nan | nan | nan | Cerrado | 38.9 |
| 34479d45-8de7-30d2-8e8d-5f4cf5352388 | -13.95647 | -39.30764 | 2026-10-01 16:11:00 | NOAA-21 | CAMAMU | BAHIA | Brasil | 2905800 | 29 | 33 | nan | nan | nan | Mata Atlântica | 10.4 |
| 7f07fc37-4859-3981-a557-9a32b293b75e | -14.33645 | -39.32467 | 2026-10-01 16:11:00 | NOAA-21 | AURELINO LEAL | BAHIA | Brasil | 2902401 | 29 | 33 | nan | nan | nan | Mata Atlântica | 9.2 |
| 791305a5-589a-3a50-9b2c-1e5585846c8f | -14.35234 | -45.22386 | 2026-10-01 16:11:00 | NOAA-21 | COCOS | BAHIA | Brasil | 2908101 | 29 | 33 | nan | nan | nan | Cerrado | 19.7 |
| b5a028d5-4c73-367d-9511-934d6e75ada4 | -14.6291 | -42.64053 | 2026-10-01 16:11:00 | NOAA-21 | URANDI | BAHIA | Brasil | 2932606 | 29 | 33 | nan | nan | nan | Cerrado | 21.5 |
| d02f5562-f21b-3291-85af-71a3285c0e63 | -14.7156 | -41.03056 | 2026-10-01 16:11:00 | NOAA-21 | ANAGÉ | BAHIA | Brasil | 2901205 | 29 | 33 | nan | nan | nan | Caatinga | 65.9 |
| c26f83e5-cab9-3abe-9f7a-df9849872140 | -14.91074 | -39.28127 | 2026-10-01 16:11:00 | NOAA-21 | ITABUNA | BAHIA | Brasil | 2914802 | 29 | 33 | nan | nan | nan | Mata Atlântica | 4.8 |
| f9fa6da1-7761-3b16-ab93-3ac3a5ee78ee | -14.50135 | -41.21832 | 2026-10-01 16:11:00 | NOAA-21 | ARACATU | BAHIA | Brasil | 2902005 | 29 | 33 | nan | nan | nan | Caatinga | 5.3 |
| ac52b589-9e1a-3c71-b1ff-9d47afe15cbf | -15.70746 | -40.48221 | 2026-10-01 16:11:00 | NOAA-21 | MACARANI | BAHIA | Brasil | 2919702 | 29 | 33 | nan | nan | nan | Mata Atlântica | 2.8 |
| 22cc5dbc-371b-3414-a162-d10bdd7ed8c7 | -15.68054 | -40.59225 | 2026-10-01 16:11:00 | NOAA-21 | ENCRUZILHADA | BAHIA | Brasil | 2910404 | 29 | 33 | nan | nan | nan | Mata Atlântica | 12.4 |
| 536edbce-01a3-3d6b-8523-2edf9b26b460 | -15.50292 | -41.47472 | 2026-10-01 16:11:00 | NOAA-21 | NINHEIRA | MINAS GERAIS | Brasil | 3144656 | 31 | 33 | nan | nan | nan | Mata Atlântica | 9.1 |
| b7bc19ca-144a-368c-a726-beb2a6de3e74 | -15.15781 | -46.13828 | 2026-10-01 16:11:00 | NOAA-21 | FORMOSO | MINAS GERAIS | Brasil | 3126208 | 31 | 33 | nan | nan | nan | Cerrado | 21.7 |
| 84116492-dfc5-3479-90f5-78c0613508eb | -15.00452 | -41.7089 | 2026-10-01 16:11:00 | NOAA-21 | PIRIPÁ | BAHIA | Brasil | 2924702 | 29 | 33 | nan | nan | nan | Mata Atlântica | 10.4 |
| 14bbe47c-0799-35df-8056-be2be949041a | -13.79264 | -41.1382 | 2026-10-01 16:11:00 | NOAA-21 | CONTENDAS DO SINCORÁ | BAHIA | Brasil | 2908804 | 29 | 33 | nan | nan | nan | Caatinga | 5.1 |
| 9b373217-03a1-34a9-9099-a9697e5213bb | -13.57823 | -39.3009 | 2026-10-01 16:11:00 | NOAA-21 | TAPEROÁ | BAHIA | Brasil | 2931202 | 29 | 33 | nan | nan | nan | Mata Atlântica | 3.7 |
| 9bc26453-32ae-3f50-ac41-4c456de5b663 | -14.64215 | -44.6845 | 2026-10-01 16:11:00 | NOAA-21 | CÔNEGO MARINHO | MINAS GERAIS | Brasil | 3117836 | 31 | 33 | nan | nan | nan | Cerrado | 12.7 |
| df422506-e25e-3dd4-8ce2-f0b49be28e77 | -14.37757 | -44.75521 | 2026-10-01 16:11:00 | NOAA-21 | COCOS | BAHIA | Brasil | 2908101 | 29 | 33 | nan | nan | nan | Cerrado | 15.3 |
| 75180784-67b0-304d-a170-7ab516c8a77e | -16.18804 | -42.8832 | 2026-10-01 16:11:00 | NOAA-21 | GRÃO MOGOL | MINAS GERAIS | Brasil | 3127800 | 31 | 33 | nan | nan | nan | Cerrado | 1.9 |
| 7c4ce6da-bcc2-3f48-9845-f785da550b94 | -14.24059 | -42.03416 | 2026-10-01 16:11:00 | NOAA-21 | RIO DO ANTÔNIO | BAHIA | Brasil | 2926806 | 29 | 33 | nan | nan | nan | Caatinga | 7.6 |
| 6775e989-57ff-3bec-ac83-886e22945a95 | -14.15946 | -39.14651 | 2026-10-01 16:11:00 | NOAA-21 | MARAÚ | BAHIA | Brasil | 2920700 | 29 | 33 | nan | nan | nan | Mata Atlântica | 7.3 |
| 11c4644d-1e06-3819-acc5-04634bff47cd | -15.96645 | -45.9654 | 2026-10-01 16:11:00 | NOAA-21 | ARINOS | MINAS GERAIS | Brasil | 3104502 | 31 | 33 | nan | nan | nan | Cerrado | 8.6 |
| ed129a79-f9f5-3dae-b963-34f3ef3e3360 | -13.83645 | -39.67855 | 2026-10-01 16:11:00 | NOAA-21 | ITAMARI | BAHIA | Brasil | 2915700 | 29 | 33 | nan | nan | nan | Mata Atlântica | 5.6 |
| 319fd845-6e0e-387b-8d88-57018b6c5b24 | -14.36891 | -44.75261 | 2026-10-01 16:11:00 | NOAA-21 | COCOS | BAHIA | Brasil | 2908101 | 29 | 33 | nan | nan | nan | Cerrado | 9.6 |
| 2c329b67-88c9-338a-acb6-d186ede12d12 | -14.87019 | -49.2155 | 2026-10-01 16:11:00 | NOAA-21 | SÃO LUIZ DO NORTE | GOIÁS | Brasil | 5220157 | 52 | 33 | nan | nan | nan | Cerrado | 13.0 |
| d76bcdac-a285-3015-8abe-0ff5ca0413d4 | -15.34489 | -42.79665 | 2026-10-01 16:11:00 | NOAA-21 | MONTE AZUL | MINAS GERAIS | Brasil | 3142908 | 31 | 33 | nan | nan | nan | Cerrado | 16.6 |
| 25e2adf6-ad77-38f4-9fe9-ca55a7e29376 | -15.25194 | -46.15413 | 2026-10-01 16:11:00 | NOAA-21 | FORMOSO | MINAS GERAIS | Brasil | 3126208 | 31 | 33 | nan | nan | nan | Cerrado | 23.9 |
| f480a63d-9f5f-3e48-80ad-0746922bc9bb | -13.89937 | -39.6468 | 2026-10-01 16:11:00 | NOAA-21 | IBIRATAIA | BAHIA | Brasil | 2912905 | 29 | 33 | nan | nan | nan | Mata Atlântica | 3.5 |
| f72a4a7d-ac2b-3c35-a819-9b4d1c642480 | -14.36842 | -44.7489 | 2026-10-01 16:11:00 | NOAA-21 | COCOS | BAHIA | Brasil | 2908101 | 29 | 33 | nan | nan | nan | Cerrado | 9.6 |
| 7c8ad9ce-1d0a-3521-b8b7-df598371f3b8 | -15.68447 | -40.59553 | 2026-10-01 16:11:00 | NOAA-21 | ENCRUZILHADA | BAHIA | Brasil | 2910404 | 29 | 33 | nan | nan | nan | Mata Atlântica | 12.4 |
| 5cfe3c22-bc3c-355c-ba17-c0474d4a036b | -15.22169 | -47.93918 | 2026-10-01 16:11:00 | NOAA-21 | PLANALTINA | GOIÁS | Brasil | 5217609 | 52 | 33 | nan | nan | nan | Cerrado | 5.3 |
| b1ff3f38-47f6-3b3b-bfab-ed8188fe9149 | -15.0981 | -41.11127 | 2026-10-01 16:11:00 | NOAA-21 | BELO CAMPO | BAHIA | Brasil | 2903508 | 29 | 33 | nan | nan | nan | Mata Atlântica | 10.4 |
| 568e8b3e-f167-3e4b-af84-3c67d64cf345 | -15.34122 | -42.7972 | 2026-10-01 16:11:00 | NOAA-21 | MONTE AZUL | MINAS GERAIS | Brasil | 3142908 | 31 | 33 | nan | nan | nan | Cerrado | 150.7 |
| 150abc44-a34a-3b14-b672-808ba2344174 | -15.26779 | -40.90497 | 2026-10-01 16:11:00 | NOAA-21 | VITÓRIA DA CONQUISTA | BAHIA | Brasil | 2933307 | 29 | 33 | nan | nan | nan | Mata Atlântica | 9.3 |
| dfe17710-5d01-39d8-9214-b84158617089 | -16.00527 | -44.10131 | 2026-10-01 16:11:00 | NOAA-21 | SÃO JOÃO DA PONTE | MINAS GERAIS | Brasil | 3162401 | 31 | 33 | nan | nan | nan | Cerrado | 15.3 |
| 7760dd02-07fe-3e19-a4ce-44787729fb35 | -14.49971 | -40.5057 | 2026-10-01 16:11:00 | NOAA-21 | POÇÕES | BAHIA | Brasil | 2925105 | 29 | 33 | nan | nan | nan | Mata Atlântica | 3.4 |
| 2cb7bc68-3c0e-3965-81f2-6076a28630ed | -15.65638 | -44.70922 | 2026-10-01 16:11:00 | NOAA-21 | JANUÁRIA | MINAS GERAIS | Brasil | 3135209 | 31 | 33 | nan | nan | nan | Cerrado | 15.2 |
| b3e0eefd-9540-340c-8ec3-76524f7f5f29 | -15.77789 | -46.02787 | 2026-10-01 16:11:00 | NOAA-21 | ARINOS | MINAS GERAIS | Brasil | 3104502 | 31 | 33 | nan | nan | nan | Cerrado | 18.6 |
| 77bd949e-d75b-3223-9f5b-1c6d6ed94681 | -14.35831 | -44.73508 | 2026-10-01 16:11:00 | NOAA-21 | COCOS | BAHIA | Brasil | 2908101 | 29 | 33 | nan | nan | nan | Cerrado | 9.2 |
| 2bec2e0e-6467-304e-98e7-fa7305f81ab7 | -16.1545 | -42.86014 | 2026-10-01 16:11:00 | NOAA-21 | RIACHO DOS MACHADOS | MINAS GERAIS | Brasil | 3154507 | 31 | 33 | nan | nan | nan | Cerrado | 4.3 |
| 83f3eaae-ce9b-3014-8b88-742c9c860605 | -14.91417 | -42.81274 | 2026-10-01 16:11:00 | NOAA-21 | ESPINOSA | MINAS GERAIS | Brasil | 3124302 | 31 | 33 | nan | nan | nan | Cerrado | 13.0 |
| 51557251-ef44-3ce6-940e-7d9cf7edfbd4 | -15.09987 | -48.40482 | 2026-10-01 16:11:00 | NOAA-21 | MIMOSO DE GOIÁS | GOIÁS | Brasil | 5213053 | 52 | 33 | nan | nan | nan | Cerrado | 58.3 |
| f56b6227-aaf3-3e41-b432-954e39bdf435 | -14.37153 | -44.74086 | 2026-10-01 16:11:00 | NOAA-21 | COCOS | BAHIA | Brasil | 2908101 | 29 | 33 | nan | nan | nan | Cerrado | 25.9 |
| 08d694b8-9e2f-3016-b085-8d4f343c55c1 | -15.10191 | -39.55631 | 2026-10-01 16:11:00 | NOAA-21 | JUSSARI | BAHIA | Brasil | 2918555 | 29 | 33 | nan | nan | nan | Mata Atlântica | 5.1 |
| 7ea37f4f-d8de-3da7-96d6-0fe1459e2dfd | -14.98041 | -41.29013 | 2026-10-01 16:11:00 | NOAA-21 | TREMEDAL | BAHIA | Brasil | 2931806 | 29 | 33 | nan | nan | nan | Mata Atlântica | 6.2 |
| 8018f2c5-0801-34a6-b3fe-24276921cc84 | -15.95283 | -45.96689 | 2026-10-01 16:11:00 | NOAA-21 | ARINOS | MINAS GERAIS | Brasil | 3104502 | 31 | 33 | nan | nan | nan | Cerrado | 72.7 |
| e8bca9a9-964e-331e-96e3-98dd3fffedc8 | -14.22332 | -40.79646 | 2026-10-01 16:11:00 | NOAA-21 | MIRANTE | BAHIA | Brasil | 2921450 | 29 | 33 | nan | nan | nan | Caatinga | 7.1 |
| 6a952ba3-4944-3829-b33b-3dcf41e4ccbb | -15.58888 | -40.73213 | 2026-10-01 16:11:00 | NOAA-21 | ENCRUZILHADA | BAHIA | Brasil | 2910404 | 29 | 33 | nan | nan | nan | Mata Atlântica | 51.0 |
| 9e0336e0-a3c0-305d-a9bc-70dc7bdb9233 | -14.3384 | -44.74173 | 2026-10-01 16:11:00 | NOAA-21 | COCOS | BAHIA | Brasil | 2908101 | 29 | 33 | nan | nan | nan | Cerrado | 7.2 |
| b98ca610-6666-3945-a17e-76910bb56a78 | -14.65773 | -41.02075 | 2026-10-01 16:11:00 | NOAA-21 | ANAGÉ | BAHIA | Brasil | 2901205 | 29 | 33 | nan | nan | nan | Caatinga | 16.5 |
| e7bbcc0c-a656-350b-ad68-e0dc5d3fb2cb | -15.2173 | -47.94602 | 2026-10-01 16:11:00 | NOAA-21 | PLANALTINA | GOIÁS | Brasil | 5217609 | 52 | 33 | nan | nan | nan | Cerrado | 4.7 |
| 05e53f21-f9b2-3fac-8c6d-6c87a0f334a1 | -15.90899 | -42.53192 | 2026-10-01 16:11:00 | NOAA-21 | RIO PARDO DE MINAS | MINAS GERAIS | Brasil | 3155603 | 31 | 33 | nan | nan | nan | Cerrado | 7.7 |
| f439df6d-d52d-3d91-bb23-bf8b33bce49c | -14.97414 | -40.66339 | 2026-10-01 16:11:00 | NOAA-21 | BARRA DO CHOÇA | BAHIA | Brasil | 2902906 | 29 | 33 | nan | nan | nan | Mata Atlântica | 2.0 |
| a395215c-4325-3dd0-869c-cc7dd898967e | -14.34247 | -44.74111 | 2026-10-01 16:11:00 | NOAA-21 | COCOS | BAHIA | Brasil | 2908101 | 29 | 33 | nan | nan | nan | Cerrado | 7.2 |


[Clique aqui para ver as próximas entradas](README111.md)
