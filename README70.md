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

## Dados Diários - Página 70

| ID | Latitude | Longitude | Data/Hora GMT | Satélite | Município | Estado | País | Município ID | Estado ID | País ID | Dias sem Chuva | Precipitação | Risco de Fogo | Bioma | FRP |
|----|----------|-----------|---------------|----------|-----------|--------|------|--------------|-----------|---------|----------------|--------------|----------------|-------|-----|
| 1a099bec-1544-3455-8861-4851ec1c8d59 | -6.1763 | -45.23552 | 2026-08-20 11:34:00 | TERRA_M-M | FERNANDO FALCÃO | MARANHÃO | Brasil | 2104081 | 21 | 33 | nan | nan | nan | Cerrado | 6.2 |
| 2a31de74-4e42-3cba-82cd-36c285f2bc7d | -7.46346 | -45.14019 | 2026-08-20 11:34:00 | TERRA_M-M | LORETO | MARANHÃO | Brasil | 2106102 | 21 | 33 | nan | nan | nan | Cerrado | 8.5 |
| ee3979c6-378b-3547-a853-73dce3e89d1f | -6.89621 | -42.84943 | 2026-08-20 11:34:00 | TERRA_M-M | FLORIANO | PIAUÍ | Brasil | 2203909 | 22 | 33 | nan | nan | nan | Caatinga | 12.8 |
| 6f0e6656-b02b-3b3a-8417-10456902c0f2 | -6.17357 | -45.2542 | 2026-08-20 11:34:00 | TERRA_M-M | FERNANDO FALCÃO | MARANHÃO | Brasil | 2104081 | 21 | 33 | nan | nan | nan | Cerrado | 73.9 |
| 1a57f1f4-5c8e-3169-a3d9-90f317a4b202 | -7.01182 | -45.89376 | 2026-08-20 11:34:00 | TERRA_M-M | FORTALEZA DOS NOGUEIRAS | MARANHÃO | Brasil | 2104107 | 21 | 33 | nan | nan | nan | Cerrado | 9.8 |
| 1d6a5e34-efb1-36cb-be24-0b6479e8e950 | -6.29783 | -43.62918 | 2026-08-20 11:34:00 | TERRA_M-M | PASSAGEM FRANCA | MARANHÃO | Brasil | 2107902 | 21 | 33 | nan | nan | nan | Cerrado | 7.2 |
| 7484ddc5-043e-3854-85dc-85c6e43479f5 | -6.289 | -43.62794 | 2026-08-20 11:34:00 | TERRA_M-M | PASSAGEM FRANCA | MARANHÃO | Brasil | 2107902 | 21 | 33 | nan | nan | nan | Cerrado | 10.0 |
| 1b80d498-4900-32c8-86e4-8a58a7d452b5 | -5.60493 | -45.68178 | 2026-08-20 11:34:00 | TERRA_M-M | JENIPAPO DOS VIEIRAS | MARANHÃO | Brasil | 2105476 | 21 | 33 | nan | nan | nan | Cerrado | 7.7 |
| 1b658cdd-f8ff-3e1a-81ca-6198b20aa998 | -7.61705 | -45.15862 | 2026-08-20 11:34:00 | TERRA_M-M | RIBEIRO GONÇALVES | PIAUÍ | Brasil | 2208908 | 22 | 33 | nan | nan | nan | Cerrado | 8.6 |
| 859a4b2e-f8ce-362f-bf6b-9437c3b16229 | -6.17494 | -45.24487 | 2026-08-20 11:34:00 | TERRA_M-M | FERNANDO FALCÃO | MARANHÃO | Brasil | 2104081 | 21 | 33 | nan | nan | nan | Cerrado | 56.1 |
| 1a9e2a59-795c-3b6c-ab6a-da147963e490 | -7.61573 | -45.16775 | 2026-08-20 11:34:00 | TERRA_M-M | RIBEIRO GONÇALVES | PIAUÍ | Brasil | 2208908 | 22 | 33 | nan | nan | nan | Cerrado | 6.6 |
| 0e730802-2372-3beb-a409-9497f51235c9 | -7.15927 | -44.05459 | 2026-08-20 11:34:00 | TERRA_M-M | PORTO ALEGRE DO PIAUÍ | PIAUÍ | Brasil | 2208551 | 22 | 33 | nan | nan | nan | Cerrado | 10.3 |
| 02da1ff1-7879-33fe-87fd-c68c1e925a86 | -7.02106 | -45.89506 | 2026-08-20 11:34:00 | TERRA_M-M | FORTALEZA DOS NOGUEIRAS | MARANHÃO | Brasil | 2104107 | 21 | 33 | nan | nan | nan | Cerrado | 9.9 |
| 325bdabd-3e2e-34dd-a98a-42090b218cd7 | -6.26481 | -43.2756 | 2026-08-20 11:34:00 | TERRA_M-M | SÃO FRANCISCO DO MARANHÃO | MARANHÃO | Brasil | 2110906 | 21 | 33 | nan | nan | nan | Cerrado | 9.7 |
| cf6bbc06-c844-3fb5-b7d3-e23b5e9c525b | -5.64695 | -43.60307 | 2026-08-20 11:34:00 | TERRA_M-M | PARNARAMA | MARANHÃO | Brasil | 2107803 | 21 | 33 | nan | nan | nan | Cerrado | 9.1 |
| 70e7d547-ad53-3d9a-894f-f101307df037 | -7.34347 | -45.82869 | 2026-08-20 11:34:00 | TERRA_M-M | BALSAS | MARANHÃO | Brasil | 2101400 | 21 | 33 | nan | nan | nan | Cerrado | 8.9 |
| 7e898c9b-736e-31b6-aa4e-4aaccae5eb39 | -3.43337 | -41.65169 | 2026-08-20 11:34:00 | TERRA_M-M | COCAL | PIAUÍ | Brasil | 2202703 | 22 | 33 | nan | nan | nan | Caatinga | 6.5 |
| 9f0ad5fb-6e54-3650-8c4c-27406fbf9053 | -7.99397 | -44.14687 | 2026-08-20 11:34:00 | TERRA_M-M | SEBASTIÃO LEAL | PIAUÍ | Brasil | 2210631 | 22 | 33 | nan | nan | nan | Cerrado | 12.9 |
| 3d8c874d-644e-3736-af4b-7b1108186225 | -5.611 | -45.68858 | 2026-08-20 11:34:00 | TERRA_M-M | JENIPAPO DOS VIEIRAS | MARANHÃO | Brasil | 2105476 | 21 | 33 | nan | nan | nan | Cerrado | 5.6 |
| ec9839c7-cecb-3c80-bea7-4fc4d6777dc4 | -7.46214 | -45.14926 | 2026-08-20 11:34:00 | TERRA_M-M | LORETO | MARANHÃO | Brasil | 2106102 | 21 | 33 | nan | nan | nan | Cerrado | 6.4 |
| 4fc697db-052a-3581-93db-6054cbd047dc | -3.96538 | -43.10795 | 2026-08-20 11:34:00 | TERRA_M-M | BURITI | MARANHÃO | Brasil | 2102200 | 21 | 33 | nan | nan | nan | Cerrado | 11.7 |
| ee5bf61f-14c1-3415-87aa-f84848d362bd | -5.29127 | -43.95062 | 2026-08-20 11:34:00 | TERRA_M-M | SENADOR ALEXANDRE COSTA | MARANHÃO | Brasil | 2111748 | 21 | 33 | nan | nan | nan | Cerrado | 5.5 |
| c8dc3180-e470-3783-82f5-0d58ca4a68ab | -6.27367 | -43.27683 | 2026-08-20 11:34:00 | TERRA_M-M | SÃO FRANCISCO DO MARANHÃO | MARANHÃO | Brasil | 2110906 | 21 | 33 | nan | nan | nan | Cerrado | 10.9 |
| 39c6bc4e-74ad-3237-84a5-c290e1ae268b | -7.96442 | -44.66712 | 2026-08-20 11:34:00 | TERRA_M-M | URUÇUÍ | PIAUÍ | Brasil | 2211209 | 22 | 33 | nan | nan | nan | Cerrado | 8.0 |
| c1fe2525-f1c7-33f5-b8fc-7ae7843e5827 | -10.41834 | -48.32761 | 2026-08-20 11:34:00 | TERRA_M-M | PORTO NACIONAL | TOCANTINS | Brasil | 1718204 | 17 | 33 | nan | nan | nan | Cerrado | 11.5 |
| 9df643c5-8b62-3f87-ae03-c211604e7127 | -11.38773 | -46.37478 | 2026-08-20 11:34:00 | TERRA_M-M | FORMOSA DO RIO PRETO | BAHIA | Brasil | 2911105 | 29 | 33 | nan | nan | nan | Cerrado | 14.2 |
| 6c8e9c33-55e1-3c06-9f28-dd97521aa26a | -8.2033 | -47.39288 | 2026-08-20 11:34:00 | TERRA_M-M | GOIATINS | TOCANTINS | Brasil | 1709005 | 17 | 33 | nan | nan | nan | Cerrado | 8.2 |
| 88345273-871b-35e2-96d4-48cf009f1272 | -9.74854 | -46.85563 | 2026-08-20 11:34:00 | TERRA_M-M | LIZARDA | TOCANTINS | Brasil | 1712405 | 17 | 33 | nan | nan | nan | Cerrado | 8.1 |
| 548c25da-34d4-3e3a-9e64-edfee897f171 | -9.80294 | -46.61647 | 2026-08-20 11:34:00 | TERRA_M-M | LIZARDA | TOCANTINS | Brasil | 1712405 | 17 | 33 | nan | nan | nan | Cerrado | 7.7 |
| 07ba51de-5184-321a-a5db-0b26929e9ca4 | -8.36858 | -46.33542 | 2026-08-20 11:34:00 | TERRA_M-M | BALSAS | MARANHÃO | Brasil | 2101400 | 21 | 33 | nan | nan | nan | Cerrado | 6.5 |
| cc414626-35c8-354a-990e-40a17ab83036 | -8.32343 | -46.51308 | 2026-08-20 11:34:00 | TERRA_M-M | RIACHÃO | MARANHÃO | Brasil | 2109502 | 21 | 33 | nan | nan | nan | Cerrado | 37.4 |
| 8800836f-62b0-367a-b771-b12376f40f86 | -11.3968 | -46.37612 | 2026-08-20 11:34:00 | TERRA_M-M | FORMOSA DO RIO PRETO | BAHIA | Brasil | 2911105 | 29 | 33 | nan | nan | nan | Cerrado | 12.2 |
| 9c56fa31-5fdb-3e02-9e70-7b569c36c733 | -8.71881 | -49.6131 | 2026-08-20 11:34:00 | TERRA_M-M | CONCEIÇÃO DO ARAGUAIA | PARÁ | Brasil | 1502707 | 15 | 33 | nan | nan | nan | Amazônia | 17.5 |
| f1554501-91e4-388c-88ec-976235ddf228 | -9.80997 | -46.61419 | 2026-08-20 11:34:00 | TERRA_M-M | LIZARDA | TOCANTINS | Brasil | 1712405 | 17 | 33 | nan | nan | nan | Cerrado | 4.8 |
| 0eb31425-7a46-3dcb-96c6-7e4e3c851043 | -11.37868 | -46.37335 | 2026-08-20 11:34:00 | TERRA_M-M | FORMOSA DO RIO PRETO | BAHIA | Brasil | 2911105 | 29 | 33 | nan | nan | nan | Cerrado | 24.1 |
| 3ba45d45-7d66-3ded-aead-3542f9b1e6a5 | -8.32493 | -46.50291 | 2026-08-20 11:34:00 | TERRA_M-M | RIACHÃO | MARANHÃO | Brasil | 2109502 | 21 | 33 | nan | nan | nan | Cerrado | 22.7 |
| 5b3716be-89ec-39c6-a64e-71cfef29fb42 | -8.485 | -46.95926 | 2026-08-20 11:34:00 | TERRA_M-M | CAMPOS LINDOS | TOCANTINS | Brasil | 1703842 | 17 | 33 | nan | nan | nan | Cerrado | 53.2 |
| b5636e03-d063-3825-a6a7-aa5a26990538 | -8.35927 | -46.3341 | 2026-08-20 11:34:00 | TERRA_M-M | BALSAS | MARANHÃO | Brasil | 2101400 | 21 | 33 | nan | nan | nan | Cerrado | 6.9 |
| 95950e0c-8928-3598-87fe-2fee9f284820 | -11.39818 | -46.3667 | 2026-08-20 11:34:00 | TERRA_M-M | FORMOSA DO RIO PRETO | BAHIA | Brasil | 2911105 | 29 | 33 | nan | nan | nan | Cerrado | 14.8 |
| 7c42b587-76da-3095-91d2-c21e7da8dd46 | -12.26572 | -45.03513 | 2026-08-20 11:34:00 | TERRA_M-M | BARREIRAS | BAHIA | Brasil | 2903201 | 29 | 33 | nan | nan | nan | Cerrado | 7.1 |
| 630986a4-5283-3b9b-a63f-a543fa2b2b55 | -8.46577 | -46.95637 | 2026-08-20 11:34:00 | TERRA_M-M | CAMPOS LINDOS | TOCANTINS | Brasil | 1703842 | 17 | 33 | nan | nan | nan | Cerrado | 9.8 |
| 4e6c6907-b15c-3967-b3bd-f3a3f1ff55fa | -11.37779 | -47.23143 | 2026-08-20 11:34:00 | TERRA_M-M | ALMAS | TOCANTINS | Brasil | 1700400 | 17 | 33 | nan | nan | nan | Cerrado | 7.6 |
| 7a70dfd9-0de4-3a30-9a56-f6ac647a0c5f | -11.38912 | -46.36533 | 2026-08-20 11:34:00 | TERRA_M-M | FORMOSA DO RIO PRETO | BAHIA | Brasil | 2911105 | 29 | 33 | nan | nan | nan | Cerrado | 16.0 |
| 5d4fd646-6e71-304e-a39e-d75928b85665 | -11.31845 | -45.21091 | 2026-08-20 11:34:00 | TERRA_M-M | FORMOSA DO RIO PRETO | BAHIA | Brasil | 2911105 | 29 | 33 | nan | nan | nan | Cerrado | 7.8 |
| 663e567e-706d-3da4-948f-26a43a681d94 | -11.64137 | -45.20306 | 2026-08-20 11:34:00 | TERRA_M-M | RIACHÃO DAS NEVES | BAHIA | Brasil | 2926202 | 29 | 33 | nan | nan | nan | Cerrado | 5.7 |
| fea340d8-a13b-37a4-b692-d95e083a4ddb | -9.80849 | -46.62402 | 2026-08-20 11:34:00 | TERRA_M-M | LIZARDA | TOCANTINS | Brasil | 1712405 | 17 | 33 | nan | nan | nan | Cerrado | 9.4 |
| 7e2ee309-ccb1-33b7-af85-bcdae038ec0e | -12.25861 | -43.15864 | 2026-08-20 11:34:00 | TERRA_M-M | IBOTIRAMA | BAHIA | Brasil | 2913200 | 29 | 33 | nan | nan | nan | Caatinga | 10.2 |
| 98d09183-5da2-3030-819d-da4b3e38cef4 | -12.24802 | -43.16724 | 2026-08-20 11:34:00 | TERRA_M-M | IBOTIRAMA | BAHIA | Brasil | 2913200 | 29 | 33 | nan | nan | nan | Caatinga | 7.5 |
| bd1e0d19-3a3d-3fbb-95a0-e490195b3b5e | -9.75006 | -46.84536 | 2026-08-20 11:34:00 | TERRA_M-M | LIZARDA | TOCANTINS | Brasil | 1712405 | 17 | 33 | nan | nan | nan | Cerrado | 13.2 |
| 2c46242e-79ef-347a-a33d-6c8c7fe64bca | -15.32198 | -44.17916 | 2026-08-20 11:36:00 | TERRA_M-M | JANUÁRIA | MINAS GERAIS | Brasil | 3135209 | 31 | 33 | nan | nan | nan | Caatinga | 5.9 |
| 40d55877-7b0c-37c2-97f6-c37133018312 | -14.4108 | -45.50578 | 2026-08-20 11:36:00 | TERRA_M-M | COCOS | BAHIA | Brasil | 2908101 | 29 | 33 | nan | nan | nan | Cerrado | 6.2 |
| 2b530f17-4ad2-3b66-8107-57330cc15424 | -17.02807 | -49.1529 | 2026-08-20 11:36:00 | TERRA_M-M | HIDROLÂNDIA | GOIÁS | Brasil | 5209705 | 52 | 33 | nan | nan | nan | Cerrado | 14.9 |
| ff445e56-54ab-3d76-9223-ca866507f22d | -15.92024 | -39.98359 | 2026-08-20 11:36:00 | TERRA_M-M | ITARANTIM | BAHIA | Brasil | 2916807 | 29 | 33 | nan | nan | nan | Mata Atlântica | 6.6 |
| 0dbf9156-27f7-352a-86e3-ecddab63ec03 | -18.02324 | -44.60683 | 2026-08-20 11:36:00 | TERRA_M-M | LASSANCE | MINAS GERAIS | Brasil | 3138104 | 31 | 33 | nan | nan | nan | Cerrado | 59.8 |
| 8283b956-4ce3-3b20-bb44-8e99ad84926a | -17.88827 | -39.86461 | 2026-08-20 11:36:00 | TERRA_M-M | NOVA VIÇOSA | BAHIA | Brasil | 2923001 | 29 | 33 | nan | nan | nan | Mata Atlântica | 7.8 |
| 55237f78-e5bf-39c1-8bdf-7234892886b8 | -12.60994 | -43.35162 | 2026-08-20 11:36:00 | TERRA_M-M | SÍTIO DO MATO | BAHIA | Brasil | 2930758 | 29 | 33 | nan | nan | nan | Cerrado | 7.4 |
| 82227196-65f8-3955-9df7-8876b63db455 | -18.02193 | -44.61679 | 2026-08-20 11:36:00 | TERRA_M-M | LASSANCE | MINAS GERAIS | Brasil | 3138104 | 31 | 33 | nan | nan | nan | Cerrado | 49.1 |
| ebe277e2-e310-3e73-9c37-06a406e2deea | -17.16703 | -44.41376 | 2026-08-20 11:36:00 | TERRA_M-M | JEQUITAÍ | MINAS GERAIS | Brasil | 3135605 | 31 | 33 | nan | nan | nan | Cerrado | 25.5 |
| 47a09467-d3ef-3345-a5f0-42417dd1783c | -14.33749 | -41.35486 | 2026-08-20 11:36:00 | TERRA_M-M | ARACATU | BAHIA | Brasil | 2902005 | 29 | 33 | nan | nan | nan | Caatinga | 17.4 |
| 2dec2f69-68f9-3d50-99e8-33c9eaa8d351 | -19.42668 | -41.3297 | 2026-08-20 11:36:00 | TERRA_M-M | SANTA RITA DO ITUETO | MINAS GERAIS | Brasil | 3159506 | 31 | 33 | nan | nan | nan | Mata Atlântica | 13.9 |
| 6be9dd56-46e6-3ad3-b8a6-21018c844702 | -14.44956 | -45.61319 | 2026-08-20 11:36:00 | TERRA_M-M | JABORANDI | BAHIA | Brasil | 2917359 | 29 | 33 | nan | nan | nan | Cerrado | 19.0 |
| d4ad0b1a-43cc-3155-96c5-36447db60b54 | -17.94071 | -44.40966 | 2026-08-20 11:36:00 | TERRA_M-M | LASSANCE | MINAS GERAIS | Brasil | 3138104 | 31 | 33 | nan | nan | nan | Cerrado | 9.2 |
| ce1f4e52-3c13-3500-befa-37f8ab78db2f | -16.84826 | -43.97434 | 2026-08-20 11:36:00 | TERRA_M-M | MONTES CLAROS | MINAS GERAIS | Brasil | 3143302 | 31 | 33 | nan | nan | nan | Cerrado | 12.9 |
| bdd6c1fe-69f4-3a8f-8e71-25aa6a0291d2 | -18.81794 | -48.33189 | 2026-08-20 11:36:00 | TERRA_M-M | UBERLÂNDIA | MINAS GERAIS | Brasil | 3170206 | 31 | 33 | nan | nan | nan | Cerrado | 7.8 |
| d2a4a405-e252-34cc-beed-fbe9a7461acb | -14.84062 | -45.51978 | 2026-08-20 11:36:00 | TERRA_M-M | COCOS | BAHIA | Brasil | 2908101 | 29 | 33 | nan | nan | nan | Cerrado | 10.2 |
| 4a7fa72d-6d49-3970-b997-d6b6d3226548 | -14.83178 | -45.51849 | 2026-08-20 11:36:00 | TERRA_M-M | COCOS | BAHIA | Brasil | 2908101 | 29 | 33 | nan | nan | nan | Cerrado | 32.2 |
| f28155b2-4c65-312d-997e-dc222cc9f048 | -13.85153 | -42.22164 | 2026-08-20 11:36:00 | TERRA_M-M | CAETITÉ | BAHIA | Brasil | 2905206 | 29 | 33 | nan | nan | nan | Caatinga | 9.7 |
| 0319b209-adae-3cb1-9a56-bdef20d82171 | -19.42374 | -41.33509 | 2026-08-20 11:36:00 | TERRA_M-M | SANTA RITA DO ITUETO | MINAS GERAIS | Brasil | 3159506 | 31 | 33 | nan | nan | nan | Mata Atlântica | 8.6 |
| 756cb625-d90e-3e72-913e-d4da54d4dfcf | -19.66111 | -45.89468 | 2026-08-20 11:36:00 | TERRA_M-M | ESTRELA DO INDAIÁ | MINAS GERAIS | Brasil | 3124708 | 31 | 33 | nan | nan | nan | Cerrado | 9.5 |
| a9e288d4-e86c-3900-bba2-7cbff55698c9 | -19.51528 | -46.6106 | 2026-08-20 11:36:00 | TERRA_M-M | IBIÁ | MINAS GERAIS | Brasil | 3129509 | 31 | 33 | nan | nan | nan | Cerrado | 3.8 |
| 76888e0c-3db4-33cf-98ad-91b500b44cf2 | -15.92447 | -39.98975 | 2026-08-20 11:36:00 | TERRA_M-M | ITARANTIM | BAHIA | Brasil | 2916807 | 29 | 33 | nan | nan | nan | Mata Atlântica | 13.0 |
| d6f714d8-510e-381b-ab4c-e5c8e2bc90ff | -19.15544 | -46.54919 | 2026-08-20 11:36:00 | TERRA_M-M | SERRA DO SALITRE | MINAS GERAIS | Brasil | 3166808 | 31 | 33 | nan | nan | nan | Cerrado | 8.3 |
| 9d5f6c43-cb69-310f-b725-0178137e239b | -19.6598 | -45.90413 | 2026-08-20 11:36:00 | TERRA_M-M | ESTRELA DO INDAIÁ | MINAS GERAIS | Brasil | 3124708 | 31 | 33 | nan | nan | nan | Cerrado | 16.4 |
| adfa90b5-f494-3204-8424-abd715f93bac | -14.33917 | -41.3412 | 2026-08-20 11:36:00 | TERRA_M-M | ARACATU | BAHIA | Brasil | 2902005 | 29 | 33 | nan | nan | nan | Caatinga | 11.7 |
| 7f8a0739-4a2b-3f92-8e4c-25cc9e4864af | -14.45839 | -45.61449 | 2026-08-20 11:36:00 | TERRA_M-M | JABORANDI | BAHIA | Brasil | 2917359 | 29 | 33 | nan | nan | nan | Cerrado | 6.6 |
| 739ac70c-dc3a-3237-a043-bdda71e45021 | -17.94205 | -44.39966 | 2026-08-20 11:36:00 | TERRA_M-M | LASSANCE | MINAS GERAIS | Brasil | 3138104 | 31 | 33 | nan | nan | nan | Cerrado | 28.6 |
| 18d7fae0-9d23-30a4-887d-4c0256cbb1c9 | -14.45709 | -45.62355 | 2026-08-20 11:36:00 | TERRA_M-M | JABORANDI | BAHIA | Brasil | 2917359 | 29 | 33 | nan | nan | nan | Cerrado | 8.3 |
| a9576ca9-db6c-3845-9cdb-cb3f25350bfb | -14.83933 | -45.52887 | 2026-08-20 11:36:00 | TERRA_M-M | COCOS | BAHIA | Brasil | 2908101 | 29 | 33 | nan | nan | nan | Cerrado | 7.7 |
| 22c2fd10-397f-35fd-923a-481733806eb5 | -16.25843 | -45.20265 | 2026-08-20 11:36:00 | TERRA_M-M | SÃO ROMÃO | MINAS GERAIS | Brasil | 3164209 | 31 | 33 | nan | nan | nan | Cerrado | 6.1 |
| c0cc7703-6459-3f0d-bbfc-87a7f2388061 | -20.01191 | -41.59565 | 2026-08-20 11:36:00 | TERRA_M-M | CHALÉ | MINAS GERAIS | Brasil | 3116001 | 31 | 33 | nan | nan | nan | Mata Atlântica | 11.9 |
| fceb7d18-2442-3635-91e5-510cac7094df | -17.44095 | -44.90578 | 2026-08-20 11:36:00 | TERRA_M-M | PIRAPORA | MINAS GERAIS | Brasil | 3151206 | 31 | 33 | nan | nan | nan | Cerrado | 75.8 |
| f769c80d-2e7a-397d-aff8-fc59dd3290d2 | -19.15676 | -46.5399 | 2026-08-20 11:36:00 | TERRA_M-M | SERRA DO SALITRE | MINAS GERAIS | Brasil | 3166808 | 31 | 33 | nan | nan | nan | Cerrado | 17.9 |
| 713b9e1a-a5b9-3b79-8710-13cbed2511bb | -19.01962 | -46.33524 | 2026-08-20 11:36:00 | TERRA_M-M | CARMO DO PARANAÍBA | MINAS GERAIS | Brasil | 3114303 | 31 | 33 | nan | nan | nan | Cerrado | 6.7 |
| 6c7317d9-c5fa-349a-83ba-24784034f274 | -16.61671 | -42.43845 | 2026-08-20 11:36:00 | TERRA_M-M | JOSENÓPOLIS | MINAS GERAIS | Brasil | 3136579 | 31 | 33 | nan | nan | nan | Cerrado | 8.5 |
| 32c38b5c-c6b5-3654-ba26-6f25c79b7fe8 | -17.43965 | -44.91541 | 2026-08-20 11:36:00 | TERRA_M-M | PIRAPORA | MINAS GERAIS | Brasil | 3151206 | 31 | 33 | nan | nan | nan | Cerrado | 73.0 |
| 969fc8f9-3e9e-3d36-84d9-740ad52efb2d | -19.71703 | -46.21833 | 2026-08-20 11:36:00 | TERRA_M-M | CAMPOS ALTOS | MINAS GERAIS | Brasil | 3111507 | 31 | 33 | nan | nan | nan | Cerrado | 5.5 |
| 809b0c22-ad29-3874-b332-b98e5d5b99c7 | -18.04027 | -44.61948 | 2026-08-20 11:36:00 | TERRA_M-M | LASSANCE | MINAS GERAIS | Brasil | 3138104 | 31 | 33 | nan | nan | nan | Cerrado | 10.3 |
| 10682a21-8d34-319d-8ec4-72404a4fb873 | -12.85391 | -48.42182 | 2026-08-20 11:36:00 | TERRA_M-M | PALMEIRÓPOLIS | TOCANTINS | Brasil | 1715754 | 17 | 33 | nan | nan | nan | Cerrado | 14.0 |
| 9c4a6e34-7685-3e35-b852-84ee61e99098 | -20.00528 | -45.73663 | 2026-08-20 11:36:00 | TERRA_M-M | IGUATAMA | MINAS GERAIS | Brasil | 3130309 | 31 | 33 | nan | nan | nan | Cerrado | 8.3 |
| a19e71c1-7a42-3b1b-9a71-fb6656e77681 | -13.85304 | -42.20985 | 2026-08-20 11:36:00 | TERRA_M-M | CAETITÉ | BAHIA | Brasil | 2905206 | 29 | 33 | nan | nan | nan | Caatinga | 22.5 |
| ef81e231-58ff-3fe4-b546-9f9889a05a87 | -14.73232 | -47.15025 | 2026-08-20 11:36:00 | TERRA_M-M | VILA BOA | GOIÁS | Brasil | 5222203 | 52 | 33 | nan | nan | nan | Cerrado | 9.5 |
| b4cdc73e-b56a-3f2c-a025-e898dd5f17c9 | -19.02094 | -46.32595 | 2026-08-20 11:36:00 | TERRA_M-M | CARMO DO PARANAÍBA | MINAS GERAIS | Brasil | 3114303 | 31 | 33 | nan | nan | nan | Cerrado | 7.6 |
| cbdf4c9b-c155-30d3-bd9b-9f9295cfcce4 | -17.53913 | -46.56668 | 2026-08-20 11:36:00 | TERRA_M-M | LAGOA GRANDE | MINAS GERAIS | Brasil | 3137536 | 31 | 33 | nan | nan | nan | Cerrado | 17.9 |
| 96b6070a-0c2e-30e4-ab2d-e353f2006be7 | -13.44451 | -43.84551 | 2026-08-20 11:36:00 | TERRA_M-M | SERRA DO RAMALHO | BAHIA | Brasil | 2930154 | 29 | 33 | nan | nan | nan | Cerrado | 7.9 |
| f894985f-8497-3f38-b2cb-e1b0088951ac | -17.16572 | -44.42354 | 2026-08-20 11:36:00 | TERRA_M-M | JEQUITAÍ | MINAS GERAIS | Brasil | 3135605 | 31 | 33 | nan | nan | nan | Cerrado | 25.7 |
| d89ea7b2-9491-37a2-8dfc-d6f0a454b41f | -17.33282 | -43.63116 | 2026-08-20 11:36:00 | TERRA_M-M | OLHOS-D'ÁGUA | MINAS GERAIS | Brasil | 3145455 | 31 | 33 | nan | nan | nan | Cerrado | 45.8 |
| c81160d6-9bbe-3d79-b77c-1ecdc4626c77 | -17.33419 | -43.62045 | 2026-08-20 11:36:00 | TERRA_M-M | OLHOS-D'ÁGUA | MINAS GERAIS | Brasil | 3145455 | 31 | 33 | nan | nan | nan | Cerrado | 50.5 |
| c8afa570-3cc4-3a28-8acb-9484f6ecdcf0 | -17.54566 | -42.74358 | 2026-08-20 11:36:00 | TERRA_M-M | VEREDINHA | MINAS GERAIS | Brasil | 3171071 | 31 | 33 | nan | nan | nan | Cerrado | 9.2 |
| c332314a-ccd0-3c0a-a078-241a1362f334 | -18.74068 | -49.17317 | 2026-08-20 11:36:00 | TERRA_M-M | CANÁPOLIS | MINAS GERAIS | Brasil | 3111804 | 31 | 33 | nan | nan | nan | Cerrado | 15.6 |
| 4fab47e9-3022-34cd-8136-72bcebd59231 | -15.93319 | -48.06526 | 2026-08-20 11:36:00 | TERRA_M-M | BRASÍLIA | DISTRITO FEDERAL | Brasil | 5300108 | 53 | 33 | nan | nan | nan | Cerrado | 9.9 |


[Clique aqui para ver as próximas entradas](README71.md)
