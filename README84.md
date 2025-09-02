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

## Dados Diários - Página 84

| ID | Latitude | Longitude | Data/Hora GMT | Satélite | Município | Estado | País | Município ID | Estado ID | País ID | Dias sem Chuva | Precipitação | Risco de Fogo | Bioma | FRP |
|----|----------|-----------|---------------|----------|-----------|--------|------|--------------|-----------|---------|----------------|--------------|----------------|-------|-----|
| 22273808-5443-3e9b-93ac-a90c6f51cf4f | -7.59787 | -61.6112 | 2025-09-02 05:53:00 | NOAA-20 | MANICORÉ | AMAZONAS | Brasil | 1302702 | 13 | 33 | nan | nan | nan | Amazônia | 3.0 |
| 2fe6b23b-5e6a-39d8-a9e1-a55508eb7c87 | -7.56186 | -63.07478 | 2025-09-02 05:53:00 | NOAA-20 | HUMAITÁ | AMAZONAS | Brasil | 1301704 | 13 | 33 | nan | nan | nan | Amazônia | 2.4 |
| 1392b943-1ba8-3a65-8fb5-ce473449f895 | -7.17518 | -69.88495 | 2025-09-02 05:53:00 | NOAA-20 | EIRUNEPÉ | AMAZONAS | Brasil | 1301407 | 13 | 33 | nan | nan | nan | Amazônia | 1.5 |
| be6a0f22-4fc4-34bd-b072-42d9634c38d8 | -8.66225 | -62.83769 | 2025-09-02 05:53:00 | NOAA-20 | CANDEIAS DO JAMARI | RONDÔNIA | Brasil | 1100809 | 11 | 33 | nan | nan | nan | Amazônia | 3.0 |
| 6321c25d-4b24-3402-aa03-7d93dc846914 | -8.65891 | -62.61049 | 2025-09-02 05:53:00 | NOAA-20 | PORTO VELHO | RONDÔNIA | Brasil | 1100205 | 11 | 33 | nan | nan | nan | Amazônia | 1.3 |
| 6863c5cf-41f9-3e98-935f-aec06eae333c | -6.40492 | -58.20765 | 2025-09-02 05:53:00 | NOAA-20 | JACAREACANGA | PARÁ | Brasil | 1503754 | 15 | 33 | nan | nan | nan | Amazônia | 2.8 |
| 1e829914-13ce-357b-8d7a-5a6803cb0990 | -12.92866 | -56.99878 | 2025-09-02 05:55:00 | NOAA-20 | NOVA MARINGÁ | MATO GROSSO | Brasil | 5108907 | 51 | 33 | nan | nan | nan | Amazônia | 3.3 |
| 9a49b87c-f5a1-339b-bc83-f1ac704bfaa6 | -6.43334 | -55.62063 | 2025-09-02 05:55:00 | NOAA-20 | NOVO PROGRESSO | PARÁ | Brasil | 1505031 | 15 | 33 | nan | nan | nan | Amazônia | 3.3 |
| 46a59ef3-aa2e-37e6-8a76-73ed5df030eb | -12.93543 | -56.99948 | 2025-09-02 05:55:00 | NOAA-20 | NOVA MARINGÁ | MATO GROSSO | Brasil | 5108907 | 51 | 33 | nan | nan | nan | Amazônia | 3.5 |
| 2f4b096b-d115-36f4-9bab-b8b3377a29d7 | -9.54132 | -62.38971 | 2025-09-02 05:55:00 | NOAA-20 | MACHADINHO D'OESTE | RONDÔNIA | Brasil | 1100130 | 11 | 33 | nan | nan | nan | Amazônia | 1.8 |
| a2411533-986b-35db-8527-7f1534824d75 | -10.07234 | -68.26871 | 2025-09-02 05:55:00 | NOAA-20 | RIO BRANCO | ACRE | Brasil | 1200401 | 12 | 33 | nan | nan | nan | Amazônia | 0.5 |
| eb0ad307-0568-3c1f-b701-37313b3b69d7 | -8.97102 | -65.97057 | 2025-09-02 05:55:00 | NOAA-20 | LÁBREA | AMAZONAS | Brasil | 1302405 | 13 | 33 | nan | nan | nan | Amazônia | 2.1 |
| 0e5b2abe-9ff9-3856-983b-05eeae28a604 | -9.22366 | -71.62965 | 2025-09-02 05:55:00 | NOAA-20 | FEIJÓ | ACRE | Brasil | 1200302 | 12 | 33 | nan | nan | nan | Amazônia | 1.5 |
| f89df20b-b1e2-39ed-846d-5ecfc2b19a98 | -9.17174 | -71.634 | 2025-09-02 05:55:00 | NOAA-20 | JORDÃO | ACRE | Brasil | 1200328 | 12 | 33 | nan | nan | nan | Amazônia | 1.7 |
| a7236470-eb2b-364a-be0f-a906b5971b4b | -12.91978 | -56.99709 | 2025-09-02 05:55:00 | NOAA-20 | NOVA MARINGÁ | MATO GROSSO | Brasil | 5108907 | 51 | 33 | nan | nan | nan | Amazônia | 1.5 |
| 8fa697e7-1ada-3634-884a-108262a2f146 | -12.93186 | -56.96867 | 2025-09-02 05:55:00 | NOAA-20 | NOVA MARINGÁ | MATO GROSSO | Brasil | 5108907 | 51 | 33 | nan | nan | nan | Amazônia | 3.4 |
| e936cb42-d6b6-3429-bff7-dff28da967ec | -12.93606 | -56.99362 | 2025-09-02 05:55:00 | NOAA-20 | NOVA MARINGÁ | MATO GROSSO | Brasil | 5108907 | 51 | 33 | nan | nan | nan | Amazônia | 3.0 |
| ceaca7b0-9dcc-3a26-9953-0eea561bc2b8 | -8.96445 | -65.96529 | 2025-09-02 05:55:00 | NOAA-20 | LÁBREA | AMAZONAS | Brasil | 1302405 | 13 | 33 | nan | nan | nan | Amazônia | 1.2 |
| 92979bdd-b059-38cc-9fd0-5668dd5c6b9d | -8.96678 | -65.9742 | 2025-09-02 05:55:00 | NOAA-20 | LÁBREA | AMAZONAS | Brasil | 1302405 | 13 | 33 | nan | nan | nan | Amazônia | 6.0 |
| 7d0db59d-7186-31de-ae84-b9abace30de7 | -8.96805 | -65.96584 | 2025-09-02 05:55:00 | NOAA-20 | LÁBREA | AMAZONAS | Brasil | 1302405 | 13 | 33 | nan | nan | nan | Amazônia | 1.2 |
| 72a47320-2d40-3f3d-b7c7-97601e8d36e0 | -11.6526 | -57.36418 | 2025-09-02 05:55:00 | NOAA-20 | PORTO DOS GAÚCHOS | MATO GROSSO | Brasil | 5106802 | 51 | 33 | nan | nan | nan | Amazônia | 6.8 |
| ebe67673-18c8-3c78-b1fa-1c2ee7babc1f | -11.6591 | -57.3651 | 2025-09-02 05:55:00 | NOAA-20 | PORTO DOS GAÚCHOS | MATO GROSSO | Brasil | 5106802 | 51 | 33 | nan | nan | nan | Amazônia | 2.7 |
| bec7f4ba-2efd-3c15-a72e-d22e4c73b8c9 | -9.28086 | -63.72217 | 2025-09-02 05:55:00 | NOAA-20 | CANDEIAS DO JAMARI | RONDÔNIA | Brasil | 1100809 | 11 | 33 | nan | nan | nan | Amazônia | 1.2 |
| 300047cf-b4c9-33cb-a5d6-f4c62ee24993 | -8.97462 | -65.9711 | 2025-09-02 05:55:00 | NOAA-20 | LÁBREA | AMAZONAS | Brasil | 1302405 | 13 | 33 | nan | nan | nan | Amazônia | 2.1 |
| 626bafcc-64b5-370c-9c0e-d554124838ee | -5.32008 | -56.00351 | 2025-09-02 05:55:00 | NOAA-20 | TRAIRÃO | PARÁ | Brasil | 1508050 | 15 | 33 | nan | nan | nan | Amazônia | 1.8 |
| d4ff039f-0b2f-3518-a22c-bdd6f3ee5580 | -10.15767 | -69.03087 | 2025-09-02 05:55:00 | NOAA-20 | SENA MADUREIRA | ACRE | Brasil | 1200500 | 12 | 33 | nan | nan | nan | Amazônia | 0.8 |
| de0c6813-caf1-39c2-bcfc-e1c54f328120 | -9.4405 | -68.94846 | 2025-09-02 05:55:00 | NOAA-20 | SENA MADUREIRA | ACRE | Brasil | 1200500 | 12 | 33 | nan | nan | nan | Amazônia | 0.9 |
| ed73c9a2-58c9-3f4c-bfaa-3c37118077c3 | -12.60563 | -57.01097 | 2025-09-02 05:55:00 | NOAA-20 | NOVA MARINGÁ | MATO GROSSO | Brasil | 5108907 | 51 | 33 | nan | nan | nan | Amazônia | 4.0 |
| 7df3cdd8-8fc8-3847-adc5-aa34c724c567 | -12.63041 | -57.00565 | 2025-09-02 05:55:00 | NOAA-20 | NOVA MARINGÁ | MATO GROSSO | Brasil | 5108907 | 51 | 33 | nan | nan | nan | Amazônia | 1.6 |
| 9824d139-c0a8-31d4-8c59-a1b02d13a017 | -8.96318 | -65.97365 | 2025-09-02 05:55:00 | NOAA-20 | LÁBREA | AMAZONAS | Brasil | 1302405 | 13 | 33 | nan | nan | nan | Amazônia | 6.0 |
| 8ffe674a-0c55-3b88-8393-0ecd4f4895f1 | -8.97254 | -65.96935 | 2025-09-02 05:55:00 | NOAA-20 | LÁBREA | AMAZONAS | Brasil | 1302405 | 13 | 33 | nan | nan | nan | Amazônia | 1.6 |
| 811dbdf3-8961-355f-8177-eb4bac7aee1d | -9.54276 | -65.94889 | 2025-09-02 05:55:00 | NOAA-20 | PORTO VELHO | RONDÔNIA | Brasil | 1100205 | 11 | 33 | nan | nan | nan | Amazônia | 5.6 |
| 0501602d-1ad2-3a58-9e01-31d432a5456a | -8.34868 | -70.26005 | 2025-09-02 05:55:00 | NOAA-20 | FEIJÓ | ACRE | Brasil | 1200302 | 12 | 33 | nan | nan | nan | Amazônia | 0.4 |
| dc7e878e-1f63-3a32-be1c-e26f1f3c2c30 | -9.18431 | -67.77868 | 2025-09-02 05:55:00 | NOAA-20 | BOCA DO ACRE | AMAZONAS | Brasil | 1300706 | 13 | 33 | nan | nan | nan | Amazônia | 0.9 |
| bafcb828-76d2-3937-9bc0-17c1923f213f | -12.6095 | -57.00959 | 2025-09-02 05:55:00 | NOAA-20 | NOVA MARINGÁ | MATO GROSSO | Brasil | 5108907 | 51 | 33 | nan | nan | nan | Amazônia | 2.6 |
| 423d7026-9014-3cd6-9a49-cefee8a76c6c | -12.60277 | -57.00883 | 2025-09-02 05:55:00 | NOAA-20 | NOVA MARINGÁ | MATO GROSSO | Brasil | 5108907 | 51 | 33 | nan | nan | nan | Amazônia | 1.7 |
| 5bffe67c-b4db-3285-bd92-d1012cfb0953 | -9.17632 | -71.63381 | 2025-09-02 05:55:00 | NOAA-20 | JORDÃO | ACRE | Brasil | 1200328 | 12 | 33 | nan | nan | nan | Amazônia | 1.3 |
| ca82d56f-9783-359a-bfb0-e290f4d1a97e | -12.92449 | -56.95501 | 2025-09-02 05:55:00 | NOAA-20 | NOVA MARINGÁ | MATO GROSSO | Brasil | 5108907 | 51 | 33 | nan | nan | nan | Amazônia | 2.7 |
| 9add12df-4324-3cbb-a933-f027449c24f3 | -12.9252 | -56.94875 | 2025-09-02 05:55:00 | NOAA-20 | NOVA MARINGÁ | MATO GROSSO | Brasil | 5108907 | 51 | 33 | nan | nan | nan | Amazônia | 3.1 |
| 9259bf5a-1342-30b1-b45c-55481472b89a | -8.96893 | -65.96881 | 2025-09-02 05:55:00 | NOAA-20 | LÁBREA | AMAZONAS | Brasil | 1302405 | 13 | 33 | nan | nan | nan | Amazônia | 1.6 |
| ed177e4c-21f4-35a3-95d5-8322ccac3236 | -8.62068 | -69.49545 | 2025-09-02 05:55:00 | NOAA-20 | MANOEL URBANO | ACRE | Brasil | 1200344 | 12 | 33 | nan | nan | nan | Amazônia | 0.5 |
| fe488cc6-d5c0-3360-a0f2-b87f59c9c8c1 | -8.3481 | -70.26364 | 2025-09-02 05:55:00 | NOAA-20 | FEIJÓ | ACRE | Brasil | 1200302 | 12 | 33 | nan | nan | nan | Amazônia | 0.7 |
| 2dc2e84f-409f-3a0b-80c4-17432bbab32c | -9.51054 | -63.56618 | 2025-09-02 05:55:00 | NOAA-20 | PORTO VELHO | RONDÔNIA | Brasil | 1100205 | 11 | 33 | nan | nan | nan | Amazônia | 1.2 |
| a9006941-ef28-3cf0-85f4-a48b911a0a8f | -12.91772 | -56.9727 | 2025-09-02 05:55:00 | NOAA-20 | NOVA MARINGÁ | MATO GROSSO | Brasil | 5108907 | 51 | 33 | nan | nan | nan | Amazônia | 1.8 |
| 470dd7bd-2659-33ef-9625-061881d257ae | -12.91481 | -56.93506 | 2025-09-02 05:55:00 | NOAA-20 | NOVA MARINGÁ | MATO GROSSO | Brasil | 5108907 | 51 | 33 | nan | nan | nan | Amazônia | 2.3 |
| a4320fcd-aa15-3bc2-8813-837bb0c2167c | -10.26678 | -68.7894 | 2025-09-02 05:55:00 | NOAA-20 | RIO BRANCO | ACRE | Brasil | 1200401 | 12 | 33 | nan | nan | nan | Amazônia | 1.1 |
| 46e8ea7d-d84e-387e-9677-556aef6ff609 | -9.18094 | -67.77815 | 2025-09-02 05:55:00 | NOAA-20 | BOCA DO ACRE | AMAZONAS | Brasil | 1300706 | 13 | 33 | nan | nan | nan | Amazônia | 0.9 |
| a8c0a489-5374-330f-b460-c857fb437dec | -8.96954 | -65.96463 | 2025-09-02 05:55:00 | NOAA-20 | LÁBREA | AMAZONAS | Brasil | 1302405 | 13 | 33 | nan | nan | nan | Amazônia | 1.4 |
| bfbfdf28-dbb3-3975-b48b-6e819bfc27a7 | -12.63112 | -56.99954 | 2025-09-02 05:55:00 | NOAA-20 | NOVA MARINGÁ | MATO GROSSO | Brasil | 5108907 | 51 | 33 | nan | nan | nan | Amazônia | 1.6 |
| ae1be6a7-9ddf-3570-97c8-5629993a26da | -12.93262 | -57.00458 | 2025-09-02 05:55:00 | NOAA-20 | NOVA MARINGÁ | MATO GROSSO | Brasil | 5108907 | 51 | 33 | nan | nan | nan | Amazônia | 3.2 |
| f0449ae6-75b2-364d-b832-9517fec069be | -8.87055 | -71.26005 | 2025-09-02 05:55:00 | NOAA-20 | FEIJÓ | ACRE | Brasil | 1200302 | 12 | 33 | nan | nan | nan | Amazônia | 0.7 |
| 4aad314f-5956-3cdc-8e96-096eea2d5e4d | -9.73762 | -63.30139 | 2025-09-02 05:55:00 | NOAA-20 | ALTO PARAÍSO | RONDÔNIA | Brasil | 1100403 | 11 | 33 | nan | nan | nan | Amazônia | 1.5 |
| e588aecb-2ec6-39d9-86ce-7f21d6eb1d6a | -8.97614 | -65.96991 | 2025-09-02 05:55:00 | NOAA-20 | LÁBREA | AMAZONAS | Brasil | 1302405 | 13 | 33 | nan | nan | nan | Amazônia | 1.3 |
| 6c8207ec-5245-3ba8-8d44-e05bf5a3a440 | -12.41847 | -63.9088 | 2025-09-02 05:55:00 | NOAA-20 | COSTA MARQUES | RONDÔNIA | Brasil | 1100080 | 11 | 33 | nan | nan | nan | Amazônia | 1.1 |
| 132344af-2549-3bb7-9f43-8d92d9076c1d | -8.67699 | -70.59139 | 2025-09-02 05:55:00 | NOAA-20 | FEIJÓ | ACRE | Brasil | 1200302 | 12 | 33 | nan | nan | nan | Amazônia | 0.6 |
| 5668848f-41d1-32de-b0f9-7ee56ec8778d | -12.92248 | -56.97297 | 2025-09-02 05:55:00 | NOAA-20 | NOVA MARINGÁ | MATO GROSSO | Brasil | 5108907 | 51 | 33 | nan | nan | nan | Amazônia | 2.6 |
| b54b93e4-380b-33d5-a9d5-0718c33cd970 | -12.92027 | -56.94848 | 2025-09-02 05:55:00 | NOAA-20 | NOVA MARINGÁ | MATO GROSSO | Brasil | 5108907 | 51 | 33 | nan | nan | nan | Amazônia | 2.9 |
| ff862b40-c23f-30b7-858c-a4b19232264c | -8.97165 | -65.96638 | 2025-09-02 05:55:00 | NOAA-20 | LÁBREA | AMAZONAS | Brasil | 1302405 | 13 | 33 | nan | nan | nan | Amazônia | 2.1 |
| 7a2dfb28-fd9e-3e7e-a659-4d422cd96533 | -12.42757 | -63.90589 | 2025-09-02 05:55:00 | NOAA-20 | COSTA MARQUES | RONDÔNIA | Brasil | 1100080 | 11 | 33 | nan | nan | nan | Amazônia | 0.9 |
| 4c22dfe3-289d-33d2-89f8-cd0cf699a1d8 | -12.91835 | -56.96676 | 2025-09-02 05:55:00 | NOAA-20 | NOVA MARINGÁ | MATO GROSSO | Brasil | 5108907 | 51 | 33 | nan | nan | nan | Amazônia | 2.4 |
| fd208a4d-cbaf-3652-a033-3039b61e5591 | -10.53172 | -69.63184 | 2025-09-02 05:55:00 | NOAA-20 | ASSIS BRASIL | ACRE | Brasil | 1200054 | 12 | 33 | nan | nan | nan | Amazônia | 1.3 |
| 15d09961-a7b5-3c86-97fa-9770e1303e73 | -12.93863 | -56.96938 | 2025-09-02 05:55:00 | NOAA-20 | NOVA MARINGÁ | MATO GROSSO | Brasil | 5108907 | 51 | 33 | nan | nan | nan | Amazônia | 2.1 |
| 7b900817-5910-342a-a16b-13565f49e42d | -8.97315 | -65.96517 | 2025-09-02 05:55:00 | NOAA-20 | LÁBREA | AMAZONAS | Brasil | 1302405 | 13 | 33 | nan | nan | nan | Amazônia | 1.4 |
| 22cc0c57-46c2-37e3-be8d-925d9546f1bf | -8.61737 | -69.49491 | 2025-09-02 05:55:00 | NOAA-20 | MANOEL URBANO | ACRE | Brasil | 1200344 | 12 | 33 | nan | nan | nan | Amazônia | 0.6 |
| fda90a37-b1a8-3dc3-8edc-ff21e5a5a6ec | -8.44597 | -70.13949 | 2025-09-02 05:55:00 | NOAA-20 | FEIJÓ | ACRE | Brasil | 1200302 | 12 | 33 | nan | nan | nan | Amazônia | 1.0 |
| b01235e8-2f45-3b6e-902d-22416dab63f9 | -12.93056 | -56.96207 | 2025-09-02 05:55:00 | NOAA-20 | NOVA MARINGÁ | MATO GROSSO | Brasil | 5108907 | 51 | 33 | nan | nan | nan | Amazônia | 3.3 |
| a92cea4c-7035-3105-89ea-bfdf8ab87f8d | -12.91897 | -56.96082 | 2025-09-02 05:55:00 | NOAA-20 | NOVA MARINGÁ | MATO GROSSO | Brasil | 5108907 | 51 | 33 | nan | nan | nan | Amazônia | 2.4 |
| 14715bd9-4dca-36cd-9306-51e957deecf1 | -12.62369 | -57.00475 | 2025-09-02 05:55:00 | NOAA-20 | NOVA MARINGÁ | MATO GROSSO | Brasil | 5108907 | 51 | 33 | nan | nan | nan | Amazônia | 1.6 |
| 465ba38c-7850-3f9b-830a-7f0ffd859331 | -9.15947 | -70.81918 | 2025-09-02 05:55:00 | NOAA-20 | FEIJÓ | ACRE | Brasil | 1200302 | 12 | 33 | nan | nan | nan | Amazônia | 1.1 |
| 2a87cbfb-9e3c-3347-bfb8-531adf8a566c | -12.92447 | -56.97371 | 2025-09-02 05:55:00 | NOAA-20 | NOVA MARINGÁ | MATO GROSSO | Brasil | 5108907 | 51 | 33 | nan | nan | nan | Amazônia | 1.6 |
| 54efbbf6-de51-35a5-b72d-e549c0b77b2a | -8.62013 | -69.49894 | 2025-09-02 05:55:00 | NOAA-20 | MANOEL URBANO | ACRE | Brasil | 1200344 | 12 | 33 | nan | nan | nan | Amazônia | 0.5 |
| 075e8f84-91c4-3fe8-bbbf-8311b00746ea | -12.92591 | -56.94238 | 2025-09-02 05:55:00 | NOAA-20 | NOVA MARINGÁ | MATO GROSSO | Brasil | 5108907 | 51 | 33 | nan | nan | nan | Amazônia | 3.1 |
| 9c15c21f-d2c1-3b4c-91ea-bd32bd8d0c3d | -9.00903 | -65.69486 | 2025-09-02 05:55:00 | NOAA-20 | LÁBREA | AMAZONAS | Brasil | 1302405 | 13 | 33 | nan | nan | nan | Amazônia | 2.3 |
| 74471aeb-e917-3b0c-9b88-f6eeeb3957e4 | -8.97192 | -65.97353 | 2025-09-02 05:55:00 | NOAA-20 | LÁBREA | AMAZONAS | Brasil | 1302405 | 13 | 33 | nan | nan | nan | Amazônia | 1.6 |
| 8ae434ca-387c-3445-ba2a-12a44732e474 | -12.9164 | -56.96608 | 2025-09-02 05:55:00 | NOAA-20 | NOVA MARINGÁ | MATO GROSSO | Brasil | 5108907 | 51 | 33 | nan | nan | nan | Amazônia | 2.6 |
| 7216ba5c-e2ae-3d2d-a4c3-fc4931e838bf | -8.96255 | -65.97783 | 2025-09-02 05:55:00 | NOAA-20 | LÁBREA | AMAZONAS | Brasil | 1302405 | 13 | 33 | nan | nan | nan | Amazônia | 6.3 |
| d8ebf283-c470-3260-933e-ec3ef846e8c2 | -9.17282 | -71.63322 | 2025-09-02 05:55:00 | NOAA-20 | JORDÃO | ACRE | Brasil | 1200328 | 12 | 33 | nan | nan | nan | Amazônia | 2.5 |
| eff265c9-f555-3077-b502-3874d482c717 | -8.97526 | -65.96693 | 2025-09-02 05:55:00 | NOAA-20 | LÁBREA | AMAZONAS | Brasil | 1302405 | 13 | 33 | nan | nan | nan | Amazônia | 2.1 |
| e8623bb9-b91f-34d4-819d-5f4e93caa714 | -12.91962 | -56.95468 | 2025-09-02 05:55:00 | NOAA-20 | NOVA MARINGÁ | MATO GROSSO | Brasil | 5108907 | 51 | 33 | nan | nan | nan | Amazônia | 2.9 |
| 29eaddbf-09da-3e86-9daa-73bb4f20dea7 | -11.65972 | -57.35973 | 2025-09-02 05:55:00 | NOAA-20 | PORTO DOS GAÚCHOS | MATO GROSSO | Brasil | 5106802 | 51 | 33 | nan | nan | nan | Amazônia | 2.7 |
| f65347b4-5775-3671-9dcb-3af721bfafab | -8.96615 | -65.97837 | 2025-09-02 05:55:00 | NOAA-20 | LÁBREA | AMAZONAS | Brasil | 1302405 | 13 | 33 | nan | nan | nan | Amazônia | 6.3 |
| 7f5ba904-d242-3aa8-aea1-77c1ce3be6c9 | -12.93328 | -56.99878 | 2025-09-02 05:55:00 | NOAA-20 | NOVA MARINGÁ | MATO GROSSO | Brasil | 5108907 | 51 | 33 | nan | nan | nan | Amazônia | 5.0 |
| 80d72356-242d-3c90-8cd4-18f752cdcea9 | -12.93926 | -56.96345 | 2025-09-02 05:55:00 | NOAA-20 | NOVA MARINGÁ | MATO GROSSO | Brasil | 5108907 | 51 | 33 | nan | nan | nan | Amazônia | 2.1 |
| 4a54c2c2-3ed6-3ae3-a24e-c005cca93a9f | -12.92509 | -56.96777 | 2025-09-02 05:55:00 | NOAA-20 | NOVA MARINGÁ | MATO GROSSO | Brasil | 5108907 | 51 | 33 | nan | nan | nan | Amazônia | 3.4 |
| 91d313ce-3728-3594-bdc1-5133e0138e9a | -12.92159 | -56.93587 | 2025-09-02 05:55:00 | NOAA-20 | NOVA MARINGÁ | MATO GROSSO | Brasil | 5108907 | 51 | 33 | nan | nan | nan | Amazônia | 2.3 |
| b79d1526-d755-36cd-957a-b499be5eaa52 | -9.0065 | -69.43994 | 2025-09-02 05:55:00 | NOAA-20 | MANOEL URBANO | ACRE | Brasil | 1200344 | 12 | 33 | nan | nan | nan | Amazônia | 1.1 |
| fc4fa50a-70e6-3436-b986-b174c62a3f37 | -9.1212 | -65.7692 | 2025-09-02 05:55:00 | NOAA-20 | LÁBREA | AMAZONAS | Brasil | 1302405 | 13 | 33 | nan | nan | nan | Amazônia | 1.3 |
| 9ee5187c-99e3-37e1-b912-fe4b1d1a88ef | -12.92637 | -56.9557 | 2025-09-02 05:55:00 | NOAA-20 | NOVA MARINGÁ | MATO GROSSO | Brasil | 5108907 | 51 | 33 | nan | nan | nan | Amazônia | 3.7 |
| e0d4325b-102d-30af-ab82-20eb5879f899 | -12.92572 | -56.96186 | 2025-09-02 05:55:00 | NOAA-20 | NOVA MARINGÁ | MATO GROSSO | Brasil | 5108907 | 51 | 33 | nan | nan | nan | Amazônia | 3.4 |
| 6fa32116-6778-36f2-a3fb-1a1d8a404a03 | -12.92381 | -56.96115 | 2025-09-02 05:55:00 | NOAA-20 | NOVA MARINGÁ | MATO GROSSO | Brasil | 5108907 | 51 | 33 | nan | nan | nan | Amazônia | 2.7 |
| a677cd6f-e5ab-3612-bb95-e939fa4da426 | -9.29852 | -71.00091 | 2025-09-02 05:55:00 | NOAA-20 | FEIJÓ | ACRE | Brasil | 1200302 | 12 | 33 | nan | nan | nan | Amazônia | 1.5 |
| 66159203-2419-3916-8eca-d84b9dd9dcc3 | -10.26346 | -68.78887 | 2025-09-02 05:55:00 | NOAA-20 | RIO BRANCO | ACRE | Brasil | 1200401 | 12 | 33 | nan | nan | nan | Amazônia | 1.0 |
| d1dd6be4-be2b-3390-83c0-548d7c69fe8e | -12.92652 | -56.99802 | 2025-09-02 05:55:00 | NOAA-20 | NOVA MARINGÁ | MATO GROSSO | Brasil | 5108907 | 51 | 33 | nan | nan | nan | Amazônia | 5.0 |
| 1e00891d-f6af-34df-882d-ff18507c3aba | -12.92092 | -56.94223 | 2025-09-02 05:55:00 | NOAA-20 | NOVA MARINGÁ | MATO GROSSO | Brasil | 5108907 | 51 | 33 | nan | nan | nan | Amazônia | 2.3 |
| 58f84a6a-e18c-3a9e-9db1-a54fca3d459e | -6.43147 | -55.61857 | 2025-09-02 05:55:00 | NOAA-20 | NOVO PROGRESSO | PARÁ | Brasil | 1505031 | 15 | 33 | nan | nan | nan | Amazônia | 3.8 |
| e8b441a3-6291-3a24-95e7-4bba33be70c0 | -12.92585 | -57.00398 | 2025-09-02 05:55:00 | NOAA-20 | NOVA MARINGÁ | MATO GROSSO | Brasil | 5108907 | 51 | 33 | nan | nan | nan | Amazônia | 3.2 |
| 1ec0cae6-43b8-34b8-8aa1-4a9981455ec5 | -12.93248 | -56.96272 | 2025-09-02 05:55:00 | NOAA-20 | NOVA MARINGÁ | MATO GROSSO | Brasil | 5108907 | 51 | 33 | nan | nan | nan | Amazônia | 3.4 |
| 31dabb24-c333-34da-8ed6-5e552168db3b | -8.87117 | -71.25623 | 2025-09-02 05:55:00 | NOAA-20 | FEIJÓ | ACRE | Brasil | 1200302 | 12 | 33 | nan | nan | nan | Amazônia | 0.7 |
| bbe2e0db-ac53-37cb-a2fb-6c8b19f74d77 | -12.42329 | -63.9053 | 2025-09-02 05:55:00 | NOAA-20 | COSTA MARQUES | RONDÔNIA | Brasil | 1100080 | 11 | 33 | nan | nan | nan | Amazônia | 1.1 |
| 89db4886-c5fb-3fde-ac3b-115cb241de8a | -12.91983 | -56.93534 | 2025-09-02 05:55:00 | NOAA-20 | NOVA MARINGÁ | MATO GROSSO | Brasil | 5108907 | 51 | 33 | nan | nan | nan | Amazônia | 4.7 |


[Clique aqui para ver as próximas entradas](README85.md)
