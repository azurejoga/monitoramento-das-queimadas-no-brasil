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

## Dados Diários - Página 48

| ID | Latitude | Longitude | Data/Hora GMT | Satélite | Município | Estado | País | Município ID | Estado ID | País ID | Dias sem Chuva | Precipitação | Risco de Fogo | Bioma | FRP |
|----|----------|-----------|---------------|----------|-----------|--------|------|--------------|-----------|---------|----------------|--------------|----------------|-------|-----|
| cbe84b7f-9751-33d7-9d04-05c5b6f25813 | -6.37373 | -43.88134 | 2025-10-03 04:10:00 | NPP-375D | PARAIBANO | MARANHÃO | Brasil | 2107704 | 21 | 33 | nan | nan | nan | Cerrado | 2.3 |
| 30bf5a18-59fa-33d3-a07a-587fa32a875f | -7.56878 | -42.62897 | 2025-10-03 04:10:00 | NPP-375D | SÃO JOSÉ DO PEIXE | PIAUÍ | Brasil | 2210102 | 22 | 33 | nan | nan | nan | Caatinga | 0.8 |
| a0002736-abad-3a53-9109-97d70413bf80 | -7.75461 | -46.2528 | 2025-10-03 04:10:00 | NPP-375D | BALSAS | MARANHÃO | Brasil | 2101400 | 21 | 33 | nan | nan | nan | Cerrado | 16.3 |
| 2ee4f436-d031-3362-9b20-f1c39b9e2552 | -5.90483 | -39.1526 | 2025-10-03 04:10:00 | NPP-375D | SOLONÓPOLE | CEARÁ | Brasil | 2313005 | 23 | 33 | nan | nan | nan | Caatinga | 2.6 |
| 426df32b-5f2e-3bae-9827-ff13d77e7873 | -2.92285 | -48.3059 | 2025-10-03 04:10:00 | NPP-375D | TOMÉ-AÇU | PARÁ | Brasil | 1508001 | 15 | 33 | nan | nan | nan | Amazônia | 7.1 |
| ec1a00d1-ba95-31ad-97aa-1b89babf6b9c | -7.78324 | -42.57693 | 2025-10-03 04:10:00 | NPP-375D | SOCORRO DO PIAUÍ | PIAUÍ | Brasil | 2210904 | 22 | 33 | nan | nan | nan | Caatinga | 1.9 |
| b47d2a5a-d4eb-390b-9b0c-7bd04b3e495c | -6.30273 | -43.11448 | 2025-10-03 04:10:00 | NPP-375D | SÃO FRANCISCO DO MARANHÃO | MARANHÃO | Brasil | 2110906 | 21 | 33 | nan | nan | nan | Cerrado | 0.9 |
| 8634c3e9-d886-3f5a-89df-995622634d91 | -3.64169 | -43.62 | 2025-10-03 04:10:00 | NPP-375D | VARGEM GRANDE | MARANHÃO | Brasil | 2112704 | 21 | 33 | nan | nan | nan | Cerrado | 3.3 |
| 31682aea-b340-3504-a6dd-fc3d3db0f0ac | -7.80002 | -42.51478 | 2025-10-03 04:10:00 | NPP-375D | SÃO JOSÉ DO PEIXE | PIAUÍ | Brasil | 2210102 | 22 | 33 | nan | nan | nan | Caatinga | 2.3 |
| f0fe30cb-bee2-396b-ba81-9cb32c16c4f8 | -4.65266 | -45.78517 | 2025-10-03 04:10:00 | NPP-375D | MARAJÁ DO SENA | MARANHÃO | Brasil | 2106359 | 21 | 33 | nan | nan | nan | Amazônia | 1.4 |
| 04a3eb8b-1833-3e77-8d82-a1bff27d3bef | -7.76366 | -42.61358 | 2025-10-03 04:10:00 | NPP-375D | RIBEIRA DO PIAUÍ | PIAUÍ | Brasil | 2208874 | 22 | 33 | nan | nan | nan | Caatinga | 15.3 |
| 197a54ba-2f02-387a-bf95-11b77b72e0c8 | -4.65895 | -45.79612 | 2025-10-03 04:10:00 | NPP-375D | MARAJÁ DO SENA | MARANHÃO | Brasil | 2106359 | 21 | 33 | nan | nan | nan | Amazônia | 15.1 |
| 7e09b5f1-ee5c-3ac3-8589-4ea76ec74601 | -7.88916 | -47.35385 | 2025-10-03 04:10:00 | NPP-375D | GOIATINS | TOCANTINS | Brasil | 1709005 | 17 | 33 | nan | nan | nan | Cerrado | 1.6 |
| 29a9bd78-89f2-391f-8d95-b43eda6e7063 | -3.84367 | -41.58937 | 2025-10-03 04:10:00 | NPP-375D | PIRACURUCA | PIAUÍ | Brasil | 2208304 | 22 | 33 | nan | nan | nan | Caatinga | 4.0 |
| 61303fb0-3475-37c0-9a0e-0c78fbe1532b | -7.75148 | -42.58266 | 2025-10-03 04:10:00 | NPP-375D | SOCORRO DO PIAUÍ | PIAUÍ | Brasil | 2210904 | 22 | 33 | nan | nan | nan | Caatinga | 2.1 |
| 404b9898-aea5-360e-b33d-36c3cce37093 | -7.78501 | -42.50158 | 2025-10-03 04:10:00 | NPP-375D | SÃO JOSÉ DO PEIXE | PIAUÍ | Brasil | 2210102 | 22 | 33 | nan | nan | nan | Caatinga | 3.3 |
| 256302c4-7ca1-342d-9338-d7de909efa19 | -8.48405 | -44.59326 | 2025-10-03 04:10:00 | NPP-375D | PALMEIRA DO PIAUÍ | PIAUÍ | Brasil | 2207405 | 22 | 33 | nan | nan | nan | Cerrado | 1.6 |
| 96ece857-eece-3ca0-89f8-ab82f0f27e62 | -7.66747 | -47.28636 | 2025-10-03 04:10:00 | NPP-375D | CAROLINA | MARANHÃO | Brasil | 2102804 | 21 | 33 | nan | nan | nan | Cerrado | 5.5 |
| e8318894-d4e6-3d02-9492-73b3cae0ffeb | -6.79838 | -44.75104 | 2025-10-03 04:10:00 | NPP-375D | SÃO DOMINGOS DO AZEITÃO | MARANHÃO | Brasil | 2110658 | 21 | 33 | nan | nan | nan | Cerrado | 2.3 |
| 16d89c23-651e-3482-b524-5e1466897fd1 | -6.68744 | -42.83033 | 2025-10-03 04:10:00 | NPP-375D | FRANCISCO AYRES | PIAUÍ | Brasil | 2204105 | 22 | 33 | nan | nan | nan | Caatinga | 1.5 |
| 55eb15f0-7aa0-3080-a118-ccbc8b88fd00 | -7.75261 | -42.57562 | 2025-10-03 04:10:00 | NPP-375D | SOCORRO DO PIAUÍ | PIAUÍ | Brasil | 2210904 | 22 | 33 | nan | nan | nan | Caatinga | 1.9 |
| 5786aa2b-b540-3c4c-862d-086251586222 | -4.01046 | -41.7949 | 2025-10-03 04:10:00 | NPP-375D | PIRACURUCA | PIAUÍ | Brasil | 2208304 | 22 | 33 | nan | nan | nan | Caatinga | 1.9 |
| b29c39e6-ffb5-316a-a8cd-08e2af966d36 | -4.43804 | -40.76359 | 2025-10-03 04:10:00 | NPP-375D | IPU | CEARÁ | Brasil | 2305803 | 23 | 33 | nan | nan | nan | Caatinga | 1.0 |
| b295d43d-0729-33ff-a604-19bc80ae27d6 | -8.05348 | -43.97818 | 2025-10-03 04:10:00 | NPP-375D | MANOEL EMÍDIO | PIAUÍ | Brasil | 2205904 | 22 | 33 | nan | nan | nan | Cerrado | 2.3 |
| e079d863-2b71-3fe7-b27f-36d998022203 | -7.76075 | -46.26387 | 2025-10-03 04:10:00 | NPP-375D | BALSAS | MARANHÃO | Brasil | 2101400 | 21 | 33 | nan | nan | nan | Cerrado | 59.7 |
| 90d554d0-1fbb-3c3e-a30f-12ddb9894ee2 | -7.56857 | -42.39462 | 2025-10-03 04:10:00 | NPP-375D | SÃO MIGUEL DO FIDALGO | PIAUÍ | Brasil | 2210391 | 22 | 33 | nan | nan | nan | Caatinga | 3.3 |
| cebac1eb-98dd-3400-a0e7-c60edbbbbf0a | -7.45242 | -46.98428 | 2025-10-03 04:10:00 | NPP-375D | RIACHÃO | MARANHÃO | Brasil | 2109502 | 21 | 33 | nan | nan | nan | Cerrado | 0.9 |
| 48a9c0c0-8e91-3915-8f48-b12dccb9a92b | -5.62849 | -43.91483 | 2025-10-03 04:10:00 | NPP-375D | FORTUNA | MARANHÃO | Brasil | 2104206 | 21 | 33 | nan | nan | nan | Cerrado | 4.2 |
| 1a0ec22c-545d-3804-843a-f54bc6f6aa6c | -5.78566 | -45.76168 | 2025-10-03 04:10:00 | NPP-375D | GRAJAÚ | MARANHÃO | Brasil | 2104800 | 21 | 33 | nan | nan | nan | Cerrado | 1.8 |
| 615497b4-e91b-3694-b569-5488dbb5cb48 | -7.71225 | -46.19682 | 2025-10-03 04:10:00 | NPP-375D | BALSAS | MARANHÃO | Brasil | 2101400 | 21 | 33 | nan | nan | nan | Cerrado | 3.8 |
| 8a724693-8408-365d-bd60-61eb3ba7debf | -7.78154 | -47.37523 | 2025-10-03 04:10:00 | NPP-375D | GOIATINS | TOCANTINS | Brasil | 1709005 | 17 | 33 | nan | nan | nan | Cerrado | 6.4 |
| e0aaabff-aea3-32f8-a0ff-b79a64ea9fac | -7.78835 | -42.5021 | 2025-10-03 04:10:00 | NPP-375D | SÃO JOSÉ DO PEIXE | PIAUÍ | Brasil | 2210102 | 22 | 33 | nan | nan | nan | Caatinga | 1.2 |
| 72e0e861-c780-37ee-be3b-354872557533 | -6.71164 | -42.80872 | 2025-10-03 04:10:00 | NPP-375D | FRANCISCO AYRES | PIAUÍ | Brasil | 2204105 | 22 | 33 | nan | nan | nan | Caatinga | 1.3 |
| 6ab268e0-c050-34ec-9390-1208d29ba2fd | -7.77431 | -42.58994 | 2025-10-03 04:10:00 | NPP-375D | SOCORRO DO PIAUÍ | PIAUÍ | Brasil | 2210904 | 22 | 33 | nan | nan | nan | Caatinga | 7.8 |
| 829e8d41-7494-350a-a6b0-1beae0bad89b | -6.301 | -43.90663 | 2025-10-03 04:10:00 | NPP-375D | PARAIBANO | MARANHÃO | Brasil | 2107704 | 21 | 33 | nan | nan | nan | Cerrado | 1.5 |
| 8162fe67-3ea9-30b1-827a-8827a3d0c78e | -5.3997 | -41.33351 | 2025-10-03 04:10:00 | NPP-375D | CASTELO DO PIAUÍ | PIAUÍ | Brasil | 2202604 | 22 | 33 | nan | nan | nan | Caatinga | 0.3 |
| 6b3d68b9-8abd-3c98-bfe8-852de33c9179 | -7.7719 | -47.38145 | 2025-10-03 04:10:00 | NPP-375D | GOIATINS | TOCANTINS | Brasil | 1709005 | 17 | 33 | nan | nan | nan | Cerrado | 4.4 |
| 6abed5a6-2a86-34c4-905f-740c3846f89d | -5.94064 | -42.88962 | 2025-10-03 04:10:00 | NPP-375D | PALMEIRAIS | PIAUÍ | Brasil | 2207504 | 22 | 33 | nan | nan | nan | Caatinga | 3.2 |
| c7e1d426-cc35-3300-9cca-b2bfb47e57d6 | -4.6558 | -45.79069 | 2025-10-03 04:10:00 | NPP-375D | MARAJÁ DO SENA | MARANHÃO | Brasil | 2106359 | 21 | 33 | nan | nan | nan | Amazônia | 3.6 |
| eca3fc51-b7eb-3a97-84d5-0163877587d6 | -6.32639 | -43.88272 | 2025-10-03 04:10:00 | NPP-375D | PARAIBANO | MARANHÃO | Brasil | 2107704 | 21 | 33 | nan | nan | nan | Cerrado | 4.2 |
| ed6327ba-563e-3e14-bef9-b08ee31c3df1 | -6.12886 | -44.03153 | 2025-10-03 04:10:00 | NPP-375D | COLINAS | MARANHÃO | Brasil | 2103505 | 21 | 33 | nan | nan | nan | Cerrado | 0.9 |
| 305eadc4-d150-3d2f-b946-3f1ab312d7d3 | -6.73618 | -44.58097 | 2025-10-03 04:10:00 | NPP-375D | SÃO DOMINGOS DO AZEITÃO | MARANHÃO | Brasil | 2110658 | 21 | 33 | nan | nan | nan | Cerrado | 2.0 |
| f016756d-5fcd-31bc-a994-33d4f33e5fc4 | -7.26721 | -45.49376 | 2025-10-03 04:10:00 | NPP-375D | SAMBAÍBA | MARANHÃO | Brasil | 2109700 | 21 | 33 | nan | nan | nan | Cerrado | 1.0 |
| 971de9cb-c8f1-312c-8c27-85bf57b08047 | -7.90385 | -43.54094 | 2025-10-03 04:10:00 | NPP-375D | CANAVIEIRA | PIAUÍ | Brasil | 2202251 | 22 | 33 | nan | nan | nan | Cerrado | 7.5 |
| d692532b-0262-3b73-9ba9-f960c63672fa | -7.52864 | -47.29009 | 2025-10-03 04:10:00 | NPP-375D | CAROLINA | MARANHÃO | Brasil | 2102804 | 21 | 33 | nan | nan | nan | Cerrado | 1.7 |
| ad6a1cd7-db5d-3812-bd58-a3f93acf93d5 | -8.16965 | -44.13599 | 2025-10-03 04:10:00 | NPP-375D | SEBASTIÃO LEAL | PIAUÍ | Brasil | 2210631 | 22 | 33 | nan | nan | nan | Cerrado | 0.9 |
| c00d7017-56a5-3efe-8f55-1f0a78dc1ebb | -5.36007 | -45.95797 | 2025-10-03 04:10:00 | NPP-375D | ITAIPAVA DO GRAJAÚ | MARANHÃO | Brasil | 2105351 | 21 | 33 | nan | nan | nan | Cerrado | 2.1 |
| 1967413a-dcc1-3035-acb9-5b85b3b08895 | -5.6432 | -43.91328 | 2025-10-03 04:10:00 | NPP-375D | FORTUNA | MARANHÃO | Brasil | 2104206 | 21 | 33 | nan | nan | nan | Cerrado | 1.7 |
| 52deb65e-9768-385f-baa0-91ec2efeb108 | -3.93649 | -47.5657 | 2025-10-03 04:10:00 | NPP-375D | ULIANÓPOLIS | PARÁ | Brasil | 1508126 | 15 | 33 | nan | nan | nan | Amazônia | 12.0 |
| 283682a1-c6fe-30c6-b0d0-6e9b73e2034c | -6.06474 | -44.33236 | 2025-10-03 04:10:00 | NPP-375D | MIRADOR | MARANHÃO | Brasil | 2106706 | 21 | 33 | nan | nan | nan | Cerrado | 2.3 |
| ff1ee32c-a106-3526-8bc5-11518f194c45 | -6.94178 | -38.57113 | 2025-10-03 04:10:00 | NPP-375D | CAJAZEIRAS | PARAÍBA | Brasil | 2503704 | 25 | 33 | nan | nan | nan | Caatinga | 3.1 |
| 420adf01-1530-332a-860b-7e6e378b81f2 | -6.33097 | -44.688 | 2025-10-03 04:10:00 | NPP-375D | MIRADOR | MARANHÃO | Brasil | 2106706 | 21 | 33 | nan | nan | nan | Cerrado | 2.3 |
| 1c7e460c-99c8-38e5-b3e5-d5fe67ebdec9 | -7.90844 | -43.53416 | 2025-10-03 04:10:00 | NPP-375D | CANAVIEIRA | PIAUÍ | Brasil | 2202251 | 22 | 33 | nan | nan | nan | Cerrado | 2.3 |
| fcdcd808-f54c-3b53-9793-de945ce2f733 | -5.63428 | -44.7018 | 2025-10-03 04:10:00 | NPP-375D | SANTA FILOMENA DO MARANHÃO | MARANHÃO | Brasil | 2109759 | 21 | 33 | nan | nan | nan | Cerrado | 3.6 |
| b5902dff-c6ea-3a9f-8d7e-92f9609deed1 | -5.9066 | -39.14875 | 2025-10-03 04:10:00 | NPP-375D | SOLONÓPOLE | CEARÁ | Brasil | 2313005 | 23 | 33 | nan | nan | nan | Caatinga | 2.8 |
| d36718aa-93ff-36bd-adbd-824f060b6b24 | -7.29546 | -44.18432 | 2025-10-03 04:10:00 | NPP-375D | ANTÔNIO ALMEIDA | PIAUÍ | Brasil | 2200806 | 22 | 33 | nan | nan | nan | Cerrado | 1.6 |
| d44db574-c78b-3f5d-93ef-4022f955d705 | -5.44969 | -44.82354 | 2025-10-03 04:10:00 | NPP-375D | TUNTUM | MARANHÃO | Brasil | 2112308 | 21 | 33 | nan | nan | nan | Cerrado | 2.3 |
| b38d8365-8328-3886-b3d0-88bb2653bc29 | -6.67295 | -42.37058 | 2025-10-03 04:10:00 | NPP-375D | TANQUE DO PIAUÍ | PIAUÍ | Brasil | 2210979 | 22 | 33 | nan | nan | nan | Caatinga | 1.0 |
| 8f33ccfb-2cbf-3e2c-b450-de11a450fbdf | -6.68967 | -42.83801 | 2025-10-03 04:10:00 | NPP-375D | AMARANTE | PIAUÍ | Brasil | 2200509 | 22 | 33 | nan | nan | nan | Caatinga | 2.1 |
| 2dc255ca-6474-329b-8edc-bad516a3ac1b | -4.9366 | -38.00182 | 2025-10-03 04:10:00 | NPP-375D | RUSSAS | CEARÁ | Brasil | 2311801 | 23 | 33 | nan | nan | nan | Caatinga | 2.8 |
| cf9c2a6b-7c0f-3b2c-83f1-485265dd6fde | -7.75541 | -46.24802 | 2025-10-03 04:10:00 | NPP-375D | BALSAS | MARANHÃO | Brasil | 2101400 | 21 | 33 | nan | nan | nan | Cerrado | 16.5 |
| faa046bc-5605-32b6-9ac0-788ebee01787 | -7.52074 | -50.49894 | 2025-10-03 04:10:00 | NPP-375D | BANNACH | PARÁ | Brasil | 1501253 | 15 | 33 | nan | nan | nan | Amazônia | 2.2 |
| 0aa512d1-bc11-3933-a1b5-1dbcd7c26332 | -3.84588 | -41.57543 | 2025-10-03 04:10:00 | NPP-375D | PIRACURUCA | PIAUÍ | Brasil | 2208304 | 22 | 33 | nan | nan | nan | Caatinga | 3.8 |
| 33dc205f-a78b-382b-bd62-920698dacb7d | -6.68012 | -42.83287 | 2025-10-03 04:10:00 | NPP-375D | FRANCISCO AYRES | PIAUÍ | Brasil | 2204105 | 22 | 33 | nan | nan | nan | Caatinga | 0.9 |
| b23a7e27-7347-3bf7-bc15-5a31e518f603 | -6.44572 | -43.46148 | 2025-10-03 04:10:00 | NPP-375D | SUCUPIRA DO RIACHÃO | MARANHÃO | Brasil | 2111953 | 21 | 33 | nan | nan | nan | Cerrado | 2.3 |
| 0fd46312-a7ad-3217-8c98-fa53f176429f | -6.9591 | -45.34374 | 2025-10-03 04:10:00 | NPP-375D | SAMBAÍBA | MARANHÃO | Brasil | 2109700 | 21 | 33 | nan | nan | nan | Cerrado | 3.4 |
| 7682c2f1-53a6-38dd-aaf9-39c7b0f14923 | -4.65183 | -45.79016 | 2025-10-03 04:10:00 | NPP-375D | MARAJÁ DO SENA | MARANHÃO | Brasil | 2106359 | 21 | 33 | nan | nan | nan | Amazônia | 3.6 |
| 210ed1d3-432d-320e-b78f-8e383dc51387 | -5.64476 | -49.13008 | 2025-10-03 04:10:00 | NPP-375D | MARABÁ | PARÁ | Brasil | 1504208 | 15 | 33 | nan | nan | nan | Amazônia | 1.3 |
| 7b3595ea-8d10-376f-a86a-d57b47e86359 | -7.8041 | -49.86638 | 2025-10-03 04:10:00 | NPP-375D | PAU D'ARCO | PARÁ | Brasil | 1505551 | 15 | 33 | nan | nan | nan | Amazônia | 3.1 |
| 6700612d-c753-32ab-8fd6-b616f18a3dc5 | -7.74644 | -42.5927 | 2025-10-03 04:10:00 | NPP-375D | SOCORRO DO PIAUÍ | PIAUÍ | Brasil | 2210904 | 22 | 33 | nan | nan | nan | Caatinga | 2.3 |
| aeb0d6d4-b032-3ada-81b6-e6f97cd7f52e | -6.59724 | -44.3231 | 2025-10-03 04:10:00 | NPP-375D | PASTOS BONS | MARANHÃO | Brasil | 2108009 | 21 | 33 | nan | nan | nan | Cerrado | 4.7 |
| 04d8d0cf-6ab5-383e-a115-42705fc44483 | -5.28299 | -47.52245 | 2025-10-03 04:10:00 | NPP-375D | IMPERATRIZ | MARANHÃO | Brasil | 2105302 | 21 | 33 | nan | nan | nan | Cerrado | 1.0 |
| b6c7bdaf-11d3-3f66-8790-947876460640 | -7.76661 | -42.53102 | 2025-10-03 04:10:00 | NPP-375D | SÃO JOSÉ DO PEIXE | PIAUÍ | Brasil | 2210102 | 22 | 33 | nan | nan | nan | Caatinga | 4.4 |
| a5d47c48-ff82-3300-981b-cc7435017948 | -7.77497 | -42.52156 | 2025-10-03 04:10:00 | NPP-375D | SÃO JOSÉ DO PEIXE | PIAUÍ | Brasil | 2210102 | 22 | 33 | nan | nan | nan | Caatinga | 3.4 |
| 1dff7a81-e0e1-313c-8a19-f3774616f307 | -6.3204 | -43.89766 | 2025-10-03 04:10:00 | NPP-375D | PARAIBANO | MARANHÃO | Brasil | 2107704 | 21 | 33 | nan | nan | nan | Cerrado | 1.2 |
| 8709f003-8631-38ed-a252-68c354e6a73c | -1.07894 | -53.67805 | 2025-10-03 04:10:00 | NPP-375D | PRAINHA | PARÁ | Brasil | 1506005 | 15 | 33 | nan | nan | nan | Amazônia | 3.2 |
| f2ab866b-9253-3b23-ace6-82c64481aa36 | -7.90503 | -43.53359 | 2025-10-03 04:10:00 | NPP-375D | CANAVIEIRA | PIAUÍ | Brasil | 2202251 | 22 | 33 | nan | nan | nan | Cerrado | 3.5 |
| 7c650608-43b9-352f-8239-e1b9811f4b7d | -4.64306 | -42.53341 | 2025-10-03 04:10:00 | NPP-375D | JOSÉ DE FREITAS | PIAUÍ | Brasil | 2205508 | 22 | 33 | nan | nan | nan | Caatinga | 1.5 |
| 70ad0206-e00f-39ea-b045-58397befc9f2 | -7.55118 | -42.40268 | 2025-10-03 04:10:00 | NPP-375D | SÃO MIGUEL DO FIDALGO | PIAUÍ | Brasil | 2210391 | 22 | 33 | nan | nan | nan | Caatinga | 1.1 |
| 54cf16ea-7ec2-3afe-b718-e34a6b8e0a92 | -7.04242 | -43.31761 | 2025-10-03 04:10:00 | NPP-375D | FLORIANO | PIAUÍ | Brasil | 2203909 | 22 | 33 | nan | nan | nan | Caatinga | 1.7 |
| 010471df-b1ef-3226-8ea7-15cad4f4a17a | -7.29395 | -46.01142 | 2025-10-03 04:10:00 | NPP-375D | BALSAS | MARANHÃO | Brasil | 2101400 | 21 | 33 | nan | nan | nan | Cerrado | 1.0 |
| be53df8f-5a9e-3373-804b-a0da43072860 | -8.30525 | -44.86943 | 2025-10-03 04:10:00 | NPP-375D | BAIXA GRANDE DO RIBEIRO | PIAUÍ | Brasil | 2201150 | 22 | 33 | nan | nan | nan | Cerrado | 2.1 |
| 02142268-0608-3d0f-901b-77d4de8febcb | -7.76871 | -42.60351 | 2025-10-03 04:10:00 | NPP-375D | RIBEIRA DO PIAUÍ | PIAUÍ | Brasil | 2208874 | 22 | 33 | nan | nan | nan | Caatinga | 5.1 |
| bd143310-b956-3509-b8b6-29af4134fd73 | -6.2487 | -43.64673 | 2025-10-03 04:10:00 | NPP-375D | PASSAGEM FRANCA | MARANHÃO | Brasil | 2107902 | 21 | 33 | nan | nan | nan | Cerrado | 2.8 |
| 8d0e813c-c90a-3eec-a6d9-45f3565340b5 | -5.20651 | -42.72204 | 2025-10-03 04:10:00 | NPP-375D | TERESINA | PIAUÍ | Brasil | 2211001 | 22 | 33 | nan | nan | nan | Caatinga | 1.9 |
| 593c3862-8b50-3c0d-9b7a-bb90dacc91ef | -6.412 | -43.84426 | 2025-10-03 04:10:00 | NPP-375D | PARAIBANO | MARANHÃO | Brasil | 2107704 | 21 | 33 | nan | nan | nan | Cerrado | 1.4 |
| 802fc199-4738-3dd0-a24f-b781dbd17bf5 | -6.70884 | -42.8046 | 2025-10-03 04:10:00 | NPP-375D | FRANCISCO AYRES | PIAUÍ | Brasil | 2204105 | 22 | 33 | nan | nan | nan | Caatinga | 2.3 |
| 0fb4cff3-8d34-3efc-b767-19bfeb1656a7 | -6.73841 | -44.58991 | 2025-10-03 04:10:00 | NPP-375D | SÃO DOMINGOS DO AZEITÃO | MARANHÃO | Brasil | 2110658 | 21 | 33 | nan | nan | nan | Cerrado | 1.9 |
| abd95a12-3115-363e-8b7e-2e756b9f97ae | -3.84644 | -41.57195 | 2025-10-03 04:10:00 | NPP-375D | PIRACURUCA | PIAUÍ | Brasil | 2208304 | 22 | 33 | nan | nan | nan | Caatinga | 3.8 |
| 5555c553-573e-3150-901c-9e590c508d00 | -7.76537 | -42.60297 | 2025-10-03 04:10:00 | NPP-375D | RIBEIRA DO PIAUÍ | PIAUÍ | Brasil | 2208874 | 22 | 33 | nan | nan | nan | Caatinga | 5.1 |
| 75efb15f-52b5-345b-9ba4-dac426ec8dbe | -6.12536 | -44.03082 | 2025-10-03 04:10:00 | NPP-375D | COLINAS | MARANHÃO | Brasil | 2103505 | 21 | 33 | nan | nan | nan | Cerrado | 0.9 |
| e49766ec-7f7e-377e-a79b-518e43419072 | -7.77821 | -42.58695 | 2025-10-03 04:10:00 | NPP-375D | SOCORRO DO PIAUÍ | PIAUÍ | Brasil | 2210904 | 22 | 33 | nan | nan | nan | Caatinga | 19.5 |
| a31edd37-1f75-35aa-b9f1-fa166c883aff | -0.90053 | -47.54924 | 2025-10-03 04:10:00 | NPP-375D | MARACANÃ | PARÁ | Brasil | 1504307 | 15 | 33 | nan | nan | nan | Amazônia | 3.8 |
| df3730c6-0b7c-316f-acdc-3341cb71e9cf | -7.89045 | -47.34621 | 2025-10-03 04:10:00 | NPP-375D | GOIATINS | TOCANTINS | Brasil | 1709005 | 17 | 33 | nan | nan | nan | Cerrado | 1.6 |
| c7ad911c-032f-3d1c-b00c-2331345d7ca3 | -1.01731 | -47.79158 | 2025-10-03 04:10:00 | NPP-375D | TERRA ALTA | PARÁ | Brasil | 1507961 | 15 | 33 | nan | nan | nan | Amazônia | 2.1 |
| 442e739b-e3b0-353d-b4c6-90dc8b05d02c | -5.63554 | -43.91599 | 2025-10-03 04:10:00 | NPP-375D | FORTUNA | MARANHÃO | Brasil | 2104206 | 21 | 33 | nan | nan | nan | Cerrado | 2.2 |
| e0adabd1-df6e-3496-9242-d16b14ed7f55 | -6.23708 | -44.25582 | 2025-10-03 04:10:00 | NPP-375D | MIRADOR | MARANHÃO | Brasil | 2106706 | 21 | 33 | nan | nan | nan | Cerrado | 3.1 |
| d75b08ca-4596-33e8-a37d-3349bd437a09 | -6.13174 | -44.03603 | 2025-10-03 04:10:00 | NPP-375D | COLINAS | MARANHÃO | Brasil | 2103505 | 21 | 33 | nan | nan | nan | Cerrado | 0.5 |
| b90564b1-0913-313f-9243-c8501836e0a6 | -8.33282 | -46.22703 | 2025-10-03 04:10:00 | NPP-375D | BALSAS | MARANHÃO | Brasil | 2101400 | 21 | 33 | nan | nan | nan | Cerrado | 2.0 |
| b9573afa-8bc9-3767-a2af-8f1530f7a7a1 | -7.79498 | -42.54636 | 2025-10-03 04:10:00 | NPP-375D | SOCORRO DO PIAUÍ | PIAUÍ | Brasil | 2210904 | 22 | 33 | nan | nan | nan | Caatinga | 1.9 |


[Clique aqui para ver as próximas entradas](README49.md)
