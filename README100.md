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

## Dados Diários - Página 100

| ID | Latitude | Longitude | Data/Hora GMT | Satélite | Município | Estado | País | Município ID | Estado ID | País ID | Dias sem Chuva | Precipitação | Risco de Fogo | Bioma | FRP |
|----|----------|-----------|---------------|----------|-----------|--------|------|--------------|-----------|---------|----------------|--------------|----------------|-------|-----|
| 37450562-5e04-3d03-858b-6a19a2a09ea3 | -1.56137 | -52.20295 | 2024-11-02 05:48:00 | AQUA_M-M | GURUPÁ | PARÁ | Brasil | 1503101 | 15 | 33 | nan | nan | nan | Amazônia | 10.0 |
| 3dc14b77-c3ce-3a3e-8429-c51ab638f37c | -1.55796 | -51.61216 | 2024-11-02 05:48:00 | AQUA_M-M | GURUPÁ | PARÁ | Brasil | 1503101 | 15 | 33 | nan | nan | nan | Amazônia | 4.6 |
| 21925d1d-2a5c-34f8-8490-d7307da3c633 | -1.55665 | -51.62099 | 2024-11-02 05:48:00 | AQUA_M-M | GURUPÁ | PARÁ | Brasil | 1503101 | 15 | 33 | nan | nan | nan | Amazônia | 7.1 |
| 64ec13b7-23ad-397d-8618-892bb35b2979 | -1.52638 | -54.2731 | 2024-11-02 05:48:00 | AQUA_M-M | MONTE ALEGRE | PARÁ | Brasil | 1504802 | 15 | 33 | nan | nan | nan | Amazônia | 4.4 |
| 184cd6cb-852b-33b4-ad40-d468b47f03b7 | -1.52484 | -54.28318 | 2024-11-02 05:48:00 | AQUA_M-M | MONTE ALEGRE | PARÁ | Brasil | 1504802 | 15 | 33 | nan | nan | nan | Amazônia | 8.6 |
| 6485f00f-997f-3e78-ad50-3dd500c16e77 | -1.51388 | -53.13653 | 2024-11-02 05:48:00 | AQUA_M-M | ALMEIRIM | PARÁ | Brasil | 1500503 | 15 | 33 | nan | nan | nan | Amazônia | 7.5 |
| eac47777-1efd-3288-97d5-d1265ea83963 | -1.46951 | -46.70922 | 2024-11-02 05:48:00 | AQUA_M-M | VISEU | PARÁ | Brasil | 1508308 | 15 | 33 | nan | nan | nan | Amazônia | 11.3 |
| 45fd3663-4c7d-3044-a796-74f7e3f7471d | -1.46713 | -46.72554 | 2024-11-02 05:48:00 | AQUA_M-M | BRAGANÇA | PARÁ | Brasil | 1501709 | 15 | 33 | nan | nan | nan | Amazônia | 20.0 |
| ecd4335b-5791-3a56-ac51-8963fc4ffc49 | -1.41876 | -52.22366 | 2024-11-02 05:48:00 | AQUA_M-M | ALMEIRIM | PARÁ | Brasil | 1500503 | 15 | 33 | nan | nan | nan | Amazônia | 5.0 |
| a034d939-70f6-3157-b1da-5459702fa95d | -1.41386 | -52.19603 | 2024-11-02 05:48:00 | AQUA_M-M | ALMEIRIM | PARÁ | Brasil | 1500503 | 15 | 33 | nan | nan | nan | Amazônia | 4.9 |
| eeed5ba6-da76-3ff6-89ac-8e5aa50ca9eb | -1.41255 | -52.20481 | 2024-11-02 05:48:00 | AQUA_M-M | ALMEIRIM | PARÁ | Brasil | 1500503 | 15 | 33 | nan | nan | nan | Amazônia | 6.4 |
| 92bb743c-0600-3384-a24c-a145352b4dc3 | -1.38293 | -54.12739 | 2024-11-02 05:48:00 | AQUA_M-M | MONTE ALEGRE | PARÁ | Brasil | 1504802 | 15 | 33 | nan | nan | nan | Amazônia | 5.0 |
| e0376af8-d9b9-3304-86b9-951b2d9cea4f | -1.34941 | -54.60913 | 2024-11-02 05:48:00 | AQUA_M-M | MONTE ALEGRE | PARÁ | Brasil | 1504802 | 15 | 33 | nan | nan | nan | Amazônia | 6.6 |
| 7a9f7e8c-70db-33c6-8788-9df32a964d52 | -1.34471 | -52.53673 | 2024-11-02 05:48:00 | AQUA_M-M | ALMEIRIM | PARÁ | Brasil | 1500503 | 15 | 33 | nan | nan | nan | Amazônia | 5.4 |
| 52bc04e2-6eac-3113-90f8-3941c13c537b | -2.72736 | -48.7419 | 2024-11-02 05:48:00 | AQUA_M-M | TAILÂNDIA | PARÁ | Brasil | 1507953 | 15 | 33 | nan | nan | nan | Amazônia | 10.1 |
| f10d2137-c8e9-394b-b662-1b12e2b3af3f | -0.67825 | -51.68316 | 2024-11-02 05:48:00 | AQUA_M-M | MAZAGÃO | AMAPÁ | Brasil | 1600402 | 16 | 33 | nan | nan | nan | Amazônia | 14.4 |
| 9dc9f94d-e084-3cf9-a8b5-d9b198a46c69 | -0.67957 | -51.67439 | 2024-11-02 05:48:00 | AQUA_M-M | MAZAGÃO | AMAPÁ | Brasil | 1600402 | 16 | 33 | nan | nan | nan | Amazônia | 13.3 |
| 418ec704-cc07-39fb-9564-13040abc10a5 | -1.08653 | -53.6441 | 2024-11-02 05:48:00 | AQUA_M-M | ALMEIRIM | PARÁ | Brasil | 1500503 | 15 | 33 | nan | nan | nan | Amazônia | 4.7 |
| 4dab13fe-d0f6-3c0b-b5cd-7bc07d5e6545 | -1.16258 | -54.17373 | 2024-11-02 05:48:00 | AQUA_M-M | MONTE ALEGRE | PARÁ | Brasil | 1504802 | 15 | 33 | nan | nan | nan | Amazônia | 16.3 |
| 4feadc3d-f246-3cd7-ad26-dc389836c7f2 | -1.17195 | -54.17514 | 2024-11-02 05:48:00 | AQUA_M-M | MONTE ALEGRE | PARÁ | Brasil | 1504802 | 15 | 33 | nan | nan | nan | Amazônia | 9.8 |
| 3b7aaf2d-e94f-3177-9bc2-3852cb9a1318 | -1.18159 | -53.68375 | 2024-11-02 05:48:00 | AQUA_M-M | PRAINHA | PARÁ | Brasil | 1506005 | 15 | 33 | nan | nan | nan | Amazônia | 8.0 |
| cb6b8f04-398e-3aec-ac21-1df46a9c9e5e | -1.18722 | -53.64626 | 2024-11-02 05:48:00 | AQUA_M-M | PRAINHA | PARÁ | Brasil | 1506005 | 15 | 33 | nan | nan | nan | Amazônia | 4.9 |
| 6b598814-996a-3488-899c-07efb21e1988 | -1.19075 | -53.68507 | 2024-11-02 05:48:00 | AQUA_M-M | PRAINHA | PARÁ | Brasil | 1506005 | 15 | 33 | nan | nan | nan | Amazônia | 5.7 |
| ed4049c5-be76-333a-aad4-8d7977f7a654 | -1.19378 | -53.90666 | 2024-11-02 05:48:00 | AQUA_M-M | MONTE ALEGRE | PARÁ | Brasil | 1504802 | 15 | 33 | nan | nan | nan | Amazônia | 4.9 |
| 6989b219-31a1-3d85-88cf-8d031478f06e | -1.20153 | -53.91791 | 2024-11-02 05:48:00 | AQUA_M-M | MONTE ALEGRE | PARÁ | Brasil | 1504802 | 15 | 33 | nan | nan | nan | Amazônia | 8.9 |
| 7f5f88de-dff7-3268-86b7-f59b691fe6d7 | -6.22656 | -55.65083 | 2024-11-02 05:50:00 | AQUA_M-M | ITAITUBA | PARÁ | Brasil | 1503606 | 15 | 33 | nan | nan | nan | Amazônia | 15.3 |
| db0a832c-9009-3ec0-a9d7-2df4baf9be7b | -6.22495 | -55.66123 | 2024-11-02 05:50:00 | AQUA_M-M | ITAITUBA | PARÁ | Brasil | 1503606 | 15 | 33 | nan | nan | nan | Amazônia | 7.3 |
| 5b0ed5ab-9b33-38c4-87ff-c95d9009a00e | 3.31738 | -59.91285 | 2024-11-02 05:50:00 | NOAA-20 | BONFIM | RORAIMA | Brasil | 1400159 | 14 | 33 | nan | nan | nan | Amazônia | 3.1 |
| 66b2f938-4440-31d1-9f6e-0ce40fead3be | 4.38489 | -60.70042 | 2024-11-02 05:50:00 | NOAA-20 | PACARAIMA | RORAIMA | Brasil | 1400456 | 14 | 33 | nan | nan | nan | Amazônia | 1.6 |
| 7ae80341-7bd1-307c-a1c8-96aadfbda0b5 | 4.38428 | -60.69678 | 2024-11-02 05:50:00 | NOAA-20 | PACARAIMA | RORAIMA | Brasil | 1400456 | 14 | 33 | nan | nan | nan | Amazônia | 1.9 |
| dd9b9acd-82cd-3127-a321-2b304b4549aa | 4.38081 | -60.70127 | 2024-11-02 05:50:00 | NOAA-20 | PACARAIMA | RORAIMA | Brasil | 1400456 | 14 | 33 | nan | nan | nan | Amazônia | 1.6 |
| 41ab798d-66ce-37a3-8616-b50f62911d02 | 2.98587 | -61.20058 | 2024-11-02 05:50:00 | NOAA-20 | ALTO ALEGRE | RORAIMA | Brasil | 1400050 | 14 | 33 | nan | nan | nan | Amazônia | 0.7 |
| b9b928be-84da-340d-a4cb-cc208db06fb9 | 2.57898 | -60.69825 | 2024-11-02 05:50:00 | NOAA-20 | CANTÁ | RORAIMA | Brasil | 1400175 | 14 | 33 | nan | nan | nan | Amazônia | 2.7 |
| 80d15d3c-89d9-33cf-ae43-dde25b05f729 | 2.22699 | -61.67196 | 2024-11-02 05:50:00 | NOAA-20 | IRACEMA | RORAIMA | Brasil | 1400282 | 14 | 33 | nan | nan | nan | Amazônia | 1.1 |
| 63f287bc-d8e0-3cfd-946d-411cdcccc40f | 1.38266 | -60.80369 | 2024-11-02 05:50:00 | NOAA-20 | CARACARAÍ | RORAIMA | Brasil | 1400209 | 14 | 33 | nan | nan | nan | Amazônia | 1.6 |
| 46cd71dc-4175-3f15-b010-18a96c298ef3 | -11.11451 | -68.58633 | 2024-11-02 05:53:00 | NOAA-20 | EPITACIOLÂNDIA | ACRE | Brasil | 1200252 | 12 | 33 | nan | nan | nan | Amazônia | 0.2 |
| fd1d49e6-4a0c-3253-b3d2-635fd398fc60 | -11.11397 | -68.5899 | 2024-11-02 05:53:00 | NOAA-20 | EPITACIOLÂNDIA | ACRE | Brasil | 1200252 | 12 | 33 | nan | nan | nan | Amazônia | 0.3 |
| e96737e1-c941-3791-b01c-e152f54fffad | -1.52152 | -54.27977 | 2024-11-02 05:53:00 | NOAA-20 | MONTE ALEGRE | PARÁ | Brasil | 1504802 | 15 | 33 | nan | nan | nan | Amazônia | 4.8 |
| 3054962c-5bef-331a-a2d4-68bb25b8cbe8 | -1.52128 | -54.27937 | 2024-11-02 05:53:00 | NOAA-20 | MONTE ALEGRE | PARÁ | Brasil | 1504802 | 15 | 33 | nan | nan | nan | Amazônia | 4.8 |
| e63452a1-d7de-3484-8554-5b78379bc2f9 | -1.52063 | -54.28563 | 2024-11-02 05:53:00 | NOAA-20 | MONTE ALEGRE | PARÁ | Brasil | 1504802 | 15 | 33 | nan | nan | nan | Amazônia | 4.8 |
| 8694b236-0ec2-3534-85a6-31656be75928 | -1.52036 | -54.28521 | 2024-11-02 05:53:00 | NOAA-20 | MONTE ALEGRE | PARÁ | Brasil | 1504802 | 15 | 33 | nan | nan | nan | Amazônia | 7.1 |
| d685af5d-aebd-35ed-8727-26627b6855f1 | -1.20792 | -53.65585 | 2024-11-02 05:53:00 | NOAA-20 | PRAINHA | PARÁ | Brasil | 1506005 | 15 | 33 | nan | nan | nan | Amazônia | 4.4 |
| 45a68b41-1d7f-3298-a254-63f677ee4a60 | -1.20415 | -53.91224 | 2024-11-02 05:53:00 | NOAA-20 | MONTE ALEGRE | PARÁ | Brasil | 1504802 | 15 | 33 | nan | nan | nan | Amazônia | 13.0 |
| 29af65b4-3126-306d-8ac1-d6851e0e0f4a | -1.20314 | -53.91045 | 2024-11-02 05:53:00 | NOAA-20 | MONTE ALEGRE | PARÁ | Brasil | 1504802 | 15 | 33 | nan | nan | nan | Amazônia | 16.5 |
| 65d62293-d416-344d-9754-cebc6c8c396a | -1.20287 | -53.92044 | 2024-11-02 05:53:00 | NOAA-20 | MONTE ALEGRE | PARÁ | Brasil | 1504802 | 15 | 33 | nan | nan | nan | Amazônia | 12.0 |
| 2ed8b831-6db2-3258-a05c-e234ee0de939 | -1.20198 | -53.91822 | 2024-11-02 05:53:00 | NOAA-20 | MONTE ALEGRE | PARÁ | Brasil | 1504802 | 15 | 33 | nan | nan | nan | Amazônia | 16.5 |
| fde09bb9-c6a8-3f01-8e2b-a954ac8f019f | -1.19699 | -53.91227 | 2024-11-02 05:53:00 | NOAA-20 | MONTE ALEGRE | PARÁ | Brasil | 1504802 | 15 | 33 | nan | nan | nan | Amazônia | 13.0 |
| 4a368c60-0e3e-3d5d-889b-2441594dd8e1 | -1.19589 | -53.91935 | 2024-11-02 05:53:00 | NOAA-20 | MONTE ALEGRE | PARÁ | Brasil | 1504802 | 15 | 33 | nan | nan | nan | Amazônia | 12.0 |
| 273696a3-4298-3768-bb89-731df7629c0d | -1.18807 | -53.69065 | 2024-11-02 05:53:00 | NOAA-20 | PRAINHA | PARÁ | Brasil | 1506005 | 15 | 33 | nan | nan | nan | Amazônia | 2.6 |
| 0a227ef1-488b-344d-a91d-2e37a9c900a9 | -1.18701 | -53.69752 | 2024-11-02 05:53:00 | NOAA-20 | PRAINHA | PARÁ | Brasil | 1506005 | 15 | 33 | nan | nan | nan | Amazônia | 2.2 |
| 1be00334-c6cf-3cbc-af4f-ff0348901e16 | -1.18397 | -53.69021 | 2024-11-02 05:53:00 | NOAA-20 | PRAINHA | PARÁ | Brasil | 1506005 | 15 | 33 | nan | nan | nan | Amazônia | 2.2 |
| 4c04c317-ed14-318e-a90a-df516228894d | -1.18283 | -53.69734 | 2024-11-02 05:53:00 | NOAA-20 | PRAINHA | PARÁ | Brasil | 1506005 | 15 | 33 | nan | nan | nan | Amazônia | 2.2 |
| 9b2f50b8-339d-34ef-a2de-fb1491923940 | -1.16201 | -54.09113 | 2024-11-02 05:53:00 | NOAA-20 | MONTE ALEGRE | PARÁ | Brasil | 1504802 | 15 | 33 | nan | nan | nan | Amazônia | 2.5 |
| 2e62d0b9-554a-35e3-90f6-48b3f9ab98a3 | -3.31123 | -54.1367 | 2024-11-02 05:53:00 | NOAA-20 | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | 1.5 |
| 23669446-b725-3b6a-a63a-aa019e923a29 | -3.31023 | -54.14372 | 2024-11-02 05:53:00 | NOAA-20 | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | 1.5 |
| 80fcf42d-1873-39e9-aca4-b23bc5b5635a | -3.30421 | -54.13507 | 2024-11-02 05:53:00 | NOAA-20 | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | 2.5 |
| d2bb4432-2a76-39b4-a243-062c1beb397a | -3.12578 | -54.25873 | 2024-11-02 05:53:00 | NOAA-20 | MOJUÍ DOS CAMPOS | PARÁ | Brasil | 1504752 | 15 | 33 | nan | nan | nan | Amazônia | 6.9 |
| 8daa0001-3d91-314b-a9ed-c5afd844e249 | -3.12475 | -54.26577 | 2024-11-02 05:53:00 | NOAA-20 | MOJUÍ DOS CAMPOS | PARÁ | Brasil | 1504752 | 15 | 33 | nan | nan | nan | Amazônia | 7.4 |
| d7db9cb4-fd99-3cef-9448-3689e3d1d132 | -3.11886 | -54.30616 | 2024-11-02 05:53:00 | NOAA-20 | MOJUÍ DOS CAMPOS | PARÁ | Brasil | 1504752 | 15 | 33 | nan | nan | nan | Amazônia | 1.9 |
| f23adffe-3bc9-3ce7-8070-ee60b46781fd | -3.11871 | -54.25802 | 2024-11-02 05:53:00 | NOAA-20 | MOJUÍ DOS CAMPOS | PARÁ | Brasil | 1504752 | 15 | 33 | nan | nan | nan | Amazônia | 13.5 |
| 8ed61f5a-a2c6-3c29-bae3-ed32685f2da9 | -3.1177 | -54.26497 | 2024-11-02 05:53:00 | NOAA-20 | MOJUÍ DOS CAMPOS | PARÁ | Brasil | 1504752 | 15 | 33 | nan | nan | nan | Amazônia | 9.6 |
| 2a5fae22-36a2-3fe8-9086-44adf9f7a4fc | -3.11669 | -54.27184 | 2024-11-02 05:53:00 | NOAA-20 | MOJUÍ DOS CAMPOS | PARÁ | Brasil | 1504752 | 15 | 33 | nan | nan | nan | Amazônia | 9.6 |
| 0c1b7624-6a23-3046-86e2-a43f1abca26d | -3.11572 | -54.27856 | 2024-11-02 05:53:00 | NOAA-20 | MOJUÍ DOS CAMPOS | PARÁ | Brasil | 1504752 | 15 | 33 | nan | nan | nan | Amazônia | 2.4 |
| c217d250-2b81-3924-8f8d-1f7e3f98549e | -3.1128 | -54.2986 | 2024-11-02 05:53:00 | NOAA-20 | MOJUÍ DOS CAMPOS | PARÁ | Brasil | 1504752 | 15 | 33 | nan | nan | nan | Amazônia | 4.3 |
| db00fc56-74e3-301b-87ea-554b28e9d910 | -3.11266 | -54.26247 | 2024-11-02 05:53:00 | NOAA-20 | MOJUÍ DOS CAMPOS | PARÁ | Brasil | 1504752 | 15 | 33 | nan | nan | nan | Amazônia | 3.4 |
| 927c7c21-2d20-3b2d-85a5-94b3f6891d45 | -3.11162 | -54.26933 | 2024-11-02 05:53:00 | NOAA-20 | MOJUÍ DOS CAMPOS | PARÁ | Brasil | 1504752 | 15 | 33 | nan | nan | nan | Amazônia | 5.2 |
| 6dd7fae9-b2d9-30da-b64f-076aeacd28d2 | -3.10959 | -54.2827 | 2024-11-02 05:53:00 | NOAA-20 | MOJUÍ DOS CAMPOS | PARÁ | Brasil | 1504752 | 15 | 33 | nan | nan | nan | Amazônia | 3.2 |
| cb46dbb9-dcaf-3401-9130-1cce2140ba96 | -3.1087 | -54.27753 | 2024-11-02 05:53:00 | NOAA-20 | MOJUÍ DOS CAMPOS | PARÁ | Brasil | 1504752 | 15 | 33 | nan | nan | nan | Amazônia | 2.4 |
| dc565464-d881-39a9-8afa-0a1eb925ad40 | -3.10857 | -54.28937 | 2024-11-02 05:53:00 | NOAA-20 | MOJUÍ DOS CAMPOS | PARÁ | Brasil | 1504752 | 15 | 33 | nan | nan | nan | Amazônia | 3.2 |
| 3ee578c3-20bc-33a1-95e4-c84ce672d9a1 | -3.10773 | -54.2842 | 2024-11-02 05:53:00 | NOAA-20 | MOJUÍ DOS CAMPOS | PARÁ | Brasil | 1504752 | 15 | 33 | nan | nan | nan | Amazônia | 2.4 |
| 5d11137c-1150-3612-8416-5dbd927dcf64 | -3.10756 | -54.29607 | 2024-11-02 05:53:00 | NOAA-20 | MOJUÍ DOS CAMPOS | PARÁ | Brasil | 1504752 | 15 | 33 | nan | nan | nan | Amazônia | 5.6 |
| e56ec257-4991-301f-9a2a-e6c9154838e3 | -3.10675 | -54.2909 | 2024-11-02 05:53:00 | NOAA-20 | MOJUÍ DOS CAMPOS | PARÁ | Brasil | 1504752 | 15 | 33 | nan | nan | nan | Amazônia | 4.3 |
| c657dc5c-1819-3299-9f08-00e94e6cb05d | -3.10579 | -54.29755 | 2024-11-02 05:53:00 | NOAA-20 | MOJUÍ DOS CAMPOS | PARÁ | Brasil | 1504752 | 15 | 33 | nan | nan | nan | Amazônia | 4.3 |
| f94ee2bd-feb4-3c15-8aeb-5c30e2cf5547 | -3.10156 | -54.28835 | 2024-11-02 05:53:00 | NOAA-20 | MOJUÍ DOS CAMPOS | PARÁ | Brasil | 1504752 | 15 | 33 | nan | nan | nan | Amazônia | 3.2 |
| 177a4172-6756-34a2-a1d0-5f6c8426f0f8 | -3.10072 | -54.28313 | 2024-11-02 05:53:00 | NOAA-20 | MOJUÍ DOS CAMPOS | PARÁ | Brasil | 1504752 | 15 | 33 | nan | nan | nan | Amazônia | 3.4 |
| 13287191-d657-39c2-ae83-6ed707a371fa | -3.10055 | -54.29504 | 2024-11-02 05:53:00 | NOAA-20 | MOJUÍ DOS CAMPOS | PARÁ | Brasil | 1504752 | 15 | 33 | nan | nan | nan | Amazônia | 5.6 |
| 7d8f4439-185a-36e5-b858-f72b5f51344f | -3.09974 | -54.28986 | 2024-11-02 05:53:00 | NOAA-20 | MOJUÍ DOS CAMPOS | PARÁ | Brasil | 1504752 | 15 | 33 | nan | nan | nan | Amazônia | 3.8 |
| ac320d47-8983-3487-92b5-ce8275689db7 | -3.08112 | -54.16926 | 2024-11-02 05:53:00 | NOAA-20 | SANTARÉM | PARÁ | Brasil | 1506807 | 15 | 33 | nan | nan | nan | Amazônia | 0.8 |
| f4aae898-15c1-3635-befb-a20db081ef2a | -3.07665 | -54.16693 | 2024-11-02 05:53:00 | NOAA-20 | SANTARÉM | PARÁ | Brasil | 1506807 | 15 | 33 | nan | nan | nan | Amazônia | 2.1 |
| 008e6aaa-b3b4-3df1-9164-52b41fb0662d | -3.07558 | -54.17412 | 2024-11-02 05:53:00 | NOAA-20 | SANTARÉM | PARÁ | Brasil | 1506807 | 15 | 33 | nan | nan | nan | Amazônia | 2.1 |
| 19beb98e-3db2-39d2-a9f8-58d370f9e7a4 | -3.07406 | -54.16826 | 2024-11-02 05:53:00 | NOAA-20 | SANTARÉM | PARÁ | Brasil | 1506807 | 15 | 33 | nan | nan | nan | Amazônia | 4.6 |
| c8ab54f5-c8ac-31fe-b734-325fe47897e1 | -3.06956 | -54.1661 | 2024-11-02 05:53:00 | NOAA-20 | SANTARÉM | PARÁ | Brasil | 1506807 | 15 | 33 | nan | nan | nan | Amazônia | 3.3 |
| ae76e7be-c69a-37d3-a26a-65eff9711048 | -3.06852 | -54.17313 | 2024-11-02 05:53:00 | NOAA-20 | SANTARÉM | PARÁ | Brasil | 1506807 | 15 | 33 | nan | nan | nan | Amazônia | 3.3 |
| 19239862-4e2e-3e20-bb31-24db72cc18e9 | -3.06697 | -54.16736 | 2024-11-02 05:53:00 | NOAA-20 | SANTARÉM | PARÁ | Brasil | 1506807 | 15 | 33 | nan | nan | nan | Amazônia | 4.6 |
| 0ef1bed9-4bb3-3585-ab82-e18051ca769d | -3.06247 | -54.16526 | 2024-11-02 05:53:00 | NOAA-20 | SANTARÉM | PARÁ | Brasil | 1506807 | 15 | 33 | nan | nan | nan | Amazônia | 3.3 |
| b504b2d8-8951-3ee4-83bd-3d87d1843825 | -3.06145 | -54.17213 | 2024-11-02 05:53:00 | NOAA-20 | SANTARÉM | PARÁ | Brasil | 1506807 | 15 | 33 | nan | nan | nan | Amazônia | 3.3 |
| c960970e-c000-362e-b548-5b984f06aee7 | -2.97196 | -53.91674 | 2024-11-02 05:53:00 | NOAA-20 | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | 1.0 |
| 835ae1cf-49b2-3098-85dc-b412c1bfd18d | -2.96478 | -53.91592 | 2024-11-02 05:53:00 | NOAA-20 | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | 1.0 |
| d51497c6-0474-369e-8040-126629163ab6 | -2.67877 | -54.03133 | 2024-11-02 05:53:00 | NOAA-20 | PRAINHA | PARÁ | Brasil | 1506005 | 15 | 33 | nan | nan | nan | Amazônia | 0.3 |
| 4f1897fc-c072-30e2-8a1c-0c9e1e802faf | -2.67173 | -54.02999 | 2024-11-02 05:53:00 | NOAA-20 | PRAINHA | PARÁ | Brasil | 1506005 | 15 | 33 | nan | nan | nan | Amazônia | 1.9 |
| 829deea8-99d4-34ea-82f6-1d5b284e2717 | -2.63874 | -54.26695 | 2024-11-02 05:53:00 | NOAA-20 | SANTARÉM | PARÁ | Brasil | 1506807 | 15 | 33 | nan | nan | nan | Amazônia | 2.4 |
| 9e2d5a58-a78c-3081-853c-8f7ef81d5289 | -2.63774 | -54.27359 | 2024-11-02 05:53:00 | NOAA-20 | SANTARÉM | PARÁ | Brasil | 1506807 | 15 | 33 | nan | nan | nan | Amazônia | 2.4 |
| 6a46db22-f097-30fd-be02-2cfc69d1bf47 | -2.63741 | -54.26857 | 2024-11-02 05:53:00 | NOAA-20 | SANTARÉM | PARÁ | Brasil | 1506807 | 15 | 33 | nan | nan | nan | Amazônia | 4.9 |
| 1a0f231b-f347-3402-8f68-1078a52aeeb1 | -2.45677 | -54.15561 | 2024-11-02 05:53:00 | NOAA-20 | PRAINHA | PARÁ | Brasil | 1506005 | 15 | 33 | nan | nan | nan | Amazônia | 2.4 |
| 04de6430-54bc-31ae-bcab-70cf41f1b5b9 | -2.45585 | -54.16191 | 2024-11-02 05:53:00 | NOAA-20 | PRAINHA | PARÁ | Brasil | 1506005 | 15 | 33 | nan | nan | nan | Amazônia | 1.8 |
| 7d79162d-88fe-303e-8f90-fe79bbc81109 | -4.42596 | -55.39452 | 2024-11-02 05:53:00 | NOAA-20 | RURÓPOLIS | PARÁ | Brasil | 1506195 | 15 | 33 | nan | nan | nan | Amazônia | 2.4 |
| c1b95671-6940-38d9-a6f5-13eba435e987 | -4.42255 | -55.39682 | 2024-11-02 05:53:00 | NOAA-20 | RURÓPOLIS | PARÁ | Brasil | 1506195 | 15 | 33 | nan | nan | nan | Amazônia | 1.6 |
| fda8e865-c29b-3357-8c6b-bfc26611cb45 | -4.41833 | -55.40005 | 2024-11-02 05:53:00 | NOAA-20 | RURÓPOLIS | PARÁ | Brasil | 1506195 | 15 | 33 | nan | nan | nan | Amazônia | 2.4 |
| e6bac8c7-9505-3f4e-b154-99fa328e4815 | -4.41584 | -55.39601 | 2024-11-02 05:53:00 | NOAA-20 | RURÓPOLIS | PARÁ | Brasil | 1506195 | 15 | 33 | nan | nan | nan | Amazônia | 1.6 |
| bf6410bf-66c4-347e-8ece-af62e1491ad4 | -4.41501 | -55.40196 | 2024-11-02 05:53:00 | NOAA-20 | RURÓPOLIS | PARÁ | Brasil | 1506195 | 15 | 33 | nan | nan | nan | Amazônia | 1.6 |


[Clique aqui para ver as próximas entradas](README101.md)
