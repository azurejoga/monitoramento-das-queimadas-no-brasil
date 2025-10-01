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

## Dados Diários - Página 96

| ID | Latitude | Longitude | Data/Hora GMT | Satélite | Município | Estado | País | Município ID | Estado ID | País ID | Dias sem Chuva | Precipitação | Risco de Fogo | Bioma | FRP |
|----|----------|-----------|---------------|----------|-----------|--------|------|--------------|-----------|---------|----------------|--------------|----------------|-------|-----|
| 8988fbe6-6842-3ad7-9813-2f11782a313f | -9.32404 | -50.62687 | 2025-10-01 04:51:00 | NPP-375D | SANTANA DO ARAGUAIA | PARÁ | Brasil | 1506708 | 15 | 33 | nan | nan | nan | Amazônia | 1.2 |
| 0048812f-5efa-3e17-913d-060f01c5dbf4 | -15.15142 | -48.01426 | 2025-10-01 04:51:00 | NPP-375D | PLANALTINA | GOIÁS | Brasil | 5217609 | 52 | 33 | nan | nan | nan | Cerrado | 0.8 |
| eee5fc0a-a802-344a-9654-2e89922d34df | -10.90291 | -46.531 | 2025-10-01 04:51:00 | NPP-375D | MATEIROS | TOCANTINS | Brasil | 1712702 | 17 | 33 | nan | nan | nan | Cerrado | 31.9 |
| 8d4c5113-299d-33d0-ba1f-3b9097824319 | -15.3363 | -46.27016 | 2025-10-01 04:51:00 | NPP-375D | FORMOSO | MINAS GERAIS | Brasil | 3126208 | 31 | 33 | nan | nan | nan | Cerrado | 2.0 |
| 4a97cbaa-0c88-3860-be48-7b4d2251ec87 | -11.52491 | -43.55765 | 2025-10-01 04:51:00 | NPP-375D | BARRA | BAHIA | Brasil | 2902708 | 29 | 33 | nan | nan | nan | Cerrado | 1.4 |
| 5dd5b6cc-e57c-3527-b247-4b7c1fd1efcc | -11.47734 | -45.1111 | 2025-10-01 04:51:00 | NPP-375D | RIACHÃO DAS NEVES | BAHIA | Brasil | 2926202 | 29 | 33 | nan | nan | nan | Cerrado | 1.2 |
| b9278044-7f36-3616-9881-b062460ba4c6 | -16.02849 | -50.89367 | 2025-10-01 04:51:00 | NPP-375D | JUSSARA | GOIÁS | Brasil | 5212204 | 52 | 33 | nan | nan | nan | Cerrado | 1.9 |
| 225b4686-00be-3fc7-ac65-2932abda8f70 | -13.45246 | -47.24442 | 2025-10-01 04:51:00 | NPP-375D | TERESINA DE GOIÁS | GOIÁS | Brasil | 5221080 | 52 | 33 | nan | nan | nan | Cerrado | 2.0 |
| d7a3810b-999c-38a8-8307-4f139b90d7e1 | -9.42542 | -54.70839 | 2025-10-01 04:51:00 | NPP-375D | NOVO PROGRESSO | PARÁ | Brasil | 1505031 | 15 | 33 | nan | nan | nan | Amazônia | 1.6 |
| dc4703a9-f606-328a-a1a9-0bb7fb57ec85 | -14.90914 | -51.67709 | 2025-10-01 04:51:00 | NPP-375D | ARAGUAIANA | MATO GROSSO | Brasil | 5101001 | 51 | 33 | nan | nan | nan | Cerrado | 3.3 |
| b09a9466-15a2-3892-9885-dbb065c180df | -13.13527 | -47.42381 | 2025-10-01 04:51:00 | NPP-375D | ARRAIAS | TOCANTINS | Brasil | 1702406 | 17 | 33 | nan | nan | nan | Cerrado | 6.4 |
| b9c21c08-4466-3213-96df-2e831d171798 | -16.3832 | -47.01816 | 2025-10-01 04:51:00 | NPP-375D | UNAÍ | MINAS GERAIS | Brasil | 3170404 | 31 | 33 | nan | nan | nan | Cerrado | 1.5 |
| 1a7b7aae-2d54-3d8f-b26c-919d4b2b35f3 | -11.82322 | -44.98838 | 2025-10-01 04:51:00 | NPP-375D | RIACHÃO DAS NEVES | BAHIA | Brasil | 2926202 | 29 | 33 | nan | nan | nan | Cerrado | 2.4 |
| 1d5c2d57-68a7-361a-8893-86098ba8c6b7 | -11.46231 | -45.00878 | 2025-10-01 04:51:00 | NPP-375D | RIACHÃO DAS NEVES | BAHIA | Brasil | 2926202 | 29 | 33 | nan | nan | nan | Cerrado | 1.5 |
| 8acf4c0c-5aec-3f93-bf31-c2b68ef06363 | -13.73472 | -48.69557 | 2025-10-01 04:51:00 | NPP-375D | CAMPINAÇU | GOIÁS | Brasil | 5204656 | 52 | 33 | nan | nan | nan | Cerrado | 1.5 |
| cbc517f7-9b68-30f3-8346-4cff6fac5a05 | -13.76673 | -47.96333 | 2025-10-01 04:51:00 | NPP-375D | CAVALCANTE | GOIÁS | Brasil | 5205307 | 52 | 33 | nan | nan | nan | Cerrado | 9.0 |
| 96a37dac-f7e7-3637-afb7-b5ea0a4602e4 | -11.54242 | -45.0646 | 2025-10-01 04:51:00 | NPP-375D | RIACHÃO DAS NEVES | BAHIA | Brasil | 2926202 | 29 | 33 | nan | nan | nan | Cerrado | 1.8 |
| 93e31f62-054b-32b6-a333-faf19b787760 | -11.85753 | -45.01852 | 2025-10-01 04:51:00 | NPP-375D | RIACHÃO DAS NEVES | BAHIA | Brasil | 2926202 | 29 | 33 | nan | nan | nan | Cerrado | 2.5 |
| 7f6ff283-b037-37cb-a462-fa62bf302122 | -10.62746 | -48.59352 | 2025-10-01 04:51:00 | NPP-375D | PORTO NACIONAL | TOCANTINS | Brasil | 1718204 | 17 | 33 | nan | nan | nan | Cerrado | 4.6 |
| 7055f456-f2bd-3b4c-ae3b-6e1ae0106cf3 | -15.26156 | -49.25451 | 2025-10-01 04:51:00 | NPP-375D | GOIANÉSIA | GOIÁS | Brasil | 5208608 | 52 | 33 | nan | nan | nan | Cerrado | 2.8 |
| e6704027-6c06-3dc1-83da-2530d11f348a | -11.05108 | -47.83083 | 2025-10-01 04:51:00 | NPP-375D | SILVANÓPOLIS | TOCANTINS | Brasil | 1720655 | 17 | 33 | nan | nan | nan | Cerrado | 5.1 |
| e1150b06-2eb9-3773-8b61-193e96e8cb59 | -13.91302 | -48.09175 | 2025-10-01 04:51:00 | NPP-375D | COLINAS DO SUL | GOIÁS | Brasil | 5205521 | 52 | 33 | nan | nan | nan | Cerrado | 0.9 |
| 01d7e672-95c5-3a72-a792-8ea98c91e975 | -14.36637 | -47.14511 | 2025-10-01 04:51:00 | NPP-375D | FLORES DE GOIÁS | GOIÁS | Brasil | 5207907 | 52 | 33 | nan | nan | nan | Cerrado | 2.8 |
| 40b1bca7-16fb-353d-9f5d-63c481ac1edc | -13.66365 | -48.05125 | 2025-10-01 04:51:00 | NPP-375D | CAVALCANTE | GOIÁS | Brasil | 5205307 | 52 | 33 | nan | nan | nan | Cerrado | 2.0 |
| e37079b6-677c-3af4-8714-bcfc810c73bb | -9.30551 | -51.56069 | 2025-10-01 04:51:00 | NPP-375D | SÃO FÉLIX DO XINGU | PARÁ | Brasil | 1507300 | 15 | 33 | nan | nan | nan | Amazônia | 0.6 |
| c8e10cc6-366e-382c-8da4-642b14d5e4d9 | -13.23102 | -47.32525 | 2025-10-01 04:51:00 | NPP-375D | ARRAIAS | TOCANTINS | Brasil | 1702406 | 17 | 33 | nan | nan | nan | Cerrado | 3.0 |
| a8bd34d0-15c7-3ee1-87eb-6cb5d6eef772 | -14.04004 | -47.96462 | 2025-10-01 04:51:00 | NPP-375D | COLINAS DO SUL | GOIÁS | Brasil | 5205521 | 52 | 33 | nan | nan | nan | Cerrado | 2.2 |
| 1c8da987-5e9c-3a97-af28-596d95b359d7 | -14.90129 | -47.21285 | 2025-10-01 04:51:00 | NPP-375D | VILA BOA | GOIÁS | Brasil | 5222203 | 52 | 33 | nan | nan | nan | Cerrado | 1.5 |
| 48383580-9de3-36b9-ab0f-6d31b7a96afb | -12.96066 | -48.43537 | 2025-10-01 04:51:00 | NPP-375D | PALMEIRÓPOLIS | TOCANTINS | Brasil | 1715754 | 17 | 33 | nan | nan | nan | Cerrado | 2.2 |
| 39a3e576-186e-3854-9351-4b8b238b0d35 | -13.6996 | -48.64244 | 2025-10-01 04:51:00 | NPP-375D | CAMPINAÇU | GOIÁS | Brasil | 5204656 | 52 | 33 | nan | nan | nan | Cerrado | 4.3 |
| bf1330c8-78a2-301d-b805-c17faf1e84ab | -10.84199 | -45.40703 | 2025-10-01 04:51:00 | NPP-375D | FORMOSA DO RIO PRETO | BAHIA | Brasil | 2911105 | 29 | 33 | nan | nan | nan | Cerrado | 1.9 |
| c2d05bea-ab57-31a8-babf-8d5e6a6a3573 | -13.37329 | -48.10666 | 2025-10-01 04:51:00 | NPP-375D | CAVALCANTE | GOIÁS | Brasil | 5205307 | 52 | 33 | nan | nan | nan | Cerrado | 1.3 |
| dff734f5-76b2-3c48-9a1a-452a2a4e4cfc | -14.18919 | -46.11315 | 2025-10-01 04:51:00 | NPP-375D | JABORANDI | BAHIA | Brasil | 2917359 | 29 | 33 | nan | nan | nan | Cerrado | 4.0 |
| 4a9a3bf1-d7a0-3f83-9435-ddb053fe5098 | -12.87999 | -46.94253 | 2025-10-01 04:51:00 | NPP-375D | ARRAIAS | TOCANTINS | Brasil | 1702406 | 17 | 33 | nan | nan | nan | Cerrado | 1.7 |
| 329a4efc-ccb6-31cc-878a-8020f283cedc | -9.429 | -54.70898 | 2025-10-01 04:51:00 | NPP-375D | NOVO PROGRESSO | PARÁ | Brasil | 1505031 | 15 | 33 | nan | nan | nan | Amazônia | 2.3 |
| ddb6764e-e4a7-3194-96ba-819aaecbcde4 | -12.82263 | -47.01908 | 2025-10-01 04:51:00 | NPP-375D | ARRAIAS | TOCANTINS | Brasil | 1702406 | 17 | 33 | nan | nan | nan | Cerrado | 4.0 |
| 49d262fb-7657-33fc-b7b1-5d81fe130828 | -11.36338 | -49.37453 | 2025-10-01 04:51:00 | NPP-375D | DUERÉ | TOCANTINS | Brasil | 1707306 | 17 | 33 | nan | nan | nan | Cerrado | 2.6 |
| 77bbe579-f166-37aa-b5c9-5e366d4e65c0 | -9.63206 | -50.89782 | 2025-10-01 04:51:00 | NPP-375D | SANTANA DO ARAGUAIA | PARÁ | Brasil | 1506708 | 15 | 33 | nan | nan | nan | Amazônia | 1.5 |
| 7ad56dd9-4c21-3a3c-82f9-4c7c4ee97737 | -16.19492 | -49.99174 | 2025-10-01 04:51:00 | NPP-375D | ITABERAÍ | GOIÁS | Brasil | 5210406 | 52 | 33 | nan | nan | nan | Cerrado | 12.2 |
| 032750f8-644d-316e-9556-02c348db14f3 | -15.27038 | -48.7779 | 2025-10-01 04:51:00 | NPP-375D | VILA PROPÍCIO | GOIÁS | Brasil | 5222302 | 52 | 33 | nan | nan | nan | Cerrado | 1.4 |
| e354add7-2f4b-3361-bfdc-866d5cf241c1 | -14.95637 | -46.88563 | 2025-10-01 04:51:00 | NPP-375D | FLORES DE GOIÁS | GOIÁS | Brasil | 5207907 | 52 | 33 | nan | nan | nan | Cerrado | 1.6 |
| f94c39e6-ee6b-3d7e-a6e1-cfe5d95b405e | -11.81782 | -44.99294 | 2025-10-01 04:51:00 | NPP-375D | RIACHÃO DAS NEVES | BAHIA | Brasil | 2926202 | 29 | 33 | nan | nan | nan | Cerrado | 2.0 |
| b0abb1d3-3c2a-37e8-84b0-5ea77f28e09c | -11.16856 | -47.21952 | 2025-10-01 04:51:00 | NPP-375D | ALMAS | TOCANTINS | Brasil | 1700400 | 17 | 33 | nan | nan | nan | Cerrado | 1.5 |
| a8a8fa99-aa20-3bad-acf6-0763dfc435df | -11.19551 | -47.20283 | 2025-10-01 04:51:00 | NPP-375D | ALMAS | TOCANTINS | Brasil | 1700400 | 17 | 33 | nan | nan | nan | Cerrado | 1.5 |
| 46bae9af-a338-3e55-91cc-f02ce3a41dec | -13.9256 | -48.10589 | 2025-10-01 04:51:00 | NPP-375D | COLINAS DO SUL | GOIÁS | Brasil | 5205521 | 52 | 33 | nan | nan | nan | Cerrado | 4.1 |
| f93a0ab7-0e1a-3463-9cbc-2f1c95b7fc40 | -11.46461 | -45.09995 | 2025-10-01 04:51:00 | NPP-375D | RIACHÃO DAS NEVES | BAHIA | Brasil | 2926202 | 29 | 33 | nan | nan | nan | Cerrado | 3.7 |
| 8b128da5-be8a-3246-8dff-bef3ac604959 | -14.61208 | -45.02179 | 2025-10-01 04:51:00 | NPP-375D | COCOS | BAHIA | Brasil | 2908101 | 29 | 33 | nan | nan | nan | Cerrado | 5.0 |
| 6b550724-eaec-3e7e-8cc0-bab1796c0360 | -11.12517 | -49.7844 | 2025-10-01 04:51:00 | NPP-375D | LAGOA DA CONFUSÃO | TOCANTINS | Brasil | 1711902 | 17 | 33 | nan | nan | nan | Cerrado | 1.4 |
| dea35ea2-b404-3883-9e16-27a331055901 | -15.25951 | -49.27022 | 2025-10-01 04:51:00 | NPP-375D | GOIANÉSIA | GOIÁS | Brasil | 5208608 | 52 | 33 | nan | nan | nan | Cerrado | 1.3 |
| 538657bc-09b7-3d3d-b01b-25ae38aeea46 | -10.02018 | -50.25313 | 2025-10-01 04:51:00 | NPP-375D | PIUM | TOCANTINS | Brasil | 1717503 | 17 | 33 | nan | nan | nan | Cerrado | 1.1 |
| ae935b1f-622d-3263-a705-9eaa8b837e2f | -11.57093 | -50.17762 | 2025-10-01 04:51:00 | NPP-375D | FORMOSO DO ARAGUAIA | TOCANTINS | Brasil | 1708205 | 17 | 33 | nan | nan | nan | Cerrado | 2.9 |
| 57dd36f1-428b-35c4-814e-efc30b6598a6 | -9.4039 | -54.70478 | 2025-10-01 04:51:00 | NPP-375D | NOVO PROGRESSO | PARÁ | Brasil | 1505031 | 15 | 33 | nan | nan | nan | Amazônia | 0.8 |
| f86287f2-8637-3fcc-88f7-9bb26dd15f3c | -10.63238 | -48.58548 | 2025-10-01 04:51:00 | NPP-375D | PORTO NACIONAL | TOCANTINS | Brasil | 1718204 | 17 | 33 | nan | nan | nan | Cerrado | 1.9 |
| 1af9157f-4217-368b-9400-4ae27dee68b8 | -14.90208 | -47.2146 | 2025-10-01 04:51:00 | NPP-375D | VILA BOA | GOIÁS | Brasil | 5222203 | 52 | 33 | nan | nan | nan | Cerrado | 1.2 |
| c3c484d2-ac06-36fb-9c0f-c5fc30f6ca86 | -15.47636 | -48.55128 | 2025-10-01 04:51:00 | NPP-375D | PADRE BERNARDO | GOIÁS | Brasil | 5215603 | 52 | 33 | nan | nan | nan | Cerrado | 1.5 |
| 3ac9c153-f542-3b53-baa3-59aa6895b36d | -13.74616 | -48.69047 | 2025-10-01 04:51:00 | NPP-375D | CAMPINAÇU | GOIÁS | Brasil | 5204656 | 52 | 33 | nan | nan | nan | Cerrado | 0.8 |
| 7847fc71-8967-34a7-90d8-62e92617603e | -14.71161 | -48.27053 | 2025-10-01 04:51:00 | NPP-375D | NIQUELÂNDIA | GOIÁS | Brasil | 5214606 | 52 | 33 | nan | nan | nan | Cerrado | 2.3 |
| 5eaa07ca-9ab0-3bd5-8bfb-441e72a54d35 | -11.8164 | -44.96726 | 2025-10-01 04:51:00 | NPP-375D | RIACHÃO DAS NEVES | BAHIA | Brasil | 2926202 | 29 | 33 | nan | nan | nan | Cerrado | 2.2 |
| 6f4d660a-e63d-3308-8616-36e6ce7c1b1e | -10.93271 | -46.50254 | 2025-10-01 04:51:00 | NPP-375D | MATEIROS | TOCANTINS | Brasil | 1712702 | 17 | 33 | nan | nan | nan | Cerrado | 3.7 |
| 99c8d9dd-f6de-3885-84d0-fa10bda533b5 | -12.24306 | -47.81544 | 2025-10-01 04:51:00 | NPP-375D | PARANÃ | TOCANTINS | Brasil | 1716208 | 17 | 33 | nan | nan | nan | Cerrado | 8.1 |
| 8a35e57a-bf40-3adb-9da1-ad9a44cdd143 | -14.83981 | -54.77774 | 2025-10-01 04:51:00 | NPP-375D | NOVA BRASILÂNDIA | MATO GROSSO | Brasil | 5106208 | 51 | 33 | nan | nan | nan | Cerrado | 1.3 |
| 6c253e88-13bc-3dd2-8d02-5fb421ecd453 | -16.4935 | -43.7312 | 2025-10-01 04:51:00 | NPP-375D | FRANCISCO SÁ | MINAS GERAIS | Brasil | 3126703 | 31 | 33 | nan | nan | nan | Cerrado | 0.8 |
| 5b920a55-8c33-3515-aeb5-694e9eba8f68 | -10.92855 | -54.3285 | 2025-10-01 04:51:00 | NPP-375D | MARCELÂNDIA | MATO GROSSO | Brasil | 5105580 | 51 | 33 | nan | nan | nan | Amazônia | 1.7 |
| 8ee6d1fa-a8a4-3955-9fcd-8a1c80930e53 | -12.90948 | -46.82096 | 2025-10-01 04:51:00 | NPP-375D | ARRAIAS | TOCANTINS | Brasil | 1702406 | 17 | 33 | nan | nan | nan | Cerrado | 2.0 |
| 6511ccb6-2225-3e1e-a145-fc11399f07dc | -13.56391 | -47.27757 | 2025-10-01 04:51:00 | NPP-375D | TERESINA DE GOIÁS | GOIÁS | Brasil | 5221080 | 52 | 33 | nan | nan | nan | Cerrado | 2.5 |
| f33f47aa-3352-38fb-ba8e-0dfdb61951ec | -12.23377 | -47.82476 | 2025-10-01 04:51:00 | NPP-375D | PARANÃ | TOCANTINS | Brasil | 1716208 | 17 | 33 | nan | nan | nan | Cerrado | 2.1 |
| 8238acba-d76f-315b-84f3-e6ecc330570d | -13.2285 | -48.45024 | 2025-10-01 04:51:00 | NPP-375D | PALMEIRÓPOLIS | TOCANTINS | Brasil | 1715754 | 17 | 33 | nan | nan | nan | Cerrado | 3.4 |
| 30b58880-8106-3e81-a597-f27a4eff8765 | -14.79684 | -45.79493 | 2025-10-01 04:51:00 | NPP-375D | COCOS | BAHIA | Brasil | 2908101 | 29 | 33 | nan | nan | nan | Cerrado | 14.5 |
| 94df4ab5-8688-31eb-8540-cd13e9975640 | -15.64 | -46.2525 | 2025-10-01 04:51:00 | NPP-375D | ARINOS | MINAS GERAIS | Brasil | 3104502 | 31 | 33 | nan | nan | nan | Cerrado | 0.9 |
| 5a8f730c-5155-3387-8d60-f990399cc108 | -14.89546 | -48.11037 | 2025-10-01 04:51:00 | NPP-375D | MIMOSO DE GOIÁS | GOIÁS | Brasil | 5213053 | 52 | 33 | nan | nan | nan | Cerrado | 2.4 |
| 24e7b473-5809-3035-9106-8497bae16c7f | -15.94395 | -46.23455 | 2025-10-01 04:51:00 | NPP-375D | ARINOS | MINAS GERAIS | Brasil | 3104502 | 31 | 33 | nan | nan | nan | Cerrado | 1.3 |
| 974cd599-4e83-3536-972e-6d06ce438fc1 | -12.9566 | -46.41806 | 2025-10-01 04:51:00 | NPP-375D | CAMPOS BELOS | GOIÁS | Brasil | 5204904 | 52 | 33 | nan | nan | nan | Cerrado | 4.2 |
| b0b78d6a-4387-31cc-be87-434d2f673e82 | -12.82435 | -50.57838 | 2025-10-01 04:51:00 | NPP-375D | FORMOSO DO ARAGUAIA | TOCANTINS | Brasil | 1708205 | 17 | 33 | nan | nan | nan | Cerrado | 2.8 |
| b1fc194a-6f7a-34b8-b5b4-b7491cf9047f | -14.37635 | -47.13504 | 2025-10-01 04:51:00 | NPP-375D | FLORES DE GOIÁS | GOIÁS | Brasil | 5207907 | 52 | 33 | nan | nan | nan | Cerrado | 2.4 |
| b2813da7-ce90-3760-9eaa-b0a4bd4688dc | -11.45592 | -43.51548 | 2025-10-01 04:51:00 | NPP-375D | BARRA | BAHIA | Brasil | 2902708 | 29 | 33 | nan | nan | nan | Cerrado | 1.4 |
| 4b7f97ca-680b-3387-bcc8-546546736d83 | -12.24522 | -47.79967 | 2025-10-01 04:51:00 | NPP-375D | PARANÃ | TOCANTINS | Brasil | 1716208 | 17 | 33 | nan | nan | nan | Cerrado | 3.0 |
| aa3d45fc-68b8-3527-a434-ac0b4af4854c | -9.31364 | -45.72343 | 2025-10-01 04:51:00 | NPP-375D | SANTA FILOMENA | PIAUÍ | Brasil | 2209203 | 22 | 33 | nan | nan | nan | Cerrado | 1.8 |
| 4a4e216a-af6e-3719-8a2d-4c87f5897cfc | -13.30826 | -47.20786 | 2025-10-01 04:51:00 | NPP-375D | MONTE ALEGRE DE GOIÁS | GOIÁS | Brasil | 5213509 | 52 | 33 | nan | nan | nan | Cerrado | 2.3 |
| 9e6d5055-9c36-3788-b676-617cf4fde32b | -15.28715 | -52.89378 | 2025-10-01 04:51:00 | NPP-375D | BARRA DO GARÇAS | MATO GROSSO | Brasil | 5101803 | 51 | 33 | nan | nan | nan | Cerrado | 1.1 |
| c10b43c0-8f61-37ea-9718-2a17a91e6b05 | -14.04737 | -47.98574 | 2025-10-01 04:51:00 | NPP-375D | COLINAS DO SUL | GOIÁS | Brasil | 5205521 | 52 | 33 | nan | nan | nan | Cerrado | 2.0 |
| 10c6a07e-b8e5-371d-96bb-79578a589c28 | -13.13628 | -47.4165 | 2025-10-01 04:51:00 | NPP-375D | ARRAIAS | TOCANTINS | Brasil | 1702406 | 17 | 33 | nan | nan | nan | Cerrado | 3.7 |
| d8cf2cb4-0151-392b-93cf-29261455bf39 | -11.918 | -47.89386 | 2025-10-01 04:51:00 | NPP-375D | SÃO VALÉRIO | TOCANTINS | Brasil | 1720499 | 17 | 33 | nan | nan | nan | Cerrado | 2.3 |
| 4bdc627d-601a-368d-8dea-83f36609f7fd | -14.02334 | -44.9744 | 2025-10-01 04:51:00 | NPP-375D | JABORANDI | BAHIA | Brasil | 2917359 | 29 | 33 | nan | nan | nan | Cerrado | 1.6 |
| 2dd6e95d-c2a8-38ba-b0b5-ca343b89cf73 | -13.72925 | -48.81188 | 2025-10-01 04:51:00 | NPP-375D | FORMOSO | GOIÁS | Brasil | 5208103 | 52 | 33 | nan | nan | nan | Cerrado | 2.3 |
| 46478358-a703-3210-9792-e0fe325fed4b | -14.03471 | -47.98912 | 2025-10-01 04:51:00 | NPP-375D | COLINAS DO SUL | GOIÁS | Brasil | 5205521 | 52 | 33 | nan | nan | nan | Cerrado | 1.2 |
| 018ffa7b-30f4-3f3f-99bb-0e4fc7fdeb1b | -12.0878 | -47.26246 | 2025-10-01 04:51:00 | NPP-375D | CONCEIÇÃO DO TOCANTINS | TOCANTINS | Brasil | 1705607 | 17 | 33 | nan | nan | nan | Cerrado | 1.1 |
| 9af3d60a-dbb0-33a8-a73b-23a55ec20396 | -14.78768 | -46.97544 | 2025-10-01 04:51:00 | NPP-375D | FLORES DE GOIÁS | GOIÁS | Brasil | 5207907 | 52 | 33 | nan | nan | nan | Cerrado | 0.9 |
| 2491d643-bd1a-3477-a442-c16c74ac0278 | -13.97827 | -45.05614 | 2025-10-01 04:51:00 | NPP-375D | JABORANDI | BAHIA | Brasil | 2917359 | 29 | 33 | nan | nan | nan | Cerrado | 2.0 |
| 22e07e32-6123-3183-8ab2-61c20b88d60a | -10.9044 | -46.55056 | 2025-10-01 04:51:00 | NPP-375D | MATEIROS | TOCANTINS | Brasil | 1712702 | 17 | 33 | nan | nan | nan | Cerrado | 4.3 |
| 586298ca-88ea-34c3-8d4b-4d8417655510 | -9.93277 | -43.65065 | 2025-10-01 04:51:00 | NPP-375D | PILÃO ARCADO | BAHIA | Brasil | 2924405 | 29 | 33 | nan | nan | nan | Cerrado | 6.2 |
| 4be044c9-9f1e-3a04-aff5-fed49afdbbd5 | -14.61137 | -48.21652 | 2025-10-01 04:51:00 | NPP-375D | NIQUELÂNDIA | GOIÁS | Brasil | 5214606 | 52 | 33 | nan | nan | nan | Cerrado | 1.2 |
| ff7f6d76-7147-3440-8ea0-47aa0f1b1d36 | -10.3518 | -43.74288 | 2025-10-01 04:51:00 | NPP-375D | PILÃO ARCADO | BAHIA | Brasil | 2924405 | 29 | 33 | nan | nan | nan | Cerrado | 1.1 |
| 515dbaec-e230-3e33-9b2b-be60537d2530 | -11.63352 | -47.48963 | 2025-10-01 04:51:00 | NPP-375D | NATIVIDADE | TOCANTINS | Brasil | 1714203 | 17 | 33 | nan | nan | nan | Cerrado | 5.7 |
| eb1f5e8e-5c58-3711-b67e-2394086818cc | -9.51222 | -54.74777 | 2025-10-01 04:51:00 | NPP-375D | NOVO PROGRESSO | PARÁ | Brasil | 1505031 | 15 | 33 | nan | nan | nan | Amazônia | 1.0 |
| 845e53bc-ec57-3f90-a1c0-c1deda79a63b | -16.02381 | -50.90126 | 2025-10-01 04:51:00 | NPP-375D | JUSSARA | GOIÁS | Brasil | 5212204 | 52 | 33 | nan | nan | nan | Cerrado | 3.6 |
| b88fffc2-ff6b-3e44-a7fe-8d73d17dd73c | -11.83055 | -44.96922 | 2025-10-01 04:51:00 | NPP-375D | RIACHÃO DAS NEVES | BAHIA | Brasil | 2926202 | 29 | 33 | nan | nan | nan | Cerrado | 1.8 |
| 9f959f78-9ae4-3350-9139-db9c35a492b2 | -14.89077 | -48.11503 | 2025-10-01 04:51:00 | NPP-375D | MIMOSO DE GOIÁS | GOIÁS | Brasil | 5213053 | 52 | 33 | nan | nan | nan | Cerrado | 5.5 |
| fe9daba5-a982-3338-8490-a3e01b38449b | -16.37918 | -47.0495 | 2025-10-01 04:51:00 | NPP-375D | UNAÍ | MINAS GERAIS | Brasil | 3170404 | 31 | 33 | nan | nan | nan | Cerrado | 2.3 |
| 5bbecf65-4a55-356d-a9dd-ce50f37c3c2e | -11.18294 | -47.20465 | 2025-10-01 04:51:00 | NPP-375D | ALMAS | TOCANTINS | Brasil | 1700400 | 17 | 33 | nan | nan | nan | Cerrado | 2.8 |
| c08510fa-8ce3-3c35-885f-19d7245ea849 | -9.40322 | -54.7089 | 2025-10-01 04:51:00 | NPP-375D | NOVO PROGRESSO | PARÁ | Brasil | 1505031 | 15 | 33 | nan | nan | nan | Amazônia | 0.8 |


[Clique aqui para ver as próximas entradas](README97.md)
