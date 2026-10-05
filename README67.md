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

## Dados Diários - Página 67

| ID | Latitude | Longitude | Data/Hora GMT | Satélite | Município | Estado | País | Município ID | Estado ID | País ID | Dias sem Chuva | Precipitação | Risco de Fogo | Bioma | FRP |
|----|----------|-----------|---------------|----------|-----------|--------|------|--------------|-----------|---------|----------------|--------------|----------------|-------|-----|
| a9f2fb9b-cfb7-393f-889d-0e4302b75c89 | -9.1349 | -65.564 | 2026-10-05 15:30:00 | GOES-19 | LÁBREA | AMAZONAS | Brasil | 1302405 | 13 | 33 | nan | nan | nan | Amazônia | 48.1 |
| ebd7f8f5-92f0-387c-97b0-e4c5fe177305 | -9.8061 | -64.9979 | 2026-10-05 15:30:00 | GOES-19 | PORTO VELHO | RONDÔNIA | Brasil | 1100205 | 11 | 33 | nan | nan | nan | Amazônia | 42.6 |
| 6511df3b-fed6-341c-910f-717a1bc7b278 | -9.1333 | -65.9186 | 2026-10-05 15:30:00 | GOES-19 | LÁBREA | AMAZONAS | Brasil | 1302405 | 13 | 33 | nan | nan | nan | Amazônia | 45.0 |
| f92210c4-831e-3dec-bed8-4f25fb0fdd83 | -9.1905 | -65.5809 | 2026-10-05 15:30:00 | GOES-19 | LÁBREA | AMAZONAS | Brasil | 1302405 | 13 | 33 | nan | nan | nan | Amazônia | 44.8 |
| e86d0b51-b3d0-3307-9745-9ee167f7da37 | -8.593 | -66.8081 | 2026-10-05 15:30:00 | GOES-19 | LÁBREA | AMAZONAS | Brasil | 1302405 | 13 | 33 | nan | nan | nan | Amazônia | 68.8 |
| 89e0d5ba-603a-32b0-827b-86d134d1d93d | -9.1445 | -67.7577 | 2026-10-05 15:30:00 | GOES-19 | BOCA DO ACRE | AMAZONAS | Brasil | 1300706 | 13 | 33 | nan | nan | nan | Amazônia | 95.9 |
| d480f914-6154-39f9-84bf-fc5a93ad4eb9 | -9.1334 | -65.9 | 2026-10-05 15:30:00 | GOES-19 | LÁBREA | AMAZONAS | Brasil | 1302405 | 13 | 33 | nan | nan | nan | Amazônia | 87.0 |
| b70606e7-90ff-3e85-b75f-20496ada0fa5 | -9.7499 | -65.075 | 2026-10-05 15:30:00 | GOES-19 | PORTO VELHO | RONDÔNIA | Brasil | 1100205 | 11 | 33 | nan | nan | nan | Amazônia | 47.2 |
| 53b2c010-d484-35a1-903c-0201e90d7af1 | -14.67413 | -40.02566 | 2026-10-05 15:31:00 | NPP-375 | IGUAÍ | BAHIA | Brasil | 2913507 | 29 | 33 | nan | nan | nan | Mata Atlântica | 4.4 |
| 59444ff0-c191-3fd7-84f0-c5dd82b3131c | -15.79373 | -40.31648 | 2026-10-05 15:31:00 | NPP-375 | MAIQUINIQUE | BAHIA | Brasil | 2920007 | 29 | 33 | nan | nan | nan | Mata Atlântica | 15.1 |
| 76886a42-c65a-3f35-a356-4b6af2d1bc5c | -15.6927 | -39.7808 | 2026-10-05 15:31:00 | NPP-375 | POTIRAGUÁ | BAHIA | Brasil | 2925402 | 29 | 33 | nan | nan | nan | Mata Atlântica | 6.0 |
| c99f21ee-de51-3179-b4de-78f46af062c5 | -15.69332 | -39.78734 | 2026-10-05 15:31:00 | NPP-375 | POTIRAGUÁ | BAHIA | Brasil | 2925402 | 29 | 33 | nan | nan | nan | Mata Atlântica | 6.0 |
| bfdfc420-41cd-395c-b83d-133275dfc542 | -14.06993 | -40.6073 | 2026-10-05 15:31:00 | NPP-375 | MANOEL VITORINO | BAHIA | Brasil | 2920403 | 29 | 33 | nan | nan | nan | Caatinga | 3.4 |
| e479bd59-472d-369a-baf3-72db99d5fa13 | -14.06852 | -40.60885 | 2026-10-05 15:31:00 | NPP-375 | MANOEL VITORINO | BAHIA | Brasil | 2920403 | 29 | 33 | nan | nan | nan | Caatinga | 3.4 |
| 2e40efc2-da28-3b06-85ec-7f80b919e86e | -15.79594 | -40.31546 | 2026-10-05 15:31:00 | NPP-375 | MAIQUINIQUE | BAHIA | Brasil | 2920007 | 29 | 33 | nan | nan | nan | Mata Atlântica | 11.2 |
| 0bd6d254-834a-347f-a3a0-3bcca8b12d85 | -12.16206 | -39.91804 | 2026-10-05 15:33:00 | NPP-375 | IPIRÁ | BAHIA | Brasil | 2914000 | 29 | 33 | nan | nan | nan | Caatinga | 12.5 |
| c83b8aca-18bb-37c3-aa19-2548960586b3 | -8.00364 | -35.08813 | 2026-10-05 15:33:00 | NPP-375 | SÃO LOURENÇO DA MATA | PERNAMBUCO | Brasil | 2613701 | 26 | 33 | nan | nan | nan | Mata Atlântica | 23.1 |
| 059c1d47-7297-3774-8654-6d0005c34afc | -8.30787 | -39.14927 | 2026-10-05 15:33:00 | NPP-375 | CABROBÓ | PERNAMBUCO | Brasil | 2603009 | 26 | 33 | nan | nan | nan | Caatinga | 5.9 |
| 53300821-9ba5-3602-8cd2-d3494b292828 | -6.61406 | -37.89236 | 2026-10-05 15:33:00 | NPP-375 | LAGOA | PARAÍBA | Brasil | 2508109 | 25 | 33 | nan | nan | nan | Caatinga | 48.1 |
| 99a20a14-76a7-36a9-931a-1af4829e32c7 | -9.50061 | -37.443 | 2026-10-05 15:33:00 | NPP-375 | SÃO JOSÉ DA TAPERA | ALAGOAS | Brasil | 2708402 | 27 | 33 | nan | nan | nan | Caatinga | 2.7 |
| 81b64e43-b5f4-3a70-8def-56ca05ddfe24 | -8.37237 | -36.17335 | 2026-10-05 15:33:00 | NPP-375 | SÃO CAITANO | PERNAMBUCO | Brasil | 2613107 | 26 | 33 | nan | nan | nan | Caatinga | 4.9 |
| 5c5e5618-4d9f-34b8-95ce-46ed3910dd97 | -6.61737 | -41.56417 | 2026-10-05 15:33:00 | NPP-375 | INHUMA | PIAUÍ | Brasil | 2204709 | 22 | 33 | nan | nan | nan | Caatinga | 17.3 |
| 000dd020-f6a6-3254-98fe-8c0ab24310e3 | -6.60769 | -37.8872 | 2026-10-05 15:33:00 | NPP-375 | LAGOA | PARAÍBA | Brasil | 2508109 | 25 | 33 | nan | nan | nan | Caatinga | 28.9 |
| 8af544b1-260a-35d8-bbbb-cf2b2047ba41 | -7.51923 | -39.72933 | 2026-10-05 15:33:00 | NPP-375 | EXU | PERNAMBUCO | Brasil | 2605301 | 26 | 33 | nan | nan | nan | Caatinga | 9.5 |
| 3f47d350-e9de-38bd-b47e-9f6dd4dbb2e3 | -7.60351 | -37.54654 | 2026-10-05 15:33:00 | NPP-375 | TABIRA | PERNAMBUCO | Brasil | 2614600 | 26 | 33 | nan | nan | nan | Caatinga | 4.1 |
| e60e3f24-0b89-3ced-9dda-796b0ab209ab | -12.86208 | -39.93242 | 2026-10-05 15:33:00 | NPP-375 | IAÇU | BAHIA | Brasil | 2911907 | 29 | 33 | nan | nan | nan | Caatinga | 25.9 |
| 133bbce9-6e39-33c9-a355-d55d7e0d0404 | -6.15743 | -37.94407 | 2026-10-05 15:33:00 | NPP-375 | SERRINHA DOS PINTOS | RIO GRANDE DO NORTE | Brasil | 2413557 | 24 | 33 | nan | nan | nan | Caatinga | 2.2 |
| b006fd45-9ea5-3acb-824e-b8d72ca61068 | -9.60393 | -37.9417 | 2026-10-05 15:33:00 | NPP-375 | CANINDÉ DE SÃO FRANCISCO | SERGIPE | Brasil | 2801207 | 28 | 33 | nan | nan | nan | Caatinga | 3.4 |
| 19c1b943-282c-3d6a-8a35-0df7aa3310cb | -7.01193 | -37.24552 | 2026-10-05 15:33:00 | NPP-375 | PATOS | PARAÍBA | Brasil | 2510808 | 25 | 33 | nan | nan | nan | Caatinga | 7.4 |
| 269a8f16-93ec-3958-83d2-c6ad58a7ce82 | -8.00107 | -35.08492 | 2026-10-05 15:33:00 | NPP-375 | SÃO LOURENÇO DA MATA | PERNAMBUCO | Brasil | 2613701 | 26 | 33 | nan | nan | nan | Mata Atlântica | 16.7 |
| b84e8eff-7359-3346-9c23-081d8976ca7d | -6.61368 | -37.88956 | 2026-10-05 15:33:00 | NPP-375 | LAGOA | PARAÍBA | Brasil | 2508109 | 25 | 33 | nan | nan | nan | Caatinga | 48.1 |
| 48eba807-aaa4-38dc-a609-f809a18cdb7a | -12.86147 | -39.9267 | 2026-10-05 15:33:00 | NPP-375 | IAÇU | BAHIA | Brasil | 2911907 | 29 | 33 | nan | nan | nan | Caatinga | 74.2 |
| 405bed18-aaab-30aa-b098-d89575ba83fb | -6.79709 | -38.07312 | 2026-10-05 15:33:00 | NPP-375 | APARECIDA | PARAÍBA | Brasil | 2500775 | 25 | 33 | nan | nan | nan | Caatinga | 3.7 |
| 8cd18338-6e24-3422-8887-8e09016b1469 | -9.3792 | -41.14218 | 2026-10-05 15:33:00 | NPP-375 | CASA NOVA | BAHIA | Brasil | 2907202 | 29 | 33 | nan | nan | nan | Caatinga | 6.3 |
| ec696a03-d35a-3d82-b97e-f347cff5b8c0 | -13.20468 | -40.46116 | 2026-10-05 15:33:00 | NPP-375 | PLANALTINO | BAHIA | Brasil | 2924900 | 29 | 33 | nan | nan | nan | Caatinga | 4.8 |
| 2293dd91-0e0c-309f-a2d7-8caab693d9ac | -6.60724 | -37.88387 | 2026-10-05 15:33:00 | NPP-375 | LAGOA | PARAÍBA | Brasil | 2508109 | 25 | 33 | nan | nan | nan | Caatinga | 28.9 |
| d14a5a1d-47f0-3436-9f0f-42c24bbfe61e | -10.06089 | -39.61468 | 2026-10-05 15:33:00 | NPP-375 | UAUÁ | BAHIA | Brasil | 2932002 | 29 | 33 | nan | nan | nan | Caatinga | 7.3 |
| c35e9184-0849-390b-9a32-ace39ae5862d | -7.88438 | -40.20367 | 2026-10-05 15:33:00 | NPP-375 | OURICURI | PERNAMBUCO | Brasil | 2609907 | 26 | 33 | nan | nan | nan | Caatinga | 5.8 |
| 82c688b7-f473-334a-8e6d-1191baa439d6 | -8.3756 | -36.17125 | 2026-10-05 15:33:00 | NPP-375 | SÃO CAITANO | PERNAMBUCO | Brasil | 2613107 | 26 | 33 | nan | nan | nan | Caatinga | 3.1 |
| 2c5db255-a2b9-3b51-9952-a3277b6a168f | -6.32658 | -35.49863 | 2026-10-05 15:33:00 | NPP-375 | SANTO ANTÔNIO | RIO GRANDE DO NORTE | Brasil | 2411502 | 24 | 33 | nan | nan | nan | Caatinga | 2.5 |
| 7ff5ec0c-593e-3937-ae5d-0566cf357b42 | -8.30848 | -39.154 | 2026-10-05 15:33:00 | NPP-375 | CABROBÓ | PERNAMBUCO | Brasil | 2603009 | 26 | 33 | nan | nan | nan | Caatinga | 3.8 |
| 62388d26-197b-3199-81ae-8c6f7edbcff3 | -13.20795 | -40.46037 | 2026-10-05 15:33:00 | NPP-375 | PLANALTINO | BAHIA | Brasil | 2924900 | 29 | 33 | nan | nan | nan | Caatinga | 4.3 |
| a1a69ea8-e776-33a3-8464-7ee4c6f583d5 | -8.6855 | -36.75032 | 2026-10-05 15:33:00 | NPP-375 | VENTUROSA | PERNAMBUCO | Brasil | 2616001 | 26 | 33 | nan | nan | nan | Caatinga | 2.6 |
| 8572a23a-a0f3-3de6-b1a8-eeb98002e6ba | -6.22542 | -38.50664 | 2026-10-05 15:33:00 | NPP-375 | SÃO MIGUEL | RIO GRANDE DO NORTE | Brasil | 2412500 | 24 | 33 | nan | nan | nan | Caatinga | 5.4 |
| acb65251-e13d-3005-b4c4-e49ac223949e | -6.69554 | -41.00292 | 2026-10-05 15:33:00 | NPP-375 | PIO IX | PIAUÍ | Brasil | 2208205 | 22 | 33 | nan | nan | nan | Caatinga | 4.1 |
| b48bbb69-2533-365c-a12e-cf84f3b9b659 | -6.60809 | -37.89017 | 2026-10-05 15:33:00 | NPP-375 | LAGOA | PARAÍBA | Brasil | 2508109 | 25 | 33 | nan | nan | nan | Caatinga | 48.1 |
| 9137cb7c-160e-32e4-b4a2-6f1346e1fa46 | -8.43266 | -39.54266 | 2026-10-05 15:33:00 | NPP-375 | CABROBÓ | PERNAMBUCO | Brasil | 2603009 | 26 | 33 | nan | nan | nan | Caatinga | 11.1 |
| b5a97b5b-4548-3e2d-aa3b-49e2f9e93b88 | -6.65581 | -36.63913 | 2026-10-05 15:33:00 | NPP-375 | PARELHAS | RIO GRANDE DO NORTE | Brasil | 2408904 | 24 | 33 | nan | nan | nan | Caatinga | 3.3 |
| 14bb5f88-23ab-3677-8bd9-c53aac8d9805 | -8.82314 | -37.86291 | 2026-10-05 15:33:00 | NPP-375 | INAJÁ | PERNAMBUCO | Brasil | 2607000 | 26 | 33 | nan | nan | nan | Caatinga | 4.5 |
| f959afcf-6c5e-3ec7-a39d-db9dec989e63 | -6.80886 | -39.29593 | 2026-10-05 15:33:00 | NPP-375 | VÁRZEA ALEGRE | CEARÁ | Brasil | 2314003 | 23 | 33 | nan | nan | nan | Caatinga | 15.3 |
| 0094dcb6-e973-36ef-8ab9-37c1428a49f2 | -11.33137 | -39.71034 | 2026-10-05 15:33:00 | NPP-375 | SANTALUZ | BAHIA | Brasil | 2928000 | 29 | 33 | nan | nan | nan | Caatinga | 4.1 |
| a21ee94b-1c4a-3c1e-b82a-40022303012c | -9.19491 | -36.05899 | 2026-10-05 15:33:00 | NPP-375 | UNIÃO DOS PALMARES | ALAGOAS | Brasil | 2709301 | 27 | 33 | nan | nan | nan | Mata Atlântica | 2.8 |
| 3939f0da-8f7e-3db0-b877-9470ec946ad0 | -6.85301 | -35.0112 | 2026-10-05 15:33:00 | NPP-375 | RIO TINTO | PARAÍBA | Brasil | 2512903 | 25 | 33 | nan | nan | nan | Mata Atlântica | 8.4 |
| c1fd3fc5-2fa6-3533-8cbb-401657ade534 | -6.60848 | -37.89305 | 2026-10-05 15:33:00 | NPP-375 | LAGOA | PARAÍBA | Brasil | 2508109 | 25 | 33 | nan | nan | nan | Caatinga | 48.1 |
| 52459c48-3425-3909-bd5f-f1835405f8ea | -6.80215 | -39.29226 | 2026-10-05 15:33:00 | NPP-375 | VÁRZEA ALEGRE | CEARÁ | Brasil | 2314003 | 23 | 33 | nan | nan | nan | Caatinga | 8.7 |
| 127d66bc-b1bb-3177-9252-6f73d4c5cd12 | -12.70245 | -40.53962 | 2026-10-05 15:33:00 | NPP-375 | BOA VISTA DO TUPIM | BAHIA | Brasil | 2903805 | 29 | 33 | nan | nan | nan | Caatinga | 5.4 |
| ce1c92bb-97c5-3b53-8024-d4fe25c1b3ec | -6.8095 | -39.30073 | 2026-10-05 15:33:00 | NPP-375 | VÁRZEA ALEGRE | CEARÁ | Brasil | 2314003 | 23 | 33 | nan | nan | nan | Caatinga | 7.5 |
| 0079de27-5b30-3152-bd0b-827962d5d765 | -6.92128 | -38.33349 | 2026-10-05 15:33:00 | NPP-375 | NAZAREZINHO | PARAÍBA | Brasil | 2510006 | 25 | 33 | nan | nan | nan | Caatinga | 3.4 |
| 14f2ba23-78b0-3951-ada0-b5da0453ea03 | -6.85367 | -35.01589 | 2026-10-05 15:33:00 | NPP-375 | RIO TINTO | PARAÍBA | Brasil | 2512903 | 25 | 33 | nan | nan | nan | Mata Atlântica | 4.7 |
| 7f5f0ef8-d441-329a-9996-acd7c0096dd7 | -7.00945 | -37.24477 | 2026-10-05 15:33:00 | NPP-375 | PATOS | PARAÍBA | Brasil | 2510808 | 25 | 33 | nan | nan | nan | Caatinga | 11.4 |
| 06f2ce39-c569-3cbf-b5d7-5cf167bf19a3 | -10.40063 | -40.51016 | 2026-10-05 15:33:00 | NPP-375 | CAMPO FORMOSO | BAHIA | Brasil | 2906006 | 29 | 33 | nan | nan | nan | Caatinga | 7.2 |
| 218d1480-5f07-38c2-a614-512ab9040071 | -6.80277 | -39.29692 | 2026-10-05 15:33:00 | NPP-375 | VÁRZEA ALEGRE | CEARÁ | Brasil | 2314003 | 23 | 33 | nan | nan | nan | Caatinga | 8.7 |
| 0afd6318-d7dd-316a-bd7e-3ab593231ce5 | -12.69825 | -40.54275 | 2026-10-05 15:33:00 | NPP-375 | BOA VISTA DO TUPIM | BAHIA | Brasil | 2903805 | 29 | 33 | nan | nan | nan | Caatinga | 15.9 |
| 323c62f8-4f23-3726-b1ea-e2601b87e656 | -6.13397 | -36.72282 | 2026-10-05 15:33:00 | NPP-375 | TENENTE LAURENTINO CRUZ | RIO GRANDE DO NORTE | Brasil | 2414159 | 24 | 33 | nan | nan | nan | Caatinga | 2.5 |
| e756dde7-c8bc-3e9d-94ca-952cc27a61a6 | -13.3277 | -39.07555 | 2026-10-05 15:33:00 | NPP-375 | VALENÇA | BAHIA | Brasil | 2932903 | 29 | 33 | nan | nan | nan | Mata Atlântica | 8.1 |
| fcf7f0f5-5ffd-3daf-b7aa-5acb12d39868 | -7.56654 | -35.45486 | 2026-10-05 15:33:00 | NPP-375 | SÃO VICENTE FÉRRER | PERNAMBUCO | Brasil | 2613800 | 26 | 33 | nan | nan | nan | Mata Atlântica | 5.3 |
| 722d4479-3f67-35e1-add6-8546bb788857 | -6.53908 | -39.50823 | 2026-10-05 15:33:00 | NPP-375 | CARIÚS | CEARÁ | Brasil | 2303303 | 23 | 33 | nan | nan | nan | Caatinga | 11.5 |
| cb2df6fe-de65-317b-bd1c-afb4bac636ea | -6.6089 | -37.8961 | 2026-10-05 15:33:00 | NPP-375 | LAGOA | PARAÍBA | Brasil | 2508109 | 25 | 33 | nan | nan | nan | Caatinga | 24.2 |
| 9ad42cdd-5821-3d80-babc-9533d388b36d | -6.61562 | -41.5693 | 2026-10-05 15:33:00 | NPP-375 | INHUMA | PIAUÍ | Brasil | 2204709 | 22 | 33 | nan | nan | nan | Caatinga | 13.0 |
| fe741407-5fb7-3e56-9daf-5d4bc2bc4a15 | -12.71999 | -40.23293 | 2026-10-05 15:33:00 | NPP-375 | ITABERABA | BAHIA | Brasil | 2914703 | 29 | 33 | nan | nan | nan | Caatinga | 3.6 |
| f6b87002-dba9-36c8-84dd-760e5a64c840 | -9.15662 | -41.4124 | 2026-10-05 15:33:00 | NPP-375 | CASA NOVA | BAHIA | Brasil | 2907202 | 29 | 33 | nan | nan | nan | Caatinga | 5.4 |
| b3cb5bbb-022a-3370-b5d5-36d013dba2f1 | -13.26969 | -40.36479 | 2026-10-05 15:33:00 | NPP-375 | PLANALTINO | BAHIA | Brasil | 2924900 | 29 | 33 | nan | nan | nan | Caatinga | 6.7 |
| 8ff34e76-73f0-33c8-a362-e70b2306e060 | -8.82363 | -37.8668 | 2026-10-05 15:33:00 | NPP-375 | INAJÁ | PERNAMBUCO | Brasil | 2607000 | 26 | 33 | nan | nan | nan | Caatinga | 3.8 |
| d6e48628-07d7-3e50-ac7e-0ce341ff4206 | -12.86034 | -39.92511 | 2026-10-05 15:33:00 | NPP-375 | IAÇU | BAHIA | Brasil | 2911907 | 29 | 33 | nan | nan | nan | Caatinga | 19.4 |
| 5a22fa9d-dcdc-35b9-ab56-0fe189bda666 | -13.51299 | -40.7716 | 2026-10-05 15:33:00 | NPP-375 | IRAMAIA | BAHIA | Brasil | 2914307 | 29 | 33 | nan | nan | nan | Caatinga | 9.4 |
| 8076522d-faa4-382b-b361-03c4819f9fbe | -6.53845 | -39.50359 | 2026-10-05 15:33:00 | NPP-375 | CARIÚS | CEARÁ | Brasil | 2303303 | 23 | 33 | nan | nan | nan | Caatinga | 11.5 |
| 6088c96f-f1a5-316b-97d5-e6c5c371d595 | -8.22129 | -36.30272 | 2026-10-05 15:33:00 | NPP-375 | BELO JARDIM | PERNAMBUCO | Brasil | 2601706 | 26 | 33 | nan | nan | nan | Caatinga | 3.5 |
| a06f1bfc-0de7-3568-ac98-3c967bd845d9 | -12.86709 | -39.92347 | 2026-10-05 15:33:00 | NPP-375 | IAÇU | BAHIA | Brasil | 2911907 | 29 | 33 | nan | nan | nan | Caatinga | 19.4 |
| 5856e63b-43e7-368d-9228-6a6551aa107f | -6.69066 | -41.00188 | 2026-10-05 15:33:00 | NPP-375 | PIO IX | PIAUÍ | Brasil | 2208205 | 22 | 33 | nan | nan | nan | Caatinga | 7.2 |
| 07074684-1b54-3cfd-b65c-f3ff77255462 | -6.07685 | -35.69092 | 2026-10-05 15:33:00 | NPP-375 | SERRA CAIADA | RIO GRANDE DO NORTE | Brasil | 2410306 | 24 | 33 | nan | nan | nan | Caatinga | 3.5 |
| 38a66b2f-d02f-34b5-811e-23deeacd5980 | -8.3705 | -36.17183 | 2026-10-05 15:33:00 | NPP-375 | SÃO CAITANO | PERNAMBUCO | Brasil | 2613107 | 26 | 33 | nan | nan | nan | Caatinga | 3.1 |
| 896327e1-da4d-3a35-90b2-2340c05a75c4 | -6.61327 | -37.88657 | 2026-10-05 15:33:00 | NPP-375 | LAGOA | PARAÍBA | Brasil | 2508109 | 25 | 33 | nan | nan | nan | Caatinga | 28.9 |
| 4e8c2840-e36d-378a-9f94-5105e4597c5d | -13.32711 | -39.07014 | 2026-10-05 15:33:00 | NPP-375 | VALENÇA | BAHIA | Brasil | 2932903 | 29 | 33 | nan | nan | nan | Mata Atlântica | 8.1 |
| 2d5c2f23-436d-36bc-b0c4-7dd52025a318 | -10.06086 | -39.6148 | 2026-10-05 15:33:00 | NPP-375 | UAUÁ | BAHIA | Brasil | 2932002 | 29 | 33 | nan | nan | nan | Caatinga | 7.8 |
| 11954066-ac16-37fe-bdd4-8745bdde5f18 | -6.61827 | -41.57098 | 2026-10-05 15:33:00 | NPP-375 | INHUMA | PIAUÍ | Brasil | 2204709 | 22 | 33 | nan | nan | nan | Caatinga | 12.7 |
| de2136c9-f11e-354f-950a-2900295e2557 | -6.61882 | -37.88568 | 2026-10-05 15:33:00 | NPP-375 | LAGOA | PARAÍBA | Brasil | 2508109 | 25 | 33 | nan | nan | nan | Caatinga | 19.1 |
| e6801c27-336e-3a31-ab1a-68c7c1d8f3f4 | -9.37262 | -35.52291 | 2026-10-05 15:33:00 | NPP-375 | BARRA DE SANTO ANTÔNIO | ALAGOAS | Brasil | 2700508 | 27 | 33 | nan | nan | nan | Mata Atlântica | 8.1 |
| 542e51cd-4fa6-38ba-9b56-985b6740189d | -11.28367 | -38.19889 | 2026-10-05 15:33:00 | NPP-375 | ITAPICURU | BAHIA | Brasil | 2916500 | 29 | 33 | nan | nan | nan | Caatinga | 6.6 |
| 054f7115-b61a-38ae-8382-dd914a4ef36c | -9.15871 | -41.41032 | 2026-10-05 15:33:00 | NPP-375 | CASA NOVA | BAHIA | Brasil | 2907202 | 29 | 33 | nan | nan | nan | Caatinga | 6.4 |
| a9f4d446-29d6-3b8f-8329-9ba1d8a9612d | -8.52768 | -36.52228 | 2026-10-05 15:33:00 | NPP-375 | SÃO BENTO DO UNA | PERNAMBUCO | Brasil | 2613008 | 26 | 33 | nan | nan | nan | Caatinga | 3.7 |
| a36c0fbf-e4af-3c4c-af82-dd49fac0f520 | -11.28479 | -38.20235 | 2026-10-05 15:33:00 | NPP-375 | ITAPICURU | BAHIA | Brasil | 2916500 | 29 | 33 | nan | nan | nan | Caatinga | 7.3 |
| aa849502-da7c-3b5e-9e52-4f4e0d102c00 | -10.40038 | -40.51127 | 2026-10-05 15:33:00 | NPP-375 | CAMPO FORMOSO | BAHIA | Brasil | 2906006 | 29 | 33 | nan | nan | nan | Caatinga | 2.3 |
| f9ee6d6d-5ee2-37b4-94a3-dcf4af3cc8bd | -6.6128 | -37.88311 | 2026-10-05 15:33:00 | NPP-375 | LAGOA | PARAÍBA | Brasil | 2508109 | 25 | 33 | nan | nan | nan | Caatinga | 28.9 |
| 319d575d-794d-3192-8940-f325c423bc85 | -7.44651 | -37.46724 | 2026-10-05 15:33:00 | NPP-375 | SANTA TEREZINHA | PERNAMBUCO | Brasil | 2612802 | 26 | 33 | nan | nan | nan | Caatinga | 10.8 |
| 9aa880f5-0c4b-36dd-a093-ca84a4146401 | -12.69555 | -40.54227 | 2026-10-05 15:33:00 | NPP-375 | BOA VISTA DO TUPIM | BAHIA | Brasil | 2903805 | 29 | 33 | nan | nan | nan | Caatinga | 5.4 |
| 4d3c89c7-e92b-3755-8114-1f520252f937 | -12.861 | -39.93098 | 2026-10-05 15:33:00 | NPP-375 | IAÇU | BAHIA | Brasil | 2911907 | 29 | 33 | nan | nan | nan | Caatinga | 19.4 |
| a9809eec-7e35-3862-bd4a-d225170ed9db | -6.85737 | -38.68374 | 2026-10-05 15:33:00 | NPP-375 | IPAUMIRIM | CEARÁ | Brasil | 2305704 | 23 | 33 | nan | nan | nan | Caatinga | 14.0 |
| 9d0cdbc2-14d5-3c1f-9823-12328c25f2f1 | -12.86823 | -39.92503 | 2026-10-05 15:33:00 | NPP-375 | IAÇU | BAHIA | Brasil | 2911907 | 29 | 33 | nan | nan | nan | Caatinga | 10.3 |
| 4eefe050-83ae-34c8-aff4-adf346ec0a03 | -6.79918 | -38.07239 | 2026-10-05 15:33:00 | NPP-375 | APARECIDA | PARAÍBA | Brasil | 2500775 | 25 | 33 | nan | nan | nan | Caatinga | 2.1 |
| cfa86fef-7500-32cd-8cdf-20751d32aef7 | -6.84908 | -35.01659 | 2026-10-05 15:33:00 | NPP-375 | RIO TINTO | PARAÍBA | Brasil | 2512903 | 25 | 33 | nan | nan | nan | Mata Atlântica | 2.1 |


[Clique aqui para ver as próximas entradas](README68.md)
