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

## Dados Diários - Página 64

| ID | Latitude | Longitude | Data/Hora GMT | Satélite | Município | Estado | País | Município ID | Estado ID | País ID | Dias sem Chuva | Precipitação | Risco de Fogo | Bioma | FRP |
|----|----------|-----------|---------------|----------|-----------|--------|------|--------------|-----------|---------|----------------|--------------|----------------|-------|-----|
| 32e79149-f6c7-3c46-bd36-7ce8856ece2f | -10.62922 | -45.1852 | 2024-10-05 04:14:00 | NPP-375D | CRISTALÂNDIA DO PIAUÍ | PIAUÍ | Brasil | 2203008 | 22 | 33 | nan | nan | nan | Cerrado | 1.2 |
| aa3dd0d9-3f06-30e0-93ac-2e728a6a26a1 | -10.62133 | -45.19128 | 2024-10-05 04:14:00 | NPP-375D | CRISTALÂNDIA DO PIAUÍ | PIAUÍ | Brasil | 2203008 | 22 | 33 | nan | nan | nan | Cerrado | 1.3 |
| dabf723b-7ef5-346e-9cf8-7f9c123003b3 | -10.62075 | -45.19488 | 2024-10-05 04:14:00 | NPP-375D | CRISTALÂNDIA DO PIAUÍ | PIAUÍ | Brasil | 2203008 | 22 | 33 | nan | nan | nan | Cerrado | 1.9 |
| 0c7b24f0-e9dc-3404-9352-1c44ec5cfe53 | -10.61854 | -45.18713 | 2024-10-05 04:14:00 | NPP-375D | CRISTALÂNDIA DO PIAUÍ | PIAUÍ | Brasil | 2203008 | 22 | 33 | nan | nan | nan | Cerrado | 1.3 |
| cbdd9a18-fb7a-3268-b72a-508103af6665 | -10.48254 | -43.65282 | 2024-10-05 04:14:00 | NPP-375D | BURITIRAMA | BAHIA | Brasil | 2904753 | 29 | 33 | nan | nan | nan | Cerrado | 1.5 |
| 3624d3ec-e054-3818-9398-ee98a0dfede8 | -10.47976 | -43.64877 | 2024-10-05 04:14:00 | NPP-375D | BURITIRAMA | BAHIA | Brasil | 2904753 | 29 | 33 | nan | nan | nan | Cerrado | 0.8 |
| d35ac01f-a654-3dc0-a911-f54c27a7705f | -10.47921 | -43.65229 | 2024-10-05 04:14:00 | NPP-375D | BURITIRAMA | BAHIA | Brasil | 2904753 | 29 | 33 | nan | nan | nan | Cerrado | 0.8 |
| 92d5fa59-c37e-3a3c-bacc-f0b7912a021d | -10.47643 | -43.64824 | 2024-10-05 04:14:00 | NPP-375D | BURITIRAMA | BAHIA | Brasil | 2904753 | 29 | 33 | nan | nan | nan | Cerrado | 0.8 |
| dfbeaca6-1c8b-396c-ace6-85217270b925 | -10.43211 | -45.2832 | 2024-10-05 04:14:00 | NPP-375D | CORRENTE | PIAUÍ | Brasil | 2202901 | 22 | 33 | nan | nan | nan | Cerrado | 1.7 |
| 5d359616-cf93-311c-8672-83db7d05f030 | -10.37288 | -45.08828 | 2024-10-05 04:14:00 | NPP-375D | CORRENTE | PIAUÍ | Brasil | 2202901 | 22 | 33 | nan | nan | nan | Cerrado | 1.1 |
| f785c88d-213e-386b-8ade-ff5ea2548727 | -10.27947 | -45.46823 | 2024-10-05 04:14:00 | NPP-375D | SÃO GONÇALO DO GURGUÉIA | PIAUÍ | Brasil | 2209757 | 22 | 33 | nan | nan | nan | Cerrado | 5.8 |
| 21988bee-e918-328a-afcb-cb4602a1bf63 | -10.27887 | -45.47192 | 2024-10-05 04:14:00 | NPP-375D | SÃO GONÇALO DO GURGUÉIA | PIAUÍ | Brasil | 2209757 | 22 | 33 | nan | nan | nan | Cerrado | 5.8 |
| adfaef26-ed40-3757-9545-163b1df48f51 | -10.27828 | -45.47561 | 2024-10-05 04:14:00 | NPP-375D | SÃO GONÇALO DO GURGUÉIA | PIAUÍ | Brasil | 2209757 | 22 | 33 | nan | nan | nan | Cerrado | 2.2 |
| 08e97a0f-778f-3926-936b-b45ac3179ff2 | -10.27739 | -45.43784 | 2024-10-05 04:14:00 | NPP-375D | CORRENTE | PIAUÍ | Brasil | 2202901 | 22 | 33 | nan | nan | nan | Cerrado | 4.3 |
| 57858e1f-d8e9-311e-943f-d31875fc73b6 | -10.27665 | -45.46412 | 2024-10-05 04:14:00 | NPP-375D | SÃO GONÇALO DO GURGUÉIA | PIAUÍ | Brasil | 2209757 | 22 | 33 | nan | nan | nan | Cerrado | 1.7 |
| f44df35d-4089-303e-bf72-81962f1b5bbd | -10.27605 | -45.46781 | 2024-10-05 04:14:00 | NPP-375D | SÃO GONÇALO DO GURGUÉIA | PIAUÍ | Brasil | 2209757 | 22 | 33 | nan | nan | nan | Cerrado | 5.8 |
| 35de4f2d-76fb-373e-bdd0-aa08969c8965 | -10.27546 | -45.4715 | 2024-10-05 04:14:00 | NPP-375D | SÃO GONÇALO DO GURGUÉIA | PIAUÍ | Brasil | 2209757 | 22 | 33 | nan | nan | nan | Cerrado | 5.8 |
| f46b6e9c-a69a-3a95-bed3-1741f46422e1 | -10.27263 | -45.4674 | 2024-10-05 04:14:00 | NPP-375D | SÃO GONÇALO DO GURGUÉIA | PIAUÍ | Brasil | 2209757 | 22 | 33 | nan | nan | nan | Cerrado | 1.4 |
| aad42622-ba7c-3e15-9ac4-6139250de81a | -10.27204 | -45.47108 | 2024-10-05 04:14:00 | NPP-375D | SÃO GONÇALO DO GURGUÉIA | PIAUÍ | Brasil | 2209757 | 22 | 33 | nan | nan | nan | Cerrado | 1.4 |
| f7bc82f3-1472-3c8b-b754-29390fbbcfac | -14.19997 | -46.47745 | 2024-10-05 04:14:00 | NPP-375D | POSSE | GOIÁS | Brasil | 5218300 | 52 | 33 | nan | nan | nan | Cerrado | 1.5 |
| b83c2d6e-4e3f-3de5-a9e1-09bea1f0ca0a | -14.19935 | -46.48122 | 2024-10-05 04:14:00 | NPP-375D | POSSE | GOIÁS | Brasil | 5218300 | 52 | 33 | nan | nan | nan | Cerrado | 2.0 |
| b7a32e09-9df5-32c0-9ac6-5dec1713a252 | -14.19656 | -46.47689 | 2024-10-05 04:14:00 | NPP-375D | POSSE | GOIÁS | Brasil | 5218300 | 52 | 33 | nan | nan | nan | Cerrado | 2.4 |
| ec69327d-6a3c-3350-94d7-1078f625792e | -14.19594 | -46.48068 | 2024-10-05 04:14:00 | NPP-375D | POSSE | GOIÁS | Brasil | 5218300 | 52 | 33 | nan | nan | nan | Cerrado | 1.3 |
| 18c2bf39-d6c4-3b40-b18d-4b52442bae48 | -14.19532 | -46.48446 | 2024-10-05 04:14:00 | NPP-375D | POSSE | GOIÁS | Brasil | 5218300 | 52 | 33 | nan | nan | nan | Cerrado | 1.3 |
| 4a19b70a-2339-32b3-bca2-532b24134b5a | -14.19252 | -46.48011 | 2024-10-05 04:14:00 | NPP-375D | POSSE | GOIÁS | Brasil | 5218300 | 52 | 33 | nan | nan | nan | Cerrado | 1.3 |
| 860f31a7-6b2e-3afb-a9e9-8beaeec27568 | -14.1919 | -46.48389 | 2024-10-05 04:14:00 | NPP-375D | POSSE | GOIÁS | Brasil | 5218300 | 52 | 33 | nan | nan | nan | Cerrado | 1.3 |
| 0ae88ebb-1128-3bbd-978e-38ae6ca1f6f6 | -14.04918 | -46.37471 | 2024-10-05 04:14:00 | NPP-375D | POSSE | GOIÁS | Brasil | 5218300 | 52 | 33 | nan | nan | nan | Cerrado | 1.8 |
| 40bb9c78-2311-3d24-91e0-487467eb3463 | -14.04764 | -46.3629 | 2024-10-05 04:14:00 | NPP-375D | POSSE | GOIÁS | Brasil | 5218300 | 52 | 33 | nan | nan | nan | Cerrado | 0.7 |
| 790b5ca1-c8e1-3edb-ab9b-9b2ee9f585a1 | -14.04702 | -46.36661 | 2024-10-05 04:14:00 | NPP-375D | POSSE | GOIÁS | Brasil | 5218300 | 52 | 33 | nan | nan | nan | Cerrado | 0.7 |
| 87a32a83-acfe-3ff9-8884-039fa1f8de3e | -14.04578 | -46.3741 | 2024-10-05 04:14:00 | NPP-375D | POSSE | GOIÁS | Brasil | 5218300 | 52 | 33 | nan | nan | nan | Cerrado | 1.8 |
| 41e85f1b-619a-3935-b1e2-b619b1e7931f | -14.04516 | -46.37787 | 2024-10-05 04:14:00 | NPP-375D | POSSE | GOIÁS | Brasil | 5218300 | 52 | 33 | nan | nan | nan | Cerrado | 1.3 |
| 64d9fe23-f3f7-3880-ac19-69a6f424cb91 | -14.04424 | -46.3623 | 2024-10-05 04:14:00 | NPP-375D | POSSE | GOIÁS | Brasil | 5218300 | 52 | 33 | nan | nan | nan | Cerrado | 1.4 |
| a94782ea-f9c2-3919-9d35-db577186faaf | -13.14698 | -46.35579 | 2024-10-05 04:14:00 | NPP-375D | SÃO DOMINGOS | GOIÁS | Brasil | 5219803 | 52 | 33 | nan | nan | nan | Cerrado | 2.2 |
| dbed56cc-074c-3355-9d6a-97fcbd2d8f2d | -13.14418 | -46.35141 | 2024-10-05 04:14:00 | NPP-375D | SÃO DOMINGOS | GOIÁS | Brasil | 5219803 | 52 | 33 | nan | nan | nan | Cerrado | 2.2 |
| 95d84924-5149-3795-9916-1f932504cdc2 | -13.14356 | -46.35519 | 2024-10-05 04:14:00 | NPP-375D | SÃO DOMINGOS | GOIÁS | Brasil | 5219803 | 52 | 33 | nan | nan | nan | Cerrado | 2.2 |
| 051c8738-02c2-338f-9ab4-3c482e8cd3fa | -13.11782 | -46.31932 | 2024-10-05 04:14:00 | NPP-375D | SÃO DOMINGOS | GOIÁS | Brasil | 5219803 | 52 | 33 | nan | nan | nan | Cerrado | 1.8 |
| 76814489-3128-3a9b-82ed-e1d6b968c3f7 | -13.11776 | -46.3624 | 2024-10-05 04:14:00 | NPP-375D | SÃO DOMINGOS | GOIÁS | Brasil | 5219803 | 52 | 33 | nan | nan | nan | Cerrado | 1.6 |
| c1fc3b43-cc22-3241-aed7-d6bcc62f42bd | -13.11718 | -46.32321 | 2024-10-05 04:14:00 | NPP-375D | SÃO DOMINGOS | GOIÁS | Brasil | 5219803 | 52 | 33 | nan | nan | nan | Cerrado | 12.2 |
| 51d0a795-2fbb-3443-bd9a-f62b0aaa59c5 | -13.11654 | -46.32712 | 2024-10-05 04:14:00 | NPP-375D | SÃO DOMINGOS | GOIÁS | Brasil | 5219803 | 52 | 33 | nan | nan | nan | Cerrado | 12.2 |
| d47a73c0-12bb-3a91-8f6b-db5ae5c8d299 | -13.1159 | -46.33097 | 2024-10-05 04:14:00 | NPP-375D | SÃO DOMINGOS | GOIÁS | Brasil | 5219803 | 52 | 33 | nan | nan | nan | Cerrado | 4.3 |
| 5956b886-5000-30dd-a831-238c02bc44b7 | -13.11434 | -46.36182 | 2024-10-05 04:14:00 | NPP-375D | SÃO DOMINGOS | GOIÁS | Brasil | 5219803 | 52 | 33 | nan | nan | nan | Cerrado | 1.6 |
| 5899fcd3-e710-321a-9df9-d49ee1d4c49f | -13.11377 | -46.32258 | 2024-10-05 04:14:00 | NPP-375D | SÃO DOMINGOS | GOIÁS | Brasil | 5219803 | 52 | 33 | nan | nan | nan | Cerrado | 12.2 |
| 08c01dbc-cfd7-364c-b0a7-55c4e13e4be0 | -13.11372 | -46.3656 | 2024-10-05 04:14:00 | NPP-375D | SÃO DOMINGOS | GOIÁS | Brasil | 5219803 | 52 | 33 | nan | nan | nan | Cerrado | 1.6 |
| 9466296a-74b8-3ced-8756-78777a7725e9 | -13.11313 | -46.3265 | 2024-10-05 04:14:00 | NPP-375D | SÃO DOMINGOS | GOIÁS | Brasil | 5219803 | 52 | 33 | nan | nan | nan | Cerrado | 12.2 |
| a5665d9d-f3e3-3975-b2fd-1f84df52c697 | -13.1131 | -46.36937 | 2024-10-05 04:14:00 | NPP-375D | SÃO DOMINGOS | GOIÁS | Brasil | 5219803 | 52 | 33 | nan | nan | nan | Cerrado | 6.4 |
| e1b82569-d67d-34ac-b467-28836d029021 | -13.11249 | -46.33037 | 2024-10-05 04:14:00 | NPP-375D | SÃO DOMINGOS | GOIÁS | Brasil | 5219803 | 52 | 33 | nan | nan | nan | Cerrado | 4.3 |
| b81fd420-8c3f-32fb-ad56-3ea97bb6da4e | -13.11247 | -46.37315 | 2024-10-05 04:14:00 | NPP-375D | SÃO DOMINGOS | GOIÁS | Brasil | 5219803 | 52 | 33 | nan | nan | nan | Cerrado | 6.4 |
| 21b091f1-e785-368b-8192-10476a97b250 | -13.11217 | -46.35367 | 2024-10-05 04:14:00 | NPP-375D | SÃO DOMINGOS | GOIÁS | Brasil | 5219803 | 52 | 33 | nan | nan | nan | Cerrado | 3.1 |
| adc1a401-d712-316f-91a2-4f24ab06134c | -13.11187 | -46.33414 | 2024-10-05 04:14:00 | NPP-375D | SÃO DOMINGOS | GOIÁS | Brasil | 5219803 | 52 | 33 | nan | nan | nan | Cerrado | 4.3 |
| 467bdffe-418c-3650-87af-4747b665ebe4 | -13.11154 | -46.35745 | 2024-10-05 04:14:00 | NPP-375D | SÃO DOMINGOS | GOIÁS | Brasil | 5219803 | 52 | 33 | nan | nan | nan | Cerrado | 3.1 |
| 85ea9376-f058-38bb-929f-3b2d32bdab57 | -13.11125 | -46.33791 | 2024-10-05 04:14:00 | NPP-375D | SÃO DOMINGOS | GOIÁS | Brasil | 5219803 | 52 | 33 | nan | nan | nan | Cerrado | 2.5 |
| 9209a722-fe48-314a-8375-8e70e65175a4 | -13.11092 | -46.36123 | 2024-10-05 04:14:00 | NPP-375D | SÃO DOMINGOS | GOIÁS | Brasil | 5219803 | 52 | 33 | nan | nan | nan | Cerrado | 5.6 |
| 5839c029-313a-3100-a623-23026511c9ec | -13.11037 | -46.32191 | 2024-10-05 04:14:00 | NPP-375D | SÃO DOMINGOS | GOIÁS | Brasil | 5219803 | 52 | 33 | nan | nan | nan | Cerrado | 3.3 |
| ea949e8d-514c-36fd-ba9f-e8b9bd6b7fa2 | -13.1103 | -46.36501 | 2024-10-05 04:14:00 | NPP-375D | SÃO DOMINGOS | GOIÁS | Brasil | 5219803 | 52 | 33 | nan | nan | nan | Cerrado | 5.6 |
| ed8fa4f0-142d-3fcb-90df-cca020207477 | -13.10968 | -46.36878 | 2024-10-05 04:14:00 | NPP-375D | SÃO DOMINGOS | GOIÁS | Brasil | 5219803 | 52 | 33 | nan | nan | nan | Cerrado | 2.7 |
| 92d139fb-5a75-309b-b748-10d5d9060a17 | -13.10938 | -46.34926 | 2024-10-05 04:14:00 | NPP-375D | SÃO DOMINGOS | GOIÁS | Brasil | 5219803 | 52 | 33 | nan | nan | nan | Cerrado | 3.0 |
| 4542a935-bc8b-364d-aa98-1096b81c0ba6 | -13.10905 | -46.37255 | 2024-10-05 04:14:00 | NPP-375D | SÃO DOMINGOS | GOIÁS | Brasil | 5219803 | 52 | 33 | nan | nan | nan | Cerrado | 2.7 |
| 7c67da8a-c361-3c68-905f-97f12a28e1fe | -13.10875 | -46.35307 | 2024-10-05 04:14:00 | NPP-375D | SÃO DOMINGOS | GOIÁS | Brasil | 5219803 | 52 | 33 | nan | nan | nan | Cerrado | 3.1 |
| 7cd4b916-cee9-3fa0-b286-2f6923c80ab7 | -13.10847 | -46.33345 | 2024-10-05 04:14:00 | NPP-375D | SÃO DOMINGOS | GOIÁS | Brasil | 5219803 | 52 | 33 | nan | nan | nan | Cerrado | 3.2 |
| 1ac32338-dde0-313a-a783-0d9f1913cf0d | -13.10812 | -46.35686 | 2024-10-05 04:14:00 | NPP-375D | SÃO DOMINGOS | GOIÁS | Brasil | 5219803 | 52 | 33 | nan | nan | nan | Cerrado | 3.1 |
| 343190ff-0899-36a0-91d8-577224193a1e | -13.10785 | -46.33721 | 2024-10-05 04:14:00 | NPP-375D | SÃO DOMINGOS | GOIÁS | Brasil | 5219803 | 52 | 33 | nan | nan | nan | Cerrado | 4.6 |
| a7d096cd-602a-311c-959f-8aedaac84195 | -13.1076 | -46.31743 | 2024-10-05 04:14:00 | NPP-375D | SÃO DOMINGOS | GOIÁS | Brasil | 5219803 | 52 | 33 | nan | nan | nan | Cerrado | 1.9 |
| 59c52403-e776-3af8-abd2-9ae775b76838 | -13.1075 | -46.36064 | 2024-10-05 04:14:00 | NPP-375D | SÃO DOMINGOS | GOIÁS | Brasil | 5219803 | 52 | 33 | nan | nan | nan | Cerrado | 5.6 |
| b87e877b-3b90-359f-938d-f1136ef3978a | -13.10722 | -46.34099 | 2024-10-05 04:14:00 | NPP-375D | SÃO DOMINGOS | GOIÁS | Brasil | 5219803 | 52 | 33 | nan | nan | nan | Cerrado | 4.6 |
| c31abf16-d431-357e-8903-4d4cce823053 | -13.10697 | -46.32125 | 2024-10-05 04:14:00 | NPP-375D | SÃO DOMINGOS | GOIÁS | Brasil | 5219803 | 52 | 33 | nan | nan | nan | Cerrado | 3.3 |
| 6e1b7592-2256-3f55-9e9f-8707b141f093 | -13.213 | -48.65946 | 2024-10-05 04:14:00 | NPP-375D | MONTIVIDIU DO NORTE | GOIÁS | Brasil | 5213772 | 52 | 33 | nan | nan | nan | Cerrado | 2.1 |
| 23c6af15-8e7e-3f99-bbf3-c46189d56441 | -13.21049 | -48.51988 | 2024-10-05 04:14:00 | NPP-375D | MINAÇU | GOIÁS | Brasil | 5213087 | 52 | 33 | nan | nan | nan | Cerrado | 2.7 |
| d671ded0-294d-324e-8573-4325de41bd26 | -13.2075 | -48.65111 | 2024-10-05 04:14:00 | NPP-375D | MONTIVIDIU DO NORTE | GOIÁS | Brasil | 5213772 | 52 | 33 | nan | nan | nan | Cerrado | 3.8 |
| c4bfcc9e-d420-307a-b12e-f6d55cf47aec | -13.18531 | -48.66648 | 2024-10-05 04:14:00 | NPP-375D | MONTIVIDIU DO NORTE | GOIÁS | Brasil | 5213772 | 52 | 33 | nan | nan | nan | Cerrado | 3.7 |
| 1b5acb49-5dcd-3fa9-a42b-91889b01ce0a | -13.18212 | -48.61691 | 2024-10-05 04:14:00 | NPP-375D | MONTIVIDIU DO NORTE | GOIÁS | Brasil | 5213772 | 52 | 33 | nan | nan | nan | Cerrado | 2.6 |
| 300a5152-f15e-3aaa-b442-ad3d8c31ea0f | -13.17071 | -48.68299 | 2024-10-05 04:14:00 | NPP-375D | MONTIVIDIU DO NORTE | GOIÁS | Brasil | 5213772 | 52 | 33 | nan | nan | nan | Cerrado | 5.5 |
| d586c442-5d89-3d10-8191-95840f216dc7 | -13.1669 | -48.68235 | 2024-10-05 04:14:00 | NPP-375D | MONTIVIDIU DO NORTE | GOIÁS | Brasil | 5213772 | 52 | 33 | nan | nan | nan | Cerrado | 3.4 |
| ff64e4b0-9c79-3dbc-8caf-58f12244f4fe | -13.16309 | -48.68172 | 2024-10-05 04:14:00 | NPP-375D | MONTIVIDIU DO NORTE | GOIÁS | Brasil | 5213772 | 52 | 33 | nan | nan | nan | Cerrado | 3.4 |
| 55a85a80-0c32-3177-b5b4-962fa66dba81 | -7.72662 | -45.35496 | 2024-10-05 04:14:00 | NPP-375D | RIBEIRO GONÇALVES | PIAUÍ | Brasil | 2208908 | 22 | 33 | nan | nan | nan | Cerrado | 1.6 |
| d516f951-8da4-3123-b841-a56f54d14cef | -7.54753 | -45.14615 | 2024-10-05 04:14:00 | NPP-375D | RIBEIRO GONÇALVES | PIAUÍ | Brasil | 2208908 | 22 | 33 | nan | nan | nan | Cerrado | 2.6 |
| 77f24adc-8c54-30ab-8327-619eb958296a | -7.53731 | -43.65316 | 2024-10-05 04:14:00 | NPP-375D | CANAVIEIRA | PIAUÍ | Brasil | 2202251 | 22 | 33 | nan | nan | nan | Cerrado | 0.8 |
| 708017d3-0e17-3f43-a00e-e94d49a87e0b | -7.52424 | -44.96695 | 2024-10-05 04:14:00 | NPP-375D | URUÇUÍ | PIAUÍ | Brasil | 2211209 | 22 | 33 | nan | nan | nan | Cerrado | 1.4 |
| cdc1f755-bf41-3422-8a89-6989d3b6762f | -7.52365 | -44.97066 | 2024-10-05 04:14:00 | NPP-375D | URUÇUÍ | PIAUÍ | Brasil | 2211209 | 22 | 33 | nan | nan | nan | Cerrado | 1.4 |
| 248782c9-67b3-3848-8067-ddbd02af9e5e | -7.52083 | -44.96641 | 2024-10-05 04:14:00 | NPP-375D | URUÇUÍ | PIAUÍ | Brasil | 2211209 | 22 | 33 | nan | nan | nan | Cerrado | 1.4 |
| bdd4a564-b9fe-3d70-8155-2431717c356d | -7.52023 | -44.97013 | 2024-10-05 04:14:00 | NPP-375D | URUÇUÍ | PIAUÍ | Brasil | 2211209 | 22 | 33 | nan | nan | nan | Cerrado | 1.4 |
| 26bc258b-7d1d-3be8-a742-ed0e2d1c4a56 | -7.50345 | -44.83553 | 2024-10-05 04:14:00 | NPP-375D | URUÇUÍ | PIAUÍ | Brasil | 2211209 | 22 | 33 | nan | nan | nan | Cerrado | 3.4 |
| f4146343-aaac-3ebb-9937-9df35e6e0a10 | -7.50063 | -44.83134 | 2024-10-05 04:14:00 | NPP-375D | URUÇUÍ | PIAUÍ | Brasil | 2211209 | 22 | 33 | nan | nan | nan | Cerrado | 3.5 |
| d6590ba0-fae7-35e6-a5c4-de25f7274b49 | -7.49723 | -44.83082 | 2024-10-05 04:14:00 | NPP-375D | URUÇUÍ | PIAUÍ | Brasil | 2211209 | 22 | 33 | nan | nan | nan | Cerrado | 1.2 |
| cb392b03-4bdd-323b-a422-d917cea4cf99 | -7.49382 | -44.8303 | 2024-10-05 04:14:00 | NPP-375D | URUÇUÍ | PIAUÍ | Brasil | 2211209 | 22 | 33 | nan | nan | nan | Cerrado | 1.2 |
| ad189263-2971-31bc-8314-b23845abe964 | -7.44265 | -44.73652 | 2024-10-05 04:14:00 | NPP-375D | URUÇUÍ | PIAUÍ | Brasil | 2211209 | 22 | 33 | nan | nan | nan | Cerrado | 5.8 |
| 2b4ecd86-8d5e-39e8-81bd-cb892f9cbee5 | -7.44207 | -44.74016 | 2024-10-05 04:14:00 | NPP-375D | URUÇUÍ | PIAUÍ | Brasil | 2211209 | 22 | 33 | nan | nan | nan | Cerrado | 5.8 |
| 2c68bde2-1aba-3d34-9264-2befec379cc0 | -7.4413 | -44.00034 | 2024-10-05 04:14:00 | NPP-375D | SEBASTIÃO LEAL | PIAUÍ | Brasil | 2210631 | 22 | 33 | nan | nan | nan | Cerrado | 0.8 |
| 112705e0-f80e-3129-b62d-b297f59b5f08 | -7.43851 | -43.99629 | 2024-10-05 04:14:00 | NPP-375D | SEBASTIÃO LEAL | PIAUÍ | Brasil | 2210631 | 22 | 33 | nan | nan | nan | Cerrado | 0.8 |
| 0231893c-2d38-3836-88cd-abbd5c40ec03 | -7.43796 | -43.99981 | 2024-10-05 04:14:00 | NPP-375D | SEBASTIÃO LEAL | PIAUÍ | Brasil | 2210631 | 22 | 33 | nan | nan | nan | Cerrado | 0.8 |
| 45bafa86-65f1-3149-97d3-92af4e36e604 | -14.29414 | -48.1699 | 2024-10-05 04:14:00 | NPP-375D | NIQUELÂNDIA | GOIÁS | Brasil | 5214606 | 52 | 33 | nan | nan | nan | Cerrado | 2.1 |
| 35dd3d1c-e49d-3be3-8584-d02441e2b536 | -14.28975 | -48.17356 | 2024-10-05 04:14:00 | NPP-375D | NIQUELÂNDIA | GOIÁS | Brasil | 5214606 | 52 | 33 | nan | nan | nan | Cerrado | 2.1 |
| 1a5e239d-8a9b-3a69-9d1a-ea79ddffcc9b | -14.28611 | -48.17289 | 2024-10-05 04:14:00 | NPP-375D | NIQUELÂNDIA | GOIÁS | Brasil | 5214606 | 52 | 33 | nan | nan | nan | Cerrado | 3.0 |
| 18694193-68d7-3ccf-bc7b-64ae8e245c73 | -14.28247 | -48.17223 | 2024-10-05 04:14:00 | NPP-375D | NIQUELÂNDIA | GOIÁS | Brasil | 5214606 | 52 | 33 | nan | nan | nan | Cerrado | 3.0 |
| d2f7b25e-8a73-366c-a62a-b7dc3c052883 | -14.00737 | -47.27024 | 2024-10-05 04:14:00 | NPP-375D | ALTO PARAÍSO DE GOIÁS | GOIÁS | Brasil | 5200605 | 52 | 33 | nan | nan | nan | Cerrado | 23.8 |
| 157c9713-8f77-3ce1-a099-b1eca43ed36b | -14.00667 | -47.27436 | 2024-10-05 04:14:00 | NPP-375D | ALTO PARAÍSO DE GOIÁS | GOIÁS | Brasil | 5200605 | 52 | 33 | nan | nan | nan | Cerrado | 8.4 |
| cee2c9fe-9fdb-35b6-b7ec-018fd2ec06bf | -14.00456 | -47.26553 | 2024-10-05 04:14:00 | NPP-375D | ALTO PARAÍSO DE GOIÁS | GOIÁS | Brasil | 5200605 | 52 | 33 | nan | nan | nan | Cerrado | 23.8 |
| 281afb75-7437-3b94-a567-723ebe97db5d | -14.00387 | -47.26958 | 2024-10-05 04:14:00 | NPP-375D | ALTO PARAÍSO DE GOIÁS | GOIÁS | Brasil | 5200605 | 52 | 33 | nan | nan | nan | Cerrado | 23.8 |
| 33d4a3f2-c0e7-33cf-b092-3996efc2f850 | -14.00318 | -47.27365 | 2024-10-05 04:14:00 | NPP-375D | ALTO PARAÍSO DE GOIÁS | GOIÁS | Brasil | 5200605 | 52 | 33 | nan | nan | nan | Cerrado | 8.4 |
| 8de3bfef-2c81-30e8-af71-9a1f51653991 | -14.00106 | -47.2649 | 2024-10-05 04:14:00 | NPP-375D | ALTO PARAÍSO DE GOIÁS | GOIÁS | Brasil | 5200605 | 52 | 33 | nan | nan | nan | Cerrado | 3.0 |
| 6fa07974-7be2-30e4-b645-4972be4f64d1 | -14.00087 | -47.26617 | 2024-10-05 04:14:00 | NPP-375D | ALTO PARAÍSO DE GOIÁS | GOIÁS | Brasil | 5200605 | 52 | 33 | nan | nan | nan | Cerrado | 3.1 |


[Clique aqui para ver as próximas entradas](README65.md)
