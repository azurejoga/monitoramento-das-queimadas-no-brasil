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

## Dados Diários - Página 27

| ID | Latitude | Longitude | Data/Hora GMT | Satélite | Município | Estado | País | Município ID | Estado ID | País ID | Dias sem Chuva | Precipitação | Risco de Fogo | Bioma | FRP |
|----|----------|-----------|---------------|----------|-----------|--------|------|--------------|-----------|---------|----------------|--------------|----------------|-------|-----|
| cdc544f5-bbd3-3caa-b1d5-b511252872e2 | -8.50326 | -43.2981 | 2025-07-09 12:29:00 | TERRA_M-T | CANTO DO BURITI | PIAUÍ | Brasil | 2202307 | 22 | 33 | nan | nan | nan | Caatinga | 22.1 |
| 2e0cc2de-e49e-37ea-b113-0e3cf4ffc3e9 | -7.64813 | -45.35598 | 2025-07-09 12:29:00 | TERRA_M-T | RIBEIRO GONÇALVES | PIAUÍ | Brasil | 2208908 | 22 | 33 | nan | nan | nan | Cerrado | 5.7 |
| 590245fa-c8dc-338d-8770-1c8cbbc12524 | -6.98007 | -47.08628 | 2025-07-09 12:29:00 | TERRA_M-T | ESTREITO | MARANHÃO | Brasil | 2104057 | 21 | 33 | nan | nan | nan | Cerrado | 8.3 |
| b7bbc649-22bc-3603-8a9f-88a80c940d28 | -7.38211 | -47.04547 | 2025-07-09 12:29:00 | TERRA_M-T | CAROLINA | MARANHÃO | Brasil | 2102804 | 21 | 33 | nan | nan | nan | Cerrado | 5.8 |
| 322c7fd9-321a-3c2d-84a6-21f6fa7920c2 | -6.57521 | -48.23508 | 2025-07-09 12:29:00 | TERRA_M-T | PIRAQUÊ | TOCANTINS | Brasil | 1717206 | 17 | 33 | nan | nan | nan | Amazônia | 7.8 |
| 5e27f8a4-7a40-36a2-b739-ab37ee58d225 | -12.09933 | -44.74477 | 2025-07-09 12:29:00 | TERRA_M-T | ANGICAL | BAHIA | Brasil | 2901403 | 29 | 33 | nan | nan | nan | Cerrado | 19.0 |
| 3ab500e5-4f9c-3888-b728-52aa150ff545 | -8.74358 | -50.26431 | 2025-07-09 12:29:00 | TERRA_M-T | SANTA MARIA DAS BARREIRAS | PARÁ | Brasil | 1506583 | 15 | 33 | nan | nan | nan | Amazônia | 5.0 |
| 9063f730-a7aa-3c6a-9fe3-2de53269bf12 | -11.67118 | -43.78168 | 2025-07-09 12:29:00 | TERRA_M-T | WANDERLEY | BAHIA | Brasil | 2933455 | 29 | 33 | nan | nan | nan | Cerrado | 19.4 |
| 10d9e691-1a67-3188-a22d-a9b3d680eea0 | -6.41649 | -41.22525 | 2025-07-09 12:29:00 | TERRA_M-T | PIMENTEIRAS | PIAUÍ | Brasil | 2208106 | 22 | 33 | nan | nan | nan | Caatinga | 27.3 |
| f722500f-ef41-3c88-8edd-600202136b9d | -14.27322 | -47.3824 | 2025-07-09 12:29:00 | TERRA_M-T | SÃO JOÃO D'ALIANÇA | GOIÁS | Brasil | 5220009 | 52 | 33 | nan | nan | nan | Cerrado | 6.5 |
| 2bd3d5c8-c92a-39bb-bddd-345aba20f0f8 | -6.83511 | -43.34448 | 2025-07-09 12:29:00 | TERRA_M-T | FLORIANO | PIAUÍ | Brasil | 2203909 | 22 | 33 | nan | nan | nan | Caatinga | 12.4 |
| 960dd9cc-34bc-3ea8-b363-d31ab0ca9268 | -7.08592 | -44.38691 | 2025-07-09 12:29:00 | TERRA_M-T | BENEDITO LEITE | MARANHÃO | Brasil | 2101806 | 21 | 33 | nan | nan | nan | Cerrado | 102.7 |
| 6fa5be97-b0a0-30ad-b054-2308911f13e9 | -10.67795 | -47.20577 | 2025-07-09 12:29:00 | TERRA_M-T | PONTE ALTA DO TOCANTINS | TOCANTINS | Brasil | 1717909 | 17 | 33 | nan | nan | nan | Cerrado | 8.5 |
| 85c080b0-e68a-3bd1-bcd3-20fa0899b066 | -10.64275 | -44.48774 | 2025-07-09 12:29:00 | TERRA_M-T | PARNAGUÁ | PIAUÍ | Brasil | 2207603 | 22 | 33 | nan | nan | nan | Cerrado | 17.6 |
| 77d93633-04a0-3a28-9eed-d799b9326cfa | -5.98923 | -45.36103 | 2025-07-09 12:29:00 | TERRA_M-T | FERNANDO FALCÃO | MARANHÃO | Brasil | 2104081 | 21 | 33 | nan | nan | nan | Cerrado | 11.2 |
| 73781c74-7634-3374-bc77-261899b2f7ba | -6.89907 | -47.39069 | 2025-07-09 12:29:00 | TERRA_M-T | ESTREITO | MARANHÃO | Brasil | 2104057 | 21 | 33 | nan | nan | nan | Cerrado | 5.2 |
| 06d34e39-9937-3dae-8998-9d0721e2cb58 | -7.18828 | -48.33848 | 2025-07-09 12:29:00 | TERRA_M-T | ARAGUAÍNA | TOCANTINS | Brasil | 1702109 | 17 | 33 | nan | nan | nan | Amazônia | 21.4 |
| 480e759e-023f-313d-93c1-c4170c2c07e2 | -14.52264 | -39.8577 | 2025-07-09 12:29:00 | TERRA_M-T | IBICUÍ | BAHIA | Brasil | 2912301 | 29 | 33 | nan | nan | nan | Mata Atlântica | 36.9 |
| db969c32-605f-388a-929b-8574d5a2c276 | -11.05512 | -50.49137 | 2025-07-09 12:29:00 | TERRA_M-T | LAGOA DA CONFUSÃO | TOCANTINS | Brasil | 1711902 | 17 | 33 | nan | nan | nan | Cerrado | 6.5 |
| b1e3eb8f-3fac-3ee9-b5e6-944ff12c8b1f | -15.60977 | -43.92096 | 2025-07-09 12:29:00 | TERRA_M-T | VARZELÂNDIA | MINAS GERAIS | Brasil | 3170909 | 31 | 33 | nan | nan | nan | Caatinga | 10.7 |
| 2f145d9b-7ed6-32bc-843c-47cb30ce9849 | -6.14145 | -43.97285 | 2025-07-09 12:29:00 | TERRA_M-T | COLINAS | MARANHÃO | Brasil | 2103505 | 21 | 33 | nan | nan | nan | Cerrado | 24.1 |
| df939ecb-63d4-36eb-b7be-d832dc94defb | -7.23862 | -43.06301 | 2025-07-09 12:29:00 | TERRA_M-T | FLORIANO | PIAUÍ | Brasil | 2203909 | 22 | 33 | nan | nan | nan | Caatinga | 14.7 |
| 2cda6be6-99b9-3dfd-b8fb-bb4a3ec91ddb | -6.89019 | -47.38949 | 2025-07-09 12:29:00 | TERRA_M-T | ESTREITO | MARANHÃO | Brasil | 2104057 | 21 | 33 | nan | nan | nan | Cerrado | 7.9 |
| c3447f00-8755-3d06-aed3-2bd1f27a5d64 | -10.23981 | -47.30608 | 2025-07-09 12:29:00 | TERRA_M-T | NOVO ACORDO | TOCANTINS | Brasil | 1715101 | 17 | 33 | nan | nan | nan | Cerrado | 8.3 |
| 54ab34fc-3e43-3428-b48a-b03c629bc326 | -7.08731 | -49.15965 | 2025-07-09 12:29:00 | TERRA_M-T | SANTA FÉ DO ARAGUAIA | TOCANTINS | Brasil | 1718865 | 17 | 33 | nan | nan | nan | Amazônia | 5.9 |
| db5972e8-e200-3de9-898e-93c3f7c5cfe0 | -9.19905 | -47.63338 | 2025-07-09 12:29:00 | TERRA_M-T | CENTENÁRIO | TOCANTINS | Brasil | 1704105 | 17 | 33 | nan | nan | nan | Cerrado | 38.0 |
| 1b081e10-eee4-309a-bfff-819cb4d3644b | -7.56993 | -46.16272 | 2025-07-09 12:29:00 | TERRA_M-T | BALSAS | MARANHÃO | Brasil | 2101400 | 21 | 33 | nan | nan | nan | Cerrado | 5.7 |
| a9d4e754-2f42-3253-9365-33b58e8a5d96 | -6.42979 | -41.22676 | 2025-07-09 12:29:00 | TERRA_M-T | PIMENTEIRAS | PIAUÍ | Brasil | 2208106 | 22 | 33 | nan | nan | nan | Caatinga | 27.4 |
| 93439704-2c1c-3209-b179-ac9b7035e623 | -6.16923 | -48.05428 | 2025-07-09 12:29:00 | TERRA_M-T | ANANÁS | TOCANTINS | Brasil | 1701002 | 17 | 33 | nan | nan | nan | Cerrado | 18.6 |
| e9ea07be-0cba-3554-b180-0bf0b57b9171 | -6.17049 | -48.04549 | 2025-07-09 12:29:00 | TERRA_M-T | ANANÁS | TOCANTINS | Brasil | 1701002 | 17 | 33 | nan | nan | nan | Cerrado | 16.7 |
| 87fc60de-d0ad-3346-aa2b-c269cb972f5f | -14.27784 | -47.38935 | 2025-07-09 12:29:00 | TERRA_M-T | SÃO JOÃO D'ALIANÇA | GOIÁS | Brasil | 5220009 | 52 | 33 | nan | nan | nan | Cerrado | 11.2 |
| 24b19123-1bee-33cf-8416-8b95270d3686 | -9.20799 | -47.63461 | 2025-07-09 12:29:00 | TERRA_M-T | CENTENÁRIO | TOCANTINS | Brasil | 1704105 | 17 | 33 | nan | nan | nan | Cerrado | 7.1 |
| b0a4e4fd-f6cb-3ed6-bef6-348d4b530c58 | -13.01016 | -46.29492 | 2025-07-09 12:29:00 | TERRA_M-T | CAMPOS BELOS | GOIÁS | Brasil | 5204904 | 52 | 33 | nan | nan | nan | Cerrado | 6.9 |
| eeed5ab7-2e7c-3fa0-a17c-4f35ca80a01b | -14.80658 | -43.90585 | 2025-07-09 12:29:00 | TERRA_M-T | MATIAS CARDOSO | MINAS GERAIS | Brasil | 3140852 | 31 | 33 | nan | nan | nan | Caatinga | 21.1 |
| 16119d90-4d97-3aa8-b2dd-33b2b630fe90 | -7.0331 | -43.32198 | 2025-07-09 12:29:00 | TERRA_M-T | JERUMENHA | PIAUÍ | Brasil | 2205300 | 22 | 33 | nan | nan | nan | Caatinga | 11.8 |
| 0d7a7273-cdad-3174-8487-21edb498651e | -8.37214 | -43.94647 | 2025-07-09 12:29:00 | TERRA_M-T | MANOEL EMÍDIO | PIAUÍ | Brasil | 2205904 | 22 | 33 | nan | nan | nan | Cerrado | 162.5 |
| 0d8a5f07-1e57-337a-b37b-e25b280712f0 | -5.89291 | -46.16102 | 2025-07-09 12:29:00 | TERRA_M-T | GRAJAÚ | MARANHÃO | Brasil | 2104800 | 21 | 33 | nan | nan | nan | Cerrado | 7.0 |
| 92fd07d9-5fc7-3a12-91f8-dd12791c9326 | -7.23657 | -43.07888 | 2025-07-09 12:29:00 | TERRA_M-T | FLORIANO | PIAUÍ | Brasil | 2203909 | 22 | 33 | nan | nan | nan | Caatinga | 15.4 |
| 5ae42cc7-2e47-3901-a104-997ebb7f8185 | -6.40267 | -43.67258 | 2025-07-09 12:29:00 | TERRA_M-T | SÃO JOÃO DOS PATOS | MARANHÃO | Brasil | 2111102 | 21 | 33 | nan | nan | nan | Cerrado | 38.4 |
| 4a24e150-2d42-3483-9ae3-f06d74c47e08 | -8.38317 | -43.9475 | 2025-07-09 12:29:00 | TERRA_M-T | MANOEL EMÍDIO | PIAUÍ | Brasil | 2205904 | 22 | 33 | nan | nan | nan | Cerrado | 10.9 |
| 92312d88-8d59-39c9-b2a8-57dcc724de21 | -12.10114 | -44.73059 | 2025-07-09 12:29:00 | TERRA_M-T | ANGICAL | BAHIA | Brasil | 2901403 | 29 | 33 | nan | nan | nan | Cerrado | 26.8 |
| 86d1ce9a-d80a-3f89-850c-85e8343f7877 | -10.58173 | -49.12292 | 2025-07-09 12:29:00 | TERRA_M-T | CRISTALÂNDIA | TOCANTINS | Brasil | 1706100 | 17 | 33 | nan | nan | nan | Cerrado | 33.7 |
| f600ec66-5610-3049-9ab9-6f63de6e41f7 | -6.17803 | -48.05552 | 2025-07-09 12:29:00 | TERRA_M-T | ANANÁS | TOCANTINS | Brasil | 1701002 | 17 | 33 | nan | nan | nan | Cerrado | 36.7 |
| 3a7d2ffb-7b42-3a61-88ae-d191af0d24eb | -15.60755 | -43.93971 | 2025-07-09 12:29:00 | TERRA_M-T | VARZELÂNDIA | MINAS GERAIS | Brasil | 3170909 | 31 | 33 | nan | nan | nan | Caatinga | 27.7 |
| b3cfcfb4-16dc-3732-ad78-3a08b71b7036 | -13.39185 | -47.8939 | 2025-07-09 12:29:00 | TERRA_M-T | CAVALCANTE | GOIÁS | Brasil | 5205307 | 52 | 33 | nan | nan | nan | Cerrado | 10.4 |
| 0c2cb421-2df9-302f-bde1-5dbecbec81b9 | -10.92426 | -48.27178 | 2025-07-09 12:29:00 | TERRA_M-T | PORTO NACIONAL | TOCANTINS | Brasil | 1718204 | 17 | 33 | nan | nan | nan | Cerrado | 6.3 |
| a30f1b6d-8fd9-3c57-a0d0-c7f1f8615d9e | -9.20034 | -47.62424 | 2025-07-09 12:29:00 | TERRA_M-T | CENTENÁRIO | TOCANTINS | Brasil | 1704105 | 17 | 33 | nan | nan | nan | Cerrado | 8.5 |
| 3bb682aa-cbc2-3d00-9e95-4ebcc360ad36 | -11.43106 | -45.11296 | 2025-07-09 12:29:00 | TERRA_M-T | RIACHÃO DAS NEVES | BAHIA | Brasil | 2926202 | 29 | 33 | nan | nan | nan | Cerrado | 32.2 |
| 8d2151b0-4d90-36cf-973a-68ec046eeb61 | -6.86313 | -47.84519 | 2025-07-09 12:29:00 | TERRA_M-T | DARCINÓPOLIS | TOCANTINS | Brasil | 1706506 | 17 | 33 | nan | nan | nan | Cerrado | 6.0 |
| 5b222920-f627-3b47-ab58-8de904714095 | -5.48138 | -43.33928 | 2025-07-09 12:29:00 | TERRA_M-T | MATÕES | MARANHÃO | Brasil | 2106607 | 21 | 33 | nan | nan | nan | Cerrado | 14.2 |
| 77962896-7f96-3e6a-bf30-f0e61563086a | -8.50532 | -43.28205 | 2025-07-09 12:29:00 | TERRA_M-T | CANTO DO BURITI | PIAUÍ | Brasil | 2202307 | 22 | 33 | nan | nan | nan | Caatinga | 141.8 |
| 6649cf93-df8e-3ffe-9f9e-5385f56bda02 | -15.61252 | -43.92802 | 2025-07-09 12:29:00 | TERRA_M-T | VARZELÂNDIA | MINAS GERAIS | Brasil | 3170909 | 31 | 33 | nan | nan | nan | Caatinga | 19.1 |
| cd8b8b88-3c27-36a4-a467-2248bcc2d93c | -8.5214 | -43.2828 | 2025-07-09 12:30:00 | GOES-19 | CANTO DO BURITI | PIAUÍ | Brasil | 2202307 | 22 | 33 | nan | nan | nan | Caatinga | 92.5 |
| 9201f935-9b0b-3ab6-9a37-fd944fa68581 | -8.3805 | -43.9295 | 2025-07-09 12:30:00 | GOES-19 | MANOEL EMÍDIO | PIAUÍ | Brasil | 2205904 | 22 | 33 | nan | nan | nan | Cerrado | 75.8 |
| b371a48d-a4b1-34ee-bff9-c30a0e5ddc84 | -8.3802 | -43.9527 | 2025-07-09 12:30:00 | GOES-19 | MANOEL EMÍDIO | PIAUÍ | Brasil | 2205904 | 22 | 33 | nan | nan | nan | Cerrado | 105.2 |
| 2b15bd49-bb26-3a73-9eec-4ceb533defad | -8.5025 | -43.285 | 2025-07-09 12:30:00 | GOES-19 | CANTO DO BURITI | PIAUÍ | Brasil | 2202307 | 22 | 33 | nan | nan | nan | Caatinga | 87.2 |
| 9da7b3a7-cc5e-3d0b-bc15-1158368eb3ce | -18.85004 | -45.20604 | 2025-07-09 12:32:00 | TERRA_M-T | MORADA NOVA DE MINAS | MINAS GERAIS | Brasil | 3143500 | 31 | 33 | nan | nan | nan | Cerrado | 11.5 |
| 8bc45968-ee52-32cf-9e6b-703eb5330f39 | -16.08037 | -50.59234 | 2025-07-09 12:32:00 | TERRA_M-T | NOVO BRASIL | GOIÁS | Brasil | 5215207 | 52 | 33 | nan | nan | nan | Cerrado | 4.3 |
| f969b0a8-c9c0-3bce-9273-08a4a79faaa6 | -18.41776 | -54.71099 | 2025-07-09 12:32:00 | TERRA_M-T | COXIM | MATO GROSSO DO SUL | Brasil | 5003306 | 50 | 33 | nan | nan | nan | Cerrado | 8.4 |
| 5fc083d6-b1c1-3952-a034-ffb1c7f6de51 | -15.24046 | -51.52395 | 2025-07-09 12:32:00 | TERRA_M-T | JUSSARA | GOIÁS | Brasil | 5212204 | 52 | 33 | nan | nan | nan | Cerrado | 4.7 |
| 3587109a-0fe0-31b2-8c8f-bb7712eb0f8e | -18.64309 | -55.71608 | 2025-07-09 12:32:00 | TERRA_M-T | CORUMBÁ | MATO GROSSO DO SUL | Brasil | 5003207 | 50 | 33 | nan | nan | nan | Pantanal | 8.3 |
| ac99c69f-8ff8-3126-be4c-c0cc76272b84 | -18.41992 | -54.69783 | 2025-07-09 12:32:00 | TERRA_M-T | COXIM | MATO GROSSO DO SUL | Brasil | 5003306 | 50 | 33 | nan | nan | nan | Cerrado | 9.5 |
| 3fbc6dc5-974c-32c9-96c7-606e6f4be0d2 | -22.86163 | -46.97495 | 2025-07-09 12:32:00 | TERRA_M-T | CAMPINAS | SÃO PAULO | Brasil | 3509502 | 35 | 33 | nan | nan | nan | Mata Atlântica | 7.5 |
| ea2d5168-c145-33d4-ac92-2d3c43260430 | -22.85999 | -46.98973 | 2025-07-09 12:32:00 | TERRA_M-T | CAMPINAS | SÃO PAULO | Brasil | 3509502 | 35 | 33 | nan | nan | nan | Mata Atlântica | 13.3 |
| e85b9132-b3bc-33ec-a41d-a1f27303999f | -17.69485 | -46.74468 | 2025-07-09 12:32:00 | TERRA_M-T | VAZANTE | MINAS GERAIS | Brasil | 3171006 | 31 | 33 | nan | nan | nan | Cerrado | 10.8 |
| 311077f5-43f5-3fe5-86b9-1d893f2a212d | -22.8576 | -46.98352 | 2025-07-09 12:32:00 | TERRA_M-T | CAMPINAS | SÃO PAULO | Brasil | 3509502 | 35 | 33 | nan | nan | nan | Mata Atlântica | 21.4 |
| 59e360fa-2c95-33d9-a2dc-148e2223b643 | -20.30552 | -42.05006 | 2025-07-09 12:32:00 | TERRA_M-T | MANHUAÇU | MINAS GERAIS | Brasil | 3139409 | 31 | 33 | nan | nan | nan | Mata Atlântica | 22.9 |
| 710fdd49-ab51-3b34-aa1f-c8a644e76d1c | -18.50486 | -53.53569 | 2025-07-09 12:32:00 | TERRA_M-T | FIGUEIRÃO | MATO GROSSO DO SUL | Brasil | 5003900 | 50 | 33 | nan | nan | nan | Cerrado | 9.4 |
| c2ff7d91-2b42-36ec-a5b5-da1020cb8759 | -18.50311 | -53.54673 | 2025-07-09 12:32:00 | TERRA_M-T | FIGUEIRÃO | MATO GROSSO DO SUL | Brasil | 5003900 | 50 | 33 | nan | nan | nan | Cerrado | 21.3 |
| a7f93f9d-0f31-352b-a07a-c737fd18bbd3 | -15.24955 | -51.52537 | 2025-07-09 12:32:00 | TERRA_M-T | JUSSARA | GOIÁS | Brasil | 5212204 | 52 | 33 | nan | nan | nan | Cerrado | 29.7 |
| 088235b5-d118-3f59-8039-a2f2861b30da | -18.64265 | -55.72199 | 2025-07-09 12:32:00 | TERRA_M-T | CORUMBÁ | MATO GROSSO DO SUL | Brasil | 5003207 | 50 | 33 | nan | nan | nan | Pantanal | 13.4 |
| 2350c874-a673-362a-8a9d-5aa6b2e73372 | -18.42063 | -54.56387 | 2025-07-09 12:32:00 | TERRA_M-T | COXIM | MATO GROSSO DO SUL | Brasil | 5003306 | 50 | 33 | nan | nan | nan | Cerrado | 18.6 |
| 6e3f82b4-fac1-3ca1-accb-7dc34d09f569 | -18.42277 | -54.55086 | 2025-07-09 12:32:00 | TERRA_M-T | COXIM | MATO GROSSO DO SUL | Brasil | 5003306 | 50 | 33 | nan | nan | nan | Cerrado | 26.8 |
| 46aa72b2-b259-3188-8aea-1ff4edb85301 | -15.2481 | -51.53505 | 2025-07-09 12:32:00 | TERRA_M-T | JUSSARA | GOIÁS | Brasil | 5212204 | 52 | 33 | nan | nan | nan | Cerrado | 8.6 |
| 8492568f-1b1d-3c45-8987-31dba985350b | -15.95789 | -47.41514 | 2025-07-09 12:32:00 | TERRA_M-T | BRASÍLIA | DISTRITO FEDERAL | Brasil | 5300108 | 53 | 33 | nan | nan | nan | Cerrado | 9.7 |
| a0bcbe66-f0d8-35d0-9257-1318c3d72787 | -15.45914 | -48.53373 | 2025-07-09 12:32:00 | TERRA_M-T | PADRE BERNARDO | GOIÁS | Brasil | 5215603 | 52 | 33 | nan | nan | nan | Cerrado | 5.9 |
| 24f2e11c-0b54-349f-84f4-41694781fa94 | -17.27857 | -46.31544 | 2025-07-09 12:32:00 | TERRA_M-T | JOÃO PINHEIRO | MINAS GERAIS | Brasil | 3136306 | 31 | 33 | nan | nan | nan | Cerrado | 13.1 |
| 339fdab3-83af-3911-bded-30801d137df6 | -18.40744 | -49.1917 | 2025-07-09 12:32:00 | TERRA_M-T | ITUMBIARA | GOIÁS | Brasil | 5211503 | 52 | 33 | nan | nan | nan | Mata Atlântica | 3.8 |
| 04569152-160f-3a6b-ae05-e150ad538548 | -22.73147 | -53.94236 | 2025-07-09 12:34:00 | TERRA_M-T | JATEÍ | MATO GROSSO DO SUL | Brasil | 5005103 | 50 | 33 | nan | nan | nan | Mata Atlântica | 5.0 |
| cca163d8-eb90-3bf5-b751-43f23fb9a718 | -22.9311 | -52.5726 | 2025-07-09 12:34:00 | TERRA_M-T | PARANAVAÍ | PARANÁ | Brasil | 4118402 | 41 | 33 | nan | nan | nan | Mata Atlântica | 4.0 |
| 6aebb124-23d2-371c-97c2-c0412c198ade | -8.5025 | -43.285 | 2025-07-09 12:40:00 | GOES-19 | CANTO DO BURITI | PIAUÍ | Brasil | 2202307 | 22 | 33 | nan | nan | nan | Caatinga | 83.5 |
| ac5db5ba-9fc0-3c02-8160-fc3771d55c93 | -8.5214 | -43.2828 | 2025-07-09 12:40:00 | GOES-19 | CANTO DO BURITI | PIAUÍ | Brasil | 2202307 | 22 | 33 | nan | nan | nan | Caatinga | 86.2 |
| 5487d374-4b3d-3ee9-9745-147826410a24 | -8.3802 | -43.9527 | 2025-07-09 12:40:00 | GOES-19 | MANOEL EMÍDIO | PIAUÍ | Brasil | 2205904 | 22 | 33 | nan | nan | nan | Cerrado | 109.6 |
| c3c3bec8-499e-3fe2-a187-f4363431b283 | -7.0943 | -44.3819 | 2025-07-09 12:40:00 | GOES-19 | BENEDITO LEITE | MARANHÃO | Brasil | 2101806 | 21 | 33 | nan | nan | nan | Cerrado | 82.3 |
| 11f453a9-48b6-38f7-b2dc-af69123f0cc1 | -10.5776 | -49.1316 | 2025-07-09 12:50:00 | GOES-19 | CRISTALÂNDIA | TOCANTINS | Brasil | 1706100 | 17 | 33 | nan | nan | nan | Cerrado | 72.7 |
| 4059d490-b589-38a6-ba05-6b8d9a9b5ccb | -8.5025 | -43.285 | 2025-07-09 12:50:00 | GOES-19 | CANTO DO BURITI | PIAUÍ | Brasil | 2202307 | 22 | 33 | nan | nan | nan | Caatinga | 96.5 |
| 16ba6a19-3e5b-32d3-ad83-6a1ab297ff40 | -8.3802 | -43.9527 | 2025-07-09 12:50:00 | GOES-19 | MANOEL EMÍDIO | PIAUÍ | Brasil | 2205904 | 22 | 33 | nan | nan | nan | Cerrado | 84.5 |
| cd259a8f-6d75-3a8b-a2ed-5f281ff267d6 | -7.0943 | -44.3819 | 2025-07-09 12:50:00 | GOES-19 | BENEDITO LEITE | MARANHÃO | Brasil | 2101806 | 21 | 33 | nan | nan | nan | Cerrado | 72.5 |
| e5d7b84c-d7ae-3ba5-b566-23ce306026f3 | -7.0943 | -44.3819 | 2025-07-09 13:00:00 | GOES-19 | BENEDITO LEITE | MARANHÃO | Brasil | 2101806 | 21 | 33 | nan | nan | nan | Cerrado | 78.1 |
| ca76db3c-3ebb-3861-a95b-a3f5c7210973 | -8.3802 | -43.9527 | 2025-07-09 13:00:00 | GOES-19 | MANOEL EMÍDIO | PIAUÍ | Brasil | 2205904 | 22 | 33 | nan | nan | nan | Cerrado | 84.4 |
| ebc87eea-ff82-3a72-a6b0-4759d84ba795 | -8.5025 | -43.285 | 2025-07-09 13:00:00 | GOES-19 | CANTO DO BURITI | PIAUÍ | Brasil | 2202307 | 22 | 33 | nan | nan | nan | Caatinga | 92.8 |
| 6b0fd37e-a225-309d-8bd4-bcd25b2c4741 | -7.0943 | -44.3819 | 2025-07-09 13:10:00 | GOES-19 | BENEDITO LEITE | MARANHÃO | Brasil | 2101806 | 21 | 33 | nan | nan | nan | Cerrado | 73.9 |
| e95fca3b-3994-3ac7-a126-cf2b7ff1fed4 | -8.3802 | -43.9527 | 2025-07-09 13:10:00 | GOES-19 | MANOEL EMÍDIO | PIAUÍ | Brasil | 2205904 | 22 | 33 | nan | nan | nan | Cerrado | 73.3 |
| 3344f938-1333-3857-906b-8c2339d6d5c6 | -6.1792 | -48.0494 | 2025-07-09 13:10:00 | GOES-19 | ANANÁS | TOCANTINS | Brasil | 1701002 | 17 | 33 | nan | nan | nan | Cerrado | 68.9 |
| 471cd325-1dc8-3deb-b293-ba01dfad37d9 | -7.6774 | -44.3727 | 2025-07-09 13:10:00 | GOES-19 | URUÇUÍ | PIAUÍ | Brasil | 2211209 | 22 | 33 | nan | nan | nan | Cerrado | 75.6 |
| b360f5f6-c605-3f97-b235-40084b7c0483 | -8.3802 | -43.9527 | 2025-07-09 13:20:00 | GOES-19 | MANOEL EMÍDIO | PIAUÍ | Brasil | 2205904 | 22 | 33 | nan | nan | nan | Cerrado | 86.2 |
| d1bbe80c-ff0a-39fe-b6e4-edf826ab4bf6 | -10.5776 | -49.1316 | 2025-07-09 13:20:00 | GOES-19 | CRISTALÂNDIA | TOCANTINS | Brasil | 1706100 | 17 | 33 | nan | nan | nan | Cerrado | 63.7 |
| d70ce215-6394-38ea-a330-0fde9591f557 | -7.0943 | -44.3819 | 2025-07-09 13:20:00 | GOES-19 | BENEDITO LEITE | MARANHÃO | Brasil | 2101806 | 21 | 33 | nan | nan | nan | Cerrado | 69.8 |
| 48c6f1be-ab60-3e78-bbf0-8bcea5d0a689 | -8.3805 | -43.9295 | 2025-07-09 13:20:00 | GOES-19 | MANOEL EMÍDIO | PIAUÍ | Brasil | 2205904 | 22 | 33 | nan | nan | nan | Cerrado | 68.1 |
| b1777c9b-e8b2-3702-931a-7095a2282f2b | -7.0858 | -43.456 | 2025-07-09 13:20:00 | GOES-19 | JERUMENHA | PIAUÍ | Brasil | 2205300 | 22 | 33 | nan | nan | nan | Caatinga | 72.7 |


[Clique aqui para ver as próximas entradas](README28.md)
