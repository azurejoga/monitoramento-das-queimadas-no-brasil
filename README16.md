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

## Dados Diários - Página 16

| ID | Latitude | Longitude | Data/Hora GMT | Satélite | Município | Estado | País | Município ID | Estado ID | País ID | Dias sem Chuva | Precipitação | Risco de Fogo | Bioma | FRP |
|----|----------|-----------|---------------|----------|-----------|--------|------|--------------|-----------|---------|----------------|--------------|----------------|-------|-----|
| 1f83caa1-6f20-357f-9dbd-7ebb01de01f0 | -8.36268 | -37.59917 | 2025-10-16 03:28:00 | NPP-375D | SERTÂNIA | PERNAMBUCO | Brasil | 2614105 | 26 | 33 | nan | nan | nan | Caatinga | 0.7 |
| 367f450b-fbbf-3f16-8c6b-ba305b6aa79b | -8.18532 | -43.31927 | 2025-10-16 03:28:00 | NPP-375D | CANTO DO BURITI | PIAUÍ | Brasil | 2202307 | 22 | 33 | nan | nan | nan | Caatinga | 6.4 |
| 02678657-4882-3016-93a0-4c6d18bd168d | -11.43162 | -44.13703 | 2025-10-16 03:28:00 | NPP-375D | MANSIDÃO | BAHIA | Brasil | 2920452 | 29 | 33 | nan | nan | nan | Cerrado | 1.6 |
| 9418c4af-4a9a-3abd-9d17-52aac4451ee4 | -7.94592 | -44.14748 | 2025-10-16 03:28:00 | NPP-375D | SEBASTIÃO LEAL | PIAUÍ | Brasil | 2210631 | 22 | 33 | nan | nan | nan | Cerrado | 9.8 |
| 926cf928-9a76-3b55-85df-1ab755466e42 | -8.29377 | -43.42706 | 2025-10-16 03:28:00 | NPP-375D | CANTO DO BURITI | PIAUÍ | Brasil | 2202307 | 22 | 33 | nan | nan | nan | Caatinga | 1.7 |
| ecd56a16-1947-3a55-affb-0b5a6ba3600f | -10.52548 | -44.51184 | 2025-10-16 03:28:00 | NPP-375D | PARNAGUÁ | PIAUÍ | Brasil | 2207603 | 22 | 33 | nan | nan | nan | Cerrado | 1.7 |
| 1b15d076-5d87-39f3-8aa1-b6e6911b0856 | -10.12817 | -44.57219 | 2025-10-16 03:28:00 | NPP-375D | PARNAGUÁ | PIAUÍ | Brasil | 2207603 | 22 | 33 | nan | nan | nan | Cerrado | 2.6 |
| 5b2b62c4-2e9c-343e-acc1-724af0eb0893 | -8.46272 | -44.18771 | 2025-10-16 03:28:00 | NPP-375D | ALVORADA DO GURGUÉIA | PIAUÍ | Brasil | 2200459 | 22 | 33 | nan | nan | nan | Cerrado | 13.6 |
| 4f802e1c-f30d-3876-8966-4f5d87ee0c64 | -8.45723 | -44.17958 | 2025-10-16 03:28:00 | NPP-375D | ALVORADA DO GURGUÉIA | PIAUÍ | Brasil | 2200459 | 22 | 33 | nan | nan | nan | Cerrado | 13.6 |
| c0122ab6-8a15-3a87-9f1a-af44b90d2ef0 | -13.90371 | -45.57867 | 2025-10-16 03:28:00 | NPP-375D | JABORANDI | BAHIA | Brasil | 2917359 | 29 | 33 | nan | nan | nan | Cerrado | 4.0 |
| c5cf180f-1c4b-32b5-b596-7be0b049173c | -12.6704 | -43.43927 | 2025-10-16 03:28:00 | NPP-375D | SÍTIO DO MATO | BAHIA | Brasil | 2930758 | 29 | 33 | nan | nan | nan | Cerrado | 15.7 |
| ef30391c-9164-376b-a2b7-3e16da204ed5 | -10.52375 | -43.36908 | 2025-10-16 03:28:00 | NPP-375D | BARRA | BAHIA | Brasil | 2902708 | 29 | 33 | nan | nan | nan | Cerrado | 3.7 |
| 43544d86-753e-300c-a3e6-7b0445bcfc07 | -9.1534 | -41.0586 | 2025-10-16 03:28:00 | NPP-375D | CASA NOVA | BAHIA | Brasil | 2907202 | 29 | 33 | nan | nan | nan | Caatinga | 5.9 |
| ac604faa-8704-32a7-9aec-d81d128bea68 | -8.19186 | -43.32049 | 2025-10-16 03:28:00 | NPP-375D | CANTO DO BURITI | PIAUÍ | Brasil | 2202307 | 22 | 33 | nan | nan | nan | Caatinga | 6.4 |
| d65d46e0-45fc-3d78-b824-a3564d9b0ac7 | -11.58412 | -44.08406 | 2025-10-16 03:28:00 | NPP-375D | WANDERLEY | BAHIA | Brasil | 2933455 | 29 | 33 | nan | nan | nan | Cerrado | 8.2 |
| f0642399-0ae8-3f27-be8a-a116d0448fc5 | -7.94711 | -44.14112 | 2025-10-16 03:28:00 | NPP-375D | SEBASTIÃO LEAL | PIAUÍ | Brasil | 2210631 | 22 | 33 | nan | nan | nan | Cerrado | 9.8 |
| f753199b-0b89-3085-acea-9fb9252ef470 | -13.96117 | -41.7226 | 2025-10-16 03:28:00 | NPP-375D | DOM BASÍLIO | BAHIA | Brasil | 2910107 | 29 | 33 | nan | nan | nan | Caatinga | 1.5 |
| 03fea85a-f6af-3a52-84f3-ccc958c5aaac | -7.34729 | -43.86656 | 2025-10-16 03:28:00 | NPP-375D | LANDRI SALES | PIAUÍ | Brasil | 2205607 | 22 | 33 | nan | nan | nan | Cerrado | 10.6 |
| 2d7eee5c-b8c8-3684-922a-da7f6f33d137 | -12.67138 | -43.43453 | 2025-10-16 03:28:00 | NPP-375D | SÍTIO DO MATO | BAHIA | Brasil | 2930758 | 29 | 33 | nan | nan | nan | Cerrado | 15.3 |
| a18eeaf0-e9ad-30c0-b42e-cc9071f1f175 | -14.07493 | -44.27954 | 2025-10-16 03:28:00 | NPP-375D | FEIRA DA MATA | BAHIA | Brasil | 2910776 | 29 | 33 | nan | nan | nan | Cerrado | 3.8 |
| d954f7cc-6f8b-35bc-bd5b-e7b124f3f9d7 | -8.25892 | -43.43134 | 2025-10-16 03:28:00 | NPP-375D | CANTO DO BURITI | PIAUÍ | Brasil | 2202307 | 22 | 33 | nan | nan | nan | Caatinga | 1.3 |
| 0291bf23-d3a6-34b6-9860-8fbd9ef0dfa4 | -8.20033 | -43.32245 | 2025-10-16 03:28:00 | NPP-375D | CANTO DO BURITI | PIAUÍ | Brasil | 2202307 | 22 | 33 | nan | nan | nan | Caatinga | 13.8 |
| 92a65ac0-d9af-393b-a40d-41a38e27b37f | -9.67966 | -44.50303 | 2025-10-16 03:28:00 | NPP-375D | REDENÇÃO DO GURGUÉIA | PIAUÍ | Brasil | 2208700 | 22 | 33 | nan | nan | nan | Cerrado | 14.4 |
| c8a301d8-d5d2-3a73-a65e-e58dc3583f39 | -10.65694 | -45.24963 | 2025-10-16 03:28:00 | NPP-375D | CRISTALÂNDIA DO PIAUÍ | PIAUÍ | Brasil | 2203008 | 22 | 33 | nan | nan | nan | Cerrado | 7.7 |
| b3927ce9-ff1b-39dc-904d-66d1eccb15f1 | -10.50843 | -43.3703 | 2025-10-16 03:28:00 | NPP-375D | BARRA | BAHIA | Brasil | 2902708 | 29 | 33 | nan | nan | nan | Cerrado | 1.9 |
| 6ed6b50a-b2ba-3609-9e93-a8f4628820a6 | -9.15831 | -41.06345 | 2025-10-16 03:28:00 | NPP-375D | CASA NOVA | BAHIA | Brasil | 2907202 | 29 | 33 | nan | nan | nan | Caatinga | 5.9 |
| 03fcf5c8-06b9-3a93-a8e9-6fa1d4b1b698 | -8.20798 | -43.31772 | 2025-10-16 03:28:00 | NPP-375D | CANTO DO BURITI | PIAUÍ | Brasil | 2202307 | 22 | 33 | nan | nan | nan | Caatinga | 6.9 |
| c4d59e3a-8f39-39e8-b9ef-532b884f4542 | -11.5863 | -44.07308 | 2025-10-16 03:28:00 | NPP-375D | WANDERLEY | BAHIA | Brasil | 2933455 | 29 | 33 | nan | nan | nan | Cerrado | 3.1 |
| b4bae2c6-2f41-386d-b7c6-c247320ef1ce | -10.81145 | -44.00316 | 2025-10-16 03:28:00 | NPP-375D | MANSIDÃO | BAHIA | Brasil | 2920452 | 29 | 33 | nan | nan | nan | Cerrado | 2.0 |
| fc4db4ba-13cb-3c56-afa2-32cd89c149e4 | -7.94969 | -43.27015 | 2025-10-16 03:28:00 | NPP-375D | PAVUSSU | PIAUÍ | Brasil | 2207850 | 22 | 33 | nan | nan | nan | Caatinga | 6.5 |
| 5ccdd898-54ac-3a17-a049-a83e17612e47 | -7.33915 | -43.87197 | 2025-10-16 03:28:00 | NPP-375D | LANDRI SALES | PIAUÍ | Brasil | 2205607 | 22 | 33 | nan | nan | nan | Cerrado | 3.8 |
| 853cc062-3411-3bc0-bf34-689b6b17ea8f | -8.26445 | -43.43813 | 2025-10-16 03:28:00 | NPP-375D | CANTO DO BURITI | PIAUÍ | Brasil | 2202307 | 22 | 33 | nan | nan | nan | Cerrado | 1.3 |
| 6efb1792-568a-3f2e-bad8-5aa351966828 | -11.59237 | -44.0756 | 2025-10-16 03:28:00 | NPP-375D | WANDERLEY | BAHIA | Brasil | 2933455 | 29 | 33 | nan | nan | nan | Cerrado | 1.2 |
| 4bbe3107-e10a-3190-9a79-31b05ae83eca | -12.67113 | -43.43923 | 2025-10-16 03:28:00 | NPP-375D | SÍTIO DO MATO | BAHIA | Brasil | 2930758 | 29 | 33 | nan | nan | nan | Cerrado | 12.3 |
| e089d48c-47b8-382e-925e-8d4f376a7952 | -10.61859 | -42.31214 | 2025-10-16 03:28:00 | NPP-375D | ITAGUAÇU DA BAHIA | BAHIA | Brasil | 2915353 | 29 | 33 | nan | nan | nan | Caatinga | 1.1 |
| 55a66bd6-244b-3ada-92d9-42cdd42aa2af | -10.65141 | -45.24119 | 2025-10-16 03:28:00 | NPP-375D | CRISTALÂNDIA DO PIAUÍ | PIAUÍ | Brasil | 2203008 | 22 | 33 | nan | nan | nan | Cerrado | 7.7 |
| beb63672-1b39-3202-98c8-a86d0f56ddbb | -8.29438 | -43.41417 | 2025-10-16 03:28:00 | NPP-375D | CANTO DO BURITI | PIAUÍ | Brasil | 2202307 | 22 | 33 | nan | nan | nan | Caatinga | 1.4 |
| 7e4042fc-e718-3dc8-bb4c-70bb03b9a793 | -8.28994 | -43.40202 | 2025-10-16 03:28:00 | NPP-375D | CANTO DO BURITI | PIAUÍ | Brasil | 2202307 | 22 | 33 | nan | nan | nan | Caatinga | 1.5 |
| 981a3771-0471-3ab7-b875-264c122d4443 | -8.2704 | -43.36296 | 2025-10-16 03:28:00 | NPP-375D | CANTO DO BURITI | PIAUÍ | Brasil | 2202307 | 22 | 33 | nan | nan | nan | Caatinga | 3.0 |
| 07893b3b-354c-3d38-ad64-23b48991105b | -10.65102 | -45.25537 | 2025-10-16 03:28:00 | NPP-375D | CRISTALÂNDIA DO PIAUÍ | PIAUÍ | Brasil | 2203008 | 22 | 33 | nan | nan | nan | Cerrado | 10.9 |
| d70c7252-0117-34d4-be6a-11b4410eaccd | -8.48522 | -36.69818 | 2025-10-16 03:28:00 | NPP-375D | ALAGOINHA | PERNAMBUCO | Brasil | 2600609 | 26 | 33 | nan | nan | nan | Caatinga | 1.3 |
| 01c1aa63-f3cf-375a-983a-2c2e83dd7caa | -8.46147 | -44.19595 | 2025-10-16 03:28:00 | NPP-375D | ALVORADA DO GURGUÉIA | PIAUÍ | Brasil | 2200459 | 22 | 33 | nan | nan | nan | Cerrado | 14.7 |
| de936e06-54ff-3f11-b760-69f4b8333b6f | -8.25272 | -44.09966 | 2025-10-16 03:28:00 | NPP-375D | MANOEL EMÍDIO | PIAUÍ | Brasil | 2205904 | 22 | 33 | nan | nan | nan | Cerrado | 1.9 |
| 2cb71f16-fb74-3ab2-a546-906b90895d49 | -10.64543 | -45.24699 | 2025-10-16 03:28:00 | NPP-375D | CRISTALÂNDIA DO PIAUÍ | PIAUÍ | Brasil | 2203008 | 22 | 33 | nan | nan | nan | Cerrado | 10.9 |
| b9fee15b-174d-3b95-a536-a4ac309ace19 | -14.6474 | -42.38375 | 2025-10-16 03:28:00 | NPP-375D | LICÍNIO DE ALMEIDA | BAHIA | Brasil | 2919405 | 29 | 33 | nan | nan | nan | Caatinga | 1.8 |
| f0303910-76c0-3f91-a6d5-abe094687cd2 | -11.49139 | -44.10947 | 2025-10-16 03:28:00 | NPP-375D | COTEGIPE | BAHIA | Brasil | 2909406 | 29 | 33 | nan | nan | nan | Cerrado | 1.2 |
| 6c02e10f-396b-349b-b54c-fbfa9bb9ceed | -11.49252 | -44.10398 | 2025-10-16 03:28:00 | NPP-375D | COTEGIPE | BAHIA | Brasil | 2909406 | 29 | 33 | nan | nan | nan | Cerrado | 1.2 |
| b89aa03a-34f7-36fa-91e9-c787f2b94ad9 | -10.12691 | -44.57841 | 2025-10-16 03:28:00 | NPP-375D | PARNAGUÁ | PIAUÍ | Brasil | 2207603 | 22 | 33 | nan | nan | nan | Cerrado | 6.9 |
| 9e4b341a-a19c-3452-ba6e-8372b541c63e | -11.46251 | -44.18427 | 2025-10-16 03:28:00 | NPP-375D | COTEGIPE | BAHIA | Brasil | 2909406 | 29 | 33 | nan | nan | nan | Cerrado | 1.9 |
| aa985f41-ba3a-388a-80bc-6bdf1f6a001e | -8.25508 | -44.08795 | 2025-10-16 03:28:00 | NPP-375D | MANOEL EMÍDIO | PIAUÍ | Brasil | 2205904 | 22 | 33 | nan | nan | nan | Cerrado | 1.4 |
| 87ef83dc-529c-390b-9c08-2e1b2aa0cd9e | -13.65273 | -43.92767 | 2025-10-16 03:28:00 | NPP-375D | SERRA DO RAMALHO | BAHIA | Brasil | 2930154 | 29 | 33 | nan | nan | nan | Cerrado | 2.6 |
| b9e4e3ab-47b5-3d4c-a74c-8ba8e9116680 | -11.44647 | -44.16341 | 2025-10-16 03:28:00 | NPP-375D | MANSIDÃO | BAHIA | Brasil | 2920452 | 29 | 33 | nan | nan | nan | Cerrado | 1.2 |
| 19cab3dc-028a-3161-9de6-b29646ed6d89 | -12.67817 | -43.43578 | 2025-10-16 03:28:00 | NPP-375D | SÍTIO DO MATO | BAHIA | Brasil | 2930758 | 29 | 33 | nan | nan | nan | Cerrado | 12.3 |
| fb54606f-c1fc-374a-a08d-0ac980250c53 | -10.52108 | -43.3726 | 2025-10-16 03:28:00 | NPP-375D | BARRA | BAHIA | Brasil | 2902708 | 29 | 33 | nan | nan | nan | Cerrado | 1.3 |
| 315a035e-42df-3ebf-94fd-daf00ed6b30d | -7.9285 | -44.1246 | 2025-10-16 03:28:00 | NPP-375D | SEBASTIÃO LEAL | PIAUÍ | Brasil | 2210631 | 22 | 33 | nan | nan | nan | Cerrado | 6.5 |
| 159aa664-e80e-31ca-8e1c-d2222faa0ba6 | -11.58593 | -44.07422 | 2025-10-16 03:28:00 | NPP-375D | WANDERLEY | BAHIA | Brasil | 2933455 | 29 | 33 | nan | nan | nan | Cerrado | 5.3 |
| a4784fa9-3ef3-3fc6-881e-f606348a277c | -7.95227 | -44.14905 | 2025-10-16 03:28:00 | NPP-375D | SEBASTIÃO LEAL | PIAUÍ | Brasil | 2210631 | 22 | 33 | nan | nan | nan | Cerrado | 14.3 |
| 16ffb816-c796-3e90-99e3-11815029b98c | -10.52178 | -43.37878 | 2025-10-16 03:28:00 | NPP-375D | BURITIRAMA | BAHIA | Brasil | 2904753 | 29 | 33 | nan | nan | nan | Cerrado | 2.7 |
| 6bea1ccd-cd12-310f-9396-feebcc4bbb5c | -7.9289 | -44.12428 | 2025-10-16 03:28:00 | NPP-375D | SEBASTIÃO LEAL | PIAUÍ | Brasil | 2210631 | 22 | 33 | nan | nan | nan | Cerrado | 6.9 |
| a7e099f4-ee1f-3482-9764-21ff00fd8515 | -13.90506 | -45.5724 | 2025-10-16 03:28:00 | NPP-375D | JABORANDI | BAHIA | Brasil | 2917359 | 29 | 33 | nan | nan | nan | Cerrado | 1.8 |
| 501527a3-aad2-3f45-82a0-3fd859068dab | -8.2527 | -44.10042 | 2025-10-16 03:28:00 | NPP-375D | MANOEL EMÍDIO | PIAUÍ | Brasil | 2205904 | 22 | 33 | nan | nan | nan | Cerrado | 2.0 |
| 9f607b08-7d10-3742-a37a-64c2dfbe9d85 | -12.67649 | -43.44057 | 2025-10-16 03:28:00 | NPP-375D | SÍTIO DO MATO | BAHIA | Brasil | 2930758 | 29 | 33 | nan | nan | nan | Cerrado | 8.2 |
| 8a0b200d-9e68-3f9f-a422-a3eb440bebbb | -8.21916 | -43.31948 | 2025-10-16 03:28:00 | NPP-375D | CANTO DO BURITI | PIAUÍ | Brasil | 2202307 | 22 | 33 | nan | nan | nan | Caatinga | 3.4 |
| e5187b9a-4d6f-3f9b-abc3-e5e89edbffcf | -7.94786 | -44.13504 | 2025-10-16 03:28:00 | NPP-375D | SEBASTIÃO LEAL | PIAUÍ | Brasil | 2210631 | 22 | 33 | nan | nan | nan | Cerrado | 7.0 |
| 4c7af539-1de7-3fbf-bd01-ff2380df4764 | -10.12538 | -44.58602 | 2025-10-16 03:28:00 | NPP-375D | PARNAGUÁ | PIAUÍ | Brasil | 2207603 | 22 | 33 | nan | nan | nan | Cerrado | 6.9 |
| 5a41affc-9b31-316a-80e6-722e62c83127 | -8.24854 | -43.34296 | 2025-10-16 03:28:00 | NPP-375D | CANTO DO BURITI | PIAUÍ | Brasil | 2202307 | 22 | 33 | nan | nan | nan | Caatinga | 1.0 |
| c6e4e859-ae08-3a8d-82e4-dd5efdd42f17 | -10.63409 | -44.42425 | 2025-10-16 03:28:00 | NPP-375D | SANTA RITA DE CÁSSIA | BAHIA | Brasil | 2928406 | 29 | 33 | nan | nan | nan | Cerrado | 2.3 |
| 38240e4f-feb1-342b-918d-af06b8fcd7ff | -7.35542 | -43.86113 | 2025-10-16 03:28:00 | NPP-375D | LANDRI SALES | PIAUÍ | Brasil | 2205607 | 22 | 33 | nan | nan | nan | Cerrado | 10.6 |
| b9bcc1bc-fbba-303e-ac5b-3d5f8335460e | -10.04785 | -43.83738 | 2025-10-16 03:28:00 | NPP-375D | MORRO CABEÇA NO TEMPO | PIAUÍ | Brasil | 2206654 | 22 | 33 | nan | nan | nan | Cerrado | 3.1 |
| 05400472-af00-3608-9f0d-ca342ed103c4 | -7.46848 | -42.67406 | 2025-10-16 03:28:00 | NPP-375D | SÃO JOSÉ DO PEIXE | PIAUÍ | Brasil | 2210102 | 22 | 33 | nan | nan | nan | Caatinga | 1.9 |
| 61141c67-b1fa-36c5-ab59-151f37574621 | -11.5848 | -44.0797 | 2025-10-16 03:28:00 | NPP-375D | WANDERLEY | BAHIA | Brasil | 2933455 | 29 | 33 | nan | nan | nan | Cerrado | 5.3 |
| f8555f38-5d44-3391-a56e-bf95c221f3e7 | -7.39217 | -44.75767 | 2025-10-16 03:28:00 | NPP-375D | URUÇUÍ | PIAUÍ | Brasil | 2211209 | 22 | 33 | nan | nan | nan | Cerrado | 4.2 |
| 4f8c2dfb-801d-30a7-b791-37fd9c369677 | -9.68947 | -44.52482 | 2025-10-16 03:28:00 | NPP-375D | REDENÇÃO DO GURGUÉIA | PIAUÍ | Brasil | 2208700 | 22 | 33 | nan | nan | nan | Cerrado | 6.0 |
| c86fdfa3-7f0f-3c57-9e7c-4196e9aa8cb5 | -10.12949 | -44.56567 | 2025-10-16 03:28:00 | NPP-375D | PARNAGUÁ | PIAUÍ | Brasil | 2207603 | 22 | 33 | nan | nan | nan | Cerrado | 2.6 |
| 37c3c64a-de61-36f3-afd5-265299ce4602 | -10.81637 | -43.94451 | 2025-10-16 03:28:00 | NPP-375D | MANSIDÃO | BAHIA | Brasil | 2920452 | 29 | 33 | nan | nan | nan | Cerrado | 1.1 |
| fed2a02a-a175-364c-ad3c-71d2e3d969d3 | -7.67085 | -42.37668 | 2025-10-16 03:28:00 | NPP-375D | SÃO MIGUEL DO FIDALGO | PIAUÍ | Brasil | 2210391 | 22 | 33 | nan | nan | nan | Caatinga | 1.8 |
| 7af37baf-3305-3cd0-ac21-aed9dbc11048 | -7.89542 | -42.9556 | 2025-10-16 03:28:00 | NPP-375D | PAJEÚ DO PIAUÍ | PIAUÍ | Brasil | 2207355 | 22 | 33 | nan | nan | nan | Caatinga | 1.0 |
| f3607c01-da79-3efc-b061-753a27cc90e2 | -8.46398 | -44.18137 | 2025-10-16 03:28:00 | NPP-375D | ALVORADA DO GURGUÉIA | PIAUÍ | Brasil | 2200459 | 22 | 33 | nan | nan | nan | Cerrado | 13.6 |
| b91875f5-3a5c-30a9-8440-971bda9fa084 | -14.64661 | -42.38762 | 2025-10-16 03:28:00 | NPP-375D | LICÍNIO DE ALMEIDA | BAHIA | Brasil | 2919405 | 29 | 33 | nan | nan | nan | Caatinga | 2.3 |
| 45b6fedf-fca7-310d-942c-4ad078d183b6 | -9.25748 | -45.26842 | 2025-10-16 03:28:00 | NPP-375D | BOM JESUS | PIAUÍ | Brasil | 2201903 | 22 | 33 | nan | nan | nan | Cerrado | 14.5 |
| 3350c96d-5717-3c24-b2cb-f1866a3bc705 | -10.1214 | -44.57063 | 2025-10-16 03:28:00 | NPP-375D | PARNAGUÁ | PIAUÍ | Brasil | 2207603 | 22 | 33 | nan | nan | nan | Cerrado | 2.2 |
| 70d1f97a-64b3-3a44-925d-faec3d872414 | -8.45462 | -44.19279 | 2025-10-16 03:28:00 | NPP-375D | ALVORADA DO GURGUÉIA | PIAUÍ | Brasil | 2200459 | 22 | 33 | nan | nan | nan | Cerrado | 14.5 |
| c031ad21-00bd-3da3-97f3-1a4768fc65ad | -10.12393 | -44.59325 | 2025-10-16 03:28:00 | NPP-375D | PARNAGUÁ | PIAUÍ | Brasil | 2207603 | 22 | 33 | nan | nan | nan | Cerrado | 9.1 |
| b9690416-3642-35ea-afd0-ea5a72d74b77 | -13.89778 | -45.57698 | 2025-10-16 03:28:00 | NPP-375D | JABORANDI | BAHIA | Brasil | 2917359 | 29 | 33 | nan | nan | nan | Cerrado | 2.5 |
| fc02c936-5b9c-3c25-9f83-46e28dec95ac | -7.34854 | -43.86008 | 2025-10-16 03:28:00 | NPP-375D | LANDRI SALES | PIAUÍ | Brasil | 2205607 | 22 | 33 | nan | nan | nan | Cerrado | 10.6 |
| 5ed80aa5-f812-3e94-b2ef-46b34dc7dafa | -8.2913 | -43.40397 | 2025-10-16 03:28:00 | NPP-375D | CANTO DO BURITI | PIAUÍ | Brasil | 2202307 | 22 | 33 | nan | nan | nan | Caatinga | 1.3 |
| 22b76594-54b1-3b3f-b565-240c6189d741 | -7.34041 | -43.86548 | 2025-10-16 03:28:00 | NPP-375D | LANDRI SALES | PIAUÍ | Brasil | 2205607 | 22 | 33 | nan | nan | nan | Cerrado | 3.7 |
| 78ac2441-293c-31bf-820c-aa26237c10aa | -11.44417 | -44.17453 | 2025-10-16 03:28:00 | NPP-375D | MANSIDÃO | BAHIA | Brasil | 2920452 | 29 | 33 | nan | nan | nan | Cerrado | 2.2 |
| 5918d9a4-2093-312c-94d8-ee914dce98a0 | -7.93413 | -44.13228 | 2025-10-16 03:28:00 | NPP-375D | SEBASTIÃO LEAL | PIAUÍ | Brasil | 2210631 | 22 | 33 | nan | nan | nan | Cerrado | 6.9 |
| f2457f25-73ac-369c-8b2c-ca0bf6287f72 | -7.34003 | -43.86489 | 2025-10-16 03:28:00 | NPP-375D | LANDRI SALES | PIAUÍ | Brasil | 2205607 | 22 | 33 | nan | nan | nan | Cerrado | 5.4 |
| 38131461-400a-3297-ad86-0feba11a311a | -7.39354 | -44.7504 | 2025-10-16 03:28:00 | NPP-375D | URUÇUÍ | PIAUÍ | Brasil | 2211209 | 22 | 33 | nan | nan | nan | Cerrado | 4.2 |
| c17aced5-5e9d-3d35-ad0f-ca52f2b13444 | -14.63955 | -42.39405 | 2025-10-16 03:28:00 | NPP-375D | LICÍNIO DE ALMEIDA | BAHIA | Brasil | 2919405 | 29 | 33 | nan | nan | nan | Caatinga | 2.0 |
| 6d111dd9-cc71-3490-a9d7-c83587161368 | -7.94264 | -44.12703 | 2025-10-16 03:28:00 | NPP-375D | SEBASTIÃO LEAL | PIAUÍ | Brasil | 2210631 | 22 | 33 | nan | nan | nan | Cerrado | 3.1 |
| e5dd9b69-7854-36cb-8aac-3cf370871f60 | -10.61269 | -42.31096 | 2025-10-16 03:28:00 | NPP-375D | ITAGUAÇU DA BAHIA | BAHIA | Brasil | 2915353 | 29 | 33 | nan | nan | nan | Caatinga | 1.1 |
| d1bee0e7-4d6b-3f6f-bb3e-c8b0a601a093 | -10.6964 | -44.43919 | 2025-10-16 03:28:00 | NPP-375D | SANTA RITA DE CÁSSIA | BAHIA | Brasil | 2928406 | 29 | 33 | nan | nan | nan | Cerrado | 8.9 |
| 6292742f-69ad-3e31-ab74-3b4a25227c5d | -7.6781 | -42.55958 | 2025-10-16 03:28:00 | NPP-375D | SÃO JOSÉ DO PEIXE | PIAUÍ | Brasil | 2210102 | 22 | 33 | nan | nan | nan | Caatinga | 1.3 |
| b2da7c87-3677-34c8-8d11-e78ba520d8ad | -7.48054 | -42.14773 | 2025-10-16 03:28:00 | NPP-375D | SANTO INÁCIO DO PIAUÍ | PIAUÍ | Brasil | 2209500 | 22 | 33 | nan | nan | nan | Caatinga | 1.5 |
| 11f6bdc8-a4c4-3aee-bb57-7b137c73ea00 | -9.6829 | -44.52451 | 2025-10-16 03:28:00 | NPP-375D | REDENÇÃO DO GURGUÉIA | PIAUÍ | Brasil | 2208700 | 22 | 33 | nan | nan | nan | Cerrado | 6.0 |
| e1879ca7-4c09-3695-acb2-80c979b3311e | -7.93537 | -44.12594 | 2025-10-16 03:28:00 | NPP-375D | SEBASTIÃO LEAL | PIAUÍ | Brasil | 2210631 | 22 | 33 | nan | nan | nan | Cerrado | 3.5 |
| 0da5c29e-472a-365a-9438-19253cdf9789 | -14.8857 | -42.13453 | 2025-10-16 03:28:00 | NPP-375D | CONDEÚBA | BAHIA | Brasil | 2908705 | 29 | 33 | nan | nan | nan | Caatinga | 1.0 |


[Clique aqui para ver as próximas entradas](README17.md)
