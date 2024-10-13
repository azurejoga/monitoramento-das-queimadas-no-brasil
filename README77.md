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

## Dados Diários - Página 77

| ID | Latitude | Longitude | Data/Hora GMT | Satélite | Município | Estado | País | Município ID | Estado ID | País ID | Dias sem Chuva | Precipitação | Risco de Fogo | Bioma | FRP |
|----|----------|-----------|---------------|----------|-----------|--------|------|--------------|-----------|---------|----------------|--------------|----------------|-------|-----|
| 474c009f-ce3f-3c8c-a8cd-396aed3ed7c4 | -3.14406 | -50.38449 | 2024-10-13 05:01:00 | NPP-375D | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 2.7 |
| 4dd50e9e-fef7-33f6-9a54-46344df5095a | -3.14089 | -50.37885 | 2024-10-13 05:01:00 | NPP-375D | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 1.4 |
| daaa2bf3-f66a-3334-a2a4-e0e02dac06e5 | -3.14014 | -50.38387 | 2024-10-13 05:01:00 | NPP-375D | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 2.5 |
| b691ca6c-f65e-3b7d-a842-492601e45d6e | -3.04785 | -49.4137 | 2024-10-13 05:01:00 | NPP-375D | MOJU | PARÁ | Brasil | 1504703 | 15 | 33 | nan | nan | nan | Amazônia | 3.1 |
| bb1c3f5d-a017-3d28-ab9f-2e19eccb6ccf | -2.99203 | -49.52777 | 2024-10-13 05:01:00 | NPP-375D | MOJU | PARÁ | Brasil | 1504703 | 15 | 33 | nan | nan | nan | Amazônia | 3.9 |
| 14d861d3-8bd6-359a-aa20-881440e755d9 | -2.98846 | -49.5234 | 2024-10-13 05:01:00 | NPP-375D | MOJU | PARÁ | Brasil | 1504703 | 15 | 33 | nan | nan | nan | Amazônia | 9.8 |
| 96046d81-586d-366e-9aae-f391a7e98744 | -2.98789 | -49.52713 | 2024-10-13 05:01:00 | NPP-375D | MOJU | PARÁ | Brasil | 1504703 | 15 | 33 | nan | nan | nan | Amazônia | 9.8 |
| f22e401d-4438-3819-aa85-0ef12d9c4487 | -2.98732 | -49.53086 | 2024-10-13 05:01:00 | NPP-375D | MOJU | PARÁ | Brasil | 1504703 | 15 | 33 | nan | nan | nan | Amazônia | 6.8 |
| 730aaa39-4837-3e6e-a25c-f8204bc7a2e9 | -2.96175 | -49.35503 | 2024-10-13 05:01:00 | NPP-375D | MOJU | PARÁ | Brasil | 1504703 | 15 | 33 | nan | nan | nan | Amazônia | 0.8 |
| e39c0318-6b57-3c4b-ab8b-48786e620288 | -3.4657 | -50.60935 | 2024-10-13 05:01:00 | NPP-375D | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 3.9 |
| e11c308f-be25-30f9-b08d-0729b318a2e7 | -3.46182 | -50.60875 | 2024-10-13 05:01:00 | NPP-375D | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 3.7 |
| 706c11c9-2890-3981-8d3d-d2fac3d7542e | -4.40927 | -49.75572 | 2024-10-13 05:01:00 | NPP-375D | NOVO REPARTIMENTO | PARÁ | Brasil | 1505064 | 15 | 33 | nan | nan | nan | Amazônia | 1.1 |
| 46ce43aa-fa8d-34a3-898c-02d97b63adca | -4.40871 | -49.75951 | 2024-10-13 05:01:00 | NPP-375D | NOVO REPARTIMENTO | PARÁ | Brasil | 1505064 | 15 | 33 | nan | nan | nan | Amazônia | 2.4 |
| 5ccad292-e013-327e-9f9c-cae66f20949f | -4.40816 | -49.7633 | 2024-10-13 05:01:00 | NPP-375D | NOVO REPARTIMENTO | PARÁ | Brasil | 1505064 | 15 | 33 | nan | nan | nan | Amazônia | 2.4 |
| 5c350fd3-7a2d-3bd6-8bd1-c834ccc85071 | -4.4078 | -49.75615 | 2024-10-13 05:01:00 | NPP-375D | NOVO REPARTIMENTO | PARÁ | Brasil | 1505064 | 15 | 33 | nan | nan | nan | Amazônia | 1.4 |
| 4188b4af-e670-3078-b065-25b8dd3aa44d | -4.40721 | -49.75994 | 2024-10-13 05:01:00 | NPP-375D | NOVO REPARTIMENTO | PARÁ | Brasil | 1505064 | 15 | 33 | nan | nan | nan | Amazônia | 2.5 |
| 5807ffee-e2b1-355d-b86c-b49da5b8d439 | -4.40663 | -49.76373 | 2024-10-13 05:01:00 | NPP-375D | NOVO REPARTIMENTO | PARÁ | Brasil | 1505064 | 15 | 33 | nan | nan | nan | Amazônia | 2.5 |
| 37bed745-225c-31de-a2e1-db43251154c1 | -4.4051 | -49.75507 | 2024-10-13 05:01:00 | NPP-375D | NOVO REPARTIMENTO | PARÁ | Brasil | 1505064 | 15 | 33 | nan | nan | nan | Amazônia | 1.1 |
| d3dbaa5e-6d16-3744-a635-9af07a69dc1d | -4.40455 | -49.75889 | 2024-10-13 05:01:00 | NPP-375D | NOVO REPARTIMENTO | PARÁ | Brasil | 1505064 | 15 | 33 | nan | nan | nan | Amazônia | 2.4 |
| 3aa4e40e-0aeb-368e-8ab7-b1a3247f2c69 | -4.40454 | -50.574 | 2024-10-13 05:01:00 | NPP-375D | NOVO REPARTIMENTO | PARÁ | Brasil | 1505064 | 15 | 33 | nan | nan | nan | Amazônia | 5.6 |
| 5b394b35-be16-3577-ba7a-ab3c8d3ba685 | -4.40399 | -49.7627 | 2024-10-13 05:01:00 | NPP-375D | NOVO REPARTIMENTO | PARÁ | Brasil | 1505064 | 15 | 33 | nan | nan | nan | Amazônia | 2.4 |
| ba03f6a8-d1d0-389c-b4b3-4ebedbb70435 | -4.40363 | -49.75552 | 2024-10-13 05:01:00 | NPP-375D | NOVO REPARTIMENTO | PARÁ | Brasil | 1505064 | 15 | 33 | nan | nan | nan | Amazônia | 2.8 |
| 27140526-76f1-36eb-9b91-f45c19a6a770 | -4.40305 | -49.75932 | 2024-10-13 05:01:00 | NPP-375D | NOVO REPARTIMENTO | PARÁ | Brasil | 1505064 | 15 | 33 | nan | nan | nan | Amazônia | 3.7 |
| 29828cb5-574f-36a0-bc85-b9f74728b6cc | -4.40247 | -49.76312 | 2024-10-13 05:01:00 | NPP-375D | NOVO REPARTIMENTO | PARÁ | Brasil | 1505064 | 15 | 33 | nan | nan | nan | Amazônia | 3.7 |
| 6f8f225c-40d4-3b0c-9f1f-56df448e7d84 | -4.39947 | -49.7549 | 2024-10-13 05:01:00 | NPP-375D | NOVO REPARTIMENTO | PARÁ | Brasil | 1505064 | 15 | 33 | nan | nan | nan | Amazônia | 2.8 |
| 42627df6-efd7-3623-93e0-8f22b1404c66 | -4.39889 | -49.7587 | 2024-10-13 05:01:00 | NPP-375D | NOVO REPARTIMENTO | PARÁ | Brasil | 1505064 | 15 | 33 | nan | nan | nan | Amazônia | 3.7 |
| 8e0befc5-3f1d-3ccd-8807-6b3576226354 | -4.37788 | -50.8074 | 2024-10-13 05:01:00 | NPP-375D | NOVO REPARTIMENTO | PARÁ | Brasil | 1505064 | 15 | 33 | nan | nan | nan | Amazônia | 0.8 |
| 2563984a-e578-3d28-bad3-bc7b5ae022a0 | -4.374 | -50.80679 | 2024-10-13 05:01:00 | NPP-375D | NOVO REPARTIMENTO | PARÁ | Brasil | 1505064 | 15 | 33 | nan | nan | nan | Amazônia | 0.8 |
| 418cb79e-7b67-3d78-9a1e-9372c3bf0fbc | -4.36725 | -50.79809 | 2024-10-13 05:01:00 | NPP-375D | NOVO REPARTIMENTO | PARÁ | Brasil | 1505064 | 15 | 33 | nan | nan | nan | Amazônia | 2.8 |
| 928c2734-7018-36fd-adb3-6c9fccf38a1b | -4.36694 | -50.80074 | 2024-10-13 05:01:00 | NPP-375D | NOVO REPARTIMENTO | PARÁ | Brasil | 1505064 | 15 | 33 | nan | nan | nan | Amazônia | 1.4 |
| be843f37-375a-3215-81e6-6ac96cbcfc51 | -4.36335 | -50.79752 | 2024-10-13 05:01:00 | NPP-375D | NOVO REPARTIMENTO | PARÁ | Brasil | 1505064 | 15 | 33 | nan | nan | nan | Amazônia | 2.8 |
| 836daf7f-c110-3855-989b-12f0d8f32260 | -4.36305 | -50.80017 | 2024-10-13 05:01:00 | NPP-375D | NOVO REPARTIMENTO | PARÁ | Brasil | 1505064 | 15 | 33 | nan | nan | nan | Amazônia | 5.8 |
| 1f848f10-e285-3b3f-b772-8df5b51bd79f | -4.3626 | -50.8024 | 2024-10-13 05:01:00 | NPP-375D | NOVO REPARTIMENTO | PARÁ | Brasil | 1505064 | 15 | 33 | nan | nan | nan | Amazônia | 2.8 |
| 7aa0b001-428e-3698-a06f-27f3e584987b | -4.36233 | -50.80505 | 2024-10-13 05:01:00 | NPP-375D | NOVO REPARTIMENTO | PARÁ | Brasil | 1505064 | 15 | 33 | nan | nan | nan | Amazônia | 3.7 |
| 5bbd79fc-560a-311f-9f1a-2090bfd7a1e1 | -4.36185 | -50.80725 | 2024-10-13 05:01:00 | NPP-375D | NOVO REPARTIMENTO | PARÁ | Brasil | 1505064 | 15 | 33 | nan | nan | nan | Amazônia | 5.0 |
| 49a77ffc-0f71-3126-95f7-86805c93ab8c | -4.35871 | -50.80181 | 2024-10-13 05:01:00 | NPP-375D | NOVO REPARTIMENTO | PARÁ | Brasil | 1505064 | 15 | 33 | nan | nan | nan | Amazônia | 0.9 |
| 0f8ecde9-8999-3f55-821e-4849704bf318 | -4.35844 | -50.80445 | 2024-10-13 05:01:00 | NPP-375D | NOVO REPARTIMENTO | PARÁ | Brasil | 1505064 | 15 | 33 | nan | nan | nan | Amazônia | 3.7 |
| 81386514-fac9-39d7-a84b-4348f8d0dc90 | -4.35796 | -50.80665 | 2024-10-13 05:01:00 | NPP-375D | NOVO REPARTIMENTO | PARÁ | Brasil | 1505064 | 15 | 33 | nan | nan | nan | Amazônia | 1.4 |
| a0e7caf8-e2b3-3141-9411-fe99f34fee52 | -4.35772 | -50.8093 | 2024-10-13 05:01:00 | NPP-375D | NOVO REPARTIMENTO | PARÁ | Brasil | 1505064 | 15 | 33 | nan | nan | nan | Amazônia | 3.7 |
| b0a86277-d221-327c-a6e6-a12bef1f2123 | -4.35721 | -50.81148 | 2024-10-13 05:01:00 | NPP-375D | NOVO REPARTIMENTO | PARÁ | Brasil | 1505064 | 15 | 33 | nan | nan | nan | Amazônia | 1.4 |
| d7f52ce2-38e9-34ce-84e5-7d9f11bee590 | -4.25947 | -50.58847 | 2024-10-13 05:01:00 | NPP-375D | NOVO REPARTIMENTO | PARÁ | Brasil | 1505064 | 15 | 33 | nan | nan | nan | Amazônia | 4.1 |
| e7ae363f-c588-33b3-8e90-43f37699b6c7 | -4.12287 | -50.7521 | 2024-10-13 05:01:00 | NPP-375D | PACAJÁ | PARÁ | Brasil | 1505486 | 15 | 33 | nan | nan | nan | Amazônia | 1.0 |
| d33380f8-5eab-31bb-854d-441f49d0012b | -4.11897 | -50.75154 | 2024-10-13 05:01:00 | NPP-375D | PACAJÁ | PARÁ | Brasil | 1505486 | 15 | 33 | nan | nan | nan | Amazônia | 0.9 |
| cc949194-68fe-3bdb-8486-7435c6b57fcd | -3.96361 | -49.89111 | 2024-10-13 05:01:00 | NPP-375D | TUCURUÍ | PARÁ | Brasil | 1508100 | 15 | 33 | nan | nan | nan | Amazônia | 1.7 |
| 1b97f6c2-1e53-3da9-b967-aa5eafce4d36 | -3.57539 | -50.56904 | 2024-10-13 05:01:00 | NPP-375D | PACAJÁ | PARÁ | Brasil | 1505486 | 15 | 33 | nan | nan | nan | Amazônia | 2.4 |
| 89e485de-54f2-37bb-b410-1cc585e0b8d1 | -3.77848 | -50.1585 | 2024-10-13 05:01:00 | NPP-375D | PACAJÁ | PARÁ | Brasil | 1505486 | 15 | 33 | nan | nan | nan | Amazônia | 2.3 |
| 62a305b4-72a3-3cd7-8537-9e9d7b16a0a7 | -3.77445 | -50.15794 | 2024-10-13 05:01:00 | NPP-375D | PACAJÁ | PARÁ | Brasil | 1505486 | 15 | 33 | nan | nan | nan | Amazônia | 2.3 |
| e62fe840-ea51-3a3c-9058-223aa16ae01d | -3.70114 | -50.1186 | 2024-10-13 05:01:00 | NPP-375D | PACAJÁ | PARÁ | Brasil | 1505486 | 15 | 33 | nan | nan | nan | Amazônia | 0.8 |
| 8345cdc9-8298-3715-aab9-ca3d6de2ab99 | -3.69767 | -50.11446 | 2024-10-13 05:01:00 | NPP-375D | PACAJÁ | PARÁ | Brasil | 1505486 | 15 | 33 | nan | nan | nan | Amazônia | 0.8 |
| 1ac754ac-469b-3aee-af03-df9fc615db9d | -3.69712 | -50.11798 | 2024-10-13 05:01:00 | NPP-375D | PACAJÁ | PARÁ | Brasil | 1505486 | 15 | 33 | nan | nan | nan | Amazônia | 0.8 |
| 6e2b429f-b281-305d-95d3-93aba9661483 | -3.69364 | -50.11385 | 2024-10-13 05:01:00 | NPP-375D | PACAJÁ | PARÁ | Brasil | 1505486 | 15 | 33 | nan | nan | nan | Amazônia | 0.8 |
| 80ca2a3b-a378-37f7-824f-abea07e90a86 | -3.66486 | -49.8662 | 2024-10-13 05:01:00 | NPP-375D | TUCURUÍ | PARÁ | Brasil | 1508100 | 15 | 33 | nan | nan | nan | Amazônia | 2.4 |
| be39b4c5-da3a-3729-ada3-212fcdbd2337 | 0.94896 | -50.20828 | 2024-10-13 05:01:00 | NPP-375D | MACAPÁ | AMAPÁ | Brasil | 1600303 | 16 | 33 | nan | nan | nan | Amazônia | 2.8 |
| 5ceb1582-16fa-3f91-9f1a-3974b2d43c15 | 0.94828 | -50.20592 | 2024-10-13 05:01:00 | NPP-375D | MACAPÁ | AMAPÁ | Brasil | 1600303 | 16 | 33 | nan | nan | nan | Amazônia | 3.3 |
| 0a780259-a0a6-3e8b-888b-a0c4b853b4e2 | 0.75346 | -50.87025 | 2024-10-13 05:01:00 | NPP-375D | MACAPÁ | AMAPÁ | Brasil | 1600303 | 16 | 33 | nan | nan | nan | Amazônia | 1.3 |
| ace8d643-0acc-39fe-aa82-4a33f0c50845 | 0.75279 | -50.86609 | 2024-10-13 05:01:00 | NPP-375D | MACAPÁ | AMAPÁ | Brasil | 1600303 | 16 | 33 | nan | nan | nan | Amazônia | 1.1 |
| 4a0bf2f3-5cc6-3d1d-aee7-bb18861a3774 | -2.19301 | -50.86616 | 2024-10-13 05:01:00 | NPP-375D | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 1.0 |
| b0607e26-e7ac-314e-b32c-e07542701394 | -2.1925 | -50.86837 | 2024-10-13 05:01:00 | NPP-375D | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 1.2 |
| 0bfd8b21-5665-3b49-afb7-6618a2bb395e | -2.05539 | -50.70771 | 2024-10-13 05:01:00 | NPP-375D | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 1.2 |
| f34f973f-b6de-3f25-9d4f-578294815970 | -1.67295 | -51.1588 | 2024-10-13 05:01:00 | NPP-375D | MELGAÇO | PARÁ | Brasil | 1504505 | 15 | 33 | nan | nan | nan | Amazônia | 0.6 |
| 0b3a0395-78f6-3a18-ac02-9838006f9c83 | -1.59572 | -50.44503 | 2024-10-13 05:01:00 | NPP-375D | BREVES | PARÁ | Brasil | 1501808 | 15 | 33 | nan | nan | nan | Amazônia | 1.0 |
| e56dda3e-262f-3b30-b13a-4d796a4ca937 | -1.57262 | -51.58875 | 2024-10-13 05:01:00 | NPP-375D | GURUPÁ | PARÁ | Brasil | 1503101 | 15 | 33 | nan | nan | nan | Amazônia | 0.8 |
| 1d90d7e8-0617-38cc-899a-66f788b362b7 | -1.51534 | -51.61454 | 2024-10-13 05:01:00 | NPP-375D | GURUPÁ | PARÁ | Brasil | 1503101 | 15 | 33 | nan | nan | nan | Amazônia | 0.7 |
| ca103303-fdfe-3d2a-a80b-fd72bdc432e3 | -2.82876 | -51.34304 | 2024-10-13 05:01:00 | NPP-375D | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 0.9 |
| f90b4738-8453-320a-bebe-7b4f328de820 | -2.82574 | -51.33815 | 2024-10-13 05:01:00 | NPP-375D | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 1.9 |
| c2aa41a0-83db-3687-9cdd-f80e7b5c9826 | -2.82272 | -51.33324 | 2024-10-13 05:01:00 | NPP-375D | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 1.9 |
| af4bb4e3-551e-3ba7-b604-c2af42c58afe | -2.82205 | -51.33758 | 2024-10-13 05:01:00 | NPP-375D | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 1.9 |
| d96dddae-bac1-32c6-8df2-29b222b1a863 | -2.82138 | -51.34192 | 2024-10-13 05:01:00 | NPP-375D | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 1.4 |
| ad8cec81-ebd9-3afd-b768-621d0b93bc5d | -2.81835 | -51.33701 | 2024-10-13 05:01:00 | NPP-375D | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 2.4 |
| c34bd6d8-e95d-3dda-bbce-609b42891273 | -2.81466 | -51.33644 | 2024-10-13 05:01:00 | NPP-375D | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 2.4 |
| 1ee41fbe-e20d-3e77-a6ea-499ccb7e4d01 | -2.80623 | -51.01628 | 2024-10-13 05:01:00 | NPP-375D | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 0.9 |
| cf8c13b0-3f15-3a98-9889-6f96dff72ac8 | -2.80553 | -51.02076 | 2024-10-13 05:01:00 | NPP-375D | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 0.9 |
| c9735025-09e8-3a50-b7b8-7b271e802cc7 | -2.80317 | -51.01122 | 2024-10-13 05:01:00 | NPP-375D | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 1.5 |
| ebc8d08c-b14e-3b7b-9383-620f404002ed | -2.80247 | -51.01571 | 2024-10-13 05:01:00 | NPP-375D | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 0.9 |
| ac6240d2-965a-34bf-a8c2-fd663dba41fb | -2.80178 | -51.02016 | 2024-10-13 05:01:00 | NPP-375D | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 0.9 |
| bea98603-8eb7-3fe0-9c24-8bc8065bad1a | -2.79872 | -51.01509 | 2024-10-13 05:01:00 | NPP-375D | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 1.3 |
| 7db6735a-bad1-3453-bfdf-fac37c8536fe | -2.78788 | -51.36332 | 2024-10-13 05:01:00 | NPP-375D | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 1.4 |
| f8415c3a-798f-3531-9f07-2f2a62a42957 | -2.78723 | -51.36762 | 2024-10-13 05:01:00 | NPP-375D | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 1.4 |
| 4e917271-dd9d-324a-9454-6ae9a2432aaa | -2.78657 | -51.37193 | 2024-10-13 05:01:00 | NPP-375D | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 0.3 |
| 5c9896d1-24ab-3cbe-8ab1-d00bd210a491 | -2.78419 | -51.36276 | 2024-10-13 05:01:00 | NPP-375D | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 0.7 |
| 27fbc8c2-33ed-33f3-8dd7-0400974ae02f | -2.78354 | -51.36707 | 2024-10-13 05:01:00 | NPP-375D | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 0.7 |
| 5bff8b86-3fc4-3632-81d9-ff9db2104522 | -2.77985 | -51.36651 | 2024-10-13 05:01:00 | NPP-375D | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 0.7 |
| 70281ba9-d6fe-3191-9e3a-cb8761899ca1 | -2.77551 | -51.37027 | 2024-10-13 05:01:00 | NPP-375D | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 1.2 |
| c7be9d37-eeb8-3c41-9802-55452e8cc143 | -2.77182 | -51.3697 | 2024-10-13 05:01:00 | NPP-375D | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 1.2 |
| 3d463147-d5f7-3a59-b88c-ef2c5f4e494a | -3.66464 | -50.95094 | 2024-10-13 05:01:00 | NPP-375D | PACAJÁ | PARÁ | Brasil | 1505486 | 15 | 33 | nan | nan | nan | Amazônia | 1.1 |
| 771191cc-0e0d-3ae2-a3b2-840982e3e158 | -3.53803 | -51.24906 | 2024-10-13 05:01:00 | NPP-375D | ANAPU | PARÁ | Brasil | 1500859 | 15 | 33 | nan | nan | nan | Amazônia | 1.2 |
| 93d77361-78e0-3613-a623-87dae1be5819 | -3.53678 | -51.251 | 2024-10-13 05:01:00 | NPP-375D | ANAPU | PARÁ | Brasil | 1500859 | 15 | 33 | nan | nan | nan | Amazônia | 2.7 |
| abf757a7-2bcf-34e6-be99-2ea53c613b71 | -3.53428 | -51.24852 | 2024-10-13 05:01:00 | NPP-375D | ANAPU | PARÁ | Brasil | 1500859 | 15 | 33 | nan | nan | nan | Amazônia | 3.9 |
| a3798487-5c71-3def-883d-8246c7765363 | -3.53303 | -51.25047 | 2024-10-13 05:01:00 | NPP-375D | ANAPU | PARÁ | Brasil | 1500859 | 15 | 33 | nan | nan | nan | Amazônia | 1.9 |
| 8d2f6812-4af5-3b8c-99bd-217b83f1811a | -3.47349 | -51.21382 | 2024-10-13 05:01:00 | NPP-375D | ANAPU | PARÁ | Brasil | 1500859 | 15 | 33 | nan | nan | nan | Amazônia | 4.3 |
| b800cdf4-2fcc-351d-83eb-d264f5d72a66 | -3.33916 | -50.80774 | 2024-10-13 05:01:00 | NPP-375D | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 2.0 |
| 128451b9-1226-3780-8df9-91d940258fff | -3.33533 | -50.80716 | 2024-10-13 05:01:00 | NPP-375D | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 2.0 |
| abdce182-f465-3f63-8647-1797653dbed0 | -3.30379 | -51.11356 | 2024-10-13 05:01:00 | NPP-375D | PACAJÁ | PARÁ | Brasil | 1505486 | 15 | 33 | nan | nan | nan | Amazônia | 1.9 |
| c5e65d02-c96b-3b10-a59e-4edb49a79534 | -3.2775 | -50.77432 | 2024-10-13 05:01:00 | NPP-375D | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 2.0 |
| e67d5050-801d-3356-a1ca-202fd2383f17 | -3.22343 | -51.28847 | 2024-10-13 05:01:00 | NPP-375D | ANAPU | PARÁ | Brasil | 1500859 | 15 | 33 | nan | nan | nan | Amazônia | 1.6 |
| 45d06e18-79dd-352c-b64f-19495e77d6bb | -3.20182 | -51.15092 | 2024-10-13 05:01:00 | NPP-375D | PACAJÁ | PARÁ | Brasil | 1505486 | 15 | 33 | nan | nan | nan | Amazônia | 1.0 |
| e0ed1fe1-16ca-3c15-85dc-04ff820f960f | -3.09002 | -51.22278 | 2024-10-13 05:01:00 | NPP-375D | ANAPU | PARÁ | Brasil | 1500859 | 15 | 33 | nan | nan | nan | Amazônia | 1.2 |
| 9995b73b-3719-3c53-9e16-a3cf744d77b1 | -3.08934 | -51.22715 | 2024-10-13 05:01:00 | NPP-375D | ANAPU | PARÁ | Brasil | 1500859 | 15 | 33 | nan | nan | nan | Amazônia | 1.8 |
| 74ab3b13-79b6-3125-b3be-7226f454f9d8 | -3.07593 | -51.33745 | 2024-10-13 05:01:00 | NPP-375D | ANAPU | PARÁ | Brasil | 1500859 | 15 | 33 | nan | nan | nan | Amazônia | 1.4 |
| 8d9a1b61-1336-33f0-9fb3-6f3202508793 | -3.07223 | -51.33687 | 2024-10-13 05:01:00 | NPP-375D | ANAPU | PARÁ | Brasil | 1500859 | 15 | 33 | nan | nan | nan | Amazônia | 2.3 |


[Clique aqui para ver as próximas entradas](README78.md)
