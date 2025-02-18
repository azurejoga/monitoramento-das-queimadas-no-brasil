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

## Dados Diários - Página 1

| ID | Latitude | Longitude | Data/Hora GMT | Satélite | Município | Estado | País | Município ID | Estado ID | País ID | Dias sem Chuva | Precipitação | Risco de Fogo | Bioma | FRP |
|----|----------|-----------|---------------|----------|-----------|--------|------|--------------|-----------|---------|----------------|--------------|----------------|-------|-----|
| 776272b1-dac5-30c1-b14f-b0ffe680641f | -19.0789 | -56.0516 | 2025-02-18 00:00:00 | GOES-16 | CORUMBÁ | MATO GROSSO DO SUL | Brasil | 5003207 | 50 | 33 | nan | nan | nan | Pantanal | 67.7 |
| f8db6c95-34fe-3b2b-b95f-d68547e05d7c | -19.1357 | -56.2114 | 2025-02-18 00:00:00 | GOES-16 | CORUMBÁ | MATO GROSSO DO SUL | Brasil | 5003207 | 50 | 33 | nan | nan | nan | Pantanal | 78.3 |
| c9cc25f3-233d-30c2-b718-3f2008c91b44 | -19.0785 | -56.0727 | 2025-02-18 00:00:00 | GOES-16 | CORUMBÁ | MATO GROSSO DO SUL | Brasil | 5003207 | 50 | 33 | nan | nan | nan | Pantanal | 64.9 |
| dd30aa8d-1276-3c37-b566-9b6683dc3a9b | -19.1153 | -56.2352 | 2025-02-18 00:00:00 | GOES-16 | CORUMBÁ | MATO GROSSO DO SUL | Brasil | 5003207 | 50 | 33 | nan | nan | nan | Pantanal | 98.6 |
| 780d8467-9ec5-3880-a316-56b236564293 | -19.0589 | -56.0545 | 2025-02-18 00:00:00 | GOES-16 | CORUMBÁ | MATO GROSSO DO SUL | Brasil | 5003207 | 50 | 33 | nan | nan | nan | Pantanal | 60.8 |
| a288e00e-cd23-3320-aad4-93cbc426e2e9 | -19.1353 | -56.2324 | 2025-02-18 00:00:00 | GOES-16 | CORUMBÁ | MATO GROSSO DO SUL | Brasil | 5003207 | 50 | 33 | nan | nan | nan | Pantanal | 99.1 |
| c2696cda-b96e-38fc-9e4c-64fa4b216ddf | -19.1157 | -56.2142 | 2025-02-18 00:00:00 | GOES-16 | CORUMBÁ | MATO GROSSO DO SUL | Brasil | 5003207 | 50 | 33 | nan | nan | nan | Pantanal | 84.0 |
| 29de9943-1a18-337d-a547-d60043037144 | -10.6191 | -45.1132 | 2025-02-18 00:00:00 | GOES-16 | CORRENTE | PIAUÍ | Brasil | 2202901 | 22 | 33 | nan | nan | nan | Cerrado | 104.2 |
| edd58000-3ad4-3dbc-8d33-32fe5631c2a1 | -10.6108 | -45.101002 | 2025-02-18 00:05:00 | METOP-C | CORRENTE | PIAUÍ | Brasil | 2202901 | 22 | 33 | nan | nan | nan | Cerrado | nan |
| 38bb0231-bc25-3f66-b09b-d704f27ad8bb | -10.6138 | -45.1157 | 2025-02-18 00:05:00 | METOP-C | CORRENTE | PIAUÍ | Brasil | 2202901 | 22 | 33 | nan | nan | nan | Cerrado | nan |
| 24eda97a-d38b-3ac8-931e-6be9e5a48e2b | -11.5838 | -44.8423 | 2025-02-18 00:05:00 | METOP-C | RIACHÃO DAS NEVES | BAHIA | Brasil | 2926202 | 29 | 33 | nan | nan | nan | Cerrado | nan |
| 2662cd14-f123-3328-a09c-85c21b622d12 | -10.6041 | -45.117699 | 2025-02-18 00:05:00 | METOP-C | CORRENTE | PIAUÍ | Brasil | 2202901 | 22 | 33 | nan | nan | nan | Cerrado | nan |
| a14cbfb9-e1c8-3691-b343-2048e74e7fb8 | -21.3978 | -48.522202 | 2025-02-18 00:05:00 | METOP-C | TAQUARITINGA | SÃO PAULO | Brasil | 3553708 | 35 | 33 | nan | nan | nan | Cerrado | nan |
| 1d3dea06-ba8b-30d9-8948-eb9153378d65 | -9.178 | -40.305302 | 2025-02-18 00:05:00 | METOP-C | PETROLINA | PERNAMBUCO | Brasil | 2611101 | 26 | 33 | nan | nan | nan | Caatinga | nan |
| d017fbc9-0546-3c4d-afec-0492eedf9089 | -21.359301 | -48.528198 | 2025-02-18 00:05:00 | METOP-C | TAQUARITINGA | SÃO PAULO | Brasil | 3553708 | 35 | 33 | nan | nan | nan | Cerrado | nan |
| 3cc51e6d-6402-3667-b941-5d3de50b1d73 | -7.389 | -35.203098 | 2025-02-18 00:05:00 | METOP-C | ITAMBÉ | PERNAMBUCO | Brasil | 2607653 | 26 | 33 | nan | nan | nan | Mata Atlântica | nan |
| 7dd6c9a4-4300-3f79-a3e8-bb47fdd3a2ed | -19.168699 | -40.134399 | 2025-02-18 00:05:00 | METOP-C | SOORETAMA | ESPÍRITO SANTO | Brasil | 3205010 | 32 | 33 | nan | nan | nan | Mata Atlântica | nan |
| 38ac7448-07c1-3605-bf9c-63cc38e9f5da | -10.5981 | -45.088402 | 2025-02-18 00:05:00 | METOP-C | CORRENTE | PIAUÍ | Brasil | 2202901 | 22 | 33 | nan | nan | nan | Cerrado | nan |
| 32cb0c38-0ed3-3391-8cb4-a60e6c344cf3 | -21.4074 | -48.520699 | 2025-02-18 00:05:00 | METOP-C | TAQUARITINGA | SÃO PAULO | Brasil | 3553708 | 35 | 33 | nan | nan | nan | Cerrado | nan |
| 60e40942-90be-3b58-907f-4185869724d4 | -19.1668 | -40.124699 | 2025-02-18 00:05:00 | METOP-C | SOORETAMA | ESPÍRITO SANTO | Brasil | 3205010 | 32 | 33 | nan | nan | nan | Mata Atlântica | nan |
| e5dee5a3-6540-3aee-ac52-0fdf05a53ea1 | -7.3792 | -35.205399 | 2025-02-18 00:05:00 | METOP-C | JURIPIRANGA | PARAÍBA | Brasil | 2507903 | 25 | 33 | nan | nan | nan | Mata Atlântica | nan |
| 4af0a102-3e30-3b48-b49a-f0d65ab96995 | -10.6011 | -45.103001 | 2025-02-18 00:05:00 | METOP-C | CORRENTE | PIAUÍ | Brasil | 2202901 | 22 | 33 | nan | nan | nan | Cerrado | nan |
| b5e35d44-73b9-3d77-81aa-75920f042e34 | -19.0789 | -56.0516 | 2025-02-18 00:10:00 | GOES-16 | CORUMBÁ | MATO GROSSO DO SUL | Brasil | 5003207 | 50 | 33 | nan | nan | nan | Pantanal | 58.3 |
| c5177d1c-d070-3538-8ac6-1c660a6c8034 | -19.1353 | -56.2324 | 2025-02-18 00:10:00 | GOES-16 | CORUMBÁ | MATO GROSSO DO SUL | Brasil | 5003207 | 50 | 33 | nan | nan | nan | Pantanal | 100.6 |
| 21a7f6ac-0072-38ac-ac84-31912a1b76aa | -19.1153 | -56.2352 | 2025-02-18 00:10:00 | GOES-16 | CORUMBÁ | MATO GROSSO DO SUL | Brasil | 5003207 | 50 | 33 | nan | nan | nan | Pantanal | 91.9 |
| b88b19af-a3ea-3250-8d97-e3eff2706247 | -19.1157 | -56.2142 | 2025-02-18 00:10:00 | GOES-16 | CORUMBÁ | MATO GROSSO DO SUL | Brasil | 5003207 | 50 | 33 | nan | nan | nan | Pantanal | 85.5 |
| 3fed82c5-9302-3ac1-b5c9-acbf784e11df | -19.0589 | -56.0545 | 2025-02-18 00:10:00 | GOES-16 | CORUMBÁ | MATO GROSSO DO SUL | Brasil | 5003207 | 50 | 33 | nan | nan | nan | Pantanal | 57.0 |
| e4229682-719e-32a9-811d-aa85fa05a935 | -10.6195 | -45.0902 | 2025-02-18 00:10:00 | GOES-16 | CORRENTE | PIAUÍ | Brasil | 2202901 | 22 | 33 | nan | nan | nan | Cerrado | 76.1 |
| abc8c5f6-3e1b-3573-894b-8d5fc5435b76 | -19.1357 | -56.2114 | 2025-02-18 00:10:00 | GOES-16 | CORUMBÁ | MATO GROSSO DO SUL | Brasil | 5003207 | 50 | 33 | nan | nan | nan | Pantanal | 79.1 |
| 1b0b182e-71aa-3b01-9282-25db260462e8 | -19.0785 | -56.0727 | 2025-02-18 00:10:00 | GOES-16 | CORUMBÁ | MATO GROSSO DO SUL | Brasil | 5003207 | 50 | 33 | nan | nan | nan | Pantanal | 52.0 |
| e5bd9ab5-1a24-3e61-a1bb-95b38c988555 | -10.6191 | -45.1132 | 2025-02-18 00:10:00 | GOES-16 | CORRENTE | PIAUÍ | Brasil | 2202901 | 22 | 33 | nan | nan | nan | Cerrado | 92.6 |
| 764b582d-c56e-3b16-b02b-9f834ae476aa | -19.0585 | -56.0755 | 2025-02-18 00:10:00 | GOES-16 | CORUMBÁ | MATO GROSSO DO SUL | Brasil | 5003207 | 50 | 33 | nan | nan | nan | Pantanal | 48.9 |
| bd49829a-60fd-3810-878d-cbe30037d252 | -19.1353 | -56.2324 | 2025-02-18 00:20:00 | GOES-16 | CORUMBÁ | MATO GROSSO DO SUL | Brasil | 5003207 | 50 | 33 | nan | nan | nan | Pantanal | 88.5 |
| 5a99519a-f220-34ec-a941-f976d92315cf | -19.1153 | -56.2352 | 2025-02-18 00:20:00 | GOES-16 | CORUMBÁ | MATO GROSSO DO SUL | Brasil | 5003207 | 50 | 33 | nan | nan | nan | Pantanal | 86.3 |
| c71ae3e2-8f16-324e-8312-021ecf2a324e | -10.6191 | -45.1132 | 2025-02-18 00:20:00 | GOES-16 | CORRENTE | PIAUÍ | Brasil | 2202901 | 22 | 33 | nan | nan | nan | Cerrado | 98.8 |
| 157dab13-70e9-3425-9664-852766337463 | -19.1157 | -56.2142 | 2025-02-18 00:20:00 | GOES-16 | CORUMBÁ | MATO GROSSO DO SUL | Brasil | 5003207 | 50 | 33 | nan | nan | nan | Pantanal | 76.1 |
| 62db29a7-a640-31f4-bb0c-7049dcddab85 | -19.0589 | -56.0545 | 2025-02-18 00:20:00 | GOES-16 | CORUMBÁ | MATO GROSSO DO SUL | Brasil | 5003207 | 50 | 33 | nan | nan | nan | Pantanal | 63.1 |
| 7f7bd39a-f8ce-3f88-a5a3-726707977849 | -19.0789 | -56.0516 | 2025-02-18 00:20:00 | GOES-16 | CORUMBÁ | MATO GROSSO DO SUL | Brasil | 5003207 | 50 | 33 | nan | nan | nan | Pantanal | 64.1 |
| 45587a74-7536-3ec6-88cb-e54cae4b742f | -10.6195 | -45.0902 | 2025-02-18 00:20:00 | GOES-16 | CORRENTE | PIAUÍ | Brasil | 2202901 | 22 | 33 | nan | nan | nan | Cerrado | 74.2 |
| 4a026fef-2395-3309-a93d-cb48ef49ab4e | -21.3814 | -48.5616 | 2025-02-18 00:20:00 | GOES-16 | TAQUARITINGA | SÃO PAULO | Brasil | 3553708 | 35 | 33 | nan | nan | nan | Mata Atlântica | 74.7 |
| be639892-fcd2-3110-9106-614c9d094a70 | -19.1357 | -56.2114 | 2025-02-18 00:20:00 | GOES-16 | CORUMBÁ | MATO GROSSO DO SUL | Brasil | 5003207 | 50 | 33 | nan | nan | nan | Pantanal | 69.4 |
| d2041aee-a9b6-3cc1-b293-ef8a51ed9bda | -21.37953 | -48.57379 | 2025-02-18 00:26:00 | TERRA_M-M | TAQUARITINGA | SÃO PAULO | Brasil | 3553708 | 35 | 33 | nan | nan | nan | Mata Atlântica | 98.8 |
| 5851a961-0063-3d1f-8b2f-5aa201205e9d | -21.37289 | -48.57993 | 2025-02-18 00:26:00 | TERRA_M-M | TAQUARITINGA | SÃO PAULO | Brasil | 3553708 | 35 | 33 | nan | nan | nan | Mata Atlântica | 35.7 |
| e44a36b6-8975-3ad8-a791-f72a1f695a88 | -21.08769 | -43.14091 | 2025-02-18 00:26:00 | TERRA_M-M | DORES DO TURVO | MINAS GERAIS | Brasil | 3123304 | 31 | 33 | nan | nan | nan | Mata Atlântica | 8.5 |
| 26797b7d-098e-3e17-8c58-be63e287a211 | -20.19247 | -41.23976 | 2025-02-18 00:26:00 | TERRA_M-M | AFONSO CLÁUDIO | ESPÍRITO SANTO | Brasil | 3200102 | 32 | 33 | nan | nan | nan | Mata Atlântica | 9.2 |
| 369bc4c4-9af9-3f48-a054-67474443dcad | -20.21324 | -40.73138 | 2025-02-18 00:26:00 | TERRA_M-M | DOMINGOS MARTINS | ESPÍRITO SANTO | Brasil | 3201902 | 32 | 33 | nan | nan | nan | Mata Atlântica | 5.2 |
| be0a04d1-d096-3a40-9812-597e5ca159a2 | -21.36802 | -48.53019 | 2025-02-18 00:26:00 | TERRA_M-M | TAQUARITINGA | SÃO PAULO | Brasil | 3553708 | 35 | 33 | nan | nan | nan | Cerrado | 16.6 |
| 2caad6ed-3008-3e18-b5d0-b37d9f9bf56e | -21.37048 | -48.55523 | 2025-02-18 00:26:00 | TERRA_M-M | TAQUARITINGA | SÃO PAULO | Brasil | 3553708 | 35 | 33 | nan | nan | nan | Mata Atlântica | 13.9 |
| 61ef0e0c-ae89-37eb-8a64-97f9194827f1 | -19.16748 | -40.13087 | 2025-02-18 00:26:00 | TERRA_M-M | SOORETAMA | ESPÍRITO SANTO | Brasil | 3205010 | 32 | 33 | nan | nan | nan | Mata Atlântica | 7.4 |
| 9a9e6a30-f81f-36e3-b2c9-6bda2a58af33 | -21.41159 | -48.55067 | 2025-02-18 00:26:00 | TERRA_M-M | TAQUARITINGA | SÃO PAULO | Brasil | 3553708 | 35 | 33 | nan | nan | nan | Mata Atlântica | 28.9 |
| e4bc8280-32c8-3399-aa5f-4a72336ce424 | -21.42073 | -48.56929 | 2025-02-18 00:26:00 | TERRA_M-M | TAQUARITINGA | SÃO PAULO | Brasil | 3553708 | 35 | 33 | nan | nan | nan | Mata Atlântica | 25.7 |
| d4f3b361-9336-3e31-b0d3-bcf85e523b9e | -21.38658 | -48.57801 | 2025-02-18 00:26:00 | TERRA_M-M | TAQUARITINGA | SÃO PAULO | Brasil | 3553708 | 35 | 33 | nan | nan | nan | Mata Atlântica | 62.1 |
| 9992b048-8c5c-32aa-8c26-1ffb5f99aa72 | -21.41842 | -48.54473 | 2025-02-18 00:26:00 | TERRA_M-M | TAQUARITINGA | SÃO PAULO | Brasil | 3553708 | 35 | 33 | nan | nan | nan | Mata Atlântica | 36.8 |
| 7eba1299-f8d7-3f9f-aed4-5c9780e457d8 | -12.84806 | -43.82143 | 2025-02-18 00:28:00 | TERRA_M-M | SERRA DOURADA | BAHIA | Brasil | 2930303 | 29 | 33 | nan | nan | nan | Cerrado | 5.7 |
| 79da4014-042c-374d-9fcf-5eb9530d5c95 | -14.69775 | -49.87254 | 2025-02-18 00:28:00 | TERRA_M-M | CRIXÁS | GOIÁS | Brasil | 5206404 | 52 | 33 | nan | nan | nan | Cerrado | 15.2 |
| 47ee13c7-8fa0-3ff9-8b69-47e847eb2786 | -16.90269 | -43.66064 | 2025-02-18 00:28:00 | TERRA_M-M | GLAUCILÂNDIA | MINAS GERAIS | Brasil | 3127354 | 31 | 33 | nan | nan | nan | Cerrado | 6.5 |
| ee62fb09-f18a-3a0c-b5e7-a72bf90d5e30 | -11.59699 | -44.8514 | 2025-02-18 00:28:00 | TERRA_M-M | RIACHÃO DAS NEVES | BAHIA | Brasil | 2926202 | 29 | 33 | nan | nan | nan | Cerrado | 13.3 |
| 0530a71b-cf88-3d3a-80f1-50ad42e33b43 | -15.59918 | -41.79759 | 2025-02-18 00:28:00 | TERRA_M-M | SÃO JOÃO DO PARAÍSO | MINAS GERAIS | Brasil | 3162708 | 31 | 33 | nan | nan | nan | Mata Atlântica | 8.1 |
| 8ad75840-791d-34a5-abb2-46f5d1e88d69 | -12.03717 | -41.38805 | 2025-02-18 00:28:00 | TERRA_M-M | BONITO | BAHIA | Brasil | 2904050 | 29 | 33 | nan | nan | nan | Caatinga | 6.9 |
| 2c8d6232-d791-39ad-a45c-939196f2201a | -12.84932 | -43.83066 | 2025-02-18 00:28:00 | TERRA_M-M | SERRA DOURADA | BAHIA | Brasil | 2930303 | 29 | 33 | nan | nan | nan | Cerrado | 6.7 |
| 4d9b25e8-dd82-3356-8748-848777736efc | -10.6195 | -45.0902 | 2025-02-18 00:30:00 | GOES-16 | CORRENTE | PIAUÍ | Brasil | 2202901 | 22 | 33 | nan | nan | nan | Cerrado | 70.4 |
| ecf55a5c-7af3-3aa8-ac3b-6f82b59b19ab | -10.6191 | -45.1132 | 2025-02-18 00:30:00 | GOES-16 | CORRENTE | PIAUÍ | Brasil | 2202901 | 22 | 33 | nan | nan | nan | Cerrado | 88.5 |
| 109c0fae-92c5-3481-af93-9475cc0f0107 | -19.1357 | -56.2114 | 2025-02-18 00:30:00 | GOES-16 | CORUMBÁ | MATO GROSSO DO SUL | Brasil | 5003207 | 50 | 33 | nan | nan | nan | Pantanal | 60.6 |
| b30bca8d-c7a1-36e5-a6c2-86ecf6a512c3 | -19.0589 | -56.0545 | 2025-02-18 00:30:00 | GOES-16 | CORUMBÁ | MATO GROSSO DO SUL | Brasil | 5003207 | 50 | 33 | nan | nan | nan | Pantanal | 54.1 |
| 82c9f108-d28a-30b7-b6f8-bffa41905458 | -10.6 | -45.1158 | 2025-02-18 00:30:00 | GOES-16 | CORRENTE | PIAUÍ | Brasil | 2202901 | 22 | 33 | nan | nan | nan | Cerrado | 77.2 |
| 962c6067-28e8-36fe-a4dd-27375b0ec9ec | -19.0785 | -56.0727 | 2025-02-18 00:30:00 | GOES-16 | CORUMBÁ | MATO GROSSO DO SUL | Brasil | 5003207 | 50 | 33 | nan | nan | nan | Pantanal | 55.9 |
| 7ad71b85-2625-351f-9b66-b5d0ad17bf1d | -19.1153 | -56.2352 | 2025-02-18 00:30:00 | GOES-16 | CORUMBÁ | MATO GROSSO DO SUL | Brasil | 5003207 | 50 | 33 | nan | nan | nan | Pantanal | 76.0 |
| ef0d8da8-039a-36ba-9288-beae158e2f63 | -19.1353 | -56.2324 | 2025-02-18 00:30:00 | GOES-16 | CORUMBÁ | MATO GROSSO DO SUL | Brasil | 5003207 | 50 | 33 | nan | nan | nan | Pantanal | 74.1 |
| 82a5ec1e-6d4a-3e68-8880-e645edf4d583 | -19.0789 | -56.0516 | 2025-02-18 00:30:00 | GOES-16 | CORUMBÁ | MATO GROSSO DO SUL | Brasil | 5003207 | 50 | 33 | nan | nan | nan | Pantanal | 56.0 |
| bd1aac6c-7182-3716-8dd4-0e5a9b3d5553 | -19.1157 | -56.2142 | 2025-02-18 00:30:00 | GOES-16 | CORUMBÁ | MATO GROSSO DO SUL | Brasil | 5003207 | 50 | 33 | nan | nan | nan | Pantanal | 67.6 |
| fa388362-b74d-38da-a6ab-d18fdc964813 | -10.61085 | -45.11589 | 2025-02-18 00:30:00 | TERRA_M-M | CORRENTE | PIAUÍ | Brasil | 2202901 | 22 | 33 | nan | nan | nan | Cerrado | 81.5 |
| f46f3ab6-1367-3865-bb58-c50176042402 | -11.25126 | -49.00203 | 2025-02-18 00:30:00 | TERRA_M-M | ALIANÇA DO TOCANTINS | TOCANTINS | Brasil | 1700350 | 17 | 33 | nan | nan | nan | Cerrado | 28.9 |
| 3517c464-4979-3b32-8571-b5d15a142c84 | -8.12906 | -43.14188 | 2025-02-18 00:30:00 | TERRA_M-M | CANTO DO BURITI | PIAUÍ | Brasil | 2202307 | 22 | 33 | nan | nan | nan | Caatinga | 10.6 |
| c15e144d-7e0b-3532-bbe4-085514385953 | -11.25338 | -49.02005 | 2025-02-18 00:30:00 | TERRA_M-M | ALIANÇA DO TOCANTINS | TOCANTINS | Brasil | 1700350 | 17 | 33 | nan | nan | nan | Cerrado | 14.3 |
| 013de0b0-2065-3650-b885-e633f1d1aed0 | -11.24718 | -49.00814 | 2025-02-18 00:30:00 | TERRA_M-M | ALIANÇA DO TOCANTINS | TOCANTINS | Brasil | 1700350 | 17 | 33 | nan | nan | nan | Cerrado | 26.5 |
| 07453937-2418-3a62-a11f-06bf720c6908 | -11.25937 | -49.00663 | 2025-02-18 00:30:00 | TERRA_M-M | ALIANÇA DO TOCANTINS | TOCANTINS | Brasil | 1700350 | 17 | 33 | nan | nan | nan | Cerrado | 12.8 |
| b7da5bf2-c1d0-3943-b54d-9a94cf5bc69c | -10.76489 | -44.34333 | 2025-02-18 00:30:00 | TERRA_M-M | SANTA RITA DE CÁSSIA | BAHIA | Brasil | 2928406 | 29 | 33 | nan | nan | nan | Cerrado | 6.4 |
| fcd10bf7-1d29-3fe1-988d-e67969a0ca42 | -10.60956 | -45.10617 | 2025-02-18 00:30:00 | TERRA_M-M | CORRENTE | PIAUÍ | Brasil | 2202901 | 22 | 33 | nan | nan | nan | Cerrado | 100.5 |
| e232d957-6101-39f1-bf70-05d1a8af9abb | -6.69486 | -42.13366 | 2025-02-18 00:32:00 | TERRA_M-M | OEIRAS | PIAUÍ | Brasil | 2207009 | 22 | 33 | nan | nan | nan | Caatinga | 6.7 |
| 40a92bba-96ac-3486-8283-3532ed0a0bab | -19.1353 | -56.2324 | 2025-02-18 00:40:00 | GOES-16 | CORUMBÁ | MATO GROSSO DO SUL | Brasil | 5003207 | 50 | 33 | nan | nan | nan | Pantanal | 59.6 |
| e2319c54-6503-3926-9879-3f41baa0b4ba | -19.0585 | -56.0755 | 2025-02-18 00:40:00 | GOES-16 | CORUMBÁ | MATO GROSSO DO SUL | Brasil | 5003207 | 50 | 33 | nan | nan | nan | Pantanal | 47.1 |
| dd1f7b52-9240-3ae7-bcc7-1477a7c6b236 | -19.0789 | -56.0516 | 2025-02-18 00:40:00 | GOES-16 | CORUMBÁ | MATO GROSSO DO SUL | Brasil | 5003207 | 50 | 33 | nan | nan | nan | Pantanal | 53.5 |
| 530750dd-e760-3de0-bd80-265ce7f5d20b | -19.1153 | -56.2352 | 2025-02-18 00:40:00 | GOES-16 | CORUMBÁ | MATO GROSSO DO SUL | Brasil | 5003207 | 50 | 33 | nan | nan | nan | Pantanal | 84.1 |
| a04794da-383a-3a15-9202-b1afd77ac600 | -19.1157 | -56.2142 | 2025-02-18 00:40:00 | GOES-16 | CORUMBÁ | MATO GROSSO DO SUL | Brasil | 5003207 | 50 | 33 | nan | nan | nan | Pantanal | 81.2 |
| e7806322-2482-3b06-b162-b3f134ce5def | -10.6191 | -45.1132 | 2025-02-18 00:40:00 | GOES-16 | CORRENTE | PIAUÍ | Brasil | 2202901 | 22 | 33 | nan | nan | nan | Cerrado | 101.5 |
| 261074fd-43fb-3039-b926-e065e97ade81 | -21.3814 | -48.5616 | 2025-02-18 00:40:00 | GOES-16 | TAQUARITINGA | SÃO PAULO | Brasil | 3553708 | 35 | 33 | nan | nan | nan | Mata Atlântica | 74.6 |
| 2c41de19-bab9-3cea-b65a-8b4a5c870c4c | -10.6 | -45.1158 | 2025-02-18 00:40:00 | GOES-16 | CORRENTE | PIAUÍ | Brasil | 2202901 | 22 | 33 | nan | nan | nan | Cerrado | 65.6 |
| 216a4f78-2f5f-3fcc-a061-4dcd92a3a462 | -19.0589 | -56.0545 | 2025-02-18 00:40:00 | GOES-16 | CORUMBÁ | MATO GROSSO DO SUL | Brasil | 5003207 | 50 | 33 | nan | nan | nan | Pantanal | 47.6 |
| 5cf7ad37-ac5a-37a6-a2b7-c11f56b9d2ac | -19.1357 | -56.2114 | 2025-02-18 00:40:00 | GOES-16 | CORUMBÁ | MATO GROSSO DO SUL | Brasil | 5003207 | 50 | 33 | nan | nan | nan | Pantanal | 52.8 |
| 6ed7a23f-ca80-3fa1-86ec-0713495e98ca | -10.6195 | -45.0902 | 2025-02-18 00:40:00 | GOES-16 | CORRENTE | PIAUÍ | Brasil | 2202901 | 22 | 33 | nan | nan | nan | Cerrado | 66.9 |
| fb5c83a1-487c-3439-ac2c-ce52d4ecde5c | -19.0785 | -56.0727 | 2025-02-18 00:40:00 | GOES-16 | CORUMBÁ | MATO GROSSO DO SUL | Brasil | 5003207 | 50 | 33 | nan | nan | nan | Pantanal | 53.5 |
| 31ce5982-67f1-35f2-be9f-08f96e5b27c4 | -10.6032 | -45.0994 | 2025-02-18 00:48:00 | METOP-B | CORRENTE | PIAUÍ | Brasil | 2202901 | 22 | 33 | nan | nan | nan | Cerrado | nan |
| 10afccd4-2d31-398b-8d6b-cf2c032bb4d6 | -21.526699 | -47.131401 | 2025-02-18 00:48:00 | METOP-B | TAMBAÚ | SÃO PAULO | Brasil | 3553302 | 35 | 33 | nan | nan | nan | Cerrado | nan |
| 52376f51-ea15-3a12-87e9-f9d4597de513 | -19.501801 | -55.319599 | 2025-02-18 00:48:00 | METOP-B | AQUIDAUANA | MATO GROSSO DO SUL | Brasil | 5001102 | 50 | 33 | nan | nan | nan | Pantanal | nan |
| 397a49a3-41ff-3e24-a1a4-efd992516417 | -21.3813 | -48.5495 | 2025-02-18 00:48:00 | METOP-B | TAQUARITINGA | SÃO PAULO | Brasil | 3553708 | 35 | 33 | nan | nan | nan | Mata Atlântica | nan |
| 7fab5d32-aa41-379c-888c-8275decccfb1 | -1.5676 | -54.012901 | 2025-02-18 00:48:00 | METOP-B | MONTE ALEGRE | PARÁ | Brasil | 1504802 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| aba1fd7b-61a7-31c8-a162-cae7ba0e3ad1 | -21.3633 | -48.516998 | 2025-02-18 00:48:00 | METOP-B | TAQUARITINGA | SÃO PAULO | Brasil | 3553708 | 35 | 33 | nan | nan | nan | Cerrado | nan |
| 4d470c73-e0d0-37cb-b926-39c255cf5097 | -21.282 | -54.003601 | 2025-02-18 00:48:00 | METOP-B | CAMPO GRANDE | MATO GROSSO DO SUL | Brasil | 5002704 | 50 | 33 | nan | nan | nan | Cerrado | nan |
| bc93f398-1fba-365a-9829-c556ade9108c | -20.917801 | -56.513599 | 2025-02-18 00:48:00 | METOP-B | BONITO | MATO GROSSO DO SUL | Brasil | 5002209 | 50 | 33 | nan | nan | nan | Cerrado | nan |
| f721b07c-25e7-3d3f-88fe-93b6807e201b | -21.636299 | -55.957699 | 2025-02-18 00:48:00 | METOP-B | GUIA LOPES DA LAGUNA | MATO GROSSO DO SUL | Brasil | 5004106 | 50 | 33 | nan | nan | nan | Cerrado | nan |


[Clique aqui para ver as próximas entradas](README2.md)
