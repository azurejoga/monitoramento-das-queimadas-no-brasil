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
| c130f562-c060-38ce-abc8-91d05af5bf93 | -11.04014 | -49.6876 | 2026-09-12 04:34:00 | NOAA-21 | SANTA RITA DO TOCANTINS | TOCANTINS | Brasil | 1718899 | 17 | 33 | nan | nan | nan | Cerrado | 0.7 |
| f877d141-bd06-3472-acdd-82de06a774f4 | -11.3495 | -45.7909 | 2026-09-12 04:34:00 | NOAA-21 | FORMOSA DO RIO PRETO | BAHIA | Brasil | 2911105 | 29 | 33 | nan | nan | nan | Cerrado | 1.2 |
| 645c8ad0-d573-31d9-b6c0-5e789c979f68 | -5.82557 | -53.8013 | 2026-09-12 04:34:00 | NOAA-21 | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 2.4 |
| 5a9c72e4-ef08-3a54-ba43-ca3263c35c60 | -5.79735 | -53.81305 | 2026-09-12 04:34:00 | NOAA-21 | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 1.5 |
| 2c9b4615-f1b7-35c4-9966-93632e3999d1 | -9.18582 | -59.4496 | 2026-09-12 04:34:00 | NOAA-21 | COLNIZA | MATO GROSSO | Brasil | 5103254 | 51 | 33 | nan | nan | nan | Amazônia | 3.0 |
| d6765167-6a12-3a3a-8438-a977c9955b0e | -9.63553 | -49.01547 | 2026-09-12 04:34:00 | NOAA-21 | ABREULÂNDIA | TOCANTINS | Brasil | 1700251 | 17 | 33 | nan | nan | nan | Cerrado | 0.5 |
| ec1974cf-d9da-3c39-a2be-2253df20da2d | -6.33833 | -55.30076 | 2026-09-12 04:34:00 | NOAA-21 | ITAITUBA | PARÁ | Brasil | 1503606 | 15 | 33 | nan | nan | nan | Amazônia | 4.5 |
| 3ca52ef2-4214-3191-9849-8e752502f4a1 | -9.79598 | -47.11301 | 2026-09-12 04:34:00 | NOAA-21 | RIO SONO | TOCANTINS | Brasil | 1718758 | 17 | 33 | nan | nan | nan | Cerrado | 2.6 |
| fe0ca124-ec40-3da6-8520-4742a9faa60f | -11.42747 | -51.43183 | 2026-09-12 04:34:00 | NOAA-21 | SÃO FÉLIX DO ARAGUAIA | MATO GROSSO | Brasil | 5107859 | 51 | 33 | nan | nan | nan | Amazônia | 1.9 |
| 80973e63-81ef-3875-afa6-15eb7e1bdcda | -6.86209 | -47.433 | 2026-09-12 04:34:00 | NOAA-21 | ESTREITO | MARANHÃO | Brasil | 2104057 | 21 | 33 | nan | nan | nan | Cerrado | 2.1 |
| 2d7fdacc-3043-37b4-9e94-a69de73793f5 | -12.12668 | -48.96023 | 2026-09-12 04:34:00 | NOAA-21 | FIGUEIRÓPOLIS | TOCANTINS | Brasil | 1707652 | 17 | 33 | nan | nan | nan | Cerrado | 2.0 |
| ed48fa54-69d8-3074-a110-970be1ee28ca | -10.90626 | -47.83396 | 2026-09-12 04:34:00 | NOAA-21 | MONTE DO CARMO | TOCANTINS | Brasil | 1713601 | 17 | 33 | nan | nan | nan | Cerrado | 1.3 |
| f016e82d-9a88-3047-9ffe-b8d47f397b33 | -6.39445 | -55.19865 | 2026-09-12 04:34:00 | NOAA-21 | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 3.3 |
| 8420fa0d-4537-317f-a212-6bb3f87be487 | -11.04162 | -47.96795 | 2026-09-12 04:34:00 | NOAA-21 | MONTE DO CARMO | TOCANTINS | Brasil | 1713601 | 17 | 33 | nan | nan | nan | Cerrado | 2.8 |
| 7ed88ad4-e020-391f-87e5-5de34ba16c69 | -13.65736 | -43.92474 | 2026-09-12 04:34:00 | NOAA-21 | SERRA DO RAMALHO | BAHIA | Brasil | 2930154 | 29 | 33 | nan | nan | nan | Cerrado | 1.3 |
| ffba4b66-657b-3672-8fd9-b1ac44c0d2bb | -10.55644 | -51.36509 | 2026-09-12 04:34:00 | NOAA-21 | CONFRESA | MATO GROSSO | Brasil | 5103353 | 51 | 33 | nan | nan | nan | Amazônia | 1.7 |
| 3481f746-e4d7-3ea7-b8b7-6f9070ea5b22 | -5.97344 | -57.77024 | 2026-09-12 04:34:00 | NOAA-21 | JACAREACANGA | PARÁ | Brasil | 1503754 | 15 | 33 | nan | nan | nan | Amazônia | 2.8 |
| a9de5c73-a79d-3eb2-8d74-22df174d9925 | -9.70651 | -43.45847 | 2026-09-12 04:34:00 | NOAA-21 | PILÃO ARCADO | BAHIA | Brasil | 2924405 | 29 | 33 | nan | nan | nan | Cerrado | 2.6 |
| 04dc2bcf-4c72-3082-ba4b-aa29557eba50 | -10.51205 | -51.30963 | 2026-09-12 04:34:00 | NOAA-21 | CONFRESA | MATO GROSSO | Brasil | 5103353 | 51 | 33 | nan | nan | nan | Amazônia | 6.9 |
| 68bc43f0-e267-30c4-856c-bab73063d00d | -9.69075 | -43.42199 | 2026-09-12 04:34:00 | NOAA-21 | PILÃO ARCADO | BAHIA | Brasil | 2924405 | 29 | 33 | nan | nan | nan | Caatinga | 1.4 |
| 709aa548-7744-34a2-9e05-5a552285b578 | -6.77254 | -59.43039 | 2026-09-12 04:34:00 | NOAA-21 | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 2.9 |
| ff0f0138-9992-36b1-8ed6-a172077e1dc9 | -6.32417 | -43.75035 | 2026-09-12 04:34:00 | NOAA-21 | SÃO JOÃO DOS PATOS | MARANHÃO | Brasil | 2111102 | 21 | 33 | nan | nan | nan | Cerrado | 2.2 |
| 1778f961-4ad0-3ba0-8a10-f58adb2a8e8e | -10.49192 | -51.36654 | 2026-09-12 04:34:00 | NOAA-21 | CONFRESA | MATO GROSSO | Brasil | 5103353 | 51 | 33 | nan | nan | nan | Amazônia | 3.8 |
| 400176ab-1940-3b3f-aa55-ffdfb04339dc | -5.82197 | -53.79655 | 2026-09-12 04:34:00 | NOAA-21 | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 2.6 |
| cf01272a-2527-30fd-b5e6-f16634d32546 | -9.79709 | -47.10565 | 2026-09-12 04:34:00 | NOAA-21 | RIO SONO | TOCANTINS | Brasil | 1718758 | 17 | 33 | nan | nan | nan | Cerrado | 2.6 |
| af0c0fa4-a89e-3f4c-8af1-29dbe35edb2f | -4.5338 | -54.95617 | 2026-09-12 04:34:00 | NOAA-21 | RURÓPOLIS | PARÁ | Brasil | 1506195 | 15 | 33 | nan | nan | nan | Amazônia | 1.7 |
| 39681df5-3624-3e4f-ac26-f2c4b2d54b49 | -8.70668 | -49.61797 | 2026-09-12 04:34:00 | NOAA-21 | CONCEIÇÃO DO ARAGUAIA | PARÁ | Brasil | 1502707 | 15 | 33 | nan | nan | nan | Amazônia | 2.6 |
| ec59c159-57e3-3f19-a3b2-a4d8fb119bc9 | -8.32003 | -54.76196 | 2026-09-12 04:34:00 | NOAA-21 | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 2.0 |
| e7b7dc5e-3c08-33b7-aec1-21f256a91ba6 | -6.12124 | -55.64064 | 2026-09-12 04:34:00 | NOAA-21 | ITAITUBA | PARÁ | Brasil | 1503606 | 15 | 33 | nan | nan | nan | Amazônia | 3.9 |
| ee5cf01e-4f73-3e49-b11c-543c8032f413 | -6.10507 | -55.64838 | 2026-09-12 04:34:00 | NOAA-21 | ITAITUBA | PARÁ | Brasil | 1503606 | 15 | 33 | nan | nan | nan | Amazônia | 2.7 |
| 8fe361a6-e3cd-3ea4-bb0d-b231013a60b6 | -6.2389 | -51.69224 | 2026-09-12 04:34:00 | NOAA-21 | SÃO FÉLIX DO XINGU | PARÁ | Brasil | 1507300 | 15 | 33 | nan | nan | nan | Amazônia | 3.2 |
| 0ba52d30-2141-39ab-a510-b592cde7f40b | -7.19313 | -45.92326 | 2026-09-12 04:34:00 | NOAA-21 | FORTALEZA DOS NOGUEIRAS | MARANHÃO | Brasil | 2104107 | 21 | 33 | nan | nan | nan | Cerrado | 2.5 |
| 011d9c3c-95a5-3cb9-97aa-78f616fab9df | -9.67735 | -45.99183 | 2026-09-12 04:34:00 | NOAA-21 | ALTO PARNAÍBA | MARANHÃO | Brasil | 2100501 | 21 | 33 | nan | nan | nan | Cerrado | 3.2 |
| e764dcc7-db8b-3b87-8128-ec36056b2a9e | -6.18255 | -57.71042 | 2026-09-12 04:34:00 | NOAA-21 | JACAREACANGA | PARÁ | Brasil | 1503754 | 15 | 33 | nan | nan | nan | Amazônia | 2.6 |
| fb022799-cb9c-350d-8925-058e2c75db12 | -6.60392 | -58.8442 | 2026-09-12 04:34:00 | NOAA-21 | MAUÉS | AMAZONAS | Brasil | 1302900 | 13 | 33 | nan | nan | nan | Amazônia | 2.3 |
| d84db88a-f760-3cc0-8bd6-542c053bcf3b | -8.31929 | -54.7662 | 2026-09-12 04:34:00 | NOAA-21 | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 2.0 |
| 3eb01d84-d1dc-3bc5-abff-471cf11f0ed4 | -7.60786 | -46.12369 | 2026-09-12 04:34:00 | NOAA-21 | BALSAS | MARANHÃO | Brasil | 2101400 | 21 | 33 | nan | nan | nan | Cerrado | 1.2 |
| 223b47b3-8007-3223-b630-1cb02c35387a | -12.13552 | -48.96883 | 2026-09-12 04:34:00 | NOAA-21 | FIGUEIRÓPOLIS | TOCANTINS | Brasil | 1707652 | 17 | 33 | nan | nan | nan | Cerrado | 4.3 |
| 25149606-be16-3755-bfc1-5b7ca237bd7b | -9.70606 | -54.34345 | 2026-09-12 04:34:00 | NOAA-21 | GUARANTÃ DO NORTE | MATO GROSSO | Brasil | 5104104 | 51 | 33 | nan | nan | nan | Amazônia | 2.7 |
| 3e447346-14b2-36b7-929c-cde91a9cdc63 | -11.28011 | -44.18562 | 2026-09-12 04:34:00 | NOAA-21 | MANSIDÃO | BAHIA | Brasil | 2920452 | 29 | 33 | nan | nan | nan | Cerrado | 2.0 |
| 1689a601-8c4d-34be-aefe-0c649c4ca887 | -11.80311 | -46.38888 | 2026-09-12 04:34:00 | NOAA-21 | PONTE ALTA DO BOM JESUS | TOCANTINS | Brasil | 1717800 | 17 | 33 | nan | nan | nan | Cerrado | 2.5 |
| fdcc1d5a-31fc-3fa3-93f0-a58cbebfc9de | -7.41707 | -46.15351 | 2026-09-12 04:34:00 | NOAA-21 | BALSAS | MARANHÃO | Brasil | 2101400 | 21 | 33 | nan | nan | nan | Cerrado | 3.4 |
| fde50371-fd20-30d4-8c32-3a13e971e5a7 | -6.87261 | -47.43156 | 2026-09-12 04:34:00 | NOAA-21 | ESTREITO | MARANHÃO | Brasil | 2104057 | 21 | 33 | nan | nan | nan | Cerrado | 0.8 |
| 8c90a482-f692-3193-82fa-36c014ac0967 | -6.19107 | -57.72665 | 2026-09-12 04:34:00 | NOAA-21 | JACAREACANGA | PARÁ | Brasil | 1503754 | 15 | 33 | nan | nan | nan | Amazônia | 5.0 |
| f5bb4db4-e82e-3211-9007-7e0d11a8e69b | -5.79603 | -53.82104 | 2026-09-12 04:34:00 | NOAA-21 | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 6.9 |
| f098a0da-fda8-3c77-98ad-fb3cf49bde8c | -10.28982 | -45.31711 | 2026-09-12 04:34:00 | NOAA-21 | CORRENTE | PIAUÍ | Brasil | 2202901 | 22 | 33 | nan | nan | nan | Cerrado | 1.1 |
| b83be431-3d7b-3fc4-80f7-dce88fe06c2a | -9.7024 | -43.45794 | 2026-09-12 04:34:00 | NOAA-21 | PILÃO ARCADO | BAHIA | Brasil | 2924405 | 29 | 33 | nan | nan | nan | Cerrado | 2.6 |
| bc643ae5-a1a7-39f8-9a5d-7141901f0615 | -6.067 | -53.49561 | 2026-09-12 04:34:00 | NOAA-21 | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 2.4 |
| e513dc7c-9479-33cd-8aa2-5158fdc75433 | -8.38086 | -47.54751 | 2026-09-12 04:34:00 | NOAA-21 | GOIATINS | TOCANTINS | Brasil | 1709005 | 17 | 33 | nan | nan | nan | Cerrado | 1.5 |
| 9eaa8a26-03c5-3c75-8843-c8c6d450e6c2 | -6.84403 | -46.71405 | 2026-09-12 04:34:00 | NOAA-21 | SÃO PEDRO DOS CRENTES | MARANHÃO | Brasil | 2111573 | 21 | 33 | nan | nan | nan | Cerrado | 1.7 |
| 2523c1dd-cad5-33c1-a5d4-5197d33ef719 | -6.3264 | -43.36022 | 2026-09-12 04:34:00 | NOAA-21 | SUCUPIRA DO RIACHÃO | MARANHÃO | Brasil | 2111953 | 21 | 33 | nan | nan | nan | Cerrado | 7.1 |
| 8e128f93-da44-39a8-b653-2fabf511be19 | -6.10557 | -57.63227 | 2026-09-12 04:34:00 | NOAA-21 | JACAREACANGA | PARÁ | Brasil | 1503754 | 15 | 33 | nan | nan | nan | Amazônia | 1.4 |
| 951d418e-a8c1-37b3-8c87-f9406d530762 | -6.28671 | -56.026 | 2026-09-12 04:34:00 | NOAA-21 | ITAITUBA | PARÁ | Brasil | 1503606 | 15 | 33 | nan | nan | nan | Amazônia | 3.9 |
| e4f94ca8-d845-3070-b10f-755c810c64ee | -9.37147 | -48.42046 | 2026-09-12 04:34:00 | NOAA-21 | MIRACEMA DO TOCANTINS | TOCANTINS | Brasil | 1713205 | 17 | 33 | nan | nan | nan | Cerrado | 0.6 |
| 4649c32b-9f20-3e13-9409-ee9e476519cd | -10.14403 | -36.19827 | 2026-09-12 04:34:00 | NOAA-21 | CORURIPE | ALAGOAS | Brasil | 2702306 | 27 | 33 | nan | nan | nan | Mata Atlântica | 3.2 |
| a6483b6e-c211-3225-8ccf-e66b6d2de815 | -7.60901 | -43.96222 | 2026-09-12 04:34:00 | NOAA-21 | BERTOLÍNIA | PIAUÍ | Brasil | 2201705 | 22 | 33 | nan | nan | nan | Cerrado | 3.5 |
| d35d56e2-26f7-3e12-a312-45d12c88a3db | -9.80644 | -48.92482 | 2026-09-12 04:34:00 | NOAA-21 | BARROLÂNDIA | TOCANTINS | Brasil | 1703107 | 17 | 33 | nan | nan | nan | Cerrado | 1.3 |
| 35b0ac2c-0fa7-3c63-81f6-af32bb450d7f | -9.68559 | -43.42887 | 2026-09-12 04:34:00 | NOAA-21 | PILÃO ARCADO | BAHIA | Brasil | 2924405 | 29 | 33 | nan | nan | nan | Caatinga | 1.1 |
| 481028ad-5c22-31c7-8618-568b8268f257 | -9.03581 | -49.81709 | 2026-09-12 04:34:00 | NOAA-21 | ARAGUACEMA | TOCANTINS | Brasil | 1701903 | 17 | 33 | nan | nan | nan | Cerrado | 0.9 |
| c48aeab8-d648-31a5-bfc5-dde4411193f2 | -6.88376 | -55.645 | 2026-09-12 04:34:00 | NOAA-21 | NOVO PROGRESSO | PARÁ | Brasil | 1505031 | 15 | 33 | nan | nan | nan | Amazônia | 1.5 |
| ea0cd09d-f40c-36e1-a7b1-8b21da31106c | -8.08038 | -54.86454 | 2026-09-12 04:34:00 | NOAA-21 | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 1.4 |
| 25a9c763-22c7-3b6f-bede-2e27bb9cb8c1 | -8.11145 | -54.78968 | 2026-09-12 04:34:00 | NOAA-21 | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 1.4 |
| ebd90a76-c5b8-391a-8214-0a83958e7b3e | -4.53769 | -54.96196 | 2026-09-12 04:34:00 | NOAA-21 | RURÓPOLIS | PARÁ | Brasil | 1506195 | 15 | 33 | nan | nan | nan | Amazônia | 1.5 |
| 5a8e8f68-5102-3190-adfb-9608965c5baa | -10.7127 | -46.0585 | 2026-09-12 04:34:00 | NOAA-21 | FORMOSA DO RIO PRETO | BAHIA | Brasil | 2911105 | 29 | 33 | nan | nan | nan | Cerrado | 0.7 |
| 193ed7e3-72f5-3645-823c-238a7a61c882 | -6.33135 | -55.85293 | 2026-09-12 04:34:00 | NOAA-21 | ITAITUBA | PARÁ | Brasil | 1503606 | 15 | 33 | nan | nan | nan | Amazônia | 3.6 |
| a9e18c2b-0aac-3083-8f51-ea0c8aaf8fb4 | -12.13221 | -48.9683 | 2026-09-12 04:34:00 | NOAA-21 | FIGUEIRÓPOLIS | TOCANTINS | Brasil | 1707652 | 17 | 33 | nan | nan | nan | Cerrado | 4.4 |
| 5b613156-f548-3653-9b48-54f467cde685 | -6.85823 | -47.43596 | 2026-09-12 04:34:00 | NOAA-21 | ESTREITO | MARANHÃO | Brasil | 2104057 | 21 | 33 | nan | nan | nan | Cerrado | 2.1 |
| 1c72af74-5a80-301f-80ab-5822fe8df6e7 | -6.10204 | -55.63723 | 2026-09-12 04:34:00 | NOAA-21 | ITAITUBA | PARÁ | Brasil | 1503606 | 15 | 33 | nan | nan | nan | Amazônia | 1.4 |
| f7baaeff-f9aa-3fa8-af96-2da2c8357bbd | -6.85455 | -55.75723 | 2026-09-12 04:34:00 | NOAA-21 | NOVO PROGRESSO | PARÁ | Brasil | 1505031 | 15 | 33 | nan | nan | nan | Amazônia | 1.8 |
| 98634a3a-602e-36d5-b170-6261c9a28ebd | -8.93703 | -44.40188 | 2026-09-12 04:34:00 | NOAA-21 | CURRAIS | PIAUÍ | Brasil | 2203230 | 22 | 33 | nan | nan | nan | Cerrado | 1.3 |
| 60f6d678-b919-3af8-872d-c418a12c245a | -8.82305 | -46.02345 | 2026-09-12 04:34:00 | NOAA-21 | ALTO PARNAÍBA | MARANHÃO | Brasil | 2100501 | 21 | 33 | nan | nan | nan | Cerrado | 2.2 |
| 550951a3-cf02-393f-aa56-5df96aea7e3a | -10.47624 | -51.3647 | 2026-09-12 04:34:00 | NOAA-21 | CONFRESA | MATO GROSSO | Brasil | 5103353 | 51 | 33 | nan | nan | nan | Amazônia | 2.2 |
| 9f1385d4-263b-36bb-ad9d-a681b872d0fb | -7.96595 | -43.99932 | 2026-09-12 04:34:00 | NOAA-21 | SEBASTIÃO LEAL | PIAUÍ | Brasil | 2210631 | 22 | 33 | nan | nan | nan | Cerrado | 7.0 |
| adf05da1-7a0b-3dcf-b2b1-90831c1e57d9 | -5.85022 | -52.00175 | 2026-09-12 04:34:00 | NOAA-21 | SÃO FÉLIX DO XINGU | PARÁ | Brasil | 1507300 | 15 | 33 | nan | nan | nan | Amazônia | 2.5 |
| 5d4bcea9-d037-338b-a2a8-bdd4fffcc7be | -10.69108 | -54.16577 | 2026-09-12 04:34:00 | NOAA-21 | MARCELÂNDIA | MATO GROSSO | Brasil | 5105580 | 51 | 33 | nan | nan | nan | Amazônia | 41.1 |
| a5e30b44-2b95-3469-81ec-f77a6490dab5 | -10.29084 | -49.99092 | 2026-09-12 04:34:00 | NOAA-21 | PIUM | TOCANTINS | Brasil | 1717503 | 17 | 33 | nan | nan | nan | Cerrado | 1.3 |
| 571e31b2-8a3f-322d-ac75-3ebc60b450d8 | -13.41407 | -42.48472 | 2026-09-12 04:34:00 | NOAA-21 | BOTUPORÃ | BAHIA | Brasil | 2904209 | 29 | 33 | nan | nan | nan | Caatinga | 2.4 |
| 666e9a50-8562-3fd4-8409-653476dba2bc | -6.11259 | -52.24676 | 2026-09-12 04:34:00 | NOAA-21 | SÃO FÉLIX DO XINGU | PARÁ | Brasil | 1507300 | 15 | 33 | nan | nan | nan | Amazônia | 1.8 |
| f52c3707-3479-3e95-9d6c-b9df52bacc5b | -4.86753 | -56.01498 | 2026-09-12 04:34:00 | NOAA-21 | TRAIRÃO | PARÁ | Brasil | 1508050 | 15 | 33 | nan | nan | nan | Amazônia | 0.4 |
| 8b425969-2e86-380c-af84-d9808fa10714 | -10.69511 | -54.1665 | 2026-09-12 04:34:00 | NOAA-21 | MARCELÂNDIA | MATO GROSSO | Brasil | 5105580 | 51 | 33 | nan | nan | nan | Amazônia | 41.1 |
| 56500245-ac4d-358f-ad6c-43f3fbe8c24b | -9.31507 | -45.64913 | 2026-09-12 04:34:00 | NOAA-21 | SANTA FILOMENA | PIAUÍ | Brasil | 2209203 | 22 | 33 | nan | nan | nan | Cerrado | 1.7 |
| bacd0763-d288-35b3-837d-d0324369900c | -6.8885 | -55.64586 | 2026-09-12 04:34:00 | NOAA-21 | NOVO PROGRESSO | PARÁ | Brasil | 1505031 | 15 | 33 | nan | nan | nan | Amazônia | 1.5 |
| 6e286057-3f4c-387a-9878-9db1c064d6eb | -4.8648 | -56.00053 | 2026-09-12 04:34:00 | NOAA-21 | TRAIRÃO | PARÁ | Brasil | 1508050 | 15 | 33 | nan | nan | nan | Amazônia | 1.4 |
| b95697b4-3d40-3f20-86c1-cc87b9360ff7 | -9.9069 | -46.22732 | 2026-09-12 04:34:00 | NOAA-21 | ALTO PARNAÍBA | MARANHÃO | Brasil | 2100501 | 21 | 33 | nan | nan | nan | Cerrado | 2.6 |
| c9ac1937-97eb-3c61-872e-c3a1a8cd19fa | -10.51502 | -57.4538 | 2026-09-12 04:34:00 | NOAA-21 | JUARA | MATO GROSSO | Brasil | 5105101 | 51 | 33 | nan | nan | nan | Amazônia | 0.6 |
| 87e7cc73-0718-3ead-bb0a-488ddeeb5999 | -10.45888 | -48.66483 | 2026-09-12 04:34:00 | NOAA-21 | PORTO NACIONAL | TOCANTINS | Brasil | 1718204 | 17 | 33 | nan | nan | nan | Cerrado | 1.5 |
| 1a74958e-215e-3cf2-b439-9330b41bb4eb | -6.34798 | -46.55015 | 2026-09-12 04:34:00 | NOAA-21 | SÍTIO NOVO | MARANHÃO | Brasil | 2111805 | 21 | 33 | nan | nan | nan | Cerrado | 2.0 |
| 2f310fcb-863f-30a9-9a55-da656eeef678 | -12.12342 | -48.98126 | 2026-09-12 04:34:00 | NOAA-21 | FIGUEIRÓPOLIS | TOCANTINS | Brasil | 1707652 | 17 | 33 | nan | nan | nan | Cerrado | 1.7 |
| ac752b8b-8512-3690-b110-ca753b6f15ec | -9.31863 | -45.64977 | 2026-09-12 04:34:00 | NOAA-21 | SANTA FILOMENA | PIAUÍ | Brasil | 2209203 | 22 | 33 | nan | nan | nan | Cerrado | 1.7 |
| 293fabfc-d589-38a0-aa10-72f707521af9 | -11.38991 | -43.95757 | 2026-09-12 04:34:00 | NOAA-21 | COTEGIPE | BAHIA | Brasil | 2909406 | 29 | 33 | nan | nan | nan | Cerrado | 2.4 |
| 3e86535d-1e44-387c-a57e-1bb5234c90e8 | -6.39486 | -53.18224 | 2026-09-12 04:34:00 | NOAA-21 | SÃO FÉLIX DO XINGU | PARÁ | Brasil | 1507300 | 15 | 33 | nan | nan | nan | Amazônia | 1.9 |
| 42df7b73-a5e1-396f-b2d2-d2e839098253 | -10.27744 | -45.32467 | 2026-09-12 04:34:00 | NOAA-21 | CORRENTE | PIAUÍ | Brasil | 2202901 | 22 | 33 | nan | nan | nan | Cerrado | 1.4 |
| 500f16dc-2714-378d-a8b9-7f5e1a0b71b1 | -4.87341 | -56.0108 | 2026-09-12 04:34:00 | NOAA-21 | TRAIRÃO | PARÁ | Brasil | 1508050 | 15 | 33 | nan | nan | nan | Amazônia | 0.5 |
| 3683cafa-7eea-3a5c-9467-3cb2b511cb17 | -9.37201 | -48.41697 | 2026-09-12 04:34:00 | NOAA-21 | MIRACEMA DO TOCANTINS | TOCANTINS | Brasil | 1713205 | 17 | 33 | nan | nan | nan | Cerrado | 1.6 |
| 94ec6e8d-8142-3dce-a945-7b17efa67e66 | -4.91673 | -55.81491 | 2026-09-12 04:34:00 | NOAA-21 | TRAIRÃO | PARÁ | Brasil | 1508050 | 15 | 33 | nan | nan | nan | Amazônia | 2.9 |
| c7e9fb94-4671-3955-9370-6e6c54630bae | -9.92994 | -48.50171 | 2026-09-12 04:34:00 | NOAA-21 | MIRACEMA DO TOCANTINS | TOCANTINS | Brasil | 1713205 | 17 | 33 | nan | nan | nan | Cerrado | 0.7 |
| 8dfa5019-873e-390c-8485-c115e026ad3d | -8.11585 | -54.79041 | 2026-09-12 04:34:00 | NOAA-21 | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 3.6 |
| dcad6ba5-f95f-3ea3-8d80-c8e1fd294ae8 | -10.55168 | -51.37236 | 2026-09-12 04:34:00 | NOAA-21 | CONFRESA | MATO GROSSO | Brasil | 5103353 | 51 | 33 | nan | nan | nan | Amazônia | 1.6 |
| 3439e938-7a56-3dfd-b631-1983f0bd69df | -10.22229 | -45.19164 | 2026-09-12 04:34:00 | NOAA-21 | CORRENTE | PIAUÍ | Brasil | 2202901 | 22 | 33 | nan | nan | nan | Cerrado | 1.5 |
| cbe1831b-61ce-3185-b56c-7209640f2655 | -4.87025 | -55.99891 | 2026-09-12 04:34:00 | NOAA-21 | TRAIRÃO | PARÁ | Brasil | 1508050 | 15 | 33 | nan | nan | nan | Amazônia | 1.8 |


[Clique aqui para ver as próximas entradas](README28.md)
