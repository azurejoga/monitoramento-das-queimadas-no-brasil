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

## Dados Diários - Página 65

| ID | Latitude | Longitude | Data/Hora GMT | Satélite | Município | Estado | País | Município ID | Estado ID | País ID | Dias sem Chuva | Precipitação | Risco de Fogo | Bioma | FRP |
|----|----------|-----------|---------------|----------|-----------|--------|------|--------------|-----------|---------|----------------|--------------|----------------|-------|-----|
| 91600513-2df7-3901-8847-385ed984376d | -15.09881 | -54.62339 | 2024-11-28 04:25:00 | NOAA-20 | CAMPO VERDE | MATO GROSSO | Brasil | 5102678 | 51 | 33 | nan | nan | nan | Cerrado | 1.2 |
| 0add756e-b5e6-3348-b470-5e71a4594050 | -3.84197 | -49.90202 | 2024-11-28 04:25:00 | NOAA-20 | TUCURUÍ | PARÁ | Brasil | 1508100 | 15 | 33 | nan | nan | nan | Amazônia | 1.1 |
| 2bb4cbaa-57da-3ee2-bd2b-3554fd671e06 | -2.61864 | -48.12446 | 2024-11-28 04:25:00 | NOAA-20 | TOMÉ-AÇU | PARÁ | Brasil | 1508001 | 15 | 33 | nan | nan | nan | Amazônia | 0.8 |
| 01e61cc8-bcb1-3ee7-b643-490ab040b7fb | -6.01282 | -38.65723 | 2024-11-28 04:25:00 | NOAA-20 | JAGUARIBE | CEARÁ | Brasil | 2306900 | 23 | 33 | nan | nan | nan | Caatinga | 1.5 |
| 65b5145f-730d-3488-b6e3-e7a95afc7a14 | -2.72818 | -48.89979 | 2024-11-28 04:25:00 | NOAA-20 | TAILÂNDIA | PARÁ | Brasil | 1507953 | 15 | 33 | nan | nan | nan | Amazônia | 22.6 |
| 40eec0f8-0133-31d8-a4e7-649eb5390424 | -4.6589 | -49.51937 | 2024-11-28 04:25:00 | NOAA-20 | NOVO REPARTIMENTO | PARÁ | Brasil | 1505064 | 15 | 33 | nan | nan | nan | Amazônia | 8.2 |
| 4e20bd7c-234a-361d-b34e-804514f5ba75 | -3.78116 | -46.68864 | 2024-11-28 04:25:00 | NOAA-20 | BOM JARDIM | MARANHÃO | Brasil | 2102002 | 21 | 33 | nan | nan | nan | Amazônia | 3.2 |
| d83d4732-24cb-35d1-b0d5-047eaf77fba5 | -2.88848 | -51.38936 | 2024-11-28 04:25:00 | NOAA-20 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 0.9 |
| 3e3c12fe-d79a-34fb-8a63-b4d2f916a79e | -4.95049 | -47.80332 | 2024-11-28 04:25:00 | NOAA-20 | CIDELÂNDIA | MARANHÃO | Brasil | 2103257 | 21 | 33 | nan | nan | nan | Amazônia | 0.9 |
| dd322dd3-58de-373a-b7c7-d1e674e7c31a | -3.77881 | -47.9586 | 2024-11-28 04:25:00 | NOAA-20 | ULIANÓPOLIS | PARÁ | Brasil | 1508126 | 15 | 33 | nan | nan | nan | Amazônia | 1.7 |
| 2e681bbd-7d55-3de7-853a-f5389b212793 | -3.10669 | -53.26191 | 2024-11-28 04:25:00 | NOAA-20 | MEDICILÂNDIA | PARÁ | Brasil | 1504455 | 15 | 33 | nan | nan | nan | Amazônia | 1.6 |
| 7e7e7d72-961c-3163-b355-19d9b2f528d7 | -3.43412 | -51.20568 | 2024-11-28 04:25:00 | NOAA-20 | PACAJÁ | PARÁ | Brasil | 1505486 | 15 | 33 | nan | nan | nan | Amazônia | 0.7 |
| e3399cca-5e7b-3252-84d2-02b3deffeb01 | -3.81562 | -46.60047 | 2024-11-28 04:25:00 | NOAA-20 | BOM JARDIM | MARANHÃO | Brasil | 2102002 | 21 | 33 | nan | nan | nan | Amazônia | 2.1 |
| 62845b8f-4196-35ba-9050-ee16cccdcbfc | -2.85927 | -46.86546 | 2024-11-28 04:25:00 | NOAA-20 | PARAGOMINAS | PARÁ | Brasil | 1505502 | 15 | 33 | nan | nan | nan | Amazônia | 1.3 |
| e9f500fc-d9ff-3031-b019-48279f5135d3 | -2.8777 | -50.74113 | 2024-11-28 04:25:00 | NOAA-20 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 0.9 |
| a33a33f8-c714-3454-a51e-d63e7c83f8a8 | -15.10233 | -54.62855 | 2024-11-28 04:25:00 | NOAA-20 | CAMPO VERDE | MATO GROSSO | Brasil | 5102678 | 51 | 33 | nan | nan | nan | Cerrado | 0.9 |
| 16acfce4-cdee-33cd-99eb-cc051bf87b6e | -3.81284 | -46.59645 | 2024-11-28 04:25:00 | NOAA-20 | BOM JARDIM | MARANHÃO | Brasil | 2102002 | 21 | 33 | nan | nan | nan | Amazônia | 3.6 |
| dea7df61-0461-38cd-b754-df4bbc170018 | -3.24131 | -53.63957 | 2024-11-28 04:25:00 | NOAA-20 | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | 3.7 |
| e665750e-2f7c-39e9-af45-6d95d5998be9 | -3.25239 | -50.61852 | 2024-11-28 04:25:00 | NOAA-20 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 4.6 |
| 694b8db5-d72e-3fed-ab35-c8b436b783e7 | -3.46317 | -54.4915 | 2024-11-28 04:25:00 | NOAA-20 | PLACAS | PARÁ | Brasil | 1505650 | 15 | 33 | nan | nan | nan | Amazônia | 1.0 |
| b16e2aa3-9615-3232-a23f-f627efc98d2d | -3.00352 | -47.34669 | 2024-11-28 04:25:00 | NOAA-20 | PARAGOMINAS | PARÁ | Brasil | 1505502 | 15 | 33 | nan | nan | nan | Amazônia | 1.2 |
| eed56031-ca8a-3545-9206-61dae11d9796 | -3.84724 | -46.65609 | 2024-11-28 04:25:00 | NOAA-20 | BOM JARDIM | MARANHÃO | Brasil | 2102002 | 21 | 33 | nan | nan | nan | Amazônia | 1.1 |
| da4bbcd8-08cc-3ae3-a382-512d35136b38 | -4.05884 | -48.33564 | 2024-11-28 04:25:00 | NOAA-20 | DOM ELISEU | PARÁ | Brasil | 1502939 | 15 | 33 | nan | nan | nan | Amazônia | 2.5 |
| 69d68c6d-fd8d-3f7f-a9ff-d0370b4fd83d | -2.24255 | -53.62708 | 2024-11-28 04:25:00 | NOAA-20 | PRAINHA | PARÁ | Brasil | 1506005 | 15 | 33 | nan | nan | nan | Amazônia | 1.1 |
| 2a5aa005-099a-3b0e-b650-484af7111137 | -2.93864 | -48.34042 | 2024-11-28 04:25:00 | NOAA-20 | TOMÉ-AÇU | PARÁ | Brasil | 1508001 | 15 | 33 | nan | nan | nan | Amazônia | 2.4 |
| 31987446-fd80-39c2-8980-06dc724f9fdc | -4.00261 | -46.31937 | 2024-11-28 04:25:00 | NOAA-20 | BOM JARDIM | MARANHÃO | Brasil | 2102002 | 21 | 33 | nan | nan | nan | Amazônia | 1.0 |
| b7a97551-85ff-30c7-8a58-94cfddd7c008 | -3.97434 | -46.73367 | 2024-11-28 04:25:00 | NOAA-20 | BOM JARDIM | MARANHÃO | Brasil | 2102002 | 21 | 33 | nan | nan | nan | Amazônia | 1.5 |
| 8c8949b8-2a59-35b7-9d29-7f13ae0f8c20 | -3.97378 | -46.73721 | 2024-11-28 04:25:00 | NOAA-20 | BOM JARDIM | MARANHÃO | Brasil | 2102002 | 21 | 33 | nan | nan | nan | Amazônia | 1.5 |
| 6eaf19ae-c4c7-3203-a2a6-ba63eb07bb55 | -5.22443 | -44.91904 | 2024-11-28 04:25:00 | NOAA-20 | BARRA DO CORDA | MARANHÃO | Brasil | 2101608 | 21 | 33 | nan | nan | nan | Cerrado | 1.4 |
| e34227a2-ccc7-3378-afcc-9c1310f1600c | -3.10515 | -53.11023 | 2024-11-28 04:25:00 | NOAA-20 | MEDICILÂNDIA | PARÁ | Brasil | 1504455 | 15 | 33 | nan | nan | nan | Amazônia | 1.7 |
| e7352e8a-dd2f-39bf-bc41-4caeb6eb776b | -4.24638 | -48.58942 | 2024-11-28 04:25:00 | NOAA-20 | RONDON DO PARÁ | PARÁ | Brasil | 1506187 | 15 | 33 | nan | nan | nan | Amazônia | 0.7 |
| 5ce865e6-240b-3d90-8670-60be45b4878c | -4.10005 | -46.11119 | 2024-11-28 04:25:00 | NOAA-20 | SANTA LUZIA | MARANHÃO | Brasil | 2110005 | 21 | 33 | nan | nan | nan | Amazônia | 0.7 |
| a6da22dc-5050-3524-8160-8b6e5d96de38 | -5.31389 | -43.08372 | 2024-11-28 04:25:00 | NOAA-20 | TIMON | MARANHÃO | Brasil | 2112209 | 21 | 33 | nan | nan | nan | Cerrado | 2.5 |
| b415ca4d-acf1-374b-95b3-a3f5b7148144 | -3.61212 | -50.76478 | 2024-11-28 04:25:00 | NOAA-20 | PACAJÁ | PARÁ | Brasil | 1505486 | 15 | 33 | nan | nan | nan | Amazônia | 2.0 |
| be23df02-e352-3506-b8b2-1d51087f8f01 | -4.0132 | -46.44572 | 2024-11-28 04:25:00 | NOAA-20 | BOM JARDIM | MARANHÃO | Brasil | 2102002 | 21 | 33 | nan | nan | nan | Amazônia | 0.8 |
| 64b06a85-1cdb-36eb-8c43-1939dee83a6e | -2.69509 | -48.59498 | 2024-11-28 04:25:00 | NOAA-20 | TAILÂNDIA | PARÁ | Brasil | 1507953 | 15 | 33 | nan | nan | nan | Amazônia | 1.5 |
| 0f510859-f525-3d2e-81e3-931c92ffb73d | -2.8559 | -46.86493 | 2024-11-28 04:25:00 | NOAA-20 | PARAGOMINAS | PARÁ | Brasil | 1505502 | 15 | 33 | nan | nan | nan | Amazônia | 0.8 |
| 5ab2a49b-a486-30e4-b75c-c9064b97551f | -3.31821 | -53.70266 | 2024-11-28 04:25:00 | NOAA-20 | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | 0.9 |
| d8124622-d9aa-3795-95ac-87f3bf468000 | -3.84446 | -46.65207 | 2024-11-28 04:25:00 | NOAA-20 | BOM JARDIM | MARANHÃO | Brasil | 2102002 | 21 | 33 | nan | nan | nan | Amazônia | 2.2 |
| f63e6b00-8d02-3189-9350-a339bba72f3f | -3.25455 | -48.88894 | 2024-11-28 04:25:00 | NOAA-20 | TAILÂNDIA | PARÁ | Brasil | 1507953 | 15 | 33 | nan | nan | nan | Amazônia | 1.7 |
| 87d9e87c-a41c-3bea-b4d5-2daf3dbe9d9b | -3.10394 | -53.82208 | 2024-11-28 04:25:00 | NOAA-20 | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | 9.1 |
| 7d88b757-59b6-37fc-b76a-ff32f30dc972 | -3.27268 | -50.62176 | 2024-11-28 04:25:00 | NOAA-20 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 1.3 |
| 360f8312-a431-372d-95b3-c7ffac9c8079 | -4.08467 | -46.14422 | 2024-11-28 04:25:00 | NOAA-20 | ALTO ALEGRE DO PINDARÉ | MARANHÃO | Brasil | 2100477 | 21 | 33 | nan | nan | nan | Amazônia | 2.2 |
| e5aa7027-af2b-3338-964b-00a9896d5cd1 | -3.24073 | -50.14513 | 2024-11-28 04:25:00 | NOAA-20 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 1.3 |
| 063dc824-c160-3205-9b2a-e0627a3fb69c | -2.7245 | -48.89925 | 2024-11-28 04:25:00 | NOAA-20 | TAILÂNDIA | PARÁ | Brasil | 1507953 | 15 | 33 | nan | nan | nan | Amazônia | 5.0 |
| 00149837-73ab-3418-98ac-057da52f41f5 | -3.23783 | -54.22587 | 2024-11-28 04:25:00 | NOAA-20 | SANTARÉM | PARÁ | Brasil | 1506807 | 15 | 33 | nan | nan | nan | Amazônia | 0.8 |
| 843a51b5-c554-30a8-94c0-04c0908032c0 | -3.94178 | -46.89526 | 2024-11-28 04:25:00 | NOAA-20 | CENTRO NOVO DO MARANHÃO | MARANHÃO | Brasil | 2103174 | 21 | 33 | nan | nan | nan | Amazônia | 0.8 |
| 8ffe3841-a521-3678-bf34-cfe59f37b804 | -3.9427 | -48.15772 | 2024-11-28 04:25:00 | NOAA-20 | DOM ELISEU | PARÁ | Brasil | 1502939 | 15 | 33 | nan | nan | nan | Amazônia | 1.6 |
| aaeb6d05-3703-3da4-84af-8f42f619d083 | -3.1009 | -50.367 | 2024-11-28 04:25:00 | NOAA-20 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 2.3 |
| 8db342c8-c475-321d-b57d-4f6aa8a8d1f9 | -4.18355 | -40.55904 | 2024-11-28 04:25:00 | NOAA-20 | VARJOTA | CEARÁ | Brasil | 2313955 | 23 | 33 | nan | nan | nan | Caatinga | 1.5 |
| d301ec57-defa-3dde-8448-d1fb323d9168 | -3.97321 | -46.74075 | 2024-11-28 04:25:00 | NOAA-20 | BOM JARDIM | MARANHÃO | Brasil | 2102002 | 21 | 33 | nan | nan | nan | Amazônia | 2.7 |
| b69ba503-08ce-3998-9253-d14c6d474f67 | -3.85547 | -50.14522 | 2024-11-28 04:25:00 | NOAA-20 | PACAJÁ | PARÁ | Brasil | 1505486 | 15 | 33 | nan | nan | nan | Amazônia | 0.9 |
| 9b1da464-2e23-3f76-8265-979beb770cff | -3.08738 | -49.21292 | 2024-11-28 04:25:00 | NOAA-20 | MOJU | PARÁ | Brasil | 1504703 | 15 | 33 | nan | nan | nan | Amazônia | 3.1 |
| b8f26802-fb6e-3dd6-bd9c-06f4c1e5cb22 | -3.23315 | -54.22189 | 2024-11-28 04:25:00 | NOAA-20 | SANTARÉM | PARÁ | Brasil | 1506807 | 15 | 33 | nan | nan | nan | Amazônia | 1.0 |
| 5b2010c6-4819-3445-9db0-de679c5ba801 | -2.8419 | -46.84434 | 2024-11-28 04:25:00 | NOAA-20 | PARAGOMINAS | PARÁ | Brasil | 1505502 | 15 | 33 | nan | nan | nan | Amazônia | 2.9 |
| 7d0bd2ab-dba7-394e-afdf-7190dabb9243 | -2.82801 | -46.81303 | 2024-11-28 04:25:00 | NOAA-20 | PARAGOMINAS | PARÁ | Brasil | 1505502 | 15 | 33 | nan | nan | nan | Amazônia | 4.5 |
| 9087dc47-a481-3588-b82d-0a1f27e38ebe | -3.44555 | -49.23513 | 2024-11-28 04:25:00 | NOAA-20 | BREU BRANCO | PARÁ | Brasil | 1501782 | 15 | 33 | nan | nan | nan | Amazônia | 0.8 |
| 3aa4bbf3-d6da-31bf-b483-75b09efae698 | -4.45342 | -49.73793 | 2024-11-28 04:25:00 | NOAA-20 | NOVO REPARTIMENTO | PARÁ | Brasil | 1505064 | 15 | 33 | nan | nan | nan | Amazônia | 1.4 |
| e7d0aa82-6d83-3c3c-b768-4104d9771eb7 | -2.85989 | -46.83981 | 2024-11-28 04:25:00 | NOAA-20 | PARAGOMINAS | PARÁ | Brasil | 1505502 | 15 | 33 | nan | nan | nan | Amazônia | 2.5 |
| 46763a42-b12c-3841-95f5-931ecf9aa2b4 | -2.36509 | -50.43267 | 2024-11-28 04:25:00 | NOAA-20 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 1.0 |
| d12a22d2-1873-3b9d-88de-525e47659965 | -4.13475 | -46.36536 | 2024-11-28 04:25:00 | NOAA-20 | BURITICUPU | MARANHÃO | Brasil | 2102325 | 21 | 33 | nan | nan | nan | Amazônia | 1.2 |
| c9aebc33-30af-34ae-a2cb-0dc0c493eaa0 | -3.10267 | -53.82204 | 2024-11-28 04:25:00 | NOAA-20 | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | 12.9 |
| f2eec78d-8864-33eb-8468-002a243ea927 | -2.95356 | -48.33862 | 2024-11-28 04:25:00 | NOAA-20 | TOMÉ-AÇU | PARÁ | Brasil | 1508001 | 15 | 33 | nan | nan | nan | Amazônia | 4.3 |
| cdeb1e15-445f-369d-945f-9234e9cfee42 | -2.83631 | -46.83613 | 2024-11-28 04:25:00 | NOAA-20 | PARAGOMINAS | PARÁ | Brasil | 1505502 | 15 | 33 | nan | nan | nan | Amazônia | 1.6 |
| 495f9965-9ce6-302a-8c56-96b7bf8ba84b | -3.96356 | -46.90965 | 2024-11-28 04:25:00 | NOAA-20 | CENTRO NOVO DO MARANHÃO | MARANHÃO | Brasil | 2103174 | 21 | 33 | nan | nan | nan | Amazônia | 2.0 |
| 68530688-86a7-3a02-990e-7d6cefb7a104 | -2.83508 | -54.12035 | 2024-11-28 04:25:00 | NOAA-20 | SANTARÉM | PARÁ | Brasil | 1506807 | 15 | 33 | nan | nan | nan | Amazônia | 5.9 |
| 75e0a0b0-26b3-3cb2-9a08-b25e950674f7 | -4.44077 | -46.34201 | 2024-11-28 04:25:00 | NOAA-20 | BURITICUPU | MARANHÃO | Brasil | 2102325 | 21 | 33 | nan | nan | nan | Amazônia | 1.9 |
| 07b8b723-d397-3886-9902-c03955bcb81a | -5.03334 | -43.59184 | 2024-11-28 04:25:00 | NOAA-20 | SÃO JOÃO DO SOTER | MARANHÃO | Brasil | 2111078 | 21 | 33 | nan | nan | nan | Cerrado | 1.0 |
| 29a82da9-c129-3132-81fa-e783f2531f4d | -6.01208 | -38.66228 | 2024-11-28 04:25:00 | NOAA-20 | JAGUARIBE | CEARÁ | Brasil | 2306900 | 23 | 33 | nan | nan | nan | Caatinga | 5.3 |
| f7805b9d-f0b5-320f-8672-fc180bd80258 | -3.25122 | -50.62571 | 2024-11-28 04:25:00 | NOAA-20 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 1.2 |
| 3a1af0f2-ab54-3a43-b7a0-0544c3e347a3 | -3.99253 | -50.55806 | 2024-11-28 04:25:00 | NOAA-20 | NOVO REPARTIMENTO | PARÁ | Brasil | 1505064 | 15 | 33 | nan | nan | nan | Amazônia | 0.7 |
| 032e72f5-480c-30b3-982f-6c6c64eb0967 | -4.01327 | -46.53133 | 2024-11-28 04:25:00 | NOAA-20 | BOM JARDIM | MARANHÃO | Brasil | 2102002 | 21 | 33 | nan | nan | nan | Amazônia | 1.3 |
| 5544c194-6b67-3db8-b557-9640bc5b9e80 | -3.91409 | -47.19942 | 2024-11-28 04:25:00 | NOAA-20 | ULIANÓPOLIS | PARÁ | Brasil | 1508126 | 15 | 33 | nan | nan | nan | Amazônia | 6.8 |
| 0bdacf39-5efb-3d44-a8a6-3012a079ff53 | -2.8445 | -54.07212 | 2024-11-28 04:25:00 | NOAA-20 | PRAINHA | PARÁ | Brasil | 1506005 | 15 | 33 | nan | nan | nan | Amazônia | 2.0 |
| 60201e54-8001-398f-b48a-8b01d24a5788 | -4.77442 | -44.42833 | 2024-11-28 04:25:00 | NOAA-20 | SANTO ANTÔNIO DOS LOPES | MARANHÃO | Brasil | 2110302 | 21 | 33 | nan | nan | nan | Cerrado | 3.1 |
| 312dc86a-9607-3fe1-a78e-d4cb6019fdfc | -3.04383 | -47.8872 | 2024-11-28 04:25:00 | NOAA-20 | PARAGOMINAS | PARÁ | Brasil | 1505502 | 15 | 33 | nan | nan | nan | Amazônia | 0.8 |
| 62946be6-7fdb-30a0-8524-989963cf188a | -4.05659 | -46.68562 | 2024-11-28 04:25:00 | NOAA-20 | BOM JARDIM | MARANHÃO | Brasil | 2102002 | 21 | 33 | nan | nan | nan | Amazônia | 2.1 |
| 93fd9dfc-b39e-37e7-afc6-d2c440bb3e39 | -1.91808 | -54.43944 | 2024-11-28 04:25:00 | NOAA-20 | MONTE ALEGRE | PARÁ | Brasil | 1504802 | 15 | 33 | nan | nan | nan | Amazônia | 1.5 |
| 41d09384-b930-3bda-b5cd-f46c9f3e40ee | -3.10519 | -53.25755 | 2024-11-28 04:25:00 | NOAA-20 | MEDICILÂNDIA | PARÁ | Brasil | 1504455 | 15 | 33 | nan | nan | nan | Amazônia | 2.4 |
| 27272219-bd7a-3866-a946-c17ba9d375ff | -3.5261 | -50.75494 | 2024-11-28 04:25:00 | NOAA-20 | PACAJÁ | PARÁ | Brasil | 1505486 | 15 | 33 | nan | nan | nan | Amazônia | 1.4 |
| bcdb5705-9801-3ca9-ac2c-89c4d7a41f2e | -3.06025 | -51.29517 | 2024-11-28 04:25:00 | NOAA-20 | ANAPU | PARÁ | Brasil | 1500859 | 15 | 33 | nan | nan | nan | Amazônia | 1.2 |
| 2b87afab-c224-31fd-b641-4b4eccbf4fe3 | -4.04298 | -46.85693 | 2024-11-28 04:25:00 | NOAA-20 | BOM JARDIM | MARANHÃO | Brasil | 2102002 | 21 | 33 | nan | nan | nan | Amazônia | 0.8 |
| 2b4009e9-ca20-374d-88f0-df33c2c1a29e | -3.07451 | -50.96718 | 2024-11-28 04:25:00 | NOAA-20 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 3.1 |
| 229d92e4-fdf8-3b0e-8f50-67f1db5dc7fe | -2.80778 | -46.83189 | 2024-11-28 04:25:00 | NOAA-20 | PARAGOMINAS | PARÁ | Brasil | 1505502 | 15 | 33 | nan | nan | nan | Amazônia | 8.2 |
| 80b2d4d5-a78a-3f92-ac7e-f1c0d100fb54 | -3.09402 | -50.35876 | 2024-11-28 04:25:00 | NOAA-20 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 1.9 |
| ca02669b-13d0-3aa9-ad8e-0822fbe62e3f | -3.71389 | -47.13469 | 2024-11-28 04:25:00 | NOAA-20 | ULIANÓPOLIS | PARÁ | Brasil | 1508126 | 15 | 33 | nan | nan | nan | Amazônia | 1.6 |
| 72c217d0-eb00-3131-8811-65c520147968 | -3.76274 | -49.90388 | 2024-11-28 04:25:00 | NOAA-20 | TUCURUÍ | PARÁ | Brasil | 1508100 | 15 | 33 | nan | nan | nan | Amazônia | 1.2 |
| 30c326cc-65e7-366b-85cc-734e2c3bd29b | -2.6492 | -48.50325 | 2024-11-28 04:25:00 | NOAA-20 | TAILÂNDIA | PARÁ | Brasil | 1507953 | 15 | 33 | nan | nan | nan | Amazônia | 1.2 |
| 2639ae03-b67e-30c0-92b3-93ec2c5c51da | -3.81007 | -46.61396 | 2024-11-28 04:25:00 | NOAA-20 | BOM JARDIM | MARANHÃO | Brasil | 2102002 | 21 | 33 | nan | nan | nan | Amazônia | 2.6 |
| 560ca61c-f95f-303a-878f-8331f8c24bc3 | -3.84146 | -51.71009 | 2024-11-28 04:25:00 | NOAA-20 | SENADOR JOSÉ PORFÍRIO | PARÁ | Brasil | 1507805 | 15 | 33 | nan | nan | nan | Amazônia | 1.6 |
| 982f3642-e4ed-35bc-9ee0-8427d74ceca1 | -3.0123 | -51.70503 | 2024-11-28 04:25:00 | NOAA-20 | SENADOR JOSÉ PORFÍRIO | PARÁ | Brasil | 1507805 | 15 | 33 | nan | nan | nan | Amazônia | 1.0 |
| ddf0bd5c-48eb-34fe-ba45-fb4bbb80119b | -5.07401 | -46.82773 | 2024-11-28 04:25:00 | NOAA-20 | AMARANTE DO MARANHÃO | MARANHÃO | Brasil | 2100600 | 21 | 33 | nan | nan | nan | Amazônia | 0.8 |
| fc6963f7-8e09-3049-af48-aee6f025bfaf | -3.49711 | -44.60907 | 2024-11-28 04:25:00 | NOAA-20 | MIRANDA DO NORTE | MARANHÃO | Brasil | 2106755 | 21 | 33 | nan | nan | nan | Amazônia | 0.9 |
| 12a07e3d-7d2c-3458-b43a-891eed3ff600 | -3.10032 | -53.81237 | 2024-11-28 04:25:00 | NOAA-20 | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | 4.9 |
| 670f8cd1-f1ae-368e-a202-5a834dab1304 | -4.35177 | -48.56377 | 2024-11-28 04:25:00 | NOAA-20 | RONDON DO PARÁ | PARÁ | Brasil | 1506187 | 15 | 33 | nan | nan | nan | Amazônia | 1.2 |
| 5f5d332f-cb40-366f-931f-a913baab9739 | -2.98522 | -49.14803 | 2024-11-28 04:25:00 | NOAA-20 | MOJU | PARÁ | Brasil | 1504703 | 15 | 33 | nan | nan | nan | Amazônia | 0.9 |
| 910d3846-b767-3c1a-997e-c51c96f8a25a | -2.84241 | -46.86282 | 2024-11-28 04:25:00 | NOAA-20 | PARAGOMINAS | PARÁ | Brasil | 1505502 | 15 | 33 | nan | nan | nan | Amazônia | 3.3 |
| 9f052203-6f28-3daf-8342-1ef7aecbda09 | -2.82842 | -46.84224 | 2024-11-28 04:25:00 | NOAA-20 | PARAGOMINAS | PARÁ | Brasil | 1505502 | 15 | 33 | nan | nan | nan | Amazônia | 1.2 |
| 3f046947-887f-3bdb-8d69-c5c39abfe965 | -4.00185 | -44.28531 | 2024-11-28 04:25:00 | NOAA-20 | COROATÁ | MARANHÃO | Brasil | 2103604 | 21 | 33 | nan | nan | nan | Cerrado | 0.9 |
| 68c6be25-6dfa-35b8-a934-5b64b13c843e | -3.10201 | -50.36007 | 2024-11-28 04:25:00 | NOAA-20 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 1.8 |


[Clique aqui para ver as próximas entradas](README66.md)
