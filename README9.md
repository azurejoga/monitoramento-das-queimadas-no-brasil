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

## Dados Diários - Página 9

| ID | Latitude | Longitude | Data/Hora GMT | Satélite | Município | Estado | País | Município ID | Estado ID | País ID | Dias sem Chuva | Precipitação | Risco de Fogo | Bioma | FRP |
|----|----------|-----------|---------------|----------|-----------|--------|------|--------------|-----------|---------|----------------|--------------|----------------|-------|-----|
| cbbdf55e-ebd3-300c-ab6e-90f8f16225ff | -11.18725 | -54.86251 | 2026-08-04 04:19:00 | NOAA-20 | NOVA SANTA HELENA | MATO GROSSO | Brasil | 5106190 | 51 | 33 | nan | nan | nan | Amazônia | 2.8 |
| ff4efafd-c6a2-3f24-b8ca-f6b346b1d50a | -6.53891 | -55.17054 | 2026-08-04 04:19:00 | NOAA-20 | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 5.5 |
| 15d926a6-66c6-3624-9f9a-2b70d68bfaa4 | -7.99713 | -47.30167 | 2026-08-04 04:19:00 | NOAA-20 | GOIATINS | TOCANTINS | Brasil | 1709005 | 17 | 33 | nan | nan | nan | Cerrado | 0.9 |
| e55904df-1be1-3bae-80b0-29ea3d0e5fa1 | -7.54086 | -45.03264 | 2026-08-04 04:19:00 | NOAA-20 | RIBEIRO GONÇALVES | PIAUÍ | Brasil | 2208908 | 22 | 33 | nan | nan | nan | Cerrado | 3.3 |
| 21c0a6d0-4539-3e92-a633-3fe44d437eff | -10.63803 | -46.76864 | 2026-08-04 04:19:00 | NOAA-20 | MATEIROS | TOCANTINS | Brasil | 1712702 | 17 | 33 | nan | nan | nan | Cerrado | 1.6 |
| 1b486382-9aed-37d5-a3ee-2ac9f410c955 | -12.44378 | -44.31827 | 2026-08-04 04:19:00 | NOAA-20 | TABOCAS DO BREJO VELHO | BAHIA | Brasil | 2930907 | 29 | 33 | nan | nan | nan | Cerrado | 0.6 |
| 0f7028c9-0e12-3f95-8675-c5a62f858900 | -12.17876 | -45.04756 | 2026-08-04 04:19:00 | NOAA-20 | BARREIRAS | BAHIA | Brasil | 2903201 | 29 | 33 | nan | nan | nan | Cerrado | 0.2 |
| c5bf6b6e-8a49-3a40-aa65-d0ffc904652f | -10.82713 | -48.4828 | 2026-08-04 04:19:00 | NOAA-20 | BREJINHO DE NAZARÉ | TOCANTINS | Brasil | 1703701 | 17 | 33 | nan | nan | nan | Cerrado | 1.6 |
| 85b276fc-3355-3ecf-9b0d-866ae21ab51b | -7.37849 | -45.05558 | 2026-08-04 04:19:00 | NOAA-20 | LORETO | MARANHÃO | Brasil | 2106102 | 21 | 33 | nan | nan | nan | Cerrado | 4.0 |
| 3ea34d9b-f783-3ce8-a464-445df422daa9 | -11.22311 | -54.86137 | 2026-08-04 04:19:00 | NOAA-20 | NOVA SANTA HELENA | MATO GROSSO | Brasil | 5106190 | 51 | 33 | nan | nan | nan | Amazônia | 13.7 |
| e249064d-1b79-3c8c-b548-ac48b764502c | -3.02625 | -39.97231 | 2026-08-04 04:19:00 | NOAA-20 | ITAREMA | CEARÁ | Brasil | 2306553 | 23 | 33 | nan | nan | nan | Caatinga | 2.2 |
| 8d42103e-c470-3625-8117-a53c8d9a1c1b | -11.21819 | -54.85609 | 2026-08-04 04:19:00 | NOAA-20 | NOVA SANTA HELENA | MATO GROSSO | Brasil | 5106190 | 51 | 33 | nan | nan | nan | Amazônia | 3.0 |
| 5de54700-f85e-387e-894d-287a4270d367 | -9.11772 | -48.37524 | 2026-08-04 04:19:00 | NOAA-20 | RIO DOS BOIS | TOCANTINS | Brasil | 1718709 | 17 | 33 | nan | nan | nan | Cerrado | 2.0 |
| 2d910f91-2430-3053-831c-4ec1763913af | -7.91157 | -44.93014 | 2026-08-04 04:19:00 | NOAA-20 | BAIXA GRANDE DO RIBEIRO | PIAUÍ | Brasil | 2201150 | 22 | 33 | nan | nan | nan | Cerrado | 1.9 |
| 97276cfe-89c9-3d63-8c43-3237800d80d3 | -7.51479 | -46.9998 | 2026-08-04 04:19:00 | NOAA-20 | RIACHÃO | MARANHÃO | Brasil | 2109502 | 21 | 33 | nan | nan | nan | Cerrado | 0.8 |
| e1db17b7-a162-38a7-ad0a-60575868a459 | -6.54523 | -55.17166 | 2026-08-04 04:19:00 | NOAA-20 | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 3.1 |
| d664ed02-c6d4-3514-91f7-f34b7dcaeae3 | -7.56794 | -46.00949 | 2026-08-04 04:19:00 | NOAA-20 | BALSAS | MARANHÃO | Brasil | 2101400 | 21 | 33 | nan | nan | nan | Cerrado | 0.8 |
| 5dfc485a-d4d6-3f53-ad03-fde6041d9698 | -11.22433 | -54.86018 | 2026-08-04 04:19:00 | NOAA-20 | NOVA SANTA HELENA | MATO GROSSO | Brasil | 5106190 | 51 | 33 | nan | nan | nan | Amazônia | 8.5 |
| 28344c14-af85-30d7-b3db-5b6bafa6b7ca | -8.27441 | -47.54888 | 2026-08-04 04:19:00 | NOAA-20 | GOIATINS | TOCANTINS | Brasil | 1709005 | 17 | 33 | nan | nan | nan | Cerrado | 1.3 |
| 7083d88a-8508-318a-9885-91ca55381d60 | -11.20285 | -54.87406 | 2026-08-04 04:19:00 | NOAA-20 | NOVA SANTA HELENA | MATO GROSSO | Brasil | 5106190 | 51 | 33 | nan | nan | nan | Amazônia | 1.9 |
| ae4fb6e3-0072-3254-a477-6417d2e102d4 | -11.21664 | -54.86417 | 2026-08-04 04:19:00 | NOAA-20 | NOVA SANTA HELENA | MATO GROSSO | Brasil | 5106190 | 51 | 33 | nan | nan | nan | Amazônia | 2.6 |
| 21f83721-cf22-39f7-89f3-ae244f966fee | -11.214 | -54.84702 | 2026-08-04 04:19:00 | NOAA-20 | NOVA SANTA HELENA | MATO GROSSO | Brasil | 5106190 | 51 | 33 | nan | nan | nan | Amazônia | 2.2 |
| d6ef1744-5506-3e1e-a450-00f426e5364b | -6.98835 | -42.11738 | 2026-08-04 04:19:00 | NOAA-20 | OEIRAS | PIAUÍ | Brasil | 2207009 | 22 | 33 | nan | nan | nan | Caatinga | 1.1 |
| 8def3fac-671a-3f57-a05c-ed8a478c1225 | -9.61029 | -47.76119 | 2026-08-04 04:19:00 | NOAA-20 | RIO SONO | TOCANTINS | Brasil | 1718758 | 17 | 33 | nan | nan | nan | Cerrado | 1.6 |
| a1291c62-3c10-3df0-8494-a6176714b4d1 | -10.62873 | -49.31995 | 2026-08-04 04:19:00 | NOAA-20 | CRISTALÂNDIA | TOCANTINS | Brasil | 1706100 | 17 | 33 | nan | nan | nan | Cerrado | 0.9 |
| dc08cda6-b4ed-3c2d-a3d9-e4971b85ab53 | -6.54478 | -55.1576 | 2026-08-04 04:19:00 | NOAA-20 | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 2.3 |
| 729a9e3a-ca95-398f-9935-39bd668d088b | -7.91551 | -44.9271 | 2026-08-04 04:19:00 | NOAA-20 | BAIXA GRANDE DO RIBEIRO | PIAUÍ | Brasil | 2201150 | 22 | 33 | nan | nan | nan | Cerrado | 1.4 |
| 2ac5a938-237f-3891-a622-37f9d608f88a | -6.5598 | -55.16342 | 2026-08-04 04:19:00 | NOAA-20 | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 3.0 |
| 1d6b6ad4-0d2b-3610-bb2d-b94f12bfc399 | -6.53356 | -55.16429 | 2026-08-04 04:19:00 | NOAA-20 | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 3.6 |
| 71b250f0-2c03-3900-88e7-7da8bc73c4e0 | -8.35916 | -48.24382 | 2026-08-04 04:19:00 | NOAA-20 | TUPIRATINS | TOCANTINS | Brasil | 1721307 | 17 | 33 | nan | nan | nan | Cerrado | 2.2 |
| 16e68861-7033-37c2-afb2-2238249350c8 | -10.56432 | -46.77298 | 2026-08-04 04:19:00 | NOAA-20 | MATEIROS | TOCANTINS | Brasil | 1712702 | 17 | 33 | nan | nan | nan | Cerrado | 2.2 |
| be69519b-31d8-382e-901a-2fca5902b82f | -11.21373 | -54.85377 | 2026-08-04 04:19:00 | NOAA-20 | NOVA SANTA HELENA | MATO GROSSO | Brasil | 5106190 | 51 | 33 | nan | nan | nan | Amazônia | 3.3 |
| 2fa996ba-aab6-33f3-935e-a354443a0fe4 | -6.98443 | -42.12043 | 2026-08-04 04:19:00 | NOAA-20 | OEIRAS | PIAUÍ | Brasil | 2207009 | 22 | 33 | nan | nan | nan | Caatinga | 0.8 |
| df192bd9-3e35-34f5-91f9-5c8ec2f168df | -11.20828 | -54.8459 | 2026-08-04 04:19:00 | NOAA-20 | NOVA SANTA HELENA | MATO GROSSO | Brasil | 5106190 | 51 | 33 | nan | nan | nan | Amazônia | 2.0 |
| 0508a3eb-fd0b-347c-af5a-351fabf7a829 | -8.93021 | -45.20808 | 2026-08-04 04:19:00 | NOAA-20 | BAIXA GRANDE DO RIBEIRO | PIAUÍ | Brasil | 2201150 | 22 | 33 | nan | nan | nan | Cerrado | 1.6 |
| e3318c10-d979-307d-8cd2-c6c6bcc59dbb | -10.7532 | -42.09486 | 2026-08-04 04:19:00 | NOAA-20 | ITAGUAÇU DA BAHIA | BAHIA | Brasil | 2915353 | 29 | 33 | nan | nan | nan | Caatinga | 1.6 |
| c2d8a52a-5c68-3b58-9fa5-9e03eaaecdaa | -7.39599 | -45.05458 | 2026-08-04 04:19:00 | NOAA-20 | SÃO FÉLIX DE BALSAS | MARANHÃO | Brasil | 2110807 | 21 | 33 | nan | nan | nan | Cerrado | 1.3 |
| 04b08e82-c1ae-33e0-957a-1c03e4472c39 | -7.60197 | -46.46741 | 2026-08-04 04:19:00 | NOAA-20 | RIACHÃO | MARANHÃO | Brasil | 2109502 | 21 | 33 | nan | nan | nan | Cerrado | 5.4 |
| 3d24efb1-2ea1-3ce3-98b1-0f64a60f0861 | -6.95975 | -52.82368 | 2026-08-04 04:19:00 | NOAA-20 | SÃO FÉLIX DO XINGU | PARÁ | Brasil | 1507300 | 15 | 33 | nan | nan | nan | Amazônia | 0.9 |
| f8541d6e-6448-3537-9335-a0e387be27e9 | -7.90822 | -44.92959 | 2026-08-04 04:19:00 | NOAA-20 | BAIXA GRANDE DO RIBEIRO | PIAUÍ | Brasil | 2201150 | 22 | 33 | nan | nan | nan | Cerrado | 3.1 |
| b77d6a2c-27e3-3111-93b3-c0b5cd8f634f | -11.22232 | -54.86551 | 2026-08-04 04:19:00 | NOAA-20 | NOVA SANTA HELENA | MATO GROSSO | Brasil | 5106190 | 51 | 33 | nan | nan | nan | Amazônia | 10.9 |
| ca030f0b-e04e-3434-b1e7-83fb2af70ce9 | -11.21451 | -54.84982 | 2026-08-04 04:19:00 | NOAA-20 | NOVA SANTA HELENA | MATO GROSSO | Brasil | 5106190 | 51 | 33 | nan | nan | nan | Amazônia | 2.8 |
| eaa2094b-3d8a-3dba-84f8-a60da835f271 | -11.12159 | -50.40518 | 2026-08-04 04:19:00 | NOAA-20 | LAGOA DA CONFUSÃO | TOCANTINS | Brasil | 1711902 | 17 | 33 | nan | nan | nan | Cerrado | 1.5 |
| 10ae2ba5-c303-38a0-b8fd-b628d5f7fa4e | -11.20125 | -54.88237 | 2026-08-04 04:19:00 | NOAA-20 | NOVA SANTA HELENA | MATO GROSSO | Brasil | 5106190 | 51 | 33 | nan | nan | nan | Amazônia | 2.3 |
| 10674193-5aaa-3521-8998-1ecf1d7264f3 | -11.7594 | -50.29029 | 2026-08-04 04:19:00 | NOAA-20 | FORMOSO DO ARAGUAIA | TOCANTINS | Brasil | 1708205 | 17 | 33 | nan | nan | nan | Cerrado | 0.6 |
| b1305cb0-5e8d-3cd7-a676-1367888d981e | -6.55155 | -55.17274 | 2026-08-04 04:19:00 | NOAA-20 | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 3.1 |
| 03eba86c-a7c1-30c6-97d9-fe5c1c61ebed | -7.6216 | -45.31165 | 2026-08-04 04:19:00 | NOAA-20 | RIBEIRO GONÇALVES | PIAUÍ | Brasil | 2208908 | 22 | 33 | nan | nan | nan | Cerrado | 1.6 |
| 956762c7-4cf3-31a8-94d5-d843c5c208e1 | -11.25263 | -54.83719 | 2026-08-04 04:19:00 | NOAA-20 | NOVA SANTA HELENA | MATO GROSSO | Brasil | 5106190 | 51 | 33 | nan | nan | nan | Amazônia | 1.2 |
| 33408adc-a3ea-30a4-915d-2704eb64b4cb | -11.14585 | -50.39281 | 2026-08-04 04:19:00 | NOAA-20 | LAGOA DA CONFUSÃO | TOCANTINS | Brasil | 1711902 | 17 | 33 | nan | nan | nan | Cerrado | 0.6 |
| b879eac4-8857-305f-9c10-c7613d5fe590 | -6.72061 | -50.94618 | 2026-08-04 04:19:00 | NOAA-20 | OURILÂNDIA DO NORTE | PARÁ | Brasil | 1505437 | 15 | 33 | nan | nan | nan | Amazônia | 2.0 |
| b4cbc1af-a716-3197-a52c-79fda90aff2b | -9.14062 | -49.66406 | 2026-08-04 04:19:00 | NOAA-20 | ARAGUACEMA | TOCANTINS | Brasil | 1701903 | 17 | 33 | nan | nan | nan | Cerrado | 1.0 |
| 2de8420b-2d54-395d-ad28-0b5c41a0d35f | -7.21023 | -42.97687 | 2026-08-04 04:19:00 | NOAA-20 | FLORIANO | PIAUÍ | Brasil | 2203909 | 22 | 33 | nan | nan | nan | Caatinga | 1.4 |
| f827e4ec-3b57-307a-bc41-ad75ecf7a58c | -7.9088 | -44.92599 | 2026-08-04 04:19:00 | NOAA-20 | BAIXA GRANDE DO RIBEIRO | PIAUÍ | Brasil | 2201150 | 22 | 33 | nan | nan | nan | Cerrado | 3.3 |
| f6f35f0d-0795-36b6-ae3e-11f0d3bb625c | -11.21324 | -54.85097 | 2026-08-04 04:19:00 | NOAA-20 | NOVA SANTA HELENA | MATO GROSSO | Brasil | 5106190 | 51 | 33 | nan | nan | nan | Amazônia | 2.2 |
| 34bd4c9d-2a9f-3004-a2f4-84b35189e741 | -6.53753 | -55.16171 | 2026-08-04 04:19:00 | NOAA-20 | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 2.9 |
| 7de7af3f-5dbd-3f09-aeae-a9838b818132 | -11.22352 | -54.86427 | 2026-08-04 04:19:00 | NOAA-20 | NOVA SANTA HELENA | MATO GROSSO | Brasil | 5106190 | 51 | 33 | nan | nan | nan | Amazônia | 9.7 |
| 0a24b5d7-725b-3471-a01d-cc0776e44b60 | -6.71971 | -50.95139 | 2026-08-04 04:19:00 | NOAA-20 | OURILÂNDIA DO NORTE | PARÁ | Brasil | 1505437 | 15 | 33 | nan | nan | nan | Amazônia | 2.0 |
| ef916b5c-64b3-33f0-a167-41ee36ad4a19 | -6.5787 | -55.16696 | 2026-08-04 04:19:00 | NOAA-20 | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 2.8 |
| 0e2b6540-8c6e-3cb1-81c2-23b4a3d4d849 | -10.89738 | -45.19584 | 2026-08-04 04:19:00 | NOAA-20 | FORMOSA DO RIO PRETO | BAHIA | Brasil | 2911105 | 29 | 33 | nan | nan | nan | Cerrado | 0.8 |
| a606309d-9811-38f2-b63d-2d95313cb8de | -10.55952 | -46.78022 | 2026-08-04 04:19:00 | NOAA-20 | MATEIROS | TOCANTINS | Brasil | 1712702 | 17 | 33 | nan | nan | nan | Cerrado | 1.5 |
| 5b5ee8c7-3a8a-3d8b-8bdb-010074d8eaa8 | -11.21864 | -54.85892 | 2026-08-04 04:19:00 | NOAA-20 | NOVA SANTA HELENA | MATO GROSSO | Brasil | 5106190 | 51 | 33 | nan | nan | nan | Amazônia | 3.3 |
| 1fde6700-a714-38f7-954a-c96296ac0aa2 | -9.08042 | -46.04873 | 2026-08-04 04:19:00 | NOAA-20 | ALTO PARNAÍBA | MARANHÃO | Brasil | 2100501 | 21 | 33 | nan | nan | nan | Cerrado | 1.7 |
| ca4a6f18-ea27-3c8c-99e8-55d67a6412bd | -10.58182 | -46.7759 | 2026-08-04 04:19:00 | NOAA-20 | MATEIROS | TOCANTINS | Brasil | 1712702 | 17 | 33 | nan | nan | nan | Cerrado | 0.9 |
| 35b4c245-0f4e-34b3-8696-a26730c22026 | -8.35116 | -45.98237 | 2026-08-04 04:19:00 | NOAA-20 | TASSO FRAGOSO | MARANHÃO | Brasil | 2112001 | 21 | 33 | nan | nan | nan | Cerrado | 6.3 |
| 28dc2487-e0fc-3ec3-abf5-2457ffdd8ebc | -6.54621 | -55.16639 | 2026-08-04 04:19:00 | NOAA-20 | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 3.3 |
| 1297c2f9-acec-392e-8bfd-c9b7a272e0f7 | -11.22268 | -54.86847 | 2026-08-04 04:19:00 | NOAA-20 | NOVA SANTA HELENA | MATO GROSSO | Brasil | 5106190 | 51 | 33 | nan | nan | nan | Amazônia | 9.7 |
| b3997842-51b9-32ed-a628-e7cf288d6ac7 | -6.72539 | -50.94697 | 2026-08-04 04:19:00 | NOAA-20 | OURILÂNDIA DO NORTE | PARÁ | Brasil | 1505437 | 15 | 33 | nan | nan | nan | Amazônia | 4.1 |
| b81dade1-aaa8-3418-8d17-a0fdad1c4ce0 | -8.56287 | -47.75135 | 2026-08-04 04:19:00 | NOAA-20 | ITACAJÁ | TOCANTINS | Brasil | 1710508 | 17 | 33 | nan | nan | nan | Cerrado | 1.2 |
| 77565273-450f-3c3c-a2db-9caf6d585ec0 | -7.56222 | -46.00055 | 2026-08-04 04:19:00 | NOAA-20 | BALSAS | MARANHÃO | Brasil | 2101400 | 21 | 33 | nan | nan | nan | Cerrado | 0.6 |
| 92111614-f1ab-3d27-8628-fcc762a06ab0 | -11.21584 | -54.86834 | 2026-08-04 04:19:00 | NOAA-20 | NOVA SANTA HELENA | MATO GROSSO | Brasil | 5106190 | 51 | 33 | nan | nan | nan | Amazônia | 2.6 |
| dc212f6d-1879-3f00-8ab4-88e417751d5c | -8.83177 | -50.48171 | 2026-08-04 04:19:00 | NOAA-20 | SANTA MARIA DAS BARREIRAS | PARÁ | Brasil | 1506583 | 15 | 33 | nan | nan | nan | Amazônia | 2.1 |
| 1d342163-d01d-3a46-a6c0-e880727600e6 | -7.49678 | -45.84337 | 2026-08-04 04:19:00 | NOAA-20 | BALSAS | MARANHÃO | Brasil | 2101400 | 21 | 33 | nan | nan | nan | Cerrado | 1.4 |
| f0792fd9-9324-3527-bd4c-f432c7e94617 | -11.20599 | -54.85778 | 2026-08-04 04:19:00 | NOAA-20 | NOVA SANTA HELENA | MATO GROSSO | Brasil | 5106190 | 51 | 33 | nan | nan | nan | Amazônia | 3.0 |
| 0614d8bd-008d-32ca-b21e-b6053fa10870 | -6.55461 | -55.17543 | 2026-08-04 04:19:00 | NOAA-20 | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 3.8 |
| 562cfd2e-7de0-3b03-bb1a-c1b93494d63b | -11.12085 | -50.40927 | 2026-08-04 04:19:00 | NOAA-20 | LAGOA DA CONFUSÃO | TOCANTINS | Brasil | 1711902 | 17 | 33 | nan | nan | nan | Cerrado | 1.5 |
| 2b751cb3-5843-3cb1-8c76-4b489ce0542d | -10.61406 | -49.9831 | 2026-08-04 04:19:00 | NOAA-20 | LAGOA DA CONFUSÃO | TOCANTINS | Brasil | 1711902 | 17 | 33 | nan | nan | nan | Cerrado | 1.4 |
| b9e48051-e396-355a-9705-47339039180f | -11.19297 | -54.86369 | 2026-08-04 04:19:00 | NOAA-20 | NOVA SANTA HELENA | MATO GROSSO | Brasil | 5106190 | 51 | 33 | nan | nan | nan | Amazônia | 2.8 |
| d0daeaa8-e402-3d75-9396-308e2084a5a5 | -7.62099 | -45.31534 | 2026-08-04 04:19:00 | NOAA-20 | RIBEIRO GONÇALVES | PIAUÍ | Brasil | 2208908 | 22 | 33 | nan | nan | nan | Cerrado | 0.4 |
| f25444af-a4e1-347e-8bed-fac2b251e0ac | -7.19619 | -43.5816 | 2026-08-04 04:19:00 | NOAA-20 | JERUMENHA | PIAUÍ | Brasil | 2205300 | 22 | 33 | nan | nan | nan | Cerrado | 2.4 |
| 0635b0b7-8e45-38cc-a491-2c4446fca3a5 | -12.55614 | -52.24515 | 2026-08-04 04:19:00 | NOAA-20 | QUERÊNCIA | MATO GROSSO | Brasil | 5107065 | 51 | 33 | nan | nan | nan | Amazônia | 3.2 |
| b082a554-e981-35e8-98a9-6bd3643f4424 | -11.21784 | -54.86295 | 2026-08-04 04:19:00 | NOAA-20 | NOVA SANTA HELENA | MATO GROSSO | Brasil | 5106190 | 51 | 33 | nan | nan | nan | Amazônia | 3.5 |
| 25dfa153-d7dd-3401-a306-2dc289f8ed3b | -11.13305 | -50.39043 | 2026-08-04 04:19:00 | NOAA-20 | LAGOA DA CONFUSÃO | TOCANTINS | Brasil | 1711902 | 17 | 33 | nan | nan | nan | Cerrado | 0.7 |
| f194ee3e-a883-3f88-808a-11b0d9825304 | -11.75659 | -50.28162 | 2026-08-04 04:19:00 | NOAA-20 | FORMOSO DO ARAGUAIA | TOCANTINS | Brasil | 1708205 | 17 | 33 | nan | nan | nan | Cerrado | 0.4 |
| 6b16389e-24b2-3612-ae36-38da1de8f084 | -6.55645 | -55.16516 | 2026-08-04 04:19:00 | NOAA-20 | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 3.1 |
| 53c977c4-53f4-3f1d-847c-d3aff2270171 | -6.53566 | -55.17209 | 2026-08-04 04:19:00 | NOAA-20 | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 2.1 |
| 39e7c969-df0c-34b5-bfa1-13b65d578b5e | -11.21617 | -54.87131 | 2026-08-04 04:19:00 | NOAA-20 | NOVA SANTA HELENA | MATO GROSSO | Brasil | 5106190 | 51 | 33 | nan | nan | nan | Amazônia | 2.1 |
| 16feb13a-c34f-3bd2-82dd-51e9158c5222 | -12.04063 | -47.65915 | 2026-08-04 04:19:00 | NOAA-20 | NATIVIDADE | TOCANTINS | Brasil | 1714203 | 17 | 33 | nan | nan | nan | Cerrado | 2.5 |
| 3e62416a-6db9-3f84-9a7f-e2af04e59185 | -7.53204 | -46.0317 | 2026-08-04 04:19:00 | NOAA-20 | BALSAS | MARANHÃO | Brasil | 2101400 | 21 | 33 | nan | nan | nan | Cerrado | 1.7 |
| 8d725821-c7f4-3350-980a-68c03104f271 | -6.09878 | -55.81528 | 2026-08-04 04:19:00 | NOAA-20 | ITAITUBA | PARÁ | Brasil | 1503606 | 15 | 33 | nan | nan | nan | Amazônia | 1.7 |
| 55e27d2f-5619-3350-959b-015fb507be1b | -6.55107 | -55.15886 | 2026-08-04 04:19:00 | NOAA-20 | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 2.3 |
| 84e5cc1f-22e3-3d7e-97e1-93c5ed0fbf99 | -11.21944 | -54.85492 | 2026-08-04 04:19:00 | NOAA-20 | NOVA SANTA HELENA | MATO GROSSO | Brasil | 5106190 | 51 | 33 | nan | nan | nan | Amazônia | 3.3 |
| a8777293-687e-345e-9836-ce33ac3cb428 | -6.52818 | -55.15821 | 2026-08-04 04:19:00 | NOAA-20 | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 0.9 |
| 1d120d7a-ef0b-30f9-96b6-8ef7a0e86d02 | -11.21049 | -54.86998 | 2026-08-04 04:19:00 | NOAA-20 | NOVA SANTA HELENA | MATO GROSSO | Brasil | 5106190 | 51 | 33 | nan | nan | nan | Amazônia | 2.1 |
| 3205249e-963c-38ca-9591-c2790869af77 | -6.54814 | -55.1561 | 2026-08-04 04:19:00 | NOAA-20 | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 2.7 |
| 2d9f46fd-cfa3-3068-a00f-49ddf3d408e4 | -11.19965 | -54.89066 | 2026-08-04 04:19:00 | NOAA-20 | NOVA SANTA HELENA | MATO GROSSO | Brasil | 5106190 | 51 | 33 | nan | nan | nan | Amazônia | 1.1 |
| e1145fcd-b4e1-31be-8502-a17138dff843 | -8.72791 | -48.32625 | 2026-08-04 04:19:00 | NOAA-20 | GUARAÍ | TOCANTINS | Brasil | 1709302 | 17 | 33 | nan | nan | nan | Cerrado | 1.2 |
| 85f28354-8b8f-3927-a090-066fbbb6b73a | -11.14159 | -50.39202 | 2026-08-04 04:19:00 | NOAA-20 | LAGOA DA CONFUSÃO | TOCANTINS | Brasil | 1711902 | 17 | 33 | nan | nan | nan | Cerrado | 0.6 |
| 0a603f97-0ee7-3891-b1f5-282512d115c6 | -7.3484 | -46.55358 | 2026-08-04 04:19:00 | NOAA-20 | RIACHÃO | MARANHÃO | Brasil | 2109502 | 21 | 33 | nan | nan | nan | Cerrado | 0.8 |
| ad09d94c-5845-3eeb-acfb-e76be0f48efa | -11.12305 | -50.39701 | 2026-08-04 04:19:00 | NOAA-20 | LAGOA DA CONFUSÃO | TOCANTINS | Brasil | 1711902 | 17 | 33 | nan | nan | nan | Cerrado | 1.7 |
| 60905c24-256a-311c-bcd8-55d340a4507c | -11.20752 | -54.84983 | 2026-08-04 04:19:00 | NOAA-20 | NOVA SANTA HELENA | MATO GROSSO | Brasil | 5106190 | 51 | 33 | nan | nan | nan | Amazônia | 2.0 |


[Clique aqui para ver as próximas entradas](README10.md)
