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

## Dados Diários - Página 52

| ID | Latitude | Longitude | Data/Hora GMT | Satélite | Município | Estado | País | Município ID | Estado ID | País ID | Dias sem Chuva | Precipitação | Risco de Fogo | Bioma | FRP |
|----|----------|-----------|---------------|----------|-----------|--------|------|--------------|-----------|---------|----------------|--------------|----------------|-------|-----|
| fddf0f6c-fc6d-3d07-9d64-14a3927a82b4 | -2.88596 | -53.98865 | 2024-10-20 04:55:00 | NOAA-20 | PRAINHA | PARÁ | Brasil | 1506005 | 15 | 33 | nan | nan | nan | Amazônia | 1.6 |
| a6a08f44-5892-37ed-b37a-d1a6f81d11e4 | -2.79729 | -54.09887 | 2024-10-20 04:55:00 | NOAA-20 | PRAINHA | PARÁ | Brasil | 1506005 | 15 | 33 | nan | nan | nan | Amazônia | 0.5 |
| 4cf23e52-2f39-3c4d-82b1-fac0d754b296 | -2.785 | -54.02597 | 2024-10-20 04:55:00 | NOAA-20 | PRAINHA | PARÁ | Brasil | 1506005 | 15 | 33 | nan | nan | nan | Amazônia | 1.1 |
| 5a81aeb5-b6e1-3912-bdb3-75902fdd007f | -2.71578 | -53.99009 | 2024-10-20 04:55:00 | NOAA-20 | PRAINHA | PARÁ | Brasil | 1506005 | 15 | 33 | nan | nan | nan | Amazônia | 3.1 |
| 5ea3fee3-38cb-3501-b674-7b34ebf589cc | -3.59182 | -54.66346 | 2024-10-20 04:55:00 | NOAA-20 | PLACAS | PARÁ | Brasil | 1505650 | 15 | 33 | nan | nan | nan | Amazônia | 2.3 |
| 58b23559-ae8a-3f4c-a0b8-d9def8f79eef | -3.59127 | -54.66698 | 2024-10-20 04:55:00 | NOAA-20 | PLACAS | PARÁ | Brasil | 1505650 | 15 | 33 | nan | nan | nan | Amazônia | 1.5 |
| 589420ee-a172-3e7e-967c-e28c378e24f6 | -3.5896 | -54.67754 | 2024-10-20 04:55:00 | NOAA-20 | PLACAS | PARÁ | Brasil | 1505650 | 15 | 33 | nan | nan | nan | Amazônia | 2.0 |
| 213cfd8b-ad9e-3494-9ca3-228e95c3e448 | -3.58905 | -54.68105 | 2024-10-20 04:55:00 | NOAA-20 | PLACAS | PARÁ | Brasil | 1505650 | 15 | 33 | nan | nan | nan | Amazônia | 3.4 |
| caad9d89-56c7-3d60-8778-f20a0e041404 | -3.5885 | -54.68457 | 2024-10-20 04:55:00 | NOAA-20 | PLACAS | PARÁ | Brasil | 1505650 | 15 | 33 | nan | nan | nan | Amazônia | 3.4 |
| 9f8c85d8-fd1b-3a67-95e6-6548def49533 | -3.58626 | -54.67701 | 2024-10-20 04:55:00 | NOAA-20 | PLACAS | PARÁ | Brasil | 1505650 | 15 | 33 | nan | nan | nan | Amazônia | 1.7 |
| 59a75135-42f1-3f15-ba24-4cca3349769d | -3.58571 | -54.68052 | 2024-10-20 04:55:00 | NOAA-20 | PLACAS | PARÁ | Brasil | 1505650 | 15 | 33 | nan | nan | nan | Amazônia | 4.1 |
| 3da9fe37-9067-3f1f-90e5-6bd18c77fa58 | -3.58515 | -54.68404 | 2024-10-20 04:55:00 | NOAA-20 | PLACAS | PARÁ | Brasil | 1505650 | 15 | 33 | nan | nan | nan | Amazônia | 4.1 |
| 679c5955-b8d3-3ac5-a2f5-22143f5a47e9 | -3.58237 | -54.68 | 2024-10-20 04:55:00 | NOAA-20 | PLACAS | PARÁ | Brasil | 1505650 | 15 | 33 | nan | nan | nan | Amazônia | 4.1 |
| 1a7fb2f9-bdd4-3673-ac49-e10786bfd20e | -3.57345 | -54.62814 | 2024-10-20 04:55:00 | NOAA-20 | PLACAS | PARÁ | Brasil | 1505650 | 15 | 33 | nan | nan | nan | Amazônia | 0.8 |
| e0943583-a749-3d0f-80ee-848e6eb0a8f7 | -3.50607 | -54.68602 | 2024-10-20 04:55:00 | NOAA-20 | PLACAS | PARÁ | Brasil | 1505650 | 15 | 33 | nan | nan | nan | Amazônia | 0.8 |
| 0ebddd9c-5abd-3cdd-85c1-255fc81dcce3 | -3.50551 | -54.68954 | 2024-10-20 04:55:00 | NOAA-20 | PLACAS | PARÁ | Brasil | 1505650 | 15 | 33 | nan | nan | nan | Amazônia | 0.6 |
| 97510faa-dc71-3a04-8184-da3517589938 | -3.50273 | -54.6855 | 2024-10-20 04:55:00 | NOAA-20 | PLACAS | PARÁ | Brasil | 1505650 | 15 | 33 | nan | nan | nan | Amazônia | 5.5 |
| 0924de5b-a51f-3e06-92c0-07d39e65852e | -3.50217 | -54.68902 | 2024-10-20 04:55:00 | NOAA-20 | PLACAS | PARÁ | Brasil | 1505650 | 15 | 33 | nan | nan | nan | Amazônia | 2.1 |
| 3eb52c63-6d3a-341c-82eb-f2cb1344a51d | -3.40662 | -54.67009 | 2024-10-20 04:55:00 | NOAA-20 | MOJUÍ DOS CAMPOS | PARÁ | Brasil | 1504752 | 15 | 33 | nan | nan | nan | Amazônia | 1.3 |
| 9881cfc6-c682-3315-bcae-68c396cc3166 | -3.35118 | -54.74546 | 2024-10-20 04:55:00 | NOAA-20 | MOJUÍ DOS CAMPOS | PARÁ | Brasil | 1504752 | 15 | 33 | nan | nan | nan | Amazônia | 2.7 |
| 34ae4987-d237-3342-af52-f2100b424052 | -3.33494 | -54.80484 | 2024-10-20 04:55:00 | NOAA-20 | MOJUÍ DOS CAMPOS | PARÁ | Brasil | 1504752 | 15 | 33 | nan | nan | nan | Amazônia | 0.5 |
| edfa3c3b-3e9c-39bf-a6c4-3fd79049cc87 | -2.51912 | -54.65914 | 2024-10-20 04:55:00 | NOAA-20 | SANTARÉM | PARÁ | Brasil | 1506807 | 15 | 33 | nan | nan | nan | Amazônia | 0.6 |
| 74aa865a-c7f6-329a-b37e-f6b18c2a7dc2 | -2.48161 | -54.70073 | 2024-10-20 04:55:00 | NOAA-20 | SANTARÉM | PARÁ | Brasil | 1506807 | 15 | 33 | nan | nan | nan | Amazônia | 1.1 |
| 2246e149-6359-3cff-9b4c-83ea78e3fc4b | -3.15339 | -54.36134 | 2024-10-20 04:55:00 | NOAA-20 | MOJUÍ DOS CAMPOS | PARÁ | Brasil | 1504752 | 15 | 33 | nan | nan | nan | Amazônia | 1.8 |
| 45d4fb36-3908-3baa-baad-dd38cda38030 | -3.15061 | -54.35733 | 2024-10-20 04:55:00 | NOAA-20 | MOJUÍ DOS CAMPOS | PARÁ | Brasil | 1504752 | 15 | 33 | nan | nan | nan | Amazônia | 2.4 |
| 633c126e-76fa-364f-8ce2-b00d3c9629c4 | -3.15006 | -54.36081 | 2024-10-20 04:55:00 | NOAA-20 | MOJUÍ DOS CAMPOS | PARÁ | Brasil | 1504752 | 15 | 33 | nan | nan | nan | Amazônia | 1.8 |
| d831ac62-3bb6-3a80-bc33-6037fd897ce8 | -3.14951 | -54.3643 | 2024-10-20 04:55:00 | NOAA-20 | MOJUÍ DOS CAMPOS | PARÁ | Brasil | 1504752 | 15 | 33 | nan | nan | nan | Amazônia | 1.8 |
| db3f95be-36eb-3471-8bab-853253c9e4e3 | -3.14674 | -54.36029 | 2024-10-20 04:55:00 | NOAA-20 | MOJUÍ DOS CAMPOS | PARÁ | Brasil | 1504752 | 15 | 33 | nan | nan | nan | Amazônia | 2.8 |
| 69438794-2cf1-36ff-81d0-4250fac835ae | -3.14618 | -54.36376 | 2024-10-20 04:55:00 | NOAA-20 | MOJUÍ DOS CAMPOS | PARÁ | Brasil | 1504752 | 15 | 33 | nan | nan | nan | Amazônia | 2.8 |
| a4c58d1d-648d-383f-9730-a782d11d3b54 | -3.14451 | -54.3528 | 2024-10-20 04:55:00 | NOAA-20 | MOJUÍ DOS CAMPOS | PARÁ | Brasil | 1504752 | 15 | 33 | nan | nan | nan | Amazônia | 2.0 |
| 3d9e5f0a-6ab0-35d2-9c6d-0e7b88b7d444 | -3.14396 | -54.35628 | 2024-10-20 04:55:00 | NOAA-20 | MOJUÍ DOS CAMPOS | PARÁ | Brasil | 1504752 | 15 | 33 | nan | nan | nan | Amazônia | 2.0 |
| 72bdb53b-f075-366a-9aa0-05051b2c53a8 | -3.14341 | -54.35976 | 2024-10-20 04:55:00 | NOAA-20 | MOJUÍ DOS CAMPOS | PARÁ | Brasil | 1504752 | 15 | 33 | nan | nan | nan | Amazônia | 2.8 |
| 855edcfe-191c-3e55-8369-48f4e8ac5549 | -3.14286 | -54.36324 | 2024-10-20 04:55:00 | NOAA-20 | MOJUÍ DOS CAMPOS | PARÁ | Brasil | 1504752 | 15 | 33 | nan | nan | nan | Amazônia | 2.8 |
| ccd6cf73-ffa4-3cb9-abf1-7b2cdc61f055 | -3.14119 | -54.35226 | 2024-10-20 04:55:00 | NOAA-20 | MOJUÍ DOS CAMPOS | PARÁ | Brasil | 1504752 | 15 | 33 | nan | nan | nan | Amazônia | 1.2 |
| b5646894-25f0-3c81-9489-2bd959d2a8ca | -3.14064 | -54.35575 | 2024-10-20 04:55:00 | NOAA-20 | MOJUÍ DOS CAMPOS | PARÁ | Brasil | 1504752 | 15 | 33 | nan | nan | nan | Amazônia | 1.2 |
| 9489b40c-9558-311a-b85c-53cdd18e2938 | -3.14009 | -54.35923 | 2024-10-20 04:55:00 | NOAA-20 | MOJUÍ DOS CAMPOS | PARÁ | Brasil | 1504752 | 15 | 33 | nan | nan | nan | Amazônia | 2.7 |
| 6833fd5c-4954-3476-a592-05af73d6d375 | -3.13953 | -54.36272 | 2024-10-20 04:55:00 | NOAA-20 | MOJUÍ DOS CAMPOS | PARÁ | Brasil | 1504752 | 15 | 33 | nan | nan | nan | Amazônia | 2.7 |
| f9737e0a-b100-323f-8d1c-7fc912fd5efd | -3.13786 | -54.35174 | 2024-10-20 04:55:00 | NOAA-20 | MOJUÍ DOS CAMPOS | PARÁ | Brasil | 1504752 | 15 | 33 | nan | nan | nan | Amazônia | 1.2 |
| 6d823611-c51f-37ec-9f9a-00ec26829e45 | -3.13731 | -54.35522 | 2024-10-20 04:55:00 | NOAA-20 | MOJUÍ DOS CAMPOS | PARÁ | Brasil | 1504752 | 15 | 33 | nan | nan | nan | Amazônia | 1.2 |
| d25a29bd-ce1b-3d8c-a902-b9ba34e9e3da | -3.13676 | -54.35871 | 2024-10-20 04:55:00 | NOAA-20 | MOJUÍ DOS CAMPOS | PARÁ | Brasil | 1504752 | 15 | 33 | nan | nan | nan | Amazônia | 2.7 |
| 75f11149-7f09-3871-a037-e64c59d031d1 | -3.13454 | -54.35121 | 2024-10-20 04:55:00 | NOAA-20 | MOJUÍ DOS CAMPOS | PARÁ | Brasil | 1504752 | 15 | 33 | nan | nan | nan | Amazônia | 2.5 |
| 6cf9d460-25e4-30d1-a524-5f91b732d564 | -3.13399 | -54.35469 | 2024-10-20 04:55:00 | NOAA-20 | MOJUÍ DOS CAMPOS | PARÁ | Brasil | 1504752 | 15 | 33 | nan | nan | nan | Amazônia | 2.5 |
| 7da1eacb-555e-351f-ac17-2f631c7ba6bc | -3.13343 | -54.35818 | 2024-10-20 04:55:00 | NOAA-20 | MOJUÍ DOS CAMPOS | PARÁ | Brasil | 1504752 | 15 | 33 | nan | nan | nan | Amazônia | 2.4 |
| d19b95b2-a231-3875-aca9-69d5f2e7e81f | -3.13288 | -54.36167 | 2024-10-20 04:55:00 | NOAA-20 | MOJUÍ DOS CAMPOS | PARÁ | Brasil | 1504752 | 15 | 33 | nan | nan | nan | Amazônia | 2.4 |
| 155679c5-dae2-3d49-b1a6-556ca55ca6f9 | -3.13122 | -54.35068 | 2024-10-20 04:55:00 | NOAA-20 | MOJUÍ DOS CAMPOS | PARÁ | Brasil | 1504752 | 15 | 33 | nan | nan | nan | Amazônia | 2.5 |
| 7a08432c-21bf-3170-b2c7-601a44b80517 | -3.13066 | -54.35417 | 2024-10-20 04:55:00 | NOAA-20 | MOJUÍ DOS CAMPOS | PARÁ | Brasil | 1504752 | 15 | 33 | nan | nan | nan | Amazônia | 2.5 |
| 90b06946-3eac-3f99-a6fa-ce9e839469f7 | -3.13011 | -54.35765 | 2024-10-20 04:55:00 | NOAA-20 | MOJUÍ DOS CAMPOS | PARÁ | Brasil | 1504752 | 15 | 33 | nan | nan | nan | Amazônia | 2.4 |
| 990cebd2-8f22-3893-9dc5-fe86b947c414 | -3.12953 | -54.27545 | 2024-10-20 04:55:00 | NOAA-20 | MOJUÍ DOS CAMPOS | PARÁ | Brasil | 1504752 | 15 | 33 | nan | nan | nan | Amazônia | 0.8 |
| ca47522d-9660-3998-abaf-75149e80ac55 | -3.08724 | -54.43676 | 2024-10-20 04:55:00 | NOAA-20 | MOJUÍ DOS CAMPOS | PARÁ | Brasil | 1504752 | 15 | 33 | nan | nan | nan | Amazônia | 0.9 |
| 6a541674-fb56-3c28-9d1a-1bb35005a070 | -3.01933 | -54.04825 | 2024-10-20 04:55:00 | NOAA-20 | SANTARÉM | PARÁ | Brasil | 1506807 | 15 | 33 | nan | nan | nan | Amazônia | 1.1 |
| c3b3f600-f482-3e68-adef-9127f1e52317 | -3.01656 | -54.04427 | 2024-10-20 04:55:00 | NOAA-20 | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | 2.7 |
| c14e3c5a-e4bd-3324-b2c1-102a7ffbcea2 | -2.95433 | -54.15878 | 2024-10-20 04:55:00 | NOAA-20 | SANTARÉM | PARÁ | Brasil | 1506807 | 15 | 33 | nan | nan | nan | Amazônia | 1.5 |
| 19ba0f03-f45a-3d3b-9fb4-ce56f37fa1ed | -2.95101 | -54.15826 | 2024-10-20 04:55:00 | NOAA-20 | SANTARÉM | PARÁ | Brasil | 1506807 | 15 | 33 | nan | nan | nan | Amazônia | 1.5 |
| 9e1b0bd1-158e-3244-9a28-0c98d4e597d2 | -2.91454 | -54.25948 | 2024-10-20 04:55:00 | NOAA-20 | SANTARÉM | PARÁ | Brasil | 1506807 | 15 | 33 | nan | nan | nan | Amazônia | 0.6 |
| 7f639a41-3259-3c1d-a953-7905ee8338f5 | -2.86793 | -54.10282 | 2024-10-20 04:55:00 | NOAA-20 | PRAINHA | PARÁ | Brasil | 1506005 | 15 | 33 | nan | nan | nan | Amazônia | 0.4 |
| df891cab-4b94-39bf-a772-44e13175eaf3 | -2.75575 | -54.03913 | 2024-10-20 04:55:00 | NOAA-20 | PRAINHA | PARÁ | Brasil | 1506005 | 15 | 33 | nan | nan | nan | Amazônia | 2.8 |
| bb7e3b2b-9319-3f97-b00a-240e1866bb06 | -2.71523 | -53.99353 | 2024-10-20 04:55:00 | NOAA-20 | PRAINHA | PARÁ | Brasil | 1506005 | 15 | 33 | nan | nan | nan | Amazônia | 2.9 |
| 00ec0227-82e7-379f-b85a-27aedbc84254 | -2.71246 | -53.98959 | 2024-10-20 04:55:00 | NOAA-20 | PRAINHA | PARÁ | Brasil | 1506005 | 15 | 33 | nan | nan | nan | Amazônia | 3.1 |
| 41b420e1-c722-36c5-8e6e-ab2f833fcfbb | -2.63332 | -54.31906 | 2024-10-20 04:55:00 | NOAA-20 | SANTARÉM | PARÁ | Brasil | 1506807 | 15 | 33 | nan | nan | nan | Amazônia | 1.3 |
| da62a700-7f60-3c94-b579-178f9ec54e80 | -2.63222 | -54.32605 | 2024-10-20 04:55:00 | NOAA-20 | SANTARÉM | PARÁ | Brasil | 1506807 | 15 | 33 | nan | nan | nan | Amazônia | 2.5 |
| 0dd13ab4-12e1-3eab-b290-fbdffb464121 | -2.63167 | -54.32955 | 2024-10-20 04:55:00 | NOAA-20 | SANTARÉM | PARÁ | Brasil | 1506807 | 15 | 33 | nan | nan | nan | Amazônia | 2.5 |
| 90eacf1e-3369-39dc-8555-1b8794550edf | -2.57487 | -54.21687 | 2024-10-20 04:55:00 | NOAA-20 | PRAINHA | PARÁ | Brasil | 1506005 | 15 | 33 | nan | nan | nan | Amazônia | 1.6 |
| c803500f-59ea-3ced-94ba-d54e491cbd3a | -2.56621 | -54.01266 | 2024-10-20 04:55:00 | NOAA-20 | PRAINHA | PARÁ | Brasil | 1506005 | 15 | 33 | nan | nan | nan | Amazônia | 1.8 |
| f642ef5c-d8db-3dbe-8fdb-d20c7677e23e | -2.31951 | -54.39288 | 2024-10-20 04:55:00 | NOAA-20 | SANTARÉM | PARÁ | Brasil | 1506807 | 15 | 33 | nan | nan | nan | Amazônia | 5.9 |
| d87f7b8b-0b72-3d1f-a9a2-c8ee23740e39 | -2.31839 | -54.37829 | 2024-10-20 04:55:00 | NOAA-20 | MONTE ALEGRE | PARÁ | Brasil | 1504802 | 15 | 33 | nan | nan | nan | Amazônia | 4.0 |
| 8b4b3f84-17e8-3621-b21f-717ec5ba3144 | -2.31783 | -54.38181 | 2024-10-20 04:55:00 | NOAA-20 | SANTARÉM | PARÁ | Brasil | 1506807 | 15 | 33 | nan | nan | nan | Amazônia | 2.8 |
| 19cea162-0993-3788-8b91-02e0cf0b8e44 | -2.31728 | -54.38532 | 2024-10-20 04:55:00 | NOAA-20 | SANTARÉM | PARÁ | Brasil | 1506807 | 15 | 33 | nan | nan | nan | Amazônia | 2.8 |
| 88a8cc42-417d-340b-8e15-cea7dacaea78 | -2.31673 | -54.38884 | 2024-10-20 04:55:00 | NOAA-20 | SANTARÉM | PARÁ | Brasil | 1506807 | 15 | 33 | nan | nan | nan | Amazônia | 5.9 |
| 33c19b12-f285-3058-b2d0-e2c2d696ec02 | -2.31617 | -54.39236 | 2024-10-20 04:55:00 | NOAA-20 | SANTARÉM | PARÁ | Brasil | 1506807 | 15 | 33 | nan | nan | nan | Amazônia | 5.9 |
| c805c711-3185-3e6d-8ea5-4d0ee6d69aca | -3.1125 | -54.98986 | 2024-10-20 04:55:00 | NOAA-20 | BELTERRA | PARÁ | Brasil | 1501451 | 15 | 33 | nan | nan | nan | Amazônia | 1.0 |
| f52b76bb-694b-3b5d-b0c5-580593e9dd96 | -3.55118 | -53.99361 | 2024-10-20 04:55:00 | NOAA-20 | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | 1.0 |
| 920585b9-1a37-3dfd-8ec2-24de5bf6c6f2 | -3.49554 | -54.45403 | 2024-10-20 04:55:00 | NOAA-20 | PLACAS | PARÁ | Brasil | 1505650 | 15 | 33 | nan | nan | nan | Amazônia | 1.1 |
| dcb4f2d2-d4f6-333d-8559-adbf2c1bf5fa | -3.49499 | -54.45752 | 2024-10-20 04:55:00 | NOAA-20 | PLACAS | PARÁ | Brasil | 1505650 | 15 | 33 | nan | nan | nan | Amazônia | 2.8 |
| fd1d6f28-35dd-3f89-b253-e01630e98fc9 | -3.49222 | -54.45351 | 2024-10-20 04:55:00 | NOAA-20 | PLACAS | PARÁ | Brasil | 1505650 | 15 | 33 | nan | nan | nan | Amazônia | 1.2 |
| 6c76f264-a447-3a9c-bed0-56b7ec5ffe75 | -3.49166 | -54.457 | 2024-10-20 04:55:00 | NOAA-20 | PLACAS | PARÁ | Brasil | 1505650 | 15 | 33 | nan | nan | nan | Amazônia | 1.3 |
| c2c39504-3cfc-3039-872b-fcdcd401d44b | -3.4388 | -54.14645 | 2024-10-20 04:55:00 | NOAA-20 | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | 0.6 |
| a26b6fbb-cb3a-35d7-b496-32845ccb49d6 | -3.43876 | -54.12516 | 2024-10-20 04:55:00 | NOAA-20 | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | 1.0 |
| 1f7d915d-dde2-3b0b-99c4-bfa1b73251bb | -3.43825 | -54.14992 | 2024-10-20 04:55:00 | NOAA-20 | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | 0.6 |
| 75e3defe-b7ef-3a7f-a20e-0f706c379ae8 | -3.43545 | -54.12464 | 2024-10-20 04:55:00 | NOAA-20 | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | 0.6 |
| dcad616c-4893-3a09-85b5-ef7349c17b18 | -3.43502 | -54.19202 | 2024-10-20 04:55:00 | NOAA-20 | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | 0.8 |
| 2202824d-6ba6-3a25-a208-082941dd7784 | -3.43494 | -54.14939 | 2024-10-20 04:55:00 | NOAA-20 | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | 0.6 |
| 1d636ec7-873c-3ce8-b3b0-9ee8de4eddd6 | -3.42832 | -54.14834 | 2024-10-20 04:55:00 | NOAA-20 | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | 0.6 |
| 2e193578-3d1e-3053-978d-7862ba3eaa8e | -3.3311 | -54.18251 | 2024-10-20 04:55:00 | NOAA-20 | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | 0.7 |
| 586018f3-0b8a-3dad-8376-80d465289172 | -3.32778 | -54.18199 | 2024-10-20 04:55:00 | NOAA-20 | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | 0.7 |
| 26d1fd51-cc32-3d65-8b07-2bb29e3833a9 | -3.32724 | -54.18545 | 2024-10-20 04:55:00 | NOAA-20 | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | 0.7 |
| 1ae6857a-eae9-335d-ab3a-62404de562dc | -3.27471 | -54.15238 | 2024-10-20 04:55:00 | NOAA-20 | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | 3.0 |
| 94ee7bf1-668e-3d02-aa34-89f984d10d28 | -3.27416 | -54.15586 | 2024-10-20 04:55:00 | NOAA-20 | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | 3.0 |
| 43d220cc-c1ed-3551-ba72-d00152a7474e | -3.27084 | -54.15535 | 2024-10-20 04:55:00 | NOAA-20 | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | 3.0 |
| 2173427e-a8a4-31eb-920f-fd87a9683b81 | -3.26808 | -54.15136 | 2024-10-20 04:55:00 | NOAA-20 | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | 1.3 |
| 0af9f7ed-ea2b-39dc-8d21-3ca3651752c3 | -3.26753 | -54.15483 | 2024-10-20 04:55:00 | NOAA-20 | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | 1.3 |
| 59bb5f3c-2323-30db-a9bd-8c2d7435891d | -3.26646 | -54.18301 | 2024-10-20 04:55:00 | NOAA-20 | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | 1.5 |
| e6ac0eb3-092c-3905-a079-667315319a7f | -3.25375 | -54.17746 | 2024-10-20 04:55:00 | NOAA-20 | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | 1.8 |
| 94120e43-afd6-3615-8893-8d5c4a547d8e | -4.08082 | -54.16917 | 2024-10-20 04:55:00 | NOAA-20 | PLACAS | PARÁ | Brasil | 1505650 | 15 | 33 | nan | nan | nan | Amazônia | 0.5 |
| fc0902c8-1f77-36d0-a418-d451d7cafbdb | -4.07852 | -54.11929 | 2024-10-20 04:55:00 | NOAA-20 | PLACAS | PARÁ | Brasil | 1505650 | 15 | 33 | nan | nan | nan | Amazônia | 2.4 |
| 3d480bc0-c808-3389-ab44-d64ba246de2f | -4.0763 | -54.11189 | 2024-10-20 04:55:00 | NOAA-20 | PLACAS | PARÁ | Brasil | 1505650 | 15 | 33 | nan | nan | nan | Amazônia | 0.7 |
| 00f4ed13-9551-3c56-b3c0-c171bdba13e8 | -4.07575 | -54.11533 | 2024-10-20 04:55:00 | NOAA-20 | PLACAS | PARÁ | Brasil | 1505650 | 15 | 33 | nan | nan | nan | Amazônia | 1.9 |
| 396892cc-5d90-3af5-9e30-9818eb688578 | -4.07521 | -54.11877 | 2024-10-20 04:55:00 | NOAA-20 | PLACAS | PARÁ | Brasil | 1505650 | 15 | 33 | nan | nan | nan | Amazônia | 1.9 |
| 9234d595-a844-3cfb-8df0-8548860dea8c | -4.05154 | -53.8789 | 2024-10-20 04:55:00 | NOAA-20 | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | 1.2 |
| f50b3314-48f9-3df2-84b8-5b6b04fc5cdb | -3.83688 | -53.99331 | 2024-10-20 04:55:00 | NOAA-20 | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | 1.8 |
| 1cbd3faa-3247-30b1-bf1d-ac0b8e7bb105 | -3.83633 | -53.99675 | 2024-10-20 04:55:00 | NOAA-20 | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | 1.8 |


[Clique aqui para ver as próximas entradas](README53.md)
