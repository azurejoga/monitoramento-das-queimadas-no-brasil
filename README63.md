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

## Dados Diários - Página 63

| ID | Latitude | Longitude | Data/Hora GMT | Satélite | Município | Estado | País | Município ID | Estado ID | País ID | Dias sem Chuva | Precipitação | Risco de Fogo | Bioma | FRP |
|----|----------|-----------|---------------|----------|-----------|--------|------|--------------|-----------|---------|----------------|--------------|----------------|-------|-----|
| c5f57481-30bd-342a-82f7-7d5073b6d607 | -6.804 | -59.42209 | 2026-08-21 05:23:00 | NPP-375D | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 2.8 |
| 0a0b9951-c532-3333-8607-e40871d713a7 | -6.85682 | -59.43815 | 2026-08-21 05:23:00 | NPP-375D | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 5.9 |
| f8bdd735-0b8a-3460-b1a8-0a0add494e1e | -8.58015 | -54.74869 | 2026-08-21 05:23:00 | NPP-375D | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 1.7 |
| 5b216cc2-4428-3f0f-8975-e6ddd9aa9076 | -7.7952 | -61.18666 | 2026-08-21 05:23:00 | NPP-375D | NOVO ARIPUANÃ | AMAZONAS | Brasil | 1303304 | 13 | 33 | nan | nan | nan | Amazônia | 3.0 |
| fa5d3909-e6e7-3b1d-88ad-f844770aaba6 | -6.88055 | -56.63638 | 2026-08-21 05:23:00 | NPP-375D | ITAITUBA | PARÁ | Brasil | 1503606 | 15 | 33 | nan | nan | nan | Amazônia | 2.7 |
| b8a6783b-883f-3c56-85ea-cb7fe43c0821 | -6.31948 | -55.91515 | 2026-08-21 05:23:00 | NPP-375D | ITAITUBA | PARÁ | Brasil | 1503606 | 15 | 33 | nan | nan | nan | Amazônia | 0.8 |
| 7912fc2a-e169-3ae5-a7df-f2895da77a2b | -8.55403 | -55.32253 | 2026-08-21 05:23:00 | NPP-375D | NOVO PROGRESSO | PARÁ | Brasil | 1505031 | 15 | 33 | nan | nan | nan | Amazônia | 1.8 |
| 5be79db3-1261-36c8-b812-65f05b1e9d40 | -8.57409 | -54.6648 | 2026-08-21 05:23:00 | NPP-375D | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 1.1 |
| eb44e9e0-1417-3af6-abf3-1e634cbbd337 | -3.54029 | -48.17757 | 2026-08-21 05:23:00 | NPP-375D | PARAGOMINAS | PARÁ | Brasil | 1505502 | 15 | 33 | nan | nan | nan | Amazônia | 7.6 |
| aa4e1a66-c555-338e-ac24-51197308ef2e | -6.72443 | -59.08964 | 2026-08-21 05:23:00 | NPP-375D | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 1.0 |
| fa7b4d25-0b65-3ebe-b89f-23fd321d69e1 | -6.85964 | -59.44241 | 2026-08-21 05:23:00 | NPP-375D | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 3.7 |
| ddbd0163-15ef-31b7-8f25-3f37e4875312 | -6.52419 | -58.60155 | 2026-08-21 05:23:00 | NPP-375D | MAUÉS | AMAZONAS | Brasil | 1302900 | 13 | 33 | nan | nan | nan | Amazônia | 1.5 |
| fec34b93-bc0d-3fd5-954c-cfbc7c9029e0 | -14.31321 | -51.89336 | 2026-08-21 05:23:00 | NPP-375D | NOVA NAZARÉ | MATO GROSSO | Brasil | 5106174 | 51 | 33 | nan | nan | nan | Cerrado | 65.9 |
| 97ffd62d-e48f-344c-b97a-d6c61fd6a397 | -8.59686 | -54.71194 | 2026-08-21 05:23:00 | NPP-375D | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 1.6 |
| 166eea1f-d5f6-3269-8d51-eb067f1fb83d | -7.37191 | -45.82463 | 2026-08-21 05:23:00 | NPP-375D | BALSAS | MARANHÃO | Brasil | 2101400 | 21 | 33 | nan | nan | nan | Cerrado | 5.0 |
| 8600747d-965b-3caf-9ff1-d86038a17379 | -8.65306 | -54.63118 | 2026-08-21 05:23:00 | NPP-375D | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 1.0 |
| 607ec643-6e56-340e-b720-a50ac92fe2cd | -7.05533 | -56.50686 | 2026-08-21 05:23:00 | NPP-375D | ITAITUBA | PARÁ | Brasil | 1503606 | 15 | 33 | nan | nan | nan | Amazônia | 1.0 |
| e0a1f15a-676f-3d0f-9ff0-cf44df46aabd | -7.55327 | -55.5599 | 2026-08-21 05:23:00 | NPP-375D | NOVO PROGRESSO | PARÁ | Brasil | 1505031 | 15 | 33 | nan | nan | nan | Amazônia | 2.1 |
| d237f1fb-cf86-3c0c-80ec-076b87c8eb54 | -13.39736 | -54.39159 | 2026-08-21 05:23:00 | NPP-375D | PARANATINGA | MATO GROSSO | Brasil | 5106307 | 51 | 33 | nan | nan | nan | Amazônia | 10.2 |
| 5e5946e8-ecc7-3a35-8cfe-67f9e404fdc4 | -9.06205 | -60.44198 | 2026-08-21 05:23:00 | NPP-375D | COLNIZA | MATO GROSSO | Brasil | 5103254 | 51 | 33 | nan | nan | nan | Amazônia | 1.5 |
| 91dfca70-631b-3225-af15-dcd31dfceb45 | -6.1076 | -57.73763 | 2026-08-21 05:23:00 | NPP-375D | JACAREACANGA | PARÁ | Brasil | 1503754 | 15 | 33 | nan | nan | nan | Amazônia | 1.7 |
| 89b62bf2-bb9c-3697-be5e-f8b27e0f4989 | -6.24373 | -55.39393 | 2026-08-21 05:23:00 | NPP-375D | ITAITUBA | PARÁ | Brasil | 1503606 | 15 | 33 | nan | nan | nan | Amazônia | 1.1 |
| fd6b2113-f2ea-32bb-a290-22e7490c61fd | -11.32652 | -45.01558 | 2026-08-21 05:23:00 | NPP-375D | FORMOSA DO RIO PRETO | BAHIA | Brasil | 2911105 | 29 | 33 | nan | nan | nan | Cerrado | 6.6 |
| 8bd46e40-5984-3508-a89c-a0b2845d95a6 | -6.87633 | -56.42113 | 2026-08-21 05:23:00 | NPP-375D | ITAITUBA | PARÁ | Brasil | 1503606 | 15 | 33 | nan | nan | nan | Amazônia | 0.9 |
| f11c209b-0f76-3d7f-8cac-2a009e6adbac | -8.57507 | -54.78238 | 2026-08-21 05:23:00 | NPP-375D | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 0.9 |
| 76d4e66e-31d0-3f7d-9e75-c9e9bc6f4a3a | -7.34232 | -55.68731 | 2026-08-21 05:23:00 | NPP-375D | NOVO PROGRESSO | PARÁ | Brasil | 1505031 | 15 | 33 | nan | nan | nan | Amazônia | 1.1 |
| 479f1554-7653-34d4-9079-5d0b190d1e8c | -14.03711 | -58.8676 | 2026-08-21 05:23:00 | NPP-375D | TANGARÁ DA SERRA | MATO GROSSO | Brasil | 5107958 | 51 | 33 | nan | nan | nan | Cerrado | 1.0 |
| d0830797-c69d-35f1-a75f-edd93840f971 | -6.66566 | -52.88802 | 2026-08-21 05:23:00 | NPP-375D | SÃO FÉLIX DO XINGU | PARÁ | Brasil | 1507300 | 15 | 33 | nan | nan | nan | Amazônia | 1.1 |
| cef158d9-d4ab-3502-8beb-8dff0dc6875d | -14.02008 | -53.68736 | 2026-08-21 05:23:00 | NPP-375D | PARANATINGA | MATO GROSSO | Brasil | 5106307 | 51 | 33 | nan | nan | nan | Cerrado | 0.9 |
| b31bd048-0761-3992-b95d-e8b93a2a0db0 | -6.86366 | -59.43925 | 2026-08-21 05:23:00 | NPP-375D | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 3.5 |
| 59cc5cc0-8b5f-318a-942e-5be3b1e91b47 | -8.57044 | -54.66425 | 2026-08-21 05:23:00 | NPP-375D | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 1.6 |
| b64010f2-53a4-32b3-8716-99550182672b | -6.87812 | -59.41502 | 2026-08-21 05:23:00 | NPP-375D | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 1.8 |
| ce240c41-d43b-3371-b227-7482392ca5ab | -15.16821 | -48.78401 | 2026-08-21 05:23:00 | NPP-375D | VILA PROPÍCIO | GOIÁS | Brasil | 5222302 | 52 | 33 | nan | nan | nan | Cerrado | 1.6 |
| c70d5818-df81-35c8-8952-0d7c47e834e1 | -7.05814 | -56.51094 | 2026-08-21 05:23:00 | NPP-375D | ITAITUBA | PARÁ | Brasil | 1503606 | 15 | 33 | nan | nan | nan | Amazônia | 1.0 |
| ffbbe776-059a-39d4-83d9-175123767da8 | -8.57951 | -54.75292 | 2026-08-21 05:23:00 | NPP-375D | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 1.7 |
| 14b6ca1f-b38e-3e42-b2f5-bedc1266bcac | -6.09708 | -57.86765 | 2026-08-21 05:23:00 | NPP-375D | JACAREACANGA | PARÁ | Brasil | 1503754 | 15 | 33 | nan | nan | nan | Amazônia | 1.1 |
| 0ba28631-f908-36ae-a105-a3dd3c6a554f | -8.62172 | -54.7201 | 2026-08-21 05:23:00 | NPP-375D | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 1.4 |
| 12093be6-a61a-3881-a64d-7bea3ddb1278 | -6.91557 | -59.35667 | 2026-08-21 05:23:00 | NPP-375D | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 1.0 |
| 03ffaa8c-e96e-36f6-91ae-4aa21094038d | -6.92358 | -59.35042 | 2026-08-21 05:23:00 | NPP-375D | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 1.5 |
| df497a67-9593-35ce-bc34-a27427e9d80e | -14.71899 | -47.14161 | 2026-08-21 05:23:00 | NPP-375D | VILA BOA | GOIÁS | Brasil | 5222203 | 52 | 33 | nan | nan | nan | Cerrado | 1.1 |
| d383c19b-a9e0-3c6b-a730-e192c7689084 | -3.84126 | -59.37552 | 2026-08-21 05:23:00 | NPP-375D | AUTAZES | AMAZONAS | Brasil | 1300300 | 13 | 33 | nan | nan | nan | Amazônia | 2.1 |
| 3a21e277-c664-32a9-8036-adfad88fb0b7 | -6.87453 | -59.43724 | 2026-08-21 05:23:00 | NPP-375D | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 3.1 |
| 727b5bcf-81c0-3024-b68a-5e58e5e69931 | -12.15772 | -57.218 | 2026-08-21 05:23:00 | NPP-375D | NOVA MARINGÁ | MATO GROSSO | Brasil | 5108907 | 51 | 33 | nan | nan | nan | Amazônia | 1.0 |
| 78fdf338-8b92-3f17-bc38-e26ad6dd0b9d | -6.2079 | -55.48805 | 2026-08-21 05:23:00 | NPP-375D | ITAITUBA | PARÁ | Brasil | 1503606 | 15 | 33 | nan | nan | nan | Amazônia | 1.3 |
| b0ac7f18-ac08-3992-85ee-1e012a563481 | -6.80742 | -59.42265 | 2026-08-21 05:23:00 | NPP-375D | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 2.8 |
| 347f9864-44eb-3b35-bcd0-1d032d19289f | -6.5777 | -58.98457 | 2026-08-21 05:23:00 | NPP-375D | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 1.3 |
| bd2e224e-79dc-3663-acae-8162b26b081f | -6.89796 | -58.99134 | 2026-08-21 05:23:00 | NPP-375D | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 1.2 |
| 70369d67-3991-360e-8d38-3295bb06a181 | -6.55314 | -56.25766 | 2026-08-21 05:23:00 | NPP-375D | ITAITUBA | PARÁ | Brasil | 1503606 | 15 | 33 | nan | nan | nan | Amazônia | 0.9 |
| b7aee4fc-cdfd-3c49-9667-746abbf11a5e | -4.95658 | -56.26117 | 2026-08-21 05:23:00 | NPP-375D | TRAIRÃO | PARÁ | Brasil | 1508050 | 15 | 33 | nan | nan | nan | Amazônia | 2.1 |
| 1f09635c-cfba-3711-9d2d-2ff00319dd54 | -8.05268 | -61.71216 | 2026-08-21 05:23:00 | NPP-375D | MANICORÉ | AMAZONAS | Brasil | 1302702 | 13 | 33 | nan | nan | nan | Amazônia | 1.2 |
| a37d5749-56be-3075-974a-f84050c5a779 | -7.53189 | -57.65495 | 2026-08-21 05:23:00 | NPP-375D | JACAREACANGA | PARÁ | Brasil | 1503754 | 15 | 33 | nan | nan | nan | Amazônia | 1.7 |
| ae7a5cf3-24b6-36ab-8e77-e56e3a457ebf | -6.70514 | -59.10139 | 2026-08-21 05:23:00 | NPP-375D | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 1.5 |
| e4d9d458-8526-3f66-847c-6e76bbd8b8aa | -6.87585 | -43.74392 | 2026-08-21 05:23:00 | NPP-375D | GUADALUPE | PIAUÍ | Brasil | 2204501 | 22 | 33 | nan | nan | nan | Cerrado | 8.1 |
| ca082666-368f-33dd-9285-fcf25fdb56cb | -14.03379 | -58.86705 | 2026-08-21 05:23:00 | NPP-375D | TANGARÁ DA SERRA | MATO GROSSO | Brasil | 5107958 | 51 | 33 | nan | nan | nan | Cerrado | 1.0 |
| e6898a57-0ccd-32af-8360-77197cc8ff21 | -6.80703 | -59.01355 | 2026-08-21 05:23:00 | NPP-375D | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 1.2 |
| 99db8cbd-cb06-3035-9d7b-c85874dd85a6 | -7.53651 | -55.57678 | 2026-08-21 05:23:00 | NPP-375D | NOVO PROGRESSO | PARÁ | Brasil | 1505031 | 15 | 33 | nan | nan | nan | Amazônia | 1.5 |
| 5f83bf70-6569-3e54-8b6f-a4b52a56620b | -3.53982 | -48.18069 | 2026-08-21 05:23:00 | NPP-375D | PARAGOMINAS | PARÁ | Brasil | 1505502 | 15 | 33 | nan | nan | nan | Amazônia | 7.6 |
| e69bc330-d9b9-32d3-ade6-874783805658 | -7.36758 | -45.80821 | 2026-08-21 05:23:00 | NPP-375D | BALSAS | MARANHÃO | Brasil | 2101400 | 21 | 33 | nan | nan | nan | Cerrado | 14.9 |
| 9ed2b47b-7056-35bd-85e1-70545e3be11a | -9.17602 | -57.00756 | 2026-08-21 05:23:00 | NPP-375D | JACAREACANGA | PARÁ | Brasil | 1503754 | 15 | 33 | nan | nan | nan | Amazônia | 1.4 |
| 37c4cb92-19df-3b12-88b7-a77171f568e3 | -6.11985 | -59.90621 | 2026-08-21 05:23:00 | NPP-375D | NOVO ARIPUANÃ | AMAZONAS | Brasil | 1303304 | 13 | 33 | nan | nan | nan | Amazônia | 2.5 |
| c01c377d-00be-3fcd-a9cc-470b4b957e62 | -8.27089 | -57.34755 | 2026-08-21 05:23:00 | NPP-375D | JACAREACANGA | PARÁ | Brasil | 1503754 | 15 | 33 | nan | nan | nan | Amazônia | 1.4 |
| 6eb40ff4-e5ab-3fd4-b9ef-85a336252d29 | -6.12623 | -59.91124 | 2026-08-21 05:23:00 | NPP-375D | NOVO ARIPUANÃ | AMAZONAS | Brasil | 1303304 | 13 | 33 | nan | nan | nan | Amazônia | 1.7 |
| 4881aacb-d6a5-3884-aa8d-d08e4ad4f1d7 | -6.23911 | -55.40087 | 2026-08-21 05:23:00 | NPP-375D | ITAITUBA | PARÁ | Brasil | 1503606 | 15 | 33 | nan | nan | nan | Amazônia | 1.4 |
| cdf1a688-a158-3593-ab37-1aa31af196ce | -5.8258 | -57.6363 | 2026-08-21 05:23:00 | NPP-375D | JACAREACANGA | PARÁ | Brasil | 1503754 | 15 | 33 | nan | nan | nan | Amazônia | 0.9 |
| c13b38fd-69e9-38c7-83af-325ca3bd0fb1 | -8.5505 | -55.32197 | 2026-08-21 05:23:00 | NPP-375D | NOVO PROGRESSO | PARÁ | Brasil | 1505031 | 15 | 33 | nan | nan | nan | Amazônia | 1.3 |
| 67625b66-7520-3fdc-9a30-811fe63b1b31 | -8.62159 | -54.71817 | 2026-08-21 05:23:00 | NPP-375D | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 1.0 |
| de88e165-90a3-3344-b341-a12cc20e80cc | -7.61016 | -60.94958 | 2026-08-21 05:23:00 | NPP-375D | NOVO ARIPUANÃ | AMAZONAS | Brasil | 1303304 | 13 | 33 | nan | nan | nan | Amazônia | 1.6 |
| a1f81628-33b4-350a-9f47-01bbd7c72766 | -6.4306 | -52.74574 | 2026-08-21 05:23:00 | NPP-375D | SÃO FÉLIX DO XINGU | PARÁ | Brasil | 1507300 | 15 | 33 | nan | nan | nan | Amazônia | 2.9 |
| 355516d1-4bf3-3e1b-9be4-f1149edabf49 | -6.10466 | -57.71591 | 2026-08-21 05:23:00 | NPP-375D | JACAREACANGA | PARÁ | Brasil | 1503754 | 15 | 33 | nan | nan | nan | Amazônia | 4.8 |
| b6d533a8-3e2b-3e46-b657-ab4dd6593de6 | -6.33731 | -46.52322 | 2026-08-21 05:23:00 | NPP-375D | SÍTIO NOVO | MARANHÃO | Brasil | 2111805 | 21 | 33 | nan | nan | nan | Cerrado | 0.8 |
| f17feb15-3f51-349b-9017-f049b4a1460b | -8.54936 | -55.30539 | 2026-08-21 05:23:00 | NPP-375D | NOVO PROGRESSO | PARÁ | Brasil | 1505031 | 15 | 33 | nan | nan | nan | Amazônia | 2.3 |
| b389d152-3a2d-3e10-8212-563bdde51b67 | -7.33657 | -55.67878 | 2026-08-21 05:23:00 | NPP-375D | NOVO PROGRESSO | PARÁ | Brasil | 1505031 | 15 | 33 | nan | nan | nan | Amazônia | 0.9 |
| 41dff8fa-a180-30c5-bab4-6464f698855d | -9.11334 | -60.34752 | 2026-08-21 05:23:00 | NPP-375D | COLNIZA | MATO GROSSO | Brasil | 5103254 | 51 | 33 | nan | nan | nan | Amazônia | 1.2 |
| 4e1acb06-4f17-31d7-b06e-b9bdb1177b2b | -8.8968 | -60.54446 | 2026-08-21 05:23:00 | NPP-375D | COLNIZA | MATO GROSSO | Brasil | 5103254 | 51 | 33 | nan | nan | nan | Amazônia | 8.5 |
| 44d791ee-6717-37b7-82cc-240c6292eb63 | -14.56959 | -52.99032 | 2026-08-21 05:23:00 | NPP-375D | CAMPINÁPOLIS | MATO GROSSO | Brasil | 5102603 | 51 | 33 | nan | nan | nan | Cerrado | 0.7 |
| e681a7a9-52fa-3344-a017-5363dd846467 | -6.89077 | -55.71917 | 2026-08-21 05:23:00 | NPP-375D | NOVO PROGRESSO | PARÁ | Brasil | 1505031 | 15 | 33 | nan | nan | nan | Amazônia | 2.1 |
| b0959a92-03ad-3b24-8ccc-35541cd086c0 | -6.86084 | -59.43499 | 2026-08-21 05:23:00 | NPP-375D | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 3.5 |
| d4bdd463-23d9-3b9c-9786-aec1c9217551 | -8.10545 | -51.66576 | 2026-08-21 05:23:00 | NPP-375D | OURILÂNDIA DO NORTE | PARÁ | Brasil | 1505437 | 15 | 33 | nan | nan | nan | Amazônia | 1.1 |
| 6c9071b9-f559-3ce2-a070-de5c824ea99f | -6.10741 | -57.69858 | 2026-08-21 05:23:00 | NPP-375D | JACAREACANGA | PARÁ | Brasil | 1503754 | 15 | 33 | nan | nan | nan | Amazônia | 1.0 |
| 135706d6-3bd0-38a7-91fe-6c91767873d1 | -14.30378 | -51.89198 | 2026-08-21 05:23:00 | NPP-375D | NOVA NAZARÉ | MATO GROSSO | Brasil | 5106174 | 51 | 33 | nan | nan | nan | Cerrado | 0.9 |
| d5efa379-b307-37e0-8806-a979dac8fb47 | -13.94156 | -53.86184 | 2026-08-21 05:23:00 | NPP-375D | PARANATINGA | MATO GROSSO | Brasil | 5106307 | 51 | 33 | nan | nan | nan | Cerrado | 2.6 |
| e1de77ff-7358-305b-86f8-780564acd243 | -6.85415 | -57.68632 | 2026-08-21 05:23:00 | NPP-375D | JACAREACANGA | PARÁ | Brasil | 1503754 | 15 | 33 | nan | nan | nan | Amazônia | 0.8 |
| 3716f4e1-1486-3018-92db-92e1e784f4db | -8.10974 | -50.03613 | 2026-08-21 05:23:00 | NPP-375D | REDENÇÃO | PARÁ | Brasil | 1506138 | 15 | 33 | nan | nan | nan | Amazônia | 2.8 |
| d97f23e8-37ea-3c2c-9d37-e95d28390ff9 | -10.531 | -50.81627 | 2026-08-21 05:23:00 | NPP-375D | SANTA TEREZINHA | MATO GROSSO | Brasil | 5107776 | 51 | 33 | nan | nan | nan | Cerrado | 1.3 |
| 016c58c2-3875-3614-883e-205fa8cf5fb2 | -9.44918 | -51.61379 | 2026-08-21 05:23:00 | NPP-375D | SÃO FÉLIX DO XINGU | PARÁ | Brasil | 1507300 | 15 | 33 | nan | nan | nan | Amazônia | 1.9 |
| 61a7fec8-d070-3449-8610-28da3536a803 | -14.22122 | -51.92581 | 2026-08-21 05:23:00 | NPP-375D | NOVA NAZARÉ | MATO GROSSO | Brasil | 5106174 | 51 | 33 | nan | nan | nan | Cerrado | 1.4 |
| b08735cb-5f78-3f26-96d7-b179dcbe1e19 | -9.01053 | -60.44643 | 2026-08-21 05:23:00 | NPP-375D | COLNIZA | MATO GROSSO | Brasil | 5103254 | 51 | 33 | nan | nan | nan | Amazônia | 1.5 |
| e762b95a-da87-3a81-b576-9ec513443d67 | -6.36775 | -58.33367 | 2026-08-21 05:23:00 | NPP-375D | MAUÉS | AMAZONAS | Brasil | 1302900 | 13 | 33 | nan | nan | nan | Amazônia | 0.7 |
| d17654d1-cdc9-3f50-8cc2-98230c2c0537 | -13.43604 | -51.81347 | 2026-08-21 05:23:00 | NPP-375D | CANARANA | MATO GROSSO | Brasil | 5102702 | 51 | 33 | nan | nan | nan | Cerrado | 2.4 |
| 5514581c-b474-3f21-9a9f-829c2d63aaec | -13.3823 | -54.38409 | 2026-08-21 05:23:00 | NPP-375D | PARANATINGA | MATO GROSSO | Brasil | 5106307 | 51 | 33 | nan | nan | nan | Amazônia | 23.4 |
| fd02e8e8-5edb-393b-93bd-2a483ea13176 | -9.15593 | -59.65899 | 2026-08-21 05:23:00 | NPP-375D | COLNIZA | MATO GROSSO | Brasil | 5103254 | 51 | 33 | nan | nan | nan | Amazônia | 0.7 |
| 76155baf-e640-3361-b3d1-f48afbddf01d | -4.45304 | -55.39322 | 2026-08-21 05:23:00 | NPP-375D | RURÓPOLIS | PARÁ | Brasil | 1506195 | 15 | 33 | nan | nan | nan | Amazônia | 1.4 |
| cf672316-fb49-33f6-b319-05a7c7d5abd2 | -13.38302 | -54.37897 | 2026-08-21 05:23:00 | NPP-375D | PARANATINGA | MATO GROSSO | Brasil | 5106307 | 51 | 33 | nan | nan | nan | Amazônia | 23.4 |
| a2d6e112-631a-3ef6-a993-98923676d9d1 | -9.06746 | -60.43094 | 2026-08-21 05:23:00 | NPP-375D | COLNIZA | MATO GROSSO | Brasil | 5103254 | 51 | 33 | nan | nan | nan | Amazônia | 1.7 |
| 8579ef9a-a8e7-3339-a170-62a54af69f38 | -6.87855 | -59.43409 | 2026-08-21 05:23:00 | NPP-375D | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 3.5 |
| 3d7c90ce-cabc-37ae-b985-21bd257187de | -7.45621 | -46.15182 | 2026-08-21 05:23:00 | NPP-375D | BALSAS | MARANHÃO | Brasil | 2101400 | 21 | 33 | nan | nan | nan | Cerrado | 3.0 |
| e6f1fa9f-6da0-397e-8a2c-f792d7043dd2 | -3.84064 | -59.3794 | 2026-08-21 05:23:00 | NPP-375D | AUTAZES | AMAZONAS | Brasil | 1300300 | 13 | 33 | nan | nan | nan | Amazônia | 2.1 |
| c9554c0b-11e4-307b-8fd4-e954738f886c | -6.88137 | -59.43835 | 2026-08-21 05:23:00 | NPP-375D | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 1.8 |
| ce306a62-07d5-3c6c-854c-ad0c45f32978 | -15.71427 | -47.79755 | 2026-08-21 05:23:00 | NPP-375D | BRASÍLIA | DISTRITO FEDERAL | Brasil | 5300108 | 53 | 33 | nan | nan | nan | Cerrado | 3.1 |
| 8c26ac1f-cba7-3b70-ace4-43a7650e8b41 | -8.71696 | -49.61628 | 2026-08-21 05:23:00 | NPP-375D | CONCEIÇÃO DO ARAGUAIA | PARÁ | Brasil | 1502707 | 15 | 33 | nan | nan | nan | Amazônia | 1.5 |


[Clique aqui para ver as próximas entradas](README64.md)
