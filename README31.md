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

## Dados Diários - Página 31

| ID | Latitude | Longitude | Data/Hora GMT | Satélite | Município | Estado | País | Município ID | Estado ID | País ID | Dias sem Chuva | Precipitação | Risco de Fogo | Bioma | FRP |
|----|----------|-----------|---------------|----------|-----------|--------|------|--------------|-----------|---------|----------------|--------------|----------------|-------|-----|
| f4b9c635-f6b2-38fa-84ea-31e8a7560d54 | -6.34149 | -44.08287 | 2026-08-20 04:19:00 | NOAA-20 | COLINAS | MARANHÃO | Brasil | 2103505 | 21 | 33 | nan | nan | nan | Cerrado | 4.7 |
| 27df95c8-7425-3610-acb8-354bf087a0ed | -11.32251 | -45.0186 | 2026-08-20 04:19:00 | NOAA-20 | FORMOSA DO RIO PRETO | BAHIA | Brasil | 2911105 | 29 | 33 | nan | nan | nan | Cerrado | 1.1 |
| 46e94dc8-8b64-32ed-95ea-7b7add55a936 | -8.49599 | -54.86675 | 2026-08-20 04:19:00 | NOAA-20 | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 3.7 |
| e26ed822-887b-3c02-8efb-078d69239eef | -7.96884 | -44.65813 | 2026-08-20 04:19:00 | NOAA-20 | URUÇUÍ | PIAUÍ | Brasil | 2211209 | 22 | 33 | nan | nan | nan | Cerrado | 4.6 |
| 73578975-6cb7-3367-9775-9c5e91fed1d0 | -9.75387 | -43.31813 | 2026-08-20 04:19:00 | NOAA-20 | PILÃO ARCADO | BAHIA | Brasil | 2924405 | 29 | 33 | nan | nan | nan | Caatinga | 1.5 |
| 1489aad5-0800-3c41-af78-17dd57797b29 | -7.4881 | -43.81739 | 2026-08-20 04:19:00 | NOAA-20 | SEBASTIÃO LEAL | PIAUÍ | Brasil | 2210631 | 22 | 33 | nan | nan | nan | Cerrado | 0.4 |
| e65bee27-262c-3f8b-b3e3-802f80d43408 | -6.43884 | -52.73676 | 2026-08-20 04:19:00 | NOAA-20 | SÃO FÉLIX DO XINGU | PARÁ | Brasil | 1507300 | 15 | 33 | nan | nan | nan | Amazônia | 1.7 |
| 6d18ab43-0681-3cf8-a19f-a0590e5b6ea2 | -5.92069 | -46.47519 | 2026-08-20 04:19:00 | NOAA-20 | SÍTIO NOVO | MARANHÃO | Brasil | 2111805 | 21 | 33 | nan | nan | nan | Cerrado | 1.4 |
| c2d8b2a1-0a55-3442-bcab-12ee852cf31d | -10.27751 | -48.23943 | 2026-08-20 04:19:00 | NOAA-20 | PALMAS | TOCANTINS | Brasil | 1721000 | 17 | 33 | nan | nan | nan | Cerrado | 7.7 |
| 4fb5d99f-d782-35bf-aaee-b33d057c26a7 | -6.38481 | -54.94402 | 2026-08-20 04:19:00 | NOAA-20 | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 2.0 |
| 16e36193-735a-315c-a7c9-0dafd1f04011 | -8.65943 | -54.59698 | 2026-08-20 04:19:00 | NOAA-20 | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 2.5 |
| 6c9bf5aa-558c-392a-89aa-3716508b08f5 | -6.44051 | -52.7586 | 2026-08-20 04:19:00 | NOAA-20 | SÃO FÉLIX DO XINGU | PARÁ | Brasil | 1507300 | 15 | 33 | nan | nan | nan | Amazônia | 2.9 |
| e7c31ecf-af38-388f-8afa-a0de70ef5149 | -7.01212 | -45.89276 | 2026-08-20 04:19:00 | NOAA-20 | FORTALEZA DOS NOGUEIRAS | MARANHÃO | Brasil | 2104107 | 21 | 33 | nan | nan | nan | Cerrado | 1.2 |
| be7892ca-53c3-3bd9-9109-704337c4f979 | -6.2433 | -55.42466 | 2026-08-20 04:19:00 | NOAA-20 | ITAITUBA | PARÁ | Brasil | 1503606 | 15 | 33 | nan | nan | nan | Amazônia | 1.0 |
| 176747e9-9699-34f9-8ff8-17c6f430c0e4 | -12.2328 | -46.99702 | 2026-08-20 04:19:00 | NOAA-20 | TAIPAS DO TOCANTINS | TOCANTINS | Brasil | 1720937 | 17 | 33 | nan | nan | nan | Cerrado | 0.8 |
| b20e2f9e-6a1d-39a9-b9db-10f67da88694 | -9.39907 | -37.81066 | 2026-08-20 04:19:00 | NOAA-20 | OLHO D'ÁGUA DO CASADO | ALAGOAS | Brasil | 2705804 | 27 | 33 | nan | nan | nan | Caatinga | 0.8 |
| 2b71dd7f-0988-3173-98ea-cc72f4d14bbf | -8.66166 | -54.65105 | 2026-08-20 04:19:00 | NOAA-20 | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 14.1 |
| 9c7a0226-68d4-3394-a74a-4373cc1e0168 | -7.35931 | -45.82845 | 2026-08-20 04:19:00 | NOAA-20 | BALSAS | MARANHÃO | Brasil | 2101400 | 21 | 33 | nan | nan | nan | Cerrado | 7.2 |
| c4579653-1de5-35e2-a7cc-9a127c475d18 | -5.42475 | -43.4382 | 2026-08-20 04:19:00 | NOAA-20 | MATÕES | MARANHÃO | Brasil | 2106607 | 21 | 33 | nan | nan | nan | Cerrado | 3.4 |
| 9ce9ff8a-7e1a-332c-a4df-2444bd074640 | -6.43386 | -52.76446 | 2026-08-20 04:19:00 | NOAA-20 | SÃO FÉLIX DO XINGU | PARÁ | Brasil | 1507300 | 15 | 33 | nan | nan | nan | Amazônia | 2.2 |
| 2c8de60d-2616-3042-85d7-316ac17ab555 | -7.47482 | -55.32462 | 2026-08-20 04:19:00 | NOAA-20 | NOVO PROGRESSO | PARÁ | Brasil | 1505031 | 15 | 33 | nan | nan | nan | Amazônia | 1.7 |
| 5d1fb761-0b99-3260-81ac-26e575c3f9ca | -7.96323 | -44.67171 | 2026-08-20 04:19:00 | NOAA-20 | URUÇUÍ | PIAUÍ | Brasil | 2211209 | 22 | 33 | nan | nan | nan | Cerrado | 4.0 |
| 50f29e46-3635-31a1-a1ed-54cff9c6ad1c | -8.65791 | -54.59605 | 2026-08-20 04:19:00 | NOAA-20 | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 1.6 |
| f5adbf97-3ba5-3797-9440-ab65d3c3c95a | -8.50793 | -54.86927 | 2026-08-20 04:19:00 | NOAA-20 | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 2.1 |
| becaf3cb-14b2-3094-b90e-f89848a34142 | -7.60655 | -45.16996 | 2026-08-20 04:19:00 | NOAA-20 | RIBEIRO GONÇALVES | PIAUÍ | Brasil | 2208908 | 22 | 33 | nan | nan | nan | Cerrado | 1.2 |
| 86b7856b-05b1-3a92-9a4a-3b9be9f4fa63 | -8.58169 | -54.78448 | 2026-08-20 04:19:00 | NOAA-20 | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 2.6 |
| e18c945c-b540-3035-8462-59066667735c | -6.26955 | -43.27507 | 2026-08-20 04:19:00 | NOAA-20 | SÃO FRANCISCO DO MARANHÃO | MARANHÃO | Brasil | 2110906 | 21 | 33 | nan | nan | nan | Cerrado | 10.5 |
| 1fc71957-6305-3082-89e9-c05ed2cb273f | -6.3839 | -54.94896 | 2026-08-20 04:19:00 | NOAA-20 | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 2.0 |
| 758649d2-4f64-375e-83b3-8e38fe65b70f | -10.75037 | -50.35362 | 2026-08-20 04:19:00 | NOAA-20 | LAGOA DA CONFUSÃO | TOCANTINS | Brasil | 1711902 | 17 | 33 | nan | nan | nan | Cerrado | 5.9 |
| 7288632c-e0d4-3c64-a3b6-056e91cd43c3 | -7.65165 | -42.77838 | 2026-08-20 04:19:00 | NOAA-20 | FLORES DO PIAUÍ | PIAUÍ | Brasil | 2203800 | 22 | 33 | nan | nan | nan | Caatinga | 3.4 |
| 1c76b7c9-bbb5-3a09-92fc-2321135a653e | -5.88686 | -48.17295 | 2026-08-20 04:19:00 | NOAA-20 | ARAGUATINS | TOCANTINS | Brasil | 1702208 | 17 | 33 | nan | nan | nan | Amazônia | 1.4 |
| c8b1f4b4-64e3-37e4-85cf-87360f5d08c2 | -8.52912 | -54.86629 | 2026-08-20 04:19:00 | NOAA-20 | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 2.1 |
| db49c949-6fe7-3764-8a05-59b24988c9c7 | -8.55655 | -54.65773 | 2026-08-20 04:19:00 | NOAA-20 | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 1.5 |
| 9ed3de74-4919-3f50-b956-1db60a0660f0 | -7.3473 | -45.81463 | 2026-08-20 04:19:00 | NOAA-20 | BALSAS | MARANHÃO | Brasil | 2101400 | 21 | 33 | nan | nan | nan | Cerrado | 6.0 |
| 0e632aa0-a4a9-3a85-b3b7-94c129c3cf4a | -7.6522 | -42.77487 | 2026-08-20 04:19:00 | NOAA-20 | FLORES DO PIAUÍ | PIAUÍ | Brasil | 2203800 | 22 | 33 | nan | nan | nan | Caatinga | 1.6 |
| bd9d4632-5b6f-3ec6-acbc-9429c2dc8d58 | -6.2458 | -55.40748 | 2026-08-20 04:19:00 | NOAA-20 | ITAITUBA | PARÁ | Brasil | 1503606 | 15 | 33 | nan | nan | nan | Amazônia | 1.1 |
| cffc92af-60e2-39de-a5aa-d6964cd70c1a | -5.43038 | -48.41408 | 2026-08-20 04:19:00 | NOAA-20 | SÃO JOÃO DO ARAGUAIA | PARÁ | Brasil | 1507508 | 15 | 33 | nan | nan | nan | Amazônia | 2.5 |
| b58da6d0-46f2-3fb6-ac50-5d5913ed3605 | -6.26625 | -43.27454 | 2026-08-20 04:19:00 | NOAA-20 | SÃO FRANCISCO DO MARANHÃO | MARANHÃO | Brasil | 2110906 | 21 | 33 | nan | nan | nan | Cerrado | 10.5 |
| f1d50147-dd25-3aa1-bccf-0a9132189a65 | -9.8028 | -49.19387 | 2026-08-20 04:19:00 | NOAA-20 | DIVINÓPOLIS DO TOCANTINS | TOCANTINS | Brasil | 1707108 | 17 | 33 | nan | nan | nan | Cerrado | 1.6 |
| 0c8faeb7-6fb4-3b9c-bf5b-3a768c613d50 | -8.57063 | -54.77774 | 2026-08-20 04:19:00 | NOAA-20 | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 1.3 |
| 3c4788f6-82c8-31e9-9dec-978226f44c84 | -6.779 | -42.88745 | 2026-08-20 04:19:00 | NOAA-20 | FLORIANO | PIAUÍ | Brasil | 2203909 | 22 | 33 | nan | nan | nan | Caatinga | 1.9 |
| 7c49a118-e2d7-3b80-9dfb-af0a3c373415 | -5.54047 | -42.27539 | 2026-08-20 04:19:00 | NOAA-20 | BENEDITINOS | PIAUÍ | Brasil | 2201606 | 22 | 33 | nan | nan | nan | Caatinga | 2.6 |
| 66a2d62e-5abf-3c6c-988d-4f8f01e65f58 | -7.60994 | -45.1705 | 2026-08-20 04:19:00 | NOAA-20 | RIBEIRO GONÇALVES | PIAUÍ | Brasil | 2208908 | 22 | 33 | nan | nan | nan | Cerrado | 1.2 |
| 2aa6ed6d-f874-3d19-bd23-215d89ef1702 | -5.73606 | -43.27504 | 2026-08-20 04:19:00 | NOAA-20 | PARNARAMA | MARANHÃO | Brasil | 2107803 | 21 | 33 | nan | nan | nan | Cerrado | 3.4 |
| d744772a-a925-3624-bcb2-78d742f63dd4 | -10.7898 | -50.30611 | 2026-08-20 04:19:00 | NOAA-20 | LAGOA DA CONFUSÃO | TOCANTINS | Brasil | 1711902 | 17 | 33 | nan | nan | nan | Cerrado | 3.9 |
| 738fe8d6-884f-3f04-8396-9fab84e287e1 | -6.42368 | -52.75888 | 2026-08-20 04:19:00 | NOAA-20 | SÃO FÉLIX DO XINGU | PARÁ | Brasil | 1507300 | 15 | 33 | nan | nan | nan | Amazônia | 4.0 |
| b96f51a8-e430-309d-8160-497e261529f3 | -8.49663 | -54.87396 | 2026-08-20 04:19:00 | NOAA-20 | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 2.8 |
| cfe880c8-8ee9-3071-a887-dd55cdc1d328 | -7.35077 | -45.8152 | 2026-08-20 04:19:00 | NOAA-20 | BALSAS | MARANHÃO | Brasil | 2101400 | 21 | 33 | nan | nan | nan | Cerrado | 6.0 |
| 254b5df6-2d9a-340c-b3d4-3c209f5f4af6 | -12.19157 | -45.15113 | 2026-08-20 04:19:00 | NOAA-20 | BARREIRAS | BAHIA | Brasil | 2903201 | 29 | 33 | nan | nan | nan | Cerrado | 1.7 |
| 9abcd934-1d42-3efb-898e-c15e1683304a | -12.24952 | -43.13808 | 2026-08-20 04:19:00 | NOAA-20 | IBOTIRAMA | BAHIA | Brasil | 2913200 | 29 | 33 | nan | nan | nan | Caatinga | 0.7 |
| 9944d324-8612-386b-a062-8811a5429236 | -7.53333 | -55.58166 | 2026-08-20 04:19:00 | NOAA-20 | NOVO PROGRESSO | PARÁ | Brasil | 1505031 | 15 | 33 | nan | nan | nan | Amazônia | 2.4 |
| a630a877-72c3-3e3e-91a1-45343098fe5f | -7.17253 | -43.08477 | 2026-08-20 04:19:00 | NOAA-20 | FLORIANO | PIAUÍ | Brasil | 2203909 | 22 | 33 | nan | nan | nan | Caatinga | 1.2 |
| da9038d7-6602-3302-acdc-02730e70fa43 | -12.37924 | -46.45255 | 2026-08-20 04:19:00 | NOAA-20 | TAGUATINGA | TOCANTINS | Brasil | 1720903 | 17 | 33 | nan | nan | nan | Cerrado | 1.8 |
| ea1f9c92-9737-3648-82c3-083f34bc3d21 | -8.55961 | -54.77082 | 2026-08-20 04:19:00 | NOAA-20 | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 3.4 |
| f7b3c59e-038d-3a51-906b-9963e98a6bd5 | -5.79483 | -55.72653 | 2026-08-20 04:19:00 | NOAA-20 | ITAITUBA | PARÁ | Brasil | 1503606 | 15 | 33 | nan | nan | nan | Amazônia | 2.4 |
| c402b7ce-1641-3117-b99f-733e07c950a1 | -6.24175 | -43.68515 | 2026-08-20 04:19:00 | NOAA-20 | PASSAGEM FRANCA | MARANHÃO | Brasil | 2107902 | 21 | 33 | nan | nan | nan | Cerrado | 2.3 |
| 40e9fdb3-9456-35d1-a182-ef6fb81631a6 | -6.77954 | -42.88398 | 2026-08-20 04:19:00 | NOAA-20 | FLORIANO | PIAUÍ | Brasil | 2203909 | 22 | 33 | nan | nan | nan | Caatinga | 1.9 |
| 2d6fec5b-d03d-31a3-9b6b-5d3bfb41aefd | -6.37952 | -54.93777 | 2026-08-20 04:19:00 | NOAA-20 | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 2.1 |
| 832232b6-8719-3864-aae7-492256e4b5e5 | -7.9638 | -44.66818 | 2026-08-20 04:19:00 | NOAA-20 | URUÇUÍ | PIAUÍ | Brasil | 2211209 | 22 | 33 | nan | nan | nan | Cerrado | 19.0 |
| 65a23b3e-37aa-3809-8aa9-bce5c5da6395 | -5.54102 | -42.27189 | 2026-08-20 04:19:00 | NOAA-20 | ALTO LONGÁ | PIAUÍ | Brasil | 2200301 | 22 | 33 | nan | nan | nan | Caatinga | 2.7 |
| 8d0cfc05-1fd9-3849-a1dd-01944ad8aba6 | -8.49843 | -54.86457 | 2026-08-20 04:19:00 | NOAA-20 | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 4.4 |
| d7b7a614-f839-3348-b48a-582398316ae8 | -7.75497 | -49.2035 | 2026-08-20 04:19:00 | NOAA-20 | ARAPOEMA | TOCANTINS | Brasil | 1702307 | 17 | 33 | nan | nan | nan | Amazônia | 3.5 |
| bbd3a6dd-27a8-3273-bf8f-f09d32398bbd | -7.75848 | -49.20808 | 2026-08-20 04:19:00 | NOAA-20 | ARAPOEMA | TOCANTINS | Brasil | 1702307 | 17 | 33 | nan | nan | nan | Amazônia | 1.8 |
| 294ab84c-18a4-3564-890c-f58f8a5cc464 | -9.79886 | -46.62787 | 2026-08-20 04:19:00 | NOAA-20 | LIZARDA | TOCANTINS | Brasil | 1712405 | 17 | 33 | nan | nan | nan | Cerrado | 2.1 |
| 6543b8a6-fa8e-3414-b634-314e901d71ce | -6.51771 | -43.6159 | 2026-08-20 04:19:00 | NOAA-20 | SÃO JOÃO DOS PATOS | MARANHÃO | Brasil | 2111102 | 21 | 33 | nan | nan | nan | Cerrado | 1.1 |
| c82f896a-a864-361c-919a-210ae1cbe13d | -6.29027 | -43.63605 | 2026-08-20 04:19:00 | NOAA-20 | PASSAGEM FRANCA | MARANHÃO | Brasil | 2107902 | 21 | 33 | nan | nan | nan | Cerrado | 5.3 |
| 958f6c3c-ad29-37c6-ac9a-4b34ce82cb20 | -5.79689 | -55.71493 | 2026-08-20 04:19:00 | NOAA-20 | ITAITUBA | PARÁ | Brasil | 1503606 | 15 | 33 | nan | nan | nan | Amazônia | 1.4 |
| 96e6b3ab-aad8-3f06-9d09-2c61e3e6ff6f | -7.34953 | -45.82287 | 2026-08-20 04:19:00 | NOAA-20 | BALSAS | MARANHÃO | Brasil | 2101400 | 21 | 33 | nan | nan | nan | Cerrado | 7.8 |
| 796fb2c1-e0ea-3bf3-af7e-624861dfd1b8 | -5.79587 | -55.72072 | 2026-08-20 04:19:00 | NOAA-20 | ITAITUBA | PARÁ | Brasil | 1503606 | 15 | 33 | nan | nan | nan | Amazônia | 2.4 |
| 6cf3ecdb-60b6-38a6-a6cc-567d30bda56f | -9.27285 | -45.6455 | 2026-08-20 04:19:00 | NOAA-20 | SANTA FILOMENA | PIAUÍ | Brasil | 2209203 | 22 | 33 | nan | nan | nan | Cerrado | 2.3 |
| c15014c1-91e9-306e-8ebc-a32b567733ca | -6.39102 | -54.94528 | 2026-08-20 04:19:00 | NOAA-20 | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 2.0 |
| 64a525c3-85cc-3cd5-9860-71dce1e76093 | -4.8066 | -45.77405 | 2026-08-20 04:19:00 | NOAA-20 | ARAME | MARANHÃO | Brasil | 2100956 | 21 | 33 | nan | nan | nan | Amazônia | 1.2 |
| 9ddf4698-cddc-3e67-9537-a19e35bbb0c2 | -5.52413 | -44.11465 | 2026-08-20 04:19:00 | NOAA-20 | GOVERNADOR LUIZ ROCHA | MARANHÃO | Brasil | 2104628 | 21 | 33 | nan | nan | nan | Cerrado | 1.2 |
| 5e3b6fbb-b865-3947-b3b8-1b8878d3e323 | -8.45032 | -51.55156 | 2026-08-20 04:19:00 | NOAA-20 | CUMARU DO NORTE | PARÁ | Brasil | 1502764 | 15 | 33 | nan | nan | nan | Amazônia | 1.5 |
| 2205ec94-4543-3bdc-9ea6-c5633930adaa | -8.58337 | -54.77552 | 2026-08-20 04:19:00 | NOAA-20 | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 3.2 |
| 075d6a07-c29b-3c66-b483-439c6ba9cdff | -7.16922 | -43.08424 | 2026-08-20 04:19:00 | NOAA-20 | FLORIANO | PIAUÍ | Brasil | 2203909 | 22 | 33 | nan | nan | nan | Caatinga | 1.0 |
| 34283982-773c-36a0-a988-2895be6b2978 | -8.55786 | -54.66462 | 2026-08-20 04:19:00 | NOAA-20 | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 2.4 |
| 33a52da4-808a-30de-964d-8da7733f3738 | -6.38572 | -54.93908 | 2026-08-20 04:19:00 | NOAA-20 | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 3.8 |
| d323f4b8-30c7-3529-827d-02ef2f322253 | -8.09726 | -51.66474 | 2026-08-20 04:19:00 | NOAA-20 | OURILÂNDIA DO NORTE | PARÁ | Brasil | 1505437 | 15 | 33 | nan | nan | nan | Amazônia | 3.0 |
| fdbdd2c6-5e5f-385a-84a7-072c90c6e4f9 | -8.5011 | -54.87265 | 2026-08-20 04:19:00 | NOAA-20 | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 2.9 |
| ff9e0663-c038-3fba-be99-b15803c7671f | -8.55943 | -54.65608 | 2026-08-20 04:19:00 | NOAA-20 | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 2.0 |
| 59f928a9-490d-3d47-9f30-a6bd04b191fa | -12.25621 | -43.16194 | 2026-08-20 04:19:00 | NOAA-20 | IBOTIRAMA | BAHIA | Brasil | 2913200 | 29 | 33 | nan | nan | nan | Caatinga | 6.8 |
| ccdf9ac4-d930-3724-be5a-023780dd9c7d | -7.2485 | -49.89324 | 2026-08-20 04:19:00 | NOAA-20 | RIO MARIA | PARÁ | Brasil | 1506161 | 15 | 33 | nan | nan | nan | Amazônia | 4.1 |
| db0cec32-b2ea-34be-b59b-78eaed898877 | -8.52827 | -54.87077 | 2026-08-20 04:19:00 | NOAA-20 | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 2.1 |
| dca5f73e-573f-3e4f-ad8a-020c390e0135 | -8.58253 | -54.78 | 2026-08-20 04:19:00 | NOAA-20 | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 3.2 |
| 03b1eac1-010a-3d87-b1a8-95fc5b23d355 | -4.38332 | -55.47774 | 2026-08-20 04:19:00 | NOAA-20 | RURÓPOLIS | PARÁ | Brasil | 1506195 | 15 | 33 | nan | nan | nan | Amazônia | 1.9 |
| b0515520-b88b-3208-aa9d-30e2122cb3dd | -11.31862 | -45.02161 | 2026-08-20 04:19:00 | NOAA-20 | FORMOSA DO RIO PRETO | BAHIA | Brasil | 2911105 | 29 | 33 | nan | nan | nan | Cerrado | 2.2 |
| 97876c37-8d75-34db-b5cc-1853c7b79b64 | -6.94892 | -52.8064 | 2026-08-20 04:19:00 | NOAA-20 | SÃO FÉLIX DO XINGU | PARÁ | Brasil | 1507300 | 15 | 33 | nan | nan | nan | Amazônia | 0.9 |
| 875372cf-faa1-3907-81cf-09db74a2582b | -8.66089 | -54.65527 | 2026-08-20 04:19:00 | NOAA-20 | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 10.1 |
| 5afc7219-99c9-38b9-98c5-d54552d42d70 | -8.49428 | -54.87603 | 2026-08-20 04:19:00 | NOAA-20 | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 2.0 |
| eb9557ef-417d-3919-aa57-88fe7f58b50a | -7.97104 | -44.66572 | 2026-08-20 04:19:00 | NOAA-20 | URUÇUÍ | PIAUÍ | Brasil | 2211209 | 22 | 33 | nan | nan | nan | Cerrado | 8.2 |
| 2af6b7ea-b038-3457-bb8b-7c9a827de20e | -5.7938 | -55.73233 | 2026-08-20 04:19:00 | NOAA-20 | ITAITUBA | PARÁ | Brasil | 1503606 | 15 | 33 | nan | nan | nan | Amazônia | 2.2 |
| c5f9608a-486e-3f53-9945-6fa19043e53b | -8.66403 | -54.63813 | 2026-08-20 04:19:00 | NOAA-20 | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 3.8 |
| c3b040fa-02e6-3506-b330-26a33ef4ce56 | -7.01743 | -47.97314 | 2026-08-20 04:19:00 | NOAA-20 | WANDERLÂNDIA | TOCANTINS | Brasil | 1722081 | 17 | 33 | nan | nan | nan | Cerrado | 1.6 |
| 0794e874-1516-32aa-8128-22910dd0a1ca | -9.64285 | -47.81062 | 2026-08-20 04:19:00 | NOAA-20 | RIO SONO | TOCANTINS | Brasil | 1718758 | 17 | 33 | nan | nan | nan | Cerrado | 1.4 |
| 31dfa49b-c204-328b-8420-0e04bf855a4e | -8.3601 | -46.3379 | 2026-08-20 04:19:00 | NOAA-20 | BALSAS | MARANHÃO | Brasil | 2101400 | 21 | 33 | nan | nan | nan | Cerrado | 4.0 |
| 760db6f7-8ba1-3aad-b64b-385d4a51dc63 | -7.12933 | -47.50064 | 2026-08-20 04:19:00 | NOAA-20 | CAROLINA | MARANHÃO | Brasil | 2102804 | 21 | 33 | nan | nan | nan | Cerrado | 2.5 |
| 2ce0e096-72c4-3c0a-adb0-d93f3c00a1f3 | -8.52069 | -54.86728 | 2026-08-20 04:19:00 | NOAA-20 | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 2.8 |
| de55122f-f801-3e4a-89ea-e8097ad52100 | -6.8002 | -43.01169 | 2026-08-20 04:19:00 | NOAA-20 | FLORIANO | PIAUÍ | Brasil | 2203909 | 22 | 33 | nan | nan | nan | Caatinga | 1.2 |
| 8989d9e8-7614-3f8e-93cb-406d241a6a6b | -8.52227 | -54.86968 | 2026-08-20 04:19:00 | NOAA-20 | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 2.1 |


[Clique aqui para ver as próximas entradas](README32.md)
