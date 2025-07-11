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

## Dados Diários - Página 12

| ID | Latitude | Longitude | Data/Hora GMT | Satélite | Município | Estado | País | Município ID | Estado ID | País ID | Dias sem Chuva | Precipitação | Risco de Fogo | Bioma | FRP |
|----|----------|-----------|---------------|----------|-----------|--------|------|--------------|-----------|---------|----------------|--------------|----------------|-------|-----|
| 1ef0ea96-f87c-3255-8d2d-4deaea6cb4d0 | -13.15881 | -47.27027 | 2025-07-11 04:08:00 | NOAA-20 | ARRAIAS | TOCANTINS | Brasil | 1702406 | 17 | 33 | nan | nan | nan | Cerrado | 1.2 |
| c646d90f-eedc-3c4e-965d-64da2c7528af | -11.93435 | -49.30343 | 2025-07-11 04:08:00 | NOAA-20 | FORMOSO DO ARAGUAIA | TOCANTINS | Brasil | 1708205 | 17 | 33 | nan | nan | nan | Cerrado | 3.9 |
| 983ee5a9-a153-3c1d-8ca0-3ec57b0aa375 | -9.85895 | -47.87207 | 2025-07-11 04:08:00 | NOAA-20 | APARECIDA DO RIO NEGRO | TOCANTINS | Brasil | 1701101 | 17 | 33 | nan | nan | nan | Cerrado | 2.0 |
| 26bc11a5-5955-3fa2-ac9f-9eca8720d239 | -10.63384 | -45.23544 | 2025-07-11 04:08:00 | NOAA-20 | CRISTALÂNDIA DO PIAUÍ | PIAUÍ | Brasil | 2203008 | 22 | 33 | nan | nan | nan | Cerrado | 4.0 |
| a68e6788-ff72-3097-a5a8-cec259e847ff | -12.06843 | -47.98432 | 2025-07-11 04:08:00 | NOAA-20 | PARANÃ | TOCANTINS | Brasil | 1716208 | 17 | 33 | nan | nan | nan | Cerrado | 2.2 |
| b63300d8-6504-3d8d-a5d5-c9476bdba386 | -8.5751 | -47.19495 | 2025-07-11 04:08:00 | NOAA-20 | RECURSOLÂNDIA | TOCANTINS | Brasil | 1718501 | 17 | 33 | nan | nan | nan | Cerrado | 3.3 |
| 50e6d584-6c32-35cc-b8f3-1b35558eb1f9 | -12.98839 | -44.87383 | 2025-07-11 04:08:00 | NOAA-20 | SÃO DESIDÉRIO | BAHIA | Brasil | 2928901 | 29 | 33 | nan | nan | nan | Cerrado | 0.8 |
| d0a96b7c-1a76-32f1-872d-a4f917e745ac | -13.84723 | -45.85189 | 2025-07-11 04:08:00 | NOAA-20 | JABORANDI | BAHIA | Brasil | 2917359 | 29 | 33 | nan | nan | nan | Cerrado | 0.8 |
| ea77f303-6e75-320f-9950-622f15e247d7 | -8.22978 | -44.92749 | 2025-07-11 04:08:00 | NOAA-20 | BAIXA GRANDE DO RIBEIRO | PIAUÍ | Brasil | 2201150 | 22 | 33 | nan | nan | nan | Cerrado | 0.8 |
| 20928d6a-430f-32fc-ae04-0956c4e8ba69 | -11.82683 | -48.2127 | 2025-07-11 04:08:00 | NOAA-20 | SÃO VALÉRIO | TOCANTINS | Brasil | 1720499 | 17 | 33 | nan | nan | nan | Cerrado | 1.9 |
| 6d41d518-3bab-3f9c-87be-d2904a23efad | -13.35921 | -47.88888 | 2025-07-11 04:08:00 | NOAA-20 | CAVALCANTE | GOIÁS | Brasil | 5205307 | 52 | 33 | nan | nan | nan | Cerrado | 4.7 |
| a41b2636-3f93-3edf-8457-f3d1e5d7e6cc | -8.3923 | -46.94185 | 2025-07-11 04:08:00 | NOAA-20 | CAMPOS LINDOS | TOCANTINS | Brasil | 1703842 | 17 | 33 | nan | nan | nan | Cerrado | 2.6 |
| 746982db-5a11-300d-b9d6-e010f1dcab10 | -9.91569 | -47.83097 | 2025-07-11 04:08:00 | NOAA-20 | NOVO ACORDO | TOCANTINS | Brasil | 1715101 | 17 | 33 | nan | nan | nan | Cerrado | 10.3 |
| a49790bc-c265-3c4e-8dc9-0a8e82d9a842 | -8.58433 | -47.18917 | 2025-07-11 04:08:00 | NOAA-20 | RECURSOLÂNDIA | TOCANTINS | Brasil | 1718501 | 17 | 33 | nan | nan | nan | Cerrado | 1.8 |
| 2a472b2c-54bc-38b5-8ad5-cf7b6b9b1588 | -11.43982 | -45.11641 | 2025-07-11 04:08:00 | NOAA-20 | RIACHÃO DAS NEVES | BAHIA | Brasil | 2926202 | 29 | 33 | nan | nan | nan | Cerrado | 1.4 |
| 8fee7fef-7c20-3280-9045-cc94854f2e39 | -8.22047 | -44.91774 | 2025-07-11 04:08:00 | NOAA-20 | BAIXA GRANDE DO RIBEIRO | PIAUÍ | Brasil | 2201150 | 22 | 33 | nan | nan | nan | Cerrado | 0.8 |
| 092735b6-04c4-38a3-a594-23f51afaf53d | -11.44328 | -45.117 | 2025-07-11 04:08:00 | NOAA-20 | RIACHÃO DAS NEVES | BAHIA | Brasil | 2926202 | 29 | 33 | nan | nan | nan | Cerrado | 1.4 |
| 8ebbe97d-bf67-3447-b7fe-7622c39f8f12 | -8.32613 | -46.03758 | 2025-07-11 04:08:00 | NOAA-20 | TASSO FRAGOSO | MARANHÃO | Brasil | 2112001 | 21 | 33 | nan | nan | nan | Cerrado | 1.0 |
| 76b771fa-88e6-3f57-9590-9bdfed8da173 | -13.04312 | -47.87641 | 2025-07-11 04:08:00 | NOAA-20 | PARANÃ | TOCANTINS | Brasil | 1716208 | 17 | 33 | nan | nan | nan | Cerrado | 3.2 |
| 7da84cca-2c46-37f5-aa41-9d6ee9e9d090 | -11.32706 | -51.44032 | 2025-07-11 04:08:00 | NOAA-20 | SÃO FÉLIX DO ARAGUAIA | MATO GROSSO | Brasil | 5107859 | 51 | 33 | nan | nan | nan | Cerrado | 0.8 |
| 9d870e41-b44c-3a21-ba6e-407709b747a1 | -12.40191 | -45.3618 | 2025-07-11 04:08:00 | NOAA-20 | SÃO DESIDÉRIO | BAHIA | Brasil | 2928901 | 29 | 33 | nan | nan | nan | Cerrado | 0.9 |
| 457824f2-4b54-35c1-bccb-6cb005659bc5 | -12.98681 | -44.86215 | 2025-07-11 04:08:00 | NOAA-20 | SÃO DESIDÉRIO | BAHIA | Brasil | 2928901 | 29 | 33 | nan | nan | nan | Cerrado | 1.2 |
| 5ea526fe-319e-3bdb-90bd-10ef9afe3fd9 | -7.32703 | -44.3282 | 2025-07-11 04:08:00 | NOAA-20 | SEBASTIÃO LEAL | PIAUÍ | Brasil | 2210631 | 22 | 33 | nan | nan | nan | Cerrado | 1.2 |
| 18bf84e5-80f8-3eaf-b1f2-1f44eccd855d | -8.37917 | -51.07835 | 2025-07-11 04:08:00 | NOAA-20 | CUMARU DO NORTE | PARÁ | Brasil | 1502764 | 15 | 33 | nan | nan | nan | Amazônia | 2.0 |
| 13fd27fb-3d9d-3934-83dd-4fde03bce295 | -10.90393 | -49.21773 | 2025-07-11 04:08:00 | NOAA-20 | SANTA RITA DO TOCANTINS | TOCANTINS | Brasil | 1718899 | 17 | 33 | nan | nan | nan | Cerrado | 1.9 |
| ccb98a54-88f5-3cdc-a66d-3c2d04f4658f | -8.28101 | -42.2682 | 2025-07-11 04:08:00 | NOAA-20 | SÃO JOÃO DO PIAUÍ | PIAUÍ | Brasil | 2210003 | 22 | 33 | nan | nan | nan | Caatinga | 1.4 |
| 2f0fbc0f-d14a-32d8-be37-c7b2555b32b1 | -11.57393 | -47.4282 | 2025-07-11 04:08:00 | NOAA-20 | NATIVIDADE | TOCANTINS | Brasil | 1714203 | 17 | 33 | nan | nan | nan | Cerrado | 6.4 |
| bd479736-30bf-313a-bbd4-87a26deb1ef3 | -12.99235 | -46.29761 | 2025-07-11 04:08:00 | NOAA-20 | CAMPOS BELOS | GOIÁS | Brasil | 5204904 | 52 | 33 | nan | nan | nan | Cerrado | 2.2 |
| 6e3ef8eb-1c55-3570-8389-8db371f7170d | -7.94179 | -44.84924 | 2025-07-11 04:08:00 | NOAA-20 | URUÇUÍ | PIAUÍ | Brasil | 2211209 | 22 | 33 | nan | nan | nan | Cerrado | 2.9 |
| da3cda59-b0ba-3146-aa6f-1e19f1821c07 | -13.39257 | -44.14051 | 2025-07-11 04:08:00 | NOAA-20 | SÃO FÉLIX DO CORIBE | BAHIA | Brasil | 2929057 | 29 | 33 | nan | nan | nan | Cerrado | 0.4 |
| 53d1d2e6-9de2-3c91-aff7-a39dafd3528b | -13.15106 | -47.29304 | 2025-07-11 04:08:00 | NOAA-20 | ARRAIAS | TOCANTINS | Brasil | 1702406 | 17 | 33 | nan | nan | nan | Cerrado | 2.0 |
| 59a28cb7-0260-3434-a0db-60a711a8235c | -13.84038 | -45.87119 | 2025-07-11 04:08:00 | NOAA-20 | JABORANDI | BAHIA | Brasil | 2917359 | 29 | 33 | nan | nan | nan | Cerrado | 1.8 |
| f450ba58-53f1-33ff-8a7a-4c0e4fdecdf7 | -8.22335 | -44.92233 | 2025-07-11 04:08:00 | NOAA-20 | BAIXA GRANDE DO RIBEIRO | PIAUÍ | Brasil | 2201150 | 22 | 33 | nan | nan | nan | Cerrado | 1.0 |
| 0fe561b4-2f1d-35a6-bbb1-fc7d20cc2895 | -7.55867 | -49.90986 | 2025-07-11 04:08:00 | NOAA-20 | RIO MARIA | PARÁ | Brasil | 1506161 | 15 | 33 | nan | nan | nan | Amazônia | 2.0 |
| fc2f84d2-70d4-3ee9-b237-e4deb0aeff57 | -10.58078 | -49.12719 | 2025-07-11 04:08:00 | NOAA-20 | CRISTALÂNDIA | TOCANTINS | Brasil | 1706100 | 17 | 33 | nan | nan | nan | Cerrado | 14.7 |
| 4018d4ee-7b53-3c6e-aa8c-e7fb33d485cc | -13.402 | -46.80672 | 2025-07-11 04:08:00 | NOAA-20 | MONTE ALEGRE DE GOIÁS | GOIÁS | Brasil | 5213509 | 52 | 33 | nan | nan | nan | Cerrado | 1.1 |
| 56cecb10-3ea7-379e-a7d8-31aaa61cc935 | -12.41937 | -43.49078 | 2025-07-11 04:08:00 | NOAA-20 | MUQUÉM DO SÃO FRANCISCO | BAHIA | Brasil | 2922250 | 29 | 33 | nan | nan | nan | Cerrado | 1.6 |
| d396a212-c2ba-3853-b091-5bf0fc79e65b | -7.43051 | -43.83632 | 2025-07-11 04:08:00 | NOAA-20 | SEBASTIÃO LEAL | PIAUÍ | Brasil | 2210631 | 22 | 33 | nan | nan | nan | Cerrado | 1.0 |
| 3991d811-4f72-3db1-949a-68ab4f5d9490 | -8.88852 | -47.34138 | 2025-07-11 04:08:00 | NOAA-20 | CENTENÁRIO | TOCANTINS | Brasil | 1704105 | 17 | 33 | nan | nan | nan | Cerrado | 1.0 |
| ec296349-ae3f-3ef8-a245-a6f2038715e9 | -11.85256 | -46.75558 | 2025-07-11 04:08:00 | NOAA-20 | NOVO JARDIM | TOCANTINS | Brasil | 1715259 | 17 | 33 | nan | nan | nan | Cerrado | 2.4 |
| 18fc5cbb-2bcb-3bc7-b531-9c7e78d25687 | -8.22757 | -44.91888 | 2025-07-11 04:08:00 | NOAA-20 | BAIXA GRANDE DO RIBEIRO | PIAUÍ | Brasil | 2201150 | 22 | 33 | nan | nan | nan | Cerrado | 0.7 |
| fd93177c-9167-346b-80c6-e40dbc9ef664 | -7.94534 | -44.84981 | 2025-07-11 04:08:00 | NOAA-20 | URUÇUÍ | PIAUÍ | Brasil | 2211209 | 22 | 33 | nan | nan | nan | Cerrado | 4.3 |
| 0589bf4c-0aa8-3dbc-80ac-30457a697a00 | -14.39659 | -43.77002 | 2025-07-11 04:08:00 | NOAA-20 | MALHADA | BAHIA | Brasil | 2920205 | 29 | 33 | nan | nan | nan | Cerrado | 1.3 |
| a7202494-3770-386a-9681-80bcb0573e25 | -11.88584 | -44.94181 | 2025-07-11 04:08:00 | NOAA-20 | RIACHÃO DAS NEVES | BAHIA | Brasil | 2926202 | 29 | 33 | nan | nan | nan | Cerrado | 0.7 |
| deca75a5-443c-37f6-95b7-fdaa506fcd0d | -8.89194 | -47.3457 | 2025-07-11 04:08:00 | NOAA-20 | CENTENÁRIO | TOCANTINS | Brasil | 1704105 | 17 | 33 | nan | nan | nan | Cerrado | 1.0 |
| 8f91e5b8-e596-3ae9-9e00-7000f1eb53e4 | -13.13156 | -47.2934 | 2025-07-11 04:08:00 | NOAA-20 | ARRAIAS | TOCANTINS | Brasil | 1702406 | 17 | 33 | nan | nan | nan | Cerrado | 0.5 |
| 4170ca1e-4bbf-359a-84bb-54d50027ba81 | -12.2308 | -40.3588 | 2025-07-11 04:08:00 | NOAA-20 | RUY BARBOSA | BAHIA | Brasil | 2927200 | 29 | 33 | nan | nan | nan | Caatinga | 0.6 |
| 182dc57d-0862-3c57-8fa7-4ef275c5785e | -10.57635 | -49.12646 | 2025-07-11 04:08:00 | NOAA-20 | CRISTALÂNDIA | TOCANTINS | Brasil | 1706100 | 17 | 33 | nan | nan | nan | Cerrado | 7.2 |
| 331b6eea-0d3d-3058-9e0a-32c34921ebd5 | -12.9942 | -44.8596 | 2025-07-11 04:08:00 | NOAA-20 | SÃO DESIDÉRIO | BAHIA | Brasil | 2928901 | 29 | 33 | nan | nan | nan | Cerrado | 2.0 |
| 41b73fa4-291e-3673-a5fd-28c4d4655d59 | -13.35449 | -47.89294 | 2025-07-11 04:08:00 | NOAA-20 | CAVALCANTE | GOIÁS | Brasil | 5205307 | 52 | 33 | nan | nan | nan | Cerrado | 1.2 |
| 16df2f43-8eb8-3157-968b-4267809bf8d6 | -7.94888 | -44.85041 | 2025-07-11 04:08:00 | NOAA-20 | URUÇUÍ | PIAUÍ | Brasil | 2211209 | 22 | 33 | nan | nan | nan | Cerrado | 4.3 |
| 77ba48e1-16cc-3f90-8369-8ab723c12112 | -12.40537 | -45.36241 | 2025-07-11 04:08:00 | NOAA-20 | SÃO DESIDÉRIO | BAHIA | Brasil | 2928901 | 29 | 33 | nan | nan | nan | Cerrado | 0.9 |
| cf0c401a-e3de-3a18-bf45-7f5a87012912 | -7.4277 | -43.83204 | 2025-07-11 04:08:00 | NOAA-20 | SEBASTIÃO LEAL | PIAUÍ | Brasil | 2210631 | 22 | 33 | nan | nan | nan | Cerrado | 1.2 |
| 33f2e44f-6adb-3f10-a04f-de96f540be60 | -12.05553 | -48.54389 | 2025-07-11 04:08:00 | NOAA-20 | PEIXE | TOCANTINS | Brasil | 1716604 | 17 | 33 | nan | nan | nan | Cerrado | 3.2 |
| 725319f9-a6cd-3943-90f1-75a56aa90d71 | -9.9075 | -47.82949 | 2025-07-11 04:08:00 | NOAA-20 | NOVO ACORDO | TOCANTINS | Brasil | 1715101 | 17 | 33 | nan | nan | nan | Cerrado | 19.9 |
| f4565d67-2a70-3a1f-91ce-5816a386fcf7 | -8.23178 | -44.91547 | 2025-07-11 04:08:00 | NOAA-20 | BAIXA GRANDE DO RIBEIRO | PIAUÍ | Brasil | 2201150 | 22 | 33 | nan | nan | nan | Cerrado | 1.1 |
| 0b9215f8-691f-32ab-acbb-bc0135c5eeee | -13.4966 | -50.22897 | 2025-07-11 04:08:00 | NOAA-20 | SÃO MIGUEL DO ARAGUAIA | GOIÁS | Brasil | 5220207 | 52 | 33 | nan | nan | nan | Cerrado | 1.6 |
| ba9d7dd7-fb5c-3e70-9443-e9a4bca3da94 | -12.98731 | -46.28361 | 2025-07-11 04:08:00 | NOAA-20 | CAMPOS BELOS | GOIÁS | Brasil | 5204904 | 52 | 33 | nan | nan | nan | Cerrado | 2.0 |
| 4e974556-2e2e-31d7-8e36-d75d317214ae | -9.85832 | -47.87573 | 2025-07-11 04:08:00 | NOAA-20 | APARECIDA DO RIO NEGRO | TOCANTINS | Brasil | 1701101 | 17 | 33 | nan | nan | nan | Cerrado | 2.0 |
| 2c25683f-0550-3c8d-8518-58b24bfce71c | -9.90683 | -47.83328 | 2025-07-11 04:08:00 | NOAA-20 | NOVO ACORDO | TOCANTINS | Brasil | 1715101 | 17 | 33 | nan | nan | nan | Cerrado | 14.6 |
| 51c9b23d-59bf-3b99-a123-6058b6f2ea27 | -8.70477 | -50.04691 | 2025-07-11 04:08:00 | NOAA-20 | SANTA MARIA DAS BARREIRAS | PARÁ | Brasil | 1506583 | 15 | 33 | nan | nan | nan | Amazônia | 1.6 |
| 121543dd-283c-361a-87da-bf4a6d9867c6 | -13.00532 | -44.87682 | 2025-07-11 04:08:00 | NOAA-20 | SÃO DESIDÉRIO | BAHIA | Brasil | 2928901 | 29 | 33 | nan | nan | nan | Cerrado | 1.1 |
| e02ebca5-21f2-3197-87b3-e30047cf0933 | -13.15504 | -47.26966 | 2025-07-11 04:08:00 | NOAA-20 | ARRAIAS | TOCANTINS | Brasil | 1702406 | 17 | 33 | nan | nan | nan | Cerrado | 1.2 |
| 8f1701c5-689a-3dbd-bd8b-b6d71b0cb217 | -10.62694 | -48.6808 | 2025-07-11 04:08:00 | NOAA-20 | PORTO NACIONAL | TOCANTINS | Brasil | 1718204 | 17 | 33 | nan | nan | nan | Cerrado | 1.7 |
| 955aaa7f-0f3c-3a03-b537-88f8a66d2598 | -9.5346 | -46.28923 | 2025-07-11 04:08:00 | NOAA-20 | ALTO PARNAÍBA | MARANHÃO | Brasil | 2100501 | 21 | 33 | nan | nan | nan | Cerrado | 1.2 |
| 4ddcf643-0090-3def-87af-9409cfc168c4 | -10.64216 | -45.22871 | 2025-07-11 04:08:00 | NOAA-20 | CRISTALÂNDIA DO PIAUÍ | PIAUÍ | Brasil | 2203008 | 22 | 33 | nan | nan | nan | Cerrado | 3.3 |
| e2c9bb8f-fcc0-3d62-9d04-50c2b9673adc | -13.13532 | -47.29413 | 2025-07-11 04:08:00 | NOAA-20 | ARRAIAS | TOCANTINS | Brasil | 1702406 | 17 | 33 | nan | nan | nan | Cerrado | 1.4 |
| 87fb2235-b3a8-36d3-adff-d6743f6f8576 | -13.14231 | -47.29824 | 2025-07-11 04:08:00 | NOAA-20 | ARRAIAS | TOCANTINS | Brasil | 1702406 | 17 | 33 | nan | nan | nan | Cerrado | 0.6 |
| 0af8970a-23fe-3a87-b390-08ae8b5f89d6 | -8.22012 | -44.9226 | 2025-07-11 04:08:00 | NOAA-20 | BAIXA GRANDE DO RIBEIRO | PIAUÍ | Brasil | 2201150 | 22 | 33 | nan | nan | nan | Cerrado | 1.0 |
| b1511a70-4c0c-3b83-a2bc-d6df36470075 | -8.2198 | -44.92176 | 2025-07-11 04:08:00 | NOAA-20 | BAIXA GRANDE DO RIBEIRO | PIAUÍ | Brasil | 2201150 | 22 | 33 | nan | nan | nan | Cerrado | 0.8 |
| e0c2cdf2-564a-3388-90c6-bc59336b46d3 | -12.05484 | -48.54771 | 2025-07-11 04:08:00 | NOAA-20 | PEIXE | TOCANTINS | Brasil | 1716604 | 17 | 33 | nan | nan | nan | Cerrado | 4.1 |
| 4a93731b-32dd-3390-9c4d-c5394769333f | -7.43112 | -43.83258 | 2025-07-11 04:08:00 | NOAA-20 | SEBASTIÃO LEAL | PIAUÍ | Brasil | 2210631 | 22 | 33 | nan | nan | nan | Cerrado | 1.9 |
| 57bfffe6-900e-3edd-b050-4f99f9a099a2 | -10.62399 | -45.22965 | 2025-07-11 04:08:00 | NOAA-20 | CRISTALÂNDIA DO PIAUÍ | PIAUÍ | Brasil | 2203008 | 22 | 33 | nan | nan | nan | Cerrado | 9.7 |
| 6cdc941a-cf10-3fb3-900d-85d769735b57 | -11.84304 | -47.50323 | 2025-07-11 04:08:00 | NOAA-20 | NATIVIDADE | TOCANTINS | Brasil | 1714203 | 17 | 33 | nan | nan | nan | Cerrado | 3.3 |
| 901b2852-399b-3031-a5b5-96b9a41faca4 | -13.16512 | -47.27905 | 2025-07-11 04:08:00 | NOAA-20 | ARRAIAS | TOCANTINS | Brasil | 1702406 | 17 | 33 | nan | nan | nan | Cerrado | 0.7 |
| 26d27028-6bc5-3ca7-beab-6bc842a1eb97 | -13.14651 | -47.29691 | 2025-07-11 04:08:00 | NOAA-20 | ARRAIAS | TOCANTINS | Brasil | 1702406 | 17 | 33 | nan | nan | nan | Cerrado | 0.8 |
| 6f6b3523-8c2b-3fd0-8dab-0793f36c8550 | -13.16678 | -47.26962 | 2025-07-11 04:08:00 | NOAA-20 | ARRAIAS | TOCANTINS | Brasil | 1702406 | 17 | 33 | nan | nan | nan | Cerrado | 3.1 |
| 736c1491-17a6-3746-98a9-9587855f2fec | -7.95115 | -49.65989 | 2025-07-11 04:08:00 | NOAA-20 | CONCEIÇÃO DO ARAGUAIA | PARÁ | Brasil | 1502707 | 15 | 33 | nan | nan | nan | Amazônia | 4.0 |
| 72e49f93-e4e6-3c7e-8265-d4d9aca5a4d8 | -8.88912 | -47.3378 | 2025-07-11 04:08:00 | NOAA-20 | CENTENÁRIO | TOCANTINS | Brasil | 1704105 | 17 | 33 | nan | nan | nan | Cerrado | 1.4 |
| b8835a2e-f6d7-36bb-b94e-fee4f4ccb42d | -11.83915 | -47.5025 | 2025-07-11 04:08:00 | NOAA-20 | NATIVIDADE | TOCANTINS | Brasil | 1714203 | 17 | 33 | nan | nan | nan | Cerrado | 3.3 |
| eb86370b-89e4-3da4-9d32-615419b1699d | -10.85383 | -49.11933 | 2025-07-11 04:08:00 | NOAA-20 | SANTA RITA DO TOCANTINS | TOCANTINS | Brasil | 1718899 | 17 | 33 | nan | nan | nan | Cerrado | 3.7 |
| fbd809ce-8553-35fb-9b06-7657c9bf2712 | -12.05301 | -48.54821 | 2025-07-11 04:08:00 | NOAA-20 | PEIXE | TOCANTINS | Brasil | 1716604 | 17 | 33 | nan | nan | nan | Cerrado | 4.0 |
| eb7b4108-4193-3f3e-81f5-aa3d545ffc7e | -12.99229 | -46.27586 | 2025-07-11 04:08:00 | NOAA-20 | CAMPOS BELOS | GOIÁS | Brasil | 5204904 | 52 | 33 | nan | nan | nan | Cerrado | 6.0 |
| aa473b3e-86a4-33e5-ac77-bd0936f946f8 | -9.65874 | -49.89149 | 2025-07-11 04:08:00 | NOAA-20 | CASEARA | TOCANTINS | Brasil | 1703909 | 17 | 33 | nan | nan | nan | Cerrado | 2.6 |
| 871f05f8-a15a-3e96-b849-207a91f72703 | -8.23045 | -44.92347 | 2025-07-11 04:08:00 | NOAA-20 | BAIXA GRANDE DO RIBEIRO | PIAUÍ | Brasil | 2201150 | 22 | 33 | nan | nan | nan | Cerrado | 0.8 |
| 847f93a9-8740-3e92-b359-0cac57510279 | -12.41662 | -43.48671 | 2025-07-11 04:08:00 | NOAA-20 | MUQUÉM DO SÃO FRANCISCO | BAHIA | Brasil | 2922250 | 29 | 33 | nan | nan | nan | Cerrado | 1.6 |
| 030c8eff-aaaa-3280-a872-2132a8ca5cc5 | -12.03341 | -48.76059 | 2025-07-11 04:08:00 | NOAA-20 | PEIXE | TOCANTINS | Brasil | 1716604 | 17 | 33 | nan | nan | nan | Cerrado | 1.0 |
| c3ae8329-2437-39c4-8c40-8c7ed042a2ea | -8.22623 | -44.92692 | 2025-07-11 04:08:00 | NOAA-20 | BAIXA GRANDE DO RIBEIRO | PIAUÍ | Brasil | 2201150 | 22 | 33 | nan | nan | nan | Cerrado | 1.0 |
| f4849fa1-e4f0-3d2f-ae64-6e09f983551e | -12.02126 | -49.52196 | 2025-07-11 04:08:00 | NOAA-20 | FORMOSO DO ARAGUAIA | TOCANTINS | Brasil | 1708205 | 17 | 33 | nan | nan | nan | Cerrado | 3.1 |
| 2dffbe92-77d1-3ef5-9e13-6f950e32cf6b | -9.65496 | -49.88547 | 2025-07-11 04:08:00 | NOAA-20 | CASEARA | TOCANTINS | Brasil | 1703909 | 17 | 33 | nan | nan | nan | Cerrado | 1.9 |
| b54ba292-44c5-32e0-9744-9db6489b6136 | -10.85307 | -49.12366 | 2025-07-11 04:08:00 | NOAA-20 | SANTA RITA DO TOCANTINS | TOCANTINS | Brasil | 1718899 | 17 | 33 | nan | nan | nan | Cerrado | 3.7 |
| 241f4a40-8b4d-3db4-9896-7a58e95c6bf2 | -12.47146 | -44.49581 | 2025-07-11 04:08:00 | NOAA-20 | BAIANÓPOLIS | BAHIA | Brasil | 2902500 | 29 | 33 | nan | nan | nan | Cerrado | 0.8 |
| a395c3a7-9190-30c8-a536-5aaf520ab03d | -10.62549 | -48.67965 | 2025-07-11 04:08:00 | NOAA-20 | PORTO NACIONAL | TOCANTINS | Brasil | 1718204 | 17 | 33 | nan | nan | nan | Cerrado | 1.6 |
| 164338c8-2441-3ba9-a014-36043981ce1c | -12.98742 | -44.85843 | 2025-07-11 04:08:00 | NOAA-20 | SÃO DESIDÉRIO | BAHIA | Brasil | 2928901 | 29 | 33 | nan | nan | nan | Cerrado | 0.9 |
| a345c4e3-2216-3cb8-a9d6-000b08fee9e1 | -14.73107 | -41.72747 | 2025-07-11 04:08:00 | NOAA-20 | PRESIDENTE JÂNIO QUADROS | BAHIA | Brasil | 2925709 | 29 | 33 | nan | nan | nan | Caatinga | 1.9 |
| 5f847f9b-ced2-3614-86fe-fae1d32dd99b | -7.65676 | -45.34701 | 2025-07-11 04:08:00 | NOAA-20 | RIBEIRO GONÇALVES | PIAUÍ | Brasil | 2208908 | 22 | 33 | nan | nan | nan | Cerrado | 2.2 |
| 1219e15c-7d0b-3076-acc3-12a0245536e9 | -11.32682 | -45.2171 | 2025-07-11 04:08:00 | NOAA-20 | FORMOSA DO RIO PRETO | BAHIA | Brasil | 2911105 | 29 | 33 | nan | nan | nan | Cerrado | 1.6 |
| e49a992c-ae60-3fb8-b1d2-c40770ffd20e | -10.57241 | -49.1484 | 2025-07-11 04:08:00 | NOAA-20 | CRISTALÂNDIA | TOCANTINS | Brasil | 1706100 | 17 | 33 | nan | nan | nan | Cerrado | 7.1 |
| e4ba3520-00d2-3b3e-9624-49d7dc3026d4 | -8.37627 | -43.95322 | 2025-07-11 04:08:00 | NOAA-20 | MANOEL EMÍDIO | PIAUÍ | Brasil | 2205904 | 22 | 33 | nan | nan | nan | Cerrado | 0.7 |
| 87b8e0d8-0a1f-3620-8871-803e42950f3e | -11.32648 | -51.44334 | 2025-07-11 04:08:00 | NOAA-20 | SÃO FÉLIX DO ARAGUAIA | MATO GROSSO | Brasil | 5107859 | 51 | 33 | nan | nan | nan | Cerrado | 0.8 |


[Clique aqui para ver as próximas entradas](README13.md)
