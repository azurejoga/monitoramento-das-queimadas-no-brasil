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

## Dados Diários - Página 11

| ID | Latitude | Longitude | Data/Hora GMT | Satélite | Município | Estado | País | Município ID | Estado ID | País ID | Dias sem Chuva | Precipitação | Risco de Fogo | Bioma | FRP |
|----|----------|-----------|---------------|----------|-----------|--------|------|--------------|-----------|---------|----------------|--------------|----------------|-------|-----|
| f960acbe-9816-38de-8aeb-94567b0ad191 | -4.0118 | -48.06323 | 2026-07-31 05:14:00 | NPP-375D | DOM ELISEU | PARÁ | Brasil | 1502939 | 15 | 33 | nan | nan | nan | Amazônia | 1.2 |
| bec93145-1b4c-3807-82a8-ae8d5134dab8 | -4.90593 | -43.47637 | 2026-07-31 05:14:00 | NPP-375D | CAXIAS | MARANHÃO | Brasil | 2103000 | 21 | 33 | nan | nan | nan | Cerrado | 1.8 |
| 83297929-757d-34cc-b9eb-0ee945dc3a42 | -3.168 | -48.13493 | 2026-07-31 05:14:00 | NPP-375D | IPIXUNA DO PARÁ | PARÁ | Brasil | 1503457 | 15 | 33 | nan | nan | nan | Amazônia | 1.1 |
| d690765e-af68-34d8-a661-1229c605c931 | -0.19856 | -60.76865 | 2026-07-31 05:14:00 | NPP-375D | RORAINÓPOLIS | RORAIMA | Brasil | 1400472 | 14 | 33 | nan | nan | nan | Amazônia | 0.8 |
| a1a6144d-1649-3017-b6c6-d629ac573d0c | -3.05071 | -48.74686 | 2026-07-31 05:14:00 | NPP-375D | TAILÂNDIA | PARÁ | Brasil | 1507953 | 15 | 33 | nan | nan | nan | Amazônia | 3.6 |
| eb9d570b-595f-3dff-86b6-76d3b6908637 | -4.27584 | -48.1917 | 2026-07-31 05:14:00 | NPP-375D | RONDON DO PARÁ | PARÁ | Brasil | 1506187 | 15 | 33 | nan | nan | nan | Amazônia | 2.9 |
| f984bdb6-ba73-36e7-92ca-5aea69afb8c7 | 1.10142 | -60.50539 | 2026-07-31 05:14:00 | NPP-375D | CARACARAÍ | RORAIMA | Brasil | 1400209 | 14 | 33 | nan | nan | nan | Amazônia | 1.0 |
| 40c0343b-2215-3380-ad2a-c4394aa4181a | -5.04669 | -43.26511 | 2026-07-31 05:14:00 | NPP-375D | CAXIAS | MARANHÃO | Brasil | 2103000 | 21 | 33 | nan | nan | nan | Cerrado | 3.8 |
| 82323e8a-0173-32ec-a371-5fe892b792ab | -3.04938 | -48.74442 | 2026-07-31 05:14:00 | NPP-375D | TAILÂNDIA | PARÁ | Brasil | 1507953 | 15 | 33 | nan | nan | nan | Amazônia | 4.0 |
| 12af23fb-e524-3e81-8df4-b94bdf3e13d3 | -3.0514 | -48.74245 | 2026-07-31 05:14:00 | NPP-375D | TAILÂNDIA | PARÁ | Brasil | 1507953 | 15 | 33 | nan | nan | nan | Amazônia | 6.9 |
| 705bba1e-a633-3fac-8f79-3bb8e9b00f41 | -4.91401 | -43.46665 | 2026-07-31 05:14:00 | NPP-375D | CAXIAS | MARANHÃO | Brasil | 2103000 | 21 | 33 | nan | nan | nan | Cerrado | 3.3 |
| e0d4a00c-b2ac-3de2-b0da-fd2f28f084cc | -3.96873 | -48.1235 | 2026-07-31 05:14:00 | NPP-375D | DOM ELISEU | PARÁ | Brasil | 1502939 | 15 | 33 | nan | nan | nan | Amazônia | 3.2 |
| fe4c8beb-1a50-3090-99c9-8a8b586c2698 | 1.09703 | -60.50608 | 2026-07-31 05:14:00 | NPP-375D | CARACARAÍ | RORAIMA | Brasil | 1400209 | 14 | 33 | nan | nan | nan | Amazônia | 2.8 |
| f4d91ffd-5a89-3d0c-a95a-7410a429d461 | -4.01217 | -48.06611 | 2026-07-31 05:14:00 | NPP-375D | DOM ELISEU | PARÁ | Brasil | 1502939 | 15 | 33 | nan | nan | nan | Amazônia | 1.5 |
| 010c757e-2b14-3e95-9e78-7774b7b56be4 | -4.2187 | -56.04989 | 2026-07-31 05:14:00 | NPP-375D | ITAITUBA | PARÁ | Brasil | 1503606 | 15 | 33 | nan | nan | nan | Amazônia | 4.7 |
| f1ce5363-ecb0-3113-a25e-614b9411f8b3 | -4.00154 | -43.2841 | 2026-07-31 05:14:00 | NPP-375D | CHAPADINHA | MARANHÃO | Brasil | 2103208 | 21 | 33 | nan | nan | nan | Cerrado | 1.6 |
| 5838eaf0-d0ae-3fdd-8ba4-c3c90f96c7d6 | -4.36851 | -47.77172 | 2026-07-31 05:14:00 | NPP-375D | DOM ELISEU | PARÁ | Brasil | 1502939 | 15 | 33 | nan | nan | nan | Amazônia | 3.4 |
| daca4ecb-9a43-3b19-8472-0d80973c50ad | 1.09965 | -60.52302 | 2026-07-31 05:14:00 | NPP-375D | CARACARAÍ | RORAIMA | Brasil | 1400209 | 14 | 33 | nan | nan | nan | Amazônia | 1.8 |
| 1c6a798e-8c8c-3370-bbdb-0f1e14cd78cc | 1.10012 | -60.49698 | 2026-07-31 05:14:00 | NPP-375D | CARACARAÍ | RORAIMA | Brasil | 1400209 | 14 | 33 | nan | nan | nan | Amazônia | 0.6 |
| 7056680e-e3d4-3f5b-b15f-50bdeb717f37 | 1.09638 | -60.50187 | 2026-07-31 05:14:00 | NPP-375D | CARACARAÍ | RORAIMA | Brasil | 1400209 | 14 | 33 | nan | nan | nan | Amazônia | 2.8 |
| 37f6e7ce-a057-3d25-aac8-ef36f0b7b0b1 | -5.72191 | -48.12606 | 2026-07-31 05:14:00 | NPP-375D | ARAGUATINS | TOCANTINS | Brasil | 1702208 | 17 | 33 | nan | nan | nan | Amazônia | 2.6 |
| ef321638-1a18-3d3d-ad13-b73457e6b730 | -3.05003 | -48.74002 | 2026-07-31 05:14:00 | NPP-375D | TAILÂNDIA | PARÁ | Brasil | 1507953 | 15 | 33 | nan | nan | nan | Amazônia | 2.0 |
| 8e0059fd-0883-3e17-a8da-d96acf7548fb | -5.80748 | -43.63861 | 2026-07-31 05:14:00 | NPP-375D | LAGOA DO MATO | MARANHÃO | Brasil | 2105922 | 21 | 33 | nan | nan | nan | Cerrado | 3.2 |
| b8b487ea-8141-3861-a416-86662df2e69e | -4.27509 | -48.19674 | 2026-07-31 05:14:00 | NPP-375D | RONDON DO PARÁ | PARÁ | Brasil | 1506187 | 15 | 33 | nan | nan | nan | Amazônia | 12.2 |
| f688094a-10b1-3b3d-9ebb-353dfbfc65cb | -3.71362 | -51.17958 | 2026-07-31 05:14:00 | NPP-375D | PACAJÁ | PARÁ | Brasil | 1505486 | 15 | 33 | nan | nan | nan | Amazônia | 1.7 |
| 321ea864-39ae-3151-9cdf-a3bebfca261b | -3.96327 | -48.12768 | 2026-07-31 05:14:00 | NPP-375D | DOM ELISEU | PARÁ | Brasil | 1502939 | 15 | 33 | nan | nan | nan | Amazônia | 10.3 |
| 0e554b4a-b1dc-363c-b14d-f6afd65d3cdb | -2.89278 | -48.01184 | 2026-07-31 05:14:00 | NPP-375D | IPIXUNA DO PARÁ | PARÁ | Brasil | 1503457 | 15 | 33 | nan | nan | nan | Amazônia | 4.0 |
| 83ba4301-1261-3016-9ce7-337689711b7c | -4.36642 | -47.76702 | 2026-07-31 05:14:00 | NPP-375D | DOM ELISEU | PARÁ | Brasil | 1502939 | 15 | 33 | nan | nan | nan | Amazônia | 3.2 |
| 8f84d0b1-ba8f-3e4a-ab7b-e1efa93b4f55 | 1.10207 | -60.50961 | 2026-07-31 05:14:00 | NPP-375D | CARACARAÍ | RORAIMA | Brasil | 1400209 | 14 | 33 | nan | nan | nan | Amazônia | 1.8 |
| 6064e392-5b1b-3d5b-b9eb-dbf9278039c1 | -3.71051 | -51.17433 | 2026-07-31 05:14:00 | NPP-375D | PACAJÁ | PARÁ | Brasil | 1505486 | 15 | 33 | nan | nan | nan | Amazônia | 3.2 |
| 882fc896-b5b6-360e-9ac8-c2bfbb26366d | -4.37052 | -47.77312 | 2026-07-31 05:14:00 | NPP-375D | DOM ELISEU | PARÁ | Brasil | 1502939 | 15 | 33 | nan | nan | nan | Amazônia | 3.0 |
| 46209453-d958-3dd2-9ca2-fa6b6c1095f6 | -3.05384 | -48.7451 | 2026-07-31 05:14:00 | NPP-375D | TAILÂNDIA | PARÁ | Brasil | 1507953 | 15 | 33 | nan | nan | nan | Amazônia | 4.4 |
| 56e2b384-efcf-354f-9477-ff611e41a827 | -3.99502 | -43.28319 | 2026-07-31 05:14:00 | NPP-375D | CHAPADINHA | MARANHÃO | Brasil | 2103208 | 21 | 33 | nan | nan | nan | Cerrado | 0.9 |
| b8c9a99b-264e-3574-944f-6ae551e92fa3 | -3.11354 | -47.90847 | 2026-07-31 05:14:00 | NPP-375D | PARAGOMINAS | PARÁ | Brasil | 1505502 | 15 | 33 | nan | nan | nan | Amazônia | 11.6 |
| 11dd85cf-afd8-3b8a-a71a-09430e8a6281 | -3.05586 | -48.74311 | 2026-07-31 05:14:00 | NPP-375D | TAILÂNDIA | PARÁ | Brasil | 1507953 | 15 | 33 | nan | nan | nan | Amazônia | 0.9 |
| 6acc17d2-d52f-3117-9cf3-5c80f217406f | -3.71435 | -51.17489 | 2026-07-31 05:14:00 | NPP-375D | PACAJÁ | PARÁ | Brasil | 1505486 | 15 | 33 | nan | nan | nan | Amazônia | 1.7 |
| 9f04537c-92c4-34c7-b963-9f14b87f6c40 | -3.85881 | -54.08241 | 2026-07-31 05:14:00 | NPP-375D | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | 0.3 |
| 7b78681f-ca34-331f-b3b7-d7a643bf952b | 1.09573 | -60.49766 | 2026-07-31 05:14:00 | NPP-375D | CARACARAÍ | RORAIMA | Brasil | 1400209 | 14 | 33 | nan | nan | nan | Amazônia | 1.6 |
| 949dc16d-1b09-39a7-a46d-90ef599fa87e | -3.11277 | -47.91356 | 2026-07-31 05:14:00 | NPP-375D | PARAGOMINAS | PARÁ | Brasil | 1505502 | 15 | 33 | nan | nan | nan | Amazônia | 11.1 |
| 7d5683eb-4318-34b0-b54e-5eda2fd5069b | -4.37128 | -47.7678 | 2026-07-31 05:14:00 | NPP-375D | DOM ELISEU | PARÁ | Brasil | 1502939 | 15 | 33 | nan | nan | nan | Amazônia | 3.2 |
| 4ba20414-9c1c-3ca6-8e99-76c5a703fb3f | 1.10339 | -60.51807 | 2026-07-31 05:14:00 | NPP-375D | CARACARAÍ | RORAIMA | Brasil | 1400209 | 14 | 33 | nan | nan | nan | Amazônia | 2.5 |
| d9525d8f-b41a-3f7c-8f32-043534557ce4 | 1.10273 | -60.51383 | 2026-07-31 05:14:00 | NPP-375D | CARACARAÍ | RORAIMA | Brasil | 1400209 | 14 | 33 | nan | nan | nan | Amazônia | 1.8 |
| 45c752eb-ed98-3f25-af88-7add481b4c45 | -3.11827 | -47.9092 | 2026-07-31 05:14:00 | NPP-375D | PARAGOMINAS | PARÁ | Brasil | 1505502 | 15 | 33 | nan | nan | nan | Amazônia | 3.1 |
| 8e96c399-fe1f-3fef-9b0e-e24c7d16fa27 | -3.89103 | -59.07502 | 2026-07-31 05:14:00 | NPP-375D | NOVA OLINDA DO NORTE | AMAZONAS | Brasil | 1303106 | 13 | 33 | nan | nan | nan | Amazônia | 0.9 |
| 90ab5ffd-21f6-31e9-a047-a003a2814a60 | -7.01087 | -45.84872 | 2026-07-31 05:16:00 | NPP-375D | SÃO RAIMUNDO DAS MANGABEIRAS | MARANHÃO | Brasil | 2111607 | 21 | 33 | nan | nan | nan | Cerrado | 1.4 |
| 65537c8f-877d-315c-9a74-1ea7477715aa | -11.45761 | -50.10232 | 2026-07-31 05:16:00 | NPP-375D | LAGOA DA CONFUSÃO | TOCANTINS | Brasil | 1711902 | 17 | 33 | nan | nan | nan | Cerrado | 1.4 |
| 9cbb2e6d-69d2-3296-b4cc-fff3c85de88d | -6.18085 | -55.52668 | 2026-07-31 05:16:00 | NPP-375D | ITAITUBA | PARÁ | Brasil | 1503606 | 15 | 33 | nan | nan | nan | Amazônia | 2.0 |
| abc398e7-92b2-38f0-8fbc-9f3beb0a1332 | -10.07849 | -60.50257 | 2026-07-31 05:16:00 | NPP-375D | ARIPUANÃ | MATO GROSSO | Brasil | 5101407 | 51 | 33 | nan | nan | nan | Amazônia | 1.6 |
| c04bfc27-04aa-36e6-b82d-7224240a3cc0 | -4.71887 | -55.99406 | 2026-07-31 05:16:00 | NPP-375D | TRAIRÃO | PARÁ | Brasil | 1508050 | 15 | 33 | nan | nan | nan | Amazônia | 0.7 |
| 5c1b4b67-1556-365a-9443-8f337673528d | -11.74259 | -48.91693 | 2026-07-31 05:16:00 | NPP-375D | GURUPI | TOCANTINS | Brasil | 1709500 | 17 | 33 | nan | nan | nan | Cerrado | 1.9 |
| b0784825-0bc8-342a-bf60-e7e59c48c7c7 | -6.18031 | -55.53014 | 2026-07-31 05:16:00 | NPP-375D | ITAITUBA | PARÁ | Brasil | 1503606 | 15 | 33 | nan | nan | nan | Amazônia | 1.6 |
| 7fe531b9-5b18-3221-9f47-97a68a541b4a | -12.60998 | -44.60324 | 2026-07-31 05:16:00 | NPP-375D | BAIANÓPOLIS | BAHIA | Brasil | 2902500 | 29 | 33 | nan | nan | nan | Cerrado | 1.0 |
| 051cb12d-2851-3963-bebe-0d5fd7cc2088 | -12.34174 | -48.21763 | 2026-07-31 05:16:00 | NPP-375D | PARANÃ | TOCANTINS | Brasil | 1716208 | 17 | 33 | nan | nan | nan | Cerrado | 0.7 |
| b44eb74c-2bff-336c-ac53-ff9e23c45cdd | -11.90504 | -55.90168 | 2026-07-31 05:16:00 | NPP-375D | IPIRANGA DO NORTE | MATO GROSSO | Brasil | 5104526 | 51 | 33 | nan | nan | nan | Amazônia | 0.5 |
| 2e4ba9ed-6be0-3253-8fcc-27fe7a95cb3e | -11.30624 | -50.29357 | 2026-07-31 05:16:00 | NPP-375D | LAGOA DA CONFUSÃO | TOCANTINS | Brasil | 1711902 | 17 | 33 | nan | nan | nan | Cerrado | 0.8 |
| 90e0d0aa-ff59-3b45-8bb8-5d50a9161150 | -12.84999 | -44.39212 | 2026-07-31 05:16:00 | NPP-375D | BAIANÓPOLIS | BAHIA | Brasil | 2902500 | 29 | 33 | nan | nan | nan | Cerrado | 1.8 |
| 01090af8-1b0d-343f-89d0-8b568cbd86ab | -11.73753 | -57.8103 | 2026-07-31 05:16:00 | NPP-375D | JUARA | MATO GROSSO | Brasil | 5105101 | 51 | 33 | nan | nan | nan | Amazônia | 0.6 |
| 1859ccf9-ab25-3d53-885c-05a79fc0b63f | -12.60601 | -44.63849 | 2026-07-31 05:16:00 | NPP-375D | SÃO DESIDÉRIO | BAHIA | Brasil | 2928901 | 29 | 33 | nan | nan | nan | Cerrado | 2.5 |
| 23c8b6d4-588c-312e-9d4f-c189bf1e9d8e | -6.17421 | -55.52563 | 2026-07-31 05:16:00 | NPP-375D | ITAITUBA | PARÁ | Brasil | 1503606 | 15 | 33 | nan | nan | nan | Amazônia | 1.2 |
| b4706884-a445-358e-82a5-3eab177613b0 | -12.61268 | -44.6394 | 2026-07-31 05:16:00 | NPP-375D | SÃO DESIDÉRIO | BAHIA | Brasil | 2928901 | 29 | 33 | nan | nan | nan | Cerrado | 2.5 |
| 43042ed3-fa00-35b8-a2ef-601d1cf33129 | -7.40558 | -49.52723 | 2026-07-31 05:16:00 | NPP-375D | FLORESTA DO ARAGUAIA | PARÁ | Brasil | 1503044 | 15 | 33 | nan | nan | nan | Amazônia | 2.2 |
| 10edfc87-59b0-3628-b79f-2455d76fd117 | -10.48383 | -46.32084 | 2026-07-31 05:16:00 | NPP-375D | MATEIROS | TOCANTINS | Brasil | 1712702 | 17 | 33 | nan | nan | nan | Cerrado | 2.0 |
| 80098911-ac4e-3139-ac38-a309a98941ac | -6.56877 | -56.53768 | 2026-07-31 05:16:00 | NPP-375D | ITAITUBA | PARÁ | Brasil | 1503606 | 15 | 33 | nan | nan | nan | Amazônia | 0.8 |
| 12ce4087-5cc5-3af2-9b6a-db0f1cb5357c | -12.61662 | -44.62764 | 2026-07-31 05:16:00 | NPP-375D | SÃO DESIDÉRIO | BAHIA | Brasil | 2928901 | 29 | 33 | nan | nan | nan | Cerrado | 2.6 |
| aea7c39b-595d-3226-825e-38e55399ad53 | -6.55977 | -55.16082 | 2026-07-31 05:16:00 | NPP-375D | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 2.4 |
| b2630d37-eb6d-3767-bd70-5f1823dd3f56 | -12.61598 | -44.63365 | 2026-07-31 05:16:00 | NPP-375D | SÃO DESIDÉRIO | BAHIA | Brasil | 2928901 | 29 | 33 | nan | nan | nan | Cerrado | 2.6 |
| 09c15fbc-f2a6-36e9-8e3e-df62b43b7783 | -12.34133 | -48.22097 | 2026-07-31 05:16:00 | NPP-375D | PARANÃ | TOCANTINS | Brasil | 1716208 | 17 | 33 | nan | nan | nan | Cerrado | 0.7 |
| 02e01099-85a7-3aef-b521-6d6327a70c34 | -12.85075 | -44.39387 | 2026-07-31 05:16:00 | NPP-375D | BAIANÓPOLIS | BAHIA | Brasil | 2902500 | 29 | 33 | nan | nan | nan | Cerrado | 4.1 |
| c37fc2fd-3f88-3fb7-b7ff-17ad5dcd7efb | -6.88706 | -44.77363 | 2026-07-31 05:16:00 | NPP-375D | SÃO FÉLIX DE BALSAS | MARANHÃO | Brasil | 2110807 | 21 | 33 | nan | nan | nan | Cerrado | 0.8 |
| 1dce34bc-1433-383f-9c21-25726c009d8f | -11.73903 | -48.90486 | 2026-07-31 05:16:00 | NPP-375D | GURUPI | TOCANTINS | Brasil | 1709500 | 17 | 33 | nan | nan | nan | Cerrado | 1.9 |
| 19d0cfa0-cfbd-3674-b6b8-dcf8a314dffc | -6.55699 | -55.15677 | 2026-07-31 05:16:00 | NPP-375D | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 1.1 |
| 6786da76-edfe-3def-935f-f1b8cf591a6c | -11.93226 | -43.44188 | 2026-07-31 05:16:00 | NPP-375D | MUQUÉM DO SÃO FRANCISCO | BAHIA | Brasil | 2922250 | 29 | 33 | nan | nan | nan | Cerrado | 5.2 |
| 65585f18-f2b0-3b4e-9a78-d183f5034200 | -6.17644 | -55.5331 | 2026-07-31 05:16:00 | NPP-375D | ITAITUBA | PARÁ | Brasil | 1503606 | 15 | 33 | nan | nan | nan | Amazônia | 1.2 |
| b6709c40-f70c-3b9c-978f-c5b101396802 | -8.99867 | -45.18037 | 2026-07-31 05:16:00 | NPP-375D | BAIXA GRANDE DO RIBEIRO | PIAUÍ | Brasil | 2201150 | 22 | 33 | nan | nan | nan | Cerrado | 2.3 |
| 92f4b64c-6390-3da9-bd06-79cf410345ca | -6.18472 | -55.52372 | 2026-07-31 05:16:00 | NPP-375D | ITAITUBA | PARÁ | Brasil | 1503606 | 15 | 33 | nan | nan | nan | Amazônia | 2.0 |
| dd663c29-9f0d-3e59-8bda-5a228f17180b | -10.07477 | -60.50195 | 2026-07-31 05:16:00 | NPP-375D | ARIPUANÃ | MATO GROSSO | Brasil | 5101407 | 51 | 33 | nan | nan | nan | Amazônia | 0.7 |
| d8d2b32b-d196-3c4b-8e18-fe16c16feace | -6.18417 | -55.5272 | 2026-07-31 05:16:00 | NPP-375D | ITAITUBA | PARÁ | Brasil | 1503606 | 15 | 33 | nan | nan | nan | Amazônia | 2.0 |
| 19b45547-4e14-3e33-add9-9eff60195d1b | -10.48331 | -46.32499 | 2026-07-31 05:16:00 | NPP-375D | MATEIROS | TOCANTINS | Brasil | 1712702 | 17 | 33 | nan | nan | nan | Cerrado | 2.8 |
| a09e6bb0-5aa6-35a2-976a-0fa26821bca1 | -6.56033 | -55.1573 | 2026-07-31 05:16:00 | NPP-375D | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 1.1 |
| aadcb60f-dbcd-3d12-99e3-7ac352e9f42a | -6.18859 | -55.52077 | 2026-07-31 05:16:00 | NPP-375D | ITAITUBA | PARÁ | Brasil | 1503606 | 15 | 33 | nan | nan | nan | Amazônia | 0.5 |
| d3d6e511-9c10-37c6-88a9-b8ce10f9c75d | -12.62003 | -44.63434 | 2026-07-31 05:16:00 | NPP-375D | SÃO DESIDÉRIO | BAHIA | Brasil | 2928901 | 29 | 33 | nan | nan | nan | Cerrado | 2.7 |
| cbf1362c-8e87-3030-bb8f-3ddc653bd8ca | -6.18804 | -55.52425 | 2026-07-31 05:16:00 | NPP-375D | ITAITUBA | PARÁ | Brasil | 1503606 | 15 | 33 | nan | nan | nan | Amazônia | 2.0 |
| 983676bb-690b-3369-8a31-dff769bedac0 | -10.63207 | -47.48629 | 2026-07-31 05:16:00 | NPP-375D | PONTE ALTA DO TOCANTINS | TOCANTINS | Brasil | 1717909 | 17 | 33 | nan | nan | nan | Cerrado | 1.4 |
| 21f75586-d073-3074-9ec0-2e0fc603f513 | -12.61736 | -44.59804 | 2026-07-31 05:16:00 | NPP-375D | BAIANÓPOLIS | BAHIA | Brasil | 2902500 | 29 | 33 | nan | nan | nan | Cerrado | 1.0 |
| 39f8d9c9-385c-3fc7-a38b-e13ab711b065 | -9.48084 | -57.31846 | 2026-07-31 05:16:00 | NPP-375D | APIACÁS | MATO GROSSO | Brasil | 5100805 | 51 | 33 | nan | nan | nan | Amazônia | 1.1 |
| 3199056e-f110-3308-b6a2-4514203077f8 | -11.44929 | -50.0994 | 2026-07-31 05:16:00 | NPP-375D | LAGOA DA CONFUSÃO | TOCANTINS | Brasil | 1711902 | 17 | 33 | nan | nan | nan | Cerrado | 0.8 |
| 22ea8a7f-380f-319e-935e-2237474a8061 | -9.96544 | -64.96652 | 2026-07-31 05:16:00 | NPP-375D | PORTO VELHO | RONDÔNIA | Brasil | 1100205 | 11 | 33 | nan | nan | nan | Amazônia | 4.3 |
| b54278b9-a652-393e-a23c-98cbd0706554 | -10.06177 | -60.50181 | 2026-07-31 05:16:00 | NPP-375D | ARIPUANÃ | MATO GROSSO | Brasil | 5101407 | 51 | 33 | nan | nan | nan | Amazônia | 0.7 |
| 80c727ea-3b23-30e8-b8d4-5e53a4b7642b | -9.00307 | -45.18146 | 2026-07-31 05:16:00 | NPP-375D | BAIXA GRANDE DO RIBEIRO | PIAUÍ | Brasil | 2201150 | 22 | 33 | nan | nan | nan | Cerrado | 0.9 |
| 2137bafe-8241-39f4-a749-cf8175961613 | -7.73636 | -55.3413 | 2026-07-31 05:16:00 | NPP-375D | NOVO PROGRESSO | PARÁ | Brasil | 1505031 | 15 | 33 | nan | nan | nan | Amazônia | 1.4 |
| ea99a682-96e3-3821-98f9-d1973b50f715 | -11.82496 | -45.60666 | 2026-07-31 05:16:00 | NPP-375D | BARREIRAS | BAHIA | Brasil | 2903201 | 29 | 33 | nan | nan | nan | Cerrado | 1.3 |
| ab4eec53-c7ad-39ff-9ffa-fa3615e27cdc | -6.10149 | -49.38507 | 2026-07-31 05:16:00 | NPP-375D | ELDORADO DO CARAJÁS | PARÁ | Brasil | 1502954 | 15 | 33 | nan | nan | nan | Amazônia | 2.9 |
| d710ebe1-3869-3e00-a1b0-92439193926f | -6.18362 | -55.53067 | 2026-07-31 05:16:00 | NPP-375D | ITAITUBA | PARÁ | Brasil | 1503606 | 15 | 33 | nan | nan | nan | Amazônia | 1.6 |
| 0eafbf9b-29fa-37ca-8f2f-a8e86770bbee | -6.17698 | -55.52962 | 2026-07-31 05:16:00 | NPP-375D | ITAITUBA | PARÁ | Brasil | 1503606 | 15 | 33 | nan | nan | nan | Amazônia | 1.2 |
| 845ff214-ff42-3ac0-b0b1-235e8f0eed31 | -12.61335 | -44.63347 | 2026-07-31 05:16:00 | NPP-375D | SÃO DESIDÉRIO | BAHIA | Brasil | 2928901 | 29 | 33 | nan | nan | nan | Cerrado | 2.5 |
| c81b3454-b83b-3633-8bfc-9570655fe3f4 | -9.93033 | -59.92159 | 2026-07-31 05:16:00 | NPP-375D | ARIPUANÃ | MATO GROSSO | Brasil | 5101407 | 51 | 33 | nan | nan | nan | Amazônia | 0.6 |
| 04c5571e-c252-3598-b400-d2e230961ca1 | -6.55644 | -55.16028 | 2026-07-31 05:16:00 | NPP-375D | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 2.4 |
| 46e46d95-e0a8-3e2b-879c-5afbf44e32ed | -10.63755 | -47.48677 | 2026-07-31 05:16:00 | NPP-375D | PONTE ALTA DO TOCANTINS | TOCANTINS | Brasil | 1717909 | 17 | 33 | nan | nan | nan | Cerrado | 1.4 |
| 575f5295-3638-324b-9502-97301c63ea51 | -7.01115 | -45.84697 | 2026-07-31 05:16:00 | NPP-375D | SÃO RAIMUNDO DAS MANGABEIRAS | MARANHÃO | Brasil | 2111607 | 21 | 33 | nan | nan | nan | Cerrado | 1.3 |
| 5890c887-d0c5-393a-9f23-9f7b2bb81518 | -11.74086 | -57.81085 | 2026-07-31 05:16:00 | NPP-375D | JUARA | MATO GROSSO | Brasil | 5105101 | 51 | 33 | nan | nan | nan | Amazônia | 0.5 |


[Clique aqui para ver as próximas entradas](README12.md)
