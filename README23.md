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

## Dados Diários - Página 23

| ID | Latitude | Longitude | Data/Hora GMT | Satélite | Município | Estado | País | Município ID | Estado ID | País ID | Dias sem Chuva | Precipitação | Risco de Fogo | Bioma | FRP |
|----|----------|-----------|---------------|----------|-----------|--------|------|--------------|-----------|---------|----------------|--------------|----------------|-------|-----|
| c5265d71-8562-3829-a5be-e53b9655cc25 | -8.23706 | -45.06132 | 2025-08-05 04:38:00 | NOAA-20 | BAIXA GRANDE DO RIBEIRO | PIAUÍ | Brasil | 2201150 | 22 | 33 | nan | nan | nan | Cerrado | 1.8 |
| b3a1cc8c-2c1f-3c2f-a310-6b5a1e9773c9 | -6.72323 | -47.20861 | 2025-08-05 04:38:00 | NOAA-20 | ESTREITO | MARANHÃO | Brasil | 2104057 | 21 | 33 | nan | nan | nan | Cerrado | 1.3 |
| d01a39a4-abd8-355c-988d-2d45e35a22bb | -6.90196 | -52.86413 | 2025-08-05 04:38:00 | NOAA-20 | SÃO FÉLIX DO XINGU | PARÁ | Brasil | 1507300 | 15 | 33 | nan | nan | nan | Amazônia | 0.7 |
| 64f6b8a6-795f-339a-8c7d-025d2f003e71 | -8.94836 | -46.74366 | 2025-08-05 04:38:00 | NOAA-20 | BALSAS | MARANHÃO | Brasil | 2101400 | 21 | 33 | nan | nan | nan | Cerrado | 10.5 |
| ade7b7ba-494a-33ad-9130-edfca141d60a | -7.98744 | -43.16471 | 2025-08-05 04:38:00 | NOAA-20 | PAVUSSU | PIAUÍ | Brasil | 2207850 | 22 | 33 | nan | nan | nan | Caatinga | 6.7 |
| f03d7422-ca3a-3046-9863-e7b9a131aae7 | -8.25305 | -45.06367 | 2025-08-05 04:38:00 | NOAA-20 | BAIXA GRANDE DO RIBEIRO | PIAUÍ | Brasil | 2201150 | 22 | 33 | nan | nan | nan | Cerrado | 1.3 |
| a30057e4-e859-301a-915e-4102aea1c63d | -7.34017 | -44.68068 | 2025-08-05 04:38:00 | NOAA-20 | BENEDITO LEITE | MARANHÃO | Brasil | 2101806 | 21 | 33 | nan | nan | nan | Cerrado | 1.0 |
| 3f4edf1a-7144-30f7-8dbb-eebf417f37bb | -2.90745 | -48.29405 | 2025-08-05 04:38:00 | NOAA-20 | TOMÉ-AÇU | PARÁ | Brasil | 1508001 | 15 | 33 | nan | nan | nan | Amazônia | 1.3 |
| 9c0f4d3e-0a05-34e3-bba2-5924306faec7 | -9.40244 | -45.50211 | 2025-08-05 04:38:00 | NOAA-20 | SANTA FILOMENA | PIAUÍ | Brasil | 2209203 | 22 | 33 | nan | nan | nan | Cerrado | 1.8 |
| ae5ef795-0fd0-38d7-bce7-862d05bf2931 | -8.21758 | -45.05487 | 2025-08-05 04:38:00 | NOAA-20 | BAIXA GRANDE DO RIBEIRO | PIAUÍ | Brasil | 2201150 | 22 | 33 | nan | nan | nan | Cerrado | 1.5 |
| 5ef7be7b-e085-3be7-95ad-91b14533ba82 | -7.08803 | -44.35989 | 2025-08-05 04:38:00 | NOAA-20 | BENEDITO LEITE | MARANHÃO | Brasil | 2101806 | 21 | 33 | nan | nan | nan | Cerrado | 1.1 |
| 1c738f25-98d7-30b7-a012-9e0eeaeb1fdf | -7.38787 | -44.63755 | 2025-08-05 04:38:00 | NOAA-20 | URUÇUÍ | PIAUÍ | Brasil | 2211209 | 22 | 33 | nan | nan | nan | Cerrado | 2.6 |
| 5ba081db-7399-3e7b-93c6-8399bb68afc1 | -7.99258 | -43.16099 | 2025-08-05 04:38:00 | NOAA-20 | CANTO DO BURITI | PIAUÍ | Brasil | 2202307 | 22 | 33 | nan | nan | nan | Caatinga | 6.7 |
| 769be847-e60f-32e6-92b4-6be1da3e7054 | -6.21901 | -45.8623 | 2025-08-05 04:38:00 | NOAA-20 | GRAJAÚ | MARANHÃO | Brasil | 2104800 | 21 | 33 | nan | nan | nan | Cerrado | 1.0 |
| 8486ed96-9e88-3cf9-8ec0-05e986d30cc0 | -6.1531 | -57.91671 | 2025-08-05 04:38:00 | NOAA-20 | JACAREACANGA | PARÁ | Brasil | 1503754 | 15 | 33 | nan | nan | nan | Amazônia | 1.8 |
| 0af095fe-1c64-38ea-99d6-866c276ba7e6 | -3.49411 | -59.37521 | 2025-08-05 04:38:00 | NOAA-20 | AUTAZES | AMAZONAS | Brasil | 1300300 | 13 | 33 | nan | nan | nan | Amazônia | 1.5 |
| c9b081e5-2109-3511-a168-05e212ee69ef | -7.90301 | -45.54052 | 2025-08-05 04:38:00 | NOAA-20 | TASSO FRAGOSO | MARANHÃO | Brasil | 2112001 | 21 | 33 | nan | nan | nan | Cerrado | 2.2 |
| e21a2c9d-705d-34f4-bb09-440e4fee8bf4 | -8.948 | -46.74604 | 2025-08-05 04:38:00 | NOAA-20 | BALSAS | MARANHÃO | Brasil | 2101400 | 21 | 33 | nan | nan | nan | Cerrado | 2.0 |
| 441e0118-39d7-3319-8881-cfed386c6e79 | -6.96649 | -42.87182 | 2025-08-05 04:38:00 | NOAA-20 | FLORIANO | PIAUÍ | Brasil | 2203909 | 22 | 33 | nan | nan | nan | Caatinga | 19.8 |
| e9b840bb-1722-34f4-bd82-d6a414249f66 | -8.94294 | -46.72956 | 2025-08-05 04:38:00 | NOAA-20 | BALSAS | MARANHÃO | Brasil | 2101400 | 21 | 33 | nan | nan | nan | Cerrado | 13.1 |
| 0b6c48ae-f6ca-3d60-8fd8-0c13bd3ccdab | -5.98916 | -49.91003 | 2025-08-05 04:38:00 | NOAA-20 | PARAUAPEBAS | PARÁ | Brasil | 1505536 | 15 | 33 | nan | nan | nan | Amazônia | 3.1 |
| c330401e-69d5-3b5b-8761-62f5671152a6 | -7.82053 | -46.88573 | 2025-08-05 04:38:00 | NOAA-20 | CAROLINA | MARANHÃO | Brasil | 2102804 | 21 | 33 | nan | nan | nan | Cerrado | 0.6 |
| e5639246-0f9a-38d4-8da8-e72eeae9fe76 | -8.26903 | -45.06607 | 2025-08-05 04:38:00 | NOAA-20 | BAIXA GRANDE DO RIBEIRO | PIAUÍ | Brasil | 2201150 | 22 | 33 | nan | nan | nan | Cerrado | 1.7 |
| 048babbf-213e-34bf-91f4-79bab5ea2fbd | -7.56407 | -44.88047 | 2025-08-05 04:38:00 | NOAA-20 | URUÇUÍ | PIAUÍ | Brasil | 2211209 | 22 | 33 | nan | nan | nan | Cerrado | 0.7 |
| 9d723210-5c67-3aee-a220-d14291291d2c | -9.39848 | -45.50159 | 2025-08-05 04:38:00 | NOAA-20 | SANTA FILOMENA | PIAUÍ | Brasil | 2209203 | 22 | 33 | nan | nan | nan | Cerrado | 1.8 |
| a8eb15d0-3698-37a5-b2d8-67c398d80fab | -7.5851 | -44.79365 | 2025-08-05 04:38:00 | NOAA-20 | URUÇUÍ | PIAUÍ | Brasil | 2211209 | 22 | 33 | nan | nan | nan | Cerrado | 1.2 |
| 673063b4-00e5-3f6d-aebc-d5eaa73e61da | -9.05916 | -45.05772 | 2025-08-05 04:38:00 | NOAA-20 | BOM JESUS | PIAUÍ | Brasil | 2201903 | 22 | 33 | nan | nan | nan | Cerrado | 0.9 |
| 5ba464e0-4686-38b0-b820-8bbc54d1d32b | -6.98228 | -43.38897 | 2025-08-05 04:38:00 | NOAA-20 | JERUMENHA | PIAUÍ | Brasil | 2205300 | 22 | 33 | nan | nan | nan | Caatinga | 1.3 |
| a3201152-7d96-3764-99bc-84f6700e15b8 | -7.11345 | -47.8433 | 2025-08-05 04:38:00 | NOAA-20 | BABAÇULÂNDIA | TOCANTINS | Brasil | 1703008 | 17 | 33 | nan | nan | nan | Cerrado | 4.4 |
| e23f0b0d-10b6-3cb3-b517-c8bd9fa2dfdb | -8.01453 | -43.13638 | 2025-08-05 04:38:00 | NOAA-20 | CANTO DO BURITI | PIAUÍ | Brasil | 2202307 | 22 | 33 | nan | nan | nan | Caatinga | 0.9 |
| 0516da81-f3fe-38e4-a23c-b88e244dc226 | -8.01518 | -43.13177 | 2025-08-05 04:38:00 | NOAA-20 | CANTO DO BURITI | PIAUÍ | Brasil | 2202307 | 22 | 33 | nan | nan | nan | Caatinga | 2.1 |
| 89153033-aeff-3276-80a5-ead60bc4d1d4 | -6.62395 | -59.97649 | 2025-08-05 04:38:00 | NOAA-20 | NOVO ARIPUANÃ | AMAZONAS | Brasil | 1303304 | 13 | 33 | nan | nan | nan | Amazônia | 0.6 |
| c57432d3-e159-3f6b-b13a-5692422894f5 | -8.24506 | -45.06246 | 2025-08-05 04:38:00 | NOAA-20 | BAIXA GRANDE DO RIBEIRO | PIAUÍ | Brasil | 2201150 | 22 | 33 | nan | nan | nan | Cerrado | 1.3 |
| bd1dc2b9-f981-39ff-b0f6-224c66cb0416 | -6.4673 | -43.03088 | 2025-08-05 04:38:00 | NOAA-20 | BARÃO DE GRAJAÚ | MARANHÃO | Brasil | 2101509 | 21 | 33 | nan | nan | nan | Cerrado | 1.7 |
| 603293e6-e35a-39e4-92dc-98cd89277c95 | -9.39775 | -45.50667 | 2025-08-05 04:38:00 | NOAA-20 | SANTA FILOMENA | PIAUÍ | Brasil | 2209203 | 22 | 33 | nan | nan | nan | Cerrado | 5.0 |
| bf4584a7-872b-3fe7-9cef-6e240b3cef5f | -6.42324 | -44.81813 | 2025-08-05 04:38:00 | NOAA-20 | MIRADOR | MARANHÃO | Brasil | 2106706 | 21 | 33 | nan | nan | nan | Cerrado | 2.6 |
| 71927522-a7f7-36ab-bb5d-c9e5ab116f3b | -7.56508 | -44.87359 | 2025-08-05 04:38:00 | NOAA-20 | URUÇUÍ | PIAUÍ | Brasil | 2211209 | 22 | 33 | nan | nan | nan | Cerrado | 1.5 |
| f92d8f8c-946e-3d4a-af0d-c9a15eade1c7 | -8.26054 | -45.06835 | 2025-08-05 04:38:00 | NOAA-20 | BAIXA GRANDE DO RIBEIRO | PIAUÍ | Brasil | 2201150 | 22 | 33 | nan | nan | nan | Cerrado | 1.2 |
| 3732cca6-3d6a-3056-9fac-f6c253074de1 | -6.28731 | -45.74769 | 2025-08-05 04:38:00 | NOAA-20 | FERNANDO FALCÃO | MARANHÃO | Brasil | 2104081 | 21 | 33 | nan | nan | nan | Cerrado | 0.9 |
| 2f1b9fc0-205f-341d-8c7b-1c6622960d5f | -6.89695 | -52.86546 | 2025-08-05 04:38:00 | NOAA-20 | SÃO FÉLIX DO XINGU | PARÁ | Brasil | 1507300 | 15 | 33 | nan | nan | nan | Amazônia | 3.2 |
| 3a166456-cc12-3a0a-bafc-a61f18c453e1 | -8.71722 | -46.4387 | 2025-08-05 04:38:00 | NOAA-20 | BALSAS | MARANHÃO | Brasil | 2101400 | 21 | 33 | nan | nan | nan | Cerrado | 1.7 |
| 337b7f4a-f993-3b70-bd91-a9360dbdb16d | -8.26453 | -45.06895 | 2025-08-05 04:38:00 | NOAA-20 | BAIXA GRANDE DO RIBEIRO | PIAUÍ | Brasil | 2201150 | 22 | 33 | nan | nan | nan | Cerrado | 1.4 |
| b16a6eac-f844-3699-9d74-3ea921718b6f | -8.24556 | -45.05901 | 2025-08-05 04:38:00 | NOAA-20 | BAIXA GRANDE DO RIBEIRO | PIAUÍ | Brasil | 2201150 | 22 | 33 | nan | nan | nan | Cerrado | 1.3 |
| df87f77b-a3a4-3c3a-b0dd-912ab9cee73f | -5.78401 | -43.62236 | 2025-08-05 04:38:00 | NOAA-20 | LAGOA DO MATO | MARANHÃO | Brasil | 2105922 | 21 | 33 | nan | nan | nan | Cerrado | 3.2 |
| dafddb38-c28e-3227-adb6-c0bb3668f6bf | -8.84596 | -47.61042 | 2025-08-05 04:38:00 | NOAA-20 | SANTA MARIA DO TOCANTINS | TOCANTINS | Brasil | 1718881 | 17 | 33 | nan | nan | nan | Cerrado | 1.8 |
| e2a97f4e-779d-38a8-866a-0dd52ee911bf | -6.37847 | -43.71795 | 2025-08-05 04:38:00 | NOAA-20 | SÃO JOÃO DOS PATOS | MARANHÃO | Brasil | 2111102 | 21 | 33 | nan | nan | nan | Cerrado | 4.3 |
| bdda7bc0-32a7-3d1d-b065-0c0271bb15d5 | -7.53706 | -44.86935 | 2025-08-05 04:38:00 | NOAA-20 | URUÇUÍ | PIAUÍ | Brasil | 2211209 | 22 | 33 | nan | nan | nan | Cerrado | 1.7 |
| ec78274c-872b-31ec-a57b-b7500e568832 | -5.48282 | -42.16277 | 2025-08-05 04:38:00 | NOAA-20 | ALTO LONGÁ | PIAUÍ | Brasil | 2200301 | 22 | 33 | nan | nan | nan | Caatinga | 4.5 |
| 9b2891b8-726c-3c0e-a74d-a364b06b892a | -7.84255 | -44.94227 | 2025-08-05 04:38:00 | NOAA-20 | RIBEIRO GONÇALVES | PIAUÍ | Brasil | 2208908 | 22 | 33 | nan | nan | nan | Cerrado | 1.2 |
| c37213ec-601d-31e6-a916-805cde7246ae | -8.15096 | -49.1421 | 2025-08-05 04:38:00 | NOAA-20 | JUARINA | TOCANTINS | Brasil | 1711803 | 17 | 33 | nan | nan | nan | Amazônia | 0.8 |
| 5ad2a20f-7f9f-3dd4-a377-e1b9d30b5f4c | -3.4948 | -59.37109 | 2025-08-05 04:38:00 | NOAA-20 | AUTAZES | AMAZONAS | Brasil | 1300300 | 13 | 33 | nan | nan | nan | Amazônia | 1.9 |
| 6308fff5-53af-3f62-b42a-9e804af45a6d | -8.21911 | -45.05825 | 2025-08-05 04:38:00 | NOAA-20 | BAIXA GRANDE DO RIBEIRO | PIAUÍ | Brasil | 2201150 | 22 | 33 | nan | nan | nan | Cerrado | 1.2 |
| d13ef226-fd73-3df4-a768-737cab5f4053 | -8.93836 | -46.73575 | 2025-08-05 04:38:00 | NOAA-20 | BALSAS | MARANHÃO | Brasil | 2101400 | 21 | 33 | nan | nan | nan | Cerrado | 16.7 |
| 30fa44c1-a9e2-3468-95e6-096c1072bc14 | -6.15203 | -57.91532 | 2025-08-05 04:38:00 | NOAA-20 | JACAREACANGA | PARÁ | Brasil | 1503754 | 15 | 33 | nan | nan | nan | Amazônia | 1.9 |
| 5e497489-66f9-3d14-969d-e274c2f02175 | -7.60456 | -45.31161 | 2025-08-05 04:38:00 | NOAA-20 | RIBEIRO GONÇALVES | PIAUÍ | Brasil | 2208908 | 22 | 33 | nan | nan | nan | Cerrado | 8.6 |
| 243fd1de-b047-3aec-945d-be641f04e3bb | -3.88402 | -54.21393 | 2025-08-05 04:38:00 | NOAA-20 | PLACAS | PARÁ | Brasil | 1505650 | 15 | 33 | nan | nan | nan | Amazônia | 1.4 |
| 76a906b1-2ee1-36c0-bf1c-56347acad072 | -7.60532 | -45.30646 | 2025-08-05 04:38:00 | NOAA-20 | RIBEIRO GONÇALVES | PIAUÍ | Brasil | 2208908 | 22 | 33 | nan | nan | nan | Cerrado | 8.6 |
| d1705c73-2f5c-3390-bf26-1abe22490531 | -8.84537 | -47.61435 | 2025-08-05 04:38:00 | NOAA-20 | SANTA MARIA DO TOCANTINS | TOCANTINS | Brasil | 1718881 | 17 | 33 | nan | nan | nan | Cerrado | 1.8 |
| 6b407815-0d13-3061-aefc-2476b825566c | -6.46494 | -43.02795 | 2025-08-05 04:38:00 | NOAA-20 | BARÃO DE GRAJAÚ | MARANHÃO | Brasil | 2101509 | 21 | 33 | nan | nan | nan | Cerrado | 2.7 |
| aa965d36-be37-3ec6-b28e-0d3f272193d4 | -6.57641 | -46.34057 | 2025-08-05 04:38:00 | NOAA-20 | FORMOSA DA SERRA NEGRA | MARANHÃO | Brasil | 2104099 | 21 | 33 | nan | nan | nan | Cerrado | 0.6 |
| 95734d0c-b3a7-306f-98d8-d7894b035151 | -7.34422 | -44.68124 | 2025-08-05 04:38:00 | NOAA-20 | BENEDITO LEITE | MARANHÃO | Brasil | 2101806 | 21 | 33 | nan | nan | nan | Cerrado | 1.0 |
| 957aaf19-f0a2-356e-8efe-d39d4dfe7797 | -8.94597 | -46.73445 | 2025-08-05 04:38:00 | NOAA-20 | BALSAS | MARANHÃO | Brasil | 2101400 | 21 | 33 | nan | nan | nan | Cerrado | 13.1 |
| 270ea67a-77db-358d-beae-0964d485f536 | -7.85392 | -46.73879 | 2025-08-05 04:38:00 | NOAA-20 | RIACHÃO | MARANHÃO | Brasil | 2109502 | 21 | 33 | nan | nan | nan | Cerrado | 1.2 |
| 0b8cbb03-a5eb-324e-8930-d4f7c4eab7d9 | -8.71112 | -46.42873 | 2025-08-05 04:38:00 | NOAA-20 | BALSAS | MARANHÃO | Brasil | 2101400 | 21 | 33 | nan | nan | nan | Cerrado | 0.8 |
| a9b64f0b-d3ab-38ec-a2e2-e612bf2456f7 | -7.78226 | -45.21956 | 2025-08-05 04:38:00 | NOAA-20 | RIBEIRO GONÇALVES | PIAUÍ | Brasil | 2208908 | 22 | 33 | nan | nan | nan | Cerrado | 2.1 |
| 73a07634-1e44-3d65-a14d-b7e3951a70db | -8.94631 | -46.73251 | 2025-08-05 04:38:00 | NOAA-20 | BALSAS | MARANHÃO | Brasil | 2101400 | 21 | 33 | nan | nan | nan | Cerrado | 9.1 |
| d476b4e1-7fd4-3319-b9a6-3122cae78fbd | -9.05403 | -45.06458 | 2025-08-05 04:38:00 | NOAA-20 | BOM JESUS | PIAUÍ | Brasil | 2201903 | 22 | 33 | nan | nan | nan | Cerrado | 0.9 |
| 07f83eb3-500e-33f1-8cb8-2f99af3fb3f7 | -7.11745 | -47.84 | 2025-08-05 04:38:00 | NOAA-20 | BABAÇULÂNDIA | TOCANTINS | Brasil | 1703008 | 17 | 33 | nan | nan | nan | Cerrado | 4.4 |
| 4bad03d1-881d-3e84-89cc-7966ad4524a1 | -7.3868 | -44.6448 | 2025-08-05 04:38:00 | NOAA-20 | URUÇUÍ | PIAUÍ | Brasil | 2211209 | 22 | 33 | nan | nan | nan | Cerrado | 1.6 |
| ae080121-8b16-3a44-8b2b-8911c7d13aa3 | -2.90875 | -40.134 | 2025-08-05 04:38:00 | NOAA-20 | ACARAÚ | CEARÁ | Brasil | 2300200 | 23 | 33 | nan | nan | nan | Caatinga | 2.9 |
| 29e70642-82d2-3a73-a76c-3410abe3493a | -4.64389 | -43.18446 | 2025-08-05 04:38:00 | NOAA-20 | CAXIAS | MARANHÃO | Brasil | 2103000 | 21 | 33 | nan | nan | nan | Cerrado | 1.5 |
| 8a38ef99-2b3b-38d7-ac65-71e66f3bd98f | -9.39995 | -45.49141 | 2025-08-05 04:38:00 | NOAA-20 | SANTA FILOMENA | PIAUÍ | Brasil | 2209203 | 22 | 33 | nan | nan | nan | Cerrado | 0.9 |
| 224f1494-47f6-3109-984e-70497b80f931 | -5.98585 | -49.9095 | 2025-08-05 04:38:00 | NOAA-20 | PARAUAPEBAS | PARÁ | Brasil | 1505536 | 15 | 33 | nan | nan | nan | Amazônia | 5.3 |
| 61829413-afb3-323f-8ca3-1a33995fd9d9 | -9.18455 | -48.84369 | 2025-08-05 04:38:00 | NOAA-20 | DOIS IRMÃOS DO TOCANTINS | TOCANTINS | Brasil | 1707207 | 17 | 33 | nan | nan | nan | Cerrado | 0.5 |
| f9901e83-db24-3424-8543-846600045bf5 | -6.68146 | -49.78616 | 2025-08-05 04:38:00 | NOAA-20 | ÁGUA AZUL DO NORTE | PARÁ | Brasil | 1500347 | 15 | 33 | nan | nan | nan | Amazônia | 0.5 |
| a58978f1-0311-3fc6-a643-d57320256269 | -7.56755 | -44.88458 | 2025-08-05 04:38:00 | NOAA-20 | URUÇUÍ | PIAUÍ | Brasil | 2211209 | 22 | 33 | nan | nan | nan | Cerrado | 2.1 |
| 7ab9bd0c-63a7-3637-9b3e-4b477a3d2f64 | -9.3938 | -45.50613 | 2025-08-05 04:38:00 | NOAA-20 | SANTA FILOMENA | PIAUÍ | Brasil | 2209203 | 22 | 33 | nan | nan | nan | Cerrado | 2.9 |
| 81ead5b0-3f6f-3595-82de-df001431e775 | -8.23356 | -45.05727 | 2025-08-05 04:38:00 | NOAA-20 | BAIXA GRANDE DO RIBEIRO | PIAUÍ | Brasil | 2201150 | 22 | 33 | nan | nan | nan | Cerrado | 1.8 |
| ec8736d4-105f-316e-b492-fe7a8ced2e4b | -7.72314 | -46.61735 | 2025-08-05 04:38:00 | NOAA-20 | RIACHÃO | MARANHÃO | Brasil | 2109502 | 21 | 33 | nan | nan | nan | Cerrado | 0.6 |
| 2fa79ab5-d885-3f96-9824-6bbda0e88ff3 | -8.01843 | -43.17405 | 2025-08-05 04:38:00 | NOAA-20 | CANTO DO BURITI | PIAUÍ | Brasil | 2202307 | 22 | 33 | nan | nan | nan | Caatinga | 1.5 |
| 91de7238-61d9-3daf-82fc-2fae8a2904aa | -8.25654 | -45.06775 | 2025-08-05 04:38:00 | NOAA-20 | BAIXA GRANDE DO RIBEIRO | PIAUÍ | Brasil | 2201150 | 22 | 33 | nan | nan | nan | Cerrado | 1.2 |
| b8d5cf24-56f8-3d16-af83-9370085fd8db | -3.78272 | -41.6847 | 2025-08-05 04:38:00 | NOAA-20 | PIRACURUCA | PIAUÍ | Brasil | 2208304 | 22 | 33 | nan | nan | nan | Caatinga | 2.2 |
| ca9a0d63-7f32-3387-9e14-1e0960095682 | -6.64743 | -59.10842 | 2025-08-05 04:38:00 | NOAA-20 | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 2.5 |
| 8fb17c31-dad3-3037-a0e3-a554670a1b96 | -6.63753 | -60.00032 | 2025-08-05 04:38:00 | NOAA-20 | NOVO ARIPUANÃ | AMAZONAS | Brasil | 1303304 | 13 | 33 | nan | nan | nan | Amazônia | 2.3 |
| 5d9e1271-e632-3da9-8fdd-44912aabb0b8 | -6.78661 | -43.25009 | 2025-08-05 04:38:00 | NOAA-20 | FLORIANO | PIAUÍ | Brasil | 2203909 | 22 | 33 | nan | nan | nan | Caatinga | 0.9 |
| 10fbdd95-eadd-3a78-af93-fe64274c7fdf | -7.05652 | -47.46185 | 2025-08-05 04:38:00 | NOAA-20 | CAROLINA | MARANHÃO | Brasil | 2102804 | 21 | 33 | nan | nan | nan | Cerrado | 2.6 |
| 5f8dd97b-2a36-396d-9e5b-dc6d00737db9 | -7.75579 | -45.23633 | 2025-08-05 04:38:00 | NOAA-20 | RIBEIRO GONÇALVES | PIAUÍ | Brasil | 2208908 | 22 | 33 | nan | nan | nan | Cerrado | 5.7 |
| 335120d4-8c63-3efd-aa28-4ba5dd347292 | -7.38733 | -44.64118 | 2025-08-05 04:38:00 | NOAA-20 | URUÇUÍ | PIAUÍ | Brasil | 2211209 | 22 | 33 | nan | nan | nan | Cerrado | 2.6 |
| 7ed00bf0-0a46-30c2-a391-2ac787a16e18 | -7.76085 | -45.22954 | 2025-08-05 04:38:00 | NOAA-20 | RIBEIRO GONÇALVES | PIAUÍ | Brasil | 2208908 | 22 | 33 | nan | nan | nan | Cerrado | 3.8 |
| 9e8dee0e-d5de-3c10-91e1-46d866260af3 | -8.94266 | -46.73197 | 2025-08-05 04:38:00 | NOAA-20 | BALSAS | MARANHÃO | Brasil | 2101400 | 21 | 33 | nan | nan | nan | Cerrado | 16.7 |
| df1b251c-1349-3f41-a4b7-fcbcc362fe9d | -7.7601 | -45.23456 | 2025-08-05 04:38:00 | NOAA-20 | RIBEIRO GONÇALVES | PIAUÍ | Brasil | 2208908 | 22 | 33 | nan | nan | nan | Cerrado | 4.6 |
| 61135abc-9fe9-3802-9d4c-df92e039a0e1 | -7.59778 | -55.19607 | 2025-08-05 04:38:00 | NOAA-20 | NOVO PROGRESSO | PARÁ | Brasil | 1505031 | 15 | 33 | nan | nan | nan | Amazônia | 1.5 |
| 612f5c00-6814-3be7-9ae9-cce4376c68c5 | -5.2434 | -46.78066 | 2025-08-05 04:38:00 | NOAA-20 | AMARANTE DO MARANHÃO | MARANHÃO | Brasil | 2100600 | 21 | 33 | nan | nan | nan | Cerrado | 0.8 |
| bf1caa21-0540-3edd-9181-8f3d20b66d3b | -9.32199 | -44.85031 | 2025-08-05 04:38:00 | NOAA-20 | BOM JESUS | PIAUÍ | Brasil | 2201903 | 22 | 33 | nan | nan | nan | Cerrado | 1.2 |
| 163f3517-9751-3ca0-89f0-356c8efa63ad | -7.08749 | -44.36359 | 2025-08-05 04:38:00 | NOAA-20 | BENEDITO LEITE | MARANHÃO | Brasil | 2101806 | 21 | 33 | nan | nan | nan | Cerrado | 1.3 |
| 21a4871c-be1b-3b36-91ec-bbdf1421ceef | -7.2051 | -44.49654 | 2025-08-05 04:38:00 | NOAA-20 | URUÇUÍ | PIAUÍ | Brasil | 2211209 | 22 | 33 | nan | nan | nan | Cerrado | 2.0 |
| d3c28817-3cda-318c-8656-8cf59b9e8781 | -8.94201 | -46.7363 | 2025-08-05 04:38:00 | NOAA-20 | BALSAS | MARANHÃO | Brasil | 2101400 | 21 | 33 | nan | nan | nan | Cerrado | 16.7 |
| 5d882356-d9ae-387c-9647-091a85bac793 | -8.94169 | -46.73823 | 2025-08-05 04:38:00 | NOAA-20 | BALSAS | MARANHÃO | Brasil | 2101400 | 21 | 33 | nan | nan | nan | Cerrado | 12.5 |
| dc40ef90-a411-32c3-9ec5-9f4170027039 | -5.88862 | -43.73359 | 2025-08-05 04:38:00 | NOAA-20 | BURITI BRAVO | MARANHÃO | Brasil | 2102309 | 21 | 33 | nan | nan | nan | Cerrado | 1.9 |
| 34b3749c-2a44-3aa7-8482-4ba3e9556579 | -8.74136 | -46.42904 | 2025-08-05 04:38:00 | NOAA-20 | BALSAS | MARANHÃO | Brasil | 2101400 | 21 | 33 | nan | nan | nan | Cerrado | 2.3 |


[Clique aqui para ver as próximas entradas](README24.md)
