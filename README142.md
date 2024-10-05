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

## Dados Diários - Página 142

| ID | Latitude | Longitude | Data/Hora GMT | Satélite | Município | Estado | País | Município ID | Estado ID | País ID | Dias sem Chuva | Precipitação | Risco de Fogo | Bioma | FRP |
|----|----------|-----------|---------------|----------|-----------|--------|------|--------------|-----------|---------|----------------|--------------|----------------|-------|-----|
| a64546fa-02b0-37d1-b54f-a23de99d81cb | -16.79028 | -57.82965 | 2024-10-05 05:31:00 | NOAA-21 | CÁCERES | MATO GROSSO | Brasil | 5102504 | 51 | 33 | nan | nan | nan | Pantanal | 2.9 |
| 8dd19e2b-806e-3625-818f-a2db757d204b | -16.78752 | -57.47302 | 2024-10-05 05:31:00 | NOAA-21 | CÁCERES | MATO GROSSO | Brasil | 5102504 | 51 | 33 | nan | nan | nan | Pantanal | 5.9 |
| 5a69a583-b275-36fe-8300-cf57afc7638a | -16.78692 | -57.43873 | 2024-10-05 05:31:00 | NOAA-21 | CÁCERES | MATO GROSSO | Brasil | 5102504 | 51 | 33 | nan | nan | nan | Pantanal | 5.8 |
| 7c04ba50-8b52-3ed8-b799-7b50a6617d40 | -16.78688 | -57.47166 | 2024-10-05 05:31:00 | NOAA-21 | CÁCERES | MATO GROSSO | Brasil | 5102504 | 51 | 33 | nan | nan | nan | Pantanal | 5.8 |
| 271fb774-148f-3201-8ad9-b57997a9d53f | -16.78653 | -57.43743 | 2024-10-05 05:31:00 | NOAA-21 | CÁCERES | MATO GROSSO | Brasil | 5102504 | 51 | 33 | nan | nan | nan | Pantanal | 9.8 |
| 4a054096-61dc-30fd-bb44-0fc75e881de1 | -16.78472 | -57.83812 | 2024-10-05 05:31:00 | NOAA-21 | CÁCERES | MATO GROSSO | Brasil | 5102504 | 51 | 33 | nan | nan | nan | Pantanal | 2.4 |
| 5bef0bca-4d83-3b5a-9a87-f0d76007714a | -16.78448 | -57.49081 | 2024-10-05 05:31:00 | NOAA-21 | CÁCERES | MATO GROSSO | Brasil | 5102504 | 51 | 33 | nan | nan | nan | Pantanal | 3.3 |
| 2dfe98cf-8d5f-3da1-97a1-74fa9dcf0b0f | -16.78416 | -57.84266 | 2024-10-05 05:31:00 | NOAA-21 | CÁCERES | MATO GROSSO | Brasil | 5102504 | 51 | 33 | nan | nan | nan | Pantanal | 2.1 |
| 76f79989-035a-3839-9606-a4f576376d3d | -16.7824 | -57.4772 | 2024-10-05 05:31:00 | NOAA-21 | CÁCERES | MATO GROSSO | Brasil | 5102504 | 51 | 33 | nan | nan | nan | Pantanal | 3.7 |
| 5eb98698-eeaf-36e1-a5cd-6cde7907a5a7 | -16.78236 | -57.43809 | 2024-10-05 05:31:00 | NOAA-21 | CÁCERES | MATO GROSSO | Brasil | 5102504 | 51 | 33 | nan | nan | nan | Pantanal | 5.8 |
| fa664dc1-04b8-32f3-8467-2894930f9578 | -16.78173 | -57.47584 | 2024-10-05 05:31:00 | NOAA-21 | CÁCERES | MATO GROSSO | Brasil | 5102504 | 51 | 33 | nan | nan | nan | Pantanal | 4.6 |
| b54225b6-c42d-32d0-83cb-7467ce84b44d | -16.78127 | -57.4868 | 2024-10-05 05:31:00 | NOAA-21 | CÁCERES | MATO GROSSO | Brasil | 5102504 | 51 | 33 | nan | nan | nan | Pantanal | 10.5 |
| a0f38ac3-af54-363c-9f88-03d6dc77d0db | -16.78113 | -57.48063 | 2024-10-05 05:31:00 | NOAA-21 | CÁCERES | MATO GROSSO | Brasil | 5102504 | 51 | 33 | nan | nan | nan | Pantanal | 4.6 |
| 0534642f-39b1-3815-b511-9cb07272f664 | -16.78071 | -57.49158 | 2024-10-05 05:31:00 | NOAA-21 | CÁCERES | MATO GROSSO | Brasil | 5102504 | 51 | 33 | nan | nan | nan | Pantanal | 5.5 |
| 12047898-4ccb-3a87-b559-eef2ea753714 | -16.78053 | -57.48541 | 2024-10-05 05:31:00 | NOAA-21 | CÁCERES | MATO GROSSO | Brasil | 5102504 | 51 | 33 | nan | nan | nan | Pantanal | 3.3 |
| d9df9531-abfa-38d1-84f6-0f1361b3723d | -16.78028 | -57.8375 | 2024-10-05 05:31:00 | NOAA-21 | CÁCERES | MATO GROSSO | Brasil | 5102504 | 51 | 33 | nan | nan | nan | Pantanal | 2.4 |
| 3e6d0514-c90b-3e41-a1b9-379484d43749 | -16.78014 | -57.49635 | 2024-10-05 05:31:00 | NOAA-21 | CÁCERES | MATO GROSSO | Brasil | 5102504 | 51 | 33 | nan | nan | nan | Pantanal | 5.5 |
| fa58a746-52d4-3581-9e84-ca6040334a9c | -16.77993 | -57.49019 | 2024-10-05 05:31:00 | NOAA-21 | CÁCERES | MATO GROSSO | Brasil | 5102504 | 51 | 33 | nan | nan | nan | Pantanal | 3.3 |
| 51bbf680-d5b7-3652-bcc1-c1f6d900dd60 | -16.77958 | -57.50115 | 2024-10-05 05:31:00 | NOAA-21 | CÁCERES | MATO GROSSO | Brasil | 5102504 | 51 | 33 | nan | nan | nan | Pantanal | 6.6 |
| 67973e46-e09e-3d5d-8e78-0e179ed50b06 | -16.77933 | -57.49495 | 2024-10-05 05:31:00 | NOAA-21 | CÁCERES | MATO GROSSO | Brasil | 5102504 | 51 | 33 | nan | nan | nan | Pantanal | 7.8 |
| 1ac80091-2dac-32c3-95c3-fcaebd2af93e | -16.77874 | -57.49973 | 2024-10-05 05:31:00 | NOAA-21 | CÁCERES | MATO GROSSO | Brasil | 5102504 | 51 | 33 | nan | nan | nan | Pantanal | 7.8 |
| 61f9be4f-a6d4-3cf5-9e55-7f8bd2b6e430 | -16.77785 | -57.47657 | 2024-10-05 05:31:00 | NOAA-21 | CÁCERES | MATO GROSSO | Brasil | 5102504 | 51 | 33 | nan | nan | nan | Pantanal | 3.7 |
| 2220c6d0-e57b-3b74-8ba3-5e28d7aa26f6 | -16.77729 | -57.48138 | 2024-10-05 05:31:00 | NOAA-21 | CÁCERES | MATO GROSSO | Brasil | 5102504 | 51 | 33 | nan | nan | nan | Pantanal | 10.5 |
| 0b6cada7-c740-3bda-bab8-dd73b16ff59c | -16.77673 | -57.48618 | 2024-10-05 05:31:00 | NOAA-21 | CÁCERES | MATO GROSSO | Brasil | 5102504 | 51 | 33 | nan | nan | nan | Pantanal | 10.5 |
| a8b96eb7-7448-378f-a404-894892ee3dd4 | -16.77658 | -57.48 | 2024-10-05 05:31:00 | NOAA-21 | CÁCERES | MATO GROSSO | Brasil | 5102504 | 51 | 33 | nan | nan | nan | Pantanal | 4.4 |
| 68163e76-4fe4-3ddb-828c-71e6e8fcb6ef | -16.77616 | -57.49096 | 2024-10-05 05:31:00 | NOAA-21 | CÁCERES | MATO GROSSO | Brasil | 5102504 | 51 | 33 | nan | nan | nan | Pantanal | 5.5 |
| 1d51a82b-9226-3230-b1f9-94cfc546c680 | -16.77598 | -57.48479 | 2024-10-05 05:31:00 | NOAA-21 | CÁCERES | MATO GROSSO | Brasil | 5102504 | 51 | 33 | nan | nan | nan | Pantanal | 16.1 |
| 781d2116-55ee-3d4d-b622-82bf81ea87c4 | -16.7756 | -57.49573 | 2024-10-05 05:31:00 | NOAA-21 | CÁCERES | MATO GROSSO | Brasil | 5102504 | 51 | 33 | nan | nan | nan | Pantanal | 5.5 |
| a8d1b590-123c-3d01-8d10-8363112c8e75 | -16.77539 | -57.48957 | 2024-10-05 05:31:00 | NOAA-21 | CÁCERES | MATO GROSSO | Brasil | 5102504 | 51 | 33 | nan | nan | nan | Pantanal | 16.1 |
| c851f9b1-bdef-31e3-90ee-2e9f9894aeab | -16.77502 | -57.45541 | 2024-10-05 05:31:00 | NOAA-21 | CÁCERES | MATO GROSSO | Brasil | 5102504 | 51 | 33 | nan | nan | nan | Pantanal | 3.8 |
| a1b47bd0-606c-3fbc-b664-20546120d353 | -16.77479 | -57.49433 | 2024-10-05 05:31:00 | NOAA-21 | CÁCERES | MATO GROSSO | Brasil | 5102504 | 51 | 33 | nan | nan | nan | Pantanal | 5.5 |
| 3f89e028-3ecf-3ac4-9de8-a649661d50c8 | -16.77442 | -57.46021 | 2024-10-05 05:31:00 | NOAA-21 | CÁCERES | MATO GROSSO | Brasil | 5102504 | 51 | 33 | nan | nan | nan | Pantanal | 3.8 |
| 5595e9b3-5076-3e78-9f3d-401e86a8fa67 | -16.77263 | -57.4746 | 2024-10-05 05:31:00 | NOAA-21 | CÁCERES | MATO GROSSO | Brasil | 5102504 | 51 | 33 | nan | nan | nan | Pantanal | 4.4 |
| e6f04da7-6a82-3576-be55-ad4c807dc0cd | -16.77203 | -57.47939 | 2024-10-05 05:31:00 | NOAA-21 | CÁCERES | MATO GROSSO | Brasil | 5102504 | 51 | 33 | nan | nan | nan | Pantanal | 4.4 |
| 4cdb798a-4d4d-3966-aa14-5be318854592 | -16.77166 | -57.44519 | 2024-10-05 05:31:00 | NOAA-21 | CÁCERES | MATO GROSSO | Brasil | 5102504 | 51 | 33 | nan | nan | nan | Pantanal | 27.2 |
| 29d3c94e-8c06-353c-a332-563c6cb99f1a | -16.77084 | -57.48895 | 2024-10-05 05:31:00 | NOAA-21 | CÁCERES | MATO GROSSO | Brasil | 5102504 | 51 | 33 | nan | nan | nan | Pantanal | 16.1 |
| 30bffb27-a273-3277-8b19-4002312f3601 | -16.77025 | -57.49372 | 2024-10-05 05:31:00 | NOAA-21 | CÁCERES | MATO GROSSO | Brasil | 5102504 | 51 | 33 | nan | nan | nan | Pantanal | 5.5 |
| c8fe4fb8-329d-37c0-a65e-e568f136df0a | -16.76867 | -57.46919 | 2024-10-05 05:31:00 | NOAA-21 | CÁCERES | MATO GROSSO | Brasil | 5102504 | 51 | 33 | nan | nan | nan | Pantanal | 3.3 |
| 44a9d7fe-dad2-3b88-9017-c821fc5d641c | -16.76829 | -57.43494 | 2024-10-05 05:31:00 | NOAA-21 | CÁCERES | MATO GROSSO | Brasil | 5102504 | 51 | 33 | nan | nan | nan | Pantanal | 3.8 |
| bd20aa86-2403-3604-95b3-77892ade898b | -16.76808 | -57.47398 | 2024-10-05 05:31:00 | NOAA-21 | CÁCERES | MATO GROSSO | Brasil | 5102504 | 51 | 33 | nan | nan | nan | Pantanal | 4.2 |
| a72f0cc7-af90-3134-a95f-c46c8ce84e62 | -16.76769 | -57.43975 | 2024-10-05 05:31:00 | NOAA-21 | CÁCERES | MATO GROSSO | Brasil | 5102504 | 51 | 33 | nan | nan | nan | Pantanal | 3.8 |
| 41e27159-fd0b-3f12-80e4-5f596b1eda7e | -16.76749 | -57.47877 | 2024-10-05 05:31:00 | NOAA-21 | CÁCERES | MATO GROSSO | Brasil | 5102504 | 51 | 33 | nan | nan | nan | Pantanal | 4.2 |
| dd8f6f63-7c6d-3753-8311-5a9db47b3a64 | -16.76689 | -57.48355 | 2024-10-05 05:31:00 | NOAA-21 | CÁCERES | MATO GROSSO | Brasil | 5102504 | 51 | 33 | nan | nan | nan | Pantanal | 9.2 |
| 61fbdb80-1440-36f3-a3c1-482d63ea6290 | -16.7663 | -57.48833 | 2024-10-05 05:31:00 | NOAA-21 | CÁCERES | MATO GROSSO | Brasil | 5102504 | 51 | 33 | nan | nan | nan | Pantanal | 9.2 |
| bb1bd474-f196-3f15-a9eb-8f314d2d12fe | -16.76472 | -57.46378 | 2024-10-05 05:31:00 | NOAA-21 | CÁCERES | MATO GROSSO | Brasil | 5102504 | 51 | 33 | nan | nan | nan | Pantanal | 3.3 |
| 6e453bc8-9025-300c-a88b-ea4f25336179 | -16.76413 | -57.46856 | 2024-10-05 05:31:00 | NOAA-21 | CÁCERES | MATO GROSSO | Brasil | 5102504 | 51 | 33 | nan | nan | nan | Pantanal | 3.3 |
| 8157c1c5-f34e-3f97-a8e3-6e124db38d7e | -16.76235 | -57.48293 | 2024-10-05 05:31:00 | NOAA-21 | CÁCERES | MATO GROSSO | Brasil | 5102504 | 51 | 33 | nan | nan | nan | Pantanal | 9.2 |
| fd088a14-d76f-3d46-a08d-c476754b823e | -16.76175 | -57.48771 | 2024-10-05 05:31:00 | NOAA-21 | CÁCERES | MATO GROSSO | Brasil | 5102504 | 51 | 33 | nan | nan | nan | Pantanal | 9.2 |
| 58728c47-32a6-3a2e-b9bd-17baec630c22 | -16.76116 | -57.49248 | 2024-10-05 05:31:00 | NOAA-21 | CÁCERES | MATO GROSSO | Brasil | 5102504 | 51 | 33 | nan | nan | nan | Pantanal | 26.7 |
| 70d5e769-35a9-3772-8018-cac9f54bac54 | -16.76017 | -57.46316 | 2024-10-05 05:31:00 | NOAA-21 | CÁCERES | MATO GROSSO | Brasil | 5102504 | 51 | 33 | nan | nan | nan | Pantanal | 6.4 |
| 8f8e432c-c2b1-3756-8541-8d78a48fd07d | -16.75662 | -57.49186 | 2024-10-05 05:31:00 | NOAA-21 | CÁCERES | MATO GROSSO | Brasil | 5102504 | 51 | 33 | nan | nan | nan | Pantanal | 15.6 |
| f32440a2-6360-3990-bf3b-953535167a07 | -16.75562 | -57.46252 | 2024-10-05 05:31:00 | NOAA-21 | CÁCERES | MATO GROSSO | Brasil | 5102504 | 51 | 33 | nan | nan | nan | Pantanal | 6.4 |
| 070d5db4-62a9-30be-a8b8-dce2fe2ef995 | -16.75503 | -57.46731 | 2024-10-05 05:31:00 | NOAA-21 | CÁCERES | MATO GROSSO | Brasil | 5102504 | 51 | 33 | nan | nan | nan | Pantanal | 6.4 |
| d9babb0e-a974-3430-96bd-bc2195e8d60e | -16.75208 | -57.49125 | 2024-10-05 05:31:00 | NOAA-21 | CÁCERES | MATO GROSSO | Brasil | 5102504 | 51 | 33 | nan | nan | nan | Pantanal | 15.6 |
| 48ff227e-652f-3dd5-b629-0ad72f15a119 | -16.7485 | -57.76342 | 2024-10-05 05:31:00 | NOAA-21 | CÁCERES | MATO GROSSO | Brasil | 5102504 | 51 | 33 | nan | nan | nan | Pantanal | 2.3 |
| 170126ad-756c-3706-bd8b-b20aeade0018 | -16.74079 | -57.47024 | 2024-10-05 05:31:00 | NOAA-21 | CÁCERES | MATO GROSSO | Brasil | 5102504 | 51 | 33 | nan | nan | nan | Pantanal | 4.6 |
| 1a02b9e5-6b7c-341a-98f9-cb72fd9f62fc | -16.73683 | -57.46482 | 2024-10-05 05:31:00 | NOAA-21 | CÁCERES | MATO GROSSO | Brasil | 5102504 | 51 | 33 | nan | nan | nan | Pantanal | 4.0 |
| 3051117a-f944-339a-9d80-2346fcff2bd2 | -16.73624 | -57.46962 | 2024-10-05 05:31:00 | NOAA-21 | CÁCERES | MATO GROSSO | Brasil | 5102504 | 51 | 33 | nan | nan | nan | Pantanal | 4.6 |
| 1683d717-72bc-3859-aab9-c8c5b350289c | -16.73566 | -57.47441 | 2024-10-05 05:31:00 | NOAA-21 | CÁCERES | MATO GROSSO | Brasil | 5102504 | 51 | 33 | nan | nan | nan | Pantanal | 4.6 |
| aab3b4ac-dbfa-32f3-a7e2-110bfa6572fd | -16.73228 | -57.46419 | 2024-10-05 05:31:00 | NOAA-21 | CÁCERES | MATO GROSSO | Brasil | 5102504 | 51 | 33 | nan | nan | nan | Pantanal | 2.9 |
| 7449b99d-9332-3538-a826-e23ade27bfbb | -16.7317 | -57.46899 | 2024-10-05 05:31:00 | NOAA-21 | CÁCERES | MATO GROSSO | Brasil | 5102504 | 51 | 33 | nan | nan | nan | Pantanal | 5.3 |
| d460cee6-d40a-30bc-b309-3ebf25b5b7a7 | -16.72773 | -57.46356 | 2024-10-05 05:31:00 | NOAA-21 | CÁCERES | MATO GROSSO | Brasil | 5102504 | 51 | 33 | nan | nan | nan | Pantanal | 2.9 |
| 7cfa8569-149b-3954-b12e-d96197e566fc | -17.05109 | -56.79451 | 2024-10-05 05:31:00 | NOAA-21 | POCONÉ | MATO GROSSO | Brasil | 5106505 | 51 | 33 | nan | nan | nan | Pantanal | 3.3 |
| 619b8732-4921-319a-8010-9a01817133f4 | -17.04153 | -56.79322 | 2024-10-05 05:31:00 | NOAA-21 | POCONÉ | MATO GROSSO | Brasil | 5106505 | 51 | 33 | nan | nan | nan | Pantanal | 4.8 |
| f4e978ad-d314-3c00-8ed9-f82745c25e0a | -17.03611 | -56.79794 | 2024-10-05 05:31:00 | NOAA-21 | POCONÉ | MATO GROSSO | Brasil | 5106505 | 51 | 33 | nan | nan | nan | Pantanal | 7.6 |
| 2dfabee0-15f5-392f-a323-aaa3e1b18ce3 | -17.03351 | -56.73743 | 2024-10-05 05:31:00 | NOAA-21 | POCONÉ | MATO GROSSO | Brasil | 5106505 | 51 | 33 | nan | nan | nan | Pantanal | 5.5 |
| 33809189-e457-341e-8422-aa35267c60aa | -17.03197 | -56.79194 | 2024-10-05 05:31:00 | NOAA-21 | POCONÉ | MATO GROSSO | Brasil | 5106505 | 51 | 33 | nan | nan | nan | Pantanal | 7.6 |
| c5a9f259-423a-3ebf-a412-27a1e41c94b6 | -17.03134 | -56.79731 | 2024-10-05 05:31:00 | NOAA-21 | POCONÉ | MATO GROSSO | Brasil | 5106505 | 51 | 33 | nan | nan | nan | Pantanal | 7.6 |
| 2a9ee27c-8191-3f99-aca2-33d6058e03e4 | -17.02808 | -56.7422 | 2024-10-05 05:31:00 | NOAA-21 | POCONÉ | MATO GROSSO | Brasil | 5106505 | 51 | 33 | nan | nan | nan | Pantanal | 5.5 |
| a754f940-2950-38f9-a78b-c909d8df6f87 | -17.02719 | -56.7913 | 2024-10-05 05:31:00 | NOAA-21 | POCONÉ | MATO GROSSO | Brasil | 5106505 | 51 | 33 | nan | nan | nan | Pantanal | 15.9 |
| f417f9f4-fc96-31da-a25e-c021a55ed8cb | -17.02656 | -56.79667 | 2024-10-05 05:31:00 | NOAA-21 | POCONÉ | MATO GROSSO | Brasil | 5106505 | 51 | 33 | nan | nan | nan | Pantanal | 15.9 |
| 182d466e-3a78-35c2-9ff9-552efae38807 | -17.02391 | -56.73614 | 2024-10-05 05:31:00 | NOAA-21 | POCONÉ | MATO GROSSO | Brasil | 5106505 | 51 | 33 | nan | nan | nan | Pantanal | 8.9 |
| bec165e6-5c03-37a3-90d5-826b52f18898 | -17.02328 | -56.74155 | 2024-10-05 05:31:00 | NOAA-21 | POCONÉ | MATO GROSSO | Brasil | 5106505 | 51 | 33 | nan | nan | nan | Pantanal | 8.9 |
| ae6a4e97-83c6-38d3-9939-8626af4ef6b4 | -17.02241 | -56.79066 | 2024-10-05 05:31:00 | NOAA-21 | POCONÉ | MATO GROSSO | Brasil | 5106505 | 51 | 33 | nan | nan | nan | Pantanal | 15.9 |
| 70c295ad-761c-3fbd-827e-bbbe4b331b4b | -17.02178 | -56.79602 | 2024-10-05 05:31:00 | NOAA-21 | POCONÉ | MATO GROSSO | Brasil | 5106505 | 51 | 33 | nan | nan | nan | Pantanal | 15.9 |
| a4cf3fde-efaf-3dd5-9f7d-bfd8e5648589 | -17.01912 | -56.7355 | 2024-10-05 05:31:00 | NOAA-21 | POCONÉ | MATO GROSSO | Brasil | 5106505 | 51 | 33 | nan | nan | nan | Pantanal | 8.9 |
| 9914ab43-72e9-3f4c-b4d4-21703a8d835b | -17.01763 | -56.79002 | 2024-10-05 05:31:00 | NOAA-21 | POCONÉ | MATO GROSSO | Brasil | 5106505 | 51 | 33 | nan | nan | nan | Pantanal | 17.0 |
| 5dd04809-c7d8-33a5-a5d1-458e30cab956 | -17.017 | -56.79539 | 2024-10-05 05:31:00 | NOAA-21 | POCONÉ | MATO GROSSO | Brasil | 5106505 | 51 | 33 | nan | nan | nan | Pantanal | 17.0 |
| 1d76aca5-ab66-3ca6-a670-400d499830f9 | -17.01285 | -56.78938 | 2024-10-05 05:31:00 | NOAA-21 | POCONÉ | MATO GROSSO | Brasil | 5106505 | 51 | 33 | nan | nan | nan | Pantanal | 17.0 |
| aae2914f-ba8d-3be3-bde4-355a3e1444a5 | -17.01222 | -56.79475 | 2024-10-05 05:31:00 | NOAA-21 | POCONÉ | MATO GROSSO | Brasil | 5106505 | 51 | 33 | nan | nan | nan | Pantanal | 17.0 |
| d12172f5-839d-353b-8d78-05a5c09346d5 | -17.0089 | -56.73963 | 2024-10-05 05:31:00 | NOAA-21 | POCONÉ | MATO GROSSO | Brasil | 5106505 | 51 | 33 | nan | nan | nan | Pantanal | 7.4 |
| 748162cc-cd0e-311d-ad18-888916d06dd8 | -17.00807 | -56.78875 | 2024-10-05 05:31:00 | NOAA-21 | POCONÉ | MATO GROSSO | Brasil | 5106505 | 51 | 33 | nan | nan | nan | Pantanal | 13.9 |
| 54415fd2-1b6d-3c90-8d51-3bafc86cb0fd | -17.0041 | -56.73898 | 2024-10-05 05:31:00 | NOAA-21 | POCONÉ | MATO GROSSO | Brasil | 5106505 | 51 | 33 | nan | nan | nan | Pantanal | 6.2 |
| db910c12-8c5d-3bd2-872e-6a72c1a1418e | -17.00329 | -56.7881 | 2024-10-05 05:31:00 | NOAA-21 | POCONÉ | MATO GROSSO | Brasil | 5106505 | 51 | 33 | nan | nan | nan | Pantanal | 13.9 |
| 578af79d-6965-3c9a-83f6-d1399bddaa77 | -17.00267 | -56.79347 | 2024-10-05 05:31:00 | NOAA-21 | POCONÉ | MATO GROSSO | Brasil | 5106505 | 51 | 33 | nan | nan | nan | Pantanal | 13.9 |
| cfd0fa8b-9375-3fa3-95a3-73d7d4ea10c4 | -16.99913 | -56.78209 | 2024-10-05 05:31:00 | NOAA-21 | POCONÉ | MATO GROSSO | Brasil | 5106505 | 51 | 33 | nan | nan | nan | Pantanal | 3.3 |
| c40e40a5-03f2-3c40-9dc8-cde84b22d113 | -16.99851 | -56.78745 | 2024-10-05 05:31:00 | NOAA-21 | POCONÉ | MATO GROSSO | Brasil | 5106505 | 51 | 33 | nan | nan | nan | Pantanal | 20.4 |
| fd9c9eb6-3a39-3ed9-b987-5cabd224793e | -16.99789 | -56.79283 | 2024-10-05 05:31:00 | NOAA-21 | POCONÉ | MATO GROSSO | Brasil | 5106505 | 51 | 33 | nan | nan | nan | Pantanal | 20.4 |
| 6b185a1c-80db-343d-9f63-e3c08b7232a7 | -16.9962 | -56.76532 | 2024-10-05 05:31:00 | NOAA-21 | POCONÉ | MATO GROSSO | Brasil | 5106505 | 51 | 33 | nan | nan | nan | Pantanal | 6.4 |
| af09db57-51de-36d4-a1e1-401906d90938 | -16.99463 | -56.73599 | 2024-10-05 05:31:00 | NOAA-21 | POCONÉ | MATO GROSSO | Brasil | 5106505 | 51 | 33 | nan | nan | nan | Pantanal | 9.4 |
| e1f877ab-53c5-3a7d-b3e6-edfd047e08bc | -16.99451 | -56.73767 | 2024-10-05 05:31:00 | NOAA-21 | POCONÉ | MATO GROSSO | Brasil | 5106505 | 51 | 33 | nan | nan | nan | Pantanal | 8.7 |
| 37331b78-3586-3839-a393-d255463eb766 | -16.99435 | -56.78144 | 2024-10-05 05:31:00 | NOAA-21 | POCONÉ | MATO GROSSO | Brasil | 5106505 | 51 | 33 | nan | nan | nan | Pantanal | 3.3 |
| 0b78df18-1f5f-344a-b0ef-2fb68ceb3de1 | -16.99373 | -56.78681 | 2024-10-05 05:31:00 | NOAA-21 | POCONÉ | MATO GROSSO | Brasil | 5106505 | 51 | 33 | nan | nan | nan | Pantanal | 20.4 |
| 1d94bd94-a33c-3585-bc82-4e3e82dc83ef | -16.99311 | -56.79217 | 2024-10-05 05:31:00 | NOAA-21 | POCONÉ | MATO GROSSO | Brasil | 5106505 | 51 | 33 | nan | nan | nan | Pantanal | 20.4 |
| c12821c7-cc00-3520-842e-51fe7f396994 | -16.99203 | -56.75929 | 2024-10-05 05:31:00 | NOAA-21 | POCONÉ | MATO GROSSO | Brasil | 5106505 | 51 | 33 | nan | nan | nan | Pantanal | 7.5 |
| c3b5cb2a-4d97-3869-8466-cb410c6ea7e2 | -16.99142 | -56.76467 | 2024-10-05 05:31:00 | NOAA-21 | POCONÉ | MATO GROSSO | Brasil | 5106505 | 51 | 33 | nan | nan | nan | Pantanal | 5.6 |
| 0b092ec8-c0b8-387f-9e13-36b2e379fef4 | -16.9908 | -56.77006 | 2024-10-05 05:31:00 | NOAA-21 | POCONÉ | MATO GROSSO | Brasil | 5106505 | 51 | 33 | nan | nan | nan | Pantanal | 5.6 |
| 78dc4a17-bd5a-35ac-b65a-2e280bcc236c | -16.99018 | -56.77543 | 2024-10-05 05:31:00 | NOAA-21 | POCONÉ | MATO GROSSO | Brasil | 5106505 | 51 | 33 | nan | nan | nan | Pantanal | 9.9 |
| 27ece336-8def-3dae-8feb-ee4018e52a97 | -16.99002 | -56.77369 | 2024-10-05 05:31:00 | NOAA-21 | POCONÉ | MATO GROSSO | Brasil | 5106505 | 51 | 33 | nan | nan | nan | Pantanal | 9.0 |
| 2ab38bbb-a7f8-3498-ada6-2e6df7e95900 | -16.98957 | -56.7808 | 2024-10-05 05:31:00 | NOAA-21 | POCONÉ | MATO GROSSO | Brasil | 5106505 | 51 | 33 | nan | nan | nan | Pantanal | 9.9 |


[Clique aqui para ver as próximas entradas](README143.md)
