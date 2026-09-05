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

## Dados Diários - Página 38

| ID | Latitude | Longitude | Data/Hora GMT | Satélite | Município | Estado | País | Município ID | Estado ID | País ID | Dias sem Chuva | Precipitação | Risco de Fogo | Bioma | FRP |
|----|----------|-----------|---------------|----------|-----------|--------|------|--------------|-----------|---------|----------------|--------------|----------------|-------|-----|
| 81a01be5-9ba7-3473-abba-5e3de803afe7 | -12.4328 | -43.275 | 2026-09-05 12:30:00 | GOES-19 | MUQUÉM DO SÃO FRANCISCO | BAHIA | Brasil | 2922250 | 29 | 33 | nan | nan | nan | Cerrado | 85.5 |
| 603f4cae-6b54-3f80-9c1c-f5e18e7a25ef | -3.5406 | -48.1889 | 2026-09-05 12:40:00 | GOES-19 | PARAGOMINAS | PARÁ | Brasil | 1505502 | 15 | 33 | nan | nan | nan | Amazônia | 311.3 |
| e5af1c55-9e00-37af-a20c-848b1b13b7f5 | -12.4328 | -43.275 | 2026-09-05 12:40:00 | GOES-19 | MUQUÉM DO SÃO FRANCISCO | BAHIA | Brasil | 2922250 | 29 | 33 | nan | nan | nan | Cerrado | 94.1 |
| da738b68-598a-3ba9-aa7e-14139009855e | -5.346 | -56.0454 | 2026-09-05 12:40:00 | GOES-19 | TRAIRÃO | PARÁ | Brasil | 1508050 | 15 | 33 | nan | nan | nan | Amazônia | 91.1 |
| 9705bb8f-2ced-3dcf-9877-0ae79736c133 | -3.5407 | -48.1673 | 2026-09-05 12:40:00 | GOES-19 | PARAGOMINAS | PARÁ | Brasil | 1505502 | 15 | 33 | nan | nan | nan | Amazônia | 101.3 |
| c27f4d69-281d-39ea-b7e1-77e7d98787bf | -5.3462 | -56.0256 | 2026-09-05 12:40:00 | GOES-19 | TRAIRÃO | PARÁ | Brasil | 1508050 | 15 | 33 | nan | nan | nan | Amazônia | 142.9 |
| e6042d39-c4cc-3c59-a64f-58f21d5c84be | -11.5388 | -44.8933 | 2026-09-05 12:40:00 | GOES-19 | RIACHÃO DAS NEVES | BAHIA | Brasil | 2926202 | 29 | 33 | nan | nan | nan | Cerrado | 67.5 |
| f99a893f-f0ff-3f9c-8d45-63edad8b7aea | -12.4522 | -43.2717 | 2026-09-05 12:50:00 | GOES-19 | MUQUÉM DO SÃO FRANCISCO | BAHIA | Brasil | 2922250 | 29 | 33 | nan | nan | nan | Cerrado | 72.6 |
| 7536d8c9-479c-3a82-880d-ebd3d50c5bc2 | -12.4328 | -43.275 | 2026-09-05 12:50:00 | GOES-19 | MUQUÉM DO SÃO FRANCISCO | BAHIA | Brasil | 2922250 | 29 | 33 | nan | nan | nan | Cerrado | 73.9 |
| b68a1c80-6edd-3e64-a745-351c3ff87090 | -5.3462 | -56.0256 | 2026-09-05 12:50:00 | GOES-19 | TRAIRÃO | PARÁ | Brasil | 1508050 | 15 | 33 | nan | nan | nan | Amazônia | 165.9 |
| 8efc8c2c-db81-3611-b6cc-077bffcb4b46 | -7.6968 | -44.3247 | 2026-09-05 12:50:00 | GOES-19 | URUÇUÍ | PIAUÍ | Brasil | 2211209 | 22 | 33 | nan | nan | nan | Cerrado | 106.4 |
| 06d915c6-e49b-3fbe-89e3-92f4e39d74ea | -3.5407 | -48.1673 | 2026-09-05 12:50:00 | GOES-19 | PARAGOMINAS | PARÁ | Brasil | 1505502 | 15 | 33 | nan | nan | nan | Amazônia | 130.8 |
| 6fd2305d-d59d-3ff7-8800-3a92814e09f8 | -3.5406 | -48.1889 | 2026-09-05 12:50:00 | GOES-19 | PARAGOMINAS | PARÁ | Brasil | 1505502 | 15 | 33 | nan | nan | nan | Amazônia | 313.9 |
| f762f204-e2c1-3572-81e3-294aa41ced02 | -5.346 | -56.0454 | 2026-09-05 12:50:00 | GOES-19 | TRAIRÃO | PARÁ | Brasil | 1508050 | 15 | 33 | nan | nan | nan | Amazônia | 118.5 |
| e96ce8df-98b4-3b24-945d-d651c3d9e216 | -11.5388 | -44.8933 | 2026-09-05 12:50:00 | GOES-19 | RIACHÃO DAS NEVES | BAHIA | Brasil | 2926202 | 29 | 33 | nan | nan | nan | Cerrado | 68.7 |
| 38818d44-fe65-361b-ac62-2a31709c76f1 | -10.9391 | -45.3457 | 2026-09-05 13:00:00 | GOES-19 | FORMOSA DO RIO PRETO | BAHIA | Brasil | 2911105 | 29 | 33 | nan | nan | nan | Cerrado | 78.3 |
| 864ccaec-86d8-306f-871e-1cd2de44917d | -3.5406 | -48.1889 | 2026-09-05 13:00:00 | GOES-19 | PARAGOMINAS | PARÁ | Brasil | 1505502 | 15 | 33 | nan | nan | nan | Amazônia | 306.1 |
| ffa3941d-fe95-3ad4-b0ff-17d71eb6c346 | -12.4328 | -43.275 | 2026-09-05 13:00:00 | GOES-19 | MUQUÉM DO SÃO FRANCISCO | BAHIA | Brasil | 2922250 | 29 | 33 | nan | nan | nan | Cerrado | 121.6 |
| 194deca6-de52-3772-8b45-f4ddda6a07b3 | -5.346 | -56.0454 | 2026-09-05 13:00:00 | GOES-19 | TRAIRÃO | PARÁ | Brasil | 1508050 | 15 | 33 | nan | nan | nan | Amazônia | 198.9 |
| 6ab382cb-2460-3598-9414-c8579f9d3bdf | -5.3462 | -56.0256 | 2026-09-05 13:00:00 | GOES-19 | TRAIRÃO | PARÁ | Brasil | 1508050 | 15 | 33 | nan | nan | nan | Amazônia | 214.4 |
| 2f08a605-98b4-352e-a940-f63df0373bed | -3.5407 | -48.1673 | 2026-09-05 13:00:00 | GOES-19 | PARAGOMINAS | PARÁ | Brasil | 1505502 | 15 | 33 | nan | nan | nan | Amazônia | 172.0 |
| 25492ac9-cc5f-37d4-96bc-bc625956e16f | -7.6968 | -44.3247 | 2026-09-05 13:00:00 | GOES-19 | URUÇUÍ | PIAUÍ | Brasil | 2211209 | 22 | 33 | nan | nan | nan | Cerrado | 95.2 |
| cffb9651-64d4-3c82-b817-391e92d1c28f | -5.3462 | -56.0256 | 2026-09-05 13:10:00 | GOES-19 | TRAIRÃO | PARÁ | Brasil | 1508050 | 15 | 33 | nan | nan | nan | Amazônia | 193.2 |
| ea1c73fb-3275-3800-aa1f-b1c548222e99 | -3.5406 | -48.1889 | 2026-09-05 13:10:00 | GOES-19 | PARAGOMINAS | PARÁ | Brasil | 1505502 | 15 | 33 | nan | nan | nan | Amazônia | 304.0 |
| 8f22da18-4413-35e8-be96-988d2e7489f5 | -3.5407 | -48.1673 | 2026-09-05 13:10:00 | GOES-19 | PARAGOMINAS | PARÁ | Brasil | 1505502 | 15 | 33 | nan | nan | nan | Amazônia | 123.5 |
| 38abb554-a545-3ff9-85ec-ec06d2423da6 | -12.4328 | -43.275 | 2026-09-05 13:10:00 | GOES-19 | MUQUÉM DO SÃO FRANCISCO | BAHIA | Brasil | 2922250 | 29 | 33 | nan | nan | nan | Cerrado | 106.8 |
| 30d3ca64-10b3-387c-ac0f-0317bc8f2169 | -5.346 | -56.0454 | 2026-09-05 13:10:00 | GOES-19 | TRAIRÃO | PARÁ | Brasil | 1508050 | 15 | 33 | nan | nan | nan | Amazônia | 167.5 |
| 15bd1db5-ea07-37b9-8a3c-b46fb8772c3c | -10.9391 | -45.3457 | 2026-09-05 13:10:00 | GOES-19 | FORMOSA DO RIO PRETO | BAHIA | Brasil | 2911105 | 29 | 33 | nan | nan | nan | Cerrado | 64.5 |
| f412f58b-b817-3937-8cfb-f888d6fa9f36 | -12.4522 | -43.2717 | 2026-09-05 13:10:00 | GOES-19 | MUQUÉM DO SÃO FRANCISCO | BAHIA | Brasil | 2922250 | 29 | 33 | nan | nan | nan | Cerrado | 104.5 |
| ab0e4438-85c3-3d8b-96f6-85d27c22f005 | -13.4264 | -43.8163 | 2026-09-05 13:10:00 | GOES-19 | SERRA DO RAMALHO | BAHIA | Brasil | 2930154 | 29 | 33 | nan | nan | nan | Cerrado | 62.6 |
| 70246485-21e3-3d78-99eb-4852ef239658 | -10.9592 | -50.2744 | 2026-09-05 13:10:00 | GOES-19 | LAGOA DA CONFUSÃO | TOCANTINS | Brasil | 1711902 | 17 | 33 | nan | nan | nan | Cerrado | 67.7 |
| 9f2ab9d4-5f93-3494-bd81-e2304077bd2e | -3.56 | -48.2 | 2026-09-05 13:15:00 | MSG-03 | PARAGOMINAS | PARÁ | Brasil | 1505502 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| f52dc40f-983c-332c-b132-772015fcafb6 | -3.53 | -48.2 | 2026-09-05 13:15:00 | MSG-03 | PARAGOMINAS | PARÁ | Brasil | 1505502 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| b97bb44a-4309-3349-bcc0-973a67735320 | -12.1508 | -47.1058 | 2026-09-05 13:20:00 | GOES-19 | CONCEIÇÃO DO TOCANTINS | TOCANTINS | Brasil | 1705607 | 17 | 33 | nan | nan | nan | Cerrado | 64.6 |
| 444dd1fa-82c5-3448-b70f-ad04d1d192ba | -12.1512 | -47.0833 | 2026-09-05 13:20:00 | GOES-19 | TAIPAS DO TOCANTINS | TOCANTINS | Brasil | 1720937 | 17 | 33 | nan | nan | nan | Cerrado | 61.6 |
| ecad38da-dc85-301b-9578-e484efa32e2a | -5.3462 | -56.0256 | 2026-09-05 13:20:00 | GOES-19 | TRAIRÃO | PARÁ | Brasil | 1508050 | 15 | 33 | nan | nan | nan | Amazônia | 285.1 |
| d1f9c7f5-9c04-3735-92e6-163033593728 | -11.5388 | -44.8933 | 2026-09-05 13:20:00 | GOES-19 | RIACHÃO DAS NEVES | BAHIA | Brasil | 2926202 | 29 | 33 | nan | nan | nan | Cerrado | 61.4 |
| 859dcee9-43d0-3f68-ad18-6810e4d48b56 | -4.6669 | -55.635 | 2026-09-05 13:20:00 | GOES-19 | ITAITUBA | PARÁ | Brasil | 1503606 | 15 | 33 | nan | nan | nan | Amazônia | 72.4 |
| 3abc295d-6054-3cdb-98c4-f89d3f27fb66 | -5.346 | -56.0454 | 2026-09-05 13:20:00 | GOES-19 | TRAIRÃO | PARÁ | Brasil | 1508050 | 15 | 33 | nan | nan | nan | Amazônia | 188.0 |
| a3ae13a1-68f6-31a3-aa08-85d5382c1693 | -12.4328 | -43.275 | 2026-09-05 13:20:00 | GOES-19 | MUQUÉM DO SÃO FRANCISCO | BAHIA | Brasil | 2922250 | 29 | 33 | nan | nan | nan | Cerrado | 119.0 |
| ab409b96-c87a-3a2b-921d-a4a59b25063a | -3.5406 | -48.1889 | 2026-09-05 13:20:00 | GOES-19 | PARAGOMINAS | PARÁ | Brasil | 1505502 | 15 | 33 | nan | nan | nan | Amazônia | 328.4 |
| 0b8b9572-bcdf-3519-8732-21f4e0d7f060 | -12.1316 | -47.1084 | 2026-09-05 13:20:00 | GOES-19 | CONCEIÇÃO DO TOCANTINS | TOCANTINS | Brasil | 1705607 | 17 | 33 | nan | nan | nan | Cerrado | 60.5 |
| 9277f90d-c0fb-351c-988a-4816c7908cee | -12.4522 | -43.2717 | 2026-09-05 13:20:00 | GOES-19 | MUQUÉM DO SÃO FRANCISCO | BAHIA | Brasil | 2922250 | 29 | 33 | nan | nan | nan | Cerrado | 65.4 |
| c511285d-ebe0-3b3d-800e-319e8052dcd3 | -5.3277 | -56.0263 | 2026-09-05 13:20:00 | GOES-19 | TRAIRÃO | PARÁ | Brasil | 1508050 | 15 | 33 | nan | nan | nan | Amazônia | 71.5 |
| 7a68142d-007e-3d68-83ac-e46849df5303 | -3.5407 | -48.1673 | 2026-09-05 13:20:00 | GOES-19 | PARAGOMINAS | PARÁ | Brasil | 1505502 | 15 | 33 | nan | nan | nan | Amazônia | 150.5 |
| b459eef5-da54-32a5-92b9-caa5735bf1f3 | -1.4211 | -54.2171 | 2026-09-05 13:20:00 | GOES-19 | MONTE ALEGRE | PARÁ | Brasil | 1504802 | 15 | 33 | nan | nan | nan | Amazônia | 89.7 |
| bc055f10-c018-37b7-a20a-ab7b7f8093f5 | -12.132 | -47.086 | 2026-09-05 13:30:00 | GOES-19 | CONCEIÇÃO DO TOCANTINS | TOCANTINS | Brasil | 1705607 | 17 | 33 | nan | nan | nan | Cerrado | 57.3 |
| e76ddbb9-b479-32d0-889d-dbd61c1bf359 | -12.4328 | -43.275 | 2026-09-05 13:30:00 | GOES-19 | MUQUÉM DO SÃO FRANCISCO | BAHIA | Brasil | 2922250 | 29 | 33 | nan | nan | nan | Cerrado | 143.1 |
| 15644642-13f3-3b13-876a-dd85a4fc4e38 | -12.4522 | -43.2717 | 2026-09-05 13:30:00 | GOES-19 | MUQUÉM DO SÃO FRANCISCO | BAHIA | Brasil | 2922250 | 29 | 33 | nan | nan | nan | Cerrado | 73.5 |
| 5f59bc62-1a44-3be6-a413-784b8f66babc | -12.1508 | -47.1058 | 2026-09-05 13:30:00 | GOES-19 | CONCEIÇÃO DO TOCANTINS | TOCANTINS | Brasil | 1705607 | 17 | 33 | nan | nan | nan | Cerrado | 69.4 |
| 10af7899-fa74-31e1-97c6-0728ec66d2ff | -5.3462 | -56.0256 | 2026-09-05 13:30:00 | GOES-19 | TRAIRÃO | PARÁ | Brasil | 1508050 | 15 | 33 | nan | nan | nan | Amazônia | 690.0 |
| 4dbb8ace-fc0a-3464-858e-0ab45e9a7bf6 | -10.5254 | -50.1709 | 2026-09-05 13:30:00 | GOES-19 | PIUM | TOCANTINS | Brasil | 1717503 | 17 | 33 | nan | nan | nan | Cerrado | 67.4 |
| d5df4563-a61b-3dc3-b355-6b4a49e2968d | -12.1704 | -47.0806 | 2026-09-05 13:30:00 | GOES-19 | TAIPAS DO TOCANTINS | TOCANTINS | Brasil | 1720937 | 17 | 33 | nan | nan | nan | Cerrado | 59.9 |
| e8a0a2cb-3267-3726-a894-eded903eeed5 | -5.346 | -56.0454 | 2026-09-05 13:30:00 | GOES-19 | TRAIRÃO | PARÁ | Brasil | 1508050 | 15 | 33 | nan | nan | nan | Amazônia | 772.4 |
| 44beed5b-b6cc-3c25-ad48-967b2a39c485 | -3.5407 | -48.1673 | 2026-09-05 13:30:00 | GOES-19 | PARAGOMINAS | PARÁ | Brasil | 1505502 | 15 | 33 | nan | nan | nan | Amazônia | 161.5 |
| a7f04db3-f937-3a26-9df2-b35729c15c06 | -5.3277 | -56.0263 | 2026-09-05 13:30:00 | GOES-19 | TRAIRÃO | PARÁ | Brasil | 1508050 | 15 | 33 | nan | nan | nan | Amazônia | 72.3 |
| d6e9c127-36db-344f-94a3-e98b3a9222ff | -12.1512 | -47.0833 | 2026-09-05 13:30:00 | GOES-19 | TAIPAS DO TOCANTINS | TOCANTINS | Brasil | 1720937 | 17 | 33 | nan | nan | nan | Cerrado | 66.5 |
| 6936fcf1-1fa1-315f-aff0-be8c57fafa72 | -3.5406 | -48.1889 | 2026-09-05 13:30:00 | GOES-19 | PARAGOMINAS | PARÁ | Brasil | 1505502 | 15 | 33 | nan | nan | nan | Amazônia | 304.4 |
| 2d1de617-a6ee-3a0b-a301-df7ed160d217 | -10.6921 | -50.4311 | 2026-09-05 13:40:00 | GOES-19 | LAGOA DA CONFUSÃO | TOCANTINS | Brasil | 1711902 | 17 | 33 | nan | nan | nan | Cerrado | 67.2 |
| e9136c61-b719-31e7-91cf-9129f8e23553 | -3.5406 | -48.1889 | 2026-09-05 13:40:00 | GOES-19 | PARAGOMINAS | PARÁ | Brasil | 1505502 | 15 | 33 | nan | nan | nan | Amazônia | 368.6 |
| 4acb11b0-f71d-399a-966b-e5a9cf335921 | -10.3196 | -50.0211 | 2026-09-05 13:40:00 | GOES-19 | PIUM | TOCANTINS | Brasil | 1717503 | 17 | 33 | nan | nan | nan | Cerrado | 64.9 |
| 361159a9-c228-3a02-b53b-947db8054a49 | -4.6669 | -55.635 | 2026-09-05 13:40:00 | GOES-19 | ITAITUBA | PARÁ | Brasil | 1503606 | 15 | 33 | nan | nan | nan | Amazônia | 66.5 |
| c666240f-bb86-32b5-b5c0-cdbecd942262 | -10.6731 | -50.4331 | 2026-09-05 13:40:00 | GOES-19 | LAGOA DA CONFUSÃO | TOCANTINS | Brasil | 1711902 | 17 | 33 | nan | nan | nan | Cerrado | 69.2 |
| f2c38f2f-1b11-3194-83be-4683aadfb676 | -10.5254 | -50.1709 | 2026-09-05 13:40:00 | GOES-19 | PIUM | TOCANTINS | Brasil | 1717503 | 17 | 33 | nan | nan | nan | Cerrado | 71.9 |
| 13e8ac64-2f76-3c0a-9eaa-5363920682da | -10.3385 | -50.0191 | 2026-09-05 13:40:00 | GOES-19 | PIUM | TOCANTINS | Brasil | 1717503 | 17 | 33 | nan | nan | nan | Cerrado | 62.7 |
| c1a7a6ec-966a-3a9d-b5ed-21e51d089099 | -3.8019 | -55.8798 | 2026-09-05 13:40:00 | GOES-19 | AVEIRO | PARÁ | Brasil | 1501006 | 15 | 33 | nan | nan | nan | Amazônia | 94.4 |
| 01fad9b1-a5b7-32fa-ab60-0477a4e994c2 | -3.5407 | -48.1673 | 2026-09-05 13:40:00 | GOES-19 | PARAGOMINAS | PARÁ | Brasil | 1505502 | 15 | 33 | nan | nan | nan | Amazônia | 147.6 |
| 76a94567-1ffd-3a82-82dc-7998320cbd34 | -12.1512 | -47.0833 | 2026-09-05 13:40:00 | GOES-19 | TAIPAS DO TOCANTINS | TOCANTINS | Brasil | 1720937 | 17 | 33 | nan | nan | nan | Cerrado | 67.2 |
| a5d06ed3-5eb6-3d65-b744-2eeedfdfd7ef | -12.1704 | -47.0806 | 2026-09-05 13:40:00 | GOES-19 | TAIPAS DO TOCANTINS | TOCANTINS | Brasil | 1720937 | 17 | 33 | nan | nan | nan | Cerrado | 63.1 |
| 6373889d-9508-35d5-be3d-61896003aea0 | -12.1312 | -47.1309 | 2026-09-05 13:40:00 | GOES-19 | CONCEIÇÃO DO TOCANTINS | TOCANTINS | Brasil | 1705607 | 17 | 33 | nan | nan | nan | Cerrado | 59.2 |
| 37f9f5bb-48db-344a-ac97-1b968d9e0547 | -3.7827 | -61.7733 | 2026-09-05 13:40:00 | GOES-19 | ANORI | AMAZONAS | Brasil | 1300102 | 13 | 33 | nan | nan | nan | Amazônia | 90.1 |
| 137934d8-996f-3576-90f9-daea79d2958b | -12.4328 | -43.275 | 2026-09-05 13:40:00 | GOES-19 | MUQUÉM DO SÃO FRANCISCO | BAHIA | Brasil | 2922250 | 29 | 33 | nan | nan | nan | Cerrado | 122.7 |
| 8ba3fe7f-7f7f-3a3a-be0a-d0e2a56f7813 | -10.3007 | -50.023 | 2026-09-05 13:40:00 | GOES-19 | PIUM | TOCANTINS | Brasil | 1717503 | 17 | 33 | nan | nan | nan | Cerrado | 66.6 |
| 8041c710-07d2-38a7-9250-97f718025482 | -3.7645 | -61.7737 | 2026-09-05 13:40:00 | GOES-19 | ANORI | AMAZONAS | Brasil | 1300102 | 13 | 33 | nan | nan | nan | Amazônia | 87.1 |
| 3964c4ed-5fb6-3bb4-8350-a364280a4b10 | -6.93799 | -71.27801 | 2026-09-05 13:46:00 | TERRA_M-T | IPIXUNA | AMAZONAS | Brasil | 1301803 | 13 | 33 | nan | nan | nan | Amazônia | 6.3 |
| 81f44a75-fe3e-3a7b-b974-5cd3d0c80eee | -3.7645 | -61.7737 | 2026-09-05 13:50:00 | GOES-19 | ANORI | AMAZONAS | Brasil | 1300102 | 13 | 33 | nan | nan | nan | Amazônia | 96.4 |
| fe09555a-08e6-3632-bcfd-9d6a56918124 | -4.6853 | -55.6343 | 2026-09-05 13:50:00 | GOES-19 | ITAITUBA | PARÁ | Brasil | 1503606 | 15 | 33 | nan | nan | nan | Amazônia | 69.4 |
| 869ed5a5-6268-3cb6-ab72-617c7e6a7282 | -12.1124 | -47.1111 | 2026-09-05 13:50:00 | GOES-19 | CONCEIÇÃO DO TOCANTINS | TOCANTINS | Brasil | 1705607 | 17 | 33 | nan | nan | nan | Cerrado | 54.4 |
| 24acd58e-14d0-3c4b-a14d-f3fe16257edb | -17.5296 | -44.606 | 2026-09-05 13:50:00 | GOES-19 | VÁRZEA DA PALMA | MINAS GERAIS | Brasil | 3170800 | 31 | 33 | nan | nan | nan | Cerrado | 109.7 |
| 85261374-ca14-3027-90e1-4adab5984ca3 | -10.5254 | -50.1709 | 2026-09-05 13:50:00 | GOES-19 | PIUM | TOCANTINS | Brasil | 1717503 | 17 | 33 | nan | nan | nan | Cerrado | 78.6 |
| d4296658-ac51-3092-bdaf-337239ff8be9 | -12.1508 | -47.1058 | 2026-09-05 13:50:00 | GOES-19 | CONCEIÇÃO DO TOCANTINS | TOCANTINS | Brasil | 1705607 | 17 | 33 | nan | nan | nan | Cerrado | 76.7 |
| 293d1f67-d82f-333c-af28-12f7e2136108 | -10.165 | -50.2933 | 2026-09-05 13:50:00 | GOES-19 | PIUM | TOCANTINS | Brasil | 1717503 | 17 | 33 | nan | nan | nan | Cerrado | 64.2 |
| e6063fdb-e946-38ba-92c1-64bc3e93f7a0 | -12.1316 | -47.1084 | 2026-09-05 13:50:00 | GOES-19 | CONCEIÇÃO DO TOCANTINS | TOCANTINS | Brasil | 1705607 | 17 | 33 | nan | nan | nan | Cerrado | 70.1 |
| 591d8a0d-2ef2-3241-b1a4-8e3cbd09f675 | -3.5407 | -48.1673 | 2026-09-05 13:50:00 | GOES-19 | PARAGOMINAS | PARÁ | Brasil | 1505502 | 15 | 33 | nan | nan | nan | Amazônia | 151.2 |
| b09262e8-09c1-31df-a996-fb86ad94823f | -10.3385 | -50.0191 | 2026-09-05 13:50:00 | GOES-19 | PIUM | TOCANTINS | Brasil | 1717503 | 17 | 33 | nan | nan | nan | Cerrado | 67.1 |
| c72d4ef2-ebbe-34f7-ad80-30f9710c7974 | -3.7827 | -61.7733 | 2026-09-05 13:50:00 | GOES-19 | ANORI | AMAZONAS | Brasil | 1300102 | 13 | 33 | nan | nan | nan | Amazônia | 99.0 |
| 5d14dc25-123b-3eae-a17f-19db750477ac | -3.5592 | -48.1666 | 2026-09-05 13:50:00 | GOES-19 | PARAGOMINAS | PARÁ | Brasil | 1505502 | 15 | 33 | nan | nan | nan | Amazônia | 161.3 |
| d55acb91-b8ad-3430-badd-8778e65ebcba | -13.4458 | -43.8128 | 2026-09-05 13:50:00 | GOES-19 | SERRA DO RAMALHO | BAHIA | Brasil | 2930154 | 29 | 33 | nan | nan | nan | Cerrado | 59.0 |
| c4389d1f-f4cc-3f52-96e6-3c56b8f734e5 | -4.6669 | -55.635 | 2026-09-05 13:50:00 | GOES-19 | ITAITUBA | PARÁ | Brasil | 1503606 | 15 | 33 | nan | nan | nan | Amazônia | 88.4 |
| aaa52f93-8c1b-30b8-a494-efc8b3af7046 | -12.1312 | -47.1309 | 2026-09-05 13:50:00 | GOES-19 | CONCEIÇÃO DO TOCANTINS | TOCANTINS | Brasil | 1705607 | 17 | 33 | nan | nan | nan | Cerrado | 54.8 |
| 393a7c15-3bd6-3a62-a027-fb8481b2b3b7 | -12.1504 | -47.1283 | 2026-09-05 13:50:00 | GOES-19 | CONCEIÇÃO DO TOCANTINS | TOCANTINS | Brasil | 1705607 | 17 | 33 | nan | nan | nan | Cerrado | 57.2 |
| 68f275b5-2161-37da-95a5-2a18339af359 | -10.3007 | -50.023 | 2026-09-05 13:50:00 | GOES-19 | PIUM | TOCANTINS | Brasil | 1717503 | 17 | 33 | nan | nan | nan | Cerrado | 71.7 |
| 8a2b77b7-01e9-3c65-b59b-e2ff04ac225f | -3.7645 | -61.7548 | 2026-09-05 13:50:00 | GOES-19 | ANORI | AMAZONAS | Brasil | 1300102 | 13 | 33 | nan | nan | nan | Amazônia | 88.7 |
| 79808076-35bc-331e-89e3-b428a91412fc | -12.4328 | -43.275 | 2026-09-05 13:50:00 | GOES-19 | MUQUÉM DO SÃO FRANCISCO | BAHIA | Brasil | 2922250 | 29 | 33 | nan | nan | nan | Cerrado | 114.1 |
| f5d54eb6-3331-3aeb-ad5f-20968b832db2 | -12.4522 | -43.2717 | 2026-09-05 13:50:00 | GOES-19 | MUQUÉM DO SÃO FRANCISCO | BAHIA | Brasil | 2922250 | 29 | 33 | nan | nan | nan | Cerrado | 60.9 |
| beb96113-b2ae-392a-85bb-3b5b6db38bd3 | -3.8019 | -55.8798 | 2026-09-05 13:50:00 | GOES-19 | AVEIRO | PARÁ | Brasil | 1501006 | 15 | 33 | nan | nan | nan | Amazônia | 65.6 |
| 93957d8b-c5b0-36ab-8b6b-477751663c5a | -10.3196 | -50.0211 | 2026-09-05 13:50:00 | GOES-19 | PIUM | TOCANTINS | Brasil | 1717503 | 17 | 33 | nan | nan | nan | Cerrado | 69.8 |
| f6fce690-be9d-3ed0-ac87-cc4559e73d9b | -3.5406 | -48.1889 | 2026-09-05 13:50:00 | GOES-19 | PARAGOMINAS | PARÁ | Brasil | 1505502 | 15 | 33 | nan | nan | nan | Amazônia | 281.2 |
| 0e0b4620-49b7-3a1f-91d6-4582167b5c74 | -10.5254 | -50.1709 | 2026-09-05 14:00:00 | GOES-19 | PIUM | TOCANTINS | Brasil | 1717503 | 17 | 33 | nan | nan | nan | Cerrado | 81.7 |
| f91b9e41-7092-31ea-9a1b-fd4fc8c8494b | -4.6853 | -55.6343 | 2026-09-05 14:00:00 | GOES-19 | ITAITUBA | PARÁ | Brasil | 1503606 | 15 | 33 | nan | nan | nan | Amazônia | 78.3 |


[Clique aqui para ver as próximas entradas](README39.md)
