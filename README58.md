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

## Dados Diários - Página 58

| ID | Latitude | Longitude | Data/Hora GMT | Satélite | Município | Estado | País | Município ID | Estado ID | País ID | Dias sem Chuva | Precipitação | Risco de Fogo | Bioma | FRP |
|----|----------|-----------|---------------|----------|-----------|--------|------|--------------|-----------|---------|----------------|--------------|----------------|-------|-----|
| 500adaf1-cc68-3c8a-8c09-60fd53aab032 | -19.54094 | -56.65137 | 2024-10-24 04:38:00 | NOAA-21 | AQUIDAUANA | MATO GROSSO DO SUL | Brasil | 5001102 | 50 | 33 | nan | nan | nan | Pantanal | 4.8 |
| 3775d1cd-7d33-3a03-925c-7992b1c80263 | -19.54089 | -56.69626 | 2024-10-24 04:38:00 | NOAA-21 | CORUMBÁ | MATO GROSSO DO SUL | Brasil | 5003207 | 50 | 33 | nan | nan | nan | Pantanal | 7.4 |
| a5891f3b-2cf1-387c-969a-330310e8f0a3 | -19.54054 | -56.67575 | 2024-10-24 04:38:00 | NOAA-21 | AQUIDAUANA | MATO GROSSO DO SUL | Brasil | 5001102 | 50 | 33 | nan | nan | nan | Pantanal | 7.8 |
| 0f0ac8e3-b9b9-3fe5-9c64-7f9005a7861b | -19.54019 | -56.65528 | 2024-10-24 04:38:00 | NOAA-21 | AQUIDAUANA | MATO GROSSO DO SUL | Brasil | 5001102 | 50 | 33 | nan | nan | nan | Pantanal | 3.9 |
| e1dbf33f-7c04-30ba-9835-ea16c29ecbd8 | -19.54014 | -56.7002 | 2024-10-24 04:38:00 | NOAA-21 | CORUMBÁ | MATO GROSSO DO SUL | Brasil | 5003207 | 50 | 33 | nan | nan | nan | Pantanal | 7.4 |
| ddb78055-b911-3633-a8e8-fafe59185f73 | -19.53979 | -56.67967 | 2024-10-24 04:38:00 | NOAA-21 | AQUIDAUANA | MATO GROSSO DO SUL | Brasil | 5001102 | 50 | 33 | nan | nan | nan | Pantanal | 9.3 |
| 5b541ba1-059b-330e-9c88-d7270a70bcb5 | -19.53944 | -56.6592 | 2024-10-24 04:38:00 | NOAA-21 | AQUIDAUANA | MATO GROSSO DO SUL | Brasil | 5001102 | 50 | 33 | nan | nan | nan | Pantanal | 3.9 |
| 3b1d73fb-e067-3932-b00e-4e023bcfbb8b | -19.53904 | -56.68359 | 2024-10-24 04:38:00 | NOAA-21 | CORUMBÁ | MATO GROSSO DO SUL | Brasil | 5003207 | 50 | 33 | nan | nan | nan | Pantanal | 9.3 |
| f62214e1-3780-3ce6-8557-a0daac4a6a5a | -19.53868 | -56.66312 | 2024-10-24 04:38:00 | NOAA-21 | AQUIDAUANA | MATO GROSSO DO SUL | Brasil | 5001102 | 50 | 33 | nan | nan | nan | Pantanal | 4.3 |
| 27b96fb8-67f6-3bbf-8984-39f2060bbd26 | -19.53828 | -56.68752 | 2024-10-24 04:38:00 | NOAA-21 | CORUMBÁ | MATO GROSSO DO SUL | Brasil | 5003207 | 50 | 33 | nan | nan | nan | Pantanal | 5.1 |
| 6eb8bbfa-637b-37aa-a954-51bfa6da2086 | -19.53793 | -56.66704 | 2024-10-24 04:38:00 | NOAA-21 | AQUIDAUANA | MATO GROSSO DO SUL | Brasil | 5001102 | 50 | 33 | nan | nan | nan | Pantanal | 4.3 |
| 89d194f7-70fb-3dec-b8f4-95d39ccd3e63 | -19.53753 | -56.69146 | 2024-10-24 04:38:00 | NOAA-21 | CORUMBÁ | MATO GROSSO DO SUL | Brasil | 5003207 | 50 | 33 | nan | nan | nan | Pantanal | 5.1 |
| 0f12a6c8-2f4a-36a4-801e-5967bfa9b771 | -19.53718 | -56.67096 | 2024-10-24 04:38:00 | NOAA-21 | AQUIDAUANA | MATO GROSSO DO SUL | Brasil | 5001102 | 50 | 33 | nan | nan | nan | Pantanal | 7.8 |
| 584ee6a1-893e-3910-b1dc-f70e991c0300 | -19.53683 | -56.65051 | 2024-10-24 04:38:00 | NOAA-21 | AQUIDAUANA | MATO GROSSO DO SUL | Brasil | 5001102 | 50 | 33 | nan | nan | nan | Pantanal | 6.9 |
| d46f4629-0109-3d67-8f7d-73439fe0f4fd | -19.53677 | -56.6954 | 2024-10-24 04:38:00 | NOAA-21 | CORUMBÁ | MATO GROSSO DO SUL | Brasil | 5003207 | 50 | 33 | nan | nan | nan | Pantanal | 11.5 |
| f5f89ecf-5a80-32fd-adc2-f54f733b1d11 | -19.53643 | -56.67488 | 2024-10-24 04:38:00 | NOAA-21 | AQUIDAUANA | MATO GROSSO DO SUL | Brasil | 5001102 | 50 | 33 | nan | nan | nan | Pantanal | 7.8 |
| 7bf3641a-ecf6-3569-903b-6d8f08973633 | -19.53608 | -56.65443 | 2024-10-24 04:38:00 | NOAA-21 | AQUIDAUANA | MATO GROSSO DO SUL | Brasil | 5001102 | 50 | 33 | nan | nan | nan | Pantanal | 3.7 |
| d66f83a6-b9ea-3a74-8db3-1ba6be704dc1 | -19.53602 | -56.69934 | 2024-10-24 04:38:00 | NOAA-21 | CORUMBÁ | MATO GROSSO DO SUL | Brasil | 5003207 | 50 | 33 | nan | nan | nan | Pantanal | 11.5 |
| 4149cbda-d266-3833-a677-f9ab1cb454a7 | -19.53568 | -56.67881 | 2024-10-24 04:38:00 | NOAA-21 | CORUMBÁ | MATO GROSSO DO SUL | Brasil | 5003207 | 50 | 33 | nan | nan | nan | Pantanal | 9.3 |
| 665fea1e-cced-373d-9bd3-bf56f437ea2a | -19.53533 | -56.65835 | 2024-10-24 04:38:00 | NOAA-21 | AQUIDAUANA | MATO GROSSO DO SUL | Brasil | 5001102 | 50 | 33 | nan | nan | nan | Pantanal | 3.7 |
| e8d7d854-7585-3c1d-aa98-7f2d2315fd21 | -19.53509 | -56.57781 | 2024-10-24 04:38:00 | NOAA-21 | AQUIDAUANA | MATO GROSSO DO SUL | Brasil | 5001102 | 50 | 33 | nan | nan | nan | Pantanal | 3.3 |
| 7221e57c-2b4c-38a5-beac-27761aaec33e | -19.53492 | -56.68274 | 2024-10-24 04:38:00 | NOAA-21 | CORUMBÁ | MATO GROSSO DO SUL | Brasil | 5003207 | 50 | 33 | nan | nan | nan | Pantanal | 9.3 |
| 0c415c33-372a-329e-8a93-8b0696563f59 | -19.53457 | -56.66226 | 2024-10-24 04:38:00 | NOAA-21 | AQUIDAUANA | MATO GROSSO DO SUL | Brasil | 5001102 | 50 | 33 | nan | nan | nan | Pantanal | 3.6 |
| 8b99d9dd-6c4d-3949-815f-d54537d44143 | -19.53437 | -56.58169 | 2024-10-24 04:38:00 | NOAA-21 | AQUIDAUANA | MATO GROSSO DO SUL | Brasil | 5001102 | 50 | 33 | nan | nan | nan | Pantanal | 1.5 |
| dd43b786-3a96-3ecf-9167-e9459aa0796a | -19.53417 | -56.68666 | 2024-10-24 04:38:00 | NOAA-21 | CORUMBÁ | MATO GROSSO DO SUL | Brasil | 5003207 | 50 | 33 | nan | nan | nan | Pantanal | 5.1 |
| cfaab868-0e13-38f4-89e9-cc1edea6a1cf | -19.53392 | -56.57704 | 2024-10-24 04:38:00 | NOAA-21 | AQUIDAUANA | MATO GROSSO DO SUL | Brasil | 5001102 | 50 | 33 | nan | nan | nan | Pantanal | 2.9 |
| 382f8514-3dd9-34e0-bbe0-a00cf54cd5a4 | -19.53382 | -56.66618 | 2024-10-24 04:38:00 | NOAA-21 | AQUIDAUANA | MATO GROSSO DO SUL | Brasil | 5001102 | 50 | 33 | nan | nan | nan | Pantanal | 3.6 |
| f5533730-b69a-3d74-a92f-b3873852a25e | -19.53341 | -56.69061 | 2024-10-24 04:38:00 | NOAA-21 | CORUMBÁ | MATO GROSSO DO SUL | Brasil | 5003207 | 50 | 33 | nan | nan | nan | Pantanal | 5.1 |
| b43e2ec3-8c4e-3736-9005-5a30c1f3b53d | -19.53317 | -56.58091 | 2024-10-24 04:38:00 | NOAA-21 | AQUIDAUANA | MATO GROSSO DO SUL | Brasil | 5001102 | 50 | 33 | nan | nan | nan | Pantanal | 1.4 |
| eea4f525-75f1-3e60-ab87-65e6d77e4a17 | -19.53307 | -56.6701 | 2024-10-24 04:38:00 | NOAA-21 | CORUMBÁ | MATO GROSSO DO SUL | Brasil | 5003207 | 50 | 33 | nan | nan | nan | Pantanal | 7.8 |
| 1e05d27c-c4a8-3baf-be0a-f1d57230ad7d | -19.53265 | -56.69454 | 2024-10-24 04:38:00 | NOAA-21 | CORUMBÁ | MATO GROSSO DO SUL | Brasil | 5003207 | 50 | 33 | nan | nan | nan | Pantanal | 11.5 |
| caea3123-ff8c-37c0-bdf2-36f0d19df12b | -19.53231 | -56.67403 | 2024-10-24 04:38:00 | NOAA-21 | CORUMBÁ | MATO GROSSO DO SUL | Brasil | 5003207 | 50 | 33 | nan | nan | nan | Pantanal | 7.8 |
| f52d16a0-2dba-3570-a690-e26a88265315 | -19.5319 | -56.69847 | 2024-10-24 04:38:00 | NOAA-21 | CORUMBÁ | MATO GROSSO DO SUL | Brasil | 5003207 | 50 | 33 | nan | nan | nan | Pantanal | 11.5 |
| 470117ff-bbc9-3950-bad1-18d9bdf550f0 | -19.53046 | -56.6614 | 2024-10-24 04:38:00 | NOAA-21 | AQUIDAUANA | MATO GROSSO DO SUL | Brasil | 5001102 | 50 | 33 | nan | nan | nan | Pantanal | 3.6 |
| 513e407b-7d85-3d93-96b4-eff176ef96c1 | -19.52971 | -56.66533 | 2024-10-24 04:38:00 | NOAA-21 | CORUMBÁ | MATO GROSSO DO SUL | Brasil | 5003207 | 50 | 33 | nan | nan | nan | Pantanal | 3.6 |
| f04919e9-bbb3-3ed9-b48f-8b7c32e36fb4 | -19.52955 | -56.58472 | 2024-10-24 04:38:00 | NOAA-21 | AQUIDAUANA | MATO GROSSO DO SUL | Brasil | 5001102 | 50 | 33 | nan | nan | nan | Pantanal | 1.5 |
| a807ffa9-ee54-3a94-ba03-06b1b1829d5f | -19.52853 | -56.69368 | 2024-10-24 04:38:00 | NOAA-21 | CORUMBÁ | MATO GROSSO DO SUL | Brasil | 5003207 | 50 | 33 | nan | nan | nan | Pantanal | 1.9 |
| 7a7d2788-94ee-30a3-84ab-3260cb4186db | -19.52833 | -56.58394 | 2024-10-24 04:38:00 | NOAA-21 | AQUIDAUANA | MATO GROSSO DO SUL | Brasil | 5001102 | 50 | 33 | nan | nan | nan | Pantanal | 1.4 |
| eb0b95dd-cec0-3f89-a5bd-c7580223cfd4 | -19.52684 | -56.59169 | 2024-10-24 04:38:00 | NOAA-21 | AQUIDAUANA | MATO GROSSO DO SUL | Brasil | 5001102 | 50 | 33 | nan | nan | nan | Pantanal | 2.5 |
| f7a74459-2326-3491-ad42-7beaabbba353 | -19.52559 | -56.66447 | 2024-10-24 04:38:00 | NOAA-21 | CORUMBÁ | MATO GROSSO DO SUL | Brasil | 5003207 | 50 | 33 | nan | nan | nan | Pantanal | 4.1 |
| dc250105-1bbe-3038-8fd7-b86c023b9606 | -19.52402 | -56.59162 | 2024-10-24 04:38:00 | NOAA-21 | AQUIDAUANA | MATO GROSSO DO SUL | Brasil | 5001102 | 50 | 33 | nan | nan | nan | Pantanal | 2.2 |
| 87fd9110-415b-3185-b618-11d2c6193036 | -19.52073 | -56.66753 | 2024-10-24 04:38:00 | NOAA-21 | CORUMBÁ | MATO GROSSO DO SUL | Brasil | 5003207 | 50 | 33 | nan | nan | nan | Pantanal | 2.2 |
| 767ac64d-e01b-3977-9a97-3982c8419c78 | -19.51913 | -56.66373 | 2024-10-24 04:38:00 | NOAA-21 | CORUMBÁ | MATO GROSSO DO SUL | Brasil | 5003207 | 50 | 33 | nan | nan | nan | Pantanal | 3.1 |
| daaa5b00-b553-3241-b03a-87017acde0cf | -19.5184 | -56.66766 | 2024-10-24 04:38:00 | NOAA-21 | CORUMBÁ | MATO GROSSO DO SUL | Brasil | 5003207 | 50 | 33 | nan | nan | nan | Pantanal | 4.4 |
| 0086eec8-0ef6-345d-beb2-9f5fda9f4d8f | -19.51775 | -56.60243 | 2024-10-24 04:38:00 | NOAA-21 | AQUIDAUANA | MATO GROSSO DO SUL | Brasil | 5001102 | 50 | 33 | nan | nan | nan | Pantanal | 2.3 |
| 87a5287f-7cc4-359d-a0f9-9c2aabf1c597 | -19.51737 | -56.66275 | 2024-10-24 04:38:00 | NOAA-21 | CORUMBÁ | MATO GROSSO DO SUL | Brasil | 5003207 | 50 | 33 | nan | nan | nan | Pantanal | 2.4 |
| 42883983-67d2-3cd3-9726-cdde7cc8a17d | -19.51661 | -56.66668 | 2024-10-24 04:38:00 | NOAA-21 | CORUMBÁ | MATO GROSSO DO SUL | Brasil | 5003207 | 50 | 33 | nan | nan | nan | Pantanal | 5.1 |
| 6476aa03-af82-3750-a805-aed75d2c0233 | -19.51557 | -56.61414 | 2024-10-24 04:38:00 | NOAA-21 | AQUIDAUANA | MATO GROSSO DO SUL | Brasil | 5001102 | 50 | 33 | nan | nan | nan | Pantanal | 3.1 |
| 1cf110bf-e999-3463-92ba-d444f74a4e83 | -19.51502 | -56.66287 | 2024-10-24 04:38:00 | NOAA-21 | CORUMBÁ | MATO GROSSO DO SUL | Brasil | 5003207 | 50 | 33 | nan | nan | nan | Pantanal | 3.1 |
| 6086960a-4385-3b96-a7ff-88c4a82d0d98 | -19.51484 | -56.61804 | 2024-10-24 04:38:00 | NOAA-21 | AQUIDAUANA | MATO GROSSO DO SUL | Brasil | 5001102 | 50 | 33 | nan | nan | nan | Pantanal | 1.6 |
| 5df895fa-a48f-321d-8725-fe569311ce7f | -19.51429 | -56.6668 | 2024-10-24 04:38:00 | NOAA-21 | CORUMBÁ | MATO GROSSO DO SUL | Brasil | 5003207 | 50 | 33 | nan | nan | nan | Pantanal | 4.4 |
| fb0932ae-8e02-3f97-8137-14ff259fd58c | -19.51411 | -56.62195 | 2024-10-24 04:38:00 | NOAA-21 | CORUMBÁ | MATO GROSSO DO SUL | Brasil | 5003207 | 50 | 33 | nan | nan | nan | Pantanal | 1.6 |
| 56230282-1b94-3e0e-953d-c8a4f444089b | -19.51326 | -56.6619 | 2024-10-24 04:38:00 | NOAA-21 | CORUMBÁ | MATO GROSSO DO SUL | Brasil | 5003207 | 50 | 33 | nan | nan | nan | Pantanal | 2.4 |
| 1a9fc143-b559-39f5-9590-5e8cd05b306b | -19.5125 | -56.66582 | 2024-10-24 04:38:00 | NOAA-21 | CORUMBÁ | MATO GROSSO DO SUL | Brasil | 5003207 | 50 | 33 | nan | nan | nan | Pantanal | 5.1 |
| ea8fa9af-9f53-32a4-a34c-c66b4fd5eb97 | -19.51018 | -56.66593 | 2024-10-24 04:38:00 | NOAA-21 | CORUMBÁ | MATO GROSSO DO SUL | Brasil | 5003207 | 50 | 33 | nan | nan | nan | Pantanal | 8.3 |
| 6e01c56a-d140-3559-99b4-5674e2e0ec6a | -19.50781 | -56.63282 | 2024-10-24 04:38:00 | NOAA-21 | CORUMBÁ | MATO GROSSO DO SUL | Brasil | 5003207 | 50 | 33 | nan | nan | nan | Pantanal | 4.0 |
| be09bcef-6011-3d40-9f38-86b0354270be | -19.50708 | -56.63674 | 2024-10-24 04:38:00 | NOAA-21 | CORUMBÁ | MATO GROSSO DO SUL | Brasil | 5003207 | 50 | 33 | nan | nan | nan | Pantanal | 4.0 |
| 05f5f8a0-ecee-3667-a54a-19284560d827 | -19.50679 | -56.66114 | 2024-10-24 04:38:00 | NOAA-21 | CORUMBÁ | MATO GROSSO DO SUL | Brasil | 5003207 | 50 | 33 | nan | nan | nan | Pantanal | 4.4 |
| d2984365-eb3b-3102-8052-8443097a5337 | -19.50635 | -56.64065 | 2024-10-24 04:38:00 | NOAA-21 | CORUMBÁ | MATO GROSSO DO SUL | Brasil | 5003207 | 50 | 33 | nan | nan | nan | Pantanal | 10.6 |
| ae98fb56-e20c-3db1-8515-b0435eb95cad | -19.50606 | -56.66507 | 2024-10-24 04:38:00 | NOAA-21 | CORUMBÁ | MATO GROSSO DO SUL | Brasil | 5003207 | 50 | 33 | nan | nan | nan | Pantanal | 8.3 |
| b1206b7b-5be6-366b-b6f2-ed6300004b9e | -19.50562 | -56.64458 | 2024-10-24 04:38:00 | NOAA-21 | CORUMBÁ | MATO GROSSO DO SUL | Brasil | 5003207 | 50 | 33 | nan | nan | nan | Pantanal | 10.6 |
| efbc40af-48fc-3d3d-a6be-945c540bb84c | -19.50533 | -56.669 | 2024-10-24 04:38:00 | NOAA-21 | CORUMBÁ | MATO GROSSO DO SUL | Brasil | 5003207 | 50 | 33 | nan | nan | nan | Pantanal | 8.3 |
| f25df187-0e03-3737-a7ef-edb0cc18e7ae | -19.50489 | -56.6485 | 2024-10-24 04:38:00 | NOAA-21 | CORUMBÁ | MATO GROSSO DO SUL | Brasil | 5003207 | 50 | 33 | nan | nan | nan | Pantanal | 7.0 |
| a570fb16-4fac-3f34-b3c3-7c95aef1ccb7 | -19.50415 | -56.65242 | 2024-10-24 04:38:00 | NOAA-21 | CORUMBÁ | MATO GROSSO DO SUL | Brasil | 5003207 | 50 | 33 | nan | nan | nan | Pantanal | 7.0 |
| 956164b9-50a1-37a3-b2d2-a614439a8c66 | -19.50342 | -56.65635 | 2024-10-24 04:38:00 | NOAA-21 | CORUMBÁ | MATO GROSSO DO SUL | Brasil | 5003207 | 50 | 33 | nan | nan | nan | Pantanal | 11.8 |
| 1de18105-5f64-3e35-aa61-0af90f765918 | -19.50298 | -56.63588 | 2024-10-24 04:38:00 | NOAA-21 | CORUMBÁ | MATO GROSSO DO SUL | Brasil | 5003207 | 50 | 33 | nan | nan | nan | Pantanal | 4.0 |
| fc4a6694-5c7b-32a1-8c67-1673ac87f204 | -19.50268 | -56.66027 | 2024-10-24 04:38:00 | NOAA-21 | CORUMBÁ | MATO GROSSO DO SUL | Brasil | 5003207 | 50 | 33 | nan | nan | nan | Pantanal | 11.8 |
| ce127ddf-3307-39f0-8e73-2f9868dd2d72 | -19.50224 | -56.63979 | 2024-10-24 04:38:00 | NOAA-21 | CORUMBÁ | MATO GROSSO DO SUL | Brasil | 5003207 | 50 | 33 | nan | nan | nan | Pantanal | 10.6 |
| 560c767a-3c25-3569-b0ca-5f8a4b67f48f | -19.50195 | -56.6642 | 2024-10-24 04:38:00 | NOAA-21 | CORUMBÁ | MATO GROSSO DO SUL | Brasil | 5003207 | 50 | 33 | nan | nan | nan | Pantanal | 9.1 |
| 95ece1cc-9ea0-308f-bab8-3339bd87749b | -19.50151 | -56.64372 | 2024-10-24 04:38:00 | NOAA-21 | CORUMBÁ | MATO GROSSO DO SUL | Brasil | 5003207 | 50 | 33 | nan | nan | nan | Pantanal | 10.6 |
| 892c1f6c-c5ca-3c1b-bbeb-7022b685d09f | -19.50121 | -56.66813 | 2024-10-24 04:38:00 | NOAA-21 | CORUMBÁ | MATO GROSSO DO SUL | Brasil | 5003207 | 50 | 33 | nan | nan | nan | Pantanal | 9.1 |
| cafa5610-7ceb-33bb-af74-05640edceef4 | -19.50077 | -56.64764 | 2024-10-24 04:38:00 | NOAA-21 | CORUMBÁ | MATO GROSSO DO SUL | Brasil | 5003207 | 50 | 33 | nan | nan | nan | Pantanal | 7.0 |
| 37551dbd-04d5-3040-a5c5-2841e7372031 | -19.50004 | -56.65156 | 2024-10-24 04:38:00 | NOAA-21 | CORUMBÁ | MATO GROSSO DO SUL | Brasil | 5003207 | 50 | 33 | nan | nan | nan | Pantanal | 7.0 |
| ced7d0c1-a2ab-39be-bb2f-4ab45a50b18c | -19.4993 | -56.65548 | 2024-10-24 04:38:00 | NOAA-21 | CORUMBÁ | MATO GROSSO DO SUL | Brasil | 5003207 | 50 | 33 | nan | nan | nan | Pantanal | 11.8 |
| 791a46c9-c446-3ecb-a3ca-897f68843c97 | -19.49857 | -56.65941 | 2024-10-24 04:38:00 | NOAA-21 | CORUMBÁ | MATO GROSSO DO SUL | Brasil | 5003207 | 50 | 33 | nan | nan | nan | Pantanal | 11.8 |
| b6f8a134-879f-30bc-b19c-85edb1899786 | -19.49783 | -56.66333 | 2024-10-24 04:38:00 | NOAA-21 | CORUMBÁ | MATO GROSSO DO SUL | Brasil | 5003207 | 50 | 33 | nan | nan | nan | Pantanal | 9.1 |
| 5079b5d6-0ce8-39c7-a868-987736db34bd | -19.49593 | -56.6507 | 2024-10-24 04:38:00 | NOAA-21 | CORUMBÁ | MATO GROSSO DO SUL | Brasil | 5003207 | 50 | 33 | nan | nan | nan | Pantanal | 5.7 |
| d3d0d20b-ae59-33c6-bc65-4e11cda39aff | -19.49519 | -56.65462 | 2024-10-24 04:38:00 | NOAA-21 | CORUMBÁ | MATO GROSSO DO SUL | Brasil | 5003207 | 50 | 33 | nan | nan | nan | Pantanal | 2.6 |
| dbe7806e-2564-306a-b692-165df19c211f | -22.19075 | -56.91505 | 2024-10-24 04:38:00 | NOAA-21 | BELA VISTA | MATO GROSSO DO SUL | Brasil | 5002100 | 50 | 33 | nan | nan | nan | Cerrado | 1.5 |
| d2c782c8-3065-36b1-985d-3392e84031c1 | -18.08719 | -57.31347 | 2024-10-24 04:38:00 | NOAA-21 | CORUMBÁ | MATO GROSSO DO SUL | Brasil | 5003207 | 50 | 33 | nan | nan | nan | Pantanal | 1.9 |
| f244baec-b9df-3a22-807d-c6039066f067 | -18.11181 | -57.328 | 2024-10-24 04:38:00 | NOAA-21 | CORUMBÁ | MATO GROSSO DO SUL | Brasil | 5003207 | 50 | 33 | nan | nan | nan | Pantanal | 2.6 |
| b033abd2-148c-3195-beba-59147b47ca3f | -18.10741 | -57.32708 | 2024-10-24 04:38:00 | NOAA-21 | CORUMBÁ | MATO GROSSO DO SUL | Brasil | 5003207 | 50 | 33 | nan | nan | nan | Pantanal | 2.6 |
| 416e0860-fbbe-3250-bee7-47d870bac958 | -18.09684 | -57.33431 | 2024-10-24 04:38:00 | NOAA-21 | CORUMBÁ | MATO GROSSO DO SUL | Brasil | 5003207 | 50 | 33 | nan | nan | nan | Pantanal | 3.8 |
| 2bee1a7c-2edb-34b2-9120-583d53f59ccb | -18.09156 | -57.33791 | 2024-10-24 04:38:00 | NOAA-21 | CORUMBÁ | MATO GROSSO DO SUL | Brasil | 5003207 | 50 | 33 | nan | nan | nan | Pantanal | 4.5 |
| 15e28fd9-730b-362f-9940-f43edd0946d0 | -18.09092 | -57.29723 | 2024-10-24 04:38:00 | NOAA-21 | CORUMBÁ | MATO GROSSO DO SUL | Brasil | 5003207 | 50 | 33 | nan | nan | nan | Pantanal | 8.1 |
| bf7f3870-3693-3a11-acfe-4d1630ff5f36 | -18.09067 | -57.34244 | 2024-10-24 04:38:00 | NOAA-21 | CORUMBÁ | MATO GROSSO DO SUL | Brasil | 5003207 | 50 | 33 | nan | nan | nan | Pantanal | 4.0 |
| 3ac6e617-e7e1-3f0c-8edb-d5095d003b5c | -18.08985 | -57.29996 | 2024-10-24 04:38:00 | NOAA-21 | CORUMBÁ | MATO GROSSO DO SUL | Brasil | 5003207 | 50 | 33 | nan | nan | nan | Pantanal | 11.9 |
| 409032f6-bd11-38ea-be46-41060f221283 | -18.08922 | -57.30626 | 2024-10-24 04:38:00 | NOAA-21 | CORUMBÁ | MATO GROSSO DO SUL | Brasil | 5003207 | 50 | 33 | nan | nan | nan | Pantanal | 2.3 |
| bbdc3fb9-6995-3c97-893d-bf53c88c5c8b | -18.08897 | -57.30446 | 2024-10-24 04:38:00 | NOAA-21 | CORUMBÁ | MATO GROSSO DO SUL | Brasil | 5003207 | 50 | 33 | nan | nan | nan | Pantanal | 2.6 |
| 5776d39a-702b-3eeb-b3f6-8af50227d09a | -18.08808 | -57.30896 | 2024-10-24 04:38:00 | NOAA-21 | CORUMBÁ | MATO GROSSO DO SUL | Brasil | 5003207 | 50 | 33 | nan | nan | nan | Pantanal | 2.6 |
| 33aaa65d-a1ff-3e93-adeb-b9905381d6a5 | -18.08715 | -57.33699 | 2024-10-24 04:38:00 | NOAA-21 | CORUMBÁ | MATO GROSSO DO SUL | Brasil | 5003207 | 50 | 33 | nan | nan | nan | Pantanal | 4.5 |
| a8369f19-e4a7-340a-8957-df970d5b13f2 | -18.08653 | -57.29631 | 2024-10-24 04:38:00 | NOAA-21 | CORUMBÁ | MATO GROSSO DO SUL | Brasil | 5003207 | 50 | 33 | nan | nan | nan | Pantanal | 8.1 |
| 80d85a1c-096e-3957-9342-454c6810fd84 | -18.08626 | -57.34153 | 2024-10-24 04:38:00 | NOAA-21 | CORUMBÁ | MATO GROSSO DO SUL | Brasil | 5003207 | 50 | 33 | nan | nan | nan | Pantanal | 4.0 |
| ee02ed7b-e4a1-3cfb-8bd0-3789e0e903fd | -18.08568 | -57.30082 | 2024-10-24 04:38:00 | NOAA-21 | CORUMBÁ | MATO GROSSO DO SUL | Brasil | 5003207 | 50 | 33 | nan | nan | nan | Pantanal | 8.1 |
| 14cebbe8-e7fc-3dd2-b424-d4439af2af92 | -18.08546 | -57.29905 | 2024-10-24 04:38:00 | NOAA-21 | CORUMBÁ | MATO GROSSO DO SUL | Brasil | 5003207 | 50 | 33 | nan | nan | nan | Pantanal | 11.9 |
| abc10983-9dc9-3a3a-aec2-5c2583231942 | -18.08482 | -57.30534 | 2024-10-24 04:38:00 | NOAA-21 | CORUMBÁ | MATO GROSSO DO SUL | Brasil | 5003207 | 50 | 33 | nan | nan | nan | Pantanal | 2.3 |
| 891a9bdd-9da8-390c-aa7a-07dbae8a6611 | -18.08457 | -57.30355 | 2024-10-24 04:38:00 | NOAA-21 | CORUMBÁ | MATO GROSSO DO SUL | Brasil | 5003207 | 50 | 33 | nan | nan | nan | Pantanal | 2.6 |
| 7067b554-e2d9-3e79-86e1-7405c397228c | -18.08397 | -57.30986 | 2024-10-24 04:38:00 | NOAA-21 | CORUMBÁ | MATO GROSSO DO SUL | Brasil | 5003207 | 50 | 33 | nan | nan | nan | Pantanal | 2.3 |
| d7b1d870-2e88-3223-8156-808afecb5e44 | -18.08369 | -57.30805 | 2024-10-24 04:38:00 | NOAA-21 | CORUMBÁ | MATO GROSSO DO SUL | Brasil | 5003207 | 50 | 33 | nan | nan | nan | Pantanal | 2.6 |
| 678fc304-e6ce-348b-ac97-2fd441d6a40f | -18.08323 | -57.33798 | 2024-10-24 04:38:00 | NOAA-21 | CORUMBÁ | MATO GROSSO DO SUL | Brasil | 5003207 | 50 | 33 | nan | nan | nan | Pantanal | 5.6 |


[Clique aqui para ver as próximas entradas](README59.md)
