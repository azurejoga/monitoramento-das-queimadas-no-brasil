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

## Dados Diários - Página 53

| ID | Latitude | Longitude | Data/Hora GMT | Satélite | Município | Estado | País | Município ID | Estado ID | País ID | Dias sem Chuva | Precipitação | Risco de Fogo | Bioma | FRP |
|----|----------|-----------|---------------|----------|-----------|--------|------|--------------|-----------|---------|----------------|--------------|----------------|-------|-----|
| a77152e0-a50e-347e-ac30-25d8bc7ed125 | -5.89502 | -57.74926 | 2026-08-29 04:53:00 | NOAA-20 | JACAREACANGA | PARÁ | Brasil | 1503754 | 15 | 33 | nan | nan | nan | Amazônia | 8.0 |
| f114d8c0-2d72-3bd1-9e19-6a5635de734f | -12.79449 | -46.45866 | 2026-08-29 04:53:00 | NOAA-20 | LAVANDEIRA | TOCANTINS | Brasil | 1712157 | 17 | 33 | nan | nan | nan | Cerrado | 1.5 |
| 66e0bd60-dd48-3e29-ada5-e0fe2197962a | -8.823 | -49.64297 | 2026-08-29 04:53:00 | NOAA-20 | SANTA MARIA DAS BARREIRAS | PARÁ | Brasil | 1506583 | 15 | 33 | nan | nan | nan | Amazônia | 2.4 |
| 7ea54a39-5e6f-35bd-a69d-39f890ff4aad | -9.15647 | -49.98154 | 2026-08-29 04:53:00 | NOAA-20 | SANTANA DO ARAGUAIA | PARÁ | Brasil | 1506708 | 15 | 33 | nan | nan | nan | Amazônia | 2.4 |
| ef5061da-7e53-3cfe-aea8-1a7f6f941552 | -13.31823 | -48.19801 | 2026-08-29 04:53:00 | NOAA-20 | MINAÇU | GOIÁS | Brasil | 5213087 | 52 | 33 | nan | nan | nan | Cerrado | 2.2 |
| 66ebb25f-7952-3e45-b738-808bdae8c367 | -7.99876 | -61.41005 | 2026-08-29 04:53:00 | NOAA-20 | MANICORÉ | AMAZONAS | Brasil | 1302702 | 13 | 33 | nan | nan | nan | Amazônia | 1.6 |
| 4ece0d35-4a90-359b-8f25-2c2758670a4b | -10.28863 | -62.82396 | 2026-08-29 04:53:00 | NOAA-20 | CACAULÂNDIA | RONDÔNIA | Brasil | 1100601 | 11 | 33 | nan | nan | nan | Amazônia | 2.3 |
| efc95eea-dde0-3edc-870f-ec3d103780f5 | -11.02891 | -57.22243 | 2026-08-29 04:53:00 | NOAA-20 | JUARA | MATO GROSSO | Brasil | 5105101 | 51 | 33 | nan | nan | nan | Amazônia | 2.6 |
| 04bed0f5-d2ed-399d-8bce-fb46c6ac6af1 | -19.00391 | -47.43953 | 2026-08-29 04:53:00 | NOAA-20 | IRAÍ DE MINAS | MINAS GERAIS | Brasil | 3131604 | 31 | 33 | nan | nan | nan | Cerrado | 2.1 |
| f8110f05-1fe2-369f-9c11-eccd9b448a72 | -7.60466 | -47.29169 | 2026-08-29 04:53:00 | NOAA-20 | CAROLINA | MARANHÃO | Brasil | 2102804 | 21 | 33 | nan | nan | nan | Cerrado | 2.5 |
| 58913b04-9f3c-32b3-b7b7-83140d885a2e | -8.10979 | -51.65658 | 2026-08-29 04:53:00 | NOAA-20 | OURILÂNDIA DO NORTE | PARÁ | Brasil | 1505437 | 15 | 33 | nan | nan | nan | Amazônia | 0.9 |
| 960de9f8-a024-3a2e-a5cc-cb86399eb0b4 | -8.98314 | -50.78775 | 2026-08-29 04:53:00 | NOAA-20 | SANTANA DO ARAGUAIA | PARÁ | Brasil | 1506708 | 15 | 33 | nan | nan | nan | Amazônia | 1.5 |
| f94e063a-904a-360f-837f-fa56a6eabba2 | -10.80969 | -50.64072 | 2026-08-29 04:53:00 | NOAA-20 | LUCIARA | MATO GROSSO | Brasil | 5105309 | 51 | 33 | nan | nan | nan | Cerrado | 1.2 |
| c3ef6964-4c18-3445-a877-1edc6f500647 | -7.1972 | -42.73634 | 2026-08-29 04:53:00 | NOAA-20 | NAZARÉ DO PIAUÍ | PIAUÍ | Brasil | 2206704 | 22 | 33 | nan | nan | nan | Caatinga | 1.5 |
| c135a001-0885-3048-b7a5-953aaf822a95 | -10.05889 | -48.67553 | 2026-08-29 04:53:00 | NOAA-20 | MIRACEMA DO TOCANTINS | TOCANTINS | Brasil | 1713205 | 17 | 33 | nan | nan | nan | Cerrado | 2.4 |
| 42cbac39-f9b7-36f6-8a2b-570556b03ed8 | -11.61618 | -46.7253 | 2026-08-29 04:53:00 | NOAA-20 | DIANÓPOLIS | TOCANTINS | Brasil | 1707009 | 17 | 33 | nan | nan | nan | Cerrado | 0.5 |
| 9d2e699c-2564-30ce-b222-06a1a14076d8 | -11.35536 | -45.1586 | 2026-08-29 04:53:00 | NOAA-20 | FORMOSA DO RIO PRETO | BAHIA | Brasil | 2911105 | 29 | 33 | nan | nan | nan | Cerrado | 2.2 |
| 7070d528-5714-335d-98e1-dfd6ce42b771 | -11.38053 | -45.13339 | 2026-08-29 04:53:00 | NOAA-20 | FORMOSA DO RIO PRETO | BAHIA | Brasil | 2911105 | 29 | 33 | nan | nan | nan | Cerrado | 5.7 |
| 5d54f451-f2cc-3083-97af-bd19cc9a1c01 | -10.48119 | -64.49511 | 2026-08-29 04:53:00 | NOAA-20 | NOVA MAMORÉ | RONDÔNIA | Brasil | 1100338 | 11 | 33 | nan | nan | nan | Amazônia | 18.0 |
| 1abe9e93-348b-33c6-a429-e197de34a05b | -9.86332 | -65.04054 | 2026-08-29 04:53:00 | NOAA-20 | PORTO VELHO | RONDÔNIA | Brasil | 1100205 | 11 | 33 | nan | nan | nan | Amazônia | 3.3 |
| 61984f5c-68a0-3036-ba4c-0b6975326f23 | -10.75334 | -54.04346 | 2026-08-29 04:53:00 | NOAA-20 | MARCELÂNDIA | MATO GROSSO | Brasil | 5105580 | 51 | 33 | nan | nan | nan | Amazônia | 1.6 |
| b797badf-f51c-39fb-a2ec-ae99f3742fed | -8.00785 | -51.8287 | 2026-08-29 04:53:00 | NOAA-20 | OURILÂNDIA DO NORTE | PARÁ | Brasil | 1505437 | 15 | 33 | nan | nan | nan | Amazônia | 1.4 |
| 66e4dad5-c029-377d-b972-ce01fe21c8ae | -6.27269 | -53.14314 | 2026-08-29 04:53:00 | NOAA-20 | SÃO FÉLIX DO XINGU | PARÁ | Brasil | 1507300 | 15 | 33 | nan | nan | nan | Amazônia | 2.0 |
| 8b4ae39f-24f3-3391-8ba7-a86f5e183234 | -10.55551 | -59.62338 | 2026-08-29 04:53:00 | NOAA-20 | ARIPUANÃ | MATO GROSSO | Brasil | 5101407 | 51 | 33 | nan | nan | nan | Amazônia | 1.1 |
| e3c74eda-6950-3e60-bfb8-c2038d42ea8f | -10.54121 | -50.47203 | 2026-08-29 04:53:00 | NOAA-20 | PIUM | TOCANTINS | Brasil | 1717503 | 17 | 33 | nan | nan | nan | Cerrado | 3.7 |
| beabaf5f-0828-329c-8ce6-b80b4677753b | -11.22303 | -54.00253 | 2026-08-29 04:53:00 | NOAA-20 | MARCELÂNDIA | MATO GROSSO | Brasil | 5105580 | 51 | 33 | nan | nan | nan | Amazônia | 1.9 |
| 57431945-7fe8-3301-a08e-48c9aa16b94d | -6.84582 | -59.94154 | 2026-08-29 04:53:00 | NOAA-20 | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 0.8 |
| 7ecf34a3-349a-354e-90fe-903816323783 | -10.46623 | -64.50314 | 2026-08-29 04:53:00 | NOAA-20 | NOVA MAMORÉ | RONDÔNIA | Brasil | 1100338 | 11 | 33 | nan | nan | nan | Amazônia | 8.4 |
| e53aeef4-44c6-32e9-8cb9-2c0ca4075bd5 | -6.76033 | -55.66419 | 2026-08-29 04:53:00 | NOAA-20 | NOVO PROGRESSO | PARÁ | Brasil | 1505031 | 15 | 33 | nan | nan | nan | Amazônia | 2.8 |
| b6ae4254-fb90-3167-9431-15fdd9c9ac67 | -12.36851 | -54.16592 | 2026-08-29 04:53:00 | NOAA-20 | NOVA UBIRATÃ | MATO GROSSO | Brasil | 5106240 | 51 | 33 | nan | nan | nan | Amazônia | 0.6 |
| d08675b3-da1e-33a5-a4e1-beec65e66a4e | -9.15705 | -49.97782 | 2026-08-29 04:53:00 | NOAA-20 | SANTANA DO ARAGUAIA | PARÁ | Brasil | 1506708 | 15 | 33 | nan | nan | nan | Amazônia | 2.4 |
| 73c1b595-e38f-378c-9759-e8d8834508a3 | -6.93692 | -58.9586 | 2026-08-29 04:53:00 | NOAA-20 | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 3.0 |
| 5441a149-235b-3603-b981-ac18c5745361 | -9.25608 | -57.07573 | 2026-08-29 04:53:00 | NOAA-20 | PARANAÍTA | MATO GROSSO | Brasil | 5106299 | 51 | 33 | nan | nan | nan | Amazônia | 2.0 |
| 02f20623-afd2-3678-8e34-cab255d7ae3b | -6.15971 | -57.79154 | 2026-08-29 04:53:00 | NOAA-20 | JACAREACANGA | PARÁ | Brasil | 1503754 | 15 | 33 | nan | nan | nan | Amazônia | 3.5 |
| 10b30bba-17d9-36f1-ae79-9e4212ecfd69 | -10.80587 | -54.02172 | 2026-08-29 04:53:00 | NOAA-20 | MARCELÂNDIA | MATO GROSSO | Brasil | 5105580 | 51 | 33 | nan | nan | nan | Amazônia | 1.7 |
| a9290816-e871-3c2e-a7fe-9ff3bcae642b | -19.28419 | -49.52313 | 2026-08-29 04:53:00 | NOAA-20 | ITUIUTABA | MINAS GERAIS | Brasil | 3134202 | 31 | 33 | nan | nan | nan | Cerrado | 1.9 |
| 10c30cb5-cad2-3cd1-a906-7291823b8567 | -11.19081 | -51.2788 | 2026-08-29 04:53:00 | NOAA-20 | LUCIARA | MATO GROSSO | Brasil | 5105309 | 51 | 33 | nan | nan | nan | Cerrado | 1.6 |
| 8468d51f-2b84-316f-8fdc-1267d3cd67dd | -10.75395 | -54.03973 | 2026-08-29 04:53:00 | NOAA-20 | MARCELÂNDIA | MATO GROSSO | Brasil | 5105580 | 51 | 33 | nan | nan | nan | Amazônia | 3.8 |
| d8e255d1-1a7e-3b16-9f05-f5690ebb6230 | -10.50951 | -59.63565 | 2026-08-29 04:53:00 | NOAA-20 | ARIPUANÃ | MATO GROSSO | Brasil | 5101407 | 51 | 33 | nan | nan | nan | Amazônia | 1.7 |
| cdc89ea4-9da1-3e09-a852-05f1692dd44b | -7.28583 | -49.96104 | 2026-08-29 04:53:00 | NOAA-20 | RIO MARIA | PARÁ | Brasil | 1506161 | 15 | 33 | nan | nan | nan | Amazônia | 1.5 |
| 899f883a-06df-32c2-8a33-552894127f2d | -8.98258 | -50.79131 | 2026-08-29 04:53:00 | NOAA-20 | SANTANA DO ARAGUAIA | PARÁ | Brasil | 1506708 | 15 | 33 | nan | nan | nan | Amazônia | 0.9 |
| 201b4879-0369-3f82-907b-72ed7c5bba6f | -16.68584 | -49.47289 | 2026-08-29 04:53:00 | NOAA-20 | TRINDADE | GOIÁS | Brasil | 5221403 | 52 | 33 | nan | nan | nan | Cerrado | 0.7 |
| bf535ee4-51c4-3f23-a7d3-11ac4afd9d58 | -13.41789 | -51.79964 | 2026-08-29 04:53:00 | NOAA-20 | RIBEIRÃO CASCALHEIRA | MATO GROSSO | Brasil | 5107180 | 51 | 33 | nan | nan | nan | Cerrado | 1.4 |
| e466154d-c51b-3ae0-998f-53d68e796681 | -10.76015 | -54.04459 | 2026-08-29 04:53:00 | NOAA-20 | MARCELÂNDIA | MATO GROSSO | Brasil | 5105580 | 51 | 33 | nan | nan | nan | Amazônia | 2.1 |
| 4bade864-ecf3-3869-81bc-e64f26e0d703 | -10.40636 | -61.1999 | 2026-08-29 04:53:00 | NOAA-20 | RONDOLÂNDIA | MATO GROSSO | Brasil | 5107578 | 51 | 33 | nan | nan | nan | Amazônia | 0.9 |
| 721c2225-b865-3c6c-ba7c-c84c1a0dab66 | -6.7764 | -55.68659 | 2026-08-29 04:53:00 | NOAA-20 | NOVO PROGRESSO | PARÁ | Brasil | 1505031 | 15 | 33 | nan | nan | nan | Amazônia | 1.7 |
| fe122f2e-d8f6-3b9d-9b97-591a9df49382 | -7.66256 | -44.78135 | 2026-08-29 04:53:00 | NOAA-20 | URUÇUÍ | PIAUÍ | Brasil | 2211209 | 22 | 33 | nan | nan | nan | Cerrado | 1.1 |
| 7c13a68c-3486-3035-a088-804debf0e550 | -13.31293 | -48.20718 | 2026-08-29 04:53:00 | NOAA-20 | MINAÇU | GOIÁS | Brasil | 5213087 | 52 | 33 | nan | nan | nan | Cerrado | 2.3 |
| 81778409-970a-3a2f-9a05-718c82a26e9b | -9.86569 | -65.02855 | 2026-08-29 04:53:00 | NOAA-20 | PORTO VELHO | RONDÔNIA | Brasil | 1100205 | 11 | 33 | nan | nan | nan | Amazônia | 1.6 |
| 057b6452-85b6-38ac-9eb4-e0f5edd1f817 | -7.63892 | -55.07662 | 2026-08-29 04:53:00 | NOAA-20 | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 0.7 |
| 3f8216cf-2856-3d58-9059-43dca5454214 | -7.52983 | -61.3701 | 2026-08-29 04:53:00 | NOAA-20 | MANICORÉ | AMAZONAS | Brasil | 1302702 | 13 | 33 | nan | nan | nan | Amazônia | 2.8 |
| 5cfeb9a8-c74c-38fb-967f-ea4485022274 | -6.75952 | -55.66902 | 2026-08-29 04:53:00 | NOAA-20 | NOVO PROGRESSO | PARÁ | Brasil | 1505031 | 15 | 33 | nan | nan | nan | Amazônia | 4.3 |
| adec6524-f6ca-3983-873a-32b2b12769c7 | -11.02894 | -57.21091 | 2026-08-29 04:53:00 | NOAA-20 | JUARA | MATO GROSSO | Brasil | 5105101 | 51 | 33 | nan | nan | nan | Amazônia | 2.6 |
| d5488df1-8c2f-336a-abf6-916542e16d5b | -6.2086 | -55.41917 | 2026-08-29 04:53:00 | NOAA-20 | ITAITUBA | PARÁ | Brasil | 1503606 | 15 | 33 | nan | nan | nan | Amazônia | 2.5 |
| 5005cf4f-4e9f-320e-ac67-05667da07801 | -9.39803 | -55.97463 | 2026-08-29 04:53:00 | NOAA-20 | NOVO PROGRESSO | PARÁ | Brasil | 1505031 | 15 | 33 | nan | nan | nan | Amazônia | 0.5 |
| c9b056b9-142b-3f5e-baff-685be49a14b3 | -7.9494 | -52.44943 | 2026-08-29 04:53:00 | NOAA-20 | SÃO FÉLIX DO XINGU | PARÁ | Brasil | 1507300 | 15 | 33 | nan | nan | nan | Amazônia | 0.9 |
| 0902a7cd-0b6e-314d-941d-cc2d0a4498b6 | -12.21416 | -50.53959 | 2026-08-29 04:53:00 | NOAA-20 | FORMOSO DO ARAGUAIA | TOCANTINS | Brasil | 1708205 | 17 | 33 | nan | nan | nan | Cerrado | 0.7 |
| ffa87a82-b295-37fe-9cfd-fd82713e0fc8 | -11.77101 | -54.51261 | 2026-08-29 04:53:00 | NOAA-20 | UNIÃO DO SUL | MATO GROSSO | Brasil | 5108303 | 51 | 33 | nan | nan | nan | Amazônia | 0.9 |
| 22e941df-a96a-343e-9f16-7ba3af83be4f | -9.48583 | -45.67902 | 2026-08-29 04:53:00 | NOAA-20 | SANTA FILOMENA | PIAUÍ | Brasil | 2209203 | 22 | 33 | nan | nan | nan | Cerrado | 3.2 |
| 7265ffec-706f-3c78-b171-5eb0c94ebbc5 | -11.02402 | -57.23972 | 2026-08-29 04:53:00 | NOAA-20 | JUARA | MATO GROSSO | Brasil | 5105101 | 51 | 33 | nan | nan | nan | Amazônia | 1.4 |
| 8c947aa3-79b9-33b8-8069-8f613d9e0e1c | -10.80632 | -54.02163 | 2026-08-29 04:53:00 | NOAA-20 | MARCELÂNDIA | MATO GROSSO | Brasil | 5105580 | 51 | 33 | nan | nan | nan | Amazônia | 1.1 |
| d1d97e94-1a4f-37e4-a17c-89a443f5bd56 | -9.93737 | -60.43803 | 2026-08-29 04:53:00 | NOAA-20 | ARIPUANÃ | MATO GROSSO | Brasil | 5101407 | 51 | 33 | nan | nan | nan | Amazônia | 1.3 |
| 5e6e8817-f06a-3de8-864d-5da4962be6e9 | -10.50198 | -59.62375 | 2026-08-29 04:53:00 | NOAA-20 | ARIPUANÃ | MATO GROSSO | Brasil | 5101407 | 51 | 33 | nan | nan | nan | Amazônia | 1.4 |
| 2ce4e72b-582c-314b-b3b3-2c48b68bc998 | -6.77721 | -55.68177 | 2026-08-29 04:53:00 | NOAA-20 | NOVO PROGRESSO | PARÁ | Brasil | 1505031 | 15 | 33 | nan | nan | nan | Amazônia | 1.7 |
| 4ad2975c-3165-318f-b2cc-fd11fc8901ac | -8.11255 | -51.66058 | 2026-08-29 04:53:00 | NOAA-20 | OURILÂNDIA DO NORTE | PARÁ | Brasil | 1505437 | 15 | 33 | nan | nan | nan | Amazônia | 0.9 |
| 329effc0-9ba4-3601-a3cb-1528ab25883b | -10.89852 | -46.61701 | 2026-08-29 04:53:00 | NOAA-20 | MATEIROS | TOCANTINS | Brasil | 1712702 | 17 | 33 | nan | nan | nan | Cerrado | 1.5 |
| e1dcc3c4-5573-3c76-a7ab-579db597387b | -10.51136 | -59.62563 | 2026-08-29 04:53:00 | NOAA-20 | ARIPUANÃ | MATO GROSSO | Brasil | 5101407 | 51 | 33 | nan | nan | nan | Amazônia | 1.8 |
| 3705b3df-f5e4-3914-a61e-95cbaec7ebdd | -17.57426 | -51.64207 | 2026-08-29 04:53:00 | NOAA-20 | RIO VERDE | GOIÁS | Brasil | 5218805 | 52 | 33 | nan | nan | nan | Cerrado | 0.9 |
| 865db032-5e59-395d-aca8-3fe47c5fd569 | -10.80308 | -54.0174 | 2026-08-29 04:53:00 | NOAA-20 | MARCELÂNDIA | MATO GROSSO | Brasil | 5105580 | 51 | 33 | nan | nan | nan | Amazônia | 1.0 |
| 680b95b7-1c7b-325d-9150-26440cbe89d4 | -6.83909 | -59.94985 | 2026-08-29 04:53:00 | NOAA-20 | NOVO ARIPUANÃ | AMAZONAS | Brasil | 1303304 | 13 | 33 | nan | nan | nan | Amazônia | 1.0 |
| ec8df3b2-eb7d-3600-a356-2249f14927e3 | -6.16252 | -57.78869 | 2026-08-29 04:53:00 | NOAA-20 | JACAREACANGA | PARÁ | Brasil | 1503754 | 15 | 33 | nan | nan | nan | Amazônia | 2.3 |
| ab60d37d-6908-3a33-be73-d8d5efe7dd29 | -9.92402 | -60.42611 | 2026-08-29 04:53:00 | NOAA-20 | ARIPUANÃ | MATO GROSSO | Brasil | 5101407 | 51 | 33 | nan | nan | nan | Amazônia | 0.9 |
| 1c136226-8b45-30de-93a0-469938c5d3a5 | -11.02401 | -57.22692 | 2026-08-29 04:53:00 | NOAA-20 | JUARA | MATO GROSSO | Brasil | 5105101 | 51 | 33 | nan | nan | nan | Amazônia | 2.6 |
| ec372024-730e-343e-bb49-4ab68defec65 | -11.26087 | -54.0317 | 2026-08-29 04:53:00 | NOAA-20 | UNIÃO DO SUL | MATO GROSSO | Brasil | 5108303 | 51 | 33 | nan | nan | nan | Amazônia | 1.1 |
| 615b38d8-3bfb-3a13-a5c1-c732e5063ce9 | -11.03331 | -57.24391 | 2026-08-29 04:53:00 | NOAA-20 | JUARA | MATO GROSSO | Brasil | 5105101 | 51 | 33 | nan | nan | nan | Amazônia | 2.6 |
| 88b761c7-e973-31cb-9ba5-4eb4c39ad5c9 | -17.24547 | -46.92323 | 2026-08-29 04:53:00 | NOAA-20 | PARACATU | MINAS GERAIS | Brasil | 3147006 | 31 | 33 | nan | nan | nan | Cerrado | 1.0 |
| 2825a1f6-de50-313d-a400-9a8f5204be67 | -7.51085 | -55.30758 | 2026-08-29 04:53:00 | NOAA-20 | NOVO PROGRESSO | PARÁ | Brasil | 1505031 | 15 | 33 | nan | nan | nan | Amazônia | 16.4 |
| c959a555-6db8-3ce5-987e-1bc583d2f5af | -6.17693 | -55.46798 | 2026-08-29 04:53:00 | NOAA-20 | ITAITUBA | PARÁ | Brasil | 1503606 | 15 | 33 | nan | nan | nan | Amazônia | 2.0 |
| db9be4f7-7755-3830-98bb-815d708b659d | -11.19032 | -55.10473 | 2026-08-29 04:53:00 | NOAA-20 | ITAÚBA | MATO GROSSO | Brasil | 5104559 | 51 | 33 | nan | nan | nan | Amazônia | 1.7 |
| 8307f78a-5be0-3784-ac32-f5bf281a6f94 | -8.1131 | -51.65711 | 2026-08-29 04:53:00 | NOAA-20 | OURILÂNDIA DO NORTE | PARÁ | Brasil | 1505437 | 15 | 33 | nan | nan | nan | Amazônia | 0.9 |
| d4d5a487-7c59-3aa3-bf0d-2e513dd23166 | -7.55294 | -61.30566 | 2026-08-29 04:53:00 | NOAA-20 | MANICORÉ | AMAZONAS | Brasil | 1302702 | 13 | 33 | nan | nan | nan | Amazônia | 3.0 |
| abfa755c-afe8-3ac6-81d1-d570a971bc1e | -6.49013 | -49.90153 | 2026-08-29 04:53:00 | NOAA-20 | CANAÃ DOS CARAJÁS | PARÁ | Brasil | 1502152 | 15 | 33 | nan | nan | nan | Amazônia | 1.9 |
| fb0e7bcf-659f-3917-ae7e-366c98c80a77 | -9.39888 | -51.62362 | 2026-08-29 04:53:00 | NOAA-20 | SÃO FÉLIX DO XINGU | PARÁ | Brasil | 1507300 | 15 | 33 | nan | nan | nan | Amazônia | 2.0 |
| 5cfefd28-c1da-3e69-81a2-c9af95173545 | -9.92737 | -60.43597 | 2026-08-29 04:53:00 | NOAA-20 | ARIPUANÃ | MATO GROSSO | Brasil | 5101407 | 51 | 33 | nan | nan | nan | Amazônia | 1.7 |
| 56b3b798-29f4-3953-b6dd-00727563a466 | -11.2384 | -53.99377 | 2026-08-29 04:53:00 | NOAA-20 | MARCELÂNDIA | MATO GROSSO | Brasil | 5105580 | 51 | 33 | nan | nan | nan | Amazônia | 1.0 |
| 5cde1dcb-5d9e-3450-ad48-34d97d32d81c | -8.98592 | -50.79184 | 2026-08-29 04:53:00 | NOAA-20 | SANTANA DO ARAGUAIA | PARÁ | Brasil | 1506708 | 15 | 33 | nan | nan | nan | Amazônia | 3.4 |
| 01539534-359a-34b6-b3df-f95b4bcb3f99 | -7.50338 | -55.3063 | 2026-08-29 04:53:00 | NOAA-20 | NOVO PROGRESSO | PARÁ | Brasil | 1505031 | 15 | 33 | nan | nan | nan | Amazônia | 23.9 |
| 19b8b9ef-ef67-3a3a-a033-249b78e92c67 | -17.59501 | -51.61199 | 2026-08-29 04:53:00 | NOAA-20 | RIO VERDE | GOIÁS | Brasil | 5218805 | 52 | 33 | nan | nan | nan | Cerrado | 2.6 |
| efbec5fd-75d7-30db-8291-395182863742 | -6.02515 | -57.70116 | 2026-08-29 04:53:00 | NOAA-20 | JACAREACANGA | PARÁ | Brasil | 1503754 | 15 | 33 | nan | nan | nan | Amazônia | 1.8 |
| 30216acd-fb48-361d-bec2-529a7075c34e | -11.22921 | -54.0074 | 2026-08-29 04:53:00 | NOAA-20 | MARCELÂNDIA | MATO GROSSO | Brasil | 5105580 | 51 | 33 | nan | nan | nan | Amazônia | 1.0 |
| 30e6e36d-0136-3792-b032-777b2659a372 | -11.26705 | -54.03654 | 2026-08-29 04:53:00 | NOAA-20 | UNIÃO DO SUL | MATO GROSSO | Brasil | 5108303 | 51 | 33 | nan | nan | nan | Amazônia | 1.3 |
| 5154c7c4-ede2-31b4-84c3-b70ff067d206 | -11.35936 | -45.16402 | 2026-08-29 04:53:00 | NOAA-20 | FORMOSA DO RIO PRETO | BAHIA | Brasil | 2911105 | 29 | 33 | nan | nan | nan | Cerrado | 0.9 |
| 5450c6f9-2131-327e-8c8d-e0ac1a28782e | -11.28063 | -54.0388 | 2026-08-29 04:53:00 | NOAA-20 | UNIÃO DO SUL | MATO GROSSO | Brasil | 5108303 | 51 | 33 | nan | nan | nan | Amazônia | 1.4 |
| e937e016-3e99-35ca-b168-27efcc2d49c0 | -9.23037 | -51.57209 | 2026-08-29 04:53:00 | NOAA-20 | SÃO FÉLIX DO XINGU | PARÁ | Brasil | 1507300 | 15 | 33 | nan | nan | nan | Amazônia | 1.8 |
| ddc4ed0f-1a7e-3662-a4e3-040afd4ceb2d | -15.57224 | -56.28491 | 2026-08-29 04:53:00 | NOAA-20 | VÁRZEA GRANDE | MATO GROSSO | Brasil | 5108402 | 51 | 33 | nan | nan | nan | Cerrado | 2.6 |
| e8ab6c40-738a-3d7b-b64d-90a8cfe01943 | -8.1554 | -64.00437 | 2026-08-29 04:53:00 | NOAA-20 | CANUTAMA | AMAZONAS | Brasil | 1300904 | 13 | 33 | nan | nan | nan | Amazônia | 1.5 |
| 232d0ec9-506d-37e0-bbdd-8033ab17d8e8 | -7.50413 | -55.30178 | 2026-08-29 04:53:00 | NOAA-20 | NOVO PROGRESSO | PARÁ | Brasil | 1505031 | 15 | 33 | nan | nan | nan | Amazônia | 23.9 |
| f9dafac2-12b2-3b6e-8db1-bbc3675a0385 | -19.28419 | -49.52105 | 2026-08-29 04:53:00 | NOAA-20 | ITUIUTABA | MINAS GERAIS | Brasil | 3134202 | 31 | 33 | nan | nan | nan | Cerrado | 3.1 |
| 037299d7-4906-3e0f-9646-774cc7eb95f4 | -6.9553 | -59.48677 | 2026-08-29 04:53:00 | NOAA-20 | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 2.3 |
| 3f9ca623-2382-33d4-b06f-8cfb403657a7 | -6.82207 | -59.57392 | 2026-08-29 04:53:00 | NOAA-20 | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 0.4 |


[Clique aqui para ver as próximas entradas](README54.md)
