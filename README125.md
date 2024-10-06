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
| c7c1825c-adc6-3113-beb4-1410afed68de | -16.67602 | -57.47437 | 2024-10-06 05:14:00 | NOAA-21 | CÁCERES | MATO GROSSO | Brasil | 5102504 | 51 | 33 | nan | nan | nan | Pantanal | 3.3 |
| c8cc4134-f79a-35d3-9a61-46ec9e93d8ef | -16.67585 | -57.46899 | 2024-10-06 05:14:00 | NOAA-21 | CÁCERES | MATO GROSSO | Brasil | 5102504 | 51 | 33 | nan | nan | nan | Pantanal | 5.2 |
| a58b132f-43fd-321a-995a-0a09d92504ff | -17.14562 | -56.75308 | 2024-10-06 05:14:00 | NOAA-21 | POCONÉ | MATO GROSSO | Brasil | 5106505 | 51 | 33 | nan | nan | nan | Pantanal | 20.7 |
| 78e4b760-a19a-3ae5-813d-c8381de2de51 | -17.14502 | -56.75734 | 2024-10-06 05:14:00 | NOAA-21 | POCONÉ | MATO GROSSO | Brasil | 5106505 | 51 | 33 | nan | nan | nan | Pantanal | 20.7 |
| d93466e7-96c6-31d2-ae91-97b277be93de | -17.14204 | -56.75253 | 2024-10-06 05:14:00 | NOAA-21 | POCONÉ | MATO GROSSO | Brasil | 5106505 | 51 | 33 | nan | nan | nan | Pantanal | 1.9 |
| d4f4e9f8-2c2b-3f72-a715-e42631cfa24e | -17.12237 | -56.76252 | 2024-10-06 05:14:00 | NOAA-21 | POCONÉ | MATO GROSSO | Brasil | 5106505 | 51 | 33 | nan | nan | nan | Pantanal | 2.0 |
| b760bdb2-1f3a-3b6c-8bd3-2bd9734bef60 | -17.12175 | -56.7407 | 2024-10-06 05:14:00 | NOAA-21 | POCONÉ | MATO GROSSO | Brasil | 5106505 | 51 | 33 | nan | nan | nan | Pantanal | 3.6 |
| 36ded99c-9bce-30f3-9dce-2df62626845b | -17.11997 | -56.75347 | 2024-10-06 05:14:00 | NOAA-21 | POCONÉ | MATO GROSSO | Brasil | 5106505 | 51 | 33 | nan | nan | nan | Pantanal | 2.6 |
| e4277ab5-bfd5-37eb-bfb6-a317684c75d2 | -17.1158 | -56.75717 | 2024-10-06 05:14:00 | NOAA-21 | POCONÉ | MATO GROSSO | Brasil | 5106505 | 51 | 33 | nan | nan | nan | Pantanal | 2.9 |
| 3ee19ca7-7229-30ce-9d25-3352828b124e | -17.11521 | -56.76142 | 2024-10-06 05:14:00 | NOAA-21 | POCONÉ | MATO GROSSO | Brasil | 5106505 | 51 | 33 | nan | nan | nan | Pantanal | 2.9 |
| a4c9e928-3463-3751-a3cc-c9af78ccbd83 | -17.11164 | -56.76087 | 2024-10-06 05:14:00 | NOAA-21 | POCONÉ | MATO GROSSO | Brasil | 5106505 | 51 | 33 | nan | nan | nan | Pantanal | 2.5 |
| 71b6ee5b-eb5e-317f-898e-24deb56ee9fc | -17.09621 | -56.79314 | 2024-10-06 05:14:00 | NOAA-21 | POCONÉ | MATO GROSSO | Brasil | 5106505 | 51 | 33 | nan | nan | nan | Pantanal | 2.1 |
| 8e6bbed4-60e6-386b-9349-9fb555b35df9 | -17.03765 | -56.7252 | 2024-10-06 05:14:00 | NOAA-21 | POCONÉ | MATO GROSSO | Brasil | 5106505 | 51 | 33 | nan | nan | nan | Pantanal | 2.5 |
| 247e65bd-6ce1-331f-91a6-c206b32d6105 | -17.03705 | -56.72946 | 2024-10-06 05:14:00 | NOAA-21 | POCONÉ | MATO GROSSO | Brasil | 5106505 | 51 | 33 | nan | nan | nan | Pantanal | 3.2 |
| d79a15a6-0ae1-3922-997f-52a4d156c7ce | -17.03467 | -56.7204 | 2024-10-06 05:14:00 | NOAA-21 | POCONÉ | MATO GROSSO | Brasil | 5106505 | 51 | 33 | nan | nan | nan | Pantanal | 2.5 |
| 3c4380ac-53df-3ff9-91f1-2a51447e216d | -17.03347 | -56.72891 | 2024-10-06 05:14:00 | NOAA-21 | POCONÉ | MATO GROSSO | Brasil | 5106505 | 51 | 33 | nan | nan | nan | Pantanal | 3.2 |
| 7b00033d-1ddc-3789-82c0-f904ffd5254e | -17.03109 | -56.71984 | 2024-10-06 05:14:00 | NOAA-21 | POCONÉ | MATO GROSSO | Brasil | 5106505 | 51 | 33 | nan | nan | nan | Pantanal | 2.0 |
| f62afb54-a8cb-3a9a-bd58-e73de38d8aa3 | -17.03049 | -56.7241 | 2024-10-06 05:14:00 | NOAA-21 | POCONÉ | MATO GROSSO | Brasil | 5106505 | 51 | 33 | nan | nan | nan | Pantanal | 2.0 |
| ef6e294f-8407-31b2-92ab-c95945ba4051 | -17.02929 | -56.70652 | 2024-10-06 05:14:00 | NOAA-21 | POCONÉ | MATO GROSSO | Brasil | 5106505 | 51 | 33 | nan | nan | nan | Pantanal | 2.9 |
| ace963bf-250e-3a3e-8a03-87f64a126505 | -17.0275 | -56.71929 | 2024-10-06 05:14:00 | NOAA-21 | POCONÉ | MATO GROSSO | Brasil | 5106505 | 51 | 33 | nan | nan | nan | Pantanal | 2.0 |
| 13033181-dab8-30fd-8f84-982efb9c52de | -17.02631 | -56.7278 | 2024-10-06 05:14:00 | NOAA-21 | POCONÉ | MATO GROSSO | Brasil | 5106505 | 51 | 33 | nan | nan | nan | Pantanal | 2.6 |
| 611cfec0-a4c0-34dd-87e7-5d3de1689d24 | -17.0263 | -56.7017 | 2024-10-06 05:14:00 | NOAA-21 | POCONÉ | MATO GROSSO | Brasil | 5106505 | 51 | 33 | nan | nan | nan | Pantanal | 2.4 |
| 1e89239e-90cf-337c-908d-0b4b1bb0254e | -17.02572 | -56.73205 | 2024-10-06 05:14:00 | NOAA-21 | POCONÉ | MATO GROSSO | Brasil | 5106505 | 51 | 33 | nan | nan | nan | Pantanal | 2.6 |
| a379019b-7508-3c3c-b370-40c9ba6c058a | -17.02571 | -56.70596 | 2024-10-06 05:14:00 | NOAA-21 | POCONÉ | MATO GROSSO | Brasil | 5106505 | 51 | 33 | nan | nan | nan | Pantanal | 2.4 |
| ac05b8c5-c0cb-32fd-a0e3-70d59b4c4208 | -17.02513 | -56.73629 | 2024-10-06 05:14:00 | NOAA-21 | POCONÉ | MATO GROSSO | Brasil | 5106505 | 51 | 33 | nan | nan | nan | Pantanal | 3.0 |
| f03e53aa-3378-3ab6-a56d-e660f79a907c | -17.02511 | -56.71022 | 2024-10-06 05:14:00 | NOAA-21 | POCONÉ | MATO GROSSO | Brasil | 5106505 | 51 | 33 | nan | nan | nan | Pantanal | 4.8 |
| c3667555-79d7-3381-8693-1b539ff2cc94 | -17.02452 | -56.71448 | 2024-10-06 05:14:00 | NOAA-21 | POCONÉ | MATO GROSSO | Brasil | 5106505 | 51 | 33 | nan | nan | nan | Pantanal | 4.8 |
| 9217b643-9ce2-33e3-a91e-ef1d5a899b4b | -17.02274 | -56.72725 | 2024-10-06 05:14:00 | NOAA-21 | POCONÉ | MATO GROSSO | Brasil | 5106505 | 51 | 33 | nan | nan | nan | Pantanal | 4.2 |
| 48d1b35d-5282-33d0-982f-ea98a2309c71 | -17.02272 | -56.70115 | 2024-10-06 05:14:00 | NOAA-21 | POCONÉ | MATO GROSSO | Brasil | 5106505 | 51 | 33 | nan | nan | nan | Pantanal | 2.4 |
| ec075966-49bf-3c06-8395-d8003bf174f6 | -17.02213 | -56.70541 | 2024-10-06 05:14:00 | NOAA-21 | POCONÉ | MATO GROSSO | Brasil | 5106505 | 51 | 33 | nan | nan | nan | Pantanal | 2.4 |
| d43a1c06-73e9-336f-a28a-3753490ff911 | -17.02094 | -56.71392 | 2024-10-06 05:14:00 | NOAA-21 | POCONÉ | MATO GROSSO | Brasil | 5106505 | 51 | 33 | nan | nan | nan | Pantanal | 4.8 |
| 07499dba-d082-32c0-a735-cd5de01547a6 | -17.01916 | -56.72669 | 2024-10-06 05:14:00 | NOAA-21 | POCONÉ | MATO GROSSO | Brasil | 5106505 | 51 | 33 | nan | nan | nan | Pantanal | 4.2 |
| ca32fb68-4a4f-315f-a42d-c7971c541323 | -17.01914 | -56.70059 | 2024-10-06 05:14:00 | NOAA-21 | POCONÉ | MATO GROSSO | Brasil | 5106505 | 51 | 33 | nan | nan | nan | Pantanal | 4.2 |
| 3c8a433f-6308-3db9-9522-9cfa881438f5 | -17.01856 | -56.73094 | 2024-10-06 05:14:00 | NOAA-21 | POCONÉ | MATO GROSSO | Brasil | 5106505 | 51 | 33 | nan | nan | nan | Pantanal | 4.2 |
| 43b940d8-db00-3f58-82b9-368c3b057286 | -17.01854 | -56.70485 | 2024-10-06 05:14:00 | NOAA-21 | POCONÉ | MATO GROSSO | Brasil | 5106505 | 51 | 33 | nan | nan | nan | Pantanal | 4.2 |
| baa94b99-22bb-3aee-8b0c-df226a0c54a2 | -17.01558 | -56.72614 | 2024-10-06 05:14:00 | NOAA-21 | POCONÉ | MATO GROSSO | Brasil | 5106505 | 51 | 33 | nan | nan | nan | Pantanal | 3.0 |
| a009a9cd-b6d1-3ece-aa09-103a3c34abee | -17.01555 | -56.70004 | 2024-10-06 05:14:00 | NOAA-21 | POCONÉ | MATO GROSSO | Brasil | 5106505 | 51 | 33 | nan | nan | nan | Pantanal | 4.2 |
| ec2056ba-411c-3fa8-a8d2-7529e1b2d7aa | -17.01499 | -56.73038 | 2024-10-06 05:14:00 | NOAA-21 | POCONÉ | MATO GROSSO | Brasil | 5106505 | 51 | 33 | nan | nan | nan | Pantanal | 3.0 |
| 2861afe1-ff40-3a5a-9e2e-1c085d49ba8f | -17.01496 | -56.7043 | 2024-10-06 05:14:00 | NOAA-21 | POCONÉ | MATO GROSSO | Brasil | 5106505 | 51 | 33 | nan | nan | nan | Pantanal | 4.2 |
| f333e045-1dff-3db4-b139-0560a44d1516 | -17.01437 | -56.70855 | 2024-10-06 05:14:00 | NOAA-21 | POCONÉ | MATO GROSSO | Brasil | 5106505 | 51 | 33 | nan | nan | nan | Pantanal | 16.5 |
| 24958505-7456-3b44-a843-96f0270bdc2e | -17.01319 | -56.71707 | 2024-10-06 05:14:00 | NOAA-21 | POCONÉ | MATO GROSSO | Brasil | 5106505 | 51 | 33 | nan | nan | nan | Pantanal | 9.3 |
| 6f8aab14-adb1-3119-9b8c-e2c28b43c278 | -17.01259 | -56.72132 | 2024-10-06 05:14:00 | NOAA-21 | POCONÉ | MATO GROSSO | Brasil | 5106505 | 51 | 33 | nan | nan | nan | Pantanal | 9.3 |
| 240935c2-1539-33b0-a7cd-d35406005e63 | -17.01138 | -56.70374 | 2024-10-06 05:14:00 | NOAA-21 | POCONÉ | MATO GROSSO | Brasil | 5106505 | 51 | 33 | nan | nan | nan | Pantanal | 3.6 |
| f514ce74-da68-340f-b750-258b8153e378 | -17.01079 | -56.708 | 2024-10-06 05:14:00 | NOAA-21 | POCONÉ | MATO GROSSO | Brasil | 5106505 | 51 | 33 | nan | nan | nan | Pantanal | 3.9 |
| 6b57ba07-0c5c-3f3c-a458-f2d66aa513ab | -17.0102 | -56.71226 | 2024-10-06 05:14:00 | NOAA-21 | POCONÉ | MATO GROSSO | Brasil | 5106505 | 51 | 33 | nan | nan | nan | Pantanal | 3.9 |
| 0b6b3ac3-9a64-3a6f-9095-9e1594a590b9 | -17.0078 | -56.70319 | 2024-10-06 05:14:00 | NOAA-21 | POCONÉ | MATO GROSSO | Brasil | 5106505 | 51 | 33 | nan | nan | nan | Pantanal | 3.6 |
| ce02ba5e-8a58-36f0-9069-6fbdc343a723 | -17.00724 | -56.73353 | 2024-10-06 05:14:00 | NOAA-21 | POCONÉ | MATO GROSSO | Brasil | 5106505 | 51 | 33 | nan | nan | nan | Pantanal | 4.9 |
| 71493f5f-257f-3d60-9e20-3dc892bcf7e8 | -17.00721 | -56.70745 | 2024-10-06 05:14:00 | NOAA-21 | POCONÉ | MATO GROSSO | Brasil | 5106505 | 51 | 33 | nan | nan | nan | Pantanal | 3.9 |
| 343287f0-46d0-3d92-8782-fde58a4dd659 | -17.00662 | -56.7117 | 2024-10-06 05:14:00 | NOAA-21 | POCONÉ | MATO GROSSO | Brasil | 5106505 | 51 | 33 | nan | nan | nan | Pantanal | 3.9 |
| b5814d33-b442-3a71-8685-d87a8ded50fa | -17.00525 | -56.7048 | 2024-10-06 05:14:00 | NOAA-21 | POCONÉ | MATO GROSSO | Brasil | 5106505 | 51 | 33 | nan | nan | nan | Pantanal | 3.3 |
| ffbd8476-5bb8-32fd-9bfe-0fc5a994acdc | -17.00484 | -56.72448 | 2024-10-06 05:14:00 | NOAA-21 | POCONÉ | MATO GROSSO | Brasil | 5106505 | 51 | 33 | nan | nan | nan | Pantanal | 6.0 |
| e37c0766-0b2c-3721-a42b-56473bbb2409 | -17.00463 | -56.70906 | 2024-10-06 05:14:00 | NOAA-21 | POCONÉ | MATO GROSSO | Brasil | 5106505 | 51 | 33 | nan | nan | nan | Pantanal | 3.2 |
| e0bd0029-0dd0-3860-8ca7-43a360c74d3f | -17.00426 | -56.72873 | 2024-10-06 05:14:00 | NOAA-21 | POCONÉ | MATO GROSSO | Brasil | 5106505 | 51 | 33 | nan | nan | nan | Pantanal | 6.0 |
| 66da55c3-a2ee-3809-80d1-14a7f126b4cb | -17.00307 | -56.73722 | 2024-10-06 05:14:00 | NOAA-21 | POCONÉ | MATO GROSSO | Brasil | 5106505 | 51 | 33 | nan | nan | nan | Pantanal | 4.9 |
| 4183ad8f-6ea1-3110-9765-758c265cbe31 | -17.00158 | -56.7303 | 2024-10-06 05:14:00 | NOAA-21 | POCONÉ | MATO GROSSO | Brasil | 5106505 | 51 | 33 | nan | nan | nan | Pantanal | 12.6 |
| e37c2a74-8b36-3ca6-8e4e-5119469fdc62 | -16.9995 | -56.73666 | 2024-10-06 05:14:00 | NOAA-21 | POCONÉ | MATO GROSSO | Brasil | 5106505 | 51 | 33 | nan | nan | nan | Pantanal | 12.8 |
| aee7f457-bffa-3b8f-8f10-69810fb40c17 | -16.9993 | -56.69519 | 2024-10-06 05:14:00 | NOAA-21 | POCONÉ | MATO GROSSO | Brasil | 5106505 | 51 | 33 | nan | nan | nan | Pantanal | 2.3 |
| 9c16e964-b41d-38f7-80f9-d8caa3a4546e | -16.99808 | -56.7037 | 2024-10-06 05:14:00 | NOAA-21 | POCONÉ | MATO GROSSO | Brasil | 5106505 | 51 | 33 | nan | nan | nan | Pantanal | 3.2 |
| ea6e4794-9a98-35f6-8e1a-308f44c094c3 | -16.99592 | -56.73611 | 2024-10-06 05:14:00 | NOAA-21 | POCONÉ | MATO GROSSO | Brasil | 5106505 | 51 | 33 | nan | nan | nan | Pantanal | 12.8 |
| 94135248-a120-3ebc-92de-61a217ff00b5 | -16.99511 | -56.69889 | 2024-10-06 05:14:00 | NOAA-21 | POCONÉ | MATO GROSSO | Brasil | 5106505 | 51 | 33 | nan | nan | nan | Pantanal | 3.2 |
| 6fac53e7-a9a1-3625-a8ec-f949731e2f77 | -16.99389 | -56.7074 | 2024-10-06 05:14:00 | NOAA-21 | POCONÉ | MATO GROSSO | Brasil | 5106505 | 51 | 33 | nan | nan | nan | Pantanal | 23.8 |
| 72fd924d-8ff2-3518-a205-257e22e2b885 | -16.98841 | -56.74559 | 2024-10-06 05:14:00 | NOAA-21 | POCONÉ | MATO GROSSO | Brasil | 5106505 | 51 | 33 | nan | nan | nan | Pantanal | 3.2 |
| 0bf23974-f019-309d-98be-f3456ea4ad0a | -16.9878 | -56.74983 | 2024-10-06 05:14:00 | NOAA-21 | POCONÉ | MATO GROSSO | Brasil | 5106505 | 51 | 33 | nan | nan | nan | Pantanal | 1.8 |
| 6c677c66-3d4b-3f73-a133-0ac5ccfa77c5 | -16.98719 | -56.75407 | 2024-10-06 05:14:00 | NOAA-21 | POCONÉ | MATO GROSSO | Brasil | 5106505 | 51 | 33 | nan | nan | nan | Pantanal | 1.8 |
| 8bc7db44-652a-3b4d-8938-fe21c5537d3b | -16.9859 | -56.78842 | 2024-10-06 05:14:00 | NOAA-21 | POCONÉ | MATO GROSSO | Brasil | 5106505 | 51 | 33 | nan | nan | nan | Pantanal | 3.5 |
| 42cad16c-158f-3eff-976e-80619bdc10af | -16.98545 | -56.7408 | 2024-10-06 05:14:00 | NOAA-21 | POCONÉ | MATO GROSSO | Brasil | 5106505 | 51 | 33 | nan | nan | nan | Pantanal | 4.9 |
| 70306d18-3662-3a04-8e56-dd898703b289 | -16.98362 | -56.75351 | 2024-10-06 05:14:00 | NOAA-21 | POCONÉ | MATO GROSSO | Brasil | 5106505 | 51 | 33 | nan | nan | nan | Pantanal | 3.8 |
| 56fafb17-c02a-3865-a48f-a206851087f1 | -16.98302 | -56.75775 | 2024-10-06 05:14:00 | NOAA-21 | POCONÉ | MATO GROSSO | Brasil | 5106505 | 51 | 33 | nan | nan | nan | Pantanal | 4.5 |
| cf2f0f9f-cb12-327c-9e80-d55d3ed994b0 | -16.98241 | -56.76198 | 2024-10-06 05:14:00 | NOAA-21 | POCONÉ | MATO GROSSO | Brasil | 5106505 | 51 | 33 | nan | nan | nan | Pantanal | 4.5 |
| 865c6a6c-3bf3-354b-90d3-66eb8d89d9e7 | -16.97945 | -56.75719 | 2024-10-06 05:14:00 | NOAA-21 | POCONÉ | MATO GROSSO | Brasil | 5106505 | 51 | 33 | nan | nan | nan | Pantanal | 4.5 |
| 3918f8f8-d1b1-399f-8532-4c3c5ac66bc9 | -16.97823 | -56.76565 | 2024-10-06 05:14:00 | NOAA-21 | POCONÉ | MATO GROSSO | Brasil | 5106505 | 51 | 33 | nan | nan | nan | Pantanal | 3.6 |
| fadf1efb-ec57-32c3-b8f8-c20c73d37f13 | -16.97527 | -56.76087 | 2024-10-06 05:14:00 | NOAA-21 | POCONÉ | MATO GROSSO | Brasil | 5106505 | 51 | 33 | nan | nan | nan | Pantanal | 12.5 |
| 16d7026a-5988-33b2-8e32-3a5b6504cf71 | -16.9717 | -56.76032 | 2024-10-06 05:14:00 | NOAA-21 | POCONÉ | MATO GROSSO | Brasil | 5106505 | 51 | 33 | nan | nan | nan | Pantanal | 12.5 |
| bb9d59e5-da2f-3134-bf2d-a6d943b43c6f | -16.97109 | -56.76455 | 2024-10-06 05:14:00 | NOAA-21 | POCONÉ | MATO GROSSO | Brasil | 5106505 | 51 | 33 | nan | nan | nan | Pantanal | 7.8 |
| 6eed9222-8cee-3e00-8ee2-72de4e8829c4 | -16.97104 | -56.79044 | 2024-10-06 05:14:00 | NOAA-21 | POCONÉ | MATO GROSSO | Brasil | 5106505 | 51 | 33 | nan | nan | nan | Pantanal | 2.5 |
| 59a2d4c2-7944-3925-8117-219057f22331 | -16.96753 | -56.764 | 2024-10-06 05:14:00 | NOAA-21 | POCONÉ | MATO GROSSO | Brasil | 5106505 | 51 | 33 | nan | nan | nan | Pantanal | 7.3 |
| 594a0b0a-2b47-36f3-8dff-b7f7f6210bf5 | -16.96275 | -56.7719 | 2024-10-06 05:14:00 | NOAA-21 | POCONÉ | MATO GROSSO | Brasil | 5106505 | 51 | 33 | nan | nan | nan | Pantanal | 18.9 |
| b1b81de2-5870-3c3f-a710-9775106704e5 | -16.95978 | -56.76712 | 2024-10-06 05:14:00 | NOAA-21 | POCONÉ | MATO GROSSO | Brasil | 5106505 | 51 | 33 | nan | nan | nan | Pantanal | 1.5 |
| ea1e1f1a-4048-3891-9f9c-64ec73593e13 | -16.8674 | -56.73236 | 2024-10-06 05:14:00 | NOAA-21 | POCONÉ | MATO GROSSO | Brasil | 5106505 | 51 | 33 | nan | nan | nan | Pantanal | 1.5 |
| a4e9165e-d611-3b62-bcfb-02068118774c | -16.86443 | -56.72758 | 2024-10-06 05:14:00 | NOAA-21 | POCONÉ | MATO GROSSO | Brasil | 5106505 | 51 | 33 | nan | nan | nan | Pantanal | 2.9 |
| 55987837-3c55-33e9-ba04-4b019b215dc9 | -16.86383 | -56.73181 | 2024-10-06 05:14:00 | NOAA-21 | POCONÉ | MATO GROSSO | Brasil | 5106505 | 51 | 33 | nan | nan | nan | Pantanal | 2.1 |
| da0fbb87-5fdb-391f-a75a-a76565dda83a | -16.86322 | -56.73603 | 2024-10-06 05:14:00 | NOAA-21 | POCONÉ | MATO GROSSO | Brasil | 5106505 | 51 | 33 | nan | nan | nan | Pantanal | 2.1 |
| 79caba53-0440-3ba1-890d-9d0dff7ab806 | -16.86207 | -56.71857 | 2024-10-06 05:14:00 | NOAA-21 | POCONÉ | MATO GROSSO | Brasil | 5106505 | 51 | 33 | nan | nan | nan | Pantanal | 4.5 |
| 0e5fe09c-ce31-3db1-a492-ce32670a5d09 | -16.85909 | -56.71379 | 2024-10-06 05:14:00 | NOAA-21 | POCONÉ | MATO GROSSO | Brasil | 5106505 | 51 | 33 | nan | nan | nan | Pantanal | 5.0 |
| 841de54c-42ff-3824-8b4f-be501fd1f763 | -16.85849 | -56.71803 | 2024-10-06 05:14:00 | NOAA-21 | POCONÉ | MATO GROSSO | Brasil | 5106505 | 51 | 33 | nan | nan | nan | Pantanal | 5.0 |
| 38d9f465-6eea-388e-b04c-cfaebc34c31f | -16.85608 | -56.73494 | 2024-10-06 05:14:00 | NOAA-21 | POCONÉ | MATO GROSSO | Brasil | 5106505 | 51 | 33 | nan | nan | nan | Pantanal | 3.6 |
| a9119011-3fe5-3718-8403-c550c99217db | -16.85552 | -56.71324 | 2024-10-06 05:14:00 | NOAA-21 | POCONÉ | MATO GROSSO | Brasil | 5106505 | 51 | 33 | nan | nan | nan | Pantanal | 5.0 |
| 5b41aba6-72c1-3e6c-b388-9823afde05a1 | -17.11645 | -56.80491 | 2024-10-06 05:14:00 | NOAA-21 | POCONÉ | MATO GROSSO | Brasil | 5106505 | 51 | 33 | nan | nan | nan | Pantanal | 17.6 |
| 502f6ccb-eebe-39d5-9958-d9a953f8a627 | -17.11406 | -56.7959 | 2024-10-06 05:14:00 | NOAA-21 | POCONÉ | MATO GROSSO | Brasil | 5106505 | 51 | 33 | nan | nan | nan | Pantanal | 3.8 |
| 603e063c-934f-362b-99ce-af521c73ad64 | -17.11347 | -56.80013 | 2024-10-06 05:14:00 | NOAA-21 | POCONÉ | MATO GROSSO | Brasil | 5106505 | 51 | 33 | nan | nan | nan | Pantanal | 2.5 |
| 5ebb2445-2204-3a1f-9dc7-85fe7b5bfc57 | -17.11229 | -56.80859 | 2024-10-06 05:14:00 | NOAA-21 | POCONÉ | MATO GROSSO | Brasil | 5106505 | 51 | 33 | nan | nan | nan | Pantanal | 10.3 |
| 4dda2520-f447-30b4-a6d9-5f27eca160cc | -17.10931 | -56.80381 | 2024-10-06 05:14:00 | NOAA-21 | POCONÉ | MATO GROSSO | Brasil | 5106505 | 51 | 33 | nan | nan | nan | Pantanal | 2.5 |
| 64e7ff80-da52-323f-8e24-408f5479c4d2 | -17.10574 | -56.80326 | 2024-10-06 05:14:00 | NOAA-21 | POCONÉ | MATO GROSSO | Brasil | 5106505 | 51 | 33 | nan | nan | nan | Pantanal | 3.6 |
| 02bbe18e-c730-3b50-b4fe-a51db059e383 | -17.10515 | -56.80748 | 2024-10-06 05:14:00 | NOAA-21 | POCONÉ | MATO GROSSO | Brasil | 5106505 | 51 | 33 | nan | nan | nan | Pantanal | 4.8 |
| 4cd15544-f5c1-3ee6-abc3-cea35ec03cbb | -17.10457 | -56.81171 | 2024-10-06 05:14:00 | NOAA-21 | POCONÉ | MATO GROSSO | Brasil | 5106505 | 51 | 33 | nan | nan | nan | Pantanal | 4.8 |
| 42d4dbb4-5879-33e4-86c2-ee694ee454b3 | -17.10041 | -56.81538 | 2024-10-06 05:14:00 | NOAA-21 | POCONÉ | MATO GROSSO | Brasil | 5106505 | 51 | 33 | nan | nan | nan | Pantanal | 6.2 |
| 6eed908b-5a4a-3a7f-8cf8-ece9b97165de | -17.10008 | -56.79983 | 2024-10-06 05:14:00 | NOAA-21 | POCONÉ | MATO GROSSO | Brasil | 5106505 | 51 | 33 | nan | nan | nan | Pantanal | 2.6 |
| 7c44b167-24ae-3c0a-988f-10643c1f9c02 | -17.09978 | -56.7937 | 2024-10-06 05:14:00 | NOAA-21 | POCONÉ | MATO GROSSO | Brasil | 5106505 | 51 | 33 | nan | nan | nan | Pantanal | 2.1 |
| b76f5496-02f3-3ac2-a52e-e46b2c348b6c | -17.09948 | -56.80404 | 2024-10-06 05:14:00 | NOAA-21 | POCONÉ | MATO GROSSO | Brasil | 5106505 | 51 | 33 | nan | nan | nan | Pantanal | 2.6 |
| 61d867cf-2c18-3849-af40-aec90f69420c | -17.09826 | -56.81248 | 2024-10-06 05:14:00 | NOAA-21 | POCONÉ | MATO GROSSO | Brasil | 5106505 | 51 | 33 | nan | nan | nan | Pantanal | 3.8 |


[Clique aqui para ver as próximas entradas](README126.md)
