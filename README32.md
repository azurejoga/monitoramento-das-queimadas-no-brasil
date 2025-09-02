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

## Dados Diários - Página 32

| ID | Latitude | Longitude | Data/Hora GMT | Satélite | Município | Estado | País | Município ID | Estado ID | País ID | Dias sem Chuva | Precipitação | Risco de Fogo | Bioma | FRP |
|----|----------|-----------|---------------|----------|-----------|--------|------|--------------|-----------|---------|----------------|--------------|----------------|-------|-----|
| 16b032d9-fda9-3d4a-ab25-6a5639941a13 | -12.77964 | -48.0977 | 2025-09-02 04:14:00 | NOAA-20 | PARANÃ | TOCANTINS | Brasil | 1716208 | 17 | 33 | nan | nan | nan | Cerrado | 1.3 |
| e4853e4e-1fa5-39aa-be3c-23558b8c3836 | -12.88285 | -48.17395 | 2025-09-02 04:14:00 | NOAA-20 | PARANÃ | TOCANTINS | Brasil | 1716208 | 17 | 33 | nan | nan | nan | Cerrado | 2.7 |
| 809108b3-4f99-3c67-b7ed-dcd918170f1d | -7.7146 | -44.60883 | 2025-09-02 04:14:00 | NOAA-20 | URUÇUÍ | PIAUÍ | Brasil | 2211209 | 22 | 33 | nan | nan | nan | Cerrado | 1.4 |
| fe74ceae-f4cc-39f7-9b86-5495dc1db2a5 | -7.48804 | -45.36127 | 2025-09-02 04:14:00 | NOAA-20 | LORETO | MARANHÃO | Brasil | 2106102 | 21 | 33 | nan | nan | nan | Cerrado | 1.7 |
| 7a8cb28c-de87-3ee1-be49-de97b474c14e | -10.049 | -48.11567 | 2025-09-02 04:14:00 | NOAA-20 | APARECIDA DO RIO NEGRO | TOCANTINS | Brasil | 1701101 | 17 | 33 | nan | nan | nan | Cerrado | 7.2 |
| caa78858-6548-3319-b357-0c4da0c9faa3 | -6.98881 | -43.23193 | 2025-09-02 04:14:00 | NOAA-20 | FLORIANO | PIAUÍ | Brasil | 2203909 | 22 | 33 | nan | nan | nan | Caatinga | 2.2 |
| ee54e2db-badd-3ecf-8c31-8cf542ca17da | -6.92243 | -45.56361 | 2025-09-02 04:14:00 | NOAA-20 | SÃO RAIMUNDO DAS MANGABEIRAS | MARANHÃO | Brasil | 2111607 | 21 | 33 | nan | nan | nan | Cerrado | 0.8 |
| edef4c82-17d4-3d58-b924-f63b3893bf1d | -6.84906 | -52.82512 | 2025-09-02 04:14:00 | NOAA-20 | SÃO FÉLIX DO XINGU | PARÁ | Brasil | 1507300 | 15 | 33 | nan | nan | nan | Amazônia | 1.5 |
| 0f0e6e09-d0d5-392a-b4d3-d779343508c8 | -10.75766 | -49.56984 | 2025-09-02 04:14:00 | NOAA-20 | LAGOA DA CONFUSÃO | TOCANTINS | Brasil | 1711902 | 17 | 33 | nan | nan | nan | Cerrado | 4.3 |
| a7ff8dcf-9d65-3a79-b708-e1121bb9f616 | -11.81995 | -51.54683 | 2025-09-02 04:14:00 | NOAA-20 | ALTO BOA VISTA | MATO GROSSO | Brasil | 5100359 | 51 | 33 | nan | nan | nan | Cerrado | 3.9 |
| a0126b5e-ec22-33f3-8a66-fa2fc5aad7f1 | -8.81628 | -47.8311 | 2025-09-02 04:14:00 | NOAA-20 | SANTA MARIA DO TOCANTINS | TOCANTINS | Brasil | 1718881 | 17 | 33 | nan | nan | nan | Cerrado | 0.7 |
| c0c8a6a7-71c6-3049-894c-60d520747952 | -10.88001 | -55.75069 | 2025-09-02 04:14:00 | NOAA-20 | NOVA CANAÃ DO NORTE | MATO GROSSO | Brasil | 5106216 | 51 | 33 | nan | nan | nan | Amazônia | 2.8 |
| f89f8915-8367-3010-92d9-890f3775533e | -7.78919 | -45.45107 | 2025-09-02 04:14:00 | NOAA-20 | RIBEIRO GONÇALVES | PIAUÍ | Brasil | 2208908 | 22 | 33 | nan | nan | nan | Cerrado | 2.6 |
| 02c26c17-a9f3-3865-9a1e-fc3b58bd0871 | -12.75311 | -44.4098 | 2025-09-02 04:14:00 | NOAA-20 | BAIANÓPOLIS | BAHIA | Brasil | 2902500 | 29 | 33 | nan | nan | nan | Cerrado | 1.4 |
| 7fdb248f-73b4-328d-83d5-137f278db2fd | -6.97959 | -44.33835 | 2025-09-02 04:14:00 | NOAA-20 | BENEDITO LEITE | MARANHÃO | Brasil | 2101806 | 21 | 33 | nan | nan | nan | Cerrado | 0.9 |
| 6a37d3a5-ac88-34a6-ae80-8e679dd8b383 | -10.96895 | -50.78431 | 2025-09-02 04:14:00 | NOAA-20 | LUCIARA | MATO GROSSO | Brasil | 5105309 | 51 | 33 | nan | nan | nan | Cerrado | 1.7 |
| 0faab06c-b31b-3671-b212-865316751c16 | -10.05228 | -48.09655 | 2025-09-02 04:14:00 | NOAA-20 | APARECIDA DO RIO NEGRO | TOCANTINS | Brasil | 1701101 | 17 | 33 | nan | nan | nan | Cerrado | 23.0 |
| c390164f-26b4-3a31-81d4-9cbc073a8839 | -7.77547 | -45.44888 | 2025-09-02 04:14:00 | NOAA-20 | RIBEIRO GONÇALVES | PIAUÍ | Brasil | 2208908 | 22 | 33 | nan | nan | nan | Cerrado | 1.6 |
| 62c86a03-9edc-3870-baa6-39800de65f4b | -11.41628 | -46.89651 | 2025-09-02 04:14:00 | NOAA-20 | DIANÓPOLIS | TOCANTINS | Brasil | 1707009 | 17 | 33 | nan | nan | nan | Cerrado | 0.8 |
| 25b59411-50f4-3d17-93c7-37c3f2d02c27 | -9.75672 | -46.93547 | 2025-09-02 04:14:00 | NOAA-20 | LIZARDA | TOCANTINS | Brasil | 1712405 | 17 | 33 | nan | nan | nan | Cerrado | 1.4 |
| a14456ab-c34e-3890-8382-5a21df850b3b | -11.05635 | -46.90039 | 2025-09-02 04:14:00 | NOAA-20 | PONTE ALTA DO TOCANTINS | TOCANTINS | Brasil | 1717909 | 17 | 33 | nan | nan | nan | Cerrado | 1.3 |
| b1d2c19d-7794-3141-b78f-0e8a773fdaf9 | -7.91628 | -46.44313 | 2025-09-02 04:14:00 | NOAA-20 | RIACHÃO | MARANHÃO | Brasil | 2109502 | 21 | 33 | nan | nan | nan | Cerrado | 2.8 |
| 62a15c3b-f765-37d0-ade0-a22636a2d7bc | -11.85169 | -51.47793 | 2025-09-02 04:14:00 | NOAA-20 | ALTO BOA VISTA | MATO GROSSO | Brasil | 5100359 | 51 | 33 | nan | nan | nan | Cerrado | 1.5 |
| 6b3f1651-0bbe-3290-90ce-8b3eca371ced | -7.69652 | -50.27002 | 2025-09-02 04:14:00 | NOAA-20 | PAU D'ARCO | PARÁ | Brasil | 1505551 | 15 | 33 | nan | nan | nan | Amazônia | 5.5 |
| 28e0f6fd-7365-35bd-9aa8-5e78e7d66ff1 | -12.96024 | -48.09466 | 2025-09-02 04:14:00 | NOAA-20 | PARANÃ | TOCANTINS | Brasil | 1716208 | 17 | 33 | nan | nan | nan | Cerrado | 1.4 |
| 703f2321-e4ec-3f60-a2c7-c4f40fe7d44f | -6.77656 | -52.81763 | 2025-09-02 04:14:00 | NOAA-20 | SÃO FÉLIX DO XINGU | PARÁ | Brasil | 1507300 | 15 | 33 | nan | nan | nan | Amazônia | 2.4 |
| 3a672395-6108-37ab-aedf-fdca560694b4 | -7.77952 | -45.44564 | 2025-09-02 04:14:00 | NOAA-20 | RIBEIRO GONÇALVES | PIAUÍ | Brasil | 2208908 | 22 | 33 | nan | nan | nan | Cerrado | 2.7 |
| 6350d8f9-a1e9-3c2b-86d0-43f724354827 | -6.9802 | -44.31315 | 2025-09-02 04:14:00 | NOAA-20 | BENEDITO LEITE | MARANHÃO | Brasil | 2101806 | 21 | 33 | nan | nan | nan | Cerrado | 1.2 |
| fe1eef39-cbed-395a-8be4-cb7136a091d2 | -7.98783 | -46.47644 | 2025-09-02 04:14:00 | NOAA-20 | RIACHÃO | MARANHÃO | Brasil | 2109502 | 21 | 33 | nan | nan | nan | Cerrado | 4.1 |
| 109f3ad6-de76-3488-83cd-b35f6298b843 | -7.69529 | -50.27222 | 2025-09-02 04:14:00 | NOAA-20 | PAU D'ARCO | PARÁ | Brasil | 1505551 | 15 | 33 | nan | nan | nan | Amazônia | 7.6 |
| 9828f871-4117-3e29-be4c-8165a5f99aa0 | -13.52205 | -47.01036 | 2025-09-02 04:14:00 | NOAA-20 | MONTE ALEGRE DE GOIÁS | GOIÁS | Brasil | 5213509 | 52 | 33 | nan | nan | nan | Cerrado | 2.2 |
| 0f123a98-eb01-32ce-a87f-26f8eb6894bd | -7.98273 | -46.46273 | 2025-09-02 04:14:00 | NOAA-20 | RIACHÃO | MARANHÃO | Brasil | 2109502 | 21 | 33 | nan | nan | nan | Cerrado | 4.4 |
| c5623334-85e4-37eb-8a3f-cdd80dc5b7ca | -13.52744 | -46.99932 | 2025-09-02 04:14:00 | NOAA-20 | MONTE ALEGRE DE GOIÁS | GOIÁS | Brasil | 5213509 | 52 | 33 | nan | nan | nan | Cerrado | 1.4 |
| 17237729-e6f7-3acc-8e14-a5468c879576 | -9.75741 | -46.93127 | 2025-09-02 04:14:00 | NOAA-20 | LIZARDA | TOCANTINS | Brasil | 1712405 | 17 | 33 | nan | nan | nan | Cerrado | 1.4 |
| cc61c892-597f-3bae-8996-8fb771abd183 | -11.10651 | -44.62125 | 2025-09-02 04:14:00 | NOAA-20 | SANTA RITA DE CÁSSIA | BAHIA | Brasil | 2928406 | 29 | 33 | nan | nan | nan | Cerrado | 5.8 |
| c36ffc97-1643-3201-a35e-68f0fe465923 | -10.97292 | -50.76933 | 2025-09-02 04:14:00 | NOAA-20 | LUCIARA | MATO GROSSO | Brasil | 5105309 | 51 | 33 | nan | nan | nan | Cerrado | 1.0 |
| c106c0ad-a4bb-3d81-a26e-0add2d01e914 | -11.89096 | -46.67185 | 2025-09-02 04:14:00 | NOAA-20 | NOVO JARDIM | TOCANTINS | Brasil | 1715259 | 17 | 33 | nan | nan | nan | Cerrado | 1.1 |
| c25e2ab2-223c-3d68-947d-ce6d67e44fed | -13.54167 | -46.97778 | 2025-09-02 04:14:00 | NOAA-20 | MONTE ALEGRE DE GOIÁS | GOIÁS | Brasil | 5213509 | 52 | 33 | nan | nan | nan | Cerrado | 1.0 |
| 178fdb29-179a-36e3-8be2-b1c7a42da827 | -7.00184 | -44.34927 | 2025-09-02 04:14:00 | NOAA-20 | BENEDITO LEITE | MARANHÃO | Brasil | 2101806 | 21 | 33 | nan | nan | nan | Cerrado | 1.4 |
| 635c4be9-ebf9-300b-bc9e-e78a17d310a0 | -8.70422 | -50.43322 | 2025-09-02 04:14:00 | NOAA-20 | SANTA MARIA DAS BARREIRAS | PARÁ | Brasil | 1506583 | 15 | 33 | nan | nan | nan | Amazônia | 4.5 |
| 718cdec3-2db7-3548-a2d1-9b9fb09d4f2a | -13.70404 | -46.88916 | 2025-09-02 04:14:00 | NOAA-20 | NOVA ROMA | GOIÁS | Brasil | 5214903 | 52 | 33 | nan | nan | nan | Cerrado | 0.8 |
| 0248ede3-6983-3ea5-817f-5053203712a9 | -11.06032 | -45.39703 | 2025-09-02 04:14:00 | NOAA-20 | FORMOSA DO RIO PRETO | BAHIA | Brasil | 2911105 | 29 | 33 | nan | nan | nan | Cerrado | 9.3 |
| 48c43b72-4843-3e30-8d9d-f346e7d85fd1 | -6.17628 | -47.28228 | 2025-09-02 04:14:00 | NOAA-20 | CAMPESTRE DO MARANHÃO | MARANHÃO | Brasil | 2102556 | 21 | 33 | nan | nan | nan | Cerrado | 8.0 |
| 52a242d2-057c-3ed5-a919-a4ad58b4fc06 | -12.86977 | -48.053 | 2025-09-02 04:14:00 | NOAA-20 | PARANÃ | TOCANTINS | Brasil | 1716208 | 17 | 33 | nan | nan | nan | Cerrado | 3.9 |
| 7e80e301-3bb4-3741-9f5e-860c9f5dfa89 | -9.73136 | -48.96004 | 2025-09-02 04:14:00 | NOAA-20 | DIVINÓPOLIS DO TOCANTINS | TOCANTINS | Brasil | 1707108 | 17 | 33 | nan | nan | nan | Cerrado | 1.4 |
| f9e38012-7e71-3f65-a05a-74dc134b354e | -11.10811 | -44.65396 | 2025-09-02 04:14:00 | NOAA-20 | SANTA RITA DE CÁSSIA | BAHIA | Brasil | 2928406 | 29 | 33 | nan | nan | nan | Cerrado | 3.6 |
| 0ebd9968-7a85-3a1f-a5be-8fb2a336b833 | -6.54365 | -44.10963 | 2025-09-02 04:14:00 | NOAA-20 | PASTOS BONS | MARANHÃO | Brasil | 2108009 | 21 | 33 | nan | nan | nan | Cerrado | 1.4 |
| 8c0d9694-2362-39ba-8ba5-80d1f05f328a | -6.84551 | -52.81351 | 2025-09-02 04:14:00 | NOAA-20 | SÃO FÉLIX DO XINGU | PARÁ | Brasil | 1507300 | 15 | 33 | nan | nan | nan | Amazônia | 1.1 |
| a3f461b7-c875-3e7a-9aa1-c28a8210e186 | -11.66509 | -52.19535 | 2025-09-02 04:14:00 | NOAA-20 | SÃO FÉLIX DO ARAGUAIA | MATO GROSSO | Brasil | 5107859 | 51 | 33 | nan | nan | nan | Amazônia | 12.1 |
| 6744afd2-1a2e-3d62-b0d7-a4911f5210fa | -13.52615 | -47.00708 | 2025-09-02 04:14:00 | NOAA-20 | MONTE ALEGRE DE GOIÁS | GOIÁS | Brasil | 5213509 | 52 | 33 | nan | nan | nan | Cerrado | 1.7 |
| cc02fa03-7395-3882-a9e9-a2831de5ffdf | -6.62934 | -43.95792 | 2025-09-02 04:14:00 | NOAA-20 | NOVA IORQUE | MARANHÃO | Brasil | 2107308 | 21 | 33 | nan | nan | nan | Cerrado | 2.2 |
| f123732e-eedf-36bc-a79b-8e055514a0fb | -10.27392 | -54.26121 | 2025-09-02 04:14:00 | NOAA-20 | PEIXOTO DE AZEVEDO | MATO GROSSO | Brasil | 5106422 | 51 | 33 | nan | nan | nan | Amazônia | 1.2 |
| e8e2db4b-ec12-3a18-92a2-602252a88066 | -12.93291 | -48.10126 | 2025-09-02 04:14:00 | NOAA-20 | PARANÃ | TOCANTINS | Brasil | 1716208 | 17 | 33 | nan | nan | nan | Cerrado | 2.5 |
| cb9c68c8-4fef-3e3c-8073-b0172e857d5f | -6.7923 | -52.82431 | 2025-09-02 04:14:00 | NOAA-20 | SÃO FÉLIX DO XINGU | PARÁ | Brasil | 1507300 | 15 | 33 | nan | nan | nan | Amazônia | 2.3 |
| c3930c91-de5b-362d-bef0-f8b22119cd02 | -11.09985 | -44.6418 | 2025-09-02 04:14:00 | NOAA-20 | SANTA RITA DE CÁSSIA | BAHIA | Brasil | 2928406 | 29 | 33 | nan | nan | nan | Cerrado | 40.7 |
| 061ee41f-3e98-37af-a8bc-fe80c5a62ee2 | -11.42405 | -55.19092 | 2025-09-02 04:14:00 | NOAA-20 | CLÁUDIA | MATO GROSSO | Brasil | 5103056 | 51 | 33 | nan | nan | nan | Amazônia | 2.3 |
| eae74c6d-f8ed-3f57-9b6f-e79d92e863cf | -10.44092 | -50.27442 | 2025-09-02 04:14:00 | NOAA-20 | PIUM | TOCANTINS | Brasil | 1717503 | 17 | 33 | nan | nan | nan | Cerrado | 4.0 |
| d9d2f4a2-4ff8-3fb8-9dd9-a1777b56d191 | -11.43167 | -55.18333 | 2025-09-02 04:14:00 | NOAA-20 | CLÁUDIA | MATO GROSSO | Brasil | 5103056 | 51 | 33 | nan | nan | nan | Amazônia | 0.6 |
| d20c3278-c10f-35e6-8650-816e2a41f533 | -7.57584 | -42.71593 | 2025-09-02 04:14:00 | NOAA-20 | FLORES DO PIAUÍ | PIAUÍ | Brasil | 2203800 | 22 | 33 | nan | nan | nan | Caatinga | 1.1 |
| 3e39da5a-6215-3e5f-992c-d7bdcd39d6ed | -11.09046 | -44.63667 | 2025-09-02 04:14:00 | NOAA-20 | SANTA RITA DE CÁSSIA | BAHIA | Brasil | 2928406 | 29 | 33 | nan | nan | nan | Cerrado | 1.5 |
| 55b471f9-763a-3b1e-b348-5a4b07a5a553 | -8.7452 | -46.124 | 2025-09-02 04:14:00 | NOAA-20 | TASSO FRAGOSO | MARANHÃO | Brasil | 2112001 | 21 | 33 | nan | nan | nan | Cerrado | 2.3 |
| f057c602-6bac-39a4-aa53-f2eee1719871 | -8.85234 | -47.54786 | 2025-09-02 04:14:00 | NOAA-20 | SANTA MARIA DO TOCANTINS | TOCANTINS | Brasil | 1718881 | 17 | 33 | nan | nan | nan | Cerrado | 2.2 |
| 3d7e1a92-5818-37aa-abcb-e308948041ae | -12.57443 | -44.78862 | 2025-09-02 04:14:00 | NOAA-20 | SÃO DESIDÉRIO | BAHIA | Brasil | 2928901 | 29 | 33 | nan | nan | nan | Cerrado | 1.2 |
| 11816b96-c927-3579-a8be-2d69aa736401 | -12.20965 | -50.13061 | 2025-09-02 04:14:00 | NOAA-20 | FORMOSO DO ARAGUAIA | TOCANTINS | Brasil | 1708205 | 17 | 33 | nan | nan | nan | Cerrado | 2.1 |
| a6816de6-92e4-397f-83ab-fd0b65309c49 | -11.64866 | -57.3586 | 2025-09-02 04:14:00 | NOAA-20 | PORTO DOS GAÚCHOS | MATO GROSSO | Brasil | 5106802 | 51 | 33 | nan | nan | nan | Amazônia | 11.4 |
| 21be3530-a204-3678-9156-9d741398d7fb | -12.64471 | -48.24911 | 2025-09-02 04:14:00 | NOAA-20 | PARANÃ | TOCANTINS | Brasil | 1716208 | 17 | 33 | nan | nan | nan | Cerrado | 2.5 |
| 7a44429f-4d56-38cc-b549-1bef480f2c39 | -13.49659 | -46.92903 | 2025-09-02 04:14:00 | NOAA-20 | MONTE ALEGRE DE GOIÁS | GOIÁS | Brasil | 5213509 | 52 | 33 | nan | nan | nan | Cerrado | 2.4 |
| c53121b7-1c88-3f4c-b808-2890a83a15ca | -11.65842 | -52.17734 | 2025-09-02 04:14:00 | NOAA-20 | SÃO FÉLIX DO ARAGUAIA | MATO GROSSO | Brasil | 5107859 | 51 | 33 | nan | nan | nan | Amazônia | 12.3 |
| c3f1eec6-b579-378c-b0d3-c0eaf1a9c642 | -7.06367 | -45.98872 | 2025-09-02 04:14:00 | NOAA-20 | FORTALEZA DOS NOGUEIRAS | MARANHÃO | Brasil | 2104107 | 21 | 33 | nan | nan | nan | Cerrado | 1.7 |
| 2336dfff-ecb7-323e-8d97-62ebf8ed36ce | -9.48248 | -47.61123 | 2025-09-02 04:14:00 | NOAA-20 | RIO SONO | TOCANTINS | Brasil | 1718758 | 17 | 33 | nan | nan | nan | Cerrado | 0.6 |
| 17d02ed4-a77d-3c12-82c6-ae38093d3304 | -11.66792 | -52.20718 | 2025-09-02 04:14:00 | NOAA-20 | SÃO FÉLIX DO ARAGUAIA | MATO GROSSO | Brasil | 5107859 | 51 | 33 | nan | nan | nan | Amazônia | 20.5 |
| 9931edde-8a8b-307f-b7fb-5d16e889547f | -12.57168 | -44.78455 | 2025-09-02 04:14:00 | NOAA-20 | SÃO DESIDÉRIO | BAHIA | Brasil | 2928901 | 29 | 33 | nan | nan | nan | Cerrado | 1.6 |
| d97d5f6d-91d7-3530-a8a7-6c63886bae34 | -11.97417 | -45.88209 | 2025-09-02 04:14:00 | NOAA-20 | LUÍS EDUARDO MAGALHÃES | BAHIA | Brasil | 2919553 | 29 | 33 | nan | nan | nan | Cerrado | 10.9 |
| bb5a817e-d93b-396c-a396-c2a08c96a986 | -7.56205 | -45.20886 | 2025-09-02 04:14:00 | NOAA-20 | RIBEIRO GONÇALVES | PIAUÍ | Brasil | 2208908 | 22 | 33 | nan | nan | nan | Cerrado | 1.7 |
| 276ca631-62f7-3a79-aba5-6aad92c36c7c | -12.9566 | -48.09399 | 2025-09-02 04:14:00 | NOAA-20 | PARANÃ | TOCANTINS | Brasil | 1716208 | 17 | 33 | nan | nan | nan | Cerrado | 3.4 |
| db72fa88-aad9-307b-82c9-6a3ad57acb7e | -12.8593 | -48.04924 | 2025-09-02 04:14:00 | NOAA-20 | PARANÃ | TOCANTINS | Brasil | 1716208 | 17 | 33 | nan | nan | nan | Cerrado | 12.5 |
| e4c27b88-4b06-3a1b-aefa-838086b03b1e | -7.92274 | -46.44835 | 2025-09-02 04:14:00 | NOAA-20 | RIACHÃO | MARANHÃO | Brasil | 2109502 | 21 | 33 | nan | nan | nan | Cerrado | 1.8 |
| 9cf1cba9-82ad-3acf-b980-057379e893e6 | -12.88362 | -48.16947 | 2025-09-02 04:14:00 | NOAA-20 | PARANÃ | TOCANTINS | Brasil | 1716208 | 17 | 33 | nan | nan | nan | Cerrado | 2.2 |
| 42330a2f-c722-3c51-8634-2a6e4ee69ed6 | -13.32332 | -46.83281 | 2025-09-02 04:14:00 | NOAA-20 | MONTE ALEGRE DE GOIÁS | GOIÁS | Brasil | 5213509 | 52 | 33 | nan | nan | nan | Cerrado | 2.9 |
| 1129e874-e161-34a5-988c-55ced3fd5ab8 | -11.00239 | -46.83351 | 2025-09-02 04:14:00 | NOAA-20 | MATEIROS | TOCANTINS | Brasil | 1712702 | 17 | 33 | nan | nan | nan | Cerrado | 8.8 |
| 439abb1f-f4ab-307e-991b-73c4c8c43e04 | -10.33795 | -42.42907 | 2025-09-02 04:14:00 | NOAA-20 | XIQUE-XIQUE | BAHIA | Brasil | 2933604 | 29 | 33 | nan | nan | nan | Caatinga | 0.3 |
| cac5482a-3d41-3ca1-a666-edafed8a5a73 | -6.78812 | -52.81601 | 2025-09-02 04:14:00 | NOAA-20 | SÃO FÉLIX DO XINGU | PARÁ | Brasil | 1507300 | 15 | 33 | nan | nan | nan | Amazônia | 3.9 |
| 04f6e8b1-8c63-3cd6-b5bb-d8b6d6c23647 | -12.94614 | -48.08963 | 2025-09-02 04:14:00 | NOAA-20 | PARANÃ | TOCANTINS | Brasil | 1716208 | 17 | 33 | nan | nan | nan | Cerrado | 6.6 |
| fa843459-e324-3974-ae16-4cfae6439df2 | -7.70814 | -50.31015 | 2025-09-02 04:14:00 | NOAA-20 | PAU D'ARCO | PARÁ | Brasil | 1505551 | 15 | 33 | nan | nan | nan | Amazônia | 2.1 |
| fe3f5db4-604a-3763-8430-d119a05a8b46 | -6.8664 | -45.55773 | 2025-09-02 04:14:00 | NOAA-20 | SÃO RAIMUNDO DAS MANGABEIRAS | MARANHÃO | Brasil | 2111607 | 21 | 33 | nan | nan | nan | Cerrado | 4.5 |
| 8741f696-6812-3593-9d57-f6e26fc64bcf | -10.87885 | -55.75381 | 2025-09-02 04:14:00 | NOAA-20 | NOVA CANAÃ DO NORTE | MATO GROSSO | Brasil | 5106216 | 51 | 33 | nan | nan | nan | Amazônia | 4.6 |
| 9d340fec-1e3e-3f6d-a6eb-76969002607b | -6.64701 | -44.10455 | 2025-09-02 04:14:00 | NOAA-20 | PASTOS BONS | MARANHÃO | Brasil | 2108009 | 21 | 33 | nan | nan | nan | Cerrado | 1.2 |
| 8cc6572f-b50c-383a-b8a8-9217a5778016 | -10.89647 | -50.83799 | 2025-09-02 04:14:00 | NOAA-20 | LUCIARA | MATO GROSSO | Brasil | 5105309 | 51 | 33 | nan | nan | nan | Cerrado | 1.4 |
| cef698c3-31f6-35a4-a6a6-be81ac2594cc | -13.49318 | -46.82725 | 2025-09-02 04:14:00 | NOAA-20 | MONTE ALEGRE DE GOIÁS | GOIÁS | Brasil | 5213509 | 52 | 33 | nan | nan | nan | Cerrado | 2.2 |
| 6996a18e-b74f-39d1-9295-5024033d63e0 | -10.28965 | -47.51931 | 2025-09-02 04:14:00 | NOAA-20 | LAGOA DO TOCANTINS | TOCANTINS | Brasil | 1711951 | 17 | 33 | nan | nan | nan | Cerrado | 2.1 |
| 8cf91ee6-735d-31f0-a94a-6c4202a462ff | -8.20201 | -49.52529 | 2025-09-02 04:14:00 | NOAA-20 | CONCEIÇÃO DO ARAGUAIA | PARÁ | Brasil | 1502707 | 15 | 33 | nan | nan | nan | Amazônia | 1.3 |
| 888f7672-a5c8-38d0-96a6-f476f4080255 | -14.0487 | -44.54779 | 2025-09-02 04:14:00 | NOAA-20 | COCOS | BAHIA | Brasil | 2908101 | 29 | 33 | nan | nan | nan | Cerrado | 0.9 |
| 4646808b-028b-3b6f-8984-152648f77bba | -10.0626 | -48.12767 | 2025-09-02 04:14:00 | NOAA-20 | APARECIDA DO RIO NEGRO | TOCANTINS | Brasil | 1701101 | 17 | 33 | nan | nan | nan | Cerrado | 4.4 |
| 28ee18d2-134f-3d20-8ba0-ab82d87a9feb | -10.44483 | -54.77634 | 2025-09-02 04:14:00 | NOAA-20 | TERRA NOVA DO NORTE | MATO GROSSO | Brasil | 5108055 | 51 | 33 | nan | nan | nan | Amazônia | 7.3 |
| cb399c6b-5f87-3965-8a06-ad8c8b35803f | -12.0708 | -45.80832 | 2025-09-02 04:14:00 | NOAA-20 | LUÍS EDUARDO MAGALHÃES | BAHIA | Brasil | 2919553 | 29 | 33 | nan | nan | nan | Cerrado | 3.0 |
| 3e2b0889-7229-3426-ad3e-62aa77f65557 | -6.83395 | -52.81515 | 2025-09-02 04:14:00 | NOAA-20 | SÃO FÉLIX DO XINGU | PARÁ | Brasil | 1507300 | 15 | 33 | nan | nan | nan | Amazônia | 1.1 |
| 56f45855-08c0-383d-9397-3a7308d39c49 | -11.04931 | -46.89914 | 2025-09-02 04:14:00 | NOAA-20 | PONTE ALTA DO TOCANTINS | TOCANTINS | Brasil | 1717909 | 17 | 33 | nan | nan | nan | Cerrado | 2.3 |
| 908e4e1d-b7ef-36be-93c1-d6bd4752b4e8 | -7.4707 | -44.81659 | 2025-09-02 04:14:00 | NOAA-20 | URUÇUÍ | PIAUÍ | Brasil | 2211209 | 22 | 33 | nan | nan | nan | Cerrado | 1.5 |
| 2bb7a04d-1cfd-3c55-a139-12d66f6ddc8b | -11.31154 | -55.21266 | 2025-09-02 04:14:00 | NOAA-20 | CLÁUDIA | MATO GROSSO | Brasil | 5103056 | 51 | 33 | nan | nan | nan | Amazônia | 0.9 |
| 88f9a54b-aeb0-332e-83e3-e7edcf35e753 | -11.80526 | -46.40144 | 2025-09-02 04:14:00 | NOAA-20 | PONTE ALTA DO BOM JESUS | TOCANTINS | Brasil | 1717800 | 17 | 33 | nan | nan | nan | Cerrado | 10.3 |


[Clique aqui para ver as próximas entradas](README33.md)
