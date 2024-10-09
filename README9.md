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

## Dados Diários - Página 9

| ID | Latitude | Longitude | Data/Hora GMT | Satélite | Município | Estado | País | Município ID | Estado ID | País ID | Dias sem Chuva | Precipitação | Risco de Fogo | Bioma | FRP |
|----|----------|-----------|---------------|----------|-----------|--------|------|--------------|-----------|---------|----------------|--------------|----------------|-------|-----|
| 122a43c5-42a8-334b-b603-f8ed8fec3e4d | -21.025 | -47.571899 | 2024-10-09 00:37:30 | METOP-C | BRODOWSKI | SÃO PAULO | Brasil | 3507803 | 35 | 33 | nan | nan | nan | Cerrado | nan |
| 34c29148-dc76-3b16-a4a3-91c2f9eb4191 | -21.026899 | -47.581799 | 2024-10-09 00:37:30 | METOP-C | BRODOWSKI | SÃO PAULO | Brasil | 3507803 | 35 | 33 | nan | nan | nan | Cerrado | nan |
| f3617bc9-6e8a-36b7-a382-1eb7d7dc80a1 | -19.844101 | -42.383301 | 2024-10-09 00:37:31 | METOP-C | CÓRREGO NOVO | MINAS GERAIS | Brasil | 3120003 | 31 | 33 | nan | nan | nan | Mata Atlântica | nan |
| ee8e191a-adfc-37de-8524-52dad66f36be | -19.8309 | -42.370899 | 2024-10-09 00:37:31 | METOP-C | CÓRREGO NOVO | MINAS GERAIS | Brasil | 3120003 | 31 | 33 | nan | nan | nan | Mata Atlântica | nan |
| 68820dd8-d68c-3ffe-900f-693e7b913a5c | -19.8326 | -42.3783 | 2024-10-09 00:37:31 | METOP-C | CÓRREGO NOVO | MINAS GERAIS | Brasil | 3120003 | 31 | 33 | nan | nan | nan | Mata Atlântica | nan |
| 3afb00a2-696a-34aa-8960-5fb179251381 | -19.834299 | -42.385799 | 2024-10-09 00:37:31 | METOP-C | CÓRREGO NOVO | MINAS GERAIS | Brasil | 3120003 | 31 | 33 | nan | nan | nan | Mata Atlântica | nan |
| cc97687a-a02d-35e4-bfcb-d247ed5cf5d7 | -19.8211 | -42.373299 | 2024-10-09 00:37:31 | METOP-C | CÓRREGO NOVO | MINAS GERAIS | Brasil | 3120003 | 31 | 33 | nan | nan | nan | Mata Atlântica | nan |
| 0a8429e5-288d-3831-9497-98c1afc7307f | -19.8228 | -42.380699 | 2024-10-09 00:37:31 | METOP-C | CÓRREGO NOVO | MINAS GERAIS | Brasil | 3120003 | 31 | 33 | nan | nan | nan | Mata Atlântica | nan |
| 07d6047b-e10a-30fb-b6bb-c0dd97cb953b | -19.824499 | -42.388199 | 2024-10-09 00:37:31 | METOP-C | CÓRREGO NOVO | MINAS GERAIS | Brasil | 3120003 | 31 | 33 | nan | nan | nan | Mata Atlântica | nan |
| 88f9544e-d830-3a62-b112-72b1d81e3323 | -20.2318 | -44.2178 | 2024-10-09 00:37:31 | METOP-C | BONFIM | MINAS GERAIS | Brasil | 3108107 | 31 | 33 | nan | nan | nan | Mata Atlântica | nan |
| ec4a426d-a0c9-32db-b2b3-f7be805f7eb4 | -19.805 | -42.3932 | 2024-10-09 00:37:32 | METOP-C | CÓRREGO NOVO | MINAS GERAIS | Brasil | 3120003 | 31 | 33 | nan | nan | nan | Mata Atlântica | nan |
| 31f8c7db-bb94-39d2-b485-400f67f2718e | -19.8067 | -42.4006 | 2024-10-09 00:37:32 | METOP-C | CÓRREGO NOVO | MINAS GERAIS | Brasil | 3120003 | 31 | 33 | nan | nan | nan | Mata Atlântica | nan |
| 37b09241-b70d-30e0-b237-3bb85e566899 | -19.7701 | -42.331001 | 2024-10-09 00:37:32 | METOP-C | BOM JESUS DO GALHO | MINAS GERAIS | Brasil | 3107802 | 31 | 33 | nan | nan | nan | Mata Atlântica | nan |
| e05b0cfd-77cd-3364-9f40-bbe868e8ddd5 | -20.797501 | -47.192699 | 2024-10-09 00:37:32 | METOP-C | SÃO TOMÁS DE AQUINO | MINAS GERAIS | Brasil | 3165107 | 31 | 33 | nan | nan | nan | Cerrado | nan |
| 2853f8c3-f344-32dc-ba11-feebec9f0f2a | -20.799299 | -47.202 | 2024-10-09 00:37:32 | METOP-C | SÃO TOMÁS DE AQUINO | MINAS GERAIS | Brasil | 3165107 | 31 | 33 | nan | nan | nan | Cerrado | nan |
| a7d3173f-d123-38bf-a48e-609cd06ebc2b | -20.801201 | -47.2113 | 2024-10-09 00:37:32 | METOP-C | SÃO TOMÁS DE AQUINO | MINAS GERAIS | Brasil | 3165107 | 31 | 33 | nan | nan | nan | Cerrado | nan |
| 22a55b5f-8b8c-38d3-8cbc-a49dbf8b3281 | -20.7896 | -47.204102 | 2024-10-09 00:37:32 | METOP-C | SÃO TOMÁS DE AQUINO | MINAS GERAIS | Brasil | 3165107 | 31 | 33 | nan | nan | nan | Cerrado | nan |
| 78488eef-e74d-3747-94aa-e3823cae4da9 | -20.791401 | -47.213501 | 2024-10-09 00:37:32 | METOP-C | PATROCÍNIO PAULISTA | SÃO PAULO | Brasil | 3536307 | 35 | 33 | nan | nan | nan | Cerrado | nan |
| d0dadc72-d9b2-3d33-ba2d-c906ee96d700 | -20.793301 | -47.222801 | 2024-10-09 00:37:32 | METOP-C | PATROCÍNIO PAULISTA | SÃO PAULO | Brasil | 3536307 | 35 | 33 | nan | nan | nan | Cerrado | nan |
| 48ca209a-6b63-387e-8812-81c6595b4700 | -20.795099 | -47.232201 | 2024-10-09 00:37:32 | METOP-C | PATROCÍNIO PAULISTA | SÃO PAULO | Brasil | 3536307 | 35 | 33 | nan | nan | nan | Cerrado | nan |
| 6984e8ba-ee4a-32d8-beb4-524f5ffe1fe9 | -20.157801 | -44.3983 | 2024-10-09 00:37:33 | METOP-C | ITATIAIUÇU | MINAS GERAIS | Brasil | 3133709 | 31 | 33 | nan | nan | nan | Mata Atlântica | nan |
| da4cf206-270e-3af4-b351-c4516d293540 | -20.159401 | -44.405701 | 2024-10-09 00:37:33 | METOP-C | ITATIAIUÇU | MINAS GERAIS | Brasil | 3133709 | 31 | 33 | nan | nan | nan | Mata Atlântica | nan |
| 72e1e15f-19da-3ce5-ab67-484c7840551c | -20.106501 | -44.209202 | 2024-10-09 00:37:33 | METOP-C | BRUMADINHO | MINAS GERAIS | Brasil | 3109006 | 31 | 33 | nan | nan | nan | Mata Atlântica | nan |
| 8b79f22a-da29-349e-a4b2-388efaf2d102 | -20.108101 | -44.216499 | 2024-10-09 00:37:33 | METOP-C | BRUMADINHO | MINAS GERAIS | Brasil | 3109006 | 31 | 33 | nan | nan | nan | Mata Atlântica | nan |
| 600ba77f-86a7-3310-96e4-e6f76faa09ad | -20.778 | -47.196899 | 2024-10-09 00:37:33 | METOP-C | SÃO TOMÁS DE AQUINO | MINAS GERAIS | Brasil | 3165107 | 31 | 33 | nan | nan | nan | Cerrado | nan |
| 75046a41-370b-373e-a6c0-0ff8d53eabc7 | -20.7798 | -47.2062 | 2024-10-09 00:37:33 | METOP-C | SÃO TOMÁS DE AQUINO | MINAS GERAIS | Brasil | 3165107 | 31 | 33 | nan | nan | nan | Cerrado | nan |
| 09460358-1779-36c5-a0df-65bc8818cabf | -20.7817 | -47.215599 | 2024-10-09 00:37:33 | METOP-C | PATROCÍNIO PAULISTA | SÃO PAULO | Brasil | 3536307 | 35 | 33 | nan | nan | nan | Cerrado | nan |
| 4ea296f1-2b29-3345-a3d2-6b325de47113 | -20.783501 | -47.224899 | 2024-10-09 00:37:33 | METOP-C | PATROCÍNIO PAULISTA | SÃO PAULO | Brasil | 3536307 | 35 | 33 | nan | nan | nan | Cerrado | nan |
| 132da77d-ba90-31e1-bb2e-c7a6aafeec5f | -20.7854 | -47.234299 | 2024-10-09 00:37:33 | METOP-C | PATROCÍNIO PAULISTA | SÃO PAULO | Brasil | 3536307 | 35 | 33 | nan | nan | nan | Cerrado | nan |
| 61c417e2-b779-371c-9c1e-48f4eb375ef1 | -20.787201 | -47.243599 | 2024-10-09 00:37:33 | METOP-C | PATROCÍNIO PAULISTA | SÃO PAULO | Brasil | 3536307 | 35 | 33 | nan | nan | nan | Cerrado | nan |
| 1bbb4b79-10c1-3024-a79d-4236bd37d853 | -20.789101 | -47.252998 | 2024-10-09 00:37:33 | METOP-C | PATROCÍNIO PAULISTA | SÃO PAULO | Brasil | 3536307 | 35 | 33 | nan | nan | nan | Cerrado | nan |
| e0064bd2-cf4b-3905-92bd-a27d360f6e53 | -20.77 | -47.208401 | 2024-10-09 00:37:33 | METOP-C | PATROCÍNIO PAULISTA | SÃO PAULO | Brasil | 3536307 | 35 | 33 | nan | nan | nan | Cerrado | nan |
| eac80e42-fe65-345a-9e8a-d42d412df78b | -20.7756 | -47.236401 | 2024-10-09 00:37:33 | METOP-C | PATROCÍNIO PAULISTA | SÃO PAULO | Brasil | 3536307 | 35 | 33 | nan | nan | nan | Cerrado | nan |
| 6d54c4f4-22e6-3f8e-b77c-556cb0330bae | -20.777399 | -47.245701 | 2024-10-09 00:37:33 | METOP-C | PATROCÍNIO PAULISTA | SÃO PAULO | Brasil | 3536307 | 35 | 33 | nan | nan | nan | Cerrado | nan |
| f9d33823-4885-3115-825a-0f0d22c8d9d8 | -20.779301 | -47.2551 | 2024-10-09 00:37:33 | METOP-C | PATROCÍNIO PAULISTA | SÃO PAULO | Brasil | 3536307 | 35 | 33 | nan | nan | nan | Cerrado | nan |
| 3888ff34-a328-39cb-b2db-d24a47b3d5cf | -20.781099 | -47.2645 | 2024-10-09 00:37:33 | METOP-C | PATROCÍNIO PAULISTA | SÃO PAULO | Brasil | 3536307 | 35 | 33 | nan | nan | nan | Cerrado | nan |
| 726911b7-4cc7-3014-a43b-c9f101ad5933 | -20.767599 | -47.247898 | 2024-10-09 00:37:33 | METOP-C | PATROCÍNIO PAULISTA | SÃO PAULO | Brasil | 3536307 | 35 | 33 | nan | nan | nan | Cerrado | nan |
| cf898e96-0683-3010-af4e-920d57e1ea1d | -20.769501 | -47.257301 | 2024-10-09 00:37:33 | METOP-C | PATROCÍNIO PAULISTA | SÃO PAULO | Brasil | 3536307 | 35 | 33 | nan | nan | nan | Cerrado | nan |
| fe9aef71-6b6e-3bf4-8c1b-05e2382dfdaa | -19.3374 | -40.876099 | 2024-10-09 00:37:34 | METOP-C | BAIXO GUANDU | ESPÍRITO SANTO | Brasil | 3200805 | 32 | 33 | nan | nan | nan | Mata Atlântica | nan |
| 5caf7c27-6299-3a33-b265-ebf7e945cddc | -19.3277 | -40.878601 | 2024-10-09 00:37:34 | METOP-C | PANCAS | ESPÍRITO SANTO | Brasil | 3204005 | 32 | 33 | nan | nan | nan | Mata Atlântica | nan |
| 69824e20-badf-37d1-bd97-b51ef311a0a2 | -19.7703 | -42.8311 | 2024-10-09 00:37:34 | METOP-C | SÃO DOMINGOS DO PRATA | MINAS GERAIS | Brasil | 3161007 | 31 | 33 | nan | nan | nan | Mata Atlântica | nan |
| b4e69533-6a96-3cb2-9e6d-1f2c3df6455d | -19.7719 | -42.838501 | 2024-10-09 00:37:34 | METOP-C | SÃO DOMINGOS DO PRATA | MINAS GERAIS | Brasil | 3161007 | 31 | 33 | nan | nan | nan | Mata Atlântica | nan |
| 0fb9b22f-62b7-360a-ab9d-a157f1cf2409 | -20.680799 | -47.169701 | 2024-10-09 00:37:34 | METOP-C | ITIRAPUÃ | SÃO PAULO | Brasil | 3523701 | 35 | 33 | nan | nan | nan | Cerrado | nan |
| f9f73e1a-7a0c-3c2a-a146-c0e5de95a101 | -20.6826 | -47.179001 | 2024-10-09 00:37:34 | METOP-C | ITIRAPUÃ | SÃO PAULO | Brasil | 3523701 | 35 | 33 | nan | nan | nan | Cerrado | nan |
| 0bff3e32-e182-30d2-aa61-ff25c21c656c | -20.671 | -47.171902 | 2024-10-09 00:37:34 | METOP-C | ITIRAPUÃ | SÃO PAULO | Brasil | 3523701 | 35 | 33 | nan | nan | nan | Cerrado | nan |
| a10eb466-a34f-3a6a-8d7b-45dfa74ef248 | -19.8316 | -43.799 | 2024-10-09 00:37:36 | METOP-C | SANTA LUZIA | MINAS GERAIS | Brasil | 3157807 | 31 | 33 | nan | nan | nan | Mata Atlântica | nan |
| ea851ee4-1969-3994-b7c9-1cf205d30e44 | -19.8284 | -43.784401 | 2024-10-09 00:37:36 | METOP-C | SANTA LUZIA | MINAS GERAIS | Brasil | 3157807 | 31 | 33 | nan | nan | nan | Cerrado | nan |
| 62158d16-785a-399f-950d-917a9cc2e0ed | -19.83 | -43.791698 | 2024-10-09 00:37:36 | METOP-C | SANTA LUZIA | MINAS GERAIS | Brasil | 3157807 | 31 | 33 | nan | nan | nan | Cerrado | nan |
| 9cd46744-8fc1-39e0-bcb2-6483ab882ec1 | -19.117201 | -40.951199 | 2024-10-09 00:37:37 | METOP-C | PANCAS | ESPÍRITO SANTO | Brasil | 3204005 | 32 | 33 | nan | nan | nan | Mata Atlântica | nan |
| 4949b307-61f1-3547-8fd9-eed4f27cba57 | -19.1192 | -40.9594 | 2024-10-09 00:37:37 | METOP-C | PANCAS | ESPÍRITO SANTO | Brasil | 3204005 | 32 | 33 | nan | nan | nan | Mata Atlântica | nan |
| 9352076a-5283-3b8c-80bd-0d0ddcd1854e | -19.8202 | -43.794102 | 2024-10-09 00:37:37 | METOP-C | SANTA LUZIA | MINAS GERAIS | Brasil | 3157807 | 31 | 33 | nan | nan | nan | Cerrado | nan |
| 455973e0-91ff-3f11-8608-580e3f6f9983 | -19.8218 | -43.801399 | 2024-10-09 00:37:37 | METOP-C | SANTA LUZIA | MINAS GERAIS | Brasil | 3157807 | 31 | 33 | nan | nan | nan | Cerrado | nan |
| 7b187228-11b8-3bac-b672-828f5a81fbd8 | -20.775 | -48.544498 | 2024-10-09 00:37:37 | METOP-C | COLINA | SÃO PAULO | Brasil | 3512001 | 35 | 33 | nan | nan | nan | Cerrado | nan |
| a3429599-dd3e-34ee-b046-d4196b8c83ba | -20.7771 | -48.5555 | 2024-10-09 00:37:37 | METOP-C | COLINA | SÃO PAULO | Brasil | 3512001 | 35 | 33 | nan | nan | nan | Cerrado | nan |
| 894e1491-ae91-3606-85fb-2b09d483c8e5 | -20.7673 | -48.557598 | 2024-10-09 00:37:37 | METOP-C | COLINA | SÃO PAULO | Brasil | 3512001 | 35 | 33 | nan | nan | nan | Cerrado | nan |
| 46aaffba-8510-3441-90ae-0dc0a24b7c88 | -20.7694 | -48.5686 | 2024-10-09 00:37:37 | METOP-C | COLINA | SÃO PAULO | Brasil | 3512001 | 35 | 33 | nan | nan | nan | Cerrado | nan |
| 31f71782-5307-31d0-87ef-0dc29bca146e | -20.747101 | -48.504601 | 2024-10-09 00:37:37 | METOP-C | COLINA | SÃO PAULO | Brasil | 3512001 | 35 | 33 | nan | nan | nan | Cerrado | nan |
| 6ffef333-698a-33eb-b940-fefe05b00ba2 | -20.749201 | -48.515598 | 2024-10-09 00:37:37 | METOP-C | COLINA | SÃO PAULO | Brasil | 3512001 | 35 | 33 | nan | nan | nan | Cerrado | nan |
| ca688904-c152-3a19-8099-9f8af4aa6d68 | -20.751301 | -48.5266 | 2024-10-09 00:37:37 | METOP-C | COLINA | SÃO PAULO | Brasil | 3512001 | 35 | 33 | nan | nan | nan | Cerrado | nan |
| 43911819-5326-3cda-8411-0dc69e72c9c2 | -20.755501 | -48.548599 | 2024-10-09 00:37:37 | METOP-C | COLINA | SÃO PAULO | Brasil | 3512001 | 35 | 33 | nan | nan | nan | Cerrado | nan |
| 99bdccf9-33cf-3a18-a4f5-3e094a853de8 | -20.757601 | -48.559601 | 2024-10-09 00:37:37 | METOP-C | COLINA | SÃO PAULO | Brasil | 3512001 | 35 | 33 | nan | nan | nan | Cerrado | nan |
| a3279458-92e8-3fd7-a246-b574a6aed9c6 | -20.759701 | -48.570702 | 2024-10-09 00:37:37 | METOP-C | COLINA | SÃO PAULO | Brasil | 3512001 | 35 | 33 | nan | nan | nan | Cerrado | nan |
| f38b301a-0d07-3c0c-9682-fa6c339f46f9 | -20.737301 | -48.506699 | 2024-10-09 00:37:37 | METOP-C | COLINA | SÃO PAULO | Brasil | 3512001 | 35 | 33 | nan | nan | nan | Cerrado | nan |
| 82500a73-3e34-33c8-9da1-823a11962d5c | -20.739401 | -48.517601 | 2024-10-09 00:37:37 | METOP-C | COLINA | SÃO PAULO | Brasil | 3512001 | 35 | 33 | nan | nan | nan | Cerrado | nan |
| e164a7ad-8808-3ea0-8fdd-480b400b345a | -20.3522 | -46.349499 | 2024-10-09 00:37:37 | METOP-C | VARGEM BONITA | MINAS GERAIS | Brasil | 3170602 | 31 | 33 | nan | nan | nan | Cerrado | nan |
| b4f1964c-e67b-3357-8021-b24ae0d17f7f | -20.353901 | -46.357899 | 2024-10-09 00:37:37 | METOP-C | VARGEM BONITA | MINAS GERAIS | Brasil | 3170602 | 31 | 33 | nan | nan | nan | Cerrado | nan |
| 8cffdca7-1e70-3721-864f-17b40ef1bd2a | -20.476 | -47.1665 | 2024-10-09 00:37:37 | METOP-C | IBIRACI | MINAS GERAIS | Brasil | 3129707 | 31 | 33 | nan | nan | nan | Cerrado | nan |
| a704156d-5d40-3f65-b862-62dabaf90009 | -19.105499 | -40.945499 | 2024-10-09 00:37:38 | METOP-C | PANCAS | ESPÍRITO SANTO | Brasil | 3204005 | 32 | 33 | nan | nan | nan | Mata Atlântica | nan |
| b407d6b4-c32f-32d7-910f-96b6b59fc503 | -19.1075 | -40.953701 | 2024-10-09 00:37:38 | METOP-C | PANCAS | ESPÍRITO SANTO | Brasil | 3204005 | 32 | 33 | nan | nan | nan | Mata Atlântica | nan |
| 4373afc9-a64c-3d05-9f9d-3bdcd8716755 | -19.109501 | -40.962002 | 2024-10-09 00:37:38 | METOP-C | PANCAS | ESPÍRITO SANTO | Brasil | 3204005 | 32 | 33 | nan | nan | nan | Mata Atlântica | nan |
| 2d341e7a-5a35-3d31-ab45-72463a0809e1 | -19.0977 | -40.9562 | 2024-10-09 00:37:38 | METOP-C | ALTO RIO NOVO | ESPÍRITO SANTO | Brasil | 3200359 | 32 | 33 | nan | nan | nan | Mata Atlântica | nan |
| baa410a0-8520-3200-a829-0bfae8affad6 | -19.448799 | -42.506199 | 2024-10-09 00:37:38 | METOP-C | SANTANA DO PARAÍSO | MINAS GERAIS | Brasil | 3158953 | 31 | 33 | nan | nan | nan | Mata Atlântica | nan |
| 8beb43fa-9071-350c-bb88-ba520965807a | -19.4505 | -42.513699 | 2024-10-09 00:37:38 | METOP-C | SANTANA DO PARAÍSO | MINAS GERAIS | Brasil | 3158953 | 31 | 33 | nan | nan | nan | Mata Atlântica | nan |
| 0e0caa6f-ed77-32c1-9952-b804c3de9d34 | -20.4645 | -47.159401 | 2024-10-09 00:37:38 | METOP-C | IBIRACI | MINAS GERAIS | Brasil | 3129707 | 31 | 33 | nan | nan | nan | Cerrado | nan |
| 417a03c0-3e4a-355c-b0ff-7a76fcd3e743 | -20.466299 | -47.168598 | 2024-10-09 00:37:38 | METOP-C | IBIRACI | MINAS GERAIS | Brasil | 3129707 | 31 | 33 | nan | nan | nan | Cerrado | nan |
| 15c57956-75b7-389a-a0fe-1c93346dcb53 | -19.2782 | -42.844898 | 2024-10-09 00:37:42 | METOP-C | FERROS | MINAS GERAIS | Brasil | 3125903 | 31 | 33 | nan | nan | nan | Mata Atlântica | nan |
| d02150c6-c869-361a-a5d7-234aa0fbe938 | -19.2799 | -42.852299 | 2024-10-09 00:37:42 | METOP-C | FERROS | MINAS GERAIS | Brasil | 3125903 | 31 | 33 | nan | nan | nan | Mata Atlântica | nan |
| 4e897513-c284-3a9d-8f3d-618aaa7beee9 | -20.6122 | -49.350498 | 2024-10-09 00:37:42 | METOP-C | ONDA VERDE | SÃO PAULO | Brasil | 3534005 | 35 | 33 | nan | nan | nan | Cerrado | nan |
| 705796d6-514c-3571-93ed-b7635de79980 | -20.6003 | -49.340302 | 2024-10-09 00:37:42 | METOP-C | NOVA GRANADA | SÃO PAULO | Brasil | 3533007 | 35 | 33 | nan | nan | nan | Cerrado | nan |
| 707af934-0d85-32bb-9056-667a176f35a6 | -20.602501 | -49.352501 | 2024-10-09 00:37:42 | METOP-C | NOVA GRANADA | SÃO PAULO | Brasil | 3533007 | 35 | 33 | nan | nan | nan | Cerrado | nan |
| 0ce00fd9-d1bc-3619-8ad4-7c28bb43bffe | -20.5905 | -49.3423 | 2024-10-09 00:37:42 | METOP-C | NOVA GRANADA | SÃO PAULO | Brasil | 3533007 | 35 | 33 | nan | nan | nan | Cerrado | nan |
| 1952b117-51fe-3bcf-8dad-388100caf5e9 | -20.0485 | -46.365101 | 2024-10-09 00:37:42 | METOP-C | MEDEIROS | MINAS GERAIS | Brasil | 3141306 | 31 | 33 | nan | nan | nan | Cerrado | nan |
| 1e946f6a-e79f-35e1-9276-d1ef1cdfde47 | -20.0502 | -46.373402 | 2024-10-09 00:37:42 | METOP-C | MEDEIROS | MINAS GERAIS | Brasil | 3141306 | 31 | 33 | nan | nan | nan | Cerrado | nan |
| 95f59d1f-61db-38f3-802b-b1390d5bb9c7 | -20.051901 | -46.381802 | 2024-10-09 00:37:42 | METOP-C | SÃO ROQUE DE MINAS | MINAS GERAIS | Brasil | 3164308 | 31 | 33 | nan | nan | nan | Cerrado | nan |
| 166a1c67-624f-3225-ba1c-1e418a0d563d | -20.451799 | -48.821098 | 2024-10-09 00:37:43 | METOP-C | BARRETOS | SÃO PAULO | Brasil | 3505500 | 35 | 33 | nan | nan | nan | Mata Atlântica | nan |
| 04c93e1a-2032-3c53-9bf7-69dc429b59fb | -20.453899 | -48.832401 | 2024-10-09 00:37:43 | METOP-C | BARRETOS | SÃO PAULO | Brasil | 3505500 | 35 | 33 | nan | nan | nan | Mata Atlântica | nan |
| 035bde21-91af-3195-914a-a198f8f518c6 | -20.442101 | -48.823101 | 2024-10-09 00:37:43 | METOP-C | BARRETOS | SÃO PAULO | Brasil | 3505500 | 35 | 33 | nan | nan | nan | Mata Atlântica | nan |
| 580ba6b0-2263-3edf-ba0b-1cefc4e799f4 | -20.444201 | -48.8344 | 2024-10-09 00:37:43 | METOP-C | BARRETOS | SÃO PAULO | Brasil | 3505500 | 35 | 33 | nan | nan | nan | Mata Atlântica | nan |
| 5004425a-8bb2-3d9a-befb-0ca5b0743675 | -20.549101 | -49.338001 | 2024-10-09 00:37:43 | METOP-C | NOVA GRANADA | SÃO PAULO | Brasil | 3533007 | 35 | 33 | nan | nan | nan | Cerrado | nan |
| 9ddf734f-e111-30af-93f2-f058be9f7846 | -20.551399 | -49.350201 | 2024-10-09 00:37:43 | METOP-C | NOVA GRANADA | SÃO PAULO | Brasil | 3533007 | 35 | 33 | nan | nan | nan | Cerrado | nan |
| ea2b96c9-7983-375b-8bce-a9fae5c5a48b | -20.5394 | -49.34 | 2024-10-09 00:37:43 | METOP-C | NOVA GRANADA | SÃO PAULO | Brasil | 3533007 | 35 | 33 | nan | nan | nan | Cerrado | nan |
| 05ea7070-834b-3477-9985-53c6394e0133 | -19.791599 | -45.620602 | 2024-10-09 00:37:43 | METOP-C | LUZ | MINAS GERAIS | Brasil | 3138807 | 31 | 33 | nan | nan | nan | Cerrado | nan |
| f0326542-ed51-3b22-ba72-848f08fdd8e2 | -19.143801 | -42.7075 | 2024-10-09 00:37:44 | METOP-C | JOANÉSIA | MINAS GERAIS | Brasil | 3136108 | 31 | 33 | nan | nan | nan | Mata Atlântica | nan |
| a9364f8c-22ea-3ffa-8dcb-58d42bbf3e67 | -19.134001 | -42.7099 | 2024-10-09 00:37:44 | METOP-C | JOANÉSIA | MINAS GERAIS | Brasil | 3136108 | 31 | 33 | nan | nan | nan | Mata Atlântica | nan |
| 97c5bf9a-57d8-3ff2-8582-4cf106f80628 | -19.1243 | -42.712299 | 2024-10-09 00:37:44 | METOP-C | BRAÚNAS | MINAS GERAIS | Brasil | 3108800 | 31 | 33 | nan | nan | nan | Mata Atlântica | nan |
| 1998ea43-8ad9-34bc-9b4b-fb43d7336b2e | -19.1259 | -42.7197 | 2024-10-09 00:37:44 | METOP-C | BRAÚNAS | MINAS GERAIS | Brasil | 3108800 | 31 | 33 | nan | nan | nan | Mata Atlântica | nan |
| 93d9c40b-caad-33eb-8c9f-20fce853cca8 | -20.369699 | -48.7099 | 2024-10-09 00:37:44 | METOP-C | BARRETOS | SÃO PAULO | Brasil | 3505500 | 35 | 33 | nan | nan | nan | Cerrado | nan |
| 33fa7a85-7d01-3379-8a22-fb25bcd7aaaf | -20.371799 | -48.721001 | 2024-10-09 00:37:44 | METOP-C | BARRETOS | SÃO PAULO | Brasil | 3505500 | 35 | 33 | nan | nan | nan | Cerrado | nan |
| 96af7e42-e20a-3d54-b5d7-284cd8bd1cfd | -20.357901 | -48.700901 | 2024-10-09 00:37:44 | METOP-C | COLÔMBIA | SÃO PAULO | Brasil | 3512100 | 35 | 33 | nan | nan | nan | Cerrado | nan |
| e15469d9-fe91-3a02-b6fc-ee5331f57295 | -20.360001 | -48.712002 | 2024-10-09 00:37:44 | METOP-C | BARRETOS | SÃO PAULO | Brasil | 3505500 | 35 | 33 | nan | nan | nan | Cerrado | nan |


[Clique aqui para ver as próximas entradas](README10.md)
