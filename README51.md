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

## Dados Diários - Página 51

| ID | Latitude | Longitude | Data/Hora GMT | Satélite | Município | Estado | País | Município ID | Estado ID | País ID | Dias sem Chuva | Precipitação | Risco de Fogo | Bioma | FRP |
|----|----------|-----------|---------------|----------|-----------|--------|------|--------------|-----------|---------|----------------|--------------|----------------|-------|-----|
| e206dae3-b520-3eae-b64b-9b48d32f6d75 | -3.42816 | -49.9754 | 2024-10-21 05:27:00 | NOAA-21 | PACAJÁ | PARÁ | Brasil | 1505486 | 15 | 33 | nan | nan | nan | Amazônia | 1.2 |
| 556c3808-e965-3a90-b8f3-40610db9e2c4 | -3.4127 | -50.6284 | 2024-10-21 05:27:00 | NOAA-21 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 1.6 |
| 5bbf29e2-905e-3b38-bf8b-d85e7fc4cfab | -2.96451 | -50.5212 | 2024-10-21 05:27:00 | NOAA-21 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 2.0 |
| ee655224-3820-333f-9012-30c717cf4fda | -2.96387 | -50.52559 | 2024-10-21 05:27:00 | NOAA-21 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 2.2 |
| 4420e8e2-75f3-33f2-9178-e6bb16bc51de | -2.95856 | -50.52025 | 2024-10-21 05:27:00 | NOAA-21 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 2.6 |
| 7c9b1ee3-67a8-3808-adbe-a90f63db88ac | -2.95792 | -50.52465 | 2024-10-21 05:27:00 | NOAA-21 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 2.1 |
| 8a0da8e3-84b7-3651-8c1c-43032880a565 | -2.78535 | -49.29873 | 2024-10-21 05:27:00 | NOAA-21 | MOJU | PARÁ | Brasil | 1504703 | 15 | 33 | nan | nan | nan | Amazônia | 5.2 |
| 3cc73fb8-9ac0-3588-93f9-4d16bdbbe292 | -2.7845 | -49.29579 | 2024-10-21 05:27:00 | NOAA-21 | MOJU | PARÁ | Brasil | 1504703 | 15 | 33 | nan | nan | nan | Amazônia | 4.7 |
| 1ee5d5d4-1b88-34c6-a2f3-466cb81fbae5 | -2.78369 | -49.30107 | 2024-10-21 05:27:00 | NOAA-21 | MOJU | PARÁ | Brasil | 1504703 | 15 | 33 | nan | nan | nan | Amazônia | 2.9 |
| ace7950b-0666-3204-a9f8-f7a24507e380 | -2.78289 | -49.30633 | 2024-10-21 05:27:00 | NOAA-21 | MOJU | PARÁ | Brasil | 1504703 | 15 | 33 | nan | nan | nan | Amazônia | 2.9 |
| 5569e9bb-88e8-3795-9543-f19b5b98ba14 | -2.77894 | -49.29767 | 2024-10-21 05:27:00 | NOAA-21 | MOJU | PARÁ | Brasil | 1504703 | 15 | 33 | nan | nan | nan | Amazônia | 6.7 |
| 84f3c151-d012-36e9-8e79-eb13f6281263 | -2.77818 | -49.30294 | 2024-10-21 05:27:00 | NOAA-21 | MOJU | PARÁ | Brasil | 1504703 | 15 | 33 | nan | nan | nan | Amazônia | 6.7 |
| 43a9caa3-7616-3ba0-a3cc-014c6e1b6fff | -2.77742 | -49.30824 | 2024-10-21 05:27:00 | NOAA-21 | MOJU | PARÁ | Brasil | 1504703 | 15 | 33 | nan | nan | nan | Amazônia | 7.3 |
| f39414c7-c718-3560-949f-967e79090d4e | -2.77729 | -49.30005 | 2024-10-21 05:27:00 | NOAA-21 | MOJU | PARÁ | Brasil | 1504703 | 15 | 33 | nan | nan | nan | Amazônia | 6.7 |
| 7561eee1-56cc-3517-9c99-0b70b13978ae | -2.77649 | -49.30529 | 2024-10-21 05:27:00 | NOAA-21 | MOJU | PARÁ | Brasil | 1504703 | 15 | 33 | nan | nan | nan | Amazônia | 6.7 |
| 6ea4b6d5-3b30-3eb6-b1d5-03766e405030 | -2.77569 | -49.31059 | 2024-10-21 05:27:00 | NOAA-21 | MOJU | PARÁ | Brasil | 1504703 | 15 | 33 | nan | nan | nan | Amazônia | 4.9 |
| 50889bc1-9a88-345b-a106-fc0ed272f7fb | -2.76348 | -49.35942 | 2024-10-21 05:27:00 | NOAA-21 | MOJU | PARÁ | Brasil | 1504703 | 15 | 33 | nan | nan | nan | Amazônia | 2.2 |
| 04fa5b42-4330-3c10-adec-83def2158c64 | -2.48701 | -49.11227 | 2024-10-21 05:27:00 | NOAA-21 | MOJU | PARÁ | Brasil | 1504703 | 15 | 33 | nan | nan | nan | Amazônia | 14.2 |
| 286d8e85-da92-31af-91e7-4c6881eea1a7 | -2.4865 | -49.11021 | 2024-10-21 05:27:00 | NOAA-21 | MOJU | PARÁ | Brasil | 1504703 | 15 | 33 | nan | nan | nan | Amazônia | 9.9 |
| c5ec01ff-f4c2-3219-97bc-4247257cd08e | -2.48568 | -49.11556 | 2024-10-21 05:27:00 | NOAA-21 | MOJU | PARÁ | Brasil | 1504703 | 15 | 33 | nan | nan | nan | Amazônia | 13.8 |
| 5a2bb919-e474-3603-8d48-65843776465e | -2.48212 | -49.10038 | 2024-10-21 05:27:00 | NOAA-21 | MOJU | PARÁ | Brasil | 1504703 | 15 | 33 | nan | nan | nan | Amazônia | 6.8 |
| b70f3071-a75a-33a5-ac69-4ad55a214961 | -2.48133 | -49.10586 | 2024-10-21 05:27:00 | NOAA-21 | MOJU | PARÁ | Brasil | 1504703 | 15 | 33 | nan | nan | nan | Amazônia | 6.8 |
| 457f162e-7b40-3a0c-9eea-5de13ce81f91 | -2.48086 | -49.10384 | 2024-10-21 05:27:00 | NOAA-21 | MOJU | PARÁ | Brasil | 1504703 | 15 | 33 | nan | nan | nan | Amazônia | 9.9 |
| 5f1d0e9e-0ace-34e9-bf9f-398fc4d2357f | -2.48056 | -49.11117 | 2024-10-21 05:27:00 | NOAA-21 | MOJU | PARÁ | Brasil | 1504703 | 15 | 33 | nan | nan | nan | Amazônia | 14.2 |
| 1b27e900-2181-3b68-bc6c-fd67c34d5179 | -2.48004 | -49.10919 | 2024-10-21 05:27:00 | NOAA-21 | MOJU | PARÁ | Brasil | 1504703 | 15 | 33 | nan | nan | nan | Amazônia | 9.9 |
| e432b0e2-fa3d-3798-ba78-3f4c444fa0e9 | -2.47977 | -49.11657 | 2024-10-21 05:27:00 | NOAA-21 | MOJU | PARÁ | Brasil | 1504703 | 15 | 33 | nan | nan | nan | Amazônia | 14.2 |
| 5cf75122-7965-386f-9171-084629d271ca | -2.47923 | -49.11452 | 2024-10-21 05:27:00 | NOAA-21 | MOJU | PARÁ | Brasil | 1504703 | 15 | 33 | nan | nan | nan | Amazônia | 13.8 |
| 7bcf402f-ef9d-32a4-ab4b-7506af46e089 | -2.47567 | -49.0993 | 2024-10-21 05:27:00 | NOAA-21 | MOJU | PARÁ | Brasil | 1504703 | 15 | 33 | nan | nan | nan | Amazônia | 1.9 |
| 3c30caa1-d23f-3496-98db-f62b13925480 | -2.47524 | -49.09726 | 2024-10-21 05:27:00 | NOAA-21 | MOJU | PARÁ | Brasil | 1504703 | 15 | 33 | nan | nan | nan | Amazônia | 2.6 |
| 69c7257b-3693-38cf-8cff-fc3714c64fe6 | -2.47487 | -49.1048 | 2024-10-21 05:27:00 | NOAA-21 | MOJU | PARÁ | Brasil | 1504703 | 15 | 33 | nan | nan | nan | Amazônia | 1.9 |
| 99041f93-d8c5-32be-aafc-5c491c581069 | -2.47441 | -49.10277 | 2024-10-21 05:27:00 | NOAA-21 | MOJU | PARÁ | Brasil | 1504703 | 15 | 33 | nan | nan | nan | Amazônia | 4.1 |
| c3b7b771-7234-3312-95a1-82189dfb2ec2 | -2.46877 | -49.09631 | 2024-10-21 05:27:00 | NOAA-21 | MOJU | PARÁ | Brasil | 1504703 | 15 | 33 | nan | nan | nan | Amazônia | 2.6 |
| e32eb365-9525-3a7c-abc0-9d63b8c6546d | 2.1085 | -50.65002 | 2024-10-21 05:27:00 | NOAA-21 | AMAPÁ | AMAPÁ | Brasil | 1600105 | 16 | 33 | nan | nan | nan | Amazônia | 1.2 |
| 5a8c74d2-eaf1-328d-86dc-d3bc365120cc | 2.10304 | -50.65095 | 2024-10-21 05:27:00 | NOAA-21 | AMAPÁ | AMAPÁ | Brasil | 1600105 | 16 | 33 | nan | nan | nan | Amazônia | 1.2 |
| ea7e2c9e-93a6-3a32-a941-8d7151a7c897 | 1.83321 | -50.49059 | 2024-10-21 05:27:00 | NOAA-21 | AMAPÁ | AMAPÁ | Brasil | 1600105 | 16 | 33 | nan | nan | nan | Amazônia | 2.2 |
| 58a7f008-1653-3742-8f36-99922ff54e06 | 1.82887 | -50.49884 | 2024-10-21 05:27:00 | NOAA-21 | AMAPÁ | AMAPÁ | Brasil | 1600105 | 16 | 33 | nan | nan | nan | Amazônia | 4.4 |
| 9f677103-b352-38f8-a6e8-df4c472ef472 | 1.82826 | -50.49516 | 2024-10-21 05:27:00 | NOAA-21 | AMAPÁ | AMAPÁ | Brasil | 1600105 | 16 | 33 | nan | nan | nan | Amazônia | 4.4 |
| d2af957e-7ad3-3785-b17d-e04389ad4c76 | -2.23157 | -50.45819 | 2024-10-21 05:27:00 | NOAA-21 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 3.7 |
| a97cf961-a304-3517-b2e4-28dc7026fdb7 | -2.22632 | -50.45286 | 2024-10-21 05:27:00 | NOAA-21 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 3.7 |
| e2d8ff51-1551-369b-b3f5-7008b74c0ec9 | -2.22566 | -50.45724 | 2024-10-21 05:27:00 | NOAA-21 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 3.7 |
| 420e513c-1493-3733-8787-8b6286e20d90 | -2.22501 | -50.46155 | 2024-10-21 05:27:00 | NOAA-21 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 5.9 |
| cc3494cc-802e-3096-9fed-65d2f5dcf909 | -2.21976 | -50.45623 | 2024-10-21 05:27:00 | NOAA-21 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 6.2 |
| dd917f66-c1fc-333d-94c1-bc9e3ea1277f | -2.21911 | -50.46054 | 2024-10-21 05:27:00 | NOAA-21 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 6.3 |
| 54212da9-fef0-33be-83ae-6bbf8f2513a4 | -2.20665 | -50.46295 | 2024-10-21 05:27:00 | NOAA-21 | BAGRE | PARÁ | Brasil | 1501105 | 15 | 33 | nan | nan | nan | Amazônia | 2.3 |
| 7e384043-42e2-3149-bd29-eb73707a847e | -1.67158 | -50.46505 | 2024-10-21 05:27:00 | NOAA-21 | BREVES | PARÁ | Brasil | 1501808 | 15 | 33 | nan | nan | nan | Amazônia | 0.9 |
| f2b2d5d4-b504-3e03-bda2-b31f9747a51f | -1.67094 | -50.46928 | 2024-10-21 05:27:00 | NOAA-21 | BREVES | PARÁ | Brasil | 1501808 | 15 | 33 | nan | nan | nan | Amazônia | 0.9 |
| cd8b7442-cd21-328e-a53e-86ef42b08cc1 | -3.50778 | -51.35045 | 2024-10-21 05:27:00 | NOAA-21 | ANAPU | PARÁ | Brasil | 1500859 | 15 | 33 | nan | nan | nan | Amazônia | 1.6 |
| 3a9c8bba-77e1-35b8-8dac-0562bfecac5e | -3.39864 | -51.24473 | 2024-10-21 05:27:00 | NOAA-21 | ANAPU | PARÁ | Brasil | 1500859 | 15 | 33 | nan | nan | nan | Amazônia | 1.8 |
| a9b78cc2-0c54-358b-9bea-38da1dd3f4d1 | -3.38355 | -51.38679 | 2024-10-21 05:27:00 | NOAA-21 | ANAPU | PARÁ | Brasil | 1500859 | 15 | 33 | nan | nan | nan | Amazônia | 1.4 |
| fa59fb92-b769-3c55-b2e9-e2d376b6f01f | -3.37112 | -51.50986 | 2024-10-21 05:27:00 | NOAA-21 | ANAPU | PARÁ | Brasil | 1500859 | 15 | 33 | nan | nan | nan | Amazônia | 0.9 |
| 89e90f66-cdcc-3f12-bad6-939a9589056b | -3.36548 | -51.50914 | 2024-10-21 05:27:00 | NOAA-21 | ANAPU | PARÁ | Brasil | 1500859 | 15 | 33 | nan | nan | nan | Amazônia | 0.9 |
| d6dfa6ea-b0e6-3aca-9e39-3e3bef475f93 | -3.39232 | -50.80595 | 2024-10-21 05:27:00 | NOAA-21 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 1.3 |
| 455c9b5b-f17b-37d1-8ae4-0be15a69525c | -3.38905 | -50.66494 | 2024-10-21 05:27:00 | NOAA-21 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 2.5 |
| 0e59f4f9-6229-3835-9a97-c941ebdcfc3a | -3.38843 | -50.66914 | 2024-10-21 05:27:00 | NOAA-21 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 3.2 |
| 070eff08-40ec-334b-89eb-c3dcd478aafe | -3.38252 | -50.66808 | 2024-10-21 05:27:00 | NOAA-21 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 3.2 |
| ada785d5-3823-3ec4-b648-62abe0de6d33 | -3.24271 | -50.85044 | 2024-10-21 05:27:00 | NOAA-21 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 2.6 |
| 80b27d6a-5791-375c-bf5b-fde2ad40c98a | -3.23685 | -50.84959 | 2024-10-21 05:27:00 | NOAA-21 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 2.6 |
| 8d562db0-c945-3ad6-8663-78b10df4eebb | -3.21425 | -50.79899 | 2024-10-21 05:27:00 | NOAA-21 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 8.1 |
| 19d1b449-3ae6-38af-8d3e-dfea2b02b3d6 | -3.21362 | -50.80336 | 2024-10-21 05:27:00 | NOAA-21 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 10.1 |
| 6067d77e-2740-3ee5-a3fe-98ca461ba5bf | -3.20838 | -50.79805 | 2024-10-21 05:27:00 | NOAA-21 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 8.1 |
| 297ca5e2-e374-34dc-aceb-11c91f95c2d7 | -3.20775 | -50.80241 | 2024-10-21 05:27:00 | NOAA-21 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 10.1 |
| f25e1b7f-362a-3bb1-a47d-e49a136e101b | -3.20713 | -50.80671 | 2024-10-21 05:27:00 | NOAA-21 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 10.1 |
| 8a83f3b6-7036-3623-9fc7-e25c870d5e6c | -3.20429 | -50.79384 | 2024-10-21 05:27:00 | NOAA-21 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 2.8 |
| 11553c00-01d7-3e51-8f83-563cc37e6573 | -3.20365 | -50.79807 | 2024-10-21 05:27:00 | NOAA-21 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 2.8 |
| 7f1553d9-ffe2-359e-a37a-7aa3854c9471 | -3.20299 | -50.80243 | 2024-10-21 05:27:00 | NOAA-21 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 3.4 |
| 14b32793-1b29-304e-8eb3-e4d6bfe904a0 | -3.20252 | -50.79706 | 2024-10-21 05:27:00 | NOAA-21 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 3.8 |
| 88aa222e-eef9-3805-9e8b-a870b0afd595 | -3.20189 | -50.80143 | 2024-10-21 05:27:00 | NOAA-21 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 2.3 |
| e20724f6-e71a-3b20-8063-989fe1f1b526 | -2.25646 | -51.9339 | 2024-10-21 05:27:00 | NOAA-21 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 1.8 |
| 25629fea-3db9-3d61-ab9d-f261a24cfd92 | -2.2516 | -51.9297 | 2024-10-21 05:27:00 | NOAA-21 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 2.0 |
| 08199ca1-01f9-38ea-b868-473a0de482ea | -2.25108 | -51.9331 | 2024-10-21 05:27:00 | NOAA-21 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 1.8 |
| 700aea1d-5d2e-3168-8668-1201fa46b5d4 | -2.24571 | -51.93229 | 2024-10-21 05:27:00 | NOAA-21 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 0.7 |
| 8bdcc2e7-43b5-308a-a637-f4caf6ff2c57 | -2.23094 | -51.88453 | 2024-10-21 05:27:00 | NOAA-21 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 3.3 |
| f5f1a262-4b64-311a-a737-3434d34d969f | -2.23042 | -51.88793 | 2024-10-21 05:27:00 | NOAA-21 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 1.8 |
| 209722cf-a869-3566-90cf-e2e078afdfc1 | -2.22504 | -51.88707 | 2024-10-21 05:27:00 | NOAA-21 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 1.8 |
| cd3f364c-bf0d-3114-879a-b192c6c43f22 | -3.24791 | -50.93642 | 2024-10-21 05:27:00 | NOAA-21 | PACAJÁ | PARÁ | Brasil | 1505486 | 15 | 33 | nan | nan | nan | Amazônia | 1.6 |
| 6c6d3113-70fc-3a55-a1da-98d5e15cc00d | -3.2473 | -50.94055 | 2024-10-21 05:27:00 | NOAA-21 | PACAJÁ | PARÁ | Brasil | 1505486 | 15 | 33 | nan | nan | nan | Amazônia | 1.6 |
| 9e6f4ccf-01a7-3d64-b854-dcf956b980fe | -3.23658 | -51.14007 | 2024-10-21 05:27:00 | NOAA-21 | PACAJÁ | PARÁ | Brasil | 1505486 | 15 | 33 | nan | nan | nan | Amazônia | 1.3 |
| 0a8db36c-f7fd-311a-be43-6c229c0d0da7 | -3.23602 | -51.14403 | 2024-10-21 05:27:00 | NOAA-21 | PACAJÁ | PARÁ | Brasil | 1505486 | 15 | 33 | nan | nan | nan | Amazônia | 1.3 |
| f3c9fe86-9866-36c6-87be-9db2d2e18bf6 | -3.23546 | -51.13877 | 2024-10-21 05:27:00 | NOAA-21 | PACAJÁ | PARÁ | Brasil | 1505486 | 15 | 33 | nan | nan | nan | Amazônia | 1.7 |
| 89de58cd-31b7-3709-a86b-da594d0df43b | -3.23488 | -51.14267 | 2024-10-21 05:27:00 | NOAA-21 | PACAJÁ | PARÁ | Brasil | 1505486 | 15 | 33 | nan | nan | nan | Amazônia | 2.0 |
| 514f470c-7352-363d-ae4a-0fc0ff2f6b00 | -3.2308 | -51.13941 | 2024-10-21 05:27:00 | NOAA-21 | PACAJÁ | PARÁ | Brasil | 1505486 | 15 | 33 | nan | nan | nan | Amazônia | 1.3 |
| de7ed74f-4df4-3396-93fa-1c41947c62a8 | -3.23025 | -51.14332 | 2024-10-21 05:27:00 | NOAA-21 | PACAJÁ | PARÁ | Brasil | 1505486 | 15 | 33 | nan | nan | nan | Amazônia | 1.3 |
| b31cfaf7-d16a-34fb-819c-cd4250782335 | -3.22969 | -51.13807 | 2024-10-21 05:27:00 | NOAA-21 | PACAJÁ | PARÁ | Brasil | 1505486 | 15 | 33 | nan | nan | nan | Amazônia | 1.7 |
| 7ae3d56d-9618-3437-ab4b-1b494515dcfa | -3.22911 | -51.14199 | 2024-10-21 05:27:00 | NOAA-21 | PACAJÁ | PARÁ | Brasil | 1505486 | 15 | 33 | nan | nan | nan | Amazônia | 2.0 |
| b6c3f6cd-68c9-3e76-8e6a-2ae16918aa43 | -3.22644 | -51.25211 | 2024-10-21 05:27:00 | NOAA-21 | PACAJÁ | PARÁ | Brasil | 1505486 | 15 | 33 | nan | nan | nan | Amazônia | 2.3 |
| bc9d6983-fe2a-3e1b-9c1a-f336ca1c1e88 | -3.22587 | -51.25611 | 2024-10-21 05:27:00 | NOAA-21 | ANAPU | PARÁ | Brasil | 1500859 | 15 | 33 | nan | nan | nan | Amazônia | 2.3 |
| 7e9bbfdc-e079-3a0e-a3a2-1d6f11553b83 | -3.22393 | -51.25452 | 2024-10-21 05:27:00 | NOAA-21 | ANAPU | PARÁ | Brasil | 1500859 | 15 | 33 | nan | nan | nan | Amazônia | 5.9 |
| 34026a03-d804-31d0-8de0-7a4fcb87f9bd | -3.22015 | -51.25536 | 2024-10-21 05:27:00 | NOAA-21 | ANAPU | PARÁ | Brasil | 1500859 | 15 | 33 | nan | nan | nan | Amazônia | 1.2 |
| c1403a11-b095-3b2f-b2e6-7927fdad5cd8 | -3.21808 | -51.35102 | 2024-10-21 05:27:00 | NOAA-21 | ANAPU | PARÁ | Brasil | 1500859 | 15 | 33 | nan | nan | nan | Amazônia | 1.3 |
| 9b6f8010-b754-33a9-8c04-7878c7a7bea3 | -3.12888 | -51.34745 | 2024-10-21 05:27:00 | NOAA-21 | ANAPU | PARÁ | Brasil | 1500859 | 15 | 33 | nan | nan | nan | Amazônia | 0.9 |
| 13663c4d-69e5-323c-ab67-f600f36365d4 | -3.12319 | -51.34675 | 2024-10-21 05:27:00 | NOAA-21 | ANAPU | PARÁ | Brasil | 1500859 | 15 | 33 | nan | nan | nan | Amazônia | 1.2 |
| a7a85666-c23e-3014-a739-4ce335e3e0ba | -3.10198 | -51.27641 | 2024-10-21 05:27:00 | NOAA-21 | ANAPU | PARÁ | Brasil | 1500859 | 15 | 33 | nan | nan | nan | Amazônia | 2.0 |
| 56fcb95a-1154-31de-bd15-32ecc8ac4409 | -3.09629 | -51.27559 | 2024-10-21 05:27:00 | NOAA-21 | ANAPU | PARÁ | Brasil | 1500859 | 15 | 33 | nan | nan | nan | Amazônia | 2.8 |
| ec2160dd-0be9-33cd-bc87-7734a1702ffd | -3.09308 | -51.21908 | 2024-10-21 05:27:00 | NOAA-21 | ANAPU | PARÁ | Brasil | 1500859 | 15 | 33 | nan | nan | nan | Amazônia | 1.4 |
| b5d32590-a3c4-34bf-852e-492d69600fee | -3.09003 | -51.27859 | 2024-10-21 05:27:00 | NOAA-21 | ANAPU | PARÁ | Brasil | 1500859 | 15 | 33 | nan | nan | nan | Amazônia | 2.8 |
| 1f0f16fb-ba0e-33fa-b7d7-04bcd24c7625 | -3.08945 | -51.28249 | 2024-10-21 05:27:00 | NOAA-21 | ANAPU | PARÁ | Brasil | 1500859 | 15 | 33 | nan | nan | nan | Amazônia | 3.5 |
| ce636477-78c8-36a0-82bd-aa7fddb948df | -3.08739 | -51.21808 | 2024-10-21 05:27:00 | NOAA-21 | ANAPU | PARÁ | Brasil | 1500859 | 15 | 33 | nan | nan | nan | Amazônia | 1.4 |
| 1f6d1585-4cf0-33ea-a154-431c1256f24c | -3.08436 | -51.27763 | 2024-10-21 05:27:00 | NOAA-21 | ANAPU | PARÁ | Brasil | 1500859 | 15 | 33 | nan | nan | nan | Amazônia | 3.8 |
| 58395825-15c8-34c8-aefb-09fd8ccc715a | -3.08378 | -51.28153 | 2024-10-21 05:27:00 | NOAA-21 | ANAPU | PARÁ | Brasil | 1500859 | 15 | 33 | nan | nan | nan | Amazônia | 1.8 |
| f827318f-813c-35cf-aaea-36144308462f | -3.08039 | -51.10683 | 2024-10-21 05:27:00 | NOAA-21 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 3.8 |


[Clique aqui para ver as próximas entradas](README52.md)
