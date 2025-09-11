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

## Dados Diários - Página 61

| ID | Latitude | Longitude | Data/Hora GMT | Satélite | Município | Estado | País | Município ID | Estado ID | País ID | Dias sem Chuva | Precipitação | Risco de Fogo | Bioma | FRP |
|----|----------|-----------|---------------|----------|-----------|--------|------|--------------|-----------|---------|----------------|--------------|----------------|-------|-----|
| 34882376-0ae3-3ba2-8092-1a4d183b21f7 | -11.22575 | -55.00372 | 2025-09-11 04:23:00 | NPP-375D | CLÁUDIA | MATO GROSSO | Brasil | 5103056 | 51 | 33 | nan | nan | nan | Amazônia | 1.7 |
| 485dd6c7-40c5-3aaa-b927-51329cc307c5 | -9.68874 | -46.79182 | 2025-09-11 04:23:00 | NPP-375D | LIZARDA | TOCANTINS | Brasil | 1712405 | 17 | 33 | nan | nan | nan | Cerrado | 2.0 |
| b8e82ae0-4c66-37e8-9454-b0cbf4232551 | -12.92081 | -54.77026 | 2025-09-11 04:23:00 | NPP-375D | NOVA UBIRATÃ | MATO GROSSO | Brasil | 5106240 | 51 | 33 | nan | nan | nan | Amazônia | 1.1 |
| dbfe7d4e-9b67-392d-bc5e-4e2d1187cdc3 | -11.34293 | -46.49756 | 2025-09-11 04:23:00 | NPP-375D | FORMOSA DO RIO PRETO | BAHIA | Brasil | 2911105 | 29 | 33 | nan | nan | nan | Cerrado | 2.0 |
| 09f75f4f-05f6-3a51-83f7-69f5a1ea6800 | -11.47791 | -43.6861 | 2025-09-11 04:23:00 | NPP-375D | BARRA | BAHIA | Brasil | 2902708 | 29 | 33 | nan | nan | nan | Cerrado | 1.7 |
| 516a2506-85ae-3caf-90bf-78f30e64ddc8 | -9.09384 | -46.95172 | 2025-09-11 04:23:00 | NPP-375D | LIZARDA | TOCANTINS | Brasil | 1712405 | 17 | 33 | nan | nan | nan | Cerrado | 4.4 |
| 1f596f13-692e-38f6-a048-5b1e055b0bd0 | -11.46519 | -43.69982 | 2025-09-11 04:23:00 | NPP-375D | BARRA | BAHIA | Brasil | 2902708 | 29 | 33 | nan | nan | nan | Cerrado | 3.9 |
| f595d8c4-8b1d-3a6c-aed8-5c079e6430a1 | -11.47269 | -43.69706 | 2025-09-11 04:23:00 | NPP-375D | BARRA | BAHIA | Brasil | 2902708 | 29 | 33 | nan | nan | nan | Cerrado | 5.3 |
| 4467f625-f600-3bc2-b29d-79aa7148bf0e | -12.94319 | -54.8193 | 2025-09-11 04:23:00 | NPP-375D | NOVA UBIRATÃ | MATO GROSSO | Brasil | 5106240 | 51 | 33 | nan | nan | nan | Cerrado | 1.4 |
| 12fb47c9-172d-3a6a-b4de-9a01da3fc01b | -14.77526 | -48.2315 | 2025-09-11 04:23:00 | NPP-375D | NIQUELÂNDIA | GOIÁS | Brasil | 5214606 | 52 | 33 | nan | nan | nan | Cerrado | 2.3 |
| 5d893ff3-21e9-33ef-a66c-ea51ac70f65a | -11.79941 | -50.58587 | 2025-09-11 04:23:00 | NPP-375D | FORMOSO DO ARAGUAIA | TOCANTINS | Brasil | 1708205 | 17 | 33 | nan | nan | nan | Cerrado | 2.5 |
| 309ce820-3342-37a9-ab7c-2eaa043c172f | -11.7438 | -48.12045 | 2025-09-11 04:23:00 | NPP-375D | SÃO VALÉRIO | TOCANTINS | Brasil | 1720499 | 17 | 33 | nan | nan | nan | Cerrado | 1.0 |
| b61a69e9-af4e-3235-8375-d19a36a93c3a | -11.34129 | -46.48632 | 2025-09-11 04:23:00 | NPP-375D | FORMOSA DO RIO PRETO | BAHIA | Brasil | 2911105 | 29 | 33 | nan | nan | nan | Cerrado | 2.3 |
| eeb7fdf7-0232-3675-ad6f-1facc4973210 | -12.85981 | -47.96137 | 2025-09-11 04:23:00 | NPP-375D | PARANÃ | TOCANTINS | Brasil | 1716208 | 17 | 33 | nan | nan | nan | Cerrado | 1.8 |
| 5ea991e8-187e-392f-9f6c-8965ffe02ea7 | -11.46066 | -43.61268 | 2025-09-11 04:23:00 | NPP-375D | BARRA | BAHIA | Brasil | 2902708 | 29 | 33 | nan | nan | nan | Cerrado | 1.4 |
| bc5c755d-b691-3f58-9fe1-4f3e6f5ad743 | -12.55872 | -46.93202 | 2025-09-11 04:23:00 | NPP-375D | ARRAIAS | TOCANTINS | Brasil | 1702406 | 17 | 33 | nan | nan | nan | Cerrado | 3.1 |
| 7ecbfa8f-f4d4-3e69-86e4-897f913d65dc | -11.3814 | -43.51825 | 2025-09-11 04:23:00 | NPP-375D | BARRA | BAHIA | Brasil | 2902708 | 29 | 33 | nan | nan | nan | Cerrado | 2.4 |
| 1e15665a-a4f1-3fd2-8fd3-02288848e81a | -12.93085 | -54.80075 | 2025-09-11 04:23:00 | NPP-375D | NOVA UBIRATÃ | MATO GROSSO | Brasil | 5106240 | 51 | 33 | nan | nan | nan | Cerrado | 1.4 |
| 7e23aebc-a821-32e5-a207-07359bfaddd8 | -12.9462 | -54.74725 | 2025-09-11 04:23:00 | NPP-375D | NOVA UBIRATÃ | MATO GROSSO | Brasil | 5106240 | 51 | 33 | nan | nan | nan | Amazônia | 1.1 |
| 3225921f-204a-3a14-ab69-f4e181a859c0 | -14.13757 | -45.39815 | 2025-09-11 04:23:00 | NPP-375D | JABORANDI | BAHIA | Brasil | 2917359 | 29 | 33 | nan | nan | nan | Cerrado | 2.4 |
| 592eb15c-80d9-3fdf-a04e-e7f213430f9a | -9.07118 | -47.06993 | 2025-09-11 04:23:00 | NPP-375D | LIZARDA | TOCANTINS | Brasil | 1712405 | 17 | 33 | nan | nan | nan | Cerrado | 3.9 |
| f69188df-1ae3-3d1f-a82b-2ae1582c4d81 | -9.71213 | -43.53571 | 2025-09-11 04:23:00 | NPP-375D | PILÃO ARCADO | BAHIA | Brasil | 2924405 | 29 | 33 | nan | nan | nan | Cerrado | 1.5 |
| d032a311-4740-306a-9ac9-ff8909d13c4a | -9.08185 | -47.09095 | 2025-09-11 04:23:00 | NPP-375D | LIZARDA | TOCANTINS | Brasil | 1712405 | 17 | 33 | nan | nan | nan | Cerrado | 2.6 |
| 65f8d789-f374-325b-bdc5-5876a7da13cc | -9.96663 | -51.69181 | 2025-09-11 04:23:00 | NPP-375D | VILA RICA | MATO GROSSO | Brasil | 5108600 | 51 | 33 | nan | nan | nan | Amazônia | 1.0 |
| ac5348d7-32bc-3a9d-8315-d89aba144710 | -11.48555 | -43.6471 | 2025-09-11 04:23:00 | NPP-375D | BARRA | BAHIA | Brasil | 2902708 | 29 | 33 | nan | nan | nan | Cerrado | 4.3 |
| f18b0f01-1cfa-3075-be0f-b17101610414 | -11.4704 | -43.68886 | 2025-09-11 04:23:00 | NPP-375D | BARRA | BAHIA | Brasil | 2902708 | 29 | 33 | nan | nan | nan | Cerrado | 1.7 |
| 6b14e77b-ccae-3016-8a60-07a4a8ced3c9 | -11.15325 | -45.29831 | 2025-09-11 04:23:00 | NPP-375D | FORMOSA DO RIO PRETO | BAHIA | Brasil | 2911105 | 29 | 33 | nan | nan | nan | Cerrado | 1.0 |
| 49130ea3-eb72-35aa-889e-abb8a64f1555 | -10.66158 | -48.63985 | 2025-09-11 04:23:00 | NPP-375D | PORTO NACIONAL | TOCANTINS | Brasil | 1718204 | 17 | 33 | nan | nan | nan | Cerrado | 1.9 |
| 35b3ee9c-cb56-3fd4-9a51-f5c29ed22f2c | -9.05275 | -46.96733 | 2025-09-11 04:23:00 | NPP-375D | BALSAS | MARANHÃO | Brasil | 2101400 | 21 | 33 | nan | nan | nan | Cerrado | 1.9 |
| 58fa8b3e-61d9-3939-928f-b1b908cf77c3 | -12.88415 | -47.95731 | 2025-09-11 04:23:00 | NPP-375D | PARANÃ | TOCANTINS | Brasil | 1716208 | 17 | 33 | nan | nan | nan | Cerrado | 1.8 |
| cfa13b68-d785-3c47-be14-add7496c9f41 | -11.48264 | -43.63182 | 2025-09-11 04:23:00 | NPP-375D | BARRA | BAHIA | Brasil | 2902708 | 29 | 33 | nan | nan | nan | Cerrado | 2.8 |
| 1543e4ae-5b8f-3078-b2e7-cefd6b85c729 | -12.92575 | -54.79979 | 2025-09-11 04:23:00 | NPP-375D | NOVA UBIRATÃ | MATO GROSSO | Brasil | 5106240 | 51 | 33 | nan | nan | nan | Cerrado | 1.1 |
| 06f36ff6-2003-338d-84d9-d4c7080900b6 | -11.36513 | -46.54104 | 2025-09-11 04:23:00 | NPP-375D | FORMOSA DO RIO PRETO | BAHIA | Brasil | 2911105 | 29 | 33 | nan | nan | nan | Cerrado | 2.5 |
| bde10aaa-aadb-3b00-bfb1-2b41a670b263 | -11.48906 | -43.67128 | 2025-09-11 04:23:00 | NPP-375D | BARRA | BAHIA | Brasil | 2902708 | 29 | 33 | nan | nan | nan | Cerrado | 1.8 |
| abf61b0b-6f50-3b93-b1bc-d8fdf4349bc6 | -9.06032 | -47.07182 | 2025-09-11 04:23:00 | NPP-375D | LIZARDA | TOCANTINS | Brasil | 1712405 | 17 | 33 | nan | nan | nan | Cerrado | 1.6 |
| c1fd6d85-51a9-35c7-9360-70d4dbc8f32d | -11.42129 | -43.54317 | 2025-09-11 04:23:00 | NPP-375D | BARRA | BAHIA | Brasil | 2902708 | 29 | 33 | nan | nan | nan | Cerrado | 3.2 |
| d2887a9e-8228-3b23-9cc8-82f6c7655fcf | -9.59131 | -48.0639 | 2025-09-11 04:23:00 | NPP-375D | TOCANTÍNIA | TOCANTINS | Brasil | 1721109 | 17 | 33 | nan | nan | nan | Cerrado | 1.0 |
| c0ac2ca9-f783-3d04-98d3-94417479a544 | -8.52284 | -54.7691 | 2025-09-11 04:23:00 | NPP-375D | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 1.3 |
| 66a31467-5ced-379c-8c1a-2a6dc9e7de9a | -9.07803 | -50.48405 | 2025-09-11 04:23:00 | NPP-375D | SANTANA DO ARAGUAIA | PARÁ | Brasil | 1506708 | 15 | 33 | nan | nan | nan | Amazônia | 2.3 |
| f5f2b591-888e-3bed-83af-19622974a5c8 | -11.10548 | -48.42127 | 2025-09-11 04:23:00 | NPP-375D | IPUEIRAS | TOCANTINS | Brasil | 1709807 | 17 | 33 | nan | nan | nan | Cerrado | 2.1 |
| 1ca88e79-ffca-3cff-b887-2266013a077f | -9.89273 | -50.16587 | 2025-09-11 04:23:00 | NPP-375D | PIUM | TOCANTINS | Brasil | 1717503 | 17 | 33 | nan | nan | nan | Cerrado | 1.6 |
| 8e0c19d9-5614-3048-a1d0-bced9603222b | -12.42648 | -47.78995 | 2025-09-11 04:23:00 | NPP-375D | PARANÃ | TOCANTINS | Brasil | 1716208 | 17 | 33 | nan | nan | nan | Cerrado | 3.8 |
| 6d46b629-db8f-35e2-8b75-d85f983f547e | -12.42684 | -47.80925 | 2025-09-11 04:23:00 | NPP-375D | PARANÃ | TOCANTINS | Brasil | 1716208 | 17 | 33 | nan | nan | nan | Cerrado | 1.4 |
| e86be1ee-61d8-3d9d-a6a5-4275aac5e0a7 | -11.71122 | -41.73704 | 2025-09-11 04:23:00 | NPP-375D | CANARANA | BAHIA | Brasil | 2906204 | 29 | 33 | nan | nan | nan | Caatinga | 1.1 |
| 7eb0a61c-c677-3f61-b8a9-472795520812 | -13.3002 | -43.75138 | 2025-09-11 04:23:00 | NPP-375D | SERRA DO RAMALHO | BAHIA | Brasil | 2930154 | 29 | 33 | nan | nan | nan | Cerrado | 4.4 |
| 996c4001-de96-3d35-a830-b0bdc4fcd3f7 | -9.06079 | -46.96103 | 2025-09-11 04:23:00 | NPP-375D | BALSAS | MARANHÃO | Brasil | 2101400 | 21 | 33 | nan | nan | nan | Cerrado | 3.3 |
| 7a531a00-4e46-3db9-ba61-bc3a0931de30 | -9.6805 | -47.52394 | 2025-09-11 04:23:00 | NPP-375D | RIO SONO | TOCANTINS | Brasil | 1718758 | 17 | 33 | nan | nan | nan | Cerrado | 0.5 |
| 5567ec95-dea6-3f13-a5bf-5f23ec23f999 | -15.04009 | -48.08906 | 2025-09-11 04:23:00 | NPP-375D | MIMOSO DE GOIÁS | GOIÁS | Brasil | 5213053 | 52 | 33 | nan | nan | nan | Cerrado | 0.8 |
| 77b4621c-530e-3c48-992a-e015a0839259 | -9.06935 | -47.0812 | 2025-09-11 04:23:00 | NPP-375D | LIZARDA | TOCANTINS | Brasil | 1712405 | 17 | 33 | nan | nan | nan | Cerrado | 3.1 |
| 2252663e-3d95-3c6b-b27e-8e886c4cd854 | -10.52252 | -43.845 | 2025-09-11 04:23:00 | NPP-375D | BURITIRAMA | BAHIA | Brasil | 2904753 | 29 | 33 | nan | nan | nan | Cerrado | 1.4 |
| 4d64aec7-ce01-3782-895b-6bab73dfc3dc | -9.59456 | -48.05961 | 2025-09-11 04:23:00 | NPP-375D | TOCANTÍNIA | TOCANTINS | Brasil | 1721109 | 17 | 33 | nan | nan | nan | Cerrado | 1.4 |
| 4f1fb0b1-56ef-30c7-b7bb-f59a683b71d8 | -12.07235 | -50.99946 | 2025-09-11 04:23:00 | NPP-375D | SÃO FÉLIX DO ARAGUAIA | MATO GROSSO | Brasil | 5107859 | 51 | 33 | nan | nan | nan | Cerrado | 7.4 |
| 2e1e5193-dd29-3f99-b7b2-8f56c382a8b3 | -11.14601 | -45.27906 | 2025-09-11 04:23:00 | NPP-375D | FORMOSA DO RIO PRETO | BAHIA | Brasil | 2911105 | 29 | 33 | nan | nan | nan | Cerrado | 1.6 |
| 7920b39e-67e2-3c9b-ade2-c77248377252 | -15.12804 | -47.02802 | 2025-09-11 04:23:00 | NPP-375D | VILA BOA | GOIÁS | Brasil | 5222203 | 52 | 33 | nan | nan | nan | Cerrado | 2.2 |
| d951c782-a50c-3e23-b59c-284d85cdca5e | -11.72365 | -50.63386 | 2025-09-11 04:23:00 | NPP-375D | FORMOSO DO ARAGUAIA | TOCANTINS | Brasil | 1708205 | 17 | 33 | nan | nan | nan | Cerrado | 38.8 |
| 87c81d59-9f94-3e81-836f-66f1c019dd8a | -15.8042 | -42.57107 | 2025-09-11 04:23:00 | NPP-375D | RIO PARDO DE MINAS | MINAS GERAIS | Brasil | 3155603 | 31 | 33 | nan | nan | nan | Mata Atlântica | 1.8 |
| 67594a7e-aa63-337a-a09c-3c3d36d3b718 | -11.44157 | -43.57417 | 2025-09-11 04:23:00 | NPP-375D | BARRA | BAHIA | Brasil | 2902708 | 29 | 33 | nan | nan | nan | Cerrado | 2.4 |
| 560710b7-af51-3e74-ac61-4905c47f38b9 | -11.10192 | -48.42081 | 2025-09-11 04:23:00 | NPP-375D | IPUEIRAS | TOCANTINS | Brasil | 1709807 | 17 | 33 | nan | nan | nan | Cerrado | 2.0 |
| 09b97a31-e4a7-3529-8a53-d837a98bc7a3 | -9.08372 | -49.84814 | 2025-09-11 04:23:00 | NPP-375D | CASEARA | TOCANTINS | Brasil | 1703909 | 17 | 33 | nan | nan | nan | Cerrado | 2.1 |
| 1b1624b3-1f28-3465-a4dd-4928c1ff6a80 | -13.15966 | -45.28868 | 2025-09-11 04:23:00 | NPP-375D | CORRENTINA | BAHIA | Brasil | 2909307 | 29 | 33 | nan | nan | nan | Cerrado | 5.4 |
| 5a566a2e-0caa-3424-b873-ab1629f8fe91 | -9.49277 | -48.30624 | 2025-09-11 04:23:00 | NPP-375D | TOCANTÍNIA | TOCANTINS | Brasil | 1721109 | 17 | 33 | nan | nan | nan | Cerrado | 0.9 |
| 4494dc17-88e5-30b3-9e98-bbad56da2879 | -11.07498 | -42.30951 | 2025-09-11 04:23:00 | NPP-375D | ITAGUAÇU DA BAHIA | BAHIA | Brasil | 2915353 | 29 | 33 | nan | nan | nan | Caatinga | 0.9 |
| 4ff3af6f-e81b-3a06-a684-80d6d1ce3168 | -13.13724 | -54.91575 | 2025-09-11 04:23:00 | NPP-375D | NOVA UBIRATÃ | MATO GROSSO | Brasil | 5106240 | 51 | 33 | nan | nan | nan | Amazônia | 1.5 |
| ab4dae46-923b-3064-9995-bb3b3c2f6680 | -11.60297 | -52.21596 | 2025-09-11 04:23:00 | NPP-375D | SÃO FÉLIX DO ARAGUAIA | MATO GROSSO | Brasil | 5107859 | 51 | 33 | nan | nan | nan | Amazônia | 1.5 |
| 326a9226-0f38-3817-bc25-04206f874420 | -11.82378 | -46.74475 | 2025-09-11 04:23:00 | NPP-375D | NOVO JARDIM | TOCANTINS | Brasil | 1715259 | 17 | 33 | nan | nan | nan | Cerrado | 1.8 |
| e92bfcad-f690-3872-aba8-6ca5ab403a20 | -11.4003 | -45.59834 | 2025-09-11 04:23:00 | NPP-375D | FORMOSA DO RIO PRETO | BAHIA | Brasil | 2911105 | 29 | 33 | nan | nan | nan | Cerrado | 1.6 |
| 2ab8f18f-1a18-32ba-bd10-17e3474e7c3a | -12.85695 | -52.93824 | 2025-09-11 04:23:00 | NPP-375D | GAÚCHA DO NORTE | MATO GROSSO | Brasil | 5103858 | 51 | 33 | nan | nan | nan | Amazônia | 1.5 |
| 0b58e6a2-97a1-3dd4-9e46-38c802176680 | -14.40412 | -47.31982 | 2025-09-11 04:23:00 | NPP-375D | SÃO JOÃO D'ALIANÇA | GOIÁS | Brasil | 5220009 | 52 | 33 | nan | nan | nan | Cerrado | 2.5 |
| 34e6368a-b129-3350-8ab7-a47a1b1d6cda | -12.56807 | -44.64882 | 2025-09-11 04:23:00 | NPP-375D | BAIANÓPOLIS | BAHIA | Brasil | 2902500 | 29 | 33 | nan | nan | nan | Cerrado | 1.1 |
| 5eb9ae42-e8ed-3529-a7ec-5dc8facdf24f | -12.8898 | -47.96574 | 2025-09-11 04:23:00 | NPP-375D | PARANÃ | TOCANTINS | Brasil | 1716208 | 17 | 33 | nan | nan | nan | Cerrado | 1.2 |
| 00a5240f-7d35-31d5-82c8-626aa8cb6f66 | -13.97333 | -46.64853 | 2025-09-11 04:23:00 | NPP-375D | IACIARA | GOIÁS | Brasil | 5209903 | 52 | 33 | nan | nan | nan | Cerrado | 2.0 |
| 8544309d-f2c0-3cf1-b28e-b66c7a60cfe8 | -13.85448 | -43.82306 | 2025-09-11 04:23:00 | NPP-375D | CARINHANHA | BAHIA | Brasil | 2907103 | 29 | 33 | nan | nan | nan | Cerrado | 1.7 |
| 9e58f89c-a48c-30e2-8e40-95eb16532cd1 | -9.79614 | -51.09301 | 2025-09-11 04:23:00 | NPP-375D | VILA RICA | MATO GROSSO | Brasil | 5108600 | 51 | 33 | nan | nan | nan | Amazônia | 2.4 |
| 13ef03c8-0f09-325a-9526-2e4b0d60fe90 | -13.15631 | -45.28813 | 2025-09-11 04:23:00 | NPP-375D | CORRENTINA | BAHIA | Brasil | 2909307 | 29 | 33 | nan | nan | nan | Cerrado | 2.1 |
| 6206df64-26e2-309b-a93a-2001158854ff | -11.39168 | -43.52664 | 2025-09-11 04:23:00 | NPP-375D | BARRA | BAHIA | Brasil | 2902708 | 29 | 33 | nan | nan | nan | Cerrado | 1.6 |
| 873da5e0-08c9-3692-ab18-3b548b8d3418 | -12.844 | -52.96124 | 2025-09-11 04:23:00 | NPP-375D | GAÚCHA DO NORTE | MATO GROSSO | Brasil | 5103858 | 51 | 33 | nan | nan | nan | Amazônia | 1.3 |
| c3c00ffe-b79c-30f7-b6e4-628738ee9f69 | -11.65151 | -46.90781 | 2025-09-11 04:23:00 | NPP-375D | DIANÓPOLIS | TOCANTINS | Brasil | 1707009 | 17 | 33 | nan | nan | nan | Cerrado | 3.8 |
| ade75ae8-dffa-3a98-9cc3-025cb54df067 | -12.88514 | -47.97261 | 2025-09-11 04:23:00 | NPP-375D | PARANÃ | TOCANTINS | Brasil | 1716208 | 17 | 33 | nan | nan | nan | Cerrado | 1.1 |
| 1f5823a4-dc44-3837-bc20-42ccde688582 | -9.08125 | -46.96452 | 2025-09-11 04:23:00 | NPP-375D | LIZARDA | TOCANTINS | Brasil | 1712405 | 17 | 33 | nan | nan | nan | Cerrado | 13.3 |
| 52752b7c-738c-39a0-83ae-8e1864a6c1be | -11.36351 | -46.52982 | 2025-09-11 04:23:00 | NPP-375D | FORMOSA DO RIO PRETO | BAHIA | Brasil | 2911105 | 29 | 33 | nan | nan | nan | Cerrado | 8.3 |
| 82174a06-ca2e-330d-9bec-dfcc24ed319a | -9.03727 | -49.7715 | 2025-09-11 04:23:00 | NPP-375D | ARAGUACEMA | TOCANTINS | Brasil | 1701903 | 17 | 33 | nan | nan | nan | Cerrado | 2.2 |
| 8e12526d-468a-3b20-becc-1aeb74e0a906 | -11.34896 | -46.52414 | 2025-09-11 04:23:00 | NPP-375D | FORMOSA DO RIO PRETO | BAHIA | Brasil | 2911105 | 29 | 33 | nan | nan | nan | Cerrado | 0.7 |
| c2f68e6b-8c4b-3917-9c31-964b17010294 | -11.3866 | -43.53096 | 2025-09-11 04:23:00 | NPP-375D | BARRA | BAHIA | Brasil | 2902708 | 29 | 33 | nan | nan | nan | Cerrado | 1.6 |
| 6e9150ba-61e4-3d22-aadd-5bd9ae0435ab | -9.91145 | -49.91101 | 2025-09-11 04:23:00 | NPP-375D | PIUM | TOCANTINS | Brasil | 1717503 | 17 | 33 | nan | nan | nan | Cerrado | 0.7 |
| 9b789298-609c-3234-befe-001ae59a87b9 | -11.36571 | -46.53748 | 2025-09-11 04:23:00 | NPP-375D | FORMOSA DO RIO PRETO | BAHIA | Brasil | 2911105 | 29 | 33 | nan | nan | nan | Cerrado | 2.5 |
| 6d375edf-6ab1-328f-9bb2-adbc12052a9d | -13.78709 | -46.28614 | 2025-09-11 04:23:00 | NPP-375D | GUARANI DE GOIÁS | GOIÁS | Brasil | 5209408 | 52 | 33 | nan | nan | nan | Cerrado | 9.0 |
| 6be01509-0818-369c-8d90-aa6a6dcaddbd | -10.258 | -48.82165 | 2025-09-11 04:23:00 | NPP-375D | PARAÍSO DO TOCANTINS | TOCANTINS | Brasil | 1716109 | 17 | 33 | nan | nan | nan | Cerrado | 1.9 |
| a383195e-750b-3cc7-a1c7-69eeae0b9cc3 | -10.56699 | -43.66774 | 2025-09-11 04:23:00 | NPP-375D | BURITIRAMA | BAHIA | Brasil | 2904753 | 29 | 33 | nan | nan | nan | Cerrado | 2.2 |
| a6ec7b43-5a30-34a8-80a6-f58234c17705 | -9.52437 | -54.641 | 2025-09-11 04:23:00 | NPP-375D | NOVO PROGRESSO | PARÁ | Brasil | 1505031 | 15 | 33 | nan | nan | nan | Amazônia | 0.8 |
| 5145d427-af36-3eba-9366-a08d2eab0329 | -15.77938 | -43.13472 | 2025-09-11 04:23:00 | NPP-375D | PORTEIRINHA | MINAS GERAIS | Brasil | 3152204 | 31 | 33 | nan | nan | nan | Caatinga | 2.3 |
| ffa052f6-d56e-322d-ab01-ba74ff0cf156 | -15.24994 | -44.03585 | 2025-09-11 04:23:00 | NPP-375D | ITACARAMBI | MINAS GERAIS | Brasil | 3132107 | 31 | 33 | nan | nan | nan | Cerrado | 2.5 |
| 098635b7-b2b2-3de8-bc36-2b379bcf547c | -15.22578 | -44.05288 | 2025-09-11 04:23:00 | NPP-375D | ITACARAMBI | MINAS GERAIS | Brasil | 3132107 | 31 | 33 | nan | nan | nan | Cerrado | 2.1 |
| dcacc123-c829-37df-845d-c2c0afe983ec | -12.94359 | -54.74731 | 2025-09-11 04:23:00 | NPP-375D | NOVA UBIRATÃ | MATO GROSSO | Brasil | 5106240 | 51 | 33 | nan | nan | nan | Amazônia | 1.5 |
| 3550cb6b-0f26-3c61-aa80-7375bde7adbe | -11.15435 | -45.29126 | 2025-09-11 04:23:00 | NPP-375D | FORMOSA DO RIO PRETO | BAHIA | Brasil | 2911105 | 29 | 33 | nan | nan | nan | Cerrado | 1.5 |
| 4d658b39-d663-3601-afbf-c39f8ab8fa7d | -11.10261 | -48.4167 | 2025-09-11 04:23:00 | NPP-375D | IPUEIRAS | TOCANTINS | Brasil | 1709807 | 17 | 33 | nan | nan | nan | Cerrado | 2.0 |
| 1f4b49c9-186a-3bb3-b40f-cba793047007 | -9.82827 | -46.08383 | 2025-09-11 04:23:00 | NPP-375D | ALTO PARNAÍBA | MARANHÃO | Brasil | 2100501 | 21 | 33 | nan | nan | nan | Cerrado | 0.9 |
| 39a59882-3db2-3169-bb08-3dca54a18b16 | -13.96175 | -48.22725 | 2025-09-11 04:23:00 | NPP-375D | COLINAS DO SUL | GOIÁS | Brasil | 5205521 | 52 | 33 | nan | nan | nan | Cerrado | 4.4 |
| b03a6e6e-386b-3f9c-a6fc-ca0d521e81dc | -9.07282 | -49.84109 | 2025-09-11 04:23:00 | NPP-375D | CASEARA | TOCANTINS | Brasil | 1703909 | 17 | 33 | nan | nan | nan | Cerrado | 1.2 |
| 5a26a77f-ff45-3b73-a9dd-171d10ab0ca9 | -12.88857 | -47.97318 | 2025-09-11 04:23:00 | NPP-375D | PARANÃ | TOCANTINS | Brasil | 1716208 | 17 | 33 | nan | nan | nan | Cerrado | 1.1 |
| 83e3475d-9d4d-344e-a397-12c9beca52ca | -10.48536 | -49.37192 | 2025-09-11 04:23:00 | NPP-375D | CRISTALÂNDIA | TOCANTINS | Brasil | 1706100 | 17 | 33 | nan | nan | nan | Cerrado | 1.6 |


[Clique aqui para ver as próximas entradas](README62.md)
