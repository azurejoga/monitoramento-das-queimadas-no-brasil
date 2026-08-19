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

## Dados Diários - Página 40

| ID | Latitude | Longitude | Data/Hora GMT | Satélite | Município | Estado | País | Município ID | Estado ID | País ID | Dias sem Chuva | Precipitação | Risco de Fogo | Bioma | FRP |
|----|----------|-----------|---------------|----------|-----------|--------|------|--------------|-----------|---------|----------------|--------------|----------------|-------|-----|
| 90efd430-52f1-371c-9bdb-4f427df09729 | -8.50287 | -54.86122 | 2026-08-19 04:40:00 | NOAA-20 | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 3.4 |
| c5256d05-9fd9-3143-b599-b78d63d43468 | -9.07344 | -50.81642 | 2026-08-19 04:40:00 | NOAA-20 | SANTANA DO ARAGUAIA | PARÁ | Brasil | 1506708 | 15 | 33 | nan | nan | nan | Amazônia | 2.4 |
| 1685b72a-d140-3240-9b58-a52d963a7807 | -11.4879 | -45.10821 | 2026-08-19 04:40:00 | NOAA-20 | RIACHÃO DAS NEVES | BAHIA | Brasil | 2926202 | 29 | 33 | nan | nan | nan | Cerrado | 2.8 |
| 8938b152-1b77-3621-8f9a-30e90ff001ca | -11.08455 | -47.6036 | 2026-08-19 04:40:00 | NOAA-20 | PINDORAMA DO TOCANTINS | TOCANTINS | Brasil | 1717008 | 17 | 33 | nan | nan | nan | Cerrado | 0.8 |
| 96cff7eb-f380-3360-8f80-89d451566479 | -12.24901 | -43.15998 | 2026-08-19 04:40:00 | NOAA-20 | IBOTIRAMA | BAHIA | Brasil | 2913200 | 29 | 33 | nan | nan | nan | Caatinga | 0.8 |
| a7172bd4-200c-323f-be5f-7664ea9a3609 | -11.33589 | -51.11835 | 2026-08-19 04:40:00 | NOAA-20 | SÃO FÉLIX DO ARAGUAIA | MATO GROSSO | Brasil | 5107859 | 51 | 33 | nan | nan | nan | Cerrado | 0.9 |
| cea3f149-dc61-3856-ac52-f9451a150737 | -8.54543 | -54.74962 | 2026-08-19 04:40:00 | NOAA-20 | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 1.7 |
| cb27e528-c4bf-3157-b414-793f96296a75 | -9.73494 | -46.83792 | 2026-08-19 04:40:00 | NOAA-20 | LIZARDA | TOCANTINS | Brasil | 1712405 | 17 | 33 | nan | nan | nan | Cerrado | 3.1 |
| 259b2369-0567-3b27-811e-6feb9acad1b8 | -8.58445 | -54.75657 | 2026-08-19 04:40:00 | NOAA-20 | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 5.7 |
| 1f423b91-2cb9-3848-9338-5b6bb230acaa | -9.39322 | -48.24458 | 2026-08-19 04:40:00 | NOAA-20 | TOCANTÍNIA | TOCANTINS | Brasil | 1721109 | 17 | 33 | nan | nan | nan | Cerrado | 2.5 |
| a94f06c5-51fd-3dbd-9233-c1ae265e80c6 | -8.57653 | -54.75076 | 2026-08-19 04:40:00 | NOAA-20 | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 3.4 |
| 6ee7ca72-4af9-3361-9fb2-a102bc3ed4ca | -8.58519 | -54.75235 | 2026-08-19 04:40:00 | NOAA-20 | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 5.7 |
| a531a94a-7f0d-32ea-b5f0-73f096dca914 | -11.09094 | -49.91618 | 2026-08-19 04:40:00 | NOAA-20 | LAGOA DA CONFUSÃO | TOCANTINS | Brasil | 1711902 | 17 | 33 | nan | nan | nan | Cerrado | 0.9 |
| 6997d8ea-678f-32f6-9a06-97f7c550d6dd | -8.56999 | -54.76257 | 2026-08-19 04:40:00 | NOAA-20 | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 4.7 |
| 8e16fd09-10f8-35bf-b550-c1dd49331d4a | -13.27785 | -51.64381 | 2026-08-19 04:40:00 | NOAA-20 | RIBEIRÃO CASCALHEIRA | MATO GROSSO | Brasil | 5107180 | 51 | 33 | nan | nan | nan | Cerrado | 7.5 |
| 7856698b-6884-3507-91f4-9f23e500c678 | -8.56718 | -54.72766 | 2026-08-19 04:40:00 | NOAA-20 | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 4.1 |
| fce24acd-16c3-3602-a859-3e252e217afc | -11.72019 | -45.58369 | 2026-08-19 04:40:00 | NOAA-20 | RIACHÃO DAS NEVES | BAHIA | Brasil | 2926202 | 29 | 33 | nan | nan | nan | Cerrado | 1.0 |
| 3bcb22ce-066e-323c-9518-1bd8f6ec8c21 | -11.21776 | -54.01005 | 2026-08-19 04:40:00 | NOAA-20 | MARCELÂNDIA | MATO GROSSO | Brasil | 5105580 | 51 | 33 | nan | nan | nan | Amazônia | 2.5 |
| e5492e18-fe3b-3d5c-bc5c-9585703f22ed | -9.76115 | -46.75746 | 2026-08-19 04:40:00 | NOAA-20 | LIZARDA | TOCANTINS | Brasil | 1712405 | 17 | 33 | nan | nan | nan | Cerrado | 1.8 |
| 4ad1c277-7c10-30a7-886d-d1b283a6d6a2 | -14.45753 | -45.63279 | 2026-08-19 04:40:00 | NOAA-20 | JABORANDI | BAHIA | Brasil | 2917359 | 29 | 33 | nan | nan | nan | Cerrado | 5.3 |
| 1cfe3bc1-ce47-318c-b44f-98c9ee93dcb0 | -8.534 | -54.75784 | 2026-08-19 04:40:00 | NOAA-20 | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 3.3 |
| 9af7dc16-45d1-3d35-b4cb-0bca90206754 | -11.71562 | -54.62627 | 2026-08-19 04:40:00 | NOAA-20 | SANTA CARMEM | MATO GROSSO | Brasil | 5107248 | 51 | 33 | nan | nan | nan | Amazônia | 1.2 |
| 6f14e48e-80bd-3d20-b7e0-729b0790251d | -12.83485 | -48.4231 | 2026-08-19 04:40:00 | NOAA-20 | SÃO SALVADOR DO TOCANTINS | TOCANTINS | Brasil | 1720259 | 17 | 33 | nan | nan | nan | Cerrado | 1.5 |
| 748d602d-c2f0-3fb4-8d8e-853075989655 | -8.54764 | -54.73717 | 2026-08-19 04:40:00 | NOAA-20 | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 2.0 |
| 3aa924b2-ed4d-3dd5-a803-4234c1043c76 | -8.53823 | -54.73983 | 2026-08-19 04:40:00 | NOAA-20 | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 2.8 |
| d86869cf-0f16-326a-a310-ed5bf94a3f6b | -11.7197 | -54.62698 | 2026-08-19 04:40:00 | NOAA-20 | SANTA CARMEM | MATO GROSSO | Brasil | 5107248 | 51 | 33 | nan | nan | nan | Amazônia | 1.0 |
| e76c5552-7588-3a48-81fa-7b5d0a5712fb | -8.52584 | -54.75915 | 2026-08-19 04:40:00 | NOAA-20 | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 1.2 |
| b8d4d58e-0f10-3988-ac4f-a129b5951be3 | -9.16237 | -59.67335 | 2026-08-19 04:40:00 | NOAA-20 | COLNIZA | MATO GROSSO | Brasil | 5103254 | 51 | 33 | nan | nan | nan | Amazônia | 1.3 |
| ac0a3f4f-efb7-3547-8a8a-537e8f74882a | -11.19437 | -54.81031 | 2026-08-19 04:40:00 | NOAA-20 | NOVA SANTA HELENA | MATO GROSSO | Brasil | 5106190 | 51 | 33 | nan | nan | nan | Amazônia | 0.9 |
| c9dea4c7-f39c-34e5-b3f6-1f4fe05e7ec0 | -8.53887 | -54.76138 | 2026-08-19 04:40:00 | NOAA-20 | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 3.4 |
| 92c6fe85-f204-3a9b-8964-0e465d65e656 | -8.52603 | -54.75218 | 2026-08-19 04:40:00 | NOAA-20 | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 2.1 |
| c55e4899-fcff-3c26-b4d9-9ba2b694a029 | -9.4182 | -60.42091 | 2026-08-19 04:40:00 | NOAA-20 | ARIPUANÃ | MATO GROSSO | Brasil | 5101407 | 51 | 33 | nan | nan | nan | Amazônia | 2.2 |
| 4dd8e8d7-adb3-364d-b73f-c9d259c910a5 | -8.53329 | -54.76202 | 2026-08-19 04:40:00 | NOAA-20 | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 2.0 |
| d3fd2409-96c2-3cc0-af02-4d70b7bacd9b | -13.28128 | -51.64443 | 2026-08-19 04:40:00 | NOAA-20 | RIBEIRÃO CASCALHEIRA | MATO GROSSO | Brasil | 5107180 | 51 | 33 | nan | nan | nan | Cerrado | 17.7 |
| a257b83d-04a3-389c-853b-40e1ba39eff9 | -11.49241 | -45.10633 | 2026-08-19 04:40:00 | NOAA-20 | RIACHÃO DAS NEVES | BAHIA | Brasil | 2926202 | 29 | 33 | nan | nan | nan | Cerrado | 2.6 |
| 183a14c6-d8d5-3373-a9f9-16a43d98602e | -8.56416 | -54.77027 | 2026-08-19 04:40:00 | NOAA-20 | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 7.3 |
| fd7129b0-7b02-378b-8622-a4afcd585b59 | -9.39896 | -60.56485 | 2026-08-19 04:40:00 | NOAA-20 | ARIPUANÃ | MATO GROSSO | Brasil | 5101407 | 51 | 33 | nan | nan | nan | Amazônia | 2.0 |
| 47babe29-91ae-3b5d-89ed-ba802a2dc5b8 | -8.53527 | -54.75645 | 2026-08-19 04:40:00 | NOAA-20 | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 3.4 |
| f84b6430-d6e4-353a-8ebb-8f32c6cc6b4b | -14.4841 | -45.66632 | 2026-08-19 04:40:00 | NOAA-20 | JABORANDI | BAHIA | Brasil | 2917359 | 29 | 33 | nan | nan | nan | Cerrado | 2.5 |
| 302bec7d-441a-3d34-94a0-95c5e1bc761a | -15.23071 | -57.66027 | 2026-08-19 04:40:00 | NOAA-20 | LAMBARI D'OESTE | MATO GROSSO | Brasil | 5105234 | 51 | 33 | nan | nan | nan | Amazônia | 3.4 |
| 60427e6b-b3d9-3be7-ad91-ee51da69587d | -8.57147 | -54.75413 | 2026-08-19 04:40:00 | NOAA-20 | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 3.4 |
| 9a637f06-09aa-39ae-952b-bfa16f582ffb | -9.45744 | -51.61462 | 2026-08-19 04:40:00 | NOAA-20 | SÃO FÉLIX DO XINGU | PARÁ | Brasil | 1507300 | 15 | 33 | nan | nan | nan | Amazônia | 3.2 |
| c4b28e58-3bd2-3479-9a05-89401b2e027f | -15.27271 | -56.50873 | 2026-08-19 04:40:00 | NOAA-20 | JANGADA | MATO GROSSO | Brasil | 5104906 | 51 | 33 | nan | nan | nan | Cerrado | 1.4 |
| 0ccd81a0-f31b-3aca-a65f-741c46ec9165 | -8.52674 | -54.74797 | 2026-08-19 04:40:00 | NOAA-20 | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 1.0 |
| 4f11b5e7-33cf-3e00-a94e-b82018a1ced8 | -8.55037 | -54.77225 | 2026-08-19 04:40:00 | NOAA-20 | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 3.4 |
| 3b773bc3-f2fa-38db-90df-cd60282e0743 | -9.39176 | -60.56858 | 2026-08-19 04:40:00 | NOAA-20 | ARIPUANÃ | MATO GROSSO | Brasil | 5101407 | 51 | 33 | nan | nan | nan | Amazônia | 3.8 |
| 6c5c5618-f9b5-3a24-bf84-5f9744919c32 | -11.61936 | -46.91743 | 2026-08-19 04:40:00 | NOAA-20 | DIANÓPOLIS | TOCANTINS | Brasil | 1707009 | 17 | 33 | nan | nan | nan | Cerrado | 1.3 |
| 6f27a845-fc2c-3cb6-8bd2-ebd17de024b4 | -15.44237 | -41.38748 | 2026-08-19 04:40:00 | NOAA-20 | CÂNDIDO SALES | BAHIA | Brasil | 2906709 | 29 | 33 | nan | nan | nan | Mata Atlântica | 1.1 |
| 3295ce19-eca0-3790-8ca0-dc3491b57941 | -8.53543 | -54.74947 | 2026-08-19 04:40:00 | NOAA-20 | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 3.0 |
| 730924a1-6d8e-300c-adce-2009eb75321c | -12.24034 | -43.1586 | 2026-08-19 04:40:00 | NOAA-20 | IBOTIRAMA | BAHIA | Brasil | 2913200 | 29 | 33 | nan | nan | nan | Caatinga | 1.8 |
| 91e53c94-3b3d-3d0c-85d8-5440df601f6f | -8.55197 | -54.73793 | 2026-08-19 04:40:00 | NOAA-20 | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 2.0 |
| f27e214d-688e-3bb1-9db5-411acafeacf3 | -10.51659 | -50.78795 | 2026-08-19 04:40:00 | NOAA-20 | SANTA TEREZINHA | MATO GROSSO | Brasil | 5107776 | 51 | 33 | nan | nan | nan | Cerrado | 1.4 |
| f21a06f5-61cd-31ce-a708-753d1fd3285d | -9.161 | -59.71384 | 2026-08-19 04:40:00 | NOAA-20 | COLNIZA | MATO GROSSO | Brasil | 5103254 | 51 | 33 | nan | nan | nan | Amazônia | 1.9 |
| 84cb5854-ed77-366d-8b91-1c378fcb92ce | -8.54914 | -54.72873 | 2026-08-19 04:40:00 | NOAA-20 | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 3.2 |
| 22bb301f-4949-3577-b36f-05537dc89f6d | -12.51605 | -47.83765 | 2026-08-19 04:40:00 | NOAA-20 | PARANÃ | TOCANTINS | Brasil | 1716208 | 17 | 33 | nan | nan | nan | Cerrado | 0.8 |
| 39871182-27b7-376f-a858-8bc25adad87a | -10.52 | -50.78852 | 2026-08-19 04:40:00 | NOAA-20 | SANTA TEREZINHA | MATO GROSSO | Brasil | 5107776 | 51 | 33 | nan | nan | nan | Cerrado | 1.4 |
| 9594fc8f-d62e-3b43-933f-54adbb2db4cf | -9.39273 | -60.56353 | 2026-08-19 04:40:00 | NOAA-20 | ARIPUANÃ | MATO GROSSO | Brasil | 5101407 | 51 | 33 | nan | nan | nan | Amazônia | 3.8 |
| 71ee1d59-afd6-3f0c-9464-2d850e96988b | -9.74179 | -46.83902 | 2026-08-19 04:40:00 | NOAA-20 | LIZARDA | TOCANTINS | Brasil | 1712405 | 17 | 33 | nan | nan | nan | Cerrado | 2.0 |
| 9b7d619d-75cc-3afa-8fd6-2e4b933bb00b | -8.50136 | -54.87 | 2026-08-19 04:40:00 | NOAA-20 | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 2.7 |
| 7d3a9056-aafe-3fdc-8776-260b2cb0fed5 | -8.52961 | -54.73121 | 2026-08-19 04:40:00 | NOAA-20 | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 2.8 |
| 13e2d77f-c2f1-347e-8eff-4f52e130bfd5 | -9.73438 | -46.84165 | 2026-08-19 04:40:00 | NOAA-20 | LIZARDA | TOCANTINS | Brasil | 1712405 | 17 | 33 | nan | nan | nan | Cerrado | 0.8 |
| df3cb4cf-cb8c-3c8a-91ae-c69377b2aaf9 | -8.5432 | -54.76222 | 2026-08-19 04:40:00 | NOAA-20 | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 3.9 |
| 4cab98f1-a44d-3a69-ba44-812ef02611e2 | -14.46585 | -45.62906 | 2026-08-19 04:40:00 | NOAA-20 | JABORANDI | BAHIA | Brasil | 2917359 | 29 | 33 | nan | nan | nan | Cerrado | 3.5 |
| 487ffb30-e4e7-3577-a6db-6a3e959c2761 | -11.22573 | -55.07457 | 2026-08-19 04:40:00 | NOAA-20 | CLÁUDIA | MATO GROSSO | Brasil | 5103056 | 51 | 33 | nan | nan | nan | Amazônia | 2.1 |
| c5f35692-56f0-3eb2-81d8-734638ff1057 | -14.48792 | -45.66689 | 2026-08-19 04:40:00 | NOAA-20 | JABORANDI | BAHIA | Brasil | 2917359 | 29 | 33 | nan | nan | nan | Cerrado | 5.1 |
| b760ec9d-9761-3e44-b9b5-23fc96f7dd89 | -16.71466 | -46.40367 | 2026-08-19 04:40:00 | NOAA-20 | DOM BOSCO | MINAS GERAIS | Brasil | 3122470 | 31 | 33 | nan | nan | nan | Cerrado | 2.2 |
| b1da1feb-35d1-3008-878e-df7c4403d4d9 | -8.52943 | -54.76407 | 2026-08-19 04:40:00 | NOAA-20 | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 1.2 |
| 977569f1-caa7-3874-af7d-2a333b3b0d14 | -8.54095 | -54.77489 | 2026-08-19 04:40:00 | NOAA-20 | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 4.6 |
| b9a3ee02-8f5a-3493-bdaa-76493ced174d | -9.40328 | -60.57619 | 2026-08-19 04:40:00 | NOAA-20 | ARIPUANÃ | MATO GROSSO | Brasil | 5101407 | 51 | 33 | nan | nan | nan | Amazônia | 1.2 |
| 6670e7b3-9723-3351-a408-68b0f14a1781 | -8.58807 | -54.73584 | 2026-08-19 04:40:00 | NOAA-20 | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 1.9 |
| 4529aeb7-5558-3831-be06-f874ba8d6811 | -8.55472 | -54.773 | 2026-08-19 04:40:00 | NOAA-20 | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 3.4 |
| 8ce09782-9743-3893-b187-29496a5162dc | -11.38468 | -46.38672 | 2026-08-19 04:40:00 | NOAA-20 | FORMOSA DO RIO PRETO | BAHIA | Brasil | 2911105 | 29 | 33 | nan | nan | nan | Cerrado | 1.3 |
| 515f0f3f-d0d9-3d76-b8ad-dd5c35e3d713 | -10.57767 | -51.96185 | 2026-08-19 04:40:00 | NOAA-20 | PORTO ALEGRE DO NORTE | MATO GROSSO | Brasil | 5106778 | 51 | 33 | nan | nan | nan | Amazônia | 0.7 |
| d1aeb3f8-c37a-3a19-9619-64a5d609d173 | -10.2993 | -50.42065 | 2026-08-19 04:40:00 | NOAA-20 | SANTA TEREZINHA | MATO GROSSO | Brasil | 5107776 | 51 | 33 | nan | nan | nan | Amazônia | 1.4 |
| be956cbf-25db-3582-9f2a-839a511cd8aa | -8.58302 | -54.73918 | 2026-08-19 04:40:00 | NOAA-20 | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 1.9 |
| 62dd7182-d0c0-3c5c-b7ce-d7986842c7c0 | -9.42439 | -60.42213 | 2026-08-19 04:40:00 | NOAA-20 | ARIPUANÃ | MATO GROSSO | Brasil | 5101407 | 51 | 33 | nan | nan | nan | Amazônia | 2.2 |
| becd9dad-f1b4-3ae5-9853-9f9d3d74f842 | -8.57946 | -54.70856 | 2026-08-19 04:40:00 | NOAA-20 | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 2.2 |
| eac6713c-88ec-355a-87e3-1ca5ec507e3e | -13.43965 | -43.84177 | 2026-08-19 04:40:00 | NOAA-20 | SERRA DO RAMALHO | BAHIA | Brasil | 2930154 | 29 | 33 | nan | nan | nan | Cerrado | 2.5 |
| 3361ee3e-e197-343c-9994-e89322f8d9d0 | -15.78379 | -55.55716 | 2026-08-19 04:40:00 | NOAA-20 | SANTO ANTÔNIO DO LEVERGER | MATO GROSSO | Brasil | 5107800 | 51 | 33 | nan | nan | nan | Cerrado | 1.4 |
| 2f1e07dd-10e5-3417-9ab8-2520f77cf903 | -8.58878 | -54.73176 | 2026-08-19 04:40:00 | NOAA-20 | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 2.5 |
| c7424cd3-03bc-33be-9ee7-b1f084a079fb | -8.55926 | -54.72197 | 2026-08-19 04:40:00 | NOAA-20 | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 3.7 |
| a7bf49b6-0fd8-3b53-ae5b-15fe112c1f8f | -8.52746 | -54.74378 | 2026-08-19 04:40:00 | NOAA-20 | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 1.0 |
| 5a8a6508-b79a-3538-bc55-bdd505e856e5 | -15.77135 | -55.58075 | 2026-08-19 04:40:00 | NOAA-20 | SANTO ANTÔNIO DO LEVERGER | MATO GROSSO | Brasil | 5107800 | 51 | 33 | nan | nan | nan | Cerrado | 1.7 |
| 883a682e-862d-3dca-9277-afa6f20bdb52 | -8.53737 | -54.76983 | 2026-08-19 04:40:00 | NOAA-20 | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 6.6 |
| 9d9af51d-2561-3f0d-8cac-d138f89b5f17 | -9.47497 | -51.59692 | 2026-08-19 04:40:00 | NOAA-20 | SÃO FÉLIX DO XINGU | PARÁ | Brasil | 1507300 | 15 | 33 | nan | nan | nan | Amazônia | 1.6 |
| a16bff42-5df6-31c0-abad-9be9ab58da50 | -9.50661 | -51.64301 | 2026-08-19 04:40:00 | NOAA-20 | SÃO FÉLIX DO XINGU | PARÁ | Brasil | 1507300 | 15 | 33 | nan | nan | nan | Amazônia | 1.2 |
| 659fc954-0e20-3eea-bb76-3abd9709dfb0 | -11.12302 | -47.28383 | 2026-08-19 04:40:00 | NOAA-20 | ALMAS | TOCANTINS | Brasil | 1700400 | 17 | 33 | nan | nan | nan | Cerrado | 1.4 |
| baf527e5-867f-35cc-904b-a8b22b1a60ed | -10.10807 | -54.28563 | 2026-08-19 04:40:00 | NOAA-20 | MATUPÁ | MATO GROSSO | Brasil | 5105606 | 51 | 33 | nan | nan | nan | Amazônia | 3.2 |
| a51bb350-dc5c-340b-ad1f-1b81bdbf4322 | -8.56152 | -54.68399 | 2026-08-19 04:40:00 | NOAA-20 | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 1.4 |
| 4931e520-b8f9-3d2d-a464-889f98b74026 | -11.22016 | -55.05693 | 2026-08-19 04:40:00 | NOAA-20 | CLÁUDIA | MATO GROSSO | Brasil | 5103056 | 51 | 33 | nan | nan | nan | Amazônia | 2.2 |
| 722dc735-633c-388c-8beb-2b8c25704412 | -14.45143 | -45.62933 | 2026-08-19 04:40:00 | NOAA-20 | JABORANDI | BAHIA | Brasil | 2917359 | 29 | 33 | nan | nan | nan | Cerrado | 1.2 |
| bf1d0f56-7960-3bdd-abe8-0eb72546d3b1 | -11.11161 | -47.26688 | 2026-08-19 04:40:00 | NOAA-20 | ALMAS | TOCANTINS | Brasil | 1700400 | 17 | 33 | nan | nan | nan | Cerrado | 1.9 |
| fb1dd625-0c2f-3ac3-8f71-eed0fe377195 | -8.5578 | -54.73022 | 2026-08-19 04:40:00 | NOAA-20 | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 2.7 |
| cdad8054-6f20-30a7-8567-161600ff0d13 | -9.59297 | -49.32114 | 2026-08-19 04:40:00 | NOAA-20 | ABREULÂNDIA | TOCANTINS | Brasil | 1700251 | 17 | 33 | nan | nan | nan | Cerrado | 0.8 |
| ee39a346-45c0-3eee-b370-c051294bd4e7 | -11.22719 | -55.06647 | 2026-08-19 04:40:00 | NOAA-20 | CLÁUDIA | MATO GROSSO | Brasil | 5103056 | 51 | 33 | nan | nan | nan | Amazônia | 1.7 |
| 9e75c3a0-a086-3518-8538-1b51f541fc4e | -12.79581 | -48.4317 | 2026-08-19 04:40:00 | NOAA-20 | SÃO SALVADOR DO TOCANTINS | TOCANTINS | Brasil | 1720259 | 17 | 33 | nan | nan | nan | Cerrado | 2.4 |
| 51ae6aa4-885f-31c4-8b1e-fdc98e735a48 | -12.82873 | -48.41837 | 2026-08-19 04:40:00 | NOAA-20 | SÃO SALVADOR DO TOCANTINS | TOCANTINS | Brasil | 1720259 | 17 | 33 | nan | nan | nan | Cerrado | 1.9 |
| 569092f0-a160-38b2-8d63-49e1d4641edc | -8.56498 | -54.74018 | 2026-08-19 04:40:00 | NOAA-20 | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 2.3 |
| ae82393e-56fe-3206-a8aa-85b149f0a9e3 | -12.80367 | -48.44744 | 2026-08-19 04:40:00 | NOAA-20 | SÃO SALVADOR DO TOCANTINS | TOCANTINS | Brasil | 1720259 | 17 | 33 | nan | nan | nan | Cerrado | 1.4 |
| 15c76f30-cf30-3a0f-8cca-8c388378a7f1 | -11.81078 | -56.6034 | 2026-08-19 04:40:00 | NOAA-20 | PORTO DOS GAÚCHOS | MATO GROSSO | Brasil | 5106802 | 51 | 33 | nan | nan | nan | Amazônia | 2.1 |


[Clique aqui para ver as próximas entradas](README41.md)
