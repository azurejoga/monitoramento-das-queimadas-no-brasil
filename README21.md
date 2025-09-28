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

## Dados Diários - Página 21

| ID | Latitude | Longitude | Data/Hora GMT | Satélite | Município | Estado | País | Município ID | Estado ID | País ID | Dias sem Chuva | Precipitação | Risco de Fogo | Bioma | FRP |
|----|----------|-----------|---------------|----------|-----------|--------|------|--------------|-----------|---------|----------------|--------------|----------------|-------|-----|
| 0565c7da-b3ca-3a73-91df-3f0cffc04c91 | -11.9927 | -47.89209 | 2025-09-28 03:38:00 | NOAA-21 | SÃO VALÉRIO | TOCANTINS | Brasil | 1720499 | 17 | 33 | nan | nan | nan | Cerrado | 11.6 |
| 7b12d439-520b-3c23-b5b1-c5748e1d9914 | -15.08362 | -48.33068 | 2025-09-28 03:38:00 | NOAA-21 | MIMOSO DE GOIÁS | GOIÁS | Brasil | 5213053 | 52 | 33 | nan | nan | nan | Cerrado | 1.4 |
| 0521a3ae-d6ba-3196-a96e-943effe753f7 | -10.90753 | -45.74985 | 2025-09-28 03:38:00 | NOAA-21 | FORMOSA DO RIO PRETO | BAHIA | Brasil | 2911105 | 29 | 33 | nan | nan | nan | Cerrado | 8.1 |
| 82506cc9-88f3-39ec-8da4-c7d7755e6da0 | -11.61836 | -44.41869 | 2025-09-28 03:38:00 | NOAA-21 | COTEGIPE | BAHIA | Brasil | 2909406 | 29 | 33 | nan | nan | nan | Cerrado | 1.1 |
| be3c2c65-efe4-311b-804a-27607614c2b4 | -10.75469 | -45.38832 | 2025-09-28 03:38:00 | NOAA-21 | FORMOSA DO RIO PRETO | BAHIA | Brasil | 2911105 | 29 | 33 | nan | nan | nan | Cerrado | 4.1 |
| 67b51657-8f4d-370d-b5f7-dd492d61e9bf | -15.32452 | -47.89822 | 2025-09-28 03:38:00 | NOAA-21 | PLANALTINA | GOIÁS | Brasil | 5217609 | 52 | 33 | nan | nan | nan | Cerrado | 1.7 |
| b4018e67-8c95-3b47-a4c7-fc3f3d2f0a0a | -12.9075 | -45.15139 | 2025-09-28 03:38:00 | NOAA-21 | SÃO DESIDÉRIO | BAHIA | Brasil | 2928901 | 29 | 33 | nan | nan | nan | Cerrado | 2.5 |
| 9ec348ff-25e4-3004-adab-25a3b25752bd | -9.11553 | -46.67311 | 2025-09-28 03:38:00 | NOAA-21 | BALSAS | MARANHÃO | Brasil | 2101400 | 21 | 33 | nan | nan | nan | Cerrado | 2.3 |
| ac4cc3b8-3d67-3566-86c8-fc98617fc642 | -14.59064 | -48.265 | 2025-09-28 03:38:00 | NOAA-21 | NIQUELÂNDIA | GOIÁS | Brasil | 5214606 | 52 | 33 | nan | nan | nan | Cerrado | 1.5 |
| 8447f19c-54a2-32b5-a24e-9d1810721d4c | -11.37045 | -45.01297 | 2025-09-28 03:38:00 | NOAA-21 | RIACHÃO DAS NEVES | BAHIA | Brasil | 2926202 | 29 | 33 | nan | nan | nan | Cerrado | 5.0 |
| e90568db-113d-31b2-a6ae-49c6910c0160 | -12.97776 | -46.85057 | 2025-09-28 03:38:00 | NOAA-21 | ARRAIAS | TOCANTINS | Brasil | 1702406 | 17 | 33 | nan | nan | nan | Cerrado | 1.9 |
| 657ddd29-9089-3ffc-bc14-174669fda9ee | -12.97874 | -46.84566 | 2025-09-28 03:38:00 | NOAA-21 | ARRAIAS | TOCANTINS | Brasil | 1702406 | 17 | 33 | nan | nan | nan | Cerrado | 1.9 |
| 488f11f6-49b2-3b56-95d9-c437241da1cb | -12.0036 | -47.04552 | 2025-09-28 03:38:00 | NOAA-21 | TAIPAS DO TOCANTINS | TOCANTINS | Brasil | 1720937 | 17 | 33 | nan | nan | nan | Cerrado | 2.5 |
| 5593a519-ff4f-3c9a-81bb-b3c8d8b3011d | -13.78174 | -47.87622 | 2025-09-28 03:38:00 | NOAA-21 | CAVALCANTE | GOIÁS | Brasil | 5205307 | 52 | 33 | nan | nan | nan | Cerrado | 6.2 |
| 5d7f70ec-3c2d-317c-ac90-f9822351c853 | -11.98972 | -47.99266 | 2025-09-28 03:38:00 | NOAA-21 | SÃO VALÉRIO | TOCANTINS | Brasil | 1720499 | 17 | 33 | nan | nan | nan | Cerrado | 4.9 |
| c90a51c2-aa0f-391b-8a72-bff12984f7a0 | -15.61434 | -43.88262 | 2025-09-28 03:38:00 | NOAA-21 | VARZELÂNDIA | MINAS GERAIS | Brasil | 3170909 | 31 | 33 | nan | nan | nan | Caatinga | 2.4 |
| d20a2cca-f9d7-3223-935f-a1373a489c7e | -9.28718 | -45.70294 | 2025-09-28 03:38:00 | NOAA-21 | SANTA FILOMENA | PIAUÍ | Brasil | 2209203 | 22 | 33 | nan | nan | nan | Cerrado | 5.1 |
| b866d267-8d88-377e-9d70-84df9e363f12 | -9.78478 | -47.76516 | 2025-09-28 03:38:00 | NOAA-21 | RIO SONO | TOCANTINS | Brasil | 1718758 | 17 | 33 | nan | nan | nan | Cerrado | 2.6 |
| a2400247-2c9c-32ec-8511-54c39553d247 | -12.00041 | -47.0934 | 2025-09-28 03:38:00 | NOAA-21 | TAIPAS DO TOCANTINS | TOCANTINS | Brasil | 1720937 | 17 | 33 | nan | nan | nan | Cerrado | 6.3 |
| 24e73040-e48b-3182-b361-0a66601878db | -15.27728 | -46.45482 | 2025-09-28 03:38:00 | NOAA-21 | BURITIS | MINAS GERAIS | Brasil | 3109303 | 31 | 33 | nan | nan | nan | Cerrado | 1.1 |
| 6cf60c0a-1633-3694-a004-ee4bbf984832 | -9.21745 | -46.7691 | 2025-09-28 03:38:00 | NOAA-21 | BALSAS | MARANHÃO | Brasil | 2101400 | 21 | 33 | nan | nan | nan | Cerrado | 7.6 |
| c9f07eae-0aa6-341b-8b58-c48022e6eefe | -13.5185 | -47.40004 | 2025-09-28 03:38:00 | NOAA-21 | CAVALCANTE | GOIÁS | Brasil | 5205307 | 52 | 33 | nan | nan | nan | Cerrado | 2.0 |
| 7cc7da52-c400-3b3d-94f2-46f7b73a9e2d | -11.38852 | -46.98352 | 2025-09-28 03:38:00 | NOAA-21 | ALMAS | TOCANTINS | Brasil | 1700400 | 17 | 33 | nan | nan | nan | Cerrado | 5.7 |
| 16e304d0-b182-39b7-840d-78f5a0005c14 | -15.02436 | -47.14697 | 2025-09-28 03:38:00 | NOAA-21 | VILA BOA | GOIÁS | Brasil | 5222203 | 52 | 33 | nan | nan | nan | Cerrado | 4.4 |
| d0d3b0e4-8e8f-3bc9-a638-93443fc21d72 | -13.61952 | -47.31126 | 2025-09-28 03:38:00 | NOAA-21 | TERESINA DE GOIÁS | GOIÁS | Brasil | 5221080 | 52 | 33 | nan | nan | nan | Cerrado | 2.5 |
| 022fe3f6-7ff1-3a93-beb9-b1c790106daf | -13.71443 | -48.34567 | 2025-09-28 03:38:00 | NOAA-21 | MINAÇU | GOIÁS | Brasil | 5213087 | 52 | 33 | nan | nan | nan | Cerrado | 4.1 |
| 97b76854-2e97-3773-91e3-ac8921b337ef | -11.61366 | -44.41418 | 2025-09-28 03:38:00 | NOAA-21 | COTEGIPE | BAHIA | Brasil | 2909406 | 29 | 33 | nan | nan | nan | Cerrado | 1.3 |
| 400f5b28-7cac-34f4-b751-291187e8802a | -15.20875 | -48.05741 | 2025-09-28 03:38:00 | NOAA-21 | PADRE BERNARDO | GOIÁS | Brasil | 5215603 | 52 | 33 | nan | nan | nan | Cerrado | 1.4 |
| d47df876-0cb4-3aab-a611-876a19bcb99d | -14.76447 | -45.69236 | 2025-09-28 03:38:00 | NOAA-21 | COCOS | BAHIA | Brasil | 2908101 | 29 | 33 | nan | nan | nan | Cerrado | 0.9 |
| 06f9273f-0d2c-391d-a0c5-c4e7b481f649 | -11.99506 | -47.88047 | 2025-09-28 03:38:00 | NOAA-21 | SÃO VALÉRIO | TOCANTINS | Brasil | 1720499 | 17 | 33 | nan | nan | nan | Cerrado | 7.4 |
| fd066068-c8c1-36e0-b381-3b0624dc19f8 | -15.31938 | -47.89175 | 2025-09-28 03:38:00 | NOAA-21 | PLANALTINA | GOIÁS | Brasil | 5217609 | 52 | 33 | nan | nan | nan | Cerrado | 1.7 |
| 3977e0e5-d954-3b92-9e29-9642efe21685 | -11.99671 | -47.89375 | 2025-09-28 03:38:00 | NOAA-21 | SÃO VALÉRIO | TOCANTINS | Brasil | 1720499 | 17 | 33 | nan | nan | nan | Cerrado | 3.9 |
| cf3e5d7d-b8cf-3dd8-811e-dc4e3d12e8f8 | -15.33607 | -47.89415 | 2025-09-28 03:38:00 | NOAA-21 | PLANALTINA | GOIÁS | Brasil | 5217609 | 52 | 33 | nan | nan | nan | Cerrado | 1.0 |
| 666b708c-be90-3d5a-a3db-ad309e80fca9 | -11.37935 | -44.96805 | 2025-09-28 03:38:00 | NOAA-21 | SANTA RITA DE CÁSSIA | BAHIA | Brasil | 2928406 | 29 | 33 | nan | nan | nan | Cerrado | 3.3 |
| 8a8faaa8-3dba-3eb8-965f-126a4f890d25 | -16.18023 | -43.6503 | 2025-09-28 03:38:00 | NOAA-21 | CAPITÃO ENÉAS | MINAS GERAIS | Brasil | 3112703 | 31 | 33 | nan | nan | nan | Cerrado | 4.7 |
| 392ea505-5b96-358a-baff-1bce69509d65 | -12.95367 | -45.14928 | 2025-09-28 03:38:00 | NOAA-21 | SÃO DESIDÉRIO | BAHIA | Brasil | 2928901 | 29 | 33 | nan | nan | nan | Cerrado | 8.7 |
| aedb3858-b2e1-3680-86e9-1ab66c598b5c | -11.37014 | -44.96534 | 2025-09-28 03:38:00 | NOAA-21 | RIACHÃO DAS NEVES | BAHIA | Brasil | 2926202 | 29 | 33 | nan | nan | nan | Cerrado | 2.6 |
| 60176af2-cbd1-30f6-8cf3-cfc5addb6773 | -15.33498 | -47.89911 | 2025-09-28 03:38:00 | NOAA-21 | PLANALTINA | GOIÁS | Brasil | 5217609 | 52 | 33 | nan | nan | nan | Cerrado | 1.0 |
| f079beff-a514-3d6f-9e25-6ca67e96fd66 | -9.65783 | -43.85614 | 2025-09-28 03:38:00 | NOAA-21 | MORRO CABEÇA NO TEMPO | PIAUÍ | Brasil | 2206654 | 22 | 33 | nan | nan | nan | Caatinga | 1.3 |
| 0875eda9-e8c2-3ac7-bc8c-0d76ff36940b | -10.4226 | -46.15989 | 2025-09-28 03:38:00 | NOAA-21 | MATEIROS | TOCANTINS | Brasil | 1712702 | 17 | 33 | nan | nan | nan | Cerrado | 1.5 |
| 6583fc1b-42e1-346a-8315-90a255f0c64c | -11.98585 | -48.01108 | 2025-09-28 03:38:00 | NOAA-21 | SÃO VALÉRIO | TOCANTINS | Brasil | 1720499 | 17 | 33 | nan | nan | nan | Cerrado | 1.9 |
| 69cb271b-5b7e-3cc1-81c6-be47f41fda70 | -15.22145 | -48.05966 | 2025-09-28 03:38:00 | NOAA-21 | PADRE BERNARDO | GOIÁS | Brasil | 5215603 | 52 | 33 | nan | nan | nan | Cerrado | 2.4 |
| 0c31d441-3c26-3909-8bc5-161e9076e881 | -15.53545 | -47.91525 | 2025-09-28 03:38:00 | NOAA-21 | BRASÍLIA | DISTRITO FEDERAL | Brasil | 5300108 | 53 | 33 | nan | nan | nan | Cerrado | 5.5 |
| b4e85301-e8a0-34d2-a7c0-706b5dc31c0e | -15.58437 | -42.4077 | 2025-09-28 03:38:00 | NOAA-21 | RIO PARDO DE MINAS | MINAS GERAIS | Brasil | 3155603 | 31 | 33 | nan | nan | nan | Cerrado | 4.2 |
| f3ebaabe-9286-3e7e-a9e7-2f53a3767cb7 | -11.97914 | -47.89111 | 2025-09-28 03:38:00 | NOAA-21 | SÃO VALÉRIO | TOCANTINS | Brasil | 1720499 | 17 | 33 | nan | nan | nan | Cerrado | 5.0 |
| 90c51ac1-51fb-3629-bf88-0fccdb410cbb | -11.37216 | -45.01568 | 2025-09-28 03:38:00 | NOAA-21 | RIACHÃO DAS NEVES | BAHIA | Brasil | 2926202 | 29 | 33 | nan | nan | nan | Cerrado | 6.2 |
| fa667e66-c7f1-3e99-af0f-11c7e3da4bcc | -12.01786 | -47.92431 | 2025-09-28 03:38:00 | NOAA-21 | SÃO VALÉRIO | TOCANTINS | Brasil | 1720499 | 17 | 33 | nan | nan | nan | Cerrado | 6.8 |
| d913769b-a9ec-3b42-a30d-3cad1fb090ff | -16.40176 | -47.02163 | 2025-09-28 03:38:00 | NOAA-21 | UNAÍ | MINAS GERAIS | Brasil | 3170404 | 31 | 33 | nan | nan | nan | Cerrado | 1.8 |
| b2550436-5d95-3103-9ff2-31abd3444eec | -10.90759 | -44.81723 | 2025-09-28 03:38:00 | NOAA-21 | SANTA RITA DE CÁSSIA | BAHIA | Brasil | 2928406 | 29 | 33 | nan | nan | nan | Cerrado | 1.5 |
| eebc5e44-d212-3aee-b63b-51585874ea04 | -11.79309 | -44.86822 | 2025-09-28 03:38:00 | NOAA-21 | RIACHÃO DAS NEVES | BAHIA | Brasil | 2926202 | 29 | 33 | nan | nan | nan | Cerrado | 1.1 |
| c67b0a0b-bf37-3ea9-9533-31264eb41dfd | -13.25177 | -44.11354 | 2025-09-28 03:38:00 | NOAA-21 | SANTA MARIA DA VITÓRIA | BAHIA | Brasil | 2928109 | 29 | 33 | nan | nan | nan | Cerrado | 1.1 |
| e74d9db9-e16d-369a-8516-b30aca999d73 | -11.43482 | -44.92159 | 2025-09-28 03:38:00 | NOAA-21 | RIACHÃO DAS NEVES | BAHIA | Brasil | 2926202 | 29 | 33 | nan | nan | nan | Cerrado | 5.9 |
| 41fcd3fb-fd7f-36e3-8e69-e76321c55480 | -13.26154 | -48.4571 | 2025-09-28 03:38:00 | NOAA-21 | PALMEIRÓPOLIS | TOCANTINS | Brasil | 1715754 | 17 | 33 | nan | nan | nan | Cerrado | 1.9 |
| 4a89baa3-10c6-30e2-b26d-b3467afd113d | -12.90454 | -45.16629 | 2025-09-28 03:38:00 | NOAA-21 | SÃO DESIDÉRIO | BAHIA | Brasil | 2928901 | 29 | 33 | nan | nan | nan | Cerrado | 1.2 |
| 21de3f6b-6574-3ab7-ae36-86708d7c35d3 | -12.01063 | -47.95889 | 2025-09-28 03:38:00 | NOAA-21 | SÃO VALÉRIO | TOCANTINS | Brasil | 1720499 | 17 | 33 | nan | nan | nan | Cerrado | 13.5 |
| b3ba23ee-a519-351f-9f0e-99340d4cfccf | -15.62521 | -48.3601 | 2025-09-28 03:38:00 | NOAA-21 | PADRE BERNARDO | GOIÁS | Brasil | 5215603 | 52 | 33 | nan | nan | nan | Cerrado | 2.0 |
| 58d39399-549e-393a-a6ac-314297691b31 | -11.36451 | -44.96444 | 2025-09-28 03:38:00 | NOAA-21 | RIACHÃO DAS NEVES | BAHIA | Brasil | 2926202 | 29 | 33 | nan | nan | nan | Cerrado | 2.6 |
| e901a21a-28bc-3ebe-8edd-6c1e19412681 | -15.44513 | -48.22236 | 2025-09-28 03:38:00 | NOAA-21 | PADRE BERNARDO | GOIÁS | Brasil | 5215603 | 52 | 33 | nan | nan | nan | Cerrado | 5.3 |
| 597b55c3-d2ad-3b5c-b8d6-a17aa74248d7 | -11.39135 | -46.93667 | 2025-09-28 03:38:00 | NOAA-21 | PORTO ALEGRE DO TOCANTINS | TOCANTINS | Brasil | 1718006 | 17 | 33 | nan | nan | nan | Cerrado | 4.1 |
| 5592835e-d027-35b0-b8e6-e5fe9dba3ffd | -12.9038 | -45.17001 | 2025-09-28 03:38:00 | NOAA-21 | SÃO DESIDÉRIO | BAHIA | Brasil | 2928901 | 29 | 33 | nan | nan | nan | Cerrado | 1.2 |
| 56bf95a3-0999-34ae-80c2-8605565130e3 | -13.34994 | -47.29624 | 2025-09-28 03:38:00 | NOAA-21 | MONTE ALEGRE DE GOIÁS | GOIÁS | Brasil | 5213509 | 52 | 33 | nan | nan | nan | Cerrado | 2.9 |
| 122d59fb-9e7b-3aa3-a150-033cdf268896 | -15.3288 | -47.89757 | 2025-09-28 03:38:00 | NOAA-21 | PLANALTINA | GOIÁS | Brasil | 5217609 | 52 | 33 | nan | nan | nan | Cerrado | 2.7 |
| 0258b653-35b1-38be-9162-d4ceea633000 | -14.88273 | -47.9837 | 2025-09-28 03:38:00 | NOAA-21 | ÁGUA FRIA DE GOIÁS | GOIÁS | Brasil | 5200175 | 52 | 33 | nan | nan | nan | Cerrado | 1.3 |
| 9f31c272-537f-360e-a0db-ab6b907b9a16 | -11.36608 | -45.04756 | 2025-09-28 03:38:00 | NOAA-21 | FORMOSA DO RIO PRETO | BAHIA | Brasil | 2911105 | 29 | 33 | nan | nan | nan | Cerrado | 1.0 |
| 043e576f-edb6-3c89-a06c-de3af755cd94 | -11.9831 | -47.89297 | 2025-09-28 03:38:00 | NOAA-21 | SÃO VALÉRIO | TOCANTINS | Brasil | 1720499 | 17 | 33 | nan | nan | nan | Cerrado | 6.5 |
| 625a9802-adc1-38a9-88b4-30723daa1bf1 | -11.36761 | -44.94825 | 2025-09-28 03:38:00 | NOAA-21 | RIACHÃO DAS NEVES | BAHIA | Brasil | 2926202 | 29 | 33 | nan | nan | nan | Cerrado | 1.6 |
| 765462ff-92da-3832-82f7-b8dbedda20e0 | -15.28326 | -46.4259 | 2025-09-28 03:38:00 | NOAA-21 | BURITIS | MINAS GERAIS | Brasil | 3109303 | 31 | 33 | nan | nan | nan | Cerrado | 1.8 |
| cbfc5986-2c18-33a9-80be-834abbbd17a2 | -11.35967 | -44.95944 | 2025-09-28 03:38:00 | NOAA-21 | RIACHÃO DAS NEVES | BAHIA | Brasil | 2926202 | 29 | 33 | nan | nan | nan | Cerrado | 1.7 |
| 0588d178-d7ed-313e-9901-84b2c620c1f4 | -10.9084 | -45.74528 | 2025-09-28 03:38:00 | NOAA-21 | FORMOSA DO RIO PRETO | BAHIA | Brasil | 2911105 | 29 | 33 | nan | nan | nan | Cerrado | 8.1 |
| ab784573-dd09-3784-aba4-6dd2b10a73ca | -13.25875 | -48.45385 | 2025-09-28 03:38:00 | NOAA-21 | PALMEIRÓPOLIS | TOCANTINS | Brasil | 1715754 | 17 | 33 | nan | nan | nan | Cerrado | 4.0 |
| 948a18f6-4c12-3345-be22-323521a4d8f2 | -12.90052 | -45.15774 | 2025-09-28 03:38:00 | NOAA-21 | SÃO DESIDÉRIO | BAHIA | Brasil | 2928901 | 29 | 33 | nan | nan | nan | Cerrado | 2.7 |
| 7bf25867-9666-33ce-8b0f-799eea312f43 | -14.40609 | -42.48915 | 2025-09-28 03:38:00 | NOAA-21 | CACULÉ | BAHIA | Brasil | 2905008 | 29 | 33 | nan | nan | nan | Caatinga | 0.7 |
| 2282b47c-d06d-32f8-90f3-72ae4c378d2a | -14.76826 | -45.67376 | 2025-09-28 03:38:00 | NOAA-21 | COCOS | BAHIA | Brasil | 2908101 | 29 | 33 | nan | nan | nan | Cerrado | 2.0 |
| f64c0ffd-6b4f-32e5-ba68-f909a31f01e0 | -13.61854 | -47.3159 | 2025-09-28 03:38:00 | NOAA-21 | CAVALCANTE | GOIÁS | Brasil | 5205307 | 52 | 33 | nan | nan | nan | Cerrado | 2.5 |
| 595ed8dd-1692-3c91-b68d-cf648d94f984 | -14.33534 | -44.49788 | 2025-09-28 03:38:00 | NOAA-21 | MONTALVÂNIA | MINAS GERAIS | Brasil | 3142700 | 31 | 33 | nan | nan | nan | Cerrado | 4.5 |
| 8a067141-0ad9-34c2-857b-775c2f17182a | -11.94656 | -47.91556 | 2025-09-28 03:38:00 | NOAA-21 | SÃO VALÉRIO | TOCANTINS | Brasil | 1720499 | 17 | 33 | nan | nan | nan | Cerrado | 3.5 |
| 44a17230-b214-39da-a396-dd609d34d1ce | -15.90712 | -45.17963 | 2025-09-28 03:38:00 | NOAA-21 | PINTÓPOLIS | MINAS GERAIS | Brasil | 3150570 | 31 | 33 | nan | nan | nan | Cerrado | 1.0 |
| f2a35f4c-d0f3-3491-9939-7f595b0f43b1 | -15.58355 | -42.41216 | 2025-09-28 03:38:00 | NOAA-21 | RIO PARDO DE MINAS | MINAS GERAIS | Brasil | 3155603 | 31 | 33 | nan | nan | nan | Cerrado | 1.1 |
| effbdf81-ea3f-35c0-b2a0-ebb845153d9a | -10.41735 | -46.15414 | 2025-09-28 03:38:00 | NOAA-21 | MATEIROS | TOCANTINS | Brasil | 1712702 | 17 | 33 | nan | nan | nan | Cerrado | 2.1 |
| 974e5070-cdd7-3ebc-8214-4889d3e25372 | -11.44848 | -45.00057 | 2025-09-28 03:38:00 | NOAA-21 | RIACHÃO DAS NEVES | BAHIA | Brasil | 2926202 | 29 | 33 | nan | nan | nan | Cerrado | 3.2 |
| 923dbabf-0d79-37d0-9206-1355440c55c4 | -12.006 | -47.96231 | 2025-09-28 03:38:00 | NOAA-21 | SÃO VALÉRIO | TOCANTINS | Brasil | 1720499 | 17 | 33 | nan | nan | nan | Cerrado | 5.2 |
| 6e0e4d18-6df0-3afb-b9b8-2ab27ec4ddf8 | -11.37451 | -44.94249 | 2025-09-28 03:38:00 | NOAA-21 | RIACHÃO DAS NEVES | BAHIA | Brasil | 2926202 | 29 | 33 | nan | nan | nan | Cerrado | 2.0 |
| 68a3704b-c08c-3128-ac35-f58cbfdba644 | -14.58018 | -48.25087 | 2025-09-28 03:38:00 | NOAA-21 | NIQUELÂNDIA | GOIÁS | Brasil | 5214606 | 52 | 33 | nan | nan | nan | Cerrado | 3.1 |
| d1ffb228-3acd-33fa-9b8c-41f413a9044d | -11.78222 | -43.76395 | 2025-09-28 03:38:00 | NOAA-21 | WANDERLEY | BAHIA | Brasil | 2933455 | 29 | 33 | nan | nan | nan | Cerrado | 4.4 |
| bf2f2261-5724-311f-9be0-95898df8e4ee | -15.15126 | -46.42323 | 2025-09-28 03:38:00 | NOAA-21 | BURITIS | MINAS GERAIS | Brasil | 3109303 | 31 | 33 | nan | nan | nan | Cerrado | 1.4 |
| 9693a514-fa3c-3df5-95f6-3369e1279db0 | -12.0094 | -47.96479 | 2025-09-28 03:38:00 | NOAA-21 | SÃO VALÉRIO | TOCANTINS | Brasil | 1720499 | 17 | 33 | nan | nan | nan | Cerrado | 7.9 |
| 6635717a-770d-398b-8551-09a6580d78cb | -11.61138 | -44.41328 | 2025-09-28 03:38:00 | NOAA-21 | COTEGIPE | BAHIA | Brasil | 2909406 | 29 | 33 | nan | nan | nan | Cerrado | 1.6 |
| e1d720ea-61f1-3ada-ad2c-3579c4b97cc1 | -14.76903 | -45.66995 | 2025-09-28 03:38:00 | NOAA-21 | COCOS | BAHIA | Brasil | 2908101 | 29 | 33 | nan | nan | nan | Cerrado | 3.4 |
| 8c288e1d-c2ca-3378-ab3e-0724b1504256 | -13.78684 | -47.88374 | 2025-09-28 03:38:00 | NOAA-21 | CAVALCANTE | GOIÁS | Brasil | 5205307 | 52 | 33 | nan | nan | nan | Cerrado | 6.2 |
| 73b7f6d1-8b12-3025-a6c1-6cc70c954a30 | -15.33197 | -47.89381 | 2025-09-28 03:38:00 | NOAA-21 | PLANALTINA | GOIÁS | Brasil | 5217609 | 52 | 33 | nan | nan | nan | Cerrado | 3.5 |
| 84f42c83-0123-3a68-9cb6-d7b46d77dc14 | -11.58277 | -45.48559 | 2025-09-28 03:38:00 | NOAA-21 | RIACHÃO DAS NEVES | BAHIA | Brasil | 2926202 | 29 | 33 | nan | nan | nan | Cerrado | 1.5 |
| fd924236-7cbd-32d9-b401-2530968f1c49 | -15.54512 | -47.90955 | 2025-09-28 03:38:00 | NOAA-21 | BRASÍLIA | DISTRITO FEDERAL | Brasil | 5300108 | 53 | 33 | nan | nan | nan | Cerrado | 2.4 |
| a79a1518-6fe1-3aed-bced-5d3833adaf2a | -13.60554 | -47.32563 | 2025-09-28 03:38:00 | NOAA-21 | CAVALCANTE | GOIÁS | Brasil | 5205307 | 52 | 33 | nan | nan | nan | Cerrado | 4.1 |
| 41b7287c-56c9-3db8-b8cb-2774cc402d23 | -11.94536 | -47.92136 | 2025-09-28 03:38:00 | NOAA-21 | SÃO VALÉRIO | TOCANTINS | Brasil | 1720499 | 17 | 33 | nan | nan | nan | Cerrado | 4.9 |
| 6df27309-5ae7-3666-bb95-89ad6fe7cd76 | -11.68823 | -44.43227 | 2025-09-28 03:38:00 | NOAA-21 | COTEGIPE | BAHIA | Brasil | 2909406 | 29 | 33 | nan | nan | nan | Cerrado | 1.8 |
| 9b269386-a276-3b3e-adee-6c53b1c153ca | -9.87621 | -45.93413 | 2025-09-28 03:38:00 | NOAA-21 | ALTO PARNAÍBA | MARANHÃO | Brasil | 2100501 | 21 | 33 | nan | nan | nan | Cerrado | 1.4 |
| ebac8062-e9b9-32d8-9fc8-b13e02fb374a | -11.41067 | -46.95284 | 2025-09-28 03:38:00 | NOAA-21 | PORTO ALEGRE DO TOCANTINS | TOCANTINS | Brasil | 1718006 | 17 | 33 | nan | nan | nan | Cerrado | 3.6 |
| b76de8a5-38e0-3b5f-9327-a4fc667601fb | -15.5525 | -47.89685 | 2025-09-28 03:38:00 | NOAA-21 | BRASÍLIA | DISTRITO FEDERAL | Brasil | 5300108 | 53 | 33 | nan | nan | nan | Cerrado | 1.0 |
| 13bb39fd-123e-30e6-bad2-c14997c4c8bd | -14.88171 | -47.97533 | 2025-09-28 03:38:00 | NOAA-21 | ÁGUA FRIA DE GOIÁS | GOIÁS | Brasil | 5200175 | 52 | 33 | nan | nan | nan | Cerrado | 2.5 |
| 854e42a1-e220-328b-aaae-b8004e4c287e | -11.70162 | -44.42041 | 2025-09-28 03:38:00 | NOAA-21 | COTEGIPE | BAHIA | Brasil | 2909406 | 29 | 33 | nan | nan | nan | Cerrado | 1.5 |


[Clique aqui para ver as próximas entradas](README22.md)
