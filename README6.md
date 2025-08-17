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

## Dados Diários - Página 6

| ID | Latitude | Longitude | Data/Hora GMT | Satélite | Município | Estado | País | Município ID | Estado ID | País ID | Dias sem Chuva | Precipitação | Risco de Fogo | Bioma | FRP |
|----|----------|-----------|---------------|----------|-----------|--------|------|--------------|-----------|---------|----------------|--------------|----------------|-------|-----|
| 7c0b9b68-6f38-3d0a-aefb-e592b5e8752b | -10.8577 | -45.3088 | 2025-08-17 01:18:00 | METOP-C | FORMOSA DO RIO PRETO | BAHIA | Brasil | 2911105 | 29 | 33 | nan | nan | nan | Cerrado | nan |
| b7b0e0b2-5532-3bd2-9d25-360814f74881 | -9.5202 | -60.535 | 2025-08-17 01:18:00 | METOP-C | ARIPUANÃ | MATO GROSSO | Brasil | 5101407 | 51 | 33 | nan | nan | nan | Amazônia | nan |
| 22b6d3a0-7985-31d9-9fe1-5be5da6eb375 | -14.9818 | -54.751301 | 2025-08-17 01:18:00 | METOP-C | NOVA BRASILÂNDIA | MATO GROSSO | Brasil | 5106208 | 51 | 33 | nan | nan | nan | Cerrado | nan |
| 88a7591b-3211-34ec-8c0c-27aec6ec0b85 | -11.3688 | -55.382198 | 2025-08-17 01:18:00 | METOP-C | CLÁUDIA | MATO GROSSO | Brasil | 5103056 | 51 | 33 | nan | nan | nan | Amazônia | nan |
| ca8f69bd-984f-323a-a9b5-e6ad8ab9feda | -6.1367 | -57.935101 | 2025-08-17 01:18:00 | METOP-C | JACAREACANGA | PARÁ | Brasil | 1503754 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| 9bd1a15c-242b-3f40-a524-55bd41b1fb99 | -9.1234 | -61.492298 | 2025-08-17 01:18:00 | METOP-C | COLNIZA | MATO GROSSO | Brasil | 5103254 | 51 | 33 | nan | nan | nan | Amazônia | nan |
| 57d7a05d-216d-3e7d-99cb-2aca83f4b1a3 | -14.6414 | -54.887001 | 2025-08-17 01:18:00 | METOP-C | PLANALTO DA SERRA | MATO GROSSO | Brasil | 5106455 | 51 | 33 | nan | nan | nan | Cerrado | nan |
| 22408549-bcc0-3b49-8d57-d00bd2e6f4ca | -13.4353 | -45.873199 | 2025-08-17 01:18:00 | METOP-C | CORRENTINA | BAHIA | Brasil | 2909307 | 29 | 33 | nan | nan | nan | Cerrado | nan |
| 5ab801c8-7e90-3c93-9e91-0dcee1d7f14e | -10.8561 | -45.340698 | 2025-08-17 01:18:00 | METOP-C | FORMOSA DO RIO PRETO | BAHIA | Brasil | 2911105 | 29 | 33 | nan | nan | nan | Cerrado | nan |
| 9ace701a-a01d-3fb6-81e4-53fd67c1315f | -9.5043 | -60.556 | 2025-08-17 01:18:00 | METOP-C | ARIPUANÃ | MATO GROSSO | Brasil | 5101407 | 51 | 33 | nan | nan | nan | Amazônia | nan |
| 77bd771f-666d-377d-935e-8d129c40260e | -11.3692 | -55.428101 | 2025-08-17 01:18:00 | METOP-C | CLÁUDIA | MATO GROSSO | Brasil | 5103056 | 51 | 33 | nan | nan | nan | Amazônia | nan |
| 232707ae-517f-3e98-86f9-673898ff28df | -15.1909 | -48.762798 | 2025-08-17 01:18:00 | METOP-C | VILA PROPÍCIO | GOIÁS | Brasil | 5222302 | 52 | 33 | nan | nan | nan | Cerrado | nan |
| 5c11826d-3b4f-3253-8c3a-4e4de942be21 | -8.9954 | -61.7057 | 2025-08-17 01:18:00 | METOP-C | MACHADINHO D'OESTE | RONDÔNIA | Brasil | 1100130 | 11 | 33 | nan | nan | nan | Amazônia | nan |
| cd799b70-7a8d-3bd5-8931-91871af20347 | -9.164 | -59.617199 | 2025-08-17 01:18:00 | METOP-C | COLNIZA | MATO GROSSO | Brasil | 5103254 | 51 | 33 | nan | nan | nan | Amazônia | nan |
| f5d63c28-3444-3133-8e2d-f3be5f971cfb | 0.9611 | -60.404301 | 2025-08-17 01:18:00 | METOP-C | RORAINÓPOLIS | RORAIMA | Brasil | 1400472 | 14 | 33 | nan | nan | nan | Amazônia | nan |
| b48365f7-e6e9-3e8a-9966-d931627205b0 | -14.6333 | -54.896599 | 2025-08-17 01:18:00 | METOP-C | PLANALTO DA SERRA | MATO GROSSO | Brasil | 5106455 | 51 | 33 | nan | nan | nan | Cerrado | nan |
| e563086a-5b92-36a7-9f4b-951b75ae23b3 | -11.3756 | -55.411301 | 2025-08-17 01:18:00 | METOP-C | CLÁUDIA | MATO GROSSO | Brasil | 5103056 | 51 | 33 | nan | nan | nan | Amazônia | nan |
| f23c35f6-b299-3225-b3d5-debc12c4be21 | -14.7163 | -59.6661 | 2025-08-17 01:18:00 | METOP-C | NOVA LACERDA | MATO GROSSO | Brasil | 5106182 | 51 | 33 | nan | nan | nan | Amazônia | nan |
| 8184e779-42fc-3061-b515-7ff577949462 | -18.7724 | -45.105202 | 2025-08-17 01:18:00 | METOP-C | FELIXLÂNDIA | MINAS GERAIS | Brasil | 3125705 | 31 | 33 | nan | nan | nan | Cerrado | nan |
| f6a35309-9ee0-3029-83ce-acd87dd338dc | -8.9878 | -60.495399 | 2025-08-17 01:18:00 | METOP-C | COLNIZA | MATO GROSSO | Brasil | 5103254 | 51 | 33 | nan | nan | nan | Amazônia | nan |
| 20150b1c-f303-3d6f-b626-4d3281460e2e | -14.9437 | -54.675598 | 2025-08-17 01:18:00 | METOP-C | PRIMAVERA DO LESTE | MATO GROSSO | Brasil | 5107040 | 51 | 33 | nan | nan | nan | Cerrado | nan |
| e14136c9-f729-36ed-875c-3e83c6decb8f | -9.2198 | -59.6367 | 2025-08-17 01:18:00 | METOP-C | COLNIZA | MATO GROSSO | Brasil | 5103254 | 51 | 33 | nan | nan | nan | Amazônia | nan |
| bc3ba171-a492-3f54-b44f-657f9a83064b | -6.1465 | -57.932899 | 2025-08-17 01:18:00 | METOP-C | JACAREACANGA | PARÁ | Brasil | 1503754 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| b12b9e35-002a-3d93-981e-663e715789fe | -14.9916 | -54.748901 | 2025-08-17 01:18:00 | METOP-C | CAMPO VERDE | MATO GROSSO | Brasil | 5102678 | 51 | 33 | nan | nan | nan | Cerrado | nan |
| 5d597695-8c26-3cb8-a31a-0dc604ef1928 | -9.5141 | -60.553902 | 2025-08-17 01:18:00 | METOP-C | ARIPUANÃ | MATO GROSSO | Brasil | 5101407 | 51 | 33 | nan | nan | nan | Amazônia | nan |
| 6d9a7d77-d2bb-3f21-8ad8-18815637c840 | -14.972 | -54.753601 | 2025-08-17 01:18:00 | METOP-C | NOVA BRASILÂNDIA | MATO GROSSO | Brasil | 5106208 | 51 | 33 | nan | nan | nan | Cerrado | nan |
| 50fd1ce9-ef7c-390c-974c-f94da1dbef1e | -8.978 | -60.497501 | 2025-08-17 01:18:00 | METOP-C | COLNIZA | MATO GROSSO | Brasil | 5103254 | 51 | 33 | nan | nan | nan | Amazônia | nan |
| 364150fc-7c64-3963-b7ab-f364c94d4f42 | -14.947 | -54.6903 | 2025-08-17 01:18:00 | METOP-C | PRIMAVERA DO LESTE | MATO GROSSO | Brasil | 5107040 | 51 | 33 | nan | nan | nan | Cerrado | nan |
| 82a1e10f-5762-3886-8dd2-ac4d4bdb5f60 | -14.6448 | -54.901501 | 2025-08-17 01:18:00 | METOP-C | PLANALTO DA SERRA | MATO GROSSO | Brasil | 5106455 | 51 | 33 | nan | nan | nan | Cerrado | nan |
| 3111ee2c-1220-3989-ba96-70686262a284 | -11.3773 | -55.418499 | 2025-08-17 01:18:00 | METOP-C | CLÁUDIA | MATO GROSSO | Brasil | 5103056 | 51 | 33 | nan | nan | nan | Amazônia | nan |
| 5dfeef3c-1907-385a-af58-9679c4f0937f | -13.0047 | -56.851101 | 2025-08-17 01:18:00 | METOP-C | NOVA MARINGÁ | MATO GROSSO | Brasil | 5108907 | 51 | 33 | nan | nan | nan | Amazônia | nan |
| 80bc4d4d-24f0-3470-b4e2-99715c10daff | -10.3167 | -52.564701 | 2025-08-17 01:18:00 | METOP-C | SANTA CRUZ DO XINGU | MATO GROSSO | Brasil | 5107743 | 51 | 33 | nan | nan | nan | Amazônia | nan |
| aae2eeaf-c24e-3c17-a3c4-02fd0f3bbcfb | -10.3247 | -54.147999 | 2025-08-17 01:18:00 | METOP-C | PEIXOTO DE AZEVEDO | MATO GROSSO | Brasil | 5106422 | 51 | 33 | nan | nan | nan | Amazônia | nan |
| e0cd08c9-8490-32df-a3fe-6d8e8a77afe3 | -9.4994 | -60.5278 | 2025-08-17 01:20:00 | GOES-19 | ARIPUANÃ | MATO GROSSO | Brasil | 5101407 | 51 | 33 | nan | nan | nan | Amazônia | 45.6 |
| d68b288b-82e0-3cc9-9005-d45becda1529 | -13.0122 | -42.3321 | 2025-08-17 01:20:00 | GOES-19 | IBIPITANGA | BAHIA | Brasil | 2912509 | 29 | 33 | nan | nan | nan | Caatinga | 83.8 |
| e0d5a0ee-877e-36e7-ad2e-42bccde1d77c | -6.545 | -43.0373 | 2025-08-17 01:20:00 | GOES-19 | BARÃO DE GRAJAÚ | MARANHÃO | Brasil | 2101509 | 21 | 33 | nan | nan | nan | Cerrado | 114.9 |
| 75b57fdb-d37b-3414-9358-8c48e536e1aa | -18.7778 | -45.0818 | 2025-08-17 01:20:00 | GOES-19 | FELIXLÂNDIA | MINAS GERAIS | Brasil | 3125705 | 31 | 33 | nan | nan | nan | Cerrado | 130.3 |
| 6aa7b62d-cd8f-3475-b79e-8677576b05c3 | -13.4421 | -45.8898 | 2025-08-17 01:20:00 | GOES-19 | CORRENTINA | BAHIA | Brasil | 2909307 | 29 | 33 | nan | nan | nan | Cerrado | 40.6 |
| 8e90d994-cd39-3a9f-a3ef-3a49adfcd842 | -6.5453 | -43.0138 | 2025-08-17 01:20:00 | GOES-19 | BARÃO DE GRAJAÚ | MARANHÃO | Brasil | 2101509 | 21 | 33 | nan | nan | nan | Cerrado | 79.4 |
| ee5312de-9c23-31c3-b13f-db93fc918675 | -10.8444 | -45.3126 | 2025-08-17 01:20:00 | GOES-19 | FORMOSA DO RIO PRETO | BAHIA | Brasil | 2911105 | 29 | 33 | nan | nan | nan | Cerrado | 103.3 |
| b052e6db-c6ac-3d4f-84c4-15293787be33 | -9.1895 | -59.6364 | 2025-08-17 01:20:00 | GOES-19 | COLNIZA | MATO GROSSO | Brasil | 5103254 | 51 | 33 | nan | nan | nan | Amazônia | 57.8 |
| 95210a5e-81d7-3fe6-b1f6-61387401cd84 | -10.8253 | -45.3152 | 2025-08-17 01:20:00 | GOES-19 | FORMOSA DO RIO PRETO | BAHIA | Brasil | 2911105 | 29 | 33 | nan | nan | nan | Cerrado | 51.4 |
| 9233e7c8-170c-331f-8d96-f85817eabec5 | -18.7771 | -45.1059 | 2025-08-17 01:20:00 | GOES-19 | FELIXLÂNDIA | MINAS GERAIS | Brasil | 3125705 | 31 | 33 | nan | nan | nan | Cerrado | 62.3 |
| aa17760f-67e8-33ac-ad66-e907acbbefd5 | -9.5179 | -60.5461 | 2025-08-17 01:20:00 | GOES-19 | ARIPUANÃ | MATO GROSSO | Brasil | 5101407 | 51 | 33 | nan | nan | nan | Amazônia | 47.2 |
| 14935fc1-32b1-327a-878d-33e1cea3d52c | -9.2082 | -59.6354 | 2025-08-17 01:20:00 | GOES-19 | COLNIZA | MATO GROSSO | Brasil | 5103254 | 51 | 33 | nan | nan | nan | Amazônia | 48.6 |
| 61e30cd7-955d-3786-85eb-05c481632141 | -18.7569 | -45.1107 | 2025-08-17 01:20:00 | GOES-19 | FELIXLÂNDIA | MINAS GERAIS | Brasil | 3125705 | 31 | 33 | nan | nan | nan | Cerrado | 65.0 |
| 01db0727-bd94-3459-9483-fb3a46d79e23 | -9.1894 | -59.6558 | 2025-08-17 01:20:00 | GOES-19 | COLNIZA | MATO GROSSO | Brasil | 5103254 | 51 | 33 | nan | nan | nan | Amazônia | 53.5 |
| f1efa2f7-ab86-3efa-b1d0-4570a29b9b0a | -8.9787 | -60.5156 | 2025-08-17 01:20:00 | GOES-19 | COLNIZA | MATO GROSSO | Brasil | 5103254 | 51 | 33 | nan | nan | nan | Amazônia | 46.5 |
| c323955d-b2a5-3112-8afd-146b94db540b | -18.7575 | -45.0866 | 2025-08-17 01:20:00 | GOES-19 | FELIXLÂNDIA | MINAS GERAIS | Brasil | 3125705 | 31 | 33 | nan | nan | nan | Cerrado | 171.3 |
| 2c06089a-d2b0-3af5-a071-08a8754d446e | -4.9305 | -43.2558 | 2025-08-17 01:20:00 | GOES-19 | CAXIAS | MARANHÃO | Brasil | 2103000 | 21 | 33 | nan | nan | nan | Cerrado | 91.1 |
| df9e0e13-4f57-385b-a0f8-8a39f22f9325 | -8.9974 | -60.4955 | 2025-08-17 01:20:00 | GOES-19 | COLNIZA | MATO GROSSO | Brasil | 5103254 | 51 | 33 | nan | nan | nan | Amazônia | 49.6 |
| 27b18336-0090-37cc-8bef-b34ad404f5f6 | -4.9118 | -43.257 | 2025-08-17 01:20:00 | GOES-19 | CAXIAS | MARANHÃO | Brasil | 2103000 | 21 | 33 | nan | nan | nan | Cerrado | 99.5 |
| e6fb2b3e-f501-384f-9ffd-5645544f73ec | -8.9788 | -60.4964 | 2025-08-17 01:20:00 | GOES-19 | COLNIZA | MATO GROSSO | Brasil | 5103254 | 51 | 33 | nan | nan | nan | Amazônia | 86.8 |
| 1f38392f-56fb-3905-b0ef-320b1e3a71d7 | -9.518 | -60.5268 | 2025-08-17 01:20:00 | GOES-19 | ARIPUANÃ | MATO GROSSO | Brasil | 5101407 | 51 | 33 | nan | nan | nan | Amazônia | 57.0 |
| f962718b-dbdf-3dfb-a67c-4a352ca08e4a | -9.1895 | -59.6364 | 2025-08-17 01:30:00 | GOES-19 | COLNIZA | MATO GROSSO | Brasil | 5103254 | 51 | 33 | nan | nan | nan | Amazônia | 58.8 |
| 93ccbd59-40cf-33e4-a00c-bb737b488492 | -9.5179 | -60.5461 | 2025-08-17 01:30:00 | GOES-19 | ARIPUANÃ | MATO GROSSO | Brasil | 5101407 | 51 | 33 | nan | nan | nan | Amazônia | 63.7 |
| e9972e35-5e2a-3b37-b12c-fbdbce458211 | -4.9118 | -43.257 | 2025-08-17 01:30:00 | GOES-19 | CAXIAS | MARANHÃO | Brasil | 2103000 | 21 | 33 | nan | nan | nan | Cerrado | 74.1 |
| 29372ada-e015-3eff-8c11-656207297828 | -15.1873 | -48.7671 | 2025-08-17 01:30:00 | GOES-19 | VILA PROPÍCIO | GOIÁS | Brasil | 5222302 | 52 | 33 | nan | nan | nan | Cerrado | 90.6 |
| 6d3df3bc-dc10-3e01-b60e-1e904b9fb871 | -9.1709 | -59.6374 | 2025-08-17 01:30:00 | GOES-19 | COLNIZA | MATO GROSSO | Brasil | 5103254 | 51 | 33 | nan | nan | nan | Amazônia | 46.8 |
| 92ef55c3-1587-3ebf-b2ac-b3c72c7d1020 | -9.4992 | -60.547 | 2025-08-17 01:30:00 | GOES-19 | ARIPUANÃ | MATO GROSSO | Brasil | 5101407 | 51 | 33 | nan | nan | nan | Amazônia | 47.2 |
| e5e4b2da-ff8d-37c1-86ea-727b65f6280a | -10.844 | -45.3356 | 2025-08-17 01:30:00 | GOES-19 | FORMOSA DO RIO PRETO | BAHIA | Brasil | 2911105 | 29 | 33 | nan | nan | nan | Cerrado | 68.7 |
| 0e4eacfa-3556-31b5-8468-bfa1cbe51332 | -8.9893 | -61.7024 | 2025-08-17 01:30:00 | GOES-19 | MACHADINHO D'OESTE | RONDÔNIA | Brasil | 1100130 | 11 | 33 | nan | nan | nan | Amazônia | 45.2 |
| 872ad913-4996-3dec-a42d-34de6b110e88 | -13.0128 | -42.3077 | 2025-08-17 01:30:00 | GOES-19 | IBIPITANGA | BAHIA | Brasil | 2912509 | 29 | 33 | nan | nan | nan | Caatinga | 73.8 |
| ddce3730-7b71-3a0b-8a4d-3f6c883ea6ee | -18.7778 | -45.0818 | 2025-08-17 01:30:00 | GOES-19 | FELIXLÂNDIA | MINAS GERAIS | Brasil | 3125705 | 31 | 33 | nan | nan | nan | Cerrado | 87.9 |
| 7afd80a2-0c44-3af7-8f54-019a831c5935 | -10.8253 | -45.3152 | 2025-08-17 01:30:00 | GOES-19 | FORMOSA DO RIO PRETO | BAHIA | Brasil | 2911105 | 29 | 33 | nan | nan | nan | Cerrado | 76.5 |
| c28e8ef0-fe67-33e5-82ae-1404724519eb | -8.9709 | -61.6842 | 2025-08-17 01:30:00 | GOES-19 | MACHADINHO D'OESTE | RONDÔNIA | Brasil | 1100130 | 11 | 33 | nan | nan | nan | Amazônia | 44.5 |
| 193f029e-8482-31b5-b091-0abab4a9108d | -10.8249 | -45.3382 | 2025-08-17 01:30:00 | GOES-19 | FORMOSA DO RIO PRETO | BAHIA | Brasil | 2911105 | 29 | 33 | nan | nan | nan | Cerrado | 57.3 |
| f7751b75-a73c-31b2-84ff-1c370d017b26 | -9.518 | -60.5268 | 2025-08-17 01:30:00 | GOES-19 | ARIPUANÃ | MATO GROSSO | Brasil | 5101407 | 51 | 33 | nan | nan | nan | Amazônia | 62.1 |
| ae387460-7ae7-3ca9-810d-392738d47018 | -18.7575 | -45.0866 | 2025-08-17 01:30:00 | GOES-19 | FELIXLÂNDIA | MINAS GERAIS | Brasil | 3125705 | 31 | 33 | nan | nan | nan | Cerrado | 123.6 |
| c6c9fbaa-3d02-3ad8-828e-d004aec9ea5b | -10.8444 | -45.3126 | 2025-08-17 01:30:00 | GOES-19 | FORMOSA DO RIO PRETO | BAHIA | Brasil | 2911105 | 29 | 33 | nan | nan | nan | Cerrado | 133.4 |
| 475e22ca-e370-35d4-8951-c9f177640a92 | -9.1894 | -59.6558 | 2025-08-17 01:30:00 | GOES-19 | COLNIZA | MATO GROSSO | Brasil | 5103254 | 51 | 33 | nan | nan | nan | Amazônia | 48.9 |
| daa6c3db-96d2-3654-bd9e-da1579ba73f7 | -4.9305 | -43.2558 | 2025-08-17 01:30:00 | GOES-19 | CAXIAS | MARANHÃO | Brasil | 2103000 | 21 | 33 | nan | nan | nan | Cerrado | 104.3 |
| 03a25e61-6077-347b-9125-9e00ed406e75 | -14.0406 | -58.8661 | 2025-08-17 01:30:00 | GOES-19 | TANGARÁ DA SERRA | MATO GROSSO | Brasil | 5107958 | 51 | 33 | nan | nan | nan | Cerrado | 39.4 |
| 71efb1fc-9e29-3801-a41e-080129fc581c | -8.9788 | -60.4964 | 2025-08-17 01:30:00 | GOES-19 | COLNIZA | MATO GROSSO | Brasil | 5103254 | 51 | 33 | nan | nan | nan | Amazônia | 60.7 |
| 87684749-ee3d-3223-95be-20ae66d4019e | -13.0122 | -42.3321 | 2025-08-17 01:30:00 | GOES-19 | IBIPITANGA | BAHIA | Brasil | 2912509 | 29 | 33 | nan | nan | nan | Caatinga | 117.1 |
| d7be2c3a-83f7-3649-9235-5e9e6832d1c1 | -9.1708 | -59.6568 | 2025-08-17 01:30:00 | GOES-19 | COLNIZA | MATO GROSSO | Brasil | 5103254 | 51 | 33 | nan | nan | nan | Amazônia | 44.3 |
| f3faff25-0e58-32db-a60b-00c994ad46a9 | -6.545 | -43.0373 | 2025-08-17 01:30:00 | GOES-19 | BARÃO DE GRAJAÚ | MARANHÃO | Brasil | 2101509 | 21 | 33 | nan | nan | nan | Cerrado | 96.6 |
| cc929554-da7f-3a12-9640-60796a754122 | -15.1869 | -48.7894 | 2025-08-17 01:30:00 | GOES-19 | VILA PROPÍCIO | GOIÁS | Brasil | 5222302 | 52 | 33 | nan | nan | nan | Cerrado | 94.6 |
| f87c6b9c-cc5f-3766-85e1-c1205c8bb776 | -18.7569 | -45.1107 | 2025-08-17 01:40:00 | GOES-19 | FELIXLÂNDIA | MINAS GERAIS | Brasil | 3125705 | 31 | 33 | nan | nan | nan | Cerrado | 72.2 |
| dabe18b7-a990-3a1f-a890-3d6d6a79e3c8 | -10.8444 | -45.3126 | 2025-08-17 01:40:00 | GOES-19 | FORMOSA DO RIO PRETO | BAHIA | Brasil | 2911105 | 29 | 33 | nan | nan | nan | Cerrado | 112.7 |
| 0782f7e0-e787-3e2b-b32d-fe3f7b96b031 | -9.2082 | -59.6354 | 2025-08-17 01:40:00 | GOES-19 | COLNIZA | MATO GROSSO | Brasil | 5103254 | 51 | 33 | nan | nan | nan | Amazônia | 42.8 |
| 240a1cc3-7bc4-3204-aefc-a55d9a314f6a | -13.0122 | -42.3321 | 2025-08-17 01:40:00 | GOES-19 | IBIPITANGA | BAHIA | Brasil | 2912509 | 29 | 33 | nan | nan | nan | Caatinga | 114.3 |
| f70d427c-578e-3fbc-8d69-8d292c5bcf0c | -18.7778 | -45.0818 | 2025-08-17 01:40:00 | GOES-19 | FELIXLÂNDIA | MINAS GERAIS | Brasil | 3125705 | 31 | 33 | nan | nan | nan | Cerrado | 120.1 |
| fc754e3d-60bd-3a0e-8a9b-503ded50a3c5 | -9.5179 | -60.5461 | 2025-08-17 01:40:00 | GOES-19 | ARIPUANÃ | MATO GROSSO | Brasil | 5101407 | 51 | 33 | nan | nan | nan | Amazônia | 53.3 |
| 598198c8-c712-3f2f-9d25-400c65f0d0b9 | -9.4992 | -60.547 | 2025-08-17 01:40:00 | GOES-19 | ARIPUANÃ | MATO GROSSO | Brasil | 5101407 | 51 | 33 | nan | nan | nan | Amazônia | 44.5 |
| b7339f59-3604-3bc4-891e-090bc6eeaf68 | -9.4994 | -60.5278 | 2025-08-17 01:40:00 | GOES-19 | ARIPUANÃ | MATO GROSSO | Brasil | 5101407 | 51 | 33 | nan | nan | nan | Amazônia | 45.5 |
| f0604fe0-f35a-3ba2-8ef8-1769c0b962e9 | -8.9974 | -60.4955 | 2025-08-17 01:40:00 | GOES-19 | COLNIZA | MATO GROSSO | Brasil | 5103254 | 51 | 33 | nan | nan | nan | Amazônia | 51.6 |
| 750c0f2c-2980-36ea-8a84-9605698276d2 | -9.1894 | -59.6558 | 2025-08-17 01:40:00 | GOES-19 | COLNIZA | MATO GROSSO | Brasil | 5103254 | 51 | 33 | nan | nan | nan | Amazônia | 51.2 |
| d146acff-2049-32bc-bbf0-2ceceeaa4511 | -9.1895 | -59.6364 | 2025-08-17 01:40:00 | GOES-19 | COLNIZA | MATO GROSSO | Brasil | 5103254 | 51 | 33 | nan | nan | nan | Amazônia | 46.6 |
| 9da733d9-8ba3-3ac2-8e01-15c9dffee32f | -12.898 | -46.1135 | 2025-08-17 01:40:00 | GOES-19 | SÃO DESIDÉRIO | BAHIA | Brasil | 2928901 | 29 | 33 | nan | nan | nan | Cerrado | 57.4 |
| 3e68c96e-f2db-3d8f-afe4-7021ba473610 | -10.8253 | -45.3152 | 2025-08-17 01:40:00 | GOES-19 | FORMOSA DO RIO PRETO | BAHIA | Brasil | 2911105 | 29 | 33 | nan | nan | nan | Cerrado | 63.6 |
| c2a2f93d-99b0-35ad-bdf9-769fa8bbcd60 | -6.545 | -43.0373 | 2025-08-17 01:40:00 | GOES-19 | BARÃO DE GRAJAÚ | MARANHÃO | Brasil | 2101509 | 21 | 33 | nan | nan | nan | Cerrado | 95.2 |
| 9b353ddb-6c35-3451-bfda-78c6b53afe8c | -6.5453 | -43.0138 | 2025-08-17 01:40:00 | GOES-19 | BARÃO DE GRAJAÚ | MARANHÃO | Brasil | 2101509 | 21 | 33 | nan | nan | nan | Cerrado | 78.3 |
| 47e5daec-46e2-304d-8ca8-2ddade43b5a5 | -13.0128 | -42.3077 | 2025-08-17 01:40:00 | GOES-19 | IBIPITANGA | BAHIA | Brasil | 2912509 | 29 | 33 | nan | nan | nan | Caatinga | 66.2 |
| 04de9aad-3b3a-36bb-9438-b757687bdb70 | -18.7771 | -45.1059 | 2025-08-17 01:40:00 | GOES-19 | FELIXLÂNDIA | MINAS GERAIS | Brasil | 3125705 | 31 | 33 | nan | nan | nan | Cerrado | 118.9 |
| 791958c4-0089-3b01-8aba-f97d287d53ae | -18.7575 | -45.0866 | 2025-08-17 01:40:00 | GOES-19 | FELIXLÂNDIA | MINAS GERAIS | Brasil | 3125705 | 31 | 33 | nan | nan | nan | Cerrado | 82.8 |
| e3b2d28c-a965-3cee-9147-20d23be0d740 | -8.9788 | -60.4964 | 2025-08-17 01:40:00 | GOES-19 | COLNIZA | MATO GROSSO | Brasil | 5103254 | 51 | 33 | nan | nan | nan | Amazônia | 76.1 |
| 9b08c086-c13a-3d11-91a3-b71c254d5b48 | -9.518 | -60.5268 | 2025-08-17 01:40:00 | GOES-19 | ARIPUANÃ | MATO GROSSO | Brasil | 5101407 | 51 | 33 | nan | nan | nan | Amazônia | 59.7 |
| b0891a8f-e212-376f-a253-97fe6b321371 | -13.0317 | -42.3285 | 2025-08-17 01:40:00 | GOES-19 | IBIPITANGA | BAHIA | Brasil | 2912509 | 29 | 33 | nan | nan | nan | Caatinga | 93.3 |
| df15e065-21df-3251-a315-7bae0a4ba7f1 | -13.4421 | -45.8898 | 2025-08-17 01:40:00 | GOES-19 | CORRENTINA | BAHIA | Brasil | 2909307 | 29 | 33 | nan | nan | nan | Cerrado | 44.7 |


[Clique aqui para ver as próximas entradas](README7.md)
