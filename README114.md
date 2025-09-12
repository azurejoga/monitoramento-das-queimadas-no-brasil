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

## Dados Diários - Página 114

| ID | Latitude | Longitude | Data/Hora GMT | Satélite | Município | Estado | País | Município ID | Estado ID | País ID | Dias sem Chuva | Precipitação | Risco de Fogo | Bioma | FRP |
|----|----------|-----------|---------------|----------|-----------|--------|------|--------------|-----------|---------|----------------|--------------|----------------|-------|-----|
| df3ca101-cda5-368a-8767-5a2d905e16a1 | -14.93505 | -55.95369 | 2025-09-12 05:46:00 | NPP-375D | CHAPADA DOS GUIMARÃES | MATO GROSSO | Brasil | 5103007 | 51 | 33 | nan | nan | nan | Cerrado | 3.5 |
| d9fc9d2c-69c8-38f8-8fe5-99b6245e0801 | -11.18776 | -55.07129 | 2025-09-12 05:46:00 | NPP-375D | ITAÚBA | MATO GROSSO | Brasil | 5104559 | 51 | 33 | nan | nan | nan | Amazônia | 2.0 |
| 2a96e63e-727e-3872-8af1-0ccee15005fc | -11.87161 | -58.82217 | 2025-09-12 05:46:00 | NPP-375D | JUÍNA | MATO GROSSO | Brasil | 5105150 | 51 | 33 | nan | nan | nan | Cerrado | 1.5 |
| d8482736-51a1-37ab-ba89-66a2bdaf3e96 | -11.77823 | -64.92649 | 2025-09-12 05:46:00 | NPP-375D | GUAJARÁ-MIRIM | RONDÔNIA | Brasil | 1100106 | 11 | 33 | nan | nan | nan | Amazônia | 0.7 |
| b4f0dd8a-6b94-3c52-892d-90d61deefd3b | -9.42196 | -58.98965 | 2025-09-12 05:46:00 | NPP-375D | COLNIZA | MATO GROSSO | Brasil | 5103254 | 51 | 33 | nan | nan | nan | Amazônia | 0.8 |
| 0658893a-4616-3c74-99fa-f8c1d7a1959e | -11.10516 | -68.69378 | 2025-09-12 05:46:00 | NPP-375D | EPITACIOLÂNDIA | ACRE | Brasil | 1200252 | 12 | 33 | nan | nan | nan | Amazônia | 1.7 |
| 7f041577-a3a6-322b-b95c-be9562f84b8d | -11.77656 | -64.93758 | 2025-09-12 05:46:00 | NPP-375D | GUAJARÁ-MIRIM | RONDÔNIA | Brasil | 1100106 | 11 | 33 | nan | nan | nan | Amazônia | 1.4 |
| 75eb6bff-91c0-3988-a9f8-1d405124885e | -11.87294 | -58.82124 | 2025-09-12 05:46:00 | NPP-375D | JUÍNA | MATO GROSSO | Brasil | 5105150 | 51 | 33 | nan | nan | nan | Cerrado | 1.4 |
| 73efa903-00bd-3b3a-98e3-53235091f09a | -9.34916 | -65.45744 | 2025-09-12 05:46:00 | NPP-375D | LÁBREA | AMAZONAS | Brasil | 1302405 | 13 | 33 | nan | nan | nan | Amazônia | 1.4 |
| d9f83bb8-5000-3ab2-b0ba-a868206df9ad | -11.77448 | -64.92973 | 2025-09-12 05:46:00 | NPP-375D | GUAJARÁ-MIRIM | RONDÔNIA | Brasil | 1100106 | 11 | 33 | nan | nan | nan | Amazônia | 0.9 |
| b4c98cf9-cbcc-397e-95ff-0cad04e94adb | -14.41236 | -52.92978 | 2025-09-12 05:46:00 | NPP-375D | CAMPINÁPOLIS | MATO GROSSO | Brasil | 5102603 | 51 | 33 | nan | nan | nan | Cerrado | 1.3 |
| b2dfe7d8-e5b2-37dc-97f1-992fde2554cb | -9.34638 | -65.45339 | 2025-09-12 05:46:00 | NPP-375D | LÁBREA | AMAZONAS | Brasil | 1302405 | 13 | 33 | nan | nan | nan | Amazônia | 1.4 |
| b0aec515-ffe7-3bf8-bf2e-ce5aacf2d0f8 | -11.77711 | -64.93388 | 2025-09-12 05:46:00 | NPP-375D | GUAJARÁ-MIRIM | RONDÔNIA | Brasil | 1100106 | 11 | 33 | nan | nan | nan | Amazônia | 1.4 |
| 22029709-2828-3ffa-8037-754f5e384f0c | -11.77505 | -64.92603 | 2025-09-12 05:46:00 | NPP-375D | GUAJARÁ-MIRIM | RONDÔNIA | Brasil | 1100106 | 11 | 33 | nan | nan | nan | Amazônia | 0.9 |
| b4da750d-ba65-3323-b8c5-26ad459989f8 | -9.89281 | -51.87124 | 2025-09-12 05:46:00 | NPP-375D | VILA RICA | MATO GROSSO | Brasil | 5108600 | 51 | 33 | nan | nan | nan | Amazônia | 3.2 |
| 95f9245f-2546-316a-82db-ab65f8be7482 | -9.53663 | -63.57613 | 2025-09-12 05:46:00 | NPP-375D | PORTO VELHO | RONDÔNIA | Brasil | 1100205 | 11 | 33 | nan | nan | nan | Amazônia | 1.1 |
| d41d2dd0-81b1-39fc-86c3-af8ff20c854f | -11.18896 | -55.06163 | 2025-09-12 05:46:00 | NPP-375D | ITAÚBA | MATO GROSSO | Brasil | 5104559 | 51 | 33 | nan | nan | nan | Amazônia | 2.0 |
| 5a3917dc-2081-3ac9-a0ad-55f9a75cabc2 | -11.19789 | -55.08299 | 2025-09-12 05:46:00 | NPP-375D | ITAÚBA | MATO GROSSO | Brasil | 5104559 | 51 | 33 | nan | nan | nan | Amazônia | 1.7 |
| fcd02986-83a1-3d6f-b2c4-742724c9449b | -14.32376 | -54.1346 | 2025-09-12 05:46:00 | NPP-375D | PARANATINGA | MATO GROSSO | Brasil | 5106307 | 51 | 33 | nan | nan | nan | Cerrado | 3.0 |
| 74e38002-4ae2-3a24-b959-1fd94a2109a8 | -11.23206 | -55.00556 | 2025-09-12 05:46:00 | NPP-375D | CLÁUDIA | MATO GROSSO | Brasil | 5103056 | 51 | 33 | nan | nan | nan | Amazônia | 1.6 |
| 07df9c84-cfc6-348e-bd33-2f75242b75b6 | -9.89973 | -51.87525 | 2025-09-12 05:46:00 | NPP-375D | VILA RICA | MATO GROSSO | Brasil | 5108600 | 51 | 33 | nan | nan | nan | Amazônia | 3.7 |
| 7c8506b4-838a-359a-90b9-616dfa484342 | -11.8688 | -58.8154 | 2025-09-12 05:46:00 | NPP-375D | JUÍNA | MATO GROSSO | Brasil | 5105150 | 51 | 33 | nan | nan | nan | Cerrado | 1.1 |
| 14308532-45ec-3a9d-842a-ce53387266c7 | -9.2183 | -59.38197 | 2025-09-12 05:46:00 | NPP-375D | COLNIZA | MATO GROSSO | Brasil | 5103254 | 51 | 33 | nan | nan | nan | Amazônia | 1.3 |
| 50b6ad7e-90b5-34db-a51a-42697423f7d0 | -9.89251 | -51.87361 | 2025-09-12 05:46:00 | NPP-375D | VILA RICA | MATO GROSSO | Brasil | 5108600 | 51 | 33 | nan | nan | nan | Amazônia | 3.8 |
| afa20da9-6132-3728-b500-9dd18c0f2866 | -10.35651 | -57.48794 | 2025-09-12 05:46:00 | NPP-375D | JUARA | MATO GROSSO | Brasil | 5105101 | 51 | 33 | nan | nan | nan | Amazônia | 1.8 |
| 8db35bce-aca3-341e-8ef9-b41db0e10827 | -9.50563 | -65.66538 | 2025-09-12 05:46:00 | NPP-375D | PORTO VELHO | RONDÔNIA | Brasil | 1100205 | 11 | 33 | nan | nan | nan | Amazônia | 1.0 |
| 60e6ddef-b44f-3c98-9a0a-da94ba60cde3 | -9.02584 | -64.30067 | 2025-09-12 05:46:00 | NPP-375D | PORTO VELHO | RONDÔNIA | Brasil | 1100205 | 11 | 33 | nan | nan | nan | Amazônia | 1.1 |
| 415c1e35-6787-3b95-8d4f-d6381e6d4e01 | -11.18727 | -55.06736 | 2025-09-12 05:46:00 | NPP-375D | ITAÚBA | MATO GROSSO | Brasil | 5104559 | 51 | 33 | nan | nan | nan | Amazônia | 1.8 |
| f44f4ef7-f4a3-3d8b-b31f-28d8f525f1ed | -9.29502 | -65.60707 | 2025-09-12 05:46:00 | NPP-375D | LÁBREA | AMAZONAS | Brasil | 1302405 | 13 | 33 | nan | nan | nan | Amazônia | 2.8 |
| 973ebe1a-f95a-371c-b1a6-bf4d61f3ea84 | -9.23822 | -65.80204 | 2025-09-12 05:46:00 | NPP-375D | LÁBREA | AMAZONAS | Brasil | 1302405 | 13 | 33 | nan | nan | nan | Amazônia | 1.7 |
| bec58bd4-9172-3866-8adc-b224c4b71950 | -11.87647 | -58.82264 | 2025-09-12 05:46:00 | NPP-375D | JUÍNA | MATO GROSSO | Brasil | 5105150 | 51 | 33 | nan | nan | nan | Cerrado | 1.5 |
| 5d927285-30ab-380d-a70f-3738a3bc6c6b | -12.97725 | -54.75673 | 2025-09-12 05:46:00 | NPP-375D | NOVA UBIRATÃ | MATO GROSSO | Brasil | 5106240 | 51 | 33 | nan | nan | nan | Amazônia | 0.2 |
| 8412f2a6-28b0-36f0-803e-0475d9b0ce45 | -11.17556 | -55.06077 | 2025-09-12 05:46:00 | NPP-375D | ITAÚBA | MATO GROSSO | Brasil | 5104559 | 51 | 33 | nan | nan | nan | Amazônia | 1.2 |
| 4fdfba21-471e-31e6-86bf-377b8181943a | -11.18162 | -55.07049 | 2025-09-12 05:46:00 | NPP-375D | ITAÚBA | MATO GROSSO | Brasil | 5104559 | 51 | 33 | nan | nan | nan | Amazônia | 1.2 |
| 85f94ef0-51c0-3a9f-b383-de3e095dbb76 | -10.39313 | -69.70547 | 2025-09-12 05:46:00 | NPP-375D | SENA MADUREIRA | ACRE | Brasil | 1200500 | 12 | 33 | nan | nan | nan | Amazônia | 0.7 |
| 024d58c1-bd47-3b50-8405-291e8135b001 | -12.41843 | -63.88541 | 2025-09-12 05:46:00 | NPP-375D | COSTA MARQUES | RONDÔNIA | Brasil | 1100080 | 11 | 33 | nan | nan | nan | Amazônia | 0.7 |
| b3fd9b20-2d2f-38eb-b1a0-91350ca272d6 | -8.64391 | -55.24736 | 2025-09-12 05:46:00 | NPP-375D | NOVO PROGRESSO | PARÁ | Brasil | 1505031 | 15 | 33 | nan | nan | nan | Amazônia | 1.7 |
| 0d44f7d6-6062-3ad0-8615-0319417f206a | -9.33013 | -65.73109 | 2025-09-12 05:46:00 | NPP-375D | LÁBREA | AMAZONAS | Brasil | 1302405 | 13 | 33 | nan | nan | nan | Amazônia | 1.4 |
| 27a7d4c7-64d2-3f8c-bf5a-13be0aaf214e | -12.92656 | -54.79313 | 2025-09-12 05:46:00 | NPP-375D | NOVA UBIRATÃ | MATO GROSSO | Brasil | 5106240 | 51 | 33 | nan | nan | nan | Cerrado | 2.3 |
| dc04400e-b208-321a-aa7a-3b0e12bd6882 | -14.50675 | -53.92369 | 2025-09-12 05:46:00 | NPP-375D | PARANATINGA | MATO GROSSO | Brasil | 5106307 | 51 | 33 | nan | nan | nan | Cerrado | 3.1 |
| 21f3d353-10a9-3d26-aac3-ed683ef4c36c | -9.23877 | -65.79854 | 2025-09-12 05:46:00 | NPP-375D | LÁBREA | AMAZONAS | Brasil | 1302405 | 13 | 33 | nan | nan | nan | Amazônia | 3.0 |
| 58cf283e-57d6-3ec2-9990-b108ff5f69ad | -9.21703 | -59.39093 | 2025-09-12 05:46:00 | NPP-375D | COLNIZA | MATO GROSSO | Brasil | 5103254 | 51 | 33 | nan | nan | nan | Amazônia | 0.9 |
| c555bfa6-7067-37ba-8725-241f8b8aff85 | -9.50379 | -66.79198 | 2025-09-12 05:46:00 | NPP-375D | LÁBREA | AMAZONAS | Brasil | 1302405 | 13 | 33 | nan | nan | nan | Amazônia | 1.9 |
| 5775c5b0-57c9-31c6-b630-010cac8c655b | -9.29169 | -65.60654 | 2025-09-12 05:46:00 | NPP-375D | LÁBREA | AMAZONAS | Brasil | 1302405 | 13 | 33 | nan | nan | nan | Amazônia | 2.8 |
| 375507aa-4905-32cc-a48e-0722af2e322c | -12.91787 | -54.76599 | 2025-09-12 05:46:00 | NPP-375D | NOVA UBIRATÃ | MATO GROSSO | Brasil | 5106240 | 51 | 33 | nan | nan | nan | Amazônia | 3.3 |
| f43ec67b-17a1-3df4-8f2e-a62304469559 | -9.29666 | -65.59656 | 2025-09-12 05:46:00 | NPP-375D | LÁBREA | AMAZONAS | Brasil | 1302405 | 13 | 33 | nan | nan | nan | Amazônia | 16.4 |
| 09cf5ead-51a8-3e1b-a006-4e5d7ed8208c | -11.1989 | -55.08198 | 2025-09-12 05:46:00 | NPP-375D | ITAÚBA | MATO GROSSO | Brasil | 5104559 | 51 | 33 | nan | nan | nan | Amazônia | 2.7 |
| 75146af8-77f1-3a25-a6c2-bc4e4ce337c0 | -14.32444 | -54.12828 | 2025-09-12 05:46:00 | NPP-375D | PARANATINGA | MATO GROSSO | Brasil | 5106307 | 51 | 33 | nan | nan | nan | Cerrado | 3.0 |
| e5d5b286-c746-37c8-81e0-fba8ee7c66e4 | -9.83824 | -54.53563 | 2025-09-12 05:46:00 | NPP-375D | GUARANTÃ DO NORTE | MATO GROSSO | Brasil | 5104104 | 51 | 33 | nan | nan | nan | Amazônia | 1.8 |
| 34437bd9-70b7-39a9-8d1b-baea31ca8911 | -11.77483 | -64.92595 | 2025-09-12 05:46:00 | NPP-375D | GUAJARÁ-MIRIM | RONDÔNIA | Brasil | 1100106 | 11 | 33 | nan | nan | nan | Amazônia | 0.7 |
| d75922e8-1512-390e-b9d7-2b35b834d354 | -10.36086 | -57.48524 | 2025-09-12 05:46:00 | NPP-375D | JUARA | MATO GROSSO | Brasil | 5105101 | 51 | 33 | nan | nan | nan | Amazônia | 2.4 |
| 884220cc-020a-37f4-9ff8-0991fc930c0b | -12.93237 | -54.75205 | 2025-09-12 05:46:00 | NPP-375D | NOVA UBIRATÃ | MATO GROSSO | Brasil | 5106240 | 51 | 33 | nan | nan | nan | Amazônia | 2.6 |
| 8d74e8bd-15b6-3e54-9c59-5f79c041fad9 | -9.29556 | -65.60357 | 2025-09-12 05:46:00 | NPP-375D | LÁBREA | AMAZONAS | Brasil | 1302405 | 13 | 33 | nan | nan | nan | Amazônia | 2.8 |
| 0c352094-345e-33d4-a6c1-904f8d4ccbde | -11.19274 | -55.08138 | 2025-09-12 05:46:00 | NPP-375D | ITAÚBA | MATO GROSSO | Brasil | 5104559 | 51 | 33 | nan | nan | nan | Amazônia | 2.1 |
| 996f3bae-b03f-3002-950c-af604cb66dd8 | -11.19229 | -55.0777 | 2025-09-12 05:46:00 | NPP-375D | ITAÚBA | MATO GROSSO | Brasil | 5104559 | 51 | 33 | nan | nan | nan | Amazônia | 1.7 |
| 7b040580-0cec-3906-997a-b88107d2a4bb | -9.89762 | -51.89388 | 2025-09-12 05:46:00 | NPP-375D | VILA RICA | MATO GROSSO | Brasil | 5108600 | 51 | 33 | nan | nan | nan | Amazônia | 4.7 |
| af0ae78d-d000-3693-a7a3-bed303022f1e | -9.34359 | -65.44935 | 2025-09-12 05:46:00 | NPP-375D | LÁBREA | AMAZONAS | Brasil | 1302405 | 13 | 33 | nan | nan | nan | Amazônia | 0.9 |
| 74a59177-06f2-37e1-9795-0598378fbd6e | -12.92475 | -54.80851 | 2025-09-12 05:46:00 | NPP-375D | NOVA UBIRATÃ | MATO GROSSO | Brasil | 5106240 | 51 | 33 | nan | nan | nan | Cerrado | 2.2 |
| 0922c2fa-0e56-38c7-88d0-176d72ad6180 | -9.34861 | -65.46095 | 2025-09-12 05:46:00 | NPP-375D | LÁBREA | AMAZONAS | Brasil | 1302405 | 13 | 33 | nan | nan | nan | Amazônia | 1.0 |
| 6302cee0-2746-3a85-b4d1-61e94054d7e7 | -11.87781 | -58.8217 | 2025-09-12 05:46:00 | NPP-375D | JUÍNA | MATO GROSSO | Brasil | 5105150 | 51 | 33 | nan | nan | nan | Cerrado | 1.4 |
| 2eb7c283-16eb-3a68-84ec-2a0fca6a0ed8 | -9.35304 | -65.45444 | 2025-09-12 05:46:00 | NPP-375D | LÁBREA | AMAZONAS | Brasil | 1302405 | 13 | 33 | nan | nan | nan | Amazônia | 1.4 |
| bae5e4d2-d9d5-3304-8a8b-fa140ae6ebcc | -10.36214 | -57.48515 | 2025-09-12 05:46:00 | NPP-375D | JUARA | MATO GROSSO | Brasil | 5105101 | 51 | 33 | nan | nan | nan | Amazônia | 1.8 |
| 2bd4ec3e-a1b2-3121-98fc-07e2a627b561 | -9.153 | -65.39371 | 2025-09-12 05:46:00 | NPP-375D | LÁBREA | AMAZONAS | Brasil | 1302405 | 13 | 33 | nan | nan | nan | Amazônia | 0.5 |
| f97cbb5e-b9ba-3121-99c3-0541940e1168 | -9.52253 | -54.63165 | 2025-09-12 05:46:00 | NPP-375D | NOVO PROGRESSO | PARÁ | Brasil | 1505031 | 15 | 33 | nan | nan | nan | Amazônia | 5.3 |
| 2d3c7069-e9e4-3f75-83a3-b1a03b34f7c1 | -9.29333 | -65.59602 | 2025-09-12 05:46:00 | NPP-375D | LÁBREA | AMAZONAS | Brasil | 1302405 | 13 | 33 | nan | nan | nan | Amazônia | 16.4 |
| bc6d9a97-8263-3293-8522-1b86d8329b37 | -11.18105 | -55.07511 | 2025-09-12 05:46:00 | NPP-375D | ITAÚBA | MATO GROSSO | Brasil | 5104559 | 51 | 33 | nan | nan | nan | Amazônia | 1.2 |
| 6fe7535d-a7fe-30a8-a645-310b236c0686 | -9.35223 | -64.26346 | 2025-09-12 05:46:00 | NPP-375D | PORTO VELHO | RONDÔNIA | Brasil | 1100205 | 11 | 33 | nan | nan | nan | Amazônia | 0.7 |
| b1fa990b-7297-30f0-8fba-32f423e9508a | -10.35927 | -69.42168 | 2025-09-12 05:46:00 | NPP-375D | SENA MADUREIRA | ACRE | Brasil | 1200500 | 12 | 33 | nan | nan | nan | Amazônia | 1.1 |
| d39fa0e8-4cd2-320a-ba2a-a44793da32c7 | -12.92382 | -54.7612 | 2025-09-12 05:46:00 | NPP-375D | NOVA UBIRATÃ | MATO GROSSO | Brasil | 5106240 | 51 | 33 | nan | nan | nan | Amazônia | 3.7 |
| e5314dc3-0377-3cef-8ca2-03c4a0076ae6 | -9.19171 | -65.88066 | 2025-09-12 05:46:00 | NPP-375D | LÁBREA | AMAZONAS | Brasil | 1302405 | 13 | 33 | nan | nan | nan | Amazônia | 1.3 |
| 52556ec6-dd6d-3560-8d1d-9783113b2fbd | -8.85857 | -64.23011 | 2025-09-12 05:46:00 | NPP-375D | CANUTAMA | AMAZONAS | Brasil | 1300904 | 13 | 33 | nan | nan | nan | Amazônia | 0.5 |
| cd830f83-39c3-385d-b39c-1a219c7a7f94 | -11.87365 | -58.81592 | 2025-09-12 05:46:00 | NPP-375D | JUÍNA | MATO GROSSO | Brasil | 5105150 | 51 | 33 | nan | nan | nan | Cerrado | 1.4 |
| bc6ce326-679c-39cb-a5fb-908292a77356 | -9.10801 | -63.55392 | 2025-09-12 05:46:00 | NPP-375D | CANDEIAS DO JAMARI | RONDÔNIA | Brasil | 1100809 | 11 | 33 | nan | nan | nan | Amazônia | 0.6 |
| ecf00914-c749-3808-8545-214d46d7f567 | -9.5116 | -65.58364 | 2025-09-12 05:46:00 | NPP-375D | PORTO VELHO | RONDÔNIA | Brasil | 1100205 | 11 | 33 | nan | nan | nan | Amazônia | 2.2 |
| f1fa28ed-59b5-35c4-ba90-591a21e3e509 | -11.18507 | -55.08611 | 2025-09-12 05:46:00 | NPP-375D | ITAÚBA | MATO GROSSO | Brasil | 5104559 | 51 | 33 | nan | nan | nan | Amazônia | 1.3 |
| c2d4d205-572a-3c35-9775-b8977bbbed3d | -9.12872 | -65.48338 | 2025-09-12 05:46:00 | NPP-375D | LÁBREA | AMAZONAS | Brasil | 1302405 | 13 | 33 | nan | nan | nan | Amazônia | 0.6 |
| 8df2b334-c232-376f-af7f-afd625aaa636 | -9.50949 | -65.58354 | 2025-09-12 05:46:00 | NPP-375D | PORTO VELHO | RONDÔNIA | Brasil | 1100205 | 11 | 33 | nan | nan | nan | Amazônia | 4.7 |
| 47836dba-4b2a-3ddf-b1bf-cbdbb74cd368 | -8.98241 | -65.44977 | 2025-09-12 05:46:00 | NPP-375D | LÁBREA | AMAZONAS | Brasil | 1302405 | 13 | 33 | nan | nan | nan | Amazônia | 0.9 |
| ba7b8714-8d20-31ed-b30c-5bedc7970e18 | -14.32777 | -54.12192 | 2025-09-12 05:46:00 | NPP-375D | PARANATINGA | MATO GROSSO | Brasil | 5106307 | 51 | 33 | nan | nan | nan | Cerrado | 3.6 |
| f1270bf5-db4f-30a5-8f37-33d929ba5b73 | -12.91804 | -54.75524 | 2025-09-12 05:46:00 | NPP-375D | NOVA UBIRATÃ | MATO GROSSO | Brasil | 5106240 | 51 | 33 | nan | nan | nan | Amazônia | 4.1 |
| 82c1e30a-48f9-3f7d-bb6a-f30f08e945e3 | -11.7933 | -62.73911 | 2025-09-12 05:46:00 | NPP-375D | SÃO MIGUEL DO GUAPORÉ | RONDÔNIA | Brasil | 1100320 | 11 | 33 | nan | nan | nan | Amazônia | 4.6 |
| cabeb5a9-4015-311f-9849-0d4c9149e138 | -11.18223 | -55.06556 | 2025-09-12 05:46:00 | NPP-375D | ITAÚBA | MATO GROSSO | Brasil | 5104559 | 51 | 33 | nan | nan | nan | Amazônia | 1.5 |
| 8996abcc-fe40-3e2e-a568-e9566a0c0d82 | -8.98574 | -65.45029 | 2025-09-12 05:46:00 | NPP-375D | LÁBREA | AMAZONAS | Brasil | 1302405 | 13 | 33 | nan | nan | nan | Amazônia | 1.4 |
| 9e5edda2-8e43-3feb-93d6-5ee767697bde | -11.1912 | -55.08696 | 2025-09-12 05:46:00 | NPP-375D | ITAÚBA | MATO GROSSO | Brasil | 5104559 | 51 | 33 | nan | nan | nan | Amazônia | 2.6 |
| a97f873a-1eab-3686-9455-972e8216169b | -12.965 | -54.75029 | 2025-09-12 05:46:00 | NPP-375D | NOVA UBIRATÃ | MATO GROSSO | Brasil | 5106240 | 51 | 33 | nan | nan | nan | Amazônia | 1.9 |
| 708a7707-5e45-3e23-9371-d105ed3e8346 | -9.33291 | -65.73512 | 2025-09-12 05:46:00 | NPP-375D | LÁBREA | AMAZONAS | Brasil | 1302405 | 13 | 33 | nan | nan | nan | Amazônia | 1.1 |
| d54b6f3d-f4e4-3417-ad91-2438109c50c1 | -9.33861 | -65.45936 | 2025-09-12 05:46:00 | NPP-375D | LÁBREA | AMAZONAS | Brasil | 1302405 | 13 | 33 | nan | nan | nan | Amazônia | 1.3 |
| 257f8825-ac69-3f24-990c-8e6b6d63106a | -9.11876 | -65.50337 | 2025-09-12 05:46:00 | NPP-375D | LÁBREA | AMAZONAS | Brasil | 1302405 | 13 | 33 | nan | nan | nan | Amazônia | 1.0 |
| 7bb5e45c-cc57-3070-974e-0c62da5be510 | -11.19389 | -55.07214 | 2025-09-12 05:46:00 | NPP-375D | ITAÚBA | MATO GROSSO | Brasil | 5104559 | 51 | 33 | nan | nan | nan | Amazônia | 2.0 |
| 56e63e9e-e9df-3f50-bfb1-eec73abca06f | -9.35638 | -65.45498 | 2025-09-12 05:46:00 | NPP-375D | LÁBREA | AMAZONAS | Brasil | 1302405 | 13 | 33 | nan | nan | nan | Amazônia | 1.1 |
| b26872bb-8e8d-3283-8746-5274b5f1032d | -12.86692 | -62.1237 | 2025-09-12 05:46:00 | NPP-375D | ALTA FLORESTA D'OESTE | RONDÔNIA | Brasil | 1100015 | 11 | 33 | nan | nan | nan | Amazônia | 1.6 |
| 48737f44-961a-3a61-89ef-e77d4febffd6 | -11.19948 | -55.07733 | 2025-09-12 05:46:00 | NPP-375D | ITAÚBA | MATO GROSSO | Brasil | 5104559 | 51 | 33 | nan | nan | nan | Amazônia | 2.1 |
| 1ddfe3a6-63c5-32f5-ba74-5e2faec205d4 | -12.92596 | -54.79822 | 2025-09-12 05:46:00 | NPP-375D | NOVA UBIRATÃ | MATO GROSSO | Brasil | 5106240 | 51 | 33 | nan | nan | nan | Cerrado | 1.7 |
| 2c6200e9-a335-3177-8c02-955b66268f3e | -12.92539 | -54.75658 | 2025-09-12 05:46:00 | NPP-375D | NOVA UBIRATÃ | MATO GROSSO | Brasil | 5106240 | 51 | 33 | nan | nan | nan | Amazônia | 2.6 |
| 8ef0d06e-f1bd-347b-bf01-9a7d519d63cf | -9.04038 | -65.40134 | 2025-09-12 05:46:00 | NPP-375D | LÁBREA | AMAZONAS | Brasil | 1302405 | 13 | 33 | nan | nan | nan | Amazônia | 1.2 |
| 3bfdb8d0-99e7-34a7-bec2-027561341211 | -10.57064 | -68.93327 | 2025-09-12 05:46:00 | NPP-375D | XAPURI | ACRE | Brasil | 1200708 | 12 | 33 | nan | nan | nan | Amazônia | 1.3 |
| ec43e1ee-e3ae-3665-aa13-c5edfa6db434 | -11.19216 | -55.08601 | 2025-09-12 05:46:00 | NPP-375D | ITAÚBA | MATO GROSSO | Brasil | 5104559 | 51 | 33 | nan | nan | nan | Amazônia | 2.1 |
| 847728cd-f956-3de5-962e-1d4d01e9c70a | -10.36173 | -57.48837 | 2025-09-12 05:46:00 | NPP-375D | JUARA | MATO GROSSO | Brasil | 5105101 | 51 | 33 | nan | nan | nan | Amazônia | 1.8 |
| 46695635-65c6-3125-92ea-85c8830cffb8 | -11.79705 | -62.73966 | 2025-09-12 05:46:00 | NPP-375D | SÃO MIGUEL DO GUAPORÉ | RONDÔNIA | Brasil | 1100320 | 11 | 33 | nan | nan | nan | Amazônia | 4.6 |
| a3dddf51-c954-3638-8929-a4b25f26ffe7 | -9.51523 | -54.63968 | 2025-09-12 05:46:00 | NPP-375D | NOVO PROGRESSO | PARÁ | Brasil | 1505031 | 15 | 33 | nan | nan | nan | Amazônia | 9.6 |


[Clique aqui para ver as próximas entradas](README115.md)
