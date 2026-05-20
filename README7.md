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
| 7353cf3c-645c-3f73-b51d-80d2a3325850 | -6.29388 | -43.63667 | 2026-05-20 04:42:00 | NOAA-20 | PASSAGEM FRANCA | MARANHÃO | Brasil | 2107902 | 21 | 33 | nan | nan | nan | Cerrado | 0.7 |
| f7778d27-1f1d-3bac-9202-a20955017b1e | -9.97109 | -52.41261 | 2026-05-20 04:42:00 | NOAA-20 | SANTA CRUZ DO XINGU | MATO GROSSO | Brasil | 5107743 | 51 | 33 | nan | nan | nan | Amazônia | 2.9 |
| 28b8bfef-b2e5-3d18-b29c-6e15a10efab2 | -10.48825 | -49.36184 | 2026-05-20 04:42:00 | NOAA-20 | CRISTALÂNDIA | TOCANTINS | Brasil | 1706100 | 17 | 33 | nan | nan | nan | Cerrado | 2.9 |
| b72a9edf-eaea-3535-b9c6-62843e6ab9e8 | -9.95125 | -52.46862 | 2026-05-20 04:42:00 | NOAA-20 | SANTA CRUZ DO XINGU | MATO GROSSO | Brasil | 5107743 | 51 | 33 | nan | nan | nan | Amazônia | 1.3 |
| 9774f490-5e34-39d8-abbf-e30545324045 | -9.88797 | -52.44209 | 2026-05-20 04:42:00 | NOAA-20 | SANTA CRUZ DO XINGU | MATO GROSSO | Brasil | 5107743 | 51 | 33 | nan | nan | nan | Amazônia | 3.8 |
| eaea0862-ad3c-3771-a72a-667707d4bc6e | -8.55379 | -45.98686 | 2026-05-20 04:42:00 | NOAA-20 | TASSO FRAGOSO | MARANHÃO | Brasil | 2112001 | 21 | 33 | nan | nan | nan | Cerrado | 8.4 |
| 2b336ce1-6ac7-3da8-bbce-6572102e26f6 | -8.43468 | -46.92889 | 2026-05-20 04:42:00 | NOAA-20 | CAMPOS LINDOS | TOCANTINS | Brasil | 1703842 | 17 | 33 | nan | nan | nan | Cerrado | 1.6 |
| 69bdbc8d-61ad-3394-8516-18c1001a7ca4 | -11.59902 | -47.10046 | 2026-05-20 04:42:00 | NOAA-20 | PORTO ALEGRE DO TOCANTINS | TOCANTINS | Brasil | 1718006 | 17 | 33 | nan | nan | nan | Cerrado | 1.4 |
| 63784772-3816-3c42-8cae-0bb589a3847f | -8.73275 | -47.97694 | 2026-05-20 04:42:00 | NOAA-20 | SANTA MARIA DO TOCANTINS | TOCANTINS | Brasil | 1718881 | 17 | 33 | nan | nan | nan | Cerrado | 6.8 |
| 451ae2d8-d619-3db0-abf6-9d9d699324d5 | -10.57777 | -46.65622 | 2026-05-20 04:42:00 | NOAA-20 | MATEIROS | TOCANTINS | Brasil | 1712702 | 17 | 33 | nan | nan | nan | Cerrado | 5.0 |
| d2f95c7a-6028-331a-b020-8278d489e99a | -11.04626 | -49.53004 | 2026-05-20 04:42:00 | NOAA-20 | SANTA RITA DO TOCANTINS | TOCANTINS | Brasil | 1718899 | 17 | 33 | nan | nan | nan | Cerrado | 2.6 |
| 989fe178-10d0-30e4-bbb0-a9a2cb42ba28 | -9.2209 | -46.6717 | 2026-05-20 04:42:00 | NOAA-20 | BALSAS | MARANHÃO | Brasil | 2101400 | 21 | 33 | nan | nan | nan | Cerrado | 0.7 |
| 72a3b422-bb82-37cd-b42a-4b3c009afc28 | -8.10415 | -44.12524 | 2026-05-20 04:42:00 | NOAA-20 | SEBASTIÃO LEAL | PIAUÍ | Brasil | 2210631 | 22 | 33 | nan | nan | nan | Cerrado | 1.9 |
| ed24d36a-3d81-33a6-a8bb-55e4a6371d17 | -11.92938 | -43.87044 | 2026-05-20 04:42:00 | NOAA-20 | WANDERLEY | BAHIA | Brasil | 2933455 | 29 | 33 | nan | nan | nan | Cerrado | 3.5 |
| 52e925ef-582f-302c-ae87-84c686f5272d | -11.0174 | -45.1292 | 2026-05-20 04:42:00 | NOAA-20 | FORMOSA DO RIO PRETO | BAHIA | Brasil | 2911105 | 29 | 33 | nan | nan | nan | Cerrado | 3.6 |
| 2a42fcfa-bacd-3e5c-9bbc-31ec54efdae2 | -11.61647 | -55.33018 | 2026-05-20 04:44:00 | NOAA-20 | SINOP | MATO GROSSO | Brasil | 5107909 | 51 | 33 | nan | nan | nan | Amazônia | 3.2 |
| e760b123-8559-35f0-9968-1c66ba530f67 | -10.94274 | -52.68476 | 2026-05-20 04:44:00 | NOAA-20 | SÃO JOSÉ DO XINGU | MATO GROSSO | Brasil | 5107354 | 51 | 33 | nan | nan | nan | Amazônia | 0.8 |
| e2068d08-4bf2-3d6f-a0cd-0003b496fe1d | -11.47327 | -52.91509 | 2026-05-20 04:44:00 | NOAA-20 | SÃO FÉLIX DO ARAGUAIA | MATO GROSSO | Brasil | 5107859 | 51 | 33 | nan | nan | nan | Amazônia | 2.5 |
| f98bef46-aedb-3e01-996d-3de9ac4817c4 | -12.45921 | -54.45308 | 2026-05-20 04:44:00 | NOAA-20 | NOVA UBIRATÃ | MATO GROSSO | Brasil | 5106240 | 51 | 33 | nan | nan | nan | Amazônia | 1.8 |
| db8d71a4-aad2-3f77-beec-e84af4d90572 | -11.45274 | -55.11363 | 2026-05-20 04:44:00 | NOAA-20 | CLÁUDIA | MATO GROSSO | Brasil | 5103056 | 51 | 33 | nan | nan | nan | Amazônia | 2.5 |
| adf11f97-106c-3527-9422-29112a02878c | -11.46914 | -52.91839 | 2026-05-20 04:44:00 | NOAA-20 | SÃO FÉLIX DO ARAGUAIA | MATO GROSSO | Brasil | 5107859 | 51 | 33 | nan | nan | nan | Amazônia | 2.5 |
| ba6463e7-1d50-3800-ab5e-af7d2d842d76 | -11.6086 | -55.32874 | 2026-05-20 04:44:00 | NOAA-20 | SINOP | MATO GROSSO | Brasil | 5107909 | 51 | 33 | nan | nan | nan | Amazônia | 5.9 |
| 8a3cf5b5-2ff2-3a1e-83e9-a3e93cb546ad | -14.15372 | -52.87915 | 2026-05-20 04:44:00 | NOAA-20 | ÁGUA BOA | MATO GROSSO | Brasil | 5100201 | 51 | 33 | nan | nan | nan | Cerrado | 2.7 |
| 91832d3e-2902-31b9-ac8b-7df253fbc978 | -16.06984 | -45.89341 | 2026-05-20 04:44:00 | NOAA-20 | ARINOS | MINAS GERAIS | Brasil | 3104502 | 31 | 33 | nan | nan | nan | Cerrado | 1.2 |
| 8a259421-a07a-3686-a26e-05087065ca11 | -12.06499 | -45.28701 | 2026-05-20 04:44:00 | NOAA-20 | BARREIRAS | BAHIA | Brasil | 2903201 | 29 | 33 | nan | nan | nan | Cerrado | 2.0 |
| ad0dd1a7-9147-399e-9b81-c10c5c5716b8 | -11.94782 | -46.93002 | 2026-05-20 04:44:00 | NOAA-20 | DIANÓPOLIS | TOCANTINS | Brasil | 1707009 | 17 | 33 | nan | nan | nan | Cerrado | 1.9 |
| 3f6dc3f1-d4e4-312c-95f7-7ffcd06c5dbb | -14.15182 | -52.89398 | 2026-05-20 04:44:00 | NOAA-20 | ÁGUA BOA | MATO GROSSO | Brasil | 5100201 | 51 | 33 | nan | nan | nan | Cerrado | 6.9 |
| 628beb74-7ccc-3539-93f9-48f2725b353b | -14.16249 | -45.31255 | 2026-05-20 04:44:00 | NOAA-20 | JABORANDI | BAHIA | Brasil | 2917359 | 29 | 33 | nan | nan | nan | Cerrado | 0.9 |
| 3e84c5ef-0043-302b-ad40-a6e1c02063d1 | -10.03166 | -59.35584 | 2026-05-20 04:44:00 | NOAA-20 | ARIPUANÃ | MATO GROSSO | Brasil | 5101407 | 51 | 33 | nan | nan | nan | Amazônia | 1.5 |
| f7375cf0-f2ea-3cd9-be8c-da124651e2ad | -14.15771 | -52.87963 | 2026-05-20 04:44:00 | NOAA-20 | ÁGUA BOA | MATO GROSSO | Brasil | 5100201 | 51 | 33 | nan | nan | nan | Cerrado | 2.4 |
| cdaecfb6-7da1-327f-ad08-ce3412c4ddd0 | -14.15879 | -45.30798 | 2026-05-20 04:44:00 | NOAA-20 | JABORANDI | BAHIA | Brasil | 2917359 | 29 | 33 | nan | nan | nan | Cerrado | 2.0 |
| 7c279ca1-b0d7-3221-96e1-c8e4380660ec | -14.29148 | -54.59707 | 2026-05-20 04:44:00 | NOAA-20 | PARANATINGA | MATO GROSSO | Brasil | 5106307 | 51 | 33 | nan | nan | nan | Cerrado | 0.9 |
| 2b3b01c1-a759-32ce-98eb-bd0401f1e8b9 | -11.48022 | -52.91629 | 2026-05-20 04:44:00 | NOAA-20 | SÃO FÉLIX DO ARAGUAIA | MATO GROSSO | Brasil | 5107859 | 51 | 33 | nan | nan | nan | Amazônia | 1.8 |
| 577f9b24-9d45-3e6b-8e26-bf920735f933 | -11.45806 | -52.92051 | 2026-05-20 04:44:00 | NOAA-20 | SÃO FÉLIX DO ARAGUAIA | MATO GROSSO | Brasil | 5107859 | 51 | 33 | nan | nan | nan | Amazônia | 1.2 |
| 064b6161-569d-313e-bc60-0eefb0d46473 | -11.61343 | -55.32434 | 2026-05-20 04:44:00 | NOAA-20 | SINOP | MATO GROSSO | Brasil | 5107909 | 51 | 33 | nan | nan | nan | Amazônia | 2.8 |
| a143bb19-2a79-3df7-ab25-0c9b9e92e7c6 | -11.46566 | -52.9178 | 2026-05-20 04:44:00 | NOAA-20 | SÃO FÉLIX DO ARAGUAIA | MATO GROSSO | Brasil | 5107859 | 51 | 33 | nan | nan | nan | Amazônia | 1.5 |
| ca64beb4-8c16-3b69-8332-e0d7ec8c2aa1 | -14.16638 | -52.86955 | 2026-05-20 04:44:00 | NOAA-20 | ÁGUA BOA | MATO GROSSO | Brasil | 5100201 | 51 | 33 | nan | nan | nan | Cerrado | 7.2 |
| ce5e3898-66d1-3b1d-b09d-749dac553d3d | -16.45452 | -51.71602 | 2026-05-20 04:44:00 | NOAA-20 | PIRANHAS | GOIÁS | Brasil | 5217203 | 52 | 33 | nan | nan | nan | Cerrado | 0.6 |
| 2a81b458-41dc-376c-aa62-c58f7c16ba60 | -11.44884 | -55.11293 | 2026-05-20 04:44:00 | NOAA-20 | CLÁUDIA | MATO GROSSO | Brasil | 5103056 | 51 | 33 | nan | nan | nan | Amazônia | 3.1 |
| f55e007a-5e96-3528-a559-b68a585a8b68 | -12.60694 | -44.5187 | 2026-05-20 04:44:00 | NOAA-20 | BAIANÓPOLIS | BAHIA | Brasil | 2902500 | 29 | 33 | nan | nan | nan | Cerrado | 0.9 |
| 5b686aa1-bf12-326a-99eb-5d3c9edb4c4b | -14.91293 | -47.73449 | 2026-05-20 04:44:00 | NOAA-20 | ÁGUA FRIA DE GOIÁS | GOIÁS | Brasil | 5200175 | 52 | 33 | nan | nan | nan | Cerrado | 3.7 |
| 0d2a0374-a6d6-3ff2-bede-a6168998658c | -13.19574 | -43.35585 | 2026-05-20 04:44:00 | NOAA-20 | BOM JESUS DA LAPA | BAHIA | Brasil | 2903904 | 29 | 33 | nan | nan | nan | Caatinga | 1.5 |
| 2258d9b1-eb27-34d9-b4b5-6f3199e2509e | -17.59255 | -46.56306 | 2026-05-20 04:44:00 | NOAA-20 | LAGOA GRANDE | MINAS GERAIS | Brasil | 3137536 | 31 | 33 | nan | nan | nan | Cerrado | 1.2 |
| da683321-4490-305b-bc14-6c1c87e19e4d | -17.10089 | -52.45489 | 2026-05-20 04:44:00 | NOAA-20 | DOVERLÂNDIA | GOIÁS | Brasil | 5207253 | 52 | 33 | nan | nan | nan | Cerrado | 1.1 |
| 9a4a4cbb-6234-374a-b400-9858468ccfd1 | -11.91821 | -54.10204 | 2026-05-20 04:44:00 | NOAA-20 | FELIZ NATAL | MATO GROSSO | Brasil | 5103700 | 51 | 33 | nan | nan | nan | Amazônia | 0.7 |
| 4c8ef485-0af0-32a8-8fc8-87a2936b3b0f | -12.04503 | -55.03836 | 2026-05-20 04:44:00 | NOAA-20 | SANTA CARMEM | MATO GROSSO | Brasil | 5107248 | 51 | 33 | nan | nan | nan | Amazônia | 0.7 |
| 22fc3e7d-0529-3c2d-b2aa-132b8f419b0f | -14.00207 | -47.50319 | 2026-05-20 04:44:00 | NOAA-20 | ALTO PARAÍSO DE GOIÁS | GOIÁS | Brasil | 5200605 | 52 | 33 | nan | nan | nan | Cerrado | 1.2 |
| dfe7677b-ce8a-3801-b97d-343de288386d | -11.92922 | -46.92756 | 2026-05-20 04:44:00 | NOAA-20 | DIANÓPOLIS | TOCANTINS | Brasil | 1707009 | 17 | 33 | nan | nan | nan | Cerrado | 3.2 |
| befff820-3e9f-3b91-b989-6a140264c312 | -14.90924 | -47.73394 | 2026-05-20 04:44:00 | NOAA-20 | ÁGUA FRIA DE GOIÁS | GOIÁS | Brasil | 5200175 | 52 | 33 | nan | nan | nan | Cerrado | 3.7 |
| 2f80e20d-7a54-329a-9dbc-12af3c987e57 | -12.59767 | -44.52168 | 2026-05-20 04:44:00 | NOAA-20 | BAIANÓPOLIS | BAHIA | Brasil | 2902500 | 29 | 33 | nan | nan | nan | Cerrado | 8.6 |
| ecaade25-2f28-359c-81a8-5f8b07bf07e7 | -14.15295 | -45.31949 | 2026-05-20 04:44:00 | NOAA-20 | JABORANDI | BAHIA | Brasil | 2917359 | 29 | 33 | nan | nan | nan | Cerrado | 1.2 |
| c22a8445-1e99-34cd-9246-3ae96a07b5df | -11.61253 | -55.32946 | 2026-05-20 04:44:00 | NOAA-20 | SINOP | MATO GROSSO | Brasil | 5107909 | 51 | 33 | nan | nan | nan | Amazônia | 5.9 |
| 6d5d5fef-6bae-340d-adeb-f58b49b990c8 | -14.15127 | -52.89412 | 2026-05-20 04:44:00 | NOAA-20 | ÁGUA BOA | MATO GROSSO | Brasil | 5100201 | 51 | 33 | nan | nan | nan | Cerrado | 4.8 |
| 108c1da5-96a0-3ba0-978a-1dbe7748bdb0 | -12.60202 | -44.52233 | 2026-05-20 04:44:00 | NOAA-20 | BAIANÓPOLIS | BAHIA | Brasil | 2902500 | 29 | 33 | nan | nan | nan | Cerrado | 8.6 |
| 5441180e-0921-3b91-8518-b0cd97e8fa62 | -11.947 | -49.2989 | 2026-05-20 04:44:00 | NOAA-20 | FORMOSO DO ARAGUAIA | TOCANTINS | Brasil | 1708205 | 17 | 33 | nan | nan | nan | Cerrado | 1.4 |
| 8b7ba1b9-036a-30fd-afe8-2bc5fa534514 | -12.44707 | -44.74786 | 2026-05-20 04:44:00 | NOAA-20 | SÃO DESIDÉRIO | BAHIA | Brasil | 2928901 | 29 | 33 | nan | nan | nan | Cerrado | 0.7 |
| 783c8dcd-1987-3f71-9bf5-6961a06a67c9 | -12.22566 | -46.6044 | 2026-05-20 04:44:00 | NOAA-20 | TAGUATINGA | TOCANTINS | Brasil | 1720903 | 17 | 33 | nan | nan | nan | Cerrado | 1.4 |
| 5938f59b-3638-3b32-9643-4336917dd5d7 | -11.45871 | -52.91661 | 2026-05-20 04:44:00 | NOAA-20 | SÃO FÉLIX DO ARAGUAIA | MATO GROSSO | Brasil | 5107859 | 51 | 33 | nan | nan | nan | Amazônia | 0.8 |
| c2c6f78e-c7e5-309f-a930-ae4ea7d36a3e | -14.15402 | -45.31146 | 2026-05-20 04:44:00 | NOAA-20 | JABORANDI | BAHIA | Brasil | 2917359 | 29 | 33 | nan | nan | nan | Cerrado | 0.8 |
| 7d7169f7-6f1e-3da4-827d-bc07c097f2b7 | -14.15771 | -45.31603 | 2026-05-20 04:44:00 | NOAA-20 | JABORANDI | BAHIA | Brasil | 2917359 | 29 | 33 | nan | nan | nan | Cerrado | 0.9 |
| fb869e6d-a86f-3510-aa9d-385f5d14fadd | -11.60301 | -54.1918 | 2026-05-20 04:44:00 | NOAA-20 | UNIÃO DO SUL | MATO GROSSO | Brasil | 5108303 | 51 | 33 | nan | nan | nan | Amazônia | 2.4 |
| 376374d7-1834-36b5-9e6e-a4daa4516282 | -11.4511 | -52.91932 | 2026-05-20 04:44:00 | NOAA-20 | SÃO FÉLIX DO ARAGUAIA | MATO GROSSO | Brasil | 5107859 | 51 | 33 | nan | nan | nan | Amazônia | 1.3 |
| d43e223d-6378-373a-967d-7d46f7bfb178 | -11.33948 | -51.41292 | 2026-05-20 04:44:00 | NOAA-20 | SÃO FÉLIX DO ARAGUAIA | MATO GROSSO | Brasil | 5107859 | 51 | 33 | nan | nan | nan | Cerrado | 1.0 |
| 15be0bb3-2086-3226-8c1d-5b03cbe37f99 | -12.89596 | -51.87675 | 2026-05-20 04:44:00 | NOAA-20 | RIBEIRÃO CASCALHEIRA | MATO GROSSO | Brasil | 5107180 | 51 | 33 | nan | nan | nan | Amazônia | 0.8 |
| f5a545a9-6133-3d88-ad4d-09bff6f383b7 | -11.31044 | -54.03699 | 2026-05-20 04:44:00 | NOAA-20 | UNIÃO DO SUL | MATO GROSSO | Brasil | 5108303 | 51 | 33 | nan | nan | nan | Amazônia | 0.8 |
| 9d9c59b9-1c90-3f47-a462-1249258cd2e0 | -12.89654 | -51.87315 | 2026-05-20 04:44:00 | NOAA-20 | RIBEIRÃO CASCALHEIRA | MATO GROSSO | Brasil | 5107180 | 51 | 33 | nan | nan | nan | Amazônia | 0.8 |
| 23b8e20d-4985-3dde-a124-ad3d3f47b632 | -13.05765 | -48.30846 | 2026-05-20 04:44:00 | NOAA-20 | PALMEIRÓPOLIS | TOCANTINS | Brasil | 1715754 | 17 | 33 | nan | nan | nan | Cerrado | 0.9 |
| 5030f426-6d49-3e54-8cf1-e041bb16bdca | -11.00147 | -54.00235 | 2026-05-20 04:44:00 | NOAA-20 | MARCELÂNDIA | MATO GROSSO | Brasil | 5105580 | 51 | 33 | nan | nan | nan | Amazônia | 0.6 |
| c4a02c50-ebf7-3145-b6de-9f0d536e38e7 | -14.92943 | -47.75045 | 2026-05-20 04:44:00 | NOAA-20 | ÁGUA FRIA DE GOIÁS | GOIÁS | Brasil | 5200175 | 52 | 33 | nan | nan | nan | Cerrado | 3.2 |
| be07b7d9-0099-387a-9679-d45e868bfd5c | -11.46218 | -52.9172 | 2026-05-20 04:44:00 | NOAA-20 | SÃO FÉLIX DO ARAGUAIA | MATO GROSSO | Brasil | 5107859 | 51 | 33 | nan | nan | nan | Amazônia | 1.5 |
| 0b550907-1b96-3e59-a22d-6e8aa58a6ab6 | -11.94925 | -47.89225 | 2026-05-20 04:44:00 | NOAA-20 | SÃO VALÉRIO | TOCANTINS | Brasil | 1720499 | 17 | 33 | nan | nan | nan | Cerrado | 0.8 |
| f7df2bd2-c6bb-3b13-af74-574db33ae26f | -12.35551 | -45.67695 | 2026-05-20 04:44:00 | NOAA-20 | LUÍS EDUARDO MAGALHÃES | BAHIA | Brasil | 2919553 | 29 | 33 | nan | nan | nan | Cerrado | 0.5 |
| ebad120d-cf20-3688-8689-50fbbfc4604c | -12.22879 | -46.60966 | 2026-05-20 04:44:00 | NOAA-20 | TAGUATINGA | TOCANTINS | Brasil | 1720903 | 17 | 33 | nan | nan | nan | Cerrado | 0.7 |
| 345b2c34-16a5-3f09-b08e-437be77b8766 | -14.90857 | -51.05548 | 2026-05-20 04:44:00 | NOAA-20 | ARUANÃ | GOIÁS | Brasil | 5202502 | 52 | 33 | nan | nan | nan | Cerrado | 0.5 |
| 8512a4e4-a07d-3da5-868e-f00a925b901b | -11.76087 | -48.28514 | 2026-05-20 04:44:00 | NOAA-20 | SÃO VALÉRIO | TOCANTINS | Brasil | 1720499 | 17 | 33 | nan | nan | nan | Cerrado | 0.8 |
| d0de3a16-22ee-3281-864e-94c2c51c2026 | -17.71025 | -42.22653 | 2026-05-20 04:44:00 | NOAA-20 | ANGELÂNDIA | MINAS GERAIS | Brasil | 3102852 | 31 | 33 | nan | nan | nan | Mata Atlântica | 1.3 |
| c37d4f37-9551-3217-8aa0-0bb1fd732a91 | -14.15188 | -52.89036 | 2026-05-20 04:44:00 | NOAA-20 | ÁGUA BOA | MATO GROSSO | Brasil | 5100201 | 51 | 33 | nan | nan | nan | Cerrado | 4.8 |
| 695b3070-96b0-33ba-94aa-6c4718fbbf57 | -11.47675 | -52.91569 | 2026-05-20 04:44:00 | NOAA-20 | SÃO FÉLIX DO ARAGUAIA | MATO GROSSO | Brasil | 5107859 | 51 | 33 | nan | nan | nan | Amazônia | 1.8 |
| cee4d108-4a9e-3966-ba62-5239d0d277f0 | -11.74485 | -54.7943 | 2026-05-20 04:44:00 | NOAA-20 | CLÁUDIA | MATO GROSSO | Brasil | 5103056 | 51 | 33 | nan | nan | nan | Amazônia | 0.8 |
| 075aaa7a-f554-3cfd-a183-38d7b138265e | -13.39037 | -47.09769 | 2026-05-20 04:44:00 | NOAA-20 | MONTE ALEGRE DE GOIÁS | GOIÁS | Brasil | 5213509 | 52 | 33 | nan | nan | nan | Cerrado | 1.1 |
| ba54d22d-6a34-3864-aaf6-96d50f1d9d1f | -14.84218 | -48.51991 | 2026-05-20 04:44:00 | NOAA-20 | NIQUELÂNDIA | GOIÁS | Brasil | 5214606 | 52 | 33 | nan | nan | nan | Cerrado | 1.0 |
| fd7e4a7e-78cf-32e6-8245-b38ed5aeb046 | -12.06088 | -45.28644 | 2026-05-20 04:44:00 | NOAA-20 | BARREIRAS | BAHIA | Brasil | 2903201 | 29 | 33 | nan | nan | nan | Cerrado | 1.1 |
| b50fd6f2-bffd-3a5b-87f1-d81f71a5a7e5 | -10.94339 | -52.68089 | 2026-05-20 04:44:00 | NOAA-20 | SÃO JOSÉ DO XINGU | MATO GROSSO | Brasil | 5107354 | 51 | 33 | nan | nan | nan | Amazônia | 0.8 |
| 2b086f4f-f7ca-3824-b19c-ffefd9ddbec1 | -11.33594 | -51.45629 | 2026-05-20 04:44:00 | NOAA-20 | SÃO FÉLIX DO ARAGUAIA | MATO GROSSO | Brasil | 5107859 | 51 | 33 | nan | nan | nan | Cerrado | 0.4 |
| a2516a28-707d-33d6-963f-ee160c9a521f | -14.85341 | -48.54239 | 2026-05-20 04:44:00 | NOAA-20 | NIQUELÂNDIA | GOIÁS | Brasil | 5214606 | 52 | 33 | nan | nan | nan | Cerrado | 2.2 |
| 6faca270-98d0-340a-8b75-1cf77c382fc6 | -12.44225 | -44.75131 | 2026-05-20 04:44:00 | NOAA-20 | SÃO DESIDÉRIO | BAHIA | Brasil | 2928901 | 29 | 33 | nan | nan | nan | Cerrado | 0.8 |
| 1b98293a-e8f5-3b66-8572-3b05e596b619 | -12.22508 | -44.25727 | 2026-05-20 04:44:00 | NOAA-20 | CRISTÓPOLIS | BAHIA | Brasil | 2909703 | 29 | 33 | nan | nan | nan | Cerrado | 1.8 |
| 554451d4-5989-33bc-afb4-2ed0b3b8633b | -13.58058 | -52.17997 | 2026-05-20 04:44:00 | NOAA-20 | CANARANA | MATO GROSSO | Brasil | 5102702 | 51 | 33 | nan | nan | nan | Cerrado | 1.7 |
| a2a1fc6e-aea8-3840-becb-d9900aebd063 | -14.15825 | -45.31201 | 2026-05-20 04:44:00 | NOAA-20 | JABORANDI | BAHIA | Brasil | 2917359 | 29 | 33 | nan | nan | nan | Cerrado | 0.9 |
| d4ca1e0d-c543-31ba-9438-c51a6b854166 | -14.16049 | -52.88394 | 2026-05-20 04:44:00 | NOAA-20 | ÁGUA BOA | MATO GROSSO | Brasil | 5100201 | 51 | 33 | nan | nan | nan | Cerrado | 1.0 |
| bd303c0b-2a16-3944-af44-6e086ea7c5c6 | -16.14838 | -51.72015 | 2026-05-20 04:44:00 | NOAA-20 | ARENÓPOLIS | GOIÁS | Brasil | 5202353 | 52 | 33 | nan | nan | nan | Cerrado | 1.5 |
| d555f1cb-6fc2-3f9d-a396-84ea115d47f9 | -11.63874 | -58.2533 | 2026-05-20 04:44:00 | NOAA-20 | BRASNORTE | MATO GROSSO | Brasil | 5101902 | 51 | 33 | nan | nan | nan | Amazônia | 2.1 |
| 449369c6-2ba7-3c64-9f48-a89b217228e9 | -14.1645 | -52.88081 | 2026-05-20 04:44:00 | NOAA-20 | ÁGUA BOA | MATO GROSSO | Brasil | 5100201 | 51 | 33 | nan | nan | nan | Cerrado | 1.0 |
| 0b18c1d8-ab74-3ade-bfa2-512cdc868f16 | -12.22623 | -44.24862 | 2026-05-20 04:44:00 | NOAA-20 | CRISTÓPOLIS | BAHIA | Brasil | 2909703 | 29 | 33 | nan | nan | nan | Cerrado | 2.5 |
| a78f5d41-0174-31ce-864a-b28933a4c843 | -11.00222 | -53.99791 | 2026-05-20 04:44:00 | NOAA-20 | MARCELÂNDIA | MATO GROSSO | Brasil | 5105580 | 51 | 33 | nan | nan | nan | Amazônia | 1.2 |
| 7a99b27a-3d99-34bc-aa75-0fbad4e844fe | -13.51361 | -47.68753 | 2026-05-20 04:44:00 | NOAA-20 | CAVALCANTE | GOIÁS | Brasil | 5205307 | 52 | 33 | nan | nan | nan | Cerrado | 0.9 |
| 1f987b08-0084-3fe9-b086-5efee111cbd8 | -12.45996 | -54.44866 | 2026-05-20 04:44:00 | NOAA-20 | NOVA UBIRATÃ | MATO GROSSO | Brasil | 5106240 | 51 | 33 | nan | nan | nan | Amazônia | 1.9 |
| bf2481ab-27b3-310e-b621-b2e422c07de6 | -14.15431 | -52.87904 | 2026-05-20 04:44:00 | NOAA-20 | ÁGUA BOA | MATO GROSSO | Brasil | 5100201 | 51 | 33 | nan | nan | nan | Cerrado | 2.4 |
| 4f21cdb7-b776-31e6-88b9-4fa41b21c07b | -16.45395 | -51.7196 | 2026-05-20 04:44:00 | NOAA-20 | PIRANHAS | GOIÁS | Brasil | 5217203 | 52 | 33 | nan | nan | nan | Cerrado | 1.0 |
| 614afd16-c7da-3e80-9da0-392a5a7a7f38 | -14.15348 | -45.31548 | 2026-05-20 04:44:00 | NOAA-20 | JABORANDI | BAHIA | Brasil | 2917359 | 29 | 33 | nan | nan | nan | Cerrado | 0.8 |


[Clique aqui para ver as próximas entradas](README8.md)
