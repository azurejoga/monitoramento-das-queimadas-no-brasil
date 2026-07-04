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

## Dados Diários - Página 12

| ID | Latitude | Longitude | Data/Hora GMT | Satélite | Município | Estado | País | Município ID | Estado ID | País ID | Dias sem Chuva | Precipitação | Risco de Fogo | Bioma | FRP |
|----|----------|-----------|---------------|----------|-----------|--------|------|--------------|-----------|---------|----------------|--------------|----------------|-------|-----|
| ae820a45-0f8e-3fc1-b7c2-dd604c7525fb | -10.9401 | -43.0355 | 2026-07-04 04:40:00 | GOES-19 | BARRA | BAHIA | Brasil | 2902708 | 29 | 33 | nan | nan | nan | Cerrado | 239.5 |
| a877e540-c1b7-3667-932f-df39dde36da3 | -12.7548 | -44.5428 | 2026-07-04 04:40:00 | GOES-19 | BAIANÓPOLIS | BAHIA | Brasil | 2902500 | 29 | 33 | nan | nan | nan | Cerrado | 211.4 |
| 57c2c5d4-f69a-3735-9dbb-23030b35ac14 | -12.7741 | -44.5396 | 2026-07-04 04:40:00 | GOES-19 | BAIANÓPOLIS | BAHIA | Brasil | 2902500 | 29 | 33 | nan | nan | nan | Cerrado | 64.9 |
| e5b951a7-e8d6-30cc-9517-bf1c64396781 | -10.9205 | -43.0622 | 2026-07-04 04:40:00 | GOES-19 | BARRA | BAHIA | Brasil | 2902708 | 29 | 33 | nan | nan | nan | Cerrado | 163.0 |
| e8b7ba85-a3e6-3777-9112-07b402b2f4f3 | -13.2209 | -54.353 | 2026-07-04 04:40:00 | GOES-19 | PARANATINGA | MATO GROSSO | Brasil | 5106307 | 51 | 33 | nan | nan | nan | Amazônia | 70.6 |
| 100d9b1c-a5b2-3237-bf9f-75d6587d94a2 | -3.87677 | -42.97532 | 2026-07-04 04:44:00 | NOAA-21 | BURITI | MARANHÃO | Brasil | 2102200 | 21 | 33 | nan | nan | nan | Cerrado | 2.7 |
| b3d8e3bf-6020-3a0a-a7e7-984b9b1affc7 | -4.66592 | -43.21469 | 2026-07-04 04:44:00 | NOAA-21 | ALDEIAS ALTAS | MARANHÃO | Brasil | 2100303 | 21 | 33 | nan | nan | nan | Cerrado | 1.0 |
| 82ece6ea-a1b1-3f9e-b269-777367a34ce4 | -3.42013 | -41.71152 | 2026-07-04 04:44:00 | NOAA-21 | BURITI DOS LOPES | PIAUÍ | Brasil | 2202000 | 22 | 33 | nan | nan | nan | Caatinga | 3.5 |
| d1ec8bc0-25c4-388c-aad4-0eed96b512c0 | -3.51175 | -48.03895 | 2026-07-04 04:44:00 | NOAA-21 | PARAGOMINAS | PARÁ | Brasil | 1505502 | 15 | 33 | nan | nan | nan | Amazônia | 5.3 |
| 2e6095d1-8f7b-317f-a975-636ed1f2ffca | -3.98162 | -48.43105 | 2026-07-04 04:44:00 | NOAA-21 | GOIANÉSIA DO PARÁ | PARÁ | Brasil | 1503093 | 15 | 33 | nan | nan | nan | Amazônia | 0.6 |
| 36d207cc-b6c5-3ebb-a025-8a9e24074104 | -5.3199 | -43.56457 | 2026-07-04 04:44:00 | NOAA-21 | MATÕES | MARANHÃO | Brasil | 2106607 | 21 | 33 | nan | nan | nan | Cerrado | 7.3 |
| 9a5b281d-3260-310c-ae17-6f2c217adb19 | -5.31525 | -43.56393 | 2026-07-04 04:44:00 | NOAA-21 | MATÕES | MARANHÃO | Brasil | 2106607 | 21 | 33 | nan | nan | nan | Cerrado | 7.3 |
| 9d58bc19-0b48-3903-9bfd-585423e927b1 | -3.42571 | -41.7092 | 2026-07-04 04:44:00 | NOAA-21 | BURITI DOS LOPES | PIAUÍ | Brasil | 2202000 | 22 | 33 | nan | nan | nan | Caatinga | 3.5 |
| 8324dc5f-103f-3133-a11b-eaf87761dbcf | -3.9948 | -48.39123 | 2026-07-04 04:44:00 | NOAA-21 | GOIANÉSIA DO PARÁ | PARÁ | Brasil | 1503093 | 15 | 33 | nan | nan | nan | Amazônia | 2.4 |
| 92bfd2a5-d843-3fec-8356-632f940afea8 | -2.43303 | -47.03027 | 2026-07-04 04:44:00 | NOAA-21 | NOVA ESPERANÇA DO PIRIÁ | PARÁ | Brasil | 1504950 | 15 | 33 | nan | nan | nan | Amazônia | 1.5 |
| 397593b9-1939-3c63-8388-dbfb9a50ae78 | -4.34256 | -48.95515 | 2026-07-04 04:44:00 | NOAA-21 | GOIANÉSIA DO PARÁ | PARÁ | Brasil | 1503093 | 15 | 33 | nan | nan | nan | Amazônia | 2.1 |
| 1def8264-e3d4-3e18-813b-97c4eb21609d | -4.34939 | -47.76653 | 2026-07-04 04:44:00 | NOAA-21 | DOM ELISEU | PARÁ | Brasil | 1502939 | 15 | 33 | nan | nan | nan | Amazônia | 13.8 |
| 3357d6c0-f229-31b4-86a0-2aa14874a0fb | -3.42437 | -41.7183 | 2026-07-04 04:44:00 | NOAA-21 | BURITI DOS LOPES | PIAUÍ | Brasil | 2202000 | 22 | 33 | nan | nan | nan | Caatinga | 2.7 |
| edeba0bb-b756-31aa-9922-27dcc40caefc | -4.291 | -48.35914 | 2026-07-04 04:44:00 | NOAA-21 | RONDON DO PARÁ | PARÁ | Brasil | 1506187 | 15 | 33 | nan | nan | nan | Amazônia | 6.2 |
| 2e6afb2b-1c73-32eb-abeb-68175205706e | -2.64672 | -47.98495 | 2026-07-04 04:44:00 | NOAA-21 | IPIXUNA DO PARÁ | PARÁ | Brasil | 1503457 | 15 | 33 | nan | nan | nan | Amazônia | 1.2 |
| 2570ce1d-1532-3a82-b848-3407dafe31a7 | -2.96881 | -48.99264 | 2026-07-04 04:44:00 | NOAA-21 | TAILÂNDIA | PARÁ | Brasil | 1507953 | 15 | 33 | nan | nan | nan | Amazônia | 0.5 |
| 340a84ee-f3d7-341f-96da-48b6b4a032e1 | -3.51578 | -48.03572 | 2026-07-04 04:44:00 | NOAA-21 | PARAGOMINAS | PARÁ | Brasil | 1505502 | 15 | 33 | nan | nan | nan | Amazônia | 1.3 |
| f3cf345f-de81-394f-ab91-f9430169d04f | -3.51521 | -48.03947 | 2026-07-04 04:44:00 | NOAA-21 | PARAGOMINAS | PARÁ | Brasil | 1505502 | 15 | 33 | nan | nan | nan | Amazônia | 1.0 |
| 736ed1a3-a325-3cf2-aff7-670b2b7b3abf | -4.6652 | -43.2198 | 2026-07-04 04:44:00 | NOAA-21 | ALDEIAS ALTAS | MARANHÃO | Brasil | 2100303 | 21 | 33 | nan | nan | nan | Cerrado | 2.3 |
| a7ab12f5-50ba-3294-98c7-9a608a4c33ab | -4.14671 | -48.83682 | 2026-07-04 04:44:00 | NOAA-21 | GOIANÉSIA DO PARÁ | PARÁ | Brasil | 1503093 | 15 | 33 | nan | nan | nan | Amazônia | 4.5 |
| 527dc79b-7231-3308-a2b1-fa2400a232a8 | -3.41588 | -41.7047 | 2026-07-04 04:44:00 | NOAA-21 | BURITI DOS LOPES | PIAUÍ | Brasil | 2202000 | 22 | 33 | nan | nan | nan | Caatinga | 2.0 |
| fc30ae8d-5891-3099-8977-bfe279dbf7de | -1.59015 | -50.43729 | 2026-07-04 04:44:00 | NOAA-21 | BREVES | PARÁ | Brasil | 1501808 | 15 | 33 | nan | nan | nan | Amazônia | 1.7 |
| f83a24f1-483b-343f-9318-6d7e88f129b4 | -4.28814 | -48.35485 | 2026-07-04 04:44:00 | NOAA-21 | RONDON DO PARÁ | PARÁ | Brasil | 1506187 | 15 | 33 | nan | nan | nan | Amazônia | 4.8 |
| ce72238a-f1b7-36f5-bbe9-69bdb50c6c9f | -2.99376 | -48.96399 | 2026-07-04 04:44:00 | NOAA-21 | TAILÂNDIA | PARÁ | Brasil | 1507953 | 15 | 33 | nan | nan | nan | Amazônia | 1.3 |
| 6de2f1d1-50ce-3e90-bb0e-67538c2ce48d | -3.41544 | -41.70774 | 2026-07-04 04:44:00 | NOAA-21 | BURITI DOS LOPES | PIAUÍ | Brasil | 2202000 | 22 | 33 | nan | nan | nan | Caatinga | 3.1 |
| 671279bf-8a93-322a-b38f-5e29567c18dd | -3.8344 | -49.1367 | 2026-07-04 04:44:00 | NOAA-21 | GOIANÉSIA DO PARÁ | PARÁ | Brasil | 1503093 | 15 | 33 | nan | nan | nan | Amazônia | 1.2 |
| 473f3633-36ab-3cef-96b3-e03feecc45a8 | -4.28756 | -48.35864 | 2026-07-04 04:44:00 | NOAA-21 | RONDON DO PARÁ | PARÁ | Brasil | 1506187 | 15 | 33 | nan | nan | nan | Amazônia | 4.8 |
| 156a6674-975d-38a1-8bd6-dc546ba60361 | -4.58071 | -48.02789 | 2026-07-04 04:44:00 | NOAA-21 | RONDON DO PARÁ | PARÁ | Brasil | 1506187 | 15 | 33 | nan | nan | nan | Amazônia | 3.7 |
| aee72432-cf2c-383c-8061-77ad60ddca29 | -3.42057 | -41.70849 | 2026-07-04 04:44:00 | NOAA-21 | BURITI DOS LOPES | PIAUÍ | Brasil | 2202000 | 22 | 33 | nan | nan | nan | Caatinga | 3.5 |
| dcbaefdb-b087-3043-a83e-5b02345d3233 | -4.66815 | -43.21805 | 2026-07-04 04:44:00 | NOAA-21 | ALDEIAS ALTAS | MARANHÃO | Brasil | 2100303 | 21 | 33 | nan | nan | nan | Cerrado | 2.1 |
| 02c613e9-79e5-3fa5-bd96-26ac91cdb012 | -3.28534 | -50.6962 | 2026-07-04 04:44:00 | NOAA-21 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 1.2 |
| 59060c66-24df-3216-912e-a815c4229d15 | -2.76582 | -48.57208 | 2026-07-04 04:44:00 | NOAA-21 | TAILÂNDIA | PARÁ | Brasil | 1507953 | 15 | 33 | nan | nan | nan | Amazônia | 1.3 |
| a2f265d3-cc03-35d4-8a0e-4e03b713b3ab | -3.5129 | -48.03138 | 2026-07-04 04:44:00 | NOAA-21 | PARAGOMINAS | PARÁ | Brasil | 1505502 | 15 | 33 | nan | nan | nan | Amazônia | 2.8 |
| 632d6093-8f5e-3d6e-b94e-b20a581f7cfd | -3.42526 | -41.71225 | 2026-07-04 04:44:00 | NOAA-21 | BURITI DOS LOPES | PIAUÍ | Brasil | 2202000 | 22 | 33 | nan | nan | nan | Caatinga | 3.5 |
| cb7e6dd3-ccb6-332b-9413-5a3e4f5c0623 | -4.01379 | -48.06312 | 2026-07-04 04:44:00 | NOAA-21 | DOM ELISEU | PARÁ | Brasil | 1502939 | 15 | 33 | nan | nan | nan | Amazônia | 2.8 |
| 6e04a36f-67de-3826-b201-cfa09233e81a | -4.34999 | -47.76256 | 2026-07-04 04:44:00 | NOAA-21 | DOM ELISEU | PARÁ | Brasil | 1502939 | 15 | 33 | nan | nan | nan | Amazônia | 5.1 |
| 54838961-9435-3e78-b298-2b0b88bc69f4 | -4.34587 | -47.76598 | 2026-07-04 04:44:00 | NOAA-21 | DOM ELISEU | PARÁ | Brasil | 1502939 | 15 | 33 | nan | nan | nan | Amazônia | 13.8 |
| 91c85909-b171-3938-b283-a0f5342f2e34 | -4.07054 | -48.95024 | 2026-07-04 04:44:00 | NOAA-21 | GOIANÉSIA DO PARÁ | PARÁ | Brasil | 1503093 | 15 | 33 | nan | nan | nan | Amazônia | 0.5 |
| b22c9e5b-c124-390f-b69d-27e7ffc8bc6a | -3.42393 | -41.72131 | 2026-07-04 04:44:00 | NOAA-21 | BURITI DOS LOPES | PIAUÍ | Brasil | 2202000 | 22 | 33 | nan | nan | nan | Caatinga | 1.3 |
| c243e432-8edb-3898-8c6b-fd25c8ca6b71 | -4.34647 | -47.762 | 2026-07-04 04:44:00 | NOAA-21 | DOM ELISEU | PARÁ | Brasil | 1502939 | 15 | 33 | nan | nan | nan | Amazônia | 5.1 |
| f373e264-b434-3cbd-82c6-525796ea3098 | -5.32059 | -43.55975 | 2026-07-04 04:44:00 | NOAA-21 | MATÕES | MARANHÃO | Brasil | 2106607 | 21 | 33 | nan | nan | nan | Cerrado | 7.3 |
| 198f09aa-461c-38ef-894e-d59b9b9f06ff | -5.31457 | -43.56863 | 2026-07-04 04:44:00 | NOAA-21 | MATÕES | MARANHÃO | Brasil | 2106607 | 21 | 33 | nan | nan | nan | Cerrado | 7.4 |
| b2155a91-0822-3034-a785-cf5e105954b7 | -4.33919 | -48.95465 | 2026-07-04 04:44:00 | NOAA-21 | GOIANÉSIA DO PARÁ | PARÁ | Brasil | 1503093 | 15 | 33 | nan | nan | nan | Amazônia | 2.5 |
| c24293b1-429e-3495-b7e2-06868429cc8c | -4.7754 | -46.39825 | 2026-07-04 04:44:00 | NOAA-21 | BURITICUPU | MARANHÃO | Brasil | 2102325 | 21 | 33 | nan | nan | nan | Amazônia | 1.5 |
| ef1b0770-e9a2-33a1-b6cf-9c3a6befbe91 | -3.99822 | -48.39175 | 2026-07-04 04:44:00 | NOAA-21 | GOIANÉSIA DO PARÁ | PARÁ | Brasil | 1503093 | 15 | 33 | nan | nan | nan | Amazônia | 2.4 |
| e8c32266-0960-310b-b9b0-033eae3bfdec | -3.4985 | -48.03777 | 2026-07-04 04:44:00 | NOAA-21 | PARAGOMINAS | PARÁ | Brasil | 1505502 | 15 | 33 | nan | nan | nan | Amazônia | 3.1 |
| beb36b32-d553-3d96-a003-4bf507c701bf | -4.29158 | -48.35536 | 2026-07-04 04:44:00 | NOAA-21 | RONDON DO PARÁ | PARÁ | Brasil | 1506187 | 15 | 33 | nan | nan | nan | Amazônia | 6.2 |
| 73f7dba0-53e7-393e-9212-c99d6da3e4ec | -3.50943 | -48.03564 | 2026-07-04 04:44:00 | NOAA-21 | PARAGOMINAS | PARÁ | Brasil | 1505502 | 15 | 33 | nan | nan | nan | Amazônia | 1.1 |
| 4631436e-ceee-3964-bf32-6809534e2369 | -3.41633 | -41.70165 | 2026-07-04 04:44:00 | NOAA-21 | BURITI DOS LOPES | PIAUÍ | Brasil | 2202000 | 22 | 33 | nan | nan | nan | Caatinga | 2.0 |
| 2c8e4171-7144-3277-8554-900999050ae2 | -2.36336 | -47.15192 | 2026-07-04 04:44:00 | NOAA-21 | GARRAFÃO DO NORTE | PARÁ | Brasil | 1503077 | 15 | 33 | nan | nan | nan | Amazônia | 1.3 |
| daf244b0-26b3-3efd-b9a5-985d9c720098 | -3.99844 | -48.39127 | 2026-07-04 04:44:00 | NOAA-21 | GOIANÉSIA DO PARÁ | PARÁ | Brasil | 1503093 | 15 | 33 | nan | nan | nan | Amazônia | 0.5 |
| f80a0a42-3c14-3c42-adb8-f975c39c59a5 | -3.42482 | -41.71528 | 2026-07-04 04:44:00 | NOAA-21 | BURITI DOS LOPES | PIAUÍ | Brasil | 2202000 | 22 | 33 | nan | nan | nan | Caatinga | 2.7 |
| b4ebc443-0063-3aa5-acbe-a85e3e9ad968 | -5.31594 | -43.55909 | 2026-07-04 04:44:00 | NOAA-21 | MATÕES | MARANHÃO | Brasil | 2106607 | 21 | 33 | nan | nan | nan | Cerrado | 7.3 |
| bab587b1-891d-3c52-adfa-0f8275671346 | -4.01033 | -48.06254 | 2026-07-04 04:44:00 | NOAA-21 | DOM ELISEU | PARÁ | Brasil | 1502939 | 15 | 33 | nan | nan | nan | Amazônia | 2.8 |
| bef4a613-b630-3a52-9826-41b66ee9bc19 | -3.50539 | -48.03886 | 2026-07-04 04:44:00 | NOAA-21 | PARAGOMINAS | PARÁ | Brasil | 1505502 | 15 | 33 | nan | nan | nan | Amazônia | 1.9 |
| aa715245-0261-3c7a-9b93-439030c809cd | -4.39622 | -43.30633 | 2026-07-04 04:44:00 | NOAA-21 | ALDEIAS ALTAS | MARANHÃO | Brasil | 2100303 | 21 | 33 | nan | nan | nan | Cerrado | 2.1 |
| 8243683f-a89a-3579-8999-f4f3937257ac | -2.76919 | -48.5726 | 2026-07-04 04:44:00 | NOAA-21 | TAILÂNDIA | PARÁ | Brasil | 1507953 | 15 | 33 | nan | nan | nan | Amazônia | 4.5 |
| 7d3ddf7e-8a5d-37d8-9509-aae426032fa7 | -4.29216 | -48.35159 | 2026-07-04 04:44:00 | NOAA-21 | RONDON DO PARÁ | PARÁ | Brasil | 1506187 | 15 | 33 | nan | nan | nan | Amazônia | 8.4 |
| f1bbcfe6-91d9-39a5-8d01-bdb26eb26a1e | -3.42102 | -41.70544 | 2026-07-04 04:44:00 | NOAA-21 | BURITI DOS LOPES | PIAUÍ | Brasil | 2202000 | 22 | 33 | nan | nan | nan | Caatinga | 3.2 |
| 71f8db4c-c1f1-3a41-841e-d411d2b958d6 | -2.64673 | -47.98417 | 2026-07-04 04:44:00 | NOAA-21 | IPIXUNA DO PARÁ | PARÁ | Brasil | 1503457 | 15 | 33 | nan | nan | nan | Amazônia | 1.0 |
| 07f75050-f76a-351f-bb89-5a33d5f11093 | -2.76638 | -48.56849 | 2026-07-04 04:44:00 | NOAA-21 | TAILÂNDIA | PARÁ | Brasil | 1507953 | 15 | 33 | nan | nan | nan | Amazônia | 1.3 |
| 2323ba8d-2f6d-3287-8bc9-f35f759fd585 | -4.14825 | -48.8374 | 2026-07-04 04:44:00 | NOAA-21 | GOIANÉSIA DO PARÁ | PARÁ | Brasil | 1503093 | 15 | 33 | nan | nan | nan | Amazônia | 0.7 |
| 965eccdb-bcbf-367b-8d52-83ddf3baf58b | -4.57781 | -48.02351 | 2026-07-04 04:44:00 | NOAA-21 | RONDON DO PARÁ | PARÁ | Brasil | 1506187 | 15 | 33 | nan | nan | nan | Amazônia | 2.9 |
| 613c7679-941f-3fe2-a9e8-63d648b90ba5 | -4.33864 | -48.95824 | 2026-07-04 04:44:00 | NOAA-21 | GOIANÉSIA DO PARÁ | PARÁ | Brasil | 1503093 | 15 | 33 | nan | nan | nan | Amazônia | 2.5 |
| de1407a0-cb9f-3d3b-af2d-7f15e9e6975a | -3.41969 | -41.71455 | 2026-07-04 04:44:00 | NOAA-21 | BURITI DOS LOPES | PIAUÍ | Brasil | 2202000 | 22 | 33 | nan | nan | nan | Caatinga | 2.7 |
| 916c2e35-cfa5-3250-bc1b-3c2e6c59dd34 | -2.76975 | -48.56901 | 2026-07-04 04:44:00 | NOAA-21 | TAILÂNDIA | PARÁ | Brasil | 1507953 | 15 | 33 | nan | nan | nan | Amazônia | 4.5 |
| 93d52545-ee87-34d8-877f-8aad547fdbb0 | -2.96492 | -52.64968 | 2026-07-04 04:44:00 | NOAA-21 | BRASIL NOVO | PARÁ | Brasil | 1501725 | 15 | 33 | nan | nan | nan | Amazônia | 1.8 |
| 140e1a30-b5e8-3e5b-8b05-93a0ea9331fa | -4.57722 | -48.02738 | 2026-07-04 04:44:00 | NOAA-21 | RONDON DO PARÁ | PARÁ | Brasil | 1506187 | 15 | 33 | nan | nan | nan | Amazônia | 2.9 |
| efec98a5-1089-38cf-9c0c-d5a7e3eeb160 | -4.85382 | -45.33124 | 2026-07-04 04:44:00 | NOAA-21 | LAGOA GRANDE DO MARANHÃO | MARANHÃO | Brasil | 2105963 | 21 | 33 | nan | nan | nan | Cerrado | 1.1 |
| 11f215bf-de48-36e4-8d6a-477305ee0f34 | -4.00688 | -48.06194 | 2026-07-04 04:44:00 | NOAA-21 | DOM ELISEU | PARÁ | Brasil | 1502939 | 15 | 33 | nan | nan | nan | Amazônia | 1.1 |
| 01c2db45-cf44-37ba-a6d2-68df495d6e4d | -4.3905 | -43.34528 | 2026-07-04 04:44:00 | NOAA-21 | ALDEIAS ALTAS | MARANHÃO | Brasil | 2100303 | 21 | 33 | nan | nan | nan | Cerrado | 1.0 |
| 51147926-e619-399a-adbc-61c4c04486b1 | -4.14334 | -48.83631 | 2026-07-04 04:44:00 | NOAA-21 | GOIANÉSIA DO PARÁ | PARÁ | Brasil | 1503093 | 15 | 33 | nan | nan | nan | Amazônia | 4.5 |
| e2b1ed0d-e746-325b-8b80-3e29644dbf6e | -3.50885 | -48.03939 | 2026-07-04 04:44:00 | NOAA-21 | PARAGOMINAS | PARÁ | Brasil | 1505502 | 15 | 33 | nan | nan | nan | Amazônia | 1.9 |
| d503efbb-db3d-3fee-a71d-4d2569a6f279 | -2.26531 | -47.00938 | 2026-07-04 04:44:00 | NOAA-21 | GARRAFÃO DO NORTE | PARÁ | Brasil | 1503077 | 15 | 33 | nan | nan | nan | Amazônia | 0.7 |
| f90016d3-03d7-3c2a-bb71-476dcc58de3f | -3.5083 | -48.03842 | 2026-07-04 04:44:00 | NOAA-21 | PARAGOMINAS | PARÁ | Brasil | 1505502 | 15 | 33 | nan | nan | nan | Amazônia | 5.3 |
| 611effee-37b2-3bd7-8462-0df44f3318e1 | -11.92319 | -43.38351 | 2026-07-04 04:46:00 | NOAA-21 | MUQUÉM DO SÃO FRANCISCO | BAHIA | Brasil | 2922250 | 29 | 33 | nan | nan | nan | Cerrado | 2.1 |
| ce52e8d3-bae1-3521-b9d7-6b38d2430c72 | -10.93292 | -43.05444 | 2026-07-04 04:46:00 | NOAA-21 | BARRA | BAHIA | Brasil | 2902708 | 29 | 33 | nan | nan | nan | Cerrado | 94.2 |
| cdbca70f-589c-3a29-b98a-04f26d8378e6 | -7.22961 | -47.11539 | 2026-07-04 04:46:00 | NOAA-21 | CAROLINA | MARANHÃO | Brasil | 2102804 | 21 | 33 | nan | nan | nan | Cerrado | 2.4 |
| 2c69ccb0-f2d9-357a-9ec6-fa09157c2007 | -9.66229 | -56.49684 | 2026-07-04 04:46:00 | NOAA-21 | PARANAÍTA | MATO GROSSO | Brasil | 5106299 | 51 | 33 | nan | nan | nan | Amazônia | 2.3 |
| 069394df-97af-32ff-a22c-8bdceb59f97a | -9.95476 | -52.20074 | 2026-07-04 04:46:00 | NOAA-21 | VILA RICA | MATO GROSSO | Brasil | 5108600 | 51 | 33 | nan | nan | nan | Amazônia | 0.9 |
| e32db767-f4fd-3675-b4a6-d8cf5924a77d | -8.03577 | -46.71508 | 2026-07-04 04:46:00 | NOAA-21 | CAMPOS LINDOS | TOCANTINS | Brasil | 1703842 | 17 | 33 | nan | nan | nan | Cerrado | 1.4 |
| 2bd35e7c-eefb-35de-abd9-e1a5d624a95b | -6.67025 | -47.9171 | 2026-07-04 04:46:00 | NOAA-21 | DARCINÓPOLIS | TOCANTINS | Brasil | 1706506 | 17 | 33 | nan | nan | nan | Cerrado | 1.4 |
| 618f667d-7431-3fde-9b63-de47b654c90c | -7.00538 | -42.77025 | 2026-07-04 04:46:00 | NOAA-21 | NAZARÉ DO PIAUÍ | PIAUÍ | Brasil | 2206704 | 22 | 33 | nan | nan | nan | Caatinga | 0.9 |
| 21c65767-cb1d-349a-993e-939b145bae43 | -10.12708 | -52.0994 | 2026-07-04 04:46:00 | NOAA-21 | SANTA CRUZ DO XINGU | MATO GROSSO | Brasil | 5107743 | 51 | 33 | nan | nan | nan | Amazônia | 2.4 |
| e20b95b6-2265-3df7-ab63-f27e094b5fb8 | -12.75021 | -44.5338 | 2026-07-04 04:46:00 | NOAA-21 | BAIANÓPOLIS | BAHIA | Brasil | 2902500 | 29 | 33 | nan | nan | nan | Cerrado | 8.5 |
| 6bb2622e-25b6-3831-ae21-92f855faa1c6 | -6.67087 | -47.913 | 2026-07-04 04:46:00 | NOAA-21 | DARCINÓPOLIS | TOCANTINS | Brasil | 1706506 | 17 | 33 | nan | nan | nan | Cerrado | 1.4 |
| 81782ab7-382d-38ec-bbfb-fa8ab64e26e2 | -10.12211 | -52.0879 | 2026-07-04 04:46:00 | NOAA-21 | SANTA CRUZ DO XINGU | MATO GROSSO | Brasil | 5107743 | 51 | 33 | nan | nan | nan | Amazônia | 1.4 |
| 1fe490e4-32d5-3067-b297-9b1aa9783c54 | -8.98874 | -47.74815 | 2026-07-04 04:46:00 | NOAA-21 | BOM JESUS DO TOCANTINS | TOCANTINS | Brasil | 1703305 | 17 | 33 | nan | nan | nan | Cerrado | 1.2 |
| 9f18147b-d75f-389d-bb30-05f7e20110b1 | -5.79446 | -45.05969 | 2026-07-04 04:46:00 | NOAA-21 | BARRA DO CORDA | MARANHÃO | Brasil | 2101608 | 21 | 33 | nan | nan | nan | Cerrado | 1.9 |
| ee435c81-8906-3411-9778-0bbd228aa423 | -9.44273 | -40.32101 | 2026-07-04 04:46:00 | NOAA-21 | JUAZEIRO | BAHIA | Brasil | 2918407 | 29 | 33 | nan | nan | nan | Caatinga | 10.2 |
| 69cfe33c-c7bb-3093-b2d3-dc7080b1e97c | -5.43771 | -44.65085 | 2026-07-04 04:46:00 | NOAA-21 | SANTA FILOMENA DO MARANHÃO | MARANHÃO | Brasil | 2109759 | 21 | 33 | nan | nan | nan | Cerrado | 1.8 |
| 5aae1800-6de6-340e-996c-d3e422b5bde6 | -12.75703 | -44.52847 | 2026-07-04 04:46:00 | NOAA-21 | BAIANÓPOLIS | BAHIA | Brasil | 2902500 | 29 | 33 | nan | nan | nan | Cerrado | 7.1 |
| 3788a88e-26f2-3e6b-b896-dead41662ae7 | -7.00845 | -42.78544 | 2026-07-04 04:46:00 | NOAA-21 | NAZARÉ DO PIAUÍ | PIAUÍ | Brasil | 2206704 | 22 | 33 | nan | nan | nan | Caatinga | 1.2 |
| 93c8ecf9-3f5f-379c-99b4-80bd2b08c1bc | -12.50906 | -48.25807 | 2026-07-04 04:46:00 | NOAA-21 | SÃO SALVADOR DO TOCANTINS | TOCANTINS | Brasil | 1720259 | 17 | 33 | nan | nan | nan | Cerrado | 1.4 |
| ad980c10-c0e0-3abe-87d7-d8838c300f43 | -8.08432 | -46.71471 | 2026-07-04 04:46:00 | NOAA-21 | CAMPOS LINDOS | TOCANTINS | Brasil | 1703842 | 17 | 33 | nan | nan | nan | Cerrado | 2.0 |


[Clique aqui para ver as próximas entradas](README13.md)
