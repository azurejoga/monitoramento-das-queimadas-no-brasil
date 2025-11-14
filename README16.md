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
| 253997c1-0184-3364-9b98-04037ece5130 | -7.85583 | -44.29296 | 2025-11-14 03:53:00 | NOAA-21 | URUÇUÍ | PIAUÍ | Brasil | 2211209 | 22 | 33 | nan | nan | nan | Cerrado | 8.5 |
| 61c6b1fc-fc17-3fd1-a266-1346694f9c0d | -6.11287 | -41.58298 | 2025-11-14 03:53:00 | NOAA-21 | PIMENTEIRAS | PIAUÍ | Brasil | 2208106 | 22 | 33 | nan | nan | nan | Caatinga | 2.1 |
| 74775f09-009d-3d41-859e-3e8bce47bf9a | -8.49928 | -39.61553 | 2025-11-14 03:53:00 | NOAA-21 | OROCÓ | PERNAMBUCO | Brasil | 2609808 | 26 | 33 | nan | nan | nan | Caatinga | 1.3 |
| 13d384f2-c6e0-30f7-9fcd-1d3537950a3b | -5.58487 | -41.09345 | 2025-11-14 03:53:00 | NOAA-21 | SÃO MIGUEL DO TAPUIO | PIAUÍ | Brasil | 2210409 | 22 | 33 | nan | nan | nan | Caatinga | 1.3 |
| bdc2c089-4cce-3c28-aaac-41a612f7f977 | -6.24159 | -38.89463 | 2025-11-14 03:53:00 | NOAA-21 | ORÓS | CEARÁ | Brasil | 2309508 | 23 | 33 | nan | nan | nan | Caatinga | 1.2 |
| 6f117421-9b01-3d24-add7-53df472bceed | -4.21788 | -49.12455 | 2025-11-14 03:53:00 | NOAA-21 | GOIANÉSIA DO PARÁ | PARÁ | Brasil | 1503093 | 15 | 33 | nan | nan | nan | Amazônia | 11.9 |
| 4d4e447b-49f5-3b5b-807e-7efd9ba04bf6 | -7.4597 | -42.76395 | 2025-11-14 03:53:00 | NOAA-21 | FLORES DO PIAUÍ | PIAUÍ | Brasil | 2203800 | 22 | 33 | nan | nan | nan | Caatinga | 1.1 |
| 57023f32-fec6-33d0-b6f2-3f16b0e40764 | -7.48588 | -42.55414 | 2025-11-14 03:53:00 | NOAA-21 | SÃO JOSÉ DO PEIXE | PIAUÍ | Brasil | 2210102 | 22 | 33 | nan | nan | nan | Caatinga | 2.3 |
| 64c471f2-bf42-3961-a6f7-5dcb3cdbb481 | -5.42543 | -43.19768 | 2025-11-14 03:53:00 | NOAA-21 | MATÕES | MARANHÃO | Brasil | 2106607 | 21 | 33 | nan | nan | nan | Cerrado | 0.8 |
| 07dc3947-b7e5-35d6-9d80-3414b138b107 | -4.76646 | -44.7879 | 2025-11-14 03:53:00 | NOAA-21 | POÇÃO DE PEDRAS | MARANHÃO | Brasil | 2108900 | 21 | 33 | nan | nan | nan | Cerrado | 1.8 |
| 0b3b1575-41a0-3d0f-9c67-6b9a5dbb0d1c | -5.31272 | -40.93917 | 2025-11-14 03:53:00 | NOAA-21 | BURITI DOS MONTES | PIAUÍ | Brasil | 2202026 | 22 | 33 | nan | nan | nan | Caatinga | 2.3 |
| 8a3782e1-6f2d-398e-8180-d765bc705232 | -6.53598 | -43.4076 | 2025-11-14 03:53:00 | NOAA-21 | SUCUPIRA DO RIACHÃO | MARANHÃO | Brasil | 2111953 | 21 | 33 | nan | nan | nan | Caatinga | 1.5 |
| b4c9f0cb-4450-3af7-b1aa-c8f493f79d1d | -6.81171 | -41.5137 | 2025-11-14 03:53:00 | NOAA-21 | SÃO JOSÉ DO PIAUÍ | PIAUÍ | Brasil | 2210201 | 22 | 33 | nan | nan | nan | Caatinga | 1.4 |
| 7cd96792-c42f-36ea-8423-cd7c5d8f25bf | -6.88604 | -42.85084 | 2025-11-14 03:53:00 | NOAA-21 | FLORIANO | PIAUÍ | Brasil | 2203909 | 22 | 33 | nan | nan | nan | Caatinga | 6.5 |
| dda96477-a2b5-3b30-a07c-b15ee43cee64 | -6.06318 | -41.56594 | 2025-11-14 03:53:00 | NOAA-21 | SÃO MIGUEL DO TAPUIO | PIAUÍ | Brasil | 2210409 | 22 | 33 | nan | nan | nan | Caatinga | 2.7 |
| 10d3075c-25e2-323f-8711-db3d472ad1be | -7.84807 | -44.28762 | 2025-11-14 03:53:00 | NOAA-21 | URUÇUÍ | PIAUÍ | Brasil | 2211209 | 22 | 33 | nan | nan | nan | Cerrado | 3.3 |
| caec3ad9-f3e9-31cf-a141-dfc567c642e8 | -6.13196 | -41.69498 | 2025-11-14 03:53:00 | NOAA-21 | AROAZES | PIAUÍ | Brasil | 2200905 | 22 | 33 | nan | nan | nan | Caatinga | 2.7 |
| b2e13717-fb57-37ed-b5a5-0939adfb5d56 | -4.70662 | -46.44542 | 2025-11-14 03:53:00 | NOAA-21 | BURITICUPU | MARANHÃO | Brasil | 2102325 | 21 | 33 | nan | nan | nan | Amazônia | 7.8 |
| b0a91fb8-f95b-32b9-b7ef-52e318de6e7e | -6.11132 | -41.56934 | 2025-11-14 03:53:00 | NOAA-21 | PIMENTEIRAS | PIAUÍ | Brasil | 2208106 | 22 | 33 | nan | nan | nan | Caatinga | 3.8 |
| e64a662b-894c-3609-801d-dd50806e39af | -7.3749 | -42.58966 | 2025-11-14 03:53:00 | NOAA-21 | SÃO FRANCISCO DO PIAUÍ | PIAUÍ | Brasil | 2209708 | 22 | 33 | nan | nan | nan | Caatinga | 1.4 |
| 38e8ebdf-0f24-35d4-ab5a-036df308fb3c | -7.72298 | -42.36484 | 2025-11-14 03:53:00 | NOAA-21 | SÃO MIGUEL DO FIDALGO | PIAUÍ | Brasil | 2210391 | 22 | 33 | nan | nan | nan | Caatinga | 2.5 |
| 076f2c17-5ed4-3911-a7cc-11668216fb90 | -5.33872 | -41.86098 | 2025-11-14 03:53:00 | NOAA-21 | NOVO SANTO ANTÔNIO | PIAUÍ | Brasil | 2206951 | 22 | 33 | nan | nan | nan | Caatinga | 2.0 |
| 42b748d6-be6d-333a-a49f-4ea5091d0eb8 | -7.44951 | -42.5634 | 2025-11-14 03:53:00 | NOAA-21 | SÃO JOSÉ DO PEIXE | PIAUÍ | Brasil | 2210102 | 22 | 33 | nan | nan | nan | Caatinga | 2.2 |
| c79fef88-d075-3789-afd2-95fe0c139fe0 | -7.93278 | -44.32655 | 2025-11-14 03:53:00 | NOAA-21 | URUÇUÍ | PIAUÍ | Brasil | 2211209 | 22 | 33 | nan | nan | nan | Cerrado | 2.4 |
| 0a51e833-36ca-3138-8ae3-6d66af0d43c9 | -6.06753 | -41.56224 | 2025-11-14 03:53:00 | NOAA-21 | SÃO MIGUEL DO TAPUIO | PIAUÍ | Brasil | 2210409 | 22 | 33 | nan | nan | nan | Caatinga | 2.7 |
| c028d605-77d7-3668-b589-0093b014db52 | -4.00821 | -48.80473 | 2025-11-14 03:53:00 | NOAA-21 | GOIANÉSIA DO PARÁ | PARÁ | Brasil | 1503093 | 15 | 33 | nan | nan | nan | Amazônia | 2.1 |
| 54ce693b-d26f-30b3-a585-5b9ad13cf80a | -4.70196 | -46.05035 | 2025-11-14 03:53:00 | NOAA-21 | SANTA LUZIA | MARANHÃO | Brasil | 2110005 | 21 | 33 | nan | nan | nan | Amazônia | 1.4 |
| bcb0111e-ce89-3548-accb-da99966995e9 | -5.54448 | -41.81719 | 2025-11-14 03:53:00 | NOAA-21 | SÃO JOÃO DA SERRA | PIAUÍ | Brasil | 2209906 | 22 | 33 | nan | nan | nan | Caatinga | 3.1 |
| 6bcc73f0-fb0f-3937-8edd-131563353687 | -5.61355 | -41.76876 | 2025-11-14 03:53:00 | NOAA-21 | SÃO MIGUEL DO TAPUIO | PIAUÍ | Brasil | 2210409 | 22 | 33 | nan | nan | nan | Caatinga | 4.4 |
| 7b206768-bcd3-3f90-b7b6-8fedf689f6d8 | -7.86681 | -44.30737 | 2025-11-14 03:53:00 | NOAA-21 | URUÇUÍ | PIAUÍ | Brasil | 2211209 | 22 | 33 | nan | nan | nan | Cerrado | 1.4 |
| aca6380c-31ab-37bc-a57a-fe1e31919707 | -5.77243 | -40.26482 | 2025-11-14 03:53:00 | NOAA-21 | TAUÁ | CEARÁ | Brasil | 2313302 | 23 | 33 | nan | nan | nan | Caatinga | 1.1 |
| ea46f73c-0e78-3ddf-bf46-5ae0abdc2d3a | -5.61526 | -41.0646 | 2025-11-14 03:53:00 | NOAA-21 | SÃO MIGUEL DO TAPUIO | PIAUÍ | Brasil | 2210409 | 22 | 33 | nan | nan | nan | Caatinga | 2.2 |
| cfe27565-9f67-3817-b0af-e045d205c153 | -7.9341 | -44.31869 | 2025-11-14 03:53:00 | NOAA-21 | URUÇUÍ | PIAUÍ | Brasil | 2211209 | 22 | 33 | nan | nan | nan | Cerrado | 2.4 |
| 51529ade-9384-3e7e-8a8d-4b437793711b | -6.14293 | -43.70641 | 2025-11-14 03:53:00 | NOAA-21 | PASSAGEM FRANCA | MARANHÃO | Brasil | 2107902 | 21 | 33 | nan | nan | nan | Cerrado | 2.9 |
| 5eedeb4d-1abe-3279-9bb4-11103e165a39 | -7.63557 | -46.15638 | 2025-11-14 03:53:00 | NOAA-21 | BALSAS | MARANHÃO | Brasil | 2101400 | 21 | 33 | nan | nan | nan | Cerrado | 1.0 |
| 36684706-3947-3a42-a465-fc3d4becf4c9 | -7.85487 | -44.30133 | 2025-11-14 03:53:00 | NOAA-21 | URUÇUÍ | PIAUÍ | Brasil | 2211209 | 22 | 33 | nan | nan | nan | Cerrado | 1.9 |
| 57031082-e23b-3004-9445-9f6f548177ea | -5.42495 | -42.57655 | 2025-11-14 03:53:00 | NOAA-21 | LAGOA DO PIAUÍ | PIAUÍ | Brasil | 2205581 | 22 | 33 | nan | nan | nan | Caatinga | 1.6 |
| 8f2898af-20ca-36e1-8439-1175b7476a43 | -4.5302 | -46.398 | 2025-11-14 03:53:00 | NOAA-21 | BURITICUPU | MARANHÃO | Brasil | 2102325 | 21 | 33 | nan | nan | nan | Amazônia | 1.9 |
| 492b1e40-0b1b-3e03-b667-1564cbad7fd0 | -6.61483 | -47.63995 | 2025-11-14 03:53:00 | NOAA-21 | PALMEIRAS DO TOCANTINS | TOCANTINS | Brasil | 1713809 | 17 | 33 | nan | nan | nan | Cerrado | 1.1 |
| 34b9278c-7be6-311b-b202-d3384317d4b2 | -7.46165 | -42.56063 | 2025-11-14 03:53:00 | NOAA-21 | SÃO JOSÉ DO PEIXE | PIAUÍ | Brasil | 2210102 | 22 | 33 | nan | nan | nan | Caatinga | 7.3 |
| b47c1012-7a71-3bf2-97d6-543169bdc4ea | -7.77958 | -43.79459 | 2025-11-14 03:53:00 | NOAA-21 | BERTOLÍNIA | PIAUÍ | Brasil | 2201705 | 22 | 33 | nan | nan | nan | Caatinga | 2.3 |
| 834ae798-378f-3b17-baeb-7282a4bd5552 | -7.93145 | -44.33443 | 2025-11-14 03:53:00 | NOAA-21 | URUÇUÍ | PIAUÍ | Brasil | 2211209 | 22 | 33 | nan | nan | nan | Cerrado | 2.3 |
| bebb7ef8-5dfb-38a0-ac20-fae83b536843 | -7.46239 | -42.57986 | 2025-11-14 03:53:00 | NOAA-21 | SÃO JOSÉ DO PEIXE | PIAUÍ | Brasil | 2210102 | 22 | 33 | nan | nan | nan | Caatinga | 2.9 |
| 8b35dcf5-1a72-33a2-9ddf-eb6aa6946522 | -7.85203 | -44.2928 | 2025-11-14 03:53:00 | NOAA-21 | URUÇUÍ | PIAUÍ | Brasil | 2211209 | 22 | 33 | nan | nan | nan | Cerrado | 10.7 |
| 81f00d77-74ba-3c6c-a465-11fe72344f37 | -7.48687 | -45.91024 | 2025-11-14 03:53:00 | NOAA-21 | BALSAS | MARANHÃO | Brasil | 2101400 | 21 | 33 | nan | nan | nan | Cerrado | 1.2 |
| 098e990b-aeab-3ddc-bae4-57059128050d | -4.96436 | -47.71934 | 2025-11-14 03:53:00 | NOAA-21 | AÇAILÂNDIA | MARANHÃO | Brasil | 2100055 | 21 | 33 | nan | nan | nan | Amazônia | 5.8 |
| 4efc6a9b-cbb5-35b5-a8c9-d9d03074a4fc | -5.60491 | -45.18324 | 2025-11-14 03:53:00 | NOAA-21 | BARRA DO CORDA | MARANHÃO | Brasil | 2101608 | 21 | 33 | nan | nan | nan | Cerrado | 1.8 |
| 5e9a6ff6-9043-3eea-9068-6dffed7e6b37 | -7.93698 | -44.32727 | 2025-11-14 03:53:00 | NOAA-21 | URUÇUÍ | PIAUÍ | Brasil | 2211209 | 22 | 33 | nan | nan | nan | Cerrado | 1.2 |
| 11ff62aa-425a-3d77-9363-b8b77dd62c15 | -4.70609 | -46.44852 | 2025-11-14 03:53:00 | NOAA-21 | BURITICUPU | MARANHÃO | Brasil | 2102325 | 21 | 33 | nan | nan | nan | Amazônia | 7.8 |
| 7eceb6d7-19b1-3ba4-bb92-55051cc88a58 | -6.88965 | -42.85875 | 2025-11-14 03:53:00 | NOAA-21 | FLORIANO | PIAUÍ | Brasil | 2203909 | 22 | 33 | nan | nan | nan | Caatinga | 31.3 |
| 7b9c822e-a414-3c28-a61d-d1c29699bd90 | -7.3816 | -48.65179 | 2025-11-14 03:53:00 | NOAA-21 | ARAGUAÍNA | TOCANTINS | Brasil | 1702109 | 17 | 33 | nan | nan | nan | Amazônia | 1.3 |
| 01b838ee-d1dd-3e74-b412-4c818ef79ed7 | -6.10661 | -41.52899 | 2025-11-14 03:53:00 | NOAA-21 | PIMENTEIRAS | PIAUÍ | Brasil | 2208106 | 22 | 33 | nan | nan | nan | Caatinga | 1.7 |
| 27219349-f958-3683-a70e-9834fa1dbb4d | -7.66796 | -45.88239 | 2025-11-14 03:53:00 | NOAA-21 | BALSAS | MARANHÃO | Brasil | 2101400 | 21 | 33 | nan | nan | nan | Cerrado | 3.7 |
| 5f3a6c74-5dda-3846-b7e5-f870541f984c | -7.84256 | -44.29474 | 2025-11-14 03:53:00 | NOAA-21 | URUÇUÍ | PIAUÍ | Brasil | 2211209 | 22 | 33 | nan | nan | nan | Cerrado | 7.8 |
| ef7b8731-d73d-3d29-ac7d-ffebb8ffc07c | -6.47996 | -39.34609 | 2025-11-14 03:53:00 | NOAA-21 | IGUATU | CEARÁ | Brasil | 2305506 | 23 | 33 | nan | nan | nan | Caatinga | 1.3 |
| abc3e136-538f-399d-96be-4d9a4aa24aad | -5.4975 | -41.90766 | 2025-11-14 03:53:00 | NOAA-21 | SÃO JOÃO DA SERRA | PIAUÍ | Brasil | 2209906 | 22 | 33 | nan | nan | nan | Caatinga | 1.4 |
| 7e0de282-ca52-3674-8ae2-50224891f92c | -7.34503 | -46.01486 | 2025-11-14 03:53:00 | NOAA-21 | BALSAS | MARANHÃO | Brasil | 2101400 | 21 | 33 | nan | nan | nan | Cerrado | 1.9 |
| 8c505071-642f-3b8c-a7f5-5d44f4f2c409 | -4.10781 | -48.01445 | 2025-11-14 03:53:00 | NOAA-21 | DOM ELISEU | PARÁ | Brasil | 1502939 | 15 | 33 | nan | nan | nan | Amazônia | 3.3 |
| 3aa46c5e-5443-3b1c-b085-edd92ac41c20 | -7.06721 | -43.58013 | 2025-11-14 03:53:00 | NOAA-21 | JERUMENHA | PIAUÍ | Brasil | 2205300 | 22 | 33 | nan | nan | nan | Cerrado | 1.0 |
| 999f2d8f-c947-340a-92d4-896298ad9677 | -6.42806 | -47.29966 | 2025-11-14 03:53:00 | NOAA-21 | PORTO FRANCO | MARANHÃO | Brasil | 2109007 | 21 | 33 | nan | nan | nan | Cerrado | 2.1 |
| a7e2d16b-8f47-31a2-91f8-ec9e286548ad | -7.45936 | -42.57456 | 2025-11-14 03:53:00 | NOAA-21 | SÃO JOSÉ DO PEIXE | PIAUÍ | Brasil | 2210102 | 22 | 33 | nan | nan | nan | Caatinga | 2.9 |
| ada548ab-78ac-389e-a0d5-e3f43e99ec2d | -4.75225 | -46.39359 | 2025-11-14 03:53:00 | NOAA-21 | BURITICUPU | MARANHÃO | Brasil | 2102325 | 21 | 33 | nan | nan | nan | Amazônia | 1.3 |
| fff8ca73-4e4a-3c32-a74b-01eec519e19b | -7.88228 | -44.31804 | 2025-11-14 03:53:00 | NOAA-21 | URUÇUÍ | PIAUÍ | Brasil | 2211209 | 22 | 33 | nan | nan | nan | Cerrado | 1.7 |
| ef8b5b58-6164-3366-8c93-2190b26205f2 | -5.48987 | -47.69886 | 2025-11-14 03:53:00 | NOAA-21 | SÃO MIGUEL DO TOCANTINS | TOCANTINS | Brasil | 1720200 | 17 | 33 | nan | nan | nan | Cerrado | 1.4 |
| a4e138ac-6219-3ebe-8a18-11d4f55b9e1f | -6.10785 | -41.59084 | 2025-11-14 03:53:00 | NOAA-21 | PIMENTEIRAS | PIAUÍ | Brasil | 2208106 | 22 | 33 | nan | nan | nan | Caatinga | 2.1 |
| 706b7726-0532-32fb-9a14-891e43e1c49d | -4.71691 | -46.44694 | 2025-11-14 03:53:00 | NOAA-21 | BURITICUPU | MARANHÃO | Brasil | 2102325 | 21 | 33 | nan | nan | nan | Amazônia | 6.6 |
| 1faf3a19-3631-3d62-b473-451afd78de50 | -7.27907 | -38.81079 | 2025-11-14 03:53:00 | NOAA-21 | MILAGRES | CEARÁ | Brasil | 2308302 | 23 | 33 | nan | nan | nan | Caatinga | 2.1 |
| 6b93cdc8-4172-3cd6-b915-a05ca2283db2 | -5.49414 | -42.16566 | 2025-11-14 03:53:00 | NOAA-21 | ALTO LONGÁ | PIAUÍ | Brasil | 2200301 | 22 | 33 | nan | nan | nan | Caatinga | 2.2 |
| b0d040d3-9b09-3014-94b0-69bd97da0c82 | -6.57911 | -42.15897 | 2025-11-14 03:53:00 | NOAA-21 | BARRA D'ALCÂNTARA | PIAUÍ | Brasil | 2201176 | 22 | 33 | nan | nan | nan | Caatinga | 1.3 |
| e980eace-7bce-39e2-91ac-5dc0fa58c0f5 | -7.46997 | -42.58111 | 2025-11-14 03:53:00 | NOAA-21 | SÃO JOSÉ DO PEIXE | PIAUÍ | Brasil | 2210102 | 22 | 33 | nan | nan | nan | Caatinga | 1.9 |
| 5c755352-ea88-3796-ad1a-a646dce54ba5 | -5.41905 | -43.26004 | 2025-11-14 03:53:00 | NOAA-21 | MATÕES | MARANHÃO | Brasil | 2106607 | 21 | 33 | nan | nan | nan | Cerrado | 3.4 |
| a22a2eae-05d6-38a5-a8f8-24d445122f7d | -5.7535 | -45.11041 | 2025-11-14 03:53:00 | NOAA-21 | BARRA DO CORDA | MARANHÃO | Brasil | 2101608 | 21 | 33 | nan | nan | nan | Cerrado | 2.2 |
| 2e406b14-e3f5-3177-8768-4a9f7b078523 | -7.11476 | -42.73345 | 2025-11-14 03:53:00 | NOAA-21 | NAZARÉ DO PIAUÍ | PIAUÍ | Brasil | 2206704 | 22 | 33 | nan | nan | nan | Caatinga | 3.4 |
| e46db362-792d-3359-a68f-36088555800a | -5.41936 | -43.26019 | 2025-11-14 03:53:00 | NOAA-21 | MATÕES | MARANHÃO | Brasil | 2106607 | 21 | 33 | nan | nan | nan | Cerrado | 5.3 |
| 476553b3-81b9-3331-b1e5-9d97d502c348 | -5.59183 | -45.17607 | 2025-11-14 03:53:00 | NOAA-21 | BARRA DO CORDA | MARANHÃO | Brasil | 2101608 | 21 | 33 | nan | nan | nan | Cerrado | 4.6 |
| 4a15c348-9b39-3253-9250-0497a3bf0d4c | -5.61168 | -41.06403 | 2025-11-14 03:53:00 | NOAA-21 | SÃO MIGUEL DO TAPUIO | PIAUÍ | Brasil | 2210409 | 22 | 33 | nan | nan | nan | Caatinga | 2.7 |
| 66fb7c4f-bb5b-30a0-83d6-41a5808222ec | -7.6572 | -36.85129 | 2025-11-14 03:53:00 | NOAA-21 | SUMÉ | PARAÍBA | Brasil | 2516300 | 25 | 33 | nan | nan | nan | Caatinga | 0.8 |
| 8da2e580-506f-3293-8229-9e7254242a51 | -5.6003 | -41.06636 | 2025-11-14 03:53:00 | NOAA-21 | SÃO MIGUEL DO TAPUIO | PIAUÍ | Brasil | 2210409 | 22 | 33 | nan | nan | nan | Caatinga | 1.4 |
| 77ecea73-f549-3450-ac6c-b47e227f96a0 | -7.01779 | -46.39651 | 2025-11-14 03:53:00 | NOAA-21 | NOVA COLINAS | MARANHÃO | Brasil | 2107258 | 21 | 33 | nan | nan | nan | Cerrado | 1.2 |
| af6e6fb2-06a8-3e98-8962-1975547fdb46 | -6.2818 | -39.86613 | 2025-11-14 03:53:00 | NOAA-21 | CATARINA | CEARÁ | Brasil | 2303600 | 23 | 33 | nan | nan | nan | Caatinga | 0.7 |
| 00c856f2-f643-3790-bca0-5d1b3a3a54eb | -4.70715 | -46.44233 | 2025-11-14 03:53:00 | NOAA-21 | BURITICUPU | MARANHÃO | Brasil | 2102325 | 21 | 33 | nan | nan | nan | Amazônia | 6.4 |
| 8fb68c54-fb39-32de-b5bf-d7b82f8c8211 | -7.83902 | -44.2901 | 2025-11-14 03:53:00 | NOAA-21 | URUÇUÍ | PIAUÍ | Brasil | 2211209 | 22 | 33 | nan | nan | nan | Cerrado | 2.6 |
| 62a869af-6ec8-3dca-a544-3101dd87e938 | -4.77536 | -48.6786 | 2025-11-14 03:53:00 | NOAA-21 | BOM JESUS DO TOCANTINS | PARÁ | Brasil | 1501576 | 15 | 33 | nan | nan | nan | Amazônia | 2.8 |
| c48378cb-31fe-36c5-9e2d-139b98bf5cd7 | -4.70094 | -46.44781 | 2025-11-14 03:53:00 | NOAA-21 | BURITICUPU | MARANHÃO | Brasil | 2102325 | 21 | 33 | nan | nan | nan | Amazônia | 7.8 |
| 2ac986f2-0612-34d5-98ca-d221ce950707 | -7.44719 | -42.57745 | 2025-11-14 03:53:00 | NOAA-21 | SÃO JOSÉ DO PEIXE | PIAUÍ | Brasil | 2210102 | 22 | 33 | nan | nan | nan | Caatinga | 1.7 |
| 224471bb-e02d-37a9-81d2-3382c514fb8b | -5.50904 | -40.55121 | 2025-11-14 03:53:00 | NOAA-21 | INDEPENDÊNCIA | CEARÁ | Brasil | 2305605 | 23 | 33 | nan | nan | nan | Caatinga | 1.5 |
| 2ad8aebe-f781-32ae-a28a-9f8e1e973233 | -6.28293 | -41.73717 | 2025-11-14 03:53:00 | NOAA-21 | VALENÇA DO PIAUÍ | PIAUÍ | Brasil | 2211308 | 22 | 33 | nan | nan | nan | Caatinga | 1.3 |
| 2c33920e-4c61-3a74-a94f-fed6aa1d1482 | -6.61546 | -47.63651 | 2025-11-14 03:53:00 | NOAA-21 | PALMEIRAS DO TOCANTINS | TOCANTINS | Brasil | 1713809 | 17 | 33 | nan | nan | nan | Cerrado | 1.1 |
| d0cb462a-3e2c-30a9-a511-f382fa92bbb5 | -5.34806 | -46.76524 | 2025-11-14 03:53:00 | NOAA-21 | AMARANTE DO MARANHÃO | MARANHÃO | Brasil | 2100600 | 21 | 33 | nan | nan | nan | Cerrado | 3.8 |
| 53f03a66-5f24-393f-864b-c5a395b2eb3a | -6.11025 | -41.52955 | 2025-11-14 03:53:00 | NOAA-21 | PIMENTEIRAS | PIAUÍ | Brasil | 2208106 | 22 | 33 | nan | nan | nan | Caatinga | 1.7 |
| 41a95a4a-30f4-3659-bec1-8f9af1eb4b64 | -6.28729 | -46.95865 | 2025-11-14 03:53:00 | NOAA-21 | SÃO JOÃO DO PARAÍSO | MARANHÃO | Brasil | 2111052 | 21 | 33 | nan | nan | nan | Cerrado | 1.2 |
| a962e2f8-1552-3229-a6b4-8f8d489b3aa7 | -7.93764 | -44.32333 | 2025-11-14 03:53:00 | NOAA-21 | URUÇUÍ | PIAUÍ | Brasil | 2211209 | 22 | 33 | nan | nan | nan | Cerrado | 1.2 |
| 88db0c5e-e447-3096-b4f7-9ec0dc118fd3 | -7.8626 | -44.30666 | 2025-11-14 03:53:00 | NOAA-21 | URUÇUÍ | PIAUÍ | Brasil | 2211209 | 22 | 33 | nan | nan | nan | Cerrado | 1.4 |
| 0f5f3786-e0a5-33d6-bc23-b93c7d4d5e22 | -4.10204 | -48.01365 | 2025-11-14 03:53:00 | NOAA-21 | DOM ELISEU | PARÁ | Brasil | 1502939 | 15 | 33 | nan | nan | nan | Amazônia | 2.3 |
| 9a666611-b221-34ea-85e0-a60955c44173 | -7.49763 | -47.33349 | 2025-11-14 03:53:00 | NOAA-21 | CAROLINA | MARANHÃO | Brasil | 2102804 | 21 | 33 | nan | nan | nan | Cerrado | 1.1 |
| 9c42888a-efa1-38b2-ae63-6c15df85354f | -6.15387 | -48.05341 | 2025-11-14 03:53:00 | NOAA-21 | ANANÁS | TOCANTINS | Brasil | 1701002 | 17 | 33 | nan | nan | nan | Cerrado | 4.2 |
| 80d75598-fde4-32f2-8b9c-dde8b0206225 | -5.57693 | -47.10094 | 2025-11-14 03:53:00 | NOAA-21 | BURITIRANA | MARANHÃO | Brasil | 2102358 | 21 | 33 | nan | nan | nan | Cerrado | 1.9 |
| f5e3a12e-8cfc-3856-9751-0a585d0b4c00 | -5.72826 | -46.5488 | 2025-11-14 03:53:00 | NOAA-21 | AMARANTE DO MARANHÃO | MARANHÃO | Brasil | 2100600 | 21 | 33 | nan | nan | nan | Cerrado | 0.8 |
| 503520c7-b096-3df2-91af-4b3838ad1b10 | -6.0853 | -41.70734 | 2025-11-14 03:53:00 | NOAA-21 | AROAZES | PIAUÍ | Brasil | 2200905 | 22 | 33 | nan | nan | nan | Caatinga | 3.2 |
| ae7a092e-6107-30c9-8940-f875b4dbe1fa | -7.73375 | -47.25278 | 2025-11-14 03:53:00 | NOAA-21 | CAROLINA | MARANHÃO | Brasil | 2102804 | 21 | 33 | nan | nan | nan | Cerrado | 1.1 |


[Clique aqui para ver as próximas entradas](README17.md)
