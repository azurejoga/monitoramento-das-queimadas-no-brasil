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

## Dados Diários - Página 62

| ID | Latitude | Longitude | Data/Hora GMT | Satélite | Município | Estado | País | Município ID | Estado ID | País ID | Dias sem Chuva | Precipitação | Risco de Fogo | Bioma | FRP |
|----|----------|-----------|---------------|----------|-----------|--------|------|--------------|-----------|---------|----------------|--------------|----------------|-------|-----|
| 6f309908-125f-399f-8716-44b675e3f1e2 | -6.75972 | -59.46803 | 2026-08-20 05:42:00 | NPP-375D | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 2.5 |
| 81488b43-f456-321b-890a-028c84fe365c | -8.49814 | -54.86839 | 2026-08-20 05:42:00 | NPP-375D | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 2.1 |
| 6a698eb4-edd5-3488-977c-4972629dce69 | -8.57098 | -54.6758 | 2026-08-20 05:42:00 | NPP-375D | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 2.0 |
| f3d8d6a5-33db-3aaf-9f50-b6e767439165 | -6.6981 | -59.09217 | 2026-08-20 05:42:00 | NPP-375D | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 2.7 |
| 94c7cdc6-247b-379d-89a2-e8981d0d5d46 | -6.70473 | -59.0975 | 2026-08-20 05:42:00 | NPP-375D | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 2.7 |
| 0ecca679-11c1-3efc-8ab2-75c1b1b4166a | -7.4652 | -55.30095 | 2026-08-20 05:42:00 | NPP-375D | NOVO PROGRESSO | PARÁ | Brasil | 1505031 | 15 | 33 | nan | nan | nan | Amazônia | 3.0 |
| 62eba70c-28b1-33bb-81b8-f0c8f4b952a1 | -8.28165 | -62.72547 | 2026-08-20 05:42:00 | NPP-375D | PORTO VELHO | RONDÔNIA | Brasil | 1100205 | 11 | 33 | nan | nan | nan | Amazônia | 1.3 |
| accbc054-a425-3ba8-977a-7f5cb41bd433 | -6.58557 | -58.97269 | 2026-08-20 05:42:00 | NPP-375D | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 6.2 |
| 9abf2679-c493-3d49-9d4e-dfb30d0e815d | -8.53498 | -54.87049 | 2026-08-20 05:42:00 | NPP-375D | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 2.8 |
| 859c4f0a-e61c-3298-92fb-93e0eeb205f8 | -13.44557 | -51.43129 | 2026-08-20 05:42:00 | NPP-375D | CANARANA | MATO GROSSO | Brasil | 5102702 | 51 | 33 | nan | nan | nan | Cerrado | 3.5 |
| 4c6659a2-cdfe-3327-9f32-12418f1ce336 | -8.50982 | -54.89223 | 2026-08-20 05:42:00 | NPP-375D | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 2.2 |
| 5e491b55-5808-3f73-89e6-9ad02247d96c | -6.74292 | -59.04268 | 2026-08-20 05:42:00 | NPP-375D | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 1.6 |
| c20c5239-5a99-36b2-a9df-4b69c806b5b6 | -9.12023 | -61.60617 | 2026-08-20 05:42:00 | NPP-375D | MACHADINHO D'OESTE | RONDÔNIA | Brasil | 1100130 | 11 | 33 | nan | nan | nan | Amazônia | 1.1 |
| d65ea89d-cfc5-34c8-8652-50df0d643646 | -13.54319 | -52.22524 | 2026-08-20 05:42:00 | NPP-375D | CANARANA | MATO GROSSO | Brasil | 5102702 | 51 | 33 | nan | nan | nan | Cerrado | 5.5 |
| 670ad2d2-eaf2-3835-9385-ae2996f762ba | -11.18491 | -54.02802 | 2026-08-20 05:42:00 | NPP-375D | MARCELÂNDIA | MATO GROSSO | Brasil | 5105580 | 51 | 33 | nan | nan | nan | Amazônia | 1.5 |
| a825e1bd-0160-3e30-9791-094d311c649a | -8.56331 | -54.65714 | 2026-08-20 05:42:00 | NPP-375D | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 2.3 |
| 84f75c12-6a1c-3806-8600-013483372d82 | -13.54534 | -52.22426 | 2026-08-20 05:42:00 | NPP-375D | CANARANA | MATO GROSSO | Brasil | 5102702 | 51 | 33 | nan | nan | nan | Cerrado | 5.8 |
| d3dbc5c1-9bb3-3e5e-9fbe-b3b32924f774 | -7.82563 | -61.60279 | 2026-08-20 05:42:00 | NPP-375D | MANICORÉ | AMAZONAS | Brasil | 1302702 | 13 | 33 | nan | nan | nan | Amazônia | 0.7 |
| aee4f541-dcd1-375b-8f2b-23f479167fc5 | -10.39579 | -61.20459 | 2026-08-20 05:42:00 | NPP-375D | RONDOLÂNDIA | MATO GROSSO | Brasil | 5107578 | 51 | 33 | nan | nan | nan | Amazônia | 3.6 |
| 06549bce-9c2b-3c8c-a79b-14446a09de8d | -6.69746 | -59.09641 | 2026-08-20 05:42:00 | NPP-375D | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 2.7 |
| 868236b0-b436-316e-b034-e23777e6b7b7 | -7.37987 | -55.54195 | 2026-08-20 05:42:00 | NPP-375D | NOVO PROGRESSO | PARÁ | Brasil | 1505031 | 15 | 33 | nan | nan | nan | Amazônia | 2.0 |
| cb394d5f-58d6-34c5-9b28-82e162ea0c92 | -8.71151 | -49.61236 | 2026-08-20 05:42:00 | NPP-375D | CONCEIÇÃO DO ARAGUAIA | PARÁ | Brasil | 1502707 | 15 | 33 | nan | nan | nan | Amazônia | 0.9 |
| bfa065de-3bee-371c-b075-27a32b4c18ee | -8.89608 | -60.55038 | 2026-08-20 05:42:00 | NPP-375D | COLNIZA | MATO GROSSO | Brasil | 5103254 | 51 | 33 | nan | nan | nan | Amazônia | 1.3 |
| 39edbe5f-5c69-3095-8ebb-5d9656c3509d | -8.57373 | -54.76851 | 2026-08-20 05:42:00 | NPP-375D | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 1.3 |
| 86829fc2-09f4-31b2-926e-ed3b59d2b553 | -6.71201 | -59.09855 | 2026-08-20 05:42:00 | NPP-375D | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 1.4 |
| 42741655-6286-343f-a783-952d89297b58 | -10.38776 | -61.21106 | 2026-08-20 05:42:00 | NPP-375D | RONDOLÂNDIA | MATO GROSSO | Brasil | 5107578 | 51 | 33 | nan | nan | nan | Amazônia | 3.1 |
| 07182177-8223-3540-8aef-d6f742d20c09 | -11.19299 | -54.00794 | 2026-08-20 05:42:00 | NPP-375D | MARCELÂNDIA | MATO GROSSO | Brasil | 5105580 | 51 | 33 | nan | nan | nan | Amazônia | 3.2 |
| d756fd11-68c7-3dd2-a4fa-27a848dd4799 | -13.54478 | -52.22917 | 2026-08-20 05:42:00 | NPP-375D | CANARANA | MATO GROSSO | Brasil | 5102702 | 51 | 33 | nan | nan | nan | Cerrado | 15.9 |
| 82723d10-5471-3958-a502-91969a61a946 | -6.72058 | -59.09116 | 2026-08-20 05:42:00 | NPP-375D | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 1.4 |
| 59717491-df72-36bb-be06-c606502b4e2a | -8.67561 | -54.65075 | 2026-08-20 05:42:00 | NPP-375D | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 2.3 |
| 840e6734-d29c-37b1-bb9d-06e32848c51d | -9.41859 | -60.4309 | 2026-08-20 05:42:00 | NPP-375D | ARIPUANÃ | MATO GROSSO | Brasil | 5101407 | 51 | 33 | nan | nan | nan | Amazônia | 10.7 |
| d0846bee-123e-39e8-9142-29a1bc7a415c | -8.66409 | -54.5901 | 2026-08-20 05:42:00 | NPP-375D | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 1.0 |
| 0e838558-9274-3f30-8055-fb8372e65ed2 | -8.53984 | -54.87156 | 2026-08-20 05:42:00 | NPP-375D | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 2.8 |
| d76dc18e-f35f-3cfb-abb9-3903b05f49ff | -9.05522 | -57.0694 | 2026-08-20 05:42:00 | NPP-375D | JACAREACANGA | PARÁ | Brasil | 1503754 | 15 | 33 | nan | nan | nan | Amazônia | 2.3 |
| 920d0533-96d0-3795-99ee-be6c2ecec14c | -10.38203 | -61.20247 | 2026-08-20 05:42:00 | NPP-375D | RONDOLÂNDIA | MATO GROSSO | Brasil | 5107578 | 51 | 33 | nan | nan | nan | Amazônia | 0.4 |
| 6498e3e1-6233-3af6-8a21-45e8bb13b5ef | -9.02397 | -60.49712 | 2026-08-20 05:42:00 | NPP-375D | COLNIZA | MATO GROSSO | Brasil | 5103254 | 51 | 33 | nan | nan | nan | Amazônia | 3.3 |
| 9574ae5f-9cf6-3efd-89a7-4d12949543e3 | -10.39923 | -61.20514 | 2026-08-20 05:42:00 | NPP-375D | RONDOLÂNDIA | MATO GROSSO | Brasil | 5107578 | 51 | 33 | nan | nan | nan | Amazônia | 8.2 |
| d266949f-f6a2-31bc-960e-f1a852b51c94 | -7.60626 | -60.94695 | 2026-08-20 05:42:00 | NPP-375D | NOVO ARIPUANÃ | AMAZONAS | Brasil | 1303304 | 13 | 33 | nan | nan | nan | Amazônia | 1.0 |
| 0c969f13-bb81-3b1b-9516-6b4c943adb46 | -7.43267 | -59.80185 | 2026-08-20 05:42:00 | NPP-375D | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 1.1 |
| eec7fca3-984c-34c9-8b96-066de4b38086 | -11.1975 | -54.01558 | 2026-08-20 05:42:00 | NPP-375D | MARCELÂNDIA | MATO GROSSO | Brasil | 5105580 | 51 | 33 | nan | nan | nan | Amazônia | 2.7 |
| fdc3e1aa-d70b-390f-8c3d-b29d10c70973 | -13.45124 | -51.43225 | 2026-08-20 05:42:00 | NPP-375D | CANARANA | MATO GROSSO | Brasil | 5102702 | 51 | 33 | nan | nan | nan | Cerrado | 1.1 |
| 48a974b1-c48e-3ffa-be55-55d13a7af3c2 | -7.04973 | -56.60993 | 2026-08-20 05:42:00 | NPP-375D | ITAITUBA | PARÁ | Brasil | 1503606 | 15 | 33 | nan | nan | nan | Amazônia | 1.1 |
| 2cf6d2ce-2ca0-3f96-88ac-61d4bfe32b7e | -11.83283 | -58.84082 | 2026-08-20 05:42:00 | NPP-375D | JUÍNA | MATO GROSSO | Brasil | 5105150 | 51 | 33 | nan | nan | nan | Cerrado | 2.4 |
| ce5bdf86-831a-32fb-aeec-0bd1c2e10ad4 | -6.76401 | -59.14772 | 2026-08-20 05:42:00 | NPP-375D | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 1.0 |
| 0dd1ea2e-428b-3a5c-9fa3-8f8673886751 | -7.3417 | -55.67537 | 2026-08-20 05:42:00 | NPP-375D | NOVO PROGRESSO | PARÁ | Brasil | 1505031 | 15 | 33 | nan | nan | nan | Amazônia | 3.1 |
| d4d91019-6465-3ce6-a2b1-96a391f3a3b5 | -7.43327 | -59.79789 | 2026-08-20 05:42:00 | NPP-375D | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 0.9 |
| 95ee635e-1129-3439-b7bc-edc2d9686bf7 | -11.21721 | -54.00687 | 2026-08-20 05:42:00 | NPP-375D | MARCELÂNDIA | MATO GROSSO | Brasil | 5105580 | 51 | 33 | nan | nan | nan | Amazônia | 2.1 |
| 42bdf477-5035-3225-ac92-7e3b13df8c2e | -7.53332 | -55.57407 | 2026-08-20 05:42:00 | NPP-375D | NOVO PROGRESSO | PARÁ | Brasil | 1505031 | 15 | 33 | nan | nan | nan | Amazônia | 2.9 |
| e99e70a6-b988-3bdc-a5c0-6f433d91bf4a | -8.29218 | -62.89494 | 2026-08-20 05:42:00 | NPP-375D | PORTO VELHO | RONDÔNIA | Brasil | 1100205 | 11 | 33 | nan | nan | nan | Amazônia | 1.1 |
| 8b9b5215-7e8c-36fa-b360-b1eb9df6b8dd | -7.77585 | -61.15904 | 2026-08-20 05:42:00 | NPP-375D | NOVO ARIPUANÃ | AMAZONAS | Brasil | 1303304 | 13 | 33 | nan | nan | nan | Amazônia | 0.7 |
| 17f99844-6ca7-346d-828d-70f764d8c9a4 | -6.79519 | -59.58758 | 2026-08-20 05:42:00 | NPP-375D | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 2.8 |
| 5a7c1185-d4a3-3a03-a764-30dc45f512c0 | -8.40472 | -62.69547 | 2026-08-20 05:42:00 | NPP-375D | PORTO VELHO | RONDÔNIA | Brasil | 1100205 | 11 | 33 | nan | nan | nan | Amazônia | 1.6 |
| acbf0f13-da6d-32a8-8060-312eeec11e6c | -8.64424 | -62.83004 | 2026-08-20 05:42:00 | NPP-375D | CANDEIAS DO JAMARI | RONDÔNIA | Brasil | 1100809 | 11 | 33 | nan | nan | nan | Amazônia | 0.9 |
| d0b8ea14-a2b8-3db3-adcc-ae1138d8f8e7 | -11.21314 | -55.0524 | 2026-08-20 05:42:00 | NPP-375D | CLÁUDIA | MATO GROSSO | Brasil | 5103056 | 51 | 33 | nan | nan | nan | Amazônia | 7.7 |
| e2ac518a-2eb7-390c-b42e-0170576cdc8f | -8.68108 | -54.65107 | 2026-08-20 05:42:00 | NPP-375D | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 1.4 |
| 20d104f8-e2bf-30ab-816b-0dfe5ce20cac | -9.25413 | -59.81973 | 2026-08-20 05:42:00 | NPP-375D | COLNIZA | MATO GROSSO | Brasil | 5103254 | 51 | 33 | nan | nan | nan | Amazônia | 0.7 |
| 2f23902a-0a73-36b7-95dd-8e79125e5cd9 | -8.58212 | -54.78101 | 2026-08-20 05:42:00 | NPP-375D | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 4.3 |
| 4d04a70c-2377-3720-be78-c7cd65a6b5b7 | -7.43093 | -59.78938 | 2026-08-20 05:42:00 | NPP-375D | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 2.4 |
| 5ebbf9cb-b697-34e8-bfe2-0969c8f62ae2 | -8.89956 | -60.55092 | 2026-08-20 05:42:00 | NPP-375D | COLNIZA | MATO GROSSO | Brasil | 5103254 | 51 | 33 | nan | nan | nan | Amazônia | 4.1 |
| 61bba9ef-5072-3584-bc2e-9ef9da180b89 | -6.86107 | -59.02391 | 2026-08-20 05:42:00 | NPP-375D | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 1.0 |
| 70a41cb7-bb19-3030-9aed-a6ac44d155c6 | -10.38547 | -61.20299 | 2026-08-20 05:42:00 | NPP-375D | RONDOLÂNDIA | MATO GROSSO | Brasil | 5107578 | 51 | 33 | nan | nan | nan | Amazônia | 2.4 |
| 88bb8b4f-3788-3a34-8f50-8dabb7b5ebb7 | -9.41681 | -60.4427 | 2026-08-20 05:42:00 | NPP-375D | ARIPUANÃ | MATO GROSSO | Brasil | 5101407 | 51 | 33 | nan | nan | nan | Amazônia | 2.2 |
| c8cd4bb3-1f72-3176-8e25-6896f7d3e70a | -6.86275 | -59.03725 | 2026-08-20 05:42:00 | NPP-375D | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 2.1 |
| 6acaaba2-2558-309f-93e5-3a2fe0d0a159 | -8.09845 | -51.66945 | 2026-08-20 05:42:00 | NPP-375D | OURILÂNDIA DO NORTE | PARÁ | Brasil | 1505437 | 15 | 33 | nan | nan | nan | Amazônia | 2.8 |
| e2119a8e-c7c0-3955-bd25-509fae8ada14 | -8.58513 | -54.75878 | 2026-08-20 05:42:00 | NPP-375D | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 3.7 |
| 196901e8-c9f7-3af6-aeca-3e37796300ac | -7.86246 | -63.76405 | 2026-08-20 05:42:00 | NPP-375D | CANUTAMA | AMAZONAS | Brasil | 1300904 | 13 | 33 | nan | nan | nan | Amazônia | 0.7 |
| 4d9ad780-4c40-3b14-82d2-d466c1a18bec | -7.86532 | -63.74619 | 2026-08-20 05:42:00 | NPP-375D | CANUTAMA | AMAZONAS | Brasil | 1300904 | 13 | 33 | nan | nan | nan | Amazônia | 1.1 |
| 7c24a2a2-2c8c-30ce-b426-09e564c96f5b | -8.56781 | -54.76544 | 2026-08-20 05:42:00 | NPP-375D | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 4.6 |
| a8c414c8-1fe7-3692-a203-8df64512c11e | -9.17136 | -59.70178 | 2026-08-20 05:42:00 | NPP-375D | COLNIZA | MATO GROSSO | Brasil | 5103254 | 51 | 33 | nan | nan | nan | Amazônia | 1.5 |
| e78ab40a-76d7-3ad2-a014-7f82832105f2 | -6.76765 | -59.14826 | 2026-08-20 05:42:00 | NPP-375D | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 1.0 |
| fc611e61-9fa1-3785-9fc4-47202640973a | -9.11797 | -61.59846 | 2026-08-20 05:42:00 | NPP-375D | MACHADINHO D'OESTE | RONDÔNIA | Brasil | 1100130 | 11 | 33 | nan | nan | nan | Amazônia | 1.5 |
| bd94443a-6471-3f7b-883e-f9a86a608117 | -7.05165 | -59.84484 | 2026-08-20 05:42:00 | NPP-375D | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 1.2 |
| 15d366f4-9716-3654-b7ee-9787fe91f593 | -6.88412 | -59.04312 | 2026-08-20 05:42:00 | NPP-375D | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 1.9 |
| 76294eb9-ace5-330b-af66-44150c27bb98 | -8.55994 | -54.67788 | 2026-08-20 05:42:00 | NPP-375D | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 1.4 |
| ce87d7b9-7d8b-3168-803c-b7129ec28d50 | -6.75186 | -59.15453 | 2026-08-20 05:42:00 | NPP-375D | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 1.9 |
| edb76638-39c6-3772-a830-bbc03ca097b2 | -11.42382 | -54.3168 | 2026-08-20 05:42:00 | NPP-375D | UNIÃO DO SUL | MATO GROSSO | Brasil | 5108303 | 51 | 33 | nan | nan | nan | Amazônia | 1.2 |
| c0b9748d-873b-310b-9432-861d9c065828 | -11.19254 | -54.01143 | 2026-08-20 05:42:00 | NPP-375D | MARCELÂNDIA | MATO GROSSO | Brasil | 5105580 | 51 | 33 | nan | nan | nan | Amazônia | 2.7 |
| 69019b13-13bf-338d-9d9b-7828c825bd45 | -6.5905 | -58.96474 | 2026-08-20 05:42:00 | NPP-375D | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 1.5 |
| 6ec4acd6-087d-3462-958f-16affe2f7bb1 | -8.6777 | -54.63884 | 2026-08-20 05:42:00 | NPP-375D | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 1.0 |
| c661d15a-8319-3c56-bb1c-1dab37bd1955 | -10.39062 | -61.21538 | 2026-08-20 05:42:00 | NPP-375D | RONDOLÂNDIA | MATO GROSSO | Brasil | 5107578 | 51 | 33 | nan | nan | nan | Amazônia | 1.0 |
| 84a4a3c8-28b3-38b3-a6ba-39109ed163a2 | -6.70596 | -58.94123 | 2026-08-20 05:42:00 | NPP-375D | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 1.9 |
| 0c3d2971-5831-3f25-bdb0-e30d170e1c17 | -10.38718 | -61.21484 | 2026-08-20 05:42:00 | NPP-375D | RONDOLÂNDIA | MATO GROSSO | Brasil | 5107578 | 51 | 33 | nan | nan | nan | Amazônia | 4.6 |
| ac1ad068-ffb8-32dc-abbc-5d2a3bcbeb7e | -7.53792 | -55.57479 | 2026-08-20 05:42:00 | NPP-375D | NOVO PROGRESSO | PARÁ | Brasil | 1505031 | 15 | 33 | nan | nan | nan | Amazônia | 2.9 |
| 2b60182c-536c-33fd-a743-3d7311639a8d | -6.75975 | -59.15141 | 2026-08-20 05:42:00 | NPP-375D | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 1.0 |
| f9acfcf5-3416-35c0-993a-3892662347b2 | -9.22413 | -59.76989 | 2026-08-20 05:42:00 | NPP-375D | COLNIZA | MATO GROSSO | Brasil | 5103254 | 51 | 33 | nan | nan | nan | Amazônia | 3.9 |
| 73d2846e-e0bc-31e9-976f-2f549ce2a492 | -8.68136 | -54.64575 | 2026-08-20 05:42:00 | NPP-375D | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 1.1 |
| f6c1c2e8-4c9d-3875-b392-02afeca125df | -6.69797 | -58.94454 | 2026-08-20 05:42:00 | NPP-375D | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 5.1 |
| 1cc35a02-ee49-3412-bb0d-b432408866d1 | -6.7041 | -59.10168 | 2026-08-20 05:42:00 | NPP-375D | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 2.7 |
| 5ff8f2b3-8ac8-33e7-9346-f08e10d1360b | -8.58168 | -54.74696 | 2026-08-20 05:42:00 | NPP-375D | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 2.6 |
| 30d5142c-15ac-399b-a357-80aab9c66ba9 | -8.56734 | -54.66134 | 2026-08-20 05:42:00 | NPP-375D | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 4.9 |
| 6114197c-499b-340f-a2a1-7ca71bd9b650 | -8.57614 | -54.77781 | 2026-08-20 05:42:00 | NPP-375D | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 7.1 |
| 93fc73a4-68ba-3757-adba-b674252ae313 | -11.19209 | -54.01491 | 2026-08-20 05:42:00 | NPP-375D | MARCELÂNDIA | MATO GROSSO | Brasil | 5105580 | 51 | 33 | nan | nan | nan | Amazônia | 2.7 |
| 7519d37e-4ba0-3c27-812e-bf7844ed1c78 | -8.5707 | -54.67353 | 2026-08-20 05:42:00 | NPP-375D | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 2.0 |
| 4b2ae8af-c699-3a3a-a43a-4bdfd2631986 | -9.08147 | -65.3837 | 2026-08-20 05:42:00 | NPP-375D | LÁBREA | AMAZONAS | Brasil | 1302405 | 13 | 33 | nan | nan | nan | Amazônia | 1.0 |
| 3bfd20cd-8cdf-3080-89af-b295659bb34d | -6.80924 | -59.44532 | 2026-08-20 05:42:00 | NPP-375D | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 0.8 |
| 4ef2d9ab-4f5d-3faa-bb1f-99e26d8698a6 | -7.04812 | -59.84432 | 2026-08-20 05:42:00 | NPP-375D | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 1.2 |
| c4e65efe-15e0-3020-9d40-d9a30271a0a3 | -6.58795 | -58.98171 | 2026-08-20 05:42:00 | NPP-375D | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 1.3 |
| 16abd342-a9b6-31ad-9d76-d1458a69cb42 | -6.70164 | -58.94504 | 2026-08-20 05:42:00 | NPP-375D | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 1.9 |
| c4673021-35ba-34b0-b42f-5d35a804a3ba | -8.95109 | -60.56984 | 2026-08-20 05:42:00 | NPP-375D | COLNIZA | MATO GROSSO | Brasil | 5103254 | 51 | 33 | nan | nan | nan | Amazônia | 1.3 |
| a47f27b9-5628-32db-9efc-7cea7b672441 | -11.8321 | -58.84589 | 2026-08-20 05:42:00 | NPP-375D | JUÍNA | MATO GROSSO | Brasil | 5105150 | 51 | 33 | nan | nan | nan | Cerrado | 2.4 |


[Clique aqui para ver as próximas entradas](README63.md)
