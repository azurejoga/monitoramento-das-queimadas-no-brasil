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

## Dados Diários - Página 3

| ID | Latitude | Longitude | Data/Hora GMT | Satélite | Município | Estado | País | Município ID | Estado ID | País ID | Dias sem Chuva | Precipitação | Risco de Fogo | Bioma | FRP |
|----|----------|-----------|---------------|----------|-----------|--------|------|--------------|-----------|---------|----------------|--------------|----------------|-------|-----|
| 6c361f1b-cb68-3596-9451-bd1745cfdc6c | -3.8945 | -42.547199 | 2024-12-12 00:12:00 | METOP-C | CAMPO LARGO DO PIAUÍ | PIAUÍ | Brasil | 2202174 | 22 | 33 | nan | nan | nan | Caatinga | nan |
| afb7b601-ee10-3152-ace7-16e2d6b5252d | -4.8972 | -38.7411 | 2024-12-12 00:12:00 | METOP-C | IBARETAMA | CEARÁ | Brasil | 2305266 | 23 | 33 | nan | nan | nan | Caatinga | nan |
| 933d1bf8-f123-3516-82f1-5c6fdea74be1 | -6.9136 | -43.520901 | 2024-12-12 00:12:00 | METOP-C | JERUMENHA | PIAUÍ | Brasil | 2205300 | 22 | 33 | nan | nan | nan | Cerrado | nan |
| 5c41dc66-0e2d-3b56-8d10-3c7aac51c317 | -5.8216 | -39.211201 | 2024-12-12 00:12:00 | METOP-C | DEPUTADO IRAPUAN PINHEIRO | CEARÁ | Brasil | 2304269 | 23 | 33 | nan | nan | nan | Caatinga | nan |
| cb923fca-5ac3-38db-bab1-61e8429ef60c | -6.9346 | -43.5168 | 2024-12-12 00:20:00 | GOES-16 | JERUMENHA | PIAUÍ | Brasil | 2205300 | 22 | 33 | nan | nan | nan | Cerrado | 325.8 |
| 363963f2-0453-3ef2-b175-f062df0ba69b | -12.5682 | -57.7579 | 2024-12-12 00:20:00 | GOES-16 | BRASNORTE | MATO GROSSO | Brasil | 5101902 | 51 | 33 | nan | nan | nan | Amazônia | 54.2 |
| f4755e13-60e9-371f-bb6f-560688927f33 | -14.7655 | -52.6446 | 2024-12-12 00:20:00 | GOES-16 | NOVA XAVANTINA | MATO GROSSO | Brasil | 5106257 | 51 | 33 | nan | nan | nan | Cerrado | 82.8 |
| 988f2564-ef5f-31cc-a462-6e082e0329b2 | -5.9185 | -48.0449 | 2024-12-12 00:20:00 | GOES-16 | SÃO BENTO DO TOCANTINS | TOCANTINS | Brasil | 1720101 | 17 | 33 | nan | nan | nan | Cerrado | 80.4 |
| 5401800f-bc19-3157-ae46-142cac8e88a8 | -5.9371 | -48.0437 | 2024-12-12 00:20:00 | GOES-16 | SÃO BENTO DO TOCANTINS | TOCANTINS | Brasil | 1720101 | 17 | 33 | nan | nan | nan | Cerrado | 178.2 |
| d8e0fb99-5c9b-351c-8223-3f67a57ca3e4 | -11.2148 | -53.833 | 2024-12-12 00:20:00 | GOES-16 | MARCELÂNDIA | MATO GROSSO | Brasil | 5105580 | 51 | 33 | nan | nan | nan | Amazônia | 81.7 |
| fe360902-d7ce-3cf5-af9a-ea34a52f8e2e | -14.7461 | -52.6471 | 2024-12-12 00:20:00 | GOES-16 | NOVA XAVANTINA | MATO GROSSO | Brasil | 5106257 | 51 | 33 | nan | nan | nan | Cerrado | 132.6 |
| 1647feab-8954-3cb4-963f-9ba13c65748a | -14.7465 | -52.6259 | 2024-12-12 00:20:00 | GOES-16 | NOVA XAVANTINA | MATO GROSSO | Brasil | 5106257 | 51 | 33 | nan | nan | nan | Cerrado | 61.0 |
| fb533ebb-bb13-3109-a6a4-1f99b2568a08 | -4.8085 | -44.5554 | 2024-12-12 00:20:00 | GOES-16 | SANTO ANTÔNIO DOS LOPES | MARANHÃO | Brasil | 2110302 | 21 | 33 | nan | nan | nan | Cerrado | 81.4 |
| e8d75adf-5901-365b-804e-9bcf0d48bcd6 | -6.9158 | -43.5185 | 2024-12-12 00:20:00 | GOES-16 | JERUMENHA | PIAUÍ | Brasil | 2205300 | 22 | 33 | nan | nan | nan | Cerrado | 299.5 |
| 39b2adac-ef50-32cb-b645-acd7d73e9747 | -2.267 | -53.4799 | 2024-12-12 00:20:00 | GOES-16 | PRAINHA | PARÁ | Brasil | 1506005 | 15 | 33 | nan | nan | nan | Amazônia | 52.1 |
| dc13f799-fff6-3bf3-bbed-6a361800095c | -6.9156 | -43.5418 | 2024-12-12 00:20:00 | GOES-16 | JERUMENHA | PIAUÍ | Brasil | 2205300 | 22 | 33 | nan | nan | nan | Cerrado | 143.4 |
| c5976a33-5a5f-36d0-ab72-97d3d12ae1af | -5.9183 | -48.0667 | 2024-12-12 00:20:00 | GOES-16 | SÃO BENTO DO TOCANTINS | TOCANTINS | Brasil | 1720101 | 17 | 33 | nan | nan | nan | Cerrado | 37.4 |
| 476181f8-7a1a-3928-9d16-0e70ab520864 | -3.2502 | -46.8929 | 2024-12-12 00:20:00 | GOES-16 | PARAGOMINAS | PARÁ | Brasil | 1505502 | 15 | 33 | nan | nan | nan | Amazônia | 47.1 |
| cf5a4fd3-1dcf-35db-b638-5e0aceab775d | -6.9344 | -43.5401 | 2024-12-12 00:20:00 | GOES-16 | JERUMENHA | PIAUÍ | Brasil | 2205300 | 22 | 33 | nan | nan | nan | Cerrado | 183.4 |
| 88395f7c-b14b-3a17-842b-50e19a6d3ca3 | -14.7457 | -52.6683 | 2024-12-12 00:20:00 | GOES-16 | NOVA XAVANTINA | MATO GROSSO | Brasil | 5106257 | 51 | 33 | nan | nan | nan | Cerrado | 65.2 |
| 15345abd-5239-3dba-80d5-e5f664a7dc2b | -11.1959 | -53.8348 | 2024-12-12 00:20:00 | GOES-16 | MARCELÂNDIA | MATO GROSSO | Brasil | 5105580 | 51 | 33 | nan | nan | nan | Amazônia | 68.4 |
| 4e2f450e-a659-3ca7-b4da-f5340c6f93b1 | -5.9369 | -48.0654 | 2024-12-12 00:20:00 | GOES-16 | SÃO BENTO DO TOCANTINS | TOCANTINS | Brasil | 1720101 | 17 | 33 | nan | nan | nan | Cerrado | 55.2 |
| 7d1c5739-3c26-3f2c-ad69-24019ce47bcb | -6.9156 | -43.5418 | 2024-12-12 00:30:00 | GOES-16 | JERUMENHA | PIAUÍ | Brasil | 2205300 | 22 | 33 | nan | nan | nan | Cerrado | 118.6 |
| 1d7f9e18-f59e-36a3-ab58-5726a8c8054d | -5.9183 | -48.0667 | 2024-12-12 00:30:00 | GOES-16 | SÃO BENTO DO TOCANTINS | TOCANTINS | Brasil | 1720101 | 17 | 33 | nan | nan | nan | Cerrado | 56.2 |
| 27ee6b6c-68b3-3ff1-883f-faa4898dde23 | -4.8085 | -44.5554 | 2024-12-12 00:30:00 | GOES-16 | SANTO ANTÔNIO DOS LOPES | MARANHÃO | Brasil | 2110302 | 21 | 33 | nan | nan | nan | Cerrado | 86.2 |
| 7201eb60-36c3-3fc7-b1af-dd7b2e920013 | -6.9349 | -43.4934 | 2024-12-12 00:30:00 | GOES-16 | JERUMENHA | PIAUÍ | Brasil | 2205300 | 22 | 33 | nan | nan | nan | Cerrado | 74.2 |
| 8b3ae4d5-73fc-3239-8e40-c6ea8ef971f5 | -6.9158 | -43.5185 | 2024-12-12 00:30:00 | GOES-16 | JERUMENHA | PIAUÍ | Brasil | 2205300 | 22 | 33 | nan | nan | nan | Cerrado | 238.3 |
| 3916568f-a783-311d-82a4-a3fb2fc384e7 | -18.0464 | -52.9582 | 2024-12-12 00:30:00 | GOES-16 | MINEIROS | GOIÁS | Brasil | 5213103 | 52 | 33 | nan | nan | nan | Cerrado | 125.3 |
| bd3b16ab-5192-3fd0-9c91-7e0859a44de4 | -4.8083 | -44.5783 | 2024-12-12 00:30:00 | GOES-16 | SANTO ANTÔNIO DOS LOPES | MARANHÃO | Brasil | 2110302 | 21 | 33 | nan | nan | nan | Cerrado | 63.4 |
| 6e4f8004-8b41-3e27-8158-211e0b8d4108 | -14.7655 | -52.6446 | 2024-12-12 00:30:00 | GOES-16 | NOVA XAVANTINA | MATO GROSSO | Brasil | 5106257 | 51 | 33 | nan | nan | nan | Cerrado | 93.6 |
| 420445f1-d5d0-3c2b-b0f7-8aa22fb404e3 | -18.0663 | -52.955 | 2024-12-12 00:30:00 | GOES-16 | MINEIROS | GOIÁS | Brasil | 5213103 | 52 | 33 | nan | nan | nan | Cerrado | 59.1 |
| dd6b9d09-507d-3f17-9f99-e11c3a09aea8 | -5.9185 | -48.0449 | 2024-12-12 00:30:00 | GOES-16 | SÃO BENTO DO TOCANTINS | TOCANTINS | Brasil | 1720101 | 17 | 33 | nan | nan | nan | Cerrado | 116.9 |
| a698678d-8afe-3a66-adca-490760ba143a | -18.0469 | -52.9366 | 2024-12-12 00:30:00 | GOES-16 | MINEIROS | GOIÁS | Brasil | 5213103 | 52 | 33 | nan | nan | nan | Cerrado | 70.1 |
| 90465988-0efe-3ec2-8753-31709a5d480a | -15.0867 | -59.6288 | 2024-12-12 00:30:00 | GOES-16 | VILA BELA DA SANTÍSSIMA TRINDADE | MATO GROSSO | Brasil | 5105507 | 51 | 33 | nan | nan | nan | Amazônia | 53.7 |
| c3ee98a6-690d-34d6-a4c2-a50c649877a5 | -6.9346 | -43.5168 | 2024-12-12 00:30:00 | GOES-16 | JERUMENHA | PIAUÍ | Brasil | 2205300 | 22 | 33 | nan | nan | nan | Cerrado | 311.2 |
| 55155aac-68d4-3c49-8af4-91bcd662bf7f | -5.9369 | -48.0654 | 2024-12-12 00:30:00 | GOES-16 | SÃO BENTO DO TOCANTINS | TOCANTINS | Brasil | 1720101 | 17 | 33 | nan | nan | nan | Cerrado | 79.7 |
| 065ccb0c-d397-3953-879a-65fced942e15 | -11.2148 | -53.833 | 2024-12-12 00:30:00 | GOES-16 | MARCELÂNDIA | MATO GROSSO | Brasil | 5105580 | 51 | 33 | nan | nan | nan | Amazônia | 90.0 |
| 8ada609e-36d1-3b9f-8bb4-e402838e48ad | -12.5682 | -57.7579 | 2024-12-12 00:30:00 | GOES-16 | BRASNORTE | MATO GROSSO | Brasil | 5101902 | 51 | 33 | nan | nan | nan | Amazônia | 55.9 |
| 1ae6f07b-ac7d-3c81-b7d2-062f03d83fe1 | -6.9161 | -43.4952 | 2024-12-12 00:30:00 | GOES-16 | JERUMENHA | PIAUÍ | Brasil | 2205300 | 22 | 33 | nan | nan | nan | Cerrado | 70.1 |
| 9976bccd-e24a-314d-bd6e-55591cb8ff0b | -5.9371 | -48.0437 | 2024-12-12 00:30:00 | GOES-16 | SÃO BENTO DO TOCANTINS | TOCANTINS | Brasil | 1720101 | 17 | 33 | nan | nan | nan | Cerrado | 161.8 |
| 105daaa9-a967-3ef1-9098-e0b0ecb46bf7 | -18.046 | -52.9798 | 2024-12-12 00:30:00 | GOES-16 | MINEIROS | GOIÁS | Brasil | 5213103 | 52 | 33 | nan | nan | nan | Cerrado | 60.2 |
| ba1890aa-495c-39cd-b875-583a9f117e9a | -14.7461 | -52.6471 | 2024-12-12 00:30:00 | GOES-16 | NOVA XAVANTINA | MATO GROSSO | Brasil | 5106257 | 51 | 33 | nan | nan | nan | Cerrado | 111.4 |
| 42702f80-57dd-3c99-9b58-ac7c3f535c3d | -14.7457 | -52.6683 | 2024-12-12 00:30:00 | GOES-16 | NOVA XAVANTINA | MATO GROSSO | Brasil | 5106257 | 51 | 33 | nan | nan | nan | Cerrado | 62.3 |
| 96f0027c-bc49-31e0-89f9-df708e8785f4 | -6.9344 | -43.5401 | 2024-12-12 00:30:00 | GOES-16 | JERUMENHA | PIAUÍ | Brasil | 2205300 | 22 | 33 | nan | nan | nan | Cerrado | 184.9 |
| a1cead19-1ae4-3f01-80e2-a35338208bcf | -15.0865 | -59.6487 | 2024-12-12 00:40:00 | GOES-16 | VILA BELA DA SANTÍSSIMA TRINDADE | MATO GROSSO | Brasil | 5105507 | 51 | 33 | nan | nan | nan | Amazônia | 54.5 |
| 3f4944b7-fe6f-32ea-9d95-deb8cc7b1f7e | -18.0464 | -52.9582 | 2024-12-12 00:40:00 | GOES-16 | MINEIROS | GOIÁS | Brasil | 5213103 | 52 | 33 | nan | nan | nan | Cerrado | 236.8 |
| b5ca3b25-9c15-3ed2-9a59-c75dca1f2e07 | -14.7655 | -52.6446 | 2024-12-12 00:40:00 | GOES-16 | NOVA XAVANTINA | MATO GROSSO | Brasil | 5106257 | 51 | 33 | nan | nan | nan | Cerrado | 94.3 |
| f1e3c6e9-9661-3d7c-807e-71b767516705 | -6.9346 | -43.5168 | 2024-12-12 00:40:00 | GOES-16 | JERUMENHA | PIAUÍ | Brasil | 2205300 | 22 | 33 | nan | nan | nan | Cerrado | 260.1 |
| ede656d8-e65d-3187-bd0c-75809d4d7e92 | -5.1648 | -44.3727 | 2024-12-12 00:40:00 | GOES-16 | PRESIDENTE DUTRA | MARANHÃO | Brasil | 2109106 | 21 | 33 | nan | nan | nan | Cerrado | 81.3 |
| d33457ec-9769-30c8-9ac0-792ee275c33c | -18.0469 | -52.9366 | 2024-12-12 00:40:00 | GOES-16 | MINEIROS | GOIÁS | Brasil | 5213103 | 52 | 33 | nan | nan | nan | Cerrado | 110.2 |
| 8c08da36-1896-3f2f-ad02-129a5294a677 | -14.7457 | -52.6683 | 2024-12-12 00:40:00 | GOES-16 | NOVA XAVANTINA | MATO GROSSO | Brasil | 5106257 | 51 | 33 | nan | nan | nan | Cerrado | 61.2 |
| d8a05938-574f-3d49-babf-a7a709b6ebda | -6.9344 | -43.5401 | 2024-12-12 00:40:00 | GOES-16 | JERUMENHA | PIAUÍ | Brasil | 2205300 | 22 | 33 | nan | nan | nan | Cerrado | 176.3 |
| 08bb7947-727a-3c33-a34d-db025156863a | -5.9183 | -48.0667 | 2024-12-12 00:40:00 | GOES-16 | SÃO BENTO DO TOCANTINS | TOCANTINS | Brasil | 1720101 | 17 | 33 | nan | nan | nan | Cerrado | 55.0 |
| 1254c071-1c36-33d4-9d8a-bc627bb00e9d | -18.0663 | -52.955 | 2024-12-12 00:40:00 | GOES-16 | MINEIROS | GOIÁS | Brasil | 5213103 | 52 | 33 | nan | nan | nan | Cerrado | 96.6 |
| 71ce24d0-c19a-3c89-bb94-a529f2cf3674 | -5.9371 | -48.0437 | 2024-12-12 00:40:00 | GOES-16 | SÃO BENTO DO TOCANTINS | TOCANTINS | Brasil | 1720101 | 17 | 33 | nan | nan | nan | Cerrado | 177.0 |
| eaf3fad3-0041-383e-84e9-064a09928192 | -5.9369 | -48.0654 | 2024-12-12 00:40:00 | GOES-16 | SÃO BENTO DO TOCANTINS | TOCANTINS | Brasil | 1720101 | 17 | 33 | nan | nan | nan | Cerrado | 65.1 |
| f098e8ba-0959-395d-896f-25f6464b88ce | -14.7461 | -52.6471 | 2024-12-12 00:40:00 | GOES-16 | NOVA XAVANTINA | MATO GROSSO | Brasil | 5106257 | 51 | 33 | nan | nan | nan | Cerrado | 112.3 |
| 5d998ccd-7e7c-3c96-a2af-736b554a8fe2 | -18.046 | -52.9798 | 2024-12-12 00:40:00 | GOES-16 | MINEIROS | GOIÁS | Brasil | 5213103 | 52 | 33 | nan | nan | nan | Cerrado | 151.4 |
| 276ec5d9-387e-34dc-ac68-3743ccbd3149 | -15.0867 | -59.6288 | 2024-12-12 00:40:00 | GOES-16 | VILA BELA DA SANTÍSSIMA TRINDADE | MATO GROSSO | Brasil | 5105507 | 51 | 33 | nan | nan | nan | Amazônia | 61.1 |
| 5f4e8e46-90df-32e5-af9a-168d8daa9570 | -6.9161 | -43.4952 | 2024-12-12 00:40:00 | GOES-16 | JERUMENHA | PIAUÍ | Brasil | 2205300 | 22 | 33 | nan | nan | nan | Cerrado | 87.9 |
| 2a97d5c3-c679-354b-80c4-ba21f1b249bb | -18.0668 | -52.9335 | 2024-12-12 00:40:00 | GOES-16 | MINEIROS | GOIÁS | Brasil | 5213103 | 52 | 33 | nan | nan | nan | Cerrado | 58.3 |
| 58c1ca54-143d-3eeb-a702-348210314b83 | -11.1959 | -53.8348 | 2024-12-12 00:40:00 | GOES-16 | MARCELÂNDIA | MATO GROSSO | Brasil | 5105580 | 51 | 33 | nan | nan | nan | Amazônia | 67.7 |
| 89530a14-59fd-33cb-b57d-599f2667effa | -11.2148 | -53.833 | 2024-12-12 00:40:00 | GOES-16 | MARCELÂNDIA | MATO GROSSO | Brasil | 5105580 | 51 | 33 | nan | nan | nan | Amazônia | 83.0 |
| 8f796198-1561-379f-95cd-21efc4388c43 | -4.8085 | -44.5554 | 2024-12-12 00:40:00 | GOES-16 | SANTO ANTÔNIO DOS LOPES | MARANHÃO | Brasil | 2110302 | 21 | 33 | nan | nan | nan | Cerrado | 76.9 |
| 8c3c1f27-df89-39b4-a038-70e98a361172 | -6.9156 | -43.5418 | 2024-12-12 00:40:00 | GOES-16 | JERUMENHA | PIAUÍ | Brasil | 2205300 | 22 | 33 | nan | nan | nan | Cerrado | 118.0 |
| 6299174c-6904-3254-8938-62284332cce1 | -6.9158 | -43.5185 | 2024-12-12 00:40:00 | GOES-16 | JERUMENHA | PIAUÍ | Brasil | 2205300 | 22 | 33 | nan | nan | nan | Cerrado | 341.4 |
| 28a9227e-9311-36eb-bc1e-e6867a286b20 | -5.9185 | -48.0449 | 2024-12-12 00:40:00 | GOES-16 | SÃO BENTO DO TOCANTINS | TOCANTINS | Brasil | 1720101 | 17 | 33 | nan | nan | nan | Cerrado | 143.7 |
| fc880f10-1c5c-35ed-9512-082967059e8d | -6.9158 | -43.5185 | 2024-12-12 00:50:00 | GOES-16 | JERUMENHA | PIAUÍ | Brasil | 2205300 | 22 | 33 | nan | nan | nan | Cerrado | 378.5 |
| 2d99ef1b-590d-30e9-abc3-0b3a09f0794c | -18.0469 | -52.9366 | 2024-12-12 00:50:00 | GOES-16 | MINEIROS | GOIÁS | Brasil | 5213103 | 52 | 33 | nan | nan | nan | Cerrado | 100.1 |
| 1acf628f-6dbb-34aa-9f57-f3881cc561a9 | -11.2148 | -53.833 | 2024-12-12 00:50:00 | GOES-16 | MARCELÂNDIA | MATO GROSSO | Brasil | 5105580 | 51 | 33 | nan | nan | nan | Amazônia | 80.1 |
| 0127d784-15e2-35f3-b90b-4c8830afea9b | -18.0464 | -52.9582 | 2024-12-12 00:50:00 | GOES-16 | MINEIROS | GOIÁS | Brasil | 5213103 | 52 | 33 | nan | nan | nan | Cerrado | 216.8 |
| d7bd3f18-8c9b-32a2-8673-3754713f359f | -6.9349 | -43.4934 | 2024-12-12 00:50:00 | GOES-16 | JERUMENHA | PIAUÍ | Brasil | 2205300 | 22 | 33 | nan | nan | nan | Cerrado | 76.1 |
| 5dc6c771-4e14-3a1f-819e-5ce15b676af8 | -15.0865 | -59.6487 | 2024-12-12 00:50:00 | GOES-16 | VILA BELA DA SANTÍSSIMA TRINDADE | MATO GROSSO | Brasil | 5105507 | 51 | 33 | nan | nan | nan | Amazônia | 53.5 |
| 1eb4edda-700c-3e31-8cc2-0e81e68b19ff | -14.7461 | -52.6471 | 2024-12-12 00:50:00 | GOES-16 | NOVA XAVANTINA | MATO GROSSO | Brasil | 5106257 | 51 | 33 | nan | nan | nan | Cerrado | 92.3 |
| 0720183e-0812-3210-b134-ee73bb3430a8 | -3.2317 | -46.8716 | 2024-12-12 00:50:00 | GOES-16 | PARAGOMINAS | PARÁ | Brasil | 1505502 | 15 | 33 | nan | nan | nan | Amazônia | 47.9 |
| 42a8dd4c-1a2a-30ee-9d67-386db6886773 | -5.9369 | -48.0654 | 2024-12-12 00:50:00 | GOES-16 | SÃO BENTO DO TOCANTINS | TOCANTINS | Brasil | 1720101 | 17 | 33 | nan | nan | nan | Cerrado | 76.5 |
| 4679a66d-c8ac-3947-8330-c207ff21c2b1 | -14.7457 | -52.6683 | 2024-12-12 00:50:00 | GOES-16 | NOVA XAVANTINA | MATO GROSSO | Brasil | 5106257 | 51 | 33 | nan | nan | nan | Cerrado | 57.0 |
| 82d29377-9cf9-3439-910c-06a4b44a6229 | -5.9185 | -48.0449 | 2024-12-12 00:50:00 | GOES-16 | SÃO BENTO DO TOCANTINS | TOCANTINS | Brasil | 1720101 | 17 | 33 | nan | nan | nan | Cerrado | 136.6 |
| 10bb4681-f68e-300c-9cbf-7a4e69ccfe0e | -14.7655 | -52.6446 | 2024-12-12 00:50:00 | GOES-16 | NOVA XAVANTINA | MATO GROSSO | Brasil | 5106257 | 51 | 33 | nan | nan | nan | Cerrado | 84.6 |
| ec4b973b-c1e0-345b-9482-cbc4aceb98e7 | -3.2502 | -46.8929 | 2024-12-12 00:50:00 | GOES-16 | PARAGOMINAS | PARÁ | Brasil | 1505502 | 15 | 33 | nan | nan | nan | Amazônia | 49.2 |
| f8ea42e5-130f-3e14-afa9-d9e101fb5ddc | -15.0867 | -59.6288 | 2024-12-12 00:50:00 | GOES-16 | VILA BELA DA SANTÍSSIMA TRINDADE | MATO GROSSO | Brasil | 5105507 | 51 | 33 | nan | nan | nan | Amazônia | 60.3 |
| 3827bc15-776b-38e3-baf7-9652ad00ff38 | -11.1959 | -53.8348 | 2024-12-12 00:50:00 | GOES-16 | MARCELÂNDIA | MATO GROSSO | Brasil | 5105580 | 51 | 33 | nan | nan | nan | Amazônia | 71.0 |
| 5aba0d96-e97a-3303-b972-441dbbb1387f | -18.0663 | -52.955 | 2024-12-12 00:50:00 | GOES-16 | MINEIROS | GOIÁS | Brasil | 5213103 | 52 | 33 | nan | nan | nan | Cerrado | 87.3 |
| 1f5b0ef2-871b-3bcc-b9e4-b2cf4f8cc119 | -3.2503 | -46.8709 | 2024-12-12 00:50:00 | GOES-16 | PARAGOMINAS | PARÁ | Brasil | 1505502 | 15 | 33 | nan | nan | nan | Amazônia | 52.9 |
| c3592e59-f036-3d5d-baa6-bc7498a04f9e | -5.9371 | -48.0437 | 2024-12-12 00:50:00 | GOES-16 | SÃO BENTO DO TOCANTINS | TOCANTINS | Brasil | 1720101 | 17 | 33 | nan | nan | nan | Cerrado | 189.2 |
| 77150da7-a0f0-326c-a4e7-ada1249ff6d9 | -6.9346 | -43.5168 | 2024-12-12 00:50:00 | GOES-16 | JERUMENHA | PIAUÍ | Brasil | 2205300 | 22 | 33 | nan | nan | nan | Cerrado | 274.7 |
| 5dfdd651-11d3-3793-bb2a-603093be968d | -6.9161 | -43.4952 | 2024-12-12 00:50:00 | GOES-16 | JERUMENHA | PIAUÍ | Brasil | 2205300 | 22 | 33 | nan | nan | nan | Cerrado | 107.3 |
| 2b011503-ecf2-3199-8c9e-405dd2bd03d3 | -5.9183 | -48.0667 | 2024-12-12 00:50:00 | GOES-16 | SÃO BENTO DO TOCANTINS | TOCANTINS | Brasil | 1720101 | 17 | 33 | nan | nan | nan | Cerrado | 59.3 |
| 2df6bd25-c025-3845-ae36-8d6870a99b77 | -5.1648 | -44.3727 | 2024-12-12 00:50:00 | GOES-16 | PRESIDENTE DUTRA | MARANHÃO | Brasil | 2109106 | 21 | 33 | nan | nan | nan | Cerrado | 96.0 |
| 779b50e8-2238-3c0b-8545-1a83cf7a38be | -6.9344 | -43.5401 | 2024-12-12 00:50:00 | GOES-16 | JERUMENHA | PIAUÍ | Brasil | 2205300 | 22 | 33 | nan | nan | nan | Cerrado | 159.1 |
| 17e7fb01-fc47-317a-9a87-1b78db15eedd | -18.046 | -52.9798 | 2024-12-12 00:50:00 | GOES-16 | MINEIROS | GOIÁS | Brasil | 5213103 | 52 | 33 | nan | nan | nan | Cerrado | 121.1 |
| 8cf24a35-2e7b-390d-af3e-bf317bf0080d | -6.9156 | -43.5418 | 2024-12-12 00:50:00 | GOES-16 | JERUMENHA | PIAUÍ | Brasil | 2205300 | 22 | 33 | nan | nan | nan | Cerrado | 124.3 |
| a3d4cca0-9909-38fd-b3a6-f3490ebe0b34 | -6.4821 | -43.570099 | 2024-12-12 00:50:00 | METOP-B | SUCUPIRA DO RIACHÃO | MARANHÃO | Brasil | 2111953 | 21 | 33 | nan | nan | nan | Cerrado | nan |
| ed50b252-8511-3056-8bad-0eb8a604b80b | -2.821 | -51.6035 | 2024-12-12 00:50:00 | METOP-B | ANAPU | PARÁ | Brasil | 1500859 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| a429cec1-9bfc-3890-983e-0a192c77bb0b | -1.9745 | -53.762199 | 2024-12-12 00:50:00 | METOP-B | PRAINHA | PARÁ | Brasil | 1506005 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| 51ceed87-1d2c-3e5c-9030-20f0f7f4430b | 2.9194 | -60.725399 | 2024-12-12 00:50:00 | METOP-B | BOA VISTA | RORAIMA | Brasil | 1400100 | 14 | 33 | nan | nan | nan | Amazônia | nan |
| f4785cb6-27c1-3176-8fba-bc3e2c3bb0f9 | -6.4987 | -43.5952 | 2024-12-12 00:50:00 | METOP-B | SÃO JOÃO DOS PATOS | MARANHÃO | Brasil | 2111102 | 21 | 33 | nan | nan | nan | Cerrado | nan |
| 1a59cd96-3db9-330b-811d-fcdc60328d11 | -1.9826 | -53.752602 | 2024-12-12 00:50:00 | METOP-B | PRAINHA | PARÁ | Brasil | 1506005 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| e9599d82-fe72-35f9-8c10-b28bde83e40f | -5.4917 | -48.105999 | 2024-12-12 00:50:00 | METOP-B | ARAGUATINS | TOCANTINS | Brasil | 1702208 | 17 | 33 | nan | nan | nan | Cerrado | nan |
| 601ea7b4-a922-3db5-a43e-bdf682801d81 | -6.5056 | -43.622601 | 2024-12-12 00:50:00 | METOP-B | SÃO JOÃO DOS PATOS | MARANHÃO | Brasil | 2111102 | 21 | 33 | nan | nan | nan | Cerrado | nan |


[Clique aqui para ver as próximas entradas](README4.md)
