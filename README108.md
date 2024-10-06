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

## Dados Diários - Página 108

| ID | Latitude | Longitude | Data/Hora GMT | Satélite | Município | Estado | País | Município ID | Estado ID | País ID | Dias sem Chuva | Precipitação | Risco de Fogo | Bioma | FRP |
|----|----------|-----------|---------------|----------|-----------|--------|------|--------------|-----------|---------|----------------|--------------|----------------|-------|-----|
| 8376c6e3-66c3-3ea0-835a-5d436dc853bf | -12.34724 | -57.37019 | 2024-10-06 05:12:00 | NOAA-21 | NOVA MARINGÁ | MATO GROSSO | Brasil | 5108907 | 51 | 33 | nan | nan | nan | Amazônia | 1.2 |
| 55146b6b-c7e1-3562-accb-73c7f803e917 | -12.34557 | -57.36665 | 2024-10-06 05:12:00 | NOAA-21 | NOVA MARINGÁ | MATO GROSSO | Brasil | 5108907 | 51 | 33 | nan | nan | nan | Amazônia | 1.9 |
| f337d218-f4f1-32f1-b262-6337e9bd0feb | -6.96623 | -59.07265 | 2024-10-06 05:12:00 | NOAA-21 | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 1.1 |
| ed1f7a47-5076-304c-90d1-48dc8c4910e1 | -6.96344 | -59.06849 | 2024-10-06 05:12:00 | NOAA-21 | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 0.4 |
| c0215246-0b11-32ae-9189-f860d9f8a19b | -6.96285 | -59.07211 | 2024-10-06 05:12:00 | NOAA-21 | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 1.1 |
| 874b5ed7-df33-3b8e-9bc8-2c3cc5ce97e6 | -6.96257 | -59.06421 | 2024-10-06 05:12:00 | NOAA-21 | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 0.9 |
| 46ace314-33a6-3c5a-9f2d-e5ab3bf9116e | -6.96199 | -59.06784 | 2024-10-06 05:12:00 | NOAA-21 | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 0.9 |
| a8eca5c0-486b-3438-ba26-668c192616ea | -6.96141 | -59.07148 | 2024-10-06 05:12:00 | NOAA-21 | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 2.1 |
| 8386971e-1850-3ec3-afc6-e1dc38cd1375 | -6.96034 | -59.05642 | 2024-10-06 05:12:00 | NOAA-21 | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 1.8 |
| 83a4f849-20c0-3567-a9ef-3b9fb8d5540a | -6.95977 | -59.06004 | 2024-10-06 05:12:00 | NOAA-21 | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 1.8 |
| 9d2302a4-cfca-3d75-a90a-04805599620d | -6.95919 | -59.06367 | 2024-10-06 05:12:00 | NOAA-21 | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 0.9 |
| 4ed11002-d0bc-3ca6-93cc-9730ab26b9c1 | -6.95861 | -59.06731 | 2024-10-06 05:12:00 | NOAA-21 | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 0.9 |
| f4185f23-5226-3e52-b583-1963ce017c6d | -6.95804 | -59.07094 | 2024-10-06 05:12:00 | NOAA-21 | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 2.1 |
| d46663a0-73f5-37f5-b280-66d8ed9692c9 | -6.95746 | -59.07457 | 2024-10-06 05:12:00 | NOAA-21 | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 2.1 |
| 57d59bea-e273-390c-a9a9-d8beeeb6be43 | -6.95697 | -59.05588 | 2024-10-06 05:12:00 | NOAA-21 | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 1.8 |
| dc14aec9-b2b2-3636-bc70-017a99193d16 | -6.95639 | -59.0595 | 2024-10-06 05:12:00 | NOAA-21 | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 1.8 |
| aae170f4-ac9c-35ba-aa8f-4e344104f572 | -6.95582 | -59.06313 | 2024-10-06 05:12:00 | NOAA-21 | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 0.8 |
| 28ffa446-a331-31d1-b0b9-f755c42aa338 | -6.95524 | -59.06676 | 2024-10-06 05:12:00 | NOAA-21 | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 0.8 |
| c1adb43c-424a-35b2-b763-793035ddbfda | -6.95466 | -59.07039 | 2024-10-06 05:12:00 | NOAA-21 | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 0.7 |
| 06135486-0085-3745-966c-4ffc171745f0 | -6.95408 | -59.07402 | 2024-10-06 05:12:00 | NOAA-21 | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 0.7 |
| 693c438c-123d-3afc-98d0-d839f2d70e7f | -6.95302 | -59.05896 | 2024-10-06 05:12:00 | NOAA-21 | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 1.8 |
| c2ac7369-cc98-326e-aafd-a97371ac7cb3 | -6.95244 | -59.06259 | 2024-10-06 05:12:00 | NOAA-21 | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 0.8 |
| e6a50cb0-5267-3580-b464-26d852841875 | -6.95186 | -59.06622 | 2024-10-06 05:12:00 | NOAA-21 | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 0.8 |
| 836dc932-ea6c-3ac3-b860-f1837ff5cf5c | -6.94964 | -59.05844 | 2024-10-06 05:12:00 | NOAA-21 | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 0.7 |
| 6242aeb5-d9bf-36fe-9f31-d86ff352f146 | -6.94907 | -59.06206 | 2024-10-06 05:12:00 | NOAA-21 | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 0.6 |
| 727ec5df-2f74-3bcb-b81f-1b10c7f4ed98 | -6.94849 | -59.06569 | 2024-10-06 05:12:00 | NOAA-21 | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 0.6 |
| 855b796d-787b-3342-a705-8ca1a030c682 | -6.94569 | -59.06153 | 2024-10-06 05:12:00 | NOAA-21 | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 0.6 |
| 5a6d5ab8-ad40-3319-ae5b-09f7e75eb4db | -6.94511 | -59.06516 | 2024-10-06 05:12:00 | NOAA-21 | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 0.6 |
| dcdf60ef-79c1-35f1-8adf-27180f32de37 | -6.91505 | -57.772 | 2024-10-06 05:12:00 | NOAA-21 | JACAREACANGA | PARÁ | Brasil | 1503754 | 15 | 33 | nan | nan | nan | Amazônia | 0.8 |
| 15dc927f-b8f5-3f40-8e9b-2e83188e6c16 | -6.91451 | -57.77546 | 2024-10-06 05:12:00 | NOAA-21 | JACAREACANGA | PARÁ | Brasil | 1503754 | 15 | 33 | nan | nan | nan | Amazônia | 0.8 |
| 91c86bcf-f992-31f6-85bd-1a2d710c6659 | -6.52929 | -58.40257 | 2024-10-06 05:12:00 | NOAA-21 | MAUÉS | AMAZONAS | Brasil | 1302900 | 13 | 33 | nan | nan | nan | Amazônia | 2.4 |
| 00355904-575f-3e05-a32a-60d9c9c1a3c1 | -6.52708 | -58.39502 | 2024-10-06 05:12:00 | NOAA-21 | MAUÉS | AMAZONAS | Brasil | 1302900 | 13 | 33 | nan | nan | nan | Amazônia | 1.8 |
| ff728ea6-d4b8-3f3d-9ead-0505e2d6ea8e | -6.52652 | -58.39853 | 2024-10-06 05:12:00 | NOAA-21 | MAUÉS | AMAZONAS | Brasil | 1302900 | 13 | 33 | nan | nan | nan | Amazônia | 1.8 |
| 67dbdc81-8f48-3486-b7ca-8cac4f32c0c6 | -6.52596 | -58.40204 | 2024-10-06 05:12:00 | NOAA-21 | MAUÉS | AMAZONAS | Brasil | 1302900 | 13 | 33 | nan | nan | nan | Amazônia | 2.4 |
| 9bb074e6-9208-34ad-a3db-6b6268e234ca | -6.5254 | -58.40555 | 2024-10-06 05:12:00 | NOAA-21 | MAUÉS | AMAZONAS | Brasil | 1302900 | 13 | 33 | nan | nan | nan | Amazônia | 2.4 |
| a4ce1b4b-dc48-321e-a38b-976a1dc659cf | -6.52339 | -58.39809 | 2024-10-06 05:12:00 | NOAA-21 | MAUÉS | AMAZONAS | Brasil | 1302900 | 13 | 33 | nan | nan | nan | Amazônia | 1.3 |
| 38733136-1f09-3d45-8245-5d5fcca3f986 | -6.51229 | -58.40353 | 2024-10-06 05:12:00 | NOAA-21 | MAUÉS | AMAZONAS | Brasil | 1302900 | 13 | 33 | nan | nan | nan | Amazônia | 1.3 |
| cabc498a-fd19-354e-b84f-0690231b86ed | -9.34767 | -58.9398 | 2024-10-06 05:12:00 | NOAA-21 | COTRIGUAÇU | MATO GROSSO | Brasil | 5103379 | 51 | 33 | nan | nan | nan | Amazônia | 3.5 |
| 6765ff32-883e-3c6b-98df-518766be5f98 | -9.34711 | -58.94333 | 2024-10-06 05:12:00 | NOAA-21 | COTRIGUAÇU | MATO GROSSO | Brasil | 5103379 | 51 | 33 | nan | nan | nan | Amazônia | 1.4 |
| cdca91c6-6388-3846-9b2e-8fb7bbdaa2c9 | -9.19426 | -58.19099 | 2024-10-06 05:12:00 | NOAA-21 | NOVA BANDEIRANTES | MATO GROSSO | Brasil | 5106158 | 51 | 33 | nan | nan | nan | Amazônia | 0.9 |
| 6c3e8d86-6dfc-3ea7-9871-e11d80b66232 | -9.1926 | -58.18006 | 2024-10-06 05:12:00 | NOAA-21 | NOVA BANDEIRANTES | MATO GROSSO | Brasil | 5106158 | 51 | 33 | nan | nan | nan | Amazônia | 1.3 |
| 0018e8c3-4ced-3dba-9321-3c1232339bb2 | -9.19096 | -58.19047 | 2024-10-06 05:12:00 | NOAA-21 | NOVA BANDEIRANTES | MATO GROSSO | Brasil | 5106158 | 51 | 33 | nan | nan | nan | Amazônia | 1.0 |
| 154c8c82-056a-38a7-b7ed-58f06d652a98 | -9.127 | -58.91475 | 2024-10-06 05:12:00 | NOAA-21 | COTRIGUAÇU | MATO GROSSO | Brasil | 5103379 | 51 | 33 | nan | nan | nan | Amazônia | 1.1 |
| 5a676967-d045-3044-9fb4-9795bccd7d67 | -9.12644 | -58.91829 | 2024-10-06 05:12:00 | NOAA-21 | COTRIGUAÇU | MATO GROSSO | Brasil | 5103379 | 51 | 33 | nan | nan | nan | Amazônia | 1.1 |
| 58d9af28-47dc-3cde-960e-38585f7afa97 | -9.11298 | -58.98132 | 2024-10-06 05:12:00 | NOAA-21 | COTRIGUAÇU | MATO GROSSO | Brasil | 5103379 | 51 | 33 | nan | nan | nan | Amazônia | 2.2 |
| 613e00e3-3792-3396-b826-7a8a6830c6d8 | -10.74667 | -59.32393 | 2024-10-06 05:12:00 | NOAA-21 | ARIPUANÃ | MATO GROSSO | Brasil | 5101407 | 51 | 33 | nan | nan | nan | Amazônia | 1.6 |
| d0968c97-14ac-3bb8-809f-e13022cd4d34 | -10.21988 | -59.40256 | 2024-10-06 05:12:00 | NOAA-21 | ARIPUANÃ | MATO GROSSO | Brasil | 5101407 | 51 | 33 | nan | nan | nan | Amazônia | 5.9 |
| 26e5a908-8be3-3ae5-bcb9-45a1a6e74acd | -10.2193 | -59.40615 | 2024-10-06 05:12:00 | NOAA-21 | ARIPUANÃ | MATO GROSSO | Brasil | 5101407 | 51 | 33 | nan | nan | nan | Amazônia | 2.5 |
| 9d65f443-8054-3532-948b-da674e0b869c | -10.21654 | -59.40201 | 2024-10-06 05:12:00 | NOAA-21 | ARIPUANÃ | MATO GROSSO | Brasil | 5101407 | 51 | 33 | nan | nan | nan | Amazônia | 8.3 |
| 1a87c66c-7734-3257-8b13-47bd6f8c3713 | -10.21596 | -59.4056 | 2024-10-06 05:12:00 | NOAA-21 | ARIPUANÃ | MATO GROSSO | Brasil | 5101407 | 51 | 33 | nan | nan | nan | Amazônia | 5.4 |
| d140320e-f525-3618-85e4-061225bab13c | -10.21262 | -59.40506 | 2024-10-06 05:12:00 | NOAA-21 | ARIPUANÃ | MATO GROSSO | Brasil | 5101407 | 51 | 33 | nan | nan | nan | Amazônia | 5.4 |
| 5acb8f0d-f682-3dcc-ac11-2a31e3c4764f | -10.11088 | -59.02059 | 2024-10-06 05:12:00 | NOAA-21 | ARIPUANÃ | MATO GROSSO | Brasil | 5101407 | 51 | 33 | nan | nan | nan | Amazônia | 0.8 |
| ebe8a4f0-3080-3ed9-a0cb-46f59501350b | -9.99538 | -59.55029 | 2024-10-06 05:12:00 | NOAA-21 | ARIPUANÃ | MATO GROSSO | Brasil | 5101407 | 51 | 33 | nan | nan | nan | Amazônia | 0.9 |
| e637aef9-7ee1-32eb-b9f1-9779c7873fa9 | -9.98423 | -59.44876 | 2024-10-06 05:12:00 | NOAA-21 | ARIPUANÃ | MATO GROSSO | Brasil | 5101407 | 51 | 33 | nan | nan | nan | Amazônia | 2.1 |
| 7f92420b-1c82-3399-ae3a-1732a7aeccef | -9.89506 | -59.49707 | 2024-10-06 05:12:00 | NOAA-21 | ARIPUANÃ | MATO GROSSO | Brasil | 5101407 | 51 | 33 | nan | nan | nan | Amazônia | 2.3 |
| 1111a298-55fb-3f5b-a915-9d25651e8030 | -9.89274 | -59.51149 | 2024-10-06 05:12:00 | NOAA-21 | ARIPUANÃ | MATO GROSSO | Brasil | 5101407 | 51 | 33 | nan | nan | nan | Amazônia | 2.0 |
| 7bb66410-d86f-371f-983d-6b961593fac3 | -9.8917 | -59.49653 | 2024-10-06 05:12:00 | NOAA-21 | ARIPUANÃ | MATO GROSSO | Brasil | 5101407 | 51 | 33 | nan | nan | nan | Amazônia | 2.3 |
| 7b489cb6-0636-33ce-a619-9c7c8bc1903e | -9.89112 | -59.50013 | 2024-10-06 05:12:00 | NOAA-21 | ARIPUANÃ | MATO GROSSO | Brasil | 5101407 | 51 | 33 | nan | nan | nan | Amazônia | 1.7 |
| cebcb2d9-5f89-3646-88d6-3c0f998de605 | -9.89054 | -59.50375 | 2024-10-06 05:12:00 | NOAA-21 | ARIPUANÃ | MATO GROSSO | Brasil | 5101407 | 51 | 33 | nan | nan | nan | Amazônia | 1.7 |
| b0cfc468-8049-3450-9782-785d2714ad83 | -9.88835 | -59.49598 | 2024-10-06 05:12:00 | NOAA-21 | ARIPUANÃ | MATO GROSSO | Brasil | 5101407 | 51 | 33 | nan | nan | nan | Amazônia | 1.9 |
| fc426a16-86cf-3d6e-88ae-df650d16c5a4 | -9.88777 | -59.49959 | 2024-10-06 05:12:00 | NOAA-21 | ARIPUANÃ | MATO GROSSO | Brasil | 5101407 | 51 | 33 | nan | nan | nan | Amazônia | 1.0 |
| da4dc131-f0bd-3226-8892-bbf20b3d7058 | -9.88719 | -59.5032 | 2024-10-06 05:12:00 | NOAA-21 | ARIPUANÃ | MATO GROSSO | Brasil | 5101407 | 51 | 33 | nan | nan | nan | Amazônia | 1.0 |
| 9f7beefc-49b6-38c1-9f62-be79d3ce0c7f | -9.88441 | -59.49905 | 2024-10-06 05:12:00 | NOAA-21 | ARIPUANÃ | MATO GROSSO | Brasil | 5101407 | 51 | 33 | nan | nan | nan | Amazônia | 1.0 |
| 301c8460-b66d-35ef-93e1-4eed96293816 | -9.88383 | -59.50266 | 2024-10-06 05:12:00 | NOAA-21 | ARIPUANÃ | MATO GROSSO | Brasil | 5101407 | 51 | 33 | nan | nan | nan | Amazônia | 1.0 |
| 23d4cdab-0d64-3eb1-a58e-37949cfa01b5 | -9.88222 | -59.4913 | 2024-10-06 05:12:00 | NOAA-21 | ARIPUANÃ | MATO GROSSO | Brasil | 5101407 | 51 | 33 | nan | nan | nan | Amazônia | 1.1 |
| ec5f1f13-dbad-3eb8-9171-7d0514cc64b4 | -9.88164 | -59.4949 | 2024-10-06 05:12:00 | NOAA-21 | ARIPUANÃ | MATO GROSSO | Brasil | 5101407 | 51 | 33 | nan | nan | nan | Amazônia | 1.1 |
| e59fbdd1-f2a0-3f44-a12e-5c65c7fa5049 | -9.88106 | -59.49851 | 2024-10-06 05:12:00 | NOAA-21 | ARIPUANÃ | MATO GROSSO | Brasil | 5101407 | 51 | 33 | nan | nan | nan | Amazônia | 2.7 |
| 5d01527b-9ae4-3a3d-baa9-39add5828b57 | -9.87887 | -59.49076 | 2024-10-06 05:12:00 | NOAA-21 | ARIPUANÃ | MATO GROSSO | Brasil | 5101407 | 51 | 33 | nan | nan | nan | Amazônia | 1.1 |
| 0b042764-5bbc-3890-9aba-2f497d7ef7fd | -9.87828 | -59.49437 | 2024-10-06 05:12:00 | NOAA-21 | ARIPUANÃ | MATO GROSSO | Brasil | 5101407 | 51 | 33 | nan | nan | nan | Amazônia | 1.1 |
| 1da7222a-97f3-39a5-a499-e30fedd7ac52 | -9.8777 | -59.49797 | 2024-10-06 05:12:00 | NOAA-21 | ARIPUANÃ | MATO GROSSO | Brasil | 5101407 | 51 | 33 | nan | nan | nan | Amazônia | 2.7 |
| 42c3c39d-454d-3a56-8f13-8b2853274c7e | -9.82671 | -58.96681 | 2024-10-06 05:12:00 | NOAA-21 | COTRIGUAÇU | MATO GROSSO | Brasil | 5103379 | 51 | 33 | nan | nan | nan | Amazônia | 0.7 |
| 9a35503b-daf1-37fc-ab04-5d48fcad818c | -9.82226 | -58.97332 | 2024-10-06 05:12:00 | NOAA-21 | COTRIGUAÇU | MATO GROSSO | Brasil | 5103379 | 51 | 33 | nan | nan | nan | Amazônia | 1.5 |
| 1a9c46e6-4e53-3cea-8304-561b62eb6ff3 | -9.8195 | -58.96926 | 2024-10-06 05:12:00 | NOAA-21 | COTRIGUAÇU | MATO GROSSO | Brasil | 5103379 | 51 | 33 | nan | nan | nan | Amazônia | 1.5 |
| 1048e9d2-b65f-3ad7-9778-51d30f62cc25 | -9.81894 | -58.97279 | 2024-10-06 05:12:00 | NOAA-21 | COTRIGUAÇU | MATO GROSSO | Brasil | 5103379 | 51 | 33 | nan | nan | nan | Amazônia | 1.5 |
| 3fd78877-699e-325a-b2b7-f047adbd4a23 | -9.81562 | -58.97225 | 2024-10-06 05:12:00 | NOAA-21 | COTRIGUAÇU | MATO GROSSO | Brasil | 5103379 | 51 | 33 | nan | nan | nan | Amazônia | 0.9 |
| 5239f31d-312a-3cc4-8bb2-9f90ece25368 | -9.80793 | -58.97823 | 2024-10-06 05:12:00 | NOAA-21 | COTRIGUAÇU | MATO GROSSO | Brasil | 5103379 | 51 | 33 | nan | nan | nan | Amazônia | 1.3 |
| 1f80b003-b8d5-3b99-8514-ec5ccbbc8378 | -9.80737 | -58.98176 | 2024-10-06 05:12:00 | NOAA-21 | COTRIGUAÇU | MATO GROSSO | Brasil | 5103379 | 51 | 33 | nan | nan | nan | Amazônia | 1.1 |
| d1d39a09-d43f-3fbe-aeef-84ef0a568cc4 | -9.80461 | -58.97771 | 2024-10-06 05:12:00 | NOAA-21 | COTRIGUAÇU | MATO GROSSO | Brasil | 5103379 | 51 | 33 | nan | nan | nan | Amazônia | 1.3 |
| 91ff023d-e573-3f6e-a96a-5d9f1a049df3 | -9.80405 | -58.98122 | 2024-10-06 05:12:00 | NOAA-21 | COTRIGUAÇU | MATO GROSSO | Brasil | 5103379 | 51 | 33 | nan | nan | nan | Amazônia | 1.1 |
| 396b7b1a-f2c9-390e-8121-9d7cc6c11196 | -9.80017 | -58.98421 | 2024-10-06 05:12:00 | NOAA-21 | COTRIGUAÇU | MATO GROSSO | Brasil | 5103379 | 51 | 33 | nan | nan | nan | Amazônia | 1.7 |
| 1744b48b-9726-3ef5-bebd-01c3d001a6ff | -9.79135 | -59.44284 | 2024-10-06 05:12:00 | NOAA-21 | ARIPUANÃ | MATO GROSSO | Brasil | 5101407 | 51 | 33 | nan | nan | nan | Amazônia | 1.1 |
| 016c7f03-8035-37c5-8cd6-b68c7b078527 | -9.77149 | -59.39541 | 2024-10-06 05:12:00 | NOAA-21 | COLNIZA | MATO GROSSO | Brasil | 5103254 | 51 | 33 | nan | nan | nan | Amazônia | 1.0 |
| fa9371d2-a171-30c3-931b-77a39322b5f1 | -9.76872 | -59.39127 | 2024-10-06 05:12:00 | NOAA-21 | COLNIZA | MATO GROSSO | Brasil | 5103254 | 51 | 33 | nan | nan | nan | Amazônia | 1.1 |
| e3e4a724-125a-323c-b3f6-9d738fbd8b76 | -9.76596 | -59.38713 | 2024-10-06 05:12:00 | NOAA-21 | COLNIZA | MATO GROSSO | Brasil | 5103254 | 51 | 33 | nan | nan | nan | Amazônia | 0.4 |
| 6ffd8348-bdad-3edf-82b6-bba9259ee5d5 | -9.76538 | -59.39073 | 2024-10-06 05:12:00 | NOAA-21 | COLNIZA | MATO GROSSO | Brasil | 5103254 | 51 | 33 | nan | nan | nan | Amazônia | 1.1 |
| a58d23f6-0eba-3e07-8b5b-70ea3219acbd | -9.63649 | -59.09204 | 2024-10-06 05:12:00 | NOAA-21 | COLNIZA | MATO GROSSO | Brasil | 5103254 | 51 | 33 | nan | nan | nan | Amazônia | 0.7 |
| 24988ec5-d6fa-3e70-9db3-650158583908 | -11.86954 | -59.02666 | 2024-10-06 05:12:00 | NOAA-21 | JUÍNA | MATO GROSSO | Brasil | 5105150 | 51 | 33 | nan | nan | nan | Cerrado | 1.3 |
| ffb2bf9b-43cf-33db-838a-ff74ec745309 | -11.86679 | -59.02259 | 2024-10-06 05:12:00 | NOAA-21 | JUÍNA | MATO GROSSO | Brasil | 5105150 | 51 | 33 | nan | nan | nan | Cerrado | 1.3 |
| c0c143de-f7c5-38dd-90d5-621631f493bc | -11.86295 | -59.00398 | 2024-10-06 05:12:00 | NOAA-21 | JUÍNA | MATO GROSSO | Brasil | 5105150 | 51 | 33 | nan | nan | nan | Cerrado | 0.8 |
| d0a59b2f-695b-344a-94af-7a23d782d657 | -11.86235 | -59.05067 | 2024-10-06 05:12:00 | NOAA-21 | JUÍNA | MATO GROSSO | Brasil | 5105150 | 51 | 33 | nan | nan | nan | Cerrado | 1.5 |
| 09c05eef-9c4a-3bda-b42d-3ce1c69a1079 | -11.85909 | -59.00695 | 2024-10-06 05:12:00 | NOAA-21 | JUÍNA | MATO GROSSO | Brasil | 5105150 | 51 | 33 | nan | nan | nan | Cerrado | 1.2 |
| 63c01416-5fc3-3106-9c6b-02da696d0b1f | -11.85854 | -59.01046 | 2024-10-06 05:12:00 | NOAA-21 | JUÍNA | MATO GROSSO | Brasil | 5105150 | 51 | 33 | nan | nan | nan | Cerrado | 1.2 |
| b280e3e5-11e3-3f45-a2ff-7dba6be3d3e0 | -11.85524 | -59.00992 | 2024-10-06 05:12:00 | NOAA-21 | JUÍNA | MATO GROSSO | Brasil | 5105150 | 51 | 33 | nan | nan | nan | Cerrado | 1.2 |
| 8895fc3c-bd2d-373a-9b71-43aec5c386c1 | -11.85468 | -59.01342 | 2024-10-06 05:12:00 | NOAA-21 | JUÍNA | MATO GROSSO | Brasil | 5105150 | 51 | 33 | nan | nan | nan | Cerrado | 2.3 |
| aca8de2e-a4af-3e13-b71d-5d367ec48d1d | -11.84547 | -58.87882 | 2024-10-06 05:12:00 | NOAA-21 | JUÍNA | MATO GROSSO | Brasil | 5105150 | 51 | 33 | nan | nan | nan | Cerrado | 0.5 |
| 65dcbde6-eba0-364b-84d8-4ee41c6abafc | -11.84544 | -58.9004 | 2024-10-06 05:12:00 | NOAA-21 | JUÍNA | MATO GROSSO | Brasil | 5105150 | 51 | 33 | nan | nan | nan | Cerrado | 1.4 |
| a3c61af3-1ac5-3933-9b0f-587ef63595c7 | -11.8427 | -58.89635 | 2024-10-06 05:12:00 | NOAA-21 | JUÍNA | MATO GROSSO | Brasil | 5105150 | 51 | 33 | nan | nan | nan | Cerrado | 0.8 |
| 129440d8-f824-3992-a307-d0e6bf078f01 | -11.84217 | -58.87828 | 2024-10-06 05:12:00 | NOAA-21 | JUÍNA | MATO GROSSO | Brasil | 5105150 | 51 | 33 | nan | nan | nan | Cerrado | 0.5 |
| 2afee496-178c-3a67-8778-c26e119a6425 | -11.84214 | -58.89986 | 2024-10-06 05:12:00 | NOAA-21 | JUÍNA | MATO GROSSO | Brasil | 5105150 | 51 | 33 | nan | nan | nan | Cerrado | 0.8 |
| d452d241-ff88-320a-8287-cfd84225cd46 | -11.7091 | -58.83876 | 2024-10-06 05:12:00 | NOAA-21 | JUÍNA | MATO GROSSO | Brasil | 5105150 | 51 | 33 | nan | nan | nan | Cerrado | 1.1 |


[Clique aqui para ver as próximas entradas](README109.md)
