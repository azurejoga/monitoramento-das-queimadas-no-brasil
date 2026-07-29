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

## Dados Diários - Página 11

| ID | Latitude | Longitude | Data/Hora GMT | Satélite | Município | Estado | País | Município ID | Estado ID | País ID | Dias sem Chuva | Precipitação | Risco de Fogo | Bioma | FRP |
|----|----------|-----------|---------------|----------|-----------|--------|------|--------------|-----------|---------|----------------|--------------|----------------|-------|-----|
| cfab33fb-93cf-3ce0-bfdd-67fd4925b433 | -6.86884 | -46.01174 | 2026-07-29 04:32:00 | NOAA-20 | FORTALEZA DOS NOGUEIRAS | MARANHÃO | Brasil | 2104107 | 21 | 33 | nan | nan | nan | Cerrado | 0.3 |
| 4b70a6a3-ef17-3016-a708-b3dac057ade4 | -10.93301 | -43.06055 | 2026-07-29 04:32:00 | NOAA-20 | BARRA | BAHIA | Brasil | 2902708 | 29 | 33 | nan | nan | nan | Cerrado | 61.3 |
| 1c0f4bf1-f002-3700-9b37-20cbc3081a61 | -6.84465 | -42.88297 | 2026-07-29 04:32:00 | NOAA-20 | FLORIANO | PIAUÍ | Brasil | 2203909 | 22 | 33 | nan | nan | nan | Caatinga | 1.7 |
| e9d0990d-7ee9-3cf5-8191-eb2ba2bf6e86 | -9.34734 | -50.2669 | 2026-07-29 04:32:00 | NOAA-20 | SANTANA DO ARAGUAIA | PARÁ | Brasil | 1506708 | 15 | 33 | nan | nan | nan | Amazônia | 1.2 |
| 88d3b607-8e54-3432-bad0-c432c225bfdd | -9.60488 | -47.76479 | 2026-07-29 04:32:00 | NOAA-20 | RIO SONO | TOCANTINS | Brasil | 1718758 | 17 | 33 | nan | nan | nan | Cerrado | 2.9 |
| ba5eb58c-86c0-304f-ae2a-62a8f746f49d | -9.0939 | -50.6093 | 2026-07-29 04:32:00 | NOAA-20 | SANTANA DO ARAGUAIA | PARÁ | Brasil | 1506708 | 15 | 33 | nan | nan | nan | Amazônia | 1.9 |
| b7105d8f-71b1-3112-b5b6-bd6f3454748c | -11.54272 | -47.56622 | 2026-07-29 04:32:00 | NOAA-20 | NATIVIDADE | TOCANTINS | Brasil | 1714203 | 17 | 33 | nan | nan | nan | Cerrado | 1.4 |
| 62dff87f-b465-3f2e-8d3d-d0b72aad0ee3 | -9.01031 | -40.99348 | 2026-07-29 04:32:00 | NOAA-20 | CASA NOVA | BAHIA | Brasil | 2907202 | 29 | 33 | nan | nan | nan | Caatinga | 0.9 |
| e6dd41bb-ea08-3ffd-86ae-6bbfd8627a85 | -9.2087 | -49.82124 | 2026-07-29 04:32:00 | NOAA-20 | CASEARA | TOCANTINS | Brasil | 1703909 | 17 | 33 | nan | nan | nan | Cerrado | 1.5 |
| 72658f1d-25b6-30bd-bfca-698086099e44 | -9.6082 | -47.76533 | 2026-07-29 04:32:00 | NOAA-20 | RIO SONO | TOCANTINS | Brasil | 1718758 | 17 | 33 | nan | nan | nan | Cerrado | 2.9 |
| 4e2aa0e7-1d32-3619-9bf0-96ad865f77e6 | -11.53279 | -47.5646 | 2026-07-29 04:32:00 | NOAA-20 | NATIVIDADE | TOCANTINS | Brasil | 1714203 | 17 | 33 | nan | nan | nan | Cerrado | 1.4 |
| 812261c5-7512-34a6-853d-064a1e1390a7 | -8.44666 | -51.54297 | 2026-07-29 04:32:00 | NOAA-20 | CUMARU DO NORTE | PARÁ | Brasil | 1502764 | 15 | 33 | nan | nan | nan | Amazônia | 1.9 |
| 68039365-eea4-3d4c-bf67-6390b8ef9063 | -9.47954 | -57.32503 | 2026-07-29 04:32:00 | NOAA-20 | APIACÁS | MATO GROSSO | Brasil | 5100805 | 51 | 33 | nan | nan | nan | Amazônia | 3.3 |
| 3f74554e-fd17-30f5-b088-f691ddb103f2 | -7.34146 | -45.83627 | 2026-07-29 04:32:00 | NOAA-20 | BALSAS | MARANHÃO | Brasil | 2101400 | 21 | 33 | nan | nan | nan | Cerrado | 12.8 |
| 45891cb9-1547-3796-a3a9-e2895813d39b | -7.40523 | -43.77519 | 2026-07-29 04:32:00 | NOAA-20 | SEBASTIÃO LEAL | PIAUÍ | Brasil | 2210631 | 22 | 33 | nan | nan | nan | Cerrado | 1.7 |
| 884c3f1f-f617-3a57-b244-9735edc14fd6 | -11.52172 | -47.54846 | 2026-07-29 04:32:00 | NOAA-20 | NATIVIDADE | TOCANTINS | Brasil | 1714203 | 17 | 33 | nan | nan | nan | Cerrado | 1.3 |
| b110d5cb-b480-36d1-934c-1f1cc0b193e7 | -10.93509 | -43.04588 | 2026-07-29 04:32:00 | NOAA-20 | BARRA | BAHIA | Brasil | 2902708 | 29 | 33 | nan | nan | nan | Cerrado | 16.4 |
| 502726dd-fa6d-3cca-92fd-7f856c286f4b | -10.35561 | -49.75051 | 2026-07-29 04:32:00 | NOAA-20 | PIUM | TOCANTINS | Brasil | 1717503 | 17 | 33 | nan | nan | nan | Cerrado | 2.2 |
| 269deae3-2774-3d88-b495-80d666dd6a93 | -10.90632 | -45.21552 | 2026-07-29 04:32:00 | NOAA-20 | FORMOSA DO RIO PRETO | BAHIA | Brasil | 2911105 | 29 | 33 | nan | nan | nan | Cerrado | 0.5 |
| 477687a7-faf1-3663-b395-5a33a4876a9d | -5.48094 | -45.11719 | 2026-07-29 04:32:00 | NOAA-20 | BARRA DO CORDA | MARANHÃO | Brasil | 2101608 | 21 | 33 | nan | nan | nan | Cerrado | 2.5 |
| 4071d0b3-4ad9-324c-afea-c9ef7ff0752a | -8.13139 | -46.77423 | 2026-07-29 04:32:00 | NOAA-20 | CAMPOS LINDOS | TOCANTINS | Brasil | 1703842 | 17 | 33 | nan | nan | nan | Cerrado | 1.3 |
| 6862cbef-55b2-3766-b098-7888b925d7fb | -6.8727 | -46.00878 | 2026-07-29 04:32:00 | NOAA-20 | FORTALEZA DOS NOGUEIRAS | MARANHÃO | Brasil | 2104107 | 21 | 33 | nan | nan | nan | Cerrado | 6.3 |
| b9a25183-64a0-3c52-b3b8-3882f09dc4d4 | -7.34258 | -45.8508 | 2026-07-29 04:32:00 | NOAA-20 | BALSAS | MARANHÃO | Brasil | 2101400 | 21 | 33 | nan | nan | nan | Cerrado | 5.9 |
| 88b3d38f-9645-3e27-950b-2ddbdbf78f56 | -5.79528 | -45.08311 | 2026-07-29 04:32:00 | NOAA-20 | BARRA DO CORDA | MARANHÃO | Brasil | 2101608 | 21 | 33 | nan | nan | nan | Cerrado | 0.7 |
| 50f00827-9cb9-36b6-9207-fde44018ef4d | -7.72953 | -47.25006 | 2026-07-29 04:32:00 | NOAA-20 | CAROLINA | MARANHÃO | Brasil | 2102804 | 21 | 33 | nan | nan | nan | Cerrado | 6.0 |
| e32835cf-1964-3dc1-abe8-43e5e5d0fe79 | -10.90404 | -45.20728 | 2026-07-29 04:32:00 | NOAA-20 | FORMOSA DO RIO PRETO | BAHIA | Brasil | 2911105 | 29 | 33 | nan | nan | nan | Cerrado | 1.2 |
| 2ba8b518-85e2-3dc3-af7e-63f957fc3d70 | -11.18158 | -49.93273 | 2026-07-29 04:32:00 | NOAA-20 | LAGOA DA CONFUSÃO | TOCANTINS | Brasil | 1711902 | 17 | 33 | nan | nan | nan | Cerrado | 2.3 |
| fca3e2b6-0161-3b1c-95b1-fdca382620b1 | -11.55595 | -47.56836 | 2026-07-29 04:32:00 | NOAA-20 | NATIVIDADE | TOCANTINS | Brasil | 1714203 | 17 | 33 | nan | nan | nan | Cerrado | 3.8 |
| 5c8bb7a7-1180-392a-8f58-a4fb4fb8f232 | -7.34792 | -45.83693 | 2026-07-29 04:32:00 | NOAA-20 | BALSAS | MARANHÃO | Brasil | 2101400 | 21 | 33 | nan | nan | nan | Cerrado | 10.9 |
| d8ac3230-b786-359e-a9e5-452d15bb73e0 | -10.32603 | -49.71349 | 2026-07-29 04:32:00 | NOAA-20 | PIUM | TOCANTINS | Brasil | 1717503 | 17 | 33 | nan | nan | nan | Cerrado | 1.2 |
| 2716824a-3dae-32b8-ba12-d9f47f75342b | -5.93116 | -46.35596 | 2026-07-29 04:32:00 | NOAA-20 | GRAJAÚ | MARANHÃO | Brasil | 2104800 | 21 | 33 | nan | nan | nan | Cerrado | 1.3 |
| 080fbed8-4c8e-3642-84c0-d6189f5774fc | -9.59799 | -49.30351 | 2026-07-29 04:32:00 | NOAA-20 | ABREULÂNDIA | TOCANTINS | Brasil | 1700251 | 17 | 33 | nan | nan | nan | Cerrado | 0.8 |
| 5c43610f-c5e2-3b8d-b7ea-1e8a9ce161c7 | -10.32255 | -49.7129 | 2026-07-29 04:32:00 | NOAA-20 | PIUM | TOCANTINS | Brasil | 1717503 | 17 | 33 | nan | nan | nan | Cerrado | 0.7 |
| 196dfc0a-1947-3437-a0fe-9713b1673f19 | -12.31086 | -46.75441 | 2026-07-29 04:32:00 | NOAA-20 | TAGUATINGA | TOCANTINS | Brasil | 1720903 | 17 | 33 | nan | nan | nan | Cerrado | 0.7 |
| 8c75905c-cd51-39e8-bacc-8e018beaf647 | -6.87325 | -46.00531 | 2026-07-29 04:32:00 | NOAA-20 | FORTALEZA DOS NOGUEIRAS | MARANHÃO | Brasil | 2104107 | 21 | 33 | nan | nan | nan | Cerrado | 6.3 |
| 987e5769-1f44-369a-bc81-0adf7b546483 | -11.94014 | -43.38382 | 2026-07-29 04:32:00 | NOAA-20 | MUQUÉM DO SÃO FRANCISCO | BAHIA | Brasil | 2922250 | 29 | 33 | nan | nan | nan | Cerrado | 0.8 |
| 51e0c9ab-20fb-3b7b-866e-f37d86342ada | -5.68833 | -50.09673 | 2026-07-29 04:32:00 | NOAA-20 | MARABÁ | PARÁ | Brasil | 1504208 | 15 | 33 | nan | nan | nan | Amazônia | 1.6 |
| 99c5ae8d-8bfb-3f92-b36d-f2b9a762c399 | -11.5361 | -47.56514 | 2026-07-29 04:32:00 | NOAA-20 | NATIVIDADE | TOCANTINS | Brasil | 1714203 | 17 | 33 | nan | nan | nan | Cerrado | 1.4 |
| db6997f2-132c-32ca-882a-af7e222d5dce | -7.24277 | -46.05333 | 2026-07-29 04:32:00 | NOAA-20 | BALSAS | MARANHÃO | Brasil | 2101400 | 21 | 33 | nan | nan | nan | Cerrado | 1.3 |
| 64beffa7-120d-38bd-acd5-384e3281e5a5 | -6.87161 | -46.01574 | 2026-07-29 04:32:00 | NOAA-20 | FORTALEZA DOS NOGUEIRAS | MARANHÃO | Brasil | 2104107 | 21 | 33 | nan | nan | nan | Cerrado | 9.8 |
| 4f440802-5d32-30ce-ac59-aad6b9ed97c4 | -9.59454 | -49.30293 | 2026-07-29 04:32:00 | NOAA-20 | ABREULÂNDIA | TOCANTINS | Brasil | 1700251 | 17 | 33 | nan | nan | nan | Cerrado | 0.8 |
| d4d5fbad-2a4e-33ab-9e68-a9a1a0d6e6fd | -10.90345 | -45.21114 | 2026-07-29 04:32:00 | NOAA-20 | FORMOSA DO RIO PRETO | BAHIA | Brasil | 2911105 | 29 | 33 | nan | nan | nan | Cerrado | 1.2 |
| a8886c73-3378-30ee-8448-51e871d92210 | -11.54913 | -50.16602 | 2026-07-29 04:32:00 | NOAA-20 | FORMOSO DO ARAGUAIA | TOCANTINS | Brasil | 1708205 | 17 | 33 | nan | nan | nan | Cerrado | 0.8 |
| d1597bf3-6368-322e-9f34-efe0e0353e34 | -10.83661 | -49.38889 | 2026-07-29 04:32:00 | NOAA-20 | SANTA RITA DO TOCANTINS | TOCANTINS | Brasil | 1718899 | 17 | 33 | nan | nan | nan | Cerrado | 0.5 |
| 486b6759-fddf-3574-9bde-2687be2562bd | -6.87987 | -46.00636 | 2026-07-29 04:32:00 | NOAA-20 | FORTALEZA DOS NOGUEIRAS | MARANHÃO | Brasil | 2104107 | 21 | 33 | nan | nan | nan | Cerrado | 1.3 |
| f8488021-f402-3a75-bbb7-165368951b6b | -7.45783 | -46.15467 | 2026-07-29 04:32:00 | NOAA-20 | BALSAS | MARANHÃO | Brasil | 2101400 | 21 | 33 | nan | nan | nan | Cerrado | 1.8 |
| abc0f2da-2296-3f72-87db-fc971ef9fb43 | -5.9317 | -46.35252 | 2026-07-29 04:32:00 | NOAA-20 | GRAJAÚ | MARANHÃO | Brasil | 2104800 | 21 | 33 | nan | nan | nan | Cerrado | 1.3 |
| d2216dcd-0ca1-3ae2-92de-e25bb636e094 | -7.40585 | -43.77113 | 2026-07-29 04:32:00 | NOAA-20 | SEBASTIÃO LEAL | PIAUÍ | Brasil | 2210631 | 22 | 33 | nan | nan | nan | Cerrado | 2.1 |
| 55f89a38-34c0-3c8d-8a21-8f61eaf297af | -4.94143 | -48.24969 | 2026-07-29 04:32:00 | NOAA-20 | ABEL FIGUEIREDO | PARÁ | Brasil | 1500131 | 15 | 33 | nan | nan | nan | Amazônia | 0.7 |
| a35d4209-a448-32fd-8bdc-95935eb9d15c | -11.75315 | -46.74368 | 2026-07-29 04:32:00 | NOAA-20 | NOVO JARDIM | TOCANTINS | Brasil | 1715259 | 17 | 33 | nan | nan | nan | Cerrado | 1.1 |
| 9e3e5d9f-a837-326f-a480-f710f77c7ef0 | -8.2566 | -45.82412 | 2026-07-29 04:32:00 | NOAA-20 | TASSO FRAGOSO | MARANHÃO | Brasil | 2112001 | 21 | 33 | nan | nan | nan | Cerrado | 0.4 |
| 9d1595f5-ab2e-38a1-a1ca-c3b5cf278795 | -9.34856 | -50.25141 | 2026-07-29 04:32:00 | NOAA-20 | SANTANA DO ARAGUAIA | PARÁ | Brasil | 1506708 | 15 | 33 | nan | nan | nan | Amazônia | 1.3 |
| 3da9b7a9-2b6b-38ce-b950-f10293ed5075 | -12.31141 | -46.75083 | 2026-07-29 04:32:00 | NOAA-20 | TAGUATINGA | TOCANTINS | Brasil | 1720903 | 17 | 33 | nan | nan | nan | Cerrado | 2.6 |
| 99be17a1-e750-3f8d-bed7-1335357b2e90 | -4.94204 | -48.24592 | 2026-07-29 04:32:00 | NOAA-20 | ABEL FIGUEIREDO | PARÁ | Brasil | 1500131 | 15 | 33 | nan | nan | nan | Amazônia | 1.6 |
| b47c27a5-87a8-3e96-84be-367c585fff22 | -10.35277 | -49.74602 | 2026-07-29 04:32:00 | NOAA-20 | PIUM | TOCANTINS | Brasil | 1717503 | 17 | 33 | nan | nan | nan | Cerrado | 1.5 |
| c0407688-ebfc-32b9-872c-a071593542d7 | -10.36256 | -49.75169 | 2026-07-29 04:32:00 | NOAA-20 | PIUM | TOCANTINS | Brasil | 1717503 | 17 | 33 | nan | nan | nan | Cerrado | 0.5 |
| 634f7310-eef3-34ce-87a4-d697aef6ba5a | -6.21207 | -45.37218 | 2026-07-29 04:32:00 | NOAA-20 | FERNANDO FALCÃO | MARANHÃO | Brasil | 2104081 | 21 | 33 | nan | nan | nan | Cerrado | 0.7 |
| 26deca59-30cd-31e7-b92f-284d4a220802 | -7.01123 | -41.59912 | 2026-07-29 04:32:00 | NOAA-20 | PICOS | PIAUÍ | Brasil | 2208007 | 22 | 33 | nan | nan | nan | Caatinga | 0.7 |
| 95c32ddc-ad02-3177-b31e-b90d5df94059 | -9.60432 | -47.76829 | 2026-07-29 04:32:00 | NOAA-20 | RIO SONO | TOCANTINS | Brasil | 1718758 | 17 | 33 | nan | nan | nan | Cerrado | 0.9 |
| dd92cf81-9be6-3ef7-a595-815f5e816898 | -10.97648 | -49.4355 | 2026-07-29 04:32:00 | NOAA-20 | SANTA RITA DO TOCANTINS | TOCANTINS | Brasil | 1718899 | 17 | 33 | nan | nan | nan | Cerrado | 0.8 |
| e6734698-c74d-380b-b348-c04fd1d18340 | -9.92807 | -46.58139 | 2026-07-29 04:32:00 | NOAA-20 | SÃO FÉLIX DO TOCANTINS | TOCANTINS | Brasil | 1720150 | 17 | 33 | nan | nan | nan | Cerrado | 1.4 |
| 5f9ec0b3-65be-320d-8dde-ab5be20f727e | -5.68908 | -50.09227 | 2026-07-29 04:32:00 | NOAA-20 | MARABÁ | PARÁ | Brasil | 1504208 | 15 | 33 | nan | nan | nan | Amazônia | 1.6 |
| 3b9485d9-d666-3ec3-ad9a-661f99054245 | -7.89942 | -48.05489 | 2026-07-29 04:32:00 | NOAA-20 | PALMEIRANTE | TOCANTINS | Brasil | 1715705 | 17 | 33 | nan | nan | nan | Cerrado | 1.1 |
| 2b9adf6e-3350-3dc6-ad92-08268a5d5f68 | -7.34036 | -45.84327 | 2026-07-29 04:32:00 | NOAA-20 | BALSAS | MARANHÃO | Brasil | 2101400 | 21 | 33 | nan | nan | nan | Cerrado | 12.4 |
| 4881ec1a-f991-327a-a025-723a310880a2 | -6.87503 | -44.76777 | 2026-07-29 04:32:00 | NOAA-20 | SÃO DOMINGOS DO AZEITÃO | MARANHÃO | Brasil | 2110658 | 21 | 33 | nan | nan | nan | Cerrado | 0.7 |
| 9b5d18d7-7ca4-3594-bff3-156528f2874b | -10.93896 | -43.04643 | 2026-07-29 04:32:00 | NOAA-20 | BARRA | BAHIA | Brasil | 2902708 | 29 | 33 | nan | nan | nan | Cerrado | 16.4 |
| 030f60a5-a133-3798-a9c4-2b0efd1e1da1 | -11.77481 | -46.58231 | 2026-07-29 04:32:00 | NOAA-20 | NOVO JARDIM | TOCANTINS | Brasil | 1715259 | 17 | 33 | nan | nan | nan | Cerrado | 0.4 |
| 773426db-a2d4-322f-9fcd-742d713d48fb | -7.33648 | -45.84626 | 2026-07-29 04:32:00 | NOAA-20 | BALSAS | MARANHÃO | Brasil | 2101400 | 21 | 33 | nan | nan | nan | Cerrado | 0.8 |
| 775ed63d-96ac-3e2b-aec9-602a4e57d419 | -7.00722 | -41.59852 | 2026-07-29 04:32:00 | NOAA-20 | PICOS | PIAUÍ | Brasil | 2208007 | 22 | 33 | nan | nan | nan | Caatinga | 0.8 |
| 3de63c7d-7bc8-3815-8650-371cab17b86b | -5.83019 | -44.13806 | 2026-07-29 04:32:00 | NOAA-20 | JATOBÁ | MARANHÃO | Brasil | 2105450 | 21 | 33 | nan | nan | nan | Cerrado | 1.0 |
| b81b938f-a3e2-34f7-ae75-8fb205714ca8 | -5.93935 | -43.66452 | 2026-07-29 04:32:00 | NOAA-20 | LAGOA DO MATO | MARANHÃO | Brasil | 2105922 | 21 | 33 | nan | nan | nan | Cerrado | 2.3 |
| dd8bf30a-d4d5-351c-b7b5-30a628c6e438 | -10.32795 | -46.86832 | 2026-07-29 04:32:00 | NOAA-20 | MATEIROS | TOCANTINS | Brasil | 1712702 | 17 | 33 | nan | nan | nan | Cerrado | 1.3 |
| 0859811f-c520-3aca-91ff-e7501c20c325 | -7.90094 | -48.28059 | 2026-07-29 04:32:00 | NOAA-20 | PALMEIRANTE | TOCANTINS | Brasil | 1715705 | 17 | 33 | nan | nan | nan | Cerrado | 1.5 |
| 80f638b5-1388-3c23-a627-4ff38ff596a1 | -10.41185 | -48.37113 | 2026-07-29 04:32:00 | NOAA-20 | PORTO NACIONAL | TOCANTINS | Brasil | 1718204 | 17 | 33 | nan | nan | nan | Cerrado | 2.6 |
| f3a085ca-9743-31f1-ad71-e03ac2e89af7 | -5.83778 | -44.89949 | 2026-07-29 04:32:00 | NOAA-20 | TUNTUM | MARANHÃO | Brasil | 2112308 | 21 | 33 | nan | nan | nan | Cerrado | 0.8 |
| 9caeed45-d9cb-3a7a-9b60-e0a06f263e12 | -7.35566 | -45.83096 | 2026-07-29 04:32:00 | NOAA-20 | BALSAS | MARANHÃO | Brasil | 2101400 | 21 | 33 | nan | nan | nan | Cerrado | 12.3 |
| 1c961044-f134-31de-a006-3830bdd3afb7 | -10.13532 | -42.41925 | 2026-07-29 04:32:00 | NOAA-20 | SENTO SÉ | BAHIA | Brasil | 2930204 | 29 | 33 | nan | nan | nan | Caatinga | 0.8 |
| 88871c30-5bc1-32a4-bad1-453b700e285c | -11.16788 | -49.42405 | 2026-07-29 04:32:00 | NOAA-20 | CRIXÁS DO TOCANTINS | TOCANTINS | Brasil | 1706258 | 17 | 33 | nan | nan | nan | Cerrado | 1.1 |
| e3993fc5-05ad-363c-b5c3-bc5ae445641f | -6.87215 | -46.01226 | 2026-07-29 04:32:00 | NOAA-20 | FORTALEZA DOS NOGUEIRAS | MARANHÃO | Brasil | 2104107 | 21 | 33 | nan | nan | nan | Cerrado | 9.8 |
| be2de6a2-97cf-3ec7-a632-12125791b5d2 | -11.52447 | -47.5525 | 2026-07-29 04:32:00 | NOAA-20 | NATIVIDADE | TOCANTINS | Brasil | 1714203 | 17 | 33 | nan | nan | nan | Cerrado | 1.3 |
| 94ca16e7-2386-38d2-9c22-bff016ec5cdb | -6.86939 | -46.00826 | 2026-07-29 04:32:00 | NOAA-20 | FORTALEZA DOS NOGUEIRAS | MARANHÃO | Brasil | 2104107 | 21 | 33 | nan | nan | nan | Cerrado | 2.6 |
| 8274f13f-a4b3-3301-9cf3-3d8514e8f0ba | -8.44497 | -51.55294 | 2026-07-29 04:32:00 | NOAA-20 | CUMARU DO NORTE | PARÁ | Brasil | 1502764 | 15 | 33 | nan | nan | nan | Amazônia | 2.4 |
| 9893c857-ccf6-349d-ae7a-bd284d478be0 | -6.05317 | -43.8685 | 2026-07-29 04:32:00 | NOAA-20 | PASSAGEM FRANCA | MARANHÃO | Brasil | 2107902 | 21 | 33 | nan | nan | nan | Cerrado | 1.0 |
| 60173900-2276-3f8a-ac6a-d722712d7ea6 | -8.44581 | -51.54797 | 2026-07-29 04:32:00 | NOAA-20 | CUMARU DO NORTE | PARÁ | Brasil | 1502764 | 15 | 33 | nan | nan | nan | Amazônia | 2.4 |
| 3129808a-8d4a-3ae9-a540-c920448f6785 | -7.22686 | -49.59396 | 2026-07-29 04:32:00 | NOAA-20 | RIO MARIA | PARÁ | Brasil | 1506161 | 15 | 33 | nan | nan | nan | Amazônia | 0.7 |
| f98c1cdf-3418-348b-9773-f836801f022a | -5.2715 | -45.17529 | 2026-07-29 04:32:00 | NOAA-20 | BARRA DO CORDA | MARANHÃO | Brasil | 2101608 | 21 | 33 | nan | nan | nan | Cerrado | 0.5 |
| db500597-c900-3b2b-bdb0-a2dd77bfb82f | -10.93826 | -43.05133 | 2026-07-29 04:32:00 | NOAA-20 | BARRA | BAHIA | Brasil | 2902708 | 29 | 33 | nan | nan | nan | Cerrado | 16.4 |
| 9c76ba20-3cad-3f98-950f-009ae3b38e3c | -7.34738 | -45.84044 | 2026-07-29 04:32:00 | NOAA-20 | BALSAS | MARANHÃO | Brasil | 2101400 | 21 | 33 | nan | nan | nan | Cerrado | 10.9 |
| eff83b61-65d3-3612-a7f7-cdc3a57f4215 | -6.87546 | -46.01279 | 2026-07-29 04:32:00 | NOAA-20 | FORTALEZA DOS NOGUEIRAS | MARANHÃO | Brasil | 2104107 | 21 | 33 | nan | nan | nan | Cerrado | 9.8 |
| ae90a65b-f02f-3e2f-81ae-b274b8268c9f | -9.08585 | -50.58996 | 2026-07-29 04:32:00 | NOAA-20 | SANTANA DO ARAGUAIA | PARÁ | Brasil | 1506708 | 15 | 33 | nan | nan | nan | Amazônia | 1.0 |
| 3a6ae2d9-148d-339d-b756-9da6b2cf840b | -7.72092 | -49.45586 | 2026-07-29 04:32:00 | NOAA-20 | FLORESTA DO ARAGUAIA | PARÁ | Brasil | 1503044 | 15 | 33 | nan | nan | nan | Amazônia | 0.9 |
| 5b1af2d6-3233-3c6c-8e61-468f28ab4baf | -10.13134 | -42.41866 | 2026-07-29 04:32:00 | NOAA-20 | SENTO SÉ | BAHIA | Brasil | 2930204 | 29 | 33 | nan | nan | nan | Caatinga | 2.0 |
| 4ca805ed-a7d0-3b38-beaa-4cf23eb34d8f | -8.49563 | -46.01331 | 2026-07-29 04:32:00 | NOAA-20 | TASSO FRAGOSO | MARANHÃO | Brasil | 2112001 | 21 | 33 | nan | nan | nan | Cerrado | 1.1 |
| b04c57fa-4ac6-3ad6-a0a0-07a5821224c4 | -9.48028 | -57.32111 | 2026-07-29 04:32:00 | NOAA-20 | APIACÁS | MATO GROSSO | Brasil | 5100805 | 51 | 33 | nan | nan | nan | Amazônia | 3.3 |
| d48f2465-cce9-3a92-8f20-05038815ca19 | -8.44274 | -51.5423 | 2026-07-29 04:32:00 | NOAA-20 | CUMARU DO NORTE | PARÁ | Brasil | 1502764 | 15 | 33 | nan | nan | nan | Amazônia | 1.7 |
| 31f5a1f3-3ba9-3f71-a84f-5df5e1f55a8f | -9.33866 | -48.55005 | 2026-07-29 04:32:00 | NOAA-20 | RIO DOS BOIS | TOCANTINS | Brasil | 1718709 | 17 | 33 | nan | nan | nan | Cerrado | 1.2 |
| a0777ac0-94e7-34fa-a9b3-8618b79fbe84 | -5.8417 | -44.89642 | 2026-07-29 04:32:00 | NOAA-20 | TUNTUM | MARANHÃO | Brasil | 2112308 | 21 | 33 | nan | nan | nan | Cerrado | 2.7 |
| 210b0750-1f44-3f7b-9cc2-c24f7d57c20c | -11.54933 | -47.56729 | 2026-07-29 04:32:00 | NOAA-20 | NATIVIDADE | TOCANTINS | Brasil | 1714203 | 17 | 33 | nan | nan | nan | Cerrado | 1.1 |
| 77e7c639-f1d0-37cf-b4fa-b797cd21f874 | -7.35125 | -45.83745 | 2026-07-29 04:32:00 | NOAA-20 | BALSAS | MARANHÃO | Brasil | 2101400 | 21 | 33 | nan | nan | nan | Cerrado | 10.9 |
| b7d12156-50d4-39e6-9119-3fea04d95e84 | -10.13339 | -42.41717 | 2026-07-29 04:32:00 | NOAA-20 | SENTO SÉ | BAHIA | Brasil | 2930204 | 29 | 33 | nan | nan | nan | Caatinga | 1.0 |


[Clique aqui para ver as próximas entradas](README12.md)
