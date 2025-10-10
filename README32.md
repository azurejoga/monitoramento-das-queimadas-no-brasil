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

## Dados Diários - Página 32

| ID | Latitude | Longitude | Data/Hora GMT | Satélite | Município | Estado | País | Município ID | Estado ID | País ID | Dias sem Chuva | Precipitação | Risco de Fogo | Bioma | FRP |
|----|----------|-----------|---------------|----------|-----------|--------|------|--------------|-----------|---------|----------------|--------------|----------------|-------|-----|
| c5d5675e-79aa-399b-85ae-4cf655c36153 | -10.90547 | -47.47059 | 2025-10-10 04:02:00 | NOAA-20 | PONTE ALTA DO TOCANTINS | TOCANTINS | Brasil | 1717909 | 17 | 33 | nan | nan | nan | Cerrado | 1.7 |
| 54485f36-170b-3dc6-b1de-ef4bfcdf5ba6 | -16.74222 | -43.97977 | 2025-10-10 04:02:00 | NOAA-20 | MONTES CLAROS | MINAS GERAIS | Brasil | 3143302 | 31 | 33 | nan | nan | nan | Cerrado | 0.5 |
| f199c61e-6f27-36e2-b23b-4d83fafd7561 | -13.50006 | -43.66911 | 2025-10-10 04:02:00 | NOAA-20 | SERRA DO RAMALHO | BAHIA | Brasil | 2930154 | 29 | 33 | nan | nan | nan | Cerrado | 1.5 |
| c8628860-9983-3b3e-a6af-6a2ba966bb39 | -12.63398 | -45.06295 | 2025-10-10 04:02:00 | NOAA-20 | SÃO DESIDÉRIO | BAHIA | Brasil | 2928901 | 29 | 33 | nan | nan | nan | Cerrado | 5.4 |
| 1b6e12a7-be99-303b-907d-cd6a1394ebb5 | -10.76711 | -47.60846 | 2025-10-10 04:02:00 | NOAA-20 | PONTE ALTA DO TOCANTINS | TOCANTINS | Brasil | 1717909 | 17 | 33 | nan | nan | nan | Cerrado | 1.2 |
| 0bb9c52b-9772-3b89-896c-632e0f5de2cb | -13.84089 | -45.85685 | 2025-10-10 04:02:00 | NOAA-20 | JABORANDI | BAHIA | Brasil | 2917359 | 29 | 33 | nan | nan | nan | Cerrado | 2.5 |
| 05b5b337-e0a0-3961-bc4b-c4b628c8de38 | -16.26412 | -47.16322 | 2025-10-10 04:02:00 | NOAA-20 | UNAÍ | MINAS GERAIS | Brasil | 3170404 | 31 | 33 | nan | nan | nan | Cerrado | 1.4 |
| 01377f94-2d19-3d64-8f86-844413ca7a2f | -17.21682 | -47.65475 | 2025-10-10 04:02:00 | NOAA-20 | IPAMERI | GOIÁS | Brasil | 5210109 | 52 | 33 | nan | nan | nan | Cerrado | 7.0 |
| 7de6bfe5-bef8-3536-a62b-4ea9b1b83f62 | -11.64055 | -47.53417 | 2025-10-10 04:02:00 | NOAA-20 | NATIVIDADE | TOCANTINS | Brasil | 1714203 | 17 | 33 | nan | nan | nan | Cerrado | 1.9 |
| 3f59a5dc-c405-35a1-822b-4e17325b5895 | -16.69884 | -45.00516 | 2025-10-10 04:02:00 | NOAA-20 | PONTO CHIQUE | MINAS GERAIS | Brasil | 3152131 | 31 | 33 | nan | nan | nan | Cerrado | 1.0 |
| ee120571-54c3-33e8-acb1-05b9f947f25d | -10.82193 | -42.82454 | 2025-10-10 04:02:00 | NOAA-20 | XIQUE-XIQUE | BAHIA | Brasil | 2933604 | 29 | 33 | nan | nan | nan | Cerrado | 2.4 |
| 7cbb103d-18a8-3aac-ab82-480e1e5b825b | -12.10552 | -44.99368 | 2025-10-10 04:02:00 | NOAA-20 | BARREIRAS | BAHIA | Brasil | 2903201 | 29 | 33 | nan | nan | nan | Cerrado | 1.1 |
| 7b8b47a7-ae24-3787-974c-47b47dd37c23 | -15.73741 | -49.03571 | 2025-10-10 04:02:00 | NOAA-20 | PIRENÓPOLIS | GOIÁS | Brasil | 5217302 | 52 | 33 | nan | nan | nan | Cerrado | 1.1 |
| 9d91d84b-63e0-365e-932e-f5224c42e7e5 | -17.20875 | -47.65301 | 2025-10-10 04:02:00 | NOAA-20 | IPAMERI | GOIÁS | Brasil | 5210109 | 52 | 33 | nan | nan | nan | Cerrado | 4.0 |
| a28174bd-938b-30f7-86d9-543a04063477 | -11.63973 | -47.53865 | 2025-10-10 04:02:00 | NOAA-20 | NATIVIDADE | TOCANTINS | Brasil | 1714203 | 17 | 33 | nan | nan | nan | Cerrado | 1.9 |
| 94fac9ea-b820-341c-813b-045e10588489 | -14.91605 | -42.21543 | 2025-10-10 04:02:00 | NOAA-20 | CONDEÚBA | BAHIA | Brasil | 2908705 | 29 | 33 | nan | nan | nan | Caatinga | 0.4 |
| 0f5b93b5-4274-31fd-9c38-bd1683c6bfaa | -15.52538 | -47.96891 | 2025-10-10 04:02:00 | NOAA-20 | BRASÍLIA | DISTRITO FEDERAL | Brasil | 5300108 | 53 | 33 | nan | nan | nan | Cerrado | 1.1 |
| e45e1370-60d0-3bef-b1fc-ded44718c73a | -12.63025 | -45.06229 | 2025-10-10 04:02:00 | NOAA-20 | SÃO DESIDÉRIO | BAHIA | Brasil | 2928901 | 29 | 33 | nan | nan | nan | Cerrado | 8.1 |
| 6d76a7cb-6343-366a-bf50-2c77de3e845b | -17.4815 | -46.95291 | 2025-10-10 04:02:00 | NOAA-20 | PARACATU | MINAS GERAIS | Brasil | 3147006 | 31 | 33 | nan | nan | nan | Cerrado | 1.3 |
| 9dd39a07-caae-34fc-8001-afec3f0b0627 | -12.62651 | -45.06165 | 2025-10-10 04:02:00 | NOAA-20 | SÃO DESIDÉRIO | BAHIA | Brasil | 2928901 | 29 | 33 | nan | nan | nan | Cerrado | 8.1 |
| 0f402b0c-1be9-3421-b041-4ff5e480a255 | -17.37516 | -46.673 | 2025-10-10 04:02:00 | NOAA-20 | PARACATU | MINAS GERAIS | Brasil | 3147006 | 31 | 33 | nan | nan | nan | Cerrado | 2.5 |
| 2c4bc4ef-ff75-3c58-a3d7-60b3c20f69bd | -13.32369 | -47.74101 | 2025-10-10 04:02:00 | NOAA-20 | PARANÃ | TOCANTINS | Brasil | 1716208 | 17 | 33 | nan | nan | nan | Cerrado | 4.8 |
| 0b80bb68-06a8-38e6-b86a-3f18ba1186f1 | -15.62036 | -45.25151 | 2025-10-10 04:02:00 | NOAA-20 | CHAPADA GAÚCHA | MINAS GERAIS | Brasil | 3116159 | 31 | 33 | nan | nan | nan | Cerrado | 1.2 |
| 8760c102-298b-3200-9e00-9e2c6f6ae893 | -16.17428 | -42.86382 | 2025-10-10 04:02:00 | NOAA-20 | GRÃO MOGOL | MINAS GERAIS | Brasil | 3127800 | 31 | 33 | nan | nan | nan | Cerrado | 1.5 |
| b4bce193-ea46-3505-8094-a9935b7812c0 | -11.63418 | -44.30534 | 2025-10-10 04:02:00 | NOAA-20 | COTEGIPE | BAHIA | Brasil | 2909406 | 29 | 33 | nan | nan | nan | Cerrado | 1.2 |
| 7711e7a9-b21f-3212-b537-c6cec7dcf655 | -13.34939 | -47.63027 | 2025-10-10 04:02:00 | NOAA-20 | CAVALCANTE | GOIÁS | Brasil | 5205307 | 52 | 33 | nan | nan | nan | Cerrado | 1.9 |
| 633db810-d0e1-3ba1-beaa-f514f54e8554 | -15.28599 | -46.14866 | 2025-10-10 04:02:00 | NOAA-20 | FORMOSO | MINAS GERAIS | Brasil | 3126208 | 31 | 33 | nan | nan | nan | Cerrado | 1.5 |
| 2944702e-5ddd-32af-8a24-c15e8f898f21 | -12.63796 | -45.03998 | 2025-10-10 04:02:00 | NOAA-20 | SÃO DESIDÉRIO | BAHIA | Brasil | 2928901 | 29 | 33 | nan | nan | nan | Cerrado | 3.6 |
| 2328477e-9c1f-33ec-abe7-3e8d7b8187b4 | -13.83662 | -45.88132 | 2025-10-10 04:02:00 | NOAA-20 | CORRENTINA | BAHIA | Brasil | 2909307 | 29 | 33 | nan | nan | nan | Cerrado | 0.7 |
| aa981dbf-3fc8-3046-ac84-5059739b6c1d | -17.93016 | -45.0217 | 2025-10-10 04:02:00 | NOAA-20 | LASSANCE | MINAS GERAIS | Brasil | 3138104 | 31 | 33 | nan | nan | nan | Cerrado | 28.0 |
| 6228564d-0abd-37f1-aa9a-75b3d9cd5dea | -16.27806 | -47.1773 | 2025-10-10 04:02:00 | NOAA-20 | UNAÍ | MINAS GERAIS | Brasil | 3170404 | 31 | 33 | nan | nan | nan | Cerrado | 1.1 |
| d9d9ee4f-1caf-3c3f-bc27-dde163abdc74 | -11.86131 | -44.91956 | 2025-10-10 04:02:00 | NOAA-20 | RIACHÃO DAS NEVES | BAHIA | Brasil | 2926202 | 29 | 33 | nan | nan | nan | Cerrado | 0.8 |
| 152b45de-81f7-39d8-809a-0ca87b09702f | -11.63533 | -47.53769 | 2025-10-10 04:02:00 | NOAA-20 | NATIVIDADE | TOCANTINS | Brasil | 1714203 | 17 | 33 | nan | nan | nan | Cerrado | 4.4 |
| e0e64bbf-723e-3720-bf9f-f310bbab02fa | -11.96697 | -45.21088 | 2025-10-10 04:02:00 | NOAA-20 | BARREIRAS | BAHIA | Brasil | 2903201 | 29 | 33 | nan | nan | nan | Cerrado | 6.5 |
| 8a5ce34a-d6f2-312e-b016-27c00fdb77ed | -15.24535 | -46.37655 | 2025-10-10 04:02:00 | NOAA-20 | FORMOSO | MINAS GERAIS | Brasil | 3126208 | 31 | 33 | nan | nan | nan | Cerrado | 2.5 |
| b7c80414-a4a2-34d8-9023-d2dc55dfd4a8 | -15.61952 | -45.25274 | 2025-10-10 04:02:00 | NOAA-20 | CHAPADA GAÚCHA | MINAS GERAIS | Brasil | 3116159 | 31 | 33 | nan | nan | nan | Cerrado | 0.6 |
| 36eeee18-3826-3b22-a95a-381d41fff0c1 | -17.93295 | -45.0265 | 2025-10-10 04:02:00 | NOAA-20 | LASSANCE | MINAS GERAIS | Brasil | 3138104 | 31 | 33 | nan | nan | nan | Cerrado | 14.1 |
| 099c7c76-5785-367d-80f9-a324570af47a | -14.93133 | -46.7743 | 2025-10-10 04:02:00 | NOAA-20 | FLORES DE GOIÁS | GOIÁS | Brasil | 5207907 | 52 | 33 | nan | nan | nan | Cerrado | 5.7 |
| a9095d32-8ec6-3da4-9cc2-2a9468d125b3 | -16.26812 | -47.16395 | 2025-10-10 04:02:00 | NOAA-20 | UNAÍ | MINAS GERAIS | Brasil | 3170404 | 31 | 33 | nan | nan | nan | Cerrado | 1.4 |
| 6022489e-8937-3443-bed2-2b9bb67b1985 | -16.11977 | -47.91113 | 2025-10-10 04:02:00 | NOAA-20 | CIDADE OCIDENTAL | GOIÁS | Brasil | 5205497 | 52 | 33 | nan | nan | nan | Cerrado | 1.2 |
| 46628e5b-f6e6-3c6a-876a-772affcd1015 | -10.8185 | -42.82396 | 2025-10-10 04:02:00 | NOAA-20 | XIQUE-XIQUE | BAHIA | Brasil | 2933604 | 29 | 33 | nan | nan | nan | Cerrado | 7.1 |
| 8b442d9e-1cc8-3020-8dc4-2b890484cc40 | -17.65404 | -47.25087 | 2025-10-10 04:02:00 | NOAA-20 | GUARDA-MOR | MINAS GERAIS | Brasil | 3128600 | 31 | 33 | nan | nan | nan | Cerrado | 2.9 |
| 9f7a4251-e270-3c95-bcd0-a02c46e391e8 | -13.38579 | -44.2374 | 2025-10-10 04:02:00 | NOAA-20 | SANTA MARIA DA VITÓRIA | BAHIA | Brasil | 2928109 | 29 | 33 | nan | nan | nan | Cerrado | 1.7 |
| 6810ce21-3aca-32ed-9b38-e8144d6147a8 | -17.9925 | -44.97789 | 2025-10-10 04:02:00 | NOAA-20 | LASSANCE | MINAS GERAIS | Brasil | 3138104 | 31 | 33 | nan | nan | nan | Cerrado | 2.3 |
| 4937e563-7fe1-3d28-b4b6-83fddd7eb7d4 | -11.78971 | -45.04486 | 2025-10-10 04:02:00 | NOAA-20 | RIACHÃO DAS NEVES | BAHIA | Brasil | 2926202 | 29 | 33 | nan | nan | nan | Cerrado | 1.9 |
| d0cb7c14-41ad-33f4-9f11-49177fbfcd8c | -17.94435 | -45.02764 | 2025-10-10 04:02:00 | NOAA-20 | LASSANCE | MINAS GERAIS | Brasil | 3138104 | 31 | 33 | nan | nan | nan | Cerrado | 4.3 |
| d259f1f7-7856-3c10-9e96-3243454ac944 | -14.54627 | -47.00377 | 2025-10-10 04:02:00 | NOAA-20 | FLORES DE GOIÁS | GOIÁS | Brasil | 5207907 | 52 | 33 | nan | nan | nan | Cerrado | 0.9 |
| ea397b07-1609-3712-98b2-c25ff61d8f58 | -13.35879 | -47.74907 | 2025-10-10 04:02:00 | NOAA-20 | PARANÃ | TOCANTINS | Brasil | 1716208 | 17 | 33 | nan | nan | nan | Cerrado | 3.7 |
| e0097dbd-7e00-306f-a829-de97bae77d5b | -16.74284 | -43.97606 | 2025-10-10 04:02:00 | NOAA-20 | MONTES CLAROS | MINAS GERAIS | Brasil | 3143302 | 31 | 33 | nan | nan | nan | Cerrado | 1.8 |
| 9ee65607-cf04-323f-9706-d38f84294f57 | -17.24351 | -44.11091 | 2025-10-10 04:02:00 | NOAA-20 | ENGENHEIRO NAVARRO | MINAS GERAIS | Brasil | 3123809 | 31 | 33 | nan | nan | nan | Cerrado | 0.6 |
| b27cb1bf-545e-3674-80cd-9fee34f0a5e2 | -10.61333 | -46.62927 | 2025-10-10 04:02:00 | NOAA-20 | MATEIROS | TOCANTINS | Brasil | 1712702 | 17 | 33 | nan | nan | nan | Cerrado | 2.6 |
| 99d2101b-309c-3de5-9842-8d7aedcdaf96 | -11.53336 | -47.10065 | 2025-10-10 04:02:00 | NOAA-20 | ALMAS | TOCANTINS | Brasil | 1700400 | 17 | 33 | nan | nan | nan | Cerrado | 2.0 |
| 7c68321e-d3b0-349d-8b56-5ab1708ef6c2 | -12.01392 | -47.79248 | 2025-10-10 04:02:00 | NOAA-20 | NATIVIDADE | TOCANTINS | Brasil | 1714203 | 17 | 33 | nan | nan | nan | Cerrado | 0.8 |
| 7cd8ec45-d021-3feb-9b3a-93bea90b572c | -13.32286 | -47.99302 | 2025-10-10 04:02:00 | NOAA-20 | CAVALCANTE | GOIÁS | Brasil | 5205307 | 52 | 33 | nan | nan | nan | Cerrado | 1.1 |
| 6f46c03d-9a4b-38cc-afa6-002a34e3602b | -17.0857 | -45.48203 | 2025-10-10 04:02:00 | NOAA-20 | BURITIZEIRO | MINAS GERAIS | Brasil | 3109402 | 31 | 33 | nan | nan | nan | Cerrado | 3.9 |
| 0820cb09-d1b1-3577-9c67-6ae47fcd65cc | -18.0697 | -44.99589 | 2025-10-10 04:02:00 | NOAA-20 | TRÊS MARIAS | MINAS GERAIS | Brasil | 3169356 | 31 | 33 | nan | nan | nan | Cerrado | 2.1 |
| 81a4cb82-0b53-39a6-80a6-f1638de34b8d | -19.84044 | -41.80967 | 2025-10-10 04:04:00 | NOAA-20 | IPANEMA | MINAS GERAIS | Brasil | 3131208 | 31 | 33 | nan | nan | nan | Mata Atlântica | 1.2 |
| 99b09146-7825-3323-8b98-046f0f08f93b | -19.42098 | -44.84347 | 2025-10-10 04:04:00 | NOAA-20 | POMPÉU | MINAS GERAIS | Brasil | 3152006 | 31 | 33 | nan | nan | nan | Cerrado | 1.8 |
| cb9661f4-4e68-3a24-a08a-c1af5f59ab49 | -20.22423 | -46.4253 | 2025-10-10 04:04:00 | NOAA-20 | SÃO ROQUE DE MINAS | MINAS GERAIS | Brasil | 3164308 | 31 | 33 | nan | nan | nan | Cerrado | 1.0 |
| 4b555062-75b2-3a68-8547-061f086fed21 | -18.78531 | -44.61341 | 2025-10-10 04:04:00 | NOAA-20 | CURVELO | MINAS GERAIS | Brasil | 3120904 | 31 | 33 | nan | nan | nan | Cerrado | 2.0 |
| 34e00bea-45ec-3184-b14b-0f216fd08f3e | -20.23067 | -46.43109 | 2025-10-10 04:04:00 | NOAA-20 | SÃO ROQUE DE MINAS | MINAS GERAIS | Brasil | 3164308 | 31 | 33 | nan | nan | nan | Cerrado | 2.8 |
| b185fcf0-2ccc-39ac-b502-f63e370147b4 | -18.86327 | -48.02356 | 2025-10-10 04:04:00 | NOAA-20 | ARAGUARI | MINAS GERAIS | Brasil | 3103504 | 31 | 33 | nan | nan | nan | Mata Atlântica | 0.6 |
| d09651b9-3cba-36f6-8085-61af896de867 | -19.01864 | -46.18374 | 2025-10-10 04:04:00 | NOAA-20 | CARMO DO PARANAÍBA | MINAS GERAIS | Brasil | 3114303 | 31 | 33 | nan | nan | nan | Cerrado | 1.0 |
| 02de0ae7-e122-3091-bbb1-67296761c737 | -20.22706 | -46.43038 | 2025-10-10 04:04:00 | NOAA-20 | SÃO ROQUE DE MINAS | MINAS GERAIS | Brasil | 3164308 | 31 | 33 | nan | nan | nan | Cerrado | 1.0 |
| 1b68279f-ca3d-30a8-a445-3269775be0a2 | -18.41537 | -45.24239 | 2025-10-10 04:04:00 | NOAA-20 | TRÊS MARIAS | MINAS GERAIS | Brasil | 3169356 | 31 | 33 | nan | nan | nan | Cerrado | 1.4 |
| f6faf1b5-c5fb-3b75-aef2-081af652d742 | -20.06224 | -48.25043 | 2025-10-10 04:04:00 | NOAA-20 | CONCEIÇÃO DAS ALAGOAS | MINAS GERAIS | Brasil | 3117306 | 31 | 33 | nan | nan | nan | Cerrado | 1.4 |
| 435569b0-3b2e-3f48-a95a-8683fdd47d29 | -18.74271 | -48.08408 | 2025-10-10 04:04:00 | NOAA-20 | ARAGUARI | MINAS GERAIS | Brasil | 3103504 | 31 | 33 | nan | nan | nan | Mata Atlântica | 1.8 |
| a705b064-1e70-39c4-95cf-7d127427a868 | -18.72799 | -44.34901 | 2025-10-10 04:04:00 | NOAA-20 | INIMUTABA | MINAS GERAIS | Brasil | 3131109 | 31 | 33 | nan | nan | nan | Cerrado | 0.4 |
| 66ffec18-a787-3541-897e-6e1b9e2d2bd7 | -20.06155 | -48.25414 | 2025-10-10 04:04:00 | NOAA-20 | CONCEIÇÃO DAS ALAGOAS | MINAS GERAIS | Brasil | 3117306 | 31 | 33 | nan | nan | nan | Cerrado | 1.8 |
| 14f4d5e8-1e7a-3190-bf59-e6171490f5a9 | -17.97106 | -48.56399 | 2025-10-10 04:04:00 | NOAA-20 | CALDAS NOVAS | GOIÁS | Brasil | 5204508 | 52 | 33 | nan | nan | nan | Cerrado | 1.4 |
| ebde46b5-8e7d-3d9a-afe1-e9269c788c65 | -18.74342 | -48.08034 | 2025-10-10 04:04:00 | NOAA-20 | ARAGUARI | MINAS GERAIS | Brasil | 3103504 | 31 | 33 | nan | nan | nan | Mata Atlântica | 1.8 |
| 1ebb17ba-9588-3a6e-960f-dab16e4b616e | -20.22783 | -46.42603 | 2025-10-10 04:04:00 | NOAA-20 | SÃO ROQUE DE MINAS | MINAS GERAIS | Brasil | 3164308 | 31 | 33 | nan | nan | nan | Cerrado | 1.0 |
| 7c13046e-2a96-34d6-b47f-d4ce82cf0f3f | -18.41467 | -45.24648 | 2025-10-10 04:04:00 | NOAA-20 | TRÊS MARIAS | MINAS GERAIS | Brasil | 3169356 | 31 | 33 | nan | nan | nan | Cerrado | 1.4 |
| 5fa889e6-ff1e-395d-985d-058d2cde13d8 | -17.9745 | -48.56895 | 2025-10-10 04:04:00 | NOAA-20 | CALDAS NOVAS | GOIÁS | Brasil | 5204508 | 52 | 33 | nan | nan | nan | Cerrado | 1.4 |
| 7a1df19f-7e99-3365-8720-676c1421c0b9 | -17.97758 | -48.55295 | 2025-10-10 04:04:00 | NOAA-20 | CALDAS NOVAS | GOIÁS | Brasil | 5204508 | 52 | 33 | nan | nan | nan | Cerrado | 0.9 |
| f5047399-3644-3f90-a0c9-e213ac5e831a | -17.7613 | -48.5663 | 2025-10-10 04:04:00 | NOAA-20 | CALDAS NOVAS | GOIÁS | Brasil | 5204508 | 52 | 33 | nan | nan | nan | Cerrado | 1.5 |
| ad3e1546-32f9-3908-9cdd-253dfd6d8bca | -19.63109 | -47.74356 | 2025-10-10 04:04:00 | NOAA-20 | UBERABA | MINAS GERAIS | Brasil | 3170107 | 31 | 33 | nan | nan | nan | Cerrado | 1.0 |
| 73d1de37-3f07-39a5-9254-93693a70bddd | -19.841 | -41.80597 | 2025-10-10 04:04:00 | NOAA-20 | IPANEMA | MINAS GERAIS | Brasil | 3131208 | 31 | 33 | nan | nan | nan | Mata Atlântica | 1.2 |
| 9baea607-cbaa-3524-848f-ade83f86542d | -18.77716 | -44.61991 | 2025-10-10 04:04:00 | NOAA-20 | CURVELO | MINAS GERAIS | Brasil | 3120904 | 31 | 33 | nan | nan | nan | Cerrado | 0.9 |
| cfa0bf2f-a6b4-3aa3-86ac-bd1a5760e154 | -19.63029 | -47.74507 | 2025-10-10 04:04:00 | NOAA-20 | UBERABA | MINAS GERAIS | Brasil | 3170107 | 31 | 33 | nan | nan | nan | Cerrado | 1.0 |
| 84204413-d143-369d-a601-33f059b3bb4b | -18.41887 | -45.24308 | 2025-10-10 04:04:00 | NOAA-20 | TRÊS MARIAS | MINAS GERAIS | Brasil | 3169356 | 31 | 33 | nan | nan | nan | Cerrado | 1.7 |
| cc8dde00-0ad0-32f3-be7a-556f73cbff81 | -17.97024 | -48.56827 | 2025-10-10 04:04:00 | NOAA-20 | CALDAS NOVAS | GOIÁS | Brasil | 5204508 | 52 | 33 | nan | nan | nan | Cerrado | 1.4 |
| 74267780-d593-37c2-89f2-4dbfa746dd7d | -19.10252 | -43.88309 | 2025-10-10 04:04:00 | NOAA-20 | SANTANA DE PIRAPAMA | MINAS GERAIS | Brasil | 3158508 | 31 | 33 | nan | nan | nan | Cerrado | 1.4 |
| 4b6b8aa3-74a0-3c05-8859-5c041249f716 | -18.78124 | -44.61666 | 2025-10-10 04:04:00 | NOAA-20 | CURVELO | MINAS GERAIS | Brasil | 3120904 | 31 | 33 | nan | nan | nan | Cerrado | 4.2 |
| 92d63232-09eb-3279-bcb4-aadb3bbe12de | -19.8371 | -41.80905 | 2025-10-10 04:04:00 | NOAA-20 | IPANEMA | MINAS GERAIS | Brasil | 3131208 | 31 | 33 | nan | nan | nan | Mata Atlântica | 1.2 |
| dce5cf81-89eb-32aa-b558-95c8b55813b6 | -19.09918 | -43.88248 | 2025-10-10 04:04:00 | NOAA-20 | SANTANA DE PIRAPAMA | MINAS GERAIS | Brasil | 3158508 | 31 | 33 | nan | nan | nan | Cerrado | 3.2 |
| 369d20ca-2c30-3ad5-989a-3b805981fa49 | -20.23144 | -46.42675 | 2025-10-10 04:04:00 | NOAA-20 | SÃO ROQUE DE MINAS | MINAS GERAIS | Brasil | 3164308 | 31 | 33 | nan | nan | nan | Cerrado | 2.8 |
| 6cea3aff-17d8-3339-862d-01734c70a323 | -18.86254 | -48.02745 | 2025-10-10 04:04:00 | NOAA-20 | ARAGUARI | MINAS GERAIS | Brasil | 3103504 | 31 | 33 | nan | nan | nan | Mata Atlântica | 0.9 |
| a6e521a2-673f-343b-9d56-ff80a303dd05 | -18.77782 | -44.61602 | 2025-10-10 04:04:00 | NOAA-20 | CURVELO | MINAS GERAIS | Brasil | 3120904 | 31 | 33 | nan | nan | nan | Cerrado | 0.9 |
| 758b2023-01e3-3829-8050-07a4ce411218 | -17.97681 | -48.55692 | 2025-10-10 04:04:00 | NOAA-20 | CALDAS NOVAS | GOIÁS | Brasil | 5204508 | 52 | 33 | nan | nan | nan | Cerrado | 1.2 |
| 64662f9b-9772-3070-84d3-97960450a997 | -18.41957 | -45.23898 | 2025-10-10 04:04:00 | NOAA-20 | TRÊS MARIAS | MINAS GERAIS | Brasil | 3169356 | 31 | 33 | nan | nan | nan | Cerrado | 2.1 |
| e2381afd-7ec0-3dd3-b597-f8bf7db854e5 | -17.9376 | -45.0148 | 2025-10-10 04:10:00 | GOES-19 | LASSANCE | MINAS GERAIS | Brasil | 3138104 | 31 | 33 | nan | nan | nan | Cerrado | 112.4 |
| d910b8b2-823a-323d-a5c9-8d5f4ce3382a | -12.6488 | -45.0486 | 2025-10-10 04:10:00 | GOES-19 | SÃO DESIDÉRIO | BAHIA | Brasil | 2928901 | 29 | 33 | nan | nan | nan | Cerrado | 89.8 |
| 4b39223b-67b4-3418-abf2-8e7a3887f945 | -17.8828 | -57.5177 | 2025-10-10 04:10:00 | GOES-19 | CORUMBÁ | MATO GROSSO DO SUL | Brasil | 5003207 | 50 | 33 | nan | nan | nan | Pantanal | 50.9 |
| fb3a4d30-20fa-36ea-84a2-8485491a95b0 | -12.6294 | -45.0517 | 2025-10-10 04:10:00 | GOES-19 | SÃO DESIDÉRIO | BAHIA | Brasil | 2928901 | 29 | 33 | nan | nan | nan | Cerrado | 126.5 |
| 9b8013ed-114b-3c1f-bb1e-b0180197dbd6 | -10.1517 | -44.5984 | 2025-10-10 04:10:00 | GOES-19 | PARNAGUÁ | PIAUÍ | Brasil | 2207603 | 22 | 33 | nan | nan | nan | Cerrado | 42.6 |
| 19b1ed27-5992-3031-8290-1aa2f3dff84d | -12.629 | -45.0749 | 2025-10-10 04:10:00 | GOES-19 | SÃO DESIDÉRIO | BAHIA | Brasil | 2928901 | 29 | 33 | nan | nan | nan | Cerrado | 94.7 |
| 2bb98b46-7ac4-34ab-8d23-63e35f08a22a | -17.8832 | -57.4971 | 2025-10-10 04:10:00 | GOES-19 | CORUMBÁ | MATO GROSSO DO SUL | Brasil | 5003207 | 50 | 33 | nan | nan | nan | Pantanal | 50.0 |
| 90c7eb6d-514f-372d-bf52-34cddbdee5dd | -12.6299 | -45.0284 | 2025-10-10 04:20:00 | GOES-19 | SÃO DESIDÉRIO | BAHIA | Brasil | 2928901 | 29 | 33 | nan | nan | nan | Cerrado | 85.5 |
| 0439245a-f2c0-3391-b2ac-d50eadd9f134 | -12.6294 | -45.0517 | 2025-10-10 04:20:00 | GOES-19 | SÃO DESIDÉRIO | BAHIA | Brasil | 2928901 | 29 | 33 | nan | nan | nan | Cerrado | 340.0 |


[Clique aqui para ver as próximas entradas](README33.md)
