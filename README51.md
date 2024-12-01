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
| 6d462cf0-8ca6-3656-8478-a7412625bb67 | -3.9955 | -49.94604 | 2024-12-01 04:44:00 | NPP-375D | TUCURUÍ | PARÁ | Brasil | 1508100 | 15 | 33 | nan | nan | nan | Amazônia | 1.9 |
| 2b487491-6cdd-325e-a28f-71e5eec5705e | -3.09365 | -54.2993 | 2024-12-01 04:44:00 | NPP-375D | MOJUÍ DOS CAMPOS | PARÁ | Brasil | 1504752 | 15 | 33 | nan | nan | nan | Amazônia | 4.6 |
| 3d99000b-02b0-3837-b91e-bb6d70d8d22e | -6.59861 | -44.18848 | 2024-12-01 04:44:00 | NPP-375D | PASTOS BONS | MARANHÃO | Brasil | 2108009 | 21 | 33 | nan | nan | nan | Cerrado | 6.2 |
| 191dbef8-0c9b-3019-92b1-5b9d3358c916 | -4.02429 | -49.93629 | 2024-12-01 04:44:00 | NPP-375D | TUCURUÍ | PARÁ | Brasil | 1508100 | 15 | 33 | nan | nan | nan | Amazônia | 1.8 |
| 730618cd-38e8-3c54-84db-1f9a5276628b | -1.23333 | -51.81123 | 2024-12-01 04:44:00 | NPP-375D | GURUPÁ | PARÁ | Brasil | 1503101 | 15 | 33 | nan | nan | nan | Amazônia | 2.7 |
| 58d5411a-3dac-3bb4-975a-05684c89ffb9 | -0.76611 | -52.4588 | 2024-12-01 04:44:00 | NPP-375D | LARANJAL DO JARI | AMAPÁ | Brasil | 1600279 | 16 | 33 | nan | nan | nan | Amazônia | 3.2 |
| fd950de3-e3ec-386b-b2b8-baae3509829c | -2.07042 | -55.01005 | 2024-12-01 04:44:00 | NPP-375D | ALENQUER | PARÁ | Brasil | 1500404 | 15 | 33 | nan | nan | nan | Amazônia | 2.4 |
| 21b51007-9e92-33d7-87ac-227f3e36d76e | -2.33492 | -50.67392 | 2024-12-01 04:44:00 | NPP-375D | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 2.2 |
| 5b6b6000-5466-33b7-aa14-3390082a0a0a | -1.22704 | -51.80642 | 2024-12-01 04:44:00 | NPP-375D | GURUPÁ | PARÁ | Brasil | 1503101 | 15 | 33 | nan | nan | nan | Amazônia | 3.8 |
| 18124c8b-90c2-3221-92b9-38cca4dbded3 | -4.06088 | -54.2434 | 2024-12-01 04:44:00 | NPP-375D | PLACAS | PARÁ | Brasil | 1505650 | 15 | 33 | nan | nan | nan | Amazônia | 2.3 |
| 3c939fef-a3bd-3aae-8745-33136cbb88fd | -2.78693 | -49.82515 | 2024-12-01 04:44:00 | NPP-375D | OEIRAS DO PARÁ | PARÁ | Brasil | 1505205 | 15 | 33 | nan | nan | nan | Amazônia | 1.7 |
| e03c6ea3-b94e-35f6-8458-6f2365b69ccf | -2.38195 | -53.68387 | 2024-12-01 04:44:00 | NPP-375D | PRAINHA | PARÁ | Brasil | 1506005 | 15 | 33 | nan | nan | nan | Amazônia | 1.8 |
| 94a31a7e-075e-3c41-bf2e-8157f372ef04 | -3.51706 | -50.25784 | 2024-12-01 04:44:00 | NPP-375D | PACAJÁ | PARÁ | Brasil | 1505486 | 15 | 33 | nan | nan | nan | Amazônia | 1.8 |
| 4c359fdf-c856-3629-b6d9-46184bdb4264 | -3.70879 | -53.75356 | 2024-12-01 04:44:00 | NPP-375D | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | 1.2 |
| b192ff27-4004-33cb-a7eb-a97e9b07d8e9 | -0.97651 | -51.76157 | 2024-12-01 04:44:00 | NPP-375D | VITÓRIA DO JARI | AMAPÁ | Brasil | 1600808 | 16 | 33 | nan | nan | nan | Amazônia | 2.6 |
| 9a592b9d-79c9-354e-a9a6-423b1daad928 | -1.46592 | -53.69102 | 2024-12-01 04:44:00 | NPP-375D | PRAINHA | PARÁ | Brasil | 1506005 | 15 | 33 | nan | nan | nan | Amazônia | 5.2 |
| 80945b23-5f59-3d08-b3be-1fbc630ee44e | -4.85904 | -50.71549 | 2024-12-01 04:44:00 | NPP-375D | NOVO REPARTIMENTO | PARÁ | Brasil | 1505064 | 15 | 33 | nan | nan | nan | Amazônia | 2.4 |
| c4498c2b-dff1-3028-a666-e7ccdcd2b82b | -2.8069 | -53.05188 | 2024-12-01 04:44:00 | NPP-375D | MEDICILÂNDIA | PARÁ | Brasil | 1504455 | 15 | 33 | nan | nan | nan | Amazônia | 2.1 |
| 7e41aa49-f0e1-3bf0-81eb-fdade95fb297 | -1.23855 | -51.8006 | 2024-12-01 04:44:00 | NPP-375D | GURUPÁ | PARÁ | Brasil | 1503101 | 15 | 33 | nan | nan | nan | Amazônia | 3.2 |
| d7ef7693-d417-3c78-9b3d-8558e2e57d8f | -3.6639 | -51.72594 | 2024-12-01 04:44:00 | NPP-375D | SENADOR JOSÉ PORFÍRIO | PARÁ | Brasil | 1507805 | 15 | 33 | nan | nan | nan | Amazônia | 1.0 |
| 6801755d-cd63-3e5c-9cfc-614e0038fdfb | -2.60224 | -54.09055 | 2024-12-01 04:44:00 | NPP-375D | PRAINHA | PARÁ | Brasil | 1506005 | 15 | 33 | nan | nan | nan | Amazônia | 2.8 |
| bb9a6467-b4d9-3e94-823f-4879bde87c92 | -3.75657 | -49.94105 | 2024-12-01 04:44:00 | NPP-375D | TUCURUÍ | PARÁ | Brasil | 1508100 | 15 | 33 | nan | nan | nan | Amazônia | 1.2 |
| f672301d-74d8-3e16-9749-521ea4040099 | -1.08639 | -53.20288 | 2024-12-01 04:44:00 | NPP-375D | ALMEIRIM | PARÁ | Brasil | 1500503 | 15 | 33 | nan | nan | nan | Amazônia | 2.4 |
| b94f18f2-f58c-380a-b4b8-279769bd9a47 | -3.09197 | -53.2319 | 2024-12-01 04:44:00 | NPP-375D | MEDICILÂNDIA | PARÁ | Brasil | 1504455 | 15 | 33 | nan | nan | nan | Amazônia | 0.6 |
| efb2055b-06cc-312a-8638-a67c7728666c | -2.40399 | -50.3868 | 2024-12-01 04:44:00 | NPP-375D | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 2.1 |
| 3b8b94bd-4fe0-3459-baf3-ca5a0ca85c27 | -4.34012 | -50.7686 | 2024-12-01 04:44:00 | NPP-375D | NOVO REPARTIMENTO | PARÁ | Brasil | 1505064 | 15 | 33 | nan | nan | nan | Amazônia | 1.1 |
| 8f029132-078d-38f7-aaf1-b9954a6f3fd9 | -3.26783 | -50.20787 | 2024-12-01 04:44:00 | NPP-375D | PACAJÁ | PARÁ | Brasil | 1505486 | 15 | 33 | nan | nan | nan | Amazônia | 3.3 |
| 46d3e750-661d-348c-9f61-cf2c700e57bd | -1.42898 | -55.27773 | 2024-12-01 04:44:00 | NPP-375D | ALENQUER | PARÁ | Brasil | 1500404 | 15 | 33 | nan | nan | nan | Amazônia | 1.7 |
| 3c039f6a-7e97-3bb1-b39b-a3779ccb96dc | -2.43362 | -50.43393 | 2024-12-01 04:44:00 | NPP-375D | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 1.6 |
| f4e33e25-1721-39ba-85d4-6a653dc4a88c | -1.6725 | -52.52003 | 2024-12-01 04:44:00 | NPP-375D | PORTO DE MOZ | PARÁ | Brasil | 1505908 | 15 | 33 | nan | nan | nan | Amazônia | 1.1 |
| 11f5f642-33e4-3857-be00-6e1b1a5f3d1f | -3.31709 | -50.02465 | 2024-12-01 04:44:00 | NPP-375D | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 1.6 |
| c7f33e1d-47cd-3637-80bb-5045ce6a1b50 | -3.80848 | -50.06253 | 2024-12-01 04:44:00 | NPP-375D | PACAJÁ | PARÁ | Brasil | 1505486 | 15 | 33 | nan | nan | nan | Amazônia | 2.4 |
| 2e521d0b-c73f-3357-bdca-fd2dc3ff6acb | -4.3209 | -48.09031 | 2024-12-01 04:44:00 | NPP-375D | RONDON DO PARÁ | PARÁ | Brasil | 1506187 | 15 | 33 | nan | nan | nan | Amazônia | 2.2 |
| 6213e568-b34f-3bbf-8934-a21478e04915 | -3.09706 | -53.73146 | 2024-12-01 04:44:00 | NPP-375D | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | 2.3 |
| e415b03b-17f5-36cb-b4c3-4b7aad93d7c8 | -1.25931 | -51.78093 | 2024-12-01 04:44:00 | NPP-375D | GURUPÁ | PARÁ | Brasil | 1503101 | 15 | 33 | nan | nan | nan | Amazônia | 2.4 |
| e5e5403b-08b0-31d7-80c0-04b9f5bc373f | -3.07315 | -53.80859 | 2024-12-01 04:44:00 | NPP-375D | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | 3.8 |
| 78fb6afd-3589-31fd-9f88-f2e0a5b5cf99 | -2.95929 | -53.89166 | 2024-12-01 04:44:00 | NPP-375D | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | 2.2 |
| 44c5e638-e3a5-36de-8e0b-1cc3f0cc7f65 | -3.42728 | -49.99229 | 2024-12-01 04:44:00 | NPP-375D | PACAJÁ | PARÁ | Brasil | 1505486 | 15 | 33 | nan | nan | nan | Amazônia | 3.0 |
| 3460dc16-f6aa-32dc-bce4-baec848edbb7 | -4.76192 | -50.9911 | 2024-12-01 04:44:00 | NPP-375D | ANAPU | PARÁ | Brasil | 1500859 | 15 | 33 | nan | nan | nan | Amazônia | 1.7 |
| 2733f47e-17ca-3205-bbb1-f9044cf64049 | -1.67563 | -52.50039 | 2024-12-01 04:44:00 | NPP-375D | PORTO DE MOZ | PARÁ | Brasil | 1505908 | 15 | 33 | nan | nan | nan | Amazônia | 1.3 |
| 69b00a6e-fc0e-3b73-a751-29cc1a49285e | -1.36768 | -52.86536 | 2024-12-01 04:44:00 | NPP-375D | ALMEIRIM | PARÁ | Brasil | 1500503 | 15 | 33 | nan | nan | nan | Amazônia | 3.1 |
| 655db6fe-aeaa-3d37-a8bf-39f723e73e21 | -2.28314 | -50.56987 | 2024-12-01 04:44:00 | NPP-375D | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 1.4 |
| 925a6c88-901d-3fcc-81a8-76c705648b85 | -6.86657 | -47.24241 | 2024-12-01 04:44:00 | NPP-375D | ESTREITO | MARANHÃO | Brasil | 2104057 | 21 | 33 | nan | nan | nan | Cerrado | 1.2 |
| a4cda4d5-ea3a-31e6-aad1-46cb8aa5db8e | -3.46735 | -50.53228 | 2024-12-01 04:44:00 | NPP-375D | PACAJÁ | PARÁ | Brasil | 1505486 | 15 | 33 | nan | nan | nan | Amazônia | 3.6 |
| f74f3f77-99cd-3ae8-9cf6-f97f27c7f0a1 | -3.53689 | -51.49799 | 2024-12-01 04:44:00 | NPP-375D | ANAPU | PARÁ | Brasil | 1500859 | 15 | 33 | nan | nan | nan | Amazônia | 2.3 |
| 46359a67-288d-30f0-84bb-20710685ad42 | -3.39497 | -50.30549 | 2024-12-01 04:44:00 | NPP-375D | PACAJÁ | PARÁ | Brasil | 1505486 | 15 | 33 | nan | nan | nan | Amazônia | 1.1 |
| ea681ca8-9cbd-3d0b-b1ee-1c958591726c | -2.263 | -50.35789 | 2024-12-01 04:44:00 | NPP-375D | BAGRE | PARÁ | Brasil | 1501105 | 15 | 33 | nan | nan | nan | Amazônia | 1.3 |
| 3e4be1a7-ac1a-35ff-ad7e-aa56b771dae2 | -3.70859 | -51.06411 | 2024-12-01 04:44:00 | NPP-375D | PACAJÁ | PARÁ | Brasil | 1505486 | 15 | 33 | nan | nan | nan | Amazônia | 4.6 |
| 6867f1f5-5d80-35b4-9d83-bc6ba5d802c5 | -2.80332 | -53.05132 | 2024-12-01 04:44:00 | NPP-375D | MEDICILÂNDIA | PARÁ | Brasil | 1504455 | 15 | 33 | nan | nan | nan | Amazônia | 0.8 |
| 79e58222-386f-3a64-969d-9d36c89e0036 | -4.90139 | -41.32531 | 2024-12-01 04:44:00 | NPP-375D | BURITI DOS MONTES | PIAUÍ | Brasil | 2202026 | 22 | 33 | nan | nan | nan | Caatinga | 3.1 |
| aa37bfc4-3dfb-3210-a78e-356db9c94aee | -1.76826 | -50.85717 | 2024-12-01 04:44:00 | NPP-375D | MELGAÇO | PARÁ | Brasil | 1504505 | 15 | 33 | nan | nan | nan | Amazônia | 1.2 |
| 762a9c88-0c53-3319-9291-64537f7705fc | -5.31212 | -50.5671 | 2024-12-01 04:44:00 | NPP-375D | MARABÁ | PARÁ | Brasil | 1504208 | 15 | 33 | nan | nan | nan | Amazônia | 1.4 |
| 0ab95e84-0c7d-33b4-a78c-518cccfc258c | -4.555 | -45.72111 | 2024-12-01 04:44:00 | NPP-375D | SANTA LUZIA | MARANHÃO | Brasil | 2110005 | 21 | 33 | nan | nan | nan | Amazônia | 22.2 |
| 982228d4-e715-36c2-9691-8a1de20e3815 | -2.37312 | -50.43151 | 2024-12-01 04:44:00 | NPP-375D | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 1.6 |
| c96ddb62-3d5f-3eca-b644-8d986db5761e | -2.90041 | -53.9656 | 2024-12-01 04:44:00 | NPP-375D | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | 2.5 |
| 13aaaf5d-879e-353c-b9aa-2c6660a6a8f6 | -2.63481 | -46.57704 | 2024-12-01 04:44:00 | NPP-375D | CENTRO NOVO DO MARANHÃO | MARANHÃO | Brasil | 2103174 | 21 | 33 | nan | nan | nan | Amazônia | 1.1 |
| 1dae819a-c8fe-34b8-84cf-92d5a41cc217 | -5.54828 | -50.27412 | 2024-12-01 04:44:00 | NPP-375D | MARABÁ | PARÁ | Brasil | 1504208 | 15 | 33 | nan | nan | nan | Amazônia | 1.4 |
| d9e5a42c-cb8f-33e6-895d-108d01ac6ed1 | -3.7252 | -50.2053 | 2024-12-01 04:44:00 | NPP-375D | PACAJÁ | PARÁ | Brasil | 1505486 | 15 | 33 | nan | nan | nan | Amazônia | 2.1 |
| d0b85b38-8229-3222-90c0-1dda6aa686f3 | -3.86489 | -52.39376 | 2024-12-01 04:44:00 | NPP-375D | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 0.7 |
| c07f10ab-712d-3434-bc36-8eec6b884f4e | -3.03977 | -51.78439 | 2024-12-01 04:44:00 | NPP-375D | SENADOR JOSÉ PORFÍRIO | PARÁ | Brasil | 1507805 | 15 | 33 | nan | nan | nan | Amazônia | 2.2 |
| a2fc9037-a591-38c3-8ce0-c72492fc9189 | -2.14316 | -54.87157 | 2024-12-01 04:44:00 | NPP-375D | SANTARÉM | PARÁ | Brasil | 1506807 | 15 | 33 | nan | nan | nan | Amazônia | 3.9 |
| feb4a37b-3639-3b45-ba20-33073eee8823 | -2.11512 | -50.62911 | 2024-12-01 04:44:00 | NPP-375D | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 1.3 |
| 4794807c-c052-3bc7-bc93-00b69fd37c58 | -2.22967 | -53.62548 | 2024-12-01 04:44:00 | NPP-375D | PRAINHA | PARÁ | Brasil | 1506005 | 15 | 33 | nan | nan | nan | Amazônia | 1.9 |
| a5a77387-801a-30e8-b89e-f489e9dfcfb0 | -2.27405 | -53.46811 | 2024-12-01 04:44:00 | NPP-375D | PRAINHA | PARÁ | Brasil | 1506005 | 15 | 33 | nan | nan | nan | Amazônia | 1.8 |
| 45a45ef6-d389-36fe-b111-b5e1199d1260 | -1.03925 | -51.73624 | 2024-12-01 04:44:00 | NPP-375D | VITÓRIA DO JARI | AMAPÁ | Brasil | 1600808 | 16 | 33 | nan | nan | nan | Amazônia | 3.0 |
| b71f8bdf-7e5e-37a9-884d-d56d8779aae2 | -1.32074 | -51.74868 | 2024-12-01 04:44:00 | NPP-375D | GURUPÁ | PARÁ | Brasil | 1503101 | 15 | 33 | nan | nan | nan | Amazônia | 1.9 |
| 1faecd21-a43f-3996-b70e-2a5a6b6e33c5 | -1.1277 | -48.3614 | 2024-12-01 04:44:00 | NPP-375D | BELÉM | PARÁ | Brasil | 1501402 | 15 | 33 | nan | nan | nan | Amazônia | 1.7 |
| 12bdc77b-e077-3658-aaaa-5b3cc85a8f0a | -3.9889 | -46.64996 | 2024-12-01 04:44:00 | NPP-375D | BOM JARDIM | MARANHÃO | Brasil | 2102002 | 21 | 33 | nan | nan | nan | Amazônia | 2.2 |
| e6ddf604-8387-3761-8413-0cc6e78b93d2 | -1.25489 | -51.74217 | 2024-12-01 04:44:00 | NPP-375D | GURUPÁ | PARÁ | Brasil | 1503101 | 15 | 33 | nan | nan | nan | Amazônia | 2.6 |
| fb57bfe0-afa8-3c26-bde4-50503ecb52b8 | -1.00544 | -51.72715 | 2024-12-01 04:44:00 | NPP-375D | VITÓRIA DO JARI | AMAPÁ | Brasil | 1600808 | 16 | 33 | nan | nan | nan | Amazônia | 4.5 |
| 1b7bd050-efe0-3f40-9432-c3c4f3232cd6 | -0.59839 | -51.69588 | 2024-12-01 04:44:00 | NPP-375D | MAZAGÃO | AMAPÁ | Brasil | 1600402 | 16 | 33 | nan | nan | nan | Amazônia | 4.5 |
| fa2d861a-cfe9-303e-8fb2-71661210ef8b | -1.15465 | -51.69297 | 2024-12-01 04:44:00 | NPP-375D | GURUPÁ | PARÁ | Brasil | 1503101 | 15 | 33 | nan | nan | nan | Amazônia | 2.8 |
| 8da80415-6054-3e70-a2f1-d775c278ba72 | -3.24839 | -53.86566 | 2024-12-01 04:44:00 | NPP-375D | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | 1.6 |
| 71fd5fc9-6370-35fe-b186-733deb493660 | -3.09949 | -54.0491 | 2024-12-01 04:44:00 | NPP-375D | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | 1.2 |
| 2f16ae57-e3a9-36cd-a280-c38bbbe2d646 | -3.27395 | -50.55528 | 2024-12-01 04:44:00 | NPP-375D | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 3.1 |
| ca2e1bf9-97e2-32cd-9860-4ba773f7b068 | -1.42544 | -55.27329 | 2024-12-01 04:44:00 | NPP-375D | ALENQUER | PARÁ | Brasil | 1500404 | 15 | 33 | nan | nan | nan | Amazônia | 1.5 |
| 99f2781b-8b78-3338-9100-5d50b3f3ed8a | -3.25109 | -53.6353 | 2024-12-01 04:44:00 | NPP-375D | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | 1.4 |
| 4b6a85b4-b095-3ecc-ba88-5f10d9299c61 | -1.89176 | -50.65088 | 2024-12-01 04:44:00 | NPP-375D | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 1.0 |
| 40160b61-6b7f-3cc2-82de-9353a507404a | -1.30589 | -51.73117 | 2024-12-01 04:44:00 | NPP-375D | GURUPÁ | PARÁ | Brasil | 1503101 | 15 | 33 | nan | nan | nan | Amazônia | 3.2 |
| e8063524-dbf7-3453-b293-f5598944753a | -2.98115 | -45.57488 | 2024-12-01 04:44:00 | NPP-375D | PEDRO DO ROSÁRIO | MARANHÃO | Brasil | 2108256 | 21 | 33 | nan | nan | nan | Amazônia | 11.8 |
| 6cba6d23-36b9-3623-b57c-12a2ddb20806 | -2.04177 | -54.66581 | 2024-12-01 04:44:00 | NPP-375D | ALENQUER | PARÁ | Brasil | 1500404 | 15 | 33 | nan | nan | nan | Amazônia | 1.7 |
| 78f6be83-c81e-306c-9d35-1004f504f97b | -3.70737 | -54.60997 | 2024-12-01 04:44:00 | NPP-375D | PLACAS | PARÁ | Brasil | 1505650 | 15 | 33 | nan | nan | nan | Amazônia | 2.6 |
| adfc2f73-c735-3ca5-aff5-d3f4d9bb198a | -1.24318 | -51.79369 | 2024-12-01 04:44:00 | NPP-375D | GURUPÁ | PARÁ | Brasil | 1503101 | 15 | 33 | nan | nan | nan | Amazônia | 2.3 |
| 13328b0e-28b4-3c71-8e7b-a95150fdfc78 | -3.0936 | -53.29096 | 2024-12-01 04:44:00 | NPP-375D | MEDICILÂNDIA | PARÁ | Brasil | 1504455 | 15 | 33 | nan | nan | nan | Amazônia | 1.5 |
| 86e275fb-7986-32fc-9f85-1f12ffa5997c | -1.06383 | -51.75918 | 2024-12-01 04:44:00 | NPP-375D | VITÓRIA DO JARI | AMAPÁ | Brasil | 1600808 | 16 | 33 | nan | nan | nan | Amazônia | 1.8 |
| cbc002be-3368-37c5-87fd-918b6b16d65a | -3.90892 | -46.44069 | 2024-12-01 04:44:00 | NPP-375D | BOM JARDIM | MARANHÃO | Brasil | 2102002 | 21 | 33 | nan | nan | nan | Amazônia | 2.3 |
| 6020282a-4885-30f5-a84b-be1b6bc5e0cd | -3.86011 | -47.06118 | 2024-12-01 04:44:00 | NPP-375D | ITINGA DO MARANHÃO | MARANHÃO | Brasil | 2105427 | 21 | 33 | nan | nan | nan | Amazônia | 2.3 |
| d32318ec-3b34-3c9c-93ce-6ea99058ac0f | -3.14378 | -53.84254 | 2024-12-01 04:44:00 | NPP-375D | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | 1.8 |
| 0c87c040-bafc-3849-87b2-6c1f8fe94418 | -2.53121 | -54.03017 | 2024-12-01 04:44:00 | NPP-375D | PRAINHA | PARÁ | Brasil | 1506005 | 15 | 33 | nan | nan | nan | Amazônia | 1.9 |
| a4a0b246-91bb-36eb-b268-c22d072ce2f0 | -3.09776 | -53.72714 | 2024-12-01 04:44:00 | NPP-375D | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | 2.3 |
| 6b00e710-18be-3653-b68d-275e2d867af5 | -3.05676 | -54.41651 | 2024-12-01 04:44:00 | NPP-375D | MOJUÍ DOS CAMPOS | PARÁ | Brasil | 1504752 | 15 | 33 | nan | nan | nan | Amazônia | 2.5 |
| ae018ec0-a2e8-3edf-8dc5-1655fe537dc1 | -4.69522 | -42.40113 | 2024-12-01 04:44:00 | NPP-375D | JOSÉ DE FREITAS | PIAUÍ | Brasil | 2205508 | 22 | 33 | nan | nan | nan | Caatinga | 2.1 |
| d1e1f3bd-cdec-3765-b5e4-0b5926571108 | -0.9983 | -51.7803 | 2024-12-01 04:44:00 | NPP-375D | VITÓRIA DO JARI | AMAPÁ | Brasil | 1600808 | 16 | 33 | nan | nan | nan | Amazônia | 3.0 |
| 9f359678-6642-3d6c-9603-77d306086f92 | -4.08533 | -49.74266 | 2024-12-01 04:44:00 | NPP-375D | NOVO REPARTIMENTO | PARÁ | Brasil | 1505064 | 15 | 33 | nan | nan | nan | Amazônia | 2.7 |
| 1036962c-6405-393c-aa0d-290772400fbc | -4.35849 | -48.70598 | 2024-12-01 04:44:00 | NPP-375D | RONDON DO PARÁ | PARÁ | Brasil | 1506187 | 15 | 33 | nan | nan | nan | Amazônia | 0.8 |
| 848a715f-919d-3db6-818b-c90fe9573c1e | -1.18993 | -51.75935 | 2024-12-01 04:44:00 | NPP-375D | GURUPÁ | PARÁ | Brasil | 1503101 | 15 | 33 | nan | nan | nan | Amazônia | 2.5 |
| c0d2463e-2c23-3cfc-a5c6-fce96d13b22f | -4.11416 | -54.41436 | 2024-12-01 04:44:00 | NPP-375D | PLACAS | PARÁ | Brasil | 1505650 | 15 | 33 | nan | nan | nan | Amazônia | 1.0 |
| 2cb44c64-d91e-3d59-b6cb-174de65d98cf | -4.77659 | -44.80805 | 2024-12-01 04:44:00 | NPP-375D | POÇÃO DE PEDRAS | MARANHÃO | Brasil | 2108900 | 21 | 33 | nan | nan | nan | Cerrado | 0.6 |
| e36dce52-cc4d-3cf0-941b-572a2206ec54 | -1.70957 | -53.24441 | 2024-12-01 04:44:00 | NPP-375D | ALMEIRIM | PARÁ | Brasil | 1500503 | 15 | 33 | nan | nan | nan | Amazônia | 2.0 |
| 5fd3b74b-4e51-35b4-9068-de595affbd05 | -2.3698 | -50.431 | 2024-12-01 04:44:00 | NPP-375D | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 1.6 |


[Clique aqui para ver as próximas entradas](README52.md)
