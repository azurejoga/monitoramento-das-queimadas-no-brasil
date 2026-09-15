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
| 985907ee-28d0-3110-bebd-affeabf4349e | -5.8505 | -52.043301 | 2026-09-15 00:02:00 | METOP-B | SÃO FÉLIX DO XINGU | PARÁ | Brasil | 1507300 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| f382419a-f8f9-3ae1-8ff3-033adcb004d4 | -5.5227 | -43.3507 | 2026-09-15 00:02:00 | METOP-B | MATÕES | MARANHÃO | Brasil | 2106607 | 21 | 33 | nan | nan | nan | Cerrado | nan |
| 9b84e38f-cebf-3826-b4de-1a37f04e3619 | -12.8503 | -44.378601 | 2026-09-15 00:02:00 | METOP-B | BAIANÓPOLIS | BAHIA | Brasil | 2902500 | 29 | 33 | nan | nan | nan | Cerrado | nan |
| ef2a8d17-3887-3d42-adc5-16779bb94469 | -8.5627 | -50.1297 | 2026-09-15 00:02:00 | METOP-B | SANTA MARIA DAS BARREIRAS | PARÁ | Brasil | 1506583 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| 5f6c9528-1168-3ccd-ac98-7a8cc299e8f5 | -10.0786 | -36.236698 | 2026-09-15 00:02:00 | METOP-B | CORURIPE | ALAGOAS | Brasil | 2702306 | 27 | 33 | nan | nan | nan | Mata Atlântica | nan |
| 1b920ef2-bf9a-310e-b133-2918406196d8 | -7.4489 | -49.732899 | 2026-09-15 00:02:00 | METOP-B | FLORESTA DO ARAGUAIA | PARÁ | Brasil | 1503044 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| 037e5b71-5788-3d26-93f8-f3c71fa1759d | -6.41 | -43.0485 | 2026-09-15 00:02:00 | METOP-B | SÃO FRANCISCO DO MARANHÃO | MARANHÃO | Brasil | 2110906 | 21 | 33 | nan | nan | nan | Cerrado | nan |
| 8261dc6a-03f7-3928-b7f8-021e011ce114 | -17.321301 | -46.902599 | 2026-09-15 00:02:00 | METOP-B | PARACATU | MINAS GERAIS | Brasil | 3147006 | 31 | 33 | nan | nan | nan | Cerrado | nan |
| 6b0da978-2687-376b-a369-521edbedfebc | -7.0117 | -44.607101 | 2026-09-15 00:02:00 | METOP-B | BENEDITO LEITE | MARANHÃO | Brasil | 2101806 | 21 | 33 | nan | nan | nan | Cerrado | nan |
| cbf45b92-ccb4-31ca-823e-d94006395c2f | -17.3118 | -42.5103 | 2026-09-15 00:02:00 | METOP-B | MINAS NOVAS | MINAS GERAIS | Brasil | 3141801 | 31 | 33 | nan | nan | nan | Cerrado | nan |
| 0ea333e5-6a1b-3057-92b3-13e289683c28 | -4.7754 | -42.711601 | 2026-09-15 00:02:00 | METOP-B | JOSÉ DE FREITAS | PIAUÍ | Brasil | 2205508 | 22 | 33 | nan | nan | nan | Cerrado | nan |
| f6821d27-c6ae-303b-bc7e-d50bb25764cd | -5.7795 | -49.855099 | 2026-09-15 00:02:00 | METOP-B | MARABÁ | PARÁ | Brasil | 1504208 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| 18fdac89-5266-398b-88e9-6baf31b9da05 | -3.8065 | -49.407902 | 2026-09-15 00:02:00 | METOP-B | BREU BRANCO | PARÁ | Brasil | 1501782 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| a5958763-5341-3329-94a1-1760a925119c | -7.2722 | -48.332401 | 2026-09-15 00:02:00 | METOP-B | ARAGUAÍNA | TOCANTINS | Brasil | 1702109 | 17 | 33 | nan | nan | nan | Amazônia | nan |
| 3b921b08-4863-3b25-a7dd-6e9ea364c510 | -6.0989 | -44.051998 | 2026-09-15 00:02:00 | METOP-B | COLINAS | MARANHÃO | Brasil | 2103505 | 21 | 33 | nan | nan | nan | Cerrado | nan |
| e108692e-8a15-33d0-86e3-af0867117629 | -9.8753 | -47.773701 | 2026-09-15 00:02:00 | METOP-B | RIO SONO | TOCANTINS | Brasil | 1718758 | 17 | 33 | nan | nan | nan | Cerrado | nan |
| ec31e527-c1b6-342b-9df2-c3c1882b07b3 | -4.5435 | -55.580002 | 2026-09-15 00:02:00 | METOP-B | ITAITUBA | PARÁ | Brasil | 1503606 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| ca15411b-197e-3b5b-a65f-cb2c7ef9acf5 | -10.6756 | -54.121201 | 2026-09-15 00:02:00 | METOP-B | MARCELÂNDIA | MATO GROSSO | Brasil | 5105580 | 51 | 33 | nan | nan | nan | Amazônia | nan |
| 80a34137-016e-372c-9c3c-f3c5e068f073 | -3.0756 | -51.061001 | 2026-09-15 00:02:00 | METOP-B | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| bce1c41b-7142-3cae-b522-7d45eb35f8c1 | -5.408 | -48.514301 | 2026-09-15 00:02:00 | METOP-B | ESPERANTINA | TOCANTINS | Brasil | 1707405 | 17 | 33 | nan | nan | nan | Amazônia | nan |
| b4422e6a-df78-3afd-9aea-85bc94f0859e | -16.8664 | -50.1334 | 2026-09-15 00:02:00 | METOP-B | PALMINÓPOLIS | GOIÁS | Brasil | 5215900 | 52 | 33 | nan | nan | nan | Cerrado | nan |
| c1ef21a9-a4d4-353d-bfa1-c37a615e89fc | -2.8877 | -50.4058 | 2026-09-15 00:02:00 | METOP-B | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| 427a7055-4d10-3b3d-94fb-62f26388f8dc | -2.8254 | -51.322102 | 2026-09-15 00:02:00 | METOP-B | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| 54f53e0e-d579-37b0-bab7-ddeb544980e8 | -10.9899 | -48.305901 | 2026-09-15 00:02:00 | METOP-B | PORTO NACIONAL | TOCANTINS | Brasil | 1718204 | 17 | 33 | nan | nan | nan | Cerrado | nan |
| 409fea75-025d-3205-849c-f0c39f805ba5 | -11.2254 | -43.429199 | 2026-09-15 00:02:00 | METOP-B | BARRA | BAHIA | Brasil | 2902708 | 29 | 33 | nan | nan | nan | Cerrado | nan |
| edd440c7-f4e3-3762-932f-3a2fd29bf8ab | -0.9587 | -47.567001 | 2026-09-15 00:02:00 | METOP-B | MARACANÃ | PARÁ | Brasil | 1504307 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| 47fa6d11-fa73-3b15-8683-1c20e5966dff | -5.5387 | -43.4193 | 2026-09-15 00:02:00 | METOP-B | PARNARAMA | MARANHÃO | Brasil | 2107803 | 21 | 33 | nan | nan | nan | Cerrado | nan |
| ae8e227f-2fdf-3175-813d-118ded867dad | -2.8975 | -50.403599 | 2026-09-15 00:02:00 | METOP-B | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| bd15177c-41c0-37f6-8a03-2545e6555e9c | -13.072 | -48.581001 | 2026-09-15 00:02:00 | METOP-B | JAÚ DO TOCANTINS | TOCANTINS | Brasil | 1711506 | 17 | 33 | nan | nan | nan | Cerrado | nan |
| dc7ed4ae-1f7f-3b29-a30f-8843fe5c5661 | -11.1816 | -42.806599 | 2026-09-15 00:02:00 | METOP-B | GENTIO DO OURO | BAHIA | Brasil | 2911303 | 29 | 33 | nan | nan | nan | Caatinga | nan |
| 7bb4682d-ca92-3adb-8262-d7da6e1dcb74 | -8.8018 | -46.8866 | 2026-09-15 00:02:00 | METOP-B | BALSAS | MARANHÃO | Brasil | 2101400 | 21 | 33 | nan | nan | nan | Cerrado | nan |
| c5af78a6-2624-3964-b5c7-3f2627d69f5e | -16.976 | -49.7089 | 2026-09-15 00:02:00 | METOP-B | VARJÃO | GOIÁS | Brasil | 5221908 | 52 | 33 | nan | nan | nan | Cerrado | nan |
| 4288115c-9019-3dbd-bede-5128e6b2f063 | -4.5249 | -54.931 | 2026-09-15 00:02:00 | METOP-B | RURÓPOLIS | PARÁ | Brasil | 1506195 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| e228b995-7f03-33df-944c-be653d4bb1b9 | -5.9557 | -49.259499 | 2026-09-15 00:02:00 | METOP-B | ELDORADO DO CARAJÁS | PARÁ | Brasil | 1502954 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| 131f2169-7238-3de4-965a-d05178179bb4 | -2.9105 | -50.369999 | 2026-09-15 00:02:00 | METOP-B | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| 81ad5af3-2b36-3ca2-b958-acd8e26fb18a | -13.2175 | -51.6488 | 2026-09-15 00:02:00 | METOP-B | RIBEIRÃO CASCALHEIRA | MATO GROSSO | Brasil | 5107180 | 51 | 33 | nan | nan | nan | Cerrado | nan |
| 1e36d5a3-b687-3880-a093-2c4ba4f29e93 | -5.3997 | -49.166401 | 2026-09-15 00:02:00 | METOP-B | MARABÁ | PARÁ | Brasil | 1504208 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| 0c528de8-0299-3402-8332-bbb654a58858 | -5.525 | -43.3606 | 2026-09-15 00:02:00 | METOP-B | MATÕES | MARANHÃO | Brasil | 2106607 | 21 | 33 | nan | nan | nan | Cerrado | nan |
| b125cea4-49d6-3bc4-a491-b7afda5d5ce7 | -11.2351 | -43.4268 | 2026-09-15 00:02:00 | METOP-B | BARRA | BAHIA | Brasil | 2902708 | 29 | 33 | nan | nan | nan | Cerrado | nan |
| 326ee02c-d18b-3ea5-9489-8c3fe21cd38b | -11.2176 | -43.439899 | 2026-09-15 00:02:00 | METOP-B | BARRA | BAHIA | Brasil | 2902708 | 29 | 33 | nan | nan | nan | Cerrado | nan |
| ca14bfdf-8d0b-3550-83df-b256e7572135 | -11.0991 | -40.4571 | 2026-09-15 00:02:00 | METOP-B | CAÉM | BAHIA | Brasil | 2905107 | 29 | 33 | nan | nan | nan | Caatinga | nan |
| bc4dfe93-78f0-3eb3-930e-c94fa79071a2 | -14.9595 | -47.522099 | 2026-09-15 00:02:00 | METOP-B | FORMOSA | GOIÁS | Brasil | 5208004 | 52 | 33 | nan | nan | nan | Cerrado | nan |
| e29e698d-c83b-39e8-adbc-2f616f736fb5 | -14.2263 | -47.406799 | 2026-09-15 00:02:00 | METOP-B | ALTO PARAÍSO DE GOIÁS | GOIÁS | Brasil | 5200605 | 52 | 33 | nan | nan | nan | Cerrado | nan |
| 9efc6a1a-1fe1-3524-95cf-a9ebe42ef5a2 | -7.614 | -47.285198 | 2026-09-15 00:02:00 | METOP-B | CAROLINA | MARANHÃO | Brasil | 2102804 | 21 | 33 | nan | nan | nan | Cerrado | nan |
| d9af136e-79fa-3934-acc7-274d9e6ae406 | -2.904 | -50.386799 | 2026-09-15 00:02:00 | METOP-B | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| d5efe687-3045-3dce-a6e7-b58785782051 | -10.7737 | -46.218102 | 2026-09-15 00:02:00 | METOP-B | FORMOSA DO RIO PRETO | BAHIA | Brasil | 2911105 | 29 | 33 | nan | nan | nan | Cerrado | nan |
| 320a3780-b031-34d3-aee3-f1671c9aa23b | -4.5534 | -50.446499 | 2026-09-15 00:02:00 | METOP-B | NOVO REPARTIMENTO | PARÁ | Brasil | 1505064 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| e97c80af-5565-3e0c-863a-e83ec3a5c42b | -13.5458 | -43.504299 | 2026-09-15 00:02:00 | METOP-B | SERRA DO RAMALHO | BAHIA | Brasil | 2930154 | 29 | 33 | nan | nan | nan | Cerrado | nan |
| 474828c4-58e3-3e67-a823-9282e8278d9e | -14.2247 | -47.399502 | 2026-09-15 00:02:00 | METOP-B | SÃO JOÃO D'ALIANÇA | GOIÁS | Brasil | 5220009 | 52 | 33 | nan | nan | nan | Cerrado | nan |
| c043547a-118d-3c40-acd9-0f3ac68fd92a | -17.472401 | -43.652302 | 2026-09-15 00:02:00 | METOP-B | OLHOS-D'ÁGUA | MINAS GERAIS | Brasil | 3145455 | 31 | 33 | nan | nan | nan | Cerrado | nan |
| 26f6d03f-6bec-3b58-8231-efb4659ae35b | -10.5865 | -47.7327 | 2026-09-15 00:02:00 | METOP-B | PONTE ALTA DO TOCANTINS | TOCANTINS | Brasil | 1717909 | 17 | 33 | nan | nan | nan | Cerrado | nan |
| c65fec27-bdd5-3b47-8b46-9e97f2bb5f8c | -2.9334 | -50.380299 | 2026-09-15 00:02:00 | METOP-B | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| ed20bac5-84a7-3f26-a077-70d5f2e20208 | -9.3103 | -44.3326 | 2026-09-15 00:02:00 | METOP-B | BOM JESUS | PIAUÍ | Brasil | 2201903 | 22 | 33 | nan | nan | nan | Cerrado | nan |
| c1d999df-ca4a-354d-9558-0ef6cd6ceaef | -5.4208 | -43.973 | 2026-09-15 00:02:00 | METOP-B | GOVERNADOR EUGÊNIO BARROS | MARANHÃO | Brasil | 2104602 | 21 | 33 | nan | nan | nan | Cerrado | nan |
| 7b837dfa-1c2d-3d8e-8814-98f77eb500e6 | -5.0738 | -56.197201 | 2026-09-15 00:02:00 | METOP-B | TRAIRÃO | PARÁ | Brasil | 1508050 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| 75320edf-da01-3c77-9704-313def7c79ad | -12.7873 | -47.5467 | 2026-09-15 00:02:00 | METOP-B | PARANÃ | TOCANTINS | Brasil | 1716208 | 17 | 33 | nan | nan | nan | Cerrado | nan |
| 19fc7228-98d2-3e04-9160-798c84cd113a | -6.724 | -48.091202 | 2026-09-15 00:02:00 | METOP-B | WANDERLÂNDIA | TOCANTINS | Brasil | 1722081 | 17 | 33 | nan | nan | nan | Amazônia | nan |
| d44c0186-1e48-3070-b8bc-ef464eaa3e78 | -6.8492 | -55.5107 | 2026-09-15 00:02:00 | METOP-B | NOVO PROGRESSO | PARÁ | Brasil | 1505031 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| 68a0ddd6-d25b-3a9a-9f90-a0df00ea56d0 | -6.7255 | -48.098099 | 2026-09-15 00:02:00 | METOP-B | WANDERLÂNDIA | TOCANTINS | Brasil | 1722081 | 17 | 33 | nan | nan | nan | Amazônia | nan |
| fbac43c2-ccbb-384f-9a62-32bb89433f99 | -8.374 | -54.684898 | 2026-09-15 00:02:00 | METOP-B | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| dbd90e83-f729-3e8c-a462-ba2cbe2916c7 | -15.5011 | -48.534698 | 2026-09-15 00:02:00 | METOP-B | PADRE BERNARDO | GOIÁS | Brasil | 5215603 | 52 | 33 | nan | nan | nan | Cerrado | nan |
| 071a9752-e2b7-368e-a3b9-9051d91d3923 | -13.2273 | -51.646801 | 2026-09-15 00:02:00 | METOP-B | RIBEIRÃO CASCALHEIRA | MATO GROSSO | Brasil | 5107180 | 51 | 33 | nan | nan | nan | Cerrado | nan |
| 3793868c-3f20-3ceb-98b5-994d2d15fbad | -7.9265 | -49.708302 | 2026-09-15 00:02:00 | METOP-B | CONCEIÇÃO DO ARAGUAIA | PARÁ | Brasil | 1502707 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| 38b60267-a028-3645-9e7d-5f0756da8f93 | -9.4595 | -48.5457 | 2026-09-15 00:02:00 | METOP-B | MIRACEMA DO TOCANTINS | TOCANTINS | Brasil | 1713205 | 17 | 33 | nan | nan | nan | Cerrado | nan |
| 371292f5-8a69-3925-8adc-f3d887b0229f | -6.0501 | -52.159599 | 2026-09-15 00:02:00 | METOP-B | SÃO FÉLIX DO XINGU | PARÁ | Brasil | 1507300 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| b5e3d06b-06d6-34ef-ab25-0e5f4a5681e4 | -11.1697 | -42.799999 | 2026-09-15 00:02:00 | METOP-B | GENTIO DO OURO | BAHIA | Brasil | 2911303 | 29 | 33 | nan | nan | nan | Caatinga | nan |
| 23f61757-9ff5-3e71-8790-8e7cc2d4b5a3 | -6.317 | -44.103298 | 2026-09-15 00:02:00 | METOP-B | COLINAS | MARANHÃO | Brasil | 2103505 | 21 | 33 | nan | nan | nan | Cerrado | nan |
| f391488d-c66e-337a-a681-865b55356839 | -14.8627 | -48.128799 | 2026-09-15 00:02:00 | METOP-B | MIMOSO DE GOIÁS | GOIÁS | Brasil | 5213053 | 52 | 33 | nan | nan | nan | Cerrado | nan |
| 34adfd67-4873-3620-b1d8-d8b5970c31b6 | -4.3038 | -49.100399 | 2026-09-15 00:02:00 | METOP-B | GOIANÉSIA DO PARÁ | PARÁ | Brasil | 1503093 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| d31845ed-1fcd-3818-a591-4caf028f6be3 | -4.5182 | -54.946899 | 2026-09-15 00:02:00 | METOP-B | RURÓPOLIS | PARÁ | Brasil | 1506195 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| 220c286e-76f5-3c38-8a32-d9b9943faef0 | -18.8281 | -44.501999 | 2026-09-15 00:02:00 | METOP-B | CURVELO | MINAS GERAIS | Brasil | 3120904 | 31 | 33 | nan | nan | nan | Cerrado | nan |
| 2e04f332-8005-3bc9-86b2-c09f01e54eb6 | -5.5975 | -43.5382 | 2026-09-15 00:02:00 | METOP-B | PARNARAMA | MARANHÃO | Brasil | 2107803 | 21 | 33 | nan | nan | nan | Cerrado | nan |
| df7c20f8-6f14-3251-903f-a2634b0eac0f | -9.3678 | -50.152302 | 2026-09-15 00:02:00 | METOP-B | SANTANA DO ARAGUAIA | PARÁ | Brasil | 1506708 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| 79c112e1-b418-3534-a2a5-4fcbb8542ed9 | -15.2768 | -42.779202 | 2026-09-15 00:02:00 | METOP-B | SANTO ANTÔNIO DO RETIRO | MINAS GERAIS | Brasil | 3160454 | 31 | 33 | nan | nan | nan | Cerrado | nan |
| 122f8f99-576c-3ad5-8ac1-1ed934edc9d2 | -5.9355 | -53.519501 | 2026-09-15 00:02:00 | METOP-B | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| 4a499a3c-7fee-32cc-8d66-52072a455a86 | -2.9106 | -50.416199 | 2026-09-15 00:02:00 | METOP-B | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| 141a9fdf-c2f5-34fd-bf27-a26a4b98f3db | -9.4257 | -50.087898 | 2026-09-15 00:02:00 | METOP-B | SANTANA DO ARAGUAIA | PARÁ | Brasil | 1506708 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| b066df96-080b-3e0d-89d2-4520d4ef89e8 | -15.5416 | -48.7794 | 2026-09-15 00:02:00 | METOP-B | COCALZINHO DE GOIÁS | GOIÁS | Brasil | 5205513 | 52 | 33 | nan | nan | nan | Cerrado | nan |
| 90b34999-1fc5-3e17-9992-6f92b6e3e025 | -12.4931 | -44.6203 | 2026-09-15 00:02:00 | METOP-B | BAIANÓPOLIS | BAHIA | Brasil | 2902500 | 29 | 33 | nan | nan | nan | Cerrado | nan |
| 5ab2a105-e292-3708-8b0c-95a5dee10b1e | -9.8851 | -47.7715 | 2026-09-15 00:02:00 | METOP-B | RIO SONO | TOCANTINS | Brasil | 1718758 | 17 | 33 | nan | nan | nan | Cerrado | nan |
| 3d50dd4a-203c-34ab-9758-59b62da77e1c | -11.8698 | -43.800201 | 2026-09-15 00:02:00 | METOP-B | WANDERLEY | BAHIA | Brasil | 2933455 | 29 | 33 | nan | nan | nan | Cerrado | nan |
| bea2a77a-4fcf-3e9d-823d-9114ac2e98d5 | -6.7764 | -48.647701 | 2026-09-15 00:02:00 | METOP-B | ARAGUANÃ | TOCANTINS | Brasil | 1702158 | 17 | 33 | nan | nan | nan | Amazônia | nan |
| ab7c3b11-3e25-371e-83b3-54b6c9e8587d | -12.4742 | -41.390598 | 2026-09-15 00:02:00 | METOP-B | LENÇÓIS | BAHIA | Brasil | 2919306 | 29 | 33 | nan | nan | nan | Caatinga | nan |
| 9d5a1935-daab-3614-b85c-2a703f596af4 | -9.0217 | -47.730202 | 2026-09-15 00:02:00 | METOP-B | BOM JESUS DO TOCANTINS | TOCANTINS | Brasil | 1703305 | 17 | 33 | nan | nan | nan | Cerrado | nan |
| e067c1ef-5e65-3b82-9209-6854d7bcf711 | -7.7409 | -49.518501 | 2026-09-15 00:02:00 | METOP-B | FLORESTA DO ARAGUAIA | PARÁ | Brasil | 1503044 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| 13e64fa6-7416-3747-9434-45c3a07120cf | -5.9231 | -53.509899 | 2026-09-15 00:02:00 | METOP-B | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| fae49595-dda5-348c-885b-9cd6fb8c5688 | -9.4181 | -47.8466 | 2026-09-15 00:02:00 | METOP-B | RIO SONO | TOCANTINS | Brasil | 1718758 | 17 | 33 | nan | nan | nan | Cerrado | nan |
| bc7d2729-6920-3d42-9028-105cf374b12b | -5.7284 | -43.261002 | 2026-09-15 00:02:00 | METOP-B | PARNARAMA | MARANHÃO | Brasil | 2107803 | 21 | 33 | nan | nan | nan | Cerrado | nan |
| 0410bc0e-0c8f-3348-acfa-69db4b189da9 | -9.3598 | -50.067699 | 2026-09-15 00:02:00 | METOP-B | SANTANA DO ARAGUAIA | PARÁ | Brasil | 1506708 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| f4ee06ba-8fb3-3188-9786-9bc82c77b88f | -10.6786 | -54.136299 | 2026-09-15 00:02:00 | METOP-B | MARCELÂNDIA | MATO GROSSO | Brasil | 5105580 | 51 | 33 | nan | nan | nan | Amazônia | nan |
| 61444b94-4c15-30c6-858a-12358de06c34 | -6.7173 | -48.107101 | 2026-09-15 00:02:00 | METOP-B | WANDERLÂNDIA | TOCANTINS | Brasil | 1722081 | 17 | 33 | nan | nan | nan | Amazônia | nan |
| 5ce0209b-4513-329d-b5c9-471b950ead35 | -14.8611 | -48.120998 | 2026-09-15 00:02:00 | METOP-B | MIMOSO DE GOIÁS | GOIÁS | Brasil | 5213053 | 52 | 33 | nan | nan | nan | Cerrado | nan |
| f577213e-e949-3312-b91c-688291a7810a | -1.7795 | -54.451698 | 2026-09-15 00:02:00 | METOP-B | ALENQUER | PARÁ | Brasil | 1500404 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| 28f1a57a-7c92-30e8-98ca-a370e188c6da | -2.891 | -50.420502 | 2026-09-15 00:02:00 | METOP-B | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| 6afda3b3-12f4-30ac-979c-166c72715763 | -5.8587 | -52.081001 | 2026-09-15 00:02:00 | METOP-B | SÃO FÉLIX DO XINGU | PARÁ | Brasil | 1507300 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| 5e4b2f00-5198-3adf-8abe-ee90e72f8a78 | -11.813 | -46.580601 | 2026-09-15 00:02:00 | METOP-B | NOVO JARDIM | TOCANTINS | Brasil | 1715259 | 17 | 33 | nan | nan | nan | Cerrado | nan |
| 7c343f17-8f6e-3103-9cc9-2ca93c3f43a7 | -14.9563 | -47.507099 | 2026-09-15 00:02:00 | METOP-B | FORMOSA | GOIÁS | Brasil | 5208004 | 52 | 33 | nan | nan | nan | Cerrado | nan |
| a9811f0a-0c10-3739-9e5c-f4a0582b8b49 | -16.8643 | -50.122898 | 2026-09-15 00:02:00 | METOP-B | PALMINÓPOLIS | GOIÁS | Brasil | 5215900 | 52 | 33 | nan | nan | nan | Cerrado | nan |
| 6cba8c34-78bf-33ec-9c4e-21851c441b8f | -4.7656 | -42.713902 | 2026-09-15 00:02:00 | METOP-B | JOSÉ DE FREITAS | PIAUÍ | Brasil | 2205508 | 22 | 33 | nan | nan | nan | Cerrado | nan |
| 4c1180e8-dca6-3e39-a5b1-19b92c9f2b3b | -9.3607 | -50.119301 | 2026-09-15 00:02:00 | METOP-B | SANTANA DO ARAGUAIA | PARÁ | Brasil | 1506708 | 15 | 33 | nan | nan | nan | Amazônia | nan |


[Clique aqui para ver as próximas entradas](README7.md)
