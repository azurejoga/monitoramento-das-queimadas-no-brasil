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

## Dados Diários - Página 44

| ID | Latitude | Longitude | Data/Hora GMT | Satélite | Município | Estado | País | Município ID | Estado ID | País ID | Dias sem Chuva | Precipitação | Risco de Fogo | Bioma | FRP |
|----|----------|-----------|---------------|----------|-----------|--------|------|--------------|-----------|---------|----------------|--------------|----------------|-------|-----|
| 25c3fcf0-23b7-3f65-9f86-c769172c80df | -12.97762 | -54.80004 | 2025-09-05 04:57:00 | NOAA-20 | NOVA UBIRATÃ | MATO GROSSO | Brasil | 5106240 | 51 | 33 | nan | nan | nan | Amazônia | 2.1 |
| 77f0c429-a18c-3bea-9474-8eea7b131e91 | -5.48454 | -60.12662 | 2025-09-05 04:57:00 | NOAA-20 | NOVO ARIPUANÃ | AMAZONAS | Brasil | 1303304 | 13 | 33 | nan | nan | nan | Amazônia | 0.7 |
| d6d7c324-bd91-3250-8bd3-7fc87d9d4446 | -8.09693 | -45.35125 | 2025-09-05 04:57:00 | NOAA-20 | BAIXA GRANDE DO RIBEIRO | PIAUÍ | Brasil | 2201150 | 22 | 33 | nan | nan | nan | Cerrado | 2.8 |
| e0c644ce-b25d-3e22-a0cd-a99955383dd0 | -8.18279 | -61.19627 | 2025-09-05 04:57:00 | NOAA-20 | MANICORÉ | AMAZONAS | Brasil | 1302702 | 13 | 33 | nan | nan | nan | Amazônia | 0.7 |
| 79085d30-666d-31c5-aaa6-f8ee97db542a | -6.333 | -58.17779 | 2025-09-05 04:57:00 | NOAA-20 | JACAREACANGA | PARÁ | Brasil | 1503754 | 15 | 33 | nan | nan | nan | Amazônia | 0.9 |
| d4860015-800d-3aca-b9d1-66d7fa971a8f | -7.97009 | -44.52961 | 2025-09-05 04:57:00 | NOAA-20 | URUÇUÍ | PIAUÍ | Brasil | 2211209 | 22 | 33 | nan | nan | nan | Cerrado | 1.7 |
| a3219b4d-1a25-34b3-9350-e733406d66ec | -13.55522 | -48.13271 | 2025-09-05 04:57:00 | NOAA-20 | MINAÇU | GOIÁS | Brasil | 5213087 | 52 | 33 | nan | nan | nan | Cerrado | 2.0 |
| d92ad90d-eb8d-386e-9066-6f027ac038d8 | -12.50689 | -53.83976 | 2025-09-05 04:57:00 | NOAA-20 | PARANATINGA | MATO GROSSO | Brasil | 5106307 | 51 | 33 | nan | nan | nan | Amazônia | 1.6 |
| 283f1bcf-9b27-3c10-a0cd-0f6157bd4fa9 | -10.13664 | -54.9982 | 2025-09-05 04:57:00 | NOAA-20 | PEIXOTO DE AZEVEDO | MATO GROSSO | Brasil | 5106422 | 51 | 33 | nan | nan | nan | Amazônia | 0.7 |
| 5e21db1b-7a1c-3099-ae18-731801a14968 | -10.47878 | -53.64549 | 2025-09-05 04:57:00 | NOAA-20 | PEIXOTO DE AZEVEDO | MATO GROSSO | Brasil | 5106422 | 51 | 33 | nan | nan | nan | Amazônia | 1.2 |
| b0a6aaf1-773b-3443-84c7-79fa35270e09 | -10.30522 | -46.35051 | 2025-09-05 04:57:00 | NOAA-20 | MATEIROS | TOCANTINS | Brasil | 1712702 | 17 | 33 | nan | nan | nan | Cerrado | 0.6 |
| bc4ea7cc-703c-317f-9eae-a8949481d34a | -12.87925 | -48.01172 | 2025-09-05 04:57:00 | NOAA-20 | PARANÃ | TOCANTINS | Brasil | 1716208 | 17 | 33 | nan | nan | nan | Cerrado | 3.8 |
| fbd9fb22-b627-30dc-9fad-e08c6ec459b2 | -5.90752 | -57.72418 | 2025-09-05 04:57:00 | NOAA-20 | JACAREACANGA | PARÁ | Brasil | 1503754 | 15 | 33 | nan | nan | nan | Amazônia | 4.1 |
| bfb02f08-08ef-3ee2-bb91-6c019e80f558 | -11.60312 | -52.17107 | 2025-09-05 04:57:00 | NOAA-20 | SÃO FÉLIX DO ARAGUAIA | MATO GROSSO | Brasil | 5107859 | 51 | 33 | nan | nan | nan | Amazônia | 3.9 |
| 0b061ec0-6f58-3906-b124-5eca86810dcd | -11.98865 | -46.75888 | 2025-09-05 04:57:00 | NOAA-20 | DIANÓPOLIS | TOCANTINS | Brasil | 1707009 | 17 | 33 | nan | nan | nan | Cerrado | 1.8 |
| 2bae7ddc-77f8-3ae9-89a8-0cc4cf46a99c | -6.84384 | -52.80157 | 2025-09-05 04:57:00 | NOAA-20 | SÃO FÉLIX DO XINGU | PARÁ | Brasil | 1507300 | 15 | 33 | nan | nan | nan | Amazônia | 1.0 |
| 40f396fa-1286-3779-ba8b-fc8e63618e84 | -10.52982 | -57.77899 | 2025-09-05 04:57:00 | NOAA-20 | JUARA | MATO GROSSO | Brasil | 5105101 | 51 | 33 | nan | nan | nan | Amazônia | 1.1 |
| bd0e3148-78ab-3b0c-80bf-298778bcf71e | -8.06568 | -52.36937 | 2025-09-05 04:57:00 | NOAA-20 | SÃO FÉLIX DO XINGU | PARÁ | Brasil | 1507300 | 15 | 33 | nan | nan | nan | Amazônia | 3.7 |
| 040ccbdf-635f-3b96-8072-5bce8508596a | -12.49895 | -53.84618 | 2025-09-05 04:57:00 | NOAA-20 | PARANATINGA | MATO GROSSO | Brasil | 5106307 | 51 | 33 | nan | nan | nan | Amazônia | 1.5 |
| 966e05b9-fa4b-3610-b2a0-e4f1db5601fb | -11.44938 | -57.81016 | 2025-09-05 04:57:00 | NOAA-20 | JUARA | MATO GROSSO | Brasil | 5105101 | 51 | 33 | nan | nan | nan | Amazônia | 0.7 |
| fc4b7324-82c2-33d2-976e-106a070794ec | -12.96185 | -54.79779 | 2025-09-05 04:57:00 | NOAA-20 | NOVA UBIRATÃ | MATO GROSSO | Brasil | 5106240 | 51 | 33 | nan | nan | nan | Amazônia | 15.0 |
| c80cc2ee-f3ad-3090-b699-13508d2725cb | -12.87368 | -48.01711 | 2025-09-05 04:57:00 | NOAA-20 | PARANÃ | TOCANTINS | Brasil | 1716208 | 17 | 33 | nan | nan | nan | Cerrado | 2.9 |
| 2be094c4-d56b-3658-9de7-b1504c4e7cfc | -11.48847 | -55.51415 | 2025-09-05 04:57:00 | NOAA-20 | SINOP | MATO GROSSO | Brasil | 5107909 | 51 | 33 | nan | nan | nan | Amazônia | 2.5 |
| 2afabaf3-3e48-392d-a4f5-d0493ad01a8f | -12.8854 | -56.95144 | 2025-09-05 04:57:00 | NOAA-20 | NOVA MARINGÁ | MATO GROSSO | Brasil | 5108907 | 51 | 33 | nan | nan | nan | Amazônia | 2.7 |
| ea07e836-1576-3363-9abd-876a84e1d733 | -12.96778 | -48.08228 | 2025-09-05 04:57:00 | NOAA-20 | PARANÃ | TOCANTINS | Brasil | 1716208 | 17 | 33 | nan | nan | nan | Cerrado | 2.9 |
| aa790d63-68f5-3ce7-9c33-3a577e8d161e | -12.97149 | -54.79539 | 2025-09-05 04:57:00 | NOAA-20 | NOVA UBIRATÃ | MATO GROSSO | Brasil | 5106240 | 51 | 33 | nan | nan | nan | Amazônia | 3.7 |
| bb30f882-d9e9-3f93-aafc-710355aab00e | -7.89892 | -45.23482 | 2025-09-05 04:57:00 | NOAA-20 | BAIXA GRANDE DO RIBEIRO | PIAUÍ | Brasil | 2201150 | 22 | 33 | nan | nan | nan | Cerrado | 1.8 |
| 3d2d8a73-564c-3d2b-a9f6-4f5b02ee6385 | -8.09738 | -45.3479 | 2025-09-05 04:57:00 | NOAA-20 | BAIXA GRANDE DO RIBEIRO | PIAUÍ | Brasil | 2201150 | 22 | 33 | nan | nan | nan | Cerrado | 2.8 |
| fae21459-eef2-3311-bf53-2e5ec8b2ef9f | -14.28217 | -45.22423 | 2025-09-05 04:57:00 | NOAA-20 | COCOS | BAHIA | Brasil | 2908101 | 29 | 33 | nan | nan | nan | Cerrado | 5.1 |
| 2e955fd8-ada0-3a04-91cc-51c7b3201629 | -12.88935 | -56.94837 | 2025-09-05 04:57:00 | NOAA-20 | NOVA MARINGÁ | MATO GROSSO | Brasil | 5108907 | 51 | 33 | nan | nan | nan | Amazônia | 1.3 |
| 99dc26a7-b568-36db-a329-c3161cd80394 | -10.98077 | -45.94461 | 2025-09-05 04:57:00 | NOAA-20 | FORMOSA DO RIO PRETO | BAHIA | Brasil | 2911105 | 29 | 33 | nan | nan | nan | Cerrado | 2.2 |
| b69e4ec1-e80e-3db9-809b-3cebe102bd8b | -12.87436 | -48.01173 | 2025-09-05 04:57:00 | NOAA-20 | PARANÃ | TOCANTINS | Brasil | 1716208 | 17 | 33 | nan | nan | nan | Cerrado | 2.9 |
| 0d44c2fb-e152-3dd1-9c55-9042ac40f2a5 | -12.27485 | -50.15623 | 2025-09-05 04:57:00 | NOAA-20 | FORMOSO DO ARAGUAIA | TOCANTINS | Brasil | 1708205 | 17 | 33 | nan | nan | nan | Cerrado | 2.4 |
| 0a9d494f-b31f-39bc-ba53-a1c8e40aaa9d | -8.01873 | -45.4228 | 2025-09-05 04:57:00 | NOAA-20 | RIBEIRO GONÇALVES | PIAUÍ | Brasil | 2208908 | 22 | 33 | nan | nan | nan | Cerrado | 2.0 |
| 174e4ac9-65db-35cb-b320-e1e5400f91ab | -10.0371 | -48.13512 | 2025-09-05 04:57:00 | NOAA-20 | APARECIDA DO RIO NEGRO | TOCANTINS | Brasil | 1701101 | 17 | 33 | nan | nan | nan | Cerrado | 2.0 |
| 97add910-b016-3f1e-a202-c92adb97f7e3 | -6.82187 | -52.80935 | 2025-09-05 04:57:00 | NOAA-20 | SÃO FÉLIX DO XINGU | PARÁ | Brasil | 1507300 | 15 | 33 | nan | nan | nan | Amazônia | 1.2 |
| 020827bf-3895-394b-97ed-4a5c8a6330b8 | -12.263 | -50.15071 | 2025-09-05 04:57:00 | NOAA-20 | FORMOSO DO ARAGUAIA | TOCANTINS | Brasil | 1708205 | 17 | 33 | nan | nan | nan | Cerrado | 1.4 |
| 936ebd84-d2ec-330c-a9f4-9f73826d74ac | -12.96073 | -54.78289 | 2025-09-05 04:57:00 | NOAA-20 | NOVA UBIRATÃ | MATO GROSSO | Brasil | 5106240 | 51 | 33 | nan | nan | nan | Amazônia | 5.4 |
| 60a21d94-9366-386c-a880-6da672e01e4c | -5.86247 | -57.77684 | 2025-09-05 04:57:00 | NOAA-20 | JACAREACANGA | PARÁ | Brasil | 1503754 | 15 | 33 | nan | nan | nan | Amazônia | 1.2 |
| b55c451e-3cc8-37d5-b969-f9cc87b53b3e | -9.32315 | -55.22504 | 2025-09-05 04:57:00 | NOAA-20 | NOVO PROGRESSO | PARÁ | Brasil | 1505031 | 15 | 33 | nan | nan | nan | Amazônia | 0.9 |
| da96e593-bfee-3f10-8865-f98fd9f81e76 | -11.67398 | -57.34328 | 2025-09-05 04:57:00 | NOAA-20 | PORTO DOS GAÚCHOS | MATO GROSSO | Brasil | 5106802 | 51 | 33 | nan | nan | nan | Amazônia | 0.9 |
| b7117471-6309-3cbf-9164-8243aeb1ed36 | -8.36324 | -52.55215 | 2025-09-05 04:57:00 | NOAA-20 | SÃO FÉLIX DO XINGU | PARÁ | Brasil | 1507300 | 15 | 33 | nan | nan | nan | Amazônia | 1.8 |
| 8f81c400-3082-31d6-b08c-da981605f538 | -12.91129 | -57.0044 | 2025-09-05 04:57:00 | NOAA-20 | NOVA MARINGÁ | MATO GROSSO | Brasil | 5108907 | 51 | 33 | nan | nan | nan | Amazônia | 1.5 |
| 7e38c2d4-a0b4-3eff-9399-9127635551dc | -8.89935 | -45.78384 | 2025-09-05 04:57:00 | NOAA-20 | SANTA FILOMENA | PIAUÍ | Brasil | 2209203 | 22 | 33 | nan | nan | nan | Cerrado | 2.2 |
| 04fdd0cf-a285-3fe0-8790-71db996d570b | -5.50685 | -60.12617 | 2025-09-05 04:57:00 | NOAA-20 | NOVO ARIPUANÃ | AMAZONAS | Brasil | 1303304 | 13 | 33 | nan | nan | nan | Amazônia | 7.0 |
| 7006551d-d0af-36a7-9c22-1129a5a4a1d1 | -6.2655 | -53.43987 | 2025-09-05 04:57:00 | NOAA-20 | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 1.9 |
| 5c1329ec-42ab-34d4-9a28-f144668a4521 | -11.64082 | -52.22277 | 2025-09-05 04:57:00 | NOAA-20 | SÃO FÉLIX DO ARAGUAIA | MATO GROSSO | Brasil | 5107859 | 51 | 33 | nan | nan | nan | Amazônia | 3.1 |
| 76472c9a-b3c6-3603-997f-b18387ffacbb | -9.96414 | -51.6411 | 2025-09-05 04:57:00 | NOAA-20 | VILA RICA | MATO GROSSO | Brasil | 5108600 | 51 | 33 | nan | nan | nan | Amazônia | 1.4 |
| 53f2b5c1-bd52-3a05-b961-27bcd076dd52 | -9.71545 | -51.0791 | 2025-09-05 04:57:00 | NOAA-20 | SANTANA DO ARAGUAIA | PARÁ | Brasil | 1506708 | 15 | 33 | nan | nan | nan | Amazônia | 11.2 |
| 06bdda51-a6a0-3324-af96-dae868552490 | -12.97039 | -54.80257 | 2025-09-05 04:57:00 | NOAA-20 | NOVA UBIRATÃ | MATO GROSSO | Brasil | 5106240 | 51 | 33 | nan | nan | nan | Amazônia | 3.8 |
| 1d9d6dad-339f-3dd1-8b7c-8814e737404a | -13.30137 | -46.84921 | 2025-09-05 04:57:00 | NOAA-20 | MONTE ALEGRE DE GOIÁS | GOIÁS | Brasil | 5213509 | 52 | 33 | nan | nan | nan | Cerrado | 1.4 |
| 8663195d-291d-384a-9976-b988e6a42d4a | -8.77744 | -49.62994 | 2025-09-05 04:57:00 | NOAA-20 | CONCEIÇÃO DO ARAGUAIA | PARÁ | Brasil | 1502707 | 15 | 33 | nan | nan | nan | Amazônia | 1.1 |
| aee93a64-567a-35fc-b4bb-0ddbcc3a12d5 | -12.18328 | -53.89783 | 2025-09-05 04:57:00 | NOAA-20 | NOVA UBIRATÃ | MATO GROSSO | Brasil | 5106240 | 51 | 33 | nan | nan | nan | Amazônia | 1.4 |
| f3b6366c-3a42-3e40-b5bb-1ec550e462d1 | -6.97475 | -56.47373 | 2025-09-05 04:57:00 | NOAA-20 | ITAITUBA | PARÁ | Brasil | 1503606 | 15 | 33 | nan | nan | nan | Amazônia | 0.7 |
| 147b797f-81f3-3ad1-aab4-33d8931685e1 | -11.60075 | -52.16204 | 2025-09-05 04:57:00 | NOAA-20 | SÃO FÉLIX DO ARAGUAIA | MATO GROSSO | Brasil | 5107859 | 51 | 33 | nan | nan | nan | Amazônia | 2.9 |
| be4842eb-b415-3433-aec6-a3bd90943610 | -7.88669 | -45.24392 | 2025-09-05 04:57:00 | NOAA-20 | BAIXA GRANDE DO RIBEIRO | PIAUÍ | Brasil | 2201150 | 22 | 33 | nan | nan | nan | Cerrado | 0.6 |
| 92960639-0363-3054-b107-d0d0d0892c2e | -14.04027 | -49.69277 | 2025-09-05 04:57:00 | NOAA-20 | MARA ROSA | GOIÁS | Brasil | 5212808 | 52 | 33 | nan | nan | nan | Cerrado | 2.4 |
| 750fb678-07ad-30a5-acfa-c259c3495246 | -5.50253 | -60.12544 | 2025-09-05 04:57:00 | NOAA-20 | NOVO ARIPUANÃ | AMAZONAS | Brasil | 1303304 | 13 | 33 | nan | nan | nan | Amazônia | 3.7 |
| e807749d-316d-3b55-9a3a-e54d2afaac5c | -7.98362 | -44.51461 | 2025-09-05 04:57:00 | NOAA-20 | URUÇUÍ | PIAUÍ | Brasil | 2211209 | 22 | 33 | nan | nan | nan | Cerrado | 9.4 |
| 495e0c86-e8dd-3599-b9d8-82e34aac95bd | -12.48588 | -53.84029 | 2025-09-05 04:57:00 | NOAA-20 | PARANATINGA | MATO GROSSO | Brasil | 5106307 | 51 | 33 | nan | nan | nan | Amazônia | 1.9 |
| a76461de-43e8-3bcf-ac0b-c70d0bd443bd | -8.5238 | -51.33234 | 2025-09-05 04:57:00 | NOAA-20 | CUMARU DO NORTE | PARÁ | Brasil | 1502764 | 15 | 33 | nan | nan | nan | Amazônia | 2.2 |
| b3a75117-6720-370e-a8cc-cfff7a0270b0 | -5.90014 | -57.72295 | 2025-09-05 04:57:00 | NOAA-20 | JACAREACANGA | PARÁ | Brasil | 1503754 | 15 | 33 | nan | nan | nan | Amazônia | 2.4 |
| 6c329f7e-3c94-39a4-823f-85cebbfa3784 | -12.91143 | -48.02743 | 2025-09-05 04:57:00 | NOAA-20 | PARANÃ | TOCANTINS | Brasil | 1716208 | 17 | 33 | nan | nan | nan | Cerrado | 7.5 |
| ae877538-836e-3aa4-83bd-ec98f52a31e0 | -9.87772 | -46.54856 | 2025-09-05 04:57:00 | NOAA-20 | SÃO FÉLIX DO TOCANTINS | TOCANTINS | Brasil | 1720150 | 17 | 33 | nan | nan | nan | Cerrado | 3.2 |
| 04a455fb-7254-3db3-88a9-f984c643be05 | -12.97872 | -54.79286 | 2025-09-05 04:57:00 | NOAA-20 | NOVA UBIRATÃ | MATO GROSSO | Brasil | 5106240 | 51 | 33 | nan | nan | nan | Amazônia | 1.4 |
| 06b00377-2ad6-3459-a24e-a6872fc82c6c | -9.07573 | -47.01099 | 2025-09-05 04:57:00 | NOAA-20 | BALSAS | MARANHÃO | Brasil | 2101400 | 21 | 33 | nan | nan | nan | Cerrado | 17.3 |
| 281c015c-4399-3664-a910-dc3358b96cc2 | -5.49389 | -60.12395 | 2025-09-05 04:57:00 | NOAA-20 | NOVO ARIPUANÃ | AMAZONAS | Brasil | 1303304 | 13 | 33 | nan | nan | nan | Amazônia | 4.2 |
| 5de24b60-a107-3634-ac9b-7fd151562eb9 | -11.0044 | -45.93074 | 2025-09-05 04:57:00 | NOAA-20 | FORMOSA DO RIO PRETO | BAHIA | Brasil | 2911105 | 29 | 33 | nan | nan | nan | Cerrado | 1.5 |
| b13c2a35-d4b7-32f0-a005-78271d7fb1ab | -9.98377 | -51.63332 | 2025-09-05 04:57:00 | NOAA-20 | VILA RICA | MATO GROSSO | Brasil | 5108600 | 51 | 33 | nan | nan | nan | Amazônia | 2.3 |
| f4ae0187-3ab8-36f6-9a42-744cd5b6a18a | -12.97538 | -54.79233 | 2025-09-05 04:57:00 | NOAA-20 | NOVA UBIRATÃ | MATO GROSSO | Brasil | 5106240 | 51 | 33 | nan | nan | nan | Amazônia | 1.4 |
| ce01dbb3-3fb3-3af0-8412-0c56bb0a3277 | -7.90629 | -44.93003 | 2025-09-05 04:57:00 | NOAA-20 | BAIXA GRANDE DO RIBEIRO | PIAUÍ | Brasil | 2201150 | 22 | 33 | nan | nan | nan | Cerrado | 1.1 |
| de4bca1e-ce4e-35b8-9b76-6d89fb6007cf | -6.27603 | -53.43793 | 2025-09-05 04:57:00 | NOAA-20 | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 1.2 |
| cdb013c8-4408-37c2-b8ff-13871c8da53e | -10.96831 | -45.97841 | 2025-09-05 04:57:00 | NOAA-20 | FORMOSA DO RIO PRETO | BAHIA | Brasil | 2911105 | 29 | 33 | nan | nan | nan | Cerrado | 0.7 |
| d43e3abf-f9ff-32c8-b7f5-297a0714fa3e | -10.97372 | -45.95741 | 2025-09-05 04:57:00 | NOAA-20 | FORMOSA DO RIO PRETO | BAHIA | Brasil | 2911105 | 29 | 33 | nan | nan | nan | Cerrado | 3.2 |
| 259af7f6-b346-3c25-8a72-bfa8536d5605 | -10.50459 | -57.77881 | 2025-09-05 04:57:00 | NOAA-20 | JUARA | MATO GROSSO | Brasil | 5105101 | 51 | 33 | nan | nan | nan | Amazônia | 1.2 |
| 461b1f0b-1b6e-3c24-9344-3898ef9754b6 | -11.64821 | -54.53528 | 2025-09-05 04:57:00 | NOAA-20 | UNIÃO DO SUL | MATO GROSSO | Brasil | 5108303 | 51 | 33 | nan | nan | nan | Amazônia | 3.4 |
| cd42a8b1-652b-3d21-a4f8-567bb010a43b | -7.72593 | -50.31756 | 2025-09-05 04:57:00 | NOAA-20 | PAU D'ARCO | PARÁ | Brasil | 1505551 | 15 | 33 | nan | nan | nan | Amazônia | 3.7 |
| 48ab33f1-98cd-379f-be1a-af2940e73d17 | -10.97232 | -45.98942 | 2025-09-05 04:57:00 | NOAA-20 | FORMOSA DO RIO PRETO | BAHIA | Brasil | 2911105 | 29 | 33 | nan | nan | nan | Cerrado | 1.0 |
| 6c0d34cf-d6ff-3be1-bcbb-197710c0d791 | -12.60673 | -56.99916 | 2025-09-05 04:57:00 | NOAA-20 | NOVA MARINGÁ | MATO GROSSO | Brasil | 5108907 | 51 | 33 | nan | nan | nan | Amazônia | 1.5 |
| 9e8dbad3-833b-3cbe-96ce-b263092588d7 | -12.9624 | -54.7721 | 2025-09-05 04:57:00 | NOAA-20 | NOVA UBIRATÃ | MATO GROSSO | Brasil | 5106240 | 51 | 33 | nan | nan | nan | Amazônia | 1.0 |
| 20425215-1d8c-3ee5-bef6-ad507bf39cc5 | -10.76241 | -48.2968 | 2025-09-05 04:57:00 | NOAA-20 | PORTO NACIONAL | TOCANTINS | Brasil | 1718204 | 17 | 33 | nan | nan | nan | Cerrado | 4.0 |
| e215e9a4-4b84-3132-a342-d8dd1190203d | -9.8173 | -46.65527 | 2025-09-05 04:57:00 | NOAA-20 | LIZARDA | TOCANTINS | Brasil | 1712405 | 17 | 33 | nan | nan | nan | Cerrado | 4.8 |
| 6fa9fb3c-8c4a-396c-b86e-751308f77d6f | -9.43135 | -46.79763 | 2025-09-05 04:57:00 | NOAA-20 | LIZARDA | TOCANTINS | Brasil | 1712405 | 17 | 33 | nan | nan | nan | Cerrado | 1.9 |
| 124194ff-739e-35a9-9bbd-1f15c56c77f7 | -10.13995 | -54.99873 | 2025-09-05 04:57:00 | NOAA-20 | PEIXOTO DE AZEVEDO | MATO GROSSO | Brasil | 5106422 | 51 | 33 | nan | nan | nan | Amazônia | 1.1 |
| cb99f62c-ec8d-387c-8361-b5e0a1ddc080 | -9.96522 | -51.65878 | 2025-09-05 04:57:00 | NOAA-20 | VILA RICA | MATO GROSSO | Brasil | 5108600 | 51 | 33 | nan | nan | nan | Amazônia | 1.6 |
| 74fb9e06-27dc-3980-8889-440bc054f612 | -8.34391 | -48.30553 | 2025-09-05 04:57:00 | NOAA-20 | PRESIDENTE KENNEDY | TOCANTINS | Brasil | 1718402 | 17 | 33 | nan | nan | nan | Cerrado | 5.2 |
| ab9d7e5f-b845-32c9-b881-71ac0b38957c | -12.29763 | -50.02013 | 2025-09-05 04:57:00 | NOAA-20 | SANDOLÂNDIA | TOCANTINS | Brasil | 1718840 | 17 | 33 | nan | nan | nan | Cerrado | 1.4 |
| 80424378-137f-38da-9649-9c8720dc8bfc | -11.39407 | -43.59377 | 2025-09-05 04:57:00 | NOAA-20 | BARRA | BAHIA | Brasil | 2902708 | 29 | 33 | nan | nan | nan | Cerrado | 0.9 |
| 8ef38dcc-336e-3141-a233-be01c1368061 | -11.59824 | -52.17901 | 2025-09-05 04:57:00 | NOAA-20 | SÃO FÉLIX DO ARAGUAIA | MATO GROSSO | Brasil | 5107859 | 51 | 33 | nan | nan | nan | Amazônia | 3.0 |
| 8d77aa37-5e48-308e-a495-155a2f2c3480 | -10.75677 | -45.2654 | 2025-09-05 04:57:00 | NOAA-20 | CRISTALÂNDIA DO PIAUÍ | PIAUÍ | Brasil | 2203008 | 22 | 33 | nan | nan | nan | Cerrado | 1.0 |
| b7486b08-0226-36cc-b6d7-795c2d1398b5 | -12.99545 | -54.8176 | 2025-09-05 04:57:00 | NOAA-20 | NOVA UBIRATÃ | MATO GROSSO | Brasil | 5106240 | 51 | 33 | nan | nan | nan | Amazônia | 6.7 |
| 3333ec5d-4fa8-3e4f-a019-5253f702d074 | -13.09042 | -57.11311 | 2025-09-05 04:57:00 | NOAA-20 | NOVA MARINGÁ | MATO GROSSO | Brasil | 5108907 | 51 | 33 | nan | nan | nan | Amazônia | 1.3 |
| e4fd924e-9ae7-3a95-8ad3-48f9d6b71a96 | -10.23543 | -50.54274 | 2025-09-05 04:57:00 | NOAA-20 | SANTA TEREZINHA | MATO GROSSO | Brasil | 5107776 | 51 | 33 | nan | nan | nan | Amazônia | 1.5 |
| 65cfe0cd-dd35-3ed5-aed7-49701081f046 | -12.83676 | -44.45416 | 2025-09-05 04:57:00 | NOAA-20 | BAIANÓPOLIS | BAHIA | Brasil | 2902500 | 29 | 33 | nan | nan | nan | Cerrado | 1.8 |
| b8b7dd13-6dd4-3ba8-900f-2ad3d71e3382 | -11.00936 | -45.93486 | 2025-09-05 04:57:00 | NOAA-20 | FORMOSA DO RIO PRETO | BAHIA | Brasil | 2911105 | 29 | 33 | nan | nan | nan | Cerrado | 1.5 |
| 68b0569e-fd55-3af2-85a2-afd93ca8e0bc | -5.89941 | -57.72733 | 2025-09-05 04:57:00 | NOAA-20 | JACAREACANGA | PARÁ | Brasil | 1503754 | 15 | 33 | nan | nan | nan | Amazônia | 2.4 |
| e77b4f89-9f06-31aa-82aa-5567f760d440 | -11.99896 | -46.76045 | 2025-09-05 04:57:00 | NOAA-20 | DIANÓPOLIS | TOCANTINS | Brasil | 1707009 | 17 | 33 | nan | nan | nan | Cerrado | 0.5 |
| e134a070-8968-3473-9450-831bf42c4635 | -11.61746 | -52.19917 | 2025-09-05 04:57:00 | NOAA-20 | SÃO FÉLIX DO ARAGUAIA | MATO GROSSO | Brasil | 5107859 | 51 | 33 | nan | nan | nan | Amazônia | 3.5 |
| 47ef13dc-7899-33e3-9112-8a9fdbaf32bd | -11.85923 | -51.45143 | 2025-09-05 04:57:00 | NOAA-20 | ALTO BOA VISTA | MATO GROSSO | Brasil | 5100359 | 51 | 33 | nan | nan | nan | Cerrado | 2.5 |
| 40b1b203-d605-3a63-9a7a-ae6c77ab7ffa | -6.26964 | -53.54416 | 2025-09-05 04:57:00 | NOAA-20 | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 0.5 |


[Clique aqui para ver as próximas entradas](README45.md)
