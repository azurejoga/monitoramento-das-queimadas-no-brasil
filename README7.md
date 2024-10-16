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

## Dados Diários - Página 7

| ID | Latitude | Longitude | Data/Hora GMT | Satélite | Município | Estado | País | Município ID | Estado ID | País ID | Dias sem Chuva | Precipitação | Risco de Fogo | Bioma | FRP |
|----|----------|-----------|---------------|----------|-----------|--------|------|--------------|-----------|---------|----------------|--------------|----------------|-------|-----|
| 2abc8c0a-3273-3bef-91bd-f69fd45ca262 | -6.8997 | -47.320801 | 2024-10-16 00:41:44 | METOP-B | ESTREITO | MARANHÃO | Brasil | 2104057 | 21 | 33 | nan | nan | nan | Cerrado | nan |
| 072289ee-f87d-30c6-8d38-e32429798c7f | -6.8862 | -47.307098 | 2024-10-16 00:41:44 | METOP-B | ESTREITO | MARANHÃO | Brasil | 2104057 | 21 | 33 | nan | nan | nan | Cerrado | nan |
| adda18c5-8eef-32b1-85b8-fa104188ccff | -6.8881 | -47.315102 | 2024-10-16 00:41:44 | METOP-B | ESTREITO | MARANHÃO | Brasil | 2104057 | 21 | 33 | nan | nan | nan | Cerrado | nan |
| 684562d5-4c3a-3ae4-a79b-22999a478d06 | -6.8899 | -47.323002 | 2024-10-16 00:41:44 | METOP-B | ESTREITO | MARANHÃO | Brasil | 2104057 | 21 | 33 | nan | nan | nan | Cerrado | nan |
| 6373afb2-0269-3c1c-aeff-3cbc090b734b | -6.1788 | -44.5075 | 2024-10-16 00:41:45 | METOP-B | MIRADOR | MARANHÃO | Brasil | 2106706 | 21 | 33 | nan | nan | nan | Cerrado | nan |
| 6d9302ff-d4a6-3ee2-90c1-b9c921710b32 | -6.1816 | -44.519199 | 2024-10-16 00:41:45 | METOP-B | MIRADOR | MARANHÃO | Brasil | 2106706 | 21 | 33 | nan | nan | nan | Cerrado | nan |
| 851fe962-7539-39dd-9219-89fa50b10c6a | -6.1844 | -44.530899 | 2024-10-16 00:41:45 | METOP-B | MIRADOR | MARANHÃO | Brasil | 2106706 | 21 | 33 | nan | nan | nan | Cerrado | nan |
| 3af3fd44-f773-3717-ac95-140df995e152 | -6.1718 | -44.5215 | 2024-10-16 00:41:45 | METOP-B | MIRADOR | MARANHÃO | Brasil | 2106706 | 21 | 33 | nan | nan | nan | Cerrado | nan |
| 40ee8752-4484-31f6-acc8-e8039aeb5550 | -6.1215 | -44.917599 | 2024-10-16 00:41:47 | METOP-B | FERNANDO FALCÃO | MARANHÃO | Brasil | 2104081 | 21 | 33 | nan | nan | nan | Cerrado | nan |
| 79cedfe1-b74e-3eec-bd28-c6ed768c58c0 | -6.373 | -46.9165 | 2024-10-16 00:41:51 | METOP-B | SÃO JOÃO DO PARAÍSO | MARANHÃO | Brasil | 2111052 | 21 | 33 | nan | nan | nan | Cerrado | nan |
| 33d66b0d-b822-3695-86c5-a84b7f26ba82 | -5.4989 | -43.682499 | 2024-10-16 00:41:53 | METOP-B | PARNARAMA | MARANHÃO | Brasil | 2107803 | 21 | 33 | nan | nan | nan | Cerrado | nan |
| fd412472-e9d7-3589-b8e7-5d5be04a2200 | -5.5021 | -43.696098 | 2024-10-16 00:41:53 | METOP-B | PARNARAMA | MARANHÃO | Brasil | 2107803 | 21 | 33 | nan | nan | nan | Cerrado | nan |
| 54f79945-8bf4-340a-ac1f-26a388079a9d | -5.6869 | -44.473701 | 2024-10-16 00:41:53 | METOP-B | TUNTUM | MARANHÃO | Brasil | 2112308 | 21 | 33 | nan | nan | nan | Cerrado | nan |
| 4118b642-a160-395e-a98b-b9022bf6391f | -5.6897 | -44.485699 | 2024-10-16 00:41:53 | METOP-B | TUNTUM | MARANHÃO | Brasil | 2112308 | 21 | 33 | nan | nan | nan | Cerrado | nan |
| 48f6aedd-216f-391c-9161-592c33ea0c2d | -5.9835 | -45.7323 | 2024-10-16 00:41:53 | METOP-B | GRAJAÚ | MARANHÃO | Brasil | 2104800 | 21 | 33 | nan | nan | nan | Cerrado | nan |
| 4f5d0b55-ead3-3daf-8fc8-b8e0147e3ca2 | -5.2665 | -43.3979 | 2024-10-16 00:41:55 | METOP-B | MATÕES | MARANHÃO | Brasil | 2106607 | 21 | 33 | nan | nan | nan | Cerrado | nan |
| 7004cc65-32d1-3f07-817b-4a925fef7188 | -6.6663 | -49.4566 | 2024-10-16 00:41:55 | METOP-B | XINGUARA | PARÁ | Brasil | 1508407 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| 344fba29-ae65-32fe-a959-c34732f151bb | -5.5746 | -44.869202 | 2024-10-16 00:41:56 | METOP-B | TUNTUM | MARANHÃO | Brasil | 2112308 | 21 | 33 | nan | nan | nan | Cerrado | nan |
| b190c5f7-7018-3238-903a-7624b047a4dc | -5.5772 | -44.880501 | 2024-10-16 00:41:56 | METOP-B | TUNTUM | MARANHÃO | Brasil | 2112308 | 21 | 33 | nan | nan | nan | Cerrado | nan |
| e1ff21ae-a0ff-359a-939d-edd1dde229ca | -5.5987 | -45.190399 | 2024-10-16 00:41:57 | METOP-B | BARRA DO CORDA | MARANHÃO | Brasil | 2101608 | 21 | 33 | nan | nan | nan | Cerrado | nan |
| abac1651-9bfb-38a3-8ee9-ba60c3f728b2 | -5.6013 | -45.201199 | 2024-10-16 00:41:57 | METOP-B | BARRA DO CORDA | MARANHÃO | Brasil | 2101608 | 21 | 33 | nan | nan | nan | Cerrado | nan |
| 8c479f99-5b05-3a8f-98cb-afe0e6934f64 | -5.1507 | -43.9911 | 2024-10-16 00:41:59 | METOP-B | SÃO JOÃO DO SOTER | MARANHÃO | Brasil | 2111078 | 21 | 33 | nan | nan | nan | Cerrado | nan |
| 5ddc795b-a9a4-3ef9-ad96-80fcb1741f8a | -5.5095 | -45.380199 | 2024-10-16 00:41:59 | METOP-B | BARRA DO CORDA | MARANHÃO | Brasil | 2101608 | 21 | 33 | nan | nan | nan | Cerrado | nan |
| 26e1246d-df3b-345a-a618-29ea095cc477 | -5.512 | -45.390701 | 2024-10-16 00:41:59 | METOP-B | BARRA DO CORDA | MARANHÃO | Brasil | 2101608 | 21 | 33 | nan | nan | nan | Cerrado | nan |
| 38fabc47-44e4-3556-a6db-a12cf4e8ca70 | -5.1538 | -44.004299 | 2024-10-16 00:41:59 | METOP-B | GONÇALVES DIAS | MARANHÃO | Brasil | 2104404 | 21 | 33 | nan | nan | nan | Cerrado | nan |
| 1a8e4225-4209-31d9-abd5-c023834ed5a0 | -5.5094 | -46.882198 | 2024-10-16 00:42:05 | METOP-B | AMARANTE DO MARANHÃO | MARANHÃO | Brasil | 2100600 | 21 | 33 | nan | nan | nan | Cerrado | nan |
| 084dd8ea-a4b9-3c75-ba85-22bdba85d8a1 | -5.5114 | -46.8908 | 2024-10-16 00:42:05 | METOP-B | AMARANTE DO MARANHÃO | MARANHÃO | Brasil | 2100600 | 21 | 33 | nan | nan | nan | Cerrado | nan |
| 8aa559df-fa7c-3331-8afc-8d33c38965c1 | -5.5134 | -46.899399 | 2024-10-16 00:42:05 | METOP-B | AMARANTE DO MARANHÃO | MARANHÃO | Brasil | 2100600 | 21 | 33 | nan | nan | nan | Cerrado | nan |
| 30d2ce9e-7996-3b4a-b0e7-91bff93ed8d2 | -5.5154 | -46.9081 | 2024-10-16 00:42:05 | METOP-B | AMARANTE DO MARANHÃO | MARANHÃO | Brasil | 2100600 | 21 | 33 | nan | nan | nan | Cerrado | nan |
| 9d8f080f-5064-3f5e-817a-e9e75e3bb664 | -4.9668 | -44.605301 | 2024-10-16 00:42:05 | METOP-B | SÃO JOSÉ DOS BASÍLIOS | MARANHÃO | Brasil | 2111250 | 21 | 33 | nan | nan | nan | Cerrado | nan |
| 5681aed2-45ef-3594-a668-a6d44b576162 | -5.5017 | -46.893002 | 2024-10-16 00:42:05 | METOP-B | AMARANTE DO MARANHÃO | MARANHÃO | Brasil | 2100600 | 21 | 33 | nan | nan | nan | Cerrado | nan |
| 46d60795-01e6-3947-bac7-f60fbc7acb6f | -5.0884 | -45.825199 | 2024-10-16 00:42:07 | METOP-B | ARAME | MARANHÃO | Brasil | 2100956 | 21 | 33 | nan | nan | nan | Amazônia | nan |
| 7bc97cc2-50ca-3a3f-8082-2e0a0f86fda1 | -4.5227 | -43.4673 | 2024-10-16 00:42:08 | METOP-B | ALDEIAS ALTAS | MARANHÃO | Brasil | 2100303 | 21 | 33 | nan | nan | nan | Cerrado | nan |
| 9a770153-20b0-3909-b63d-a03541d1feae | -4.5262 | -43.4818 | 2024-10-16 00:42:08 | METOP-B | ALDEIAS ALTAS | MARANHÃO | Brasil | 2100303 | 21 | 33 | nan | nan | nan | Cerrado | nan |
| 7875f679-6604-3f24-a0bc-cd9ed06297bd | -4.5165 | -43.4841 | 2024-10-16 00:42:08 | METOP-B | ALDEIAS ALTAS | MARANHÃO | Brasil | 2100303 | 21 | 33 | nan | nan | nan | Cerrado | nan |
| d54943fc-edcd-3a87-9b49-0ad7467dda98 | -5.0436 | -46.074799 | 2024-10-16 00:42:09 | METOP-B | ARAME | MARANHÃO | Brasil | 2100956 | 21 | 33 | nan | nan | nan | Amazônia | nan |
| 19567233-515b-3f36-8103-6a2bc5792352 | -5.1074 | -46.837101 | 2024-10-16 00:42:11 | METOP-B | AMARANTE DO MARANHÃO | MARANHÃO | Brasil | 2100600 | 21 | 33 | nan | nan | nan | Amazônia | nan |
| d1d22647-67bf-3a0a-9ace-3dfcaa033e6d | -5.3919 | -48.3862 | 2024-10-16 00:42:12 | METOP-B | ARAGUATINS | TOCANTINS | Brasil | 1702208 | 17 | 33 | nan | nan | nan | Amazônia | nan |
| 2ea49de2-39a8-3d40-b015-d6aebcb3b017 | -5.2304 | -47.951599 | 2024-10-16 00:42:13 | METOP-B | VILA NOVA DOS MARTÍRIOS | MARANHÃO | Brasil | 2112852 | 21 | 33 | nan | nan | nan | Amazônia | nan |
| 293eeff4-498a-33fe-9bd5-4b69e5a67543 | -5.2188 | -47.945999 | 2024-10-16 00:42:13 | METOP-B | VILA NOVA DOS MARTÍRIOS | MARANHÃO | Brasil | 2112852 | 21 | 33 | nan | nan | nan | Amazônia | nan |
| 2e7dff85-2ef0-35a0-bb42-af43e3d0ee9e | -5.2206 | -47.9538 | 2024-10-16 00:42:13 | METOP-B | VILA NOVA DOS MARTÍRIOS | MARANHÃO | Brasil | 2112852 | 21 | 33 | nan | nan | nan | Amazônia | nan |
| b7ed0617-2243-3430-b6d7-6ed2d2ef4ac5 | -5.2224 | -47.961498 | 2024-10-16 00:42:13 | METOP-B | VILA NOVA DOS MARTÍRIOS | MARANHÃO | Brasil | 2112852 | 21 | 33 | nan | nan | nan | Amazônia | nan |
| 1d009794-f0f9-31c1-afa6-118621d64509 | -4.4404 | -44.816601 | 2024-10-16 00:42:14 | METOP-B | SÃO LUÍS GONZAGA DO MARANHÃO | MARANHÃO | Brasil | 2111409 | 21 | 33 | nan | nan | nan | Cerrado | nan |
| c180e4c7-a1cb-3b19-abb8-3bba5de1eb87 | -4.4432 | -44.828499 | 2024-10-16 00:42:14 | METOP-B | SÃO LUÍS GONZAGA DO MARANHÃO | MARANHÃO | Brasil | 2111409 | 21 | 33 | nan | nan | nan | Cerrado | nan |
| e6a0de13-f184-35ab-9d20-17c620cfd254 | -5.4001 | -49.191002 | 2024-10-16 00:42:15 | METOP-B | MARABÁ | PARÁ | Brasil | 1504208 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| 300520b4-1f15-33e4-80ad-b82bce632aa8 | -4.8202 | -46.9767 | 2024-10-16 00:42:16 | METOP-B | AÇAILÂNDIA | MARANHÃO | Brasil | 2100055 | 21 | 33 | nan | nan | nan | Amazônia | nan |
| 141a2d23-2c05-3f37-8c63-9e3141119af1 | -4.8222 | -46.985401 | 2024-10-16 00:42:16 | METOP-B | AÇAILÂNDIA | MARANHÃO | Brasil | 2100055 | 21 | 33 | nan | nan | nan | Amazônia | nan |
| 2be77b7c-aca7-34ef-8c7e-c685fa37239b | -3.5111 | -43.2257 | 2024-10-16 00:42:23 | METOP-B | ANAPURUS | MARANHÃO | Brasil | 2100808 | 21 | 33 | nan | nan | nan | Cerrado | nan |
| 270bbd23-11e6-3ba8-af86-0c2c3bbc2752 | -3.5148 | -43.241402 | 2024-10-16 00:42:23 | METOP-B | ANAPURUS | MARANHÃO | Brasil | 2100808 | 21 | 33 | nan | nan | nan | Cerrado | nan |
| ed0b585c-6958-33d9-8710-103a3dbc79e6 | -3.5014 | -43.228001 | 2024-10-16 00:42:23 | METOP-B | ANAPURUS | MARANHÃO | Brasil | 2100808 | 21 | 33 | nan | nan | nan | Cerrado | nan |
| 3132830c-4bd0-39a8-bb52-c53a071a795c | -3.5051 | -43.243698 | 2024-10-16 00:42:23 | METOP-B | ANAPURUS | MARANHÃO | Brasil | 2100808 | 21 | 33 | nan | nan | nan | Cerrado | nan |
| 5aeea1ea-37c6-3954-b07b-ed954a2e97b1 | -4.8205 | -49.134998 | 2024-10-16 00:42:24 | METOP-B | JACUNDÁ | PARÁ | Brasil | 1503804 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| 62abb8d7-e8be-3d5f-9e9a-fb347aaf5d82 | -3.9709 | -45.580399 | 2024-10-16 00:42:25 | METOP-B | SANTA LUZIA | MARANHÃO | Brasil | 2110005 | 21 | 33 | nan | nan | nan | Amazônia | nan |
| 61ce1c82-34b4-3cf1-8cb8-ddc2935fb6b7 | -3.9734 | -45.591099 | 2024-10-16 00:42:25 | METOP-B | SANTA LUZIA | MARANHÃO | Brasil | 2110005 | 21 | 33 | nan | nan | nan | Amazônia | nan |
| 14d4df8f-df17-3f15-80e3-2ab9b75cbf60 | -4.4674 | -47.7262 | 2024-10-16 00:42:25 | METOP-B | DOM ELISEU | PARÁ | Brasil | 1502939 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| 579ad9f1-98f1-3340-b8a1-560cf4e4f409 | -4.4693 | -47.7342 | 2024-10-16 00:42:25 | METOP-B | DOM ELISEU | PARÁ | Brasil | 1502939 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| 7295eaff-f486-33e3-8469-fc85d1b6a3f9 | -3.9564 | -45.6064 | 2024-10-16 00:42:25 | METOP-B | SANTA LUZIA | MARANHÃO | Brasil | 2110005 | 21 | 33 | nan | nan | nan | Amazônia | nan |
| 0f7088a2-7a5c-3719-a1d8-513b7063f133 | -3.9589 | -45.6171 | 2024-10-16 00:42:25 | METOP-B | SANTA LUZIA | MARANHÃO | Brasil | 2110005 | 21 | 33 | nan | nan | nan | Amazônia | nan |
| b3aa2a65-c8ca-3532-9ef3-cd49896b419c | -4.8148 | -49.381901 | 2024-10-16 00:42:25 | METOP-B | NOVA IPIXUNA | PARÁ | Brasil | 1504976 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| cc341a68-63d1-3d76-b272-a60a0448dc01 | -4.8164 | -49.389 | 2024-10-16 00:42:25 | METOP-B | NOVA IPIXUNA | PARÁ | Brasil | 1504976 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| d514c170-f6a4-304c-9e8b-114dc8b73d14 | -4.9686 | -50.471901 | 2024-10-16 00:42:27 | METOP-B | ITUPIRANGA | PARÁ | Brasil | 1503705 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| 03fd8b38-3025-3aef-b414-655ed104554b | -4.9975 | -50.874802 | 2024-10-16 00:42:28 | METOP-B | ANAPU | PARÁ | Brasil | 1500859 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| 7091b2e1-7d40-33e6-bf10-22b45d97f21d | -3.8634 | -45.958801 | 2024-10-16 00:42:28 | METOP-B | ALTO ALEGRE DO PINDARÉ | MARANHÃO | Brasil | 2100477 | 21 | 33 | nan | nan | nan | Amazônia | nan |
| b998ddac-05c1-3f0b-99bd-92639251da17 | -3.9613 | -46.425598 | 2024-10-16 00:42:28 | METOP-B | BOM JARDIM | MARANHÃO | Brasil | 2102002 | 21 | 33 | nan | nan | nan | Amazônia | nan |
| 8cd8c7b2-316f-3db0-a568-2f5a01046780 | -3.9493 | -46.418201 | 2024-10-16 00:42:28 | METOP-B | BOM JARDIM | MARANHÃO | Brasil | 2102002 | 21 | 33 | nan | nan | nan | Amazônia | nan |
| a653b915-bc86-3fca-bb26-91fd621014e4 | -3.9515 | -46.427799 | 2024-10-16 00:42:28 | METOP-B | BOM JARDIM | MARANHÃO | Brasil | 2102002 | 21 | 33 | nan | nan | nan | Amazônia | nan |
| f0296f17-aa20-3714-bcf2-e928d7d0d972 | -3.9538 | -46.437401 | 2024-10-16 00:42:28 | METOP-B | BOM JARDIM | MARANHÃO | Brasil | 2102002 | 21 | 33 | nan | nan | nan | Amazônia | nan |
| d6e3471e-70a1-3397-98da-c1d1437c8527 | -4.361 | -48.205898 | 2024-10-16 00:42:28 | METOP-B | RONDON DO PARÁ | PARÁ | Brasil | 1506187 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| 89e64325-5ad5-3c4c-bcd6-84037313d37e | -4.3628 | -48.2136 | 2024-10-16 00:42:28 | METOP-B | RONDON DO PARÁ | PARÁ | Brasil | 1506187 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| 1be2b631-68ea-379a-9629-178c9e179a61 | -3.9329 | -46.391701 | 2024-10-16 00:42:28 | METOP-B | BOM JARDIM | MARANHÃO | Brasil | 2102002 | 21 | 33 | nan | nan | nan | Amazônia | nan |
| cef42c9e-c8e9-346c-b1ee-6c975d0c513e | -3.9351 | -46.401299 | 2024-10-16 00:42:28 | METOP-B | BOM JARDIM | MARANHÃO | Brasil | 2102002 | 21 | 33 | nan | nan | nan | Amazônia | nan |
| dc38ce09-3cf5-3166-a5b8-54fddff0eb8e | -4.8823 | -50.591599 | 2024-10-16 00:42:28 | METOP-B | NOVO REPARTIMENTO | PARÁ | Brasil | 1505064 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| 65b666d9-45b7-3d0c-ae23-0e9430b9f207 | -4.3516 | -48.480099 | 2024-10-16 00:42:29 | METOP-B | RONDON DO PARÁ | PARÁ | Brasil | 1506187 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| 163a61fc-ff7a-3d6a-9639-18d6e90c3dc0 | -4.3533 | -48.487598 | 2024-10-16 00:42:29 | METOP-B | RONDON DO PARÁ | PARÁ | Brasil | 1506187 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| 71d148fa-b152-3202-a502-b5b047688e00 | -3.4113 | -44.548698 | 2024-10-16 00:42:30 | METOP-B | ANAJATUBA | MARANHÃO | Brasil | 2100709 | 21 | 33 | nan | nan | nan | Amazônia | nan |
| f249fe37-f786-34be-bb28-4cbc0ce3c3f8 | -4.4447 | -49.023701 | 2024-10-16 00:42:30 | METOP-B | JACUNDÁ | PARÁ | Brasil | 1503804 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| d15b7c51-1d60-32db-84c9-28b9453c5071 | -3.3986 | -44.5382 | 2024-10-16 00:42:30 | METOP-B | ANAJATUBA | MARANHÃO | Brasil | 2100709 | 21 | 33 | nan | nan | nan | Amazônia | nan |
| ac1c85d1-42e3-3b85-8f95-3c0629ddfe91 | -3.4016 | -44.550999 | 2024-10-16 00:42:30 | METOP-B | ANAJATUBA | MARANHÃO | Brasil | 2100709 | 21 | 33 | nan | nan | nan | Amazônia | nan |
| c19a86c0-fcd5-3788-9951-e836e9a7c888 | -3.4046 | -44.563801 | 2024-10-16 00:42:30 | METOP-B | ANAJATUBA | MARANHÃO | Brasil | 2100709 | 21 | 33 | nan | nan | nan | Amazônia | nan |
| 539d6d8a-8f5e-3641-a10a-e1c0f5ccff5a | -4.3218 | -48.620499 | 2024-10-16 00:42:30 | METOP-B | RONDON DO PARÁ | PARÁ | Brasil | 1506187 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| 36c5b10e-6e66-3b20-af03-1e25f6260e8e | -4.3952 | -49.6674 | 2024-10-16 00:42:33 | METOP-B | NOVO REPARTIMENTO | PARÁ | Brasil | 1505064 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| 29a554b1-3987-38f3-8d50-243d9500fa16 | -3.9606 | -47.942402 | 2024-10-16 00:42:34 | METOP-B | DOM ELISEU | PARÁ | Brasil | 1502939 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| 8e4508eb-1874-335c-a7b4-4f082a9eec1c | -3.9624 | -47.950401 | 2024-10-16 00:42:34 | METOP-B | DOM ELISEU | PARÁ | Brasil | 1502939 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| 9cb4d9eb-98d9-3fa4-b97f-bdd9c81da4a5 | -3.8005 | -47.783901 | 2024-10-16 00:42:36 | METOP-B | ULIANÓPOLIS | PARÁ | Brasil | 1508126 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| e58c7feb-50c9-3a3d-b58a-ed5927c98042 | -3.8024 | -47.792099 | 2024-10-16 00:42:36 | METOP-B | ULIANÓPOLIS | PARÁ | Brasil | 1508126 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| e00a3b77-e7a7-3504-9e8e-87660bcf4b2c | -3.9289 | -48.344101 | 2024-10-16 00:42:36 | METOP-B | DOM ELISEU | PARÁ | Brasil | 1502939 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| bf8a9e0e-564f-3b5c-ab37-40c8f71b8db6 | -4.4083 | -50.682701 | 2024-10-16 00:42:36 | METOP-B | NOVO REPARTIMENTO | PARÁ | Brasil | 1505064 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| 982f6dac-a92f-3307-98c1-6dd8bf7a5078 | -4.4098 | -50.689602 | 2024-10-16 00:42:36 | METOP-B | NOVO REPARTIMENTO | PARÁ | Brasil | 1505064 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| 5713343b-2908-3aef-a70b-b6a899df0e64 | -4.3573 | -50.959499 | 2024-10-16 00:42:38 | METOP-B | NOVO REPARTIMENTO | PARÁ | Brasil | 1505064 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| d779dba4-e60e-3d2e-bbc3-822b0f3f9115 | -4.3588 | -50.966301 | 2024-10-16 00:42:38 | METOP-B | NOVO REPARTIMENTO | PARÁ | Brasil | 1505064 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| edd6a1bb-19b5-35fa-9468-d738e205253b | -4.3603 | -50.973099 | 2024-10-16 00:42:38 | METOP-B | NOVO REPARTIMENTO | PARÁ | Brasil | 1505064 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| aa5a4114-1b7a-34f6-b4bb-9f09bb51edcf | -4.349 | -50.968498 | 2024-10-16 00:42:38 | METOP-B | NOVO REPARTIMENTO | PARÁ | Brasil | 1505064 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| 9deebb63-18f2-310f-9a1e-a37e4f014615 | -4.3505 | -50.9753 | 2024-10-16 00:42:38 | METOP-B | NOVO REPARTIMENTO | PARÁ | Brasil | 1505064 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| f656c86e-6ad9-3496-adfd-b4c8c909bde6 | -3.2809 | -46.510399 | 2024-10-16 00:42:39 | METOP-B | CENTRO NOVO DO MARANHÃO | MARANHÃO | Brasil | 2103174 | 21 | 33 | nan | nan | nan | Amazônia | nan |
| 393b6818-3019-3851-a2f0-1ee173fa1e79 | -3.2831 | -46.5201 | 2024-10-16 00:42:39 | METOP-B | CENTRO NOVO DO MARANHÃO | MARANHÃO | Brasil | 2103174 | 21 | 33 | nan | nan | nan | Amazônia | nan |
| 4432bcff-e00e-3e55-8b5e-1fa21709168a | -3.8678 | -49.069901 | 2024-10-16 00:42:39 | METOP-B | GOIANÉSIA DO PARÁ | PARÁ | Brasil | 1503093 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| 41707b2f-828d-3005-883b-116943705c9e | -3.9313 | -49.3946 | 2024-10-16 00:42:39 | METOP-B | BREU BRANCO | PARÁ | Brasil | 1501782 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| bf7ba208-bbae-3720-8666-2d27124656c9 | -3.9329 | -49.401699 | 2024-10-16 00:42:39 | METOP-B | BREU BRANCO | PARÁ | Brasil | 1501782 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| 27f83433-6dd0-3581-984f-ee3639d5fde2 | -3.2494 | -46.8647 | 2024-10-16 00:42:41 | METOP-B | PARAGOMINAS | PARÁ | Brasil | 1505502 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| b56993a9-c5b8-31f6-9279-831fca526fc9 | -3.2515 | -46.873901 | 2024-10-16 00:42:41 | METOP-B | PARAGOMINAS | PARÁ | Brasil | 1505502 | 15 | 33 | nan | nan | nan | Amazônia | nan |


[Clique aqui para ver as próximas entradas](README8.md)
