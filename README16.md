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

## Dados Diários - Página 16

| ID | Latitude | Longitude | Data/Hora GMT | Satélite | Município | Estado | País | Município ID | Estado ID | País ID | Dias sem Chuva | Precipitação | Risco de Fogo | Bioma | FRP |
|----|----------|-----------|---------------|----------|-----------|--------|------|--------------|-----------|---------|----------------|--------------|----------------|-------|-----|
| dba0ba45-66ba-3107-b9b7-1cd053649046 | -3.7391 | -46.00793 | 2025-12-01 04:25:00 | NOAA-20 | ALTO ALEGRE DO PINDARÉ | MARANHÃO | Brasil | 2100477 | 21 | 33 | nan | nan | nan | Amazônia | 2.2 |
| 27d7b6c5-0119-3bec-9c82-0ef125dc4143 | -4.39799 | -43.3299 | 2025-12-01 04:25:00 | NOAA-20 | ALDEIAS ALTAS | MARANHÃO | Brasil | 2100303 | 21 | 33 | nan | nan | nan | Cerrado | 10.9 |
| abc4a925-15eb-3653-ad75-7c6d0eacdaac | -2.25141 | -45.61443 | 2025-12-01 04:25:00 | NOAA-20 | TURILÂNDIA | MARANHÃO | Brasil | 2112456 | 21 | 33 | nan | nan | nan | Amazônia | 2.4 |
| d54b1568-4bf0-38f4-b43a-0ba49823ada3 | -3.62182 | -50.63022 | 2025-12-01 04:25:00 | NOAA-20 | PACAJÁ | PARÁ | Brasil | 1505486 | 15 | 33 | nan | nan | nan | Amazônia | 1.2 |
| 06bd757a-b2a2-32c7-b632-5483c6497181 | -3.57377 | -45.69971 | 2025-12-01 04:25:00 | NOAA-20 | BOM JARDIM | MARANHÃO | Brasil | 2102002 | 21 | 33 | nan | nan | nan | Amazônia | 0.6 |
| 718a2478-9f7d-39f2-8734-776145c2a870 | -3.7138 | -50.65652 | 2025-12-01 04:25:00 | NOAA-20 | PACAJÁ | PARÁ | Brasil | 1505486 | 15 | 33 | nan | nan | nan | Amazônia | 1.4 |
| 81a821bd-e90b-3e80-a362-9ccabf2de804 | -4.39739 | -43.33379 | 2025-12-01 04:25:00 | NOAA-20 | ALDEIAS ALTAS | MARANHÃO | Brasil | 2100303 | 21 | 33 | nan | nan | nan | Cerrado | 10.9 |
| a7c0c1f9-f3c6-32eb-8bf9-47c5d6b892de | -2.03991 | -46.6719 | 2025-12-01 04:25:00 | NOAA-20 | VISEU | PARÁ | Brasil | 1508308 | 15 | 33 | nan | nan | nan | Amazônia | 1.2 |
| cce9b4aa-6e8f-370b-956b-f7f8170c8a8f | -3.71435 | -50.65307 | 2025-12-01 04:25:00 | NOAA-20 | PACAJÁ | PARÁ | Brasil | 1505486 | 15 | 33 | nan | nan | nan | Amazônia | 1.4 |
| 38b30f37-9c25-3e2b-b5ad-da22620a6b91 | -4.38072 | -43.15906 | 2025-12-01 04:25:00 | NOAA-20 | COELHO NETO | MARANHÃO | Brasil | 2103406 | 21 | 33 | nan | nan | nan | Cerrado | 12.8 |
| c51ee023-98dc-3abf-bde0-6772a9aeff6c | -4.5794 | -45.9779 | 2025-12-01 04:25:00 | NOAA-20 | SANTA LUZIA | MARANHÃO | Brasil | 2110005 | 21 | 33 | nan | nan | nan | Amazônia | 0.9 |
| 4384e171-99f7-34e1-9d82-41e58eae5eee | -0.93212 | -47.48849 | 2025-12-01 04:25:00 | NOAA-20 | MARACANÃ | PARÁ | Brasil | 1504307 | 15 | 33 | nan | nan | nan | Amazônia | 1.0 |
| 558a790b-7a1c-31e7-b623-ed299a4be5e1 | -2.6432 | -48.54995 | 2025-12-01 04:25:00 | NOAA-20 | TAILÂNDIA | PARÁ | Brasil | 1507953 | 15 | 33 | nan | nan | nan | Amazônia | 2.4 |
| 6e71f53b-829d-3735-a6fd-9038274329a4 | -2.44745 | -49.00513 | 2025-12-01 04:25:00 | NOAA-20 | MOJU | PARÁ | Brasil | 1504703 | 15 | 33 | nan | nan | nan | Amazônia | 2.1 |
| 80aee5e2-f7a1-36fa-89f2-f91e185e0334 | -3.59643 | -47.27098 | 2025-12-01 04:25:00 | NOAA-20 | ULIANÓPOLIS | PARÁ | Brasil | 1508126 | 15 | 33 | nan | nan | nan | Amazônia | 9.6 |
| 0b5869fb-374e-3792-8ac8-31decafee978 | -3.69088 | -50.62093 | 2025-12-01 04:25:00 | NOAA-20 | PACAJÁ | PARÁ | Brasil | 1505486 | 15 | 33 | nan | nan | nan | Amazônia | 1.8 |
| 6d5364c2-cc5f-34a3-9a8c-04863eae171b | -3.50397 | -44.21682 | 2025-12-01 04:25:00 | NOAA-20 | ITAPECURU MIRIM | MARANHÃO | Brasil | 2105401 | 21 | 33 | nan | nan | nan | Cerrado | 0.9 |
| 730c2f4e-5426-3a25-82df-046b2052f29c | -3.23326 | -50.24715 | 2025-12-01 04:25:00 | NOAA-20 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 2.1 |
| 242160da-6492-397d-a5dc-2a4d9f68f772 | -5.52188 | -42.60571 | 2025-12-01 04:25:00 | NOAA-20 | MONSENHOR GIL | PIAUÍ | Brasil | 2206407 | 22 | 33 | nan | nan | nan | Caatinga | 0.8 |
| a959f733-a9d3-30b0-9969-82af2bb1d3ba | -5.26778 | -42.70248 | 2025-12-01 04:25:00 | NOAA-20 | TERESINA | PIAUÍ | Brasil | 2211001 | 22 | 33 | nan | nan | nan | Caatinga | 0.8 |
| 8cd47400-fef0-332e-abf5-6be7bc0c857f | -3.22124 | -50.32209 | 2025-12-01 04:25:00 | NOAA-20 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 1.8 |
| b59e6c46-88c8-315c-a158-6427f91973ec | -2.90382 | -46.81771 | 2025-12-01 04:25:00 | NOAA-20 | PARAGOMINAS | PARÁ | Brasil | 1505502 | 15 | 33 | nan | nan | nan | Amazônia | 0.7 |
| 4e3f7966-121b-3506-91e9-76f7c15c66da | -3.17477 | -50.30938 | 2025-12-01 04:25:00 | NOAA-20 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 1.0 |
| f7ab6495-98cc-36c3-a8a2-f25359560d00 | -3.23247 | -50.67035 | 2025-12-01 04:25:00 | NOAA-20 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 2.6 |
| fce0dc66-42e0-3658-a61e-0c04315d1b85 | -6.31672 | -43.81268 | 2025-12-01 04:25:00 | NOAA-20 | SÃO JOÃO DOS PATOS | MARANHÃO | Brasil | 2111102 | 21 | 33 | nan | nan | nan | Cerrado | 0.8 |
| bdbb2347-61bb-3a9d-97fe-1e509a34a8a4 | -2.59729 | -49.25932 | 2025-12-01 04:25:00 | NOAA-20 | MOJU | PARÁ | Brasil | 1504703 | 15 | 33 | nan | nan | nan | Amazônia | 1.0 |
| e1467259-168f-34ff-b347-f64593dfe20f | -4.59804 | -45.21373 | 2025-12-01 04:25:00 | NOAA-20 | PAULO RAMOS | MARANHÃO | Brasil | 2108108 | 21 | 33 | nan | nan | nan | Amazônia | 2.3 |
| 654dd994-d85e-32b5-993d-024ead3b05f5 | -4.14481 | -43.72422 | 2025-12-01 04:25:00 | NOAA-20 | TIMBIRAS | MARANHÃO | Brasil | 2112100 | 21 | 33 | nan | nan | nan | Cerrado | 0.6 |
| fba81bfb-f34e-3da8-a31d-b0dfbb884e32 | -2.04652 | -52.10373 | 2025-12-01 04:25:00 | NOAA-20 | PORTO DE MOZ | PARÁ | Brasil | 1505908 | 15 | 33 | nan | nan | nan | Amazônia | 2.3 |
| 20369fd7-2e0a-3a65-aad6-d7f36c55228b | -2.31258 | -53.85382 | 2025-12-01 04:25:00 | NOAA-20 | PRAINHA | PARÁ | Brasil | 1506005 | 15 | 33 | nan | nan | nan | Amazônia | 1.8 |
| cbda3980-4371-329c-8eda-cb0581bf536b | -5.33188 | -43.56148 | 2025-12-01 04:25:00 | NOAA-20 | MATÕES | MARANHÃO | Brasil | 2106607 | 21 | 33 | nan | nan | nan | Cerrado | 20.5 |
| 316a4374-a5e6-3003-a711-397ceb5dcaee | -4.39157 | -43.32489 | 2025-12-01 04:25:00 | NOAA-20 | ALDEIAS ALTAS | MARANHÃO | Brasil | 2100303 | 21 | 33 | nan | nan | nan | Cerrado | 0.8 |
| 113f10a9-a745-3267-b0eb-38cdd6ffc173 | -1.4128 | -48.95935 | 2025-12-01 04:25:00 | NOAA-20 | PONTA DE PEDRAS | PARÁ | Brasil | 1505700 | 15 | 33 | nan | nan | nan | Amazônia | 0.7 |
| fbb2ecd6-3c2a-34b3-8f5d-d9b96c1656cc | -4.25368 | -44.33098 | 2025-12-01 04:25:00 | NOAA-20 | ALTO ALEGRE DO MARANHÃO | MARANHÃO | Brasil | 2100436 | 21 | 33 | nan | nan | nan | Cerrado | 1.4 |
| 75f68d91-fdba-3fec-b207-755c0aa0fa76 | -2.18427 | -48.24465 | 2025-12-01 04:25:00 | NOAA-20 | ACARÁ | PARÁ | Brasil | 1500206 | 15 | 33 | nan | nan | nan | Amazônia | 0.9 |
| 1fa2473b-4b89-39da-96bf-253b2ae8bb3d | -4.60082 | -45.2177 | 2025-12-01 04:25:00 | NOAA-20 | PAULO RAMOS | MARANHÃO | Brasil | 2108108 | 21 | 33 | nan | nan | nan | Amazônia | 2.3 |
| f11f0f57-5d48-36f6-8a88-df3d74734369 | -6.99151 | -38.69268 | 2025-12-01 04:25:00 | NOAA-20 | CACHOEIRA DOS ÍNDIOS | PARAÍBA | Brasil | 2503308 | 25 | 33 | nan | nan | nan | Caatinga | 1.1 |
| 3744ac04-1276-30d5-a6bd-c6df4974a76c | -6.31261 | -43.81608 | 2025-12-01 04:25:00 | NOAA-20 | SÃO JOÃO DOS PATOS | MARANHÃO | Brasil | 2111102 | 21 | 33 | nan | nan | nan | Cerrado | 9.2 |
| 2b6de3cb-247f-30c6-9988-684be36d07f2 | -4.36782 | -43.14896 | 2025-12-01 04:25:00 | NOAA-20 | COELHO NETO | MARANHÃO | Brasil | 2103406 | 21 | 33 | nan | nan | nan | Cerrado | 2.0 |
| d132fab4-b30b-375e-afd4-c71b3bbc38af | -3.22333 | -50.5754 | 2025-12-01 04:25:00 | NOAA-20 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 0.4 |
| 5ccc9173-6cbe-3953-b871-10c50ebb937c | -6.35659 | -43.98042 | 2025-12-01 04:25:00 | NOAA-20 | PARAIBANO | MARANHÃO | Brasil | 2107704 | 21 | 33 | nan | nan | nan | Cerrado | 1.4 |
| 44f53a21-1882-3d75-8f55-f0f918a498b4 | -2.57343 | -49.10164 | 2025-12-01 04:25:00 | NOAA-20 | MOJU | PARÁ | Brasil | 1504703 | 15 | 33 | nan | nan | nan | Amazônia | 1.7 |
| 3f29f986-bd6f-3c70-9c03-74c8f199cdbd | -4.59583 | -45.93816 | 2025-12-01 04:25:00 | NOAA-20 | SANTA LUZIA | MARANHÃO | Brasil | 2110005 | 21 | 33 | nan | nan | nan | Amazônia | 0.7 |
| e247dfbb-7ee8-31a4-9bb3-661de2d0bbfd | -2.83918 | -48.82906 | 2025-12-01 04:25:00 | NOAA-20 | TAILÂNDIA | PARÁ | Brasil | 1507953 | 15 | 33 | nan | nan | nan | Amazônia | 4.7 |
| b30fbd10-e751-3e32-a925-06f479cd2c62 | -14.05109 | -42.65168 | 2025-12-01 04:27:00 | NOAA-20 | CAETITÉ | BAHIA | Brasil | 2905206 | 29 | 33 | nan | nan | nan | Caatinga | 1.3 |
| 0eb72f80-4eba-327a-af99-a3fbdd0447c4 | -14.93939 | -44.55529 | 2025-12-01 04:27:00 | NOAA-20 | CÔNEGO MARINHO | MINAS GERAIS | Brasil | 3117836 | 31 | 33 | nan | nan | nan | Cerrado | 0.8 |
| 6af5a1cc-9ed0-34bb-ab47-9cb3a8c6cb34 | -14.42888 | -44.84264 | 2025-12-01 04:27:00 | NOAA-20 | COCOS | BAHIA | Brasil | 2908101 | 29 | 33 | nan | nan | nan | Cerrado | 2.3 |
| 5a0754a0-c789-3066-8041-ae36a2593fde | -10.5617 | -48.20941 | 2025-12-01 04:27:00 | NOAA-20 | MONTE DO CARMO | TOCANTINS | Brasil | 1713601 | 17 | 33 | nan | nan | nan | Cerrado | 1.5 |
| d12cb0c4-1e81-347b-8c8b-4defa0286bb2 | -12.00675 | -49.264 | 2025-12-01 04:27:00 | NOAA-20 | CARIRI DO TOCANTINS | TOCANTINS | Brasil | 1703867 | 17 | 33 | nan | nan | nan | Cerrado | 3.7 |
| 4cd24912-1fb9-3ba3-9b66-3eb4a6d915a6 | -15.09045 | -50.3423 | 2025-12-01 04:27:00 | NOAA-20 | ARAGUAPAZ | GOIÁS | Brasil | 5202155 | 52 | 33 | nan | nan | nan | Cerrado | 0.9 |
| 408973b8-7220-33cb-934b-335091526f1a | -13.7227 | -48.73834 | 2025-12-01 04:27:00 | NOAA-20 | CAMPINORTE | GOIÁS | Brasil | 5204706 | 52 | 33 | nan | nan | nan | Cerrado | 1.0 |
| ff610e25-2c8e-3f04-aeee-47668af4e8a0 | -11.36043 | -54.34936 | 2025-12-01 04:27:00 | NOAA-20 | UNIÃO DO SUL | MATO GROSSO | Brasil | 5108303 | 51 | 33 | nan | nan | nan | Amazônia | 1.0 |
| 9abb6516-85c9-3e3e-b52d-4230eeed8fef | -15.09387 | -50.34289 | 2025-12-01 04:27:00 | NOAA-20 | ARAGUAPAZ | GOIÁS | Brasil | 5202155 | 52 | 33 | nan | nan | nan | Cerrado | 0.9 |
| ec6c9650-cbbb-31e9-8971-9c47b694bdfe | -12.01393 | -49.26791 | 2025-12-01 04:27:00 | NOAA-20 | CARIRI DO TOCANTINS | TOCANTINS | Brasil | 1703867 | 17 | 33 | nan | nan | nan | Cerrado | 5.8 |
| 11632d21-ff99-3506-bd67-850b3f15444e | -12.00336 | -49.26342 | 2025-12-01 04:27:00 | NOAA-20 | CARIRI DO TOCANTINS | TOCANTINS | Brasil | 1703867 | 17 | 33 | nan | nan | nan | Cerrado | 0.4 |
| 16d0f06f-454b-3a7d-b732-15530cf83b4c | -13.48425 | -46.7094 | 2025-12-01 04:27:00 | NOAA-20 | SÃO DOMINGOS | GOIÁS | Brasil | 5219803 | 52 | 33 | nan | nan | nan | Cerrado | 1.1 |
| d5d1f929-8fc3-3677-ae35-e4ba34952a7b | -10.14064 | -36.1518 | 2025-12-01 04:27:00 | NOAA-20 | CORURIPE | ALAGOAS | Brasil | 2702306 | 27 | 33 | nan | nan | nan | Mata Atlântica | 43.7 |
| 805c969b-ee8b-325f-962e-a46b090e9354 | -13.48705 | -46.71358 | 2025-12-01 04:27:00 | NOAA-20 | SÃO DOMINGOS | GOIÁS | Brasil | 5219803 | 52 | 33 | nan | nan | nan | Cerrado | 1.1 |
| 55079ae1-0076-3438-9cb8-fa81e56fc51b | -12.01454 | -49.26423 | 2025-12-01 04:27:00 | NOAA-20 | CARIRI DO TOCANTINS | TOCANTINS | Brasil | 1703867 | 17 | 33 | nan | nan | nan | Cerrado | 2.2 |
| 274734e3-7ade-34a3-b7f8-350e33bbcbc6 | -13.03291 | -40.05439 | 2025-12-01 04:27:00 | NOAA-20 | NOVA ITARANA | BAHIA | Brasil | 2922805 | 29 | 33 | nan | nan | nan | Caatinga | 4.1 |
| c16e2a40-a8a2-35b8-b94a-7399bd43baf8 | -12.01332 | -49.27159 | 2025-12-01 04:27:00 | NOAA-20 | CARIRI DO TOCANTINS | TOCANTINS | Brasil | 1703867 | 17 | 33 | nan | nan | nan | Cerrado | 5.8 |
| fcdd7231-9416-32cc-9a5e-79382c817160 | -11.84093 | -43.857 | 2025-12-01 04:27:00 | NOAA-20 | WANDERLEY | BAHIA | Brasil | 2933455 | 29 | 33 | nan | nan | nan | Cerrado | 1.7 |
| 4d9689a8-ea3a-3938-9b1d-b1ef42e41b1a | -10.14228 | -36.13845 | 2025-12-01 04:27:00 | NOAA-20 | CORURIPE | ALAGOAS | Brasil | 2702306 | 27 | 33 | nan | nan | nan | Mata Atlântica | 3.5 |
| 7dc5e874-2ab2-3c1d-af92-3f48ee0df5ac | -14.42949 | -44.84093 | 2025-12-01 04:27:00 | NOAA-20 | COCOS | BAHIA | Brasil | 2908101 | 29 | 33 | nan | nan | nan | Cerrado | 1.7 |
| 45e79295-2e4a-34e3-bf47-6490267f2915 | -13.4714 | -44.54943 | 2025-12-01 04:27:00 | NOAA-20 | CORRENTINA | BAHIA | Brasil | 2909307 | 29 | 33 | nan | nan | nan | Cerrado | 3.3 |
| ba8f2594-8fc7-3532-a4c5-425842b5f9e6 | -13.03228 | -40.0508 | 2025-12-01 04:27:00 | NOAA-20 | NOVA ITARANA | BAHIA | Brasil | 2922805 | 29 | 33 | nan | nan | nan | Caatinga | 0.8 |
| a9fb61e4-a0fc-3fc0-9d8c-dbded7fc9de6 | -13.10316 | -49.57904 | 2025-12-01 04:27:00 | NOAA-20 | ARAGUAÇU | TOCANTINS | Brasil | 1702000 | 17 | 33 | nan | nan | nan | Cerrado | 0.6 |
| 3744832b-472e-3fff-9317-fc4cf2bd42ab | -14.42889 | -44.84523 | 2025-12-01 04:27:00 | NOAA-20 | COCOS | BAHIA | Brasil | 2908101 | 29 | 33 | nan | nan | nan | Cerrado | 1.7 |
| 1e50eabb-03c2-3a96-8162-8badadb25634 | -13.48369 | -46.71304 | 2025-12-01 04:27:00 | NOAA-20 | SÃO DOMINGOS | GOIÁS | Brasil | 5219803 | 52 | 33 | nan | nan | nan | Cerrado | 1.1 |
| c6c4a742-fdd6-3aea-a85f-3bf136107b1a | -15.65423 | -43.57253 | 2025-12-01 04:27:00 | NOAA-20 | VERDELÂNDIA | MINAS GERAIS | Brasil | 3171030 | 31 | 33 | nan | nan | nan | Cerrado | 0.6 |
| 89f1546a-39ea-3d5c-9b56-f2a3a054213b | -13.72659 | -48.73532 | 2025-12-01 04:27:00 | NOAA-20 | CAMPINORTE | GOIÁS | Brasil | 5204706 | 52 | 33 | nan | nan | nan | Cerrado | 1.0 |
| b6bcccbe-ebe5-392e-8fdf-427c61e8cd20 | -10.14173 | -36.14292 | 2025-12-01 04:27:00 | NOAA-20 | CORURIPE | ALAGOAS | Brasil | 2702306 | 27 | 33 | nan | nan | nan | Mata Atlântica | 46.7 |
| c0b3ca58-7bd3-348f-86b6-8ca1b1be4cd0 | -14.19274 | -44.45914 | 2025-12-01 04:27:00 | NOAA-20 | COCOS | BAHIA | Brasil | 2908101 | 29 | 33 | nan | nan | nan | Cerrado | 1.5 |
| e18299ed-db77-37aa-b9c0-152756cf73f1 | -13.72327 | -48.73477 | 2025-12-01 04:27:00 | NOAA-20 | CAMPINORTE | GOIÁS | Brasil | 5204706 | 52 | 33 | nan | nan | nan | Cerrado | 1.0 |
| 5971ea50-2231-3622-8a29-7987e46cd16a | -12.01272 | -49.27527 | 2025-12-01 04:27:00 | NOAA-20 | CARIRI DO TOCANTINS | TOCANTINS | Brasil | 1703867 | 17 | 33 | nan | nan | nan | Cerrado | 2.0 |
| 5d38d4e8-b66e-304d-9ae4-ba18867f69bd | -12.01732 | -49.26849 | 2025-12-01 04:27:00 | NOAA-20 | CARIRI DO TOCANTINS | TOCANTINS | Brasil | 1703867 | 17 | 33 | nan | nan | nan | Cerrado | 0.9 |
| 95bb28a6-7573-34fc-8b3b-0767c5621f4a | -13.44392 | -48.37803 | 2025-12-01 04:27:00 | NOAA-20 | MINAÇU | GOIÁS | Brasil | 5213087 | 52 | 33 | nan | nan | nan | Cerrado | 0.9 |
| 0bc63cf8-05f2-3c5f-b0c6-effbee8e2fd6 | -10.14725 | -36.1479 | 2025-12-01 04:27:00 | NOAA-20 | CORURIPE | ALAGOAS | Brasil | 2702306 | 27 | 33 | nan | nan | nan | Mata Atlântica | 46.7 |
| de539fe7-c931-321d-8e57-b757c7034377 | -13.03711 | -40.05152 | 2025-12-01 04:27:00 | NOAA-20 | NOVA ITARANA | BAHIA | Brasil | 2922805 | 29 | 33 | nan | nan | nan | Caatinga | 2.6 |
| ac152e60-e906-3e64-bc35-49b22ec1ede8 | -9.87716 | -40.56953 | 2025-12-01 04:27:00 | NOAA-20 | JUAZEIRO | BAHIA | Brasil | 2918407 | 29 | 33 | nan | nan | nan | Caatinga | 1.3 |
| 0f34aa1a-ef51-35d3-97f1-5dfeed2eeed5 | -11.97787 | -47.85465 | 2025-12-01 04:27:00 | NOAA-20 | NATIVIDADE | TOCANTINS | Brasil | 1714203 | 17 | 33 | nan | nan | nan | Cerrado | 0.6 |
| d39ab385-5430-37cc-8903-5571cb97e06e | -10.14118 | -36.14738 | 2025-12-01 04:27:00 | NOAA-20 | CORURIPE | ALAGOAS | Brasil | 2702306 | 27 | 33 | nan | nan | nan | Mata Atlântica | 46.7 |
| b4e8aef0-0cc4-3bfa-a244-9853a287ec7f | -21.02433 | -48.41273 | 2025-12-01 04:29:00 | NOAA-20 | PITANGUEIRAS | SÃO PAULO | Brasil | 3539509 | 35 | 33 | nan | nan | nan | Cerrado | 0.7 |
| 7e29fdc2-7385-398c-a71b-75c1b32037dd | -20.01929 | -57.43058 | 2025-12-01 04:29:00 | NOAA-20 | CORUMBÁ | MATO GROSSO DO SUL | Brasil | 5003207 | 50 | 33 | nan | nan | nan | Pantanal | 4.0 |
| bc682aa2-62d3-3c0d-abca-3e745c02d612 | -21.95561 | -44.88196 | 2025-12-01 04:29:00 | NOAA-20 | BAEPENDI | MINAS GERAIS | Brasil | 3104908 | 31 | 33 | nan | nan | nan | Mata Atlântica | 1.8 |
| 2607e1fd-649d-3b46-98fb-5db3298e2133 | -16.96898 | -48.20386 | 2025-12-01 04:29:00 | NOAA-20 | ORIZONA | GOIÁS | Brasil | 5215306 | 52 | 33 | nan | nan | nan | Cerrado | 0.6 |
| 719f6f8d-14d0-3fa4-be85-3c8f159ec344 | -20.92096 | -46.7914 | 2025-12-01 04:29:00 | NOAA-20 | FORTALEZA DE MINAS | MINAS GERAIS | Brasil | 3126307 | 31 | 33 | nan | nan | nan | Mata Atlântica | 2.0 |
| 960aa89f-e0b0-36ec-8b36-692dfb017f51 | -18.33843 | -52.96725 | 2025-12-01 04:29:00 | NOAA-20 | COSTA RICA | MATO GROSSO DO SUL | Brasil | 5003256 | 50 | 33 | nan | nan | nan | Cerrado | 2.3 |
| 88cdeb18-ae62-3b59-b24d-09d1e81575d7 | -20.0282 | -57.44051 | 2025-12-01 04:29:00 | NOAA-20 | CORUMBÁ | MATO GROSSO DO SUL | Brasil | 5003207 | 50 | 33 | nan | nan | nan | Pantanal | 4.3 |
| e6bac2ff-8093-3e13-86c0-4824261c6c03 | -15.42416 | -52.19318 | 2025-12-01 04:29:00 | NOAA-20 | BARRA DO GARÇAS | MATO GROSSO | Brasil | 5101803 | 51 | 33 | nan | nan | nan | Cerrado | 2.9 |
| a8d0db7e-5a48-3463-a374-7b3551bb3913 | -17.75278 | -47.29649 | 2025-12-01 04:29:00 | NOAA-20 | GUARDA-MOR | MINAS GERAIS | Brasil | 3128600 | 31 | 33 | nan | nan | nan | Cerrado | 0.8 |
| 92367335-4c05-3322-8b0e-fae261b9afda | -18.33762 | -52.97187 | 2025-12-01 04:29:00 | NOAA-20 | COSTA RICA | MATO GROSSO DO SUL | Brasil | 5003256 | 50 | 33 | nan | nan | nan | Cerrado | 4.2 |
| 2543906c-a03a-3f60-a972-240177f49e5d | -20.01354 | -57.43481 | 2025-12-01 04:29:00 | NOAA-20 | CORUMBÁ | MATO GROSSO DO SUL | Brasil | 5003207 | 50 | 33 | nan | nan | nan | Pantanal | 2.6 |
| e2c3941c-9d78-3232-98b5-a33849e4ad47 | -21.55084 | -48.89548 | 2025-12-01 04:29:00 | NOAA-20 | ITÁPOLIS | SÃO PAULO | Brasil | 3522703 | 35 | 33 | nan | nan | nan | Cerrado | 0.5 |
| ca241e8f-15d4-314a-8341-79f4f47fc76e | -21.05914 | -47.11547 | 2025-12-01 04:29:00 | NOAA-20 | ITAMOGI | MINAS GERAIS | Brasil | 3132909 | 31 | 33 | nan | nan | nan | Cerrado | 0.9 |
| 457c5ccb-8dc8-3afd-a747-51820e945091 | -16.46726 | -46.4207 | 2025-12-01 04:29:00 | NOAA-20 | NATALÂNDIA | MINAS GERAIS | Brasil | 3144375 | 31 | 33 | nan | nan | nan | Cerrado | 1.6 |
| 31c39d48-2630-358e-af10-6dfcf14e885f | -20.02711 | -57.44583 | 2025-12-01 04:29:00 | NOAA-20 | CORUMBÁ | MATO GROSSO DO SUL | Brasil | 5003207 | 50 | 33 | nan | nan | nan | Pantanal | 2.9 |
| 9cb98e8f-c497-3424-b217-44310e45c720 | -21.05712 | -48.70897 | 2025-12-01 04:29:00 | NOAA-20 | PIRANGI | SÃO PAULO | Brasil | 3539004 | 35 | 33 | nan | nan | nan | Mata Atlântica | 0.6 |
| d77e283f-a5f9-33dc-ad75-3d2684fa1f8b | -18.33681 | -52.97647 | 2025-12-01 04:29:00 | NOAA-20 | COSTA RICA | MATO GROSSO DO SUL | Brasil | 5003256 | 50 | 33 | nan | nan | nan | Cerrado | 4.2 |
| fb037660-cdb5-35a3-9a07-9b5a6cb8448e | -18.14628 | -47.14477 | 2025-12-01 04:29:00 | NOAA-20 | COROMANDEL | MINAS GERAIS | Brasil | 3119302 | 31 | 33 | nan | nan | nan | Cerrado | 1.8 |


[Clique aqui para ver as próximas entradas](README17.md)
