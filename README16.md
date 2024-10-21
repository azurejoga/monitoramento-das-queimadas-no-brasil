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

## Dados Diários - Página 16

| ID | Latitude | Longitude | Data/Hora GMT | Satélite | Município | Estado | País | Município ID | Estado ID | País ID | Dias sem Chuva | Precipitação | Risco de Fogo | Bioma | FRP |
|----|----------|-----------|---------------|----------|-----------|--------|------|--------------|-----------|---------|----------------|--------------|----------------|-------|-----|
| 5e3740ae-0001-3106-941c-be486011430b | -12.5046 | -63.2714 | 2024-10-21 01:32:29 | METOP-C | SÃO FRANCISCO DO GUAPORÉ | RONDÔNIA | Brasil | 1101492 | 11 | 33 | nan | nan | nan | Amazônia | nan |
| fc6a9711-000a-37cf-ada5-0227ce67fabf | -12.5166 | -63.279701 | 2024-10-21 01:32:29 | METOP-C | SÃO FRANCISCO DO GUAPORÉ | RONDÔNIA | Brasil | 1101492 | 11 | 33 | nan | nan | nan | Amazônia | nan |
| 138b6ee9-f809-3490-8866-5cdfaef67b00 | -12.4876 | -63.189602 | 2024-10-21 01:32:29 | METOP-C | SÃO FRANCISCO DO GUAPORÉ | RONDÔNIA | Brasil | 1101492 | 11 | 33 | nan | nan | nan | Amazônia | nan |
| 4c87e748-91cc-3d24-b02a-0ebf9f6bac99 | -12.4853 | -63.032398 | 2024-10-21 01:32:29 | METOP-C | SÃO FRANCISCO DO GUAPORÉ | RONDÔNIA | Brasil | 1101492 | 11 | 33 | nan | nan | nan | Amazônia | nan |
| dc8c58b8-3add-3750-b54a-fe930e293751 | -12.4874 | -63.0424 | 2024-10-21 01:32:29 | METOP-C | SÃO FRANCISCO DO GUAPORÉ | RONDÔNIA | Brasil | 1101492 | 11 | 33 | nan | nan | nan | Amazônia | nan |
| 084cdae1-4959-3d5f-badb-179d7e8e6114 | -12.4952 | -63.177399 | 2024-10-21 01:32:29 | METOP-C | SÃO FRANCISCO DO GUAPORÉ | RONDÔNIA | Brasil | 1101492 | 11 | 33 | nan | nan | nan | Amazônia | nan |
| 1b339a64-9b48-30ce-8f9f-e7a9e2eeeb4b | -12.4974 | -63.1875 | 2024-10-21 01:32:29 | METOP-C | SÃO FRANCISCO DO GUAPORÉ | RONDÔNIA | Brasil | 1101492 | 11 | 33 | nan | nan | nan | Amazônia | nan |
| 8e13eb51-6683-3737-840b-2a34ea3b5116 | -12.5144 | -63.269402 | 2024-10-21 01:32:29 | METOP-C | SÃO FRANCISCO DO GUAPORÉ | RONDÔNIA | Brasil | 1101492 | 11 | 33 | nan | nan | nan | Amazônia | nan |
| 3826e916-2ebd-3fdb-8941-5a31bfda4a52 | -12.4774 | -63.287998 | 2024-10-21 01:32:30 | METOP-C | SÃO FRANCISCO DO GUAPORÉ | RONDÔNIA | Brasil | 1101492 | 11 | 33 | nan | nan | nan | Amazônia | nan |
| fda76f4c-1662-3331-93bc-78c598ffb0c2 | -12.4266 | -63.044899 | 2024-10-21 01:32:30 | METOP-C | SÃO FRANCISCO DO GUAPORÉ | RONDÔNIA | Brasil | 1101492 | 11 | 33 | nan | nan | nan | Amazônia | nan |
| c0ef4e17-1213-375b-b826-bf181ea6bd01 | -12.4365 | -63.1898 | 2024-10-21 01:32:30 | METOP-C | SÃO FRANCISCO DO GUAPORÉ | RONDÔNIA | Brasil | 1101492 | 11 | 33 | nan | nan | nan | Amazônia | nan |
| f39d0b3b-bc0d-358a-81ea-fcfbe77eab55 | -12.4029 | -63.029099 | 2024-10-21 01:32:30 | METOP-C | SÃO FRANCISCO DO GUAPORÉ | RONDÔNIA | Brasil | 1101492 | 11 | 33 | nan | nan | nan | Amazônia | nan |
| 8245a884-ad46-3d16-bd29-77693376d28b | -12.4698 | -63.300301 | 2024-10-21 01:32:30 | METOP-C | SÃO FRANCISCO DO GUAPORÉ | RONDÔNIA | Brasil | 1101492 | 11 | 33 | nan | nan | nan | Amazônia | nan |
| 46faf30e-d648-3428-8708-80ebcf97baa0 | -12.4676 | -63.290001 | 2024-10-21 01:32:30 | METOP-C | SÃO FRANCISCO DO GUAPORÉ | RONDÔNIA | Brasil | 1101492 | 11 | 33 | nan | nan | nan | Amazônia | nan |
| 82316415-c55f-3810-ba40-2d67a69e60a8 | -12.4655 | -63.279701 | 2024-10-21 01:32:30 | METOP-C | SÃO FRANCISCO DO GUAPORÉ | RONDÔNIA | Brasil | 1101492 | 11 | 33 | nan | nan | nan | Amazônia | nan |
| 499d9c8c-bb8d-3060-9a93-95d8bbbd11a3 | -12.4484 | -63.1978 | 2024-10-21 01:32:30 | METOP-C | SÃO FRANCISCO DO GUAPORÉ | RONDÔNIA | Brasil | 1101492 | 11 | 33 | nan | nan | nan | Amazônia | nan |
| 93e7ada8-545b-336d-b9bd-b8e0666b2553 | -12.4463 | -63.187698 | 2024-10-21 01:32:30 | METOP-C | SÃO FRANCISCO DO GUAPORÉ | RONDÔNIA | Brasil | 1101492 | 11 | 33 | nan | nan | nan | Amazônia | nan |
| 98f5e2fe-c75b-3216-aff0-c658643a41f7 | -12.4441 | -63.177502 | 2024-10-21 01:32:30 | METOP-C | SÃO FRANCISCO DO GUAPORÉ | RONDÔNIA | Brasil | 1101492 | 11 | 33 | nan | nan | nan | Amazônia | nan |
| 5d60f6d4-2081-3a64-a86b-159c43942d93 | -12.4168 | -63.046902 | 2024-10-21 01:32:30 | METOP-C | SÃO FRANCISCO DO GUAPORÉ | RONDÔNIA | Brasil | 1101492 | 11 | 33 | nan | nan | nan | Amazônia | nan |
| 3ff9ce89-a447-38f4-8e20-8067c691c8d4 | -12.4817 | -63.308601 | 2024-10-21 01:32:30 | METOP-C | SÃO FRANCISCO DO GUAPORÉ | RONDÔNIA | Brasil | 1101492 | 11 | 33 | nan | nan | nan | Amazônia | nan |
| 9d3c2239-0dba-37e9-be87-4312c4692aea | -12.4796 | -63.298302 | 2024-10-21 01:32:30 | METOP-C | SÃO FRANCISCO DO GUAPORÉ | RONDÔNIA | Brasil | 1101492 | 11 | 33 | nan | nan | nan | Amazônia | nan |
| a9b4c687-5e5c-372e-908f-354fe5ae93c5 | -10.7981 | -58.610001 | 2024-10-21 01:32:40 | METOP-C | CASTANHEIRA | MATO GROSSO | Brasil | 5102850 | 51 | 33 | nan | nan | nan | Amazônia | nan |
| b759b765-1363-3981-82aa-a0dcd0d9c9f9 | -10.7965 | -58.6031 | 2024-10-21 01:32:40 | METOP-C | CASTANHEIRA | MATO GROSSO | Brasil | 5102850 | 51 | 33 | nan | nan | nan | Amazônia | nan |
| 38db38b8-9ac2-3f6b-9066-5accab8991b0 | -12.6819 | -62.897598 | 2024-10-21 01:32:41 | METOP-C | SÃO FRANCISCO DO GUAPORÉ | RONDÔNIA | Brasil | 1101492 | 11 | 33 | nan | nan | nan | Amazônia | nan |
| ff08f23b-48d9-3d5a-8702-9c9ba4466e41 | -12.4776 | -63.044498 | 2024-10-21 01:32:45 | METOP-C | SÃO FRANCISCO DO GUAPORÉ | RONDÔNIA | Brasil | 1101492 | 11 | 33 | nan | nan | nan | Amazônia | nan |
| ff4f6da4-3445-312d-ab0f-002bbbf171f8 | -12.4755 | -63.0345 | 2024-10-21 01:32:45 | METOP-C | SÃO FRANCISCO DO GUAPORÉ | RONDÔNIA | Brasil | 1101492 | 11 | 33 | nan | nan | nan | Amazônia | nan |
| 317e7ce3-cbd6-355f-affc-0c71109930f4 | -12.4972 | -63.040298 | 2024-10-21 01:32:45 | METOP-C | SÃO FRANCISCO DO GUAPORÉ | RONDÔNIA | Brasil | 1101492 | 11 | 33 | nan | nan | nan | Amazônia | nan |
| bdfa3281-c32d-3c8d-b905-1c9b3c87b16b | -12.4951 | -63.0303 | 2024-10-21 01:32:45 | METOP-C | SÃO FRANCISCO DO GUAPORÉ | RONDÔNIA | Brasil | 1101492 | 11 | 33 | nan | nan | nan | Amazônia | nan |
| 62606eac-4f7d-3909-955f-8443e718dfa4 | -12.493 | -63.020302 | 2024-10-21 01:32:45 | METOP-C | SÃO FRANCISCO DO GUAPORÉ | RONDÔNIA | Brasil | 1101492 | 11 | 33 | nan | nan | nan | Amazônia | nan |
| f520e0fd-f54c-3537-b9a3-9b820c795215 | -11.973 | -63.513599 | 2024-10-21 01:32:55 | METOP-C | SÃO FRANCISCO DO GUAPORÉ | RONDÔNIA | Brasil | 1101492 | 11 | 33 | nan | nan | nan | Amazônia | nan |
| 0a8c3d2d-0b99-3234-b0b4-fd80df14e156 | -11.9708 | -63.503101 | 2024-10-21 01:32:55 | METOP-C | SÃO FRANCISCO DO GUAPORÉ | RONDÔNIA | Brasil | 1101492 | 11 | 33 | nan | nan | nan | Amazônia | nan |
| c7b4dcb6-e131-349b-b73d-a0e09a65509f | -9.7248 | -64.719299 | 2024-10-21 01:33:36 | METOP-C | PORTO VELHO | RONDÔNIA | Brasil | 1100205 | 11 | 33 | nan | nan | nan | Amazônia | nan |
| 2ae38636-755b-31d0-a926-4c0434d081af | -9.7224 | -64.707802 | 2024-10-21 01:33:36 | METOP-C | PORTO VELHO | RONDÔNIA | Brasil | 1100205 | 11 | 33 | nan | nan | nan | Amazônia | nan |
| a993b796-bfa8-3ebc-bc66-5e7d0b1b7015 | -9.7346 | -64.717201 | 2024-10-21 01:33:36 | METOP-C | PORTO VELHO | RONDÔNIA | Brasil | 1100205 | 11 | 33 | nan | nan | nan | Amazônia | nan |
| b94ca2b3-725c-30c7-a7a8-7b47e10db446 | -9.3294 | -66.476601 | 2024-10-21 01:33:48 | METOP-C | LÁBREA | AMAZONAS | Brasil | 1302405 | 13 | 33 | nan | nan | nan | Amazônia | nan |
| ec049908-d81a-3916-a102-f49b0a13b43b | -9.3263 | -66.4617 | 2024-10-21 01:33:48 | METOP-C | LÁBREA | AMAZONAS | Brasil | 1302405 | 13 | 33 | nan | nan | nan | Amazônia | nan |
| 1c7a0d21-0b58-30e9-9e83-7bcd493eaea2 | -9.3391 | -66.474602 | 2024-10-21 01:33:48 | METOP-C | LÁBREA | AMAZONAS | Brasil | 1302405 | 13 | 33 | nan | nan | nan | Amazônia | nan |
| c400fd37-d593-3c3f-827d-c6d09ebde91f | -3.1809 | -50.824402 | 2024-10-21 01:34:13 | METOP-C | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| 49ba9578-603e-33a9-b59f-32c7680ab564 | -3.1755 | -50.802399 | 2024-10-21 01:34:13 | METOP-C | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| 2ecb9f23-d307-3326-b89e-9acf6ac806f7 | -3.1701 | -50.780201 | 2024-10-21 01:34:13 | METOP-C | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| 92e8155b-84d8-3a09-a730-d5017a2c828e | -3.1852 | -50.800098 | 2024-10-21 01:34:13 | METOP-C | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| 94e533dd-6a74-3619-94f6-44085110f547 | -3.1798 | -50.777901 | 2024-10-21 01:34:13 | METOP-C | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| 170b3fdf-652b-3b66-82ff-da6b9a667ce9 | -3.7426 | -53.407001 | 2024-10-21 01:34:14 | METOP-C | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| 08eabda1-ccce-3d70-a8e9-ec1eb0ec932c | -3.7391 | -53.392601 | 2024-10-21 01:34:14 | METOP-C | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| ca6ab141-a3bb-3870-bbc1-150748a0e83b | -2.7516 | -49.314201 | 2024-10-21 01:34:14 | METOP-C | MOJU | PARÁ | Brasil | 1504703 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| 8fef1ff8-f58d-34fc-991e-af1856e54e86 | -2.7447 | -49.285702 | 2024-10-21 01:34:14 | METOP-C | MOJU | PARÁ | Brasil | 1504703 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| 903fb992-de2d-34c9-98cc-71d6cd71915b | -2.7351 | -49.287998 | 2024-10-21 01:34:15 | METOP-C | MOJU | PARÁ | Brasil | 1504703 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| dc3dc58d-b3c7-3dae-829b-ee7601f32d65 | -3.0565 | -51.282001 | 2024-10-21 01:34:17 | METOP-C | ANAPU | PARÁ | Brasil | 1500859 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| b42f2067-586b-3df9-a5be-691b8716f52e | -2.4571 | -49.1077 | 2024-10-21 01:34:18 | METOP-C | MOJU | PARÁ | Brasil | 1504703 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| 58a78539-6816-3949-abf7-7029228ea835 | -2.4475 | -49.1101 | 2024-10-21 01:34:19 | METOP-C | MOJU | PARÁ | Brasil | 1504703 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| 11f55d6a-9c41-32fe-ac34-03b03fac52be | -2.4403 | -49.0802 | 2024-10-21 01:34:19 | METOP-C | MOJU | PARÁ | Brasil | 1504703 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| 5036b471-88a3-3adc-b853-dc242a0bdebc | -2.7616 | -51.373798 | 2024-10-21 01:34:22 | METOP-C | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| aea931cf-4223-3c96-b24f-d24695b467ce | -2.7567 | -51.353298 | 2024-10-21 01:34:22 | METOP-C | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| e4bad700-2bd5-343c-9568-3a61e3fa18be | -2.7713 | -51.371498 | 2024-10-21 01:34:22 | METOP-C | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| d75f6168-92d6-3855-8bec-79119373185b | -2.7664 | -51.351002 | 2024-10-21 01:34:22 | METOP-C | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| 52d6ff27-05c0-3be4-97d8-5b98d4255f83 | -3.235 | -53.777599 | 2024-10-21 01:34:24 | METOP-C | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| fecd6ae4-5652-3a9a-806e-df6d5a20b1b5 | -3.0795 | -53.125801 | 2024-10-21 01:34:24 | METOP-C | MEDICILÂNDIA | PARÁ | Brasil | 1504455 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| 1960ecff-12c5-34ac-973d-e240ef6b43ad | -3.0759 | -53.1105 | 2024-10-21 01:34:24 | METOP-C | MEDICILÂNDIA | PARÁ | Brasil | 1504455 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| ec33be21-92d1-356f-97f7-c18b706fe9bf | -2.9603 | -53.056 | 2024-10-21 01:34:26 | METOP-C | MEDICILÂNDIA | PARÁ | Brasil | 1504455 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| bfcfd974-2c07-3119-959a-07170c18ab7e | -2.9566 | -53.040501 | 2024-10-21 01:34:26 | METOP-C | MEDICILÂNDIA | PARÁ | Brasil | 1504455 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| 78f52700-4f6e-3ccd-afd8-f1269f00fd1c | -2.97 | -53.053699 | 2024-10-21 01:34:26 | METOP-C | MEDICILÂNDIA | PARÁ | Brasil | 1504455 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| 05bd95f2-21c5-3795-9700-ffaccb8e8e6c | -2.9663 | -53.0382 | 2024-10-21 01:34:26 | METOP-C | MEDICILÂNDIA | PARÁ | Brasil | 1504455 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| c46c6e76-560d-3471-9a12-5618b018d7cc | -3.4433 | -55.393799 | 2024-10-21 01:34:27 | METOP-C | AVEIRO | PARÁ | Brasil | 1501006 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| 6e7227f7-8ad2-3d38-a507-259a71e3907c | -3.0642 | -54.183399 | 2024-10-21 01:34:28 | METOP-C | SANTARÉM | PARÁ | Brasil | 1506807 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| 24e49669-f023-3ed0-90e3-708781ceca8b | -3.0611 | -54.170399 | 2024-10-21 01:34:28 | METOP-C | SANTARÉM | PARÁ | Brasil | 1506807 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| 440faaf0-6e4e-3a82-a826-29934f545277 | -3.058 | -54.157398 | 2024-10-21 01:34:28 | METOP-C | SANTARÉM | PARÁ | Brasil | 1506807 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| e09e0b07-2372-3ed0-9f39-d4ab217032b1 | -3.055 | -54.144402 | 2024-10-21 01:34:28 | METOP-C | SANTARÉM | PARÁ | Brasil | 1506807 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| 76fe3bf2-fb5f-322a-922f-f5a8ae28d5af | -2.7958 | -53.012001 | 2024-10-21 01:34:28 | METOP-C | MEDICILÂNDIA | PARÁ | Brasil | 1504455 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| 9065cbdd-50c7-3efe-aa8b-0b3347fc6e35 | -2.7921 | -52.9963 | 2024-10-21 01:34:28 | METOP-C | MEDICILÂNDIA | PARÁ | Brasil | 1504455 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| 4dc89c4f-0b46-3be9-934d-cff38ae6ca20 | -3.0514 | -54.172699 | 2024-10-21 01:34:29 | METOP-C | SANTARÉM | PARÁ | Brasil | 1506807 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| fcc9eed1-2524-343c-b430-4c9972452313 | -3.0483 | -54.159698 | 2024-10-21 01:34:29 | METOP-C | SANTARÉM | PARÁ | Brasil | 1506807 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| 605f42f1-b3a4-3b26-aa91-06326566fe88 | -2.8106 | -53.3325 | 2024-10-21 01:34:29 | METOP-C | MEDICILÂNDIA | PARÁ | Brasil | 1504455 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| 3cea1604-1073-319b-ae15-7ed9f1e05d9f | -2.8142 | -53.347401 | 2024-10-21 01:34:29 | METOP-C | MEDICILÂNDIA | PARÁ | Brasil | 1504455 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| 17484b2e-6216-30cb-b390-8d084887f15b | -2.8204 | -53.330299 | 2024-10-21 01:34:29 | METOP-C | MEDICILÂNDIA | PARÁ | Brasil | 1504455 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| 72458ce6-fa4b-310f-9513-29891f75334b | -3.0545 | -54.185699 | 2024-10-21 01:34:29 | METOP-C | SANTARÉM | PARÁ | Brasil | 1506807 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| 93f0af2a-18e6-3502-8da6-25345e74e54f | -2.689 | -54.770199 | 2024-10-21 01:34:37 | METOP-C | MOJUÍ DOS CAMPOS | PARÁ | Brasil | 1504752 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| 0e40850e-3d2a-3e0c-945d-8a50a4d3605e | -1.9012 | -52.095299 | 2024-10-21 01:34:39 | METOP-C | PORTO DE MOZ | PARÁ | Brasil | 1505908 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| c11fe5d7-01f5-33e3-8cba-711feb0a3932 | -1.9057 | -52.114101 | 2024-10-21 01:34:39 | METOP-C | PORTO DE MOZ | PARÁ | Brasil | 1505908 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| 556680b0-a27f-3f22-a9d5-c581a9c1ed25 | -2.2442 | -53.757301 | 2024-10-21 01:34:40 | METOP-C | PRAINHA | PARÁ | Brasil | 1506005 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| 1ec577eb-551b-351c-8b5a-422a20c53568 | -1.1687 | -53.633598 | 2024-10-21 01:34:57 | METOP-C | ALMEIRIM | PARÁ | Brasil | 1500503 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| 5a97b02f-d151-3624-b2cf-1ba87ff07a31 | -1.1722 | -53.648701 | 2024-10-21 01:34:57 | METOP-C | PRAINHA | PARÁ | Brasil | 1506005 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| 0ffc21f6-0c1f-334f-ab98-7b38eaef7215 | -1.1518 | -53.605499 | 2024-10-21 01:34:57 | METOP-C | ALMEIRIM | PARÁ | Brasil | 1500503 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| 63a61dc5-c267-368c-92fb-b5bbabccc0a1 | -1.1554 | -53.620701 | 2024-10-21 01:34:57 | METOP-C | ALMEIRIM | PARÁ | Brasil | 1500503 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| 0997d682-794a-3c09-91ec-87d1d6e7b1c9 | -1.159 | -53.635799 | 2024-10-21 01:34:57 | METOP-C | PRAINHA | PARÁ | Brasil | 1506005 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| 89e5ec3e-c365-3403-a5cd-189e686b6b3a | -1.1834 | -53.6368 | 2024-10-21 01:35:13 | GOES-16 | PRAINHA | PARÁ | Brasil | 1506005 | 15 | 33 | nan | nan | nan | Amazônia | 40.6 |
| c716f258-a4da-3ed4-a8ed-f049ae887f01 | -1.1835 | -53.6166 | 2024-10-21 01:35:13 | GOES-16 | ALMEIRIM | PARÁ | Brasil | 1500503 | 15 | 33 | nan | nan | nan | Amazônia | 36.8 |
| 37729e2e-ed4c-30b6-9353-c6c52a49244a | -1.2018 | -53.6366 | 2024-10-21 01:35:13 | GOES-16 | PRAINHA | PARÁ | Brasil | 1506005 | 15 | 33 | nan | nan | nan | Amazônia | 60.6 |
| f75cc8e8-5ac6-3809-9340-dc2db4103291 | -1.9395 | -52.1016 | 2024-10-21 01:35:17 | GOES-16 | PORTO DE MOZ | PARÁ | Brasil | 1505908 | 15 | 33 | nan | nan | nan | Amazônia | 59.0 |
| ec3a953b-c638-3505-912c-947f7a077859 | -2.2671 | -47.0775 | 2024-10-21 01:35:19 | GOES-16 | GARRAFÃO DO NORTE | PARÁ | Brasil | 1503077 | 15 | 33 | nan | nan | nan | Amazônia | 37.3 |
| 9307ce60-06d2-355a-8283-bff0a522289a | -2.464 | -49.1024 | 2024-10-21 01:35:20 | GOES-16 | MOJU | PARÁ | Brasil | 1504703 | 15 | 33 | nan | nan | nan | Amazônia | 49.4 |
| 12e128c2-af9e-3a43-ab2c-20de7690d1fb | -2.4824 | -49.1233 | 2024-10-21 01:35:20 | GOES-16 | MOJU | PARÁ | Brasil | 1504703 | 15 | 33 | nan | nan | nan | Amazônia | 66.9 |
| e3ec9872-56e8-3f20-920b-9d5241e9adbd | -2.4824 | -49.102 | 2024-10-21 01:35:20 | GOES-16 | MOJU | PARÁ | Brasil | 1504703 | 15 | 33 | nan | nan | nan | Amazônia | 85.8 |
| fcb3514e-20ca-35de-9647-0564107beca0 | -2.7885 | -51.3618 | 2024-10-21 01:35:22 | GOES-16 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 68.2 |
| 35e9763c-1690-37b0-98b2-0d94a14e8ba3 | -2.8069 | -51.3613 | 2024-10-21 01:35:22 | GOES-16 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 59.0 |
| 22f0d221-86e2-3190-ba9c-d9ca6063903d | -2.8372 | -53.3261 | 2024-10-21 01:35:22 | GOES-16 | MEDICILÂNDIA | PARÁ | Brasil | 1504455 | 15 | 33 | nan | nan | nan | Amazônia | 42.3 |
| 1db9e614-fe24-3a4e-90cd-e6d46f089683 | -2.8668 | -45.4631 | 2024-10-21 01:35:22 | GOES-16 | PEDRO DO ROSÁRIO | MARANHÃO | Brasil | 2108256 | 21 | 33 | nan | nan | nan | Amazônia | 59.4 |
| 0a28792c-89c9-377a-8634-de4000997037 | -2.8555 | -53.3459 | 2024-10-21 01:35:22 | GOES-16 | MEDICILÂNDIA | PARÁ | Brasil | 1504455 | 15 | 33 | nan | nan | nan | Amazônia | 39.1 |
| f739e387-c042-372a-9d39-7f10fe994488 | -2.8556 | -53.3256 | 2024-10-21 01:35:22 | GOES-16 | MEDICILÂNDIA | PARÁ | Brasil | 1504455 | 15 | 33 | nan | nan | nan | Amazônia | 46.9 |
| 3a13f68a-62ca-3ccc-97b1-888a31a60616 | -2.8864 | -45.215 | 2024-10-21 01:35:22 | GOES-16 | SÃO BENTO | MARANHÃO | Brasil | 2110500 | 21 | 33 | nan | nan | nan | Amazônia | 56.6 |
| bc4ff95a-358c-3424-ad68-7146a093340c | -2.905 | -45.2143 | 2024-10-21 01:35:22 | GOES-16 | SÃO BENTO | MARANHÃO | Brasil | 2110500 | 21 | 33 | nan | nan | nan | Amazônia | 130.4 |


[Clique aqui para ver as próximas entradas](README17.md)
