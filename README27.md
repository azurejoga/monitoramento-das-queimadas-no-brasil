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

## Dados Diários - Página 27

| ID | Latitude | Longitude | Data/Hora GMT | Satélite | Município | Estado | País | Município ID | Estado ID | País ID | Dias sem Chuva | Precipitação | Risco de Fogo | Bioma | FRP |
|----|----------|-----------|---------------|----------|-----------|--------|------|--------------|-----------|---------|----------------|--------------|----------------|-------|-----|
| 1a206a82-1620-3a1b-8e4c-941458bcebb9 | -3.78849 | -43.90955 | 2024-11-16 04:23:00 | NPP-375D | VARGEM GRANDE | MARANHÃO | Brasil | 2112704 | 21 | 33 | nan | nan | nan | Cerrado | 8.3 |
| a4671a37-41a1-340f-bc5d-ebbf46a1737c | -2.50311 | -46.35608 | 2024-11-16 04:23:00 | NPP-375D | CENTRO NOVO DO MARANHÃO | MARANHÃO | Brasil | 2103174 | 21 | 33 | nan | nan | nan | Amazônia | 1.1 |
| c2ccda82-1d7d-348b-ba4f-62772237eb51 | -2.54739 | -46.89169 | 2024-11-16 04:23:00 | NPP-375D | PARAGOMINAS | PARÁ | Brasil | 1505502 | 15 | 33 | nan | nan | nan | Amazônia | 5.1 |
| ae18117d-e748-3d68-827a-2a81864cc195 | -5.67072 | -35.64777 | 2024-11-16 04:23:00 | NPP-375D | POÇO BRANCO | RIO GRANDE DO NORTE | Brasil | 2410108 | 24 | 33 | nan | nan | nan | Caatinga | 17.6 |
| 502fce67-5abe-33da-ac28-68517ea2971b | -3.0127 | -47.96646 | 2024-11-16 04:23:00 | NPP-375D | IPIXUNA DO PARÁ | PARÁ | Brasil | 1503457 | 15 | 33 | nan | nan | nan | Amazônia | 1.4 |
| 6638e646-87ae-3d31-b356-7d0c0f6797c0 | -2.14623 | -46.80329 | 2024-11-16 04:23:00 | NPP-375D | NOVA ESPERANÇA DO PIRIÁ | PARÁ | Brasil | 1504950 | 15 | 33 | nan | nan | nan | Amazônia | 1.4 |
| 8cd24154-e177-313c-934d-b1738cdf195f | -3.85599 | -46.65773 | 2024-11-16 04:23:00 | NPP-375D | BOM JARDIM | MARANHÃO | Brasil | 2102002 | 21 | 33 | nan | nan | nan | Amazônia | 0.9 |
| eb79f971-5d5c-34c4-8f09-e67ffa376af9 | -2.46283 | -46.37156 | 2024-11-16 04:23:00 | NPP-375D | CENTRO NOVO DO MARANHÃO | MARANHÃO | Brasil | 2103174 | 21 | 33 | nan | nan | nan | Amazônia | 1.0 |
| e6d83a7a-8f17-3dc8-a134-4f511bfa7114 | -2.9432 | -48.01603 | 2024-11-16 04:23:00 | NPP-375D | IPIXUNA DO PARÁ | PARÁ | Brasil | 1503457 | 15 | 33 | nan | nan | nan | Amazônia | 1.2 |
| b593d845-ecbf-383b-ad4c-3b16a81dfd8a | -1.69184 | -54.26378 | 2024-11-16 04:23:00 | NPP-375D | MONTE ALEGRE | PARÁ | Brasil | 1504802 | 15 | 33 | nan | nan | nan | Amazônia | 1.0 |
| 81acaa5e-2549-3211-875e-084bb159639b | -3.32252 | -51.66256 | 2024-11-16 04:23:00 | NPP-375D | ANAPU | PARÁ | Brasil | 1500859 | 15 | 33 | nan | nan | nan | Amazônia | 2.0 |
| cca4ef53-a3e5-3d8a-8082-940ac9630be8 | -3.68578 | -40.77397 | 2024-11-16 04:23:00 | NPP-375D | COREAÚ | CEARÁ | Brasil | 2304004 | 23 | 33 | nan | nan | nan | Caatinga | 1.0 |
| e026e592-cb73-38db-b757-bf01f25afab8 | -2.77445 | -48.57611 | 2024-11-16 04:23:00 | NPP-375D | TAILÂNDIA | PARÁ | Brasil | 1507953 | 15 | 33 | nan | nan | nan | Amazônia | 13.3 |
| 42730413-9a33-3046-8add-4c601d6f4b48 | -1.73648 | -46.72149 | 2024-11-16 04:23:00 | NPP-375D | VISEU | PARÁ | Brasil | 1508308 | 15 | 33 | nan | nan | nan | Amazônia | 1.1 |
| a682b29a-1526-3e96-864b-db79531652ef | -3.07344 | -48.01546 | 2024-11-16 04:23:00 | NPP-375D | IPIXUNA DO PARÁ | PARÁ | Brasil | 1503457 | 15 | 33 | nan | nan | nan | Amazônia | 2.6 |
| ee93d4d0-dcc5-3038-a741-4cbe19bad741 | -2.5732 | -54.4297 | 2024-11-16 04:23:00 | NPP-375D | SANTARÉM | PARÁ | Brasil | 1506807 | 15 | 33 | nan | nan | nan | Amazônia | 6.2 |
| a7f991bf-630a-3aa8-b7c2-703743c0465d | -3.98297 | -43.71346 | 2024-11-16 04:23:00 | NPP-375D | TIMBIRAS | MARANHÃO | Brasil | 2112100 | 21 | 33 | nan | nan | nan | Cerrado | 3.2 |
| 11c67614-1da3-3594-bfc2-46cec0ebce75 | -3.04034 | -47.9738 | 2024-11-16 04:23:00 | NPP-375D | IPIXUNA DO PARÁ | PARÁ | Brasil | 1503457 | 15 | 33 | nan | nan | nan | Amazônia | 0.9 |
| 6ebcff40-99aa-330c-ad00-1ba47ce9f899 | -2.65964 | -46.20077 | 2024-11-16 04:23:00 | NPP-375D | CENTRO NOVO DO MARANHÃO | MARANHÃO | Brasil | 2103174 | 21 | 33 | nan | nan | nan | Amazônia | 1.7 |
| d23f4fbf-107f-38ae-84a9-0b37640436a4 | -2.02611 | -53.94445 | 2024-11-16 04:23:00 | NPP-375D | PRAINHA | PARÁ | Brasil | 1506005 | 15 | 33 | nan | nan | nan | Amazônia | 6.4 |
| c7ed2a22-cbdc-307d-a3e9-4c825db7c934 | -3.87935 | -44.09013 | 2024-11-16 04:23:00 | NPP-375D | COROATÁ | MARANHÃO | Brasil | 2103604 | 21 | 33 | nan | nan | nan | Cerrado | 2.8 |
| 08b3442c-1c9c-3618-99eb-42aa34b33dbe | -2.13484 | -48.77903 | 2024-11-16 04:23:00 | NPP-375D | MOJU | PARÁ | Brasil | 1504703 | 15 | 33 | nan | nan | nan | Amazônia | 17.6 |
| 537b64ca-dc82-383b-9c6b-f2c4f96089c7 | -2.17839 | -48.75324 | 2024-11-16 04:23:00 | NPP-375D | MOJU | PARÁ | Brasil | 1504703 | 15 | 33 | nan | nan | nan | Amazônia | 1.3 |
| f8f98127-7613-3628-b8dc-4dbd8a42620f | -3.74313 | -45.65582 | 2024-11-16 04:23:00 | NPP-375D | TUFILÂNDIA | MARANHÃO | Brasil | 2112274 | 21 | 33 | nan | nan | nan | Amazônia | 4.1 |
| 0d64b50a-7437-3997-8b3e-0d423a39826f | -2.85333 | -46.66191 | 2024-11-16 04:23:00 | NPP-375D | PARAGOMINAS | PARÁ | Brasil | 1505502 | 15 | 33 | nan | nan | nan | Amazônia | 1.2 |
| 1c4dae6f-51a3-3c2a-a47d-771275aed848 | -4.53663 | -43.56205 | 2024-11-16 04:23:00 | NPP-375D | ALDEIAS ALTAS | MARANHÃO | Brasil | 2100303 | 21 | 33 | nan | nan | nan | Cerrado | 2.0 |
| f1a374de-14fa-3991-87b2-a876e85051e3 | -4.75087 | -42.55008 | 2024-11-16 04:23:00 | NPP-375D | JOSÉ DE FREITAS | PIAUÍ | Brasil | 2205508 | 22 | 33 | nan | nan | nan | Caatinga | 1.1 |
| 8937cb72-5c7a-3041-a362-be7c61a352e7 | -4.81281 | -42.91999 | 2024-11-16 04:23:00 | NPP-375D | UNIÃO | PIAUÍ | Brasil | 2211100 | 22 | 33 | nan | nan | nan | Cerrado | 4.6 |
| d9075fee-0040-3cc3-80a2-ee7a4d29d81f | -1.24843 | -47.46998 | 2024-11-16 04:23:00 | NPP-375D | NOVA TIMBOTEUA | PARÁ | Brasil | 1505007 | 15 | 33 | nan | nan | nan | Amazônia | 0.8 |
| dd34ad8e-4ab6-341f-b27e-41e451da709e | -5.24053 | -44.91516 | 2024-11-16 04:23:00 | NPP-375D | BARRA DO CORDA | MARANHÃO | Brasil | 2101608 | 21 | 33 | nan | nan | nan | Cerrado | 5.0 |
| e0ba4903-efea-35e2-acd5-6bf1b8eaa39b | -3.52228 | -44.71716 | 2024-11-16 04:23:00 | NPP-375D | ARARI | MARANHÃO | Brasil | 2101004 | 21 | 33 | nan | nan | nan | Amazônia | 11.4 |
| 869e13db-cc6b-3356-9314-35b5a0e658c2 | -1.69507 | -47.97436 | 2024-11-16 04:23:00 | NPP-375D | BUJARU | PARÁ | Brasil | 1501907 | 15 | 33 | nan | nan | nan | Amazônia | 0.6 |
| cf649ea1-83eb-3053-a2b9-9167d8a3499f | -2.6663 | -46.18026 | 2024-11-16 04:23:00 | NPP-375D | CENTRO DO GUILHERME | MARANHÃO | Brasil | 2103158 | 21 | 33 | nan | nan | nan | Amazônia | 4.4 |
| ff200427-6523-32e4-a5f2-72b5fe17c3ca | -4.99554 | -44.31903 | 2024-11-16 04:23:00 | NPP-375D | DOM PEDRO | MARANHÃO | Brasil | 2103802 | 21 | 33 | nan | nan | nan | Cerrado | 3.6 |
| 31059e9f-81ed-3292-acb5-346b94be7c9b | -2.64318 | -46.53452 | 2024-11-16 04:23:00 | NPP-375D | CENTRO NOVO DO MARANHÃO | MARANHÃO | Brasil | 2103174 | 21 | 33 | nan | nan | nan | Amazônia | 0.6 |
| 802b63b8-d507-3557-84d9-3075970c9eee | -2.64096 | -45.97251 | 2024-11-16 04:23:00 | NPP-375D | SANTA LUZIA DO PARUÁ | MARANHÃO | Brasil | 2110039 | 21 | 33 | nan | nan | nan | Amazônia | 0.9 |
| d119f8df-46cc-3945-ada8-929784245508 | -1.85852 | -54.28333 | 2024-11-16 04:23:00 | NPP-375D | MONTE ALEGRE | PARÁ | Brasil | 1504802 | 15 | 33 | nan | nan | nan | Amazônia | 1.5 |
| ee3d0e57-6361-371b-81e2-ca86f46a1878 | -4.10361 | -46.88627 | 2024-11-16 04:23:00 | NPP-375D | BOM JARDIM | MARANHÃO | Brasil | 2102002 | 21 | 33 | nan | nan | nan | Amazônia | 1.6 |
| 5cc0a0c6-8f74-3d9b-b90d-6ee7ec562f16 | -5.15665 | -44.08926 | 2024-11-16 04:23:00 | NPP-375D | GONÇALVES DIAS | MARANHÃO | Brasil | 2104404 | 21 | 33 | nan | nan | nan | Cerrado | 9.4 |
| f22abf0f-e8b1-3ccd-a4c8-cd6999fe0a8d | -2.64845 | -46.16312 | 2024-11-16 04:23:00 | NPP-375D | CENTRO DO GUILHERME | MARANHÃO | Brasil | 2103158 | 21 | 33 | nan | nan | nan | Amazônia | 1.7 |
| c830e58c-f299-3e32-a59b-cfd3c060687c | -1.58391 | -50.44661 | 2024-11-16 04:23:00 | NPP-375D | BREVES | PARÁ | Brasil | 1501808 | 15 | 33 | nan | nan | nan | Amazônia | 1.8 |
| 5a854c97-5e4d-3b42-9d6a-9ccb07cba80c | -4.90716 | -44.03325 | 2024-11-16 04:23:00 | NPP-375D | CODÓ | MARANHÃO | Brasil | 2103307 | 21 | 33 | nan | nan | nan | Cerrado | 3.2 |
| ec367367-32f6-32a7-b3ae-702da915dc5d | -2.78106 | -48.58149 | 2024-11-16 04:23:00 | NPP-375D | TAILÂNDIA | PARÁ | Brasil | 1507953 | 15 | 33 | nan | nan | nan | Amazônia | 19.9 |
| 6766e658-450b-38b0-8cb5-947e37033cf5 | -2.64738 | -46.19165 | 2024-11-16 04:23:00 | NPP-375D | CENTRO DO GUILHERME | MARANHÃO | Brasil | 2103158 | 21 | 33 | nan | nan | nan | Amazônia | 0.9 |
| ae518ed6-8ae8-34eb-a7ce-a2f0be817822 | -1.95849 | -47.83732 | 2024-11-16 04:23:00 | NPP-375D | SÃO DOMINGOS DO CAPIM | PARÁ | Brasil | 1507201 | 15 | 33 | nan | nan | nan | Amazônia | 1.0 |
| bc5066ac-8930-32ca-aae2-7253e1f04eb9 | -2.65909 | -46.20428 | 2024-11-16 04:23:00 | NPP-375D | CENTRO NOVO DO MARANHÃO | MARANHÃO | Brasil | 2103174 | 21 | 33 | nan | nan | nan | Amazônia | 1.7 |
| 971a8645-d655-349b-8bce-171e513c91c8 | -3.23858 | -41.37996 | 2024-11-16 04:23:00 | NPP-375D | LUÍS CORREIA | PIAUÍ | Brasil | 2205706 | 22 | 33 | nan | nan | nan | Caatinga | 3.6 |
| 864af3b9-02c5-3b26-99f2-e81555b89a6b | -5.22606 | -40.59033 | 2024-11-16 04:23:00 | NPP-375D | CRATEÚS | CEARÁ | Brasil | 2304103 | 23 | 33 | nan | nan | nan | Caatinga | 1.1 |
| 1d4dd0fa-d838-3c2d-bfce-97caa7b63931 | -2.13368 | -48.12228 | 2024-11-16 04:23:00 | NPP-375D | TOMÉ-AÇU | PARÁ | Brasil | 1508001 | 15 | 33 | nan | nan | nan | Amazônia | 0.7 |
| a0f2554d-78d9-398f-b58c-e51c74bf84aa | -3.03139 | -47.98552 | 2024-11-16 04:23:00 | NPP-375D | IPIXUNA DO PARÁ | PARÁ | Brasil | 1503457 | 15 | 33 | nan | nan | nan | Amazônia | 1.4 |
| f043f22a-2221-34e5-8274-0b68be31265b | -3.56389 | -47.37506 | 2024-11-16 04:23:00 | NPP-375D | ULIANÓPOLIS | PARÁ | Brasil | 1508126 | 15 | 33 | nan | nan | nan | Amazônia | 1.7 |
| 20cbbcfb-0bff-3f80-b883-02ac4476660a | -3.73269 | -45.66135 | 2024-11-16 04:23:00 | NPP-375D | ALTO ALEGRE DO PINDARÉ | MARANHÃO | Brasil | 2100477 | 21 | 33 | nan | nan | nan | Amazônia | 7.5 |
| 9b6571d5-a072-37ab-b63b-4642628037be | -2.34135 | -48.84025 | 2024-11-16 04:23:00 | NPP-375D | MOJU | PARÁ | Brasil | 1504703 | 15 | 33 | nan | nan | nan | Amazônia | 0.8 |
| c1ac148b-12e6-3bc9-aeed-d9ddfdfd442d | -2.73691 | -45.14875 | 2024-11-16 04:23:00 | NPP-375D | PINHEIRO | MARANHÃO | Brasil | 2108603 | 21 | 33 | nan | nan | nan | Amazônia | 0.8 |
| 4d3dafe3-b527-3c3d-875c-d7077423c89e | -2.36485 | -48.52554 | 2024-11-16 04:23:00 | NPP-375D | ACARÁ | PARÁ | Brasil | 1500206 | 15 | 33 | nan | nan | nan | Amazônia | 1.5 |
| 03492a8a-7468-30dc-ad82-ac172150c86d | -2.36418 | -48.52978 | 2024-11-16 04:23:00 | NPP-375D | ACARÁ | PARÁ | Brasil | 1500206 | 15 | 33 | nan | nan | nan | Amazônia | 1.1 |
| 723ddcb9-c7bc-312b-b547-c74a1f3a3240 | -4.9043 | -44.0291 | 2024-11-16 04:23:00 | NPP-375D | CODÓ | MARANHÃO | Brasil | 2103307 | 21 | 33 | nan | nan | nan | Cerrado | 3.2 |
| 9e3962ea-0f84-3205-adce-faf34ee6a26f | -3.49497 | -47.21337 | 2024-11-16 04:23:00 | NPP-375D | ULIANÓPOLIS | PARÁ | Brasil | 1508126 | 15 | 33 | nan | nan | nan | Amazônia | 1.4 |
| 10951351-2e94-3c8b-8059-7ccc2d2256d1 | -2.83703 | -46.65568 | 2024-11-16 04:23:00 | NPP-375D | PARAGOMINAS | PARÁ | Brasil | 1505502 | 15 | 33 | nan | nan | nan | Amazônia | 0.9 |
| 952a9ab6-6181-3a8c-8b74-94c009bdf582 | -4.5401 | -43.56258 | 2024-11-16 04:23:00 | NPP-375D | ALDEIAS ALTAS | MARANHÃO | Brasil | 2100303 | 21 | 33 | nan | nan | nan | Cerrado | 2.0 |
| a7a4c70f-3d99-320b-945a-a4aa43353618 | -3.58491 | -50.53295 | 2024-11-16 04:23:00 | NPP-375D | PACAJÁ | PARÁ | Brasil | 1505486 | 15 | 33 | nan | nan | nan | Amazônia | 3.6 |
| eb5586ec-2d7f-3428-a99f-b805e30423c9 | -2.65458 | -46.16767 | 2024-11-16 04:23:00 | NPP-375D | CENTRO DO GUILHERME | MARANHÃO | Brasil | 2103158 | 21 | 33 | nan | nan | nan | Amazônia | 1.7 |
| 8015bfbc-3fd0-3e79-8520-6ccc2dd1b489 | -4.21792 | -47.21704 | 2024-11-16 04:23:00 | NPP-375D | ITINGA DO MARANHÃO | MARANHÃO | Brasil | 2105427 | 21 | 33 | nan | nan | nan | Amazônia | 6.3 |
| 0de97fbf-33d1-388c-8170-ff5bf2682075 | -5.04939 | -43.22675 | 2024-11-16 04:23:00 | NPP-375D | CAXIAS | MARANHÃO | Brasil | 2103000 | 21 | 33 | nan | nan | nan | Cerrado | 1.0 |
| 7a5cbc7a-4722-3a60-9075-7983f6e93588 | -3.01852 | -47.97541 | 2024-11-16 04:23:00 | NPP-375D | IPIXUNA DO PARÁ | PARÁ | Brasil | 1503457 | 15 | 33 | nan | nan | nan | Amazônia | 1.2 |
| da478cc9-db03-3e27-a34c-0c4eca7bc371 | -3.09857 | -45.96898 | 2024-11-16 04:23:00 | NPP-375D | ZÉ DOCA | MARANHÃO | Brasil | 2114007 | 21 | 33 | nan | nan | nan | Amazônia | 1.3 |
| fb6849c5-2e6f-32bf-83dc-bdd0df005404 | -3.94731 | -46.70163 | 2024-11-16 04:23:00 | NPP-375D | BOM JARDIM | MARANHÃO | Brasil | 2102002 | 21 | 33 | nan | nan | nan | Amazônia | 1.0 |
| f95deaa4-4a2a-3fca-adae-5e193748bb5c | -2.62898 | -46.178 | 2024-11-16 04:23:00 | NPP-375D | CENTRO DO GUILHERME | MARANHÃO | Brasil | 2103158 | 21 | 33 | nan | nan | nan | Amazônia | 1.3 |
| 0a09a3cf-f2fe-38f9-b5b4-0a18e9e992a0 | -3.03015 | -47.99341 | 2024-11-16 04:23:00 | NPP-375D | IPIXUNA DO PARÁ | PARÁ | Brasil | 1503457 | 15 | 33 | nan | nan | nan | Amazônia | 2.2 |
| 4e7fdf53-ca39-35ac-895f-8d93b9aec4f4 | -3.57619 | -50.50974 | 2024-11-16 04:23:00 | NPP-375D | PACAJÁ | PARÁ | Brasil | 1505486 | 15 | 33 | nan | nan | nan | Amazônia | 2.9 |
| 75963446-d781-3960-92d5-1a2c5547cb17 | -2.68292 | -46.69817 | 2024-11-16 04:23:00 | NPP-375D | PARAGOMINAS | PARÁ | Brasil | 1505502 | 15 | 33 | nan | nan | nan | Amazônia | 1.1 |
| 342485e4-10fc-35a8-ae5b-d4382f47e213 | -3.50774 | -46.05432 | 2024-11-16 04:23:00 | NPP-375D | BOM JARDIM | MARANHÃO | Brasil | 2102002 | 21 | 33 | nan | nan | nan | Amazônia | 0.7 |
| b89d3f9b-5e04-3615-b17b-f5fb3cdcbec4 | -5.67749 | -35.64687 | 2024-11-16 04:23:00 | NPP-375D | POÇO BRANCO | RIO GRANDE DO NORTE | Brasil | 2410108 | 24 | 33 | nan | nan | nan | Caatinga | 13.7 |
| 04d8ef20-4eb8-3e33-bdc6-5e27db8a923e | -2.79103 | -48.56585 | 2024-11-16 04:23:00 | NPP-375D | TAILÂNDIA | PARÁ | Brasil | 1507953 | 15 | 33 | nan | nan | nan | Amazônia | 18.1 |
| 453b2a57-dc9e-32f3-a6b2-22719517f532 | -3.81117 | -46.51732 | 2024-11-16 04:23:00 | NPP-375D | BOM JARDIM | MARANHÃO | Brasil | 2102002 | 21 | 33 | nan | nan | nan | Amazônia | 1.4 |
| 432711d6-3d7a-36c5-abfa-7f74db216293 | -3.88292 | -45.02621 | 2024-11-16 04:23:00 | NPP-375D | PIO XII | MARANHÃO | Brasil | 2108702 | 21 | 33 | nan | nan | nan | Amazônia | 3.8 |
| 7667d142-a5ef-32b1-ba60-0a675d5c9f5a | -3.90546 | -47.16183 | 2024-11-16 04:23:00 | NPP-375D | ULIANÓPOLIS | PARÁ | Brasil | 1508126 | 15 | 33 | nan | nan | nan | Amazônia | 0.9 |
| 3f462107-e258-33b8-8e00-1b6d33396ddc | -2.5221 | -46.3229 | 2024-11-16 04:23:00 | NPP-375D | CENTRO NOVO DO MARANHÃO | MARANHÃO | Brasil | 2103174 | 21 | 33 | nan | nan | nan | Amazônia | 1.3 |
| 46784e7f-134f-3c76-a213-70b5d54c950f | -2.09964 | -46.58891 | 2024-11-16 04:23:00 | NPP-375D | CACHOEIRA DO PIRIÁ | PARÁ | Brasil | 1501956 | 15 | 33 | nan | nan | nan | Amazônia | 1.1 |
| 0eedded6-b06b-3a51-a592-df80034641ff | -2.25652 | -48.3848 | 2024-11-16 04:23:00 | NPP-375D | ACARÁ | PARÁ | Brasil | 1500206 | 15 | 33 | nan | nan | nan | Amazônia | 1.3 |
| 31c6afb4-62e0-3362-874d-00b741ec5565 | -4.12937 | -46.94141 | 2024-11-16 04:23:00 | NPP-375D | BOM JARDIM | MARANHÃO | Brasil | 2102002 | 21 | 33 | nan | nan | nan | Amazônia | 1.2 |
| 69954c97-36ac-33b0-ad04-556162cdc89f | -2.55362 | -46.89639 | 2024-11-16 04:23:00 | NPP-375D | PARAGOMINAS | PARÁ | Brasil | 1505502 | 15 | 33 | nan | nan | nan | Amazônia | 2.8 |
| 9cce9aed-f2a2-313e-b461-39c204fc9856 | -3.97472 | -46.70234 | 2024-11-16 04:23:00 | NPP-375D | BOM JARDIM | MARANHÃO | Brasil | 2102002 | 21 | 33 | nan | nan | nan | Amazônia | 1.1 |
| 5807cafb-ee37-3ffc-b0b6-5f1276609547 | -2.89311 | -46.87069 | 2024-11-16 04:23:00 | NPP-375D | PARAGOMINAS | PARÁ | Brasil | 1505502 | 15 | 33 | nan | nan | nan | Amazônia | 1.5 |
| e6e19be0-1d92-3703-8225-6f01b054e650 | -3.73378 | -45.65445 | 2024-11-16 04:23:00 | NPP-375D | TUFILÂNDIA | MARANHÃO | Brasil | 2112274 | 21 | 33 | nan | nan | nan | Amazônia | 5.2 |
| b2432938-a898-30a1-9d99-a5b0ce94fa20 | -3.90489 | -47.16546 | 2024-11-16 04:23:00 | NPP-375D | ULIANÓPOLIS | PARÁ | Brasil | 1508126 | 15 | 33 | nan | nan | nan | Amazônia | 0.9 |
| 89621940-6f5c-383d-af24-3ea24c0b1b8e | -2.22012 | -47.21439 | 2024-11-16 04:23:00 | NPP-375D | GARRAFÃO DO NORTE | PARÁ | Brasil | 1503077 | 15 | 33 | nan | nan | nan | Amazônia | 1.5 |
| de834011-b451-3d96-9f86-34fa50df887d | -3.49957 | -47.20657 | 2024-11-16 04:23:00 | NPP-375D | ULIANÓPOLIS | PARÁ | Brasil | 1508126 | 15 | 33 | nan | nan | nan | Amazônia | 3.1 |
| 0f82341f-3ee7-389a-ac53-050fa1dd22f2 | -2.16335 | -46.42691 | 2024-11-16 04:23:00 | NPP-375D | CACHOEIRA DO PIRIÁ | PARÁ | Brasil | 1501956 | 15 | 33 | nan | nan | nan | Amazônia | 0.9 |
| 103f4649-4db4-36ab-be39-b75786eb7031 | -2.38714 | -51.22159 | 2024-11-16 04:23:00 | NPP-375D | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 0.6 |
| 7517dcd5-7287-3e9d-af4d-bfa4a70e2b36 | -1.23358 | -53.7089 | 2024-11-16 04:23:00 | NPP-375D | PRAINHA | PARÁ | Brasil | 1506005 | 15 | 33 | nan | nan | nan | Amazônia | 1.4 |
| a13e216a-e081-3a00-bc1a-3fe233e1f3dc | -3.9501 | -46.70571 | 2024-11-16 04:23:00 | NPP-375D | BOM JARDIM | MARANHÃO | Brasil | 2102002 | 21 | 33 | nan | nan | nan | Amazônia | 1.2 |
| cdec956c-a514-3541-a13f-c4d99a94d825 | -3.12114 | -45.89078 | 2024-11-16 04:23:00 | NPP-375D | ARAGUANÃ | MARANHÃO | Brasil | 2100873 | 21 | 33 | nan | nan | nan | Amazônia | 1.2 |
| aaebf209-cca5-398a-a216-536c47852eb0 | -2.6145 | -46.18291 | 2024-11-16 04:23:00 | NPP-375D | CENTRO DO GUILHERME | MARANHÃO | Brasil | 2103158 | 21 | 33 | nan | nan | nan | Amazônia | 1.8 |
| 84af4ffe-2b9a-3198-a071-e701e60edd26 | -2.82297 | -46.65714 | 2024-11-16 04:23:00 | NPP-375D | PARAGOMINAS | PARÁ | Brasil | 1505502 | 15 | 33 | nan | nan | nan | Amazônia | 1.1 |
| 50a9e2b5-be51-34ed-87dd-4c4315c23200 | -2.65351 | -46.1962 | 2024-11-16 04:23:00 | NPP-375D | CENTRO DO GUILHERME | MARANHÃO | Brasil | 2103158 | 21 | 33 | nan | nan | nan | Amazônia | 1.2 |
| 7f0c0d85-a44b-3f80-8fbf-b7cfa325c563 | -3.04383 | -47.97542 | 2024-11-16 04:23:00 | NPP-375D | IPIXUNA DO PARÁ | PARÁ | Brasil | 1503457 | 15 | 33 | nan | nan | nan | Amazônia | 1.3 |
| 5ffa2350-2532-3408-b9cf-1c6aa7e94110 | -3.06519 | -45.34462 | 2024-11-16 04:23:00 | NPP-375D | PEDRO DO ROSÁRIO | MARANHÃO | Brasil | 2108256 | 21 | 33 | nan | nan | nan | Amazônia | 9.4 |
| 443f8506-2c59-3352-95c9-50077603c5c7 | -3.19827 | -45.55241 | 2024-11-16 04:23:00 | NPP-375D | PEDRO DO ROSÁRIO | MARANHÃO | Brasil | 2108256 | 21 | 33 | nan | nan | nan | Amazônia | 11.8 |
| bb46e9dc-716a-3c45-8406-4e41112ef45f | -3.56732 | -47.3756 | 2024-11-16 04:23:00 | NPP-375D | ULIANÓPOLIS | PARÁ | Brasil | 1508126 | 15 | 33 | nan | nan | nan | Amazônia | 1.0 |


[Clique aqui para ver as próximas entradas](README28.md)
