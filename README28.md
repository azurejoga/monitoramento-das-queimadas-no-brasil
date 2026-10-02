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

## Dados Diários - Página 28

| ID | Latitude | Longitude | Data/Hora GMT | Satélite | Município | Estado | País | Município ID | Estado ID | País ID | Dias sem Chuva | Precipitação | Risco de Fogo | Bioma | FRP |
|----|----------|-----------|---------------|----------|-----------|--------|------|--------------|-----------|---------|----------------|--------------|----------------|-------|-----|
| 0babf12f-927c-390e-9ec5-16203f4c0427 | -11.42255 | -43.39952 | 2026-10-02 03:55:00 | NPP-375D | BARRA | BAHIA | Brasil | 2902708 | 29 | 33 | nan | nan | nan | Cerrado | 2.4 |
| 9353ae46-f27f-3b59-b666-549d7a11b0b3 | -11.46386 | -43.42407 | 2026-10-02 03:55:00 | NPP-375D | BARRA | BAHIA | Brasil | 2902708 | 29 | 33 | nan | nan | nan | Cerrado | 4.0 |
| 209cfe30-4f2e-32dc-a7a1-184d8d6df38f | -12.99085 | -51.27769 | 2026-10-02 03:55:00 | NPP-375D | RIBEIRÃO CASCALHEIRA | MATO GROSSO | Brasil | 5107180 | 51 | 33 | nan | nan | nan | Cerrado | 11.9 |
| ebe354c1-5b42-34af-a375-7640b9387a31 | -9.84204 | -44.83994 | 2026-10-02 03:55:00 | NPP-375D | RIACHO FRIO | PIAUÍ | Brasil | 2208858 | 22 | 33 | nan | nan | nan | Cerrado | 0.9 |
| 31848fef-ee19-3714-91f6-364701352af2 | -7.5111 | -47.33835 | 2026-10-02 03:55:00 | NPP-375D | CAROLINA | MARANHÃO | Brasil | 2102804 | 21 | 33 | nan | nan | nan | Cerrado | 1.4 |
| 8664a024-38fa-3a00-ae41-1ede918488d7 | -11.64849 | -43.56896 | 2026-10-02 03:55:00 | NPP-375D | BARRA | BAHIA | Brasil | 2902708 | 29 | 33 | nan | nan | nan | Cerrado | 5.2 |
| bb105fe6-dc6b-3050-8a66-ab39936ded6c | -11.26406 | -43.51863 | 2026-10-02 03:55:00 | NPP-375D | BARRA | BAHIA | Brasil | 2902708 | 29 | 33 | nan | nan | nan | Cerrado | 2.0 |
| a55631c4-4b0d-3668-9b9a-e517f21cc319 | -11.46475 | -43.41923 | 2026-10-02 03:55:00 | NPP-375D | BARRA | BAHIA | Brasil | 2902708 | 29 | 33 | nan | nan | nan | Cerrado | 2.0 |
| 3be72b3a-778b-33dc-acd2-c8492b15b177 | -11.74083 | -43.44954 | 2026-10-02 03:55:00 | NPP-375D | BARRA | BAHIA | Brasil | 2902708 | 29 | 33 | nan | nan | nan | Cerrado | 1.6 |
| ac35ce77-3038-3ad5-b6f4-e39fc0212c17 | -11.7804 | -43.57133 | 2026-10-02 03:55:00 | NPP-375D | BARRA | BAHIA | Brasil | 2902708 | 29 | 33 | nan | nan | nan | Cerrado | 3.1 |
| 7d85fb7e-3909-3ec8-bb4d-ab70b3025b0f | -11.67189 | -43.59875 | 2026-10-02 03:55:00 | NPP-375D | BARRA | BAHIA | Brasil | 2902708 | 29 | 33 | nan | nan | nan | Cerrado | 15.7 |
| 0524c6bb-19f9-3d0c-849a-2268e85fc2cc | -11.23212 | -45.18176 | 2026-10-02 03:55:00 | NPP-375D | FORMOSA DO RIO PRETO | BAHIA | Brasil | 2911105 | 29 | 33 | nan | nan | nan | Cerrado | 1.0 |
| 0c173b89-fad0-3212-95ab-4fb68467dfa6 | -14.76787 | -40.32945 | 2026-10-02 03:55:00 | NPP-375D | PLANALTO | BAHIA | Brasil | 2925006 | 29 | 33 | nan | nan | nan | Mata Atlântica | 0.9 |
| a04b5b0b-2769-3fde-9130-c9fc377260f2 | -11.73145 | -43.42932 | 2026-10-02 03:55:00 | NPP-375D | BARRA | BAHIA | Brasil | 2902708 | 29 | 33 | nan | nan | nan | Cerrado | 2.7 |
| d063801e-c5d4-3ad5-a6a1-ba6246bcfe06 | -9.52053 | -45.32709 | 2026-10-02 03:55:00 | NPP-375D | GILBUÉS | PIAUÍ | Brasil | 2204402 | 22 | 33 | nan | nan | nan | Cerrado | 1.2 |
| ac8bef54-da74-37d1-a71a-4717ebaded27 | -10.52609 | -43.5027 | 2026-10-02 03:55:00 | NPP-375D | BURITIRAMA | BAHIA | Brasil | 2904753 | 29 | 33 | nan | nan | nan | Cerrado | 3.9 |
| d7b0ec70-d51c-31f8-b0bb-9259758a24b2 | -12.52906 | -43.10217 | 2026-10-02 03:55:00 | NPP-375D | PARATINGA | BAHIA | Brasil | 2923704 | 29 | 33 | nan | nan | nan | Caatinga | 1.9 |
| 3788cd54-3387-3be9-b74a-845c4ddf8378 | -9.84323 | -44.83344 | 2026-10-02 03:55:00 | NPP-375D | RIACHO FRIO | PIAUÍ | Brasil | 2208858 | 22 | 33 | nan | nan | nan | Cerrado | 1.4 |
| 5d5c1caa-b02e-3dc4-95d6-0d706017dd03 | -11.75554 | -43.4473 | 2026-10-02 03:55:00 | NPP-375D | BARRA | BAHIA | Brasil | 2902708 | 29 | 33 | nan | nan | nan | Cerrado | 1.9 |
| 08475f3a-bdcc-3346-8258-2a311caf6c6f | -11.13322 | -44.62131 | 2026-10-02 03:55:00 | NPP-375D | SANTA RITA DE CÁSSIA | BAHIA | Brasil | 2928406 | 29 | 33 | nan | nan | nan | Cerrado | 1.3 |
| b635fd59-1327-33c7-9ebe-64495c63d278 | -9.83858 | -44.82936 | 2026-10-02 03:55:00 | NPP-375D | RIACHO FRIO | PIAUÍ | Brasil | 2208858 | 22 | 33 | nan | nan | nan | Cerrado | 1.3 |
| aa537402-cc02-313c-9805-373a20d2a348 | -13.01235 | -51.28587 | 2026-10-02 03:55:00 | NPP-375D | RIBEIRÃO CASCALHEIRA | MATO GROSSO | Brasil | 5107180 | 51 | 33 | nan | nan | nan | Cerrado | 4.1 |
| a9912b1e-61ee-394b-b3bd-b8388487e980 | -10.90539 | -43.83986 | 2026-10-02 03:55:00 | NPP-375D | BARRA | BAHIA | Brasil | 2902708 | 29 | 33 | nan | nan | nan | Cerrado | 3.3 |
| f8edaf72-a3ba-3c91-86c4-dcf6213c4481 | -11.15449 | -44.61906 | 2026-10-02 03:55:00 | NPP-375D | SANTA RITA DE CÁSSIA | BAHIA | Brasil | 2928406 | 29 | 33 | nan | nan | nan | Cerrado | 133.6 |
| 8818ae4c-655f-335b-ad12-f283252ec9a0 | -11.66635 | -43.60272 | 2026-10-02 03:55:00 | NPP-375D | BARRA | BAHIA | Brasil | 2902708 | 29 | 33 | nan | nan | nan | Cerrado | 15.7 |
| 392fa32f-376f-3901-aa31-721379de768c | -13.85607 | -43.63499 | 2026-10-02 03:55:00 | NPP-375D | CARINHANHA | BAHIA | Brasil | 2907103 | 29 | 33 | nan | nan | nan | Cerrado | 1.3 |
| 8d8c7bca-adba-310f-bac2-8704ffec3263 | -15.25016 | -41.01311 | 2026-10-02 03:55:00 | NPP-375D | VITÓRIA DA CONQUISTA | BAHIA | Brasil | 2933307 | 29 | 33 | nan | nan | nan | Mata Atlântica | 0.7 |
| 392ae200-0c2d-3f52-84ca-8ddd0bf5ca15 | -14.34398 | -44.73465 | 2026-10-02 03:55:00 | NPP-375D | COCOS | BAHIA | Brasil | 2908101 | 29 | 33 | nan | nan | nan | Cerrado | 1.5 |
| 17b1926e-16fd-3c37-8173-6c5b0cb50fa0 | -12.54804 | -47.19973 | 2026-10-02 03:55:00 | NPP-375D | ARRAIAS | TOCANTINS | Brasil | 1702406 | 17 | 33 | nan | nan | nan | Cerrado | 3.2 |
| 0955d68f-6bab-3173-9e15-3372730db2c0 | -11.66547 | -43.60747 | 2026-10-02 03:55:00 | NPP-375D | BARRA | BAHIA | Brasil | 2902708 | 29 | 33 | nan | nan | nan | Cerrado | 13.2 |
| 7436cf02-ab74-3f88-a458-e6040aa211d1 | -11.65235 | -43.60019 | 2026-10-02 03:55:00 | NPP-375D | BARRA | BAHIA | Brasil | 2902708 | 29 | 33 | nan | nan | nan | Cerrado | 2.2 |
| 781e7706-34c0-3bea-a24b-d7184e9aa2cf | -13.86241 | -43.63403 | 2026-10-02 03:55:00 | NPP-375D | CARINHANHA | BAHIA | Brasil | 2907103 | 29 | 33 | nan | nan | nan | Cerrado | 3.1 |
| 3f0e1f0b-671f-32b8-b496-537022504ac3 | -11.64657 | -43.5534 | 2026-10-02 03:55:00 | NPP-375D | BARRA | BAHIA | Brasil | 2902708 | 29 | 33 | nan | nan | nan | Cerrado | 19.8 |
| ac9f75a9-537d-3f8e-82f4-04bfbba6e881 | -11.72972 | -43.43891 | 2026-10-02 03:55:00 | NPP-375D | BARRA | BAHIA | Brasil | 2902708 | 29 | 33 | nan | nan | nan | Cerrado | 1.9 |
| b8700ea3-5f5e-32c6-a92e-ba0f8c102b47 | -14.91123 | -39.27032 | 2026-10-02 03:55:00 | NPP-375D | ITABUNA | BAHIA | Brasil | 2914802 | 29 | 33 | nan | nan | nan | Mata Atlântica | 0.7 |
| b91d306b-b90d-3301-a0c5-eb2ac6eeb05a | -11.64759 | -43.57385 | 2026-10-02 03:55:00 | NPP-375D | BARRA | BAHIA | Brasil | 2902708 | 29 | 33 | nan | nan | nan | Cerrado | 7.2 |
| 0795054a-7dca-3843-81c8-c7c614c05b61 | -11.73712 | -43.44387 | 2026-10-02 03:55:00 | NPP-375D | BARRA | BAHIA | Brasil | 2902708 | 29 | 33 | nan | nan | nan | Cerrado | 2.4 |
| 5e6d4de6-3609-3546-b6ba-659b742899ad | -14.02881 | -41.59955 | 2026-10-02 03:55:00 | NPP-375D | BRUMADO | BAHIA | Brasil | 2904605 | 29 | 33 | nan | nan | nan | Caatinga | 2.1 |
| c94e2078-17ec-3364-b96a-c31df74b4e70 | -11.43886 | -43.40424 | 2026-10-02 03:55:00 | NPP-375D | BARRA | BAHIA | Brasil | 2902708 | 29 | 33 | nan | nan | nan | Cerrado | 2.4 |
| 45dd64ea-3b4b-3282-b608-d833710bf7ab | -11.44419 | -43.5308 | 2026-10-02 03:55:00 | NPP-375D | BARRA | BAHIA | Brasil | 2902708 | 29 | 33 | nan | nan | nan | Cerrado | 3.3 |
| ad05e7ee-b228-338f-8d23-af515b570e7c | -11.72798 | -43.44852 | 2026-10-02 03:55:00 | NPP-375D | BARRA | BAHIA | Brasil | 2902708 | 29 | 33 | nan | nan | nan | Cerrado | 1.9 |
| fee84e21-e24a-3fb8-8a2a-a50578ad803a | -11.70331 | -43.5979 | 2026-10-02 03:55:00 | NPP-375D | BARRA | BAHIA | Brasil | 2902708 | 29 | 33 | nan | nan | nan | Cerrado | 3.4 |
| 55423a03-c87a-3ed2-944c-25058aafb58e | -11.78671 | -43.56309 | 2026-10-02 03:55:00 | NPP-375D | BARRA | BAHIA | Brasil | 2902708 | 29 | 33 | nan | nan | nan | Cerrado | 3.1 |
| 0b279c41-2e7a-37ad-874e-2cc0cd30bbc9 | -11.70802 | -43.58541 | 2026-10-02 03:55:00 | NPP-375D | BARRA | BAHIA | Brasil | 2902708 | 29 | 33 | nan | nan | nan | Cerrado | 1.7 |
| ecc6d7d6-85a3-3077-b181-5d05a1b70e04 | -11.70981 | -43.58898 | 2026-10-02 03:55:00 | NPP-375D | BARRA | BAHIA | Brasil | 2902708 | 29 | 33 | nan | nan | nan | Cerrado | 1.7 |
| 0e97d9f6-c194-34cc-8323-cef3307e2d07 | -11.15394 | -44.62202 | 2026-10-02 03:55:00 | NPP-375D | SANTA RITA DE CÁSSIA | BAHIA | Brasil | 2928406 | 29 | 33 | nan | nan | nan | Cerrado | 133.6 |
| 9dab7b2e-e518-398e-b78d-bdfddd7695a0 | -11.1374 | -44.5991 | 2026-10-02 03:55:00 | NPP-375D | SANTA RITA DE CÁSSIA | BAHIA | Brasil | 2928406 | 29 | 33 | nan | nan | nan | Cerrado | 4.6 |
| a3855b77-6f7b-3489-8766-fffdc9aa67cc | -11.24879 | -45.20786 | 2026-10-02 03:55:00 | NPP-375D | FORMOSA DO RIO PRETO | BAHIA | Brasil | 2911105 | 29 | 33 | nan | nan | nan | Cerrado | 1.0 |
| fe44872b-c8a3-34ab-b5f1-f5fdc4f31d96 | -11.13378 | -44.61832 | 2026-10-02 03:55:00 | NPP-375D | SANTA RITA DE CÁSSIA | BAHIA | Brasil | 2928406 | 29 | 33 | nan | nan | nan | Cerrado | 0.9 |
| cdf1670a-b18a-3ba2-be53-cee93a25590a | -11.46954 | -43.44518 | 2026-10-02 03:55:00 | NPP-375D | BARRA | BAHIA | Brasil | 2902708 | 29 | 33 | nan | nan | nan | Cerrado | 1.2 |
| ce6111e2-9f82-3886-a176-e119e3a20165 | -13.14955 | -51.22056 | 2026-10-02 03:55:00 | NPP-375D | RIBEIRÃO CASCALHEIRA | MATO GROSSO | Brasil | 5107180 | 51 | 33 | nan | nan | nan | Cerrado | 3.4 |
| 9bfedcec-ed81-3e34-be74-15c5ef47ebc8 | -11.70161 | -43.59424 | 2026-10-02 03:55:00 | NPP-375D | BARRA | BAHIA | Brasil | 2902708 | 29 | 33 | nan | nan | nan | Cerrado | 1.8 |
| b17d08c2-81e7-38de-963a-32c640d4f9ab | -13.40498 | -44.0111 | 2026-10-02 03:55:00 | NPP-375D | SÃO FÉLIX DO CORIBE | BAHIA | Brasil | 2929057 | 29 | 33 | nan | nan | nan | Cerrado | 3.8 |
| 9128742c-abe0-3d57-b0d3-82158a43fb56 | -11.45181 | -43.41169 | 2026-10-02 03:55:00 | NPP-375D | BARRA | BAHIA | Brasil | 2902708 | 29 | 33 | nan | nan | nan | Cerrado | 2.2 |
| 4cc1984d-a53d-39b6-9c9a-30da1df96d46 | -13.34763 | -43.86658 | 2026-10-02 03:55:00 | NPP-375D | SERRA DO RAMALHO | BAHIA | Brasil | 2930154 | 29 | 33 | nan | nan | nan | Cerrado | 5.6 |
| 3aafbb24-e7c4-39ac-86f8-f8cdc5e20cfe | -11.65121 | -43.55431 | 2026-10-02 03:55:00 | NPP-375D | BARRA | BAHIA | Brasil | 2902708 | 29 | 33 | nan | nan | nan | Cerrado | 19.8 |
| 06e37667-a9cb-3608-823e-0fb410f3a4c4 | -11.52227 | -43.51242 | 2026-10-02 03:55:00 | NPP-375D | BARRA | BAHIA | Brasil | 2902708 | 29 | 33 | nan | nan | nan | Cerrado | 7.1 |
| 4b6914e3-88e6-3c08-9f7f-df062a6f6055 | -12.51858 | -43.10927 | 2026-10-02 03:55:00 | NPP-375D | PARATINGA | BAHIA | Brasil | 2923704 | 29 | 33 | nan | nan | nan | Caatinga | 1.7 |
| f5f1e04e-db5a-31b3-9eb1-0f7ebcfe922a | -11.65145 | -43.60507 | 2026-10-02 03:55:00 | NPP-375D | BARRA | BAHIA | Brasil | 2902708 | 29 | 33 | nan | nan | nan | Cerrado | 3.0 |
| 3b112197-e6a7-3c5e-bb52-fe019b20e380 | -12.52543 | -43.09688 | 2026-10-02 03:55:00 | NPP-375D | PARATINGA | BAHIA | Brasil | 2923704 | 29 | 33 | nan | nan | nan | Caatinga | 1.9 |
| ea328465-8ed4-308a-9c51-0144da59f523 | -11.47328 | -43.4509 | 2026-10-02 03:55:00 | NPP-375D | BARRA | BAHIA | Brasil | 2902708 | 29 | 33 | nan | nan | nan | Cerrado | 1.2 |
| 5fec1cad-0952-31f7-b31b-4c1a3df28bf0 | -11.75915 | -43.58237 | 2026-10-02 03:55:00 | NPP-375D | BARRA | BAHIA | Brasil | 2902708 | 29 | 33 | nan | nan | nan | Cerrado | 12.1 |
| a693d7fa-0640-3ed5-bf96-ab7dd1c12bba | -11.16341 | -44.6271 | 2026-10-02 03:55:00 | NPP-375D | SANTA RITA DE CÁSSIA | BAHIA | Brasil | 2928406 | 29 | 33 | nan | nan | nan | Cerrado | 2.3 |
| 41797245-68e2-397a-86b7-5215aa2f6181 | -11.47309 | -43.42583 | 2026-10-02 03:55:00 | NPP-375D | BARRA | BAHIA | Brasil | 2902708 | 29 | 33 | nan | nan | nan | Cerrado | 3.8 |
| 5f01597c-aae9-36a4-b2bb-f0f232a72a03 | -11.66347 | -43.59213 | 2026-10-02 03:55:00 | NPP-375D | BARRA | BAHIA | Brasil | 2902708 | 29 | 33 | nan | nan | nan | Cerrado | 7.1 |
| 4eee461c-d230-3ff9-af68-546018b5f315 | -11.68886 | -43.61141 | 2026-10-02 03:55:00 | NPP-375D | BARRA | BAHIA | Brasil | 2902708 | 29 | 33 | nan | nan | nan | Cerrado | 7.0 |
| cb72477e-279a-3e66-a0ad-e26bcb7098b4 | -10.30586 | -44.63008 | 2026-10-02 03:55:00 | NPP-375D | PARNAGUÁ | PIAUÍ | Brasil | 2207603 | 22 | 33 | nan | nan | nan | Cerrado | 0.5 |
| 63737bb7-6a6b-3345-8234-6f51343574bb | -11.68588 | -43.6013 | 2026-10-02 03:55:00 | NPP-375D | BARRA | BAHIA | Brasil | 2902708 | 29 | 33 | nan | nan | nan | Cerrado | 3.6 |
| 1470b1c6-d091-304f-87e8-a10204456ac6 | -11.7569 | -43.54275 | 2026-10-02 03:55:00 | NPP-375D | BARRA | BAHIA | Brasil | 2902708 | 29 | 33 | nan | nan | nan | Cerrado | 1.7 |
| c81794d4-79e7-387f-be52-ae32089ea6d1 | -10.30417 | -44.63926 | 2026-10-02 03:55:00 | NPP-375D | PARNAGUÁ | PIAUÍ | Brasil | 2207603 | 22 | 33 | nan | nan | nan | Cerrado | 2.2 |
| 71cb6434-5fbc-3679-9add-7357d6d055e7 | -11.46103 | -43.41347 | 2026-10-02 03:55:00 | NPP-375D | BARRA | BAHIA | Brasil | 2902708 | 29 | 33 | nan | nan | nan | Cerrado | 1.9 |
| e447ba99-a8c8-341f-9e59-94b663a2b8e8 | -11.65612 | -43.60588 | 2026-10-02 03:55:00 | NPP-375D | BARRA | BAHIA | Brasil | 2902708 | 29 | 33 | nan | nan | nan | Cerrado | 70.9 |
| 293a91d8-05b8-3957-9559-417cf11928cd | -8.96752 | -46.82365 | 2026-10-02 03:55:00 | NPP-375D | BALSAS | MARANHÃO | Brasil | 2101400 | 21 | 33 | nan | nan | nan | Cerrado | 0.9 |
| 053b1696-df1e-3c6e-853b-bf6935f23d51 | -13.39678 | -46.81971 | 2026-10-02 03:55:00 | NPP-375D | MONTE ALEGRE DE GOIÁS | GOIÁS | Brasil | 5213509 | 52 | 33 | nan | nan | nan | Cerrado | 2.1 |
| ee60d598-be07-3513-9765-54b7e4b4073b | -13.14111 | -40.87651 | 2026-10-02 03:55:00 | NPP-375D | ITAETÉ | BAHIA | Brasil | 2915007 | 29 | 33 | nan | nan | nan | Caatinga | 2.6 |
| c2f2b403-1a6a-3c22-a0d5-8cf3a8141b91 | -12.97872 | -51.29872 | 2026-10-02 03:55:00 | NPP-375D | RIBEIRÃO CASCALHEIRA | MATO GROSSO | Brasil | 5107180 | 51 | 33 | nan | nan | nan | Cerrado | 4.6 |
| 1acbfbb5-adbd-3fb2-9565-4c98c95cf1a8 | -14.33333 | -44.7383 | 2026-10-02 03:55:00 | NPP-375D | COCOS | BAHIA | Brasil | 2908101 | 29 | 33 | nan | nan | nan | Cerrado | 4.8 |
| 124c2f81-111f-3009-8623-4583800ec00f | -11.73201 | -43.57323 | 2026-10-02 03:55:00 | NPP-375D | BARRA | BAHIA | Brasil | 2902708 | 29 | 33 | nan | nan | nan | Cerrado | 26.5 |
| 29004606-f34e-37f7-a4cf-31fb2f78802b | -12.98896 | -51.2883 | 2026-10-02 03:55:00 | NPP-375D | RIBEIRÃO CASCALHEIRA | MATO GROSSO | Brasil | 5107180 | 51 | 33 | nan | nan | nan | Cerrado | 11.3 |
| 92e3544b-cbde-3a0f-b7a2-805724941f27 | -11.69592 | -43.61151 | 2026-10-02 03:55:00 | NPP-375D | BARRA | BAHIA | Brasil | 2902708 | 29 | 33 | nan | nan | nan | Cerrado | 2.6 |
| 74834963-565d-3861-b915-9d28a2791836 | -11.26912 | -43.57069 | 2026-10-02 03:55:00 | NPP-375D | BARRA | BAHIA | Brasil | 2902708 | 29 | 33 | nan | nan | nan | Cerrado | 1.3 |
| 8e90a2b4-d55b-336b-b477-3a650e3dec1b | -10.26028 | -36.54369 | 2026-10-02 03:55:00 | NPP-375D | PENEDO | ALAGOAS | Brasil | 2706703 | 27 | 33 | nan | nan | nan | Mata Atlântica | 3.3 |
| d570ca07-eb67-35de-a01f-aafc0e8d5a50 | -13.85617 | -43.64228 | 2026-10-02 03:55:00 | NPP-375D | CARINHANHA | BAHIA | Brasil | 2907103 | 29 | 33 | nan | nan | nan | Cerrado | 2.5 |
| c8d3d2cf-49a3-30a3-898b-96b4c7d4536d | -8.38649 | -46.29215 | 2026-10-02 03:55:00 | NPP-375D | BALSAS | MARANHÃO | Brasil | 2101400 | 21 | 33 | nan | nan | nan | Cerrado | 1.9 |
| e7cf1f1b-086f-337e-a890-6a710eaeeb58 | -11.26443 | -43.56984 | 2026-10-02 03:55:00 | NPP-375D | BARRA | BAHIA | Brasil | 2902708 | 29 | 33 | nan | nan | nan | Cerrado | 1.2 |
| 1dbebfe3-7aaa-3075-aeb0-b5f27f8bef30 | -12.54477 | -46.7969 | 2026-10-02 03:55:00 | NPP-375D | ARRAIAS | TOCANTINS | Brasil | 1702406 | 17 | 33 | nan | nan | nan | Cerrado | 0.6 |
| 6d0ec487-802c-35eb-b389-8a9d7aca0c09 | -11.77739 | -43.56163 | 2026-10-02 03:55:00 | NPP-375D | BARRA | BAHIA | Brasil | 2902708 | 29 | 33 | nan | nan | nan | Cerrado | 1.9 |
| 0df96832-23b8-3399-bf2f-e54204b5e303 | -13.86515 | -43.64405 | 2026-10-02 03:55:00 | NPP-375D | CARINHANHA | BAHIA | Brasil | 2907103 | 29 | 33 | nan | nan | nan | Cerrado | 9.4 |
| d242e553-14b0-322f-839f-1c7657ea2c98 | -10.56455 | -50.07525 | 2026-10-02 03:55:00 | NPP-375D | PIUM | TOCANTINS | Brasil | 1717503 | 17 | 33 | nan | nan | nan | Cerrado | 1.5 |
| 37b62ffa-30e6-3cd2-a5da-af90d0e8873e | -13.39604 | -46.82335 | 2026-10-02 03:55:00 | NPP-375D | MONTE ALEGRE DE GOIÁS | GOIÁS | Brasil | 5213509 | 52 | 33 | nan | nan | nan | Cerrado | 2.9 |
| bfc4fb9b-81da-3daf-b409-e304562877f7 | -11.13994 | -44.61331 | 2026-10-02 03:55:00 | NPP-375D | SANTA RITA DE CÁSSIA | BAHIA | Brasil | 2928406 | 29 | 33 | nan | nan | nan | Cerrado | 1.3 |
| 108883be-9056-30e1-a7cd-9e45673586a6 | -12.85815 | -43.81032 | 2026-10-02 03:55:00 | NPP-375D | SERRA DOURADA | BAHIA | Brasil | 2930303 | 29 | 33 | nan | nan | nan | Cerrado | 5.9 |
| ac1f4aa5-a0d6-3cc2-9d68-752b31e26c1e | -11.43425 | -43.40337 | 2026-10-02 03:55:00 | NPP-375D | BARRA | BAHIA | Brasil | 2902708 | 29 | 33 | nan | nan | nan | Cerrado | 6.0 |
| 82901b45-2bdf-3e6e-8340-545794a94870 | -11.66258 | -43.59701 | 2026-10-02 03:55:00 | NPP-375D | BARRA | BAHIA | Brasil | 2902708 | 29 | 33 | nan | nan | nan | Cerrado | 90.2 |
| 0da2a384-c38a-3a80-8a89-5ce56c0658d1 | -11.47132 | -43.4355 | 2026-10-02 03:55:00 | NPP-375D | BARRA | BAHIA | Brasil | 2902708 | 29 | 33 | nan | nan | nan | Cerrado | 7.4 |
| 304ad12b-ef96-3967-8a66-208fc51085bd | -11.15558 | -44.61319 | 2026-10-02 03:55:00 | NPP-375D | SANTA RITA DE CÁSSIA | BAHIA | Brasil | 2928406 | 29 | 33 | nan | nan | nan | Cerrado | 132.0 |
| fcf6b1f5-3336-3fae-90f2-7fba6c6d67a5 | -13.34487 | -43.85583 | 2026-10-02 03:55:00 | NPP-375D | SERRA DO RAMALHO | BAHIA | Brasil | 2930154 | 29 | 33 | nan | nan | nan | Cerrado | 2.3 |
| 278e9c94-f6c0-32e0-9489-500204deec9e | -11.69525 | -43.60274 | 2026-10-02 03:55:00 | NPP-375D | BARRA | BAHIA | Brasil | 2902708 | 29 | 33 | nan | nan | nan | Cerrado | 5.8 |
| 46be7f72-02a7-3c0a-920e-e67ec924e623 | -11.24992 | -45.23043 | 2026-10-02 03:55:00 | NPP-375D | FORMOSA DO RIO PRETO | BAHIA | Brasil | 2911105 | 29 | 33 | nan | nan | nan | Cerrado | 2.9 |
| 36579c2b-cc4d-37b3-80af-9b07f298084c | -8.96064 | -46.8271 | 2026-10-02 03:55:00 | NPP-375D | BALSAS | MARANHÃO | Brasil | 2101400 | 21 | 33 | nan | nan | nan | Cerrado | 1.1 |


[Clique aqui para ver as próximas entradas](README29.md)
