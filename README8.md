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

## Dados Diários - Página 8

| ID | Latitude | Longitude | Data/Hora GMT | Satélite | Município | Estado | País | Município ID | Estado ID | País ID | Dias sem Chuva | Precipitação | Risco de Fogo | Bioma | FRP |
|----|----------|-----------|---------------|----------|-----------|--------|------|--------------|-----------|---------|----------------|--------------|----------------|-------|-----|
| a9ebd4c5-126d-38b0-8077-d62550841a80 | -5.6592 | -51.63657 | 2025-09-10 00:33:00 | TERRA_M-M | SÃO FÉLIX DO XINGU | PARÁ | Brasil | 1507300 | 15 | 33 | nan | nan | nan | Amazônia | 7.4 |
| b3a83abf-b4e9-3051-9f53-f17a433b99d4 | -8.48956 | -45.66465 | 2025-09-10 00:33:00 | TERRA_M-M | SANTA FILOMENA | PIAUÍ | Brasil | 2209203 | 22 | 33 | nan | nan | nan | Cerrado | 8.4 |
| 18c3fde1-ff30-3740-aa91-c56b12a1a6c3 | -7.59886 | -49.29662 | 2025-09-10 00:33:00 | TERRA_M-M | PAU D'ARCO | TOCANTINS | Brasil | 1716307 | 17 | 33 | nan | nan | nan | Amazônia | 12.4 |
| 1fc47617-7ca1-356c-b507-e74de2cf8971 | -8.52629 | -51.38349 | 2025-09-10 00:33:00 | TERRA_M-M | CUMARU DO NORTE | PARÁ | Brasil | 1502764 | 15 | 33 | nan | nan | nan | Amazônia | 11.0 |
| 0d010bee-7bd7-30c9-b5d3-8a69c0bab1ad | -6.83705 | -51.89542 | 2025-09-10 00:33:00 | TERRA_M-M | SÃO FÉLIX DO XINGU | PARÁ | Brasil | 1507300 | 15 | 33 | nan | nan | nan | Amazônia | 9.3 |
| d09c2980-0bb5-3486-8602-0a4300a55a45 | -8.49281 | -44.6468 | 2025-09-10 00:33:00 | TERRA_M-M | PALMEIRA DO PIAUÍ | PIAUÍ | Brasil | 2207405 | 22 | 33 | nan | nan | nan | Cerrado | 7.9 |
| ce59e8b7-68ab-3cf3-a71c-1cd72f8d9eed | -6.36473 | -48.16383 | 2025-09-10 00:33:00 | TERRA_M-M | RIACHINHO | TOCANTINS | Brasil | 1718550 | 17 | 33 | nan | nan | nan | Amazônia | 7.6 |
| b6323369-0d38-3ad7-a7a3-18b85063b1a5 | -6.85025 | -44.89907 | 2025-09-10 00:33:00 | TERRA_M-M | SÃO FÉLIX DE BALSAS | MARANHÃO | Brasil | 2110807 | 21 | 33 | nan | nan | nan | Cerrado | 9.0 |
| 07fa6911-1e90-39ef-aeaf-b13d56ed19bc | -7.78363 | -46.06087 | 2025-09-10 00:33:00 | TERRA_M-M | BALSAS | MARANHÃO | Brasil | 2101400 | 21 | 33 | nan | nan | nan | Cerrado | 67.9 |
| 958c26bb-fe03-32ad-bcfc-81e5a042b812 | -6.6753 | -49.75552 | 2025-09-10 00:33:00 | TERRA_M-M | ÁGUA AZUL DO NORTE | PARÁ | Brasil | 1500347 | 15 | 33 | nan | nan | nan | Amazônia | 6.2 |
| 75dbfc65-36dd-31c0-8389-54aa33d23535 | -5.75065 | -47.46865 | 2025-09-10 00:33:00 | TERRA_M-M | GOVERNADOR EDISON LOBÃO | MARANHÃO | Brasil | 2104552 | 21 | 33 | nan | nan | nan | Cerrado | 27.1 |
| 4e9a217c-258e-322b-8407-eb14e509029c | -6.263 | -43.40737 | 2025-09-10 00:33:00 | TERRA_M-M | LAGOA DO MATO | MARANHÃO | Brasil | 2105922 | 21 | 33 | nan | nan | nan | Cerrado | 73.6 |
| c14a2059-348c-3a46-802c-6d87a8c5d3ad | -7.48992 | -48.2362 | 2025-09-10 00:33:00 | TERRA_M-M | ARAGUAÍNA | TOCANTINS | Brasil | 1702109 | 17 | 33 | nan | nan | nan | Cerrado | 14.2 |
| f254cfcd-6a25-36aa-9e39-4603d7c83d57 | -9.06614 | -45.75782 | 2025-09-10 00:33:00 | TERRA_M-M | SANTA FILOMENA | PIAUÍ | Brasil | 2209203 | 22 | 33 | nan | nan | nan | Cerrado | 6.7 |
| 65d84beb-55b2-329e-ba86-01dc891ff91d | -5.65843 | -43.9081 | 2025-09-10 00:33:00 | TERRA_M-M | BURITI BRAVO | MARANHÃO | Brasil | 2102309 | 21 | 33 | nan | nan | nan | Cerrado | 12.8 |
| fe4cdb5d-576d-37cf-ba11-0b040ccdfd28 | -6.85592 | -47.91296 | 2025-09-10 00:33:00 | TERRA_M-M | WANDERLÂNDIA | TOCANTINS | Brasil | 1722081 | 17 | 33 | nan | nan | nan | Cerrado | 11.2 |
| 0aaceeb8-c25f-37a4-b0e0-f08f79fda26e | -10.56302 | -49.44143 | 2025-09-10 00:33:00 | TERRA_M-M | CRISTALÂNDIA | TOCANTINS | Brasil | 1706100 | 17 | 33 | nan | nan | nan | Cerrado | 44.4 |
| 498b531c-8edb-36ca-a3a4-b542c00aafdd | -7.37292 | -49.53438 | 2025-09-10 00:33:00 | TERRA_M-M | FLORESTA DO ARAGUAIA | PARÁ | Brasil | 1503044 | 15 | 33 | nan | nan | nan | Amazônia | 13.7 |
| b88c30b6-d284-3505-9081-43bd7d51aaf5 | -6.8584 | -47.93066 | 2025-09-10 00:33:00 | TERRA_M-M | WANDERLÂNDIA | TOCANTINS | Brasil | 1722081 | 17 | 33 | nan | nan | nan | Cerrado | 18.8 |
| ae25b588-e4e3-3543-b72e-d1240e82923d | -5.22348 | -43.6954 | 2025-09-10 00:33:00 | TERRA_M-M | CAXIAS | MARANHÃO | Brasil | 2103000 | 21 | 33 | nan | nan | nan | Cerrado | 36.1 |
| 491acf9d-47f3-30b5-814a-b3a8c49f3ef9 | -8.21299 | -45.79646 | 2025-09-10 00:33:00 | TERRA_M-M | TASSO FRAGOSO | MARANHÃO | Brasil | 2112001 | 21 | 33 | nan | nan | nan | Cerrado | 16.4 |
| 7d97bf94-5ea7-3dff-8ea5-14ea7dc3c36d | -5.9324 | -42.79052 | 2025-09-10 00:33:00 | TERRA_M-M | PALMEIRAIS | PIAUÍ | Brasil | 2207504 | 22 | 33 | nan | nan | nan | Caatinga | 16.1 |
| c29abb88-236a-3002-8cb4-efa6778026e4 | -3.64203 | -49.20389 | 2025-09-10 00:33:00 | TERRA_M-M | GOIANÉSIA DO PARÁ | PARÁ | Brasil | 1503093 | 15 | 33 | nan | nan | nan | Amazônia | 9.0 |
| 95a46c8e-2aa4-3ffe-9de8-51619876f5a8 | -6.85197 | -44.91094 | 2025-09-10 00:33:00 | TERRA_M-M | SÃO FÉLIX DE BALSAS | MARANHÃO | Brasil | 2110807 | 21 | 33 | nan | nan | nan | Cerrado | 26.1 |
| 480a2527-2124-31ec-b4d1-a68938f3e63b | -10.27792 | -48.8195 | 2025-09-10 00:33:00 | TERRA_M-M | PARAÍSO DO TOCANTINS | TOCANTINS | Brasil | 1716109 | 17 | 33 | nan | nan | nan | Cerrado | 26.4 |
| bc6f635a-13ad-3997-bfc2-da97baf95bc3 | -7.79228 | -46.074 | 2025-09-10 00:33:00 | TERRA_M-M | BALSAS | MARANHÃO | Brasil | 2101400 | 21 | 33 | nan | nan | nan | Cerrado | 14.3 |
| 8e270560-a0a6-34ad-9ce5-1d32bf0a1848 | -10.29811 | -48.82948 | 2025-09-10 00:33:00 | TERRA_M-M | PARAÍSO DO TOCANTINS | TOCANTINS | Brasil | 1716109 | 17 | 33 | nan | nan | nan | Cerrado | 6.1 |
| cdabecf7-686b-3721-87eb-4f481f99c3cf | -5.39849 | -48.84964 | 2025-09-10 00:33:00 | TERRA_M-M | SÃO JOÃO DO ARAGUAIA | PARÁ | Brasil | 1507508 | 15 | 33 | nan | nan | nan | Amazônia | 5.3 |
| 39636cce-a913-3eab-be31-2e0ace401eaa | -8.86228 | -45.86735 | 2025-09-10 00:33:00 | TERRA_M-M | SANTA FILOMENA | PIAUÍ | Brasil | 2209203 | 22 | 33 | nan | nan | nan | Cerrado | 35.6 |
| d996350c-950c-3ee2-8b73-bbc9cf67829d | -8.98357 | -46.07304 | 2025-09-10 00:33:00 | TERRA_M-M | ALTO PARNAÍBA | MARANHÃO | Brasil | 2100501 | 21 | 33 | nan | nan | nan | Cerrado | 12.7 |
| 9ee3d92e-a390-32e0-a97f-60f8ec0d2ba6 | -5.68904 | -43.33968 | 2025-09-10 00:33:00 | TERRA_M-M | PARNARAMA | MARANHÃO | Brasil | 2107803 | 21 | 33 | nan | nan | nan | Cerrado | 16.5 |
| 4ab3f6da-4abb-3047-936d-03e46de5048a | -8.47556 | -47.30624 | 2025-09-10 00:33:00 | TERRA_M-M | ITACAJÁ | TOCANTINS | Brasil | 1710508 | 17 | 33 | nan | nan | nan | Cerrado | 7.0 |
| 3df185e1-f18f-3a80-85ed-0b8e6b0d6268 | -6.2539 | -43.42471 | 2025-09-10 00:33:00 | TERRA_M-M | LAGOA DO MATO | MARANHÃO | Brasil | 2105922 | 21 | 33 | nan | nan | nan | Cerrado | 43.0 |
| 14e75d09-1aad-380d-bc1a-62570cede7f0 | -5.7254 | -45.40548 | 2025-09-10 00:33:00 | TERRA_M-M | BARRA DO CORDA | MARANHÃO | Brasil | 2101608 | 21 | 33 | nan | nan | nan | Cerrado | 9.4 |
| c9322e01-9e7a-3042-ac55-649706bb6933 | -5.66579 | -43.34293 | 2025-09-10 00:33:00 | TERRA_M-M | PARNARAMA | MARANHÃO | Brasil | 2107803 | 21 | 33 | nan | nan | nan | Cerrado | 12.6 |
| fbd4c14a-6d4e-3c71-a48d-eda047db52ef | -5.72804 | -51.68951 | 2025-09-10 00:33:00 | TERRA_M-M | SÃO FÉLIX DO XINGU | PARÁ | Brasil | 1507300 | 15 | 33 | nan | nan | nan | Amazônia | 16.1 |
| cc86ff64-22b8-32b9-ab50-bf2fbcbb1b6c | -9.0769 | -45.76643 | 2025-09-10 00:33:00 | TERRA_M-M | SANTA FILOMENA | PIAUÍ | Brasil | 2209203 | 22 | 33 | nan | nan | nan | Cerrado | 29.5 |
| 17fb1939-abe6-33e1-b38f-d0738a2c4119 | -9.67226 | -46.63865 | 2025-09-10 00:33:00 | TERRA_M-M | LIZARDA | TOCANTINS | Brasil | 1712405 | 17 | 33 | nan | nan | nan | Cerrado | 10.8 |
| 7dba03d7-02c9-32f2-a81e-1a6d46f10283 | -6.16702 | -43.3812 | 2025-09-10 00:33:00 | TERRA_M-M | LAGOA DO MATO | MARANHÃO | Brasil | 2105922 | 21 | 33 | nan | nan | nan | Cerrado | 29.2 |
| 34b5f3a7-1072-3900-8438-e3f2508518e8 | -5.79741 | -51.67992 | 2025-09-10 00:33:00 | TERRA_M-M | SÃO FÉLIX DO XINGU | PARÁ | Brasil | 1507300 | 15 | 33 | nan | nan | nan | Amazônia | 11.4 |
| a05cb7db-b864-3b0f-bacc-57a67096be28 | -5.42846 | -43.99043 | 2025-09-10 00:33:00 | TERRA_M-M | GOVERNADOR EUGÊNIO BARROS | MARANHÃO | Brasil | 2104602 | 21 | 33 | nan | nan | nan | Cerrado | 29.3 |
| 247c83b8-59f0-38e1-9b64-cf7a3cd5817e | -9.35421 | -49.00099 | 2025-09-10 00:33:00 | TERRA_M-M | DOIS IRMÃOS DO TOCANTINS | TOCANTINS | Brasil | 1707207 | 17 | 33 | nan | nan | nan | Cerrado | 23.2 |
| d0476497-8a07-3c0e-9e22-63d3484c35b9 | -7.36968 | -47.43867 | 2025-09-10 00:33:00 | TERRA_M-M | CAROLINA | MARANHÃO | Brasil | 2102804 | 21 | 33 | nan | nan | nan | Cerrado | 7.1 |
| 4270e437-b2fc-35e7-b498-98ad0565b1c5 | -7.78504 | -46.07081 | 2025-09-10 00:33:00 | TERRA_M-M | BALSAS | MARANHÃO | Brasil | 2101400 | 21 | 33 | nan | nan | nan | Cerrado | 47.4 |
| feb2e226-e480-39d9-9813-e0f4482c7931 | -6.69002 | -46.41618 | 2025-09-10 00:33:00 | TERRA_M-M | FORMOSA DA SERRA NEGRA | MARANHÃO | Brasil | 2104099 | 21 | 33 | nan | nan | nan | Cerrado | 8.1 |
| 40850185-9db5-38a3-9392-4cd6394e268d | -7.62324 | -47.99782 | 2025-09-10 00:33:00 | TERRA_M-M | PALMEIRANTE | TOCANTINS | Brasil | 1715705 | 17 | 33 | nan | nan | nan | Cerrado | 5.7 |
| 6d146d00-44d4-3449-a883-f29b8c11a395 | -5.58238 | -45.0511 | 2025-09-10 00:33:00 | TERRA_M-M | BARRA DO CORDA | MARANHÃO | Brasil | 2101608 | 21 | 33 | nan | nan | nan | Cerrado | 38.9 |
| 189088b7-0eb9-363c-a804-b9a38444a2c5 | -7.86531 | -46.25289 | 2025-09-10 00:33:00 | TERRA_M-M | BALSAS | MARANHÃO | Brasil | 2101400 | 21 | 33 | nan | nan | nan | Cerrado | 23.3 |
| f13da4ce-2324-3bc2-bfbd-4c8e03f17b25 | -8.04889 | -48.68736 | 2025-09-10 00:33:00 | TERRA_M-M | BANDEIRANTES DO TOCANTINS | TOCANTINS | Brasil | 1703057 | 17 | 33 | nan | nan | nan | Amazônia | 178.3 |
| 6db69f9d-f609-38ed-a135-1c92df8e117c | -6.05884 | -43.13651 | 2025-09-10 00:33:00 | TERRA_M-M | SÃO FRANCISCO DO MARANHÃO | MARANHÃO | Brasil | 2110906 | 21 | 33 | nan | nan | nan | Caatinga | 15.8 |
| b094bdf4-bc10-33ac-a598-8959d12314ec | -6.87869 | -47.88266 | 2025-09-10 00:33:00 | TERRA_M-M | WANDERLÂNDIA | TOCANTINS | Brasil | 1722081 | 17 | 33 | nan | nan | nan | Cerrado | 108.8 |
| 4703f7ff-d525-358c-9ea6-96921bedda16 | -9.76044 | -51.06183 | 2025-09-10 00:33:00 | TERRA_M-M | SANTANA DO ARAGUAIA | PARÁ | Brasil | 1506708 | 15 | 33 | nan | nan | nan | Amazônia | 10.9 |
| 29e03c12-3438-305f-9145-80c60effb521 | -8.05526 | -48.66816 | 2025-09-10 00:33:00 | TERRA_M-M | BANDEIRANTES DO TOCANTINS | TOCANTINS | Brasil | 1703057 | 17 | 33 | nan | nan | nan | Amazônia | 10.8 |
| adb89152-ff71-3124-b285-ed608694048e | -9.69678 | -46.81203 | 2025-09-10 00:33:00 | TERRA_M-M | LIZARDA | TOCANTINS | Brasil | 1712405 | 17 | 33 | nan | nan | nan | Cerrado | 10.1 |
| ee929c98-6a14-3a67-aab9-276c7943def0 | -8.07406 | -48.65918 | 2025-09-10 00:33:00 | TERRA_M-M | BANDEIRANTES DO TOCANTINS | TOCANTINS | Brasil | 1703057 | 17 | 33 | nan | nan | nan | Amazônia | 7.6 |
| 961e621c-ee03-3144-9518-4da81aa820db | -7.4887 | -48.22737 | 2025-09-10 00:33:00 | TERRA_M-M | ARAGUAÍNA | TOCANTINS | Brasil | 1702109 | 17 | 33 | nan | nan | nan | Cerrado | 4.8 |
| a5ef3f90-0127-3f89-a32b-091af65a6415 | -8.49901 | -45.66348 | 2025-09-10 00:33:00 | TERRA_M-M | SANTA FILOMENA | PIAUÍ | Brasil | 2209203 | 22 | 33 | nan | nan | nan | Cerrado | 10.2 |
| d435fb96-5aca-3889-9462-f77deef96825 | -7.66536 | -50.27258 | 2025-09-10 00:33:00 | TERRA_M-M | PAU D'ARCO | PARÁ | Brasil | 1505551 | 15 | 33 | nan | nan | nan | Amazônia | 6.5 |
| 6470e9ae-64ae-37af-b85d-5ad856adfd59 | -10.29561 | -48.81068 | 2025-09-10 00:33:00 | TERRA_M-M | PARAÍSO DO TOCANTINS | TOCANTINS | Brasil | 1716109 | 17 | 33 | nan | nan | nan | Cerrado | 25.4 |
| 31a95c04-b2fe-3dde-abdf-81ab589d10b8 | -7.44684 | -49.26486 | 2025-09-10 00:33:00 | TERRA_M-M | PAU D'ARCO | TOCANTINS | Brasil | 1716307 | 17 | 33 | nan | nan | nan | Amazônia | 14.7 |
| 22e8a5ce-c51b-3036-86fa-4d983a4c5e67 | -8.50131 | -51.34493 | 2025-09-10 00:33:00 | TERRA_M-M | CUMARU DO NORTE | PARÁ | Brasil | 1502764 | 15 | 33 | nan | nan | nan | Amazônia | 8.2 |
| 5e20d31b-f817-3468-bf4e-6c3917660294 | -8.0652 | -48.66039 | 2025-09-10 00:33:00 | TERRA_M-M | BANDEIRANTES DO TOCANTINS | TOCANTINS | Brasil | 1703057 | 17 | 33 | nan | nan | nan | Amazônia | 26.9 |
| 601d85e9-f163-3837-abc8-9b7823f8214f | -5.86428 | -48.15472 | 2025-09-10 00:33:00 | TERRA_M-M | ARAGUATINS | TOCANTINS | Brasil | 1702208 | 17 | 33 | nan | nan | nan | Amazônia | 21.5 |
| 5c557272-42cf-3090-a776-ceb7848cbfdc | -4.50071 | -47.82581 | 2025-09-10 00:33:00 | TERRA_M-M | DOM ELISEU | PARÁ | Brasil | 1502939 | 15 | 33 | nan | nan | nan | Amazônia | 11.7 |
| 1b9e6cb2-d8c8-3ba9-8b0e-730a6029b42d | -6.2425 | -43.42657 | 2025-09-10 00:33:00 | TERRA_M-M | LAGOA DO MATO | MARANHÃO | Brasil | 2105922 | 21 | 33 | nan | nan | nan | Cerrado | 14.3 |
| cbba02ef-dca5-3736-9bb7-9e8aad27f15b | -9.09323 | -46.98046 | 2025-09-10 00:33:00 | TERRA_M-M | LIZARDA | TOCANTINS | Brasil | 1712405 | 17 | 33 | nan | nan | nan | Cerrado | 18.4 |
| 746f8a3e-2491-3204-a9d6-11bf1a5a7459 | -8.41146 | -49.1096 | 2025-09-10 00:33:00 | TERRA_M-M | COUTO MAGALHÃES | TOCANTINS | Brasil | 1706001 | 17 | 33 | nan | nan | nan | Cerrado | 18.6 |
| e1f2055c-b924-3728-9bc3-6db2428ef774 | -8.07031 | -50.19294 | 2025-09-10 00:33:00 | TERRA_M-M | REDENÇÃO | PARÁ | Brasil | 1506138 | 15 | 33 | nan | nan | nan | Amazônia | 18.7 |
| 8d6bc0f7-bd25-3aa5-90bb-c6e5a5493bca | -10.19624 | -46.82823 | 2025-09-10 00:33:00 | TERRA_M-M | MATEIROS | TOCANTINS | Brasil | 1712702 | 17 | 33 | nan | nan | nan | Cerrado | 11.0 |
| da185a27-b63b-3f4f-98b8-5a8b1347b102 | -5.97578 | -47.4274 | 2025-09-10 00:33:00 | TERRA_M-M | RIBAMAR FIQUENE | MARANHÃO | Brasil | 2109551 | 21 | 33 | nan | nan | nan | Cerrado | 6.6 |
| 6ee935e9-1b78-3a00-bea7-fc3ce4a67e51 | -9.44215 | -46.7097 | 2025-09-10 00:33:00 | TERRA_M-M | LIZARDA | TOCANTINS | Brasil | 1712405 | 17 | 33 | nan | nan | nan | Cerrado | 73.0 |
| a9dfdb2f-8fac-3592-97ac-53ca3611a8d2 | -8.43185 | -49.1254 | 2025-09-10 00:33:00 | TERRA_M-M | COUTO MAGALHÃES | TOCANTINS | Brasil | 1706001 | 17 | 33 | nan | nan | nan | Cerrado | 11.7 |
| 8013f411-02c4-3935-8ee6-04e2ac89b91f | -9.99717 | -51.70483 | 2025-09-10 00:33:00 | TERRA_M-M | VILA RICA | MATO GROSSO | Brasil | 5108600 | 51 | 33 | nan | nan | nan | Amazônia | 7.5 |
| ef204526-985c-3e11-9cc0-b35e0597a4e2 | -6.85716 | -47.92181 | 2025-09-10 00:33:00 | TERRA_M-M | WANDERLÂNDIA | TOCANTINS | Brasil | 1722081 | 17 | 33 | nan | nan | nan | Cerrado | 13.7 |
| e4f89a82-ab99-3165-8cf8-e3e952171b96 | -5.93987 | -45.82146 | 2025-09-10 00:33:00 | TERRA_M-M | GRAJAÚ | MARANHÃO | Brasil | 2104800 | 21 | 33 | nan | nan | nan | Cerrado | 11.3 |
| 62630548-6da7-3652-8a39-a9d4e4a0d345 | -10.47253 | -47.94366 | 2025-09-10 00:33:00 | TERRA_M-M | MONTE DO CARMO | TOCANTINS | Brasil | 1713601 | 17 | 33 | nan | nan | nan | Cerrado | 5.0 |
| 439fd12c-dccc-3ef5-bd7c-878ff00a169e | -10.02718 | -51.68761 | 2025-09-10 00:33:00 | TERRA_M-M | VILA RICA | MATO GROSSO | Brasil | 5108600 | 51 | 33 | nan | nan | nan | Amazônia | 21.1 |
| 687513b6-ba5e-36d9-b8ab-4494e56c3195 | -9.08689 | -47.06434 | 2025-09-10 00:33:00 | TERRA_M-M | LIZARDA | TOCANTINS | Brasil | 1712405 | 17 | 33 | nan | nan | nan | Cerrado | 10.0 |
| a92ba357-f249-3da8-ace6-82dbaef92863 | -6.44503 | -47.02926 | 2025-09-10 00:33:00 | TERRA_M-M | SÃO JOÃO DO PARAÍSO | MARANHÃO | Brasil | 2111052 | 21 | 33 | nan | nan | nan | Cerrado | 6.5 |
| ce9c4662-9c7b-38b1-ac5d-6668c7fb49c3 | -5.73839 | -45.28032 | 2025-09-10 00:33:00 | TERRA_M-M | BARRA DO CORDA | MARANHÃO | Brasil | 2101608 | 21 | 33 | nan | nan | nan | Cerrado | 8.9 |
| bba28b10-888c-302c-a7ff-92a2e4b1767b | -5.53562 | -42.64946 | 2025-09-10 00:33:00 | TERRA_M-M | MONSENHOR GIL | PIAUÍ | Brasil | 2206407 | 22 | 33 | nan | nan | nan | Caatinga | 20.4 |
| 6a61a12c-c0c0-34f0-be50-d7cc0fd66b33 | -5.64733 | -43.90968 | 2025-09-10 00:33:00 | TERRA_M-M | FORTUNA | MARANHÃO | Brasil | 2104206 | 21 | 33 | nan | nan | nan | Cerrado | 9.6 |
| 4cd62e1c-66b0-3293-a699-458c34bcda5e | -6.17285 | -45.81838 | 2025-09-10 00:33:00 | TERRA_M-M | GRAJAÚ | MARANHÃO | Brasil | 2104800 | 21 | 33 | nan | nan | nan | Cerrado | 12.4 |
| 805495a7-cb26-381b-b862-5b21c7cdf339 | -5.79657 | -44.84003 | 2025-09-10 00:33:00 | TERRA_M-M | TUNTUM | MARANHÃO | Brasil | 2112308 | 21 | 33 | nan | nan | nan | Cerrado | 8.8 |
| ea9f9d42-c77e-3dcd-894b-3d8c3d523e19 | -4.48255 | -42.92701 | 2025-09-10 00:33:00 | TERRA_M-M | CAXIAS | MARANHÃO | Brasil | 2103000 | 21 | 33 | nan | nan | nan | Cerrado | 17.0 |
| 6cc78a12-1724-3ba9-845b-7010704936e3 | -9.5209 | -46.54511 | 2025-09-10 00:33:00 | TERRA_M-M | ALTO PARNAÍBA | MARANHÃO | Brasil | 2100501 | 21 | 33 | nan | nan | nan | Cerrado | 19.4 |
| 40389b8c-b44d-3180-af6c-1d2f61512eaf | -11.29856 | -53.96581 | 2025-09-10 00:33:00 | TERRA_M-M | UNIÃO DO SUL | MATO GROSSO | Brasil | 5108303 | 51 | 33 | nan | nan | nan | Amazônia | 13.3 |
| c4089f9a-b403-3b47-be62-85ef2df0a43b | -5.66907 | -51.63524 | 2025-09-10 00:33:00 | TERRA_M-M | SÃO FÉLIX DO XINGU | PARÁ | Brasil | 1507300 | 15 | 33 | nan | nan | nan | Amazônia | 13.7 |
| 197d484f-fad3-3c12-9b4f-53259782820a | -8.86814 | -45.86051 | 2025-09-10 00:33:00 | TERRA_M-M | SANTA FILOMENA | PIAUÍ | Brasil | 2209203 | 22 | 33 | nan | nan | nan | Cerrado | 109.4 |
| d51f2fc9-9dfe-3547-96a9-bc8b859418c3 | -9.44086 | -46.70055 | 2025-09-10 00:33:00 | TERRA_M-M | LIZARDA | TOCANTINS | Brasil | 1712405 | 17 | 33 | nan | nan | nan | Cerrado | 70.1 |
| 14d38d16-ee70-3ab6-8bab-a21c284cc248 | -8.04516 | -48.66035 | 2025-09-10 00:33:00 | TERRA_M-M | COLINAS DO TOCANTINS | TOCANTINS | Brasil | 1705508 | 17 | 33 | nan | nan | nan | Amazônia | 22.2 |
| 4fee1bce-bb81-3ee2-9c56-e3c05b29c26f | -9.35546 | -49.01024 | 2025-09-10 00:33:00 | TERRA_M-M | DOIS IRMÃOS DO TOCANTINS | TOCANTINS | Brasil | 1707207 | 17 | 33 | nan | nan | nan | Cerrado | 12.4 |
| 78586a4d-8388-34d5-a7dd-93f99b74d9c7 | -10.15747 | -48.88017 | 2025-09-10 00:33:00 | TERRA_M-M | PARAÍSO DO TOCANTINS | TOCANTINS | Brasil | 1716109 | 17 | 33 | nan | nan | nan | Cerrado | 12.4 |
| 0538c59f-eff2-3851-8484-e8cd66660f49 | -5.74172 | -47.46999 | 2025-09-10 00:33:00 | TERRA_M-M | GOVERNADOR EDISON LOBÃO | MARANHÃO | Brasil | 2104552 | 21 | 33 | nan | nan | nan | Cerrado | 58.3 |
| 5315bc7f-536c-34cb-a157-13d27318f898 | -9.06945 | -49.83156 | 2025-09-10 00:33:00 | TERRA_M-M | ARAGUACEMA | TOCANTINS | Brasil | 1701903 | 17 | 33 | nan | nan | nan | Cerrado | 9.4 |
| 44786af0-b0f1-328e-b341-1064ac6b27d6 | -9.05347 | -50.48372 | 2025-09-10 00:33:00 | TERRA_M-M | SANTANA DO ARAGUAIA | PARÁ | Brasil | 1506708 | 15 | 33 | nan | nan | nan | Amazônia | 21.7 |
| 3a66f633-6e6c-33ae-bfb9-ab583dd491bf | -8.16149 | -46.07541 | 2025-09-10 00:33:00 | TERRA_M-M | TASSO FRAGOSO | MARANHÃO | Brasil | 2112001 | 21 | 33 | nan | nan | nan | Cerrado | 6.0 |
| 260b719d-f0d2-397d-a898-1961e44955df | -8.26347 | -49.92697 | 2025-09-10 00:33:00 | TERRA_M-M | REDENÇÃO | PARÁ | Brasil | 1506138 | 15 | 33 | nan | nan | nan | Amazônia | 18.0 |
| 2076c9fd-07e0-36d7-a032-c552d2df206d | -5.55912 | -45.17601 | 2025-09-10 00:33:00 | TERRA_M-M | BARRA DO CORDA | MARANHÃO | Brasil | 2101608 | 21 | 33 | nan | nan | nan | Cerrado | 17.9 |
| 14aa255a-2ed5-3bd6-81bc-0b90286d0cab | -3.63322 | -49.20513 | 2025-09-10 00:33:00 | TERRA_M-M | GOIANÉSIA DO PARÁ | PARÁ | Brasil | 1503093 | 15 | 33 | nan | nan | nan | Amazônia | 18.3 |


[Clique aqui para ver as próximas entradas](README9.md)
