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

## Dados Diários - Página 1

| ID | Latitude | Longitude | Data/Hora GMT | Satélite | Município | Estado | País | Município ID | Estado ID | País ID | Dias sem Chuva | Precipitação | Risco de Fogo | Bioma | FRP |
|----|----------|-----------|---------------|----------|-----------|--------|------|--------------|-----------|---------|----------------|--------------|----------------|-------|-----|
| 225345ab-4f88-3d10-9252-01f2e452ed77 | -7.0398 | -34.9366 | 2025-02-11 00:00:00 | GOES-16 | SANTA RITA | PARAÍBA | Brasil | 2513703 | 25 | 33 | nan | nan | nan | Mata Atlântica | 68.4 |
| 0281c237-38fe-3398-8ac0-fff4f35a71b4 | -10.7553 | -44.934 | 2025-02-11 00:10:00 | GOES-16 | CRISTALÂNDIA DO PIAUÍ | PIAUÍ | Brasil | 2203008 | 22 | 33 | nan | nan | nan | Cerrado | 62.5 |
| beab1385-8111-3e33-be6b-cf33e593010b | -20.75104 | -53.97605 | 2025-02-11 00:43:00 | TERRA_M-M | RIBAS DO RIO PARDO | MATO GROSSO DO SUL | Brasil | 5007109 | 50 | 33 | nan | nan | nan | Cerrado | 19.4 |
| 5f4c3f75-7db4-3fe3-a1ac-16f056bd099d | -22.90136 | -43.65819 | 2025-02-11 00:43:00 | TERRA_M-M | RIO DE JANEIRO | RIO DE JANEIRO | Brasil | 3304557 | 33 | 33 | nan | nan | nan | Mata Atlântica | 9.1 |
| 39a63026-4f8c-32c7-9eb0-4db02e35d77a | -20.74986 | -53.96941 | 2025-02-11 00:43:00 | TERRA_M-M | RIBAS DO RIO PARDO | MATO GROSSO DO SUL | Brasil | 5007109 | 50 | 33 | nan | nan | nan | Cerrado | 26.1 |
| 33d4f356-0d55-3a78-8040-e782b04ba12e | -21.46829 | -48.57787 | 2025-02-11 00:43:00 | TERRA_M-M | TAQUARITINGA | SÃO PAULO | Brasil | 3553708 | 35 | 33 | nan | nan | nan | Mata Atlântica | 6.1 |
| 91bfb9dd-77f6-3b6c-83f3-4a51e0f12c34 | -18.62992 | -40.35515 | 2025-02-11 00:43:00 | TERRA_M-M | NOVA VENÉCIA | ESPÍRITO SANTO | Brasil | 3203908 | 32 | 33 | nan | nan | nan | Mata Atlântica | 50.5 |
| 36999c28-eeca-3863-b9f6-e9f1923009a9 | -20.07322 | -41.73121 | 2025-02-11 00:43:00 | TERRA_M-M | CHALÉ | MINAS GERAIS | Brasil | 3116001 | 31 | 33 | nan | nan | nan | Mata Atlântica | 24.2 |
| 26c8a0c0-03d9-3048-a2d7-a25d8e45155f | -18.53656 | -39.92979 | 2025-02-11 00:43:00 | TERRA_M-M | CONCEIÇÃO DA BARRA | ESPÍRITO SANTO | Brasil | 3201605 | 32 | 33 | nan | nan | nan | Mata Atlântica | 12.2 |
| 548c2b64-9c9c-3348-8120-be99aac8390e | -20.7483 | -53.94683 | 2025-02-11 00:43:00 | TERRA_M-M | RIBAS DO RIO PARDO | MATO GROSSO DO SUL | Brasil | 5007109 | 50 | 33 | nan | nan | nan | Cerrado | 18.9 |
| e1cd6b90-2f0e-3ed6-8e9f-a3110338452a | -18.62982 | -40.34489 | 2025-02-11 00:43:00 | TERRA_M-M | NOVA VENÉCIA | ESPÍRITO SANTO | Brasil | 3203908 | 32 | 33 | nan | nan | nan | Mata Atlântica | 38.0 |
| 0cf15319-7926-3e9b-a8eb-9f47d0c7ec5d | -18.6325 | -40.36115 | 2025-02-11 00:43:00 | TERRA_M-M | NOVA VENÉCIA | ESPÍRITO SANTO | Brasil | 3203908 | 32 | 33 | nan | nan | nan | Mata Atlântica | 15.5 |
| 05298589-9637-37b2-a666-ded5c597186e | -21.49291 | -48.7809 | 2025-02-11 00:43:00 | TERRA_M-M | ITÁPOLIS | SÃO PAULO | Brasil | 3522703 | 35 | 33 | nan | nan | nan | Cerrado | 8.8 |
| ba2412c1-7292-32a2-aa99-10fc43af99f6 | -20.28809 | -55.01004 | 2025-02-11 00:43:00 | TERRA_M-M | TERENOS | MATO GROSSO DO SUL | Brasil | 5008008 | 50 | 33 | nan | nan | nan | Cerrado | 37.9 |
| c53281c4-76f8-3340-88e2-4fcbeeaa5990 | -18.62711 | -40.33888 | 2025-02-11 00:43:00 | TERRA_M-M | NOVA VENÉCIA | ESPÍRITO SANTO | Brasil | 3203908 | 32 | 33 | nan | nan | nan | Mata Atlântica | 19.7 |
| 1829f2c4-aec7-3964-b8bd-e8e655cf5fd2 | -21.51677 | -47.1466 | 2025-02-11 00:43:00 | TERRA_M-M | TAMBAÚ | SÃO PAULO | Brasil | 3553302 | 35 | 33 | nan | nan | nan | Cerrado | 5.5 |
| f705e5ee-217c-3a08-a942-64267e269b77 | -20.07123 | -41.71894 | 2025-02-11 00:43:00 | TERRA_M-M | CHALÉ | MINAS GERAIS | Brasil | 3116001 | 31 | 33 | nan | nan | nan | Mata Atlântica | 18.6 |
| 07c6871c-4e61-317f-8536-32d0f5663abb | -7.24533 | -44.71909 | 2025-02-11 00:47:00 | TERRA_M-M | SÃO FÉLIX DE BALSAS | MARANHÃO | Brasil | 2110807 | 21 | 33 | nan | nan | nan | Cerrado | 6.2 |
| d71b8c47-e28b-3b45-ae10-ca8bc4b48bc8 | -11.57892 | -44.8715 | 2025-02-11 00:47:00 | TERRA_M-M | RIACHÃO DAS NEVES | BAHIA | Brasil | 2926202 | 29 | 33 | nan | nan | nan | Cerrado | 5.9 |
| 8f93059f-8742-3a82-a204-6b3abb8e9a39 | -6.83469 | -45.48317 | 2025-02-11 00:47:00 | TERRA_M-M | SÃO RAIMUNDO DAS MANGABEIRAS | MARANHÃO | Brasil | 2111607 | 21 | 33 | nan | nan | nan | Cerrado | 9.5 |
| 24c19ef8-9523-3487-898f-a9fba5f12a2f | -20.2836 | -55.001999 | 2025-02-11 00:48:00 | METOP-C | TERENOS | MATO GROSSO DO SUL | Brasil | 5008008 | 50 | 33 | nan | nan | nan | Cerrado | nan |
| dcdfc90a-353f-37d2-8e4e-6f96f98b18fd | -30.412201 | -50.655998 | 2025-02-11 00:48:00 | METOP-C | PALMARES DO SUL | RIO GRANDE DO SUL | Brasil | 4313656 | 43 | 33 | nan | nan | nan | Pampa | nan |
| effd0131-5134-3c9c-9e25-0b19db203f3c | -20.293301 | -55.000198 | 2025-02-11 00:48:00 | METOP-C | TERENOS | MATO GROSSO DO SUL | Brasil | 5008008 | 50 | 33 | nan | nan | nan | Cerrado | nan |
| 34ab5050-cbf0-3865-b337-b34e535f3a70 | -10.7531 | -44.943199 | 2025-02-11 00:48:00 | METOP-C | CRISTALÂNDIA DO PIAUÍ | PIAUÍ | Brasil | 2203008 | 22 | 33 | nan | nan | nan | Cerrado | nan |
| 753b9542-4bd2-3faa-8ddd-9799bef9a06b | -6.8337 | -45.474701 | 2025-02-11 00:48:00 | METOP-C | SÃO RAIMUNDO DAS MANGABEIRAS | MARANHÃO | Brasil | 2111607 | 21 | 33 | nan | nan | nan | Cerrado | nan |
| e841642c-2a4d-360f-b2a8-747f363cf6b8 | -18.627899 | -40.3372 | 2025-02-11 00:48:00 | METOP-C | NOVA VENÉCIA | ESPÍRITO SANTO | Brasil | 3203908 | 32 | 33 | nan | nan | nan | Mata Atlântica | nan |
| c6dedd44-d0a6-35c3-9ee5-204fff52403b | -20.280701 | -54.9855 | 2025-02-11 00:48:00 | METOP-C | TERENOS | MATO GROSSO DO SUL | Brasil | 5008008 | 50 | 33 | nan | nan | nan | Cerrado | nan |
| 486fd8da-03a4-3f10-aa3a-0d46e39c9518 | -30.410101 | -50.643002 | 2025-02-11 00:48:00 | METOP-C | PALMARES DO SUL | RIO GRANDE DO SUL | Brasil | 4313656 | 43 | 33 | nan | nan | nan | Pampa | nan |
| 1b2e6c6f-3519-3eab-a51b-89eae204af60 | -10.7605 | -44.931198 | 2025-02-11 00:48:00 | METOP-C | CRISTALÂNDIA DO PIAUÍ | PIAUÍ | Brasil | 2203008 | 22 | 33 | nan | nan | nan | Cerrado | nan |
| 6a8d56c8-19fb-3930-b41f-ff19e14b1a06 | -10.7508 | -44.933601 | 2025-02-11 00:48:00 | METOP-C | CRISTALÂNDIA DO PIAUÍ | PIAUÍ | Brasil | 2203008 | 22 | 33 | nan | nan | nan | Cerrado | nan |
| fea68d96-00fe-34a4-8bfc-06dfa59aaf24 | -20.7526 | -53.954201 | 2025-02-11 00:48:00 | METOP-C | RIBAS DO RIO PARDO | MATO GROSSO DO SUL | Brasil | 5007109 | 50 | 33 | nan | nan | nan | Cerrado | nan |
| e7f5b9a3-e934-39a9-8b3a-5952f4fc8292 | -20.755199 | -53.968601 | 2025-02-11 00:48:00 | METOP-C | RIBAS DO RIO PARDO | MATO GROSSO DO SUL | Brasil | 5007109 | 50 | 33 | nan | nan | nan | Cerrado | nan |
| d88402a8-f72c-3c6d-8482-e926e5dc430d | -18.635201 | -40.365398 | 2025-02-11 00:48:00 | METOP-C | NOVA VENÉCIA | ESPÍRITO SANTO | Brasil | 3203908 | 32 | 33 | nan | nan | nan | Mata Atlântica | nan |
| b4fb8a6c-ea15-34fb-bb27-a898047e17dc | -18.631599 | -40.351299 | 2025-02-11 00:48:00 | METOP-C | NOVA VENÉCIA | ESPÍRITO SANTO | Brasil | 3203908 | 32 | 33 | nan | nan | nan | Mata Atlântica | nan |
| 99526ff7-8947-349a-ba88-e33a31feb80e | -22.9063 | -43.6609 | 2025-02-11 00:48:00 | METOP-C | RIO DE JANEIRO | RIO DE JANEIRO | Brasil | 3304557 | 33 | 33 | nan | nan | nan | Mata Atlântica | nan |
| a8668b8d-b09b-3c70-b0e1-3600866d3815 | -6.8361 | -45.484699 | 2025-02-11 00:48:00 | METOP-C | SÃO RAIMUNDO DAS MANGABEIRAS | MARANHÃO | Brasil | 2111607 | 21 | 33 | nan | nan | nan | Cerrado | nan |
| fc932763-9272-3305-893f-cb4db42a77e4 | -32.189999 | -52.252602 | 2025-02-11 00:48:00 | METOP-C | RIO GRANDE | RIO GRANDE DO SUL | Brasil | 4315602 | 43 | 33 | nan | nan | nan | Pampa | nan |
| 6bc337c6-2b8b-3a04-a161-bbfb58dddd1d | -7.0949 | -35.0943 | 2025-02-11 00:50:00 | GOES-16 | CRUZ DO ESPÍRITO SANTO | PARAÍBA | Brasil | 2504900 | 25 | 33 | nan | nan | nan | Mata Atlântica | 89.5 |
| ff285d20-14be-3c49-b121-ed628f3a2761 | -20.2833 | -54.983501 | 2025-02-11 01:32:00 | METOP-B | TERENOS | MATO GROSSO DO SUL | Brasil | 5008008 | 50 | 33 | nan | nan | nan | Cerrado | nan |
| 4105e1d5-8aab-39c8-952b-e03da2fc83b7 | -32.194698 | -52.249901 | 2025-02-11 01:32:00 | METOP-B | RIO GRANDE | RIO GRANDE DO SUL | Brasil | 4315602 | 43 | 33 | nan | nan | nan | Pampa | nan |
| 156782d5-b7da-3f6c-a3f2-f5598d28ddc8 | -16.091999 | -60.053101 | 2025-02-11 01:32:00 | METOP-B | VILA BELA DA SANTÍSSIMA TRINDADE | MATO GROSSO | Brasil | 5105507 | 51 | 33 | nan | nan | nan | Amazônia | nan |
| 0e0a9bbd-dc3f-3744-a054-bd91768d3c9f | -16.0823 | -60.055599 | 2025-02-11 01:32:00 | METOP-B | VILA BELA DA SANTÍSSIMA TRINDADE | MATO GROSSO | Brasil | 5105507 | 51 | 33 | nan | nan | nan | Amazônia | nan |
| 61f10e49-46b3-3326-a9bc-8c9b71aecaca | -7.0391 | -34.9917 | 2025-02-11 02:40:00 | GOES-16 | SANTA RITA | PARAÍBA | Brasil | 2513703 | 25 | 33 | nan | nan | nan | Mata Atlântica | 72.8 |
| f66a10f9-b7a0-37bb-ab64-3feab78d1453 | -7.0394 | -34.9641 | 2025-02-11 02:40:00 | GOES-16 | SANTA RITA | PARAÍBA | Brasil | 2513703 | 25 | 33 | nan | nan | nan | Mata Atlântica | 75.9 |
| d34a2835-d56b-39e5-955f-be4fa660f75c | -4.59184 | -37.73193 | 2025-02-11 03:27:00 | NOAA-21 | ARACATI | CEARÁ | Brasil | 2301109 | 23 | 33 | nan | nan | nan | Caatinga | 1.9 |
| a0ada61c-9b3b-32ad-8d06-65c423d53ed6 | -4.70742 | -38.46699 | 2025-02-11 03:27:00 | NOAA-21 | MORADA NOVA | CEARÁ | Brasil | 2308708 | 23 | 33 | nan | nan | nan | Caatinga | 1.0 |
| 41d5345e-60b6-3902-a3bf-b411ef735464 | -4.59097 | -37.72847 | 2025-02-11 03:27:00 | NOAA-21 | ARACATI | CEARÁ | Brasil | 2301109 | 23 | 33 | nan | nan | nan | Caatinga | 1.4 |
| d416070a-36cb-3da6-b33b-0be4dfc4e5d2 | -7.24546 | -44.71364 | 2025-02-11 03:29:00 | NOAA-21 | SÃO FÉLIX DE BALSAS | MARANHÃO | Brasil | 2110807 | 21 | 33 | nan | nan | nan | Cerrado | 2.2 |
| 3fc01df9-c46e-388a-a5cd-3dcb98bbe746 | -7.24442 | -44.71911 | 2025-02-11 03:29:00 | NOAA-21 | SÃO FÉLIX DE BALSAS | MARANHÃO | Brasil | 2110807 | 21 | 33 | nan | nan | nan | Cerrado | 2.2 |
| 102ded6f-c130-37e5-999e-e07e9e906592 | -7.23297 | -44.71519 | 2025-02-11 03:29:00 | NOAA-21 | SÃO FÉLIX DE BALSAS | MARANHÃO | Brasil | 2110807 | 21 | 33 | nan | nan | nan | Cerrado | 2.2 |
| 22a3e4fb-1d2a-3f27-85f5-ae6bf6838c61 | -7.72837 | -37.48842 | 2025-02-11 03:29:00 | NOAA-21 | INGAZEIRA | PERNAMBUCO | Brasil | 2607109 | 26 | 33 | nan | nan | nan | Caatinga | 1.1 |
| b647e355-3ab9-377a-8207-8a9e101147e6 | -8.70938 | -36.15922 | 2025-02-11 03:29:00 | NOAA-21 | JUREMA | PERNAMBUCO | Brasil | 2608404 | 26 | 33 | nan | nan | nan | Mata Atlântica | 1.7 |
| e9642480-d680-39c7-8f6b-e19667169102 | -7.23953 | -44.7164 | 2025-02-11 03:29:00 | NOAA-21 | SÃO FÉLIX DE BALSAS | MARANHÃO | Brasil | 2110807 | 21 | 33 | nan | nan | nan | Cerrado | 2.2 |
| 0628f0de-da74-3b37-ac2b-ce0a0a2fe166 | -6.97377 | -42.82452 | 2025-02-11 03:29:00 | NOAA-21 | NAZARÉ DO PIAUÍ | PIAUÍ | Brasil | 2206704 | 22 | 33 | nan | nan | nan | Caatinga | 1.8 |
| cc5a5cad-b27e-3b56-a4a1-d3d26f6774b7 | -6.97964 | -42.8256 | 2025-02-11 03:29:00 | NOAA-21 | NAZARÉ DO PIAUÍ | PIAUÍ | Brasil | 2206704 | 22 | 33 | nan | nan | nan | Caatinga | 1.5 |
| f55bd7ba-e1a1-307d-b57b-325e5bdf11cf | -7.24611 | -44.7175 | 2025-02-11 03:29:00 | NOAA-21 | SÃO FÉLIX DE BALSAS | MARANHÃO | Brasil | 2110807 | 21 | 33 | nan | nan | nan | Cerrado | 2.1 |
| 57eb8292-30d9-30ba-9d82-63c21d1afdce | -8.70863 | -36.16368 | 2025-02-11 03:29:00 | NOAA-21 | JUREMA | PERNAMBUCO | Brasil | 2608404 | 26 | 33 | nan | nan | nan | Mata Atlântica | 1.7 |
| ef4c05e3-49cb-397b-81b5-7aaa7e869bb0 | -8.51479 | -36.64846 | 2025-02-11 03:29:00 | NOAA-21 | PESQUEIRA | PERNAMBUCO | Brasil | 2610905 | 26 | 33 | nan | nan | nan | Caatinga | 0.9 |
| 48c16b1a-55df-35de-9aa0-089958c5bb97 | -12.84788 | -43.82186 | 2025-02-11 03:32:00 | NOAA-21 | SERRA DOURADA | BAHIA | Brasil | 2930303 | 29 | 33 | nan | nan | nan | Cerrado | 3.4 |
| f6f53dfa-682f-31d3-98a7-6d4284722719 | -12.85353 | -43.82294 | 2025-02-11 03:32:00 | NOAA-21 | SERRA DOURADA | BAHIA | Brasil | 2930303 | 29 | 33 | nan | nan | nan | Cerrado | 4.3 |
| 7ebb149f-e516-3d0a-8e14-2eec3d996dc3 | -12.8471 | -43.82576 | 2025-02-11 03:32:00 | NOAA-21 | SERRA DOURADA | BAHIA | Brasil | 2930303 | 29 | 33 | nan | nan | nan | Cerrado | 6.4 |
| a77c9fdf-3222-30a1-a365-76a742b92cbe | -12.85275 | -43.82686 | 2025-02-11 03:32:00 | NOAA-21 | SERRA DOURADA | BAHIA | Brasil | 2930303 | 29 | 33 | nan | nan | nan | Cerrado | 3.5 |
| 069a076d-726d-3027-9c4a-873024ea7b95 | -18.7691 | -39.86683 | 2025-02-11 03:32:00 | NOAA-21 | SÃO MATEUS | ESPÍRITO SANTO | Brasil | 3204906 | 32 | 33 | nan | nan | nan | Mata Atlântica | 0.8 |
| 257a5782-caad-3a90-96ad-7a7d209c5f68 | -12.86337 | -38.36627 | 2025-02-11 03:32:00 | NOAA-21 | SALVADOR | BAHIA | Brasil | 2927408 | 29 | 33 | nan | nan | nan | Mata Atlântica | 1.2 |
| 4adae6a7-3341-3a78-8806-ad483a6105d9 | -18.53447 | -39.93298 | 2025-02-11 03:32:00 | NOAA-21 | CONCEIÇÃO DA BARRA | ESPÍRITO SANTO | Brasil | 3201605 | 32 | 33 | nan | nan | nan | Mata Atlântica | 1.6 |
| 8306e41e-a810-37c4-ab9e-67e67fd6714b | -18.53911 | -39.93018 | 2025-02-11 03:32:00 | NOAA-21 | CONCEIÇÃO DA BARRA | ESPÍRITO SANTO | Brasil | 3201605 | 32 | 33 | nan | nan | nan | Mata Atlântica | 1.2 |
| b5dcd654-2cd0-3887-a969-ea7c34ec0067 | -12.86018 | -38.36822 | 2025-02-11 03:32:00 | NOAA-21 | SALVADOR | BAHIA | Brasil | 2927408 | 29 | 33 | nan | nan | nan | Mata Atlântica | 0.6 |
| 62300f5c-2a73-31c6-9cf0-f62651b8b1fa | -18.53844 | -39.93379 | 2025-02-11 03:32:00 | NOAA-21 | CONCEIÇÃO DA BARRA | ESPÍRITO SANTO | Brasil | 3201605 | 32 | 33 | nan | nan | nan | Mata Atlântica | 1.6 |
| 39cf1b52-ceb2-39c7-8eb8-f26b7832dbf8 | -20.47983 | -47.53009 | 2025-02-11 03:34:00 | NOAA-21 | RIBEIRÃO CORRENTE | SÃO PAULO | Brasil | 3543105 | 35 | 33 | nan | nan | nan | Cerrado | 4.5 |
| 0ca37f41-4599-3d3b-be18-85763df9f75d | -21.60703 | -48.45078 | 2025-02-11 03:34:00 | NOAA-21 | MATÃO | SÃO PAULO | Brasil | 3529302 | 35 | 33 | nan | nan | nan | Cerrado | 2.1 |
| fba6f562-27dd-3e96-a585-6770d19f33b9 | -21.05868 | -48.47097 | 2025-02-11 03:34:00 | NOAA-21 | BEBEDOURO | SÃO PAULO | Brasil | 3506102 | 35 | 33 | nan | nan | nan | Cerrado | 2.9 |
| 29bd69ff-4c7b-353c-87a9-34740b33ea79 | -20.4799 | -47.53279 | 2025-02-11 03:34:00 | NOAA-21 | RIBEIRÃO CORRENTE | SÃO PAULO | Brasil | 3543105 | 35 | 33 | nan | nan | nan | Cerrado | 7.3 |
| 8dac635d-bf17-3f3a-bd16-b76c65f6308a | -21.35743 | -48.61384 | 2025-02-11 03:34:00 | NOAA-21 | CÂNDIDO RODRIGUES | SÃO PAULO | Brasil | 3510104 | 35 | 33 | nan | nan | nan | Mata Atlântica | 2.6 |
| 5ee36791-2e0f-3d1b-b550-2b35322e01e7 | -21.04887 | -48.47896 | 2025-02-11 03:34:00 | NOAA-21 | BEBEDOURO | SÃO PAULO | Brasil | 3506102 | 35 | 33 | nan | nan | nan | Cerrado | 4.7 |
| 57bb92c3-768f-3b42-a79b-14e444ce453a | -21.59947 | -48.4546 | 2025-02-11 03:34:00 | NOAA-21 | MATÃO | SÃO PAULO | Brasil | 3529302 | 35 | 33 | nan | nan | nan | Cerrado | 1.9 |
| 80b197e6-2338-3975-8475-fb62684354a1 | -21.44176 | -48.69213 | 2025-02-11 03:34:00 | NOAA-21 | TAQUARITINGA | SÃO PAULO | Brasil | 3553708 | 35 | 33 | nan | nan | nan | Cerrado | 2.5 |
| 71af821a-fec5-3742-9018-ef6a559cc4f9 | -21.06419 | -48.47105 | 2025-02-11 03:34:00 | NOAA-21 | BEBEDOURO | SÃO PAULO | Brasil | 3506102 | 35 | 33 | nan | nan | nan | Cerrado | 3.3 |
| af4b4e17-0658-3ffe-b823-98ef0141b169 | -19.6364 | -40.96164 | 2025-02-11 03:34:00 | NOAA-21 | BAIXO GUANDU | ESPÍRITO SANTO | Brasil | 3200805 | 32 | 33 | nan | nan | nan | Mata Atlântica | 0.9 |
| 5b4f2e75-5994-3110-ad61-5532c4923451 | -21.35784 | -48.61584 | 2025-02-11 03:34:00 | NOAA-21 | CÂNDIDO RODRIGUES | SÃO PAULO | Brasil | 3510104 | 35 | 33 | nan | nan | nan | Mata Atlântica | 1.1 |
| acbcdb23-683d-3343-829b-6671463948cd | -21.35152 | -48.61402 | 2025-02-11 03:34:00 | NOAA-21 | CÂNDIDO RODRIGUES | SÃO PAULO | Brasil | 3510104 | 35 | 33 | nan | nan | nan | Mata Atlântica | 1.1 |
| b89849ca-8f99-34c5-ad7a-1affa7f078f8 | -20.4786 | -47.53529 | 2025-02-11 03:34:00 | NOAA-21 | RIBEIRÃO CORRENTE | SÃO PAULO | Brasil | 3543105 | 35 | 33 | nan | nan | nan | Cerrado | 4.5 |
| 3b4d1222-974e-3020-abeb-65e6ee7892de | -21.4431 | -48.68662 | 2025-02-11 03:34:00 | NOAA-21 | TAQUARITINGA | SÃO PAULO | Brasil | 3553708 | 35 | 33 | nan | nan | nan | Cerrado | 2.6 |
| b19ecd84-ea72-3d07-be13-ffc6dc6a5fa3 | -21.05096 | -48.47501 | 2025-02-11 03:34:00 | NOAA-21 | BEBEDOURO | SÃO PAULO | Brasil | 3506102 | 35 | 33 | nan | nan | nan | Cerrado | 7.5 |
| 2d5fd354-75f6-3af6-ba4c-630ac0a0cea6 | -21.05021 | -48.47326 | 2025-02-11 03:34:00 | NOAA-21 | BEBEDOURO | SÃO PAULO | Brasil | 3506102 | 35 | 33 | nan | nan | nan | Cerrado | 4.6 |
| 905a9c41-abdd-3f12-b213-1b744f9d1b29 | -22.67908 | -42.85524 | 2025-02-11 03:34:00 | NOAA-21 | ITABORAÍ | RIO DE JANEIRO | Brasil | 3301900 | 33 | 33 | nan | nan | nan | Mata Atlântica | 2.2 |
| 386324fc-ef7f-3c74-8a0a-cbc05dbced07 | -19.6357 | -40.96531 | 2025-02-11 03:34:00 | NOAA-21 | BAIXO GUANDU | ESPÍRITO SANTO | Brasil | 3200805 | 32 | 33 | nan | nan | nan | Mata Atlântica | 1.3 |
| e8f2f0c2-5e1d-35f6-945d-045b17997068 | -32.20148 | -52.26868 | 2025-02-11 03:38:00 | NOAA-21 | RIO GRANDE | RIO GRANDE DO SUL | Brasil | 4315602 | 43 | 33 | nan | nan | nan | Pampa | 20.3 |
| d65c5a5e-63b2-3375-8551-1634c4350386 | -32.19699 | -52.26089 | 2025-02-11 03:38:00 | NOAA-21 | RIO GRANDE | RIO GRANDE DO SUL | Brasil | 4315602 | 43 | 33 | nan | nan | nan | Pampa | 1.6 |
| 05f5186d-4065-333c-8c10-7c95cfba8b6b | -32.1913 | -52.26351 | 2025-02-11 03:38:00 | NOAA-21 | RIO GRANDE | RIO GRANDE DO SUL | Brasil | 4315602 | 43 | 33 | nan | nan | nan | Pampa | 2.0 |
| 186c93dd-22ae-3a69-b915-a036af231196 | -32.19096 | -52.25865 | 2025-02-11 03:38:00 | NOAA-21 | RIO GRANDE | RIO GRANDE DO SUL | Brasil | 4315602 | 43 | 33 | nan | nan | nan | Pampa | 1.6 |
| d64473eb-a361-3376-bf29-4eec90b036d5 | -32.19281 | -52.25797 | 2025-02-11 03:38:00 | NOAA-21 | RIO GRANDE | RIO GRANDE DO SUL | Brasil | 4315602 | 43 | 33 | nan | nan | nan | Pampa | 2.0 |
| 5ba35f31-222c-3bdb-bcde-a462a61aceee | -4.44786 | -38.05753 | 2025-02-11 03:53:00 | NPP-375D | BEBERIBE | CEARÁ | Brasil | 2302206 | 23 | 33 | nan | nan | nan | Caatinga | 0.8 |
| bc88c61b-d734-374b-b84f-d73790700a03 | -4.59104 | -37.72908 | 2025-02-11 03:53:00 | NPP-375D | ARACATI | CEARÁ | Brasil | 2301109 | 23 | 33 | nan | nan | nan | Caatinga | 1.0 |
| 6a3f8825-f11d-352e-aa21-5a76ec911682 | -4.70822 | -38.4669 | 2025-02-11 03:53:00 | NPP-375D | MORADA NOVA | CEARÁ | Brasil | 2308708 | 23 | 33 | nan | nan | nan | Caatinga | 1.6 |
| 05ed9378-174b-384c-a4da-09b9f2666024 | -4.80236 | -38.77068 | 2025-02-11 03:53:00 | NPP-375D | IBARETAMA | CEARÁ | Brasil | 2305266 | 23 | 33 | nan | nan | nan | Caatinga | 1.0 |
| adbf835b-9643-3a57-b307-0b3a7d417d7e | -7.22994 | -44.71288 | 2025-02-11 03:55:00 | NPP-375D | SÃO FÉLIX DE BALSAS | MARANHÃO | Brasil | 2110807 | 21 | 33 | nan | nan | nan | Cerrado | 0.9 |
| e9972493-1774-38e7-bc0e-16e279ed7dee | -7.92059 | -44.87922 | 2025-02-11 03:55:00 | NPP-375D | URUÇUÍ | PIAUÍ | Brasil | 2211209 | 22 | 33 | nan | nan | nan | Cerrado | 0.7 |
| accbd0d9-7ff0-3248-819c-b35cb9d9a91b | -7.72396 | -37.48742 | 2025-02-11 03:55:00 | NPP-375D | INGAZEIRA | PERNAMBUCO | Brasil | 2607109 | 26 | 33 | nan | nan | nan | Caatinga | 0.5 |
| 05f72ed2-3764-3bf7-af56-8cbaa305a4c8 | -6.97303 | -42.82634 | 2025-02-11 03:55:00 | NPP-375D | NAZARÉ DO PIAUÍ | PIAUÍ | Brasil | 2206704 | 22 | 33 | nan | nan | nan | Caatinga | 1.2 |
| ea600c15-1975-3def-8d7e-dd69cb99a0a7 | -6.97127 | -42.82423 | 2025-02-11 03:55:00 | NPP-375D | NAZARÉ DO PIAUÍ | PIAUÍ | Brasil | 2206704 | 22 | 33 | nan | nan | nan | Caatinga | 1.1 |


[Clique aqui para ver as próximas entradas](README2.md)
