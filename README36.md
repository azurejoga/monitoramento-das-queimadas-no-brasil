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

## Dados Diários - Página 36

| ID | Latitude | Longitude | Data/Hora GMT | Satélite | Município | Estado | País | Município ID | Estado ID | País ID | Dias sem Chuva | Precipitação | Risco de Fogo | Bioma | FRP |
|----|----------|-----------|---------------|----------|-----------|--------|------|--------------|-----------|---------|----------------|--------------|----------------|-------|-----|
| 62752cde-3baf-31d8-9df5-77f4888b4d4f | -5.43756 | -42.58839 | 2025-09-08 04:00:00 | NOAA-20 | LAGOA DO PIAUÍ | PIAUÍ | Brasil | 2205581 | 22 | 33 | nan | nan | nan | Caatinga | 6.3 |
| da80fb2e-78d3-3313-ab83-984adb25b6c5 | -5.87383 | -44.18228 | 2025-09-08 04:00:00 | NOAA-20 | JATOBÁ | MARANHÃO | Brasil | 2105450 | 21 | 33 | nan | nan | nan | Cerrado | 1.5 |
| 26e93cdb-26db-3efb-90d2-dd58b9978826 | -6.55883 | -42.95459 | 2025-09-08 04:00:00 | NOAA-20 | BARÃO DE GRAJAÚ | MARANHÃO | Brasil | 2101509 | 21 | 33 | nan | nan | nan | Cerrado | 1.2 |
| 33923453-1f26-399c-a2e3-141f47ef6400 | -5.63751 | -43.64506 | 2025-09-08 04:00:00 | NOAA-20 | PARNARAMA | MARANHÃO | Brasil | 2107803 | 21 | 33 | nan | nan | nan | Cerrado | 2.0 |
| 50b3dfca-1188-3855-bdda-94b31fe968e9 | -3.35394 | -39.27774 | 2025-09-08 04:00:00 | NOAA-20 | TRAIRI | CEARÁ | Brasil | 2313500 | 23 | 33 | nan | nan | nan | Caatinga | 1.1 |
| 585cd993-dec4-3a56-aaab-1d41ac560577 | -5.94939 | -45.75445 | 2025-09-08 04:00:00 | NOAA-20 | GRAJAÚ | MARANHÃO | Brasil | 2104800 | 21 | 33 | nan | nan | nan | Cerrado | 2.3 |
| 1ac6c16b-3c26-39f2-b718-789d8cd43553 | -5.21911 | -43.69063 | 2025-09-08 04:00:00 | NOAA-20 | CAXIAS | MARANHÃO | Brasil | 2103000 | 21 | 33 | nan | nan | nan | Cerrado | 7.4 |
| e2bacef2-b1d3-3905-9e92-71d05b669703 | -5.87306 | -45.07073 | 2025-09-08 04:00:00 | NOAA-20 | FERNANDO FALCÃO | MARANHÃO | Brasil | 2104081 | 21 | 33 | nan | nan | nan | Cerrado | 1.9 |
| 8b538085-24ae-3c36-bf6d-c785fb03c951 | -5.99039 | -44.14751 | 2025-09-08 04:00:00 | NOAA-20 | COLINAS | MARANHÃO | Brasil | 2103505 | 21 | 33 | nan | nan | nan | Cerrado | 4.0 |
| 78778c08-314a-3e8e-a47d-0fc62595ccf2 | -7.62399 | -46.1094 | 2025-09-08 04:00:00 | NOAA-20 | BALSAS | MARANHÃO | Brasil | 2101400 | 21 | 33 | nan | nan | nan | Cerrado | 0.8 |
| 26eabd1c-960a-3642-aa33-c3f4a09ecff0 | -6.27317 | -53.4318 | 2025-09-08 04:00:00 | NOAA-20 | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 2.0 |
| fa4e9161-a016-3fa6-a74e-919264300bf4 | -6.21443 | -40.99026 | 2025-09-08 04:00:00 | NOAA-20 | PIMENTEIRAS | PIAUÍ | Brasil | 2208106 | 22 | 33 | nan | nan | nan | Caatinga | 1.4 |
| f96523a3-875c-3abb-8151-3c7064ada1d0 | -7.99114 | -46.34708 | 2025-09-08 04:00:00 | NOAA-20 | BALSAS | MARANHÃO | Brasil | 2101400 | 21 | 33 | nan | nan | nan | Cerrado | 2.6 |
| d15cc115-d921-3b97-b1e8-b280a3c94628 | -4.89687 | -42.21241 | 2025-09-08 04:00:00 | NOAA-20 | CAMPO MAIOR | PIAUÍ | Brasil | 2202208 | 22 | 33 | nan | nan | nan | Caatinga | 4.0 |
| 1ac1cf07-0d13-3717-9ae3-af0e284d3c2a | -6.00416 | -44.1471 | 2025-09-08 04:00:00 | NOAA-20 | COLINAS | MARANHÃO | Brasil | 2103505 | 21 | 33 | nan | nan | nan | Cerrado | 3.5 |
| 255d084c-5123-3e9a-9a03-be366fd645db | -5.32745 | -42.68841 | 2025-09-08 04:00:00 | NOAA-20 | DEMERVAL LOBÃO | PIAUÍ | Brasil | 2203305 | 22 | 33 | nan | nan | nan | Caatinga | 1.8 |
| 40a55cfc-4513-3483-8631-09616b272b04 | -6.63133 | -53.3782 | 2025-09-08 04:00:00 | NOAA-20 | SÃO FÉLIX DO XINGU | PARÁ | Brasil | 1507300 | 15 | 33 | nan | nan | nan | Amazônia | 4.0 |
| 8aeca79d-bf2d-3942-8578-bf17193651d6 | -6.28254 | -53.42002 | 2025-09-08 04:00:00 | NOAA-20 | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 3.0 |
| 256f94ca-a2b5-30ea-87f6-fc9702e48143 | -5.71709 | -43.89649 | 2025-09-08 04:00:00 | NOAA-20 | BURITI BRAVO | MARANHÃO | Brasil | 2102309 | 21 | 33 | nan | nan | nan | Cerrado | 2.7 |
| 0d74c65b-6bd1-3439-b6f8-ecadf498c8d7 | -5.8793 | -46.09926 | 2025-09-08 04:00:00 | NOAA-20 | GRAJAÚ | MARANHÃO | Brasil | 2104800 | 21 | 33 | nan | nan | nan | Cerrado | 1.4 |
| bdb78a37-57d3-386c-8de8-384780ae953c | -6.30772 | -42.19966 | 2025-09-08 04:00:00 | NOAA-20 | ELESBÃO VELOSO | PIAUÍ | Brasil | 2203503 | 22 | 33 | nan | nan | nan | Caatinga | 2.5 |
| f6a07513-eaf6-39fa-a3c1-7599d53db316 | -5.36098 | -42.63957 | 2025-09-08 04:00:00 | NOAA-20 | DEMERVAL LOBÃO | PIAUÍ | Brasil | 2203305 | 22 | 33 | nan | nan | nan | Caatinga | 1.6 |
| dbcd4ed6-5774-360d-a630-d7b4258c770d | -6.18972 | -43.37616 | 2025-09-08 04:00:00 | NOAA-20 | LAGOA DO MATO | MARANHÃO | Brasil | 2105922 | 21 | 33 | nan | nan | nan | Cerrado | 1.3 |
| d859aa02-ede2-3881-a57e-b46e40e12826 | -6.19921 | -43.60971 | 2025-09-08 04:00:00 | NOAA-20 | PASSAGEM FRANCA | MARANHÃO | Brasil | 2107902 | 21 | 33 | nan | nan | nan | Cerrado | 2.8 |
| 9bb22daf-5669-30af-921b-544585eb5480 | -6.23346 | -45.60802 | 2025-09-08 04:00:00 | NOAA-20 | FERNANDO FALCÃO | MARANHÃO | Brasil | 2104081 | 21 | 33 | nan | nan | nan | Cerrado | 2.6 |
| 03a8262b-8265-3c00-93a5-b10fb96bfec7 | -6.12282 | -44.25326 | 2025-09-08 04:00:00 | NOAA-20 | COLINAS | MARANHÃO | Brasil | 2103505 | 21 | 33 | nan | nan | nan | Cerrado | 2.0 |
| 557761e4-92a5-3609-bbc7-fc52b73f2871 | -4.5678 | -40.34408 | 2025-09-08 04:00:00 | NOAA-20 | HIDROLÂNDIA | CEARÁ | Brasil | 2305209 | 23 | 33 | nan | nan | nan | Caatinga | 2.0 |
| 244d531a-6314-3c65-9902-5a991363b77d | -6.37698 | -39.25275 | 2025-09-08 04:00:00 | NOAA-20 | IGUATU | CEARÁ | Brasil | 2305506 | 23 | 33 | nan | nan | nan | Caatinga | 1.5 |
| f8f51989-2445-30f7-9287-6893d6932767 | -7.76493 | -34.90852 | 2025-09-08 04:00:00 | NOAA-20 | ITAPISSUMA | PERNAMBUCO | Brasil | 2607752 | 26 | 33 | nan | nan | nan | Mata Atlântica | 1.3 |
| 84a86555-ec2e-30f8-9f07-eeaa39b96812 | -5.87998 | -43.96545 | 2025-09-08 04:00:00 | NOAA-20 | BURITI BRAVO | MARANHÃO | Brasil | 2102309 | 21 | 33 | nan | nan | nan | Cerrado | 5.9 |
| 102191d5-341e-364b-a7d3-a06f251ece42 | -6.10586 | -44.14211 | 2025-09-08 04:00:00 | NOAA-20 | COLINAS | MARANHÃO | Brasil | 2103505 | 21 | 33 | nan | nan | nan | Cerrado | 2.3 |
| 054e75f7-3ae6-3551-b028-be614742aa85 | -6.3875 | -43.80649 | 2025-09-08 04:00:00 | NOAA-20 | SÃO JOÃO DOS PATOS | MARANHÃO | Brasil | 2111102 | 21 | 33 | nan | nan | nan | Cerrado | 1.7 |
| e0deb4dd-2933-3dab-b3d2-4341683dacaa | -3.96357 | -38.87924 | 2025-09-08 04:00:00 | NOAA-20 | CAUCAIA | CEARÁ | Brasil | 2303709 | 23 | 33 | nan | nan | nan | Caatinga | 1.4 |
| aeab6b21-87fa-3545-bc70-211a1020d1f1 | -7.43463 | -45.21533 | 2025-09-08 04:00:00 | NOAA-20 | LORETO | MARANHÃO | Brasil | 2106102 | 21 | 33 | nan | nan | nan | Cerrado | 3.0 |
| d59b560b-6db0-3d48-a392-1837748b906e | -4.89851 | -42.22479 | 2025-09-08 04:00:00 | NOAA-20 | CAMPO MAIOR | PIAUÍ | Brasil | 2202208 | 22 | 33 | nan | nan | nan | Caatinga | 4.1 |
| de8fe8c3-96fa-35a6-910c-b952a1e7b7da | -5.44836 | -43.42408 | 2025-09-08 04:00:00 | NOAA-20 | MATÕES | MARANHÃO | Brasil | 2106607 | 21 | 33 | nan | nan | nan | Cerrado | 1.4 |
| 5fad86a0-fe52-3455-b194-b2a0e32335b0 | -6.82959 | -52.80708 | 2025-09-08 04:00:00 | NOAA-20 | SÃO FÉLIX DO XINGU | PARÁ | Brasil | 1507300 | 15 | 33 | nan | nan | nan | Amazônia | 2.0 |
| 201b1173-9f91-3973-a04b-b347dd17338f | -6.10972 | -44.14265 | 2025-09-08 04:00:00 | NOAA-20 | COLINAS | MARANHÃO | Brasil | 2103505 | 21 | 33 | nan | nan | nan | Cerrado | 2.3 |
| 3dc8c8e0-cd23-3935-b2bc-5c42d262ce48 | -8.30039 | -45.38559 | 2025-09-08 04:00:00 | NOAA-20 | BAIXA GRANDE DO RIBEIRO | PIAUÍ | Brasil | 2201150 | 22 | 33 | nan | nan | nan | Cerrado | 1.9 |
| 89eea487-5455-357c-8fed-5fe7573b6893 | -7.73769 | -44.72551 | 2025-09-08 04:00:00 | NOAA-20 | URUÇUÍ | PIAUÍ | Brasil | 2211209 | 22 | 33 | nan | nan | nan | Cerrado | 2.2 |
| f97b3f74-830d-3e59-8f08-a1a9f4e5f9c9 | -5.79471 | -45.66372 | 2025-09-08 04:00:00 | NOAA-20 | GRAJAÚ | MARANHÃO | Brasil | 2104800 | 21 | 33 | nan | nan | nan | Cerrado | 0.7 |
| 65b80576-d779-397a-9824-58b6076db095 | -6.62113 | -53.3562 | 2025-09-08 04:00:00 | NOAA-20 | SÃO FÉLIX DO XINGU | PARÁ | Brasil | 1507300 | 15 | 33 | nan | nan | nan | Amazônia | 2.4 |
| 9b38910e-f17e-3372-8ecf-e5971990ba5e | -6.36087 | -42.59077 | 2025-09-08 04:00:00 | NOAA-20 | REGENERAÇÃO | PIAUÍ | Brasil | 2208809 | 22 | 33 | nan | nan | nan | Caatinga | 2.5 |
| 45d10135-9cdf-3034-bef6-7ade02022712 | -5.71979 | -43.8997 | 2025-09-08 04:00:00 | NOAA-20 | BURITI BRAVO | MARANHÃO | Brasil | 2102309 | 21 | 33 | nan | nan | nan | Cerrado | 1.5 |
| e84114ed-e6d2-3cf3-89f6-39cb355ffffb | -7.72247 | -44.71546 | 2025-09-08 04:00:00 | NOAA-20 | URUÇUÍ | PIAUÍ | Brasil | 2211209 | 22 | 33 | nan | nan | nan | Cerrado | 2.6 |
| 806f043e-bd2d-3f0c-9a9b-d5fb564d2b56 | -6.29914 | -43.8227 | 2025-09-08 04:00:00 | NOAA-20 | SÃO JOÃO DOS PATOS | MARANHÃO | Brasil | 2111102 | 21 | 33 | nan | nan | nan | Cerrado | 1.5 |
| 3d275c6a-ec45-3190-b1b0-ef5de9f0d37c | -5.42111 | -42.68979 | 2025-09-08 04:00:00 | NOAA-20 | LAGOA DO PIAUÍ | PIAUÍ | Brasil | 2205581 | 22 | 33 | nan | nan | nan | Caatinga | 1.9 |
| 42bfb478-11b0-311d-9e81-b1c20eb2bde9 | -7.99464 | -45.46132 | 2025-09-08 04:00:00 | NOAA-20 | RIBEIRO GONÇALVES | PIAUÍ | Brasil | 2208908 | 22 | 33 | nan | nan | nan | Cerrado | 2.0 |
| 843a47bf-33fc-312b-8d5c-6fa3268b6892 | -6.21877 | -42.59687 | 2025-09-08 04:00:00 | NOAA-20 | REGENERAÇÃO | PIAUÍ | Brasil | 2208809 | 22 | 33 | nan | nan | nan | Caatinga | 3.3 |
| 44107a9d-ed17-3858-9d76-f23998e63b57 | -5.80591 | -45.64903 | 2025-09-08 04:00:00 | NOAA-20 | GRAJAÚ | MARANHÃO | Brasil | 2104800 | 21 | 33 | nan | nan | nan | Cerrado | 1.4 |
| d7949057-2880-3793-98f1-fa12b682079e | -6.46345 | -43.9552 | 2025-09-08 04:00:00 | NOAA-20 | PARAIBANO | MARANHÃO | Brasil | 2107704 | 21 | 33 | nan | nan | nan | Cerrado | 3.1 |
| 15c5a96e-23c9-3011-a8de-9f4a8c3b13e5 | -6.21896 | -43.28889 | 2025-09-08 04:00:00 | NOAA-20 | SÃO FRANCISCO DO MARANHÃO | MARANHÃO | Brasil | 2110906 | 21 | 33 | nan | nan | nan | Cerrado | 1.1 |
| 51b880cb-6361-336f-8616-1f4972636bee | -7.3919 | -43.99393 | 2025-09-08 04:00:00 | NOAA-20 | LANDRI SALES | PIAUÍ | Brasil | 2205607 | 22 | 33 | nan | nan | nan | Cerrado | 1.3 |
| 8db723ef-a81e-3399-ab5c-b634996c5c38 | -6.22357 | -42.58957 | 2025-09-08 04:00:00 | NOAA-20 | REGENERAÇÃO | PIAUÍ | Brasil | 2208809 | 22 | 33 | nan | nan | nan | Caatinga | 2.1 |
| 5594100e-927f-349a-be0e-f917a352f015 | -6.64652 | -44.80598 | 2025-09-08 04:00:00 | NOAA-20 | MIRADOR | MARANHÃO | Brasil | 2106706 | 21 | 33 | nan | nan | nan | Cerrado | 3.2 |
| c4974845-6631-3784-a9a4-093f25c58edf | -8.1546 | -44.84881 | 2025-09-08 04:00:00 | NOAA-20 | URUÇUÍ | PIAUÍ | Brasil | 2211209 | 22 | 33 | nan | nan | nan | Cerrado | 2.7 |
| da1af013-9525-39c8-83ec-3ca3b0e3e56f | -6.27934 | -53.42958 | 2025-09-08 04:00:00 | NOAA-20 | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 3.3 |
| ebda0c58-aeba-30c9-b369-9a83f3674ec1 | -6.20213 | -41.00282 | 2025-09-08 04:00:00 | NOAA-20 | PIMENTEIRAS | PIAUÍ | Brasil | 2208106 | 22 | 33 | nan | nan | nan | Caatinga | 1.4 |
| adfa9584-f4d8-3461-b9b3-c4496c434a53 | -6.10718 | -44.14447 | 2025-09-08 04:00:00 | NOAA-20 | COLINAS | MARANHÃO | Brasil | 2103505 | 21 | 33 | nan | nan | nan | Cerrado | 3.7 |
| 53359c6a-89e2-3373-b03f-213a041db53a | -5.88075 | -43.96071 | 2025-09-08 04:00:00 | NOAA-20 | BURITI BRAVO | MARANHÃO | Brasil | 2102309 | 21 | 33 | nan | nan | nan | Cerrado | 3.3 |
| 9a73fd07-fbd3-3654-9be3-618daf06f621 | -6.21848 | -43.31499 | 2025-09-08 04:00:00 | NOAA-20 | SÃO FRANCISCO DO MARANHÃO | MARANHÃO | Brasil | 2110906 | 21 | 33 | nan | nan | nan | Cerrado | 2.5 |
| 029a756c-f442-3deb-a958-a70ad3d0b218 | -8.46277 | -45.02671 | 2025-09-08 04:00:00 | NOAA-20 | BAIXA GRANDE DO RIBEIRO | PIAUÍ | Brasil | 2201150 | 22 | 33 | nan | nan | nan | Cerrado | 2.5 |
| df092060-f7a4-3d52-84c5-3fe15b46a1a6 | -8.07928 | -45.48012 | 2025-09-08 04:00:00 | NOAA-20 | RIBEIRO GONÇALVES | PIAUÍ | Brasil | 2208908 | 22 | 33 | nan | nan | nan | Cerrado | 2.9 |
| d2073663-ecb4-3bf9-8f0c-2d1b3baa3127 | -5.21621 | -43.28197 | 2025-09-08 04:00:00 | NOAA-20 | MATÕES | MARANHÃO | Brasil | 2106607 | 21 | 33 | nan | nan | nan | Cerrado | 5.5 |
| 2dc117cb-cafb-3ae1-8a24-cab94acccf98 | -5.63776 | -43.64756 | 2025-09-08 04:00:00 | NOAA-20 | PARNARAMA | MARANHÃO | Brasil | 2107803 | 21 | 33 | nan | nan | nan | Cerrado | 1.6 |
| 68087b8a-1765-3274-9d52-81528d6d2c0a | -5.8815 | -43.95615 | 2025-09-08 04:00:00 | NOAA-20 | BURITI BRAVO | MARANHÃO | Brasil | 2102309 | 21 | 33 | nan | nan | nan | Cerrado | 3.3 |
| bf70b799-0aa7-32c7-9403-362b40c210fb | -5.91278 | -49.67511 | 2025-09-08 04:00:00 | NOAA-20 | MARABÁ | PARÁ | Brasil | 1504208 | 15 | 33 | nan | nan | nan | Amazônia | 6.4 |
| 6f862ff3-8924-3cfe-a116-d62140236c08 | -7.22121 | -46.20293 | 2025-09-08 04:00:00 | NOAA-20 | NOVA COLINAS | MARANHÃO | Brasil | 2107258 | 21 | 33 | nan | nan | nan | Cerrado | 4.0 |
| e6c4fcf0-3243-3327-b7ea-a72c7991602e | -6.21394 | -43.29674 | 2025-09-08 04:00:00 | NOAA-20 | SÃO FRANCISCO DO MARANHÃO | MARANHÃO | Brasil | 2110906 | 21 | 33 | nan | nan | nan | Cerrado | 1.3 |
| fc16125b-248e-3bfa-bfc0-8b6d763a0e00 | -6.40515 | -42.98135 | 2025-09-08 04:00:00 | NOAA-20 | SÃO FRANCISCO DO MARANHÃO | MARANHÃO | Brasil | 2110906 | 21 | 33 | nan | nan | nan | Cerrado | 1.1 |
| 1af29c28-2cce-3d5b-9bd9-d8094c386f0d | -6.28132 | -53.42665 | 2025-09-08 04:00:00 | NOAA-20 | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 3.0 |
| 926fc97f-f205-3d2b-a621-7e94cf878e34 | -6.2476 | -44.82975 | 2025-09-08 04:00:00 | NOAA-20 | MIRADOR | MARANHÃO | Brasil | 2106706 | 21 | 33 | nan | nan | nan | Cerrado | 1.9 |
| 728241db-1e06-359c-9585-ebfd49939064 | -6.25074 | -43.6911 | 2025-09-08 04:00:00 | NOAA-20 | PASSAGEM FRANCA | MARANHÃO | Brasil | 2107902 | 21 | 33 | nan | nan | nan | Cerrado | 1.6 |
| 3edc9833-79c6-3a4c-8839-16500768b788 | -8.1549 | -44.85139 | 2025-09-08 04:00:00 | NOAA-20 | URUÇUÍ | PIAUÍ | Brasil | 2211209 | 22 | 33 | nan | nan | nan | Cerrado | 3.1 |
| 1d714cda-2845-36fc-a37c-3f315b055949 | -6.48616 | -44.00471 | 2025-09-08 04:00:00 | NOAA-20 | PASTOS BONS | MARANHÃO | Brasil | 2108009 | 21 | 33 | nan | nan | nan | Cerrado | 2.7 |
| ffe4efc6-c228-34af-b7bf-48e5c3f4121f | -6.66724 | -44.55642 | 2025-09-08 04:00:00 | NOAA-20 | SUCUPIRA DO NORTE | MARANHÃO | Brasil | 2111904 | 21 | 33 | nan | nan | nan | Cerrado | 1.3 |
| ff52cc83-d8cb-3af5-bb62-28d0f6a1ee1b | -7.08051 | -43.51854 | 2025-09-08 04:00:00 | NOAA-20 | JERUMENHA | PIAUÍ | Brasil | 2205300 | 22 | 33 | nan | nan | nan | Cerrado | 1.6 |
| d6523bc1-9afd-3a71-9f67-124b9c7ccdad | -6.85265 | -45.92312 | 2025-09-08 04:00:00 | NOAA-20 | SÃO RAIMUNDO DAS MANGABEIRAS | MARANHÃO | Brasil | 2111607 | 21 | 33 | nan | nan | nan | Cerrado | 1.2 |
| 7396ecc0-3302-309b-a7de-09c1341d1a69 | -6.28363 | -43.32896 | 2025-09-08 04:00:00 | NOAA-20 | SÃO FRANCISCO DO MARANHÃO | MARANHÃO | Brasil | 2110906 | 21 | 33 | nan | nan | nan | Cerrado | 2.0 |
| 1ee2f020-448c-32ab-a81d-d760a02f24d0 | -6.19412 | -43.60593 | 2025-09-08 04:00:00 | NOAA-20 | PASSAGEM FRANCA | MARANHÃO | Brasil | 2107902 | 21 | 33 | nan | nan | nan | Cerrado | 3.6 |
| 9a4e4022-de4d-39dc-b73e-41899899d870 | -6.21828 | -43.2931 | 2025-09-08 04:00:00 | NOAA-20 | SÃO FRANCISCO DO MARANHÃO | MARANHÃO | Brasil | 2110906 | 21 | 33 | nan | nan | nan | Cerrado | 1.3 |
| 25aa00ec-1c68-38f8-bb29-57b649adda58 | -7.56902 | -44.00501 | 2025-09-08 04:00:00 | NOAA-20 | SEBASTIÃO LEAL | PIAUÍ | Brasil | 2210631 | 22 | 33 | nan | nan | nan | Cerrado | 2.2 |
| 97c8c7a8-4e55-37e2-bcad-fdd294b6de2f | -7.24785 | -44.83696 | 2025-09-08 04:00:00 | NOAA-20 | SÃO FÉLIX DE BALSAS | MARANHÃO | Brasil | 2110807 | 21 | 33 | nan | nan | nan | Cerrado | 6.5 |
| 7495367d-e8ce-3681-b0c4-450c5007d63a | -5.96116 | -45.78024 | 2025-09-08 04:00:00 | NOAA-20 | GRAJAÚ | MARANHÃO | Brasil | 2104800 | 21 | 33 | nan | nan | nan | Cerrado | 1.0 |
| 7fabec49-128d-32b3-9aa2-5c1b04af6b4e | -5.55184 | -43.79061 | 2025-09-08 04:00:00 | NOAA-20 | PARNARAMA | MARANHÃO | Brasil | 2107803 | 21 | 33 | nan | nan | nan | Cerrado | 3.0 |
| 3a5c47e6-eab7-3569-86cc-9216afc9c631 | -5.18759 | -43.04324 | 2025-09-08 04:00:00 | NOAA-20 | TIMON | MARANHÃO | Brasil | 2112209 | 21 | 33 | nan | nan | nan | Cerrado | 2.9 |
| 43546217-5861-338d-94ab-0101b817587f | -5.91183 | -49.67227 | 2025-09-08 04:00:00 | NOAA-20 | MARABÁ | PARÁ | Brasil | 1504208 | 15 | 33 | nan | nan | nan | Amazônia | 1.2 |
| 08a3909d-c9ed-3222-892e-a2200c0bed8d | -6.25496 | -42.57435 | 2025-09-08 04:00:00 | NOAA-20 | REGENERAÇÃO | PIAUÍ | Brasil | 2208809 | 22 | 33 | nan | nan | nan | Caatinga | 1.6 |
| 072812e6-2967-3658-96c5-9848742f152c | -6.48237 | -44.00408 | 2025-09-08 04:00:00 | NOAA-20 | PASTOS BONS | MARANHÃO | Brasil | 2108009 | 21 | 33 | nan | nan | nan | Cerrado | 3.7 |
| a3073534-5806-3f5b-bb4a-d9fe0a371759 | -6.36326 | -42.57823 | 2025-09-08 04:00:00 | NOAA-20 | REGENERAÇÃO | PIAUÍ | Brasil | 2208809 | 22 | 33 | nan | nan | nan | Caatinga | 2.0 |
| a3457b69-d09c-3e2b-a23c-2ab24b30ec8e | -6.18916 | -42.64538 | 2025-09-08 04:00:00 | NOAA-20 | REGENERAÇÃO | PIAUÍ | Brasil | 2208809 | 22 | 33 | nan | nan | nan | Caatinga | 2.8 |
| 9ff94e15-c62e-377f-9d0f-dfefcab909b5 | -6.21813 | -42.60084 | 2025-09-08 04:00:00 | NOAA-20 | REGENERAÇÃO | PIAUÍ | Brasil | 2208809 | 22 | 33 | nan | nan | nan | Caatinga | 3.1 |
| 6ecc1c1c-47f9-349b-9c24-eb370ba516df | -3.79067 | -48.87837 | 2025-09-08 04:00:00 | NOAA-20 | GOIANÉSIA DO PARÁ | PARÁ | Brasil | 1503093 | 15 | 33 | nan | nan | nan | Amazônia | 1.0 |
| fa4bbae2-39d7-3ba8-9a9b-77c76640c861 | -6.59507 | -44.12074 | 2025-09-08 04:00:00 | NOAA-20 | PASTOS BONS | MARANHÃO | Brasil | 2108009 | 21 | 33 | nan | nan | nan | Cerrado | 2.0 |
| 9047c981-2c79-30a2-af02-9099ecea1e61 | -6.35383 | -42.58958 | 2025-09-08 04:00:00 | NOAA-20 | REGENERAÇÃO | PIAUÍ | Brasil | 2208809 | 22 | 33 | nan | nan | nan | Caatinga | 2.2 |
| 309706f8-6f4b-344f-9699-1241340fd94e | -2.13609 | -47.71334 | 2025-09-08 04:00:00 | NOAA-20 | AURORA DO PARÁ | PARÁ | Brasil | 1500958 | 15 | 33 | nan | nan | nan | Amazônia | 1.9 |
| 238854fe-3452-3d95-a759-d56543fa08ef | -6.1743 | -44.74082 | 2025-09-08 04:00:00 | NOAA-20 | MIRADOR | MARANHÃO | Brasil | 2106706 | 21 | 33 | nan | nan | nan | Cerrado | 1.4 |
| 53a56a05-cc23-3291-9ac4-c5d74ca31b61 | -8.0438 | -44.06321 | 2025-09-08 04:00:00 | NOAA-20 | MANOEL EMÍDIO | PIAUÍ | Brasil | 2205904 | 22 | 33 | nan | nan | nan | Cerrado | 1.6 |
| afa1d4fa-74de-3bb7-958f-3ff1daea805a | -6.45966 | -43.95467 | 2025-09-08 04:00:00 | NOAA-20 | PARAIBANO | MARANHÃO | Brasil | 2107704 | 21 | 33 | nan | nan | nan | Cerrado | 2.4 |
| 65673452-6303-39a7-b118-0c05dce860bd | -5.87693 | -43.96018 | 2025-09-08 04:00:00 | NOAA-20 | BURITI BRAVO | MARANHÃO | Brasil | 2102309 | 21 | 33 | nan | nan | nan | Cerrado | 1.9 |


[Clique aqui para ver as próximas entradas](README37.md)
