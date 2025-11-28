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

## Dados Diários - Página 9

| ID | Latitude | Longitude | Data/Hora GMT | Satélite | Município | Estado | País | Município ID | Estado ID | País ID | Dias sem Chuva | Precipitação | Risco de Fogo | Bioma | FRP |
|----|----------|-----------|---------------|----------|-----------|--------|------|--------------|-----------|---------|----------------|--------------|----------------|-------|-----|
| cf9d3cda-a3d8-3342-9775-2ec763940a9e | -2.61848 | -47.35724 | 2025-11-28 04:31:00 | NOAA-21 | IPIXUNA DO PARÁ | PARÁ | Brasil | 1503457 | 15 | 33 | nan | nan | nan | Amazônia | 1.0 |
| 0786cbab-f714-3a68-aa65-7f47f0f5785e | -3.40612 | -54.57846 | 2025-11-28 04:31:00 | NOAA-21 | PLACAS | PARÁ | Brasil | 1505650 | 15 | 33 | nan | nan | nan | Amazônia | 7.6 |
| 418d1311-52aa-3cfa-b724-7abff37077b9 | -3.75884 | -46.96279 | 2025-11-28 04:31:00 | NOAA-21 | CENTRO NOVO DO MARANHÃO | MARANHÃO | Brasil | 2103174 | 21 | 33 | nan | nan | nan | Amazônia | 3.2 |
| dfed9520-b46f-3483-b7c9-13fe0431f295 | -3.76376 | -46.95298 | 2025-11-28 04:31:00 | NOAA-21 | CENTRO NOVO DO MARANHÃO | MARANHÃO | Brasil | 2103174 | 21 | 33 | nan | nan | nan | Amazônia | 2.9 |
| f8c0f8c6-06d2-3593-98ff-fdd1906e5bc6 | -2.71068 | -45.21368 | 2025-11-28 04:31:00 | NOAA-21 | PINHEIRO | MARANHÃO | Brasil | 2108603 | 21 | 33 | nan | nan | nan | Amazônia | 3.3 |
| 43153514-b1a0-3574-acc2-a1578ebf4025 | -3.67056 | -45.40378 | 2025-11-28 04:31:00 | NOAA-21 | SANTA INÊS | MARANHÃO | Brasil | 2109908 | 21 | 33 | nan | nan | nan | Amazônia | 11.6 |
| 2e59fe30-de07-30ef-baa9-790cde8ff126 | -3.66751 | -45.78171 | 2025-11-28 04:31:00 | NOAA-21 | ALTO ALEGRE DO PINDARÉ | MARANHÃO | Brasil | 2100477 | 21 | 33 | nan | nan | nan | Amazônia | 1.8 |
| 6e369fb8-431f-3374-b63b-1e67954f6108 | -4.34205 | -48.63678 | 2025-11-28 04:31:00 | NOAA-21 | RONDON DO PARÁ | PARÁ | Brasil | 1506187 | 15 | 33 | nan | nan | nan | Amazônia | 1.6 |
| add31d85-842e-39e6-915e-0246a796dcd0 | -3.56067 | -52.07465 | 2025-11-28 04:31:00 | NOAA-21 | SENADOR JOSÉ PORFÍRIO | PARÁ | Brasil | 1507805 | 15 | 33 | nan | nan | nan | Amazônia | 2.5 |
| e41c5f6f-7e01-353c-b77a-855bb0215235 | -2.98779 | -45.41984 | 2025-11-28 04:31:00 | NOAA-21 | PEDRO DO ROSÁRIO | MARANHÃO | Brasil | 2108256 | 21 | 33 | nan | nan | nan | Amazônia | 1.2 |
| 910c5225-1de8-343f-8dfc-84f61433fae2 | -2.01626 | -46.05363 | 2025-11-28 04:31:00 | NOAA-21 | JUNCO DO MARANHÃO | MARANHÃO | Brasil | 2105658 | 21 | 33 | nan | nan | nan | Amazônia | 0.6 |
| 2ff2b3f9-ad7d-3ac4-b806-ae360486f419 | -3.74616 | -46.95731 | 2025-11-28 04:31:00 | NOAA-21 | CENTRO NOVO DO MARANHÃO | MARANHÃO | Brasil | 2103174 | 21 | 33 | nan | nan | nan | Amazônia | 1.9 |
| 78a8f3eb-9a66-33cc-8e6f-15af35626840 | -4.1405 | -50.64989 | 2025-11-28 04:31:00 | NOAA-21 | NOVO REPARTIMENTO | PARÁ | Brasil | 1505064 | 15 | 33 | nan | nan | nan | Amazônia | 0.5 |
| 5896102f-3c3e-3b1e-a403-750595901a6b | -2.77237 | -49.64235 | 2025-11-28 04:31:00 | NOAA-21 | BAIÃO | PARÁ | Brasil | 1501204 | 15 | 33 | nan | nan | nan | Amazônia | 3.6 |
| 6ad13c80-d5fe-3154-89c4-1557fb3a4e36 | -3.74313 | -50.03604 | 2025-11-28 04:31:00 | NOAA-21 | PACAJÁ | PARÁ | Brasil | 1505486 | 15 | 33 | nan | nan | nan | Amazônia | 0.7 |
| 4505acae-d300-3b19-a06e-9e918fba4f4b | -3.28052 | -53.76385 | 2025-11-28 04:31:00 | NOAA-21 | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | 1.0 |
| 38db459b-87d5-3522-86cb-fc09efb6a8b3 | -3.03761 | -50.97932 | 2025-11-28 04:31:00 | NOAA-21 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 5.8 |
| b6675830-0fd7-3159-829a-1e36e750b1b0 | -5.23326 | -44.92048 | 2025-11-28 04:31:00 | NOAA-21 | BARRA DO CORDA | MARANHÃO | Brasil | 2101608 | 21 | 33 | nan | nan | nan | Cerrado | 2.8 |
| 2bdfffb4-c499-3ad5-a99c-44fa16b26b46 | -2.62233 | -47.35431 | 2025-11-28 04:31:00 | NOAA-21 | IPIXUNA DO PARÁ | PARÁ | Brasil | 1503457 | 15 | 33 | nan | nan | nan | Amazônia | 5.0 |
| cb2d5788-f595-32cc-bed4-76d1a671940f | -2.6251 | -47.35826 | 2025-11-28 04:31:00 | NOAA-21 | IPIXUNA DO PARÁ | PARÁ | Brasil | 1503457 | 15 | 33 | nan | nan | nan | Amazônia | 1.0 |
| ce49453b-9756-3030-aeec-5a6359af7da5 | -2.71074 | -53.17891 | 2025-11-28 04:31:00 | NOAA-21 | MEDICILÂNDIA | PARÁ | Brasil | 1504455 | 15 | 33 | nan | nan | nan | Amazônia | 1.3 |
| 6f32c134-8974-3d43-8d4a-6b3f14551cf2 | -2.60964 | -47.34882 | 2025-11-28 04:31:00 | NOAA-21 | IPIXUNA DO PARÁ | PARÁ | Brasil | 1503457 | 15 | 33 | nan | nan | nan | Amazônia | 1.5 |
| 72834616-f5e2-300a-900d-09fe9bd0bb59 | -2.99062 | -45.42399 | 2025-11-28 04:31:00 | NOAA-21 | PEDRO DO ROSÁRIO | MARANHÃO | Brasil | 2108256 | 21 | 33 | nan | nan | nan | Amazônia | 1.8 |
| 94d31a7b-691f-3c83-8bc4-490ff0243904 | -2.56551 | -54.76174 | 2025-11-28 04:31:00 | NOAA-21 | SANTARÉM | PARÁ | Brasil | 1506807 | 15 | 33 | nan | nan | nan | Amazônia | 2.3 |
| ba0f070e-edb7-328a-8e4e-c429a826a0a3 | -3.75384 | -46.95144 | 2025-11-28 04:31:00 | NOAA-21 | CENTRO NOVO DO MARANHÃO | MARANHÃO | Brasil | 2103174 | 21 | 33 | nan | nan | nan | Amazônia | 1.7 |
| 2202e24f-1c31-31da-9e84-e3f852ffbbe9 | -2.6201 | -47.34692 | 2025-11-28 04:31:00 | NOAA-21 | IPIXUNA DO PARÁ | PARÁ | Brasil | 1503457 | 15 | 33 | nan | nan | nan | Amazônia | 1.4 |
| 8f182229-b13d-34c4-a3d3-50c1bcc81cd1 | -2.34715 | -47.15592 | 2025-11-28 04:31:00 | NOAA-21 | GARRAFÃO DO NORTE | PARÁ | Brasil | 1503077 | 15 | 33 | nan | nan | nan | Amazônia | 0.7 |
| 7f759fee-0197-34f0-9e37-8e60ee9f8e5a | -3.01351 | -51.15416 | 2025-11-28 04:31:00 | NOAA-21 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 1.9 |
| a4c5c5ce-a120-3ede-ac1c-3af53ab38b93 | -6.72221 | -40.82004 | 2025-11-28 04:31:00 | NOAA-21 | PIO IX | PIAUÍ | Brasil | 2208205 | 22 | 33 | nan | nan | nan | Caatinga | 5.0 |
| 2d669bb2-22b3-3889-b3e0-f248ac06614e | -2.75967 | -48.62056 | 2025-11-28 04:31:00 | NOAA-21 | TAILÂNDIA | PARÁ | Brasil | 1507953 | 15 | 33 | nan | nan | nan | Amazônia | 1.3 |
| e5be9377-9e8e-38d1-bc95-f1852f1f17d4 | -4.70891 | -48.31939 | 2025-11-28 04:31:00 | NOAA-21 | RONDON DO PARÁ | PARÁ | Brasil | 1506187 | 15 | 33 | nan | nan | nan | Amazônia | 0.4 |
| c749cbde-4c6b-37d2-bd97-79d563d34612 | -3.78656 | -52.37394 | 2025-11-28 04:31:00 | NOAA-21 | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 1.5 |
| dfaf40ba-9d4c-35c9-ab93-27578874f4b2 | -4.81137 | -43.09142 | 2025-11-28 04:31:00 | NOAA-21 | CAXIAS | MARANHÃO | Brasil | 2103000 | 21 | 33 | nan | nan | nan | Cerrado | 1.6 |
| 96cca893-7583-3d94-b38c-1bf1be08a91d | -3.43791 | -50.17179 | 2025-11-28 04:31:00 | NOAA-21 | PACAJÁ | PARÁ | Brasil | 1505486 | 15 | 33 | nan | nan | nan | Amazônia | 2.1 |
| 8478b751-297d-327e-b282-fd0d7c6279b3 | -3.75438 | -46.94801 | 2025-11-28 04:31:00 | NOAA-21 | CENTRO NOVO DO MARANHÃO | MARANHÃO | Brasil | 2103174 | 21 | 33 | nan | nan | nan | Amazônia | 0.9 |
| 28e05429-f528-336c-b23c-154c44d68d9e | -6.72749 | -40.81605 | 2025-11-28 04:31:00 | NOAA-21 | PIO IX | PIAUÍ | Brasil | 2208205 | 22 | 33 | nan | nan | nan | Caatinga | 4.1 |
| 14ce88b7-777c-322e-b3bd-f223d8aec384 | -4.56465 | -45.19808 | 2025-11-28 04:31:00 | NOAA-21 | PAULO RAMOS | MARANHÃO | Brasil | 2108108 | 21 | 33 | nan | nan | nan | Amazônia | 1.7 |
| 118c7d4d-69e3-3c61-9f65-7dd7f0f826fa | -3.4513 | -50.54942 | 2025-11-28 04:31:00 | NOAA-21 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 3.4 |
| 5b3f6fbc-dbc2-3dbf-a900-637538d190aa | -1.41454 | -55.39055 | 2025-11-28 04:31:00 | NOAA-21 | ALENQUER | PARÁ | Brasil | 1500404 | 15 | 33 | nan | nan | nan | Amazônia | 1.6 |
| f44fc4e3-4aca-3a7b-b30a-f8017fec0e99 | -3.18483 | -48.62008 | 2025-11-28 04:31:00 | NOAA-21 | TAILÂNDIA | PARÁ | Brasil | 1507953 | 15 | 33 | nan | nan | nan | Amazônia | 1.2 |
| 803e3901-8e26-35ab-a6a1-5efe0a1f9cd3 | -3.92448 | -50.99136 | 2025-11-28 04:31:00 | NOAA-21 | PACAJÁ | PARÁ | Brasil | 1505486 | 15 | 33 | nan | nan | nan | Amazônia | 2.0 |
| 949ccb57-c71f-3ec4-a3aa-881eb5253f0f | -2.6284 | -47.35877 | 2025-11-28 04:31:00 | NOAA-21 | IPIXUNA DO PARÁ | PARÁ | Brasil | 1503457 | 15 | 33 | nan | nan | nan | Amazônia | 1.4 |
| 6518b81f-fd2a-3740-af8d-288ebe7a912b | -3.27798 | -53.7662 | 2025-11-28 04:31:00 | NOAA-21 | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | 0.9 |
| cae87084-78dd-383e-b8b5-d9cb3a46cb91 | -3.49049 | -50.49047 | 2025-11-28 04:31:00 | NOAA-21 | PACAJÁ | PARÁ | Brasil | 1505486 | 15 | 33 | nan | nan | nan | Amazônia | 1.2 |
| b0d9c601-a9b3-337a-a79e-7d407d96b214 | -3.98552 | -50.86428 | 2025-11-28 04:31:00 | NOAA-21 | PACAJÁ | PARÁ | Brasil | 1505486 | 15 | 33 | nan | nan | nan | Amazônia | 2.2 |
| e8e2a97a-3bb9-348c-b196-ae2437ffe165 | -2.95438 | -45.55905 | 2025-11-28 04:31:00 | NOAA-21 | PEDRO DO ROSÁRIO | MARANHÃO | Brasil | 2108256 | 21 | 33 | nan | nan | nan | Amazônia | 1.1 |
| a54ae8be-8147-3e52-88ed-317f2bea1ab7 | -2.7454 | -47.13418 | 2025-11-28 04:31:00 | NOAA-21 | PARAGOMINAS | PARÁ | Brasil | 1505502 | 15 | 33 | nan | nan | nan | Amazônia | 1.2 |
| 39f3dac4-5f9c-3e99-b2f8-8aa03f62803a | -5.47526 | -50.7 | 2025-11-28 04:31:00 | NOAA-21 | MARABÁ | PARÁ | Brasil | 1504208 | 15 | 33 | nan | nan | nan | Amazônia | 1.5 |
| b8b42eff-4d36-30ce-8e88-dce4673466ce | -3.07739 | -50.35252 | 2025-11-28 04:31:00 | NOAA-21 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 3.9 |
| 8a990f95-c557-3d7e-9c00-25e20a8bbff1 | -5.43625 | -43.0469 | 2025-11-28 04:31:00 | NOAA-21 | MATÕES | MARANHÃO | Brasil | 2106607 | 21 | 33 | nan | nan | nan | Cerrado | 2.0 |
| cba14382-3721-3b9a-afb7-9dbf5875d4cc | -2.96751 | -45.64153 | 2025-11-28 04:31:00 | NOAA-21 | ARAGUANÃ | MARANHÃO | Brasil | 2100873 | 21 | 33 | nan | nan | nan | Amazônia | 0.7 |
| a6cc5836-9d8d-3ad1-a05e-78362feb326b | -3.35085 | -54.08856 | 2025-11-28 04:31:00 | NOAA-21 | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | 3.0 |
| 2d4ad59f-a936-3ecc-b30a-a835f7ed1517 | -3.8651 | -40.63925 | 2025-11-28 04:31:00 | NOAA-21 | CARIRÉ | CEARÁ | Brasil | 2303105 | 23 | 33 | nan | nan | nan | Caatinga | 1.8 |
| 5ce3e881-a038-3c20-aa9f-cb9451358686 | -5.75124 | -45.11126 | 2025-11-28 04:31:00 | NOAA-21 | BARRA DO CORDA | MARANHÃO | Brasil | 2101608 | 21 | 33 | nan | nan | nan | Cerrado | 6.9 |
| f9d83c5c-ea71-3f97-8c72-5659b43b343c | -2.7343 | -51.83813 | 2025-11-28 04:31:00 | NOAA-21 | SENADOR JOSÉ PORFÍRIO | PARÁ | Brasil | 1507805 | 15 | 33 | nan | nan | nan | Amazônia | 1.9 |
| b1a076b6-7741-396e-8dc8-c623fc536e98 | -3.89173 | -47.24115 | 2025-11-28 04:31:00 | NOAA-21 | ULIANÓPOLIS | PARÁ | Brasil | 1508126 | 15 | 33 | nan | nan | nan | Amazônia | 1.1 |
| 0183a20a-340e-38e3-bd9b-4a87c48f3e03 | -3.38493 | -51.49922 | 2025-11-28 04:31:00 | NOAA-21 | ANAPU | PARÁ | Brasil | 1500859 | 15 | 33 | nan | nan | nan | Amazônia | 3.0 |
| 4a29f348-57e6-3d35-9f1a-1187442e1617 | -5.45646 | -50.74782 | 2025-11-28 04:31:00 | NOAA-21 | MARABÁ | PARÁ | Brasil | 1504208 | 15 | 33 | nan | nan | nan | Amazônia | 1.4 |
| be07ec17-8420-38cb-8181-45a6a8273ed0 | -4.30587 | -50.73978 | 2025-11-28 04:31:00 | NOAA-21 | NOVO REPARTIMENTO | PARÁ | Brasil | 1505064 | 15 | 33 | nan | nan | nan | Amazônia | 1.1 |
| 4288fec8-e2e4-32e5-9b8c-a4a941dc31d2 | -2.85545 | -53.00676 | 2025-11-28 04:31:00 | NOAA-21 | MEDICILÂNDIA | PARÁ | Brasil | 1504455 | 15 | 33 | nan | nan | nan | Amazônia | 0.6 |
| ce787b60-f139-3b61-8d9d-693c9df49e95 | -4.82797 | -49.89951 | 2025-11-28 04:31:00 | NOAA-21 | ITUPIRANGA | PARÁ | Brasil | 1503705 | 15 | 33 | nan | nan | nan | Amazônia | 1.4 |
| acf80c21-6875-3f99-b29e-b75975aee651 | -4.32145 | -44.05555 | 2025-11-28 04:31:00 | NOAA-21 | TIMBIRAS | MARANHÃO | Brasil | 2112100 | 21 | 33 | nan | nan | nan | Cerrado | 1.0 |
| b2913dc7-9cc4-37d4-a0e2-e245e4b1d00b | -3.89227 | -47.23771 | 2025-11-28 04:31:00 | NOAA-21 | ULIANÓPOLIS | PARÁ | Brasil | 1508126 | 15 | 33 | nan | nan | nan | Amazônia | 1.8 |
| 7b3c1ed1-1b26-32a1-b487-29babba70484 | -4.70741 | -46.28444 | 2025-11-28 04:31:00 | NOAA-21 | BURITICUPU | MARANHÃO | Brasil | 2102325 | 21 | 33 | nan | nan | nan | Amazônia | 1.7 |
| fd5dee44-20b4-3171-9995-40759c6ef174 | -3.23291 | -50.69849 | 2025-11-28 04:31:00 | NOAA-21 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 1.4 |
| c8504828-b6c2-3eae-9e53-99a8ad655e8b | -2.60357 | -47.34436 | 2025-11-28 04:31:00 | NOAA-21 | IPIXUNA DO PARÁ | PARÁ | Brasil | 1503457 | 15 | 33 | nan | nan | nan | Amazônia | 4.2 |
| 5b6a0a9d-f204-353b-96a0-fdb14f141d1a | -2.73136 | -51.84007 | 2025-11-28 04:31:00 | NOAA-21 | SENADOR JOSÉ PORFÍRIO | PARÁ | Brasil | 1507805 | 15 | 33 | nan | nan | nan | Amazônia | 1.9 |
| 83562363-1c17-3ca4-b034-0bd1aca68813 | -2.96104 | -48.59291 | 2025-11-28 04:31:00 | NOAA-21 | TAILÂNDIA | PARÁ | Brasil | 1507953 | 15 | 33 | nan | nan | nan | Amazônia | 2.8 |
| f5c2ef51-16da-3599-872f-624d4a2beb97 | -4.01335 | -50.59787 | 2025-11-28 04:31:00 | NOAA-21 | NOVO REPARTIMENTO | PARÁ | Brasil | 1505064 | 15 | 33 | nan | nan | nan | Amazônia | 1.8 |
| 1cbde4bc-d946-363f-9525-9aae2f9d7b60 | -5.33465 | -49.52109 | 2025-11-28 04:31:00 | NOAA-21 | ITUPIRANGA | PARÁ | Brasil | 1503705 | 15 | 33 | nan | nan | nan | Amazônia | 0.7 |
| e427576b-48bd-32b3-a1af-598e33abaec0 | -2.43832 | -46.35704 | 2025-11-28 04:31:00 | NOAA-21 | CENTRO NOVO DO MARANHÃO | MARANHÃO | Brasil | 2103174 | 21 | 33 | nan | nan | nan | Amazônia | 1.3 |
| 3f6d6fc1-66b3-3e7a-91d5-f1cf6480c6a9 | -3.59042 | -47.27807 | 2025-11-28 04:31:00 | NOAA-21 | ULIANÓPOLIS | PARÁ | Brasil | 1508126 | 15 | 33 | nan | nan | nan | Amazônia | 3.3 |
| ace6d732-f03c-3a9b-84f3-254d621c3186 | -3.0956 | -51.54443 | 2025-11-28 04:31:00 | NOAA-21 | ANAPU | PARÁ | Brasil | 1500859 | 15 | 33 | nan | nan | nan | Amazônia | 1.6 |
| 7488ce01-2b5e-31a2-b3e2-d017a08e031d | -2.65955 | -46.96607 | 2025-11-28 04:31:00 | NOAA-21 | PARAGOMINAS | PARÁ | Brasil | 1505502 | 15 | 33 | nan | nan | nan | Amazônia | 2.2 |
| 64f32d9d-8cd7-3279-9d00-14a01e296833 | -2.96031 | -51.02512 | 2025-11-28 04:31:00 | NOAA-21 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 3.0 |
| 95eb20a6-430c-3ede-ac56-6fa659d3acf9 | -2.62341 | -47.34743 | 2025-11-28 04:31:00 | NOAA-21 | IPIXUNA DO PARÁ | PARÁ | Brasil | 1503457 | 15 | 33 | nan | nan | nan | Amazônia | 1.1 |
| 412293ce-cedf-3926-9695-d9464c95f2e8 | -3.55848 | -52.07409 | 2025-11-28 04:31:00 | NOAA-21 | SENADOR JOSÉ PORFÍRIO | PARÁ | Brasil | 1507805 | 15 | 33 | nan | nan | nan | Amazônia | 1.2 |
| 7ac16a72-2b17-342c-afcc-51a3235f362e | -2.61572 | -47.35329 | 2025-11-28 04:31:00 | NOAA-21 | IPIXUNA DO PARÁ | PARÁ | Brasil | 1503457 | 15 | 33 | nan | nan | nan | Amazônia | 3.0 |
| 58370345-f525-307b-9613-e70446add00b | -2.42776 | -45.74799 | 2025-11-28 04:31:00 | NOAA-21 | SANTA LUZIA DO PARUÁ | MARANHÃO | Brasil | 2110039 | 21 | 33 | nan | nan | nan | Amazônia | 1.8 |
| 1bccc549-2a42-3fa9-b26e-25c6a08f0211 | -3.49388 | -51.08572 | 2025-11-28 04:31:00 | NOAA-21 | PACAJÁ | PARÁ | Brasil | 1505486 | 15 | 33 | nan | nan | nan | Amazônia | 1.9 |
| 4835d001-6e04-32a0-9f37-2b638bbbd072 | -2.69567 | -49.55428 | 2025-11-28 04:31:00 | NOAA-21 | BAIÃO | PARÁ | Brasil | 1501204 | 15 | 33 | nan | nan | nan | Amazônia | 1.0 |
| 2a538eea-1569-35af-9d4d-f6b7a70bbcf9 | -2.50085 | -46.0432 | 2025-11-28 04:31:00 | NOAA-21 | MARANHÃOZINHO | MARANHÃO | Brasil | 2106375 | 21 | 33 | nan | nan | nan | Amazônia | 0.5 |
| 3633a721-ce71-30d5-91ea-e595f2ad9fb7 | -2.4355 | -50.26315 | 2025-11-28 04:31:00 | NOAA-21 | BAGRE | PARÁ | Brasil | 1501105 | 15 | 33 | nan | nan | nan | Amazônia | 1.7 |
| d2053045-1a39-3af3-9622-b3feb9ccbd01 | -4.01698 | -50.59843 | 2025-11-28 04:31:00 | NOAA-21 | NOVO REPARTIMENTO | PARÁ | Brasil | 1505064 | 15 | 33 | nan | nan | nan | Amazônia | 2.0 |
| 7f1b7d7f-f6c2-3fbf-aede-833c9470f548 | -2.61956 | -47.35036 | 2025-11-28 04:31:00 | NOAA-21 | IPIXUNA DO PARÁ | PARÁ | Brasil | 1503457 | 15 | 33 | nan | nan | nan | Amazônia | 3.0 |
| c2185450-8922-3230-b244-1649ac13dbe5 | -3.27604 | -53.76309 | 2025-11-28 04:31:00 | NOAA-21 | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | 1.1 |
| 69d6e49f-4d26-3e91-91f0-ffd03cde642e | -2.67898 | -46.86362 | 2025-11-28 04:31:00 | NOAA-21 | PARAGOMINAS | PARÁ | Brasil | 1505502 | 15 | 33 | nan | nan | nan | Amazônia | 1.2 |
| 519d357a-af46-3cce-99b1-abfddc7a6325 | -3.40936 | -53.19448 | 2025-11-28 04:31:00 | NOAA-21 | MEDICILÂNDIA | PARÁ | Brasil | 1504455 | 15 | 33 | nan | nan | nan | Amazônia | 1.0 |
| a8eb2b4d-c8b7-327e-89d7-c9a560c3add5 | -5.71928 | -46.202 | 2025-11-28 04:31:00 | NOAA-21 | GRAJAÚ | MARANHÃO | Brasil | 2104800 | 21 | 33 | nan | nan | nan | Cerrado | 0.9 |
| 4c3183e4-babe-3bde-9ff6-bbd519494ec0 | -3.59096 | -47.27464 | 2025-11-28 04:31:00 | NOAA-21 | ULIANÓPOLIS | PARÁ | Brasil | 1508126 | 15 | 33 | nan | nan | nan | Amazônia | 10.4 |
| 8b422763-f284-321e-b708-3b04564ff176 | -3.46715 | -43.93667 | 2025-11-28 04:31:00 | NOAA-21 | NINA RODRIGUES | MARANHÃO | Brasil | 2107209 | 21 | 33 | nan | nan | nan | Cerrado | 1.8 |
| 4ca69458-6fc6-326c-ae17-a8888cd738f9 | -2.74527 | -49.33272 | 2025-11-28 04:31:00 | NOAA-21 | MOJU | PARÁ | Brasil | 1504703 | 15 | 33 | nan | nan | nan | Amazônia | 1.2 |
| 376456c0-c6b0-3270-ac2c-972e50de6c9f | -2.98991 | -49.59868 | 2025-11-28 04:31:00 | NOAA-21 | MOJU | PARÁ | Brasil | 1504703 | 15 | 33 | nan | nan | nan | Amazônia | 1.9 |
| 1f87b538-00c7-35e4-8dc1-3b12ac6daef9 | -3.76215 | -46.9633 | 2025-11-28 04:31:00 | NOAA-21 | CENTRO NOVO DO MARANHÃO | MARANHÃO | Brasil | 2103174 | 21 | 33 | nan | nan | nan | Amazônia | 3.2 |
| 3a04ab38-247d-3ea4-b41d-9c392d427b66 | -3.03832 | -50.97483 | 2025-11-28 04:31:00 | NOAA-21 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 2.9 |
| 7800b209-0658-3e2c-ba8a-f9664787a6f7 | -4.64388 | -46.43341 | 2025-11-28 04:31:00 | NOAA-21 | BURITICUPU | MARANHÃO | Brasil | 2102325 | 21 | 33 | nan | nan | nan | Amazônia | 0.7 |
| 2f55f0f3-abe2-34da-a38c-662e7a19d36f | -5.06703 | -40.82164 | 2025-11-28 04:31:00 | NOAA-21 | CRATEÚS | CEARÁ | Brasil | 2304103 | 23 | 33 | nan | nan | nan | Caatinga | 9.9 |
| 689887f3-d6be-3d45-91c0-fd8a7bd01a97 | -4.56947 | -50.49605 | 2025-11-28 04:31:00 | NOAA-21 | NOVO REPARTIMENTO | PARÁ | Brasil | 1505064 | 15 | 33 | nan | nan | nan | Amazônia | 2.0 |
| 68d22c60-4e5a-3c0a-90d6-94f211edb76c | -4.54382 | -43.29876 | 2025-11-28 04:31:00 | NOAA-21 | ALDEIAS ALTAS | MARANHÃO | Brasil | 2100303 | 21 | 33 | nan | nan | nan | Cerrado | 3.2 |
| 231017ac-daff-39c3-ac1a-b291bb52d595 | -4.14325 | -46.76517 | 2025-11-28 04:31:00 | NOAA-21 | BOM JARDIM | MARANHÃO | Brasil | 2102002 | 21 | 33 | nan | nan | nan | Amazônia | 3.3 |


[Clique aqui para ver as próximas entradas](README10.md)
