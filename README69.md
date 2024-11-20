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

## Dados Diários - Página 69

| ID | Latitude | Longitude | Data/Hora GMT | Satélite | Município | Estado | País | Município ID | Estado ID | País ID | Dias sem Chuva | Precipitação | Risco de Fogo | Bioma | FRP |
|----|----------|-----------|---------------|----------|-----------|--------|------|--------------|-----------|---------|----------------|--------------|----------------|-------|-----|
| 8085fd44-0400-3191-a47b-3061977b0995 | -1.85593 | -54.28042 | 2024-11-20 05:14:00 | NOAA-20 | MONTE ALEGRE | PARÁ | Brasil | 1504802 | 15 | 33 | nan | nan | nan | Amazônia | 36.0 |
| f4254b63-5cef-3bbd-9a6e-9f007602a087 | -0.93652 | -51.7212 | 2024-11-20 05:14:00 | NOAA-20 | VITÓRIA DO JARI | AMAPÁ | Brasil | 1600808 | 16 | 33 | nan | nan | nan | Amazônia | 2.5 |
| ef47df48-a434-3397-b75c-eab99038f142 | -4.24607 | -53.66551 | 2024-11-20 05:14:00 | NOAA-20 | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 5.1 |
| 541d866c-6cb4-3006-9e57-3415baaf3e49 | -3.11706 | -53.70566 | 2024-11-20 05:14:00 | NOAA-20 | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | 2.5 |
| 96746e6a-3e6d-33d9-a5d3-9cf909b6b0fb | -1.44735 | -47.11565 | 2024-11-20 05:14:00 | NOAA-20 | OURÉM | PARÁ | Brasil | 1505403 | 15 | 33 | nan | nan | nan | Amazônia | 1.1 |
| 05563297-6450-35b6-97eb-5d777e530a22 | -1.53846 | -54.90181 | 2024-11-20 05:14:00 | NOAA-20 | ALENQUER | PARÁ | Brasil | 1500404 | 15 | 33 | nan | nan | nan | Amazônia | 2.8 |
| 02987b84-0f19-3ab7-b591-ba436da9254a | -1.23051 | -51.74539 | 2024-11-20 05:14:00 | NOAA-20 | GURUPÁ | PARÁ | Brasil | 1503101 | 15 | 33 | nan | nan | nan | Amazônia | 1.4 |
| 9750d6c5-1a1c-3aff-bd35-e7025157b990 | -2.21549 | -46.48616 | 2024-11-20 05:14:00 | NOAA-20 | CACHOEIRA DO PIRIÁ | PARÁ | Brasil | 1501956 | 15 | 33 | nan | nan | nan | Amazônia | 3.4 |
| 35df9d7a-6fd2-3e9f-ad32-ddfcefcfcdc9 | -3.0567 | -54.40243 | 2024-11-20 05:14:00 | NOAA-20 | MOJUÍ DOS CAMPOS | PARÁ | Brasil | 1504752 | 15 | 33 | nan | nan | nan | Amazônia | 1.1 |
| ca8588cb-2c8d-3e78-b39a-de143d94cba1 | -2.92205 | -53.06955 | 2024-11-20 05:14:00 | NOAA-20 | MEDICILÂNDIA | PARÁ | Brasil | 1504455 | 15 | 33 | nan | nan | nan | Amazônia | 15.2 |
| eb23fee6-879e-31e9-8d83-ab2b785e0206 | -2.99622 | -49.1896 | 2024-11-20 05:14:00 | NOAA-20 | MOJU | PARÁ | Brasil | 1504703 | 15 | 33 | nan | nan | nan | Amazônia | 2.1 |
| 1f3a429c-0d1c-373f-a566-c0baa5128ba9 | -2.9974 | -45.44545 | 2024-11-20 05:14:00 | NOAA-20 | PEDRO DO ROSÁRIO | MARANHÃO | Brasil | 2108256 | 21 | 33 | nan | nan | nan | Amazônia | 2.5 |
| 6a4b18dd-ef58-3646-aac6-ea20ea056012 | -4.25004 | -53.66612 | 2024-11-20 05:14:00 | NOAA-20 | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 5.1 |
| 6c6e5121-9c3e-318c-8f68-4096b14554f1 | -2.74344 | -54.05099 | 2024-11-20 05:14:00 | NOAA-20 | PRAINHA | PARÁ | Brasil | 1506005 | 15 | 33 | nan | nan | nan | Amazônia | 2.2 |
| 28811bb2-b1d0-3edd-b969-049419bc97d1 | -4.38265 | -47.75941 | 2024-11-20 05:14:00 | NOAA-20 | DOM ELISEU | PARÁ | Brasil | 1502939 | 15 | 33 | nan | nan | nan | Amazônia | 0.6 |
| 45ceaa9b-e88c-313d-8704-2d502641d20a | -2.22173 | -46.48711 | 2024-11-20 05:14:00 | NOAA-20 | CACHOEIRA DO PIRIÁ | PARÁ | Brasil | 1501956 | 15 | 33 | nan | nan | nan | Amazônia | 2.0 |
| 9ed6d368-5a06-3420-94eb-d30720288b76 | -3.54548 | -54.57621 | 2024-11-20 05:14:00 | NOAA-20 | PLACAS | PARÁ | Brasil | 1505650 | 15 | 33 | nan | nan | nan | Amazônia | 0.7 |
| 4813b970-c8d0-38da-b200-636f02fe5e9e | -2.81372 | -54.02378 | 2024-11-20 05:14:00 | NOAA-20 | PRAINHA | PARÁ | Brasil | 1506005 | 15 | 33 | nan | nan | nan | Amazônia | 2.4 |
| 595fed2a-2ff4-3d97-bfd5-74a1317e0a2e | -1.09011 | -51.73948 | 2024-11-20 05:14:00 | NOAA-20 | VITÓRIA DO JARI | AMAPÁ | Brasil | 1600808 | 16 | 33 | nan | nan | nan | Amazônia | 1.5 |
| 0061afbd-b823-3871-8b74-619bd3d385d4 | -2.74333 | -51.82771 | 2024-11-20 05:14:00 | NOAA-20 | SENADOR JOSÉ PORFÍRIO | PARÁ | Brasil | 1507805 | 15 | 33 | nan | nan | nan | Amazônia | 27.7 |
| 39b58fb2-1039-310c-b1c5-fce80c7e8e89 | -5.41961 | -47.39337 | 2024-11-20 05:14:00 | NOAA-20 | JOÃO LISBOA | MARANHÃO | Brasil | 2105500 | 21 | 33 | nan | nan | nan | Cerrado | 1.8 |
| 580ff7b5-b849-3447-8d7a-ee22901669d6 | -0.90943 | -51.78308 | 2024-11-20 05:14:00 | NOAA-20 | VITÓRIA DO JARI | AMAPÁ | Brasil | 1600808 | 16 | 33 | nan | nan | nan | Amazônia | 0.9 |
| b2615b3f-2d7f-3e48-82c4-33221909fee8 | -3.82481 | -52.25863 | 2024-11-20 05:14:00 | NOAA-20 | SENADOR JOSÉ PORFÍRIO | PARÁ | Brasil | 1507805 | 15 | 33 | nan | nan | nan | Amazônia | 1.4 |
| 363a6bea-b547-31ed-a62d-e73918a054ca | -2.91044 | -53.06435 | 2024-11-20 05:14:00 | NOAA-20 | MEDICILÂNDIA | PARÁ | Brasil | 1504455 | 15 | 33 | nan | nan | nan | Amazônia | 6.9 |
| c499897c-ff2d-393a-86ce-c0049e3637c2 | -2.38515 | -53.66372 | 2024-11-20 05:14:00 | NOAA-20 | PRAINHA | PARÁ | Brasil | 1506005 | 15 | 33 | nan | nan | nan | Amazônia | 1.4 |
| 2ee33e79-43f3-3d72-b231-c19709f83b76 | -3.81704 | -51.35644 | 2024-11-20 05:14:00 | NOAA-20 | ANAPU | PARÁ | Brasil | 1500859 | 15 | 33 | nan | nan | nan | Amazônia | 6.2 |
| 6d7298be-71ce-3fbd-a997-09120f3404bc | -2.22098 | -46.49199 | 2024-11-20 05:14:00 | NOAA-20 | CACHOEIRA DO PIRIÁ | PARÁ | Brasil | 1501956 | 15 | 33 | nan | nan | nan | Amazônia | 1.7 |
| 455c22c1-9f6a-369b-971b-b9fc2ed648ac | -4.32274 | -49.39194 | 2024-11-20 05:14:00 | NOAA-20 | GOIANÉSIA DO PARÁ | PARÁ | Brasil | 1503093 | 15 | 33 | nan | nan | nan | Amazônia | 2.9 |
| dc93162f-341e-3bb3-bef2-a68d4b54ca82 | -3.53919 | -54.0877 | 2024-11-20 05:14:00 | NOAA-20 | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | 1.4 |
| 35155e06-a15f-3e1a-9a6f-0d45f9d70eef | -1.14098 | -51.68263 | 2024-11-20 05:14:00 | NOAA-20 | GURUPÁ | PARÁ | Brasil | 1503101 | 15 | 33 | nan | nan | nan | Amazônia | 2.6 |
| 832f741f-fea6-3d65-9572-5b0f185e7718 | -3.90999 | -52.40896 | 2024-11-20 05:14:00 | NOAA-20 | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 1.7 |
| 08750346-2f1b-3ed0-b8b3-315e1a77531b | -2.59513 | -54.00677 | 2024-11-20 05:14:00 | NOAA-20 | PRAINHA | PARÁ | Brasil | 1506005 | 15 | 33 | nan | nan | nan | Amazônia | 4.3 |
| 2738b385-7ab2-3085-8f0d-fc3a4909e87c | -2.74641 | -48.57296 | 2024-11-20 05:14:00 | NOAA-20 | TAILÂNDIA | PARÁ | Brasil | 1507953 | 15 | 33 | nan | nan | nan | Amazônia | 1.7 |
| 37af99a8-40a1-3cc3-8f7a-4f88cf485a8c | -3.04471 | -49.47191 | 2024-11-20 05:14:00 | NOAA-20 | MOJU | PARÁ | Brasil | 1504703 | 15 | 33 | nan | nan | nan | Amazônia | 1.5 |
| a007e59d-5d7b-3b61-b33a-cec9d6e9a0f2 | -4.38369 | -47.77723 | 2024-11-20 05:14:00 | NOAA-20 | DOM ELISEU | PARÁ | Brasil | 1502939 | 15 | 33 | nan | nan | nan | Amazônia | 2.4 |
| c82f17e3-c111-3702-b8f7-911c05fa9ac3 | -1.8555 | -47.82684 | 2024-11-20 05:14:00 | NOAA-20 | SÃO DOMINGOS DO CAPIM | PARÁ | Brasil | 1507201 | 15 | 33 | nan | nan | nan | Amazônia | 1.3 |
| 184784c2-277d-3c43-a74c-1d5a728dbf45 | -1.8656 | -46.80045 | 2024-11-20 05:14:00 | NOAA-20 | VISEU | PARÁ | Brasil | 1508308 | 15 | 33 | nan | nan | nan | Amazônia | 2.9 |
| da74803a-bb25-3b32-b18c-4542c902f695 | -3.66435 | -54.65573 | 2024-11-20 05:14:00 | NOAA-20 | PLACAS | PARÁ | Brasil | 1505650 | 15 | 33 | nan | nan | nan | Amazônia | 0.9 |
| 0801221d-7ba8-34e8-9037-ed73dd6f2d3d | -3.20085 | -54.32166 | 2024-11-20 05:14:00 | NOAA-20 | MOJUÍ DOS CAMPOS | PARÁ | Brasil | 1504752 | 15 | 33 | nan | nan | nan | Amazônia | 8.2 |
| cce1a84e-0731-3860-acd9-32494e5873cc | -3.76848 | -53.85159 | 2024-11-20 05:14:00 | NOAA-20 | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | 1.5 |
| 0bbbe5f0-1bde-3ece-bfe2-423371e7d4e3 | -1.48132 | -51.97569 | 2024-11-20 05:14:00 | NOAA-20 | GURUPÁ | PARÁ | Brasil | 1503101 | 15 | 33 | nan | nan | nan | Amazônia | 1.7 |
| e42dfa65-49ef-3a7a-883b-54048810b5dc | -5.37556 | -50.47751 | 2024-11-20 05:14:00 | NOAA-20 | MARABÁ | PARÁ | Brasil | 1504208 | 15 | 33 | nan | nan | nan | Amazônia | 1.0 |
| 658f73b3-3014-37d7-8a36-dbb58da42fd9 | -1.51341 | -55.48418 | 2024-11-20 05:14:00 | NOAA-20 | ÓBIDOS | PARÁ | Brasil | 1505106 | 15 | 33 | nan | nan | nan | Amazônia | 2.0 |
| 4ab30e7b-c677-3646-b327-10fd41a39201 | -2.82104 | -54.02246 | 2024-11-20 05:14:00 | NOAA-20 | PRAINHA | PARÁ | Brasil | 1506005 | 15 | 33 | nan | nan | nan | Amazônia | 1.9 |
| 9c329a21-25a7-3242-85db-1c359290641f | -6.36272 | -55.3689 | 2024-11-20 05:14:00 | NOAA-20 | ITAITUBA | PARÁ | Brasil | 1503606 | 15 | 33 | nan | nan | nan | Amazônia | 1.5 |
| b69f8703-191f-3c8b-9160-04da23436567 | -0.18622 | -51.62098 | 2024-11-20 05:14:00 | NOAA-20 | MAZAGÃO | AMAPÁ | Brasil | 1600402 | 16 | 33 | nan | nan | nan | Amazônia | 1.7 |
| 3e11c2f1-96dd-3538-b45a-34901928300e | -1.20777 | -51.76398 | 2024-11-20 05:14:00 | NOAA-20 | GURUPÁ | PARÁ | Brasil | 1503101 | 15 | 33 | nan | nan | nan | Amazônia | 1.8 |
| cbca79d3-2f82-3b7b-9159-e94e52ee4666 | -1.9876 | -53.14233 | 2024-11-20 05:14:00 | NOAA-20 | PORTO DE MOZ | PARÁ | Brasil | 1505908 | 15 | 33 | nan | nan | nan | Amazônia | 1.6 |
| 9c9d32dc-68a0-3c5d-80b1-02bf2218cde6 | -3.02701 | -51.52786 | 2024-11-20 05:14:00 | NOAA-20 | ANAPU | PARÁ | Brasil | 1500859 | 15 | 33 | nan | nan | nan | Amazônia | 7.8 |
| ffce4546-a4cf-3848-944c-5e970e25824d | -2.85167 | -53.97461 | 2024-11-20 05:14:00 | NOAA-20 | PRAINHA | PARÁ | Brasil | 1506005 | 15 | 33 | nan | nan | nan | Amazônia | 1.4 |
| d31b66fa-fc36-3b2e-a3cd-3b0513116636 | -3.10679 | -53.97913 | 2024-11-20 05:14:00 | NOAA-20 | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | 0.7 |
| 926f1f64-d8a0-3186-8ba6-247d6fe74bd1 | -0.77739 | -51.7481 | 2024-11-20 05:14:00 | NOAA-20 | MAZAGÃO | AMAPÁ | Brasil | 1600402 | 16 | 33 | nan | nan | nan | Amazônia | 0.6 |
| dcafdd86-9184-31a8-a659-692fa6573ceb | -1.11069 | -52.34898 | 2024-11-20 05:14:00 | NOAA-20 | ALMEIRIM | PARÁ | Brasil | 1500503 | 15 | 33 | nan | nan | nan | Amazônia | 2.0 |
| e94014f5-51db-3d37-96a2-5e9876903e23 | -3.50571 | -51.0196 | 2024-11-20 05:14:00 | NOAA-20 | PACAJÁ | PARÁ | Brasil | 1505486 | 15 | 33 | nan | nan | nan | Amazônia | 1.6 |
| db0c7322-d9fd-3792-985d-7360ca7cd14c | -2.85096 | -53.9793 | 2024-11-20 05:14:00 | NOAA-20 | PRAINHA | PARÁ | Brasil | 1506005 | 15 | 33 | nan | nan | nan | Amazônia | 1.4 |
| abc3eb7f-b15c-3478-8aae-77e43adf260c | -3.37433 | -44.428 | 2024-11-20 05:14:00 | NOAA-20 | ITAPECURU MIRIM | MARANHÃO | Brasil | 2105401 | 21 | 33 | nan | nan | nan | Cerrado | 4.8 |
| 7ba1e4ca-0c47-3022-9011-e236f88dfe1a | -3.06919 | -53.28135 | 2024-11-20 05:14:00 | NOAA-20 | MEDICILÂNDIA | PARÁ | Brasil | 1504455 | 15 | 33 | nan | nan | nan | Amazônia | 0.7 |
| be07c75a-489c-3918-87b7-d3ec4d85199e | -1.46058 | -52.69244 | 2024-11-20 05:14:00 | NOAA-20 | ALMEIRIM | PARÁ | Brasil | 1500503 | 15 | 33 | nan | nan | nan | Amazônia | 2.5 |
| 723e8376-ed54-36e3-a7d2-5625b2768b21 | -1.28711 | -52.47018 | 2024-11-20 05:14:00 | NOAA-20 | ALMEIRIM | PARÁ | Brasil | 1500503 | 15 | 33 | nan | nan | nan | Amazônia | 2.5 |
| 1130e5e1-dc4b-35cc-b007-bb7f1fe96986 | -2.13193 | -48.53063 | 2024-11-20 05:14:00 | NOAA-20 | ACARÁ | PARÁ | Brasil | 1500206 | 15 | 33 | nan | nan | nan | Amazônia | 1.8 |
| aeafac4f-507e-393d-8d9d-bd71a27e6e16 | -3.76794 | -51.6842 | 2024-11-20 05:14:00 | NOAA-20 | SENADOR JOSÉ PORFÍRIO | PARÁ | Brasil | 1507805 | 15 | 33 | nan | nan | nan | Amazônia | 2.8 |
| 3bea3a1e-338a-3c36-8daa-713cfe93e306 | -1.6469 | -52.67221 | 2024-11-20 05:14:00 | NOAA-20 | PORTO DE MOZ | PARÁ | Brasil | 1505908 | 15 | 33 | nan | nan | nan | Amazônia | 3.7 |
| 1d88f6de-f378-3f26-8a50-4370d8670bd9 | -2.90345 | -53.05589 | 2024-11-20 05:14:00 | NOAA-20 | MEDICILÂNDIA | PARÁ | Brasil | 1504455 | 15 | 33 | nan | nan | nan | Amazônia | 2.9 |
| f5821502-8112-3d90-a457-f32e03ad452d | -2.92095 | -53.0767 | 2024-11-20 05:14:00 | NOAA-20 | MEDICILÂNDIA | PARÁ | Brasil | 1504455 | 15 | 33 | nan | nan | nan | Amazônia | 17.7 |
| 1033392e-18aa-3351-9c29-ba1b469783e6 | -2.53316 | -54.00872 | 2024-11-20 05:14:00 | NOAA-20 | PRAINHA | PARÁ | Brasil | 1506005 | 15 | 33 | nan | nan | nan | Amazônia | 3.0 |
| 5ab1f990-9665-38ad-82f1-13ec02e35676 | -0.91774 | -52.54056 | 2024-11-20 05:14:00 | NOAA-20 | ALMEIRIM | PARÁ | Brasil | 1500503 | 15 | 33 | nan | nan | nan | Amazônia | 0.9 |
| c7aff8f9-4a66-3a0a-86fb-34e7abe025e0 | -2.0605 | -53.42743 | 2024-11-20 05:14:00 | NOAA-20 | PRAINHA | PARÁ | Brasil | 1506005 | 15 | 33 | nan | nan | nan | Amazônia | 2.5 |
| fb051935-8ced-3f7d-ab30-29263c901dd7 | -1.29718 | -52.24232 | 2024-11-20 05:14:00 | NOAA-20 | ALMEIRIM | PARÁ | Brasil | 1500503 | 15 | 33 | nan | nan | nan | Amazônia | 0.8 |
| ccad0454-bd81-3e9f-91d6-be609a5278c6 | -2.59935 | -51.79683 | 2024-11-20 05:14:00 | NOAA-20 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 2.0 |
| 67c84845-017f-3729-ba46-79a5875cdfda | -2.92611 | -53.07007 | 2024-11-20 05:14:00 | NOAA-20 | MEDICILÂNDIA | PARÁ | Brasil | 1504455 | 15 | 33 | nan | nan | nan | Amazônia | 15.2 |
| 7f5da169-d8f9-365f-8a01-e6dd93f8e4d3 | -2.13893 | -48.56563 | 2024-11-20 05:14:00 | NOAA-20 | ACARÁ | PARÁ | Brasil | 1500206 | 15 | 33 | nan | nan | nan | Amazônia | 11.0 |
| d3e846dc-c3ba-3965-aedc-cb05e76f4cfe | -2.77879 | -48.58146 | 2024-11-20 05:14:00 | NOAA-20 | TAILÂNDIA | PARÁ | Brasil | 1507953 | 15 | 33 | nan | nan | nan | Amazônia | 0.7 |
| 06fcb32e-c02e-36cf-afb5-5b1f1f16c132 | -1.19787 | -51.77084 | 2024-11-20 05:14:00 | NOAA-20 | GURUPÁ | PARÁ | Brasil | 1503101 | 15 | 33 | nan | nan | nan | Amazônia | 2.1 |
| 7b1418af-f029-3d2b-977b-88f56717eeed | -3.66806 | -54.65626 | 2024-11-20 05:14:00 | NOAA-20 | PLACAS | PARÁ | Brasil | 1505650 | 15 | 33 | nan | nan | nan | Amazônia | 1.8 |
| a645422a-e78f-3d6d-b2f9-d9decd8417d1 | -2.76237 | -53.21682 | 2024-11-20 05:14:00 | NOAA-20 | MEDICILÂNDIA | PARÁ | Brasil | 1504455 | 15 | 33 | nan | nan | nan | Amazônia | 0.9 |
| aabef7ee-61c7-36d1-86eb-78db81ff4012 | -1.39024 | -55.62502 | 2024-11-20 05:14:00 | NOAA-20 | ÓBIDOS | PARÁ | Brasil | 1505106 | 15 | 33 | nan | nan | nan | Amazônia | 1.3 |
| 9d4b5643-d215-3e55-b9da-c5c80f8c1628 | -0.1856 | -51.62499 | 2024-11-20 05:14:00 | NOAA-20 | MAZAGÃO | AMAPÁ | Brasil | 1600402 | 16 | 33 | nan | nan | nan | Amazônia | 1.7 |
| 0f1ed8e1-89bd-3c6c-8751-15fbf2112d87 | -3.19944 | -54.33069 | 2024-11-20 05:14:00 | NOAA-20 | MOJUÍ DOS CAMPOS | PARÁ | Brasil | 1504752 | 15 | 33 | nan | nan | nan | Amazônia | 5.9 |
| 90f08766-d705-3478-9926-ea3ee4f1aedc | -3.04144 | -49.45847 | 2024-11-20 05:14:00 | NOAA-20 | MOJU | PARÁ | Brasil | 1504703 | 15 | 33 | nan | nan | nan | Amazônia | 2.7 |
| 3312b6ee-298e-3432-a6a3-197a92d6fca2 | -1.60464 | -54.64332 | 2024-11-20 05:14:00 | NOAA-20 | ALENQUER | PARÁ | Brasil | 1500404 | 15 | 33 | nan | nan | nan | Amazônia | 1.4 |
| fb20a0b0-182d-3132-b0bc-a8020ffc42c1 | -3.48467 | -54.70195 | 2024-11-20 05:14:00 | NOAA-20 | PLACAS | PARÁ | Brasil | 1505650 | 15 | 33 | nan | nan | nan | Amazônia | 3.5 |
| 3f18bcef-60d7-3c04-a936-d696ec04bd4f | -2.30176 | -48.49312 | 2024-11-20 05:14:00 | NOAA-20 | ACARÁ | PARÁ | Brasil | 1500206 | 15 | 33 | nan | nan | nan | Amazônia | 4.2 |
| 954ae0e1-93ae-3cc0-a2ca-79bcd72280e8 | -1.21944 | -54.18757 | 2024-11-20 05:14:00 | NOAA-20 | MONTE ALEGRE | PARÁ | Brasil | 1504802 | 15 | 33 | nan | nan | nan | Amazônia | 1.5 |
| e04d37a2-73e7-3069-90d1-c86fbe0cfd44 | -4.06536 | -46.84594 | 2024-11-20 05:14:00 | NOAA-20 | BOM JARDIM | MARANHÃO | Brasil | 2102002 | 21 | 33 | nan | nan | nan | Amazônia | 1.6 |
| abbef459-8533-35b0-a344-830df3f95ead | -3.88249 | -52.24059 | 2024-11-20 05:14:00 | NOAA-20 | SENADOR JOSÉ PORFÍRIO | PARÁ | Brasil | 1507805 | 15 | 33 | nan | nan | nan | Amazônia | 7.9 |
| bf64b12e-babf-328c-b28b-2b2d93d10aa8 | -2.80122 | -51.80161 | 2024-11-20 05:14:00 | NOAA-20 | SENADOR JOSÉ PORFÍRIO | PARÁ | Brasil | 1507805 | 15 | 33 | nan | nan | nan | Amazônia | 1.9 |
| 78137b13-c171-3708-a300-b3e51d58ff2e | -1.33233 | -52.23609 | 2024-11-20 05:14:00 | NOAA-20 | ALMEIRIM | PARÁ | Brasil | 1500503 | 15 | 33 | nan | nan | nan | Amazônia | 1.1 |
| 738f926e-6fef-3688-9ec8-7121a9ed8aac | -3.06972 | -53.27785 | 2024-11-20 05:14:00 | NOAA-20 | MEDICILÂNDIA | PARÁ | Brasil | 1504455 | 15 | 33 | nan | nan | nan | Amazônia | 0.7 |
| d371d2b4-55d0-3e7b-b162-0fbaad5ad499 | -1.78605 | -53.58764 | 2024-11-20 05:14:00 | NOAA-20 | PRAINHA | PARÁ | Brasil | 1506005 | 15 | 33 | nan | nan | nan | Amazônia | 1.4 |
| 0458aa13-392b-3439-bf82-b9045c45f65d | -1.22188 | -51.74408 | 2024-11-20 05:14:00 | NOAA-20 | GURUPÁ | PARÁ | Brasil | 1503101 | 15 | 33 | nan | nan | nan | Amazônia | 2.7 |
| f86d0918-b2fa-3a6c-9de0-6390d9ce8c0c | -3.67279 | -54.27479 | 2024-11-20 05:14:00 | NOAA-20 | PLACAS | PARÁ | Brasil | 1505650 | 15 | 33 | nan | nan | nan | Amazônia | 3.8 |
| 9c858827-e39c-35e0-858e-bfde36a59a9f | -2.93221 | -49.4345 | 2024-11-20 05:14:00 | NOAA-20 | MOJU | PARÁ | Brasil | 1504703 | 15 | 33 | nan | nan | nan | Amazônia | 1.7 |
| 8b4c6104-c8a4-35aa-953f-ef6d48a334a9 | -2.88125 | -53.95993 | 2024-11-20 05:14:00 | NOAA-20 | PRAINHA | PARÁ | Brasil | 1506005 | 15 | 33 | nan | nan | nan | Amazônia | 2.4 |
| 2db004b1-320b-3f13-b9b8-72f8e822bedd | -2.35235 | -48.60872 | 2024-11-20 05:14:00 | NOAA-20 | ACARÁ | PARÁ | Brasil | 1500206 | 15 | 33 | nan | nan | nan | Amazônia | 2.1 |
| 411ce48a-7b01-3721-a0a3-3ef8b65812c3 | -6.23564 | -47.2785 | 2024-11-20 05:14:00 | NOAA-20 | CAMPESTRE DO MARANHÃO | MARANHÃO | Brasil | 2102556 | 21 | 33 | nan | nan | nan | Cerrado | 1.1 |
| 69bbb845-a0b4-3670-a06f-59b7f31b83c0 | -1.78851 | -53.60978 | 2024-11-20 05:14:00 | NOAA-20 | PRAINHA | PARÁ | Brasil | 1506005 | 15 | 33 | nan | nan | nan | Amazônia | 1.7 |
| 5c03b36d-5247-304f-bdba-85a0b600e9d3 | -3.04483 | -54.40513 | 2024-11-20 05:14:00 | NOAA-20 | MOJUÍ DOS CAMPOS | PARÁ | Brasil | 1504752 | 15 | 33 | nan | nan | nan | Amazônia | 1.1 |
| 2e6951ae-3afe-33ce-9c3c-ddd4e672a056 | -2.71401 | -53.174 | 2024-11-20 05:14:00 | NOAA-20 | MEDICILÂNDIA | PARÁ | Brasil | 1504455 | 15 | 33 | nan | nan | nan | Amazônia | 2.1 |
| 7117f306-18a9-3b7b-b572-f2fe23fe6d2c | -3.30932 | -53.36733 | 2024-11-20 05:14:00 | NOAA-20 | MEDICILÂNDIA | PARÁ | Brasil | 1504455 | 15 | 33 | nan | nan | nan | Amazônia | 1.2 |
| 757ac342-fb4e-3664-b330-28919909fa26 | -4.55224 | -48.01102 | 2024-11-20 05:14:00 | NOAA-20 | RONDON DO PARÁ | PARÁ | Brasil | 1506187 | 15 | 33 | nan | nan | nan | Amazônia | 1.1 |


[Clique aqui para ver as próximas entradas](README70.md)
