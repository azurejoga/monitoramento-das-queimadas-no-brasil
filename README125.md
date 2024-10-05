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

## Dados Diários - Página 125

| ID | Latitude | Longitude | Data/Hora GMT | Satélite | Município | Estado | País | Município ID | Estado ID | País ID | Dias sem Chuva | Precipitação | Risco de Fogo | Bioma | FRP |
|----|----------|-----------|---------------|----------|-----------|--------|------|--------------|-----------|---------|----------------|--------------|----------------|-------|-----|
| c6aca0fc-a77e-3128-9bd4-ec34cc5875c2 | -17.14415 | -57.3656 | 2024-10-05 04:40:00 | NOAA-20 | CÁCERES | MATO GROSSO | Brasil | 5102504 | 51 | 33 | nan | nan | nan | Pantanal | 2.4 |
| 7ee9fa47-a623-3d51-a304-01ef64f09157 | -17.14384 | -56.75676 | 2024-10-05 04:40:00 | NOAA-20 | POCONÉ | MATO GROSSO | Brasil | 5106505 | 51 | 33 | nan | nan | nan | Pantanal | 5.0 |
| b75543fc-5d8b-3d08-9cf9-08b2df6dfeda | -17.00611 | -56.78642 | 2024-10-05 04:40:00 | NOAA-20 | POCONÉ | MATO GROSSO | Brasil | 5106505 | 51 | 33 | nan | nan | nan | Pantanal | 15.3 |
| c54bf2fc-8b67-3d1d-8361-1fe5aeaee399 | -17.00515 | -56.79171 | 2024-10-05 04:40:00 | NOAA-20 | POCONÉ | MATO GROSSO | Brasil | 5106505 | 51 | 33 | nan | nan | nan | Pantanal | 15.3 |
| 083fffbf-3dfc-307c-9794-b2bcf3b8c040 | -17.00298 | -56.75845 | 2024-10-05 04:40:00 | NOAA-20 | POCONÉ | MATO GROSSO | Brasil | 5106505 | 51 | 33 | nan | nan | nan | Pantanal | 4.2 |
| eb295c6e-e3af-3f0f-a3d2-a45dd9c23ef9 | -17.0012 | -56.79092 | 2024-10-05 04:40:00 | NOAA-20 | POCONÉ | MATO GROSSO | Brasil | 5106505 | 51 | 33 | nan | nan | nan | Pantanal | 15.3 |
| 95e0bb75-1fa9-37ec-be81-e1a0e5c42f6b | -16.99904 | -56.75766 | 2024-10-05 04:40:00 | NOAA-20 | POCONÉ | MATO GROSSO | Brasil | 5106505 | 51 | 33 | nan | nan | nan | Pantanal | 4.2 |
| acdc0619-67a4-3b70-88c8-843d5584aeba | -16.99821 | -56.78485 | 2024-10-05 04:40:00 | NOAA-20 | POCONÉ | MATO GROSSO | Brasil | 5106505 | 51 | 33 | nan | nan | nan | Pantanal | 22.0 |
| 8eb8765c-4f23-3f92-a8c5-290deff16b41 | -16.99809 | -56.76293 | 2024-10-05 04:40:00 | NOAA-20 | POCONÉ | MATO GROSSO | Brasil | 5106505 | 51 | 33 | nan | nan | nan | Pantanal | 3.5 |
| 8ed8f9d6-a5ce-3364-a224-5c7cc4ec0b41 | -16.99725 | -56.79014 | 2024-10-05 04:40:00 | NOAA-20 | POCONÉ | MATO GROSSO | Brasil | 5106505 | 51 | 33 | nan | nan | nan | Pantanal | 22.0 |
| 61e13945-6692-3e0e-85ef-ed7cd022cf81 | -16.99713 | -56.76821 | 2024-10-05 04:40:00 | NOAA-20 | POCONÉ | MATO GROSSO | Brasil | 5106505 | 51 | 33 | nan | nan | nan | Pantanal | 3.5 |
| 0e7fef9b-060b-3bcd-bb5c-80bedaa6cbf4 | -16.9963 | -56.79543 | 2024-10-05 04:40:00 | NOAA-20 | POCONÉ | MATO GROSSO | Brasil | 5106505 | 51 | 33 | nan | nan | nan | Pantanal | 7.7 |
| 7f0cfecc-540e-37ba-8685-a95b0f877bc5 | -16.9951 | -56.75688 | 2024-10-05 04:40:00 | NOAA-20 | POCONÉ | MATO GROSSO | Brasil | 5106505 | 51 | 33 | nan | nan | nan | Pantanal | 3.5 |
| 13ba8409-bef7-3989-add6-e34b340c84ca | -16.99426 | -56.78406 | 2024-10-05 04:40:00 | NOAA-20 | POCONÉ | MATO GROSSO | Brasil | 5106505 | 51 | 33 | nan | nan | nan | Pantanal | 22.0 |
| 4a90f7c1-f040-380b-9bc1-4fab3deb79fe | -16.99415 | -56.76215 | 2024-10-05 04:40:00 | NOAA-20 | POCONÉ | MATO GROSSO | Brasil | 5106505 | 51 | 33 | nan | nan | nan | Pantanal | 4.5 |
| c6498765-60fb-3276-b954-d5e8d0be8668 | -16.99331 | -56.78936 | 2024-10-05 04:40:00 | NOAA-20 | POCONÉ | MATO GROSSO | Brasil | 5106505 | 51 | 33 | nan | nan | nan | Pantanal | 22.0 |
| dd138a54-cbac-3576-8a37-12a9e183c90f | -16.99319 | -56.76742 | 2024-10-05 04:40:00 | NOAA-20 | POCONÉ | MATO GROSSO | Brasil | 5106505 | 51 | 33 | nan | nan | nan | Pantanal | 4.5 |
| baba8f95-c5c0-3f82-a058-6896c814243d | -16.99235 | -56.79464 | 2024-10-05 04:40:00 | NOAA-20 | POCONÉ | MATO GROSSO | Brasil | 5106505 | 51 | 33 | nan | nan | nan | Pantanal | 7.7 |
| 951d800a-0e36-3b5b-9118-9b821181cef4 | -16.99224 | -56.7727 | 2024-10-05 04:40:00 | NOAA-20 | POCONÉ | MATO GROSSO | Brasil | 5106505 | 51 | 33 | nan | nan | nan | Pantanal | 1.8 |
| 4af7cc48-0b5e-3a38-98a8-ad17ddb20046 | -16.99128 | -56.77798 | 2024-10-05 04:40:00 | NOAA-20 | POCONÉ | MATO GROSSO | Brasil | 5106505 | 51 | 33 | nan | nan | nan | Pantanal | 1.8 |
| 8ac56190-119a-3b04-8bd2-e09e9f41a261 | -16.99116 | -56.75609 | 2024-10-05 04:40:00 | NOAA-20 | POCONÉ | MATO GROSSO | Brasil | 5106505 | 51 | 33 | nan | nan | nan | Pantanal | 3.5 |
| c3fcd029-f0ee-3a65-9223-ce8e5fd44390 | -16.99032 | -56.78328 | 2024-10-05 04:40:00 | NOAA-20 | POCONÉ | MATO GROSSO | Brasil | 5106505 | 51 | 33 | nan | nan | nan | Pantanal | 51.8 |
| 691aac0c-ca30-3d55-ae10-79a3ff5edb49 | -16.9902 | -56.76136 | 2024-10-05 04:40:00 | NOAA-20 | POCONÉ | MATO GROSSO | Brasil | 5106505 | 51 | 33 | nan | nan | nan | Pantanal | 4.5 |
| c8dd9289-aee2-3d90-a898-4c64f2f135f3 | -16.98936 | -56.78857 | 2024-10-05 04:40:00 | NOAA-20 | POCONÉ | MATO GROSSO | Brasil | 5106505 | 51 | 33 | nan | nan | nan | Pantanal | 51.8 |
| 9ac97b6b-f423-374c-98e1-b812b20e7ca8 | -16.98925 | -56.76664 | 2024-10-05 04:40:00 | NOAA-20 | POCONÉ | MATO GROSSO | Brasil | 5106505 | 51 | 33 | nan | nan | nan | Pantanal | 4.5 |
| 90dd6a44-b912-3bf4-8edb-674ebf9145d0 | -16.9884 | -56.79386 | 2024-10-05 04:40:00 | NOAA-20 | POCONÉ | MATO GROSSO | Brasil | 5106505 | 51 | 33 | nan | nan | nan | Pantanal | 1.9 |
| de80928c-2765-3d7b-925f-80b1c44c99bb | -16.98829 | -56.77192 | 2024-10-05 04:40:00 | NOAA-20 | POCONÉ | MATO GROSSO | Brasil | 5106505 | 51 | 33 | nan | nan | nan | Pantanal | 1.8 |
| 5e151708-a3cf-30ed-81f6-aa3226da2c81 | -16.98818 | -56.75005 | 2024-10-05 04:40:00 | NOAA-20 | POCONÉ | MATO GROSSO | Brasil | 5106505 | 51 | 33 | nan | nan | nan | Pantanal | 4.1 |
| fdfcf8f1-472d-3ed3-9a34-555d61738a1e | -16.98733 | -56.7772 | 2024-10-05 04:40:00 | NOAA-20 | POCONÉ | MATO GROSSO | Brasil | 5106505 | 51 | 33 | nan | nan | nan | Pantanal | 1.8 |
| e053277b-5c4e-375d-8312-a2e4a1ce9848 | -16.98722 | -56.75531 | 2024-10-05 04:40:00 | NOAA-20 | POCONÉ | MATO GROSSO | Brasil | 5106505 | 51 | 33 | nan | nan | nan | Pantanal | 4.1 |
| ece0dca8-4f98-3a89-8138-a4ea3434bca5 | -16.98637 | -56.78249 | 2024-10-05 04:40:00 | NOAA-20 | POCONÉ | MATO GROSSO | Brasil | 5106505 | 51 | 33 | nan | nan | nan | Pantanal | 51.8 |
| d4760832-2ea4-39f5-ac26-ac267e096ef4 | -16.98626 | -56.76058 | 2024-10-05 04:40:00 | NOAA-20 | POCONÉ | MATO GROSSO | Brasil | 5106505 | 51 | 33 | nan | nan | nan | Pantanal | 8.8 |
| eab31e30-196b-3398-a4bf-932606ce8d4f | -16.98541 | -56.78778 | 2024-10-05 04:40:00 | NOAA-20 | POCONÉ | MATO GROSSO | Brasil | 5106505 | 51 | 33 | nan | nan | nan | Pantanal | 51.8 |
| 9b1e904d-ae01-3a99-9c68-96fe679537d1 | -16.9853 | -56.76586 | 2024-10-05 04:40:00 | NOAA-20 | POCONÉ | MATO GROSSO | Brasil | 5106505 | 51 | 33 | nan | nan | nan | Pantanal | 8.8 |
| 6c7df35e-8529-34b9-a81f-73f5103fd6f9 | -16.98445 | -56.79307 | 2024-10-05 04:40:00 | NOAA-20 | POCONÉ | MATO GROSSO | Brasil | 5106505 | 51 | 33 | nan | nan | nan | Pantanal | 1.9 |
| 8585f6b1-1f3b-39f5-ba5c-5686b4acb3e4 | -16.98434 | -56.77114 | 2024-10-05 04:40:00 | NOAA-20 | POCONÉ | MATO GROSSO | Brasil | 5106505 | 51 | 33 | nan | nan | nan | Pantanal | 24.0 |
| 6c86ec1b-b7ba-38de-902c-fe8dff6237de | -16.98338 | -56.77642 | 2024-10-05 04:40:00 | NOAA-20 | POCONÉ | MATO GROSSO | Brasil | 5106505 | 51 | 33 | nan | nan | nan | Pantanal | 24.0 |
| 5965e51d-070b-348e-aef5-71271b0302a6 | -16.98242 | -56.78171 | 2024-10-05 04:40:00 | NOAA-20 | POCONÉ | MATO GROSSO | Brasil | 5106505 | 51 | 33 | nan | nan | nan | Pantanal | 39.7 |
| ce9614e7-3644-3b74-bf37-975ce3cbecde | -16.98146 | -56.78699 | 2024-10-05 04:40:00 | NOAA-20 | POCONÉ | MATO GROSSO | Brasil | 5106505 | 51 | 33 | nan | nan | nan | Pantanal | 39.7 |
| 0dd3b193-6363-3c7a-8abd-34cf96daea4c | -16.98136 | -56.76508 | 2024-10-05 04:40:00 | NOAA-20 | POCONÉ | MATO GROSSO | Brasil | 5106505 | 51 | 33 | nan | nan | nan | Pantanal | 8.8 |
| 2acdbda2-ffdc-30ce-996f-e68d53e3c8ce | -16.9805 | -56.79229 | 2024-10-05 04:40:00 | NOAA-20 | POCONÉ | MATO GROSSO | Brasil | 5106505 | 51 | 33 | nan | nan | nan | Pantanal | 2.9 |
| 053cdbc2-0e45-34c7-add6-30a211c6dcd4 | -16.9804 | -56.77036 | 2024-10-05 04:40:00 | NOAA-20 | POCONÉ | MATO GROSSO | Brasil | 5106505 | 51 | 33 | nan | nan | nan | Pantanal | 24.0 |
| 03f73222-796d-3377-8c36-2ef00f3e0180 | -16.97944 | -56.77564 | 2024-10-05 04:40:00 | NOAA-20 | POCONÉ | MATO GROSSO | Brasil | 5106505 | 51 | 33 | nan | nan | nan | Pantanal | 24.0 |
| 7ae02349-6806-3c3f-a173-7ed3b7e80fd4 | -16.97848 | -56.78092 | 2024-10-05 04:40:00 | NOAA-20 | POCONÉ | MATO GROSSO | Brasil | 5106505 | 51 | 33 | nan | nan | nan | Pantanal | 39.7 |
| 09595f43-c982-3438-9d01-e756721ae1fc | -16.97751 | -56.78621 | 2024-10-05 04:40:00 | NOAA-20 | POCONÉ | MATO GROSSO | Brasil | 5106505 | 51 | 33 | nan | nan | nan | Pantanal | 39.7 |
| 3c50e33c-c1ab-3fd6-a971-717f1ac8ed65 | -16.97742 | -56.76429 | 2024-10-05 04:40:00 | NOAA-20 | POCONÉ | MATO GROSSO | Brasil | 5106505 | 51 | 33 | nan | nan | nan | Pantanal | 10.3 |
| 189451fe-ddf4-3b4e-9583-037433654cc5 | -16.97645 | -56.76958 | 2024-10-05 04:40:00 | NOAA-20 | POCONÉ | MATO GROSSO | Brasil | 5106505 | 51 | 33 | nan | nan | nan | Pantanal | 51.8 |
| a094eb78-c778-3f39-8894-13864c8ac0e9 | -16.97549 | -56.77485 | 2024-10-05 04:40:00 | NOAA-20 | POCONÉ | MATO GROSSO | Brasil | 5106505 | 51 | 33 | nan | nan | nan | Pantanal | 51.8 |
| 30818bc1-d507-3d1c-819e-c363de509d42 | -16.97453 | -56.78014 | 2024-10-05 04:40:00 | NOAA-20 | POCONÉ | MATO GROSSO | Brasil | 5106505 | 51 | 33 | nan | nan | nan | Pantanal | 8.0 |
| 3319bbfc-6a47-3096-98ba-5ff0d2dec116 | -16.97357 | -56.78542 | 2024-10-05 04:40:00 | NOAA-20 | POCONÉ | MATO GROSSO | Brasil | 5106505 | 51 | 33 | nan | nan | nan | Pantanal | 8.0 |
| b2bbae84-e8d5-38c5-8358-83093ba62276 | -16.97347 | -56.76352 | 2024-10-05 04:40:00 | NOAA-20 | POCONÉ | MATO GROSSO | Brasil | 5106505 | 51 | 33 | nan | nan | nan | Pantanal | 10.3 |
| 094efafb-144f-386a-8100-92031287daf7 | -16.97251 | -56.7688 | 2024-10-05 04:40:00 | NOAA-20 | POCONÉ | MATO GROSSO | Brasil | 5106505 | 51 | 33 | nan | nan | nan | Pantanal | 51.8 |
| baa73d5f-bc75-3a4c-ad05-443f8f1e704f | -16.97154 | -56.77407 | 2024-10-05 04:40:00 | NOAA-20 | POCONÉ | MATO GROSSO | Brasil | 5106505 | 51 | 33 | nan | nan | nan | Pantanal | 51.8 |
| 9de9a71f-7365-323c-b089-4a855091e7bc | -16.97058 | -56.77935 | 2024-10-05 04:40:00 | NOAA-20 | POCONÉ | MATO GROSSO | Brasil | 5106505 | 51 | 33 | nan | nan | nan | Pantanal | 8.0 |
| 51838fbb-3306-342c-8077-a64c09d44017 | -16.96856 | -56.76801 | 2024-10-05 04:40:00 | NOAA-20 | POCONÉ | MATO GROSSO | Brasil | 5106505 | 51 | 33 | nan | nan | nan | Pantanal | 18.8 |
| d1708105-21b3-3b2d-b7d2-5ca94af98778 | -16.9676 | -56.77329 | 2024-10-05 04:40:00 | NOAA-20 | POCONÉ | MATO GROSSO | Brasil | 5106505 | 51 | 33 | nan | nan | nan | Pantanal | 18.8 |
| caa43332-bdbf-30a5-aa6b-853191dea817 | -16.96663 | -56.77857 | 2024-10-05 04:40:00 | NOAA-20 | POCONÉ | MATO GROSSO | Brasil | 5106505 | 51 | 33 | nan | nan | nan | Pantanal | 4.3 |
| 7295c3b6-646c-3b18-a807-e9a8c5db760a | -16.92554 | -57.70657 | 2024-10-05 04:40:00 | NOAA-20 | CÁCERES | MATO GROSSO | Brasil | 5102504 | 51 | 33 | nan | nan | nan | Pantanal | 2.4 |
| 51b17de9-7f74-3c5d-b168-074922cd61bf | -16.9221 | -57.70172 | 2024-10-05 04:40:00 | NOAA-20 | CÁCERES | MATO GROSSO | Brasil | 5102504 | 51 | 33 | nan | nan | nan | Pantanal | 4.1 |
| 864b4f4b-8bf1-3fc6-9ff4-e0f05baf18a1 | -16.91866 | -57.69686 | 2024-10-05 04:40:00 | NOAA-20 | CÁCERES | MATO GROSSO | Brasil | 5102504 | 51 | 33 | nan | nan | nan | Pantanal | 2.1 |
| 8b203f36-c591-37b4-9e3a-478cc6c7c4b4 | -16.91523 | -57.69201 | 2024-10-05 04:40:00 | NOAA-20 | CÁCERES | MATO GROSSO | Brasil | 5102504 | 51 | 33 | nan | nan | nan | Pantanal | 3.2 |
| 9f82ded0-4a4d-3a37-be2c-565d6c247f0d | -16.91449 | -57.69601 | 2024-10-05 04:40:00 | NOAA-20 | CÁCERES | MATO GROSSO | Brasil | 5102504 | 51 | 33 | nan | nan | nan | Pantanal | 3.2 |
| 1241b68b-6388-3af8-a8b7-f9055d837513 | -16.91106 | -57.69116 | 2024-10-05 04:40:00 | NOAA-20 | CÁCERES | MATO GROSSO | Brasil | 5102504 | 51 | 33 | nan | nan | nan | Pantanal | 3.2 |
| 88ce9ccd-7b76-3752-9663-73e74edc09e5 | -16.91031 | -57.69516 | 2024-10-05 04:40:00 | NOAA-20 | CÁCERES | MATO GROSSO | Brasil | 5102504 | 51 | 33 | nan | nan | nan | Pantanal | 3.2 |
| aadb46de-83e8-3509-8d0b-e82a70a6d834 | -16.89092 | -57.6829 | 2024-10-05 04:40:00 | NOAA-20 | CÁCERES | MATO GROSSO | Brasil | 5102504 | 51 | 33 | nan | nan | nan | Pantanal | 2.5 |
| edded2b6-f6fa-3718-b2c8-aee2f8ed1db7 | -16.89016 | -57.6869 | 2024-10-05 04:40:00 | NOAA-20 | CÁCERES | MATO GROSSO | Brasil | 5102504 | 51 | 33 | nan | nan | nan | Pantanal | 3.4 |
| a9edb81b-245b-3c62-adf9-ef9c8d6be00e | -16.8879 | -57.69891 | 2024-10-05 04:40:00 | NOAA-20 | CÁCERES | MATO GROSSO | Brasil | 5102504 | 51 | 33 | nan | nan | nan | Pantanal | 2.7 |
| 97044bd9-f597-3f9e-b84e-2b99a68ab432 | -16.69869 | -57.16499 | 2024-10-05 04:40:00 | NOAA-20 | POCONÉ | MATO GROSSO | Brasil | 5106505 | 51 | 33 | nan | nan | nan | Pantanal | 6.0 |
| 8b83839e-23c3-3ca0-9173-29bd0cbb75f0 | -16.71531 | -57.45736 | 2024-10-05 04:40:00 | NOAA-20 | CÁCERES | MATO GROSSO | Brasil | 5102504 | 51 | 33 | nan | nan | nan | Pantanal | 2.2 |
| e12d6a43-b8e5-38d4-b55d-9db8080e3ae9 | -16.71191 | -57.45263 | 2024-10-05 04:40:00 | NOAA-20 | CÁCERES | MATO GROSSO | Brasil | 5102504 | 51 | 33 | nan | nan | nan | Pantanal | 2.4 |
| db360714-10c3-3107-9a1d-0b355680ccb1 | -16.69845 | -57.42205 | 2024-10-05 04:40:00 | NOAA-20 | CÁCERES | MATO GROSSO | Brasil | 5102504 | 51 | 33 | nan | nan | nan | Pantanal | 1.3 |
| 8d518cad-5a46-355d-96cc-eddeaa790036 | -16.68937 | -57.44846 | 2024-10-05 04:40:00 | NOAA-20 | CÁCERES | MATO GROSSO | Brasil | 5102504 | 51 | 33 | nan | nan | nan | Pantanal | 1.7 |
| 1f5343a2-1f0b-3b90-a72e-47ce1e1a0325 | -16.68524 | -57.44762 | 2024-10-05 04:40:00 | NOAA-20 | CÁCERES | MATO GROSSO | Brasil | 5102504 | 51 | 33 | nan | nan | nan | Pantanal | 2.0 |
| dbec2dc1-c513-35e4-ad47-13ffdbe02aa5 | -16.68453 | -57.45152 | 2024-10-05 04:40:00 | NOAA-20 | CÁCERES | MATO GROSSO | Brasil | 5102504 | 51 | 33 | nan | nan | nan | Pantanal | 3.5 |
| 67fe23ce-5b87-3423-8ec5-2d31abefb701 | -16.68382 | -57.45541 | 2024-10-05 04:40:00 | NOAA-20 | CÁCERES | MATO GROSSO | Brasil | 5102504 | 51 | 33 | nan | nan | nan | Pantanal | 3.5 |
| df12f6d5-a9d9-318b-abcd-7cb1ae449273 | -16.68311 | -57.45932 | 2024-10-05 04:40:00 | NOAA-20 | CÁCERES | MATO GROSSO | Brasil | 5102504 | 51 | 33 | nan | nan | nan | Pantanal | 7.0 |
| 82b8ec21-0ceb-389e-b2db-acdb109b6ee9 | -16.67969 | -57.45458 | 2024-10-05 04:40:00 | NOAA-20 | CÁCERES | MATO GROSSO | Brasil | 5102504 | 51 | 33 | nan | nan | nan | Pantanal | 3.5 |
| cbbe3f7e-f72f-37fe-8a11-1d0ac6d5a3dd | -16.67897 | -57.45848 | 2024-10-05 04:40:00 | NOAA-20 | CÁCERES | MATO GROSSO | Brasil | 5102504 | 51 | 33 | nan | nan | nan | Pantanal | 7.0 |
| 184c0cfe-41b4-3441-8944-23f2e4f34350 | -16.67484 | -57.45765 | 2024-10-05 04:40:00 | NOAA-20 | CÁCERES | MATO GROSSO | Brasil | 5102504 | 51 | 33 | nan | nan | nan | Pantanal | 3.0 |
| f0c45bfa-bac6-3f87-b99e-8f542bbadc7b | -16.65146 | -57.44484 | 2024-10-05 04:40:00 | NOAA-20 | CÁCERES | MATO GROSSO | Brasil | 5102504 | 51 | 33 | nan | nan | nan | Pantanal | 1.2 |
| 72c206f8-cf00-3f20-8c43-a732d3ed6e58 | -17.03697 | -56.70535 | 2024-10-05 04:40:00 | NOAA-20 | POCONÉ | MATO GROSSO | Brasil | 5106505 | 51 | 33 | nan | nan | nan | Pantanal | 3.3 |
| b9c72032-e30b-3282-af9e-b491c0ed3306 | -17.03304 | -56.70456 | 2024-10-05 04:40:00 | NOAA-20 | POCONÉ | MATO GROSSO | Brasil | 5106505 | 51 | 33 | nan | nan | nan | Pantanal | 3.3 |
| 9bf894bb-917f-3005-9c93-b384191acdbc | -17.0321 | -56.7098 | 2024-10-05 04:40:00 | NOAA-20 | POCONÉ | MATO GROSSO | Brasil | 5106505 | 51 | 33 | nan | nan | nan | Pantanal | 3.3 |
| 44b6dfc4-228e-32c0-abb0-acb1fd1d54d7 | -17.02911 | -56.70378 | 2024-10-05 04:40:00 | NOAA-20 | POCONÉ | MATO GROSSO | Brasil | 5106505 | 51 | 33 | nan | nan | nan | Pantanal | 6.2 |
| 533adeb3-5931-3a48-8f57-6e43aa1071d8 | -17.02818 | -56.70902 | 2024-10-05 04:40:00 | NOAA-20 | POCONÉ | MATO GROSSO | Brasil | 5106505 | 51 | 33 | nan | nan | nan | Pantanal | 6.2 |
| cb9b4bd0-ea70-39b5-8ac1-02c43a09e5df | -17.19165 | -57.35532 | 2024-10-05 04:40:00 | NOAA-20 | CÁCERES | MATO GROSSO | Brasil | 5102504 | 51 | 33 | nan | nan | nan | Pantanal | 2.2 |
| 2e87302d-e570-3285-ab3e-afb8812743d1 | -17.17981 | -57.39624 | 2024-10-05 04:40:00 | NOAA-20 | CÁCERES | MATO GROSSO | Brasil | 5102504 | 51 | 33 | nan | nan | nan | Pantanal | 2.4 |
| 79ba308f-e603-3475-9fd1-60c394d34f22 | -17.17911 | -57.40005 | 2024-10-05 04:40:00 | NOAA-20 | CÁCERES | MATO GROSSO | Brasil | 5102504 | 51 | 33 | nan | nan | nan | Pantanal | 2.4 |
| 1fe14573-fcac-3702-a12e-afff12febecc | -17.17873 | -57.35664 | 2024-10-05 04:40:00 | NOAA-20 | CÁCERES | MATO GROSSO | Brasil | 5102504 | 51 | 33 | nan | nan | nan | Pantanal | 2.4 |
| 54778f6e-b5e4-33d9-952b-7942d871b200 | -17.1759 | -57.37179 | 2024-10-05 04:40:00 | NOAA-20 | CÁCERES | MATO GROSSO | Brasil | 5102504 | 51 | 33 | nan | nan | nan | Pantanal | 2.2 |
| b5f3bb2d-d7e7-3f21-92f9-4594521e57c7 | -17.17502 | -57.39922 | 2024-10-05 04:40:00 | NOAA-20 | CÁCERES | MATO GROSSO | Brasil | 5102504 | 51 | 33 | nan | nan | nan | Pantanal | 2.4 |
| 9c44bba3-96e6-359f-bad7-940229ddfad4 | -17.17182 | -57.37097 | 2024-10-05 04:40:00 | NOAA-20 | CÁCERES | MATO GROSSO | Brasil | 5102504 | 51 | 33 | nan | nan | nan | Pantanal | 2.2 |
| 70fe02d8-4dff-300c-931e-3a5381e8a3bd | -17.17023 | -57.4022 | 2024-10-05 04:40:00 | NOAA-20 | CÁCERES | MATO GROSSO | Brasil | 5102504 | 51 | 33 | nan | nan | nan | Pantanal | 5.9 |
| 91d54e6b-aa48-3105-8e80-9afb2efb0487 | -17.16951 | -57.40601 | 2024-10-05 04:40:00 | NOAA-20 | CÁCERES | MATO GROSSO | Brasil | 5102504 | 51 | 33 | nan | nan | nan | Pantanal | 5.9 |
| bc1c919a-9f36-3af4-9205-d8c7af957ec2 | -17.16438 | -57.36552 | 2024-10-05 04:40:00 | NOAA-20 | CÁCERES | MATO GROSSO | Brasil | 5102504 | 51 | 33 | nan | nan | nan | Pantanal | 2.5 |
| e238543e-e61b-32a1-9946-bebc37f3aca9 | -17.15551 | -57.36767 | 2024-10-05 04:40:00 | NOAA-20 | CÁCERES | MATO GROSSO | Brasil | 5102504 | 51 | 33 | nan | nan | nan | Pantanal | 1.9 |
| 88b8979b-3ee2-31e6-b1a5-8054792c4eb6 | -17.14736 | -57.36602 | 2024-10-05 04:40:00 | NOAA-20 | CÁCERES | MATO GROSSO | Brasil | 5102504 | 51 | 33 | nan | nan | nan | Pantanal | 3.1 |
| 7849ab19-7311-3184-b366-355492872541 | -17.14277 | -57.37321 | 2024-10-05 04:40:00 | NOAA-20 | CÁCERES | MATO GROSSO | Brasil | 5102504 | 51 | 33 | nan | nan | nan | Pantanal | 3.4 |
| 4748454d-9e86-3134-b8a5-ea2035a4ea8f | -17.14207 | -57.37703 | 2024-10-05 04:40:00 | NOAA-20 | CÁCERES | MATO GROSSO | Brasil | 5102504 | 51 | 33 | nan | nan | nan | Pantanal | 3.4 |
| c13bbe89-f701-36c1-beb2-7a477374bc17 | -17.14007 | -57.36477 | 2024-10-05 04:40:00 | NOAA-20 | POCONÉ | MATO GROSSO | Brasil | 5106505 | 51 | 33 | nan | nan | nan | Pantanal | 2.4 |


[Clique aqui para ver as próximas entradas](README126.md)
