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

## Dados Diários - Página 18

| ID | Latitude | Longitude | Data/Hora GMT | Satélite | Município | Estado | País | Município ID | Estado ID | País ID | Dias sem Chuva | Precipitação | Risco de Fogo | Bioma | FRP |
|----|----------|-----------|---------------|----------|-----------|--------|------|--------------|-----------|---------|----------------|--------------|----------------|-------|-----|
| 1a67efe1-c433-36d7-ab74-eea90df30598 | -3.98654 | -47.88489 | 2025-10-23 04:36:00 | NPP-375D | ULIANÓPOLIS | PARÁ | Brasil | 1508126 | 15 | 33 | nan | nan | nan | Amazônia | 2.7 |
| f8fcf2c3-55e5-37ae-898d-d7265c2ca9f4 | -2.85521 | -50.73818 | 2025-10-23 04:36:00 | NPP-375D | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 1.5 |
| 753ebedc-77ef-3fa5-be75-426731dc6b20 | -5.81454 | -50.2009 | 2025-10-23 04:36:00 | NPP-375D | MARABÁ | PARÁ | Brasil | 1504208 | 15 | 33 | nan | nan | nan | Amazônia | 0.5 |
| 9965238a-f5b6-3f14-9f64-ede69f89715d | -5.93013 | -47.32117 | 2025-10-23 04:36:00 | NPP-375D | RIBAMAR FIQUENE | MARANHÃO | Brasil | 2109551 | 21 | 33 | nan | nan | nan | Cerrado | 1.5 |
| 1a8553af-647e-348c-a8bb-37983b2ab6a4 | -3.01645 | -49.45108 | 2025-10-23 04:36:00 | NPP-375D | MOJU | PARÁ | Brasil | 1504703 | 15 | 33 | nan | nan | nan | Amazônia | 10.4 |
| 32e7c21a-0fde-3b24-a4e3-6f95149ab73a | -5.5833 | -41.3181 | 2025-10-23 04:36:00 | NPP-375D | SÃO MIGUEL DO TAPUIO | PIAUÍ | Brasil | 2210409 | 22 | 33 | nan | nan | nan | Caatinga | 1.0 |
| 33b60fc1-c636-318e-8c42-25b5892fc1bc | -3.79863 | -48.99391 | 2025-10-23 04:36:00 | NPP-375D | GOIANÉSIA DO PARÁ | PARÁ | Brasil | 1503093 | 15 | 33 | nan | nan | nan | Amazônia | 0.7 |
| b7c14614-bfd0-35dc-8a42-6556750304a6 | -7.07975 | -44.6521 | 2025-10-23 04:36:00 | NPP-375D | BENEDITO LEITE | MARANHÃO | Brasil | 2101806 | 21 | 33 | nan | nan | nan | Cerrado | 2.6 |
| 8bc8e331-3e6e-3003-9265-494c06347345 | -5.37217 | -46.86918 | 2025-10-23 04:36:00 | NPP-375D | AMARANTE DO MARANHÃO | MARANHÃO | Brasil | 2100600 | 21 | 33 | nan | nan | nan | Cerrado | 2.1 |
| f4a13b74-3bde-33ba-8ccc-712de0dc7776 | -4.19911 | -48.36221 | 2025-10-23 04:36:00 | NPP-375D | RONDON DO PARÁ | PARÁ | Brasil | 1506187 | 15 | 33 | nan | nan | nan | Amazônia | 0.7 |
| 0def466c-ee23-3d2b-a7f1-ff8ef1413e91 | -2.85893 | -50.73876 | 2025-10-23 04:36:00 | NPP-375D | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 1.5 |
| 917f4c61-cabf-3db3-9c3e-ab3c9fc2fd59 | -6.32391 | -43.62732 | 2025-10-23 04:36:00 | NPP-375D | SUCUPIRA DO RIACHÃO | MARANHÃO | Brasil | 2111953 | 21 | 33 | nan | nan | nan | Cerrado | 5.5 |
| c4bc58f0-460b-3b41-b3e5-a72ef65cbb4c | -3.67642 | -47.62614 | 2025-10-23 04:36:00 | NPP-375D | ULIANÓPOLIS | PARÁ | Brasil | 1508126 | 15 | 33 | nan | nan | nan | Amazônia | 3.9 |
| 5fa0faff-9987-3d54-9727-e43af1d815b2 | -3.05042 | -50.26302 | 2025-10-23 04:36:00 | NPP-375D | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 1.3 |
| 1afd7342-fd34-338b-a089-b3079d82a03b | -3.32474 | -48.70383 | 2025-10-23 04:36:00 | NPP-375D | IPIXUNA DO PARÁ | PARÁ | Brasil | 1503457 | 15 | 33 | nan | nan | nan | Amazônia | 0.7 |
| 6cc4a0c9-8f2f-3d14-85f8-b79a86e50443 | -6.28253 | -47.01057 | 2025-10-23 04:36:00 | NPP-375D | SÃO JOÃO DO PARAÍSO | MARANHÃO | Brasil | 2111052 | 21 | 33 | nan | nan | nan | Cerrado | 1.1 |
| 76b65013-02d0-3d02-a0e9-8a594922039f | -6.32519 | -43.74881 | 2025-10-23 04:36:00 | NPP-375D | SÃO JOÃO DOS PATOS | MARANHÃO | Brasil | 2111102 | 21 | 33 | nan | nan | nan | Cerrado | 1.1 |
| e65ee537-d5fe-3a17-a89e-18fe7145b505 | -7.80925 | -44.00443 | 2025-10-23 04:36:00 | NPP-375D | SEBASTIÃO LEAL | PIAUÍ | Brasil | 2210631 | 22 | 33 | nan | nan | nan | Cerrado | 0.8 |
| 2ec207aa-7849-3e66-bd5b-794a5526a419 | -7.03374 | -45.53907 | 2025-10-23 04:36:00 | NPP-375D | SÃO RAIMUNDO DAS MANGABEIRAS | MARANHÃO | Brasil | 2111607 | 21 | 33 | nan | nan | nan | Cerrado | 1.7 |
| 2328705d-8cb3-3516-994c-1baa37b0f878 | -3.59946 | -48.99268 | 2025-10-23 04:36:00 | NPP-375D | GOIANÉSIA DO PARÁ | PARÁ | Brasil | 1503093 | 15 | 33 | nan | nan | nan | Amazônia | 1.0 |
| ff30357b-d628-3769-bd0e-19060caa5bf4 | -7.08506 | -46.19507 | 2025-10-23 04:36:00 | NPP-375D | NOVA COLINAS | MARANHÃO | Brasil | 2107258 | 21 | 33 | nan | nan | nan | Cerrado | 5.8 |
| 28ec05a8-c5fe-3a5f-99ee-de77647d1c12 | -7.14833 | -42.36744 | 2025-10-23 04:36:00 | NPP-375D | OEIRAS | PIAUÍ | Brasil | 2207009 | 22 | 33 | nan | nan | nan | Caatinga | 1.4 |
| 3c45e50f-3c62-3f2d-adc8-a093068d85ca | -5.68994 | -45.96997 | 2025-10-23 04:36:00 | NPP-375D | GRAJAÚ | MARANHÃO | Brasil | 2104800 | 21 | 33 | nan | nan | nan | Cerrado | 5.5 |
| bcec93bc-1f93-3d70-888a-940ab6ce80c5 | -3.39865 | -51.50155 | 2025-10-23 04:36:00 | NPP-375D | ANAPU | PARÁ | Brasil | 1500859 | 15 | 33 | nan | nan | nan | Amazônia | 1.1 |
| a547dc20-c921-3deb-ba0b-8880721bff8b | -2.80919 | -50.27505 | 2025-10-23 04:36:00 | NPP-375D | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 1.5 |
| b5719db2-5a2b-3ca3-a979-f6b299f84e12 | -3.25762 | -49.12114 | 2025-10-23 04:36:00 | NPP-375D | MOJU | PARÁ | Brasil | 1504703 | 15 | 33 | nan | nan | nan | Amazônia | 0.9 |
| 2947a4da-ab84-3993-944a-ceaf54ff9a5e | -7.12983 | -45.50115 | 2025-10-23 04:36:00 | NPP-375D | SÃO RAIMUNDO DAS MANGABEIRAS | MARANHÃO | Brasil | 2111607 | 21 | 33 | nan | nan | nan | Cerrado | 1.3 |
| ec115026-b6ee-37ad-8733-337f2e61896b | -3.02261 | -49.47963 | 2025-10-23 04:36:00 | NPP-375D | MOJU | PARÁ | Brasil | 1504703 | 15 | 33 | nan | nan | nan | Amazônia | 14.0 |
| 205aefd0-a22e-3687-bced-8f530d4e539d | -4.27625 | -50.54636 | 2025-10-23 04:36:00 | NPP-375D | NOVO REPARTIMENTO | PARÁ | Brasil | 1505064 | 15 | 33 | nan | nan | nan | Amazônia | 2.7 |
| 2dd6a8f6-e701-3d66-a1e1-b4143dae42b4 | -3.94803 | -49.35031 | 2025-10-23 04:36:00 | NPP-375D | BREU BRANCO | PARÁ | Brasil | 1501782 | 15 | 33 | nan | nan | nan | Amazônia | 0.6 |
| 48132fd6-7b3e-3aab-8da4-3801c414240c | -3.10912 | -51.20373 | 2025-10-23 04:36:00 | NPP-375D | ANAPU | PARÁ | Brasil | 1500859 | 15 | 33 | nan | nan | nan | Amazônia | 0.8 |
| 9d691045-d399-3786-b716-01f327178572 | -6.10141 | -46.24259 | 2025-10-23 04:36:00 | NPP-375D | GRAJAÚ | MARANHÃO | Brasil | 2104800 | 21 | 33 | nan | nan | nan | Cerrado | 1.4 |
| cbf70d85-bf53-3e5d-9845-659fb0726305 | -7.06738 | -47.36323 | 2025-10-23 04:36:00 | NPP-375D | CAROLINA | MARANHÃO | Brasil | 2102804 | 21 | 33 | nan | nan | nan | Cerrado | 2.7 |
| c2e0c26e-ae26-3109-baf2-cc5fd86dd2e7 | -7.17154 | -44.78745 | 2025-10-23 04:36:00 | NPP-375D | SÃO FÉLIX DE BALSAS | MARANHÃO | Brasil | 2110807 | 21 | 33 | nan | nan | nan | Cerrado | 3.5 |
| 1b8fd9f5-f785-3c13-ac44-60a032edc16a | -7.2782 | -49.98949 | 2025-10-23 04:36:00 | NPP-375D | RIO MARIA | PARÁ | Brasil | 1506161 | 15 | 33 | nan | nan | nan | Amazônia | 1.7 |
| 32b9a37c-7ba6-3cb5-a548-2934bae496f5 | -7.26379 | -46.17198 | 2025-10-23 04:36:00 | NPP-375D | BALSAS | MARANHÃO | Brasil | 2101400 | 21 | 33 | nan | nan | nan | Cerrado | 1.0 |
| 992a296b-db79-336e-bbeb-62097f0c6275 | -7.5141 | -46.87658 | 2025-10-23 04:36:00 | NPP-375D | RIACHÃO | MARANHÃO | Brasil | 2109502 | 21 | 33 | nan | nan | nan | Cerrado | 0.6 |
| 863c7dc6-cadc-39f7-ac4c-5c77717b178a | -8.35186 | -46.18245 | 2025-10-23 04:36:00 | NPP-375D | BALSAS | MARANHÃO | Brasil | 2101400 | 21 | 33 | nan | nan | nan | Cerrado | 3.2 |
| ea5c5645-c903-349d-9672-77c407867b32 | -4.53312 | -40.68576 | 2025-10-23 04:36:00 | NPP-375D | IPUEIRAS | CEARÁ | Brasil | 2305902 | 23 | 33 | nan | nan | nan | Caatinga | 0.7 |
| fc0c1e7e-e3a4-3e57-b1ce-1edab5c58d18 | -3.79836 | -48.99337 | 2025-10-23 04:36:00 | NPP-375D | GOIANÉSIA DO PARÁ | PARÁ | Brasil | 1503093 | 15 | 33 | nan | nan | nan | Amazônia | 0.7 |
| 447d6cc6-8371-3afa-a938-c1120d564d5b | -7.76451 | -46.19979 | 2025-10-23 04:36:00 | NPP-375D | BALSAS | MARANHÃO | Brasil | 2101400 | 21 | 33 | nan | nan | nan | Cerrado | 1.4 |
| 17b1ec4b-ec12-32bc-ba26-a3a281df984c | -3.95148 | -49.35084 | 2025-10-23 04:36:00 | NPP-375D | BREU BRANCO | PARÁ | Brasil | 1501782 | 15 | 33 | nan | nan | nan | Amazônia | 0.6 |
| ae312711-a344-3167-8d02-8046b74bc860 | -3.04627 | -49.51103 | 2025-10-23 04:36:00 | NPP-375D | MOJU | PARÁ | Brasil | 1504703 | 15 | 33 | nan | nan | nan | Amazônia | 2.5 |
| a605837b-e711-3c7c-9c67-43482fa5c2da | -3.41777 | -50.36461 | 2025-10-23 04:36:00 | NPP-375D | PACAJÁ | PARÁ | Brasil | 1505486 | 15 | 33 | nan | nan | nan | Amazônia | 1.0 |
| 74799ab0-fdca-32aa-995d-d75ddffebff8 | -5.32479 | -48.1783 | 2025-10-23 04:36:00 | NPP-375D | BURITI DO TOCANTINS | TOCANTINS | Brasil | 1703800 | 17 | 33 | nan | nan | nan | Amazônia | 5.0 |
| 0550cb04-339e-3b45-a6cc-fc00e17f41de | -6.78889 | -45.4441 | 2025-10-23 04:36:00 | NPP-375D | SÃO RAIMUNDO DAS MANGABEIRAS | MARANHÃO | Brasil | 2111607 | 21 | 33 | nan | nan | nan | Cerrado | 1.1 |
| 0a97b8fa-b364-3b9d-b67d-d179bcb46e27 | -7.51692 | -46.88069 | 2025-10-23 04:36:00 | NPP-375D | RIACHÃO | MARANHÃO | Brasil | 2109502 | 21 | 33 | nan | nan | nan | Cerrado | 1.5 |
| b05fa173-f247-36f9-b423-8db886a5c22d | -3.05374 | -50.26063 | 2025-10-23 04:36:00 | NPP-375D | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 0.9 |
| 9e13fcc1-1439-352d-9c6a-9a047215dfa6 | -3.99941 | -43.2834 | 2025-10-23 04:36:00 | NPP-375D | CHAPADINHA | MARANHÃO | Brasil | 2103208 | 21 | 33 | nan | nan | nan | Cerrado | 1.8 |
| 225f1d2f-d5bb-3864-81d2-3ec8f7f06323 | -7.80826 | -44.00259 | 2025-10-23 04:36:00 | NPP-375D | SEBASTIÃO LEAL | PIAUÍ | Brasil | 2210631 | 22 | 33 | nan | nan | nan | Cerrado | 1.1 |
| a11dbe73-cb72-380e-81f8-90e008c279be | -5.93067 | -47.31768 | 2025-10-23 04:36:00 | NPP-375D | RIBAMAR FIQUENE | MARANHÃO | Brasil | 2109551 | 21 | 33 | nan | nan | nan | Cerrado | 0.5 |
| fbc7e599-b896-33c4-8b63-ac1258aa09eb | -3.15138 | -50.16491 | 2025-10-23 04:36:00 | NPP-375D | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 1.6 |
| 397b2225-1309-30eb-987d-db56e65922cb | -3.99559 | -43.28282 | 2025-10-23 04:36:00 | NPP-375D | CHAPADINHA | MARANHÃO | Brasil | 2103208 | 21 | 33 | nan | nan | nan | Cerrado | 1.8 |
| 69e88080-e604-3a45-926b-b045cb92461b | -2.87444 | -54.86768 | 2025-10-23 04:36:00 | NPP-375D | BELTERRA | PARÁ | Brasil | 1501451 | 15 | 33 | nan | nan | nan | Amazônia | 2.9 |
| a6fb6722-9e35-3f65-ac0a-76b35480ae1d | -7.8413 | -45.38493 | 2025-10-23 04:36:00 | NPP-375D | RIBEIRO GONÇALVES | PIAUÍ | Brasil | 2208908 | 22 | 33 | nan | nan | nan | Cerrado | 0.9 |
| bc01cd6d-5637-38f2-8b42-9fdd4c122981 | -4.78517 | -42.97389 | 2025-10-23 04:36:00 | NPP-375D | CAXIAS | MARANHÃO | Brasil | 2103000 | 21 | 33 | nan | nan | nan | Cerrado | 1.5 |
| f66515fd-dfef-3dba-9ef4-7307e6480dba | -3.51924 | -52.82917 | 2025-10-23 04:36:00 | NPP-375D | MEDICILÂNDIA | PARÁ | Brasil | 1504455 | 15 | 33 | nan | nan | nan | Amazônia | 1.3 |
| 96e7a5d3-9101-36ab-9bb4-8f85681a892a | -5.03517 | -50.58429 | 2025-10-23 04:36:00 | NPP-375D | NOVO REPARTIMENTO | PARÁ | Brasil | 1505064 | 15 | 33 | nan | nan | nan | Amazônia | 0.5 |
| 18ac3020-4fb6-35c4-a658-fb7df93403ba | -6.90694 | -46.13036 | 2025-10-23 04:36:00 | NPP-375D | FORTALEZA DOS NOGUEIRAS | MARANHÃO | Brasil | 2104107 | 21 | 33 | nan | nan | nan | Cerrado | 1.9 |
| 0a4a39c1-20d0-3dd4-bef2-97b61daa6360 | -2.87534 | -54.86234 | 2025-10-23 04:36:00 | NPP-375D | BELTERRA | PARÁ | Brasil | 1501451 | 15 | 33 | nan | nan | nan | Amazônia | 2.2 |
| ea11098f-762e-3b95-b7ac-f7a504259579 | -3.59748 | -49.85372 | 2025-10-23 04:36:00 | NPP-375D | BAIÃO | PARÁ | Brasil | 1501204 | 15 | 33 | nan | nan | nan | Amazônia | 0.5 |
| 11733ab5-ef24-34f7-a71c-e9494c7dfa0c | -6.48382 | -47.50077 | 2025-10-23 04:36:00 | NPP-375D | AGUIARNÓPOLIS | TOCANTINS | Brasil | 1700301 | 17 | 33 | nan | nan | nan | Cerrado | 0.7 |
| 60357c55-6941-35ff-9fde-647e3395407c | -3.01851 | -49.48291 | 2025-10-23 04:36:00 | NPP-375D | MOJU | PARÁ | Brasil | 1504703 | 15 | 33 | nan | nan | nan | Amazônia | 14.0 |
| 54dfca2b-38e8-381c-9152-cd76e5df6521 | -2.90217 | -49.39832 | 2025-10-23 04:36:00 | NPP-375D | MOJU | PARÁ | Brasil | 1504703 | 15 | 33 | nan | nan | nan | Amazônia | 1.1 |
| 31f143d7-324e-34da-8c2e-fb4893be002f | -6.96801 | -46.00912 | 2025-10-23 04:36:00 | NPP-375D | FORTALEZA DOS NOGUEIRAS | MARANHÃO | Brasil | 2104107 | 21 | 33 | nan | nan | nan | Cerrado | 1.2 |
| c25c73a0-309c-3ade-83af-de9677de2801 | -5.03451 | -50.58842 | 2025-10-23 04:36:00 | NPP-375D | NOVO REPARTIMENTO | PARÁ | Brasil | 1505064 | 15 | 33 | nan | nan | nan | Amazônia | 0.6 |
| 5d601267-1df0-3a07-9b82-23b32817277b | -7.0062 | -46.99593 | 2025-10-23 04:36:00 | NPP-375D | ESTREITO | MARANHÃO | Brasil | 2104057 | 21 | 33 | nan | nan | nan | Cerrado | 2.2 |
| 766a8b41-c589-3681-8d4f-4bb8c870c0db | -6.01372 | -43.32489 | 2025-10-23 04:36:00 | NPP-375D | LAGOA DO MATO | MARANHÃO | Brasil | 2105922 | 21 | 33 | nan | nan | nan | Caatinga | 2.1 |
| 1d5fd3fb-3bea-3bf0-8b8d-47fcbe87927f | -6.60494 | -44.21763 | 2025-10-23 04:36:00 | NPP-375D | PASTOS BONS | MARANHÃO | Brasil | 2108009 | 21 | 33 | nan | nan | nan | Cerrado | 5.3 |
| 1bff5bd2-fe7d-39d3-bdae-75e4efb39c61 | -5.36827 | -46.87218 | 2025-10-23 04:36:00 | NPP-375D | AMARANTE DO MARANHÃO | MARANHÃO | Brasil | 2100600 | 21 | 33 | nan | nan | nan | Cerrado | 2.1 |
| 89ea5982-af81-378c-a281-68849dd1b302 | -3.04505 | -49.51871 | 2025-10-23 04:36:00 | NPP-375D | MOJU | PARÁ | Brasil | 1504703 | 15 | 33 | nan | nan | nan | Amazônia | 1.0 |
| f1fec75d-23ce-3e68-86f5-128a05bf081a | -7.2776 | -49.99321 | 2025-10-23 04:36:00 | NPP-375D | RIO MARIA | PARÁ | Brasil | 1506161 | 15 | 33 | nan | nan | nan | Amazônia | 2.4 |
| ab8d639a-d5ee-3eda-a99c-982a8226a48b | -2.91393 | -48.67313 | 2025-10-23 04:36:00 | NPP-375D | TAILÂNDIA | PARÁ | Brasil | 1507953 | 15 | 33 | nan | nan | nan | Amazônia | 0.7 |
| 1e14594b-486b-36aa-b293-8de12b5f0892 | -2.86265 | -50.73936 | 2025-10-23 04:36:00 | NPP-375D | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 1.3 |
| 86a5a4f3-7ce2-378e-961c-5fb24894c5c6 | -2.92702 | -48.3006 | 2025-10-23 04:36:00 | NPP-375D | TOMÉ-AÇU | PARÁ | Brasil | 1508001 | 15 | 33 | nan | nan | nan | Amazônia | 0.7 |
| 97f9d4e8-5280-3915-946c-23baf794dde9 | -5.8857 | -46.28398 | 2025-10-23 04:36:00 | NPP-375D | GRAJAÚ | MARANHÃO | Brasil | 2104800 | 21 | 33 | nan | nan | nan | Cerrado | 0.6 |
| 47ef58a1-94d2-347a-b21b-471597243f52 | -2.87129 | -50.7167 | 2025-10-23 04:36:00 | NPP-375D | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 1.4 |
| 3a18a46a-1fa3-38f1-899f-a3fb05184bed | -7.62946 | -42.19592 | 2025-10-23 04:36:00 | NPP-375D | SIMPLÍCIO MENDES | PIAUÍ | Brasil | 2210805 | 22 | 33 | nan | nan | nan | Caatinga | 1.2 |
| 4264bd8e-101a-301b-9378-818edc438c5a | -5.47257 | -47.13523 | 2025-10-23 04:36:00 | NPP-375D | BURITIRANA | MARANHÃO | Brasil | 2102358 | 21 | 33 | nan | nan | nan | Cerrado | 1.1 |
| 2ed1146a-e9d9-3d7b-bfe4-3c9d034eff6e | -2.79787 | -48.94022 | 2025-10-23 04:36:00 | NPP-375D | TAILÂNDIA | PARÁ | Brasil | 1507953 | 15 | 33 | nan | nan | nan | Amazônia | 0.8 |
| 3bdb5696-3142-341c-a786-60ed0cbca3a6 | -3.67588 | -47.6296 | 2025-10-23 04:36:00 | NPP-375D | ULIANÓPOLIS | PARÁ | Brasil | 1508126 | 15 | 33 | nan | nan | nan | Amazônia | 3.9 |
| db906d32-3971-3ec2-9706-91d16b265a55 | -5.84641 | -43.64781 | 2025-10-23 04:36:00 | NPP-375D | LAGOA DO MATO | MARANHÃO | Brasil | 2105922 | 21 | 33 | nan | nan | nan | Cerrado | 1.3 |
| 0c029f3a-66b1-3232-9ad6-1ab6c3c43129 | -2.80915 | -54.38194 | 2025-10-23 04:36:00 | NPP-375D | MOJUÍ DOS CAMPOS | PARÁ | Brasil | 1504752 | 15 | 33 | nan | nan | nan | Amazônia | 3.5 |
| 4ac948c0-fd87-394b-af96-56fd3125b915 | -3.1115 | -51.2064 | 2025-10-23 04:36:00 | NPP-375D | ANAPU | PARÁ | Brasil | 1500859 | 15 | 33 | nan | nan | nan | Amazônia | 1.3 |
| 5c282bef-6e8d-36b5-abec-389c9f8802aa | -6.81296 | -44.00951 | 2025-10-23 04:36:00 | NPP-375D | PORTO ALEGRE DO PIAUÍ | PIAUÍ | Brasil | 2208551 | 22 | 33 | nan | nan | nan | Cerrado | 1.7 |
| 085e6fe1-91d7-3fce-bcf6-cbc527cfc413 | -9.62514 | -40.33709 | 2025-10-23 04:36:00 | NPP-375D | JUAZEIRO | BAHIA | Brasil | 2918407 | 29 | 33 | nan | nan | nan | Caatinga | 4.6 |
| ae6d46bb-979a-3f57-9955-385e94b12181 | -7.79216 | -44.00502 | 2025-10-23 04:36:00 | NPP-375D | SEBASTIÃO LEAL | PIAUÍ | Brasil | 2210631 | 22 | 33 | nan | nan | nan | Cerrado | 1.4 |
| b737d853-3a88-382f-895a-0a9c149ca330 | -9.23421 | -45.60127 | 2025-10-23 04:36:00 | NPP-375D | SANTA FILOMENA | PIAUÍ | Brasil | 2209203 | 22 | 33 | nan | nan | nan | Cerrado | 2.4 |
| 746cd55b-705e-3065-bf17-378a7dbf959d | -2.87357 | -50.71856 | 2025-10-23 04:36:00 | NPP-375D | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 1.5 |
| cbaec746-fbb8-3a1c-887c-75860bba39c6 | -3.14912 | -49.4758 | 2025-10-23 04:36:00 | NPP-375D | MOJU | PARÁ | Brasil | 1504703 | 15 | 33 | nan | nan | nan | Amazônia | 0.6 |
| 01b7b75a-49ad-312b-acfb-c85209a5444f | -7.06178 | -44.09609 | 2025-10-23 04:36:00 | NPP-375D | PORTO ALEGRE DO PIAUÍ | PIAUÍ | Brasil | 2208551 | 22 | 33 | nan | nan | nan | Cerrado | 2.3 |
| cbc23c31-b472-3e9a-b05e-63dbe05b75a7 | -6.96931 | -43.98985 | 2025-10-23 04:36:00 | NPP-375D | PORTO ALEGRE DO PIAUÍ | PIAUÍ | Brasil | 2208551 | 22 | 33 | nan | nan | nan | Cerrado | 1.0 |
| d51624f4-dbad-3047-b7bc-4c3304280b9f | -3.73665 | -51.37448 | 2025-10-23 04:36:00 | NPP-375D | ANAPU | PARÁ | Brasil | 1500859 | 15 | 33 | nan | nan | nan | Amazônia | 2.2 |
| adbc933d-6bad-3823-aea7-4bf61fa73bb9 | -5.55872 | -47.01637 | 2025-10-23 04:36:00 | NPP-375D | BURITIRANA | MARANHÃO | Brasil | 2102358 | 21 | 33 | nan | nan | nan | Cerrado | 1.2 |
| 7d759600-e6ff-3f78-b846-ae5fd2289a6e | -6.30687 | -41.88049 | 2025-10-23 04:36:00 | NPP-375D | VALENÇA DO PIAUÍ | PIAUÍ | Brasil | 2211308 | 22 | 33 | nan | nan | nan | Caatinga | 1.1 |
| 80380f8b-e7d1-3516-bd5c-5828bea7cfda | -3.84833 | -48.15992 | 2025-10-23 04:36:00 | NPP-375D | DOM ELISEU | PARÁ | Brasil | 1502939 | 15 | 33 | nan | nan | nan | Amazônia | 1.2 |
| 705ddff3-1b22-3a3f-ad90-4f45e359cac9 | -7.27922 | -44.2143 | 2025-10-23 04:36:00 | NPP-375D | ANTÔNIO ALMEIDA | PIAUÍ | Brasil | 2200806 | 22 | 33 | nan | nan | nan | Cerrado | 1.2 |
| 4dae4fd9-727f-3d27-867d-7c314e3c605a | -6.91038 | -46.13089 | 2025-10-23 04:36:00 | NPP-375D | FORTALEZA DOS NOGUEIRAS | MARANHÃO | Brasil | 2104107 | 21 | 33 | nan | nan | nan | Cerrado | 1.1 |
| e1f4eae9-a430-3a67-84fb-be88f13b0c6c | -5.28866 | -50.56772 | 2025-10-23 04:36:00 | NPP-375D | MARABÁ | PARÁ | Brasil | 1504208 | 15 | 33 | nan | nan | nan | Amazônia | 2.6 |
| f8fb5cc2-e9fa-3544-aa07-b5bb3b6bf4ad | -3.47879 | -50.07649 | 2025-10-23 04:36:00 | NPP-375D | PACAJÁ | PARÁ | Brasil | 1505486 | 15 | 33 | nan | nan | nan | Amazônia | 3.7 |


[Clique aqui para ver as próximas entradas](README19.md)
