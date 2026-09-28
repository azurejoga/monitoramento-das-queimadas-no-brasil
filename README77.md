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

## Dados Diários - Página 77

| ID | Latitude | Longitude | Data/Hora GMT | Satélite | Município | Estado | País | Município ID | Estado ID | País ID | Dias sem Chuva | Precipitação | Risco de Fogo | Bioma | FRP |
|----|----------|-----------|---------------|----------|-----------|--------|------|--------------|-----------|---------|----------------|--------------|----------------|-------|-----|
| 2244a2dd-d46a-3956-ac49-357ddbd4a199 | -8.2482 | -45.4356 | 2026-09-28 14:10:00 | GOES-19 | BAIXA GRANDE DO RIBEIRO | PIAUÍ | Brasil | 2201150 | 22 | 33 | nan | nan | nan | Cerrado | 100.3 |
| 0a04fead-d7d0-3e74-befd-7ca9628ec725 | -9.1771 | -61.3882 | 2026-09-28 14:10:00 | GOES-19 | COLNIZA | MATO GROSSO | Brasil | 5103254 | 51 | 33 | nan | nan | nan | Amazônia | 88.1 |
| 27e715ba-dfd2-30c9-88bc-1abb9fe561f1 | -10.4043 | -53.8236 | 2026-09-28 14:10:00 | GOES-19 | PEIXOTO DE AZEVEDO | MATO GROSSO | Brasil | 5106422 | 51 | 33 | nan | nan | nan | Amazônia | 63.0 |
| 03c0b776-d811-3bbd-abdd-cf17773b8d4b | -15.6867 | -48.2141 | 2026-09-28 14:10:00 | GOES-19 | BRASÍLIA | DISTRITO FEDERAL | Brasil | 5300108 | 53 | 33 | nan | nan | nan | Cerrado | 92.4 |
| e7a8c52b-2c30-3649-befe-0cf2c564cd4b | -8.1664 | -44.4382 | 2026-09-28 14:10:00 | GOES-19 | URUÇUÍ | PIAUÍ | Brasil | 2211209 | 22 | 33 | nan | nan | nan | Cerrado | 108.7 |
| 508038f4-f777-32a5-be49-e45247fa2722 | -15.1847 | -46.141 | 2026-09-28 14:10:00 | GOES-19 | FORMOSO | MINAS GERAIS | Brasil | 3126208 | 31 | 33 | nan | nan | nan | Cerrado | 104.8 |
| 1a5dfe6e-f038-3481-997b-bebb59ea09e5 | -12.6836 | -47.3217 | 2026-09-28 14:10:00 | GOES-19 | PARANÃ | TOCANTINS | Brasil | 1716208 | 17 | 33 | nan | nan | nan | Cerrado | 144.3 |
| b5d9a483-89f7-3807-b074-67b65d284bb4 | -11.9244 | -50.4866 | 2026-09-28 14:10:00 | GOES-19 | FORMOSO DO ARAGUAIA | TOCANTINS | Brasil | 1708205 | 17 | 33 | nan | nan | nan | Cerrado | 72.5 |
| 5ba01351-e148-3d88-a43e-1edc074c6ef4 | -11.8094 | -50.5428 | 2026-09-28 14:10:00 | GOES-19 | FORMOSO DO ARAGUAIA | TOCANTINS | Brasil | 1708205 | 17 | 33 | nan | nan | nan | Cerrado | 79.1 |
| c6df72ca-8dff-3444-9e96-9bae68816611 | -11.7828 | -51.0578 | 2026-09-28 14:10:00 | GOES-19 | SÃO FÉLIX DO ARAGUAIA | MATO GROSSO | Brasil | 5107859 | 51 | 33 | nan | nan | nan | Cerrado | 149.2 |
| c6070b17-6c8c-3e94-aa40-6b6bf2cd4242 | -11.1966 | -44.7805 | 2026-09-28 14:10:00 | GOES-19 | SANTA RITA DE CÁSSIA | BAHIA | Brasil | 2928406 | 29 | 33 | nan | nan | nan | Cerrado | 331.0 |
| fee553ad-8a43-30ca-a5c0-bea03f0b7cec | -12.7868 | -54.0275 | 2026-09-28 14:10:00 | GOES-19 | PARANATINGA | MATO GROSSO | Brasil | 5106307 | 51 | 33 | nan | nan | nan | Amazônia | 114.1 |
| 5631315f-4ecf-30be-8147-68b60f2b4e5e | -11.1775 | -44.7832 | 2026-09-28 14:10:00 | GOES-19 | SANTA RITA DE CÁSSIA | BAHIA | Brasil | 2928406 | 29 | 33 | nan | nan | nan | Cerrado | 213.4 |
| 42dcce0d-35ac-3740-8eca-b3f91d0b963b | -11.3922 | -43.4417 | 2026-09-28 14:10:00 | GOES-19 | BARRA | BAHIA | Brasil | 2902708 | 29 | 33 | nan | nan | nan | Cerrado | 182.6 |
| f5cc4deb-723b-333c-bf7f-89cb8cf675a7 | -12.1731 | -50.4142 | 2026-09-28 14:10:00 | GOES-19 | FORMOSO DO ARAGUAIA | TOCANTINS | Brasil | 1708205 | 17 | 33 | nan | nan | nan | Cerrado | 96.5 |
| d015bb9f-c8be-3d15-8ab0-c5bc74b5c2fe | -11.7141 | -50.5538 | 2026-09-28 14:10:00 | GOES-19 | FORMOSO DO ARAGUAIA | TOCANTINS | Brasil | 1708205 | 17 | 33 | nan | nan | nan | Cerrado | 67.9 |
| a96e2744-f745-3f49-8f5f-7526da191acc | -13.1803 | -48.5409 | 2026-09-28 14:10:00 | GOES-19 | JAÚ DO TOCANTINS | TOCANTINS | Brasil | 1711506 | 17 | 33 | nan | nan | nan | Cerrado | 142.3 |
| 09e58e4e-3398-340d-874f-05e2c5e4ffa8 | -12.8061 | -54.0048 | 2026-09-28 14:10:00 | GOES-19 | PARANATINGA | MATO GROSSO | Brasil | 5106307 | 51 | 33 | nan | nan | nan | Amazônia | 118.2 |
| 43e0c91a-0a3b-3a2a-8fa1-2da4a773ebfb | -13.4201 | -51.3517 | 2026-09-28 14:10:00 | GOES-19 | RIBEIRÃO CASCALHEIRA | MATO GROSSO | Brasil | 5107180 | 51 | 33 | nan | nan | nan | Cerrado | 64.3 |
| d42fb7ae-b8e9-3e1d-9305-4a8eefa42bdd | -11.7316 | -50.6587 | 2026-09-28 14:10:00 | GOES-19 | FORMOSO DO ARAGUAIA | TOCANTINS | Brasil | 1708205 | 17 | 33 | nan | nan | nan | Cerrado | 56.2 |
| afaa725c-bd15-34cb-80a4-b2b20f92a781 | -9.1325 | -45.6138 | 2026-09-28 14:10:00 | GOES-19 | SANTA FILOMENA | PIAUÍ | Brasil | 2209203 | 22 | 33 | nan | nan | nan | Cerrado | 177.9 |
| 5a497532-fb43-3563-a865-f47e73dfbfe5 | -8.7267 | -44.8836 | 2026-09-28 14:10:00 | GOES-19 | CURRAIS | PIAUÍ | Brasil | 2203230 | 22 | 33 | nan | nan | nan | Cerrado | 93.2 |
| 82b0d6c6-22df-3584-9fa3-482d5cd20151 | -13.5911 | -51.458 | 2026-09-28 14:10:00 | GOES-19 | COCALINHO | MATO GROSSO | Brasil | 5103106 | 51 | 33 | nan | nan | nan | Cerrado | 188.7 |
| 23de6fa2-3d2e-3740-9b5a-5d71bc868ed6 | -12.8059 | -54.0255 | 2026-09-28 14:10:00 | GOES-19 | PARANATINGA | MATO GROSSO | Brasil | 5106307 | 51 | 33 | nan | nan | nan | Amazônia | 118.1 |
| 0cf2a569-7052-3a28-a4ca-284658f6a94a | -11.7177 | -44.5188 | 2026-09-28 14:10:00 | GOES-19 | COTEGIPE | BAHIA | Brasil | 2909406 | 29 | 33 | nan | nan | nan | Cerrado | 212.7 |
| a12b7ee4-3207-36dc-bc6f-e1604b28982d | -11.197 | -44.7573 | 2026-09-28 14:10:00 | GOES-19 | SANTA RITA DE CÁSSIA | BAHIA | Brasil | 2928406 | 29 | 33 | nan | nan | nan | Cerrado | 132.3 |
| fa727039-6918-36fe-8b51-08117ba0847c | -11.1183 | -54.0062 | 2026-09-28 14:10:00 | GOES-19 | MARCELÂNDIA | MATO GROSSO | Brasil | 5105580 | 51 | 33 | nan | nan | nan | Amazônia | 82.5 |
| c67da0bd-77e3-335c-a1a5-696c2f2f350a | -11.4425 | -44.9303 | 2026-09-28 14:10:00 | GOES-19 | RIACHÃO DAS NEVES | BAHIA | Brasil | 2926202 | 29 | 33 | nan | nan | nan | Cerrado | 107.3 |
| cc2922b9-49c8-3b69-986e-2ef141e525d7 | -10.2254 | -50.0093 | 2026-09-28 14:10:00 | GOES-19 | PIUM | TOCANTINS | Brasil | 1717503 | 17 | 33 | nan | nan | nan | Cerrado | 73.8 |
| fb02d413-0602-36f0-a3a2-1c3c1344ec5e | -11.8662 | -50.5576 | 2026-09-28 14:10:00 | GOES-19 | FORMOSO DO ARAGUAIA | TOCANTINS | Brasil | 1708205 | 17 | 33 | nan | nan | nan | Cerrado | 65.1 |
| baf6a78d-cd6c-3938-8d07-7e9ac6f79e08 | -8.2807 | -54.7158 | 2026-09-28 14:10:00 | GOES-19 | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 102.1 |
| c01de4c3-79f9-3a54-bccd-ef17087a8fe4 | -8.2291 | -45.4602 | 2026-09-28 14:10:00 | GOES-19 | RIBEIRO GONÇALVES | PIAUÍ | Brasil | 2208908 | 22 | 33 | nan | nan | nan | Cerrado | 180.5 |
| 40209ac9-a969-3cd6-8e13-4cf28d7d8842 | -10.6035 | -49.9913 | 2026-09-28 14:10:00 | GOES-19 | LAGOA DA CONFUSÃO | TOCANTINS | Brasil | 1711902 | 17 | 33 | nan | nan | nan | Cerrado | 79.0 |
| fe359bbb-4462-3cd8-91ab-1633220a6a7e | -10.8187 | -57.2192 | 2026-09-28 14:10:00 | GOES-19 | JUARA | MATO GROSSO | Brasil | 5105101 | 51 | 33 | nan | nan | nan | Amazônia | 86.9 |
| fcc19c3a-cae5-39f5-8ac9-334224f7e88b | -11.7831 | -51.0365 | 2026-09-28 14:10:00 | GOES-19 | SÃO FÉLIX DO ARAGUAIA | MATO GROSSO | Brasil | 5107859 | 51 | 33 | nan | nan | nan | Cerrado | 68.1 |
| 40229e8f-a44a-3377-952e-c7335113543e | -13.0848 | -47.4423 | 2026-09-28 14:10:00 | GOES-19 | PARANÃ | TOCANTINS | Brasil | 1716208 | 17 | 33 | nan | nan | nan | Cerrado | 198.4 |
| d9bbec34-50e8-304f-9424-ff33d7592566 | -12.7417 | -47.2909 | 2026-09-28 14:10:00 | GOES-19 | ARRAIAS | TOCANTINS | Brasil | 1702406 | 17 | 33 | nan | nan | nan | Cerrado | 160.8 |
| 06b7d13a-a455-3722-b2f2-594d4c125dc8 | -12.2119 | -50.3666 | 2026-09-28 14:10:00 | GOES-19 | FORMOSO DO ARAGUAIA | TOCANTINS | Brasil | 1708205 | 17 | 33 | nan | nan | nan | Cerrado | 65.2 |
| e8f9d07c-2b70-3e36-9e9f-f3132b0b850f | -10.2065 | -50.0113 | 2026-09-28 14:10:00 | GOES-19 | PIUM | TOCANTINS | Brasil | 1717503 | 17 | 33 | nan | nan | nan | Cerrado | 130.9 |
| f3f0cd32-a6d9-3e63-9b22-d2ed04871148 | -11.7522 | -50.5494 | 2026-09-28 14:10:00 | GOES-19 | FORMOSO DO ARAGUAIA | TOCANTINS | Brasil | 1708205 | 17 | 33 | nan | nan | nan | Cerrado | 92.7 |
| 1a5921fb-45fa-372e-8d6d-c1b28926316c | -11.8281 | -50.562 | 2026-09-28 14:10:00 | GOES-19 | FORMOSO DO ARAGUAIA | TOCANTINS | Brasil | 1708205 | 17 | 33 | nan | nan | nan | Cerrado | 87.6 |
| 38358486-128d-3699-9800-0200a0a1252d | -10.4232 | -53.8219 | 2026-09-28 14:10:00 | GOES-19 | PEIXOTO DE AZEVEDO | MATO GROSSO | Brasil | 5106422 | 51 | 33 | nan | nan | nan | Amazônia | 62.4 |
| 7c0f6985-3f05-3070-856b-b9205c7b8f39 | -11.2154 | -44.801 | 2026-09-28 14:10:00 | GOES-19 | SANTA RITA DE CÁSSIA | BAHIA | Brasil | 2928406 | 29 | 33 | nan | nan | nan | Cerrado | 314.2 |
| 43c8585b-e8ce-339f-afac-82342585a202 | -11.77 | -50.6329 | 2026-09-28 14:10:00 | GOES-19 | FORMOSO DO ARAGUAIA | TOCANTINS | Brasil | 1708205 | 17 | 33 | nan | nan | nan | Cerrado | 70.7 |
| e3ac7152-eb5a-37ef-921b-579b70674193 | -8.3608 | -45.4695 | 2026-09-28 14:10:00 | GOES-19 | RIBEIRO GONÇALVES | PIAUÍ | Brasil | 2208908 | 22 | 33 | nan | nan | nan | Cerrado | 203.0 |
| c2ae6c49-1aca-3352-b648-02c14b4a2cf2 | -8.5731 | -45.0832 | 2026-09-28 14:10:00 | GOES-19 | BAIXA GRANDE DO RIBEIRO | PIAUÍ | Brasil | 2201150 | 22 | 33 | nan | nan | nan | Cerrado | 88.5 |
| 54d1a7f1-80c2-33db-9668-76e1b4087da1 | -12.1734 | -50.3927 | 2026-09-28 14:10:00 | GOES-19 | FORMOSO DO ARAGUAIA | TOCANTINS | Brasil | 1708205 | 17 | 33 | nan | nan | nan | Cerrado | 85.6 |
| fe939064-d14b-3ecb-b57d-86f9629c5187 | -15.1451 | -43.6088 | 2026-09-28 14:10:00 | GOES-19 | JAÍBA | MINAS GERAIS | Brasil | 3135050 | 31 | 33 | nan | nan | nan | Caatinga | 155.1 |
| 4d45b429-73c6-37d7-bdaa-c422c967ca04 | -7.449 | -44.6016 | 2026-09-28 14:10:00 | GOES-19 | URUÇUÍ | PIAUÍ | Brasil | 2211209 | 22 | 33 | nan | nan | nan | Cerrado | 114.0 |
| 4dabbc70-9aef-3bf7-97b9-968b5b824816 | -11.8472 | -50.5598 | 2026-09-28 14:10:00 | GOES-19 | FORMOSO DO ARAGUAIA | TOCANTINS | Brasil | 1708205 | 17 | 33 | nan | nan | nan | Cerrado | 64.5 |
| 35151853-f529-3ed5-8963-ea7e0cee2645 | -9.4999 | -46.385 | 2026-09-28 14:10:00 | GOES-19 | ALTO PARNAÍBA | MARANHÃO | Brasil | 2100501 | 21 | 33 | nan | nan | nan | Cerrado | 114.5 |
| dc7be701-001c-31f6-9457-0d11ad295511 | -11.3927 | -43.418 | 2026-09-28 14:10:00 | GOES-19 | BARRA | BAHIA | Brasil | 2902708 | 29 | 33 | nan | nan | nan | Cerrado | 310.9 |
| 5129f59b-63db-35d0-8367-005eaa28a74c | -10.8723 | -54.0694 | 2026-09-28 14:10:00 | GOES-19 | MARCELÂNDIA | MATO GROSSO | Brasil | 5105580 | 51 | 33 | nan | nan | nan | Amazônia | 57.3 |
| 2b50be51-0a56-3a52-87d8-b6df48f979e6 | -9.1584 | -61.4082 | 2026-09-28 14:10:00 | GOES-19 | COLNIZA | MATO GROSSO | Brasil | 5103254 | 51 | 33 | nan | nan | nan | Amazônia | 99.4 |
| 9a755db0-bbd1-3087-80c6-467b871ab498 | -12.2897 | -50.2712 | 2026-09-28 14:10:00 | GOES-19 | FORMOSO DO ARAGUAIA | TOCANTINS | Brasil | 1708205 | 17 | 33 | nan | nan | nan | Cerrado | 136.4 |
| e85ef96b-cd0a-3a3f-a871-ccec741c71e0 | -11.5352 | -47.3678 | 2026-09-28 14:10:00 | GOES-19 | ALMAS | TOCANTINS | Brasil | 1700400 | 17 | 33 | nan | nan | nan | Cerrado | 130.7 |
| 3edbf9c7-53c5-3246-8c44-2f0d2abf868c | -16.6424 | -48.4724 | 2026-09-28 14:10:00 | GOES-19 | SILVÂNIA | GOIÁS | Brasil | 5220603 | 52 | 33 | nan | nan | nan | Cerrado | 199.5 |
| 548f6092-d17b-325e-b4c3-fa82d0b771a3 | -11.8641 | -47.1004 | 2026-09-28 14:10:00 | GOES-19 | DIANÓPOLIS | TOCANTINS | Brasil | 1707009 | 17 | 33 | nan | nan | nan | Cerrado | 162.9 |
| 84cc6aae-b654-3752-8a3a-998e769b61bf | -12.6878 | -45.0192 | 2026-09-28 14:10:00 | GOES-19 | SÃO DESIDÉRIO | BAHIA | Brasil | 2928901 | 29 | 33 | nan | nan | nan | Cerrado | 148.9 |
| c7dab8fe-eda2-3d60-8d8f-6fcda28e83b2 | -7.4185 | -55.6301 | 2026-09-28 14:10:00 | GOES-19 | NOVO PROGRESSO | PARÁ | Brasil | 1505031 | 15 | 33 | nan | nan | nan | Amazônia | 274.4 |
| 92117d83-cb18-3f97-81c6-ef1704ac7529 | -11.8097 | -50.5214 | 2026-09-28 14:10:00 | GOES-19 | FORMOSO DO ARAGUAIA | TOCANTINS | Brasil | 1708205 | 17 | 33 | nan | nan | nan | Cerrado | 59.9 |
| 6531be51-6293-3368-83b3-ad9cbe5c8928 | -7.7088 | -44.8971 | 2026-09-28 14:10:00 | GOES-19 | URUÇUÍ | PIAUÍ | Brasil | 2211209 | 22 | 33 | nan | nan | nan | Cerrado | 90.4 |
| 3e8f8b74-d996-36c3-a5f6-b725545db71b | -8.2859 | -45.4317 | 2026-09-28 14:10:00 | GOES-19 | BAIXA GRANDE DO RIBEIRO | PIAUÍ | Brasil | 2201150 | 22 | 33 | nan | nan | nan | Cerrado | 123.2 |
| 11ec8cd4-daf3-37f5-9d79-98851728c132 | -12.4346 | -44.1733 | 2026-09-28 14:10:00 | GOES-19 | TABOCAS DO BREJO VELHO | BAHIA | Brasil | 2930907 | 29 | 33 | nan | nan | nan | Cerrado | 117.0 |
| 86721c3b-3587-3df6-84bb-f04e59100c5e | -11.7903 | -50.545 | 2026-09-28 14:10:00 | GOES-19 | FORMOSO DO ARAGUAIA | TOCANTINS | Brasil | 1708205 | 17 | 33 | nan | nan | nan | Cerrado | 62.5 |
| 158cee38-5309-3f92-bf4a-acd5dc346602 | 1.6566 | -55.903 | 2026-09-28 14:10:00 | GOES-19 | ORIXIMINÁ | PARÁ | Brasil | 1505304 | 15 | 33 | nan | nan | nan | Amazônia | 88.6 |
| 9bf1618b-ca3a-39e8-98b0-1469ca27bdda | -10.7916 | -48.7377 | 2026-09-28 14:10:00 | GOES-19 | PORTO NACIONAL | TOCANTINS | Brasil | 1718204 | 17 | 33 | nan | nan | nan | Cerrado | 85.2 |
| a886eca2-047b-3ba5-961d-f15078a7d62c | -12.4351 | -44.1497 | 2026-09-28 14:10:00 | GOES-19 | TABOCAS DO BREJO VELHO | BAHIA | Brasil | 2930907 | 29 | 33 | nan | nan | nan | Cerrado | 138.8 |
| 74400d88-8d4b-3353-a378-75caa6d28a74 | -10.7343 | -48.7661 | 2026-09-28 14:10:00 | GOES-19 | PORTO NACIONAL | TOCANTINS | Brasil | 1718204 | 17 | 33 | nan | nan | nan | Cerrado | 76.0 |
| c699e991-3082-38ca-b1e0-7537198046c6 | -12.2311 | -50.3643 | 2026-09-28 14:10:00 | GOES-19 | FORMOSO DO ARAGUAIA | TOCANTINS | Brasil | 1708205 | 17 | 33 | nan | nan | nan | Cerrado | 77.9 |
| b2172af2-3fa9-39b7-a527-813b12db61df | 1.6566 | -55.9227 | 2026-09-28 14:10:00 | GOES-19 | ORIXIMINÁ | PARÁ | Brasil | 1505304 | 15 | 33 | nan | nan | nan | Amazônia | 93.2 |
| 9d546d47-a75b-3bb5-99a8-e0eaacf73816 | -11.1958 | -44.8269 | 2026-09-28 14:10:00 | GOES-19 | SANTA RITA DE CÁSSIA | BAHIA | Brasil | 2928406 | 29 | 33 | nan | nan | nan | Cerrado | 110.1 |
| 54e8c1ab-2947-3c0a-b8ed-6f7b7938e1e6 | -7.7086 | -44.92 | 2026-09-28 14:10:00 | GOES-19 | URUÇUÍ | PIAUÍ | Brasil | 2211209 | 22 | 33 | nan | nan | nan | Cerrado | 184.7 |
| 2a60d225-9068-3db8-8528-6fb537c557e9 | -8.2862 | -45.409 | 2026-09-28 14:10:00 | GOES-19 | BAIXA GRANDE DO RIBEIRO | PIAUÍ | Brasil | 2201150 | 22 | 33 | nan | nan | nan | Cerrado | 101.8 |
| d3c86670-7724-39d0-9559-c5728de60bc7 | -11.8644 | -47.078 | 2026-09-28 14:10:00 | GOES-19 | DIANÓPOLIS | TOCANTINS | Brasil | 1707009 | 17 | 33 | nan | nan | nan | Cerrado | 102.6 |
| 29c9c9f9-c80c-389f-9937-37c247e16a20 | -12.1547 | -50.3735 | 2026-09-28 14:10:00 | GOES-19 | FORMOSO DO ARAGUAIA | TOCANTINS | Brasil | 1708205 | 17 | 33 | nan | nan | nan | Cerrado | 72.5 |
| ca428a75-d4fa-301e-bff9-0db723e6a377 | -10.2067 | -49.9898 | 2026-09-28 14:10:00 | GOES-19 | PIUM | TOCANTINS | Brasil | 1717503 | 17 | 33 | nan | nan | nan | Cerrado | 125.2 |
| ea46b824-bfc9-3c4b-a81f-43e3f4f595b3 | -7.4869 | -44.5751 | 2026-09-28 14:10:00 | GOES-19 | URUÇUÍ | PIAUÍ | Brasil | 2211209 | 22 | 33 | nan | nan | nan | Cerrado | 118.0 |
| e1977f00-f6ce-3239-b461-230356ab6eae | -10.8189 | -57.1993 | 2026-09-28 14:10:00 | GOES-19 | JUARA | MATO GROSSO | Brasil | 5105101 | 51 | 33 | nan | nan | nan | Amazônia | 82.8 |
| 81196f73-65b1-370d-a101-29afd595b1a4 | -15.4003 | -47.9035 | 2026-09-28 14:10:00 | GOES-19 | PLANALTINA | GOIÁS | Brasil | 5217609 | 52 | 33 | nan | nan | nan | Cerrado | 61.6 |
| c4ab21e3-df6f-313d-9708-eb73fbc7705e | -13.161 | -48.5437 | 2026-09-28 14:10:00 | GOES-19 | JAÚ DO TOCANTINS | TOCANTINS | Brasil | 1711506 | 17 | 33 | nan | nan | nan | Cerrado | 141.7 |
| 37ed7a10-b30b-31ea-827d-e034ae4df8d3 | 1.62 | -55.9035 | 2026-09-28 14:10:00 | GOES-19 | ORIXIMINÁ | PARÁ | Brasil | 1505304 | 15 | 33 | nan | nan | nan | Amazônia | 95.8 |
| 5fe0b6c2-b0f9-3b57-be9d-49a133f07399 | 1.6749 | -55.9225 | 2026-09-28 14:10:00 | GOES-19 | ORIXIMINÁ | PARÁ | Brasil | 1505304 | 15 | 33 | nan | nan | nan | Amazônia | 88.2 |
| fdb548c0-6fe3-3a8e-8a03-f715f65e6682 | -12.3088 | -50.2688 | 2026-09-28 14:10:00 | GOES-19 | FORMOSO DO ARAGUAIA | TOCANTINS | Brasil | 1708205 | 17 | 33 | nan | nan | nan | Cerrado | 258.4 |
| ef53d5d6-58cd-3768-993d-e9009a86d306 | -12.6451 | -47.3272 | 2026-09-28 14:10:00 | GOES-19 | PARANÃ | TOCANTINS | Brasil | 1716208 | 17 | 33 | nan | nan | nan | Cerrado | 147.7 |
| 03389f87-b1b3-3718-a982-67a75844ebe0 | -12.6259 | -47.33 | 2026-09-28 14:10:00 | GOES-19 | PARANÃ | TOCANTINS | Brasil | 1716208 | 17 | 33 | nan | nan | nan | Cerrado | 95.4 |
| 56102259-40b2-3e65-8413-c43f2c8f877c | -12.2307 | -50.3858 | 2026-09-28 14:10:00 | GOES-19 | FORMOSO DO ARAGUAIA | TOCANTINS | Brasil | 1708205 | 17 | 33 | nan | nan | nan | Cerrado | 71.0 |
| bd292f3d-fc02-3636-a5f3-998457d0772d | -10.872 | -54.0899 | 2026-09-28 14:10:00 | GOES-19 | MARCELÂNDIA | MATO GROSSO | Brasil | 5105580 | 51 | 33 | nan | nan | nan | Amazônia | 68.7 |
| fc35df5d-a8cc-3394-8c01-84304d34b7aa | -11.0991 | -54.0285 | 2026-09-28 14:10:00 | GOES-19 | MARCELÂNDIA | MATO GROSSO | Brasil | 5105580 | 51 | 33 | nan | nan | nan | Amazônia | 74.3 |
| 4c326631-fbba-3e3a-abb3-c713b366947a | -7.4492 | -44.5786 | 2026-09-28 14:10:00 | GOES-19 | URUÇUÍ | PIAUÍ | Brasil | 2211209 | 22 | 33 | nan | nan | nan | Cerrado | 107.1 |
| 53886c7f-874e-398b-b6df-4b1174ea6f90 | -12.7223 | -50.6905 | 2026-09-28 14:10:00 | GOES-19 | COCALINHO | MATO GROSSO | Brasil | 5103106 | 51 | 33 | nan | nan | nan | Cerrado | 69.1 |
| 64fc32f0-1b0a-3997-b540-ac1b16b71a08 | -14.7736 | -41.1424 | 2026-09-28 14:10:00 | GOES-19 | ANAGÉ | BAHIA | Brasil | 2901205 | 29 | 33 | nan | nan | nan | Caatinga | 293.1 |
| d153df21-3670-36a0-aa56-d61c67265232 | -14.7742 | -41.1173 | 2026-09-28 14:10:00 | GOES-19 | ANAGÉ | BAHIA | Brasil | 2901205 | 29 | 33 | nan | nan | nan | Caatinga | 107.9 |
| 4a2f58f4-5622-3764-ad70-ab03ee59de0b | -13.1606 | -48.5658 | 2026-09-28 14:10:00 | GOES-19 | JAÚ DO TOCANTINS | TOCANTINS | Brasil | 1711506 | 17 | 33 | nan | nan | nan | Cerrado | 128.0 |
| 02ee6694-468b-3fc6-95fb-66ff86899a0d | -8.2293 | -45.4375 | 2026-09-28 14:10:00 | GOES-19 | RIBEIRO GONÇALVES | PIAUÍ | Brasil | 2208908 | 22 | 33 | nan | nan | nan | Cerrado | 124.7 |
| 58e51356-0fbf-39fb-9d65-bb9967acd640 | -10.7114 | -60.7505 | 2026-09-28 14:10:00 | GOES-19 | RONDOLÂNDIA | MATO GROSSO | Brasil | 5107578 | 51 | 33 | nan | nan | nan | Amazônia | 56.5 |
| d4e6e657-5384-3355-9b8d-5c8a0dd55c3d | -10.2257 | -49.9879 | 2026-09-28 14:10:00 | GOES-19 | PIUM | TOCANTINS | Brasil | 1717503 | 17 | 33 | nan | nan | nan | Cerrado | 90.4 |
| 2d66a7b4-5e73-33bc-9327-054a7e666ece | -11.924 | -50.5081 | 2026-09-28 14:10:00 | GOES-19 | FORMOSO DO ARAGUAIA | TOCANTINS | Brasil | 1708205 | 17 | 33 | nan | nan | nan | Cerrado | 68.5 |
| 02e8e99d-0eef-30a1-b197-54691a7005f9 | -11.8672 | -50.4933 | 2026-09-28 14:10:00 | GOES-19 | FORMOSO DO ARAGUAIA | TOCANTINS | Brasil | 1708205 | 17 | 33 | nan | nan | nan | Cerrado | 83.9 |
| abd47102-ba9c-3c73-829d-f3916f5b9579 | 1.6383 | -55.9033 | 2026-09-28 14:10:00 | GOES-19 | ORIXIMINÁ | PARÁ | Brasil | 1505304 | 15 | 33 | nan | nan | nan | Amazônia | 89.1 |


[Clique aqui para ver as próximas entradas](README78.md)
