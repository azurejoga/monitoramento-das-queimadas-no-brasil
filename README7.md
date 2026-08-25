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

## Dados Diários - Página 7

| ID | Latitude | Longitude | Data/Hora GMT | Satélite | Município | Estado | País | Município ID | Estado ID | País ID | Dias sem Chuva | Precipitação | Risco de Fogo | Bioma | FRP |
|----|----------|-----------|---------------|----------|-----------|--------|------|--------------|-----------|---------|----------------|--------------|----------------|-------|-----|
| 76d0fc54-cee3-3f59-a006-b003b5becbe8 | -6.2223 | -55.468601 | 2026-08-25 00:32:00 | METOP-B | ITAITUBA | PARÁ | Brasil | 1503606 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| ee136190-4989-3964-bf15-ea050ecf3096 | -11.1158 | -44.4221 | 2026-08-25 00:32:00 | METOP-B | SANTA RITA DE CÁSSIA | BAHIA | Brasil | 2928406 | 29 | 33 | nan | nan | nan | Cerrado | nan |
| 8b109330-45e4-3e08-b5f1-c9e73959bd4e | -7.2289 | -45.345501 | 2026-08-25 00:32:00 | METOP-B | LORETO | MARANHÃO | Brasil | 2106102 | 21 | 33 | nan | nan | nan | Cerrado | nan |
| 59943c3f-da22-30eb-8287-3506701f7e80 | -7.495 | -55.355999 | 2026-08-25 00:32:00 | METOP-B | NOVO PROGRESSO | PARÁ | Brasil | 1505031 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| 3d5639e0-4e80-3353-9b7d-aced2de00a61 | -8.5459 | -54.7659 | 2026-08-25 00:32:00 | METOP-B | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| 535614c5-75ab-325b-b719-d28d7f134fe6 | -16.401199 | -49.850601 | 2026-08-25 00:32:00 | METOP-B | ANICUNS | GOIÁS | Brasil | 5201306 | 52 | 33 | nan | nan | nan | Cerrado | nan |
| 6dabbd48-fc5f-3d17-b558-5f208d996cad | -6.1342 | -57.826099 | 2026-08-25 00:32:00 | METOP-B | JACAREACANGA | PARÁ | Brasil | 1503754 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| 94eaedb7-0de3-375e-97fd-dded92e5c66e | -6.9614 | -59.060299 | 2026-08-25 00:32:00 | METOP-B | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | nan |
| a8bae5d0-9e53-38fb-9c5f-ed31a9626db2 | -11.1615 | -53.985699 | 2026-08-25 00:32:00 | METOP-B | MARCELÂNDIA | MATO GROSSO | Brasil | 5105580 | 51 | 33 | nan | nan | nan | Amazônia | nan |
| ff0022a9-1251-31e2-8cdd-6a6533033f9d | -6.131 | -57.811699 | 2026-08-25 00:32:00 | METOP-B | JACAREACANGA | PARÁ | Brasil | 1503754 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| 62488ba2-6ab7-3eb1-9f41-d9f74ece5fe5 | -8.6066 | -54.715099 | 2026-08-25 00:32:00 | METOP-B | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| 869c0130-1f76-380a-b20e-82df76bbc25e | -6.8865 | -58.999401 | 2026-08-25 00:32:00 | METOP-B | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | nan |
| 3e787bcc-bfd7-31fa-9fc3-ca612423ec62 | -8.5764 | -54.854599 | 2026-08-25 00:32:00 | METOP-B | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| 0b6a397f-b118-36b8-9dd3-51edbb672adb | -16.404699 | -49.908501 | 2026-08-25 00:32:00 | METOP-B | ANICUNS | GOIÁS | Brasil | 5201306 | 52 | 33 | nan | nan | nan | Cerrado | nan |
| e634636f-d94c-388a-8718-c1cd413ccb00 | -7.2226 | -45.320499 | 2026-08-25 00:32:00 | METOP-B | LORETO | MARANHÃO | Brasil | 2106102 | 21 | 33 | nan | nan | nan | Cerrado | nan |
| 82ce098b-c34d-3b58-9b1b-76a514f1854b | -6.1866 | -53.511299 | 2026-08-25 00:32:00 | METOP-B | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| e945915d-81d7-3280-af14-b8e0ee276afb | -13.8702 | -53.980801 | 2026-08-25 00:32:00 | METOP-B | PARANATINGA | MATO GROSSO | Brasil | 5106307 | 51 | 33 | nan | nan | nan | Cerrado | nan |
| 3ff22032-e8d3-3a70-b67a-6c1fa00d947c | -14.8728 | -52.626999 | 2026-08-25 00:32:00 | METOP-B | NOVA XAVANTINA | MATO GROSSO | Brasil | 5106257 | 51 | 33 | nan | nan | nan | Cerrado | nan |
| 6adcca3f-ea33-33f2-8a09-11b1d0956daa | -10.3459 | -45.015999 | 2026-08-25 00:32:00 | METOP-B | CORRENTE | PIAUÍ | Brasil | 2202901 | 22 | 33 | nan | nan | nan | Cerrado | nan |
| 5ba494c6-fc5b-3f5d-b2b5-1edf07593140 | -6.1819 | -55.426701 | 2026-08-25 00:32:00 | METOP-B | ITAITUBA | PARÁ | Brasil | 1503606 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| 95b2913e-e316-395c-ba5e-2abbaa2056e3 | -7.0014 | -59.242901 | 2026-08-25 00:32:00 | METOP-B | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | nan |
| fa9f13eb-2944-3508-bda1-d9a7f306a91d | -12.6893 | -48.379101 | 2026-08-25 00:32:00 | METOP-B | SÃO SALVADOR DO TOCANTINS | TOCANTINS | Brasil | 1720259 | 17 | 33 | nan | nan | nan | Cerrado | nan |
| 7e3c2c3f-3eee-3c6b-93e0-328a92e5af96 | -6.1445 | -57.687599 | 2026-08-25 00:32:00 | METOP-B | JACAREACANGA | PARÁ | Brasil | 1503754 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| 5576acae-a1aa-3f3e-a6ca-22ef573f42f4 | -18.733999 | -47.421799 | 2026-08-25 00:32:00 | METOP-B | MONTE CARMELO | MINAS GERAIS | Brasil | 3143104 | 31 | 33 | nan | nan | nan | Cerrado | nan |
| 01118c35-eb1b-30b8-8157-7866b2b4c14d | -7.5421 | -61.320801 | 2026-08-25 00:32:00 | METOP-B | MANICORÉ | AMAZONAS | Brasil | 1302702 | 13 | 33 | nan | nan | nan | Amazônia | nan |
| 5642bf8c-3e44-3ce4-9301-016d19e47c22 | -8.6196 | -54.726898 | 2026-08-25 00:32:00 | METOP-B | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| 878251a1-d24f-302a-ba69-3cbf74354a1c | -6.1853 | -57.686199 | 2026-08-25 00:32:00 | METOP-B | JACAREACANGA | PARÁ | Brasil | 1503754 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| 758584a2-8dbf-37f9-b3f1-ce0dcf36eeb4 | -6.1493 | -59.8964 | 2026-08-25 00:32:00 | METOP-B | NOVO ARIPUANÃ | AMAZONAS | Brasil | 1303304 | 13 | 33 | nan | nan | nan | Amazônia | nan |
| 6a49afc3-e7c3-3538-ac8d-efefa03c9fc0 | -6.3497 | -54.760601 | 2026-08-25 00:32:00 | METOP-B | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| f14923d9-c8df-3c7f-95e5-56d190d6d085 | -6.8289 | -58.643398 | 2026-08-25 00:32:00 | METOP-B | MAUÉS | AMAZONAS | Brasil | 1302900 | 13 | 33 | nan | nan | nan | Amazônia | nan |
| 628ccdb4-3e59-38c9-be39-7a98914cba7c | -6.3481 | -54.753502 | 2026-08-25 00:32:00 | METOP-B | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| 4aca7faa-d6ba-3a13-89a8-905ea3a5eafa | -6.8255 | -58.627701 | 2026-08-25 00:32:00 | METOP-B | MAUÉS | AMAZONAS | Brasil | 1302900 | 13 | 33 | nan | nan | nan | Amazônia | nan |
| 2b0dcb5c-b3b7-3baf-a651-f5c3eedf59ea | -23.023899 | -52.646198 | 2026-08-25 00:32:00 | METOP-B | PARANAVAÍ | PARANÁ | Brasil | 4118402 | 41 | 33 | nan | nan | nan | Mata Atlântica | nan |
| 932b19d6-dcc0-34f6-a362-a2fcab0eea60 | -7.219 | -45.833099 | 2026-08-25 00:32:00 | METOP-B | SÃO RAIMUNDO DAS MANGABEIRAS | MARANHÃO | Brasil | 2111607 | 21 | 33 | nan | nan | nan | Cerrado | nan |
| 3e08ff7d-4693-3504-acfc-c958cb33df5a | -6.9712 | -59.058201 | 2026-08-25 00:32:00 | METOP-B | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | nan |
| a822f9ca-c444-305c-bf1e-73bfd914a8a1 | -6.2245 | -49.946201 | 2026-08-25 00:32:00 | METOP-B | PARAUAPEBAS | PARÁ | Brasil | 1505536 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| 994a2f2c-56a8-3ae6-83da-0ba06ee52eda | -12.7472 | -44.205101 | 2026-08-25 00:32:00 | METOP-B | BAIANÓPOLIS | BAHIA | Brasil | 2902500 | 29 | 33 | nan | nan | nan | Cerrado | nan |
| a86b377f-29e2-34b3-bca8-c97eb3d2fa54 | -11.5529 | -46.941299 | 2026-08-25 00:32:00 | METOP-B | DIANÓPOLIS | TOCANTINS | Brasil | 1707009 | 17 | 33 | nan | nan | nan | Cerrado | nan |
| 9fe073cc-9a95-37fe-bab3-3929b816e1bc | -6.757 | -59.627102 | 2026-08-25 00:32:00 | METOP-B | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | nan |
| 7e7b277c-9907-3290-ab53-21bc96349e7f | -8.6164 | -54.712898 | 2026-08-25 00:32:00 | METOP-B | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| 1154f912-f843-3c8a-b0e2-271a51b0c698 | -6.1837 | -57.679001 | 2026-08-25 00:32:00 | METOP-B | JACAREACANGA | PARÁ | Brasil | 1503754 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| 77d37900-4b68-3b8b-ac1b-e68895a04d09 | -6.1536 | -57.913399 | 2026-08-25 00:32:00 | METOP-B | JACAREACANGA | PARÁ | Brasil | 1503754 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| c9f2aa69-34dd-3d67-ac15-7912ef421e8f | -6.3383 | -54.755699 | 2026-08-25 00:32:00 | METOP-B | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| 6c96627a-8c75-3d58-b706-773f9f27c974 | -16.422701 | -51.827499 | 2026-08-25 00:32:00 | METOP-B | PIRANHAS | GOIÁS | Brasil | 5217203 | 52 | 33 | nan | nan | nan | Cerrado | nan |
| 0332cd26-2e13-37e6-8526-47ead6dde422 | -7.4836 | -55.351299 | 2026-08-25 00:32:00 | METOP-B | NOVO PROGRESSO | PARÁ | Brasil | 1505031 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| a2a20138-04d9-311c-8ba2-b3e76ede8a46 | -7.2578 | -45.3381 | 2026-08-25 00:32:00 | METOP-B | LORETO | MARANHÃO | Brasil | 2106102 | 21 | 33 | nan | nan | nan | Cerrado | nan |
| 77e12b88-e841-38c3-8170-4a6c9048c62d | -6.7943 | -59.609901 | 2026-08-25 00:32:00 | METOP-B | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | nan |
| 4b6d4fc2-d590-30b0-b675-a028f3e19386 | -12.7632 | -44.226299 | 2026-08-25 00:32:00 | METOP-B | BAIANÓPOLIS | BAHIA | Brasil | 2902500 | 29 | 33 | nan | nan | nan | Cerrado | nan |
| bd1e8909-761d-3b45-910d-d4b4d68f3d6b | -6.5509 | -58.500599 | 2026-08-25 00:32:00 | METOP-B | MAUÉS | AMAZONAS | Brasil | 1302900 | 13 | 33 | nan | nan | nan | Amazônia | nan |
| fcefa5e9-e8e6-3e64-b61c-92338a8ae89f | -6.7964 | -59.384499 | 2026-08-25 00:32:00 | METOP-B | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | nan |
| 6ce44f42-7a3b-3765-b294-65d5f1821a18 | -3.5078 | -48.1581 | 2026-08-25 00:32:00 | METOP-B | PARAGOMINAS | PARÁ | Brasil | 1505502 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| 1935c9d6-bb4f-39fe-ba4e-1b8661a02d45 | -6.7981 | -59.6273 | 2026-08-25 00:32:00 | METOP-B | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | nan |
| 42fa3fd0-735d-3985-87c2-4510288bc69c | -8.5716 | -54.833698 | 2026-08-25 00:32:00 | METOP-B | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| e36f7c1d-874a-3096-bf2c-9cc468a170a7 | -8.6 | -54.7314 | 2026-08-25 00:32:00 | METOP-B | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| f5faee6f-c430-3792-99de-2d640f6bf69a | -10.9215 | -51.047901 | 2026-08-25 00:32:00 | METOP-B | LUCIARA | MATO GROSSO | Brasil | 5105309 | 51 | 33 | nan | nan | nan | Cerrado | nan |
| 629d0ca5-844e-39f7-b1b3-e1cadd4c945e | -6.3237 | -54.7365 | 2026-08-25 00:32:00 | METOP-B | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| 82b5cdfa-c87e-3645-998a-f7e747765c06 | -5.9436 | -57.7094 | 2026-08-25 00:32:00 | METOP-B | JACAREACANGA | PARÁ | Brasil | 1503754 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| 2f51dd8c-bd44-3871-979c-59ad21c446b8 | -12.7536 | -44.229 | 2026-08-25 00:32:00 | METOP-B | BAIANÓPOLIS | BAHIA | Brasil | 2902500 | 29 | 33 | nan | nan | nan | Cerrado | nan |
| dab2fd2a-c1da-33cc-bc7e-6d0cff99e543 | -8.0827 | -47.438099 | 2026-08-25 00:32:00 | METOP-B | GOIATINS | TOCANTINS | Brasil | 1709005 | 17 | 33 | nan | nan | nan | Cerrado | nan |
| 661b99b6-ef22-3b3c-98f2-990d7ededbcd | -6.4327 | -54.943298 | 2026-08-25 00:32:00 | METOP-B | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| 256119a7-8b5e-3f1f-ac24-e60a28691c65 | -5.7844 | -57.594799 | 2026-08-25 00:32:00 | METOP-B | JACAREACANGA | PARÁ | Brasil | 1503754 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| e86d91ef-a640-34c0-ac88-bb4af4435693 | -6.6243 | -58.4604 | 2026-08-25 00:32:00 | METOP-B | MAUÉS | AMAZONAS | Brasil | 1302900 | 13 | 33 | nan | nan | nan | Amazônia | nan |
| a8baaacf-a493-326f-9806-630530e48536 | -6.5576 | -56.5434 | 2026-08-25 00:32:00 | METOP-B | ITAITUBA | PARÁ | Brasil | 1503606 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| 6fbd8afc-aea2-3b7d-9388-3703cd5a143b | -9.6764 | -55.072399 | 2026-08-25 00:32:00 | METOP-B | NOVO MUNDO | MATO GROSSO | Brasil | 5106265 | 51 | 33 | nan | nan | nan | Amazônia | nan |
| 83e87545-92a6-3134-84c3-5e32b663de26 | -6.9314 | -52.766899 | 2026-08-25 00:32:00 | METOP-B | SÃO FÉLIX DO XINGU | PARÁ | Brasil | 1507300 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| ef5f965d-266c-34b9-94b5-7a675959223e | -5.9473 | -53.591099 | 2026-08-25 00:32:00 | METOP-B | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| 118b4e76-def9-3a43-b810-7f51fb32c34b | -9.4842 | -56.888802 | 2026-08-25 00:32:00 | METOP-B | PARANAÍTA | MATO GROSSO | Brasil | 5106299 | 51 | 33 | nan | nan | nan | Amazônia | nan |
| e1c2b9f6-690c-3d13-91f4-2f371ffe1897 | -10.9064 | -51.071201 | 2026-08-25 00:32:00 | METOP-B | LUCIARA | MATO GROSSO | Brasil | 5105309 | 51 | 33 | nan | nan | nan | Cerrado | nan |
| 0006c68a-ca41-3524-8ea6-6e7ceb30b084 | -6.8608 | -59.397301 | 2026-08-25 00:32:00 | METOP-B | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | nan |
| 73473bc2-14af-377c-b9c3-582c9d363c39 | -4.4695 | -54.785 | 2026-08-25 00:32:00 | METOP-B | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| e10b3b5b-3be0-30aa-a39b-205df89e5ad2 | -5.8675 | -52.094299 | 2026-08-25 00:32:00 | METOP-B | SÃO FÉLIX DO XINGU | PARÁ | Brasil | 1507300 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| a467af5d-238d-3d6d-a416-10326581630f | -6.2391 | -55.406399 | 2026-08-25 00:32:00 | METOP-B | ITAITUBA | PARÁ | Brasil | 1503606 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| 2b5d1a7d-ef95-3b28-9bdd-1ef283f4dc02 | -11.1631 | -53.992802 | 2026-08-25 00:32:00 | METOP-B | MARCELÂNDIA | MATO GROSSO | Brasil | 5105580 | 51 | 33 | nan | nan | nan | Amazônia | nan |
| 742ddb0a-d927-3039-8945-9eb13cc9c027 | -6.8063 | -59.5709 | 2026-08-25 00:32:00 | METOP-B | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | nan |
| c1167855-756b-3038-8211-595ce128f902 | -6.2571 | -55.3951 | 2026-08-25 00:32:00 | METOP-B | ITAITUBA | PARÁ | Brasil | 1503606 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| 83316e72-0283-38f5-8255-d7afacc4a7b8 | -13.6484 | -51.8396 | 2026-08-25 00:32:00 | METOP-B | CANARANA | MATO GROSSO | Brasil | 5102702 | 51 | 33 | nan | nan | nan | Cerrado | nan |
| ad6a1981-3677-3bda-b7dc-8ae304175c54 | -6.7845 | -59.612 | 2026-08-25 00:32:00 | METOP-B | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | nan |
| 6c1b41c7-8d34-3eea-8834-966d35d828a5 | -6.6259 | -58.467999 | 2026-08-25 00:32:00 | METOP-B | MAUÉS | AMAZONAS | Brasil | 1302900 | 13 | 33 | nan | nan | nan | Amazônia | nan |
| 7837bb0f-5da7-3bfb-8777-844c8a7a4b22 | -11.1127 | -44.449402 | 2026-08-25 00:32:00 | METOP-B | SANTA RITA DE CÁSSIA | BAHIA | Brasil | 2928406 | 29 | 33 | nan | nan | nan | Cerrado | nan |
| ecf0a7d4-e19d-31c2-8d37-d5f837416b13 | -6.1216 | -57.7229 | 2026-08-25 00:32:00 | METOP-B | JACAREACANGA | PARÁ | Brasil | 1503754 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| 092c0226-2ef0-33f2-9968-954f87861178 | -12.6925 | -48.3918 | 2026-08-25 00:32:00 | METOP-B | SÃO SALVADOR DO TOCANTINS | TOCANTINS | Brasil | 1720259 | 17 | 33 | nan | nan | nan | Cerrado | nan |
| 94e40b93-a447-35a2-a40e-9786392b8a73 | -6.9996 | -59.234501 | 2026-08-25 00:32:00 | METOP-B | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | nan |
| f8da32b5-90f4-3ac7-acc5-b1a80fec4ea3 | -11.5473 | -46.9603 | 2026-08-25 00:32:00 | METOP-B | DIANÓPOLIS | TOCANTINS | Brasil | 1707009 | 17 | 33 | nan | nan | nan | Cerrado | nan |
| 06313fcf-6734-352c-a82e-cf505af44d5c | -6.0888 | -53.400299 | 2026-08-25 00:32:00 | METOP-B | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| 3b9b646e-507c-3e3c-a76b-0e465847048b | -6.8076 | -58.6399 | 2026-08-25 00:32:00 | METOP-B | MAUÉS | AMAZONAS | Brasil | 1302900 | 13 | 33 | nan | nan | nan | Amazônia | nan |
| 2e7442e1-0797-399b-8e03-f840ac8cdac0 | -6.7646 | -59.426998 | 2026-08-25 00:32:00 | METOP-B | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | nan |
| d1012adf-9e22-3c25-9466-30327d44ca7d | -6.6408 | -58.488998 | 2026-08-25 00:32:00 | METOP-B | MAUÉS | AMAZONAS | Brasil | 1302900 | 13 | 33 | nan | nan | nan | Amazônia | nan |
| 925502bd-d7c9-3614-969c-829a961ff227 | -6.6374 | -58.473598 | 2026-08-25 00:32:00 | METOP-B | MAUÉS | AMAZONAS | Brasil | 1302900 | 13 | 33 | nan | nan | nan | Amazônia | nan |
| 17ed9921-7620-3971-8013-c76f1cd815ed | -10.0698 | -60.4772 | 2026-08-25 00:32:00 | METOP-B | ARIPUANÃ | MATO GROSSO | Brasil | 5101407 | 51 | 33 | nan | nan | nan | Amazônia | nan |
| 86622ebb-136d-3acc-896f-ed2b865f843f | -6.3415 | -54.724899 | 2026-08-25 00:32:00 | METOP-B | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| bd373f51-3e32-35da-b9bf-950db666c671 | -8.618 | -54.719898 | 2026-08-25 00:32:00 | METOP-B | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| 0ae00b9f-a9d1-3384-b11e-b0723e893859 | -6.7037 | -56.322601 | 2026-08-25 00:32:00 | METOP-B | ITAITUBA | PARÁ | Brasil | 1503606 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| 51208255-0619-3c00-bec6-1563a34fce73 | -6.6975 | -55.565102 | 2026-08-25 00:32:00 | METOP-B | NOVO PROGRESSO | PARÁ | Brasil | 1505031 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| 8e5caaf8-d2dd-3bc4-886e-6907cd69977a | -6.4457 | -54.9552 | 2026-08-25 00:32:00 | METOP-B | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| 25966bbd-231b-343c-a8a1-0de2e2e4bfb4 | -9.4356 | -51.571301 | 2026-08-25 00:32:00 | METOP-B | SÃO FÉLIX DO XINGU | PARÁ | Brasil | 1507300 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| 2fa5fb92-1ce8-3b19-90d7-ca30525dcdfd | -13.9123 | -54.030399 | 2026-08-25 00:32:00 | METOP-B | PARANATINGA | MATO GROSSO | Brasil | 5106307 | 51 | 33 | nan | nan | nan | Cerrado | nan |
| 19d6d848-076d-3fb9-805f-98be589e94a4 | -7.3551 | -55.6488 | 2026-08-25 00:32:00 | METOP-B | NOVO PROGRESSO | PARÁ | Brasil | 1505031 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| bd58c52f-15c5-322a-9386-dbe58b3ff197 | -9.2023 | -50.075298 | 2026-08-25 00:32:00 | METOP-B | SANTANA DO ARAGUAIA | PARÁ | Brasil | 1506708 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| 67e5c0e5-f9e9-3ead-9f9c-1c5388882546 | -6.2603 | -55.409 | 2026-08-25 00:32:00 | METOP-B | ITAITUBA | PARÁ | Brasil | 1503606 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| 4065218a-9b7b-3d18-940d-e1ca06a04a73 | -5.7958 | -57.599701 | 2026-08-25 00:32:00 | METOP-B | JACAREACANGA | PARÁ | Brasil | 1503754 | 15 | 33 | nan | nan | nan | Amazônia | nan |


[Clique aqui para ver as próximas entradas](README8.md)
