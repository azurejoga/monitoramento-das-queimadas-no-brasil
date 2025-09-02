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

## Dados Diários - Página 22

| ID | Latitude | Longitude | Data/Hora GMT | Satélite | Município | Estado | País | Município ID | Estado ID | País ID | Dias sem Chuva | Precipitação | Risco de Fogo | Bioma | FRP |
|----|----------|-----------|---------------|----------|-----------|--------|------|--------------|-----------|---------|----------------|--------------|----------------|-------|-----|
| 9e160a4e-df63-3d50-ba44-428da031ef82 | -7.56102 | -45.71125 | 2025-09-02 03:51:00 | NPP-375D | SAMBAÍBA | MARANHÃO | Brasil | 2109700 | 21 | 33 | nan | nan | nan | Cerrado | 1.0 |
| d12efb16-892b-3f74-9b20-8a46450deff1 | -9.12568 | -46.05176 | 2025-09-02 03:51:00 | NPP-375D | ALTO PARNAÍBA | MARANHÃO | Brasil | 2100501 | 21 | 33 | nan | nan | nan | Cerrado | 2.9 |
| 26b63666-ad5a-3082-8eae-a78f6594cc34 | -9.73175 | -48.98436 | 2025-09-02 03:51:00 | NPP-375D | DIVINÓPOLIS DO TOCANTINS | TOCANTINS | Brasil | 1707108 | 17 | 33 | nan | nan | nan | Cerrado | 3.1 |
| 6e42dd3b-609a-3ab7-aef9-d4a22c949959 | -13.36921 | -46.93804 | 2025-09-02 03:51:00 | NPP-375D | MONTE ALEGRE DE GOIÁS | GOIÁS | Brasil | 5213509 | 52 | 33 | nan | nan | nan | Cerrado | 0.9 |
| d83042ff-d3b3-3b13-b113-aed5e3fe3d78 | -7.53391 | -45.35941 | 2025-09-02 03:51:00 | NPP-375D | LORETO | MARANHÃO | Brasil | 2106102 | 21 | 33 | nan | nan | nan | Cerrado | 1.8 |
| 4263fea1-ce74-3ad3-86b3-daf6d84588c7 | -12.95393 | -48.09208 | 2025-09-02 03:51:00 | NPP-375D | PARANÃ | TOCANTINS | Brasil | 1716208 | 17 | 33 | nan | nan | nan | Cerrado | 2.6 |
| 3165f90b-219b-3fa9-bd0c-bd7ee936a735 | -11.35508 | -43.67569 | 2025-09-02 03:51:00 | NPP-375D | BARRA | BAHIA | Brasil | 2902708 | 29 | 33 | nan | nan | nan | Cerrado | 1.0 |
| fa60a63f-be2e-3eda-b268-5ad22dab571b | -8.74591 | -46.12445 | 2025-09-02 03:51:00 | NPP-375D | TASSO FRAGOSO | MARANHÃO | Brasil | 2112001 | 21 | 33 | nan | nan | nan | Cerrado | 1.5 |
| b77c8f0e-8276-37f6-87c6-35384ec709e3 | -8.45913 | -47.35954 | 2025-09-02 03:51:00 | NPP-375D | GOIATINS | TOCANTINS | Brasil | 1709005 | 17 | 33 | nan | nan | nan | Cerrado | 1.3 |
| 9286addf-54eb-3f29-850a-5e6a268d5a46 | -15.02662 | -42.14924 | 2025-09-02 03:51:00 | NPP-375D | CONDEÚBA | BAHIA | Brasil | 2908705 | 29 | 33 | nan | nan | nan | Caatinga | 2.7 |
| 406182fd-c0da-3d30-a18f-7fecefc908c6 | -9.73547 | -48.96503 | 2025-09-02 03:51:00 | NPP-375D | DIVINÓPOLIS DO TOCANTINS | TOCANTINS | Brasil | 1707108 | 17 | 33 | nan | nan | nan | Cerrado | 1.5 |
| 6fa08fc7-5fa9-367f-b144-84e547b487a3 | -12.57612 | -48.25722 | 2025-09-02 03:51:00 | NPP-375D | PARANÃ | TOCANTINS | Brasil | 1716208 | 17 | 33 | nan | nan | nan | Cerrado | 2.5 |
| 0646067b-9430-3e54-9e02-5bccb7ce5ae1 | -11.00247 | -46.9383 | 2025-09-02 03:51:00 | NPP-375D | PONTE ALTA DO TOCANTINS | TOCANTINS | Brasil | 1717909 | 17 | 33 | nan | nan | nan | Cerrado | 0.6 |
| b9f375fd-560a-3ee5-afbc-ddce9f0fcb03 | -7.7907 | -45.45087 | 2025-09-02 03:51:00 | NPP-375D | RIBEIRO GONÇALVES | PIAUÍ | Brasil | 2208908 | 22 | 33 | nan | nan | nan | Cerrado | 1.3 |
| 35a1c477-9b2d-3757-995b-de16b7805879 | -8.46317 | -47.37478 | 2025-09-02 03:51:00 | NPP-375D | GOIATINS | TOCANTINS | Brasil | 1709005 | 17 | 33 | nan | nan | nan | Cerrado | 4.7 |
| b559296d-8916-34f1-a54d-07900893a4f6 | -10.58321 | -44.86241 | 2025-09-02 03:51:00 | NPP-375D | SEBASTIÃO BARROS | PIAUÍ | Brasil | 2210623 | 22 | 33 | nan | nan | nan | Cerrado | 1.3 |
| 2b9a3b29-66f4-3059-a959-f36f338b7f49 | -14.22064 | -48.05699 | 2025-09-02 03:51:00 | NPP-375D | NIQUELÂNDIA | GOIÁS | Brasil | 5214606 | 52 | 33 | nan | nan | nan | Cerrado | 1.1 |
| ab818364-1bf3-3a6d-9fef-47feacc83c0d | -11.66107 | -52.22234 | 2025-09-02 03:51:00 | NPP-375D | SÃO FÉLIX DO ARAGUAIA | MATO GROSSO | Brasil | 5107859 | 51 | 33 | nan | nan | nan | Amazônia | 31.6 |
| 9a2955da-be69-37af-b15d-1c7890f8dad2 | -12.88222 | -48.16477 | 2025-09-02 03:51:00 | NPP-375D | PARANÃ | TOCANTINS | Brasil | 1716208 | 17 | 33 | nan | nan | nan | Cerrado | 1.7 |
| 8c40cf57-8d7b-32f2-a625-2454a614c373 | -8.45973 | -47.36179 | 2025-09-02 03:51:00 | NPP-375D | GOIATINS | TOCANTINS | Brasil | 1709005 | 17 | 33 | nan | nan | nan | Cerrado | 1.8 |
| 74c3ce22-f647-346c-9083-c67e540d91d8 | -11.4347 | -46.81509 | 2025-09-02 03:51:00 | NPP-375D | RIO DA CONCEIÇÃO | TOCANTINS | Brasil | 1718659 | 17 | 33 | nan | nan | nan | Cerrado | 0.4 |
| edfe3e6a-c375-3dfb-826f-961682d83525 | -11.85847 | -46.71391 | 2025-09-02 03:51:00 | NPP-375D | NOVO JARDIM | TOCANTINS | Brasil | 1715259 | 17 | 33 | nan | nan | nan | Cerrado | 1.4 |
| 9254722a-661b-3f0a-9350-caf4d10803b3 | -13.32121 | -46.83235 | 2025-09-02 03:51:00 | NPP-375D | MONTE ALEGRE DE GOIÁS | GOIÁS | Brasil | 5213509 | 52 | 33 | nan | nan | nan | Cerrado | 1.1 |
| 89d0dd15-fb35-3d52-b7ec-ca895cc1e9c7 | -14.49018 | -45.95324 | 2025-09-02 03:51:00 | NPP-375D | JABORANDI | BAHIA | Brasil | 2917359 | 29 | 33 | nan | nan | nan | Cerrado | 1.5 |
| 2963005e-b78d-3e8c-9c3c-a2da9f466137 | -12.75166 | -44.41181 | 2025-09-02 03:51:00 | NPP-375D | BAIANÓPOLIS | BAHIA | Brasil | 2902500 | 29 | 33 | nan | nan | nan | Cerrado | 5.8 |
| 3ccd5332-177d-3aef-8732-ace05c540106 | -11.65469 | -44.86277 | 2025-09-02 03:51:00 | NPP-375D | RIACHÃO DAS NEVES | BAHIA | Brasil | 2926202 | 29 | 33 | nan | nan | nan | Cerrado | 1.7 |
| fe5e66f6-8085-33a0-9dd5-f36578b21241 | -13.5004 | -46.92804 | 2025-09-02 03:51:00 | NPP-375D | MONTE ALEGRE DE GOIÁS | GOIÁS | Brasil | 5213509 | 52 | 33 | nan | nan | nan | Cerrado | 1.0 |
| a76efd43-3154-3333-a868-beec792119af | -11.02343 | -46.85505 | 2025-09-02 03:51:00 | NPP-375D | MATEIROS | TOCANTINS | Brasil | 1712702 | 17 | 33 | nan | nan | nan | Cerrado | 1.6 |
| d2bf7bd5-cfa7-3a4b-8ac6-7238afdfe880 | -12.85942 | -48.05562 | 2025-09-02 03:51:00 | NPP-375D | PARANÃ | TOCANTINS | Brasil | 1716208 | 17 | 33 | nan | nan | nan | Cerrado | 2.9 |
| f24b9dc3-66d3-3c4f-a922-9f4a386ff3cc | -10.05116 | -48.12834 | 2025-09-02 03:51:00 | NPP-375D | APARECIDA DO RIO NEGRO | TOCANTINS | Brasil | 1701101 | 17 | 33 | nan | nan | nan | Cerrado | 3.5 |
| 0b4c11a4-dd5b-3801-b832-b8d6c64a2fc1 | -14.05604 | -44.55275 | 2025-09-02 03:51:00 | NPP-375D | COCOS | BAHIA | Brasil | 2908101 | 29 | 33 | nan | nan | nan | Cerrado | 1.3 |
| 39773c61-32da-3911-852d-ab110b983c4b | -11.05188 | -46.89975 | 2025-09-02 03:51:00 | NPP-375D | PONTE ALTA DO TOCANTINS | TOCANTINS | Brasil | 1717909 | 17 | 33 | nan | nan | nan | Cerrado | 1.0 |
| b773a75e-7def-3f1f-88b3-e6e18432234e | -11.96433 | -45.79445 | 2025-09-02 03:51:00 | NPP-375D | LUÍS EDUARDO MAGALHÃES | BAHIA | Brasil | 2919553 | 29 | 33 | nan | nan | nan | Cerrado | 1.1 |
| 7caf6b18-92c1-3dcc-b337-bd09fe1b1f28 | -11.90004 | -44.88478 | 2025-09-02 03:51:00 | NPP-375D | RIACHÃO DAS NEVES | BAHIA | Brasil | 2926202 | 29 | 33 | nan | nan | nan | Cerrado | 1.0 |
| a013efd0-1c86-36ad-8dec-215b0267f602 | -9.48169 | -46.51019 | 2025-09-02 03:51:00 | NPP-375D | ALTO PARNAÍBA | MARANHÃO | Brasil | 2100501 | 21 | 33 | nan | nan | nan | Cerrado | 0.6 |
| 0cd317a2-1074-3f92-a297-6aa321cc2c7a | -12.61692 | -48.18254 | 2025-09-02 03:51:00 | NPP-375D | PARANÃ | TOCANTINS | Brasil | 1716208 | 17 | 33 | nan | nan | nan | Cerrado | 13.0 |
| f5ceca53-f020-37e7-b0db-a21e9866860f | -12.78239 | -48.09739 | 2025-09-02 03:51:00 | NPP-375D | PARANÃ | TOCANTINS | Brasil | 1716208 | 17 | 33 | nan | nan | nan | Cerrado | 1.1 |
| 7c73a278-bf1e-3507-b7ac-c2195093f9a3 | -13.32608 | -46.83428 | 2025-09-02 03:51:00 | NPP-375D | MONTE ALEGRE DE GOIÁS | GOIÁS | Brasil | 5213509 | 52 | 33 | nan | nan | nan | Cerrado | 1.1 |
| fd6961b9-0ffc-3861-b839-a68694275797 | -8.46266 | -47.37255 | 2025-09-02 03:51:00 | NPP-375D | GOIATINS | TOCANTINS | Brasil | 1709005 | 17 | 33 | nan | nan | nan | Cerrado | 3.1 |
| d983e4b4-fc5e-3ca3-ae0e-9e24c2413850 | -13.53899 | -46.98646 | 2025-09-02 03:51:00 | NPP-375D | MONTE ALEGRE DE GOIÁS | GOIÁS | Brasil | 5213509 | 52 | 33 | nan | nan | nan | Cerrado | 4.2 |
| 27d64e6f-43f3-3f5e-a0f0-c193afb696c4 | -11.09829 | -44.64021 | 2025-09-02 03:51:00 | NPP-375D | SANTA RITA DE CÁSSIA | BAHIA | Brasil | 2928406 | 29 | 33 | nan | nan | nan | Cerrado | 54.5 |
| 2855cf4d-2ed3-37ff-b7d7-ac6eadb9d625 | -13.69863 | -46.93899 | 2025-09-02 03:51:00 | NPP-375D | NOVA ROMA | GOIÁS | Brasil | 5214903 | 52 | 33 | nan | nan | nan | Cerrado | 36.0 |
| bcd1f97c-454f-3447-85be-9992b6774fcb | -10.75582 | -49.57591 | 2025-09-02 03:51:00 | NPP-375D | LAGOA DA CONFUSÃO | TOCANTINS | Brasil | 1711902 | 17 | 33 | nan | nan | nan | Cerrado | 2.1 |
| 657a44e4-13ea-3674-b6fb-ed2c92505fb5 | -14.48648 | -45.94724 | 2025-09-02 03:51:00 | NPP-375D | JABORANDI | BAHIA | Brasil | 2917359 | 29 | 33 | nan | nan | nan | Cerrado | 2.5 |
| c681dd69-a2f7-3eb1-abf7-aac2eacb35a2 | -11.34168 | -43.67714 | 2025-09-02 03:51:00 | NPP-375D | BARRA | BAHIA | Brasil | 2902708 | 29 | 33 | nan | nan | nan | Cerrado | 3.4 |
| 4322cf7e-9782-3834-bddb-7bc23306ee5f | -11.81057 | -46.3991 | 2025-09-02 03:51:00 | NPP-375D | PONTE ALTA DO BOM JESUS | TOCANTINS | Brasil | 1717800 | 17 | 33 | nan | nan | nan | Cerrado | 1.4 |
| 11a4aed6-834c-3bba-a1b1-ef3b742953c5 | -10.05087 | -48.12192 | 2025-09-02 03:51:00 | NPP-375D | APARECIDA DO RIO NEGRO | TOCANTINS | Brasil | 1701101 | 17 | 33 | nan | nan | nan | Cerrado | 2.9 |
| 8655c994-fd44-321c-8b3d-36fcf2294bce | -14.59068 | -48.06084 | 2025-09-02 03:51:00 | NPP-375D | NIQUELÂNDIA | GOIÁS | Brasil | 5214606 | 52 | 33 | nan | nan | nan | Cerrado | 3.2 |
| 464eeaca-dcc2-3d53-adb2-8cf862f56cb4 | -13.68605 | -46.86811 | 2025-09-02 03:51:00 | NPP-375D | NOVA ROMA | GOIÁS | Brasil | 5214903 | 52 | 33 | nan | nan | nan | Cerrado | 0.7 |
| d4207849-1ac3-3380-9d62-328cd9720526 | -8.46392 | -47.3708 | 2025-09-02 03:51:00 | NPP-375D | GOIATINS | TOCANTINS | Brasil | 1709005 | 17 | 33 | nan | nan | nan | Cerrado | 2.2 |
| 7067238d-4859-3bb7-84d1-30357ee917b3 | -11.664 | -52.19965 | 2025-09-02 03:51:00 | NPP-375D | SÃO FÉLIX DO ARAGUAIA | MATO GROSSO | Brasil | 5107859 | 51 | 33 | nan | nan | nan | Amazônia | 30.6 |
| 2a3dc0f9-18c7-3b64-954e-d7f804b105fe | -7.57474 | -45.22868 | 2025-09-02 03:51:00 | NPP-375D | RIBEIRO GONÇALVES | PIAUÍ | Brasil | 2208908 | 22 | 33 | nan | nan | nan | Cerrado | 3.0 |
| 98ea5fa8-bebc-3c7b-9c16-ac4f7a0c06e7 | -11.66514 | -52.16887 | 2025-09-02 03:51:00 | NPP-375D | SÃO FÉLIX DO ARAGUAIA | MATO GROSSO | Brasil | 5107859 | 51 | 33 | nan | nan | nan | Amazônia | 11.2 |
| a220aac9-c152-363b-a1b4-5bf91d4e573c | -10.83913 | -47.44586 | 2025-09-02 03:51:00 | NPP-375D | PONTE ALTA DO TOCANTINS | TOCANTINS | Brasil | 1717909 | 17 | 33 | nan | nan | nan | Cerrado | 4.2 |
| 0b71df7a-820e-30b3-a3c0-28cdacd525e3 | -12.93753 | -48.08796 | 2025-09-02 03:51:00 | NPP-375D | PARANÃ | TOCANTINS | Brasil | 1716208 | 17 | 33 | nan | nan | nan | Cerrado | 2.2 |
| 1dbbc993-d5cb-302d-8e8e-487d8606b065 | -11.92301 | -50.61822 | 2025-09-02 03:51:00 | NPP-375D | FORMOSO DO ARAGUAIA | TOCANTINS | Brasil | 1708205 | 17 | 33 | nan | nan | nan | Cerrado | 1.3 |
| 309659bf-8402-3d21-8862-1edc94963039 | -14.05411 | -44.55074 | 2025-09-02 03:51:00 | NPP-375D | COCOS | BAHIA | Brasil | 2908101 | 29 | 33 | nan | nan | nan | Cerrado | 2.1 |
| 14a23dc6-e985-35c2-808e-e6bfa23ef94a | -13.69421 | -46.93472 | 2025-09-02 03:51:00 | NPP-375D | NOVA ROMA | GOIÁS | Brasil | 5214903 | 52 | 33 | nan | nan | nan | Cerrado | 36.0 |
| 57973dfd-05af-3ab2-8014-301a477d8fa2 | -14.60144 | -48.03511 | 2025-09-02 03:51:00 | NPP-375D | NIQUELÂNDIA | GOIÁS | Brasil | 5214606 | 52 | 33 | nan | nan | nan | Cerrado | 1.6 |
| fcfab9ef-2fe8-36e8-9d3e-465f52c9ab13 | -14.49213 | -45.94298 | 2025-09-02 03:51:00 | NPP-375D | JABORANDI | BAHIA | Brasil | 2917359 | 29 | 33 | nan | nan | nan | Cerrado | 1.9 |
| b96906de-cf4b-3593-92b6-f20a1e01db56 | -12.6233 | -48.17966 | 2025-09-02 03:51:00 | NPP-375D | PARANÃ | TOCANTINS | Brasil | 1716208 | 17 | 33 | nan | nan | nan | Cerrado | 7.5 |
| c5d88013-14f3-3ada-98a5-6eaa782979ab | -14.58149 | -48.06843 | 2025-09-02 03:51:00 | NPP-375D | NIQUELÂNDIA | GOIÁS | Brasil | 5214606 | 52 | 33 | nan | nan | nan | Cerrado | 5.0 |
| 4c0381e2-ead7-3cf4-b479-b65ed2361523 | -9.44056 | -48.86374 | 2025-09-02 03:51:00 | NPP-375D | DOIS IRMÃOS DO TOCANTINS | TOCANTINS | Brasil | 1707207 | 17 | 33 | nan | nan | nan | Cerrado | 1.7 |
| 12592a87-4cb2-322f-b269-61db7a784143 | -11.38185 | -43.59829 | 2025-09-02 03:51:00 | NPP-375D | BARRA | BAHIA | Brasil | 2902708 | 29 | 33 | nan | nan | nan | Cerrado | 2.0 |
| 71c8ca6b-91a9-38ac-99c9-66824b3cfa34 | -14.26522 | -45.25207 | 2025-09-02 03:51:00 | NPP-375D | COCOS | BAHIA | Brasil | 2908101 | 29 | 33 | nan | nan | nan | Cerrado | 3.4 |
| a7fe1dd7-bfe6-3044-a6ff-dca75568146d | -14.58382 | -48.06722 | 2025-09-02 03:51:00 | NPP-375D | NIQUELÂNDIA | GOIÁS | Brasil | 5214606 | 52 | 33 | nan | nan | nan | Cerrado | 19.5 |
| 92d598d3-f6dd-339b-a54d-7414e3ad356f | -11.6696 | -52.20871 | 2025-09-02 03:51:00 | NPP-375D | SÃO FÉLIX DO ARAGUAIA | MATO GROSSO | Brasil | 5107859 | 51 | 33 | nan | nan | nan | Amazônia | 32.6 |
| 31f98f39-3302-330b-af99-2fcab427e245 | -12.81359 | -48.0556 | 2025-09-02 03:51:00 | NPP-375D | PARANÃ | TOCANTINS | Brasil | 1716208 | 17 | 33 | nan | nan | nan | Cerrado | 2.6 |
| 5ced3cc5-3fab-3a62-bbf7-180d42be6e34 | -11.0274 | -46.85627 | 2025-09-02 03:51:00 | NPP-375D | MATEIROS | TOCANTINS | Brasil | 1712702 | 17 | 33 | nan | nan | nan | Cerrado | 2.7 |
| b64e2248-8808-358a-ba93-c2a26b9a8397 | -11.79354 | -46.40615 | 2025-09-02 03:51:00 | NPP-375D | PONTE ALTA DO BOM JESUS | TOCANTINS | Brasil | 1717800 | 17 | 33 | nan | nan | nan | Cerrado | 4.7 |
| 22b12be9-2fa9-36da-abf7-45924e873d7b | -7.70818 | -50.26328 | 2025-09-02 03:51:00 | NPP-375D | PAU D'ARCO | PARÁ | Brasil | 1505551 | 15 | 33 | nan | nan | nan | Amazônia | 3.7 |
| a16ab2e8-14f0-368f-8b73-2bd5d4648acd | -15.43567 | -43.31376 | 2025-09-02 03:51:00 | NPP-375D | JANAÚBA | MINAS GERAIS | Brasil | 3135100 | 31 | 33 | nan | nan | nan | Caatinga | 1.7 |
| 858ec697-6b15-3682-948f-db80b6745a61 | -13.46942 | -46.92495 | 2025-09-02 03:51:00 | NPP-375D | MONTE ALEGRE DE GOIÁS | GOIÁS | Brasil | 5213509 | 52 | 33 | nan | nan | nan | Cerrado | 0.9 |
| 8acb81fa-78bc-3cf7-9ffc-fb22058d118f | -7.94273 | -46.43361 | 2025-09-02 03:51:00 | NPP-375D | BALSAS | MARANHÃO | Brasil | 2101400 | 21 | 33 | nan | nan | nan | Cerrado | 1.4 |
| 7d0745e9-acfa-3724-909a-32b0d77dd32e | -10.83734 | -47.27814 | 2025-09-02 03:51:00 | NPP-375D | PONTE ALTA DO TOCANTINS | TOCANTINS | Brasil | 1717909 | 17 | 33 | nan | nan | nan | Cerrado | 1.7 |
| f95797c0-c889-36e7-bea1-cc3ecf173115 | -13.31065 | -46.83275 | 2025-09-02 03:51:00 | NPP-375D | MONTE ALEGRE DE GOIÁS | GOIÁS | Brasil | 5213509 | 52 | 33 | nan | nan | nan | Cerrado | 4.2 |
| b246566b-5602-3451-8d37-a7cc145a0912 | -7.55229 | -45.69997 | 2025-09-02 03:51:00 | NPP-375D | SAMBAÍBA | MARANHÃO | Brasil | 2109700 | 21 | 33 | nan | nan | nan | Cerrado | 2.6 |
| ab748b84-789c-3a05-8856-ee819ae0af94 | -14.58226 | -48.06448 | 2025-09-02 03:51:00 | NPP-375D | NIQUELÂNDIA | GOIÁS | Brasil | 5214606 | 52 | 33 | nan | nan | nan | Cerrado | 2.7 |
| 70662709-e504-3c18-8011-df80903738a2 | -13.5396 | -46.98333 | 2025-09-02 03:51:00 | NPP-375D | MONTE ALEGRE DE GOIÁS | GOIÁS | Brasil | 5213509 | 52 | 33 | nan | nan | nan | Cerrado | 1.7 |
| 6ec44809-81b7-3531-ac9d-978834f9a581 | -9.13032 | -46.05279 | 2025-09-02 03:51:00 | NPP-375D | ALTO PARNAÍBA | MARANHÃO | Brasil | 2100501 | 21 | 33 | nan | nan | nan | Cerrado | 2.3 |
| ebf735cf-7147-36d0-9e9c-8ad460925207 | -7.60621 | -46.03465 | 2025-09-02 03:51:00 | NPP-375D | BALSAS | MARANHÃO | Brasil | 2101400 | 21 | 33 | nan | nan | nan | Cerrado | 2.7 |
| ffb46e94-2d46-32b6-9c24-c785c92b19f4 | -15.78775 | -42.1329 | 2025-09-02 03:51:00 | NPP-375D | TAIOBEIRAS | MINAS GERAIS | Brasil | 3168002 | 31 | 33 | nan | nan | nan | Cerrado | 4.4 |
| 7b1acbb8-da39-3bf1-acf1-13259f7015ae | -11.02351 | -46.84811 | 2025-09-02 03:51:00 | NPP-375D | MATEIROS | TOCANTINS | Brasil | 1712702 | 17 | 33 | nan | nan | nan | Cerrado | 1.8 |
| 2a7707eb-68bc-3475-8c15-4a8bd1e40e08 | -13.3157 | -46.83372 | 2025-09-02 03:51:00 | NPP-375D | MONTE ALEGRE DE GOIÁS | GOIÁS | Brasil | 5213509 | 52 | 33 | nan | nan | nan | Cerrado | 1.1 |
| 3e0aae7c-03f0-3f07-ad29-38bfd391ae41 | -10.83938 | -45.04181 | 2025-09-02 03:51:00 | NPP-375D | CRISTALÂNDIA DO PIAUÍ | PIAUÍ | Brasil | 2203008 | 22 | 33 | nan | nan | nan | Cerrado | 2.1 |
| 58e9d512-abc9-339e-b014-c3b4a6b65750 | -11.66082 | -52.21482 | 2025-09-02 03:51:00 | NPP-375D | SÃO FÉLIX DO ARAGUAIA | MATO GROSSO | Brasil | 5107859 | 51 | 33 | nan | nan | nan | Amazônia | 36.2 |
| 21db92e1-7e81-342a-926e-b7b38ed4f485 | -13.69397 | -46.88116 | 2025-09-02 03:51:00 | NPP-375D | NOVA ROMA | GOIÁS | Brasil | 5214903 | 52 | 33 | nan | nan | nan | Cerrado | 2.8 |
| d6a3c686-2c9e-3e6e-9402-39beaae0bd35 | -11.02802 | -46.85976 | 2025-09-02 03:51:00 | NPP-375D | MATEIROS | TOCANTINS | Brasil | 1712702 | 17 | 33 | nan | nan | nan | Cerrado | 3.5 |
| 798bd58e-d6d9-3d72-8e35-199d1ea8b5e3 | -14.05101 | -44.55604 | 2025-09-02 03:51:00 | NPP-375D | COCOS | BAHIA | Brasil | 2908101 | 29 | 33 | nan | nan | nan | Cerrado | 1.4 |
| 046c270b-ad8e-33c7-ade1-45ca975bbc88 | -13.52781 | -41.84193 | 2025-09-02 03:51:00 | NPP-375D | RIO DE CONTAS | BAHIA | Brasil | 2926707 | 29 | 33 | nan | nan | nan | Caatinga | 1.4 |
| 31a33e81-0307-3b82-97de-d1595112fa5b | -11.10537 | -44.62684 | 2025-09-02 03:51:00 | NPP-375D | SANTA RITA DE CÁSSIA | BAHIA | Brasil | 2928406 | 29 | 33 | nan | nan | nan | Cerrado | 20.1 |
| f0fe6db9-e65b-3b7b-85bb-982d9473f64f | -13.89529 | -48.09589 | 2025-09-02 03:51:00 | NPP-375D | COLINAS DO SUL | GOIÁS | Brasil | 5205521 | 52 | 33 | nan | nan | nan | Cerrado | 1.4 |
| 8709e50c-c081-36d5-a8a1-0bd0e1925bef | -13.30932 | -46.8395 | 2025-09-02 03:51:00 | NPP-375D | MONTE ALEGRE DE GOIÁS | GOIÁS | Brasil | 5213509 | 52 | 33 | nan | nan | nan | Cerrado | 2.4 |
| 7a43ad6b-729c-32f1-b8ba-4da272149885 | -7.99216 | -44.04898 | 2025-09-02 03:51:00 | NPP-375D | SEBASTIÃO LEAL | PIAUÍ | Brasil | 2210631 | 22 | 33 | nan | nan | nan | Cerrado | 1.5 |
| 0f152a2e-9e47-3747-8fa7-8e1edfdfad0a | -10.26805 | -47.52727 | 2025-09-02 03:51:00 | NPP-375D | LAGOA DO TOCANTINS | TOCANTINS | Brasil | 1711951 | 17 | 33 | nan | nan | nan | Cerrado | 1.3 |
| 280f6739-0163-3f4a-b250-df38d0d3263b | -13.37433 | -46.93886 | 2025-09-02 03:51:00 | NPP-375D | MONTE ALEGRE DE GOIÁS | GOIÁS | Brasil | 5213509 | 52 | 33 | nan | nan | nan | Cerrado | 0.9 |
| 96cc000c-539e-3291-800e-456ca4b0a465 | -14.72715 | -46.75064 | 2025-09-02 03:51:00 | NPP-375D | FLORES DE GOIÁS | GOIÁS | Brasil | 5207907 | 52 | 33 | nan | nan | nan | Cerrado | 1.6 |
| a3e972e3-799b-3b29-8ddd-a5fc77b0c625 | -13.75992 | -43.77456 | 2025-09-02 03:51:00 | NPP-375D | CARINHANHA | BAHIA | Brasil | 2907103 | 29 | 33 | nan | nan | nan | Cerrado | 2.6 |
| db801bf8-add1-3184-9b32-6e0f0c4af73b | -12.64587 | -48.24155 | 2025-09-02 03:51:00 | NPP-375D | PARANÃ | TOCANTINS | Brasil | 1716208 | 17 | 33 | nan | nan | nan | Cerrado | 2.2 |
| 9a292f9f-e50b-395b-a4cb-f428b4b4eff3 | -11.97264 | -45.88596 | 2025-09-02 03:51:00 | NPP-375D | LUÍS EDUARDO MAGALHÃES | BAHIA | Brasil | 2919553 | 29 | 33 | nan | nan | nan | Cerrado | 3.7 |


[Clique aqui para ver as próximas entradas](README23.md)
