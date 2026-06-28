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

## Dados Diários - Página 6

| ID | Latitude | Longitude | Data/Hora GMT | Satélite | Município | Estado | País | Município ID | Estado ID | País ID | Dias sem Chuva | Precipitação | Risco de Fogo | Bioma | FRP |
|----|----------|-----------|---------------|----------|-----------|--------|------|--------------|-----------|---------|----------------|--------------|----------------|-------|-----|
| 0497c9f5-37dc-3317-83b6-2b477630a1a8 | -12.4528 | -58.477901 | 2026-06-28 01:00:00 | METOP-C | SAPEZAL | MATO GROSSO | Brasil | 5107875 | 51 | 33 | nan | nan | nan | Cerrado | nan |
| 4a8abb6b-6c39-398a-9104-c062a4066a40 | -12.1941 | -52.896198 | 2026-06-28 01:00:00 | METOP-C | QUERÊNCIA | MATO GROSSO | Brasil | 5107065 | 51 | 33 | nan | nan | nan | Amazônia | nan |
| 2173ef74-da43-359e-9047-a92c17929096 | -11.2182 | -54.293098 | 2026-06-28 01:00:00 | METOP-C | MARCELÂNDIA | MATO GROSSO | Brasil | 5105580 | 51 | 33 | nan | nan | nan | Amazônia | nan |
| 407dbc17-a94b-3e1d-a3af-ff56c97e0bfe | -11.2116 | -54.310001 | 2026-06-28 01:00:00 | METOP-C | MARCELÂNDIA | MATO GROSSO | Brasil | 5105580 | 51 | 33 | nan | nan | nan | Amazônia | nan |
| d24c50e0-11c5-3401-8968-0bd651fd415a | -12.1859 | -52.905399 | 2026-06-28 01:00:00 | METOP-C | QUERÊNCIA | MATO GROSSO | Brasil | 5107065 | 51 | 33 | nan | nan | nan | Amazônia | nan |
| 8821fefb-6b59-34d3-a0b5-4b79a5d86066 | -12.2381 | -56.5518 | 2026-06-28 01:00:00 | METOP-C | ITANHANGÁ | MATO GROSSO | Brasil | 5104542 | 51 | 33 | nan | nan | nan | Amazônia | nan |
| 96f5dabc-d825-37d9-b415-c0ddc2fa7fd2 | -18.4778 | -54.0989 | 2026-06-28 01:00:00 | METOP-C | COXIM | MATO GROSSO DO SUL | Brasil | 5003306 | 50 | 33 | nan | nan | nan | Cerrado | nan |
| 57b12a59-5719-3d7a-bede-c5fc007ff94b | -11.2132 | -54.317299 | 2026-06-28 01:00:00 | METOP-C | MARCELÂNDIA | MATO GROSSO | Brasil | 5105580 | 51 | 33 | nan | nan | nan | Amazônia | nan |
| 8d7096c2-a344-36ab-8033-918a3ba7a92f | -10.303 | -57.122898 | 2026-06-28 01:00:00 | METOP-C | NOVA MONTE VERDE | MATO GROSSO | Brasil | 5108956 | 51 | 33 | nan | nan | nan | Amazônia | nan |
| c952821f-924d-32ca-96b8-728929166ee0 | -12.2007 | -52.879902 | 2026-06-28 01:00:00 | METOP-C | QUERÊNCIA | MATO GROSSO | Brasil | 5107065 | 51 | 33 | nan | nan | nan | Amazônia | nan |
| df83795a-4d74-3066-b345-41592890c0d2 | -12.4579 | -58.502998 | 2026-06-28 01:00:00 | METOP-C | SAPEZAL | MATO GROSSO | Brasil | 5107875 | 51 | 33 | nan | nan | nan | Cerrado | nan |
| f9819f41-6d1a-3a0d-9da3-3d30dc5688c3 | -9.0862 | -59.383499 | 2026-06-28 01:00:00 | METOP-C | COLNIZA | MATO GROSSO | Brasil | 5103254 | 51 | 33 | nan | nan | nan | Amazônia | nan |
| 39427823-c1fc-32ef-a4d1-61068c24db79 | -12.1771 | -57.138599 | 2026-06-28 01:00:00 | METOP-C | NOVA MARINGÁ | MATO GROSSO | Brasil | 5108907 | 51 | 33 | nan | nan | nan | Amazônia | nan |
| 0de3d648-1e8b-3366-90f1-a263dff3f805 | -9.0916 | -59.409 | 2026-06-28 01:00:00 | METOP-C | COLNIZA | MATO GROSSO | Brasil | 5103254 | 51 | 33 | nan | nan | nan | Amazônia | nan |
| 07f9b6dc-69da-3dc9-a6bc-033de1aecb45 | -12.1694 | -57.150902 | 2026-06-28 01:00:00 | METOP-C | NOVA MARINGÁ | MATO GROSSO | Brasil | 5108907 | 51 | 33 | nan | nan | nan | Amazônia | nan |
| 05cce5e7-9fc5-390d-a48d-9d32f3932fc0 | -12.0838 | -51.995899 | 2026-06-28 01:00:00 | METOP-C | BOM JESUS DO ARAGUAIA | MATO GROSSO | Brasil | 5101852 | 51 | 33 | nan | nan | nan | Amazônia | nan |
| eee44126-20b8-397b-bd3b-967d694d90fc | -11.2169 | -53.822201 | 2026-06-28 01:00:00 | METOP-C | MARCELÂNDIA | MATO GROSSO | Brasil | 5105580 | 51 | 33 | nan | nan | nan | Amazônia | nan |
| 8a1b796b-4e38-3891-959b-bd56b54ed4b4 | -12.2361 | -56.5424 | 2026-06-28 01:00:00 | METOP-C | ITANHANGÁ | MATO GROSSO | Brasil | 5104542 | 51 | 33 | nan | nan | nan | Amazônia | nan |
| 0a2494c6-0503-3ade-97a6-ed5bff6d6e50 | -12.2023 | -52.886902 | 2026-06-28 01:00:00 | METOP-C | QUERÊNCIA | MATO GROSSO | Brasil | 5107065 | 51 | 33 | nan | nan | nan | Amazônia | nan |
| 5a6a56d1-348a-3adf-87ef-8565e06a6247 | -12.0854 | -52.002899 | 2026-06-28 01:00:00 | METOP-C | BOM JESUS DO ARAGUAIA | MATO GROSSO | Brasil | 5101852 | 51 | 33 | nan | nan | nan | Amazônia | nan |
| 71a4f8a0-f281-33d3-b89a-6cf623f563f0 | -12.1813 | -57.159 | 2026-06-28 01:00:00 | METOP-C | NOVA MARINGÁ | MATO GROSSO | Brasil | 5108907 | 51 | 33 | nan | nan | nan | Amazônia | nan |
| 3f931124-8646-3764-b0f2-5327ff950c49 | -12.1843 | -52.898399 | 2026-06-28 01:00:00 | METOP-C | QUERÊNCIA | MATO GROSSO | Brasil | 5107065 | 51 | 33 | nan | nan | nan | Amazônia | nan |
| c2a69d3f-c387-37d7-be04-a81457474804 | -10.6395 | -50.519901 | 2026-06-28 01:00:00 | METOP-C | PIUM | TOCANTINS | Brasil | 1717503 | 17 | 33 | nan | nan | nan | Cerrado | nan |
| b8b0ce42-dce7-35ee-a162-dbb20adfa015 | -10.6413 | -50.527599 | 2026-06-28 01:00:00 | METOP-C | PIUM | TOCANTINS | Brasil | 1717503 | 17 | 33 | nan | nan | nan | Cerrado | nan |
| e2779001-bf7c-351b-8d17-4ce311e2f3a4 | -12.6042 | -57.872501 | 2026-06-28 01:00:00 | METOP-C | BRASNORTE | MATO GROSSO | Brasil | 5101902 | 51 | 33 | nan | nan | nan | Cerrado | nan |
| 2d52e9d4-c9e2-3cfa-8b23-dace765036b8 | -11.223 | -54.315102 | 2026-06-28 01:00:00 | METOP-C | MARCELÂNDIA | MATO GROSSO | Brasil | 5105580 | 51 | 33 | nan | nan | nan | Amazônia | nan |
| 378799e9-7c3d-3130-b318-e3a889b4dc4a | -12.1728 | -57.118198 | 2026-06-28 01:00:00 | METOP-C | NOVA MARINGÁ | MATO GROSSO | Brasil | 5108907 | 51 | 33 | nan | nan | nan | Amazônia | nan |
| ebc5aa7d-61bb-3e82-a381-40b814b3b34f | -12.1673 | -57.140598 | 2026-06-28 01:00:00 | METOP-C | NOVA MARINGÁ | MATO GROSSO | Brasil | 5108907 | 51 | 33 | nan | nan | nan | Amazônia | nan |
| 1cd5cbb3-53f3-3c6b-b1e4-655ec76df902 | -11.5308 | -54.7817 | 2026-06-28 01:00:00 | METOP-C | CLÁUDIA | MATO GROSSO | Brasil | 5103056 | 51 | 33 | nan | nan | nan | Amazônia | nan |
| 3741db52-256d-3b59-9d5a-fa72137ae390 | -12.4651 | -58.4884 | 2026-06-28 01:00:00 | METOP-C | SAPEZAL | MATO GROSSO | Brasil | 5107875 | 51 | 33 | nan | nan | nan | Cerrado | nan |
| cd925d75-6e38-30f2-bf68-e740ae100461 | -9.0818 | -59.410999 | 2026-06-28 01:00:00 | METOP-C | COLNIZA | MATO GROSSO | Brasil | 5103254 | 51 | 33 | nan | nan | nan | Amazônia | nan |
| 4b9c807d-90fe-305a-8b90-315457bc64f6 | -9.0889 | -59.396301 | 2026-06-28 01:00:00 | METOP-C | COLNIZA | MATO GROSSO | Brasil | 5103254 | 51 | 33 | nan | nan | nan | Amazônia | nan |
| 48c81fd1-5f38-3c7a-a711-7b56683ff20c | -17.706301 | -46.774799 | 2026-06-28 01:00:00 | METOP-C | VAZANTE | MINAS GERAIS | Brasil | 3171006 | 31 | 33 | nan | nan | nan | Cerrado | nan |
| f156f1dd-fc0f-3b2c-8a01-7fc590349aa2 | -18.491199 | -54.113899 | 2026-06-28 01:00:00 | METOP-C | COXIM | MATO GROSSO DO SUL | Brasil | 5003306 | 50 | 33 | nan | nan | nan | Cerrado | nan |
| e68405fd-c076-3dcb-86d1-b36afb0ef95d | -12.1926 | -52.889198 | 2026-06-28 01:00:00 | METOP-C | QUERÊNCIA | MATO GROSSO | Brasil | 5107065 | 51 | 33 | nan | nan | nan | Amazônia | nan |
| 93e4f162-df69-32ba-8c05-d782f2c9234d | -17.708599 | -40.153801 | 2026-06-28 01:00:00 | METOP-C | IBIRAPUÃ | BAHIA | Brasil | 2912806 | 29 | 33 | nan | nan | nan | Mata Atlântica | nan |
| 1ca15b56-2027-38a1-b5bc-14012ce4fea3 | -12.7957 | -54.888199 | 2026-06-28 01:00:00 | METOP-C | NOVA UBIRATÃ | MATO GROSSO | Brasil | 5106240 | 51 | 33 | nan | nan | nan | Amazônia | nan |
| 61cc5ede-359b-399d-9fc8-b28200629b59 | -17.3048 | -42.634899 | 2026-06-28 01:00:00 | METOP-C | MINAS NOVAS | MINAS GERAIS | Brasil | 3141801 | 31 | 33 | nan | nan | nan | Cerrado | nan |
| 4ba0648e-878b-3cc3-bcb2-e5006c1b8e3a | -16.045601 | -50.553902 | 2026-06-28 01:00:00 | METOP-C | NOVO BRASIL | GOIÁS | Brasil | 5215207 | 52 | 33 | nan | nan | nan | Cerrado | nan |
| 19c14022-776d-38b7-9174-fd6abd336d09 | -11.9186 | -58.652901 | 2026-06-28 01:00:00 | METOP-C | JUÍNA | MATO GROSSO | Brasil | 5105150 | 51 | 33 | nan | nan | nan | Cerrado | nan |
| e0a4c105-9da7-3434-bd87-a0c703d31442 | -12.087 | -52.009899 | 2026-06-28 01:00:00 | METOP-C | BOM JESUS DO ARAGUAIA | MATO GROSSO | Brasil | 5101852 | 51 | 33 | nan | nan | nan | Amazônia | nan |
| a09930ec-67b9-30ac-93fe-320280fd246e | -12.196 | -52.858799 | 2026-06-28 01:00:00 | METOP-C | QUERÊNCIA | MATO GROSSO | Brasil | 5107065 | 51 | 33 | nan | nan | nan | Amazônia | nan |
| cc76c758-f24d-3d19-98f0-9580d99d6629 | -12.191 | -52.882198 | 2026-06-28 01:00:00 | METOP-C | QUERÊNCIA | MATO GROSSO | Brasil | 5107065 | 51 | 33 | nan | nan | nan | Amazônia | nan |
| 2614e65f-87cf-3a34-b3e8-d42e88a60858 | -12.1 | -52.021599 | 2026-06-28 01:00:00 | METOP-C | BOM JESUS DO ARAGUAIA | MATO GROSSO | Brasil | 5101852 | 51 | 33 | nan | nan | nan | Amazônia | nan |
| a3043e51-07e9-3c7e-9c3f-338c73b23a07 | -10.3009 | -57.1133 | 2026-06-28 01:00:00 | METOP-C | NOVA MONTE VERDE | MATO GROSSO | Brasil | 5108956 | 51 | 33 | nan | nan | nan | Amazônia | nan |
| dd15e387-3bea-39b8-a671-7c047cb92bc6 | -12.2755 | -50.098499 | 2026-06-28 01:00:00 | METOP-C | SANDOLÂNDIA | TOCANTINS | Brasil | 1718840 | 17 | 33 | nan | nan | nan | Cerrado | nan |
| f23e82b8-b7b0-39dc-b860-4bb28c415d77 | -12.5945 | -57.874599 | 2026-06-28 01:00:00 | METOP-C | BRASNORTE | MATO GROSSO | Brasil | 5101902 | 51 | 33 | nan | nan | nan | Cerrado | nan |
| a415ccb1-5945-3954-98b6-faba751074bf | -12.1745 | -52.9006 | 2026-06-28 01:00:00 | METOP-C | QUERÊNCIA | MATO GROSSO | Brasil | 5107065 | 51 | 33 | nan | nan | nan | Amazônia | nan |
| f387b6f7-6e57-34e7-a90b-9516be207c7d | -10.3071 | -57.141998 | 2026-06-28 01:00:00 | METOP-C | NOVA MONTE VERDE | MATO GROSSO | Brasil | 5108956 | 51 | 33 | nan | nan | nan | Amazônia | nan |
| 8dd6ebab-17aa-3623-8958-618ac4033131 | -11.2198 | -54.3004 | 2026-06-28 01:00:00 | METOP-C | MARCELÂNDIA | MATO GROSSO | Brasil | 5105580 | 51 | 33 | nan | nan | nan | Amazônia | nan |
| dc7334e9-885b-3a0b-8f26-bfa3d01a3057 | -11.9037 | -57.101101 | 2026-06-28 01:00:00 | METOP-C | PORTO DOS GAÚCHOS | MATO GROSSO | Brasil | 5106802 | 51 | 33 | nan | nan | nan | Amazônia | nan |
| 8ab19bea-ef49-3e41-b639-85765f143812 | -10.2911 | -57.115398 | 2026-06-28 01:00:00 | METOP-C | NOVA MONTE VERDE | MATO GROSSO | Brasil | 5108956 | 51 | 33 | nan | nan | nan | Amazônia | nan |
| a8d01a28-13eb-35f1-97db-5797391364c1 | -11.91 | -57.131302 | 2026-06-28 01:00:00 | METOP-C | PORTO DOS GAÚCHOS | MATO GROSSO | Brasil | 5106802 | 51 | 33 | nan | nan | nan | Amazônia | nan |
| 6c68d0e7-e52b-38b3-b6b5-acadf83f3b8f | -12.163 | -57.1203 | 2026-06-28 01:00:00 | METOP-C | NOVA MARINGÁ | MATO GROSSO | Brasil | 5108907 | 51 | 33 | nan | nan | nan | Amazônia | nan |
| 2fa1413b-6ea3-3d7a-acc1-9afb53902c3d | -12.6065 | -57.883999 | 2026-06-28 01:00:00 | METOP-C | BRASNORTE | MATO GROSSO | Brasil | 5101902 | 51 | 33 | nan | nan | nan | Cerrado | nan |
| cbdc7180-6d5b-36fd-b28b-83d64efe8cfc | -12.6089 | -57.895599 | 2026-06-28 01:00:00 | METOP-C | BRASNORTE | MATO GROSSO | Brasil | 5101902 | 51 | 33 | nan | nan | nan | Cerrado | nan |
| f7d1e2c5-c8de-3fa4-b795-81ca0bd4884e | -10.9402 | -56.848099 | 2026-06-28 01:00:00 | METOP-C | JUARA | MATO GROSSO | Brasil | 5105101 | 51 | 33 | nan | nan | nan | Amazônia | nan |
| 8f1c71c2-57c7-32f7-81ae-15e55b88d978 | -10.7847 | -54.099701 | 2026-06-28 01:00:00 | METOP-C | MARCELÂNDIA | MATO GROSSO | Brasil | 5105580 | 51 | 33 | nan | nan | nan | Amazônia | nan |
| e944061a-778b-32f0-aaff-71f955ad6613 | -11.5324 | -54.789398 | 2026-06-28 01:00:00 | METOP-C | CLÁUDIA | MATO GROSSO | Brasil | 5103056 | 51 | 33 | nan | nan | nan | Amazônia | nan |
| f35272e1-338b-357b-b258-147cecf9a8a6 | -11.8841 | -57.105202 | 2026-06-28 01:00:00 | METOP-C | PORTO DOS GAÚCHOS | MATO GROSSO | Brasil | 5106802 | 51 | 33 | nan | nan | nan | Amazônia | nan |
| e6d9ee0a-e272-3591-9b90-93c6c730b209 | -11.9058 | -57.111099 | 2026-06-28 01:00:00 | METOP-C | PORTO DOS GAÚCHOS | MATO GROSSO | Brasil | 5106802 | 51 | 33 | nan | nan | nan | Amazônia | nan |
| 57662657-8205-3100-9b16-64af3f4bf50b | -12.1792 | -57.1488 | 2026-06-28 01:00:00 | METOP-C | NOVA MARINGÁ | MATO GROSSO | Brasil | 5108907 | 51 | 33 | nan | nan | nan | Amazônia | nan |
| c1c4ffcf-58d0-35d2-926c-eb9f15ba8714 | -9.5945 | -56.922501 | 2026-06-28 01:00:00 | METOP-C | PARANAÍTA | MATO GROSSO | Brasil | 5106299 | 51 | 33 | nan | nan | nan | Amazônia | nan |
| f2ba6732-bce3-3bf8-89a1-e83058aac326 | -12.1879 | -52.868099 | 2026-06-28 01:00:00 | METOP-C | QUERÊNCIA | MATO GROSSO | Brasil | 5107065 | 51 | 33 | nan | nan | nan | Amazônia | nan |
| 10e2b113-3a41-3289-a296-a3ac715496a9 | -12.1976 | -52.865799 | 2026-06-28 01:00:00 | METOP-C | QUERÊNCIA | MATO GROSSO | Brasil | 5107065 | 51 | 33 | nan | nan | nan | Amazônia | nan |
| 58ffa01e-e5bc-3a8e-8dff-91e78f2f9ea8 | -11.6705 | -57.256001 | 2026-06-28 01:00:00 | METOP-C | PORTO DOS GAÚCHOS | MATO GROSSO | Brasil | 5106802 | 51 | 33 | nan | nan | nan | Amazônia | nan |
| a8cce07f-bc7e-37d1-885a-2a637961bc6b | -12.1894 | -52.875099 | 2026-06-28 01:00:00 | METOP-C | QUERÊNCIA | MATO GROSSO | Brasil | 5107065 | 51 | 33 | nan | nan | nan | Amazônia | nan |
| 1fd65ba4-d60a-340f-8ddf-92437020b5fd | -4.2596 | -48.5383 | 2026-06-28 01:00:00 | METOP-C | RONDON DO PARÁ | PARÁ | Brasil | 1506187 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| 8c05ce49-4fd4-35c3-9ebd-5e71873e47be | -12.2263 | -56.544399 | 2026-06-28 01:00:00 | METOP-C | ITANHANGÁ | MATO GROSSO | Brasil | 5104542 | 51 | 33 | nan | nan | nan | Amazônia | nan |
| 78cd9f8c-808e-32b0-b341-e6a5b41b0009 | -12.209 | -52.870602 | 2026-06-28 01:00:00 | METOP-C | QUERÊNCIA | MATO GROSSO | Brasil | 5107065 | 51 | 33 | nan | nan | nan | Amazônia | nan |
| 80448433-7e25-3fc1-9b63-9509c2c4c658 | -17.703899 | -46.765099 | 2026-06-28 01:00:00 | METOP-C | VAZANTE | MINAS GERAIS | Brasil | 3171006 | 31 | 33 | nan | nan | nan | Cerrado | nan |
| 697f0d63-d401-3cdb-8b69-90c0eceb3077 | -12.5968 | -57.886101 | 2026-06-28 01:00:00 | METOP-C | BRASNORTE | MATO GROSSO | Brasil | 5101902 | 51 | 33 | nan | nan | nan | Cerrado | nan |
| 1f46b311-16a9-3c6d-9bd5-ce238e35e4a9 | -18.489401 | -54.105202 | 2026-06-28 01:00:00 | METOP-C | COXIM | MATO GROSSO DO SUL | Brasil | 5003306 | 50 | 33 | nan | nan | nan | Cerrado | nan |
| 9c7d8f28-4579-3c60-8c74-58c45b24ad45 | -12.2039 | -52.893902 | 2026-06-28 01:00:00 | METOP-C | QUERÊNCIA | MATO GROSSO | Brasil | 5107065 | 51 | 33 | nan | nan | nan | Amazônia | nan |
| ac7e75b6-74bd-3179-b473-9dad082cc99d | -11.9079 | -57.121201 | 2026-06-28 01:00:00 | METOP-C | PORTO DOS GAÚCHOS | MATO GROSSO | Brasil | 5106802 | 51 | 33 | nan | nan | nan | Amazônia | nan |
| 1c436bd1-3016-3f56-aedb-431b0d0c418c | -12.175 | -57.128399 | 2026-06-28 01:00:00 | METOP-C | NOVA MARINGÁ | MATO GROSSO | Brasil | 5108907 | 51 | 33 | nan | nan | nan | Amazônia | nan |
| 52356358-8304-30df-b765-4b1bd18280d8 | -11.6585 | -57.247898 | 2026-06-28 01:00:00 | METOP-C | PORTO DOS GAÚCHOS | MATO GROSSO | Brasil | 5106802 | 51 | 33 | nan | nan | nan | Amazônia | nan |
| 452d0ad7-c14f-3df0-8fb5-da9e594b5db6 | -10.2952 | -57.134499 | 2026-06-28 01:00:00 | METOP-C | NOVA MONTE VERDE | MATO GROSSO | Brasil | 5108956 | 51 | 33 | nan | nan | nan | Amazônia | nan |
| fcab7b59-2050-305b-a1f8-0af3db51f368 | -12.2773 | -50.106201 | 2026-06-28 01:00:00 | METOP-C | SANDOLÂNDIA | TOCANTINS | Brasil | 1718840 | 17 | 33 | nan | nan | nan | Cerrado | nan |
| 6ae218e7-79e5-331f-ac6f-8b419b3d00bc | -12.1992 | -52.872799 | 2026-06-28 01:00:00 | METOP-C | QUERÊNCIA | MATO GROSSO | Brasil | 5107065 | 51 | 33 | nan | nan | nan | Amazônia | nan |
| ae8c6ce1-9e2f-389e-830b-c16e0674f532 | -10.305 | -57.132401 | 2026-06-28 01:00:00 | METOP-C | NOVA MONTE VERDE | MATO GROSSO | Brasil | 5108956 | 51 | 33 | nan | nan | nan | Amazônia | nan |
| 26083790-8238-353f-b078-0f3cb92214f7 | -12.2074 | -52.863602 | 2026-06-28 01:00:00 | METOP-C | QUERÊNCIA | MATO GROSSO | Brasil | 5107065 | 51 | 33 | nan | nan | nan | Amazônia | nan |
| c1ec5035-d948-330b-b05d-36b1bc682e61 | -12.1828 | -52.891399 | 2026-06-28 01:00:00 | METOP-C | QUERÊNCIA | MATO GROSSO | Brasil | 5107065 | 51 | 33 | nan | nan | nan | Amazônia | nan |
| 08c30182-d909-3b64-8c57-77e9545dad5b | -12.0923 | -51.9966 | 2026-06-28 01:10:00 | GOES-19 | BOM JESUS DO ARAGUAIA | MATO GROSSO | Brasil | 5101852 | 51 | 33 | nan | nan | nan | Amazônia | 93.8 |
| 5a9f5e6b-ba59-3144-b36f-aedeb262a2af | -12.6046 | -57.8942 | 2026-06-28 01:10:00 | GOES-19 | BRASNORTE | MATO GROSSO | Brasil | 5101902 | 51 | 33 | nan | nan | nan | Cerrado | 71.4 |
| 704af6c8-489c-3262-b085-87f7aa4ba547 | -11.2093 | -54.2848 | 2026-06-28 01:10:00 | GOES-19 | MARCELÂNDIA | MATO GROSSO | Brasil | 5105580 | 51 | 33 | nan | nan | nan | Amazônia | 96.1 |
| 4ef65e3b-1989-321a-86ef-892d5d27ce4b | -11.2088 | -54.3258 | 2026-06-28 01:10:00 | GOES-19 | MARCELÂNDIA | MATO GROSSO | Brasil | 5105580 | 51 | 33 | nan | nan | nan | Amazônia | 77.2 |
| aad1b63c-178d-3a81-a5ee-b145ed00a5ac | -12.1773 | -57.1519 | 2026-06-28 01:10:00 | GOES-19 | NOVA MARINGÁ | MATO GROSSO | Brasil | 5108907 | 51 | 33 | nan | nan | nan | Amazônia | 52.8 |
| f10eab2c-d88a-335b-b3a4-f828b3abe0ef | -12.4654 | -58.481 | 2026-06-28 01:10:00 | GOES-19 | SAPEZAL | MATO GROSSO | Brasil | 5107875 | 51 | 33 | nan | nan | nan | Cerrado | 42.7 |
| ee06d705-873a-35b4-a504-099cd82780f2 | -12.1775 | -57.1319 | 2026-06-28 01:10:00 | GOES-19 | NOVA MARINGÁ | MATO GROSSO | Brasil | 5108907 | 51 | 33 | nan | nan | nan | Amazônia | 58.8 |
| b921ab8d-e0eb-391e-b313-8177b47d417d | -17.3041 | -42.643 | 2026-06-28 01:10:00 | GOES-19 | MINAS NOVAS | MINAS GERAIS | Brasil | 3141801 | 31 | 33 | nan | nan | nan | Cerrado | 64.8 |
| 58bab816-47ad-3848-9f60-80a9057e3b42 | -11.209 | -54.3053 | 2026-06-28 01:10:00 | GOES-19 | MARCELÂNDIA | MATO GROSSO | Brasil | 5105580 | 51 | 33 | nan | nan | nan | Amazônia | 268.8 |
| bf0adc02-d903-3fe6-80f3-ef1a5ab2efec | -10.2942 | -57.1182 | 2026-06-28 01:10:00 | GOES-19 | NOVA MONTE VERDE | MATO GROSSO | Brasil | 5108956 | 51 | 33 | nan | nan | nan | Amazônia | 99.9 |
| 31d23ff7-3fe1-3b11-a463-2419b0972ad5 | -12.4651 | -58.5009 | 2026-06-28 01:10:00 | GOES-19 | SAPEZAL | MATO GROSSO | Brasil | 5107875 | 51 | 33 | nan | nan | nan | Cerrado | 74.7 |
| cdd2e3b4-b7a5-3ed5-9200-0139fd4e2c62 | -12.092 | -52.0176 | 2026-06-28 01:10:00 | GOES-19 | BOM JESUS DO ARAGUAIA | MATO GROSSO | Brasil | 5101852 | 51 | 33 | nan | nan | nan | Amazônia | 205.9 |
| 15eddf6a-e0f9-37aa-b82a-68084c728962 | -9.0796 | -59.4098 | 2026-06-28 01:10:00 | GOES-19 | COLNIZA | MATO GROSSO | Brasil | 5103254 | 51 | 33 | nan | nan | nan | Amazônia | 68.7 |
| d0261297-aabf-377e-982f-306c0800ae3a | -11.6657 | -57.2536 | 2026-06-28 01:10:00 | GOES-19 | PORTO DOS GAÚCHOS | MATO GROSSO | Brasil | 5106802 | 51 | 33 | nan | nan | nan | Amazônia | 56.4 |
| 926a84fd-8024-39de-b9d4-a1f5ad1913fe | -11.2277 | -54.3241 | 2026-06-28 01:10:00 | GOES-19 | MARCELÂNDIA | MATO GROSSO | Brasil | 5105580 | 51 | 33 | nan | nan | nan | Amazônia | 58.3 |
| 5a6c7bdf-711d-311a-bb31-5aab6136d82b | -10.3128 | -57.1367 | 2026-06-28 01:10:00 | GOES-19 | JUARA | MATO GROSSO | Brasil | 5105101 | 51 | 33 | nan | nan | nan | Amazônia | 77.1 |
| 63dddaf0-a168-3657-9fa8-e1d1d97ae56b | -10.313 | -57.1169 | 2026-06-28 01:10:00 | GOES-19 | JUARA | MATO GROSSO | Brasil | 5105101 | 51 | 33 | nan | nan | nan | Amazônia | 68.8 |


[Clique aqui para ver as próximas entradas](README7.md)
