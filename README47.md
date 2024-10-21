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

## Dados Diários - Página 47

| ID | Latitude | Longitude | Data/Hora GMT | Satélite | Município | Estado | País | Município ID | Estado ID | País ID | Dias sem Chuva | Precipitação | Risco de Fogo | Bioma | FRP |
|----|----------|-----------|---------------|----------|-----------|--------|------|--------------|-----------|---------|----------------|--------------|----------------|-------|-----|
| 369ee911-358c-3d8d-91f1-01ef1cec05c4 | -3.5472 | -55.44218 | 2024-10-21 04:36:00 | NOAA-20 | AVEIRO | PARÁ | Brasil | 1501006 | 15 | 33 | nan | nan | nan | Amazônia | 1.1 |
| f4d1e3cf-b304-31b6-a052-85f87d793784 | -3.47751 | -55.38928 | 2024-10-21 04:36:00 | NOAA-20 | AVEIRO | PARÁ | Brasil | 1501006 | 15 | 33 | nan | nan | nan | Amazônia | 1.9 |
| b495bf87-075c-33d6-b051-cbad5c0f6658 | -3.47302 | -55.38862 | 2024-10-21 04:36:00 | NOAA-20 | AVEIRO | PARÁ | Brasil | 1501006 | 15 | 33 | nan | nan | nan | Amazônia | 1.4 |
| 9d74ed8c-bf33-318c-b142-54533ed3c9a5 | -12.5147 | -63.3014 | 2024-10-21 04:36:18 | GOES-16 | SÃO FRANCISCO DO GUAPORÉ | RONDÔNIA | Brasil | 1101492 | 11 | 33 | nan | nan | nan | Amazônia | 33.7 |
| 34809da3-8f25-3b15-9d74-32e4d90c575a | -18.2828 | -56.0994 | 2024-10-21 04:36:49 | GOES-16 | CORUMBÁ | MATO GROSSO DO SUL | Brasil | 5003207 | 50 | 33 | nan | nan | nan | Pantanal | 101.6 |
| af90b6af-50a8-3385-a98d-ae4898ab77de | -10.90345 | -40.53733 | 2024-10-21 04:38:00 | NOAA-20 | MIRANGABA | BAHIA | Brasil | 2921401 | 29 | 33 | nan | nan | nan | Caatinga | 1.0 |
| d9708568-8c64-37d9-9304-0da1f1b93a70 | -10.89788 | -40.53636 | 2024-10-21 04:38:00 | NOAA-20 | MIRANGABA | BAHIA | Brasil | 2921401 | 29 | 33 | nan | nan | nan | Caatinga | 1.0 |
| 143a81f0-dc4a-3df0-a20f-2341159c6ab0 | -9.90488 | -42.10461 | 2024-10-21 04:38:00 | NOAA-20 | SENTO SÉ | BAHIA | Brasil | 2930204 | 29 | 33 | nan | nan | nan | Caatinga | 3.7 |
| 283473ef-f34c-38a0-9220-c743a3de233a | -9.90408 | -42.10269 | 2024-10-21 04:38:00 | NOAA-20 | SENTO SÉ | BAHIA | Brasil | 2930204 | 29 | 33 | nan | nan | nan | Caatinga | 4.1 |
| 7d1f1091-bcdf-328f-86ef-2dcc0cce5285 | -6.00848 | -44.52429 | 2024-10-21 04:38:00 | NOAA-20 | MIRADOR | MARANHÃO | Brasil | 2106706 | 21 | 33 | nan | nan | nan | Cerrado | 3.7 |
| 467af28a-0758-314a-ad86-65c012be97ae | -7.18466 | -44.96397 | 2024-10-21 04:38:00 | NOAA-20 | SÃO FÉLIX DE BALSAS | MARANHÃO | Brasil | 2110807 | 21 | 33 | nan | nan | nan | Cerrado | 0.8 |
| b46e5dcc-38dd-3392-bd75-bf9f294f324a | -7.18073 | -44.96334 | 2024-10-21 04:38:00 | NOAA-20 | SÃO FÉLIX DE BALSAS | MARANHÃO | Brasil | 2110807 | 21 | 33 | nan | nan | nan | Cerrado | 0.7 |
| b62e5778-44da-3ac3-9376-55e4ca2749b1 | -7.18 | -44.96838 | 2024-10-21 04:38:00 | NOAA-20 | SÃO FÉLIX DE BALSAS | MARANHÃO | Brasil | 2110807 | 21 | 33 | nan | nan | nan | Cerrado | 0.7 |
| cdf294b0-3c78-3caa-8c5a-d7ffe3299459 | -5.84137 | -46.23587 | 2024-10-21 04:38:00 | NOAA-20 | GRAJAÚ | MARANHÃO | Brasil | 2104800 | 21 | 33 | nan | nan | nan | Cerrado | 3.3 |
| 58b260b0-6a97-36c3-bcbf-df07952cf01f | -5.69272 | -46.42781 | 2024-10-21 04:38:00 | NOAA-20 | AMARANTE DO MARANHÃO | MARANHÃO | Brasil | 2100600 | 21 | 33 | nan | nan | nan | Cerrado | 8.3 |
| c6b1e79d-3163-32c5-a48c-6d484de81e71 | -5.6921 | -46.43182 | 2024-10-21 04:38:00 | NOAA-20 | AMARANTE DO MARANHÃO | MARANHÃO | Brasil | 2100600 | 21 | 33 | nan | nan | nan | Cerrado | 8.3 |
| 3d1156e0-f3c5-3e55-a549-57ffb386dd59 | -5.69149 | -46.43582 | 2024-10-21 04:38:00 | NOAA-20 | AMARANTE DO MARANHÃO | MARANHÃO | Brasil | 2100600 | 21 | 33 | nan | nan | nan | Cerrado | 1.6 |
| 2c184ac8-ff47-30ad-84d0-58c0a96f9df6 | -5.68916 | -46.42727 | 2024-10-21 04:38:00 | NOAA-20 | AMARANTE DO MARANHÃO | MARANHÃO | Brasil | 2100600 | 21 | 33 | nan | nan | nan | Cerrado | 8.3 |
| a4b3d77f-5518-369e-8dbc-73ae985f61f7 | -5.68855 | -46.43131 | 2024-10-21 04:38:00 | NOAA-20 | AMARANTE DO MARANHÃO | MARANHÃO | Brasil | 2100600 | 21 | 33 | nan | nan | nan | Cerrado | 8.3 |
| a7522f21-57f1-3fd2-9391-7680c1a9392b | -5.68794 | -46.43532 | 2024-10-21 04:38:00 | NOAA-20 | AMARANTE DO MARANHÃO | MARANHÃO | Brasil | 2100600 | 21 | 33 | nan | nan | nan | Cerrado | 1.6 |
| 17e28b50-4a11-3678-bb00-f0dfc15797bf | -5.68623 | -46.42264 | 2024-10-21 04:38:00 | NOAA-20 | AMARANTE DO MARANHÃO | MARANHÃO | Brasil | 2100600 | 21 | 33 | nan | nan | nan | Cerrado | 1.3 |
| 43299932-3023-371e-be03-95e16e4ee3ec | -5.68561 | -46.42673 | 2024-10-21 04:38:00 | NOAA-20 | AMARANTE DO MARANHÃO | MARANHÃO | Brasil | 2100600 | 21 | 33 | nan | nan | nan | Cerrado | 3.0 |
| fb6430aa-e981-31d6-8141-01684163bf8a | -5.68499 | -46.43079 | 2024-10-21 04:38:00 | NOAA-20 | AMARANTE DO MARANHÃO | MARANHÃO | Brasil | 2100600 | 21 | 33 | nan | nan | nan | Cerrado | 3.0 |
| 264726bf-1dbe-3d78-ad59-e97b10d87a99 | -5.68438 | -46.43478 | 2024-10-21 04:38:00 | NOAA-20 | AMARANTE DO MARANHÃO | MARANHÃO | Brasil | 2100600 | 21 | 33 | nan | nan | nan | Cerrado | 0.6 |
| c843bc65-3761-3a98-8d76-fe52ce417ed1 | -5.68378 | -46.43877 | 2024-10-21 04:38:00 | NOAA-20 | AMARANTE DO MARANHÃO | MARANHÃO | Brasil | 2100600 | 21 | 33 | nan | nan | nan | Cerrado | 0.6 |
| 7ec05eaf-5806-3a3d-8629-24bcba8af1db | -5.68023 | -46.43821 | 2024-10-21 04:38:00 | NOAA-20 | AMARANTE DO MARANHÃO | MARANHÃO | Brasil | 2100600 | 21 | 33 | nan | nan | nan | Cerrado | 0.6 |
| 596a5c81-cff8-36b9-8f99-4329bb0e0440 | -5.67352 | -46.48228 | 2024-10-21 04:38:00 | NOAA-20 | AMARANTE DO MARANHÃO | MARANHÃO | Brasil | 2100600 | 21 | 33 | nan | nan | nan | Cerrado | 1.3 |
| cc6256d7-a9d0-3d6d-9313-9fe9c8f4098e | -5.43613 | -46.35371 | 2024-10-21 04:38:00 | NOAA-20 | AMARANTE DO MARANHÃO | MARANHÃO | Brasil | 2100600 | 21 | 33 | nan | nan | nan | Cerrado | 5.3 |
| 67076463-4f69-340c-8fb8-3bd52c408d83 | -5.43551 | -46.35778 | 2024-10-21 04:38:00 | NOAA-20 | AMARANTE DO MARANHÃO | MARANHÃO | Brasil | 2100600 | 21 | 33 | nan | nan | nan | Cerrado | 2.2 |
| 2413f1ae-f258-397d-8c5c-f4d717ea3b50 | -5.43196 | -46.3572 | 2024-10-21 04:38:00 | NOAA-20 | AMARANTE DO MARANHÃO | MARANHÃO | Brasil | 2100600 | 21 | 33 | nan | nan | nan | Cerrado | 2.2 |
| 8860ca01-d993-3388-87de-eba360593e7d | -6.78123 | -46.42639 | 2024-10-21 04:38:00 | NOAA-20 | FORMOSA DA SERRA NEGRA | MARANHÃO | Brasil | 2104099 | 21 | 33 | nan | nan | nan | Cerrado | 0.9 |
| f1397426-0c76-3b87-a531-c37b6162a1c5 | -6.141 | -46.90354 | 2024-10-21 04:38:00 | NOAA-20 | LAJEADO NOVO | MARANHÃO | Brasil | 2105989 | 21 | 33 | nan | nan | nan | Cerrado | 0.8 |
| 8511a0bb-c5a2-31e0-9cb3-85fbd0a176e8 | -5.71448 | -47.17692 | 2024-10-21 04:38:00 | NOAA-20 | GOVERNADOR EDISON LOBÃO | MARANHÃO | Brasil | 2104552 | 21 | 33 | nan | nan | nan | Cerrado | 0.6 |
| 28749102-51e6-3dba-b951-408580cc35cf | -5.66347 | -47.00266 | 2024-10-21 04:38:00 | NOAA-20 | MONTES ALTOS | MARANHÃO | Brasil | 2107001 | 21 | 33 | nan | nan | nan | Cerrado | 0.7 |
| 9cc3e7cc-aef7-3f90-ae33-fc22d7c4c995 | -5.66001 | -47.00214 | 2024-10-21 04:38:00 | NOAA-20 | MONTES ALTOS | MARANHÃO | Brasil | 2107001 | 21 | 33 | nan | nan | nan | Cerrado | 0.7 |
| 95030fff-780b-3dc5-9810-39be6fbe1e51 | -7.49083 | -46.94383 | 2024-10-21 04:38:00 | NOAA-20 | RIACHÃO | MARANHÃO | Brasil | 2109502 | 21 | 33 | nan | nan | nan | Cerrado | 1.3 |
| 65303312-8caa-38eb-a363-0b8fb74016dc | -7.04026 | -46.98113 | 2024-10-21 04:38:00 | NOAA-20 | CAROLINA | MARANHÃO | Brasil | 2102804 | 21 | 33 | nan | nan | nan | Cerrado | 2.0 |
| 957a7d57-9bb2-334b-a64c-d19f03d0ddf2 | -6.92115 | -46.83857 | 2024-10-21 04:38:00 | NOAA-20 | SÃO PEDRO DOS CRENTES | MARANHÃO | Brasil | 2111573 | 21 | 33 | nan | nan | nan | Cerrado | 1.2 |
| 810e0f05-8d65-3ab4-9d7b-a18e6cf6dec7 | -11.97774 | -48.69275 | 2024-10-21 04:38:00 | NOAA-20 | PEIXE | TOCANTINS | Brasil | 1716604 | 17 | 33 | nan | nan | nan | Cerrado | 0.9 |
| 4ce3d4c6-dba7-3c23-8a74-920df9aebd9b | -6.40519 | -49.58392 | 2024-10-21 04:38:00 | NOAA-20 | CURIONÓPOLIS | PARÁ | Brasil | 1502772 | 15 | 33 | nan | nan | nan | Amazônia | 1.3 |
| 48f831fc-b208-3be7-8044-6b5223baa3b5 | -6.2919 | -49.31212 | 2024-10-21 04:38:00 | NOAA-20 | ELDORADO DO CARAJÁS | PARÁ | Brasil | 1502954 | 15 | 33 | nan | nan | nan | Amazônia | 1.1 |
| 70825ee6-e08b-343f-9c30-35bc090d7270 | -6.29136 | -49.31557 | 2024-10-21 04:38:00 | NOAA-20 | ELDORADO DO CARAJÁS | PARÁ | Brasil | 1502954 | 15 | 33 | nan | nan | nan | Amazônia | 1.1 |
| de37533b-2f36-37e9-9130-582ada289a6c | -6.28806 | -49.31505 | 2024-10-21 04:38:00 | NOAA-20 | ELDORADO DO CARAJÁS | PARÁ | Brasil | 1502954 | 15 | 33 | nan | nan | nan | Amazônia | 1.1 |
| 7fe014a9-34f6-3bda-b78f-69d597d2c381 | -6.2303 | -49.07572 | 2024-10-21 04:38:00 | NOAA-20 | SÃO GERALDO DO ARAGUAIA | PARÁ | Brasil | 1507458 | 15 | 33 | nan | nan | nan | Amazônia | 0.4 |
| 1d6647be-aa0b-3b02-9e09-031b091c0361 | -6.07231 | -49.62705 | 2024-10-21 04:38:00 | NOAA-20 | CURIONÓPOLIS | PARÁ | Brasil | 1502772 | 15 | 33 | nan | nan | nan | Amazônia | 0.9 |
| b5b49d84-5938-3cfb-b813-7884cad46fe0 | -6.06996 | -49.556 | 2024-10-21 04:38:00 | NOAA-20 | CURIONÓPOLIS | PARÁ | Brasil | 1502772 | 15 | 33 | nan | nan | nan | Amazônia | 1.7 |
| cc803186-5660-33cc-864a-3bb660dc10fa | -6.06942 | -49.55945 | 2024-10-21 04:38:00 | NOAA-20 | CURIONÓPOLIS | PARÁ | Brasil | 1502772 | 15 | 33 | nan | nan | nan | Amazônia | 0.9 |
| d08849b8-e18d-3c51-b9ba-3fb3edafab30 | -6.06901 | -49.62653 | 2024-10-21 04:38:00 | NOAA-20 | CURIONÓPOLIS | PARÁ | Brasil | 1502772 | 15 | 33 | nan | nan | nan | Amazônia | 0.9 |
| 6767c7c0-e94a-3999-92e2-5a80f998767c | -6.06612 | -49.55893 | 2024-10-21 04:38:00 | NOAA-20 | CURIONÓPOLIS | PARÁ | Brasil | 1502772 | 15 | 33 | nan | nan | nan | Amazônia | 0.9 |
| 89556e04-4f3f-3d7d-89ea-1c1b8786c5cd | -5.78866 | -48.16333 | 2024-10-21 04:38:00 | NOAA-20 | ARAGUATINS | TOCANTINS | Brasil | 1702208 | 17 | 33 | nan | nan | nan | Amazônia | 0.4 |
| ded0c52e-e7eb-37e1-9d69-e0c6c31f1f94 | -5.34697 | -48.16407 | 2024-10-21 04:38:00 | NOAA-20 | BURITI DO TOCANTINS | TOCANTINS | Brasil | 1703800 | 17 | 33 | nan | nan | nan | Amazônia | 0.9 |
| f1f6903d-8b6c-3299-b4e4-d4fe37a1b87e | -5.28146 | -49.29742 | 2024-10-21 04:38:00 | NOAA-20 | MARABÁ | PARÁ | Brasil | 1504208 | 15 | 33 | nan | nan | nan | Amazônia | 2.4 |
| 86d19b0b-39b4-35c0-a7a2-7c57b5a38fdc | -5.27816 | -49.29691 | 2024-10-21 04:38:00 | NOAA-20 | MARABÁ | PARÁ | Brasil | 1504208 | 15 | 33 | nan | nan | nan | Amazônia | 2.4 |
| afe48cae-6b00-3ff9-9c1b-102b3e483027 | -7.74186 | -49.85677 | 2024-10-21 04:38:00 | NOAA-20 | PAU D'ARCO | PARÁ | Brasil | 1505551 | 15 | 33 | nan | nan | nan | Amazônia | 0.8 |
| 2343819b-24af-342e-a07f-88d60e7b1b22 | -7.74132 | -49.86023 | 2024-10-21 04:38:00 | NOAA-20 | PAU D'ARCO | PARÁ | Brasil | 1505551 | 15 | 33 | nan | nan | nan | Amazônia | 1.4 |
| 8f27dfbe-55d9-3090-83c7-b05451d2c7bc | -7.74078 | -49.86366 | 2024-10-21 04:38:00 | NOAA-20 | PAU D'ARCO | PARÁ | Brasil | 1505551 | 15 | 33 | nan | nan | nan | Amazônia | 1.4 |
| 51d81478-b012-34d1-83e2-ab997ce74f3d | -7.73856 | -49.85625 | 2024-10-21 04:38:00 | NOAA-20 | PAU D'ARCO | PARÁ | Brasil | 1505551 | 15 | 33 | nan | nan | nan | Amazônia | 0.8 |
| 29c7c393-c294-308a-974b-ddf4ab7f9f21 | -7.10371 | -49.15946 | 2024-10-21 04:38:00 | NOAA-20 | SANTA FÉ DO ARAGUAIA | TOCANTINS | Brasil | 1718865 | 17 | 33 | nan | nan | nan | Amazônia | 1.8 |
| 4bbe6ebf-890f-3dd3-b241-0dde173be140 | -7.08271 | -49.14195 | 2024-10-21 04:38:00 | NOAA-20 | SANTA FÉ DO ARAGUAIA | TOCANTINS | Brasil | 1718865 | 17 | 33 | nan | nan | nan | Amazônia | 1.9 |
| f6c409ff-d273-3d2d-b787-d4b873ab9506 | -6.83183 | -49.13841 | 2024-10-21 04:38:00 | NOAA-20 | XINGUARA | PARÁ | Brasil | 1508407 | 15 | 33 | nan | nan | nan | Amazônia | 4.2 |
| d970cbdf-9abe-342f-84cd-5f43f21e8dfc | -6.82853 | -49.13789 | 2024-10-21 04:38:00 | NOAA-20 | XINGUARA | PARÁ | Brasil | 1508407 | 15 | 33 | nan | nan | nan | Amazônia | 1.3 |
| 49b021a6-c07a-38a1-84da-11f7a02100fe | -10.23392 | -49.68775 | 2024-10-21 04:38:00 | NOAA-20 | PIUM | TOCANTINS | Brasil | 1717503 | 17 | 33 | nan | nan | nan | Cerrado | 1.9 |
| 37bc0ddd-5864-3149-bd09-dfd308e30bdf | -10.97833 | -49.30623 | 2024-10-21 04:38:00 | NOAA-20 | SANTA RITA DO TOCANTINS | TOCANTINS | Brasil | 1718899 | 17 | 33 | nan | nan | nan | Cerrado | 2.5 |
| e3796575-3290-3240-b0d2-3164c2e5e662 | -10.97498 | -49.30569 | 2024-10-21 04:38:00 | NOAA-20 | SANTA RITA DO TOCANTINS | TOCANTINS | Brasil | 1718899 | 17 | 33 | nan | nan | nan | Cerrado | 2.5 |
| b1fe784a-3b15-3062-8748-db075cc3edb1 | -10.97219 | -49.30157 | 2024-10-21 04:38:00 | NOAA-20 | SANTA RITA DO TOCANTINS | TOCANTINS | Brasil | 1718899 | 17 | 33 | nan | nan | nan | Cerrado | 0.4 |
| 388a83f7-7b29-362c-8b3b-b8d1c6f998e4 | -5.09179 | -49.59584 | 2024-10-21 04:38:00 | NOAA-20 | ITUPIRANGA | PARÁ | Brasil | 1503705 | 15 | 33 | nan | nan | nan | Amazônia | 0.7 |
| c042b8fc-7e61-324a-b024-d97b137002b9 | -5.0616 | -50.06525 | 2024-10-21 04:38:00 | NOAA-20 | ITUPIRANGA | PARÁ | Brasil | 1503705 | 15 | 33 | nan | nan | nan | Amazônia | 0.3 |
| cc0eb067-f3da-3694-93cf-a50fe7ec7772 | -5.05925 | -49.5872 | 2024-10-21 04:38:00 | NOAA-20 | ITUPIRANGA | PARÁ | Brasil | 1503705 | 15 | 33 | nan | nan | nan | Amazônia | 0.6 |
| d2c36605-b305-3add-b3c8-4fcf88439966 | -5.05871 | -49.59066 | 2024-10-21 04:38:00 | NOAA-20 | ITUPIRANGA | PARÁ | Brasil | 1503705 | 15 | 33 | nan | nan | nan | Amazônia | 1.5 |
| 7eb9fa96-767f-316b-be3b-925e8de3d65f | -5.05594 | -49.58669 | 2024-10-21 04:38:00 | NOAA-20 | ITUPIRANGA | PARÁ | Brasil | 1503705 | 15 | 33 | nan | nan | nan | Amazônia | 0.6 |
| 715cd688-6746-3dfc-a0a9-6b4e30c9c05d | -5.0554 | -49.59015 | 2024-10-21 04:38:00 | NOAA-20 | ITUPIRANGA | PARÁ | Brasil | 1503705 | 15 | 33 | nan | nan | nan | Amazônia | 1.5 |
| d0be80be-51be-35d0-89b9-1a1f5389daf7 | -4.96802 | -49.88557 | 2024-10-21 04:38:00 | NOAA-20 | ITUPIRANGA | PARÁ | Brasil | 1503705 | 15 | 33 | nan | nan | nan | Amazônia | 0.6 |
| 37aaa12e-dea6-3b57-b62c-6d565be0ecaf | -4.94757 | -50.46345 | 2024-10-21 04:38:00 | NOAA-20 | NOVO REPARTIMENTO | PARÁ | Brasil | 1505064 | 15 | 33 | nan | nan | nan | Amazônia | 1.7 |
| 2d0c76ca-03c8-3d56-a2af-72df7cc75d4d | -4.94421 | -50.46292 | 2024-10-21 04:38:00 | NOAA-20 | NOVO REPARTIMENTO | PARÁ | Brasil | 1505064 | 15 | 33 | nan | nan | nan | Amazônia | 1.7 |
| 077b8713-f193-34d2-92df-7e8152ac281c | -4.92519 | -50.45261 | 2024-10-21 04:38:00 | NOAA-20 | NOVO REPARTIMENTO | PARÁ | Brasil | 1505064 | 15 | 33 | nan | nan | nan | Amazônia | 0.8 |
| b735a7c5-d6ea-3aed-a469-d469dfee418e | -4.79519 | -50.71641 | 2024-10-21 04:38:00 | NOAA-20 | NOVO REPARTIMENTO | PARÁ | Brasil | 1505064 | 15 | 33 | nan | nan | nan | Amazônia | 0.4 |
| 2bef5db1-d4fb-35c0-91c6-49d37685c4fe | -6.21995 | -50.88443 | 2024-10-21 04:38:00 | NOAA-20 | PARAUAPEBAS | PARÁ | Brasil | 1505536 | 15 | 33 | nan | nan | nan | Amazônia | 1.2 |
| 3de1e731-4ce7-34a0-8e63-761c968cccee | -6.21657 | -50.88391 | 2024-10-21 04:38:00 | NOAA-20 | PARAUAPEBAS | PARÁ | Brasil | 1505536 | 15 | 33 | nan | nan | nan | Amazônia | 1.2 |
| 2feff5c8-2ca9-33c5-98a1-d11c190ae1b7 | -6.21378 | -50.87976 | 2024-10-21 04:38:00 | NOAA-20 | PARAUAPEBAS | PARÁ | Brasil | 1505536 | 15 | 33 | nan | nan | nan | Amazônia | 1.6 |
| a79e9dff-4d38-3c8b-998c-05abc49a09f4 | -6.21263 | -50.887 | 2024-10-21 04:38:00 | NOAA-20 | PARAUAPEBAS | PARÁ | Brasil | 1505536 | 15 | 33 | nan | nan | nan | Amazônia | 2.2 |
| 1c312fe5-6091-3b9f-842f-0d5fbb743337 | -6.21041 | -50.87923 | 2024-10-21 04:38:00 | NOAA-20 | PARAUAPEBAS | PARÁ | Brasil | 1505536 | 15 | 33 | nan | nan | nan | Amazônia | 1.6 |
| fd7ea7ab-6915-390a-8bca-aa798fbd8cd5 | -6.20646 | -50.88231 | 2024-10-21 04:38:00 | NOAA-20 | PARAUAPEBAS | PARÁ | Brasil | 1505536 | 15 | 33 | nan | nan | nan | Amazônia | 1.4 |
| 6e235532-8114-3bd2-ba86-318bbcafd62c | -6.20144 | -50.87043 | 2024-10-21 04:38:00 | NOAA-20 | PARAUAPEBAS | PARÁ | Brasil | 1505536 | 15 | 33 | nan | nan | nan | Amazônia | 1.3 |
| 4dc51776-c63d-3828-bd3e-6bdd6cbbc694 | -6.20029 | -50.87762 | 2024-10-21 04:38:00 | NOAA-20 | PARAUAPEBAS | PARÁ | Brasil | 1505536 | 15 | 33 | nan | nan | nan | Amazônia | 2.4 |
| c5e8f0af-613e-3b7f-82a4-1b39063484cc | -6.19972 | -50.88122 | 2024-10-21 04:38:00 | NOAA-20 | PARAUAPEBAS | PARÁ | Brasil | 1505536 | 15 | 33 | nan | nan | nan | Amazônia | 1.7 |
| e8ba8285-c862-3590-9470-1478a88b4ab8 | -6.1975 | -50.87349 | 2024-10-21 04:38:00 | NOAA-20 | PARAUAPEBAS | PARÁ | Brasil | 1505536 | 15 | 33 | nan | nan | nan | Amazônia | 2.4 |
| 47ad719e-1090-3a5c-9756-78818757100d | -6.19692 | -50.87709 | 2024-10-21 04:38:00 | NOAA-20 | PARAUAPEBAS | PARÁ | Brasil | 1505536 | 15 | 33 | nan | nan | nan | Amazônia | 2.4 |
| 8007bd5c-5c44-3f7f-b415-ee171c05fc58 | -6.19635 | -50.88068 | 2024-10-21 04:38:00 | NOAA-20 | PARAUAPEBAS | PARÁ | Brasil | 1505536 | 15 | 33 | nan | nan | nan | Amazônia | 1.7 |
| ca9fca45-2dda-3c09-a3f9-8467d8a0c9eb | -6.1947 | -50.86937 | 2024-10-21 04:38:00 | NOAA-20 | PARAUAPEBAS | PARÁ | Brasil | 1505536 | 15 | 33 | nan | nan | nan | Amazônia | 1.6 |
| 391c5bad-9a78-39a0-8883-2f1fe2051637 | -6.19413 | -50.87295 | 2024-10-21 04:38:00 | NOAA-20 | PARAUAPEBAS | PARÁ | Brasil | 1505536 | 15 | 33 | nan | nan | nan | Amazônia | 3.9 |
| 1a3e69e8-783e-391b-a2f9-fff0dac47be3 | -6.18738 | -50.87191 | 2024-10-21 04:38:00 | NOAA-20 | PARAUAPEBAS | PARÁ | Brasil | 1505536 | 15 | 33 | nan | nan | nan | Amazônia | 0.8 |
| ce39f0eb-cc9a-3a89-af62-d1ca9488537b | -6.18401 | -50.87138 | 2024-10-21 04:38:00 | NOAA-20 | PARAUAPEBAS | PARÁ | Brasil | 1505536 | 15 | 33 | nan | nan | nan | Amazônia | 0.8 |
| 7c9fa9c8-8eda-345b-ae06-4ccdbb81e3aa | -6.18171 | -50.88577 | 2024-10-21 04:38:00 | NOAA-20 | PARAUAPEBAS | PARÁ | Brasil | 1505536 | 15 | 33 | nan | nan | nan | Amazônia | 1.2 |
| 1729970f-0641-3ae3-a9c3-cb73e8c0bd50 | -6.18007 | -50.87444 | 2024-10-21 04:38:00 | NOAA-20 | PARAUAPEBAS | PARÁ | Brasil | 1505536 | 15 | 33 | nan | nan | nan | Amazônia | 1.4 |
| a7d30fc5-e6a3-3038-9cc9-911f89ee1352 | -6.17891 | -50.88163 | 2024-10-21 04:38:00 | NOAA-20 | PARAUAPEBAS | PARÁ | Brasil | 1505536 | 15 | 33 | nan | nan | nan | Amazônia | 1.5 |
| bf6d86da-0ed8-35f1-ac31-1be2a8164e8a | -6.17834 | -50.88524 | 2024-10-21 04:38:00 | NOAA-20 | PARAUAPEBAS | PARÁ | Brasil | 1505536 | 15 | 33 | nan | nan | nan | Amazônia | 1.7 |
| 487c1ff1-fd99-3293-b8ae-9b5c15951370 | -6.17554 | -50.88111 | 2024-10-21 04:38:00 | NOAA-20 | PARAUAPEBAS | PARÁ | Brasil | 1505536 | 15 | 33 | nan | nan | nan | Amazônia | 1.5 |
| f244b577-d186-3422-b03a-04cb72be60c6 | -6.05457 | -51.1537 | 2024-10-21 04:38:00 | NOAA-20 | MARABÁ | PARÁ | Brasil | 1504208 | 15 | 33 | nan | nan | nan | Amazônia | 0.9 |
| 2ab8a36b-cf57-37fb-8d87-49c3519a4c74 | -6.05059 | -51.15684 | 2024-10-21 04:38:00 | NOAA-20 | MARABÁ | PARÁ | Brasil | 1504208 | 15 | 33 | nan | nan | nan | Amazônia | 0.8 |
| 004b1bc8-436d-3b88-80e4-eb5866b0ae45 | -5.91488 | -51.06352 | 2024-10-21 04:38:00 | NOAA-20 | MARABÁ | PARÁ | Brasil | 1504208 | 15 | 33 | nan | nan | nan | Amazônia | 1.8 |


[Clique aqui para ver as próximas entradas](README48.md)
