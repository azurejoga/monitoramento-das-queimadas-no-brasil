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

## Dados Diários - Página 40

| ID | Latitude | Longitude | Data/Hora GMT | Satélite | Município | Estado | País | Município ID | Estado ID | País ID | Dias sem Chuva | Precipitação | Risco de Fogo | Bioma | FRP |
|----|----------|-----------|---------------|----------|-----------|--------|------|--------------|-----------|---------|----------------|--------------|----------------|-------|-----|
| ed934026-f304-3446-ad61-48bd075bf3c0 | -12.9358 | -62.6818 | 2024-10-02 01:46:20 | GOES-16 | ALTA FLORESTA D'OESTE | RONDÔNIA | Brasil | 1100015 | 11 | 33 | nan | nan | nan | Amazônia | 103.2 |
| 692724e2-c660-3cb0-980e-9f5521c604d7 | -12.9546 | -62.6999 | 2024-10-02 01:46:20 | GOES-16 | ALTA FLORESTA D'OESTE | RONDÔNIA | Brasil | 1100015 | 11 | 33 | nan | nan | nan | Amazônia | 222.2 |
| 63a1b08a-de51-3448-b52b-5361c81f172b | -12.9548 | -62.6806 | 2024-10-02 01:46:20 | GOES-16 | ALTA FLORESTA D'OESTE | RONDÔNIA | Brasil | 1100015 | 11 | 33 | nan | nan | nan | Amazônia | 191.9 |
| 6d754c93-b422-39ff-82e1-247c849276f2 | -12.9736 | -62.6987 | 2024-10-02 01:46:20 | GOES-16 | ALTA FLORESTA D'OESTE | RONDÔNIA | Brasil | 1100015 | 11 | 33 | nan | nan | nan | Amazônia | 56.8 |
| 4499406c-3fd1-335e-b599-200e16bab16b | -12.9738 | -62.6795 | 2024-10-02 01:46:20 | GOES-16 | ALTA FLORESTA D'OESTE | RONDÔNIA | Brasil | 1100015 | 11 | 33 | nan | nan | nan | Amazônia | 63.0 |
| b33b1ef5-fdc5-3005-8e43-48d556fb1cdf | -13.2116 | -51.2073 | 2024-10-02 01:46:20 | GOES-16 | RIBEIRÃO CASCALHEIRA | MATO GROSSO | Brasil | 5107180 | 51 | 33 | nan | nan | nan | Cerrado | 58.0 |
| 147f2013-e29d-3f2d-a818-de3d621af4de | -13.5965 | -51.1367 | 2024-10-02 01:46:23 | GOES-16 | COCALINHO | MATO GROSSO | Brasil | 5103106 | 51 | 33 | nan | nan | nan | Cerrado | 77.1 |
| 629f0995-241d-38f5-9b86-7d9d1ea023b7 | -14.5699 | -44.8351 | 2024-10-02 01:46:27 | GOES-16 | BONITO DE MINAS | MINAS GERAIS | Brasil | 3108255 | 31 | 33 | nan | nan | nan | Cerrado | 54.2 |
| f1b349d8-7342-333e-af9e-2e648d931681 | -16.6127 | -57.217 | 2024-10-02 01:46:39 | GOES-16 | POCONÉ | MATO GROSSO | Brasil | 5106505 | 51 | 33 | nan | nan | nan | Pantanal | 247.7 |
| 2abe826e-0a81-3f32-ade2-67194799a351 | -16.612 | -57.2579 | 2024-10-02 01:46:39 | GOES-16 | POCONÉ | MATO GROSSO | Brasil | 5106505 | 51 | 33 | nan | nan | nan | Pantanal | 35.3 |
| 6c6f99d6-48aa-32e1-8e29-1925ad00217e | -16.6124 | -57.2375 | 2024-10-02 01:46:39 | GOES-16 | POCONÉ | MATO GROSSO | Brasil | 5106505 | 51 | 33 | nan | nan | nan | Pantanal | 160.9 |
| 02ceea23-2fc8-3d5b-87eb-e1cbaf022493 | -16.7647 | -57.4856 | 2024-10-02 01:46:40 | GOES-16 | CÁCERES | MATO GROSSO | Brasil | 5102504 | 51 | 33 | nan | nan | nan | Pantanal | 50.4 |
| 989cf45d-729e-38a4-8372-3672f9c5d0ed | -16.7663 | -57.3833 | 2024-10-02 01:46:40 | GOES-16 | POCONÉ | MATO GROSSO | Brasil | 5106505 | 51 | 33 | nan | nan | nan | Pantanal | 35.0 |
| 939c88da-646a-3c6a-885d-dddc45490f63 | -16.7862 | -57.3606 | 2024-10-02 01:46:40 | GOES-16 | POCONÉ | MATO GROSSO | Brasil | 5106505 | 51 | 33 | nan | nan | nan | Pantanal | 34.2 |
| c2567210-5261-3e91-886a-edbcefa401c9 | -16.8096 | -55.9177 | 2024-10-02 01:46:40 | GOES-16 | BARÃO DE MELGAÇO | MATO GROSSO | Brasil | 5101605 | 51 | 33 | nan | nan | nan | Pantanal | 68.8 |
| ac7d2d28-80a9-3661-8759-85c98f22f753 | -16.6319 | -57.2352 | 2024-10-02 01:46:40 | GOES-16 | POCONÉ | MATO GROSSO | Brasil | 5106505 | 51 | 33 | nan | nan | nan | Pantanal | 59.5 |
| 465af754-fdbd-360e-8635-0285b787a091 | -16.6322 | -57.2147 | 2024-10-02 01:46:40 | GOES-16 | POCONÉ | MATO GROSSO | Brasil | 5106505 | 51 | 33 | nan | nan | nan | Pantanal | 93.2 |
| c0c15128-5c60-32f9-b255-b4f7c2c41b5b | -16.6518 | -57.2125 | 2024-10-02 01:46:40 | GOES-16 | POCONÉ | MATO GROSSO | Brasil | 5106505 | 51 | 33 | nan | nan | nan | Pantanal | 39.9 |
| e75da276-9740-3111-be72-53cd9354564c | -16.6717 | -57.1897 | 2024-10-02 01:46:40 | GOES-16 | POCONÉ | MATO GROSSO | Brasil | 5106505 | 51 | 33 | nan | nan | nan | Pantanal | 50.0 |
| 2ffd8b81-f4b2-312b-8030-5655f10a89de | -16.6884 | -57.3718 | 2024-10-02 01:46:40 | GOES-16 | POCONÉ | MATO GROSSO | Brasil | 5106505 | 51 | 33 | nan | nan | nan | Pantanal | 73.6 |
| 26894614-c354-37bd-a9ad-2ccb0180c661 | -16.6887 | -57.3513 | 2024-10-02 01:46:40 | GOES-16 | POCONÉ | MATO GROSSO | Brasil | 5106505 | 51 | 33 | nan | nan | nan | Pantanal | 93.0 |
| c786ce38-afab-37b7-a79c-99a2164b655d | -16.689 | -57.3309 | 2024-10-02 01:46:40 | GOES-16 | POCONÉ | MATO GROSSO | Brasil | 5106505 | 51 | 33 | nan | nan | nan | Pantanal | 42.0 |
| c65ebe12-02e4-3ac1-96d8-d6a5eadd65c5 | -16.6912 | -57.1875 | 2024-10-02 01:46:40 | GOES-16 | POCONÉ | MATO GROSSO | Brasil | 5106505 | 51 | 33 | nan | nan | nan | Pantanal | 100.4 |
| 851ed8ec-a27d-314c-ac10-c7a1f4ca41a2 | -16.6916 | -57.167 | 2024-10-02 01:46:40 | GOES-16 | POCONÉ | MATO GROSSO | Brasil | 5106505 | 51 | 33 | nan | nan | nan | Pantanal | 44.6 |
| 83123dfe-b56a-3849-9672-cfd5823ef0f4 | -16.7079 | -57.3696 | 2024-10-02 01:46:40 | GOES-16 | POCONÉ | MATO GROSSO | Brasil | 5106505 | 51 | 33 | nan | nan | nan | Pantanal | 35.3 |
| 9800b97b-192a-3452-ae68-ca4f2dbdbd14 | -16.7082 | -57.3491 | 2024-10-02 01:46:40 | GOES-16 | POCONÉ | MATO GROSSO | Brasil | 5106505 | 51 | 33 | nan | nan | nan | Pantanal | 48.5 |
| 14cfb79f-acdb-344a-9d3c-be00c23e7e0b | -16.7108 | -57.1852 | 2024-10-02 01:46:40 | GOES-16 | POCONÉ | MATO GROSSO | Brasil | 5106505 | 51 | 33 | nan | nan | nan | Pantanal | 39.9 |
| cce48bf3-027b-3f7b-8208-aba3ced9f683 | -16.7265 | -57.4287 | 2024-10-02 01:46:40 | GOES-16 | CÁCERES | MATO GROSSO | Brasil | 5102504 | 51 | 33 | nan | nan | nan | Pantanal | 90.1 |
| c9442534-c0fd-3cdb-afdd-1f8c028344dd | -16.7452 | -57.4878 | 2024-10-02 01:46:40 | GOES-16 | CÁCERES | MATO GROSSO | Brasil | 5102504 | 51 | 33 | nan | nan | nan | Pantanal | 59.5 |
| 4177cfff-da91-3ca4-bc62-28e750735267 | -16.7461 | -57.4265 | 2024-10-02 01:46:40 | GOES-16 | CÁCERES | MATO GROSSO | Brasil | 5102504 | 51 | 33 | nan | nan | nan | Pantanal | 52.7 |
| 3538b2af-1113-33d5-8a87-dc1e56c9431e | -16.8292 | -55.9152 | 2024-10-02 01:46:41 | GOES-16 | BARÃO DE MELGAÇO | MATO GROSSO | Brasil | 5101605 | 51 | 33 | nan | nan | nan | Pantanal | 114.8 |
| 1484dae8-7ea5-3bad-8e9c-e8e154aefff9 | -16.8295 | -55.8945 | 2024-10-02 01:46:41 | GOES-16 | BARÃO DE MELGAÇO | MATO GROSSO | Brasil | 5101605 | 51 | 33 | nan | nan | nan | Pantanal | 143.0 |
| 87a576f7-48b8-3c15-903f-b77a0f5f5f85 | -16.8299 | -55.8737 | 2024-10-02 01:46:41 | GOES-16 | BARÃO DE MELGAÇO | MATO GROSSO | Brasil | 5101605 | 51 | 33 | nan | nan | nan | Pantanal | 74.2 |
| e360a103-a856-3920-8cb4-923ab8c8c9e6 | -16.8234 | -57.4789 | 2024-10-02 01:46:41 | GOES-16 | CÁCERES | MATO GROSSO | Brasil | 5102504 | 51 | 33 | nan | nan | nan | Pantanal | 41.6 |
| ee3d1a9f-39c7-3e05-b0ba-4a064cbaa4e8 | -16.8488 | -55.9128 | 2024-10-02 01:46:41 | GOES-16 | BARÃO DE MELGAÇO | MATO GROSSO | Brasil | 5101605 | 51 | 33 | nan | nan | nan | Pantanal | 70.8 |
| c9ea48b0-fd9e-3b0b-a3c6-9a35038b15b3 | -16.8491 | -55.892 | 2024-10-02 01:46:41 | GOES-16 | BARÃO DE MELGAÇO | MATO GROSSO | Brasil | 5101605 | 51 | 33 | nan | nan | nan | Pantanal | 100.4 |
| 832b1cf9-d90a-3ab3-b7b3-3a7dfdba7b36 | -16.8695 | -55.848 | 2024-10-02 01:46:41 | GOES-16 | BARÃO DE MELGAÇO | MATO GROSSO | Brasil | 5101605 | 51 | 33 | nan | nan | nan | Pantanal | 85.6 |
| e3cfbf52-958e-31e7-860b-6241c4d4b3bf | -17.0705 | -56.7114 | 2024-10-02 01:46:42 | GOES-16 | POCONÉ | MATO GROSSO | Brasil | 5106505 | 51 | 33 | nan | nan | nan | Pantanal | 67.6 |
| 04a55d64-e85d-38b1-9b02-9ad736b3e1ea | -17.0892 | -56.7709 | 2024-10-02 01:46:42 | GOES-16 | POCONÉ | MATO GROSSO | Brasil | 5106505 | 51 | 33 | nan | nan | nan | Pantanal | 75.6 |
| 8a9f63b6-0ea7-32e5-8a1a-0ee3aef788e4 | -17.0895 | -56.7503 | 2024-10-02 01:46:42 | GOES-16 | POCONÉ | MATO GROSSO | Brasil | 5106505 | 51 | 33 | nan | nan | nan | Pantanal | 77.2 |
| ff1bfe61-dfdd-327d-b36f-a431ba2595fc | -17.1091 | -56.7479 | 2024-10-02 01:46:42 | GOES-16 | POCONÉ | MATO GROSSO | Brasil | 5106505 | 51 | 33 | nan | nan | nan | Pantanal | 77.1 |
| 823156d6-c7ed-3a01-a9cc-dd381603cbfd | -17.1581 | -56.1637 | 2024-10-02 01:46:42 | GOES-16 | BARÃO DE MELGAÇO | MATO GROSSO | Brasil | 5101605 | 51 | 33 | nan | nan | nan | Pantanal | 84.1 |
| ac1a2fee-700a-307a-8d6c-eb379fb9c46e | -19.2317 | -46.8687 | 2024-10-02 01:46:52 | GOES-16 | SERRA DO SALITRE | MINAS GERAIS | Brasil | 3166808 | 31 | 33 | nan | nan | nan | Cerrado | 94.6 |
| 6b8bfa93-315d-3871-9bbc-8b268b706c0f | -19.2323 | -46.8452 | 2024-10-02 01:46:52 | GOES-16 | SERRA DO SALITRE | MINAS GERAIS | Brasil | 3166808 | 31 | 33 | nan | nan | nan | Cerrado | 77.4 |
| 9c5d19ed-ac85-393a-8e3a-be746b442eab | -20.0424 | -55.9738 | 2024-10-02 01:46:58 | GOES-16 | AQUIDAUANA | MATO GROSSO DO SUL | Brasil | 5001102 | 50 | 33 | nan | nan | nan | Pantanal | 83.1 |
| a8fc81d3-0d8d-371b-b4c1-b3e2084847bd | -21.3456 | -55.6841 | 2024-10-02 01:47:04 | GOES-16 | MARACAJU | MATO GROSSO DO SUL | Brasil | 5005400 | 50 | 33 | nan | nan | nan | Cerrado | 78.5 |
| 692f9a06-fee7-3152-b21f-fd9e7c7e35c6 | -21.3661 | -55.6807 | 2024-10-02 01:47:04 | GOES-16 | NIOAQUE | MATO GROSSO DO SUL | Brasil | 5005806 | 50 | 33 | nan | nan | nan | Cerrado | 93.9 |
| 00b940e6-24b4-324c-84d3-f6ea6436d6f3 | -22.3713 | -49.3011 | 2024-10-02 01:47:09 | GOES-16 | PIRATININGA | SÃO PAULO | Brasil | 3539400 | 35 | 33 | nan | nan | nan | Mata Atlântica | 181.8 |
| 6cc41ca8-442c-39a4-978b-b759ea79eb15 | -22.372 | -49.2777 | 2024-10-02 01:47:09 | GOES-16 | PIRATININGA | SÃO PAULO | Brasil | 3539400 | 35 | 33 | nan | nan | nan | Mata Atlântica | 250.5 |
| c2a49d75-5869-382c-b676-3b9c47e1a8b7 | -22.3922 | -49.2961 | 2024-10-02 01:47:09 | GOES-16 | PIRATININGA | SÃO PAULO | Brasil | 3539400 | 35 | 33 | nan | nan | nan | Mata Atlântica | 124.8 |
| 60e29cfe-2ba8-3912-827e-4632e687c96e | -22.3929 | -49.2727 | 2024-10-02 01:47:09 | GOES-16 | PIRATININGA | SÃO PAULO | Brasil | 3539400 | 35 | 33 | nan | nan | nan | Mata Atlântica | 157.7 |
| fffdb3ef-948b-3f3e-8cd4-bd41e23656f3 | -22.9006 | -45.1029 | 2024-10-02 01:47:11 | GOES-16 | GUARATINGUETÁ | SÃO PAULO | Brasil | 3518404 | 35 | 33 | nan | nan | nan | Mata Atlântica | 85.2 |
| cb7aa6eb-75c5-3f44-a7c1-61f3b93b010d | -22.9014 | -45.0779 | 2024-10-02 01:47:11 | GOES-16 | GUARATINGUETÁ | SÃO PAULO | Brasil | 3518404 | 35 | 33 | nan | nan | nan | Mata Atlântica | 94.9 |
| d2facff3-4497-3e14-ac35-fcba0e217cea | -22.9277 | -43.7243 | 2024-10-02 01:47:11 | GOES-16 | RIO DE JANEIRO | RIO DE JANEIRO | Brasil | 3304557 | 33 | 33 | nan | nan | nan | Mata Atlântica | 70.8 |
| efacdcd4-da74-3de8-9aa5-640c4cde239e | -2.9013 | -50.7351 | 2024-10-02 01:55:22 | GOES-16 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 52.4 |
| 798a1a57-1fb3-313a-8354-8a29b5be4530 | -3.2136 | -46.7843 | 2024-10-02 01:55:24 | GOES-16 | PARAGOMINAS | PARÁ | Brasil | 1505502 | 15 | 33 | nan | nan | nan | Amazônia | 63.3 |
| f2c94089-761d-367b-bfd2-8c20f7ab3357 | -5.9788 | -45.3621 | 2024-10-02 01:55:40 | GOES-16 | FERNANDO FALCÃO | MARANHÃO | Brasil | 2104081 | 21 | 33 | nan | nan | nan | Cerrado | 33.7 |
| a6513e3a-4688-39f7-ad4c-c4d21a38e8d2 | -7.1796 | -46.9444 | 2024-10-02 01:55:46 | GOES-16 | CAROLINA | MARANHÃO | Brasil | 2102804 | 21 | 33 | nan | nan | nan | Cerrado | 70.8 |
| be3d4dd5-51e9-3e90-9d67-80176f198869 | -8.4643 | -62.7124 | 2024-10-02 01:55:54 | GOES-16 | PORTO VELHO | RONDÔNIA | Brasil | 1100205 | 11 | 33 | nan | nan | nan | Amazônia | 54.0 |
| 50b6256e-6722-3f73-ae79-ed41f65656c2 | -9.9367 | -64.9179 | 2024-10-02 01:56:03 | GOES-16 | PORTO VELHO | RONDÔNIA | Brasil | 1100205 | 11 | 33 | nan | nan | nan | Amazônia | 114.0 |
| 59de737a-6b2a-3307-a738-ce06be40253b | -9.9368 | -64.8991 | 2024-10-02 01:56:03 | GOES-16 | PORTO VELHO | RONDÔNIA | Brasil | 1100205 | 11 | 33 | nan | nan | nan | Amazônia | 98.1 |
| f00800c2-7c02-33e0-a571-b53f862458bc | -9.9553 | -64.9172 | 2024-10-02 01:56:03 | GOES-16 | PORTO VELHO | RONDÔNIA | Brasil | 1100205 | 11 | 33 | nan | nan | nan | Amazônia | 130.6 |
| fdd21c00-3f0f-39c4-b9cc-9e05cdbd1ba1 | -9.9554 | -64.8984 | 2024-10-02 01:56:03 | GOES-16 | PORTO VELHO | RONDÔNIA | Brasil | 1100205 | 11 | 33 | nan | nan | nan | Amazônia | 123.2 |
| b7307e19-5bf3-358d-87a8-925f9ed98c52 | -11.6554 | -65.018 | 2024-10-02 01:56:13 | GOES-16 | GUAJARÁ-MIRIM | RONDÔNIA | Brasil | 1100106 | 11 | 33 | nan | nan | nan | Amazônia | 63.7 |
| 24788465-12fd-39fa-9523-8868997eb223 | -11.6555 | -64.9991 | 2024-10-02 01:56:13 | GOES-16 | GUAJARÁ-MIRIM | RONDÔNIA | Brasil | 1100106 | 11 | 33 | nan | nan | nan | Amazônia | 52.3 |
| 4e0850ca-eba8-375a-bf5a-580e1d3bfad7 | -11.6742 | -65.0172 | 2024-10-02 01:56:13 | GOES-16 | GUAJARÁ-MIRIM | RONDÔNIA | Brasil | 1100106 | 11 | 33 | nan | nan | nan | Amazônia | 50.7 |
| c6f48705-bae9-3d51-8e9f-5c1a24bb4708 | -11.6743 | -64.9983 | 2024-10-02 01:56:13 | GOES-16 | GUAJARÁ-MIRIM | RONDÔNIA | Brasil | 1100106 | 11 | 33 | nan | nan | nan | Amazônia | 83.1 |
| f288697e-4403-36d6-a9fe-9ee322af322a | -12.4433 | -43.7242 | 2024-10-02 01:56:15 | GOES-16 | BREJOLÂNDIA | BAHIA | Brasil | 2904407 | 29 | 33 | nan | nan | nan | Cerrado | 79.3 |
| db7fb8a1-170a-3491-8d41-e430fed841c2 | -12.2946 | -47.6446 | 2024-10-02 01:56:15 | GOES-16 | PARANÃ | TOCANTINS | Brasil | 1716208 | 17 | 33 | nan | nan | nan | Cerrado | 92.2 |
| fd01467b-2959-302f-835a-9f6b3fd64212 | -12.6484 | -63.1214 | 2024-10-02 01:56:18 | GOES-16 | SÃO FRANCISCO DO GUAPORÉ | RONDÔNIA | Brasil | 1101492 | 11 | 33 | nan | nan | nan | Amazônia | 110.5 |
| de71d7c0-3b73-3396-bd85-3b6c915533c6 | -12.6486 | -63.1022 | 2024-10-02 01:56:18 | GOES-16 | SÃO FRANCISCO DO GUAPORÉ | RONDÔNIA | Brasil | 1101492 | 11 | 33 | nan | nan | nan | Amazônia | 57.9 |
| 05129783-33b5-32b2-bad1-60be28659284 | -12.7054 | -63.0798 | 2024-10-02 01:56:18 | GOES-16 | SÃO FRANCISCO DO GUAPORÉ | RONDÔNIA | Brasil | 1101492 | 11 | 33 | nan | nan | nan | Amazônia | 64.8 |
| 69d718a4-7380-347c-822d-6c36b46fbaaf | -12.8593 | -62.7826 | 2024-10-02 01:56:19 | GOES-16 | SÃO FRANCISCO DO GUAPORÉ | RONDÔNIA | Brasil | 1101492 | 11 | 33 | nan | nan | nan | Amazônia | 54.6 |
| 0cd23ced-c904-3906-ba46-e54e3306c4f9 | -12.9357 | -62.701 | 2024-10-02 01:56:20 | GOES-16 | ALTA FLORESTA D'OESTE | RONDÔNIA | Brasil | 1100015 | 11 | 33 | nan | nan | nan | Amazônia | 87.0 |
| 2a05da25-fa9d-3b45-9373-8646b42bd21b | -12.9546 | -62.6999 | 2024-10-02 01:56:20 | GOES-16 | ALTA FLORESTA D'OESTE | RONDÔNIA | Brasil | 1100015 | 11 | 33 | nan | nan | nan | Amazônia | 120.1 |
| 35b8cb05-de0b-351f-8d03-b0045867ef4d | -12.9548 | -62.6806 | 2024-10-02 01:56:20 | GOES-16 | ALTA FLORESTA D'OESTE | RONDÔNIA | Brasil | 1100015 | 11 | 33 | nan | nan | nan | Amazônia | 110.3 |
| a644efdb-61dc-3a00-9a85-cb7fad0a1e7a | -12.9736 | -62.6987 | 2024-10-02 01:56:20 | GOES-16 | ALTA FLORESTA D'OESTE | RONDÔNIA | Brasil | 1100015 | 11 | 33 | nan | nan | nan | Amazônia | 54.2 |
| e102b725-3910-34af-a50c-5568a99d189d | -12.9738 | -62.6795 | 2024-10-02 01:56:20 | GOES-16 | ALTA FLORESTA D'OESTE | RONDÔNIA | Brasil | 1100015 | 11 | 33 | nan | nan | nan | Amazônia | 57.4 |
| 27051589-39fe-3902-9b9d-5ace9c82fa54 | -13.2173 | -48.624 | 2024-10-02 01:56:20 | GOES-16 | MONTIVIDIU DO NORTE | GOIÁS | Brasil | 5213772 | 52 | 33 | nan | nan | nan | Cerrado | 87.8 |
| 39ad63c3-d328-3f49-bf75-3847a363f0c0 | -12.9358 | -62.6818 | 2024-10-02 01:56:20 | GOES-16 | ALTA FLORESTA D'OESTE | RONDÔNIA | Brasil | 1100015 | 11 | 33 | nan | nan | nan | Amazônia | 55.9 |
| 6fb10ab5-de2d-3442-ad65-4b11c496e4f7 | -13.5965 | -51.1367 | 2024-10-02 01:56:23 | GOES-16 | COCALINHO | MATO GROSSO | Brasil | 5103106 | 51 | 33 | nan | nan | nan | Cerrado | 77.9 |
| 3cf0e9ac-b7cb-3425-a683-674321c2ace1 | -15.1197 | -55.8307 | 2024-10-02 01:56:31 | GOES-16 | CHAPADA DOS GUIMARÃES | MATO GROSSO | Brasil | 5103007 | 51 | 33 | nan | nan | nan | Cerrado | 107.6 |
| 3247463a-b400-3b56-9741-dcc8cb121632 | -15.139 | -55.8285 | 2024-10-02 01:56:31 | GOES-16 | CHAPADA DOS GUIMARÃES | MATO GROSSO | Brasil | 5103007 | 51 | 33 | nan | nan | nan | Cerrado | 90.9 |
| 1bdfaa9f-278e-3037-88e9-f56573d41948 | -16.4533 | -57.4392 | 2024-10-02 01:56:39 | GOES-16 | CÁCERES | MATO GROSSO | Brasil | 5102504 | 51 | 33 | nan | nan | nan | Pantanal | 28.4 |
| 280c9e87-edf2-318d-997e-5e82a374400d | -16.4536 | -57.4188 | 2024-10-02 01:56:39 | GOES-16 | CÁCERES | MATO GROSSO | Brasil | 5102504 | 51 | 33 | nan | nan | nan | Pantanal | 24.3 |
| 92b36a5b-4f92-3c98-8b7b-f192a388b10d | -16.6124 | -57.2375 | 2024-10-02 01:56:39 | GOES-16 | POCONÉ | MATO GROSSO | Brasil | 5106505 | 51 | 33 | nan | nan | nan | Pantanal | 60.6 |
| f5485cca-a7ce-3534-b39e-1165704f946e | -16.7461 | -57.4265 | 2024-10-02 01:56:40 | GOES-16 | CÁCERES | MATO GROSSO | Brasil | 5102504 | 51 | 33 | nan | nan | nan | Pantanal | 47.5 |
| 23b5b0fb-d727-3305-a69f-83d34b8e4fca | -16.6717 | -57.1897 | 2024-10-02 01:56:40 | GOES-16 | POCONÉ | MATO GROSSO | Brasil | 5106505 | 51 | 33 | nan | nan | nan | Pantanal | 29.5 |
| 6639cade-4b36-31c8-9aa9-496f738b6dbe | -16.6868 | -57.4741 | 2024-10-02 01:56:40 | GOES-16 | CÁCERES | MATO GROSSO | Brasil | 5102504 | 51 | 33 | nan | nan | nan | Pantanal | 39.7 |
| 164abea3-ad36-3cdd-adc8-482a4cff3019 | -16.6884 | -57.3718 | 2024-10-02 01:56:40 | GOES-16 | POCONÉ | MATO GROSSO | Brasil | 5106505 | 51 | 33 | nan | nan | nan | Pantanal | 74.6 |
| ca7745bd-0734-3a2a-9f98-806457fecdad | -16.6887 | -57.3513 | 2024-10-02 01:56:40 | GOES-16 | POCONÉ | MATO GROSSO | Brasil | 5106505 | 51 | 33 | nan | nan | nan | Pantanal | 81.7 |
| d795db29-cec4-395a-a19b-d1508ff45ba8 | -16.689 | -57.3309 | 2024-10-02 01:56:40 | GOES-16 | POCONÉ | MATO GROSSO | Brasil | 5106505 | 51 | 33 | nan | nan | nan | Pantanal | 39.4 |
| 1d4491ca-e4b0-3654-a45e-c37470f86214 | -16.6909 | -57.208 | 2024-10-02 01:56:40 | GOES-16 | POCONÉ | MATO GROSSO | Brasil | 5106505 | 51 | 33 | nan | nan | nan | Pantanal | 51.1 |
| af875f7c-2136-3a7d-baaf-28a442527c55 | -16.6912 | -57.1875 | 2024-10-02 01:56:40 | GOES-16 | POCONÉ | MATO GROSSO | Brasil | 5106505 | 51 | 33 | nan | nan | nan | Pantanal | 174.6 |
| 8edec2b5-284c-35aa-a80f-0eff3dad3471 | -16.6916 | -57.167 | 2024-10-02 01:56:40 | GOES-16 | POCONÉ | MATO GROSSO | Brasil | 5106505 | 51 | 33 | nan | nan | nan | Pantanal | 60.7 |
| 7aec3bc5-105f-3c1f-ac20-2d125f8e4dc7 | -16.7079 | -57.3696 | 2024-10-02 01:56:40 | GOES-16 | POCONÉ | MATO GROSSO | Brasil | 5106505 | 51 | 33 | nan | nan | nan | Pantanal | 30.6 |
| 3166d715-5c27-31f9-b501-2fe11d9efb11 | -16.7082 | -57.3491 | 2024-10-02 01:56:40 | GOES-16 | POCONÉ | MATO GROSSO | Brasil | 5106505 | 51 | 33 | nan | nan | nan | Pantanal | 41.1 |
| b657ba21-052d-3b6b-9588-01a08aeca89e | -16.7108 | -57.1852 | 2024-10-02 01:56:40 | GOES-16 | POCONÉ | MATO GROSSO | Brasil | 5106505 | 51 | 33 | nan | nan | nan | Pantanal | 57.5 |
| 59df2f91-5a28-3511-9506-b5c9af913552 | -16.7265 | -57.4287 | 2024-10-02 01:56:40 | GOES-16 | CÁCERES | MATO GROSSO | Brasil | 5102504 | 51 | 33 | nan | nan | nan | Pantanal | 77.0 |
| 75c37e14-b854-3506-b0f5-f71deb5238ec | -16.7269 | -57.4083 | 2024-10-02 01:56:40 | GOES-16 | CÁCERES | MATO GROSSO | Brasil | 5102504 | 51 | 33 | nan | nan | nan | Pantanal | 39.5 |


[Clique aqui para ver as próximas entradas](README41.md)
