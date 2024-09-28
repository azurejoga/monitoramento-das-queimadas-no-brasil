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

## Dados Diários - Página 41

| ID | Latitude | Longitude | Data/Hora GMT | Satélite | Município | Estado | País | Município ID | Estado ID | País ID | Dias sem Chuva | Precipitação | Risco de Fogo | Bioma | FRP |
|----|----------|-----------|---------------|----------|-----------|--------|------|--------------|-----------|---------|----------------|--------------|----------------|-------|-----|
| 9e4af259-5730-3b0f-9c43-7562a1296731 | -8.40174 | -44.64761 | 2024-09-28 04:19:00 | NOAA-21 | PALMEIRA DO PIAUÍ | PIAUÍ | Brasil | 2207405 | 22 | 33 | nan | nan | nan | Cerrado | 1.6 |
| 916cfa8c-c303-370a-9e01-9029684c49d4 | -8.35913 | -45.00669 | 2024-09-28 04:19:00 | NOAA-21 | BAIXA GRANDE DO RIBEIRO | PIAUÍ | Brasil | 2201150 | 22 | 33 | nan | nan | nan | Cerrado | 2.9 |
| 4eaa8f12-1ede-3e70-8c14-92d073ef4bb9 | -8.24055 | -44.85315 | 2024-09-28 04:19:00 | NOAA-21 | BAIXA GRANDE DO RIBEIRO | PIAUÍ | Brasil | 2201150 | 22 | 33 | nan | nan | nan | Cerrado | 1.2 |
| ca31034a-c9af-39e4-8559-b8d0995cc5ae | -8.24001 | -44.85662 | 2024-09-28 04:19:00 | NOAA-21 | BAIXA GRANDE DO RIBEIRO | PIAUÍ | Brasil | 2201150 | 22 | 33 | nan | nan | nan | Cerrado | 2.0 |
| 2b2b72ae-b83f-3bf2-a5aa-f6bb6e91b1f9 | -8.23779 | -44.84917 | 2024-09-28 04:19:00 | NOAA-21 | URUÇUÍ | PIAUÍ | Brasil | 2211209 | 22 | 33 | nan | nan | nan | Cerrado | 1.2 |
| bd06c0cf-de34-30cc-94d8-2d34e91a922b | -3.61279 | -44.80351 | 2024-09-28 04:19:00 | NOAA-21 | ARARI | MARANHÃO | Brasil | 2101004 | 21 | 33 | nan | nan | nan | Amazônia | 0.9 |
| 3916de05-7373-3688-9301-63664b5450f9 | -2.41472 | -45.14837 | 2024-09-28 04:19:00 | NOAA-21 | PINHEIRO | MARANHÃO | Brasil | 2108603 | 21 | 33 | nan | nan | nan | Amazônia | 0.8 |
| fbdc1481-8826-34c2-bdef-e7ac8b1ccd92 | -4.11053 | -45.79308 | 2024-09-28 04:19:00 | NOAA-21 | SANTA LUZIA | MARANHÃO | Brasil | 2110005 | 21 | 33 | nan | nan | nan | Amazônia | 1.4 |
| bd35839b-0cff-3363-9338-c2ad7ab54eda | -4.04498 | -45.81257 | 2024-09-28 04:19:00 | NOAA-21 | SANTA LUZIA | MARANHÃO | Brasil | 2110005 | 21 | 33 | nan | nan | nan | Amazônia | 0.9 |
| 6f3d3c07-045a-3c8e-b76d-4aacb3547d96 | -3.66461 | -46.01668 | 2024-09-28 04:19:00 | NOAA-21 | BOM JARDIM | MARANHÃO | Brasil | 2102002 | 21 | 33 | nan | nan | nan | Amazônia | 1.2 |
| 87c6537a-8e14-3c71-9261-eb3f544066c3 | -5.11489 | -44.83959 | 2024-09-28 04:19:00 | NOAA-21 | JOSELÂNDIA | MARANHÃO | Brasil | 2105609 | 21 | 33 | nan | nan | nan | Cerrado | 1.4 |
| 30f45f14-e268-3f16-b280-8bdaeb2c3576 | -4.86396 | -44.8776 | 2024-09-28 04:19:00 | NOAA-21 | ESPERANTINÓPOLIS | MARANHÃO | Brasil | 2104008 | 21 | 33 | nan | nan | nan | Cerrado | 1.5 |
| df35a994-6ec7-312e-a308-688623e06b74 | -4.98874 | -45.40125 | 2024-09-28 04:19:00 | NOAA-21 | LAGOA GRANDE DO MARANHÃO | MARANHÃO | Brasil | 2105963 | 21 | 33 | nan | nan | nan | Cerrado | 2.4 |
| baa31bb0-7e97-32fc-8f18-07f2356b2e30 | -4.98541 | -45.40073 | 2024-09-28 04:19:00 | NOAA-21 | LAGOA GRANDE DO MARANHÃO | MARANHÃO | Brasil | 2105963 | 21 | 33 | nan | nan | nan | Cerrado | 2.4 |
| b35faeeb-7904-3cea-8574-9b23a227e557 | -4.98486 | -45.40422 | 2024-09-28 04:19:00 | NOAA-21 | LAGOA GRANDE DO MARANHÃO | MARANHÃO | Brasil | 2105963 | 21 | 33 | nan | nan | nan | Cerrado | 1.9 |
| 1cdf88eb-f6b0-39bd-ae91-664eee82427f | -4.93925 | -45.66927 | 2024-09-28 04:19:00 | NOAA-21 | ARAME | MARANHÃO | Brasil | 2100956 | 21 | 33 | nan | nan | nan | Amazônia | 1.9 |
| d5455c10-e345-379f-b158-c102cff588c9 | -4.93589 | -45.66874 | 2024-09-28 04:19:00 | NOAA-21 | ARAME | MARANHÃO | Brasil | 2100956 | 21 | 33 | nan | nan | nan | Amazônia | 1.9 |
| ac528814-1449-3313-988e-df8635fcd025 | -4.78853 | -45.26852 | 2024-09-28 04:19:00 | NOAA-21 | LAGO DA PEDRA | MARANHÃO | Brasil | 2105708 | 21 | 33 | nan | nan | nan | Cerrado | 1.2 |
| a1850173-04ae-33c4-9056-6a0cbe98f882 | -4.7716 | -45.8857 | 2024-09-28 04:19:00 | NOAA-21 | ARAME | MARANHÃO | Brasil | 2100956 | 21 | 33 | nan | nan | nan | Amazônia | 3.1 |
| a2b4f56e-c1c4-3e5e-9747-3bcc8371e3d9 | -5.97606 | -45.70264 | 2024-09-28 04:19:00 | NOAA-21 | GRAJAÚ | MARANHÃO | Brasil | 2104800 | 21 | 33 | nan | nan | nan | Cerrado | 1.4 |
| 8bf9cf63-64b1-3db2-980e-03fb5061af99 | -5.9039 | -45.59731 | 2024-09-28 04:19:00 | NOAA-21 | GRAJAÚ | MARANHÃO | Brasil | 2104800 | 21 | 33 | nan | nan | nan | Cerrado | 0.8 |
| 10b4494d-c792-3f15-8304-e2b6c276f068 | -5.86762 | -45.35456 | 2024-09-28 04:19:00 | NOAA-21 | BARRA DO CORDA | MARANHÃO | Brasil | 2101608 | 21 | 33 | nan | nan | nan | Cerrado | 1.4 |
| 04a9ea67-78af-39ee-a576-9a6e5e9c84c3 | -5.77255 | -45.54718 | 2024-09-28 04:19:00 | NOAA-21 | GRAJAÚ | MARANHÃO | Brasil | 2104800 | 21 | 33 | nan | nan | nan | Cerrado | 1.1 |
| 1e0c1940-098d-3c49-88d3-9176bf0cd0c0 | -5.76977 | -45.54314 | 2024-09-28 04:19:00 | NOAA-21 | GRAJAÚ | MARANHÃO | Brasil | 2104800 | 21 | 33 | nan | nan | nan | Cerrado | 1.9 |
| 9d9be39c-256c-368b-a5fe-7f773b16c534 | -5.76921 | -45.54666 | 2024-09-28 04:19:00 | NOAA-21 | GRAJAÚ | MARANHÃO | Brasil | 2104800 | 21 | 33 | nan | nan | nan | Cerrado | 1.9 |
| a609c0b5-3b88-347b-99e6-61171e7e13c0 | -5.76866 | -45.55019 | 2024-09-28 04:19:00 | NOAA-21 | GRAJAÚ | MARANHÃO | Brasil | 2104800 | 21 | 33 | nan | nan | nan | Cerrado | 1.9 |
| e889ba26-310a-3420-a13a-4c98bb2c5c44 | -5.76588 | -45.54615 | 2024-09-28 04:19:00 | NOAA-21 | GRAJAÚ | MARANHÃO | Brasil | 2104800 | 21 | 33 | nan | nan | nan | Cerrado | 1.9 |
| 98388159-1cd4-3c82-be19-20c1cebd2e24 | -5.76532 | -45.54967 | 2024-09-28 04:19:00 | NOAA-21 | GRAJAÚ | MARANHÃO | Brasil | 2104800 | 21 | 33 | nan | nan | nan | Cerrado | 1.9 |
| d9ab7880-3a4f-3309-a35e-ebd507e73b98 | -5.71354 | -46.4512 | 2024-09-28 04:19:00 | NOAA-21 | AMARANTE DO MARANHÃO | MARANHÃO | Brasil | 2100600 | 21 | 33 | nan | nan | nan | Cerrado | 2.1 |
| d94114e5-cd56-30b3-9f07-0e5852fc72b4 | -5.71295 | -46.45492 | 2024-09-28 04:19:00 | NOAA-21 | AMARANTE DO MARANHÃO | MARANHÃO | Brasil | 2100600 | 21 | 33 | nan | nan | nan | Cerrado | 2.1 |
| 84ae66c8-e1a9-3b38-b87d-6ecdfcb9416a | -5.71013 | -46.45065 | 2024-09-28 04:19:00 | NOAA-21 | AMARANTE DO MARANHÃO | MARANHÃO | Brasil | 2100600 | 21 | 33 | nan | nan | nan | Cerrado | 2.1 |
| 62654db6-0784-323c-93fb-45ccee20c53c | -5.70953 | -46.45436 | 2024-09-28 04:19:00 | NOAA-21 | AMARANTE DO MARANHÃO | MARANHÃO | Brasil | 2100600 | 21 | 33 | nan | nan | nan | Cerrado | 2.1 |
| 676d361b-048f-34ac-818d-2fe79c8c37b0 | -5.70612 | -46.4538 | 2024-09-28 04:19:00 | NOAA-21 | AMARANTE DO MARANHÃO | MARANHÃO | Brasil | 2100600 | 21 | 33 | nan | nan | nan | Cerrado | 1.0 |
| c4b53b23-d172-3099-bb96-31e850463b0b | -5.66765 | -45.90531 | 2024-09-28 04:19:00 | NOAA-21 | GRAJAÚ | MARANHÃO | Brasil | 2104800 | 21 | 33 | nan | nan | nan | Cerrado | 0.9 |
| f99e5ab8-ddf0-3bde-a6bb-f8abf296e811 | -5.66761 | -46.3454 | 2024-09-28 04:19:00 | NOAA-21 | AMARANTE DO MARANHÃO | MARANHÃO | Brasil | 2100600 | 21 | 33 | nan | nan | nan | Cerrado | 1.0 |
| 433335cb-2e58-3472-9443-3ef0c33303b2 | -5.66701 | -46.34909 | 2024-09-28 04:19:00 | NOAA-21 | AMARANTE DO MARANHÃO | MARANHÃO | Brasil | 2100600 | 21 | 33 | nan | nan | nan | Cerrado | 1.0 |
| 04680d2f-490b-3965-8019-9455404e6cef | -5.56868 | -46.28381 | 2024-09-28 04:19:00 | NOAA-21 | GRAJAÚ | MARANHÃO | Brasil | 2104800 | 21 | 33 | nan | nan | nan | Cerrado | 2.8 |
| 600d23f1-a2d4-3d4d-975c-cbebfb3da852 | -5.56587 | -46.2796 | 2024-09-28 04:19:00 | NOAA-21 | GRAJAÚ | MARANHÃO | Brasil | 2104800 | 21 | 33 | nan | nan | nan | Cerrado | 1.5 |
| df7ad0c4-7c60-3e25-9f90-4cd89bb73a20 | -5.56528 | -46.28326 | 2024-09-28 04:19:00 | NOAA-21 | GRAJAÚ | MARANHÃO | Brasil | 2104800 | 21 | 33 | nan | nan | nan | Cerrado | 2.8 |
| 68582e18-8239-3d13-a127-c3be4060e035 | -5.56493 | -46.27972 | 2024-09-28 04:19:00 | NOAA-21 | GRAJAÚ | MARANHÃO | Brasil | 2104800 | 21 | 33 | nan | nan | nan | Cerrado | 1.3 |
| 392ebac6-528b-30a6-9f36-f42dc14ee72c | -5.56435 | -46.28338 | 2024-09-28 04:19:00 | NOAA-21 | GRAJAÚ | MARANHÃO | Brasil | 2104800 | 21 | 33 | nan | nan | nan | Cerrado | 1.6 |
| 7aa84d9d-c8ca-35dc-9ac4-d7adf444003d | -5.56095 | -46.28283 | 2024-09-28 04:19:00 | NOAA-21 | GRAJAÚ | MARANHÃO | Brasil | 2104800 | 21 | 33 | nan | nan | nan | Cerrado | 1.6 |
| 5c883396-4d79-3b11-994d-d8e9088bbb17 | -5.48803 | -45.9251 | 2024-09-28 04:19:00 | NOAA-21 | GRAJAÚ | MARANHÃO | Brasil | 2104800 | 21 | 33 | nan | nan | nan | Cerrado | 0.9 |
| e241c070-84b3-3560-bf1e-5d2ec7b00d2f | -5.19996 | -44.94855 | 2024-09-28 04:19:00 | NOAA-21 | BARRA DO CORDA | MARANHÃO | Brasil | 2101608 | 21 | 33 | nan | nan | nan | Cerrado | 1.8 |
| a2acd715-a5a6-3577-8181-c742cbdd3892 | -5.19941 | -44.95201 | 2024-09-28 04:19:00 | NOAA-21 | BARRA DO CORDA | MARANHÃO | Brasil | 2101608 | 21 | 33 | nan | nan | nan | Cerrado | 1.4 |
| 8aecb460-7156-31cb-b451-d3a6de1f5eed | -5.19828 | -44.93768 | 2024-09-28 04:19:00 | NOAA-21 | BARRA DO CORDA | MARANHÃO | Brasil | 2101608 | 21 | 33 | nan | nan | nan | Cerrado | 3.8 |
| 2ab9771e-fd82-3262-bcd6-fa77b8061de2 | -5.19774 | -44.94113 | 2024-09-28 04:19:00 | NOAA-21 | BARRA DO CORDA | MARANHÃO | Brasil | 2101608 | 21 | 33 | nan | nan | nan | Cerrado | 3.8 |
| 72c3efba-9314-3a26-9a09-ef2235ff4987 | -5.1972 | -44.94458 | 2024-09-28 04:19:00 | NOAA-21 | BARRA DO CORDA | MARANHÃO | Brasil | 2101608 | 21 | 33 | nan | nan | nan | Cerrado | 2.3 |
| 6f08f74b-9309-30a7-9d38-cec2e399b72a | -5.19665 | -44.94804 | 2024-09-28 04:19:00 | NOAA-21 | BARRA DO CORDA | MARANHÃO | Brasil | 2101608 | 21 | 33 | nan | nan | nan | Cerrado | 2.3 |
| 52f7a89e-6b54-326c-b991-9bc83d048a89 | -5.19611 | -44.9515 | 2024-09-28 04:19:00 | NOAA-21 | BARRA DO CORDA | MARANHÃO | Brasil | 2101608 | 21 | 33 | nan | nan | nan | Cerrado | 2.0 |
| ea757956-8b8c-3612-8a53-157395fd796e | -5.19443 | -44.94062 | 2024-09-28 04:19:00 | NOAA-21 | BARRA DO CORDA | MARANHÃO | Brasil | 2101608 | 21 | 33 | nan | nan | nan | Cerrado | 3.8 |
| 97fa3b55-5c86-3c7a-96f8-d5048208eab5 | -5.42266 | -45.47717 | 2024-09-28 04:19:00 | NOAA-21 | JENIPAPO DOS VIEIRAS | MARANHÃO | Brasil | 2105476 | 21 | 33 | nan | nan | nan | Cerrado | 1.4 |
| a89e7d84-343b-3ab2-b1e5-0e608e054f52 | -5.39143 | -45.56613 | 2024-09-28 04:19:00 | NOAA-21 | JENIPAPO DOS VIEIRAS | MARANHÃO | Brasil | 2105476 | 21 | 33 | nan | nan | nan | Cerrado | 1.8 |
| a9c5a67d-eb91-384b-a730-a96da7431281 | -5.37945 | -45.40557 | 2024-09-28 04:19:00 | NOAA-21 | BARRA DO CORDA | MARANHÃO | Brasil | 2101608 | 21 | 33 | nan | nan | nan | Cerrado | 0.7 |
| 72ad1016-7a3d-38f7-8d64-d4ee9b03df9e | -5.37889 | -45.40907 | 2024-09-28 04:19:00 | NOAA-21 | BARRA DO CORDA | MARANHÃO | Brasil | 2101608 | 21 | 33 | nan | nan | nan | Cerrado | 1.5 |
| 3ddb8c4e-261e-32ed-9c3f-aaf7c50dfada | -5.37644 | -45.40498 | 2024-09-28 04:19:00 | NOAA-21 | BARRA DO CORDA | MARANHÃO | Brasil | 2101608 | 21 | 33 | nan | nan | nan | Cerrado | 1.8 |
| 0b30318c-91ed-37f5-a8d0-13fa3f89c47e | -5.34531 | -45.89848 | 2024-09-28 04:19:00 | NOAA-21 | ITAIPAVA DO GRAJAÚ | MARANHÃO | Brasil | 2105351 | 21 | 33 | nan | nan | nan | Cerrado | 1.4 |
| df0e934b-b909-3bc1-aeb6-90e8542011c0 | -5.33207 | -45.42673 | 2024-09-28 04:19:00 | NOAA-21 | BARRA DO CORDA | MARANHÃO | Brasil | 2101608 | 21 | 33 | nan | nan | nan | Cerrado | 0.9 |
| 8e2f30b6-ec34-3ce0-a888-35ccc3a9d86b | -5.33151 | -45.43023 | 2024-09-28 04:19:00 | NOAA-21 | BARRA DO CORDA | MARANHÃO | Brasil | 2101608 | 21 | 33 | nan | nan | nan | Cerrado | 1.3 |
| bc2ff14b-4a02-30dc-a2e7-f7cccd012621 | -5.32874 | -45.42619 | 2024-09-28 04:19:00 | NOAA-21 | BARRA DO CORDA | MARANHÃO | Brasil | 2101608 | 21 | 33 | nan | nan | nan | Cerrado | 0.9 |
| 42719ae2-755a-3454-a0ff-a373ba461f99 | -5.32818 | -45.42969 | 2024-09-28 04:19:00 | NOAA-21 | BARRA DO CORDA | MARANHÃO | Brasil | 2101608 | 21 | 33 | nan | nan | nan | Cerrado | 1.3 |
| 0fedcb4a-7bd2-3b2d-80cd-541f0750ca9a | -5.28103 | -45.72684 | 2024-09-28 04:19:00 | NOAA-21 | JENIPAPO DOS VIEIRAS | MARANHÃO | Brasil | 2105476 | 21 | 33 | nan | nan | nan | Cerrado | 1.8 |
| adec988a-be12-38ed-bcc4-6b20cd0379ff | -5.27044 | -46.21407 | 2024-09-28 04:19:00 | NOAA-21 | ARAME | MARANHÃO | Brasil | 2100956 | 21 | 33 | nan | nan | nan | Amazônia | 1.5 |
| 70663da6-bcce-3f13-b3f5-81127b6e228e | -5.2558 | -46.19677 | 2024-09-28 04:19:00 | NOAA-21 | ARAME | MARANHÃO | Brasil | 2100956 | 21 | 33 | nan | nan | nan | Amazônia | 1.5 |
| 26e07744-eb9e-3cbf-9fea-92b6e7543941 | -5.11264 | -45.99137 | 2024-09-28 04:19:00 | NOAA-21 | ARAME | MARANHÃO | Brasil | 2100956 | 21 | 33 | nan | nan | nan | Amazônia | 1.8 |
| 424e7d30-7ac7-3e70-8b27-deaa16a4a47a | -5.09306 | -45.83307 | 2024-09-28 04:19:00 | NOAA-21 | ARAME | MARANHÃO | Brasil | 2100956 | 21 | 33 | nan | nan | nan | Amazônia | 10.2 |
| 2b05e0c6-7fe6-3760-9bae-17a26c8e8287 | -5.09249 | -45.83664 | 2024-09-28 04:19:00 | NOAA-21 | ARAME | MARANHÃO | Brasil | 2100956 | 21 | 33 | nan | nan | nan | Amazônia | 3.8 |
| cb568322-05f0-3172-95af-8638b151c701 | -5.09191 | -45.84022 | 2024-09-28 04:19:00 | NOAA-21 | ARAME | MARANHÃO | Brasil | 2100956 | 21 | 33 | nan | nan | nan | Amazônia | 3.8 |
| 70741070-6567-3755-aeab-53f6768e93ee | -5.06966 | -46.10784 | 2024-09-28 04:19:00 | NOAA-21 | ARAME | MARANHÃO | Brasil | 2100956 | 21 | 33 | nan | nan | nan | Amazônia | 1.1 |
| 5c5d78cf-8aee-3c1b-9c42-38a09d29cf06 | -6.46261 | -46.16808 | 2024-09-28 04:19:00 | NOAA-21 | FORMOSA DA SERRA NEGRA | MARANHÃO | Brasil | 2104099 | 21 | 33 | nan | nan | nan | Cerrado | 1.5 |
| f24770f0-e3b5-3af5-b7d8-78be1369df1e | -6.39747 | -45.95938 | 2024-09-28 04:19:00 | NOAA-21 | FORMOSA DA SERRA NEGRA | MARANHÃO | Brasil | 2104099 | 21 | 33 | nan | nan | nan | Cerrado | 0.9 |
| 8ddb880f-56c1-318a-bff9-080f72f2bb40 | -6.39412 | -45.95885 | 2024-09-28 04:19:00 | NOAA-21 | FORMOSA DA SERRA NEGRA | MARANHÃO | Brasil | 2104099 | 21 | 33 | nan | nan | nan | Cerrado | 0.9 |
| fa059d30-5f50-31bb-ba43-dc3c045af6a2 | -6.31221 | -46.35247 | 2024-09-28 04:19:00 | NOAA-21 | FORMOSA DA SERRA NEGRA | MARANHÃO | Brasil | 2104099 | 21 | 33 | nan | nan | nan | Cerrado | 1.1 |
| 1c1ec12e-84cf-30e7-b2d0-8469aa5c0a38 | -6.18724 | -46.08366 | 2024-09-28 04:19:00 | NOAA-21 | GRAJAÚ | MARANHÃO | Brasil | 2104800 | 21 | 33 | nan | nan | nan | Cerrado | 0.7 |
| 620a5d31-a276-379b-8d22-56d06d8efb81 | -6.18667 | -46.08725 | 2024-09-28 04:19:00 | NOAA-21 | GRAJAÚ | MARANHÃO | Brasil | 2104800 | 21 | 33 | nan | nan | nan | Cerrado | 0.7 |
| f76003ae-9d64-389a-b3ae-56f8f4fa2eb2 | -6.18387 | -46.08314 | 2024-09-28 04:19:00 | NOAA-21 | GRAJAÚ | MARANHÃO | Brasil | 2104800 | 21 | 33 | nan | nan | nan | Cerrado | 0.7 |
| fb0370de-0093-38bb-b233-857f9d135076 | -6.17869 | -45.43265 | 2024-09-28 04:19:00 | NOAA-21 | FERNANDO FALCÃO | MARANHÃO | Brasil | 2104081 | 21 | 33 | nan | nan | nan | Cerrado | 7.5 |
| a97a6283-5692-3bc2-a4e8-393728bbba4c | -6.17482 | -45.43562 | 2024-09-28 04:19:00 | NOAA-21 | FERNANDO FALCÃO | MARANHÃO | Brasil | 2104081 | 21 | 33 | nan | nan | nan | Cerrado | 8.4 |
| 7dd452f7-3beb-35f6-9674-a959978a6a9a | -6.17426 | -45.43911 | 2024-09-28 04:19:00 | NOAA-21 | FERNANDO FALCÃO | MARANHÃO | Brasil | 2104081 | 21 | 33 | nan | nan | nan | Cerrado | 8.4 |
| bc296767-ab7e-3b8f-aeeb-5d6022d98deb | -6.1715 | -45.4351 | 2024-09-28 04:19:00 | NOAA-21 | FERNANDO FALCÃO | MARANHÃO | Brasil | 2104081 | 21 | 33 | nan | nan | nan | Cerrado | 8.4 |
| 03958960-87fd-3bba-97ca-409a9671dd79 | -6.17094 | -45.4386 | 2024-09-28 04:19:00 | NOAA-21 | FERNANDO FALCÃO | MARANHÃO | Brasil | 2104081 | 21 | 33 | nan | nan | nan | Cerrado | 8.4 |
| cff9d512-9e47-3456-ac8b-c4175e10aa6d | -7.83766 | -45.4879 | 2024-09-28 04:19:00 | NOAA-21 | RIBEIRO GONÇALVES | PIAUÍ | Brasil | 2208908 | 22 | 33 | nan | nan | nan | Cerrado | 1.2 |
| abd7a96b-6ea3-3d45-af98-40433ffe0500 | -7.83545 | -45.48041 | 2024-09-28 04:19:00 | NOAA-21 | RIBEIRO GONÇALVES | PIAUÍ | Brasil | 2208908 | 22 | 33 | nan | nan | nan | Cerrado | 2.4 |
| 2b83f266-40e0-32a9-8335-a6ac3fb9dd26 | -7.8349 | -45.48389 | 2024-09-28 04:19:00 | NOAA-21 | RIBEIRO GONÇALVES | PIAUÍ | Brasil | 2208908 | 22 | 33 | nan | nan | nan | Cerrado | 2.4 |
| 74ee1ddd-b1b1-33c2-8b25-9924df8e9906 | -7.83215 | -45.47987 | 2024-09-28 04:19:00 | NOAA-21 | RIBEIRO GONÇALVES | PIAUÍ | Brasil | 2208908 | 22 | 33 | nan | nan | nan | Cerrado | 2.4 |
| 87f99823-298e-3a1d-b5fb-9e3882a14d13 | -7.8316 | -45.48336 | 2024-09-28 04:19:00 | NOAA-21 | RIBEIRO GONÇALVES | PIAUÍ | Brasil | 2208908 | 22 | 33 | nan | nan | nan | Cerrado | 2.4 |
| 67f29e34-4d62-3bd9-98dc-067d535e1e62 | -7.82829 | -45.48283 | 2024-09-28 04:19:00 | NOAA-21 | RIBEIRO GONÇALVES | PIAUÍ | Brasil | 2208908 | 22 | 33 | nan | nan | nan | Cerrado | 3.5 |
| 764d86fb-a5d7-34da-987f-5161880a90da | -7.83327 | -45.53712 | 2024-09-28 04:19:00 | NOAA-21 | SAMBAÍBA | MARANHÃO | Brasil | 2109700 | 21 | 33 | nan | nan | nan | Cerrado | 4.3 |
| be63e053-4950-3f9d-ba5d-4286a55059f9 | -7.83272 | -45.54059 | 2024-09-28 04:19:00 | NOAA-21 | SAMBAÍBA | MARANHÃO | Brasil | 2109700 | 21 | 33 | nan | nan | nan | Cerrado | 4.3 |
| f24d369f-58c6-33c0-9657-e1007480ff9c | -7.82942 | -45.54005 | 2024-09-28 04:19:00 | NOAA-21 | SAMBAÍBA | MARANHÃO | Brasil | 2109700 | 21 | 33 | nan | nan | nan | Cerrado | 4.3 |
| 44586c8a-0e14-3d72-a935-4327b33342cb | -7.82611 | -45.53951 | 2024-09-28 04:19:00 | NOAA-21 | SAMBAÍBA | MARANHÃO | Brasil | 2109700 | 21 | 33 | nan | nan | nan | Cerrado | 1.8 |
| dd86cbc7-e6d8-3e8c-a79c-a628a8c23fd0 | -7.82502 | -45.54646 | 2024-09-28 04:19:00 | NOAA-21 | SAMBAÍBA | MARANHÃO | Brasil | 2109700 | 21 | 33 | nan | nan | nan | Cerrado | 2.6 |
| 596d8f1f-1d7d-372b-a78f-5a683069c26e | -7.82281 | -45.53898 | 2024-09-28 04:19:00 | NOAA-21 | SAMBAÍBA | MARANHÃO | Brasil | 2109700 | 21 | 33 | nan | nan | nan | Cerrado | 1.8 |
| 9b274270-a151-3625-96f2-78342687f77c | -7.82227 | -45.56384 | 2024-09-28 04:19:00 | NOAA-21 | SAMBAÍBA | MARANHÃO | Brasil | 2109700 | 21 | 33 | nan | nan | nan | Cerrado | 1.3 |
| 77ded95a-e913-36c2-8c6c-daa35f79152d | -7.82226 | -45.54245 | 2024-09-28 04:19:00 | NOAA-21 | SAMBAÍBA | MARANHÃO | Brasil | 2109700 | 21 | 33 | nan | nan | nan | Cerrado | 2.6 |
| 36d40f73-0895-3e12-9c72-4875076b113c | -7.82171 | -45.54591 | 2024-09-28 04:19:00 | NOAA-21 | SAMBAÍBA | MARANHÃO | Brasil | 2109700 | 21 | 33 | nan | nan | nan | Cerrado | 2.6 |
| 14e9a737-9251-3dc0-85ca-c7f4935f9548 | -7.82061 | -45.55285 | 2024-09-28 04:19:00 | NOAA-21 | SAMBAÍBA | MARANHÃO | Brasil | 2109700 | 21 | 33 | nan | nan | nan | Cerrado | 1.8 |
| bff2fffe-055b-3911-be38-565499a6670f | -7.81896 | -45.56329 | 2024-09-28 04:19:00 | NOAA-21 | SAMBAÍBA | MARANHÃO | Brasil | 2109700 | 21 | 33 | nan | nan | nan | Cerrado | 1.3 |
| fb29695d-a785-349c-90c0-eec541013964 | -7.81841 | -45.54537 | 2024-09-28 04:19:00 | NOAA-21 | SAMBAÍBA | MARANHÃO | Brasil | 2109700 | 21 | 33 | nan | nan | nan | Cerrado | 2.7 |
| 785740b4-ccce-3ac8-a1a6-d97a02909192 | -7.81786 | -45.57026 | 2024-09-28 04:19:00 | NOAA-21 | SAMBAÍBA | MARANHÃO | Brasil | 2109700 | 21 | 33 | nan | nan | nan | Cerrado | 2.4 |


[Clique aqui para ver as próximas entradas](README42.md)
