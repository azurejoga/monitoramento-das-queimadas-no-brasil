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

## Dados Diários - Página 19

| ID | Latitude | Longitude | Data/Hora GMT | Satélite | Município | Estado | País | Município ID | Estado ID | País ID | Dias sem Chuva | Precipitação | Risco de Fogo | Bioma | FRP |
|----|----------|-----------|---------------|----------|-----------|--------|------|--------------|-----------|---------|----------------|--------------|----------------|-------|-----|
| eefc7125-9841-333d-8dbd-5e9e14984ec9 | -12.89207 | -46.12426 | 2025-08-17 04:14:00 | NOAA-20 | SÃO DESIDÉRIO | BAHIA | Brasil | 2928901 | 29 | 33 | nan | nan | nan | Cerrado | 3.4 |
| cf99d843-d51d-31d4-9385-1d326178f3b8 | -6.45304 | -44.79129 | 2025-08-17 04:14:00 | NOAA-20 | MIRADOR | MARANHÃO | Brasil | 2106706 | 21 | 33 | nan | nan | nan | Cerrado | 1.2 |
| e5ba4929-4238-3ca7-97ce-ff511df1d61a | -11.35786 | -55.39097 | 2025-08-17 04:14:00 | NOAA-20 | CLÁUDIA | MATO GROSSO | Brasil | 5103056 | 51 | 33 | nan | nan | nan | Amazônia | 7.6 |
| 9167ea88-37b1-3e7a-abd3-8a1baed247e6 | -7.02836 | -44.27866 | 2025-08-17 04:14:00 | NOAA-20 | BENEDITO LEITE | MARANHÃO | Brasil | 2101806 | 21 | 33 | nan | nan | nan | Cerrado | 1.2 |
| 6f4bd6b0-c9c3-3351-8b94-8b5970b9cf6b | -12.89663 | -46.11755 | 2025-08-17 04:14:00 | NOAA-20 | SÃO DESIDÉRIO | BAHIA | Brasil | 2928901 | 29 | 33 | nan | nan | nan | Cerrado | 0.5 |
| 076a2b39-a2cf-309e-9e42-2a0373b33da5 | -12.92692 | -46.12281 | 2025-08-17 04:14:00 | NOAA-20 | CAMPOS BELOS | GOIÁS | Brasil | 5204904 | 52 | 33 | nan | nan | nan | Cerrado | 0.8 |
| 3f537b1c-631f-33d8-bd19-c95596c8b38c | -12.55517 | -46.93749 | 2025-08-17 04:14:00 | NOAA-20 | ARRAIAS | TOCANTINS | Brasil | 1702406 | 17 | 33 | nan | nan | nan | Cerrado | 3.2 |
| 83773fb2-a4b1-3eb3-8bd9-eb92f685a003 | -10.8457 | -45.22253 | 2025-08-17 04:14:00 | NOAA-20 | FORMOSA DO RIO PRETO | BAHIA | Brasil | 2911105 | 29 | 33 | nan | nan | nan | Cerrado | 1.1 |
| acea456a-f5d6-356f-8bf5-1d8af65708b0 | -12.89148 | -46.12791 | 2025-08-17 04:14:00 | NOAA-20 | SÃO DESIDÉRIO | BAHIA | Brasil | 2928901 | 29 | 33 | nan | nan | nan | Cerrado | 1.3 |
| 39117579-c7ff-34cf-b854-5a7846c32eb6 | -10.88018 | -48.49615 | 2025-08-17 04:14:00 | NOAA-20 | BREJINHO DE NAZARÉ | TOCANTINS | Brasil | 1703701 | 17 | 33 | nan | nan | nan | Cerrado | 1.7 |
| 97e46c2a-552b-37ee-bc25-5fd71dd7e498 | -6.72483 | -44.05054 | 2025-08-17 04:14:00 | NOAA-20 | NOVA IORQUE | MARANHÃO | Brasil | 2107308 | 21 | 33 | nan | nan | nan | Cerrado | 2.3 |
| 428a16ea-c980-3a0b-a7e7-0a5718a5f0cf | -10.82509 | -45.32908 | 2025-08-17 04:14:00 | NOAA-20 | FORMOSA DO RIO PRETO | BAHIA | Brasil | 2911105 | 29 | 33 | nan | nan | nan | Cerrado | 1.7 |
| 187ce977-8cc5-37b1-bb30-70941f1efad2 | -10.85518 | -45.33408 | 2025-08-17 04:14:00 | NOAA-20 | FORMOSA DO RIO PRETO | BAHIA | Brasil | 2911105 | 29 | 33 | nan | nan | nan | Cerrado | 1.2 |
| 5190c8fb-faf2-3f7c-a778-fd3164b4bb4e | -10.82451 | -45.33267 | 2025-08-17 04:14:00 | NOAA-20 | FORMOSA DO RIO PRETO | BAHIA | Brasil | 2911105 | 29 | 33 | nan | nan | nan | Cerrado | 1.5 |
| 205a0a23-5c6e-377f-97cf-003668666edf | -7.89381 | -42.12118 | 2025-08-17 04:14:00 | NOAA-20 | SIMPLÍCIO MENDES | PIAUÍ | Brasil | 2210805 | 22 | 33 | nan | nan | nan | Caatinga | 1.0 |
| 96027602-b201-3195-9978-33bca52a58e1 | -7.19726 | -46.2341 | 2025-08-17 04:14:00 | NOAA-20 | NOVA COLINAS | MARANHÃO | Brasil | 2107258 | 21 | 33 | nan | nan | nan | Cerrado | 0.9 |
| 28e88360-36b1-3d23-a25b-07caa6e65982 | -8.79759 | -52.06936 | 2025-08-17 04:14:00 | NOAA-20 | SÃO FÉLIX DO XINGU | PARÁ | Brasil | 1507300 | 15 | 33 | nan | nan | nan | Amazônia | 3.0 |
| 5aef57e1-c080-3ab4-b163-68d8016c84dd | -8.50858 | -44.72976 | 2025-08-17 04:14:00 | NOAA-20 | PALMEIRA DO PIAUÍ | PIAUÍ | Brasil | 2207405 | 22 | 33 | nan | nan | nan | Cerrado | 5.7 |
| 799dd69c-e450-369d-8cce-b63141e279e4 | -9.29024 | -40.24048 | 2025-08-17 04:14:00 | NOAA-20 | JUAZEIRO | BAHIA | Brasil | 2918407 | 29 | 33 | nan | nan | nan | Caatinga | 1.1 |
| fe3e9edb-b55d-3466-9638-5dd82e4c0e5e | -13.64931 | -45.89524 | 2025-08-17 04:14:00 | NOAA-20 | CORRENTINA | BAHIA | Brasil | 2909307 | 29 | 33 | nan | nan | nan | Cerrado | 0.5 |
| 09d79217-b295-36cc-a398-b04bf8670fab | -10.83904 | -45.32771 | 2025-08-17 04:14:00 | NOAA-20 | FORMOSA DO RIO PRETO | BAHIA | Brasil | 2911105 | 29 | 33 | nan | nan | nan | Cerrado | 9.4 |
| 7affe643-dfa8-3bdb-baa7-d1623200dccc | -6.31732 | -45.80761 | 2025-08-17 04:14:00 | NOAA-20 | FERNANDO FALCÃO | MARANHÃO | Brasil | 2104081 | 21 | 33 | nan | nan | nan | Cerrado | 1.3 |
| 24013106-25df-384a-8bdf-3f90ae2c326f | -12.8893 | -46.12 | 2025-08-17 04:14:00 | NOAA-20 | SÃO DESIDÉRIO | BAHIA | Brasil | 2928901 | 29 | 33 | nan | nan | nan | Cerrado | 3.4 |
| c4d0d1ff-e13d-33a9-a54e-4ee20c007f93 | -6.54578 | -43.03344 | 2025-08-17 04:14:00 | NOAA-20 | BARÃO DE GRAJAÚ | MARANHÃO | Brasil | 2101509 | 21 | 33 | nan | nan | nan | Cerrado | 2.7 |
| fecdd78d-fd6a-38ab-baff-f7f8163c4397 | -11.36118 | -55.40562 | 2025-08-17 04:14:00 | NOAA-20 | CLÁUDIA | MATO GROSSO | Brasil | 5103056 | 51 | 33 | nan | nan | nan | Amazônia | 2.0 |
| 7f2ff74c-aea1-3b86-a20f-a7c05fea73f2 | -8.50467 | -44.73277 | 2025-08-17 04:14:00 | NOAA-20 | PALMEIRA DO PIAUÍ | PIAUÍ | Brasil | 2207405 | 22 | 33 | nan | nan | nan | Cerrado | 5.7 |
| c2826227-9b65-32b3-9b34-fcd88fc4a97f | -7.14599 | -44.62493 | 2025-08-17 04:14:00 | NOAA-20 | BENEDITO LEITE | MARANHÃO | Brasil | 2101806 | 21 | 33 | nan | nan | nan | Cerrado | 1.2 |
| 9bfd2d16-2324-3e3c-9730-63edcddbba87 | -7.4189 | -42.02649 | 2025-08-17 04:14:00 | NOAA-20 | SANTO INÁCIO DO PIAUÍ | PIAUÍ | Brasil | 2209500 | 22 | 33 | nan | nan | nan | Caatinga | 1.5 |
| bb0778d4-cc7b-39d5-8569-00347c13efa6 | -13.47174 | -44.08027 | 2025-08-17 04:14:00 | NOAA-20 | SÃO FÉLIX DO CORIBE | BAHIA | Brasil | 2929057 | 29 | 33 | nan | nan | nan | Cerrado | 0.9 |
| f3982843-8ae6-3a1d-b71a-dd5e82989f2c | -8.5736 | -39.42671 | 2025-08-17 04:14:00 | NOAA-20 | CURAÇÁ | BAHIA | Brasil | 2909901 | 29 | 33 | nan | nan | nan | Caatinga | 2.7 |
| abc8bde6-c7df-3286-8af5-6d19cf5f17a9 | -12.84563 | -46.0487 | 2025-08-17 04:14:00 | NOAA-20 | SÃO DESIDÉRIO | BAHIA | Brasil | 2928901 | 29 | 33 | nan | nan | nan | Cerrado | 1.0 |
| 4414880a-e3e2-3781-9d3a-420032944a9c | -7.53123 | -36.73022 | 2025-08-17 04:14:00 | NOAA-20 | SERRA BRANCA | PARAÍBA | Brasil | 2515500 | 25 | 33 | nan | nan | nan | Caatinga | 1.0 |
| bfed80c8-12d7-313e-8b55-b15c8491fd46 | -13.09619 | -46.84727 | 2025-08-17 04:14:00 | NOAA-20 | MONTE ALEGRE DE GOIÁS | GOIÁS | Brasil | 5213509 | 52 | 33 | nan | nan | nan | Cerrado | 1.1 |
| 077f8314-f076-3a18-bb1c-2a1226263a27 | -6.18981 | -45.44918 | 2025-08-17 04:14:00 | NOAA-20 | FERNANDO FALCÃO | MARANHÃO | Brasil | 2104081 | 21 | 33 | nan | nan | nan | Cerrado | 2.7 |
| 51ba2405-24e2-3d6b-b629-92ba7903d0a4 | -10.8366 | -45.36416 | 2025-08-17 04:14:00 | NOAA-20 | FORMOSA DO RIO PRETO | BAHIA | Brasil | 2911105 | 29 | 33 | nan | nan | nan | Cerrado | 7.2 |
| 1ac13407-b98f-3ffc-8038-0c6e06ea97e6 | -10.83442 | -45.35641 | 2025-08-17 04:14:00 | NOAA-20 | FORMOSA DO RIO PRETO | BAHIA | Brasil | 2911105 | 29 | 33 | nan | nan | nan | Cerrado | 0.9 |
| f2dfaf5a-3cb1-378d-b6fe-19853209c10b | -13.42943 | -45.88853 | 2025-08-17 04:14:00 | NOAA-20 | CORRENTINA | BAHIA | Brasil | 2909307 | 29 | 33 | nan | nan | nan | Cerrado | 2.1 |
| b01b7b11-2c61-3ba8-a32b-a96c6c6c1023 | -9.9463 | -47.95852 | 2025-08-17 04:14:00 | NOAA-20 | APARECIDA DO RIO NEGRO | TOCANTINS | Brasil | 1701101 | 17 | 33 | nan | nan | nan | Cerrado | 1.6 |
| 4d93349e-0449-3728-b21c-7d53aa818a3c | -12.34455 | -45.78622 | 2025-08-17 04:14:00 | NOAA-20 | LUÍS EDUARDO MAGALHÃES | BAHIA | Brasil | 2919553 | 29 | 33 | nan | nan | nan | Cerrado | 0.3 |
| 8b04fc0f-94db-313d-8efc-a0ecc86da002 | -8.81747 | -52.04506 | 2025-08-17 04:14:00 | NOAA-20 | SÃO FÉLIX DO XINGU | PARÁ | Brasil | 1507300 | 15 | 33 | nan | nan | nan | Amazônia | 1.2 |
| d6191d6f-073d-3eb8-846c-53adba8b5c37 | -12.83519 | -46.01698 | 2025-08-17 04:14:00 | NOAA-20 | SÃO DESIDÉRIO | BAHIA | Brasil | 2928901 | 29 | 33 | nan | nan | nan | Cerrado | 0.8 |
| dde392fb-6a7d-3c6b-b7d9-f551ddc5f421 | -8.50687 | -44.74043 | 2025-08-17 04:14:00 | NOAA-20 | PALMEIRA DO PIAUÍ | PIAUÍ | Brasil | 2207405 | 22 | 33 | nan | nan | nan | Cerrado | 3.9 |
| 17f69ee0-e462-3e3d-8105-99c5dbd55d52 | -10.31352 | -54.16251 | 2025-08-17 04:14:00 | NOAA-20 | PEIXOTO DE AZEVEDO | MATO GROSSO | Brasil | 5106422 | 51 | 33 | nan | nan | nan | Amazônia | 4.3 |
| ea7a36c5-7040-38f7-8ef6-3c4ba245b7ff | -6.80507 | -44.71737 | 2025-08-17 04:14:00 | NOAA-20 | SÃO DOMINGOS DO AZEITÃO | MARANHÃO | Brasil | 2110658 | 21 | 33 | nan | nan | nan | Cerrado | 1.1 |
| 40eb4e92-65b6-3e01-a74c-280136c7c643 | -6.55511 | -43.01719 | 2025-08-17 04:14:00 | NOAA-20 | BARÃO DE GRAJAÚ | MARANHÃO | Brasil | 2101509 | 21 | 33 | nan | nan | nan | Cerrado | 3.4 |
| 8b053f13-08ec-355c-8b64-129896727fcc | -12.85572 | -46.0504 | 2025-08-17 04:14:00 | NOAA-20 | SÃO DESIDÉRIO | BAHIA | Brasil | 2928901 | 29 | 33 | nan | nan | nan | Cerrado | 0.8 |
| b1bc8625-093a-35fd-8bd8-35b4cddcfee3 | -12.85295 | -46.04617 | 2025-08-17 04:14:00 | NOAA-20 | SÃO DESIDÉRIO | BAHIA | Brasil | 2928901 | 29 | 33 | nan | nan | nan | Cerrado | 0.8 |
| ad5eec6d-e1b9-34ef-8690-e7b2b130580e | -10.82959 | -45.32246 | 2025-08-17 04:14:00 | NOAA-20 | FORMOSA DO RIO PRETO | BAHIA | Brasil | 2911105 | 29 | 33 | nan | nan | nan | Cerrado | 2.0 |
| 4788989a-4d44-30b9-8f67-cbff29ac0aed | -14.20219 | -42.78127 | 2025-08-17 04:14:00 | NOAA-20 | GUANAMBI | BAHIA | Brasil | 2911709 | 29 | 33 | nan | nan | nan | Caatinga | 0.4 |
| 1581140a-01a3-3854-a7d6-ad26656fefb7 | -10.83351 | -45.31943 | 2025-08-17 04:14:00 | NOAA-20 | FORMOSA DO RIO PRETO | BAHIA | Brasil | 2911105 | 29 | 33 | nan | nan | nan | Cerrado | 2.0 |
| e81e9ad5-21b3-3aae-94c5-bbf40a9c1475 | -11.35296 | -55.4005 | 2025-08-17 04:14:00 | NOAA-20 | CLÁUDIA | MATO GROSSO | Brasil | 5103056 | 51 | 33 | nan | nan | nan | Amazônia | 3.2 |
| c109fe8d-de09-3b3f-a7c8-06f1472d647f | -13.01364 | -42.32828 | 2025-08-17 04:14:00 | NOAA-20 | IBIPITANGA | BAHIA | Brasil | 2912509 | 29 | 33 | nan | nan | nan | Caatinga | 7.9 |
| 48d21384-bf00-30ee-9c9d-1dc5ac2ac75b | -7.60095 | -44.94103 | 2025-08-17 04:14:00 | NOAA-20 | URUÇUÍ | PIAUÍ | Brasil | 2211209 | 22 | 33 | nan | nan | nan | Cerrado | 1.5 |
| dd05c741-ce44-3f3c-a2ba-ebd9d7c51b48 | -10.83937 | -45.36832 | 2025-08-17 04:14:00 | NOAA-20 | FORMOSA DO RIO PRETO | BAHIA | Brasil | 2911105 | 29 | 33 | nan | nan | nan | Cerrado | 7.2 |
| 2d418c9c-2079-3b05-9cce-ae3af5b1efe8 | -11.35974 | -55.3975 | 2025-08-17 04:14:00 | NOAA-20 | CLÁUDIA | MATO GROSSO | Brasil | 5103056 | 51 | 33 | nan | nan | nan | Amazônia | 3.2 |
| 288627c8-adf4-3ea7-876e-af7a8ff33cd4 | -13.56362 | -46.98944 | 2025-08-17 04:14:00 | NOAA-20 | NOVA ROMA | GOIÁS | Brasil | 5214903 | 52 | 33 | nan | nan | nan | Cerrado | 1.2 |
| 8b38e0b1-c918-314e-9e7b-81270832e5c6 | -10.84342 | -45.34317 | 2025-08-17 04:14:00 | NOAA-20 | FORMOSA DO RIO PRETO | BAHIA | Brasil | 2911105 | 29 | 33 | nan | nan | nan | Cerrado | 2.1 |
| ed46901a-e99b-388b-ac11-087ed3157790 | -12.85848 | -46.05462 | 2025-08-17 04:14:00 | NOAA-20 | SÃO DESIDÉRIO | BAHIA | Brasil | 2928901 | 29 | 33 | nan | nan | nan | Cerrado | 0.4 |
| 63bfdf82-a780-3f4e-8549-515071c01986 | -8.80447 | -52.03137 | 2025-08-17 04:14:00 | NOAA-20 | SÃO FÉLIX DO XINGU | PARÁ | Brasil | 1507300 | 15 | 33 | nan | nan | nan | Amazônia | 1.4 |
| 25061295-a6f5-3768-ab06-8a9c2f2f71ed | -11.89927 | -43.42808 | 2025-08-17 04:14:00 | NOAA-20 | MUQUÉM DO SÃO FRANCISCO | BAHIA | Brasil | 2922250 | 29 | 33 | nan | nan | nan | Cerrado | 2.3 |
| 853d5bf9-9acc-3119-a8d3-413819ef9f77 | -6.54686 | -43.02652 | 2025-08-17 04:14:00 | NOAA-20 | BARÃO DE GRAJAÚ | MARANHÃO | Brasil | 2101509 | 21 | 33 | nan | nan | nan | Cerrado | 10.3 |
| f9751cd8-3190-3f0e-b3d2-2891ae725975 | -6.25564 | -45.38468 | 2025-08-17 04:14:00 | NOAA-20 | FERNANDO FALCÃO | MARANHÃO | Brasil | 2104081 | 21 | 33 | nan | nan | nan | Cerrado | 1.2 |
| a266f36e-11c4-37e6-bccb-c0490840d65b | -7.09789 | -41.33305 | 2025-08-17 04:14:00 | NOAA-20 | SUSSUAPARA | PIAUÍ | Brasil | 2210938 | 22 | 33 | nan | nan | nan | Caatinga | 0.7 |
| caca2974-d068-382d-8b9c-c9786dc897db | -13.43494 | -45.89688 | 2025-08-17 04:14:00 | NOAA-20 | CORRENTINA | BAHIA | Brasil | 2909307 | 29 | 33 | nan | nan | nan | Cerrado | 1.3 |
| 22424604-9de7-3c7c-ba4c-53907f1bf7a0 | -6.54908 | -43.03395 | 2025-08-17 04:14:00 | NOAA-20 | BARÃO DE GRAJAÚ | MARANHÃO | Brasil | 2101509 | 21 | 33 | nan | nan | nan | Cerrado | 2.7 |
| 4a9c8d76-0c60-3fc2-bb6a-9d197285823a | -13.56427 | -46.98554 | 2025-08-17 04:14:00 | NOAA-20 | NOVA ROMA | GOIÁS | Brasil | 5214903 | 52 | 33 | nan | nan | nan | Cerrado | 1.5 |
| e9e8957f-0f8b-3112-a2e0-85bb0de261c3 | -12.56151 | -46.94226 | 2025-08-17 04:14:00 | NOAA-20 | ARRAIAS | TOCANTINS | Brasil | 1702406 | 17 | 33 | nan | nan | nan | Cerrado | 2.5 |
| 1700e0e8-ae64-3c1e-a319-8afd8785b435 | -6.9863 | -42.78008 | 2025-08-17 04:14:00 | NOAA-20 | NAZARÉ DO PIAUÍ | PIAUÍ | Brasil | 2206704 | 22 | 33 | nan | nan | nan | Caatinga | 1.4 |
| 7c46dcce-6231-3998-90eb-791f9b58f3e3 | -7.20083 | -46.23454 | 2025-08-17 04:14:00 | NOAA-20 | NOVA COLINAS | MARANHÃO | Brasil | 2107258 | 21 | 33 | nan | nan | nan | Cerrado | 2.3 |
| 4263f375-2a95-30e3-843e-2a11499c0e5f | -12.84959 | -46.04562 | 2025-08-17 04:14:00 | NOAA-20 | SÃO DESIDÉRIO | BAHIA | Brasil | 2928901 | 29 | 33 | nan | nan | nan | Cerrado | 1.0 |
| 10cc337a-59f6-3f40-ac78-e4019c7962d5 | -12.12299 | -47.90987 | 2025-08-17 04:14:00 | NOAA-20 | PARANÃ | TOCANTINS | Brasil | 1716208 | 17 | 33 | nan | nan | nan | Cerrado | 1.2 |
| c32d27fd-6a72-3dc1-974c-1b81ccd43833 | -12.55107 | -46.9407 | 2025-08-17 04:14:00 | NOAA-20 | ARRAIAS | TOCANTINS | Brasil | 1702406 | 17 | 33 | nan | nan | nan | Cerrado | 5.1 |
| b5b4f055-be5e-397d-8b8f-60558c2573bb | -8.50133 | -44.73223 | 2025-08-17 04:14:00 | NOAA-20 | PALMEIRA DO PIAUÍ | PIAUÍ | Brasil | 2207405 | 22 | 33 | nan | nan | nan | Cerrado | 2.0 |
| 19adbdcf-a0ac-3fe2-841b-2a9d13f88528 | -9.64057 | -50.89384 | 2025-08-17 04:14:00 | NOAA-20 | SANTANA DO ARAGUAIA | PARÁ | Brasil | 1506708 | 15 | 33 | nan | nan | nan | Amazônia | 1.7 |
| 2df4fbcb-8eb1-3b72-afda-76c31ca084f2 | -10.99718 | -45.63095 | 2025-08-17 04:14:00 | NOAA-20 | FORMOSA DO RIO PRETO | BAHIA | Brasil | 2911105 | 29 | 33 | nan | nan | nan | Cerrado | 1.0 |
| 509c9ca3-7758-3ec4-aa76-bbc90c10361e | -7.20349 | -46.21834 | 2025-08-17 04:14:00 | NOAA-20 | NOVA COLINAS | MARANHÃO | Brasil | 2107258 | 21 | 33 | nan | nan | nan | Cerrado | 2.0 |
| e9401253-df36-32f9-84c8-826f231ba33c | -10.84619 | -45.3473 | 2025-08-17 04:14:00 | NOAA-20 | FORMOSA DO RIO PRETO | BAHIA | Brasil | 2911105 | 29 | 33 | nan | nan | nan | Cerrado | 2.3 |
| e8a77676-1aa1-36bb-b44c-3dea64e763a0 | -6.53333 | -44.54905 | 2025-08-17 04:14:00 | NOAA-20 | MIRADOR | MARANHÃO | Brasil | 2106706 | 21 | 33 | nan | nan | nan | Cerrado | 0.8 |
| bf7e0d7e-3ff1-35a4-86f1-efb2f8c3e39a | -10.83293 | -45.32301 | 2025-08-17 04:14:00 | NOAA-20 | FORMOSA DO RIO PRETO | BAHIA | Brasil | 2911105 | 29 | 33 | nan | nan | nan | Cerrado | 2.0 |
| 89002cf3-4123-3f7b-bf2b-33bbe0c245ca | -6.18696 | -45.44471 | 2025-08-17 04:14:00 | NOAA-20 | FERNANDO FALCÃO | MARANHÃO | Brasil | 2104081 | 21 | 33 | nan | nan | nan | Cerrado | 1.6 |
| 1b07e1af-a55c-3441-bbdc-470f065ce5a7 | -7.15347 | -44.38554 | 2025-08-17 04:14:00 | NOAA-20 | URUÇUÍ | PIAUÍ | Brasil | 2211209 | 22 | 33 | nan | nan | nan | Cerrado | 3.4 |
| 4c5d65b4-7597-3674-a439-a83362d57734 | -10.84677 | -45.34372 | 2025-08-17 04:14:00 | NOAA-20 | FORMOSA DO RIO PRETO | BAHIA | Brasil | 2911105 | 29 | 33 | nan | nan | nan | Cerrado | 2.3 |
| 64eb3ed0-8a92-3aed-ae0c-55a4e9d8d725 | -9.69361 | -46.26389 | 2025-08-17 04:14:00 | NOAA-20 | ALTO PARNAÍBA | MARANHÃO | Brasil | 2100501 | 21 | 33 | nan | nan | nan | Cerrado | 1.5 |
| 6336e26b-b451-371c-9753-0bae1c889b39 | -10.82901 | -45.32604 | 2025-08-17 04:14:00 | NOAA-20 | FORMOSA DO RIO PRETO | BAHIA | Brasil | 2911105 | 29 | 33 | nan | nan | nan | Cerrado | 1.3 |
| 59c178d2-6b4f-35d5-974b-57da5334beef | -6.48941 | -42.96079 | 2025-08-17 04:14:00 | NOAA-20 | BARÃO DE GRAJAÚ | MARANHÃO | Brasil | 2101509 | 21 | 33 | nan | nan | nan | Cerrado | 0.9 |
| 8f46400e-fe45-39f1-83dc-5ca307e71da1 | -8.21853 | -47.31095 | 2025-08-17 04:14:00 | NOAA-20 | GOIATINS | TOCANTINS | Brasil | 1709005 | 17 | 33 | nan | nan | nan | Cerrado | 1.3 |
| e50fe239-141a-3c84-8d66-5eb2fce18e5f | -9.611 | -40.34573 | 2025-08-17 04:14:00 | NOAA-20 | JUAZEIRO | BAHIA | Brasil | 2918407 | 29 | 33 | nan | nan | nan | Caatinga | 5.7 |
| 191e035b-f55f-38ed-8ec9-91e6a7e1781c | -12.89999 | -46.11813 | 2025-08-17 04:14:00 | NOAA-20 | SÃO DESIDÉRIO | BAHIA | Brasil | 2928901 | 29 | 33 | nan | nan | nan | Cerrado | 0.5 |
| d6c967ea-cca5-3c94-85ad-aa241fab6d49 | -11.5653 | -47.26297 | 2025-08-17 04:14:00 | NOAA-20 | ALMAS | TOCANTINS | Brasil | 1700400 | 17 | 33 | nan | nan | nan | Cerrado | 0.9 |
| 672495b5-ba13-3f0b-9b67-bc1f6699bf20 | -7.07759 | -44.94285 | 2025-08-17 04:14:00 | NOAA-20 | SÃO FÉLIX DE BALSAS | MARANHÃO | Brasil | 2110807 | 21 | 33 | nan | nan | nan | Cerrado | 1.2 |
| 8909f8a5-7457-38ff-8615-8ec38bb68b18 | -7.62164 | -44.96297 | 2025-08-17 04:14:00 | NOAA-20 | RIBEIRO GONÇALVES | PIAUÍ | Brasil | 2208908 | 22 | 33 | nan | nan | nan | Cerrado | 1.9 |
| 87bd03d3-33f6-3fe2-98bc-823fc9449b34 | -10.84961 | -45.2195 | 2025-08-17 04:14:00 | NOAA-20 | FORMOSA DO RIO PRETO | BAHIA | Brasil | 2911105 | 29 | 33 | nan | nan | nan | Cerrado | 1.1 |
| 16204153-c1d5-3924-9ad3-c4ea59890993 | -13.44789 | -45.88052 | 2025-08-17 04:14:00 | NOAA-20 | CORRENTINA | BAHIA | Brasil | 2909307 | 29 | 33 | nan | nan | nan | Cerrado | 4.9 |
| f44d7264-6b73-3dac-bdc1-96ff377efa99 | -7.14149 | -44.63153 | 2025-08-17 04:14:00 | NOAA-20 | BENEDITO LEITE | MARANHÃO | Brasil | 2101806 | 21 | 33 | nan | nan | nan | Cerrado | 1.8 |
| 8bedb6f7-f0eb-3c71-8243-f8e9c627bfb6 | -12.86618 | -46.07094 | 2025-08-17 04:14:00 | NOAA-20 | SÃO DESIDÉRIO | BAHIA | Brasil | 2928901 | 29 | 33 | nan | nan | nan | Cerrado | 1.6 |
| d1dd58da-a079-3ba8-8d02-1fea0918ffc7 | -7.20283 | -46.22239 | 2025-08-17 04:14:00 | NOAA-20 | NOVA COLINAS | MARANHÃO | Brasil | 2107258 | 21 | 33 | nan | nan | nan | Cerrado | 3.3 |
| b5584d80-5bbe-311f-a2de-679540ced422 | -7.0413 | -42.20636 | 2025-08-17 04:14:00 | NOAA-20 | OEIRAS | PIAUÍ | Brasil | 2207009 | 22 | 33 | nan | nan | nan | Caatinga | 4.1 |
| d70c5601-036f-338f-bf31-6456cbbcc563 | -7.14264 | -44.62438 | 2025-08-17 04:14:00 | NOAA-20 | BENEDITO LEITE | MARANHÃO | Brasil | 2101806 | 21 | 33 | nan | nan | nan | Cerrado | 1.2 |
| 3d40d5ec-7e63-3b21-b4d3-f1195fffbd34 | -12.61204 | -46.90632 | 2025-08-17 04:14:00 | NOAA-20 | ARRAIAS | TOCANTINS | Brasil | 1702406 | 17 | 33 | nan | nan | nan | Cerrado | 3.2 |
| fce0435c-fbf0-3594-83de-9dce1580ee10 | -10.84284 | -45.34675 | 2025-08-17 04:14:00 | NOAA-20 | FORMOSA DO RIO PRETO | BAHIA | Brasil | 2911105 | 29 | 33 | nan | nan | nan | Cerrado | 2.1 |


[Clique aqui para ver as próximas entradas](README20.md)
