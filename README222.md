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

## Dados Diários - Página 222

| ID | Latitude | Longitude | Data/Hora GMT | Satélite | Município | Estado | País | Município ID | Estado ID | País ID | Dias sem Chuva | Precipitação | Risco de Fogo | Bioma | FRP |
|----|----------|-----------|---------------|----------|-----------|--------|------|--------------|-----------|---------|----------------|--------------|----------------|-------|-----|
| 778b812d-984d-3c03-836f-63269abf6a49 | 1.71343 | -55.60682 | 2026-10-07 16:39:00 | NPP-375 | ÓBIDOS | PARÁ | Brasil | 1505106 | 15 | 33 | nan | nan | nan | Amazônia | 4.9 |
| c05b5841-186a-3381-8c33-86bb55bc9b1c | -2.49694 | -56.12539 | 2026-10-07 16:39:00 | NPP-375 | JURUTI | PARÁ | Brasil | 1503903 | 15 | 33 | nan | nan | nan | Amazônia | 11.6 |
| bc015b53-e1e4-37f5-917f-ab61b8b2dd01 | -2.85191 | -43.89354 | 2026-10-07 16:39:00 | NPP-375 | MORROS | MARANHÃO | Brasil | 2107100 | 21 | 33 | nan | nan | nan | Cerrado | 3.9 |
| e2d0721a-aa91-34bf-bdf8-e3686a5564e1 | -3.46893 | -50.08857 | 2026-10-07 16:39:00 | NPP-375 | PACAJÁ | PARÁ | Brasil | 1505486 | 15 | 33 | nan | nan | nan | Amazônia | 3.0 |
| 346edd08-2013-3eb5-9daa-1ca235ea3ad6 | -3.09171 | -53.72904 | 2026-10-07 16:39:00 | NPP-375 | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | 9.8 |
| 79519eaa-7b5e-3813-a58b-21e27dffdca5 | -2.88271 | -54.12509 | 2026-10-07 16:39:00 | NPP-375 | SANTARÉM | PARÁ | Brasil | 1506807 | 15 | 33 | nan | nan | nan | Amazônia | 8.3 |
| 2e8b8f0e-298b-304a-854e-4029d810bfea | -3.86273 | -55.99654 | 2026-10-07 16:39:00 | NPP-375 | AVEIRO | PARÁ | Brasil | 1501006 | 15 | 33 | nan | nan | nan | Amazônia | 7.0 |
| 1e43cb6c-15f6-3040-8e0c-ebc9d8fc3fc3 | -4.25128 | -51.04684 | 2026-10-07 16:39:00 | NPP-375 | ANAPU | PARÁ | Brasil | 1500859 | 15 | 33 | nan | nan | nan | Amazônia | 6.6 |
| 0bb0a318-475e-3c53-aeb8-12c94d7f9f7b | -4.14311 | -54.02819 | 2026-10-07 16:39:00 | NPP-375 | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | 4.0 |
| b51e3f78-e60f-30ca-9e64-3f77a521f423 | -2.13447 | -54.45516 | 2026-10-07 16:39:00 | NPP-375 | MONTE ALEGRE | PARÁ | Brasil | 1504802 | 15 | 33 | nan | nan | nan | Amazônia | 8.1 |
| 6d088ce7-cece-3ce4-9978-478d5c96beb9 | -1.12893 | -57.2271 | 2026-10-07 16:39:00 | NPP-375 | ORIXIMINÁ | PARÁ | Brasil | 1505304 | 15 | 33 | nan | nan | nan | Amazônia | 5.9 |
| 36e2bf0c-5daa-3cf7-a9f3-32ecaea6837e | -3.88553 | -52.24957 | 2026-10-07 16:39:00 | NPP-375 | SENADOR JOSÉ PORFÍRIO | PARÁ | Brasil | 1507805 | 15 | 33 | nan | nan | nan | Amazônia | 10.9 |
| 56a898b2-5d00-3710-a052-5c7878e75f54 | -3.17291 | -50.44446 | 2026-10-07 16:39:00 | NPP-375 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 7.2 |
| e0971257-9fd8-36fa-a925-e1a639b83fc8 | -3.44758 | -56.9335 | 2026-10-07 16:39:00 | NPP-375 | BARREIRINHA | AMAZONAS | Brasil | 1300508 | 13 | 33 | nan | nan | nan | Amazônia | 266.9 |
| a8c52e58-8c65-3103-b5c3-5e8bdac0a661 | -1.75685 | -55.11979 | 2026-10-07 16:39:00 | NPP-375 | CURUÁ | PARÁ | Brasil | 1502855 | 15 | 33 | nan | nan | nan | Amazônia | 88.8 |
| dae3381d-9f43-3908-8ae6-f66ac6feba8c | -3.00037 | -54.1214 | 2026-10-07 16:39:00 | NPP-375 | SANTARÉM | PARÁ | Brasil | 1506807 | 15 | 33 | nan | nan | nan | Amazônia | 4.6 |
| f1621b49-2b7d-3421-af13-0aa94a5c9343 | -2.83348 | -48.64898 | 2026-10-07 16:39:00 | NPP-375 | TAILÂNDIA | PARÁ | Brasil | 1507953 | 15 | 33 | nan | nan | nan | Amazônia | 11.3 |
| 27828935-0507-33cc-b6fc-fbc47b4ec9d3 | -3.54607 | -54.64047 | 2026-10-07 16:39:00 | NPP-375 | PLACAS | PARÁ | Brasil | 1505650 | 15 | 33 | nan | nan | nan | Amazônia | 3.6 |
| a9db16ca-f024-329b-ad73-cf4f754be2d1 | -3.09718 | -54.2841 | 2026-10-07 16:39:00 | NPP-375 | MOJUÍ DOS CAMPOS | PARÁ | Brasil | 1504752 | 15 | 33 | nan | nan | nan | Amazônia | 5.6 |
| da190802-3173-31b1-8783-34bdd5048752 | -3.0697 | -54.24989 | 2026-10-07 16:39:00 | NPP-375 | MOJUÍ DOS CAMPOS | PARÁ | Brasil | 1504752 | 15 | 33 | nan | nan | nan | Amazônia | 9.5 |
| 9be9aef4-98f6-39ef-a635-1eac691be325 | -2.9038 | -54.1926 | 2026-10-07 16:39:00 | NPP-375 | SANTARÉM | PARÁ | Brasil | 1506807 | 15 | 33 | nan | nan | nan | Amazônia | 2.1 |
| b6fe341c-37d9-3393-bf86-8f956e8cd413 | -3.28409 | -54.0646 | 2026-10-07 16:39:00 | NPP-375 | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | 7.0 |
| cbd964c6-d8f2-307f-8011-f2f0dabaa248 | 1.35025 | -56.13521 | 2026-10-07 16:39:00 | NPP-375 | ORIXIMINÁ | PARÁ | Brasil | 1505304 | 15 | 33 | nan | nan | nan | Amazônia | 6.5 |
| 047e0dfd-df97-31bd-bc9f-1824e0452d26 | -2.92497 | -54.11208 | 2026-10-07 16:39:00 | NPP-375 | SANTARÉM | PARÁ | Brasil | 1506807 | 15 | 33 | nan | nan | nan | Amazônia | 3.3 |
| 7dce6dd0-5042-3ab9-bd7c-1f6571e01184 | -3.86206 | -55.99176 | 2026-10-07 16:39:00 | NPP-375 | AVEIRO | PARÁ | Brasil | 1501006 | 15 | 33 | nan | nan | nan | Amazônia | 9.1 |
| cb342563-3bea-37d2-ac7b-a4588fd27166 | -2.04926 | -54.30277 | 2026-10-07 16:39:00 | NPP-375 | MONTE ALEGRE | PARÁ | Brasil | 1504802 | 15 | 33 | nan | nan | nan | Amazônia | 8.6 |
| 35ce80cf-c658-3ee5-ba79-826958839ee1 | -3.01047 | -54.75573 | 2026-10-07 16:39:00 | NPP-375 | MOJUÍ DOS CAMPOS | PARÁ | Brasil | 1504752 | 15 | 33 | nan | nan | nan | Amazônia | 7.3 |
| 01340333-df37-3044-aa69-af9b43ef5a4c | -2.9476 | -54.06278 | 2026-10-07 16:39:00 | NPP-375 | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | 18.4 |
| ce799422-906d-316f-aec6-b7cfdcf2fd8a | -1.52521 | -54.51461 | 2026-10-07 16:39:00 | NPP-375 | ALENQUER | PARÁ | Brasil | 1500404 | 15 | 33 | nan | nan | nan | Amazônia | 2.1 |
| d6bcdfb0-ed1f-3dbf-a65a-ee92035b53a9 | -2.58242 | -56.1566 | 2026-10-07 16:39:00 | NPP-375 | JURUTI | PARÁ | Brasil | 1503903 | 15 | 33 | nan | nan | nan | Amazônia | 18.7 |
| 7de48bd7-d3bc-377b-b495-1d042d49825b | -2.9995 | -54.0414 | 2026-10-07 16:39:00 | NPP-375 | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | 8.0 |
| 76c4bc2c-d0a4-3968-b858-2310c6355ada | -3.6586 | -50.94632 | 2026-10-07 16:39:00 | NPP-375 | PACAJÁ | PARÁ | Brasil | 1505486 | 15 | 33 | nan | nan | nan | Amazônia | 20.9 |
| f8ab0a8b-89e4-362e-9d9d-a103408e40c6 | -3.18312 | -57.85984 | 2026-10-07 16:39:00 | NPP-375 | BOA VISTA DO RAMOS | AMAZONAS | Brasil | 1300680 | 13 | 33 | nan | nan | nan | Amazônia | 7.3 |
| 7e73ca60-04e5-3a87-b054-f457424752d8 | -4.14049 | -54.91494 | 2026-10-07 16:39:00 | NPP-375 | RURÓPOLIS | PARÁ | Brasil | 1506195 | 15 | 33 | nan | nan | nan | Amazônia | 8.7 |
| eeec33b2-98e7-3f20-90b7-a981a8a6232d | -2.93834 | -54.15149 | 2026-10-07 16:39:00 | NPP-375 | SANTARÉM | PARÁ | Brasil | 1506807 | 15 | 33 | nan | nan | nan | Amazônia | 12.3 |
| 78742ec9-7897-37ca-8dac-6c5270aa66f7 | -4.1357 | -54.2531 | 2026-10-07 16:39:00 | NPP-375 | PLACAS | PARÁ | Brasil | 1505650 | 15 | 33 | nan | nan | nan | Amazônia | 9.1 |
| 45a01cab-6253-31ac-98c5-daa6481bf909 | -0.79466 | -49.51468 | 2026-10-07 16:39:00 | NPP-375 | PONTA DE PEDRAS | PARÁ | Brasil | 1505700 | 15 | 33 | nan | nan | nan | Amazônia | 6.5 |
| 1b37be54-5632-3fa7-a2ef-6dda52054130 | -1.63106 | -55.41963 | 2026-10-07 16:39:00 | NPP-375 | ÓBIDOS | PARÁ | Brasil | 1505106 | 15 | 33 | nan | nan | nan | Amazônia | 5.1 |
| 8551e01f-3a85-3c62-935f-c01cbe9ba7f5 | -1.5279 | -54.83068 | 2026-10-07 16:39:00 | NPP-375 | ALENQUER | PARÁ | Brasil | 1500404 | 15 | 33 | nan | nan | nan | Amazônia | 7.0 |
| dad6177d-7947-3ecb-8c7d-1141921b3ef2 | -3.21694 | -53.88405 | 2026-10-07 16:39:00 | NPP-375 | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | 5.5 |
| b5044e25-7caf-3aa0-b123-31e322e4b4b1 | 1.76108 | -55.58876 | 2026-10-07 16:39:00 | NPP-375 | ÓBIDOS | PARÁ | Brasil | 1505106 | 15 | 33 | nan | nan | nan | Amazônia | 5.8 |
| 8c45d042-1545-34c9-8069-2cd6af2ec3a4 | -1.21977 | -49.04171 | 2026-10-07 16:39:00 | NPP-375 | PONTA DE PEDRAS | PARÁ | Brasil | 1505700 | 15 | 33 | nan | nan | nan | Amazônia | 12.3 |
| 28f859a8-ee44-33fd-9130-32017895f754 | -4.60515 | -56.07457 | 2026-10-07 16:39:00 | NPP-375 | ITAITUBA | PARÁ | Brasil | 1503606 | 15 | 33 | nan | nan | nan | Amazônia | 6.3 |
| ba7aa0f3-1abf-3143-a2c8-79bbe43575f9 | -3.1008 | -53.71787 | 2026-10-07 16:39:00 | NPP-375 | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | 3.2 |
| 03a4f858-8a73-3b54-948c-52f19ac576f4 | -3.26087 | -50.39691 | 2026-10-07 16:39:00 | NPP-375 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 14.2 |
| 472c906c-bf7e-3e27-9ff1-dfb07764f95b | 1.80998 | -55.53281 | 2026-10-07 16:39:00 | NPP-375 | ÓBIDOS | PARÁ | Brasil | 1505106 | 15 | 33 | nan | nan | nan | Amazônia | 9.9 |
| 0d456a6d-8f7b-3a2a-a722-8fc60d7b0ef9 | -3.35097 | -51.6257 | 2026-10-07 16:39:00 | NPP-375 | ANAPU | PARÁ | Brasil | 1500859 | 15 | 33 | nan | nan | nan | Amazônia | 20.5 |
| d922156c-bd04-3823-8873-90b5616fb219 | -3.44179 | -50.63148 | 2026-10-07 16:39:00 | NPP-375 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 10.1 |
| bcc44398-6efd-396b-94b8-1f159b013af6 | -3.40199 | -58.01744 | 2026-10-07 16:39:00 | NPP-375 | MAUÉS | AMAZONAS | Brasil | 1302900 | 13 | 33 | nan | nan | nan | Amazônia | 29.3 |
| 58cf5528-ef16-3385-94d5-b1e7ba6f33c3 | -2.47013 | -56.07254 | 2026-10-07 16:39:00 | NPP-375 | JURUTI | PARÁ | Brasil | 1503903 | 15 | 33 | nan | nan | nan | Amazônia | 4.5 |
| d4ee5441-7fdd-34ec-af0e-173988fed97a | -3.47197 | -50.08065 | 2026-10-07 16:39:00 | NPP-375 | PACAJÁ | PARÁ | Brasil | 1505486 | 15 | 33 | nan | nan | nan | Amazônia | 6.2 |
| b554feca-9ee9-3e12-95e4-4183fa07be4c | -3.94585 | -49.48355 | 2026-10-07 16:39:00 | NPP-375 | BREU BRANCO | PARÁ | Brasil | 1501782 | 15 | 33 | nan | nan | nan | Amazônia | 29.3 |
| f22c302a-0c22-3d38-9e99-bb189431557e | -4.9272 | -55.85456 | 2026-10-07 16:39:00 | NPP-375 | TRAIRÃO | PARÁ | Brasil | 1508050 | 15 | 33 | nan | nan | nan | Amazônia | 15.9 |
| 77d3370d-1b74-3bd0-8cab-8221475f7a90 | -3.27349 | -50.39505 | 2026-10-07 16:39:00 | NPP-375 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 6.1 |
| aa435c15-439f-35f0-aea7-a4bfb950c0b3 | -3.04915 | -54.14476 | 2026-10-07 16:39:00 | NPP-375 | SANTARÉM | PARÁ | Brasil | 1506807 | 15 | 33 | nan | nan | nan | Amazônia | 5.8 |
| ca0bedef-bab8-3a4f-ad51-651a2ec68f93 | -3.9316 | -53.01321 | 2026-10-07 16:39:00 | NPP-375 | BRASIL NOVO | PARÁ | Brasil | 1501725 | 15 | 33 | nan | nan | nan | Amazônia | 7.0 |
| b103fdd3-d612-3607-a2de-cef3c47cfb6e | 1.94886 | -55.13123 | 2026-10-07 16:39:00 | NPP-375 | ALMEIRIM | PARÁ | Brasil | 1500503 | 15 | 33 | nan | nan | nan | Amazônia | 46.1 |
| 254b2a5f-7d24-3c9c-a32a-08b2fabcb5df | -1.2901 | -54.56662 | 2026-10-07 16:39:00 | NPP-375 | MONTE ALEGRE | PARÁ | Brasil | 1504802 | 15 | 33 | nan | nan | nan | Amazônia | 5.5 |
| 56a554c9-71da-3a3b-a849-c39e3aafe6ae | -2.45522 | -46.0246 | 2026-10-07 16:39:00 | NPP-375 | MARANHÃOZINHO | MARANHÃO | Brasil | 2106375 | 21 | 33 | nan | nan | nan | Amazônia | 4.8 |
| dea57ca0-ef10-3182-a006-97c7416fffce | -1.41131 | -55.41335 | 2026-10-07 16:39:00 | NPP-375 | ÓBIDOS | PARÁ | Brasil | 1505106 | 15 | 33 | nan | nan | nan | Amazônia | 4.6 |
| 8e8afa14-f2b5-39ab-a961-2ca217930b06 | -3.13111 | -43.84193 | 2026-10-07 16:39:00 | NPP-375 | CACHOEIRA GRANDE | MARANHÃO | Brasil | 2102374 | 21 | 33 | nan | nan | nan | Cerrado | 17.7 |
| 6c497c48-c36c-39bf-aec4-1c287c0d3d44 | 2.22017 | -55.88931 | 2026-10-07 16:39:00 | NPP-375 | ÓBIDOS | PARÁ | Brasil | 1505106 | 15 | 33 | nan | nan | nan | Amazônia | 5.1 |
| 71d854e3-d55d-3a90-a40d-3f1fb7cf4f80 | 1.89324 | -55.71175 | 2026-10-07 16:39:00 | NPP-375 | ÓBIDOS | PARÁ | Brasil | 1505106 | 15 | 33 | nan | nan | nan | Amazônia | 5.7 |
| c28b60c2-eb4b-34e1-a6ba-f87b7b396f1e | -1.80531 | -57.10495 | 2026-10-07 16:39:00 | NPP-375 | NHAMUNDÁ | AMAZONAS | Brasil | 1303007 | 13 | 33 | nan | nan | nan | Amazônia | 59.0 |
| 1f8b67de-1579-37b0-9711-a691b5f20e1a | -2.13917 | -54.45533 | 2026-10-07 16:39:00 | NPP-375 | MONTE ALEGRE | PARÁ | Brasil | 1504802 | 15 | 33 | nan | nan | nan | Amazônia | 21.7 |
| 6cc2f3da-0649-3d8b-92ae-f1752cee9963 | -4.53813 | -55.61516 | 2026-10-07 16:39:00 | NPP-375 | ITAITUBA | PARÁ | Brasil | 1503606 | 15 | 33 | nan | nan | nan | Amazônia | 88.7 |
| 8021c51f-e398-3dec-b574-b3812ccbe863 | -3.04297 | -54.25788 | 2026-10-07 16:39:00 | NPP-375 | MOJUÍ DOS CAMPOS | PARÁ | Brasil | 1504752 | 15 | 33 | nan | nan | nan | Amazônia | 49.7 |
| 5cd62758-8523-3724-a39d-f3e73cffdcfc | -3.08927 | -53.71297 | 2026-10-07 16:39:00 | NPP-375 | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | 4.4 |
| c2eae171-532c-3eb0-a9e6-b7c6c27efa70 | -3.29985 | -54.0588 | 2026-10-07 16:39:00 | NPP-375 | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | 4.2 |
| 044db4d6-f6cf-3370-865c-e52e2d6fa9b8 | 1.463 | -50.75608 | 2026-10-07 16:39:00 | NPP-375 | TARTARUGALZINHO | AMAPÁ | Brasil | 1600709 | 16 | 33 | nan | nan | nan | Amazônia | 9.1 |
| d80cd235-ee0d-337f-bf3f-9be2491b8f2d | -2.27128 | -53.85744 | 2026-10-07 16:39:00 | NPP-375 | PRAINHA | PARÁ | Brasil | 1506005 | 15 | 33 | nan | nan | nan | Amazônia | 5.9 |
| 56897444-f706-36d9-a95f-9fb476d5edc2 | -4.02977 | -52.13175 | 2026-10-07 16:39:00 | NPP-375 | SENADOR JOSÉ PORFÍRIO | PARÁ | Brasil | 1507805 | 15 | 33 | nan | nan | nan | Amazônia | 7.9 |
| 1d2346dd-6aba-395a-a6c5-a7bceb7e48b6 | -2.9412 | -54.10979 | 2026-10-07 16:39:00 | NPP-375 | SANTARÉM | PARÁ | Brasil | 1506807 | 15 | 33 | nan | nan | nan | Amazônia | 8.4 |
| 28a34cff-cb30-3c56-a8be-36691ca62152 | -1.29691 | -54.56474 | 2026-10-07 16:39:00 | NPP-375 | MONTE ALEGRE | PARÁ | Brasil | 1504802 | 15 | 33 | nan | nan | nan | Amazônia | 4.3 |
| 303f3f57-f6c6-31ad-b850-29b6174fb07a | -3.0451 | -53.92687 | 2026-10-07 16:39:00 | NPP-375 | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | 5.1 |
| 2b6f154a-713a-3b13-a290-d5377429e6bd | -2.55655 | -55.72359 | 2026-10-07 16:39:00 | NPP-375 | SANTARÉM | PARÁ | Brasil | 1506807 | 15 | 33 | nan | nan | nan | Amazônia | 3.7 |
| 543b5b93-5ed9-3afe-a405-3ea61743fc2f | -2.76992 | -54.08193 | 2026-10-07 16:39:00 | NPP-375 | PRAINHA | PARÁ | Brasil | 1506005 | 15 | 33 | nan | nan | nan | Amazônia | 15.4 |
| 6c8967f6-e364-36ae-aaa7-759654a5f139 | -3.06085 | -54.15499 | 2026-10-07 16:39:00 | NPP-375 | SANTARÉM | PARÁ | Brasil | 1506807 | 15 | 33 | nan | nan | nan | Amazônia | 6.3 |
| 9ea23ac0-e1ee-339d-902f-c22dc6e78ba4 | -1.28124 | -55.84996 | 2026-10-07 16:39:00 | NPP-375 | ÓBIDOS | PARÁ | Brasil | 1505106 | 15 | 33 | nan | nan | nan | Amazônia | 37.3 |
| 1860c5b9-6781-36bf-9b11-ea5365b1f7c3 | -3.11456 | -54.17441 | 2026-10-07 16:39:00 | NPP-375 | SANTARÉM | PARÁ | Brasil | 1506807 | 15 | 33 | nan | nan | nan | Amazônia | 24.5 |
| 983c1d2f-db82-3786-b7a2-7b92f87ebeeb | -3.50008 | -51.68375 | 2026-10-07 16:39:00 | NPP-375 | ANAPU | PARÁ | Brasil | 1500859 | 15 | 33 | nan | nan | nan | Amazônia | 52.3 |
| fe5a78eb-6ccc-38dc-a64b-857c7e8eb27e | -1.28091 | -55.41507 | 2026-10-07 16:39:00 | NPP-375 | ÓBIDOS | PARÁ | Brasil | 1505106 | 15 | 33 | nan | nan | nan | Amazônia | 4.5 |
| f61739d7-8ee3-3a16-a7a1-a98d9f113790 | -3.73848 | -51.21397 | 2026-10-07 16:39:00 | NPP-375 | PACAJÁ | PARÁ | Brasil | 1505486 | 15 | 33 | nan | nan | nan | Amazônia | 10.5 |
| 43117feb-1be0-37ec-891c-3d5e3e1d720c | -2.58313 | -56.1613 | 2026-10-07 16:39:00 | NPP-375 | JURUTI | PARÁ | Brasil | 1503903 | 15 | 33 | nan | nan | nan | Amazônia | 6.8 |
| 429a7273-067b-39f2-bab9-8a6638a5239a | -3.00157 | -42.87475 | 2026-10-07 16:39:00 | NPP-375 | BARREIRINHAS | MARANHÃO | Brasil | 2101707 | 21 | 33 | nan | nan | nan | Cerrado | 18.9 |
| d6221da1-16d0-3cfc-bb0e-daaafb2eba51 | -1.28904 | -54.55981 | 2026-10-07 16:39:00 | NPP-375 | MONTE ALEGRE | PARÁ | Brasil | 1504802 | 15 | 33 | nan | nan | nan | Amazônia | 7.9 |
| 87c55cee-80e2-3c64-b0f3-83a9483f3eeb | -3.28893 | -54.02198 | 2026-10-07 16:39:00 | NPP-375 | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | 5.3 |
| b47f848e-acd8-3d4b-8532-587385b887c7 | -2.50045 | -56.14837 | 2026-10-07 16:39:00 | NPP-375 | JURUTI | PARÁ | Brasil | 1503903 | 15 | 33 | nan | nan | nan | Amazônia | 18.1 |
| 32c1dbdf-0716-3f99-924a-23a1c02d32f5 | -1.12292 | -54.11665 | 2026-10-07 16:39:00 | NPP-375 | MONTE ALEGRE | PARÁ | Brasil | 1504802 | 15 | 33 | nan | nan | nan | Amazônia | 2.8 |
| 37be9dab-6538-39c0-abd6-4234b9240472 | -3.54039 | -54.6411 | 2026-10-07 16:39:00 | NPP-375 | PLACAS | PARÁ | Brasil | 1505650 | 15 | 33 | nan | nan | nan | Amazônia | 9.0 |
| 6611acbc-2ae2-38a5-b822-2d172ab428d9 | -3.44052 | -49.25822 | 2026-10-07 16:39:00 | NPP-375 | BREU BRANCO | PARÁ | Brasil | 1501782 | 15 | 33 | nan | nan | nan | Amazônia | 10.4 |
| 89613fdc-9aa6-3583-a0a1-c615273f2045 | -2.76941 | -54.07855 | 2026-10-07 16:39:00 | NPP-375 | PRAINHA | PARÁ | Brasil | 1506005 | 15 | 33 | nan | nan | nan | Amazônia | 15.4 |
| 4b8823fb-dbaa-3191-9ad4-3343278563b9 | -2.27915 | -48.75616 | 2026-10-07 16:39:00 | NPP-375 | MOJU | PARÁ | Brasil | 1504703 | 15 | 33 | nan | nan | nan | Amazônia | 7.9 |
| a267e193-a763-3693-808a-97261e10ddc6 | -3.10291 | -53.76729 | 2026-10-07 16:39:00 | NPP-375 | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | 21.8 |
| a3ec3cf6-9a8a-338b-a973-a1a756aa1af7 | -2.49428 | -56.155 | 2026-10-07 16:39:00 | NPP-375 | JURUTI | PARÁ | Brasil | 1503903 | 15 | 33 | nan | nan | nan | Amazônia | 30.1 |
| 6de64fdd-de54-3e21-ae62-9662575bd1ee | -2.39039 | -56.12607 | 2026-10-07 16:39:00 | NPP-375 | JURUTI | PARÁ | Brasil | 1503903 | 15 | 33 | nan | nan | nan | Amazônia | 18.7 |
| 064e33f3-5f3f-3eae-a3ab-d942c8b0bccf | -4.37731 | -55.45215 | 2026-10-07 16:39:00 | NPP-375 | RURÓPOLIS | PARÁ | Brasil | 1506195 | 15 | 33 | nan | nan | nan | Amazônia | 6.4 |
| c0101d3a-f856-3243-a880-932ccf53fcde | -2.48965 | -58.06446 | 2026-10-07 16:39:00 | NPP-375 | SÃO SEBASTIÃO DO UATUMÃ | AMAZONAS | Brasil | 1303957 | 13 | 33 | nan | nan | nan | Amazônia | 6.2 |
| d6fe10a6-22df-3b8b-ac7b-160705a2dd05 | -3.23406 | -57.8719 | 2026-10-07 16:39:00 | NPP-375 | BOA VISTA DO RAMOS | AMAZONAS | Brasil | 1300680 | 13 | 33 | nan | nan | nan | Amazônia | 28.4 |
| a9218e5d-f4cd-3015-a376-d8fea60c9063 | 3.40699 | -51.30025 | 2026-10-07 16:39:00 | NPP-375 | OIAPOQUE | AMAPÁ | Brasil | 1600501 | 16 | 33 | nan | nan | nan | Amazônia | 3.7 |


[Clique aqui para ver as próximas entradas](README223.md)
