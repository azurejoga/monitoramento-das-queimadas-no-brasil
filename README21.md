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

## Dados Diários - Página 21

| ID | Latitude | Longitude | Data/Hora GMT | Satélite | Município | Estado | País | Município ID | Estado ID | País ID | Dias sem Chuva | Precipitação | Risco de Fogo | Bioma | FRP |
|----|----------|-----------|---------------|----------|-----------|--------|------|--------------|-----------|---------|----------------|--------------|----------------|-------|-----|
| e12d2a91-b377-364b-857b-f92a82b22dd2 | -14.17596 | -46.20813 | 2025-09-12 03:38:00 | NOAA-21 | POSSE | GOIÁS | Brasil | 5218300 | 52 | 33 | nan | nan | nan | Cerrado | 4.1 |
| 4a96488b-c6ae-3b2e-95d7-122d7d351747 | -14.18233 | -46.20621 | 2025-09-12 03:38:00 | NOAA-21 | POSSE | GOIÁS | Brasil | 5218300 | 52 | 33 | nan | nan | nan | Cerrado | 3.1 |
| e90a033d-c5ef-3ece-aa73-c5ccd5e71d4e | -14.44846 | -47.30711 | 2025-09-12 03:38:00 | NOAA-21 | SÃO JOÃO D'ALIANÇA | GOIÁS | Brasil | 5220009 | 52 | 33 | nan | nan | nan | Cerrado | 2.8 |
| 790732fd-e9e2-3bd9-a374-ede4e53e2126 | -11.6741 | -46.60115 | 2025-09-12 03:38:00 | NOAA-21 | NOVO JARDIM | TOCANTINS | Brasil | 1715259 | 17 | 33 | nan | nan | nan | Cerrado | 5.8 |
| 84829695-7404-36b8-ad76-11f7f202346d | -13.7805 | -46.28386 | 2025-09-12 03:38:00 | NOAA-21 | GUARANI DE GOIÁS | GOIÁS | Brasil | 5209408 | 52 | 33 | nan | nan | nan | Cerrado | 3.5 |
| f60a3606-9e0d-34b3-8367-77ee6acbed98 | -11.12224 | -45.12309 | 2025-09-12 03:38:00 | NOAA-21 | FORMOSA DO RIO PRETO | BAHIA | Brasil | 2911105 | 29 | 33 | nan | nan | nan | Cerrado | 3.7 |
| d0d5a9da-0ec2-3936-a1d9-af8c5c8a1b3b | -14.12947 | -45.37214 | 2025-09-12 03:38:00 | NOAA-21 | JABORANDI | BAHIA | Brasil | 2917359 | 29 | 33 | nan | nan | nan | Cerrado | 1.6 |
| c0390065-1afa-3bdb-817b-1b6c48d0d633 | -8.64329 | -45.71771 | 2025-09-12 03:38:00 | NOAA-21 | SANTA FILOMENA | PIAUÍ | Brasil | 2209203 | 22 | 33 | nan | nan | nan | Cerrado | 6.5 |
| 6cd29229-dd30-32b5-882b-bced28861e52 | -14.1303 | -45.37231 | 2025-09-12 03:38:00 | NOAA-21 | JABORANDI | BAHIA | Brasil | 2917359 | 29 | 33 | nan | nan | nan | Cerrado | 2.4 |
| 731819c5-b6eb-31c1-95f0-aa0ba9b08dd6 | -11.66517 | -46.64593 | 2025-09-12 03:38:00 | NOAA-21 | NOVO JARDIM | TOCANTINS | Brasil | 1715259 | 17 | 33 | nan | nan | nan | Cerrado | 3.8 |
| 9bf9fa31-e8b1-301d-8193-edfbcde7356b | -14.18081 | -46.20884 | 2025-09-12 03:38:00 | NOAA-21 | POSSE | GOIÁS | Brasil | 5218300 | 52 | 33 | nan | nan | nan | Cerrado | 4.5 |
| 9671f8e9-e0b3-3345-a015-fa154444cea7 | -9.06121 | -45.71754 | 2025-09-12 03:38:00 | NOAA-21 | SANTA FILOMENA | PIAUÍ | Brasil | 2209203 | 22 | 33 | nan | nan | nan | Cerrado | 6.1 |
| a9ee56b9-04ff-35bf-8bcd-a88d30124505 | -11.6503 | -46.68826 | 2025-09-12 03:38:00 | NOAA-21 | DIANÓPOLIS | TOCANTINS | Brasil | 1707009 | 17 | 33 | nan | nan | nan | Cerrado | 6.1 |
| bb4cf31f-d868-30bc-8194-6fd383d6382b | -11.45207 | -43.57933 | 2025-09-12 03:38:00 | NOAA-21 | BARRA | BAHIA | Brasil | 2902708 | 29 | 33 | nan | nan | nan | Cerrado | 3.3 |
| cec95939-4c85-35ef-8795-892c42ee925e | -11.15189 | -45.31552 | 2025-09-12 03:38:00 | NOAA-21 | FORMOSA DO RIO PRETO | BAHIA | Brasil | 2911105 | 29 | 33 | nan | nan | nan | Cerrado | 2.7 |
| 6675127d-9e80-30fc-ab1b-bb71f6e133dd | -15.11081 | -48.02102 | 2025-09-12 03:38:00 | NOAA-21 | ÁGUA FRIA DE GOIÁS | GOIÁS | Brasil | 5200175 | 52 | 33 | nan | nan | nan | Cerrado | 3.4 |
| 4147a75d-4d11-33ee-99ef-1e82c7597e61 | -8.96044 | -46.08084 | 2025-09-12 03:38:00 | NOAA-21 | ALTO PARNAÍBA | MARANHÃO | Brasil | 2100501 | 21 | 33 | nan | nan | nan | Cerrado | 2.9 |
| 7cda4caf-14ba-3b22-9d64-aa5473cde9cb | -13.35454 | -41.92509 | 2025-09-12 03:38:00 | NOAA-21 | ÉRICO CARDOSO | BAHIA | Brasil | 2900504 | 29 | 33 | nan | nan | nan | Caatinga | 9.4 |
| d51638e2-5a36-393c-80af-7c3fbeb4a81e | -10.3593 | -46.38649 | 2025-09-12 03:38:00 | NOAA-21 | MATEIROS | TOCANTINS | Brasil | 1712702 | 17 | 33 | nan | nan | nan | Cerrado | 1.5 |
| 5d8f20a5-f108-3dd0-9e6d-32cfac3ef615 | -11.3675 | -43.50905 | 2025-09-12 03:38:00 | NOAA-21 | BARRA | BAHIA | Brasil | 2902708 | 29 | 33 | nan | nan | nan | Cerrado | 1.6 |
| b44bc96f-70ab-36df-a1d3-b169c6502a12 | -14.1712 | -46.2023 | 2025-09-12 03:38:00 | NOAA-21 | POSSE | GOIÁS | Brasil | 5218300 | 52 | 33 | nan | nan | nan | Cerrado | 1.8 |
| 6750d5c9-6184-3a71-aaee-1106f72f1630 | -9.8479 | -43.54338 | 2025-09-12 03:38:00 | NOAA-21 | PILÃO ARCADO | BAHIA | Brasil | 2924405 | 29 | 33 | nan | nan | nan | Cerrado | 0.7 |
| 2e01e665-0b18-37fd-8f5a-fbebf8c273bb | -15.2403 | -44.05296 | 2025-09-12 03:38:00 | NOAA-21 | ITACARAMBI | MINAS GERAIS | Brasil | 3132107 | 31 | 33 | nan | nan | nan | Cerrado | 2.9 |
| e72e22c8-27d9-301a-802b-5b8c4551592b | -11.13618 | -45.24419 | 2025-09-12 03:38:00 | NOAA-21 | FORMOSA DO RIO PRETO | BAHIA | Brasil | 2911105 | 29 | 33 | nan | nan | nan | Cerrado | 3.0 |
| 914e4afc-30e4-30c7-975a-2123a419f012 | -10.74445 | -48.18585 | 2025-09-12 03:38:00 | NOAA-21 | MONTE DO CARMO | TOCANTINS | Brasil | 1713601 | 17 | 33 | nan | nan | nan | Cerrado | 8.6 |
| 7b5e3748-fdf3-3240-9765-0cae95dd81fc | -10.71079 | -48.62993 | 2025-09-12 03:38:00 | NOAA-21 | PORTO NACIONAL | TOCANTINS | Brasil | 1718204 | 17 | 33 | nan | nan | nan | Cerrado | 4.7 |
| 293a51a1-b6d1-3ff1-bb1c-81aeb0ce77d8 | -9.07463 | -46.95715 | 2025-09-12 03:38:00 | NOAA-21 | LIZARDA | TOCANTINS | Brasil | 1712405 | 17 | 33 | nan | nan | nan | Cerrado | 11.4 |
| 94c58b2c-8e61-34b6-bb8f-64e4caa00946 | -11.68056 | -46.5368 | 2025-09-12 03:38:00 | NOAA-21 | NOVO JARDIM | TOCANTINS | Brasil | 1715259 | 17 | 33 | nan | nan | nan | Cerrado | 5.2 |
| bb1b3a45-0cc0-360b-948a-e8e36aeccda2 | -14.43375 | -48.42992 | 2025-09-12 03:38:00 | NOAA-21 | NIQUELÂNDIA | GOIÁS | Brasil | 5214606 | 52 | 33 | nan | nan | nan | Cerrado | 3.0 |
| 8e8f649f-4a57-31be-85e0-346198aa5ed6 | -11.46661 | -43.61398 | 2025-09-12 03:38:00 | NOAA-21 | BARRA | BAHIA | Brasil | 2902708 | 29 | 33 | nan | nan | nan | Cerrado | 1.7 |
| 3f02ab8f-4c2b-3adc-87e1-37bc9a1651a9 | -14.44758 | -47.31136 | 2025-09-12 03:38:00 | NOAA-21 | SÃO JOÃO D'ALIANÇA | GOIÁS | Brasil | 5220009 | 52 | 33 | nan | nan | nan | Cerrado | 2.8 |
| 237a9fe9-198b-3d3b-9093-195bef6cd1ea | -8.9506 | -46.72581 | 2025-09-12 03:38:00 | NOAA-21 | BALSAS | MARANHÃO | Brasil | 2101400 | 21 | 33 | nan | nan | nan | Cerrado | 4.1 |
| 2f240dea-7a72-315d-ac64-fec87fe97eb8 | -9.04094 | -47.09823 | 2025-09-12 03:38:00 | NOAA-21 | LIZARDA | TOCANTINS | Brasil | 1712405 | 17 | 33 | nan | nan | nan | Cerrado | 8.3 |
| 05b255ee-b3c4-3802-b042-2abff302b4ff | -11.15108 | -45.31968 | 2025-09-12 03:38:00 | NOAA-21 | FORMOSA DO RIO PRETO | BAHIA | Brasil | 2911105 | 29 | 33 | nan | nan | nan | Cerrado | 4.4 |
| f7f822a4-e860-3ad6-b9fc-dc6f08d00ce9 | -10.88894 | -45.58747 | 2025-09-12 03:38:00 | NOAA-21 | FORMOSA DO RIO PRETO | BAHIA | Brasil | 2911105 | 29 | 33 | nan | nan | nan | Cerrado | 19.7 |
| 2ee84716-0322-3c22-9956-3b81e0623f52 | -14.28039 | -45.06931 | 2025-09-12 03:38:00 | NOAA-21 | COCOS | BAHIA | Brasil | 2908101 | 29 | 33 | nan | nan | nan | Cerrado | 4.4 |
| 28952280-d3d5-37db-a1cd-9bf5ca44b56e | -15.68203 | -47.05207 | 2025-09-12 03:38:00 | NOAA-21 | CABECEIRAS | GOIÁS | Brasil | 5204003 | 52 | 33 | nan | nan | nan | Cerrado | 2.3 |
| 402702c4-67e6-3eb6-9af7-53a233e7c79e | -11.44095 | -43.56649 | 2025-09-12 03:38:00 | NOAA-21 | BARRA | BAHIA | Brasil | 2902708 | 29 | 33 | nan | nan | nan | Cerrado | 3.6 |
| dbea76f9-9f53-300a-a6d1-605d7a8491ba | -13.91466 | -48.26942 | 2025-09-12 03:38:00 | NOAA-21 | COLINAS DO SUL | GOIÁS | Brasil | 5205521 | 52 | 33 | nan | nan | nan | Cerrado | 14.2 |
| b84f825e-11f0-34ad-aef0-59ad2c933be7 | -14.28448 | -45.04839 | 2025-09-12 03:38:00 | NOAA-21 | COCOS | BAHIA | Brasil | 2908101 | 29 | 33 | nan | nan | nan | Cerrado | 1.8 |
| 016d1d99-e382-3020-a793-4d96d1aa890a | -8.49437 | -47.27654 | 2025-09-12 03:38:00 | NOAA-21 | ITACAJÁ | TOCANTINS | Brasil | 1710508 | 17 | 33 | nan | nan | nan | Cerrado | 3.2 |
| 1a0db6e5-43e2-3346-9af0-0e43d900b336 | -15.56118 | -41.79213 | 2025-09-12 03:38:00 | NOAA-21 | SÃO JOÃO DO PARAÍSO | MINAS GERAIS | Brasil | 3162708 | 31 | 33 | nan | nan | nan | Mata Atlântica | 4.6 |
| d19cac97-ae08-3ab8-aedb-737457a4603e | -15.07882 | -48.00309 | 2025-09-12 03:38:00 | NOAA-21 | ÁGUA FRIA DE GOIÁS | GOIÁS | Brasil | 5200175 | 52 | 33 | nan | nan | nan | Cerrado | 3.4 |
| e1f8534c-9e02-3450-a7ef-7fb2bbd4c668 | -11.41633 | -43.71108 | 2025-09-12 03:38:00 | NOAA-21 | BARRA | BAHIA | Brasil | 2902708 | 29 | 33 | nan | nan | nan | Cerrado | 1.6 |
| c14ce0cd-04d5-3864-89b8-48eb6337f366 | -11.69934 | -46.50628 | 2025-09-12 03:38:00 | NOAA-21 | NOVO JARDIM | TOCANTINS | Brasil | 1715259 | 17 | 33 | nan | nan | nan | Cerrado | 3.9 |
| 758e2476-9cc2-34af-9fd9-d5315529635e | -11.15432 | -45.30301 | 2025-09-12 03:38:00 | NOAA-21 | FORMOSA DO RIO PRETO | BAHIA | Brasil | 2911105 | 29 | 33 | nan | nan | nan | Cerrado | 4.3 |
| f0e71e0e-d1d1-3f33-826d-366370f561bd | -14.3758 | -47.28945 | 2025-09-12 03:38:00 | NOAA-21 | SÃO JOÃO D'ALIANÇA | GOIÁS | Brasil | 5220009 | 52 | 33 | nan | nan | nan | Cerrado | 1.7 |
| 3dd3421e-a750-3443-a8e0-2d62fd6af9b3 | -9.0463 | -47.05891 | 2025-09-12 03:38:00 | NOAA-21 | LIZARDA | TOCANTINS | Brasil | 1712405 | 17 | 33 | nan | nan | nan | Cerrado | 12.5 |
| 2c37c99e-7d0f-366c-bfa4-c4a76c0eb797 | -11.67206 | -46.61134 | 2025-09-12 03:38:00 | NOAA-21 | NOVO JARDIM | TOCANTINS | Brasil | 1715259 | 17 | 33 | nan | nan | nan | Cerrado | 8.3 |
| 2b522da5-aaaa-371b-9ded-bca4115760ba | -13.9031 | -48.2599 | 2025-09-12 03:38:00 | NOAA-21 | COLINAS DO SUL | GOIÁS | Brasil | 5205521 | 52 | 33 | nan | nan | nan | Cerrado | 17.6 |
| 9bd5c3be-21f7-3803-9e6b-0eb9fb791db6 | -11.4245 | -43.54153 | 2025-09-12 03:38:00 | NOAA-21 | BARRA | BAHIA | Brasil | 2902708 | 29 | 33 | nan | nan | nan | Cerrado | 3.7 |
| c28e9c08-66a8-34d6-8e79-25531b449283 | -11.42337 | -43.54766 | 2025-09-12 03:38:00 | NOAA-21 | BARRA | BAHIA | Brasil | 2902708 | 29 | 33 | nan | nan | nan | Cerrado | 2.3 |
| f7907d6d-eb8e-3937-802e-421b3244a692 | -11.6581 | -46.64928 | 2025-09-12 03:38:00 | NOAA-21 | DIANÓPOLIS | TOCANTINS | Brasil | 1707009 | 17 | 33 | nan | nan | nan | Cerrado | 4.5 |
| 6dc14767-3031-38e2-9153-9b7b0d15be85 | -14.15148 | -44.45021 | 2025-09-12 03:38:00 | NOAA-21 | COCOS | BAHIA | Brasil | 2908101 | 29 | 33 | nan | nan | nan | Cerrado | 1.7 |
| b6898d14-d15a-3d9a-9921-37a2a551056f | -15.48587 | -47.34727 | 2025-09-12 03:38:00 | NOAA-21 | FORMOSA | GOIÁS | Brasil | 5208004 | 52 | 33 | nan | nan | nan | Cerrado | 1.6 |
| 1c284913-b77d-378b-9cbd-797fa1211519 | -14.28107 | -45.06582 | 2025-09-12 03:38:00 | NOAA-21 | COCOS | BAHIA | Brasil | 2908101 | 29 | 33 | nan | nan | nan | Cerrado | 3.1 |
| 54366b88-02ee-317f-aa53-589c392e34e7 | -15.10889 | -48.0161 | 2025-09-12 03:38:00 | NOAA-21 | ÁGUA FRIA DE GOIÁS | GOIÁS | Brasil | 5200175 | 52 | 33 | nan | nan | nan | Cerrado | 5.1 |
| ad764f07-19f5-3b54-a28b-2e0b5eccab32 | -14.1848 | -46.19425 | 2025-09-12 03:38:00 | NOAA-21 | POSSE | GOIÁS | Brasil | 5218300 | 52 | 33 | nan | nan | nan | Cerrado | 1.6 |
| f3b232e8-f6ba-3edc-9d28-2609dda6325a | -10.13336 | -47.91708 | 2025-09-12 03:38:00 | NOAA-21 | APARECIDA DO RIO NEGRO | TOCANTINS | Brasil | 1701101 | 17 | 33 | nan | nan | nan | Cerrado | 8.2 |
| d2627043-8a4c-3b78-bec2-49afd2a55b69 | -9.03545 | -47.09114 | 2025-09-12 03:38:00 | NOAA-21 | LIZARDA | TOCANTINS | Brasil | 1712405 | 17 | 33 | nan | nan | nan | Cerrado | 8.7 |
| b362d84a-a7a3-37b9-b53e-f5e0a2f76dad | -11.41469 | -43.70956 | 2025-09-12 03:38:00 | NOAA-21 | BARRA | BAHIA | Brasil | 2902708 | 29 | 33 | nan | nan | nan | Cerrado | 1.3 |
| df448c95-48b5-370d-9f60-e753f8c11f1e | -9.88756 | -46.46543 | 2025-09-12 03:38:00 | NOAA-21 | ALTO PARNAÍBA | MARANHÃO | Brasil | 2100501 | 21 | 33 | nan | nan | nan | Cerrado | 2.2 |
| 95eef56a-f051-3963-bf2a-64f08ec18162 | -9.0377 | -47.07935 | 2025-09-12 03:38:00 | NOAA-21 | LIZARDA | TOCANTINS | Brasil | 1712405 | 17 | 33 | nan | nan | nan | Cerrado | 7.6 |
| 6b360c6b-8218-3136-9ca3-3f571a9bbd2a | -14.41517 | -47.31407 | 2025-09-12 03:38:00 | NOAA-21 | SÃO JOÃO D'ALIANÇA | GOIÁS | Brasil | 5220009 | 52 | 33 | nan | nan | nan | Cerrado | 3.3 |
| 9f666c9b-e588-3f88-a271-1995f0103a48 | -13.31946 | -44.64902 | 2025-09-12 03:38:00 | NOAA-21 | CORRENTINA | BAHIA | Brasil | 2909307 | 29 | 33 | nan | nan | nan | Cerrado | 1.7 |
| 395f891b-4532-30df-85b3-a37c67737205 | -9.01231 | -45.74259 | 2025-09-12 03:38:00 | NOAA-21 | SANTA FILOMENA | PIAUÍ | Brasil | 2209203 | 22 | 33 | nan | nan | nan | Cerrado | 8.3 |
| 669ad18a-37e4-30fb-bfb7-74572a53dbfd | -13.15135 | -47.14756 | 2025-09-12 03:38:00 | NOAA-21 | ARRAIAS | TOCANTINS | Brasil | 1702406 | 17 | 33 | nan | nan | nan | Cerrado | 2.5 |
| 87e43cda-7b91-3cc4-8f25-201179500609 | -9.72229 | -43.51962 | 2025-09-12 03:38:00 | NOAA-21 | PILÃO ARCADO | BAHIA | Brasil | 2924405 | 29 | 33 | nan | nan | nan | Cerrado | 1.7 |
| 1e72879d-b017-3542-83c2-b7f76361f47e | -9.04536 | -47.11101 | 2025-09-12 03:38:00 | NOAA-21 | LIZARDA | TOCANTINS | Brasil | 1712405 | 17 | 33 | nan | nan | nan | Cerrado | 3.2 |
| 2633299c-ead4-3ac4-bf40-45abbe3c9470 | -11.43911 | -43.56436 | 2025-09-12 03:38:00 | NOAA-21 | BARRA | BAHIA | Brasil | 2902708 | 29 | 33 | nan | nan | nan | Cerrado | 2.1 |
| 5cfd902c-68d8-310c-9380-83143e75e2a4 | -15.07755 | -48.00908 | 2025-09-12 03:38:00 | NOAA-21 | ÁGUA FRIA DE GOIÁS | GOIÁS | Brasil | 5200175 | 52 | 33 | nan | nan | nan | Cerrado | 3.4 |
| eb4f4d0c-9297-3345-9790-da93702a9478 | -10.88823 | -45.59112 | 2025-09-12 03:38:00 | NOAA-21 | FORMOSA DO RIO PRETO | BAHIA | Brasil | 2911105 | 29 | 33 | nan | nan | nan | Cerrado | 19.7 |
| af270dbc-fa05-30d3-93ca-69c21111e65c | -11.85878 | -46.75677 | 2025-09-12 03:38:00 | NOAA-21 | NOVO JARDIM | TOCANTINS | Brasil | 1715259 | 17 | 33 | nan | nan | nan | Cerrado | 6.0 |
| 417eb2cf-e05c-3bd6-95b7-d17478b1fcac | -9.04686 | -47.06722 | 2025-09-12 03:38:00 | NOAA-21 | LIZARDA | TOCANTINS | Brasil | 1712405 | 17 | 33 | nan | nan | nan | Cerrado | 6.7 |
| 98701c88-2a49-3e4e-9363-edc9e01160ff | -9.01838 | -45.74389 | 2025-09-12 03:38:00 | NOAA-21 | SANTA FILOMENA | PIAUÍ | Brasil | 2209203 | 22 | 33 | nan | nan | nan | Cerrado | 8.3 |
| 1f96da5a-a4b7-3a68-8315-7eaf4dccd9f7 | -13.30977 | -42.38277 | 2025-09-12 03:38:00 | NOAA-21 | CATURAMA | BAHIA | Brasil | 2907558 | 29 | 33 | nan | nan | nan | Caatinga | 2.6 |
| 7555adf5-6f3f-33c3-95db-67e3a05a2421 | -14.04609 | -40.63671 | 2025-09-12 03:38:00 | NOAA-21 | MANOEL VITORINO | BAHIA | Brasil | 2920403 | 29 | 33 | nan | nan | nan | Caatinga | 1.1 |
| 90d56522-3a75-3466-8098-ba1f16eea72a | -11.69601 | -46.55502 | 2025-09-12 03:38:00 | NOAA-21 | NOVO JARDIM | TOCANTINS | Brasil | 1715259 | 17 | 33 | nan | nan | nan | Cerrado | 9.5 |
| 7da276b6-74af-31cb-a39e-ac74be7b5606 | -9.0387 | -47.10996 | 2025-09-12 03:38:00 | NOAA-21 | LIZARDA | TOCANTINS | Brasil | 1712405 | 17 | 33 | nan | nan | nan | Cerrado | 2.8 |
| 2a164d7d-dbef-3b89-9f73-5d1e7672f326 | -10.70571 | -48.61919 | 2025-09-12 03:38:00 | NOAA-21 | PORTO NACIONAL | TOCANTINS | Brasil | 1718204 | 17 | 33 | nan | nan | nan | Cerrado | 20.0 |
| c03c229a-feae-308d-a9f7-b662a6265e90 | -14.18727 | -46.2064 | 2025-09-12 03:38:00 | NOAA-21 | POSSE | GOIÁS | Brasil | 5218300 | 52 | 33 | nan | nan | nan | Cerrado | 3.5 |
| 9d965d26-c93d-342a-801c-164b93dcd5f5 | -10.85821 | -48.15927 | 2025-09-12 03:38:00 | NOAA-21 | MONTE DO CARMO | TOCANTINS | Brasil | 1713601 | 17 | 33 | nan | nan | nan | Cerrado | 2.4 |
| 19172f1e-333d-3652-b71a-654541df2636 | -14.17519 | -46.21185 | 2025-09-12 03:38:00 | NOAA-21 | POSSE | GOIÁS | Brasil | 5218300 | 52 | 33 | nan | nan | nan | Cerrado | 4.1 |
| e0ef8104-664a-3ae5-b2ed-fb6e4de775b2 | -9.04206 | -47.0924 | 2025-09-12 03:38:00 | NOAA-21 | LIZARDA | TOCANTINS | Brasil | 1712405 | 17 | 33 | nan | nan | nan | Cerrado | 8.7 |
| 80db16aa-a04c-3e63-a1af-1647468b01e8 | -11.13698 | -45.24011 | 2025-09-12 03:38:00 | NOAA-21 | FORMOSA DO RIO PRETO | BAHIA | Brasil | 2911105 | 29 | 33 | nan | nan | nan | Cerrado | 3.0 |
| ec86d0ce-db66-3296-84a9-36caa6c849f5 | -14.17584 | -46.17411 | 2025-09-12 03:38:00 | NOAA-21 | POSSE | GOIÁS | Brasil | 5218300 | 52 | 33 | nan | nan | nan | Cerrado | 5.8 |
| 82342c2d-1a42-38c5-aedc-33a5387415c7 | -14.28627 | -45.08477 | 2025-09-12 03:38:00 | NOAA-21 | COCOS | BAHIA | Brasil | 2908101 | 29 | 33 | nan | nan | nan | Cerrado | 0.9 |
| c3266cc4-6737-3fe0-bfd0-2c1d38737249 | -21.2068 | -47.5059 | 2025-09-12 03:40:00 | GOES-19 | SERRA AZUL | SÃO PAULO | Brasil | 3551405 | 35 | 33 | nan | nan | nan | Cerrado | 111.3 |
| 2b591a30-7a3c-38d9-83d5-b019f5c64d1f | -21.1854 | -47.5346 | 2025-09-12 03:40:00 | GOES-19 | SERRANA | SÃO PAULO | Brasil | 3551504 | 35 | 33 | nan | nan | nan | Cerrado | 112.0 |
| dd4da046-2d73-3386-9722-502c40012d54 | -11.6817 | -46.5858 | 2025-09-12 03:40:00 | GOES-19 | NOVO JARDIM | TOCANTINS | Brasil | 1715259 | 17 | 33 | nan | nan | nan | Cerrado | 54.3 |
| 636d2e25-6528-3d79-80e9-640cb7dc6c1e | -21.1861 | -47.5109 | 2025-09-12 03:40:00 | GOES-19 | ALTINÓPOLIS | SÃO PAULO | Brasil | 3501004 | 35 | 33 | nan | nan | nan | Cerrado | 89.4 |
| 55718f79-4060-3359-aa76-413786f74c79 | -11.5235 | -50.5968 | 2025-09-12 03:40:00 | GOES-19 | LAGOA DA CONFUSÃO | TOCANTINS | Brasil | 1711902 | 17 | 33 | nan | nan | nan | Cerrado | 95.3 |
| 6eb92937-e894-3aa5-bda3-ab6fa1539643 | -12.9292 | -54.7538 | 2025-09-12 03:40:00 | GOES-19 | NOVA UBIRATÃ | MATO GROSSO | Brasil | 5106240 | 51 | 33 | nan | nan | nan | Amazônia | 393.9 |
| f107c5b7-67a5-3342-83f8-612f5f7a9a11 | -9.3017 | -65.5959 | 2025-09-12 03:40:00 | GOES-19 | LÁBREA | AMAZONAS | Brasil | 1302405 | 13 | 33 | nan | nan | nan | Amazônia | 50.9 |
| 0d327f93-a2ba-3026-a237-63cbb9b80d32 | -11.5232 | -50.6182 | 2025-09-12 03:40:00 | GOES-19 | LAGOA DA CONFUSÃO | TOCANTINS | Brasil | 1711902 | 17 | 33 | nan | nan | nan | Cerrado | 62.6 |
| c3b04da9-4790-3f15-a1aa-55e74d8196ec | -12.9289 | -54.7744 | 2025-09-12 03:40:00 | GOES-19 | NOVA UBIRATÃ | MATO GROSSO | Brasil | 5106240 | 51 | 33 | nan | nan | nan | Amazônia | 113.5 |
| 679abca1-59f9-349f-953d-2a4772a0c0a7 | -11.5263 | -50.404 | 2025-09-12 03:40:00 | GOES-19 | LAGOA DA CONFUSÃO | TOCANTINS | Brasil | 1711902 | 17 | 33 | nan | nan | nan | Cerrado | 101.0 |
| d0f087e8-e751-3b05-b170-10a85e5655c0 | -12.9098 | -54.7763 | 2025-09-12 03:40:00 | GOES-19 | NOVA UBIRATÃ | MATO GROSSO | Brasil | 5106240 | 51 | 33 | nan | nan | nan | Amazônia | 60.1 |
| f312a732-6d16-34d7-b85c-097415c6c612 | -21.947 | -47.5578 | 2025-09-12 03:40:00 | GOES-19 | DESCALVADO | SÃO PAULO | Brasil | 3513702 | 35 | 33 | nan | nan | nan | Cerrado | 101.3 |
| 7c015871-1bab-3983-9aba-576a2d37d54c | -12.9103 | -54.7352 | 2025-09-12 03:40:00 | GOES-19 | NOVA UBIRATÃ | MATO GROSSO | Brasil | 5106240 | 51 | 33 | nan | nan | nan | Amazônia | 62.8 |


[Clique aqui para ver as próximas entradas](README22.md)
