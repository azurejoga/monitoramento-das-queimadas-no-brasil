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

## Dados Diários - Página 103

| ID | Latitude | Longitude | Data/Hora GMT | Satélite | Município | Estado | País | Município ID | Estado ID | País ID | Dias sem Chuva | Precipitação | Risco de Fogo | Bioma | FRP |
|----|----------|-----------|---------------|----------|-----------|--------|------|--------------|-----------|---------|----------------|--------------|----------------|-------|-----|
| 2ec521cc-88a7-3963-8790-174aec8baa27 | -10.59369 | -48.71386 | 2025-10-03 04:32:00 | NOAA-20 | PORTO NACIONAL | TOCANTINS | Brasil | 1718204 | 17 | 33 | nan | nan | nan | Cerrado | 4.8 |
| 6bcfbb7d-5836-3da3-b18e-4327c2b48998 | -6.03666 | -52.4219 | 2025-10-03 04:32:00 | NOAA-20 | SÃO FÉLIX DO XINGU | PARÁ | Brasil | 1507300 | 15 | 33 | nan | nan | nan | Amazônia | 1.0 |
| c6ab6db3-d9ab-32a2-aa43-477b22862201 | -4.66734 | -45.80659 | 2025-10-03 04:32:00 | NOAA-20 | MARAJÁ DO SENA | MARANHÃO | Brasil | 2106359 | 21 | 33 | nan | nan | nan | Amazônia | 1.9 |
| 58fc1091-f5f4-36de-ab06-1d1ba8fad5fb | -11.07045 | -48.35941 | 2025-10-03 04:32:00 | NOAA-20 | IPUEIRAS | TOCANTINS | Brasil | 1709807 | 17 | 33 | nan | nan | nan | Cerrado | 1.7 |
| 7b2d3a78-9715-385c-8dd7-75dee4643599 | -11.77832 | -46.82348 | 2025-10-03 04:32:00 | NOAA-20 | DIANÓPOLIS | TOCANTINS | Brasil | 1707009 | 17 | 33 | nan | nan | nan | Cerrado | 1.0 |
| a4c6b52a-c817-3144-b2c9-5e2e7f7d809c | -11.53812 | -49.82101 | 2025-10-03 04:32:00 | NOAA-20 | FORMOSO DO ARAGUAIA | TOCANTINS | Brasil | 1708205 | 17 | 33 | nan | nan | nan | Cerrado | 2.6 |
| 07f0d4f6-93a8-3df9-a7f4-87ea7b32b863 | -7.75684 | -46.25502 | 2025-10-03 04:32:00 | NOAA-20 | BALSAS | MARANHÃO | Brasil | 2101400 | 21 | 33 | nan | nan | nan | Cerrado | 28.0 |
| 9310fa3a-8da4-3a51-ab3c-254995293359 | -6.34999 | -43.95702 | 2025-10-03 04:32:00 | NOAA-20 | PARAIBANO | MARANHÃO | Brasil | 2107704 | 21 | 33 | nan | nan | nan | Cerrado | 1.4 |
| 430a17e4-7275-3f96-a23c-dd2d3b342a44 | -11.90522 | -46.3023 | 2025-10-03 04:32:00 | NOAA-20 | PONTE ALTA DO BOM JESUS | TOCANTINS | Brasil | 1717800 | 17 | 33 | nan | nan | nan | Cerrado | 2.4 |
| 1c802027-632f-35cb-84fc-19f7a8b5970f | -8.1798 | -47.01591 | 2025-10-03 04:32:00 | NOAA-20 | CAMPOS LINDOS | TOCANTINS | Brasil | 1703842 | 17 | 33 | nan | nan | nan | Cerrado | 1.8 |
| f71c50df-e0e2-3567-81fe-d7c991622ce0 | -9.90731 | -43.72538 | 2025-10-03 04:32:00 | NOAA-20 | MORRO CABEÇA NO TEMPO | PIAUÍ | Brasil | 2206654 | 22 | 33 | nan | nan | nan | Caatinga | 18.5 |
| 8a7e7d47-e446-391d-813f-07eae301e510 | -10.89433 | -46.70478 | 2025-10-03 04:32:00 | NOAA-20 | MATEIROS | TOCANTINS | Brasil | 1712702 | 17 | 33 | nan | nan | nan | Cerrado | 0.8 |
| 81ec2426-f0de-3d9a-bf47-1ca005a6ebb2 | -9.44558 | -47.3683 | 2025-10-03 04:32:00 | NOAA-20 | RIO SONO | TOCANTINS | Brasil | 1718758 | 17 | 33 | nan | nan | nan | Cerrado | 1.6 |
| 49a6011c-74eb-3ee9-8123-c68833f46eb6 | -5.626 | -43.9184 | 2025-10-03 04:32:00 | NOAA-20 | FORTUNA | MARANHÃO | Brasil | 2104206 | 21 | 33 | nan | nan | nan | Cerrado | 1.9 |
| 85b1b14d-aa3c-32cf-a410-13481a5f53ca | -9.00178 | -47.4736 | 2025-10-03 04:32:00 | NOAA-20 | CENTENÁRIO | TOCANTINS | Brasil | 1704105 | 17 | 33 | nan | nan | nan | Cerrado | 0.8 |
| 37504a86-8c1b-30c2-b062-4bc3c74e7d48 | -5.22162 | -44.49391 | 2025-10-03 04:32:00 | NOAA-20 | PRESIDENTE DUTRA | MARANHÃO | Brasil | 2109106 | 21 | 33 | nan | nan | nan | Cerrado | 1.3 |
| 1c45c0e7-c767-3b8c-942a-672c9e8fda0c | -5.83203 | -53.666 | 2025-10-03 04:32:00 | NOAA-20 | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 1.2 |
| 2694d758-28c0-3f80-b8f4-a0aac0042060 | -6.7573 | -44.81107 | 2025-10-03 04:32:00 | NOAA-20 | SÃO FÉLIX DE BALSAS | MARANHÃO | Brasil | 2110807 | 21 | 33 | nan | nan | nan | Cerrado | 1.1 |
| e70cac5d-d874-335c-b124-340b1770c977 | -5.71726 | -49.25619 | 2025-10-03 04:32:00 | NOAA-20 | MARABÁ | PARÁ | Brasil | 1504208 | 15 | 33 | nan | nan | nan | Amazônia | 0.6 |
| 21db9c9c-ff95-3bd3-932d-5016ffb66478 | -6.3376 | -43.0359 | 2025-10-03 04:32:00 | NOAA-20 | SÃO FRANCISCO DO MARANHÃO | MARANHÃO | Brasil | 2110906 | 21 | 33 | nan | nan | nan | Cerrado | 2.3 |
| 98996f22-f731-3475-8d6a-047c45651ee1 | -7.74717 | -46.24979 | 2025-10-03 04:32:00 | NOAA-20 | BALSAS | MARANHÃO | Brasil | 2101400 | 21 | 33 | nan | nan | nan | Cerrado | 1.2 |
| 0d18f6a5-f84e-30a2-a6c9-5451fcc5911d | -4.89636 | -45.72944 | 2025-10-03 04:32:00 | NOAA-20 | ARAME | MARANHÃO | Brasil | 2100956 | 21 | 33 | nan | nan | nan | Amazônia | 3.0 |
| fd53d2a9-a3d4-39de-9199-a8b10e150788 | -5.78155 | -51.74344 | 2025-10-03 04:32:00 | NOAA-20 | SÃO FÉLIX DO XINGU | PARÁ | Brasil | 1507300 | 15 | 33 | nan | nan | nan | Amazônia | 0.6 |
| 921fb913-8994-34e6-b7c2-27c6d05abd9a | -10.94059 | -46.49273 | 2025-10-03 04:32:00 | NOAA-20 | MATEIROS | TOCANTINS | Brasil | 1712702 | 17 | 33 | nan | nan | nan | Cerrado | 1.0 |
| 0381d20e-de1a-3dd3-8526-a38b6eb6c96d | -8.25145 | -50.09284 | 2025-10-03 04:32:00 | NOAA-20 | REDENÇÃO | PARÁ | Brasil | 1506138 | 15 | 33 | nan | nan | nan | Amazônia | 0.5 |
| ca4bde28-7205-30a5-9082-e49446da7be8 | -8.90089 | -46.60431 | 2025-10-03 04:32:00 | NOAA-20 | BALSAS | MARANHÃO | Brasil | 2101400 | 21 | 33 | nan | nan | nan | Cerrado | 1.4 |
| 1afd9351-8e73-3297-8ca7-ebe69e559a09 | -8.53736 | -47.27425 | 2025-10-03 04:32:00 | NOAA-20 | ITACAJÁ | TOCANTINS | Brasil | 1710508 | 17 | 33 | nan | nan | nan | Cerrado | 0.8 |
| e4e9bd3b-35ae-3b8d-9394-dc54366dcadc | -7.05404 | -43.22866 | 2025-10-03 04:32:00 | NOAA-20 | FLORIANO | PIAUÍ | Brasil | 2203909 | 22 | 33 | nan | nan | nan | Caatinga | 1.9 |
| 500d165f-2b4d-3c78-9f20-b95d4cf0f422 | -6.8519 | -44.78234 | 2025-10-03 04:32:00 | NOAA-20 | SÃO FÉLIX DE BALSAS | MARANHÃO | Brasil | 2110807 | 21 | 33 | nan | nan | nan | Cerrado | 2.0 |
| d6960588-e819-3706-a6de-df8a51f16008 | -6.04058 | -44.63076 | 2025-10-03 04:32:00 | NOAA-20 | MIRADOR | MARANHÃO | Brasil | 2106706 | 21 | 33 | nan | nan | nan | Cerrado | 4.3 |
| af55afec-199e-35ff-a0f0-1bcdbd7bcf08 | -9.9494 | -43.73354 | 2025-10-03 04:32:00 | NOAA-20 | MORRO CABEÇA NO TEMPO | PIAUÍ | Brasil | 2206654 | 22 | 33 | nan | nan | nan | Caatinga | 3.8 |
| 700548bd-7ea7-3236-8458-2fdb418eea91 | -10.94243 | -46.70777 | 2025-10-03 04:32:00 | NOAA-20 | MATEIROS | TOCANTINS | Brasil | 1712702 | 17 | 33 | nan | nan | nan | Cerrado | 0.7 |
| a1f7a0e0-f99e-30a9-b78c-4838263b8756 | -11.55601 | -47.65205 | 2025-10-03 04:32:00 | NOAA-20 | NATIVIDADE | TOCANTINS | Brasil | 1714203 | 17 | 33 | nan | nan | nan | Cerrado | 1.2 |
| 6c4bbf21-f69c-3299-a6d4-7ed0947bc51e | -10.88803 | -46.7232 | 2025-10-03 04:32:00 | NOAA-20 | MATEIROS | TOCANTINS | Brasil | 1712702 | 17 | 33 | nan | nan | nan | Cerrado | 35.0 |
| 20ac6ec4-6b17-32e8-ad35-50255b0d0c2a | -11.86811 | -44.98838 | 2025-10-03 04:32:00 | NOAA-20 | RIACHÃO DAS NEVES | BAHIA | Brasil | 2926202 | 29 | 33 | nan | nan | nan | Cerrado | 1.6 |
| aa6c14d9-1288-3e93-ae26-38b65dbdbe05 | -10.87909 | -53.77283 | 2025-10-03 04:32:00 | NOAA-20 | MARCELÂNDIA | MATO GROSSO | Brasil | 5105580 | 51 | 33 | nan | nan | nan | Amazônia | 1.0 |
| e1ffa6e9-deae-3a5c-874d-5dcd4b363abf | -6.03546 | -44.62868 | 2025-10-03 04:32:00 | NOAA-20 | MIRADOR | MARANHÃO | Brasil | 2106706 | 21 | 33 | nan | nan | nan | Cerrado | 6.3 |
| ed79c7c7-73eb-3bdf-b09d-e1fdc9e4f04e | -11.85933 | -44.9688 | 2025-10-03 04:32:00 | NOAA-20 | RIACHÃO DAS NEVES | BAHIA | Brasil | 2926202 | 29 | 33 | nan | nan | nan | Cerrado | 3.0 |
| 2ba015a6-1a73-3394-8f47-71be9ba3d100 | -10.34201 | -43.73425 | 2025-10-03 04:32:00 | NOAA-20 | PILÃO ARCADO | BAHIA | Brasil | 2924405 | 29 | 33 | nan | nan | nan | Cerrado | 1.6 |
| 0ae65628-8315-3a62-a543-35e0f1007c3b | -11.14091 | -47.20004 | 2025-10-03 04:32:00 | NOAA-20 | ALMAS | TOCANTINS | Brasil | 1700400 | 17 | 33 | nan | nan | nan | Cerrado | 1.5 |
| 8342cf17-6202-3d52-9ac2-303fdc5f39a1 | -10.63254 | -49.15441 | 2025-10-03 04:32:00 | NOAA-20 | CRISTALÂNDIA | TOCANTINS | Brasil | 1706100 | 17 | 33 | nan | nan | nan | Cerrado | 2.7 |
| e9842363-96d5-3d33-8729-ce72d9a180eb | -10.92815 | -46.73275 | 2025-10-03 04:32:00 | NOAA-20 | MATEIROS | TOCANTINS | Brasil | 1712702 | 17 | 33 | nan | nan | nan | Cerrado | 1.7 |
| 9e1a6638-034a-3d9a-9a93-b03af1fe4d44 | -10.4133 | -54.40869 | 2025-10-03 04:32:00 | NOAA-20 | PEIXOTO DE AZEVEDO | MATO GROSSO | Brasil | 5106422 | 51 | 33 | nan | nan | nan | Amazônia | 2.5 |
| 2d3b64d5-2b3d-3d0f-8481-44a1eba8f1b5 | -11.14288 | -43.38168 | 2025-10-03 04:32:00 | NOAA-20 | BARRA | BAHIA | Brasil | 2902708 | 29 | 33 | nan | nan | nan | Caatinga | 1.9 |
| ea66c67d-630f-3b5c-a717-6a717ce3f49c | -5.85538 | -43.36654 | 2025-10-03 04:32:00 | NOAA-20 | PARNARAMA | MARANHÃO | Brasil | 2107803 | 21 | 33 | nan | nan | nan | Cerrado | 1.4 |
| c0c39886-4d0d-3c30-8eed-9513b059ce03 | -10.90465 | -46.70638 | 2025-10-03 04:32:00 | NOAA-20 | MATEIROS | TOCANTINS | Brasil | 1712702 | 17 | 33 | nan | nan | nan | Cerrado | 0.7 |
| c5e27b13-da9d-32b0-a86e-b0384edb2663 | -6.02983 | -44.62909 | 2025-10-03 04:32:00 | NOAA-20 | MIRADOR | MARANHÃO | Brasil | 2106706 | 21 | 33 | nan | nan | nan | Cerrado | 10.2 |
| f4741464-cba7-397f-89a7-4e771368e9c3 | -9.95149 | -43.70035 | 2025-10-03 04:32:00 | NOAA-20 | MORRO CABEÇA NO TEMPO | PIAUÍ | Brasil | 2206654 | 22 | 33 | nan | nan | nan | Cerrado | 1.0 |
| 582d490d-5beb-30e6-846d-1362086a8610 | -8.71229 | -47.98006 | 2025-10-03 04:32:00 | NOAA-20 | SANTA MARIA DO TOCANTINS | TOCANTINS | Brasil | 1718881 | 17 | 33 | nan | nan | nan | Cerrado | 3.6 |
| fd3924bd-88e7-3957-b147-a7f74312a231 | -7.84969 | -45.27945 | 2025-10-03 04:32:00 | NOAA-20 | RIBEIRO GONÇALVES | PIAUÍ | Brasil | 2208908 | 22 | 33 | nan | nan | nan | Cerrado | 0.3 |
| 65c35340-0b76-38a5-bb94-1179c5a5ca7d | -10.59644 | -48.71788 | 2025-10-03 04:32:00 | NOAA-20 | PORTO NACIONAL | TOCANTINS | Brasil | 1718204 | 17 | 33 | nan | nan | nan | Cerrado | 2.2 |
| 5adf6c1a-69f4-3906-bf66-943f6b419f02 | -9.8976 | -43.70826 | 2025-10-03 04:32:00 | NOAA-20 | MORRO CABEÇA NO TEMPO | PIAUÍ | Brasil | 2206654 | 22 | 33 | nan | nan | nan | Caatinga | 1.2 |
| c210e438-666a-3d20-9060-0c7c575c9053 | -8.4792 | -44.59442 | 2025-10-03 04:32:00 | NOAA-20 | PALMEIRA DO PIAUÍ | PIAUÍ | Brasil | 2207405 | 22 | 33 | nan | nan | nan | Cerrado | 2.2 |
| 157399bc-c284-3ca2-b8df-0e7440a61343 | -6.99182 | -44.19864 | 2025-10-03 04:32:00 | NOAA-20 | PORTO ALEGRE DO PIAUÍ | PIAUÍ | Brasil | 2208551 | 22 | 33 | nan | nan | nan | Cerrado | 1.9 |
| 89334cda-d6a3-35c1-85f7-05404d65a59d | -11.07631 | -47.71012 | 2025-10-03 04:32:00 | NOAA-20 | PINDORAMA DO TOCANTINS | TOCANTINS | Brasil | 1717008 | 17 | 33 | nan | nan | nan | Cerrado | 1.0 |
| 0ab7ed59-a1a4-3dfb-b232-befceb1c0d37 | -7.77325 | -47.38515 | 2025-10-03 04:32:00 | NOAA-20 | GOIATINS | TOCANTINS | Brasil | 1709005 | 17 | 33 | nan | nan | nan | Cerrado | 1.4 |
| 2f39e856-e975-37ba-a73f-b03ee8f28ed3 | -5.78365 | -45.74262 | 2025-10-03 04:32:00 | NOAA-20 | GRAJAÚ | MARANHÃO | Brasil | 2104800 | 21 | 33 | nan | nan | nan | Cerrado | 1.2 |
| 358c2329-4b6d-3a03-9eb6-6ae4b08d647d | -10.59975 | -48.71842 | 2025-10-03 04:32:00 | NOAA-20 | PORTO NACIONAL | TOCANTINS | Brasil | 1718204 | 17 | 33 | nan | nan | nan | Cerrado | 3.8 |
| c2f71897-d4e6-32e4-b7a0-5bcaa442ea80 | -11.59066 | -47.62788 | 2025-10-03 04:32:00 | NOAA-20 | NATIVIDADE | TOCANTINS | Brasil | 1714203 | 17 | 33 | nan | nan | nan | Cerrado | 1.7 |
| 6d24ff4e-0190-3979-a611-d0b9af30a741 | -5.78613 | -47.06314 | 2025-10-03 04:32:00 | NOAA-20 | MONTES ALTOS | MARANHÃO | Brasil | 2107001 | 21 | 33 | nan | nan | nan | Cerrado | 1.5 |
| aba58ecc-9205-3f3d-a3be-784a34b1a037 | -10.95161 | -46.71697 | 2025-10-03 04:32:00 | NOAA-20 | MATEIROS | TOCANTINS | Brasil | 1712702 | 17 | 33 | nan | nan | nan | Cerrado | 0.7 |
| 41fec6f3-65ab-32a9-9a67-7037c0773610 | -4.57361 | -46.49978 | 2025-10-03 04:32:00 | NOAA-20 | BOM JESUS DAS SELVAS | MARANHÃO | Brasil | 2102036 | 21 | 33 | nan | nan | nan | Amazônia | 3.3 |
| e74a87b4-6ca8-3778-9e32-13c809591734 | -11.13099 | -43.37631 | 2025-10-03 04:32:00 | NOAA-20 | BARRA | BAHIA | Brasil | 2902708 | 29 | 33 | nan | nan | nan | Caatinga | 3.0 |
| 7c60eda8-48a0-3521-80d6-0ac29cd5b5b4 | -8.58887 | -44.78776 | 2025-10-03 04:32:00 | NOAA-20 | CURRAIS | PIAUÍ | Brasil | 2203230 | 22 | 33 | nan | nan | nan | Cerrado | 9.0 |
| 1b2deb09-d413-3774-b78b-652253e52fd3 | -6.23146 | -44.24053 | 2025-10-03 04:32:00 | NOAA-20 | MIRADOR | MARANHÃO | Brasil | 2106706 | 21 | 33 | nan | nan | nan | Cerrado | 2.0 |
| 1e7e8e8f-56c9-3e7e-b65e-db0e3947d551 | -6.6766 | -42.82727 | 2025-10-03 04:32:00 | NOAA-20 | FRANCISCO AYRES | PIAUÍ | Brasil | 2204105 | 22 | 33 | nan | nan | nan | Caatinga | 1.4 |
| 79823ee1-0f8c-3438-955e-92f99cd74a81 | -7.46436 | -47.01331 | 2025-10-03 04:32:00 | NOAA-20 | RIACHÃO | MARANHÃO | Brasil | 2109502 | 21 | 33 | nan | nan | nan | Cerrado | 1.1 |
| 98e898f1-6776-3b4e-b4dc-25e621aa7101 | -10.88907 | -44.27407 | 2025-10-03 04:32:00 | NOAA-20 | SANTA RITA DE CÁSSIA | BAHIA | Brasil | 2928406 | 29 | 33 | nan | nan | nan | Cerrado | 0.8 |
| 0e51e116-0f8c-3d2b-8552-4da5efa9bf22 | -6.05225 | -44.61454 | 2025-10-03 04:32:00 | NOAA-20 | MIRADOR | MARANHÃO | Brasil | 2106706 | 21 | 33 | nan | nan | nan | Cerrado | 5.9 |
| c5ec3bb2-b921-376a-9ec7-f79d6407ea1b | -9.04033 | -46.67437 | 2025-10-03 04:32:00 | NOAA-20 | BALSAS | MARANHÃO | Brasil | 2101400 | 21 | 33 | nan | nan | nan | Cerrado | 2.4 |
| 0218711d-c29d-3853-9d30-32dbfb7a65c7 | -9.02905 | -46.68003 | 2025-10-03 04:32:00 | NOAA-20 | BALSAS | MARANHÃO | Brasil | 2101400 | 21 | 33 | nan | nan | nan | Cerrado | 0.8 |
| 8a569265-802a-3330-a16b-cdbf65e71ae6 | -10.95218 | -46.71316 | 2025-10-03 04:32:00 | NOAA-20 | MATEIROS | TOCANTINS | Brasil | 1712702 | 17 | 33 | nan | nan | nan | Cerrado | 0.7 |
| dc24dac5-e4f4-364b-9696-2020abcd9eee | -10.84329 | -53.78107 | 2025-10-03 04:32:00 | NOAA-20 | MARCELÂNDIA | MATO GROSSO | Brasil | 5105580 | 51 | 33 | nan | nan | nan | Amazônia | 1.3 |
| b492c9d0-2110-3796-939a-51cf5a11ddb7 | -10.58707 | -48.71279 | 2025-10-03 04:32:00 | NOAA-20 | PORTO NACIONAL | TOCANTINS | Brasil | 1718204 | 17 | 33 | nan | nan | nan | Cerrado | 9.2 |
| c7b764ce-756a-359f-b761-eb1aceeb2fb4 | -7.74321 | -46.25294 | 2025-10-03 04:32:00 | NOAA-20 | BALSAS | MARANHÃO | Brasil | 2101400 | 21 | 33 | nan | nan | nan | Cerrado | 1.2 |
| 82ebeabd-b9b0-3180-ab92-14a404199e95 | -11.55583 | -47.00311 | 2025-10-03 04:32:00 | NOAA-20 | DIANÓPOLIS | TOCANTINS | Brasil | 1707009 | 17 | 33 | nan | nan | nan | Cerrado | 1.1 |
| 8a35f0cb-70a0-3b5f-ab0c-5b8fed067a50 | -10.20739 | -48.18981 | 2025-10-03 04:32:00 | NOAA-20 | PALMAS | TOCANTINS | Brasil | 1721000 | 17 | 33 | nan | nan | nan | Cerrado | 1.1 |
| b31c3fd9-d7cb-3517-afa7-7588dd04516a | -10.3377 | -48.18103 | 2025-10-03 04:32:00 | NOAA-20 | PALMAS | TOCANTINS | Brasil | 1721000 | 17 | 33 | nan | nan | nan | Cerrado | 3.8 |
| 47231a08-9082-3d3f-9797-3c9c9e1bea1c | -11.05576 | -47.79866 | 2025-10-03 04:32:00 | NOAA-20 | SILVANÓPOLIS | TOCANTINS | Brasil | 1720655 | 17 | 33 | nan | nan | nan | Cerrado | 1.8 |
| b4953f55-91cf-33d0-9f2b-de4de9196684 | -10.88745 | -46.72698 | 2025-10-03 04:32:00 | NOAA-20 | MATEIROS | TOCANTINS | Brasil | 1712702 | 17 | 33 | nan | nan | nan | Cerrado | 1.1 |
| 919020f4-9a34-3fa8-a371-430e2c882e59 | -7.00767 | -44.49475 | 2025-10-03 04:32:00 | NOAA-20 | BENEDITO LEITE | MARANHÃO | Brasil | 2101806 | 21 | 33 | nan | nan | nan | Cerrado | 2.0 |
| 1c19e8f5-7718-3a6b-bdd5-5969b8b78c81 | -5.23264 | -49.86655 | 2025-10-03 04:32:00 | NOAA-20 | ITUPIRANGA | PARÁ | Brasil | 1503705 | 15 | 33 | nan | nan | nan | Amazônia | 0.4 |
| 7272eaeb-ec2d-34e7-a230-37058e9dd5f2 | -8.8329 | -44.80091 | 2025-10-03 04:32:00 | NOAA-20 | CURRAIS | PIAUÍ | Brasil | 2203230 | 22 | 33 | nan | nan | nan | Cerrado | 2.0 |
| 51733f1c-4640-3a13-8da0-a5d6ea423181 | -6.22578 | -45.35093 | 2025-10-03 04:32:00 | NOAA-20 | FERNANDO FALCÃO | MARANHÃO | Brasil | 2104081 | 21 | 33 | nan | nan | nan | Cerrado | 2.3 |
| 491955ae-3666-340f-9d95-9d8e71c7908c | -10.88345 | -46.70698 | 2025-10-03 04:32:00 | NOAA-20 | MATEIROS | TOCANTINS | Brasil | 1712702 | 17 | 33 | nan | nan | nan | Cerrado | 0.5 |
| 09b897f3-a896-3132-90f1-3b4ebf3f7734 | -11.1024 | -49.80386 | 2025-10-03 04:32:00 | NOAA-20 | LAGOA DA CONFUSÃO | TOCANTINS | Brasil | 1711902 | 17 | 33 | nan | nan | nan | Cerrado | 1.8 |
| 11b65d3b-053f-3d53-bc8c-0e8b33373d68 | -10.16858 | -45.49422 | 2025-10-03 04:32:00 | NOAA-20 | SÃO GONÇALO DO GURGUÉIA | PIAUÍ | Brasil | 2209757 | 22 | 33 | nan | nan | nan | Cerrado | 3.4 |
| 5683c7ee-9a0e-3580-a852-97f67f63530e | -10.00916 | -50.24263 | 2025-10-03 04:32:00 | NOAA-20 | PIUM | TOCANTINS | Brasil | 1717503 | 17 | 33 | nan | nan | nan | Cerrado | 1.8 |
| 31d4d91f-eacb-3225-9194-8c3c2d2f3647 | -9.44448 | -47.37542 | 2025-10-03 04:32:00 | NOAA-20 | RIO SONO | TOCANTINS | Brasil | 1718758 | 17 | 33 | nan | nan | nan | Cerrado | 0.6 |
| e29a7fd3-861b-3810-9c15-aacaa651e4c3 | -9.90084 | -43.714 | 2025-10-03 04:32:00 | NOAA-20 | MORRO CABEÇA NO TEMPO | PIAUÍ | Brasil | 2206654 | 22 | 33 | nan | nan | nan | Caatinga | 3.9 |
| cd36c537-1de8-39dd-bd78-739af59c59b6 | -8.83328 | -44.80277 | 2025-10-03 04:32:00 | NOAA-20 | CURRAIS | PIAUÍ | Brasil | 2203230 | 22 | 33 | nan | nan | nan | Cerrado | 5.2 |
| a290d630-1541-3a14-8a88-8732caeed522 | -6.37856 | -44.63166 | 2025-10-03 04:32:00 | NOAA-20 | MIRADOR | MARANHÃO | Brasil | 2106706 | 21 | 33 | nan | nan | nan | Cerrado | 2.8 |
| 60749a61-b92b-34d5-9cac-4dbb0376a33e | -6.70795 | -42.80968 | 2025-10-03 04:32:00 | NOAA-20 | FRANCISCO AYRES | PIAUÍ | Brasil | 2204105 | 22 | 33 | nan | nan | nan | Caatinga | 2.0 |
| f4be1722-5e45-3fdb-bc4c-5f8922034757 | -10.12663 | -52.35112 | 2025-10-03 04:32:00 | NOAA-20 | SANTA CRUZ DO XINGU | MATO GROSSO | Brasil | 5107743 | 51 | 33 | nan | nan | nan | Amazônia | 0.9 |
| 4b5a69eb-5d30-3e47-8bf3-7c081914efc0 | -10.34255 | -54.19027 | 2025-10-03 04:32:00 | NOAA-20 | PEIXOTO DE AZEVEDO | MATO GROSSO | Brasil | 5106422 | 51 | 33 | nan | nan | nan | Amazônia | 1.0 |
| b3b12131-5cf9-3a03-8bab-7864bb5359f0 | -6.26007 | -43.88586 | 2025-10-03 04:32:00 | NOAA-20 | PASSAGEM FRANCA | MARANHÃO | Brasil | 2107902 | 21 | 33 | nan | nan | nan | Cerrado | 9.0 |
| 1ebb2071-1380-3578-8a45-e97973115918 | -6.44973 | -43.44451 | 2025-10-03 04:32:00 | NOAA-20 | SUCUPIRA DO RIACHÃO | MARANHÃO | Brasil | 2111953 | 21 | 33 | nan | nan | nan | Cerrado | 1.8 |
| 938598af-e972-39cf-9778-76958f1111f4 | -11.42606 | -43.48907 | 2025-10-03 04:32:00 | NOAA-20 | BARRA | BAHIA | Brasil | 2902708 | 29 | 33 | nan | nan | nan | Cerrado | 2.0 |
| f8b34656-052b-3ecb-b601-7f22ddb4a587 | -9.40983 | -47.5335 | 2025-10-03 04:32:00 | NOAA-20 | RIO SONO | TOCANTINS | Brasil | 1718758 | 17 | 33 | nan | nan | nan | Cerrado | 0.9 |
| c57b7bee-aebd-3288-bfca-bef5f9b6404d | -11.16803 | -47.18158 | 2025-10-03 04:32:00 | NOAA-20 | ALMAS | TOCANTINS | Brasil | 1700400 | 17 | 33 | nan | nan | nan | Cerrado | 1.5 |


[Clique aqui para ver as próximas entradas](README104.md)
