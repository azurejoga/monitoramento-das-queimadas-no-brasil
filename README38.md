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

## Dados Diários - Página 38

| ID | Latitude | Longitude | Data/Hora GMT | Satélite | Município | Estado | País | Município ID | Estado ID | País ID | Dias sem Chuva | Precipitação | Risco de Fogo | Bioma | FRP |
|----|----------|-----------|---------------|----------|-----------|--------|------|--------------|-----------|---------|----------------|--------------|----------------|-------|-----|
| 86b807b0-cc49-38fd-a402-8ed4af5b4863 | -3.63122 | -53.96308 | 2024-10-24 04:32:00 | NOAA-21 | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | 3.4 |
| 2ab094d3-80ff-39b4-9c02-871e135b6eb7 | -3.63044 | -53.96782 | 2024-10-24 04:32:00 | NOAA-21 | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | 3.4 |
| 4a7e7425-5955-3691-9fe9-ba1ecefdb34b | -3.59151 | -53.78581 | 2024-10-24 04:32:00 | NOAA-21 | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | 2.1 |
| dfca9189-1129-37dd-8de9-023ca8195fdf | -3.58903 | -53.78257 | 2024-10-24 04:32:00 | NOAA-21 | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | 2.0 |
| ab5729fe-99c0-32fd-ab5b-99d2a603312c | -3.58829 | -53.78719 | 2024-10-24 04:32:00 | NOAA-21 | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | 2.0 |
| 6d45a48a-f44b-3779-b3e2-aca6664741e4 | -3.587 | -53.78533 | 2024-10-24 04:32:00 | NOAA-21 | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | 2.1 |
| c8dad934-e81d-3a0b-8ed3-d1970d94d644 | -3.5838 | -53.78659 | 2024-10-24 04:32:00 | NOAA-21 | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | 3.0 |
| 3ab39ba5-58a3-3d11-ae4d-48ad0fb7730c | -3.57931 | -53.78599 | 2024-10-24 04:32:00 | NOAA-21 | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | 3.0 |
| 132b2692-55ff-3e80-bcc3-763e16678925 | -3.55937 | -54.75892 | 2024-10-24 04:32:00 | NOAA-21 | PLACAS | PARÁ | Brasil | 1505650 | 15 | 33 | nan | nan | nan | Amazônia | 1.4 |
| 729fad54-2f47-3f82-aa88-38863d8ab2a9 | -3.54291 | -54.74018 | 2024-10-24 04:32:00 | NOAA-21 | PLACAS | PARÁ | Brasil | 1505650 | 15 | 33 | nan | nan | nan | Amazônia | 1.9 |
| 6ba9f647-373c-3a6e-bf0c-e77de90a1722 | -3.54221 | -54.74313 | 2024-10-24 04:32:00 | NOAA-21 | PLACAS | PARÁ | Brasil | 1505650 | 15 | 33 | nan | nan | nan | Amazônia | 3.2 |
| caf99453-dcb6-34b1-a15d-e617886f6251 | -3.53815 | -54.73933 | 2024-10-24 04:32:00 | NOAA-21 | PLACAS | PARÁ | Brasil | 1505650 | 15 | 33 | nan | nan | nan | Amazônia | 2.3 |
| 3b65de6b-b56f-3cc9-a791-22eabc516e52 | -3.53744 | -54.74226 | 2024-10-24 04:32:00 | NOAA-21 | PLACAS | PARÁ | Brasil | 1505650 | 15 | 33 | nan | nan | nan | Amazônia | 2.8 |
| 4063848e-7b82-33d8-b265-bed8cfb97256 | -3.48899 | -54.46251 | 2024-10-24 04:32:00 | NOAA-21 | PLACAS | PARÁ | Brasil | 1505650 | 15 | 33 | nan | nan | nan | Amazônia | 2.5 |
| ae809d84-244a-35e9-945f-1c42b6556a77 | -3.48394 | -54.68052 | 2024-10-24 04:32:00 | NOAA-21 | PLACAS | PARÁ | Brasil | 1505650 | 15 | 33 | nan | nan | nan | Amazônia | 3.6 |
| 52133a9f-9652-3c25-aed1-a16987cdf7d9 | -3.48005 | -54.67453 | 2024-10-24 04:32:00 | NOAA-21 | PLACAS | PARÁ | Brasil | 1505650 | 15 | 33 | nan | nan | nan | Amazônia | 2.1 |
| e79cc771-6081-3124-8ee4-825ee4e5bb60 | -3.4792 | -54.67964 | 2024-10-24 04:32:00 | NOAA-21 | PLACAS | PARÁ | Brasil | 1505650 | 15 | 33 | nan | nan | nan | Amazônia | 2.1 |
| d0b157d8-9803-3ca3-a358-191a566a3490 | -3.44417 | -54.12679 | 2024-10-24 04:32:00 | NOAA-21 | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | 1.8 |
| dc3b0863-2f05-3ec4-ab58-711aaeb6c16f | -3.42176 | -54.66767 | 2024-10-24 04:32:00 | NOAA-21 | MOJUÍ DOS CAMPOS | PARÁ | Brasil | 1504752 | 15 | 33 | nan | nan | nan | Amazônia | 2.7 |
| 42bf2411-1f93-3824-8599-e0d387590b1c | -3.41868 | -54.27868 | 2024-10-24 04:32:00 | NOAA-21 | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | 1.9 |
| abd429c2-cdbc-33bd-a96e-5d2a75c236dc | -3.41778 | -54.57312 | 2024-10-24 04:32:00 | NOAA-21 | PLACAS | PARÁ | Brasil | 1505650 | 15 | 33 | nan | nan | nan | Amazônia | 1.9 |
| 00741132-3fb0-3e58-85d7-07e5503d2970 | -3.33036 | -54.18788 | 2024-10-24 04:32:00 | NOAA-21 | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | 3.7 |
| 3f917c07-99c3-34c4-bca0-9ab835882d17 | -3.26228 | -53.7803 | 2024-10-24 04:32:00 | NOAA-21 | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | 1.5 |
| 1e8a554a-ab6c-339a-841e-8efb75147134 | -3.24843 | -53.93882 | 2024-10-24 04:32:00 | NOAA-21 | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | 1.8 |
| cc5f32af-354a-325b-b993-25c6b1e46e2d | -3.10911 | -53.72949 | 2024-10-24 04:32:00 | NOAA-21 | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | 2.0 |
| 7f8379e5-b7e7-31d4-9f0e-1826a1ffd78f | -3.10087 | -53.72357 | 2024-10-24 04:32:00 | NOAA-21 | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | 6.9 |
| d220c0a2-9158-319c-86c6-21889807e5cb | -3.10014 | -53.72805 | 2024-10-24 04:32:00 | NOAA-21 | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | 4.0 |
| b18af875-a49c-3fae-b1a7-b10bcae56be6 | -3.09639 | -53.72285 | 2024-10-24 04:32:00 | NOAA-21 | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | 3.7 |
| 001a35d3-0566-3c18-ae9f-c541598e597f | -3.07976 | -53.82346 | 2024-10-24 04:32:00 | NOAA-21 | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | 7.3 |
| 7c04e485-57d2-3f98-9ef7-5685b13a28f1 | -3.07899 | -53.82811 | 2024-10-24 04:32:00 | NOAA-21 | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | 5.7 |
| 7cef1a54-b182-3743-9aec-799fe9f46346 | -3.07524 | -53.82277 | 2024-10-24 04:32:00 | NOAA-21 | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | 7.3 |
| 39db2728-c9db-3997-8cb7-61b2fdec849b | -3.07445 | -53.82751 | 2024-10-24 04:32:00 | NOAA-21 | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | 5.7 |
| b45498f4-09e7-3e4b-ae78-66e54319a6b6 | -3.0715 | -53.81734 | 2024-10-24 04:32:00 | NOAA-21 | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | 3.8 |
| aa6d70cc-c702-384c-8bd6-b3f91bdfa123 | -3.07072 | -53.82206 | 2024-10-24 04:32:00 | NOAA-21 | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | 3.8 |
| b4a661d8-7908-361a-aa6a-f6d4de87e427 | -3.06993 | -53.82679 | 2024-10-24 04:32:00 | NOAA-21 | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | 2.6 |
| 8c2a7d9e-3e66-3b5c-b985-f848ea94c050 | -3.06619 | -53.8214 | 2024-10-24 04:32:00 | NOAA-21 | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | 3.8 |
| d1b30293-013f-3ece-a281-ef244827b09e | -3.06542 | -53.82605 | 2024-10-24 04:32:00 | NOAA-21 | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | 2.6 |
| 19684498-a0dd-36fd-9179-4f27acb39c0d | -3.13731 | -54.27511 | 2024-10-24 04:32:00 | NOAA-21 | MOJUÍ DOS CAMPOS | PARÁ | Brasil | 1504752 | 15 | 33 | nan | nan | nan | Amazônia | 3.0 |
| de533c24-fe80-3c2b-9798-d2c9fe1eec4e | -3.13652 | -54.27989 | 2024-10-24 04:32:00 | NOAA-21 | MOJUÍ DOS CAMPOS | PARÁ | Brasil | 1504752 | 15 | 33 | nan | nan | nan | Amazônia | 3.7 |
| 7bb0067f-553d-3d70-978d-75d77dbbbe1b | -3.13267 | -54.2743 | 2024-10-24 04:32:00 | NOAA-21 | MOJUÍ DOS CAMPOS | PARÁ | Brasil | 1504752 | 15 | 33 | nan | nan | nan | Amazônia | 2.0 |
| 16ade72c-cf7f-336c-a405-17f316c6c4f7 | -3.11158 | -54.17162 | 2024-10-24 04:32:00 | NOAA-21 | SANTARÉM | PARÁ | Brasil | 1506807 | 15 | 33 | nan | nan | nan | Amazônia | 5.6 |
| ef538644-3beb-36d6-ba35-fc80f4157a05 | -3.11129 | -54.14888 | 2024-10-24 04:32:00 | NOAA-21 | SANTARÉM | PARÁ | Brasil | 1506807 | 15 | 33 | nan | nan | nan | Amazônia | 6.6 |
| 06aa20be-0afa-39c3-b4a5-6be2f5be0e1a | -3.11053 | -54.1536 | 2024-10-24 04:32:00 | NOAA-21 | SANTARÉM | PARÁ | Brasil | 1506807 | 15 | 33 | nan | nan | nan | Amazônia | 6.6 |
| b47e095a-8396-366d-b2b7-d9e4e6394d36 | -3.11007 | -54.15226 | 2024-10-24 04:32:00 | NOAA-21 | SANTARÉM | PARÁ | Brasil | 1506807 | 15 | 33 | nan | nan | nan | Amazônia | 9.4 |
| bc91568b-c645-3bce-8c48-6cc157284243 | -3.10979 | -54.15826 | 2024-10-24 04:32:00 | NOAA-21 | SANTARÉM | PARÁ | Brasil | 1506807 | 15 | 33 | nan | nan | nan | Amazônia | 5.7 |
| 8cce5a76-0cc2-354f-9f2a-c245fb2ad16e | -3.10929 | -54.15693 | 2024-10-24 04:32:00 | NOAA-21 | SANTARÉM | PARÁ | Brasil | 1506807 | 15 | 33 | nan | nan | nan | Amazônia | 7.0 |
| 4f1d60fd-3ea6-37b3-9237-7a9b9c49ed01 | -3.10905 | -54.16291 | 2024-10-24 04:32:00 | NOAA-21 | SANTARÉM | PARÁ | Brasil | 1506807 | 15 | 33 | nan | nan | nan | Amazônia | 5.7 |
| 9580a22e-d82f-31b4-a0ad-78f3e61e6e10 | -3.10852 | -54.16157 | 2024-10-24 04:32:00 | NOAA-21 | SANTARÉM | PARÁ | Brasil | 1506807 | 15 | 33 | nan | nan | nan | Amazônia | 7.0 |
| b599dc54-aa9d-37c9-96aa-81bd82e31ad0 | -3.10831 | -54.16756 | 2024-10-24 04:32:00 | NOAA-21 | SANTARÉM | PARÁ | Brasil | 1506807 | 15 | 33 | nan | nan | nan | Amazônia | 4.7 |
| 5dcd29c0-ad4c-34ba-84b3-7367791c68fe | -3.10774 | -54.16621 | 2024-10-24 04:32:00 | NOAA-21 | SANTARÉM | PARÁ | Brasil | 1506807 | 15 | 33 | nan | nan | nan | Amazônia | 5.6 |
| d38adc13-b1b9-391a-a158-fc48675df49a | -3.10755 | -54.17228 | 2024-10-24 04:32:00 | NOAA-21 | SANTARÉM | PARÁ | Brasil | 1506807 | 15 | 33 | nan | nan | nan | Amazônia | 4.7 |
| 50a42ef6-0bc4-34fb-89ca-f3765295968a | -3.10696 | -54.17086 | 2024-10-24 04:32:00 | NOAA-21 | SANTARÉM | PARÁ | Brasil | 1506807 | 15 | 33 | nan | nan | nan | Amazônia | 5.6 |
| 2b486663-02ee-3448-9c9f-a9b71cf403c4 | -3.10666 | -54.1482 | 2024-10-24 04:32:00 | NOAA-21 | SANTARÉM | PARÁ | Brasil | 1506807 | 15 | 33 | nan | nan | nan | Amazônia | 6.6 |
| 6757fe13-01ab-34c2-bfde-17ac120c59c7 | -3.10623 | -54.14688 | 2024-10-24 04:32:00 | NOAA-21 | SANTARÉM | PARÁ | Brasil | 1506807 | 15 | 33 | nan | nan | nan | Amazônia | 6.3 |
| 2c363938-25bc-31fe-9979-2b4ba611bbac | -3.1059 | -54.15292 | 2024-10-24 04:32:00 | NOAA-21 | SANTARÉM | PARÁ | Brasil | 1506807 | 15 | 33 | nan | nan | nan | Amazônia | 6.6 |
| 10d1c56e-0760-331b-8f9b-b6bbc1a0c52f | -3.10544 | -54.15159 | 2024-10-24 04:32:00 | NOAA-21 | SANTARÉM | PARÁ | Brasil | 1506807 | 15 | 33 | nan | nan | nan | Amazônia | 6.3 |
| 3adb22bd-81e5-3c02-ab1d-0ca659b59bf6 | -3.10516 | -54.15757 | 2024-10-24 04:32:00 | NOAA-21 | SANTARÉM | PARÁ | Brasil | 1506807 | 15 | 33 | nan | nan | nan | Amazônia | 5.7 |
| 81f82f75-8a30-3d61-a9ee-5a18ed77276f | -3.10466 | -54.15626 | 2024-10-24 04:32:00 | NOAA-21 | SANTARÉM | PARÁ | Brasil | 1506807 | 15 | 33 | nan | nan | nan | Amazônia | 3.6 |
| d9920f67-73be-3948-886c-4c8fd140bfbf | -3.10442 | -54.16219 | 2024-10-24 04:32:00 | NOAA-21 | SANTARÉM | PARÁ | Brasil | 1506807 | 15 | 33 | nan | nan | nan | Amazônia | 5.7 |
| 39d57ad1-bb4e-30e3-91c5-042dc382c5f0 | -3.10389 | -54.16086 | 2024-10-24 04:32:00 | NOAA-21 | SANTARÉM | PARÁ | Brasil | 1506807 | 15 | 33 | nan | nan | nan | Amazônia | 3.6 |
| c1a44063-6ea6-3371-88a3-8e2d34522480 | -3.10368 | -54.16683 | 2024-10-24 04:32:00 | NOAA-21 | SANTARÉM | PARÁ | Brasil | 1506807 | 15 | 33 | nan | nan | nan | Amazônia | 4.7 |
| 0ae3eae4-a008-3256-9b7a-409b1381f1de | -3.10311 | -54.16548 | 2024-10-24 04:32:00 | NOAA-21 | SANTARÉM | PARÁ | Brasil | 1506807 | 15 | 33 | nan | nan | nan | Amazônia | 2.0 |
| e29a105b-4ac5-3990-885f-fd0d2975385e | -3.10293 | -54.17151 | 2024-10-24 04:32:00 | NOAA-21 | SANTARÉM | PARÁ | Brasil | 1506807 | 15 | 33 | nan | nan | nan | Amazônia | 4.7 |
| 64aa62a4-02da-31a2-a6a8-39bf9fb236c1 | -3.10234 | -54.17012 | 2024-10-24 04:32:00 | NOAA-21 | SANTARÉM | PARÁ | Brasil | 1506807 | 15 | 33 | nan | nan | nan | Amazônia | 2.0 |
| 33af0334-be18-31a6-972d-5ca29635ccb6 | -3.10217 | -54.17629 | 2024-10-24 04:32:00 | NOAA-21 | SANTARÉM | PARÁ | Brasil | 1506807 | 15 | 33 | nan | nan | nan | Amazônia | 4.0 |
| 2bf95784-a93c-3420-8ad5-118bf5836fab | -3.10154 | -54.17487 | 2024-10-24 04:32:00 | NOAA-21 | SANTARÉM | PARÁ | Brasil | 1506807 | 15 | 33 | nan | nan | nan | Amazônia | 1.7 |
| 2d9ac81b-4e74-3f70-a9cf-867350c4488c | -3.10128 | -54.15219 | 2024-10-24 04:32:00 | NOAA-21 | SANTARÉM | PARÁ | Brasil | 1506807 | 15 | 33 | nan | nan | nan | Amazônia | 6.4 |
| 09561f40-2769-3e6c-bd3a-2c4127c47fee | -3.10082 | -54.15086 | 2024-10-24 04:32:00 | NOAA-21 | SANTARÉM | PARÁ | Brasil | 1506807 | 15 | 33 | nan | nan | nan | Amazônia | 6.3 |
| bf7413ad-d54e-3b7a-afca-fdbef8d8c25c | -3.10073 | -54.17966 | 2024-10-24 04:32:00 | NOAA-21 | SANTARÉM | PARÁ | Brasil | 1506807 | 15 | 33 | nan | nan | nan | Amazônia | 1.7 |
| c1a6e16f-87cb-31a9-b8b2-04112aa5d55f | -3.10053 | -54.15685 | 2024-10-24 04:32:00 | NOAA-21 | SANTARÉM | PARÁ | Brasil | 1506807 | 15 | 33 | nan | nan | nan | Amazônia | 3.0 |
| e89bffd0-e612-3183-9081-f5ba4e885fc6 | -3.10003 | -54.15555 | 2024-10-24 04:32:00 | NOAA-21 | SANTARÉM | PARÁ | Brasil | 1506807 | 15 | 33 | nan | nan | nan | Amazônia | 3.6 |
| 902d0c26-40d2-3b6b-8d59-e0566b038f17 | -3.0998 | -54.16146 | 2024-10-24 04:32:00 | NOAA-21 | SANTARÉM | PARÁ | Brasil | 1506807 | 15 | 33 | nan | nan | nan | Amazônia | 3.0 |
| 07f37fe9-c761-30b3-85e0-9d804cf59fcc | -3.09926 | -54.16014 | 2024-10-24 04:32:00 | NOAA-21 | SANTARÉM | PARÁ | Brasil | 1506807 | 15 | 33 | nan | nan | nan | Amazônia | 3.6 |
| a40c2280-a6bf-32ce-ab9f-2f61d562580a | -3.09905 | -54.1661 | 2024-10-24 04:32:00 | NOAA-21 | SANTARÉM | PARÁ | Brasil | 1506807 | 15 | 33 | nan | nan | nan | Amazônia | 1.2 |
| 7aea7330-729b-3763-8290-40a1588c53c2 | -3.09849 | -54.16476 | 2024-10-24 04:32:00 | NOAA-21 | SANTARÉM | PARÁ | Brasil | 1506807 | 15 | 33 | nan | nan | nan | Amazônia | 2.0 |
| 8a754013-f792-3042-9ced-7289f72bdd3f | -3.0983 | -54.17076 | 2024-10-24 04:32:00 | NOAA-21 | SANTARÉM | PARÁ | Brasil | 1506807 | 15 | 33 | nan | nan | nan | Amazônia | 1.2 |
| 112e0c7a-62e7-3971-926d-71233e3e9f3e | -3.09771 | -54.16941 | 2024-10-24 04:32:00 | NOAA-21 | SANTARÉM | PARÁ | Brasil | 1506807 | 15 | 33 | nan | nan | nan | Amazônia | 2.0 |
| cf0ea5f3-1874-3a89-b0be-95f41cd22b7d | -3.09754 | -54.17552 | 2024-10-24 04:32:00 | NOAA-21 | SANTARÉM | PARÁ | Brasil | 1506807 | 15 | 33 | nan | nan | nan | Amazônia | 3.1 |
| 329e799d-5a54-34bc-86b3-27d230d078e0 | -3.09691 | -54.17412 | 2024-10-24 04:32:00 | NOAA-21 | SANTARÉM | PARÁ | Brasil | 1506807 | 15 | 33 | nan | nan | nan | Amazônia | 1.7 |
| 17aa70ad-e311-31f7-bc82-3a13103edffe | -3.09666 | -54.15144 | 2024-10-24 04:32:00 | NOAA-21 | SANTARÉM | PARÁ | Brasil | 1506807 | 15 | 33 | nan | nan | nan | Amazônia | 6.4 |
| ee0fdc02-972d-3da0-ba2e-3a46daae7b9a | -3.09621 | -54.15011 | 2024-10-24 04:32:00 | NOAA-21 | SANTARÉM | PARÁ | Brasil | 1506807 | 15 | 33 | nan | nan | nan | Amazônia | 4.5 |
| 814df532-2240-32ac-95c6-c6cb18127558 | -3.09591 | -54.15612 | 2024-10-24 04:32:00 | NOAA-21 | SANTARÉM | PARÁ | Brasil | 1506807 | 15 | 33 | nan | nan | nan | Amazônia | 3.0 |
| acf3c8b6-77d2-3369-995a-f6e06115ffc5 | -3.09541 | -54.15483 | 2024-10-24 04:32:00 | NOAA-21 | SANTARÉM | PARÁ | Brasil | 1506807 | 15 | 33 | nan | nan | nan | Amazônia | 6.7 |
| f75d25e5-4da4-38d4-8948-a064fec6c502 | -3.09442 | -54.16538 | 2024-10-24 04:32:00 | NOAA-21 | SANTARÉM | PARÁ | Brasil | 1506807 | 15 | 33 | nan | nan | nan | Amazônia | 1.2 |
| 028f481e-50b2-3558-9f83-e8f585e9918d | -3.09386 | -54.16406 | 2024-10-24 04:32:00 | NOAA-21 | SANTARÉM | PARÁ | Brasil | 1506807 | 15 | 33 | nan | nan | nan | Amazônia | 3.6 |
| 80d97bdd-e825-342c-94d5-a9632fdd837a | -3.09367 | -54.17005 | 2024-10-24 04:32:00 | NOAA-21 | SANTARÉM | PARÁ | Brasil | 1506807 | 15 | 33 | nan | nan | nan | Amazônia | 1.2 |
| fd7cb8f7-9f70-3069-a460-974db8173c59 | -3.09054 | -54.16004 | 2024-10-24 04:32:00 | NOAA-21 | SANTARÉM | PARÁ | Brasil | 1506807 | 15 | 33 | nan | nan | nan | Amazônia | 1.8 |
| 142ea560-fdb6-37b2-9b60-d2ea973c5eec | -3.07901 | -54.17268 | 2024-10-24 04:32:00 | NOAA-21 | SANTARÉM | PARÁ | Brasil | 1506807 | 15 | 33 | nan | nan | nan | Amazônia | 3.4 |
| c87d811d-cbae-3eae-b39c-12e59b4125de | -3.05186 | -54.8553 | 2024-10-24 04:32:00 | NOAA-21 | BELTERRA | PARÁ | Brasil | 1501451 | 15 | 33 | nan | nan | nan | Amazônia | 0.9 |
| 88673c20-70f0-3c01-b0b1-19d20b1137dd | -3.67855 | -54.55131 | 2024-10-24 04:32:00 | NOAA-21 | PLACAS | PARÁ | Brasil | 1505650 | 15 | 33 | nan | nan | nan | Amazônia | 2.5 |
| 915a532e-1502-3c08-9877-8d08b04f7770 | -3.67629 | -54.55277 | 2024-10-24 04:32:00 | NOAA-21 | PLACAS | PARÁ | Brasil | 1505650 | 15 | 33 | nan | nan | nan | Amazônia | 2.4 |
| a9f19b41-5925-34d2-b84f-46e0e1440a5b | -3.6663 | -54.26431 | 2024-10-24 04:32:00 | NOAA-21 | PLACAS | PARÁ | Brasil | 1505650 | 15 | 33 | nan | nan | nan | Amazônia | 7.1 |
| 497a6fa5-ec66-39c9-ac6c-b0adecee0ff1 | -3.66548 | -54.26928 | 2024-10-24 04:32:00 | NOAA-21 | PLACAS | PARÁ | Brasil | 1505650 | 15 | 33 | nan | nan | nan | Amazônia | 7.1 |
| d18e702b-2186-3b8b-a3e5-ec5b8e9e33c0 | -3.66466 | -54.27418 | 2024-10-24 04:32:00 | NOAA-21 | PLACAS | PARÁ | Brasil | 1505650 | 15 | 33 | nan | nan | nan | Amazônia | 4.5 |
| d0e66540-fc47-3f19-8ec5-4820dce539fd | -3.66087 | -54.26846 | 2024-10-24 04:32:00 | NOAA-21 | PLACAS | PARÁ | Brasil | 1505650 | 15 | 33 | nan | nan | nan | Amazônia | 7.1 |
| 6504ce74-c1ab-3cbf-b6d3-3846e2de94b2 | -3.66005 | -54.27338 | 2024-10-24 04:32:00 | NOAA-21 | PLACAS | PARÁ | Brasil | 1505650 | 15 | 33 | nan | nan | nan | Amazônia | 4.5 |
| 446ff673-64cd-3903-9211-23d813e5a4ae | -3.6474 | -54.79177 | 2024-10-24 04:32:00 | NOAA-21 | PLACAS | PARÁ | Brasil | 1505650 | 15 | 33 | nan | nan | nan | Amazônia | 4.1 |
| 214a8545-f867-3eb7-a89a-11f8fe0886e3 | -3.64693 | -54.7939 | 2024-10-24 04:32:00 | NOAA-21 | PLACAS | PARÁ | Brasil | 1505650 | 15 | 33 | nan | nan | nan | Amazônia | 4.0 |
| 5b3c853a-fdc9-306c-9d58-ccd2dc803c8a | -3.6465 | -54.79708 | 2024-10-24 04:32:00 | NOAA-21 | PLACAS | PARÁ | Brasil | 1505650 | 15 | 33 | nan | nan | nan | Amazônia | 4.1 |
| db7b2103-da52-32ee-91ea-f2d507e16e45 | -3.64605 | -54.79934 | 2024-10-24 04:32:00 | NOAA-21 | PLACAS | PARÁ | Brasil | 1505650 | 15 | 33 | nan | nan | nan | Amazônia | 4.0 |


[Clique aqui para ver as próximas entradas](README39.md)
