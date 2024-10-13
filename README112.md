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

## Dados Diários - Página 112

| ID | Latitude | Longitude | Data/Hora GMT | Satélite | Município | Estado | País | Município ID | Estado ID | País ID | Dias sem Chuva | Precipitação | Risco de Fogo | Bioma | FRP |
|----|----------|-----------|---------------|----------|-----------|--------|------|--------------|-----------|---------|----------------|--------------|----------------|-------|-----|
| 33324d41-9b82-3ca3-998b-a783b9f431c0 | -3.09993 | -53.02439 | 2024-10-13 05:33:00 | AQUA_M-M | MEDICILÂNDIA | PARÁ | Brasil | 1504455 | 15 | 33 | nan | nan | nan | Amazônia | 10.8 |
| d77bdb33-ed28-3f24-a15a-98edef3854dd | -3.09806 | -53.03685 | 2024-10-13 05:33:00 | AQUA_M-M | MEDICILÂNDIA | PARÁ | Brasil | 1504455 | 15 | 33 | nan | nan | nan | Amazônia | 55.5 |
| 442f098e-bdeb-371c-a2ef-1142231a9876 | -3.02135 | -51.20264 | 2024-10-13 05:33:00 | AQUA_M-M | ANAPU | PARÁ | Brasil | 1500859 | 15 | 33 | nan | nan | nan | Amazônia | 9.2 |
| b64cf443-8e0c-392a-9d2e-2fc6d53719a9 | -3.01985 | -51.21244 | 2024-10-13 05:33:00 | AQUA_M-M | ANAPU | PARÁ | Brasil | 1500859 | 15 | 33 | nan | nan | nan | Amazônia | 7.4 |
| 7dacde2e-bb2e-3e35-9fe3-4f3209ccc534 | -2.99934 | -49.52136 | 2024-10-13 05:33:00 | AQUA_M-M | MOJU | PARÁ | Brasil | 1504703 | 15 | 33 | nan | nan | nan | Amazônia | 17.5 |
| c5d27fe3-1e24-3b7e-bff0-107e05842923 | -2.99802 | -49.53017 | 2024-10-13 05:33:00 | AQUA_M-M | MOJU | PARÁ | Brasil | 1504703 | 15 | 33 | nan | nan | nan | Amazônia | 22.2 |
| 871c86f3-74a5-39d8-b05d-054abdfbca5f | -2.82617 | -51.33313 | 2024-10-13 05:33:00 | AQUA_M-M | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 11.5 |
| 047aeeb9-0298-3d0f-9cfd-aeba7ce9a649 | -2.82464 | -51.34309 | 2024-10-13 05:33:00 | AQUA_M-M | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 3.6 |
| 2689795c-e232-32b8-b0ca-ef48de174865 | -2.81033 | -51.01414 | 2024-10-13 05:33:00 | AQUA_M-M | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 5.9 |
| 2fb95281-c125-35b5-a9c4-ab362a5fc920 | -2.80221 | -49.29372 | 2024-10-13 05:33:00 | AQUA_M-M | MOJU | PARÁ | Brasil | 1504703 | 15 | 33 | nan | nan | nan | Amazônia | 19.1 |
| 6ae15fc0-960b-3ca8-b65a-8619e15a3e9b | -2.79574 | -51.36374 | 2024-10-13 05:33:00 | AQUA_M-M | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 3.4 |
| df9bd2d3-0ad3-3e5b-be14-aec890273f01 | -2.79337 | -49.29244 | 2024-10-13 05:33:00 | AQUA_M-M | MOJU | PARÁ | Brasil | 1504703 | 15 | 33 | nan | nan | nan | Amazônia | 12.8 |
| fb1baba9-f58a-39a2-b527-7a8b297db8a2 | -2.78283 | -49.36277 | 2024-10-13 05:33:00 | AQUA_M-M | MOJU | PARÁ | Brasil | 1504703 | 15 | 33 | nan | nan | nan | Amazônia | 12.0 |
| 55351ba0-0df2-39f8-921d-5ec857dcf134 | -2.76006 | -48.40094 | 2024-10-13 05:33:00 | AQUA_M-M | TOMÉ-AÇU | PARÁ | Brasil | 1508001 | 15 | 33 | nan | nan | nan | Amazônia | 8.1 |
| 5f926fcc-0337-3382-8e4b-e7a1b0402ea3 | -2.75022 | -49.51996 | 2024-10-13 05:33:00 | AQUA_M-M | BAIÃO | PARÁ | Brasil | 1501204 | 15 | 33 | nan | nan | nan | Amazônia | 5.4 |
| 00018760-0550-3308-b085-02c1115e79b2 | -2.53101 | -47.26973 | 2024-10-13 05:33:00 | AQUA_M-M | CAPITÃO POÇO | PARÁ | Brasil | 1502301 | 15 | 33 | nan | nan | nan | Amazônia | 5.9 |
| 59fdd319-2d94-3156-afc3-25cee24f902d | -2.52438 | -49.67332 | 2024-10-13 05:33:00 | AQUA_M-M | CAMETÁ | PARÁ | Brasil | 1502103 | 15 | 33 | nan | nan | nan | Amazônia | 13.8 |
| 78592eb8-319b-3b2e-b933-227f60093a1f | -2.17849 | -48.83706 | 2024-10-13 05:33:00 | AQUA_M-M | MOJU | PARÁ | Brasil | 1504703 | 15 | 33 | nan | nan | nan | Amazônia | 4.3 |
| 82a818b9-cccd-3887-990b-00643786d19a | -2.17718 | -48.84584 | 2024-10-13 05:33:00 | AQUA_M-M | MOJU | PARÁ | Brasil | 1504703 | 15 | 33 | nan | nan | nan | Amazônia | 6.0 |
| d12be139-3ebe-368c-8679-7fd08832845c | -2.17319 | -48.80267 | 2024-10-13 05:33:00 | AQUA_M-M | MOJU | PARÁ | Brasil | 1504703 | 15 | 33 | nan | nan | nan | Amazônia | 5.6 |
| d765a198-7209-3857-b811-d22b0afd2ebd | -2.17188 | -48.81145 | 2024-10-13 05:33:00 | AQUA_M-M | MOJU | PARÁ | Brasil | 1504703 | 15 | 33 | nan | nan | nan | Amazônia | 21.1 |
| ec539ddb-b93c-3f67-ae7e-790f66794b73 | -1.6674 | -52.13109 | 2024-10-13 05:33:00 | AQUA_M-M | PORTO DE MOZ | PARÁ | Brasil | 1505908 | 15 | 33 | nan | nan | nan | Amazônia | 6.4 |
| 5b8a0332-fbf9-330c-88cd-5e6492498f89 | -1.0577 | -47.92764 | 2024-10-13 05:33:00 | AQUA_M-M | CASTANHAL | PARÁ | Brasil | 1502400 | 15 | 33 | nan | nan | nan | Amazônia | 37.6 |
| ffd012eb-3e97-3cbb-be19-bf905e9adb88 | -1.05904 | -47.91867 | 2024-10-13 05:33:00 | AQUA_M-M | CASTANHAL | PARÁ | Brasil | 1502400 | 15 | 33 | nan | nan | nan | Amazônia | 24.5 |
| 2dd42b2f-547d-3dcd-bc9e-2233fa739268 | -8.06512 | -44.8151 | 2024-10-13 05:36:00 | AQUA_M-M | URUÇUÍ | PIAUÍ | Brasil | 2211209 | 22 | 33 | nan | nan | nan | Cerrado | 18.3 |
| 9d97711e-fc69-39d6-a5a3-63c42efe21c8 | -8.06267 | -44.83297 | 2024-10-13 05:36:00 | AQUA_M-M | URUÇUÍ | PIAUÍ | Brasil | 2211209 | 22 | 33 | nan | nan | nan | Cerrado | 11.6 |
| 74eff675-bb9a-394e-b707-ba626442ac79 | -7.68644 | -47.30426 | 2024-10-13 05:36:00 | AQUA_M-M | CAROLINA | MARANHÃO | Brasil | 2102804 | 21 | 33 | nan | nan | nan | Cerrado | 7.1 |
| e15b381e-c5c6-37ef-b8b8-e67412d6187f | -7.68489 | -47.3152 | 2024-10-13 05:36:00 | AQUA_M-M | CAROLINA | MARANHÃO | Brasil | 2102804 | 21 | 33 | nan | nan | nan | Cerrado | 30.7 |
| be39e247-71e5-3b82-8754-e6d37bc6817b | -7.6751 | -47.31383 | 2024-10-13 05:36:00 | AQUA_M-M | CAROLINA | MARANHÃO | Brasil | 2102804 | 21 | 33 | nan | nan | nan | Cerrado | 73.9 |
| d22ac9da-39e9-3a0f-970f-127a9309b58a | -7.67356 | -47.32479 | 2024-10-13 05:36:00 | AQUA_M-M | CAROLINA | MARANHÃO | Brasil | 2102804 | 21 | 33 | nan | nan | nan | Cerrado | 13.9 |
| 1ea5533a-8ea2-393e-93ab-1778be719c3a | -7.58653 | -49.58323 | 2024-10-13 05:36:00 | AQUA_M-M | FLORESTA DO ARAGUAIA | PARÁ | Brasil | 1503044 | 15 | 33 | nan | nan | nan | Amazônia | 5.5 |
| 6aab99fd-783c-3a2a-b069-b2a33d54cfc1 | -7.3882 | -47.24447 | 2024-10-13 05:36:00 | AQUA_M-M | CAROLINA | MARANHÃO | Brasil | 2102804 | 21 | 33 | nan | nan | nan | Cerrado | 31.6 |
| 1c64534f-5152-3713-bf2b-b0fe7d367f7d | -7.38666 | -47.25548 | 2024-10-13 05:36:00 | AQUA_M-M | CAROLINA | MARANHÃO | Brasil | 2102804 | 21 | 33 | nan | nan | nan | Cerrado | 35.1 |
| 3b2d83d4-30ad-3700-a677-2e52e7ab2fb4 | -7.38596 | -47.24868 | 2024-10-13 05:36:00 | AQUA_M-M | CAROLINA | MARANHÃO | Brasil | 2102804 | 21 | 33 | nan | nan | nan | Cerrado | 62.6 |
| f71c8862-8a3d-372e-86e8-39823b078bde | -7.38436 | -47.25968 | 2024-10-13 05:36:00 | AQUA_M-M | CAROLINA | MARANHÃO | Brasil | 2102804 | 21 | 33 | nan | nan | nan | Cerrado | 9.8 |
| 45c22827-6b6f-31c3-8311-aca4758bd201 | -6.14384 | -47.27871 | 2024-10-13 05:36:00 | AQUA_M-M | CAMPESTRE DO MARANHÃO | MARANHÃO | Brasil | 2102556 | 21 | 33 | nan | nan | nan | Cerrado | 3.6 |
| 3dfe88e8-7dd7-3517-a22f-72dce74195c0 | -6.13423 | -47.27731 | 2024-10-13 05:36:00 | AQUA_M-M | CAMPESTRE DO MARANHÃO | MARANHÃO | Brasil | 2102556 | 21 | 33 | nan | nan | nan | Cerrado | 7.9 |
| 338d3286-d014-3282-af6b-6c41ce3566cf | -6.08483 | -44.62811 | 2024-10-13 05:36:00 | AQUA_M-M | MIRADOR | MARANHÃO | Brasil | 2106706 | 21 | 33 | nan | nan | nan | Cerrado | 16.0 |
| 627e812c-d3cb-311f-bdb2-fac95564a263 | -5.64921 | -48.64867 | 2024-10-13 05:36:00 | AQUA_M-M | SÃO DOMINGOS DO ARAGUAIA | PARÁ | Brasil | 1507151 | 15 | 33 | nan | nan | nan | Amazônia | 5.8 |
| 3131bc6c-cb64-344e-aced-fc50e62d44ab | -5.57842 | -46.16135 | 2024-10-13 05:36:00 | AQUA_M-M | GRAJAÚ | MARANHÃO | Brasil | 2104800 | 21 | 33 | nan | nan | nan | Cerrado | 13.0 |
| 8fc87aa8-5f4d-36e9-99e9-bcad9ebe40b4 | -5.57669 | -46.17336 | 2024-10-13 05:36:00 | AQUA_M-M | GRAJAÚ | MARANHÃO | Brasil | 2104800 | 21 | 33 | nan | nan | nan | Cerrado | 16.0 |
| 2e28b38d-4f24-3927-b8f8-09fa60a877e2 | -4.90896 | -47.66343 | 2024-10-13 05:36:00 | AQUA_M-M | AÇAILÂNDIA | MARANHÃO | Brasil | 2100055 | 21 | 33 | nan | nan | nan | Amazônia | 3.9 |
| 123ab8ec-a172-305f-953a-7a70c11231c2 | -4.79081 | -48.08526 | 2024-10-13 05:36:00 | AQUA_M-M | RONDON DO PARÁ | PARÁ | Brasil | 1506187 | 15 | 33 | nan | nan | nan | Amazônia | 4.7 |
| 7b2fb13d-0967-3037-8854-5c6e17ba419c | -4.62078 | -50.95411 | 2024-10-13 05:36:00 | AQUA_M-M | ANAPU | PARÁ | Brasil | 1500859 | 15 | 33 | nan | nan | nan | Amazônia | 5.7 |
| 6a1d2cca-2923-3a9e-a7ec-c99966ebae86 | -9.44893 | -45.51056 | 2024-10-13 05:38:00 | AQUA_M-M | SANTA FILOMENA | PIAUÍ | Brasil | 2209203 | 22 | 33 | nan | nan | nan | Cerrado | 25.7 |
| f5784287-8b3c-3a67-a6f9-4426bd424eab | -15.32878 | -41.89045 | 2024-10-13 05:38:00 | AQUA_M-M | SÃO JOÃO DO PARAÍSO | MINAS GERAIS | Brasil | 3162708 | 31 | 33 | nan | nan | nan | Mata Atlântica | 121.3 |
| 79f81865-c82e-32ca-b186-74317ae624e2 | -15.32466 | -41.8824 | 2024-10-13 05:38:00 | AQUA_M-M | SÃO JOÃO DO PARAÍSO | MINAS GERAIS | Brasil | 3162708 | 31 | 33 | nan | nan | nan | Mata Atlântica | 113.4 |
| fcecc4a0-511e-348d-afba-6c82bab8d082 | -13.21265 | -49.82619 | 2024-10-13 05:38:00 | AQUA_M-M | SÃO MIGUEL DO ARAGUAIA | GOIÁS | Brasil | 5220207 | 52 | 33 | nan | nan | nan | Cerrado | 3.8 |
| 44284772-db44-39c1-b325-850dbc62e953 | -11.11234 | -43.33318 | 2024-10-13 05:38:00 | AQUA_M-M | BARRA | BAHIA | Brasil | 2902708 | 29 | 33 | nan | nan | nan | Caatinga | 24.4 |
| a96f0766-a6f4-312a-a419-d823c80a42b5 | -10.95051 | -44.66269 | 2024-10-13 05:38:00 | AQUA_M-M | SANTA RITA DE CÁSSIA | BAHIA | Brasil | 2928406 | 29 | 33 | nan | nan | nan | Cerrado | 66.4 |
| 096110d5-a8bf-3447-a102-5b9b1552ce10 | -10.94913 | -44.65733 | 2024-10-13 05:38:00 | AQUA_M-M | SANTA RITA DE CÁSSIA | BAHIA | Brasil | 2928406 | 29 | 33 | nan | nan | nan | Cerrado | 58.9 |
| e499c352-0135-3370-9b86-edf90a564360 | -10.94658 | -44.67661 | 2024-10-13 05:38:00 | AQUA_M-M | SANTA RITA DE CÁSSIA | BAHIA | Brasil | 2928406 | 29 | 33 | nan | nan | nan | Cerrado | 21.3 |
| 9c56cf4f-bd83-384f-9d2e-d4a8cd495aec | -10.51561 | -42.48927 | 2024-10-13 05:38:00 | AQUA_M-M | XIQUE-XIQUE | BAHIA | Brasil | 2933604 | 29 | 33 | nan | nan | nan | Caatinga | 23.9 |
| 1095e856-9836-350c-9159-3df742aa3e17 | -10.51237 | -42.51614 | 2024-10-13 05:38:00 | AQUA_M-M | XIQUE-XIQUE | BAHIA | Brasil | 2933604 | 29 | 33 | nan | nan | nan | Caatinga | 45.4 |
| 7971abae-4c1b-32ef-870a-42fa79b74c60 | -10.51221 | -42.51125 | 2024-10-13 05:38:00 | AQUA_M-M | XIQUE-XIQUE | BAHIA | Brasil | 2933604 | 29 | 33 | nan | nan | nan | Caatinga | 58.2 |
| 9423786f-7651-35e1-bd92-fffa0d7d9b04 | -9.96076 | -47.26904 | 2024-10-13 05:38:00 | AQUA_M-M | RIO SONO | TOCANTINS | Brasil | 1718758 | 17 | 33 | nan | nan | nan | Cerrado | 14.7 |
| 2106cbe7-f206-301b-aad4-b63479a8a53c | -9.95828 | -47.27525 | 2024-10-13 05:38:00 | AQUA_M-M | RIO SONO | TOCANTINS | Brasil | 1718758 | 17 | 33 | nan | nan | nan | Cerrado | 21.7 |
| b2c46489-50c6-323a-bb9a-4494e826bb38 | -9.72103 | -52.84947 | 2024-10-13 05:38:00 | AQUA_M-M | PEIXOTO DE AZEVEDO | MATO GROSSO | Brasil | 5106422 | 51 | 33 | nan | nan | nan | Amazônia | 13.6 |
| 0196009d-9919-36a9-9217-219758b970c9 | -9.71646 | -52.81745 | 2024-10-13 05:38:00 | AQUA_M-M | PEIXOTO DE AZEVEDO | MATO GROSSO | Brasil | 5106422 | 51 | 33 | nan | nan | nan | Amazônia | 11.5 |
| d261c850-219f-3f6d-8bc4-cc4a315267dc | -9.71169 | -52.84774 | 2024-10-13 05:38:00 | AQUA_M-M | PEIXOTO DE AZEVEDO | MATO GROSSO | Brasil | 5106422 | 51 | 33 | nan | nan | nan | Amazônia | 16.4 |
| ded14038-8bda-3563-85cc-de050d17ac05 | -9.70549 | -52.82609 | 2024-10-13 05:38:00 | AQUA_M-M | PEIXOTO DE AZEVEDO | MATO GROSSO | Brasil | 5106422 | 51 | 33 | nan | nan | nan | Amazônia | 15.0 |
| 55a3f851-85cb-3dc7-a60a-1d5aee608ab7 | -9.05229 | -52.9949 | 2024-10-13 05:38:00 | AQUA_M-M | SÃO FÉLIX DO XINGU | PARÁ | Brasil | 1507300 | 15 | 33 | nan | nan | nan | Amazônia | 10.1 |
| 4e185056-1e00-3418-a0f6-86b020fe059b | -8.86407 | -53.01701 | 2024-10-13 05:38:00 | AQUA_M-M | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 5.7 |
| f069a260-fdd9-3dd9-a4fb-b6c55513540b | -8.79073 | -49.929 | 2024-10-13 05:38:00 | AQUA_M-M | SANTA MARIA DAS BARREIRAS | PARÁ | Brasil | 1506583 | 15 | 33 | nan | nan | nan | Amazônia | 4.4 |
| 46a7381f-bdb5-332b-8315-e6b30980403b | -8.69807 | -49.92781 | 2024-10-13 05:38:00 | AQUA_M-M | SANTA MARIA DAS BARREIRAS | PARÁ | Brasil | 1506583 | 15 | 33 | nan | nan | nan | Amazônia | 8.4 |
| cf11e634-e039-3aff-add5-4fc09792dfe3 | -10.32852 | -48.79618 | 2024-10-13 05:38:00 | AQUA_M-M | PARAÍSO DO TOCANTINS | TOCANTINS | Brasil | 1716109 | 17 | 33 | nan | nan | nan | Cerrado | 5.8 |
| 9a76f0a4-da59-31c1-9492-03db9a005a72 | -12.39296 | -47.31645 | 2024-10-13 05:38:00 | AQUA_M-M | CONCEIÇÃO DO TOCANTINS | TOCANTINS | Brasil | 1705607 | 17 | 33 | nan | nan | nan | Cerrado | 6.3 |
| bc45ecdc-3a99-3aba-b439-714b8bc4e2c3 | -12.28732 | -47.65283 | 2024-10-13 05:38:00 | AQUA_M-M | PARANÃ | TOCANTINS | Brasil | 1716208 | 17 | 33 | nan | nan | nan | Cerrado | 13.4 |
| 3ef11793-b7dd-393d-bf88-94ae69817033 | -12.27877 | -47.63926 | 2024-10-13 05:38:00 | AQUA_M-M | PARANÃ | TOCANTINS | Brasil | 1716208 | 17 | 33 | nan | nan | nan | Cerrado | 7.4 |
| 5685425f-ada0-32e0-b271-5cd736bc2dbd | -12.27708 | -47.65149 | 2024-10-13 05:38:00 | AQUA_M-M | PARANÃ | TOCANTINS | Brasil | 1716208 | 17 | 33 | nan | nan | nan | Cerrado | 17.2 |
| 7e309ffc-2da5-3e9d-9449-aa992435429d | -12.19064 | -50.70636 | 2024-10-13 05:38:00 | AQUA_M-M | NOVO SANTO ANTÔNIO | MATO GROSSO | Brasil | 5106315 | 51 | 33 | nan | nan | nan | Cerrado | 3.5 |
| e85dbd6f-11f2-317f-b8e8-95883ed9db6d | -12.18176 | -50.70503 | 2024-10-13 05:38:00 | AQUA_M-M | NOVO SANTO ANTÔNIO | MATO GROSSO | Brasil | 5106315 | 51 | 33 | nan | nan | nan | Cerrado | 9.0 |
| 5e97a9f9-908b-34b6-908f-c6aebe131667 | -11.75116 | -48.36065 | 2024-10-13 05:38:00 | AQUA_M-M | SÃO VALÉRIO | TOCANTINS | Brasil | 1720499 | 17 | 33 | nan | nan | nan | Cerrado | 12.6 |
| 67309837-284d-3387-828d-2813eb413386 | -11.74967 | -48.37148 | 2024-10-13 05:38:00 | AQUA_M-M | SÃO VALÉRIO | TOCANTINS | Brasil | 1720499 | 17 | 33 | nan | nan | nan | Cerrado | 13.6 |
| 12f2c7bc-4ef1-34e6-a33b-72411ea16dfd | -11.66362 | -49.05923 | 2024-10-13 05:38:00 | AQUA_M-M | GURUPI | TOCANTINS | Brasil | 1709500 | 17 | 33 | nan | nan | nan | Cerrado | 4.1 |
| 9821337e-db23-3284-ba88-f84f29aaaddd | -11.64562 | -48.38409 | 2024-10-13 05:38:00 | AQUA_M-M | SÃO VALÉRIO | TOCANTINS | Brasil | 1720499 | 17 | 33 | nan | nan | nan | Cerrado | 8.8 |
| 750a83da-a202-3199-be83-b36e1c64cc5f | -11.6438 | -48.37719 | 2024-10-13 05:38:00 | AQUA_M-M | SÃO VALÉRIO | TOCANTINS | Brasil | 1720499 | 17 | 33 | nan | nan | nan | Cerrado | 9.4 |
| 159c8455-e4b7-3b51-9e3d-d738f85d11a9 | -11.64227 | -48.38794 | 2024-10-13 05:38:00 | AQUA_M-M | PEIXE | TOCANTINS | Brasil | 1716604 | 17 | 33 | nan | nan | nan | Cerrado | 18.7 |
| 57a6e4b7-c0e7-38cb-a26c-b5315f0ce169 | -11.63414 | -48.37583 | 2024-10-13 05:38:00 | AQUA_M-M | SÃO VALÉRIO | TOCANTINS | Brasil | 1720499 | 17 | 33 | nan | nan | nan | Cerrado | 47.2 |
| 7b21ba8d-bf32-3a2e-884a-268574315abe | -11.63261 | -48.38661 | 2024-10-13 05:38:00 | AQUA_M-M | SÃO VALÉRIO | TOCANTINS | Brasil | 1720499 | 17 | 33 | nan | nan | nan | Cerrado | 30.9 |
| 017e8dc8-b70c-39f5-9f5a-6f41bfa1d1c9 | -11.62447 | -48.37448 | 2024-10-13 05:38:00 | AQUA_M-M | SÃO VALÉRIO | TOCANTINS | Brasil | 1720499 | 17 | 33 | nan | nan | nan | Cerrado | 14.1 |
| f9075dcf-7ed3-36e0-840f-4674b5d8bbb4 | -11.27369 | -50.91145 | 2024-10-13 05:38:00 | AQUA_M-M | LUCIARA | MATO GROSSO | Brasil | 5105309 | 51 | 33 | nan | nan | nan | Cerrado | 6.5 |
| 3440e017-339c-3af5-a73f-a3d4bd5061e6 | -11.20807 | -47.84456 | 2024-10-13 05:38:00 | AQUA_M-M | SILVANÓPOLIS | TOCANTINS | Brasil | 1720655 | 17 | 33 | nan | nan | nan | Cerrado | 9.1 |
| 18730b51-f26c-3ea2-8154-3fd702201f77 | -11.26483 | -50.91012 | 2024-10-13 05:38:00 | AQUA_M-M | LUCIARA | MATO GROSSO | Brasil | 5105309 | 51 | 33 | nan | nan | nan | Cerrado | 4.1 |
| a3a37149-b5a7-330f-b29b-672cfb6bb85e | -10.82508 | -51.13946 | 2024-10-13 05:38:00 | AQUA_M-M | PORTO ALEGRE DO NORTE | MATO GROSSO | Brasil | 5106778 | 51 | 33 | nan | nan | nan | Cerrado | 6.9 |
| 8a1fd2d4-0ac1-35fb-81fb-06056d4994e8 | -10.5303 | -49.95224 | 2024-10-13 05:38:00 | AQUA_M-M | PIUM | TOCANTINS | Brasil | 1717503 | 17 | 33 | nan | nan | nan | Cerrado | 7.7 |
| ea441ca3-ede1-309c-90ee-97acab5f9037 | -10.52896 | -49.96137 | 2024-10-13 05:38:00 | AQUA_M-M | PIUM | TOCANTINS | Brasil | 1717503 | 17 | 33 | nan | nan | nan | Cerrado | 4.5 |
| f506ccf7-d835-3232-abd3-fe4648670717 | -10.52002 | -49.96006 | 2024-10-13 05:38:00 | AQUA_M-M | PIUM | TOCANTINS | Brasil | 1717503 | 17 | 33 | nan | nan | nan | Cerrado | 8.4 |
| 7bcd8deb-8325-3ee4-82a0-f5189d84cfdd | -18.22972 | -56.54249 | 2024-10-13 05:40:00 | AQUA_M-M | CORUMBÁ | MATO GROSSO DO SUL | Brasil | 5003207 | 50 | 33 | nan | nan | nan | Pantanal | 10.1 |
| 59b13221-2301-3223-a434-443af88d9a59 | -18.22753 | -56.55556 | 2024-10-13 05:40:00 | AQUA_M-M | CORUMBÁ | MATO GROSSO DO SUL | Brasil | 5003207 | 50 | 33 | nan | nan | nan | Pantanal | 12.3 |
| a950c4b3-082a-309f-ab5c-0247682a2d17 | -18.22532 | -56.56868 | 2024-10-13 05:40:00 | AQUA_M-M | CORUMBÁ | MATO GROSSO DO SUL | Brasil | 5003207 | 50 | 33 | nan | nan | nan | Pantanal | 7.1 |
| 9d45c0de-c11b-35ca-b3a7-d2cb695fd202 | -17.97265 | -57.38187 | 2024-10-13 05:40:00 | AQUA_M-M | CORUMBÁ | MATO GROSSO DO SUL | Brasil | 5003207 | 50 | 33 | nan | nan | nan | Pantanal | 15.8 |
| c6e71942-708a-3279-b7c1-b55331867b34 | -17.96157 | -57.37975 | 2024-10-13 05:40:00 | AQUA_M-M | CORUMBÁ | MATO GROSSO DO SUL | Brasil | 5003207 | 50 | 33 | nan | nan | nan | Pantanal | 31.5 |
| 07ae07a0-c08e-3d81-a8c0-a55b66b02593 | -17.91151 | -57.33926 | 2024-10-13 05:40:00 | AQUA_M-M | CORUMBÁ | MATO GROSSO DO SUL | Brasil | 5003207 | 50 | 33 | nan | nan | nan | Pantanal | 19.7 |
| b05997e9-c34c-3af6-848b-e4d18d4f916f | -17.90883 | -57.3542 | 2024-10-13 05:40:00 | AQUA_M-M | CORUMBÁ | MATO GROSSO DO SUL | Brasil | 5003207 | 50 | 33 | nan | nan | nan | Pantanal | 27.4 |
| 6934dcc5-fa6f-371d-a064-e66aec7c45cd | -17.90796 | -57.34847 | 2024-10-13 05:40:00 | AQUA_M-M | CORUMBÁ | MATO GROSSO DO SUL | Brasil | 5003207 | 50 | 33 | nan | nan | nan | Pantanal | 28.4 |
| 2bd24656-7b8e-31ea-ad21-d6319e7adf8d | -15.65678 | -59.98533 | 2024-10-13 05:40:00 | AQUA_M-M | PONTES E LACERDA | MATO GROSSO | Brasil | 5106752 | 51 | 33 | nan | nan | nan | Amazônia | 27.1 |
| 9257b7b0-d315-3493-b4be-26292fd24b75 | 1.12784 | -59.52829 | 2024-10-13 06:18:00 | NOAA-21 | CAROEBE | RORAIMA | Brasil | 1400233 | 14 | 33 | nan | nan | nan | Amazônia | 5.3 |
| 522f1b77-80aa-3877-917b-3f59d33102ca | 1.12162 | -59.52029 | 2024-10-13 06:18:00 | NOAA-21 | CAROEBE | RORAIMA | Brasil | 1400233 | 14 | 33 | nan | nan | nan | Amazônia | 3.6 |
| 85e5cced-797b-39fa-a2f4-2e7970c96ce4 | 1.11969 | -59.52269 | 2024-10-13 06:18:00 | NOAA-21 | CAROEBE | RORAIMA | Brasil | 1400233 | 14 | 33 | nan | nan | nan | Amazônia | 6.5 |


[Clique aqui para ver as próximas entradas](README113.md)
