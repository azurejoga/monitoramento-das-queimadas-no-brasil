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

## Dados Diários - Página 112

| ID | Latitude | Longitude | Data/Hora GMT | Satélite | Município | Estado | País | Município ID | Estado ID | País ID | Dias sem Chuva | Precipitação | Risco de Fogo | Bioma | FRP |
|----|----------|-----------|---------------|----------|-----------|--------|------|--------------|-----------|---------|----------------|--------------|----------------|-------|-----|
| 0880f953-f735-3a67-a75f-76f74c796f24 | -16.73249 | -57.43442 | 2024-10-02 04:49:00 | NOAA-21 | CÁCERES | MATO GROSSO | Brasil | 5102504 | 51 | 33 | nan | nan | nan | Pantanal | 9.3 |
| 09a30f31-27af-3813-9988-62fecaeb4dc3 | -16.73242 | -57.47808 | 2024-10-02 04:49:00 | NOAA-21 | CÁCERES | MATO GROSSO | Brasil | 5102504 | 51 | 33 | nan | nan | nan | Pantanal | 4.5 |
| feceb349-ac7b-36d8-ab70-89194c077234 | -16.73112 | -57.50708 | 2024-10-02 04:49:00 | NOAA-21 | CÁCERES | MATO GROSSO | Brasil | 5102504 | 51 | 33 | nan | nan | nan | Pantanal | 6.1 |
| 545a4834-62d6-3267-9100-4f76dfe6bce9 | -16.72959 | -57.42903 | 2024-10-02 04:49:00 | NOAA-21 | CÁCERES | MATO GROSSO | Brasil | 5102504 | 51 | 33 | nan | nan | nan | Pantanal | 5.0 |
| 37e02c13-f5e3-37f1-9083-fc60c88e29df | -16.72875 | -57.43372 | 2024-10-02 04:49:00 | NOAA-21 | CÁCERES | MATO GROSSO | Brasil | 5102504 | 51 | 33 | nan | nan | nan | Pantanal | 9.3 |
| cbc4a5c6-83cb-3ef8-8037-57807b97efed | -16.72868 | -57.47738 | 2024-10-02 04:49:00 | NOAA-21 | CÁCERES | MATO GROSSO | Brasil | 5102504 | 51 | 33 | nan | nan | nan | Pantanal | 4.5 |
| 76046b66-a649-33f6-8f91-421b9c93de6b | -16.72753 | -57.41898 | 2024-10-02 04:49:00 | NOAA-21 | CÁCERES | MATO GROSSO | Brasil | 5102504 | 51 | 33 | nan | nan | nan | Pantanal | 8.9 |
| 4e2ded19-ab17-3075-951c-838b8fe10f7f | -16.72737 | -57.50637 | 2024-10-02 04:49:00 | NOAA-21 | CÁCERES | MATO GROSSO | Brasil | 5102504 | 51 | 33 | nan | nan | nan | Pantanal | 5.5 |
| b8efbddb-b713-38b8-bb00-eed77cf2b8da | -16.72669 | -57.42365 | 2024-10-02 04:49:00 | NOAA-21 | CÁCERES | MATO GROSSO | Brasil | 5102504 | 51 | 33 | nan | nan | nan | Pantanal | 33.0 |
| bc950fa7-55a1-3930-8878-d43d6be1313e | -16.72586 | -57.42833 | 2024-10-02 04:49:00 | NOAA-21 | CÁCERES | MATO GROSSO | Brasil | 5102504 | 51 | 33 | nan | nan | nan | Pantanal | 33.0 |
| 30663b38-c05c-3220-9337-6628cb2de015 | -16.72502 | -57.43301 | 2024-10-02 04:49:00 | NOAA-21 | CÁCERES | MATO GROSSO | Brasil | 5102504 | 51 | 33 | nan | nan | nan | Pantanal | 10.3 |
| ae1fdec6-7822-3bef-9794-e7457e13a182 | -16.7238 | -57.41827 | 2024-10-02 04:49:00 | NOAA-21 | CÁCERES | MATO GROSSO | Brasil | 5102504 | 51 | 33 | nan | nan | nan | Pantanal | 8.9 |
| 841a8e9a-38f2-3a05-a57d-d24a47b86b13 | -16.72296 | -57.42294 | 2024-10-02 04:49:00 | NOAA-21 | CÁCERES | MATO GROSSO | Brasil | 5102504 | 51 | 33 | nan | nan | nan | Pantanal | 33.0 |
| 59c63fb7-be18-3852-81ff-0ed58815e353 | -16.72287 | -57.46656 | 2024-10-02 04:49:00 | NOAA-21 | CÁCERES | MATO GROSSO | Brasil | 5102504 | 51 | 33 | nan | nan | nan | Pantanal | 4.0 |
| 58e73bc9-2feb-37a7-9cff-a27673aa2df5 | -16.72212 | -57.42762 | 2024-10-02 04:49:00 | NOAA-21 | CÁCERES | MATO GROSSO | Brasil | 5102504 | 51 | 33 | nan | nan | nan | Pantanal | 33.0 |
| 178d0770-176a-3014-bac7-e21fadf29242 | -16.72203 | -57.47125 | 2024-10-02 04:49:00 | NOAA-21 | CÁCERES | MATO GROSSO | Brasil | 5102504 | 51 | 33 | nan | nan | nan | Pantanal | 9.0 |
| 51f3b464-ab22-3d5f-ab4b-b24562091c41 | -16.71922 | -57.42225 | 2024-10-02 04:49:00 | NOAA-21 | CÁCERES | MATO GROSSO | Brasil | 5102504 | 51 | 33 | nan | nan | nan | Pantanal | 2.4 |
| 96afd9b0-8be0-3d60-b3c0-0f8934cead39 | -16.71828 | -57.47055 | 2024-10-02 04:49:00 | NOAA-21 | CÁCERES | MATO GROSSO | Brasil | 5102504 | 51 | 33 | nan | nan | nan | Pantanal | 2.2 |
| 0950538c-0f5c-3796-af7b-940ae670de4a | -16.71744 | -57.47526 | 2024-10-02 04:49:00 | NOAA-21 | CÁCERES | MATO GROSSO | Brasil | 5102504 | 51 | 33 | nan | nan | nan | Pantanal | 2.2 |
| 3d56138b-92f5-3040-8769-09fe948d7d88 | -16.71454 | -57.46985 | 2024-10-02 04:49:00 | NOAA-21 | CÁCERES | MATO GROSSO | Brasil | 5102504 | 51 | 33 | nan | nan | nan | Pantanal | 2.2 |
| 848c6490-b9ac-35a6-9d3a-39768b48b2eb | -16.70638 | -57.37877 | 2024-10-02 04:49:00 | NOAA-21 | POCONÉ | MATO GROSSO | Brasil | 5106505 | 51 | 33 | nan | nan | nan | Pantanal | 3.1 |
| 4ca470c2-cea1-3378-99e8-3afa725c7060 | -16.7017 | -57.33946 | 2024-10-02 04:49:00 | NOAA-21 | POCONÉ | MATO GROSSO | Brasil | 5106505 | 51 | 33 | nan | nan | nan | Pantanal | 2.4 |
| 4a9855b3-98ed-30b3-9ef0-9096bc7ead15 | -16.70123 | -57.21096 | 2024-10-02 04:49:00 | NOAA-21 | POCONÉ | MATO GROSSO | Brasil | 5106505 | 51 | 33 | nan | nan | nan | Pantanal | 5.0 |
| bee41302-2230-337b-961b-98c2b026d807 | -16.69871 | -57.47173 | 2024-10-02 04:49:00 | NOAA-21 | CÁCERES | MATO GROSSO | Brasil | 5102504 | 51 | 33 | nan | nan | nan | Pantanal | 29.6 |
| 50298e8d-1ed4-3b94-93b7-7c52d22da82f | -16.69864 | -57.18221 | 2024-10-02 04:49:00 | NOAA-21 | POCONÉ | MATO GROSSO | Brasil | 5106505 | 51 | 33 | nan | nan | nan | Pantanal | 20.2 |
| 807f1959-7246-3206-b17c-ae4671675a62 | -16.69834 | -57.46924 | 2024-10-02 04:49:00 | NOAA-21 | CÁCERES | MATO GROSSO | Brasil | 5102504 | 51 | 33 | nan | nan | nan | Pantanal | 24.6 |
| 40c46c5c-28a4-35ca-bcbe-b7c811a98899 | -16.69798 | -57.33876 | 2024-10-02 04:49:00 | NOAA-21 | POCONÉ | MATO GROSSO | Brasil | 5106505 | 51 | 33 | nan | nan | nan | Pantanal | 2.4 |
| d1c84b43-4e0d-3b49-8a03-8d2f73bcd407 | -16.69786 | -57.47644 | 2024-10-02 04:49:00 | NOAA-21 | CÁCERES | MATO GROSSO | Brasil | 5102504 | 51 | 33 | nan | nan | nan | Pantanal | 22.5 |
| 64513594-47e6-331c-a361-86fabf290ab4 | -16.69785 | -57.18676 | 2024-10-02 04:49:00 | NOAA-21 | POCONÉ | MATO GROSSO | Brasil | 5106505 | 51 | 33 | nan | nan | nan | Pantanal | 20.2 |
| cc466bd7-8b2a-36c3-8892-25ae2977fe63 | -16.69753 | -57.21027 | 2024-10-02 04:49:00 | NOAA-21 | POCONÉ | MATO GROSSO | Brasil | 5106505 | 51 | 33 | nan | nan | nan | Pantanal | 5.0 |
| bf470807-fb85-3fa6-88c6-08ebf6a372be | -16.69752 | -57.47395 | 2024-10-02 04:49:00 | NOAA-21 | CÁCERES | MATO GROSSO | Brasil | 5102504 | 51 | 33 | nan | nan | nan | Pantanal | 24.6 |
| 6ddc841b-82d2-3ab8-bf55-985dc10b0635 | -16.69705 | -57.19132 | 2024-10-02 04:49:00 | NOAA-21 | POCONÉ | MATO GROSSO | Brasil | 5106505 | 51 | 33 | nan | nan | nan | Pantanal | 6.6 |
| 08ee10bf-aa79-30b2-ae9d-1e31d829b2fd | -16.6967 | -57.47868 | 2024-10-02 04:49:00 | NOAA-21 | CÁCERES | MATO GROSSO | Brasil | 5102504 | 51 | 33 | nan | nan | nan | Pantanal | 8.1 |
| a8b5f183-bde6-323a-9c39-792fba44f2b1 | -16.69576 | -57.17697 | 2024-10-02 04:49:00 | NOAA-21 | POCONÉ | MATO GROSSO | Brasil | 5106505 | 51 | 33 | nan | nan | nan | Pantanal | 6.8 |
| 9c8084ec-5554-334d-b368-ad4bf63987e4 | -16.69496 | -57.18152 | 2024-10-02 04:49:00 | NOAA-21 | POCONÉ | MATO GROSSO | Brasil | 5106505 | 51 | 33 | nan | nan | nan | Pantanal | 20.2 |
| fb38fba3-fb25-3b6d-9545-9183f29d1f8f | -16.69426 | -57.33805 | 2024-10-02 04:49:00 | NOAA-21 | POCONÉ | MATO GROSSO | Brasil | 5106505 | 51 | 33 | nan | nan | nan | Pantanal | 6.1 |
| 76e92592-902c-39c7-974f-bc1acb43107c | -16.69415 | -57.18607 | 2024-10-02 04:49:00 | NOAA-21 | POCONÉ | MATO GROSSO | Brasil | 5106505 | 51 | 33 | nan | nan | nan | Pantanal | 20.2 |
| 91b2bb1e-df58-3cbd-9980-f2a8be6b8e66 | -16.69377 | -57.47324 | 2024-10-02 04:49:00 | NOAA-21 | CÁCERES | MATO GROSSO | Brasil | 5102504 | 51 | 33 | nan | nan | nan | Pantanal | 5.9 |
| cfa58b40-9294-3d48-85e2-7738d84471cc | -16.69345 | -57.3427 | 2024-10-02 04:49:00 | NOAA-21 | POCONÉ | MATO GROSSO | Brasil | 5106505 | 51 | 33 | nan | nan | nan | Pantanal | 4.4 |
| 9543c92f-5489-397f-937d-1b8ac0324132 | -16.69335 | -57.19063 | 2024-10-02 04:49:00 | NOAA-21 | POCONÉ | MATO GROSSO | Brasil | 5106505 | 51 | 33 | nan | nan | nan | Pantanal | 6.6 |
| cbaffbb2-9b82-3bee-8add-12a7b207a77a | -16.69295 | -57.47796 | 2024-10-02 04:49:00 | NOAA-21 | CÁCERES | MATO GROSSO | Brasil | 5102504 | 51 | 33 | nan | nan | nan | Pantanal | 5.5 |
| 587b8a47-96b3-3ad1-ac1e-014cc91c2e56 | -16.69271 | -57.23772 | 2024-10-02 04:49:00 | NOAA-21 | POCONÉ | MATO GROSSO | Brasil | 5106505 | 51 | 33 | nan | nan | nan | Pantanal | 4.1 |
| 99fd9eb3-48d6-3ce9-a170-270b09fa2f04 | -16.69264 | -57.34734 | 2024-10-02 04:49:00 | NOAA-21 | POCONÉ | MATO GROSSO | Brasil | 5106505 | 51 | 33 | nan | nan | nan | Pantanal | 4.4 |
| f392a5a4-4b1b-3415-8754-d43c623d0f7c | -16.69207 | -57.17628 | 2024-10-02 04:49:00 | NOAA-21 | POCONÉ | MATO GROSSO | Brasil | 5106505 | 51 | 33 | nan | nan | nan | Pantanal | 3.1 |
| ab215570-9634-3f39-a216-9aa2dfb6f1ba | -16.6919 | -57.24231 | 2024-10-02 04:49:00 | NOAA-21 | POCONÉ | MATO GROSSO | Brasil | 5106505 | 51 | 33 | nan | nan | nan | Pantanal | 4.1 |
| 35fef573-f737-36f1-9840-c2ad4f09fc7a | -16.69147 | -57.37596 | 2024-10-02 04:49:00 | NOAA-21 | POCONÉ | MATO GROSSO | Brasil | 5106505 | 51 | 33 | nan | nan | nan | Pantanal | 2.1 |
| 88b3b657-ff97-3614-a62e-088a5ef5cd19 | -16.69127 | -57.18083 | 2024-10-02 04:49:00 | NOAA-21 | POCONÉ | MATO GROSSO | Brasil | 5106505 | 51 | 33 | nan | nan | nan | Pantanal | 9.6 |
| 1392c863-17fc-340d-80f9-46c941d6402f | -16.69047 | -57.18538 | 2024-10-02 04:49:00 | NOAA-21 | POCONÉ | MATO GROSSO | Brasil | 5106505 | 51 | 33 | nan | nan | nan | Pantanal | 9.6 |
| cd03b035-49e2-3694-ab25-455161507904 | -16.69002 | -57.47253 | 2024-10-02 04:49:00 | NOAA-21 | CÁCERES | MATO GROSSO | Brasil | 5102504 | 51 | 33 | nan | nan | nan | Pantanal | 5.9 |
| a72fb60b-e379-38aa-aae6-5473ad740801 | -16.68983 | -57.38528 | 2024-10-02 04:49:00 | NOAA-21 | POCONÉ | MATO GROSSO | Brasil | 5106505 | 51 | 33 | nan | nan | nan | Pantanal | 4.2 |
| d3d5a8d8-b7ed-39f6-a39e-64c808d0b732 | -16.68973 | -57.34199 | 2024-10-02 04:49:00 | NOAA-21 | POCONÉ | MATO GROSSO | Brasil | 5106505 | 51 | 33 | nan | nan | nan | Pantanal | 4.4 |
| 768e227b-1a80-3bfc-9e58-a015d03905ef | -16.6892 | -57.47725 | 2024-10-02 04:49:00 | NOAA-21 | CÁCERES | MATO GROSSO | Brasil | 5102504 | 51 | 33 | nan | nan | nan | Pantanal | 5.5 |
| 1f6c5f73-09ca-316e-98c8-abf2e859c3c5 | -16.68891 | -57.34664 | 2024-10-02 04:49:00 | NOAA-21 | POCONÉ | MATO GROSSO | Brasil | 5106505 | 51 | 33 | nan | nan | nan | Pantanal | 4.4 |
| e9b69fe6-1104-36de-a262-9367e23a5428 | -16.68837 | -57.48197 | 2024-10-02 04:49:00 | NOAA-21 | CÁCERES | MATO GROSSO | Brasil | 5102504 | 51 | 33 | nan | nan | nan | Pantanal | 5.5 |
| 46e0dd59-77ee-31d9-8bf3-a9576d70eed1 | -16.6881 | -57.35128 | 2024-10-02 04:49:00 | NOAA-21 | POCONÉ | MATO GROSSO | Brasil | 5106505 | 51 | 33 | nan | nan | nan | Pantanal | 9.3 |
| 485e7b0b-5fff-3ac8-a070-79484d0bdfa5 | -16.68774 | -57.37526 | 2024-10-02 04:49:00 | NOAA-21 | POCONÉ | MATO GROSSO | Brasil | 5106505 | 51 | 33 | nan | nan | nan | Pantanal | 5.2 |
| 24375b1f-3de6-3001-928e-a5b5532d66c1 | -16.68728 | -57.35593 | 2024-10-02 04:49:00 | NOAA-21 | POCONÉ | MATO GROSSO | Brasil | 5106505 | 51 | 33 | nan | nan | nan | Pantanal | 9.3 |
| 87c4593d-4c45-3fdc-bc38-89435048a77f | -16.68693 | -57.37991 | 2024-10-02 04:49:00 | NOAA-21 | POCONÉ | MATO GROSSO | Brasil | 5106505 | 51 | 33 | nan | nan | nan | Pantanal | 2.9 |
| 73f36509-1d3d-3153-b5aa-c0b98dfe38c1 | -16.68678 | -57.18469 | 2024-10-02 04:49:00 | NOAA-21 | POCONÉ | MATO GROSSO | Brasil | 5106505 | 51 | 33 | nan | nan | nan | Pantanal | 9.6 |
| 02f78771-2cf2-3238-b377-27b714df8efd | -16.68647 | -57.36058 | 2024-10-02 04:49:00 | NOAA-21 | POCONÉ | MATO GROSSO | Brasil | 5106505 | 51 | 33 | nan | nan | nan | Pantanal | 12.8 |
| 6f03b328-74b6-368f-beef-d56a3ca49e9d | -16.68612 | -57.23175 | 2024-10-02 04:49:00 | NOAA-21 | POCONÉ | MATO GROSSO | Brasil | 5106505 | 51 | 33 | nan | nan | nan | Pantanal | 3.0 |
| 62064eae-43f8-31be-9960-4cbc2ecabc46 | -16.68611 | -57.38458 | 2024-10-02 04:49:00 | NOAA-21 | POCONÉ | MATO GROSSO | Brasil | 5106505 | 51 | 33 | nan | nan | nan | Pantanal | 2.9 |
| 7e2e4497-b1f3-3bd3-ac45-85398c36940c | -16.68597 | -57.18925 | 2024-10-02 04:49:00 | NOAA-21 | POCONÉ | MATO GROSSO | Brasil | 5106505 | 51 | 33 | nan | nan | nan | Pantanal | 7.9 |
| 3e5d732a-3e73-3c11-b7ec-5c5173637260 | -16.68565 | -57.36523 | 2024-10-02 04:49:00 | NOAA-21 | POCONÉ | MATO GROSSO | Brasil | 5106505 | 51 | 33 | nan | nan | nan | Pantanal | 12.8 |
| 13a59cde-58fb-33bc-aa24-31c26b735787 | -16.68531 | -57.23633 | 2024-10-02 04:49:00 | NOAA-21 | POCONÉ | MATO GROSSO | Brasil | 5106505 | 51 | 33 | nan | nan | nan | Pantanal | 1.9 |
| 45df9ab6-4cfc-3584-b843-2dae6a48ed0f | -16.68517 | -57.19381 | 2024-10-02 04:49:00 | NOAA-21 | POCONÉ | MATO GROSSO | Brasil | 5106505 | 51 | 33 | nan | nan | nan | Pantanal | 7.9 |
| 6886e6b1-2e6c-3e05-b2cc-f8c8123e9982 | -16.68483 | -57.36989 | 2024-10-02 04:49:00 | NOAA-21 | POCONÉ | MATO GROSSO | Brasil | 5106505 | 51 | 33 | nan | nan | nan | Pantanal | 5.2 |
| 6aa8e6c6-a8f9-3085-8d86-cfff4c7a7fde | -16.68309 | -57.184 | 2024-10-02 04:49:00 | NOAA-21 | POCONÉ | MATO GROSSO | Brasil | 5106505 | 51 | 33 | nan | nan | nan | Pantanal | 2.4 |
| cd985e24-a343-30e0-8a90-feb8b51edfcb | -16.68228 | -57.18855 | 2024-10-02 04:49:00 | NOAA-21 | POCONÉ | MATO GROSSO | Brasil | 5106505 | 51 | 33 | nan | nan | nan | Pantanal | 3.7 |
| 55deef3b-43a4-37c5-b435-aa0a28f6191a | -16.68148 | -57.19312 | 2024-10-02 04:49:00 | NOAA-21 | POCONÉ | MATO GROSSO | Brasil | 5106505 | 51 | 33 | nan | nan | nan | Pantanal | 3.7 |
| 7209c18f-5b12-3875-80d5-dcf40edc92fb | -16.68005 | -57.48528 | 2024-10-02 04:49:00 | NOAA-21 | CÁCERES | MATO GROSSO | Brasil | 5102504 | 51 | 33 | nan | nan | nan | Pantanal | 2.4 |
| a340ea87-2301-381c-a613-5e6e87f38211 | -16.67751 | -57.45557 | 2024-10-02 04:49:00 | NOAA-21 | CÁCERES | MATO GROSSO | Brasil | 5102504 | 51 | 33 | nan | nan | nan | Pantanal | 1.9 |
| 9c7296e1-3163-3029-bdbb-efdb3e4112ce | -16.67258 | -57.24342 | 2024-10-02 04:49:00 | NOAA-21 | POCONÉ | MATO GROSSO | Brasil | 5106505 | 51 | 33 | nan | nan | nan | Pantanal | 1.1 |
| 94770151-9373-3d4e-a3dd-5efad05fc315 | -16.6692 | -57.45886 | 2024-10-02 04:49:00 | NOAA-21 | CÁCERES | MATO GROSSO | Brasil | 5102504 | 51 | 33 | nan | nan | nan | Pantanal | 2.9 |
| dd24b55a-829d-3bb3-aebf-e18d1e1e8461 | -16.66837 | -57.46358 | 2024-10-02 04:49:00 | NOAA-21 | CÁCERES | MATO GROSSO | Brasil | 5102504 | 51 | 33 | nan | nan | nan | Pantanal | 1.0 |
| caec37bc-02b1-3d26-b5c9-e556ffd6014d | -16.66509 | -57.19946 | 2024-10-02 04:49:00 | NOAA-21 | POCONÉ | MATO GROSSO | Brasil | 5106505 | 51 | 33 | nan | nan | nan | Pantanal | 2.2 |
| bf583b5f-bb0c-3bdb-bdee-90558837e651 | -16.66428 | -57.20403 | 2024-10-02 04:49:00 | NOAA-21 | POCONÉ | MATO GROSSO | Brasil | 5106505 | 51 | 33 | nan | nan | nan | Pantanal | 3.1 |
| 3b549514-7bdc-35de-a81c-a8e68e759ac9 | -16.6614 | -57.19877 | 2024-10-02 04:49:00 | NOAA-21 | POCONÉ | MATO GROSSO | Brasil | 5106505 | 51 | 33 | nan | nan | nan | Pantanal | 2.2 |
| 01eef4f1-c691-3ff2-960a-febb3cb35cf9 | -16.66059 | -57.20333 | 2024-10-02 04:49:00 | NOAA-21 | POCONÉ | MATO GROSSO | Brasil | 5106505 | 51 | 33 | nan | nan | nan | Pantanal | 3.1 |
| 7fb4834c-5b1e-3142-9bd4-cd292b7e7b99 | -16.65689 | -57.20265 | 2024-10-02 04:49:00 | NOAA-21 | POCONÉ | MATO GROSSO | Brasil | 5106505 | 51 | 33 | nan | nan | nan | Pantanal | 2.8 |
| f91d8988-0161-302c-a268-00c93fdc8c4a | -16.65608 | -57.20721 | 2024-10-02 04:49:00 | NOAA-21 | POCONÉ | MATO GROSSO | Brasil | 5106505 | 51 | 33 | nan | nan | nan | Pantanal | 2.8 |
| 9115037b-4408-3fa1-816d-7bf3692d9866 | -16.65526 | -57.21178 | 2024-10-02 04:49:00 | NOAA-21 | POCONÉ | MATO GROSSO | Brasil | 5106505 | 51 | 33 | nan | nan | nan | Pantanal | 2.6 |
| 1c134575-8a1d-3868-856d-1553817efbe9 | -16.65417 | -57.32572 | 2024-10-02 04:49:00 | NOAA-21 | POCONÉ | MATO GROSSO | Brasil | 5106505 | 51 | 33 | nan | nan | nan | Pantanal | 2.8 |
| a9451670-4552-3ae1-9bdc-a3104153e3b0 | -16.65238 | -57.20652 | 2024-10-02 04:49:00 | NOAA-21 | POCONÉ | MATO GROSSO | Brasil | 5106505 | 51 | 33 | nan | nan | nan | Pantanal | 2.8 |
| 49111a86-e561-3c39-bb7a-6089d4032836 | -16.65157 | -57.21109 | 2024-10-02 04:49:00 | NOAA-21 | POCONÉ | MATO GROSSO | Brasil | 5106505 | 51 | 33 | nan | nan | nan | Pantanal | 2.6 |
| b8ca6592-111c-36f2-acff-3115637b007d | -16.64787 | -57.21041 | 2024-10-02 04:49:00 | NOAA-21 | POCONÉ | MATO GROSSO | Brasil | 5106505 | 51 | 33 | nan | nan | nan | Pantanal | 2.7 |
| 27e34175-d908-3a40-b40c-ab23509b37a8 | -16.64561 | -57.21118 | 2024-10-02 04:49:00 | NOAA-21 | POCONÉ | MATO GROSSO | Brasil | 5106505 | 51 | 33 | nan | nan | nan | Pantanal | 1.4 |
| 4e08aa11-69b7-31b4-bb1d-b2e076205cf4 | -16.64549 | -57.35287 | 2024-10-02 04:49:00 | NOAA-21 | POCONÉ | MATO GROSSO | Brasil | 5106505 | 51 | 33 | nan | nan | nan | Pantanal | 3.7 |
| 7169a4e1-2851-30a4-8520-2833a92a98e6 | -16.64482 | -57.21576 | 2024-10-02 04:49:00 | NOAA-21 | POCONÉ | MATO GROSSO | Brasil | 5106505 | 51 | 33 | nan | nan | nan | Pantanal | 1.4 |
| 85d12e72-84ee-3b72-8afa-2dc353c62c7b | -16.64177 | -57.35217 | 2024-10-02 04:49:00 | NOAA-21 | POCONÉ | MATO GROSSO | Brasil | 5106505 | 51 | 33 | nan | nan | nan | Pantanal | 3.7 |
| ef7f9a30-aa66-3162-b0eb-218177c753cb | -16.62976 | -57.35472 | 2024-10-02 04:49:00 | NOAA-21 | POCONÉ | MATO GROSSO | Brasil | 5106505 | 51 | 33 | nan | nan | nan | Pantanal | 1.8 |
| e4f625a7-00bc-3769-a6af-bde118d437cc | -16.83221 | -57.46557 | 2024-10-02 04:49:00 | NOAA-21 | CÁCERES | MATO GROSSO | Brasil | 5102504 | 51 | 33 | nan | nan | nan | Pantanal | 2.9 |
| da4015b8-262b-3571-b4b2-3b04947b9b31 | -16.82847 | -57.46487 | 2024-10-02 04:49:00 | NOAA-21 | CÁCERES | MATO GROSSO | Brasil | 5102504 | 51 | 33 | nan | nan | nan | Pantanal | 2.4 |
| 79a28584-8500-3478-8fb2-2f6b74bddee3 | -16.82763 | -57.46955 | 2024-10-02 04:49:00 | NOAA-21 | CÁCERES | MATO GROSSO | Brasil | 5102504 | 51 | 33 | nan | nan | nan | Pantanal | 2.7 |
| bb56559b-a989-30c3-866f-18350809a764 | -16.82389 | -57.46886 | 2024-10-02 04:49:00 | NOAA-21 | CÁCERES | MATO GROSSO | Brasil | 5102504 | 51 | 33 | nan | nan | nan | Pantanal | 2.7 |
| ce04aa27-037a-3f54-ab77-a87f8b0ca03d | -16.82305 | -57.47355 | 2024-10-02 04:49:00 | NOAA-21 | CÁCERES | MATO GROSSO | Brasil | 5102504 | 51 | 33 | nan | nan | nan | Pantanal | 2.7 |
| ff2b65a1-988f-3f5a-8ca2-44ce88e918a5 | -16.81931 | -57.47285 | 2024-10-02 04:49:00 | NOAA-21 | CÁCERES | MATO GROSSO | Brasil | 5102504 | 51 | 33 | nan | nan | nan | Pantanal | 5.3 |
| af22e02e-de3d-3942-b248-82cf490e84a1 | -16.81905 | -57.56058 | 2024-10-02 04:49:00 | NOAA-21 | CÁCERES | MATO GROSSO | Brasil | 5102504 | 51 | 33 | nan | nan | nan | Pantanal | 3.1 |
| b173815e-9029-3f58-98d8-e3594b5709cd | -16.81847 | -57.47754 | 2024-10-02 04:49:00 | NOAA-21 | CÁCERES | MATO GROSSO | Brasil | 5102504 | 51 | 33 | nan | nan | nan | Pantanal | 7.3 |
| 98b8b05d-4940-319d-bf4d-1db9c5a16dda | -16.81809 | -57.47484 | 2024-10-02 04:49:00 | NOAA-21 | CÁCERES | MATO GROSSO | Brasil | 5102504 | 51 | 33 | nan | nan | nan | Pantanal | 8.4 |


[Clique aqui para ver as próximas entradas](README113.md)
