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

## Dados Diários - Página 91

| ID | Latitude | Longitude | Data/Hora GMT | Satélite | Município | Estado | País | Município ID | Estado ID | País ID | Dias sem Chuva | Precipitação | Risco de Fogo | Bioma | FRP |
|----|----------|-----------|---------------|----------|-----------|--------|------|--------------|-----------|---------|----------------|--------------|----------------|-------|-----|
| 88050f0f-a296-3e41-b687-3d6434e03618 | -12.2897 | -50.2712 | 2026-09-28 16:20:00 | GOES-19 | FORMOSO DO ARAGUAIA | TOCANTINS | Brasil | 1708205 | 17 | 33 | nan | nan | nan | Cerrado | 90.5 |
| 2c5d3b2d-d9ff-34f7-bb03-fff21d6ecf34 | -10.9156 | -50.6845 | 2026-09-28 16:20:00 | GOES-19 | LUCIARA | MATO GROSSO | Brasil | 5105309 | 51 | 33 | nan | nan | nan | Cerrado | 94.3 |
| 9259b7ec-79ae-349e-9f77-a426ed2a5889 | -10.9536 | -50.6805 | 2026-09-28 16:20:00 | GOES-19 | LUCIARA | MATO GROSSO | Brasil | 5105309 | 51 | 33 | nan | nan | nan | Cerrado | 139.7 |
| 38a7d814-f0d4-3b1c-a63f-6e4b1156d647 | -10.9154 | -50.7059 | 2026-09-28 16:20:00 | GOES-19 | LUCIARA | MATO GROSSO | Brasil | 5105309 | 51 | 33 | nan | nan | nan | Cerrado | 146.3 |
| df24505f-82ff-3ee3-a636-fc72765e9c7b | -10.2565 | -50.5185 | 2026-09-28 16:20:00 | GOES-19 | SANTA TEREZINHA | MATO GROSSO | Brasil | 5107776 | 51 | 33 | nan | nan | nan | Amazônia | 90.0 |
| 11612afd-e416-3688-be4f-d7dcf991936a | -11.7129 | -50.6394 | 2026-09-28 16:20:00 | GOES-19 | FORMOSO DO ARAGUAIA | TOCANTINS | Brasil | 1708205 | 17 | 33 | nan | nan | nan | Cerrado | 79.6 |
| bbc6ea12-49fa-34d0-adba-4a82221a22a9 | -11.0767 | -51.3674 | 2026-09-28 16:20:00 | GOES-19 | LUCIARA | MATO GROSSO | Brasil | 5105309 | 51 | 33 | nan | nan | nan | Cerrado | 105.0 |
| 2654d461-56f9-38ac-9725-bbfdccab29b7 | -11.7141 | -50.5538 | 2026-09-28 16:20:00 | GOES-19 | FORMOSO DO ARAGUAIA | TOCANTINS | Brasil | 1708205 | 17 | 33 | nan | nan | nan | Cerrado | 120.6 |
| b2aa7ef1-1942-3264-b1f5-a982a9432822 | -12.1557 | -50.3089 | 2026-09-28 16:20:00 | GOES-19 | FORMOSO DO ARAGUAIA | TOCANTINS | Brasil | 1708205 | 17 | 33 | nan | nan | nan | Cerrado | 95.6 |
| 514c5eab-19cb-362c-9f51-3f9c3d9e8651 | -12.2307 | -50.3858 | 2026-09-28 16:20:00 | GOES-19 | FORMOSO DO ARAGUAIA | TOCANTINS | Brasil | 1708205 | 17 | 33 | nan | nan | nan | Cerrado | 86.2 |
| 7566570c-31c6-3c60-a1db-0d96a13c7eaa | -11.5625 | -50.5283 | 2026-09-28 16:20:00 | GOES-19 | FORMOSO DO ARAGUAIA | TOCANTINS | Brasil | 1708205 | 17 | 33 | nan | nan | nan | Cerrado | 91.5 |
| 65609912-4047-36a4-bb9c-6dd1ee03b466 | 2.1266 | -50.8788 | 2026-09-28 16:20:00 | GOES-19 | AMAPÁ | AMAPÁ | Brasil | 1600105 | 16 | 33 | nan | nan | nan | Amazônia | 81.0 |
| e94b8c98-70a4-30fe-a09f-341d63c6956b | -12.0158 | -50.7327 | 2026-09-28 16:20:00 | GOES-19 | NOVO SANTO ANTÔNIO | MATO GROSSO | Brasil | 5106315 | 51 | 33 | nan | nan | nan | Cerrado | 93.3 |
| 8d83beef-cfe3-36df-b4ef-b7059a2f9268 | -12.3088 | -50.2688 | 2026-09-28 16:20:00 | GOES-19 | FORMOSO DO ARAGUAIA | TOCANTINS | Brasil | 1708205 | 17 | 33 | nan | nan | nan | Cerrado | 89.9 |
| 146565a1-f78a-3144-a191-4289e42e0178 | -11.0764 | -51.3885 | 2026-09-28 16:20:00 | GOES-19 | LUCIARA | MATO GROSSO | Brasil | 5105309 | 51 | 33 | nan | nan | nan | Cerrado | 101.7 |
| b97d8589-b6d6-315b-8996-099749d9b773 | -11.2853 | -51.3454 | 2026-09-28 16:20:00 | GOES-19 | SÃO FÉLIX DO ARAGUAIA | MATO GROSSO | Brasil | 5107859 | 51 | 33 | nan | nan | nan | Cerrado | 83.6 |
| 326cc88f-94ea-31c0-903b-9ef366725a0e | -11.7138 | -50.5752 | 2026-09-28 16:20:00 | GOES-19 | FORMOSO DO ARAGUAIA | TOCANTINS | Brasil | 1708205 | 17 | 33 | nan | nan | nan | Cerrado | 123.6 |
| 2cb9205b-e344-3988-bd11-5822ac089d5e | -12.156 | -50.2874 | 2026-09-28 16:20:00 | GOES-19 | FORMOSO DO ARAGUAIA | TOCANTINS | Brasil | 1708205 | 17 | 33 | nan | nan | nan | Cerrado | 103.8 |
| 447c2208-939f-3809-a1e3-a8a2c800349d | -12.1734 | -50.3927 | 2026-09-28 16:20:00 | GOES-19 | FORMOSO DO ARAGUAIA | TOCANTINS | Brasil | 1708205 | 17 | 33 | nan | nan | nan | Cerrado | 114.6 |
| 020cbf6f-a017-33e7-bdf1-9f15d2e6b655 | -12.1737 | -50.3712 | 2026-09-28 16:20:00 | GOES-19 | FORMOSO DO ARAGUAIA | TOCANTINS | Brasil | 1708205 | 17 | 33 | nan | nan | nan | Cerrado | 107.2 |
| f21230de-ec3d-3b1b-9073-9061fa54af5c | -1.4116 | -49.0384 | 2026-09-28 16:20:00 | GOES-19 | PONTA DE PEDRAS | PARÁ | Brasil | 1505700 | 15 | 33 | nan | nan | nan | Amazônia | 93.5 |
| f22f6b83-c13d-3db8-9dfd-a82e1fb3f177 | -11.7329 | -50.573 | 2026-09-28 16:20:00 | GOES-19 | FORMOSO DO ARAGUAIA | TOCANTINS | Brasil | 1708205 | 17 | 33 | nan | nan | nan | Cerrado | 118.4 |
| 8e1d02e2-947a-36b7-a817-0e17551ef743 | -11.6951 | -50.556 | 2026-09-28 16:20:00 | GOES-19 | FORMOSO DO ARAGUAIA | TOCANTINS | Brasil | 1708205 | 17 | 33 | nan | nan | nan | Cerrado | 117.7 |
| ba52d23d-e333-3e76-8467-7edf87be77b9 | -11.9968 | -50.7349 | 2026-09-28 16:20:00 | GOES-19 | NOVO SANTO ANTÔNIO | MATO GROSSO | Brasil | 5106315 | 51 | 33 | nan | nan | nan | Cerrado | 90.0 |
| 918485a5-1e56-38b5-83ed-e4b5f708c6f8 | -1.3008 | -49.0613 | 2026-09-28 16:20:00 | GOES-19 | PONTA DE PEDRAS | PARÁ | Brasil | 1505700 | 15 | 33 | nan | nan | nan | Amazônia | 86.8 |
| 869cd71d-e60f-3fa6-b92a-0943fb93b7a3 | -11.9964 | -50.7563 | 2026-09-28 16:20:00 | GOES-19 | NOVO SANTO ANTÔNIO | MATO GROSSO | Brasil | 5106315 | 51 | 33 | nan | nan | nan | Cerrado | 90.3 |
| 40067209-9e7d-3a2c-8933-37a445d414bd | -11.7325 | -50.5944 | 2026-09-28 16:20:00 | GOES-19 | FORMOSO DO ARAGUAIA | TOCANTINS | Brasil | 1708205 | 17 | 33 | nan | nan | nan | Cerrado | 109.7 |
| 0a75012b-fc46-387a-b6dc-a0d06dffcbee | -11.077 | -51.3462 | 2026-09-28 16:20:00 | GOES-19 | LUCIARA | MATO GROSSO | Brasil | 5105309 | 51 | 33 | nan | nan | nan | Cerrado | 104.1 |
| 38645480-d3bf-38d0-a57c-ff6a19b1054c | -11.9619 | -50.5251 | 2026-09-28 16:20:00 | GOES-19 | FORMOSO DO ARAGUAIA | TOCANTINS | Brasil | 1708205 | 17 | 33 | nan | nan | nan | Cerrado | 98.1 |
| 14f3e619-683c-3b9a-89b6-5392a8a7bd8a | -12.1547 | -50.3735 | 2026-09-28 16:20:00 | GOES-19 | FORMOSO DO ARAGUAIA | TOCANTINS | Brasil | 1708205 | 17 | 33 | nan | nan | nan | Cerrado | 101.5 |
| 319d3c09-9f52-31d4-bec9-e3eeb144b73c | -18.65487 | -43.04111 | 2026-09-28 16:22:00 | NOAA-20 | SABINÓPOLIS | MINAS GERAIS | Brasil | 3156809 | 31 | 33 | nan | nan | nan | Mata Atlântica | 7.7 |
| 8954dba3-d205-3c3e-8c12-2566b572a864 | -21.07416 | -45.88612 | 2026-09-28 16:22:00 | NOAA-20 | CAMPO DO MEIO | MINAS GERAIS | Brasil | 3111309 | 31 | 33 | nan | nan | nan | Mata Atlântica | 4.3 |
| 8b9ae016-9b65-3a90-80ca-11fe8b814dab | -21.46278 | -44.38322 | 2026-09-28 16:22:00 | NOAA-20 | MADRE DE DEUS DE MINAS | MINAS GERAIS | Brasil | 3139102 | 31 | 33 | nan | nan | nan | Mata Atlântica | 3.8 |
| e08cc014-f092-3512-bbfd-4d330dde490c | -20.0582 | -41.40335 | 2026-09-28 16:22:00 | NOAA-20 | MUTUM | MINAS GERAIS | Brasil | 3144003 | 31 | 33 | nan | nan | nan | Mata Atlântica | 3.9 |
| c08dbd28-726d-3154-82f2-25406fcf321a | -23.11935 | -52.34369 | 2026-09-28 16:22:00 | NOAA-20 | ALTO PARANÁ | PARANÁ | Brasil | 4100608 | 41 | 33 | nan | nan | nan | Mata Atlântica | 19.7 |
| b9fb8de3-2cff-3f7a-8e59-b125beb7cb9e | -18.46427 | -46.43584 | 2026-09-28 16:22:00 | NOAA-20 | PRESIDENTE OLEGÁRIO | MINAS GERAIS | Brasil | 3153400 | 31 | 33 | nan | nan | nan | Cerrado | 5.3 |
| a7e13089-b430-3d43-8c1e-b3480282fbd7 | -17.9449 | -42.56205 | 2026-09-28 16:22:00 | NOAA-20 | ARICANDUVA | MINAS GERAIS | Brasil | 3104452 | 31 | 33 | nan | nan | nan | Mata Atlântica | 3.8 |
| 6793ab80-3790-34f5-bb48-2f5ff6f35817 | -20.97793 | -48.99573 | 2026-09-28 16:22:00 | NOAA-20 | TABAPUÃ | SÃO PAULO | Brasil | 3552601 | 35 | 33 | nan | nan | nan | Mata Atlântica | 3.5 |
| 95804f02-183e-3fbf-b3b8-fc182b887fa9 | -21.54377 | -47.12415 | 2026-09-28 16:22:00 | NOAA-20 | TAMBAÚ | SÃO PAULO | Brasil | 3553302 | 35 | 33 | nan | nan | nan | Cerrado | 18.1 |
| 79cdbb74-a3b7-3c12-8d1a-6750d4b431af | -22.53089 | -45.28181 | 2026-09-28 16:22:00 | NOAA-20 | DELFIM MOREIRA | MINAS GERAIS | Brasil | 3121100 | 31 | 33 | nan | nan | nan | Mata Atlântica | 6.1 |
| 65b49be2-6e35-3da6-a3bb-6dbd2edda07c | -17.94746 | -47.00207 | 2026-09-28 16:22:00 | NOAA-20 | VAZANTE | MINAS GERAIS | Brasil | 3171006 | 31 | 33 | nan | nan | nan | Cerrado | 57.3 |
| a8981807-6c77-3422-807b-615e060a2c3a | -20.20299 | -48.56861 | 2026-09-28 16:22:00 | NOAA-20 | GUAÍRA | SÃO PAULO | Brasil | 3517406 | 35 | 33 | nan | nan | nan | Cerrado | 6.3 |
| ae3a4a7a-0f91-3b63-a659-273f0ce4149f | -18.08928 | -43.686 | 2026-09-28 16:22:00 | NOAA-20 | DIAMANTINA | MINAS GERAIS | Brasil | 3121605 | 31 | 33 | nan | nan | nan | Cerrado | 4.0 |
| 197e73d9-1fdb-36f3-a076-d69e21736df1 | -20.36669 | -47.09134 | 2026-09-28 16:22:00 | NOAA-20 | IBIRACI | MINAS GERAIS | Brasil | 3129707 | 31 | 33 | nan | nan | nan | Cerrado | 13.7 |
| b2f697ad-6071-3888-b9a7-cad5ee4d5162 | -18.023 | -47.63612 | 2026-09-28 16:22:00 | NOAA-20 | CATALÃO | GOIÁS | Brasil | 5205109 | 52 | 33 | nan | nan | nan | Cerrado | 4.9 |
| 859b1056-7512-34ee-9750-2ce70b08d4cf | -19.41458 | -48.43983 | 2026-09-28 16:22:00 | NOAA-20 | PRATA | MINAS GERAIS | Brasil | 3152808 | 31 | 33 | nan | nan | nan | Cerrado | 60.6 |
| 4f5e0e2f-237e-3a7c-891e-b3ff1a30dd3c | -21.62185 | -44.40467 | 2026-09-28 16:22:00 | NOAA-20 | SÃO VICENTE DE MINAS | MINAS GERAIS | Brasil | 3165305 | 31 | 33 | nan | nan | nan | Mata Atlântica | 6.0 |
| 5f4efbd5-a6fb-3e67-93b0-9cf385f92e52 | -18.6855 | -48.62761 | 2026-09-28 16:22:00 | NOAA-20 | TUPACIGUARA | MINAS GERAIS | Brasil | 3169604 | 31 | 33 | nan | nan | nan | Cerrado | 88.3 |
| 6aad62be-8c98-3441-a558-1f534387be87 | -17.99755 | -41.91693 | 2026-09-28 16:22:00 | NOAA-20 | FRANCISCÓPOLIS | MINAS GERAIS | Brasil | 3126752 | 31 | 33 | nan | nan | nan | Mata Atlântica | 7.6 |
| bd02b9eb-9432-30c8-ba24-3cac979109bf | -19.41094 | -48.44505 | 2026-09-28 16:22:00 | NOAA-20 | PRATA | MINAS GERAIS | Brasil | 3152808 | 31 | 33 | nan | nan | nan | Cerrado | 46.9 |
| 3dbdfe85-5ee4-362b-b075-2e685e905592 | -19.41029 | -48.43911 | 2026-09-28 16:22:00 | NOAA-20 | PRATA | MINAS GERAIS | Brasil | 3152808 | 31 | 33 | nan | nan | nan | Cerrado | 36.4 |
| edec79c9-ef7f-353f-90e7-ea3f164d4b89 | -17.79043 | -47.16113 | 2026-09-28 16:22:00 | NOAA-20 | GUARDA-MOR | MINAS GERAIS | Brasil | 3128600 | 31 | 33 | nan | nan | nan | Cerrado | 71.9 |
| 59e5e449-d6c9-3fde-a0a6-8a9e1ca7ab15 | -18.68358 | -48.62376 | 2026-09-28 16:22:00 | NOAA-20 | TUPACIGUARA | MINAS GERAIS | Brasil | 3169604 | 31 | 33 | nan | nan | nan | Cerrado | 47.9 |
| ade2020f-ab8a-3255-b51e-d9c4f62b028f | -22.61283 | -44.77299 | 2026-09-28 16:22:00 | NOAA-20 | AREIAS | SÃO PAULO | Brasil | 3503505 | 35 | 33 | nan | nan | nan | Mata Atlântica | 4.7 |
| a789925d-4edb-3b38-9c95-785275d5ef98 | -22.25331 | -44.66824 | 2026-09-28 16:22:00 | NOAA-20 | ITAMONTE | MINAS GERAIS | Brasil | 3133006 | 31 | 33 | nan | nan | nan | Mata Atlântica | 15.0 |
| 8eab6b94-9b8f-344a-a755-114ba6fe1044 | -18.09612 | -44.35981 | 2026-09-28 16:22:00 | NOAA-20 | AUGUSTO DE LIMA | MINAS GERAIS | Brasil | 3104809 | 31 | 33 | nan | nan | nan | Cerrado | 39.8 |
| aeb648ce-0eb9-322a-9bf5-3ce853e2996b | -22.60399 | -47.43169 | 2026-09-28 16:22:00 | NOAA-20 | LIMEIRA | SÃO PAULO | Brasil | 3526902 | 35 | 33 | nan | nan | nan | Cerrado | 4.3 |
| 88e08da2-23a9-34c5-a683-e33b21f4d8b2 | -23.10584 | -50.92189 | 2026-09-28 16:22:00 | NOAA-20 | RANCHO ALEGRE | PARANÁ | Brasil | 4121307 | 41 | 33 | nan | nan | nan | Mata Atlântica | 10.3 |
| 717ed430-3a8e-368a-bd44-ee50a9cdcfb2 | -20.77087 | -51.31774 | 2026-09-28 16:22:00 | NOAA-20 | ANDRADINA | SÃO PAULO | Brasil | 3502101 | 35 | 33 | nan | nan | nan | Mata Atlântica | 19.6 |
| 438ca372-afef-3927-8880-39a913cab6dc | -20.46091 | -45.58077 | 2026-09-28 16:22:00 | NOAA-20 | PAINS | MINAS GERAIS | Brasil | 3146503 | 31 | 33 | nan | nan | nan | Cerrado | 3.3 |
| b24139d1-f17b-3bcd-a4b0-531bb1eb50d3 | -18.1665 | -43.95689 | 2026-09-28 16:22:00 | NOAA-20 | DIAMANTINA | MINAS GERAIS | Brasil | 3121605 | 31 | 33 | nan | nan | nan | Cerrado | 6.2 |
| 90826799-43db-3929-8178-11adf63e99a2 | -19.87303 | -42.09727 | 2026-09-28 16:22:00 | NOAA-20 | SANTA RITA DE MINAS | MINAS GERAIS | Brasil | 3159357 | 31 | 33 | nan | nan | nan | Mata Atlântica | 4.8 |
| adf3fa09-82a6-318e-9dc3-237db9fe86da | -18.0293 | -43.96394 | 2026-09-28 16:22:00 | NOAA-20 | AUGUSTO DE LIMA | MINAS GERAIS | Brasil | 3104809 | 31 | 33 | nan | nan | nan | Cerrado | 2.1 |
| 55d6a337-6ebe-33c5-a5ca-874fab33b9e2 | -18.55204 | -43.58202 | 2026-09-28 16:22:00 | NOAA-20 | PRESIDENTE KUBITSCHEK | MINAS GERAIS | Brasil | 3153301 | 31 | 33 | nan | nan | nan | Mata Atlântica | 2.8 |
| c2721476-6b5a-31dd-bdcf-d7af37ae46bc | -18.24281 | -49.58819 | 2026-09-28 16:22:00 | NOAA-20 | BOM JESUS DE GOIÁS | GOIÁS | Brasil | 5203500 | 52 | 33 | nan | nan | nan | Mata Atlântica | 13.9 |
| 3740694a-cf61-3f44-8364-79086455fa40 | -19.97307 | -44.47794 | 2026-09-28 16:22:00 | NOAA-20 | MATEUS LEME | MINAS GERAIS | Brasil | 3140704 | 31 | 33 | nan | nan | nan | Mata Atlântica | 11.1 |
| 70bcf3e0-1652-35fb-ab9a-c848bfbd39fa | -18.55803 | -48.39874 | 2026-09-28 16:22:00 | NOAA-20 | ARAGUARI | MINAS GERAIS | Brasil | 3103504 | 31 | 33 | nan | nan | nan | Mata Atlântica | 9.8 |
| 43f4b0b8-675f-3f14-b6dc-5ee27a53c195 | -20.77026 | -51.31419 | 2026-09-28 16:22:00 | NOAA-20 | ANDRADINA | SÃO PAULO | Brasil | 3502101 | 35 | 33 | nan | nan | nan | Mata Atlântica | 16.4 |
| 0fa59326-29dc-3a06-b4ef-783c1cac624b | -20.9715 | -43.80143 | 2026-09-28 16:22:00 | NOAA-20 | CARANDAÍ | MINAS GERAIS | Brasil | 3113206 | 31 | 33 | nan | nan | nan | Mata Atlântica | 6.5 |
| dec10fdc-494d-3c3b-9d97-f736d8837aa3 | -21.85862 | -45.46549 | 2026-09-28 16:22:00 | NOAA-20 | CAMPANHA | MINAS GERAIS | Brasil | 3110905 | 31 | 33 | nan | nan | nan | Mata Atlântica | 3.3 |
| 306b9835-e9e6-3137-91cb-9455347e5711 | -21.90856 | -45.34713 | 2026-09-28 16:22:00 | NOAA-20 | CAMPANHA | MINAS GERAIS | Brasil | 3110905 | 31 | 33 | nan | nan | nan | Mata Atlântica | 5.1 |
| 77476854-35bd-34cc-aafc-3ab55539e3e7 | -20.81213 | -43.25637 | 2026-09-28 16:22:00 | NOAA-20 | BRÁS PIRES | MINAS GERAIS | Brasil | 3108701 | 31 | 33 | nan | nan | nan | Mata Atlântica | 3.9 |
| 243babca-359b-3091-a885-098113f508f7 | -21.30083 | -45.6121 | 2026-09-28 16:22:00 | NOAA-20 | CAMPOS GERAIS | MINAS GERAIS | Brasil | 3111606 | 31 | 33 | nan | nan | nan | Mata Atlântica | 3.4 |
| 383b481b-9a73-3fc3-9ea0-bff9bdca2e44 | -21.91081 | -45.32941 | 2026-09-28 16:22:00 | NOAA-20 | CAMBUQUIRA | MINAS GERAIS | Brasil | 3110707 | 31 | 33 | nan | nan | nan | Mata Atlântica | 28.1 |
| 91ef3b60-5ccf-3d92-8759-ae3542bf8585 | -20.35428 | -46.38782 | 2026-09-28 16:22:00 | NOAA-20 | VARGEM BONITA | MINAS GERAIS | Brasil | 3170602 | 31 | 33 | nan | nan | nan | Cerrado | 4.6 |
| c087d844-65f0-33bb-9e81-a72321b5d0e8 | -20.45808 | -47.80375 | 2026-09-28 16:22:00 | NOAA-20 | GUARÁ | SÃO PAULO | Brasil | 3517703 | 35 | 33 | nan | nan | nan | Cerrado | 5.7 |
| 0cc1255c-4b60-37a8-83b6-4d05ca09e3fd | -21.2378 | -44.33473 | 2026-09-28 16:22:00 | NOAA-20 | SÃO JOÃO DEL REI | MINAS GERAIS | Brasil | 3162500 | 31 | 33 | nan | nan | nan | Mata Atlântica | 2.3 |
| d31d1a64-41f2-31dd-94cb-9c67a1c308f9 | -19.54255 | -45.26889 | 2026-09-28 16:22:00 | NOAA-20 | BOM DESPACHO | MINAS GERAIS | Brasil | 3107406 | 31 | 33 | nan | nan | nan | Cerrado | 9.8 |
| f8cbf1b7-6e90-35e5-b7dd-bf53611f31fa | -22.8497 | -49.35876 | 2026-09-28 16:22:00 | NOAA-20 | ÁGUAS DE SANTA BÁRBARA | SÃO PAULO | Brasil | 3500550 | 35 | 33 | nan | nan | nan | Cerrado | 9.4 |
| fdb52088-5244-34f1-8abf-f480d5f4a469 | -20.76409 | -51.31469 | 2026-09-28 16:22:00 | NOAA-20 | ANDRADINA | SÃO PAULO | Brasil | 3502101 | 35 | 33 | nan | nan | nan | Mata Atlântica | 21.0 |
| 114ac01a-f43e-3aed-aa1d-bdfe7b1ae65b | -21.23799 | -45.61868 | 2026-09-28 16:22:00 | NOAA-20 | CAMPOS GERAIS | MINAS GERAIS | Brasil | 3111606 | 31 | 33 | nan | nan | nan | Mata Atlântica | 7.6 |
| aca43708-5dd9-32e6-8764-3381722eebc0 | -20.71866 | -41.30941 | 2026-09-28 16:22:00 | NOAA-20 | CACHOEIRO DE ITAPEMIRIM | ESPÍRITO SANTO | Brasil | 3201209 | 32 | 33 | nan | nan | nan | Mata Atlântica | 2.4 |
| 28c7cadd-16de-3958-b684-cb9e69a23fc0 | -18.97289 | -48.0993 | 2026-09-28 16:22:00 | NOAA-20 | UBERLÂNDIA | MINAS GERAIS | Brasil | 3170206 | 31 | 33 | nan | nan | nan | Cerrado | 4.4 |
| 9bf56bda-31cf-3747-9c1b-8e96110053a0 | -18.74106 | -48.13246 | 2026-09-28 16:22:00 | NOAA-20 | ARAGUARI | MINAS GERAIS | Brasil | 3103504 | 31 | 33 | nan | nan | nan | Mata Atlântica | 10.3 |
| efa4dabc-7709-38ad-ae16-7b7bc71c2075 | -18.16472 | -48.01855 | 2026-09-28 16:22:00 | NOAA-20 | GOIANDIRA | GOIÁS | Brasil | 5208509 | 52 | 33 | nan | nan | nan | Cerrado | 27.4 |
| 6f919f28-ccb8-3ba0-859b-98d67838675e | -21.22458 | -44.32562 | 2026-09-28 16:22:00 | NOAA-20 | SÃO JOÃO DEL REI | MINAS GERAIS | Brasil | 3162500 | 31 | 33 | nan | nan | nan | Mata Atlântica | 5.7 |
| d8bada6c-9c19-327e-80e4-8acf8bcf443a | -17.80885 | -44.42833 | 2026-09-28 16:22:00 | NOAA-20 | LASSANCE | MINAS GERAIS | Brasil | 3138104 | 31 | 33 | nan | nan | nan | Cerrado | 5.5 |
| 4a47dba2-b915-355b-ad7e-361803d81913 | -17.80951 | -44.4333 | 2026-09-28 16:22:00 | NOAA-20 | LASSANCE | MINAS GERAIS | Brasil | 3138104 | 31 | 33 | nan | nan | nan | Cerrado | 5.5 |
| e36542af-636a-3b7a-8199-eb004865355e | -17.8034 | -42.34698 | 2026-09-28 16:22:00 | NOAA-20 | ÁGUA BOA | MINAS GERAIS | Brasil | 3100609 | 31 | 33 | nan | nan | nan | Mata Atlântica | 3.3 |
| e8d667cf-6905-35c1-bab2-e2383978c930 | -21.02119 | -44.99532 | 2026-09-28 16:22:00 | NOAA-20 | SANTO ANTÔNIO DO AMPARO | MINAS GERAIS | Brasil | 3159902 | 31 | 33 | nan | nan | nan | Mata Atlântica | 6.7 |
| 589e98b9-ffb6-36b5-838d-1eaf3202fe81 | -19.38496 | -42.00434 | 2026-09-28 16:22:00 | NOAA-20 | TARUMIRIM | MINAS GERAIS | Brasil | 3168408 | 31 | 33 | nan | nan | nan | Mata Atlântica | 5.0 |
| fe9285ca-739b-3668-9919-a0d77d38d1e5 | -18.12866 | -44.37081 | 2026-09-28 16:22:00 | NOAA-20 | AUGUSTO DE LIMA | MINAS GERAIS | Brasil | 3104809 | 31 | 33 | nan | nan | nan | Cerrado | 37.6 |
| 8aa5a684-f327-3bd4-bb3d-645c6cf99e45 | -17.09839 | -41.62033 | 2026-09-28 16:22:00 | NOAA-20 | PADRE PARAÍSO | MINAS GERAIS | Brasil | 3146305 | 31 | 33 | nan | nan | nan | Mata Atlântica | 9.2 |
| 709402c0-3a0d-3d24-824a-22a35d847cf8 | -19.40922 | -48.43744 | 2026-09-28 16:22:00 | NOAA-20 | PRATA | MINAS GERAIS | Brasil | 3152808 | 31 | 33 | nan | nan | nan | Cerrado | 12.1 |
| 25078a50-630f-3a4b-a86c-36b760147721 | -20.76365 | -51.30954 | 2026-09-28 16:22:00 | NOAA-20 | ANDRADINA | SÃO PAULO | Brasil | 3502101 | 35 | 33 | nan | nan | nan | Mata Atlântica | 21.0 |
| 1edf4840-9da7-3f51-b2f0-75186e811070 | -21.05949 | -46.26529 | 2026-09-28 16:22:00 | NOAA-20 | CONCEIÇÃO DA APARECIDA | MINAS GERAIS | Brasil | 3117108 | 31 | 33 | nan | nan | nan | Mata Atlântica | 4.4 |
| 99f43315-9b41-37c6-bf1b-43dcf131a7d6 | -21.00339 | -46.46866 | 2026-09-28 16:22:00 | NOAA-20 | BOM JESUS DA PENHA | MINAS GERAIS | Brasil | 3107604 | 31 | 33 | nan | nan | nan | Mata Atlântica | 7.9 |
| 7c73d4b6-f085-39dc-8dc3-a4e05c0f6c0e | -19.13116 | -46.68369 | 2026-09-28 16:22:00 | NOAA-20 | SERRA DO SALITRE | MINAS GERAIS | Brasil | 3166808 | 31 | 33 | nan | nan | nan | Cerrado | 23.5 |
| 0c31f33f-ab59-3c03-bb7c-f03acd0b605a | -17.81844 | -44.44209 | 2026-09-28 16:22:00 | NOAA-20 | LASSANCE | MINAS GERAIS | Brasil | 3138104 | 31 | 33 | nan | nan | nan | Cerrado | 9.8 |
| c771401e-1423-336a-9e45-56e51fad14d5 | -17.82714 | -44.39035 | 2026-09-28 16:22:00 | NOAA-20 | LASSANCE | MINAS GERAIS | Brasil | 3138104 | 31 | 33 | nan | nan | nan | Cerrado | 10.2 |


[Clique aqui para ver as próximas entradas](README92.md)
