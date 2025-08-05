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
| 6515c04d-3716-3abc-b524-c68c6891dfd3 | -7.60748 | -45.30904 | 2025-08-05 04:17:00 | NPP-375D | RIBEIRO GONÇALVES | PIAUÍ | Brasil | 2208908 | 22 | 33 | nan | nan | nan | Cerrado | 1.7 |
| 0241fb60-aa8a-3aff-a257-b0d333b07d2d | -8.3823 | -46.5374 | 2025-08-05 04:17:00 | NPP-375D | RIACHÃO | MARANHÃO | Brasil | 2109502 | 21 | 33 | nan | nan | nan | Cerrado | 0.6 |
| 90a04d4a-c38c-3801-bf8c-de2a75c45f1e | -5.88945 | -43.73409 | 2025-08-05 04:17:00 | NPP-375D | BURITI BRAVO | MARANHÃO | Brasil | 2102309 | 21 | 33 | nan | nan | nan | Cerrado | 2.1 |
| 035aa5e4-7443-3377-a176-00c624f71b5b | -7.56883 | -44.90327 | 2025-08-05 04:17:00 | NPP-375D | URUÇUÍ | PIAUÍ | Brasil | 2211209 | 22 | 33 | nan | nan | nan | Cerrado | 0.8 |
| 4e58ae5e-b0d1-3186-9f6c-b71a96a90363 | -8.88098 | -44.79002 | 2025-08-05 04:17:00 | NPP-375D | CURRAIS | PIAUÍ | Brasil | 2203230 | 22 | 33 | nan | nan | nan | Cerrado | 1.2 |
| 125ea2bd-4e1b-3b09-a254-bd530d34d27e | -6.2503 | -45.07948 | 2025-08-05 04:17:00 | NPP-375D | FERNANDO FALCÃO | MARANHÃO | Brasil | 2104081 | 21 | 33 | nan | nan | nan | Cerrado | 0.7 |
| 293c481b-a95f-3bc4-938e-cee1feb70c74 | -6.97068 | -42.86853 | 2025-08-05 04:17:00 | NPP-375D | FLORIANO | PIAUÍ | Brasil | 2203909 | 22 | 33 | nan | nan | nan | Caatinga | 19.1 |
| d8923322-b026-30ce-854b-3c5b4fd938f7 | -6.33582 | -45.64067 | 2025-08-05 04:17:00 | NPP-375D | FERNANDO FALCÃO | MARANHÃO | Brasil | 2104081 | 21 | 33 | nan | nan | nan | Cerrado | 1.2 |
| 39f71c36-3247-3c10-bbea-92fd5a172734 | -9.05276 | -45.06272 | 2025-08-05 04:17:00 | NPP-375D | BOM JESUS | PIAUÍ | Brasil | 2201903 | 22 | 33 | nan | nan | nan | Cerrado | 1.4 |
| 2951ea9e-612b-3eba-a10e-81ca5900044f | -8.00864 | -43.21772 | 2025-08-05 04:17:00 | NPP-375D | PAVUSSU | PIAUÍ | Brasil | 2207850 | 22 | 33 | nan | nan | nan | Caatinga | 8.6 |
| 53acc74e-57eb-37fc-973c-176db98bd164 | -7.34599 | -44.68202 | 2025-08-05 04:17:00 | NPP-375D | BENEDITO LEITE | MARANHÃO | Brasil | 2101806 | 21 | 33 | nan | nan | nan | Cerrado | 1.3 |
| 2b454ece-5221-3cba-b24b-2ec04b06a947 | -11.75113 | -45.01202 | 2025-08-05 04:17:00 | NPP-375D | RIACHÃO DAS NEVES | BAHIA | Brasil | 2926202 | 29 | 33 | nan | nan | nan | Cerrado | 2.4 |
| ebaec3a8-562f-3a3f-840a-20157af76a7e | -11.74674 | -44.99667 | 2025-08-05 04:17:00 | NPP-375D | RIACHÃO DAS NEVES | BAHIA | Brasil | 2926202 | 29 | 33 | nan | nan | nan | Cerrado | 1.8 |
| 5b992327-f0b0-3e03-8f99-fa6ebd87a571 | -8.2729 | -45.06496 | 2025-08-05 04:17:00 | NPP-375D | BAIXA GRANDE DO RIBEIRO | PIAUÍ | Brasil | 2201150 | 22 | 33 | nan | nan | nan | Cerrado | 1.1 |
| 5156c8d6-2401-3112-91cd-f235ee8114a3 | -7.37964 | -43.7487 | 2025-08-05 04:17:00 | NPP-375D | SEBASTIÃO LEAL | PIAUÍ | Brasil | 2210631 | 22 | 33 | nan | nan | nan | Cerrado | 0.6 |
| 989fa977-b89c-3186-babd-0f9595971e62 | -10.92241 | -48.36722 | 2025-08-05 04:17:00 | NPP-375D | PORTO NACIONAL | TOCANTINS | Brasil | 1718204 | 17 | 33 | nan | nan | nan | Cerrado | 1.6 |
| 7a11d72a-0749-38f6-af7b-cc58e9b5efba | -7.34319 | -44.67788 | 2025-08-05 04:17:00 | NPP-375D | BENEDITO LEITE | MARANHÃO | Brasil | 2101806 | 21 | 33 | nan | nan | nan | Cerrado | 1.5 |
| 28e93748-1b7d-3526-9966-13de8cafee46 | -8.8505 | -47.60827 | 2025-08-05 04:17:00 | NPP-375D | SANTA MARIA DO TOCANTINS | TOCANTINS | Brasil | 1718881 | 17 | 33 | nan | nan | nan | Cerrado | 4.3 |
| e5a133a6-777b-3a15-aaed-7555907d45ee | -7.21308 | -41.85266 | 2025-08-05 04:17:00 | NPP-375D | WALL FERRAZ | PIAUÍ | Brasil | 2211704 | 22 | 33 | nan | nan | nan | Caatinga | 0.6 |
| 8d5b8239-05d7-3737-9a96-524b02e698e4 | -5.24315 | -46.77871 | 2025-08-05 04:17:00 | NPP-375D | AMARANTE DO MARANHÃO | MARANHÃO | Brasil | 2100600 | 21 | 33 | nan | nan | nan | Cerrado | 2.0 |
| a8b119a0-5c8a-327c-90b5-4aaf8cc1e869 | -5.77963 | -51.66745 | 2025-08-05 04:17:00 | NPP-375D | SÃO FÉLIX DO XINGU | PARÁ | Brasil | 1507300 | 15 | 33 | nan | nan | nan | Amazônia | 0.8 |
| 89f61945-ba90-33d2-ae5d-c4c070300eed | -7.56491 | -44.88437 | 2025-08-05 04:17:00 | NPP-375D | URUÇUÍ | PIAUÍ | Brasil | 2211209 | 22 | 33 | nan | nan | nan | Cerrado | 1.1 |
| a5e5fae1-b8fc-3485-8dbd-cc7e755fa2d7 | -10.52822 | -42.54921 | 2025-08-05 04:17:00 | NPP-375D | XIQUE-XIQUE | BAHIA | Brasil | 2933604 | 29 | 33 | nan | nan | nan | Caatinga | 1.5 |
| 97b6bd31-9269-34bc-ad6c-7cb7527c4168 | -10.78719 | -46.52456 | 2025-08-05 04:17:00 | NPP-375D | MATEIROS | TOCANTINS | Brasil | 1712702 | 17 | 33 | nan | nan | nan | Cerrado | 1.1 |
| b0ee9f3c-98a0-3420-826a-20e5dadc2511 | -13.29486 | -39.86272 | 2025-08-05 04:17:00 | NPP-375D | SANTA INÊS | BAHIA | Brasil | 2927903 | 29 | 33 | nan | nan | nan | Mata Atlântica | 1.9 |
| d48f67ac-7403-3725-b806-412f670c770d | -11.91153 | -44.95755 | 2025-08-05 04:17:00 | NPP-375D | RIACHÃO DAS NEVES | BAHIA | Brasil | 2926202 | 29 | 33 | nan | nan | nan | Cerrado | 4.2 |
| f4bd9a31-d847-3d9d-8e12-0196a6153a96 | -18.85365 | -40.46049 | 2025-08-05 04:17:00 | NPP-375D | NOVA VENÉCIA | ESPÍRITO SANTO | Brasil | 3203908 | 32 | 33 | nan | nan | nan | Mata Atlântica | 2.1 |
| 6cb4b705-cfe7-3347-800f-c7eccce41a3a | -5.75104 | -51.64629 | 2025-08-05 04:17:00 | NPP-375D | SÃO FÉLIX DO XINGU | PARÁ | Brasil | 1507300 | 15 | 33 | nan | nan | nan | Amazônia | 0.4 |
| 57e93a1c-41ea-3ae3-948f-aeb97423504e | -9.72366 | -42.20218 | 2025-08-05 04:17:00 | NPP-375D | REMANSO | BAHIA | Brasil | 2926004 | 29 | 33 | nan | nan | nan | Caatinga | 0.6 |
| a91f0a63-2a54-33c8-9437-3b68fd8fab77 | -9.6967 | -51.93909 | 2025-08-05 04:17:00 | NPP-375D | SÃO FÉLIX DO XINGU | PARÁ | Brasil | 1507300 | 15 | 33 | nan | nan | nan | Amazônia | 1.4 |
| f0aa44db-9051-3028-8aa2-ac7f762ad7a9 | -8.2395 | -45.05575 | 2025-08-05 04:17:00 | NPP-375D | BAIXA GRANDE DO RIBEIRO | PIAUÍ | Brasil | 2201150 | 22 | 33 | nan | nan | nan | Cerrado | 1.5 |
| 7387e85c-0158-329d-8c33-eef23ef6b24d | -7.53608 | -44.86845 | 2025-08-05 04:17:00 | NPP-375D | URUÇUÍ | PIAUÍ | Brasil | 2211209 | 22 | 33 | nan | nan | nan | Cerrado | 1.0 |
| 34e3a6af-3408-318e-8c78-9fb2c558cd22 | -7.36649 | -44.16803 | 2025-08-05 04:17:00 | NPP-375D | ANTÔNIO ALMEIDA | PIAUÍ | Brasil | 2200806 | 22 | 33 | nan | nan | nan | Cerrado | 0.9 |
| f196fee1-d172-3970-86e2-fc35add93637 | -17.20314 | -44.82796 | 2025-08-05 04:17:00 | NPP-375D | VÁRZEA DA PALMA | MINAS GERAIS | Brasil | 3170800 | 31 | 33 | nan | nan | nan | Cerrado | 1.2 |
| d3faeb98-ad3c-31f5-b9ab-73a8efec4e8e | -11.74722 | -45.01504 | 2025-08-05 04:17:00 | NPP-375D | RIACHÃO DAS NEVES | BAHIA | Brasil | 2926202 | 29 | 33 | nan | nan | nan | Cerrado | 0.9 |
| bd3b1e9e-c7a5-3f34-8d5f-b283a8b7c446 | -6.96404 | -42.86748 | 2025-08-05 04:17:00 | NPP-375D | FLORIANO | PIAUÍ | Brasil | 2203909 | 22 | 33 | nan | nan | nan | Caatinga | 4.0 |
| f50a9be3-c387-360e-a02f-77a0e28d2a01 | -7.08621 | -44.35987 | 2025-08-05 04:17:00 | NPP-375D | BENEDITO LEITE | MARANHÃO | Brasil | 2101806 | 21 | 33 | nan | nan | nan | Cerrado | 0.8 |
| 9844be6a-f5f8-3399-8094-914ff93ce055 | -11.27532 | -44.64361 | 2025-08-05 04:17:00 | NPP-375D | SANTA RITA DE CÁSSIA | BAHIA | Brasil | 2928406 | 29 | 33 | nan | nan | nan | Cerrado | 0.9 |
| 2e988375-d4e9-3c93-aa29-360a2854c4c8 | -6.43585 | -44.82243 | 2025-08-05 04:17:00 | NPP-375D | MIRADOR | MARANHÃO | Brasil | 2106706 | 21 | 33 | nan | nan | nan | Cerrado | 1.5 |
| a8db9f1d-36f0-3ede-89f7-1c15c1cda989 | -8.3845 | -46.54635 | 2025-08-05 04:17:00 | NPP-375D | RIACHÃO | MARANHÃO | Brasil | 2109502 | 21 | 33 | nan | nan | nan | Cerrado | 2.0 |
| 42a4612b-107b-3667-85a4-bcdb63a662fa | -6.89884 | -52.86702 | 2025-08-05 04:17:00 | NPP-375D | SÃO FÉLIX DO XINGU | PARÁ | Brasil | 1507300 | 15 | 33 | nan | nan | nan | Amazônia | 4.1 |
| 1af71a79-feec-3ece-8037-f181c247142c | -7.33981 | -44.67732 | 2025-08-05 04:17:00 | NPP-375D | BENEDITO LEITE | MARANHÃO | Brasil | 2101806 | 21 | 33 | nan | nan | nan | Cerrado | 1.3 |
| 7c0c7ed3-a5bf-3af5-96c9-0de079efdc76 | -7.90227 | -45.53489 | 2025-08-05 04:17:00 | NPP-375D | RIBEIRO GONÇALVES | PIAUÍ | Brasil | 2208908 | 22 | 33 | nan | nan | nan | Cerrado | 1.4 |
| d30dcfab-224a-3e25-929f-8ad163fa0118 | -9.18193 | -48.84632 | 2025-08-05 04:17:00 | NPP-375D | DOIS IRMÃOS DO TOCANTINS | TOCANTINS | Brasil | 1707207 | 17 | 33 | nan | nan | nan | Cerrado | 5.0 |
| a57f10d6-3cd8-39fb-aef6-04b1c1cc2395 | -9.55828 | -47.8815 | 2025-08-05 04:17:00 | NPP-375D | RIO SONO | TOCANTINS | Brasil | 1718758 | 17 | 33 | nan | nan | nan | Cerrado | 1.2 |
| 1ccde0a7-7301-375d-bcbf-1821587c8b86 | -11.78974 | -44.99974 | 2025-08-05 04:17:00 | NPP-375D | RIACHÃO DAS NEVES | BAHIA | Brasil | 2926202 | 29 | 33 | nan | nan | nan | Cerrado | 2.2 |
| 0bb8a27c-26bf-3a69-b646-6a09b5b2b16b | -6.73487 | -45.3117 | 2025-08-05 04:17:00 | NPP-375D | MIRADOR | MARANHÃO | Brasil | 2106706 | 21 | 33 | nan | nan | nan | Cerrado | 1.2 |
| 2697f6fc-b8a1-3eae-9e4f-b0c909083a4e | -18.74553 | -43.9243 | 2025-08-05 04:17:00 | NPP-375D | SANTANA DE PIRAPAMA | MINAS GERAIS | Brasil | 3158508 | 31 | 33 | nan | nan | nan | Cerrado | 0.9 |
| 06c4a77e-077a-3e17-89e6-4edde62ba4c6 | -10.78552 | -46.64271 | 2025-08-05 04:17:00 | NPP-375D | MATEIROS | TOCANTINS | Brasil | 1712702 | 17 | 33 | nan | nan | nan | Cerrado | 1.5 |
| 96ae8032-5b62-33b2-b585-aa111a30c3c8 | -11.49663 | -44.27114 | 2025-08-05 04:17:00 | NPP-375D | COTEGIPE | BAHIA | Brasil | 2909406 | 29 | 33 | nan | nan | nan | Cerrado | 1.0 |
| c4959845-f441-3f50-964e-d7462304d326 | -9.94026 | -47.98433 | 2025-08-05 04:17:00 | NPP-375D | APARECIDA DO RIO NEGRO | TOCANTINS | Brasil | 1701101 | 17 | 33 | nan | nan | nan | Cerrado | 0.7 |
| 0a175719-c6ee-3709-a9a5-6fd3cc5640ab | -12.22256 | -44.19708 | 2025-08-05 04:17:00 | NPP-375D | CRISTÓPOLIS | BAHIA | Brasil | 2909703 | 29 | 33 | nan | nan | nan | Cerrado | 0.5 |
| 45fe17b7-6b33-3edb-9bdb-cf08f09d4ceb | -7.53499 | -45.04958 | 2025-08-05 04:17:00 | NPP-375D | RIBEIRO GONÇALVES | PIAUÍ | Brasil | 2208908 | 22 | 33 | nan | nan | nan | Cerrado | 2.3 |
| 6370caaf-c1cb-3e41-b8e2-7794cc21491f | -11.7478 | -45.01148 | 2025-08-05 04:17:00 | NPP-375D | RIACHÃO DAS NEVES | BAHIA | Brasil | 2926202 | 29 | 33 | nan | nan | nan | Cerrado | 0.9 |
| b8c8582f-062e-3e01-aa83-c41c39098d5c | -9.1814 | -48.84559 | 2025-08-05 04:17:00 | NPP-375D | DOIS IRMÃOS DO TOCANTINS | TOCANTINS | Brasil | 1707207 | 17 | 33 | nan | nan | nan | Cerrado | 10.6 |
| 5b5f85be-dbdb-37f5-9b5a-d891aad54570 | -8.94339 | -46.73319 | 2025-08-05 04:17:00 | NPP-375D | BALSAS | MARANHÃO | Brasil | 2101400 | 21 | 33 | nan | nan | nan | Cerrado | 17.8 |
| 58a40f7f-420e-37b1-bc44-5442ff90b415 | -7.77589 | -45.22078 | 2025-08-05 04:17:00 | NPP-375D | RIBEIRO GONÇALVES | PIAUÍ | Brasil | 2208908 | 22 | 33 | nan | nan | nan | Cerrado | 0.8 |
| f1ae2422-8f1f-3f1f-a121-e0805578ac4b | -8.00424 | -43.22408 | 2025-08-05 04:17:00 | NPP-375D | PAVUSSU | PIAUÍ | Brasil | 2207850 | 22 | 33 | nan | nan | nan | Caatinga | 16.0 |
| d798a4b1-248d-3360-90be-02721b281dc4 | -7.70091 | -45.1248 | 2025-08-05 04:17:00 | NPP-375D | RIBEIRO GONÇALVES | PIAUÍ | Brasil | 2208908 | 22 | 33 | nan | nan | nan | Cerrado | 1.0 |
| fd3f6385-83c2-3324-bf7d-3a9f26e446cc | -6.24686 | -45.07887 | 2025-08-05 04:17:00 | NPP-375D | FERNANDO FALCÃO | MARANHÃO | Brasil | 2104081 | 21 | 33 | nan | nan | nan | Cerrado | 0.7 |
| 0ab32fdc-9287-3518-b9d2-895b6ab25464 | -11.75521 | -44.96511 | 2025-08-05 04:17:00 | NPP-375D | RIACHÃO DAS NEVES | BAHIA | Brasil | 2926202 | 29 | 33 | nan | nan | nan | Cerrado | 2.4 |
| f2be3e68-d1cd-3a8e-964a-a038bf74b1af | -7.56842 | -44.8844 | 2025-08-05 04:17:00 | NPP-375D | URUÇUÍ | PIAUÍ | Brasil | 2211209 | 22 | 33 | nan | nan | nan | Cerrado | 1.3 |
| 01f6b22d-5a50-30c9-acde-eb0018bf3514 | -10.80734 | -46.51178 | 2025-08-05 04:17:00 | NPP-375D | MATEIROS | TOCANTINS | Brasil | 1712702 | 17 | 33 | nan | nan | nan | Cerrado | 7.0 |
| 441ee7d8-b319-30bd-88b0-2cc3c40ec907 | -7.37632 | -43.74817 | 2025-08-05 04:17:00 | NPP-375D | SEBASTIÃO LEAL | PIAUÍ | Brasil | 2210631 | 22 | 33 | nan | nan | nan | Cerrado | 0.6 |
| 668657c2-17c6-3604-b66d-f4ea57f07eec | -11.9199 | -44.94804 | 2025-08-05 04:17:00 | NPP-375D | RIACHÃO DAS NEVES | BAHIA | Brasil | 2926202 | 29 | 33 | nan | nan | nan | Cerrado | 1.4 |
| f5ff6c38-57ad-3c1a-a9ad-82a90bf0f39a | -10.71458 | -47.33285 | 2025-08-05 04:17:00 | NPP-375D | PONTE ALTA DO TOCANTINS | TOCANTINS | Brasil | 1717909 | 17 | 33 | nan | nan | nan | Cerrado | 1.0 |
| aac19e72-f842-3c0f-982e-b683ff87e9ed | -6.91145 | -43.90371 | 2025-08-05 04:17:00 | NPP-375D | GUADALUPE | PIAUÍ | Brasil | 2204501 | 22 | 33 | nan | nan | nan | Cerrado | 0.9 |
| 704df04b-c95b-3ad1-84f9-d0e323a59f23 | -10.47904 | -44.36896 | 2025-08-05 04:17:00 | NPP-375D | PARNAGUÁ | PIAUÍ | Brasil | 2207603 | 22 | 33 | nan | nan | nan | Cerrado | 0.6 |
| e2fa8123-b6f6-39a5-bf7a-8c30abb18d8e | -8.94855 | -46.74688 | 2025-08-05 04:17:00 | NPP-375D | BALSAS | MARANHÃO | Brasil | 2101400 | 21 | 33 | nan | nan | nan | Cerrado | 6.9 |
| 05e2cbeb-4c2a-3778-8e17-2601ed5ee93d | -8.93909 | -46.73673 | 2025-08-05 04:17:00 | NPP-375D | BALSAS | MARANHÃO | Brasil | 2101400 | 21 | 33 | nan | nan | nan | Cerrado | 13.7 |
| 695271b0-5669-3455-a089-9c8e4dce3da9 | -7.36412 | -43.71761 | 2025-08-05 04:17:00 | NPP-375D | SEBASTIÃO LEAL | PIAUÍ | Brasil | 2210631 | 22 | 33 | nan | nan | nan | Caatinga | 3.3 |
| 819da820-c8f3-3a4d-9bfb-1b7cd6ab48e6 | -9.62028 | -43.85378 | 2025-08-05 04:17:00 | NPP-375D | MORRO CABEÇA NO TEMPO | PIAUÍ | Brasil | 2206654 | 22 | 33 | nan | nan | nan | Caatinga | 1.1 |
| 0fe719c3-350c-35c8-b114-dd38d2b4eb3b | -8.01688 | -43.18694 | 2025-08-05 04:17:00 | NPP-375D | CANTO DO BURITI | PIAUÍ | Brasil | 2202307 | 22 | 33 | nan | nan | nan | Caatinga | 1.9 |
| 2a9e1d63-2b14-3802-aefd-4bb8db62b6e0 | -6.78585 | -43.24458 | 2025-08-05 04:17:00 | NPP-375D | FLORIANO | PIAUÍ | Brasil | 2203909 | 22 | 33 | nan | nan | nan | Caatinga | 1.0 |
| 060a71ae-79be-3394-a5f5-120b5e70ddf5 | -11.78916 | -45.00333 | 2025-08-05 04:17:00 | NPP-375D | RIACHÃO DAS NEVES | BAHIA | Brasil | 2926202 | 29 | 33 | nan | nan | nan | Cerrado | 5.0 |
| cfa5b3b2-d11e-32a5-a73a-c5d1efbe4c30 | -7.18867 | -44.16117 | 2025-08-05 04:17:00 | NPP-375D | ANTÔNIO ALMEIDA | PIAUÍ | Brasil | 2200806 | 22 | 33 | nan | nan | nan | Cerrado | 0.9 |
| fada0e6f-984c-391b-b3cd-71987225d0c3 | -10.46958 | -44.38549 | 2025-08-05 04:17:00 | NPP-375D | PARNAGUÁ | PIAUÍ | Brasil | 2207603 | 22 | 33 | nan | nan | nan | Cerrado | 1.2 |
| 5f2e0eaf-195d-317d-bc9d-df6a064f766e | -6.50043 | -42.80136 | 2025-08-05 04:17:00 | NPP-375D | AMARANTE | PIAUÍ | Brasil | 2200509 | 22 | 33 | nan | nan | nan | Caatinga | 0.9 |
| 65901b74-dfc0-32fc-93f1-7dc3d0f51ff4 | -11.93152 | -44.96088 | 2025-08-05 04:17:00 | NPP-375D | RIACHÃO DAS NEVES | BAHIA | Brasil | 2926202 | 29 | 33 | nan | nan | nan | Cerrado | 2.7 |
| 5017d2a2-2df8-3de3-901a-bb6eb41a1f87 | -10.47459 | -44.37545 | 2025-08-05 04:17:00 | NPP-375D | PARNAGUÁ | PIAUÍ | Brasil | 2207603 | 22 | 33 | nan | nan | nan | Cerrado | 0.8 |
| 370a651d-9a88-3606-96dd-b6e90ff0fcae | -8.25591 | -45.06219 | 2025-08-05 04:17:00 | NPP-375D | BAIXA GRANDE DO RIBEIRO | PIAUÍ | Brasil | 2201150 | 22 | 33 | nan | nan | nan | Cerrado | 1.4 |
| 6d3723ab-0aa9-36dd-9ac1-bd5a6c793f64 | -10.78447 | -48.7971 | 2025-08-05 04:17:00 | NPP-375D | FÁTIMA | TOCANTINS | Brasil | 1707553 | 17 | 33 | nan | nan | nan | Cerrado | 3.0 |
| 29e1060b-b12b-391e-8616-b96312e7a970 | -8.38811 | -46.54689 | 2025-08-05 04:17:00 | NPP-375D | RIACHÃO | MARANHÃO | Brasil | 2109502 | 21 | 33 | nan | nan | nan | Cerrado | 1.3 |
| 82f38250-1ee6-39d0-9297-3ff6d6a9a567 | -11.81702 | -44.25453 | 2025-08-05 04:17:00 | NPP-375D | COTEGIPE | BAHIA | Brasil | 2909406 | 29 | 33 | nan | nan | nan | Cerrado | 0.6 |
| 0af12639-2b91-3e27-970d-c2b119fb6778 | -7.85909 | -43.86121 | 2025-08-05 04:17:00 | NPP-375D | BERTOLÍNIA | PIAUÍ | Brasil | 2201705 | 22 | 33 | nan | nan | nan | Cerrado | 0.9 |
| 0c0781ee-fd46-3036-ae9c-60c6bc25e959 | -7.53735 | -45.05313 | 2025-08-05 04:17:00 | NPP-375D | RIBEIRO GONÇALVES | PIAUÍ | Brasil | 2208908 | 22 | 33 | nan | nan | nan | Cerrado | 3.8 |
| 45834281-db58-3fc8-9275-cf9fe68f9d56 | -5.98544 | -49.91045 | 2025-08-05 04:17:00 | NPP-375D | PARAUAPEBAS | PARÁ | Brasil | 1505536 | 15 | 33 | nan | nan | nan | Amazônia | 6.2 |
| e3d2b826-7f14-3776-9dc8-306b4ab5c934 | -11.92103 | -44.94098 | 2025-08-05 04:17:00 | NPP-375D | RIACHÃO DAS NEVES | BAHIA | Brasil | 2926202 | 29 | 33 | nan | nan | nan | Cerrado | 2.1 |
| 8ec00967-bf57-31d0-aaeb-cc244bdfbc64 | -8.11245 | -45.52166 | 2025-08-05 04:17:00 | NPP-375D | RIBEIRO GONÇALVES | PIAUÍ | Brasil | 2208908 | 22 | 33 | nan | nan | nan | Cerrado | 1.2 |
| 4cac1d92-7e3b-3651-a690-91943e104d77 | -8.26551 | -45.06752 | 2025-08-05 04:17:00 | NPP-375D | BAIXA GRANDE DO RIBEIRO | PIAUÍ | Brasil | 2201150 | 22 | 33 | nan | nan | nan | Cerrado | 1.2 |
| af79aba1-4384-38e1-9a35-25cf602a3979 | -10.782 | -46.64209 | 2025-08-05 04:17:00 | NPP-375D | MATEIROS | TOCANTINS | Brasil | 1712702 | 17 | 33 | nan | nan | nan | Cerrado | 2.1 |
| de3e67b7-5542-39a3-bf8f-711a5233025a | -8.00477 | -43.22067 | 2025-08-05 04:17:00 | NPP-375D | PAVUSSU | PIAUÍ | Brasil | 2207850 | 22 | 33 | nan | nan | nan | Caatinga | 16.0 |
| 539b64e5-b9f2-305f-8950-efc2c76b27ce | -7.09336 | -44.68964 | 2025-08-05 04:17:00 | NPP-375D | BENEDITO LEITE | MARANHÃO | Brasil | 2101806 | 21 | 33 | nan | nan | nan | Cerrado | 1.3 |
| 94dcf454-b113-3421-98a2-a72873bb9dbb | -8.7149 | -46.43879 | 2025-08-05 04:17:00 | NPP-375D | BALSAS | MARANHÃO | Brasil | 2101400 | 21 | 33 | nan | nan | nan | Cerrado | 2.1 |
| a839d110-20ab-3f97-bd51-273dcd537d84 | -11.92096 | -44.96276 | 2025-08-05 04:17:00 | NPP-375D | RIACHÃO DAS NEVES | BAHIA | Brasil | 2926202 | 29 | 33 | nan | nan | nan | Cerrado | 7.4 |
| 32224c91-cddd-3a5f-80b8-2fcc88f37884 | -6.96791 | -42.86453 | 2025-08-05 04:17:00 | NPP-375D | FLORIANO | PIAUÍ | Brasil | 2203909 | 22 | 33 | nan | nan | nan | Caatinga | 19.1 |
| bf762326-2776-3491-9bbe-bbafd1fa11a7 | -8.73563 | -46.43699 | 2025-08-05 04:17:00 | NPP-375D | BALSAS | MARANHÃO | Brasil | 2101400 | 21 | 33 | nan | nan | nan | Cerrado | 1.2 |
| 185a6243-785a-38ba-936f-0d3f77aafed2 | -11.04028 | -47.61467 | 2025-08-05 04:17:00 | NPP-375D | PINDORAMA DO TOCANTINS | TOCANTINS | Brasil | 1717008 | 17 | 33 | nan | nan | nan | Cerrado | 1.1 |
| b1ee8883-24c2-31cd-9cb9-031f72536cca | -10.4462 | -44.36753 | 2025-08-05 04:17:00 | NPP-375D | PARNAGUÁ | PIAUÍ | Brasil | 2207603 | 22 | 33 | nan | nan | nan | Cerrado | 2.6 |
| 9ae3deb5-6ad7-3cf6-a979-963767f28893 | -10.77429 | -46.64487 | 2025-08-05 04:17:00 | NPP-375D | MATEIROS | TOCANTINS | Brasil | 1712702 | 17 | 33 | nan | nan | nan | Cerrado | 1.7 |


[Clique aqui para ver as próximas entradas](README18.md)
