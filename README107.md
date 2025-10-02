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

## Dados Diários - Página 107

| ID | Latitude | Longitude | Data/Hora GMT | Satélite | Município | Estado | País | Município ID | Estado ID | País ID | Dias sem Chuva | Precipitação | Risco de Fogo | Bioma | FRP |
|----|----------|-----------|---------------|----------|-----------|--------|------|--------------|-----------|---------|----------------|--------------|----------------|-------|-----|
| 5e53c87b-5661-337c-98b3-4d682c3791d6 | -6.66421 | -42.7999 | 2025-10-02 04:49:00 | NOAA-20 | FRANCISCO AYRES | PIAUÍ | Brasil | 2204105 | 22 | 33 | nan | nan | nan | Caatinga | 3.1 |
| 6f1f5dd9-b2a5-303b-a7c6-f580eb29fa2c | -4.48159 | -47.67258 | 2025-10-02 04:49:00 | NOAA-20 | DOM ELISEU | PARÁ | Brasil | 1502939 | 15 | 33 | nan | nan | nan | Amazônia | 1.9 |
| b9578685-cd67-33be-b7bf-ee218ef132ae | -3.38556 | -50.1459 | 2025-10-02 04:49:00 | NOAA-20 | PACAJÁ | PARÁ | Brasil | 1505486 | 15 | 33 | nan | nan | nan | Amazônia | 1.4 |
| b800bb36-c3dd-33d3-87b8-189241f250c9 | -5.5032 | -52.13453 | 2025-10-02 04:49:00 | NOAA-20 | SÃO FÉLIX DO XINGU | PARÁ | Brasil | 1507300 | 15 | 33 | nan | nan | nan | Amazônia | 0.8 |
| 672a3f8f-72b0-354d-a02c-2700ff8c38cb | -6.96622 | -45.34975 | 2025-10-02 04:49:00 | NOAA-20 | SAMBAÍBA | MARANHÃO | Brasil | 2109700 | 21 | 33 | nan | nan | nan | Cerrado | 2.4 |
| 1340a67e-cfef-3eff-967f-a2d64bc8172a | -5.47962 | -51.22504 | 2025-10-02 04:49:00 | NOAA-20 | SÃO FÉLIX DO XINGU | PARÁ | Brasil | 1507300 | 15 | 33 | nan | nan | nan | Amazônia | 1.2 |
| f846a4a1-6255-346e-b830-a3f3f34cf11d | -4.62949 | -49.36828 | 2025-10-02 04:49:00 | NOAA-20 | JACUNDÁ | PARÁ | Brasil | 1503804 | 15 | 33 | nan | nan | nan | Amazônia | 1.8 |
| 3908bcd7-9b08-3d21-ad70-9b6d54151341 | -6.55721 | -43.87628 | 2025-10-02 04:49:00 | NOAA-20 | PASTOS BONS | MARANHÃO | Brasil | 2108009 | 21 | 33 | nan | nan | nan | Cerrado | 2.4 |
| 46bbd619-4128-3f4a-b4fa-062952c176e8 | -6.95623 | -45.31864 | 2025-10-02 04:49:00 | NOAA-20 | SAMBAÍBA | MARANHÃO | Brasil | 2109700 | 21 | 33 | nan | nan | nan | Cerrado | 31.2 |
| ebda4c97-69c1-3012-a39d-6ad30fdf50fd | -6.77342 | -45.58516 | 2025-10-02 04:49:00 | NOAA-20 | MIRADOR | MARANHÃO | Brasil | 2106706 | 21 | 33 | nan | nan | nan | Cerrado | 2.7 |
| fa90d6c9-15e1-3b8f-9171-1cebe8e71d82 | -9.33751 | -45.71105 | 2025-10-02 04:49:00 | NOAA-20 | SANTA FILOMENA | PIAUÍ | Brasil | 2209203 | 22 | 33 | nan | nan | nan | Cerrado | 3.0 |
| 6c5cbe2c-afcf-3852-ae91-02d3d2b24a05 | -9.08937 | -46.72672 | 2025-10-02 04:49:00 | NOAA-20 | BALSAS | MARANHÃO | Brasil | 2101400 | 21 | 33 | nan | nan | nan | Cerrado | 2.5 |
| 4367e7c2-d084-3ef4-87ca-1d596260a3ae | -3.69803 | -49.57163 | 2025-10-02 04:49:00 | NOAA-20 | BREU BRANCO | PARÁ | Brasil | 1501782 | 15 | 33 | nan | nan | nan | Amazônia | 2.6 |
| e3d84d24-d311-35b1-a0f7-06104f321df4 | -3.55268 | -50.32755 | 2025-10-02 04:49:00 | NOAA-20 | PACAJÁ | PARÁ | Brasil | 1505486 | 15 | 33 | nan | nan | nan | Amazônia | 0.6 |
| fc9199c8-8ba8-3589-b4d6-6569a545dcd2 | -5.57849 | -51.56761 | 2025-10-02 04:49:00 | NOAA-20 | SÃO FÉLIX DO XINGU | PARÁ | Brasil | 1507300 | 15 | 33 | nan | nan | nan | Amazônia | 0.7 |
| ebfcfec8-3fc5-3657-b0e0-06ae741c9a6c | -5.91721 | -44.86148 | 2025-10-02 04:49:00 | NOAA-20 | FERNANDO FALCÃO | MARANHÃO | Brasil | 2104081 | 21 | 33 | nan | nan | nan | Cerrado | 1.4 |
| f78f0a73-4fde-37f3-b753-6e8777ca5a4f | -3.45173 | -53.83287 | 2025-10-02 04:49:00 | NOAA-20 | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | 1.6 |
| 4af7f6ce-e1b2-3eb8-8256-fcd1a8a6f53b | -6.96431 | -45.32941 | 2025-10-02 04:49:00 | NOAA-20 | SAMBAÍBA | MARANHÃO | Brasil | 2109700 | 21 | 33 | nan | nan | nan | Cerrado | 3.8 |
| 0a01b781-daf4-3709-b66e-ef7663926055 | -4.54944 | -50.45683 | 2025-10-02 04:49:00 | NOAA-20 | NOVO REPARTIMENTO | PARÁ | Brasil | 1505064 | 15 | 33 | nan | nan | nan | Amazônia | 0.7 |
| 514f7174-da3c-3c03-bc33-9a8d948d8ce8 | -3.0912 | -47.01245 | 2025-10-02 04:49:00 | NOAA-20 | PARAGOMINAS | PARÁ | Brasil | 1505502 | 15 | 33 | nan | nan | nan | Amazônia | 2.0 |
| 99966926-3e80-3e0c-8194-226b5e98982c | -7.78971 | -50.21817 | 2025-10-02 04:49:00 | NOAA-20 | PAU D'ARCO | PARÁ | Brasil | 1505551 | 15 | 33 | nan | nan | nan | Amazônia | 1.1 |
| 851c59e0-c564-335f-82a3-434d8f1a6833 | -1.24751 | -54.22218 | 2025-10-02 04:49:00 | NOAA-20 | MONTE ALEGRE | PARÁ | Brasil | 1504802 | 15 | 33 | nan | nan | nan | Amazônia | 0.8 |
| 107f8418-1797-3e53-80b8-998d3fe043b1 | -3.31722 | -49.08303 | 2025-10-02 04:49:00 | NOAA-20 | MOJU | PARÁ | Brasil | 1504703 | 15 | 33 | nan | nan | nan | Amazônia | 0.7 |
| 9a194466-75b0-3d50-8953-017bae7a03dc | -8.87647 | -46.58627 | 2025-10-02 04:49:00 | NOAA-20 | BALSAS | MARANHÃO | Brasil | 2101400 | 21 | 33 | nan | nan | nan | Cerrado | 1.9 |
| 612a87be-d83a-3703-8921-9db4181d7c74 | -3.8116 | -47.57198 | 2025-10-02 04:49:00 | NOAA-20 | ULIANÓPOLIS | PARÁ | Brasil | 1508126 | 15 | 33 | nan | nan | nan | Amazônia | 4.2 |
| a3fb629b-c1e7-30aa-aac9-3e99b2234929 | -4.50094 | -50.4492 | 2025-10-02 04:49:00 | NOAA-20 | NOVO REPARTIMENTO | PARÁ | Brasil | 1505064 | 15 | 33 | nan | nan | nan | Amazônia | 0.9 |
| ab771b32-326b-32cc-8429-45a517b77c77 | -3.34873 | -43.19637 | 2025-10-02 04:49:00 | NOAA-20 | URBANO SANTOS | MARANHÃO | Brasil | 2112605 | 21 | 33 | nan | nan | nan | Cerrado | 4.0 |
| 90e44245-134d-3478-a75b-7fce32195d42 | -3.8677 | -42.51938 | 2025-10-02 04:49:00 | NOAA-20 | CAMPO LARGO DO PIAUÍ | PIAUÍ | Brasil | 2202174 | 22 | 33 | nan | nan | nan | Caatinga | 1.4 |
| 31845d22-6561-3c79-b1e5-7afa5a5e11e2 | -5.45467 | -42.84752 | 2025-10-02 04:49:00 | NOAA-20 | NAZÁRIA | PIAUÍ | Brasil | 2206720 | 22 | 33 | nan | nan | nan | Caatinga | 1.2 |
| fc0b66ff-855d-3405-af60-4155c41c7778 | -3.81576 | -52.15049 | 2025-10-02 04:49:00 | NOAA-20 | SENADOR JOSÉ PORFÍRIO | PARÁ | Brasil | 1507805 | 15 | 33 | nan | nan | nan | Amazônia | 0.6 |
| f6ea4450-299d-3b11-a02c-e64e1b18d27d | -3.09453 | -47.01013 | 2025-10-02 04:49:00 | NOAA-20 | PARAGOMINAS | PARÁ | Brasil | 1505502 | 15 | 33 | nan | nan | nan | Amazônia | 2.1 |
| 562aba13-b020-3fe1-bf90-b4cb796ba246 | -6.47382 | -44.20702 | 2025-10-02 04:49:00 | NOAA-20 | SUCUPIRA DO NORTE | MARANHÃO | Brasil | 2111904 | 21 | 33 | nan | nan | nan | Cerrado | 1.9 |
| 231a7255-c13b-34fd-9530-9cc555d9a959 | -5.48339 | -42.76194 | 2025-10-02 04:49:00 | NOAA-20 | TERESINA | PIAUÍ | Brasil | 2211001 | 22 | 33 | nan | nan | nan | Caatinga | 1.0 |
| c886e546-dd08-30d3-8cf4-a99914f77bad | -6.96026 | -45.32413 | 2025-10-02 04:49:00 | NOAA-20 | SAMBAÍBA | MARANHÃO | Brasil | 2109700 | 21 | 33 | nan | nan | nan | Cerrado | 3.8 |
| 3c874e70-006c-3f23-bdc8-5410b30832f3 | -8.8917 | -46.60627 | 2025-10-02 04:49:00 | NOAA-20 | BALSAS | MARANHÃO | Brasil | 2101400 | 21 | 33 | nan | nan | nan | Cerrado | 1.2 |
| 7ea23663-d081-39f5-b652-0ac4a51ab2a3 | -3.37644 | -52.71708 | 2025-10-02 04:49:00 | NOAA-20 | MEDICILÂNDIA | PARÁ | Brasil | 1504455 | 15 | 33 | nan | nan | nan | Amazônia | 1.1 |
| 688272f1-f710-370d-b334-26dfb5ae6a61 | -6.70213 | -42.81291 | 2025-10-02 04:49:00 | NOAA-20 | FRANCISCO AYRES | PIAUÍ | Brasil | 2204105 | 22 | 33 | nan | nan | nan | Caatinga | 3.8 |
| 7d331aa0-af47-3fc4-9ed5-e65fc0567e3d | -5.45338 | -42.84677 | 2025-10-02 04:49:00 | NOAA-20 | NAZÁRIA | PIAUÍ | Brasil | 2206720 | 22 | 33 | nan | nan | nan | Caatinga | 1.0 |
| 1985800e-9adf-3511-812e-2ba4aca70981 | -9.32862 | -45.67658 | 2025-10-02 04:49:00 | NOAA-20 | SANTA FILOMENA | PIAUÍ | Brasil | 2209203 | 22 | 33 | nan | nan | nan | Cerrado | 3.8 |
| e9216189-198a-37fc-a90a-9c957cb91d10 | -1.58016 | -47.31448 | 2025-10-02 04:49:00 | NOAA-20 | OURÉM | PARÁ | Brasil | 1505403 | 15 | 33 | nan | nan | nan | Amazônia | 1.0 |
| 7d4536ee-3a6f-3d6f-a417-2c936f40edc4 | -8.89866 | -46.61409 | 2025-10-02 04:49:00 | NOAA-20 | BALSAS | MARANHÃO | Brasil | 2101400 | 21 | 33 | nan | nan | nan | Cerrado | 3.7 |
| 817cc2e3-dfdf-30be-8159-258c8412807c | -8.87888 | -46.5934 | 2025-10-02 04:49:00 | NOAA-20 | BALSAS | MARANHÃO | Brasil | 2101400 | 21 | 33 | nan | nan | nan | Cerrado | 1.4 |
| c7714adc-6565-3be3-bbcf-f9a3434a44ff | -6.32618 | -43.04874 | 2025-10-02 04:49:00 | NOAA-20 | SÃO FRANCISCO DO MARANHÃO | MARANHÃO | Brasil | 2110906 | 21 | 33 | nan | nan | nan | Cerrado | 1.9 |
| 19ed3c4d-0824-36a4-9a27-776b0c65f075 | -3.46771 | -50.0876 | 2025-10-02 04:49:00 | NOAA-20 | PACAJÁ | PARÁ | Brasil | 1505486 | 15 | 33 | nan | nan | nan | Amazônia | 1.6 |
| 53f437d6-b388-3bd1-9b62-7dd82cbd14a2 | -8.50809 | -44.7058 | 2025-10-02 04:49:00 | NOAA-20 | PALMEIRA DO PIAUÍ | PIAUÍ | Brasil | 2207405 | 22 | 33 | nan | nan | nan | Cerrado | 0.7 |
| 1147f163-066f-3cbb-b9d4-6128a02cab77 | -6.55042 | -43.92383 | 2025-10-02 04:49:00 | NOAA-20 | PASTOS BONS | MARANHÃO | Brasil | 2108009 | 21 | 33 | nan | nan | nan | Cerrado | 2.2 |
| db784a92-7b54-3ad6-b9bd-ea5bfa283748 | -2.64641 | -54.58057 | 2025-10-02 04:49:00 | NOAA-20 | SANTARÉM | PARÁ | Brasil | 1506807 | 15 | 33 | nan | nan | nan | Amazônia | 0.4 |
| 68b963a0-0a61-3c9d-ac45-a6156531b51e | -6.04438 | -42.44236 | 2025-10-02 04:49:00 | NOAA-20 | HUGO NAPOLEÃO | PIAUÍ | Brasil | 2204600 | 22 | 33 | nan | nan | nan | Caatinga | 2.1 |
| 2e7a8478-5a0d-3ad4-831e-7e64be81f323 | -4.25701 | -48.5536 | 2025-10-02 04:49:00 | NOAA-20 | RONDON DO PARÁ | PARÁ | Brasil | 1506187 | 15 | 33 | nan | nan | nan | Amazônia | 1.8 |
| 3f5beeb1-2f41-3feb-81ea-c693a067f00f | -8.81755 | -46.68367 | 2025-10-02 04:49:00 | NOAA-20 | BALSAS | MARANHÃO | Brasil | 2101400 | 21 | 33 | nan | nan | nan | Cerrado | 20.4 |
| 37d909eb-0858-3193-b50f-c022936e363b | -8.5136 | -47.79969 | 2025-10-02 04:49:00 | NOAA-20 | ITACAJÁ | TOCANTINS | Brasil | 1710508 | 17 | 33 | nan | nan | nan | Cerrado | 2.0 |
| 85ca6f2d-dd9b-3eb3-bc50-f252bb212386 | -3.69514 | -49.56727 | 2025-10-02 04:49:00 | NOAA-20 | BREU BRANCO | PARÁ | Brasil | 1501782 | 15 | 33 | nan | nan | nan | Amazônia | 3.8 |
| 44e4cd83-93cd-357c-b0a7-5c15ce82c45e | -9.33208 | -45.71529 | 2025-10-02 04:49:00 | NOAA-20 | SANTA FILOMENA | PIAUÍ | Brasil | 2209203 | 22 | 33 | nan | nan | nan | Cerrado | 4.9 |
| 1864ffcc-afc1-32c6-b584-6f1cdf0df1ba | -5.48289 | -42.76553 | 2025-10-02 04:49:00 | NOAA-20 | TERESINA | PIAUÍ | Brasil | 2211001 | 22 | 33 | nan | nan | nan | Caatinga | 1.0 |
| aa01d9b8-3a63-3bf9-b2a6-458052af78b7 | -2.18486 | -51.37658 | 2025-10-02 04:49:00 | NOAA-20 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 1.5 |
| ad29846b-5498-3112-8fc8-05637618385a | -6.95554 | -45.32354 | 2025-10-02 04:49:00 | NOAA-20 | SAMBAÍBA | MARANHÃO | Brasil | 2109700 | 21 | 33 | nan | nan | nan | Cerrado | 31.1 |
| d737358e-ba02-3f06-9ee5-0c9fcf13e69f | -6.05057 | -42.43923 | 2025-10-02 04:49:00 | NOAA-20 | HUGO NAPOLEÃO | PIAUÍ | Brasil | 2204600 | 22 | 33 | nan | nan | nan | Caatinga | 2.1 |
| b667940a-101c-3d1e-82f3-fb8927ec3f1f | -6.67069 | -42.79401 | 2025-10-02 04:49:00 | NOAA-20 | FRANCISCO AYRES | PIAUÍ | Brasil | 2204105 | 22 | 33 | nan | nan | nan | Caatinga | 4.7 |
| d152b98c-956e-3081-81a4-175302c16984 | -2.63416 | -48.03944 | 2025-10-02 04:49:00 | NOAA-20 | TOMÉ-AÇU | PARÁ | Brasil | 1508001 | 15 | 33 | nan | nan | nan | Amazônia | 0.8 |
| 2baf1234-2289-3094-b44a-9a8e4934c63d | -3.35234 | -43.19623 | 2025-10-02 04:49:00 | NOAA-20 | URBANO SANTOS | MARANHÃO | Brasil | 2112605 | 21 | 33 | nan | nan | nan | Cerrado | 6.0 |
| d5700a33-7ef1-3e72-9c3e-012a10ecc6d9 | -8.65646 | -47.09184 | 2025-10-02 04:49:00 | NOAA-20 | RECURSOLÂNDIA | TOCANTINS | Brasil | 1718501 | 17 | 33 | nan | nan | nan | Cerrado | 2.0 |
| 7e3276f0-15b7-3c5a-8f72-6f13199892af | -5.78951 | -44.69758 | 2025-10-02 04:49:00 | NOAA-20 | TUNTUM | MARANHÃO | Brasil | 2112308 | 21 | 33 | nan | nan | nan | Cerrado | 3.2 |
| 51c669a0-4e57-39c7-8f8a-5047ad4e2fa9 | -8.50852 | -44.70277 | 2025-10-02 04:49:00 | NOAA-20 | PALMEIRA DO PIAUÍ | PIAUÍ | Brasil | 2207405 | 22 | 33 | nan | nan | nan | Cerrado | 0.7 |
| 1cba0f03-5375-3bf7-bf4e-dc11340fc3a5 | -6.96096 | -45.31921 | 2025-10-02 04:49:00 | NOAA-20 | SAMBAÍBA | MARANHÃO | Brasil | 2109700 | 21 | 33 | nan | nan | nan | Cerrado | 1.5 |
| dced8373-3c24-3129-88ce-f823dc8d5047 | -7.40873 | -45.19172 | 2025-10-02 04:49:00 | NOAA-20 | LORETO | MARANHÃO | Brasil | 2106102 | 21 | 33 | nan | nan | nan | Cerrado | 9.0 |
| 4e949651-39a6-3fc3-90a8-4d0a03e065fb | -6.69547 | -42.81994 | 2025-10-02 04:49:00 | NOAA-20 | FRANCISCO AYRES | PIAUÍ | Brasil | 2204105 | 22 | 33 | nan | nan | nan | Caatinga | 3.5 |
| 6de6160e-f189-3393-abae-aabcc01a14b7 | -7.55057 | -42.64189 | 2025-10-02 04:49:00 | NOAA-20 | SÃO JOSÉ DO PEIXE | PIAUÍ | Brasil | 2210102 | 22 | 33 | nan | nan | nan | Caatinga | 1.2 |
| f6e6c0a2-8ba6-3100-87c3-3ff5ecb07b03 | -9.33482 | -45.6958 | 2025-10-02 04:49:00 | NOAA-20 | SANTA FILOMENA | PIAUÍ | Brasil | 2209203 | 22 | 33 | nan | nan | nan | Cerrado | 4.0 |
| 9e4a8e08-4431-3fad-9f27-916c70d31643 | -8.57469 | -44.66444 | 2025-10-02 04:49:00 | NOAA-20 | CURRAIS | PIAUÍ | Brasil | 2203230 | 22 | 33 | nan | nan | nan | Cerrado | 0.4 |
| eba24e6a-02f3-3935-be32-97fe5e9780a4 | -3.94179 | -50.82864 | 2025-10-02 04:49:00 | NOAA-20 | NOVO REPARTIMENTO | PARÁ | Brasil | 1505064 | 15 | 33 | nan | nan | nan | Amazônia | 0.6 |
| 960e744b-9352-333b-bad5-b8c56d447c03 | -8.90037 | -45.03926 | 2025-10-02 04:49:00 | NOAA-20 | BAIXA GRANDE DO RIBEIRO | PIAUÍ | Brasil | 2201150 | 22 | 33 | nan | nan | nan | Cerrado | 2.0 |
| 36825b86-4036-3a30-a517-58ffadfb4232 | -5.19114 | -45.3957 | 2025-10-02 04:49:00 | NOAA-20 | JENIPAPO DOS VIEIRAS | MARANHÃO | Brasil | 2105476 | 21 | 33 | nan | nan | nan | Cerrado | 3.4 |
| 75593966-413e-3b33-937c-b2b617c5647f | -5.40565 | -41.33384 | 2025-10-02 04:49:00 | NOAA-20 | CASTELO DO PIAUÍ | PIAUÍ | Brasil | 2202604 | 22 | 33 | nan | nan | nan | Caatinga | 3.1 |
| 7ef2adaf-18a0-3d17-91ba-cce12458706b | -7.3103 | -42.88293 | 2025-10-02 04:49:00 | NOAA-20 | FLORIANO | PIAUÍ | Brasil | 2203909 | 22 | 33 | nan | nan | nan | Caatinga | 1.0 |
| 4d387690-87ca-34ed-bd65-b66328c118f3 | -6.54521 | -43.92345 | 2025-10-02 04:49:00 | NOAA-20 | PASTOS BONS | MARANHÃO | Brasil | 2108009 | 21 | 33 | nan | nan | nan | Cerrado | 2.2 |
| c10b36ce-96fd-38c8-b452-effc44aec28e | -3.47065 | -50.02425 | 2025-10-02 04:49:00 | NOAA-20 | PACAJÁ | PARÁ | Brasil | 1505486 | 15 | 33 | nan | nan | nan | Amazônia | 1.1 |
| aac790d7-8e49-3a48-8abf-87f602a2d0cf | -5.17358 | -45.38821 | 2025-10-02 04:49:00 | NOAA-20 | JENIPAPO DOS VIEIRAS | MARANHÃO | Brasil | 2105476 | 21 | 33 | nan | nan | nan | Cerrado | 0.9 |
| 05c08c98-730b-3f70-b57f-411a827bb98c | -4.05229 | -49.07813 | 2025-10-02 04:49:00 | NOAA-20 | BREU BRANCO | PARÁ | Brasil | 1501782 | 15 | 33 | nan | nan | nan | Amazônia | 2.1 |
| 126871f0-4eee-3e9a-96dd-f0934603354b | -6.77411 | -45.58359 | 2025-10-02 04:49:00 | NOAA-20 | MIRADOR | MARANHÃO | Brasil | 2106706 | 21 | 33 | nan | nan | nan | Cerrado | 3.4 |
| 855f38ce-9734-3e16-b90e-271a26c91925 | -2.74078 | -48.67599 | 2025-10-02 04:49:00 | NOAA-20 | TAILÂNDIA | PARÁ | Brasil | 1507953 | 15 | 33 | nan | nan | nan | Amazônia | 1.0 |
| d27cccb7-cf19-3c46-9f3c-1121c0a72395 | -5.63483 | -45.96439 | 2025-10-02 04:49:00 | NOAA-20 | GRAJAÚ | MARANHÃO | Brasil | 2104800 | 21 | 33 | nan | nan | nan | Cerrado | 1.3 |
| dc6c3024-ae65-38ad-8873-021c9e9ec126 | -7.77155 | -42.53965 | 2025-10-02 04:49:00 | NOAA-20 | SÃO JOSÉ DO PEIXE | PIAUÍ | Brasil | 2210102 | 22 | 33 | nan | nan | nan | Caatinga | 11.1 |
| 17c2ccb7-67be-30e7-84ad-67542945f7ef | -6.96693 | -45.34477 | 2025-10-02 04:49:00 | NOAA-20 | SAMBAÍBA | MARANHÃO | Brasil | 2109700 | 21 | 33 | nan | nan | nan | Cerrado | 2.4 |
| 14246aa0-07f3-3547-b444-335185a93587 | -2.92353 | -48.29991 | 2025-10-02 04:49:00 | NOAA-20 | TOMÉ-AÇU | PARÁ | Brasil | 1508001 | 15 | 33 | nan | nan | nan | Amazônia | 8.2 |
| 305cdb1b-ff38-3013-abc4-be1dafb574c8 | -5.98399 | -44.56351 | 2025-10-02 04:49:00 | NOAA-20 | COLINAS | MARANHÃO | Brasil | 2103505 | 21 | 33 | nan | nan | nan | Cerrado | 2.8 |
| 3a0988c2-3a9d-30ac-a6cb-368df169fec2 | -4.25635 | -48.55786 | 2025-10-02 04:49:00 | NOAA-20 | RONDON DO PARÁ | PARÁ | Brasil | 1506187 | 15 | 33 | nan | nan | nan | Amazônia | 1.8 |
| 4188b260-6beb-3720-9f3e-37694bec6f3d | -6.10834 | -41.79602 | 2025-10-02 04:49:00 | NOAA-20 | AROAZES | PIAUÍ | Brasil | 2200905 | 22 | 33 | nan | nan | nan | Caatinga | 1.4 |
| c1a5f70a-889e-3863-88c1-16608d2f8ad2 | -7.77498 | -45.71273 | 2025-10-02 04:49:00 | NOAA-20 | SAMBAÍBA | MARANHÃO | Brasil | 2109700 | 21 | 33 | nan | nan | nan | Cerrado | 2.4 |
| 3bf2783a-b249-3bde-811a-6dbdfc4b018c | -6.2754 | -44.05663 | 2025-10-02 04:49:00 | NOAA-20 | COLINAS | MARANHÃO | Brasil | 2103505 | 21 | 33 | nan | nan | nan | Cerrado | 1.8 |
| faaace07-1b97-33cf-8093-c415526f7d44 | -8.81192 | -46.69181 | 2025-10-02 04:49:00 | NOAA-20 | BALSAS | MARANHÃO | Brasil | 2101400 | 21 | 33 | nan | nan | nan | Cerrado | 20.7 |
| bba8918d-0e8d-3fc2-85b0-d49b47748bad | -8.74594 | -47.34234 | 2025-10-02 04:49:00 | NOAA-20 | ITACAJÁ | TOCANTINS | Brasil | 1710508 | 17 | 33 | nan | nan | nan | Cerrado | 7.1 |
| 09cd2d82-c362-3dbf-b113-1c91927a2e97 | -3.65194 | -51.22812 | 2025-10-02 04:49:00 | NOAA-20 | ANAPU | PARÁ | Brasil | 1500859 | 15 | 33 | nan | nan | nan | Amazônia | 0.6 |
| c57aca10-a5b1-3bbe-a37e-21ba42051deb | -8.41722 | -47.74846 | 2025-10-02 04:49:00 | NOAA-20 | ITACAJÁ | TOCANTINS | Brasil | 1710508 | 17 | 33 | nan | nan | nan | Cerrado | 1.9 |
| 997c7916-dccf-3467-835f-5430f8731c85 | -5.17813 | -45.38895 | 2025-10-02 04:49:00 | NOAA-20 | JENIPAPO DOS VIEIRAS | MARANHÃO | Brasil | 2105476 | 21 | 33 | nan | nan | nan | Cerrado | 0.9 |
| 1cec7d35-18d3-3c79-ade2-0bcda25a1161 | -5.82908 | -42.86125 | 2025-10-02 04:49:00 | NOAA-20 | SÃO PEDRO DO PIAUÍ | PIAUÍ | Brasil | 2210508 | 22 | 33 | nan | nan | nan | Caatinga | 4.0 |
| c715b59d-9923-3470-a8c7-75e446688192 | -8.57484 | -49.60116 | 2025-10-02 04:49:00 | NOAA-20 | CONCEIÇÃO DO ARAGUAIA | PARÁ | Brasil | 1502707 | 15 | 33 | nan | nan | nan | Amazônia | 3.5 |
| 86fb8581-2d20-3343-8647-16b92c9e427a | -6.26988 | -44.05902 | 2025-10-02 04:49:00 | NOAA-20 | COLINAS | MARANHÃO | Brasil | 2103505 | 21 | 33 | nan | nan | nan | Cerrado | 1.8 |
| 5083caf9-3032-3ba4-8604-9b106f26d625 | -2.63349 | -48.04381 | 2025-10-02 04:49:00 | NOAA-20 | TOMÉ-AÇU | PARÁ | Brasil | 1508001 | 15 | 33 | nan | nan | nan | Amazônia | 0.8 |
| fb67ad51-ad64-3065-ad85-6ec0798aba94 | -6.38589 | -43.8843 | 2025-10-02 04:49:00 | NOAA-20 | PARAIBANO | MARANHÃO | Brasil | 2107704 | 21 | 33 | nan | nan | nan | Cerrado | 3.8 |
| 1ef2a817-9e30-3dbd-833e-ce524dc4fd3b | -4.40454 | -50.84566 | 2025-10-02 04:49:00 | NOAA-20 | NOVO REPARTIMENTO | PARÁ | Brasil | 1505064 | 15 | 33 | nan | nan | nan | Amazônia | 0.8 |


[Clique aqui para ver as próximas entradas](README108.md)
