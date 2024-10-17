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

## Dados Diários - Página 68

| ID | Latitude | Longitude | Data/Hora GMT | Satélite | Município | Estado | País | Município ID | Estado ID | País ID | Dias sem Chuva | Precipitação | Risco de Fogo | Bioma | FRP |
|----|----------|-----------|---------------|----------|-----------|--------|------|--------------|-----------|---------|----------------|--------------|----------------|-------|-----|
| fababcd1-4bb9-3e65-af40-06058530ffec | -3.36932 | -41.52279 | 2024-10-17 12:25:00 | TERRA_M-T | COCAL | PIAUÍ | Brasil | 2202703 | 22 | 33 | nan | nan | nan | Caatinga | 14.1 |
| 44b364cd-c6a7-33ee-825e-7da6f6759ed9 | -3.37059 | -41.51397 | 2024-10-17 12:25:00 | TERRA_M-T | COCAL | PIAUÍ | Brasil | 2202703 | 22 | 33 | nan | nan | nan | Caatinga | 5.6 |
| a2e9ae84-a48f-36dc-af04-f16cfe227a1e | -3.5155 | -42.17393 | 2024-10-17 12:25:00 | TERRA_M-T | JOAQUIM PIRES | PIAUÍ | Brasil | 2205409 | 22 | 33 | nan | nan | nan | Caatinga | 6.2 |
| 6547afed-f7ec-3cca-8062-4a7002dc6f19 | -3.51701 | -43.23982 | 2024-10-17 12:25:00 | TERRA_M-T | ANAPURUS | MARANHÃO | Brasil | 2100808 | 21 | 33 | nan | nan | nan | Cerrado | 10.2 |
| 78f305ae-8163-3506-8030-28ca935eebfa | -3.7473 | -42.23397 | 2024-10-17 12:25:00 | TERRA_M-T | MORRO DO CHAPÉU DO PIAUÍ | PIAUÍ | Brasil | 2206670 | 22 | 33 | nan | nan | nan | Caatinga | 19.0 |
| 4fd03a68-be4b-33e4-8619-9dee5a55b2f5 | -4.2336 | -41.92215 | 2024-10-17 12:25:00 | TERRA_M-T | PIRIPIRI | PIAUÍ | Brasil | 2208403 | 22 | 33 | nan | nan | nan | Caatinga | 10.4 |
| d9fdb67a-8315-3b78-8ce2-3bf2cb2c78fb | -4.24246 | -41.92339 | 2024-10-17 12:25:00 | TERRA_M-T | PIRIPIRI | PIAUÍ | Brasil | 2208403 | 22 | 33 | nan | nan | nan | Caatinga | 32.1 |
| f8d6ac98-3b26-3f40-8a62-eceb09bb2573 | -4.24374 | -41.91456 | 2024-10-17 12:25:00 | TERRA_M-T | PIRIPIRI | PIAUÍ | Brasil | 2208403 | 22 | 33 | nan | nan | nan | Caatinga | 12.7 |
| c6c8d5fc-09be-3b13-b6ff-f1b02e382af2 | -4.65368 | -42.9043 | 2024-10-17 12:25:00 | TERRA_M-T | UNIÃO | PIAUÍ | Brasil | 2211100 | 22 | 33 | nan | nan | nan | Cerrado | 8.0 |
| d433be17-7a27-3c6e-b9bb-2a24c32eb3a0 | -6.06863 | -43.82543 | 2024-10-17 12:25:00 | TERRA_M-T | PASSAGEM FRANCA | MARANHÃO | Brasil | 2107902 | 21 | 33 | nan | nan | nan | Cerrado | 6.3 |
| 16a895d3-3ed8-3075-89f2-429f1788dee5 | -6.3761 | -40.47951 | 2024-10-17 12:25:00 | TERRA_M-T | PARAMBU | CEARÁ | Brasil | 2310308 | 23 | 33 | nan | nan | nan | Caatinga | 17.4 |
| ef9c5fd6-eb07-3295-9102-46b67266cca0 | -6.37752 | -40.46954 | 2024-10-17 12:25:00 | TERRA_M-T | PARAMBU | CEARÁ | Brasil | 2310308 | 23 | 33 | nan | nan | nan | Caatinga | 21.3 |
| f6086ab8-fb0d-3fbe-8bb7-9d64450e8de6 | -6.63893 | -40.95797 | 2024-10-17 12:25:00 | TERRA_M-T | PIMENTEIRAS | PIAUÍ | Brasil | 2208106 | 22 | 33 | nan | nan | nan | Caatinga | 15.3 |
| 3f2ba129-fb14-30e8-8a00-3c1d91b13b3a | -3.41461 | -44.45911 | 2024-10-17 12:25:00 | TERRA_M-T | ITAPECURU MIRIM | MARANHÃO | Brasil | 2105401 | 21 | 33 | nan | nan | nan | Cerrado | 11.1 |
| 01ddb678-ec75-307d-91f7-300bd71170c0 | -3.62155 | -44.40158 | 2024-10-17 12:25:00 | TERRA_M-T | CANTANHEDE | MARANHÃO | Brasil | 2102705 | 21 | 33 | nan | nan | nan | Cerrado | 16.1 |
| 7d721813-8259-3a3f-983d-9975ae2b14a7 | -4.13706 | -44.03594 | 2024-10-17 12:25:00 | TERRA_M-T | COROATÁ | MARANHÃO | Brasil | 2103604 | 21 | 33 | nan | nan | nan | Cerrado | 11.2 |
| baf76918-6008-39c9-82cb-e38c9cf68951 | -5.5684 | -44.88303 | 2024-10-17 12:25:00 | TERRA_M-T | TUNTUM | MARANHÃO | Brasil | 2112308 | 21 | 33 | nan | nan | nan | Cerrado | 33.6 |
| 1372ce31-719e-3fff-946b-afc1760d0abc | -5.57797 | -44.88438 | 2024-10-17 12:25:00 | TERRA_M-T | TUNTUM | MARANHÃO | Brasil | 2112308 | 21 | 33 | nan | nan | nan | Cerrado | 127.4 |
| fcf6c94a-8530-3bcd-aaa5-6606ae6e5e8a | -5.57955 | -44.87393 | 2024-10-17 12:25:00 | TERRA_M-T | TUNTUM | MARANHÃO | Brasil | 2112308 | 21 | 33 | nan | nan | nan | Cerrado | 14.2 |
| 8335bdde-f3ec-30a1-94f4-369d53580faf | -5.97605 | -45.36639 | 2024-10-17 12:25:00 | TERRA_M-T | FERNANDO FALCÃO | MARANHÃO | Brasil | 2104081 | 21 | 33 | nan | nan | nan | Cerrado | 21.0 |
| 96c77358-7b4a-328e-bc0c-0f83231ce782 | -5.98585 | -45.36775 | 2024-10-17 12:25:00 | TERRA_M-T | FERNANDO FALCÃO | MARANHÃO | Brasil | 2104081 | 21 | 33 | nan | nan | nan | Cerrado | 62.7 |
| 616d1e02-7da0-3e01-846a-6c07eec14698 | -6.68789 | -42.16337 | 2024-10-17 12:27:00 | TERRA_M-T | TANQUE DO PIAUÍ | PIAUÍ | Brasil | 2210979 | 22 | 33 | nan | nan | nan | Caatinga | 5.3 |
| a4629359-a40b-3f80-982a-9cd3a25dc126 | -6.68917 | -42.15446 | 2024-10-17 12:27:00 | TERRA_M-T | TANQUE DO PIAUÍ | PIAUÍ | Brasil | 2210979 | 22 | 33 | nan | nan | nan | Caatinga | 11.1 |
| 4cf0d89b-b0b0-3db7-aae6-78a69e0ddc50 | -7.00598 | -41.55407 | 2024-10-17 12:27:00 | TERRA_M-T | PICOS | PIAUÍ | Brasil | 2208007 | 22 | 33 | nan | nan | nan | Caatinga | 7.7 |
| b88b9f11-8c6f-30e6-9246-4675da9db92e | -7.78586 | -37.15 | 2024-10-17 12:27:00 | TERRA_M-T | MONTEIRO | PARAÍBA | Brasil | 2509701 | 25 | 33 | nan | nan | nan | Caatinga | 18.4 |
| ce1866fc-e00a-3dd0-8411-0bffdb809d2e | -8.14835 | -45.0304 | 2024-10-17 12:27:00 | TERRA_M-T | BAIXA GRANDE DO RIBEIRO | PIAUÍ | Brasil | 2201150 | 22 | 33 | nan | nan | nan | Cerrado | 8.5 |
| 1727960e-c244-36be-98e7-2b7925c3fcf1 | -8.72496 | -41.25007 | 2024-10-17 12:27:00 | TERRA_M-T | CASA NOVA | BAHIA | Brasil | 2907202 | 29 | 33 | nan | nan | nan | Caatinga | 12.2 |
| c7281dda-e84b-3192-97e4-829e8ae4e6ea | -8.72633 | -41.24028 | 2024-10-17 12:27:00 | TERRA_M-T | CASA NOVA | BAHIA | Brasil | 2907202 | 29 | 33 | nan | nan | nan | Caatinga | 13.6 |
| 81361513-b735-394b-955c-04f8aedc40f6 | -8.80345 | -41.34641 | 2024-10-17 12:27:00 | TERRA_M-T | CASA NOVA | BAHIA | Brasil | 2907202 | 29 | 33 | nan | nan | nan | Caatinga | 11.4 |
| cb6d1928-3fc4-3fbc-948f-a5400de9c626 | -12.63615 | -46.38984 | 2024-10-17 12:27:00 | TERRA_M-T | AURORA DO TOCANTINS | TOCANTINS | Brasil | 1702703 | 17 | 33 | nan | nan | nan | Cerrado | 13.7 |
| e739c648-f392-39c2-9a86-d7b6a200f787 | -11.73776 | -52.45821 | 2024-10-17 12:27:00 | TERRA_M-T | QUERÊNCIA | MATO GROSSO | Brasil | 5107065 | 51 | 33 | nan | nan | nan | Amazônia | 31.1 |
| 038fc0a2-5c03-3505-a58e-8b6fa33e3a7c | -19.29582 | -46.1669 | 2024-10-17 12:29:00 | TERRA_M-T | RIO PARANAÍBA | MINAS GERAIS | Brasil | 3155504 | 31 | 33 | nan | nan | nan | Cerrado | 14.6 |
| a3d76a33-76dc-3306-8dc1-12e87375e4e1 | -19.29723 | -46.15737 | 2024-10-17 12:29:00 | TERRA_M-T | RIO PARANAÍBA | MINAS GERAIS | Brasil | 3155504 | 31 | 33 | nan | nan | nan | Cerrado | 14.1 |
| 13d17a05-4a5c-3ccc-969d-0e5afc0fff7a | -19.79178 | -42.1442 | 2024-10-17 12:29:00 | TERRA_M-T | CARATINGA | MINAS GERAIS | Brasil | 3113404 | 31 | 33 | nan | nan | nan | Mata Atlântica | 8.4 |
| 2909e6b8-5523-36f6-b939-c4f19d897a9b | -19.84498 | -44.46523 | 2024-10-17 12:29:00 | TERRA_M-T | FLORESTAL | MINAS GERAIS | Brasil | 3126000 | 31 | 33 | nan | nan | nan | Cerrado | 6.8 |
| 0abb6467-d6dc-30c2-893e-72270d5cb535 | -20.02656 | -42.22014 | 2024-10-17 12:29:00 | TERRA_M-T | VERMELHO NOVO | MINAS GERAIS | Brasil | 3171154 | 31 | 33 | nan | nan | nan | Mata Atlântica | 14.7 |
| 10827bb5-ee4c-3095-9829-65effae6af53 | -20.02731 | -42.21395 | 2024-10-17 12:29:00 | TERRA_M-T | VERMELHO NOVO | MINAS GERAIS | Brasil | 3171154 | 31 | 33 | nan | nan | nan | Mata Atlântica | 10.9 |
| b2efb52e-ad5e-34b9-9065-a67270547afe | -20.05645 | -41.38546 | 2024-10-17 12:29:00 | TERRA_M-T | MUTUM | MINAS GERAIS | Brasil | 3144003 | 31 | 33 | nan | nan | nan | Mata Atlântica | 6.9 |
| c202f6fd-1460-38fd-93d8-32a203dc51a6 | -20.07976 | -41.95247 | 2024-10-17 12:29:00 | TERRA_M-T | SIMONÉSIA | MINAS GERAIS | Brasil | 3167608 | 31 | 33 | nan | nan | nan | Mata Atlântica | 7.9 |
| 24e6bffe-53be-3334-bdaf-be666a9199f2 | -20.33946 | -41.21694 | 2024-10-17 12:29:00 | TERRA_M-T | CONCEIÇÃO DO CASTELO | ESPÍRITO SANTO | Brasil | 3201704 | 32 | 33 | nan | nan | nan | Mata Atlântica | 8.5 |
| 4571ba31-2afe-368d-98ae-f4c3cd111183 | -20.38912 | -44.11918 | 2024-10-17 12:29:00 | TERRA_M-T | BELO VALE | MINAS GERAIS | Brasil | 3106408 | 31 | 33 | nan | nan | nan | Mata Atlântica | 8.7 |
| 728f8640-ad3c-3a2f-80a3-8c8ef26fd4ee | -20.3924 | -41.89715 | 2024-10-17 12:29:00 | TERRA_M-T | ALTO JEQUITIBÁ | MINAS GERAIS | Brasil | 3153509 | 31 | 33 | nan | nan | nan | Mata Atlântica | 12.3 |
| f94818b8-863e-3768-9c8e-b4a53fc9535f | -20.43171 | -46.21955 | 2024-10-17 12:29:00 | TERRA_M-T | PIUMHI | MINAS GERAIS | Brasil | 3151503 | 31 | 33 | nan | nan | nan | Cerrado | 32.9 |
| 7937f37c-e630-31ac-a716-d7ef794271ac | -20.43312 | -46.21006 | 2024-10-17 12:29:00 | TERRA_M-T | PIUMHI | MINAS GERAIS | Brasil | 3151503 | 31 | 33 | nan | nan | nan | Cerrado | 7.0 |
| cbee3d15-e6e5-3358-a778-4fff6d8d9dd1 | -20.56285 | -42.80717 | 2024-10-17 12:29:00 | TERRA_M-T | AMPARO DO SERRA | MINAS GERAIS | Brasil | 3102506 | 31 | 33 | nan | nan | nan | Mata Atlântica | 6.6 |
| 12e77bc1-9647-3ced-9efb-8847a1779437 | -20.86284 | -45.01939 | 2024-10-17 12:29:00 | TERRA_M-T | SANTANA DO JACARÉ | MINAS GERAIS | Brasil | 3158805 | 31 | 33 | nan | nan | nan | Mata Atlântica | 6.1 |
| b9863053-00ac-3189-aeb3-2366dbc2f20e | -20.86417 | -45.00988 | 2024-10-17 12:29:00 | TERRA_M-T | SANTANA DO JACARÉ | MINAS GERAIS | Brasil | 3158805 | 31 | 33 | nan | nan | nan | Mata Atlântica | 7.1 |
| a611386b-b6d4-37ac-8c79-2318c41da7b2 | -21.16683 | -43.02629 | 2024-10-17 12:29:00 | TERRA_M-T | TOCANTINS | MINAS GERAIS | Brasil | 3169000 | 31 | 33 | nan | nan | nan | Mata Atlântica | 6.7 |
| 66546f74-f918-3343-a9bb-15473effa33a | -16.12659 | -46.39197 | 2024-10-17 12:29:00 | TERRA_M-T | UNAÍ | MINAS GERAIS | Brasil | 3170404 | 31 | 33 | nan | nan | nan | Cerrado | 30.6 |
| 7820045c-fa95-3f72-b9ab-7fe26c78c3b1 | -16.1281 | -46.38202 | 2024-10-17 12:29:00 | TERRA_M-T | URUANA DE MINAS | MINAS GERAIS | Brasil | 3170479 | 31 | 33 | nan | nan | nan | Cerrado | 14.5 |
| d74d35fc-8669-390f-bfea-86890d131ea7 | -16.13448 | -46.38954 | 2024-10-17 12:29:00 | TERRA_M-T | UNAÍ | MINAS GERAIS | Brasil | 3170404 | 31 | 33 | nan | nan | nan | Cerrado | 22.2 |
| cd148366-fb8e-3294-a7f7-75beb3491c2f | -16.44146 | -42.2615 | 2024-10-17 12:29:00 | TERRA_M-T | RUBELITA | MINAS GERAIS | Brasil | 3156502 | 31 | 33 | nan | nan | nan | Mata Atlântica | 11.7 |
| 1f8e5cc8-459a-3260-b843-3e90361e7cae | -16.84435 | -41.99681 | 2024-10-17 12:29:00 | TERRA_M-T | ARAÇUAÍ | MINAS GERAIS | Brasil | 3103405 | 31 | 33 | nan | nan | nan | Mata Atlântica | 16.5 |
| 4d865c09-4a9b-38b9-8671-16ddd4cd6f3f | -16.94259 | -41.96643 | 2024-10-17 12:29:00 | TERRA_M-T | ARAÇUAÍ | MINAS GERAIS | Brasil | 3103405 | 31 | 33 | nan | nan | nan | Mata Atlântica | 7.0 |
| 0ff0e754-bf84-3042-94f3-d5ab8b90c904 | -17.30808 | -44.43886 | 2024-10-17 12:29:00 | TERRA_M-T | JEQUITAÍ | MINAS GERAIS | Brasil | 3135605 | 31 | 33 | nan | nan | nan | Cerrado | 8.3 |
| c8300f3b-79f8-3403-b5d6-ce6eafbabe95 | -17.3094 | -44.42962 | 2024-10-17 12:29:00 | TERRA_M-T | JEQUITAÍ | MINAS GERAIS | Brasil | 3135605 | 31 | 33 | nan | nan | nan | Cerrado | 5.7 |
| 83c12f89-1a0c-38dc-ac62-34c968055153 | -17.31699 | -44.4402 | 2024-10-17 12:29:00 | TERRA_M-T | JEQUITAÍ | MINAS GERAIS | Brasil | 3135605 | 31 | 33 | nan | nan | nan | Cerrado | 8.1 |
| c33d36be-a46c-37ed-8d8c-66b85ada413a | -17.46513 | -42.89177 | 2024-10-17 12:29:00 | TERRA_M-T | CARBONITA | MINAS GERAIS | Brasil | 3113503 | 31 | 33 | nan | nan | nan | Cerrado | 11.3 |
| 4f7c19f5-f262-3eb1-aa91-1c7f6147d830 | -17.88455 | -45.92455 | 2024-10-17 12:29:00 | TERRA_M-T | JOÃO PINHEIRO | MINAS GERAIS | Brasil | 3136306 | 31 | 33 | nan | nan | nan | Cerrado | 5.8 |
| 10cb886a-ed0c-31a7-941a-cd7859ccda4e | -17.98268 | -43.42612 | 2024-10-17 12:29:00 | TERRA_M-T | COUTO DE MAGALHÃES DE MINAS | MINAS GERAIS | Brasil | 3120102 | 31 | 33 | nan | nan | nan | Cerrado | 22.8 |
| 0d3c5947-9cb0-3709-8489-94b220ab35fc | -17.99186 | -43.42743 | 2024-10-17 12:29:00 | TERRA_M-T | SÃO GONÇALO DO RIO PRETO | MINAS GERAIS | Brasil | 3125507 | 31 | 33 | nan | nan | nan | Cerrado | 6.8 |
| b8d52a69-0454-3c05-85ef-64a6a70b777a | -17.99285 | -45.377 | 2024-10-17 12:29:00 | TERRA_M-T | SÃO GONÇALO DO ABAETÉ | MINAS GERAIS | Brasil | 3161700 | 31 | 33 | nan | nan | nan | Cerrado | 10.8 |
| c6d33456-a4cb-332c-a423-87220d24ee74 | -17.9942 | -45.36772 | 2024-10-17 12:29:00 | TERRA_M-T | SÃO GONÇALO DO ABAETÉ | MINAS GERAIS | Brasil | 3161700 | 31 | 33 | nan | nan | nan | Cerrado | 15.7 |
| 83dca2ac-8586-39c8-9683-efd047d84cfc | -18.08827 | -42.7085 | 2024-10-17 12:29:00 | TERRA_M-T | ITAMARANDIBA | MINAS GERAIS | Brasil | 3132503 | 31 | 33 | nan | nan | nan | Mata Atlântica | 13.0 |
| 03c9db85-3546-3d2a-959b-ef7e0c34f942 | -18.12836 | -42.62554 | 2024-10-17 12:29:00 | TERRA_M-T | SÃO SEBASTIÃO DO MARANHÃO | MINAS GERAIS | Brasil | 3164506 | 31 | 33 | nan | nan | nan | Mata Atlântica | 14.5 |
| cfa0b3c5-6ce3-33e6-9160-f7068083b080 | -18.17479 | -42.44929 | 2024-10-17 12:29:00 | TERRA_M-T | SANTA MARIA DO SUAÇUÍ | MINAS GERAIS | Brasil | 3158201 | 31 | 33 | nan | nan | nan | Mata Atlântica | 9.8 |
| e0cdf6ee-7398-3d67-8f0d-d31ce262f09e | -18.18444 | -42.45055 | 2024-10-17 12:29:00 | TERRA_M-T | SANTA MARIA DO SUAÇUÍ | MINAS GERAIS | Brasil | 3158201 | 31 | 33 | nan | nan | nan | Mata Atlântica | 6.2 |
| 5980201e-4638-3b83-aa9e-859478983ad4 | -18.2392 | -47.40855 | 2024-10-17 12:29:00 | TERRA_M-T | ABADIA DOS DOURADOS | MINAS GERAIS | Brasil | 3100104 | 31 | 33 | nan | nan | nan | Cerrado | 39.6 |
| 35842e12-a925-3bf5-8b2a-240da037ca90 | -18.29466 | -43.01314 | 2024-10-17 12:29:00 | TERRA_M-T | RIO VERMELHO | MINAS GERAIS | Brasil | 3156007 | 31 | 33 | nan | nan | nan | Mata Atlântica | 7.6 |
| 48dba4c2-2925-3bcb-a2ce-6daa89d05d88 | -18.66858 | -47.86435 | 2024-10-17 12:29:00 | TERRA_M-T | CASCALHO RICO | MINAS GERAIS | Brasil | 3115003 | 31 | 33 | nan | nan | nan | Cerrado | 83.0 |
| 8cfaadab-52e5-30b5-9f88-3b7f2be9f375 | -18.67028 | -47.85346 | 2024-10-17 12:29:00 | TERRA_M-T | ESTRELA DO SUL | MINAS GERAIS | Brasil | 3124807 | 31 | 33 | nan | nan | nan | Cerrado | 76.8 |
| 238f2695-273d-3713-9517-16d154432a2d | -18.67293 | -47.86059 | 2024-10-17 12:29:00 | TERRA_M-T | CASCALHO RICO | MINAS GERAIS | Brasil | 3115003 | 31 | 33 | nan | nan | nan | Cerrado | 52.4 |
| cd88fc54-bdfc-309e-92ef-965cae4988a0 | -18.9864 | -46.2638 | 2024-10-17 12:29:00 | TERRA_M-T | CARMO DO PARANAÍBA | MINAS GERAIS | Brasil | 3114303 | 31 | 33 | nan | nan | nan | Cerrado | 59.1 |
| 3bddbb19-c278-3c5a-98ac-273ad737296f | -18.98783 | -46.25425 | 2024-10-17 12:29:00 | TERRA_M-T | CARMO DO PARANAÍBA | MINAS GERAIS | Brasil | 3114303 | 31 | 33 | nan | nan | nan | Cerrado | 147.8 |
| 4303be00-e69b-3fc0-a8d2-e44d44ca88e4 | -18.9968 | -46.25567 | 2024-10-17 12:29:00 | TERRA_M-T | CARMO DO PARANAÍBA | MINAS GERAIS | Brasil | 3114303 | 31 | 33 | nan | nan | nan | Cerrado | 14.3 |
| f3883061-3899-3e43-b356-d617c7bab5a0 | -19.01892 | -46.29465 | 2024-10-17 12:29:00 | TERRA_M-T | CARMO DO PARANAÍBA | MINAS GERAIS | Brasil | 3114303 | 31 | 33 | nan | nan | nan | Cerrado | 152.3 |
| a8810b49-604d-38c9-82eb-04af3faf4491 | -19.02036 | -46.28513 | 2024-10-17 12:29:00 | TERRA_M-T | CARMO DO PARANAÍBA | MINAS GERAIS | Brasil | 3114303 | 31 | 33 | nan | nan | nan | Cerrado | 24.3 |
| c3abfe65-ae05-392c-8e7e-adc6da81a4ef | -19.02789 | -46.29615 | 2024-10-17 12:29:00 | TERRA_M-T | CARMO DO PARANAÍBA | MINAS GERAIS | Brasil | 3114303 | 31 | 33 | nan | nan | nan | Cerrado | 47.7 |
| a0945e5a-c42f-375f-b6ef-ffcab49b5548 | -19.02933 | -46.28661 | 2024-10-17 12:29:00 | TERRA_M-T | CARMO DO PARANAÍBA | MINAS GERAIS | Brasil | 3114303 | 31 | 33 | nan | nan | nan | Cerrado | 12.5 |
| 904bf6ae-5f19-3607-a6d0-db24f423d8e6 | -19.04322 | -46.13292 | 2024-10-17 12:29:00 | TERRA_M-T | ARAPUÁ | MINAS GERAIS | Brasil | 3103801 | 31 | 33 | nan | nan | nan | Cerrado | 19.6 |
| 1918ffe5-247b-3a77-b2d8-9748899e82cd | -19.19576 | -46.71228 | 2024-10-17 12:29:00 | TERRA_M-T | SERRA DO SALITRE | MINAS GERAIS | Brasil | 3166808 | 31 | 33 | nan | nan | nan | Cerrado | 135.3 |
| e752b1e1-f434-3abe-a3b1-a6282303ed02 | -19.19723 | -46.70255 | 2024-10-17 12:29:00 | TERRA_M-T | SERRA DO SALITRE | MINAS GERAIS | Brasil | 3166808 | 31 | 33 | nan | nan | nan | Cerrado | 30.4 |
| b92618dd-f1a6-38c2-8198-0f519edb2856 | -19.22999 | -46.60831 | 2024-10-17 12:29:00 | TERRA_M-T | SERRA DO SALITRE | MINAS GERAIS | Brasil | 3166808 | 31 | 33 | nan | nan | nan | Cerrado | 5.7 |
| 716c9df1-834b-3c8d-ad2c-87aa3f2b6283 | -1.1346 | -49.1698 | 2024-10-17 13:15:12 | GOES-16 | PONTA DE PEDRAS | PARÁ | Brasil | 1505700 | 15 | 33 | nan | nan | nan | Amazônia | 64.1 |
| 35a4098a-c95a-3b65-86f8-d99cad7b210e | -1.1161 | -49.17 | 2024-10-17 13:25:12 | GOES-16 | PONTA DE PEDRAS | PARÁ | Brasil | 1505700 | 15 | 33 | nan | nan | nan | Amazônia | 59.5 |
| 179b3cb2-54d5-3d22-abf8-e266b5499ec4 | -1.1346 | -49.1698 | 2024-10-17 13:35:12 | GOES-16 | PONTA DE PEDRAS | PARÁ | Brasil | 1505700 | 15 | 33 | nan | nan | nan | Amazônia | 75.2 |
| 62cd8cb8-2272-3cec-b627-54dacf3ee9e6 | -1.1161 | -49.17 | 2024-10-17 13:35:12 | GOES-16 | PONTA DE PEDRAS | PARÁ | Brasil | 1505700 | 15 | 33 | nan | nan | nan | Amazônia | 61.6 |
| 42d608ba-1e06-3582-9151-7dd717a6de59 | -0.766 | -48.7042 | 2024-10-17 13:45:10 | GOES-16 | SALVATERRA | PARÁ | Brasil | 1506302 | 15 | 33 | nan | nan | nan | Amazônia | 61.3 |
| f7c1f2ca-83a6-35f1-affb-c8b52b34c105 | -1.1346 | -49.1698 | 2024-10-17 13:45:12 | GOES-16 | PONTA DE PEDRAS | PARÁ | Brasil | 1505700 | 15 | 33 | nan | nan | nan | Amazônia | 80.1 |
| 669a8059-f1d7-3c0d-bf01-ac7f701154db | -1.1161 | -49.17 | 2024-10-17 13:45:12 | GOES-16 | PONTA DE PEDRAS | PARÁ | Brasil | 1505700 | 15 | 33 | nan | nan | nan | Amazônia | 64.0 |
| 5b7e4370-6563-3c18-901e-f8c39b43245f | -1.1161 | -49.17 | 2024-10-17 13:55:12 | GOES-16 | PONTA DE PEDRAS | PARÁ | Brasil | 1505700 | 15 | 33 | nan | nan | nan | Amazônia | 67.5 |
| 01d2ae18-40ee-3ebc-bd2d-c7cd06e9f495 | -1.1346 | -49.1698 | 2024-10-17 13:55:12 | GOES-16 | PONTA DE PEDRAS | PARÁ | Brasil | 1505700 | 15 | 33 | nan | nan | nan | Amazônia | 84.4 |
| 4dec3311-420c-3101-ba5c-67c2c9e0b987 | -1.1345 | -49.1911 | 2024-10-17 13:55:12 | GOES-16 | PONTA DE PEDRAS | PARÁ | Brasil | 1505700 | 15 | 33 | nan | nan | nan | Amazônia | 72.1 |
| 017e98b5-9e67-368f-9fd6-59bff275fe89 | -1.153 | -49.1696 | 2024-10-17 13:55:13 | GOES-16 | PONTA DE PEDRAS | PARÁ | Brasil | 1505700 | 15 | 33 | nan | nan | nan | Amazônia | 73.7 |
| 302233bf-2024-3500-ba20-2aba5a6c025d | -2.4665 | -48.3531 | 2024-10-17 13:55:20 | GOES-16 | TOMÉ-AÇU | PARÁ | Brasil | 1508001 | 15 | 33 | nan | nan | nan | Amazônia | 62.7 |
| 83dc9163-7fde-377c-8de4-e6ba6f294129 | -2.6303 | -49.0767 | 2024-10-17 13:55:21 | GOES-16 | MOJU | PARÁ | Brasil | 1504703 | 15 | 33 | nan | nan | nan | Amazônia | 62.8 |
| 0d4f2f8b-d800-3d17-bbd4-26dc267825f4 | -3.0949 | -44.3677 | 2024-10-17 13:55:24 | GOES-16 | SANTA RITA | MARANHÃO | Brasil | 2110203 | 21 | 33 | nan | nan | nan | Amazônia | 74.0 |
| 49005ccc-c8e6-3aea-9e6a-318426d27ee7 | -3.7007 | -45.9223 | 2024-10-17 13:55:27 | GOES-16 | ALTO ALEGRE DO PINDARÉ | MARANHÃO | Brasil | 2100477 | 21 | 33 | nan | nan | nan | Amazônia | 76.9 |
| 3f007097-273c-3bd6-a719-aa8aa5054e74 | -2.4665 | -48.3531 | 2024-10-17 14:05:20 | GOES-16 | TOMÉ-AÇU | PARÁ | Brasil | 1508001 | 15 | 33 | nan | nan | nan | Amazônia | 68.6 |
| 52c34dff-ef72-345d-b915-2e9beaa6cfe9 | -2.6303 | -49.0767 | 2024-10-17 14:05:21 | GOES-16 | MOJU | PARÁ | Brasil | 1504703 | 15 | 33 | nan | nan | nan | Amazônia | 79.6 |


[Clique aqui para ver as próximas entradas](README69.md)
