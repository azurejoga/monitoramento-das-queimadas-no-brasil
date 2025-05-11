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

## Dados Diários - Página 4

| ID | Latitude | Longitude | Data/Hora GMT | Satélite | Município | Estado | País | Município ID | Estado ID | País ID | Dias sem Chuva | Precipitação | Risco de Fogo | Bioma | FRP |
|----|----------|-----------|---------------|----------|-----------|--------|------|--------------|-----------|---------|----------------|--------------|----------------|-------|-----|
| f7f7b7df-e164-3cb6-9497-d8af0b56b1b7 | -17.22925 | -47.38936 | 2025-05-11 04:29:00 | NPP-375D | CRISTALINA | GOIÁS | Brasil | 5206206 | 52 | 33 | nan | nan | nan | Cerrado | 1.9 |
| 3367706a-f4da-3b51-87be-d6a2d7cb4c56 | -12.72167 | -54.97417 | 2025-05-11 04:29:00 | NPP-375D | FELIZ NATAL | MATO GROSSO | Brasil | 5103700 | 51 | 33 | nan | nan | nan | Amazônia | 1.0 |
| 26a0da6d-38cf-33b1-b0b0-21b51dc2fdc4 | -13.97469 | -56.81066 | 2025-05-11 04:29:00 | NPP-375D | DIAMANTINO | MATO GROSSO | Brasil | 5103502 | 51 | 33 | nan | nan | nan | Cerrado | 2.8 |
| 32390839-2953-3ba8-8095-ff69d00fc60b | -16.49308 | -43.13649 | 2025-05-11 04:29:00 | NPP-375D | GRÃO MOGOL | MINAS GERAIS | Brasil | 3127800 | 31 | 33 | nan | nan | nan | Cerrado | 1.9 |
| 2d9357d6-d0a8-32d4-a6f5-5a7f12305f12 | -13.97975 | -56.8119 | 2025-05-11 04:29:00 | NPP-375D | DIAMANTINO | MATO GROSSO | Brasil | 5103502 | 51 | 33 | nan | nan | nan | Cerrado | 2.8 |
| 27067722-4b5a-341a-ac5c-dd0a6f03774d | -13.04884 | -53.71795 | 2025-05-11 04:29:00 | NPP-375D | GAÚCHA DO NORTE | MATO GROSSO | Brasil | 5103858 | 51 | 33 | nan | nan | nan | Amazônia | 2.8 |
| fb2bac48-0d0d-383f-b9e8-1f266393d79f | -14.67072 | -45.12754 | 2025-05-11 04:29:00 | NPP-375D | COCOS | BAHIA | Brasil | 2908101 | 29 | 33 | nan | nan | nan | Cerrado | 1.4 |
| 2eeb6fe7-be2a-3995-8a67-3d9c73ba88f3 | -12.65018 | -54.06655 | 2025-05-11 04:29:00 | NPP-375D | PARANATINGA | MATO GROSSO | Brasil | 5106307 | 51 | 33 | nan | nan | nan | Amazônia | 2.4 |
| 1b0c0ee2-d75a-341b-8f0d-576c19fd1dc7 | -13.98205 | -56.80907 | 2025-05-11 04:29:00 | NPP-375D | DIAMANTINO | MATO GROSSO | Brasil | 5103502 | 51 | 33 | nan | nan | nan | Cerrado | 2.8 |
| f485203d-0f76-3e20-a04e-51206fef484e | -14.28006 | -42.69509 | 2025-05-11 04:29:00 | NPP-375D | GUANAMBI | BAHIA | Brasil | 2911709 | 29 | 33 | nan | nan | nan | Caatinga | 0.7 |
| e16f0596-0893-33d1-9502-6c048bf623dd | -13.48376 | -52.9794 | 2025-05-11 04:29:00 | NPP-375D | CANARANA | MATO GROSSO | Brasil | 5102702 | 51 | 33 | nan | nan | nan | Cerrado | 4.7 |
| 9f1dee36-0183-3496-9c09-7b2906f54dde | -14.65267 | -45.12482 | 2025-05-11 04:29:00 | NPP-375D | COCOS | BAHIA | Brasil | 2908101 | 29 | 33 | nan | nan | nan | Cerrado | 1.8 |
| 48f29d92-ccf5-3e58-aded-34b7a78b3e2f | -16.10764 | -47.54616 | 2025-05-11 04:29:00 | NPP-375D | CRISTALINA | GOIÁS | Brasil | 5206206 | 52 | 33 | nan | nan | nan | Cerrado | 1.5 |
| 72a7e3e0-72c0-3619-a317-e028c7e70589 | -13.37642 | -54.26374 | 2025-05-11 04:29:00 | NPP-375D | PARANATINGA | MATO GROSSO | Brasil | 5106307 | 51 | 33 | nan | nan | nan | Amazônia | 1.4 |
| a7fc5cbf-b4f7-397b-8131-4dc00ccd9f89 | -13.05006 | -53.71877 | 2025-05-11 04:29:00 | NPP-375D | GAÚCHA DO NORTE | MATO GROSSO | Brasil | 5103858 | 51 | 33 | nan | nan | nan | Amazônia | 3.2 |
| c91e11f8-c89a-37bd-9ae2-71a471598bd4 | -14.21761 | -54.5693 | 2025-05-11 04:29:00 | NPP-375D | PARANATINGA | MATO GROSSO | Brasil | 5106307 | 51 | 33 | nan | nan | nan | Cerrado | 0.9 |
| f2277db6-9a43-3f88-b95e-1bc7cab19062 | -14.64907 | -45.12428 | 2025-05-11 04:29:00 | NPP-375D | COCOS | BAHIA | Brasil | 2908101 | 29 | 33 | nan | nan | nan | Cerrado | 1.0 |
| 0c69dc7b-c53c-3bf6-b813-8bc80949becc | -13.41226 | -50.27098 | 2025-05-11 04:29:00 | NPP-375D | SÃO MIGUEL DO ARAGUAIA | GOIÁS | Brasil | 5220207 | 52 | 33 | nan | nan | nan | Cerrado | 2.1 |
| 5900a760-f560-37fd-b669-ec047e598d1e | -13.4816 | -52.96814 | 2025-05-11 04:29:00 | NPP-375D | CANARANA | MATO GROSSO | Brasil | 5102702 | 51 | 33 | nan | nan | nan | Cerrado | 3.9 |
| 751b27c6-bef0-3057-8020-079d783a98e2 | -14.1779 | -41.66527 | 2025-05-11 04:29:00 | NPP-375D | BRUMADO | BAHIA | Brasil | 2904605 | 29 | 33 | nan | nan | nan | Caatinga | 1.3 |
| ef130dc0-49f2-3a7a-9689-326f20ba85e6 | -13.47574 | -52.97791 | 2025-05-11 04:29:00 | NPP-375D | CANARANA | MATO GROSSO | Brasil | 5102702 | 51 | 33 | nan | nan | nan | Cerrado | 5.9 |
| ac112c38-7790-3c0a-b6ca-5a11f4bafce9 | -14.64783 | -45.13274 | 2025-05-11 04:29:00 | NPP-375D | COCOS | BAHIA | Brasil | 2908101 | 29 | 33 | nan | nan | nan | Cerrado | 1.0 |
| 4df06f82-d9c5-3c9e-b1ec-cc125ffe3a13 | -13.48438 | -52.97591 | 2025-05-11 04:29:00 | NPP-375D | CANARANA | MATO GROSSO | Brasil | 5102702 | 51 | 33 | nan | nan | nan | Cerrado | 4.7 |
| 20747253-b9e3-322c-8e1c-d95b699b9fcd | -14.66738 | -45.12948 | 2025-05-11 04:29:00 | NPP-375D | COCOS | BAHIA | Brasil | 2908101 | 29 | 33 | nan | nan | nan | Cerrado | 2.0 |
| b354ecdf-980b-398d-9cf3-e2d03da49fef | -13.47697 | -52.97091 | 2025-05-11 04:29:00 | NPP-375D | CANARANA | MATO GROSSO | Brasil | 5102702 | 51 | 33 | nan | nan | nan | Cerrado | 3.6 |
| beeff0fc-d6b7-3f75-8262-54b5da965167 | -13.04388 | -53.72108 | 2025-05-11 04:29:00 | NPP-375D | GAÚCHA DO NORTE | MATO GROSSO | Brasil | 5103858 | 51 | 33 | nan | nan | nan | Amazônia | 3.7 |
| c5cb3f4d-84a6-332d-beb3-7e3c45966618 | -13.04019 | -53.72504 | 2025-05-11 04:29:00 | NPP-375D | GAÚCHA DO NORTE | MATO GROSSO | Brasil | 5103858 | 51 | 33 | nan | nan | nan | Amazônia | 2.1 |
| 0b1f5972-bc24-3b4c-90e6-f86f7705b363 | -14.86836 | -51.98295 | 2025-05-11 04:29:00 | NPP-375D | ARAGUAIANA | MATO GROSSO | Brasil | 5101001 | 51 | 33 | nan | nan | nan | Cerrado | 2.8 |
| d77550d3-88dd-3860-a9a7-38cbb6a5f2ce | -17.09795 | -47.93413 | 2025-05-11 04:29:00 | NPP-375D | IPAMERI | GOIÁS | Brasil | 5210109 | 52 | 33 | nan | nan | nan | Cerrado | 0.8 |
| 1684a818-f89a-33c5-9c9f-61145a52ae62 | -17.45924 | -44.71511 | 2025-05-11 04:29:00 | NPP-375D | VÁRZEA DA PALMA | MINAS GERAIS | Brasil | 3170800 | 31 | 33 | nan | nan | nan | Cerrado | 0.8 |
| 2285ccf5-f602-39b3-8386-cfec24d9769f | -14.86973 | -51.98071 | 2025-05-11 04:29:00 | NPP-375D | ARAGUAIANA | MATO GROSSO | Brasil | 5101001 | 51 | 33 | nan | nan | nan | Cerrado | 3.2 |
| 441303bc-4bc7-3ad1-a9a7-7026cbf35648 | -14.2209 | -54.55171 | 2025-05-11 04:29:00 | NPP-375D | PARANATINGA | MATO GROSSO | Brasil | 5106307 | 51 | 33 | nan | nan | nan | Cerrado | 0.8 |
| 26e48fc7-9d41-3635-b6e7-8a04cb09984d | -12.6856 | -58.15155 | 2025-05-11 04:29:00 | NPP-375D | BRASNORTE | MATO GROSSO | Brasil | 5101902 | 51 | 33 | nan | nan | nan | Cerrado | 0.8 |
| 6b811d8b-52d7-3696-a2d0-ee22211c1780 | -12.6913 | -58.15269 | 2025-05-11 04:29:00 | NPP-375D | BRASNORTE | MATO GROSSO | Brasil | 5101902 | 51 | 33 | nan | nan | nan | Cerrado | 0.8 |
| b974a157-d564-3412-8eb8-8c21dc3e71c3 | -11.62363 | -54.94123 | 2025-05-11 04:29:00 | NPP-375D | CLÁUDIA | MATO GROSSO | Brasil | 5103056 | 51 | 33 | nan | nan | nan | Amazônia | 1.6 |
| 21ba005e-fb16-3f13-9df4-a6bc40b3f211 | -15.07975 | -48.94377 | 2025-05-11 04:29:00 | NPP-375D | BARRO ALTO | GOIÁS | Brasil | 5203203 | 52 | 33 | nan | nan | nan | Cerrado | 1.8 |
| 46271c21-daad-387a-8b66-4c636b3d4fca | -13.04314 | -53.72507 | 2025-05-11 04:29:00 | NPP-375D | GAÚCHA DO NORTE | MATO GROSSO | Brasil | 5103858 | 51 | 33 | nan | nan | nan | Amazônia | 3.7 |
| c0181734-692a-3a5d-9087-2cf5aba68b37 | -13.04513 | -53.72189 | 2025-05-11 04:29:00 | NPP-375D | GAÚCHA DO NORTE | MATO GROSSO | Brasil | 5103858 | 51 | 33 | nan | nan | nan | Amazônia | 2.1 |
| f57e912c-6936-3eea-9304-a1e80def30ff | -13.47636 | -52.9744 | 2025-05-11 04:29:00 | NPP-375D | CANARANA | MATO GROSSO | Brasil | 5102702 | 51 | 33 | nan | nan | nan | Cerrado | 5.9 |
| 7652168b-e7f7-3e60-ba8e-69e6a3f2d474 | -11.62541 | -54.93833 | 2025-05-11 04:29:00 | NPP-375D | CLÁUDIA | MATO GROSSO | Brasil | 5103056 | 51 | 33 | nan | nan | nan | Amazônia | 1.8 |
| 3e280909-11e1-373e-bc89-3c3b5a3f1cdd | -14.65144 | -45.13329 | 2025-05-11 04:29:00 | NPP-375D | COCOS | BAHIA | Brasil | 2908101 | 29 | 33 | nan | nan | nan | Cerrado | 1.7 |
| eb41f079-56a4-3518-a26c-7f82ed3e31de | -12.64941 | -54.07087 | 2025-05-11 04:29:00 | NPP-375D | PARANATINGA | MATO GROSSO | Brasil | 5106307 | 51 | 33 | nan | nan | nan | Amazônia | 2.2 |
| 3e06ead3-7121-3fae-983d-ebebbff5b268 | -13.04737 | -53.72592 | 2025-05-11 04:29:00 | NPP-375D | GAÚCHA DO NORTE | MATO GROSSO | Brasil | 5103858 | 51 | 33 | nan | nan | nan | Amazônia | 3.7 |
| 5ab6fa93-268f-31c1-93d0-2155988dd24e | -14.66678 | -45.13372 | 2025-05-11 04:29:00 | NPP-375D | COCOS | BAHIA | Brasil | 2908101 | 29 | 33 | nan | nan | nan | Cerrado | 2.0 |
| 247c20e3-1b63-39fa-b1f0-febd8d304942 | -14.66377 | -45.12894 | 2025-05-11 04:29:00 | NPP-375D | COCOS | BAHIA | Brasil | 2908101 | 29 | 33 | nan | nan | nan | Cerrado | 2.0 |
| 78d04290-c8b9-3497-9a29-81258c087083 | -13.48839 | -52.97666 | 2025-05-11 04:29:00 | NPP-375D | CANARANA | MATO GROSSO | Brasil | 5102702 | 51 | 33 | nan | nan | nan | Cerrado | 2.3 |
| f669444e-9981-3e3b-bc8a-e3d9c0b25152 | -14.21926 | -54.56051 | 2025-05-11 04:29:00 | NPP-375D | PARANATINGA | MATO GROSSO | Brasil | 5106307 | 51 | 33 | nan | nan | nan | Cerrado | 1.0 |
| 8c85e537-db14-375b-8d4f-60f44eeb89ff | -14.87344 | -51.98139 | 2025-05-11 04:29:00 | NPP-375D | ARAGUAIANA | MATO GROSSO | Brasil | 5101001 | 51 | 33 | nan | nan | nan | Cerrado | 3.2 |
| 76c3540b-03d8-3cb9-b623-c070ada3ebcd | -13.97698 | -56.80786 | 2025-05-11 04:29:00 | NPP-375D | DIAMANTINO | MATO GROSSO | Brasil | 5103502 | 51 | 33 | nan | nan | nan | Cerrado | 2.8 |
| a32322fa-117c-35f4-a174-fb5bf83407e2 | -14.31598 | -54.64834 | 2025-05-11 04:29:00 | NPP-375D | PARANATINGA | MATO GROSSO | Brasil | 5106307 | 51 | 33 | nan | nan | nan | Cerrado | 1.2 |
| 8291ae7e-d7bb-3039-bebc-9b04f6ea28b9 | -13.41291 | -50.26704 | 2025-05-11 04:29:00 | NPP-375D | SÃO MIGUEL DO ARAGUAIA | GOIÁS | Brasil | 5220207 | 52 | 33 | nan | nan | nan | Cerrado | 1.4 |
| 1e69736b-694a-32ae-af52-ad295797c9fb | -14.64845 | -45.12851 | 2025-05-11 04:29:00 | NPP-375D | COCOS | BAHIA | Brasil | 2908101 | 29 | 33 | nan | nan | nan | Cerrado | 1.0 |
| d1e08360-30eb-36ee-accf-90f4673a7b0b | -13.09393 | -52.29429 | 2025-05-11 04:29:00 | NPP-375D | QUERÊNCIA | MATO GROSSO | Brasil | 5107065 | 51 | 33 | nan | nan | nan | Amazônia | 1.5 |
| 3ae7d316-a12c-320c-b0ac-df6832c131e1 | -13.48037 | -52.97515 | 2025-05-11 04:29:00 | NPP-375D | CANARANA | MATO GROSSO | Brasil | 5102702 | 51 | 33 | nan | nan | nan | Cerrado | 4.7 |
| 47645459-ed4e-3d0c-9fd1-b7262251be41 | -13.48098 | -52.97166 | 2025-05-11 04:29:00 | NPP-375D | CANARANA | MATO GROSSO | Brasil | 5102702 | 51 | 33 | nan | nan | nan | Cerrado | 3.9 |
| 500b5728-d2c4-3548-94e2-ca776059f903 | -11.91662 | -54.41109 | 2025-05-11 04:29:00 | NPP-375D | SANTA CARMEM | MATO GROSSO | Brasil | 5107248 | 51 | 33 | nan | nan | nan | Amazônia | 1.2 |
| 6df4347b-36ad-331e-afd8-fd41e4e07364 | -14.67009 | -45.13178 | 2025-05-11 04:29:00 | NPP-375D | COCOS | BAHIA | Brasil | 2908101 | 29 | 33 | nan | nan | nan | Cerrado | 3.2 |
| f6c7b5dd-8da5-39ef-a284-81b7f729da9b | -13.09378 | -52.29626 | 2025-05-11 04:29:00 | NPP-375D | QUERÊNCIA | MATO GROSSO | Brasil | 5107065 | 51 | 33 | nan | nan | nan | Amazônia | 1.2 |
| c453b3b5-3054-341c-8cf8-bb47f041849f | -14.28475 | -42.69149 | 2025-05-11 04:29:00 | NPP-375D | GUANAMBI | BAHIA | Brasil | 2911709 | 29 | 33 | nan | nan | nan | Caatinga | 0.4 |
| 8ecc60cd-9f18-3c68-9d01-832e2ece354e | -17.77962 | -42.81004 | 2025-05-11 04:29:00 | NPP-375D | ITAMARANDIBA | MINAS GERAIS | Brasil | 3132503 | 31 | 33 | nan | nan | nan | Cerrado | 1.3 |
| e94d7ef1-6db0-3c06-a4d5-8d74ee80c424 | -12.17356 | -54.23619 | 2025-05-11 04:29:00 | NPP-375D | FELIZ NATAL | MATO GROSSO | Brasil | 5103700 | 51 | 33 | nan | nan | nan | Amazônia | 3.6 |
| 375b3650-4ed4-353f-88ce-b1be43965301 | -13.05233 | -53.7228 | 2025-05-11 04:29:00 | NPP-375D | GAÚCHA DO NORTE | MATO GROSSO | Brasil | 5103858 | 51 | 33 | nan | nan | nan | Amazônia | 1.1 |
| b310c7d9-04a3-3c4f-8b3e-89f60121f147 | -17.00852 | -49.78075 | 2025-05-11 04:29:00 | NPP-375D | CEZARINA | GOIÁS | Brasil | 5205455 | 52 | 33 | nan | nan | nan | Cerrado | 0.8 |
| 2e06bab0-e2cf-3d8e-aa4f-95529c20e69f | -14.21679 | -54.57369 | 2025-05-11 04:29:00 | NPP-375D | PARANATINGA | MATO GROSSO | Brasil | 5106307 | 51 | 33 | nan | nan | nan | Cerrado | 0.9 |
| 869f242d-f6eb-36ea-bfc0-9e311e1302ed | -14.66711 | -45.12701 | 2025-05-11 04:29:00 | NPP-375D | COCOS | BAHIA | Brasil | 2908101 | 29 | 33 | nan | nan | nan | Cerrado | 1.4 |
| 8e3b816a-b014-3b77-9c4f-d8806ad065b7 | -13.97635 | -56.81102 | 2025-05-11 04:29:00 | NPP-375D | DIAMANTINO | MATO GROSSO | Brasil | 5103502 | 51 | 33 | nan | nan | nan | Cerrado | 2.8 |
| bff0dd1f-d54d-328b-8904-22173c2eaa47 | -12.72422 | -54.9767 | 2025-05-11 04:29:00 | NPP-375D | FELIZ NATAL | MATO GROSSO | Brasil | 5103700 | 51 | 33 | nan | nan | nan | Amazônia | 1.5 |
| 937dad97-3fb4-3524-a0da-c92a40a70d32 | -16.49675 | -43.14074 | 2025-05-11 04:29:00 | NPP-375D | GRÃO MOGOL | MINAS GERAIS | Brasil | 3127800 | 31 | 33 | nan | nan | nan | Cerrado | 1.9 |
| ad1cd9db-792c-3bf6-b446-a3631ee6b2ec | -18.59442 | -46.55127 | 2025-05-11 04:29:00 | NPP-375D | PATOS DE MINAS | MINAS GERAIS | Brasil | 3148004 | 31 | 33 | nan | nan | nan | Cerrado | 0.7 |
| d7cbf480-6428-3238-8a40-5c4b25d09db5 | -14.65504 | -45.13384 | 2025-05-11 04:29:00 | NPP-375D | COCOS | BAHIA | Brasil | 2908101 | 29 | 33 | nan | nan | nan | Cerrado | 1.7 |
| 1eef4f75-ee93-3b76-8318-727e96d8fa3b | -14.27129 | -47.33818 | 2025-05-11 04:29:00 | NPP-375D | SÃO JOÃO D'ALIANÇA | GOIÁS | Brasil | 5220009 | 52 | 33 | nan | nan | nan | Cerrado | 0.6 |
| 3dc15b07-5247-36c9-a121-5e4c17695b59 | -14.66317 | -45.13317 | 2025-05-11 04:29:00 | NPP-375D | COCOS | BAHIA | Brasil | 2908101 | 29 | 33 | nan | nan | nan | Cerrado | 2.0 |
| 5a137f10-928b-3c5f-97ca-7b61808a18b5 | -13.4776 | -52.96738 | 2025-05-11 04:29:00 | NPP-375D | CANARANA | MATO GROSSO | Brasil | 5102702 | 51 | 33 | nan | nan | nan | Cerrado | 3.6 |
| 7950c9af-95b5-3b47-a9af-e9a261848858 | -14.87207 | -51.98363 | 2025-05-11 04:29:00 | NPP-375D | ARAGUAIANA | MATO GROSSO | Brasil | 5101001 | 51 | 33 | nan | nan | nan | Cerrado | 2.8 |
| 5d6c9bbf-934c-3c51-ad91-c220dfe2246e | -14.21431 | -54.58694 | 2025-05-11 04:29:00 | NPP-375D | PARANATINGA | MATO GROSSO | Brasil | 5106307 | 51 | 33 | nan | nan | nan | Cerrado | 0.6 |
| 04d96638-c9b9-3e4c-91b5-4e49dc04d5d8 | -14.22009 | -54.55608 | 2025-05-11 04:29:00 | NPP-375D | PARANATINGA | MATO GROSSO | Brasil | 5106307 | 51 | 33 | nan | nan | nan | Cerrado | 0.8 |
| dadb906c-d29a-3bf4-b583-cb34c3520ac1 | -14.66287 | -45.1307 | 2025-05-11 04:29:00 | NPP-375D | COCOS | BAHIA | Brasil | 2908101 | 29 | 33 | nan | nan | nan | Cerrado | 2.2 |
| 57755bfc-1803-37e0-9c48-df62fdb04ef7 | -13.0409 | -53.72104 | 2025-05-11 04:29:00 | NPP-375D | GAÚCHA DO NORTE | MATO GROSSO | Brasil | 5103858 | 51 | 33 | nan | nan | nan | Amazônia | 2.1 |
| cd5a1d17-f24c-3766-90f1-47096f91b323 | -13.48777 | -52.98016 | 2025-05-11 04:29:00 | NPP-375D | CANARANA | MATO GROSSO | Brasil | 5102702 | 51 | 33 | nan | nan | nan | Cerrado | 2.3 |
| e5de2dca-6a5c-37e1-a01a-863b0d58f2a0 | -18.14632 | -47.79986 | 2025-05-11 04:29:00 | NPP-375D | OUVIDOR | GOIÁS | Brasil | 5215504 | 52 | 33 | nan | nan | nan | Cerrado | 0.8 |
| 1e1d5aec-0d66-3697-88d5-5b18fc021739 | -14.22251 | -54.54314 | 2025-05-11 04:29:00 | NPP-375D | PARANATINGA | MATO GROSSO | Brasil | 5106307 | 51 | 33 | nan | nan | nan | Cerrado | 1.1 |
| debba774-496d-384a-bca7-af25e5702deb | -14.21843 | -54.56491 | 2025-05-11 04:29:00 | NPP-375D | PARANATINGA | MATO GROSSO | Brasil | 5106307 | 51 | 33 | nan | nan | nan | Cerrado | 1.0 |
| 3519ad62-4070-3769-ad12-8d2420d4ce9d | -14.65206 | -45.12906 | 2025-05-11 04:29:00 | NPP-375D | COCOS | BAHIA | Brasil | 2908101 | 29 | 33 | nan | nan | nan | Cerrado | 1.7 |
| 0338eef1-d6e8-3405-9c7e-e03da8a020c8 | -13.4924 | -52.97743 | 2025-05-11 04:29:00 | NPP-375D | CANARANA | MATO GROSSO | Brasil | 5102702 | 51 | 33 | nan | nan | nan | Cerrado | 2.3 |
| 2ecbc5c9-7f5e-3fe9-8844-c2ab2d2b5e9a | -13.31419 | -47.16665 | 2025-05-11 04:29:00 | NPP-375D | MONTE ALEGRE DE GOIÁS | GOIÁS | Brasil | 5213509 | 52 | 33 | nan | nan | nan | Cerrado | 1.1 |
| fb9fb957-1977-35ea-a6b9-76b684e459d4 | -14.65865 | -45.13439 | 2025-05-11 04:29:00 | NPP-375D | COCOS | BAHIA | Brasil | 2908101 | 29 | 33 | nan | nan | nan | Cerrado | 2.2 |
| a3375f85-3288-3b01-ad01-b822d185dcb9 | -14.67159 | -45.12577 | 2025-05-11 04:29:00 | NPP-375D | COCOS | BAHIA | Brasil | 2908101 | 29 | 33 | nan | nan | nan | Cerrado | 0.6 |
| 6ed1678c-b9b3-3e1a-8a35-a300edd33776 | -13.489 | -52.97318 | 2025-05-11 04:29:00 | NPP-375D | CANARANA | MATO GROSSO | Brasil | 5102702 | 51 | 33 | nan | nan | nan | Cerrado | 1.6 |
| 777e6ec8-003f-3dd9-8f54-47f303e6f61c | -14.66648 | -45.13124 | 2025-05-11 04:29:00 | NPP-375D | COCOS | BAHIA | Brasil | 2908101 | 29 | 33 | nan | nan | nan | Cerrado | 3.2 |
| 74033042-634c-32fd-bcba-20e83dd5e95c | -14.64969 | -45.12004 | 2025-05-11 04:29:00 | NPP-375D | COCOS | BAHIA | Brasil | 2908101 | 29 | 33 | nan | nan | nan | Cerrado | 1.0 |
| dcb340db-d0c1-3fe1-92b4-443bcc00484b | -14.28055 | -42.69143 | 2025-05-11 04:29:00 | NPP-375D | GUANAMBI | BAHIA | Brasil | 2911709 | 29 | 33 | nan | nan | nan | Caatinga | 0.7 |
| f823fdbe-88e6-312f-a4b3-ccc45129f6b5 | -16.49723 | -43.13702 | 2025-05-11 04:29:00 | NPP-375D | GRÃO MOGOL | MINAS GERAIS | Brasil | 3127800 | 31 | 33 | nan | nan | nan | Cerrado | 1.9 |
| 8342f7ad-973c-3c98-b11f-a58eaa2d7e31 | -13.98036 | -56.80872 | 2025-05-11 04:29:00 | NPP-375D | DIAMANTINO | MATO GROSSO | Brasil | 5103502 | 51 | 33 | nan | nan | nan | Cerrado | 2.8 |
| 3f6ad8eb-1ef8-3a92-ba37-10a51130b139 | -13.04936 | -53.72276 | 2025-05-11 04:29:00 | NPP-375D | GAÚCHA DO NORTE | MATO GROSSO | Brasil | 5103858 | 51 | 33 | nan | nan | nan | Amazônia | 4.2 |
| a606e0da-6b16-363e-a44d-7b1ce1a00cca | -13.04442 | -53.72589 | 2025-05-11 04:29:00 | NPP-375D | GAÚCHA DO NORTE | MATO GROSSO | Brasil | 5103858 | 51 | 33 | nan | nan | nan | Amazônia | 2.1 |
| b3c96849-147d-3893-a1fe-4d34bdf70057 | -14.65442 | -45.13807 | 2025-05-11 04:29:00 | NPP-375D | COCOS | BAHIA | Brasil | 2908101 | 29 | 33 | nan | nan | nan | Cerrado | 1.6 |
| 9f424d45-d844-3bd5-bbb9-285ffd990a2a | -13.97529 | -56.8075 | 2025-05-11 04:29:00 | NPP-375D | DIAMANTINO | MATO GROSSO | Brasil | 5103502 | 51 | 33 | nan | nan | nan | Cerrado | 2.8 |
| aed2a485-cd67-3f03-a6bf-9160ee6d123b | -25.1934 | -49.32657 | 2025-05-11 04:32:00 | NPP-375D | RIO BRANCO DO SUL | PARANÁ | Brasil | 4122206 | 41 | 33 | nan | nan | nan | Mata Atlântica | 0.7 |
| 6788742f-d564-3d76-9602-d4e9cbe78cbc | -20.41656 | -43.55476 | 2025-05-11 04:32:00 | NPP-375D | OURO PRETO | MINAS GERAIS | Brasil | 3146107 | 31 | 33 | nan | nan | nan | Mata Atlântica | 1.7 |
| 9965919b-d5a0-3a5e-879b-fdfacc650d82 | -25.19002 | -49.32594 | 2025-05-11 04:32:00 | NPP-375D | RIO BRANCO DO SUL | PARANÁ | Brasil | 4122206 | 41 | 33 | nan | nan | nan | Mata Atlântica | 0.7 |


[Clique aqui para ver as próximas entradas](README5.md)
