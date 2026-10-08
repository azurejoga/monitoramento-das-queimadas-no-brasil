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

## Dados Diários - Página 22

| ID | Latitude | Longitude | Data/Hora GMT | Satélite | Município | Estado | País | Município ID | Estado ID | País ID | Dias sem Chuva | Precipitação | Risco de Fogo | Bioma | FRP |
|----|----------|-----------|---------------|----------|-----------|--------|------|--------------|-----------|---------|----------------|--------------|----------------|-------|-----|
| 7c090614-f834-32f4-9968-38cdad553a9a | -2.9205 | -54.138 | 2026-10-08 00:26:00 | METOP-B | SANTARÉM | PARÁ | Brasil | 1506807 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| 7d1a2757-db58-3ed3-9e93-cfa984a5a24d | -3.507 | -59.3269 | 2026-10-08 00:26:00 | METOP-B | AUTAZES | AMAZONAS | Brasil | 1300300 | 13 | 33 | nan | nan | nan | Amazônia | nan |
| c6173aff-6331-3764-ad1a-7d19e422b829 | -5.9916 | -55.372101 | 2026-10-08 00:26:00 | METOP-B | ITAITUBA | PARÁ | Brasil | 1503606 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| 61963e44-2819-3feb-ac63-4ee9975b0d2c | -6.2251 | -52.798901 | 2026-10-08 00:26:00 | METOP-B | SÃO FÉLIX DO XINGU | PARÁ | Brasil | 1507300 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| cdc1c07e-fb38-3a5f-8b9a-78968f52df22 | -3.822 | -58.987301 | 2026-10-08 00:26:00 | METOP-B | NOVA OLINDA DO NORTE | AMAZONAS | Brasil | 1303106 | 13 | 33 | nan | nan | nan | Amazônia | nan |
| 8230c332-285d-3dd4-8b0b-947cbb5c6506 | -7.4038 | -55.148102 | 2026-10-08 00:26:00 | METOP-B | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| 164d6652-4f06-3969-baf0-3f79d1e5d08d | -5.2375 | -56.007 | 2026-10-08 00:26:00 | METOP-B | TRAIRÃO | PARÁ | Brasil | 1508050 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| 9122debf-280c-3940-93c6-7e4f11719998 | -3.0469 | -53.876801 | 2026-10-08 00:26:00 | METOP-B | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| b8c09d12-1f0a-32ff-9f8e-1b33d6be9beb | -3.1209 | -53.7943 | 2026-10-08 00:26:00 | METOP-B | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| b7e9744b-fe1d-3c6a-9f5f-b6765dbcb629 | -3.519 | -59.334499 | 2026-10-08 00:26:00 | METOP-B | AUTAZES | AMAZONAS | Brasil | 1300300 | 13 | 33 | nan | nan | nan | Amazônia | nan |
| ba52ff9e-b985-378c-9447-6793b5806d5b | -3.0936 | -53.719501 | 2026-10-08 00:26:00 | METOP-B | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| b841dcf9-b08e-3a9a-af03-3e2297577d69 | -6.0999 | -55.719299 | 2026-10-08 00:26:00 | METOP-B | ITAITUBA | PARÁ | Brasil | 1503606 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| 820a3186-f4b3-35a3-bdbc-23d2cbb33ab2 | -15.3267 | -42.774101 | 2026-10-08 00:26:00 | METOP-B | MONTE AZUL | MINAS GERAIS | Brasil | 3142908 | 31 | 33 | nan | nan | nan | Cerrado | nan |
| ca318a2d-737b-30a6-b47b-98a2f797f32c | -3.854 | -52.0364 | 2026-10-08 00:26:00 | METOP-B | SENADOR JOSÉ PORFÍRIO | PARÁ | Brasil | 1507805 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| a311d5cc-4082-3ff4-85e8-90fcd59cd52c | -3.1066 | -54.139999 | 2026-10-08 00:26:00 | METOP-B | SANTARÉM | PARÁ | Brasil | 1506807 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| f9e11164-1cbf-3766-9e80-5b985ad08c3a | -2.8875 | -54.1744 | 2026-10-08 00:26:00 | METOP-B | SANTARÉM | PARÁ | Brasil | 1506807 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| a403327e-88a9-39e9-8f9e-11f06aceb1b2 | -2.9401 | -54.133701 | 2026-10-08 00:26:00 | METOP-B | SANTARÉM | PARÁ | Brasil | 1506807 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| a0c4a38c-dbaa-366d-9ef3-c5664e25542a | -4.073 | -59.846401 | 2026-10-08 00:26:00 | METOP-B | AUTAZES | AMAZONAS | Brasil | 1300300 | 13 | 33 | nan | nan | nan | Amazônia | nan |
| d05c895c-7e29-3727-8873-878a2a6eb4ed | -2.9786 | -54.030602 | 2026-10-08 00:26:00 | METOP-B | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| 40266c0e-059c-3748-8393-148661d9ebc8 | -3.0119 | -54.132099 | 2026-10-08 00:26:00 | METOP-B | SANTARÉM | PARÁ | Brasil | 1506807 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| d6867606-a2df-37a5-80e8-9c3e012f5858 | -3.1227 | -53.757099 | 2026-10-08 00:26:00 | METOP-B | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| 53a188b7-b704-3cb2-8a46-bbfb6c570f0e | -2.9923 | -54.136501 | 2026-10-08 00:26:00 | METOP-B | SANTARÉM | PARÁ | Brasil | 1506807 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| 61775a0a-81db-3fe1-94cf-eb0a298381c7 | -3.7241 | -54.225899 | 2026-10-08 00:26:00 | METOP-B | PLACAS | PARÁ | Brasil | 1505650 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| f6507bf7-ef81-3834-8876-c26e0474156c | -3.2554 | -54.6604 | 2026-10-08 00:26:00 | METOP-B | MOJUÍ DOS CAMPOS | PARÁ | Brasil | 1504752 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| ab4daa35-4ed1-3e10-a060-93378a01dbf6 | -2.0443 | -56.876801 | 2026-10-08 00:26:00 | METOP-B | NHAMUNDÁ | AMAZONAS | Brasil | 1303007 | 13 | 33 | nan | nan | nan | Amazônia | nan |
| 80ed4ac3-a6ea-341c-833f-57e72e478b8b | -3.8396 | -55.9729 | 2026-10-08 00:26:00 | METOP-B | AVEIRO | PARÁ | Brasil | 1501006 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| 16e6a3a8-bdf1-339e-8283-41f5c8de5ad9 | -3.0151 | -54.145901 | 2026-10-08 00:26:00 | METOP-B | SANTARÉM | PARÁ | Brasil | 1506807 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| c5661133-9f96-379b-b430-ce76ae1a02da | -2.8574 | -49.548599 | 2026-10-08 00:26:00 | METOP-B | BAIÃO | PARÁ | Brasil | 1501204 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| 33855214-161b-3c96-801f-5962766e165a | -1.8213 | -54.929298 | 2026-10-08 00:26:00 | METOP-B | ALENQUER | PARÁ | Brasil | 1500404 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| 66d96717-4021-311f-a460-d89e44f0e6bf | -13.8077 | -52.779301 | 2026-10-08 00:26:00 | METOP-B | ÁGUA BOA | MATO GROSSO | Brasil | 5100201 | 51 | 33 | nan | nan | nan | Cerrado | nan |
| 9ed0ad19-a21d-36f4-810c-a095041c6f6b | -3.0793 | -54.247299 | 2026-10-08 00:26:00 | METOP-B | MOJUÍ DOS CAMPOS | PARÁ | Brasil | 1504752 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| 52ce00fe-92ed-3ec5-a507-2d44045f2f75 | -2.853 | -59.110001 | 2026-10-08 00:26:00 | METOP-B | ITACOATIARA | AMAZONAS | Brasil | 1301902 | 13 | 33 | nan | nan | nan | Amazônia | nan |
| da9c2b0a-105e-3408-8f17-d3e90fa86645 | -7.1914 | -45.355 | 2026-10-08 00:26:00 | METOP-B | SAMBAÍBA | MARANHÃO | Brasil | 2109700 | 21 | 33 | nan | nan | nan | Cerrado | nan |
| 78db6e80-1da5-3048-a873-50c953cc7f5b | -3.4913 | -59.580101 | 2026-10-08 00:26:00 | METOP-B | CAREIRO DA VÁRZEA | AMAZONAS | Brasil | 1301159 | 13 | 33 | nan | nan | nan | Amazônia | nan |
| d1d2fcfe-d8d7-3bdb-9131-44ed24fb8ce4 | -5.9818 | -55.374298 | 2026-10-08 00:26:00 | METOP-B | ITAITUBA | PARÁ | Brasil | 1503606 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| 76dc7d66-3fba-3913-967f-a27d738c0209 | -5.877 | -53.489899 | 2026-10-08 00:26:00 | METOP-B | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| e1c2c49d-5b6d-3cdd-b9c1-b5e213901c4e | -2.937 | -54.1199 | 2026-10-08 00:26:00 | METOP-B | SANTARÉM | PARÁ | Brasil | 1506807 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| 93d54c7e-0ae1-3c90-9624-90182f8b9f52 | -3.4799 | -55.426899 | 2026-10-08 00:26:00 | METOP-B | AVEIRO | PARÁ | Brasil | 1501006 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| 41b1a672-70a4-3a3f-9e98-09b19cf721ff | -4.9248 | -55.8517 | 2026-10-08 00:26:00 | METOP-B | TRAIRÃO | PARÁ | Brasil | 1508050 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| 231e8f5f-e515-32e5-873b-1ed1b5434c11 | -1.4738 | -54.5327 | 2026-10-08 00:26:00 | METOP-B | MONTE ALEGRE | PARÁ | Brasil | 1504802 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| 73ae7d43-4e3c-3410-b90a-8069c0df984a | -3.0225 | -53.860298 | 2026-10-08 00:26:00 | METOP-B | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| 5d6aa756-1e61-34fb-a55e-9fb78584e8e8 | -3.2793 | -53.9925 | 2026-10-08 00:26:00 | METOP-B | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| 1f6743c1-5cf1-3814-b8e2-20260d030566 | -3.0665 | -54.372601 | 2026-10-08 00:26:00 | METOP-B | MOJUÍ DOS CAMPOS | PARÁ | Brasil | 1504752 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| 07e8e669-212c-3a68-8daa-b556411bdca8 | -2.9241 | -54.1082 | 2026-10-08 00:26:00 | METOP-B | SANTARÉM | PARÁ | Brasil | 1506807 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| f8af388a-5a29-38d6-a3f9-261b67b2de7f | -3.6631 | -54.275501 | 2026-10-08 00:26:00 | METOP-B | PLACAS | PARÁ | Brasil | 1505650 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| 4315d117-1c9f-3e51-b287-7e0635f0d006 | -2.9283 | -54.172501 | 2026-10-08 00:26:00 | METOP-B | SANTARÉM | PARÁ | Brasil | 1506807 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| 4221d607-dce5-3ab4-9b6c-7a15201667b7 | -6.422 | -54.9478 | 2026-10-08 00:26:00 | METOP-B | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| e5af973b-f53b-3a5a-9a4e-faf2a3ec44c2 | -3.5934 | -54.2407 | 2026-10-08 00:26:00 | METOP-B | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| 21bc48ce-aa54-3e3f-b98d-7054e1cc08d8 | -11.6209 | -43.6964 | 2026-10-08 00:26:00 | METOP-B | BARRA | BAHIA | Brasil | 2902708 | 29 | 33 | nan | nan | nan | Cerrado | nan |
| c10f2782-3e6a-3606-9634-c87f9838452f | -3.7378 | -59.442402 | 2026-10-08 00:26:00 | METOP-B | AUTAZES | AMAZONAS | Brasil | 1300300 | 13 | 33 | nan | nan | nan | Amazônia | nan |
| 32515b45-78d1-38ad-8e50-8ffcce243b90 | -3.3322 | -52.504101 | 2026-10-08 00:26:00 | METOP-B | BRASIL NOVO | PARÁ | Brasil | 1501725 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| 02ab5d1e-8902-3992-81f7-8abb0f0e03f2 | -3.1649 | -54.7164 | 2026-10-08 00:26:00 | METOP-B | MOJUÍ DOS CAMPOS | PARÁ | Brasil | 1504752 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| f141c605-a554-362d-a520-13db18a1ecaa | -2.4737 | -56.084202 | 2026-10-08 00:26:00 | METOP-B | JURUTI | PARÁ | Brasil | 1503903 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| 0f88dbd8-2e6a-3f15-b3f7-e62ad21a6d2b | -6.2278 | -55.646198 | 2026-10-08 00:26:00 | METOP-B | ITAITUBA | PARÁ | Brasil | 1503606 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| b8d08370-9ec2-3272-a76b-ccddebdb244a | -2.4867 | -56.095901 | 2026-10-08 00:26:00 | METOP-B | JURUTI | PARÁ | Brasil | 1503903 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| 7cf9beaf-c39b-3a21-9189-818c867f3a5d | -6.8544 | -55.779598 | 2026-10-08 00:26:00 | METOP-B | NOVO PROGRESSO | PARÁ | Brasil | 1505031 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| fa0c46b6-f26b-375f-b76f-777310b9d0b4 | -3.1675 | -54.090199 | 2026-10-08 00:26:00 | METOP-B | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| 2b42a638-82e9-3b2c-9ce4-439923e5edf7 | -2.8852 | -54.073299 | 2026-10-08 00:26:00 | METOP-B | PRAINHA | PARÁ | Brasil | 1506005 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| 01e3e465-af1c-3e5d-a6c2-ffce7cc7f42e | -2.9269 | -58.289101 | 2026-10-08 00:26:00 | METOP-B | SILVES | AMAZONAS | Brasil | 1304005 | 13 | 33 | nan | nan | nan | Amazônia | nan |
| e650473e-6a61-3807-a9f9-ac65a64965eb | -2.5793 | -56.141201 | 2026-10-08 00:26:00 | METOP-B | JURUTI | PARÁ | Brasil | 1503903 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| 8c8c048e-ff2f-38a1-a874-a7357bb5c1ec | -2.4863 | -56.139801 | 2026-10-08 00:26:00 | METOP-B | JURUTI | PARÁ | Brasil | 1503903 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| 545ba2dc-4e6d-3b54-994d-c00f5c0f0008 | -3.001 | -53.901699 | 2026-10-08 00:26:00 | METOP-B | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| 8a48ea7f-1f7f-3bd0-972f-cf4c354cd552 | 1.7001 | -55.632301 | 2026-10-08 00:26:00 | METOP-B | ÓBIDOS | PARÁ | Brasil | 1505106 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| c6109d2c-c313-3bbc-802f-94a0920f1e1e | -4.5643 | -54.203602 | 2026-10-08 00:26:00 | METOP-B | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| cdcaf6f9-8ed1-365a-8d94-5aeaa2d9ea86 | -3.2133 | -53.8834 | 2026-10-08 00:26:00 | METOP-B | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| a8ce0634-c331-33fb-bb2e-6d733684e6ad | -3.0109 | -54.0816 | 2026-10-08 00:26:00 | METOP-B | SANTARÉM | PARÁ | Brasil | 1506807 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| 46def8fc-f41f-3b3d-9f10-e133a166649f | -3.5806 | -55.599499 | 2026-10-08 00:26:00 | METOP-B | AVEIRO | PARÁ | Brasil | 1501006 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| 183d4d50-6725-3633-8844-5a67cf168f22 | -3.6799 | -53.7132 | 2026-10-08 00:26:00 | METOP-B | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| 980a2bc6-1d56-366f-9ec0-925ffd6c5729 | 1.7806 | -55.5499 | 2026-10-08 00:26:00 | METOP-B | ÓBIDOS | PARÁ | Brasil | 1505106 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| d500cd78-7156-3b26-9245-20947300ef87 | 3.1624 | -60.573299 | 2026-10-08 00:26:00 | METOP-B | BOA VISTA | RORAIMA | Brasil | 1400100 | 14 | 33 | nan | nan | nan | Amazônia | nan |
| 86d2cdf8-f998-3c6f-a10a-f8a43cfc09db | -2.491 | -56.160702 | 2026-10-08 00:26:00 | METOP-B | JURUTI | PARÁ | Brasil | 1503903 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| a855c9df-d40d-3590-8404-fbc52c4b003a | -9.8727 | -50.492699 | 2026-10-08 00:26:00 | METOP-B | SANTA TEREZINHA | MATO GROSSO | Brasil | 5107776 | 51 | 33 | nan | nan | nan | Amazônia | nan |
| e0d02c06-e9f7-3f7b-865e-f6abf7ac779c | -2.3834 | -56.140701 | 2026-10-08 00:26:00 | METOP-B | JURUTI | PARÁ | Brasil | 1503903 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| 198f1a78-4e85-31a3-a98c-15f62b48d3e1 | -3.9123 | -55.883301 | 2026-10-08 00:26:00 | METOP-B | ITAITUBA | PARÁ | Brasil | 1503606 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| 120e3263-6c2a-3f58-9915-e0d283c47083 | -15.4194 | -43.709801 | 2026-10-08 00:26:00 | METOP-B | VERDELÂNDIA | MINAS GERAIS | Brasil | 3171030 | 31 | 33 | nan | nan | nan | Caatinga | nan |
| 628cb7b3-8924-38ad-961d-060b4769fbd7 | -4.9334 | -55.797901 | 2026-10-08 00:26:00 | METOP-B | TRAIRÃO | PARÁ | Brasil | 1508050 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| 56b64be3-253a-3e97-95a7-4ba7bd1c70a3 | -2.9457 | -54.067101 | 2026-10-08 00:26:00 | METOP-B | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| bf2ed249-f50c-37ca-96a9-2c01d8f705b4 | -3.2585 | -54.674 | 2026-10-08 00:26:00 | METOP-B | MOJUÍ DOS CAMPOS | PARÁ | Brasil | 1504752 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| 4854b648-2dd5-36a7-bc1e-0e956faec497 | -3.1063 | -53.775501 | 2026-10-08 00:26:00 | METOP-B | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| 8673660b-36a2-3404-970a-8f41bedd3593 | -7.2513 | -48.053101 | 2026-10-08 00:26:00 | METOP-B | BABAÇULÂNDIA | TOCANTINS | Brasil | 1703008 | 17 | 33 | nan | nan | nan | Cerrado | nan |
| 760e9c1e-82d1-3592-8c72-b2c31dde7995 | -3.2358 | -57.875599 | 2026-10-08 00:26:00 | METOP-B | BOA VISTA DO RAMOS | AMAZONAS | Brasil | 1300680 | 13 | 33 | nan | nan | nan | Amazônia | nan |
| cad7359b-74df-3d65-8d2d-b7e0f94a4e79 | -13.3089 | -48.679298 | 2026-10-08 00:26:00 | METOP-B | MONTIVIDIU DO NORTE | GOIÁS | Brasil | 5213772 | 52 | 33 | nan | nan | nan | Cerrado | nan |
| 137cd8b1-af5d-3471-9911-d02c6c9a5f7a | -3.5962 | -54.6633 | 2026-10-08 00:26:00 | METOP-B | PLACAS | PARÁ | Brasil | 1505650 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| 429004b0-9534-3cf4-b683-b773a7651f57 | -6.2251 | -52.8438 | 2026-10-08 00:26:00 | METOP-B | SÃO FÉLIX DO XINGU | PARÁ | Brasil | 1507300 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| b5f522f4-9298-381f-ab22-63e64c24ec26 | -1.5229 | -54.521801 | 2026-10-08 00:26:00 | METOP-B | ALENQUER | PARÁ | Brasil | 1500404 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| ea5c6be1-7bf2-3ec0-b8fb-6471ab76a88b | -2.7811 | -51.6731 | 2026-10-08 00:26:00 | METOP-B | ANAPU | PARÁ | Brasil | 1500859 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| 3ee2dd8a-5ac9-36cf-aab6-a3b67a0d8a58 | -3.0452 | -54.2332 | 2026-10-08 00:26:00 | METOP-B | SANTARÉM | PARÁ | Brasil | 1506807 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| 87c494f8-6c66-34ca-9e4f-05aa141570ef | -3.851 | -55.977798 | 2026-10-08 00:26:00 | METOP-B | AVEIRO | PARÁ | Brasil | 1501006 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| 797d050b-eaab-35c8-ad76-ccefc9e34e2f | -3.474 | -50.077202 | 2026-10-08 00:26:00 | METOP-B | PACAJÁ | PARÁ | Brasil | 1505486 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| d9a1000f-2997-3441-b087-80ede78f2ae7 | -6.2103 | -52.869499 | 2026-10-08 00:26:00 | METOP-B | SÃO FÉLIX DO XINGU | PARÁ | Brasil | 1507300 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| e65d61ab-a41a-3c54-aa26-3a1b817abf34 | -6.7336 | -55.097698 | 2026-10-08 00:26:00 | METOP-B | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| a9c18550-69d9-31f2-b326-778972ccf3e0 | -7.9042 | -54.7132 | 2026-10-08 00:26:00 | METOP-B | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| 8aeaf6b6-fe60-39b6-8acd-bb77f28ebb4f | -3.0128 | -54.0448 | 2026-10-08 00:26:00 | METOP-B | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| d257248c-9ce9-3f28-8849-e004bd655836 | -3.6664 | -60.605598 | 2026-10-08 00:26:00 | METOP-B | MANAQUIRI | AMAZONAS | Brasil | 1302553 | 13 | 33 | nan | nan | nan | Amazônia | nan |
| f7323a5c-63a9-3b84-92ec-18c1ccc4128d | -2.9578 | -54.166 | 2026-10-08 00:26:00 | METOP-B | SANTARÉM | PARÁ | Brasil | 1506807 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| 65da7435-fc45-3101-b9f1-82e5b65f420d | -16.7644 | -53.3731 | 2026-10-08 00:26:00 | METOP-B | ALTO GARÇAS | MATO GROSSO | Brasil | 5100409 | 51 | 33 | nan | nan | nan | Cerrado | nan |
| 3ac8c3de-f615-35dd-b192-bc50927c8a86 | -3.0218 | -53.9482 | 2026-10-08 00:26:00 | METOP-B | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| c461ddf2-9d57-3682-838f-681ad491ab54 | -3.9627 | -56.108501 | 2026-10-08 00:26:00 | METOP-B | ITAITUBA | PARÁ | Brasil | 1503606 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| 6e9cdf14-386d-3dd7-8b07-27a800da81f9 | -1.4852 | -54.537399 | 2026-10-08 00:26:00 | METOP-B | MONTE ALEGRE | PARÁ | Brasil | 1504802 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| 157d141b-dc4e-3942-b93b-b385d64a8868 | -3.6549 | -54.2845 | 2026-10-08 00:26:00 | METOP-B | PLACAS | PARÁ | Brasil | 1505650 | 15 | 33 | nan | nan | nan | Amazônia | nan |


[Clique aqui para ver as próximas entradas](README23.md)
