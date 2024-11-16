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
| 749ee0be-2fb4-3df8-b39c-09793bc20ce8 | -3.97049 | -45.80446 | 2024-11-16 04:23:00 | NPP-375D | SANTA LUZIA | MARANHÃO | Brasil | 2110005 | 21 | 33 | nan | nan | nan | Amazônia | 1.3 |
| 3ec7641c-76bc-3152-aaa2-7771774a69a7 | -3.03554 | -47.98214 | 2024-11-16 04:23:00 | NPP-375D | IPIXUNA DO PARÁ | PARÁ | Brasil | 1503457 | 15 | 33 | nan | nan | nan | Amazônia | 2.1 |
| e3df6750-19f0-3456-895a-43bb37d71b0e | -2.64403 | -46.19112 | 2024-11-16 04:23:00 | NPP-375D | CENTRO DO GUILHERME | MARANHÃO | Brasil | 2103158 | 21 | 33 | nan | nan | nan | Amazônia | 0.9 |
| 577059b3-09fb-37b3-a71a-15b38823b1d3 | -2.08434 | -48.95302 | 2024-11-16 04:23:00 | NPP-375D | MOJU | PARÁ | Brasil | 1504703 | 15 | 33 | nan | nan | nan | Amazônia | 3.6 |
| 50b75a76-b00c-34b2-b256-71d43125ed6c | -2.82577 | -46.66124 | 2024-11-16 04:23:00 | NPP-375D | PARAGOMINAS | PARÁ | Brasil | 1505502 | 15 | 33 | nan | nan | nan | Amazônia | 1.2 |
| 7f3c201c-1838-375f-b277-59f1861df868 | -3.85655 | -46.63249 | 2024-11-16 04:23:00 | NPP-375D | BOM JARDIM | MARANHÃO | Brasil | 2102002 | 21 | 33 | nan | nan | nan | Amazônia | 1.3 |
| b5f0e7e5-9a5c-3231-b1f8-2d145e1d01de | -0.78343 | -49.48296 | 2024-11-16 04:23:00 | NPP-375D | PONTA DE PEDRAS | PARÁ | Brasil | 1505700 | 15 | 33 | nan | nan | nan | Amazônia | 2.1 |
| 05de8d73-7a2d-3062-a17e-3582fa567257 | -3.98925 | -43.71825 | 2024-11-16 04:23:00 | NPP-375D | TIMBIRAS | MARANHÃO | Brasil | 2112100 | 21 | 33 | nan | nan | nan | Cerrado | 3.9 |
| e528bbc3-dec6-36dc-af35-82fbb33a48b5 | -4.35365 | -45.84735 | 2024-11-16 04:23:00 | NPP-375D | SANTA LUZIA | MARANHÃO | Brasil | 2110005 | 21 | 33 | nan | nan | nan | Amazônia | 0.8 |
| 799e97a6-433b-3324-bbdb-c94fe43bf8b4 | -2.66417 | -46.83917 | 2024-11-16 04:23:00 | NPP-375D | PARAGOMINAS | PARÁ | Brasil | 1505502 | 15 | 33 | nan | nan | nan | Amazônia | 2.2 |
| 5e6a1d83-577c-3ce4-aa01-fbef49db0d53 | -2.39433 | -46.18404 | 2024-11-16 04:23:00 | NPP-375D | CENTRO DO GUILHERME | MARANHÃO | Brasil | 2103158 | 21 | 33 | nan | nan | nan | Amazônia | 1.3 |
| 5a91423e-9d51-3ce8-a9c7-602de7fa32d0 | -2.10021 | -46.58532 | 2024-11-16 04:23:00 | NPP-375D | CACHOEIRA DO PIRIÁ | PARÁ | Brasil | 1501956 | 15 | 33 | nan | nan | nan | Amazônia | 1.1 |
| bc899b96-0533-33e9-b2d0-a0cfa8fcbb72 | -3.50463 | -47.21859 | 2024-11-16 04:23:00 | NPP-375D | ULIANÓPOLIS | PARÁ | Brasil | 1508126 | 15 | 33 | nan | nan | nan | Amazônia | 3.2 |
| 677fade1-910d-3ddb-a620-a5c79320b79b | -2.47682 | -46.37012 | 2024-11-16 04:23:00 | NPP-375D | CENTRO NOVO DO MARANHÃO | MARANHÃO | Brasil | 2103174 | 21 | 33 | nan | nan | nan | Amazônia | 3.2 |
| 6097615d-79ce-31cf-a6f3-953c9c8f4077 | -2.97238 | -47.99236 | 2024-11-16 04:23:00 | NPP-375D | IPIXUNA DO PARÁ | PARÁ | Brasil | 1503457 | 15 | 33 | nan | nan | nan | Amazônia | 12.8 |
| 6cb8b573-6f96-3620-9b1f-4ef251a55e95 | -3.27015 | -45.50417 | 2024-11-16 04:23:00 | NPP-375D | PENALVA | MARANHÃO | Brasil | 2108306 | 21 | 33 | nan | nan | nan | Amazônia | 29.4 |
| ef797147-5b46-3f9c-90d4-10c56460941d | -3.08141 | -47.76482 | 2024-11-16 04:23:00 | NPP-375D | PARAGOMINAS | PARÁ | Brasil | 1505502 | 15 | 33 | nan | nan | nan | Amazônia | 1.3 |
| 74a1cef1-988e-348f-974e-57d88420cb08 | -2.62843 | -46.1815 | 2024-11-16 04:23:00 | NPP-375D | CENTRO DO GUILHERME | MARANHÃO | Brasil | 2103158 | 21 | 33 | nan | nan | nan | Amazônia | 2.8 |
| e80a6bbf-4f81-3d5e-a8c0-710e5f44299e | 2.66197 | -50.89567 | 2024-11-16 04:23:00 | NPP-375D | CALÇOENE | AMAPÁ | Brasil | 1600204 | 16 | 33 | nan | nan | nan | Amazônia | 1.8 |
| e94c5870-ffd0-38a6-9801-1a50e57ecb32 | -2.64496 | -46.82869 | 2024-11-16 04:23:00 | NPP-375D | PARAGOMINAS | PARÁ | Brasil | 1505502 | 15 | 33 | nan | nan | nan | Amazônia | 1.6 |
| 7b10d705-6914-3ec3-ae0a-3ac9d1cf1fcd | -2.93398 | -48.32346 | 2024-11-16 04:23:00 | NPP-375D | TOMÉ-AÇU | PARÁ | Brasil | 1508001 | 15 | 33 | nan | nan | nan | Amazônia | 1.4 |
| e6fe25ff-7517-32eb-bd40-1438aee4051c | -2.95027 | -48.01715 | 2024-11-16 04:23:00 | NPP-375D | IPIXUNA DO PARÁ | PARÁ | Brasil | 1503457 | 15 | 33 | nan | nan | nan | Amazônia | 1.8 |
| ac995e28-e64d-39ad-b8bc-7d61aea9289c | -3.93569 | -46.47253 | 2024-11-16 04:23:00 | NPP-375D | BOM JARDIM | MARANHÃO | Brasil | 2102002 | 21 | 33 | nan | nan | nan | Amazônia | 1.0 |
| eda02f9f-4626-3bf2-9b1b-6bedc271ce53 | -2.79012 | -45.95315 | 2024-11-16 04:23:00 | NPP-375D | NOVA OLINDA DO MARANHÃO | MARANHÃO | Brasil | 2107357 | 21 | 33 | nan | nan | nan | Amazônia | 2.1 |
| 72732cc2-20a8-3e58-8fdc-bc5ba5c505ce | -2.03121 | -48.9722 | 2024-11-16 04:23:00 | NPP-375D | IGARAPÉ-MIRI | PARÁ | Brasil | 1503309 | 15 | 33 | nan | nan | nan | Amazônia | 1.1 |
| 710d07dc-4fdd-388a-ba0c-896c3024f408 | -2.56839 | -54.42543 | 2024-11-16 04:23:00 | NPP-375D | SANTARÉM | PARÁ | Brasil | 1506807 | 15 | 33 | nan | nan | nan | Amazônia | 2.3 |
| d417a128-11da-3b4b-9c03-e186a4eb42d5 | -5.66474 | -35.65311 | 2024-11-16 04:23:00 | NPP-375D | POÇO BRANCO | RIO GRANDE DO NORTE | Brasil | 2410108 | 24 | 33 | nan | nan | nan | Caatinga | 3.1 |
| e3d46557-ec8f-336e-a5c4-5e7532bd4d9b | -2.77742 | -48.58092 | 2024-11-16 04:23:00 | NPP-375D | TAILÂNDIA | PARÁ | Brasil | 1507953 | 15 | 33 | nan | nan | nan | Amazônia | 19.9 |
| 9f14a59c-8028-36c4-bf87-36ac9f5f52be | -2.2386 | -46.8364 | 2024-11-16 04:23:00 | NPP-375D | NOVA ESPERANÇA DO PIRIÁ | PARÁ | Brasil | 1504950 | 15 | 33 | nan | nan | nan | Amazônia | 1.7 |
| 1e35633b-35ae-339f-9c2a-cf9044f3b4aa | -2.32064 | -46.18362 | 2024-11-16 04:23:00 | NPP-375D | CENTRO DO GUILHERME | MARANHÃO | Brasil | 2103158 | 21 | 33 | nan | nan | nan | Amazônia | 0.8 |
| 5d4b955d-c8b8-396f-9da6-aa45152d235e | -3.04323 | -47.9783 | 2024-11-16 04:23:00 | NPP-375D | IPIXUNA DO PARÁ | PARÁ | Brasil | 1503457 | 15 | 33 | nan | nan | nan | Amazônia | 2.9 |
| ea5214b1-8c34-3c85-9663-49bd5f174187 | -3.03096 | -47.96534 | 2024-11-16 04:23:00 | NPP-375D | IPIXUNA DO PARÁ | PARÁ | Brasil | 1503457 | 15 | 33 | nan | nan | nan | Amazônia | 1.2 |
| 783e5937-df49-3797-a972-f49c3f73ce27 | -3.09748 | -45.97591 | 2024-11-16 04:23:00 | NPP-375D | ZÉ DOCA | MARANHÃO | Brasil | 2114007 | 21 | 33 | nan | nan | nan | Amazônia | 1.0 |
| 6e323a7d-397b-3781-af64-4d7dc3d2db9c | -4.12445 | -50.43024 | 2024-11-16 04:23:00 | NPP-375D | NOVO REPARTIMENTO | PARÁ | Brasil | 1505064 | 15 | 33 | nan | nan | nan | Amazônia | 1.4 |
| 2c2ceb04-80d1-38a7-8966-01af8855f007 | -1.5542 | -54.31501 | 2024-11-16 04:23:00 | NPP-375D | MONTE ALEGRE | PARÁ | Brasil | 1504802 | 15 | 33 | nan | nan | nan | Amazônia | 3.2 |
| 3f87bb3e-6726-3f81-a3b6-7a1814f8c8ff | -3.71953 | -51.84555 | 2024-11-16 04:23:00 | NPP-375D | SENADOR JOSÉ PORFÍRIO | PARÁ | Brasil | 1507805 | 15 | 33 | nan | nan | nan | Amazônia | 1.5 |
| 2f498951-890d-30e1-b3fa-8e7c0e2eec23 | -2.62748 | -46.52478 | 2024-11-16 04:23:00 | NPP-375D | CENTRO NOVO DO MARANHÃO | MARANHÃO | Brasil | 2103174 | 21 | 33 | nan | nan | nan | Amazônia | 0.7 |
| d7d2e3f5-8f70-3ffd-8826-04d7bfbd1adc | -2.66799 | -46.1913 | 2024-11-16 04:23:00 | NPP-375D | CENTRO NOVO DO MARANHÃO | MARANHÃO | Brasil | 2103174 | 21 | 33 | nan | nan | nan | Amazônia | 2.6 |
| ee8375f3-7069-372e-8a71-5ba83de6dc10 | -4.36467 | -45.62617 | 2024-11-16 04:23:00 | NPP-375D | BREJO DE AREIA | MARANHÃO | Brasil | 2102150 | 21 | 33 | nan | nan | nan | Amazônia | 1.3 |
| 9d6369ca-19f0-3afc-9d9b-28c96bd452ff | -3.72273 | -45.6598 | 2024-11-16 04:23:00 | NPP-375D | ALTO ALEGRE DO PINDARÉ | MARANHÃO | Brasil | 2100477 | 21 | 33 | nan | nan | nan | Amazônia | 1.1 |
| 2c79c4d8-f0a8-35ea-8b17-54efbdbb8efb | -3.0351 | -47.96196 | 2024-11-16 04:23:00 | NPP-375D | IPIXUNA DO PARÁ | PARÁ | Brasil | 1503457 | 15 | 33 | nan | nan | nan | Amazônia | 1.6 |
| 35739022-9a42-37c2-b5e8-9caf0b973427 | -3.33117 | -43.82182 | 2024-11-16 04:23:00 | NPP-375D | NINA RODRIGUES | MARANHÃO | Brasil | 2107209 | 21 | 33 | nan | nan | nan | Cerrado | 1.7 |
| b4602da8-0c93-3e06-a278-f13ff0e3d454 | -1.71095 | -46.15709 | 2024-11-16 04:23:00 | NPP-375D | BOA VISTA DO GURUPI | MARANHÃO | Brasil | 2101970 | 21 | 33 | nan | nan | nan | Amazônia | 1.5 |
| 139b7c41-365e-31cb-b270-ef61da9260ed | -3.99643 | -46.50005 | 2024-11-16 04:23:00 | NPP-375D | BOM JARDIM | MARANHÃO | Brasil | 2102002 | 21 | 33 | nan | nan | nan | Amazônia | 1.5 |
| 30335528-ad23-3301-8955-f49aab44ee5d | -2.1794 | -47.94758 | 2024-11-16 04:23:00 | NPP-375D | SÃO DOMINGOS DO CAPIM | PARÁ | Brasil | 1507201 | 15 | 33 | nan | nan | nan | Amazônia | 1.2 |
| f388d532-5467-3142-8fad-061181c3a0a7 | -2.07875 | -46.4754 | 2024-11-16 04:23:00 | NPP-375D | CACHOEIRA DO PIRIÁ | PARÁ | Brasil | 1501956 | 15 | 33 | nan | nan | nan | Amazônia | 1.5 |
| 16d5629a-a87c-3a69-ac30-34d863cc990f | -2.95091 | -48.0132 | 2024-11-16 04:23:00 | NPP-375D | IPIXUNA DO PARÁ | PARÁ | Brasil | 1503457 | 15 | 33 | nan | nan | nan | Amazônia | 1.8 |
| 813aa851-a938-3de0-b802-879dbcac90bf | -2.62744 | -46.82954 | 2024-11-16 04:23:00 | NPP-375D | PARAGOMINAS | PARÁ | Brasil | 1505502 | 15 | 33 | nan | nan | nan | Amazônia | 1.1 |
| 4088755b-1b03-3336-a3d1-005bd690bb83 | -2.47179 | -46.35846 | 2024-11-16 04:23:00 | NPP-375D | CENTRO NOVO DO MARANHÃO | MARANHÃO | Brasil | 2103174 | 21 | 33 | nan | nan | nan | Amazônia | 1.6 |
| 0adb60dc-3865-39c9-8ca8-b3e2c1d4f50e | -4.2305 | -50.67403 | 2024-11-16 04:23:00 | NPP-375D | NOVO REPARTIMENTO | PARÁ | Brasil | 1505064 | 15 | 33 | nan | nan | nan | Amazônia | 2.1 |
| a031fd4c-2c58-33bd-8e47-f161d85b03fa | -3.19496 | -45.55189 | 2024-11-16 04:23:00 | NPP-375D | PEDRO DO ROSÁRIO | MARANHÃO | Brasil | 2108256 | 21 | 33 | nan | nan | nan | Amazônia | 14.1 |
| 67bf83c8-d468-3aec-8212-45ffa4f36470 | -2.649 | -46.15962 | 2024-11-16 04:23:00 | NPP-375D | CENTRO DO GUILHERME | MARANHÃO | Brasil | 2103158 | 21 | 33 | nan | nan | nan | Amazônia | 2.0 |
| c9ad2d3f-0270-344f-9358-7e83845b63e4 | -4.21995 | -46.81293 | 2024-11-16 04:23:00 | NPP-375D | BOM JARDIM | MARANHÃO | Brasil | 2102002 | 21 | 33 | nan | nan | nan | Amazônia | 2.0 |
| f591e9de-f195-327b-b236-af04ffa4b750 | -2.97655 | -47.98898 | 2024-11-16 04:23:00 | NPP-375D | IPIXUNA DO PARÁ | PARÁ | Brasil | 1503457 | 15 | 33 | nan | nan | nan | Amazônia | 8.4 |
| 48d19b73-4e01-3523-a1dd-a2bdf05cc5ee | -2.18162 | -47.95103 | 2024-11-16 04:23:00 | NPP-375D | SÃO DOMINGOS DO CAPIM | PARÁ | Brasil | 1507201 | 15 | 33 | nan | nan | nan | Amazônia | 1.2 |
| 970254bd-b38e-3c7e-8c3c-b0a23020cbf5 | -1.1207 | -48.37796 | 2024-11-16 04:23:00 | NPP-375D | BELÉM | PARÁ | Brasil | 1501402 | 15 | 33 | nan | nan | nan | Amazônia | 0.6 |
| 89f8eefc-f2d1-3453-a1da-0acaf57c8117 | -4.10606 | -46.10261 | 2024-11-16 04:23:00 | NPP-375D | SANTA LUZIA | MARANHÃO | Brasil | 2110005 | 21 | 33 | nan | nan | nan | Amazônia | 1.0 |
| 8ac79180-dcb7-3fd0-b8d6-27853c0de03f | -3.45413 | -47.66517 | 2024-11-16 04:23:00 | NPP-375D | PARAGOMINAS | PARÁ | Brasil | 1505502 | 15 | 33 | nan | nan | nan | Amazônia | 0.7 |
| c1e8486d-ec87-3967-b025-84c160d48613 | -2.66296 | -46.17974 | 2024-11-16 04:23:00 | NPP-375D | CENTRO DO GUILHERME | MARANHÃO | Brasil | 2103158 | 21 | 33 | nan | nan | nan | Amazônia | 1.5 |
| 545c526c-c72c-30b9-9369-4d619cd3bb95 | -3.25142 | -46.52384 | 2024-11-16 04:23:00 | NPP-375D | CENTRO NOVO DO MARANHÃO | MARANHÃO | Brasil | 2103174 | 21 | 33 | nan | nan | nan | Amazônia | 1.0 |
| 0b1ffdc0-d605-3458-b3c3-0b3f1d238a1a | -4.61501 | -45.34632 | 2024-11-16 04:23:00 | NPP-375D | PAULO RAMOS | MARANHÃO | Brasil | 2108108 | 21 | 33 | nan | nan | nan | Cerrado | 0.8 |
| 295a3771-d31e-3051-a572-a036d9e3667c | -2.64069 | -46.1906 | 2024-11-16 04:23:00 | NPP-375D | CENTRO DO GUILHERME | MARANHÃO | Brasil | 2103158 | 21 | 33 | nan | nan | nan | Amazônia | 0.9 |
| 16156c62-3d54-3467-ac8c-29a34cc23ff3 | -2.64778 | -46.83287 | 2024-11-16 04:23:00 | NPP-375D | PARAGOMINAS | PARÁ | Brasil | 1505502 | 15 | 33 | nan | nan | nan | Amazônia | 1.8 |
| 1dcb8156-ddcc-3e95-bc13-abd3b362b65c | -4.37131 | -45.62721 | 2024-11-16 04:23:00 | NPP-375D | BREJO DE AREIA | MARANHÃO | Brasil | 2102150 | 21 | 33 | nan | nan | nan | Amazônia | 1.0 |
| b306fe78-6101-38fb-beb1-47d4f8eb139e | -2.64293 | -46.19812 | 2024-11-16 04:23:00 | NPP-375D | CENTRO DO GUILHERME | MARANHÃO | Brasil | 2103158 | 21 | 33 | nan | nan | nan | Amazônia | 0.8 |
| 9d09bfe6-afe9-3d19-b070-0fb9bdae0ad2 | -3.04722 | -44.9422 | 2024-11-16 04:23:00 | NPP-375D | OLINDA NOVA DO MARANHÃO | MARANHÃO | Brasil | 2107456 | 21 | 33 | nan | nan | nan | Amazônia | 0.9 |
| a2024923-9609-3650-a4cb-a0eb33c9a46c | -2.14982 | -46.55639 | 2024-11-16 04:23:00 | NPP-375D | CACHOEIRA DO PIRIÁ | PARÁ | Brasil | 1501956 | 15 | 33 | nan | nan | nan | Amazônia | 2.1 |
| 219108de-6d59-39f1-a61a-8e39cc205276 | -4.21734 | -47.22066 | 2024-11-16 04:23:00 | NPP-375D | ITINGA DO MARANHÃO | MARANHÃO | Brasil | 2105427 | 21 | 33 | nan | nan | nan | Amazônia | 6.3 |
| 9dfbbd08-cb3d-358a-abfb-798a486c4b69 | -5.33846 | -40.89246 | 2024-11-16 04:23:00 | NPP-375D | CRATEÚS | CEARÁ | Brasil | 2304103 | 23 | 33 | nan | nan | nan | Caatinga | 0.7 |
| 7ccf4b34-05ea-3b90-aab2-de7f70d104fe | -2.57376 | -54.42634 | 2024-11-16 04:23:00 | NPP-375D | SANTARÉM | PARÁ | Brasil | 1506807 | 15 | 33 | nan | nan | nan | Amazônia | 2.3 |
| 0eab4c38-71cb-3aa5-8dcd-ba2cbe44ebf3 | -4.45369 | -42.92998 | 2024-11-16 04:23:00 | NPP-375D | CAXIAS | MARANHÃO | Brasil | 2103000 | 21 | 33 | nan | nan | nan | Cerrado | 1.4 |
| 8096e2eb-96fb-37bb-a86a-e446ff159d86 | -3.11024 | -45.98146 | 2024-11-16 04:23:00 | NPP-375D | ZÉ DOCA | MARANHÃO | Brasil | 2114007 | 21 | 33 | nan | nan | nan | Amazônia | 0.8 |
| 88ee6752-34a7-3678-a72f-8a4a898f8f05 | -4.37903 | -45.62134 | 2024-11-16 04:23:00 | NPP-375D | BREJO DE AREIA | MARANHÃO | Brasil | 2102150 | 21 | 33 | nan | nan | nan | Amazônia | 0.9 |
| c7b87181-29bc-3fd1-8fbe-06b072e441a4 | -2.63959 | -46.1976 | 2024-11-16 04:23:00 | NPP-375D | CENTRO DO GUILHERME | MARANHÃO | Brasil | 2103158 | 21 | 33 | nan | nan | nan | Amazônia | 0.9 |
| 3d723852-0e28-3d0a-8cdd-fb1e18f8c48c | -2.11627 | -46.37587 | 2024-11-16 04:23:00 | NPP-375D | CACHOEIRA DO PIRIÁ | PARÁ | Brasil | 1501956 | 15 | 33 | nan | nan | nan | Amazônia | 1.3 |
| 710e1692-83d4-3b17-bd8a-ed56d867228f | -2.68328 | -46.83043 | 2024-11-16 04:23:00 | NPP-375D | PARAGOMINAS | PARÁ | Brasil | 1505502 | 15 | 33 | nan | nan | nan | Amazônia | 0.8 |
| 0332f3a5-6675-376b-baaa-57e9e3ad3914 | -4.33421 | -48.61953 | 2024-11-16 04:23:00 | NPP-375D | RONDON DO PARÁ | PARÁ | Brasil | 1506187 | 15 | 33 | nan | nan | nan | Amazônia | 1.6 |
| 5d7fcd9c-2a12-3e57-a9ec-0dbfd6b38369 | -2.21703 | -50.51112 | 2024-11-16 04:23:00 | NPP-375D | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 1.2 |
| fcb7902d-d3a7-3e7d-9440-806cf03db7b4 | -3.18707 | -46.53912 | 2024-11-16 04:23:00 | NPP-375D | CENTRO NOVO DO MARANHÃO | MARANHÃO | Brasil | 2103174 | 21 | 33 | nan | nan | nan | Amazônia | 0.8 |
| b19544e6-b54f-3bdc-b59e-ad03f5319b58 | -4.81121 | -42.91826 | 2024-11-16 04:23:00 | NPP-375D | UNIÃO | PIAUÍ | Brasil | 2211100 | 22 | 33 | nan | nan | nan | Cerrado | 5.4 |
| 6a75a9bd-bbba-3cd7-ad03-4aae46e14bb0 | -2.1684 | -46.46051 | 2024-11-16 04:23:00 | NPP-375D | CACHOEIRA DO PIRIÁ | PARÁ | Brasil | 1501956 | 15 | 33 | nan | nan | nan | Amazônia | 0.8 |
| 8b7bfadf-2bbd-3cbd-9757-114cbb191f18 | -2.33375 | -45.99212 | 2024-11-16 04:23:00 | NPP-375D | MARANHÃOZINHO | MARANHÃO | Brasil | 2106375 | 21 | 33 | nan | nan | nan | Amazônia | 1.2 |
| 4d627a41-e2c1-3281-add5-a7fd706d3f69 | -4.22589 | -50.67688 | 2024-11-16 04:23:00 | NPP-375D | NOVO REPARTIMENTO | PARÁ | Brasil | 1505064 | 15 | 33 | nan | nan | nan | Amazônia | 2.1 |
| 3ee5a04e-1257-3900-8672-f63d47341717 | -3.88166 | -52.26957 | 2024-11-16 04:23:00 | NPP-375D | SENADOR JOSÉ PORFÍRIO | PARÁ | Brasil | 1507805 | 15 | 33 | nan | nan | nan | Amazônia | 0.8 |
| 4ec43402-baac-3975-9403-e0b53bf20277 | -2.64813 | -48.47933 | 2024-11-16 04:23:00 | NPP-375D | TAILÂNDIA | PARÁ | Brasil | 1507953 | 15 | 33 | nan | nan | nan | Amazônia | 9.4 |
| 75929df5-261b-3239-bebc-4b6b23aa2c04 | -2.93068 | -48.071 | 2024-11-16 04:23:00 | NPP-375D | IPIXUNA DO PARÁ | PARÁ | Brasil | 1503457 | 15 | 33 | nan | nan | nan | Amazônia | 0.9 |
| b61e0955-1ab7-3eaf-a3df-bf57a1a79916 | -3.94283 | -46.70816 | 2024-11-16 04:23:00 | NPP-375D | BOM JARDIM | MARANHÃO | Brasil | 2102002 | 21 | 33 | nan | nan | nan | Amazônia | 1.8 |
| 1bb9f492-cf76-37ff-896d-a90beae8e418 | -3.19042 | -46.53964 | 2024-11-16 04:23:00 | NPP-375D | CENTRO NOVO DO MARANHÃO | MARANHÃO | Brasil | 2103174 | 21 | 33 | nan | nan | nan | Amazônia | 1.5 |
| 9bf1c296-5663-32a6-bc96-7eb525d0c0bd | -2.21685 | -48.39995 | 2024-11-16 04:23:00 | NPP-375D | ACARÁ | PARÁ | Brasil | 1500206 | 15 | 33 | nan | nan | nan | Amazônia | 0.9 |
| a4057fbb-7059-3667-86d3-37d0cf14bd99 | -2.26986 | -46.59344 | 2024-11-16 04:23:00 | NPP-375D | NOVA ESPERANÇA DO PIRIÁ | PARÁ | Brasil | 1504950 | 15 | 33 | nan | nan | nan | Amazônia | 1.2 |
| 4200ee94-8fc0-34af-b14b-deeec97dba76 | -4.10589 | -46.87198 | 2024-11-16 04:23:00 | NPP-375D | BOM JARDIM | MARANHÃO | Brasil | 2102002 | 21 | 33 | nan | nan | nan | Amazônia | 0.9 |
| 482a02eb-621c-34c9-ade7-d73bba865958 | -3.46435 | -51.61875 | 2024-11-16 04:23:00 | NPP-375D | ANAPU | PARÁ | Brasil | 1500859 | 15 | 33 | nan | nan | nan | Amazônia | 0.6 |
| 0582513a-c4e1-33cf-b066-57d38e41b515 | -3.28065 | -45.50227 | 2024-11-16 04:23:00 | NPP-375D | MONÇÃO | MARANHÃO | Brasil | 2106904 | 21 | 33 | nan | nan | nan | Amazônia | 17.3 |
| 9e9b1ded-bc46-38ec-a48f-43d35594ba35 | -2.2884 | -46.45372 | 2024-11-16 04:23:00 | NPP-375D | CACHOEIRA DO PIRIÁ | PARÁ | Brasil | 1501956 | 15 | 33 | nan | nan | nan | Amazônia | 1.2 |
| 609579d0-095f-3ca9-9343-fe3ae8acbff7 | -3.75791 | -44.39661 | 2024-11-16 04:23:00 | NPP-375D | MATÕES DO NORTE | MARANHÃO | Brasil | 2106631 | 21 | 33 | nan | nan | nan | Cerrado | 0.9 |
| a0bc5224-5651-325f-be03-72cd507c5a71 | -2.64382 | -46.83594 | 2024-11-16 04:23:00 | NPP-375D | PARAGOMINAS | PARÁ | Brasil | 1505502 | 15 | 33 | nan | nan | nan | Amazônia | 1.8 |
| b0121f0e-261f-3bc7-b10f-941f3984aa88 | -4.09453 | -49.97361 | 2024-11-16 04:23:00 | NPP-375D | NOVO REPARTIMENTO | PARÁ | Brasil | 1505064 | 15 | 33 | nan | nan | nan | Amazônia | 1.8 |
| 20e9cf90-a16d-3dd4-b8a7-7ec9b45c232e | -3.78791 | -43.91319 | 2024-11-16 04:23:00 | NPP-375D | VARGEM GRANDE | MARANHÃO | Brasil | 2112704 | 21 | 33 | nan | nan | nan | Cerrado | 4.4 |
| 80cb5669-f072-39a1-aa2a-903e551d68e9 | -4.55364 | -45.75815 | 2024-11-16 04:23:00 | NPP-375D | SANTA LUZIA | MARANHÃO | Brasil | 2110005 | 21 | 33 | nan | nan | nan | Amazônia | 2.1 |
| 218afc10-b5e0-36f1-aff2-2f5d9f5632c5 | -4.12262 | -46.94036 | 2024-11-16 04:23:00 | NPP-375D | BOM JARDIM | MARANHÃO | Brasil | 2102002 | 21 | 33 | nan | nan | nan | Amazônia | 1.0 |


[Clique aqui para ver as próximas entradas](README33.md)
