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

## Dados Diários - Página 8

| ID | Latitude | Longitude | Data/Hora GMT | Satélite | Município | Estado | País | Município ID | Estado ID | País ID | Dias sem Chuva | Precipitação | Risco de Fogo | Bioma | FRP |
|----|----------|-----------|---------------|----------|-----------|--------|------|--------------|-----------|---------|----------------|--------------|----------------|-------|-----|
| 7f7d372b-2316-31f1-b2e9-1fe916cb361a | -10.8819 | -54.3127 | 2025-06-10 04:40:00 | NOAA-21 | MARCELÂNDIA | MATO GROSSO | Brasil | 5105580 | 51 | 33 | nan | nan | nan | Amazônia | 3.3 |
| fe0bdb41-59a6-35ee-b6f9-67fda62bc421 | -9.02793 | -51.14101 | 2025-06-10 04:40:00 | NOAA-21 | CUMARU DO NORTE | PARÁ | Brasil | 1502764 | 15 | 33 | nan | nan | nan | Amazônia | 0.8 |
| bfefcb2f-d4f7-386e-b0d9-963587695835 | -9.38865 | -48.42968 | 2025-06-10 04:40:00 | NOAA-21 | MIRACEMA DO TOCANTINS | TOCANTINS | Brasil | 1713205 | 17 | 33 | nan | nan | nan | Cerrado | 0.7 |
| eddcfdb3-aa79-3b74-933f-7470d00fb0cf | -9.02404 | -51.14402 | 2025-06-10 04:40:00 | NOAA-21 | CUMARU DO NORTE | PARÁ | Brasil | 1502764 | 15 | 33 | nan | nan | nan | Amazônia | 0.7 |
| c66bfc54-3357-3633-b05e-03aadd516932 | -10.84372 | -53.77685 | 2025-06-10 04:40:00 | NOAA-21 | MARCELÂNDIA | MATO GROSSO | Brasil | 5105580 | 51 | 33 | nan | nan | nan | Amazônia | 1.1 |
| eba01e0b-85eb-31b6-943f-822bbd813eb3 | -10.4522 | -47.44885 | 2025-06-10 04:40:00 | NOAA-21 | LAGOA DO TOCANTINS | TOCANTINS | Brasil | 1711951 | 17 | 33 | nan | nan | nan | Cerrado | 1.1 |
| fa37c8c3-fbae-3fbd-ae8c-15af533a75b9 | -10.84151 | -53.76773 | 2025-06-10 04:40:00 | NOAA-21 | MARCELÂNDIA | MATO GROSSO | Brasil | 5105580 | 51 | 33 | nan | nan | nan | Amazônia | 8.4 |
| c4326813-b6e4-3fe0-8cf5-5d0def23d9c7 | -9.93834 | -57.49094 | 2025-06-10 04:40:00 | NOAA-21 | NOVA MONTE VERDE | MATO GROSSO | Brasil | 5108956 | 51 | 33 | nan | nan | nan | Amazônia | 2.9 |
| 50e4a74f-42a2-32b8-94df-1348e53db55b | -9.01489 | -49.57859 | 2025-06-10 04:40:00 | NOAA-21 | ARAGUACEMA | TOCANTINS | Brasil | 1701903 | 17 | 33 | nan | nan | nan | Cerrado | 1.7 |
| 1e116d16-588c-3530-b29c-7c45a583b347 | -10.2368 | -49.4825 | 2025-06-10 04:40:00 | NOAA-21 | PIUM | TOCANTINS | Brasil | 1717503 | 17 | 33 | nan | nan | nan | Cerrado | 1.9 |
| a3b1cc82-893c-3e49-84bd-ee7507d78955 | -8.41886 | -48.30232 | 2025-06-10 04:40:00 | NOAA-21 | PRESIDENTE KENNEDY | TOCANTINS | Brasil | 1718402 | 17 | 33 | nan | nan | nan | Cerrado | 2.4 |
| ece6e04b-6352-3890-a03f-830c9d7f6d68 | -12.29397 | -50.10122 | 2025-06-10 04:40:00 | NOAA-21 | SANDOLÂNDIA | TOCANTINS | Brasil | 1718840 | 17 | 33 | nan | nan | nan | Cerrado | 1.8 |
| 477f916d-4ea2-348a-b649-17cb2b7fd18b | -10.64639 | -47.47992 | 2025-06-10 04:40:00 | NOAA-21 | PONTE ALTA DO TOCANTINS | TOCANTINS | Brasil | 1717909 | 17 | 33 | nan | nan | nan | Cerrado | 0.6 |
| 804639bd-a795-3707-8623-aff14dbf2479 | -12.11248 | -49.48503 | 2025-06-10 04:40:00 | NOAA-21 | FORMOSO DO ARAGUAIA | TOCANTINS | Brasil | 1708205 | 17 | 33 | nan | nan | nan | Cerrado | 0.3 |
| 4c279a2d-a2d3-3795-a8b6-d24152a85586 | -10.04758 | -48.66831 | 2025-06-10 04:40:00 | NOAA-21 | MIRACEMA DO TOCANTINS | TOCANTINS | Brasil | 1713205 | 17 | 33 | nan | nan | nan | Cerrado | 7.5 |
| e42542b1-7467-39df-b77e-ee76b65297c0 | -12.29619 | -50.10884 | 2025-06-10 04:40:00 | NOAA-21 | SANDOLÂNDIA | TOCANTINS | Brasil | 1718840 | 17 | 33 | nan | nan | nan | Cerrado | 5.0 |
| c61c91a3-78ed-3b8b-86b5-7ca988f54b9b | -11.49557 | -48.07875 | 2025-06-10 04:40:00 | NOAA-21 | SANTA ROSA DO TOCANTINS | TOCANTINS | Brasil | 1718907 | 17 | 33 | nan | nan | nan | Cerrado | 1.1 |
| fa0ed151-7b9a-341d-a93e-7566a3d133ff | -12.09876 | -44.74838 | 2025-06-10 04:40:00 | NOAA-21 | ANGICAL | BAHIA | Brasil | 2901403 | 29 | 33 | nan | nan | nan | Cerrado | 1.3 |
| 4e5b5460-120e-3685-9283-b1694e7305b0 | -13.50686 | -47.86795 | 2025-06-10 04:40:00 | NOAA-21 | CAVALCANTE | GOIÁS | Brasil | 5205307 | 52 | 33 | nan | nan | nan | Cerrado | 1.5 |
| 62f38739-c739-3f30-8b31-550f73b4d490 | -9.70741 | -57.87559 | 2025-06-10 04:40:00 | NOAA-21 | NOVA BANDEIRANTES | MATO GROSSO | Brasil | 5106158 | 51 | 33 | nan | nan | nan | Amazônia | 2.0 |
| 54f8c144-0aa8-3300-8e54-bb48757fe920 | -13.33269 | -45.46375 | 2025-06-10 04:40:00 | NOAA-21 | CORRENTINA | BAHIA | Brasil | 2909307 | 29 | 33 | nan | nan | nan | Cerrado | 0.6 |
| 114c0630-e21c-3a33-8301-6332ce9671d2 | -11.5902 | -51.34117 | 2025-06-10 04:40:00 | NOAA-21 | SÃO FÉLIX DO ARAGUAIA | MATO GROSSO | Brasil | 5107859 | 51 | 33 | nan | nan | nan | Cerrado | 1.7 |
| 3c3407bb-219a-3683-aab8-770474e27437 | -11.64441 | -58.01221 | 2025-06-10 04:40:00 | NOAA-21 | JUARA | MATO GROSSO | Brasil | 5105101 | 51 | 33 | nan | nan | nan | Amazônia | 1.8 |
| 21e480ce-021d-3f7c-9940-0cf6bc7bb8ca | -6.85042 | -47.84503 | 2025-06-10 04:40:00 | NOAA-21 | DARCINÓPOLIS | TOCANTINS | Brasil | 1706506 | 17 | 33 | nan | nan | nan | Cerrado | 1.1 |
| d7a8ba72-d60d-30d1-b7f0-8f7bb14f05f0 | -10.21693 | -46.93045 | 2025-06-10 04:40:00 | NOAA-21 | MATEIROS | TOCANTINS | Brasil | 1712702 | 17 | 33 | nan | nan | nan | Cerrado | 6.8 |
| 59544a3b-d024-30d9-952a-6fe676d8eaed | -12.69169 | -45.06229 | 2025-06-10 04:40:00 | NOAA-21 | SÃO DESIDÉRIO | BAHIA | Brasil | 2928901 | 29 | 33 | nan | nan | nan | Cerrado | 1.0 |
| 805acce7-ff44-33a6-a741-64cc6f6604aa | -12.60293 | -45.7363 | 2025-06-10 04:40:00 | NOAA-21 | SÃO DESIDÉRIO | BAHIA | Brasil | 2928901 | 29 | 33 | nan | nan | nan | Cerrado | 1.2 |
| 83d85945-f163-3f34-8ef3-a8fae5bbc6d4 | -8.60336 | -46.58328 | 2025-06-10 04:40:00 | NOAA-21 | BALSAS | MARANHÃO | Brasil | 2101400 | 21 | 33 | nan | nan | nan | Cerrado | 1.5 |
| b18c938b-4449-3ff4-be66-05dda93fffb6 | -10.94548 | -55.3242 | 2025-06-10 04:40:00 | NOAA-21 | ITAÚBA | MATO GROSSO | Brasil | 5104559 | 51 | 33 | nan | nan | nan | Amazônia | 1.9 |
| 5f3ce1db-b68d-30fd-a53d-be34a069816d | -8.07979 | -47.12218 | 2025-06-10 04:40:00 | NOAA-21 | GOIATINS | TOCANTINS | Brasil | 1709005 | 17 | 33 | nan | nan | nan | Cerrado | 2.0 |
| f58e1aec-6277-3331-9568-1ba9cc8c2e4f | -10.13302 | -51.66066 | 2025-06-10 04:40:00 | NOAA-21 | CONFRESA | MATO GROSSO | Brasil | 5103353 | 51 | 33 | nan | nan | nan | Amazônia | 1.2 |
| e96ea4af-90ee-3202-9de0-df10cd5311c4 | -9.78125 | -49.19397 | 2025-06-10 04:40:00 | NOAA-21 | DIVINÓPOLIS DO TOCANTINS | TOCANTINS | Brasil | 1707108 | 17 | 33 | nan | nan | nan | Cerrado | 0.9 |
| 0dd7efa0-ab1b-33cf-9416-bcda97076644 | -10.9494 | -55.32489 | 2025-06-10 04:40:00 | NOAA-21 | ITAÚBA | MATO GROSSO | Brasil | 5104559 | 51 | 33 | nan | nan | nan | Amazônia | 1.9 |
| 015bf9a0-404d-3e0e-8506-f5756a5fecea | -10.83721 | -53.77138 | 2025-06-10 04:40:00 | NOAA-21 | MARCELÂNDIA | MATO GROSSO | Brasil | 5105580 | 51 | 33 | nan | nan | nan | Amazônia | 2.1 |
| c7cab719-751e-3f6a-8430-7d00b7cc1c63 | -11.62968 | -47.68375 | 2025-06-10 04:40:00 | NOAA-21 | NATIVIDADE | TOCANTINS | Brasil | 1714203 | 17 | 33 | nan | nan | nan | Cerrado | 3.2 |
| 2ec68d7a-2f43-380d-b549-b3ba93ff9aab | -14.19548 | -45.49312 | 2025-06-10 04:40:00 | NOAA-21 | JABORANDI | BAHIA | Brasil | 2917359 | 29 | 33 | nan | nan | nan | Cerrado | 1.9 |
| 715b7566-f375-3572-b64d-be6d127a9491 | -7.47356 | -45.50576 | 2025-06-10 04:40:00 | NOAA-21 | LORETO | MARANHÃO | Brasil | 2106102 | 21 | 33 | nan | nan | nan | Cerrado | 9.9 |
| 3324f824-5d2c-337f-97d3-c0f6979aa019 | -11.58745 | -51.33712 | 2025-06-10 04:40:00 | NOAA-21 | SÃO FÉLIX DO ARAGUAIA | MATO GROSSO | Brasil | 5107859 | 51 | 33 | nan | nan | nan | Cerrado | 1.7 |
| cbb6860b-cd97-3840-b93c-3ec93e3aa4fd | -14.19601 | -45.48911 | 2025-06-10 04:40:00 | NOAA-21 | JABORANDI | BAHIA | Brasil | 2917359 | 29 | 33 | nan | nan | nan | Cerrado | 1.9 |
| 6ff95c65-4c21-37ce-845f-40728f8379c5 | -12.13121 | -54.65717 | 2025-06-10 04:40:00 | NOAA-21 | FELIZ NATAL | MATO GROSSO | Brasil | 5103700 | 51 | 33 | nan | nan | nan | Amazônia | 1.6 |
| 15ddd085-c3fa-3748-9a1a-820afd28d837 | -8.70596 | -47.14828 | 2025-06-10 04:40:00 | NOAA-21 | RECURSOLÂNDIA | TOCANTINS | Brasil | 1718501 | 17 | 33 | nan | nan | nan | Cerrado | 0.7 |
| dd8e90df-6398-3cff-97de-b6651cfc58c8 | -13.09657 | -52.28935 | 2025-06-10 04:40:00 | NOAA-21 | QUERÊNCIA | MATO GROSSO | Brasil | 5107065 | 51 | 33 | nan | nan | nan | Amazônia | 1.4 |
| 89f49735-a95f-354a-8b3b-a211d9fbdb11 | -10.22058 | -46.93102 | 2025-06-10 04:40:00 | NOAA-21 | MATEIROS | TOCANTINS | Brasil | 1712702 | 17 | 33 | nan | nan | nan | Cerrado | 6.8 |
| 8350dc10-09c4-38c1-b94a-f160ef3a692c | -10.05152 | -48.66514 | 2025-06-10 04:40:00 | NOAA-21 | MIRACEMA DO TOCANTINS | TOCANTINS | Brasil | 1713205 | 17 | 33 | nan | nan | nan | Cerrado | 7.5 |
| da55766b-4a04-3a51-9c5a-8c18969b4546 | -11.57756 | -44.87763 | 2025-06-10 04:40:00 | NOAA-21 | RIACHÃO DAS NEVES | BAHIA | Brasil | 2926202 | 29 | 33 | nan | nan | nan | Cerrado | 0.9 |
| 18f1b502-2a3b-3fdb-9050-917b4fe63a00 | -10.22487 | -46.92723 | 2025-06-10 04:40:00 | NOAA-21 | MATEIROS | TOCANTINS | Brasil | 1712702 | 17 | 33 | nan | nan | nan | Cerrado | 6.6 |
| 8db4f17f-fc43-3310-9cb4-0255b429d17d | -10.36666 | -57.49996 | 2025-06-10 04:40:00 | NOAA-21 | JUARA | MATO GROSSO | Brasil | 5105101 | 51 | 33 | nan | nan | nan | Amazônia | 1.9 |
| 85fc2cd3-182f-3e8c-a056-4ee629917174 | -10.86715 | -53.77946 | 2025-06-10 04:40:00 | NOAA-21 | MARCELÂNDIA | MATO GROSSO | Brasil | 5105580 | 51 | 33 | nan | nan | nan | Amazônia | 2.1 |
| 4b44273d-0d4f-3541-80e3-fee254df9209 | -10.1291 | -51.66372 | 2025-06-10 04:40:00 | NOAA-21 | CONFRESA | MATO GROSSO | Brasil | 5103353 | 51 | 33 | nan | nan | nan | Amazônia | 0.9 |
| 93b0d194-5dcb-3f6e-a6ec-559662c940b3 | -13.07083 | -49.23989 | 2025-06-10 04:40:00 | NOAA-21 | PORANGATU | GOIÁS | Brasil | 5218003 | 52 | 33 | nan | nan | nan | Cerrado | 1.1 |
| a8263196-1ff5-3454-9a69-945bfa74ba95 | -9.67455 | -49.73291 | 2025-06-10 04:40:00 | NOAA-21 | MARIANÓPOLIS DO TOCANTINS | TOCANTINS | Brasil | 1712504 | 17 | 33 | nan | nan | nan | Cerrado | 1.0 |
| 83b7bbd9-2f95-3e9f-9264-463ac2caf0bc | -9.92089 | -49.83236 | 2025-06-10 04:40:00 | NOAA-21 | PIUM | TOCANTINS | Brasil | 1717503 | 17 | 33 | nan | nan | nan | Cerrado | 0.6 |
| 9435371a-d0e9-321f-b2b0-cbe06784c5e6 | -10.3559 | -51.99457 | 2025-06-10 04:40:00 | NOAA-21 | CONFRESA | MATO GROSSO | Brasil | 5103353 | 51 | 33 | nan | nan | nan | Amazônia | 0.4 |
| c77cbf45-988d-3b16-8762-9e9f52499196 | -10.84081 | -53.77199 | 2025-06-10 04:40:00 | NOAA-21 | MARCELÂNDIA | MATO GROSSO | Brasil | 5105580 | 51 | 33 | nan | nan | nan | Amazônia | 8.4 |
| b38c9233-19a9-3e47-8608-8bd40d776469 | -11.58127 | -47.62243 | 2025-06-10 04:40:00 | NOAA-21 | NATIVIDADE | TOCANTINS | Brasil | 1714203 | 17 | 33 | nan | nan | nan | Cerrado | 1.1 |
| f81b50f8-7dd2-39aa-9faf-eaee738f859f | -11.06476 | -55.0473 | 2025-06-10 04:40:00 | NOAA-21 | ITAÚBA | MATO GROSSO | Brasil | 5104559 | 51 | 33 | nan | nan | nan | Amazônia | 0.9 |
| 39112ed2-92d9-32b4-8da5-50c8f5adf12a | -9.41339 | -48.43294 | 2025-06-10 04:40:00 | NOAA-21 | MIRACEMA DO TOCANTINS | TOCANTINS | Brasil | 1713205 | 17 | 33 | nan | nan | nan | Cerrado | 1.3 |
| e7651b62-8aa6-37cb-8237-e5de5e310780 | -12.10304 | -44.74907 | 2025-06-10 04:40:00 | NOAA-21 | ANGICAL | BAHIA | Brasil | 2901403 | 29 | 33 | nan | nan | nan | Cerrado | 1.3 |
| ca88642e-eeee-323f-86f5-e7a8517dcd2d | -10.21265 | -46.93419 | 2025-06-10 04:40:00 | NOAA-21 | MATEIROS | TOCANTINS | Brasil | 1712702 | 17 | 33 | nan | nan | nan | Cerrado | 13.6 |
| 320204ea-8bff-38d5-b267-7cea05b62893 | -8.08041 | -47.11812 | 2025-06-10 04:40:00 | NOAA-21 | GOIATINS | TOCANTINS | Brasil | 1709005 | 17 | 33 | nan | nan | nan | Cerrado | 2.0 |
| 811e9927-7b93-3da2-bb43-f6481ba5d641 | -11.7692 | -54.37926 | 2025-06-10 04:40:00 | NOAA-21 | UNIÃO DO SUL | MATO GROSSO | Brasil | 5108303 | 51 | 33 | nan | nan | nan | Amazônia | 4.0 |
| 8d481cab-0c40-3dd0-adb3-f3fb08a2980d | -8.34098 | -48.45066 | 2025-06-10 04:40:00 | NOAA-21 | BRASILÂNDIA DO TOCANTINS | TOCANTINS | Brasil | 1703602 | 17 | 33 | nan | nan | nan | Cerrado | 0.9 |
| 54121390-1fbc-382f-ab68-ff0cf94a2fe9 | -14.1918 | -45.48853 | 2025-06-10 04:40:00 | NOAA-21 | JABORANDI | BAHIA | Brasil | 2917359 | 29 | 33 | nan | nan | nan | Cerrado | 1.9 |
| 0ef4e709-bee4-3a7c-8726-ca0b66cd7472 | -11.9067 | -54.82886 | 2025-06-10 04:40:00 | NOAA-21 | SANTA CARMEM | MATO GROSSO | Brasil | 5107248 | 51 | 33 | nan | nan | nan | Amazônia | 3.1 |
| b7687063-df95-3185-947d-49355968d010 | -12.10069 | -44.74657 | 2025-06-10 04:40:00 | NOAA-21 | ANGICAL | BAHIA | Brasil | 2901403 | 29 | 33 | nan | nan | nan | Cerrado | 1.7 |
| fe3cc14a-ede8-3c3c-a080-dd8f58a4e0bf | -10.05491 | -48.66565 | 2025-06-10 04:40:00 | NOAA-21 | MIRACEMA DO TOCANTINS | TOCANTINS | Brasil | 1713205 | 17 | 33 | nan | nan | nan | Cerrado | 13.2 |
| 5340b06b-521a-3354-9624-f36aed627332 | -11.56823 | -47.43521 | 2025-06-10 04:40:00 | NOAA-21 | NATIVIDADE | TOCANTINS | Brasil | 1714203 | 17 | 33 | nan | nan | nan | Cerrado | 2.4 |
| dd41024c-e20e-352c-b80d-247d0ccf7c9f | -12.29674 | -50.1053 | 2025-06-10 04:40:00 | NOAA-21 | SANDOLÂNDIA | TOCANTINS | Brasil | 1718840 | 17 | 33 | nan | nan | nan | Cerrado | 5.0 |
| 6819a662-0bab-36c0-8d3e-b4bdbf24678b | -12.25035 | -51.42784 | 2025-06-10 04:40:00 | NOAA-21 | BOM JESUS DO ARAGUAIA | MATO GROSSO | Brasil | 5101852 | 51 | 33 | nan | nan | nan | Cerrado | 0.8 |
| e2b25317-7a95-344d-ac2b-f0f7245a3f59 | -12.7235 | -54.9716 | 2025-06-10 04:40:00 | NOAA-21 | FELIZ NATAL | MATO GROSSO | Brasil | 5103700 | 51 | 33 | nan | nan | nan | Amazônia | 10.7 |
| 91dd8a65-60e7-38fd-acdb-482d94f0877d | -10.27346 | -47.60743 | 2025-06-10 04:40:00 | NOAA-21 | LAGOA DO TOCANTINS | TOCANTINS | Brasil | 1711951 | 17 | 33 | nan | nan | nan | Cerrado | 2.6 |
| 933e48af-a5fd-34d4-87c6-cfcfb8223205 | -11.76777 | -54.36542 | 2025-06-10 04:40:00 | NOAA-21 | UNIÃO DO SUL | MATO GROSSO | Brasil | 5108303 | 51 | 33 | nan | nan | nan | Amazônia | 2.8 |
| 2de0bef3-0018-3686-8187-98a3c58b4d7d | -14.20916 | -45.48688 | 2025-06-10 04:40:00 | NOAA-21 | JABORANDI | BAHIA | Brasil | 2917359 | 29 | 33 | nan | nan | nan | Cerrado | 1.1 |
| eaf782b3-9897-3466-8f78-b9ac8571d078 | -6.86231 | -47.85812 | 2025-06-10 04:40:00 | NOAA-21 | DARCINÓPOLIS | TOCANTINS | Brasil | 1706506 | 17 | 33 | nan | nan | nan | Cerrado | 1.6 |
| 22a9a975-aad7-3767-a93c-4187f3b9d929 | -7.7022 | -45.77064 | 2025-06-10 04:40:00 | NOAA-21 | SAMBAÍBA | MARANHÃO | Brasil | 2109700 | 21 | 33 | nan | nan | nan | Cerrado | 1.3 |
| ae858c92-bf24-3f60-96f6-931783f5c6e5 | -9.0246 | -51.14048 | 2025-06-10 04:40:00 | NOAA-21 | CUMARU DO NORTE | PARÁ | Brasil | 1502764 | 15 | 33 | nan | nan | nan | Amazônia | 0.8 |
| 82de8348-4050-30be-a422-6dce4f9f2e1a | -12.13415 | -54.6623 | 2025-06-10 04:40:00 | NOAA-21 | FELIZ NATAL | MATO GROSSO | Brasil | 5103700 | 51 | 33 | nan | nan | nan | Amazônia | 1.1 |
| 9cb218ef-55e9-38a6-b9d3-0ad01d47c357 | -12.60435 | -48.36719 | 2025-06-10 04:40:00 | NOAA-21 | SÃO SALVADOR DO TOCANTINS | TOCANTINS | Brasil | 1720259 | 17 | 33 | nan | nan | nan | Cerrado | 0.6 |
| f86afe7a-90b1-35ae-9f80-e875104760a6 | -9.38015 | -48.41702 | 2025-06-10 04:40:00 | NOAA-21 | MIRACEMA DO TOCANTINS | TOCANTINS | Brasil | 1713205 | 17 | 33 | nan | nan | nan | Cerrado | 1.4 |
| b1555051-b03e-30a1-bbe4-190bed7e068b | -12.22977 | -44.19059 | 2025-06-10 04:40:00 | NOAA-21 | CRISTÓPOLIS | BAHIA | Brasil | 2909703 | 29 | 33 | nan | nan | nan | Cerrado | 1.2 |
| 11dc4211-d17a-30b2-9b26-7fcc08f0cf6a | -8.90009 | -48.8458 | 2025-06-10 04:40:00 | NOAA-21 | GOIANORTE | TOCANTINS | Brasil | 1708304 | 17 | 33 | nan | nan | nan | Cerrado | 0.8 |
| 99e81585-7d36-3e23-828f-2e737b6420f7 | -7.27731 | -49.57378 | 2025-06-10 04:40:00 | NOAA-21 | RIO MARIA | PARÁ | Brasil | 1506161 | 15 | 33 | nan | nan | nan | Amazônia | 1.3 |
| 56bd58da-ac7d-3ecb-a943-cb1e3a52919d | -7.77479 | -43.05783 | 2025-06-10 04:40:00 | NOAA-21 | RIO GRANDE DO PIAUÍ | PIAUÍ | Brasil | 2209005 | 22 | 33 | nan | nan | nan | Caatinga | 1.6 |
| ab2d61ed-7ba3-3e28-ad88-3dfc06027ef5 | -10.2163 | -46.93478 | 2025-06-10 04:40:00 | NOAA-21 | MATEIROS | TOCANTINS | Brasil | 1712702 | 17 | 33 | nan | nan | nan | Cerrado | 1.3 |
| 62b67657-7d45-37f0-a801-ca72569d16e6 | -11.06688 | -55.04583 | 2025-06-10 04:40:00 | NOAA-21 | ITAÚBA | MATO GROSSO | Brasil | 5104559 | 51 | 33 | nan | nan | nan | Amazônia | 1.9 |
| 28b0f0df-7f57-3372-9a4f-d6e7978648e1 | -10.83908 | -53.77026 | 2025-06-10 04:40:00 | NOAA-21 | MARCELÂNDIA | MATO GROSSO | Brasil | 5105580 | 51 | 33 | nan | nan | nan | Amazônia | 9.1 |
| a0796db0-7965-3309-b596-5d71b5bac78d | -10.01074 | -48.67445 | 2025-06-10 04:40:00 | NOAA-21 | MIRACEMA DO TOCANTINS | TOCANTINS | Brasil | 1713205 | 17 | 33 | nan | nan | nan | Cerrado | 3.8 |
| 7fd37e84-3d5d-310d-84ad-507beb26f43e | -14.21811 | -45.48413 | 2025-06-10 04:40:00 | NOAA-21 | JABORANDI | BAHIA | Brasil | 2917359 | 29 | 33 | nan | nan | nan | Cerrado | 1.1 |
| cfead832-5b2c-36f2-86fd-2722b23cd876 | -7.4361 | -45.79117 | 2025-06-10 04:40:00 | NOAA-21 | BALSAS | MARANHÃO | Brasil | 2101400 | 21 | 33 | nan | nan | nan | Cerrado | 2.2 |
| be28df0c-e3c9-387c-b408-f676b2df0ecd | -12.13338 | -54.66679 | 2025-06-10 04:40:00 | NOAA-21 | FELIZ NATAL | MATO GROSSO | Brasil | 5103700 | 51 | 33 | nan | nan | nan | Amazônia | 1.1 |
| 0e132554-4e95-359a-b400-04457469c5fe | -9.54658 | -47.50758 | 2025-06-10 04:40:00 | NOAA-21 | RIO SONO | TOCANTINS | Brasil | 1718758 | 17 | 33 | nan | nan | nan | Cerrado | 1.0 |
| 291676f5-762b-316f-bb6b-96a5426e4c1d | -9.03126 | -51.14155 | 2025-06-10 04:40:00 | NOAA-21 | CUMARU DO NORTE | PARÁ | Brasil | 1502764 | 15 | 33 | nan | nan | nan | Amazônia | 0.7 |
| a257ad38-7670-3241-82f9-294bffc99de0 | -11.06052 | -44.27436 | 2025-06-10 04:40:00 | NOAA-21 | SANTA RITA DE CÁSSIA | BAHIA | Brasil | 2928406 | 29 | 33 | nan | nan | nan | Cerrado | 0.9 |
| 33fef642-afb0-3137-bb95-65f077bc7c26 | -8.96407 | -47.96871 | 2025-06-10 04:40:00 | NOAA-21 | BOM JESUS DO TOCANTINS | TOCANTINS | Brasil | 1703305 | 17 | 33 | nan | nan | nan | Cerrado | 6.0 |
| bf55db69-60b9-3ed3-a59f-fc7bcca666cd | -7.09182 | -46.44959 | 2025-06-10 04:40:00 | NOAA-21 | RIACHÃO | MARANHÃO | Brasil | 2109502 | 21 | 33 | nan | nan | nan | Cerrado | 1.6 |
| b841f59d-36ec-3c4f-a731-dbedaee4656b | -12.42489 | -47.80462 | 2025-06-10 04:40:00 | NOAA-21 | PARANÃ | TOCANTINS | Brasil | 1716208 | 17 | 33 | nan | nan | nan | Cerrado | 5.4 |
| 8e25cc25-081f-3c59-a494-390cad53ad09 | -7.77544 | -43.05328 | 2025-06-10 04:40:00 | NOAA-21 | RIO GRANDE DO PIAUÍ | PIAUÍ | Brasil | 2209005 | 22 | 33 | nan | nan | nan | Caatinga | 1.6 |
| 5522d4df-1819-336a-8153-075a1774fd35 | -12.42596 | -47.80664 | 2025-06-10 04:40:00 | NOAA-21 | PARANÃ | TOCANTINS | Brasil | 1716208 | 17 | 33 | nan | nan | nan | Cerrado | 3.6 |
| 2d56473a-68e1-3efe-ab7f-7f657d375710 | -13.0829 | -47.42906 | 2025-06-10 04:40:00 | NOAA-21 | PARANÃ | TOCANTINS | Brasil | 1716208 | 17 | 33 | nan | nan | nan | Cerrado | 2.6 |
| ba0b2dcb-7e76-37cf-ae4d-f860473a9f38 | -10.37038 | -57.50554 | 2025-06-10 04:40:00 | NOAA-21 | JUARA | MATO GROSSO | Brasil | 5105101 | 51 | 33 | nan | nan | nan | Amazônia | 4.8 |


[Clique aqui para ver as próximas entradas](README9.md)
