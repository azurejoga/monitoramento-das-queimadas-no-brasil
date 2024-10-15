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
| e324e034-7618-3147-8dbf-04be89a834c5 | -11.68988 | -65.23858 | 2024-10-15 01:56:00 | TERRA_M-M | GUAJARÁ-MIRIM | RONDÔNIA | Brasil | 1100106 | 11 | 33 | nan | nan | nan | Amazônia | 89.7 |
| 9856bf85-9625-32e4-8a70-c2e73b513554 | -11.68855 | -65.22826 | 2024-10-15 01:56:00 | TERRA_M-M | GUAJARÁ-MIRIM | RONDÔNIA | Brasil | 1100106 | 11 | 33 | nan | nan | nan | Amazônia | 64.0 |
| 2ec5811d-da58-30b3-8547-e7e10d520281 | -11.51767 | -61.89085 | 2024-10-15 01:56:00 | TERRA_M-M | CASTANHEIRAS | RONDÔNIA | Brasil | 1100908 | 11 | 33 | nan | nan | nan | Amazônia | 4.1 |
| 94a983ea-efea-3823-88d7-a986cdb5132d | -10.94814 | -54.11621 | 2024-10-15 01:56:00 | TERRA_M-M | MARCELÂNDIA | MATO GROSSO | Brasil | 5105580 | 51 | 33 | nan | nan | nan | Amazônia | 21.4 |
| 7626266d-dcfa-303b-8207-77e7d9d64da8 | -10.94578 | -61.13214 | 2024-10-15 01:56:00 | TERRA_M-M | RONDOLÂNDIA | MATO GROSSO | Brasil | 5107578 | 51 | 33 | nan | nan | nan | Amazônia | 8.8 |
| 9631569e-b9b8-3d2f-b8b3-41adcb9a1b81 | -10.94346 | -54.11204 | 2024-10-15 01:56:00 | TERRA_M-M | MARCELÂNDIA | MATO GROSSO | Brasil | 5105580 | 51 | 33 | nan | nan | nan | Amazônia | 61.6 |
| a8bf9b3a-0d75-3b6e-98d1-b2f2d2ca06b2 | -10.94141 | -61.1025 | 2024-10-15 01:56:00 | TERRA_M-M | RONDOLÂNDIA | MATO GROSSO | Brasil | 5107578 | 51 | 33 | nan | nan | nan | Amazônia | 4.5 |
| 4eade729-94ed-3b82-b626-e87cd43055c2 | -10.93271 | -54.11926 | 2024-10-15 01:56:00 | TERRA_M-M | MARCELÂNDIA | MATO GROSSO | Brasil | 5105580 | 51 | 33 | nan | nan | nan | Amazônia | 22.2 |
| f70a95e2-6646-33a3-9843-1757b7bb75b2 | -10.86229 | -62.33761 | 2024-10-15 01:56:00 | TERRA_M-M | OURO PRETO DO OESTE | RONDÔNIA | Brasil | 1100155 | 11 | 33 | nan | nan | nan | Amazônia | 9.2 |
| 835b4c39-1209-3a59-8a6c-b701ac971cc9 | -10.86099 | -62.32853 | 2024-10-15 01:56:00 | TERRA_M-M | OURO PRETO DO OESTE | RONDÔNIA | Brasil | 1100155 | 11 | 33 | nan | nan | nan | Amazônia | 10.3 |
| 0094f1d1-2210-3f8b-86d8-f4bd833197f1 | -10.80193 | -53.88725 | 2024-10-15 01:56:00 | TERRA_M-M | MARCELÂNDIA | MATO GROSSO | Brasil | 5105580 | 51 | 33 | nan | nan | nan | Amazônia | 24.2 |
| 3a7a7aa1-d0a3-3f75-97d8-4710b3271e33 | -10.63067 | -61.43459 | 2024-10-15 01:56:00 | TERRA_M-M | RONDOLÂNDIA | MATO GROSSO | Brasil | 5107578 | 51 | 33 | nan | nan | nan | Amazônia | 6.3 |
| 8ac2fd51-c0f7-3e4e-982c-7b003d9394e7 | -10.62927 | -61.42497 | 2024-10-15 01:56:00 | TERRA_M-M | RONDOLÂNDIA | MATO GROSSO | Brasil | 5107578 | 51 | 33 | nan | nan | nan | Amazônia | 3.6 |
| 794a9684-bb97-320a-98a6-7c38174897d7 | -10.45116 | -61.27496 | 2024-10-15 01:56:00 | TERRA_M-M | RONDOLÂNDIA | MATO GROSSO | Brasil | 5107578 | 51 | 33 | nan | nan | nan | Amazônia | 7.2 |
| 9c30c0a5-5107-344d-994c-c2271997a2a3 | -10.44971 | -61.26505 | 2024-10-15 01:56:00 | TERRA_M-M | RONDOLÂNDIA | MATO GROSSO | Brasil | 5107578 | 51 | 33 | nan | nan | nan | Amazônia | 11.8 |
| ab61a8d2-ab30-3842-b0f0-a2c161caef27 | -10.4419 | -61.27629 | 2024-10-15 01:56:00 | TERRA_M-M | RONDOLÂNDIA | MATO GROSSO | Brasil | 5107578 | 51 | 33 | nan | nan | nan | Amazônia | 6.0 |
| 1a4f88de-04f4-308b-aff6-aca36c79fb5f | -10.42413 | -61.02404 | 2024-10-15 01:56:00 | TERRA_M-M | RONDOLÂNDIA | MATO GROSSO | Brasil | 5107578 | 51 | 33 | nan | nan | nan | Amazônia | 28.0 |
| 77de37ae-8066-352a-b28b-00f766880aaf | -10.42265 | -61.01386 | 2024-10-15 01:56:00 | TERRA_M-M | RONDOLÂNDIA | MATO GROSSO | Brasil | 5107578 | 51 | 33 | nan | nan | nan | Amazônia | 6.1 |
| 623cded7-da1a-324d-9484-f164197fff3e | -10.0352 | -47.3286 | 2024-10-15 01:56:02 | GOES-16 | RIO SONO | TOCANTINS | Brasil | 1718758 | 17 | 33 | nan | nan | nan | Cerrado | 65.7 |
| af05d51f-5400-3c39-9dc0-71d93555f2e1 | -10.0355 | -47.3064 | 2024-10-15 01:56:02 | GOES-16 | RIO SONO | TOCANTINS | Brasil | 1718758 | 17 | 33 | nan | nan | nan | Cerrado | 66.0 |
| 87f6eb9c-62f2-3ddd-a81d-416a95dd5c16 | -10.4918 | -42.433 | 2024-10-15 01:56:05 | GOES-16 | XIQUE-XIQUE | BAHIA | Brasil | 2933604 | 29 | 33 | nan | nan | nan | Caatinga | 67.5 |
| 411545fd-fbea-33f4-9746-6ca33e1fd839 | -10.3524 | -61.1946 | 2024-10-15 01:56:05 | GOES-16 | RONDOLÂNDIA | MATO GROSSO | Brasil | 5107578 | 51 | 33 | nan | nan | nan | Amazônia | 71.4 |
| 8a139495-93d1-37ba-80d0-dddf171fa4f3 | -10.3711 | -61.1935 | 2024-10-15 01:56:05 | GOES-16 | RONDOLÂNDIA | MATO GROSSO | Brasil | 5107578 | 51 | 33 | nan | nan | nan | Amazônia | 139.2 |
| 52172c68-afe3-3154-a7e6-59fabef7c31e | -10.3713 | -61.1743 | 2024-10-15 01:56:05 | GOES-16 | RONDOLÂNDIA | MATO GROSSO | Brasil | 5107578 | 51 | 33 | nan | nan | nan | Amazônia | 87.3 |
| 0addcfca-6781-3201-a5ec-b55b4b20fedb | -13.1474 | -62.3013 | 2024-10-15 01:56:06 | METOP-C | ALTO ALEGRE DOS PARECIS | RONDÔNIA | Brasil | 1100379 | 11 | 33 | nan | nan | nan | Amazônia | nan |
| 3b5bbd42-66dd-3712-abe2-539cb2b25bf6 | -13.1358 | -62.296001 | 2024-10-15 01:56:06 | METOP-C | ALTO ALEGRE DOS PARECIS | RONDÔNIA | Brasil | 1100379 | 11 | 33 | nan | nan | nan | Amazônia | nan |
| 4be667b7-f754-3b50-b5c0-75ef6002df7d | -13.1376 | -62.3036 | 2024-10-15 01:56:06 | METOP-C | ALTO ALEGRE DOS PARECIS | RONDÔNIA | Brasil | 1100379 | 11 | 33 | nan | nan | nan | Amazônia | nan |
| 19f5debe-64df-31ca-abcb-644b2c222027 | -13.143 | -62.326401 | 2024-10-15 01:56:06 | METOP-C | ALTO ALEGRE DOS PARECIS | RONDÔNIA | Brasil | 1100379 | 11 | 33 | nan | nan | nan | Amazônia | nan |
| b77acf5a-4d36-3633-a15e-36280439696b | -13.1279 | -62.306 | 2024-10-15 01:56:06 | METOP-C | ALTO ALEGRE DOS PARECIS | RONDÔNIA | Brasil | 1100379 | 11 | 33 | nan | nan | nan | Amazônia | nan |
| 8424dda0-dbe6-3c29-b6dc-34f72fba7d26 | -13.1297 | -62.313599 | 2024-10-15 01:56:06 | METOP-C | ALTO ALEGRE DOS PARECIS | RONDÔNIA | Brasil | 1100379 | 11 | 33 | nan | nan | nan | Amazônia | nan |
| 8254f199-a602-3f83-b0b4-c7e89bd7523b | -10.9304 | -54.0741 | 2024-10-15 01:56:08 | METOP-C | MARCELÂNDIA | MATO GROSSO | Brasil | 5105580 | 51 | 33 | nan | nan | nan | Amazônia | nan |
| d3474b93-23ad-36cb-a76d-3a93d91abd6b | -10.9373 | -54.099602 | 2024-10-15 01:56:08 | METOP-C | MARCELÂNDIA | MATO GROSSO | Brasil | 5105580 | 51 | 33 | nan | nan | nan | Amazônia | nan |
| 54147195-0ee4-398c-a48f-091b2b72d221 | -12.9809 | -62.737598 | 2024-10-15 01:56:10 | METOP-C | ALTA FLORESTA D'OESTE | RONDÔNIA | Brasil | 1100015 | 11 | 33 | nan | nan | nan | Amazônia | nan |
| 0883f8d4-5794-38f2-bb1f-b7fd346207ba | -12.9699 | -62.779202 | 2024-10-15 01:56:10 | METOP-C | ALTA FLORESTA D'OESTE | RONDÔNIA | Brasil | 1100015 | 11 | 33 | nan | nan | nan | Amazônia | nan |
| 9bd6c638-57a4-33bd-8dc0-090624040fe1 | -12.9734 | -62.793999 | 2024-10-15 01:56:10 | METOP-C | ALTA FLORESTA D'OESTE | RONDÔNIA | Brasil | 1100015 | 11 | 33 | nan | nan | nan | Amazônia | nan |
| 69efec4e-6edb-3172-8ede-56ba5ca489ab | -12.9601 | -62.781502 | 2024-10-15 01:56:10 | METOP-C | ALTA FLORESTA D'OESTE | RONDÔNIA | Brasil | 1100015 | 11 | 33 | nan | nan | nan | Amazônia | nan |
| fd6174f7-0da5-3606-a027-1af4f8ce7403 | -12.9618 | -62.788898 | 2024-10-15 01:56:10 | METOP-C | ALTA FLORESTA D'OESTE | RONDÔNIA | Brasil | 1100015 | 11 | 33 | nan | nan | nan | Amazônia | nan |
| e89a1966-734d-3d85-9b3b-fbcfc009d229 | -12.9636 | -62.796299 | 2024-10-15 01:56:10 | METOP-C | ALTA FLORESTA D'OESTE | RONDÔNIA | Brasil | 1100015 | 11 | 33 | nan | nan | nan | Amazônia | nan |
| 2ed6783c-3758-3a90-8a89-484708b23615 | -12.7703 | -62.279202 | 2024-10-15 01:56:12 | METOP-C | ALTA FLORESTA D'OESTE | RONDÔNIA | Brasil | 1100015 | 11 | 33 | nan | nan | nan | Amazônia | nan |
| 96808a94-6615-3c20-b1d8-ad293cf46e53 | -12.7721 | -62.2869 | 2024-10-15 01:56:12 | METOP-C | ALTA FLORESTA D'OESTE | RONDÔNIA | Brasil | 1100015 | 11 | 33 | nan | nan | nan | Amazônia | nan |
| 44ec0f54-1cc3-336b-bef2-eebfed77d5fa | -12.7739 | -62.294601 | 2024-10-15 01:56:12 | METOP-C | ALTA FLORESTA D'OESTE | RONDÔNIA | Brasil | 1100015 | 11 | 33 | nan | nan | nan | Amazônia | nan |
| 4e3daf49-0900-3b3b-a88c-6344f2174c04 | -12.7606 | -62.281601 | 2024-10-15 01:56:12 | METOP-C | ALTA FLORESTA D'OESTE | RONDÔNIA | Brasil | 1100015 | 11 | 33 | nan | nan | nan | Amazônia | nan |
| dd6dda9b-7d8c-3afe-ab1c-af8f1e7500ea | -12.7624 | -62.2892 | 2024-10-15 01:56:12 | METOP-C | ALTA FLORESTA D'OESTE | RONDÔNIA | Brasil | 1100015 | 11 | 33 | nan | nan | nan | Amazônia | nan |
| 7b3546c1-417d-3682-8bcf-6fcb03a853a9 | -12.7052 | -62.221802 | 2024-10-15 01:56:12 | METOP-C | ALTA FLORESTA D'OESTE | RONDÔNIA | Brasil | 1100015 | 11 | 33 | nan | nan | nan | Amazônia | nan |
| 84ae93ea-117a-3920-9ec3-44c8adca7d94 | -12.707 | -62.2295 | 2024-10-15 01:56:12 | METOP-C | ALTA FLORESTA D'OESTE | RONDÔNIA | Brasil | 1100015 | 11 | 33 | nan | nan | nan | Amazônia | nan |
| ae7181f2-e428-3728-b032-366f61f0ad25 | -12.7088 | -62.237202 | 2024-10-15 01:56:12 | METOP-C | ALTA FLORESTA D'OESTE | RONDÔNIA | Brasil | 1100015 | 11 | 33 | nan | nan | nan | Amazônia | nan |
| d4092f7c-e9d1-39b2-a72d-d0a339fa0d76 | -11.6915 | -65.2432 | 2024-10-15 01:56:13 | GOES-16 | GUAJARÁ-MIRIM | RONDÔNIA | Brasil | 1100106 | 11 | 33 | nan | nan | nan | Amazônia | 78.8 |
| b2a2a089-9f6c-3b8b-8a4b-4149b52d1ec5 | -11.6917 | -65.2243 | 2024-10-15 01:56:13 | GOES-16 | GUAJARÁ-MIRIM | RONDÔNIA | Brasil | 1100106 | 11 | 33 | nan | nan | nan | Amazônia | 89.6 |
| 750c054f-1e53-3563-808b-01d68ce3b830 | -12.6954 | -62.224098 | 2024-10-15 01:56:13 | METOP-C | ALTA FLORESTA D'OESTE | RONDÔNIA | Brasil | 1100015 | 11 | 33 | nan | nan | nan | Amazônia | nan |
| 1750f4b3-442e-3889-9f2e-48616fc3e531 | -12.834 | -62.9049 | 2024-10-15 01:56:13 | METOP-C | SÃO FRANCISCO DO GUAPORÉ | RONDÔNIA | Brasil | 1101492 | 11 | 33 | nan | nan | nan | Amazônia | nan |
| fbf5de1f-42c6-3999-9152-77b87c74e803 | -12.8357 | -62.912201 | 2024-10-15 01:56:13 | METOP-C | SÃO FRANCISCO DO GUAPORÉ | RONDÔNIA | Brasil | 1101492 | 11 | 33 | nan | nan | nan | Amazônia | nan |
| 36675aee-c859-3557-8097-4d8ecda9f875 | -12.8216 | -62.9851 | 2024-10-15 01:56:13 | METOP-C | SÃO FRANCISCO DO GUAPORÉ | RONDÔNIA | Brasil | 1101492 | 11 | 33 | nan | nan | nan | Amazônia | nan |
| ef8b2e0e-dd96-3342-b203-6123d611fb3c | -12.8232 | -62.992401 | 2024-10-15 01:56:13 | METOP-C | SÃO FRANCISCO DO GUAPORÉ | RONDÔNIA | Brasil | 1101492 | 11 | 33 | nan | nan | nan | Amazônia | nan |
| 61603487-348a-3901-a6ed-2a94b226f414 | -12.8249 | -62.999599 | 2024-10-15 01:56:13 | METOP-C | SÃO FRANCISCO DO GUAPORÉ | RONDÔNIA | Brasil | 1101492 | 11 | 33 | nan | nan | nan | Amazônia | nan |
| 37dbfc0d-ba33-31ff-91c3-29d539286028 | -12.099 | -50.2728 | 2024-10-15 01:56:14 | GOES-16 | FORMOSO DO ARAGUAIA | TOCANTINS | Brasil | 1708205 | 17 | 33 | nan | nan | nan | Cerrado | 104.0 |
| a631f8dd-3f3c-3fd8-b3c9-339182163ad6 | -12.7292 | -63.076199 | 2024-10-15 01:56:15 | METOP-C | SÃO FRANCISCO DO GUAPORÉ | RONDÔNIA | Brasil | 1101492 | 11 | 33 | nan | nan | nan | Amazônia | nan |
| ceebb017-33d5-315c-a26d-2d66da0012e5 | -12.6654 | -63.068401 | 2024-10-15 01:56:16 | METOP-C | SÃO FRANCISCO DO GUAPORÉ | RONDÔNIA | Brasil | 1101492 | 11 | 33 | nan | nan | nan | Amazônia | nan |
| 3b428821-8e50-31ab-a894-0e19ef700bfd | -12.6556 | -63.070702 | 2024-10-15 01:56:16 | METOP-C | SÃO FRANCISCO DO GUAPORÉ | RONDÔNIA | Brasil | 1101492 | 11 | 33 | nan | nan | nan | Amazônia | nan |
| 41391c19-a476-3082-b933-70dc902250c0 | -12.6573 | -63.077999 | 2024-10-15 01:56:16 | METOP-C | SÃO FRANCISCO DO GUAPORÉ | RONDÔNIA | Brasil | 1101492 | 11 | 33 | nan | nan | nan | Amazônia | nan |
| 95309f6e-142e-3a90-bff2-6d90aae20393 | -12.3982 | -63.7284 | 2024-10-15 01:56:17 | GOES-16 | COSTA MARQUES | RONDÔNIA | Brasil | 1100080 | 11 | 33 | nan | nan | nan | Amazônia | 63.3 |
| 92183d6f-7999-319b-9608-5907846874e2 | -12.3983 | -63.7093 | 2024-10-15 01:56:17 | GOES-16 | COSTA MARQUES | RONDÔNIA | Brasil | 1100080 | 11 | 33 | nan | nan | nan | Amazônia | 79.4 |
| 8d8fa78c-5b36-3d06-840d-4dc4b050a789 | -12.4603 | -63.0169 | 2024-10-15 01:56:17 | GOES-16 | SÃO FRANCISCO DO GUAPORÉ | RONDÔNIA | Brasil | 1101492 | 11 | 33 | nan | nan | nan | Amazônia | 73.4 |
| 36e0f4c1-95d6-30d9-acaf-fccf4a39dc79 | -12.515 | -63.263 | 2024-10-15 01:56:17 | GOES-16 | SÃO FRANCISCO DO GUAPORÉ | RONDÔNIA | Brasil | 1101492 | 11 | 33 | nan | nan | nan | Amazônia | 95.6 |
| ffd8a641-41b3-3d9e-9b8f-225a795c0c15 | -12.5047 | -62.998699 | 2024-10-15 01:56:19 | METOP-C | SÃO FRANCISCO DO GUAPORÉ | RONDÔNIA | Brasil | 1101492 | 11 | 33 | nan | nan | nan | Amazônia | nan |
| b82c3518-01bf-333b-993b-323db31db97d | -12.4966 | -63.0084 | 2024-10-15 01:56:19 | METOP-C | SÃO FRANCISCO DO GUAPORÉ | RONDÔNIA | Brasil | 1101492 | 11 | 33 | nan | nan | nan | Amazônia | nan |
| 9fd08c8d-44dd-345b-b5aa-238e7b77132b | -12.4983 | -63.015701 | 2024-10-15 01:56:19 | METOP-C | SÃO FRANCISCO DO GUAPORÉ | RONDÔNIA | Brasil | 1101492 | 11 | 33 | nan | nan | nan | Amazônia | nan |
| 4c829e29-3406-33d0-aa14-5a902618d1a4 | -12.4818 | -62.988701 | 2024-10-15 01:56:19 | METOP-C | SÃO FRANCISCO DO GUAPORÉ | RONDÔNIA | Brasil | 1101492 | 11 | 33 | nan | nan | nan | Amazônia | nan |
| fb9ba3ef-199d-3908-989a-7aedb9066dea | -12.4686 | -62.976398 | 2024-10-15 01:56:19 | METOP-C | SÃO FRANCISCO DO GUAPORÉ | RONDÔNIA | Brasil | 1101492 | 11 | 33 | nan | nan | nan | Amazônia | nan |
| 80a2823a-b6a7-3828-a20b-255458661415 | -12.4571 | -62.971401 | 2024-10-15 01:56:19 | METOP-C | SÃO FRANCISCO DO GUAPORÉ | RONDÔNIA | Brasil | 1101492 | 11 | 33 | nan | nan | nan | Amazônia | nan |
| 5f6dd039-0830-3bef-8c46-9b5ce895e89b | -12.4588 | -62.978699 | 2024-10-15 01:56:19 | METOP-C | SÃO FRANCISCO DO GUAPORÉ | RONDÔNIA | Brasil | 1101492 | 11 | 33 | nan | nan | nan | Amazônia | nan |
| 25ceaed7-2e9d-3638-8e7e-10e91f753367 | -12.4605 | -62.986 | 2024-10-15 01:56:19 | METOP-C | SÃO FRANCISCO DO GUAPORÉ | RONDÔNIA | Brasil | 1101492 | 11 | 33 | nan | nan | nan | Amazônia | nan |
| 295f46e8-ded0-3828-bab0-99768977577f | -12.4558 | -63.010399 | 2024-10-15 01:56:19 | METOP-C | SÃO FRANCISCO DO GUAPORÉ | RONDÔNIA | Brasil | 1101492 | 11 | 33 | nan | nan | nan | Amazônia | nan |
| 225bf199-f8d8-378b-9445-2252c2f2c4d9 | -12.4575 | -63.0177 | 2024-10-15 01:56:19 | METOP-C | SÃO FRANCISCO DO GUAPORÉ | RONDÔNIA | Brasil | 1101492 | 11 | 33 | nan | nan | nan | Amazônia | nan |
| 99406681-faee-3837-9878-1c3797d5747d | -12.4592 | -63.025002 | 2024-10-15 01:56:19 | METOP-C | SÃO FRANCISCO DO GUAPORÉ | RONDÔNIA | Brasil | 1101492 | 11 | 33 | nan | nan | nan | Amazônia | nan |
| 96b9ca57-3a17-3e07-b11b-5e394a479b7c | -12.5114 | -63.250198 | 2024-10-15 01:56:19 | METOP-C | SÃO FRANCISCO DO GUAPORÉ | RONDÔNIA | Brasil | 1101492 | 11 | 33 | nan | nan | nan | Amazônia | nan |
| 2920186a-feec-3791-bfa4-40b92842a126 | -12.5131 | -63.257401 | 2024-10-15 01:56:19 | METOP-C | SÃO FRANCISCO DO GUAPORÉ | RONDÔNIA | Brasil | 1101492 | 11 | 33 | nan | nan | nan | Amazônia | nan |
| e8413fc9-809d-3c0b-9327-9fc252f4243a | -12.5147 | -63.264599 | 2024-10-15 01:56:19 | METOP-C | SÃO FRANCISCO DO GUAPORÉ | RONDÔNIA | Brasil | 1101492 | 11 | 33 | nan | nan | nan | Amazônia | nan |
| ead69c94-1e93-39cc-b170-e5941e2e22fb | -12.5164 | -63.271801 | 2024-10-15 01:56:19 | METOP-C | SÃO FRANCISCO DO GUAPORÉ | RONDÔNIA | Brasil | 1101492 | 11 | 33 | nan | nan | nan | Amazônia | nan |
| 7d18c645-348c-31bf-af93-4f64688fcb40 | -12.9728 | -62.7951 | 2024-10-15 01:56:20 | GOES-16 | ALTA FLORESTA D'OESTE | RONDÔNIA | Brasil | 1100015 | 11 | 33 | nan | nan | nan | Amazônia | 80.3 |
| 03f51535-f849-35c5-95f0-98d92ce8dfd2 | -12.4477 | -63.02 | 2024-10-15 01:56:20 | METOP-C | SÃO FRANCISCO DO GUAPORÉ | RONDÔNIA | Brasil | 1101492 | 11 | 33 | nan | nan | nan | Amazônia | nan |
| ab45fd37-6fd3-3167-bd82-d501cb4f48ce | -12.4494 | -63.027302 | 2024-10-15 01:56:20 | METOP-C | SÃO FRANCISCO DO GUAPORÉ | RONDÔNIA | Brasil | 1101492 | 11 | 33 | nan | nan | nan | Amazônia | nan |
| ea6b537b-91a2-39a2-ae73-ac6618678036 | -12.5016 | -63.252499 | 2024-10-15 01:56:20 | METOP-C | SÃO FRANCISCO DO GUAPORÉ | RONDÔNIA | Brasil | 1101492 | 11 | 33 | nan | nan | nan | Amazônia | nan |
| ab7c03f5-67ca-3a3d-b464-650aafb6c6a8 | -12.5033 | -63.259701 | 2024-10-15 01:56:20 | METOP-C | SÃO FRANCISCO DO GUAPORÉ | RONDÔNIA | Brasil | 1101492 | 11 | 33 | nan | nan | nan | Amazônia | nan |
| ea065568-b90c-3761-b104-2f3e23a2a8b2 | -12.5049 | -63.266899 | 2024-10-15 01:56:20 | METOP-C | SÃO FRANCISCO DO GUAPORÉ | RONDÔNIA | Brasil | 1101492 | 11 | 33 | nan | nan | nan | Amazônia | nan |
| 84286506-7714-35de-a876-5ea92728314f | -12.5066 | -63.274101 | 2024-10-15 01:56:20 | METOP-C | SÃO FRANCISCO DO GUAPORÉ | RONDÔNIA | Brasil | 1101492 | 11 | 33 | nan | nan | nan | Amazônia | nan |
| 4ee4af64-8f97-387b-a8be-e1615274f371 | -13.1285 | -62.3227 | 2024-10-15 01:56:21 | GOES-16 | ALTO ALEGRE DOS PARECIS | RONDÔNIA | Brasil | 1100379 | 11 | 33 | nan | nan | nan | Amazônia | 90.8 |
| 2a1b2143-2822-304f-a219-9110d3bfb2c1 | -13.1287 | -62.3034 | 2024-10-15 01:56:21 | GOES-16 | ALTO ALEGRE DOS PARECIS | RONDÔNIA | Brasil | 1100379 | 11 | 33 | nan | nan | nan | Amazônia | 82.7 |
| bd578eba-07cf-3965-9987-1120bcd0b54f | -13.1473 | -62.3408 | 2024-10-15 01:56:21 | GOES-16 | ALTO ALEGRE DOS PARECIS | RONDÔNIA | Brasil | 1100379 | 11 | 33 | nan | nan | nan | Amazônia | 71.6 |
| b1655af9-14af-3841-9737-dbc7ac420309 | -13.1475 | -62.3215 | 2024-10-15 01:56:21 | GOES-16 | ALTO ALEGRE DOS PARECIS | RONDÔNIA | Brasil | 1100379 | 11 | 33 | nan | nan | nan | Amazônia | 122.4 |
| 8c2f1591-5cc6-36bd-8e26-3fe71381ecb8 | -12.3702 | -62.9533 | 2024-10-15 01:56:21 | METOP-C | SÃO FRANCISCO DO GUAPORÉ | RONDÔNIA | Brasil | 1101492 | 11 | 33 | nan | nan | nan | Amazônia | nan |
| 4ff362fa-7e22-34ba-8749-6e2366bc0149 | -12.3719 | -62.960701 | 2024-10-15 01:56:21 | METOP-C | SÃO FRANCISCO DO GUAPORÉ | RONDÔNIA | Brasil | 1101492 | 11 | 33 | nan | nan | nan | Amazônia | nan |
| 2e1f68d4-7656-3a9e-8124-f3250d687505 | -12.3736 | -62.967999 | 2024-10-15 01:56:21 | METOP-C | SÃO FRANCISCO DO GUAPORÉ | RONDÔNIA | Brasil | 1101492 | 11 | 33 | nan | nan | nan | Amazônia | nan |
| 16b08ee4-a866-30cd-8b59-6275718cf4cc | -12.3754 | -62.9753 | 2024-10-15 01:56:21 | METOP-C | SÃO FRANCISCO DO GUAPORÉ | RONDÔNIA | Brasil | 1101492 | 11 | 33 | nan | nan | nan | Amazônia | nan |
| 1f40e971-da93-3b3d-ac7f-674c70e63acc | -13.888 | -45.8388 | 2024-10-15 01:56:23 | GOES-16 | JABORANDI | BAHIA | Brasil | 2917359 | 29 | 33 | nan | nan | nan | Cerrado | 79.4 |
| 2354f612-6edc-39dc-a588-88b11f93d866 | -12.3884 | -63.701302 | 2024-10-15 01:56:23 | METOP-C | COSTA MARQUES | RONDÔNIA | Brasil | 1100080 | 11 | 33 | nan | nan | nan | Amazônia | nan |
| c83ac6ba-1e02-3525-af2f-66030d469255 | -12.39 | -63.708401 | 2024-10-15 01:56:23 | METOP-C | COSTA MARQUES | RONDÔNIA | Brasil | 1100080 | 11 | 33 | nan | nan | nan | Amazônia | nan |
| 3b2623f2-0359-3e16-81e0-f95a29c48238 | -12.3916 | -63.7155 | 2024-10-15 01:56:23 | METOP-C | COSTA MARQUES | RONDÔNIA | Brasil | 1100080 | 11 | 33 | nan | nan | nan | Amazônia | nan |
| ac5d349b-5085-3685-a829-ad4be08f33f7 | -12.3933 | -63.722599 | 2024-10-15 01:56:23 | METOP-C | COSTA MARQUES | RONDÔNIA | Brasil | 1100080 | 11 | 33 | nan | nan | nan | Amazônia | nan |
| 4cad37c8-889c-3463-ac8e-d8d0b54d5c56 | -12.3818 | -63.7178 | 2024-10-15 01:56:23 | METOP-C | COSTA MARQUES | RONDÔNIA | Brasil | 1100080 | 11 | 33 | nan | nan | nan | Amazônia | nan |
| 3c50dffe-e071-33cf-bb79-c6074c2d3341 | -12.3835 | -63.724899 | 2024-10-15 01:56:23 | METOP-C | COSTA MARQUES | RONDÔNIA | Brasil | 1100080 | 11 | 33 | nan | nan | nan | Amazônia | nan |


[Clique aqui para ver as próximas entradas](README19.md)
