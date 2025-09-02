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

## Dados Diários - Página 92

| ID | Latitude | Longitude | Data/Hora GMT | Satélite | Município | Estado | País | Município ID | Estado ID | País ID | Dias sem Chuva | Precipitação | Risco de Fogo | Bioma | FRP |
|----|----------|-----------|---------------|----------|-----------|--------|------|--------------|-----------|---------|----------------|--------------|----------------|-------|-----|
| b369c959-4c82-3a1f-9d32-46bdc58e1825 | -11.43011 | -55.18507 | 2025-09-02 12:36:00 | TERRA_M-T | CLÁUDIA | MATO GROSSO | Brasil | 5103056 | 51 | 33 | nan | nan | nan | Amazônia | 16.8 |
| 34c03576-e661-3919-a227-d1dccc007e11 | -12.88466 | -48.04615 | 2025-09-02 12:36:00 | TERRA_M-T | PARANÃ | TOCANTINS | Brasil | 1716208 | 17 | 33 | nan | nan | nan | Cerrado | 17.0 |
| 192b698f-21ad-3e8a-acc9-641f28a434ca | -15.78204 | -48.13648 | 2025-09-02 12:36:00 | TERRA_M-T | BRASÍLIA | DISTRITO FEDERAL | Brasil | 5300108 | 53 | 33 | nan | nan | nan | Cerrado | 27.4 |
| 4cb9d3ad-bdec-35cf-9863-7ff7fe5d21a8 | -12.65702 | -45.32985 | 2025-09-02 12:36:00 | TERRA_M-T | SÃO DESIDÉRIO | BAHIA | Brasil | 2928901 | 29 | 33 | nan | nan | nan | Cerrado | 20.9 |
| ac8111ea-b6d9-3413-8e6e-fe96a9d3b306 | -15.5609 | -50.38686 | 2025-09-02 12:36:00 | TERRA_M-T | FAINA | GOIÁS | Brasil | 5207535 | 52 | 33 | nan | nan | nan | Cerrado | 13.6 |
| eac37122-398c-3f32-b571-37cd40808e2b | -14.33405 | -48.65467 | 2025-09-02 12:36:00 | TERRA_M-T | NIQUELÂNDIA | GOIÁS | Brasil | 5214606 | 52 | 33 | nan | nan | nan | Cerrado | 20.9 |
| 109676c7-6e7f-38d9-a8e4-eca8dd34d29f | -10.84492 | -45.02496 | 2025-09-02 12:36:00 | TERRA_M-T | CRISTALÂNDIA DO PIAUÍ | PIAUÍ | Brasil | 2203008 | 22 | 33 | nan | nan | nan | Cerrado | 40.3 |
| 5db3929b-9899-36b7-9b3b-ddfb3533ab99 | -12.97998 | -48.10273 | 2025-09-02 12:36:00 | TERRA_M-T | PARANÃ | TOCANTINS | Brasil | 1716208 | 17 | 33 | nan | nan | nan | Cerrado | 20.4 |
| e3357a02-0c98-3dd7-a73f-94ee9b998327 | -15.48524 | -51.23447 | 2025-09-02 12:36:00 | TERRA_M-T | BRITÂNIA | GOIÁS | Brasil | 5203807 | 52 | 33 | nan | nan | nan | Cerrado | 12.3 |
| 26574129-9704-39cc-8f6f-121c7c22a2be | -12.99217 | -48.09169 | 2025-09-02 12:36:00 | TERRA_M-T | PARANÃ | TOCANTINS | Brasil | 1716208 | 17 | 33 | nan | nan | nan | Cerrado | 23.8 |
| bd5ec388-3ff6-3023-964f-37fe250bffe3 | -11.48244 | -50.48948 | 2025-09-02 12:36:00 | TERRA_M-T | LAGOA DA CONFUSÃO | TOCANTINS | Brasil | 1711902 | 17 | 33 | nan | nan | nan | Cerrado | 10.6 |
| 93d9fb79-8d45-35eb-9ef2-6acbc3996d97 | -11.65653 | -52.18596 | 2025-09-02 12:36:00 | TERRA_M-T | SÃO FÉLIX DO ARAGUAIA | MATO GROSSO | Brasil | 5107859 | 51 | 33 | nan | nan | nan | Amazônia | 46.1 |
| bc090c94-e045-3e40-9842-11b036bfbdcf | -11.91568 | -50.61921 | 2025-09-02 12:36:00 | TERRA_M-T | FORMOSO DO ARAGUAIA | TOCANTINS | Brasil | 1708205 | 17 | 33 | nan | nan | nan | Cerrado | 22.2 |
| 6d9cf7ca-eabc-327e-820c-7c5c80c17d1f | -11.99721 | -51.34814 | 2025-09-02 12:36:00 | TERRA_M-T | SERRA NOVA DOURADA | MATO GROSSO | Brasil | 5107883 | 51 | 33 | nan | nan | nan | Cerrado | 7.1 |
| a1f1af02-8e9d-33d3-9bc1-f15719ea78dd | -10.4478 | -54.77343 | 2025-09-02 12:36:00 | TERRA_M-T | TERRA NOVA DO NORTE | MATO GROSSO | Brasil | 5108055 | 51 | 33 | nan | nan | nan | Amazônia | 9.0 |
| 4350be0a-41c9-3ef2-8a66-c57e40310ab5 | -12.92975 | -56.95305 | 2025-09-02 12:36:00 | TERRA_M-T | NOVA MARINGÁ | MATO GROSSO | Brasil | 5108907 | 51 | 33 | nan | nan | nan | Amazônia | 22.1 |
| dc78f88c-35bb-3e98-9d9b-a9a3005e1046 | -15.10673 | -48.1504 | 2025-09-02 12:36:00 | TERRA_M-T | MIMOSO DE GOIÁS | GOIÁS | Brasil | 5213053 | 52 | 33 | nan | nan | nan | Cerrado | 13.2 |
| 78b412ec-2e3f-3c33-be96-e0a30d0631db | -10.24866 | -51.13775 | 2025-09-02 12:36:00 | TERRA_M-T | VILA RICA | MATO GROSSO | Brasil | 5108600 | 51 | 33 | nan | nan | nan | Cerrado | 11.1 |
| ac0f9fd3-c629-3fc6-a3c5-1e8db6a3b400 | -16.30349 | -52.9435 | 2025-09-02 12:36:00 | TERRA_M-T | TORIXORÉU | MATO GROSSO | Brasil | 5108204 | 51 | 33 | nan | nan | nan | Cerrado | 31.5 |
| 13078a05-49ac-3cbd-85cf-eba94b281bd4 | -15.73781 | -49.00957 | 2025-09-02 12:36:00 | TERRA_M-T | PIRENÓPOLIS | GOIÁS | Brasil | 5217302 | 52 | 33 | nan | nan | nan | Cerrado | 11.7 |
| e19e5749-9cce-31fd-b351-6c67deee844c | -12.98162 | -48.08995 | 2025-09-02 12:36:00 | TERRA_M-T | PARANÃ | TOCANTINS | Brasil | 1716208 | 17 | 33 | nan | nan | nan | Cerrado | 50.4 |
| 50509309-66af-3b43-8ca9-c25deff71f0b | -17.85238 | -44.73883 | 2025-09-02 12:36:00 | TERRA_M-T | LASSANCE | MINAS GERAIS | Brasil | 3138104 | 31 | 33 | nan | nan | nan | Cerrado | 75.1 |
| 66b9db10-dfd6-3ba6-b435-41bb6600a5c4 | -11.18886 | -48.61259 | 2025-09-02 12:36:00 | TERRA_M-T | BREJINHO DE NAZARÉ | TOCANTINS | Brasil | 1703701 | 17 | 33 | nan | nan | nan | Cerrado | 10.0 |
| 4c59f44e-821a-3a86-af15-16f5280510e5 | -10.9725 | -50.77511 | 2025-09-02 12:36:00 | TERRA_M-T | LUCIARA | MATO GROSSO | Brasil | 5105309 | 51 | 33 | nan | nan | nan | Cerrado | 21.2 |
| a065d62a-7f51-3956-a6f0-dd50aa864db0 | -15.55953 | -50.39737 | 2025-09-02 12:36:00 | TERRA_M-T | FAINA | GOIÁS | Brasil | 5207535 | 52 | 33 | nan | nan | nan | Cerrado | 80.3 |
| f07581c6-f173-371e-a385-9233ad40e3c0 | -15.10444 | -48.14422 | 2025-09-02 12:36:00 | TERRA_M-T | MIMOSO DE GOIÁS | GOIÁS | Brasil | 5213053 | 52 | 33 | nan | nan | nan | Cerrado | 24.3 |
| 7ca12204-334e-3c0b-91f3-74dc12b7750a | -11.85917 | -51.47939 | 2025-09-02 12:36:00 | TERRA_M-T | ALTO BOA VISTA | MATO GROSSO | Brasil | 5100359 | 51 | 33 | nan | nan | nan | Cerrado | 12.9 |
| f26b6368-b6f6-30f0-a01a-ca5613c8ba79 | -11.9985 | -51.33905 | 2025-09-02 12:36:00 | TERRA_M-T | SERRA NOVA DOURADA | MATO GROSSO | Brasil | 5107883 | 51 | 33 | nan | nan | nan | Cerrado | 56.8 |
| c1996ed3-dc7b-3162-9a35-b97d073635f9 | -14.76406 | -48.14008 | 2025-09-02 12:36:00 | TERRA_M-T | NIQUELÂNDIA | GOIÁS | Brasil | 5214606 | 52 | 33 | nan | nan | nan | Cerrado | 16.1 |
| 8e8317d3-2712-3772-9f9b-421ee885fff5 | -15.25749 | -52.72683 | 2025-09-02 12:36:00 | TERRA_M-T | BARRA DO GARÇAS | MATO GROSSO | Brasil | 5101803 | 51 | 33 | nan | nan | nan | Cerrado | 13.6 |
| 05b442c3-68a2-36f7-9a5d-c7abf93dab2d | -11.67032 | -52.2155 | 2025-09-02 12:36:00 | TERRA_M-T | SÃO FÉLIX DO ARAGUAIA | MATO GROSSO | Brasil | 5107859 | 51 | 33 | nan | nan | nan | Amazônia | 31.9 |
| 4e97a9fc-78e7-3174-acd7-48c441c177d8 | -11.96356 | -45.79237 | 2025-09-02 12:36:00 | TERRA_M-T | LUÍS EDUARDO MAGALHÃES | BAHIA | Brasil | 2919553 | 29 | 33 | nan | nan | nan | Cerrado | 15.7 |
| 1307e1b3-ed44-3b20-85c5-c84f353c7d41 | -15.25486 | -52.74504 | 2025-09-02 12:36:00 | TERRA_M-T | BARRA DO GARÇAS | MATO GROSSO | Brasil | 5101803 | 51 | 33 | nan | nan | nan | Cerrado | 14.0 |
| 6b639453-522a-3b2b-addb-74777c3a55ef | -16.82408 | -52.13805 | 2025-09-02 12:36:00 | TERRA_M-T | CAIAPÔNIA | GOIÁS | Brasil | 5204409 | 52 | 33 | nan | nan | nan | Cerrado | 31.4 |
| 100779df-b8d4-36b8-a2b0-05907e1f9c8b | -11.66799 | -52.16927 | 2025-09-02 12:36:00 | TERRA_M-T | SÃO FÉLIX DO ARAGUAIA | MATO GROSSO | Brasil | 5107859 | 51 | 33 | nan | nan | nan | Amazônia | 13.5 |
| cc797077-e126-3ecc-876d-675e43e1b289 | -11.11707 | -50.60071 | 2025-09-02 12:36:00 | TERRA_M-T | LAGOA DA CONFUSÃO | TOCANTINS | Brasil | 1711902 | 17 | 33 | nan | nan | nan | Cerrado | 13.7 |
| 81c2ae81-cb85-3a96-8033-2297dbfbbfa8 | -12.41027 | -47.79589 | 2025-09-02 12:36:00 | TERRA_M-T | PARANÃ | TOCANTINS | Brasil | 1716208 | 17 | 33 | nan | nan | nan | Cerrado | 20.8 |
| c1157510-462a-3b6a-8760-982759591695 | -11.93641 | -50.60291 | 2025-09-02 12:36:00 | TERRA_M-T | FORMOSO DO ARAGUAIA | TOCANTINS | Brasil | 1708205 | 17 | 33 | nan | nan | nan | Cerrado | 10.1 |
| 1022c77c-903d-36ac-b6aa-48811ebea7c0 | -11.86045 | -51.47038 | 2025-09-02 12:36:00 | TERRA_M-T | ALTO BOA VISTA | MATO GROSSO | Brasil | 5100359 | 51 | 33 | nan | nan | nan | Cerrado | 118.9 |
| 4afdc649-cb6f-364b-a168-a8ef8d39b8c4 | -10.34364 | -48.143 | 2025-09-02 12:36:00 | TERRA_M-T | PALMAS | TOCANTINS | Brasil | 1721000 | 17 | 33 | nan | nan | nan | Cerrado | 12.0 |
| 90aaee10-4532-3773-a3d7-f449eb2cc4b4 | -15.24864 | -52.72551 | 2025-09-02 12:36:00 | TERRA_M-T | BARRA DO GARÇAS | MATO GROSSO | Brasil | 5101803 | 51 | 33 | nan | nan | nan | Cerrado | 14.2 |
| da871b7b-588a-3080-8a8b-6bf7cc905f03 | -11.66902 | -52.2245 | 2025-09-02 12:36:00 | TERRA_M-T | SÃO FÉLIX DO ARAGUAIA | MATO GROSSO | Brasil | 5107859 | 51 | 33 | nan | nan | nan | Amazônia | 14.2 |
| f4b242ec-33ce-34fa-b309-69e1c465aaf9 | -16.59403 | -48.98624 | 2025-09-02 12:36:00 | TERRA_M-T | BONFINÓPOLIS | GOIÁS | Brasil | 5203559 | 52 | 33 | nan | nan | nan | Cerrado | 19.0 |
| 392ef87b-0222-39e4-919e-1f39b44fbd93 | -11.67423 | -52.18854 | 2025-09-02 12:36:00 | TERRA_M-T | SÃO FÉLIX DO ARAGUAIA | MATO GROSSO | Brasil | 5107859 | 51 | 33 | nan | nan | nan | Amazônia | 30.7 |
| 741b6d8e-bb90-36c9-ba3a-72e484b9cfd1 | -14.47862 | -53.07236 | 2025-09-02 12:36:00 | TERRA_M-T | CAMPINÁPOLIS | MATO GROSSO | Brasil | 5102603 | 51 | 33 | nan | nan | nan | Cerrado | 4.2 |
| 82501f6f-527a-38b3-b02a-f5f47343431f | -17.28931 | -49.2041 | 2025-09-02 12:36:00 | TERRA_M-T | PROFESSOR JAMIL | GOIÁS | Brasil | 5218391 | 52 | 33 | nan | nan | nan | Cerrado | 13.2 |
| c0032e56-267d-3860-8724-9bb9a0f9f510 | -11.63824 | -52.04894 | 2025-09-02 12:36:00 | TERRA_M-T | SÃO FÉLIX DO ARAGUAIA | MATO GROSSO | Brasil | 5107859 | 51 | 33 | nan | nan | nan | Amazônia | 16.9 |
| 3a6ad95c-47b9-3d40-85ce-109bc77a7341 | -12.41207 | -47.7822 | 2025-09-02 12:36:00 | TERRA_M-T | PARANÃ | TOCANTINS | Brasil | 1716208 | 17 | 33 | nan | nan | nan | Cerrado | 33.4 |
| 10f9f330-7923-38e7-b3eb-bf686b3b398d | -11.6508 | -52.03849 | 2025-09-02 12:36:00 | TERRA_M-T | SÃO FÉLIX DO ARAGUAIA | MATO GROSSO | Brasil | 5107859 | 51 | 33 | nan | nan | nan | Amazônia | 31.5 |
| 3e700020-8458-39c2-bb29-34fab8beb7e4 | -11.9793 | -45.87077 | 2025-09-02 12:36:00 | TERRA_M-T | LUÍS EDUARDO MAGALHÃES | BAHIA | Brasil | 2919553 | 29 | 33 | nan | nan | nan | Cerrado | 23.6 |
| 56151d81-54ac-3838-b234-5a358a23ce9a | -11.06021 | -46.90342 | 2025-09-02 12:36:00 | TERRA_M-T | PONTE ALTA DO TOCANTINS | TOCANTINS | Brasil | 1717909 | 17 | 33 | nan | nan | nan | Cerrado | 38.1 |
| 4b30c5f1-aced-3eb5-b0fc-9c91dd105097 | -12.76004 | -44.80143 | 2025-09-02 12:36:00 | TERRA_M-T | SÃO DESIDÉRIO | BAHIA | Brasil | 2928901 | 29 | 33 | nan | nan | nan | Cerrado | 90.0 |
| a9c56234-a1ab-362e-8802-8c5a7369dc58 | -11.67554 | -52.17955 | 2025-09-02 12:36:00 | TERRA_M-T | SÃO FÉLIX DO ARAGUAIA | MATO GROSSO | Brasil | 5107859 | 51 | 33 | nan | nan | nan | Amazônia | 24.6 |
| 30f051a6-eeb1-37fa-a527-7d3e548b3c6e | -16.03287 | -48.05087 | 2025-09-02 12:36:00 | TERRA_M-T | BRASÍLIA | DISTRITO FEDERAL | Brasil | 5300108 | 53 | 33 | nan | nan | nan | Cerrado | 12.7 |
| 5083eecc-88dc-33db-b009-1757978998b6 | -12.93912 | -48.08545 | 2025-09-02 12:36:00 | TERRA_M-T | PARANÃ | TOCANTINS | Brasil | 1716208 | 17 | 33 | nan | nan | nan | Cerrado | 21.4 |
| 63b89419-4088-3fb7-ac4e-8cfed245c45c | -14.60469 | -48.03673 | 2025-09-02 12:36:00 | TERRA_M-T | NIQUELÂNDIA | GOIÁS | Brasil | 5214606 | 52 | 33 | nan | nan | nan | Cerrado | 23.6 |
| a725272e-f113-3ead-9087-0dac44a1d4f7 | -12.48878 | -48.02177 | 2025-09-02 12:36:00 | TERRA_M-T | PARANÃ | TOCANTINS | Brasil | 1716208 | 17 | 33 | nan | nan | nan | Cerrado | 11.5 |
| 80eb27c9-41bd-30c4-a16d-1abe1fe696c4 | -10.89962 | -50.83954 | 2025-09-02 12:36:00 | TERRA_M-T | LUCIARA | MATO GROSSO | Brasil | 5105309 | 51 | 33 | nan | nan | nan | Cerrado | 8.7 |
| 31f12481-9a62-3434-b3bc-a39497e0ac27 | -15.15492 | -52.34547 | 2025-09-02 12:36:00 | TERRA_M-T | BARRA DO GARÇAS | MATO GROSSO | Brasil | 5101803 | 51 | 33 | nan | nan | nan | Cerrado | 21.1 |
| 27e95aa4-e1a5-37a4-a8ab-4e80c38b8ec2 | -12.13081 | -45.92045 | 2025-09-02 12:36:00 | TERRA_M-T | LUÍS EDUARDO MAGALHÃES | BAHIA | Brasil | 2919553 | 29 | 33 | nan | nan | nan | Cerrado | 22.4 |
| f294be28-9981-3c4a-9c06-46df772f5940 | -11.39755 | -46.86259 | 2025-09-02 12:36:00 | TERRA_M-T | RIO DA CONCEIÇÃO | TOCANTINS | Brasil | 1718659 | 17 | 33 | nan | nan | nan | Cerrado | 20.2 |
| 1a3e3861-708e-3d66-a420-9c5f748eadfb | -12.14134 | -50.25363 | 2025-09-02 12:36:00 | TERRA_M-T | FORMOSO DO ARAGUAIA | TOCANTINS | Brasil | 1708205 | 17 | 33 | nan | nan | nan | Cerrado | 7.8 |
| 2c6fb07e-35bf-30f0-a47b-963487ca767d | -11.66669 | -52.17826 | 2025-09-02 12:36:00 | TERRA_M-T | SÃO FÉLIX DO ARAGUAIA | MATO GROSSO | Brasil | 5107859 | 51 | 33 | nan | nan | nan | Amazônia | 23.5 |
| da6b3a3e-63ca-3f51-b261-70f1127f6de3 | -10.47469 | -51.61717 | 2025-09-02 12:36:00 | TERRA_M-T | CONFRESA | MATO GROSSO | Brasil | 5103353 | 51 | 33 | nan | nan | nan | Amazônia | 5.1 |
| 64687456-1d34-38b0-8d3e-ed1142db1616 | -10.2951 | -47.50311 | 2025-09-02 12:36:00 | TERRA_M-T | LAGOA DO TOCANTINS | TOCANTINS | Brasil | 1711951 | 17 | 33 | nan | nan | nan | Cerrado | 29.2 |
| 480bc922-3f9e-3009-8da9-e733bd8bf42a | -11.11266 | -44.63514 | 2025-09-02 12:36:00 | TERRA_M-T | SANTA RITA DE CÁSSIA | BAHIA | Brasil | 2928406 | 29 | 33 | nan | nan | nan | Cerrado | 46.0 |
| 1bb582e1-5e38-36cd-827b-2c3808ef3310 | -11.4747 | -50.47879 | 2025-09-02 12:36:00 | TERRA_M-T | LAGOA DA CONFUSÃO | TOCANTINS | Brasil | 1711902 | 17 | 33 | nan | nan | nan | Cerrado | 20.3 |
| 91f41c9b-292d-39a5-923b-3a8b6bd39b6e | -10.84015 | -45.05217 | 2025-09-02 12:36:00 | TERRA_M-T | CRISTALÂNDIA DO PIAUÍ | PIAUÍ | Brasil | 2203008 | 22 | 33 | nan | nan | nan | Cerrado | 28.2 |
| 338c36ce-0c09-3e50-b45d-42a38bd606d1 | -14.83277 | -49.30329 | 2025-09-02 12:36:00 | TERRA_M-T | SÃO LUIZ DO NORTE | GOIÁS | Brasil | 5220157 | 52 | 33 | nan | nan | nan | Cerrado | 7.4 |
| b23e7674-53a7-3a21-87bf-0f85171a445c | -16.61525 | -50.19453 | 2025-09-02 12:36:00 | TERRA_M-T | TURVÂNIA | GOIÁS | Brasil | 5221502 | 52 | 33 | nan | nan | nan | Cerrado | 5.8 |
| 174cb2f2-f2fe-3254-9681-f3d350bfeb5f | -16.29333 | -52.95132 | 2025-09-02 12:36:00 | TERRA_M-T | TORIXORÉU | MATO GROSSO | Brasil | 5108204 | 51 | 33 | nan | nan | nan | Cerrado | 20.9 |
| 5af2200f-cd9b-3c6a-8ccb-e92011d81659 | -14.76226 | -48.15487 | 2025-09-02 12:36:00 | TERRA_M-T | NIQUELÂNDIA | GOIÁS | Brasil | 5214606 | 52 | 33 | nan | nan | nan | Cerrado | 14.4 |
| 9dde79f2-4ca5-371f-be41-2958180ab385 | -12.9274 | -56.96186 | 2025-09-02 12:36:00 | TERRA_M-T | NOVA MARINGÁ | MATO GROSSO | Brasil | 5108907 | 51 | 33 | nan | nan | nan | Amazônia | 27.2 |
| 4e784362-a32a-310e-ae04-52295bbb4b73 | -11.38425 | -46.87638 | 2025-09-02 12:36:00 | TERRA_M-T | RIO DA CONCEIÇÃO | TOCANTINS | Brasil | 1718659 | 17 | 33 | nan | nan | nan | Cerrado | 14.1 |
| 76f7752b-a56d-346a-b343-441962506729 | -11.65523 | -52.19495 | 2025-09-02 12:36:00 | TERRA_M-T | SÃO FÉLIX DO ARAGUAIA | MATO GROSSO | Brasil | 5107859 | 51 | 33 | nan | nan | nan | Amazônia | 39.9 |
| 77800f5b-b309-3a34-9ac9-926d4ede6c7a | -15.73456 | -49.01485 | 2025-09-02 12:36:00 | TERRA_M-T | PIRENÓPOLIS | GOIÁS | Brasil | 5217302 | 52 | 33 | nan | nan | nan | Cerrado | 27.0 |
| 65ada8e5-bb3a-3f24-922b-78a47c85a9d4 | -11.87045 | -50.61288 | 2025-09-02 12:36:00 | TERRA_M-T | FORMOSO DO ARAGUAIA | TOCANTINS | Brasil | 1708205 | 17 | 33 | nan | nan | nan | Cerrado | 13.9 |
| f0417070-7397-32d6-896b-5c42e131181e | -12.7842 | -47.6574 | 2025-09-02 12:36:00 | TERRA_M-T | PARANÃ | TOCANTINS | Brasil | 1716208 | 17 | 33 | nan | nan | nan | Cerrado | 16.2 |
| 63826012-9e9e-30d0-844b-8e6b31be96a5 | -14.62511 | -48.93976 | 2025-09-02 12:36:00 | TERRA_M-T | NIQUELÂNDIA | GOIÁS | Brasil | 5214606 | 52 | 33 | nan | nan | nan | Cerrado | 9.7 |
| deb68188-54b0-322c-bfbe-eda51ae2cd6b | -14.05046 | -44.56708 | 2025-09-02 12:36:00 | TERRA_M-T | COCOS | BAHIA | Brasil | 2908101 | 29 | 33 | nan | nan | nan | Cerrado | 26.1 |
| e5f1ade8-e6e9-3d1b-9d9e-fbe930854181 | -15.25618 | -52.73594 | 2025-09-02 12:36:00 | TERRA_M-T | BARRA DO GARÇAS | MATO GROSSO | Brasil | 5101803 | 51 | 33 | nan | nan | nan | Cerrado | 23.4 |
| e159b249-1ffe-3d64-9b6f-51dc7ee3262c | -11.38618 | -46.86122 | 2025-09-02 12:36:00 | TERRA_M-T | RIO DA CONCEIÇÃO | TOCANTINS | Brasil | 1718659 | 17 | 33 | nan | nan | nan | Cerrado | 48.3 |
| fe7e77be-7a4b-3d8a-9393-77d9f31a0beb | -15.73154 | -53.6435 | 2025-09-02 12:36:00 | TERRA_M-T | TESOURO | MATO GROSSO | Brasil | 5108105 | 51 | 33 | nan | nan | nan | Cerrado | 18.4 |
| f6dbd1ad-70a2-3423-990a-07a10b7cf915 | -13.89612 | -48.10718 | 2025-09-02 12:36:00 | TERRA_M-T | COLINAS DO SUL | GOIÁS | Brasil | 5205521 | 52 | 33 | nan | nan | nan | Cerrado | 14.3 |
| 6ca3df92-01b7-3e0e-9802-9e73f37ee921 | -11.844 | -51.45878 | 2025-09-02 12:36:00 | TERRA_M-T | ALTO BOA VISTA | MATO GROSSO | Brasil | 5100359 | 51 | 33 | nan | nan | nan | Cerrado | 19.0 |
| 2059fdf8-8866-34d8-a4c4-7ad897f8a2df | -11.90346 | -46.66961 | 2025-09-02 12:36:00 | TERRA_M-T | NOVO JARDIM | TOCANTINS | Brasil | 1715259 | 17 | 33 | nan | nan | nan | Cerrado | 13.7 |
| c2b1d4c9-da90-380e-b986-d2e6c29a6777 | -12.99054 | -48.1043 | 2025-09-02 12:36:00 | TERRA_M-T | PARANÃ | TOCANTINS | Brasil | 1716208 | 17 | 33 | nan | nan | nan | Cerrado | 14.3 |
| c828d040-be5c-3830-a91c-0c51ad5e0f80 | -14.20179 | -51.6615 | 2025-09-02 12:36:00 | TERRA_M-T | COCALINHO | MATO GROSSO | Brasil | 5103106 | 51 | 33 | nan | nan | nan | Cerrado | 16.2 |
| e3e9b2ed-8b24-368d-9f3d-0697a9910ac6 | -10.45772 | -54.77489 | 2025-09-02 12:36:00 | TERRA_M-T | TERRA NOVA DO NORTE | MATO GROSSO | Brasil | 5108055 | 51 | 33 | nan | nan | nan | Amazônia | 15.8 |
| d64272a2-37a7-38a8-8c93-169e2d95efd0 | -14.9904 | -50.20075 | 2025-09-02 12:36:00 | TERRA_M-T | CRIXÁS | GOIÁS | Brasil | 5206404 | 52 | 33 | nan | nan | nan | Cerrado | 15.6 |
| d92527fd-b24b-3461-b74c-915ab8e85679 | -10.75997 | -45.28516 | 2025-09-02 12:36:00 | TERRA_M-T | CRISTALÂNDIA DO PIAUÍ | PIAUÍ | Brasil | 2203008 | 22 | 33 | nan | nan | nan | Cerrado | 27.3 |
| 39fdbb5d-1307-30ab-b8c3-524f57e87fda | -11.9534 | -50.6117 | 2025-09-02 12:36:00 | TERRA_M-T | FORMOSO DO ARAGUAIA | TOCANTINS | Brasil | 1708205 | 17 | 33 | nan | nan | nan | Cerrado | 7.7 |
| 8969491d-31ed-34fa-bd90-920add57237b | -15.69722 | -53.62859 | 2025-09-02 12:36:00 | TERRA_M-T | GENERAL CARNEIRO | MATO GROSSO | Brasil | 5103908 | 51 | 33 | nan | nan | nan | Cerrado | 9.3 |
| dce58be6-b6ea-3662-af78-727ffcab71a4 | -12.61248 | -48.18915 | 2025-09-02 12:36:00 | TERRA_M-T | PARANÃ | TOCANTINS | Brasil | 1716208 | 17 | 33 | nan | nan | nan | Cerrado | 13.7 |
| 7fd0422f-8c8f-3a13-8e5e-be7817c9fb5a | -11.05956 | -46.90916 | 2025-09-02 12:36:00 | TERRA_M-T | PONTE ALTA DO TOCANTINS | TOCANTINS | Brasil | 1717909 | 17 | 33 | nan | nan | nan | Cerrado | 24.4 |
| 499da4ae-3bf6-3273-8800-b8ed74864e84 | -10.84121 | -47.27998 | 2025-09-02 12:36:00 | TERRA_M-T | PONTE ALTA DO TOCANTINS | TOCANTINS | Brasil | 1717909 | 17 | 33 | nan | nan | nan | Cerrado | 13.8 |
| f487286a-9f9e-3e9b-9d4e-c7648800be56 | -13.31177 | -46.82846 | 2025-09-02 12:36:00 | TERRA_M-T | MONTE ALEGRE DE GOIÁS | GOIÁS | Brasil | 5213509 | 52 | 33 | nan | nan | nan | Cerrado | 21.8 |
| ac43f299-326b-3259-a6d9-aaa3ec7c6dde | -13.30002 | -46.82705 | 2025-09-02 12:36:00 | TERRA_M-T | MONTE ALEGRE DE GOIÁS | GOIÁS | Brasil | 5213509 | 52 | 33 | nan | nan | nan | Cerrado | 44.4 |
| 7e1f6d61-2949-3d3b-adb5-88cf0a2af737 | -11.68308 | -52.18983 | 2025-09-02 12:36:00 | TERRA_M-T | SÃO FÉLIX DO ARAGUAIA | MATO GROSSO | Brasil | 5107859 | 51 | 33 | nan | nan | nan | Amazônia | 9.7 |
| 21fd8e6c-784b-3d58-b626-e3e4f4650acd | -12.84967 | -48.06713 | 2025-09-02 12:36:00 | TERRA_M-T | PARANÃ | TOCANTINS | Brasil | 1716208 | 17 | 33 | nan | nan | nan | Cerrado | 10.5 |


[Clique aqui para ver as próximas entradas](README93.md)
