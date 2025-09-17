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

## Dados Diários - Página 4

| ID | Latitude | Longitude | Data/Hora GMT | Satélite | Município | Estado | País | Município ID | Estado ID | País ID | Dias sem Chuva | Precipitação | Risco de Fogo | Bioma | FRP |
|----|----------|-----------|---------------|----------|-----------|--------|------|--------------|-----------|---------|----------------|--------------|----------------|-------|-----|
| 58a31b98-cd4d-32df-9f16-add8f3b3af49 | -6.86062 | -43.96925 | 2025-09-17 00:11:00 | TERRA_M-M | PORTO ALEGRE DO PIAUÍ | PIAUÍ | Brasil | 2208551 | 22 | 33 | nan | nan | nan | Cerrado | 8.1 |
| 80435976-a627-3fb1-9a25-ee692acedfc8 | -7.57855 | -44.56356 | 2025-09-17 00:11:00 | TERRA_M-M | URUÇUÍ | PIAUÍ | Brasil | 2211209 | 22 | 33 | nan | nan | nan | Cerrado | 118.8 |
| c3b795ab-5960-3d90-8758-72f3f5fe8159 | -8.68301 | -46.3729 | 2025-09-17 00:11:00 | TERRA_M-M | BALSAS | MARANHÃO | Brasil | 2101400 | 21 | 33 | nan | nan | nan | Cerrado | 11.5 |
| ef466614-e831-346d-8403-6c5eeb88a86a | -11.49184 | -43.60407 | 2025-09-17 00:11:00 | TERRA_M-M | BARRA | BAHIA | Brasil | 2902708 | 29 | 33 | nan | nan | nan | Cerrado | 4.2 |
| a9d26cd4-ce45-3a00-ab52-933e720f2250 | -9.0942 | -44.94029 | 2025-09-17 00:11:00 | TERRA_M-M | BOM JESUS | PIAUÍ | Brasil | 2201903 | 22 | 33 | nan | nan | nan | Cerrado | 10.6 |
| 6a1f01c1-da2f-3041-91f8-f1f78ec1ea49 | -12.35795 | -47.06834 | 2025-09-17 00:11:00 | TERRA_M-M | TAIPAS DO TOCANTINS | TOCANTINS | Brasil | 1720937 | 17 | 33 | nan | nan | nan | Cerrado | 20.7 |
| 9e530455-e1fa-384f-9b02-a1a6e2beddd2 | -9.05096 | -44.96589 | 2025-09-17 00:11:00 | TERRA_M-M | BOM JESUS | PIAUÍ | Brasil | 2201903 | 22 | 33 | nan | nan | nan | Cerrado | 7.3 |
| c8283d0a-f54e-37a5-ae32-2d0ae182ba82 | -8.96125 | -45.75749 | 2025-09-17 00:11:00 | TERRA_M-M | SANTA FILOMENA | PIAUÍ | Brasil | 2209203 | 22 | 33 | nan | nan | nan | Cerrado | 5.3 |
| d5389a73-043b-339c-9a9d-c2d6e8f30be8 | -6.22186 | -42.0323 | 2025-09-17 00:11:00 | TERRA_M-M | ELESBÃO VELOSO | PIAUÍ | Brasil | 2203503 | 22 | 33 | nan | nan | nan | Caatinga | 5.4 |
| 7bd33a2f-b708-33de-82aa-e62f270dd33b | -9.04842 | -44.94675 | 2025-09-17 00:11:00 | TERRA_M-M | BOM JESUS | PIAUÍ | Brasil | 2201903 | 22 | 33 | nan | nan | nan | Cerrado | 6.2 |
| c355e350-89d1-30b4-9e3d-f53f91bfe586 | -7.72422 | -45.30006 | 2025-09-17 00:11:00 | TERRA_M-M | RIBEIRO GONÇALVES | PIAUÍ | Brasil | 2208908 | 22 | 33 | nan | nan | nan | Cerrado | 11.7 |
| 82dc3995-2da0-33e4-85d0-d3eb81d14151 | -8.16245 | -46.76728 | 2025-09-17 00:11:00 | TERRA_M-M | CAMPOS LINDOS | TOCANTINS | Brasil | 1703842 | 17 | 33 | nan | nan | nan | Cerrado | 13.3 |
| 61e12511-774c-3d28-af5b-ea1ff4d5a9da | -12.69299 | -45.81519 | 2025-09-17 00:11:00 | TERRA_M-M | SÃO DESIDÉRIO | BAHIA | Brasil | 2928901 | 29 | 33 | nan | nan | nan | Cerrado | 11.2 |
| de1c2c67-5249-3ae7-b2ed-a6b7b5a10509 | -8.54518 | -48.97658 | 2025-09-17 00:11:00 | TERRA_M-M | PEQUIZEIRO | TOCANTINS | Brasil | 1716653 | 17 | 33 | nan | nan | nan | Cerrado | 28.2 |
| 72cdb4ec-76fa-34b7-8360-bfc572e34b9a | -13.9598 | -44.23769 | 2025-09-17 00:11:00 | TERRA_M-M | CORIBE | BAHIA | Brasil | 2909109 | 29 | 33 | nan | nan | nan | Cerrado | 7.4 |
| 09fb5227-d373-3462-958b-e76db7541079 | -9.16425 | -46.9357 | 2025-09-17 00:11:00 | TERRA_M-M | LIZARDA | TOCANTINS | Brasil | 1712405 | 17 | 33 | nan | nan | nan | Cerrado | 25.0 |
| 0f53afec-53ae-3f93-aafc-a83779a55d3f | -6.96132 | -44.55736 | 2025-09-17 00:11:00 | TERRA_M-M | SÃO DOMINGOS DO AZEITÃO | MARANHÃO | Brasil | 2110658 | 21 | 33 | nan | nan | nan | Cerrado | 10.4 |
| 7ef2060a-1d8a-388d-852d-c95c254c0983 | -10.73641 | -46.55516 | 2025-09-17 00:11:00 | TERRA_M-M | MATEIROS | TOCANTINS | Brasil | 1712702 | 17 | 33 | nan | nan | nan | Cerrado | 18.6 |
| f4812337-929a-34a2-8964-8eb98c532814 | -12.25088 | -46.762 | 2025-09-17 00:11:00 | TERRA_M-M | PONTE ALTA DO BOM JESUS | TOCANTINS | Brasil | 1717800 | 17 | 33 | nan | nan | nan | Cerrado | 14.3 |
| 3cd136cc-92a2-3727-a42c-01e9b9c31e75 | -6.25993 | -44.68601 | 2025-09-17 00:11:00 | TERRA_M-M | MIRADOR | MARANHÃO | Brasil | 2106706 | 21 | 33 | nan | nan | nan | Cerrado | 11.1 |
| 2643a0ad-1343-3bc8-9720-e375670e059c | -11.03753 | -42.25023 | 2025-09-17 00:11:00 | TERRA_M-M | ITAGUAÇU DA BAHIA | BAHIA | Brasil | 2915353 | 29 | 33 | nan | nan | nan | Caatinga | 5.7 |
| 6804e799-eda0-3153-8385-7828a48aebfd | -10.154 | -46.14657 | 2025-09-17 00:11:00 | TERRA_M-M | ALTO PARNAÍBA | MARANHÃO | Brasil | 2100501 | 21 | 33 | nan | nan | nan | Cerrado | 11.4 |
| 7a9dd05f-5c23-3ded-845e-80e9f6f2981e | -12.70152 | -45.80188 | 2025-09-17 00:11:00 | TERRA_M-M | SÃO DESIDÉRIO | BAHIA | Brasil | 2928901 | 29 | 33 | nan | nan | nan | Cerrado | 10.3 |
| f7f18b32-8edb-3fde-bb2a-0731af368ce7 | -12.35622 | -47.05401 | 2025-09-17 00:11:00 | TERRA_M-M | TAIPAS DO TOCANTINS | TOCANTINS | Brasil | 1720937 | 17 | 33 | nan | nan | nan | Cerrado | 21.0 |
| 13e5330b-c0e7-3240-97be-17255035ae78 | -6.30129 | -42.39978 | 2025-09-17 00:11:00 | TERRA_M-M | REGENERAÇÃO | PIAUÍ | Brasil | 2208809 | 22 | 33 | nan | nan | nan | Caatinga | 6.0 |
| 2ea963c4-b8a5-3873-aba9-61ae2210250c | -6.40298 | -42.66599 | 2025-09-17 00:11:00 | TERRA_M-M | AMARANTE | PIAUÍ | Brasil | 2200509 | 22 | 33 | nan | nan | nan | Caatinga | 8.3 |
| f5c39d72-b3fd-34dc-a38d-72c978eb2846 | -8.97393 | -44.187 | 2025-09-17 00:11:00 | TERRA_M-M | SANTA LUZ | PIAUÍ | Brasil | 2209302 | 22 | 33 | nan | nan | nan | Cerrado | 8.7 |
| fe65136e-3247-3e03-8242-f3fae2da4d0c | -6.96899 | -44.54705 | 2025-09-17 00:11:00 | TERRA_M-M | SÃO DOMINGOS DO AZEITÃO | MARANHÃO | Brasil | 2110658 | 21 | 33 | nan | nan | nan | Cerrado | 8.6 |
| 39fb80d3-c8d3-37c6-962a-96aac681f949 | -11.01146 | -48.91961 | 2025-09-17 00:11:00 | TERRA_M-M | SANTA RITA DO TOCANTINS | TOCANTINS | Brasil | 1718899 | 17 | 33 | nan | nan | nan | Cerrado | 71.0 |
| 9f129e9d-26c1-3308-9925-c348ea825ca9 | -11.4577 | -43.55308 | 2025-09-17 00:11:00 | TERRA_M-M | BARRA | BAHIA | Brasil | 2902708 | 29 | 33 | nan | nan | nan | Cerrado | 10.0 |
| 9316d4cd-9eb1-3463-a0c9-bdcb5c3972e5 | -6.40576 | -43.34806 | 2025-09-17 00:11:00 | TERRA_M-M | BARÃO DE GRAJAÚ | MARANHÃO | Brasil | 2101509 | 21 | 33 | nan | nan | nan | Cerrado | 11.9 |
| 07d2bb79-2fb3-3dc3-89d8-e6704195dc5c | -6.97022 | -44.55608 | 2025-09-17 00:11:00 | TERRA_M-M | SÃO DOMINGOS DO AZEITÃO | MARANHÃO | Brasil | 2110658 | 21 | 33 | nan | nan | nan | Cerrado | 21.7 |
| 6b068778-3942-389b-90ca-533fe72d6d08 | -9.49967 | -37.96898 | 2025-09-17 00:11:00 | TERRA_M-M | DELMIRO GOUVEIA | ALAGOAS | Brasil | 2702405 | 27 | 33 | nan | nan | nan | Caatinga | 9.2 |
| aa3f042a-a4a9-3c81-8d04-c162da66c180 | -8.67604 | -46.39692 | 2025-09-17 00:11:00 | TERRA_M-M | BALSAS | MARANHÃO | Brasil | 2101400 | 21 | 33 | nan | nan | nan | Cerrado | 19.3 |
| b2a32af1-6968-3534-9134-efe7f43b09b5 | -6.04566 | -43.1368 | 2025-09-17 00:11:00 | TERRA_M-M | SÃO FRANCISCO DO MARANHÃO | MARANHÃO | Brasil | 2110906 | 21 | 33 | nan | nan | nan | Caatinga | 10.1 |
| 45b599a1-bbab-3751-a36d-608547cb139c | -11.12273 | -45.11502 | 2025-09-17 00:11:00 | TERRA_M-M | FORMOSA DO RIO PRETO | BAHIA | Brasil | 2911105 | 29 | 33 | nan | nan | nan | Cerrado | 25.7 |
| afa80edd-53d2-3562-87e9-ca0f220a85bc | -12.70304 | -45.81376 | 2025-09-17 00:11:00 | TERRA_M-M | SÃO DESIDÉRIO | BAHIA | Brasil | 2928901 | 29 | 33 | nan | nan | nan | Cerrado | 15.6 |
| 5e1dc7a1-d966-310e-a797-206db436cefe | -12.71023 | -44.67174 | 2025-09-17 00:11:00 | TERRA_M-M | SÃO DESIDÉRIO | BAHIA | Brasil | 2928901 | 29 | 33 | nan | nan | nan | Cerrado | 11.6 |
| c978a467-e507-34ef-8e03-2d49ad250cd2 | -6.2587 | -44.67699 | 2025-09-17 00:11:00 | TERRA_M-M | MIRADOR | MARANHÃO | Brasil | 2106706 | 21 | 33 | nan | nan | nan | Cerrado | 10.3 |
| e48c7d90-d277-3c49-a20c-a2cb4c5a4c51 | -6.22051 | -42.02268 | 2025-09-17 00:11:00 | TERRA_M-M | VALENÇA DO PIAUÍ | PIAUÍ | Brasil | 2211308 | 22 | 33 | nan | nan | nan | Caatinga | 7.1 |
| 5b6937f9-4790-33e7-8cdb-6b138464290f | -8.62908 | -46.43288 | 2025-09-17 00:11:00 | TERRA_M-M | BALSAS | MARANHÃO | Brasil | 2101400 | 21 | 33 | nan | nan | nan | Cerrado | 79.7 |
| 8391d8f5-12db-351b-b51a-3e8e339cf102 | -6.62394 | -45.59966 | 2025-09-17 00:11:00 | TERRA_M-M | MIRADOR | MARANHÃO | Brasil | 2106706 | 21 | 33 | nan | nan | nan | Cerrado | 118.4 |
| 6d4914f6-e62d-3bd8-8d94-2b59af02ce79 | -8.97517 | -44.19613 | 2025-09-17 00:11:00 | TERRA_M-M | SANTA LUZ | PIAUÍ | Brasil | 2209302 | 22 | 33 | nan | nan | nan | Cerrado | 4.8 |
| 25f1bacd-55b4-3dab-8ceb-fa9e076c1cc3 | -12.39652 | -51.39764 | 2025-09-17 00:11:00 | TERRA_M-M | BOM JESUS DO ARAGUAIA | MATO GROSSO | Brasil | 5101852 | 51 | 33 | nan | nan | nan | Cerrado | 54.2 |
| d87b2a8c-b299-3b3e-bb0d-801eeeeadd4d | -12.98088 | -47.95471 | 2025-09-17 00:11:00 | TERRA_M-M | PARANÃ | TOCANTINS | Brasil | 1716208 | 17 | 33 | nan | nan | nan | Cerrado | 19.9 |
| 8ad5ba86-6b9c-3e2e-90e1-2398d026d4e1 | -8.67751 | -46.40843 | 2025-09-17 00:11:00 | TERRA_M-M | BALSAS | MARANHÃO | Brasil | 2101400 | 21 | 33 | nan | nan | nan | Cerrado | 67.8 |
| 5245bc80-9807-3baf-be7d-d8da77d1e98d | -7.61146 | -47.45861 | 2025-09-17 00:11:00 | TERRA_M-M | GOIATINS | TOCANTINS | Brasil | 1709005 | 17 | 33 | nan | nan | nan | Cerrado | 11.6 |
| f941fd39-4ca3-3cad-97c5-0d37f1b520e7 | -12.98701 | -47.94899 | 2025-09-17 00:11:00 | TERRA_M-M | PARANÃ | TOCANTINS | Brasil | 1716208 | 17 | 33 | nan | nan | nan | Cerrado | 10.2 |
| e95f99a6-d1ef-3a45-a4fa-cad990335be2 | -11.03447 | -45.07079 | 2025-09-17 00:11:00 | TERRA_M-M | FORMOSA DO RIO PRETO | BAHIA | Brasil | 2911105 | 29 | 33 | nan | nan | nan | Cerrado | 12.3 |
| 6a3b7296-83a6-307f-99f8-133a98e0f37b | -6.35209 | -43.15667 | 2025-09-17 00:11:00 | TERRA_M-M | SÃO FRANCISCO DO MARANHÃO | MARANHÃO | Brasil | 2110906 | 21 | 33 | nan | nan | nan | Cerrado | 67.8 |
| 695edf18-2acb-37ff-8342-e0e67e3413e0 | -6.61765 | -44.74031 | 2025-09-17 00:11:00 | TERRA_M-M | MIRADOR | MARANHÃO | Brasil | 2106706 | 21 | 33 | nan | nan | nan | Cerrado | 5.1 |
| 0f0b11b1-226e-3d8c-9a84-b7298d9baacf | -12.69276 | -45.09754 | 2025-09-17 00:11:00 | TERRA_M-M | SÃO DESIDÉRIO | BAHIA | Brasil | 2928901 | 29 | 33 | nan | nan | nan | Cerrado | 13.3 |
| 1cc2f945-08c4-32d4-b9e9-d213ba9d8271 | -9.09293 | -44.93081 | 2025-09-17 00:11:00 | TERRA_M-M | BOM JESUS | PIAUÍ | Brasil | 2201903 | 22 | 33 | nan | nan | nan | Cerrado | 29.6 |
| 9ae81f00-5944-3ce7-8334-96c013863a4c | -11.49433 | -43.62238 | 2025-09-17 00:11:00 | TERRA_M-M | BARRA | BAHIA | Brasil | 2902708 | 29 | 33 | nan | nan | nan | Cerrado | 5.6 |
| 5c9fc369-04b3-3b0a-af68-b25b9670c784 | -6.39571 | -43.34044 | 2025-09-17 00:11:00 | TERRA_M-M | BARÃO DE GRAJAÚ | MARANHÃO | Brasil | 2101509 | 21 | 33 | nan | nan | nan | Cerrado | 5.2 |
| 5a20e36a-6b1f-3da0-92d1-6bd6e152731c | -7.61319 | -47.47155 | 2025-09-17 00:11:00 | TERRA_M-M | GOIATINS | TOCANTINS | Brasil | 1709005 | 17 | 33 | nan | nan | nan | Cerrado | 20.5 |
| 1dd133b3-2bba-3c92-b4ad-fcc42cfaaeb6 | -6.97329 | -44.44569 | 2025-09-17 00:11:00 | TERRA_M-M | BENEDITO LEITE | MARANHÃO | Brasil | 2101806 | 21 | 33 | nan | nan | nan | Cerrado | 6.6 |
| e97e7777-1ff1-306f-b3f4-69f8df4495d7 | -9.60053 | -40.57705 | 2025-09-17 00:11:00 | TERRA_M-M | JUAZEIRO | BAHIA | Brasil | 2918407 | 29 | 33 | nan | nan | nan | Caatinga | 6.5 |
| ebb07849-6cf4-3441-826c-6d848a644ae8 | -13.64887 | -44.25874 | 2025-09-17 00:11:00 | TERRA_M-M | CORIBE | BAHIA | Brasil | 2909109 | 29 | 33 | nan | nan | nan | Cerrado | 12.2 |
| ded0dabb-df1e-3ca4-98eb-9ab36ac27a17 | -10.04445 | -47.18768 | 2025-09-17 00:11:00 | TERRA_M-M | NOVO ACORDO | TOCANTINS | Brasil | 1715101 | 17 | 33 | nan | nan | nan | Cerrado | 7.3 |
| 29cbb7d2-02ce-39a5-b17d-194816920143 | -9.11128 | -44.85995 | 2025-09-17 00:11:00 | TERRA_M-M | BOM JESUS | PIAUÍ | Brasil | 2201903 | 22 | 33 | nan | nan | nan | Cerrado | 7.1 |
| 02bd03f7-ce78-3299-a742-b89c8b58f540 | -11.12407 | -45.12525 | 2025-09-17 00:11:00 | TERRA_M-M | FORMOSA DO RIO PRETO | BAHIA | Brasil | 2911105 | 29 | 33 | nan | nan | nan | Cerrado | 9.5 |
| d9719c0c-1c89-3479-8865-37b514719a5e | -9.17457 | -46.93418 | 2025-09-17 00:11:00 | TERRA_M-M | LIZARDA | TOCANTINS | Brasil | 1712405 | 17 | 33 | nan | nan | nan | Cerrado | 22.2 |
| edd06fc7-1238-3586-a4fb-d28a939cf986 | -8.53315 | -48.97818 | 2025-09-17 00:11:00 | TERRA_M-M | PEQUIZEIRO | TOCANTINS | Brasil | 1716653 | 17 | 33 | nan | nan | nan | Amazônia | 17.6 |
| 366fa94d-93eb-3672-869c-68bccde983c3 | -6.88217 | -43.97791 | 2025-09-17 00:11:00 | TERRA_M-M | PORTO ALEGRE DO PIAUÍ | PIAUÍ | Brasil | 2208551 | 22 | 33 | nan | nan | nan | Cerrado | 80.4 |
| d0ec13f2-a813-3503-bf7b-a8ef5bf0e978 | -11.45893 | -43.5622 | 2025-09-17 00:11:00 | TERRA_M-M | BARRA | BAHIA | Brasil | 2902708 | 29 | 33 | nan | nan | nan | Cerrado | 3.9 |
| 992cd1d4-ac1d-35ae-baf4-306c6c8e6dc0 | -5.59931 | -44.11607 | 2025-09-17 00:13:00 | TERRA_M-M | GOVERNADOR LUIZ ROCHA | MARANHÃO | Brasil | 2104628 | 21 | 33 | nan | nan | nan | Cerrado | 26.2 |
| 0d9127ef-44f9-35e5-95ac-9a0f0fcfa4a3 | -2.83553 | -48.64854 | 2025-09-17 00:13:00 | TERRA_M-M | TAILÂNDIA | PARÁ | Brasil | 1507953 | 15 | 33 | nan | nan | nan | Amazônia | 10.7 |
| fcf8e39c-3d62-3310-8d94-9d3b60135c00 | -6.1559 | -44.53327 | 2025-09-17 00:13:00 | TERRA_M-M | MIRADOR | MARANHÃO | Brasil | 2106706 | 21 | 33 | nan | nan | nan | Cerrado | 6.7 |
| bcde8ef0-8c0a-364d-be12-a6cad9ffeaca | -2.2576 | -47.84669 | 2025-09-17 00:13:00 | TERRA_M-M | AURORA DO PARÁ | PARÁ | Brasil | 1500958 | 15 | 33 | nan | nan | nan | Amazônia | 14.1 |
| 4b9d6ec5-50fe-354a-b0a9-9ac9c02c76e1 | -4.06258 | -47.51184 | 2025-09-17 00:13:00 | TERRA_M-M | ULIANÓPOLIS | PARÁ | Brasil | 1508126 | 15 | 33 | nan | nan | nan | Amazônia | 22.2 |
| 9b11e2cf-4fab-3957-814c-8eb7916c262c | -5.49027 | -43.994 | 2025-09-17 00:13:00 | TERRA_M-M | GOVERNADOR LUIZ ROCHA | MARANHÃO | Brasil | 2104628 | 21 | 33 | nan | nan | nan | Cerrado | 31.4 |
| ce2723a1-a89c-3ad5-b22c-68cfa6e01c5d | -5.81028 | -43.49652 | 2025-09-17 00:13:00 | TERRA_M-M | PARNARAMA | MARANHÃO | Brasil | 2107803 | 21 | 33 | nan | nan | nan | Cerrado | 4.8 |
| 7a33e119-5e2c-3f5c-a7a2-7e7f38106d4d | -5.76535 | -43.70652 | 2025-09-17 00:13:00 | TERRA_M-M | BURITI BRAVO | MARANHÃO | Brasil | 2102309 | 21 | 33 | nan | nan | nan | Cerrado | 7.7 |
| ca814265-5218-3059-aa74-6ccdeb6e5129 | -3.69 | -49.02813 | 2025-09-17 00:13:00 | TERRA_M-M | GOIANÉSIA DO PARÁ | PARÁ | Brasil | 1503093 | 15 | 33 | nan | nan | nan | Amazônia | 16.1 |
| c7a7087c-4dea-3bad-abc0-e1af31b2cb64 | -3.39376 | -44.75182 | 2025-09-17 00:13:00 | TERRA_M-M | ARARI | MARANHÃO | Brasil | 2101004 | 21 | 33 | nan | nan | nan | Amazônia | 4.9 |
| c239436e-42d1-3df3-912a-47e10f9a6775 | -5.77573 | -45.52826 | 2025-09-17 00:13:00 | TERRA_M-M | BARRA DO CORDA | MARANHÃO | Brasil | 2101608 | 21 | 33 | nan | nan | nan | Cerrado | 5.4 |
| d71d0810-f87f-3012-82f8-f10fa8b20c8f | -3.23009 | -46.79534 | 2025-09-17 00:13:00 | TERRA_M-M | PARAGOMINAS | PARÁ | Brasil | 1505502 | 15 | 33 | nan | nan | nan | Amazônia | 6.7 |
| fac85eec-2c26-3a73-ab94-065f92cf2158 | -4.93705 | -45.59372 | 2025-09-17 00:13:00 | TERRA_M-M | ARAME | MARANHÃO | Brasil | 2100956 | 21 | 33 | nan | nan | nan | Cerrado | 5.0 |
| 1c3781fb-cae7-3f7f-b27a-121d3147c92e | -1.95643 | -48.11326 | 2025-09-17 00:13:00 | TERRA_M-M | ACARÁ | PARÁ | Brasil | 1500206 | 15 | 33 | nan | nan | nan | Amazônia | 9.1 |
| baa1c330-78d2-3862-92ef-0d3081d507c1 | -5.59712 | -45.36778 | 2025-09-17 00:13:00 | TERRA_M-M | BARRA DO CORDA | MARANHÃO | Brasil | 2101608 | 21 | 33 | nan | nan | nan | Cerrado | 13.2 |
| aff2ebf4-6b9d-3a95-9403-fd26261ac743 | -2.38036 | -47.62893 | 2025-09-17 00:13:00 | TERRA_M-M | IPIXUNA DO PARÁ | PARÁ | Brasil | 1503457 | 15 | 33 | nan | nan | nan | Amazônia | 83.0 |
| 76b31ff8-c273-3b8a-bcac-de93a1b9bd4e | -4.0928 | -44.14874 | 2025-09-17 00:13:00 | TERRA_M-M | COROATÁ | MARANHÃO | Brasil | 2103604 | 21 | 33 | nan | nan | nan | Cerrado | 24.3 |
| afe182c0-9990-3018-8284-a3ef9cf76857 | -2.8373 | -48.66176 | 2025-09-17 00:13:00 | TERRA_M-M | TAILÂNDIA | PARÁ | Brasil | 1507953 | 15 | 33 | nan | nan | nan | Amazônia | 59.8 |
| a55e727e-1441-3d68-a128-f49f4fcee6bd | -5.57092 | -43.44063 | 2025-09-17 00:13:00 | TERRA_M-M | PARNARAMA | MARANHÃO | Brasil | 2107803 | 21 | 33 | nan | nan | nan | Cerrado | 5.3 |
| bd469f72-524d-3c3b-8c75-8c155a1480f0 | -5.79005 | -43.4963 | 2025-09-17 00:13:00 | TERRA_M-M | PARNARAMA | MARANHÃO | Brasil | 2107803 | 21 | 33 | nan | nan | nan | Cerrado | 23.7 |
| 56a26167-f97a-337f-a10d-29fe5ad83120 | -5.87834 | -45.88091 | 2025-09-17 00:13:00 | TERRA_M-M | GRAJAÚ | MARANHÃO | Brasil | 2104800 | 21 | 33 | nan | nan | nan | Cerrado | 5.6 |
| 156bb59c-0ec5-3ee9-8ff0-35340053cbc8 | -5.59838 | -45.37708 | 2025-09-17 00:13:00 | TERRA_M-M | BARRA DO CORDA | MARANHÃO | Brasil | 2101608 | 21 | 33 | nan | nan | nan | Cerrado | 8.1 |
| b5ac1204-bf5d-3082-8b30-9733a6a49ed6 | -5.67374 | -45.05082 | 2025-09-17 00:13:00 | TERRA_M-M | BARRA DO CORDA | MARANHÃO | Brasil | 2101608 | 21 | 33 | nan | nan | nan | Cerrado | 6.1 |
| b24dca58-8397-3763-824b-c77608682259 | -5.89547 | -45.72964 | 2025-09-17 00:13:00 | TERRA_M-M | GRAJAÚ | MARANHÃO | Brasil | 2104800 | 21 | 33 | nan | nan | nan | Cerrado | 4.9 |
| 6d07e4fc-b58e-3caf-ac5e-70dd99a42c89 | -2.92347 | -48.30262 | 2025-09-17 00:13:00 | TERRA_M-M | TOMÉ-AÇU | PARÁ | Brasil | 1508001 | 15 | 33 | nan | nan | nan | Amazônia | 50.6 |
| a32aca65-e6b0-3561-af6c-4fb397ae3251 | -5.78189 | -43.95522 | 2025-09-17 00:13:00 | TERRA_M-M | BURITI BRAVO | MARANHÃO | Brasil | 2102309 | 21 | 33 | nan | nan | nan | Cerrado | 5.6 |
| 280735b5-a90b-37f8-a26b-d10efa11b477 | -5.78883 | -43.48747 | 2025-09-17 00:13:00 | TERRA_M-M | PARNARAMA | MARANHÃO | Brasil | 2107803 | 21 | 33 | nan | nan | nan | Cerrado | 6.3 |
| 69107149-dd3f-3369-8e6e-588085b4e527 | -5.78068 | -43.94643 | 2025-09-17 00:13:00 | TERRA_M-M | BURITI BRAVO | MARANHÃO | Brasil | 2102309 | 21 | 33 | nan | nan | nan | Cerrado | 8.6 |
| 944a02ca-b076-38da-90af-4868fe4c14d5 | -5.4033 | -46.52884 | 2025-09-17 00:13:00 | TERRA_M-M | AMARANTE DO MARANHÃO | MARANHÃO | Brasil | 2100600 | 21 | 33 | nan | nan | nan | Cerrado | 10.4 |
| 1f6cef68-1d33-3cd6-87e1-6ee573c3cb6d | -5.64172 | -48.60972 | 2025-09-17 00:13:00 | TERRA_M-M | SÃO DOMINGOS DO ARAGUAIA | PARÁ | Brasil | 1507151 | 15 | 33 | nan | nan | nan | Amazônia | 19.2 |
| 6f2b0bf5-c158-3796-807f-344970f41733 | -4.92926 | -45.60445 | 2025-09-17 00:13:00 | TERRA_M-M | ARAME | MARANHÃO | Brasil | 2100956 | 21 | 33 | nan | nan | nan | Amazônia | 6.7 |
| fd355b92-fa9d-3e92-a4e2-affd1be33703 | -5.82244 | -46.36735 | 2025-09-17 00:13:00 | TERRA_M-M | GRAJAÚ | MARANHÃO | Brasil | 2104800 | 21 | 33 | nan | nan | nan | Cerrado | 14.9 |
| 1596d99e-94e5-3b8d-a075-6e2f1a986e20 | -3.50599 | -48.4474 | 2025-09-17 00:13:00 | TERRA_M-M | PARAGOMINAS | PARÁ | Brasil | 1505502 | 15 | 33 | nan | nan | nan | Amazônia | 22.5 |
| ad10341f-dd63-3568-b77d-dc3ab800402a | -3.23954 | -46.79404 | 2025-09-17 00:13:00 | TERRA_M-M | PARAGOMINAS | PARÁ | Brasil | 1505502 | 15 | 33 | nan | nan | nan | Amazônia | 69.9 |


[Clique aqui para ver as próximas entradas](README5.md)
