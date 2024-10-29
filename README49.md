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

## Dados Diários - Página 49

| ID | Latitude | Longitude | Data/Hora GMT | Satélite | Município | Estado | País | Município ID | Estado ID | País ID | Dias sem Chuva | Precipitação | Risco de Fogo | Bioma | FRP |
|----|----------|-----------|---------------|----------|-----------|--------|------|--------------|-----------|---------|----------------|--------------|----------------|-------|-----|
| 3746c547-1153-3294-9fee-ff8c2d6de897 | -2.53221 | -51.18639 | 2024-10-29 04:38:00 | NOAA-21 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 1.4 |
| 6f1e2ded-af22-3de2-bdf4-2cda68e84d74 | -2.53159 | -51.19032 | 2024-10-29 04:38:00 | NOAA-21 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 1.4 |
| 62e0e945-027f-3b70-99f8-799db52a5696 | -2.53056 | -51.17407 | 2024-10-29 04:38:00 | NOAA-21 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 2.6 |
| a1546b05-c60c-35fa-bb61-126644ed581c | -2.52993 | -51.17799 | 2024-10-29 04:38:00 | NOAA-21 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 1.3 |
| 50b1ab75-728b-3e54-8b0b-163ac75a21fa | -2.52931 | -51.18192 | 2024-10-29 04:38:00 | NOAA-21 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 1.3 |
| f184cf12-caed-352c-8624-4ad456b91d39 | -2.52869 | -51.18585 | 2024-10-29 04:38:00 | NOAA-21 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 1.4 |
| 4c347a54-31f7-3bc8-b36c-734140cbb22e | -2.52807 | -51.18978 | 2024-10-29 04:38:00 | NOAA-21 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 1.4 |
| d27d454f-78f6-3d98-8caa-7833e6fa9880 | -2.52744 | -51.19371 | 2024-10-29 04:38:00 | NOAA-21 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 2.1 |
| 255fae03-f4e8-39a7-bf3a-f9984a4c961a | -2.52704 | -51.17353 | 2024-10-29 04:38:00 | NOAA-21 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 1.6 |
| 0f8f453b-0282-355b-95fa-cd2286182363 | -2.52649 | -51.04141 | 2024-10-29 04:38:00 | NOAA-21 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 1.6 |
| e7635a18-aef1-348c-b6be-45942269d2b5 | -2.52642 | -51.17745 | 2024-10-29 04:38:00 | NOAA-21 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 1.5 |
| e6ea54b2-a2d6-366c-a6f9-0f521effc923 | -2.52587 | -51.04528 | 2024-10-29 04:38:00 | NOAA-21 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 1.6 |
| 3be4deec-f931-3b56-bac7-3f63f6801ec1 | -2.52579 | -51.18137 | 2024-10-29 04:38:00 | NOAA-21 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 1.5 |
| 62c92a9e-1832-3713-8e9d-6ed43a802063 | -2.52517 | -51.1853 | 2024-10-29 04:38:00 | NOAA-21 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 1.2 |
| b59a7904-2fb5-351b-8fcd-8d221def7dc8 | -2.52455 | -51.18923 | 2024-10-29 04:38:00 | NOAA-21 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 1.2 |
| 026b54fc-7276-3361-9079-89c17bdd75c7 | -2.52352 | -51.17299 | 2024-10-29 04:38:00 | NOAA-21 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 1.6 |
| fde23414-db78-3292-bb51-47ad9b3334dc | -2.5229 | -51.17691 | 2024-10-29 04:38:00 | NOAA-21 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 1.5 |
| debf7f85-f760-3ad5-bb54-8c59334a9525 | -2.52228 | -51.18082 | 2024-10-29 04:38:00 | NOAA-21 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 1.5 |
| cce469d8-638a-3e8d-91b3-4359afda2761 | -2.51876 | -51.18029 | 2024-10-29 04:38:00 | NOAA-21 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 1.9 |
| 3c4edac7-a9ce-3134-bb1c-95df0d11dfa1 | -2.51814 | -51.18421 | 2024-10-29 04:38:00 | NOAA-21 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 1.3 |
| a72163d2-1a96-31b4-b4e2-0be820ca9704 | -2.51462 | -51.18367 | 2024-10-29 04:38:00 | NOAA-21 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 1.3 |
| 08e04291-da57-3e53-86db-7cedf91e8aed | -2.5111 | -51.18314 | 2024-10-29 04:38:00 | NOAA-21 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 1.9 |
| f10cdd25-fff6-3c96-8c1c-d66174caa990 | -2.45095 | -50.98983 | 2024-10-29 04:38:00 | NOAA-21 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 1.6 |
| e4b572df-2d37-3c33-aeb4-51d0aab54f73 | -2.45034 | -50.9937 | 2024-10-29 04:38:00 | NOAA-21 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 1.6 |
| c06e80f7-0ec5-3bb5-bd68-98274f9ad7a3 | -2.41878 | -50.5041 | 2024-10-29 04:38:00 | NOAA-21 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 2.7 |
| 1137b616-69aa-3b54-99a7-f8e4245171ae | -3.27335 | -51.61096 | 2024-10-29 04:38:00 | NOAA-21 | ANAPU | PARÁ | Brasil | 1500859 | 15 | 33 | nan | nan | nan | Amazônia | 1.6 |
| b0169469-cf8c-3f33-9fad-2f10aa6c621e | -3.27269 | -51.615 | 2024-10-29 04:38:00 | NOAA-21 | ANAPU | PARÁ | Brasil | 1500859 | 15 | 33 | nan | nan | nan | Amazônia | 1.9 |
| 22a9f052-3617-3536-a9f5-9ca5bb920c71 | -3.0841 | -51.13771 | 2024-10-29 04:38:00 | NOAA-21 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 1.1 |
| 83a20c56-f107-3701-bfcd-81cfd9a6e719 | -3.07999 | -51.14105 | 2024-10-29 04:38:00 | NOAA-21 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 1.1 |
| 81ace8b2-a4ce-3047-8211-52cd8ed4d7a2 | -3.07529 | -51.35271 | 2024-10-29 04:38:00 | NOAA-21 | ANAPU | PARÁ | Brasil | 1500859 | 15 | 33 | nan | nan | nan | Amazônia | 2.1 |
| 2d58d84f-d671-3cc3-9e1e-815eab137447 | -3.07467 | -51.35666 | 2024-10-29 04:38:00 | NOAA-21 | ANAPU | PARÁ | Brasil | 1500859 | 15 | 33 | nan | nan | nan | Amazônia | 3.3 |
| 49030e30-6772-3af4-a2be-17c199aaf7c8 | -3.06307 | -51.33866 | 2024-10-29 04:38:00 | NOAA-21 | ANAPU | PARÁ | Brasil | 1500859 | 15 | 33 | nan | nan | nan | Amazônia | 1.1 |
| 77eadd46-d06a-3132-a970-e9a91f0e401f | -3.03551 | -51.4441 | 2024-10-29 04:38:00 | NOAA-21 | ANAPU | PARÁ | Brasil | 1500859 | 15 | 33 | nan | nan | nan | Amazônia | 2.9 |
| cf17c239-4072-3c33-8886-11616e7f7ff5 | -3.03297 | -51.46008 | 2024-10-29 04:38:00 | NOAA-21 | ANAPU | PARÁ | Brasil | 1500859 | 15 | 33 | nan | nan | nan | Amazônia | 1.7 |
| bf81247c-c1ef-3ce3-bc93-a46a004a16b4 | -3.03234 | -51.46405 | 2024-10-29 04:38:00 | NOAA-21 | ANAPU | PARÁ | Brasil | 1500859 | 15 | 33 | nan | nan | nan | Amazônia | 1.5 |
| 48adf77e-0c63-39c2-8fd2-8ea44b262542 | -3.03196 | -51.4436 | 2024-10-29 04:38:00 | NOAA-21 | ANAPU | PARÁ | Brasil | 1500859 | 15 | 33 | nan | nan | nan | Amazônia | 2.9 |
| 4c1b1480-f154-33a3-83bb-ec1e0be2ba13 | -2.95784 | -51.00006 | 2024-10-29 04:38:00 | NOAA-21 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 1.6 |
| 216a576e-65b7-33af-9ce8-e56b3b447e76 | -2.94227 | -51.41411 | 2024-10-29 04:38:00 | NOAA-21 | ANAPU | PARÁ | Brasil | 1500859 | 15 | 33 | nan | nan | nan | Amazônia | 1.0 |
| cdc58fb7-26e0-31fb-be45-0bad417297b0 | -2.22531 | -51.86913 | 2024-10-29 04:38:00 | NOAA-21 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 1.5 |
| 9991efd5-7520-3a24-83bc-3279d22211e7 | -2.22464 | -51.87339 | 2024-10-29 04:38:00 | NOAA-21 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 1.5 |
| 48d59893-98a3-36fc-8297-5a49d3c1092c | -2.22165 | -51.86856 | 2024-10-29 04:38:00 | NOAA-21 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 2.4 |
| cf94a81b-556f-3926-9dd7-d58b9a7a7031 | -2.22098 | -51.87283 | 2024-10-29 04:38:00 | NOAA-21 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 2.4 |
| 92a704f0-b5be-3885-b54e-6abecd8f4dd6 | -2.29171 | -50.66488 | 2024-10-29 04:38:00 | NOAA-21 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 0.9 |
| be4495fe-9ea7-3992-9e39-edbd37311488 | -2.28886 | -50.66056 | 2024-10-29 04:38:00 | NOAA-21 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 1.8 |
| 7f6074af-d3d4-35b4-9057-572893567fe3 | -2.28541 | -50.66002 | 2024-10-29 04:38:00 | NOAA-21 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 1.8 |
| ef39cfab-b68d-38c5-ae71-3cedd33960e9 | -2.25526 | -50.69404 | 2024-10-29 04:38:00 | NOAA-21 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 1.9 |
| ab129b13-5d36-364f-b54e-98afb57fc488 | -2.24836 | -50.69296 | 2024-10-29 04:38:00 | NOAA-21 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 1.7 |
| c0559047-e4c6-3d8f-ad17-5179b1da24c0 | -2.24715 | -50.70056 | 2024-10-29 04:38:00 | NOAA-21 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 1.7 |
| 6b03673a-ad35-37a5-a2b5-2df57cb921a4 | -2.23316 | -50.72165 | 2024-10-29 04:38:00 | NOAA-21 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 2.0 |
| 904becf8-865a-31a5-bebd-d706823f5ee1 | -3.00974 | -51.76904 | 2024-10-29 04:38:00 | NOAA-21 | SENADOR JOSÉ PORFÍRIO | PARÁ | Brasil | 1507805 | 15 | 33 | nan | nan | nan | Amazônia | 1.5 |
| 6782e8e6-d0b0-383c-bc50-8bd239eeafdd | -3.00909 | -51.7732 | 2024-10-29 04:38:00 | NOAA-21 | SENADOR JOSÉ PORFÍRIO | PARÁ | Brasil | 1507805 | 15 | 33 | nan | nan | nan | Amazônia | 1.5 |
| f4f5b0bc-0b49-3ef9-aa40-4a17c91cf60e | -2.92403 | -51.75139 | 2024-10-29 04:38:00 | NOAA-21 | SENADOR JOSÉ PORFÍRIO | PARÁ | Brasil | 1507805 | 15 | 33 | nan | nan | nan | Amazônia | 2.6 |
| 21726327-b8c2-3ae1-982a-d3e07c3761f1 | -2.92336 | -51.7555 | 2024-10-29 04:38:00 | NOAA-21 | SENADOR JOSÉ PORFÍRIO | PARÁ | Brasil | 1507805 | 15 | 33 | nan | nan | nan | Amazônia | 2.7 |
| d99111e1-2dd8-300f-a722-4d2ac9bc8cd2 | -2.91976 | -51.75492 | 2024-10-29 04:38:00 | NOAA-21 | SENADOR JOSÉ PORFÍRIO | PARÁ | Brasil | 1507805 | 15 | 33 | nan | nan | nan | Amazônia | 1.6 |
| 8eee8f3b-6be5-35ff-b3f0-2841dfd2a420 | -2.91836 | -51.70503 | 2024-10-29 04:38:00 | NOAA-21 | SENADOR JOSÉ PORFÍRIO | PARÁ | Brasil | 1507805 | 15 | 33 | nan | nan | nan | Amazônia | 2.0 |
| d415e0c6-df7e-3f7e-8705-f1ddb9e73c25 | -2.91703 | -51.70371 | 2024-10-29 04:38:00 | NOAA-21 | SENADOR JOSÉ PORFÍRIO | PARÁ | Brasil | 1507805 | 15 | 33 | nan | nan | nan | Amazônia | 1.9 |
| 9bae10be-89cb-323c-941d-514f0d64eba0 | -2.91549 | -51.7585 | 2024-10-29 04:38:00 | NOAA-21 | SENADOR JOSÉ PORFÍRIO | PARÁ | Brasil | 1507805 | 15 | 33 | nan | nan | nan | Amazônia | 1.6 |
| 1e4b2e32-26f7-3d98-a91d-d5a7f24fa044 | -2.91481 | -51.76265 | 2024-10-29 04:38:00 | NOAA-21 | SENADOR JOSÉ PORFÍRIO | PARÁ | Brasil | 1507805 | 15 | 33 | nan | nan | nan | Amazônia | 5.3 |
| d9f19181-2e8e-3001-baa4-fe9d277b351f | -2.91413 | -51.76684 | 2024-10-29 04:38:00 | NOAA-21 | SENADOR JOSÉ PORFÍRIO | PARÁ | Brasil | 1507805 | 15 | 33 | nan | nan | nan | Amazônia | 5.3 |
| 76cadefd-0e7c-3cc9-bca9-2651601e639e | -2.91352 | -51.75937 | 2024-10-29 04:38:00 | NOAA-21 | SENADOR JOSÉ PORFÍRIO | PARÁ | Brasil | 1507805 | 15 | 33 | nan | nan | nan | Amazônia | 2.0 |
| fff2ddb3-1b0f-3cf6-8cf5-679835f6988b | -2.91287 | -51.76354 | 2024-10-29 04:38:00 | NOAA-21 | SENADOR JOSÉ PORFÍRIO | PARÁ | Brasil | 1507805 | 15 | 33 | nan | nan | nan | Amazônia | 14.9 |
| 5a2b6188-a6d8-36d9-9fb1-33b8fee0a54d | -2.91189 | -51.75796 | 2024-10-29 04:38:00 | NOAA-21 | SENADOR JOSÉ PORFÍRIO | PARÁ | Brasil | 1507805 | 15 | 33 | nan | nan | nan | Amazônia | 2.3 |
| 0913a41e-38e5-3d9e-ba7d-c5b43d295ffd | -2.9112 | -51.76214 | 2024-10-29 04:38:00 | NOAA-21 | SENADOR JOSÉ PORFÍRIO | PARÁ | Brasil | 1507805 | 15 | 33 | nan | nan | nan | Amazônia | 3.5 |
| 9b2196ce-133d-3e40-bcb7-7c2c135bcd7e | -2.91053 | -51.7663 | 2024-10-29 04:38:00 | NOAA-21 | SENADOR JOSÉ PORFÍRIO | PARÁ | Brasil | 1507805 | 15 | 33 | nan | nan | nan | Amazônia | 3.5 |
| 3a07fb0d-4407-392e-9d60-5ded8bce424e | -2.90991 | -51.75882 | 2024-10-29 04:38:00 | NOAA-21 | SENADOR JOSÉ PORFÍRIO | PARÁ | Brasil | 1507805 | 15 | 33 | nan | nan | nan | Amazônia | 2.0 |
| 133028b3-e40a-3a56-a7b2-e938d87b7f99 | -2.88181 | -51.65718 | 2024-10-29 04:38:00 | NOAA-21 | ANAPU | PARÁ | Brasil | 1500859 | 15 | 33 | nan | nan | nan | Amazônia | 2.5 |
| dcdb3d83-3642-354d-8d58-f58b2ef9b973 | -2.8178 | -51.60638 | 2024-10-29 04:38:00 | NOAA-21 | ANAPU | PARÁ | Brasil | 1500859 | 15 | 33 | nan | nan | nan | Amazônia | 0.9 |
| 6915ec6c-2a23-3582-be05-011c66681cda | -2.81487 | -51.60174 | 2024-10-29 04:38:00 | NOAA-21 | ANAPU | PARÁ | Brasil | 1500859 | 15 | 33 | nan | nan | nan | Amazônia | 1.3 |
| dbca1b11-cd4f-37c9-8390-73196572cfc7 | -2.81193 | -51.59711 | 2024-10-29 04:38:00 | NOAA-21 | ANAPU | PARÁ | Brasil | 1500859 | 15 | 33 | nan | nan | nan | Amazônia | 1.3 |
| a12f4758-a9db-3224-8c87-fb9632c1cbba | -2.74015 | -51.72468 | 2024-10-29 04:38:00 | NOAA-21 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 1.6 |
| b48b61b1-a390-350a-9a4c-9442c2132e7a | -2.73655 | -51.7241 | 2024-10-29 04:38:00 | NOAA-21 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 2.6 |
| f2c566d0-59db-3be4-bb08-349e61741ec3 | -2.65243 | -51.75422 | 2024-10-29 04:38:00 | NOAA-21 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 3.7 |
| 1fe43a9c-fd9c-35a5-8a62-b3f4518fef50 | -2.65014 | -51.74533 | 2024-10-29 04:38:00 | NOAA-21 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 1.4 |
| e1d6fc65-5d9c-335d-8837-ffdf9d38160a | -2.64948 | -51.74949 | 2024-10-29 04:38:00 | NOAA-21 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 3.7 |
| d7f184b9-eb06-312d-a25e-b9deab3d9503 | -2.64882 | -51.75365 | 2024-10-29 04:38:00 | NOAA-21 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 3.7 |
| 20cc88a0-5380-3215-94a5-5f5dff67072a | -2.64786 | -51.73645 | 2024-10-29 04:38:00 | NOAA-21 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 1.4 |
| 4a285301-e9b5-30c0-aae8-a7550ee5fd49 | -2.6472 | -51.7406 | 2024-10-29 04:38:00 | NOAA-21 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 2.2 |
| 2a8d9918-cde6-310c-b7b8-b01423bb102a | -2.64653 | -51.74477 | 2024-10-29 04:38:00 | NOAA-21 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 2.2 |
| b2176300-0b5c-3bf1-8768-0b24d6514407 | -2.64587 | -51.74893 | 2024-10-29 04:38:00 | NOAA-21 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 8.6 |
| 00068c4c-806c-364a-beb3-c62ff3bbacb9 | -2.64521 | -51.75309 | 2024-10-29 04:38:00 | NOAA-21 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 8.6 |
| ac2d8499-73dc-3546-b8ab-5bbc5439151a | -2.64491 | -51.73173 | 2024-10-29 04:38:00 | NOAA-21 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 1.4 |
| 004d7e5d-9b78-3504-b805-42a039bda7e7 | -2.64425 | -51.73589 | 2024-10-29 04:38:00 | NOAA-21 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 1.4 |
| aa0feb3a-d261-30e1-9f65-57e511c14b20 | -2.64359 | -51.74005 | 2024-10-29 04:38:00 | NOAA-21 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 2.2 |
| 1e03a254-8ed2-3240-b132-d8ad00f5e7a7 | -2.64292 | -51.74421 | 2024-10-29 04:38:00 | NOAA-21 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 2.2 |
| 6222dc57-6db4-3298-9d55-aab7e5d04659 | -2.64226 | -51.74836 | 2024-10-29 04:38:00 | NOAA-21 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 8.6 |
| 9b75c725-d968-396d-a108-4d7535beb6be | -2.6416 | -51.75252 | 2024-10-29 04:38:00 | NOAA-21 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 8.6 |
| 14e43b87-3a01-3cf1-8077-9e4f5bce7b52 | -2.64131 | -51.73117 | 2024-10-29 04:38:00 | NOAA-21 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 2.0 |
| 2038623b-47da-30e1-8605-5d8b4e4b75f6 | -2.64064 | -51.73532 | 2024-10-29 04:38:00 | NOAA-21 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 2.0 |
| 0351d45e-9c85-3873-8893-7fcabee07d8d | -2.63931 | -51.74364 | 2024-10-29 04:38:00 | NOAA-21 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 4.2 |
| e15445d6-9c30-3636-a3eb-8c230584e800 | -2.63836 | -51.72646 | 2024-10-29 04:38:00 | NOAA-21 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 2.1 |
| 94d1ab25-a0e6-33f8-958a-74823d31c6e8 | -2.6377 | -51.73061 | 2024-10-29 04:38:00 | NOAA-21 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 2.0 |
| f21b5184-84fc-3404-88cf-5c9f3c6368b1 | -2.60077 | -51.77608 | 2024-10-29 04:38:00 | NOAA-21 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 1.7 |
| c9aad132-6b60-3bda-9343-98c6527fb205 | -2.60009 | -51.78026 | 2024-10-29 04:38:00 | NOAA-21 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 1.7 |
| c3b80bdd-7d72-369f-864b-f9d9d4cef63c | -2.87917 | -51.31065 | 2024-10-29 04:38:00 | NOAA-21 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 3.3 |
| c800d5dd-97bb-339b-a1bb-aba96ab34cdb | -2.87565 | -51.31011 | 2024-10-29 04:38:00 | NOAA-21 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 2.2 |
| 865f64aa-7696-3012-b7f4-00265ed7d127 | -2.87513 | -51.31072 | 2024-10-29 04:38:00 | NOAA-21 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 2.7 |
| 5f93c0b1-e49f-3145-8e78-c201a66506cd | -2.87501 | -51.31406 | 2024-10-29 04:38:00 | NOAA-21 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 2.2 |
| 4520991b-355e-32f4-b1d2-33d13c452ee6 | -2.87451 | -51.31468 | 2024-10-29 04:38:00 | NOAA-21 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 2.7 |
| 95af0486-3c01-34d2-bfea-43a4cfc3b778 | -2.87212 | -51.30956 | 2024-10-29 04:38:00 | NOAA-21 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 2.2 |
| f83c4070-a37f-37ef-98f6-648415200f2a | -2.87161 | -51.31017 | 2024-10-29 04:38:00 | NOAA-21 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 2.7 |


[Clique aqui para ver as próximas entradas](README50.md)
