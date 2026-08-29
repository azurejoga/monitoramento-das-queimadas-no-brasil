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

## Dados Diários - Página 70

| ID | Latitude | Longitude | Data/Hora GMT | Satélite | Município | Estado | País | Município ID | Estado ID | País ID | Dias sem Chuva | Precipitação | Risco de Fogo | Bioma | FRP |
|----|----------|-----------|---------------|----------|-----------|--------|------|--------------|-----------|---------|----------------|--------------|----------------|-------|-----|
| 3d74df43-6d86-30bc-bd92-866b435720f7 | -9.51266 | -65.57625 | 2026-08-29 06:14:00 | NPP-375D | PORTO VELHO | RONDÔNIA | Brasil | 1100205 | 11 | 33 | nan | nan | nan | Amazônia | 2.5 |
| 49aab67c-1409-33b6-a38a-48570a9a49a8 | -11.0429 | -57.23077 | 2026-08-29 06:14:00 | NPP-375D | JUARA | MATO GROSSO | Brasil | 5105101 | 51 | 33 | nan | nan | nan | Amazônia | 3.9 |
| bb0a8787-45f0-3651-8a36-2f132dcf7ad0 | -9.09223 | -65.47895 | 2026-08-29 06:14:00 | NPP-375D | LÁBREA | AMAZONAS | Brasil | 1302405 | 13 | 33 | nan | nan | nan | Amazônia | 1.8 |
| 9e66fdb8-c884-3b2d-86a4-797fa2f203ba | -9.34152 | -68.88885 | 2026-08-29 06:14:00 | NPP-375D | SENA MADUREIRA | ACRE | Brasil | 1200500 | 12 | 33 | nan | nan | nan | Amazônia | 0.8 |
| bb9f80bf-5407-3d65-b0e6-099145856cbe | -8.79224 | -69.37088 | 2026-08-29 06:14:00 | NPP-375D | MANOEL URBANO | ACRE | Brasil | 1200344 | 12 | 33 | nan | nan | nan | Amazônia | 0.5 |
| 4ef54e67-ebf8-3501-a746-0d7f56c7ede9 | -9.51023 | -65.57678 | 2026-08-29 06:14:00 | NPP-375D | PORTO VELHO | RONDÔNIA | Brasil | 1100205 | 11 | 33 | nan | nan | nan | Amazônia | 1.7 |
| 0671391c-bb59-37f8-ae70-7bea24e13861 | -8.456 | -70.41824 | 2026-08-29 06:14:00 | NPP-375D | FEIJÓ | ACRE | Brasil | 1200302 | 12 | 33 | nan | nan | nan | Amazônia | 0.7 |
| 98d05f51-d382-335b-bd16-3f6bda7ce135 | -9.06563 | -65.41546 | 2026-08-29 06:14:00 | NPP-375D | LÁBREA | AMAZONAS | Brasil | 1302405 | 13 | 33 | nan | nan | nan | Amazônia | 1.0 |
| 9600377f-5fd1-3cd8-b6d6-5237034cb595 | -8.37751 | -70.84864 | 2026-08-29 06:14:00 | NPP-375D | TARAUACÁ | ACRE | Brasil | 1200609 | 12 | 33 | nan | nan | nan | Amazônia | 1.5 |
| b7aa5ac0-00d1-3169-a8cf-72d9a5effc40 | -8.63077 | -66.54091 | 2026-08-29 06:14:00 | NPP-375D | LÁBREA | AMAZONAS | Brasil | 1302405 | 13 | 33 | nan | nan | nan | Amazônia | 1.3 |
| f744a702-c32a-3b34-8afc-47506481fc6e | -9.00054 | -65.45885 | 2026-08-29 06:14:00 | NPP-375D | LÁBREA | AMAZONAS | Brasil | 1302405 | 13 | 33 | nan | nan | nan | Amazônia | 1.1 |
| 22bb560d-be93-3f1f-bd27-f51547f7426b | -8.82766 | -70.63497 | 2026-08-29 06:14:00 | NPP-375D | FEIJÓ | ACRE | Brasil | 1200302 | 12 | 33 | nan | nan | nan | Amazônia | 0.8 |
| dee492a0-b9c3-30a7-b698-942fbd0927f2 | -10.47427 | -64.5005 | 2026-08-29 06:14:00 | NPP-375D | NOVA MAMORÉ | RONDÔNIA | Brasil | 1100338 | 11 | 33 | nan | nan | nan | Amazônia | 5.9 |
| 02ff24b6-0ebe-3440-9956-a5e39cd95022 | -10.51088 | -59.63342 | 2026-08-29 06:14:00 | NPP-375D | ARIPUANÃ | MATO GROSSO | Brasil | 5101407 | 51 | 33 | nan | nan | nan | Amazônia | 2.2 |
| 2a6fccae-be31-36ab-b6b6-48b7d2905048 | -8.89865 | -71.3991 | 2026-08-29 06:14:00 | NPP-375D | FEIJÓ | ACRE | Brasil | 1200302 | 12 | 33 | nan | nan | nan | Amazônia | 1.0 |
| 7baf876d-98fd-3629-abb4-87a3c0e41362 | -8.99334 | -65.45025 | 2026-08-29 06:14:00 | NPP-375D | LÁBREA | AMAZONAS | Brasil | 1302405 | 13 | 33 | nan | nan | nan | Amazônia | 0.8 |
| c471c792-45dd-3993-8d35-86c89add02a0 | -9.20622 | -71.85964 | 2026-08-29 06:14:00 | NPP-375D | JORDÃO | ACRE | Brasil | 1200328 | 12 | 33 | nan | nan | nan | Amazônia | 0.7 |
| 55d077d6-b670-378c-a368-28c6c5fdb92b | -8.99522 | -65.44733 | 2026-08-29 06:14:00 | NPP-375D | LÁBREA | AMAZONAS | Brasil | 1302405 | 13 | 33 | nan | nan | nan | Amazônia | 0.9 |
| 1912f90c-7f09-3260-a9c5-5fa5211e7f25 | -9.92472 | -60.43843 | 2026-08-29 06:14:00 | NPP-375D | ARIPUANÃ | MATO GROSSO | Brasil | 5101407 | 51 | 33 | nan | nan | nan | Amazônia | 1.9 |
| 2fd38c0a-0aa4-32a2-8469-b9a3db79d44d | -9.51434 | -65.57737 | 2026-08-29 06:14:00 | NPP-375D | PORTO VELHO | RONDÔNIA | Brasil | 1100205 | 11 | 33 | nan | nan | nan | Amazônia | 1.7 |
| 15e425c6-025f-3522-9ff4-b25c86069a51 | -8.60041 | -70.20541 | 2026-08-29 06:14:00 | NPP-375D | FEIJÓ | ACRE | Brasil | 1200302 | 12 | 33 | nan | nan | nan | Amazônia | 1.3 |
| b9f7a16b-ccbd-313a-ba35-f2fea17a81b3 | -8.35681 | -71.06002 | 2026-08-29 06:14:00 | NPP-375D | TARAUACÁ | ACRE | Brasil | 1200609 | 12 | 33 | nan | nan | nan | Amazônia | 0.5 |
| 8f7bc403-836b-3698-9a47-7cbd4d63a0c9 | -9.93059 | -60.4391 | 2026-08-29 06:14:00 | NPP-375D | ARIPUANÃ | MATO GROSSO | Brasil | 5101407 | 51 | 33 | nan | nan | nan | Amazônia | 2.6 |
| fe22ca38-1da0-3c9d-8c70-1c35770f0d54 | -10.5544 | -59.62052 | 2026-08-29 06:14:00 | NPP-375D | ARIPUANÃ | MATO GROSSO | Brasil | 5101407 | 51 | 33 | nan | nan | nan | Amazônia | 1.6 |
| bf74f645-25b2-3e17-84f2-1924b7e0c308 | -10.47489 | -64.49602 | 2026-08-29 06:14:00 | NPP-375D | NOVA MAMORÉ | RONDÔNIA | Brasil | 1100338 | 11 | 33 | nan | nan | nan | Amazônia | 5.8 |
| cbba785a-3f67-3a26-92bc-54d6e92af000 | -7.00472 | -71.66028 | 2026-08-29 06:14:00 | NPP-375D | IPIXUNA | AMAZONAS | Brasil | 1301803 | 13 | 33 | nan | nan | nan | Amazônia | 3.9 |
| 8d226259-5d0f-30e6-bbbe-1ae5faf31580 | -9.04645 | -65.43163 | 2026-08-29 06:14:00 | NPP-375D | LÁBREA | AMAZONAS | Brasil | 1302405 | 13 | 33 | nan | nan | nan | Amazônia | 1.1 |
| 4b76c4ef-f942-3b48-98a9-4fc93e8ba639 | -9.5138 | -65.58106 | 2026-08-29 06:14:00 | NPP-375D | PORTO VELHO | RONDÔNIA | Brasil | 1100205 | 11 | 33 | nan | nan | nan | Amazônia | 4.0 |
| 8a349a75-70db-32e7-823d-a2b3fb2c4bb8 | -8.5283 | -70.85535 | 2026-08-29 06:14:00 | NPP-375D | TARAUACÁ | ACRE | Brasil | 1200609 | 12 | 33 | nan | nan | nan | Amazônia | 0.5 |
| 5327c4b5-fb52-380e-a82f-f340edca67eb | -10.48324 | -64.50175 | 2026-08-29 06:14:00 | NPP-375D | NOVA MAMORÉ | RONDÔNIA | Brasil | 1100338 | 11 | 33 | nan | nan | nan | Amazônia | 14.3 |
| 4c0e5a5a-44d4-371f-84ba-28dc38e75095 | -10.50293 | -59.62856 | 2026-08-29 06:14:00 | NPP-375D | ARIPUANÃ | MATO GROSSO | Brasil | 5101407 | 51 | 33 | nan | nan | nan | Amazônia | 0.9 |
| 32a00a6b-76dd-3465-9858-d33f22c3cda1 | -7.54737 | -70.0027 | 2026-08-29 06:14:00 | NPP-375D | ENVIRA | AMAZONAS | Brasil | 1301506 | 13 | 33 | nan | nan | nan | Amazônia | 1.5 |
| f038bea2-70ad-3303-9704-0aaa5cd1c758 | -8.59932 | -70.21242 | 2026-08-29 06:14:00 | NPP-375D | FEIJÓ | ACRE | Brasil | 1200302 | 12 | 33 | nan | nan | nan | Amazônia | 0.9 |
| 047a982f-5dde-3032-9284-6b1d92bf9871 | -9.35296 | -67.80114 | 2026-08-29 06:14:00 | NPP-375D | BOCA DO ACRE | AMAZONAS | Brasil | 1300706 | 13 | 33 | nan | nan | nan | Amazônia | 1.0 |
| 692f6746-9904-3547-a0cf-0f2f78ea1bb3 | -8.95878 | -62.40609 | 2026-08-29 06:14:00 | NPP-375D | CUJUBIM | RONDÔNIA | Brasil | 1100940 | 11 | 33 | nan | nan | nan | Amazônia | 0.6 |
| 4d551e4d-9a34-3638-a01a-4c044733b836 | -7.54792 | -69.99921 | 2026-08-29 06:14:00 | NPP-375D | ENVIRA | AMAZONAS | Brasil | 1301506 | 13 | 33 | nan | nan | nan | Amazônia | 1.5 |
| 6f815e42-4f60-31f5-896d-921f6de7d2bf | -7.59116 | -61.34346 | 2026-08-29 06:14:00 | NPP-375D | MANICORÉ | AMAZONAS | Brasil | 1302702 | 13 | 33 | nan | nan | nan | Amazônia | 1.1 |
| 90c84830-f663-3cd1-8d6e-507d358e0c9d | -8.65686 | -70.75081 | 2026-08-29 06:14:00 | NPP-375D | FEIJÓ | ACRE | Brasil | 1200302 | 12 | 33 | nan | nan | nan | Amazônia | 0.5 |
| 60b975de-675b-357b-8fb9-a11ff7dd2cc0 | -8.60542 | -70.21696 | 2026-08-29 06:14:00 | NPP-375D | FEIJÓ | ACRE | Brasil | 1200302 | 12 | 33 | nan | nan | nan | Amazônia | 4.6 |
| 1739baf4-94ab-3368-8d15-e0eb3138ae3e | -8.95737 | -62.37878 | 2026-08-29 06:14:00 | NPP-375D | CUJUBIM | RONDÔNIA | Brasil | 1100940 | 11 | 33 | nan | nan | nan | Amazônia | 1.5 |
| 3b97fa80-1421-37cc-93b9-a733f3768ccd | -11.03315 | -57.25132 | 2026-08-29 06:14:00 | NPP-375D | JUARA | MATO GROSSO | Brasil | 5105101 | 51 | 33 | nan | nan | nan | Amazônia | 2.8 |
| aeb30cf3-eab1-3ea8-bcae-32ce9b04cce9 | -7.92583 | -70.66549 | 2026-08-29 06:14:00 | NPP-375D | TARAUACÁ | ACRE | Brasil | 1200609 | 12 | 33 | nan | nan | nan | Amazônia | 0.5 |
| af341622-0f83-3a59-9fcb-40d7f3a24af7 | -9.9993 | -66.86529 | 2026-08-29 06:14:00 | NPP-375D | ACRELÂNDIA | ACRE | Brasil | 1200013 | 12 | 33 | nan | nan | nan | Amazônia | 0.7 |
| 17b44a62-8ab0-3290-b9eb-5a95890e8dcf | -11.03891 | -57.21436 | 2026-08-29 06:14:00 | NPP-375D | JUARA | MATO GROSSO | Brasil | 5105101 | 51 | 33 | nan | nan | nan | Amazônia | 2.9 |
| 11e9ffad-9ce1-3b09-a54f-15aba43b56cb | -6.77161 | -63.04712 | 2026-08-29 06:14:00 | NPP-375D | TAPAUÁ | AMAZONAS | Brasil | 1304104 | 13 | 33 | nan | nan | nan | Amazônia | 2.7 |
| 590debda-ab36-3f9f-9f88-8dbe66018c46 | -7.55834 | -61.30457 | 2026-08-29 06:14:00 | NPP-375D | MANICORÉ | AMAZONAS | Brasil | 1302702 | 13 | 33 | nan | nan | nan | Amazônia | 1.3 |
| 10ccd122-5bb6-3aef-975d-8e9f09977ad0 | -8.33322 | -70.72009 | 2026-08-29 06:14:00 | NPP-375D | TARAUACÁ | ACRE | Brasil | 1200609 | 12 | 33 | nan | nan | nan | Amazônia | 1.2 |
| 6859a0b5-9adc-3bc1-94df-9278f7e0f232 | -7.56971 | -61.38086 | 2026-08-29 06:14:00 | NPP-375D | MANICORÉ | AMAZONAS | Brasil | 1302702 | 13 | 33 | nan | nan | nan | Amazônia | 1.8 |
| 8c87ce45-4648-364b-8b8b-ed772edc0c54 | -9.87331 | -65.02592 | 2026-08-29 06:14:00 | NPP-375D | PORTO VELHO | RONDÔNIA | Brasil | 1100205 | 11 | 33 | nan | nan | nan | Amazônia | 1.1 |
| 9f8f36df-c18d-39fc-a344-7a2720dc70cb | -10.50976 | -59.62424 | 2026-08-29 06:14:00 | NPP-375D | ARIPUANÃ | MATO GROSSO | Brasil | 5101407 | 51 | 33 | nan | nan | nan | Amazônia | 1.5 |
| 5ca7685a-8215-35cf-a0a0-8b3515f1a758 | -7.59603 | -61.34754 | 2026-08-29 06:14:00 | NPP-375D | MANICORÉ | AMAZONAS | Brasil | 1302702 | 13 | 33 | nan | nan | nan | Amazônia | 1.1 |
| f9e4eb7d-f680-3f1b-b3da-7de849d038ee | -8.99577 | -65.44366 | 2026-08-29 06:14:00 | NPP-375D | LÁBREA | AMAZONAS | Brasil | 1302405 | 13 | 33 | nan | nan | nan | Amazônia | 2.2 |
| 66eaf686-a94e-3565-9bc7-b186b9b9d1e4 | -9.04232 | -65.43105 | 2026-08-29 06:14:00 | NPP-375D | LÁBREA | AMAZONAS | Brasil | 1302405 | 13 | 33 | nan | nan | nan | Amazônia | 1.1 |
| 8b486aec-d095-31c1-9866-aa2d5790c0d1 | -9.86474 | -65.02464 | 2026-08-29 06:14:00 | NPP-375D | PORTO VELHO | RONDÔNIA | Brasil | 1100205 | 11 | 33 | nan | nan | nan | Amazônia | 0.7 |
| bbd42e9f-40c2-31ea-b348-7a1ac54cf08f | -8.82489 | -70.63094 | 2026-08-29 06:14:00 | NPP-375D | FEIJÓ | ACRE | Brasil | 1200302 | 12 | 33 | nan | nan | nan | Amazônia | 0.8 |
| f474346b-e8fa-3d56-af4e-2bee806bd615 | -9.06456 | -65.42288 | 2026-08-29 06:14:00 | NPP-375D | LÁBREA | AMAZONAS | Brasil | 1302405 | 13 | 33 | nan | nan | nan | Amazônia | 0.7 |
| 046ed34a-8284-33d7-a4f2-c6fa074408e3 | -10.2793 | -68.86521 | 2026-08-29 06:14:00 | NPP-375D | RIO BRANCO | ACRE | Brasil | 1200401 | 12 | 33 | nan | nan | nan | Amazônia | 0.7 |
| d640c9fe-4603-3f85-a1ad-412d370338d0 | -10.20333 | -69.36182 | 2026-08-29 06:14:00 | NPP-375D | SENA MADUREIRA | ACRE | Brasil | 1200500 | 12 | 33 | nan | nan | nan | Amazônia | 1.2 |
| 8ba27b2e-bab5-3e38-8408-a8b2941a61d0 | -8.93307 | -62.40539 | 2026-08-29 06:14:00 | NPP-375D | CUJUBIM | RONDÔNIA | Brasil | 1100940 | 11 | 33 | nan | nan | nan | Amazônia | 1.6 |
| 931a7e5d-2d93-3271-94a1-bbf713d3b674 | -8.95456 | -63.27947 | 2026-08-29 06:14:00 | NPP-375D | ITAPUÃ DO OESTE | RONDÔNIA | Brasil | 1101104 | 11 | 33 | nan | nan | nan | Amazônia | 5.9 |
| e50847cc-934b-3a08-9e23-d2e7e5979a70 | -11.04446 | -57.23 | 2026-08-29 06:14:00 | NPP-375D | JUARA | MATO GROSSO | Brasil | 5105101 | 51 | 33 | nan | nan | nan | Amazônia | 3.6 |
| d546239d-4c94-30d3-b96e-7773f16e0958 | -8.95331 | -62.40831 | 2026-08-29 06:14:00 | NPP-375D | CUJUBIM | RONDÔNIA | Brasil | 1100940 | 11 | 33 | nan | nan | nan | Amazônia | 0.8 |
| 0488e5a2-5d1a-341e-8ed9-5a9ccc3b15c0 | -8.42532 | -70.20236 | 2026-08-29 06:14:00 | NPP-375D | FEIJÓ | ACRE | Brasil | 1200302 | 12 | 33 | nan | nan | nan | Amazônia | 0.8 |
| 37993a33-be11-37a1-bdd4-1c9c5be3888e | -10.50353 | -59.62354 | 2026-08-29 06:14:00 | NPP-375D | ARIPUANÃ | MATO GROSSO | Brasil | 5101407 | 51 | 33 | nan | nan | nan | Amazônia | 0.9 |
| bdd0ead6-4d30-348a-a2de-e747a50bcf6c | -8.9443 | -63.28326 | 2026-08-29 06:14:00 | NPP-375D | ITAPUÃ DO OESTE | RONDÔNIA | Brasil | 1101104 | 11 | 33 | nan | nan | nan | Amazônia | 8.0 |
| 2c960dec-9974-3f91-9f7d-379905305dea | -8.86596 | -70.90564 | 2026-08-29 06:14:00 | NPP-375D | FEIJÓ | ACRE | Brasil | 1200302 | 12 | 33 | nan | nan | nan | Amazônia | 0.8 |
| 6b704302-2b40-3f46-8caa-4b1ea7af3cc9 | -9.53385 | -67.43678 | 2026-08-29 06:14:00 | NPP-375D | BOCA DO ACRE | AMAZONAS | Brasil | 1300706 | 13 | 33 | nan | nan | nan | Amazônia | 1.2 |
| a09ff58a-66a2-3b14-9be1-c6d8605dab38 | -8.60319 | -70.20945 | 2026-08-29 06:14:00 | NPP-375D | FEIJÓ | ACRE | Brasil | 1200302 | 12 | 33 | nan | nan | nan | Amazônia | 0.9 |
| 1d4efe88-2f19-34af-86a9-7e3d7d0f0641 | -9.20737 | -67.78053 | 2026-08-29 06:14:00 | NPP-375D | BOCA DO ACRE | AMAZONAS | Brasil | 1300706 | 13 | 33 | nan | nan | nan | Amazônia | 0.6 |
| 2f76668c-9823-3930-9f8a-ef45c9015cdc | -9.86788 | -65.0334 | 2026-08-29 06:14:00 | NPP-375D | PORTO VELHO | RONDÔNIA | Brasil | 1100205 | 11 | 33 | nan | nan | nan | Amazônia | 1.6 |
| 0070eccf-b68c-3876-b622-8311de713486 | -9.87235 | -60.29684 | 2026-08-29 06:14:00 | NPP-375D | ARIPUANÃ | MATO GROSSO | Brasil | 5101407 | 51 | 33 | nan | nan | nan | Amazônia | 1.8 |
| 361f712a-b641-33ce-b226-e9f24620dccd | -8.59987 | -70.20892 | 2026-08-29 06:14:00 | NPP-375D | FEIJÓ | ACRE | Brasil | 1200302 | 12 | 33 | nan | nan | nan | Amazônia | 0.9 |
| 0798d516-7f97-3f0b-b0ed-40aa2620aa11 | -11.02765 | -57.2497 | 2026-08-29 06:14:00 | NPP-375D | JUARA | MATO GROSSO | Brasil | 5105101 | 51 | 33 | nan | nan | nan | Amazônia | 3.0 |
| bd49adb5-1ffe-3512-a20b-bb4cc28459c2 | -9.87181 | -60.30107 | 2026-08-29 06:14:00 | NPP-375D | ARIPUANÃ | MATO GROSSO | Brasil | 5101407 | 51 | 33 | nan | nan | nan | Amazônia | 1.8 |
| 1bb96ae3-3b7b-334b-911a-2ea50e87e46d | -8.90199 | -71.39964 | 2026-08-29 06:14:00 | NPP-375D | FEIJÓ | ACRE | Brasil | 1200302 | 12 | 33 | nan | nan | nan | Amazônia | 1.0 |
| 5f1f462a-e66a-3bd6-b25e-a11474ea22cf | -9.51214 | -65.57996 | 2026-08-29 06:14:00 | NPP-375D | PORTO VELHO | RONDÔNIA | Brasil | 1100205 | 11 | 33 | nan | nan | nan | Amazônia | 3.2 |
| 942dd319-5b3b-3f35-89cb-fd30f63d31f9 | -9.48377 | -66.62746 | 2026-08-29 06:14:00 | NPP-375D | LÁBREA | AMAZONAS | Brasil | 1302405 | 13 | 33 | nan | nan | nan | Amazônia | 1.1 |
| 3f9eea89-4009-3d14-b9bf-26181e5a4a30 | -9.50969 | -65.58048 | 2026-08-29 06:14:00 | NPP-375D | PORTO VELHO | RONDÔNIA | Brasil | 1100205 | 11 | 33 | nan | nan | nan | Amazônia | 4.0 |
| a4100e19-a056-304f-a6e3-ea610b95dca2 | -10.56068 | -59.62082 | 2026-08-29 06:14:00 | NPP-375D | ARIPUANÃ | MATO GROSSO | Brasil | 5101407 | 51 | 33 | nan | nan | nan | Amazônia | 0.9 |
| ecd6303f-f408-326e-8c05-018a00344c25 | -9.17864 | -70.89532 | 2026-08-29 06:14:00 | NPP-375D | FEIJÓ | ACRE | Brasil | 1200302 | 12 | 33 | nan | nan | nan | Amazônia | 1.4 |
| 3810bc6d-402a-31ef-8376-79a20b7031e6 | -8.24839 | -70.10297 | 2026-08-29 06:14:00 | NPP-375D | FEIJÓ | ACRE | Brasil | 1200302 | 12 | 33 | nan | nan | nan | Amazônia | 1.7 |
| 055db3a6-0176-3e24-a6b0-8dd47b71e077 | -8.95696 | -62.38174 | 2026-08-29 06:14:00 | NPP-375D | CUJUBIM | RONDÔNIA | Brasil | 1100940 | 11 | 33 | nan | nan | nan | Amazônia | 1.5 |
| 4d6d401d-22e2-3b38-9074-66a8ed15d973 | -8.95413 | -62.4024 | 2026-08-29 06:14:00 | NPP-375D | CUJUBIM | RONDÔNIA | Brasil | 1100940 | 11 | 33 | nan | nan | nan | Amazônia | 1.3 |
| b8670c5e-77f5-3819-8943-a64c725ae683 | -8.95615 | -62.38765 | 2026-08-29 06:14:00 | NPP-375D | CUJUBIM | RONDÔNIA | Brasil | 1100940 | 11 | 33 | nan | nan | nan | Amazônia | 1.2 |
| 39a0043c-4e4a-3ffa-a641-d4e684191901 | -9.88861 | -66.99477 | 2026-08-29 06:14:00 | NPP-375D | ACRELÂNDIA | ACRE | Brasil | 1200013 | 12 | 33 | nan | nan | nan | Amazônia | 1.2 |
| 6e3f7920-616c-3677-a74c-1267e3b843c6 | -10.39277 | -61.23831 | 2026-08-29 06:14:00 | NPP-375D | RONDOLÂNDIA | MATO GROSSO | Brasil | 5107578 | 51 | 33 | nan | nan | nan | Amazônia | 1.7 |
| 4b47a307-2364-38b6-ba93-e3792c5409ca | -9.25543 | -65.50274 | 2026-08-29 06:14:00 | NPP-375D | LÁBREA | AMAZONAS | Brasil | 1302405 | 13 | 33 | nan | nan | nan | Amazônia | 1.1 |
| 68907490-5500-35da-bd8e-6b89cc9c261a | -8.60652 | -70.20998 | 2026-08-29 06:14:00 | NPP-375D | FEIJÓ | ACRE | Brasil | 1200302 | 12 | 33 | nan | nan | nan | Amazônia | 2.2 |
| 8f868afa-223c-3ab7-b06a-4949d3fc05b8 | -7.5907 | -61.34679 | 2026-08-29 06:14:00 | NPP-375D | MANICORÉ | AMAZONAS | Brasil | 1302702 | 13 | 33 | nan | nan | nan | Amazônia | 1.1 |
| 12031123-ac8c-30f2-8dbc-bed396f7f517 | -7.00868 | -71.65722 | 2026-08-29 06:14:00 | NPP-375D | IPIXUNA | AMAZONAS | Brasil | 1301803 | 13 | 33 | nan | nan | nan | Amazônia | 3.4 |
| ee7c9ed8-197c-3d7f-a9f4-5279869c872c | -11.04377 | -57.22342 | 2026-08-29 06:14:00 | NPP-375D | JUARA | MATO GROSSO | Brasil | 5105101 | 51 | 33 | nan | nan | nan | Amazônia | 2.8 |
| 242de320-ba0d-31af-96c0-fbabc1fb376c | -11.02594 | -57.25052 | 2026-08-29 06:14:00 | NPP-375D | JUARA | MATO GROSSO | Brasil | 5105101 | 51 | 33 | nan | nan | nan | Amazônia | 1.6 |
| db5661c6-74a5-3b2b-be82-081a5214bb15 | -8.95528 | -63.27435 | 2026-08-29 06:14:00 | NPP-375D | ITAPUÃ DO OESTE | RONDÔNIA | Brasil | 1101104 | 11 | 33 | nan | nan | nan | Amazônia | 5.9 |
| 0b96e559-32e8-35e0-8114-a19463b5e0a9 | -10.46979 | -64.49988 | 2026-08-29 06:14:00 | NPP-375D | NOVA MAMORÉ | RONDÔNIA | Brasil | 1100338 | 11 | 33 | nan | nan | nan | Amazônia | 5.9 |
| b52f6788-9b92-3b2f-98ae-cd0e737c5502 | -7.58673 | -61.33606 | 2026-08-29 06:14:00 | NPP-375D | MANICORÉ | AMAZONAS | Brasil | 1302702 | 13 | 33 | nan | nan | nan | Amazônia | 1.6 |
| fc9361d7-478a-3288-8707-479377664d9d | -8.95149 | -62.38397 | 2026-08-29 06:14:00 | NPP-375D | CUJUBIM | RONDÔNIA | Brasil | 1100940 | 11 | 33 | nan | nan | nan | Amazônia | 1.2 |
| 78c30bb9-bff6-34be-9dad-e8d293fd609f | -8.80333 | -70.78841 | 2026-08-29 06:14:00 | NPP-375D | FEIJÓ | ACRE | Brasil | 1200302 | 12 | 33 | nan | nan | nan | Amazônia | 0.5 |
| 51d5b5d8-3b76-35bf-8f1e-4d7f50590790 | -10.5059 | -59.6228 | 2026-08-29 06:14:00 | NPP-375D | ARIPUANÃ | MATO GROSSO | Brasil | 5101407 | 51 | 33 | nan | nan | nan | Amazônia | 1.2 |
| 82380e09-7d27-3d4a-b4c3-294df547c541 | -9.02675 | -70.91704 | 2026-08-29 06:14:00 | NPP-375D | FEIJÓ | ACRE | Brasil | 1200302 | 12 | 33 | nan | nan | nan | Amazônia | 0.8 |
| cb143b7a-b4e6-333a-b253-cd3dce83312e | -9.20156 | -71.83729 | 2026-08-29 06:14:00 | NPP-375D | JORDÃO | ACRE | Brasil | 1200328 | 12 | 33 | nan | nan | nan | Amazônia | 0.7 |


[Clique aqui para ver as próximas entradas](README71.md)
