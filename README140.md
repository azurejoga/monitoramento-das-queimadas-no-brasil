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

## Dados Diários - Página 140

| ID | Latitude | Longitude | Data/Hora GMT | Satélite | Município | Estado | País | Município ID | Estado ID | País ID | Dias sem Chuva | Precipitação | Risco de Fogo | Bioma | FRP |
|----|----------|-----------|---------------|----------|-----------|--------|------|--------------|-----------|---------|----------------|--------------|----------------|-------|-----|
| 63fe734d-d2e6-3e5e-a6b1-3b12b8b70164 | -15.71465 | -57.43347 | 2024-10-05 05:31:00 | NOAA-21 | PORTO ESTRELA | MATO GROSSO | Brasil | 5106851 | 51 | 33 | nan | nan | nan | Cerrado | 7.5 |
| fc93cd03-3387-3a20-bba8-036472408e10 | -15.71385 | -57.42301 | 2024-10-05 05:31:00 | NOAA-21 | PORTO ESTRELA | MATO GROSSO | Brasil | 5106851 | 51 | 33 | nan | nan | nan | Cerrado | 5.8 |
| cbbffff7-7f1d-341f-a895-b745b223b4ff | -15.7133 | -57.42729 | 2024-10-05 05:31:00 | NOAA-21 | PORTO ESTRELA | MATO GROSSO | Brasil | 5106851 | 51 | 33 | nan | nan | nan | Cerrado | 4.6 |
| be25b831-4b04-35a4-a295-90bab4a9b24d | -15.71272 | -57.43176 | 2024-10-05 05:31:00 | NOAA-21 | PORTO ESTRELA | MATO GROSSO | Brasil | 5106851 | 51 | 33 | nan | nan | nan | Cerrado | 4.6 |
| 3338e0f5-81a7-3437-849b-1fb4b97b836c | -15.71121 | -57.42404 | 2024-10-05 05:31:00 | NOAA-21 | PORTO ESTRELA | MATO GROSSO | Brasil | 5106851 | 51 | 33 | nan | nan | nan | Cerrado | 6.5 |
| a50e65d4-f085-3b03-8a45-952af9733316 | -15.7107 | -57.42831 | 2024-10-05 05:31:00 | NOAA-21 | PORTO ESTRELA | MATO GROSSO | Brasil | 5106851 | 51 | 33 | nan | nan | nan | Cerrado | 6.5 |
| 0222fb5f-f4c8-3038-b523-cb77e17bb644 | -15.70934 | -57.42247 | 2024-10-05 05:31:00 | NOAA-21 | PORTO ESTRELA | MATO GROSSO | Brasil | 5106851 | 51 | 33 | nan | nan | nan | Cerrado | 12.1 |
| 16a0fd53-5213-3eba-a94d-4fd3ebf60857 | -15.70879 | -57.42673 | 2024-10-05 05:31:00 | NOAA-21 | PORTO ESTRELA | MATO GROSSO | Brasil | 5106851 | 51 | 33 | nan | nan | nan | Cerrado | 6.0 |
| 29e3abce-8a12-30e0-817f-06c4bf41fa1c | -15.70429 | -57.42619 | 2024-10-05 05:31:00 | NOAA-21 | PORTO ESTRELA | MATO GROSSO | Brasil | 5106851 | 51 | 33 | nan | nan | nan | Cerrado | 6.0 |
| aa61f4ec-5a12-3e1d-a26e-f6f81a07e07d | -15.51988 | -56.88625 | 2024-10-05 05:31:00 | NOAA-21 | NOSSA SENHORA DO LIVRAMENTO | MATO GROSSO | Brasil | 5106109 | 51 | 33 | nan | nan | nan | Cerrado | 1.8 |
| a4fd2977-7854-3ae4-bdec-014dbab12cab | -17.14357 | -56.75273 | 2024-10-05 05:31:00 | NOAA-21 | POCONÉ | MATO GROSSO | Brasil | 5106505 | 51 | 33 | nan | nan | nan | Pantanal | 2.4 |
| c52351ca-9200-3d8c-9b8e-03d1793aedb4 | -17.14293 | -56.75815 | 2024-10-05 05:31:00 | NOAA-21 | POCONÉ | MATO GROSSO | Brasil | 5106505 | 51 | 33 | nan | nan | nan | Pantanal | 4.0 |
| e14d6a24-b9b3-31b8-89f0-ad3dacc1bda6 | -17.125 | -56.74475 | 2024-10-05 05:31:00 | NOAA-21 | POCONÉ | MATO GROSSO | Brasil | 5106505 | 51 | 33 | nan | nan | nan | Pantanal | 3.9 |
| a68f8860-1a39-327d-962b-1fc7df53e45c | -17.12374 | -56.7556 | 2024-10-05 05:31:00 | NOAA-21 | POCONÉ | MATO GROSSO | Brasil | 5106505 | 51 | 33 | nan | nan | nan | Pantanal | 3.2 |
| f7c8a7bd-a083-3d2b-8a89-e16202489745 | -17.1202 | -56.74412 | 2024-10-05 05:31:00 | NOAA-21 | POCONÉ | MATO GROSSO | Brasil | 5106505 | 51 | 33 | nan | nan | nan | Pantanal | 3.5 |
| 17d53b0b-e93f-3580-aa89-6df4a2fe056f | -17.11957 | -56.74955 | 2024-10-05 05:31:00 | NOAA-21 | POCONÉ | MATO GROSSO | Brasil | 5106505 | 51 | 33 | nan | nan | nan | Pantanal | 3.5 |
| fea06290-8223-3702-bacc-081af12ba6a5 | -17.11539 | -56.74349 | 2024-10-05 05:31:00 | NOAA-21 | POCONÉ | MATO GROSSO | Brasil | 5106505 | 51 | 33 | nan | nan | nan | Pantanal | 3.5 |
| 8898d282-b279-3bc5-b9a0-edb92e454325 | -17.03414 | -56.73203 | 2024-10-05 05:31:00 | NOAA-21 | POCONÉ | MATO GROSSO | Brasil | 5106505 | 51 | 33 | nan | nan | nan | Pantanal | 3.5 |
| ab65b6f6-84df-38b4-8543-d06c93b81890 | -17.03251 | -56.70424 | 2024-10-05 05:31:00 | NOAA-21 | POCONÉ | MATO GROSSO | Brasil | 5106505 | 51 | 33 | nan | nan | nan | Pantanal | 4.6 |
| ec2649f2-20b3-33d4-9ddc-448f6a192f78 | -17.02934 | -56.73139 | 2024-10-05 05:31:00 | NOAA-21 | POCONÉ | MATO GROSSO | Brasil | 5106505 | 51 | 33 | nan | nan | nan | Pantanal | 3.5 |
| 0ab78e2b-f84f-3954-88bf-a0df253fd18e | -17.02707 | -56.70903 | 2024-10-05 05:31:00 | NOAA-21 | POCONÉ | MATO GROSSO | Brasil | 5106505 | 51 | 33 | nan | nan | nan | Pantanal | 5.0 |
| 55b02baf-f83a-3e52-9188-5ec336479aaf | -17.01849 | -56.74091 | 2024-10-05 05:31:00 | NOAA-21 | POCONÉ | MATO GROSSO | Brasil | 5106505 | 51 | 33 | nan | nan | nan | Pantanal | 8.9 |
| de94c2c8-a240-3282-94ce-aa999b15c791 | -17.01432 | -56.73486 | 2024-10-05 05:31:00 | NOAA-21 | POCONÉ | MATO GROSSO | Brasil | 5106505 | 51 | 33 | nan | nan | nan | Pantanal | 7.4 |
| 97c84eea-1b19-3e85-a323-ef8b3ec869f1 | -17.01369 | -56.74027 | 2024-10-05 05:31:00 | NOAA-21 | POCONÉ | MATO GROSSO | Brasil | 5106505 | 51 | 33 | nan | nan | nan | Pantanal | 7.4 |
| 078dd225-cb9d-3c45-acd7-65c715edb073 | -17.00952 | -56.73422 | 2024-10-05 05:31:00 | NOAA-21 | POCONÉ | MATO GROSSO | Brasil | 5106505 | 51 | 33 | nan | nan | nan | Pantanal | 7.4 |
| f1acda37-6343-3099-837a-e922a072a1a2 | -17.00224 | -56.75517 | 2024-10-05 05:31:00 | NOAA-21 | POCONÉ | MATO GROSSO | Brasil | 5106505 | 51 | 33 | nan | nan | nan | Pantanal | 3.6 |
| 08ca1f8d-9a29-3deb-a6e1-6ab018b34da2 | -17.00161 | -56.76057 | 2024-10-05 05:31:00 | NOAA-21 | POCONÉ | MATO GROSSO | Brasil | 5106505 | 51 | 33 | nan | nan | nan | Pantanal | 3.6 |
| 3dd94264-ffd6-3539-900e-77ce89b1d014 | -16.99931 | -56.73832 | 2024-10-05 05:31:00 | NOAA-21 | POCONÉ | MATO GROSSO | Brasil | 5106505 | 51 | 33 | nan | nan | nan | Pantanal | 6.2 |
| 18f8a8d7-e199-36ce-a27e-dfb67f6fd24d | -16.99869 | -56.74372 | 2024-10-05 05:31:00 | NOAA-21 | POCONÉ | MATO GROSSO | Brasil | 5106505 | 51 | 33 | nan | nan | nan | Pantanal | 4.8 |
| e9cf0b2e-f8fa-34ea-9c14-97f3e5fe6005 | -16.99682 | -56.75993 | 2024-10-05 05:31:00 | NOAA-21 | POCONÉ | MATO GROSSO | Brasil | 5106505 | 51 | 33 | nan | nan | nan | Pantanal | 3.6 |
| 74ca6f3f-e9d7-38f3-a9d3-be1a79f6f6ec | -16.99199 | -56.75755 | 2024-10-05 05:31:00 | NOAA-21 | POCONÉ | MATO GROSSO | Brasil | 5106505 | 51 | 33 | nan | nan | nan | Pantanal | 6.3 |
| bca46bf3-746d-394e-a51e-212dbe182cf8 | -16.99134 | -56.76294 | 2024-10-05 05:31:00 | NOAA-21 | POCONÉ | MATO GROSSO | Brasil | 5106505 | 51 | 33 | nan | nan | nan | Pantanal | 6.3 |
| bff895ad-8e28-30c4-a9e8-fd4888e97fb5 | -16.98721 | -56.75692 | 2024-10-05 05:31:00 | NOAA-21 | POCONÉ | MATO GROSSO | Brasil | 5106505 | 51 | 33 | nan | nan | nan | Pantanal | 6.3 |
| 144f64aa-0a41-3d76-bef4-20030c7af549 | -16.98663 | -56.76403 | 2024-10-05 05:31:00 | NOAA-21 | POCONÉ | MATO GROSSO | Brasil | 5106505 | 51 | 33 | nan | nan | nan | Pantanal | 5.6 |
| df5d4d51-38e1-3a34-a6a0-4869c3fb5dce | -16.98655 | -56.7623 | 2024-10-05 05:31:00 | NOAA-21 | POCONÉ | MATO GROSSO | Brasil | 5106505 | 51 | 33 | nan | nan | nan | Pantanal | 6.3 |
| 5c17bde3-7f99-34d4-8de2-3090a5077703 | -16.98589 | -56.76768 | 2024-10-05 05:31:00 | NOAA-21 | POCONÉ | MATO GROSSO | Brasil | 5106505 | 51 | 33 | nan | nan | nan | Pantanal | 9.0 |
| f44cbdaa-aa94-37d6-8aff-3d7c0aab445a | -16.97633 | -56.7664 | 2024-10-05 05:31:00 | NOAA-21 | POCONÉ | MATO GROSSO | Brasil | 5106505 | 51 | 33 | nan | nan | nan | Pantanal | 20.4 |
| ea6d33dc-e5fa-371f-a4b1-f194ebab2f37 | -16.96688 | -56.76682 | 2024-10-05 05:31:00 | NOAA-21 | POCONÉ | MATO GROSSO | Brasil | 5106505 | 51 | 33 | nan | nan | nan | Pantanal | 35.2 |
| aced5e73-e9f7-3982-9ea0-5370a018544e | -16.71466 | -57.45689 | 2024-10-05 05:31:00 | NOAA-21 | CÁCERES | MATO GROSSO | Brasil | 5102504 | 51 | 33 | nan | nan | nan | Pantanal | 4.1 |
| 8556f9fd-4e07-3a6f-a449-8555d33fd730 | -16.71408 | -57.46169 | 2024-10-05 05:31:00 | NOAA-21 | CÁCERES | MATO GROSSO | Brasil | 5102504 | 51 | 33 | nan | nan | nan | Pantanal | 4.1 |
| 2a2238bd-f10e-32fd-895d-d5b7662adb4c | -16.7135 | -57.46648 | 2024-10-05 05:31:00 | NOAA-21 | CÁCERES | MATO GROSSO | Brasil | 5102504 | 51 | 33 | nan | nan | nan | Pantanal | 4.1 |
| 9c4693a7-dac5-3e94-b669-90091c27b302 | -16.70895 | -57.46586 | 2024-10-05 05:31:00 | NOAA-21 | CÁCERES | MATO GROSSO | Brasil | 5102504 | 51 | 33 | nan | nan | nan | Pantanal | 4.1 |
| c172f99f-1074-31ce-b37b-1eba3f9d4d8f | -16.69986 | -57.4646 | 2024-10-05 05:31:00 | NOAA-21 | CÁCERES | MATO GROSSO | Brasil | 5102504 | 51 | 33 | nan | nan | nan | Pantanal | 4.3 |
| 3d577304-8596-3680-a76c-0dc5056e076b | -16.69947 | -57.15979 | 2024-10-05 05:31:00 | NOAA-21 | POCONÉ | MATO GROSSO | Brasil | 5106505 | 51 | 33 | nan | nan | nan | Pantanal | 3.1 |
| a79d73f7-94f6-3d32-a186-972b9c7cad0b | -16.69929 | -57.46939 | 2024-10-05 05:31:00 | NOAA-21 | CÁCERES | MATO GROSSO | Brasil | 5102504 | 51 | 33 | nan | nan | nan | Pantanal | 4.3 |
| 2b1cb1dc-fb54-30c3-86a5-fbcfcf9bd133 | -16.69885 | -57.1648 | 2024-10-05 05:31:00 | NOAA-21 | POCONÉ | MATO GROSSO | Brasil | 5106505 | 51 | 33 | nan | nan | nan | Pantanal | 3.1 |
| 74b1b081-7d17-3d51-9add-a8a71ac82306 | -16.69588 | -57.45918 | 2024-10-05 05:31:00 | NOAA-21 | CÁCERES | MATO GROSSO | Brasil | 5102504 | 51 | 33 | nan | nan | nan | Pantanal | 4.2 |
| a5c56276-a99f-3f5c-85ab-56d420ece66b | -16.69531 | -57.46397 | 2024-10-05 05:31:00 | NOAA-21 | CÁCERES | MATO GROSSO | Brasil | 5102504 | 51 | 33 | nan | nan | nan | Pantanal | 4.4 |
| 76fe02bf-19d5-3835-a854-e7af3ec59de2 | -16.69164 | -57.44763 | 2024-10-05 05:31:00 | NOAA-21 | CÁCERES | MATO GROSSO | Brasil | 5102504 | 51 | 33 | nan | nan | nan | Pantanal | 2.2 |
| 50b3fe0e-348d-3eed-add4-65fe99982cee | -16.69076 | -57.46335 | 2024-10-05 05:31:00 | NOAA-21 | CÁCERES | MATO GROSSO | Brasil | 5102504 | 51 | 33 | nan | nan | nan | Pantanal | 4.4 |
| 9f32e4e2-238e-3c98-8a45-0fabe52d42d8 | -16.68982 | -57.462 | 2024-10-05 05:31:00 | NOAA-21 | CÁCERES | MATO GROSSO | Brasil | 5102504 | 51 | 33 | nan | nan | nan | Pantanal | 10.0 |
| e4487900-7cd1-38bc-bdb7-cf6e9b5076e1 | -16.68792 | -57.44833 | 2024-10-05 05:31:00 | NOAA-21 | CÁCERES | MATO GROSSO | Brasil | 5102504 | 51 | 33 | nan | nan | nan | Pantanal | 3.4 |
| 97c70089-5ed7-3961-ac55-0be25a8ce0c2 | -16.68735 | -57.45313 | 2024-10-05 05:31:00 | NOAA-21 | CÁCERES | MATO GROSSO | Brasil | 5102504 | 51 | 33 | nan | nan | nan | Pantanal | 7.7 |
| 5fbb520f-17ee-333d-8442-86299b30ecb9 | -16.68708 | -57.44701 | 2024-10-05 05:31:00 | NOAA-21 | CÁCERES | MATO GROSSO | Brasil | 5102504 | 51 | 33 | nan | nan | nan | Pantanal | 2.2 |
| 8ce7787b-38fe-3704-b106-0b8b99ef53bf | -16.68678 | -57.45794 | 2024-10-05 05:31:00 | NOAA-21 | CÁCERES | MATO GROSSO | Brasil | 5102504 | 51 | 33 | nan | nan | nan | Pantanal | 7.7 |
| afd8dbdd-b9b7-3c91-bec6-92c9087383e8 | -16.68648 | -57.45181 | 2024-10-05 05:31:00 | NOAA-21 | CÁCERES | MATO GROSSO | Brasil | 5102504 | 51 | 33 | nan | nan | nan | Pantanal | 2.2 |
| 9338b176-f986-39b8-bcd0-51cb12b90bdb | -16.68621 | -57.46272 | 2024-10-05 05:31:00 | NOAA-21 | CÁCERES | MATO GROSSO | Brasil | 5102504 | 51 | 33 | nan | nan | nan | Pantanal | 5.2 |
| b8bbf447-96ff-37b4-8553-5a07bdb6a9fa | -16.68587 | -57.4566 | 2024-10-05 05:31:00 | NOAA-21 | CÁCERES | MATO GROSSO | Brasil | 5102504 | 51 | 33 | nan | nan | nan | Pantanal | 10.0 |
| 4281c6d6-2854-31bc-9a73-7aada064fc83 | -16.68527 | -57.46138 | 2024-10-05 05:31:00 | NOAA-21 | CÁCERES | MATO GROSSO | Brasil | 5102504 | 51 | 33 | nan | nan | nan | Pantanal | 10.0 |
| ff0f8d48-af3b-3ec3-a249-22f3291dbb5b | -16.68467 | -57.46616 | 2024-10-05 05:31:00 | NOAA-21 | CÁCERES | MATO GROSSO | Brasil | 5102504 | 51 | 33 | nan | nan | nan | Pantanal | 4.6 |
| 1160a43b-bf4b-383a-9ea8-29d60334e82e | -16.6828 | -57.4525 | 2024-10-05 05:31:00 | NOAA-21 | CÁCERES | MATO GROSSO | Brasil | 5102504 | 51 | 33 | nan | nan | nan | Pantanal | 7.7 |
| 950084e4-5521-30a2-8b72-4555d3fec789 | -16.68223 | -57.45731 | 2024-10-05 05:31:00 | NOAA-21 | CÁCERES | MATO GROSSO | Brasil | 5102504 | 51 | 33 | nan | nan | nan | Pantanal | 7.7 |
| f132bc94-b88d-340b-81ce-9d493c215e29 | -16.68167 | -57.46209 | 2024-10-05 05:31:00 | NOAA-21 | CÁCERES | MATO GROSSO | Brasil | 5102504 | 51 | 33 | nan | nan | nan | Pantanal | 5.2 |
| 567a19c1-98bc-31e9-b257-6205770f41df | -16.68133 | -57.45597 | 2024-10-05 05:31:00 | NOAA-21 | CÁCERES | MATO GROSSO | Brasil | 5102504 | 51 | 33 | nan | nan | nan | Pantanal | 4.8 |
| ca87bb17-0403-3628-adf8-07f3c51eb00d | -16.6811 | -57.46689 | 2024-10-05 05:31:00 | NOAA-21 | CÁCERES | MATO GROSSO | Brasil | 5102504 | 51 | 33 | nan | nan | nan | Pantanal | 5.2 |
| 9618a79a-29e9-3623-a8f8-f6a3ee74ecdd | -16.68073 | -57.46076 | 2024-10-05 05:31:00 | NOAA-21 | CÁCERES | MATO GROSSO | Brasil | 5102504 | 51 | 33 | nan | nan | nan | Pantanal | 4.8 |
| c72addc5-e41c-3b08-9142-21b3ae26f09d | -16.68013 | -57.46554 | 2024-10-05 05:31:00 | NOAA-21 | CÁCERES | MATO GROSSO | Brasil | 5102504 | 51 | 33 | nan | nan | nan | Pantanal | 5.5 |
| 27313719-b734-3b13-8f58-99663ff49fe5 | -16.67768 | -57.45667 | 2024-10-05 05:31:00 | NOAA-21 | CÁCERES | MATO GROSSO | Brasil | 5102504 | 51 | 33 | nan | nan | nan | Pantanal | 2.2 |
| f4160ae9-d822-3906-8b6f-877425729d83 | -16.67712 | -57.46147 | 2024-10-05 05:31:00 | NOAA-21 | CÁCERES | MATO GROSSO | Brasil | 5102504 | 51 | 33 | nan | nan | nan | Pantanal | 4.5 |
| 24758de2-751a-36d0-b427-b3b0372a31e1 | -16.67678 | -57.45534 | 2024-10-05 05:31:00 | NOAA-21 | CÁCERES | MATO GROSSO | Brasil | 5102504 | 51 | 33 | nan | nan | nan | Pantanal | 4.8 |
| c800c0f0-3b2e-37ee-b1cf-f15ae760976a | -16.67655 | -57.46625 | 2024-10-05 05:31:00 | NOAA-21 | CÁCERES | MATO GROSSO | Brasil | 5102504 | 51 | 33 | nan | nan | nan | Pantanal | 4.5 |
| c706e08e-cbe8-39d0-b52f-148cdea01ff3 | -16.67618 | -57.46013 | 2024-10-05 05:31:00 | NOAA-21 | CÁCERES | MATO GROSSO | Brasil | 5102504 | 51 | 33 | nan | nan | nan | Pantanal | 4.8 |
| 34a4e12e-4aad-38b3-9ab6-393491268ef8 | -16.67599 | -57.47103 | 2024-10-05 05:31:00 | NOAA-21 | CÁCERES | MATO GROSSO | Brasil | 5102504 | 51 | 33 | nan | nan | nan | Pantanal | 2.5 |
| 82003de4-479c-363b-9436-ce2103437e3e | -16.67558 | -57.46492 | 2024-10-05 05:31:00 | NOAA-21 | CÁCERES | MATO GROSSO | Brasil | 5102504 | 51 | 33 | nan | nan | nan | Pantanal | 5.5 |
| 36ee5322-099c-390e-bdf5-72b627b64339 | -16.67543 | -57.4758 | 2024-10-05 05:31:00 | NOAA-21 | CÁCERES | MATO GROSSO | Brasil | 5102504 | 51 | 33 | nan | nan | nan | Pantanal | 2.5 |
| 3e313a61-af35-3713-b7a8-1b4ed57e3fc7 | -16.67498 | -57.46968 | 2024-10-05 05:31:00 | NOAA-21 | CÁCERES | MATO GROSSO | Brasil | 5102504 | 51 | 33 | nan | nan | nan | Pantanal | 5.5 |
| 560815de-8fdb-3cb8-b35e-b933aaf37f43 | -16.67314 | -57.45604 | 2024-10-05 05:31:00 | NOAA-21 | CÁCERES | MATO GROSSO | Brasil | 5102504 | 51 | 33 | nan | nan | nan | Pantanal | 2.2 |
| c2fa5d34-26c4-372c-8238-6389df87b586 | -16.67257 | -57.46084 | 2024-10-05 05:31:00 | NOAA-21 | CÁCERES | MATO GROSSO | Brasil | 5102504 | 51 | 33 | nan | nan | nan | Pantanal | 4.5 |
| 40b0cb9a-af1c-30cd-b026-90a006002cd8 | -16.67201 | -57.46562 | 2024-10-05 05:31:00 | NOAA-21 | CÁCERES | MATO GROSSO | Brasil | 5102504 | 51 | 33 | nan | nan | nan | Pantanal | 4.5 |
| 03adc311-8a35-3999-aa9e-d31481dd6c9e | -16.67163 | -57.45951 | 2024-10-05 05:31:00 | NOAA-21 | CÁCERES | MATO GROSSO | Brasil | 5102504 | 51 | 33 | nan | nan | nan | Pantanal | 4.6 |
| 1aad2273-29ca-3b7e-bff8-0b96fab8d09c | -16.67145 | -57.4704 | 2024-10-05 05:31:00 | NOAA-21 | CÁCERES | MATO GROSSO | Brasil | 5102504 | 51 | 33 | nan | nan | nan | Pantanal | 2.5 |
| 33d5c412-c7fc-3431-aa94-15af75f1d296 | -16.67103 | -57.46429 | 2024-10-05 05:31:00 | NOAA-21 | CÁCERES | MATO GROSSO | Brasil | 5102504 | 51 | 33 | nan | nan | nan | Pantanal | 3.5 |
| 6135bf5f-566b-32f5-86da-9f60923dabbb | -16.67044 | -57.46906 | 2024-10-05 05:31:00 | NOAA-21 | CÁCERES | MATO GROSSO | Brasil | 5102504 | 51 | 33 | nan | nan | nan | Pantanal | 3.5 |
| 2e088199-0de1-359f-9019-8c1550f542e5 | -17.14554 | -57.36321 | 2024-10-05 05:31:00 | NOAA-21 | CÁCERES | MATO GROSSO | Brasil | 5102504 | 51 | 33 | nan | nan | nan | Pantanal | 4.3 |
| 94e58433-3eed-3df4-a151-04a5dd6d2be1 | -17.14491 | -57.40813 | 2024-10-05 05:31:00 | NOAA-21 | CÁCERES | MATO GROSSO | Brasil | 5102504 | 51 | 33 | nan | nan | nan | Pantanal | 7.2 |
| 154c49f8-0312-3427-9abe-9aac93ae0872 | -17.14438 | -57.37306 | 2024-10-05 05:31:00 | NOAA-21 | CÁCERES | MATO GROSSO | Brasil | 5102504 | 51 | 33 | nan | nan | nan | Pantanal | 4.0 |
| f5a837c9-9ead-364b-bf45-acb03454f8dd | -17.14205 | -57.39278 | 2024-10-05 05:31:00 | NOAA-21 | CÁCERES | MATO GROSSO | Brasil | 5102504 | 51 | 33 | nan | nan | nan | Pantanal | 4.1 |
| a0769db8-52a5-3c14-88e2-63f6690d8951 | -17.14147 | -57.39771 | 2024-10-05 05:31:00 | NOAA-21 | CÁCERES | MATO GROSSO | Brasil | 5102504 | 51 | 33 | nan | nan | nan | Pantanal | 4.1 |
| 06200c4a-499d-3c05-8cc9-cf61ab6b7159 | -17.14089 | -57.4026 | 2024-10-05 05:31:00 | NOAA-21 | CÁCERES | MATO GROSSO | Brasil | 5102504 | 51 | 33 | nan | nan | nan | Pantanal | 2.6 |
| 2de327e0-82ce-3251-84fa-0834e476126d | -17.14031 | -57.40751 | 2024-10-05 05:31:00 | NOAA-21 | CÁCERES | MATO GROSSO | Brasil | 5102504 | 51 | 33 | nan | nan | nan | Pantanal | 2.6 |
| 0c6f3e06-2193-336e-ac68-dcefdfe51447 | -17.13978 | -57.37244 | 2024-10-05 05:31:00 | NOAA-21 | CÁCERES | MATO GROSSO | Brasil | 5102504 | 51 | 33 | nan | nan | nan | Pantanal | 4.0 |
| acf2a18b-93ff-36d6-bc66-86d030b470ce | -17.13973 | -57.41243 | 2024-10-05 05:31:00 | NOAA-21 | CÁCERES | MATO GROSSO | Brasil | 5102504 | 51 | 33 | nan | nan | nan | Pantanal | 11.0 |
| 7bbba8d2-7554-316d-8c69-dec6b455718f | -17.13688 | -57.39708 | 2024-10-05 05:31:00 | NOAA-21 | CÁCERES | MATO GROSSO | Brasil | 5102504 | 51 | 33 | nan | nan | nan | Pantanal | 4.1 |
| c7493cfc-a0a9-3043-b410-3695868efb4b | -17.1363 | -57.40199 | 2024-10-05 05:31:00 | NOAA-21 | CÁCERES | MATO GROSSO | Brasil | 5102504 | 51 | 33 | nan | nan | nan | Pantanal | 2.6 |
| 14cbe01c-0cda-3edb-bf75-49dddeb56b7c | -17.13572 | -57.40689 | 2024-10-05 05:31:00 | NOAA-21 | CÁCERES | MATO GROSSO | Brasil | 5102504 | 51 | 33 | nan | nan | nan | Pantanal | 2.6 |
| b774dd01-34cf-3f83-b183-83c5344c5a25 | -17.13514 | -57.4118 | 2024-10-05 05:31:00 | NOAA-21 | CÁCERES | MATO GROSSO | Brasil | 5102504 | 51 | 33 | nan | nan | nan | Pantanal | 11.0 |
| 8ea977ee-70a6-34ac-9af5-1a56a3dc86d5 | -17.13456 | -57.41671 | 2024-10-05 05:31:00 | NOAA-21 | CÁCERES | MATO GROSSO | Brasil | 5102504 | 51 | 33 | nan | nan | nan | Pantanal | 11.0 |
| e41e91fe-43f1-3dc6-8980-a5b8ea05dad6 | -17.13228 | -57.39646 | 2024-10-05 05:31:00 | NOAA-21 | CÁCERES | MATO GROSSO | Brasil | 5102504 | 51 | 33 | nan | nan | nan | Pantanal | 5.3 |
| 25ea76cb-f441-30c8-bebb-0758fe63eef5 | -17.1317 | -57.40136 | 2024-10-05 05:31:00 | NOAA-21 | CÁCERES | MATO GROSSO | Brasil | 5102504 | 51 | 33 | nan | nan | nan | Pantanal | 3.8 |
| b7dfa6de-bb44-3abe-a46d-e31cab07038f | -17.13112 | -57.40627 | 2024-10-05 05:31:00 | NOAA-21 | CÁCERES | MATO GROSSO | Brasil | 5102504 | 51 | 33 | nan | nan | nan | Pantanal | 3.8 |


[Clique aqui para ver as próximas entradas](README141.md)
