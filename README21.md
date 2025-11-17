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
| a851a5df-4257-33e6-8043-a910c1ac7d9f | -12.67341 | -47.16583 | 2025-11-17 03:49:00 | NOAA-20 | ARRAIAS | TOCANTINS | Brasil | 1702406 | 17 | 33 | nan | nan | nan | Cerrado | 3.1 |
| 19f11197-5b08-3d7e-90f8-2f79f4b44269 | -11.83843 | -49.22008 | 2025-11-17 03:49:00 | NOAA-20 | CARIRI DO TOCANTINS | TOCANTINS | Brasil | 1703867 | 17 | 33 | nan | nan | nan | Cerrado | 10.4 |
| 16a29ff6-8790-39c5-be48-585067266a2d | -8.53467 | -46.07551 | 2025-11-17 03:49:00 | NOAA-20 | TASSO FRAGOSO | MARANHÃO | Brasil | 2112001 | 21 | 33 | nan | nan | nan | Cerrado | 2.4 |
| 0c8e86a8-0c30-3db7-89c2-c1926bf1e70b | -10.1321 | -49.15451 | 2025-11-17 03:49:00 | NOAA-20 | CHAPADA DE AREIA | TOCANTINS | Brasil | 1704600 | 17 | 33 | nan | nan | nan | Cerrado | 1.7 |
| 5684ed1c-2db1-30ed-bc99-bfce9d491fc1 | -12.84555 | -46.01611 | 2025-11-17 03:49:00 | NOAA-20 | SÃO DESIDÉRIO | BAHIA | Brasil | 2928901 | 29 | 33 | nan | nan | nan | Cerrado | 1.4 |
| 6ab415d8-66a5-3060-98f7-7fd6d88486ed | -12.66187 | -47.17003 | 2025-11-17 03:49:00 | NOAA-20 | ARRAIAS | TOCANTINS | Brasil | 1702406 | 17 | 33 | nan | nan | nan | Cerrado | 1.3 |
| c5db6871-edea-3de3-b5f5-b6915218db1e | -3.66932 | -44.8914 | 2025-11-17 03:49:00 | NOAA-20 | VITÓRIA DO MEARIM | MARANHÃO | Brasil | 2112902 | 21 | 33 | nan | nan | nan | Amazônia | 2.1 |
| 50477c33-a891-38e6-afd4-6ee144e3ac56 | -10.9511 | -48.705 | 2025-11-17 03:49:00 | NOAA-20 | BREJINHO DE NAZARÉ | TOCANTINS | Brasil | 1703701 | 17 | 33 | nan | nan | nan | Cerrado | 2.9 |
| 2f48c67c-90a4-3cef-9ee4-e453481a9a60 | -12.79602 | -46.44475 | 2025-11-17 03:49:00 | NOAA-20 | LAVANDEIRA | TOCANTINS | Brasil | 1712157 | 17 | 33 | nan | nan | nan | Cerrado | 4.7 |
| 1eba7a9d-e799-3c58-b91e-2cd9bce98055 | -11.80444 | -45.30723 | 2025-11-17 03:49:00 | NOAA-20 | BARREIRAS | BAHIA | Brasil | 2903201 | 29 | 33 | nan | nan | nan | Cerrado | 14.6 |
| 120887d7-a113-3128-9cff-fe812067952d | -8.31774 | -45.41072 | 2025-11-17 03:49:00 | NOAA-20 | BAIXA GRANDE DO RIBEIRO | PIAUÍ | Brasil | 2201150 | 22 | 33 | nan | nan | nan | Cerrado | 2.1 |
| c526a595-5cbb-3822-aba6-ff4ac1c6934a | -11.9995 | -38.16642 | 2025-11-17 03:49:00 | NOAA-20 | ENTRE RIOS | BAHIA | Brasil | 2910503 | 29 | 33 | nan | nan | nan | Mata Atlântica | 0.6 |
| 8f092eb0-3687-35c7-91e1-f07bb8d45965 | -3.82415 | -45.56872 | 2025-11-17 03:49:00 | NOAA-20 | TUFILÂNDIA | MARANHÃO | Brasil | 2112274 | 21 | 33 | nan | nan | nan | Amazônia | 0.8 |
| f6e8face-0766-30c3-9d25-7dd5fe48e6cd | -8.52952 | -46.08214 | 2025-11-17 03:49:00 | NOAA-20 | TASSO FRAGOSO | MARANHÃO | Brasil | 2112001 | 21 | 33 | nan | nan | nan | Cerrado | 1.1 |
| a40f95e9-7e61-3ed9-84b1-66017d5ac2b0 | -12.8832 | -46.45861 | 2025-11-17 03:49:00 | NOAA-20 | COMBINADO | TOCANTINS | Brasil | 1705557 | 17 | 33 | nan | nan | nan | Cerrado | 2.3 |
| 5482ebd9-e8f3-3137-87f7-10176ed447d9 | -9.45306 | -44.85785 | 2025-11-17 03:49:00 | NOAA-20 | MONTE ALEGRE DO PIAUÍ | PIAUÍ | Brasil | 2206605 | 22 | 33 | nan | nan | nan | Cerrado | 3.3 |
| 0bc3d63e-307a-3437-bc9b-87d7bdacf772 | -9.04981 | -46.00923 | 2025-11-17 03:49:00 | NOAA-20 | ALTO PARNAÍBA | MARANHÃO | Brasil | 2100501 | 21 | 33 | nan | nan | nan | Cerrado | 1.4 |
| 866e1928-682a-3692-8613-eaaef285e694 | -3.62318 | -44.44334 | 2025-11-17 03:49:00 | NOAA-20 | CANTANHEDE | MARANHÃO | Brasil | 2102705 | 21 | 33 | nan | nan | nan | Cerrado | 1.2 |
| 39f2ef7a-0228-3da5-91f3-336a95d673cd | -3.4072 | -42.47262 | 2025-11-17 03:49:00 | NOAA-20 | SÃO BERNARDO | MARANHÃO | Brasil | 2110609 | 21 | 33 | nan | nan | nan | Caatinga | 0.9 |
| 38471420-491a-3f75-8656-3ff779fabdca | -11.69962 | -48.866 | 2025-11-17 03:49:00 | NOAA-20 | GURUPI | TOCANTINS | Brasil | 1709500 | 17 | 33 | nan | nan | nan | Cerrado | 7.1 |
| 8e76bcd4-0c92-3733-96e2-92d03908f750 | -12.8617 | -46.03563 | 2025-11-17 03:49:00 | NOAA-20 | SÃO DESIDÉRIO | BAHIA | Brasil | 2928901 | 29 | 33 | nan | nan | nan | Cerrado | 1.9 |
| aa87d41e-4603-39dc-960a-a4185b06b4d6 | -10.78621 | -44.3278 | 2025-11-17 03:49:00 | NOAA-20 | SANTA RITA DE CÁSSIA | BAHIA | Brasil | 2928406 | 29 | 33 | nan | nan | nan | Cerrado | 2.3 |
| 37dc0658-9d44-39b8-ae8c-ecf477610a2a | -11.569 | -42.42146 | 2025-11-17 03:49:00 | NOAA-20 | GENTIO DO OURO | BAHIA | Brasil | 2911303 | 29 | 33 | nan | nan | nan | Caatinga | 2.2 |
| 588f2ccc-4cf1-34d4-85c6-54e9afd82109 | -11.15637 | -49.45506 | 2025-11-17 03:49:00 | NOAA-20 | SANTA RITA DO TOCANTINS | TOCANTINS | Brasil | 1718899 | 17 | 33 | nan | nan | nan | Cerrado | 2.0 |
| 7cf64881-4029-3c33-84fe-f672bb41083f | -10.78754 | -44.32491 | 2025-11-17 03:49:00 | NOAA-20 | SANTA RITA DE CÁSSIA | BAHIA | Brasil | 2928406 | 29 | 33 | nan | nan | nan | Cerrado | 3.6 |
| 6d7c7c28-0785-362e-b601-01ae58928bee | -12.80664 | -46.44238 | 2025-11-17 03:49:00 | NOAA-20 | LAVANDEIRA | TOCANTINS | Brasil | 1712157 | 17 | 33 | nan | nan | nan | Cerrado | 2.9 |
| 651f3c62-9162-35ef-a4fa-3c2e5dfcce9c | -11.96865 | -44.29793 | 2025-11-17 03:49:00 | NOAA-20 | COTEGIPE | BAHIA | Brasil | 2909406 | 29 | 33 | nan | nan | nan | Cerrado | 9.9 |
| bae24e9a-ef88-3d29-a6ad-75f97da37f3d | -13.27548 | -47.29845 | 2025-11-17 03:49:00 | NOAA-20 | MONTE ALEGRE DE GOIÁS | GOIÁS | Brasil | 5213509 | 52 | 33 | nan | nan | nan | Cerrado | 2.2 |
| 27d4d5ff-a4fd-3feb-a5bf-7a377bb164fd | -3.61045 | -42.41768 | 2025-11-17 03:49:00 | NOAA-20 | JOCA MARQUES | PIAUÍ | Brasil | 2205458 | 22 | 33 | nan | nan | nan | Caatinga | 1.5 |
| 241961e1-acb1-31a1-94ee-b420deabbb04 | -12.41136 | -43.17025 | 2025-11-17 03:49:00 | NOAA-20 | PARATINGA | BAHIA | Brasil | 2923704 | 29 | 33 | nan | nan | nan | Cerrado | 1.8 |
| e2e606a8-96a0-33d1-b284-7f0dd83861d4 | -8.53521 | -46.07246 | 2025-11-17 03:49:00 | NOAA-20 | TASSO FRAGOSO | MARANHÃO | Brasil | 2112001 | 21 | 33 | nan | nan | nan | Cerrado | 3.4 |
| 0fa92079-4d61-31b1-b0bc-fd5760268ff2 | -3.66231 | -44.73418 | 2025-11-17 03:49:00 | NOAA-20 | ARARI | MARANHÃO | Brasil | 2101004 | 21 | 33 | nan | nan | nan | Amazônia | 1.4 |
| 201662ae-08ed-343a-902e-27c9f8e69aef | -8.57296 | -45.68176 | 2025-11-17 03:49:00 | NOAA-20 | SANTA FILOMENA | PIAUÍ | Brasil | 2209203 | 22 | 33 | nan | nan | nan | Cerrado | 1.4 |
| e6ecacef-5049-3839-a29e-c68f3b477696 | -3.88675 | -46.46801 | 2025-11-17 03:49:00 | NOAA-20 | BOM JARDIM | MARANHÃO | Brasil | 2102002 | 21 | 33 | nan | nan | nan | Amazônia | 1.6 |
| 44f6ef05-7281-353a-9d2c-6f28f73073e1 | -11.4042 | -43.32837 | 2025-11-17 03:49:00 | NOAA-20 | BARRA | BAHIA | Brasil | 2902708 | 29 | 33 | nan | nan | nan | Cerrado | 10.0 |
| eee5a4c9-ceb5-39d2-82e9-90ebd0a3fb83 | -10.85376 | -44.88346 | 2025-11-17 03:49:00 | NOAA-20 | CRISTALÂNDIA DO PIAUÍ | PIAUÍ | Brasil | 2203008 | 22 | 33 | nan | nan | nan | Cerrado | 2.7 |
| 16a0f8b7-747a-3995-8e3e-3fd0a6f12069 | -10.82027 | -44.3161 | 2025-11-17 03:49:00 | NOAA-20 | SANTA RITA DE CÁSSIA | BAHIA | Brasil | 2928406 | 29 | 33 | nan | nan | nan | Cerrado | 2.8 |
| 953371d7-d3ad-33aa-9c9e-eedf19537764 | -14.58972 | -45.22856 | 2025-11-17 03:49:00 | NOAA-20 | COCOS | BAHIA | Brasil | 2908101 | 29 | 33 | nan | nan | nan | Cerrado | 0.7 |
| b3c1dd29-4fd2-3cfc-a7e5-6a1c297fb968 | -8.54384 | -46.0624 | 2025-11-17 03:49:00 | NOAA-20 | TASSO FRAGOSO | MARANHÃO | Brasil | 2112001 | 21 | 33 | nan | nan | nan | Cerrado | 0.8 |
| 119cac53-6c32-3982-b0b0-157fa3a23a29 | -15.13135 | -43.74533 | 2025-11-17 03:49:00 | NOAA-20 | JAÍBA | MINAS GERAIS | Brasil | 3135050 | 31 | 33 | nan | nan | nan | Caatinga | 2.3 |
| dfe28446-b1cd-307e-ba44-6d6996e21696 | -11.71123 | -48.8688 | 2025-11-17 03:49:00 | NOAA-20 | GURUPI | TOCANTINS | Brasil | 1709500 | 17 | 33 | nan | nan | nan | Cerrado | 6.2 |
| ed0052fd-82e0-3bb5-b40e-4c24b14345d0 | -8.82567 | -47.36731 | 2025-11-17 03:49:00 | NOAA-20 | RECURSOLÂNDIA | TOCANTINS | Brasil | 1718501 | 17 | 33 | nan | nan | nan | Cerrado | 1.4 |
| d534e95a-510e-369d-9957-8503cc3b75cb | -10.92591 | -48.68778 | 2025-11-17 03:49:00 | NOAA-20 | BREJINHO DE NAZARÉ | TOCANTINS | Brasil | 1703701 | 17 | 33 | nan | nan | nan | Cerrado | 2.8 |
| 23687600-8d4c-34e8-9bd1-3749beb39064 | -8.53008 | -46.0791 | 2025-11-17 03:49:00 | NOAA-20 | TASSO FRAGOSO | MARANHÃO | Brasil | 2112001 | 21 | 33 | nan | nan | nan | Cerrado | 1.8 |
| a0bebe16-e5ca-311f-a56d-511dbd189354 | -4.0584 | -42.08609 | 2025-11-17 03:49:00 | NOAA-20 | BATALHA | PIAUÍ | Brasil | 2201507 | 22 | 33 | nan | nan | nan | Caatinga | 1.0 |
| 03239dc9-6894-3e08-9dbc-8f04b5227b24 | -11.40484 | -43.32463 | 2025-11-17 03:49:00 | NOAA-20 | BARRA | BAHIA | Brasil | 2902708 | 29 | 33 | nan | nan | nan | Cerrado | 10.0 |
| 74d2ae78-bf4b-3377-ab08-a7f4070121ff | -3.34794 | -43.49017 | 2025-11-17 03:49:00 | NOAA-20 | SÃO BENEDITO DO RIO PRETO | MARANHÃO | Brasil | 2110401 | 21 | 33 | nan | nan | nan | Cerrado | 8.9 |
| e54e5e2e-90e2-3e2f-9cbf-3a7553d976fb | -11.71051 | -44.45118 | 2025-11-17 03:49:00 | NOAA-20 | COTEGIPE | BAHIA | Brasil | 2909406 | 29 | 33 | nan | nan | nan | Cerrado | 3.9 |
| 29ab26fb-8bd3-3f39-9774-523959455be8 | -3.62366 | -44.4404 | 2025-11-17 03:49:00 | NOAA-20 | CANTANHEDE | MARANHÃO | Brasil | 2102705 | 21 | 33 | nan | nan | nan | Cerrado | 1.0 |
| fb619962-2eb4-335f-acd2-530623e0455e | -11.97484 | -43.99245 | 2025-11-17 03:49:00 | NOAA-20 | WANDERLEY | BAHIA | Brasil | 2933455 | 29 | 33 | nan | nan | nan | Cerrado | 1.2 |
| dd968337-4d2b-388d-a24e-6c7443640bab | -11.40701 | -43.33657 | 2025-11-17 03:49:00 | NOAA-20 | BARRA | BAHIA | Brasil | 2902708 | 29 | 33 | nan | nan | nan | Cerrado | 26.4 |
| 8910077a-2eb8-3e42-a4d9-d9ce13f8d491 | -2.51399 | -47.81427 | 2025-11-17 03:49:00 | NOAA-20 | IPIXUNA DO PARÁ | PARÁ | Brasil | 1503457 | 15 | 33 | nan | nan | nan | Amazônia | 9.6 |
| 5df62caf-bb54-34d9-b453-fcc0d3cb7d8b | -12.67611 | -47.1795 | 2025-11-17 03:49:00 | NOAA-20 | ARRAIAS | TOCANTINS | Brasil | 1702406 | 17 | 33 | nan | nan | nan | Cerrado | 1.4 |
| 97f9efc8-ce66-34bd-a699-f0895fce6017 | -3.46122 | -40.51263 | 2025-11-17 03:49:00 | NOAA-20 | MASSAPÊ | CEARÁ | Brasil | 2308005 | 23 | 33 | nan | nan | nan | Caatinga | 2.0 |
| d3663a37-0c7e-36ca-9724-0405416de103 | -8.53636 | -46.07401 | 2025-11-17 03:49:00 | NOAA-20 | TASSO FRAGOSO | MARANHÃO | Brasil | 2112001 | 21 | 33 | nan | nan | nan | Cerrado | 3.9 |
| 56c65d19-8cbb-3a62-ac0a-b95fda985c8e | -8.5358 | -46.07704 | 2025-11-17 03:49:00 | NOAA-20 | TASSO FRAGOSO | MARANHÃO | Brasil | 2112001 | 21 | 33 | nan | nan | nan | Cerrado | 1.8 |
| ea9ae8da-8745-3ac7-a2b5-a7ba2ebc837c | -3.55074 | -41.72183 | 2025-11-17 03:49:00 | NOAA-20 | CARAÚBAS DO PIAUÍ | PIAUÍ | Brasil | 2202539 | 22 | 33 | nan | nan | nan | Caatinga | 1.1 |
| 8ccc4c2d-d2d9-3d68-b7d0-4c5f8089d279 | -3.89969 | -45.18479 | 2025-11-17 03:49:00 | NOAA-20 | PIO XII | MARANHÃO | Brasil | 2108702 | 21 | 33 | nan | nan | nan | Amazônia | 0.9 |
| 9c533806-1fe3-3565-a195-db20b297d329 | -3.21639 | -43.3604 | 2025-11-17 03:49:00 | NOAA-20 | URBANO SANTOS | MARANHÃO | Brasil | 2112605 | 21 | 33 | nan | nan | nan | Cerrado | 2.0 |
| 8c2bb693-fe19-3501-9a53-aabc31e157ba | -10.91687 | -49.41809 | 2025-11-17 03:49:00 | NOAA-20 | SANTA RITA DO TOCANTINS | TOCANTINS | Brasil | 1718899 | 17 | 33 | nan | nan | nan | Cerrado | 1.5 |
| d2a1ec98-f3e8-37f9-8000-e99b70588abd | -10.13117 | -49.15924 | 2025-11-17 03:49:00 | NOAA-20 | CHAPADA DE AREIA | TOCANTINS | Brasil | 1704600 | 17 | 33 | nan | nan | nan | Cerrado | 1.5 |
| 0533f468-9f0a-3485-b806-e4112f387dd4 | -11.66992 | -44.72808 | 2025-11-17 03:49:00 | NOAA-20 | RIACHÃO DAS NEVES | BAHIA | Brasil | 2926202 | 29 | 33 | nan | nan | nan | Cerrado | 3.5 |
| 296067f2-60ec-371d-aeb9-e322f9c18490 | -12.86933 | -46.44283 | 2025-11-17 03:49:00 | NOAA-20 | COMBINADO | TOCANTINS | Brasil | 1705557 | 17 | 33 | nan | nan | nan | Cerrado | 4.9 |
| e7834666-c781-358d-af3d-d32be5bdff6f | -11.66829 | -44.73716 | 2025-11-17 03:49:00 | NOAA-20 | RIACHÃO DAS NEVES | BAHIA | Brasil | 2926202 | 29 | 33 | nan | nan | nan | Cerrado | 4.6 |
| 40ba19d6-2f01-372e-88d5-edd2f9531fb9 | -14.65187 | -46.54116 | 2025-11-17 03:49:00 | NOAA-20 | ALVORADA DO NORTE | GOIÁS | Brasil | 5200803 | 52 | 33 | nan | nan | nan | Cerrado | 2.7 |
| 1ceb4ab3-f712-38c9-ac6c-f60ffaedf43d | -12.80278 | -46.43575 | 2025-11-17 03:49:00 | NOAA-20 | LAVANDEIRA | TOCANTINS | Brasil | 1712157 | 17 | 33 | nan | nan | nan | Cerrado | 5.5 |
| 7059113d-a050-386d-8449-ba4aa931acca | -7.42982 | -48.94387 | 2025-11-17 03:49:00 | NOAA-20 | ARAGUAÍNA | TOCANTINS | Brasil | 1702109 | 17 | 33 | nan | nan | nan | Amazônia | 2.8 |
| 98e31e17-16e6-3568-99d0-a0ca2debd039 | -11.41482 | -43.3341 | 2025-11-17 03:49:00 | NOAA-20 | BARRA | BAHIA | Brasil | 2902708 | 29 | 33 | nan | nan | nan | Cerrado | 3.0 |
| 14445923-e645-35a3-b3b9-1ea9495dffab | -2.51861 | -47.82592 | 2025-11-17 03:49:00 | NOAA-20 | IPIXUNA DO PARÁ | PARÁ | Brasil | 1503457 | 15 | 33 | nan | nan | nan | Amazônia | 9.1 |
| 1ee93583-f2e9-34e9-9ecc-3bd8f4fab5d6 | -10.96536 | -44.52114 | 2025-11-17 03:49:00 | NOAA-20 | SANTA RITA DE CÁSSIA | BAHIA | Brasil | 2928406 | 29 | 33 | nan | nan | nan | Cerrado | 1.9 |
| e08714ce-cfef-3a94-acf6-43cb3fad0a24 | -14.6653 | -46.6003 | 2025-11-17 03:49:00 | NOAA-20 | ALVORADA DO NORTE | GOIÁS | Brasil | 5200803 | 52 | 33 | nan | nan | nan | Cerrado | 2.9 |
| 47bb5a1d-c3d9-3b08-b9eb-e19d0087077b | -10.55375 | -44.82127 | 2025-11-17 03:49:00 | NOAA-20 | SEBASTIÃO BARROS | PIAUÍ | Brasil | 2210623 | 22 | 33 | nan | nan | nan | Cerrado | 4.2 |
| 655c66ab-8b52-38e9-84cb-c03d1a060205 | -11.05286 | -47.60816 | 2025-11-17 03:49:00 | NOAA-20 | PINDORAMA DO TOCANTINS | TOCANTINS | Brasil | 1717008 | 17 | 33 | nan | nan | nan | Cerrado | 1.6 |
| 77f4cc87-d055-3119-a276-cdee5e5f4260 | -11.40765 | -43.33284 | 2025-11-17 03:49:00 | NOAA-20 | BARRA | BAHIA | Brasil | 2902708 | 29 | 33 | nan | nan | nan | Cerrado | 26.4 |
| 8a4d7c39-5297-303f-90f5-000b8b0d8e1d | -9.57605 | -49.12031 | 2025-11-17 03:49:00 | NOAA-20 | ABREULÂNDIA | TOCANTINS | Brasil | 1700251 | 17 | 33 | nan | nan | nan | Cerrado | 4.1 |
| ef4fb04e-e91b-3a2b-9242-5b135faca224 | -12.88575 | -46.46379 | 2025-11-17 03:49:00 | NOAA-20 | COMBINADO | TOCANTINS | Brasil | 1705557 | 17 | 33 | nan | nan | nan | Cerrado | 2.6 |
| bab2fa3e-d50a-30fa-9b22-fcb097031fbf | -9.32948 | -46.58083 | 2025-11-17 03:49:00 | NOAA-20 | ALTO PARNAÍBA | MARANHÃO | Brasil | 2100501 | 21 | 33 | nan | nan | nan | Cerrado | 10.5 |
| 1c18ee50-adf2-3bdc-9786-cb7281aa10d7 | -9.86985 | -44.19042 | 2025-11-17 03:49:00 | NOAA-20 | CURIMATÁ | PIAUÍ | Brasil | 2203206 | 22 | 33 | nan | nan | nan | Cerrado | 1.1 |
| 7c1826a3-f38c-33d7-af3a-36572caa9008 | -10.96824 | -44.53096 | 2025-11-17 03:49:00 | NOAA-20 | SANTA RITA DE CÁSSIA | BAHIA | Brasil | 2928406 | 29 | 33 | nan | nan | nan | Cerrado | 1.6 |
| 5e6b19b4-0d1d-3c45-817d-d4763ef14f72 | -15.1332 | -43.74408 | 2025-11-17 03:49:00 | NOAA-20 | JAÍBA | MINAS GERAIS | Brasil | 3135050 | 31 | 33 | nan | nan | nan | Caatinga | 3.2 |
| dc0f631d-cea2-3474-8dca-2ccc0051bcec | -10.57037 | -44.5471 | 2025-11-17 03:49:00 | NOAA-20 | PARNAGUÁ | PIAUÍ | Brasil | 2207603 | 22 | 33 | nan | nan | nan | Cerrado | 3.2 |
| 4be6096c-22f0-31da-b8ab-80b5e098f265 | -12.02509 | -47.01519 | 2025-11-17 03:49:00 | NOAA-20 | TAIPAS DO TOCANTINS | TOCANTINS | Brasil | 1720937 | 17 | 33 | nan | nan | nan | Cerrado | 2.0 |
| b91a1a0e-d91e-383e-b6ec-6cb2928b3412 | -3.66404 | -44.81976 | 2025-11-17 03:49:00 | NOAA-20 | VITÓRIA DO MEARIM | MARANHÃO | Brasil | 2112902 | 21 | 33 | nan | nan | nan | Amazônia | 1.4 |
| b2320029-6b20-3407-8b8e-8c192b32d73b | -3.40735 | -42.47453 | 2025-11-17 03:49:00 | NOAA-20 | SÃO BERNARDO | MARANHÃO | Brasil | 2110609 | 21 | 33 | nan | nan | nan | Caatinga | 2.1 |
| 02dbe1b8-bac3-35d5-9154-4fad8a8f5b41 | -8.33115 | -45.41876 | 2025-11-17 03:49:00 | NOAA-20 | BAIXA GRANDE DO RIBEIRO | PIAUÍ | Brasil | 2201150 | 22 | 33 | nan | nan | nan | Cerrado | 3.5 |
| 13adef94-9f01-3143-b491-26ac70563cde | -11.20345 | -46.62769 | 2025-11-17 03:49:00 | NOAA-20 | MATEIROS | TOCANTINS | Brasil | 1712702 | 17 | 33 | nan | nan | nan | Cerrado | 0.4 |
| 4401f823-c448-3fca-b466-9bc4162a3ef5 | -11.81657 | -47.58144 | 2025-11-17 03:49:00 | NOAA-20 | NATIVIDADE | TOCANTINS | Brasil | 1714203 | 17 | 33 | nan | nan | nan | Cerrado | 3.7 |
| 158cfa7d-aaf1-39f8-9026-89f516631aa7 | -11.78774 | -44.65062 | 2025-11-17 03:49:00 | NOAA-20 | ANGICAL | BAHIA | Brasil | 2901403 | 29 | 33 | nan | nan | nan | Cerrado | 5.5 |
| d3d6d038-f914-3303-8d4f-3af7f8ac9a98 | -3.65718 | -44.73328 | 2025-11-17 03:49:00 | NOAA-20 | ARARI | MARANHÃO | Brasil | 2101004 | 21 | 33 | nan | nan | nan | Amazônia | 1.4 |
| 7d032bf4-3996-39e8-b87f-d99ef953f29c | -11.92667 | -43.84836 | 2025-11-17 03:49:00 | NOAA-20 | WANDERLEY | BAHIA | Brasil | 2933455 | 29 | 33 | nan | nan | nan | Cerrado | 1.1 |
| 72aa4604-5b4c-3135-ba13-d9837861b137 | -10.85671 | -46.74587 | 2025-11-17 03:49:00 | NOAA-20 | MATEIROS | TOCANTINS | Brasil | 1712702 | 17 | 33 | nan | nan | nan | Cerrado | 17.0 |
| 1b0d7c05-6f27-3a2b-b580-d61a51be787b | -3.34636 | -43.4925 | 2025-11-17 03:49:00 | NOAA-20 | SÃO BENEDITO DO RIO PRETO | MARANHÃO | Brasil | 2110401 | 21 | 33 | nan | nan | nan | Cerrado | 3.0 |
| d43744ae-fe7d-3c56-8b9f-4ddad1ffadb1 | -12.69665 | -46.78263 | 2025-11-17 03:49:00 | NOAA-20 | ARRAIAS | TOCANTINS | Brasil | 1702406 | 17 | 33 | nan | nan | nan | Cerrado | 1.6 |
| a2f180dc-5348-3d5a-bae7-a108ceff3199 | -9.58111 | -49.12052 | 2025-11-17 03:49:00 | NOAA-20 | ABREULÂNDIA | TOCANTINS | Brasil | 1700251 | 17 | 33 | nan | nan | nan | Cerrado | 6.0 |
| db4561b7-917a-3f60-83b4-41e41a9bd6c9 | -11.8403 | -49.21077 | 2025-11-17 03:49:00 | NOAA-20 | CARIRI DO TOCANTINS | TOCANTINS | Brasil | 1703867 | 17 | 33 | nan | nan | nan | Cerrado | 10.7 |
| 52f48866-10bb-34d9-a7c5-3734f9ef90cf | -4.61584 | -38.68401 | 2025-11-17 03:49:00 | NOAA-20 | ARACOIABA | CEARÁ | Brasil | 2301208 | 23 | 33 | nan | nan | nan | Caatinga | 0.4 |
| 2a58aa1b-df5e-3963-8791-6888354bb373 | -12.85792 | -46.02936 | 2025-11-17 03:49:00 | NOAA-20 | SÃO DESIDÉRIO | BAHIA | Brasil | 2928901 | 29 | 33 | nan | nan | nan | Cerrado | 1.9 |
| 6db70975-f457-3beb-8291-3adbb232c393 | -9.71645 | -43.96048 | 2025-11-17 03:49:00 | NOAA-20 | MORRO CABEÇA NO TEMPO | PIAUÍ | Brasil | 2206654 | 22 | 33 | nan | nan | nan | Caatinga | 1.8 |
| bdb742eb-a15f-36ef-a2a6-29fca98d1f3b | -11.15733 | -49.45027 | 2025-11-17 03:49:00 | NOAA-20 | SANTA RITA DO TOCANTINS | TOCANTINS | Brasil | 1718899 | 17 | 33 | nan | nan | nan | Cerrado | 2.1 |
| 89fce098-6e34-385d-880a-71d80c29f9c3 | -14.58176 | -45.22249 | 2025-11-17 03:49:00 | NOAA-20 | COCOS | BAHIA | Brasil | 2908101 | 29 | 33 | nan | nan | nan | Cerrado | 1.1 |


[Clique aqui para ver as próximas entradas](README22.md)
