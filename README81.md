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

## Dados Diários - Página 81

| ID | Latitude | Longitude | Data/Hora GMT | Satélite | Município | Estado | País | Município ID | Estado ID | País ID | Dias sem Chuva | Precipitação | Risco de Fogo | Bioma | FRP |
|----|----------|-----------|---------------|----------|-----------|--------|------|--------------|-----------|---------|----------------|--------------|----------------|-------|-----|
| 3ea4ef66-43f5-3554-a465-60f2574fdc26 | -6.1505 | -52.87678 | 2026-10-08 04:46:00 | NOAA-21 | SÃO FÉLIX DO XINGU | PARÁ | Brasil | 1507300 | 15 | 33 | nan | nan | nan | Amazônia | 3.9 |
| 439def8d-032d-3292-9587-f4301382c5fb | -3.0132 | -54.07821 | 2026-10-08 04:46:00 | NOAA-21 | SANTARÉM | PARÁ | Brasil | 1506807 | 15 | 33 | nan | nan | nan | Amazônia | 4.6 |
| 5dd447fe-f411-3f14-b6d5-7b21e64488ce | -2.49935 | -56.12873 | 2026-10-08 04:46:00 | NOAA-21 | JURUTI | PARÁ | Brasil | 1503903 | 15 | 33 | nan | nan | nan | Amazônia | 3.6 |
| bbebb86e-b23c-33cb-b4df-4281618373db | -3.81367 | -52.19868 | 2026-10-08 04:46:00 | NOAA-21 | SENADOR JOSÉ PORFÍRIO | PARÁ | Brasil | 1507805 | 15 | 33 | nan | nan | nan | Amazônia | 1.2 |
| 18097c6b-ced7-307d-bbc3-23d59e1d01d8 | -2.50588 | -56.16995 | 2026-10-08 04:46:00 | NOAA-21 | JURUTI | PARÁ | Brasil | 1503903 | 15 | 33 | nan | nan | nan | Amazônia | 23.5 |
| a504835b-5b18-3b5a-aebb-ea5f9eb603e1 | -6.13676 | -47.95028 | 2026-10-08 04:46:00 | NOAA-21 | CACHOEIRINHA | TOCANTINS | Brasil | 1703826 | 17 | 33 | nan | nan | nan | Cerrado | 3.9 |
| e7804fdc-cca2-30cf-955a-1f3838fdb064 | -2.93766 | -54.14738 | 2026-10-08 04:46:00 | NOAA-21 | SANTARÉM | PARÁ | Brasil | 1506807 | 15 | 33 | nan | nan | nan | Amazônia | 1.3 |
| f199b7c7-ba9a-3a34-812c-3b9c95feeb52 | -7.89022 | -55.01498 | 2026-10-08 04:46:00 | NOAA-21 | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 1.5 |
| 2d2dd79a-efe1-3d02-a00e-218ba25381ab | -3.31158 | -54.04081 | 2026-10-08 04:46:00 | NOAA-21 | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | 5.6 |
| 6d31fe74-8a49-3e0b-8db3-6b4eb0ba1d0d | -3.00952 | -54.07764 | 2026-10-08 04:46:00 | NOAA-21 | SANTARÉM | PARÁ | Brasil | 1506807 | 15 | 33 | nan | nan | nan | Amazônia | 5.2 |
| cc155ed0-5ad0-392a-bea3-d1a17a55dc6b | -6.02313 | -53.85551 | 2026-10-08 04:46:00 | NOAA-21 | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 1.4 |
| 767ce12c-748e-37cc-bb43-807f0fa6489a | -7.38244 | -55.20238 | 2026-10-08 04:46:00 | NOAA-21 | NOVO PROGRESSO | PARÁ | Brasil | 1505031 | 15 | 33 | nan | nan | nan | Amazônia | 1.9 |
| cebea8a4-8989-3871-92b5-f553afc17e38 | -5.99154 | -40.93523 | 2026-10-08 04:46:00 | NOAA-21 | ASSUNÇÃO DO PIAUÍ | PIAUÍ | Brasil | 2201051 | 22 | 33 | nan | nan | nan | Caatinga | 3.5 |
| 5b7a77fb-474d-3237-8d4a-1c5e819b394b | -3.22169 | -54.30287 | 2026-10-08 04:46:00 | NOAA-21 | MOJUÍ DOS CAMPOS | PARÁ | Brasil | 1504752 | 15 | 33 | nan | nan | nan | Amazônia | 3.0 |
| 77dbddd9-3dd9-3514-aedf-cec07420d2a4 | -2.93171 | -58.30057 | 2026-10-08 04:46:00 | NOAA-21 | SILVES | AMAZONAS | Brasil | 1304005 | 13 | 33 | nan | nan | nan | Amazônia | 2.6 |
| ac9b3c48-e02b-32e4-b5ea-6eca80351311 | -7.88432 | -55.0052 | 2026-10-08 04:46:00 | NOAA-21 | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 1.2 |
| eac4afb9-09d7-3a30-a2bf-8bbc5b531474 | -3.68306 | -55.94917 | 2026-10-08 04:46:00 | NOAA-21 | AVEIRO | PARÁ | Brasil | 1501006 | 15 | 33 | nan | nan | nan | Amazônia | 1.7 |
| de8965ab-d7ff-35ef-bfa8-49e1b08e2044 | -2.86716 | -54.19264 | 2026-10-08 04:46:00 | NOAA-21 | SANTARÉM | PARÁ | Brasil | 1506807 | 15 | 33 | nan | nan | nan | Amazônia | 2.5 |
| b89bbd8a-1b17-38c5-8e49-c5ab50959d23 | -2.98634 | -54.12793 | 2026-10-08 04:46:00 | NOAA-21 | SANTARÉM | PARÁ | Brasil | 1506807 | 15 | 33 | nan | nan | nan | Amazônia | 3.1 |
| 6de60a01-779b-3941-8cc1-0db08784e705 | -7.03206 | -45.44527 | 2026-10-08 04:46:00 | NOAA-21 | SÃO RAIMUNDO DAS MANGABEIRAS | MARANHÃO | Brasil | 2111607 | 21 | 33 | nan | nan | nan | Cerrado | 2.9 |
| e9589daf-2f72-361b-ae39-000a1722c3c9 | -6.99344 | -40.037 | 2026-10-08 04:46:00 | NOAA-21 | ASSARÉ | CEARÁ | Brasil | 2301604 | 23 | 33 | nan | nan | nan | Caatinga | 2.3 |
| 59383438-f450-3b43-9de2-a1158a587c27 | -3.28101 | -54.06702 | 2026-10-08 04:46:00 | NOAA-21 | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | 2.1 |
| 53309f35-fada-3961-ac2c-d0537130882a | -5.8199 | -53.83603 | 2026-10-08 04:46:00 | NOAA-21 | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 1.8 |
| 07d9e889-25a4-39f3-98dd-ce85fb3f913e | -7.33929 | -47.49574 | 2026-10-08 04:46:00 | NOAA-21 | FILADÉLFIA | TOCANTINS | Brasil | 1707702 | 17 | 33 | nan | nan | nan | Cerrado | 2.6 |
| 42511133-c5dc-3b2a-89b4-53dc65a17250 | -4.46619 | -54.97145 | 2026-10-08 04:46:00 | NOAA-21 | RURÓPOLIS | PARÁ | Brasil | 1506195 | 15 | 33 | nan | nan | nan | Amazônia | 1.9 |
| 3334dc83-d402-3089-ae7b-09ee17deda24 | -9.79983 | -44.77795 | 2026-10-08 04:46:00 | NOAA-21 | RIACHO FRIO | PIAUÍ | Brasil | 2208858 | 22 | 33 | nan | nan | nan | Cerrado | 4.3 |
| 87b40754-2bad-30b9-bc19-d3dabc36a691 | -3.84614 | -51.92933 | 2026-10-08 04:46:00 | NOAA-21 | SENADOR JOSÉ PORFÍRIO | PARÁ | Brasil | 1507805 | 15 | 33 | nan | nan | nan | Amazônia | 0.7 |
| fedcd47e-4e09-3369-83ad-076bb0fe1884 | -2.93402 | -53.93889 | 2026-10-08 04:46:00 | NOAA-21 | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | 2.4 |
| 7614efd3-a584-301c-bbf3-9fe51785392b | -5.05285 | -45.19923 | 2026-10-08 04:46:00 | NOAA-21 | SÃO RAIMUNDO DO DOCA BEZERRA | MARANHÃO | Brasil | 2111631 | 21 | 33 | nan | nan | nan | Cerrado | 1.3 |
| fab466d1-ebd3-3eb8-a55b-6990c1358918 | -3.00412 | -57.75331 | 2026-10-08 04:46:00 | NOAA-21 | BOA VISTA DO RAMOS | AMAZONAS | Brasil | 1300680 | 13 | 33 | nan | nan | nan | Amazônia | 1.8 |
| 38b1a9a6-4c14-3b69-9e03-3fc73ff97bf6 | -3.27685 | -51.04944 | 2026-10-08 04:46:00 | NOAA-21 | PACAJÁ | PARÁ | Brasil | 1505486 | 15 | 33 | nan | nan | nan | Amazônia | 1.2 |
| 3ac3d878-9b8b-3f17-ab29-d30bfa37f9c9 | -8.3857 | -46.30257 | 2026-10-08 04:46:00 | NOAA-21 | BALSAS | MARANHÃO | Brasil | 2101400 | 21 | 33 | nan | nan | nan | Cerrado | 3.9 |
| 9943b019-e1a2-37b7-81ed-96660e39383f | -9.89786 | -44.81322 | 2026-10-08 04:46:00 | NOAA-21 | RIACHO FRIO | PIAUÍ | Brasil | 2208858 | 22 | 33 | nan | nan | nan | Cerrado | 7.8 |
| 7ec7afa1-b776-3e1f-a1a2-8d3b38546017 | -4.23789 | -49.99209 | 2026-10-08 04:46:00 | NOAA-21 | NOVO REPARTIMENTO | PARÁ | Brasil | 1505064 | 15 | 33 | nan | nan | nan | Amazônia | 2.9 |
| dd044626-f1b7-3a69-9c38-ffce5fa8cdf7 | -6.82678 | -44.86424 | 2026-10-08 04:46:00 | NOAA-21 | SÃO FÉLIX DE BALSAS | MARANHÃO | Brasil | 2110807 | 21 | 33 | nan | nan | nan | Cerrado | 5.5 |
| dfbbe83a-0f7c-3604-8b72-1ba0fa053e86 | -5.48514 | -42.8451 | 2026-10-08 04:46:00 | NOAA-21 | NAZÁRIA | PIAUÍ | Brasil | 2206720 | 22 | 33 | nan | nan | nan | Caatinga | 2.9 |
| d57fc0e2-f185-3072-993e-9e1cf54b94b8 | -6.04147 | -53.60531 | 2026-10-08 04:46:00 | NOAA-21 | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 5.0 |
| e4d95d76-ad6a-32f3-9f92-3f7329871069 | -5.51277 | -46.11733 | 2026-10-08 04:46:00 | NOAA-21 | GRAJAÚ | MARANHÃO | Brasil | 2104800 | 21 | 33 | nan | nan | nan | Cerrado | 1.8 |
| c387afed-ccc1-3421-8c2a-b7e6ac59ab17 | -4.53798 | -55.61853 | 2026-10-08 04:46:00 | NOAA-21 | ITAITUBA | PARÁ | Brasil | 1503606 | 15 | 33 | nan | nan | nan | Amazônia | 2.3 |
| af0c570c-a46c-30bb-9e93-5f221efddef6 | -3.02589 | -54.09362 | 2026-10-08 04:46:00 | NOAA-21 | SANTARÉM | PARÁ | Brasil | 1506807 | 15 | 33 | nan | nan | nan | Amazônia | 3.0 |
| 84711490-086d-34a5-bce1-13189a2e1218 | -2.93298 | -56.58803 | 2026-10-08 04:46:00 | NOAA-21 | JURUTI | PARÁ | Brasil | 1503903 | 15 | 33 | nan | nan | nan | Amazônia | 1.7 |
| 3e148efc-8a05-3544-b353-ebae552d7ec8 | -3.30058 | -54.0391 | 2026-10-08 04:46:00 | NOAA-21 | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | 3.7 |
| cd2aa1c1-d186-3149-8594-d6724d558b7f | -3.35383 | -59.5049 | 2026-10-08 04:46:00 | NOAA-21 | CAREIRO DA VÁRZEA | AMAZONAS | Brasil | 1301159 | 13 | 33 | nan | nan | nan | Amazônia | 1.6 |
| c2abe635-44b1-31e5-b77d-8ca02ff3819d | -3.43122 | -59.62522 | 2026-10-08 04:46:00 | NOAA-21 | CAREIRO DA VÁRZEA | AMAZONAS | Brasil | 1301159 | 13 | 33 | nan | nan | nan | Amazônia | 1.2 |
| 5975a1a7-6468-3b44-8fa8-160e46132bd8 | -3.36244 | -58.18354 | 2026-10-08 04:46:00 | NOAA-21 | ITACOATIARA | AMAZONAS | Brasil | 1301902 | 13 | 33 | nan | nan | nan | Amazônia | 1.0 |
| 2f99519e-60c9-3fb4-a212-a67334bed70f | -3.09162 | -54.29243 | 2026-10-08 04:46:00 | NOAA-21 | MOJUÍ DOS CAMPOS | PARÁ | Brasil | 1504752 | 15 | 33 | nan | nan | nan | Amazônia | 2.6 |
| ca085aed-dc84-3b46-bc52-54d2b62d83c4 | -3.16894 | -54.73656 | 2026-10-08 04:46:00 | NOAA-21 | MOJUÍ DOS CAMPOS | PARÁ | Brasil | 1504752 | 15 | 33 | nan | nan | nan | Amazônia | 4.6 |
| da79f7de-3e1c-3517-a048-b6602216dba5 | -5.12537 | -47.11294 | 2026-10-08 04:46:00 | NOAA-21 | JOÃO LISBOA | MARANHÃO | Brasil | 2105500 | 21 | 33 | nan | nan | nan | Amazônia | 2.5 |
| 14a78a3d-cf85-3976-bd89-5c0114908c32 | -3.30473 | -53.87054 | 2026-10-08 04:46:00 | NOAA-21 | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | 1.7 |
| 20956884-21fd-3ce1-9fb4-98d2c2bb4cb5 | -5.50011 | -42.84738 | 2026-10-08 04:46:00 | NOAA-21 | TERESINA | PIAUÍ | Brasil | 2211001 | 22 | 33 | nan | nan | nan | Caatinga | 2.4 |
| bc7d927f-3a6a-34bc-8ba9-6e8ec49f541b | -2.99336 | -54.0841 | 2026-10-08 04:46:00 | NOAA-21 | SANTARÉM | PARÁ | Brasil | 1506807 | 15 | 33 | nan | nan | nan | Amazônia | 38.1 |
| cbe5d165-9d7d-364b-aac2-00e28697e068 | -3.3655 | -58.19467 | 2026-10-08 04:46:00 | NOAA-21 | ITACOATIARA | AMAZONAS | Brasil | 1301902 | 13 | 33 | nan | nan | nan | Amazônia | 1.2 |
| ca9c5952-7987-3bf8-8ba2-b78717f9db38 | -4.21799 | -56.05107 | 2026-10-08 04:46:00 | NOAA-21 | ITAITUBA | PARÁ | Brasil | 1503606 | 15 | 33 | nan | nan | nan | Amazônia | 0.9 |
| 54188f55-0415-3624-8fa6-328e3e8915a2 | -3.22887 | -54.35447 | 2026-10-08 04:46:00 | NOAA-21 | MOJUÍ DOS CAMPOS | PARÁ | Brasil | 1504752 | 15 | 33 | nan | nan | nan | Amazônia | 2.2 |
| 92ed681a-1340-344a-b880-d71af679110a | -4.23566 | -49.98463 | 2026-10-08 04:46:00 | NOAA-21 | NOVO REPARTIMENTO | PARÁ | Brasil | 1505064 | 15 | 33 | nan | nan | nan | Amazônia | 1.3 |
| 7c505ef0-35bd-3c7f-851d-887b1323efd6 | -3.28366 | -54.02761 | 2026-10-08 04:46:00 | NOAA-21 | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | 1.2 |
| 227607bc-964a-3093-ba48-9530b230af47 | -3.28819 | -54.04596 | 2026-10-08 04:46:00 | NOAA-21 | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | 2.6 |
| fe29353d-70ec-32b2-babc-659e389c91bc | -2.49377 | -56.16407 | 2026-10-08 04:46:00 | NOAA-21 | JURUTI | PARÁ | Brasil | 1503903 | 15 | 33 | nan | nan | nan | Amazônia | 4.2 |
| d74f996f-0bac-3859-b72f-2790af829ea1 | -3.01346 | -53.95847 | 2026-10-08 04:46:00 | NOAA-21 | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | 1.1 |
| 250c3883-22e7-3caf-9054-67ce53020f23 | -2.94823 | -54.05917 | 2026-10-08 04:46:00 | NOAA-21 | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | 1.3 |
| 3d0042b9-2a5d-30b8-8d5e-9a8e0e0166ee | -3.85953 | -55.99255 | 2026-10-08 04:46:00 | NOAA-21 | AVEIRO | PARÁ | Brasil | 1501006 | 15 | 33 | nan | nan | nan | Amazônia | 2.1 |
| 18a63fd0-74b5-3e87-9597-f1404ddce79a | -3.28054 | -54.07289 | 2026-10-08 04:46:00 | NOAA-21 | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | 2.5 |
| 8fe7270b-fc3d-31a0-a408-f80e562fb421 | -3.10979 | -53.78053 | 2026-10-08 04:46:00 | NOAA-21 | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | 6.4 |
| 90001af4-979d-3859-bb21-469f6aaaa52a | -7.59902 | -42.38934 | 2026-10-08 04:46:00 | NOAA-21 | SÃO MIGUEL DO FIDALGO | PIAUÍ | Brasil | 2210391 | 22 | 33 | nan | nan | nan | Caatinga | 0.8 |
| 50028602-a559-3c13-b683-d220812fa065 | -5.70709 | -53.49781 | 2026-10-08 04:46:00 | NOAA-21 | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 7.2 |
| da882c10-3f74-305b-a5f6-3a97ee4ba6cc | -3.84146 | -55.9746 | 2026-10-08 04:46:00 | NOAA-21 | AVEIRO | PARÁ | Brasil | 1501006 | 15 | 33 | nan | nan | nan | Amazônia | 3.0 |
| 6745b929-6bde-34f2-aa56-296a21335451 | -2.94338 | -54.11221 | 2026-10-08 04:46:00 | NOAA-21 | SANTARÉM | PARÁ | Brasil | 1506807 | 15 | 33 | nan | nan | nan | Amazônia | 2.2 |
| 90d24c22-f35a-3e15-b76b-023839e4fb4f | -3.66394 | -60.61116 | 2026-10-08 04:46:00 | NOAA-21 | MANAQUIRI | AMAZONAS | Brasil | 1302553 | 13 | 33 | nan | nan | nan | Amazônia | 1.8 |
| 5b3f8f4e-22d9-3039-8a8e-4206099c1d9d | -8.08044 | -55.2927 | 2026-10-08 04:46:00 | NOAA-21 | NOVO PROGRESSO | PARÁ | Brasil | 1505031 | 15 | 33 | nan | nan | nan | Amazônia | 1.5 |
| f51ce465-0056-321c-b2fa-2b4ad5ebaca9 | -3.03233 | -54.07673 | 2026-10-08 04:46:00 | NOAA-21 | SANTARÉM | PARÁ | Brasil | 1506807 | 15 | 33 | nan | nan | nan | Amazônia | 5.0 |
| 7aaf3929-2142-3c93-877f-7da3dbc2ac3c | -6.22854 | -52.65885 | 2026-10-08 04:46:00 | NOAA-21 | SÃO FÉLIX DO XINGU | PARÁ | Brasil | 1507300 | 15 | 33 | nan | nan | nan | Amazônia | 1.7 |
| 76083485-83e4-3e2b-9733-e9dd825941d5 | -3.10565 | -53.77684 | 2026-10-08 04:46:00 | NOAA-21 | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | 3.4 |
| 16d180f0-a49b-3412-ad88-1c49636d0888 | -5.85009 | -53.55186 | 2026-10-08 04:46:00 | NOAA-21 | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 1.9 |
| 24a13db7-fd88-3463-8f4e-2d28389e96f0 | -11.73904 | -43.64265 | 2026-10-08 04:46:00 | NOAA-21 | BARRA | BAHIA | Brasil | 2902708 | 29 | 33 | nan | nan | nan | Cerrado | 1.2 |
| 5bda3949-eda0-377e-9747-c0e0889cd772 | -3.01021 | -54.07327 | 2026-10-08 04:46:00 | NOAA-21 | SANTARÉM | PARÁ | Brasil | 1506807 | 15 | 33 | nan | nan | nan | Amazônia | 5.2 |
| a4e5df79-ea37-3f02-9383-70322b695513 | -8.20755 | -46.33075 | 2026-10-08 04:46:00 | NOAA-21 | BALSAS | MARANHÃO | Brasil | 2101400 | 21 | 33 | nan | nan | nan | Cerrado | 5.5 |
| 396afc71-c5c5-3d61-813b-6a4841e46433 | -3.70185 | -54.20292 | 2026-10-08 04:46:00 | NOAA-21 | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | 2.2 |
| 5979aace-92c6-3126-8e55-c7b48353836e | -5.76092 | -42.0724 | 2026-10-08 04:46:00 | NOAA-21 | SANTA CRUZ DOS MILAGRES | PIAUÍ | Brasil | 2209153 | 22 | 33 | nan | nan | nan | Caatinga | 5.4 |
| a5d73779-f211-3b02-853e-ca997907181f | -5.90996 | -53.88319 | 2026-10-08 04:46:00 | NOAA-21 | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 0.9 |
| 3450fa6f-3db0-3cf4-aa77-322e20f6c7a5 | -5.96073 | -55.36165 | 2026-10-08 04:46:00 | NOAA-21 | ITAITUBA | PARÁ | Brasil | 1503606 | 15 | 33 | nan | nan | nan | Amazônia | 5.4 |
| eec3cdc7-563e-3c53-aced-19d4ba79dcd8 | -5.73072 | -45.15141 | 2026-10-08 04:46:00 | NOAA-21 | BARRA DO CORDA | MARANHÃO | Brasil | 2101608 | 21 | 33 | nan | nan | nan | Cerrado | 8.0 |
| 0fa93499-e3df-38d6-90a0-3403826678bb | -3.01884 | -57.7375 | 2026-10-08 04:46:00 | NOAA-21 | BOA VISTA DO RAMOS | AMAZONAS | Brasil | 1300680 | 13 | 33 | nan | nan | nan | Amazônia | 1.7 |
| 0eeb3c7e-8b18-3b41-84a7-8f64a2dfe634 | -6.04662 | -53.48405 | 2026-10-08 04:46:00 | NOAA-21 | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 2.8 |
| fbcf7ec7-23d7-3424-9853-9ee28a3077b2 | -3.29914 | -54.67079 | 2026-10-08 04:46:00 | NOAA-21 | MOJUÍ DOS CAMPOS | PARÁ | Brasil | 1504752 | 15 | 33 | nan | nan | nan | Amazônia | 1.4 |
| a13bad85-884c-3737-887b-8739a195f303 | -10.43014 | -47.26677 | 2026-10-08 04:46:00 | NOAA-21 | PONTE ALTA DO TOCANTINS | TOCANTINS | Brasil | 1717909 | 17 | 33 | nan | nan | nan | Cerrado | 4.8 |
| 7edbc481-bf65-3024-850b-051878b24e36 | -6.32254 | -43.34429 | 2026-10-08 04:46:00 | NOAA-21 | SUCUPIRA DO RIACHÃO | MARANHÃO | Brasil | 2111953 | 21 | 33 | nan | nan | nan | Cerrado | 4.7 |
| de410193-27c9-3965-9ba4-2f85761e7972 | -6.99335 | -40.03691 | 2026-10-08 04:46:00 | NOAA-21 | ASSARÉ | CEARÁ | Brasil | 2301604 | 23 | 33 | nan | nan | nan | Caatinga | 1.4 |
| 26ab5a1d-04ae-36dd-aa07-905a0ff1f993 | -2.57041 | -56.17235 | 2026-10-08 04:46:00 | NOAA-21 | JURUTI | PARÁ | Brasil | 1503903 | 15 | 33 | nan | nan | nan | Amazônia | 4.2 |
| e8eda141-120e-3d48-b687-91e718593f9e | -3.28941 | -54.01532 | 2026-10-08 04:46:00 | NOAA-21 | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | 1.7 |
| 87e05a52-92ab-3ac3-8070-b8929b5b78a3 | -4.80779 | -54.68078 | 2026-10-08 04:46:00 | NOAA-21 | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 3.4 |
| bf3a65af-243f-3e6a-af11-2487a4c47a9c | -2.98794 | -54.14169 | 2026-10-08 04:46:00 | NOAA-21 | SANTARÉM | PARÁ | Brasil | 1506807 | 15 | 33 | nan | nan | nan | Amazônia | 3.2 |
| e7d27fae-5401-3bf8-8077-ca018f0e8377 | -3.54739 | -50.10044 | 2026-10-08 04:46:00 | NOAA-21 | PACAJÁ | PARÁ | Brasil | 1505486 | 15 | 33 | nan | nan | nan | Amazônia | 2.0 |
| 033101cf-85c7-3797-8799-8d63edd629a3 | -3.5847 | -54.68348 | 2026-10-08 04:46:00 | NOAA-21 | PLACAS | PARÁ | Brasil | 1505650 | 15 | 33 | nan | nan | nan | Amazônia | 15.7 |
| a336807d-bcc4-3a9f-b4b4-4330d8d5483f | -4.29494 | -48.60746 | 2026-10-08 04:46:00 | NOAA-21 | RONDON DO PARÁ | PARÁ | Brasil | 1506187 | 15 | 33 | nan | nan | nan | Amazônia | 1.8 |
| bf8ea55a-f96f-3b34-96fe-ba5a2b087c67 | -2.51312 | -56.25716 | 2026-10-08 04:46:00 | NOAA-21 | JURUTI | PARÁ | Brasil | 1503903 | 15 | 33 | nan | nan | nan | Amazônia | 4.0 |
| b9cec841-d305-34e9-a911-e04714128181 | -7.62939 | -45.38347 | 2026-10-08 04:46:00 | NOAA-21 | RIBEIRO GONÇALVES | PIAUÍ | Brasil | 2208908 | 22 | 33 | nan | nan | nan | Cerrado | 2.1 |
| 08d332a5-8c40-3ef3-be47-1c18dad7c13c | -3.70225 | -50.65536 | 2026-10-08 04:46:00 | NOAA-21 | PACAJÁ | PARÁ | Brasil | 1505486 | 15 | 33 | nan | nan | nan | Amazônia | 1.1 |
| 5c6f6e01-b861-3b9a-897f-e4fa9a4867fd | -2.48133 | -56.10576 | 2026-10-08 04:46:00 | NOAA-21 | JURUTI | PARÁ | Brasil | 1503903 | 15 | 33 | nan | nan | nan | Amazônia | 2.8 |
| 6a0da55f-feea-30de-a2cc-4a42747a2be5 | -3.10763 | -53.76414 | 2026-10-08 04:46:00 | NOAA-21 | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | 1.7 |
| bee96cce-9a5c-3673-af2f-d3439ac55dd2 | -3.06716 | -59.28006 | 2026-10-08 04:46:00 | NOAA-21 | ITACOATIARA | AMAZONAS | Brasil | 1301902 | 13 | 33 | nan | nan | nan | Amazônia | 1.8 |


[Clique aqui para ver as próximas entradas](README82.md)
