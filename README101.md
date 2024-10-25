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
| 07c7cc7e-ef45-3262-ae49-7909fda1a461 | -17.25168 | -57.50616 | 2024-10-25 05:06:00 | NOAA-20 | CÁCERES | MATO GROSSO | Brasil | 5102504 | 51 | 33 | nan | nan | nan | Pantanal | 7.8 |
| 00fadfe3-aff2-3d03-90e9-a36c184a79de | -17.25001 | -57.51709 | 2024-10-25 05:06:00 | NOAA-20 | CÁCERES | MATO GROSSO | Brasil | 5102504 | 51 | 33 | nan | nan | nan | Pantanal | 2.6 |
| 259e4cf3-2c16-307a-bbeb-b64ed90a30d7 | -17.24831 | -57.50939 | 2024-10-25 05:06:00 | NOAA-20 | CÁCERES | MATO GROSSO | Brasil | 5102504 | 51 | 33 | nan | nan | nan | Pantanal | 2.1 |
| fcadcf87-6a0c-3180-aaad-fa7b0322c4af | -17.23829 | -57.53013 | 2024-10-25 05:06:00 | NOAA-20 | CÁCERES | MATO GROSSO | Brasil | 5102504 | 51 | 33 | nan | nan | nan | Pantanal | 3.7 |
| 49766577-7b7e-3900-8fc0-3be5cae32361 | -17.23553 | -57.52594 | 2024-10-25 05:06:00 | NOAA-20 | CÁCERES | MATO GROSSO | Brasil | 5102504 | 51 | 33 | nan | nan | nan | Pantanal | 3.6 |
| ea554d23-7eaa-3dd8-92f6-1b6df5a8dd0d | -17.22613 | -57.49825 | 2024-10-25 05:06:00 | NOAA-20 | CÁCERES | MATO GROSSO | Brasil | 5102504 | 51 | 33 | nan | nan | nan | Pantanal | 1.2 |
| 2ac3e1e6-1889-3f50-ac36-8f98501bfa2f | -17.2256 | -57.47948 | 2024-10-25 05:06:00 | NOAA-20 | CÁCERES | MATO GROSSO | Brasil | 5102504 | 51 | 33 | nan | nan | nan | Pantanal | 1.7 |
| 223cd085-2405-3bc9-9dba-7ea92128048b | -17.22336 | -57.49405 | 2024-10-25 05:06:00 | NOAA-20 | CÁCERES | MATO GROSSO | Brasil | 5102504 | 51 | 33 | nan | nan | nan | Pantanal | 7.1 |
| 56dd5e19-294d-3b34-a9b5-99993bed39a1 | -17.22224 | -57.50134 | 2024-10-25 05:06:00 | NOAA-20 | CÁCERES | MATO GROSSO | Brasil | 5102504 | 51 | 33 | nan | nan | nan | Pantanal | 2.6 |
| ab1c7112-9e08-3c04-b1fa-278412d94c61 | -17.22063 | -57.44501 | 2024-10-25 05:06:00 | NOAA-20 | CÁCERES | MATO GROSSO | Brasil | 5102504 | 51 | 33 | nan | nan | nan | Pantanal | 3.4 |
| fef75047-2cb9-39a0-bd34-ffa25e9ffc12 | -17.22059 | -57.48985 | 2024-10-25 05:06:00 | NOAA-20 | CÁCERES | MATO GROSSO | Brasil | 5102504 | 51 | 33 | nan | nan | nan | Pantanal | 7.1 |
| a436ce48-f779-324f-b8ad-9fc97038fbee | -17.21838 | -57.48203 | 2024-10-25 05:06:00 | NOAA-20 | CÁCERES | MATO GROSSO | Brasil | 5102504 | 51 | 33 | nan | nan | nan | Pantanal | 5.2 |
| 94c58f1b-d417-3aad-b76f-46e18aa60b57 | -17.21782 | -57.48566 | 2024-10-25 05:06:00 | NOAA-20 | CÁCERES | MATO GROSSO | Brasil | 5102504 | 51 | 33 | nan | nan | nan | Pantanal | 5.2 |
| a4c4c61f-f1d0-3df8-9296-1db3d19be814 | -17.21449 | -57.48511 | 2024-10-25 05:06:00 | NOAA-20 | CÁCERES | MATO GROSSO | Brasil | 5102504 | 51 | 33 | nan | nan | nan | Pantanal | 5.2 |
| 53543fad-af21-3762-bd80-bce830afd3d4 | -17.20507 | -57.47981 | 2024-10-25 05:06:00 | NOAA-20 | CÁCERES | MATO GROSSO | Brasil | 5102504 | 51 | 33 | nan | nan | nan | Pantanal | 3.2 |
| 98795e73-9ea7-3959-a86c-aec72d44bfaa | -17.1436 | -57.46257 | 2024-10-25 05:06:00 | NOAA-20 | CÁCERES | MATO GROSSO | Brasil | 5102504 | 51 | 33 | nan | nan | nan | Pantanal | 0.6 |
| 6839598e-97e2-380c-8076-a1b3d47068e0 | -17.14304 | -57.4662 | 2024-10-25 05:06:00 | NOAA-20 | CÁCERES | MATO GROSSO | Brasil | 5102504 | 51 | 33 | nan | nan | nan | Pantanal | 0.6 |
| f86237b8-9724-3676-8a62-64b60b530a5c | -17.13971 | -57.46565 | 2024-10-25 05:06:00 | NOAA-20 | CÁCERES | MATO GROSSO | Brasil | 5102504 | 51 | 33 | nan | nan | nan | Pantanal | 0.7 |
| 6a9a47f5-64e8-3b4f-a0c5-992169121009 | -17.10419 | -57.47471 | 2024-10-25 05:06:00 | NOAA-20 | CÁCERES | MATO GROSSO | Brasil | 5102504 | 51 | 33 | nan | nan | nan | Pantanal | 2.0 |
| 67b83f78-b349-3b15-9c79-54f98840b293 | -17.10087 | -57.47416 | 2024-10-25 05:06:00 | NOAA-20 | CÁCERES | MATO GROSSO | Brasil | 5102504 | 51 | 33 | nan | nan | nan | Pantanal | 2.0 |
| 78eb6b87-a8fd-36ce-98a9-e788d77abfeb | -17.07757 | -57.47031 | 2024-10-25 05:06:00 | NOAA-20 | CÁCERES | MATO GROSSO | Brasil | 5102504 | 51 | 33 | nan | nan | nan | Pantanal | 2.2 |
| 7f10959f-229c-37eb-88da-361c36084e4a | -17.0759 | -57.48122 | 2024-10-25 05:06:00 | NOAA-20 | CÁCERES | MATO GROSSO | Brasil | 5102504 | 51 | 33 | nan | nan | nan | Pantanal | 3.1 |
| 37dc6260-cd62-37b9-8928-5a6d1ada8add | -17.07424 | -57.46975 | 2024-10-25 05:06:00 | NOAA-20 | CÁCERES | MATO GROSSO | Brasil | 5102504 | 51 | 33 | nan | nan | nan | Pantanal | 2.2 |
| 905591ec-f89c-305f-98d5-30dd2f99805b | -17.06869 | -57.48376 | 2024-10-25 05:06:00 | NOAA-20 | CÁCERES | MATO GROSSO | Brasil | 5102504 | 51 | 33 | nan | nan | nan | Pantanal | 1.5 |
| 4bc14ab4-6b5e-335c-8367-3b97a14744cd | -17.30554 | -57.28635 | 2024-10-25 05:06:00 | NOAA-20 | POCONÉ | MATO GROSSO | Brasil | 5106505 | 51 | 33 | nan | nan | nan | Pantanal | 1.2 |
| 198162db-4149-33be-a822-00a7d2ef8c60 | -17.30499 | -57.29002 | 2024-10-25 05:06:00 | NOAA-20 | POCONÉ | MATO GROSSO | Brasil | 5106505 | 51 | 33 | nan | nan | nan | Pantanal | 1.2 |
| 6558d037-5730-3568-ba53-7ff238ae5b7f | -17.30165 | -57.28947 | 2024-10-25 05:06:00 | NOAA-20 | POCONÉ | MATO GROSSO | Brasil | 5106505 | 51 | 33 | nan | nan | nan | Pantanal | 1.5 |
| eeedb772-8f53-3f02-85f4-fae611fd28c8 | -17.30109 | -57.29315 | 2024-10-25 05:06:00 | NOAA-20 | POCONÉ | MATO GROSSO | Brasil | 5106505 | 51 | 33 | nan | nan | nan | Pantanal | 1.3 |
| 5250f909-40e8-303c-a73c-739c59d61bb6 | -17.29775 | -57.29259 | 2024-10-25 05:06:00 | NOAA-20 | POCONÉ | MATO GROSSO | Brasil | 5106505 | 51 | 33 | nan | nan | nan | Pantanal | 1.3 |
| 8cc33c98-8ba5-3173-a615-5d83c08061ab | -17.2972 | -57.29626 | 2024-10-25 05:06:00 | NOAA-20 | POCONÉ | MATO GROSSO | Brasil | 5106505 | 51 | 33 | nan | nan | nan | Pantanal | 1.3 |
| 3129a8b8-672d-389b-ac70-328e20bb0f01 | -17.29552 | -57.2847 | 2024-10-25 05:06:00 | NOAA-20 | POCONÉ | MATO GROSSO | Brasil | 5106505 | 51 | 33 | nan | nan | nan | Pantanal | 1.3 |
| f6d95869-be4c-37f8-aa1d-c0eb818cf16d | -17.29218 | -57.28415 | 2024-10-25 05:06:00 | NOAA-20 | POCONÉ | MATO GROSSO | Brasil | 5106505 | 51 | 33 | nan | nan | nan | Pantanal | 1.3 |
| 0cb570cd-024a-3e1d-bf5f-597de30afcb1 | -17.28328 | -57.29774 | 2024-10-25 05:06:00 | NOAA-20 | POCONÉ | MATO GROSSO | Brasil | 5106505 | 51 | 33 | nan | nan | nan | Pantanal | 2.0 |
| be48acbd-f11a-3085-989f-203e05ca27bd | -17.28272 | -57.30141 | 2024-10-25 05:06:00 | NOAA-20 | POCONÉ | MATO GROSSO | Brasil | 5106505 | 51 | 33 | nan | nan | nan | Pantanal | 2.0 |
| b02c3ebe-5e8f-3019-8c29-21c714400341 | -17.28083 | -57.29742 | 2024-10-25 05:06:00 | NOAA-20 | POCONÉ | MATO GROSSO | Brasil | 5106505 | 51 | 33 | nan | nan | nan | Pantanal | 2.1 |
| 7c6cfa25-7212-3e03-b89f-57473a73b618 | -17.28027 | -57.30109 | 2024-10-25 05:06:00 | NOAA-20 | POCONÉ | MATO GROSSO | Brasil | 5106505 | 51 | 33 | nan | nan | nan | Pantanal | 2.1 |
| 68566837-854a-37bb-bc1b-420db5317895 | -17.27971 | -57.30476 | 2024-10-25 05:06:00 | NOAA-20 | POCONÉ | MATO GROSSO | Brasil | 5106505 | 51 | 33 | nan | nan | nan | Pantanal | 1.5 |
| 70e71f14-cb38-34a8-b838-047b26e4ed18 | -17.27693 | -57.30054 | 2024-10-25 05:06:00 | NOAA-20 | POCONÉ | MATO GROSSO | Brasil | 5106505 | 51 | 33 | nan | nan | nan | Pantanal | 2.1 |
| 727969c8-bece-3aa4-bf94-ad640f0e610d | -17.26747 | -57.29522 | 2024-10-25 05:06:00 | NOAA-20 | POCONÉ | MATO GROSSO | Brasil | 5106505 | 51 | 33 | nan | nan | nan | Pantanal | 1.4 |
| a0907d16-6bb6-3296-a1b7-5b536927a829 | -17.26691 | -57.29889 | 2024-10-25 05:06:00 | NOAA-20 | POCONÉ | MATO GROSSO | Brasil | 5106505 | 51 | 33 | nan | nan | nan | Pantanal | 1.4 |
| 459ebac6-546c-3a32-9920-39952371aa76 | -17.26443 | -57.512 | 2024-10-25 05:06:00 | NOAA-20 | CÁCERES | MATO GROSSO | Brasil | 5102504 | 51 | 33 | nan | nan | nan | Pantanal | 1.5 |
| 8c199b47-912b-3ca8-bc02-ea009bb07ed1 | -17.26166 | -57.50781 | 2024-10-25 05:06:00 | NOAA-20 | CÁCERES | MATO GROSSO | Brasil | 5102504 | 51 | 33 | nan | nan | nan | Pantanal | 6.9 |
| 2f3d3cd5-4457-3804-b135-b6193f2b8d87 | -17.2611 | -57.51146 | 2024-10-25 05:06:00 | NOAA-20 | CÁCERES | MATO GROSSO | Brasil | 5102504 | 51 | 33 | nan | nan | nan | Pantanal | 6.4 |
| c1547fd8-9984-3c97-9734-3f62830dab6b | -17.25833 | -57.50727 | 2024-10-25 05:06:00 | NOAA-20 | CÁCERES | MATO GROSSO | Brasil | 5102504 | 51 | 33 | nan | nan | nan | Pantanal | 6.9 |
| b5ca2eea-5b4a-3ba2-8998-80afe29fcb4d | -17.25801 | -57.28991 | 2024-10-25 05:06:00 | NOAA-20 | POCONÉ | MATO GROSSO | Brasil | 5106505 | 51 | 33 | nan | nan | nan | Pantanal | 1.0 |
| 6927e059-5f1f-3c4c-be15-78a718c3942f | -17.25778 | -57.5109 | 2024-10-25 05:06:00 | NOAA-20 | CÁCERES | MATO GROSSO | Brasil | 5102504 | 51 | 33 | nan | nan | nan | Pantanal | 6.4 |
| 8759569e-e44d-3a23-9a21-a26ef2c6b16a | -17.25745 | -57.29358 | 2024-10-25 05:06:00 | NOAA-20 | POCONÉ | MATO GROSSO | Brasil | 5106505 | 51 | 33 | nan | nan | nan | Pantanal | 1.0 |
| 340ffc90-c093-3ec4-9186-1c5109c83cae | -17.25445 | -57.51035 | 2024-10-25 05:06:00 | NOAA-20 | CÁCERES | MATO GROSSO | Brasil | 5102504 | 51 | 33 | nan | nan | nan | Pantanal | 3.8 |
| b2d36622-27ea-38a2-b6c9-ff15e53e420d | -17.25389 | -57.514 | 2024-10-25 05:06:00 | NOAA-20 | CÁCERES | MATO GROSSO | Brasil | 5102504 | 51 | 33 | nan | nan | nan | Pantanal | 3.8 |
| 184be700-f4b5-3a9a-8fd0-512e535288a0 | -17.25334 | -57.51764 | 2024-10-25 05:06:00 | NOAA-20 | CÁCERES | MATO GROSSO | Brasil | 5102504 | 51 | 33 | nan | nan | nan | Pantanal | 2.6 |
| 65d8c999-6a64-3fb6-8292-ac1dcb1d263d | -17.25112 | -57.5098 | 2024-10-25 05:06:00 | NOAA-20 | CÁCERES | MATO GROSSO | Brasil | 5102504 | 51 | 33 | nan | nan | nan | Pantanal | 3.8 |
| d6000253-5a8d-36a6-b151-08fa8575adcf | -17.24943 | -57.5021 | 2024-10-25 05:06:00 | NOAA-20 | CÁCERES | MATO GROSSO | Brasil | 5102504 | 51 | 33 | nan | nan | nan | Pantanal | 9.2 |
| 015d764a-52be-3d90-be5d-d848280d6da5 | -17.24719 | -57.51667 | 2024-10-25 05:06:00 | NOAA-20 | CÁCERES | MATO GROSSO | Brasil | 5102504 | 51 | 33 | nan | nan | nan | Pantanal | 1.7 |
| 010cbf71-438d-35c8-be46-dd2c6135a833 | -17.24554 | -57.50519 | 2024-10-25 05:06:00 | NOAA-20 | CÁCERES | MATO GROSSO | Brasil | 5102504 | 51 | 33 | nan | nan | nan | Pantanal | 9.2 |
| a7af22c3-f29a-3338-96a1-e5eb92697932 | -17.23997 | -57.51921 | 2024-10-25 05:06:00 | NOAA-20 | CÁCERES | MATO GROSSO | Brasil | 5102504 | 51 | 33 | nan | nan | nan | Pantanal | 0.7 |
| 589df62a-6238-3914-911f-02d8591903f5 | -17.23886 | -57.52649 | 2024-10-25 05:06:00 | NOAA-20 | CÁCERES | MATO GROSSO | Brasil | 5102504 | 51 | 33 | nan | nan | nan | Pantanal | 3.6 |
| b6a43d85-f0ea-36f3-bb97-405fef2f20de | -17.23609 | -57.5223 | 2024-10-25 05:06:00 | NOAA-20 | CÁCERES | MATO GROSSO | Brasil | 5102504 | 51 | 33 | nan | nan | nan | Pantanal | 3.6 |
| d04e7673-8a2a-3896-b842-7a532c4a120d | -17.23497 | -57.52957 | 2024-10-25 05:06:00 | NOAA-20 | CÁCERES | MATO GROSSO | Brasil | 5102504 | 51 | 33 | nan | nan | nan | Pantanal | 3.7 |
| 452952ff-c97a-3a91-94a8-cedc4012cfd7 | -17.2322 | -57.52538 | 2024-10-25 05:06:00 | NOAA-20 | CÁCERES | MATO GROSSO | Brasil | 5102504 | 51 | 33 | nan | nan | nan | Pantanal | 2.7 |
| aa186d85-1c2e-33f5-aa4f-f3cb563efc29 | -17.23164 | -57.52902 | 2024-10-25 05:06:00 | NOAA-20 | CÁCERES | MATO GROSSO | Brasil | 5102504 | 51 | 33 | nan | nan | nan | Pantanal | 1.6 |
| 36f7dd9a-2987-3b37-afae-a710caae2287 | -17.22849 | -57.32639 | 2024-10-25 05:06:00 | NOAA-20 | POCONÉ | MATO GROSSO | Brasil | 5106505 | 51 | 33 | nan | nan | nan | Pantanal | 1.1 |
| 49eb1599-5d63-3d4f-b09f-dde26b0f00a1 | -17.22831 | -57.52847 | 2024-10-25 05:06:00 | NOAA-20 | CÁCERES | MATO GROSSO | Brasil | 5102504 | 51 | 33 | nan | nan | nan | Pantanal | 1.6 |
| af069068-29d4-31f9-bfc6-13d48edb6d36 | -17.22669 | -57.4946 | 2024-10-25 05:06:00 | NOAA-20 | CÁCERES | MATO GROSSO | Brasil | 5102504 | 51 | 33 | nan | nan | nan | Pantanal | 6.8 |
| 879510ef-4486-3b75-8f82-df7553a11399 | -17.22504 | -57.48312 | 2024-10-25 05:06:00 | NOAA-20 | CÁCERES | MATO GROSSO | Brasil | 5102504 | 51 | 33 | nan | nan | nan | Pantanal | 6.1 |
| e2d07d0a-5314-3f2d-b4bf-e4e22e0e8630 | -17.22392 | -57.49041 | 2024-10-25 05:06:00 | NOAA-20 | CÁCERES | MATO GROSSO | Brasil | 5102504 | 51 | 33 | nan | nan | nan | Pantanal | 7.1 |
| a0cd5cf3-62ff-3715-ac28-7f77d5bee300 | -17.22171 | -57.48257 | 2024-10-25 05:06:00 | NOAA-20 | CÁCERES | MATO GROSSO | Brasil | 5102504 | 51 | 33 | nan | nan | nan | Pantanal | 6.1 |
| 80f44dcf-b635-3f76-8237-192ff7820820 | -17.22115 | -57.48621 | 2024-10-25 05:06:00 | NOAA-20 | CÁCERES | MATO GROSSO | Brasil | 5102504 | 51 | 33 | nan | nan | nan | Pantanal | 6.1 |
| 24433f49-9dc9-3fe9-b8e0-c6b0cdb4b8d3 | -17.21727 | -57.48931 | 2024-10-25 05:06:00 | NOAA-20 | CÁCERES | MATO GROSSO | Brasil | 5102504 | 51 | 33 | nan | nan | nan | Pantanal | 4.3 |
| 4231b644-6c14-38d9-b37c-71fa75646093 | -17.21671 | -57.49295 | 2024-10-25 05:06:00 | NOAA-20 | CÁCERES | MATO GROSSO | Brasil | 5102504 | 51 | 33 | nan | nan | nan | Pantanal | 4.3 |
| 434b9b44-5d0b-35e8-9c6a-3245ee27a96c | -17.21505 | -57.48146 | 2024-10-25 05:06:00 | NOAA-20 | CÁCERES | MATO GROSSO | Brasil | 5102504 | 51 | 33 | nan | nan | nan | Pantanal | 5.2 |
| 6cb0f46e-0931-3c39-afd1-258915dc3656 | -17.21176 | -57.43608 | 2024-10-25 05:06:00 | NOAA-20 | CÁCERES | MATO GROSSO | Brasil | 5102504 | 51 | 33 | nan | nan | nan | Pantanal | 2.7 |
| 9213c496-1235-3631-a46d-1ea24ae9b559 | -17.20174 | -57.47927 | 2024-10-25 05:06:00 | NOAA-20 | CÁCERES | MATO GROSSO | Brasil | 5102504 | 51 | 33 | nan | nan | nan | Pantanal | 3.2 |
| f6cc1f1a-43ae-3cd6-acc0-c4cfcd2615b4 | -17.20068 | -57.30679 | 2024-10-25 05:06:00 | NOAA-20 | POCONÉ | MATO GROSSO | Brasil | 5106505 | 51 | 33 | nan | nan | nan | Pantanal | 1.6 |
| f4ae702d-a686-3ba2-8757-1f7ab8dfb66f | -17.194 | -57.3057 | 2024-10-25 05:06:00 | NOAA-20 | POCONÉ | MATO GROSSO | Brasil | 5106505 | 51 | 33 | nan | nan | nan | Pantanal | 0.3 |
| 81f18ee6-78fb-3798-a5a3-99554f394fa5 | -17.194 | -57.28314 | 2024-10-25 05:06:00 | NOAA-20 | POCONÉ | MATO GROSSO | Brasil | 5106505 | 51 | 33 | nan | nan | nan | Pantanal | 2.6 |
| c3d961ea-5e44-3504-84a7-ff3f9ca41cfb | -17.19344 | -57.28681 | 2024-10-25 05:06:00 | NOAA-20 | POCONÉ | MATO GROSSO | Brasil | 5106505 | 51 | 33 | nan | nan | nan | Pantanal | 2.6 |
| 759c5337-6aa0-37d0-94ad-24af391dfff5 | -17.1901 | -57.28627 | 2024-10-25 05:06:00 | NOAA-20 | POCONÉ | MATO GROSSO | Brasil | 5106505 | 51 | 33 | nan | nan | nan | Pantanal | 2.6 |
| b9a606d4-b726-30c8-ade3-8ea6bb7abc3b | -17.18954 | -57.28993 | 2024-10-25 05:06:00 | NOAA-20 | POCONÉ | MATO GROSSO | Brasil | 5106505 | 51 | 33 | nan | nan | nan | Pantanal | 2.4 |
| 134fbe57-91b1-38a9-84e5-7a93eb00f57a | -17.18899 | -57.2936 | 2024-10-25 05:06:00 | NOAA-20 | POCONÉ | MATO GROSSO | Brasil | 5106505 | 51 | 33 | nan | nan | nan | Pantanal | 2.4 |
| e9c9ea33-b878-34bd-9c91-7fa1817e4bc3 | -17.18676 | -57.28572 | 2024-10-25 05:06:00 | NOAA-20 | POCONÉ | MATO GROSSO | Brasil | 5106505 | 51 | 33 | nan | nan | nan | Pantanal | 1.0 |
| 88ceaebc-5337-3b27-9a7b-8341cb1b6e93 | -17.1862 | -57.28938 | 2024-10-25 05:06:00 | NOAA-20 | POCONÉ | MATO GROSSO | Brasil | 5106505 | 51 | 33 | nan | nan | nan | Pantanal | 2.1 |
| d3ab8f13-95f2-311f-8ecc-480da67909ba | -17.18565 | -57.29305 | 2024-10-25 05:06:00 | NOAA-20 | POCONÉ | MATO GROSSO | Brasil | 5106505 | 51 | 33 | nan | nan | nan | Pantanal | 2.1 |
| a22bbca5-a101-30cf-9ee3-42a6f10a66c6 | -17.18231 | -57.2925 | 2024-10-25 05:06:00 | NOAA-20 | POCONÉ | MATO GROSSO | Brasil | 5106505 | 51 | 33 | nan | nan | nan | Pantanal | 2.1 |
| cd91029f-ec1c-3671-80b9-f5e2b74d4bea | -17.18176 | -57.29617 | 2024-10-25 05:06:00 | NOAA-20 | POCONÉ | MATO GROSSO | Brasil | 5106505 | 51 | 33 | nan | nan | nan | Pantanal | 2.2 |
| d27e2754-adf5-30f8-916c-05468dc91ee9 | -17.17734 | -57.41542 | 2024-10-25 05:06:00 | NOAA-20 | CÁCERES | MATO GROSSO | Brasil | 5102504 | 51 | 33 | nan | nan | nan | Pantanal | 2.7 |
| a1297001-f828-3365-95e7-619b0eaf277a | -17.17345 | -57.41853 | 2024-10-25 05:06:00 | NOAA-20 | CÁCERES | MATO GROSSO | Brasil | 5102504 | 51 | 33 | nan | nan | nan | Pantanal | 0.9 |
| d13e061d-dfc7-33a5-8951-04a83f15d7a6 | -17.06647 | -57.47593 | 2024-10-25 05:06:00 | NOAA-20 | CÁCERES | MATO GROSSO | Brasil | 5102504 | 51 | 33 | nan | nan | nan | Pantanal | 1.8 |
| 2202ea24-8df6-34c8-8720-126146c9a8bb | -17.06426 | -57.46811 | 2024-10-25 05:06:00 | NOAA-20 | CÁCERES | MATO GROSSO | Brasil | 5102504 | 51 | 33 | nan | nan | nan | Pantanal | 3.4 |
| 16df6313-476b-37bd-8702-47226c5b5e7a | -17.06315 | -57.47538 | 2024-10-25 05:06:00 | NOAA-20 | CÁCERES | MATO GROSSO | Brasil | 5102504 | 51 | 33 | nan | nan | nan | Pantanal | 1.4 |
| eda528a5-dcfd-3fb2-8608-6d6ae59a39fa | -17.06149 | -57.44152 | 2024-10-25 05:06:00 | NOAA-20 | CÁCERES | MATO GROSSO | Brasil | 5102504 | 51 | 33 | nan | nan | nan | Pantanal | 2.7 |
| e044baa7-1990-3ce5-b029-80de5d4bba09 | -17.05926 | -57.47847 | 2024-10-25 05:06:00 | NOAA-20 | CÁCERES | MATO GROSSO | Brasil | 5102504 | 51 | 33 | nan | nan | nan | Pantanal | 2.4 |
| b4ff70f7-ec63-3e41-9808-c0c56dd85680 | -17.05871 | -57.48211 | 2024-10-25 05:06:00 | NOAA-20 | CÁCERES | MATO GROSSO | Brasil | 5102504 | 51 | 33 | nan | nan | nan | Pantanal | 2.4 |
| 89105f09-0d9a-3d2c-a2d9-cd068293caa1 | -17.05871 | -57.45973 | 2024-10-25 05:06:00 | NOAA-20 | CÁCERES | MATO GROSSO | Brasil | 5102504 | 51 | 33 | nan | nan | nan | Pantanal | 2.0 |
| 30830f6e-6e9e-3a69-88a0-7a17ec436e39 | -17.05816 | -57.44098 | 2024-10-25 05:06:00 | NOAA-20 | CÁCERES | MATO GROSSO | Brasil | 5102504 | 51 | 33 | nan | nan | nan | Pantanal | 2.7 |
| bf9fe283-3b75-361a-ba3a-36bf28274ff7 | -17.0565 | -57.4519 | 2024-10-25 05:06:00 | NOAA-20 | CÁCERES | MATO GROSSO | Brasil | 5102504 | 51 | 33 | nan | nan | nan | Pantanal | 5.2 |
| 66806816-2b30-314a-8360-dc5d506539ef | -17.05538 | -57.48155 | 2024-10-25 05:06:00 | NOAA-20 | CÁCERES | MATO GROSSO | Brasil | 5102504 | 51 | 33 | nan | nan | nan | Pantanal | 6.6 |
| ce015cd5-fde7-3396-bb1e-e17363e54d25 | -17.05372 | -57.4477 | 2024-10-25 05:06:00 | NOAA-20 | CÁCERES | MATO GROSSO | Brasil | 5102504 | 51 | 33 | nan | nan | nan | Pantanal | 5.0 |
| 9bf3d828-a766-3309-9999-1ac05ec60c57 | -17.05317 | -57.45135 | 2024-10-25 05:06:00 | NOAA-20 | CÁCERES | MATO GROSSO | Brasil | 5102504 | 51 | 33 | nan | nan | nan | Pantanal | 5.0 |
| 175bb38d-6068-33f0-866d-b58f1d25a6da | -17.05261 | -57.47737 | 2024-10-25 05:06:00 | NOAA-20 | CÁCERES | MATO GROSSO | Brasil | 5102504 | 51 | 33 | nan | nan | nan | Pantanal | 6.6 |
| 4ad93738-c79a-327c-8c0e-cf03ff23d31a | -17.05039 | -57.44716 | 2024-10-25 05:06:00 | NOAA-20 | CÁCERES | MATO GROSSO | Brasil | 5102504 | 51 | 33 | nan | nan | nan | Pantanal | 5.0 |


[Clique aqui para ver as próximas entradas](README102.md)
