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
| 88cf013c-c2d7-3bd8-925d-7680b254b909 | -7.19865 | -45.49924 | 2026-07-29 04:12:00 | NPP-375D | SÃO RAIMUNDO DAS MANGABEIRAS | MARANHÃO | Brasil | 2111607 | 21 | 33 | nan | nan | nan | Cerrado | 1.1 |
| 4d6dd98a-8f9c-3a94-88d2-c2a36f3b7f02 | -7.34005 | -45.8398 | 2026-07-29 04:12:00 | NPP-375D | BALSAS | MARANHÃO | Brasil | 2101400 | 21 | 33 | nan | nan | nan | Cerrado | 3.5 |
| baac4a9a-b8f8-3a65-8119-b8019825bb37 | -7.22681 | -49.59573 | 2026-07-29 04:12:00 | NPP-375D | RIO MARIA | PARÁ | Brasil | 1506161 | 15 | 33 | nan | nan | nan | Amazônia | 0.8 |
| 7fd17d29-02cb-38f9-b86e-46a7b39aaecb | -6.87866 | -46.00956 | 2026-07-29 04:12:00 | NPP-375D | FORTALEZA DOS NOGUEIRAS | MARANHÃO | Brasil | 2104107 | 21 | 33 | nan | nan | nan | Cerrado | 4.9 |
| 145209e0-76ea-3a06-920d-aad17e9e5684 | -7.33811 | -45.85118 | 2026-07-29 04:12:00 | NPP-375D | BALSAS | MARANHÃO | Brasil | 2101400 | 21 | 33 | nan | nan | nan | Cerrado | 6.6 |
| 8b91cf5a-53e6-347c-9d42-316df0852942 | -7.35317 | -45.83825 | 2026-07-29 04:12:00 | NPP-375D | BALSAS | MARANHÃO | Brasil | 2101400 | 21 | 33 | nan | nan | nan | Cerrado | 11.3 |
| 4ca535e8-c247-3006-aa76-677b92eca54b | -4.87002 | -45.30883 | 2026-07-29 04:12:00 | NPP-375D | LAGOA GRANDE DO MARANHÃO | MARANHÃO | Brasil | 2105963 | 21 | 33 | nan | nan | nan | Cerrado | 1.8 |
| 4f22a131-b9c4-389c-a61d-6d9eefcd42ef | -3.96196 | -48.13034 | 2026-07-29 04:12:00 | NPP-375D | DOM ELISEU | PARÁ | Brasil | 1502939 | 15 | 33 | nan | nan | nan | Amazônia | 2.5 |
| 54642441-610a-30f2-8797-4a39909c6679 | -5.48212 | -45.11916 | 2026-07-29 04:12:00 | NPP-375D | BARRA DO CORDA | MARANHÃO | Brasil | 2101608 | 21 | 33 | nan | nan | nan | Cerrado | 1.9 |
| 2067d558-21ab-3c72-a16b-8acdce8c62ba | -4.11731 | -49.0896 | 2026-07-29 04:12:00 | NPP-375D | GOIANÉSIA DO PARÁ | PARÁ | Brasil | 1503093 | 15 | 33 | nan | nan | nan | Amazônia | 5.0 |
| f333f7d8-9119-3430-8de5-378968f2eaeb | -3.9449 | -40.97076 | 2026-07-29 04:12:00 | NPP-375D | IBIAPINA | CEARÁ | Brasil | 2305308 | 23 | 33 | nan | nan | nan | Caatinga | 1.2 |
| ecad7f1c-aed8-333f-844c-38d06e46c8a5 | -6.33858 | -44.60775 | 2026-07-29 04:12:00 | NPP-375D | MIRADOR | MARANHÃO | Brasil | 2106706 | 21 | 33 | nan | nan | nan | Cerrado | 2.6 |
| 4f915cce-e63f-3bec-9af1-b99191b078b5 | -7.34161 | -45.85578 | 2026-07-29 04:12:00 | NPP-375D | BALSAS | MARANHÃO | Brasil | 2101400 | 21 | 33 | nan | nan | nan | Cerrado | 4.2 |
| 92e199f9-baa8-37a5-a62b-265dd895e7a7 | -6.1584 | -44.65623 | 2026-07-29 04:12:00 | NPP-375D | MIRADOR | MARANHÃO | Brasil | 2106706 | 21 | 33 | nan | nan | nan | Cerrado | 2.4 |
| d706ad23-9f02-3052-9490-6be9a90731dc | -6.87306 | -46.0168 | 2026-07-29 04:12:00 | NPP-375D | FORTALEZA DOS NOGUEIRAS | MARANHÃO | Brasil | 2104107 | 21 | 33 | nan | nan | nan | Cerrado | 9.2 |
| f2bffc14-0037-30f6-8329-01ff3be73655 | -6.87373 | -46.01287 | 2026-07-29 04:12:00 | NPP-375D | FORTALEZA DOS NOGUEIRAS | MARANHÃO | Brasil | 2104107 | 21 | 33 | nan | nan | nan | Cerrado | 9.2 |
| ce8c0e79-5f32-31fb-b69c-7653c301046b | -3.16786 | -48.13094 | 2026-07-29 04:12:00 | NPP-375D | IPIXUNA DO PARÁ | PARÁ | Brasil | 1503457 | 15 | 33 | nan | nan | nan | Amazônia | 1.9 |
| 5a9c540b-d119-36f5-8eea-dbfe7385f1ea | -5.82165 | -44.75441 | 2026-07-29 04:12:00 | NPP-375D | TUNTUM | MARANHÃO | Brasil | 2112308 | 21 | 33 | nan | nan | nan | Cerrado | 2.6 |
| aadc5af8-2c4a-3a34-8db5-d191ed6ad9ed | -7.735 | -44.55636 | 2026-07-29 04:12:00 | NPP-375D | URUÇUÍ | PIAUÍ | Brasil | 2211209 | 22 | 33 | nan | nan | nan | Cerrado | 6.0 |
| 17cb3d27-4892-3fbe-8d3e-0e2f99092355 | -4.91162 | -43.47196 | 2026-07-29 04:12:00 | NPP-375D | CAXIAS | MARANHÃO | Brasil | 2103000 | 21 | 33 | nan | nan | nan | Cerrado | 2.6 |
| eb4edc6d-efd6-32ca-8550-43d557c3ab2c | -7.24325 | -46.05503 | 2026-07-29 04:12:00 | NPP-375D | BALSAS | MARANHÃO | Brasil | 2101400 | 21 | 33 | nan | nan | nan | Cerrado | 1.2 |
| 0f6cb611-ddfa-3e9b-a897-1c9ce42ddcc0 | -3.68518 | -47.64273 | 2026-07-29 04:12:00 | NPP-375D | ULIANÓPOLIS | PARÁ | Brasil | 1508126 | 15 | 33 | nan | nan | nan | Amazônia | 3.7 |
| ce5c3cc9-1968-3464-9b68-cb9a94768d5f | -4.47151 | -38.64946 | 2026-07-29 04:12:00 | NPP-375D | ARACOIABA | CEARÁ | Brasil | 2301208 | 23 | 33 | nan | nan | nan | Caatinga | 6.6 |
| fe7e3de5-c500-31e9-8340-2840b63b01b6 | -7.34772 | -45.8451 | 2026-07-29 04:12:00 | NPP-375D | BALSAS | MARANHÃO | Brasil | 2101400 | 21 | 33 | nan | nan | nan | Cerrado | 8.4 |
| f30a6f48-6e7e-3aa4-9617-614317bf6bf1 | -7.34421 | -45.84052 | 2026-07-29 04:12:00 | NPP-375D | BALSAS | MARANHÃO | Brasil | 2101400 | 21 | 33 | nan | nan | nan | Cerrado | 16.0 |
| 3479779b-70c5-3945-8d61-3071fe0eea45 | -4.57714 | -45.66982 | 2026-07-29 04:12:00 | NPP-375D | PAULO RAMOS | MARANHÃO | Brasil | 2108108 | 21 | 33 | nan | nan | nan | Amazônia | 0.6 |
| bb54bc5b-2055-3200-8b8b-17c915cc6eb6 | -3.69017 | -47.64365 | 2026-07-29 04:12:00 | NPP-375D | ULIANÓPOLIS | PARÁ | Brasil | 1508126 | 15 | 33 | nan | nan | nan | Amazônia | 3.7 |
| 23dab889-5c5d-31bf-9b8b-d21d8f22088f | -7.34226 | -45.85195 | 2026-07-29 04:12:00 | NPP-375D | BALSAS | MARANHÃO | Brasil | 2101400 | 21 | 33 | nan | nan | nan | Cerrado | 4.2 |
| e52cd42b-be76-312b-9b65-ee2d11b01c2f | -4.94237 | -48.25101 | 2026-07-29 04:12:00 | NPP-375D | ABEL FIGUEIREDO | PARÁ | Brasil | 1500131 | 15 | 33 | nan | nan | nan | Amazônia | 1.4 |
| 73261a3b-205f-32ce-a792-cb14c4390328 | -6.87014 | -46.00832 | 2026-07-29 04:12:00 | NPP-375D | FORTALEZA DOS NOGUEIRAS | MARANHÃO | Brasil | 2104107 | 21 | 33 | nan | nan | nan | Cerrado | 3.7 |
| 8318d689-6641-345f-ab00-1ae3999158ed | -3.03466 | -48.41344 | 2026-07-29 04:12:00 | NPP-375D | TOMÉ-AÇU | PARÁ | Brasil | 1508001 | 15 | 33 | nan | nan | nan | Amazônia | 0.5 |
| 8dca5607-1294-31ad-a1b6-0d80d3489246 | -4.28136 | -48.24916 | 2026-07-29 04:12:00 | NPP-375D | RONDON DO PARÁ | PARÁ | Brasil | 1506187 | 15 | 33 | nan | nan | nan | Amazônia | 1.2 |
| c93ec668-82ff-3149-80fd-4029b075c77f | -7.34707 | -45.84891 | 2026-07-29 04:12:00 | NPP-375D | BALSAS | MARANHÃO | Brasil | 2101400 | 21 | 33 | nan | nan | nan | Cerrado | 8.4 |
| 0da1849f-46c7-3bae-b1c0-50cf270b79e8 | -7.01002 | -41.59758 | 2026-07-29 04:12:00 | NPP-375D | PICOS | PIAUÍ | Brasil | 2208007 | 22 | 33 | nan | nan | nan | Caatinga | 2.2 |
| f3c1fd64-cc56-3df4-b2bc-37a84262dfa4 | -3.963 | -48.12414 | 2026-07-29 04:12:00 | NPP-375D | DOM ELISEU | PARÁ | Brasil | 1502939 | 15 | 33 | nan | nan | nan | Amazônia | 2.1 |
| d84424f8-a0ad-3d86-b603-1ef0253d4f3e | -7.34902 | -45.83747 | 2026-07-29 04:12:00 | NPP-375D | BALSAS | MARANHÃO | Brasil | 2101400 | 21 | 33 | nan | nan | nan | Cerrado | 16.0 |
| 55c13be6-6109-37b2-abd5-af3cf878411a | -6.80463 | -41.81345 | 2026-07-29 04:12:00 | NPP-375D | IPIRANGA DO PIAUÍ | PIAUÍ | Brasil | 2204808 | 22 | 33 | nan | nan | nan | Caatinga | 1.0 |
| 8a37513d-a4a2-399f-b459-1b960bb3167b | -7.81914 | -45.2802 | 2026-07-29 04:12:00 | NPP-375D | RIBEIRO GONÇALVES | PIAUÍ | Brasil | 2208908 | 22 | 33 | nan | nan | nan | Cerrado | 0.9 |
| 6c8021bb-4b9f-398d-aea3-26ca2f547cc8 | -3.17306 | -48.13189 | 2026-07-29 04:12:00 | NPP-375D | IPIXUNA DO PARÁ | PARÁ | Brasil | 1503457 | 15 | 33 | nan | nan | nan | Amazônia | 0.6 |
| e1aee725-ebe4-3ac6-bede-dd2536484e57 | -4.37063 | -47.76647 | 2026-07-29 04:12:00 | NPP-375D | DOM ELISEU | PARÁ | Brasil | 1502939 | 15 | 33 | nan | nan | nan | Amazônia | 5.5 |
| 6ae18536-a37f-347c-ba24-7d4728c75e94 | -5.83066 | -44.13921 | 2026-07-29 04:12:00 | NPP-375D | JATOBÁ | MARANHÃO | Brasil | 2105450 | 21 | 33 | nan | nan | nan | Cerrado | 0.7 |
| 13224952-364a-358a-9948-ac64f1dd84d9 | -7.22619 | -49.5992 | 2026-07-29 04:12:00 | NPP-375D | RIO MARIA | PARÁ | Brasil | 1506161 | 15 | 33 | nan | nan | nan | Amazônia | 1.2 |
| 5a2cc0a0-a180-3c07-b04a-336149ee4e8e | -7.3022 | -45.28233 | 2026-07-29 04:12:00 | NPP-375D | LORETO | MARANHÃO | Brasil | 2106102 | 21 | 33 | nan | nan | nan | Cerrado | 0.7 |
| 4180cb8e-936f-3c84-a997-0502f08cafe7 | -3.96248 | -48.12724 | 2026-07-29 04:12:00 | NPP-375D | DOM ELISEU | PARÁ | Brasil | 1502939 | 15 | 33 | nan | nan | nan | Amazônia | 2.1 |
| 851c18c7-e11d-319a-9448-fdc29ce35b32 | -5.84102 | -44.89372 | 2026-07-29 04:12:00 | NPP-375D | TUNTUM | MARANHÃO | Brasil | 2112308 | 21 | 33 | nan | nan | nan | Cerrado | 1.3 |
| ee279015-9aea-3687-8e5c-10c4a734d936 | -7.7302 | -47.25383 | 2026-07-29 04:12:00 | NPP-375D | CAROLINA | MARANHÃO | Brasil | 2102804 | 21 | 33 | nan | nan | nan | Cerrado | 3.2 |
| bdc2b8d8-314c-3de9-b98b-2f4c3e3294ba | -7.81515 | -46.8474 | 2026-07-29 04:12:00 | NPP-375D | CAROLINA | MARANHÃO | Brasil | 2102804 | 21 | 33 | nan | nan | nan | Cerrado | 1.8 |
| 792e1588-837e-315c-91c7-e52f25ffca95 | -4.28098 | -48.24603 | 2026-07-29 04:12:00 | NPP-375D | RONDON DO PARÁ | PARÁ | Brasil | 1506187 | 15 | 33 | nan | nan | nan | Amazônia | 1.3 |
| c6f6b8f9-de9a-309f-8666-56dea29057e7 | -7.35447 | -45.83062 | 2026-07-29 04:12:00 | NPP-375D | BALSAS | MARANHÃO | Brasil | 2101400 | 21 | 33 | nan | nan | nan | Cerrado | 18.6 |
| 9ae5a5c9-7ea3-39e7-9dde-fa57ca1b2034 | -7.19925 | -45.49563 | 2026-07-29 04:12:00 | NPP-375D | SÃO RAIMUNDO DAS MANGABEIRAS | MARANHÃO | Brasil | 2111607 | 21 | 33 | nan | nan | nan | Cerrado | 0.7 |
| be25bd98-7d24-32c5-9952-2f524e40e361 | -6.87082 | -46.0044 | 2026-07-29 04:12:00 | NPP-375D | FORTALEZA DOS NOGUEIRAS | MARANHÃO | Brasil | 2104107 | 21 | 33 | nan | nan | nan | Cerrado | 3.7 |
| 9ad1fd3b-bc9b-39c1-b80a-2663ef96e318 | -7.3407 | -45.83601 | 2026-07-29 04:12:00 | NPP-375D | BALSAS | MARANHÃO | Brasil | 2101400 | 21 | 33 | nan | nan | nan | Cerrado | 3.5 |
| 82ad92c0-1cd9-362c-9953-cbc7611f7bb2 | -7.33745 | -45.855 | 2026-07-29 04:12:00 | NPP-375D | BALSAS | MARANHÃO | Brasil | 2101400 | 21 | 33 | nan | nan | nan | Cerrado | 6.6 |
| f5e4d0dd-5cf9-3cd0-8792-65132e2836e8 | -6.87932 | -46.00569 | 2026-07-29 04:12:00 | NPP-375D | FORTALEZA DOS NOGUEIRAS | MARANHÃO | Brasil | 2104107 | 21 | 33 | nan | nan | nan | Cerrado | 4.9 |
| 3925104a-bcca-3992-b42a-86fdfd9a799f | -3.68018 | -47.64187 | 2026-07-29 04:12:00 | NPP-375D | ULIANÓPOLIS | PARÁ | Brasil | 1508126 | 15 | 33 | nan | nan | nan | Amazônia | 11.0 |
| 7629cadf-9afc-364f-b0d3-f5b99633d3ac | -3.16838 | -48.12783 | 2026-07-29 04:12:00 | NPP-375D | IPIXUNA DO PARÁ | PARÁ | Brasil | 1503457 | 15 | 33 | nan | nan | nan | Amazônia | 1.2 |
| 180f72a2-541e-3582-a17f-f036466cc30d | -6.0758 | -44.57343 | 2026-07-29 04:12:00 | NPP-375D | MIRADOR | MARANHÃO | Brasil | 2106706 | 21 | 33 | nan | nan | nan | Cerrado | 1.2 |
| f9521060-c9fb-36f8-8755-c9e7553f97c0 | -7.6211 | -38.79708 | 2026-07-29 04:12:00 | NPP-375D | BREJO SANTO | CEARÁ | Brasil | 2302503 | 23 | 33 | nan | nan | nan | Caatinga | 1.0 |
| 007f0fa4-3ad4-31d1-b408-4ebee21fc464 | -7.35862 | -45.83139 | 2026-07-29 04:12:00 | NPP-375D | BALSAS | MARANHÃO | Brasil | 2101400 | 21 | 33 | nan | nan | nan | Cerrado | 18.6 |
| c7ffa03a-ce7b-311e-8f96-200ae2f53fdf | -7.33876 | -45.84738 | 2026-07-29 04:12:00 | NPP-375D | BALSAS | MARANHÃO | Brasil | 2101400 | 21 | 33 | nan | nan | nan | Cerrado | 6.1 |
| 3f521d8e-d65a-3c67-9971-f77f1da9ee4a | -7.40491 | -43.77592 | 2026-07-29 04:12:00 | NPP-375D | SEBASTIÃO LEAL | PIAUÍ | Brasil | 2210631 | 22 | 33 | nan | nan | nan | Cerrado | 3.0 |
| 5ae44b53-0be3-3607-aac3-6fa3461e10a9 | -7.00945 | -41.60118 | 2026-07-29 04:12:00 | NPP-375D | PICOS | PIAUÍ | Brasil | 2208007 | 22 | 33 | nan | nan | nan | Caatinga | 4.3 |
| 779b738f-28f3-3743-985b-e74f6fa36887 | -7.82199 | -45.27918 | 2026-07-29 04:12:00 | NPP-375D | RIBEIRO GONÇALVES | PIAUÍ | Brasil | 2208908 | 22 | 33 | nan | nan | nan | Cerrado | 2.2 |
| 634c1e0a-b924-371a-a3d3-a8b826e4a63b | -4.94399 | -48.24177 | 2026-07-29 04:12:00 | NPP-375D | ABEL FIGUEIREDO | PARÁ | Brasil | 1500131 | 15 | 33 | nan | nan | nan | Amazônia | 1.0 |
| 1b2d9229-f95f-3093-ba37-857ac5d3a377 | -5.93307 | -46.35379 | 2026-07-29 04:12:00 | NPP-375D | GRAJAÚ | MARANHÃO | Brasil | 2104800 | 21 | 33 | nan | nan | nan | Cerrado | 2.1 |
| 447527cc-717c-3f4f-bacd-6324d1f84164 | -3.95783 | -48.12343 | 2026-07-29 04:12:00 | NPP-375D | DOM ELISEU | PARÁ | Brasil | 1502939 | 15 | 33 | nan | nan | nan | Amazônia | 2.1 |
| bb3f83bf-775b-3e37-b2b0-6dea187d2fbc | -7.34642 | -45.85273 | 2026-07-29 04:12:00 | NPP-375D | BALSAS | MARANHÃO | Brasil | 2101400 | 21 | 33 | nan | nan | nan | Cerrado | 4.2 |
| 1ddc1b22-e3ef-342c-bca6-e21c68560325 | -4.36564 | -47.76568 | 2026-07-29 04:12:00 | NPP-375D | DOM ELISEU | PARÁ | Brasil | 1502939 | 15 | 33 | nan | nan | nan | Amazônia | 5.5 |
| a4bdab7d-a50f-373b-95df-53456d373616 | -7.90198 | -48.2818 | 2026-07-29 04:12:00 | NPP-375D | PALMEIRANTE | TOCANTINS | Brasil | 1715705 | 17 | 33 | nan | nan | nan | Cerrado | 3.6 |
| 7e8bc078-16ed-3b8e-a41c-aa19dcdca85c | -7.3394 | -45.84359 | 2026-07-29 04:12:00 | NPP-375D | BALSAS | MARANHÃO | Brasil | 2101400 | 21 | 33 | nan | nan | nan | Cerrado | 6.1 |
| ad24d040-67ad-3ffa-93f1-aaef9b848262 | -4.28044 | -48.24922 | 2026-07-29 04:12:00 | NPP-375D | RONDON DO PARÁ | PARÁ | Brasil | 1506187 | 15 | 33 | nan | nan | nan | Amazônia | 1.6 |
| 6db1b9fb-6645-37fb-99d6-1cdeb8a13b1d | -7.34486 | -45.83672 | 2026-07-29 04:12:00 | NPP-375D | BALSAS | MARANHÃO | Brasil | 2101400 | 21 | 33 | nan | nan | nan | Cerrado | 16.0 |
| ef689e68-7ecb-36d1-b104-a7a08144aec8 | -3.6842 | -47.64855 | 2026-07-29 04:12:00 | NPP-375D | ULIANÓPOLIS | PARÁ | Brasil | 1508126 | 15 | 33 | nan | nan | nan | Amazônia | 3.7 |
| a30f34a6-9ed9-38df-a8ca-015a7b831664 | -4.28191 | -48.24598 | 2026-07-29 04:12:00 | NPP-375D | RONDON DO PARÁ | PARÁ | Brasil | 1506187 | 15 | 33 | nan | nan | nan | Amazônia | 1.1 |
| af2371c2-b081-3f43-b676-5166005fcd0b | -6.8744 | -46.00896 | 2026-07-29 04:12:00 | NPP-375D | FORTALEZA DOS NOGUEIRAS | MARANHÃO | Brasil | 2104107 | 21 | 33 | nan | nan | nan | Cerrado | 4.9 |
| 5b5998ef-bd98-31c5-9057-f74a16d781a5 | -7.82003 | -45.27505 | 2026-07-29 04:12:00 | NPP-375D | RIBEIRO GONÇALVES | PIAUÍ | Brasil | 2208908 | 22 | 33 | nan | nan | nan | Cerrado | 0.9 |
| a2a00982-2270-3b3d-bf34-a75f964da07c | -3.68615 | -47.63697 | 2026-07-29 04:12:00 | NPP-375D | ULIANÓPOLIS | PARÁ | Brasil | 1508126 | 15 | 33 | nan | nan | nan | Amazônia | 1.2 |
| cb0ad1d5-048a-335c-9f04-c63b39ab1f8c | -11.5364 | -47.56476 | 2026-07-29 04:14:00 | NPP-375D | NATIVIDADE | TOCANTINS | Brasil | 1714203 | 17 | 33 | nan | nan | nan | Cerrado | 1.7 |
| c257271a-e5cc-3c24-8b6c-2cc766d0ec50 | -10.3277 | -49.71418 | 2026-07-29 04:14:00 | NPP-375D | PIUM | TOCANTINS | Brasil | 1717503 | 17 | 33 | nan | nan | nan | Cerrado | 2.6 |
| 84ce83c4-0235-3f0f-a091-503897ab6314 | -9.59844 | -49.30206 | 2026-07-29 04:14:00 | NPP-375D | ABREULÂNDIA | TOCANTINS | Brasil | 1700251 | 17 | 33 | nan | nan | nan | Cerrado | 0.5 |
| 3a72dba6-053a-3c2d-b2d0-2c8a88da546e | -12.31551 | -46.7519 | 2026-07-29 04:14:00 | NPP-375D | TAGUATINGA | TOCANTINS | Brasil | 1720903 | 17 | 33 | nan | nan | nan | Cerrado | 2.8 |
| 66458c34-3a79-381e-9c8e-ec77275b5bf3 | -10.93267 | -43.05769 | 2026-07-29 04:14:00 | NPP-375D | BARRA | BAHIA | Brasil | 2902708 | 29 | 33 | nan | nan | nan | Cerrado | 23.8 |
| e74f00d1-743b-300c-babe-899f2045936e | -14.1959 | -51.90824 | 2026-07-29 04:14:00 | NPP-375D | NOVA NAZARÉ | MATO GROSSO | Brasil | 5106174 | 51 | 33 | nan | nan | nan | Cerrado | 1.0 |
| 469afe0d-04fe-3d0f-9945-3bf21909abd7 | -15.06633 | -41.21968 | 2026-07-29 04:14:00 | NPP-375D | BELO CAMPO | BAHIA | Brasil | 2903508 | 29 | 33 | nan | nan | nan | Mata Atlântica | 1.4 |
| f6097453-dde7-397f-9e0a-fbab424f08b6 | -13.45756 | -44.04225 | 2026-07-29 04:14:00 | NPP-375D | SÃO FÉLIX DO CORIBE | BAHIA | Brasil | 2929057 | 29 | 33 | nan | nan | nan | Cerrado | 1.2 |
| 3c52dcac-8cd3-3c90-888b-c6e6ca951d95 | -9.66147 | -40.59301 | 2026-07-29 04:14:00 | NPP-375D | JUAZEIRO | BAHIA | Brasil | 2918407 | 29 | 33 | nan | nan | nan | Caatinga | 25.7 |
| 92c2a794-e1dc-3fe1-bfaa-5a166fe0c254 | -10.90131 | -45.21035 | 2026-07-29 04:14:00 | NPP-375D | FORMOSA DO RIO PRETO | BAHIA | Brasil | 2911105 | 29 | 33 | nan | nan | nan | Cerrado | 1.1 |
| 34e2c95f-840d-3364-8b41-e1f8ba985ae8 | -14.06291 | -53.97433 | 2026-07-29 04:14:00 | NPP-375D | PARANATINGA | MATO GROSSO | Brasil | 5106307 | 51 | 33 | nan | nan | nan | Cerrado | 2.9 |
| 1db497d8-8c3c-32ad-bdd3-62d63c9f6156 | -12.14844 | -48.95215 | 2026-07-29 04:14:00 | NPP-375D | SUCUPIRA | TOCANTINS | Brasil | 1720853 | 17 | 33 | nan | nan | nan | Cerrado | 4.5 |
| 46d26b4a-248a-305a-9cfc-a7c9b1432ce3 | -14.06073 | -53.98445 | 2026-07-29 04:14:00 | NPP-375D | PARANATINGA | MATO GROSSO | Brasil | 5106307 | 51 | 33 | nan | nan | nan | Cerrado | 1.8 |
| c428a102-0e58-3df9-8cea-51b97d4a3c4f | -14.2166 | -44.65794 | 2026-07-29 04:14:00 | NPP-375D | COCOS | BAHIA | Brasil | 2908101 | 29 | 33 | nan | nan | nan | Cerrado | 0.6 |
| 20924bf5-2826-3291-9021-e421f1f11565 | -14.0394 | -53.97822 | 2026-07-29 04:14:00 | NPP-375D | PARANATINGA | MATO GROSSO | Brasil | 5106307 | 51 | 33 | nan | nan | nan | Cerrado | 2.9 |
| 783444db-5375-3fbd-8dd1-25ee86c82d04 | -15.17966 | -43.85366 | 2026-07-29 04:14:00 | NPP-375D | JAÍBA | MINAS GERAIS | Brasil | 3135050 | 31 | 33 | nan | nan | nan | Cerrado | 1.1 |
| 6e3b1018-cfdc-35ef-8d24-a07abe939b62 | -10.13516 | -42.42211 | 2026-07-29 04:14:00 | NPP-375D | SENTO SÉ | BAHIA | Brasil | 2930204 | 29 | 33 | nan | nan | nan | Caatinga | 1.4 |
| 785e3b03-a0e5-3af0-b1bc-a440b988de23 | -13.45341 | -44.04559 | 2026-07-29 04:14:00 | NPP-375D | SÃO FÉLIX DO CORIBE | BAHIA | Brasil | 2929057 | 29 | 33 | nan | nan | nan | Cerrado | 0.7 |
| e7b634a6-5642-3eaa-9461-4bbae5ee4976 | -14.07172 | -53.98039 | 2026-07-29 04:14:00 | NPP-375D | PARANATINGA | MATO GROSSO | Brasil | 5106307 | 51 | 33 | nan | nan | nan | Cerrado | 0.8 |
| 202e7aa6-cfbb-3f39-b87c-2058237093af | -14.19514 | -51.91198 | 2026-07-29 04:14:00 | NPP-375D | NOVA NAZARÉ | MATO GROSSO | Brasil | 5106174 | 51 | 33 | nan | nan | nan | Cerrado | 1.2 |
| f4834a15-1541-367e-8e8c-730140f98d2b | -12.62374 | -44.63071 | 2026-07-29 04:14:00 | NPP-375D | SÃO DESIDÉRIO | BAHIA | Brasil | 2928901 | 29 | 33 | nan | nan | nan | Cerrado | 0.9 |
| 59a3b800-f0dd-393d-b138-e28f3c3c7ff9 | -14.72073 | -47.14788 | 2026-07-29 04:14:00 | NPP-375D | VILA BOA | GOIÁS | Brasil | 5222203 | 52 | 33 | nan | nan | nan | Cerrado | 0.9 |
| 9f469eab-0ace-3fa8-8d77-1e4f9c49372f | -14.22014 | -44.65854 | 2026-07-29 04:14:00 | NPP-375D | COCOS | BAHIA | Brasil | 2908101 | 29 | 33 | nan | nan | nan | Cerrado | 1.4 |


[Clique aqui para ver as próximas entradas](README7.md)
