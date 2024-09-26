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

## Dados Diários - Página 76

| ID | Latitude | Longitude | Data/Hora GMT | Satélite | Município | Estado | País | Município ID | Estado ID | País ID | Dias sem Chuva | Precipitação | Risco de Fogo | Bioma | FRP |
|----|----------|-----------|---------------|----------|-----------|--------|------|--------------|-----------|---------|----------------|--------------|----------------|-------|-----|
| 810c4805-2a88-3873-8f34-a5c67aee7a5f | -12.66913 | -50.94751 | 2024-09-26 04:08:00 | NOAA-20 | RIBEIRÃO CASCALHEIRA | MATO GROSSO | Brasil | 5107180 | 51 | 33 | nan | nan | nan | Cerrado | 2.0 |
| bdc39fc6-2643-3a7e-b2d0-f5c9a334e503 | -12.62717 | -50.92743 | 2024-09-26 04:08:00 | NOAA-20 | RIBEIRÃO CASCALHEIRA | MATO GROSSO | Brasil | 5107180 | 51 | 33 | nan | nan | nan | Cerrado | 10.4 |
| 14e9559c-67cf-3dec-b97c-8cf02b24ea92 | -12.62611 | -50.93304 | 2024-09-26 04:08:00 | NOAA-20 | RIBEIRÃO CASCALHEIRA | MATO GROSSO | Brasil | 5107180 | 51 | 33 | nan | nan | nan | Cerrado | 8.3 |
| 8ced6300-cc8a-3223-8499-d6810682de69 | -12.62121 | -50.93207 | 2024-09-26 04:08:00 | NOAA-20 | RIBEIRÃO CASCALHEIRA | MATO GROSSO | Brasil | 5107180 | 51 | 33 | nan | nan | nan | Cerrado | 1.8 |
| 14eaaa05-efce-3c48-a7ae-c43993e414b2 | -12.49252 | -50.43608 | 2024-09-26 04:08:00 | NOAA-20 | FORMOSO DO ARAGUAIA | TOCANTINS | Brasil | 1708205 | 17 | 33 | nan | nan | nan | Cerrado | 2.3 |
| 2a1a3de4-bff1-3d8b-8010-47d0b492c458 | -12.49071 | -50.41949 | 2024-09-26 04:08:00 | NOAA-20 | FORMOSO DO ARAGUAIA | TOCANTINS | Brasil | 1708205 | 17 | 33 | nan | nan | nan | Cerrado | 1.8 |
| df3d9a60-f4d8-3323-a552-00e12ffd3f96 | -12.48973 | -50.42471 | 2024-09-26 04:08:00 | NOAA-20 | FORMOSO DO ARAGUAIA | TOCANTINS | Brasil | 1708205 | 17 | 33 | nan | nan | nan | Cerrado | 1.8 |
| a60a5e39-562f-3a05-a376-735453b193ab | -12.48876 | -50.42993 | 2024-09-26 04:08:00 | NOAA-20 | FORMOSO DO ARAGUAIA | TOCANTINS | Brasil | 1708205 | 17 | 33 | nan | nan | nan | Cerrado | 2.0 |
| c7490f6e-ff86-3535-be28-dd990890faff | -12.29533 | -50.51542 | 2024-09-26 04:08:00 | NOAA-20 | FORMOSO DO ARAGUAIA | TOCANTINS | Brasil | 1708205 | 17 | 33 | nan | nan | nan | Cerrado | 3.2 |
| c2c08344-44c7-31a9-90d0-0c41b3cc3e02 | -12.28955 | -50.51982 | 2024-09-26 04:08:00 | NOAA-20 | FORMOSO DO ARAGUAIA | TOCANTINS | Brasil | 1708205 | 17 | 33 | nan | nan | nan | Cerrado | 2.9 |
| 04d98874-3638-30d3-b6f7-5c26801fd5cf | -12.28856 | -50.52517 | 2024-09-26 04:08:00 | NOAA-20 | FORMOSO DO ARAGUAIA | TOCANTINS | Brasil | 1708205 | 17 | 33 | nan | nan | nan | Cerrado | 2.9 |
| 86c56a51-304b-3ac6-959a-327b6e54b80c | -12.28757 | -50.53052 | 2024-09-26 04:08:00 | NOAA-20 | FORMOSO DO ARAGUAIA | TOCANTINS | Brasil | 1708205 | 17 | 33 | nan | nan | nan | Cerrado | 1.6 |
| 15cb4c2c-da0b-3228-80ef-93a35704f173 | -12.28658 | -50.53587 | 2024-09-26 04:08:00 | NOAA-20 | FORMOSO DO ARAGUAIA | TOCANTINS | Brasil | 1708205 | 17 | 33 | nan | nan | nan | Cerrado | 1.6 |
| af02315c-3cff-3d8e-acce-292d17a5735c | -12.27238 | -50.63941 | 2024-09-26 04:08:00 | NOAA-20 | NOVO SANTO ANTÔNIO | MATO GROSSO | Brasil | 5106315 | 51 | 33 | nan | nan | nan | Cerrado | 2.9 |
| c7e14e7f-ce6f-349d-8c26-8eeb68f7abd5 | -12.21439 | -50.78807 | 2024-09-26 04:08:00 | NOAA-20 | NOVO SANTO ANTÔNIO | MATO GROSSO | Brasil | 5106315 | 51 | 33 | nan | nan | nan | Cerrado | 2.0 |
| 9e2c65c6-7219-35f5-93db-04d3a2ca6d4c | -12.21333 | -50.79366 | 2024-09-26 04:08:00 | NOAA-20 | NOVO SANTO ANTÔNIO | MATO GROSSO | Brasil | 5106315 | 51 | 33 | nan | nan | nan | Cerrado | 2.0 |
| f6f24917-add6-32bb-8091-2d840eb045eb | -12.2095 | -50.7871 | 2024-09-26 04:08:00 | NOAA-20 | NOVO SANTO ANTÔNIO | MATO GROSSO | Brasil | 5106315 | 51 | 33 | nan | nan | nan | Cerrado | 2.0 |
| dc041e0e-6f8b-3a08-ad84-bde152651d29 | -12.20739 | -50.79828 | 2024-09-26 04:08:00 | NOAA-20 | NOVO SANTO ANTÔNIO | MATO GROSSO | Brasil | 5106315 | 51 | 33 | nan | nan | nan | Cerrado | 2.8 |
| 6ca32493-aee7-37b9-958f-436d12ad7447 | -14.87245 | -51.08777 | 2024-09-26 04:08:00 | NOAA-20 | ARUANÃ | GOIÁS | Brasil | 5202502 | 52 | 33 | nan | nan | nan | Cerrado | 1.9 |
| 63496aae-e15e-33ca-a1bb-586866a3d232 | -14.88815 | -51.48909 | 2024-09-26 04:08:00 | NOAA-20 | COCALINHO | MATO GROSSO | Brasil | 5103106 | 51 | 33 | nan | nan | nan | Cerrado | 46.8 |
| a3b9f445-257d-3165-9ce5-bf2b038e0e71 | -14.88705 | -51.49471 | 2024-09-26 04:08:00 | NOAA-20 | COCALINHO | MATO GROSSO | Brasil | 5103106 | 51 | 33 | nan | nan | nan | Cerrado | 18.8 |
| 8a677f85-ddd1-3a50-9c17-62373b889e67 | -14.88595 | -51.50033 | 2024-09-26 04:08:00 | NOAA-20 | COCALINHO | MATO GROSSO | Brasil | 5103106 | 51 | 33 | nan | nan | nan | Cerrado | 18.8 |
| e2432739-f7e5-32ec-960b-54adfa2c58cd | -14.88438 | -51.48246 | 2024-09-26 04:08:00 | NOAA-20 | COCALINHO | MATO GROSSO | Brasil | 5103106 | 51 | 33 | nan | nan | nan | Cerrado | 47.8 |
| 64aeeaf7-7df4-3f45-a31d-301c95776555 | -14.88328 | -51.48807 | 2024-09-26 04:08:00 | NOAA-20 | COCALINHO | MATO GROSSO | Brasil | 5103106 | 51 | 33 | nan | nan | nan | Cerrado | 47.8 |
| 699e9f57-d8be-3749-8fa2-8d5af907ec18 | -14.88218 | -51.49369 | 2024-09-26 04:08:00 | NOAA-20 | COCALINHO | MATO GROSSO | Brasil | 5103106 | 51 | 33 | nan | nan | nan | Cerrado | 10.2 |
| 5f286cf7-a414-3220-8f33-eee1bca3a4a1 | -14.88108 | -51.49931 | 2024-09-26 04:08:00 | NOAA-20 | COCALINHO | MATO GROSSO | Brasil | 5103106 | 51 | 33 | nan | nan | nan | Cerrado | 10.2 |
| 9e5dae0c-bca6-36ca-b931-6c5a4b21420f | -14.87997 | -51.50494 | 2024-09-26 04:08:00 | NOAA-20 | COCALINHO | MATO GROSSO | Brasil | 5103106 | 51 | 33 | nan | nan | nan | Cerrado | 6.3 |
| af2ccafd-13ea-3935-9845-4ee25651435c | -14.87951 | -51.48145 | 2024-09-26 04:08:00 | NOAA-20 | COCALINHO | MATO GROSSO | Brasil | 5103106 | 51 | 33 | nan | nan | nan | Cerrado | 47.8 |
| 352a9f41-ecd1-3dc4-b4fd-c5614665760a | -14.87887 | -51.51057 | 2024-09-26 04:08:00 | NOAA-20 | COCALINHO | MATO GROSSO | Brasil | 5103106 | 51 | 33 | nan | nan | nan | Cerrado | 6.3 |
| 9b05fc2f-c7fb-3c06-b9d5-9740f80ea761 | -14.87841 | -51.48706 | 2024-09-26 04:08:00 | NOAA-20 | COCALINHO | MATO GROSSO | Brasil | 5103106 | 51 | 33 | nan | nan | nan | Cerrado | 47.8 |
| 6283ab66-c5db-31cf-977f-bcae978e8c03 | -14.87731 | -51.49267 | 2024-09-26 04:08:00 | NOAA-20 | COCALINHO | MATO GROSSO | Brasil | 5103106 | 51 | 33 | nan | nan | nan | Cerrado | 10.2 |
| 95a06496-a6fc-3512-82be-a82204dc1176 | -14.87664 | -51.48555 | 2024-09-26 04:08:00 | NOAA-20 | COCALINHO | MATO GROSSO | Brasil | 5103106 | 51 | 33 | nan | nan | nan | Cerrado | 56.6 |
| 3f46e75f-7e65-363f-92a9-babeb5b3e404 | -14.8762 | -51.49829 | 2024-09-26 04:08:00 | NOAA-20 | COCALINHO | MATO GROSSO | Brasil | 5103106 | 51 | 33 | nan | nan | nan | Cerrado | 10.2 |
| a857da8c-62ea-3f29-8c16-741da777c41a | -14.87558 | -51.49117 | 2024-09-26 04:08:00 | NOAA-20 | COCALINHO | MATO GROSSO | Brasil | 5103106 | 51 | 33 | nan | nan | nan | Cerrado | 56.6 |
| ea53945c-d36a-371e-b703-8ff70b6d342d | -14.87451 | -51.4968 | 2024-09-26 04:08:00 | NOAA-20 | COCALINHO | MATO GROSSO | Brasil | 5103106 | 51 | 33 | nan | nan | nan | Cerrado | 27.2 |
| 1877c1f0-8043-381d-b8c1-1cc228827bf3 | -14.87399 | -51.50955 | 2024-09-26 04:08:00 | NOAA-20 | COCALINHO | MATO GROSSO | Brasil | 5103106 | 51 | 33 | nan | nan | nan | Cerrado | 6.3 |
| 82fd699b-811f-36f5-b28c-547295168aaf | -14.87353 | -51.48605 | 2024-09-26 04:08:00 | NOAA-20 | COCALINHO | MATO GROSSO | Brasil | 5103106 | 51 | 33 | nan | nan | nan | Cerrado | 33.6 |
| 4767992e-4d1b-3917-b02c-77c5b51e824f | -14.87243 | -51.49166 | 2024-09-26 04:08:00 | NOAA-20 | COCALINHO | MATO GROSSO | Brasil | 5103106 | 51 | 33 | nan | nan | nan | Cerrado | 70.8 |
| aa633897-ff09-3977-82ce-93e918efeaa7 | -14.87238 | -51.50808 | 2024-09-26 04:08:00 | NOAA-20 | COCALINHO | MATO GROSSO | Brasil | 5103106 | 51 | 33 | nan | nan | nan | Cerrado | 6.1 |
| 3c1ac286-7f9c-3889-900e-a3bbccaca771 | -14.87176 | -51.48453 | 2024-09-26 04:08:00 | NOAA-20 | COCALINHO | MATO GROSSO | Brasil | 5103106 | 51 | 33 | nan | nan | nan | Cerrado | 56.6 |
| 973406f4-37e4-3c90-bafd-67098b741a44 | -14.87132 | -51.49728 | 2024-09-26 04:08:00 | NOAA-20 | COCALINHO | MATO GROSSO | Brasil | 5103106 | 51 | 33 | nan | nan | nan | Cerrado | 70.8 |
| bda4ab9c-0432-3c6a-a0fa-69f839d7ec76 | -14.8707 | -51.49015 | 2024-09-26 04:08:00 | NOAA-20 | COCALINHO | MATO GROSSO | Brasil | 5103106 | 51 | 33 | nan | nan | nan | Cerrado | 56.6 |
| bd3a46eb-8e47-365b-b638-3ed3ff361885 | -14.87022 | -51.5029 | 2024-09-26 04:08:00 | NOAA-20 | COCALINHO | MATO GROSSO | Brasil | 5103106 | 51 | 33 | nan | nan | nan | Cerrado | 4.9 |
| 3eb75e78-3ecc-350a-9999-aadf8e27183f | -14.86964 | -51.49577 | 2024-09-26 04:08:00 | NOAA-20 | COCALINHO | MATO GROSSO | Brasil | 5103106 | 51 | 33 | nan | nan | nan | Cerrado | 27.2 |
| b58dbc28-5097-3c96-abe0-d2a92155703a | -14.86911 | -51.50853 | 2024-09-26 04:08:00 | NOAA-20 | COCALINHO | MATO GROSSO | Brasil | 5103106 | 51 | 33 | nan | nan | nan | Cerrado | 4.9 |
| ec487fb1-5de5-3451-993f-664e943d4afe | -14.86866 | -51.48504 | 2024-09-26 04:08:00 | NOAA-20 | COCALINHO | MATO GROSSO | Brasil | 5103106 | 51 | 33 | nan | nan | nan | Cerrado | 33.6 |
| cfdab3c8-999b-3e7d-a9e0-d733ba4007cc | -14.86857 | -51.50141 | 2024-09-26 04:08:00 | NOAA-20 | COCALINHO | MATO GROSSO | Brasil | 5103106 | 51 | 33 | nan | nan | nan | Cerrado | 27.2 |
| ae158693-7e06-3b04-a9f2-370d7b6320cd | -14.86755 | -51.49065 | 2024-09-26 04:08:00 | NOAA-20 | COCALINHO | MATO GROSSO | Brasil | 5103106 | 51 | 33 | nan | nan | nan | Cerrado | 70.8 |
| f91a2ce8-7c25-34f6-9595-45cf6411d8da | -14.86751 | -51.50705 | 2024-09-26 04:08:00 | NOAA-20 | COCALINHO | MATO GROSSO | Brasil | 5103106 | 51 | 33 | nan | nan | nan | Cerrado | 6.1 |
| 1df56a70-7f61-388d-9da0-c657a2e46456 | -14.86689 | -51.4835 | 2024-09-26 04:08:00 | NOAA-20 | COCALINHO | MATO GROSSO | Brasil | 5103106 | 51 | 33 | nan | nan | nan | Cerrado | 2.5 |
| 59f0fb54-4fbc-3498-ba8d-2cc0b7a67b2d | -14.86645 | -51.49627 | 2024-09-26 04:08:00 | NOAA-20 | COCALINHO | MATO GROSSO | Brasil | 5103106 | 51 | 33 | nan | nan | nan | Cerrado | 70.8 |
| c5a5e0c4-7ecf-33c8-89b6-ab4159e42398 | -14.86644 | -51.5127 | 2024-09-26 04:08:00 | NOAA-20 | COCALINHO | MATO GROSSO | Brasil | 5103106 | 51 | 33 | nan | nan | nan | Cerrado | 6.1 |
| fe2eb457-4e92-3221-a065-c8eadb2ea99a | -14.86583 | -51.48912 | 2024-09-26 04:08:00 | NOAA-20 | COCALINHO | MATO GROSSO | Brasil | 5103106 | 51 | 33 | nan | nan | nan | Cerrado | 2.5 |
| fde52578-89ee-3281-b804-2485ea334091 | -14.86534 | -51.50189 | 2024-09-26 04:08:00 | NOAA-20 | COCALINHO | MATO GROSSO | Brasil | 5103106 | 51 | 33 | nan | nan | nan | Cerrado | 4.9 |
| 2124350b-9d25-39c7-9707-d848ced16012 | -14.86476 | -51.49475 | 2024-09-26 04:08:00 | NOAA-20 | COCALINHO | MATO GROSSO | Brasil | 5103106 | 51 | 33 | nan | nan | nan | Cerrado | 46.3 |
| 4ffe56b1-1334-3253-9ef8-516dc6dcaa29 | -14.86423 | -51.50752 | 2024-09-26 04:08:00 | NOAA-20 | COCALINHO | MATO GROSSO | Brasil | 5103106 | 51 | 33 | nan | nan | nan | Cerrado | 4.9 |
| 8b8bfb4b-bd46-3578-a79d-dc526d1580c4 | -14.86379 | -51.48402 | 2024-09-26 04:08:00 | NOAA-20 | COCALINHO | MATO GROSSO | Brasil | 5103106 | 51 | 33 | nan | nan | nan | Cerrado | 0.9 |
| 3cd8a054-be64-3828-a7a1-1ca8a05bbff5 | -14.86369 | -51.50039 | 2024-09-26 04:08:00 | NOAA-20 | COCALINHO | MATO GROSSO | Brasil | 5103106 | 51 | 33 | nan | nan | nan | Cerrado | 46.3 |
| 70f14ea4-030f-3073-8db5-d86fbaab86bf | -14.86312 | -51.51315 | 2024-09-26 04:08:00 | NOAA-20 | COCALINHO | MATO GROSSO | Brasil | 5103106 | 51 | 33 | nan | nan | nan | Cerrado | 6.3 |
| f0d67881-e85d-3530-882d-e394c804ec07 | -14.86268 | -51.48964 | 2024-09-26 04:08:00 | NOAA-20 | COCALINHO | MATO GROSSO | Brasil | 5103106 | 51 | 33 | nan | nan | nan | Cerrado | 24.2 |
| 569bd60b-ab22-3f03-b9fb-025c6e9b69b6 | -14.86262 | -51.50603 | 2024-09-26 04:08:00 | NOAA-20 | COCALINHO | MATO GROSSO | Brasil | 5103106 | 51 | 33 | nan | nan | nan | Cerrado | 4.2 |
| 518870f1-8da5-36b4-9572-c9e6a649546d | -14.86202 | -51.48248 | 2024-09-26 04:08:00 | NOAA-20 | COCALINHO | MATO GROSSO | Brasil | 5103106 | 51 | 33 | nan | nan | nan | Cerrado | 2.5 |
| baa54237-e3f2-35a6-9125-4fea8991680a | -14.86157 | -51.49525 | 2024-09-26 04:08:00 | NOAA-20 | COCALINHO | MATO GROSSO | Brasil | 5103106 | 51 | 33 | nan | nan | nan | Cerrado | 24.2 |
| 17298b12-b267-36a3-b148-fcd6a1bf3372 | -14.86156 | -51.51167 | 2024-09-26 04:08:00 | NOAA-20 | COCALINHO | MATO GROSSO | Brasil | 5103106 | 51 | 33 | nan | nan | nan | Cerrado | 4.2 |
| 4f1031cf-e7b3-3578-bd16-407296e3bc24 | -14.86095 | -51.4881 | 2024-09-26 04:08:00 | NOAA-20 | COCALINHO | MATO GROSSO | Brasil | 5103106 | 51 | 33 | nan | nan | nan | Cerrado | 2.5 |
| 963343f5-0946-3a55-8f2d-e436dcf32573 | -14.86046 | -51.50088 | 2024-09-26 04:08:00 | NOAA-20 | COCALINHO | MATO GROSSO | Brasil | 5103106 | 51 | 33 | nan | nan | nan | Cerrado | 22.5 |
| e2eb7a79-a2ec-3310-b82b-5516bf360992 | -14.85988 | -51.49373 | 2024-09-26 04:08:00 | NOAA-20 | COCALINHO | MATO GROSSO | Brasil | 5103106 | 51 | 33 | nan | nan | nan | Cerrado | 46.3 |
| 769a7565-51d2-3ccb-a0b3-496d04a1e567 | -14.85935 | -51.5065 | 2024-09-26 04:08:00 | NOAA-20 | COCALINHO | MATO GROSSO | Brasil | 5103106 | 51 | 33 | nan | nan | nan | Cerrado | 22.5 |
| 79ce5264-0f50-30e9-b896-e2a784686f28 | -14.85892 | -51.48301 | 2024-09-26 04:08:00 | NOAA-20 | COCALINHO | MATO GROSSO | Brasil | 5103106 | 51 | 33 | nan | nan | nan | Cerrado | 0.9 |
| 7f2635cd-a20c-3202-aa71-d2a0c59047db | -14.85882 | -51.49936 | 2024-09-26 04:08:00 | NOAA-20 | COCALINHO | MATO GROSSO | Brasil | 5103106 | 51 | 33 | nan | nan | nan | Cerrado | 46.3 |
| b575f509-a77e-37c0-b96a-d4926ddd57c4 | -14.85824 | -51.51213 | 2024-09-26 04:08:00 | NOAA-20 | COCALINHO | MATO GROSSO | Brasil | 5103106 | 51 | 33 | nan | nan | nan | Cerrado | 3.9 |
| b5c44459-b070-3be9-b3c8-3057894b67d5 | -14.85774 | -51.505 | 2024-09-26 04:08:00 | NOAA-20 | COCALINHO | MATO GROSSO | Brasil | 5103106 | 51 | 33 | nan | nan | nan | Cerrado | 4.2 |
| da1ecea2-4857-36da-a5fb-c1c21bc7f883 | -14.85667 | -51.51064 | 2024-09-26 04:08:00 | NOAA-20 | COCALINHO | MATO GROSSO | Brasil | 5103106 | 51 | 33 | nan | nan | nan | Cerrado | 4.2 |
| 526f6f0f-905c-321d-83ff-8e62e1a9d45a | -14.85608 | -51.48707 | 2024-09-26 04:08:00 | NOAA-20 | COCALINHO | MATO GROSSO | Brasil | 5103106 | 51 | 33 | nan | nan | nan | Cerrado | 2.8 |
| 7c88d123-e548-3dc2-8209-6a1847aeb38d | -14.85013 | -51.49167 | 2024-09-26 04:08:00 | NOAA-20 | COCALINHO | MATO GROSSO | Brasil | 5103106 | 51 | 33 | nan | nan | nan | Cerrado | 3.5 |
| 63d4e664-bae4-37fa-a535-3c2f198f657e | -13.74199 | -51.09097 | 2024-09-26 04:08:00 | NOAA-20 | COCALINHO | MATO GROSSO | Brasil | 5103106 | 51 | 33 | nan | nan | nan | Cerrado | 1.4 |
| 25947aed-04ab-3a53-bcb7-3fc9f126becf | -13.74126 | -51.06791 | 2024-09-26 04:08:00 | NOAA-20 | COCALINHO | MATO GROSSO | Brasil | 5103106 | 51 | 33 | nan | nan | nan | Cerrado | 1.4 |
| 682a6532-6cfb-348a-82ac-30a167f936bb | -13.74096 | -51.09649 | 2024-09-26 04:08:00 | NOAA-20 | COCALINHO | MATO GROSSO | Brasil | 5103106 | 51 | 33 | nan | nan | nan | Cerrado | 1.4 |
| da538be0-7c1b-339f-a1d7-d30e0a02dbfc | -13.7392 | -51.07893 | 2024-09-26 04:08:00 | NOAA-20 | COCALINHO | MATO GROSSO | Brasil | 5103106 | 51 | 33 | nan | nan | nan | Cerrado | 1.5 |
| ce91dce7-0654-346a-9e2d-19dea4c3369d | -13.71947 | -51.10362 | 2024-09-26 04:08:00 | NOAA-20 | COCALINHO | MATO GROSSO | Brasil | 5103106 | 51 | 33 | nan | nan | nan | Cerrado | 2.1 |
| a7c43d7d-9449-38d4-a2cd-6e30accd142b | -13.74441 | -51.09355 | 2024-09-26 04:08:00 | NOAA-20 | COCALINHO | MATO GROSSO | Brasil | 5103106 | 51 | 33 | nan | nan | nan | Cerrado | 2.4 |
| 63db8193-f7a7-347c-9336-193e7824f3e9 | -13.74023 | -51.07342 | 2024-09-26 04:08:00 | NOAA-20 | COCALINHO | MATO GROSSO | Brasil | 5103106 | 51 | 33 | nan | nan | nan | Cerrado | 1.4 |
| f805cf9f-715e-34d9-827a-86a611b350bb | -16.66784 | -50.59888 | 2024-09-26 04:08:00 | NOAA-20 | AURILÂNDIA | GOIÁS | Brasil | 5202601 | 52 | 33 | nan | nan | nan | Cerrado | 2.4 |
| 01694d35-982a-3eed-987b-2aff7f7cd76b | -12.83753 | -51.17985 | 2024-09-26 04:08:00 | NOAA-20 | RIBEIRÃO CASCALHEIRA | MATO GROSSO | Brasil | 5107180 | 51 | 33 | nan | nan | nan | Cerrado | 5.7 |
| dd9db641-6de1-38a2-bbdb-283b0fe7b9ca | -12.83644 | -51.18563 | 2024-09-26 04:08:00 | NOAA-20 | RIBEIRÃO CASCALHEIRA | MATO GROSSO | Brasil | 5107180 | 51 | 33 | nan | nan | nan | Cerrado | 5.7 |
| 7fc15751-3fb2-3f30-b046-b8fbb4802aba | -12.83535 | -51.19144 | 2024-09-26 04:08:00 | NOAA-20 | RIBEIRÃO CASCALHEIRA | MATO GROSSO | Brasil | 5107180 | 51 | 33 | nan | nan | nan | Cerrado | 3.9 |
| 6decf493-ab88-3f9e-bfd7-354e3b646664 | -12.83427 | -51.19725 | 2024-09-26 04:08:00 | NOAA-20 | RIBEIRÃO CASCALHEIRA | MATO GROSSO | Brasil | 5107180 | 51 | 33 | nan | nan | nan | Cerrado | 3.9 |
| c12d57d9-7511-38f2-b060-ee8ec8dce560 | -12.83365 | -51.17305 | 2024-09-26 04:08:00 | NOAA-20 | RIBEIRÃO CASCALHEIRA | MATO GROSSO | Brasil | 5107180 | 51 | 33 | nan | nan | nan | Cerrado | 40.8 |
| ae491500-6846-3107-a903-328df4e4f6f8 | -12.83257 | -51.17884 | 2024-09-26 04:08:00 | NOAA-20 | RIBEIRÃO CASCALHEIRA | MATO GROSSO | Brasil | 5107180 | 51 | 33 | nan | nan | nan | Cerrado | 269.2 |
| 22644567-c29f-33d5-bd8c-b0d7b3c5c613 | -12.83039 | -51.19043 | 2024-09-26 04:08:00 | NOAA-20 | RIBEIRÃO CASCALHEIRA | MATO GROSSO | Brasil | 5107180 | 51 | 33 | nan | nan | nan | Cerrado | 45.7 |
| 413aa189-75b5-3366-a00c-ac7835f58725 | -12.82978 | -51.16626 | 2024-09-26 04:08:00 | NOAA-20 | RIBEIRÃO CASCALHEIRA | MATO GROSSO | Brasil | 5107180 | 51 | 33 | nan | nan | nan | Cerrado | 40.8 |
| 294538d5-9fc0-3375-9dca-408343fa040a | -12.8293 | -51.19624 | 2024-09-26 04:08:00 | NOAA-20 | RIBEIRÃO CASCALHEIRA | MATO GROSSO | Brasil | 5107180 | 51 | 33 | nan | nan | nan | Cerrado | 45.7 |
| 8beb6d9a-0956-32fa-a8c6-56b9db6de33e | -12.8287 | -51.17204 | 2024-09-26 04:08:00 | NOAA-20 | RIBEIRÃO CASCALHEIRA | MATO GROSSO | Brasil | 5107180 | 51 | 33 | nan | nan | nan | Cerrado | 40.8 |
| b9066465-5490-3dd7-ac59-96377a7eeda2 | -12.82821 | -51.20205 | 2024-09-26 04:08:00 | NOAA-20 | RIBEIRÃO CASCALHEIRA | MATO GROSSO | Brasil | 5107180 | 51 | 33 | nan | nan | nan | Cerrado | 16.1 |
| caf3d724-50b1-317e-a13a-bbdc399fbdb6 | -12.82761 | -51.17784 | 2024-09-26 04:08:00 | NOAA-20 | RIBEIRÃO CASCALHEIRA | MATO GROSSO | Brasil | 5107180 | 51 | 33 | nan | nan | nan | Cerrado | 269.2 |
| cade81b4-d7a1-32db-9251-83ce16234691 | -12.82652 | -51.18363 | 2024-09-26 04:08:00 | NOAA-20 | RIBEIRÃO CASCALHEIRA | MATO GROSSO | Brasil | 5107180 | 51 | 33 | nan | nan | nan | Cerrado | 269.2 |
| 49a21da0-d8bf-3708-b82f-cfc5867ba5b8 | -12.82543 | -51.18943 | 2024-09-26 04:08:00 | NOAA-20 | RIBEIRÃO CASCALHEIRA | MATO GROSSO | Brasil | 5107180 | 51 | 33 | nan | nan | nan | Cerrado | 45.7 |
| bf2256af-ae04-3734-bf0b-481f8b410642 | -12.82483 | -51.16526 | 2024-09-26 04:08:00 | NOAA-20 | RIBEIRÃO CASCALHEIRA | MATO GROSSO | Brasil | 5107180 | 51 | 33 | nan | nan | nan | Cerrado | 66.6 |
| 4568e982-8e0f-32dd-a1f9-a91da842ea39 | -12.82434 | -51.19523 | 2024-09-26 04:08:00 | NOAA-20 | RIBEIRÃO CASCALHEIRA | MATO GROSSO | Brasil | 5107180 | 51 | 33 | nan | nan | nan | Cerrado | 45.7 |
| 3584983f-bea9-3f0d-a90d-7c2858b8a08a | -12.82374 | -51.17104 | 2024-09-26 04:08:00 | NOAA-20 | RIBEIRÃO CASCALHEIRA | MATO GROSSO | Brasil | 5107180 | 51 | 33 | nan | nan | nan | Cerrado | 66.6 |


[Clique aqui para ver as próximas entradas](README77.md)
