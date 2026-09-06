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

## Dados Diários - Página 17

| ID | Latitude | Longitude | Data/Hora GMT | Satélite | Município | Estado | País | Município ID | Estado ID | País ID | Dias sem Chuva | Precipitação | Risco de Fogo | Bioma | FRP |
|----|----------|-----------|---------------|----------|-----------|--------|------|--------------|-----------|---------|----------------|--------------|----------------|-------|-----|
| 63a8ec88-6863-3689-8f13-f5afa6fbf8b9 | -5.37363 | -56.04012 | 2026-09-06 04:46:00 | NOAA-21 | TRAIRÃO | PARÁ | Brasil | 1508050 | 15 | 33 | nan | nan | nan | Amazônia | 5.0 |
| 29a02b4d-3ff6-3300-afa8-ad0293026376 | -3.55288 | -48.18643 | 2026-09-06 04:46:00 | NOAA-21 | PARAGOMINAS | PARÁ | Brasil | 1505502 | 15 | 33 | nan | nan | nan | Amazônia | 2.8 |
| 7be40238-3bb4-3201-928c-7d1e1179f3fb | -11.2873 | -45.71124 | 2026-09-06 04:46:00 | NOAA-21 | FORMOSA DO RIO PRETO | BAHIA | Brasil | 2911105 | 29 | 33 | nan | nan | nan | Cerrado | 2.5 |
| 04a8c0b7-c5c0-3f68-9c99-b9cc5b80c203 | -5.35863 | -56.03033 | 2026-09-06 04:46:00 | NOAA-21 | TRAIRÃO | PARÁ | Brasil | 1508050 | 15 | 33 | nan | nan | nan | Amazônia | 3.3 |
| df582429-e58c-3f78-9be2-3f630474e6ec | -11.28875 | -45.70873 | 2026-09-06 04:46:00 | NOAA-21 | FORMOSA DO RIO PRETO | BAHIA | Brasil | 2911105 | 29 | 33 | nan | nan | nan | Cerrado | 2.1 |
| 680e6e8f-ec98-378d-9bb7-1c3761113bbe | -5.1436 | -56.27037 | 2026-09-06 04:46:00 | NOAA-21 | TRAIRÃO | PARÁ | Brasil | 1508050 | 15 | 33 | nan | nan | nan | Amazônia | 13.3 |
| f5bc5da5-8a2b-3b3a-a2d1-7721986a6bfc | -7.7361 | -44.30904 | 2026-09-06 04:46:00 | NOAA-21 | URUÇUÍ | PIAUÍ | Brasil | 2211209 | 22 | 33 | nan | nan | nan | Cerrado | 1.1 |
| 7a421773-f459-3e91-a34d-9c38282cd590 | -3.788 | -55.87809 | 2026-09-06 04:46:00 | NOAA-21 | AVEIRO | PARÁ | Brasil | 1501006 | 15 | 33 | nan | nan | nan | Amazônia | 1.1 |
| 9c85cd4f-1c5e-3564-be62-4697734d0369 | -10.65601 | -45.09581 | 2026-09-06 04:46:00 | NOAA-21 | CRISTALÂNDIA DO PIAUÍ | PIAUÍ | Brasil | 2203008 | 22 | 33 | nan | nan | nan | Cerrado | 1.5 |
| 514cea0c-a6ad-3bea-9670-54ed46b1b2a1 | -11.31885 | -45.10197 | 2026-09-06 04:46:00 | NOAA-21 | FORMOSA DO RIO PRETO | BAHIA | Brasil | 2911105 | 29 | 33 | nan | nan | nan | Cerrado | 3.4 |
| ec2b7c31-a6b7-374b-9c74-fb2d2cd2ca48 | -5.35575 | -56.02256 | 2026-09-06 04:46:00 | NOAA-21 | TRAIRÃO | PARÁ | Brasil | 1508050 | 15 | 33 | nan | nan | nan | Amazônia | 5.2 |
| 75fa9f87-9bae-3781-9532-33fe81f3de1d | -4.92593 | -55.81693 | 2026-09-06 04:46:00 | NOAA-21 | TRAIRÃO | PARÁ | Brasil | 1508050 | 15 | 33 | nan | nan | nan | Amazônia | 1.2 |
| 06357e03-709e-318e-aebd-27f39d6aaf54 | -11.27543 | -45.70657 | 2026-09-06 04:46:00 | NOAA-21 | FORMOSA DO RIO PRETO | BAHIA | Brasil | 2911105 | 29 | 33 | nan | nan | nan | Cerrado | 2.6 |
| 02d41e1e-fa00-3b56-9fa9-c21657603974 | -4.11277 | -49.08604 | 2026-09-06 04:46:00 | NOAA-21 | GOIANÉSIA DO PARÁ | PARÁ | Brasil | 1503093 | 15 | 33 | nan | nan | nan | Amazônia | 2.8 |
| 9cb9212e-7d34-32bc-b906-25d7fa062ab8 | -2.4602 | -57.91202 | 2026-09-06 04:46:00 | NOAA-21 | SÃO SEBASTIÃO DO UATUMÃ | AMAZONAS | Brasil | 1303957 | 13 | 33 | nan | nan | nan | Amazônia | 11.8 |
| 5b0aa667-e460-35b1-889e-7f3b15cfcc90 | -4.66988 | -55.63958 | 2026-09-06 04:46:00 | NOAA-21 | ITAITUBA | PARÁ | Brasil | 1503606 | 15 | 33 | nan | nan | nan | Amazônia | 2.1 |
| 1f49496a-abf3-3381-ba27-b12ed7785f09 | -4.63647 | -48.6408 | 2026-09-06 04:46:00 | NOAA-21 | RONDON DO PARÁ | PARÁ | Brasil | 1506187 | 15 | 33 | nan | nan | nan | Amazônia | 1.4 |
| d0ad5764-5c2d-3011-aa69-91396d294c27 | -5.65604 | -60.23796 | 2026-09-06 04:46:00 | NOAA-21 | NOVO ARIPUANÃ | AMAZONAS | Brasil | 1303304 | 13 | 33 | nan | nan | nan | Amazônia | 2.2 |
| 3da2b282-716e-3eaa-8113-f53f00b9193f | -5.34595 | -56.03184 | 2026-09-06 04:46:00 | NOAA-21 | TRAIRÃO | PARÁ | Brasil | 1508050 | 15 | 33 | nan | nan | nan | Amazônia | 1.3 |
| 25e90168-b807-3ff3-a30a-b215ae4e3169 | -4.35088 | -48.97336 | 2026-09-06 04:46:00 | NOAA-21 | GOIANÉSIA DO PARÁ | PARÁ | Brasil | 1503093 | 15 | 33 | nan | nan | nan | Amazônia | 1.6 |
| d5c22de4-1ca4-3ba9-982c-68de6ce3d51a | -3.15307 | -59.14911 | 2026-09-06 04:46:00 | NOAA-21 | ITACOATIARA | AMAZONAS | Brasil | 1301902 | 13 | 33 | nan | nan | nan | Amazônia | 4.5 |
| c40d9c4a-9792-3280-9167-92bcbf168d1d | -7.09998 | -56.51833 | 2026-09-06 04:46:00 | NOAA-21 | ITAITUBA | PARÁ | Brasil | 1503606 | 15 | 33 | nan | nan | nan | Amazônia | 2.2 |
| 10c5a837-e615-3e9c-b247-e433df858f97 | -4.54794 | -55.98228 | 2026-09-06 04:46:00 | NOAA-21 | ITAITUBA | PARÁ | Brasil | 1503606 | 15 | 33 | nan | nan | nan | Amazônia | 1.0 |
| d62cf7ae-abf7-3642-af51-19cf5eeca053 | -5.30732 | -56.01466 | 2026-09-06 04:46:00 | NOAA-21 | TRAIRÃO | PARÁ | Brasil | 1508050 | 15 | 33 | nan | nan | nan | Amazônia | 1.6 |
| 0c2679c0-5ac6-35e3-87ba-536d330ed5ca | -11.28908 | -45.69741 | 2026-09-06 04:46:00 | NOAA-21 | FORMOSA DO RIO PRETO | BAHIA | Brasil | 2911105 | 29 | 33 | nan | nan | nan | Cerrado | 1.1 |
| 7f29d471-91b2-3882-980f-22b0ea9be204 | -3.859 | -51.03051 | 2026-09-06 04:46:00 | NOAA-21 | PACAJÁ | PARÁ | Brasil | 1505486 | 15 | 33 | nan | nan | nan | Amazônia | 1.5 |
| d1319848-4452-3211-a75d-aba71a3ad818 | -3.54305 | -48.18099 | 2026-09-06 04:46:00 | NOAA-21 | PARAGOMINAS | PARÁ | Brasil | 1505502 | 15 | 33 | nan | nan | nan | Amazônia | 2.3 |
| 0a9c3699-4fcb-3f5d-afb1-130b7f162a96 | -6.02008 | -57.69712 | 2026-09-06 04:46:00 | NOAA-21 | JACAREACANGA | PARÁ | Brasil | 1503754 | 15 | 33 | nan | nan | nan | Amazônia | 4.3 |
| 80388da2-75b9-3308-aed0-0ee7cb3ee0df | -6.63909 | -59.44072 | 2026-09-06 04:46:00 | NOAA-21 | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 1.5 |
| 8f3d21b0-b67d-32f1-9a7f-d6d9092986f7 | -4.16514 | -47.83477 | 2026-09-06 04:46:00 | NOAA-21 | DOM ELISEU | PARÁ | Brasil | 1502939 | 15 | 33 | nan | nan | nan | Amazônia | 1.0 |
| 5e547941-5163-3f72-b361-dea4273eb09f | -5.35172 | -56.02187 | 2026-09-06 04:46:00 | NOAA-21 | TRAIRÃO | PARÁ | Brasil | 1508050 | 15 | 33 | nan | nan | nan | Amazônia | 2.0 |
| 9ec422af-6f98-3172-b225-bcb62ee90e7c | -6.87161 | -55.60706 | 2026-09-06 04:46:00 | NOAA-21 | NOVO PROGRESSO | PARÁ | Brasil | 1505031 | 15 | 33 | nan | nan | nan | Amazônia | 6.9 |
| f3cc9fd7-8cd0-388f-8c9f-1b2002e4dc2d | -3.77035 | -61.76362 | 2026-09-06 04:46:00 | NOAA-21 | ANORI | AMAZONAS | Brasil | 1300102 | 13 | 33 | nan | nan | nan | Amazônia | 1.6 |
| e9e7ee66-fd88-34b0-85b1-121d7350e44c | -6.206 | -57.77148 | 2026-09-06 04:46:00 | NOAA-21 | JACAREACANGA | PARÁ | Brasil | 1503754 | 15 | 33 | nan | nan | nan | Amazônia | 1.4 |
| 2e50680d-9001-32dc-b8fc-1f043b352e13 | -5.28486 | -60.13054 | 2026-09-06 04:46:00 | NOAA-21 | NOVO ARIPUANÃ | AMAZONAS | Brasil | 1303304 | 13 | 33 | nan | nan | nan | Amazônia | 2.6 |
| bc43feec-2a14-305c-83ab-d628908d7994 | -5.25168 | -59.98106 | 2026-09-06 04:46:00 | NOAA-21 | NOVO ARIPUANÃ | AMAZONAS | Brasil | 1303304 | 13 | 33 | nan | nan | nan | Amazônia | 2.2 |
| 14457fa4-c303-3049-aed8-fb557d15b0fd | -4.81774 | -49.38511 | 2026-09-06 04:46:00 | NOAA-21 | NOVA IPIXUNA | PARÁ | Brasil | 1504976 | 15 | 33 | nan | nan | nan | Amazônia | 1.8 |
| 51a23c8c-5a83-3d35-9d1f-ca45131b91c9 | -4.1326 | -56.341 | 2026-09-06 04:46:00 | NOAA-21 | AVEIRO | PARÁ | Brasil | 1501006 | 15 | 33 | nan | nan | nan | Amazônia | 1.3 |
| 18843551-e903-3f8e-8e7a-cf6d87a96b7c | -6.86111 | -46.4611 | 2026-09-06 04:46:00 | NOAA-21 | SÃO PEDRO DOS CRENTES | MARANHÃO | Brasil | 2111573 | 21 | 33 | nan | nan | nan | Cerrado | 1.0 |
| ceb068a6-1653-3f05-b118-1cd78e543347 | -7.37365 | -47.75893 | 2026-09-06 04:46:00 | NOAA-21 | FILADÉLFIA | TOCANTINS | Brasil | 1707702 | 17 | 33 | nan | nan | nan | Cerrado | 2.4 |
| 4f670d02-3038-3d86-aff3-75b1c8ba3a61 | -4.67556 | -55.62962 | 2026-09-06 04:46:00 | NOAA-21 | ITAITUBA | PARÁ | Brasil | 1503606 | 15 | 33 | nan | nan | nan | Amazônia | 2.6 |
| eb192e90-90a9-3dfb-b595-35dd5e344188 | -3.54594 | -48.18535 | 2026-09-06 04:46:00 | NOAA-21 | PARAGOMINAS | PARÁ | Brasil | 1505502 | 15 | 33 | nan | nan | nan | Amazônia | 7.9 |
| a8376512-4ff5-3473-bcb0-821e193bda9b | -5.36037 | -56.04521 | 2026-09-06 04:46:00 | NOAA-21 | TRAIRÃO | PARÁ | Brasil | 1508050 | 15 | 33 | nan | nan | nan | Amazônia | 1.6 |
| f241cf29-334c-315a-a399-7ad5a7ba74cd | -4.9795 | -56.00088 | 2026-09-06 04:46:00 | NOAA-21 | TRAIRÃO | PARÁ | Brasil | 1508050 | 15 | 33 | nan | nan | nan | Amazônia | 1.0 |
| 3c9a3243-8ae0-3ab6-b08d-088286aec7c8 | -5.29135 | -45.13948 | 2026-09-06 04:46:00 | NOAA-21 | BARRA DO CORDA | MARANHÃO | Brasil | 2101608 | 21 | 33 | nan | nan | nan | Cerrado | 1.1 |
| 9f041157-4e34-37fd-83f5-cbb3bf591adf | -3.85738 | -51.04086 | 2026-09-06 04:46:00 | NOAA-21 | PACAJÁ | PARÁ | Brasil | 1505486 | 15 | 33 | nan | nan | nan | Amazônia | 0.8 |
| dd6d6922-0335-37ee-be8e-ff8411a5512b | -9.71846 | -54.32832 | 2026-09-06 04:46:00 | NOAA-21 | GUARANTÃ DO NORTE | MATO GROSSO | Brasil | 5104104 | 51 | 33 | nan | nan | nan | Amazônia | 1.3 |
| 165b836c-55cb-3c5a-aa9f-42d7eef5a007 | -9.58074 | -40.35683 | 2026-09-06 04:46:00 | NOAA-21 | JUAZEIRO | BAHIA | Brasil | 2918407 | 29 | 33 | nan | nan | nan | Caatinga | 10.0 |
| 057a9b0e-357f-316d-a97f-b1ca7c9672b4 | -3.81138 | -55.88926 | 2026-09-06 04:46:00 | NOAA-21 | AVEIRO | PARÁ | Brasil | 1501006 | 15 | 33 | nan | nan | nan | Amazônia | 1.9 |
| ae775a2d-3495-37e4-b899-e2e60aec1ac6 | -5.34133 | -56.03474 | 2026-09-06 04:46:00 | NOAA-21 | TRAIRÃO | PARÁ | Brasil | 1508050 | 15 | 33 | nan | nan | nan | Amazônia | 1.2 |
| 61bdd96a-3e0d-37cf-a871-99f8f4a294e9 | -4.66593 | -55.63875 | 2026-09-06 04:46:00 | NOAA-21 | ITAITUBA | PARÁ | Brasil | 1503606 | 15 | 33 | nan | nan | nan | Amazônia | 2.1 |
| 4e215cf6-6b7f-3512-a70e-df2ba8be5c1c | -5.34941 | -56.03608 | 2026-09-06 04:46:00 | NOAA-21 | TRAIRÃO | PARÁ | Brasil | 1508050 | 15 | 33 | nan | nan | nan | Amazônia | 1.9 |
| 31ae0731-528a-3b9b-a9bf-1ccbfaef612a | -5.13702 | -60.36262 | 2026-09-06 04:46:00 | NOAA-21 | NOVO ARIPUANÃ | AMAZONAS | Brasil | 1303304 | 13 | 33 | nan | nan | nan | Amazônia | 1.8 |
| f3cbe3fb-72cd-3578-919f-047c93cb2927 | -6.09296 | -55.59579 | 2026-09-06 04:46:00 | NOAA-21 | ITAITUBA | PARÁ | Brasil | 1503606 | 15 | 33 | nan | nan | nan | Amazônia | 1.6 |
| 373d8466-f1d7-3bc7-8bf6-f7feecca3705 | -7.11618 | -55.12976 | 2026-09-06 04:46:00 | NOAA-21 | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 1.5 |
| fd18ba32-6e3a-36bb-a572-eadd915bf7dd | -9.63498 | -47.68738 | 2026-09-06 04:46:00 | NOAA-21 | RIO SONO | TOCANTINS | Brasil | 1718758 | 17 | 33 | nan | nan | nan | Cerrado | 2.2 |
| f4a5395d-becc-3e24-aee5-87df325dd07a | -4.90369 | -45.09897 | 2026-09-06 04:46:00 | NOAA-21 | POÇÃO DE PEDRAS | MARANHÃO | Brasil | 2108900 | 21 | 33 | nan | nan | nan | Cerrado | 1.0 |
| ab211644-bcbe-3300-adbf-0b612b144094 | -5.60028 | -60.24234 | 2026-09-06 04:46:00 | NOAA-21 | NOVO ARIPUANÃ | AMAZONAS | Brasil | 1303304 | 13 | 33 | nan | nan | nan | Amazônia | 1.0 |
| cfb07466-dedb-3a2d-b7a1-73b46f11122e | -11.3182 | -45.10695 | 2026-09-06 04:46:00 | NOAA-21 | FORMOSA DO RIO PRETO | BAHIA | Brasil | 2911105 | 29 | 33 | nan | nan | nan | Cerrado | 2.8 |
| 434a613f-1120-3275-92b0-d5f2f9cf4734 | -4.67442 | -55.63672 | 2026-09-06 04:46:00 | NOAA-21 | ITAITUBA | PARÁ | Brasil | 1503606 | 15 | 33 | nan | nan | nan | Amazônia | 1.2 |
| 9b495ec6-781f-37f3-8ece-10e56a975cbf | -5.83604 | -60.25397 | 2026-09-06 04:46:00 | NOAA-21 | NOVO ARIPUANÃ | AMAZONAS | Brasil | 1303304 | 13 | 33 | nan | nan | nan | Amazônia | 3.8 |
| 39ddb164-69be-3ac3-8e71-49c1fbbacda7 | -5.30094 | -55.86907 | 2026-09-06 04:46:00 | NOAA-21 | TRAIRÃO | PARÁ | Brasil | 1508050 | 15 | 33 | nan | nan | nan | Amazônia | 1.4 |
| 3a24445d-4636-39b6-9cc3-c2fe45976f1e | -5.65547 | -60.24133 | 2026-09-06 04:46:00 | NOAA-21 | NOVO ARIPUANÃ | AMAZONAS | Brasil | 1303304 | 13 | 33 | nan | nan | nan | Amazônia | 2.2 |
| 2966535f-a688-35ee-9003-0a41122a139c | -3.21841 | -53.16536 | 2026-09-06 04:46:00 | NOAA-21 | MEDICILÂNDIA | PARÁ | Brasil | 1504455 | 15 | 33 | nan | nan | nan | Amazônia | 3.6 |
| 3f6b7962-33c9-30f0-8d30-71877d9e6da2 | -4.91901 | -55.80894 | 2026-09-06 04:46:00 | NOAA-21 | TRAIRÃO | PARÁ | Brasil | 1508050 | 15 | 33 | nan | nan | nan | Amazônia | 2.2 |
| 0a48257f-56d6-3a14-8f45-7ebefee4e3c0 | -5.4307 | -60.18539 | 2026-09-06 04:46:00 | NOAA-21 | NOVO ARIPUANÃ | AMAZONAS | Brasil | 1303304 | 13 | 33 | nan | nan | nan | Amazônia | 1.2 |
| 8246af8d-efcb-3584-b129-56bd8f617997 | -4.23971 | -44.6113 | 2026-09-06 04:46:00 | NOAA-21 | BACABAL | MARANHÃO | Brasil | 2101202 | 21 | 33 | nan | nan | nan | Cerrado | 0.9 |
| ccccae17-561b-31a6-93b2-e24b6b63462f | -6.06493 | -57.79939 | 2026-09-06 04:46:00 | NOAA-21 | JACAREACANGA | PARÁ | Brasil | 1503754 | 15 | 33 | nan | nan | nan | Amazônia | 2.1 |
| 1f0bc93d-8efc-32f0-8499-00e139b82437 | -7.10119 | -56.51108 | 2026-09-06 04:46:00 | NOAA-21 | ITAITUBA | PARÁ | Brasil | 1503606 | 15 | 33 | nan | nan | nan | Amazônia | 1.5 |
| d38511af-e915-39a3-ac53-ceeaebfc0b88 | -6.63858 | -59.44373 | 2026-09-06 04:46:00 | NOAA-21 | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 1.5 |
| 3625b59c-5c55-3293-8b56-468f5d6e1380 | -6.87999 | -55.61668 | 2026-09-06 04:46:00 | NOAA-21 | NOVO PROGRESSO | PARÁ | Brasil | 1505031 | 15 | 33 | nan | nan | nan | Amazônia | 1.2 |
| 705a1b81-e681-3aac-a158-2c82071f67ec | -6.51275 | -58.29118 | 2026-09-06 04:46:00 | NOAA-21 | JACAREACANGA | PARÁ | Brasil | 1503754 | 15 | 33 | nan | nan | nan | Amazônia | 2.6 |
| c1033ba8-96ae-3efc-a210-74471627b44e | -5.59494 | -60.24139 | 2026-09-06 04:46:00 | NOAA-21 | NOVO ARIPUANÃ | AMAZONAS | Brasil | 1303304 | 13 | 33 | nan | nan | nan | Amazônia | 1.0 |
| 07be976d-e46a-3e26-9f5a-b56c2fcd5b72 | -5.35806 | -56.03389 | 2026-09-06 04:46:00 | NOAA-21 | TRAIRÃO | PARÁ | Brasil | 1508050 | 15 | 33 | nan | nan | nan | Amazônia | 3.3 |
| d456c4c4-05e6-35e7-85b6-7e1b50b5ddbe | -4.12009 | -49.08344 | 2026-09-06 04:46:00 | NOAA-21 | GOIANÉSIA DO PARÁ | PARÁ | Brasil | 1503093 | 15 | 33 | nan | nan | nan | Amazônia | 3.0 |
| c5f3a24a-4e5f-39a1-9c74-79a81cf202db | -5.36267 | -56.03101 | 2026-09-06 04:46:00 | NOAA-21 | TRAIRÃO | PARÁ | Brasil | 1508050 | 15 | 33 | nan | nan | nan | Amazônia | 6.7 |
| fede3752-3045-3ba8-8bbf-24c7d59245a2 | -5.30149 | -55.86559 | 2026-09-06 04:46:00 | NOAA-21 | TRAIRÃO | PARÁ | Brasil | 1508050 | 15 | 33 | nan | nan | nan | Amazônia | 1.4 |
| b0c7e143-ba04-32b4-b3d5-cd090d8f93ea | -5.34883 | -56.03963 | 2026-09-06 04:46:00 | NOAA-21 | TRAIRÃO | PARÁ | Brasil | 1508050 | 15 | 33 | nan | nan | nan | Amazônia | 1.9 |
| f1b6d60f-bdb0-3bf9-83d1-1dad69221fac | -3.62841 | -54.60503 | 2026-09-06 04:46:00 | NOAA-21 | PLACAS | PARÁ | Brasil | 1505650 | 15 | 33 | nan | nan | nan | Amazônia | 1.1 |
| 6b59f5c7-805a-359c-8815-24fe1c9cb3d4 | -2.46781 | -54.8979 | 2026-09-06 04:46:00 | NOAA-21 | SANTARÉM | PARÁ | Brasil | 1506807 | 15 | 33 | nan | nan | nan | Amazônia | 2.2 |
| ddd7c7e0-3e17-366b-a17e-d31a8ee5648e | -4.66649 | -55.63529 | 2026-09-06 04:46:00 | NOAA-21 | ITAITUBA | PARÁ | Brasil | 1503606 | 15 | 33 | nan | nan | nan | Amazônia | 2.1 |
| dc466922-9fd7-3584-8d59-1219a1e67d6d | -3.43982 | -49.48584 | 2026-09-06 04:46:00 | NOAA-21 | BREU BRANCO | PARÁ | Brasil | 1501782 | 15 | 33 | nan | nan | nan | Amazônia | 1.1 |
| d5bc83e2-58b9-3a22-b7d7-74d8b0acc651 | -5.36209 | -56.03455 | 2026-09-06 04:46:00 | NOAA-21 | TRAIRÃO | PARÁ | Brasil | 1508050 | 15 | 33 | nan | nan | nan | Amazônia | 6.7 |
| c4a9bc59-56b8-33d6-9dfe-e2c7889f93ad | -4.29738 | -55.72552 | 2026-09-06 04:46:00 | NOAA-21 | ITAITUBA | PARÁ | Brasil | 1503606 | 15 | 33 | nan | nan | nan | Amazônia | 0.9 |
| 9b2f3854-2734-30d0-9177-cd357381283e | -5.36441 | -56.04589 | 2026-09-06 04:46:00 | NOAA-21 | TRAIRÃO | PARÁ | Brasil | 1508050 | 15 | 33 | nan | nan | nan | Amazônia | 1.6 |
| f2b93565-3d5f-34b8-9afd-bb5f45e288c0 | -7.67426 | -46.05451 | 2026-09-06 04:46:00 | NOAA-21 | BALSAS | MARANHÃO | Brasil | 2101400 | 21 | 33 | nan | nan | nan | Cerrado | 1.5 |
| d377e42a-1613-3300-a723-6158dead7fae | -6.06416 | -57.8039 | 2026-09-06 04:46:00 | NOAA-21 | JACAREACANGA | PARÁ | Brasil | 1503754 | 15 | 33 | nan | nan | nan | Amazônia | 6.5 |
| 07bfbcd6-083b-32a3-977a-a6f60ba19665 | -4.81437 | -49.38459 | 2026-09-06 04:46:00 | NOAA-21 | NOVA IPIXUNA | PARÁ | Brasil | 1504976 | 15 | 33 | nan | nan | nan | Amazônia | 1.8 |
| a95076c6-063f-3f77-88d2-3df320441aac | -3.15626 | -50.82495 | 2026-09-06 04:46:00 | NOAA-21 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 3.8 |
| 3fac08d3-d4e0-3caf-ae41-57548255c3ab | -5.37074 | -56.03235 | 2026-09-06 04:46:00 | NOAA-21 | TRAIRÃO | PARÁ | Brasil | 1508050 | 15 | 33 | nan | nan | nan | Amazônia | 12.8 |
| d95d909d-0067-3f3a-ad1f-1e227f43d96c | -2.4594 | -57.91512 | 2026-09-06 04:46:00 | NOAA-21 | SÃO SEBASTIÃO DO UATUMÃ | AMAZONAS | Brasil | 1303957 | 13 | 33 | nan | nan | nan | Amazônia | 11.2 |
| b1f7dc3c-91b3-3d0a-b70c-e3c8abc56aef | -11.29001 | -45.6995 | 2026-09-06 04:46:00 | NOAA-21 | FORMOSA DO RIO PRETO | BAHIA | Brasil | 2911105 | 29 | 33 | nan | nan | nan | Cerrado | 1.8 |
| b97ab708-a5c2-31fc-bd01-2836bb4bad19 | -5.14443 | -55.96099 | 2026-09-06 04:46:00 | NOAA-21 | TRAIRÃO | PARÁ | Brasil | 1508050 | 15 | 33 | nan | nan | nan | Amazônia | 4.0 |
| 2de55e8e-c23d-3e4c-ba42-667b64bffe8a | -5.33325 | -56.03343 | 2026-09-06 04:46:00 | NOAA-21 | TRAIRÃO | PARÁ | Brasil | 1508050 | 15 | 33 | nan | nan | nan | Amazônia | 1.5 |
| 6bbd2511-e47f-3c2d-b57b-53dcb75a0490 | -7.95522 | -54.88475 | 2026-09-06 04:46:00 | NOAA-21 | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 2.3 |
| cbe7da89-a4b6-3a4e-8458-654329d97023 | -5.36845 | -56.04655 | 2026-09-06 04:46:00 | NOAA-21 | TRAIRÃO | PARÁ | Brasil | 1508050 | 15 | 33 | nan | nan | nan | Amazônia | 3.4 |
| ca8ac9d3-c30e-3838-9678-63c56f4fa078 | -5.84728 | -60.2524 | 2026-09-06 04:46:00 | NOAA-21 | NOVO ARIPUANÃ | AMAZONAS | Brasil | 1303304 | 13 | 33 | nan | nan | nan | Amazônia | 2.0 |
| 9b71e093-337d-338a-be5e-c786db9ce8f8 | -3.41583 | -54.77354 | 2026-09-06 04:46:00 | NOAA-21 | MOJUÍ DOS CAMPOS | PARÁ | Brasil | 1504752 | 15 | 33 | nan | nan | nan | Amazônia | 1.2 |
| 4d606e09-3a13-32b7-8214-9166e613974d | -8.95308 | -44.41141 | 2026-09-06 04:46:00 | NOAA-21 | CURRAIS | PIAUÍ | Brasil | 2203230 | 22 | 33 | nan | nan | nan | Cerrado | 4.5 |
| 72e22c78-d757-3f07-8729-15002abbbbb0 | -5.86535 | -46.22036 | 2026-09-06 04:46:00 | NOAA-21 | GRAJAÚ | MARANHÃO | Brasil | 2104800 | 21 | 33 | nan | nan | nan | Cerrado | 2.3 |


[Clique aqui para ver as próximas entradas](README18.md)
