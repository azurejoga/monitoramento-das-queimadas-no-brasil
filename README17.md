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

## Dados Diários - Página 17

| ID | Latitude | Longitude | Data/Hora GMT | Satélite | Município | Estado | País | Município ID | Estado ID | País ID | Dias sem Chuva | Precipitação | Risco de Fogo | Bioma | FRP |
|----|----------|-----------|---------------|----------|-----------|--------|------|--------------|-----------|---------|----------------|--------------|----------------|-------|-----|
| e1f7f726-8645-3146-b8d7-67ccfdabda0b | -2.84254 | -42.42435 | 2024-12-27 12:10:00 | TERRA_M-T | TUTÓIA | MARANHÃO | Brasil | 2112506 | 21 | 33 | nan | nan | nan | Cerrado | 91.4 |
| 835a966c-6fff-351c-8cd7-51dc2b61a8cb | -4.79704 | -40.54814 | 2024-12-27 12:10:00 | TERRA_M-T | NOVA RUSSAS | CEARÁ | Brasil | 2309300 | 23 | 33 | nan | nan | nan | Caatinga | 7.4 |
| 0fa21e2d-8793-380f-a523-fbdfbdf465a9 | -5.55611 | -41.10127 | 2024-12-27 12:10:00 | TERRA_M-T | SÃO MIGUEL DO TAPUIO | PIAUÍ | Brasil | 2210409 | 22 | 33 | nan | nan | nan | Caatinga | 11.5 |
| 196e3e50-8f7e-35a9-bbe1-cc6ed342de08 | -3.76245 | -40.37006 | 2024-12-27 12:10:00 | TERRA_M-T | SOBRAL | CEARÁ | Brasil | 2312908 | 23 | 33 | nan | nan | nan | Caatinga | 16.8 |
| 2a19e82a-c418-3be1-b55b-b5545590c1b1 | -6.0491 | -38.64696 | 2024-12-27 12:10:00 | TERRA_M-T | JAGUARIBE | CEARÁ | Brasil | 2306900 | 23 | 33 | nan | nan | nan | Caatinga | 20.3 |
| c24b4b68-db14-3369-b089-173604603611 | -3.37319 | -40.63235 | 2024-12-27 12:10:00 | TERRA_M-T | MORAÚJO | CEARÁ | Brasil | 2308807 | 23 | 33 | nan | nan | nan | Caatinga | 31.3 |
| d02a2857-299f-3a41-a642-017e97e9768b | -3.76377 | -40.36107 | 2024-12-27 12:10:00 | TERRA_M-T | SOBRAL | CEARÁ | Brasil | 2312908 | 23 | 33 | nan | nan | nan | Caatinga | 22.6 |
| 7d7685e8-5484-3a73-97d4-a677d7140863 | -3.37453 | -40.62319 | 2024-12-27 12:10:00 | TERRA_M-T | MORAÚJO | CEARÁ | Brasil | 2308807 | 23 | 33 | nan | nan | nan | Caatinga | 11.1 |
| 236220b4-bd97-367a-ad82-daac05141a6b | -5.22924 | -43.186 | 2024-12-27 12:10:00 | TERRA_M-T | MATÕES | MARANHÃO | Brasil | 2106607 | 21 | 33 | nan | nan | nan | Cerrado | 12.9 |
| a68ce6e2-11bd-36da-b205-39727ab791ba | -8.21913 | -39.5332 | 2024-12-27 12:12:00 | TERRA_M-T | PARNAMIRIM | PERNAMBUCO | Brasil | 2610400 | 26 | 33 | nan | nan | nan | Caatinga | 6.0 |
| 8a4fd4bc-4b77-3d6e-8990-754fe0ee2c8e | -11.99675 | -38.06739 | 2024-12-27 12:12:00 | TERRA_M-T | ENTRE RIOS | BAHIA | Brasil | 2910503 | 29 | 33 | nan | nan | nan | Mata Atlântica | 9.1 |
| 7b827d3b-ba72-3f86-a9a4-5cdc0a144857 | -8.28109 | -35.31672 | 2024-12-27 12:12:00 | TERRA_M-T | VITÓRIA DE SANTO ANTÃO | PERNAMBUCO | Brasil | 2616407 | 26 | 33 | nan | nan | nan | Mata Atlântica | 34.0 |
| 7bdb7f31-baaf-3c35-9890-67abbc62d586 | -11.99841 | -38.06186 | 2024-12-27 12:12:00 | TERRA_M-T | ENTRE RIOS | BAHIA | Brasil | 2910503 | 29 | 33 | nan | nan | nan | Mata Atlântica | 12.5 |
| b5e4e62c-70b8-3d7b-8e0d-8eff2343deed | -8.66176 | -39.46221 | 2024-12-27 12:12:00 | TERRA_M-T | CURAÇÁ | BAHIA | Brasil | 2909901 | 29 | 33 | nan | nan | nan | Caatinga | 9.8 |
| cdc744bd-ebc2-3f5a-9f43-f6305d65a9b6 | -8.88575 | -46.21536 | 2024-12-27 12:12:00 | TERRA_M-T | ALTO PARNAÍBA | MARANHÃO | Brasil | 2100501 | 21 | 33 | nan | nan | nan | Cerrado | 18.5 |
| deb4c3e5-4702-3861-94ec-3e890f668e2c | -7.31357 | -37.35493 | 2024-12-27 12:12:00 | TERRA_M-T | MATURÉIA | PARAÍBA | Brasil | 2509396 | 25 | 33 | nan | nan | nan | Caatinga | 16.6 |
| 79d698af-8c53-375b-82bc-6df72e045cce | -11.78944 | -42.87656 | 2024-12-27 12:12:00 | TERRA_M-T | MORPARÁ | BAHIA | Brasil | 2921609 | 29 | 33 | nan | nan | nan | Caatinga | 8.4 |
| 9f9c7eed-01fe-394a-801e-a592772bf64b | -6.33076 | -41.23119 | 2024-12-27 12:12:00 | TERRA_M-T | PIMENTEIRAS | PIAUÍ | Brasil | 2208106 | 22 | 33 | nan | nan | nan | Caatinga | 7.9 |
| f33f03df-e472-334d-81e7-7ef21a6d78f6 | -6.51363 | -39.71323 | 2024-12-27 12:12:00 | TERRA_M-T | JUCÁS | CEARÁ | Brasil | 2307403 | 23 | 33 | nan | nan | nan | Caatinga | 14.7 |
| a238515e-5794-32c5-bd45-a6bccd691007 | -7.5812 | -38.36829 | 2024-12-27 12:12:00 | TERRA_M-T | SANTANA DE MANGUEIRA | PARAÍBA | Brasil | 2513505 | 25 | 33 | nan | nan | nan | Caatinga | 6.0 |
| 58bac71b-9e14-315d-9a7c-16bb7588130a | -13.548 | -41.72368 | 2024-12-27 12:12:00 | TERRA_M-T | RIO DE CONTAS | BAHIA | Brasil | 2926707 | 29 | 33 | nan | nan | nan | Caatinga | 14.6 |
| 04c4488d-b97c-30aa-a9b8-185fa2a6ace6 | -6.5999 | -39.05025 | 2024-12-27 12:12:00 | TERRA_M-T | CEDRO | CEARÁ | Brasil | 2303808 | 23 | 33 | nan | nan | nan | Caatinga | 70.1 |
| a4b9a913-f935-3b4f-bb61-b120334a0915 | -6.96954 | -38.58921 | 2024-12-27 12:12:00 | TERRA_M-T | CAJAZEIRAS | PARAÍBA | Brasil | 2503704 | 25 | 33 | nan | nan | nan | Caatinga | 7.5 |
| cfd54c24-2fd2-3f25-920d-968c7b9e60d2 | -6.07655 | -44.14795 | 2024-12-27 12:12:00 | TERRA_M-T | COLINAS | MARANHÃO | Brasil | 2103505 | 21 | 33 | nan | nan | nan | Cerrado | 48.1 |
| da959b7f-e4bc-3a11-a0ef-13bf0ceca548 | -7.14092 | -37.77036 | 2024-12-27 12:12:00 | TERRA_M-T | EMAS | PARAÍBA | Brasil | 2505907 | 25 | 33 | nan | nan | nan | Caatinga | 10.8 |
| 9bdb7d0c-070b-3ab4-a877-2b4cc26030ca | -7.05381 | -39.49092 | 2024-12-27 12:12:00 | TERRA_M-T | CRATO | CEARÁ | Brasil | 2304202 | 23 | 33 | nan | nan | nan | Caatinga | 6.1 |
| da136f7f-7341-32c3-b72a-52265242ad71 | -9.1883 | -38.80013 | 2024-12-27 12:12:00 | TERRA_M-T | MACURURÉ | BAHIA | Brasil | 2919900 | 29 | 33 | nan | nan | nan | Caatinga | 10.5 |
| 70b55c14-450e-3fed-9805-eee0cf89478a | -10.72698 | -42.33258 | 2024-12-27 12:12:00 | TERRA_M-T | ITAGUAÇU DA BAHIA | BAHIA | Brasil | 2915353 | 29 | 33 | nan | nan | nan | Caatinga | 31.0 |
| 99fcc432-5577-38eb-a449-fb15b1c53961 | -10.14928 | -42.43166 | 2024-12-27 12:12:00 | TERRA_M-T | PILÃO ARCADO | BAHIA | Brasil | 2924405 | 29 | 33 | nan | nan | nan | Caatinga | 6.4 |
| f3bcea60-6865-39ac-8956-bba29ffe320a | -7.31022 | -37.35962 | 2024-12-27 12:12:00 | TERRA_M-T | MATURÉIA | PARAÍBA | Brasil | 2509396 | 25 | 33 | nan | nan | nan | Caatinga | 9.9 |
| 7ee9fa6c-301a-3075-aa71-8447f93aadb6 | -8.81957 | -37.39474 | 2024-12-27 12:12:00 | TERRA_M-T | ITAÍBA | PERNAMBUCO | Brasil | 2607505 | 26 | 33 | nan | nan | nan | Caatinga | 19.0 |
| 0f8ab8f9-569a-3525-b65f-efb34bc15bec | -6.6012 | -39.04118 | 2024-12-27 12:12:00 | TERRA_M-T | CEDRO | CEARÁ | Brasil | 2303808 | 23 | 33 | nan | nan | nan | Caatinga | 81.1 |
| c2095ded-2bfa-3a45-86d6-b5fc4d8a643a | -6.64331 | -41.99609 | 2024-12-27 12:12:00 | TERRA_M-T | OEIRAS | PIAUÍ | Brasil | 2207009 | 22 | 33 | nan | nan | nan | Caatinga | 15.7 |
| 0265b0e3-5cc0-31ef-ad1b-e20398ea0841 | -13.32474 | -40.8993 | 2024-12-27 12:12:00 | TERRA_M-T | IRAMAIA | BAHIA | Brasil | 2914307 | 29 | 33 | nan | nan | nan | Caatinga | 9.2 |
| 4337bacb-8d68-33e8-a6d7-9f34953b82b0 | -10.72558 | -42.34199 | 2024-12-27 12:12:00 | TERRA_M-T | ITAGUAÇU DA BAHIA | BAHIA | Brasil | 2915353 | 29 | 33 | nan | nan | nan | Caatinga | 38.5 |
| 00ddeca5-7253-3caa-b8f9-642c990b60fa | -7.49946 | -38.36095 | 2024-12-27 12:12:00 | TERRA_M-T | IBIARA | PARAÍBA | Brasil | 2506608 | 25 | 33 | nan | nan | nan | Caatinga | 8.8 |
| 4b60a0d2-086a-355d-b050-72eb85acfda3 | -11.19566 | -40.3148 | 2024-12-27 12:12:00 | TERRA_M-T | CAÉM | BAHIA | Brasil | 2905107 | 29 | 33 | nan | nan | nan | Caatinga | 81.1 |
| 4b17bab1-8248-30f4-91e2-39a985b04fba | -7.15488 | -41.46299 | 2024-12-27 12:12:00 | TERRA_M-T | GEMINIANO | PIAUÍ | Brasil | 2204352 | 22 | 33 | nan | nan | nan | Caatinga | 19.8 |
| 4f0c7e43-11f4-3acc-8993-2ec75c7c57fb | -13.27102 | -40.10341 | 2024-12-27 12:12:00 | TERRA_M-T | IRAJUBA | BAHIA | Brasil | 2914208 | 29 | 33 | nan | nan | nan | Mata Atlântica | 12.7 |
| 33c16d90-7899-3e3d-96c7-074c863562fe | -8.16893 | -43.94046 | 2024-12-27 12:12:00 | TERRA_M-T | MANOEL EMÍDIO | PIAUÍ | Brasil | 2205904 | 22 | 33 | nan | nan | nan | Cerrado | 7.6 |
| 6baf1d54-3d6e-3dea-91bc-e39c95f54afb | -7.23312 | -39.13576 | 2024-12-27 12:12:00 | TERRA_M-T | MISSÃO VELHA | CEARÁ | Brasil | 2308401 | 23 | 33 | nan | nan | nan | Caatinga | 7.3 |
| 94dca315-b512-3058-a957-9ced78545438 | -7.58739 | -42.28376 | 2024-12-27 12:12:00 | TERRA_M-T | SÃO MIGUEL DO FIDALGO | PIAUÍ | Brasil | 2210391 | 22 | 33 | nan | nan | nan | Caatinga | 9.8 |
| 9c46f590-890d-3c22-9832-b93315fdd4f0 | -9.18695 | -38.80981 | 2024-12-27 12:12:00 | TERRA_M-T | MACURURÉ | BAHIA | Brasil | 2919900 | 29 | 33 | nan | nan | nan | Caatinga | 7.5 |
| 51f326fe-092a-3cf1-9e21-afa41d1761d2 | -10.4883 | -40.29383 | 2024-12-27 12:12:00 | TERRA_M-T | CAMPO FORMOSO | BAHIA | Brasil | 2906006 | 29 | 33 | nan | nan | nan | Caatinga | 19.4 |
| 02a2bc78-4413-3fc8-b449-ae0af87ed404 | -7.70783 | -37.59677 | 2024-12-27 12:12:00 | TERRA_M-T | AFOGADOS DA INGAZEIRA | PERNAMBUCO | Brasil | 2600104 | 26 | 33 | nan | nan | nan | Caatinga | 8.3 |
| 8eb8cf02-0b3b-3ce7-93f4-fba04d995c8f | -7.69805 | -35.64906 | 2024-12-27 12:12:00 | TERRA_M-T | OROBÓ | PERNAMBUCO | Brasil | 2609709 | 26 | 33 | nan | nan | nan | Caatinga | 10.7 |
| 7efbc90f-563d-3b91-864f-4b5867d12d86 | -11.18676 | -40.31355 | 2024-12-27 12:12:00 | TERRA_M-T | CAÉM | BAHIA | Brasil | 2905107 | 29 | 33 | nan | nan | nan | Caatinga | 17.2 |
| 53e61dfb-f4f8-30e5-865c-8cd65d6c2304 | -6.66577 | -38.25959 | 2024-12-27 12:12:00 | TERRA_M-T | SOUSA | PARAÍBA | Brasil | 2516201 | 25 | 33 | nan | nan | nan | Caatinga | 16.7 |
| ea3f2b1d-9056-3e1d-b451-4f9ccb5551b6 | -7.58974 | -37.11982 | 2024-12-27 12:12:00 | TERRA_M-T | OURO VELHO | PARAÍBA | Brasil | 2510600 | 25 | 33 | nan | nan | nan | Caatinga | 20.7 |
| 66d6825d-fe79-3d38-ba51-15c6a0f67382 | -9.13906 | -41.02128 | 2024-12-27 12:12:00 | TERRA_M-T | CASA NOVA | BAHIA | Brasil | 2907202 | 29 | 33 | nan | nan | nan | Caatinga | 14.8 |
| e6d8f417-4dfc-3e3b-82fb-8725346f3fd7 | -5.94242 | -43.28093 | 2024-12-27 12:12:00 | TERRA_M-T | SÃO FRANCISCO DO MARANHÃO | MARANHÃO | Brasil | 2110906 | 21 | 33 | nan | nan | nan | Caatinga | 14.1 |
| 3aa8794a-eeb6-3792-b74a-170e95eaa5c5 | -7.92313 | -40.17413 | 2024-12-27 12:12:00 | TERRA_M-T | OURICURI | PERNAMBUCO | Brasil | 2609907 | 26 | 33 | nan | nan | nan | Caatinga | 6.7 |
| d122c31a-9601-3e97-82bd-6f473e98eaea | -13.54669 | -41.73271 | 2024-12-27 12:12:00 | TERRA_M-T | RIO DE CONTAS | BAHIA | Brasil | 2926707 | 29 | 33 | nan | nan | nan | Caatinga | 9.7 |
| 5f6775f9-d9b7-356c-afbc-0f2d32e6513d | -8.04703 | -39.18342 | 2024-12-27 12:12:00 | TERRA_M-T | SALGUEIRO | PERNAMBUCO | Brasil | 2612208 | 26 | 33 | nan | nan | nan | Caatinga | 9.3 |
| 5382e611-093b-3ce2-9bee-da4aea5363e7 | -14.1456 | -40.83058 | 2024-12-27 12:12:00 | TERRA_M-T | MIRANTE | BAHIA | Brasil | 2921450 | 29 | 33 | nan | nan | nan | Caatinga | 11.3 |
| 460162d1-3e27-3bad-bd98-10859cb65552 | -7.13947 | -37.78066 | 2024-12-27 12:12:00 | TERRA_M-T | EMAS | PARAÍBA | Brasil | 2505907 | 25 | 33 | nan | nan | nan | Caatinga | 15.3 |
| 391bf49e-9d88-3fa9-9a4a-fa584c9f761a | -10.48957 | -40.28494 | 2024-12-27 12:12:00 | TERRA_M-T | CAMPO FORMOSO | BAHIA | Brasil | 2906006 | 29 | 33 | nan | nan | nan | Caatinga | 12.0 |
| a1559d7f-e628-364a-8fe1-555a163d5cde | -11.28685 | -41.85824 | 2024-12-27 12:12:00 | TERRA_M-T | IRECÊ | BAHIA | Brasil | 2914604 | 29 | 33 | nan | nan | nan | Caatinga | 8.2 |
| ee97e143-c51a-3fd4-b390-7960d794676f | -8.80221 | -41.2463 | 2024-12-27 12:12:00 | TERRA_M-T | CASA NOVA | BAHIA | Brasil | 2907202 | 29 | 33 | nan | nan | nan | Caatinga | 6.0 |
| 0a480975-d0f1-3efc-b161-7ed5eecc4fad | -7.15624 | -41.45372 | 2024-12-27 12:12:00 | TERRA_M-T | GEMINIANO | PIAUÍ | Brasil | 2204352 | 22 | 33 | nan | nan | nan | Caatinga | 16.4 |
| d4d380da-9222-39ea-84fd-fa7812d84025 | -9.88069 | -37.47898 | 2024-12-27 12:12:00 | TERRA_M-T | PORTO DA FOLHA | SERGIPE | Brasil | 2805604 | 28 | 33 | nan | nan | nan | Caatinga | 11.8 |
| ff3b73e3-d5ea-333c-a05c-76c4fa960c18 | -13.2697 | -40.11285 | 2024-12-27 12:12:00 | TERRA_M-T | IRAJUBA | BAHIA | Brasil | 2914208 | 29 | 33 | nan | nan | nan | Mata Atlântica | 13.2 |
| 005d8f4e-7fcf-3a68-b0ae-efc12cd7b3e7 | -10.14786 | -42.44123 | 2024-12-27 12:12:00 | TERRA_M-T | PILÃO ARCADO | BAHIA | Brasil | 2924405 | 29 | 33 | nan | nan | nan | Caatinga | 34.0 |
| c6555ace-21c6-3a4a-9e90-8b43003eac41 | -11.2295 | -37.61868 | 2024-12-27 12:12:00 | TERRA_M-T | ARAUÁ | SERGIPE | Brasil | 2800407 | 28 | 33 | nan | nan | nan | Mata Atlântica | 13.7 |
| d5e0519b-4388-3a97-a8b6-93a2448f4c8e | -8.48806 | -36.89502 | 2024-12-27 12:12:00 | TERRA_M-T | PEDRA | PERNAMBUCO | Brasil | 2610806 | 26 | 33 | nan | nan | nan | Caatinga | 16.1 |
| 94324107-1b4a-37d8-a3bb-47661ea91bec | -6.51235 | -39.72207 | 2024-12-27 12:12:00 | TERRA_M-T | JUCÁS | CEARÁ | Brasil | 2307403 | 23 | 33 | nan | nan | nan | Caatinga | 8.6 |
| d749ee7c-dde0-337a-a488-32966b54cf48 | -15.18841 | -39.94547 | 2024-12-27 12:14:00 | TERRA_M-T | ITAPETINGA | BAHIA | Brasil | 2916401 | 29 | 33 | nan | nan | nan | Mata Atlântica | 24.1 |
| d5e7c1fb-d58f-30ed-9f99-2cfabcea48e3 | -15.92612 | -39.8589 | 2024-12-27 12:14:00 | TERRA_M-T | ITAPEBI | BAHIA | Brasil | 2916302 | 29 | 33 | nan | nan | nan | Mata Atlântica | 15.8 |
| 5676bfca-64da-3089-a47a-7771e9c311b1 | -16.03381 | -42.12515 | 2024-12-27 12:14:00 | TERRA_M-T | SALINAS | MINAS GERAIS | Brasil | 3157005 | 31 | 33 | nan | nan | nan | Mata Atlântica | 4.4 |
| d43aafdf-5796-3d50-a1e4-bf561705dfa3 | -15.18704 | -39.95556 | 2024-12-27 12:14:00 | TERRA_M-T | ITAPETINGA | BAHIA | Brasil | 2916401 | 29 | 33 | nan | nan | nan | Mata Atlântica | 8.8 |
| 7646bbd1-990a-336a-b1dd-5b1ee071e464 | -14.96836 | -39.53061 | 2024-12-27 12:14:00 | TERRA_M-T | ITAPÉ | BAHIA | Brasil | 2916203 | 29 | 33 | nan | nan | nan | Mata Atlântica | 14.2 |
| 61ad0258-b14c-3f3d-9a98-a556eebb6433 | -15.92475 | -39.86922 | 2024-12-27 12:14:00 | TERRA_M-T | ITAPEBI | BAHIA | Brasil | 2916302 | 29 | 33 | nan | nan | nan | Mata Atlântica | 21.4 |
| 1d163af3-c98f-3b7d-86a7-34f2fe7c6b0a | -3.42 | -44.9 | 2024-12-27 13:00:00 | MSG-03 | VITÓRIA DO MEARIM | MARANHÃO | Brasil | 2112902 | 21 | 33 | nan | nan | nan | Amazônia | nan |
| c87f3e43-8143-3d6e-b8ca-81d0872907e6 | -5.91 | -43.47 | 2024-12-27 13:00:00 | MSG-03 | PARNARAMA | MARANHÃO | Brasil | 2107803 | 21 | 33 | nan | nan | nan | Cerrado | nan |
| 91148702-9a40-3a17-b03f-c181326f0c81 | -5.91 | -43.47 | 2024-12-27 14:00:00 | MSG-03 | PARNARAMA | MARANHÃO | Brasil | 2107803 | 21 | 33 | nan | nan | nan | Cerrado | nan |


