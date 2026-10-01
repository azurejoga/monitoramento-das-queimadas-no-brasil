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

## Dados Diários - Página 47

| ID | Latitude | Longitude | Data/Hora GMT | Satélite | Município | Estado | País | Município ID | Estado ID | País ID | Dias sem Chuva | Precipitação | Risco de Fogo | Bioma | FRP |
|----|----------|-----------|---------------|----------|-----------|--------|------|--------------|-----------|---------|----------------|--------------|----------------|-------|-----|
| d607828e-531a-394a-a42a-329ffa0773ad | -4.27941 | -50.74743 | 2026-10-01 04:32:00 | NOAA-20 | NOVO REPARTIMENTO | PARÁ | Brasil | 1505064 | 15 | 33 | nan | nan | nan | Amazônia | 9.1 |
| d417c3d2-13a4-3438-a5ce-4579ba5bb00f | -5.42987 | -43.44836 | 2026-10-01 04:32:00 | NOAA-20 | MATÕES | MARANHÃO | Brasil | 2106607 | 21 | 33 | nan | nan | nan | Cerrado | 6.3 |
| f5639f11-a592-3fe8-8af3-6d3ba08291a4 | -3.16537 | -54.07865 | 2026-10-01 04:32:00 | NOAA-20 | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | 2.4 |
| 49c2357c-9a92-34a7-8828-a76d859d6ea7 | -3.16586 | -54.08302 | 2026-10-01 04:32:00 | NOAA-20 | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | 11.6 |
| 90d78ba2-31b9-3119-bccd-99514d026586 | -1.23395 | -48.23264 | 2026-10-01 04:32:00 | NOAA-20 | SANTA BÁRBARA DO PARÁ | PARÁ | Brasil | 1506351 | 15 | 33 | nan | nan | nan | Amazônia | 0.7 |
| dc736dcd-b188-338d-9f31-0b3a96f0e80c | -1.67509 | -55.31161 | 2026-10-01 04:32:00 | NOAA-20 | ÓBIDOS | PARÁ | Brasil | 1505106 | 15 | 33 | nan | nan | nan | Amazônia | 0.8 |
| db97b7bd-d371-3215-823c-dde5ef2165b9 | -3.02875 | -51.27208 | 2026-10-01 04:32:00 | NOAA-20 | ANAPU | PARÁ | Brasil | 1500859 | 15 | 33 | nan | nan | nan | Amazônia | 5.0 |
| fe64ad58-0c4c-35a8-9bc1-ea357bea01f4 | -3.4821 | -49.92267 | 2026-10-01 04:32:00 | NOAA-20 | PACAJÁ | PARÁ | Brasil | 1505486 | 15 | 33 | nan | nan | nan | Amazônia | 1.6 |
| afda2da9-d528-3e98-8f1c-0e85d41ff5d9 | -3.58529 | -53.99712 | 2026-10-01 04:32:00 | NOAA-20 | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | 2.7 |
| 1d8e6690-09bc-30da-b8ac-d2e12791f260 | -5.75221 | -45.15638 | 2026-10-01 04:32:00 | NOAA-20 | BARRA DO CORDA | MARANHÃO | Brasil | 2101608 | 21 | 33 | nan | nan | nan | Cerrado | 5.3 |
| 36f4899d-b239-377e-94ed-ea6a2ab6520a | -4.06504 | -51.10649 | 2026-10-01 04:32:00 | NOAA-20 | PACAJÁ | PARÁ | Brasil | 1505486 | 15 | 33 | nan | nan | nan | Amazônia | 1.3 |
| 5887f324-14ff-3609-9493-6cb4ebc6ba47 | -3.11221 | -50.27015 | 2026-10-01 04:32:00 | NOAA-20 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 2.0 |
| 6470030c-6c2a-3058-8a00-b19bdbfb4b06 | -3.16806 | -54.10139 | 2026-10-01 04:32:00 | NOAA-20 | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | 19.5 |
| ab36f12f-c307-383f-aa0b-723cd0fa94a8 | -5.17706 | -46.19982 | 2026-10-01 04:32:00 | NOAA-20 | ARAME | MARANHÃO | Brasil | 2100956 | 21 | 33 | nan | nan | nan | Amazônia | 11.7 |
| 13c93783-a5ad-3f75-b393-81e8b065b034 | -7.32432 | -42.07704 | 2026-10-01 04:32:00 | NOAA-20 | COLÔNIA DO PIAUÍ | PIAUÍ | Brasil | 2202778 | 22 | 33 | nan | nan | nan | Caatinga | 5.8 |
| 5827cb9f-4c7f-306a-9079-0f0064f22efc | -4.6281 | -50.61054 | 2026-10-01 04:32:00 | NOAA-20 | NOVO REPARTIMENTO | PARÁ | Brasil | 1505064 | 15 | 33 | nan | nan | nan | Amazônia | 4.4 |
| 52e8f3de-2926-3f0e-bdeb-ceb259de3c1c | -4.04872 | -54.23526 | 2026-10-01 04:32:00 | NOAA-20 | PLACAS | PARÁ | Brasil | 1505650 | 15 | 33 | nan | nan | nan | Amazônia | 1.9 |
| b6993378-947c-31da-96af-815915380079 | -3.48494 | -54.73146 | 2026-10-01 04:32:00 | NOAA-20 | MOJUÍ DOS CAMPOS | PARÁ | Brasil | 1504752 | 15 | 33 | nan | nan | nan | Amazônia | 1.0 |
| 030770a9-40b4-3bf3-999b-a1f95478a33e | -2.99001 | -51.02702 | 2026-10-01 04:32:00 | NOAA-20 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 6.0 |
| 97ee6c8a-d351-3516-af01-37de93c37088 | -3.11532 | -50.27573 | 2026-10-01 04:32:00 | NOAA-20 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 4.1 |
| 50c0bf5c-68d3-3233-af07-62ec4fb9685d | -4.44263 | -50.66262 | 2026-10-01 04:32:00 | NOAA-20 | NOVO REPARTIMENTO | PARÁ | Brasil | 1505064 | 15 | 33 | nan | nan | nan | Amazônia | 2.8 |
| 7b6f34c9-9ae1-3a89-850d-0fffeee2383c | -4.45388 | -47.92004 | 2026-10-01 04:32:00 | NOAA-20 | DOM ELISEU | PARÁ | Brasil | 1502939 | 15 | 33 | nan | nan | nan | Amazônia | 15.7 |
| 60a27a25-2e04-3fa2-8335-34dd87ec5f86 | -4.2717 | -50.79359 | 2026-10-01 04:32:00 | NOAA-20 | PACAJÁ | PARÁ | Brasil | 1505486 | 15 | 33 | nan | nan | nan | Amazônia | 15.7 |
| 7634df84-9d6d-3910-ac8e-5779a5028509 | -1.47135 | -48.90238 | 2026-10-01 04:32:00 | NOAA-20 | PONTA DE PEDRAS | PARÁ | Brasil | 1505700 | 15 | 33 | nan | nan | nan | Amazônia | 3.2 |
| cffe829e-6211-3c6c-9384-00a5bd48dd1a | -4.28535 | -50.78517 | 2026-10-01 04:32:00 | NOAA-20 | NOVO REPARTIMENTO | PARÁ | Brasil | 1505064 | 15 | 33 | nan | nan | nan | Amazônia | 243.8 |
| 1f3d7525-13ca-300d-82b9-8455624d0448 | -5.18354 | -48.26741 | 2026-10-01 04:32:00 | NOAA-20 | SÃO PEDRO DA ÁGUA BRANCA | MARANHÃO | Brasil | 2111532 | 21 | 33 | nan | nan | nan | Amazônia | 0.7 |
| d49b6397-8d9d-356a-851b-e2fc085bcdfe | -2.89693 | -54.09109 | 2026-10-01 04:32:00 | NOAA-20 | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | 1.5 |
| 0ae7f034-7c03-3953-a99b-5edb9a083769 | -5.11524 | -56.01553 | 2026-10-01 04:32:00 | NOAA-20 | TRAIRÃO | PARÁ | Brasil | 1508050 | 15 | 33 | nan | nan | nan | Amazônia | 1.7 |
| 29643700-d27d-3dcd-9f45-1a4c43004358 | -4.26581 | -50.75571 | 2026-10-01 04:32:00 | NOAA-20 | NOVO REPARTIMENTO | PARÁ | Brasil | 1505064 | 15 | 33 | nan | nan | nan | Amazônia | 77.9 |
| 730446b0-7c50-3f8e-b19d-275ed5406b33 | -3.98174 | -56.09073 | 2026-10-01 04:32:00 | NOAA-20 | ITAITUBA | PARÁ | Brasil | 1503606 | 15 | 33 | nan | nan | nan | Amazônia | 1.6 |
| 053a22ea-ff0d-34e0-9863-db7fdf601b09 | -1.91654 | -55.05258 | 2026-10-01 04:32:00 | NOAA-20 | CURUÁ | PARÁ | Brasil | 1502855 | 15 | 33 | nan | nan | nan | Amazônia | 4.0 |
| ac0fb466-6154-3f00-bcf5-8f184d79cfa7 | -3.21924 | -48.81524 | 2026-10-01 04:32:00 | NOAA-20 | TAILÂNDIA | PARÁ | Brasil | 1507953 | 15 | 33 | nan | nan | nan | Amazônia | 1.3 |
| 6e00eb36-c93c-3ccf-bf66-d554c0307fa0 | -3.42426 | -54.5443 | 2026-10-01 04:32:00 | NOAA-20 | PLACAS | PARÁ | Brasil | 1505650 | 15 | 33 | nan | nan | nan | Amazônia | 0.8 |
| fbee7ea9-2f7f-3461-a747-a5036dc352be | -3.01451 | -53.87852 | 2026-10-01 04:32:00 | NOAA-20 | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | 2.3 |
| 1276114a-c1a2-3013-bb0e-ab8758832b61 | -3.54732 | -41.57077 | 2026-10-01 04:32:00 | NOAA-20 | COCAL | PIAUÍ | Brasil | 2202703 | 22 | 33 | nan | nan | nan | Caatinga | 2.4 |
| f4d51ba4-b6f8-3daf-8c3f-ae1d290507d8 | -3.17407 | -54.09641 | 2026-10-01 04:32:00 | NOAA-20 | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | 13.6 |
| 21dff7e5-57c6-386f-b5f1-e292370933a4 | -4.26892 | -50.76145 | 2026-10-01 04:32:00 | NOAA-20 | NOVO REPARTIMENTO | PARÁ | Brasil | 1505064 | 15 | 33 | nan | nan | nan | Amazônia | 16.1 |
| b6814260-34bf-39fc-9f1f-5ca838702b9d | -2.18799 | -46.1511 | 2026-10-01 04:32:00 | NOAA-20 | CENTRO NOVO DO MARANHÃO | MARANHÃO | Brasil | 2103174 | 21 | 33 | nan | nan | nan | Amazônia | 1.0 |
| 931df426-1374-357a-bd2a-50db77410d8f | -2.9166 | -51.32097 | 2026-10-01 04:32:00 | NOAA-20 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 4.8 |
| 9fcd4ecc-1cef-34e7-9fad-ebef26950e02 | -3.01759 | -53.89078 | 2026-10-01 04:32:00 | NOAA-20 | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | 2.5 |
| 70d7b95b-5635-3e16-b50c-0b0c5aebf1dc | -4.26922 | -50.74408 | 2026-10-01 04:32:00 | NOAA-20 | NOVO REPARTIMENTO | PARÁ | Brasil | 1505064 | 15 | 33 | nan | nan | nan | Amazônia | 6.7 |
| b78d2601-a51d-38d6-b9e3-f63ee5fc3229 | -4.28958 | -50.75971 | 2026-10-01 04:32:00 | NOAA-20 | NOVO REPARTIMENTO | PARÁ | Brasil | 1505064 | 15 | 33 | nan | nan | nan | Amazônia | 20.0 |
| 68a4e5b2-7448-392e-b828-919d10323e8b | -1.44169 | -54.46326 | 2026-10-01 04:32:00 | NOAA-20 | MONTE ALEGRE | PARÁ | Brasil | 1504802 | 15 | 33 | nan | nan | nan | Amazônia | 0.8 |
| e7712724-677e-3945-a41a-220a5edb2ac1 | -2.87889 | -54.87925 | 2026-10-01 04:32:00 | NOAA-20 | BELTERRA | PARÁ | Brasil | 1501451 | 15 | 33 | nan | nan | nan | Amazônia | 3.0 |
| 01730f6e-bdf8-37cd-8703-9af427e5ad74 | -3.26678 | -50.70688 | 2026-10-01 04:32:00 | NOAA-20 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 1.1 |
| 053c52e2-b80a-37d9-9c15-373dcef98671 | -3.48528 | -54.72775 | 2026-10-01 04:32:00 | NOAA-20 | MOJUÍ DOS CAMPOS | PARÁ | Brasil | 1504752 | 15 | 33 | nan | nan | nan | Amazônia | 1.1 |
| b390faca-450d-3481-8b0e-ee64af409d93 | -4.03713 | -54.24245 | 2026-10-01 04:32:00 | NOAA-20 | PLACAS | PARÁ | Brasil | 1505650 | 15 | 33 | nan | nan | nan | Amazônia | 3.1 |
| 071d448f-ee5c-3e57-9fdd-bb425990250a | -5.36706 | -46.22315 | 2026-10-01 04:32:00 | NOAA-20 | GRAJAÚ | MARANHÃO | Brasil | 2104800 | 21 | 33 | nan | nan | nan | Amazônia | 1.2 |
| 849f6819-7f10-3947-8a7b-029de8d16baf | -3.80637 | -51.03059 | 2026-10-01 04:32:00 | NOAA-20 | PACAJÁ | PARÁ | Brasil | 1505486 | 15 | 33 | nan | nan | nan | Amazônia | 8.2 |
| b3747ea9-1258-38ef-b5d6-47e5986145aa | -4.26677 | -50.75932 | 2026-10-01 04:32:00 | NOAA-20 | NOVO REPARTIMENTO | PARÁ | Brasil | 1505064 | 15 | 33 | nan | nan | nan | Amazônia | 13.8 |
| b0e9f768-c43d-36b7-b4d1-73fdbc364e24 | -4.1589 | -48.89244 | 2026-10-01 04:32:00 | NOAA-20 | GOIANÉSIA DO PARÁ | PARÁ | Brasil | 1503093 | 15 | 33 | nan | nan | nan | Amazônia | 1.5 |
| 1ac50be2-edfc-3a07-a4b9-e741898c3b54 | -4.2613 | -50.73413 | 2026-10-01 04:32:00 | NOAA-20 | NOVO REPARTIMENTO | PARÁ | Brasil | 1505064 | 15 | 33 | nan | nan | nan | Amazônia | 2.9 |
| cdff0d21-575f-3952-8279-b0f8a74828fc | -4.29726 | -50.78711 | 2026-10-01 04:32:00 | NOAA-20 | NOVO REPARTIMENTO | PARÁ | Brasil | 1505064 | 15 | 33 | nan | nan | nan | Amazônia | 11.7 |
| f53a2bbe-558d-3562-8945-6fbbed4b2d01 | -2.50047 | -56.91579 | 2026-10-01 04:32:00 | NOAA-20 | PARINTINS | AMAZONAS | Brasil | 1303403 | 13 | 33 | nan | nan | nan | Amazônia | 2.2 |
| adcfd315-a365-3dc1-8906-fd145879fef9 | 1.71079 | -55.91496 | 2026-10-01 04:32:00 | NOAA-20 | ORIXIMINÁ | PARÁ | Brasil | 1505304 | 15 | 33 | nan | nan | nan | Amazônia | 0.4 |
| bfc484d4-a461-3f09-8941-6762608fd4ce | -5.74496 | -45.15889 | 2026-10-01 04:32:00 | NOAA-20 | BARRA DO CORDA | MARANHÃO | Brasil | 2101608 | 21 | 33 | nan | nan | nan | Cerrado | 4.6 |
| 560a8a8e-e6aa-3b8f-b0e3-2d39b1a01f1a | -4.03774 | -54.23887 | 2026-10-01 04:32:00 | NOAA-20 | PLACAS | PARÁ | Brasil | 1505650 | 15 | 33 | nan | nan | nan | Amazônia | 3.1 |
| 35ad7625-201c-363f-8be3-23a34f382b8d | -6.74205 | -44.14106 | 2026-10-01 04:32:00 | NOAA-20 | NOVA IORQUE | MARANHÃO | Brasil | 2107308 | 21 | 33 | nan | nan | nan | Cerrado | 2.4 |
| 9f088a54-c045-31bf-b903-ff30984c66a5 | -5.76337 | -45.15083 | 2026-10-01 04:32:00 | NOAA-20 | BARRA DO CORDA | MARANHÃO | Brasil | 2101608 | 21 | 33 | nan | nan | nan | Cerrado | 4.6 |
| a4b0ffde-7b93-39ef-9405-c6b49e33e8af | -3.17251 | -54.09779 | 2026-10-01 04:32:00 | NOAA-20 | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | 14.1 |
| 8fd1a750-1817-38a6-ad0f-0bd8e414aff6 | -3.16299 | -54.10057 | 2026-10-01 04:32:00 | NOAA-20 | SANTARÉM | PARÁ | Brasil | 1506807 | 15 | 33 | nan | nan | nan | Amazônia | 1.8 |
| e47609fd-f564-3fd2-9b92-ce91899993e1 | -1.33064 | -47.78519 | 2026-10-01 04:32:00 | NOAA-20 | CASTANHAL | PARÁ | Brasil | 1502400 | 15 | 33 | nan | nan | nan | Amazônia | 1.1 |
| da24a95d-f281-3b52-af68-e0cca1a0be75 | -5.44224 | -43.74497 | 2026-10-01 04:32:00 | NOAA-20 | PARNARAMA | MARANHÃO | Brasil | 2107803 | 21 | 33 | nan | nan | nan | Cerrado | 2.3 |
| aa6f1b73-432c-3b61-999b-8932af9b90e7 | -3.85667 | -51.94794 | 2026-10-01 04:32:00 | NOAA-20 | SENADOR JOSÉ PORFÍRIO | PARÁ | Brasil | 1507805 | 15 | 33 | nan | nan | nan | Amazônia | 2.7 |
| 13c91063-a5d1-3ebe-96a8-ca80c05551a8 | -2.9606 | -51.026 | 2026-10-01 04:32:00 | NOAA-20 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 2.1 |
| d27dda57-22e1-3143-aceb-3661f5548497 | -3.16538 | -54.08594 | 2026-10-01 04:32:00 | NOAA-20 | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | 6.8 |
| ffe9f08f-2d26-38e6-8e7d-77c4a09920d2 | -3.00878 | -51.06805 | 2026-10-01 04:32:00 | NOAA-20 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 3.2 |
| f3132681-a922-3b90-bc49-7fff07434f8d | -4.2927 | -50.76543 | 2026-10-01 04:32:00 | NOAA-20 | NOVO REPARTIMENTO | PARÁ | Brasil | 1505064 | 15 | 33 | nan | nan | nan | Amazônia | 10.7 |
| 9304d263-cbd9-3eaf-bc71-603a14e326bb | -2.98118 | -51.02935 | 2026-10-01 04:32:00 | NOAA-20 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 3.6 |
| 87e5b0a6-35e0-3a24-b53d-5d816c27d41f | -3.03996 | -53.87993 | 2026-10-01 04:32:00 | NOAA-20 | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | 0.9 |
| c3bd89ce-74c4-36b7-b1b8-b095c066a495 | -4.30007 | -50.74554 | 2026-10-01 04:32:00 | NOAA-20 | NOVO REPARTIMENTO | PARÁ | Brasil | 1505064 | 15 | 33 | nan | nan | nan | Amazônia | 1.8 |
| 40039b87-c30a-3307-afda-129ff62f5fe3 | -5.10479 | -45.66803 | 2026-10-01 04:32:00 | NOAA-20 | ITAIPAVA DO GRAJAÚ | MARANHÃO | Brasil | 2105351 | 21 | 33 | nan | nan | nan | Cerrado | 0.9 |
| 9d6b8d2c-e8cf-362b-acdd-0ac5ceb9cad2 | -5.74313 | -45.06038 | 2026-10-01 04:32:00 | NOAA-20 | BARRA DO CORDA | MARANHÃO | Brasil | 2101608 | 21 | 33 | nan | nan | nan | Cerrado | 1.3 |
| 648e2895-08f0-3dd4-abbf-12093d745522 | -4.2595 | -50.77927 | 2026-10-01 04:32:00 | NOAA-20 | PACAJÁ | PARÁ | Brasil | 1505486 | 15 | 33 | nan | nan | nan | Amazônia | 4.2 |
| 2c0a8c56-1363-3d37-85b6-659e979152f5 | -4.28647 | -50.75393 | 2026-10-01 04:32:00 | NOAA-20 | NOVO REPARTIMENTO | PARÁ | Brasil | 1505064 | 15 | 33 | nan | nan | nan | Amazônia | 3.9 |
| be1d18fc-f02e-3c45-ae3b-5046cb3c1908 | -3.16895 | -54.08817 | 2026-10-01 04:32:00 | NOAA-20 | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | 6.1 |
| 737c3eef-9ebe-3dd4-bc47-12e0b493e450 | -4.25652 | -50.74714 | 2026-10-01 04:32:00 | NOAA-20 | NOVO REPARTIMENTO | PARÁ | Brasil | 1505064 | 15 | 33 | nan | nan | nan | Amazônia | 16.3 |
| f42843de-8cdb-3b41-bf68-a79c02dcb0cf | -6.69373 | -45.62809 | 2026-10-01 04:32:00 | NOAA-20 | MIRADOR | MARANHÃO | Brasil | 2106706 | 21 | 33 | nan | nan | nan | Cerrado | 1.4 |
| d01a5481-be15-3e0f-937f-03ee9f0afaab | -3.34858 | -42.40648 | 2026-10-01 04:32:00 | NOAA-20 | SÃO BERNARDO | MARANHÃO | Brasil | 2110609 | 21 | 33 | nan | nan | nan | Caatinga | 1.9 |
| 02dc0557-6d34-30c8-94dc-2b14970101ed | -4.26751 | -50.74561 | 2026-10-01 04:32:00 | NOAA-20 | NOVO REPARTIMENTO | PARÁ | Brasil | 1505064 | 15 | 33 | nan | nan | nan | Amazônia | 6.7 |
| 67e44b3d-4aac-3cbc-8be6-9bbf42645081 | -3.41585 | -48.33598 | 2026-10-01 04:32:00 | NOAA-20 | PARAGOMINAS | PARÁ | Brasil | 1505502 | 15 | 33 | nan | nan | nan | Amazônia | 1.7 |
| 4ea96f65-f2a8-3994-8966-51b375d8e782 | -3.15525 | -54.08434 | 2026-10-01 04:32:00 | NOAA-20 | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | 1.5 |
| 90e05f3c-b3ff-3068-8687-2e06f0d1c0cf | -5.86648 | -50.16157 | 2026-10-01 04:32:00 | NOAA-20 | MARABÁ | PARÁ | Brasil | 1504208 | 15 | 33 | nan | nan | nan | Amazônia | 1.4 |
| d8286c0c-4d1c-3111-a65d-c7aa5f5d6e52 | -4.29414 | -50.78133 | 2026-10-01 04:32:00 | NOAA-20 | NOVO REPARTIMENTO | PARÁ | Brasil | 1505064 | 15 | 33 | nan | nan | nan | Amazônia | 30.6 |
| 769f9b33-6c3d-311e-a1f8-cf74fbbaecc1 | -2.84606 | -45.1289 | 2026-10-01 04:32:00 | NOAA-20 | SÃO BENTO | MARANHÃO | Brasil | 2110500 | 21 | 33 | nan | nan | nan | Amazônia | 0.7 |
| 350485f0-ec85-3ab1-9306-783fe536d7e9 | -4.30147 | -50.76165 | 2026-10-01 04:32:00 | NOAA-20 | NOVO REPARTIMENTO | PARÁ | Brasil | 1505064 | 15 | 33 | nan | nan | nan | Amazônia | 6.4 |
| 50f0a570-ad45-34c0-97db-209adac5968d | 1.04107 | -50.0205 | 2026-10-01 04:32:00 | NOAA-20 | MACAPÁ | AMAPÁ | Brasil | 1600303 | 16 | 33 | nan | nan | nan | Amazônia | 1.8 |
| 765ce8f5-ec38-393a-8be5-8a099da953ac | 1.87684 | -55.64941 | 2026-10-01 04:32:00 | NOAA-20 | ÓBIDOS | PARÁ | Brasil | 1505106 | 15 | 33 | nan | nan | nan | Amazônia | 0.8 |
| ee111717-016d-342c-b188-e3981dc10361 | -3.15669 | -54.07555 | 2026-10-01 04:32:00 | NOAA-20 | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | 3.7 |
| 75b3232e-c522-3c1d-a026-ba902add9405 | -5.74776 | -45.16295 | 2026-10-01 04:32:00 | NOAA-20 | BARRA DO CORDA | MARANHÃO | Brasil | 2101608 | 21 | 33 | nan | nan | nan | Cerrado | 4.6 |
| b17dbba9-0248-3ce7-a2de-195a890e7ac0 | -2.82987 | -48.64862 | 2026-10-01 04:32:00 | NOAA-20 | TAILÂNDIA | PARÁ | Brasil | 1507953 | 15 | 33 | nan | nan | nan | Amazônia | 1.1 |
| 4c5bd037-8fd7-3e70-beab-6c3ffb42eb09 | -5.7606 | -45.16854 | 2026-10-01 04:32:00 | NOAA-20 | BARRA DO CORDA | MARANHÃO | Brasil | 2101608 | 21 | 33 | nan | nan | nan | Cerrado | 2.2 |
| 2775b09b-93f2-34a6-97da-e4485e7d2ac6 | -3.9773 | -41.51744 | 2026-10-01 04:32:00 | NOAA-20 | PIRACURUCA | PIAUÍ | Brasil | 2208304 | 22 | 33 | nan | nan | nan | Caatinga | 1.4 |
| a4df7428-321c-34eb-977a-f3e32e99f40e | -4.25734 | -50.74209 | 2026-10-01 04:32:00 | NOAA-20 | NOVO REPARTIMENTO | PARÁ | Brasil | 1505064 | 15 | 33 | nan | nan | nan | Amazônia | 5.9 |
| ac38b4db-b283-302e-8d6a-d6dd66535b35 | -3.01806 | -53.88794 | 2026-10-01 04:32:00 | NOAA-20 | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | 2.5 |
| 99e152fe-2d22-3ff5-9514-d0e6d0c1ffca | -5.71703 | -46.20045 | 2026-10-01 04:32:00 | NOAA-20 | GRAJAÚ | MARANHÃO | Brasil | 2104800 | 21 | 33 | nan | nan | nan | Cerrado | 1.2 |
| ae3b38c5-44cb-35f3-9f4c-e433b9b112c4 | -4.25442 | -50.77495 | 2026-10-01 04:32:00 | NOAA-20 | PACAJÁ | PARÁ | Brasil | 1505486 | 15 | 33 | nan | nan | nan | Amazônia | 5.0 |
| d13bd851-c06d-35b3-9104-3a0faabba8c1 | -6.70564 | -45.98458 | 2026-10-01 04:32:00 | NOAA-20 | FORTALEZA DOS NOGUEIRAS | MARANHÃO | Brasil | 2104107 | 21 | 33 | nan | nan | nan | Cerrado | 1.3 |
| 1fb3390a-9452-3e57-8930-233cc4f1d202 | -3.37677 | -50.85189 | 2026-10-01 04:32:00 | NOAA-20 | PACAJÁ | PARÁ | Brasil | 1505486 | 15 | 33 | nan | nan | nan | Amazônia | 0.7 |
| 2717b5b2-9f43-3838-8411-75f2a7dbe5fc | -3.17606 | -54.1075 | 2026-10-01 04:32:00 | NOAA-20 | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | 9.0 |


[Clique aqui para ver as próximas entradas](README48.md)
