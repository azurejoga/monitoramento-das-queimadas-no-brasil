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

## Dados Diários - Página 100

| ID | Latitude | Longitude | Data/Hora GMT | Satélite | Município | Estado | País | Município ID | Estado ID | País ID | Dias sem Chuva | Precipitação | Risco de Fogo | Bioma | FRP |
|----|----------|-----------|---------------|----------|-----------|--------|------|--------------|-----------|---------|----------------|--------------|----------------|-------|-----|
| cabc8eb8-b2ec-33d0-8b5f-009e85545e81 | 0.69 | -59.54613 | 2026-09-20 05:57:00 | NPP-375D | CAROEBE | RORAIMA | Brasil | 1400233 | 14 | 33 | nan | nan | nan | Amazônia | 1.6 |
| a1971f7d-d8d5-3244-b03c-9f6fb7994a38 | -1.22196 | -55.72016 | 2026-09-20 05:57:00 | NPP-375D | ÓBIDOS | PARÁ | Brasil | 1505106 | 15 | 33 | nan | nan | nan | Amazônia | 2.2 |
| e78855a3-cbc4-3120-94ef-6fe48ff4577c | 0.94672 | -59.53113 | 2026-09-20 05:57:00 | NPP-375D | CAROEBE | RORAIMA | Brasil | 1400233 | 14 | 33 | nan | nan | nan | Amazônia | 0.7 |
| 42cb1efc-3137-3fe9-8d41-9701eb81ac98 | 2.31867 | -60.9207 | 2026-09-20 05:57:00 | NPP-375D | MUCAJAÍ | RORAIMA | Brasil | 1400308 | 14 | 33 | nan | nan | nan | Amazônia | 4.7 |
| 2f6ef29c-6239-347c-b815-64daabc7a888 | -1.63769 | -55.1502 | 2026-09-20 05:57:00 | NPP-375D | CURUÁ | PARÁ | Brasil | 1502855 | 15 | 33 | nan | nan | nan | Amazônia | 1.1 |
| 0407fb09-266b-36d1-b2b4-352c80afc427 | 4.53109 | -60.87124 | 2026-09-20 05:57:00 | NPP-375D | PACARAIMA | RORAIMA | Brasil | 1400456 | 14 | 33 | nan | nan | nan | Amazônia | 1.7 |
| 7294750c-618c-33b6-8e5f-a9aba2ac6934 | 4.36015 | -60.31868 | 2026-09-20 05:57:00 | NPP-375D | UIRAMUTÃ | RORAIMA | Brasil | 1400704 | 14 | 33 | nan | nan | nan | Amazônia | 0.9 |
| a7f61a28-bc0f-3bc9-a24b-e5f07cf6d859 | 4.53008 | -60.8733 | 2026-09-20 05:57:00 | NPP-375D | PACARAIMA | RORAIMA | Brasil | 1400456 | 14 | 33 | nan | nan | nan | Amazônia | 1.9 |
| b62c99da-ce27-3234-926f-1656ccdebd18 | -1.25557 | -55.76507 | 2026-09-20 05:57:00 | NPP-375D | ÓBIDOS | PARÁ | Brasil | 1505106 | 15 | 33 | nan | nan | nan | Amazônia | 1.2 |
| f613ac39-a49a-3a3a-8ee9-957be09689b9 | -1.22136 | -55.72398 | 2026-09-20 05:57:00 | NPP-375D | ÓBIDOS | PARÁ | Brasil | 1505106 | 15 | 33 | nan | nan | nan | Amazônia | 2.2 |
| e3d621a6-546a-336a-b692-dc26e5e6a134 | 0.0085 | -60.60738 | 2026-09-20 05:57:00 | NPP-375D | RORAINÓPOLIS | RORAIMA | Brasil | 1400472 | 14 | 33 | nan | nan | nan | Amazônia | 2.4 |
| 56f4dcb3-7950-3393-bc40-795a8c8ef3cc | -1.25824 | -55.76397 | 2026-09-20 05:57:00 | NPP-375D | ÓBIDOS | PARÁ | Brasil | 1505106 | 15 | 33 | nan | nan | nan | Amazônia | 1.0 |
| 72fca44c-6017-3313-b8e2-62b0d25533ae | 4.53489 | -60.87136 | 2026-09-20 05:57:00 | NPP-375D | PACARAIMA | RORAIMA | Brasil | 1400456 | 14 | 33 | nan | nan | nan | Amazônia | 1.7 |
| 7b43f898-0b21-3b63-a0bb-b2f9626f3ca9 | -1.6396 | -55.15472 | 2026-09-20 05:57:00 | NPP-375D | CURUÁ | PARÁ | Brasil | 1502855 | 15 | 33 | nan | nan | nan | Amazônia | 1.2 |
| 4fdc963b-c3a2-3576-9497-eb28090ab67d | -1.25253 | -55.76329 | 2026-09-20 05:57:00 | NPP-375D | ÓBIDOS | PARÁ | Brasil | 1505106 | 15 | 33 | nan | nan | nan | Amazônia | 1.0 |
| f2c35621-13c1-3d11-8f9b-59084f284d16 | 4.35641 | -60.31974 | 2026-09-20 05:57:00 | NPP-375D | UIRAMUTÃ | RORAIMA | Brasil | 1400704 | 14 | 33 | nan | nan | nan | Amazônia | 0.9 |
| fdd6f910-6eef-38bd-83d4-16050122efbc | 0.0125 | -60.60673 | 2026-09-20 05:57:00 | NPP-375D | RORAINÓPOLIS | RORAIMA | Brasil | 1400472 | 14 | 33 | nan | nan | nan | Amazônia | 3.0 |
| a99471d6-de8d-34be-9740-e3db4f8f8221 | 4.5371 | -60.95584 | 2026-09-20 05:57:00 | NPP-375D | PACARAIMA | RORAIMA | Brasil | 1400456 | 14 | 33 | nan | nan | nan | Amazônia | 1.5 |
| e7be1ada-3d3d-3f67-9b88-44bff4ee8a5e | -1.25494 | -55.76897 | 2026-09-20 05:57:00 | NPP-375D | ÓBIDOS | PARÁ | Brasil | 1505106 | 15 | 33 | nan | nan | nan | Amazônia | 1.2 |
| 1d64f2f9-0aef-35a0-8869-fd19234e6828 | 0.69126 | -59.55398 | 2026-09-20 05:57:00 | NPP-375D | CAROEBE | RORAIMA | Brasil | 1400233 | 14 | 33 | nan | nan | nan | Amazônia | 2.2 |
| f150177f-48c2-3e10-a3c7-b4c59cb7a147 | 0.69063 | -59.55006 | 2026-09-20 05:57:00 | NPP-375D | CAROEBE | RORAIMA | Brasil | 1400233 | 14 | 33 | nan | nan | nan | Amazônia | 2.2 |
| 7dc15f50-8a1a-3d67-9e7b-56714d2db70e | -1.63703 | -55.1544 | 2026-09-20 05:57:00 | NPP-375D | CURUÁ | PARÁ | Brasil | 1502855 | 15 | 33 | nan | nan | nan | Amazônia | 0.8 |
| 5f70bc19-94fb-3a9b-9ff7-2b3c05f96a24 | -1.18799 | -55.67626 | 2026-09-20 05:57:00 | NPP-375D | ÓBIDOS | PARÁ | Brasil | 1505106 | 15 | 33 | nan | nan | nan | Amazônia | 1.5 |
| 1bbc9c25-74f9-364a-bd92-d3addd77b1ca | 0.91022 | -59.62809 | 2026-09-20 05:57:00 | NPP-375D | CAROEBE | RORAIMA | Brasil | 1400233 | 14 | 33 | nan | nan | nan | Amazônia | 1.0 |
| d5b96cbc-099e-3090-88d4-3d7c29c9e756 | -1.25194 | -55.76719 | 2026-09-20 05:57:00 | NPP-375D | ÓBIDOS | PARÁ | Brasil | 1505106 | 15 | 33 | nan | nan | nan | Amazônia | 1.0 |
| 22a1e11a-1379-3ac6-abe3-1ec81f74e594 | 4.53387 | -60.87328 | 2026-09-20 05:57:00 | NPP-375D | PACARAIMA | RORAIMA | Brasil | 1400456 | 14 | 33 | nan | nan | nan | Amazônia | 1.9 |
| 69f7228e-c469-3d39-89cd-ea02b784f93a | -1.64023 | -55.1505 | 2026-09-20 05:57:00 | NPP-375D | CURUÁ | PARÁ | Brasil | 1502855 | 15 | 33 | nan | nan | nan | Amazônia | 1.1 |
| f14c153e-f420-3423-9a04-f2f123baa8da | 4.53957 | -60.95288 | 2026-09-20 05:57:00 | NPP-375D | PACARAIMA | RORAIMA | Brasil | 1400456 | 14 | 33 | nan | nan | nan | Amazônia | 0.7 |
| 701ec652-a033-39a1-9d83-a81a0ecc989f | -6.35244 | -58.30463 | 2026-09-20 05:59:00 | NPP-375D | MAUÉS | AMAZONAS | Brasil | 1302900 | 13 | 33 | nan | nan | nan | Amazônia | 1.9 |
| 5b5c2c91-67a2-3d7c-bbd1-b3c98e093bc5 | -3.23264 | -61.21094 | 2026-09-20 05:59:00 | NPP-375D | MANACAPURU | AMAZONAS | Brasil | 1302504 | 13 | 33 | nan | nan | nan | Amazônia | 1.8 |
| 658b38a6-6f26-35dc-ae39-aa95c7ad4100 | -2.88428 | -57.79787 | 2026-09-20 05:59:00 | NPP-375D | URUCURITUBA | AMAZONAS | Brasil | 1304401 | 13 | 33 | nan | nan | nan | Amazônia | 1.9 |
| bb95267d-dc91-31a3-bca8-31b9732fca43 | -8.18511 | -54.75918 | 2026-09-20 05:59:00 | NPP-375D | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 6.9 |
| ad17e915-5a3d-3c0b-b4f8-1eda4305fc1e | -3.69273 | -60.56214 | 2026-09-20 05:59:00 | NPP-375D | MANAQUIRI | AMAZONAS | Brasil | 1302553 | 13 | 33 | nan | nan | nan | Amazônia | 1.4 |
| 5c1c80f8-f083-3f68-9fe5-8a83800deb55 | -2.61687 | -54.7592 | 2026-09-20 05:59:00 | NPP-375D | SANTARÉM | PARÁ | Brasil | 1506807 | 15 | 33 | nan | nan | nan | Amazônia | 6.4 |
| 307eeba9-be11-31bc-9577-593e0bc4472b | -3.58645 | -59.02716 | 2026-09-20 05:59:00 | NPP-375D | AUTAZES | AMAZONAS | Brasil | 1300300 | 13 | 33 | nan | nan | nan | Amazônia | 1.6 |
| 1ca15175-f2ea-3787-84ce-6b210c4b5851 | -7.04467 | -62.95994 | 2026-09-20 05:59:00 | NPP-375D | HUMAITÁ | AMAZONAS | Brasil | 1301704 | 13 | 33 | nan | nan | nan | Amazônia | 1.4 |
| 42fd80b3-176b-319a-8b83-7d368336b903 | -2.8834 | -57.80374 | 2026-09-20 05:59:00 | NPP-375D | URUCURITUBA | AMAZONAS | Brasil | 1304401 | 13 | 33 | nan | nan | nan | Amazônia | 2.7 |
| d5b801ee-583b-31df-a42e-f9f6fdcb6689 | -2.71694 | -57.96322 | 2026-09-20 05:59:00 | NPP-375D | ITAPIRANGA | AMAZONAS | Brasil | 1302009 | 13 | 33 | nan | nan | nan | Amazônia | 6.8 |
| 3a4a1580-5aac-310a-b1e2-7aa081243add | -2.98425 | -54.77246 | 2026-09-20 05:59:00 | NPP-375D | MOJUÍ DOS CAMPOS | PARÁ | Brasil | 1504752 | 15 | 33 | nan | nan | nan | Amazônia | 1.6 |
| d3402a22-7184-3413-8997-d031ce58ed17 | -8.08071 | -55.34257 | 2026-09-20 05:59:00 | NPP-375D | NOVO PROGRESSO | PARÁ | Brasil | 1505031 | 15 | 33 | nan | nan | nan | Amazônia | 1.3 |
| caccb9d3-1f63-37a5-ad05-6621905162a1 | -7.57758 | -57.68309 | 2026-09-20 05:59:00 | NPP-375D | JACAREACANGA | PARÁ | Brasil | 1503754 | 15 | 33 | nan | nan | nan | Amazônia | 1.1 |
| 0bdd7cd2-574b-3c19-983f-528a1513b825 | -3.34465 | -57.85911 | 2026-09-20 05:59:00 | NPP-375D | MAUÉS | AMAZONAS | Brasil | 1302900 | 13 | 33 | nan | nan | nan | Amazônia | 1.2 |
| b6df9393-0ce8-3042-939c-fbe0e0c8ee04 | -3.40043 | -54.07583 | 2026-09-20 05:59:00 | NPP-375D | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | 1.8 |
| 4d137638-cdbc-3be8-887f-9cf03997c4cc | -3.39509 | -54.06901 | 2026-09-20 05:59:00 | NPP-375D | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | 1.3 |
| ae7a6ae7-e4c5-3683-90b7-c5747361299f | -3.3513 | -59.86649 | 2026-09-20 05:59:00 | NPP-375D | CAREIRO DA VÁRZEA | AMAZONAS | Brasil | 1301159 | 13 | 33 | nan | nan | nan | Amazônia | 1.6 |
| f2219bb7-c0e3-365f-b05c-81710c112ec1 | -5.83649 | -53.52502 | 2026-09-20 05:59:00 | NPP-375D | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 0.8 |
| 3b7d58a7-8d9d-32de-a387-f8016e9be3a1 | -2.58871 | -59.98983 | 2026-09-20 05:59:00 | NPP-375D | MANAUS | AMAZONAS | Brasil | 1302603 | 13 | 33 | nan | nan | nan | Amazônia | 2.1 |
| 47ae3ebc-4e19-3e21-967d-36ce879246dc | -6.89452 | -63.04226 | 2026-09-20 05:59:00 | NPP-375D | HUMAITÁ | AMAZONAS | Brasil | 1301704 | 13 | 33 | nan | nan | nan | Amazônia | 1.0 |
| c7ca47e1-a296-3058-8ba5-0ce4f411b536 | -6.36794 | -58.30688 | 2026-09-20 05:59:00 | NPP-375D | MAUÉS | AMAZONAS | Brasil | 1302900 | 13 | 33 | nan | nan | nan | Amazônia | 1.2 |
| 0cfd2a2a-8fa0-3e2f-88ab-8d3a605e2e35 | -6.13701 | -59.93874 | 2026-09-20 05:59:00 | NPP-375D | NOVO ARIPUANÃ | AMAZONAS | Brasil | 1303304 | 13 | 33 | nan | nan | nan | Amazônia | 1.9 |
| f38c2c2c-0f55-3130-945d-7362bd61ec9e | -7.57642 | -57.68723 | 2026-09-20 05:59:00 | NPP-375D | JACAREACANGA | PARÁ | Brasil | 1503754 | 15 | 33 | nan | nan | nan | Amazônia | 1.2 |
| 65ee0ca7-5737-3b43-9073-7a1675f295c9 | -3.14622 | -57.89233 | 2026-09-20 05:59:00 | NPP-375D | BOA VISTA DO RAMOS | AMAZONAS | Brasil | 1300680 | 13 | 33 | nan | nan | nan | Amazônia | 2.1 |
| 779fbd32-4315-3ca0-94e8-a16bef12ff11 | -7.55798 | -61.32478 | 2026-09-20 05:59:00 | NPP-375D | MANICORÉ | AMAZONAS | Brasil | 1302702 | 13 | 33 | nan | nan | nan | Amazônia | 1.0 |
| 19e7fe09-e630-3ca6-bd85-3e7bd635b72c | -3.1463 | -60.42038 | 2026-09-20 05:59:00 | NPP-375D | MANACAPURU | AMAZONAS | Brasil | 1302504 | 13 | 33 | nan | nan | nan | Amazônia | 1.3 |
| f7804572-08b5-3340-b4f7-546f5a1f091a | -7.60205 | -55.71334 | 2026-09-20 05:59:00 | NPP-375D | NOVO PROGRESSO | PARÁ | Brasil | 1505031 | 15 | 33 | nan | nan | nan | Amazônia | 2.4 |
| a255d92e-a1fd-3538-872e-4787c9666065 | -8.42436 | -54.72287 | 2026-09-20 05:59:00 | NPP-375D | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 1.1 |
| 54095a53-0ec3-3371-8d80-a907e77f6349 | -6.45264 | -59.98237 | 2026-09-20 05:59:00 | NPP-375D | NOVO ARIPUANÃ | AMAZONAS | Brasil | 1303304 | 13 | 33 | nan | nan | nan | Amazônia | 2.0 |
| d70b173a-2043-38ba-861c-c13687f15d7d | -8.18164 | -54.76509 | 2026-09-20 05:59:00 | NPP-375D | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 4.1 |
| e3192543-bee5-3b3f-a0af-4767b9c7b1bc | -8.08 | -55.34793 | 2026-09-20 05:59:00 | NPP-375D | NOVO PROGRESSO | PARÁ | Brasil | 1505031 | 15 | 33 | nan | nan | nan | Amazônia | 1.3 |
| dd907a6c-9195-31b1-9e4a-42e974280225 | -7.6027 | -55.70851 | 2026-09-20 05:59:00 | NPP-375D | NOVO PROGRESSO | PARÁ | Brasil | 1505031 | 15 | 33 | nan | nan | nan | Amazônia | 2.0 |
| 786a5b60-35b5-3546-aad1-ffa2367c873d | -3.52598 | -56.91654 | 2026-09-20 05:59:00 | NPP-375D | BARREIRINHA | AMAZONAS | Brasil | 1300508 | 13 | 33 | nan | nan | nan | Amazônia | 0.7 |
| 7db40805-9af8-31f1-a671-47927bcdc540 | -2.8856 | -57.78905 | 2026-09-20 05:59:00 | NPP-375D | URUCURITUBA | AMAZONAS | Brasil | 1304401 | 13 | 33 | nan | nan | nan | Amazônia | 2.6 |
| a37aad59-5a1f-360b-a30b-cf51ea3ad766 | -3.88559 | -58.94812 | 2026-09-20 05:59:00 | NPP-375D | NOVA OLINDA DO NORTE | AMAZONAS | Brasil | 1303106 | 13 | 33 | nan | nan | nan | Amazônia | 1.8 |
| 4813479f-d1b7-373f-80fb-56e6a4daa872 | -2.88384 | -57.8008 | 2026-09-20 05:59:00 | NPP-375D | URUCURITUBA | AMAZONAS | Brasil | 1304401 | 13 | 33 | nan | nan | nan | Amazônia | 2.7 |
| 99a4a64f-e757-3c76-ba95-ca3c933281d3 | -6.09837 | -57.6857 | 2026-09-20 05:59:00 | NPP-375D | JACAREACANGA | PARÁ | Brasil | 1503754 | 15 | 33 | nan | nan | nan | Amazônia | 1.3 |
| b11eec5a-a111-3113-a8b8-0e6ac8c74989 | -3.00082 | -60.80441 | 2026-09-20 05:59:00 | NPP-375D | IRANDUBA | AMAZONAS | Brasil | 1301852 | 13 | 33 | nan | nan | nan | Amazônia | 1.5 |
| c7e8fec3-111d-31a4-9d8d-8687a7bcf9bb | -5.854 | -53.54724 | 2026-09-20 05:59:00 | NPP-375D | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 2.8 |
| cea1a504-3180-3893-8374-91e03bfd09b0 | -6.64866 | -62.88163 | 2026-09-20 05:59:00 | NPP-375D | HUMAITÁ | AMAZONAS | Brasil | 1301704 | 13 | 33 | nan | nan | nan | Amazônia | 1.6 |
| 1eb1b732-e41d-39d9-a546-dd9b07f88848 | -3.44125 | -58.23244 | 2026-09-20 05:59:00 | NPP-375D | ITACOATIARA | AMAZONAS | Brasil | 1301902 | 13 | 33 | nan | nan | nan | Amazônia | 5.3 |
| 62ca9b99-c7ed-39ab-892f-b107751088c6 | -5.83929 | -53.55135 | 2026-09-20 05:59:00 | NPP-375D | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 2.3 |
| 6c39c6d3-625a-3c41-896a-c0081343a36f | -6.13565 | -59.94807 | 2026-09-20 05:59:00 | NPP-375D | NOVO ARIPUANÃ | AMAZONAS | Brasil | 1303304 | 13 | 33 | nan | nan | nan | Amazônia | 1.6 |
| 3e61f82b-40fb-3ae9-ae88-d98985ef8466 | -3.40149 | -61.30035 | 2026-09-20 05:59:00 | NPP-375D | CAAPIRANGA | AMAZONAS | Brasil | 1300839 | 13 | 33 | nan | nan | nan | Amazônia | 1.5 |
| af0a3d46-1afa-3a98-9217-788d14b2df6a | -7.60065 | -55.70962 | 2026-09-20 05:59:00 | NPP-375D | NOVO PROGRESSO | PARÁ | Brasil | 1505031 | 15 | 33 | nan | nan | nan | Amazônia | 2.9 |
| 50663b29-5421-30d4-ac63-d6fc35045f67 | -6.20208 | -57.78156 | 2026-09-20 05:59:00 | NPP-375D | JACAREACANGA | PARÁ | Brasil | 1503754 | 15 | 33 | nan | nan | nan | Amazônia | 1.2 |
| 431a72a3-d07b-3150-a6a8-9469970dc771 | -8.18433 | -54.765 | 2026-09-20 05:59:00 | NPP-375D | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 7.6 |
| 9722d736-97a5-3300-bc5c-090ef1d344c3 | -5.83741 | -53.51853 | 2026-09-20 05:59:00 | NPP-375D | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 0.8 |
| 97aa1eee-4386-3cd1-b29c-9f58cd42c732 | -4.49442 | -55.48791 | 2026-09-20 05:59:00 | NPP-375D | RURÓPOLIS | PARÁ | Brasil | 1506195 | 15 | 33 | nan | nan | nan | Amazônia | 1.4 |
| 370cf957-086c-30f5-9d90-0515644380f4 | -3.08262 | -61.18775 | 2026-09-20 05:59:00 | NPP-375D | MANACAPURU | AMAZONAS | Brasil | 1302504 | 13 | 33 | nan | nan | nan | Amazônia | 1.0 |
| b84aed58-f7c8-3c76-9a40-5846e689b3d9 | -8.18238 | -54.7593 | 2026-09-20 05:59:00 | NPP-375D | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 4.1 |
| 0519b210-f377-3e50-9bf0-f99720f47f4e | -6.13633 | -59.94339 | 2026-09-20 05:59:00 | NPP-375D | NOVO ARIPUANÃ | AMAZONAS | Brasil | 1303304 | 13 | 33 | nan | nan | nan | Amazônia | 1.6 |
| 730e0974-3089-3d03-92d3-f19c741847e2 | -3.29665 | -57.86706 | 2026-09-20 05:59:00 | NPP-375D | MAUÉS | AMAZONAS | Brasil | 1302900 | 13 | 33 | nan | nan | nan | Amazônia | 0.6 |
| ebc6bc87-311a-31a6-9f42-eef023b61580 | -3.00357 | -54.1702 | 2026-09-20 05:59:00 | NPP-375D | SANTARÉM | PARÁ | Brasil | 1506807 | 15 | 33 | nan | nan | nan | Amazônia | 1.3 |
| 83e18134-1690-3697-9529-250065d66ccb | -2.88296 | -57.80669 | 2026-09-20 05:59:00 | NPP-375D | URUCURITUBA | AMAZONAS | Brasil | 1304401 | 13 | 33 | nan | nan | nan | Amazônia | 6.6 |
| 03b36f7b-5b19-3e4f-bdb8-e44a42e2c7ee | -6.35201 | -58.3077 | 2026-09-20 05:59:00 | NPP-375D | MAUÉS | AMAZONAS | Brasil | 1302900 | 13 | 33 | nan | nan | nan | Amazônia | 1.1 |
| 6662fd95-eda1-39ff-a624-01e226bc2b22 | -3.08206 | -61.19125 | 2026-09-20 05:59:00 | NPP-375D | MANACAPURU | AMAZONAS | Brasil | 1302504 | 13 | 33 | nan | nan | nan | Amazônia | 0.8 |
| 0cf45a18-187b-38c6-ae8f-9b55c7195195 | -6.34211 | -58.30313 | 2026-09-20 05:59:00 | NPP-375D | MAUÉS | AMAZONAS | Brasil | 1302900 | 13 | 33 | nan | nan | nan | Amazônia | 1.0 |
| 1820637d-fe1b-3972-b600-d78afbb544d8 | -3.0524 | -61.27557 | 2026-09-20 05:59:00 | NPP-375D | MANACAPURU | AMAZONAS | Brasil | 1302504 | 13 | 33 | nan | nan | nan | Amazônia | 1.8 |
| 4e2ab263-8978-3ae0-a780-aeaa8e238720 | -3.00997 | -54.17144 | 2026-09-20 05:59:00 | NPP-375D | SANTARÉM | PARÁ | Brasil | 1506807 | 15 | 33 | nan | nan | nan | Amazônia | 1.3 |
| f01a64e3-8e0f-3073-975e-910ae409ca7a | -5.77073 | -57.45686 | 2026-09-20 05:59:00 | NPP-375D | JACAREACANGA | PARÁ | Brasil | 1503754 | 15 | 33 | nan | nan | nan | Amazônia | 2.2 |
| 674944b2-915c-3e90-83b9-0333c22a02e8 | -3.9222 | -60.55531 | 2026-09-20 05:59:00 | NPP-375D | CAREIRO | AMAZONAS | Brasil | 1301100 | 13 | 33 | nan | nan | nan | Amazônia | 0.8 |
| d4c24b12-83cb-35be-a40e-d275e6c08c6e | -5.84371 | -53.51877 | 2026-09-20 05:59:00 | NPP-375D | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 2.7 |
| 38f4f273-b6ee-3cbe-9992-ca02a4c28e99 | -5.84889 | -53.53282 | 2026-09-20 05:59:00 | NPP-375D | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 2.9 |
| 53fbeae0-62fd-381d-b1b8-0eaaa7e40c06 | -2.88472 | -57.79493 | 2026-09-20 05:59:00 | NPP-375D | URUCURITUBA | AMAZONAS | Brasil | 1304401 | 13 | 33 | nan | nan | nan | Amazônia | 1.9 |
| 1a747466-e210-319c-8db7-bcd658f3596b | -3.69276 | -60.59017 | 2026-09-20 05:59:00 | NPP-375D | MANAQUIRI | AMAZONAS | Brasil | 1302553 | 13 | 33 | nan | nan | nan | Amazônia | 1.1 |
| ace0da4a-3035-37af-9358-608fd5196b95 | -4.51516 | -55.47266 | 2026-09-20 05:59:00 | NPP-375D | RURÓPOLIS | PARÁ | Brasil | 1506195 | 15 | 33 | nan | nan | nan | Amazônia | 1.8 |
| 61be51cf-fe84-3809-b693-46afb0068188 | -6.06655 | -57.73361 | 2026-09-20 05:59:00 | NPP-375D | JACAREACANGA | PARÁ | Brasil | 1503754 | 15 | 33 | nan | nan | nan | Amazônia | 1.0 |
| c03c552e-a108-3a8b-ac7b-c94f2fcea16e | -6.06702 | -57.73036 | 2026-09-20 05:59:00 | NPP-375D | JACAREACANGA | PARÁ | Brasil | 1503754 | 15 | 33 | nan | nan | nan | Amazônia | 1.0 |
| 0dc634e6-ef41-3dfc-900f-43e88a30bc3e | -5.8383 | -53.55866 | 2026-09-20 05:59:00 | NPP-375D | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 2.3 |
| 00ebd2d9-eb0d-336e-aa2c-64c428c9c68a | -2.21481 | -60.17529 | 2026-09-20 05:59:00 | NPP-375D | MANAUS | AMAZONAS | Brasil | 1302603 | 13 | 33 | nan | nan | nan | Amazônia | 1.4 |
| d0efde5d-731b-380f-8ea4-83965f87518a | -6.73158 | -55.08006 | 2026-09-20 05:59:00 | NPP-375D | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 1.9 |


[Clique aqui para ver as próximas entradas](README101.md)
