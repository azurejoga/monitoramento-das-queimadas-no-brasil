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

## Dados Diários - Página 4

| ID | Latitude | Longitude | Data/Hora GMT | Satélite | Município | Estado | País | Município ID | Estado ID | País ID | Dias sem Chuva | Precipitação | Risco de Fogo | Bioma | FRP |
|----|----------|-----------|---------------|----------|-----------|--------|------|--------------|-----------|---------|----------------|--------------|----------------|-------|-----|
| b3659957-d20e-32b4-ae4e-bcca815e7921 | -20.37592 | -43.59143 | 2025-02-18 03:49:00 | NOAA-20 | OURO PRETO | MINAS GERAIS | Brasil | 3146107 | 31 | 33 | nan | nan | nan | Mata Atlântica | 1.9 |
| 8dbabcf9-6c3c-3efa-93fe-9ac7889c7ac9 | -14.98886 | -50.77552 | 2025-02-18 03:49:00 | NOAA-20 | ARAGUAPAZ | GOIÁS | Brasil | 5202155 | 52 | 33 | nan | nan | nan | Cerrado | 3.1 |
| e27110e7-1dc2-3541-bc3b-c0fbcc4efc29 | -20.88916 | -40.79874 | 2025-02-18 03:49:00 | NOAA-20 | ITAPEMIRIM | ESPÍRITO SANTO | Brasil | 3202801 | 32 | 33 | nan | nan | nan | Mata Atlântica | 6.0 |
| d18d2155-a4f8-33ce-8896-f3d885e0a0be | -20.6102 | -40.98824 | 2025-02-18 03:49:00 | NOAA-20 | VARGEM ALTA | ESPÍRITO SANTO | Brasil | 3205036 | 32 | 33 | nan | nan | nan | Mata Atlântica | 3.8 |
| 840c62f8-4773-32d3-924c-86a91e966bdc | -14.98045 | -50.77492 | 2025-02-18 03:49:00 | NOAA-20 | ARAGUAPAZ | GOIÁS | Brasil | 5202155 | 52 | 33 | nan | nan | nan | Cerrado | 2.0 |
| 9c17f3a1-b099-37c7-bff6-91ac7795ae76 | -14.98168 | -50.77893 | 2025-02-18 03:49:00 | NOAA-20 | ARAGUAPAZ | GOIÁS | Brasil | 5202155 | 52 | 33 | nan | nan | nan | Cerrado | 1.8 |
| 245037b2-ba4a-3a07-a164-3bc02edeb7f5 | -16.89939 | -43.66014 | 2025-02-18 03:49:00 | NOAA-20 | GLAUCILÂNDIA | MINAS GERAIS | Brasil | 3127354 | 31 | 33 | nan | nan | nan | Cerrado | 7.5 |
| 0340f590-4acb-3ea4-90e7-4231832bc8d2 | -14.98271 | -50.77396 | 2025-02-18 03:49:00 | NOAA-20 | ARAGUAPAZ | GOIÁS | Brasil | 5202155 | 52 | 33 | nan | nan | nan | Cerrado | 1.7 |
| 0c55618c-6e42-3537-b806-24dc7e2a4b8c | -18.397 | -45.97634 | 2025-02-18 03:49:00 | NOAA-20 | VARJÃO DE MINAS | MINAS GERAIS | Brasil | 3170750 | 31 | 33 | nan | nan | nan | Cerrado | 1.1 |
| d9e70c86-29e1-3731-9ec4-d23b2b3c4890 | -16.68216 | -43.88577 | 2025-02-18 03:49:00 | NOAA-20 | MONTES CLAROS | MINAS GERAIS | Brasil | 3143302 | 31 | 33 | nan | nan | nan | Cerrado | 2.5 |
| 93355cdc-fe92-329f-80d0-4bf8b932da1b | -9.18076 | -40.31091 | 2025-02-18 03:49:00 | NOAA-20 | PETROLINA | PERNAMBUCO | Brasil | 2611101 | 26 | 33 | nan | nan | nan | Caatinga | 0.8 |
| edb42052-c7b9-3d76-9009-38692e535b0c | -19.83799 | -40.08046 | 2025-02-18 03:49:00 | NOAA-20 | ARACRUZ | ESPÍRITO SANTO | Brasil | 3200607 | 32 | 33 | nan | nan | nan | Mata Atlântica | 2.0 |
| 681a9b55-3701-3cc3-983d-647b9bd32478 | -18.77098 | -41.93487 | 2025-02-18 03:49:00 | NOAA-20 | GOVERNADOR VALADARES | MINAS GERAIS | Brasil | 3127701 | 31 | 33 | nan | nan | nan | Mata Atlântica | 3.8 |
| aa4f1638-91c0-3402-9505-25bab569277f | -20.61515 | -42.18919 | 2025-02-18 03:49:00 | NOAA-20 | DIVINO | MINAS GERAIS | Brasil | 3122009 | 31 | 33 | nan | nan | nan | Mata Atlântica | 0.9 |
| a344bccd-dbfe-326d-8f5f-aa6562ad4555 | -20.37787 | -40.84698 | 2025-02-18 03:49:00 | NOAA-20 | DOMINGOS MARTINS | ESPÍRITO SANTO | Brasil | 3201902 | 32 | 33 | nan | nan | nan | Mata Atlântica | 1.2 |
| dabf7916-d58c-3afb-a6a0-2ff94e399a65 | -10.17811 | -36.46277 | 2025-02-18 03:49:00 | NOAA-20 | PENEDO | ALAGOAS | Brasil | 2706703 | 27 | 33 | nan | nan | nan | Caatinga | 1.2 |
| 474debf9-a09e-33f3-bf00-47c57cf391e9 | -20.62586 | -40.93383 | 2025-02-18 03:49:00 | NOAA-20 | VARGEM ALTA | ESPÍRITO SANTO | Brasil | 3205036 | 32 | 33 | nan | nan | nan | Mata Atlântica | 1.0 |
| 4f956348-d1f4-3454-bf3c-d63f26283adb | -18.11692 | -39.68744 | 2025-02-18 03:49:00 | NOAA-20 | MUCURI | BAHIA | Brasil | 2922003 | 29 | 33 | nan | nan | nan | Mata Atlântica | 0.7 |
| ce7f20c0-e95b-30cd-ae38-ff319861a3d4 | -17.18128 | -40.74786 | 2025-02-18 03:49:00 | NOAA-20 | UMBURATIBA | MINAS GERAIS | Brasil | 3170305 | 31 | 33 | nan | nan | nan | Mata Atlântica | 0.8 |
| 05b0368e-93d6-3408-bca6-5ae5a658d6a8 | -14.98781 | -50.78052 | 2025-02-18 03:49:00 | NOAA-20 | ARAGUAPAZ | GOIÁS | Brasil | 5202155 | 52 | 33 | nan | nan | nan | Cerrado | 2.7 |
| f185fbe3-cc66-3b62-b999-e6a30412814a | -19.9646 | -45.16481 | 2025-02-18 03:49:00 | NOAA-20 | ARAÚJOS | MINAS GERAIS | Brasil | 3103900 | 31 | 33 | nan | nan | nan | Cerrado | 2.6 |
| b2b7fa3c-512a-3916-bb71-602bbefda392 | -19.71665 | -40.35286 | 2025-02-18 03:49:00 | NOAA-20 | JOÃO NEIVA | ESPÍRITO SANTO | Brasil | 3203130 | 32 | 33 | nan | nan | nan | Mata Atlântica | 0.9 |
| f34b56a0-2824-3c9b-9b1e-0be68e7aac04 | -7.54757 | -45.87722 | 2025-02-18 03:49:00 | NOAA-20 | BALSAS | MARANHÃO | Brasil | 2101400 | 21 | 33 | nan | nan | nan | Cerrado | 0.9 |
| fa89732a-c3b3-3144-9ca6-0ccaa7b71dc6 | -20.3812 | -40.84758 | 2025-02-18 03:49:00 | NOAA-20 | DOMINGOS MARTINS | ESPÍRITO SANTO | Brasil | 3201902 | 32 | 33 | nan | nan | nan | Mata Atlântica | 0.7 |
| 791577cb-fe2a-3cdc-a72b-e70e0a7f9030 | -7.54814 | -45.87403 | 2025-02-18 03:49:00 | NOAA-20 | BALSAS | MARANHÃO | Brasil | 2101400 | 21 | 33 | nan | nan | nan | Cerrado | 0.9 |
| aaa80508-cb13-35af-8ab6-2f31dd6d78f8 | -7.54926 | -45.86778 | 2025-02-18 03:49:00 | NOAA-20 | BALSAS | MARANHÃO | Brasil | 2101400 | 21 | 33 | nan | nan | nan | Cerrado | 0.8 |
| 8be4d8e1-cad1-3bb7-be96-2455e82d94ee | -14.97937 | -50.77987 | 2025-02-18 03:49:00 | NOAA-20 | ARAGUAPAZ | GOIÁS | Brasil | 5202155 | 52 | 33 | nan | nan | nan | Cerrado | 2.0 |
| 661b2033-4d83-3ae9-997e-5735f27dcda5 | -20.70007 | -41.70373 | 2025-02-18 03:49:00 | NOAA-20 | GUAÇUÍ | ESPÍRITO SANTO | Brasil | 3202306 | 32 | 33 | nan | nan | nan | Mata Atlântica | 1.1 |
| 908513e5-b9cd-3211-9354-9f9130f95f3c | -21.62725 | -43.46534 | 2025-02-18 03:49:00 | NOAA-20 | JUIZ DE FORA | MINAS GERAIS | Brasil | 3136702 | 31 | 33 | nan | nan | nan | Mata Atlântica | 1.1 |
| 01b77ef3-e18d-30a4-b61c-226b992868ed | -17.75073 | -42.89653 | 2025-02-18 03:49:00 | NOAA-20 | ITAMARANDIBA | MINAS GERAIS | Brasil | 3132503 | 31 | 33 | nan | nan | nan | Cerrado | 1.1 |
| b103d852-48c2-37e4-b350-569165221331 | -10.18201 | -36.4597 | 2025-02-18 03:49:00 | NOAA-20 | PENEDO | ALAGOAS | Brasil | 2706703 | 27 | 33 | nan | nan | nan | Caatinga | 1.4 |
| 275abb19-619e-3473-a1dc-d72c8e76206a | -18.7703 | -41.93887 | 2025-02-18 03:49:00 | NOAA-20 | GOVERNADOR VALADARES | MINAS GERAIS | Brasil | 3127701 | 31 | 33 | nan | nan | nan | Mata Atlântica | 3.8 |
| 376c1c83-dc83-3b17-9f6b-78dec737166d | -17.76424 | -39.76841 | 2025-02-18 03:49:00 | NOAA-20 | IBIRAPUÃ | BAHIA | Brasil | 2912806 | 29 | 33 | nan | nan | nan | Mata Atlântica | 0.7 |
| 26e3522a-daf3-387a-b490-dbf5a892e643 | -20.6145 | -42.19308 | 2025-02-18 03:49:00 | NOAA-20 | DIVINO | MINAS GERAIS | Brasil | 3122009 | 31 | 33 | nan | nan | nan | Mata Atlântica | 0.8 |
| 674a6d69-9f03-38d4-8160-386e4a9cb90c | -14.98552 | -50.78144 | 2025-02-18 03:49:00 | NOAA-20 | ARAGUAPAZ | GOIÁS | Brasil | 5202155 | 52 | 33 | nan | nan | nan | Cerrado | 2.0 |
| 5629bc9e-432f-35bc-885c-563039e18f74 | -19.33818 | -44.83797 | 2025-02-18 03:49:00 | NOAA-20 | POMPÉU | MINAS GERAIS | Brasil | 3152006 | 31 | 33 | nan | nan | nan | Cerrado | 1.3 |
| ae2c02b2-de75-3c67-9db5-c61f252cf81e | -20.34721 | -40.36158 | 2025-02-18 03:49:00 | NOAA-20 | CARIACICA | ESPÍRITO SANTO | Brasil | 3201308 | 32 | 33 | nan | nan | nan | Mata Atlântica | 2.3 |
| 28c39064-015d-3c2f-b981-f819fb7c058e | -17.77783 | -42.8059 | 2025-02-18 03:49:00 | NOAA-20 | ITAMARANDIBA | MINAS GERAIS | Brasil | 3132503 | 31 | 33 | nan | nan | nan | Cerrado | 1.3 |
| 5154f862-126f-319d-a633-6e7179f7f80c | -9.50245 | -40.92796 | 2025-02-18 03:49:00 | NOAA-20 | SOBRADINHO | BAHIA | Brasil | 2930774 | 29 | 33 | nan | nan | nan | Caatinga | 1.6 |
| c55a7472-b074-3c92-a232-966f60230a05 | -20.6616 | -42.20452 | 2025-02-18 03:49:00 | NOAA-20 | DIVINO | MINAS GERAIS | Brasil | 3122009 | 31 | 33 | nan | nan | nan | Mata Atlântica | 0.9 |
| f999b525-100b-3489-a708-1c1eb097700a | -20.7007 | -41.69994 | 2025-02-18 03:49:00 | NOAA-20 | GUAÇUÍ | ESPÍRITO SANTO | Brasil | 3202306 | 32 | 33 | nan | nan | nan | Mata Atlântica | 1.3 |
| 76e4f570-c4dd-3722-ae8d-0756e9a82c96 | -16.64023 | -39.8693 | 2025-02-18 03:49:00 | NOAA-20 | GUARATINGA | BAHIA | Brasil | 2911808 | 29 | 33 | nan | nan | nan | Mata Atlântica | 0.9 |
| 5572c405-d699-3de5-99ab-3b0514dcb4f8 | -9.12428 | -40.56378 | 2025-02-18 03:49:00 | NOAA-20 | PETROLINA | PERNAMBUCO | Brasil | 2611101 | 26 | 33 | nan | nan | nan | Caatinga | 1.5 |
| 8d4497b8-7b05-3c7c-a995-034ff6d82595 | -20.60626 | -40.99137 | 2025-02-18 03:49:00 | NOAA-20 | VARGEM ALTA | ESPÍRITO SANTO | Brasil | 3205036 | 32 | 33 | nan | nan | nan | Mata Atlântica | 1.6 |
| ccfc71e3-2694-3093-879b-e5653529d393 | -16.34825 | -43.69825 | 2025-02-18 03:49:00 | NOAA-20 | CAPITÃO ENÉAS | MINAS GERAIS | Brasil | 3112703 | 31 | 33 | nan | nan | nan | Cerrado | 1.3 |
| 2f961b4c-7dc2-346f-a39e-9ad0cdaf615a | -14.406 | -42.86628 | 2025-02-18 03:49:00 | NOAA-20 | CANDIBA | BAHIA | Brasil | 2906600 | 29 | 33 | nan | nan | nan | Caatinga | 1.2 |
| e96d9bab-c47e-3256-855c-a44efc6c62b4 | -10.27993 | -40.80962 | 2025-02-18 03:49:00 | NOAA-20 | CAMPO FORMOSO | BAHIA | Brasil | 2906006 | 29 | 33 | nan | nan | nan | Caatinga | 0.7 |
| b5624bc2-f706-3e82-bd6e-877383085927 | -19.17045 | -40.1334 | 2025-02-18 03:49:00 | NOAA-20 | SOORETAMA | ESPÍRITO SANTO | Brasil | 3205010 | 32 | 33 | nan | nan | nan | Mata Atlântica | 2.8 |
| 94ab794a-453f-3fc7-9d5f-ff8e37b7a6d0 | -15.55812 | -46.28082 | 2025-02-18 03:49:00 | NOAA-20 | BURITIS | MINAS GERAIS | Brasil | 3109303 | 31 | 33 | nan | nan | nan | Cerrado | 1.0 |
| 82e67e5c-e3b9-32b3-8fd4-8e63570e64cc | -10.17866 | -36.45917 | 2025-02-18 03:49:00 | NOAA-20 | PENEDO | ALAGOAS | Brasil | 2706703 | 27 | 33 | nan | nan | nan | Caatinga | 1.2 |
| 30ae22be-d72e-3a15-b691-df839482043b | -9.72964 | -37.25578 | 2025-02-18 03:49:00 | NOAA-20 | PALESTINA | ALAGOAS | Brasil | 2706208 | 27 | 33 | nan | nan | nan | Caatinga | 0.8 |
| 16c0809f-ad3c-37fa-ab5f-36278f6375bb | -18.44127 | -44.48972 | 2025-02-18 03:49:00 | NOAA-20 | CORINTO | MINAS GERAIS | Brasil | 3119104 | 31 | 33 | nan | nan | nan | Cerrado | 3.6 |
| ea56d92b-d1e1-36d7-8e81-7dde276e8b25 | -20.41647 | -43.55273 | 2025-02-18 03:49:00 | NOAA-20 | OURO PRETO | MINAS GERAIS | Brasil | 3146107 | 31 | 33 | nan | nan | nan | Mata Atlântica | 2.4 |
| 8c39aa96-d022-3d15-86b9-b0cb0de6678e | -14.9866 | -50.77642 | 2025-02-18 03:49:00 | NOAA-20 | ARAGUAPAZ | GOIÁS | Brasil | 5202155 | 52 | 33 | nan | nan | nan | Cerrado | 2.0 |
| 34fa27f5-cab0-31e4-87c3-403c73d64f34 | -18.92954 | -41.93515 | 2025-02-18 03:49:00 | NOAA-20 | ALPERCATA | MINAS GERAIS | Brasil | 3101805 | 31 | 33 | nan | nan | nan | Mata Atlântica | 1.9 |
| 7535b2bf-e34a-3ff5-a3e9-3995b4aa959a | -18.12023 | -39.68801 | 2025-02-18 03:49:00 | NOAA-20 | MUCURI | BAHIA | Brasil | 2922003 | 29 | 33 | nan | nan | nan | Mata Atlântica | 1.0 |
| 9b275cfa-f0fe-33ca-bcaf-2e708c485dbb | -18.77442 | -41.93556 | 2025-02-18 03:49:00 | NOAA-20 | GOVERNADOR VALADARES | MINAS GERAIS | Brasil | 3127701 | 31 | 33 | nan | nan | nan | Mata Atlântica | 3.8 |
| 8a8eeca3-22cc-3421-89bb-16af1edf2b9e | -22.85641 | -42.98 | 2025-02-18 03:51:00 | NOAA-20 | SÃO GONÇALO | RIO DE JANEIRO | Brasil | 3304904 | 33 | 33 | nan | nan | nan | Mata Atlântica | 0.6 |
| 9084e307-324c-3590-944b-b1cd3a82587e | -22.88968 | -42.84844 | 2025-02-18 03:51:00 | NOAA-20 | MARICÁ | RIO DE JANEIRO | Brasil | 3302700 | 33 | 33 | nan | nan | nan | Mata Atlântica | 2.1 |
| 8dd16ce8-c39b-38d4-8f78-5b0f6d000129 | -21.41503 | -48.54935 | 2025-02-18 03:51:00 | NOAA-20 | TAQUARITINGA | SÃO PAULO | Brasil | 3553708 | 35 | 33 | nan | nan | nan | Mata Atlântica | 2.0 |
| d4d4b30a-1f17-3aef-9171-5f78c7df373c | -21.41496 | -48.55299 | 2025-02-18 03:51:00 | NOAA-20 | TAQUARITINGA | SÃO PAULO | Brasil | 3553708 | 35 | 33 | nan | nan | nan | Mata Atlântica | 3.9 |
| d6fcdb42-aeb7-39f6-9733-069ee8da0358 | -21.41494 | -49.20411 | 2025-02-18 03:51:00 | NOAA-20 | NOVO HORIZONTE | SÃO PAULO | Brasil | 3533502 | 35 | 33 | nan | nan | nan | Mata Atlântica | 1.4 |
| c864f921-efb6-37bf-8470-01f580864689 | -22.91059 | -43.3795 | 2025-02-18 03:51:00 | NOAA-20 | RIO DE JANEIRO | RIO DE JANEIRO | Brasil | 3304557 | 33 | 33 | nan | nan | nan | Mata Atlântica | 2.1 |
| 63cf5353-9997-3116-aefe-916939fc45ce | -22.69804 | -43.34766 | 2025-02-18 03:51:00 | NOAA-20 | DUQUE DE CAXIAS | RIO DE JANEIRO | Brasil | 3301702 | 33 | 33 | nan | nan | nan | Mata Atlântica | 1.7 |
| 79f4a201-f973-3844-ad68-ccc9371f6c34 | -21.32108 | -48.6902 | 2025-02-18 03:51:00 | NOAA-20 | FERNANDO PRESTES | SÃO PAULO | Brasil | 3515608 | 35 | 33 | nan | nan | nan | Mata Atlântica | 3.5 |
| 8d0890f7-d5d7-3b6b-82ad-bcdb3bd60092 | -21.41978 | -48.55054 | 2025-02-18 03:51:00 | NOAA-20 | TAQUARITINGA | SÃO PAULO | Brasil | 3553708 | 35 | 33 | nan | nan | nan | Mata Atlântica | 2.0 |
| 3d72c652-fd3b-3819-8821-361ed8c9626f | -21.52883 | -47.14768 | 2025-02-18 03:51:00 | NOAA-20 | TAMBAÚ | SÃO PAULO | Brasil | 3553302 | 35 | 33 | nan | nan | nan | Cerrado | 1.5 |
| e029f0f5-7343-3edb-aeb9-15469680c502 | -21.41861 | -48.55602 | 2025-02-18 03:51:00 | NOAA-20 | TAQUARITINGA | SÃO PAULO | Brasil | 3553708 | 35 | 33 | nan | nan | nan | Mata Atlântica | 2.4 |
| 4eca106c-9140-3311-9760-4e6938732b4f | -21.52446 | -47.14674 | 2025-02-18 03:51:00 | NOAA-20 | TAMBAÚ | SÃO PAULO | Brasil | 3553302 | 35 | 33 | nan | nan | nan | Cerrado | 1.5 |
| 53b8afaa-427f-3fd5-9dd3-56ab07e016a3 | -22.90003 | -43.75331 | 2025-02-18 03:51:00 | NOAA-20 | RIO DE JANEIRO | RIO DE JANEIRO | Brasil | 3304557 | 33 | 33 | nan | nan | nan | Mata Atlântica | 3.8 |
| 02630ca2-3f44-3a1b-a648-aa9861feecbf | -22.6778 | -42.85424 | 2025-02-18 03:51:00 | NOAA-20 | ITABORAÍ | RIO DE JANEIRO | Brasil | 3301900 | 33 | 33 | nan | nan | nan | Mata Atlântica | 2.9 |
| ab56496c-2261-39ee-bae0-19bf293bba52 | -22.92578 | -43.08593 | 2025-02-18 03:51:00 | NOAA-20 | NITERÓI | RIO DE JANEIRO | Brasil | 3303302 | 33 | 33 | nan | nan | nan | Mata Atlântica | 2.2 |
| 2e8b8f4b-1b90-30a4-ac7d-0eae11a891b2 | -21.37579 | -48.57301 | 2025-02-18 03:51:00 | NOAA-20 | TAQUARITINGA | SÃO PAULO | Brasil | 3553708 | 35 | 33 | nan | nan | nan | Mata Atlântica | 1.5 |
| b475ef87-dc39-32f3-ae8c-75b23bf35f6f | -22.78641 | -43.75813 | 2025-02-18 03:51:00 | NOAA-20 | SEROPÉDICA | RIO DE JANEIRO | Brasil | 3305554 | 33 | 33 | nan | nan | nan | Mata Atlântica | 2.0 |
| 47aed75f-ec69-3b42-bbf3-dde3736bdebb | -21.38059 | -48.57402 | 2025-02-18 03:51:00 | NOAA-20 | TAQUARITINGA | SÃO PAULO | Brasil | 3553708 | 35 | 33 | nan | nan | nan | Mata Atlântica | 2.5 |
| b032784c-7c3f-34fb-8c12-a692da0183de | -21.38178 | -48.5683 | 2025-02-18 03:51:00 | NOAA-20 | TAQUARITINGA | SÃO PAULO | Brasil | 3553708 | 35 | 33 | nan | nan | nan | Mata Atlântica | 2.2 |
| 396803ce-84ae-368a-9781-9e4dde35a513 | -21.52536 | -47.14227 | 2025-02-18 03:51:00 | NOAA-20 | TAMBAÚ | SÃO PAULO | Brasil | 3553302 | 35 | 33 | nan | nan | nan | Cerrado | 1.7 |
| e1fd828f-1f6f-3db6-9395-cd30b23edc46 | -21.37099 | -48.57198 | 2025-02-18 03:51:00 | NOAA-20 | TAQUARITINGA | SÃO PAULO | Brasil | 3553708 | 35 | 33 | nan | nan | nan | Mata Atlântica | 1.5 |
| 31af60cc-06ad-3053-b521-1e5ef50b42f6 | -22.96284 | -43.59934 | 2025-02-18 03:51:00 | NOAA-20 | RIO DE JANEIRO | RIO DE JANEIRO | Brasil | 3304557 | 33 | 33 | nan | nan | nan | Mata Atlântica | 1.7 |
| fff01c68-68c6-36ae-91c1-b8814708e146 | -21.36262 | -48.54007 | 2025-02-18 03:51:00 | NOAA-20 | TAQUARITINGA | SÃO PAULO | Brasil | 3553708 | 35 | 33 | nan | nan | nan | Cerrado | 1.2 |
| b3028cfd-22f6-39f9-8069-fa30b2bd04db | -21.36735 | -48.54135 | 2025-02-18 03:51:00 | NOAA-20 | TAQUARITINGA | SÃO PAULO | Brasil | 3553708 | 35 | 33 | nan | nan | nan | Cerrado | 1.4 |
| 1923379e-f07c-3586-84b5-ca4464171e40 | -22.78552 | -43.75645 | 2025-02-18 03:51:00 | NOAA-20 | SEROPÉDICA | RIO DE JANEIRO | Brasil | 3305554 | 33 | 33 | nan | nan | nan | Mata Atlântica | 1.8 |
| 72b45355-a7fe-3699-a2e1-d769580b9183 | -21.41388 | -48.55477 | 2025-02-18 03:51:00 | NOAA-20 | TAQUARITINGA | SÃO PAULO | Brasil | 3553708 | 35 | 33 | nan | nan | nan | Mata Atlântica | 2.4 |
| a127ce2c-7790-3a74-aa40-6738c884ad12 | -21.41971 | -48.55423 | 2025-02-18 03:51:00 | NOAA-20 | TAQUARITINGA | SÃO PAULO | Brasil | 3553708 | 35 | 33 | nan | nan | nan | Mata Atlântica | 3.9 |
| fb23a3be-f52c-3b6d-b7f9-93a18b3f61c0 | -23.33982 | -46.77301 | 2025-02-18 03:51:00 | NOAA-20 | CAIEIRAS | SÃO PAULO | Brasil | 3509007 | 35 | 33 | nan | nan | nan | Mata Atlântica | 0.8 |
| 29076d17-6e7b-36e0-bdb9-4d66b1d3b4c9 | 3.5578 | -60.32035 | 2025-02-18 04:36:00 | NOAA-21 | NORMANDIA | RORAIMA | Brasil | 1400407 | 14 | 33 | nan | nan | nan | Amazônia | 1.6 |
| 761ed119-9e4a-388f-824a-afa79b4e6b1c | 3.55776 | -60.3248 | 2025-02-18 04:36:00 | NOAA-21 | NORMANDIA | RORAIMA | Brasil | 1400407 | 14 | 33 | nan | nan | nan | Amazônia | 3.3 |
| b5304f55-a315-3e01-a330-c0cc63fff472 | 3.55871 | -60.32674 | 2025-02-18 04:36:00 | NOAA-21 | NORMANDIA | RORAIMA | Brasil | 1400407 | 14 | 33 | nan | nan | nan | Amazônia | 1.6 |
| 1af3dbae-6d47-3590-b882-f78a0278768f | -1.57083 | -54.02287 | 2025-02-18 04:38:00 | NOAA-21 | MONTE ALEGRE | PARÁ | Brasil | 1504802 | 15 | 33 | nan | nan | nan | Amazônia | 1.2 |
| e73db067-0a73-32ea-9311-c855dbf75ee4 | -1.56602 | -54.02607 | 2025-02-18 04:38:00 | NOAA-21 | MONTE ALEGRE | PARÁ | Brasil | 1504802 | 15 | 33 | nan | nan | nan | Amazônia | 1.2 |
| 02b7f865-617a-35b8-96fc-d2008f0db58d | -2.50408 | -54.13223 | 2025-02-18 04:38:00 | NOAA-21 | PRAINHA | PARÁ | Brasil | 1506005 | 15 | 33 | nan | nan | nan | Amazônia | 1.3 |
| 096225e3-366a-3025-b312-cb911c6484bb | -2.61544 | -54.22061 | 2025-02-18 04:38:00 | NOAA-21 | SANTARÉM | PARÁ | Brasil | 1506807 | 15 | 33 | nan | nan | nan | Amazônia | 1.7 |
| 0c05829d-8cc6-3cd8-bf82-58389b12355c | -12.32715 | -52.48193 | 2025-02-18 04:40:00 | NOAA-21 | QUERÊNCIA | MATO GROSSO | Brasil | 5107065 | 51 | 33 | nan | nan | nan | Amazônia | 1.5 |
| 0c985131-7138-3335-ad46-72ccbd3cd50b | -12.70413 | -44.67592 | 2025-02-18 04:40:00 | NOAA-21 | SÃO DESIDÉRIO | BAHIA | Brasil | 2928901 | 29 | 33 | nan | nan | nan | Cerrado | 0.8 |
| 1d8e8138-8e4c-371d-8e32-d8c58323ade3 | -11.45362 | -52.92122 | 2025-02-18 04:40:00 | NOAA-21 | SÃO FÉLIX DO ARAGUAIA | MATO GROSSO | Brasil | 5107859 | 51 | 33 | nan | nan | nan | Amazônia | 1.5 |
| cc5dc3e1-b84c-3ec4-85bc-c7073b70686b | -12.33331 | -52.48677 | 2025-02-18 04:40:00 | NOAA-21 | QUERÊNCIA | MATO GROSSO | Brasil | 5107065 | 51 | 33 | nan | nan | nan | Amazônia | 1.7 |
| a612dec4-17b1-32e4-97bb-d932802094da | -7.55267 | -45.8726 | 2025-02-18 04:40:00 | NOAA-21 | BALSAS | MARANHÃO | Brasil | 2101400 | 21 | 33 | nan | nan | nan | Cerrado | 0.9 |
| ab06c9bb-2bb6-3ffa-a022-9da379afc97d | -13.28197 | -39.80124 | 2025-02-18 04:40:00 | NOAA-21 | SANTA INÊS | BAHIA | Brasil | 2927903 | 29 | 33 | nan | nan | nan | Mata Atlântica | 7.4 |
| 40f9d041-7de4-3f76-9015-0e0edcb1b912 | -10.60978 | -45.10424 | 2025-02-18 04:40:00 | NOAA-21 | CORRENTE | PIAUÍ | Brasil | 2202901 | 22 | 33 | nan | nan | nan | Cerrado | 3.3 |
| 46c437c3-b2c5-38f1-a664-e151881f4aa7 | -10.60928 | -45.10796 | 2025-02-18 04:40:00 | NOAA-21 | CORRENTE | PIAUÍ | Brasil | 2202901 | 22 | 33 | nan | nan | nan | Cerrado | 3.3 |


[Clique aqui para ver as próximas entradas](README5.md)
