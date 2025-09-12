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

## Dados Diários - Página 33

| ID | Latitude | Longitude | Data/Hora GMT | Satélite | Município | Estado | País | Município ID | Estado ID | País ID | Dias sem Chuva | Precipitação | Risco de Fogo | Bioma | FRP |
|----|----------|-----------|---------------|----------|-----------|--------|------|--------------|-----------|---------|----------------|--------------|----------------|-------|-----|
| 33c28a89-b5d3-3c87-83df-acc0061d0e11 | -6.15121 | -42.60874 | 2025-09-12 04:04:00 | NPP-375D | JARDIM DO MULATO | PIAUÍ | Brasil | 2205250 | 22 | 33 | nan | nan | nan | Caatinga | 1.9 |
| cb449e5f-0a52-3e77-9e7b-ae4250a8c051 | -6.82407 | -45.64938 | 2025-09-12 04:04:00 | NPP-375D | SÃO RAIMUNDO DAS MANGABEIRAS | MARANHÃO | Brasil | 2111607 | 21 | 33 | nan | nan | nan | Cerrado | 2.1 |
| c84bcf96-a8c1-38ed-ba26-b27cf7a1fa24 | -6.21673 | -43.37558 | 2025-09-12 04:04:00 | NPP-375D | LAGOA DO MATO | MARANHÃO | Brasil | 2105922 | 21 | 33 | nan | nan | nan | Cerrado | 0.5 |
| 6d638c6e-90f4-3919-81aa-451f043bf00e | -7.46862 | -45.29752 | 2025-09-12 04:04:00 | NPP-375D | LORETO | MARANHÃO | Brasil | 2106102 | 21 | 33 | nan | nan | nan | Cerrado | 4.3 |
| 4f071f86-224f-35e5-aff6-786305922fac | -11.69205 | -46.51922 | 2025-09-12 04:04:00 | NPP-375D | NOVO JARDIM | TOCANTINS | Brasil | 1715259 | 17 | 33 | nan | nan | nan | Cerrado | 1.8 |
| 9d93a9b5-f530-3443-991f-cb46d6b26deb | -6.99609 | -44.78143 | 2025-09-12 04:04:00 | NPP-375D | SÃO FÉLIX DE BALSAS | MARANHÃO | Brasil | 2110807 | 21 | 33 | nan | nan | nan | Cerrado | 1.9 |
| 3c2c3ac4-f839-3ee6-b285-645e08dea0f3 | -10.20613 | -48.16034 | 2025-09-12 04:04:00 | NPP-375D | PALMAS | TOCANTINS | Brasil | 1721000 | 17 | 33 | nan | nan | nan | Cerrado | 1.3 |
| 62c9c5d5-238d-37b9-ad56-c2e9e89c8612 | -11.67426 | -46.57059 | 2025-09-12 04:04:00 | NPP-375D | NOVO JARDIM | TOCANTINS | Brasil | 1715259 | 17 | 33 | nan | nan | nan | Cerrado | 10.1 |
| a321135f-5f95-3e08-bc00-f372f983990a | -6.34244 | -43.03986 | 2025-09-12 04:04:00 | NPP-375D | SÃO FRANCISCO DO MARANHÃO | MARANHÃO | Brasil | 2110906 | 21 | 33 | nan | nan | nan | Cerrado | 1.5 |
| 19c21ba3-944d-3624-a97b-384b019bde29 | -11.67233 | -46.57116 | 2025-09-12 04:04:00 | NPP-375D | NOVO JARDIM | TOCANTINS | Brasil | 1715259 | 17 | 33 | nan | nan | nan | Cerrado | 5.5 |
| c1dde504-6a77-3740-96d8-0bfb32fdbd64 | -6.67855 | -44.14069 | 2025-09-12 04:04:00 | NPP-375D | PASTOS BONS | MARANHÃO | Brasil | 2108009 | 21 | 33 | nan | nan | nan | Cerrado | 2.5 |
| 06b9aaab-2a58-3823-8ca5-df8c9665e1e9 | -12.12187 | -44.8494 | 2025-09-12 04:04:00 | NPP-375D | BARREIRAS | BAHIA | Brasil | 2903201 | 29 | 33 | nan | nan | nan | Cerrado | 2.5 |
| ca99b818-fb6f-3e9c-b2f9-e5c28aa4f1e5 | -9.99075 | -51.71821 | 2025-09-12 04:04:00 | NPP-375D | VILA RICA | MATO GROSSO | Brasil | 5108600 | 51 | 33 | nan | nan | nan | Amazônia | 1.9 |
| 92c7e273-ae0e-30ab-9bed-777c2a31614d | -10.68434 | -48.66161 | 2025-09-12 04:04:00 | NPP-375D | PORTO NACIONAL | TOCANTINS | Brasil | 1718204 | 17 | 33 | nan | nan | nan | Cerrado | 3.5 |
| 9eb3a011-e922-37c6-a50b-60effbeab47d | -11.68794 | -46.51843 | 2025-09-12 04:04:00 | NPP-375D | NOVO JARDIM | TOCANTINS | Brasil | 1715259 | 17 | 33 | nan | nan | nan | Cerrado | 1.8 |
| 6a6116af-372c-3988-9f9c-5a75763f63cb | -10.67467 | -48.65988 | 2025-09-12 04:04:00 | NPP-375D | PORTO NACIONAL | TOCANTINS | Brasil | 1718204 | 17 | 33 | nan | nan | nan | Cerrado | 4.3 |
| 47eeb12c-08ac-3911-81ee-de8ff5f7bde1 | -8.94812 | -46.09364 | 2025-09-12 04:04:00 | NPP-375D | ALTO PARNAÍBA | MARANHÃO | Brasil | 2100501 | 21 | 33 | nan | nan | nan | Cerrado | 0.9 |
| 11e5d621-e157-3328-b0f4-3ecc20019c8a | -7.24424 | -44.47687 | 2025-09-12 04:04:00 | NPP-375D | URUÇUÍ | PIAUÍ | Brasil | 2211209 | 22 | 33 | nan | nan | nan | Cerrado | 1.7 |
| 7ac700af-289c-384d-8c69-2afa0c53cf80 | -9.04567 | -47.04612 | 2025-09-12 04:04:00 | NPP-375D | BALSAS | MARANHÃO | Brasil | 2101400 | 21 | 33 | nan | nan | nan | Cerrado | 2.9 |
| 0047f438-95e2-3383-a6e1-8d856deb5f8a | -10.67089 | -48.5997 | 2025-09-12 04:04:00 | NPP-375D | PORTO NACIONAL | TOCANTINS | Brasil | 1718204 | 17 | 33 | nan | nan | nan | Cerrado | 4.8 |
| bf87692c-f058-3952-9085-f51b86459b15 | -10.71025 | -48.62925 | 2025-09-12 04:04:00 | NPP-375D | PORTO NACIONAL | TOCANTINS | Brasil | 1718204 | 17 | 33 | nan | nan | nan | Cerrado | 5.8 |
| 7d664381-d90d-318d-99f3-fa807afae767 | -9.07724 | -50.5017 | 2025-09-12 04:04:00 | NPP-375D | SANTANA DO ARAGUAIA | PARÁ | Brasil | 1506708 | 15 | 33 | nan | nan | nan | Amazônia | 1.9 |
| 299a004d-49da-3f01-b1ab-a0d237ba1cd5 | -6.24771 | -44.79848 | 2025-09-12 04:04:00 | NPP-375D | MIRADOR | MARANHÃO | Brasil | 2106706 | 21 | 33 | nan | nan | nan | Cerrado | 1.6 |
| db355a11-c953-3232-a8f0-b1557d9e152c | -8.07837 | -42.5621 | 2025-09-12 04:04:00 | NPP-375D | RIBEIRA DO PIAUÍ | PIAUÍ | Brasil | 2208874 | 22 | 33 | nan | nan | nan | Caatinga | 3.0 |
| a776e15a-1969-35e5-89ae-d547376097c4 | -3.68922 | -49.10666 | 2025-09-12 04:04:00 | NPP-375D | GOIANÉSIA DO PARÁ | PARÁ | Brasil | 1503093 | 15 | 33 | nan | nan | nan | Amazônia | 1.5 |
| 2249f423-110d-3f7d-9e1e-8f30f2122ee8 | -8.18688 | -46.10055 | 2025-09-12 04:04:00 | NPP-375D | TASSO FRAGOSO | MARANHÃO | Brasil | 2112001 | 21 | 33 | nan | nan | nan | Cerrado | 2.9 |
| 19f90f73-3ca0-36dd-9a87-f3db231267d2 | -5.96933 | -44.72311 | 2025-09-12 04:04:00 | NPP-375D | TUNTUM | MARANHÃO | Brasil | 2112308 | 21 | 33 | nan | nan | nan | Cerrado | 2.9 |
| bcee4573-f3dd-3c90-bd34-6c8bb0a90080 | -8.94426 | -46.11647 | 2025-09-12 04:04:00 | NPP-375D | ALTO PARNAÍBA | MARANHÃO | Brasil | 2100501 | 21 | 33 | nan | nan | nan | Cerrado | 0.9 |
| 47403021-0ec9-31b4-b734-64eb8fcf1a8c | -6.26756 | -42.42225 | 2025-09-12 04:04:00 | NPP-375D | REGENERAÇÃO | PIAUÍ | Brasil | 2208809 | 22 | 33 | nan | nan | nan | Caatinga | 1.1 |
| 6ed3f25c-9085-3f9e-9b9b-5ac01539c44d | -9.99498 | -51.72824 | 2025-09-12 04:04:00 | NPP-375D | VILA RICA | MATO GROSSO | Brasil | 5108600 | 51 | 33 | nan | nan | nan | Amazônia | 4.9 |
| c68775f1-1b86-36e4-abbb-18d9091a3181 | -11.67711 | -46.60216 | 2025-09-12 04:04:00 | NPP-375D | NOVO JARDIM | TOCANTINS | Brasil | 1715259 | 17 | 33 | nan | nan | nan | Cerrado | 3.6 |
| 4c648207-9644-3489-9ee5-3e72584dd226 | -9.68399 | -47.52486 | 2025-09-12 04:04:00 | NPP-375D | RIO SONO | TOCANTINS | Brasil | 1718758 | 17 | 33 | nan | nan | nan | Cerrado | 1.6 |
| ad282a60-3855-3ab4-b731-f0942136f8e0 | -11.14317 | -45.23929 | 2025-09-12 04:04:00 | NPP-375D | FORMOSA DO RIO PRETO | BAHIA | Brasil | 2911105 | 29 | 33 | nan | nan | nan | Cerrado | 3.2 |
| 836975ef-6c1f-30e9-9a4e-f3af30d57ca8 | -8.18581 | -46.09892 | 2025-09-12 04:04:00 | NPP-375D | TASSO FRAGOSO | MARANHÃO | Brasil | 2112001 | 21 | 33 | nan | nan | nan | Cerrado | 2.7 |
| 23985864-f155-35af-8a61-71be0d877eeb | -6.44719 | -41.76463 | 2025-09-12 04:04:00 | NPP-375D | VALENÇA DO PIAUÍ | PIAUÍ | Brasil | 2211308 | 22 | 33 | nan | nan | nan | Caatinga | 1.6 |
| 794ba7a9-899c-39ea-98e1-193f244e1bcb | -6.1813 | -42.74945 | 2025-09-12 04:04:00 | NPP-375D | AMARANTE | PIAUÍ | Brasil | 2200509 | 22 | 33 | nan | nan | nan | Caatinga | 2.2 |
| 41c260c6-5133-3df2-a453-b497983f2c32 | -9.8338 | -47.76977 | 2025-09-12 04:04:00 | NPP-375D | RIO SONO | TOCANTINS | Brasil | 1718758 | 17 | 33 | nan | nan | nan | Cerrado | 1.0 |
| 44eb9a48-4e3e-3443-a09f-cc4d450771cf | -10.43678 | -50.61162 | 2025-09-12 04:04:00 | NPP-375D | SANTA TEREZINHA | MATO GROSSO | Brasil | 5107776 | 51 | 33 | nan | nan | nan | Cerrado | 2.0 |
| bf604036-c42b-3963-bfb9-5e430d98e305 | -11.67562 | -46.55221 | 2025-09-12 04:04:00 | NPP-375D | NOVO JARDIM | TOCANTINS | Brasil | 1715259 | 17 | 33 | nan | nan | nan | Cerrado | 2.5 |
| 96e309f6-4210-338b-8fd8-ad4925bc47cf | -5.49235 | -42.15372 | 2025-09-12 04:04:00 | NPP-375D | ALTO LONGÁ | PIAUÍ | Brasil | 2200301 | 22 | 33 | nan | nan | nan | Caatinga | 0.6 |
| 13258ae6-4e98-3481-80bf-2f12573b206e | -6.21718 | -44.53442 | 2025-09-12 04:04:00 | NPP-375D | MIRADOR | MARANHÃO | Brasil | 2106706 | 21 | 33 | nan | nan | nan | Cerrado | 1.6 |
| 47d7e069-6f60-35e3-ae0d-a1a658764fd9 | -6.30897 | -43.42474 | 2025-09-12 04:04:00 | NPP-375D | SUCUPIRA DO RIACHÃO | MARANHÃO | Brasil | 2111953 | 21 | 33 | nan | nan | nan | Cerrado | 1.1 |
| d45528f3-d9d5-3d2b-8d39-b577b83012f9 | -6.4222 | -44.50586 | 2025-09-12 04:04:00 | NPP-375D | MIRADOR | MARANHÃO | Brasil | 2106706 | 21 | 33 | nan | nan | nan | Cerrado | 4.8 |
| 90c5136c-b649-33dd-9b0c-8f1cbc56ab8b | -9.05728 | -45.71431 | 2025-09-12 04:04:00 | NPP-375D | SANTA FILOMENA | PIAUÍ | Brasil | 2209203 | 22 | 33 | nan | nan | nan | Cerrado | 2.3 |
| 31b0c78f-bf8f-366f-8586-e4c5a700c589 | -10.09134 | -48.17537 | 2025-09-12 04:04:00 | NPP-375D | PALMAS | TOCANTINS | Brasil | 1721000 | 17 | 33 | nan | nan | nan | Cerrado | 3.6 |
| cacd0460-59e8-3d66-bb45-b0a871797f41 | -7.40494 | -50.6476 | 2025-09-12 04:04:00 | NPP-375D | BANNACH | PARÁ | Brasil | 1501253 | 15 | 33 | nan | nan | nan | Amazônia | 1.3 |
| 62c52a86-47c0-3c30-b46b-70717e1a90ca | -10.53084 | -51.51802 | 2025-09-12 04:04:00 | NPP-375D | CONFRESA | MATO GROSSO | Brasil | 5103353 | 51 | 33 | nan | nan | nan | Amazônia | 5.1 |
| de939db3-8ab1-33b4-b7aa-2eb52bb1c5f2 | -10.56191 | -51.48836 | 2025-09-12 04:04:00 | NPP-375D | CONFRESA | MATO GROSSO | Brasil | 5103353 | 51 | 33 | nan | nan | nan | Amazônia | 2.4 |
| 0e68fcff-02f6-30d8-adf0-d780d17fa0dc | -6.9992 | -44.78708 | 2025-09-12 04:04:00 | NPP-375D | SÃO FÉLIX DE BALSAS | MARANHÃO | Brasil | 2110807 | 21 | 33 | nan | nan | nan | Cerrado | 1.9 |
| da968b82-8240-3116-9440-c5bbc0a36264 | -10.89056 | -45.58838 | 2025-09-12 04:04:00 | NPP-375D | FORMOSA DO RIO PRETO | BAHIA | Brasil | 2911105 | 29 | 33 | nan | nan | nan | Cerrado | 3.0 |
| 9ea48d91-7015-3910-a376-17f3be236901 | -6.12429 | -42.96019 | 2025-09-12 04:04:00 | NPP-375D | PALMEIRAIS | PIAUÍ | Brasil | 2207504 | 22 | 33 | nan | nan | nan | Caatinga | 1.6 |
| f5ec02d3-e522-3547-8b26-c85c223da41b | -9.81147 | -47.81521 | 2025-09-12 04:04:00 | NPP-375D | RIO SONO | TOCANTINS | Brasil | 1718758 | 17 | 33 | nan | nan | nan | Cerrado | 0.7 |
| 158b9ad6-9b1e-344f-b23e-7a06d7b51e73 | -10.357 | -50.52665 | 2025-09-12 04:04:00 | NPP-375D | SANTA TEREZINHA | MATO GROSSO | Brasil | 5107776 | 51 | 33 | nan | nan | nan | Amazônia | 3.4 |
| 705d33ee-f7d3-30ef-93d9-31a9b55902f4 | -6.99424 | -44.77922 | 2025-09-12 04:04:00 | NPP-375D | SÃO FÉLIX DE BALSAS | MARANHÃO | Brasil | 2110807 | 21 | 33 | nan | nan | nan | Cerrado | 1.4 |
| f5b4e39a-c79f-3e91-8139-789983d99311 | -10.85517 | -48.16168 | 2025-09-12 04:04:00 | NPP-375D | MONTE DO CARMO | TOCANTINS | Brasil | 1713601 | 17 | 33 | nan | nan | nan | Cerrado | 1.8 |
| 75acfc40-6cd1-34b1-b2fb-b894d07f55af | -10.87589 | -45.56401 | 2025-09-12 04:04:00 | NPP-375D | FORMOSA DO RIO PRETO | BAHIA | Brasil | 2911105 | 29 | 33 | nan | nan | nan | Cerrado | 3.9 |
| eb6aaa60-b690-3469-ae31-0e97aa361075 | -11.14668 | -45.31702 | 2025-09-12 04:04:00 | NPP-375D | FORMOSA DO RIO PRETO | BAHIA | Brasil | 2911105 | 29 | 33 | nan | nan | nan | Cerrado | 3.8 |
| 78eed0f0-d64d-3063-9c37-da7dc6b83d53 | -6.44962 | -44.07365 | 2025-09-12 04:04:00 | NPP-375D | PASTOS BONS | MARANHÃO | Brasil | 2108009 | 21 | 33 | nan | nan | nan | Cerrado | 2.7 |
| c1b11630-4be0-39e2-8cca-aa7e6c7dbff5 | -11.73858 | -43.37685 | 2025-09-12 04:04:00 | NPP-375D | MUQUÉM DO SÃO FRANCISCO | BAHIA | Brasil | 2922250 | 29 | 33 | nan | nan | nan | Cerrado | 0.7 |
| cd648b5c-0639-3c0a-b851-bfbccb41b3ed | -7.41158 | -50.64426 | 2025-09-12 04:04:00 | NPP-375D | BANNACH | PARÁ | Brasil | 1501253 | 15 | 33 | nan | nan | nan | Amazônia | 2.0 |
| 306859cc-cd46-3a9b-8a74-1a0286146116 | -7.8638 | -44.84119 | 2025-09-12 04:04:00 | NPP-375D | URUÇUÍ | PIAUÍ | Brasil | 2211209 | 22 | 33 | nan | nan | nan | Cerrado | 1.2 |
| a48482c6-bbc0-3d63-bd3a-9967d15b453d | -6.24711 | -44.80197 | 2025-09-12 04:04:00 | NPP-375D | MIRADOR | MARANHÃO | Brasil | 2106706 | 21 | 33 | nan | nan | nan | Cerrado | 2.5 |
| e86b138c-5e37-3bd1-b3ad-92c02720346c | -10.53099 | -51.52395 | 2025-09-12 04:04:00 | NPP-375D | CONFRESA | MATO GROSSO | Brasil | 5103353 | 51 | 33 | nan | nan | nan | Amazônia | 4.6 |
| 01766132-6f79-3f95-adb0-6cc7497433e2 | -10.6775 | -48.64461 | 2025-09-12 04:04:00 | NPP-375D | PORTO NACIONAL | TOCANTINS | Brasil | 1718204 | 17 | 33 | nan | nan | nan | Cerrado | 3.2 |
| 407a7591-8f3e-3be8-9e70-4495cc21af79 | -4.94682 | -49.92396 | 2025-09-12 04:04:00 | NPP-375D | ITUPIRANGA | PARÁ | Brasil | 1503705 | 15 | 33 | nan | nan | nan | Amazônia | 1.0 |
| b63f4777-2395-3867-ac59-4c848f3dfad0 | -6.54889 | -42.44588 | 2025-09-12 04:04:00 | NPP-375D | ARRAIAL | PIAUÍ | Brasil | 2201002 | 22 | 33 | nan | nan | nan | Caatinga | 2.6 |
| 4b6364f1-45b0-33c6-9a63-4559967baebc | -6.47953 | -45.15159 | 2025-09-12 04:04:00 | NPP-375D | MIRADOR | MARANHÃO | Brasil | 2106706 | 21 | 33 | nan | nan | nan | Cerrado | 3.6 |
| 6e07bbbb-8c42-301c-b84e-2c74eb307ab2 | -8.94468 | -46.72276 | 2025-09-12 04:04:00 | NPP-375D | BALSAS | MARANHÃO | Brasil | 2101400 | 21 | 33 | nan | nan | nan | Cerrado | 4.0 |
| ba09b50f-6437-3a23-a023-5ca6e62c3927 | -6.8862 | -42.83707 | 2025-09-12 04:04:00 | NPP-375D | FLORIANO | PIAUÍ | Brasil | 2203909 | 22 | 33 | nan | nan | nan | Caatinga | 1.6 |
| 16923648-3d30-3cd6-89f5-4f82fc637228 | -6.09604 | -45.94066 | 2025-09-12 04:04:00 | NPP-375D | GRAJAÚ | MARANHÃO | Brasil | 2104800 | 21 | 33 | nan | nan | nan | Cerrado | 0.7 |
| 7abae3de-ff50-3432-9167-be907812e1e8 | -8.42447 | -47.26625 | 2025-09-12 04:04:00 | NPP-375D | GOIATINS | TOCANTINS | Brasil | 1709005 | 17 | 33 | nan | nan | nan | Cerrado | 2.6 |
| d183f74a-671a-3828-a891-88583f66503a | -10.53996 | -51.5332 | 2025-09-12 04:04:00 | NPP-375D | CONFRESA | MATO GROSSO | Brasil | 5103353 | 51 | 33 | nan | nan | nan | Amazônia | 4.5 |
| eb13a982-4146-306b-b577-e346b8f0bd7f | -7.79093 | -50.78081 | 2025-09-12 04:04:00 | NPP-375D | CUMARU DO NORTE | PARÁ | Brasil | 1502764 | 15 | 33 | nan | nan | nan | Amazônia | 3.7 |
| e35e657b-d8a9-3f16-8a39-8f8008da8936 | -6.48925 | -43.87939 | 2025-09-12 04:04:00 | NPP-375D | PARAIBANO | MARANHÃO | Brasil | 2107704 | 21 | 33 | nan | nan | nan | Cerrado | 4.6 |
| 2a8a7bac-3d8d-3c85-b12b-5c353fd9909e | -10.08125 | -50.39679 | 2025-09-12 04:04:00 | NPP-375D | SANTA TEREZINHA | MATO GROSSO | Brasil | 5107776 | 51 | 33 | nan | nan | nan | Amazônia | 3.4 |
| b83837e1-9ede-354e-9ba2-b9c527cd16af | -9.04399 | -47.05564 | 2025-09-12 04:04:00 | NPP-375D | LIZARDA | TOCANTINS | Brasil | 1712405 | 17 | 33 | nan | nan | nan | Cerrado | 3.5 |
| ed8f0392-826f-3d39-8b53-5952450175ea | -9.11759 | -46.96479 | 2025-09-12 04:04:00 | NPP-375D | LIZARDA | TOCANTINS | Brasil | 1712405 | 17 | 33 | nan | nan | nan | Cerrado | 1.8 |
| e099cff4-f424-37a3-8584-934d379a5220 | -6.19465 | -42.66827 | 2025-09-12 04:04:00 | NPP-375D | REGENERAÇÃO | PIAUÍ | Brasil | 2208809 | 22 | 33 | nan | nan | nan | Caatinga | 3.0 |
| 68efb204-23ea-3ff3-bb88-30370041ea6d | -9.44919 | -46.41877 | 2025-09-12 04:04:00 | NPP-375D | ALTO PARNAÍBA | MARANHÃO | Brasil | 2100501 | 21 | 33 | nan | nan | nan | Cerrado | 2.7 |
| 63d93a75-af12-318f-867c-c888a6cdb79e | -9.07652 | -50.5056 | 2025-09-12 04:04:00 | NPP-375D | SANTANA DO ARAGUAIA | PARÁ | Brasil | 1506708 | 15 | 33 | nan | nan | nan | Amazônia | 1.9 |
| 50df5758-9c16-3936-b477-c2afdf22d452 | -11.19933 | -37.23129 | 2025-09-12 04:04:00 | NPP-375D | ITAPORANGA D'AJUDA | SERGIPE | Brasil | 2803203 | 28 | 33 | nan | nan | nan | Mata Atlântica | 1.8 |
| a80e57ee-2a22-324c-aa06-7ff608adac30 | -7.84634 | -44.80555 | 2025-09-12 04:04:00 | NPP-375D | URUÇUÍ | PIAUÍ | Brasil | 2211209 | 22 | 33 | nan | nan | nan | Cerrado | 2.5 |
| 9bd4eb1b-bb68-3695-af86-88106a4ce560 | -11.67156 | -46.6092 | 2025-09-12 04:04:00 | NPP-375D | NOVO JARDIM | TOCANTINS | Brasil | 1715259 | 17 | 33 | nan | nan | nan | Cerrado | 9.4 |
| c2ee5b9e-7494-35de-b677-bf3c89f517d3 | -6.97072 | -44.82248 | 2025-09-12 04:04:00 | NPP-375D | SÃO FÉLIX DE BALSAS | MARANHÃO | Brasil | 2110807 | 21 | 33 | nan | nan | nan | Cerrado | 3.3 |
| c44e888d-9ec5-3173-b494-76f822477268 | -10.35769 | -50.52303 | 2025-09-12 04:04:00 | NPP-375D | SANTA TEREZINHA | MATO GROSSO | Brasil | 5107776 | 51 | 33 | nan | nan | nan | Amazônia | 1.8 |
| 14c92eb9-0460-3aba-987b-e4533e255920 | -6.28904 | -42.40122 | 2025-09-12 04:04:00 | NPP-375D | REGENERAÇÃO | PIAUÍ | Brasil | 2208809 | 22 | 33 | nan | nan | nan | Caatinga | 1.6 |
| 3e68fde5-82d6-3900-a8a3-70721d83f07d | -11.14839 | -45.30728 | 2025-09-12 04:04:00 | NPP-375D | FORMOSA DO RIO PRETO | BAHIA | Brasil | 2911105 | 29 | 33 | nan | nan | nan | Cerrado | 2.9 |
| dfdc64f5-ed3e-3020-b7f7-a5884506d7e9 | -4.48039 | -48.11584 | 2025-09-12 04:04:00 | NPP-375D | RONDON DO PARÁ | PARÁ | Brasil | 1506187 | 15 | 33 | nan | nan | nan | Amazônia | 6.9 |
| c0f18382-ce03-3410-87d6-97865ee5ef7d | -11.24001 | -49.40693 | 2025-09-12 04:04:00 | NPP-375D | DUERÉ | TOCANTINS | Brasil | 1707306 | 17 | 33 | nan | nan | nan | Cerrado | 1.7 |
| 6ae53480-9f98-389f-8985-fa6bc057804b | -8.89148 | -49.94355 | 2025-09-12 04:04:00 | NPP-375D | SANTA MARIA DAS BARREIRAS | PARÁ | Brasil | 1506583 | 15 | 33 | nan | nan | nan | Amazônia | 4.3 |
| 062694a6-2dfd-3975-a7fc-fb9b2eebf5e8 | -11.67777 | -46.62222 | 2025-09-12 04:04:00 | NPP-375D | NOVO JARDIM | TOCANTINS | Brasil | 1715259 | 17 | 33 | nan | nan | nan | Cerrado | 1.5 |
| 493741d2-6cdf-336e-9516-5d810d6094f8 | -8.08121 | -42.56659 | 2025-09-12 04:04:00 | NPP-375D | RIBEIRA DO PIAUÍ | PIAUÍ | Brasil | 2208874 | 22 | 33 | nan | nan | nan | Caatinga | 3.0 |
| bcc7ccaa-64c0-3740-829d-df61b4011ad5 | -10.12817 | -47.92337 | 2025-09-12 04:04:00 | NPP-375D | APARECIDA DO RIO NEGRO | TOCANTINS | Brasil | 1701101 | 17 | 33 | nan | nan | nan | Cerrado | 3.0 |
| 9f8a1141-5b8e-322b-9b26-b70c876af1c6 | -9.51875 | -54.64357 | 2025-09-12 04:04:00 | NPP-375D | NOVO PROGRESSO | PARÁ | Brasil | 1505031 | 15 | 33 | nan | nan | nan | Amazônia | 5.5 |
| 5ea111bf-34ac-3536-974b-5f3c3dbc08fd | -8.08469 | -42.56723 | 2025-09-12 04:04:00 | NPP-375D | RIBEIRA DO PIAUÍ | PIAUÍ | Brasil | 2208874 | 22 | 33 | nan | nan | nan | Caatinga | 2.8 |
| 9416e77f-454c-3017-af17-ee4e69312cc7 | -6.28197 | -42.40024 | 2025-09-12 04:04:00 | NPP-375D | REGENERAÇÃO | PIAUÍ | Brasil | 2208809 | 22 | 33 | nan | nan | nan | Caatinga | 1.7 |
| f84387e0-6808-3db5-ae9b-c3d1afea3006 | -11.93837 | -44.30512 | 2025-09-12 04:04:00 | NPP-375D | COTEGIPE | BAHIA | Brasil | 2909406 | 29 | 33 | nan | nan | nan | Cerrado | 3.5 |
| f116e79e-6e9a-3e4b-962e-a7303baafaf7 | -9.66987 | -47.55356 | 2025-09-12 04:04:00 | NPP-375D | RIO SONO | TOCANTINS | Brasil | 1718758 | 17 | 33 | nan | nan | nan | Cerrado | 2.0 |
| f7cf697b-912b-38e4-ab61-cdda2ab73441 | -9.66448 | -47.55458 | 2025-09-12 04:04:00 | NPP-375D | RIO SONO | TOCANTINS | Brasil | 1718758 | 17 | 33 | nan | nan | nan | Cerrado | 1.4 |
| 90701968-7ea7-3b51-9a90-e45da164acbe | -10.53829 | -51.5174 | 2025-09-12 04:04:00 | NPP-375D | CONFRESA | MATO GROSSO | Brasil | 5103353 | 51 | 33 | nan | nan | nan | Amazônia | 2.4 |


[Clique aqui para ver as próximas entradas](README34.md)
