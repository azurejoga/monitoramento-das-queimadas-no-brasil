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

## Dados Diários - Página 101

| ID | Latitude | Longitude | Data/Hora GMT | Satélite | Município | Estado | País | Município ID | Estado ID | País ID | Dias sem Chuva | Precipitação | Risco de Fogo | Bioma | FRP |
|----|----------|-----------|---------------|----------|-----------|--------|------|--------------|-----------|---------|----------------|--------------|----------------|-------|-----|
| 533b4d83-3316-3592-b763-dc9baccfe1ae | -3.158 | -50.59624 | 2024-10-29 05:25:00 | NOAA-20 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 3.1 |
| e7fcb558-9d0d-31c3-bf7a-9597ca9b7fd0 | -3.15202 | -50.59538 | 2024-10-29 05:25:00 | NOAA-20 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 3.1 |
| c65bfe5e-ddf0-38e8-b03c-7a41a72d7b35 | -3.91201 | -51.19963 | 2024-10-29 05:25:00 | NOAA-20 | PACAJÁ | PARÁ | Brasil | 1505486 | 15 | 33 | nan | nan | nan | Amazônia | 1.7 |
| 47f07a93-8178-3f67-b213-56f4b3b9f19a | -3.91142 | -51.2037 | 2024-10-29 05:25:00 | NOAA-20 | PACAJÁ | PARÁ | Brasil | 1505486 | 15 | 33 | nan | nan | nan | Amazônia | 1.5 |
| 6c015541-4649-357b-bc2b-6d3e5530c332 | -3.86252 | -51.70234 | 2024-10-29 05:25:00 | NOAA-20 | SENADOR JOSÉ PORFÍRIO | PARÁ | Brasil | 1507805 | 15 | 33 | nan | nan | nan | Amazônia | 1.1 |
| 09c2b4d6-bc14-3e79-b856-69fca038da7e | -3.85745 | -51.69778 | 2024-10-29 05:25:00 | NOAA-20 | SENADOR JOSÉ PORFÍRIO | PARÁ | Brasil | 1507805 | 15 | 33 | nan | nan | nan | Amazônia | 1.9 |
| 810a5081-9db5-360d-be8b-d3f801ccb2e8 | -3.85689 | -51.7016 | 2024-10-29 05:25:00 | NOAA-20 | SENADOR JOSÉ PORFÍRIO | PARÁ | Brasil | 1507805 | 15 | 33 | nan | nan | nan | Amazônia | 1.1 |
| e7e747be-7501-304b-9b8f-11dccd101f61 | -3.81174 | -51.07638 | 2024-10-29 05:25:00 | NOAA-20 | PACAJÁ | PARÁ | Brasil | 1505486 | 15 | 33 | nan | nan | nan | Amazônia | 2.2 |
| cad23fa7-f923-32d7-8291-dfc5fb529338 | -3.81105 | -51.07767 | 2024-10-29 05:25:00 | NOAA-20 | PACAJÁ | PARÁ | Brasil | 1505486 | 15 | 33 | nan | nan | nan | Amazônia | 2.2 |
| 23195daf-2b73-3c6d-ba06-fa8f833fd2bc | -3.79881 | -50.96248 | 2024-10-29 05:25:00 | NOAA-20 | PACAJÁ | PARÁ | Brasil | 1505486 | 15 | 33 | nan | nan | nan | Amazônia | 0.6 |
| 96dabdb5-073f-3a71-85a1-f923a46f519a | -3.79815 | -50.96697 | 2024-10-29 05:25:00 | NOAA-20 | PACAJÁ | PARÁ | Brasil | 1505486 | 15 | 33 | nan | nan | nan | Amazônia | 0.6 |
| 88efbb33-8e90-385c-9fa7-937a9b252520 | -3.7964 | -52.00095 | 2024-10-29 05:25:00 | NOAA-20 | SENADOR JOSÉ PORFÍRIO | PARÁ | Brasil | 1507805 | 15 | 33 | nan | nan | nan | Amazônia | 0.9 |
| 21b629aa-a3bc-3b21-9ac3-14dbf54b634b | -3.79588 | -52.00452 | 2024-10-29 05:25:00 | NOAA-20 | SENADOR JOSÉ PORFÍRIO | PARÁ | Brasil | 1507805 | 15 | 33 | nan | nan | nan | Amazônia | 0.9 |
| a6b50d60-01a8-3308-9288-0d6c82c8adb6 | -3.69694 | -51.83626 | 2024-10-29 05:25:00 | NOAA-20 | SENADOR JOSÉ PORFÍRIO | PARÁ | Brasil | 1507805 | 15 | 33 | nan | nan | nan | Amazônia | 1.0 |
| 7c8b9509-115a-3792-a4c0-9ae54bc779f3 | -3.69638 | -51.83999 | 2024-10-29 05:25:00 | NOAA-20 | SENADOR JOSÉ PORFÍRIO | PARÁ | Brasil | 1507805 | 15 | 33 | nan | nan | nan | Amazônia | 1.2 |
| d9d41829-adb5-33e4-9762-c5f79878b2fb | -3.6961 | -51.83833 | 2024-10-29 05:25:00 | NOAA-20 | SENADOR JOSÉ PORFÍRIO | PARÁ | Brasil | 1507805 | 15 | 33 | nan | nan | nan | Amazônia | 1.9 |
| 625d3a16-4e34-3c32-a119-4fc0171567dd | -3.69581 | -51.84375 | 2024-10-29 05:25:00 | NOAA-20 | SENADOR JOSÉ PORFÍRIO | PARÁ | Brasil | 1507805 | 15 | 33 | nan | nan | nan | Amazônia | 1.2 |
| 8550d3d9-afd2-35f3-90f9-db2b2886292e | -3.69556 | -51.8421 | 2024-10-29 05:25:00 | NOAA-20 | SENADOR JOSÉ PORFÍRIO | PARÁ | Brasil | 1507805 | 15 | 33 | nan | nan | nan | Amazônia | 1.9 |
| a9a63285-601d-3943-b4f1-9250f9bdfba3 | -3.69502 | -51.84586 | 2024-10-29 05:25:00 | NOAA-20 | SENADOR JOSÉ PORFÍRIO | PARÁ | Brasil | 1507805 | 15 | 33 | nan | nan | nan | Amazônia | 1.7 |
| f767494b-9714-37a1-8d86-024cd626f992 | -3.69394 | -51.85335 | 2024-10-29 05:25:00 | NOAA-20 | SENADOR JOSÉ PORFÍRIO | PARÁ | Brasil | 1507805 | 15 | 33 | nan | nan | nan | Amazônia | 1.6 |
| 3fac1f66-0745-3d26-92fd-09ea7044b78a | -3.69083 | -51.83913 | 2024-10-29 05:25:00 | NOAA-20 | SENADOR JOSÉ PORFÍRIO | PARÁ | Brasil | 1507805 | 15 | 33 | nan | nan | nan | Amazônia | 1.2 |
| 2cdd0013-e389-314a-9d7e-55c4555fe5d0 | -3.69056 | -51.83748 | 2024-10-29 05:25:00 | NOAA-20 | SENADOR JOSÉ PORFÍRIO | PARÁ | Brasil | 1507805 | 15 | 33 | nan | nan | nan | Amazônia | 1.0 |
| 90fbb52a-2899-3422-b6fb-e67f029859cd | -3.69027 | -51.84287 | 2024-10-29 05:25:00 | NOAA-20 | SENADOR JOSÉ PORFÍRIO | PARÁ | Brasil | 1507805 | 15 | 33 | nan | nan | nan | Amazônia | 1.2 |
| 7df10ace-af0d-3e3f-a515-fa53efd6f145 | -3.69002 | -51.84121 | 2024-10-29 05:25:00 | NOAA-20 | SENADOR JOSÉ PORFÍRIO | PARÁ | Brasil | 1507805 | 15 | 33 | nan | nan | nan | Amazônia | 1.0 |
| f97a3734-14e3-3dda-affd-1049b890c2b9 | -3.68971 | -51.84661 | 2024-10-29 05:25:00 | NOAA-20 | SENADOR JOSÉ PORFÍRIO | PARÁ | Brasil | 1507805 | 15 | 33 | nan | nan | nan | Amazônia | 2.2 |
| 10465bd1-75e3-3361-8678-fb4d8addcd69 | -3.68948 | -51.84496 | 2024-10-29 05:25:00 | NOAA-20 | SENADOR JOSÉ PORFÍRIO | PARÁ | Brasil | 1507805 | 15 | 33 | nan | nan | nan | Amazônia | 3.0 |
| 28d08f71-d8e4-31a8-afb9-ebf0c63a27d0 | -3.68913 | -51.8504 | 2024-10-29 05:25:00 | NOAA-20 | SENADOR JOSÉ PORFÍRIO | PARÁ | Brasil | 1507805 | 15 | 33 | nan | nan | nan | Amazônia | 2.2 |
| c08c0989-5f10-3b04-8194-8eef1440ea39 | -3.68856 | -51.85417 | 2024-10-29 05:25:00 | NOAA-20 | SENADOR JOSÉ PORFÍRIO | PARÁ | Brasil | 1507805 | 15 | 33 | nan | nan | nan | Amazônia | 3.1 |
| 22861af7-c748-31c1-916c-9b0a344e980c | -3.6884 | -51.85255 | 2024-10-29 05:25:00 | NOAA-20 | SENADOR JOSÉ PORFÍRIO | PARÁ | Brasil | 1507805 | 15 | 33 | nan | nan | nan | Amazônia | 3.1 |
| 2e41f704-4e91-389a-8ef4-7821d2908d15 | -3.68802 | -51.85777 | 2024-10-29 05:25:00 | NOAA-20 | SENADOR JOSÉ PORFÍRIO | PARÁ | Brasil | 1507805 | 15 | 33 | nan | nan | nan | Amazônia | 3.1 |
| 9ed68207-b0b5-392f-b9f4-b34448ff97a6 | -3.68787 | -51.85622 | 2024-10-29 05:25:00 | NOAA-20 | SENADOR JOSÉ PORFÍRIO | PARÁ | Brasil | 1507805 | 15 | 33 | nan | nan | nan | Amazônia | 3.1 |
| 821bd1b6-004b-38cc-97b6-4636aa02fffe | -3.67206 | -51.38237 | 2024-10-29 05:25:00 | NOAA-20 | ANAPU | PARÁ | Brasil | 1500859 | 15 | 33 | nan | nan | nan | Amazônia | 1.5 |
| 57debb0e-1a17-3f32-8a2e-3e50176cb74e | -3.67149 | -51.38628 | 2024-10-29 05:25:00 | NOAA-20 | ANAPU | PARÁ | Brasil | 1500859 | 15 | 33 | nan | nan | nan | Amazônia | 2.1 |
| 4f8cee01-a50a-30ac-90ca-f7857197df26 | -3.66631 | -51.38174 | 2024-10-29 05:25:00 | NOAA-20 | ANAPU | PARÁ | Brasil | 1500859 | 15 | 33 | nan | nan | nan | Amazônia | 1.5 |
| ad2ba6c4-abb6-331e-934b-47e20b33a81c | 2.62395 | -50.91961 | 2024-10-29 05:25:00 | NOAA-20 | CALÇOENE | AMAPÁ | Brasil | 1600204 | 16 | 33 | nan | nan | nan | Amazônia | 0.6 |
| 3bc65bcf-be4a-353b-8a1f-3a7997c6fcc2 | 2.6203 | -50.91774 | 2024-10-29 05:25:00 | NOAA-20 | CALÇOENE | AMAPÁ | Brasil | 1600204 | 16 | 33 | nan | nan | nan | Amazônia | 1.5 |
| 9b70c79d-6a46-33db-827f-f2b16a336de9 | 2.6186 | -50.92049 | 2024-10-29 05:25:00 | NOAA-20 | CALÇOENE | AMAPÁ | Brasil | 1600204 | 16 | 33 | nan | nan | nan | Amazônia | 1.7 |
| a766bb25-739c-36ed-b926-a1ec8e009501 | -2.23099 | -52.22916 | 2024-10-29 05:25:00 | NOAA-20 | PORTO DE MOZ | PARÁ | Brasil | 1505908 | 15 | 33 | nan | nan | nan | Amazônia | 2.7 |
| 33982d6d-d3d7-3db5-a9e0-c7a727aafa18 | -2.23049 | -52.23242 | 2024-10-29 05:25:00 | NOAA-20 | PORTO DE MOZ | PARÁ | Brasil | 1505908 | 15 | 33 | nan | nan | nan | Amazônia | 2.7 |
| ea5e7387-3506-3015-95e9-42e6713c19df | -2.23 | -52.22919 | 2024-10-29 05:25:00 | NOAA-20 | PORTO DE MOZ | PARÁ | Brasil | 1505908 | 15 | 33 | nan | nan | nan | Amazônia | 2.6 |
| 730fd56e-fc3d-3cf5-9b44-3b9b6e19a234 | -2.22952 | -52.23245 | 2024-10-29 05:25:00 | NOAA-20 | PORTO DE MOZ | PARÁ | Brasil | 1505908 | 15 | 33 | nan | nan | nan | Amazônia | 2.6 |
| 288c29cc-872b-3c29-b4a4-a30e77786bab | -2.06098 | -52.14166 | 2024-10-29 05:25:00 | NOAA-20 | PORTO DE MOZ | PARÁ | Brasil | 1505908 | 15 | 33 | nan | nan | nan | Amazônia | 1.2 |
| b7e8e662-4981-3156-a904-dff606499222 | -2.06049 | -52.14495 | 2024-10-29 05:25:00 | NOAA-20 | PORTO DE MOZ | PARÁ | Brasil | 1505908 | 15 | 33 | nan | nan | nan | Amazônia | 1.2 |
| 0f963ca4-ebf0-3906-b224-a5198cbd72dd | -2.04476 | -52.08035 | 2024-10-29 05:25:00 | NOAA-20 | PORTO DE MOZ | PARÁ | Brasil | 1505908 | 15 | 33 | nan | nan | nan | Amazônia | 1.9 |
| eb93f02a-d580-318d-9bce-12db19a8a867 | -2.04373 | -52.08696 | 2024-10-29 05:25:00 | NOAA-20 | PORTO DE MOZ | PARÁ | Brasil | 1505908 | 15 | 33 | nan | nan | nan | Amazônia | 0.9 |
| 81fc65f4-534c-3956-908d-d215b40b8477 | -2.04322 | -52.09023 | 2024-10-29 05:25:00 | NOAA-20 | PORTO DE MOZ | PARÁ | Brasil | 1505908 | 15 | 33 | nan | nan | nan | Amazônia | 0.9 |
| f082a21b-b8c8-34c6-8854-6e608491eca2 | -2.04321 | -52.07854 | 2024-10-29 05:25:00 | NOAA-20 | PORTO DE MOZ | PARÁ | Brasil | 1505908 | 15 | 33 | nan | nan | nan | Amazônia | 2.1 |
| 37e734d0-d0ef-31ef-a419-947cfd9f2d2a | -2.04223 | -52.08519 | 2024-10-29 05:25:00 | NOAA-20 | PORTO DE MOZ | PARÁ | Brasil | 1505908 | 15 | 33 | nan | nan | nan | Amazônia | 1.0 |
| 91bb1756-6ffb-3066-91ac-687090e7d602 | -2.04174 | -52.08849 | 2024-10-29 05:25:00 | NOAA-20 | PORTO DE MOZ | PARÁ | Brasil | 1505908 | 15 | 33 | nan | nan | nan | Amazônia | 1.0 |
| cd037ba9-9d80-32ec-a984-f51a70be8700 | -1.97935 | -52.08065 | 2024-10-29 05:25:00 | NOAA-20 | PORTO DE MOZ | PARÁ | Brasil | 1505908 | 15 | 33 | nan | nan | nan | Amazônia | 2.0 |
| 05aef8fc-3c7b-3a98-a3d6-7441bf51e2ff | -1.97885 | -52.08397 | 2024-10-29 05:25:00 | NOAA-20 | PORTO DE MOZ | PARÁ | Brasil | 1505908 | 15 | 33 | nan | nan | nan | Amazônia | 1.7 |
| f3d21daf-3faf-3b9b-b5a5-af4f2e5e6641 | -1.97834 | -52.08729 | 2024-10-29 05:25:00 | NOAA-20 | PORTO DE MOZ | PARÁ | Brasil | 1505908 | 15 | 33 | nan | nan | nan | Amazônia | 1.7 |
| 0b159d5e-f3b8-3531-a669-62a753e9e1fe | -1.9242 | -52.12862 | 2024-10-29 05:25:00 | NOAA-20 | PORTO DE MOZ | PARÁ | Brasil | 1505908 | 15 | 33 | nan | nan | nan | Amazônia | 0.8 |
| 958fcc67-8dc2-32f4-b9c0-8e27d6476ac8 | -1.9237 | -52.13188 | 2024-10-29 05:25:00 | NOAA-20 | PORTO DE MOZ | PARÁ | Brasil | 1505908 | 15 | 33 | nan | nan | nan | Amazônia | 0.8 |
| 6d2c144e-f59f-3407-8d84-d3ce5356954e | -1.92314 | -52.1295 | 2024-10-29 05:25:00 | NOAA-20 | PORTO DE MOZ | PARÁ | Brasil | 1505908 | 15 | 33 | nan | nan | nan | Amazônia | 1.1 |
| 741b5a8f-0a58-3722-85e1-c6d51e98a442 | -1.92266 | -52.13276 | 2024-10-29 05:25:00 | NOAA-20 | PORTO DE MOZ | PARÁ | Brasil | 1505908 | 15 | 33 | nan | nan | nan | Amazônia | 1.1 |
| 6389e699-30c4-35fc-a501-eec9946e69e8 | -1.91959 | -52.05345 | 2024-10-29 05:25:00 | NOAA-20 | PORTO DE MOZ | PARÁ | Brasil | 1505908 | 15 | 33 | nan | nan | nan | Amazônia | 0.5 |
| 7bd0473a-d0ff-3010-b9ab-279b002e72a5 | -1.91907 | -52.0568 | 2024-10-29 05:25:00 | NOAA-20 | PORTO DE MOZ | PARÁ | Brasil | 1505908 | 15 | 33 | nan | nan | nan | Amazônia | 0.5 |
| 390b8992-256f-3cfc-968d-15169481aed3 | -1.91891 | -52.1278 | 2024-10-29 05:25:00 | NOAA-20 | PORTO DE MOZ | PARÁ | Brasil | 1505908 | 15 | 33 | nan | nan | nan | Amazônia | 0.8 |
| c5811fd5-0bc2-3c5d-9d62-afefc28157f6 | -1.75562 | -52.06891 | 2024-10-29 05:25:00 | NOAA-20 | PORTO DE MOZ | PARÁ | Brasil | 1505908 | 15 | 33 | nan | nan | nan | Amazônia | 1.8 |
| 3cdae405-06d1-3ed6-97b6-d2295d20a019 | -1.75073 | -52.31264 | 2024-10-29 05:25:00 | NOAA-20 | PORTO DE MOZ | PARÁ | Brasil | 1505908 | 15 | 33 | nan | nan | nan | Amazônia | 1.8 |
| 4c6f2283-5a5c-394a-90c7-39f1503d33ee | -1.89473 | -53.00861 | 2024-10-29 05:25:00 | NOAA-20 | PORTO DE MOZ | PARÁ | Brasil | 1505908 | 15 | 33 | nan | nan | nan | Amazônia | 2.1 |
| 9db99d17-45ee-3c0b-b2db-c02889bdde69 | -1.68486 | -52.74025 | 2024-10-29 05:25:00 | NOAA-20 | PORTO DE MOZ | PARÁ | Brasil | 1505908 | 15 | 33 | nan | nan | nan | Amazônia | 0.8 |
| 672bbbea-d923-3d95-965d-714fd499db16 | -1.68441 | -52.7432 | 2024-10-29 05:25:00 | NOAA-20 | PORTO DE MOZ | PARÁ | Brasil | 1505908 | 15 | 33 | nan | nan | nan | Amazônia | 0.8 |
| 4ba6d39f-174c-34f5-af36-9c45f6e9f213 | -1.65975 | -52.66666 | 2024-10-29 05:25:00 | NOAA-20 | PORTO DE MOZ | PARÁ | Brasil | 1505908 | 15 | 33 | nan | nan | nan | Amazônia | 1.0 |
| f89818c3-ec88-3020-b953-3e1d91892556 | -1.6593 | -52.66965 | 2024-10-29 05:25:00 | NOAA-20 | PORTO DE MOZ | PARÁ | Brasil | 1505908 | 15 | 33 | nan | nan | nan | Amazônia | 1.6 |
| 6781a4ee-88bc-3b3d-b9f3-995d320f6414 | -1.65467 | -52.66588 | 2024-10-29 05:25:00 | NOAA-20 | PORTO DE MOZ | PARÁ | Brasil | 1505908 | 15 | 33 | nan | nan | nan | Amazônia | 1.0 |
| cc1daec5-f90b-370e-b1b9-a620c0d35018 | -1.58989 | -53.19324 | 2024-10-29 05:25:00 | NOAA-20 | ALMEIRIM | PARÁ | Brasil | 1500503 | 15 | 33 | nan | nan | nan | Amazônia | 2.8 |
| b46f6055-6904-3111-9779-af286032be40 | -1.58907 | -53.19865 | 2024-10-29 05:25:00 | NOAA-20 | ALMEIRIM | PARÁ | Brasil | 1500503 | 15 | 33 | nan | nan | nan | Amazônia | 2.8 |
| 44f61dea-167a-3fae-a363-0fa532824b68 | -1.58585 | -53.18682 | 2024-10-29 05:25:00 | NOAA-20 | ALMEIRIM | PARÁ | Brasil | 1500503 | 15 | 33 | nan | nan | nan | Amazônia | 2.4 |
| d8c2f921-a952-3eaf-a55f-245bf79e66d9 | -3.22558 | -52.60764 | 2024-10-29 05:25:00 | NOAA-20 | BRASIL NOVO | PARÁ | Brasil | 1501725 | 15 | 33 | nan | nan | nan | Amazônia | 0.8 |
| 51dbd29a-1060-39db-8644-ece3fe6e620b | -3.22512 | -52.61063 | 2024-10-29 05:25:00 | NOAA-20 | BRASIL NOVO | PARÁ | Brasil | 1501725 | 15 | 33 | nan | nan | nan | Amazônia | 0.8 |
| 7b4949d0-846a-3919-b106-473a4f4e0378 | -3.21988 | -52.60994 | 2024-10-29 05:25:00 | NOAA-20 | BRASIL NOVO | PARÁ | Brasil | 1501725 | 15 | 33 | nan | nan | nan | Amazônia | 0.8 |
| 8b96bfa6-acd3-32db-8314-c9e25592b066 | -3.18419 | -52.88145 | 2024-10-29 05:25:00 | NOAA-20 | MEDICILÂNDIA | PARÁ | Brasil | 1504455 | 15 | 33 | nan | nan | nan | Amazônia | 0.8 |
| 887cb43f-3b59-3407-bd1b-1a001ecc8593 | -3.18373 | -52.88448 | 2024-10-29 05:25:00 | NOAA-20 | MEDICILÂNDIA | PARÁ | Brasil | 1504455 | 15 | 33 | nan | nan | nan | Amazônia | 0.8 |
| 8b49bfbd-93de-3c6e-aa54-c1a23ef98bdd | -3.04257 | -53.03746 | 2024-10-29 05:25:00 | NOAA-20 | MEDICILÂNDIA | PARÁ | Brasil | 1504455 | 15 | 33 | nan | nan | nan | Amazônia | 0.7 |
| e055b2be-eea9-3bae-8fcb-904de2b8044a | -3.04212 | -53.04041 | 2024-10-29 05:25:00 | NOAA-20 | MEDICILÂNDIA | PARÁ | Brasil | 1504455 | 15 | 33 | nan | nan | nan | Amazônia | 0.7 |
| b53d0278-b7a3-3773-b82f-f34ca0ee9bcd | -3.03751 | -53.03663 | 2024-10-29 05:25:00 | NOAA-20 | MEDICILÂNDIA | PARÁ | Brasil | 1504455 | 15 | 33 | nan | nan | nan | Amazônia | 0.7 |
| ba8f281b-cfa7-3a50-9e44-cbedff48da25 | -3.00252 | -53.43557 | 2024-10-29 05:25:00 | NOAA-20 | MEDICILÂNDIA | PARÁ | Brasil | 1504455 | 15 | 33 | nan | nan | nan | Amazônia | 4.1 |
| 09677fd9-2958-3af7-a027-86ca026e3e73 | -3.0017 | -53.44093 | 2024-10-29 05:25:00 | NOAA-20 | MEDICILÂNDIA | PARÁ | Brasil | 1504455 | 15 | 33 | nan | nan | nan | Amazônia | 4.1 |
| 8e4615f2-85aa-39c4-9d04-a61638c8316f | -2.99757 | -53.43499 | 2024-10-29 05:25:00 | NOAA-20 | MEDICILÂNDIA | PARÁ | Brasil | 1504455 | 15 | 33 | nan | nan | nan | Amazônia | 4.1 |
| 4b36ef56-5618-320b-a567-de9b11b8ed60 | -2.99676 | -53.4403 | 2024-10-29 05:25:00 | NOAA-20 | MEDICILÂNDIA | PARÁ | Brasil | 1504455 | 15 | 33 | nan | nan | nan | Amazônia | 4.1 |
| 1d1cc3ea-122a-3cf2-b8c9-6763dde03243 | -2.98235 | -53.26736 | 2024-10-29 05:25:00 | NOAA-20 | MEDICILÂNDIA | PARÁ | Brasil | 1504455 | 15 | 33 | nan | nan | nan | Amazônia | 1.1 |
| 3fa6f038-d4eb-38b2-9bc9-3a5405598068 | -2.98194 | -53.27015 | 2024-10-29 05:25:00 | NOAA-20 | MEDICILÂNDIA | PARÁ | Brasil | 1504455 | 15 | 33 | nan | nan | nan | Amazônia | 0.6 |
| 729724ab-2ca3-31e6-9cec-49d53ff92cc0 | -2.97735 | -53.26674 | 2024-10-29 05:25:00 | NOAA-20 | MEDICILÂNDIA | PARÁ | Brasil | 1504455 | 15 | 33 | nan | nan | nan | Amazônia | 1.0 |
| d071e780-e596-322f-abad-6306ca52c349 | -2.97194 | -53.26889 | 2024-10-29 05:25:00 | NOAA-20 | MEDICILÂNDIA | PARÁ | Brasil | 1504455 | 15 | 33 | nan | nan | nan | Amazônia | 1.3 |
| 831adc3f-a887-3f8a-b400-418d36a95154 | -2.86889 | -53.34169 | 2024-10-29 05:25:00 | NOAA-20 | MEDICILÂNDIA | PARÁ | Brasil | 1504455 | 15 | 33 | nan | nan | nan | Amazônia | 3.1 |
| 9f4a4afd-7b5f-38a0-9ade-9110bc242280 | -2.86805 | -53.34726 | 2024-10-29 05:25:00 | NOAA-20 | MEDICILÂNDIA | PARÁ | Brasil | 1504455 | 15 | 33 | nan | nan | nan | Amazônia | 6.4 |
| 5d02ba04-d3ea-3f98-bc0f-2725f8216a18 | -2.86728 | -53.35243 | 2024-10-29 05:25:00 | NOAA-20 | MEDICILÂNDIA | PARÁ | Brasil | 1504455 | 15 | 33 | nan | nan | nan | Amazônia | 6.4 |
| be1ac523-a2dd-3140-a8d8-632425ec192c | -2.86561 | -53.32984 | 2024-10-29 05:25:00 | NOAA-20 | MEDICILÂNDIA | PARÁ | Brasil | 1504455 | 15 | 33 | nan | nan | nan | Amazônia | 2.7 |
| aa8b96e4-d26d-373f-a882-6de71cf09953 | -2.86475 | -53.33558 | 2024-10-29 05:25:00 | NOAA-20 | MEDICILÂNDIA | PARÁ | Brasil | 1504455 | 15 | 33 | nan | nan | nan | Amazônia | 3.1 |
| a9d02fdc-eff4-3f01-9e0f-7c8010e6bb01 | -2.8639 | -53.34126 | 2024-10-29 05:25:00 | NOAA-20 | MEDICILÂNDIA | PARÁ | Brasil | 1504455 | 15 | 33 | nan | nan | nan | Amazônia | 3.1 |
| a82fcdce-f010-32de-891d-d8b7b79be91c | -2.86307 | -53.34679 | 2024-10-29 05:25:00 | NOAA-20 | MEDICILÂNDIA | PARÁ | Brasil | 1504455 | 15 | 33 | nan | nan | nan | Amazônia | 6.4 |
| d2a1b100-284d-3512-ab8e-f5ad93e5faeb | -2.86231 | -53.35187 | 2024-10-29 05:25:00 | NOAA-20 | MEDICILÂNDIA | PARÁ | Brasil | 1504455 | 15 | 33 | nan | nan | nan | Amazônia | 6.4 |
| 6513bf2f-0a44-36e2-8da8-d1e8efcc298c | -2.86151 | -53.35721 | 2024-10-29 05:25:00 | NOAA-20 | MEDICILÂNDIA | PARÁ | Brasil | 1504455 | 15 | 33 | nan | nan | nan | Amazônia | 5.5 |
| 9151cb34-19ce-3c32-b892-bc89eb3b8ebc | -2.85977 | -53.33501 | 2024-10-29 05:25:00 | NOAA-20 | MEDICILÂNDIA | PARÁ | Brasil | 1504455 | 15 | 33 | nan | nan | nan | Amazônia | 4.9 |
| 54e68b91-9e0d-3566-abfe-a5812707a38f | -2.8581 | -53.34617 | 2024-10-29 05:25:00 | NOAA-20 | MEDICILÂNDIA | PARÁ | Brasil | 1504455 | 15 | 33 | nan | nan | nan | Amazônia | 2.0 |
| 4987bc9d-7a54-36ee-9ba9-7d92479a52c1 | -2.85734 | -53.35126 | 2024-10-29 05:25:00 | NOAA-20 | MEDICILÂNDIA | PARÁ | Brasil | 1504455 | 15 | 33 | nan | nan | nan | Amazônia | 2.0 |
| 11a70ee6-4dab-37f9-9312-476792280fdc | -2.85656 | -53.35649 | 2024-10-29 05:25:00 | NOAA-20 | MEDICILÂNDIA | PARÁ | Brasil | 1504455 | 15 | 33 | nan | nan | nan | Amazônia | 1.1 |
| 6e7ecf2f-d761-3956-9ea7-b93a841188b8 | -2.85315 | -53.34548 | 2024-10-29 05:25:00 | NOAA-20 | MEDICILÂNDIA | PARÁ | Brasil | 1504455 | 15 | 33 | nan | nan | nan | Amazônia | 2.0 |


[Clique aqui para ver as próximas entradas](README102.md)
