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

## Dados Diários - Página 57

| ID | Latitude | Longitude | Data/Hora GMT | Satélite | Município | Estado | País | Município ID | Estado ID | País ID | Dias sem Chuva | Precipitação | Risco de Fogo | Bioma | FRP |
|----|----------|-----------|---------------|----------|-----------|--------|------|--------------|-----------|---------|----------------|--------------|----------------|-------|-----|
| 0c659ae6-bd6a-35e4-a346-da5e62d49635 | -2.81948 | -46.62204 | 2024-11-02 05:04:00 | NOAA-21 | PARAGOMINAS | PARÁ | Brasil | 1505502 | 15 | 33 | nan | nan | nan | Amazônia | 0.7 |
| 988b17f2-5731-3a8e-bb51-b09d59a0538e | -2.6873 | -46.75645 | 2024-11-02 05:04:00 | NOAA-21 | PARAGOMINAS | PARÁ | Brasil | 1505502 | 15 | 33 | nan | nan | nan | Amazônia | 1.4 |
| 0f206d87-978c-3bcb-abe0-1c0e44831aa7 | -2.68716 | -46.7551 | 2024-11-02 05:04:00 | NOAA-21 | PARAGOMINAS | PARÁ | Brasil | 1505502 | 15 | 33 | nan | nan | nan | Amazônia | 1.3 |
| c0835cde-57a4-34d2-bc07-1bb58cf4841f | -2.68672 | -46.75797 | 2024-11-02 05:04:00 | NOAA-21 | PARAGOMINAS | PARÁ | Brasil | 1505502 | 15 | 33 | nan | nan | nan | Amazônia | 1.5 |
| b407695a-84ac-3d4f-9270-f0af8cad156c | -2.68312 | -46.75 | 2024-11-02 05:04:00 | NOAA-21 | PARAGOMINAS | PARÁ | Brasil | 1505502 | 15 | 33 | nan | nan | nan | Amazônia | 2.0 |
| 0bde1130-cc12-38c2-a630-c56edb93ef8d | -2.68271 | -46.75286 | 2024-11-02 05:04:00 | NOAA-21 | PARAGOMINAS | PARÁ | Brasil | 1505502 | 15 | 33 | nan | nan | nan | Amazônia | 1.9 |
| 1af8ff7e-4e76-372e-8c3d-d3ad98967f5a | -2.68259 | -46.75153 | 2024-11-02 05:04:00 | NOAA-21 | PARAGOMINAS | PARÁ | Brasil | 1505502 | 15 | 33 | nan | nan | nan | Amazônia | 1.3 |
| 43b5425e-9791-31e5-a46c-f7c05cce3a6e | -2.68215 | -46.7544 | 2024-11-02 05:04:00 | NOAA-21 | PARAGOMINAS | PARÁ | Brasil | 1505502 | 15 | 33 | nan | nan | nan | Amazônia | 1.3 |
| bc469441-2b5d-3ed4-9f85-5799dfc54c86 | -2.67935 | -46.74069 | 2024-11-02 05:04:00 | NOAA-21 | PARAGOMINAS | PARÁ | Brasil | 1505502 | 15 | 33 | nan | nan | nan | Amazônia | 1.2 |
| b1def280-9d4c-3f4b-a802-c71898b2a1d8 | -2.67932 | -46.73938 | 2024-11-02 05:04:00 | NOAA-21 | PARAGOMINAS | PARÁ | Brasil | 1505502 | 15 | 33 | nan | nan | nan | Amazônia | 1.1 |
| 414991d3-3360-385e-8d32-89d8dbede546 | -2.67894 | -46.74355 | 2024-11-02 05:04:00 | NOAA-21 | PARAGOMINAS | PARÁ | Brasil | 1505502 | 15 | 33 | nan | nan | nan | Amazônia | 1.2 |
| e5b6b5d1-84c3-3196-91ba-c7c2b972f193 | -2.67889 | -46.74224 | 2024-11-02 05:04:00 | NOAA-21 | PARAGOMINAS | PARÁ | Brasil | 1505502 | 15 | 33 | nan | nan | nan | Amazônia | 1.1 |
| ad6d68f3-96de-3210-a566-572438eff5df | -2.67852 | -46.74641 | 2024-11-02 05:04:00 | NOAA-21 | PARAGOMINAS | PARÁ | Brasil | 1505502 | 15 | 33 | nan | nan | nan | Amazônia | 2.0 |
| 270718e3-cd75-3f77-8329-da9e047c1269 | -2.67845 | -46.74509 | 2024-11-02 05:04:00 | NOAA-21 | PARAGOMINAS | PARÁ | Brasil | 1505502 | 15 | 33 | nan | nan | nan | Amazônia | 2.5 |
| 296d9233-427f-3760-8e43-7928939235ba | -2.67811 | -46.74926 | 2024-11-02 05:04:00 | NOAA-21 | PARAGOMINAS | PARÁ | Brasil | 1505502 | 15 | 33 | nan | nan | nan | Amazônia | 2.0 |
| cb36591b-fc91-3a2d-b825-b7dd9bbaa65b | -2.67802 | -46.74794 | 2024-11-02 05:04:00 | NOAA-21 | PARAGOMINAS | PARÁ | Brasil | 1505502 | 15 | 33 | nan | nan | nan | Amazônia | 2.5 |
| c0e8d1c6-a950-3e42-bdfd-9fe1d4ee3030 | -2.6777 | -46.75212 | 2024-11-02 05:04:00 | NOAA-21 | PARAGOMINAS | PARÁ | Brasil | 1505502 | 15 | 33 | nan | nan | nan | Amazônia | 1.9 |
| eaaacf76-c73b-360f-baed-1f870c571f86 | -2.67758 | -46.7508 | 2024-11-02 05:04:00 | NOAA-21 | PARAGOMINAS | PARÁ | Brasil | 1505502 | 15 | 33 | nan | nan | nan | Amazônia | 2.2 |
| a9fd518b-58d1-3f96-8019-82b2dd79d0fc | -2.67477 | -46.73565 | 2024-11-02 05:04:00 | NOAA-21 | PARAGOMINAS | PARÁ | Brasil | 1505502 | 15 | 33 | nan | nan | nan | Amazônia | 1.9 |
| 56c23eb5-2639-33fc-81c0-3b311ad62f6f | -2.67389 | -46.74142 | 2024-11-02 05:04:00 | NOAA-21 | PARAGOMINAS | PARÁ | Brasil | 1505502 | 15 | 33 | nan | nan | nan | Amazônia | 1.1 |
| 28f57b68-cb5b-3437-8188-4d3050bf2833 | -2.66172 | -46.75417 | 2024-11-02 05:04:00 | NOAA-21 | PARAGOMINAS | PARÁ | Brasil | 1505502 | 15 | 33 | nan | nan | nan | Amazônia | 1.4 |
| 709482dd-5db7-3543-8db2-7c9f8e604a47 | -2.60692 | -47.34237 | 2024-11-02 05:04:00 | NOAA-21 | IPIXUNA DO PARÁ | PARÁ | Brasil | 1503457 | 15 | 33 | nan | nan | nan | Amazônia | 1.9 |
| 8319652e-58c0-30ba-bf21-53eea80e2023 | -2.6064 | -47.34574 | 2024-11-02 05:04:00 | NOAA-21 | IPIXUNA DO PARÁ | PARÁ | Brasil | 1503457 | 15 | 33 | nan | nan | nan | Amazônia | 2.7 |
| 4f45052f-1c70-3fd1-ae46-cd6c42c6be06 | -2.59279 | -46.1465 | 2024-11-02 05:04:00 | NOAA-21 | CENTRO DO GUILHERME | MARANHÃO | Brasil | 2103158 | 21 | 33 | nan | nan | nan | Amazônia | 1.1 |
| d20de066-9454-39b2-a35e-4b40a325e782 | -2.59232 | -46.14968 | 2024-11-02 05:04:00 | NOAA-21 | CENTRO DO GUILHERME | MARANHÃO | Brasil | 2103158 | 21 | 33 | nan | nan | nan | Amazônia | 1.1 |
| 7ee002a5-2561-3565-908d-3a0ca0489ee2 | -2.57277 | -47.30866 | 2024-11-02 05:04:00 | NOAA-21 | CAPITÃO POÇO | PARÁ | Brasil | 1502301 | 15 | 33 | nan | nan | nan | Amazônia | 2.6 |
| 7c0eacaa-3f68-3168-accd-ad9a1c4cf467 | -2.56877 | -47.30265 | 2024-11-02 05:04:00 | NOAA-21 | CAPITÃO POÇO | PARÁ | Brasil | 1502301 | 15 | 33 | nan | nan | nan | Amazônia | 2.6 |
| af1de837-800e-3fb6-8f4b-614511b6446c | -2.56798 | -47.30788 | 2024-11-02 05:04:00 | NOAA-21 | CAPITÃO POÇO | PARÁ | Brasil | 1502301 | 15 | 33 | nan | nan | nan | Amazônia | 2.6 |
| 69cd429f-0555-3276-aa1f-04b08ab6a2dd | -3.30606 | -47.01141 | 2024-11-02 05:04:00 | NOAA-21 | PARAGOMINAS | PARÁ | Brasil | 1505502 | 15 | 33 | nan | nan | nan | Amazônia | 1.3 |
| c1a9a3f8-66a4-3fe5-895e-c122ec12e17e | -3.30503 | -47.00992 | 2024-11-02 05:04:00 | NOAA-21 | PARAGOMINAS | PARÁ | Brasil | 1505502 | 15 | 33 | nan | nan | nan | Amazônia | 1.9 |
| 7ca7aa43-c912-35b4-93f4-891fc90c3082 | -3.21679 | -46.17682 | 2024-11-02 05:04:00 | NOAA-21 | ZÉ DOCA | MARANHÃO | Brasil | 2114007 | 21 | 33 | nan | nan | nan | Amazônia | 6.6 |
| 831f5586-6f03-3f44-b869-b29d10126952 | -3.21632 | -46.18003 | 2024-11-02 05:04:00 | NOAA-21 | ZÉ DOCA | MARANHÃO | Brasil | 2114007 | 21 | 33 | nan | nan | nan | Amazônia | 6.6 |
| 9d0d0e28-df2c-3c63-b8db-fdfc6d06af59 | -3.21154 | -46.17603 | 2024-11-02 05:04:00 | NOAA-21 | ZÉ DOCA | MARANHÃO | Brasil | 2114007 | 21 | 33 | nan | nan | nan | Amazônia | 6.6 |
| 745df3a8-0a35-3f3c-878a-5b86de671f6a | -3.21107 | -46.17925 | 2024-11-02 05:04:00 | NOAA-21 | ZÉ DOCA | MARANHÃO | Brasil | 2114007 | 21 | 33 | nan | nan | nan | Amazônia | 6.6 |
| 2479b06e-0e5e-3e7d-9336-61f2bdaf78f7 | -3.18289 | -46.59144 | 2024-11-02 05:04:00 | NOAA-21 | CENTRO NOVO DO MARANHÃO | MARANHÃO | Brasil | 2103174 | 21 | 33 | nan | nan | nan | Amazônia | 2.0 |
| 6dfaf7e6-6a99-3f14-b912-9264944c1eb7 | -3.18245 | -46.59441 | 2024-11-02 05:04:00 | NOAA-21 | CENTRO NOVO DO MARANHÃO | MARANHÃO | Brasil | 2103174 | 21 | 33 | nan | nan | nan | Amazônia | 2.0 |
| 3c856250-0fe1-35e2-b0ec-7e8e273c6ad2 | -3.18202 | -46.59738 | 2024-11-02 05:04:00 | NOAA-21 | CENTRO NOVO DO MARANHÃO | MARANHÃO | Brasil | 2103174 | 21 | 33 | nan | nan | nan | Amazônia | 2.6 |
| 0efe1b65-3ee1-31b2-9638-35e9dfd24852 | -3.18158 | -46.60038 | 2024-11-02 05:04:00 | NOAA-21 | CENTRO NOVO DO MARANHÃO | MARANHÃO | Brasil | 2103174 | 21 | 33 | nan | nan | nan | Amazônia | 2.6 |
| 3585b6f1-26bb-37e0-9b2a-3850add2f072 | -3.17779 | -46.59066 | 2024-11-02 05:04:00 | NOAA-21 | CENTRO NOVO DO MARANHÃO | MARANHÃO | Brasil | 2103174 | 21 | 33 | nan | nan | nan | Amazônia | 1.9 |
| 03fc731b-c3e8-31ab-8936-d87fbe7b3ffd | -3.17736 | -46.59363 | 2024-11-02 05:04:00 | NOAA-21 | CENTRO NOVO DO MARANHÃO | MARANHÃO | Brasil | 2103174 | 21 | 33 | nan | nan | nan | Amazônia | 1.9 |
| 2f407d4c-136c-36d2-9847-0924271eb1d9 | -3.17692 | -46.59661 | 2024-11-02 05:04:00 | NOAA-21 | CENTRO NOVO DO MARANHÃO | MARANHÃO | Brasil | 2103174 | 21 | 33 | nan | nan | nan | Amazônia | 1.8 |
| cdc9af86-ef40-3227-8bb9-d4841a3963dd | -2.46451 | -46.14281 | 2024-11-02 05:04:00 | NOAA-21 | CENTRO DO GUILHERME | MARANHÃO | Brasil | 2103158 | 21 | 33 | nan | nan | nan | Amazônia | 1.1 |
| 56ecc305-97f0-3cbd-a61d-e62f24e8a5a7 | -2.44489 | -46.34867 | 2024-11-02 05:04:00 | NOAA-21 | CENTRO NOVO DO MARANHÃO | MARANHÃO | Brasil | 2103174 | 21 | 33 | nan | nan | nan | Amazônia | 1.2 |
| c336b2ad-745b-381d-a7f4-9427fccb342e | -2.44445 | -46.3517 | 2024-11-02 05:04:00 | NOAA-21 | CENTRO NOVO DO MARANHÃO | MARANHÃO | Brasil | 2103174 | 21 | 33 | nan | nan | nan | Amazônia | 1.1 |
| d1aaff08-21dd-357f-93a4-534bbc625606 | -2.444 | -46.35474 | 2024-11-02 05:04:00 | NOAA-21 | CENTRO NOVO DO MARANHÃO | MARANHÃO | Brasil | 2103174 | 21 | 33 | nan | nan | nan | Amazônia | 1.1 |
| 588f24c0-a514-33a0-bd86-0330266713a6 | -2.39047 | -46.5783 | 2024-11-02 05:04:00 | NOAA-21 | NOVA ESPERANÇA DO PIRIÁ | PARÁ | Brasil | 1504950 | 15 | 33 | nan | nan | nan | Amazônia | 0.9 |
| 36c2a3b0-1045-3287-a07e-a0cc2bd63074 | -2.38681 | -46.57309 | 2024-11-02 05:04:00 | NOAA-21 | NOVA ESPERANÇA DO PIRIÁ | PARÁ | Brasil | 1504950 | 15 | 33 | nan | nan | nan | Amazônia | 1.7 |
| a791b51c-8579-367f-8dd4-5278dc9823eb | -2.38586 | -46.57457 | 2024-11-02 05:04:00 | NOAA-21 | NOVA ESPERANÇA DO PIRIÁ | PARÁ | Brasil | 1504950 | 15 | 33 | nan | nan | nan | Amazônia | 1.2 |
| 8424b17b-25c4-3476-aea9-4c64bfb652cc | -2.38223 | -46.56931 | 2024-11-02 05:04:00 | NOAA-21 | NOVA ESPERANÇA DO PIRIÁ | PARÁ | Brasil | 1504950 | 15 | 33 | nan | nan | nan | Amazônia | 2.1 |
| dcc03d93-ec58-3817-941b-b21f64e71dd5 | -2.38178 | -46.57224 | 2024-11-02 05:04:00 | NOAA-21 | NOVA ESPERANÇA DO PIRIÁ | PARÁ | Brasil | 1504950 | 15 | 33 | nan | nan | nan | Amazônia | 0.8 |
| f364785b-2ed9-3179-8b9a-7823e0ac61e4 | -2.38168 | -46.56784 | 2024-11-02 05:04:00 | NOAA-21 | NOVA ESPERANÇA DO PIRIÁ | PARÁ | Brasil | 1504950 | 15 | 33 | nan | nan | nan | Amazônia | 1.1 |
| 57a6d8af-8151-3b20-b8d5-025b4ea13730 | -2.38133 | -46.57517 | 2024-11-02 05:04:00 | NOAA-21 | NOVA ESPERANÇA DO PIRIÁ | PARÁ | Brasil | 1504950 | 15 | 33 | nan | nan | nan | Amazônia | 0.8 |
| 8b21dbfa-aced-32a3-8157-e4c737670001 | -2.38125 | -46.57077 | 2024-11-02 05:04:00 | NOAA-21 | NOVA ESPERANÇA DO PIRIÁ | PARÁ | Brasil | 1504950 | 15 | 33 | nan | nan | nan | Amazônia | 1.1 |
| cae46e09-2746-343d-ba78-0bca9f1326e3 | -2.38083 | -46.57371 | 2024-11-02 05:04:00 | NOAA-21 | NOVA ESPERANÇA DO PIRIÁ | PARÁ | Brasil | 1504950 | 15 | 33 | nan | nan | nan | Amazônia | 1.2 |
| c6d88045-74de-3ea5-a9c3-0529ca4b5a62 | -2.37674 | -46.57143 | 2024-11-02 05:04:00 | NOAA-21 | NOVA ESPERANÇA DO PIRIÁ | PARÁ | Brasil | 1504950 | 15 | 33 | nan | nan | nan | Amazônia | 0.8 |
| 03d63760-a39e-364e-a644-97f227ba1a90 | -2.371 | -46.50726 | 2024-11-02 05:04:00 | NOAA-21 | CACHOEIRA DO PIRIÁ | PARÁ | Brasil | 1501956 | 15 | 33 | nan | nan | nan | Amazônia | 0.8 |
| 7a6d2a0a-e53d-3cef-9427-1bdd201f753a | -2.37055 | -46.51023 | 2024-11-02 05:04:00 | NOAA-21 | NOVA ESPERANÇA DO PIRIÁ | PARÁ | Brasil | 1504950 | 15 | 33 | nan | nan | nan | Amazônia | 1.3 |
| 15dc766b-4e0f-3de3-a469-7d868536139d | -2.36595 | -46.50637 | 2024-11-02 05:04:00 | NOAA-21 | CACHOEIRA DO PIRIÁ | PARÁ | Brasil | 1501956 | 15 | 33 | nan | nan | nan | Amazônia | 0.8 |
| 123a728f-9b9d-3f93-b7d8-6da736bf326d | -2.33753 | -46.5233 | 2024-11-02 05:04:00 | NOAA-21 | CACHOEIRA DO PIRIÁ | PARÁ | Brasil | 1501956 | 15 | 33 | nan | nan | nan | Amazônia | 1.1 |
| b579c3fb-71dc-311b-a11d-12118a493e0f | -2.3371 | -46.5262 | 2024-11-02 05:04:00 | NOAA-21 | CACHOEIRA DO PIRIÁ | PARÁ | Brasil | 1501956 | 15 | 33 | nan | nan | nan | Amazônia | 1.1 |
| f4468b3a-ef2e-38b3-8778-f3cb456a7217 | -2.33666 | -46.52909 | 2024-11-02 05:04:00 | NOAA-21 | CACHOEIRA DO PIRIÁ | PARÁ | Brasil | 1501956 | 15 | 33 | nan | nan | nan | Amazônia | 0.8 |
| cd0c7bf5-9272-3c1a-bbeb-c8f89486d4bc | -2.32742 | -46.52175 | 2024-11-02 05:04:00 | NOAA-21 | CACHOEIRA DO PIRIÁ | PARÁ | Brasil | 1501956 | 15 | 33 | nan | nan | nan | Amazônia | 1.2 |
| 62fabb2d-f2d7-3536-9560-c3c163ca0eef | -2.40092 | -48.58667 | 2024-11-02 05:04:00 | NOAA-21 | ACARÁ | PARÁ | Brasil | 1500206 | 15 | 33 | nan | nan | nan | Amazônia | 1.3 |
| 14d3b74f-d008-386c-9350-6a89ae431f8d | -2.3228 | -46.51804 | 2024-11-02 05:04:00 | NOAA-21 | CACHOEIRA DO PIRIÁ | PARÁ | Brasil | 1501956 | 15 | 33 | nan | nan | nan | Amazônia | 1.8 |
| 2395d3a0-bf4c-358b-9b61-b8fc207becc4 | -2.32236 | -46.52097 | 2024-11-02 05:04:00 | NOAA-21 | CACHOEIRA DO PIRIÁ | PARÁ | Brasil | 1501956 | 15 | 33 | nan | nan | nan | Amazônia | 1.2 |
| cde12462-1e31-38a4-98af-ebb5a15511a6 | -2.31774 | -46.51727 | 2024-11-02 05:04:00 | NOAA-21 | CACHOEIRA DO PIRIÁ | PARÁ | Brasil | 1501956 | 15 | 33 | nan | nan | nan | Amazônia | 1.5 |
| f263cebf-ab1a-3825-ae45-8e6a86cb5abf | -2.31269 | -46.51646 | 2024-11-02 05:04:00 | NOAA-21 | CACHOEIRA DO PIRIÁ | PARÁ | Brasil | 1501956 | 15 | 33 | nan | nan | nan | Amazônia | 1.5 |
| 0a0e4248-0725-35e5-8091-a3d5963b23db | -2.31225 | -46.51944 | 2024-11-02 05:04:00 | NOAA-21 | CACHOEIRA DO PIRIÁ | PARÁ | Brasil | 1501956 | 15 | 33 | nan | nan | nan | Amazônia | 2.0 |
| 5ef761a9-15d0-3a06-ac84-653d065980c5 | -2.24008 | -46.52351 | 2024-11-02 05:04:00 | NOAA-21 | CACHOEIRA DO PIRIÁ | PARÁ | Brasil | 1501956 | 15 | 33 | nan | nan | nan | Amazônia | 2.6 |
| 01a5d456-5b0f-3df6-9ff1-9feb3851977f | -2.23964 | -46.52645 | 2024-11-02 05:04:00 | NOAA-21 | CACHOEIRA DO PIRIÁ | PARÁ | Brasil | 1501956 | 15 | 33 | nan | nan | nan | Amazônia | 3.7 |
| c0201e5c-0807-303d-a692-4b4db34b7342 | -2.21903 | -46.5262 | 2024-11-02 05:04:00 | NOAA-21 | CACHOEIRA DO PIRIÁ | PARÁ | Brasil | 1501956 | 15 | 33 | nan | nan | nan | Amazônia | 1.5 |
| f554c33d-386f-3847-a75f-bd3b482eab68 | -2.2186 | -46.52913 | 2024-11-02 05:04:00 | NOAA-21 | CACHOEIRA DO PIRIÁ | PARÁ | Brasil | 1501956 | 15 | 33 | nan | nan | nan | Amazônia | 0.9 |
| b7d42c06-0f62-333b-938d-b457667c92c1 | -2.20162 | -46.4692 | 2024-11-02 05:04:00 | NOAA-21 | CACHOEIRA DO PIRIÁ | PARÁ | Brasil | 1501956 | 15 | 33 | nan | nan | nan | Amazônia | 0.7 |
| 8c7eaa23-5ffc-3fc4-ba05-778985103170 | -2.19655 | -46.46844 | 2024-11-02 05:04:00 | NOAA-21 | CACHOEIRA DO PIRIÁ | PARÁ | Brasil | 1501956 | 15 | 33 | nan | nan | nan | Amazônia | 1.8 |
| 8c30fd3b-58ab-3573-8e62-a3d1a15eda5c | -2.45092 | -46.89011 | 2024-11-02 05:04:00 | NOAA-21 | PARAGOMINAS | PARÁ | Brasil | 1505502 | 15 | 33 | nan | nan | nan | Amazônia | 8.8 |
| b0709eea-9fd5-3526-81d4-8e25263784a8 | -2.4476 | -46.89008 | 2024-11-02 05:04:00 | NOAA-21 | PARAGOMINAS | PARÁ | Brasil | 1505502 | 15 | 33 | nan | nan | nan | Amazônia | 12.2 |
| b9359e66-ed8b-3da2-8859-6747eaf455cb | -2.4194 | -46.69545 | 2024-11-02 05:04:00 | NOAA-21 | NOVA ESPERANÇA DO PIRIÁ | PARÁ | Brasil | 1504950 | 15 | 33 | nan | nan | nan | Amazônia | 0.6 |
| 0cad24e8-c4ed-34f3-8f59-84a72a27d0c9 | -2.4144 | -46.69469 | 2024-11-02 05:04:00 | NOAA-21 | NOVA ESPERANÇA DO PIRIÁ | PARÁ | Brasil | 1504950 | 15 | 33 | nan | nan | nan | Amazônia | 0.6 |
| 8937b75a-c1ec-3a4d-9289-b4dcd7f11125 | -2.40716 | -46.74326 | 2024-11-02 05:04:00 | NOAA-21 | NOVA ESPERANÇA DO PIRIÁ | PARÁ | Brasil | 1504950 | 15 | 33 | nan | nan | nan | Amazônia | 1.0 |
| 004336af-d144-31f9-b732-89ca8160e7f1 | -2.40674 | -46.74611 | 2024-11-02 05:04:00 | NOAA-21 | NOVA ESPERANÇA DO PIRIÁ | PARÁ | Brasil | 1504950 | 15 | 33 | nan | nan | nan | Amazônia | 1.0 |
| 647a80c6-1d9e-34ec-b856-d9222a72c245 | -2.37348 | -46.76435 | 2024-11-02 05:04:00 | NOAA-21 | NOVA ESPERANÇA DO PIRIÁ | PARÁ | Brasil | 1504950 | 15 | 33 | nan | nan | nan | Amazônia | 1.7 |
| 6f2d60da-8080-3a59-ba8b-1205ac071251 | -2.36785 | -46.80275 | 2024-11-02 05:04:00 | NOAA-21 | NOVA ESPERANÇA DO PIRIÁ | PARÁ | Brasil | 1504950 | 15 | 33 | nan | nan | nan | Amazônia | 3.3 |
| d307385c-f280-3b05-accf-68af00d94e12 | -2.36708 | -46.80072 | 2024-11-02 05:04:00 | NOAA-21 | NOVA ESPERANÇA DO PIRIÁ | PARÁ | Brasil | 1504950 | 15 | 33 | nan | nan | nan | Amazônia | 1.7 |
| c6e9f19e-bb46-31fb-8b5f-4a0b574b709d | -2.33314 | -46.62143 | 2024-11-02 05:04:00 | NOAA-21 | NOVA ESPERANÇA DO PIRIÁ | PARÁ | Brasil | 1504950 | 15 | 33 | nan | nan | nan | Amazônia | 0.9 |
| 73113932-d2b6-3d5f-b7f6-0837a0404af8 | -2.33226 | -46.62725 | 2024-11-02 05:04:00 | NOAA-21 | NOVA ESPERANÇA DO PIRIÁ | PARÁ | Brasil | 1504950 | 15 | 33 | nan | nan | nan | Amazônia | 2.1 |
| cf66da12-7add-398a-a7ab-95852b522df5 | -2.32812 | -46.62063 | 2024-11-02 05:04:00 | NOAA-21 | NOVA ESPERANÇA DO PIRIÁ | PARÁ | Brasil | 1504950 | 15 | 33 | nan | nan | nan | Amazônia | 0.9 |
| 4a92b3d5-f8ab-3714-9743-6ac0f8a70d00 | -2.28025 | -46.70164 | 2024-11-02 05:04:00 | NOAA-21 | NOVA ESPERANÇA DO PIRIÁ | PARÁ | Brasil | 1504950 | 15 | 33 | nan | nan | nan | Amazônia | 2.1 |
| e2d21ed2-8dc6-3ff4-9966-591b629b5741 | -2.27724 | -46.75648 | 2024-11-02 05:04:00 | NOAA-21 | NOVA ESPERANÇA DO PIRIÁ | PARÁ | Brasil | 1504950 | 15 | 33 | nan | nan | nan | Amazônia | 1.0 |
| 2a68339c-7060-347f-8ba5-c6ea758d3b56 | -2.27683 | -46.75928 | 2024-11-02 05:04:00 | NOAA-21 | NOVA ESPERANÇA DO PIRIÁ | PARÁ | Brasil | 1504950 | 15 | 33 | nan | nan | nan | Amazônia | 1.0 |
| 69e086c1-f02b-338d-83a6-614c2e8cb79e | -2.27642 | -46.76208 | 2024-11-02 05:04:00 | NOAA-21 | NOVA ESPERANÇA DO PIRIÁ | PARÁ | Brasil | 1504950 | 15 | 33 | nan | nan | nan | Amazônia | 4.6 |
| 3742b8bd-7d65-38ae-93e1-15af3a6a0c80 | -2.27442 | -46.70655 | 2024-11-02 05:04:00 | NOAA-21 | NOVA ESPERANÇA DO PIRIÁ | PARÁ | Brasil | 1504950 | 15 | 33 | nan | nan | nan | Amazônia | 2.2 |
| 214e5458-24e4-35a0-abf2-bba2a6a1caef | -2.274 | -46.70942 | 2024-11-02 05:04:00 | NOAA-21 | NOVA ESPERANÇA DO PIRIÁ | PARÁ | Brasil | 1504950 | 15 | 33 | nan | nan | nan | Amazônia | 0.9 |
| 63a2262c-0146-390b-9e52-10428c2cf33f | -2.27228 | -46.75568 | 2024-11-02 05:04:00 | NOAA-21 | NOVA ESPERANÇA DO PIRIÁ | PARÁ | Brasil | 1504950 | 15 | 33 | nan | nan | nan | Amazônia | 1.2 |
| baeb5227-733b-3beb-865c-22ddd761728a | -2.26944 | -46.70573 | 2024-11-02 05:04:00 | NOAA-21 | NOVA ESPERANÇA DO PIRIÁ | PARÁ | Brasil | 1504950 | 15 | 33 | nan | nan | nan | Amazônia | 1.6 |
| 07be95d6-7e38-3f18-b692-ec6bb78e6233 | -2.26365 | -46.67553 | 2024-11-02 05:04:00 | NOAA-21 | NOVA ESPERANÇA DO PIRIÁ | PARÁ | Brasil | 1504950 | 15 | 33 | nan | nan | nan | Amazônia | 2.3 |
| e31f62bd-44ec-33fa-b900-7b97b61ec26b | -2.26214 | -46.64918 | 2024-11-02 05:04:00 | NOAA-21 | NOVA ESPERANÇA DO PIRIÁ | PARÁ | Brasil | 1504950 | 15 | 33 | nan | nan | nan | Amazônia | 0.7 |
| 34e319ba-608a-3d12-a0a8-59a0c3a17499 | -2.2617 | -46.65203 | 2024-11-02 05:04:00 | NOAA-21 | NOVA ESPERANÇA DO PIRIÁ | PARÁ | Brasil | 1504950 | 15 | 33 | nan | nan | nan | Amazônia | 0.7 |
| 1aa4833e-bfb6-3c6c-884c-8e52f0a5dd1c | -2.25906 | -46.66922 | 2024-11-02 05:04:00 | NOAA-21 | NOVA ESPERANÇA DO PIRIÁ | PARÁ | Brasil | 1504950 | 15 | 33 | nan | nan | nan | Amazônia | 1.0 |
| cbbf1d64-aeb3-3e8c-9fa9-000c594ce788 | -2.2567 | -46.65124 | 2024-11-02 05:04:00 | NOAA-21 | NOVA ESPERANÇA DO PIRIÁ | PARÁ | Brasil | 1504950 | 15 | 33 | nan | nan | nan | Amazônia | 0.7 |
| e03aed3b-c864-3c5c-9ae8-4d8005371448 | -2.25451 | -46.66556 | 2024-11-02 05:04:00 | NOAA-21 | NOVA ESPERANÇA DO PIRIÁ | PARÁ | Brasil | 1504950 | 15 | 33 | nan | nan | nan | Amazônia | 1.0 |


[Clique aqui para ver as próximas entradas](README58.md)
