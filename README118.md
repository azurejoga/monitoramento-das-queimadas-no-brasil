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

## Dados Diários - Página 118

| ID | Latitude | Longitude | Data/Hora GMT | Satélite | Município | Estado | País | Município ID | Estado ID | País ID | Dias sem Chuva | Precipitação | Risco de Fogo | Bioma | FRP |
|----|----------|-----------|---------------|----------|-----------|--------|------|--------------|-----------|---------|----------------|--------------|----------------|-------|-----|
| 1dd87758-8153-398d-87d5-3ed6b056d041 | -16.65479 | -55.91019 | 2024-10-06 05:14:00 | NOAA-21 | BARÃO DE MELGAÇO | MATO GROSSO | Brasil | 5101605 | 51 | 33 | nan | nan | nan | Pantanal | 1.6 |
| a74313d5-f2a0-3d21-bdbc-231f333a734d | -16.65172 | -55.90503 | 2024-10-06 05:14:00 | NOAA-21 | BARÃO DE MELGAÇO | MATO GROSSO | Brasil | 5101605 | 51 | 33 | nan | nan | nan | Pantanal | 1.6 |
| f4afaccc-003a-32f5-871f-af9e933d69f0 | -16.64801 | -55.90446 | 2024-10-06 05:14:00 | NOAA-21 | BARÃO DE MELGAÇO | MATO GROSSO | Brasil | 5101605 | 51 | 33 | nan | nan | nan | Pantanal | 5.6 |
| c79fe8df-81dd-3ca6-8275-8383a8621382 | -16.64429 | -55.9039 | 2024-10-06 05:14:00 | NOAA-21 | BARÃO DE MELGAÇO | MATO GROSSO | Brasil | 5101605 | 51 | 33 | nan | nan | nan | Pantanal | 5.6 |
| 7466af55-14a3-3e6e-8035-97853af8946c | -16.64365 | -55.9085 | 2024-10-06 05:14:00 | NOAA-21 | BARÃO DE MELGAÇO | MATO GROSSO | Brasil | 5101605 | 51 | 33 | nan | nan | nan | Pantanal | 5.6 |
| ee46bd2c-c089-3412-a6d8-1d5038507d39 | -16.64302 | -55.91309 | 2024-10-06 05:14:00 | NOAA-21 | BARÃO DE MELGAÇO | MATO GROSSO | Brasil | 5101605 | 51 | 33 | nan | nan | nan | Pantanal | 2.8 |
| 5104ad41-3574-3da7-a1c2-1ac543cf6935 | -16.6393 | -55.91253 | 2024-10-06 05:14:00 | NOAA-21 | BARÃO DE MELGAÇO | MATO GROSSO | Brasil | 5101605 | 51 | 33 | nan | nan | nan | Pantanal | 3.1 |
| 2e635933-fb44-3b97-ab4e-08870674c00b | -16.62508 | -55.90569 | 2024-10-06 05:14:00 | NOAA-21 | BARÃO DE MELGAÇO | MATO GROSSO | Brasil | 5101605 | 51 | 33 | nan | nan | nan | Pantanal | 5.0 |
| 2579e84a-c757-31ee-a972-e8ee47247b73 | -16.62229 | -56.00787 | 2024-10-06 05:14:00 | NOAA-21 | BARÃO DE MELGAÇO | MATO GROSSO | Brasil | 5101605 | 51 | 33 | nan | nan | nan | Pantanal | 1.9 |
| af97f3c3-ec55-3e52-b3c1-2cc7ae5de344 | -16.62137 | -55.90512 | 2024-10-06 05:14:00 | NOAA-21 | BARÃO DE MELGAÇO | MATO GROSSO | Brasil | 5101605 | 51 | 33 | nan | nan | nan | Pantanal | 5.0 |
| 8b96422b-4d8c-37e3-b70e-997339d4c96f | -16.62074 | -55.90972 | 2024-10-06 05:14:00 | NOAA-21 | BARÃO DE MELGAÇO | MATO GROSSO | Brasil | 5101605 | 51 | 33 | nan | nan | nan | Pantanal | 3.8 |
| 36bd0040-ef8e-3164-becb-72213538b4c9 | -16.6201 | -55.91432 | 2024-10-06 05:14:00 | NOAA-21 | BARÃO DE MELGAÇO | MATO GROSSO | Brasil | 5101605 | 51 | 33 | nan | nan | nan | Pantanal | 3.8 |
| 8aa2d87b-9eeb-38fa-8a05-fc91d6caa1b9 | -16.61947 | -55.91891 | 2024-10-06 05:14:00 | NOAA-21 | BARÃO DE MELGAÇO | MATO GROSSO | Brasil | 5101605 | 51 | 33 | nan | nan | nan | Pantanal | 4.2 |
| 36d933c6-4b3a-3685-adfe-87f727b1fabc | -16.61702 | -55.90916 | 2024-10-06 05:14:00 | NOAA-21 | BARÃO DE MELGAÇO | MATO GROSSO | Brasil | 5101605 | 51 | 33 | nan | nan | nan | Pantanal | 6.5 |
| df26e8a8-27cd-3687-b7cd-b25e6c85c36f | -16.61639 | -55.91375 | 2024-10-06 05:14:00 | NOAA-21 | BARÃO DE MELGAÇO | MATO GROSSO | Brasil | 5101605 | 51 | 33 | nan | nan | nan | Pantanal | 6.5 |
| ae0d7385-eff9-31d8-acd4-a51a48a7d924 | -16.61576 | -55.91834 | 2024-10-06 05:14:00 | NOAA-21 | BARÃO DE MELGAÇO | MATO GROSSO | Brasil | 5101605 | 51 | 33 | nan | nan | nan | Pantanal | 7.1 |
| 0ee2095f-99de-377a-9260-3e5819d01809 | -16.61331 | -55.90859 | 2024-10-06 05:14:00 | NOAA-21 | BARÃO DE MELGAÇO | MATO GROSSO | Brasil | 5101605 | 51 | 33 | nan | nan | nan | Pantanal | 6.5 |
| 2eade467-5342-3a04-a3a7-2c43a3ab7559 | -16.61268 | -55.91319 | 2024-10-06 05:14:00 | NOAA-21 | BARÃO DE MELGAÇO | MATO GROSSO | Brasil | 5101605 | 51 | 33 | nan | nan | nan | Pantanal | 6.5 |
| 17f360a9-f5d4-390b-b8cf-9146d82a2407 | -16.61205 | -55.91777 | 2024-10-06 05:14:00 | NOAA-21 | BARÃO DE MELGAÇO | MATO GROSSO | Brasil | 5101605 | 51 | 33 | nan | nan | nan | Pantanal | 7.1 |
| 968ea2c7-da03-3c91-9b01-3e386023d4b8 | -16.61142 | -55.92236 | 2024-10-06 05:14:00 | NOAA-21 | BARÃO DE MELGAÇO | MATO GROSSO | Brasil | 5101605 | 51 | 33 | nan | nan | nan | Pantanal | 7.1 |
| a0bd67fb-e29a-3f46-94cd-dbcfac4b67e0 | -16.58589 | -56.05321 | 2024-10-06 05:14:00 | NOAA-21 | BARÃO DE MELGAÇO | MATO GROSSO | Brasil | 5101605 | 51 | 33 | nan | nan | nan | Pantanal | 1.5 |
| 65d8c457-3ca2-3ec4-8702-9dbde62c4d8d | -16.58527 | -56.05772 | 2024-10-06 05:14:00 | NOAA-21 | BARÃO DE MELGAÇO | MATO GROSSO | Brasil | 5101605 | 51 | 33 | nan | nan | nan | Pantanal | 1.5 |
| cead3224-a53d-3306-b966-fc4759458290 | -16.6929 | -55.5514 | 2024-10-06 05:14:00 | NOAA-21 | BARÃO DE MELGAÇO | MATO GROSSO | Brasil | 5101605 | 51 | 33 | nan | nan | nan | Pantanal | 1.9 |
| 62915e19-bd12-33fb-869b-c6a48c96f0f8 | -16.68911 | -55.55083 | 2024-10-06 05:14:00 | NOAA-21 | BARÃO DE MELGAÇO | MATO GROSSO | Brasil | 5101605 | 51 | 33 | nan | nan | nan | Pantanal | 2.9 |
| baeb10aa-4e9e-3c27-89ce-a324bcf1a8c4 | -16.68662 | -55.54072 | 2024-10-06 05:14:00 | NOAA-21 | BARÃO DE MELGAÇO | MATO GROSSO | Brasil | 5101605 | 51 | 33 | nan | nan | nan | Pantanal | 2.0 |
| 9f816c54-9c9f-3dcd-9abd-ae3c3a223045 | -19.69685 | -56.49091 | 2024-10-06 05:14:00 | NOAA-21 | AQUIDAUANA | MATO GROSSO DO SUL | Brasil | 5001102 | 50 | 33 | nan | nan | nan | Pantanal | 4.0 |
| aea09681-ed66-37e9-b846-5d38259194ef | -19.6639 | -56.45201 | 2024-10-06 05:14:00 | NOAA-21 | AQUIDAUANA | MATO GROSSO DO SUL | Brasil | 5001102 | 50 | 33 | nan | nan | nan | Pantanal | 1.9 |
| f0e99061-8808-3d1f-814b-42844cf53bd7 | -19.66327 | -56.45676 | 2024-10-06 05:14:00 | NOAA-21 | AQUIDAUANA | MATO GROSSO DO SUL | Brasil | 5001102 | 50 | 33 | nan | nan | nan | Pantanal | 2.3 |
| e7d71bac-4a75-3406-aa32-83daf0e187ac | -19.66264 | -56.4615 | 2024-10-06 05:14:00 | NOAA-21 | AQUIDAUANA | MATO GROSSO DO SUL | Brasil | 5001102 | 50 | 33 | nan | nan | nan | Pantanal | 2.3 |
| c0ecd056-9ed5-3c5f-866c-2be8e963a8a6 | -20.28136 | -56.9375 | 2024-10-06 05:14:00 | NOAA-21 | BODOQUENA | MATO GROSSO DO SUL | Brasil | 5002159 | 50 | 33 | nan | nan | nan | Cerrado | 1.9 |
| c278a548-794f-32c9-8f4a-ad635ea8974e | -20.27833 | -56.9322 | 2024-10-06 05:14:00 | NOAA-21 | BODOQUENA | MATO GROSSO DO SUL | Brasil | 5002159 | 50 | 33 | nan | nan | nan | Cerrado | 1.7 |
| 8574f9a9-e71d-3e67-90bb-1e7c89bd99ba | -16.37485 | -57.75764 | 2024-10-06 05:14:00 | NOAA-21 | CÁCERES | MATO GROSSO | Brasil | 5102504 | 51 | 33 | nan | nan | nan | Pantanal | 0.9 |
| c3d9af28-54a9-3272-982d-27c31bfa2fac | -16.51121 | -57.73586 | 2024-10-06 05:14:00 | NOAA-21 | CÁCERES | MATO GROSSO | Brasil | 5102504 | 51 | 33 | nan | nan | nan | Pantanal | 4.7 |
| 3ff08773-f428-3a09-b202-c0332c11cc8f | -16.51064 | -57.7397 | 2024-10-06 05:14:00 | NOAA-21 | CÁCERES | MATO GROSSO | Brasil | 5102504 | 51 | 33 | nan | nan | nan | Pantanal | 6.7 |
| f2858c8d-2c44-3438-b45b-8e827db790bc | -16.50805 | -57.27483 | 2024-10-06 05:14:00 | NOAA-21 | CÁCERES | MATO GROSSO | Brasil | 5102504 | 51 | 33 | nan | nan | nan | Pantanal | 1.9 |
| 79c406b6-f8e0-3e9f-8ff9-a4fd96c9deff | -16.47882 | -57.29132 | 2024-10-06 05:14:00 | NOAA-21 | CÁCERES | MATO GROSSO | Brasil | 5102504 | 51 | 33 | nan | nan | nan | Pantanal | 1.3 |
| fc3ab5d0-3e51-30df-a467-2a14025ab0fb | -16.47535 | -57.29077 | 2024-10-06 05:14:00 | NOAA-21 | CÁCERES | MATO GROSSO | Brasil | 5102504 | 51 | 33 | nan | nan | nan | Pantanal | 1.3 |
| 6c343a83-9e09-31c5-bc3f-9499606d7eab | -16.4661 | -57.2812 | 2024-10-06 05:14:00 | NOAA-21 | CÁCERES | MATO GROSSO | Brasil | 5102504 | 51 | 33 | nan | nan | nan | Pantanal | 2.0 |
| 49b837b8-429e-3dd6-b123-c9067caa9ccc | -16.46552 | -57.28517 | 2024-10-06 05:14:00 | NOAA-21 | CÁCERES | MATO GROSSO | Brasil | 5102504 | 51 | 33 | nan | nan | nan | Pantanal | 1.9 |
| 05a44c6a-b266-397d-8c3a-41a0bef8469d | -16.4632 | -57.2767 | 2024-10-06 05:14:00 | NOAA-21 | CÁCERES | MATO GROSSO | Brasil | 5102504 | 51 | 33 | nan | nan | nan | Pantanal | 2.0 |
| dbd4dda9-eb83-3932-b52c-f0f918928fea | -16.46263 | -57.28066 | 2024-10-06 05:14:00 | NOAA-21 | CÁCERES | MATO GROSSO | Brasil | 5102504 | 51 | 33 | nan | nan | nan | Pantanal | 2.0 |
| beff2b3b-aac3-3467-936c-44a14977cf30 | -16.45973 | -57.27615 | 2024-10-06 05:14:00 | NOAA-21 | CÁCERES | MATO GROSSO | Brasil | 5102504 | 51 | 33 | nan | nan | nan | Pantanal | 2.4 |
| c94b865c-4d01-31a0-b275-f8ce45a2df0e | -16.45393 | -57.31584 | 2024-10-06 05:14:00 | NOAA-21 | CÁCERES | MATO GROSSO | Brasil | 5102504 | 51 | 33 | nan | nan | nan | Pantanal | 3.1 |
| 60774b3c-b31f-3e98-a169-cf3b67a624c7 | -16.45162 | -57.30736 | 2024-10-06 05:14:00 | NOAA-21 | CÁCERES | MATO GROSSO | Brasil | 5102504 | 51 | 33 | nan | nan | nan | Pantanal | 1.2 |
| 5c8b8c7a-f3fd-354e-8432-41541ac6b803 | -16.45104 | -57.31133 | 2024-10-06 05:14:00 | NOAA-21 | CÁCERES | MATO GROSSO | Brasil | 5102504 | 51 | 33 | nan | nan | nan | Pantanal | 1.2 |
| 306f0a28-5d7f-3e41-9cd9-3d58bca706bf | -16.45046 | -57.3153 | 2024-10-06 05:14:00 | NOAA-21 | CÁCERES | MATO GROSSO | Brasil | 5102504 | 51 | 33 | nan | nan | nan | Pantanal | 3.1 |
| 1cd4556a-afb8-3475-9642-f0201041a690 | -16.44873 | -57.27848 | 2024-10-06 05:14:00 | NOAA-21 | CÁCERES | MATO GROSSO | Brasil | 5102504 | 51 | 33 | nan | nan | nan | Pantanal | 1.9 |
| 2422a1d7-5c5d-31a2-8864-f27d7c3f1b19 | -16.44699 | -57.31475 | 2024-10-06 05:14:00 | NOAA-21 | CÁCERES | MATO GROSSO | Brasil | 5102504 | 51 | 33 | nan | nan | nan | Pantanal | 1.8 |
| 44a84441-c320-3e15-9c86-37ead619b1d9 | -16.44584 | -57.27396 | 2024-10-06 05:14:00 | NOAA-21 | CÁCERES | MATO GROSSO | Brasil | 5102504 | 51 | 33 | nan | nan | nan | Pantanal | 2.0 |
| 1c08f64e-a21a-3dc5-816d-9992d8cf298e | -18.67331 | -57.26479 | 2024-10-06 05:14:00 | NOAA-21 | CORUMBÁ | MATO GROSSO DO SUL | Brasil | 5003207 | 50 | 33 | nan | nan | nan | Pantanal | 2.3 |
| c842d564-3f26-374e-96aa-c34f9b99dcb6 | -16.44526 | -57.27793 | 2024-10-06 05:14:00 | NOAA-21 | CÁCERES | MATO GROSSO | Brasil | 5102504 | 51 | 33 | nan | nan | nan | Pantanal | 2.0 |
| 594f4ef0-984c-30ea-83e9-fae451fb2628 | -16.44468 | -57.2819 | 2024-10-06 05:14:00 | NOAA-21 | CÁCERES | MATO GROSSO | Brasil | 5102504 | 51 | 33 | nan | nan | nan | Pantanal | 1.5 |
| bc4b4c49-9d02-3a89-94e9-6921add06355 | -16.44179 | -57.27738 | 2024-10-06 05:14:00 | NOAA-21 | CÁCERES | MATO GROSSO | Brasil | 5102504 | 51 | 33 | nan | nan | nan | Pantanal | 2.0 |
| 62e48816-2d49-35b3-98c6-0f8712f810be | -16.44121 | -57.28135 | 2024-10-06 05:14:00 | NOAA-21 | CÁCERES | MATO GROSSO | Brasil | 5102504 | 51 | 33 | nan | nan | nan | Pantanal | 1.5 |
| 714cf53c-a714-3993-a52e-c7a792ead0e2 | -16.44005 | -57.28928 | 2024-10-06 05:14:00 | NOAA-21 | CÁCERES | MATO GROSSO | Brasil | 5102504 | 51 | 33 | nan | nan | nan | Pantanal | 1.3 |
| bc1e5b5a-d311-3ded-a530-df9f4645f199 | -16.43658 | -57.28874 | 2024-10-06 05:14:00 | NOAA-21 | CÁCERES | MATO GROSSO | Brasil | 5102504 | 51 | 33 | nan | nan | nan | Pantanal | 2.4 |
| d27d7c45-ed0d-3331-bb19-9b85d0fdd6f2 | -16.436 | -57.29271 | 2024-10-06 05:14:00 | NOAA-21 | CÁCERES | MATO GROSSO | Brasil | 5102504 | 51 | 33 | nan | nan | nan | Pantanal | 2.4 |
| 4116959b-bdc4-37cd-ad5d-1c0f3d7c0f2a | -16.43484 | -57.27629 | 2024-10-06 05:14:00 | NOAA-21 | CÁCERES | MATO GROSSO | Brasil | 5102504 | 51 | 33 | nan | nan | nan | Pantanal | 2.9 |
| 735fd6df-3c28-3c93-9972-3c78437f683f | -16.43427 | -57.30463 | 2024-10-06 05:14:00 | NOAA-21 | CÁCERES | MATO GROSSO | Brasil | 5102504 | 51 | 33 | nan | nan | nan | Pantanal | 1.4 |
| 028c429f-f0ec-3f4b-b243-00cb60d1d015 | -16.43369 | -57.3086 | 2024-10-06 05:14:00 | NOAA-21 | CÁCERES | MATO GROSSO | Brasil | 5102504 | 51 | 33 | nan | nan | nan | Pantanal | 1.4 |
| 033ae3da-d737-3eda-8f3e-bfa27e6acba1 | -16.43369 | -57.28423 | 2024-10-06 05:14:00 | NOAA-21 | CÁCERES | MATO GROSSO | Brasil | 5102504 | 51 | 33 | nan | nan | nan | Pantanal | 2.3 |
| 27f80570-6c99-3c3e-a36a-a051575d4303 | -16.43136 | -57.27574 | 2024-10-06 05:14:00 | NOAA-21 | CÁCERES | MATO GROSSO | Brasil | 5102504 | 51 | 33 | nan | nan | nan | Pantanal | 1.9 |
| 160b168d-a538-377b-baa6-4e02ed435891 | -16.42851 | -57.34424 | 2024-10-06 05:14:00 | NOAA-21 | CÁCERES | MATO GROSSO | Brasil | 5102504 | 51 | 33 | nan | nan | nan | Pantanal | 1.3 |
| 0c1fa5aa-00b2-36b1-bf9f-a3e37552898d | -16.42793 | -57.34818 | 2024-10-06 05:14:00 | NOAA-21 | CÁCERES | MATO GROSSO | Brasil | 5102504 | 51 | 33 | nan | nan | nan | Pantanal | 1.3 |
| 406c816f-dd7c-3df2-b452-393ac04192f7 | -16.42504 | -57.34369 | 2024-10-06 05:14:00 | NOAA-21 | CÁCERES | MATO GROSSO | Brasil | 5102504 | 51 | 33 | nan | nan | nan | Pantanal | 1.3 |
| 743ca39c-7343-385c-b217-71fe1934a491 | -16.42447 | -57.34763 | 2024-10-06 05:14:00 | NOAA-21 | CÁCERES | MATO GROSSO | Brasil | 5102504 | 51 | 33 | nan | nan | nan | Pantanal | 1.3 |
| d95fc0f2-284f-3db4-85d1-7376b53fd9e2 | -16.41295 | -57.37814 | 2024-10-06 05:14:00 | NOAA-21 | CÁCERES | MATO GROSSO | Brasil | 5102504 | 51 | 33 | nan | nan | nan | Pantanal | 1.9 |
| d0767ab0-fe88-31cd-bdeb-785fbc4e5bfe | -16.41238 | -57.38208 | 2024-10-06 05:14:00 | NOAA-21 | CÁCERES | MATO GROSSO | Brasil | 5102504 | 51 | 33 | nan | nan | nan | Pantanal | 2.6 |
| a182c133-887a-343d-b1a2-d46ac3f08803 | -16.41061 | -57.34547 | 2024-10-06 05:14:00 | NOAA-21 | CÁCERES | MATO GROSSO | Brasil | 5102504 | 51 | 33 | nan | nan | nan | Pantanal | 1.6 |
| b93551eb-adf6-37f0-8cd9-8a017002168e | -16.41004 | -57.34942 | 2024-10-06 05:14:00 | NOAA-21 | CÁCERES | MATO GROSSO | Brasil | 5102504 | 51 | 33 | nan | nan | nan | Pantanal | 1.9 |
| a170e07b-8d6c-334c-83ae-583b38446c86 | -16.40949 | -57.37759 | 2024-10-06 05:14:00 | NOAA-21 | CÁCERES | MATO GROSSO | Brasil | 5102504 | 51 | 33 | nan | nan | nan | Pantanal | 1.9 |
| 23f27016-8f4d-309d-9567-1905c01ed81b | -16.40603 | -57.37704 | 2024-10-06 05:14:00 | NOAA-21 | CÁCERES | MATO GROSSO | Brasil | 5102504 | 51 | 33 | nan | nan | nan | Pantanal | 1.9 |
| 1cd23ece-2af6-3a8f-bbb7-a61730f14a9d | -16.40257 | -57.3765 | 2024-10-06 05:14:00 | NOAA-21 | CÁCERES | MATO GROSSO | Brasil | 5102504 | 51 | 33 | nan | nan | nan | Pantanal | 3.5 |
| 33ab8f4a-7c96-3e6c-be62-41131dee4c9c | -16.40254 | -57.35229 | 2024-10-06 05:14:00 | NOAA-21 | CÁCERES | MATO GROSSO | Brasil | 5102504 | 51 | 33 | nan | nan | nan | Pantanal | 1.8 |
| ac531edb-0697-3a9d-a2d3-50530026b157 | -16.39566 | -57.37542 | 2024-10-06 05:14:00 | NOAA-21 | CÁCERES | MATO GROSSO | Brasil | 5102504 | 51 | 33 | nan | nan | nan | Pantanal | 2.3 |
| 47805bdd-5296-3679-a0bb-5d99d38600d3 | -16.39505 | -57.35516 | 2024-10-06 05:14:00 | NOAA-21 | CÁCERES | MATO GROSSO | Brasil | 5102504 | 51 | 33 | nan | nan | nan | Pantanal | 1.6 |
| 02d9733b-4a78-3c45-aa44-f1384479fb6c | -16.39277 | -57.37093 | 2024-10-06 05:14:00 | NOAA-21 | CÁCERES | MATO GROSSO | Brasil | 5102504 | 51 | 33 | nan | nan | nan | Pantanal | 2.3 |
| a75a1183-50d9-3dc0-99a2-fd04159fe8d4 | -18.67034 | -57.26001 | 2024-10-06 05:14:00 | NOAA-21 | CORUMBÁ | MATO GROSSO DO SUL | Brasil | 5003207 | 50 | 33 | nan | nan | nan | Pantanal | 2.3 |
| 4addc259-77ff-3d46-abf8-f7667f1e1219 | -16.38755 | -57.35802 | 2024-10-06 05:14:00 | NOAA-21 | CÁCERES | MATO GROSSO | Brasil | 5102504 | 51 | 33 | nan | nan | nan | Pantanal | 1.2 |
| 984e4481-139d-3f81-b52e-ab0868b5f257 | -16.38585 | -57.36985 | 2024-10-06 05:14:00 | NOAA-21 | CÁCERES | MATO GROSSO | Brasil | 5102504 | 51 | 33 | nan | nan | nan | Pantanal | 3.7 |
| 9d497846-d681-3335-9530-d9f1952dd8a1 | -16.38125 | -57.37719 | 2024-10-06 05:14:00 | NOAA-21 | CÁCERES | MATO GROSSO | Brasil | 5102504 | 51 | 33 | nan | nan | nan | Pantanal | 3.7 |
| 1e174e1e-b3c3-3bec-a371-81756858fa55 | -16.38068 | -57.38113 | 2024-10-06 05:14:00 | NOAA-21 | CÁCERES | MATO GROSSO | Brasil | 5102504 | 51 | 33 | nan | nan | nan | Pantanal | 3.7 |
| 0794dc47-1667-3e73-bcdf-547704c4ef48 | -16.38011 | -57.38507 | 2024-10-06 05:14:00 | NOAA-21 | CÁCERES | MATO GROSSO | Brasil | 5102504 | 51 | 33 | nan | nan | nan | Pantanal | 3.2 |
| 3a8cd790-412f-3141-bf4e-de76e2a5a2ed | -16.37893 | -57.36877 | 2024-10-06 05:14:00 | NOAA-21 | CÁCERES | MATO GROSSO | Brasil | 5102504 | 51 | 33 | nan | nan | nan | Pantanal | 6.8 |
| 9d5b9461-0f83-3cc9-a262-da83133e2c77 | -16.37836 | -57.37271 | 2024-10-06 05:14:00 | NOAA-21 | CÁCERES | MATO GROSSO | Brasil | 5102504 | 51 | 33 | nan | nan | nan | Pantanal | 6.8 |
| eed8f3ae-b988-3279-9083-65af5f5f1d88 | -16.37779 | -57.37665 | 2024-10-06 05:14:00 | NOAA-21 | CÁCERES | MATO GROSSO | Brasil | 5102504 | 51 | 33 | nan | nan | nan | Pantanal | 3.7 |
| dca0d153-9aea-3b2d-b42b-19fccd3a181f | -16.37722 | -57.38059 | 2024-10-06 05:14:00 | NOAA-21 | CÁCERES | MATO GROSSO | Brasil | 5102504 | 51 | 33 | nan | nan | nan | Pantanal | 3.7 |
| 7d5080f0-3303-3502-a109-1bc493214522 | -16.37546 | -57.36823 | 2024-10-06 05:14:00 | NOAA-21 | CÁCERES | MATO GROSSO | Brasil | 5102504 | 51 | 33 | nan | nan | nan | Pantanal | 6.1 |
| 14a22305-430b-396d-9859-ae6928195e41 | -16.3749 | -57.37217 | 2024-10-06 05:14:00 | NOAA-21 | CÁCERES | MATO GROSSO | Brasil | 5102504 | 51 | 33 | nan | nan | nan | Pantanal | 6.1 |
| a6044644-cf41-30b9-b587-6bb091b5d97c | -16.3691 | -57.7019 | 2024-10-06 05:14:00 | NOAA-21 | CÁCERES | MATO GROSSO | Brasil | 5102504 | 51 | 33 | nan | nan | nan | Pantanal | 1.3 |
| 068491fd-a016-3e72-ba1f-9de941f8c43d | -16.57883 | -57.15484 | 2024-10-06 05:14:00 | NOAA-21 | POCONÉ | MATO GROSSO | Brasil | 5106505 | 51 | 33 | nan | nan | nan | Pantanal | 2.7 |
| 32a71b4e-287f-37be-9451-842453720e36 | -16.57822 | -57.20813 | 2024-10-06 05:14:00 | NOAA-21 | POCONÉ | MATO GROSSO | Brasil | 5106505 | 51 | 33 | nan | nan | nan | Pantanal | 1.0 |
| 38011eeb-5d84-3cde-a8e3-7a77aac694d1 | -16.57475 | -57.15829 | 2024-10-06 05:14:00 | NOAA-21 | POCONÉ | MATO GROSSO | Brasil | 5106505 | 51 | 33 | nan | nan | nan | Pantanal | 2.7 |
| f17a43a9-f379-3ed6-894d-76769c3af2a7 | -16.57415 | -57.2116 | 2024-10-06 05:14:00 | NOAA-21 | POCONÉ | MATO GROSSO | Brasil | 5106505 | 51 | 33 | nan | nan | nan | Pantanal | 1.5 |
| 17d45b10-d907-3fa2-9fe5-b9570bdf587d | -16.57357 | -57.21561 | 2024-10-06 05:14:00 | NOAA-21 | POCONÉ | MATO GROSSO | Brasil | 5106505 | 51 | 33 | nan | nan | nan | Pantanal | 1.5 |
| 22789b79-e10b-317d-8518-3516f76e49e5 | -16.57125 | -57.20704 | 2024-10-06 05:14:00 | NOAA-21 | POCONÉ | MATO GROSSO | Brasil | 5106505 | 51 | 33 | nan | nan | nan | Pantanal | 1.2 |
| 8ba2ec6b-54b4-382f-8cc9-de3a355202c9 | -16.57067 | -57.16174 | 2024-10-06 05:14:00 | NOAA-21 | POCONÉ | MATO GROSSO | Brasil | 5106505 | 51 | 33 | nan | nan | nan | Pantanal | 1.9 |
| f81f0456-337e-391d-bfd5-99c24e705a2a | -16.57066 | -57.21105 | 2024-10-06 05:14:00 | NOAA-21 | POCONÉ | MATO GROSSO | Brasil | 5106505 | 51 | 33 | nan | nan | nan | Pantanal | 1.3 |
| 2b03869a-511c-31f5-b157-704754bbcf92 | -16.5701 | -57.16576 | 2024-10-06 05:14:00 | NOAA-21 | POCONÉ | MATO GROSSO | Brasil | 5106505 | 51 | 33 | nan | nan | nan | Pantanal | 1.9 |
| 16521538-5586-3ec9-a7a5-292010942bdb | -16.57008 | -57.21507 | 2024-10-06 05:14:00 | NOAA-21 | POCONÉ | MATO GROSSO | Brasil | 5106505 | 51 | 33 | nan | nan | nan | Pantanal | 1.3 |


[Clique aqui para ver as próximas entradas](README119.md)
