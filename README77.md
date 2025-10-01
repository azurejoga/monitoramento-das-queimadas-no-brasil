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

## Dados Diários - Página 77

| ID | Latitude | Longitude | Data/Hora GMT | Satélite | Município | Estado | País | Município ID | Estado ID | País ID | Dias sem Chuva | Precipitação | Risco de Fogo | Bioma | FRP |
|----|----------|-----------|---------------|----------|-----------|--------|------|--------------|-----------|---------|----------------|--------------|----------------|-------|-----|
| a1829bae-4a10-381d-a3fb-03ef2d97b234 | -21.34142 | -45.87864 | 2025-10-01 04:23:00 | NOAA-21 | ALFENAS | MINAS GERAIS | Brasil | 3101607 | 31 | 33 | nan | nan | nan | Mata Atlântica | 0.8 |
| 83d6c69d-7e26-3ccb-b744-2782c01bdf64 | -19.69668 | -43.68489 | 2025-10-01 04:23:00 | NOAA-21 | TAQUARAÇU DE MINAS | MINAS GERAIS | Brasil | 3168309 | 31 | 33 | nan | nan | nan | Cerrado | 2.2 |
| 46e88268-5216-3bce-87ac-34e6038b2374 | -21.66235 | -45.33889 | 2025-10-01 04:23:00 | NOAA-21 | TRÊS CORAÇÕES | MINAS GERAIS | Brasil | 3169307 | 31 | 33 | nan | nan | nan | Mata Atlântica | 4.7 |
| 07e2dc0c-895c-3342-9413-38cd689bced9 | -19.96626 | -43.71818 | 2025-10-01 04:23:00 | NOAA-21 | CAETÉ | MINAS GERAIS | Brasil | 3110004 | 31 | 33 | nan | nan | nan | Mata Atlântica | 1.7 |
| d9671232-166a-3c32-9d11-d64ef2c5c8ff | -19.87008 | -42.5916 | 2025-10-01 04:23:00 | NOAA-21 | DIONÍSIO | MINAS GERAIS | Brasil | 3121803 | 31 | 33 | nan | nan | nan | Mata Atlântica | 1.7 |
| da6c491d-9059-34fa-9d3d-ee0012969a4e | -22.28794 | -47.7328 | 2025-10-01 04:23:00 | NOAA-21 | ITIRAPINA | SÃO PAULO | Brasil | 3523602 | 35 | 33 | nan | nan | nan | Cerrado | 1.8 |
| c602915f-1925-370a-9953-60863cec2bf7 | -22.26985 | -46.72728 | 2025-10-01 04:23:00 | NOAA-21 | ESPÍRITO SANTO DO PINHAL | SÃO PAULO | Brasil | 3515186 | 35 | 33 | nan | nan | nan | Mata Atlântica | 1.4 |
| 1b03a6a5-4247-39a6-858e-43f19d6d05cb | -20.62613 | -46.20781 | 2025-10-01 04:23:00 | NOAA-21 | CAPITÓLIO | MINAS GERAIS | Brasil | 3112802 | 31 | 33 | nan | nan | nan | Cerrado | 1.3 |
| 02d29b18-fcae-3e36-94fa-66675c79fd23 | -18.80766 | -47.54936 | 2025-10-01 04:23:00 | NOAA-21 | MONTE CARMELO | MINAS GERAIS | Brasil | 3143104 | 31 | 33 | nan | nan | nan | Cerrado | 2.2 |
| 33c62dfc-6369-3dc9-93f2-f0cc91ed3399 | -17.73772 | -46.63802 | 2025-10-01 04:23:00 | NOAA-21 | VAZANTE | MINAS GERAIS | Brasil | 3171006 | 31 | 33 | nan | nan | nan | Cerrado | 1.9 |
| bc34b1e3-c0fc-3d50-9fc2-ea5d7039e9f4 | -21.4729 | -43.90137 | 2025-10-01 04:23:00 | NOAA-21 | IBERTIOGA | MINAS GERAIS | Brasil | 3129400 | 31 | 33 | nan | nan | nan | Mata Atlântica | 4.1 |
| d8e838dd-4966-3225-a6c3-b92021eed3fc | -20.03734 | -44.53529 | 2025-10-01 04:23:00 | NOAA-21 | ITAÚNA | MINAS GERAIS | Brasil | 3133808 | 31 | 33 | nan | nan | nan | Mata Atlântica | 1.1 |
| 56e6c655-32ed-3073-a20a-18a33cb5a576 | -20.12707 | -46.33529 | 2025-10-01 04:23:00 | NOAA-21 | SÃO ROQUE DE MINAS | MINAS GERAIS | Brasil | 3164308 | 31 | 33 | nan | nan | nan | Cerrado | 8.4 |
| 63ca5d7b-5406-3429-94f7-d497fe0a97f1 | -17.96196 | -45.01936 | 2025-10-01 04:23:00 | NOAA-21 | LASSANCE | MINAS GERAIS | Brasil | 3138104 | 31 | 33 | nan | nan | nan | Cerrado | 1.8 |
| 91f871f2-9b64-3b29-a180-552cbc90c305 | -20.1309 | -44.0139 | 2025-10-01 04:23:00 | NOAA-21 | BRUMADINHO | MINAS GERAIS | Brasil | 3109006 | 31 | 33 | nan | nan | nan | Mata Atlântica | 1.5 |
| 393e96e3-8daf-3afa-8a55-7bf9440d35fd | -20.61025 | -43.80587 | 2025-10-01 04:23:00 | NOAA-21 | CONSELHEIRO LAFAIETE | MINAS GERAIS | Brasil | 3118304 | 31 | 33 | nan | nan | nan | Mata Atlântica | 1.1 |
| 4b688ba4-9b30-3472-9312-4ac4bdff88df | -22.58906 | -46.79435 | 2025-10-01 04:23:00 | NOAA-21 | AMPARO | SÃO PAULO | Brasil | 3501905 | 35 | 33 | nan | nan | nan | Mata Atlântica | 0.5 |
| e8085540-a7a1-30ab-b276-6ca5045394f5 | -22.65236 | -46.76524 | 2025-10-01 04:23:00 | NOAA-21 | AMPARO | SÃO PAULO | Brasil | 3501905 | 35 | 33 | nan | nan | nan | Mata Atlântica | 1.1 |
| 25cf6001-0b7c-3a29-a39a-7f8e2d748dec | -23.22734 | -49.40643 | 2025-10-01 04:23:00 | NOAA-21 | PIRAJU | SÃO PAULO | Brasil | 3538808 | 35 | 33 | nan | nan | nan | Mata Atlântica | 1.3 |
| ebe15add-fef2-37d0-b746-a4645acf3844 | -22.27324 | -46.72786 | 2025-10-01 04:23:00 | NOAA-21 | ESPÍRITO SANTO DO PINHAL | SÃO PAULO | Brasil | 3515186 | 35 | 33 | nan | nan | nan | Mata Atlântica | 1.4 |
| 04d98a4b-1053-31aa-8b21-9770655e149e | -23.09797 | -47.31192 | 2025-10-01 04:23:00 | NOAA-21 | ELIAS FAUSTO | SÃO PAULO | Brasil | 3514908 | 35 | 33 | nan | nan | nan | Mata Atlântica | 0.6 |
| 29557760-0d3a-3fc2-ac9b-f5d7ab27a40f | -17.85864 | -46.15428 | 2025-10-01 04:23:00 | NOAA-21 | JOÃO PINHEIRO | MINAS GERAIS | Brasil | 3136306 | 31 | 33 | nan | nan | nan | Cerrado | 1.8 |
| 07970be4-ee38-3c94-892a-d2792bd2eb29 | -19.89044 | -42.6249 | 2025-10-01 04:23:00 | NOAA-21 | DIONÍSIO | MINAS GERAIS | Brasil | 3121803 | 31 | 33 | nan | nan | nan | Mata Atlântica | 1.8 |
| c168d88a-9168-38dd-8159-8b03459a3f53 | -22.41338 | -43.16392 | 2025-10-01 04:23:00 | NOAA-21 | PETRÓPOLIS | RIO DE JANEIRO | Brasil | 3303906 | 33 | 33 | nan | nan | nan | Mata Atlântica | 2.0 |
| d19e4546-4444-305d-a512-6ec905aef477 | -19.84809 | -43.81892 | 2025-10-01 04:23:00 | NOAA-21 | SABARÁ | MINAS GERAIS | Brasil | 3156700 | 31 | 33 | nan | nan | nan | Mata Atlântica | 1.8 |
| ec563fa3-ba1c-3c0b-ab73-ddefec526ce2 | -23.22794 | -49.40266 | 2025-10-01 04:23:00 | NOAA-21 | PIRAJU | SÃO PAULO | Brasil | 3538808 | 35 | 33 | nan | nan | nan | Mata Atlântica | 1.3 |
| d3ac0255-1d96-368c-a1df-2c48d5215bf7 | -22.74479 | -46.29403 | 2025-10-01 04:23:00 | NOAA-21 | EXTREMA | MINAS GERAIS | Brasil | 3125101 | 31 | 33 | nan | nan | nan | Mata Atlântica | 0.5 |
| 037e9cad-7be1-3ac6-8b8f-5f2e9a082dfd | -20.02645 | -44.53383 | 2025-10-01 04:23:00 | NOAA-21 | ITAÚNA | MINAS GERAIS | Brasil | 3133808 | 31 | 33 | nan | nan | nan | Mata Atlântica | 1.2 |
| 2e7b78ff-598c-3dff-b62f-550f49d51186 | -18.60933 | -43.27283 | 2025-10-01 04:23:00 | NOAA-21 | SERRO | MINAS GERAIS | Brasil | 3167103 | 31 | 33 | nan | nan | nan | Mata Atlântica | 3.2 |
| b3e88685-757d-30a9-b599-7554efe907fc | -21.42713 | -44.16945 | 2025-10-01 04:23:00 | NOAA-21 | PIEDADE DO RIO GRANDE | MINAS GERAIS | Brasil | 3150307 | 31 | 33 | nan | nan | nan | Mata Atlântica | 1.9 |
| 19a07bd4-ae68-3aed-9e64-3fa3d0c43591 | -22.25369 | -43.43784 | 2025-10-01 04:23:00 | NOAA-21 | VASSOURAS | RIO DE JANEIRO | Brasil | 3306206 | 33 | 33 | nan | nan | nan | Mata Atlântica | 1.3 |
| 2a1b3301-1a6b-3617-aad4-4687ab1573a3 | -20.58509 | -45.88421 | 2025-10-01 04:23:00 | NOAA-21 | PIMENTA | MINAS GERAIS | Brasil | 3150505 | 31 | 33 | nan | nan | nan | Cerrado | 6.1 |
| bcaba509-14e0-3903-a4ca-9a409229d07f | -18.3257 | -44.77012 | 2025-10-01 04:23:00 | NOAA-21 | CORINTO | MINAS GERAIS | Brasil | 3119104 | 31 | 33 | nan | nan | nan | Cerrado | 2.6 |
| 0efcca2a-9bd1-3adc-9ce0-bb1c7c97b3c5 | -20.63063 | -46.17657 | 2025-10-01 04:23:00 | NOAA-21 | CAPITÓLIO | MINAS GERAIS | Brasil | 3112802 | 31 | 33 | nan | nan | nan | Cerrado | 0.8 |
| 66483cf7-6652-3a62-8691-72e2a95b4d43 | -18.7083 | -49.16943 | 2025-10-01 04:23:00 | NOAA-21 | CANÁPOLIS | MINAS GERAIS | Brasil | 3111804 | 31 | 33 | nan | nan | nan | Cerrado | 3.1 |
| e3dc4e77-f7f4-3618-beaa-3e986721073c | -20.62442 | -46.19551 | 2025-10-01 04:23:00 | NOAA-21 | CAPITÓLIO | MINAS GERAIS | Brasil | 3112802 | 31 | 33 | nan | nan | nan | Cerrado | 7.1 |
| 5e95c537-8664-39c0-ae38-ca2b3e3aef7c | -22.7754 | -47.61081 | 2025-10-01 04:23:00 | NOAA-21 | PIRACICABA | SÃO PAULO | Brasil | 3538709 | 35 | 33 | nan | nan | nan | Mata Atlântica | 3.8 |
| 61743f50-31cc-3a90-a29c-ff5d2acaf2eb | -21.88499 | -48.14426 | 2025-10-01 04:23:00 | NOAA-21 | ARARAQUARA | SÃO PAULO | Brasil | 3503208 | 35 | 33 | nan | nan | nan | Cerrado | 0.6 |
| f4630118-7c1d-3888-80fc-abe0528f04c9 | -22.76681 | -45.78243 | 2025-10-01 04:23:00 | NOAA-21 | SAPUCAÍ-MIRIM | MINAS GERAIS | Brasil | 3165404 | 31 | 33 | nan | nan | nan | Mata Atlântica | 3.9 |
| 5257f9f1-f1c9-3e3d-abdd-91e63b2d07b6 | -22.62995 | -49.05444 | 2025-10-01 04:23:00 | NOAA-21 | AGUDOS | SÃO PAULO | Brasil | 3500709 | 35 | 33 | nan | nan | nan | Cerrado | 19.1 |
| 2f0117f9-1fd9-3403-a2a1-d6a8cc8c2b56 | -20.22284 | -43.44391 | 2025-10-01 04:23:00 | NOAA-21 | MARIANA | MINAS GERAIS | Brasil | 3140001 | 31 | 33 | nan | nan | nan | Mata Atlântica | 22.7 |
| d5b20786-76c9-3e20-8002-89b372d68df9 | -19.693 | -46.35571 | 2025-10-01 04:23:00 | NOAA-21 | PRATINHA | MINAS GERAIS | Brasil | 3153004 | 31 | 33 | nan | nan | nan | Cerrado | 1.0 |
| 8a505fd7-e8c4-36bf-98cd-17078bd908e4 | -17.95906 | -45.0148 | 2025-10-01 04:23:00 | NOAA-21 | LASSANCE | MINAS GERAIS | Brasil | 3138104 | 31 | 33 | nan | nan | nan | Cerrado | 1.8 |
| 2bf6b6e7-c6e8-30a3-b3f0-53fdb12221ae | -20.60679 | -46.19718 | 2025-10-01 04:23:00 | NOAA-21 | CAPITÓLIO | MINAS GERAIS | Brasil | 3112802 | 31 | 33 | nan | nan | nan | Cerrado | 2.0 |
| 1be9de9b-5663-32d2-ab84-eff59b598d8b | -19.86342 | -42.57931 | 2025-10-01 04:23:00 | NOAA-21 | DIONÍSIO | MINAS GERAIS | Brasil | 3121803 | 31 | 33 | nan | nan | nan | Mata Atlântica | 1.3 |
| 1b78593b-6317-3df5-be15-17d2f74c0cf3 | -17.86392 | -47.14499 | 2025-10-01 04:23:00 | NOAA-21 | GUARDA-MOR | MINAS GERAIS | Brasil | 3128600 | 31 | 33 | nan | nan | nan | Cerrado | 3.0 |
| faaf0150-3eb3-386d-97bd-addf2ed49502 | -18.32513 | -44.77425 | 2025-10-01 04:23:00 | NOAA-21 | CORINTO | MINAS GERAIS | Brasil | 3119104 | 31 | 33 | nan | nan | nan | Cerrado | 2.6 |
| c285529e-ba11-3804-99e8-9bf079700d76 | -19.88881 | -42.60567 | 2025-10-01 04:23:00 | NOAA-21 | SÃO JOSÉ DO GOIABAL | MINAS GERAIS | Brasil | 3163409 | 31 | 33 | nan | nan | nan | Mata Atlântica | 0.8 |
| 6ce8e024-f714-3a8c-8f4b-b19e61b9e640 | -20.63404 | -46.17707 | 2025-10-01 04:23:00 | NOAA-21 | CAPITÓLIO | MINAS GERAIS | Brasil | 3112802 | 31 | 33 | nan | nan | nan | Cerrado | 2.8 |
| 7d6706f4-23a4-359a-927a-93a8b577c053 | -19.84274 | -46.71579 | 2025-10-01 04:23:00 | NOAA-21 | IBIÁ | MINAS GERAIS | Brasil | 3129509 | 31 | 33 | nan | nan | nan | Cerrado | 1.4 |
| a898ca55-9f04-32c2-91ad-6f9ad6c03a0f | -22.62665 | -49.05384 | 2025-10-01 04:23:00 | NOAA-21 | AGUDOS | SÃO PAULO | Brasil | 3500709 | 35 | 33 | nan | nan | nan | Cerrado | 22.5 |
| b8fddba0-85ed-3f8a-8424-21fb759cfb82 | -18.49337 | -44.03735 | 2025-10-01 04:23:00 | NOAA-21 | SANTO HIPÓLITO | MINAS GERAIS | Brasil | 3160603 | 31 | 33 | nan | nan | nan | Cerrado | 2.3 |
| 3cf6fdae-41eb-3e19-80b2-91ce677552e7 | -20.61069 | -43.80431 | 2025-10-01 04:23:00 | NOAA-21 | CONSELHEIRO LAFAIETE | MINAS GERAIS | Brasil | 3118304 | 31 | 33 | nan | nan | nan | Mata Atlântica | 1.9 |
| d533d1ac-70d6-38de-832d-94caa651669a | -19.52062 | -43.89711 | 2025-10-01 04:23:00 | NOAA-21 | JABOTICATUBAS | MINAS GERAIS | Brasil | 3134608 | 31 | 33 | nan | nan | nan | Cerrado | 5.6 |
| e3d53a92-7266-310f-ba1a-6a393a1a7ead | -20.43287 | -43.5969 | 2025-10-01 04:23:00 | NOAA-21 | OURO PRETO | MINAS GERAIS | Brasil | 3146107 | 31 | 33 | nan | nan | nan | Mata Atlântica | 1.0 |
| 5288509b-3459-358e-867a-55d16a0c8f7f | -22.09707 | -47.80379 | 2025-10-01 04:23:00 | NOAA-21 | SÃO CARLOS | SÃO PAULO | Brasil | 3548906 | 35 | 33 | nan | nan | nan | Cerrado | 4.5 |
| 8127c3e9-cfb5-36f6-ad90-9ac262e06250 | -22.05937 | -43.07408 | 2025-10-01 04:23:00 | NOAA-21 | CHIADOR | MINAS GERAIS | Brasil | 3116209 | 31 | 33 | nan | nan | nan | Mata Atlântica | 0.9 |
| 8aeac304-035c-31e2-ba20-874c165e1fb1 | -22.11484 | -44.70186 | 2025-10-01 04:23:00 | NOAA-21 | BAEPENDI | MINAS GERAIS | Brasil | 3104908 | 31 | 33 | nan | nan | nan | Mata Atlântica | 3.7 |
| 3263822e-3ed8-3566-8c0c-c836a6a1794f | -19.81202 | -44.07433 | 2025-10-01 04:23:00 | NOAA-21 | RIBEIRÃO DAS NEVES | MINAS GERAIS | Brasil | 3154606 | 31 | 33 | nan | nan | nan | Cerrado | 1.4 |
| 70ef90f6-7327-3c6a-b8ca-213c8ad8329b | -21.88715 | -48.15223 | 2025-10-01 04:23:00 | NOAA-21 | ARARAQUARA | SÃO PAULO | Brasil | 3503208 | 35 | 33 | nan | nan | nan | Cerrado | 1.6 |
| 383e31bc-dc4e-3adc-b6e9-4ce5b269b4e8 | -18.95716 | -45.37994 | 2025-10-01 04:23:00 | NOAA-21 | PAINEIRAS | MINAS GERAIS | Brasil | 3146404 | 31 | 33 | nan | nan | nan | Cerrado | 1.1 |
| e8a05e72-768b-38f9-9af8-2fe22c80466d | -20.47936 | -43.94789 | 2025-10-01 04:23:00 | NOAA-21 | CONGONHAS | MINAS GERAIS | Brasil | 3118007 | 31 | 33 | nan | nan | nan | Mata Atlântica | 5.0 |
| afada5db-49d5-3540-b0bd-1560bd23860e | -21.97516 | -47.88989 | 2025-10-01 04:23:00 | NOAA-21 | SÃO CARLOS | SÃO PAULO | Brasil | 3548906 | 35 | 33 | nan | nan | nan | Cerrado | 2.4 |
| 05ca3a7a-20fd-35e5-a96a-d639a68addf4 | -21.97847 | -47.89047 | 2025-10-01 04:23:00 | NOAA-21 | SÃO CARLOS | SÃO PAULO | Brasil | 3548906 | 35 | 33 | nan | nan | nan | Cerrado | 2.4 |
| 3e5af2a9-4ee3-3da0-8cdc-df6bdd60cc5b | -22.27435 | -46.7202 | 2025-10-01 04:23:00 | NOAA-21 | ESPÍRITO SANTO DO PINHAL | SÃO PAULO | Brasil | 3515186 | 35 | 33 | nan | nan | nan | Mata Atlântica | 2.1 |
| e2a88012-7fd9-339b-91e3-b02b9c2bc3ed | -18.16406 | -46.10782 | 2025-10-01 04:23:00 | NOAA-21 | PRESIDENTE OLEGÁRIO | MINAS GERAIS | Brasil | 3153400 | 31 | 33 | nan | nan | nan | Cerrado | 8.4 |
| 7fd85051-5426-3eb9-972f-d8b64f9cd6e7 | -19.89399 | -42.62917 | 2025-10-01 04:23:00 | NOAA-21 | DIONÍSIO | MINAS GERAIS | Brasil | 3121803 | 31 | 33 | nan | nan | nan | Mata Atlântica | 0.9 |
| 1109fe5b-0c9b-390e-bc80-0300dcb31016 | -23.2045 | -45.80122 | 2025-10-01 04:23:00 | NOAA-21 | SÃO JOSÉ DOS CAMPOS | SÃO PAULO | Brasil | 3549904 | 35 | 33 | nan | nan | nan | Mata Atlântica | 2.6 |
| 89762d44-b3d1-3b9b-8086-9f9b5812026c | -22.58028 | -46.7779 | 2025-10-01 04:23:00 | NOAA-21 | AMPARO | SÃO PAULO | Brasil | 3501905 | 35 | 33 | nan | nan | nan | Mata Atlântica | 7.1 |
| 67057ad6-55c0-3cd3-87ab-f33af32920a5 | -18.95986 | -43.70856 | 2025-10-01 04:23:00 | NOAA-21 | CONGONHAS DO NORTE | MINAS GERAIS | Brasil | 3118106 | 31 | 33 | nan | nan | nan | Cerrado | 3.2 |
| c7c1d36e-7d59-3842-ab92-f3bc5ec79daf | -19.8294 | -46.71339 | 2025-10-01 04:23:00 | NOAA-21 | IBIÁ | MINAS GERAIS | Brasil | 3129509 | 31 | 33 | nan | nan | nan | Cerrado | 0.9 |
| e2a1a9fc-7dda-3751-a1fa-c54108fedd5d | -22.42906 | -46.97305 | 2025-10-01 04:23:00 | NOAA-21 | MOGI MIRIM | SÃO PAULO | Brasil | 3530805 | 35 | 33 | nan | nan | nan | Cerrado | 0.3 |
| 2301640f-38c2-3658-a77a-c40778bf0efb | -20.62158 | -46.21521 | 2025-10-01 04:23:00 | NOAA-21 | CAPITÓLIO | MINAS GERAIS | Brasil | 3112802 | 31 | 33 | nan | nan | nan | Cerrado | 2.8 |
| ca867af9-2bd1-3c46-b629-ee897c040689 | -21.28405 | -45.04794 | 2025-10-01 04:23:00 | NOAA-21 | LAVRAS | MINAS GERAIS | Brasil | 3138203 | 31 | 33 | nan | nan | nan | Mata Atlântica | 0.7 |
| ce5c44f3-6eda-305f-9cf6-08ca102f726f | -19.95398 | -43.66462 | 2025-10-01 04:23:00 | NOAA-21 | CAETÉ | MINAS GERAIS | Brasil | 3110004 | 31 | 33 | nan | nan | nan | Mata Atlântica | 2.4 |
| 9fd488c7-5b2a-3a1c-96d3-753630b4ea91 | -18.27661 | -43.71138 | 2025-10-01 04:23:00 | NOAA-21 | DIAMANTINA | MINAS GERAIS | Brasil | 3121605 | 31 | 33 | nan | nan | nan | Cerrado | 1.9 |
| c228886e-964a-3ab2-bdf6-e1ba7f25f892 | -22.25898 | -43.42791 | 2025-10-01 04:23:00 | NOAA-21 | VASSOURAS | RIO DE JANEIRO | Brasil | 3306206 | 33 | 33 | nan | nan | nan | Mata Atlântica | 1.4 |
| 5a1df645-8b7c-3258-8da5-a2d6d967ada8 | -17.95972 | -45.03507 | 2025-10-01 04:23:00 | NOAA-21 | LASSANCE | MINAS GERAIS | Brasil | 3138104 | 31 | 33 | nan | nan | nan | Cerrado | 2.6 |
| f6cb2075-ec35-39ad-a8e4-5471410bdc55 | -18.41993 | -43.81334 | 2025-10-01 04:23:00 | NOAA-21 | GOUVEIA | MINAS GERAIS | Brasil | 3127602 | 31 | 33 | nan | nan | nan | Cerrado | 0.4 |
| 10184b5c-5c68-3bf0-82ed-452a69bd7cd4 | -22.64954 | -46.76072 | 2025-10-01 04:23:00 | NOAA-21 | AMPARO | SÃO PAULO | Brasil | 3501905 | 35 | 33 | nan | nan | nan | Mata Atlântica | 0.9 |
| 3433c221-f3d9-3060-a390-01693d4197fc | -20.48074 | -43.94489 | 2025-10-01 04:23:00 | NOAA-21 | CONGONHAS | MINAS GERAIS | Brasil | 3118007 | 31 | 33 | nan | nan | nan | Mata Atlântica | 5.4 |
| cf370c06-10a3-3524-9565-2511115baa5c | -21.79958 | -48.18983 | 2025-10-01 04:23:00 | NOAA-21 | ARARAQUARA | SÃO PAULO | Brasil | 3503208 | 35 | 33 | nan | nan | nan | Cerrado | 2.0 |
| 42996f1d-d06a-3bee-a36a-2fd52ba7b505 | -22.53749 | -44.60683 | 2025-10-01 04:23:00 | NOAA-21 | ITATIAIA | RIO DE JANEIRO | Brasil | 3302254 | 33 | 33 | nan | nan | nan | Mata Atlântica | 1.7 |
| 62a72e63-b8a0-3b3d-9644-c4fa3e2a18ac | -22.41173 | -43.16892 | 2025-10-01 04:23:00 | NOAA-21 | PETRÓPOLIS | RIO DE JANEIRO | Brasil | 3303906 | 33 | 33 | nan | nan | nan | Mata Atlântica | 6.0 |
| a9516546-c754-3b33-9cde-cdd25bce8f4d | -20.22868 | -43.8914 | 2025-10-01 04:23:00 | NOAA-21 | ITABIRITO | MINAS GERAIS | Brasil | 3131901 | 31 | 33 | nan | nan | nan | Mata Atlântica | 2.0 |
| 072648c5-f393-3ad7-969b-a3d6f47b4ffd | -20.59598 | -45.88185 | 2025-10-01 04:23:00 | NOAA-21 | PIMENTA | MINAS GERAIS | Brasil | 3150505 | 31 | 33 | nan | nan | nan | Cerrado | 6.5 |
| ed0c0087-ab29-35bb-bd12-e432aaa4bf86 | -22.28737 | -47.73655 | 2025-10-01 04:23:00 | NOAA-21 | ITIRAPINA | SÃO PAULO | Brasil | 3523602 | 35 | 33 | nan | nan | nan | Cerrado | 1.8 |
| a9e944c3-14d0-3e2b-bc7f-cfe481019536 | -20.61028 | -46.07362 | 2025-10-01 04:23:00 | NOAA-21 | CAPITÓLIO | MINAS GERAIS | Brasil | 3112802 | 31 | 33 | nan | nan | nan | Cerrado | 0.6 |
| c388578f-1dff-3eca-81e5-f2b39100693f | -23.3347 | -46.86613 | 2025-10-01 04:23:00 | NOAA-21 | CAJAMAR | SÃO PAULO | Brasil | 3509205 | 35 | 33 | nan | nan | nan | Mata Atlântica | 0.6 |
| b58a87ee-a74e-3a41-b5e1-8c85859efd34 | -19.89552 | -42.62558 | 2025-10-01 04:23:00 | NOAA-21 | DIONÍSIO | MINAS GERAIS | Brasil | 3121803 | 31 | 33 | nan | nan | nan | Mata Atlântica | 1.3 |
| 9eb0b252-03d5-3ca4-8b1b-8df9c02a534e | -20.62782 | -46.2202 | 2025-10-01 04:23:00 | NOAA-21 | CAPITÓLIO | MINAS GERAIS | Brasil | 3112802 | 31 | 33 | nan | nan | nan | Cerrado | 3.7 |
| a8caba63-bfdf-3fef-a689-83ea7a9101ab | -20.62048 | -46.22283 | 2025-10-01 04:23:00 | NOAA-21 | CAPITÓLIO | MINAS GERAIS | Brasil | 3112802 | 31 | 33 | nan | nan | nan | Cerrado | 1.2 |
| 18e7cc82-2522-35c4-ad78-cfc328353016 | -20.83114 | -43.25776 | 2025-10-01 04:23:00 | NOAA-21 | BRÁS PIRES | MINAS GERAIS | Brasil | 3108701 | 31 | 33 | nan | nan | nan | Mata Atlântica | 0.9 |
| fa383562-37e7-3b10-b696-833f3698c187 | -20.13026 | -44.01862 | 2025-10-01 04:23:00 | NOAA-21 | BRUMADINHO | MINAS GERAIS | Brasil | 3109006 | 31 | 33 | nan | nan | nan | Mata Atlântica | 1.5 |
| 5925d55c-282d-3eb5-a7c1-9d8840f8cd07 | -21.9939 | -48.29631 | 2025-10-01 04:23:00 | NOAA-21 | TRABIJU | SÃO PAULO | Brasil | 3554755 | 35 | 33 | nan | nan | nan | Cerrado | 1.0 |
| 0c5ac284-fd97-397c-a7d8-18b2cebeb4a3 | -22.10708 | -47.80478 | 2025-10-01 04:23:00 | NOAA-21 | SÃO CARLOS | SÃO PAULO | Brasil | 3548906 | 35 | 33 | nan | nan | nan | Cerrado | 3.1 |
| e89d6a0a-fa00-3afd-a295-e11d2f0958c8 | -23.21265 | -47.40993 | 2025-10-01 04:23:00 | NOAA-21 | ITU | SÃO PAULO | Brasil | 3523909 | 35 | 33 | nan | nan | nan | Mata Atlântica | 0.8 |
| aece861e-b9af-367c-8496-b9bf305652a9 | -20.28239 | -46.23689 | 2025-10-01 04:23:00 | NOAA-21 | SÃO ROQUE DE MINAS | MINAS GERAIS | Brasil | 3164308 | 31 | 33 | nan | nan | nan | Cerrado | 0.4 |
| 742a9764-419e-3f74-b394-e32f503fada4 | -19.862 | -42.59053 | 2025-10-01 04:23:00 | NOAA-21 | DIONÍSIO | MINAS GERAIS | Brasil | 3121803 | 31 | 33 | nan | nan | nan | Mata Atlântica | 3.9 |
| 053e4ceb-5efc-3f74-8b70-00b25788f235 | -22.64615 | -46.76006 | 2025-10-01 04:23:00 | NOAA-21 | AMPARO | SÃO PAULO | Brasil | 3501905 | 35 | 33 | nan | nan | nan | Mata Atlântica | 0.9 |


[Clique aqui para ver as próximas entradas](README78.md)
