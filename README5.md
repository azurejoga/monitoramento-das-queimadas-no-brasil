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

## Dados Diários - Página 5

| ID | Latitude | Longitude | Data/Hora GMT | Satélite | Município | Estado | País | Município ID | Estado ID | País ID | Dias sem Chuva | Precipitação | Risco de Fogo | Bioma | FRP |
|----|----------|-----------|---------------|----------|-----------|--------|------|--------------|-----------|---------|----------------|--------------|----------------|-------|-----|
| 5319efd7-bd83-3db8-b00a-8bd5ccbb4f31 | -3.06121 | -53.79477 | 2024-12-25 05:10:00 | NOAA-21 | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | 2.1 |
| abe14c26-cb93-3b95-b220-9242fded43f0 | -1.70119 | -52.4137 | 2024-12-25 05:10:00 | NOAA-21 | PORTO DE MOZ | PARÁ | Brasil | 1505908 | 15 | 33 | nan | nan | nan | Amazônia | 1.6 |
| 3b5d150c-e64a-3806-9dfb-40a98d47b9a2 | -1.71115 | -52.42472 | 2024-12-25 05:10:00 | NOAA-21 | PORTO DE MOZ | PARÁ | Brasil | 1505908 | 15 | 33 | nan | nan | nan | Amazônia | 2.8 |
| 3f64b43a-f618-3437-8ebe-1315e79b5f94 | -3.5283 | -52.13068 | 2024-12-25 05:10:00 | NOAA-21 | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 2.4 |
| e9034998-3da5-3e16-a4cd-f567a678a93b | -1.3505 | -55.20839 | 2024-12-25 05:10:00 | NOAA-21 | ALENQUER | PARÁ | Brasil | 1500404 | 15 | 33 | nan | nan | nan | Amazônia | 2.4 |
| ac55f32c-ca57-38bf-81e1-beaf2a563a75 | -1.70878 | -52.41488 | 2024-12-25 05:10:00 | NOAA-21 | PORTO DE MOZ | PARÁ | Brasil | 1505908 | 15 | 33 | nan | nan | nan | Amazônia | 3.1 |
| db655b9a-c4b0-3ce6-9ff3-e3363959f9e2 | -3.5272 | -52.13182 | 2024-12-25 05:10:00 | NOAA-21 | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 3.1 |
| 08bb7f6b-8c99-3e2b-9fc8-a155a87f916d | -1.35439 | -55.20537 | 2024-12-25 05:10:00 | NOAA-21 | ALENQUER | PARÁ | Brasil | 1500404 | 15 | 33 | nan | nan | nan | Amazônia | 2.4 |
| fedc14ea-8b7f-364a-b5ef-891e6c209959 | -3.06025 | -53.79373 | 2024-12-25 05:10:00 | NOAA-21 | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | 2.0 |
| 931f7d84-7cde-3cee-aaff-b1faf05743c6 | -3.03408 | -53.89885 | 2024-12-25 05:10:00 | NOAA-21 | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | 2.0 |
| 1e6129b5-ac45-3e92-a87d-5f9960f5ad8b | -2.91161 | -52.38169 | 2024-12-25 05:10:00 | NOAA-21 | BRASIL NOVO | PARÁ | Brasil | 1501725 | 15 | 33 | nan | nan | nan | Amazônia | 1.6 |
| ef63e83f-a93c-3a50-bec1-5789d390e18c | -2.57761 | -53.68438 | 2024-12-25 05:10:00 | NOAA-21 | PRAINHA | PARÁ | Brasil | 1506005 | 15 | 33 | nan | nan | nan | Amazônia | 1.4 |
| 5fd99401-6f02-3c61-b2b1-2a17dad24cc7 | -1.35104 | -55.20485 | 2024-12-25 05:10:00 | NOAA-21 | ALENQUER | PARÁ | Brasil | 1500404 | 15 | 33 | nan | nan | nan | Amazônia | 2.4 |
| 73dbb376-e312-376a-9dc4-2ce3b477705f | -2.91086 | -52.38662 | 2024-12-25 05:10:00 | NOAA-21 | BRASIL NOVO | PARÁ | Brasil | 1501725 | 15 | 33 | nan | nan | nan | Amazônia | 1.6 |
| aee3ce83-c594-3964-a44f-6ae205d7e87b | -1.34995 | -55.21193 | 2024-12-25 05:10:00 | NOAA-21 | ALENQUER | PARÁ | Brasil | 1500404 | 15 | 33 | nan | nan | nan | Amazônia | 2.3 |
| 41e675c0-aeb3-36f5-aaf1-e4ca933b2ea3 | -2.94781 | -51.48594 | 2024-12-25 05:10:00 | NOAA-21 | ANAPU | PARÁ | Brasil | 1500859 | 15 | 33 | nan | nan | nan | Amazônia | 7.0 |
| 01d0aa98-bc21-3281-a746-72f4eae4172f | -3.15176 | -53.18085 | 2024-12-25 05:10:00 | NOAA-21 | MEDICILÂNDIA | PARÁ | Brasil | 1504455 | 15 | 33 | nan | nan | nan | Amazônia | 6.9 |
| ebdf662f-d230-3851-b7f3-6b442947a438 | -2.34404 | -53.88504 | 2024-12-25 05:10:00 | NOAA-21 | PRAINHA | PARÁ | Brasil | 1506005 | 15 | 33 | nan | nan | nan | Amazônia | 3.9 |
| 56807f2c-25a9-3f21-941a-707720bc22c4 | -3.42276 | -53.42212 | 2024-12-25 05:10:00 | NOAA-21 | MEDICILÂNDIA | PARÁ | Brasil | 1504455 | 15 | 33 | nan | nan | nan | Amazônia | 1.1 |
| e70b44a4-7e48-31cf-a118-1f8fa2edc520 | -3.15372 | -52.9779 | 2024-12-25 05:10:00 | NOAA-21 | MEDICILÂNDIA | PARÁ | Brasil | 1504455 | 15 | 33 | nan | nan | nan | Amazônia | 1.5 |
| a552248f-641b-320d-ba09-271faa3d596e | -3.15111 | -53.18523 | 2024-12-25 05:10:00 | NOAA-21 | MEDICILÂNDIA | PARÁ | Brasil | 1504455 | 15 | 33 | nan | nan | nan | Amazônia | 6.9 |
| 295267c1-dd50-3666-9b29-f3dd2e229dc4 | -3.14894 | -53.18198 | 2024-12-25 05:10:00 | NOAA-21 | MEDICILÂNDIA | PARÁ | Brasil | 1504455 | 15 | 33 | nan | nan | nan | Amazônia | 5.8 |
| 91739c80-59c0-3088-bb29-2ce28971ca67 | -3.05763 | -53.79424 | 2024-12-25 05:10:00 | NOAA-21 | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | 2.0 |
| 29cfed9c-5694-3686-890a-010478075db3 | -3.53041 | -52.13754 | 2024-12-25 05:10:00 | NOAA-21 | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 1.4 |
| 08c0ffc2-3c13-3541-91b7-6793f89b0826 | -3.59492 | -53.78692 | 2024-12-25 05:10:00 | NOAA-21 | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | 1.6 |
| 35a28dfa-c50d-3e83-882d-671feb44266d | -3.15746 | -52.97851 | 2024-12-25 05:10:00 | NOAA-21 | MEDICILÂNDIA | PARÁ | Brasil | 1504455 | 15 | 33 | nan | nan | nan | Amazônia | 2.0 |
| 323102f5-a69d-37b5-aa7b-dc6b60c96550 | -3.50459 | -52.47497 | 2024-12-25 05:10:00 | NOAA-21 | BRASIL NOVO | PARÁ | Brasil | 1501725 | 15 | 33 | nan | nan | nan | Amazônia | 1.3 |
| 3a59375c-3837-3b57-a3da-462cdacebfad | -3.81143 | -52.38026 | 2024-12-25 05:10:00 | NOAA-21 | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 1.0 |
| a70a4ead-9434-3adb-a340-05462bbf6dd4 | -3.15196 | -53.18693 | 2024-12-25 05:10:00 | NOAA-21 | MEDICILÂNDIA | PARÁ | Brasil | 1504455 | 15 | 33 | nan | nan | nan | Amazônia | 5.8 |
| 325eacb1-6f78-3f83-b3c2-d05d681538c6 | -3.06542 | -53.79127 | 2024-12-25 05:10:00 | NOAA-21 | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | 2.1 |
| 05452aec-e035-3987-acd3-0bf26a85319f | -3.0347 | -53.89482 | 2024-12-25 05:10:00 | NOAA-21 | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | 2.0 |
| 3c3a1342-9f56-32da-a23e-9f6b31b7c9e1 | -3.52751 | -52.1358 | 2024-12-25 05:10:00 | NOAA-21 | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 5.5 |
| 813172c4-1dfc-32b9-a466-c00726046c4c | -3.52645 | -52.13693 | 2024-12-25 05:10:00 | NOAA-21 | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 3.1 |
| 22e5759e-0e3a-31b3-bfdd-396d7d09b465 | -3.24123 | -53.63047 | 2024-12-25 05:10:00 | NOAA-21 | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | 1.2 |
| d9b845b0-f096-30a5-a12b-5f39ac091f5b | -1.35384 | -55.2089 | 2024-12-25 05:10:00 | NOAA-21 | ALENQUER | PARÁ | Brasil | 1500404 | 15 | 33 | nan | nan | nan | Amazônia | 2.4 |
| 41fbc418-c60f-36ac-aca0-97428b9ea9d7 | -3.06184 | -53.79073 | 2024-12-25 05:10:00 | NOAA-21 | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | 2.1 |
| 4284e808-b936-3473-bbdb-17d399eaad97 | -3.03114 | -53.89428 | 2024-12-25 05:10:00 | NOAA-21 | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | 2.0 |
| 6d69249c-fe26-3f91-991c-6267f56c289d | -2.85166 | -52.79932 | 2024-12-25 05:10:00 | NOAA-21 | BRASIL NOVO | PARÁ | Brasil | 1501725 | 15 | 33 | nan | nan | nan | Amazônia | 6.6 |
| 2686a3c6-783f-3f6c-82cb-24f2791958f4 | -2.29546 | -53.66106 | 2024-12-25 05:10:00 | NOAA-21 | PRAINHA | PARÁ | Brasil | 1506005 | 15 | 33 | nan | nan | nan | Amazônia | 0.9 |
| 0d272020-66eb-3a96-9820-4666de6d83d3 | -1.53741 | -55.25182 | 2024-12-25 05:10:00 | NOAA-21 | CURUÁ | PARÁ | Brasil | 1502855 | 15 | 33 | nan | nan | nan | Amazônia | 1.5 |
| 446c5968-622b-33d3-a907-6e430a86dd67 | -1.54076 | -55.25234 | 2024-12-25 05:10:00 | NOAA-21 | CURUÁ | PARÁ | Brasil | 1502855 | 15 | 33 | nan | nan | nan | Amazônia | 3.7 |
| 02604a34-d544-3fdc-ad07-dae41825c33f | -3.06383 | -53.79427 | 2024-12-25 05:10:00 | NOAA-21 | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | 2.0 |
| 94cabd8b-6c98-3629-afc2-1f68bffde575 | -1.5413 | -55.24881 | 2024-12-25 05:10:00 | NOAA-21 | CURUÁ | PARÁ | Brasil | 1502855 | 15 | 33 | nan | nan | nan | Amazônia | 3.7 |
| 773c1ee2-ffed-3037-8860-071ceb7a61da | -3.02403 | -53.8932 | 2024-12-25 05:10:00 | NOAA-21 | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | 2.3 |
| 8a36e4b4-db38-3a0f-9616-017f2eb668e7 | -1.35802 | -53.67766 | 2024-12-25 05:10:00 | NOAA-21 | PRAINHA | PARÁ | Brasil | 1506005 | 15 | 33 | nan | nan | nan | Amazônia | 2.2 |
| 803d7253-456f-345b-9ee9-9273b4f27f06 | -2.94837 | -51.48226 | 2024-12-25 05:10:00 | NOAA-21 | ANAPU | PARÁ | Brasil | 1500859 | 15 | 33 | nan | nan | nan | Amazônia | 2.7 |
| 5866d90b-4f85-37a1-a77d-c1da98f15baa | -3.32029 | -51.61099 | 2024-12-25 05:10:00 | NOAA-21 | ANAPU | PARÁ | Brasil | 1500859 | 15 | 33 | nan | nan | nan | Amazônia | 1.4 |
| d818c541-f8be-3837-8d83-b031d4e1ef92 | -1.75543 | -52.81728 | 2024-12-25 05:10:00 | NOAA-21 | PORTO DE MOZ | PARÁ | Brasil | 1505908 | 15 | 33 | nan | nan | nan | Amazônia | 2.9 |
| 32ba4b3a-3e99-39b1-bae8-2948aa046f38 | -2.49634 | -51.80569 | 2024-12-25 05:10:00 | NOAA-21 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 1.5 |
| d1fa2f9f-bc8d-3275-8a7a-8ef3c82931ee | -3.03764 | -53.89939 | 2024-12-25 05:10:00 | NOAA-21 | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | 0.9 |
| 9c759b87-4bd8-3148-a6c4-3adf1f4d4ff1 | -3.05964 | -53.79779 | 2024-12-25 05:10:00 | NOAA-21 | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | 2.5 |
| 5eda426f-a2d8-3ad3-aeaf-1fd700058b27 | -2.50637 | -51.79313 | 2024-12-25 05:10:00 | NOAA-21 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 0.9 |
| a0866e5d-f903-334c-bc7c-55ec14804b92 | -3.87977 | -52.13596 | 2024-12-25 05:10:00 | NOAA-21 | SENADOR JOSÉ PORFÍRIO | PARÁ | Brasil | 1507805 | 15 | 33 | nan | nan | nan | Amazônia | 0.8 |
| 2d0ea14f-da22-3edb-aaaa-2a18d30317cb | -3.03372 | -53.24446 | 2024-12-25 05:10:00 | NOAA-21 | MEDICILÂNDIA | PARÁ | Brasil | 1504455 | 15 | 33 | nan | nan | nan | Amazônia | 1.0 |
| bcd4171e-1477-33d4-b041-be7e9832c9d6 | -2.69393 | -51.78273 | 2024-12-25 05:10:00 | NOAA-21 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 0.9 |
| 4a15e33c-2f06-368c-b81f-dc6ce03db54a | -2.34343 | -53.889 | 2024-12-25 05:10:00 | NOAA-21 | PRAINHA | PARÁ | Brasil | 1506005 | 15 | 33 | nan | nan | nan | Amazônia | 3.9 |
| 1eff28ee-8c8c-3137-811b-26956471c656 | -3.06086 | -53.78968 | 2024-12-25 05:10:00 | NOAA-21 | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | 2.0 |
| d7912ab5-8b46-3093-8de7-36a5367a7057 | -3.00911 | -53.82421 | 2024-12-25 05:10:00 | NOAA-21 | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | 5.5 |
| d1388bde-6565-33a7-b46b-7dd9adeeff09 | -2.2919 | -53.66048 | 2024-12-25 05:10:00 | NOAA-21 | PRAINHA | PARÁ | Brasil | 1506005 | 15 | 33 | nan | nan | nan | Amazônia | 0.9 |
| c111a831-58a8-3fae-9993-8032e2705a7a | -3.23825 | -53.6257 | 2024-12-25 05:10:00 | NOAA-21 | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | 1.0 |
| 491f9715-483a-34fd-9be8-baadd50bd267 | -3.15263 | -53.18256 | 2024-12-25 05:10:00 | NOAA-21 | MEDICILÂNDIA | PARÁ | Brasil | 1504455 | 15 | 33 | nan | nan | nan | Amazônia | 5.8 |
| fdaf391f-d7c9-3009-9f8e-668cb588ffd2 | -1.34715 | -55.20787 | 2024-12-25 05:10:00 | NOAA-21 | ALENQUER | PARÁ | Brasil | 1500404 | 15 | 33 | nan | nan | nan | Amazônia | 0.7 |
| 952d41d6-1a15-3062-89b5-d58335fbaa87 | -1.71494 | -52.4253 | 2024-12-25 05:10:00 | NOAA-21 | PORTO DE MOZ | PARÁ | Brasil | 1505908 | 15 | 33 | nan | nan | nan | Amazônia | 1.1 |
| 68bf4f9a-9e52-3df4-a5fc-ea11a787a307 | -9.92861 | -59.90414 | 2024-12-25 05:12:00 | NOAA-21 | ARIPUANÃ | MATO GROSSO | Brasil | 5101407 | 51 | 33 | nan | nan | nan | Amazônia | 4.0 |
| 16693251-058f-323e-becb-e34ff3e7f091 | -9.93199 | -59.90469 | 2024-12-25 05:12:00 | NOAA-21 | ARIPUANÃ | MATO GROSSO | Brasil | 5101407 | 51 | 33 | nan | nan | nan | Amazônia | 4.0 |
| 551acadd-1052-3efe-ae4c-18f62963ca4d | -9.92582 | -59.89993 | 2024-12-25 05:12:00 | NOAA-21 | ARIPUANÃ | MATO GROSSO | Brasil | 5101407 | 51 | 33 | nan | nan | nan | Amazônia | 1.5 |
| 47e99119-29d0-361e-9e14-64f738efb07d | -13.04582 | -57.09531 | 2024-12-25 05:14:00 | NOAA-21 | NOVA MARINGÁ | MATO GROSSO | Brasil | 5108907 | 51 | 33 | nan | nan | nan | Amazônia | 1.0 |
| 84d7c657-1f98-3550-9b00-51f9ac9a3837 | -12.55703 | -57.75488 | 2024-12-25 05:14:00 | NOAA-21 | BRASNORTE | MATO GROSSO | Brasil | 5101902 | 51 | 33 | nan | nan | nan | Amazônia | 1.4 |
| 6ca418ea-39e4-3882-8a69-a5945f65d4ff | -3.06732 | -53.79372 | 2024-12-25 05:33:00 | NPP-375D | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | 2.0 |
| 37ef6463-a7a3-3cb0-a796-c5f67814db52 | -3.52409 | -52.13918 | 2024-12-25 05:33:00 | NPP-375D | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 2.5 |
| 779da7ce-f339-300c-86ab-99a7a721a290 | -3.06189 | -53.79293 | 2024-12-25 05:33:00 | NPP-375D | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | 2.0 |
| 95a89550-33bb-3a64-b466-3948f0006e09 | -3.00804 | -53.8194 | 2024-12-25 05:33:00 | NPP-375D | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | 1.2 |
| 805b2502-c2fc-3aa4-9e72-5bec4233620f | 0.11082 | -60.51615 | 2024-12-25 05:33:00 | NPP-375D | RORAINÓPOLIS | RORAIMA | Brasil | 1400472 | 14 | 33 | nan | nan | nan | Amazônia | 1.7 |
| 7ad276c8-1e0f-31d9-82c5-e38b50450dee | -3.14761 | -53.18916 | 2024-12-25 05:33:00 | NPP-375D | MEDICILÂNDIA | PARÁ | Brasil | 1504455 | 15 | 33 | nan | nan | nan | Amazônia | 3.3 |
| 64e35503-e66e-3c4c-9157-df2802719a9e | -3.00698 | -53.8265 | 2024-12-25 05:33:00 | NPP-375D | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | 1.8 |
| d6280469-10e8-3a86-b957-4a740d308adf | -2.85111 | -52.80347 | 2024-12-25 05:33:00 | NPP-375D | BRASIL NOVO | PARÁ | Brasil | 1501725 | 15 | 33 | nan | nan | nan | Amazônia | 3.0 |
| d172184c-2950-3699-aa5c-f648eb064af5 | -2.9474 | -51.48232 | 2024-12-25 05:33:00 | NPP-375D | ANAPU | PARÁ | Brasil | 1500859 | 15 | 33 | nan | nan | nan | Amazônia | 2.3 |
| 91bd01da-ba4d-3388-8a2e-f8ec039533f0 | -3.52488 | -52.13877 | 2024-12-25 05:33:00 | NPP-375D | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 2.3 |
| 7e8e4521-df04-3eda-8b4f-5b8a2196f98f | -3.43536 | -53.28936 | 2024-12-25 05:33:00 | NPP-375D | MEDICILÂNDIA | PARÁ | Brasil | 1504455 | 15 | 33 | nan | nan | nan | Amazônia | 1.9 |
| ad91cc70-75a3-39b5-b591-5888e0c736c3 | -1.58643 | -53.33395 | 2024-12-25 05:33:00 | NPP-375D | ALMEIRIM | PARÁ | Brasil | 1500503 | 15 | 33 | nan | nan | nan | Amazônia | 2.0 |
| 30fedac3-f6a0-3a57-833d-7a19dbf3af49 | 3.80931 | -60.40121 | 2024-12-25 05:33:00 | NPP-375D | NORMANDIA | RORAIMA | Brasil | 1400407 | 14 | 33 | nan | nan | nan | Amazônia | 1.5 |
| 272c5fd5-2e69-3b2f-aa2c-14b5a809f51c | -2.94111 | -51.48134 | 2024-12-25 05:33:00 | NPP-375D | ANAPU | PARÁ | Brasil | 1500859 | 15 | 33 | nan | nan | nan | Amazônia | 0.4 |
| 4fc196e1-be39-3b42-b25a-ebfd0d81587c | -2.85174 | -52.79921 | 2024-12-25 05:33:00 | NPP-375D | BRASIL NOVO | PARÁ | Brasil | 1501725 | 15 | 33 | nan | nan | nan | Amazônia | 3.0 |
| 72c3bf2a-1e6c-3fc5-a01b-b98c5b62463c | 1.598 | -61.43884 | 2024-12-25 05:33:00 | NPP-375D | CARACARAÍ | RORAIMA | Brasil | 1400209 | 14 | 33 | nan | nan | nan | Amazônia | 0.9 |
| 56285794-0698-33a1-b268-2382732c532e | -3.05594 | -53.79554 | 2024-12-25 05:33:00 | NPP-375D | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | 0.9 |
| f66794a0-aaf9-3cf6-8fd8-a08bc5d16ec4 | -3.52476 | -52.13469 | 2024-12-25 05:33:00 | NPP-375D | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 1.7 |
| b82761b1-9aad-3f91-b9c2-a26ab55a3885 | -3.14875 | -53.18161 | 2024-12-25 05:33:00 | NPP-375D | MEDICILÂNDIA | PARÁ | Brasil | 1504455 | 15 | 33 | nan | nan | nan | Amazônia | 3.2 |
| 9819d8d3-1674-3b17-9872-e724c16cf4cb | -3.14818 | -53.18539 | 2024-12-25 05:33:00 | NPP-375D | MEDICILÂNDIA | PARÁ | Brasil | 1504455 | 15 | 33 | nan | nan | nan | Amazônia | 3.3 |
| c53c8fab-281a-3653-a841-8dd949d73838 | -3.15383 | -53.18629 | 2024-12-25 05:33:00 | NPP-375D | MEDICILÂNDIA | PARÁ | Brasil | 1504455 | 15 | 33 | nan | nan | nan | Amazônia | 1.5 |
| d8e34b52-3006-35fc-b657-5d0b475ddd16 | -3.15575 | -52.97959 | 2024-12-25 05:33:00 | NPP-375D | MEDICILÂNDIA | PARÁ | Brasil | 1504455 | 15 | 33 | nan | nan | nan | Amazônia | 2.0 |
| fa5051c6-94ae-39fe-b408-a9426a4f233b | -2.91338 | -52.38542 | 2024-12-25 05:33:00 | NPP-375D | BRASIL NOVO | PARÁ | Brasil | 1501725 | 15 | 33 | nan | nan | nan | Amazônia | 1.9 |
| 2a4b59de-660c-3630-b156-e497b0eef2d0 | -3.0624 | -53.78959 | 2024-12-25 05:33:00 | NPP-375D | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | 1.4 |
| f3df096e-d507-3739-b93b-130064b84a8b | -3.53084 | -52.13562 | 2024-12-25 05:33:00 | NPP-375D | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 1.7 |
| 9df53bf3-6536-3510-aa8b-6e7f0c9cb6c3 | -1.5859 | -53.33741 | 2024-12-25 05:33:00 | NPP-375D | ALMEIRIM | PARÁ | Brasil | 1500503 | 15 | 33 | nan | nan | nan | Amazônia | 4.9 |
| c7be42d0-ada9-37a7-a3f8-e8ee5a81d0a0 | -3.52552 | -52.13426 | 2024-12-25 05:33:00 | NPP-375D | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 3.0 |
| df367961-0048-3f2d-87d8-f6d22c98389e | -3.15326 | -53.19004 | 2024-12-25 05:33:00 | NPP-375D | MEDICILÂNDIA | PARÁ | Brasil | 1504455 | 15 | 33 | nan | nan | nan | Amazônia | 1.5 |
| 3886a0f3-af0a-315d-81ab-dd9f350b6e3e | -3.43592 | -53.28559 | 2024-12-25 05:33:00 | NPP-375D | MEDICILÂNDIA | PARÁ | Brasil | 1504455 | 15 | 33 | nan | nan | nan | Amazônia | 1.6 |
| d06fb994-bc8a-353a-8805-fa5f1f73a203 | 0.11126 | -60.51629 | 2024-12-25 05:33:00 | NPP-375D | RORAINÓPOLIS | RORAIMA | Brasil | 1400472 | 14 | 33 | nan | nan | nan | Amazônia | 2.3 |
| e69d6729-3679-3bc2-9fbc-c678e84f08b4 | -2.94666 | -51.48732 | 2024-12-25 05:33:00 | NPP-375D | ANAPU | PARÁ | Brasil | 1500859 | 15 | 33 | nan | nan | nan | Amazônia | 2.6 |
| 3a118026-cb32-3b97-a719-68b4931f6a3a | 0.10783 | -60.51682 | 2024-12-25 05:33:00 | NPP-375D | RORAINÓPOLIS | RORAIMA | Brasil | 1400472 | 14 | 33 | nan | nan | nan | Amazônia | 2.3 |


[Clique aqui para ver as próximas entradas](README6.md)
