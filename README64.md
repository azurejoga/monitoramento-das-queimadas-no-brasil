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

## Dados Diários - Página 64

| ID | Latitude | Longitude | Data/Hora GMT | Satélite | Município | Estado | País | Município ID | Estado ID | País ID | Dias sem Chuva | Precipitação | Risco de Fogo | Bioma | FRP |
|----|----------|-----------|---------------|----------|-----------|--------|------|--------------|-----------|---------|----------------|--------------|----------------|-------|-----|
| e5ae5251-7967-39f2-8904-cfcf32379c2b | -1.18397 | -51.95451 | 2024-11-23 05:33:00 | NPP-375D | ALMEIRIM | PARÁ | Brasil | 1500503 | 15 | 33 | nan | nan | nan | Amazônia | 0.6 |
| 4f5604ce-318f-3d57-b4a9-fe55a678087f | -1.98974 | -53.13911 | 2024-11-23 05:33:00 | NPP-375D | PORTO DE MOZ | PARÁ | Brasil | 1505908 | 15 | 33 | nan | nan | nan | Amazônia | 2.0 |
| a792dad3-4e28-318c-ab74-b2cd66d22c0b | -3.50662 | -53.81033 | 2024-11-23 05:33:00 | NPP-375D | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | 1.0 |
| 2d96752d-06b9-38d6-a77e-4e2381506a66 | -1.783 | -53.61127 | 2024-11-23 05:33:00 | NPP-375D | PRAINHA | PARÁ | Brasil | 1506005 | 15 | 33 | nan | nan | nan | Amazônia | 1.8 |
| 0a0cc3f2-12c3-38ef-9621-62625ec9f104 | -2.62419 | -51.79051 | 2024-11-23 05:33:00 | NPP-375D | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 1.9 |
| 7fd27832-df4f-363b-b509-b78d568a8b0c | -1.64156 | -52.09994 | 2024-11-23 05:33:00 | NPP-375D | PORTO DE MOZ | PARÁ | Brasil | 1505908 | 15 | 33 | nan | nan | nan | Amazônia | 1.1 |
| 79b5fff0-2370-3f9b-aece-f454f3225375 | -3.67391 | -51.73636 | 2024-11-23 05:33:00 | NPP-375D | SENADOR JOSÉ PORFÍRIO | PARÁ | Brasil | 1507805 | 15 | 33 | nan | nan | nan | Amazônia | 1.9 |
| b1570df4-b501-3d60-abb1-06c77e2930e2 | -1.4491 | -53.39211 | 2024-11-23 05:33:00 | NPP-375D | ALMEIRIM | PARÁ | Brasil | 1500503 | 15 | 33 | nan | nan | nan | Amazônia | 3.0 |
| 6a071517-4c2f-3ea5-afd7-96100008976d | -2.5088 | -54.15267 | 2024-11-23 05:33:00 | NPP-375D | PRAINHA | PARÁ | Brasil | 1506005 | 15 | 33 | nan | nan | nan | Amazônia | 0.8 |
| 88821eec-5912-37d9-9869-68684dae04a8 | -2.4596 | -53.70214 | 2024-11-23 05:33:00 | NPP-375D | PRAINHA | PARÁ | Brasil | 1506005 | 15 | 33 | nan | nan | nan | Amazônia | 1.1 |
| 6814baa6-496c-372d-aa88-3ef816f3e4b6 | -1.22923 | -51.74073 | 2024-11-23 05:33:00 | NPP-375D | GURUPÁ | PARÁ | Brasil | 1503101 | 15 | 33 | nan | nan | nan | Amazônia | 3.8 |
| e417a3dd-e35b-38e3-a39a-9dbd75fd5bab | -2.79098 | -54.15628 | 2024-11-23 05:33:00 | NPP-375D | SANTARÉM | PARÁ | Brasil | 1506807 | 15 | 33 | nan | nan | nan | Amazônia | 0.9 |
| 99cb3a0c-2ef1-3d8b-a680-cf0b9ad08cae | -1.20796 | -54.03651 | 2024-11-23 05:33:00 | NPP-375D | MONTE ALEGRE | PARÁ | Brasil | 1504802 | 15 | 33 | nan | nan | nan | Amazônia | 1.5 |
| 4fad8e08-4c55-38a3-a8aa-cb67ef2cffd0 | -5.57171 | -50.95015 | 2024-11-23 05:33:00 | NPP-375D | SÃO FÉLIX DO XINGU | PARÁ | Brasil | 1507300 | 15 | 33 | nan | nan | nan | Amazônia | 5.4 |
| d68cd216-3b5a-3da4-8da9-eb2f215c2f93 | -1.6216 | -52.60891 | 2024-11-23 05:33:00 | NPP-375D | PORTO DE MOZ | PARÁ | Brasil | 1505908 | 15 | 33 | nan | nan | nan | Amazônia | 2.0 |
| fe9cfd67-652e-3b80-8718-9ec224e8b5c1 | -1.65938 | -52.69971 | 2024-11-23 05:33:00 | NPP-375D | PORTO DE MOZ | PARÁ | Brasil | 1505908 | 15 | 33 | nan | nan | nan | Amazônia | 1.4 |
| 5c27988f-5e37-3683-a36c-7a998e263bb5 | -2.45428 | -49.08502 | 2024-11-23 05:33:00 | NPP-375D | MOJU | PARÁ | Brasil | 1504703 | 15 | 33 | nan | nan | nan | Amazônia | 5.2 |
| eddf5c65-cb9c-3808-9b5f-b012bb4ce5ed | -2.76724 | -54.06693 | 2024-11-23 05:33:00 | NPP-375D | PRAINHA | PARÁ | Brasil | 1506005 | 15 | 33 | nan | nan | nan | Amazônia | 0.8 |
| 61694834-4a9d-3f70-b798-a02dcea916d5 | -1.2649 | -51.76336 | 2024-11-23 05:33:00 | NPP-375D | GURUPÁ | PARÁ | Brasil | 1503101 | 15 | 33 | nan | nan | nan | Amazônia | 11.3 |
| 702e42d4-9bc1-318a-95fd-020f82624250 | -1.23518 | -51.74164 | 2024-11-23 05:33:00 | NPP-375D | GURUPÁ | PARÁ | Brasil | 1503101 | 15 | 33 | nan | nan | nan | Amazônia | 3.8 |
| 1b420c40-177d-30b0-971d-849e1bb4dfba | -3.28892 | -53.8558 | 2024-11-23 05:33:00 | NPP-375D | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | 0.8 |
| 7afdc5a0-3d0f-3a2b-912f-12fa1ae6d433 | -3.50843 | -53.81316 | 2024-11-23 05:33:00 | NPP-375D | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | 0.5 |
| 6eb1edea-f37a-32c7-b150-5abeab068c87 | -2.50924 | -54.14964 | 2024-11-23 05:33:00 | NPP-375D | PRAINHA | PARÁ | Brasil | 1506005 | 15 | 33 | nan | nan | nan | Amazônia | 0.8 |
| 480d1816-6986-3be5-8653-6913c976ecf6 | -2.68026 | -52.07404 | 2024-11-23 05:33:00 | NPP-375D | PORTO DE MOZ | PARÁ | Brasil | 1505908 | 15 | 33 | nan | nan | nan | Amazônia | 1.1 |
| 1bc3a78a-34e5-3586-af12-ff4f72268496 | -2.15143 | -50.9175 | 2024-11-23 05:33:00 | NPP-375D | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 3.8 |
| 46f6edd1-64b8-3249-ad50-fb74db3f51c0 | -3.50613 | -53.81359 | 2024-11-23 05:33:00 | NPP-375D | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | 0.9 |
| b4f7c2c6-1a01-3f52-baf0-c77ddb1a18eb | -1.7891 | -53.6421 | 2024-11-23 05:33:00 | NPP-375D | PRAINHA | PARÁ | Brasil | 1506005 | 15 | 33 | nan | nan | nan | Amazônia | 1.1 |
| 1c437ee9-6677-3663-a7f7-8b9f0707351d | -1.63077 | -53.31728 | 2024-11-23 05:33:00 | NPP-375D | ALMEIRIM | PARÁ | Brasil | 1500503 | 15 | 33 | nan | nan | nan | Amazônia | 1.1 |
| e5e959bf-60ee-32da-87be-52a9478a31d2 | -1.83693 | -54.52403 | 2024-11-23 05:33:00 | NPP-375D | ALENQUER | PARÁ | Brasil | 1500404 | 15 | 33 | nan | nan | nan | Amazônia | 2.4 |
| ab5754ff-0171-3ab0-a0d4-3d28c18ca204 | -2.7611 | -54.0724 | 2024-11-23 05:33:00 | NPP-375D | PRAINHA | PARÁ | Brasil | 1506005 | 15 | 33 | nan | nan | nan | Amazônia | 0.9 |
| 0b396b04-0fc3-32b3-be78-08eb8dd5dad2 | -1.18984 | -51.95532 | 2024-11-23 05:33:00 | NPP-375D | ALMEIRIM | PARÁ | Brasil | 1500503 | 15 | 33 | nan | nan | nan | Amazônia | 0.6 |
| 80b54d99-1838-37fa-be6e-880a6c712936 | -3.28019 | -53.82239 | 2024-11-23 05:33:00 | NPP-375D | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | 0.4 |
| 38797cf0-3522-3a42-99e0-9fd13c2aa8f2 | -2.20666 | -48.92023 | 2024-11-23 05:33:00 | NPP-375D | MOJU | PARÁ | Brasil | 1504703 | 15 | 33 | nan | nan | nan | Amazônia | 3.5 |
| 6016c0ef-089a-3c24-ad8e-4a7ca485709c | -1.11438 | -53.39633 | 2024-11-23 05:33:00 | NPP-375D | ALMEIRIM | PARÁ | Brasil | 1500503 | 15 | 33 | nan | nan | nan | Amazônia | 2.1 |
| fc376bc8-ff07-34ea-a4a9-c32fbdcf0bfd | -1.20937 | -51.94556 | 2024-11-23 05:33:00 | NPP-375D | ALMEIRIM | PARÁ | Brasil | 1500503 | 15 | 33 | nan | nan | nan | Amazônia | 1.4 |
| 7ccb92e2-40c7-3d73-bdd1-fe0a12cfd8bd | -1.26218 | -51.76342 | 2024-11-23 05:33:00 | NPP-375D | GURUPÁ | PARÁ | Brasil | 1503101 | 15 | 33 | nan | nan | nan | Amazônia | 14.5 |
| 83d801bc-4435-33ea-978c-f675a5d71998 | -3.50984 | -53.80338 | 2024-11-23 05:33:00 | NPP-375D | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | 0.5 |
| ffdd44ec-50bd-31dc-a2c3-6c91182ac60d | -1.12934 | -53.40538 | 2024-11-23 05:33:00 | NPP-375D | ALMEIRIM | PARÁ | Brasil | 1500503 | 15 | 33 | nan | nan | nan | Amazônia | 1.7 |
| 8b7bda33-1539-35c7-b3c9-35a0c8e8371d | -3.50712 | -53.80704 | 2024-11-23 05:33:00 | NPP-375D | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | 1.0 |
| c825755b-bf33-3d41-8213-df443eb0ae03 | -1.72731 | -52.7299 | 2024-11-23 05:33:00 | NPP-375D | PORTO DE MOZ | PARÁ | Brasil | 1505908 | 15 | 33 | nan | nan | nan | Amazônia | 5.5 |
| 9a66755c-5af8-3aa9-a1be-494d4b22c3ef | -0.92106 | -53.10084 | 2024-11-23 05:33:00 | NPP-375D | ALMEIRIM | PARÁ | Brasil | 1500503 | 15 | 33 | nan | nan | nan | Amazônia | 1.2 |
| aa6bc882-0a57-3ea1-9cc1-ed4eb31267be | -0.95931 | -51.71653 | 2024-11-23 05:33:00 | NPP-375D | VITÓRIA DO JARI | AMAPÁ | Brasil | 1600808 | 16 | 33 | nan | nan | nan | Amazônia | 1.2 |
| ce5093ff-413f-3574-b9f9-d5657efffe0b | -3.23455 | -54.22873 | 2024-11-23 05:33:00 | NPP-375D | SANTARÉM | PARÁ | Brasil | 1506807 | 15 | 33 | nan | nan | nan | Amazônia | 1.4 |
| 5e58fce8-4ccc-312e-b616-ededf2b32137 | -1.10906 | -53.39552 | 2024-11-23 05:33:00 | NPP-375D | ALMEIRIM | PARÁ | Brasil | 1500503 | 15 | 33 | nan | nan | nan | Amazônia | 2.1 |
| c6aa05dc-b047-3072-a017-32078dcf0e44 | -3.2454 | -54.22723 | 2024-11-23 05:33:00 | NPP-375D | SANTARÉM | PARÁ | Brasil | 1506807 | 15 | 33 | nan | nan | nan | Amazônia | 0.6 |
| 474886a1-1a34-32b2-92ec-fcf554b7ec50 | -1.6313 | -53.31384 | 2024-11-23 05:33:00 | NPP-375D | ALMEIRIM | PARÁ | Brasil | 1500503 | 15 | 33 | nan | nan | nan | Amazônia | 1.1 |
| b423a657-2910-3494-97d0-0dda1cb84e0e | -1.11053 | -53.39594 | 2024-11-23 05:33:00 | NPP-375D | ALMEIRIM | PARÁ | Brasil | 1500503 | 15 | 33 | nan | nan | nan | Amazônia | 2.2 |
| c65536bc-4bb7-30fe-8d02-aa3ceba1a9b2 | -3.06371 | -53.28274 | 2024-11-23 05:33:00 | NPP-375D | MEDICILÂNDIA | PARÁ | Brasil | 1504455 | 15 | 33 | nan | nan | nan | Amazônia | 2.7 |
| b3b4a57f-4100-398f-a9d3-8c763be0140b | -1.60872 | -52.57963 | 2024-11-23 05:33:00 | NPP-375D | PORTO DE MOZ | PARÁ | Brasil | 1505908 | 15 | 33 | nan | nan | nan | Amazônia | 4.3 |
| 32f80133-a78f-331e-9be7-15857ec2130f | -3.08389 | -53.2593 | 2024-11-23 05:33:00 | NPP-375D | MEDICILÂNDIA | PARÁ | Brasil | 1504455 | 15 | 33 | nan | nan | nan | Amazônia | 0.9 |
| 15f6a7dd-cd15-331b-8c38-da2532a57356 | -3.28844 | -53.85912 | 2024-11-23 05:33:00 | NPP-375D | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | 0.8 |
| 87b2cbc1-f725-35fb-a552-f427e262e457 | -3.32153 | -53.28602 | 2024-11-23 05:33:00 | NPP-375D | MEDICILÂNDIA | PARÁ | Brasil | 1504455 | 15 | 33 | nan | nan | nan | Amazônia | 1.8 |
| e7ef6d26-4f33-3ad0-a2a5-59e7dabcfb97 | -1.63348 | -52.60685 | 2024-11-23 05:33:00 | NPP-375D | PORTO DE MOZ | PARÁ | Brasil | 1505908 | 15 | 33 | nan | nan | nan | Amazônia | 1.3 |
| caf43c24-8ae6-3ad2-bbc7-d3f1dc7d4277 | -3.1243 | -53.10065 | 2024-11-23 05:33:00 | NPP-375D | MEDICILÂNDIA | PARÁ | Brasil | 1504455 | 15 | 33 | nan | nan | nan | Amazônia | 3.5 |
| 575bafde-2441-3561-919b-9d50ff0fb9aa | -3.2489 | -54.24204 | 2024-11-23 05:33:00 | NPP-375D | SANTARÉM | PARÁ | Brasil | 1506807 | 15 | 33 | nan | nan | nan | Amazônia | 1.0 |
| cf0350b4-7063-3252-9aee-fc4974bfb9a9 | -1.76288 | -52.70314 | 2024-11-23 05:33:00 | NPP-375D | PORTO DE MOZ | PARÁ | Brasil | 1505908 | 15 | 33 | nan | nan | nan | Amazônia | 0.9 |
| 369073ba-f1b0-34cf-b7dc-8cbf8e685187 | -1.2835 | -54.53699 | 2024-11-23 05:33:00 | NPP-375D | MONTE ALEGRE | PARÁ | Brasil | 1504802 | 15 | 33 | nan | nan | nan | Amazônia | 3.4 |
| 6eb4ca39-13a3-3c2f-bb62-ecf4ae5cb79e | -0.95273 | -51.71987 | 2024-11-23 05:33:00 | NPP-375D | VITÓRIA DO JARI | AMAPÁ | Brasil | 1600808 | 16 | 33 | nan | nan | nan | Amazônia | 2.0 |
| 1af98d99-e556-3025-996f-26e383126b5e | -3.2916 | -53.85501 | 2024-11-23 05:33:00 | NPP-375D | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | 0.9 |
| e14b203c-9e33-3aa2-8c2b-c50906909185 | -1.7452 | -52.38615 | 2024-11-23 05:33:00 | NPP-375D | PORTO DE MOZ | PARÁ | Brasil | 1505908 | 15 | 33 | nan | nan | nan | Amazônia | 1.6 |
| 502d4806-fc33-3724-9f00-337c28e7a368 | -1.91429 | -53.34092 | 2024-11-23 05:33:00 | NPP-375D | PRAINHA | PARÁ | Brasil | 1506005 | 15 | 33 | nan | nan | nan | Amazônia | 1.5 |
| eb29f1c0-7078-3e7a-b788-3ac7bc3bd8bb | -1.60755 | -52.58726 | 2024-11-23 05:33:00 | NPP-375D | PORTO DE MOZ | PARÁ | Brasil | 1505908 | 15 | 33 | nan | nan | nan | Amazônia | 4.2 |
| 1b7f5655-e365-350d-8eb1-8f433ff16f06 | -1.67543 | -53.20831 | 2024-11-23 05:33:00 | NPP-375D | ALMEIRIM | PARÁ | Brasil | 1500503 | 15 | 33 | nan | nan | nan | Amazônia | 2.1 |
| 037ddbc5-ce44-30aa-94f6-485e6dd439bd | -1.61512 | -53.31145 | 2024-11-23 05:33:00 | NPP-375D | ALMEIRIM | PARÁ | Brasil | 1500503 | 15 | 33 | nan | nan | nan | Amazônia | 1.8 |
| 2e1e17e4-b19a-3164-b8ff-85edc49bda12 | -1.77771 | -53.61046 | 2024-11-23 05:33:00 | NPP-375D | PRAINHA | PARÁ | Brasil | 1506005 | 15 | 33 | nan | nan | nan | Amazônia | 2.4 |
| f9d68b52-8d06-3809-a396-7d026c0e9e45 | -3.80184 | -51.76168 | 2024-11-23 05:33:00 | NPP-375D | SENADOR JOSÉ PORFÍRIO | PARÁ | Brasil | 1507805 | 15 | 33 | nan | nan | nan | Amazônia | 1.4 |
| 1410c0e5-080b-3bab-9a6a-59ffd08f677f | -1.18718 | -51.93375 | 2024-11-23 05:33:00 | NPP-375D | ALMEIRIM | PARÁ | Brasil | 1500503 | 15 | 33 | nan | nan | nan | Amazônia | 1.0 |
| da393391-5f42-3058-b48a-ee4cefcc5768 | -1.45167 | -53.3919 | 2024-11-23 05:33:00 | NPP-375D | ALMEIRIM | PARÁ | Brasil | 1500503 | 15 | 33 | nan | nan | nan | Amazônia | 9.2 |
| a212c692-5825-309c-a5de-fa572c04e3f5 | -1.25625 | -51.76246 | 2024-11-23 05:33:00 | NPP-375D | GURUPÁ | PARÁ | Brasil | 1503101 | 15 | 33 | nan | nan | nan | Amazônia | 7.6 |
| fee8cdc7-0e0d-3487-96fa-7e22c32aa2f1 | -1.77241 | -53.60966 | 2024-11-23 05:33:00 | NPP-375D | PRAINHA | PARÁ | Brasil | 1506005 | 15 | 33 | nan | nan | nan | Amazônia | 2.4 |
| 17e1a756-fcfb-3253-8765-0d097348ac4d | -1.26286 | -51.75911 | 2024-11-23 05:33:00 | NPP-375D | GURUPÁ | PARÁ | Brasil | 1503101 | 15 | 33 | nan | nan | nan | Amazônia | 9.6 |
| 8b39555f-220c-3b32-b4da-3b6692be3d65 | -1.11001 | -53.39925 | 2024-11-23 05:33:00 | NPP-375D | ALMEIRIM | PARÁ | Brasil | 1500503 | 15 | 33 | nan | nan | nan | Amazônia | 2.6 |
| a95b4a15-4536-3c35-afb3-993651c97544 | -3.50762 | -53.80376 | 2024-11-23 05:33:00 | NPP-375D | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | 0.6 |
| 263f6c04-410c-3aff-a503-f6df7e4857bf | -1.25851 | -53.36426 | 2024-11-23 05:33:00 | NPP-375D | ALMEIRIM | PARÁ | Brasil | 1500503 | 15 | 33 | nan | nan | nan | Amazônia | 1.0 |
| dbb00ead-cfe9-314a-a349-f05d689d30b4 | -1.21074 | -51.74223 | 2024-11-23 05:33:00 | NPP-375D | GURUPÁ | PARÁ | Brasil | 1503101 | 15 | 33 | nan | nan | nan | Amazônia | 0.8 |
| 4cb55481-7182-327f-b529-803bd397471c | -0.14204 | -60.86407 | 2024-11-23 05:33:00 | NPP-375D | RORAINÓPOLIS | RORAIMA | Brasil | 1400472 | 14 | 33 | nan | nan | nan | Amazônia | 1.2 |
| 7c53d222-c189-3fee-808a-d3255c34f46c | -1.12065 | -53.40081 | 2024-11-23 05:33:00 | NPP-375D | ALMEIRIM | PARÁ | Brasil | 1500503 | 15 | 33 | nan | nan | nan | Amazônia | 1.2 |
| a637bcef-f390-3a81-b856-f77a0d19e3c2 | -1.63183 | -53.31045 | 2024-11-23 05:33:00 | NPP-375D | ALMEIRIM | PARÁ | Brasil | 1500503 | 15 | 33 | nan | nan | nan | Amazônia | 2.1 |
| c8e3e325-840e-333b-bd26-c77052b905de | -1.52602 | -51.55872 | 2024-11-23 05:33:00 | NPP-375D | GURUPÁ | PARÁ | Brasil | 1503101 | 15 | 33 | nan | nan | nan | Amazônia | 1.4 |
| a313e670-71a6-30e8-b770-66446f60fc23 | -1.67686 | -53.20417 | 2024-11-23 05:33:00 | NPP-375D | ALMEIRIM | PARÁ | Brasil | 1500503 | 15 | 33 | nan | nan | nan | Amazônia | 1.6 |
| 941100a1-4da0-3ec9-86f4-03f36129076d | -3.23073 | -53.93446 | 2024-11-23 05:33:00 | NPP-375D | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | 2.0 |
| 4212a325-da36-3b69-8780-a9aba143ba39 | -1.61088 | -52.60336 | 2024-11-23 05:33:00 | NPP-375D | PORTO DE MOZ | PARÁ | Brasil | 1505908 | 15 | 33 | nan | nan | nan | Amazônia | 4.9 |
| 6257ed79-dfbc-3575-9f96-86d67bc01184 | -2.06598 | -53.23116 | 2024-11-23 05:33:00 | NPP-375D | PORTO DE MOZ | PARÁ | Brasil | 1505908 | 15 | 33 | nan | nan | nan | Amazônia | 1.5 |
| fedd1afe-d592-3985-a831-1ede74da8096 | -3.46595 | -54.64468 | 2024-11-23 05:33:00 | NPP-375D | PLACAS | PARÁ | Brasil | 1505650 | 15 | 33 | nan | nan | nan | Amazônia | 1.0 |
| d56b8e6e-54f4-301e-be39-c06bb45b07ef | -2.79052 | -54.1593 | 2024-11-23 05:33:00 | NPP-375D | SANTARÉM | PARÁ | Brasil | 1506807 | 15 | 33 | nan | nan | nan | Amazônia | 0.9 |
| d92831a6-c5b6-35c7-a870-f64caee180a3 | -3.11819 | -53.10332 | 2024-11-23 05:33:00 | NPP-375D | MEDICILÂNDIA | PARÁ | Brasil | 1504455 | 15 | 33 | nan | nan | nan | Amazônia | 3.5 |
| 3d7d880c-f5e4-31ec-b86b-e3169f9bd5c7 | -1.63231 | -52.61445 | 2024-11-23 05:33:00 | NPP-375D | PORTO DE MOZ | PARÁ | Brasil | 1505908 | 15 | 33 | nan | nan | nan | Amazônia | 2.0 |
| 53bdca1e-0de6-3c87-92c3-639fde2f656c | -2.9331 | -54.28294 | 2024-11-23 05:33:00 | NPP-375D | MOJUÍ DOS CAMPOS | PARÁ | Brasil | 1504752 | 15 | 33 | nan | nan | nan | Amazônia | 2.0 |
| 167cae54-84b2-327a-8927-06f0b07729be | -3.24493 | -54.23034 | 2024-11-23 05:33:00 | NPP-375D | SANTARÉM | PARÁ | Brasil | 1506807 | 15 | 33 | nan | nan | nan | Amazônia | 0.6 |
| c76bba3f-dc40-35f9-a815-73b99feac93d | -1.72789 | -52.72617 | 2024-11-23 05:33:00 | NPP-375D | PORTO DE MOZ | PARÁ | Brasil | 1505908 | 15 | 33 | nan | nan | nan | Amazônia | 4.0 |
| 698b1855-3916-36f3-9583-f1f1bcbf40bf | -1.11638 | -53.39338 | 2024-11-23 05:33:00 | NPP-375D | ALMEIRIM | PARÁ | Brasil | 1500503 | 15 | 33 | nan | nan | nan | Amazônia | 2.2 |
| 3ec12ff1-9b62-3bfb-a9e2-24948088bd43 | -3.24508 | -54.23193 | 2024-11-23 05:33:00 | NPP-375D | SANTARÉM | PARÁ | Brasil | 1506807 | 15 | 33 | nan | nan | nan | Amazônia | 0.5 |
| 2ac5e9ae-0651-3e8f-ac2a-a51fe760b8b3 | -1.21734 | -51.73888 | 2024-11-23 05:33:00 | NPP-375D | GURUPÁ | PARÁ | Brasil | 1503101 | 15 | 33 | nan | nan | nan | Amazônia | 2.0 |
| 1fbfc47e-cd37-349b-866c-962c5845400e | -1.13858 | -51.67572 | 2024-11-23 05:33:00 | NPP-375D | GURUPÁ | PARÁ | Brasil | 1503101 | 15 | 33 | nan | nan | nan | Amazônia | 1.1 |
| b979b067-c9ab-3992-ad43-83a2b16ce439 | -3.23989 | -54.23111 | 2024-11-23 05:33:00 | NPP-375D | SANTARÉM | PARÁ | Brasil | 1506807 | 15 | 33 | nan | nan | nan | Amazônia | 0.5 |
| e923fcc4-b476-35ff-bd7d-df566d2245f7 | -1.04346 | -51.74029 | 2024-11-23 05:33:00 | NPP-375D | VITÓRIA DO JARI | AMAPÁ | Brasil | 1600808 | 16 | 33 | nan | nan | nan | Amazônia | 4.8 |
| 9af4ead7-2282-3f30-8a0b-65ac00e81acb | -1.414 | -54.28386 | 2024-11-23 05:33:00 | NPP-375D | MONTE ALEGRE | PARÁ | Brasil | 1504802 | 15 | 33 | nan | nan | nan | Amazônia | 0.8 |
| 988e2e6e-17f0-31ca-8a07-4b0d6b734515 | -3.27489 | -53.82135 | 2024-11-23 05:33:00 | NPP-375D | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | 2.0 |
| 5854888b-8e9f-3499-9160-5b11676641c4 | -3.11215 | -54.2923 | 2024-11-23 05:33:00 | NPP-375D | MOJUÍ DOS CAMPOS | PARÁ | Brasil | 1504752 | 15 | 33 | nan | nan | nan | Amazônia | 0.4 |
| 83c6ffe7-08bf-3835-9729-b31dba4b1605 | -0.95337 | -51.71563 | 2024-11-23 05:33:00 | NPP-375D | VITÓRIA DO JARI | AMAPÁ | Brasil | 1600808 | 16 | 33 | nan | nan | nan | Amazônia | 1.3 |


[Clique aqui para ver as próximas entradas](README65.md)
