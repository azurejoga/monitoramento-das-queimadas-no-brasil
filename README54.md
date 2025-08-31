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

## Dados Diários - Página 54

| ID | Latitude | Longitude | Data/Hora GMT | Satélite | Município | Estado | País | Município ID | Estado ID | País ID | Dias sem Chuva | Precipitação | Risco de Fogo | Bioma | FRP |
|----|----------|-----------|---------------|----------|-----------|--------|------|--------------|-----------|---------|----------------|--------------|----------------|-------|-----|
| dc14fadd-b38b-30aa-83f7-bec715e3d964 | -6.94398 | -44.05578 | 2025-08-31 04:49:00 | NOAA-20 | PORTO ALEGRE DO PIAUÍ | PIAUÍ | Brasil | 2208551 | 22 | 33 | nan | nan | nan | Cerrado | 1.4 |
| 70b4fb2c-af06-318b-8b33-a2f897313d41 | -7.58543 | -42.70952 | 2025-08-31 04:49:00 | NOAA-20 | FLORES DO PIAUÍ | PIAUÍ | Brasil | 2203800 | 22 | 33 | nan | nan | nan | Caatinga | 1.9 |
| bb4ac7e9-4a4d-38f7-ba20-ec49ab30779b | -7.08326 | -44.33184 | 2025-08-31 04:49:00 | NOAA-20 | BENEDITO LEITE | MARANHÃO | Brasil | 2101806 | 21 | 33 | nan | nan | nan | Cerrado | 0.4 |
| 7538d1bf-0031-3a8c-a2a9-14af1f77d356 | -3.59029 | -47.52362 | 2025-08-31 04:49:00 | NOAA-20 | ULIANÓPOLIS | PARÁ | Brasil | 1508126 | 15 | 33 | nan | nan | nan | Amazônia | 9.4 |
| 7d6acf33-8cf8-3785-b265-ba7bb136341b | -6.77057 | -43.76404 | 2025-08-31 04:49:00 | NOAA-20 | GUADALUPE | PIAUÍ | Brasil | 2204501 | 22 | 33 | nan | nan | nan | Cerrado | 1.2 |
| 4e40304b-5e0c-36e5-8e12-776fca9a7706 | -6.17271 | -44.13298 | 2025-08-31 04:49:00 | NOAA-20 | COLINAS | MARANHÃO | Brasil | 2103505 | 21 | 33 | nan | nan | nan | Cerrado | 1.0 |
| 3874f302-9961-3fc6-8ac4-2dc47ff26197 | -4.2706 | -48.64332 | 2025-08-31 04:49:00 | NOAA-20 | RONDON DO PARÁ | PARÁ | Brasil | 1506187 | 15 | 33 | nan | nan | nan | Amazônia | 2.0 |
| 7a26b86f-3873-33a5-8b6b-e496f0722d50 | -8.19977 | -42.31021 | 2025-08-31 04:49:00 | NOAA-20 | SÃO JOÃO DO PIAUÍ | PIAUÍ | Brasil | 2210003 | 22 | 33 | nan | nan | nan | Caatinga | 1.0 |
| ab6c28d9-3e58-3e3d-a46a-27e5d4d31c47 | -6.95338 | -42.01583 | 2025-08-31 04:49:00 | NOAA-20 | OEIRAS | PIAUÍ | Brasil | 2207009 | 22 | 33 | nan | nan | nan | Caatinga | 1.5 |
| b196d3d5-ada7-3e04-b8f5-a3ed91c357d4 | -6.17831 | -43.56247 | 2025-08-31 04:49:00 | NOAA-20 | PASSAGEM FRANCA | MARANHÃO | Brasil | 2107902 | 21 | 33 | nan | nan | nan | Cerrado | 1.1 |
| a35b6fd3-2ce9-3534-8f21-6be321053e5e | -7.4899 | -45.0578 | 2025-08-31 04:49:00 | NOAA-20 | SÃO FÉLIX DE BALSAS | MARANHÃO | Brasil | 2110807 | 21 | 33 | nan | nan | nan | Cerrado | 2.5 |
| dcd70fcd-b2a8-31cf-906b-3b7a4a808aaa | -2.26744 | -47.85723 | 2025-08-31 04:49:00 | NOAA-20 | AURORA DO PARÁ | PARÁ | Brasil | 1500958 | 15 | 33 | nan | nan | nan | Amazônia | 3.0 |
| 1f7625c2-11a1-3fa7-8074-819ac8608198 | -3.79061 | -52.15684 | 2025-08-31 04:49:00 | NOAA-20 | SENADOR JOSÉ PORFÍRIO | PARÁ | Brasil | 1507805 | 15 | 33 | nan | nan | nan | Amazônia | 1.1 |
| b072d088-3abb-3d16-9800-042e8f59f5f0 | -8.19073 | -42.30679 | 2025-08-31 04:49:00 | NOAA-20 | SÃO JOÃO DO PIAUÍ | PIAUÍ | Brasil | 2210003 | 22 | 33 | nan | nan | nan | Caatinga | 0.6 |
| 2d6ccc7c-3ae9-3827-a5dc-84b18572688b | -5.14076 | -45.03517 | 2025-08-31 04:49:00 | NOAA-20 | SÃO RAIMUNDO DO DOCA BEZERRA | MARANHÃO | Brasil | 2111631 | 21 | 33 | nan | nan | nan | Cerrado | 2.3 |
| 9b43ca4b-77b4-36e7-a2db-cb06ef5267f3 | -6.96834 | -40.95041 | 2025-08-31 04:49:00 | NOAA-20 | ALAGOINHA DO PIAUÍ | PIAUÍ | Brasil | 2200251 | 22 | 33 | nan | nan | nan | Caatinga | 4.9 |
| 32918c04-695a-38df-be4f-6eb7d92dcde5 | -7.63459 | -42.65879 | 2025-08-31 04:49:00 | NOAA-20 | RIBEIRA DO PIAUÍ | PIAUÍ | Brasil | 2208874 | 22 | 33 | nan | nan | nan | Caatinga | 1.5 |
| 9cce4dd6-2b8d-3fd1-83a6-9a8a0fbe5867 | -6.18207 | -43.34304 | 2025-08-31 04:49:00 | NOAA-20 | LAGOA DO MATO | MARANHÃO | Brasil | 2105922 | 21 | 33 | nan | nan | nan | Cerrado | 1.1 |
| d4a8ffa3-4939-3ac8-b195-fc36cda521b9 | -6.18854 | -44.1316 | 2025-08-31 04:49:00 | NOAA-20 | COLINAS | MARANHÃO | Brasil | 2103505 | 21 | 33 | nan | nan | nan | Cerrado | 2.1 |
| 9099c713-c69b-36d0-9a2e-8cb8702bd643 | -7.40495 | -47.44157 | 2025-08-31 04:49:00 | NOAA-20 | CAROLINA | MARANHÃO | Brasil | 2102804 | 21 | 33 | nan | nan | nan | Cerrado | 2.1 |
| 0a3eaca7-ac9e-33f6-af0e-d6e5082e61a4 | -5.70021 | -45.95968 | 2025-08-31 04:49:00 | NOAA-20 | GRAJAÚ | MARANHÃO | Brasil | 2104800 | 21 | 33 | nan | nan | nan | Cerrado | 2.1 |
| d1f97b98-11f6-3d2d-bc05-4304c0c24860 | -6.17667 | -44.14186 | 2025-08-31 04:49:00 | NOAA-20 | COLINAS | MARANHÃO | Brasil | 2103505 | 21 | 33 | nan | nan | nan | Cerrado | 2.2 |
| c960add5-ff8d-34a0-8350-c3775d512e09 | -7.21436 | -45.42673 | 2025-08-31 04:49:00 | NOAA-20 | SAMBAÍBA | MARANHÃO | Brasil | 2109700 | 21 | 33 | nan | nan | nan | Cerrado | 2.4 |
| 3b8ba7fb-8532-394c-90bf-a8e1540756bc | -5.65262 | -43.64339 | 2025-08-31 04:49:00 | NOAA-20 | BURITI BRAVO | MARANHÃO | Brasil | 2102309 | 21 | 33 | nan | nan | nan | Cerrado | 1.1 |
| 7af35f64-3ef7-3b81-9bca-5234401869a0 | -6.13068 | -42.94801 | 2025-08-31 04:49:00 | NOAA-20 | PALMEIRAIS | PIAUÍ | Brasil | 2207504 | 22 | 33 | nan | nan | nan | Caatinga | 4.7 |
| 64d1ffc3-9c6c-3c9e-8074-666c3b62cc35 | -6.58324 | -43.68869 | 2025-08-31 04:49:00 | NOAA-20 | SÃO JOÃO DOS PATOS | MARANHÃO | Brasil | 2111102 | 21 | 33 | nan | nan | nan | Cerrado | 11.4 |
| fc72b392-5ccd-324d-b9dd-3123777ef99c | -6.42624 | -43.96725 | 2025-08-31 04:49:00 | NOAA-20 | PARAIBANO | MARANHÃO | Brasil | 2107704 | 21 | 33 | nan | nan | nan | Cerrado | 1.7 |
| 2eb353b1-bbef-3b8f-90b0-5c867e2839d0 | -6.16241 | -43.3263 | 2025-08-31 04:49:00 | NOAA-20 | LAGOA DO MATO | MARANHÃO | Brasil | 2105922 | 21 | 33 | nan | nan | nan | Cerrado | 20.1 |
| de08f106-2beb-3ac3-9370-ec67868e2d01 | -5.48227 | -51.22446 | 2025-08-31 04:49:00 | NOAA-20 | SÃO FÉLIX DO XINGU | PARÁ | Brasil | 1507300 | 15 | 33 | nan | nan | nan | Amazônia | 1.0 |
| 359521c7-20e6-3b82-b187-157cefa10407 | -2.90312 | -48.29703 | 2025-08-31 04:49:00 | NOAA-20 | TOMÉ-AÇU | PARÁ | Brasil | 1508001 | 15 | 33 | nan | nan | nan | Amazônia | 1.3 |
| fc73d2c1-54ae-3194-9a7a-5f52dabbf6fd | -3.84841 | -49.28462 | 2025-08-31 04:49:00 | NOAA-20 | BREU BRANCO | PARÁ | Brasil | 1501782 | 15 | 33 | nan | nan | nan | Amazônia | 1.6 |
| c2467de6-a711-345d-a718-db3b287ed183 | -6.42664 | -43.96442 | 2025-08-31 04:49:00 | NOAA-20 | PARAIBANO | MARANHÃO | Brasil | 2107704 | 21 | 33 | nan | nan | nan | Cerrado | 1.4 |
| 02ead4a4-f881-302c-a6ec-7c5370eeab89 | -6.18597 | -43.31529 | 2025-08-31 04:49:00 | NOAA-20 | LAGOA DO MATO | MARANHÃO | Brasil | 2105922 | 21 | 33 | nan | nan | nan | Cerrado | 9.0 |
| c1959ccc-a6c5-39f3-b4ed-7f74700b6901 | -7.08449 | -44.3228 | 2025-08-31 04:49:00 | NOAA-20 | BENEDITO LEITE | MARANHÃO | Brasil | 2101806 | 21 | 33 | nan | nan | nan | Cerrado | 1.0 |
| 8e6bcfb7-6ae6-338c-8fa5-032f3679430a | -6.9646 | -44.31748 | 2025-08-31 04:49:00 | NOAA-20 | BENEDITO LEITE | MARANHÃO | Brasil | 2101806 | 21 | 33 | nan | nan | nan | Cerrado | 0.9 |
| 74558b21-f7c4-3df5-a8bc-66d5d7c12928 | -6.94918 | -44.0565 | 2025-08-31 04:49:00 | NOAA-20 | PORTO ALEGRE DO PIAUÍ | PIAUÍ | Brasil | 2208551 | 22 | 33 | nan | nan | nan | Cerrado | 1.4 |
| c1baf3cf-46f5-3326-887f-1aa0ebd8d771 | -7.10067 | -44.31886 | 2025-08-31 04:49:00 | NOAA-20 | BENEDITO LEITE | MARANHÃO | Brasil | 2101806 | 21 | 33 | nan | nan | nan | Cerrado | 12.3 |
| 1701c0fa-2d52-3ac2-9072-c2d09509204f | -6.61305 | -53.12764 | 2025-08-31 04:49:00 | NOAA-20 | SÃO FÉLIX DO XINGU | PARÁ | Brasil | 1507300 | 15 | 33 | nan | nan | nan | Amazônia | 1.6 |
| ffb64aa5-fe13-3117-9d36-a13390b28251 | -6.28428 | -43.53304 | 2025-08-31 04:49:00 | NOAA-20 | SUCUPIRA DO RIACHÃO | MARANHÃO | Brasil | 2111953 | 21 | 33 | nan | nan | nan | Cerrado | 1.3 |
| c021f71d-a249-3fff-9335-fc151baabfea | -2.29355 | -47.98509 | 2025-08-31 04:49:00 | NOAA-20 | AURORA DO PARÁ | PARÁ | Brasil | 1500958 | 15 | 33 | nan | nan | nan | Amazônia | 1.3 |
| 45c2cc00-f5d7-3bc6-866e-74edb7bd9a1c | -5.99268 | -43.36306 | 2025-08-31 04:49:00 | NOAA-20 | LAGOA DO MATO | MARANHÃO | Brasil | 2105922 | 21 | 33 | nan | nan | nan | Caatinga | 1.5 |
| 0750632c-b941-387b-a034-5d9335134c32 | -4.55518 | -50.47743 | 2025-08-31 04:49:00 | NOAA-20 | NOVO REPARTIMENTO | PARÁ | Brasil | 1505064 | 15 | 33 | nan | nan | nan | Amazônia | 2.1 |
| 779c6216-0829-3c00-8d2a-13185d3b2fd4 | -4.26994 | -48.64071 | 2025-08-31 04:49:00 | NOAA-20 | RONDON DO PARÁ | PARÁ | Brasil | 1506187 | 15 | 33 | nan | nan | nan | Amazônia | 3.1 |
| 3b75c09b-878d-3408-92cd-51c27dfde528 | -6.16989 | -44.00402 | 2025-08-31 04:49:00 | NOAA-20 | COLINAS | MARANHÃO | Brasil | 2103505 | 21 | 33 | nan | nan | nan | Cerrado | 1.8 |
| 5ef20834-8a4d-3e57-bc02-f94e966bf9e8 | -6.50577 | -43.55748 | 2025-08-31 04:49:00 | NOAA-20 | SUCUPIRA DO RIACHÃO | MARANHÃO | Brasil | 2111953 | 21 | 33 | nan | nan | nan | Cerrado | 1.0 |
| 630f36be-e2d5-3be8-a55f-bfe3ab7e6217 | -7.75731 | -45.45878 | 2025-08-31 04:49:00 | NOAA-20 | RIBEIRO GONÇALVES | PIAUÍ | Brasil | 2208908 | 22 | 33 | nan | nan | nan | Cerrado | 1.9 |
| 4d8bf12a-986a-3c9b-8306-e137a188bee2 | -3.51405 | -47.20195 | 2025-08-31 04:49:00 | NOAA-20 | ULIANÓPOLIS | PARÁ | Brasil | 1508126 | 15 | 33 | nan | nan | nan | Amazônia | 1.9 |
| 7257982e-f9c3-3542-b2ad-bf5692a1846a | -6.50001 | -43.55976 | 2025-08-31 04:49:00 | NOAA-20 | SUCUPIRA DO RIACHÃO | MARANHÃO | Brasil | 2111953 | 21 | 33 | nan | nan | nan | Cerrado | 1.0 |
| 7b313e83-3e55-365d-958c-25a616f1bcac | -7.58323 | -42.72562 | 2025-08-31 04:49:00 | NOAA-20 | FLORES DO PIAUÍ | PIAUÍ | Brasil | 2203800 | 22 | 33 | nan | nan | nan | Caatinga | 2.1 |
| 55255c7e-c977-3421-8b1a-c924d85eb756 | -6.96263 | -40.94472 | 2025-08-31 04:49:00 | NOAA-20 | ALAGOINHA DO PIAUÍ | PIAUÍ | Brasil | 2200251 | 22 | 33 | nan | nan | nan | Caatinga | 0.8 |
| 52f950bb-d784-3248-b8a9-ea2f121f6659 | -6.71063 | -51.41991 | 2025-08-31 04:49:00 | NOAA-20 | TUCUMÃ | PARÁ | Brasil | 1508084 | 15 | 33 | nan | nan | nan | Amazônia | 10.9 |
| ab89fc73-2e2e-356d-a3fc-e647c42f6a17 | -6.48021 | -44.41433 | 2025-08-31 04:49:00 | NOAA-20 | MIRADOR | MARANHÃO | Brasil | 2106706 | 21 | 33 | nan | nan | nan | Cerrado | 0.6 |
| 49dccec8-0d3f-3569-8abc-be60cff11359 | -2.9038 | -48.29267 | 2025-08-31 04:49:00 | NOAA-20 | TOMÉ-AÇU | PARÁ | Brasil | 1508001 | 15 | 33 | nan | nan | nan | Amazônia | 1.8 |
| 2731f5e5-5f6f-309e-a7b3-8d8b0dc31e35 | -7.7676 | -45.45464 | 2025-08-31 04:49:00 | NOAA-20 | RIBEIRO GONÇALVES | PIAUÍ | Brasil | 2208908 | 22 | 33 | nan | nan | nan | Cerrado | 2.5 |
| 45ad2ddf-b3dd-3896-be97-0061b5667f8f | -4.27363 | -48.64127 | 2025-08-31 04:49:00 | NOAA-20 | RONDON DO PARÁ | PARÁ | Brasil | 1506187 | 15 | 33 | nan | nan | nan | Amazônia | 3.1 |
| 90d95c8e-6417-3def-8515-a06158dc1d2b | -6.44852 | -42.40789 | 2025-08-31 04:49:00 | NOAA-20 | REGENERAÇÃO | PIAUÍ | Brasil | 2208809 | 22 | 33 | nan | nan | nan | Caatinga | 1.5 |
| 200c6337-c899-3e97-96d6-8bbaeffa7228 | -3.2155 | -46.83069 | 2025-08-31 04:49:00 | NOAA-20 | PARAGOMINAS | PARÁ | Brasil | 1505502 | 15 | 33 | nan | nan | nan | Amazônia | 0.9 |
| 4afb374b-c897-3882-9c5d-3a0c77ceec6f | -6.42584 | -43.97008 | 2025-08-31 04:49:00 | NOAA-20 | PARAIBANO | MARANHÃO | Brasil | 2107704 | 21 | 33 | nan | nan | nan | Cerrado | 1.7 |
| ff135ec2-ee37-3903-8630-e5f00ba148a3 | -3.51725 | -47.20778 | 2025-08-31 04:49:00 | NOAA-20 | ULIANÓPOLIS | PARÁ | Brasil | 1508126 | 15 | 33 | nan | nan | nan | Amazônia | 0.8 |
| 2012b415-f5b7-3b9a-8843-b7e291997e1e | -6.24993 | -43.38822 | 2025-08-31 04:49:00 | NOAA-20 | LAGOA DO MATO | MARANHÃO | Brasil | 2105922 | 21 | 33 | nan | nan | nan | Cerrado | 2.0 |
| df6c36bb-27b8-3d36-8347-f01ffa988cda | -6.47562 | -44.41055 | 2025-08-31 04:49:00 | NOAA-20 | MIRADOR | MARANHÃO | Brasil | 2106706 | 21 | 33 | nan | nan | nan | Cerrado | 0.6 |
| dac4bf78-9d2d-35f3-872e-e5447365efb7 | -5.55865 | -44.21476 | 2025-08-31 04:49:00 | NOAA-20 | SÃO DOMINGOS DO MARANHÃO | MARANHÃO | Brasil | 2110708 | 21 | 33 | nan | nan | nan | Cerrado | 1.4 |
| cf288284-fc9e-38d7-856a-c3927e099076 | -7.32902 | -44.1 | 2025-08-31 04:49:00 | NOAA-20 | LANDRI SALES | PIAUÍ | Brasil | 2205607 | 22 | 33 | nan | nan | nan | Cerrado | 1.9 |
| 526bde7a-52ad-3774-9ef4-7314a25e3d65 | -6.17619 | -43.34579 | 2025-08-31 04:49:00 | NOAA-20 | LAGOA DO MATO | MARANHÃO | Brasil | 2105922 | 21 | 33 | nan | nan | nan | Cerrado | 1.1 |
| 85ef0b5e-2e63-3f90-8990-144f883b9eb8 | -7.57574 | -45.12062 | 2025-08-31 04:49:00 | NOAA-20 | RIBEIRO GONÇALVES | PIAUÍ | Brasil | 2208908 | 22 | 33 | nan | nan | nan | Cerrado | 1.8 |
| c99bac61-4624-3f3e-84e9-2fbeed811124 | -3.99965 | -47.09292 | 2025-08-31 04:49:00 | NOAA-20 | ITINGA DO MARANHÃO | MARANHÃO | Brasil | 2105427 | 21 | 33 | nan | nan | nan | Amazônia | 0.7 |
| 27b00071-c8a3-322d-b3ec-61b23d428f46 | -6.16984 | -43.35188 | 2025-08-31 04:49:00 | NOAA-20 | LAGOA DO MATO | MARANHÃO | Brasil | 2105922 | 21 | 33 | nan | nan | nan | Cerrado | 2.0 |
| 06ffa1e4-5fd1-35f4-8399-a6d27ae9f00c | -4.27128 | -48.63902 | 2025-08-31 04:49:00 | NOAA-20 | RONDON DO PARÁ | PARÁ | Brasil | 1506187 | 15 | 33 | nan | nan | nan | Amazônia | 3.1 |
| d87140b9-0e61-3e14-b6a2-97961e8e003a | -6.57162 | -43.6945 | 2025-08-31 04:49:00 | NOAA-20 | SÃO JOÃO DOS PATOS | MARANHÃO | Brasil | 2111102 | 21 | 33 | nan | nan | nan | Cerrado | 2.1 |
| d076e44c-4faf-3390-a5d8-7bc6b1e4f716 | -7.20272 | -45.44038 | 2025-08-31 04:49:00 | NOAA-20 | SAMBAÍBA | MARANHÃO | Brasil | 2109700 | 21 | 33 | nan | nan | nan | Cerrado | 2.4 |
| c3cccb6e-eb77-3c37-be85-46347b4a1d86 | -6.28285 | -43.54311 | 2025-08-31 04:49:00 | NOAA-20 | SUCUPIRA DO RIACHÃO | MARANHÃO | Brasil | 2111953 | 21 | 33 | nan | nan | nan | Cerrado | 1.1 |
| 7f25b260-2474-3f5f-b232-061fc2798032 | -7.20744 | -45.44122 | 2025-08-31 04:49:00 | NOAA-20 | SAMBAÍBA | MARANHÃO | Brasil | 2109700 | 21 | 33 | nan | nan | nan | Cerrado | 3.5 |
| f69dbbfc-83ea-307a-8467-22e9758b4601 | -8.19493 | -42.32037 | 2025-08-31 04:49:00 | NOAA-20 | SÃO JOÃO DO PIAUÍ | PIAUÍ | Brasil | 2210003 | 22 | 33 | nan | nan | nan | Caatinga | 1.2 |
| f7dc43f3-e21f-3bff-b9f4-dccb8019eda2 | -6.17717 | -43.33879 | 2025-08-31 04:49:00 | NOAA-20 | LAGOA DO MATO | MARANHÃO | Brasil | 2105922 | 21 | 33 | nan | nan | nan | Cerrado | 0.9 |
| 85da0625-a3a6-3aa5-a7a5-71448c9837c1 | -6.27703 | -43.54582 | 2025-08-31 04:49:00 | NOAA-20 | SUCUPIRA DO RIACHÃO | MARANHÃO | Brasil | 2111953 | 21 | 33 | nan | nan | nan | Cerrado | 0.9 |
| 168dbff7-802d-3a61-9ea3-ef9ae9d52f75 | -6.13017 | -42.95169 | 2025-08-31 04:49:00 | NOAA-20 | PALMEIRAIS | PIAUÍ | Brasil | 2207504 | 22 | 33 | nan | nan | nan | Caatinga | 4.7 |
| 710a6eb3-0d43-3478-9d0f-618b2c624fd4 | -7.76693 | -45.45831 | 2025-08-31 04:49:00 | NOAA-20 | RIBEIRO GONÇALVES | PIAUÍ | Brasil | 2208908 | 22 | 33 | nan | nan | nan | Cerrado | 2.0 |
| 09ca6c61-dadd-301b-9b61-d7178805d4b9 | -5.5889 | -46.32543 | 2025-08-31 04:49:00 | NOAA-20 | GRAJAÚ | MARANHÃO | Brasil | 2104800 | 21 | 33 | nan | nan | nan | Cerrado | 2.0 |
| 63d4bc15-2f91-39ee-a07f-2ce2d05b0d64 | -6.43663 | -43.96859 | 2025-08-31 04:49:00 | NOAA-20 | PARAIBANO | MARANHÃO | Brasil | 2107704 | 21 | 33 | nan | nan | nan | Cerrado | 1.2 |
| e1872d65-9173-389b-a8c6-dbec81cb5b8f | -6.27147 | -43.85158 | 2025-08-31 04:49:00 | NOAA-20 | PASSAGEM FRANCA | MARANHÃO | Brasil | 2107902 | 21 | 33 | nan | nan | nan | Cerrado | 1.6 |
| d585538a-c2fe-36c1-b080-6e502e27fb61 | -6.44922 | -43.95448 | 2025-08-31 04:49:00 | NOAA-20 | PARAIBANO | MARANHÃO | Brasil | 2107704 | 21 | 33 | nan | nan | nan | Cerrado | 1.7 |
| 37e14283-e1fa-38e7-baa8-5c86fe8152e0 | -6.63897 | -44.2576 | 2025-08-31 04:49:00 | NOAA-20 | PASTOS BONS | MARANHÃO | Brasil | 2108009 | 21 | 33 | nan | nan | nan | Cerrado | 1.2 |
| 6a1be621-0871-36b8-957b-6086792c8367 | -6.33039 | -42.5298 | 2025-08-31 04:49:00 | NOAA-20 | REGENERAÇÃO | PIAUÍ | Brasil | 2208809 | 22 | 33 | nan | nan | nan | Caatinga | 2.0 |
| 414606ce-288c-318d-9f1f-c270da5ab063 | -7.07935 | -44.32236 | 2025-08-31 04:49:00 | NOAA-20 | BENEDITO LEITE | MARANHÃO | Brasil | 2101806 | 21 | 33 | nan | nan | nan | Cerrado | 1.0 |
| cdd2277f-7d8c-3fea-821c-b5e27ac28504 | -6.43621 | -43.9715 | 2025-08-31 04:49:00 | NOAA-20 | PARAIBANO | MARANHÃO | Brasil | 2107704 | 21 | 33 | nan | nan | nan | Cerrado | 1.2 |
| 49711dfd-f6ee-37d5-be7a-dabc22094ad7 | -3.84754 | -49.28787 | 2025-08-31 04:49:00 | NOAA-20 | BREU BRANCO | PARÁ | Brasil | 1501782 | 15 | 33 | nan | nan | nan | Amazônia | 2.9 |
| ee27c1da-a44c-3c7b-a019-c522b44ae32f | -6.44873 | -43.9579 | 2025-08-31 04:49:00 | NOAA-20 | PARAIBANO | MARANHÃO | Brasil | 2107704 | 21 | 33 | nan | nan | nan | Cerrado | 2.5 |
| 88162cea-4c44-343b-b916-58ab78e306d9 | -6.1731 | -44.13022 | 2025-08-31 04:49:00 | NOAA-20 | COLINAS | MARANHÃO | Brasil | 2103505 | 21 | 33 | nan | nan | nan | Cerrado | 1.0 |
| 158bd569-b67b-370d-ab84-06b503ada4c4 | -6.93059 | -45.57133 | 2025-08-31 04:49:00 | NOAA-20 | SÃO RAIMUNDO DAS MANGABEIRAS | MARANHÃO | Brasil | 2111607 | 21 | 33 | nan | nan | nan | Cerrado | 4.3 |
| 68d8758c-b602-3789-9d94-d140dacb4da4 | -7.10622 | -44.31645 | 2025-08-31 04:49:00 | NOAA-20 | BENEDITO LEITE | MARANHÃO | Brasil | 2101806 | 21 | 33 | nan | nan | nan | Cerrado | 12.3 |
| 817d2687-273d-3f74-8a95-039a2d415fed | -6.53797 | -44.43887 | 2025-08-31 04:49:00 | NOAA-20 | SUCUPIRA DO NORTE | MARANHÃO | Brasil | 2111904 | 21 | 33 | nan | nan | nan | Cerrado | 0.9 |
| dfd9fbc5-371d-3f07-9dfc-a2e00e762ce9 | -6.95087 | -42.01355 | 2025-08-31 04:49:00 | NOAA-20 | OEIRAS | PIAUÍ | Brasil | 2207009 | 22 | 33 | nan | nan | nan | Caatinga | 1.5 |
| f164de4b-5170-3af6-8da8-498eb7e2e7c4 | -7.10662 | -44.31351 | 2025-08-31 04:49:00 | NOAA-20 | BENEDITO LEITE | MARANHÃO | Brasil | 2101806 | 21 | 33 | nan | nan | nan | Cerrado | 6.4 |
| 2d8ddae7-88a7-3c1f-bcf8-a5793f72d382 | -8.19269 | -42.31833 | 2025-08-31 04:49:00 | NOAA-20 | SÃO JOÃO DO PIAUÍ | PIAUÍ | Brasil | 2210003 | 22 | 33 | nan | nan | nan | Caatinga | 2.3 |
| b9339a50-73ca-325d-bf1a-1be656b21f1b | -5.65783 | -43.64429 | 2025-08-31 04:49:00 | NOAA-20 | BURITI BRAVO | MARANHÃO | Brasil | 2102309 | 21 | 33 | nan | nan | nan | Cerrado | 1.1 |
| 649bed1e-bd13-3bdb-a39c-b35bb6bce985 | -6.64404 | -44.25852 | 2025-08-31 04:49:00 | NOAA-20 | PASTOS BONS | MARANHÃO | Brasil | 2108009 | 21 | 33 | nan | nan | nan | Cerrado | 1.2 |
| d899c8e5-f5a1-3617-b702-f40822ea2211 | -4.30481 | -48.09803 | 2025-08-31 04:49:00 | NOAA-20 | RONDON DO PARÁ | PARÁ | Brasil | 1506187 | 15 | 33 | nan | nan | nan | Amazônia | 1.4 |
| a7e20eec-aafd-3d65-8465-ec83730a41c7 | -7.77237 | -45.45539 | 2025-08-31 04:49:00 | NOAA-20 | RIBEIRO GONÇALVES | PIAUÍ | Brasil | 2208908 | 22 | 33 | nan | nan | nan | Cerrado | 1.5 |
| d8fc0aa7-b8a2-3a20-8d25-96ddf5c59c29 | -6.64121 | -44.25721 | 2025-08-31 04:49:00 | NOAA-20 | PASTOS BONS | MARANHÃO | Brasil | 2108009 | 21 | 33 | nan | nan | nan | Cerrado | 1.5 |
| 2db1e2e9-e7bd-36d3-a245-8de75f8183c9 | -7.77169 | -45.45904 | 2025-08-31 04:49:00 | NOAA-20 | RIBEIRO GONÇALVES | PIAUÍ | Brasil | 2208908 | 22 | 33 | nan | nan | nan | Cerrado | 1.4 |


[Clique aqui para ver as próximas entradas](README55.md)
