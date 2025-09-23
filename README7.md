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

## Dados Diários - Página 7

| ID | Latitude | Longitude | Data/Hora GMT | Satélite | Município | Estado | País | Município ID | Estado ID | País ID | Dias sem Chuva | Precipitação | Risco de Fogo | Bioma | FRP |
|----|----------|-----------|---------------|----------|-----------|--------|------|--------------|-----------|---------|----------------|--------------|----------------|-------|-----|
| c0a10c60-0d84-3898-8fb5-1ba8b296e051 | -11.40602 | -44.95238 | 2025-09-23 03:57:00 | NPP-375D | RIACHÃO DAS NEVES | BAHIA | Brasil | 2926202 | 29 | 33 | nan | nan | nan | Cerrado | 2.4 |
| 94a25d51-094b-3ebc-9412-9b596fdea16e | -5.6833 | -41.39939 | 2025-09-23 03:57:00 | NPP-375D | SÃO MIGUEL DO TAPUIO | PIAUÍ | Brasil | 2210409 | 22 | 33 | nan | nan | nan | Caatinga | 1.5 |
| 33b3822d-05ff-3f78-b45a-580b952b4f46 | -8.95223 | -44.48681 | 2025-09-23 03:57:00 | NPP-375D | CURRAIS | PIAUÍ | Brasil | 2203230 | 22 | 33 | nan | nan | nan | Cerrado | 1.4 |
| 278d9eeb-ca93-3c4b-9441-c030587ff0c6 | -6.25887 | -45.33434 | 2025-09-23 03:57:00 | NPP-375D | FERNANDO FALCÃO | MARANHÃO | Brasil | 2104081 | 21 | 33 | nan | nan | nan | Cerrado | 3.3 |
| f8ae996a-84ae-32db-b811-be36e7f6027d | -11.40868 | -44.93695 | 2025-09-23 03:57:00 | NPP-375D | RIACHÃO DAS NEVES | BAHIA | Brasil | 2926202 | 29 | 33 | nan | nan | nan | Cerrado | 4.0 |
| 40efb390-7d9f-3b89-b6fe-ff21010bf278 | -11.42061 | -44.95046 | 2025-09-23 03:57:00 | NPP-375D | RIACHÃO DAS NEVES | BAHIA | Brasil | 2926202 | 29 | 33 | nan | nan | nan | Cerrado | 2.7 |
| 95e299d2-a6b3-3469-a8b7-2dfc42d93e9f | -11.81997 | -43.16593 | 2025-09-23 03:57:00 | NPP-375D | MORPARÁ | BAHIA | Brasil | 2921609 | 29 | 33 | nan | nan | nan | Caatinga | 2.9 |
| 7ae14c37-6a0f-325c-9d4a-dcc6049b3712 | -7.88137 | -44.02134 | 2025-09-23 03:57:00 | NPP-375D | SEBASTIÃO LEAL | PIAUÍ | Brasil | 2210631 | 22 | 33 | nan | nan | nan | Cerrado | 5.1 |
| fb423109-a02e-3953-ac73-de86f0778567 | -8.37967 | -44.70086 | 2025-09-23 03:57:00 | NPP-375D | PALMEIRA DO PIAUÍ | PIAUÍ | Brasil | 2207405 | 22 | 33 | nan | nan | nan | Cerrado | 1.1 |
| 48d21d16-10ec-335c-bb24-566be03a2cc3 | -8.00017 | -45.73001 | 2025-09-23 03:57:00 | NPP-375D | TASSO FRAGOSO | MARANHÃO | Brasil | 2112001 | 21 | 33 | nan | nan | nan | Cerrado | 1.7 |
| 86fb1663-a415-3d3a-872a-b3322a8a786c | -11.21317 | -46.17096 | 2025-09-23 03:57:00 | NPP-375D | FORMOSA DO RIO PRETO | BAHIA | Brasil | 2911105 | 29 | 33 | nan | nan | nan | Cerrado | 1.5 |
| 0995cb7d-fe43-36c9-99ba-f4020158f8c6 | -5.10668 | -43.16631 | 2025-09-23 03:57:00 | NPP-375D | CAXIAS | MARANHÃO | Brasil | 2103000 | 21 | 33 | nan | nan | nan | Cerrado | 0.6 |
| 989a8967-1f05-3e81-9987-512620f7c6a2 | -9.31687 | -43.36355 | 2025-09-23 03:57:00 | NPP-375D | CARACOL | PIAUÍ | Brasil | 2202505 | 22 | 33 | nan | nan | nan | Caatinga | 2.3 |
| 2c37f9ca-f3f7-3439-b243-d07b58aa9dd5 | -11.20869 | -46.17012 | 2025-09-23 03:57:00 | NPP-375D | FORMOSA DO RIO PRETO | BAHIA | Brasil | 2911105 | 29 | 33 | nan | nan | nan | Cerrado | 2.3 |
| 81c51204-8d60-3387-925b-7ae4316f1704 | -8.80496 | -43.07655 | 2025-09-23 03:57:00 | NPP-375D | JUREMA | PIAUÍ | Brasil | 2205532 | 22 | 33 | nan | nan | nan | Caatinga | 1.2 |
| be67f6a1-0f57-3a09-bef1-1e533b57b51b | -7.88193 | -44.02917 | 2025-09-23 03:57:00 | NPP-375D | SEBASTIÃO LEAL | PIAUÍ | Brasil | 2210631 | 22 | 33 | nan | nan | nan | Cerrado | 5.1 |
| b59d2b15-9802-389c-8ad4-a43372beafa4 | -3.62323 | -51.91587 | 2025-09-23 03:57:00 | NPP-375D | SENADOR JOSÉ PORFÍRIO | PARÁ | Brasil | 1507805 | 15 | 33 | nan | nan | nan | Amazônia | 3.4 |
| 8f2974a3-114b-36e1-8ffd-d7468b224a82 | -5.2364 | -43.69523 | 2025-09-23 03:57:00 | NPP-375D | CAXIAS | MARANHÃO | Brasil | 2103000 | 21 | 33 | nan | nan | nan | Cerrado | 1.3 |
| 4cbade15-d364-3821-aa4c-1b463399d3d8 | -6.41165 | -43.7676 | 2025-09-23 03:57:00 | NPP-375D | SÃO JOÃO DOS PATOS | MARANHÃO | Brasil | 2111102 | 21 | 33 | nan | nan | nan | Cerrado | 1.4 |
| 251cffa7-4266-3436-a43e-1425289d8668 | -4.77857 | -42.76382 | 2025-09-23 03:57:00 | NPP-375D | JOSÉ DE FREITAS | PIAUÍ | Brasil | 2205508 | 22 | 33 | nan | nan | nan | Cerrado | 1.8 |
| 1eba1de5-326d-33cd-81c9-e2467ed062eb | -4.37974 | -43.28824 | 2025-09-23 03:57:00 | NPP-375D | ALDEIAS ALTAS | MARANHÃO | Brasil | 2100303 | 21 | 33 | nan | nan | nan | Cerrado | 1.3 |
| 65a2a8fe-7965-3855-bd10-93a38b9b71fb | -7.18461 | -39.669 | 2025-09-23 03:57:00 | NPP-375D | SANTANA DO CARIRI | CEARÁ | Brasil | 2312106 | 23 | 33 | nan | nan | nan | Caatinga | 1.0 |
| 7f3d3e92-7f6c-3cb3-abb0-5c85115663de | -8.19552 | -44.41378 | 2025-09-23 03:57:00 | NPP-375D | URUÇUÍ | PIAUÍ | Brasil | 2211209 | 22 | 33 | nan | nan | nan | Cerrado | 1.3 |
| 8c30029c-9c7f-3711-94f1-867bc53d7110 | -11.88902 | -41.27422 | 2025-09-23 03:57:00 | NPP-375D | BONITO | BAHIA | Brasil | 2904050 | 29 | 33 | nan | nan | nan | Caatinga | 4.4 |
| adb31347-117b-39d5-bbb3-7d72691f23fc | -8.54362 | -44.92459 | 2025-09-23 03:57:00 | NPP-375D | BAIXA GRANDE DO RIBEIRO | PIAUÍ | Brasil | 2201150 | 22 | 33 | nan | nan | nan | Cerrado | 2.5 |
| 2ea8583a-9d41-31e4-8502-9cb6a00b7cc4 | -3.63169 | -51.91391 | 2025-09-23 03:57:00 | NPP-375D | SENADOR JOSÉ PORFÍRIO | PARÁ | Brasil | 1507805 | 15 | 33 | nan | nan | nan | Amazônia | 4.0 |
| 0abbd77f-c260-3cef-be5b-d586bd22d34e | -9.00926 | -48.02494 | 2025-09-23 03:57:00 | NPP-375D | BOM JESUS DO TOCANTINS | TOCANTINS | Brasil | 1703305 | 17 | 33 | nan | nan | nan | Cerrado | 0.6 |
| 452b5735-ccac-3325-b271-40e683b973d1 | -7.16861 | -44.43607 | 2025-09-23 03:57:00 | NPP-375D | URUÇUÍ | PIAUÍ | Brasil | 2211209 | 22 | 33 | nan | nan | nan | Cerrado | 2.0 |
| d813c88f-3e6d-3628-a960-0b498eca0e9a | -9.48097 | -40.35928 | 2025-09-23 03:57:00 | NPP-375D | JUAZEIRO | BAHIA | Brasil | 2918407 | 29 | 33 | nan | nan | nan | Caatinga | 3.9 |
| 84995ea2-c1bd-3aae-a7f4-0774ff05bdb9 | -3.62449 | -51.91208 | 2025-09-23 03:57:00 | NPP-375D | SENADOR JOSÉ PORFÍRIO | PARÁ | Brasil | 1507805 | 15 | 33 | nan | nan | nan | Amazônia | 4.0 |
| a1e3267a-9316-3cae-be93-a9afd7bf99be | -4.76396 | -43.62732 | 2025-09-23 03:57:00 | NPP-375D | CAXIAS | MARANHÃO | Brasil | 2103000 | 21 | 33 | nan | nan | nan | Cerrado | 1.8 |
| cb23cf1e-6bd0-3af9-9614-f8e43fb9ba6f | -7.89618 | -44.02037 | 2025-09-23 03:57:00 | NPP-375D | SEBASTIÃO LEAL | PIAUÍ | Brasil | 2210631 | 22 | 33 | nan | nan | nan | Cerrado | 4.8 |
| ddb5fea0-4197-3a60-a6bd-e1d5ea7fa1f8 | -6.89832 | -44.76288 | 2025-09-23 03:57:00 | NPP-375D | SÃO FÉLIX DE BALSAS | MARANHÃO | Brasil | 2110807 | 21 | 33 | nan | nan | nan | Cerrado | 1.9 |
| 3a25ccda-36c0-3134-83e5-7bb760cbfe4f | -8.52131 | -44.97584 | 2025-09-23 03:57:00 | NPP-375D | BAIXA GRANDE DO RIBEIRO | PIAUÍ | Brasil | 2201150 | 22 | 33 | nan | nan | nan | Cerrado | 3.9 |
| 6766916b-f8a3-370b-9dee-6242b3f57290 | -4.4057 | -44.37317 | 2025-09-23 03:57:00 | NPP-375D | PERITORÓ | MARANHÃO | Brasil | 2108454 | 21 | 33 | nan | nan | nan | Cerrado | 2.5 |
| 2706973f-f087-39b0-ba1b-0bf1a8b483cd | -7.89207 | -44.01964 | 2025-09-23 03:57:00 | NPP-375D | SEBASTIÃO LEAL | PIAUÍ | Brasil | 2210631 | 22 | 33 | nan | nan | nan | Cerrado | 4.8 |
| 62bac692-ebe6-3c89-a933-ca3c616ff998 | -11.40258 | -44.9476 | 2025-09-23 03:57:00 | NPP-375D | RIACHÃO DAS NEVES | BAHIA | Brasil | 2926202 | 29 | 33 | nan | nan | nan | Cerrado | 2.4 |
| f634f866-4eb2-3b8a-997f-6621608a98b1 | -8.522 | -44.97185 | 2025-09-23 03:57:00 | NPP-375D | BAIXA GRANDE DO RIBEIRO | PIAUÍ | Brasil | 2201150 | 22 | 33 | nan | nan | nan | Cerrado | 5.1 |
| 60834d4a-4b65-3493-b8f8-79462ca159e6 | -4.7845 | -47.25772 | 2025-09-23 03:57:00 | NPP-375D | AÇAILÂNDIA | MARANHÃO | Brasil | 2100055 | 21 | 33 | nan | nan | nan | Amazônia | 2.8 |
| 3f9ab6e4-f41d-3fa3-a1ad-6987052ee334 | -3.64279 | -48.32632 | 2025-09-23 03:57:00 | NPP-375D | PARAGOMINAS | PARÁ | Brasil | 1505502 | 15 | 33 | nan | nan | nan | Amazônia | 2.9 |
| d666938d-2b86-3acc-8d89-57f25f54ee16 | -11.02547 | -45.89781 | 2025-09-23 03:57:00 | NPP-375D | FORMOSA DO RIO PRETO | BAHIA | Brasil | 2911105 | 29 | 33 | nan | nan | nan | Cerrado | 3.9 |
| dd81e8d2-66a9-3ea7-92de-3b16e99ef02c | -11.40691 | -44.95549 | 2025-09-23 03:57:00 | NPP-375D | RIACHÃO DAS NEVES | BAHIA | Brasil | 2926202 | 29 | 33 | nan | nan | nan | Cerrado | 4.5 |
| dc9ce7a7-ddd3-3320-8ae1-bda5ecdd611d | -8.52563 | -44.9511 | 2025-09-23 03:57:00 | NPP-375D | BAIXA GRANDE DO RIBEIRO | PIAUÍ | Brasil | 2201150 | 22 | 33 | nan | nan | nan | Cerrado | 18.3 |
| 73a9b5b9-e9c0-36de-aa0c-c0f6244b6285 | -6.67327 | -38.49817 | 2025-09-23 03:57:00 | NPP-375D | SÃO JOÃO DO RIO DO PEIXE | PARAÍBA | Brasil | 2500700 | 25 | 33 | nan | nan | nan | Caatinga | 1.5 |
| 1aad7916-ae9f-39c4-8fa0-ddb8a242d177 | -12.64609 | -39.44162 | 2025-09-23 03:57:00 | NPP-375D | SANTA TEREZINHA | BAHIA | Brasil | 2928505 | 29 | 33 | nan | nan | nan | Mata Atlântica | 2.1 |
| 3df9605a-09a2-3a0c-9063-7280e6cfb361 | -7.90028 | -44.02119 | 2025-09-23 03:57:00 | NPP-375D | SEBASTIÃO LEAL | PIAUÍ | Brasil | 2210631 | 22 | 33 | nan | nan | nan | Cerrado | 1.6 |
| ace38f9a-ab3f-3b7d-b66c-71a254f99db9 | -7.86338 | -42.95423 | 2025-09-23 03:57:00 | NPP-375D | FLORES DO PIAUÍ | PIAUÍ | Brasil | 2203800 | 22 | 33 | nan | nan | nan | Caatinga | 1.8 |
| 22057781-020f-3015-b1c9-656b3af12880 | -5.98006 | -44.12769 | 2025-09-23 03:57:00 | NPP-375D | COLINAS | MARANHÃO | Brasil | 2103505 | 21 | 33 | nan | nan | nan | Cerrado | 6.6 |
| ce69e92e-612c-3770-88f2-dc9a56a423c9 | -7.88899 | -44.02647 | 2025-09-23 03:57:00 | NPP-375D | SEBASTIÃO LEAL | PIAUÍ | Brasil | 2210631 | 22 | 33 | nan | nan | nan | Cerrado | 6.7 |
| 22f8eebf-e7ff-3973-8832-4acd70241d9c | -11.89024 | -41.26673 | 2025-09-23 03:57:00 | NPP-375D | BONITO | BAHIA | Brasil | 2904050 | 29 | 33 | nan | nan | nan | Caatinga | 7.4 |
| 33e7b2e8-b4d2-32b3-8ada-e600a8250ea3 | -3.52158 | -49.44759 | 2025-09-23 03:57:00 | NPP-375D | BREU BRANCO | PARÁ | Brasil | 1501782 | 15 | 33 | nan | nan | nan | Amazônia | 3.4 |
| bd14baa6-71d8-3b1b-99f0-becd1d8e2f60 | -7.28182 | -41.86679 | 2025-09-23 03:57:00 | NPP-375D | WALL FERRAZ | PIAUÍ | Brasil | 2211704 | 22 | 33 | nan | nan | nan | Caatinga | 1.5 |
| 99274190-d276-3c38-a655-78aedd149184 | -5.73821 | -42.60401 | 2025-09-23 03:57:00 | NPP-375D | OLHO D'ÁGUA DO PIAUÍ | PIAUÍ | Brasil | 2207108 | 22 | 33 | nan | nan | nan | Caatinga | 2.0 |
| 172a9bea-f19a-32e1-83f5-5a55bceee714 | -8.52203 | -44.94614 | 2025-09-23 03:57:00 | NPP-375D | BAIXA GRANDE DO RIBEIRO | PIAUÍ | Brasil | 2201150 | 22 | 33 | nan | nan | nan | Cerrado | 3.8 |
| 22511a35-cdb0-3206-bb6b-4ee86854d706 | -5.23578 | -43.69905 | 2025-09-23 03:57:00 | NPP-375D | CAXIAS | MARANHÃO | Brasil | 2103000 | 21 | 33 | nan | nan | nan | Cerrado | 1.3 |
| 0bd1aac3-646a-397f-9fbd-301043726761 | -11.52247 | -43.63574 | 2025-09-23 03:57:00 | NPP-375D | BARRA | BAHIA | Brasil | 2902708 | 29 | 33 | nan | nan | nan | Cerrado | 0.8 |
| 123a068a-1f64-3b95-9e32-c5edcd9bfdd9 | -4.38036 | -43.28451 | 2025-09-23 03:57:00 | NPP-375D | ALDEIAS ALTAS | MARANHÃO | Brasil | 2100303 | 21 | 33 | nan | nan | nan | Cerrado | 1.3 |
| 4847437d-96c7-3e48-bc60-3e89512d6790 | -3.516 | -49.45248 | 2025-09-23 03:57:00 | NPP-375D | BREU BRANCO | PARÁ | Brasil | 1501782 | 15 | 33 | nan | nan | nan | Amazônia | 7.3 |
| bf8bd3fa-2d77-3369-a2b7-c278043531c5 | -11.40419 | -44.94693 | 2025-09-23 03:57:00 | NPP-375D | RIACHÃO DAS NEVES | BAHIA | Brasil | 2926202 | 29 | 33 | nan | nan | nan | Cerrado | 5.2 |
| a94c8d65-9dd6-3f50-9149-bdc3741c6c23 | -8.80197 | -43.07106 | 2025-09-23 03:57:00 | NPP-375D | JUREMA | PIAUÍ | Brasil | 2205532 | 22 | 33 | nan | nan | nan | Caatinga | 1.5 |
| 145a73fc-7f5f-3847-ba52-4b3a8aa7b9ca | -10.76485 | -40.27625 | 2025-09-23 03:57:00 | NPP-375D | PINDOBAÇU | BAHIA | Brasil | 2924603 | 29 | 33 | nan | nan | nan | Caatinga | 0.6 |
| cdca5298-d6cc-322e-953c-ef061568df6c | -12.35493 | -40.29576 | 2025-09-23 03:57:00 | NPP-375D | ITABERABA | BAHIA | Brasil | 2914703 | 29 | 33 | nan | nan | nan | Caatinga | 0.5 |
| 2c3183bc-8ac5-3db1-85f6-45e99a84c8d1 | -11.53547 | -43.6212 | 2025-09-23 03:57:00 | NPP-375D | BARRA | BAHIA | Brasil | 2902708 | 29 | 33 | nan | nan | nan | Cerrado | 1.4 |
| 12f29c0a-bd39-35f0-accf-a424f4479bb1 | -6.41229 | -43.76371 | 2025-09-23 03:57:00 | NPP-375D | SÃO JOÃO DOS PATOS | MARANHÃO | Brasil | 2111102 | 21 | 33 | nan | nan | nan | Cerrado | 1.2 |
| 1e44a5ea-13c5-3a08-80aa-f29559d74343 | -5.38403 | -42.25494 | 2025-09-23 03:57:00 | NPP-375D | ALTO LONGÁ | PIAUÍ | Brasil | 2200301 | 22 | 33 | nan | nan | nan | Caatinga | 2.9 |
| 041da004-a50d-35ae-bd50-744a5fa9f207 | -7.88732 | -44.02257 | 2025-09-23 03:57:00 | NPP-375D | SEBASTIÃO LEAL | PIAUÍ | Brasil | 2210631 | 22 | 33 | nan | nan | nan | Cerrado | 7.0 |
| 5e2779a2-a437-3bc0-8f09-555e5581d909 | -5.5709 | -43.60415 | 2025-09-23 03:57:00 | NPP-375D | PARNARAMA | MARANHÃO | Brasil | 2107803 | 21 | 33 | nan | nan | nan | Cerrado | 0.8 |
| cf5bc8f7-edbd-3c99-838c-22f5e21737a3 | -11.45966 | -43.52316 | 2025-09-23 03:57:00 | NPP-375D | BARRA | BAHIA | Brasil | 2902708 | 29 | 33 | nan | nan | nan | Cerrado | 1.9 |
| 095bd8a8-c22a-394d-8252-eeca7b6275d6 | -4.0783 | -48.03963 | 2025-09-23 03:57:00 | NPP-375D | DOM ELISEU | PARÁ | Brasil | 1502939 | 15 | 33 | nan | nan | nan | Amazônia | 1.7 |
| be8e6a1d-0c6b-3202-b9fc-1a430804b2ee | -5.12532 | -40.7464 | 2025-09-23 03:57:00 | NPP-375D | CRATEÚS | CEARÁ | Brasil | 2304103 | 23 | 33 | nan | nan | nan | Caatinga | 1.7 |
| dd193e37-18e5-3699-ba33-70cb237643e9 | -8.52274 | -44.96765 | 2025-09-23 03:57:00 | NPP-375D | BAIXA GRANDE DO RIBEIRO | PIAUÍ | Brasil | 2201150 | 22 | 33 | nan | nan | nan | Cerrado | 5.1 |
| fe550c3b-1e3c-326f-8f5d-b1ee2f2c52d9 | -7.28868 | -44.15535 | 2025-09-23 03:57:00 | NPP-375D | ANTÔNIO ALMEIDA | PIAUÍ | Brasil | 2200806 | 22 | 33 | nan | nan | nan | Cerrado | 2.9 |
| 6388f894-0ab0-3ab3-80a2-7cbcc37dab9c | -7.06222 | -45.05544 | 2025-09-23 03:57:00 | NPP-375D | LORETO | MARANHÃO | Brasil | 2106102 | 21 | 33 | nan | nan | nan | Cerrado | 1.8 |
| 1f99acdc-13e6-3276-a7b2-467a3702349b | -8.80642 | -43.07947 | 2025-09-23 03:57:00 | NPP-375D | JUREMA | PIAUÍ | Brasil | 2205532 | 22 | 33 | nan | nan | nan | Caatinga | 1.7 |
| d3403356-fdf6-3ff4-80ff-ff79aa744b50 | -4.40123 | -44.37246 | 2025-09-23 03:57:00 | NPP-375D | PERITORÓ | MARANHÃO | Brasil | 2108454 | 21 | 33 | nan | nan | nan | Cerrado | 2.5 |
| 138dd311-ef48-360b-a24a-cc149eb60302 | -8.92498 | -44.47047 | 2025-09-23 03:57:00 | NPP-375D | CURRAIS | PIAUÍ | Brasil | 2203230 | 22 | 33 | nan | nan | nan | Cerrado | 1.0 |
| 4b4a116d-a0c7-35c5-99ca-e69989759a2b | -7.1643 | -44.43549 | 2025-09-23 03:57:00 | NPP-375D | URUÇUÍ | PIAUÍ | Brasil | 2211209 | 22 | 33 | nan | nan | nan | Cerrado | 2.0 |
| 66910f31-3ed9-3d34-8be4-7ba8701c7225 | -11.20949 | -46.16572 | 2025-09-23 03:57:00 | NPP-375D | FORMOSA DO RIO PRETO | BAHIA | Brasil | 2911105 | 29 | 33 | nan | nan | nan | Cerrado | 6.7 |
| 32583245-5335-373f-95ae-ffca0fcafd6e | -11.4076 | -44.95167 | 2025-09-23 03:57:00 | NPP-375D | RIACHÃO DAS NEVES | BAHIA | Brasil | 2926202 | 29 | 33 | nan | nan | nan | Cerrado | 3.1 |
| 230d19fb-dec0-327e-bd05-74debb60e4ca | -4.64698 | -43.37401 | 2025-09-23 03:57:00 | NPP-375D | CAXIAS | MARANHÃO | Brasil | 2103000 | 21 | 33 | nan | nan | nan | Cerrado | 1.2 |
| 100a878b-b12a-3d2b-bb46-cbc052987e93 | -11.40736 | -44.94457 | 2025-09-23 03:57:00 | NPP-375D | RIACHÃO DAS NEVES | BAHIA | Brasil | 2926202 | 29 | 33 | nan | nan | nan | Cerrado | 2.5 |
| f6744245-9075-3b36-98d2-10471815cd58 | -5.73782 | -42.60645 | 2025-09-23 03:57:00 | NPP-375D | OLHO D'ÁGUA DO PIAUÍ | PIAUÍ | Brasil | 2207108 | 22 | 33 | nan | nan | nan | Caatinga | 2.8 |
| ecb47cc7-62d8-38d1-9df9-3eb07e5ed6fd | -11.52628 | -43.6364 | 2025-09-23 03:57:00 | NPP-375D | BARRA | BAHIA | Brasil | 2902708 | 29 | 33 | nan | nan | nan | Cerrado | 2.5 |
| de3cabea-2d8d-3c86-845e-4943af5f6169 | -7.89555 | -44.02401 | 2025-09-23 03:57:00 | NPP-375D | SEBASTIÃO LEAL | PIAUÍ | Brasil | 2210631 | 22 | 33 | nan | nan | nan | Cerrado | 4.0 |
| 6ff24905-ddc5-3f3e-9d3a-9041c14c35d7 | -7.8861 | -44.01841 | 2025-09-23 03:57:00 | NPP-375D | SEBASTIÃO LEAL | PIAUÍ | Brasil | 2210631 | 22 | 33 | nan | nan | nan | Cerrado | 3.7 |
| b9d7570d-1c28-3fc4-a7dd-25bf78d11531 | -11.02624 | -45.89342 | 2025-09-23 03:57:00 | NPP-375D | FORMOSA DO RIO PRETO | BAHIA | Brasil | 2911105 | 29 | 33 | nan | nan | nan | Cerrado | 3.9 |
| 6241576c-eee2-3b5a-bcc0-bdd5e9ccbe0a | -11.41582 | -44.9534 | 2025-09-23 03:57:00 | NPP-375D | RIACHÃO DAS NEVES | BAHIA | Brasil | 2926202 | 29 | 33 | nan | nan | nan | Cerrado | 2.7 |
| 5539215b-ed13-364f-a20d-1e517be7eff9 | -7.04067 | -41.99921 | 2025-09-23 03:57:00 | NPP-375D | OEIRAS | PIAUÍ | Brasil | 2207009 | 22 | 33 | nan | nan | nan | Caatinga | 2.1 |
| 95ab06d1-48fb-3ff9-b11d-31143d41015a | -8.52133 | -44.95015 | 2025-09-23 03:57:00 | NPP-375D | BAIXA GRANDE DO RIBEIRO | PIAUÍ | Brasil | 2201150 | 22 | 33 | nan | nan | nan | Cerrado | 18.3 |
| 9d8a1840-67e5-3799-8bd4-1f8a6354039e | -9.9941 | -46.28504 | 2025-09-23 03:57:00 | NPP-375D | ALTO PARNAÍBA | MARANHÃO | Brasil | 2100501 | 21 | 33 | nan | nan | nan | Cerrado | 1.8 |
| 5a0697d8-cfbf-38e8-a95b-4ffa34fb71f4 | -10.57719 | -43.82242 | 2025-09-23 03:57:00 | NPP-375D | BURITIRAMA | BAHIA | Brasil | 2904753 | 29 | 33 | nan | nan | nan | Cerrado | 1.2 |
| a55e64b5-6311-32cc-8734-fd43bc4ac44b | -7.18854 | -39.66597 | 2025-09-23 03:57:00 | NPP-375D | SANTANA DO CARIRI | CEARÁ | Brasil | 2312106 | 23 | 33 | nan | nan | nan | Caatinga | 0.5 |
| 7f2b0ae5-9834-3fc5-a43b-f9413df81b7d | -11.02347 | -45.89942 | 2025-09-23 03:57:00 | NPP-375D | FORMOSA DO RIO PRETO | BAHIA | Brasil | 2911105 | 29 | 33 | nan | nan | nan | Cerrado | 2.5 |
| 0e826f41-21b4-3e6e-ba55-417a8d683bdc | -7.50242 | -35.24694 | 2025-09-23 03:57:00 | NPP-375D | TIMBAÚBA | PERNAMBUCO | Brasil | 2615300 | 26 | 33 | nan | nan | nan | Mata Atlântica | 7.2 |
| 360419bd-fe43-3b4e-9b08-14a7a4ec0266 | -5.75342 | -42.60872 | 2025-09-23 03:57:00 | NPP-375D | LAGOINHA DO PIAUÍ | PIAUÍ | Brasil | 2205540 | 22 | 33 | nan | nan | nan | Caatinga | 2.9 |
| 13b167b6-9ffc-3e68-85c0-f35266c57953 | -8.96061 | -44.48805 | 2025-09-23 03:57:00 | NPP-375D | CURRAIS | PIAUÍ | Brasil | 2203230 | 22 | 33 | nan | nan | nan | Cerrado | 1.9 |
| 57769178-7e24-35e3-abdf-93c29a85f2f0 | -11.40488 | -44.94309 | 2025-09-23 03:57:00 | NPP-375D | RIACHÃO DAS NEVES | BAHIA | Brasil | 2926202 | 29 | 33 | nan | nan | nan | Cerrado | 3.3 |
| cea95751-4bc5-33c8-a7cc-b6bdb8bae41c | -11.89583 | -41.27537 | 2025-09-23 03:57:00 | NPP-375D | BONITO | BAHIA | Brasil | 2904050 | 29 | 33 | nan | nan | nan | Caatinga | 1.1 |
| 63bb41d9-11db-31c8-81ca-c7fca2a240d4 | -8.13927 | -44.46513 | 2025-09-23 03:57:00 | NPP-375D | URUÇUÍ | PIAUÍ | Brasil | 2211209 | 22 | 33 | nan | nan | nan | Cerrado | 2.7 |
| 83f1b058-13bd-3374-a9fe-17418dd6c8c6 | -8.13903 | -44.46418 | 2025-09-23 03:57:00 | NPP-375D | URUÇUÍ | PIAUÍ | Brasil | 2211209 | 22 | 33 | nan | nan | nan | Cerrado | 4.5 |


[Clique aqui para ver as próximas entradas](README8.md)
