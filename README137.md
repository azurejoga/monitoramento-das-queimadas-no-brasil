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

## Dados Diários - Página 137

| ID | Latitude | Longitude | Data/Hora GMT | Satélite | Município | Estado | País | Município ID | Estado ID | País ID | Dias sem Chuva | Precipitação | Risco de Fogo | Bioma | FRP |
|----|----------|-----------|---------------|----------|-----------|--------|------|--------------|-----------|---------|----------------|--------------|----------------|-------|-----|
| 44173880-f3e0-331a-b901-047a9a8b557b | -4.1092 | -59.91939 | 2026-10-08 05:23:00 | NPP-375D | AUTAZES | AMAZONAS | Brasil | 1300300 | 13 | 33 | nan | nan | nan | Amazônia | 1.8 |
| 3530f78e-f3f1-3fd4-936d-9513756d6fa8 | -2.99971 | -54.12136 | 2026-10-08 05:23:00 | NPP-375D | SANTARÉM | PARÁ | Brasil | 1506807 | 15 | 33 | nan | nan | nan | Amazônia | 2.2 |
| c12cf91f-d3ff-30c0-8441-a0f3c6373975 | -1.49764 | -55.66226 | 2026-10-08 05:23:00 | NPP-375D | ÓBIDOS | PARÁ | Brasil | 1505106 | 15 | 33 | nan | nan | nan | Amazônia | 1.5 |
| 65240421-8010-36d8-beb4-60ccde87053f | -2.49811 | -58.06622 | 2026-10-08 05:23:00 | NPP-375D | SÃO SEBASTIÃO DO UATUMÃ | AMAZONAS | Brasil | 1303957 | 13 | 33 | nan | nan | nan | Amazônia | 1.8 |
| c474ff26-3aec-385f-b6d6-e388f335fb86 | -3.08381 | -54.27487 | 2026-10-08 05:23:00 | NPP-375D | MOJUÍ DOS CAMPOS | PARÁ | Brasil | 1504752 | 15 | 33 | nan | nan | nan | Amazônia | 1.7 |
| 9d4d5985-03ef-376f-a215-d89d89c33b37 | -3.14446 | -53.72856 | 2026-10-08 05:23:00 | NPP-375D | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | 1.8 |
| 873c4de7-a87b-32fe-b445-ff87be8a939c | -2.77271 | -54.0755 | 2026-10-08 05:23:00 | NPP-375D | PRAINHA | PARÁ | Brasil | 1506005 | 15 | 33 | nan | nan | nan | Amazônia | 2.2 |
| 6a636e2b-debb-3246-a0f0-37a4c6f9a5d7 | -2.58462 | -56.1659 | 2026-10-08 05:23:00 | NPP-375D | JURUTI | PARÁ | Brasil | 1503903 | 15 | 33 | nan | nan | nan | Amazônia | 1.5 |
| 603700a0-2b41-3b83-8e47-6f17114f7c7b | -3.01452 | -54.07215 | 2026-10-08 05:23:00 | NPP-375D | SANTARÉM | PARÁ | Brasil | 1506807 | 15 | 33 | nan | nan | nan | Amazônia | 2.8 |
| 085dbaee-7284-3737-9f38-00af6b8fc25c | -3.2731 | -54.05443 | 2026-10-08 05:23:00 | NPP-375D | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | 3.5 |
| b14021a7-dcf4-3477-aba1-9a622e232b2c | -3.05347 | -51.22136 | 2026-10-08 05:23:00 | NPP-375D | ANAPU | PARÁ | Brasil | 1500859 | 15 | 33 | nan | nan | nan | Amazônia | 1.0 |
| a201a464-b955-307a-a624-97dff1650008 | -3.08269 | -54.25906 | 2026-10-08 05:23:00 | NPP-375D | MOJUÍ DOS CAMPOS | PARÁ | Brasil | 1504752 | 15 | 33 | nan | nan | nan | Amazônia | 1.4 |
| 101bc38a-35a5-3119-84fb-54cbf77d84de | -6.09231 | -55.72321 | 2026-10-08 05:23:00 | NPP-375D | ITAITUBA | PARÁ | Brasil | 1503606 | 15 | 33 | nan | nan | nan | Amazônia | 2.3 |
| f7bd5cdd-f918-357c-a32f-ad9d6e3ef0fc | -3.591 | -54.55974 | 2026-10-08 05:23:00 | NPP-375D | PLACAS | PARÁ | Brasil | 1505650 | 15 | 33 | nan | nan | nan | Amazônia | 1.2 |
| be6babe4-7fff-3c3c-93a6-cdd7c87c5d32 | -9.04997 | -65.93053 | 2026-10-08 05:23:00 | NPP-375D | LÁBREA | AMAZONAS | Brasil | 1302405 | 13 | 33 | nan | nan | nan | Amazônia | 1.9 |
| 1d41fb60-4835-373e-bb43-daa857bfc106 | -1.76892 | -55.03271 | 2026-10-08 05:23:00 | NPP-375D | ALENQUER | PARÁ | Brasil | 1500404 | 15 | 33 | nan | nan | nan | Amazônia | 1.8 |
| 4c14c65b-9046-3c79-8114-ad918efa275b | -1.52671 | -54.5508 | 2026-10-08 05:23:00 | NPP-375D | ALENQUER | PARÁ | Brasil | 1500404 | 15 | 33 | nan | nan | nan | Amazônia | 2.5 |
| f8299bf9-8f06-3f64-8ec5-8953368c7642 | -3.22685 | -54.30397 | 2026-10-08 05:23:00 | NPP-375D | MOJUÍ DOS CAMPOS | PARÁ | Brasil | 1504752 | 15 | 33 | nan | nan | nan | Amazônia | 1.4 |
| 1cc2b981-2da2-340b-9b16-0e95ab5952a0 | -4.92499 | -55.87021 | 2026-10-08 05:23:00 | NPP-375D | TRAIRÃO | PARÁ | Brasil | 1508050 | 15 | 33 | nan | nan | nan | Amazônia | 0.9 |
| f24d7184-be03-3199-960b-fc62f699c86e | -4.07017 | -54.05028 | 2026-10-08 05:23:00 | NPP-375D | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | 1.3 |
| de44e024-51dd-3ba8-a8e5-566f4db22817 | -3.04934 | -51.22071 | 2026-10-08 05:23:00 | NPP-375D | ANAPU | PARÁ | Brasil | 1500859 | 15 | 33 | nan | nan | nan | Amazônia | 5.3 |
| 4844ef39-7e24-3a6a-b032-c24f23e98509 | -3.84988 | -55.9769 | 2026-10-08 05:23:00 | NPP-375D | AVEIRO | PARÁ | Brasil | 1501006 | 15 | 33 | nan | nan | nan | Amazônia | 3.0 |
| 2d6d44a9-6d50-31a5-b154-efea21bd94fb | -2.97693 | -54.12957 | 2026-10-08 05:23:00 | NPP-375D | SANTARÉM | PARÁ | Brasil | 1506807 | 15 | 33 | nan | nan | nan | Amazônia | 1.8 |
| bf6ef74d-bc71-33a3-b2aa-7b87d935b4eb | -12.06246 | -58.0434 | 2026-10-08 05:23:00 | NPP-375D | BRASNORTE | MATO GROSSO | Brasil | 5101902 | 51 | 33 | nan | nan | nan | Amazônia | 1.3 |
| 16310e16-ce85-3c42-ab8a-8ec14cb21ec9 | -2.83945 | -57.48032 | 2026-10-08 05:23:00 | NPP-375D | BOA VISTA DO RAMOS | AMAZONAS | Brasil | 1300680 | 13 | 33 | nan | nan | nan | Amazônia | 1.3 |
| 08e4d478-85ef-35dc-803d-38fa7679c7ef | -7.21725 | -55.10368 | 2026-10-08 05:23:00 | NPP-375D | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 2.2 |
| 7e664fc4-c50a-3f30-8015-990330835896 | -2.76752 | -54.10313 | 2026-10-08 05:23:00 | NPP-375D | PRAINHA | PARÁ | Brasil | 1506005 | 15 | 33 | nan | nan | nan | Amazônia | 2.7 |
| 94b0f2b9-9893-3678-9027-e27443b54fa0 | -5.11282 | -47.12185 | 2026-10-08 05:23:00 | NPP-375D | JOÃO LISBOA | MARANHÃO | Brasil | 2105500 | 21 | 33 | nan | nan | nan | Amazônia | 2.6 |
| ad3f88b5-a100-34e7-8595-8621f85176d2 | -3.30103 | -54.01459 | 2026-10-08 05:23:00 | NPP-375D | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | 3.1 |
| c0cc70d5-d0a4-3d89-8df4-703c9f9058fc | -2.87849 | -54.18143 | 2026-10-08 05:23:00 | NPP-375D | SANTARÉM | PARÁ | Brasil | 1506807 | 15 | 33 | nan | nan | nan | Amazônia | 1.9 |
| 57d2424f-db19-37ee-940e-6b5ea149b29c | -2.98777 | -56.59055 | 2026-10-08 05:23:00 | NPP-375D | JURUTI | PARÁ | Brasil | 1503903 | 15 | 33 | nan | nan | nan | Amazônia | 0.8 |
| b0e61186-722c-34cf-92be-290c8230a2cd | -2.22222 | -53.69955 | 2026-10-08 05:23:00 | NPP-375D | PRAINHA | PARÁ | Brasil | 1506005 | 15 | 33 | nan | nan | nan | Amazônia | 20.7 |
| 7bf19678-875e-3e93-893f-549dec302228 | -3.97904 | -56.11834 | 2026-10-08 05:23:00 | NPP-375D | ITAITUBA | PARÁ | Brasil | 1503606 | 15 | 33 | nan | nan | nan | Amazônia | 4.0 |
| c30b4ecc-725e-32ab-9997-c88cc0f0bbc7 | -5.72816 | -45.15254 | 2026-10-08 05:23:00 | NPP-375D | BARRA DO CORDA | MARANHÃO | Brasil | 2101608 | 21 | 33 | nan | nan | nan | Cerrado | 6.9 |
| f28bff56-d992-36b4-8305-4ef552553f16 | -3.01874 | -54.04496 | 2026-10-08 05:23:00 | NPP-375D | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | 3.3 |
| c083f7ef-5b26-309b-866f-afeffa7cefc3 | -9.16641 | -61.4044 | 2026-10-08 05:23:00 | NPP-375D | COLNIZA | MATO GROSSO | Brasil | 5103254 | 51 | 33 | nan | nan | nan | Amazônia | 2.5 |
| e07819fc-78bd-391c-a2a0-488114cbd48b | -9.05491 | -65.93139 | 2026-10-08 05:23:00 | NPP-375D | LÁBREA | AMAZONAS | Brasil | 1302405 | 13 | 33 | nan | nan | nan | Amazônia | 3.7 |
| 0f28d850-1af4-31af-a95a-b9e9d346c167 | -3.01032 | -54.23712 | 2026-10-08 05:23:00 | NPP-375D | SANTARÉM | PARÁ | Brasil | 1506807 | 15 | 33 | nan | nan | nan | Amazônia | 1.7 |
| b64792b1-002a-383e-a1bf-55236c165836 | -2.93025 | -54.07909 | 2026-10-08 05:23:00 | NPP-375D | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | 1.6 |
| 991b2849-7096-3162-abfd-724e33806b98 | -2.03965 | -54.4866 | 2026-10-08 05:23:00 | NPP-375D | MONTE ALEGRE | PARÁ | Brasil | 1504802 | 15 | 33 | nan | nan | nan | Amazônia | 2.3 |
| c72e422c-ff12-3a38-bf9d-aa05990f7f08 | -3.61689 | -55.50418 | 2026-10-08 05:23:00 | NPP-375D | AVEIRO | PARÁ | Brasil | 1501006 | 15 | 33 | nan | nan | nan | Amazônia | 2.1 |
| 1bf58674-83ad-30a3-b887-10d8f336f212 | -6.39439 | -59.98496 | 2026-10-08 05:23:00 | NPP-375D | NOVO ARIPUANÃ | AMAZONAS | Brasil | 1303304 | 13 | 33 | nan | nan | nan | Amazônia | 1.2 |
| 845dd0f2-2579-3dc1-977a-a157a5617b24 | -3.17123 | -58.63758 | 2026-10-08 05:23:00 | NPP-375D | ITACOATIARA | AMAZONAS | Brasil | 1301902 | 13 | 33 | nan | nan | nan | Amazônia | 1.4 |
| ed389bef-3e76-39d5-955a-9899d2bfbb06 | -2.94029 | -54.0608 | 2026-10-08 05:23:00 | NPP-375D | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | 2.4 |
| 4eb92cc1-e31b-3b10-8e5e-990785f72f7a | -3.92761 | -56.06039 | 2026-10-08 05:23:00 | NPP-375D | ITAITUBA | PARÁ | Brasil | 1503606 | 15 | 33 | nan | nan | nan | Amazônia | 2.4 |
| 1f8f764d-9742-3d39-bb4a-8081d572a25c | -3.15503 | -58.0419 | 2026-10-08 05:23:00 | NPP-375D | URUCURITUBA | AMAZONAS | Brasil | 1304401 | 13 | 33 | nan | nan | nan | Amazônia | 0.7 |
| dfac5b9c-fced-3527-af7c-5c34dd56da24 | -5.73556 | -45.14583 | 2026-10-08 05:23:00 | NPP-375D | BARRA DO CORDA | MARANHÃO | Brasil | 2101608 | 21 | 33 | nan | nan | nan | Cerrado | 2.7 |
| 4eadc04f-5aad-31ba-8e1b-36f774853096 | -1.50793 | -54.8248 | 2026-10-08 05:23:00 | NPP-375D | ALENQUER | PARÁ | Brasil | 1500404 | 15 | 33 | nan | nan | nan | Amazônia | 1.1 |
| 3f5ed580-bde9-35da-acc2-037d4c95a974 | -3.84577 | -55.80751 | 2026-10-08 05:23:00 | NPP-375D | AVEIRO | PARÁ | Brasil | 1501006 | 15 | 33 | nan | nan | nan | Amazônia | 1.9 |
| 3b56102d-f88e-32c1-933a-a7274f47bd86 | -2.98472 | -51.2405 | 2026-10-08 05:23:00 | NPP-375D | ANAPU | PARÁ | Brasil | 1500859 | 15 | 33 | nan | nan | nan | Amazônia | 0.8 |
| ef20283b-b76a-3a34-a3b9-cb9ddf1d4d51 | -3.17315 | -58.98288 | 2026-10-08 05:23:00 | NPP-375D | ITACOATIARA | AMAZONAS | Brasil | 1301902 | 13 | 33 | nan | nan | nan | Amazônia | 0.7 |
| 36aea5b2-552a-394e-b319-7d7002dc9588 | -5.92191 | -55.69683 | 2026-10-08 05:23:00 | NPP-375D | ITAITUBA | PARÁ | Brasil | 1503606 | 15 | 33 | nan | nan | nan | Amazônia | 1.0 |
| 8df5dc45-37c7-3a04-a5e7-8ead91faf050 | -4.52281 | -54.983 | 2026-10-08 05:23:00 | NPP-375D | RURÓPOLIS | PARÁ | Brasil | 1506195 | 15 | 33 | nan | nan | nan | Amazônia | 3.9 |
| e83ddada-77d0-3f52-8bd9-396de7ad6c97 | -3.17497 | -57.09248 | 2026-10-08 05:23:00 | NPP-375D | BARREIRINHA | AMAZONAS | Brasil | 1300508 | 13 | 33 | nan | nan | nan | Amazônia | 1.1 |
| 2db99dba-41b4-3c0b-85e7-22f5fffd1f5d | -3.25797 | -54.65882 | 2026-10-08 05:23:00 | NPP-375D | MOJUÍ DOS CAMPOS | PARÁ | Brasil | 1504752 | 15 | 33 | nan | nan | nan | Amazônia | 1.5 |
| a3b967a0-4706-3451-a55e-d58b2dfd3bb1 | -3.55569 | -59.4699 | 2026-10-08 05:23:00 | NPP-375D | AUTAZES | AMAZONAS | Brasil | 1300300 | 13 | 33 | nan | nan | nan | Amazônia | 4.8 |
| 4e29fd56-ca72-3162-8548-3538f6d2b14b | -2.93942 | -54.11217 | 2026-10-08 05:23:00 | NPP-375D | SANTARÉM | PARÁ | Brasil | 1506807 | 15 | 33 | nan | nan | nan | Amazônia | 2.8 |
| 8717a4eb-5a6d-334b-80d3-26efd685661f | -3.09069 | -54.2994 | 2026-10-08 05:23:00 | NPP-375D | MOJUÍ DOS CAMPOS | PARÁ | Brasil | 1504752 | 15 | 33 | nan | nan | nan | Amazônia | 2.6 |
| b0b26a2b-32d2-35bc-abc0-404b9e4ed9ac | -7.14049 | -46.52545 | 2026-10-08 05:23:00 | NPP-375D | RIACHÃO | MARANHÃO | Brasil | 2109502 | 21 | 33 | nan | nan | nan | Cerrado | 1.8 |
| ffdc65d4-579f-302e-a499-490877cb71c3 | -6.63298 | -43.7382 | 2026-10-08 05:23:00 | NPP-375D | SÃO JOÃO DOS PATOS | MARANHÃO | Brasil | 2111102 | 21 | 33 | nan | nan | nan | Cerrado | 15.1 |
| eebb500c-f393-3c30-8f57-f6f0f88fafbf | -2.47126 | -56.07035 | 2026-10-08 05:23:00 | NPP-375D | JURUTI | PARÁ | Brasil | 1503903 | 15 | 33 | nan | nan | nan | Amazônia | 1.4 |
| 67fd4925-913d-350a-9ef7-5c3d82882a49 | -1.29656 | -55.69421 | 2026-10-08 05:23:00 | NPP-375D | ÓBIDOS | PARÁ | Brasil | 1505106 | 15 | 33 | nan | nan | nan | Amazônia | 1.1 |
| f5f51b31-61d1-3b5b-b33f-86a1087766ec | -3.54723 | -59.47681 | 2026-10-08 05:23:00 | NPP-375D | AUTAZES | AMAZONAS | Brasil | 1300300 | 13 | 33 | nan | nan | nan | Amazônia | 2.3 |
| 5178a454-2f4f-30d2-ae29-21e086fb90f8 | -3.82594 | -55.46394 | 2026-10-08 05:23:00 | NPP-375D | AVEIRO | PARÁ | Brasil | 1501006 | 15 | 33 | nan | nan | nan | Amazônia | 4.4 |
| 6442ddb5-7e85-35b0-a53b-29bafbeae91f | -3.58358 | -59.52414 | 2026-10-08 05:23:00 | NPP-375D | AUTAZES | AMAZONAS | Brasil | 1300300 | 13 | 33 | nan | nan | nan | Amazônia | 1.1 |
| 062aa8db-33a7-3cf0-9c15-23fcb33edfce | -3.01392 | -54.07603 | 2026-10-08 05:23:00 | NPP-375D | SANTARÉM | PARÁ | Brasil | 1506807 | 15 | 33 | nan | nan | nan | Amazônia | 4.1 |
| b69d1f1d-fe3f-3b06-ba82-e6d40ecbdf6d | -5.11566 | -47.12013 | 2026-10-08 05:23:00 | NPP-375D | JOÃO LISBOA | MARANHÃO | Brasil | 2105500 | 21 | 33 | nan | nan | nan | Amazônia | 1.7 |
| 06be7733-9495-3cc0-a289-f45d0b3abfe9 | -3.02362 | -54.12902 | 2026-10-08 05:23:00 | NPP-375D | SANTARÉM | PARÁ | Brasil | 1506807 | 15 | 33 | nan | nan | nan | Amazônia | 1.5 |
| 5bcc2d19-c16c-3f60-97d0-26a57bc1a4cf | -3.01182 | -50.47073 | 2026-10-08 05:23:00 | NPP-375D | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 1.4 |
| 9e649cb6-31a2-3604-8d65-7db0de37251e | -2.91261 | -54.10009 | 2026-10-08 05:23:00 | NPP-375D | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | 2.7 |
| c4a50145-bf89-3875-a02d-a093605a5d66 | -10.62138 | -60.48687 | 2026-10-08 05:23:00 | NPP-375D | ARIPUANÃ | MATO GROSSO | Brasil | 5101407 | 51 | 33 | nan | nan | nan | Amazônia | 4.6 |
| 207780d5-aefc-3f17-ab51-d1ed8ab0a1eb | -2.50195 | -56.1779 | 2026-10-08 05:23:00 | NPP-375D | JURUTI | PARÁ | Brasil | 1503903 | 15 | 33 | nan | nan | nan | Amazônia | 2.7 |
| 781f3839-327f-3d5b-a7bd-0fe970154010 | -3.01772 | -54.14385 | 2026-10-08 05:23:00 | NPP-375D | SANTARÉM | PARÁ | Brasil | 1506807 | 15 | 33 | nan | nan | nan | Amazônia | 1.9 |
| 18ca63b9-99b9-39ef-8eae-f0af7fb8658e | -2.99988 | -54.07384 | 2026-10-08 05:23:00 | NPP-375D | SANTARÉM | PARÁ | Brasil | 1506807 | 15 | 33 | nan | nan | nan | Amazônia | 31.1 |
| f260508b-3b26-3b00-9303-8bf89a5c9c51 | -3.28305 | -54.05998 | 2026-10-08 05:23:00 | NPP-375D | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | 1.3 |
| 84d3a343-f9db-305d-ab5a-fa61c3d27f1a | -3.28575 | -53.83401 | 2026-10-08 05:23:00 | NPP-375D | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | 1.0 |
| e30fdfc7-adb2-382a-aae9-1ddac6a565b3 | -3.61185 | -55.47064 | 2026-10-08 05:23:00 | NPP-375D | AVEIRO | PARÁ | Brasil | 1501006 | 15 | 33 | nan | nan | nan | Amazônia | 1.8 |
| dcb4180b-2ac1-3987-83bf-16d0d20a6746 | -3.35248 | -59.50143 | 2026-10-08 05:23:00 | NPP-375D | CAREIRO DA VÁRZEA | AMAZONAS | Brasil | 1301159 | 13 | 33 | nan | nan | nan | Amazônia | 1.0 |
| ee41ac6d-9909-3fde-82ff-2ec68ea9f8e2 | -4.15574 | -54.91933 | 2026-10-08 05:23:00 | NPP-375D | RURÓPOLIS | PARÁ | Brasil | 1506195 | 15 | 33 | nan | nan | nan | Amazônia | 2.0 |
| 7081bb06-191a-3a24-87d7-a2878beaf32d | -5.68063 | -53.48608 | 2026-10-08 05:23:00 | NPP-375D | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 0.9 |
| d167b9b1-dc36-331e-9eb3-e617988d400a | -3.54065 | -54.64082 | 2026-10-08 05:23:00 | NPP-375D | PLACAS | PARÁ | Brasil | 1505650 | 15 | 33 | nan | nan | nan | Amazônia | 1.3 |
| 5ac22ef2-3e27-3859-8712-4f7f7dc1ae1d | -3.09536 | -54.29232 | 2026-10-08 05:23:00 | NPP-375D | MOJUÍ DOS CAMPOS | PARÁ | Brasil | 1504752 | 15 | 33 | nan | nan | nan | Amazônia | 1.8 |
| e3b10988-fcbd-3185-94e3-726c19617059 | -2.7595 | -57.67833 | 2026-10-08 05:23:00 | NPP-375D | URUCURITUBA | AMAZONAS | Brasil | 1304401 | 13 | 33 | nan | nan | nan | Amazônia | 1.4 |
| 51eee267-6999-3271-98de-062b2845a05c | -5.74192 | -53.45904 | 2026-10-08 05:23:00 | NPP-375D | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 1.6 |
| 856fd6c9-20c3-3f8e-a070-f517aba2b1f4 | -2.76328 | -54.11343 | 2026-10-08 05:23:00 | NPP-375D | SANTARÉM | PARÁ | Brasil | 1506807 | 15 | 33 | nan | nan | nan | Amazônia | 2.9 |
| 2339fb3c-8349-383a-9235-c36c62142a59 | -2.93108 | -54.14243 | 2026-10-08 05:23:00 | NPP-375D | SANTARÉM | PARÁ | Brasil | 1506807 | 15 | 33 | nan | nan | nan | Amazônia | 1.2 |
| 1262e055-58c5-340f-8f64-0ba2bcb2b6ee | -3.72556 | -54.6607 | 2026-10-08 05:23:00 | NPP-375D | PLACAS | PARÁ | Brasil | 1505650 | 15 | 33 | nan | nan | nan | Amazônia | 2.2 |
| cde0b3a5-7367-3b59-ae39-addd287dfedc | -2.99645 | -54.04947 | 2026-10-08 05:23:00 | NPP-375D | SANTARÉM | PARÁ | Brasil | 1506807 | 15 | 33 | nan | nan | nan | Amazônia | 2.4 |
| 5d300123-5c04-3e17-b26a-15712a224fce | -3.05229 | -54.22014 | 2026-10-08 05:23:00 | NPP-375D | SANTARÉM | PARÁ | Brasil | 1506807 | 15 | 33 | nan | nan | nan | Amazônia | 1.2 |
| 6b4e2dec-5271-3cf4-957a-18542a017b6e | -2.93949 | -57.94918 | 2026-10-08 05:23:00 | NPP-375D | URUCURITUBA | AMAZONAS | Brasil | 1304401 | 13 | 33 | nan | nan | nan | Amazônia | 1.1 |
| 66c9134b-59d6-3fa1-8dfc-d73dc81a30fe | -3.50024 | -51.68429 | 2026-10-08 05:23:00 | NPP-375D | ANAPU | PARÁ | Brasil | 1500859 | 15 | 33 | nan | nan | nan | Amazônia | 1.7 |
| f7a901ea-01ea-3160-a00e-32a755a51b48 | -4.29237 | -60.95919 | 2026-10-08 05:23:00 | NPP-375D | BERURI | AMAZONAS | Brasil | 1300631 | 13 | 33 | nan | nan | nan | Amazônia | 0.8 |
| 01c6ad05-60ef-3b67-9abd-0493a42aa9a7 | -3.05166 | -53.92591 | 2026-10-08 05:23:00 | NPP-375D | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | 1.7 |
| 6c243123-64ba-3bb4-a6e7-0a797effb729 | -1.50905 | -54.81767 | 2026-10-08 05:23:00 | NPP-375D | ALENQUER | PARÁ | Brasil | 1500404 | 15 | 33 | nan | nan | nan | Amazônia | 1.0 |
| 4c1e6368-81d9-3a59-892a-bf133058bab3 | -3.05987 | -54.21738 | 2026-10-08 05:23:00 | NPP-375D | SANTARÉM | PARÁ | Brasil | 1506807 | 15 | 33 | nan | nan | nan | Amazônia | 1.2 |
| 193e5cd5-2e7d-3fa2-8da1-95bf934ce238 | -4.37512 | -54.74706 | 2026-10-08 05:23:00 | NPP-375D | PLACAS | PARÁ | Brasil | 1505650 | 15 | 33 | nan | nan | nan | Amazônia | 2.0 |
| 2709d951-595d-38dd-8205-bcec1d9410c0 | -3.53839 | -59.47611 | 2026-10-08 05:23:00 | NPP-375D | AUTAZES | AMAZONAS | Brasil | 1300300 | 13 | 33 | nan | nan | nan | Amazônia | 1.3 |
| f684191f-1b5d-3273-957a-67b3dcdc3d11 | -3.60021 | -54.56889 | 2026-10-08 05:23:00 | NPP-375D | PLACAS | PARÁ | Brasil | 1505650 | 15 | 33 | nan | nan | nan | Amazônia | 2.6 |
| 2ad39bc0-22be-3096-ac22-4f04180d9b17 | -3.27387 | -54.02651 | 2026-10-08 05:23:00 | NPP-375D | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | 1.1 |
| 9212c9f0-3a07-3aab-b72b-1a6ef46f25a2 | -4.77025 | -55.67557 | 2026-10-08 05:23:00 | NPP-375D | TRAIRÃO | PARÁ | Brasil | 1508050 | 15 | 33 | nan | nan | nan | Amazônia | 1.6 |


[Clique aqui para ver as próximas entradas](README138.md)
