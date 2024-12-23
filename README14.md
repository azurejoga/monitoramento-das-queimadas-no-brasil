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

## Dados Diários - Página 14

| ID | Latitude | Longitude | Data/Hora GMT | Satélite | Município | Estado | País | Município ID | Estado ID | País ID | Dias sem Chuva | Precipitação | Risco de Fogo | Bioma | FRP |
|----|----------|-----------|---------------|----------|-----------|--------|------|--------------|-----------|---------|----------------|--------------|----------------|-------|-----|
| 853515d1-87c6-33f4-835a-a15cc1252a4d | -3.98052 | -46.67469 | 2024-12-23 04:31:00 | NPP-375D | BOM JARDIM | MARANHÃO | Brasil | 2102002 | 21 | 33 | nan | nan | nan | Amazônia | 1.4 |
| ede5317e-073d-3287-b717-5cf4dfe4773d | -4.03902 | -47.03703 | 2024-12-23 04:31:00 | NPP-375D | ITINGA DO MARANHÃO | MARANHÃO | Brasil | 2105427 | 21 | 33 | nan | nan | nan | Amazônia | 1.3 |
| 94c56421-c010-3a2c-ba48-fbb8b5fc8914 | -3.33433 | -53.10879 | 2024-12-23 04:31:00 | NPP-375D | MEDICILÂNDIA | PARÁ | Brasil | 1504455 | 15 | 33 | nan | nan | nan | Amazônia | 5.6 |
| c97ab0df-2226-38ec-9cea-bf489a7e9b7e | -6.94119 | -43.53041 | 2024-12-23 04:31:00 | NPP-375D | JERUMENHA | PIAUÍ | Brasil | 2205300 | 22 | 33 | nan | nan | nan | Cerrado | 11.7 |
| 00a5390d-75d7-3e0d-a4ca-f6d785a0bc34 | -4.10054 | -46.81889 | 2024-12-23 04:31:00 | NPP-375D | BOM JARDIM | MARANHÃO | Brasil | 2102002 | 21 | 33 | nan | nan | nan | Amazônia | 1.2 |
| 2ccb1567-57e9-3650-b065-c965db33350a | -0.96293 | -46.84919 | 2024-12-23 04:31:00 | NPP-375D | TRACUATEUA | PARÁ | Brasil | 1508035 | 15 | 33 | nan | nan | nan | Amazônia | 1.3 |
| 19c6559a-d616-3a32-852b-c0726a17afb7 | -3.0937 | -54.60295 | 2024-12-23 04:31:00 | NPP-375D | MOJUÍ DOS CAMPOS | PARÁ | Brasil | 1504752 | 15 | 33 | nan | nan | nan | Amazônia | 3.4 |
| 69eceffa-d9e0-3449-a377-252a484b4b5e | -3.85867 | -46.58791 | 2024-12-23 04:31:00 | NPP-375D | BOM JARDIM | MARANHÃO | Brasil | 2102002 | 21 | 33 | nan | nan | nan | Amazônia | 0.8 |
| cb99eb0d-6238-3f99-9e54-93f43d6ce4eb | -3.09166 | -46.56884 | 2024-12-23 04:31:00 | NPP-375D | CENTRO NOVO DO MARANHÃO | MARANHÃO | Brasil | 2103174 | 21 | 33 | nan | nan | nan | Amazônia | 0.9 |
| eeb04037-1d4c-3329-ad21-be6bb8ed8f7f | -3.91621 | -46.88938 | 2024-12-23 04:31:00 | NPP-375D | CENTRO NOVO DO MARANHÃO | MARANHÃO | Brasil | 2103174 | 21 | 33 | nan | nan | nan | Amazônia | 0.9 |
| e58ceb8f-4355-3f4a-98b0-991b6e2a1e11 | -5.80694 | -39.07447 | 2024-12-23 04:31:00 | NPP-375D | SOLONÓPOLE | CEARÁ | Brasil | 2313005 | 23 | 33 | nan | nan | nan | Caatinga | 1.1 |
| caa5ec19-3542-3ed4-82d5-6c04dd01e754 | -3.92888 | -46.35749 | 2024-12-23 04:31:00 | NPP-375D | BOM JARDIM | MARANHÃO | Brasil | 2102002 | 21 | 33 | nan | nan | nan | Amazônia | 2.1 |
| b33e951b-0921-39e4-8231-83d4210831c3 | -6.93333 | -43.52923 | 2024-12-23 04:31:00 | NPP-375D | JERUMENHA | PIAUÍ | Brasil | 2205300 | 22 | 33 | nan | nan | nan | Cerrado | 17.2 |
| 8246959c-1b7c-36e1-b4c6-31cc5694f679 | -4.0766 | -46.6221 | 2024-12-23 04:31:00 | NPP-375D | BOM JARDIM | MARANHÃO | Brasil | 2102002 | 21 | 33 | nan | nan | nan | Amazônia | 0.2 |
| c302abed-3d33-3e5d-8e7d-9b0d893f3c95 | -2.99416 | -51.43921 | 2024-12-23 04:31:00 | NPP-375D | ANAPU | PARÁ | Brasil | 1500859 | 15 | 33 | nan | nan | nan | Amazônia | 1.4 |
| f59bb08e-adc7-343d-9f1a-c9970edf7c95 | -3.90549 | -47.00145 | 2024-12-23 04:31:00 | NPP-375D | ITINGA DO MARANHÃO | MARANHÃO | Brasil | 2105427 | 21 | 33 | nan | nan | nan | Amazônia | 1.5 |
| 3348fc10-079e-34a1-adeb-1d53337b0958 | -4.01525 | -47.05817 | 2024-12-23 04:31:00 | NPP-375D | ITINGA DO MARANHÃO | MARANHÃO | Brasil | 2105427 | 21 | 33 | nan | nan | nan | Amazônia | 2.9 |
| 82c1f927-e99e-32c8-aa86-ead5356285cb | -3.83573 | -46.88771 | 2024-12-23 04:31:00 | NPP-375D | CENTRO NOVO DO MARANHÃO | MARANHÃO | Brasil | 2103174 | 21 | 33 | nan | nan | nan | Amazônia | 1.0 |
| bed1734f-0737-383c-a071-c9c7b2624416 | -4.77235 | -46.3891 | 2024-12-23 04:31:00 | NPP-375D | BURITICUPU | MARANHÃO | Brasil | 2102325 | 21 | 33 | nan | nan | nan | Amazônia | 1.6 |
| d9253951-45aa-331f-b057-8ec96b01da81 | -3.919 | -46.89338 | 2024-12-23 04:31:00 | NPP-375D | CENTRO NOVO DO MARANHÃO | MARANHÃO | Brasil | 2103174 | 21 | 33 | nan | nan | nan | Amazônia | 1.6 |
| 661cf12b-e772-3e4f-8ad2-9e8167baaa0c | -3.91846 | -46.89686 | 2024-12-23 04:31:00 | NPP-375D | CENTRO NOVO DO MARANHÃO | MARANHÃO | Brasil | 2103174 | 21 | 33 | nan | nan | nan | Amazônia | 1.6 |
| d6a89685-ebb0-35ac-b22d-cce95db1dcca | -4.01034 | -46.81147 | 2024-12-23 04:31:00 | NPP-375D | BOM JARDIM | MARANHÃO | Brasil | 2102002 | 21 | 33 | nan | nan | nan | Amazônia | 0.6 |
| 455c9340-2e74-3f76-8597-8de6f0a73905 | -4.08053 | -46.81578 | 2024-12-23 04:31:00 | NPP-375D | BOM JARDIM | MARANHÃO | Brasil | 2102002 | 21 | 33 | nan | nan | nan | Amazônia | 0.7 |
| 629d649a-f78e-32ee-abf3-95cfdc97194b | -3.53554 | -52.67082 | 2024-12-23 04:31:00 | NPP-375D | BRASIL NOVO | PARÁ | Brasil | 1501725 | 15 | 33 | nan | nan | nan | Amazônia | 1.6 |
| c13bb8cd-52f8-348b-b0fc-a23f7b7cba6e | -3.91581 | -46.93554 | 2024-12-23 04:31:00 | NPP-375D | CENTRO NOVO DO MARANHÃO | MARANHÃO | Brasil | 2103174 | 21 | 33 | nan | nan | nan | Amazônia | 2.4 |
| 92d93cfe-240c-3bd7-b8f0-694029a28b91 | -3.6487 | -54.73702 | 2024-12-23 04:31:00 | NPP-375D | PLACAS | PARÁ | Brasil | 1505650 | 15 | 33 | nan | nan | nan | Amazônia | 1.4 |
| 058ed3ec-0520-3378-8c74-a367db2a70a5 | -2.99536 | -52.00842 | 2024-12-23 04:31:00 | NPP-375D | VITÓRIA DO XINGU | PARÁ | Brasil | 1508357 | 15 | 33 | nan | nan | nan | Amazônia | 2.4 |
| 857699cb-7bf0-343e-b890-dffff47fc4ef | -4.02197 | -46.90644 | 2024-12-23 04:31:00 | NPP-375D | CENTRO NOVO DO MARANHÃO | MARANHÃO | Brasil | 2103174 | 21 | 33 | nan | nan | nan | Amazônia | 0.8 |
| 40c909ea-d152-3664-9dd1-7c469952c192 | -2.49412 | -51.80431 | 2024-12-23 04:31:00 | NPP-375D | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 1.6 |
| e647775d-5efb-39ad-9db4-31ea76aa804b | -2.12657 | -53.49556 | 2024-12-23 04:31:00 | NPP-375D | PRAINHA | PARÁ | Brasil | 1506005 | 15 | 33 | nan | nan | nan | Amazônia | 1.0 |
| 54e1f114-7dd5-357e-934b-2c2ea1155cbe | -2.12174 | -50.70292 | 2024-12-23 04:31:00 | NPP-375D | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 1.0 |
| b822e9ca-5d30-3824-b52a-eb3c3ef2d505 | -2.64798 | -46.11349 | 2024-12-23 04:31:00 | NPP-375D | CENTRO DO GUILHERME | MARANHÃO | Brasil | 2103158 | 21 | 33 | nan | nan | nan | Amazônia | 1.1 |
| 823b8e43-c346-3a3f-be01-451448b66027 | -6.90361 | -43.54252 | 2024-12-23 04:31:00 | NPP-375D | GUADALUPE | PIAUÍ | Brasil | 2204501 | 22 | 33 | nan | nan | nan | Cerrado | 2.6 |
| c16e2140-c340-3261-a6ed-6b2af43bc27a | -3.92403 | -46.90485 | 2024-12-23 04:31:00 | NPP-375D | CENTRO NOVO DO MARANHÃO | MARANHÃO | Brasil | 2103174 | 21 | 33 | nan | nan | nan | Amazônia | 1.2 |
| 7beea1d7-9b88-3d9d-971b-ad1b771fc764 | -2.73542 | -46.87213 | 2024-12-23 04:31:00 | NPP-375D | PARAGOMINAS | PARÁ | Brasil | 1505502 | 15 | 33 | nan | nan | nan | Amazônia | 1.7 |
| ed7352fe-2054-3a5e-b18b-0f788cf2a9ce | -2.79522 | -52.94444 | 2024-12-23 04:31:00 | NPP-375D | MEDICILÂNDIA | PARÁ | Brasil | 1504455 | 15 | 33 | nan | nan | nan | Amazônia | 1.7 |
| 033aa23e-e6f8-3515-94e6-c1759f339941 | -3.23902 | -52.84096 | 2024-12-23 04:31:00 | NPP-375D | MEDICILÂNDIA | PARÁ | Brasil | 1504455 | 15 | 33 | nan | nan | nan | Amazônia | 2.0 |
| 5c2cc8e3-1c89-3fc3-a400-c0b0ade07d54 | -3.77472 | -46.82483 | 2024-12-23 04:31:00 | NPP-375D | CENTRO NOVO DO MARANHÃO | MARANHÃO | Brasil | 2103174 | 21 | 33 | nan | nan | nan | Amazônia | 1.5 |
| f0cb51fa-21bc-3625-8b18-d4efbfd16920 | -3.50695 | -47.19458 | 2024-12-23 04:31:00 | NPP-375D | ULIANÓPOLIS | PARÁ | Brasil | 1508126 | 15 | 33 | nan | nan | nan | Amazônia | 2.0 |
| f4b8978d-e115-391c-9478-db22af420d51 | -3.92376 | -46.99362 | 2024-12-23 04:31:00 | NPP-375D | ITINGA DO MARANHÃO | MARANHÃO | Brasil | 2105427 | 21 | 33 | nan | nan | nan | Amazônia | 1.7 |
| e5c39d1e-8952-336c-acdd-58bad55a9190 | -2.62826 | -46.11714 | 2024-12-23 04:31:00 | NPP-375D | CENTRO DO GUILHERME | MARANHÃO | Brasil | 2103158 | 21 | 33 | nan | nan | nan | Amazônia | 1.4 |
| 6a6b3e28-b04b-3409-98db-0221773960cf | -2.65018 | -46.09939 | 2024-12-23 04:31:00 | NPP-375D | CENTRO DO GUILHERME | MARANHÃO | Brasil | 2103158 | 21 | 33 | nan | nan | nan | Amazônia | 1.4 |
| 2793211e-620d-3dd3-8fa4-5f5ad7205a35 | -4.17795 | -43.65718 | 2024-12-23 04:31:00 | NPP-375D | TIMBIRAS | MARANHÃO | Brasil | 2112100 | 21 | 33 | nan | nan | nan | Cerrado | 4.5 |
| 45b01f18-f38a-325a-a7cf-8c40c0fcd77e | -7.53411 | -35.3036 | 2024-12-23 04:31:00 | NPP-375D | TIMBAÚBA | PERNAMBUCO | Brasil | 2615300 | 26 | 33 | nan | nan | nan | Mata Atlântica | 5.2 |
| 785f20fc-b1d8-3cbb-901c-42e4e7d1a4f6 | -1.62568 | -45.83989 | 2024-12-23 04:31:00 | NPP-375D | AMAPÁ DO MARANHÃO | MARANHÃO | Brasil | 2100550 | 21 | 33 | nan | nan | nan | Amazônia | 0.7 |
| 73ce0040-889e-34e3-8012-366fbdbaf714 | -4.01279 | -46.90442 | 2024-12-23 04:31:00 | NPP-375D | CENTRO NOVO DO MARANHÃO | MARANHÃO | Brasil | 2103174 | 21 | 33 | nan | nan | nan | Amazônia | 1.4 |
| 93dc7ad1-bec7-345e-a2d7-0799cf9b2c43 | -3.54111 | -43.58618 | 2024-12-23 04:31:00 | NPP-375D | SÃO BENEDITO DO RIO PRETO | MARANHÃO | Brasil | 2110401 | 21 | 33 | nan | nan | nan | Cerrado | 3.0 |
| 0713a43f-726a-36f6-b326-0c45f20c87df | -3.17572 | -45.96926 | 2024-12-23 04:31:00 | NPP-375D | ZÉ DOCA | MARANHÃO | Brasil | 2114007 | 21 | 33 | nan | nan | nan | Amazônia | 1.1 |
| bea82c28-721d-3173-8e5e-ed70b280c9a9 | -3.02578 | -53.89342 | 2024-12-23 04:31:00 | NPP-375D | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | 1.5 |
| 0b5e3fd0-32b1-31fd-81c8-653db6ed87e4 | -4.15541 | -43.65371 | 2024-12-23 04:31:00 | NPP-375D | TIMBIRAS | MARANHÃO | Brasil | 2112100 | 21 | 33 | nan | nan | nan | Cerrado | 2.3 |
| 42f1908b-8d61-32dd-9d35-9455fd8eea16 | -3.18779 | -50.54975 | 2024-12-23 04:31:00 | NPP-375D | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 1.8 |
| dd2d1ef5-9001-3414-9928-92fc32856560 | -3.86002 | -46.66696 | 2024-12-23 04:31:00 | NPP-375D | BOM JARDIM | MARANHÃO | Brasil | 2102002 | 21 | 33 | nan | nan | nan | Amazônia | 0.6 |
| 8c0ab6fe-f3f7-3887-ae79-d4d9745b33b1 | -2.40846 | -53.74608 | 2024-12-23 04:31:00 | NPP-375D | PRAINHA | PARÁ | Brasil | 1506005 | 15 | 33 | nan | nan | nan | Amazônia | 5.0 |
| 185765eb-e414-3a2d-b322-ae8af6da6bcc | -2.64517 | -46.10944 | 2024-12-23 04:31:00 | NPP-375D | CENTRO DO GUILHERME | MARANHÃO | Brasil | 2103158 | 21 | 33 | nan | nan | nan | Amazônia | 1.1 |
| 91584f81-6568-3788-9a4c-5d4c77ee5cee | -2.81841 | -48.08556 | 2024-12-23 04:31:00 | NPP-375D | TOMÉ-AÇU | PARÁ | Brasil | 1508001 | 15 | 33 | nan | nan | nan | Amazônia | 0.6 |
| e93ed0f3-56ed-3df4-af9d-db4ce2431603 | -3.91454 | -46.66825 | 2024-12-23 04:31:00 | NPP-375D | BOM JARDIM | MARANHÃO | Brasil | 2102002 | 21 | 33 | nan | nan | nan | Amazônia | 0.8 |
| 773f4b3d-a379-381a-86c6-1446f94a23e2 | -4.31925 | -43.9684 | 2024-12-23 04:31:00 | NPP-375D | TIMBIRAS | MARANHÃO | Brasil | 2112100 | 21 | 33 | nan | nan | nan | Cerrado | 2.6 |
| 9031ed09-890f-31dc-be5e-7712b7ec6111 | -2.64237 | -46.10539 | 2024-12-23 04:31:00 | NPP-375D | CENTRO DO GUILHERME | MARANHÃO | Brasil | 2103158 | 21 | 33 | nan | nan | nan | Amazônia | 1.4 |
| 3ed2f2ff-f165-34a0-9ee1-40e7e4d5e6e9 | -3.79476 | -46.84933 | 2024-12-23 04:31:00 | NPP-375D | CENTRO NOVO DO MARANHÃO | MARANHÃO | Brasil | 2103174 | 21 | 33 | nan | nan | nan | Amazônia | 1.1 |
| d2340504-fe4e-32f2-9aff-9d5f5bb8b14b | -6.90436 | -43.53756 | 2024-12-23 04:31:00 | NPP-375D | GUADALUPE | PIAUÍ | Brasil | 2204501 | 22 | 33 | nan | nan | nan | Cerrado | 2.6 |
| 33498b93-753b-3168-a9ba-df6a96bba99a | -3.08554 | -46.56431 | 2024-12-23 04:31:00 | NPP-375D | CENTRO NOVO DO MARANHÃO | MARANHÃO | Brasil | 2103174 | 21 | 33 | nan | nan | nan | Amazônia | 1.5 |
| 2e0b27ea-05b5-3606-bcf4-f8887d6a42d3 | -4.05856 | -47.08619 | 2024-12-23 04:31:00 | NPP-375D | ITINGA DO MARANHÃO | MARANHÃO | Brasil | 2105427 | 21 | 33 | nan | nan | nan | Amazônia | 1.2 |
| 3162e4c4-ee0f-30a2-8d4c-bf954d2347ea | -3.87603 | -47.02184 | 2024-12-23 04:31:00 | NPP-375D | ITINGA DO MARANHÃO | MARANHÃO | Brasil | 2105427 | 21 | 33 | nan | nan | nan | Amazônia | 1.2 |
| 71a0ed0c-e01f-339b-a5a7-eed05d506888 | -4.00785 | -46.99666 | 2024-12-23 04:31:00 | NPP-375D | ITINGA DO MARANHÃO | MARANHÃO | Brasil | 2105427 | 21 | 33 | nan | nan | nan | Amazônia | 2.2 |
| fd56e1ba-4804-3594-9723-83c1f9f840cb | -3.99273 | -46.66222 | 2024-12-23 04:31:00 | NPP-375D | BOM JARDIM | MARANHÃO | Brasil | 2102002 | 21 | 33 | nan | nan | nan | Amazônia | 0.4 |
| 89ddff9d-c8cb-3600-9083-1ef45aad749a | -4.00914 | -46.55721 | 2024-12-23 04:31:00 | NPP-375D | BOM JARDIM | MARANHÃO | Brasil | 2102002 | 21 | 33 | nan | nan | nan | Amazônia | 1.5 |
| 9dd17aeb-8328-3693-8524-8569f76195a3 | -1.56958 | -54.76885 | 2024-12-23 04:31:00 | NPP-375D | ALENQUER | PARÁ | Brasil | 1500404 | 15 | 33 | nan | nan | nan | Amazônia | 1.1 |
| 12804b39-33ae-39d5-95b7-5225694fbe77 | -3.13202 | -49.16476 | 2024-12-23 04:31:00 | NPP-375D | MOJU | PARÁ | Brasil | 1504703 | 15 | 33 | nan | nan | nan | Amazônia | 1.1 |
| 03278ce4-3968-319b-9cd8-8e822a6a6186 | -3.92348 | -46.90833 | 2024-12-23 04:31:00 | NPP-375D | CENTRO NOVO DO MARANHÃO | MARANHÃO | Brasil | 2103174 | 21 | 33 | nan | nan | nan | Amazônia | 1.1 |
| 977d8e88-42d2-32dd-a70e-be7b8ed7f639 | -3.93169 | -46.36154 | 2024-12-23 04:31:00 | NPP-375D | BOM JARDIM | MARANHÃO | Brasil | 2102002 | 21 | 33 | nan | nan | nan | Amazônia | 1.8 |
| ceb6cb26-9fb1-3aee-91ec-fafe57940f2a | -2.81181 | -45.93191 | 2024-12-23 04:31:00 | NPP-375D | NOVA OLINDA DO MARANHÃO | MARANHÃO | Brasil | 2107357 | 21 | 33 | nan | nan | nan | Amazônia | 1.2 |
| 0d6efe4a-5104-3b0a-9acd-0714cca19fe4 | -3.92097 | -46.98964 | 2024-12-23 04:31:00 | NPP-375D | ITINGA DO MARANHÃO | MARANHÃO | Brasil | 2105427 | 21 | 33 | nan | nan | nan | Amazônia | 0.8 |
| 9b2aa401-ae82-31cb-a03f-6bfdaac4ab3b | -1.515 | -45.51796 | 2024-12-23 04:31:00 | NPP-375D | TURIAÇU | MARANHÃO | Brasil | 2112407 | 21 | 33 | nan | nan | nan | Amazônia | 4.4 |
| f125cd3d-922f-31eb-9e29-b280d1188e26 | -2.63011 | -46.11792 | 2024-12-23 04:31:00 | NPP-375D | CENTRO DO GUILHERME | MARANHÃO | Brasil | 2103158 | 21 | 33 | nan | nan | nan | Amazônia | 1.2 |
| 6eb6a917-220c-3362-a699-408127586a31 | -3.14578 | -46.34505 | 2024-12-23 04:31:00 | NPP-375D | NOVA OLINDA DO MARANHÃO | MARANHÃO | Brasil | 2107357 | 21 | 33 | nan | nan | nan | Amazônia | 2.2 |
| b1aa472c-68a7-3104-a41b-4bd77e6f90a9 | -3.95966 | -46.76434 | 2024-12-23 04:31:00 | NPP-375D | CENTRO NOVO DO MARANHÃO | MARANHÃO | Brasil | 2103174 | 21 | 33 | nan | nan | nan | Amazônia | 0.6 |
| e94d166b-725a-35e2-8300-3c2ba6146162 | -4.05918 | -54.74223 | 2024-12-23 04:31:00 | NPP-375D | PLACAS | PARÁ | Brasil | 1505650 | 15 | 33 | nan | nan | nan | Amazônia | 0.7 |
| 54ca475e-3f78-3e3a-87f1-8c53f56f4e22 | -6.90759 | -43.54072 | 2024-12-23 04:31:00 | NPP-375D | GUADALUPE | PIAUÍ | Brasil | 2204501 | 22 | 33 | nan | nan | nan | Cerrado | 3.9 |
| 7c6d5555-7402-3b38-a5ba-1dfc28024f90 | -3.90216 | -47.00093 | 2024-12-23 04:31:00 | NPP-375D | ITINGA DO MARANHÃO | MARANHÃO | Brasil | 2105427 | 21 | 33 | nan | nan | nan | Amazônia | 2.5 |
| 1a15866b-daa1-3f84-9f04-e60ae5ac4234 | -3.50363 | -47.19407 | 2024-12-23 04:31:00 | NPP-375D | PARAGOMINAS | PARÁ | Brasil | 1505502 | 15 | 33 | nan | nan | nan | Amazônia | 2.0 |
| 1573acba-c684-314b-ae43-5ed138ac74c1 | -3.98846 | -46.73314 | 2024-12-23 04:31:00 | NPP-375D | BOM JARDIM | MARANHÃO | Brasil | 2102002 | 21 | 33 | nan | nan | nan | Amazônia | 0.8 |
| 22bdb9fb-421a-3829-9c28-a12c5c0dd465 | -2.64098 | -46.97764 | 2024-12-23 04:31:00 | NPP-375D | PARAGOMINAS | PARÁ | Brasil | 1505502 | 15 | 33 | nan | nan | nan | Amazônia | 0.7 |
| f2635a81-e32e-3c8b-8774-c68b1157fb94 | -4.45078 | -45.31134 | 2024-12-23 04:31:00 | NPP-375D | PAULO RAMOS | MARANHÃO | Brasil | 2108108 | 21 | 33 | nan | nan | nan | Amazônia | 1.1 |
| 7511910f-5d02-33c3-acf7-6117fd2d6606 | -3.90936 | -46.99849 | 2024-12-23 04:31:00 | NPP-375D | ITINGA DO MARANHÃO | MARANHÃO | Brasil | 2105427 | 21 | 33 | nan | nan | nan | Amazônia | 1.5 |
| e22039be-1dba-35f1-aecb-008a8f0f83d7 | -1.63073 | -45.85151 | 2024-12-23 04:31:00 | NPP-375D | AMAPÁ DO MARANHÃO | MARANHÃO | Brasil | 2100550 | 21 | 33 | nan | nan | nan | Amazônia | 0.6 |
| 8d83d696-d473-3f01-860c-2a7e3a7a2dce | -3.17797 | -45.97692 | 2024-12-23 04:31:00 | NPP-375D | ZÉ DOCA | MARANHÃO | Brasil | 2114007 | 21 | 33 | nan | nan | nan | Amazônia | 1.5 |
| 437b2ff0-19d4-3f97-95dd-a9080eb962f8 | -5.24379 | -36.17991 | 2024-12-23 04:31:00 | NPP-375D | GALINHOS | RIO GRANDE DO NORTE | Brasil | 2404101 | 24 | 33 | nan | nan | nan | Caatinga | 1.9 |
| d18ca5cb-95e5-32ba-91b2-4940ad791d3f | -3.91852 | -46.91822 | 2024-12-23 04:31:00 | NPP-375D | CENTRO NOVO DO MARANHÃO | MARANHÃO | Brasil | 2103174 | 21 | 33 | nan | nan | nan | Amazônia | 1.7 |
| 066f22fd-7893-3b70-a7c9-a2d972a616f8 | -2.11523 | -45.49907 | 2024-12-23 04:31:00 | NPP-375D | TURILÂNDIA | MARANHÃO | Brasil | 2112456 | 21 | 33 | nan | nan | nan | Amazônia | 1.3 |
| b1e84876-90bb-3ccc-8bdf-6619c85ff189 | -4.0047 | -46.56371 | 2024-12-23 04:31:00 | NPP-375D | BOM JARDIM | MARANHÃO | Brasil | 2102002 | 21 | 33 | nan | nan | nan | Amazônia | 2.2 |
| 257ab7cc-2044-3eed-aca2-fcbdc5ddf199 | -0.77658 | -48.79037 | 2024-12-23 04:31:00 | NPP-375D | CACHOEIRA DO ARARI | PARÁ | Brasil | 1502004 | 15 | 33 | nan | nan | nan | Amazônia | 1.4 |
| 93745a5a-a455-37e3-a4c6-dd5b18b22aef | -4.44604 | -45.92694 | 2024-12-23 04:31:00 | NPP-375D | SANTA LUZIA | MARANHÃO | Brasil | 2110005 | 21 | 33 | nan | nan | nan | Amazônia | 5.4 |
| 0023bf5f-ef8c-349f-ba63-58464647bbb4 | -3.7558 | -40.98976 | 2024-12-23 04:31:00 | NPP-375D | TIANGUÁ | CEARÁ | Brasil | 2313401 | 23 | 33 | nan | nan | nan | Caatinga | 0.6 |
| ef4df5fa-2ac4-31cd-a53b-dc24da169cdb | -3.91635 | -46.93209 | 2024-12-23 04:31:00 | NPP-375D | CENTRO NOVO DO MARANHÃO | MARANHÃO | Brasil | 2103174 | 21 | 33 | nan | nan | nan | Amazônia | 1.3 |
| 28986310-3e60-398f-a295-05717bf44b84 | -4.01666 | -46.90148 | 2024-12-23 04:31:00 | NPP-375D | CENTRO NOVO DO MARANHÃO | MARANHÃO | Brasil | 2103174 | 21 | 33 | nan | nan | nan | Amazônia | 0.5 |
| 2e409ab2-9fc7-3300-a4cf-9f9c65526498 | -3.90512 | -46.68465 | 2024-12-23 04:31:00 | NPP-375D | BOM JARDIM | MARANHÃO | Brasil | 2102002 | 21 | 33 | nan | nan | nan | Amazônia | 0.6 |
| 4f8cacad-061f-3a64-8910-d3c90d48ec32 | -7.8389 | -35.22145 | 2024-12-23 04:31:00 | NPP-375D | PAUDALHO | PERNAMBUCO | Brasil | 2610608 | 26 | 33 | nan | nan | nan | Mata Atlântica | 5.6 |
| 045812dd-4a64-3ccf-a4a8-50f91d9ebbc9 | -3.97622 | -46.92005 | 2024-12-23 04:31:00 | NPP-375D | CENTRO NOVO DO MARANHÃO | MARANHÃO | Brasil | 2103174 | 21 | 33 | nan | nan | nan | Amazônia | 0.6 |
| f515bd8c-3c39-3c49-9c22-065140dbdb8d | -4.02642 | -46.79612 | 2024-12-23 04:31:00 | NPP-375D | BOM JARDIM | MARANHÃO | Brasil | 2102002 | 21 | 33 | nan | nan | nan | Amazônia | 1.2 |
| 8d380793-0c1c-3816-8742-17d6eb309b9c | -3.92729 | -46.88399 | 2024-12-23 04:31:00 | NPP-375D | CENTRO NOVO DO MARANHÃO | MARANHÃO | Brasil | 2103174 | 21 | 33 | nan | nan | nan | Amazônia | 0.8 |


[Clique aqui para ver as próximas entradas](README15.md)
