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

## Dados Diários - Página 115

| ID | Latitude | Longitude | Data/Hora GMT | Satélite | Município | Estado | País | Município ID | Estado ID | País ID | Dias sem Chuva | Precipitação | Risco de Fogo | Bioma | FRP |
|----|----------|-----------|---------------|----------|-----------|--------|------|--------------|-----------|---------|----------------|--------------|----------------|-------|-----|
| 7b4c6b46-6939-3aec-97ec-81d98806687f | -9.59802 | -42.92746 | 2024-10-24 12:12:00 | TERRA_M-T | CAMPO ALEGRE DE LOURDES | BAHIA | Brasil | 2905909 | 29 | 33 | nan | nan | nan | Caatinga | 18.5 |
| a637b2eb-42d3-3785-b33d-2ae04309268e | -9.59623 | -42.93924 | 2024-10-24 12:12:00 | TERRA_M-T | CAMPO ALEGRE DE LOURDES | BAHIA | Brasil | 2905909 | 29 | 33 | nan | nan | nan | Caatinga | 20.5 |
| c616ecb2-cabb-39d0-b09a-e428d4a1a03d | -12.18132 | -43.45478 | 2024-10-24 12:12:00 | TERRA_M-T | MUQUÉM DO SÃO FRANCISCO | BAHIA | Brasil | 2922250 | 29 | 33 | nan | nan | nan | Cerrado | 12.1 |
| d13f657a-bb72-3ec4-8f21-2ea91a3c8e83 | -10.87925 | -44.28236 | 2024-10-24 12:12:00 | TERRA_M-T | SANTA RITA DE CÁSSIA | BAHIA | Brasil | 2928406 | 29 | 33 | nan | nan | nan | Cerrado | 16.0 |
| b9512183-f272-3cc9-bd62-dbe88104fff6 | -10.87437 | -44.28868 | 2024-10-24 12:12:00 | TERRA_M-T | SANTA RITA DE CÁSSIA | BAHIA | Brasil | 2928406 | 29 | 33 | nan | nan | nan | Cerrado | 26.3 |
| e4e78687-066d-38ad-a1c6-c423fb6ee429 | -5.72814 | -43.84306 | 2024-10-24 12:12:00 | TERRA_M-T | BURITI BRAVO | MARANHÃO | Brasil | 2102309 | 21 | 33 | nan | nan | nan | Cerrado | 25.7 |
| 79e172dc-994d-3f5e-a847-2c7e6b4309cc | -5.71913 | -43.82612 | 2024-10-24 12:12:00 | TERRA_M-T | BURITI BRAVO | MARANHÃO | Brasil | 2102309 | 21 | 33 | nan | nan | nan | Cerrado | 24.3 |
| af902139-cffd-3cd0-a89e-74d48eb45023 | -5.71677 | -43.8413 | 2024-10-24 12:12:00 | TERRA_M-T | BURITI BRAVO | MARANHÃO | Brasil | 2102309 | 21 | 33 | nan | nan | nan | Cerrado | 50.3 |
| 2d9a2679-4ea0-3963-8787-e623ea147383 | -5.58042 | -44.87515 | 2024-10-24 12:12:00 | TERRA_M-T | TUNTUM | MARANHÃO | Brasil | 2112308 | 21 | 33 | nan | nan | nan | Cerrado | 31.6 |
| 13cd5e46-f2fa-373e-bdbe-e4b9408eddd3 | -6.94452 | -45.21581 | 2024-10-24 12:12:00 | TERRA_M-T | LORETO | MARANHÃO | Brasil | 2106102 | 21 | 33 | nan | nan | nan | Cerrado | 60.6 |
| 594bf6d8-d99a-3088-b116-9510b6d3930b | -9.23912 | -45.24708 | 2024-10-24 12:12:00 | TERRA_M-T | BOM JESUS | PIAUÍ | Brasil | 2201903 | 22 | 33 | nan | nan | nan | Cerrado | 16.6 |
| c2c0daa4-19ed-3187-9dc8-7836bf722ccc | -8.8014 | -44.72515 | 2024-10-24 12:12:00 | TERRA_M-T | CURRAIS | PIAUÍ | Brasil | 2203230 | 22 | 33 | nan | nan | nan | Cerrado | 29.0 |
| 587a5d43-055b-3e23-a6f1-cf1dc5fc1899 | -8.79101 | -44.73314 | 2024-10-24 12:12:00 | TERRA_M-T | CURRAIS | PIAUÍ | Brasil | 2203230 | 22 | 33 | nan | nan | nan | Cerrado | 21.4 |
| b58808e5-62f2-34bb-b6f7-55f65beb30b1 | -8.57878 | -45.11518 | 2024-10-24 12:12:00 | TERRA_M-T | BAIXA GRANDE DO RIBEIRO | PIAUÍ | Brasil | 2201150 | 22 | 33 | nan | nan | nan | Cerrado | 23.9 |
| 3a8223f1-c8e8-35ed-bb09-75d42bab007b | -8.5761 | -45.13199 | 2024-10-24 12:12:00 | TERRA_M-T | BAIXA GRANDE DO RIBEIRO | PIAUÍ | Brasil | 2201150 | 22 | 33 | nan | nan | nan | Cerrado | 25.1 |
| 749c3598-21d4-3cae-a838-e4cecf3b6d36 | -8.53475 | -44.45153 | 2024-10-24 12:12:00 | TERRA_M-T | PALMEIRA DO PIAUÍ | PIAUÍ | Brasil | 2207405 | 22 | 33 | nan | nan | nan | Cerrado | 16.0 |
| 86898a53-f6d0-3a0f-b7b7-fcc3f4165964 | -10.82432 | -45.27089 | 2024-10-24 12:12:00 | TERRA_M-T | FORMOSA DO RIO PRETO | BAHIA | Brasil | 2911105 | 29 | 33 | nan | nan | nan | Cerrado | 21.9 |
| 5c09c999-ee77-314e-ad3c-e2c16e30966c | -10.82045 | -45.27597 | 2024-10-24 12:12:00 | TERRA_M-T | FORMOSA DO RIO PRETO | BAHIA | Brasil | 2911105 | 29 | 33 | nan | nan | nan | Cerrado | 37.6 |
| 38280280-9f0a-3410-903c-830c487a8364 | -10.52102 | -44.85225 | 2024-10-24 12:12:00 | TERRA_M-T | SEBASTIÃO BARROS | PIAUÍ | Brasil | 2210623 | 22 | 33 | nan | nan | nan | Cerrado | 108.1 |
| 666bf8fa-36a5-3792-8311-4c218597c957 | -10.52009 | -44.86171 | 2024-10-24 12:12:00 | TERRA_M-T | SEBASTIÃO BARROS | PIAUÍ | Brasil | 2210623 | 22 | 33 | nan | nan | nan | Cerrado | 150.2 |
| d780ac8b-f6aa-387f-a1ce-c516643bdaa2 | -10.51854 | -44.86745 | 2024-10-24 12:12:00 | TERRA_M-T | SEBASTIÃO BARROS | PIAUÍ | Brasil | 2210623 | 22 | 33 | nan | nan | nan | Cerrado | 86.0 |
| f77d927c-27bf-3f39-8e34-533cee105adf | -9.90683 | -44.58741 | 2024-10-24 12:12:00 | TERRA_M-T | PARNAGUÁ | PIAUÍ | Brasil | 2207603 | 22 | 33 | nan | nan | nan | Cerrado | 19.2 |
| be64daca-3871-35c9-b137-b218448b650d | -11.63038 | -44.90855 | 2024-10-24 12:12:00 | TERRA_M-T | RIACHÃO DAS NEVES | BAHIA | Brasil | 2926202 | 29 | 33 | nan | nan | nan | Cerrado | 15.9 |
| c2b0a163-10b5-31d2-a59d-ec983cb9cc3b | -11.628 | -44.92312 | 2024-10-24 12:12:00 | TERRA_M-T | RIACHÃO DAS NEVES | BAHIA | Brasil | 2926202 | 29 | 33 | nan | nan | nan | Cerrado | 34.2 |
| 49a0138b-1763-3baf-b541-e28378168b62 | -11.54852 | -45.05713 | 2024-10-24 12:12:00 | TERRA_M-T | RIACHÃO DAS NEVES | BAHIA | Brasil | 2926202 | 29 | 33 | nan | nan | nan | Cerrado | 123.6 |
| 4884ba08-bfca-3b7e-9af8-8340a64bf43a | -10.84366 | -45.27996 | 2024-10-24 12:12:00 | TERRA_M-T | FORMOSA DO RIO PRETO | BAHIA | Brasil | 2911105 | 29 | 33 | nan | nan | nan | Cerrado | 60.8 |
| 70c82c2e-b47c-3245-9f1a-d1254cb08e6c | -10.8411 | -45.29562 | 2024-10-24 12:12:00 | TERRA_M-T | FORMOSA DO RIO PRETO | BAHIA | Brasil | 2911105 | 29 | 33 | nan | nan | nan | Cerrado | 106.7 |
| 3513418b-85c7-3b41-a5be-44f772268ce9 | -7.1466 | -45.44181 | 2024-10-24 12:12:00 | TERRA_M-T | SAMBAÍBA | MARANHÃO | Brasil | 2109700 | 21 | 33 | nan | nan | nan | Cerrado | 37.8 |
| 1a56dbb0-59a7-334f-99ba-b151f2e4ca99 | -6.94653 | -45.22224 | 2024-10-24 12:12:00 | TERRA_M-T | LORETO | MARANHÃO | Brasil | 2106102 | 21 | 33 | nan | nan | nan | Cerrado | 94.8 |
| 85247504-5e63-308f-a2f2-432b0eae4c21 | -6.9434 | -45.24147 | 2024-10-24 12:12:00 | TERRA_M-T | LORETO | MARANHÃO | Brasil | 2106102 | 21 | 33 | nan | nan | nan | Cerrado | 105.1 |
| d3944e95-562e-346c-89d8-6f04eec9dd0f | -6.94159 | -45.23478 | 2024-10-24 12:12:00 | TERRA_M-T | LORETO | MARANHÃO | Brasil | 2106102 | 21 | 33 | nan | nan | nan | Cerrado | 197.3 |
| 01ade518-0aa2-3725-9396-06ce7eaa8e14 | -10.47059 | -47.34874 | 2024-10-24 12:12:00 | TERRA_M-T | LAGOA DO TOCANTINS | TOCANTINS | Brasil | 1711951 | 17 | 33 | nan | nan | nan | Cerrado | 26.0 |
| 915d867a-85ea-3718-afb5-28ed8ad1318e | -10.46467 | -47.3418 | 2024-10-24 12:12:00 | TERRA_M-T | LAGOA DO TOCANTINS | TOCANTINS | Brasil | 1711951 | 17 | 33 | nan | nan | nan | Cerrado | 41.8 |
| 22620033-6588-3329-8fc1-884c5cd0346f | -6.51998 | -47.24947 | 2024-10-24 12:12:00 | TERRA_M-T | PORTO FRANCO | MARANHÃO | Brasil | 2109007 | 21 | 33 | nan | nan | nan | Cerrado | 35.1 |
| 64806ea2-5c76-3213-ab3c-6371cedd5e0e | -10.01542 | -47.45703 | 2024-10-24 12:12:00 | TERRA_M-T | NOVO ACORDO | TOCANTINS | Brasil | 1715101 | 17 | 33 | nan | nan | nan | Cerrado | 49.8 |
| 15a18920-77f3-3911-b129-3df3620289dc | -10.01931 | -47.46444 | 2024-10-24 12:12:00 | TERRA_M-T | NOVO ACORDO | TOCANTINS | Brasil | 1715101 | 17 | 33 | nan | nan | nan | Cerrado | 46.1 |
| b1accf90-9d8a-3434-8840-a5d6759364a1 | -10.02343 | -47.44016 | 2024-10-24 12:12:00 | TERRA_M-T | NOVO ACORDO | TOCANTINS | Brasil | 1715101 | 17 | 33 | nan | nan | nan | Cerrado | 59.5 |
| a2ae8b9f-614e-3194-8a94-ad04d45d1a9c | -10.03338 | -47.46664 | 2024-10-24 12:12:00 | TERRA_M-T | NOVO ACORDO | TOCANTINS | Brasil | 1715101 | 17 | 33 | nan | nan | nan | Cerrado | 31.3 |
| 1b1141ca-b9fb-3377-8548-809d44fc6f43 | -20.20135 | -40.30826 | 2024-10-24 12:14:00 | TERRA_M-T | SERRA | ESPÍRITO SANTO | Brasil | 3205002 | 32 | 33 | nan | nan | nan | Mata Atlântica | 7.6 |
| bcb978dc-6310-3155-923b-75f64ce26830 | -14.18699 | -40.34349 | 2024-10-24 12:14:00 | TERRA_M-T | MANOEL VITORINO | BAHIA | Brasil | 2920403 | 29 | 33 | nan | nan | nan | Caatinga | 12.9 |
| 1a7ebac2-50f6-33df-8a07-5575da45e494 | -15.61816 | -40.186 | 2024-10-24 12:14:00 | TERRA_M-T | MAIQUINIQUE | BAHIA | Brasil | 2920007 | 29 | 33 | nan | nan | nan | Mata Atlântica | 7.7 |
| 4dbf590d-8cf8-314b-8783-1e63a1a12c9f | -15.58279 | -39.84803 | 2024-10-24 12:14:00 | TERRA_M-T | POTIRAGUÁ | BAHIA | Brasil | 2925402 | 29 | 33 | nan | nan | nan | Mata Atlântica | 27.1 |
| 91d10d93-08b3-3dc3-83c3-27fab12c0baa | -15.42476 | -39.79344 | 2024-10-24 12:14:00 | TERRA_M-T | ITAPETINGA | BAHIA | Brasil | 2916401 | 29 | 33 | nan | nan | nan | Mata Atlântica | 17.1 |
| a10ee5e0-9b37-3138-9b02-21cf84eea68c | -15.30421 | -39.79913 | 2024-10-24 12:14:00 | TERRA_M-T | ITAJU DO COLÔNIA | BAHIA | Brasil | 2915403 | 29 | 33 | nan | nan | nan | Mata Atlântica | 7.2 |
| 40367fc7-db5f-308a-b13c-e95f8d6a7dfa | -15.12555 | -40.80263 | 2024-10-24 12:14:00 | TERRA_M-T | VITÓRIA DA CONQUISTA | BAHIA | Brasil | 2933307 | 29 | 33 | nan | nan | nan | Mata Atlântica | 18.5 |
| 1547c9c5-2629-3620-97d4-d8c5da046019 | -15.12424 | -40.81176 | 2024-10-24 12:14:00 | TERRA_M-T | VITÓRIA DA CONQUISTA | BAHIA | Brasil | 2933307 | 29 | 33 | nan | nan | nan | Mata Atlântica | 10.5 |
| b7597a2a-c926-375b-a589-f47949a30102 | -17.31921 | -40.92352 | 2024-10-24 12:14:00 | TERRA_M-T | CRISÓLITA | MINAS GERAIS | Brasil | 3120151 | 31 | 33 | nan | nan | nan | Mata Atlântica | 14.8 |
| 3b6a3824-69cd-3bf0-921c-ec1ff34fca64 | -18.93597 | -41.14643 | 2024-10-24 12:14:00 | TERRA_M-T | CONSELHEIRO PENA | MINAS GERAIS | Brasil | 3118403 | 31 | 33 | nan | nan | nan | Mata Atlântica | 10.6 |
| 4398498a-44aa-3a11-ad9a-10510e87d93d | -18.4378 | -41.14876 | 2024-10-24 12:14:00 | TERRA_M-T | ÁGUA DOCE DO NORTE | ESPÍRITO SANTO | Brasil | 3200169 | 32 | 33 | nan | nan | nan | Mata Atlântica | 12.6 |
| f5a667f0-09f6-3cbb-951f-8f04eedd0c70 | -18.4302 | -40.48276 | 2024-10-24 12:14:00 | TERRA_M-T | NOVA VENÉCIA | ESPÍRITO SANTO | Brasil | 3203908 | 32 | 33 | nan | nan | nan | Mata Atlântica | 53.0 |
| 67329e3b-6707-3a72-b0d4-c8fe59355c12 | -18.42886 | -40.4924 | 2024-10-24 12:14:00 | TERRA_M-T | NOVA VENÉCIA | ESPÍRITO SANTO | Brasil | 3203908 | 32 | 33 | nan | nan | nan | Mata Atlântica | 10.5 |
| 5ca9e84f-e703-3311-9399-739b848fe95a | -18.13847 | -41.05526 | 2024-10-24 12:14:00 | TERRA_M-T | ATALÉIA | MINAS GERAIS | Brasil | 3104700 | 31 | 33 | nan | nan | nan | Mata Atlântica | 7.2 |
| d042b6e6-92e0-3fc0-9602-cd6b1c859f2c | -20.2729 | -41.32294 | 2024-10-24 12:14:00 | TERRA_M-T | MUNIZ FREIRE | ESPÍRITO SANTO | Brasil | 3203700 | 32 | 33 | nan | nan | nan | Mata Atlântica | 21.9 |
| b34f8576-8300-3e51-bb69-b737458c34f5 | -20.252 | -41.79911 | 2024-10-24 12:14:00 | TERRA_M-T | MARTINS SOARES | MINAS GERAIS | Brasil | 3140530 | 31 | 33 | nan | nan | nan | Mata Atlântica | 8.3 |
| 91601285-6ea4-3eab-98a6-0952ce5e44e4 | -12.46661 | -46.83932 | 2024-10-24 12:14:00 | TERRA_M-T | TAGUATINGA | TOCANTINS | Brasil | 1720903 | 17 | 33 | nan | nan | nan | Cerrado | 63.2 |
| 4a7c6351-f1e2-3ff5-bac6-983f9c8f0e06 | -13.69018 | -41.47327 | 2024-10-24 12:14:00 | TERRA_M-T | ITUAÇU | BAHIA | Brasil | 2917201 | 29 | 33 | nan | nan | nan | Caatinga | 12.4 |
| 7eac8312-990a-341f-b011-2b994d5a53ef | -13.6406 | -41.56079 | 2024-10-24 12:14:00 | TERRA_M-T | JUSSIAPE | BAHIA | Brasil | 2918605 | 29 | 33 | nan | nan | nan | Caatinga | 21.0 |
| 5e1600c7-0011-3958-b20f-0920c793465f | -13.63922 | -41.57005 | 2024-10-24 12:14:00 | TERRA_M-T | JUSSIAPE | BAHIA | Brasil | 2918605 | 29 | 33 | nan | nan | nan | Caatinga | 19.6 |
| a51facc7-404f-3125-b531-d4893fea8fc1 | -13.62543 | -41.53961 | 2024-10-24 12:14:00 | TERRA_M-T | JUSSIAPE | BAHIA | Brasil | 2918605 | 29 | 33 | nan | nan | nan | Caatinga | 13.0 |
| ca577970-00e2-3ab2-bb54-1f5bd8100079 | -13.51367 | -40.91444 | 2024-10-24 12:14:00 | TERRA_M-T | IRAMAIA | BAHIA | Brasil | 2914307 | 29 | 33 | nan | nan | nan | Caatinga | 51.1 |
| 520f1dc0-e330-30ac-8a5c-bfacb5f164d9 | -13.51234 | -40.92353 | 2024-10-24 12:14:00 | TERRA_M-T | IRAMAIA | BAHIA | Brasil | 2914307 | 29 | 33 | nan | nan | nan | Caatinga | 102.7 |
| 0f6d4515-001e-3eb5-a849-e163b0bf3a99 | -13.37519 | -41.04519 | 2024-10-24 12:14:00 | TERRA_M-T | IRAMAIA | BAHIA | Brasil | 2914307 | 29 | 33 | nan | nan | nan | Caatinga | 10.9 |
| 20743ffe-11e8-3bcc-86d8-47ece2411c74 | -13.36629 | -41.0439 | 2024-10-24 12:14:00 | TERRA_M-T | IRAMAIA | BAHIA | Brasil | 2914307 | 29 | 33 | nan | nan | nan | Caatinga | 6.3 |
| bc33f926-e03a-3ec3-9514-08eb1e6d534e | -14.79016 | -41.51817 | 2024-10-24 12:14:00 | TERRA_M-T | MAETINGA | BAHIA | Brasil | 2919959 | 29 | 33 | nan | nan | nan | Caatinga | 7.1 |
| 9400cf28-3b65-3aa6-926a-d66c1f7afa91 | -14.74513 | -41.19592 | 2024-10-24 12:14:00 | TERRA_M-T | BELO CAMPO | BAHIA | Brasil | 2903508 | 29 | 33 | nan | nan | nan | Caatinga | 12.3 |
| 7cee016e-7dbe-3227-9b47-1e514e94a238 | -14.74379 | -41.20506 | 2024-10-24 12:14:00 | TERRA_M-T | BELO CAMPO | BAHIA | Brasil | 2903508 | 29 | 33 | nan | nan | nan | Caatinga | 16.2 |
| 523cc73a-eaea-3042-a81e-b9eb11d71121 | -14.65321 | -41.00776 | 2024-10-24 12:14:00 | TERRA_M-T | ANAGÉ | BAHIA | Brasil | 2901205 | 29 | 33 | nan | nan | nan | Caatinga | 7.8 |
| 1dbfc584-bdbf-3f9a-8068-245c567f45b1 | -14.57456 | -42.1 | 2024-10-24 12:14:00 | TERRA_M-T | GUAJERU | BAHIA | Brasil | 2911659 | 29 | 33 | nan | nan | nan | Caatinga | 10.9 |
| 38ba2dd1-a185-3358-97ff-1fbbfc615a99 | -14.55958 | -41.70673 | 2024-10-24 12:14:00 | TERRA_M-T | PRESIDENTE JÂNIO QUADROS | BAHIA | Brasil | 2925709 | 29 | 33 | nan | nan | nan | Caatinga | 9.0 |
| 86a43b16-e976-3418-9b42-0a16f572982b | -13.84432 | -41.24636 | 2024-10-24 12:14:00 | TERRA_M-T | ITUAÇU | BAHIA | Brasil | 2917201 | 29 | 33 | nan | nan | nan | Caatinga | 9.7 |
| f9993ee8-7104-347d-a2ed-52865af58721 | -13.77796 | -41.81457 | 2024-10-24 12:14:00 | TERRA_M-T | DOM BASÍLIO | BAHIA | Brasil | 2910107 | 29 | 33 | nan | nan | nan | Caatinga | 7.8 |
| 71a0d84a-f136-31b5-80d9-e45411743e85 | -15.72805 | -41.1605 | 2024-10-24 12:14:00 | TERRA_M-T | ENCRUZILHADA | BAHIA | Brasil | 2910404 | 29 | 33 | nan | nan | nan | Mata Atlântica | 13.7 |
| ae4ff2ce-9bba-3cf4-ad7b-8723de723bb9 | -17.75596 | -42.72348 | 2024-10-24 12:14:00 | TERRA_M-T | ITAMARANDIBA | MINAS GERAIS | Brasil | 3132503 | 31 | 33 | nan | nan | nan | Mata Atlântica | 5.3 |
| 22be2546-5a05-37ef-83d0-a9fbaa206693 | -16.73438 | -42.27816 | 2024-10-24 12:14:00 | TERRA_M-T | VIRGEM DA LAPA | MINAS GERAIS | Brasil | 3171600 | 31 | 33 | nan | nan | nan | Mata Atlântica | 12.2 |
| 9d8eb3a3-b3f2-34e4-a0b4-281084f19792 | -18.18671 | -42.8646 | 2024-10-24 12:14:00 | TERRA_M-T | COLUNA | MINAS GERAIS | Brasil | 3116803 | 31 | 33 | nan | nan | nan | Mata Atlântica | 8.3 |
| 8490380a-012b-388d-9746-fca9d3592b46 | -18.17542 | -42.44619 | 2024-10-24 12:14:00 | TERRA_M-T | SANTA MARIA DO SUAÇUÍ | MINAS GERAIS | Brasil | 3158201 | 31 | 33 | nan | nan | nan | Mata Atlântica | 11.7 |
| 0b0a39ba-a470-3757-87a6-c1bda68e4e02 | -13.71322 | -42.90589 | 2024-10-24 12:14:00 | TERRA_M-T | RIACHO DE SANTANA | BAHIA | Brasil | 2926400 | 29 | 33 | nan | nan | nan | Caatinga | 9.9 |
| 7ee911e2-64f5-3000-b853-df2493f793c5 | -13.57424 | -43.0815 | 2024-10-24 12:14:00 | TERRA_M-T | RIACHO DE SANTANA | BAHIA | Brasil | 2926400 | 29 | 33 | nan | nan | nan | Caatinga | 12.7 |
| 1b41b7ab-058f-338a-a03e-8d9cb77f2690 | -13.2173 | -43.06497 | 2024-10-24 12:14:00 | TERRA_M-T | BOM JESUS DA LAPA | BAHIA | Brasil | 2903904 | 29 | 33 | nan | nan | nan | Caatinga | 13.9 |
| b31455c6-b9ac-32d7-92cb-eb5bc406e14b | -13.21565 | -43.07557 | 2024-10-24 12:14:00 | TERRA_M-T | BOM JESUS DA LAPA | BAHIA | Brasil | 2903904 | 29 | 33 | nan | nan | nan | Caatinga | 61.7 |
| b304a55e-aa53-3871-b7ae-7fb326fe992a | -13.19774 | -43.31709 | 2024-10-24 12:14:00 | TERRA_M-T | BOM JESUS DA LAPA | BAHIA | Brasil | 2903904 | 29 | 33 | nan | nan | nan | Caatinga | 16.0 |
| 359197bd-1861-37cb-99fb-72c1f4470369 | -13.02178 | -43.19805 | 2024-10-24 12:14:00 | TERRA_M-T | BOM JESUS DA LAPA | BAHIA | Brasil | 2903904 | 29 | 33 | nan | nan | nan | Caatinga | 23.1 |
| 22687d1f-ded5-31f3-923c-b0e15c5c3787 | -13.02008 | -43.20893 | 2024-10-24 12:14:00 | TERRA_M-T | BOM JESUS DA LAPA | BAHIA | Brasil | 2903904 | 29 | 33 | nan | nan | nan | Caatinga | 10.6 |
| ea2141d4-3f5b-3ed2-bb03-9f69d7446b6a | -13.01211 | -43.19651 | 2024-10-24 12:14:00 | TERRA_M-T | BOM JESUS DA LAPA | BAHIA | Brasil | 2903904 | 29 | 33 | nan | nan | nan | Caatinga | 7.7 |
| 2e491386-5ecf-354a-a88f-29ec37af356a | -13.00368 | -43.10056 | 2024-10-24 12:14:00 | TERRA_M-T | PARATINGA | BAHIA | Brasil | 2923704 | 29 | 33 | nan | nan | nan | Caatinga | 12.6 |
| 7019f3c3-d469-3aa4-8672-ea7f3eebc160 | -12.62105 | -43.12576 | 2024-10-24 12:14:00 | TERRA_M-T | PARATINGA | BAHIA | Brasil | 2923704 | 29 | 33 | nan | nan | nan | Caatinga | 9.9 |
| f5dfdceb-635d-3552-be04-c9b9e6b773f9 | -12.51396 | -43.15829 | 2024-10-24 12:14:00 | TERRA_M-T | PARATINGA | BAHIA | Brasil | 2923704 | 29 | 33 | nan | nan | nan | Cerrado | 20.4 |
| c30d4c6b-6e81-3b49-ae7a-844d0801768c | -13.58649 | -42.5296 | 2024-10-24 12:14:00 | TERRA_M-T | TANQUE NOVO | BAHIA | Brasil | 2931053 | 29 | 33 | nan | nan | nan | Caatinga | 18.3 |
| a5824bc3-9eeb-3d41-8492-6467e24d4d7c | -13.55812 | -42.29624 | 2024-10-24 12:14:00 | TERRA_M-T | PARAMIRIM | BAHIA | Brasil | 2923605 | 29 | 33 | nan | nan | nan | Caatinga | 8.9 |
| dc9b7b69-0f0d-35d6-8fd6-2836d28b90ad | -13.44408 | -42.25328 | 2024-10-24 12:14:00 | TERRA_M-T | PARAMIRIM | BAHIA | Brasil | 2923605 | 29 | 33 | nan | nan | nan | Caatinga | 37.8 |
| 253e83c8-ad92-3de4-b4f4-6417d75f753a | -13.44259 | -42.26304 | 2024-10-24 12:14:00 | TERRA_M-T | PARAMIRIM | BAHIA | Brasil | 2923605 | 29 | 33 | nan | nan | nan | Caatinga | 96.7 |
| 9e7375a7-d522-3d0c-bf4e-8328a32ec7fd | -13.27326 | -42.53817 | 2024-10-24 12:14:00 | TERRA_M-T | BOTUPORÃ | BAHIA | Brasil | 2904209 | 29 | 33 | nan | nan | nan | Caatinga | 11.0 |
| 7c2a34fa-0f8e-3ce0-9aa9-9256e4c75181 | -13.16705 | -42.50482 | 2024-10-24 12:14:00 | TERRA_M-T | MACAÚBAS | BAHIA | Brasil | 2919801 | 29 | 33 | nan | nan | nan | Caatinga | 8.5 |
| 8eef96e5-2d93-3ee0-a53b-1fcac6954bd3 | -13.0388 | -42.42807 | 2024-10-24 12:14:00 | TERRA_M-T | MACAÚBAS | BAHIA | Brasil | 2919801 | 29 | 33 | nan | nan | nan | Caatinga | 6.4 |
| e7a00ab3-6b99-3532-a819-597bf86218c4 | -13.02205 | -42.05614 | 2024-10-24 12:14:00 | TERRA_M-T | PIATÃ | BAHIA | Brasil | 2924306 | 29 | 33 | nan | nan | nan | Caatinga | 16.5 |
| 6a640e77-eae7-3d99-9710-2a4220979020 | -12.94675 | -42.48931 | 2024-10-24 12:14:00 | TERRA_M-T | MACAÚBAS | BAHIA | Brasil | 2919801 | 29 | 33 | nan | nan | nan | Caatinga | 17.8 |
| 88b2e03d-a39c-30e0-8d91-8aabafcb7acf | -12.93996 | -42.23776 | 2024-10-24 12:14:00 | TERRA_M-T | IBIPITANGA | BAHIA | Brasil | 2912509 | 29 | 33 | nan | nan | nan | Caatinga | 8.7 |
| 26f6097f-0f7a-32b9-9936-c4064ca70aac | -12.88864 | -42.51537 | 2024-10-24 12:14:00 | TERRA_M-T | MACAÚBAS | BAHIA | Brasil | 2919801 | 29 | 33 | nan | nan | nan | Caatinga | 13.1 |
| 908a60d8-2f94-3231-8f8e-ffd7738832cf | -12.39143 | -42.37518 | 2024-10-24 12:14:00 | TERRA_M-T | OLIVEIRA DOS BREJINHOS | BAHIA | Brasil | 2923209 | 29 | 33 | nan | nan | nan | Caatinga | 9.5 |
| 18c60c89-2589-3ac8-a1f0-403aaa64ddc5 | -14.71672 | -42.7528 | 2024-10-24 12:14:00 | TERRA_M-T | URANDI | BAHIA | Brasil | 2932606 | 29 | 33 | nan | nan | nan | Caatinga | 12.1 |


[Clique aqui para ver as próximas entradas](README116.md)
