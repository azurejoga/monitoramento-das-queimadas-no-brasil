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

## Dados Diários - Página 12

| ID | Latitude | Longitude | Data/Hora GMT | Satélite | Município | Estado | País | Município ID | Estado ID | País ID | Dias sem Chuva | Precipitação | Risco de Fogo | Bioma | FRP |
|----|----------|-----------|---------------|----------|-----------|--------|------|--------------|-----------|---------|----------------|--------------|----------------|-------|-----|
| 1222430b-d1ca-3199-a970-c20e85ac1fe5 | -12.97876 | -44.88485 | 2025-08-06 03:57:00 | NPP-375D | SÃO DESIDÉRIO | BAHIA | Brasil | 2928901 | 29 | 33 | nan | nan | nan | Cerrado | 0.9 |
| 1aa006fd-ef7a-392e-854c-3cd149485d6e | -11.89901 | -44.97774 | 2025-08-06 03:57:00 | NPP-375D | RIACHÃO DAS NEVES | BAHIA | Brasil | 2926202 | 29 | 33 | nan | nan | nan | Cerrado | 2.4 |
| c05c32db-991e-31c8-887e-e73227e3e122 | -12.72693 | -46.39092 | 2025-08-06 03:57:00 | NPP-375D | AURORA DO TOCANTINS | TOCANTINS | Brasil | 1702703 | 17 | 33 | nan | nan | nan | Cerrado | 1.3 |
| a6dd3772-4749-3335-a894-f1a940190478 | -12.73352 | -46.39302 | 2025-08-06 03:57:00 | NPP-375D | AURORA DO TOCANTINS | TOCANTINS | Brasil | 1702703 | 17 | 33 | nan | nan | nan | Cerrado | 2.3 |
| 261f5dc1-9439-3d6e-ba19-6f769a5bcf1d | -9.55319 | -40.32309 | 2025-08-06 03:57:00 | NPP-375D | JUAZEIRO | BAHIA | Brasil | 2918407 | 29 | 33 | nan | nan | nan | Caatinga | 0.8 |
| a3f3882e-1d9f-3322-9102-069a0e1ed8b2 | -12.55087 | -44.73627 | 2025-08-06 03:57:00 | NPP-375D | SÃO DESIDÉRIO | BAHIA | Brasil | 2928901 | 29 | 33 | nan | nan | nan | Cerrado | 1.3 |
| 53ddf153-aa29-32a9-8b1f-a68b98b2d636 | -14.21769 | -39.77055 | 2025-08-06 03:57:00 | NPP-375D | ITAGIBÁ | BAHIA | Brasil | 2915205 | 29 | 33 | nan | nan | nan | Mata Atlântica | 0.7 |
| 6f92d526-22a9-3fde-a117-16849081db3e | -11.43282 | -45.13204 | 2025-08-06 03:57:00 | NPP-375D | RIACHÃO DAS NEVES | BAHIA | Brasil | 2926202 | 29 | 33 | nan | nan | nan | Cerrado | 8.5 |
| 0cf61be1-4765-32e4-9ad0-ebacab315662 | -11.75787 | -44.96019 | 2025-08-06 03:57:00 | NPP-375D | RIACHÃO DAS NEVES | BAHIA | Brasil | 2926202 | 29 | 33 | nan | nan | nan | Cerrado | 3.3 |
| 387602be-9060-350e-b509-c6b07149eadc | -11.9094 | -44.94383 | 2025-08-06 03:57:00 | NPP-375D | RIACHÃO DAS NEVES | BAHIA | Brasil | 2926202 | 29 | 33 | nan | nan | nan | Cerrado | 1.9 |
| 1af3131c-bff5-36b1-b88a-169507387d08 | -12.89666 | -43.79403 | 2025-08-06 03:57:00 | NPP-375D | SERRA DOURADA | BAHIA | Brasil | 2930303 | 29 | 33 | nan | nan | nan | Cerrado | 0.9 |
| 8ebf0a49-d9f4-3388-842c-3fe488bc74c6 | -9.6253 | -40.58911 | 2025-08-06 03:57:00 | NPP-375D | JUAZEIRO | BAHIA | Brasil | 2918407 | 29 | 33 | nan | nan | nan | Caatinga | 2.2 |
| e5f6dcbf-134e-3c70-b59e-09a0d29ec910 | -8.52957 | -47.47315 | 2025-08-06 03:57:00 | NPP-375D | ITACAJÁ | TOCANTINS | Brasil | 1710508 | 17 | 33 | nan | nan | nan | Cerrado | 1.4 |
| b70b77c7-82fd-3144-b4a7-8b79d65a09ea | -11.91257 | -44.92624 | 2025-08-06 03:57:00 | NPP-375D | RIACHÃO DAS NEVES | BAHIA | Brasil | 2926202 | 29 | 33 | nan | nan | nan | Cerrado | 3.8 |
| 656a0a16-5d23-3aee-9d71-2e2f3e5cb309 | -10.44212 | -44.36314 | 2025-08-06 03:57:00 | NPP-375D | PARNAGUÁ | PIAUÍ | Brasil | 2207603 | 22 | 33 | nan | nan | nan | Cerrado | 1.7 |
| 41656b2b-a3ae-3a38-a8ea-9f44f1101a18 | -9.07181 | -45.06008 | 2025-08-06 03:57:00 | NPP-375D | BOM JESUS | PIAUÍ | Brasil | 2201903 | 22 | 33 | nan | nan | nan | Cerrado | 4.0 |
| 5dce2eec-65f5-33ad-a34b-0ffd2be2af2f | -11.42861 | -45.13131 | 2025-08-06 03:57:00 | NPP-375D | RIACHÃO DAS NEVES | BAHIA | Brasil | 2926202 | 29 | 33 | nan | nan | nan | Cerrado | 8.5 |
| 3c64402f-ef40-3ec2-9831-ce502b303a50 | -8.75374 | -46.4176 | 2025-08-06 03:57:00 | NPP-375D | BALSAS | MARANHÃO | Brasil | 2101400 | 21 | 33 | nan | nan | nan | Cerrado | 2.2 |
| 78742fee-a3ff-3977-8823-8e1f0c0e0d6a | -8.83597 | -47.62387 | 2025-08-06 03:57:00 | NPP-375D | SANTA MARIA DO TOCANTINS | TOCANTINS | Brasil | 1718881 | 17 | 33 | nan | nan | nan | Cerrado | 4.3 |
| f42f5e3f-336a-3976-80b7-49aa6fa0ff8d | -10.64958 | -45.23651 | 2025-08-06 03:57:00 | NPP-375D | CRISTALÂNDIA DO PIAUÍ | PIAUÍ | Brasil | 2203008 | 22 | 33 | nan | nan | nan | Cerrado | 2.2 |
| 92e4919c-0f65-3416-a96e-a30a68dcb865 | -8.99191 | -45.69181 | 2025-08-06 03:57:00 | NPP-375D | SANTA FILOMENA | PIAUÍ | Brasil | 2209203 | 22 | 33 | nan | nan | nan | Cerrado | 1.8 |
| 81418f86-4cc5-3fef-a660-5ba1acdc8824 | -9.70717 | -51.94651 | 2025-08-06 03:57:00 | NPP-375D | SÃO FÉLIX DO XINGU | PARÁ | Brasil | 1507300 | 15 | 33 | nan | nan | nan | Amazônia | 1.4 |
| 24b1d4c7-e697-30a2-a091-1bdfad499d3f | -11.74832 | -44.99021 | 2025-08-06 03:57:00 | NPP-375D | RIACHÃO DAS NEVES | BAHIA | Brasil | 2926202 | 29 | 33 | nan | nan | nan | Cerrado | 0.8 |
| 18d305af-668e-3976-bcc3-1bf4397fbf60 | -12.72008 | -46.39074 | 2025-08-06 03:57:00 | NPP-375D | AURORA DO TOCANTINS | TOCANTINS | Brasil | 1702703 | 17 | 33 | nan | nan | nan | Cerrado | 1.0 |
| f33a88d6-4b81-3afa-9c89-edaecf99529c | -8.06942 | -49.71757 | 2025-08-06 03:57:00 | NPP-375D | CONCEIÇÃO DO ARAGUAIA | PARÁ | Brasil | 1502707 | 15 | 33 | nan | nan | nan | Amazônia | 1.2 |
| 55631778-515a-3e2d-8c9e-ea5d710fb68a | -12.89748 | -43.78937 | 2025-08-06 03:57:00 | NPP-375D | SERRA DOURADA | BAHIA | Brasil | 2930303 | 29 | 33 | nan | nan | nan | Cerrado | 1.1 |
| 9906c60d-9359-3e34-af8d-efe94fefd94c | -8.84642 | -47.60062 | 2025-08-06 03:57:00 | NPP-375D | SANTA MARIA DO TOCANTINS | TOCANTINS | Brasil | 1718881 | 17 | 33 | nan | nan | nan | Cerrado | 2.0 |
| 6bd9adc8-bc08-3200-af60-40fae84867ca | -11.49391 | -50.29321 | 2025-08-06 03:57:00 | NPP-375D | LAGOA DA CONFUSÃO | TOCANTINS | Brasil | 1711902 | 17 | 33 | nan | nan | nan | Cerrado | 3.2 |
| 12fa5012-cbcb-3a07-bdc9-ab0ebe854164 | -12.99764 | -44.89587 | 2025-08-06 03:57:00 | NPP-375D | SÃO DESIDÉRIO | BAHIA | Brasil | 2928901 | 29 | 33 | nan | nan | nan | Cerrado | 1.7 |
| 3766bc3c-8dac-3242-a9a1-e4764c393f31 | -11.74491 | -45.00957 | 2025-08-06 03:57:00 | NPP-375D | RIACHÃO DAS NEVES | BAHIA | Brasil | 2926202 | 29 | 33 | nan | nan | nan | Cerrado | 0.6 |
| 75c202b2-8753-3d27-9bb1-7bd543b96c12 | -9.64452 | -43.84684 | 2025-08-06 03:57:00 | NPP-375D | MORRO CABEÇA NO TEMPO | PIAUÍ | Brasil | 2206654 | 22 | 33 | nan | nan | nan | Caatinga | 2.0 |
| 0e51b22e-564e-3132-90e7-eb5ca8a80542 | -11.79396 | -45.00519 | 2025-08-06 03:57:00 | NPP-375D | RIACHÃO DAS NEVES | BAHIA | Brasil | 2926202 | 29 | 33 | nan | nan | nan | Cerrado | 0.9 |
| 8314e2f8-b383-31a0-883c-bf50a58bf0ea | -11.91669 | -44.92697 | 2025-08-06 03:57:00 | NPP-375D | RIACHÃO DAS NEVES | BAHIA | Brasil | 2926202 | 29 | 33 | nan | nan | nan | Cerrado | 3.8 |
| 578a8971-a603-34fd-9646-97763456e149 | -9.30382 | -40.24203 | 2025-08-06 03:57:00 | NPP-375D | JUAZEIRO | BAHIA | Brasil | 2918407 | 29 | 33 | nan | nan | nan | Caatinga | 4.3 |
| aafdf51e-c252-3919-9c75-24489b871214 | -12.71658 | -47.79765 | 2025-08-06 03:57:00 | NPP-375D | PARANÃ | TOCANTINS | Brasil | 1716208 | 17 | 33 | nan | nan | nan | Cerrado | 2.5 |
| 52d9c5ad-e5cf-3cd3-bebc-7e4c0b3915e1 | -9.07328 | -45.05566 | 2025-08-06 03:57:00 | NPP-375D | BOM JESUS | PIAUÍ | Brasil | 2201903 | 22 | 33 | nan | nan | nan | Cerrado | 3.8 |
| af234de5-d5ac-3797-986f-255e0956258b | -8.52883 | -47.44729 | 2025-08-06 03:57:00 | NPP-375D | ITACAJÁ | TOCANTINS | Brasil | 1710508 | 17 | 33 | nan | nan | nan | Cerrado | 1.4 |
| 62aa1cc7-fd31-344d-8c94-212749975274 | -11.43156 | -45.14028 | 2025-08-06 03:57:00 | NPP-375D | RIACHÃO DAS NEVES | BAHIA | Brasil | 2926202 | 29 | 33 | nan | nan | nan | Cerrado | 15.0 |
| 499d0ae6-790c-33f2-bb96-91a85edabce0 | -8.62396 | -50.02057 | 2025-08-06 03:57:00 | NPP-375D | SANTA MARIA DAS BARREIRAS | PARÁ | Brasil | 1506583 | 15 | 33 | nan | nan | nan | Amazônia | 2.4 |
| cd115ae9-c1a1-345f-8ed7-77ab654105b4 | -12.55891 | -44.73772 | 2025-08-06 03:57:00 | NPP-375D | SÃO DESIDÉRIO | BAHIA | Brasil | 2928901 | 29 | 33 | nan | nan | nan | Cerrado | 1.1 |
| 393e1f87-0c26-3bcc-b130-9fe1fb82133a | -13.86141 | -44.12694 | 2025-08-06 03:57:00 | NPP-375D | CORIBE | BAHIA | Brasil | 2909109 | 29 | 33 | nan | nan | nan | Cerrado | 1.1 |
| c063cb19-2a8b-3630-b3de-fa18886d4054 | -11.49731 | -44.26134 | 2025-08-06 03:57:00 | NPP-375D | COTEGIPE | BAHIA | Brasil | 2909406 | 29 | 33 | nan | nan | nan | Cerrado | 0.9 |
| 99f80add-9c0d-38ae-8520-b081d994bcb5 | -9.62809 | -40.59335 | 2025-08-06 03:57:00 | NPP-375D | JUAZEIRO | BAHIA | Brasil | 2918407 | 29 | 33 | nan | nan | nan | Caatinga | 1.1 |
| de6bf3e4-780a-38f7-b5e0-39930a6e175e | -11.76266 | -47.52897 | 2025-08-06 03:57:00 | NPP-375D | NATIVIDADE | TOCANTINS | Brasil | 1714203 | 17 | 33 | nan | nan | nan | Cerrado | 2.1 |
| 43fb5c21-3fc2-3503-afdd-91bc68b2b4eb | -9.6219 | -40.58855 | 2025-08-06 03:57:00 | NPP-375D | JUAZEIRO | BAHIA | Brasil | 2918407 | 29 | 33 | nan | nan | nan | Caatinga | 2.2 |
| 28ef762c-676d-3f2f-bfe3-5a811512e204 | -8.53936 | -47.48136 | 2025-08-06 03:57:00 | NPP-375D | ITACAJÁ | TOCANTINS | Brasil | 1710508 | 17 | 33 | nan | nan | nan | Cerrado | 0.7 |
| 7497b88c-8a12-3e53-ae54-7373a36054f4 | -11.91065 | -44.98411 | 2025-08-06 03:57:00 | NPP-375D | RIACHÃO DAS NEVES | BAHIA | Brasil | 2926202 | 29 | 33 | nan | nan | nan | Cerrado | 2.0 |
| b900e1fa-abbb-378a-be8d-bc709921f0c1 | -13.29947 | -39.86523 | 2025-08-06 03:57:00 | NPP-375D | SANTA INÊS | BAHIA | Brasil | 2927903 | 29 | 33 | nan | nan | nan | Mata Atlântica | 0.3 |
| 55d906fb-1cfe-3776-aa44-7b917e1c77d6 | -12.72245 | -46.39017 | 2025-08-06 03:57:00 | NPP-375D | AURORA DO TOCANTINS | TOCANTINS | Brasil | 1702703 | 17 | 33 | nan | nan | nan | Cerrado | 1.8 |
| 107b5509-8936-3d44-9522-a6491504666b | -9.70597 | -51.95261 | 2025-08-06 03:57:00 | NPP-375D | SÃO FÉLIX DO XINGU | PARÁ | Brasil | 1507300 | 15 | 33 | nan | nan | nan | Amazônia | 1.4 |
| 55cabac8-99a2-3c77-861e-36e819ae0e1c | -12.73506 | -46.39685 | 2025-08-06 03:57:00 | NPP-375D | AURORA DO TOCANTINS | TOCANTINS | Brasil | 1702703 | 17 | 33 | nan | nan | nan | Cerrado | 1.0 |
| ba6296db-0d3a-3e6d-8c89-f4f4d9cef8f2 | -10.44085 | -44.37048 | 2025-08-06 03:57:00 | NPP-375D | PARNAGUÁ | PIAUÍ | Brasil | 2207603 | 22 | 33 | nan | nan | nan | Cerrado | 1.4 |
| 4afc2cf4-3bb4-300f-8a10-19f3f4f832de | -15.11732 | -47.42908 | 2025-08-06 03:57:00 | NPP-375D | FORMOSA | GOIÁS | Brasil | 5208004 | 52 | 33 | nan | nan | nan | Cerrado | 4.4 |
| 6686a6f4-bca2-33fb-9fb8-33f78942329e | -11.72731 | -47.52806 | 2025-08-06 03:57:00 | NPP-375D | NATIVIDADE | TOCANTINS | Brasil | 1714203 | 17 | 33 | nan | nan | nan | Cerrado | 5.9 |
| 4ed39be8-8f52-3c01-a1bc-0082ada8bb86 | -12.55489 | -44.73699 | 2025-08-06 03:57:00 | NPP-375D | SÃO DESIDÉRIO | BAHIA | Brasil | 2928901 | 29 | 33 | nan | nan | nan | Cerrado | 1.1 |
| 3bc959ae-5b78-302e-b608-8edb3b5c4a84 | -12.99488 | -44.88779 | 2025-08-06 03:57:00 | NPP-375D | SÃO DESIDÉRIO | BAHIA | Brasil | 2928901 | 29 | 33 | nan | nan | nan | Cerrado | 1.5 |
| 96f146fd-b157-3777-91f1-edd4c4728d79 | -11.4323 | -45.13622 | 2025-08-06 03:57:00 | NPP-375D | RIACHÃO DAS NEVES | BAHIA | Brasil | 2926202 | 29 | 33 | nan | nan | nan | Cerrado | 22.2 |
| f6be0689-f1a7-32d8-a284-20cd0e6043dd | -11.84074 | -43.72216 | 2025-08-06 03:57:00 | NPP-375D | WANDERLEY | BAHIA | Brasil | 2933455 | 29 | 33 | nan | nan | nan | Cerrado | 3.5 |
| fc9c2d78-4767-3dd1-9990-878a376106d4 | -10.47497 | -44.34242 | 2025-08-06 03:57:00 | NPP-375D | JÚLIO BORGES | PIAUÍ | Brasil | 2205524 | 22 | 33 | nan | nan | nan | Cerrado | 1.5 |
| 42b2f911-a439-3952-bb94-b59dcb21e77a | -11.43374 | -45.12825 | 2025-08-06 03:57:00 | NPP-375D | RIACHÃO DAS NEVES | BAHIA | Brasil | 2926202 | 29 | 33 | nan | nan | nan | Cerrado | 3.8 |
| 50f0c924-0f3a-33ac-bf0c-7744ad7abb12 | -12.53821 | -47.17821 | 2025-08-06 03:57:00 | NPP-375D | ARRAIAS | TOCANTINS | Brasil | 1702406 | 17 | 33 | nan | nan | nan | Cerrado | 3.1 |
| 596bbc19-666d-3c32-8c3a-4a38171efcb7 | -8.8371 | -47.61752 | 2025-08-06 03:57:00 | NPP-375D | SANTA MARIA DO TOCANTINS | TOCANTINS | Brasil | 1718881 | 17 | 33 | nan | nan | nan | Cerrado | 2.9 |
| da0a0836-b48d-3212-9087-7548317227bc | -12.75874 | -44.41684 | 2025-08-06 03:57:00 | NPP-375D | BAIANÓPOLIS | BAHIA | Brasil | 2902500 | 29 | 33 | nan | nan | nan | Cerrado | 0.9 |
| e772a807-0bfc-32a5-ad28-fba2902c464e | -10.48152 | -44.37745 | 2025-08-06 03:57:00 | NPP-375D | PARNAGUÁ | PIAUÍ | Brasil | 2207603 | 22 | 33 | nan | nan | nan | Cerrado | 0.9 |
| dfb4871c-506d-34a4-b497-409bd4a92725 | -8.83658 | -47.62479 | 2025-08-06 03:57:00 | NPP-375D | SANTA MARIA DO TOCANTINS | TOCANTINS | Brasil | 1718881 | 17 | 33 | nan | nan | nan | Cerrado | 3.2 |
| 9f75273b-fe7a-3ac7-a3a7-74bf892981da | -12.9862 | -44.88984 | 2025-08-06 03:57:00 | NPP-375D | SÃO DESIDÉRIO | BAHIA | Brasil | 2928901 | 29 | 33 | nan | nan | nan | Cerrado | 1.3 |
| c86b0e45-585b-3c11-b45b-2228e49fa100 | -10.43073 | -44.38049 | 2025-08-06 03:57:00 | NPP-375D | PARNAGUÁ | PIAUÍ | Brasil | 2207603 | 22 | 33 | nan | nan | nan | Cerrado | 0.9 |
| ad6be349-53ce-33c3-961b-c06b7c733e6c | -11.43212 | -45.13607 | 2025-08-06 03:57:00 | NPP-375D | RIACHÃO DAS NEVES | BAHIA | Brasil | 2926202 | 29 | 33 | nan | nan | nan | Cerrado | 8.5 |
| 4275ce32-23f3-317f-abbc-fe702383f3c2 | -11.89758 | -44.97411 | 2025-08-06 03:57:00 | NPP-375D | RIACHÃO DAS NEVES | BAHIA | Brasil | 2926202 | 29 | 33 | nan | nan | nan | Cerrado | 0.8 |
| e65260c1-a791-3ed5-a9f9-f837feec5873 | -8.87974 | -44.79011 | 2025-08-06 03:57:00 | NPP-375D | CURRAIS | PIAUÍ | Brasil | 2203230 | 22 | 33 | nan | nan | nan | Cerrado | 3.1 |
| 16a37f7f-f7a6-3006-bb3c-fda1434fb2e5 | -11.98772 | -42.20283 | 2025-08-06 03:57:00 | NPP-375D | BARRA DO MENDES | BAHIA | Brasil | 2903003 | 29 | 33 | nan | nan | nan | Caatinga | 0.5 |
| 6761009a-7fbd-3a85-8eb5-c42831174310 | -11.73397 | -47.54704 | 2025-08-06 03:57:00 | NPP-375D | NATIVIDADE | TOCANTINS | Brasil | 1714203 | 17 | 33 | nan | nan | nan | Cerrado | 1.3 |
| 90844626-01b7-3457-9f57-3b02852bba7e | -12.55427 | -44.74056 | 2025-08-06 03:57:00 | NPP-375D | SÃO DESIDÉRIO | BAHIA | Brasil | 2928901 | 29 | 33 | nan | nan | nan | Cerrado | 1.4 |
| a13dcc88-5976-3d3a-9adc-6630123c9457 | -11.4389 | -45.1385 | 2025-08-06 04:00:00 | GOES-19 | RIACHÃO DAS NEVES | BAHIA | Brasil | 2926202 | 29 | 33 | nan | nan | nan | Cerrado | 89.5 |
| e319e3db-0180-311e-a126-75db6af2f85d | -13.0728 | -56.8729 | 2025-08-06 04:00:00 | GOES-19 | NOVA MARINGÁ | MATO GROSSO | Brasil | 5108907 | 51 | 33 | nan | nan | nan | Amazônia | 52.0 |
| 73bd383f-edda-37e1-b740-282c13779bb7 | -8.9213 | -60.7489 | 2025-08-06 04:00:00 | GOES-19 | COLNIZA | MATO GROSSO | Brasil | 5103254 | 51 | 33 | nan | nan | nan | Amazônia | 75.9 |
| 8bddd560-1116-3f09-8b5f-9a2c09adf44b | -13.0731 | -56.8527 | 2025-08-06 04:00:00 | GOES-19 | NOVA MARINGÁ | MATO GROSSO | Brasil | 5108907 | 51 | 33 | nan | nan | nan | Amazônia | 55.0 |
| d6d50747-fd75-36d7-acdf-cf74ab34afea | -8.9028 | -60.7498 | 2025-08-06 04:00:00 | GOES-19 | COLNIZA | MATO GROSSO | Brasil | 5103254 | 51 | 33 | nan | nan | nan | Amazônia | 52.4 |
| d3c9fea4-4d4c-347e-90fe-eb6f7f66f12c | -8.9215 | -60.7297 | 2025-08-06 04:00:00 | GOES-19 | COLNIZA | MATO GROSSO | Brasil | 5103254 | 51 | 33 | nan | nan | nan | Amazônia | 47.4 |
| e6bf95a6-64e5-374f-b151-ad86842c4415 | -19.84788 | -51.20195 | 2025-08-06 04:00:00 | NPP-375D | PARANAÍBA | MATO GROSSO DO SUL | Brasil | 5006309 | 50 | 33 | nan | nan | nan | Cerrado | 1.2 |
| 03620e26-34a2-39b6-a423-fae87ec2a8eb | -16.34223 | -50.35161 | 2025-08-06 04:00:00 | NPP-375D | SÃO LUÍS DE MONTES BELOS | GOIÁS | Brasil | 5220108 | 52 | 33 | nan | nan | nan | Cerrado | 1.0 |
| 814c89e2-37af-31e7-bab5-3c43375e935f | -16.32995 | -50.35638 | 2025-08-06 04:00:00 | NPP-375D | SÃO LUÍS DE MONTES BELOS | GOIÁS | Brasil | 5220108 | 52 | 33 | nan | nan | nan | Cerrado | 1.1 |
| 81e7e4b6-9ef1-3fe0-ae4e-73a28cd19031 | -15.69334 | -48.96711 | 2025-08-06 04:00:00 | NPP-375D | PIRENÓPOLIS | GOIÁS | Brasil | 5217302 | 52 | 33 | nan | nan | nan | Cerrado | 2.5 |
| b0e88fb7-089a-32de-adf3-b18dfc83897b | -21.02314 | -50.04455 | 2025-08-06 04:00:00 | NPP-375D | ZACARIAS | SÃO PAULO | Brasil | 3557154 | 35 | 33 | nan | nan | nan | Mata Atlântica | 2.0 |
| 35ddc69d-fdef-3fd5-9260-c4b16233e2ee | -15.70488 | -48.96641 | 2025-08-06 04:00:00 | NPP-375D | PIRENÓPOLIS | GOIÁS | Brasil | 5217302 | 52 | 33 | nan | nan | nan | Cerrado | 0.6 |
| b4851653-7786-3665-aa43-f9f4ac6d4c7d | -21.01227 | -50.04816 | 2025-08-06 04:00:00 | NPP-375D | ZACARIAS | SÃO PAULO | Brasil | 3557154 | 35 | 33 | nan | nan | nan | Mata Atlântica | 0.4 |
| 47bd7925-bbc2-3fc5-9483-23c435cd777e | -16.34144 | -50.35542 | 2025-08-06 04:00:00 | NPP-375D | SÃO LUÍS DE MONTES BELOS | GOIÁS | Brasil | 5220108 | 52 | 33 | nan | nan | nan | Cerrado | 1.0 |
| 2210a020-7e9b-31da-9205-99614ca51dc2 | -21.07163 | -49.99167 | 2025-08-06 04:00:00 | NPP-375D | ZACARIAS | SÃO PAULO | Brasil | 3557154 | 35 | 33 | nan | nan | nan | Mata Atlântica | 7.3 |
| 7987e07e-a5d9-3a93-a21b-d97fcc672560 | -21.02481 | -50.0458 | 2025-08-06 04:00:00 | NPP-375D | ZACARIAS | SÃO PAULO | Brasil | 3557154 | 35 | 33 | nan | nan | nan | Mata Atlântica | 1.3 |
| 048a4acc-dc29-386e-9b92-82e77799621c | -16.33071 | -50.35269 | 2025-08-06 04:00:00 | NPP-375D | SÃO LUÍS DE MONTES BELOS | GOIÁS | Brasil | 5220108 | 52 | 33 | nan | nan | nan | Cerrado | 0.5 |
| a6ac0883-58ea-315a-acc6-0942ada6a624 | -21.07758 | -49.98737 | 2025-08-06 04:00:00 | NPP-375D | ZACARIAS | SÃO PAULO | Brasil | 3557154 | 35 | 33 | nan | nan | nan | Mata Atlântica | 7.5 |
| a1fea3a8-3c3d-3ff1-b319-fa015edad8a9 | -21.31193 | -48.5682 | 2025-08-06 04:00:00 | NPP-375D | MONTE ALTO | SÃO PAULO | Brasil | 3531308 | 35 | 33 | nan | nan | nan | Cerrado | 0.7 |
| fd846193-626a-3d67-b8e9-2a65e0024670 | -21.07528 | -49.99841 | 2025-08-06 04:00:00 | NPP-375D | ZACARIAS | SÃO PAULO | Brasil | 3557154 | 35 | 33 | nan | nan | nan | Mata Atlântica | 7.3 |
| bbc6999d-59f2-3f42-9aeb-fe9d67732b73 | -21.0183 | -50.04342 | 2025-08-06 04:00:00 | NPP-375D | ZACARIAS | SÃO PAULO | Brasil | 3557154 | 35 | 33 | nan | nan | nan | Mata Atlântica | 0.4 |
| 80cc8264-ccb1-3ea0-ad0e-65195f9e42ac | -16.33685 | -50.35032 | 2025-08-06 04:00:00 | NPP-375D | SÃO LUÍS DE MONTES BELOS | GOIÁS | Brasil | 5220108 | 52 | 33 | nan | nan | nan | Cerrado | 0.5 |
| e36e0660-2861-34c1-b56d-a7f4d9b20b41 | -15.70435 | -48.96914 | 2025-08-06 04:00:00 | NPP-375D | PIRENÓPOLIS | GOIÁS | Brasil | 5217302 | 52 | 33 | nan | nan | nan | Cerrado | 0.6 |
| 1f5a111f-d9e8-35e3-9e23-b75d7e21709f | -17.83369 | -55.10488 | 2025-08-06 04:00:00 | NPP-375D | SONORA | MATO GROSSO DO SUL | Brasil | 5007935 | 50 | 33 | nan | nan | nan | Pantanal | 1.8 |
| de256529-db31-392f-b384-dbab29efa6a1 | -21.01998 | -50.04467 | 2025-08-06 04:00:00 | NPP-375D | ZACARIAS | SÃO PAULO | Brasil | 3557154 | 35 | 33 | nan | nan | nan | Mata Atlântica | 1.3 |
| fd9f36bb-c01a-3dcd-9016-2b504fc55619 | -15.68851 | -48.97018 | 2025-08-06 04:00:00 | NPP-375D | PIRENÓPOLIS | GOIÁS | Brasil | 5217302 | 52 | 33 | nan | nan | nan | Cerrado | 2.1 |
| e38b01da-bafc-3ccd-8cc4-631ac2b9c7b6 | -19.16161 | -40.94305 | 2025-08-06 04:00:00 | NPP-375D | RESPLENDOR | MINAS GERAIS | Brasil | 3154309 | 31 | 33 | nan | nan | nan | Mata Atlântica | 0.4 |


[Clique aqui para ver as próximas entradas](README13.md)
