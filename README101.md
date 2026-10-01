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

## Dados Diários - Página 101

| ID | Latitude | Longitude | Data/Hora GMT | Satélite | Município | Estado | País | Município ID | Estado ID | País ID | Dias sem Chuva | Precipitação | Risco de Fogo | Bioma | FRP |
|----|----------|-----------|---------------|----------|-----------|--------|------|--------------|-----------|---------|----------------|--------------|----------------|-------|-----|
| f72d9d93-c20e-3596-a6f8-4fd2f5c82e73 | -8.0166 | -42.8681 | 2026-10-01 14:00:00 | GOES-19 | PAJEÚ DO PIAUÍ | PIAUÍ | Brasil | 2207355 | 22 | 33 | nan | nan | nan | Caatinga | 77.3 |
| 2f9ee026-4945-3596-988e-20812295c6d5 | -9.88 | -44.9783 | 2026-10-01 14:00:00 | GOES-19 | RIACHO FRIO | PIAUÍ | Brasil | 2208858 | 22 | 33 | nan | nan | nan | Cerrado | 114.0 |
| 60501420-8165-3336-857b-0af7dccf9ca1 | -11.7187 | -43.4148 | 2026-10-01 14:00:00 | GOES-19 | BARRA | BAHIA | Brasil | 2902708 | 29 | 33 | nan | nan | nan | Cerrado | 136.5 |
| 8ce96339-dae3-3245-a575-b3b460c1ea43 | -11.4294 | -43.507 | 2026-10-01 14:00:00 | GOES-19 | BARRA | BAHIA | Brasil | 2902708 | 29 | 33 | nan | nan | nan | Cerrado | 668.6 |
| b84f84f2-0be9-3892-853c-956ad778875a | -9.2243 | -45.8074 | 2026-10-01 14:00:00 | GOES-19 | SANTA FILOMENA | PIAUÍ | Brasil | 2209203 | 22 | 33 | nan | nan | nan | Cerrado | 62.7 |
| e75e9589-bc30-3ade-85d3-46cd87139c2a | -7.3776 | -42.6517 | 2026-10-01 14:00:00 | GOES-19 | SÃO JOSÉ DO PEIXE | PIAUÍ | Brasil | 2210102 | 22 | 33 | nan | nan | nan | Caatinga | 77.8 |
| 13b4b699-4cb8-3641-ae5b-1f691df57fd8 | -9.8803 | -44.9553 | 2026-10-01 14:00:00 | GOES-19 | RIACHO FRIO | PIAUÍ | Brasil | 2208858 | 22 | 33 | nan | nan | nan | Cerrado | 340.6 |
| 8c8827fb-4ea7-35e7-8aed-ef45bb74f9e1 | -10.2067 | -49.9898 | 2026-10-01 14:10:00 | GOES-19 | PIUM | TOCANTINS | Brasil | 1717503 | 17 | 33 | nan | nan | nan | Cerrado | 68.0 |
| 573a9fe7-5068-3d0a-848d-de424b3f7aa4 | -8.6259 | -45.3737 | 2026-10-01 14:10:00 | GOES-19 | BAIXA GRANDE DO RIBEIRO | PIAUÍ | Brasil | 2201150 | 22 | 33 | nan | nan | nan | Cerrado | 59.3 |
| ba0cf6bb-9fd2-35da-b818-905c4d445f3d | -11.2282 | -45.1682 | 2026-10-01 14:10:00 | GOES-19 | FORMOSA DO RIO PRETO | BAHIA | Brasil | 2911105 | 29 | 33 | nan | nan | nan | Cerrado | 104.3 |
| 93e580de-808d-3e38-96f3-59c9b96f021e | -7.3967 | -42.6261 | 2026-10-01 14:10:00 | GOES-19 | SÃO JOSÉ DO PEIXE | PIAUÍ | Brasil | 2210102 | 22 | 33 | nan | nan | nan | Caatinga | 90.7 |
| 6c569b96-fd5f-3cb2-b8eb-3a16c2ec5d0c | -7.4156 | -42.6241 | 2026-10-01 14:10:00 | GOES-19 | SÃO JOSÉ DO PEIXE | PIAUÍ | Brasil | 2210102 | 22 | 33 | nan | nan | nan | Caatinga | 90.4 |
| 7fe790f3-39f6-37ae-857a-1a2e057ee573 | -7.3278 | -42.0858 | 2026-10-01 14:10:00 | GOES-19 | COLÔNIA DO PIAUÍ | PIAUÍ | Brasil | 2202778 | 22 | 33 | nan | nan | nan | Caatinga | 83.2 |
| d1694ba3-4e36-3a85-973d-81eb304f0655 | -12.9036 | -44.8217 | 2026-10-01 14:10:00 | GOES-19 | SÃO DESIDÉRIO | BAHIA | Brasil | 2928901 | 29 | 33 | nan | nan | nan | Cerrado | 120.7 |
| 3bc2b365-7844-3279-a6c5-e880f4d93bfc | -9.7877 | -44.8058 | 2026-10-01 14:10:00 | GOES-19 | RIACHO FRIO | PIAUÍ | Brasil | 2208858 | 22 | 33 | nan | nan | nan | Cerrado | 94.6 |
| 58f4b3e5-3272-321c-9016-70772435e687 | -10.6889 | -50.6658 | 2026-10-01 14:10:00 | GOES-19 | LUCIARA | MATO GROSSO | Brasil | 5105309 | 51 | 33 | nan | nan | nan | Cerrado | 80.5 |
| 4a1d3178-0bc4-3410-86d0-05ba571673bd | -11.4123 | -43.3913 | 2026-10-01 14:10:00 | GOES-19 | BARRA | BAHIA | Brasil | 2902708 | 29 | 33 | nan | nan | nan | Cerrado | 178.6 |
| f92e799f-7a80-3ea4-a823-57a5cb2acf26 | -12.4539 | -44.1702 | 2026-10-01 14:10:00 | GOES-19 | TABOCAS DO BREJO VELHO | BAHIA | Brasil | 2930907 | 29 | 33 | nan | nan | nan | Cerrado | 537.7 |
| a492cc44-80ba-31ab-98fc-565aef921600 | -7.7221 | -54.7913 | 2026-10-01 14:10:00 | GOES-19 | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 79.0 |
| 4d7bda22-4cb4-309e-9326-bb184ef67912 | -7.1581 | -42.0792 | 2026-10-01 14:10:00 | GOES-19 | OEIRAS | PIAUÍ | Brasil | 2207009 | 22 | 33 | nan | nan | nan | Caatinga | 66.2 |
| 43a114e2-111b-303c-8c1e-59ae159f7060 | -10.1881 | -49.9703 | 2026-10-01 14:10:00 | GOES-19 | PIUM | TOCANTINS | Brasil | 1717503 | 17 | 33 | nan | nan | nan | Cerrado | 66.9 |
| 1cd4903c-7b94-34fb-85d4-24dc24d8e9a1 | -15.6481 | -44.7217 | 2026-10-01 14:10:00 | GOES-19 | JANUÁRIA | MINAS GERAIS | Brasil | 3135209 | 31 | 33 | nan | nan | nan | Cerrado | 188.4 |
| 54e0e572-fcd7-3092-bc09-8bca604364f9 | -11.6203 | -43.5485 | 2026-10-01 14:10:00 | GOES-19 | BARRA | BAHIA | Brasil | 2902708 | 29 | 33 | nan | nan | nan | Cerrado | 418.4 |
| 1c777d6c-4f52-341e-aa0f-8081a25fdde5 | -5.8597 | -53.479 | 2026-10-01 14:10:00 | GOES-19 | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 123.2 |
| a373adae-0491-3d70-9771-67f0ea74b1c1 | -9.0247 | -49.6549 | 2026-10-01 14:10:00 | GOES-19 | ARAGUACEMA | TOCANTINS | Brasil | 1701903 | 17 | 33 | nan | nan | nan | Cerrado | 65.3 |
| 422d9b81-ef93-3183-8946-9a183c01174b | -11.4294 | -43.507 | 2026-10-01 14:10:00 | GOES-19 | BARRA | BAHIA | Brasil | 2902708 | 29 | 33 | nan | nan | nan | Cerrado | 486.8 |
| d6ff62a9-bbbf-32f9-96e2-916b93f0d556 | -8.6268 | -45.3054 | 2026-10-01 14:10:00 | GOES-19 | BAIXA GRANDE DO RIBEIRO | PIAUÍ | Brasil | 2201150 | 22 | 33 | nan | nan | nan | Cerrado | 110.2 |
| 3d81e64e-c3d9-33a4-919d-f7edce6119f0 | -11.6395 | -43.5455 | 2026-10-01 14:10:00 | GOES-19 | BARRA | BAHIA | Brasil | 2902708 | 29 | 33 | nan | nan | nan | Cerrado | 190.7 |
| 4cb28955-8c26-3031-9a43-44a08d6ee8a4 | -11.6011 | -43.5515 | 2026-10-01 14:10:00 | GOES-19 | BARRA | BAHIA | Brasil | 2902708 | 29 | 33 | nan | nan | nan | Cerrado | 165.4 |
| efbf0b96-da52-34f8-8219-f6fd7f94c622 | -7.3779 | -42.628 | 2026-10-01 14:10:00 | GOES-19 | SÃO JOSÉ DO PEIXE | PIAUÍ | Brasil | 2210102 | 22 | 33 | nan | nan | nan | Caatinga | 84.7 |
| 7e2818ac-2fa7-38b4-9765-177316a4e611 | -10.6333 | -50.5864 | 2026-10-01 14:10:00 | GOES-19 | SANTA TEREZINHA | MATO GROSSO | Brasil | 5107776 | 51 | 33 | nan | nan | nan | Cerrado | 60.1 |
| f831b9a6-44ff-30b9-9b92-960bfd90990a | -7.7219 | -54.8114 | 2026-10-01 14:10:00 | GOES-19 | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 57.6 |
| 8afb3eb7-e9b4-3235-8dbf-2c757c7ec46f | -11.4298 | -43.4833 | 2026-10-01 14:10:00 | GOES-19 | BARRA | BAHIA | Brasil | 2902708 | 29 | 33 | nan | nan | nan | Cerrado | 144.6 |
| ff6cbc70-8c7a-3a6a-845a-11bb91939a5c | -9.825 | -44.8472 | 2026-10-01 14:10:00 | GOES-19 | RIACHO FRIO | PIAUÍ | Brasil | 2208858 | 22 | 33 | nan | nan | nan | Cerrado | 250.6 |
| 2612e8bc-be61-3c45-b00b-1a1acdb5e8fd | -11.6207 | -43.5248 | 2026-10-01 14:10:00 | GOES-19 | BARRA | BAHIA | Brasil | 2902708 | 29 | 33 | nan | nan | nan | Cerrado | 179.7 |
| dbd8f5c2-1962-3b68-9e27-b05cfd4b5a26 | -5.9152 | -53.4762 | 2026-10-01 14:10:00 | GOES-19 | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 103.1 |
| e030ca68-2876-3312-967d-22f234fbbbf9 | -12.4732 | -44.167 | 2026-10-01 14:10:00 | GOES-19 | TABOCAS DO BREJO VELHO | BAHIA | Brasil | 2930907 | 29 | 33 | nan | nan | nan | Cerrado | 260.5 |
| 3cef2f77-aadc-3b7b-8aa8-9ddc3b7fcb9f | -11.1232 | -44.6056 | 2026-10-01 14:10:00 | GOES-19 | SANTA RITA DE CÁSSIA | BAHIA | Brasil | 2928406 | 29 | 33 | nan | nan | nan | Cerrado | 166.3 |
| 71ec9a00-3a13-3c48-9c8e-01851ea9c460 | -11.3931 | -43.3942 | 2026-10-01 14:10:00 | GOES-19 | BARRA | BAHIA | Brasil | 2902708 | 29 | 33 | nan | nan | nan | Cerrado | 170.8 |
| da782fa6-b74f-37ed-9aa7-fa9e0596d507 | -10.9262 | -43.8406 | 2026-10-01 14:10:00 | GOES-19 | BARRA | BAHIA | Brasil | 2902708 | 29 | 33 | nan | nan | nan | Cerrado | 123.6 |
| 69cccef1-6b65-321b-9551-9ef2a93e3612 | -9.0742 | -47.1668 | 2026-10-01 14:10:00 | GOES-19 | LIZARDA | TOCANTINS | Brasil | 1712405 | 17 | 33 | nan | nan | nan | Cerrado | 62.4 |
| 07302d22-df0e-366b-8170-41dfb2824de9 | -5.8412 | -53.4799 | 2026-10-01 14:10:00 | GOES-19 | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 107.6 |
| 64365264-37a0-3ca2-9bfe-202afc77b081 | -9.8803 | -44.9553 | 2026-10-01 14:10:00 | GOES-19 | RIACHO FRIO | PIAUÍ | Brasil | 2208858 | 22 | 33 | nan | nan | nan | Cerrado | 310.9 |
| b862d26d-d13e-3da0-b7c7-5b49359ba683 | -11.7187 | -43.4148 | 2026-10-01 14:10:00 | GOES-19 | BARRA | BAHIA | Brasil | 2902708 | 29 | 33 | nan | nan | nan | Cerrado | 130.5 |
| 9d153b84-28cd-3ca6-b081-a59a4dece296 | -5.8411 | -53.5002 | 2026-10-01 14:10:00 | GOES-19 | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 90.9 |
| 05cb893c-e196-3c1c-9d62-4b445fb3b879 | -11.4127 | -43.3675 | 2026-10-01 14:10:00 | GOES-19 | BARRA | BAHIA | Brasil | 2902708 | 29 | 33 | nan | nan | nan | Cerrado | 149.4 |
| 062021f1-db54-37f6-8060-b377293270c8 | -14.659 | -41.0175 | 2026-10-01 14:10:00 | GOES-19 | ANAGÉ | BAHIA | Brasil | 2901205 | 29 | 33 | nan | nan | nan | Caatinga | 129.9 |
| 32fe9686-f391-307b-bf00-0265d1b8f617 | -12.6455 | -47.3048 | 2026-10-01 14:10:00 | GOES-19 | PARANÃ | TOCANTINS | Brasil | 1716208 | 17 | 33 | nan | nan | nan | Cerrado | 62.8 |
| afc59fd5-95ed-31f7-9f6f-2ba048980cae | -11.3935 | -43.3705 | 2026-10-01 14:10:00 | GOES-19 | BARRA | BAHIA | Brasil | 2902708 | 29 | 33 | nan | nan | nan | Cerrado | 189.8 |
| 002aa302-67c7-3c8e-800f-44161c1ea3df | -9.1335 | -49.987 | 2026-10-01 14:10:00 | GOES-19 | SANTANA DO ARAGUAIA | PARÁ | Brasil | 1506708 | 15 | 33 | nan | nan | nan | Amazônia | 52.2 |
| 00718061-977d-3a91-af3c-d4c4daa761ea | -12.4346 | -44.1733 | 2026-10-01 14:10:00 | GOES-19 | TABOCAS DO BREJO VELHO | BAHIA | Brasil | 2930907 | 29 | 33 | nan | nan | nan | Cerrado | 156.5 |
| 7e30d461-f6f6-3c6e-9b48-13e19d81ee9d | -14.3574 | -44.7569 | 2026-10-01 14:10:00 | GOES-19 | COCOS | BAHIA | Brasil | 2908101 | 29 | 33 | nan | nan | nan | Cerrado | 267.0 |
| e2bd3e84-4332-31a9-b029-8cf2e6746d5c | -9.1525 | -49.9639 | 2026-10-01 14:10:00 | GOES-19 | SANTANA DO ARAGUAIA | PARÁ | Brasil | 1506708 | 15 | 33 | nan | nan | nan | Amazônia | 55.8 |
| a78d30cb-601b-3c8d-9501-d1f36a04ab9d | -16.9909 | -45.4594 | 2026-10-01 14:10:00 | GOES-19 | BURITIZEIRO | MINAS GERAIS | Brasil | 3109402 | 31 | 33 | nan | nan | nan | Cerrado | 108.8 |
| 4f959f0d-eb2b-3773-96f5-f26f0ddb4ddc | -12.6463 | -47.2598 | 2026-10-01 14:10:00 | GOES-19 | PARANÃ | TOCANTINS | Brasil | 1716208 | 17 | 33 | nan | nan | nan | Cerrado | 39.2 |
| 9a0f6135-6c90-32b3-9907-fb87f65d1e5a | -14.5035 | -45.1981 | 2026-10-01 14:10:00 | GOES-19 | COCOS | BAHIA | Brasil | 2908101 | 29 | 33 | nan | nan | nan | Cerrado | 112.4 |
| f79656e7-0cba-3b75-89c9-300feeab08b8 | -11.4106 | -43.4862 | 2026-10-01 14:10:00 | GOES-19 | BARRA | BAHIA | Brasil | 2902708 | 29 | 33 | nan | nan | nan | Cerrado | 144.4 |
| 4e1a819b-892e-3582-be60-2f1519bda89c | -7.3965 | -42.6498 | 2026-10-01 14:10:00 | GOES-19 | SÃO JOSÉ DO PEIXE | PIAUÍ | Brasil | 2210102 | 22 | 33 | nan | nan | nan | Caatinga | 92.0 |
| ccf3331f-a499-3a8d-abae-1e1cba829a7c | -14.3379 | -44.7605 | 2026-10-01 14:10:00 | GOES-19 | COCOS | BAHIA | Brasil | 2908101 | 29 | 33 | nan | nan | nan | Cerrado | 95.9 |
| 5ec31f04-e569-3b24-9427-8af84858a40c | -11.6588 | -43.5425 | 2026-10-01 14:10:00 | GOES-19 | BARRA | BAHIA | Brasil | 2902708 | 29 | 33 | nan | nan | nan | Cerrado | 529.9 |
| 62385dfc-bd80-3de0-908b-7192f2b198c1 | -7.4977 | -54.9854 | 2026-10-01 14:10:00 | GOES-19 | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 63.5 |
| 168769cd-bb88-3707-b6d3-255a6e9cb703 | -8.0355 | -42.866 | 2026-10-01 14:10:00 | GOES-19 | PAJEÚ DO PIAUÍ | PIAUÍ | Brasil | 2207355 | 22 | 33 | nan | nan | nan | Caatinga | 84.0 |
| ae68471f-60cd-358e-ba24-b79755c82455 | -10.1878 | -49.9918 | 2026-10-01 14:10:00 | GOES-19 | PIUM | TOCANTINS | Brasil | 1717503 | 17 | 33 | nan | nan | nan | Cerrado | 56.5 |
| fc2e5608-4ac5-3fcd-a57f-fc62ee6966b8 | -8.3211 | -44.1447 | 2026-10-01 14:10:00 | GOES-19 | MANOEL EMÍDIO | PIAUÍ | Brasil | 2205904 | 22 | 33 | nan | nan | nan | Cerrado | 105.2 |
| dcde9fcd-49b7-3110-a320-e0ebe996a400 | -6.9419 | -42.8598 | 2026-10-01 14:10:00 | GOES-19 | FLORIANO | PIAUÍ | Brasil | 2203909 | 22 | 33 | nan | nan | nan | Caatinga | 109.3 |
| 7537a0f8-8968-327d-96a9-02e35a251283 | -10.5388 | -45.3759 | 2026-10-01 14:10:00 | GOES-19 | CORRENTE | PIAUÍ | Brasil | 2202901 | 22 | 33 | nan | nan | nan | Cerrado | 162.9 |
| 24accebe-10dc-3821-b658-c30fd291ae97 | -7.7224 | -54.751 | 2026-10-01 14:10:00 | GOES-19 | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 51.5 |
| 03d15392-28c4-3eae-9414-01b55730ff46 | -9.481 | -46.3871 | 2026-10-01 14:10:00 | GOES-19 | ALTO PARNAÍBA | MARANHÃO | Brasil | 2100501 | 21 | 33 | nan | nan | nan | Cerrado | 69.5 |
| e99ebb61-3ea4-3b52-8788-3c25b542687c | -15.5175 | -46.1257 | 2026-10-01 14:10:00 | GOES-19 | ARINOS | MINAS GERAIS | Brasil | 3104502 | 31 | 33 | nan | nan | nan | Cerrado | 181.5 |
| 31ec8c8c-99e1-303c-8b45-fb9c951060fb | -12.6263 | -47.3075 | 2026-10-01 14:10:00 | GOES-19 | PARANÃ | TOCANTINS | Brasil | 1716208 | 17 | 33 | nan | nan | nan | Cerrado | 64.0 |
| 206a290f-512a-334d-8546-7f1ab24886e7 | -12.6267 | -47.2851 | 2026-10-01 14:10:00 | GOES-19 | PARANÃ | TOCANTINS | Brasil | 1716208 | 17 | 33 | nan | nan | nan | Cerrado | 65.4 |
| 75129aab-40ee-3105-ace4-e3e853a4f9d2 | -6.3665 | -55.1461 | 2026-10-01 14:10:00 | GOES-19 | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 69.4 |
| 73441cac-5659-3c9c-ba7c-5b31bcf168c5 | -13.3297 | -43.8097 | 2026-10-01 14:10:00 | GOES-19 | SERRA DO RAMALHO | BAHIA | Brasil | 2930154 | 29 | 33 | nan | nan | nan | Cerrado | 130.1 |
| 89704daf-506b-3427-83b2-612d5525c76f | -9.1337 | -49.9656 | 2026-10-01 14:10:00 | GOES-19 | SANTANA DO ARAGUAIA | PARÁ | Brasil | 1506708 | 15 | 33 | nan | nan | nan | Amazônia | 61.9 |
| b5c93161-7e06-37e8-96e6-cebe65d9c45b | -12.6643 | -47.3245 | 2026-10-01 14:10:00 | GOES-19 | PARANÃ | TOCANTINS | Brasil | 1716208 | 17 | 33 | nan | nan | nan | Cerrado | 54.1 |
| 58e93f2e-93c8-3082-b4bc-0f2a4a9cd4b8 | -10.67 | -50.6678 | 2026-10-01 14:10:00 | GOES-19 | SANTA TEREZINHA | MATO GROSSO | Brasil | 5107776 | 51 | 33 | nan | nan | nan | Cerrado | 62.9 |
| bee43d61-04a2-3e38-9ad7-575e4382fc48 | -12.6271 | -47.2626 | 2026-10-01 14:10:00 | GOES-19 | PARANÃ | TOCANTINS | Brasil | 1716208 | 17 | 33 | nan | nan | nan | Cerrado | 54.7 |
| b11e251a-0bcb-3d5d-92e2-2ccdb004df01 | -8.6265 | -45.3282 | 2026-10-01 14:10:00 | GOES-19 | BAIXA GRANDE DO RIBEIRO | PIAUÍ | Brasil | 2201150 | 22 | 33 | nan | nan | nan | Cerrado | 200.8 |
| 3e7a2aac-fc7b-35f3-a1ba-2f4f4c1c36ce | -9.3881 | -49.1473 | 2026-10-01 14:10:00 | GOES-19 | DOIS IRMÃOS DO TOCANTINS | TOCANTINS | Brasil | 1707207 | 17 | 33 | nan | nan | nan | Cerrado | 96.0 |
| fdda6a03-3fe5-31c3-91c8-0e3a8b398762 | -10.207 | -49.9684 | 2026-10-01 14:10:00 | GOES-19 | PIUM | TOCANTINS | Brasil | 1717503 | 17 | 33 | nan | nan | nan | Cerrado | 57.0 |
| 7ddef4dc-2d37-3366-85b8-726e1a87fa17 | -9.88 | -44.9783 | 2026-10-01 14:10:00 | GOES-19 | RIACHO FRIO | PIAUÍ | Brasil | 2208858 | 22 | 33 | nan | nan | nan | Cerrado | 93.2 |
| 34960f55-640b-308a-983a-2c95474ab8e4 | -7.0738 | -42.8472 | 2026-10-01 14:10:00 | GOES-19 | NAZARÉ DO PIAUÍ | PIAUÍ | Brasil | 2206704 | 22 | 33 | nan | nan | nan | Caatinga | 90.4 |
| 37660bad-9604-35f1-86e6-2035d28af18c | -8.6457 | -45.3034 | 2026-10-01 14:10:00 | GOES-19 | BAIXA GRANDE DO RIBEIRO | PIAUÍ | Brasil | 2201150 | 22 | 33 | nan | nan | nan | Cerrado | 94.2 |
| c3e06805-259d-346e-8c87-4421f95c779a | -12.4535 | -44.1937 | 2026-10-01 14:10:00 | GOES-19 | TABOCAS DO BREJO VELHO | BAHIA | Brasil | 2930907 | 29 | 33 | nan | nan | nan | Cerrado | 359.9 |
| 548e89f4-3eae-3bb6-b82b-48fd3d8cd8d8 | -11.2278 | -45.1913 | 2026-10-01 14:10:00 | GOES-19 | FORMOSA DO RIO PRETO | BAHIA | Brasil | 2911105 | 29 | 33 | nan | nan | nan | Cerrado | 123.8 |
| 4a5ef828-6105-32b8-b5c8-9579eb0937a2 | -9.8067 | -44.8035 | 2026-10-01 14:10:00 | GOES-19 | RIACHO FRIO | PIAUÍ | Brasil | 2208858 | 22 | 33 | nan | nan | nan | Cerrado | 228.3 |
| 6d87db4c-f779-3ed4-9bcb-67c7857f6760 | -11.6977 | -43.5128 | 2026-10-01 14:10:00 | GOES-19 | BARRA | BAHIA | Brasil | 2902708 | 29 | 33 | nan | nan | nan | Cerrado | 128.3 |
| 0d9eb05a-9a58-3cd5-9a2f-f4b94b9e20ec | -14.377 | -44.7534 | 2026-10-01 14:10:00 | GOES-19 | COCOS | BAHIA | Brasil | 2908101 | 29 | 33 | nan | nan | nan | Cerrado | 179.0 |
| 278cc5cd-8a40-3d97-b477-6c6d186f2742 | -10.2827 | -49.9606 | 2026-10-01 14:10:00 | GOES-19 | PIUM | TOCANTINS | Brasil | 1717503 | 17 | 33 | nan | nan | nan | Cerrado | 69.4 |
| 1afd46ba-7411-3157-8971-854b4bd011c2 | -14.5458 | -40.8417 | 2026-10-01 14:10:00 | GOES-19 | ANAGÉ | BAHIA | Brasil | 2901205 | 29 | 33 | nan | nan | nan | Caatinga | 176.6 |
| 2ad03f32-2d69-387e-b933-8e90ebd6d1f0 | -12.4544 | -44.1466 | 2026-10-01 14:10:00 | GOES-19 | TABOCAS DO BREJO VELHO | BAHIA | Brasil | 2930907 | 29 | 33 | nan | nan | nan | Cerrado | 188.2 |
| 100e5e6c-d3cd-390e-8856-559feecefb95 | -11.1236 | -44.5823 | 2026-10-01 14:10:00 | GOES-19 | SANTA RITA DE CÁSSIA | BAHIA | Brasil | 2928406 | 29 | 33 | nan | nan | nan | Cerrado | 197.6 |
| 8e183f48-feb6-3dc6-9493-c50302ee619c | -9.8064 | -44.8265 | 2026-10-01 14:10:00 | GOES-19 | RIACHO FRIO | PIAUÍ | Brasil | 2208858 | 22 | 33 | nan | nan | nan | Cerrado | 672.2 |
| 7d25eb83-87d8-3df8-8e7f-4762f5115f31 | -16.9909 | -45.4594 | 2026-10-01 14:20:00 | GOES-19 | BURITIZEIRO | MINAS GERAIS | Brasil | 3109402 | 31 | 33 | nan | nan | nan | Cerrado | 115.2 |
| 46efa719-4f0d-39de-9971-09edd71bccc3 | -11.4123 | -43.3913 | 2026-10-01 14:20:00 | GOES-19 | BARRA | BAHIA | Brasil | 2902708 | 29 | 33 | nan | nan | nan | Cerrado | 201.7 |
| 7b85e010-ad38-3313-84ee-8407fc00f258 | -11.4127 | -43.3675 | 2026-10-01 14:20:00 | GOES-19 | BARRA | BAHIA | Brasil | 2902708 | 29 | 33 | nan | nan | nan | Cerrado | 174.8 |
| c122486d-0b74-31af-998d-289b8133033a | -12.6459 | -47.2823 | 2026-10-01 14:20:00 | GOES-19 | PARANÃ | TOCANTINS | Brasil | 1716208 | 17 | 33 | nan | nan | nan | Cerrado | 40.5 |
| aec4dc64-327e-3da6-a00a-e1793dfa1565 | -12.6259 | -47.33 | 2026-10-01 14:20:00 | GOES-19 | PARANÃ | TOCANTINS | Brasil | 1716208 | 17 | 33 | nan | nan | nan | Cerrado | 43.3 |
| 9f55ce76-d8cf-3677-90f4-dff9274aff1b | -9.7877 | -44.8058 | 2026-10-01 14:20:00 | GOES-19 | RIACHO FRIO | PIAUÍ | Brasil | 2208858 | 22 | 33 | nan | nan | nan | Cerrado | 111.8 |
| 77184883-de64-38b0-a21f-64d6cebb5f1d | -7.3779 | -42.628 | 2026-10-01 14:20:00 | GOES-19 | SÃO JOSÉ DO PEIXE | PIAUÍ | Brasil | 2210102 | 22 | 33 | nan | nan | nan | Caatinga | 94.1 |


[Clique aqui para ver as próximas entradas](README102.md)
