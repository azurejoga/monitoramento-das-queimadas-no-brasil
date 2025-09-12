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

## Dados Diários - Página 56

| ID | Latitude | Longitude | Data/Hora GMT | Satélite | Município | Estado | País | Município ID | Estado ID | País ID | Dias sem Chuva | Precipitação | Risco de Fogo | Bioma | FRP |
|----|----------|-----------|---------------|----------|-----------|--------|------|--------------|-----------|---------|----------------|--------------|----------------|-------|-----|
| f5e23cda-fc73-3e34-bdf2-576a31d714e8 | -21.96515 | -47.5586 | 2025-09-12 04:08:00 | NPP-375D | DESCALVADO | SÃO PAULO | Brasil | 3513702 | 35 | 33 | nan | nan | nan | Cerrado | 2.6 |
| 8f85b9b4-7be8-3c03-ab47-5e36a4a4f82f | -19.24395 | -48.04136 | 2025-09-12 04:08:00 | NPP-375D | UBERABA | MINAS GERAIS | Brasil | 3170107 | 31 | 33 | nan | nan | nan | Cerrado | 13.3 |
| f52df8e5-6dfa-322d-a9bd-f9885fbf327f | -21.36839 | -45.16796 | 2025-09-12 04:08:00 | NPP-375D | CARMO DA CACHOEIRA | MINAS GERAIS | Brasil | 3113909 | 31 | 33 | nan | nan | nan | Mata Atlântica | 3.1 |
| cee08c38-cbe1-3bae-b8ab-7dbb3f946c0f | -20.14665 | -47.38146 | 2025-09-12 04:08:00 | NPP-375D | PEDREGULHO | SÃO PAULO | Brasil | 3537008 | 35 | 33 | nan | nan | nan | Cerrado | 2.1 |
| 5382e0f1-4799-3dd1-88cc-1df64282416b | -19.75213 | -46.08886 | 2025-09-12 04:08:00 | NPP-375D | CÓRREGO DANTA | MINAS GERAIS | Brasil | 3119807 | 31 | 33 | nan | nan | nan | Cerrado | 1.0 |
| 45cd76a8-174c-3486-8ebf-c191feb36312 | -18.44494 | -47.18536 | 2025-09-12 04:08:00 | NPP-375D | COROMANDEL | MINAS GERAIS | Brasil | 3119302 | 31 | 33 | nan | nan | nan | Cerrado | 2.3 |
| 0fb732f7-042b-35e5-bf54-497930c03fe2 | -18.5964 | -47.19194 | 2025-09-12 04:08:00 | NPP-375D | COROMANDEL | MINAS GERAIS | Brasil | 3119302 | 31 | 33 | nan | nan | nan | Cerrado | 3.7 |
| 8b20394a-a171-3213-8d1e-4f25909e9740 | -19.74401 | -45.94524 | 2025-09-12 04:08:00 | NPP-375D | CÓRREGO DANTA | MINAS GERAIS | Brasil | 3119807 | 31 | 33 | nan | nan | nan | Cerrado | 1.3 |
| 019eb001-1db9-38f3-9305-ebdb060697fa | -23.11529 | -47.4932 | 2025-09-12 04:08:00 | NPP-375D | PORTO FELIZ | SÃO PAULO | Brasil | 3540606 | 35 | 33 | nan | nan | nan | Mata Atlântica | 2.4 |
| fc941421-c076-385c-a5a6-2ef4576cd9a7 | -22.79671 | -47.80877 | 2025-09-12 04:08:00 | NPP-375D | PIRACICABA | SÃO PAULO | Brasil | 3538709 | 35 | 33 | nan | nan | nan | Cerrado | 2.5 |
| a96081e5-0326-33b8-b8ce-bf4ce765375e | -22.78462 | -47.8113 | 2025-09-12 04:08:00 | NPP-375D | PIRACICABA | SÃO PAULO | Brasil | 3538709 | 35 | 33 | nan | nan | nan | Cerrado | 1.2 |
| 03f537fb-c895-309a-924f-cd560ab1d4c9 | -22.78924 | -47.80726 | 2025-09-12 04:08:00 | NPP-375D | PIRACICABA | SÃO PAULO | Brasil | 3538709 | 35 | 33 | nan | nan | nan | Cerrado | 1.9 |
| cd4db485-b979-38ab-abc0-7aef14929ea9 | -18.31107 | -50.42525 | 2025-09-12 04:08:00 | NPP-375D | QUIRINÓPOLIS | GOIÁS | Brasil | 5218508 | 52 | 33 | nan | nan | nan | Cerrado | 15.1 |
| 795afdc5-8149-3230-8277-40382cc5d253 | -20.57306 | -43.7779 | 2025-09-12 04:08:00 | NPP-375D | CONSELHEIRO LAFAIETE | MINAS GERAIS | Brasil | 3118304 | 31 | 33 | nan | nan | nan | Mata Atlântica | 1.1 |
| d88b658a-7945-3148-a3be-0c60fc41152a | -19.66063 | -44.90148 | 2025-09-12 04:08:00 | NPP-375D | PITANGUI | MINAS GERAIS | Brasil | 3151404 | 31 | 33 | nan | nan | nan | Mata Atlântica | 0.9 |
| 0f5c65d1-e0a5-3aa6-bc0b-5d0b0fff15d9 | -18.45157 | -47.17077 | 2025-09-12 04:08:00 | NPP-375D | COROMANDEL | MINAS GERAIS | Brasil | 3119302 | 31 | 33 | nan | nan | nan | Cerrado | 2.5 |
| ab58e381-0f00-3727-97fe-7a618ad4cd55 | -24.16921 | -51.03369 | 2025-09-12 04:08:00 | NPP-375D | ORTIGUEIRA | PARANÁ | Brasil | 4117305 | 41 | 33 | nan | nan | nan | Mata Atlântica | 0.9 |
| 2ff1f0c2-c3e1-384f-b79a-c97f909007d6 | -21.12588 | -42.93396 | 2025-09-12 04:08:00 | NPP-375D | UBÁ | MINAS GERAIS | Brasil | 3169901 | 31 | 33 | nan | nan | nan | Mata Atlântica | 0.3 |
| 51524f8f-050c-39f6-8deb-1c24b4d58b3d | -23.15 | -48.25038 | 2025-09-12 04:08:00 | NPP-375D | BOFETE | SÃO PAULO | Brasil | 3506904 | 35 | 33 | nan | nan | nan | Mata Atlântica | 2.3 |
| ce4aa116-542d-320e-bf3a-fc57abadb8f4 | -21.94563 | -47.55956 | 2025-09-12 04:08:00 | NPP-375D | DESCALVADO | SÃO PAULO | Brasil | 3513702 | 35 | 33 | nan | nan | nan | Cerrado | 2.9 |
| f0a459ef-15e8-3b7f-b805-7c0e1711127e | -17.37842 | -52.95498 | 2025-09-12 04:08:00 | NPP-375D | MINEIROS | GOIÁS | Brasil | 5213103 | 52 | 33 | nan | nan | nan | Cerrado | 2.5 |
| 03fb732f-43a3-3eb2-a7f5-e1d1e0d7e28b | -20.26911 | -42.11232 | 2025-09-12 04:08:00 | NPP-375D | MANHUAÇU | MINAS GERAIS | Brasil | 3139409 | 31 | 33 | nan | nan | nan | Mata Atlântica | 2.8 |
| 4fbe2626-366b-3055-8b6a-27e5c2c06494 | -18.82579 | -46.8836 | 2025-09-12 04:08:00 | NPP-375D | PATROCÍNIO | MINAS GERAIS | Brasil | 3148103 | 31 | 33 | nan | nan | nan | Cerrado | 2.2 |
| ea4d697a-dbe4-3444-92e5-170b55a224d4 | -22.60866 | -47.27618 | 2025-09-12 04:08:00 | NPP-375D | LIMEIRA | SÃO PAULO | Brasil | 3526902 | 35 | 33 | nan | nan | nan | Cerrado | 1.0 |
| f76b9382-e518-30d2-b3e5-9a46fba5a511 | -20.13112 | -47.68433 | 2025-09-12 04:08:00 | NPP-375D | IGARAPAVA | SÃO PAULO | Brasil | 3520103 | 35 | 33 | nan | nan | nan | Cerrado | 0.6 |
| 9679704e-7470-3540-87e1-5f11eaa70994 | -22.65532 | -53.10551 | 2025-09-12 04:08:00 | NPP-375D | MARILENA | PARANÁ | Brasil | 4115002 | 41 | 33 | nan | nan | nan | Mata Atlântica | 0.8 |
| 12116038-b8f0-3bf3-a511-3eccf5c84a0e | -19.97363 | -44.95885 | 2025-09-12 04:08:00 | NPP-375D | PERDIGÃO | MINAS GERAIS | Brasil | 3149705 | 31 | 33 | nan | nan | nan | Cerrado | 0.7 |
| fcfd12fd-3314-3269-95e6-b51ecbb2d284 | -21.32265 | -45.02676 | 2025-09-12 04:08:00 | NPP-375D | LAVRAS | MINAS GERAIS | Brasil | 3138203 | 31 | 33 | nan | nan | nan | Mata Atlântica | 1.0 |
| 965efa72-2c05-33d0-a540-22a87f6144b7 | -18.3281 | -52.05911 | 2025-09-12 04:08:00 | NPP-375D | SERRANÓPOLIS | GOIÁS | Brasil | 5220504 | 52 | 33 | nan | nan | nan | Cerrado | 0.4 |
| 260a9d9c-4479-37ba-9fcd-310a8f832c0b | -22.60835 | -47.27388 | 2025-09-12 04:08:00 | NPP-375D | LIMEIRA | SÃO PAULO | Brasil | 3526902 | 35 | 33 | nan | nan | nan | Cerrado | 0.7 |
| 690bbb1e-b509-39b9-9d70-f11d922a8998 | -21.19465 | -47.52647 | 2025-09-12 04:08:00 | NPP-375D | ALTINÓPOLIS | SÃO PAULO | Brasil | 3501004 | 35 | 33 | nan | nan | nan | Cerrado | 17.2 |
| 44bbec61-fd67-3bab-9ca5-31371a95af9d | -22.15152 | -45.83023 | 2025-09-12 04:08:00 | NPP-375D | SÃO SEBASTIÃO DA BELA VISTA | MINAS GERAIS | Brasil | 3164407 | 31 | 33 | nan | nan | nan | Mata Atlântica | 2.4 |
| ace0addd-673d-3f1b-a0b7-5afc796a6eef | -23.10996 | -47.48981 | 2025-09-12 04:08:00 | NPP-375D | PORTO FELIZ | SÃO PAULO | Brasil | 3540606 | 35 | 33 | nan | nan | nan | Mata Atlântica | 2.3 |
| df3067c8-7e07-315a-aff4-cdf76e0a2008 | -19.9695 | -46.88446 | 2025-09-12 04:08:00 | NPP-375D | TAPIRA | MINAS GERAIS | Brasil | 3168101 | 31 | 33 | nan | nan | nan | Cerrado | 0.6 |
| f9d767bc-fc3f-339d-a420-da29bbd37c02 | -21.95856 | -47.55236 | 2025-09-12 04:08:00 | NPP-375D | DESCALVADO | SÃO PAULO | Brasil | 3513702 | 35 | 33 | nan | nan | nan | Cerrado | 1.0 |
| c5910267-aac0-3008-82cb-70866edfb1ed | -20.01354 | -47.64709 | 2025-09-12 04:08:00 | NPP-375D | CONQUISTA | MINAS GERAIS | Brasil | 3118205 | 31 | 33 | nan | nan | nan | Cerrado | 2.4 |
| 9025f064-c127-34e8-84ca-d4edbd8284a1 | -19.88255 | -41.41849 | 2025-09-12 04:08:00 | NPP-375D | MUTUM | MINAS GERAIS | Brasil | 3144003 | 31 | 33 | nan | nan | nan | Mata Atlântica | 1.8 |
| 99ea4049-cd4a-39cc-befe-a6fcc2ade75a | -23.28822 | -46.47547 | 2025-09-12 04:08:00 | NPP-375D | MAIRIPORÃ | SÃO PAULO | Brasil | 3528502 | 35 | 33 | nan | nan | nan | Mata Atlântica | 2.7 |
| 71aa8199-20f3-3c1a-b4c0-0e56e703159d | -23.27589 | -46.54675 | 2025-09-12 04:08:00 | NPP-375D | MAIRIPORÃ | SÃO PAULO | Brasil | 3528502 | 35 | 33 | nan | nan | nan | Mata Atlântica | 0.7 |
| 6935aa72-92fe-3ea4-b6b3-0aa1975e8a5b | -22.79761 | -47.80383 | 2025-09-12 04:08:00 | NPP-375D | PIRACICABA | SÃO PAULO | Brasil | 3538709 | 35 | 33 | nan | nan | nan | Cerrado | 3.5 |
| 9d6bb546-024d-3b3b-a1eb-7d88af0fee7a | -23.40143 | -46.8615 | 2025-09-12 04:08:00 | NPP-375D | CAJAMAR | SÃO PAULO | Brasil | 3509205 | 35 | 33 | nan | nan | nan | Mata Atlântica | 0.7 |
| 66e53bfc-612e-326f-aff0-39eb67eee074 | -20.69916 | -46.07208 | 2025-09-12 04:08:00 | NPP-375D | GUAPÉ | MINAS GERAIS | Brasil | 3128105 | 31 | 33 | nan | nan | nan | Cerrado | 1.8 |
| a4187e0c-8be2-3392-928a-8c189ce67c72 | -22.60669 | -47.28297 | 2025-09-12 04:08:00 | NPP-375D | LIMEIRA | SÃO PAULO | Brasil | 3526902 | 35 | 33 | nan | nan | nan | Cerrado | 1.1 |
| d054a7d6-3946-323e-90f3-2e34e41e9ca9 | -19.98841 | -47.63153 | 2025-09-12 04:08:00 | NPP-375D | CONQUISTA | MINAS GERAIS | Brasil | 3118205 | 31 | 33 | nan | nan | nan | Cerrado | 1.3 |
| 4f4b12fe-a90f-3c74-aced-89d496c6cfd3 | -17.38107 | -52.94268 | 2025-09-12 04:08:00 | NPP-375D | MINEIROS | GOIÁS | Brasil | 5213103 | 52 | 33 | nan | nan | nan | Cerrado | 1.9 |
| 36f1946f-15ae-3ac2-8f7d-acc02534b7de | -18.54013 | -48.4096 | 2025-09-12 04:08:00 | NPP-375D | ARAGUARI | MINAS GERAIS | Brasil | 3103504 | 31 | 33 | nan | nan | nan | Mata Atlântica | 9.5 |
| f794059c-64b3-35c8-8d64-3436a785b77e | -22.87081 | -46.40012 | 2025-09-12 04:08:00 | NPP-375D | VARGEM | SÃO PAULO | Brasil | 3556354 | 35 | 33 | nan | nan | nan | Mata Atlântica | 0.5 |
| 6d44b941-3af7-33d5-9bab-4fba89ac155d | -21.76738 | -47.2824 | 2025-09-12 04:08:00 | NPP-375D | SANTA CRUZ DAS PALMEIRAS | SÃO PAULO | Brasil | 3546306 | 35 | 33 | nan | nan | nan | Mata Atlântica | 1.0 |
| f4fea0ab-b4b1-3d43-a97c-529bed332532 | -22.63054 | -53.09559 | 2025-09-12 04:08:00 | NPP-375D | ROSANA | SÃO PAULO | Brasil | 3544251 | 35 | 33 | nan | nan | nan | Mata Atlântica | 3.4 |
| 3f7addd9-ef32-3d8b-bd22-a6050c826dde | -22.66347 | -53.1212 | 2025-09-12 04:08:00 | NPP-375D | MARILENA | PARANÁ | Brasil | 4115002 | 41 | 33 | nan | nan | nan | Mata Atlântica | 1.1 |
| cf455e9a-aefa-37aa-ba31-c7ba9fcb2100 | -20.03882 | -41.74498 | 2025-09-12 04:08:00 | NPP-375D | CHALÉ | MINAS GERAIS | Brasil | 3116001 | 31 | 33 | nan | nan | nan | Mata Atlântica | 4.1 |
| 49239fcf-6e7e-340f-b6a8-ad74a9868ae8 | -19.06281 | -48.74289 | 2025-09-12 04:08:00 | NPP-375D | MONTE ALEGRE DE MINAS | MINAS GERAIS | Brasil | 3142809 | 31 | 33 | nan | nan | nan | Cerrado | 0.7 |
| 19dc430d-1b6d-3b50-80cc-3fae95fc96c1 | -21.17425 | -54.9696 | 2025-09-12 04:08:00 | NPP-375D | SIDROLÂNDIA | MATO GROSSO DO SUL | Brasil | 5007901 | 50 | 33 | nan | nan | nan | Cerrado | 0.4 |
| 0bb2da35-5968-367a-897f-030014f80caf | -18.44769 | -47.17021 | 2025-09-12 04:08:00 | NPP-375D | COROMANDEL | MINAS GERAIS | Brasil | 3119302 | 31 | 33 | nan | nan | nan | Cerrado | 5.1 |
| b6349049-9a5b-3b5b-85f1-db5afdc1949d | -18.65445 | -47.66637 | 2025-09-12 04:08:00 | NPP-375D | ESTRELA DO SUL | MINAS GERAIS | Brasil | 3124807 | 31 | 33 | nan | nan | nan | Cerrado | 4.2 |
| 257970e8-d6e3-3a2a-9184-e42657fd9821 | -23.5503 | -46.17099 | 2025-09-12 04:08:00 | NPP-375D | MOGI DAS CRUZES | SÃO PAULO | Brasil | 3530607 | 35 | 33 | nan | nan | nan | Mata Atlântica | 0.9 |
| ab7d473c-92ae-31c6-9997-b2411ba134c2 | -20.26854 | -42.1161 | 2025-09-12 04:08:00 | NPP-375D | MANHUAÇU | MINAS GERAIS | Brasil | 3139409 | 31 | 33 | nan | nan | nan | Mata Atlântica | 2.4 |
| 01adc70b-2b83-3c4c-beff-955b14062fad | -21.29101 | -45.95362 | 2025-09-12 04:08:00 | NPP-375D | ALFENAS | MINAS GERAIS | Brasil | 3101607 | 31 | 33 | nan | nan | nan | Mata Atlântica | 3.4 |
| f403182d-fca8-30a4-9b7e-1379e8df403c | -22.18429 | -49.73367 | 2025-09-12 04:08:00 | NPP-375D | GARÇA | SÃO PAULO | Brasil | 3516705 | 35 | 33 | nan | nan | nan | Mata Atlântica | 6.8 |
| f2d53383-14a7-36ee-9575-1851c74b6ab0 | -22.19424 | -49.59505 | 2025-09-12 04:08:00 | NPP-375D | GARÇA | SÃO PAULO | Brasil | 3516705 | 35 | 33 | nan | nan | nan | Mata Atlântica | 1.5 |
| 8ea2507c-d4e7-31a8-bdc6-fa4097266eda | -21.32658 | -45.00329 | 2025-09-12 04:08:00 | NPP-375D | LAVRAS | MINAS GERAIS | Brasil | 3138203 | 31 | 33 | nan | nan | nan | Mata Atlântica | 2.0 |
| 1ffa35ce-4eb4-3742-b130-19f1adb3cea0 | -20.1209 | -42.35209 | 2025-09-12 04:08:00 | NPP-375D | RAUL SOARES | MINAS GERAIS | Brasil | 3154002 | 31 | 33 | nan | nan | nan | Mata Atlântica | 2.8 |
| 775a2e29-5a4c-368e-8f17-497d094df595 | -17.37058 | -52.92405 | 2025-09-12 04:08:00 | NPP-375D | MINEIROS | GOIÁS | Brasil | 5213103 | 52 | 33 | nan | nan | nan | Cerrado | 2.7 |
| 6838ef47-40b6-3d08-adf6-421cc6d26b95 | -18.61699 | -48.24934 | 2025-09-12 04:08:00 | NPP-375D | ARAGUARI | MINAS GERAIS | Brasil | 3103504 | 31 | 33 | nan | nan | nan | Mata Atlântica | 3.1 |
| 6a9a4461-c7dc-3163-8a17-7cbffc743456 | -20.00485 | -47.65087 | 2025-09-12 04:08:00 | NPP-375D | CONQUISTA | MINAS GERAIS | Brasil | 3118205 | 31 | 33 | nan | nan | nan | Cerrado | 1.8 |
| a9965864-1a0e-3f3f-a283-40f9a31213f9 | -20.35923 | -49.95814 | 2025-09-12 04:08:00 | NPP-375D | VOTUPORANGA | SÃO PAULO | Brasil | 3557105 | 35 | 33 | nan | nan | nan | Cerrado | 1.1 |
| cc066a65-3487-3413-a8f2-bb3947446ced | -19.97558 | -47.5929 | 2025-09-12 04:08:00 | NPP-375D | CONQUISTA | MINAS GERAIS | Brasil | 3118205 | 31 | 33 | nan | nan | nan | Cerrado | 1.0 |
| 028a257a-639a-3e13-aad0-1220ad54ff6f | -20.55805 | -46.93173 | 2025-09-12 04:08:00 | NPP-375D | CÁSSIA | MINAS GERAIS | Brasil | 3115102 | 31 | 33 | nan | nan | nan | Cerrado | 3.6 |
| 88c5df78-a19d-3bcc-9453-629eb6910a2c | -20.58892 | -48.57596 | 2025-09-12 04:08:00 | NPP-375D | BARRETOS | SÃO PAULO | Brasil | 3505500 | 35 | 33 | nan | nan | nan | Cerrado | 3.2 |
| 243f6d2c-b7d4-3090-b25f-a7f880476f35 | -18.59732 | -47.18681 | 2025-09-12 04:08:00 | NPP-375D | COROMANDEL | MINAS GERAIS | Brasil | 3119302 | 31 | 33 | nan | nan | nan | Cerrado | 9.0 |
| 5ae2ddb0-f9ba-322a-9eab-bbe01f3f588b | -22.39986 | -46.74654 | 2025-09-12 04:08:00 | NPP-375D | ITAPIRA | SÃO PAULO | Brasil | 3522604 | 35 | 33 | nan | nan | nan | Mata Atlântica | 11.4 |
| 877c1359-3c75-3a13-9a4b-2c5c3ba31971 | -23.38518 | -47.016 | 2025-09-12 04:08:00 | NPP-375D | PIRAPORA DO BOM JESUS | SÃO PAULO | Brasil | 3539103 | 35 | 33 | nan | nan | nan | Mata Atlântica | 1.2 |
| 4fde8cab-4c75-31ec-aede-4d024b38c3e3 | -19.19441 | -48.0128 | 2025-09-12 04:08:00 | NPP-375D | UBERLÂNDIA | MINAS GERAIS | Brasil | 3170206 | 31 | 33 | nan | nan | nan | Cerrado | 15.7 |
| 1ea9e603-fedd-353d-902f-4611e4265a60 | -21.19 | -47.53053 | 2025-09-12 04:08:00 | NPP-375D | ALTINÓPOLIS | SÃO PAULO | Brasil | 3501004 | 35 | 33 | nan | nan | nan | Cerrado | 38.0 |
| 21643f7e-d064-3035-83f7-4e828cf4b43d | -23.14911 | -48.25512 | 2025-09-12 04:08:00 | NPP-375D | BOFETE | SÃO PAULO | Brasil | 3506904 | 35 | 33 | nan | nan | nan | Mata Atlântica | 2.3 |
| 924b0a4e-967b-37d1-a3f2-80de6948b690 | -17.3828 | -52.93467 | 2025-09-12 04:08:00 | NPP-375D | MINEIROS | GOIÁS | Brasil | 5213103 | 52 | 33 | nan | nan | nan | Cerrado | 1.4 |
| 6efd6486-6ef6-35de-a635-feeb2f02a578 | -18.53939 | -48.41351 | 2025-09-12 04:08:00 | NPP-375D | ARAGUARI | MINAS GERAIS | Brasil | 3103504 | 31 | 33 | nan | nan | nan | Mata Atlântica | 9.5 |
| 1f944af0-290b-36a3-bfad-f500b1965170 | -20.35485 | -49.95708 | 2025-09-12 04:08:00 | NPP-375D | VOTUPORANGA | SÃO PAULO | Brasil | 3557105 | 35 | 33 | nan | nan | nan | Cerrado | 1.7 |
| af65e51e-42ad-3e71-98f6-3db6a8f9cae1 | -23.13986 | -49.65855 | 2025-09-12 04:08:00 | NPP-375D | TIMBURI | SÃO PAULO | Brasil | 3554607 | 35 | 33 | nan | nan | nan | Mata Atlântica | 8.2 |
| 0d3852da-df3a-303a-8d52-7c8bc19bb00e | -23.16076 | -47.49354 | 2025-09-12 04:08:00 | NPP-375D | PORTO FELIZ | SÃO PAULO | Brasil | 3540606 | 35 | 33 | nan | nan | nan | Mata Atlântica | 0.9 |
| 989438e3-6f42-33d4-ba31-b34443bfbda5 | -19.99998 | -47.65563 | 2025-09-12 04:08:00 | NPP-375D | CONQUISTA | MINAS GERAIS | Brasil | 3118205 | 31 | 33 | nan | nan | nan | Cerrado | 1.5 |
| e8a787bc-0975-38af-86ae-12c34d339066 | -21.51273 | -45.90509 | 2025-09-12 04:08:00 | NPP-375D | ALFENAS | MINAS GERAIS | Brasil | 3101607 | 31 | 33 | nan | nan | nan | Mata Atlântica | 1.2 |
| 35372a85-8e10-3d6b-9a32-3c499a58f5d3 | -18.97324 | -47.90143 | 2025-09-12 04:08:00 | NPP-375D | INDIANÓPOLIS | MINAS GERAIS | Brasil | 3130705 | 31 | 33 | nan | nan | nan | Cerrado | 0.8 |
| 95f36073-d450-3f3d-89e5-0f784c077591 | -21.6491 | -50.12172 | 2025-09-12 04:08:00 | NPP-375D | ALTO ALEGRE | SÃO PAULO | Brasil | 3501103 | 35 | 33 | nan | nan | nan | Mata Atlântica | 1.1 |
| 476393d0-9c84-39f2-b946-eb3f5a1eea47 | -20.36972 | -49.97512 | 2025-09-12 04:08:00 | NPP-375D | VOTUPORANGA | SÃO PAULO | Brasil | 3557105 | 35 | 33 | nan | nan | nan | Cerrado | 0.7 |
| a6e07d79-222a-3c7e-9a68-33166da80cc1 | -22.40343 | -46.74728 | 2025-09-12 04:08:00 | NPP-375D | ITAPIRA | SÃO PAULO | Brasil | 3522604 | 35 | 33 | nan | nan | nan | Mata Atlântica | 11.4 |
| c56489f7-80de-3d01-bec8-5dc0e6345225 | -22.62034 | -53.09295 | 2025-09-12 04:08:00 | NPP-375D | ROSANA | SÃO PAULO | Brasil | 3544251 | 35 | 33 | nan | nan | nan | Mata Atlântica | 8.3 |
| 419f2770-a061-35e9-9dad-b7f5e550e19d | -18.62282 | -46.47317 | 2025-09-12 04:08:00 | NPP-375D | PATOS DE MINAS | MINAS GERAIS | Brasil | 3148004 | 31 | 33 | nan | nan | nan | Cerrado | 0.9 |
| 4303d371-365a-3f72-955f-2175c24e9ae2 | -23.42583 | -47.02284 | 2025-09-12 04:08:00 | NPP-375D | PIRAPORA DO BOM JESUS | SÃO PAULO | Brasil | 3539103 | 35 | 33 | nan | nan | nan | Mata Atlântica | 1.8 |
| ef32fadc-18ea-3774-b403-fd430af5ebee | -20.86932 | -46.50716 | 2025-09-12 04:08:00 | NPP-375D | PASSOS | MINAS GERAIS | Brasil | 3147907 | 31 | 33 | nan | nan | nan | Cerrado | 1.1 |
| fc34387c-b698-387f-8576-8cb596e25ddd | -23.11188 | -47.51169 | 2025-09-12 04:08:00 | NPP-375D | PORTO FELIZ | SÃO PAULO | Brasil | 3540606 | 35 | 33 | nan | nan | nan | Mata Atlântica | 3.5 |
| bb3666f9-46b0-33c4-9e13-0ae1c343c24b | -20.60502 | -46.90339 | 2025-09-12 04:08:00 | NPP-375D | CÁSSIA | MINAS GERAIS | Brasil | 3115102 | 31 | 33 | nan | nan | nan | Mata Atlântica | 1.9 |
| 3a6837f4-9455-38e4-a948-18b32b8af1d5 | -19.9978 | -46.9189 | 2025-09-12 04:08:00 | NPP-375D | TAPIRA | MINAS GERAIS | Brasil | 3168101 | 31 | 33 | nan | nan | nan | Cerrado | 2.6 |
| 2519e3ae-3758-3852-863f-9a095cb06360 | -23.14302 | -49.65656 | 2025-09-12 04:08:00 | NPP-375D | TIMBURI | SÃO PAULO | Brasil | 3554607 | 35 | 33 | nan | nan | nan | Mata Atlântica | 7.2 |
| 8ab1afd8-2323-318f-bc54-79419f37a7fa | -23.19211 | -49.65436 | 2025-09-12 04:08:00 | NPP-375D | TIMBURI | SÃO PAULO | Brasil | 3554607 | 35 | 33 | nan | nan | nan | Mata Atlântica | 5.5 |
| 08447038-feab-378f-95e8-66a48d263a2b | -22.86662 | -46.40338 | 2025-09-12 04:08:00 | NPP-375D | VARGEM | SÃO PAULO | Brasil | 3556354 | 35 | 33 | nan | nan | nan | Mata Atlântica | 0.5 |
| 56ba3cc5-891a-3c6f-961c-7b62317ed5e7 | -19.81228 | -45.00191 | 2025-09-12 04:08:00 | NPP-375D | NOVA SERRANA | MINAS GERAIS | Brasil | 3145208 | 31 | 33 | nan | nan | nan | Cerrado | 1.1 |
| 96dd14ed-1428-3a3b-b976-f09da840e230 | -22.17927 | -49.7369 | 2025-09-12 04:08:00 | NPP-375D | GARÇA | SÃO PAULO | Brasil | 3516705 | 35 | 33 | nan | nan | nan | Mata Atlântica | 5.6 |
| 12b07e00-97b6-3a66-80c6-2ac9e6d956f9 | -21.32057 | -45.01832 | 2025-09-12 04:08:00 | NPP-375D | LAVRAS | MINAS GERAIS | Brasil | 3138203 | 31 | 33 | nan | nan | nan | Mata Atlântica | 4.2 |
| f8b44a66-790f-358f-aecd-e389d37d72f2 | -23.14528 | -48.25453 | 2025-09-12 04:08:00 | NPP-375D | BOFETE | SÃO PAULO | Brasil | 3506904 | 35 | 33 | nan | nan | nan | Mata Atlântica | 5.4 |


[Clique aqui para ver as próximas entradas](README57.md)
