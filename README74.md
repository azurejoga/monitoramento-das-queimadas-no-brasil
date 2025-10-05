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

## Dados Diários - Página 74

| ID | Latitude | Longitude | Data/Hora GMT | Satélite | Município | Estado | País | Município ID | Estado ID | País ID | Dias sem Chuva | Precipitação | Risco de Fogo | Bioma | FRP |
|----|----------|-----------|---------------|----------|-----------|--------|------|--------------|-----------|---------|----------------|--------------|----------------|-------|-----|
| 1fc2ba6d-a6b8-359f-8ed8-6948b011a50d | -6.29045 | -43.92085 | 2025-10-05 04:44:00 | NOAA-21 | PASSAGEM FRANCA | MARANHÃO | Brasil | 2107902 | 21 | 33 | nan | nan | nan | Cerrado | 4.3 |
| 7ae3fb0f-73f5-3914-9a8b-618d4ebedb26 | -4.25759 | -46.77267 | 2025-10-05 04:44:00 | NOAA-21 | BOM JARDIM | MARANHÃO | Brasil | 2102002 | 21 | 33 | nan | nan | nan | Amazônia | 1.9 |
| dcd43969-c1e8-339c-b164-83b40dfd6d47 | -4.2684 | -46.75122 | 2025-10-05 04:44:00 | NOAA-21 | BOM JARDIM | MARANHÃO | Brasil | 2102002 | 21 | 33 | nan | nan | nan | Amazônia | 3.1 |
| 513bd0d5-5d9a-38bf-a471-ee7a890f35ec | -6.14855 | -44.65396 | 2025-10-05 04:44:00 | NOAA-21 | MIRADOR | MARANHÃO | Brasil | 2106706 | 21 | 33 | nan | nan | nan | Cerrado | 7.8 |
| 77a3f8b2-d71f-3a85-8193-6f8f6ce28842 | -3.89997 | -52.1908 | 2025-10-05 04:44:00 | NOAA-21 | SENADOR JOSÉ PORFÍRIO | PARÁ | Brasil | 1507805 | 15 | 33 | nan | nan | nan | Amazônia | 1.5 |
| 9e26d74a-3cd6-3951-8093-ab9b911518d2 | -4.25619 | -46.77042 | 2025-10-05 04:44:00 | NOAA-21 | BOM JARDIM | MARANHÃO | Brasil | 2102002 | 21 | 33 | nan | nan | nan | Amazônia | 1.2 |
| d2e3350e-21b9-3eab-b70e-01548d296a3b | -4.23448 | -46.76256 | 2025-10-05 04:44:00 | NOAA-21 | BOM JARDIM | MARANHÃO | Brasil | 2102002 | 21 | 33 | nan | nan | nan | Amazônia | 7.3 |
| d158640f-f3d1-331c-be04-ee1ab2c72ed8 | -6.12354 | -42.85604 | 2025-10-05 04:44:00 | NOAA-21 | AMARANTE | PIAUÍ | Brasil | 2200509 | 22 | 33 | nan | nan | nan | Caatinga | 3.8 |
| acdb518d-78a3-3189-abd7-bb91f2445c14 | -3.77068 | -51.24231 | 2025-10-05 04:44:00 | NOAA-21 | ANAPU | PARÁ | Brasil | 1500859 | 15 | 33 | nan | nan | nan | Amazônia | 0.5 |
| 35b3a013-204a-3c2f-84ff-549b7d7a1a08 | -6.64103 | -42.7762 | 2025-10-05 04:44:00 | NOAA-21 | FRANCISCO AYRES | PIAUÍ | Brasil | 2204105 | 22 | 33 | nan | nan | nan | Caatinga | 2.9 |
| 13e7e42b-66e5-3ba4-b1c2-32ca1d7db6ee | -6.06831 | -42.66119 | 2025-10-05 04:44:00 | NOAA-21 | SÃO GONÇALO DO PIAUÍ | PIAUÍ | Brasil | 2209807 | 22 | 33 | nan | nan | nan | Caatinga | 0.7 |
| f6b6b678-f871-3ce7-aa54-629e2f4625b2 | -3.03924 | -51.47803 | 2025-10-05 04:44:00 | NOAA-21 | ANAPU | PARÁ | Brasil | 1500859 | 15 | 33 | nan | nan | nan | Amazônia | 0.2 |
| e575f88b-15dd-3779-9b9f-cc93b22d98c1 | -4.46378 | -49.10818 | 2025-10-05 04:44:00 | NOAA-21 | JACUNDÁ | PARÁ | Brasil | 1503804 | 15 | 33 | nan | nan | nan | Amazônia | 0.4 |
| ad9aaff1-fa00-31ed-be21-e1683f08c486 | -5.78087 | -45.74942 | 2025-10-05 04:44:00 | NOAA-21 | GRAJAÚ | MARANHÃO | Brasil | 2104800 | 21 | 33 | nan | nan | nan | Cerrado | 1.3 |
| 13082726-81dd-3a76-a4c6-d91df8c65124 | -5.89601 | -42.91162 | 2025-10-05 04:44:00 | NOAA-21 | PALMEIRAIS | PIAUÍ | Brasil | 2207504 | 22 | 33 | nan | nan | nan | Caatinga | 17.4 |
| c537fa1b-3838-3bbc-b915-061ee6d8e8a4 | -4.23076 | -46.76196 | 2025-10-05 04:44:00 | NOAA-21 | BOM JARDIM | MARANHÃO | Brasil | 2102002 | 21 | 33 | nan | nan | nan | Amazônia | 7.3 |
| a6e15516-bee7-3dfd-83e5-5aa15b0442f7 | -5.92721 | -43.32734 | 2025-10-05 04:44:00 | NOAA-21 | SÃO FRANCISCO DO MARANHÃO | MARANHÃO | Brasil | 2110906 | 21 | 33 | nan | nan | nan | Cerrado | 4.3 |
| ff49491b-b683-3777-8eff-721198379c31 | -4.31376 | -48.09163 | 2025-10-05 04:44:00 | NOAA-21 | RONDON DO PARÁ | PARÁ | Brasil | 1506187 | 15 | 33 | nan | nan | nan | Amazônia | 1.1 |
| 23d608aa-598c-362e-a3ae-5359cb73d209 | -5.88089 | -42.53845 | 2025-10-05 04:44:00 | NOAA-21 | OLHO D'ÁGUA DO PIAUÍ | PIAUÍ | Brasil | 2207108 | 22 | 33 | nan | nan | nan | Caatinga | 2.1 |
| 3df5d150-ad5c-3383-85c2-2f2289569ad7 | -5.55127 | -42.66412 | 2025-10-05 04:44:00 | NOAA-21 | MONSENHOR GIL | PIAUÍ | Brasil | 2206407 | 22 | 33 | nan | nan | nan | Caatinga | 1.3 |
| 9031cd18-c0c9-3470-9c61-21adc2dd6cf8 | -5.66164 | -42.75116 | 2025-10-05 04:44:00 | NOAA-21 | CURRALINHOS | PIAUÍ | Brasil | 2203255 | 22 | 33 | nan | nan | nan | Caatinga | 0.8 |
| 46786014-0f55-31c9-bbe2-4dd4a11b312b | -3.39604 | -50.27106 | 2025-10-05 04:44:00 | NOAA-21 | PACAJÁ | PARÁ | Brasil | 1505486 | 15 | 33 | nan | nan | nan | Amazônia | 4.1 |
| 0b5e1c07-ec18-36ec-b6bb-63f4a71f8b8b | -4.2602 | -48.55738 | 2025-10-05 04:44:00 | NOAA-21 | RONDON DO PARÁ | PARÁ | Brasil | 1506187 | 15 | 33 | nan | nan | nan | Amazônia | 2.6 |
| 5e937edf-32b5-3483-a9bd-c94a3edce029 | -5.49072 | -42.79603 | 2025-10-05 04:44:00 | NOAA-21 | TERESINA | PIAUÍ | Brasil | 2211001 | 22 | 33 | nan | nan | nan | Caatinga | 5.4 |
| 2935bb67-de58-3169-9ee7-870c8f250cb4 | -4.81839 | -42.76954 | 2025-10-05 04:44:00 | NOAA-21 | JOSÉ DE FREITAS | PIAUÍ | Brasil | 2205508 | 22 | 33 | nan | nan | nan | Cerrado | 4.9 |
| d438b39b-4871-3465-aab8-65ba1c9cc42c | -4.25164 | -48.56749 | 2025-10-05 04:44:00 | NOAA-21 | RONDON DO PARÁ | PARÁ | Brasil | 1506187 | 15 | 33 | nan | nan | nan | Amazônia | 5.5 |
| feb03849-834f-35ae-97ba-f45869c0ebd9 | -4.57116 | -55.95984 | 2025-10-05 04:44:00 | NOAA-21 | TRAIRÃO | PARÁ | Brasil | 1508050 | 15 | 33 | nan | nan | nan | Amazônia | 1.1 |
| 14112418-6e5a-3f39-b036-507454f4918c | -5.85338 | -45.85114 | 2025-10-05 04:44:00 | NOAA-21 | GRAJAÚ | MARANHÃO | Brasil | 2104800 | 21 | 33 | nan | nan | nan | Cerrado | 1.5 |
| 49bfc341-cb24-38b3-8c49-a19f0860feba | -2.98644 | -44.2538 | 2025-10-05 04:44:00 | NOAA-21 | ROSÁRIO | MARANHÃO | Brasil | 2109601 | 21 | 33 | nan | nan | nan | Amazônia | 1.0 |
| 9ce7b9e6-54aa-374c-a50b-63e8c6af1610 | -5.78372 | -42.93349 | 2025-10-05 04:44:00 | NOAA-21 | PALMEIRAIS | PIAUÍ | Brasil | 2207504 | 22 | 33 | nan | nan | nan | Caatinga | 9.8 |
| 22c323cb-186e-3813-9533-1a3492ea21cb | -2.905 | -50.73141 | 2025-10-05 04:44:00 | NOAA-21 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 1.6 |
| 06983afa-d784-3104-bf48-eb55693e82c9 | -6.25111 | -44.23976 | 2025-10-05 04:44:00 | NOAA-21 | MIRADOR | MARANHÃO | Brasil | 2106706 | 21 | 33 | nan | nan | nan | Cerrado | 2.1 |
| 37b7bb96-f9ae-3b52-b371-655f9c9ecfab | -3.8463 | -41.58573 | 2025-10-05 04:44:00 | NOAA-21 | PIRACURUCA | PIAUÍ | Brasil | 2208304 | 22 | 33 | nan | nan | nan | Caatinga | 4.2 |
| 3f0b71ed-bb67-3776-a923-58d86b206d57 | -6.41265 | -43.06163 | 2025-10-05 04:44:00 | NOAA-21 | SÃO FRANCISCO DO MARANHÃO | MARANHÃO | Brasil | 2110906 | 21 | 33 | nan | nan | nan | Cerrado | 8.1 |
| 539ae42e-310c-3688-9107-e67df8b5431f | -3.81763 | -51.07652 | 2025-10-05 04:44:00 | NOAA-21 | PACAJÁ | PARÁ | Brasil | 1505486 | 15 | 33 | nan | nan | nan | Amazônia | 3.6 |
| 6ca773a8-6a4d-3c48-bffa-a0ba4ca2f583 | -3.27979 | -48.89822 | 2025-10-05 04:44:00 | NOAA-21 | TAILÂNDIA | PARÁ | Brasil | 1507953 | 15 | 33 | nan | nan | nan | Amazônia | 0.6 |
| 0068c1e8-e7ab-3411-a764-69f47bc71ff2 | -6.15108 | -44.66753 | 2025-10-05 04:44:00 | NOAA-21 | MIRADOR | MARANHÃO | Brasil | 2106706 | 21 | 33 | nan | nan | nan | Cerrado | 45.7 |
| 97e02104-f87b-34e2-9f56-707bb45355fd | -6.04321 | -45.40874 | 2025-10-05 04:44:00 | NOAA-21 | FERNANDO FALCÃO | MARANHÃO | Brasil | 2104081 | 21 | 33 | nan | nan | nan | Cerrado | 3.1 |
| f0174e9f-3fa1-3d54-98a6-1f4b195daf70 | -4.76649 | -46.90954 | 2025-10-05 04:44:00 | NOAA-21 | BOM JESUS DAS SELVAS | MARANHÃO | Brasil | 2102036 | 21 | 33 | nan | nan | nan | Amazônia | 1.7 |
| a5f467f9-7068-3866-8f40-521ba0621589 | -5.85645 | -42.78679 | 2025-10-05 04:44:00 | NOAA-21 | PALMEIRAIS | PIAUÍ | Brasil | 2207504 | 22 | 33 | nan | nan | nan | Caatinga | 1.9 |
| 9f218bb5-1e2c-35f1-a6c2-ea4eeb213f5e | -6.20779 | -44.07921 | 2025-10-05 04:44:00 | NOAA-21 | COLINAS | MARANHÃO | Brasil | 2103505 | 21 | 33 | nan | nan | nan | Cerrado | 3.2 |
| a97aea28-ffa7-3ba1-96e8-382ab492f8dc | -6.69874 | -42.17096 | 2025-10-05 04:44:00 | NOAA-21 | TANQUE DO PIAUÍ | PIAUÍ | Brasil | 2210979 | 22 | 33 | nan | nan | nan | Caatinga | 2.3 |
| 42b99431-d0c8-3fdd-ac01-4f7ef261dde2 | -2.68016 | -48.39948 | 2025-10-05 04:44:00 | NOAA-21 | TOMÉ-AÇU | PARÁ | Brasil | 1508001 | 15 | 33 | nan | nan | nan | Amazônia | 2.2 |
| c37d37be-e599-3397-836c-e4725b1976b8 | -6.05228 | -44.08575 | 2025-10-05 04:44:00 | NOAA-21 | COLINAS | MARANHÃO | Brasil | 2103505 | 21 | 33 | nan | nan | nan | Cerrado | 2.8 |
| e4974432-6aee-3216-91a4-6b18f1204f20 | -6.24791 | -45.37096 | 2025-10-05 04:44:00 | NOAA-21 | FERNANDO FALCÃO | MARANHÃO | Brasil | 2104081 | 21 | 33 | nan | nan | nan | Cerrado | 4.6 |
| 91358dab-2702-3d9b-af2e-aaa1e7332133 | -5.98232 | -42.65598 | 2025-10-05 04:44:00 | NOAA-21 | SÃO GONÇALO DO PIAUÍ | PIAUÍ | Brasil | 2209807 | 22 | 33 | nan | nan | nan | Caatinga | 0.9 |
| b275245d-a71f-30d1-99da-1c082ef40c86 | -6.09645 | -43.47929 | 2025-10-05 04:44:00 | NOAA-21 | LAGOA DO MATO | MARANHÃO | Brasil | 2105922 | 21 | 33 | nan | nan | nan | Cerrado | 3.6 |
| aed80315-a95f-3b97-a92b-e04a0c1a8185 | -6.14352 | -44.65771 | 2025-10-05 04:44:00 | NOAA-21 | MIRADOR | MARANHÃO | Brasil | 2106706 | 21 | 33 | nan | nan | nan | Cerrado | 11.5 |
| 3e3ecb14-47ba-3f12-b66f-226d4b500baf | -6.12682 | -42.86251 | 2025-10-05 04:44:00 | NOAA-21 | AMARANTE | PIAUÍ | Brasil | 2200509 | 22 | 33 | nan | nan | nan | Caatinga | 3.1 |
| a3005533-126a-3458-8a41-cf871878d99b | -4.22109 | -55.75073 | 2025-10-05 04:44:00 | NOAA-21 | RURÓPOLIS | PARÁ | Brasil | 1506195 | 15 | 33 | nan | nan | nan | Amazônia | 1.6 |
| 4346a1df-dd3c-3dcb-aa08-224cd4427dca | -6.36273 | -43.91234 | 2025-10-05 04:44:00 | NOAA-21 | PARAIBANO | MARANHÃO | Brasil | 2107704 | 21 | 33 | nan | nan | nan | Cerrado | 3.8 |
| ce2341c7-2485-3f96-b9e3-b53a112c19d1 | -5.346 | -45.30159 | 2025-10-05 04:44:00 | NOAA-21 | BARRA DO CORDA | MARANHÃO | Brasil | 2101608 | 21 | 33 | nan | nan | nan | Cerrado | 2.1 |
| 9a8a17d0-982b-3600-8965-2ce917438a22 | -5.32244 | -42.65347 | 2025-10-05 04:44:00 | NOAA-21 | DEMERVAL LOBÃO | PIAUÍ | Brasil | 2203305 | 22 | 33 | nan | nan | nan | Cerrado | 1.7 |
| acfb4164-997e-3cff-8b31-7e2636b13e94 | -6.1542 | -44.64598 | 2025-10-05 04:44:00 | NOAA-21 | MIRADOR | MARANHÃO | Brasil | 2106706 | 21 | 33 | nan | nan | nan | Cerrado | 4.6 |
| b1671817-2467-3cbb-9f0f-bc9c266a404a | -5.93029 | -43.30597 | 2025-10-05 04:44:00 | NOAA-21 | SÃO FRANCISCO DO MARANHÃO | MARANHÃO | Brasil | 2110906 | 21 | 33 | nan | nan | nan | Cerrado | 1.7 |
| 55644bfd-659d-3183-88dd-6934027d79ec | -2.68867 | -48.38956 | 2025-10-05 04:44:00 | NOAA-21 | TOMÉ-AÇU | PARÁ | Brasil | 1508001 | 15 | 33 | nan | nan | nan | Amazônia | 2.4 |
| 3a3a5f98-58c2-318a-862e-820b4429d482 | -6.05969 | -42.53549 | 2025-10-05 04:44:00 | NOAA-21 | JARDIM DO MULATO | PIAUÍ | Brasil | 2205250 | 22 | 33 | nan | nan | nan | Caatinga | 0.8 |
| f2a9fa79-77fd-3020-9c7f-be321ab3e0ac | -6.12643 | -42.86522 | 2025-10-05 04:44:00 | NOAA-21 | AMARANTE | PIAUÍ | Brasil | 2200509 | 22 | 33 | nan | nan | nan | Caatinga | 1.5 |
| 194577b5-4afb-3d0b-b86c-923580b0765c | -4.45107 | -43.23487 | 2025-10-05 04:44:00 | NOAA-21 | ALDEIAS ALTAS | MARANHÃO | Brasil | 2100303 | 21 | 33 | nan | nan | nan | Cerrado | 12.7 |
| 8bd153fa-e306-322c-a02a-ad578ee5df39 | -5.84697 | -45.81011 | 2025-10-05 04:44:00 | NOAA-21 | GRAJAÚ | MARANHÃO | Brasil | 2104800 | 21 | 33 | nan | nan | nan | Cerrado | 1.2 |
| bf2e93c3-1fac-390a-8800-ed1d35bc8f50 | -6.33905 | -41.62869 | 2025-10-05 04:44:00 | NOAA-21 | VALENÇA DO PIAUÍ | PIAUÍ | Brasil | 2211308 | 22 | 33 | nan | nan | nan | Caatinga | 1.3 |
| e3bc6c99-1d12-33cf-bdc5-011312c4dbab | -6.37752 | -44.62629 | 2025-10-05 04:44:00 | NOAA-21 | MIRADOR | MARANHÃO | Brasil | 2106706 | 21 | 33 | nan | nan | nan | Cerrado | 2.6 |
| e0530363-b06f-3c1c-be18-5a42c76414d9 | -6.69594 | -41.9525 | 2025-10-05 04:44:00 | NOAA-21 | OEIRAS | PIAUÍ | Brasil | 2207009 | 22 | 33 | nan | nan | nan | Caatinga | 2.1 |
| 4cd67950-80cb-3e5c-a254-576b47ddee1f | -5.32203 | -42.65638 | 2025-10-05 04:44:00 | NOAA-21 | DEMERVAL LOBÃO | PIAUÍ | Brasil | 2203305 | 22 | 33 | nan | nan | nan | Cerrado | 2.0 |
| 2a569489-09b3-3cc3-b6cf-6c1a32ea797b | -4.27589 | -46.75225 | 2025-10-05 04:44:00 | NOAA-21 | BOM JARDIM | MARANHÃO | Brasil | 2102002 | 21 | 33 | nan | nan | nan | Amazônia | 2.8 |
| 617ef43b-e06a-3818-a57c-416b214f5a9f | -1.96804 | -47.31348 | 2025-10-05 04:44:00 | NOAA-21 | IRITUIA | PARÁ | Brasil | 1503507 | 15 | 33 | nan | nan | nan | Amazônia | 1.4 |
| bef11bf1-1be1-3641-9659-a3363bfe50f6 | -5.24279 | -42.63584 | 2025-10-05 04:44:00 | NOAA-21 | TERESINA | PIAUÍ | Brasil | 2211001 | 22 | 33 | nan | nan | nan | Cerrado | 4.2 |
| fb830e4a-9ffc-3140-8fb1-fdc928abccd6 | -6.12268 | -42.85596 | 2025-10-05 04:44:00 | NOAA-21 | AMARANTE | PIAUÍ | Brasil | 2200509 | 22 | 33 | nan | nan | nan | Caatinga | 2.6 |
| b1520180-ff33-3051-97d1-d14e0809700a | -6.29258 | -43.91486 | 2025-10-05 04:44:00 | NOAA-21 | PASSAGEM FRANCA | MARANHÃO | Brasil | 2107902 | 21 | 33 | nan | nan | nan | Cerrado | 5.6 |
| 83e8bfc1-cb83-3d2f-b01e-6dac1b82e391 | -6.27449 | -44.03681 | 2025-10-05 04:44:00 | NOAA-21 | COLINAS | MARANHÃO | Brasil | 2103505 | 21 | 33 | nan | nan | nan | Cerrado | 1.6 |
| 85b68df3-76c8-35c7-afc4-21783b4cff47 | -3.6128 | -51.03687 | 2025-10-05 04:44:00 | NOAA-21 | PACAJÁ | PARÁ | Brasil | 1505486 | 15 | 33 | nan | nan | nan | Amazônia | 1.7 |
| 5ad56cb9-ae5a-31f0-883d-6e5d0dad7ccc | -6.65826 | -41.60102 | 2025-10-05 04:44:00 | NOAA-21 | INHUMA | PIAUÍ | Brasil | 2204709 | 22 | 33 | nan | nan | nan | Caatinga | 1.4 |
| 33220f25-b450-3fa6-ab56-c3fdb5228d0a | -5.85102 | -43.3791 | 2025-10-05 04:44:00 | NOAA-21 | PARNARAMA | MARANHÃO | Brasil | 2107803 | 21 | 33 | nan | nan | nan | Cerrado | 1.1 |
| ec98f44c-6d51-3773-b0c5-f4ad27e53d70 | -5.22594 | -43.70204 | 2025-10-05 04:44:00 | NOAA-21 | CAXIAS | MARANHÃO | Brasil | 2103000 | 21 | 33 | nan | nan | nan | Cerrado | 3.4 |
| cf15de61-34f8-3910-8db2-96eb4c1013ec | -5.80468 | -45.75679 | 2025-10-05 04:44:00 | NOAA-21 | GRAJAÚ | MARANHÃO | Brasil | 2104800 | 21 | 33 | nan | nan | nan | Cerrado | 3.4 |
| 2c60fcf0-0248-33fa-8f0d-918ec9b5469a | -5.43691 | -45.50909 | 2025-10-05 04:44:00 | NOAA-21 | JENIPAPO DOS VIEIRAS | MARANHÃO | Brasil | 2105476 | 21 | 33 | nan | nan | nan | Cerrado | 1.9 |
| 88da6030-b175-3836-9b82-171794c62cb0 | -6.34909 | -41.63622 | 2025-10-05 04:44:00 | NOAA-21 | VALENÇA DO PIAUÍ | PIAUÍ | Brasil | 2211308 | 22 | 33 | nan | nan | nan | Caatinga | 4.4 |
| 936b0a48-2e93-3672-9b9d-c917d161c923 | -5.23057 | -43.70279 | 2025-10-05 04:44:00 | NOAA-21 | CAXIAS | MARANHÃO | Brasil | 2103000 | 21 | 33 | nan | nan | nan | Cerrado | 1.9 |
| 671cd11f-9add-32e1-a0b5-04cfb68342a8 | -3.49704 | -50.27263 | 2025-10-05 04:44:00 | NOAA-21 | PACAJÁ | PARÁ | Brasil | 1505486 | 15 | 33 | nan | nan | nan | Amazônia | 1.1 |
| 7f53df74-e86d-3973-8bed-7d03c0e0a764 | -6.2505 | -44.24417 | 2025-10-05 04:44:00 | NOAA-21 | MIRADOR | MARANHÃO | Brasil | 2106706 | 21 | 33 | nan | nan | nan | Cerrado | 4.0 |
| 110cd5dd-9aba-39ea-acbe-5b84145d7003 | -3.09302 | -47.02303 | 2025-10-05 04:44:00 | NOAA-21 | PARAGOMINAS | PARÁ | Brasil | 1505502 | 15 | 33 | nan | nan | nan | Amazônia | 1.7 |
| cbfde608-5701-3081-b579-609a1ad1f8d1 | -5.37953 | -45.27554 | 2025-10-05 04:44:00 | NOAA-21 | BARRA DO CORDA | MARANHÃO | Brasil | 2101608 | 21 | 33 | nan | nan | nan | Cerrado | 0.8 |
| 8f592c9f-6c6c-3c99-ba3f-8705564da793 | -5.66382 | -42.69988 | 2025-10-05 04:44:00 | NOAA-21 | MONSENHOR GIL | PIAUÍ | Brasil | 2206407 | 22 | 33 | nan | nan | nan | Caatinga | 1.4 |
| 4d768b1f-4e7e-32ff-94f5-e97b988b31e4 | -6.40078 | -44.779 | 2025-10-05 04:44:00 | NOAA-21 | MIRADOR | MARANHÃO | Brasil | 2106706 | 21 | 33 | nan | nan | nan | Cerrado | 3.6 |
| bdf610e9-7b4a-3067-97e3-7b762a2e89b8 | -3.43529 | -49.49309 | 2025-10-05 04:44:00 | NOAA-21 | BREU BRANCO | PARÁ | Brasil | 1501782 | 15 | 33 | nan | nan | nan | Amazônia | 1.0 |
| caaa7189-6c5d-3708-98ce-79352c5717e1 | -6.40849 | -43.0552 | 2025-10-05 04:44:00 | NOAA-21 | SÃO FRANCISCO DO MARANHÃO | MARANHÃO | Brasil | 2110906 | 21 | 33 | nan | nan | nan | Cerrado | 8.1 |
| 0ea6c825-36d1-3d0e-b077-d6decab99816 | -5.23245 | -42.98639 | 2025-10-05 04:44:00 | NOAA-21 | TIMON | MARANHÃO | Brasil | 2112209 | 21 | 33 | nan | nan | nan | Caatinga | 2.7 |
| 60779d73-a013-3845-97c6-75b469d895d1 | -4.23585 | -46.7536 | 2025-10-05 04:44:00 | NOAA-21 | BOM JARDIM | MARANHÃO | Brasil | 2102002 | 21 | 33 | nan | nan | nan | Amazônia | 3.0 |
| 37479f3f-c2ec-3a52-b835-458b6c3fd918 | -5.22525 | -43.70676 | 2025-10-05 04:44:00 | NOAA-21 | CAXIAS | MARANHÃO | Brasil | 2103000 | 21 | 33 | nan | nan | nan | Cerrado | 3.1 |
| 91e46b17-0352-3850-93db-2db84558e225 | -6.14483 | -44.6797 | 2025-10-05 04:44:00 | NOAA-21 | MIRADOR | MARANHÃO | Brasil | 2106706 | 21 | 33 | nan | nan | nan | Cerrado | 35.9 |
| f892d5f3-de2e-370c-9905-1c66327b0338 | -6.08464 | -46.18647 | 2025-10-05 04:44:00 | NOAA-21 | GRAJAÚ | MARANHÃO | Brasil | 2104800 | 21 | 33 | nan | nan | nan | Cerrado | 1.7 |
| a04564ba-cc32-36fb-81a5-61685894cdec | -5.77119 | -43.98481 | 2025-10-05 04:44:00 | NOAA-21 | BURITI BRAVO | MARANHÃO | Brasil | 2102309 | 21 | 33 | nan | nan | nan | Cerrado | 8.6 |
| 3116116a-84b3-3fcd-9e03-ef31aab43235 | -3.84819 | -41.5726 | 2025-10-05 04:44:00 | NOAA-21 | PIRACURUCA | PIAUÍ | Brasil | 2208304 | 22 | 33 | nan | nan | nan | Caatinga | 17.1 |
| 4793345a-c488-30bf-bcc3-3626736885d5 | -2.94229 | -51.27262 | 2025-10-05 04:44:00 | NOAA-21 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 0.2 |
| 47ca1d12-88de-3227-9023-b6afd9b9128f | -6.12773 | -42.86257 | 2025-10-05 04:44:00 | NOAA-21 | AMARANTE | PIAUÍ | Brasil | 2200509 | 22 | 33 | nan | nan | nan | Caatinga | 3.6 |
| 0a78c6fa-3bca-3c74-ad0d-d67d3acad036 | -2.61808 | -49.40837 | 2025-10-05 04:44:00 | NOAA-21 | MOCAJUBA | PARÁ | Brasil | 1504604 | 15 | 33 | nan | nan | nan | Amazônia | 0.8 |
| 8bf83987-d291-3d3c-98b0-144199ccb1dc | -6.02295 | -44.02726 | 2025-10-05 04:44:00 | NOAA-21 | COLINAS | MARANHÃO | Brasil | 2103505 | 21 | 33 | nan | nan | nan | Cerrado | 3.8 |
| e1afaa9c-7b33-3487-b77a-ddb07f5377e7 | -3.66998 | -41.76046 | 2025-10-05 04:44:00 | NOAA-21 | PIRACURUCA | PIAUÍ | Brasil | 2208304 | 22 | 33 | nan | nan | nan | Caatinga | 1.4 |
| 70f9b4c9-22c7-34a7-8994-9109141ee77e | -3.47198 | -50.32491 | 2025-10-05 04:44:00 | NOAA-21 | PACAJÁ | PARÁ | Brasil | 1505486 | 15 | 33 | nan | nan | nan | Amazônia | 0.6 |
| d5e8995b-484b-3230-a7c8-6747cf6022d4 | -6.41005 | -43.0436 | 2025-10-05 04:44:00 | NOAA-21 | SÃO FRANCISCO DO MARANHÃO | MARANHÃO | Brasil | 2110906 | 21 | 33 | nan | nan | nan | Cerrado | 13.6 |


[Clique aqui para ver as próximas entradas](README75.md)
