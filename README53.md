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

## Dados Diários - Página 53

| ID | Latitude | Longitude | Data/Hora GMT | Satélite | Município | Estado | País | Município ID | Estado ID | País ID | Dias sem Chuva | Precipitação | Risco de Fogo | Bioma | FRP |
|----|----------|-----------|---------------|----------|-----------|--------|------|--------------|-----------|---------|----------------|--------------|----------------|-------|-----|
| ebfea800-ac0a-3a82-9539-c3dafb4a81f4 | -2.6568 | -49.32377 | 2024-10-28 04:57:00 | NOAA-21 | MOCAJUBA | PARÁ | Brasil | 1504604 | 15 | 33 | nan | nan | nan | Amazônia | 1.9 |
| 3ec6de0d-8755-31be-9e3d-7df84ec4c968 | -2.65237 | -49.27422 | 2024-10-28 04:57:00 | NOAA-21 | MOJU | PARÁ | Brasil | 1504703 | 15 | 33 | nan | nan | nan | Amazônia | 3.8 |
| 5020fc66-bc8d-3ac5-b46e-c704354536a2 | -2.65032 | -49.83993 | 2024-10-28 04:57:00 | NOAA-21 | OEIRAS DO PARÁ | PARÁ | Brasil | 1505205 | 15 | 33 | nan | nan | nan | Amazônia | 1.3 |
| 54f3781a-5e4d-3c27-9827-75fb9d7f17ea | -2.64964 | -49.79578 | 2024-10-28 04:57:00 | NOAA-21 | OEIRAS DO PARÁ | PARÁ | Brasil | 1505205 | 15 | 33 | nan | nan | nan | Amazônia | 3.4 |
| a9122561-ded3-3877-898c-4ed36e95cf0e | -2.64829 | -49.70671 | 2024-10-28 04:57:00 | NOAA-21 | MOCAJUBA | PARÁ | Brasil | 1504604 | 15 | 33 | nan | nan | nan | Amazônia | 1.5 |
| 28866dae-6937-30bf-9876-8f84da870370 | -2.6401 | -49.25346 | 2024-10-28 04:57:00 | NOAA-21 | MOJU | PARÁ | Brasil | 1504703 | 15 | 33 | nan | nan | nan | Amazônia | 2.1 |
| 5a4edac0-8df8-3beb-b00b-943470424295 | -2.63846 | -49.23901 | 2024-10-28 04:57:00 | NOAA-21 | MOJU | PARÁ | Brasil | 1504703 | 15 | 33 | nan | nan | nan | Amazônia | 3.2 |
| 81e45a32-eba1-3028-aa70-c4d1addc0d21 | -2.63631 | -49.25287 | 2024-10-28 04:57:00 | NOAA-21 | MOJU | PARÁ | Brasil | 1504703 | 15 | 33 | nan | nan | nan | Amazônia | 2.1 |
| 9993c24a-6206-3b30-9300-23a71995bb49 | -2.6311 | -49.26151 | 2024-10-28 04:57:00 | NOAA-21 | MOJU | PARÁ | Brasil | 1504703 | 15 | 33 | nan | nan | nan | Amazônia | 3.3 |
| 4ae48e63-c7dd-33c9-b619-1064586f4dae | -2.62732 | -49.26092 | 2024-10-28 04:57:00 | NOAA-21 | MOJU | PARÁ | Brasil | 1504703 | 15 | 33 | nan | nan | nan | Amazônia | 3.3 |
| 2be8a6c2-5455-3bdd-b539-fcc59fe84a06 | -2.60623 | -50.02855 | 2024-10-28 04:57:00 | NOAA-21 | BAGRE | PARÁ | Brasil | 1501105 | 15 | 33 | nan | nan | nan | Amazônia | 1.4 |
| 40ee0763-db6e-321c-8f14-07d368b94da2 | -2.59853 | -49.11833 | 2024-10-28 04:57:00 | NOAA-21 | MOJU | PARÁ | Brasil | 1504703 | 15 | 33 | nan | nan | nan | Amazônia | 1.3 |
| 595d615b-272c-3d0d-8dc4-129548e2f8bc | -2.59412 | -49.19894 | 2024-10-28 04:57:00 | NOAA-21 | MOJU | PARÁ | Brasil | 1504703 | 15 | 33 | nan | nan | nan | Amazônia | 4.4 |
| cf39f827-1c0f-3ee8-b133-cf92e25a16be | -2.59032 | -49.19835 | 2024-10-28 04:57:00 | NOAA-21 | MOJU | PARÁ | Brasil | 1504703 | 15 | 33 | nan | nan | nan | Amazônia | 4.4 |
| 412b2924-f460-3e58-9ea0-ff392fc0df78 | -2.5892 | -49.23138 | 2024-10-28 04:57:00 | NOAA-21 | MOJU | PARÁ | Brasil | 1504703 | 15 | 33 | nan | nan | nan | Amazônia | 2.3 |
| 8806c76b-8f60-3e13-9013-660c67294e06 | -2.58849 | -49.23603 | 2024-10-28 04:57:00 | NOAA-21 | MOJU | PARÁ | Brasil | 1504703 | 15 | 33 | nan | nan | nan | Amazônia | 2.3 |
| e9588263-800b-31ac-b93e-ee9e779029fc | -2.58723 | -49.19311 | 2024-10-28 04:57:00 | NOAA-21 | MOJU | PARÁ | Brasil | 1504703 | 15 | 33 | nan | nan | nan | Amazônia | 1.4 |
| d6141711-c807-3aab-9113-3d6b4b0e02df | -2.58653 | -49.19776 | 2024-10-28 04:57:00 | NOAA-21 | MOJU | PARÁ | Brasil | 1504703 | 15 | 33 | nan | nan | nan | Amazônia | 1.4 |
| 500c2848-91bd-3efa-be2c-30495a3698b5 | -2.58597 | -49.14985 | 2024-10-28 04:57:00 | NOAA-21 | MOJU | PARÁ | Brasil | 1504703 | 15 | 33 | nan | nan | nan | Amazônia | 2.1 |
| 0626c01a-ab71-326d-9bd0-af88132e8ad7 | -2.58541 | -49.2308 | 2024-10-28 04:57:00 | NOAA-21 | MOJU | PARÁ | Brasil | 1504703 | 15 | 33 | nan | nan | nan | Amazônia | 2.3 |
| 767d9bb3-06e0-31db-96f6-21ec1928878d | -2.5847 | -49.23544 | 2024-10-28 04:57:00 | NOAA-21 | MOJU | PARÁ | Brasil | 1504703 | 15 | 33 | nan | nan | nan | Amazônia | 2.3 |
| 0d248218-5237-3704-acb4-d8434dafd8e0 | -2.58092 | -49.23486 | 2024-10-28 04:57:00 | NOAA-21 | MOJU | PARÁ | Brasil | 1504703 | 15 | 33 | nan | nan | nan | Amazônia | 2.4 |
| 7e69f5ef-edbe-3bea-a3a9-ba97b44f95d4 | -2.57596 | -48.96737 | 2024-10-28 04:57:00 | NOAA-21 | MOJU | PARÁ | Brasil | 1504703 | 15 | 33 | nan | nan | nan | Amazônia | 1.8 |
| 34cc145c-2247-3857-881e-14f81a7c208e | -2.57285 | -48.96202 | 2024-10-28 04:57:00 | NOAA-21 | MOJU | PARÁ | Brasil | 1504703 | 15 | 33 | nan | nan | nan | Amazônia | 1.8 |
| bd99da60-28ec-31e6-b758-aa68acae3258 | -2.57264 | -49.23831 | 2024-10-28 04:57:00 | NOAA-21 | MOJU | PARÁ | Brasil | 1504703 | 15 | 33 | nan | nan | nan | Amazônia | 1.7 |
| 0c47b735-030b-302f-9d43-314b8bc390b3 | -2.57211 | -48.96678 | 2024-10-28 04:57:00 | NOAA-21 | MOJU | PARÁ | Brasil | 1504703 | 15 | 33 | nan | nan | nan | Amazônia | 1.8 |
| 37a3a755-cf85-3706-a45e-bfbe6e2a35a5 | -2.56973 | -48.95666 | 2024-10-28 04:57:00 | NOAA-21 | MOJU | PARÁ | Brasil | 1504703 | 15 | 33 | nan | nan | nan | Amazônia | 1.4 |
| de83755e-4cdf-36ff-b1ee-72ffde7b44ea | -2.56899 | -48.96144 | 2024-10-28 04:57:00 | NOAA-21 | MOJU | PARÁ | Brasil | 1504703 | 15 | 33 | nan | nan | nan | Amazônia | 1.3 |
| 12d45008-205a-3e82-97d5-8ac1b6ec38c5 | -2.56886 | -49.23772 | 2024-10-28 04:57:00 | NOAA-21 | MOJU | PARÁ | Brasil | 1504703 | 15 | 33 | nan | nan | nan | Amazônia | 1.7 |
| 8bf17984-cc58-34a0-8b55-61a94a97c59a | -2.56617 | -49.23052 | 2024-10-28 04:57:00 | NOAA-21 | MOJU | PARÁ | Brasil | 1504703 | 15 | 33 | nan | nan | nan | Amazônia | 2.1 |
| 9d98a900-a079-3912-86fa-3ae7d417fc74 | -2.56588 | -48.95607 | 2024-10-28 04:57:00 | NOAA-21 | MOJU | PARÁ | Brasil | 1504703 | 15 | 33 | nan | nan | nan | Amazônia | 1.4 |
| 4ebdbdc1-7fd4-3b7d-afe6-e662ab2075f9 | -2.56576 | -49.2325 | 2024-10-28 04:57:00 | NOAA-21 | MOJU | PARÁ | Brasil | 1504703 | 15 | 33 | nan | nan | nan | Amazônia | 1.3 |
| f0f2b2c8-a820-3d56-84ca-e75b53c7738c | -2.56544 | -49.23514 | 2024-10-28 04:57:00 | NOAA-21 | MOJU | PARÁ | Brasil | 1504703 | 15 | 33 | nan | nan | nan | Amazônia | 2.1 |
| b3a12411-7816-386d-a62d-ae12077dfbd6 | -2.56507 | -49.23713 | 2024-10-28 04:57:00 | NOAA-21 | MOJU | PARÁ | Brasil | 1504703 | 15 | 33 | nan | nan | nan | Amazônia | 3.0 |
| 7fbe05bd-35f8-3b5c-8b5d-95114917808e | -2.56267 | -49.22728 | 2024-10-28 04:57:00 | NOAA-21 | MOJU | PARÁ | Brasil | 1504703 | 15 | 33 | nan | nan | nan | Amazônia | 1.3 |
| 312fbf9d-6f00-36ed-97f0-29c05e66f9ed | -2.56238 | -49.22993 | 2024-10-28 04:57:00 | NOAA-21 | MOJU | PARÁ | Brasil | 1504703 | 15 | 33 | nan | nan | nan | Amazônia | 2.1 |
| dc3ab14f-44fa-325c-8e6f-f40880dc8849 | -2.56198 | -49.23191 | 2024-10-28 04:57:00 | NOAA-21 | MOJU | PARÁ | Brasil | 1504703 | 15 | 33 | nan | nan | nan | Amazônia | 1.3 |
| d2f9e54a-df60-3687-8a7c-9dd392de779c | -2.5599 | -49.62362 | 2024-10-28 04:57:00 | NOAA-21 | MOCAJUBA | PARÁ | Brasil | 1504604 | 15 | 33 | nan | nan | nan | Amazônia | 1.1 |
| cca07135-aaba-39f9-91d0-f6929ee88251 | -2.55907 | -49.82355 | 2024-10-28 04:57:00 | NOAA-21 | OEIRAS DO PARÁ | PARÁ | Brasil | 1505205 | 15 | 33 | nan | nan | nan | Amazônia | 5.8 |
| 07b32b73-a8a0-3143-b492-3c8ad9f9fa0d | -2.5584 | -49.82784 | 2024-10-28 04:57:00 | NOAA-21 | OEIRAS DO PARÁ | PARÁ | Brasil | 1505205 | 15 | 33 | nan | nan | nan | Amazônia | 3.4 |
| 1b5afbfd-3203-334e-af1d-ce6cc1ff4e28 | -2.55838 | -49.87594 | 2024-10-28 04:57:00 | NOAA-21 | OEIRAS DO PARÁ | PARÁ | Brasil | 1505205 | 15 | 33 | nan | nan | nan | Amazônia | 1.1 |
| b781e9ca-ae73-37a8-8c46-ffbd7a69aea0 | -2.55541 | -49.82299 | 2024-10-28 04:57:00 | NOAA-21 | OEIRAS DO PARÁ | PARÁ | Brasil | 1505205 | 15 | 33 | nan | nan | nan | Amazônia | 5.8 |
| 37a5728e-66f3-301e-9f8f-d43f74b6c082 | -2.55157 | -49.19979 | 2024-10-28 04:57:00 | NOAA-21 | MOJU | PARÁ | Brasil | 1504703 | 15 | 33 | nan | nan | nan | Amazônia | 1.2 |
| 61b2c0cc-781c-37ea-bd81-4e45f709919b | -2.54778 | -49.1992 | 2024-10-28 04:57:00 | NOAA-21 | MOJU | PARÁ | Brasil | 1504703 | 15 | 33 | nan | nan | nan | Amazônia | 0.9 |
| d4ea49bb-75dd-341c-aa37-fdc5d30b9a0f | -2.54614 | -49.1847 | 2024-10-28 04:57:00 | NOAA-21 | MOJU | PARÁ | Brasil | 1504703 | 15 | 33 | nan | nan | nan | Amazônia | 6.9 |
| 5a391673-adf7-39dc-9d46-fcc2611ee5fa | -2.54177 | -49.83844 | 2024-10-28 04:57:00 | NOAA-21 | OEIRAS DO PARÁ | PARÁ | Brasil | 1505205 | 15 | 33 | nan | nan | nan | Amazônia | 6.5 |
| 5db12d3b-e8a4-3d23-90ca-e9687ed95fc9 | -2.53811 | -49.83788 | 2024-10-28 04:57:00 | NOAA-21 | OEIRAS DO PARÁ | PARÁ | Brasil | 1505205 | 15 | 33 | nan | nan | nan | Amazônia | 6.5 |
| 59d91f5e-919a-3990-b0d5-f07996dcbbb2 | -2.52618 | -49.86665 | 2024-10-28 04:57:00 | NOAA-21 | OEIRAS DO PARÁ | PARÁ | Brasil | 1505205 | 15 | 33 | nan | nan | nan | Amazônia | 2.4 |
| 465d2712-6e7d-3354-acec-5438568c32e9 | -2.50998 | -49.72762 | 2024-10-28 04:57:00 | NOAA-21 | CAMETÁ | PARÁ | Brasil | 1502103 | 15 | 33 | nan | nan | nan | Amazônia | 1.3 |
| 761f4032-4ebe-3f8d-9d93-a36dd24cba67 | -2.20939 | -50.32055 | 2024-10-28 04:57:00 | NOAA-21 | BAGRE | PARÁ | Brasil | 1501105 | 15 | 33 | nan | nan | nan | Amazônia | 1.2 |
| 871db0bb-d8d1-317b-8c41-1d24c2633e9e | -2.20645 | -50.31597 | 2024-10-28 04:57:00 | NOAA-21 | BAGRE | PARÁ | Brasil | 1501105 | 15 | 33 | nan | nan | nan | Amazônia | 0.6 |
| 3664be48-f60f-3959-952f-ef5dfe5a355b | -2.20583 | -50.32001 | 2024-10-28 04:57:00 | NOAA-21 | BAGRE | PARÁ | Brasil | 1501105 | 15 | 33 | nan | nan | nan | Amazônia | 0.8 |
| 78a37744-ef9a-3da8-90aa-f927ac810045 | -2.19535 | -49.50538 | 2024-10-28 04:57:00 | NOAA-21 | CAMETÁ | PARÁ | Brasil | 1502103 | 15 | 33 | nan | nan | nan | Amazônia | 1.0 |
| 258420d1-9d04-3c58-b236-542494a5786a | -3.01462 | -50.48257 | 2024-10-28 04:57:00 | NOAA-21 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 1.4 |
| 3bdbd2e0-fb9c-362f-8680-578f0f138b32 | -3.01399 | -50.48661 | 2024-10-28 04:57:00 | NOAA-21 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 2.0 |
| ab9c5c57-663e-312a-b132-c403236b4f8d | -3.01336 | -50.49063 | 2024-10-28 04:57:00 | NOAA-21 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 2.0 |
| 4569a499-71a0-3ee6-b8bc-96d49594125c | -3.01107 | -50.48202 | 2024-10-28 04:57:00 | NOAA-21 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 1.4 |
| 3f3eeb47-216e-3588-abb9-ae221761c647 | -3.01043 | -50.48606 | 2024-10-28 04:57:00 | NOAA-21 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 2.0 |
| d3490a02-f751-3fdf-b250-1aa97a47aab0 | -3.00981 | -50.49009 | 2024-10-28 04:57:00 | NOAA-21 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 2.0 |
| e2f74f7c-476b-3eec-a69c-7ebefadab970 | -3.00918 | -50.49411 | 2024-10-28 04:57:00 | NOAA-21 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 7.3 |
| ac4fba62-5e82-393b-9c7a-50277c22aae0 | -3.00688 | -50.48552 | 2024-10-28 04:57:00 | NOAA-21 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 2.2 |
| 9b9c9658-f114-3f63-a570-38067e734e48 | -3.00625 | -50.48954 | 2024-10-28 04:57:00 | NOAA-21 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 2.2 |
| ff984fcf-3ae4-30ba-913b-4638bffba79f | -3.00332 | -50.48496 | 2024-10-28 04:57:00 | NOAA-21 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 2.2 |
| 23c019bd-44c2-35c4-9a16-ece75f304a5f | -3.00269 | -50.489 | 2024-10-28 04:57:00 | NOAA-21 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 2.2 |
| af35929d-0499-3758-8878-2031c902f3ef | -2.99914 | -50.48845 | 2024-10-28 04:57:00 | NOAA-21 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 2.0 |
| 5766c0aa-4b6c-36ce-a55f-5f1bbe7418c3 | -2.98263 | -50.47746 | 2024-10-28 04:57:00 | NOAA-21 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 2.2 |
| cb00ec3b-b198-3fdf-bf3b-d3a16a287465 | -2.982 | -50.48154 | 2024-10-28 04:57:00 | NOAA-21 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 6.3 |
| f352951a-ce9d-316e-95b9-77a03055d04f | -2.97908 | -50.4769 | 2024-10-28 04:57:00 | NOAA-21 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 14.9 |
| 73ffdf00-832b-3548-82a0-02bae1f38612 | -2.97845 | -50.48096 | 2024-10-28 04:57:00 | NOAA-21 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 11.4 |
| 62521211-9811-3e65-bcba-edb3b3da73b8 | -2.97551 | -50.47639 | 2024-10-28 04:57:00 | NOAA-21 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 14.9 |
| 48d7b1dd-e69d-319e-b299-df2495a167cd | -2.97489 | -50.48041 | 2024-10-28 04:57:00 | NOAA-21 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 11.4 |
| ed3d77a7-f1b2-3e0e-9152-687a49521feb | -2.95446 | -50.5186 | 2024-10-28 04:57:00 | NOAA-21 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 3.1 |
| 0cacf3c8-bf02-356c-8546-162852c7f7da | -2.48513 | -50.27394 | 2024-10-28 04:57:00 | NOAA-21 | BAGRE | PARÁ | Brasil | 1501105 | 15 | 33 | nan | nan | nan | Amazônia | 0.8 |
| 8f6036fd-e087-3f78-b22a-e6a2784e2b51 | -2.4845 | -50.27802 | 2024-10-28 04:57:00 | NOAA-21 | BAGRE | PARÁ | Brasil | 1501105 | 15 | 33 | nan | nan | nan | Amazônia | 1.1 |
| 4a980159-816f-3b31-9bd9-00968415c2bf | -2.48092 | -50.27746 | 2024-10-28 04:57:00 | NOAA-21 | BAGRE | PARÁ | Brasil | 1501105 | 15 | 33 | nan | nan | nan | Amazônia | 1.6 |
| ffd1b884-3320-3226-8926-b335354caf31 | -2.48029 | -50.28153 | 2024-10-28 04:57:00 | NOAA-21 | BAGRE | PARÁ | Brasil | 1501105 | 15 | 33 | nan | nan | nan | Amazônia | 1.6 |
| 68cb289c-3295-34b5-835f-bb0178a1199a | -2.47609 | -50.28505 | 2024-10-28 04:57:00 | NOAA-21 | BAGRE | PARÁ | Brasil | 1501105 | 15 | 33 | nan | nan | nan | Amazônia | 2.0 |
| 2339b5e0-c98f-3c9c-9ffd-95950ee592a0 | -2.47188 | -50.28856 | 2024-10-28 04:57:00 | NOAA-21 | BAGRE | PARÁ | Brasil | 1501105 | 15 | 33 | nan | nan | nan | Amazônia | 2.6 |
| 95a4f527-27a4-3376-a6aa-f1dbc7fd561d | -2.46768 | -50.29206 | 2024-10-28 04:57:00 | NOAA-21 | BAGRE | PARÁ | Brasil | 1501105 | 15 | 33 | nan | nan | nan | Amazônia | 1.3 |
| 4111a43e-caaf-3a97-96eb-335441e5969e | -2.46016 | -50.41069 | 2024-10-28 04:57:00 | NOAA-21 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 1.1 |
| edf98a92-4a30-3424-bc37-7a8258daa400 | -2.45954 | -50.41469 | 2024-10-28 04:57:00 | NOAA-21 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 3.6 |
| cfc3f629-d025-30b6-b911-cc20b042a57d | -2.45661 | -50.41014 | 2024-10-28 04:57:00 | NOAA-21 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 1.1 |
| beeaefb4-8a6a-32ee-9625-a2aed983df9f | -2.45599 | -50.41415 | 2024-10-28 04:57:00 | NOAA-21 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 3.6 |
| 122e9f75-c9e4-33cd-8c56-d845f0858912 | -2.45306 | -50.4096 | 2024-10-28 04:57:00 | NOAA-21 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 0.9 |
| 18346aa5-7d1a-312c-9026-1b070f6cd60f | -2.4474 | -50.37581 | 2024-10-28 04:57:00 | NOAA-21 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 2.1 |
| bc5a914e-7651-397d-ba02-ea343a5616d1 | -2.44384 | -50.37527 | 2024-10-28 04:57:00 | NOAA-21 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 1.1 |
| c4b07d72-5f2b-3b4e-9013-693ae45dd70e | -2.44322 | -50.37929 | 2024-10-28 04:57:00 | NOAA-21 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 3.5 |
| 0c033bfd-cf4f-3fcd-803c-3c274e8cf8af | -2.43967 | -50.37874 | 2024-10-28 04:57:00 | NOAA-21 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 3.5 |
| 7acb551a-67bb-3d5f-a599-4275e4ec80b9 | -2.42113 | -50.40466 | 2024-10-28 04:57:00 | NOAA-21 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 1.2 |
| 5768307b-b0b7-3c09-a963-3c697347c042 | -2.42051 | -50.40865 | 2024-10-28 04:57:00 | NOAA-21 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 2.0 |
| cc82331d-8925-35e3-a7c1-3b32bbc45d51 | -2.41648 | -50.29242 | 2024-10-28 04:57:00 | NOAA-21 | BAGRE | PARÁ | Brasil | 1501105 | 15 | 33 | nan | nan | nan | Amazônia | 0.8 |
| 070a844f-685d-3bae-849f-8e97a2a7e631 | -2.41586 | -50.29648 | 2024-10-28 04:57:00 | NOAA-21 | BAGRE | PARÁ | Brasil | 1501105 | 15 | 33 | nan | nan | nan | Amazônia | 0.8 |
| 8b5bf360-7881-3a72-8bba-41d0c29beca4 | -2.41574 | -50.41611 | 2024-10-28 04:57:00 | NOAA-21 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 2.1 |
| 29d6e7b4-c014-3c39-96c8-5cfa0a9f2888 | -2.41512 | -50.42012 | 2024-10-28 04:57:00 | NOAA-21 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 2.1 |
| 31483455-b837-3cbc-bd32-7abaa9fb438f | -2.41034 | -50.4276 | 2024-10-28 04:57:00 | NOAA-21 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 1.4 |
| e7f82dc7-2925-3edb-b7ee-e178c3cfd44d | -2.40741 | -50.42303 | 2024-10-28 04:57:00 | NOAA-21 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 2.0 |
| 9aa63659-5966-3e42-8c73-c0d2a7da4051 | -2.4068 | -50.42704 | 2024-10-28 04:57:00 | NOAA-21 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 2.0 |
| 015e3049-b124-3041-bd4c-0546b70e7e1e | -2.40387 | -50.42249 | 2024-10-28 04:57:00 | NOAA-21 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 2.0 |
| e3334fcf-2ea3-30f8-89e2-e3bc7bf3435c | -2.40325 | -50.42649 | 2024-10-28 04:57:00 | NOAA-21 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 2.0 |
| 57fc81cd-b82e-3df4-b7a0-47b241bdc6d8 | -2.88831 | -49.25391 | 2024-10-28 04:57:00 | NOAA-21 | MOJU | PARÁ | Brasil | 1504703 | 15 | 33 | nan | nan | nan | Amazônia | 22.4 |


[Clique aqui para ver as próximas entradas](README54.md)
