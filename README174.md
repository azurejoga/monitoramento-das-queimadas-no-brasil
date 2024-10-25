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

## Dados Diários - Página 174

| ID | Latitude | Longitude | Data/Hora GMT | Satélite | Município | Estado | País | Município ID | Estado ID | País ID | Dias sem Chuva | Precipitação | Risco de Fogo | Bioma | FRP |
|----|----------|-----------|---------------|----------|-----------|--------|------|--------------|-----------|---------|----------------|--------------|----------------|-------|-----|
| 08c2adb8-4026-3cf7-bc1d-2d233d3efa2e | -5.51917 | -45.85914 | 2024-10-25 16:52:00 | NOAA-21 | GRAJAÚ | MARANHÃO | Brasil | 2104800 | 21 | 33 | nan | nan | nan | Cerrado | 8.1 |
| 1743663a-550b-3a67-9e08-ceb749b68d1d | -5.51519 | -45.85975 | 2024-10-25 16:52:00 | NOAA-21 | GRAJAÚ | MARANHÃO | Brasil | 2104800 | 21 | 33 | nan | nan | nan | Cerrado | 8.1 |
| 49742d8a-ca8e-3bb0-88fb-61d96a78f10c | -5.47959 | -45.51858 | 2024-10-25 16:52:00 | NOAA-21 | JENIPAPO DOS VIEIRAS | MARANHÃO | Brasil | 2105476 | 21 | 33 | nan | nan | nan | Cerrado | 2.3 |
| 73b591f5-8d7c-311f-a7c7-7a0103331cf6 | -5.35368 | -45.69732 | 2024-10-25 16:52:00 | NOAA-21 | JENIPAPO DOS VIEIRAS | MARANHÃO | Brasil | 2105476 | 21 | 33 | nan | nan | nan | Cerrado | 6.1 |
| 8dd68f5d-26f7-371e-b6c0-e9cdf5519412 | -5.34964 | -45.69789 | 2024-10-25 16:52:00 | NOAA-21 | JENIPAPO DOS VIEIRAS | MARANHÃO | Brasil | 2105476 | 21 | 33 | nan | nan | nan | Cerrado | 5.7 |
| 1169cf2c-1d61-3136-beef-80d74bec97d1 | -5.31789 | -45.42579 | 2024-10-25 16:52:00 | NOAA-21 | BARRA DO CORDA | MARANHÃO | Brasil | 2101608 | 21 | 33 | nan | nan | nan | Cerrado | 4.7 |
| 226c4736-d73b-387e-8c04-be50e97d061a | -5.11783 | -46.18518 | 2024-10-25 16:52:00 | NOAA-21 | ARAME | MARANHÃO | Brasil | 2100956 | 21 | 33 | nan | nan | nan | Amazônia | 7.8 |
| 8da8e61a-6f4b-31cb-8387-5e3678476961 | -5.11736 | -46.18275 | 2024-10-25 16:52:00 | NOAA-21 | ARAME | MARANHÃO | Brasil | 2100956 | 21 | 33 | nan | nan | nan | Amazônia | 4.6 |
| e747c598-dd31-350f-a77d-224eb44b928f | -5.08012 | -45.8828 | 2024-10-25 16:52:00 | NOAA-21 | ARAME | MARANHÃO | Brasil | 2100956 | 21 | 33 | nan | nan | nan | Amazônia | 17.9 |
| 367c1786-71ba-3b5e-9660-0a2d3c69486f | -5.07953 | -45.87927 | 2024-10-25 16:52:00 | NOAA-21 | ARAME | MARANHÃO | Brasil | 2100956 | 21 | 33 | nan | nan | nan | Amazônia | 6.9 |
| 491670b6-87cd-39b6-9089-db95e7931d73 | -5.07612 | -45.88344 | 2024-10-25 16:52:00 | NOAA-21 | ARAME | MARANHÃO | Brasil | 2100956 | 21 | 33 | nan | nan | nan | Amazônia | 17.9 |
| 3bbfc42e-6b02-3877-a438-c431fe2eeed3 | -6.50837 | -45.26994 | 2024-10-25 16:52:00 | NOAA-21 | MIRADOR | MARANHÃO | Brasil | 2106706 | 21 | 33 | nan | nan | nan | Cerrado | 15.5 |
| 29c4d961-20ae-35dd-95e4-68e69adf803f | -6.3995 | -46.24778 | 2024-10-25 16:52:00 | NOAA-21 | FORMOSA DA SERRA NEGRA | MARANHÃO | Brasil | 2104099 | 21 | 33 | nan | nan | nan | Cerrado | 24.6 |
| 995e690f-e342-3ba9-bd98-c6515d8efff6 | -6.39873 | -46.24302 | 2024-10-25 16:52:00 | NOAA-21 | FORMOSA DA SERRA NEGRA | MARANHÃO | Brasil | 2104099 | 21 | 33 | nan | nan | nan | Cerrado | 20.7 |
| 427bbf8e-ffdb-3368-a72c-05b678b6686e | -6.3949 | -46.24364 | 2024-10-25 16:52:00 | NOAA-21 | FORMOSA DA SERRA NEGRA | MARANHÃO | Brasil | 2104099 | 21 | 33 | nan | nan | nan | Cerrado | 20.7 |
| cc394aaf-2af2-34fc-bcd5-0ecbe975a5d7 | -6.32907 | -46.10616 | 2024-10-25 16:52:00 | NOAA-21 | FORMOSA DA SERRA NEGRA | MARANHÃO | Brasil | 2104099 | 21 | 33 | nan | nan | nan | Cerrado | 5.7 |
| 4028731a-7bca-37cb-ae27-d4af2059f768 | -6.28076 | -45.51373 | 2024-10-25 16:52:00 | NOAA-21 | FERNANDO FALCÃO | MARANHÃO | Brasil | 2104081 | 21 | 33 | nan | nan | nan | Cerrado | 4.0 |
| b81f4906-30ae-3b89-9f93-64de71f424e2 | -6.28016 | -45.51006 | 2024-10-25 16:52:00 | NOAA-21 | FERNANDO FALCÃO | MARANHÃO | Brasil | 2104081 | 21 | 33 | nan | nan | nan | Cerrado | 4.0 |
| f0348f41-dfaa-3ea0-a425-9bfd53b68ae6 | -6.09553 | -46.1296 | 2024-10-25 16:52:00 | NOAA-21 | GRAJAÚ | MARANHÃO | Brasil | 2104800 | 21 | 33 | nan | nan | nan | Cerrado | 25.0 |
| cf1b239a-a7a5-3454-8e33-df7b28fa6ca6 | -6.00442 | -45.94449 | 2024-10-25 16:52:00 | NOAA-21 | GRAJAÚ | MARANHÃO | Brasil | 2104800 | 21 | 33 | nan | nan | nan | Cerrado | 6.1 |
| 454c89d7-7e13-3c96-8750-c79404f47795 | -5.95532 | -45.64312 | 2024-10-25 16:52:00 | NOAA-21 | GRAJAÚ | MARANHÃO | Brasil | 2104800 | 21 | 33 | nan | nan | nan | Cerrado | 4.5 |
| cd00856d-7bea-3ccc-b7d4-e2c451d88ad8 | -5.94736 | -46.18896 | 2024-10-25 16:52:00 | NOAA-21 | GRAJAÚ | MARANHÃO | Brasil | 2104800 | 21 | 33 | nan | nan | nan | Cerrado | 15.3 |
| cfe13a34-930d-3a1f-9318-45d08fc8866b | -5.94136 | -45.37876 | 2024-10-25 16:52:00 | NOAA-21 | FERNANDO FALCÃO | MARANHÃO | Brasil | 2104081 | 21 | 33 | nan | nan | nan | Cerrado | 2.4 |
| 7073c51f-4bb3-38d0-b160-5ae045cec47d | -5.9048 | -45.56158 | 2024-10-25 16:52:00 | NOAA-21 | GRAJAÚ | MARANHÃO | Brasil | 2104800 | 21 | 33 | nan | nan | nan | Cerrado | 4.5 |
| 8f1bb243-68fe-35c7-83c9-7373ff804b12 | -5.88415 | -46.37431 | 2024-10-25 16:52:00 | NOAA-21 | GRAJAÚ | MARANHÃO | Brasil | 2104800 | 21 | 33 | nan | nan | nan | Cerrado | 13.8 |
| 603e1cc5-749e-3d51-88d9-3987f0c17ea5 | -5.86499 | -46.14748 | 2024-10-25 16:52:00 | NOAA-21 | GRAJAÚ | MARANHÃO | Brasil | 2104800 | 21 | 33 | nan | nan | nan | Cerrado | 40.0 |
| 8b437e65-de12-312c-85ed-ab3fe25ba2d9 | -5.86336 | -46.14475 | 2024-10-25 16:52:00 | NOAA-21 | GRAJAÚ | MARANHÃO | Brasil | 2104800 | 21 | 33 | nan | nan | nan | Cerrado | 7.5 |
| 5ad2a672-464b-356d-a54f-783a0c862e6b | -5.77407 | -45.22507 | 2024-10-25 16:52:00 | NOAA-21 | BARRA DO CORDA | MARANHÃO | Brasil | 2101608 | 21 | 33 | nan | nan | nan | Cerrado | 6.4 |
| 43939892-27ff-3259-bedd-d0b44cdde16d | -5.6923 | -45.54133 | 2024-10-25 16:52:00 | NOAA-21 | BARRA DO CORDA | MARANHÃO | Brasil | 2101608 | 21 | 33 | nan | nan | nan | Cerrado | 3.1 |
| b8d0930c-0c04-3fd2-a463-e9dc871d724f | -5.68824 | -45.5419 | 2024-10-25 16:52:00 | NOAA-21 | BARRA DO CORDA | MARANHÃO | Brasil | 2101608 | 21 | 33 | nan | nan | nan | Cerrado | 3.1 |
| a37d3383-c04d-3647-bdde-e0d1c6531144 | -7.80925 | -46.87678 | 2024-10-25 16:52:00 | NOAA-21 | CAROLINA | MARANHÃO | Brasil | 2102804 | 21 | 33 | nan | nan | nan | Cerrado | 10.7 |
| 02cef1c3-040b-335b-afbf-243e8f179804 | -7.76709 | -46.61424 | 2024-10-25 16:52:00 | NOAA-21 | RIACHÃO | MARANHÃO | Brasil | 2109502 | 21 | 33 | nan | nan | nan | Cerrado | 79.6 |
| 42a01adc-dcd1-33e2-8950-577e1ba3535b | -7.76139 | -46.78835 | 2024-10-25 16:52:00 | NOAA-21 | RIACHÃO | MARANHÃO | Brasil | 2109502 | 21 | 33 | nan | nan | nan | Cerrado | 3.3 |
| bd17a5dc-63aa-3ab1-b18f-77a703661a46 | -7.72942 | -46.77604 | 2024-10-25 16:52:00 | NOAA-21 | RIACHÃO | MARANHÃO | Brasil | 2109502 | 21 | 33 | nan | nan | nan | Cerrado | 4.8 |
| cdd8e626-ccb7-3b00-9396-832f2afc28af | -7.7023 | -46.63396 | 2024-10-25 16:52:00 | NOAA-21 | RIACHÃO | MARANHÃO | Brasil | 2109502 | 21 | 33 | nan | nan | nan | Cerrado | 65.1 |
| a400cf0a-7fda-36c7-b0c7-3e83e9c1e7af | -7.69934 | -46.63889 | 2024-10-25 16:52:00 | NOAA-21 | RIACHÃO | MARANHÃO | Brasil | 2109502 | 21 | 33 | nan | nan | nan | Cerrado | 15.5 |
| 9f63a18d-df5c-34fc-b1a5-6c109e40ef82 | -7.68351 | -46.81792 | 2024-10-25 16:52:00 | NOAA-21 | RIACHÃO | MARANHÃO | Brasil | 2109502 | 21 | 33 | nan | nan | nan | Cerrado | 11.0 |
| 7d6868a3-77d6-3b04-a90b-896d2b0351b9 | -7.67424 | -46.87625 | 2024-10-25 16:52:00 | NOAA-21 | RIACHÃO | MARANHÃO | Brasil | 2109502 | 21 | 33 | nan | nan | nan | Cerrado | 13.1 |
| ca1ec339-9040-3541-8ae4-e4d1c4a1e1c9 | -7.66766 | -46.88168 | 2024-10-25 16:52:00 | NOAA-21 | RIACHÃO | MARANHÃO | Brasil | 2109502 | 21 | 33 | nan | nan | nan | Cerrado | 21.3 |
| 25946515-121c-335a-87b2-b317975cebc7 | -7.66021 | -46.62621 | 2024-10-25 16:52:00 | NOAA-21 | RIACHÃO | MARANHÃO | Brasil | 2109502 | 21 | 33 | nan | nan | nan | Cerrado | 3.4 |
| b9505c0c-5a75-3418-829e-77500fe8f80b | -7.65214 | -46.62309 | 2024-10-25 16:52:00 | NOAA-21 | RIACHÃO | MARANHÃO | Brasil | 2109502 | 21 | 33 | nan | nan | nan | Cerrado | 8.9 |
| 22a1109c-20dd-3f70-b7d0-d59fa0f9f58f | -7.62161 | -46.69081 | 2024-10-25 16:52:00 | NOAA-21 | RIACHÃO | MARANHÃO | Brasil | 2109502 | 21 | 33 | nan | nan | nan | Cerrado | 7.6 |
| 693480b2-a844-3111-870f-ff4270f5e5e2 | -7.61794 | -46.69142 | 2024-10-25 16:52:00 | NOAA-21 | RIACHÃO | MARANHÃO | Brasil | 2109502 | 21 | 33 | nan | nan | nan | Cerrado | 7.6 |
| 4cf66a46-1017-3df7-90dd-d0e8a24cb540 | -7.56307 | -46.79166 | 2024-10-25 16:52:00 | NOAA-21 | RIACHÃO | MARANHÃO | Brasil | 2109502 | 21 | 33 | nan | nan | nan | Cerrado | 11.9 |
| dd18c078-e0d4-35cd-8ccd-457778710331 | -7.56011 | -46.79657 | 2024-10-25 16:52:00 | NOAA-21 | RIACHÃO | MARANHÃO | Brasil | 2109502 | 21 | 33 | nan | nan | nan | Cerrado | 23.5 |
| af67ae9a-604b-3a18-986d-9293bf6149c7 | -7.55941 | -46.79226 | 2024-10-25 16:52:00 | NOAA-21 | RIACHÃO | MARANHÃO | Brasil | 2109502 | 21 | 33 | nan | nan | nan | Cerrado | 12.0 |
| 6b2c226d-61ca-349c-84fe-0539fa5a5009 | -7.53905 | -46.78241 | 2024-10-25 16:52:00 | NOAA-21 | RIACHÃO | MARANHÃO | Brasil | 2109502 | 21 | 33 | nan | nan | nan | Cerrado | 10.5 |
| 927cfe20-3cdb-3123-8335-c25120ae1424 | -7.52354 | -46.68705 | 2024-10-25 16:52:00 | NOAA-21 | RIACHÃO | MARANHÃO | Brasil | 2109502 | 21 | 33 | nan | nan | nan | Cerrado | 6.0 |
| 71c92a43-7a1e-3354-b4c0-5e075282f418 | -7.48776 | -46.63016 | 2024-10-25 16:52:00 | NOAA-21 | RIACHÃO | MARANHÃO | Brasil | 2109502 | 21 | 33 | nan | nan | nan | Cerrado | 43.5 |
| bed29732-48e9-3d9b-8b15-ca01be8fe781 | -7.47858 | -46.48153 | 2024-10-25 16:52:00 | NOAA-21 | RIACHÃO | MARANHÃO | Brasil | 2109502 | 21 | 33 | nan | nan | nan | Cerrado | 16.9 |
| af9c2144-2349-3f61-aabb-daa9118ca147 | -7.40988 | -46.58781 | 2024-10-25 16:52:00 | NOAA-21 | RIACHÃO | MARANHÃO | Brasil | 2109502 | 21 | 33 | nan | nan | nan | Cerrado | 5.0 |
| 94d72f32-de06-3dad-8f5a-63227376005a | -7.40121 | -46.69736 | 2024-10-25 16:52:00 | NOAA-21 | RIACHÃO | MARANHÃO | Brasil | 2109502 | 21 | 33 | nan | nan | nan | Cerrado | 3.3 |
| 3805063c-df9c-322b-b405-6371cb5eec1e | -7.3688 | -45.57275 | 2024-10-25 16:52:00 | NOAA-21 | SAMBAÍBA | MARANHÃO | Brasil | 2109700 | 21 | 33 | nan | nan | nan | Cerrado | 7.2 |
| 5d3951d7-2caa-36b8-ac18-2a8b4ecbc9f4 | -7.36486 | -45.57341 | 2024-10-25 16:52:00 | NOAA-21 | SAMBAÍBA | MARANHÃO | Brasil | 2109700 | 21 | 33 | nan | nan | nan | Cerrado | 7.2 |
| 3b29cda9-e035-3cff-9fd0-31fcf48106e2 | -7.36403 | -45.56833 | 2024-10-25 16:52:00 | NOAA-21 | SAMBAÍBA | MARANHÃO | Brasil | 2109700 | 21 | 33 | nan | nan | nan | Cerrado | 7.2 |
| 90ea8439-6e49-3d56-ae4d-8ebc5ab41dbf | -7.33359 | -45.67661 | 2024-10-25 16:52:00 | NOAA-21 | SÃO RAIMUNDO DAS MANGABEIRAS | MARANHÃO | Brasil | 2111607 | 21 | 33 | nan | nan | nan | Cerrado | 6.5 |
| 6d679dd7-6c93-39e4-b833-eb841bb59d60 | -7.32968 | -45.67723 | 2024-10-25 16:52:00 | NOAA-21 | SÃO RAIMUNDO DAS MANGABEIRAS | MARANHÃO | Brasil | 2111607 | 21 | 33 | nan | nan | nan | Cerrado | 12.2 |
| 078045e0-b6d1-3b86-9d20-6772d0adec3f | -7.32884 | -45.67223 | 2024-10-25 16:52:00 | NOAA-21 | SÃO RAIMUNDO DAS MANGABEIRAS | MARANHÃO | Brasil | 2111607 | 21 | 33 | nan | nan | nan | Cerrado | 9.0 |
| ddd0188a-70d9-316b-b70b-93b22b002b72 | -7.29117 | -45.76323 | 2024-10-25 16:52:00 | NOAA-21 | SÃO RAIMUNDO DAS MANGABEIRAS | MARANHÃO | Brasil | 2111607 | 21 | 33 | nan | nan | nan | Cerrado | 9.9 |
| 1777d614-5a25-39c6-b1d3-128f09084838 | -7.2881 | -45.76887 | 2024-10-25 16:52:00 | NOAA-21 | SÃO RAIMUNDO DAS MANGABEIRAS | MARANHÃO | Brasil | 2111607 | 21 | 33 | nan | nan | nan | Cerrado | 9.9 |
| a1019a2f-28b2-3122-86c3-eb8b57ccde68 | -7.20801 | -46.44781 | 2024-10-25 16:52:00 | NOAA-21 | RIACHÃO | MARANHÃO | Brasil | 2109502 | 21 | 33 | nan | nan | nan | Cerrado | 5.6 |
| 1310c93f-1e67-3ff6-af0b-2fceb7be06bd | -7.18121 | -46.4246 | 2024-10-25 16:52:00 | NOAA-21 | RIACHÃO | MARANHÃO | Brasil | 2109502 | 21 | 33 | nan | nan | nan | Cerrado | 11.0 |
| 1762bc4d-84ab-3d3d-a2fe-22964d1d37e8 | -7.17398 | -46.33212 | 2024-10-25 16:52:00 | NOAA-21 | RIACHÃO | MARANHÃO | Brasil | 2109502 | 21 | 33 | nan | nan | nan | Cerrado | 14.8 |
| d736882e-5107-3d08-81f7-89c60c9766e1 | -7.17323 | -46.32746 | 2024-10-25 16:52:00 | NOAA-21 | RIACHÃO | MARANHÃO | Brasil | 2109502 | 21 | 33 | nan | nan | nan | Cerrado | 14.8 |
| 6c548f81-4937-3dd0-97e7-25a50382534f | -7.15719 | -46.44241 | 2024-10-25 16:52:00 | NOAA-21 | RIACHÃO | MARANHÃO | Brasil | 2109502 | 21 | 33 | nan | nan | nan | Cerrado | 7.4 |
| cfc16583-fb13-3974-83a2-196f7961620e | -7.14832 | -46.17324 | 2024-10-25 16:52:00 | NOAA-21 | NOVA COLINAS | MARANHÃO | Brasil | 2107258 | 21 | 33 | nan | nan | nan | Cerrado | 7.3 |
| 5efa1680-8ac1-345a-aeb4-365500213892 | -7.14448 | -46.02782 | 2024-10-25 16:52:00 | NOAA-21 | FORTALEZA DOS NOGUEIRAS | MARANHÃO | Brasil | 2104107 | 21 | 33 | nan | nan | nan | Cerrado | 5.1 |
| 84d459e1-9094-3f33-8c0b-c9702915b6e4 | -7.14216 | -45.44155 | 2024-10-25 16:52:00 | NOAA-21 | SAMBAÍBA | MARANHÃO | Brasil | 2109700 | 21 | 33 | nan | nan | nan | Cerrado | 5.6 |
| c0564b0a-44d8-3410-96a7-8b96a45754ae | -7.14159 | -45.43812 | 2024-10-25 16:52:00 | NOAA-21 | SAMBAÍBA | MARANHÃO | Brasil | 2109700 | 21 | 33 | nan | nan | nan | Cerrado | 15.2 |
| 052a39ca-6315-373a-bdc6-46c54ddbed78 | -7.11416 | -45.32063 | 2024-10-25 16:52:00 | NOAA-21 | SAMBAÍBA | MARANHÃO | Brasil | 2109700 | 21 | 33 | nan | nan | nan | Cerrado | 6.3 |
| 01f5d35b-b42d-3891-9833-d380b8ac2ae4 | -7.11299 | -45.31349 | 2024-10-25 16:52:00 | NOAA-21 | SAMBAÍBA | MARANHÃO | Brasil | 2109700 | 21 | 33 | nan | nan | nan | Cerrado | 2.3 |
| 243cb2ba-5c81-35a8-a6a8-432db97d4622 | -7.10956 | -45.31776 | 2024-10-25 16:52:00 | NOAA-21 | SAMBAÍBA | MARANHÃO | Brasil | 2109700 | 21 | 33 | nan | nan | nan | Cerrado | 31.5 |
| 453375da-89db-363d-9e84-f0f1fa2769e7 | -7.10898 | -45.3142 | 2024-10-25 16:52:00 | NOAA-21 | SAMBAÍBA | MARANHÃO | Brasil | 2109700 | 21 | 33 | nan | nan | nan | Cerrado | 15.3 |
| c785c0c8-550f-38a5-9ad4-09ca90fcb60b | -7.09723 | -45.53996 | 2024-10-25 16:52:00 | NOAA-21 | SÃO RAIMUNDO DAS MANGABEIRAS | MARANHÃO | Brasil | 2111607 | 21 | 33 | nan | nan | nan | Cerrado | 9.6 |
| 6a29d709-9e08-3b6d-835e-95633e677ace | -7.09606 | -45.50853 | 2024-10-25 16:52:00 | NOAA-21 | SÃO RAIMUNDO DAS MANGABEIRAS | MARANHÃO | Brasil | 2111607 | 21 | 33 | nan | nan | nan | Cerrado | 5.4 |
| f20e01cc-8fff-3dd0-919e-76eab6242a56 | -7.09208 | -45.50915 | 2024-10-25 16:52:00 | NOAA-21 | SÃO RAIMUNDO DAS MANGABEIRAS | MARANHÃO | Brasil | 2111607 | 21 | 33 | nan | nan | nan | Cerrado | 6.7 |
| 6e4e5a01-fd1b-3785-b3d2-c6bd35a6d319 | -7.08904 | -45.368 | 2024-10-25 16:52:00 | NOAA-21 | SAMBAÍBA | MARANHÃO | Brasil | 2109700 | 21 | 33 | nan | nan | nan | Cerrado | 6.8 |
| 71531062-0ab1-3057-bcd0-2edc3a8850e3 | -7.08688 | -45.59929 | 2024-10-25 16:52:00 | NOAA-21 | SÃO RAIMUNDO DAS MANGABEIRAS | MARANHÃO | Brasil | 2111607 | 21 | 33 | nan | nan | nan | Cerrado | 8.4 |
| 3593f384-60e9-32ea-b29d-297e51039f00 | -7.08384 | -45.60157 | 2024-10-25 16:52:00 | NOAA-21 | SÃO RAIMUNDO DAS MANGABEIRAS | MARANHÃO | Brasil | 2111607 | 21 | 33 | nan | nan | nan | Cerrado | 50.5 |
| c034a562-1e87-3f35-86ad-4a4bdf2f8aae | -7.08293 | -45.59992 | 2024-10-25 16:52:00 | NOAA-21 | SÃO RAIMUNDO DAS MANGABEIRAS | MARANHÃO | Brasil | 2111607 | 21 | 33 | nan | nan | nan | Cerrado | 35.9 |
| 72c14835-ded1-3fef-a4bc-3b63974729a7 | -7.07318 | -46.33284 | 2024-10-25 16:52:00 | NOAA-21 | NOVA COLINAS | MARANHÃO | Brasil | 2107258 | 21 | 33 | nan | nan | nan | Cerrado | 62.3 |
| 68b0024b-d832-3a77-b6b1-b0b623158975 | -7.06995 | -45.30292 | 2024-10-25 16:52:00 | NOAA-21 | SAMBAÍBA | MARANHÃO | Brasil | 2109700 | 21 | 33 | nan | nan | nan | Cerrado | 4.5 |
| b13eb708-bd87-3fd6-9fc7-2b21181d9383 | -7.06865 | -46.32877 | 2024-10-25 16:52:00 | NOAA-21 | NOVA COLINAS | MARANHÃO | Brasil | 2107258 | 21 | 33 | nan | nan | nan | Cerrado | 60.7 |
| b3446bd5-7f06-3e53-b04f-8908222f6cc7 | -7.05155 | -46.00258 | 2024-10-25 16:52:00 | NOAA-21 | FORTALEZA DOS NOGUEIRAS | MARANHÃO | Brasil | 2104107 | 21 | 33 | nan | nan | nan | Cerrado | 24.4 |
| cc5442fd-c288-359e-a2ff-9864a62bc0fa | -7.04994 | -46.00486 | 2024-10-25 16:52:00 | NOAA-21 | FORTALEZA DOS NOGUEIRAS | MARANHÃO | Brasil | 2104107 | 21 | 33 | nan | nan | nan | Cerrado | 35.5 |
| 22116700-1c68-39fa-8c17-7654f8bcb13a | -7.04846 | -46.008 | 2024-10-25 16:52:00 | NOAA-21 | FORTALEZA DOS NOGUEIRAS | MARANHÃO | Brasil | 2104107 | 21 | 33 | nan | nan | nan | Cerrado | 30.6 |
| 6c575940-2956-3451-8ab7-e12d19caaf96 | -7.04769 | -46.00317 | 2024-10-25 16:52:00 | NOAA-21 | FORTALEZA DOS NOGUEIRAS | MARANHÃO | Brasil | 2104107 | 21 | 33 | nan | nan | nan | Cerrado | 24.4 |
| f623c227-6457-3a79-9005-5115929d129f | -7.04608 | -46.00546 | 2024-10-25 16:52:00 | NOAA-21 | FORTALEZA DOS NOGUEIRAS | MARANHÃO | Brasil | 2104107 | 21 | 33 | nan | nan | nan | Cerrado | 35.5 |
| 74a31b2f-2db2-39da-bf56-1cdcef52c927 | -7.04148 | -46.2568 | 2024-10-25 16:52:00 | NOAA-21 | NOVA COLINAS | MARANHÃO | Brasil | 2107258 | 21 | 33 | nan | nan | nan | Cerrado | 38.9 |
| eab4c8f7-c501-389e-8464-876a4b6c9aa2 | -7.03846 | -46.26217 | 2024-10-25 16:52:00 | NOAA-21 | NOVA COLINAS | MARANHÃO | Brasil | 2107258 | 21 | 33 | nan | nan | nan | Cerrado | 24.4 |
| 4b99bd68-2a86-36e9-bb70-585350dcfc3a | -7.0377 | -46.25749 | 2024-10-25 16:52:00 | NOAA-21 | NOVA COLINAS | MARANHÃO | Brasil | 2107258 | 21 | 33 | nan | nan | nan | Cerrado | 11.8 |
| 4392282a-bd45-3a91-8ae6-da33c9a61ce3 | -7.03619 | -46.27212 | 2024-10-25 16:52:00 | NOAA-21 | NOVA COLINAS | MARANHÃO | Brasil | 2107258 | 21 | 33 | nan | nan | nan | Cerrado | 4.2 |
| 6a6e26d8-ddc2-30da-accc-431f9a2b31e8 | -7.03391 | -46.25815 | 2024-10-25 16:52:00 | NOAA-21 | NOVA COLINAS | MARANHÃO | Brasil | 2107258 | 21 | 33 | nan | nan | nan | Cerrado | 11.8 |
| 510a8442-3367-3404-b39d-2393499fd073 | -7.03305 | -46.01039 | 2024-10-25 16:52:00 | NOAA-21 | FORTALEZA DOS NOGUEIRAS | MARANHÃO | Brasil | 2104107 | 21 | 33 | nan | nan | nan | Cerrado | 66.7 |
| 8d68a1b5-dce2-392e-9b29-794dc646a42a | -7.0324 | -46.27276 | 2024-10-25 16:52:00 | NOAA-21 | NOVA COLINAS | MARANHÃO | Brasil | 2107258 | 21 | 33 | nan | nan | nan | Cerrado | 6.4 |
| fc05d484-a32a-3335-9670-203dcb9e4b54 | -7.03165 | -46.26814 | 2024-10-25 16:52:00 | NOAA-21 | NOVA COLINAS | MARANHÃO | Brasil | 2107258 | 21 | 33 | nan | nan | nan | Cerrado | 14.5 |
| 86601e48-76b6-394c-b41f-21f2521955b2 | -7.03159 | -46.21991 | 2024-10-25 16:52:00 | NOAA-21 | FORTALEZA DOS NOGUEIRAS | MARANHÃO | Brasil | 2104107 | 21 | 33 | nan | nan | nan | Cerrado | 2.0 |
| af616b1a-7cd6-395b-ba57-239026454eec | -7.0026 | -45.3032 | 2024-10-25 16:52:00 | NOAA-21 | SAMBAÍBA | MARANHÃO | Brasil | 2109700 | 21 | 33 | nan | nan | nan | Cerrado | 1.2 |
| 8199d591-00d9-3682-9781-ab21470b4da0 | -6.99398 | -45.30106 | 2024-10-25 16:52:00 | NOAA-21 | SAMBAÍBA | MARANHÃO | Brasil | 2109700 | 21 | 33 | nan | nan | nan | Cerrado | 2.4 |
| d19e7c4f-2611-3793-8f62-471644b6170d | -6.9934 | -45.29756 | 2024-10-25 16:52:00 | NOAA-21 | SAMBAÍBA | MARANHÃO | Brasil | 2109700 | 21 | 33 | nan | nan | nan | Cerrado | 4.0 |


[Clique aqui para ver as próximas entradas](README175.md)
