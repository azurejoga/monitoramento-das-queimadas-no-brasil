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

## Dados Diários - Página 87

| ID | Latitude | Longitude | Data/Hora GMT | Satélite | Município | Estado | País | Município ID | Estado ID | País ID | Dias sem Chuva | Precipitação | Risco de Fogo | Bioma | FRP |
|----|----------|-----------|---------------|----------|-----------|--------|------|--------------|-----------|---------|----------------|--------------|----------------|-------|-----|
| ada339b5-17d1-3d09-b85b-95971ce95b46 | -10.6128 | -44.3284 | 2025-09-06 07:50:00 | GOES-19 | SANTA RITA DE CÁSSIA | BAHIA | Brasil | 2928406 | 29 | 33 | nan | nan | nan | Cerrado | 155.5 |
| a31d314b-a9fe-35f7-a032-ae283529d36a | -10.5937 | -44.331 | 2025-09-06 08:00:00 | GOES-19 | SANTA RITA DE CÁSSIA | BAHIA | Brasil | 2928406 | 29 | 33 | nan | nan | nan | Cerrado | 72.3 |
| 88f3ee9b-9cd4-30df-8f52-de95c92e9c4d | -21.5233 | -50.0925 | 2025-09-06 08:00:00 | GOES-19 | PENÁPOLIS | SÃO PAULO | Brasil | 3537305 | 35 | 33 | nan | nan | nan | Mata Atlântica | 95.4 |
| 60fbc844-13db-39ca-b1d8-59fe9cb00bd4 | -9.0951 | -47.0093 | 2025-09-06 08:00:00 | GOES-19 | LIZARDA | TOCANTINS | Brasil | 1712405 | 17 | 33 | nan | nan | nan | Cerrado | 71.8 |
| 0a725d94-576f-3772-9617-8fd26ce87ba3 | -21.5027 | -50.097 | 2025-09-06 08:00:00 | GOES-19 | PENÁPOLIS | SÃO PAULO | Brasil | 3537305 | 35 | 33 | nan | nan | nan | Mata Atlântica | 101.3 |
| 07e1b370-c43d-36cc-ac06-a009a74ef750 | -10.6128 | -44.3284 | 2025-09-06 08:00:00 | GOES-19 | SANTA RITA DE CÁSSIA | BAHIA | Brasil | 2928406 | 29 | 33 | nan | nan | nan | Cerrado | 117.6 |
| 04bfde5f-0498-300a-9ec6-2fb678699127 | -21.502 | -50.1199 | 2025-09-06 08:00:00 | GOES-19 | PENÁPOLIS | SÃO PAULO | Brasil | 3537305 | 35 | 33 | nan | nan | nan | Mata Atlântica | 63.7 |
| 41230095-1dd9-3ab4-b496-ac8de6c51586 | -21.5227 | -50.1154 | 2025-09-06 08:00:00 | GOES-19 | PENÁPOLIS | SÃO PAULO | Brasil | 3537305 | 35 | 33 | nan | nan | nan | Mata Atlântica | 60.3 |
| 5b3296c6-dcf7-3426-95f4-156646e8bb3d | -10.5937 | -44.331 | 2025-09-06 08:10:00 | GOES-19 | SANTA RITA DE CÁSSIA | BAHIA | Brasil | 2928406 | 29 | 33 | nan | nan | nan | Cerrado | 81.9 |
| 37d127ae-ee8b-3104-9f22-66363256fe98 | -9.0951 | -47.0093 | 2025-09-06 08:10:00 | GOES-19 | LIZARDA | TOCANTINS | Brasil | 1712405 | 17 | 33 | nan | nan | nan | Cerrado | 72.1 |
| 5600d1de-8704-3fdf-826d-07b8cc6a4fde | -20.5415 | -46.4648 | 2025-09-06 08:10:00 | GOES-19 | SÃO JOÃO BATISTA DO GLÓRIA | MINAS GERAIS | Brasil | 3162203 | 31 | 33 | nan | nan | nan | Cerrado | 57.5 |
| 574bb04a-6894-3bab-a178-d582d861a275 | -10.6128 | -44.3284 | 2025-09-06 08:10:00 | GOES-19 | SANTA RITA DE CÁSSIA | BAHIA | Brasil | 2928406 | 29 | 33 | nan | nan | nan | Cerrado | 102.1 |
| a4694bd6-3cc0-3366-bb61-716f59bf0e5e | -21.5233 | -50.0925 | 2025-09-06 08:10:00 | GOES-19 | PENÁPOLIS | SÃO PAULO | Brasil | 3537305 | 35 | 33 | nan | nan | nan | Mata Atlântica | 70.2 |
| 51b1a3f4-180e-3434-8e44-cb09e295cf97 | -9.0951 | -47.0093 | 2025-09-06 08:20:00 | GOES-19 | LIZARDA | TOCANTINS | Brasil | 1712405 | 17 | 33 | nan | nan | nan | Cerrado | 65.3 |
| b0abeb25-7491-3d74-a266-4768f09b3331 | -10.5937 | -44.331 | 2025-09-06 08:20:00 | GOES-19 | SANTA RITA DE CÁSSIA | BAHIA | Brasil | 2928406 | 29 | 33 | nan | nan | nan | Cerrado | 54.6 |
| 945da710-5c19-3ae2-b742-9f4740ee00a5 | -10.6128 | -44.3284 | 2025-09-06 08:20:00 | GOES-19 | SANTA RITA DE CÁSSIA | BAHIA | Brasil | 2928406 | 29 | 33 | nan | nan | nan | Cerrado | 118.7 |
| c27f07a0-b530-30c8-82a2-13e994cb35d4 | -9.0948 | -47.0316 | 2025-09-06 08:30:00 | GOES-19 | LIZARDA | TOCANTINS | Brasil | 1712405 | 17 | 33 | nan | nan | nan | Cerrado | 81.9 |
| 863a58ed-ff90-37af-969f-c88bdc9f023f | -9.0951 | -47.0093 | 2025-09-06 08:30:00 | GOES-19 | LIZARDA | TOCANTINS | Brasil | 1712405 | 17 | 33 | nan | nan | nan | Cerrado | 68.8 |
| abf641f6-d5b3-3f1c-bb25-8ae0536ecfec | -15.9003 | -52.1473 | 2025-09-06 08:30:00 | GOES-19 | ARAGARÇAS | GOIÁS | Brasil | 5201702 | 52 | 33 | nan | nan | nan | Cerrado | 56.2 |
| b2d64f78-7dba-3514-947e-e7efb74d8d4d | -15.9199 | -52.1445 | 2025-09-06 08:30:00 | GOES-19 | ARAGARÇAS | GOIÁS | Brasil | 5201702 | 52 | 33 | nan | nan | nan | Cerrado | 67.4 |
| 58a0b788-6665-3204-8e61-2698026c749c | -10.6128 | -44.3284 | 2025-09-06 09:00:00 | GOES-19 | SANTA RITA DE CÁSSIA | BAHIA | Brasil | 2928406 | 29 | 33 | nan | nan | nan | Cerrado | 136.6 |
| 1fd26e55-b4a5-3c49-b451-6057ecd87014 | -10.6128 | -44.3284 | 2025-09-06 09:10:00 | GOES-19 | SANTA RITA DE CÁSSIA | BAHIA | Brasil | 2928406 | 29 | 33 | nan | nan | nan | Cerrado | 106.7 |
| 685420be-d2e8-31a0-b872-d53dfb05dfff | -9.0948 | -47.0316 | 2025-09-06 09:10:00 | GOES-19 | LIZARDA | TOCANTINS | Brasil | 1712405 | 17 | 33 | nan | nan | nan | Cerrado | 116.7 |
| 71b27c2d-18b5-38d5-9d60-11b34691c874 | -9.0948 | -47.0316 | 2025-09-06 09:20:00 | GOES-19 | LIZARDA | TOCANTINS | Brasil | 1712405 | 17 | 33 | nan | nan | nan | Cerrado | 131.1 |
| 0904b725-ba3d-3370-99fd-2d657e9f1fc2 | -10.6128 | -44.3284 | 2025-09-06 09:20:00 | GOES-19 | SANTA RITA DE CÁSSIA | BAHIA | Brasil | 2928406 | 29 | 33 | nan | nan | nan | Cerrado | 119.3 |
| a6aaa69c-639f-392c-938f-f80ddb7d9726 | -10.6128 | -44.3284 | 2025-09-06 09:30:00 | GOES-19 | SANTA RITA DE CÁSSIA | BAHIA | Brasil | 2928406 | 29 | 33 | nan | nan | nan | Cerrado | 113.9 |
| 92cc06db-7299-38d8-8db1-a81e48c27004 | -9.0948 | -47.0316 | 2025-09-06 09:40:00 | GOES-19 | LIZARDA | TOCANTINS | Brasil | 1712405 | 17 | 33 | nan | nan | nan | Cerrado | 96.6 |
| b3c7f93e-d004-3ed3-b87c-930f32a438b0 | -10.6128 | -44.3284 | 2025-09-06 09:40:00 | GOES-19 | SANTA RITA DE CÁSSIA | BAHIA | Brasil | 2928406 | 29 | 33 | nan | nan | nan | Cerrado | 107.2 |
| e00c570e-7b60-36ca-9b36-cbef88b165a4 | -10.6128 | -44.3284 | 2025-09-06 09:50:00 | GOES-19 | SANTA RITA DE CÁSSIA | BAHIA | Brasil | 2928406 | 29 | 33 | nan | nan | nan | Cerrado | 129.0 |
| ed358515-46a6-379e-9a67-1a461ae57ff5 | -10.6128 | -44.3284 | 2025-09-06 10:00:00 | GOES-19 | SANTA RITA DE CÁSSIA | BAHIA | Brasil | 2928406 | 29 | 33 | nan | nan | nan | Cerrado | 118.3 |
| ef56267d-aa36-357a-8123-432cfcd8d62d | -9.0948 | -47.0316 | 2025-09-06 10:00:00 | GOES-19 | LIZARDA | TOCANTINS | Brasil | 1712405 | 17 | 33 | nan | nan | nan | Cerrado | 89.1 |
| 0c73988f-ba32-3e59-a847-f3ba638b9b40 | -7.6881 | -50.2991 | 2025-09-06 10:10:00 | GOES-19 | PAU D'ARCO | PARÁ | Brasil | 1505551 | 15 | 33 | nan | nan | nan | Amazônia | 127.1 |
| f33ded6d-22c0-305c-a32f-3d91b4605b8c | -10.6128 | -44.3284 | 2025-09-06 10:10:00 | GOES-19 | SANTA RITA DE CÁSSIA | BAHIA | Brasil | 2928406 | 29 | 33 | nan | nan | nan | Cerrado | 155.4 |
| 64379552-cd91-300f-b062-f496a43822b1 | -7.6881 | -50.2991 | 2025-09-06 10:20:00 | GOES-19 | PAU D'ARCO | PARÁ | Brasil | 1505551 | 15 | 33 | nan | nan | nan | Amazônia | 135.3 |
| 484cf0a8-64a7-3770-af70-1c6052e0c0a6 | -9.0948 | -47.0316 | 2025-09-06 10:20:00 | GOES-19 | LIZARDA | TOCANTINS | Brasil | 1712405 | 17 | 33 | nan | nan | nan | Cerrado | 106.6 |
| 9bb26eee-fa29-31a2-9930-9d24b5d866ea | -10.6128 | -44.3284 | 2025-09-06 10:20:00 | GOES-19 | SANTA RITA DE CÁSSIA | BAHIA | Brasil | 2928406 | 29 | 33 | nan | nan | nan | Cerrado | 146.8 |
| 856c9262-9669-3b8d-b17a-7b7062ad5337 | -10.5937 | -44.331 | 2025-09-06 10:30:00 | GOES-19 | SANTA RITA DE CÁSSIA | BAHIA | Brasil | 2928406 | 29 | 33 | nan | nan | nan | Cerrado | 104.4 |
| 616fe362-1211-3236-ace7-bb91e665c6c2 | -10.6128 | -44.3284 | 2025-09-06 10:30:00 | GOES-19 | SANTA RITA DE CÁSSIA | BAHIA | Brasil | 2928406 | 29 | 33 | nan | nan | nan | Cerrado | 146.8 |
| cff33f67-57de-3557-9831-536559e8e790 | -7.6881 | -50.2991 | 2025-09-06 10:40:00 | GOES-19 | PAU D'ARCO | PARÁ | Brasil | 1505551 | 15 | 33 | nan | nan | nan | Amazônia | 85.6 |
| 2035d618-11f8-34f9-bbab-09f680b2201d | -10.6128 | -44.3284 | 2025-09-06 10:40:00 | GOES-19 | SANTA RITA DE CÁSSIA | BAHIA | Brasil | 2928406 | 29 | 33 | nan | nan | nan | Cerrado | 205.9 |
| a8ce3df3-7a82-3b56-8fe5-9587cec7ed93 | -8.4978 | -45.0684 | 2025-09-06 10:50:00 | GOES-19 | BAIXA GRANDE DO RIBEIRO | PIAUÍ | Brasil | 2201150 | 22 | 33 | nan | nan | nan | Cerrado | 97.3 |
| 02001710-f219-3cad-a89f-357e722b233b | -10.6128 | -44.3284 | 2025-09-06 10:50:00 | GOES-19 | SANTA RITA DE CÁSSIA | BAHIA | Brasil | 2928406 | 29 | 33 | nan | nan | nan | Cerrado | 148.6 |
| 30b0682a-d4ca-3390-affa-99d517af8c96 | -10.5937 | -44.331 | 2025-09-06 10:50:00 | GOES-19 | SANTA RITA DE CÁSSIA | BAHIA | Brasil | 2928406 | 29 | 33 | nan | nan | nan | Cerrado | 100.4 |
| 7411d32f-fec3-3029-9233-faf81adf7420 | -7.6881 | -50.2991 | 2025-09-06 10:50:00 | GOES-19 | PAU D'ARCO | PARÁ | Brasil | 1505551 | 15 | 33 | nan | nan | nan | Amazônia | 84.3 |
| 04617b85-06dc-387d-aa23-d612a8788192 | -8.9223 | -45.7953 | 2025-09-06 11:00:00 | GOES-19 | SANTA FILOMENA | PIAUÍ | Brasil | 2209203 | 22 | 33 | nan | nan | nan | Cerrado | 154.4 |
| 7401b35d-2e18-3467-bc24-8fc894bc0d9d | -8.9037 | -45.7747 | 2025-09-06 11:00:00 | GOES-19 | SANTA FILOMENA | PIAUÍ | Brasil | 2209203 | 22 | 33 | nan | nan | nan | Cerrado | 91.7 |
| 1c238284-5d0b-3451-b089-e8763f97bb97 | -7.6881 | -50.2991 | 2025-09-06 11:00:00 | GOES-19 | PAU D'ARCO | PARÁ | Brasil | 1505551 | 15 | 33 | nan | nan | nan | Amazônia | 117.6 |
| 5c75d5ad-92fb-3640-a704-54534a2999db | -10.6128 | -44.3284 | 2025-09-06 11:00:00 | GOES-19 | SANTA RITA DE CÁSSIA | BAHIA | Brasil | 2928406 | 29 | 33 | nan | nan | nan | Cerrado | 154.1 |
| d6a7fbfe-b831-39c1-ba29-1b3840b57f34 | -9.0951 | -47.0093 | 2025-09-06 11:00:00 | GOES-19 | LIZARDA | TOCANTINS | Brasil | 1712405 | 17 | 33 | nan | nan | nan | Cerrado | 95.1 |
| fb857370-26f3-36ea-9387-4e1de1e418da | -10.3137 | -46.4248 | 2025-09-06 11:00:00 | GOES-19 | MATEIROS | TOCANTINS | Brasil | 1712702 | 17 | 33 | nan | nan | nan | Cerrado | 98.1 |
| 28f9d0bf-ff76-37de-98b9-9c3ed8597fce | -10.5937 | -44.331 | 2025-09-06 11:00:00 | GOES-19 | SANTA RITA DE CÁSSIA | BAHIA | Brasil | 2928406 | 29 | 33 | nan | nan | nan | Cerrado | 87.5 |
| e5134ece-e79d-3ecc-8460-c744da0569fe | -10.3137 | -46.4248 | 2025-09-06 11:10:00 | GOES-19 | MATEIROS | TOCANTINS | Brasil | 1712702 | 17 | 33 | nan | nan | nan | Cerrado | 208.7 |
| 7f6a3018-cace-3b72-89d1-99588850a9b0 | -10.5937 | -44.331 | 2025-09-06 11:10:00 | GOES-19 | SANTA RITA DE CÁSSIA | BAHIA | Brasil | 2928406 | 29 | 33 | nan | nan | nan | Cerrado | 115.7 |
| b2aa006b-ada0-3e12-8336-b1f576adef17 | -7.6881 | -50.2991 | 2025-09-06 11:10:00 | GOES-19 | PAU D'ARCO | PARÁ | Brasil | 1505551 | 15 | 33 | nan | nan | nan | Amazônia | 91.3 |
| 980837c0-4842-31ad-bf7d-a1a673e813f1 | -10.6128 | -44.3284 | 2025-09-06 11:10:00 | GOES-19 | SANTA RITA DE CÁSSIA | BAHIA | Brasil | 2928406 | 29 | 33 | nan | nan | nan | Cerrado | 151.9 |
| 913c3a6d-8b0d-3d74-bf63-0749b558ba82 | -10.6128 | -44.3284 | 2025-09-06 11:20:00 | GOES-19 | SANTA RITA DE CÁSSIA | BAHIA | Brasil | 2928406 | 29 | 33 | nan | nan | nan | Cerrado | 183.2 |
| bc60801d-051d-38bc-951e-c07448d29214 | -10.5937 | -44.331 | 2025-09-06 11:20:00 | GOES-19 | SANTA RITA DE CÁSSIA | BAHIA | Brasil | 2928406 | 29 | 33 | nan | nan | nan | Cerrado | 126.2 |
| 8204f769-2c09-38e7-83f1-2c4077c5fb13 | -10.3137 | -46.4248 | 2025-09-06 11:20:00 | GOES-19 | MATEIROS | TOCANTINS | Brasil | 1712702 | 17 | 33 | nan | nan | nan | Cerrado | 152.2 |
| 95ca21c3-996c-3190-b689-7e0e64acefc7 | -7.6881 | -50.2991 | 2025-09-06 11:20:00 | GOES-19 | PAU D'ARCO | PARÁ | Brasil | 1505551 | 15 | 33 | nan | nan | nan | Amazônia | 77.4 |
| d31bd081-6d55-3fcf-bfa9-87d10da87887 | -10.314 | -46.4022 | 2025-09-06 11:20:00 | GOES-19 | MATEIROS | TOCANTINS | Brasil | 1712702 | 17 | 33 | nan | nan | nan | Cerrado | 83.7 |
| 2bb7e0f1-9541-3723-96da-469a190022b8 | -9.0951 | -47.0093 | 2025-09-06 11:30:00 | GOES-19 | LIZARDA | TOCANTINS | Brasil | 1712405 | 17 | 33 | nan | nan | nan | Cerrado | 81.8 |
| 679f006e-ca31-3708-8ac7-3e05bf176876 | -10.6128 | -44.3284 | 2025-09-06 11:30:00 | GOES-19 | SANTA RITA DE CÁSSIA | BAHIA | Brasil | 2928406 | 29 | 33 | nan | nan | nan | Cerrado | 185.0 |
| 72a6e8f5-224e-3c42-8e83-b5a0a0731d07 | -7.6881 | -50.2991 | 2025-09-06 11:30:00 | GOES-19 | PAU D'ARCO | PARÁ | Brasil | 1505551 | 15 | 33 | nan | nan | nan | Amazônia | 87.2 |
| dcd16c0d-58c7-36b9-8c63-11c13942b5ba | -10.5937 | -44.331 | 2025-09-06 11:30:00 | GOES-19 | SANTA RITA DE CÁSSIA | BAHIA | Brasil | 2928406 | 29 | 33 | nan | nan | nan | Cerrado | 116.7 |
| 71273c00-f522-380b-96f7-ea88b31a4392 | -10.3137 | -46.4248 | 2025-09-06 11:30:00 | GOES-19 | MATEIROS | TOCANTINS | Brasil | 1712702 | 17 | 33 | nan | nan | nan | Cerrado | 78.5 |
| e88cb624-f5db-34d0-ac35-55aba7f6e02d | -8.9223 | -45.7953 | 2025-09-06 11:40:00 | GOES-19 | SANTA FILOMENA | PIAUÍ | Brasil | 2209203 | 22 | 33 | nan | nan | nan | Cerrado | 71.5 |
| b113e269-bc86-33f6-9bed-e10a81553a77 | -10.6128 | -44.3284 | 2025-09-06 11:40:00 | GOES-19 | SANTA RITA DE CÁSSIA | BAHIA | Brasil | 2928406 | 29 | 33 | nan | nan | nan | Cerrado | 214.1 |
| 8e924985-b7ac-3d56-b408-e8eff73afb2c | -7.6881 | -50.2991 | 2025-09-06 11:40:00 | GOES-19 | PAU D'ARCO | PARÁ | Brasil | 1505551 | 15 | 33 | nan | nan | nan | Amazônia | 83.4 |
| 31ba0149-b8b6-33fe-9557-ad452f6b9a1b | -9.0951 | -47.0093 | 2025-09-06 11:40:00 | GOES-19 | LIZARDA | TOCANTINS | Brasil | 1712405 | 17 | 33 | nan | nan | nan | Cerrado | 117.9 |
| dc0b7dc9-8d15-363a-bc6e-be23230a742a | -10.3137 | -46.4248 | 2025-09-06 11:40:00 | GOES-19 | MATEIROS | TOCANTINS | Brasil | 1712702 | 17 | 33 | nan | nan | nan | Cerrado | 77.3 |
| 062ed2db-1e1a-3a44-ae7d-ef70ac5ebead | -10.5937 | -44.331 | 2025-09-06 11:40:00 | GOES-19 | SANTA RITA DE CÁSSIA | BAHIA | Brasil | 2928406 | 29 | 33 | nan | nan | nan | Cerrado | 122.2 |
| 974ccbfd-e4e6-3d4e-ad2c-2f16a1f09b8e | -9.0951 | -47.0093 | 2025-09-06 11:50:00 | GOES-19 | LIZARDA | TOCANTINS | Brasil | 1712405 | 17 | 33 | nan | nan | nan | Cerrado | 80.9 |
| e0d3381a-86f1-3453-aa53-bba9472fd8a8 | -10.5937 | -44.331 | 2025-09-06 11:50:00 | GOES-19 | SANTA RITA DE CÁSSIA | BAHIA | Brasil | 2928406 | 29 | 33 | nan | nan | nan | Cerrado | 129.9 |
| fccbf75a-f933-3489-b28f-34c404786e87 | -14.4364 | -48.4421 | 2025-09-06 11:50:00 | GOES-19 | NIQUELÂNDIA | GOIÁS | Brasil | 5214606 | 52 | 33 | nan | nan | nan | Cerrado | 239.0 |
| 121c37d7-33a3-39f7-a51c-db475ec599f1 | -7.6881 | -50.2991 | 2025-09-06 11:50:00 | GOES-19 | PAU D'ARCO | PARÁ | Brasil | 1505551 | 15 | 33 | nan | nan | nan | Amazônia | 95.2 |
| f3a6aafe-d054-3e4c-8f69-b491fb1ba105 | -9.6841 | -51.103 | 2025-09-06 11:50:00 | GOES-19 | SANTANA DO ARAGUAIA | PARÁ | Brasil | 1506708 | 15 | 33 | nan | nan | nan | Amazônia | 79.0 |
| db7ab5ef-08b6-3909-85c4-6f0a9da48a0a | -10.6128 | -44.3284 | 2025-09-06 11:50:00 | GOES-19 | SANTA RITA DE CÁSSIA | BAHIA | Brasil | 2928406 | 29 | 33 | nan | nan | nan | Cerrado | 201.7 |
| 9553805e-3b53-3604-8a48-3ba99fd7467f | -10.3137 | -46.4248 | 2025-09-06 11:50:00 | GOES-19 | MATEIROS | TOCANTINS | Brasil | 1712702 | 17 | 33 | nan | nan | nan | Cerrado | 87.0 |
| ce80a906-1450-31e3-aab6-0428b0391bf9 | -8.9223 | -45.7953 | 2025-09-06 11:50:00 | GOES-19 | SANTA FILOMENA | PIAUÍ | Brasil | 2209203 | 22 | 33 | nan | nan | nan | Cerrado | 128.2 |
| 89bb15c6-79d1-3fc7-9cc9-4120a5959a2d | -5.32353 | -42.78542 | 2025-09-06 11:55:00 | TERRA_M-M | TERESINA | PIAUÍ | Brasil | 2211001 | 22 | 33 | nan | nan | nan | Caatinga | 6.7 |
| e87cf697-8120-3fbc-a139-33a42d130bd7 | -5.73187 | -43.90734 | 2025-09-06 11:55:00 | TERRA_M-M | BURITI BRAVO | MARANHÃO | Brasil | 2102309 | 21 | 33 | nan | nan | nan | Cerrado | 12.5 |
| 5d11f144-3774-31e0-ab7c-bfe032ba62ea | -5.99313 | -44.15402 | 2025-09-06 11:55:00 | TERRA_M-M | COLINAS | MARANHÃO | Brasil | 2103505 | 21 | 33 | nan | nan | nan | Cerrado | 22.0 |
| 927055ca-1018-36ff-bce6-c0676bd959fc | -4.82267 | -42.7325 | 2025-09-06 11:55:00 | TERRA_M-M | JOSÉ DE FREITAS | PIAUÍ | Brasil | 2205508 | 22 | 33 | nan | nan | nan | Cerrado | 25.4 |
| d96f36b8-12bd-3bdc-843d-91a1a76734a7 | -6.4295 | -41.21238 | 2025-09-06 11:55:00 | TERRA_M-M | PIMENTEIRAS | PIAUÍ | Brasil | 2208106 | 22 | 33 | nan | nan | nan | Caatinga | 5.9 |
| f5a3958b-0f0f-3b98-a3fb-0246b9d333d3 | -5.67231 | -41.40765 | 2025-09-06 11:55:00 | TERRA_M-M | SÃO MIGUEL DO TAPUIO | PIAUÍ | Brasil | 2210409 | 22 | 33 | nan | nan | nan | Caatinga | 18.5 |
| 9f74a5eb-3025-349b-8fcb-37a5de440267 | -3.96624 | -43.23937 | 2025-09-06 11:55:00 | TERRA_M-M | CHAPADINHA | MARANHÃO | Brasil | 2103208 | 21 | 33 | nan | nan | nan | Cerrado | 12.5 |
| 4acd24b9-3123-3919-b5ab-d47a11a7a157 | -6.22928 | -42.64405 | 2025-09-06 11:55:00 | TERRA_M-M | REGENERAÇÃO | PIAUÍ | Brasil | 2208809 | 22 | 33 | nan | nan | nan | Caatinga | 8.8 |
| 55bbd62e-75e2-3932-bcaa-2c270326be09 | -5.98325 | -43.60964 | 2025-09-06 11:55:00 | TERRA_M-M | LAGOA DO MATO | MARANHÃO | Brasil | 2105922 | 21 | 33 | nan | nan | nan | Cerrado | 11.8 |
| f4cb24c7-68c3-3acc-a919-1c357f1b70bd | -5.44828 | -42.80564 | 2025-09-06 11:55:00 | TERRA_M-M | NAZÁRIA | PIAUÍ | Brasil | 2206720 | 22 | 33 | nan | nan | nan | Caatinga | 5.2 |
| 0faf908c-05df-3705-aa3e-1789ef2a8cb6 | -5.15826 | -42.84926 | 2025-09-06 11:55:00 | TERRA_M-M | TIMON | MARANHÃO | Brasil | 2112209 | 21 | 33 | nan | nan | nan | Cerrado | 12.3 |
| 1b7ea784-29fd-3e27-8b38-7f6ec4e0a121 | -6.22787 | -42.65358 | 2025-09-06 11:55:00 | TERRA_M-M | REGENERAÇÃO | PIAUÍ | Brasil | 2208809 | 22 | 33 | nan | nan | nan | Caatinga | 8.4 |
| 95e36c62-f837-32e5-84c5-db856d1a8d45 | -5.73725 | -43.10848 | 2025-09-06 11:55:00 | TERRA_M-M | PARNARAMA | MARANHÃO | Brasil | 2107803 | 21 | 33 | nan | nan | nan | Caatinga | 7.6 |
| 226c8a25-8746-352e-9db5-38e557e76172 | -4.79407 | -43.05438 | 2025-09-06 11:55:00 | TERRA_M-M | CAXIAS | MARANHÃO | Brasil | 2103000 | 21 | 33 | nan | nan | nan | Cerrado | 10.0 |
| ef02820d-e371-3993-b8df-2cff017cbac6 | -5.99139 | -44.16546 | 2025-09-06 11:55:00 | TERRA_M-M | COLINAS | MARANHÃO | Brasil | 2103505 | 21 | 33 | nan | nan | nan | Cerrado | 25.9 |
| 6219dce2-e4b4-3ee0-bfa1-1d4146bbce02 | -5.32496 | -42.77561 | 2025-09-06 11:55:00 | TERRA_M-M | TERESINA | PIAUÍ | Brasil | 2211001 | 22 | 33 | nan | nan | nan | Caatinga | 15.5 |
| 5f3785ec-d3e9-31f0-95ab-d32d1961dedf | -6.39533 | -38.90764 | 2025-09-06 11:55:00 | TERRA_M-M | ICÓ | CEARÁ | Brasil | 2305407 | 23 | 33 | nan | nan | nan | Caatinga | 18.5 |
| e5e5b3fe-6ef3-32aa-916c-2e7b20265dc4 | -5.98687 | -44.72932 | 2025-09-06 11:55:00 | TERRA_M-M | TUNTUM | MARANHÃO | Brasil | 2112308 | 21 | 33 | nan | nan | nan | Cerrado | 11.8 |
| b2355c66-5e8a-3b10-8b8c-4d4b16ab1a9d | -4.82122 | -42.74228 | 2025-09-06 11:55:00 | TERRA_M-M | JOSÉ DE FREITAS | PIAUÍ | Brasil | 2205508 | 22 | 33 | nan | nan | nan | Cerrado | 14.7 |
| 7475405e-ada4-3622-9c7b-34c5eefb112f | -6.22576 | -42.60489 | 2025-09-06 11:55:00 | TERRA_M-M | REGENERAÇÃO | PIAUÍ | Brasil | 2208809 | 22 | 33 | nan | nan | nan | Caatinga | 7.3 |
| 7a0946f9-5305-353a-bae1-6f438803b96e | -4.39068 | -41.90844 | 2025-09-06 11:55:00 | TERRA_M-M | PIRIPIRI | PIAUÍ | Brasil | 2208403 | 22 | 33 | nan | nan | nan | Caatinga | 6.9 |


[Clique aqui para ver as próximas entradas](README88.md)
