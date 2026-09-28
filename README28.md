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

## Dados Diários - Página 28

| ID | Latitude | Longitude | Data/Hora GMT | Satélite | Município | Estado | País | Município ID | Estado ID | País ID | Dias sem Chuva | Precipitação | Risco de Fogo | Bioma | FRP |
|----|----------|-----------|---------------|----------|-----------|--------|------|--------------|-----------|---------|----------------|--------------|----------------|-------|-----|
| d9127e38-3f1b-3797-92df-9894cfbd6afc | -3.82741 | -44.09657 | 2026-09-28 04:32:00 | NOAA-21 | PIRAPEMAS | MARANHÃO | Brasil | 2108801 | 21 | 33 | nan | nan | nan | Cerrado | 2.5 |
| ecf37142-a429-30d9-b70c-f16f01458e6d | -3.69804 | -51.36985 | 2026-09-28 04:32:00 | NOAA-21 | ANAPU | PARÁ | Brasil | 1500859 | 15 | 33 | nan | nan | nan | Amazônia | 2.5 |
| bf1a9b00-fe8b-30f0-9540-056dc44164fe | 1.66622 | -55.92559 | 2026-09-28 04:32:00 | NOAA-21 | ORIXIMINÁ | PARÁ | Brasil | 1505304 | 15 | 33 | nan | nan | nan | Amazônia | 1.8 |
| 6fecf158-ba58-3e31-a5d1-6d08b6702b65 | -3.984 | -44.51701 | 2026-09-28 04:32:00 | NOAA-21 | SÃO MATEUS DO MARANHÃO | MARANHÃO | Brasil | 2111508 | 21 | 33 | nan | nan | nan | Cerrado | 2.3 |
| 092b411b-59d2-32ab-972e-d9c1ae2f2650 | -5.49974 | -45.51271 | 2026-09-28 04:32:00 | NOAA-21 | JENIPAPO DOS VIEIRAS | MARANHÃO | Brasil | 2105476 | 21 | 33 | nan | nan | nan | Cerrado | 1.4 |
| 2bd07550-437b-3bb9-b129-cda450727bc1 | -1.75236 | -55.65284 | 2026-09-28 04:32:00 | NOAA-21 | ÓBIDOS | PARÁ | Brasil | 1505106 | 15 | 33 | nan | nan | nan | Amazônia | 1.3 |
| b59ab943-38fe-39a5-abdb-fb4881de8e7d | -2.76893 | -49.48083 | 2026-09-28 04:32:00 | NOAA-21 | BAIÃO | PARÁ | Brasil | 1501204 | 15 | 33 | nan | nan | nan | Amazônia | 12.7 |
| 9864a99e-bbe0-345b-867e-e8dab00f93ef | -3.97424 | -48.00312 | 2026-09-28 04:32:00 | NOAA-21 | DOM ELISEU | PARÁ | Brasil | 1502939 | 15 | 33 | nan | nan | nan | Amazônia | 0.8 |
| dba1b47e-4478-3521-a555-44e36479e0c7 | 0.69964 | -51.43515 | 2026-09-28 04:32:00 | NOAA-21 | PORTO GRANDE | AMAPÁ | Brasil | 1600535 | 16 | 33 | nan | nan | nan | Amazônia | 1.7 |
| 891b8cc3-3e5f-3dc6-bd50-36ec957f24bf | -4.79677 | -49.1133 | 2026-09-28 04:32:00 | NOAA-21 | JACUNDÁ | PARÁ | Brasil | 1503804 | 15 | 33 | nan | nan | nan | Amazônia | 2.3 |
| f9788849-083e-37c5-a5dd-de43e9b5a14a | -3.94142 | -42.55249 | 2026-09-28 04:32:00 | NOAA-21 | CAMPO LARGO DO PIAUÍ | PIAUÍ | Brasil | 2202174 | 22 | 33 | nan | nan | nan | Caatinga | 10.1 |
| e57ddbc1-3213-384e-8dac-c6a869b6e6b3 | -4.79284 | -49.11636 | 2026-09-28 04:32:00 | NOAA-21 | JACUNDÁ | PARÁ | Brasil | 1503804 | 15 | 33 | nan | nan | nan | Amazônia | 2.3 |
| db0a16a5-0f75-3e43-bbf6-d8213a10f929 | -6.24961 | -41.59985 | 2026-09-28 04:32:00 | NOAA-21 | PIMENTEIRAS | PIAUÍ | Brasil | 2208106 | 22 | 33 | nan | nan | nan | Caatinga | 2.3 |
| 0dfe40be-a4c9-397c-b6ee-d3dc4aa2a38e | -1.86172 | -47.97735 | 2026-09-28 04:32:00 | NOAA-21 | CONCÓRDIA DO PARÁ | PARÁ | Brasil | 1502756 | 15 | 33 | nan | nan | nan | Amazônia | 3.3 |
| 8f9406fe-3878-3e31-affa-bbd6bf2068e5 | -4.31754 | -50.39993 | 2026-09-28 04:32:00 | NOAA-21 | NOVO REPARTIMENTO | PARÁ | Brasil | 1505064 | 15 | 33 | nan | nan | nan | Amazônia | 10.4 |
| 49981fa9-faeb-3caf-a77f-58b5aa4f9be0 | -3.94091 | -42.55594 | 2026-09-28 04:32:00 | NOAA-21 | CAMPO LARGO DO PIAUÍ | PIAUÍ | Brasil | 2202174 | 22 | 33 | nan | nan | nan | Caatinga | 10.1 |
| fa50e6b7-90ae-3942-84c9-7cb6d8ae583e | -2.29691 | -48.75729 | 2026-09-28 04:32:00 | NOAA-21 | MOJU | PARÁ | Brasil | 1504703 | 15 | 33 | nan | nan | nan | Amazônia | 1.4 |
| 4bef3b7f-e400-32ac-9c38-d969ab89b136 | -0.76968 | -48.52589 | 2026-09-28 04:32:00 | NOAA-21 | SALVATERRA | PARÁ | Brasil | 1506302 | 15 | 33 | nan | nan | nan | Amazônia | 0.6 |
| f3bde2eb-6ac4-35b9-be97-4721f8cd578d | -2.77525 | -49.48568 | 2026-09-28 04:32:00 | NOAA-21 | BAIÃO | PARÁ | Brasil | 1501204 | 15 | 33 | nan | nan | nan | Amazônia | 4.2 |
| f6bd73bf-dc54-34cd-bfcf-82591aa93a6d | -3.26647 | -50.14416 | 2026-09-28 04:32:00 | NOAA-21 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 1.5 |
| 42bb9e60-ae12-3d56-9d7b-498800772dd1 | 1.67324 | -55.93622 | 2026-09-28 04:32:00 | NOAA-21 | ORIXIMINÁ | PARÁ | Brasil | 1505304 | 15 | 33 | nan | nan | nan | Amazônia | 3.2 |
| ef77ab91-ecd1-3051-8f12-3f0d2ccffe31 | -3.42152 | -50.41944 | 2026-09-28 04:32:00 | NOAA-21 | PACAJÁ | PARÁ | Brasil | 1505486 | 15 | 33 | nan | nan | nan | Amazônia | 1.8 |
| 8de42503-eacf-3b53-a4be-bce7569887f3 | -3.03311 | -51.47281 | 2026-09-28 04:32:00 | NOAA-21 | ANAPU | PARÁ | Brasil | 1500859 | 15 | 33 | nan | nan | nan | Amazônia | 2.5 |
| 5451716d-24d1-3915-b9d2-52e9774aaf5f | -3.15406 | -54.09774 | 2026-09-28 04:32:00 | NOAA-21 | SANTARÉM | PARÁ | Brasil | 1506807 | 15 | 33 | nan | nan | nan | Amazônia | 1.5 |
| c8d1d8ec-b329-377d-b38b-73629c343b5b | -2.7712 | -49.48894 | 2026-09-28 04:32:00 | NOAA-21 | BAIÃO | PARÁ | Brasil | 1501204 | 15 | 33 | nan | nan | nan | Amazônia | 3.5 |
| 5bd96e4c-96e3-3bec-8dce-22d17ed3d63c | -3.42088 | -50.43235 | 2026-09-28 04:32:00 | NOAA-21 | PACAJÁ | PARÁ | Brasil | 1505486 | 15 | 33 | nan | nan | nan | Amazônia | 3.2 |
| 449edf73-1781-308e-9dcc-55800db76e34 | -3.15242 | -54.09847 | 2026-09-28 04:32:00 | NOAA-21 | SANTARÉM | PARÁ | Brasil | 1506807 | 15 | 33 | nan | nan | nan | Amazônia | 2.2 |
| c18fcd86-c9a3-34c7-b0ca-d274fcf0cf82 | -2.37951 | -50.40693 | 2026-09-28 04:32:00 | NOAA-21 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 1.4 |
| b3112625-51dc-377e-a0d2-2c7283e86389 | -3.8651 | -49.21189 | 2026-09-28 04:32:00 | NOAA-21 | BREU BRANCO | PARÁ | Brasil | 1501782 | 15 | 33 | nan | nan | nan | Amazônia | 0.6 |
| 7a5e12f3-41de-3f1e-b868-d25b04376443 | -4.78948 | -49.11583 | 2026-09-28 04:32:00 | NOAA-21 | JACUNDÁ | PARÁ | Brasil | 1503804 | 15 | 33 | nan | nan | nan | Amazônia | 1.0 |
| 9fa7b385-0690-36ce-b2eb-3b28ad1d8aea | -3.29285 | -50.32142 | 2026-09-28 04:32:00 | NOAA-21 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 0.8 |
| 26e652c9-a6a2-3198-a81a-58cbe3891ee8 | 0.6991 | -51.43167 | 2026-09-28 04:32:00 | NOAA-21 | PORTO GRANDE | AMAPÁ | Brasil | 1600535 | 16 | 33 | nan | nan | nan | Amazônia | 1.9 |
| 8ee3e7c7-54a4-3518-89be-0da4b62fe59a | 0.46858 | -50.97704 | 2026-09-28 04:32:00 | NOAA-21 | MACAPÁ | AMAPÁ | Brasil | 1600303 | 16 | 33 | nan | nan | nan | Amazônia | 2.4 |
| 74dc15cd-4c10-3941-9aa0-2ce2e3b8edd7 | 1.67234 | -55.92846 | 2026-09-28 04:32:00 | NOAA-21 | ORIXIMINÁ | PARÁ | Brasil | 1505304 | 15 | 33 | nan | nan | nan | Amazônia | 1.8 |
| 74fb352a-3716-3ca4-8b50-3acb0915304b | -2.99989 | -50.47101 | 2026-09-28 04:32:00 | NOAA-21 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 2.0 |
| ee7975d0-760d-3d3a-9ef6-ae86a73de85a | 1.26724 | -50.6894 | 2026-09-28 04:32:00 | NOAA-21 | TARTARUGALZINHO | AMAPÁ | Brasil | 1600709 | 16 | 33 | nan | nan | nan | Amazônia | 1.5 |
| 6bbccc07-d432-3d75-a5ad-9c8d3718f2bd | -5.1301 | -45.75549 | 2026-09-28 04:32:00 | NOAA-21 | ITAIPAVA DO GRAJAÚ | MARANHÃO | Brasil | 2105351 | 21 | 33 | nan | nan | nan | Cerrado | 2.1 |
| c20b7415-9404-324b-94f6-fe5246f353c8 | -1.77549 | -53.76418 | 2026-09-28 04:32:00 | NOAA-21 | PRAINHA | PARÁ | Brasil | 1506005 | 15 | 33 | nan | nan | nan | Amazônia | 4.2 |
| 63fd280b-88dd-3019-a616-12840d3bed8c | 1.67292 | -55.93214 | 2026-09-28 04:32:00 | NOAA-21 | ORIXIMINÁ | PARÁ | Brasil | 1505304 | 15 | 33 | nan | nan | nan | Amazônia | 2.3 |
| 2c6d0ae6-bc79-3253-b562-9fee105ddb70 | -2.73963 | -49.46461 | 2026-09-28 04:32:00 | NOAA-21 | MOJU | PARÁ | Brasil | 1504703 | 15 | 33 | nan | nan | nan | Amazônia | 2.1 |
| 4fd13984-ced3-37f7-b63d-d4814ba3c43e | -1.79204 | -47.94507 | 2026-09-28 04:32:00 | NOAA-21 | CONCÓRDIA DO PARÁ | PARÁ | Brasil | 1502756 | 15 | 33 | nan | nan | nan | Amazônia | 2.6 |
| 45dbe671-35de-3169-a8cc-9f8d5aae8c0a | -3.01301 | -54.20665 | 2026-09-28 04:32:00 | NOAA-21 | SANTARÉM | PARÁ | Brasil | 1506807 | 15 | 33 | nan | nan | nan | Amazônia | 1.4 |
| 57b14e84-6e82-3456-8631-cc7c40c0bac7 | -4.03869 | -54.21614 | 2026-09-28 04:32:00 | NOAA-21 | PLACAS | PARÁ | Brasil | 1505650 | 15 | 33 | nan | nan | nan | Amazônia | 0.9 |
| b554a005-5904-3c3e-9fa7-c537678e558f | -3.67719 | -45.371 | 2026-09-28 04:32:00 | NOAA-21 | SANTA INÊS | MARANHÃO | Brasil | 2109908 | 21 | 33 | nan | nan | nan | Amazônia | 2.8 |
| 95561a64-25c8-3a00-9957-9232f94426a2 | -2.66317 | -51.73434 | 2026-09-28 04:32:00 | NOAA-21 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 5.4 |
| 4c6d4448-f91c-3bf2-b882-44d0949d0445 | -3.09915 | -50.19324 | 2026-09-28 04:32:00 | NOAA-21 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 1.6 |
| 10518cc6-88e0-37f1-8205-fb03aa48e3a0 | 1.1558 | -51.16536 | 2026-09-28 04:32:00 | NOAA-21 | TARTARUGALZINHO | AMAPÁ | Brasil | 1600709 | 16 | 33 | nan | nan | nan | Amazônia | 1.6 |
| 5c421ee1-3ed4-3434-978f-564306f16a2b | -2.66117 | -56.44958 | 2026-09-28 04:32:00 | NOAA-21 | JURUTI | PARÁ | Brasil | 1503903 | 15 | 33 | nan | nan | nan | Amazônia | 1.6 |
| 81c8ccc0-ba48-34d0-881e-a2a101036c8b | -1.77476 | -53.76874 | 2026-09-28 04:32:00 | NOAA-21 | PRAINHA | PARÁ | Brasil | 1506005 | 15 | 33 | nan | nan | nan | Amazônia | 4.2 |
| 1df8a4eb-84d4-3058-a41c-13f3464ded95 | -1.94986 | -49.43841 | 2026-09-28 04:32:00 | NOAA-21 | LIMOEIRO DO AJURU | PARÁ | Brasil | 1504000 | 15 | 33 | nan | nan | nan | Amazônia | 2.2 |
| 86c93944-f9fd-33b7-a25c-054250a97be4 | -3.20187 | -51.04026 | 2026-09-28 04:32:00 | NOAA-21 | PACAJÁ | PARÁ | Brasil | 1505486 | 15 | 33 | nan | nan | nan | Amazônia | 4.8 |
| cc525ba3-e79c-37bc-a129-8c7f1ecb3604 | 1.67434 | -55.94357 | 2026-09-28 04:32:00 | NOAA-21 | ORIXIMINÁ | PARÁ | Brasil | 1505304 | 15 | 33 | nan | nan | nan | Amazônia | 4.4 |
| 5438cba6-1b76-3caf-949d-1cfd753c03d6 | -0.50727 | -49.12745 | 2026-09-28 04:32:00 | NOAA-21 | CACHOEIRA DO ARARI | PARÁ | Brasil | 1502004 | 15 | 33 | nan | nan | nan | Amazônia | 3.2 |
| 239d2113-744c-3b64-b554-d749d179becb | -2.65847 | -51.73864 | 2026-09-28 04:32:00 | NOAA-21 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 2.0 |
| f7c420b0-f4a9-3ba1-b54a-e482b5c2eeaa | -1.85894 | -47.97335 | 2026-09-28 04:32:00 | NOAA-21 | CONCÓRDIA DO PARÁ | PARÁ | Brasil | 1502756 | 15 | 33 | nan | nan | nan | Amazônia | 0.7 |
| e55e04bb-e944-3306-9c1f-c09cfecf5cd7 | -2.66189 | -51.73691 | 2026-09-28 04:32:00 | NOAA-21 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 5.4 |
| 961ba706-c77b-3873-b88a-b8525edb2ff9 | -1.75565 | -55.12559 | 2026-09-28 04:32:00 | NOAA-21 | CURUÁ | PARÁ | Brasil | 1502855 | 15 | 33 | nan | nan | nan | Amazônia | 1.4 |
| 02e7adfa-ff8b-35a3-aaaa-7f0275806446 | -0.50032 | -49.12638 | 2026-09-28 04:32:00 | NOAA-21 | CACHOEIRA DO ARARI | PARÁ | Brasil | 1502004 | 15 | 33 | nan | nan | nan | Amazônia | 1.3 |
| 23fa372e-f290-37d1-b122-9ea9e695e1bd | -3.29349 | -50.31736 | 2026-09-28 04:32:00 | NOAA-21 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 1.0 |
| b87e3643-f3b2-38d3-9002-c1e20e50bbb7 | -3.6973 | -51.3744 | 2026-09-28 04:32:00 | NOAA-21 | ANAPU | PARÁ | Brasil | 1500859 | 15 | 33 | nan | nan | nan | Amazônia | 2.5 |
| 9bb503dd-b95a-3b0d-af27-555cfbf1b46e | -4.05933 | -47.50222 | 2026-09-28 04:32:00 | NOAA-21 | ULIANÓPOLIS | PARÁ | Brasil | 1508126 | 15 | 33 | nan | nan | nan | Amazônia | 2.8 |
| f2ff6e64-4440-34c5-b975-2b819be21511 | 1.65121 | -55.90218 | 2026-09-28 04:32:00 | NOAA-21 | ORIXIMINÁ | PARÁ | Brasil | 1505304 | 15 | 33 | nan | nan | nan | Amazônia | 1.7 |
| ec84f66b-24e2-3cf6-818d-343b8b012593 | -3.4219 | -48.33568 | 2026-09-28 04:32:00 | NOAA-21 | PARAGOMINAS | PARÁ | Brasil | 1505502 | 15 | 33 | nan | nan | nan | Amazônia | 48.3 |
| 94edcd2f-faf2-3f39-83c8-c03be6064fd0 | -3.29413 | -50.31328 | 2026-09-28 04:32:00 | NOAA-21 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 1.0 |
| 267c3324-dd55-33dc-96e4-a76630205695 | -0.53247 | -49.19432 | 2026-09-28 04:32:00 | NOAA-21 | CACHOEIRA DO ARARI | PARÁ | Brasil | 1502004 | 15 | 33 | nan | nan | nan | Amazônia | 2.7 |
| 48b3454e-98aa-3aa5-b60a-59bfc9261cd4 | -3.01583 | -51.53302 | 2026-09-28 04:32:00 | NOAA-21 | ANAPU | PARÁ | Brasil | 1500859 | 15 | 33 | nan | nan | nan | Amazônia | 2.2 |
| 2a073e89-b546-39ef-9208-a1926ab8c0c6 | -2.89689 | -54.08077 | 2026-09-28 04:32:00 | NOAA-21 | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | 0.5 |
| 872ac6d6-e065-3304-90d0-95a05de71dfe | -3.20882 | -51.03506 | 2026-09-28 04:32:00 | NOAA-21 | PACAJÁ | PARÁ | Brasil | 1505486 | 15 | 33 | nan | nan | nan | Amazônia | 16.1 |
| c90159bb-10ae-390d-943c-b9bd2f7da550 | -5.13085 | -50.71186 | 2026-09-28 04:32:00 | NOAA-21 | NOVO REPARTIMENTO | PARÁ | Brasil | 1505064 | 15 | 33 | nan | nan | nan | Amazônia | 2.1 |
| 33836419-4c24-3738-9fa3-358f745953fb | -5.46511 | -47.47632 | 2026-09-28 04:32:00 | NOAA-21 | IMPERATRIZ | MARANHÃO | Brasil | 2105302 | 21 | 33 | nan | nan | nan | Cerrado | 1.2 |
| 316e1cc2-4686-3d5b-823d-801b20eeac10 | -3.98042 | -44.51648 | 2026-09-28 04:32:00 | NOAA-21 | SÃO MATEUS DO MARANHÃO | MARANHÃO | Brasil | 2111508 | 21 | 33 | nan | nan | nan | Cerrado | 7.7 |
| 0f682652-e4fe-35c9-a48f-ab704defe78e | -3.81648 | -44.09486 | 2026-09-28 04:32:00 | NOAA-21 | PIRAPEMAS | MARANHÃO | Brasil | 2108801 | 21 | 33 | nan | nan | nan | Cerrado | 2.9 |
| 8a20b9d4-5ae4-3fe6-ab6d-dd02beec3742 | -2.98016 | -54.14902 | 2026-09-28 04:32:00 | NOAA-21 | SANTARÉM | PARÁ | Brasil | 1506807 | 15 | 33 | nan | nan | nan | Amazônia | 2.5 |
| 5ebe1499-0f22-3f81-bfc5-6c9deaaf5681 | 1.7655 | -50.84168 | 2026-09-28 04:32:00 | NOAA-21 | PRACUÚBA | AMAPÁ | Brasil | 1600550 | 16 | 33 | nan | nan | nan | Amazônia | 1.8 |
| a095af80-2657-348c-8b68-37a43726bbc7 | -4.7934 | -49.11278 | 2026-09-28 04:32:00 | NOAA-21 | JACUNDÁ | PARÁ | Brasil | 1503804 | 15 | 33 | nan | nan | nan | Amazônia | 2.3 |
| 1684da22-a193-3674-8f14-4f806cc9b696 | -5.07529 | -46.14195 | 2026-09-28 04:32:00 | NOAA-21 | ARAME | MARANHÃO | Brasil | 2100956 | 21 | 33 | nan | nan | nan | Amazônia | 1.4 |
| 5aed5ea6-7f38-3691-883c-cf223e358cef | -3.20207 | -51.19385 | 2026-09-28 04:32:00 | NOAA-21 | PACAJÁ | PARÁ | Brasil | 1505486 | 15 | 33 | nan | nan | nan | Amazônia | 1.2 |
| 55c7c885-fe9d-3245-8a4f-ca70076c0b75 | -5.23276 | -48.18072 | 2026-09-28 04:32:00 | NOAA-21 | VILA NOVA DOS MARTÍRIOS | MARANHÃO | Brasil | 2112852 | 21 | 33 | nan | nan | nan | Amazônia | 0.9 |
| b4656d26-2f0f-3b70-956b-6715cae9a3dc | -3.07697 | -51.19913 | 2026-09-28 04:32:00 | NOAA-21 | ANAPU | PARÁ | Brasil | 1500859 | 15 | 33 | nan | nan | nan | Amazônia | 1.1 |
| 5e8af26f-570d-3630-b8a1-be4f902390db | -3.0 | -54.74947 | 2026-09-28 04:32:00 | NOAA-21 | MOJUÍ DOS CAMPOS | PARÁ | Brasil | 1504752 | 15 | 33 | nan | nan | nan | Amazônia | 1.7 |
| 166ae334-9af2-3aa0-aa5c-82b2679ececd | -3.4228 | -50.42006 | 2026-09-28 04:32:00 | NOAA-21 | PACAJÁ | PARÁ | Brasil | 1505486 | 15 | 33 | nan | nan | nan | Amazônia | 2.8 |
| 2cdc4a0a-340d-38b2-be91-122881f067aa | -3.23732 | -50.57871 | 2026-09-28 04:32:00 | NOAA-21 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 2.4 |
| f42a5c81-32ce-32e8-881f-7fceb06dc52d | -5.63636 | -43.72254 | 2026-09-28 04:32:00 | NOAA-21 | BURITI BRAVO | MARANHÃO | Brasil | 2102309 | 21 | 33 | nan | nan | nan | Cerrado | 8.0 |
| 3aed734a-c5ca-31e1-a2c8-344c1ebf7d66 | -2.76774 | -49.48841 | 2026-09-28 04:32:00 | NOAA-21 | BAIÃO | PARÁ | Brasil | 1501204 | 15 | 33 | nan | nan | nan | Amazônia | 3.5 |
| 2ae0b207-c071-366d-82ce-20af138b9127 | -2.99035 | -49.10289 | 2026-09-28 04:32:00 | NOAA-21 | MOJU | PARÁ | Brasil | 1504703 | 15 | 33 | nan | nan | nan | Amazônia | 2.0 |
| 0fa72399-7327-3297-bb49-a39971545af5 | -0.49215 | -49.13299 | 2026-09-28 04:32:00 | NOAA-21 | CACHOEIRA DO ARARI | PARÁ | Brasil | 1502004 | 15 | 33 | nan | nan | nan | Amazônia | 0.5 |
| 7aa9fefa-0f63-32d1-b4aa-191e41bcea3e | 1.67708 | -55.96201 | 2026-09-28 04:32:00 | NOAA-21 | ORIXIMINÁ | PARÁ | Brasil | 1505304 | 15 | 33 | nan | nan | nan | Amazônia | 0.9 |
| cb82699d-d2c4-35ec-885e-21ec05869a50 | -2.27167 | -57.01489 | 2026-09-28 04:32:00 | NOAA-21 | NHAMUNDÁ | AMAZONAS | Brasil | 1303007 | 13 | 33 | nan | nan | nan | Amazônia | 11.9 |
| 273c411d-dc8d-3637-9adf-6d7f92d80318 | -2.67075 | -56.45814 | 2026-09-28 04:32:00 | NOAA-21 | JURUTI | PARÁ | Brasil | 1503903 | 15 | 33 | nan | nan | nan | Amazônia | 1.1 |
| 7d63e328-92f5-3c9e-bb5c-01f05386589f | -2.05271 | -56.86563 | 2026-09-28 04:32:00 | NOAA-21 | NHAMUNDÁ | AMAZONAS | Brasil | 1303007 | 13 | 33 | nan | nan | nan | Amazônia | 2.2 |
| ff8d52b6-35cf-396a-88df-5a539fb812c3 | -1.75285 | -55.64985 | 2026-09-28 04:32:00 | NOAA-21 | ÓBIDOS | PARÁ | Brasil | 1505106 | 15 | 33 | nan | nan | nan | Amazônia | 1.3 |
| 41acc0a7-a75d-3190-9cc3-a6381e6a17e6 | -3.00766 | -54.21075 | 2026-09-28 04:32:00 | NOAA-21 | SANTARÉM | PARÁ | Brasil | 1506807 | 15 | 33 | nan | nan | nan | Amazônia | 2.0 |
| ba1157b7-1794-3e2a-8a48-ebbfd9d40d1e | -2.05873 | -56.86933 | 2026-09-28 04:32:00 | NOAA-21 | NHAMUNDÁ | AMAZONAS | Brasil | 1303007 | 13 | 33 | nan | nan | nan | Amazônia | 3.6 |
| a1855838-2382-3bd1-a55c-7c75a391b0ac | -3.82377 | -44.096 | 2026-09-28 04:32:00 | NOAA-21 | PIRAPEMAS | MARANHÃO | Brasil | 2108801 | 21 | 33 | nan | nan | nan | Cerrado | 2.5 |
| e4f4f9dd-9318-37c5-ac6c-dc25530203f2 | 1.83373 | -50.86724 | 2026-09-28 04:32:00 | NOAA-21 | AMAPÁ | AMAPÁ | Brasil | 1600105 | 16 | 33 | nan | nan | nan | Amazônia | 1.4 |
| ef51b23b-76f0-3f78-aebc-e91add156ac2 | -1.92772 | -52.13676 | 2026-09-28 04:32:00 | NOAA-21 | PORTO DE MOZ | PARÁ | Brasil | 1505908 | 15 | 33 | nan | nan | nan | Amazônia | 2.6 |
| f081bab9-ca97-3603-a7b6-47230b826db5 | -3.22564 | -54.31731 | 2026-09-28 04:32:00 | NOAA-21 | MOJUÍ DOS CAMPOS | PARÁ | Brasil | 1504752 | 15 | 33 | nan | nan | nan | Amazônia | 1.8 |
| 2c6cabb9-c1ca-344a-a284-def58c7db9ae | -3.15313 | -54.09396 | 2026-09-28 04:32:00 | NOAA-21 | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | 3.0 |
| 63cfccd4-8b41-3904-8825-3ff534b8d85b | -2.87076 | -50.40226 | 2026-09-28 04:32:00 | NOAA-21 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 3.0 |
| 39eda756-8dc9-3be1-b50d-5301cbc91119 | -2.9084 | -54.12524 | 2026-09-28 04:32:00 | NOAA-21 | SANTARÉM | PARÁ | Brasil | 1506807 | 15 | 33 | nan | nan | nan | Amazônia | 2.7 |


[Clique aqui para ver as próximas entradas](README29.md)
