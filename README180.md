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

## Dados Diários - Página 180

| ID | Latitude | Longitude | Data/Hora GMT | Satélite | Município | Estado | País | Município ID | Estado ID | País ID | Dias sem Chuva | Precipitação | Risco de Fogo | Bioma | FRP |
|----|----------|-----------|---------------|----------|-----------|--------|------|--------------|-----------|---------|----------------|--------------|----------------|-------|-----|
| 353eb4cb-b9bf-3489-bc5b-f9b422661e86 | -16.4632 | -57.42802 | 2024-10-02 05:36:00 | NOAA-20 | CÁCERES | MATO GROSSO | Brasil | 5102504 | 51 | 33 | nan | nan | nan | Pantanal | 3.4 |
| c8a243f9-6c02-3a5a-bd22-baf2d7fd0af1 | -16.46275 | -57.42567 | 2024-10-02 05:36:00 | NOAA-20 | CÁCERES | MATO GROSSO | Brasil | 5102504 | 51 | 33 | nan | nan | nan | Pantanal | 2.5 |
| 519d4f1e-7c77-3e46-a05b-36cd994ea036 | -16.46241 | -57.42871 | 2024-10-02 05:36:00 | NOAA-20 | CÁCERES | MATO GROSSO | Brasil | 5102504 | 51 | 33 | nan | nan | nan | Pantanal | 3.8 |
| 03bca2e6-f62a-34f6-be00-14711ad6654d | -16.46207 | -57.43175 | 2024-10-02 05:36:00 | NOAA-20 | CÁCERES | MATO GROSSO | Brasil | 5102504 | 51 | 33 | nan | nan | nan | Pantanal | 3.8 |
| 51485701-2cfb-3728-af24-569245d2fa78 | -16.46174 | -57.3542 | 2024-10-02 05:36:00 | NOAA-20 | CÁCERES | MATO GROSSO | Brasil | 5102504 | 51 | 33 | nan | nan | nan | Pantanal | 3.5 |
| f127e2a9-665a-36df-9e32-bccf083022dd | -16.46138 | -57.35724 | 2024-10-02 05:36:00 | NOAA-20 | CÁCERES | MATO GROSSO | Brasil | 5102504 | 51 | 33 | nan | nan | nan | Pantanal | 3.5 |
| a9a36216-e843-385e-b605-b6585a03804d | -16.46102 | -57.36028 | 2024-10-02 05:36:00 | NOAA-20 | CÁCERES | MATO GROSSO | Brasil | 5102504 | 51 | 33 | nan | nan | nan | Pantanal | 3.5 |
| c9a253e5-4d68-3d28-bd8d-25fa1b817b61 | -16.46066 | -57.36332 | 2024-10-02 05:36:00 | NOAA-20 | CÁCERES | MATO GROSSO | Brasil | 5102504 | 51 | 33 | nan | nan | nan | Pantanal | 3.5 |
| d5a67e67-472f-353b-8bb6-35fb760d80b9 | -16.45994 | -57.3694 | 2024-10-02 05:36:00 | NOAA-20 | CÁCERES | MATO GROSSO | Brasil | 5102504 | 51 | 33 | nan | nan | nan | Pantanal | 2.1 |
| e493353e-b76e-3900-af6b-23e93c183756 | -16.45886 | -57.3785 | 2024-10-02 05:36:00 | NOAA-20 | CÁCERES | MATO GROSSO | Brasil | 5102504 | 51 | 33 | nan | nan | nan | Pantanal | 3.3 |
| 2a3f59bf-f047-34d8-ae5a-66efd562cc04 | -16.45816 | -57.4274 | 2024-10-02 05:36:00 | NOAA-20 | CÁCERES | MATO GROSSO | Brasil | 5102504 | 51 | 33 | nan | nan | nan | Pantanal | 3.4 |
| 8c59c283-af9e-3d49-af59-5059d9948489 | -16.45744 | -57.43345 | 2024-10-02 05:36:00 | NOAA-20 | CÁCERES | MATO GROSSO | Brasil | 5102504 | 51 | 33 | nan | nan | nan | Pantanal | 7.0 |
| a0fafb7b-7bbc-341e-b694-df79ed20f9a3 | -10.541 | -69.32684 | 2024-10-02 05:36:00 | NOAA-20 | BRASILÉIA | ACRE | Brasil | 1200104 | 12 | 33 | nan | nan | nan | Amazônia | 2.0 |
| 02daa66d-1bda-3ddf-853d-cbbee401c3fe | -10.55849 | -69.31954 | 2024-10-02 05:36:00 | NOAA-20 | BRASILÉIA | ACRE | Brasil | 1200104 | 12 | 33 | nan | nan | nan | Amazônia | 2.0 |
| c66fccd8-eedb-3739-8607-efe8be71ad20 | -10.56636 | -69.32093 | 2024-10-02 05:36:00 | NOAA-20 | BRASILÉIA | ACRE | Brasil | 1200104 | 12 | 33 | nan | nan | nan | Amazônia | 1.2 |
| 28066541-6f42-3eb4-a109-ce35e7e9f0a0 | -10.6029 | -69.24876 | 2024-10-02 05:36:00 | NOAA-20 | BRASILÉIA | ACRE | Brasil | 1200104 | 12 | 33 | nan | nan | nan | Amazônia | 1.2 |
| 23c4d7e0-0669-3487-9d6a-bb1c55a145ea | -10.6227 | -69.41201 | 2024-10-02 05:36:00 | NOAA-20 | BRASILÉIA | ACRE | Brasil | 1200104 | 12 | 33 | nan | nan | nan | Amazônia | 0.8 |
| bd4b0b37-d67b-3351-ba4b-223231db8f5b | -10.62571 | -69.25496 | 2024-10-02 05:36:00 | NOAA-20 | BRASILÉIA | ACRE | Brasil | 1200104 | 12 | 33 | nan | nan | nan | Amazônia | 1.7 |
| bec0d6c5-b947-3a7c-a631-b27461731905 | -10.63302 | -69.32915 | 2024-10-02 05:36:00 | NOAA-20 | BRASILÉIA | ACRE | Brasil | 1200104 | 12 | 33 | nan | nan | nan | Amazônia | 2.4 |
| ac752984-21c2-3e23-a3d1-6729e53a47c4 | -10.64784 | -69.64804 | 2024-10-02 05:36:00 | NOAA-20 | ASSIS BRASIL | ACRE | Brasil | 1200054 | 12 | 33 | nan | nan | nan | Amazônia | 1.5 |
| fc23e713-a281-3547-b3f9-20f0fced51b4 | -10.65185 | -69.64874 | 2024-10-02 05:36:00 | NOAA-20 | ASSIS BRASIL | ACRE | Brasil | 1200054 | 12 | 33 | nan | nan | nan | Amazônia | 1.0 |
| ab7d963e-9df9-34ba-a8a9-e9fb4a58aab2 | -10.65301 | -69.64929 | 2024-10-02 05:36:00 | NOAA-20 | ASSIS BRASIL | ACRE | Brasil | 1200054 | 12 | 33 | nan | nan | nan | Amazônia | 1.0 |
| 7705c64e-59af-3fdd-8f74-d4acd3308807 | -10.67054 | -69.29942 | 2024-10-02 05:36:00 | NOAA-20 | BRASILÉIA | ACRE | Brasil | 1200104 | 12 | 33 | nan | nan | nan | Amazônia | 1.3 |
| 41683990-cd65-381a-a16c-73d2d193f3b5 | -10.67104 | -69.36756 | 2024-10-02 05:36:00 | NOAA-20 | BRASILÉIA | ACRE | Brasil | 1200104 | 12 | 33 | nan | nan | nan | Amazônia | 1.9 |
| c71096e3-8db1-341a-b1b9-56f3998980c1 | -10.67447 | -69.30013 | 2024-10-02 05:36:00 | NOAA-20 | BRASILÉIA | ACRE | Brasil | 1200104 | 12 | 33 | nan | nan | nan | Amazônia | 1.3 |
| 7510fa46-51dc-334a-9cf2-9d4214188e93 | -10.69465 | -69.39026 | 2024-10-02 05:36:00 | NOAA-20 | BRASILÉIA | ACRE | Brasil | 1200104 | 12 | 33 | nan | nan | nan | Amazônia | 10.0 |
| b1dee2ce-cf5f-37c4-a144-024c4b2eeb08 | -10.69512 | -69.39326 | 2024-10-02 05:36:00 | NOAA-20 | BRASILÉIA | ACRE | Brasil | 1200104 | 12 | 33 | nan | nan | nan | Amazônia | 9.6 |
| 52b0649c-6146-37d7-8a05-1a1cc8f9090b | -10.69556 | -69.38512 | 2024-10-02 05:36:00 | NOAA-20 | BRASILÉIA | ACRE | Brasil | 1200104 | 12 | 33 | nan | nan | nan | Amazônia | 10.0 |
| 44ed81eb-6847-379a-b0ee-d3db5ef4fa9b | -10.69599 | -69.3881 | 2024-10-02 05:36:00 | NOAA-20 | BRASILÉIA | ACRE | Brasil | 1200104 | 12 | 33 | nan | nan | nan | Amazônia | 9.6 |
| e397ff53-3738-3ab4-b6cb-745953f0d794 | -10.69951 | -69.3858 | 2024-10-02 05:36:00 | NOAA-20 | BRASILÉIA | ACRE | Brasil | 1200104 | 12 | 33 | nan | nan | nan | Amazônia | 3.0 |
| e615544d-c8a9-3270-85ec-f61a296df345 | -10.7008 | -69.38364 | 2024-10-02 05:36:00 | NOAA-20 | BRASILÉIA | ACRE | Brasil | 1200104 | 12 | 33 | nan | nan | nan | Amazônia | 3.5 |
| 21803f01-c049-3d6e-9740-2bb782b2cd85 | -10.70263 | -69.42108 | 2024-10-02 05:36:00 | NOAA-20 | BRASILÉIA | ACRE | Brasil | 1200104 | 12 | 33 | nan | nan | nan | Amazônia | 1.7 |
| cc4b2423-a228-38f2-ad6b-6e7ee22721cb | -10.70346 | -69.38646 | 2024-10-02 05:36:00 | NOAA-20 | BRASILÉIA | ACRE | Brasil | 1200104 | 12 | 33 | nan | nan | nan | Amazônia | 3.0 |
| 27ab1911-05d4-34e9-9767-dd9a6d6ab15b | -10.70389 | -69.38944 | 2024-10-02 05:36:00 | NOAA-20 | BRASILÉIA | ACRE | Brasil | 1200104 | 12 | 33 | nan | nan | nan | Amazônia | 3.4 |
| 97656822-3c0a-37c9-8898-ff5a6b23169a | -10.70475 | -69.38432 | 2024-10-02 05:36:00 | NOAA-20 | BRASILÉIA | ACRE | Brasil | 1200104 | 12 | 33 | nan | nan | nan | Amazônia | 2.2 |
| 2bfe4509-0242-3f49-99b9-221c13a30ae1 | -10.70504 | -69.42382 | 2024-10-02 05:36:00 | NOAA-20 | ASSIS BRASIL | ACRE | Brasil | 1200054 | 12 | 33 | nan | nan | nan | Amazônia | 2.3 |
| 7438d0f3-fd06-3a47-9006-5ff7eacd4d5d | -10.70594 | -69.41866 | 2024-10-02 05:36:00 | NOAA-20 | BRASILÉIA | ACRE | Brasil | 1200104 | 12 | 33 | nan | nan | nan | Amazônia | 2.3 |
| 3c7cd911-8efd-379e-a642-81c0ca832a83 | -10.7074 | -69.38715 | 2024-10-02 05:36:00 | NOAA-20 | BRASILÉIA | ACRE | Brasil | 1200104 | 12 | 33 | nan | nan | nan | Amazônia | 2.6 |
| d0c11ede-33cf-3c82-b22f-448e84fd9e37 | -10.709 | -69.42449 | 2024-10-02 05:36:00 | NOAA-20 | ASSIS BRASIL | ACRE | Brasil | 1200054 | 12 | 33 | nan | nan | nan | Amazônia | 2.9 |
| f27aff02-ec2e-36a3-8e3e-19a14eba3d02 | -16.4574 | -57.34756 | 2024-10-02 05:36:00 | NOAA-20 | CÁCERES | MATO GROSSO | Brasil | 5102504 | 51 | 33 | nan | nan | nan | Pantanal | 1.8 |
| 739a0e1a-1496-34ca-b350-903d76eba75c | -16.45484 | -57.32568 | 2024-10-02 05:36:00 | NOAA-20 | CÁCERES | MATO GROSSO | Brasil | 5102504 | 51 | 33 | nan | nan | nan | Pantanal | 2.2 |
| 6d3b9adb-f581-337f-a5b2-acaa26fbe3dc | -16.45241 | -57.43284 | 2024-10-02 05:36:00 | NOAA-20 | CÁCERES | MATO GROSSO | Brasil | 5102504 | 51 | 33 | nan | nan | nan | Pantanal | 2.9 |
| 80577e01-37d0-3d6c-86aa-bc364be78696 | -16.45205 | -57.43586 | 2024-10-02 05:36:00 | NOAA-20 | CÁCERES | MATO GROSSO | Brasil | 5102504 | 51 | 33 | nan | nan | nan | Pantanal | 2.9 |
| 9b4aa75d-27bc-30ef-b730-debeb6cbde1f | -16.45131 | -57.39903 | 2024-10-02 05:36:00 | NOAA-20 | CÁCERES | MATO GROSSO | Brasil | 5102504 | 51 | 33 | nan | nan | nan | Pantanal | 2.0 |
| 6e00d639-fb47-3cc8-bf28-7299ac39af75 | -16.45095 | -57.40204 | 2024-10-02 05:36:00 | NOAA-20 | CÁCERES | MATO GROSSO | Brasil | 5102504 | 51 | 33 | nan | nan | nan | Pantanal | 3.6 |
| 3d5e923e-11a7-34e2-9026-e49f54d5a65b | -16.44737 | -57.43224 | 2024-10-02 05:36:00 | NOAA-20 | CÁCERES | MATO GROSSO | Brasil | 5102504 | 51 | 33 | nan | nan | nan | Pantanal | 2.9 |
| 9aeff96e-84ae-37c9-a53d-37f36c5f7eb8 | -16.44701 | -57.43526 | 2024-10-02 05:36:00 | NOAA-20 | CÁCERES | MATO GROSSO | Brasil | 5102504 | 51 | 33 | nan | nan | nan | Pantanal | 2.9 |
| 6b3482ed-b7a4-3acc-b3e6-219de6244afa | -16.44626 | -57.39841 | 2024-10-02 05:36:00 | NOAA-20 | CÁCERES | MATO GROSSO | Brasil | 5102504 | 51 | 33 | nan | nan | nan | Pantanal | 3.3 |
| a6ab0fed-8c4c-373b-882b-4e8e075917b4 | -16.44591 | -57.40142 | 2024-10-02 05:36:00 | NOAA-20 | CÁCERES | MATO GROSSO | Brasil | 5102504 | 51 | 33 | nan | nan | nan | Pantanal | 1.5 |
| 12605f7d-2edd-31b0-a298-f2647a2cd076 | -16.44555 | -57.40444 | 2024-10-02 05:36:00 | NOAA-20 | CÁCERES | MATO GROSSO | Brasil | 5102504 | 51 | 33 | nan | nan | nan | Pantanal | 1.5 |
| 815209ba-606e-3cda-aa4a-528c15f19ac1 | -16.44363 | -57.33356 | 2024-10-02 05:36:00 | NOAA-20 | CÁCERES | MATO GROSSO | Brasil | 5102504 | 51 | 33 | nan | nan | nan | Pantanal | 1.6 |
| e56000a0-ec02-3338-b4d9-8e1f568b5986 | -16.44234 | -57.43161 | 2024-10-02 05:36:00 | NOAA-20 | CÁCERES | MATO GROSSO | Brasil | 5102504 | 51 | 33 | nan | nan | nan | Pantanal | 10.6 |
| 2b6a1595-b9e8-3763-88c3-eded69af8edc | -16.44163 | -57.4376 | 2024-10-02 05:36:00 | NOAA-20 | CÁCERES | MATO GROSSO | Brasil | 5102504 | 51 | 33 | nan | nan | nan | Pantanal | 18.9 |
| 2cff1dcc-3066-32b4-9098-0efb048ebc5e | -16.47258 | -57.30616 | 2024-10-02 05:36:00 | NOAA-20 | CÁCERES | MATO GROSSO | Brasil | 5102504 | 51 | 33 | nan | nan | nan | Pantanal | 3.5 |
| 57317684-8da6-3541-b339-b3079a9a9711 | -16.47149 | -57.31535 | 2024-10-02 05:36:00 | NOAA-20 | CÁCERES | MATO GROSSO | Brasil | 5102504 | 51 | 33 | nan | nan | nan | Pantanal | 2.0 |
| 3ec2f079-e56c-3734-8f94-489a6aa92298 | -16.47114 | -57.36154 | 2024-10-02 05:36:00 | NOAA-20 | CÁCERES | MATO GROSSO | Brasil | 5102504 | 51 | 33 | nan | nan | nan | Pantanal | 1.2 |
| 07ca981d-2ad4-3e05-9245-69fcd0815787 | -16.47113 | -57.31841 | 2024-10-02 05:36:00 | NOAA-20 | CÁCERES | MATO GROSSO | Brasil | 5102504 | 51 | 33 | nan | nan | nan | Pantanal | 1.0 |
| b12c21cb-ccf1-3798-a663-a841aee16ef2 | -16.46859 | -57.42561 | 2024-10-02 05:36:00 | NOAA-20 | CÁCERES | MATO GROSSO | Brasil | 5102504 | 51 | 33 | nan | nan | nan | Pantanal | 3.4 |
| bda3bb93-daad-3acb-9b6e-08fb32878879 | -16.46779 | -57.4263 | 2024-10-02 05:36:00 | NOAA-20 | CÁCERES | MATO GROSSO | Brasil | 5102504 | 51 | 33 | nan | nan | nan | Pantanal | 2.5 |
| c5d4b5bb-2b91-3564-a7e0-abadbf74a761 | -16.46714 | -57.3086 | 2024-10-02 05:36:00 | NOAA-20 | CÁCERES | MATO GROSSO | Brasil | 5102504 | 51 | 33 | nan | nan | nan | Pantanal | 7.5 |
| 8d4f5d3b-ed00-3518-9ed8-dc2357e25efd | -16.4668 | -57.38942 | 2024-10-02 05:36:00 | NOAA-20 | CÁCERES | MATO GROSSO | Brasil | 5102504 | 51 | 33 | nan | nan | nan | Pantanal | 2.3 |
| a45e9d81-a7a5-3469-ad59-0b61c6443f7b | -16.46678 | -57.31166 | 2024-10-02 05:36:00 | NOAA-20 | CÁCERES | MATO GROSSO | Brasil | 5102504 | 51 | 33 | nan | nan | nan | Pantanal | 4.7 |
| 2eb80de2-4862-3487-8082-ae8056c3733b | -16.46647 | -57.39244 | 2024-10-02 05:36:00 | NOAA-20 | CÁCERES | MATO GROSSO | Brasil | 5102504 | 51 | 33 | nan | nan | nan | Pantanal | 2.2 |
| 9eb7422d-30ff-3a2c-8413-d101d7884291 | -16.46644 | -57.35786 | 2024-10-02 05:36:00 | NOAA-20 | CÁCERES | MATO GROSSO | Brasil | 5102504 | 51 | 33 | nan | nan | nan | Pantanal | 1.4 |
| a139af91-0ddb-3070-828f-421b4d3469b5 | -16.46608 | -57.3609 | 2024-10-02 05:36:00 | NOAA-20 | CÁCERES | MATO GROSSO | Brasil | 5102504 | 51 | 33 | nan | nan | nan | Pantanal | 1.2 |
| 90d92543-6cdb-3ac4-9394-a121f704ff2e | -16.46534 | -57.32388 | 2024-10-02 05:36:00 | NOAA-20 | CÁCERES | MATO GROSSO | Brasil | 5102504 | 51 | 33 | nan | nan | nan | Pantanal | 1.2 |
| aa03ae94-4379-3ae7-a618-2dcb19ddbb9c | -16.46392 | -57.42197 | 2024-10-02 05:36:00 | NOAA-20 | CÁCERES | MATO GROSSO | Brasil | 5102504 | 51 | 33 | nan | nan | nan | Pantanal | 3.7 |
| 823ec55f-f135-3bbd-82ba-072cd9156cb7 | -10.7117 | -69.40904 | 2024-10-02 05:36:00 | NOAA-20 | BRASILÉIA | ACRE | Brasil | 1200104 | 12 | 33 | nan | nan | nan | Amazônia | 1.7 |
| e011f1bb-59a9-3b90-9ac6-e4d25df8da98 | -10.71565 | -69.40974 | 2024-10-02 05:36:00 | NOAA-20 | BRASILÉIA | ACRE | Brasil | 1200104 | 12 | 33 | nan | nan | nan | Amazônia | 1.7 |
| 63e6fbc1-2928-33c9-a29a-10e5220632ab | -10.71654 | -69.40466 | 2024-10-02 05:36:00 | NOAA-20 | BRASILÉIA | ACRE | Brasil | 1200104 | 12 | 33 | nan | nan | nan | Amazônia | 1.7 |
| 277105be-b63d-3924-a084-2c95ae3ced0f | -10.71871 | -69.41552 | 2024-10-02 05:36:00 | NOAA-20 | ASSIS BRASIL | ACRE | Brasil | 1200054 | 12 | 33 | nan | nan | nan | Amazônia | 1.9 |
| 637c2ef6-0a89-3230-a253-451f7f7c4f97 | -10.73578 | -69.43451 | 2024-10-02 05:36:00 | NOAA-20 | ASSIS BRASIL | ACRE | Brasil | 1200054 | 12 | 33 | nan | nan | nan | Amazônia | 1.9 |
| 46865187-7fc4-397f-a604-eeb3f79bef95 | -10.8127 | -69.68859 | 2024-10-02 05:36:00 | NOAA-20 | BRASILÉIA | ACRE | Brasil | 1200104 | 12 | 33 | nan | nan | nan | Amazônia | 0.6 |
| 6101de3a-9533-3599-82be-e7a1c77d19d6 | -10.81332 | -69.68502 | 2024-10-02 05:36:00 | NOAA-20 | BRASILÉIA | ACRE | Brasil | 1200104 | 12 | 33 | nan | nan | nan | Amazônia | 1.2 |
| 3539b219-989c-3833-a763-6a31af5371a7 | -10.81671 | -69.68932 | 2024-10-02 05:36:00 | NOAA-20 | BRASILÉIA | ACRE | Brasil | 1200104 | 12 | 33 | nan | nan | nan | Amazônia | 0.6 |
| 9e5ee406-fc89-3cf7-8df9-222410136c23 | -10.86142 | -69.50138 | 2024-10-02 05:36:00 | NOAA-20 | ASSIS BRASIL | ACRE | Brasil | 1200054 | 12 | 33 | nan | nan | nan | Amazônia | 11.9 |
| 8bb75e60-fd79-32f2-81a4-33ba50528fb7 | -10.8623 | -69.49628 | 2024-10-02 05:36:00 | NOAA-20 | ASSIS BRASIL | ACRE | Brasil | 1200054 | 12 | 33 | nan | nan | nan | Amazônia | 11.9 |
| 98c7ee6e-31e0-34a9-a896-cedcfb1113bc | -10.86538 | -69.50213 | 2024-10-02 05:36:00 | NOAA-20 | ASSIS BRASIL | ACRE | Brasil | 1200054 | 12 | 33 | nan | nan | nan | Amazônia | 11.9 |
| 42953eaf-ce93-3395-a874-32898788a5f6 | -10.87166 | -69.66662 | 2024-10-02 05:36:00 | NOAA-20 | ASSIS BRASIL | ACRE | Brasil | 1200054 | 12 | 33 | nan | nan | nan | Amazônia | 0.9 |
| 45d3d402-b655-37c7-965b-51e5ccdf77f8 | -10.88865 | -69.34253 | 2024-10-02 05:36:00 | NOAA-20 | BRASILÉIA | ACRE | Brasil | 1200104 | 12 | 33 | nan | nan | nan | Amazônia | 2.1 |
| 050c2553-2764-367a-b3fb-80b543e78389 | -10.89256 | -69.34325 | 2024-10-02 05:36:00 | NOAA-20 | BRASILÉIA | ACRE | Brasil | 1200104 | 12 | 33 | nan | nan | nan | Amazônia | 2.1 |
| 44de818d-c821-356d-8570-84fd57ff5e49 | -10.90424 | -69.29847 | 2024-10-02 05:36:00 | NOAA-20 | BRASILÉIA | ACRE | Brasil | 1200104 | 12 | 33 | nan | nan | nan | Amazônia | 3.2 |
| 0a9695e8-4956-373d-89ea-35a120a860bc | -10.90518 | -69.34034 | 2024-10-02 05:36:00 | NOAA-20 | BRASILÉIA | ACRE | Brasil | 1200104 | 12 | 33 | nan | nan | nan | Amazônia | 1.3 |
| 1cb37ddc-0b3f-32c3-b3a8-49ea9e45740c | -9.16908 | -70.21958 | 2024-10-02 05:36:00 | NOAA-20 | SANTA ROSA DO PURUS | ACRE | Brasil | 1200435 | 12 | 33 | nan | nan | nan | Amazônia | 1.4 |
| 0ff2e525-53c0-31cb-a592-697e51d138e5 | -16.46356 | -57.42499 | 2024-10-02 05:36:00 | NOAA-20 | CÁCERES | MATO GROSSO | Brasil | 5102504 | 51 | 33 | nan | nan | nan | Pantanal | 3.7 |
| 7be1b47b-46db-3af7-9fbe-419c5538ca7a | -16.46309 | -57.42265 | 2024-10-02 05:36:00 | NOAA-20 | CÁCERES | MATO GROSSO | Brasil | 5102504 | 51 | 33 | nan | nan | nan | Pantanal | 2.5 |
| 617599cc-7a08-3e0e-b0d8-fd897cd1cfd1 | -16.46283 | -57.43105 | 2024-10-02 05:36:00 | NOAA-20 | CÁCERES | MATO GROSSO | Brasil | 5102504 | 51 | 33 | nan | nan | nan | Pantanal | 3.4 |
| 4f6f8206-e759-3b9c-8d44-d36fcba9d01f | -16.4621 | -57.35118 | 2024-10-02 05:36:00 | NOAA-20 | CÁCERES | MATO GROSSO | Brasil | 5102504 | 51 | 33 | nan | nan | nan | Pantanal | 1.8 |
| 3d137c92-4252-3901-902f-02593783c730 | -16.4603 | -57.36636 | 2024-10-02 05:36:00 | NOAA-20 | CÁCERES | MATO GROSSO | Brasil | 5102504 | 51 | 33 | nan | nan | nan | Pantanal | 2.1 |
| 5afcf99e-94e4-372c-b715-70ff9c460e01 | -16.45991 | -57.32632 | 2024-10-02 05:36:00 | NOAA-20 | CÁCERES | MATO GROSSO | Brasil | 5102504 | 51 | 33 | nan | nan | nan | Pantanal | 1.2 |
| f507c739-5e5a-3757-8285-07a8a37d9747 | -16.45958 | -57.37244 | 2024-10-02 05:36:00 | NOAA-20 | CÁCERES | MATO GROSSO | Brasil | 5102504 | 51 | 33 | nan | nan | nan | Pantanal | 2.1 |
| 47996d0c-b3ae-3cee-8683-731b96090fd5 | -16.45922 | -57.37547 | 2024-10-02 05:36:00 | NOAA-20 | CÁCERES | MATO GROSSO | Brasil | 5102504 | 51 | 33 | nan | nan | nan | Pantanal | 2.1 |
| 9f871451-4d33-3454-b49c-76799d7f549b | -16.4578 | -57.43042 | 2024-10-02 05:36:00 | NOAA-20 | CÁCERES | MATO GROSSO | Brasil | 5102504 | 51 | 33 | nan | nan | nan | Pantanal | 3.4 |
| 4ea50259-70c7-3aef-b04d-c7465e40d774 | -16.45704 | -57.35058 | 2024-10-02 05:36:00 | NOAA-20 | CÁCERES | MATO GROSSO | Brasil | 5102504 | 51 | 33 | nan | nan | nan | Pantanal | 1.8 |
| 4dd601b2-d931-36fe-8c28-f67b0a3cdaf6 | -16.45635 | -57.39965 | 2024-10-02 05:36:00 | NOAA-20 | CÁCERES | MATO GROSSO | Brasil | 5102504 | 51 | 33 | nan | nan | nan | Pantanal | 2.0 |
| cf7b1bdf-081e-3704-b562-bd2d74d38ea0 | -16.44941 | -57.32811 | 2024-10-02 05:36:00 | NOAA-20 | CÁCERES | MATO GROSSO | Brasil | 5102504 | 51 | 33 | nan | nan | nan | Pantanal | 2.7 |
| 7c24b4d4-ce8d-30c4-ad0c-612a6f130453 | -16.4487 | -57.33419 | 2024-10-02 05:36:00 | NOAA-20 | CÁCERES | MATO GROSSO | Brasil | 5102504 | 51 | 33 | nan | nan | nan | Pantanal | 2.2 |
| e860889f-58a5-3191-9b9c-d10609711ba2 | -16.44328 | -57.33661 | 2024-10-02 05:36:00 | NOAA-20 | CÁCERES | MATO GROSSO | Brasil | 5102504 | 51 | 33 | nan | nan | nan | Pantanal | 1.6 |
| 8fda3798-4b5c-3855-81c4-b3990e1b2228 | -16.44198 | -57.43461 | 2024-10-02 05:36:00 | NOAA-20 | CÁCERES | MATO GROSSO | Brasil | 5102504 | 51 | 33 | nan | nan | nan | Pantanal | 10.6 |
| 9aa2b81f-ff38-31d8-b500-8a853404f053 | -16.44086 | -57.4008 | 2024-10-02 05:36:00 | NOAA-20 | CÁCERES | MATO GROSSO | Brasil | 5102504 | 51 | 33 | nan | nan | nan | Pantanal | 1.5 |


[Clique aqui para ver as próximas entradas](README181.md)
