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

## Dados Diários - Página 74

| ID | Latitude | Longitude | Data/Hora GMT | Satélite | Município | Estado | País | Município ID | Estado ID | País ID | Dias sem Chuva | Precipitação | Risco de Fogo | Bioma | FRP |
|----|----------|-----------|---------------|----------|-----------|--------|------|--------------|-----------|---------|----------------|--------------|----------------|-------|-----|
| 6a6aa150-3d78-3056-8840-c3b3c9d6d478 | -9.4819 | -66.7836 | 2026-09-30 15:50:00 | GOES-19 | LÁBREA | AMAZONAS | Brasil | 1302405 | 13 | 33 | nan | nan | nan | Amazônia | 70.0 |
| 4aca9dc9-ec4b-330a-b307-68e9bdcfd2a2 | -2.0933 | -49.557 | 2026-09-30 15:50:00 | GOES-19 | CAMETÁ | PARÁ | Brasil | 1502103 | 15 | 33 | nan | nan | nan | Amazônia | 98.2 |
| aadad9bf-66b7-392e-8e69-1e7af2b6637c | -15.251 | -41.6845 | 2026-09-30 15:50:00 | GOES-19 | NINHEIRA | MINAS GERAIS | Brasil | 3144656 | 31 | 33 | nan | nan | nan | Mata Atlântica | 164.0 |
| 2fdf5a07-a53b-3255-80d4-ef8df5518b49 | -1.2085 | -49.0838 | 2026-09-30 15:50:00 | GOES-19 | PONTA DE PEDRAS | PARÁ | Brasil | 1505700 | 15 | 33 | nan | nan | nan | Amazônia | 105.7 |
| 89de005f-11c7-37c3-8ca8-a29b77a223a6 | -1.1901 | -49.084 | 2026-09-30 16:00:00 | GOES-19 | PONTA DE PEDRAS | PARÁ | Brasil | 1505700 | 15 | 33 | nan | nan | nan | Amazônia | 100.5 |
| dfbc3299-4e12-3633-83e2-a9636ab7a8ab | -9.0584 | -66.1073 | 2026-09-30 16:00:00 | GOES-19 | LÁBREA | AMAZONAS | Brasil | 1302405 | 13 | 33 | nan | nan | nan | Amazônia | 65.6 |
| 0037634b-6efc-38dc-a946-ad5586b4a06b | -2.0933 | -49.557 | 2026-09-30 16:00:00 | GOES-19 | CAMETÁ | PARÁ | Brasil | 1502103 | 15 | 33 | nan | nan | nan | Amazônia | 96.3 |
| 2ee2388b-424c-3b88-b645-795a9f168aee | -9.077 | -66.0881 | 2026-09-30 16:00:00 | GOES-19 | LÁBREA | AMAZONAS | Brasil | 1302405 | 13 | 33 | nan | nan | nan | Amazônia | 51.4 |
| 607bf362-ff59-3107-bbac-2d230887f2eb | -9.4819 | -66.7836 | 2026-09-30 16:00:00 | GOES-19 | LÁBREA | AMAZONAS | Brasil | 1302405 | 13 | 33 | nan | nan | nan | Amazônia | 66.7 |
| 64d554b2-0fd5-31e6-9bb3-1d80b89a9af1 | -8.6451 | -45.3489 | 2026-09-30 16:10:00 | GOES-19 | BAIXA GRANDE DO RIBEIRO | PIAUÍ | Brasil | 2201150 | 22 | 33 | nan | nan | nan | Cerrado | 153.8 |
| bb4548c9-cbb5-3a97-babf-5c9d24c33f95 | -0.8399 | -48.725 | 2026-09-30 16:10:00 | GOES-19 | CACHOEIRA DO ARARI | PARÁ | Brasil | 1502004 | 15 | 33 | nan | nan | nan | Amazônia | 81.7 |
| 62b6598b-6616-3c34-b63f-57de1b53bc72 | -15.22 | -41.7 | 2026-09-30 16:15:00 | MSG-03 | NINHEIRA | MINAS GERAIS | Brasil | 3144656 | 31 | 33 | nan | nan | nan | Mata Atlântica | nan |
| 28805d7d-d1e2-3179-8716-f633ee901db1 | -15.74 | -43.67 | 2026-09-30 16:15:00 | MSG-03 | SÃO JOÃO DA PONTE | MINAS GERAIS | Brasil | 3162401 | 31 | 33 | nan | nan | nan | Cerrado | nan |
| 5bfed34d-98ca-3978-91aa-4d7d2e9f4f19 | -15.77 | -43.68 | 2026-09-30 16:15:00 | MSG-03 | SÃO JOÃO DA PONTE | MINAS GERAIS | Brasil | 3162401 | 31 | 33 | nan | nan | nan | Cerrado | nan |
| a632106f-5f22-332b-a0bd-4cf376677357 | -4.29 | -50.76 | 2026-09-30 16:15:00 | MSG-03 | NOVO REPARTIMENTO | PARÁ | Brasil | 1505064 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| f0572a88-6474-3974-9d87-03c8cd5fe2cc | -4.26 | -50.75 | 2026-09-30 16:15:00 | MSG-03 | NOVO REPARTIMENTO | PARÁ | Brasil | 1505064 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| d4e91b4e-21c1-3cdb-b770-21f4c8666477 | -3.11 | -50.25 | 2026-09-30 16:15:00 | MSG-03 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| 41e8beda-b8c3-366c-97c3-1ef5231e3058 | -15.25 | -41.71 | 2026-09-30 16:15:00 | MSG-03 | NINHEIRA | MINAS GERAIS | Brasil | 3144656 | 31 | 33 | nan | nan | nan | Mata Atlântica | nan |
| 987c009d-860f-37dc-8c2f-86ac58219181 | -3.11 | -50.31 | 2026-09-30 16:15:00 | MSG-03 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| 2a18d316-987d-392e-be57-e51eb69fb502 | -5.73 | -45.14 | 2026-09-30 16:15:00 | MSG-03 | BARRA DO CORDA | MARANHÃO | Brasil | 2101608 | 21 | 33 | nan | nan | nan | Cerrado | nan |
| 3ca1d2c6-7054-381e-986b-869206fa297a | -5.76 | -45.14 | 2026-09-30 16:15:00 | MSG-03 | BARRA DO CORDA | MARANHÃO | Brasil | 2101608 | 21 | 33 | nan | nan | nan | Cerrado | nan |
| afea4ef5-88aa-3690-be49-785c41685a5f | -3.0 | -51.01 | 2026-09-30 16:15:00 | MSG-03 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| bbf4d71b-e050-3cc4-868f-4e5de5bbac5e | -2.97 | -51.01 | 2026-09-30 16:15:00 | MSG-03 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| 008abd72-c583-3ad8-afb8-deb9b3ae502b | -4.26 | -50.81 | 2026-09-30 16:15:00 | MSG-03 | PACAJÁ | PARÁ | Brasil | 1505486 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| f60024be-d9ed-36d8-af26-2c2e24e821b2 | -1.2085 | -49.0838 | 2026-09-30 16:50:00 | GOES-19 | PONTA DE PEDRAS | PARÁ | Brasil | 1505700 | 15 | 33 | nan | nan | nan | Amazônia | 101.5 |
| fc6bfbd0-4dc6-37e3-acaf-4359e5be0a99 | -4.23 | -50.75 | 2026-09-30 17:15:00 | MSG-03 | PACAJÁ | PARÁ | Brasil | 1505486 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| 2d1e6c9b-fed3-30bd-a5f2-5b3dfa222b17 | -5.76 | -45.19 | 2026-09-30 17:15:00 | MSG-03 | BARRA DO CORDA | MARANHÃO | Brasil | 2101608 | 21 | 33 | nan | nan | nan | Cerrado | nan |
| e131e66a-5a97-39d6-ba32-f5dfc5cde416 | -4.29 | -50.76 | 2026-09-30 17:15:00 | MSG-03 | NOVO REPARTIMENTO | PARÁ | Brasil | 1505064 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| e8119d0d-3c4b-37d6-91b7-21c3b204ec3f | -15.25 | -41.71 | 2026-09-30 17:15:00 | MSG-03 | NINHEIRA | MINAS GERAIS | Brasil | 3144656 | 31 | 33 | nan | nan | nan | Mata Atlântica | nan |
| 690e73cb-a923-3e34-b132-4b985dc34ddb | -3.9 | -44.3 | 2026-09-30 17:15:00 | MSG-03 | COROATÁ | MARANHÃO | Brasil | 2103604 | 21 | 33 | nan | nan | nan | Cerrado | nan |
| c83d5f27-d318-35bc-823c-13c2ae59435d | -3.11 | -50.31 | 2026-09-30 17:15:00 | MSG-03 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| 0e91951b-a4a9-38a8-b3b7-d2c94034a339 | -6.38 | -55.14 | 2026-09-30 17:15:00 | MSG-03 | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| d0ee4443-a8de-343c-86fa-f6a39e0657b5 | -3.58 | -53.98 | 2026-09-30 17:15:00 | MSG-03 | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| 5ca1d986-2de6-3466-94f6-630a47071dec | -12.44 | -44.15 | 2026-09-30 17:15:00 | MSG-03 | TABOCAS DO BREJO VELHO | BAHIA | Brasil | 2930907 | 29 | 33 | nan | nan | nan | Cerrado | nan |
| be3bd139-4a43-3704-b19b-4baa66dedb1a | -14.34 | -44.75 | 2026-09-30 17:15:00 | MSG-03 | COCOS | BAHIA | Brasil | 2908101 | 29 | 33 | nan | nan | nan | Cerrado | nan |
| 40bd526e-b10a-34e5-a28a-d0e72aaa8284 | -5.73 | -45.18 | 2026-09-30 17:15:00 | MSG-03 | BARRA DO CORDA | MARANHÃO | Brasil | 2101608 | 21 | 33 | nan | nan | nan | Cerrado | nan |
| 9d3df52a-c4bf-3549-ae5b-7788ee3385c0 | -3.11 | -50.25 | 2026-09-30 17:15:00 | MSG-03 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| ff95ad65-9992-3eac-b5f8-bb1513b54246 | -4.26 | -50.81 | 2026-09-30 17:15:00 | MSG-03 | PACAJÁ | PARÁ | Brasil | 1505486 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| 8778b991-3738-3499-8da6-816bf1d17cc9 | -5.73 | -45.14 | 2026-09-30 17:15:00 | MSG-03 | BARRA DO CORDA | MARANHÃO | Brasil | 2101608 | 21 | 33 | nan | nan | nan | Cerrado | nan |
| 89c51d7a-0af8-3c45-8030-b8f801739c96 | -8.21 | -45.48 | 2026-09-30 17:15:00 | MSG-03 | RIBEIRO GONÇALVES | PIAUÍ | Brasil | 2208908 | 22 | 33 | nan | nan | nan | Cerrado | nan |
| 54afc013-0bac-3b69-a548-a2be4eb5dbc0 | -6.35 | -55.13 | 2026-09-30 17:15:00 | MSG-03 | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| 23ae828b-b838-3d45-9b08-e5c3bf51c607 | -11.12 | -44.6 | 2026-09-30 17:15:00 | MSG-03 | SANTA RITA DE CÁSSIA | BAHIA | Brasil | 2928406 | 29 | 33 | nan | nan | nan | Cerrado | nan |
| 62a6ae8a-1235-39d0-b8cf-42a93a2478d2 | -5.76 | -45.14 | 2026-09-30 17:15:00 | MSG-03 | BARRA DO CORDA | MARANHÃO | Brasil | 2101608 | 21 | 33 | nan | nan | nan | Cerrado | nan |
| 6b4709bd-b3c8-317a-8a53-8480927c7933 | -12.47 | -44.16 | 2026-09-30 17:15:00 | MSG-03 | TABOCAS DO BREJO VELHO | BAHIA | Brasil | 2930907 | 29 | 33 | nan | nan | nan | Cerrado | nan |
| 140d5e35-fd60-3e90-bb35-9d8d2293f48b | -15.22 | -41.7 | 2026-09-30 17:15:00 | MSG-03 | NINHEIRA | MINAS GERAIS | Brasil | 3144656 | 31 | 33 | nan | nan | nan | Mata Atlântica | nan |
| e3fc08dc-e1c0-3dd3-8cce-0a497e9df26b | -4.26 | -50.75 | 2026-09-30 17:15:00 | MSG-03 | NOVO REPARTIMENTO | PARÁ | Brasil | 1505064 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| 440b50e7-306c-39c8-becb-445ad12f2160 | -4.26 | -50.7 | 2026-09-30 17:15:00 | MSG-03 | NOVO REPARTIMENTO | PARÁ | Brasil | 1505064 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| 291809a4-0c49-344b-8cb5-3ccc709ff670 | -11.23 | -44.3 | 2026-09-30 17:15:00 | MSG-03 | MANSIDÃO | BAHIA | Brasil | 2920452 | 29 | 33 | nan | nan | nan | Cerrado | nan |
| a14c8f5c-2813-3716-b566-7c7cf72b8c46 | 1.9792 | -50.8817 | 2026-09-30 17:20:00 | GOES-19 | AMAPÁ | AMAPÁ | Brasil | 1600105 | 16 | 33 | nan | nan | nan | Amazônia | 74.0 |
| b8409fb6-ea30-3f10-9dd5-a161c7e1d93d | -0.8399 | -48.725 | 2026-09-30 17:30:00 | GOES-19 | CACHOEIRA DO ARARI | PARÁ | Brasil | 1502004 | 15 | 33 | nan | nan | nan | Amazônia | 66.3 |
| 02d0e3c7-f2c4-3703-a72f-bcda010525ba | 1.924 | -50.8411 | 2026-09-30 17:40:00 | GOES-19 | AMAPÁ | AMAPÁ | Brasil | 1600105 | 16 | 33 | nan | nan | nan | Amazônia | 66.6 |
| 80f7eb1b-fcfc-33b8-b66e-73ed12f0e17b | -11.4495 | -43.4566 | 2026-09-30 17:40:00 | GOES-19 | BARRA | BAHIA | Brasil | 2902708 | 29 | 33 | nan | nan | nan | Cerrado | 511.1 |
| b6089420-68e6-31b5-badd-d8aa029cee2e | -10.5197 | -45.3784 | 2026-09-30 17:40:00 | GOES-19 | CORRENTE | PIAUÍ | Brasil | 2202901 | 22 | 33 | nan | nan | nan | Cerrado | 180.2 |
| aac469d2-f910-395d-b4c0-ce38d05f39e1 | 3.2375 | -60.668 | 2026-09-30 17:40:00 | GOES-19 | BOA VISTA | RORAIMA | Brasil | 1400100 | 14 | 33 | nan | nan | nan | Amazônia | 86.2 |
| 5967f62b-c084-36c5-b267-b468281c1450 | -10.9463 | -47.2869 | 2026-09-30 17:50:00 | GOES-19 | PONTE ALTA DO TOCANTINS | TOCANTINS | Brasil | 1717909 | 17 | 33 | nan | nan | nan | Cerrado | 101.0 |
| fb4f2477-94b2-3f00-92ad-c920ff8e672f | -11.1751 | -46.0663 | 2026-09-30 17:50:00 | GOES-19 | FORMOSA DO RIO PRETO | BAHIA | Brasil | 2911105 | 29 | 33 | nan | nan | nan | Cerrado | 138.3 |
| 68fe6f1a-85c9-3097-9d22-74bda9058e5f | -10.7112 | -45.3075 | 2026-09-30 17:50:00 | GOES-19 | CRISTALÂNDIA DO PIAUÍ | PIAUÍ | Brasil | 2203008 | 22 | 33 | nan | nan | nan | Cerrado | 233.6 |
| b1dc260b-c835-3068-a9c5-11a85f954dfc | -11.3555 | -43.3526 | 2026-09-30 17:50:00 | GOES-19 | BARRA | BAHIA | Brasil | 2902708 | 29 | 33 | nan | nan | nan | Cerrado | 215.7 |
| a082b2c9-a17b-3e9a-9ebf-0f57775e8bf2 | -10.5197 | -45.3784 | 2026-09-30 17:50:00 | GOES-19 | CORRENTE | PIAUÍ | Brasil | 2202901 | 22 | 33 | nan | nan | nan | Cerrado | 241.1 |
| 0a81ad20-b510-3dd4-9504-d2094ba4817d | -11.6994 | -43.4178 | 2026-09-30 17:50:00 | GOES-19 | BARRA | BAHIA | Brasil | 2902708 | 29 | 33 | nan | nan | nan | Cerrado | 124.5 |
| d1dc257a-c424-3d29-9c34-0abca8f04987 | -9.8064 | -44.8265 | 2026-09-30 17:50:00 | GOES-19 | RIACHO FRIO | PIAUÍ | Brasil | 2208858 | 22 | 33 | nan | nan | nan | Cerrado | 103.0 |
| fc412d0c-40c2-3b02-9d47-513e16bc0f5a | -15.2043 | -46.1374 | 2026-09-30 17:50:00 | GOES-19 | FORMOSO | MINAS GERAIS | Brasil | 3126208 | 31 | 33 | nan | nan | nan | Cerrado | 153.0 |
| 6114d120-546d-3ca9-9896-b18890cf8133 | -11.6596 | -43.4951 | 2026-09-30 17:50:00 | GOES-19 | BARRA | BAHIA | Brasil | 2902708 | 29 | 33 | nan | nan | nan | Cerrado | 133.7 |
| 909a726f-0ccf-3ec9-8f3a-b14312cf2de0 | -11.1903 | -45.1505 | 2026-09-30 17:50:00 | GOES-19 | FORMOSA DO RIO PRETO | BAHIA | Brasil | 2911105 | 29 | 33 | nan | nan | nan | Cerrado | 85.4 |
| cd4d476d-3157-3a7d-8e22-96041b508ec9 | -11.3747 | -43.3497 | 2026-09-30 17:50:00 | GOES-19 | BARRA | BAHIA | Brasil | 2902708 | 29 | 33 | nan | nan | nan | Cerrado | 133.7 |
| 4aec89c7-0213-32ac-8b17-318d2c509cff | -15.2043 | -46.1374 | 2026-09-30 18:00:00 | GOES-19 | FORMOSO | MINAS GERAIS | Brasil | 3126208 | 31 | 33 | nan | nan | nan | Cerrado | 147.1 |
| 3cf9b537-3dea-3722-9bf2-39899b41b544 | -13.384 | -43.9895 | 2026-09-30 18:00:00 | GOES-19 | SÃO FÉLIX DO CORIBE | BAHIA | Brasil | 2929057 | 29 | 33 | nan | nan | nan | Cerrado | 139.6 |
| 47b02cff-9ca0-3176-87c5-d0400ea9b403 | -11.3555 | -43.3526 | 2026-09-30 18:00:00 | GOES-19 | BARRA | BAHIA | Brasil | 2902708 | 29 | 33 | nan | nan | nan | Cerrado | 244.0 |
| 13533b9f-5d48-31dd-8f85-2d09c7c1446c | -11.7182 | -43.4386 | 2026-09-30 18:00:00 | GOES-19 | BARRA | BAHIA | Brasil | 2902708 | 29 | 33 | nan | nan | nan | Cerrado | 201.9 |
| c666f771-84f0-3c77-8ba3-2288732af81c | -12.4539 | -44.1702 | 2026-09-30 18:00:00 | GOES-19 | TABOCAS DO BREJO VELHO | BAHIA | Brasil | 2930907 | 29 | 33 | nan | nan | nan | Cerrado | 114.6 |
| 881c2279-79dc-3e51-997d-10a32c127b00 | -10.907 | -43.8433 | 2026-09-30 18:00:00 | GOES-19 | BARRA | BAHIA | Brasil | 2902708 | 29 | 33 | nan | nan | nan | Cerrado | 129.8 |
| 9627fb0e-6c30-325d-94c0-7e208ef2b0da | -16.9203 | -42.1171 | 2026-09-30 18:00:00 | GOES-19 | ARAÇUAÍ | MINAS GERAIS | Brasil | 3103405 | 31 | 33 | nan | nan | nan | Mata Atlântica | 168.6 |
| 584e39ab-22a8-3cea-b233-6eb2404d491d | -11.3931 | -43.3942 | 2026-09-30 18:00:00 | GOES-19 | BARRA | BAHIA | Brasil | 2902708 | 29 | 33 | nan | nan | nan | Cerrado | 103.0 |
| 32f03d26-24e8-3566-a845-0afc2bef1fbf | -10.7115 | -45.2845 | 2026-09-30 18:00:00 | GOES-19 | CRISTALÂNDIA DO PIAUÍ | PIAUÍ | Brasil | 2203008 | 22 | 33 | nan | nan | nan | Cerrado | 96.8 |
| 6efa3634-37bf-3f96-8b8d-ebe8c979bb82 | -11.4499 | -43.4329 | 2026-09-30 18:00:00 | GOES-19 | BARRA | BAHIA | Brasil | 2902708 | 29 | 33 | nan | nan | nan | Cerrado | 267.2 |
| 50946154-9ca9-39a4-8d08-49454e9c40d0 | -9.8064 | -44.8265 | 2026-09-30 18:00:00 | GOES-19 | RIACHO FRIO | PIAUÍ | Brasil | 2208858 | 22 | 33 | nan | nan | nan | Cerrado | 252.9 |
| e5699bd4-cba6-3e25-9d15-9e3d560780bf | -9.7877 | -44.8058 | 2026-09-30 18:00:00 | GOES-19 | RIACHO FRIO | PIAUÍ | Brasil | 2208858 | 22 | 33 | nan | nan | nan | Cerrado | 103.3 |
| b4a36346-5cd6-34fe-8303-cc0a78efd48a | -11.64 | -43.5218 | 2026-09-30 18:00:00 | GOES-19 | BARRA | BAHIA | Brasil | 2902708 | 29 | 33 | nan | nan | nan | Cerrado | 143.4 |
| 1264eaa9-11ee-3557-9a2d-6951f6c867b7 | -12.514 | -43.0703 | 2026-09-30 18:00:00 | GOES-19 | PARATINGA | BAHIA | Brasil | 2923704 | 29 | 33 | nan | nan | nan | Caatinga | 144.0 |
| efbc7829-bd92-31ac-9fd5-6ce897abbe72 | 1.822 | -55.6247 | 2026-09-30 18:00:00 | GOES-19 | ÓBIDOS | PARÁ | Brasil | 1505106 | 15 | 33 | nan | nan | nan | Amazônia | 65.8 |
| 31d34bd2-f2ba-34e5-977b-20950531b0a6 | -10.5197 | -45.3784 | 2026-09-30 18:00:00 | GOES-19 | CORRENTE | PIAUÍ | Brasil | 2202901 | 22 | 33 | nan | nan | nan | Cerrado | 179.9 |
| 072ce83d-f6a8-3882-b9fa-b3ce3afe007f | -11.2095 | -45.1478 | 2026-09-30 18:00:00 | GOES-19 | FORMOSA DO RIO PRETO | BAHIA | Brasil | 2911105 | 29 | 33 | nan | nan | nan | Cerrado | 40.8 |
| 0a482a66-0e87-3e1c-a8aa-6cb72b4eb776 | -10.9463 | -47.2869 | 2026-09-30 18:00:00 | GOES-19 | PONTE ALTA DO TOCANTINS | TOCANTINS | Brasil | 1717909 | 17 | 33 | nan | nan | nan | Cerrado | 70.6 |
| 5b000b56-dc2b-32da-bd31-4a95466a8640 | -7.9723 | -71.3443 | 2026-09-30 18:00:00 | GOES-19 | TARAUACÁ | ACRE | Brasil | 1200609 | 12 | 33 | nan | nan | nan | Amazônia | 90.7 |
| 8d5de817-fe1c-3f9e-8326-ba44382ad04b | -11.4311 | -43.4121 | 2026-09-30 18:00:00 | GOES-19 | BARRA | BAHIA | Brasil | 2902708 | 29 | 33 | nan | nan | nan | Cerrado | 199.4 |
| bc7f9b86-4eaa-3bbd-8493-d3c7b9729fe6 | -7.9907 | -71.3441 | 2026-09-30 18:00:00 | GOES-19 | TARAUACÁ | ACRE | Brasil | 1200609 | 12 | 33 | nan | nan | nan | Amazônia | 72.3 |
| 739b0d10-7165-3e30-9bec-cccf03352ec2 | -11.1751 | -46.0663 | 2026-09-30 18:00:00 | GOES-19 | FORMOSA DO RIO PRETO | BAHIA | Brasil | 2911105 | 29 | 33 | nan | nan | nan | Cerrado | 86.6 |
| 1af78a0e-f1bf-3bb9-9253-50b36c31c1db | 1.8037 | -55.6249 | 2026-09-30 18:00:00 | GOES-19 | ÓBIDOS | PARÁ | Brasil | 1505106 | 15 | 33 | nan | nan | nan | Amazônia | 61.2 |
| 34b3fb7c-77c7-35a4-9a6f-4f4d51a70661 | -9.8617 | -44.9347 | 2026-09-30 18:00:00 | GOES-19 | RIACHO FRIO | PIAUÍ | Brasil | 2208858 | 22 | 33 | nan | nan | nan | Cerrado | 103.9 |
| 6cd73774-438d-364e-8f38-63a908910b9b | -12.4962 | -44.98 | 2026-09-30 18:00:00 | GOES-19 | SÃO DESIDÉRIO | BAHIA | Brasil | 2928901 | 29 | 33 | nan | nan | nan | Cerrado | 76.6 |
| 3bf019dc-cb18-3291-ba4d-2caccc2f7d1d | -11.4119 | -43.415 | 2026-09-30 18:00:00 | GOES-19 | BARRA | BAHIA | Brasil | 2902708 | 29 | 33 | nan | nan | nan | Cerrado | 285.7 |
| c5474282-a203-3f6f-89ae-1fba18c62fbf | -10.7112 | -45.3075 | 2026-09-30 18:10:00 | GOES-19 | CRISTALÂNDIA DO PIAUÍ | PIAUÍ | Brasil | 2203008 | 22 | 33 | nan | nan | nan | Cerrado | 181.5 |
| 060418f8-0c87-3f1e-9420-9f678b5658fd | -9.7687 | -44.8082 | 2026-09-30 18:10:00 | GOES-19 | RIACHO FRIO | PIAUÍ | Brasil | 2208858 | 22 | 33 | nan | nan | nan | Cerrado | 81.7 |
| 806e39f5-c28e-3118-a61f-4f1a23e1cae7 | -10.7115 | -45.2845 | 2026-09-30 18:10:00 | GOES-19 | CRISTALÂNDIA DO PIAUÍ | PIAUÍ | Brasil | 2203008 | 22 | 33 | nan | nan | nan | Cerrado | 89.2 |
| 7828b7ec-7f67-3a5d-b15b-da3709046c2d | -13.384 | -43.9895 | 2026-09-30 18:10:00 | GOES-19 | SÃO FÉLIX DO CORIBE | BAHIA | Brasil | 2929057 | 29 | 33 | nan | nan | nan | Cerrado | 193.4 |
| 572e7ea9-9dcb-3bbe-8894-075834fbfa6b | -10.907 | -43.8433 | 2026-09-30 18:10:00 | GOES-19 | BARRA | BAHIA | Brasil | 2902708 | 29 | 33 | nan | nan | nan | Cerrado | 153.3 |
| f2bc255b-f16a-36d2-9e98-2faf08eaf7da | -11.4687 | -43.4537 | 2026-09-30 18:10:00 | GOES-19 | BARRA | BAHIA | Brasil | 2902708 | 29 | 33 | nan | nan | nan | Cerrado | 226.5 |
| dddf21d3-b6ae-35cd-9e2d-40b54ae76024 | -11.4307 | -43.4358 | 2026-09-30 18:10:00 | GOES-19 | BARRA | BAHIA | Brasil | 2902708 | 29 | 33 | nan | nan | nan | Cerrado | 178.2 |
| be8a20eb-18d9-3cb8-bc78-2c202516dfe3 | -10.5197 | -45.3784 | 2026-09-30 18:10:00 | GOES-19 | CORRENTE | PIAUÍ | Brasil | 2202901 | 22 | 33 | nan | nan | nan | Cerrado | 122.1 |
| d012b347-3bb1-3a07-a8ae-486b3b76c416 | -11.3935 | -43.3705 | 2026-09-30 18:10:00 | GOES-19 | BARRA | BAHIA | Brasil | 2902708 | 29 | 33 | nan | nan | nan | Cerrado | 150.9 |


[Clique aqui para ver as próximas entradas](README75.md)
