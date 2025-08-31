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

## Dados Diários - Página 81

| ID | Latitude | Longitude | Data/Hora GMT | Satélite | Município | Estado | País | Município ID | Estado ID | País ID | Dias sem Chuva | Precipitação | Risco de Fogo | Bioma | FRP |
|----|----------|-----------|---------------|----------|-----------|--------|------|--------------|-----------|---------|----------------|--------------|----------------|-------|-----|
| a91c4de5-4b53-38ce-8661-983b169ede1e | -7.7299 | -71.9906 | 2025-08-31 06:10:00 | NPP-375D | CRUZEIRO DO SUL | ACRE | Brasil | 1200203 | 12 | 33 | nan | nan | nan | Amazônia | 0.8 |
| adec6707-2232-3008-a9d6-5885463832bc | -9.45112 | -62.35057 | 2025-08-31 06:10:00 | NPP-375D | MACHADINHO D'OESTE | RONDÔNIA | Brasil | 1100130 | 11 | 33 | nan | nan | nan | Amazônia | 5.3 |
| 8afecbc5-ac8b-3b8a-b655-f51f27ecb840 | -9.44206 | -60.56773 | 2025-08-31 06:10:00 | NPP-375D | ARIPUANÃ | MATO GROSSO | Brasil | 5101407 | 51 | 33 | nan | nan | nan | Amazônia | 1.5 |
| a5c551cd-f827-3a19-919e-80cbeeaed8ff | -8.69471 | -71.60043 | 2025-08-31 06:10:00 | NPP-375D | JORDÃO | ACRE | Brasil | 1200328 | 12 | 33 | nan | nan | nan | Amazônia | 0.9 |
| e049a9b8-63d7-3d52-a373-91020587a0e8 | -9.32927 | -70.43352 | 2025-08-31 06:10:00 | NPP-375D | SANTA ROSA DO PURUS | ACRE | Brasil | 1200435 | 12 | 33 | nan | nan | nan | Amazônia | 0.5 |
| 9cd0317e-fe35-392e-be74-84e2f5a9ee18 | -8.74106 | -71.1053 | 2025-08-31 06:10:00 | NPP-375D | TARAUACÁ | ACRE | Brasil | 1200609 | 12 | 33 | nan | nan | nan | Amazônia | 0.4 |
| 5a636f94-76d4-32f3-9d61-8f4c27700a3c | -7.9293 | -63.01048 | 2025-08-31 06:10:00 | NPP-375D | HUMAITÁ | AMAZONAS | Brasil | 1301704 | 13 | 33 | nan | nan | nan | Amazônia | 2.7 |
| f500ab76-8c4f-31b9-9669-7c0afde04753 | -9.45772 | -62.34373 | 2025-08-31 06:10:00 | NPP-375D | MACHADINHO D'OESTE | RONDÔNIA | Brasil | 1100130 | 11 | 33 | nan | nan | nan | Amazônia | 5.5 |
| 830d2105-6af1-3308-be44-d4d761ae96c0 | -8.74144 | -62.39521 | 2025-08-31 06:10:00 | NPP-375D | CUJUBIM | RONDÔNIA | Brasil | 1100940 | 11 | 33 | nan | nan | nan | Amazônia | 0.9 |
| 7b9e9c52-d981-3034-a7db-bde302f0af61 | -8.51546 | -70.00909 | 2025-08-31 06:10:00 | NPP-375D | FEIJÓ | ACRE | Brasil | 1200302 | 12 | 33 | nan | nan | nan | Amazônia | 1.0 |
| 1e065de3-b4a1-30a3-b3f3-fc5ba60a3688 | -9.43842 | -62.36032 | 2025-08-31 06:10:00 | NPP-375D | MACHADINHO D'OESTE | RONDÔNIA | Brasil | 1100130 | 11 | 33 | nan | nan | nan | Amazônia | 1.6 |
| 2f710560-1110-397b-87d5-e739d50ea122 | -8.43097 | -62.29255 | 2025-08-31 06:10:00 | NPP-375D | HUMAITÁ | AMAZONAS | Brasil | 1301704 | 13 | 33 | nan | nan | nan | Amazônia | 1.1 |
| ea95fd8b-b591-36c1-a159-1456df4cd2e3 | -8.68097 | -66.93477 | 2025-08-31 06:10:00 | NPP-375D | LÁBREA | AMAZONAS | Brasil | 1302405 | 13 | 33 | nan | nan | nan | Amazônia | 2.2 |
| 17b01db9-0e08-33c0-a210-87dea7c3514c | -8.90612 | -62.10224 | 2025-08-31 06:10:00 | NPP-375D | MACHADINHO D'OESTE | RONDÔNIA | Brasil | 1100130 | 11 | 33 | nan | nan | nan | Amazônia | 1.4 |
| f09d37df-f828-3231-8526-5170a69ebd54 | -8.59896 | -61.95834 | 2025-08-31 06:10:00 | NPP-375D | MANICORÉ | AMAZONAS | Brasil | 1302702 | 13 | 33 | nan | nan | nan | Amazônia | 0.5 |
| f2609502-f0f0-3dd9-be2d-befe3f470c11 | -8.67143 | -62.41185 | 2025-08-31 06:10:00 | NPP-375D | PORTO VELHO | RONDÔNIA | Brasil | 1100205 | 11 | 33 | nan | nan | nan | Amazônia | 0.7 |
| 3d2410b4-0049-32e0-a9c8-2a0e9a392192 | -8.74947 | -62.3775 | 2025-08-31 06:10:00 | NPP-375D | CUJUBIM | RONDÔNIA | Brasil | 1100940 | 11 | 33 | nan | nan | nan | Amazônia | 1.0 |
| 96f1c192-36c0-303a-8d8d-f92bf76c27dc | -8.68 | -66.93487 | 2025-08-31 06:10:00 | NPP-375D | LÁBREA | AMAZONAS | Brasil | 1302405 | 13 | 33 | nan | nan | nan | Amazônia | 2.5 |
| d651ef4d-08af-3cab-84fe-b93e881f88fc | -8.6782 | -62.41365 | 2025-08-31 06:10:00 | NPP-375D | PORTO VELHO | RONDÔNIA | Brasil | 1100205 | 11 | 33 | nan | nan | nan | Amazônia | 1.2 |
| 2ec9def7-fa97-3ee8-b166-d30b1f9eb7c7 | -8.74392 | -62.37666 | 2025-08-31 06:10:00 | NPP-375D | PORTO VELHO | RONDÔNIA | Brasil | 1100205 | 11 | 33 | nan | nan | nan | Amazônia | 1.8 |
| 44fbc4ad-b1b8-34e9-bae9-b94cee60a549 | -8.66957 | -62.42619 | 2025-08-31 06:10:00 | NPP-375D | PORTO VELHO | RONDÔNIA | Brasil | 1100205 | 11 | 33 | nan | nan | nan | Amazônia | 0.9 |
| 2173125a-2fd9-3f38-9d89-07d63d7c6083 | -8.67263 | -62.41307 | 2025-08-31 06:10:00 | NPP-375D | PORTO VELHO | RONDÔNIA | Brasil | 1100205 | 11 | 33 | nan | nan | nan | Amazônia | 1.2 |
| cce22b0a-d6d5-3241-b142-fcabddc2ce58 | -8.67214 | -62.41663 | 2025-08-31 06:10:00 | NPP-375D | PORTO VELHO | RONDÔNIA | Brasil | 1100205 | 11 | 33 | nan | nan | nan | Amazônia | 1.2 |
| 3a57065b-41f6-36bc-adea-85da81cddac2 | -9.43127 | -62.345 | 2025-08-31 06:10:00 | NPP-375D | MACHADINHO D'OESTE | RONDÔNIA | Brasil | 1100130 | 11 | 33 | nan | nan | nan | Amazônia | 1.5 |
| 8a1dde09-a348-385f-84fb-15ae70065e99 | -8.67051 | -62.41898 | 2025-08-31 06:10:00 | NPP-375D | PORTO VELHO | RONDÔNIA | Brasil | 1100205 | 11 | 33 | nan | nan | nan | Amazônia | 1.0 |
| c360bac9-c74e-32e8-8a5a-7fa3177188c3 | -9.46187 | -62.35602 | 2025-08-31 06:10:00 | NPP-375D | MACHADINHO D'OESTE | RONDÔNIA | Brasil | 1100130 | 11 | 33 | nan | nan | nan | Amazônia | 1.7 |
| 2fa76c26-5a2d-310e-8f37-52fe7da4c36c | -8.79517 | -71.02253 | 2025-08-31 06:10:00 | NPP-375D | FEIJÓ | ACRE | Brasil | 1200302 | 12 | 33 | nan | nan | nan | Amazônia | 0.7 |
| 2905eb98-e95a-3569-80b5-2ccbe9dbbe46 | -9.44307 | -62.36865 | 2025-08-31 06:10:00 | NPP-375D | MACHADINHO D'OESTE | RONDÔNIA | Brasil | 1100130 | 11 | 33 | nan | nan | nan | Amazônia | 1.9 |
| 788ab45a-cf63-3cd3-8fdf-bead62f51f46 | -8.56959 | -70.06324 | 2025-08-31 06:10:00 | NPP-375D | FEIJÓ | ACRE | Brasil | 1200302 | 12 | 33 | nan | nan | nan | Amazônia | 1.2 |
| 900bd948-5209-3e6b-a9f1-1b04e21d57b6 | -8.97887 | -70.74068 | 2025-08-31 06:10:00 | NPP-375D | FEIJÓ | ACRE | Brasil | 1200302 | 12 | 33 | nan | nan | nan | Amazônia | 1.3 |
| 39c2f4d4-0c6c-3ef8-b525-07bc84d01937 | -8.23709 | -73.33572 | 2025-08-31 06:10:00 | NPP-375D | CRUZEIRO DO SUL | ACRE | Brasil | 1200203 | 12 | 33 | nan | nan | nan | Amazônia | 0.8 |
| 28df56c0-03e7-3900-8b53-d14cc8a0ff94 | -8.88122 | -62.3876 | 2025-08-31 06:10:00 | NPP-375D | CUJUBIM | RONDÔNIA | Brasil | 1100940 | 11 | 33 | nan | nan | nan | Amazônia | 2.4 |
| 9803c5fa-1c34-32bd-82a4-7e978fc6fe42 | -8.67004 | -62.42256 | 2025-08-31 06:10:00 | NPP-375D | PORTO VELHO | RONDÔNIA | Brasil | 1100205 | 11 | 33 | nan | nan | nan | Amazônia | 1.0 |
| 1a97f84d-652a-3232-a315-111781c0ffda | -8.90398 | -62.10564 | 2025-08-31 06:10:00 | NPP-375D | MACHADINHO D'OESTE | RONDÔNIA | Brasil | 1100130 | 11 | 33 | nan | nan | nan | Amazônia | 1.5 |
| 46baa475-3555-3b04-867e-f80b70e81634 | -8.38054 | -71.18336 | 2025-08-31 06:10:00 | NPP-375D | TARAUACÁ | ACRE | Brasil | 1200609 | 12 | 33 | nan | nan | nan | Amazônia | 0.6 |
| db097291-273e-39f3-945e-2d761c05a301 | -10.72026 | -65.05152 | 2025-08-31 06:10:00 | NPP-375D | GUAJARÁ-MIRIM | RONDÔNIA | Brasil | 1100106 | 11 | 33 | nan | nan | nan | Amazônia | 0.9 |
| 69a5b55d-06f1-3099-8278-0f04285d7c32 | -7.67236 | -73.00853 | 2025-08-31 06:10:00 | NPP-375D | MÂNCIO LIMA | ACRE | Brasil | 1200336 | 12 | 33 | nan | nan | nan | Amazônia | 0.9 |
| 224ef153-1846-3b11-a4ea-0e1bcbcf861b | -8.88445 | -70.85613 | 2025-08-31 06:10:00 | NPP-375D | FEIJÓ | ACRE | Brasil | 1200302 | 12 | 33 | nan | nan | nan | Amazônia | 0.6 |
| a9b433d3-a631-3c22-a896-14147d69dfee | -10.63969 | -69.04961 | 2025-08-31 06:10:00 | NPP-375D | BRASILÉIA | ACRE | Brasil | 1200104 | 12 | 33 | nan | nan | nan | Amazônia | 1.3 |
| 9247c5c1-2f54-3377-995a-06fca43dd2cc | -7.91349 | -63.00827 | 2025-08-31 06:10:00 | NPP-375D | HUMAITÁ | AMAZONAS | Brasil | 1301704 | 13 | 33 | nan | nan | nan | Amazônia | 0.4 |
| 003b3dc5-8eff-3672-9f3a-536eb9fa9bad | -8.67097 | -62.41543 | 2025-08-31 06:10:00 | NPP-375D | PORTO VELHO | RONDÔNIA | Brasil | 1100205 | 11 | 33 | nan | nan | nan | Amazônia | 0.7 |
| 12aa7581-3fd3-3f40-a810-2306ae876b03 | -7.92448 | -63.00649 | 2025-08-31 06:10:00 | NPP-375D | HUMAITÁ | AMAZONAS | Brasil | 1301704 | 13 | 33 | nan | nan | nan | Amazônia | 1.3 |
| fa68e214-8cd5-3e94-820f-4aab9a7c0de3 | -9.45674 | -62.35138 | 2025-08-31 06:10:00 | NPP-375D | MACHADINHO D'OESTE | RONDÔNIA | Brasil | 1100130 | 11 | 33 | nan | nan | nan | Amazônia | 5.3 |
| a748c80a-4ec0-3c33-bb76-34b3e90c8de6 | -8.97837 | -70.7412 | 2025-08-31 06:10:00 | NPP-375D | FEIJÓ | ACRE | Brasil | 1200302 | 12 | 33 | nan | nan | nan | Amazônia | 1.3 |
| aec38a1b-f487-32a2-bc77-6fdbcd83832f | -8.6787 | -62.41004 | 2025-08-31 06:10:00 | NPP-375D | PORTO VELHO | RONDÔNIA | Brasil | 1100205 | 11 | 33 | nan | nan | nan | Amazônia | 1.7 |
| c655d261-7160-3eb5-acc2-abae73eb79cf | -8.74442 | -62.37289 | 2025-08-31 06:10:00 | NPP-375D | PORTO VELHO | RONDÔNIA | Brasil | 1100205 | 11 | 33 | nan | nan | nan | Amazônia | 0.9 |
| e4e5ef6a-b922-30d4-813b-ef74c007b639 | -8.75369 | -61.86306 | 2025-08-31 06:10:00 | NPP-375D | MANICORÉ | AMAZONAS | Brasil | 1302702 | 13 | 33 | nan | nan | nan | Amazônia | 1.2 |
| f1956215-c7a5-3846-889f-b9b3682dc7f1 | -11.31708 | -63.26772 | 2025-08-31 06:10:00 | NPP-375D | SÃO MIGUEL DO GUAPORÉ | RONDÔNIA | Brasil | 1100320 | 11 | 33 | nan | nan | nan | Amazônia | 9.9 |
| 27058855-6553-33c3-ab61-097e22c95131 | -8.68113 | -62.42407 | 2025-08-31 06:10:00 | NPP-375D | PORTO VELHO | RONDÔNIA | Brasil | 1100205 | 11 | 33 | nan | nan | nan | Amazônia | 1.4 |
| 7c72cd43-59a1-3c2d-94c7-6b897ef48223 | -8.74997 | -62.37376 | 2025-08-31 06:10:00 | NPP-375D | CUJUBIM | RONDÔNIA | Brasil | 1100940 | 11 | 33 | nan | nan | nan | Amazônia | 0.9 |
| 02a58b78-82e7-303d-9c63-7e85a5b3d17a | -9.43835 | -60.54675 | 2025-08-31 06:10:00 | NPP-375D | ARIPUANÃ | MATO GROSSO | Brasil | 5101407 | 51 | 33 | nan | nan | nan | Amazônia | 0.9 |
| bef1c002-4d3e-3ff9-b15d-589f339f71a1 | -9.33362 | -68.21297 | 2025-08-31 06:10:00 | NPP-375D | BUJARI | ACRE | Brasil | 1200138 | 12 | 33 | nan | nan | nan | Amazônia | 1.6 |
| 03ca7595-2ab1-36b1-bac1-b6b9193ec2fd | -8.65059 | -62.82561 | 2025-08-31 06:10:00 | NPP-375D | CANDEIAS DO JAMARI | RONDÔNIA | Brasil | 1100809 | 11 | 33 | nan | nan | nan | Amazônia | 1.2 |
| 0744fe00-6113-346c-b156-7634201a80c1 | -8.74699 | -62.396 | 2025-08-31 06:10:00 | NPP-375D | CUJUBIM | RONDÔNIA | Brasil | 1100940 | 11 | 33 | nan | nan | nan | Amazônia | 1.1 |
| cd02a988-0cf4-3a11-a831-31de082a92a7 | -8.68667 | -62.42485 | 2025-08-31 06:10:00 | NPP-375D | PORTO VELHO | RONDÔNIA | Brasil | 1100205 | 11 | 33 | nan | nan | nan | Amazônia | 1.0 |
| efefbb8c-7349-3fee-83a6-8ca6c7636364 | -8.56296 | -63.01229 | 2025-08-31 06:10:00 | NPP-375D | CANDEIAS DO JAMARI | RONDÔNIA | Brasil | 1100809 | 11 | 33 | nan | nan | nan | Amazônia | 2.3 |
| 23f91a82-3213-321f-b3cb-2dc7f17bd30a | -6.91915 | -71.74765 | 2025-08-31 06:10:00 | NPP-375D | IPIXUNA | AMAZONAS | Brasil | 1301803 | 13 | 33 | nan | nan | nan | Amazônia | 0.9 |
| a5993608-8e91-34cd-ac6d-07766c590184 | -8.67017 | -62.43101 | 2025-08-31 06:10:00 | NPP-375D | PORTO VELHO | RONDÔNIA | Brasil | 1100205 | 11 | 33 | nan | nan | nan | Amazônia | 1.2 |
| 79b51691-697e-3138-a3a1-ba65fc111af4 | -11.38826 | -63.27965 | 2025-08-31 06:10:00 | NPP-375D | SÃO MIGUEL DO GUAPORÉ | RONDÔNIA | Brasil | 1100320 | 11 | 33 | nan | nan | nan | Amazônia | 0.9 |
| 25f309fe-7191-3021-903f-57690b105cde | -10.70233 | -69.05896 | 2025-08-31 06:10:00 | NPP-375D | BRASILÉIA | ACRE | Brasil | 1200104 | 12 | 33 | nan | nan | nan | Amazônia | 0.3 |
| 09c3a043-0bc9-38be-9445-f1b162d14f91 | -7.91832 | -63.01223 | 2025-08-31 06:10:00 | NPP-375D | HUMAITÁ | AMAZONAS | Brasil | 1301704 | 13 | 33 | nan | nan | nan | Amazônia | 5.2 |
| e6de3ccf-2c66-35a5-ae5b-1a91290ba6f3 | -9.44646 | -62.34227 | 2025-08-31 06:10:00 | NPP-375D | MACHADINHO D'OESTE | RONDÔNIA | Brasil | 1100130 | 11 | 33 | nan | nan | nan | Amazônia | 0.9 |
| 629b03a4-6faf-34a0-b263-630e3f4ff611 | -8.88632 | -62.39207 | 2025-08-31 06:10:00 | NPP-375D | CUJUBIM | RONDÔNIA | Brasil | 1100940 | 11 | 33 | nan | nan | nan | Amazônia | 2.4 |
| fca62209-62a4-3bee-a070-5b68ca1e95ac | -9.56446 | -66.68965 | 2025-08-31 06:10:00 | NPP-375D | LÁBREA | AMAZONAS | Brasil | 1302405 | 13 | 33 | nan | nan | nan | Amazônia | 1.2 |
| 70c7d0e0-d0d7-361b-bfd9-5b8a67885070 | -9.76288 | -67.54346 | 2025-08-31 06:10:00 | NPP-375D | PORTO ACRE | ACRE | Brasil | 1200807 | 12 | 33 | nan | nan | nan | Amazônia | 0.8 |
| faf68d5b-4b8a-3514-a3ec-9e4b7601a742 | -9.57728 | -66.69022 | 2025-08-31 06:10:00 | NPP-375D | LÁBREA | AMAZONAS | Brasil | 1302405 | 13 | 33 | nan | nan | nan | Amazônia | 1.0 |
| 5174d70b-ec76-36d8-9027-c67733e9280e | -9.45155 | -60.56956 | 2025-08-31 06:10:00 | NPP-375D | ARIPUANÃ | MATO GROSSO | Brasil | 5101407 | 51 | 33 | nan | nan | nan | Amazônia | 1.2 |
| 93af4b3e-90bc-3efc-8d00-f40b0cc5bab4 | -9.44791 | -62.33089 | 2025-08-31 06:10:00 | NPP-375D | MACHADINHO D'OESTE | RONDÔNIA | Brasil | 1100130 | 11 | 33 | nan | nan | nan | Amazônia | 0.8 |
| 38ed1b7a-aeb4-3222-8edc-8f0327e26cac | -8.66631 | -62.83126 | 2025-08-31 06:10:00 | NPP-375D | CANDEIAS DO JAMARI | RONDÔNIA | Brasil | 1100809 | 11 | 33 | nan | nan | nan | Amazônia | 4.0 |
| f593aed9-9198-3ad8-8dcf-233c2e1ee5ba | -8.56341 | -63.009 | 2025-08-31 06:10:00 | NPP-375D | CANDEIAS DO JAMARI | RONDÔNIA | Brasil | 1100809 | 11 | 33 | nan | nan | nan | Amazônia | 1.3 |
| 615cf0ab-d0c1-3476-8c24-a7a1dab06604 | -9.00639 | -63.62673 | 2025-08-31 06:10:00 | NPP-375D | CANDEIAS DO JAMARI | RONDÔNIA | Brasil | 1100809 | 11 | 33 | nan | nan | nan | Amazônia | 1.1 |
| a05fa1f8-c935-3c3d-a7a7-cdc0645f7159 | -8.38527 | -70.83075 | 2025-08-31 06:10:00 | NPP-375D | TARAUACÁ | ACRE | Brasil | 1200609 | 12 | 33 | nan | nan | nan | Amazônia | 1.1 |
| 0a26af45-87e6-3d85-acf0-00dc644d2380 | -9.43569 | -62.33688 | 2025-08-31 06:10:00 | NPP-375D | MACHADINHO D'OESTE | RONDÔNIA | Brasil | 1100130 | 11 | 33 | nan | nan | nan | Amazônia | 1.6 |
| bf01ac4c-a251-3386-8d7f-efceded4fdc9 | -8.63936 | -62.82747 | 2025-08-31 06:10:00 | NPP-375D | CANDEIAS DO JAMARI | RONDÔNIA | Brasil | 1100809 | 11 | 33 | nan | nan | nan | Amazônia | 1.6 |
| 3fcae2b7-52b1-3815-a57f-e37ddf90db64 | -9.44142 | -60.57264 | 2025-08-31 06:10:00 | NPP-375D | ARIPUANÃ | MATO GROSSO | Brasil | 5101407 | 51 | 33 | nan | nan | nan | Amazônia | 3.4 |
| 0ca15542-f012-3c97-950e-199dbf43c129 | -7.95401 | -63.33141 | 2025-08-31 06:10:00 | NPP-375D | HUMAITÁ | AMAZONAS | Brasil | 1301704 | 13 | 33 | nan | nan | nan | Amazônia | 0.5 |
| 8ba40b05-8cdc-3709-86e2-ec17a14120d6 | -8.6452 | -62.82485 | 2025-08-31 06:10:00 | NPP-375D | CANDEIAS DO JAMARI | RONDÔNIA | Brasil | 1100809 | 11 | 33 | nan | nan | nan | Amazônia | 1.2 |
| a47bfb43-8221-3bfc-bdf6-f396959538b5 | -8.74292 | -62.38413 | 2025-08-31 06:10:00 | NPP-375D | PORTO VELHO | RONDÔNIA | Brasil | 1100205 | 11 | 33 | nan | nan | nan | Amazônia | 1.8 |
| 1cf16993-ebbc-33c5-af22-82bbc5a11b77 | -9.43831 | -60.57302 | 2025-08-31 06:10:00 | NPP-375D | ARIPUANÃ | MATO GROSSO | Brasil | 5101407 | 51 | 33 | nan | nan | nan | Amazônia | 2.6 |
| 7771f8bb-a40b-34b8-8d1b-1e960c9d0315 | -9.44356 | -62.36488 | 2025-08-31 06:10:00 | NPP-375D | MACHADINHO D'OESTE | RONDÔNIA | Brasil | 1100130 | 11 | 33 | nan | nan | nan | Amazônia | 1.6 |
| 16d40160-e3d2-3c38-b46e-7e77397fd943 | -8.88075 | -62.39125 | 2025-08-31 06:10:00 | NPP-375D | CUJUBIM | RONDÔNIA | Brasil | 1100940 | 11 | 33 | nan | nan | nan | Amazônia | 2.4 |
| 466e1533-99f0-32c2-963b-fa69c2ea85cd | -8.67559 | -62.42331 | 2025-08-31 06:10:00 | NPP-375D | PORTO VELHO | RONDÔNIA | Brasil | 1100205 | 11 | 33 | nan | nan | nan | Amazônia | 1.4 |
| 6ab176c5-9dc0-3769-8fa5-5aa7a2624e88 | -8.73687 | -62.38703 | 2025-08-31 06:10:00 | NPP-375D | PORTO VELHO | RONDÔNIA | Brasil | 1100205 | 11 | 33 | nan | nan | nan | Amazônia | 1.8 |
| 95f73d27-a73a-3ad9-acce-b3f0eaa490e2 | -8.68713 | -62.42129 | 2025-08-31 06:10:00 | NPP-375D | PORTO VELHO | RONDÔNIA | Brasil | 1100205 | 11 | 33 | nan | nan | nan | Amazônia | 1.0 |
| 9ef237fc-c972-30bc-af01-accebd1bef87 | -8.69847 | -62.87723 | 2025-08-31 06:10:00 | NPP-375D | CANDEIAS DO JAMARI | RONDÔNIA | Brasil | 1100809 | 11 | 33 | nan | nan | nan | Amazônia | 0.9 |
| 7b42ee76-3fd6-378d-818f-3bded3649593 | -9.4582 | -62.34002 | 2025-08-31 06:10:00 | NPP-375D | MACHADINHO D'OESTE | RONDÔNIA | Brasil | 1100130 | 11 | 33 | nan | nan | nan | Amazônia | 5.5 |
| 26bf1580-3b41-3af3-b041-ead376c43557 | -8.74648 | -62.39979 | 2025-08-31 06:10:00 | NPP-375D | CUJUBIM | RONDÔNIA | Brasil | 1100940 | 11 | 33 | nan | nan | nan | Amazônia | 1.5 |
| f20184f9-81a0-3317-9559-37762efad708 | -7.5662 | -63.41047 | 2025-08-31 06:10:00 | NPP-375D | CANUTAMA | AMAZONAS | Brasil | 1300904 | 13 | 33 | nan | nan | nan | Amazônia | 0.8 |
| 76a52cbb-0cb3-3066-9656-c5ee137d71a5 | -8.38471 | -70.83434 | 2025-08-31 06:10:00 | NPP-375D | TARAUACÁ | ACRE | Brasil | 1200609 | 12 | 33 | nan | nan | nan | Amazônia | 0.8 |
| 8dc8d2b7-f7f9-39cb-934b-49e99f46c5fc | -11.40995 | -63.23975 | 2025-08-31 06:10:00 | NPP-375D | SÃO MIGUEL DO GUAPORÉ | RONDÔNIA | Brasil | 1100320 | 11 | 33 | nan | nan | nan | Amazônia | 14.6 |
| b3c7e141-0ac3-3619-99f1-208bbda0fd82 | -11.32749 | -63.27264 | 2025-08-31 06:10:00 | NPP-375D | SÃO MIGUEL DO GUAPORÉ | RONDÔNIA | Brasil | 1100320 | 11 | 33 | nan | nan | nan | Amazônia | 3.2 |
| ef156ee1-67a9-32d6-b1ba-611e48c64c67 | -7.46312 | -70.14102 | 2025-08-31 06:10:00 | NPP-375D | ENVIRA | AMAZONAS | Brasil | 1301506 | 13 | 33 | nan | nan | nan | Amazônia | 1.5 |
| 8e65554e-0d92-3dce-a9f0-a30f05f771cb | -10.30674 | -68.26687 | 2025-08-31 06:10:00 | NPP-375D | RIO BRANCO | ACRE | Brasil | 1200401 | 12 | 33 | nan | nan | nan | Amazônia | 1.9 |
| 76d1dcb1-8c5b-3fd4-9803-a738ae5b5029 | -7.46368 | -70.13734 | 2025-08-31 06:10:00 | NPP-375D | ENVIRA | AMAZONAS | Brasil | 1301506 | 13 | 33 | nan | nan | nan | Amazônia | 1.5 |
| 9538ae1c-a746-3d6a-9b56-f633ad6720fa | -8.74848 | -62.3849 | 2025-08-31 06:10:00 | NPP-375D | CUJUBIM | RONDÔNIA | Brasil | 1100940 | 11 | 33 | nan | nan | nan | Amazônia | 0.9 |
| 3307ead8-b033-3a6c-93d2-8f90aae5ea4d | -9.44131 | -62.33772 | 2025-08-31 06:10:00 | NPP-375D | MACHADINHO D'OESTE | RONDÔNIA | Brasil | 1100130 | 11 | 33 | nan | nan | nan | Amazônia | 0.9 |
| 9f6ff2bc-c878-3f9a-97be-05e2ae4c5bef | -9.57255 | -66.69343 | 2025-08-31 06:10:00 | NPP-375D | LÁBREA | AMAZONAS | Brasil | 1302405 | 13 | 33 | nan | nan | nan | Amazônia | 1.0 |
| c4cd19f9-04b6-32b3-996b-d64e4308a189 | -9.57704 | -66.69152 | 2025-08-31 06:10:00 | NPP-375D | LÁBREA | AMAZONAS | Brasil | 1302405 | 13 | 33 | nan | nan | nan | Amazônia | 1.2 |
| e8c9b7f9-714b-37a2-ac5d-dcf21991c649 | -7.46083 | -70.13315 | 2025-08-31 06:10:00 | NPP-375D | ENVIRA | AMAZONAS | Brasil | 1301506 | 13 | 33 | nan | nan | nan | Amazônia | 0.9 |
| 4c4d1ccb-e610-3f2e-a881-e6edb7fe99b0 | -8.92191 | -62.42324 | 2025-08-31 06:10:00 | NPP-375D | CUJUBIM | RONDÔNIA | Brasil | 1100940 | 11 | 33 | nan | nan | nan | Amazônia | 1.7 |


[Clique aqui para ver as próximas entradas](README82.md)
