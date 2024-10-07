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

## Dados Diários - Página 138

| ID | Latitude | Longitude | Data/Hora GMT | Satélite | Município | Estado | País | Município ID | Estado ID | País ID | Dias sem Chuva | Precipitação | Risco de Fogo | Bioma | FRP |
|----|----------|-----------|---------------|----------|-----------|--------|------|--------------|-----------|---------|----------------|--------------|----------------|-------|-----|
| 61b53ccc-da40-355a-8e01-aa94d95a601b | -17.11199 | -57.38676 | 2024-10-07 05:44:00 | NOAA-20 | CÁCERES | MATO GROSSO | Brasil | 5102504 | 51 | 33 | nan | nan | nan | Pantanal | 2.7 |
| 7fddc39d-a2c3-336c-a7a2-e72586f5fcbd | -17.11155 | -57.39074 | 2024-10-07 05:44:00 | NOAA-20 | CÁCERES | MATO GROSSO | Brasil | 5102504 | 51 | 33 | nan | nan | nan | Pantanal | 3.5 |
| 5ae9b302-78bd-305a-9a0f-cae8d4ab1c1d | -17.11009 | -57.3753 | 2024-10-07 05:44:00 | NOAA-20 | CÁCERES | MATO GROSSO | Brasil | 5102504 | 51 | 33 | nan | nan | nan | Pantanal | 2.6 |
| b943e160-ee81-3964-8ff2-d636e2ac634a | -17.10927 | -57.38327 | 2024-10-07 05:44:00 | NOAA-20 | CÁCERES | MATO GROSSO | Brasil | 5102504 | 51 | 33 | nan | nan | nan | Pantanal | 3.8 |
| fe7041b2-5178-3a4c-a378-71121cf364de | -17.10887 | -57.38724 | 2024-10-07 05:44:00 | NOAA-20 | CÁCERES | MATO GROSSO | Brasil | 5102504 | 51 | 33 | nan | nan | nan | Pantanal | 2.6 |
| 2dc3d268-f7fa-32ec-89cd-1f74b8644a4e | -17.10846 | -57.39123 | 2024-10-07 05:44:00 | NOAA-20 | CÁCERES | MATO GROSSO | Brasil | 5102504 | 51 | 33 | nan | nan | nan | Pantanal | 2.6 |
| a848af06-0593-3fbd-9928-8bca05291952 | -17.10806 | -57.39521 | 2024-10-07 05:44:00 | NOAA-20 | CÁCERES | MATO GROSSO | Brasil | 5102504 | 51 | 33 | nan | nan | nan | Pantanal | 2.2 |
| b61bb8cc-cf67-3913-87f8-1cd72a1dfdab | -17.10719 | -57.37816 | 2024-10-07 05:44:00 | NOAA-20 | CÁCERES | MATO GROSSO | Brasil | 5102504 | 51 | 33 | nan | nan | nan | Pantanal | 3.7 |
| 94ec0bf7-2eac-3b3c-acb3-f6ef1a259703 | -17.10633 | -57.3861 | 2024-10-07 05:44:00 | NOAA-20 | CÁCERES | MATO GROSSO | Brasil | 5102504 | 51 | 33 | nan | nan | nan | Pantanal | 3.9 |
| bcba10d9-9ffc-3280-bb6c-bacd0c657b30 | -17.10589 | -57.39008 | 2024-10-07 05:44:00 | NOAA-20 | CÁCERES | MATO GROSSO | Brasil | 5102504 | 51 | 33 | nan | nan | nan | Pantanal | 2.1 |
| 2804b23f-5005-381b-950b-6169a58ef56f | -17.10546 | -57.39407 | 2024-10-07 05:44:00 | NOAA-20 | CÁCERES | MATO GROSSO | Brasil | 5102504 | 51 | 33 | nan | nan | nan | Pantanal | 2.1 |
| ca23603b-ee9b-3e92-bb0d-f638211f41c3 | -17.10442 | -57.37463 | 2024-10-07 05:44:00 | NOAA-20 | POCONÉ | MATO GROSSO | Brasil | 5106505 | 51 | 33 | nan | nan | nan | Pantanal | 2.6 |
| b03faf39-dc74-3bc4-8d9d-e126736cacae | -17.10402 | -57.37862 | 2024-10-07 05:44:00 | NOAA-20 | CÁCERES | MATO GROSSO | Brasil | 5102504 | 51 | 33 | nan | nan | nan | Pantanal | 3.8 |
| 60baf9eb-abdd-31bd-be9d-d1eaf85925f7 | -17.10361 | -57.38261 | 2024-10-07 05:44:00 | NOAA-20 | CÁCERES | MATO GROSSO | Brasil | 5102504 | 51 | 33 | nan | nan | nan | Pantanal | 3.8 |
| 8caf5261-a0cd-377e-9b05-15bdb7975ef5 | -17.1032 | -57.38658 | 2024-10-07 05:44:00 | NOAA-20 | CÁCERES | MATO GROSSO | Brasil | 5102504 | 51 | 33 | nan | nan | nan | Pantanal | 2.6 |
| e718c3b0-334c-3e05-9c68-6fa0bcbaec89 | -17.10239 | -57.39457 | 2024-10-07 05:44:00 | NOAA-20 | CÁCERES | MATO GROSSO | Brasil | 5102504 | 51 | 33 | nan | nan | nan | Pantanal | 2.2 |
| 8f4912df-64d8-3cef-b665-0ebbf667e678 | -17.10153 | -57.37751 | 2024-10-07 05:44:00 | NOAA-20 | CÁCERES | MATO GROSSO | Brasil | 5102504 | 51 | 33 | nan | nan | nan | Pantanal | 3.7 |
| 79361876-7151-3ea3-ab85-a6b1f4895e23 | -17.1011 | -57.38149 | 2024-10-07 05:44:00 | NOAA-20 | CÁCERES | MATO GROSSO | Brasil | 5102504 | 51 | 33 | nan | nan | nan | Pantanal | 3.9 |
| fe774840-7eb7-336b-8c2f-b6e7205bcf08 | -17.10066 | -57.38547 | 2024-10-07 05:44:00 | NOAA-20 | CÁCERES | MATO GROSSO | Brasil | 5102504 | 51 | 33 | nan | nan | nan | Pantanal | 3.9 |
| 03d0e230-0d7c-3e77-ac9e-3a103d1a28f1 | -17.10023 | -57.38944 | 2024-10-07 05:44:00 | NOAA-20 | CÁCERES | MATO GROSSO | Brasil | 5102504 | 51 | 33 | nan | nan | nan | Pantanal | 2.1 |
| 0e32542a-3473-3b51-b65b-f4bb69515e47 | -17.17497 | -57.35854 | 2024-10-07 05:44:00 | NOAA-20 | CÁCERES | MATO GROSSO | Brasil | 5102504 | 51 | 33 | nan | nan | nan | Pantanal | 3.4 |
| 3fbcd6be-c49e-396d-b513-70c4dd3461ac | -17.17226 | -57.32978 | 2024-10-07 05:44:00 | NOAA-20 | POCONÉ | MATO GROSSO | Brasil | 5106505 | 51 | 33 | nan | nan | nan | Pantanal | 2.1 |
| 4d58798e-dd8c-394f-8a82-598c989c149b | -17.17183 | -57.33381 | 2024-10-07 05:44:00 | NOAA-20 | POCONÉ | MATO GROSSO | Brasil | 5106505 | 51 | 33 | nan | nan | nan | Pantanal | 2.1 |
| 3b127438-8b36-35f6-bae2-85fff69a708e | -17.17141 | -57.33783 | 2024-10-07 05:44:00 | NOAA-20 | POCONÉ | MATO GROSSO | Brasil | 5106505 | 51 | 33 | nan | nan | nan | Pantanal | 14.3 |
| 374f4113-79ff-3b80-8ab3-9cefe24553f8 | -17.17099 | -57.34184 | 2024-10-07 05:44:00 | NOAA-20 | POCONÉ | MATO GROSSO | Brasil | 5106505 | 51 | 33 | nan | nan | nan | Pantanal | 14.3 |
| d0632bf0-b348-3770-ad8c-8523858cf4cf | -17.17056 | -57.34584 | 2024-10-07 05:44:00 | NOAA-20 | POCONÉ | MATO GROSSO | Brasil | 5106505 | 51 | 33 | nan | nan | nan | Pantanal | 39.8 |
| d2b7cbd7-0083-352f-b302-221aa83560da | -17.17014 | -57.34986 | 2024-10-07 05:44:00 | NOAA-20 | POCONÉ | MATO GROSSO | Brasil | 5106505 | 51 | 33 | nan | nan | nan | Pantanal | 39.8 |
| ff187726-f9e2-32d2-a946-45959709723d | -17.16972 | -57.35388 | 2024-10-07 05:44:00 | NOAA-20 | POCONÉ | MATO GROSSO | Brasil | 5106505 | 51 | 33 | nan | nan | nan | Pantanal | 10.6 |
| 205cead7-6365-3a41-be35-18241d52fb99 | -17.16929 | -57.35789 | 2024-10-07 05:44:00 | NOAA-20 | POCONÉ | MATO GROSSO | Brasil | 5106505 | 51 | 33 | nan | nan | nan | Pantanal | 10.6 |
| df6ba1cb-bff5-31f5-a75f-afb5a6a3acba | -17.16887 | -57.36192 | 2024-10-07 05:44:00 | NOAA-20 | POCONÉ | MATO GROSSO | Brasil | 5106505 | 51 | 33 | nan | nan | nan | Pantanal | 3.5 |
| 69bc777b-1e46-39b8-ae01-b8518975bde3 | -17.16615 | -57.33315 | 2024-10-07 05:44:00 | NOAA-20 | POCONÉ | MATO GROSSO | Brasil | 5106505 | 51 | 33 | nan | nan | nan | Pantanal | 2.1 |
| 87eb854d-3a0e-3b0e-87b6-5309b5c8e18a | -17.16573 | -57.33718 | 2024-10-07 05:44:00 | NOAA-20 | POCONÉ | MATO GROSSO | Brasil | 5106505 | 51 | 33 | nan | nan | nan | Pantanal | 14.3 |
| 440540d1-8452-3a39-b6b5-90a52057a213 | -17.16531 | -57.34119 | 2024-10-07 05:44:00 | NOAA-20 | POCONÉ | MATO GROSSO | Brasil | 5106505 | 51 | 33 | nan | nan | nan | Pantanal | 14.3 |
| f7b5d260-a13b-3799-9793-dbb3cfd1535b | -17.16488 | -57.34518 | 2024-10-07 05:44:00 | NOAA-20 | POCONÉ | MATO GROSSO | Brasil | 5106505 | 51 | 33 | nan | nan | nan | Pantanal | 39.8 |
| 1ef5b065-5d5a-3c2d-9cbd-7cfa5245eaa2 | -17.16446 | -57.34919 | 2024-10-07 05:44:00 | NOAA-20 | POCONÉ | MATO GROSSO | Brasil | 5106505 | 51 | 33 | nan | nan | nan | Pantanal | 39.8 |
| 82e466e9-6e47-3f6b-a42a-40a33f4a9458 | -17.16404 | -57.3532 | 2024-10-07 05:44:00 | NOAA-20 | POCONÉ | MATO GROSSO | Brasil | 5106505 | 51 | 33 | nan | nan | nan | Pantanal | 10.6 |
| 91b550b4-37d3-3d7e-9774-eefc63b2b602 | -17.1634 | -57.41371 | 2024-10-07 05:44:00 | NOAA-20 | CÁCERES | MATO GROSSO | Brasil | 5102504 | 51 | 33 | nan | nan | nan | Pantanal | 2.2 |
| 417f37b5-4136-3171-bee1-0c417204677f | -17.16004 | -57.33653 | 2024-10-07 05:44:00 | NOAA-20 | POCONÉ | MATO GROSSO | Brasil | 5106505 | 51 | 33 | nan | nan | nan | Pantanal | 8.1 |
| c9b84522-0723-3906-9483-2cf8134dd33b | -17.15962 | -57.34053 | 2024-10-07 05:44:00 | NOAA-20 | POCONÉ | MATO GROSSO | Brasil | 5106505 | 51 | 33 | nan | nan | nan | Pantanal | 8.1 |
| 63c8d7bf-5b26-3018-965a-878527bfe371 | -16.51451 | -57.73351 | 2024-10-07 05:44:00 | NOAA-20 | CÁCERES | MATO GROSSO | Brasil | 5102504 | 51 | 33 | nan | nan | nan | Pantanal | 1.2 |
| d841e667-5cde-3a34-b297-7bb85310ee68 | -16.51411 | -57.73718 | 2024-10-07 05:44:00 | NOAA-20 | CÁCERES | MATO GROSSO | Brasil | 5102504 | 51 | 33 | nan | nan | nan | Pantanal | 1.0 |
| 3ef57cec-1efc-3639-b747-411c9023d23a | -16.51369 | -57.74088 | 2024-10-07 05:44:00 | NOAA-20 | CÁCERES | MATO GROSSO | Brasil | 5102504 | 51 | 33 | nan | nan | nan | Pantanal | 1.0 |
| b654375a-a992-30c2-afea-ab19086c2ad0 | -16.51328 | -57.74459 | 2024-10-07 05:44:00 | NOAA-20 | CÁCERES | MATO GROSSO | Brasil | 5102504 | 51 | 33 | nan | nan | nan | Pantanal | 1.2 |
| 85710143-72b7-3555-9db7-ab300eed0a98 | -16.51019 | -57.72231 | 2024-10-07 05:44:00 | NOAA-20 | CÁCERES | MATO GROSSO | Brasil | 5102504 | 51 | 33 | nan | nan | nan | Pantanal | 1.4 |
| 761fcc90-c7db-3737-9d4c-693f1fe97c7a | -16.50777 | -57.74412 | 2024-10-07 05:44:00 | NOAA-20 | CÁCERES | MATO GROSSO | Brasil | 5102504 | 51 | 33 | nan | nan | nan | Pantanal | 1.2 |
| f32214e3-ff5d-39d5-a407-02593ce5df2c | -16.5043 | -57.72513 | 2024-10-07 05:44:00 | NOAA-20 | CÁCERES | MATO GROSSO | Brasil | 5102504 | 51 | 33 | nan | nan | nan | Pantanal | 1.5 |
| 01e286d3-085c-3f5b-a5af-6ac3e98ea8c5 | -16.5031 | -57.73602 | 2024-10-07 05:44:00 | NOAA-20 | CÁCERES | MATO GROSSO | Brasil | 5102504 | 51 | 33 | nan | nan | nan | Pantanal | 2.3 |
| fbeed363-9dd0-3939-a663-d55de62f0646 | -16.50269 | -57.73978 | 2024-10-07 05:44:00 | NOAA-20 | CÁCERES | MATO GROSSO | Brasil | 5102504 | 51 | 33 | nan | nan | nan | Pantanal | 2.3 |
| 7b658608-43b3-3eea-beab-54921e4dada0 | -16.50227 | -57.74354 | 2024-10-07 05:44:00 | NOAA-20 | CÁCERES | MATO GROSSO | Brasil | 5102504 | 51 | 33 | nan | nan | nan | Pantanal | 1.4 |
| 33d9bc49-e0a0-3409-8a88-6b2cd67da6bd | -16.49883 | -57.7243 | 2024-10-07 05:44:00 | NOAA-20 | CÁCERES | MATO GROSSO | Brasil | 5102504 | 51 | 33 | nan | nan | nan | Pantanal | 1.5 |
| f0a08880-87f2-32e3-b97f-e3362eefa0f1 | -16.49803 | -57.73155 | 2024-10-07 05:44:00 | NOAA-20 | CÁCERES | MATO GROSSO | Brasil | 5102504 | 51 | 33 | nan | nan | nan | Pantanal | 4.3 |
| 31f01a68-f97e-3642-a2f2-f4834203e451 | -16.49762 | -57.73529 | 2024-10-07 05:44:00 | NOAA-20 | CÁCERES | MATO GROSSO | Brasil | 5102504 | 51 | 33 | nan | nan | nan | Pantanal | 2.3 |
| 34d8070b-2e62-39ae-b728-30357ad25982 | -16.4972 | -57.73904 | 2024-10-07 05:44:00 | NOAA-20 | CÁCERES | MATO GROSSO | Brasil | 5102504 | 51 | 33 | nan | nan | nan | Pantanal | 2.3 |
| 3bed40d3-9b95-3f4b-831e-126e6fe55871 | -16.49679 | -57.74281 | 2024-10-07 05:44:00 | NOAA-20 | CÁCERES | MATO GROSSO | Brasil | 5102504 | 51 | 33 | nan | nan | nan | Pantanal | 1.4 |
| 9cabe64d-909c-3c31-b8bb-3ce15be00aac | -16.49294 | -57.7272 | 2024-10-07 05:44:00 | NOAA-20 | CÁCERES | MATO GROSSO | Brasil | 5102504 | 51 | 33 | nan | nan | nan | Pantanal | 1.2 |
| a5f3e5c9-5741-3ae7-b1d0-56fe9134934c | -16.49173 | -57.73825 | 2024-10-07 05:44:00 | NOAA-20 | CÁCERES | MATO GROSSO | Brasil | 5102504 | 51 | 33 | nan | nan | nan | Pantanal | 1.8 |
| c8b54b84-f461-3df8-a561-5b8654e52e77 | -16.58973 | -57.15384 | 2024-10-07 05:44:00 | NOAA-20 | POCONÉ | MATO GROSSO | Brasil | 5106505 | 51 | 33 | nan | nan | nan | Pantanal | 18.0 |
| 6c09ad85-5236-3e54-83af-0892f01979c1 | -16.58491 | -57.14503 | 2024-10-07 05:44:00 | NOAA-20 | POCONÉ | MATO GROSSO | Brasil | 5106505 | 51 | 33 | nan | nan | nan | Pantanal | 5.6 |
| 1f727720-841f-3040-b8f3-03fa88819d31 | -16.58446 | -57.14917 | 2024-10-07 05:44:00 | NOAA-20 | POCONÉ | MATO GROSSO | Brasil | 5106505 | 51 | 33 | nan | nan | nan | Pantanal | 18.0 |
| 0d7ca872-3797-388a-98a1-292c4033a7c7 | -16.58401 | -57.15331 | 2024-10-07 05:44:00 | NOAA-20 | POCONÉ | MATO GROSSO | Brasil | 5106505 | 51 | 33 | nan | nan | nan | Pantanal | 18.0 |
| 27eff1be-836c-31d3-b10e-cd90b7676627 | -16.58357 | -57.15732 | 2024-10-07 05:44:00 | NOAA-20 | POCONÉ | MATO GROSSO | Brasil | 5106505 | 51 | 33 | nan | nan | nan | Pantanal | 8.4 |
| 429e881f-7876-333b-a3cd-24ec0a67eb85 | -16.58315 | -57.16125 | 2024-10-07 05:44:00 | NOAA-20 | POCONÉ | MATO GROSSO | Brasil | 5106505 | 51 | 33 | nan | nan | nan | Pantanal | 8.4 |
| e1d15d37-9c48-38cf-8059-175de2429e10 | -16.57919 | -57.14439 | 2024-10-07 05:44:00 | NOAA-20 | POCONÉ | MATO GROSSO | Brasil | 5106505 | 51 | 33 | nan | nan | nan | Pantanal | 2.4 |
| 170d1b3e-3cf8-33dd-9f58-d0c956b244d8 | -16.57874 | -57.14858 | 2024-10-07 05:44:00 | NOAA-20 | POCONÉ | MATO GROSSO | Brasil | 5106505 | 51 | 33 | nan | nan | nan | Pantanal | 2.4 |
| 53d09813-6348-3dff-9160-5476a2472b0a | -16.57828 | -57.15282 | 2024-10-07 05:44:00 | NOAA-20 | POCONÉ | MATO GROSSO | Brasil | 5106505 | 51 | 33 | nan | nan | nan | Pantanal | 2.4 |
| fbfd80ae-654c-3616-9be3-abc28058af67 | -16.57785 | -57.15681 | 2024-10-07 05:44:00 | NOAA-20 | POCONÉ | MATO GROSSO | Brasil | 5106505 | 51 | 33 | nan | nan | nan | Pantanal | 4.1 |
| eabf7b55-ecc5-3647-91b0-ee1a5f2e54d3 | -16.57303 | -57.14791 | 2024-10-07 05:44:00 | NOAA-20 | POCONÉ | MATO GROSSO | Brasil | 5106505 | 51 | 33 | nan | nan | nan | Pantanal | 2.4 |
| 00954d34-d752-398b-a9da-574858082c99 | -16.57257 | -57.15218 | 2024-10-07 05:44:00 | NOAA-20 | POCONÉ | MATO GROSSO | Brasil | 5106505 | 51 | 33 | nan | nan | nan | Pantanal | 2.4 |
| 651ecdef-372e-3fcf-9010-c2f97389ed0e | -16.57043 | -57.17202 | 2024-10-07 05:44:00 | NOAA-20 | POCONÉ | MATO GROSSO | Brasil | 5106505 | 51 | 33 | nan | nan | nan | Pantanal | 2.8 |
| 3d199738-b742-3353-b28d-cc689041d281 | -16.56999 | -57.17604 | 2024-10-07 05:44:00 | NOAA-20 | POCONÉ | MATO GROSSO | Brasil | 5106505 | 51 | 33 | nan | nan | nan | Pantanal | 2.8 |
| 5c1958c9-e154-3490-9a4d-8f00cd62d8ab | -16.56087 | -57.2602 | 2024-10-07 05:44:00 | NOAA-20 | CÁCERES | MATO GROSSO | Brasil | 5102504 | 51 | 33 | nan | nan | nan | Pantanal | 4.7 |
| b93e2e13-36c7-38a9-866d-bfe8226b35c0 | -16.56082 | -57.20757 | 2024-10-07 05:44:00 | NOAA-20 | POCONÉ | MATO GROSSO | Brasil | 5106505 | 51 | 33 | nan | nan | nan | Pantanal | 1.8 |
| 66ca0989-08f6-3f11-ad6b-2659283243f5 | -16.49558 | -57.28093 | 2024-10-07 05:44:00 | NOAA-20 | CÁCERES | MATO GROSSO | Brasil | 5102504 | 51 | 33 | nan | nan | nan | Pantanal | 0.7 |
| 959b74dd-23a2-32d6-8545-c3b9a9b1f8a9 | -16.49517 | -57.28484 | 2024-10-07 05:44:00 | NOAA-20 | CÁCERES | MATO GROSSO | Brasil | 5102504 | 51 | 33 | nan | nan | nan | Pantanal | 1.4 |
| d07bf3bd-d2fa-38d5-9c18-6b474b64ef80 | -16.49074 | -57.27242 | 2024-10-07 05:44:00 | NOAA-20 | CÁCERES | MATO GROSSO | Brasil | 5102504 | 51 | 33 | nan | nan | nan | Pantanal | 1.3 |
| f3382f6c-c0fd-3949-83cb-40a411a3d2a5 | -16.49032 | -57.27639 | 2024-10-07 05:44:00 | NOAA-20 | CÁCERES | MATO GROSSO | Brasil | 5102504 | 51 | 33 | nan | nan | nan | Pantanal | 0.7 |
| 204cbec8-3e4e-3f9b-979b-993810b00b8e | -16.48991 | -57.28035 | 2024-10-07 05:44:00 | NOAA-20 | CÁCERES | MATO GROSSO | Brasil | 5102504 | 51 | 33 | nan | nan | nan | Pantanal | 0.7 |
| 8afacc4e-7744-3e12-acce-af6ba362f969 | -16.48466 | -57.2758 | 2024-10-07 05:44:00 | NOAA-20 | CÁCERES | MATO GROSSO | Brasil | 5102504 | 51 | 33 | nan | nan | nan | Pantanal | 1.2 |
| a453c646-3ee1-3889-9009-363fe690df09 | -16.47778 | -57.28687 | 2024-10-07 05:44:00 | NOAA-20 | CÁCERES | MATO GROSSO | Brasil | 5102504 | 51 | 33 | nan | nan | nan | Pantanal | 1.5 |
| a4a4c2db-f68c-30a9-ae1b-4150892bbdc7 | -16.44264 | -57.26831 | 2024-10-07 05:44:00 | NOAA-20 | CÁCERES | MATO GROSSO | Brasil | 5102504 | 51 | 33 | nan | nan | nan | Pantanal | 1.9 |
| b69452e0-6056-3c8f-8fa2-38c2c77421b4 | -16.44223 | -57.27216 | 2024-10-07 05:44:00 | NOAA-20 | CÁCERES | MATO GROSSO | Brasil | 5102504 | 51 | 33 | nan | nan | nan | Pantanal | 2.2 |
| 57b79129-15b7-3609-88dd-c01f1eff8565 | -16.43698 | -57.26765 | 2024-10-07 05:44:00 | NOAA-20 | CÁCERES | MATO GROSSO | Brasil | 5102504 | 51 | 33 | nan | nan | nan | Pantanal | 1.4 |
| e9ef9ab2-c864-3edc-827d-2e332204e554 | -16.43657 | -57.27151 | 2024-10-07 05:44:00 | NOAA-20 | CÁCERES | MATO GROSSO | Brasil | 5102504 | 51 | 33 | nan | nan | nan | Pantanal | 1.0 |
| d9f6f4e6-509c-3d1a-bf89-d830e3e840ab | -16.43614 | -57.27544 | 2024-10-07 05:44:00 | NOAA-20 | CÁCERES | MATO GROSSO | Brasil | 5102504 | 51 | 33 | nan | nan | nan | Pantanal | 1.0 |
| 9b67931b-640d-3501-b5c2-1dd339e1234a | -16.43133 | -57.26696 | 2024-10-07 05:44:00 | NOAA-20 | CÁCERES | MATO GROSSO | Brasil | 5102504 | 51 | 33 | nan | nan | nan | Pantanal | 1.4 |
| b0486a9e-848e-3ac8-b13f-3fb38ef19d7e | -16.43091 | -57.27085 | 2024-10-07 05:44:00 | NOAA-20 | CÁCERES | MATO GROSSO | Brasil | 5102504 | 51 | 33 | nan | nan | nan | Pantanal | 1.0 |
| 91f58f12-df16-301a-8f13-24e07c347306 | -16.42566 | -57.26633 | 2024-10-07 05:44:00 | NOAA-20 | CÁCERES | MATO GROSSO | Brasil | 5102504 | 51 | 33 | nan | nan | nan | Pantanal | 0.7 |
| c6dc960d-0dcb-39c8-af6c-a723f379bebb | -16.41013 | -57.30463 | 2024-10-07 05:44:00 | NOAA-20 | CÁCERES | MATO GROSSO | Brasil | 5102504 | 51 | 33 | nan | nan | nan | Pantanal | 1.3 |
| 5e1fc6f6-551c-327f-bc9a-9a4fd4e39226 | -16.40971 | -57.30854 | 2024-10-07 05:44:00 | NOAA-20 | CÁCERES | MATO GROSSO | Brasil | 5102504 | 51 | 33 | nan | nan | nan | Pantanal | 1.5 |
| 7b50925e-7020-350a-a382-915ee10722dc | -16.63817 | -57.15268 | 2024-10-07 05:44:00 | NOAA-20 | POCONÉ | MATO GROSSO | Brasil | 5106505 | 51 | 33 | nan | nan | nan | Pantanal | 3.2 |
| 6f98a94c-f84a-3ba0-94d4-d7a5ea82269e | -16.63774 | -57.15675 | 2024-10-07 05:44:00 | NOAA-20 | POCONÉ | MATO GROSSO | Brasil | 5106505 | 51 | 33 | nan | nan | nan | Pantanal | 3.2 |
| 68ec6aa8-25f2-3686-ad28-46ca00ff40eb | -16.63731 | -57.16082 | 2024-10-07 05:44:00 | NOAA-20 | POCONÉ | MATO GROSSO | Brasil | 5106505 | 51 | 33 | nan | nan | nan | Pantanal | 2.8 |
| c5e158f9-cc27-3746-b1de-b7e65f443681 | -16.63458 | -57.13169 | 2024-10-07 05:44:00 | NOAA-20 | POCONÉ | MATO GROSSO | Brasil | 5106505 | 51 | 33 | nan | nan | nan | Pantanal | 1.4 |
| 254ba729-ffb4-3b55-bb54-1fd629b8a6ff | -16.63415 | -57.13577 | 2024-10-07 05:44:00 | NOAA-20 | POCONÉ | MATO GROSSO | Brasil | 5106505 | 51 | 33 | nan | nan | nan | Pantanal | 1.5 |
| bd53233b-8de1-326b-830b-315e362c07ed | -16.63373 | -57.13984 | 2024-10-07 05:44:00 | NOAA-20 | POCONÉ | MATO GROSSO | Brasil | 5106505 | 51 | 33 | nan | nan | nan | Pantanal | 1.5 |
| 7584180c-b3a6-3a09-ae2b-a7895fe1b092 | -16.6333 | -57.14391 | 2024-10-07 05:44:00 | NOAA-20 | POCONÉ | MATO GROSSO | Brasil | 5106505 | 51 | 33 | nan | nan | nan | Pantanal | 2.9 |
| af3b23cd-548e-3829-b63d-94a2a35a8ef4 | -16.63288 | -57.14797 | 2024-10-07 05:44:00 | NOAA-20 | POCONÉ | MATO GROSSO | Brasil | 5106505 | 51 | 33 | nan | nan | nan | Pantanal | 2.9 |
| 0394ac55-98cb-339d-b276-acf6d8bbb868 | -16.63245 | -57.15203 | 2024-10-07 05:44:00 | NOAA-20 | POCONÉ | MATO GROSSO | Brasil | 5106505 | 51 | 33 | nan | nan | nan | Pantanal | 3.2 |
| f6c91ef7-dbd1-33dc-8c04-485751432e18 | -16.63203 | -57.15608 | 2024-10-07 05:44:00 | NOAA-20 | POCONÉ | MATO GROSSO | Brasil | 5106505 | 51 | 33 | nan | nan | nan | Pantanal | 3.2 |
| 6095d8d9-47c9-3e70-b1d9-3cca4c58b41c | -16.6316 | -57.16014 | 2024-10-07 05:44:00 | NOAA-20 | POCONÉ | MATO GROSSO | Brasil | 5106505 | 51 | 33 | nan | nan | nan | Pantanal | 2.8 |


[Clique aqui para ver as próximas entradas](README139.md)
