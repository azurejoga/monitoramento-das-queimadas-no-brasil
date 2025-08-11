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

## Dados Diários - Página 18

| ID | Latitude | Longitude | Data/Hora GMT | Satélite | Município | Estado | País | Município ID | Estado ID | País ID | Dias sem Chuva | Precipitação | Risco de Fogo | Bioma | FRP |
|----|----------|-----------|---------------|----------|-----------|--------|------|--------------|-----------|---------|----------------|--------------|----------------|-------|-----|
| 6cd80c91-d44d-30ac-ae1b-dc0ccb06fd7c | -15.43829 | -53.92795 | 2025-08-11 04:27:00 | NOAA-20 | POXORÉU | MATO GROSSO | Brasil | 5107008 | 51 | 33 | nan | nan | nan | Cerrado | 5.6 |
| af9d9912-c44a-3e1b-bce6-51df76849fc1 | -14.60316 | -49.61149 | 2025-08-11 04:27:00 | NOAA-20 | SANTA TEREZINHA DE GOIÁS | GOIÁS | Brasil | 5219704 | 52 | 33 | nan | nan | nan | Cerrado | 9.3 |
| 96191d40-1edb-3fcb-b261-f28cadf23ea5 | -12.60865 | -47.13844 | 2025-08-11 04:27:00 | NOAA-20 | ARRAIAS | TOCANTINS | Brasil | 1702406 | 17 | 33 | nan | nan | nan | Cerrado | 1.3 |
| 8d05ae75-ac64-33da-9d9c-be9fa31ed98d | -14.12172 | -44.86764 | 2025-08-11 04:27:00 | NOAA-20 | COCOS | BAHIA | Brasil | 2908101 | 29 | 33 | nan | nan | nan | Cerrado | 4.7 |
| 5490585d-151b-3763-9a84-2e78cca448a3 | -11.12121 | -50.50875 | 2025-08-11 04:27:00 | NOAA-20 | LAGOA DA CONFUSÃO | TOCANTINS | Brasil | 1711902 | 17 | 33 | nan | nan | nan | Cerrado | 0.8 |
| 05bf8990-bacd-3660-98c7-eca1c9abde49 | -14.12026 | -45.40566 | 2025-08-11 04:27:00 | NOAA-20 | JABORANDI | BAHIA | Brasil | 2917359 | 29 | 33 | nan | nan | nan | Cerrado | 0.9 |
| 0d3bc88b-6f83-3dfe-ad97-2a88dca8667c | -13.58882 | -46.94181 | 2025-08-11 04:27:00 | NOAA-20 | NOVA ROMA | GOIÁS | Brasil | 5214903 | 52 | 33 | nan | nan | nan | Cerrado | 0.7 |
| 9d1b9dc1-8cc9-310d-8076-542195ddaa4b | -15.4492 | -53.93783 | 2025-08-11 04:27:00 | NOAA-20 | POXORÉU | MATO GROSSO | Brasil | 5107008 | 51 | 33 | nan | nan | nan | Cerrado | 6.9 |
| 328e5c79-ccbc-30d6-9b6f-30cdf27f0d9d | -15.76856 | -47.77139 | 2025-08-11 04:27:00 | NOAA-20 | BRASÍLIA | DISTRITO FEDERAL | Brasil | 5300108 | 53 | 33 | nan | nan | nan | Cerrado | 0.3 |
| 86094eb0-419f-3a0f-bad1-a9315813c3ca | -14.30336 | -51.96214 | 2025-08-11 04:27:00 | NOAA-20 | NOVA NAZARÉ | MATO GROSSO | Brasil | 5106174 | 51 | 33 | nan | nan | nan | Cerrado | 6.2 |
| 35b2cc9b-79da-36c7-98d4-7e52b4d6e80e | -16.20823 | -49.9874 | 2025-08-11 04:27:00 | NOAA-20 | MOSSÂMEDES | GOIÁS | Brasil | 5213905 | 52 | 33 | nan | nan | nan | Cerrado | 2.1 |
| 4178f5aa-5dd3-3360-a33e-4476dbaa5682 | -16.29694 | -52.91914 | 2025-08-11 04:27:00 | NOAA-20 | TORIXORÉU | MATO GROSSO | Brasil | 5108204 | 51 | 33 | nan | nan | nan | Cerrado | 2.6 |
| d8445c8d-0a00-3ac4-b05f-641a0a4df8f2 | -13.59436 | -46.95044 | 2025-08-11 04:27:00 | NOAA-20 | NOVA ROMA | GOIÁS | Brasil | 5214903 | 52 | 33 | nan | nan | nan | Cerrado | 3.8 |
| 769833b6-2f85-3c32-a3d6-ac3c47eb75e4 | -16.40175 | -48.11051 | 2025-08-11 04:27:00 | NOAA-20 | LUZIÂNIA | GOIÁS | Brasil | 5212501 | 52 | 33 | nan | nan | nan | Cerrado | 2.0 |
| 1487a15c-1131-372e-89c2-26c713c3c573 | -15.63367 | -48.5497 | 2025-08-11 04:27:00 | NOAA-20 | COCALZINHO DE GOIÁS | GOIÁS | Brasil | 5205513 | 52 | 33 | nan | nan | nan | Cerrado | 0.8 |
| c1ebb6a4-8ea5-3c65-8ebe-c2056632c728 | -13.64677 | -49.03597 | 2025-08-11 04:27:00 | NOAA-20 | SANTA TEREZA DE GOIÁS | GOIÁS | Brasil | 5219605 | 52 | 33 | nan | nan | nan | Cerrado | 1.6 |
| 62ad8869-2274-3327-8267-a68da9572d19 | -13.06495 | -56.8488 | 2025-08-11 04:27:00 | NOAA-20 | NOVA MARINGÁ | MATO GROSSO | Brasil | 5108907 | 51 | 33 | nan | nan | nan | Amazônia | 0.8 |
| 461b7896-2027-3379-bc3a-8cd6006190ba | -19.41891 | -43.36966 | 2025-08-11 04:27:00 | NOAA-20 | ITAMBÉ DO MATO DENTRO | MINAS GERAIS | Brasil | 3132800 | 31 | 33 | nan | nan | nan | Cerrado | 3.6 |
| 2471d393-97e7-39bd-9ccf-0241179f5687 | -15.43353 | -53.93092 | 2025-08-11 04:27:00 | NOAA-20 | POXORÉU | MATO GROSSO | Brasil | 5107008 | 51 | 33 | nan | nan | nan | Cerrado | 36.2 |
| ce7576ea-07e6-30c7-90b3-d36c80faab06 | -15.41583 | -53.91194 | 2025-08-11 04:27:00 | NOAA-20 | POXORÉU | MATO GROSSO | Brasil | 5107008 | 51 | 33 | nan | nan | nan | Cerrado | 2.0 |
| 834d2578-9346-3fe4-ad70-61893a78f759 | -18.80155 | -43.8737 | 2025-08-11 04:27:00 | NOAA-20 | SANTANA DE PIRAPAMA | MINAS GERAIS | Brasil | 3158508 | 31 | 33 | nan | nan | nan | Cerrado | 3.9 |
| 9d0de854-f6bd-3b24-9b7a-ec5f25202ffc | -17.22779 | -46.95874 | 2025-08-11 04:27:00 | NOAA-20 | PARACATU | MINAS GERAIS | Brasil | 3147006 | 31 | 33 | nan | nan | nan | Cerrado | 1.7 |
| 6e7e259a-ad2a-3cb9-a2b9-8e8bd9e848f3 | -16.37949 | -42.53251 | 2025-08-11 04:27:00 | NOAA-20 | PADRE CARVALHO | MINAS GERAIS | Brasil | 3146255 | 31 | 33 | nan | nan | nan | Cerrado | 1.0 |
| 8af275a5-6c83-3373-9794-f86150758557 | -19.21809 | -46.80486 | 2025-08-11 04:27:00 | NOAA-20 | SERRA DO SALITRE | MINAS GERAIS | Brasil | 3166808 | 31 | 33 | nan | nan | nan | Cerrado | 10.0 |
| df697681-223e-3eee-9e39-78909c5997a5 | -13.80285 | -41.20507 | 2025-08-11 04:27:00 | NOAA-20 | CONTENDAS DO SINCORÁ | BAHIA | Brasil | 2908804 | 29 | 33 | nan | nan | nan | Caatinga | 1.1 |
| b06ed131-0023-3291-a47c-9cc0b8f072a4 | -12.6092 | -47.13489 | 2025-08-11 04:27:00 | NOAA-20 | ARRAIAS | TOCANTINS | Brasil | 1702406 | 17 | 33 | nan | nan | nan | Cerrado | 0.9 |
| e752c098-a1e7-35dc-9acb-897bf82feb0a | -13.5977 | -46.95102 | 2025-08-11 04:27:00 | NOAA-20 | NOVA ROMA | GOIÁS | Brasil | 5214903 | 52 | 33 | nan | nan | nan | Cerrado | 0.6 |
| d40211fa-f220-31fe-8bb4-0eba72782433 | -12.70606 | -46.36843 | 2025-08-11 04:27:00 | NOAA-20 | AURORA DO TOCANTINS | TOCANTINS | Brasil | 1702703 | 17 | 33 | nan | nan | nan | Cerrado | 1.3 |
| c4685ec8-b192-3ff7-abd7-b2097d57b123 | -18.61942 | -46.85704 | 2025-08-11 04:27:00 | NOAA-20 | COROMANDEL | MINAS GERAIS | Brasil | 3119302 | 31 | 33 | nan | nan | nan | Cerrado | 3.7 |
| 5c3f7a1b-2a1a-34ed-b10b-f30bde70eb19 | -12.04496 | -45.76311 | 2025-08-11 04:27:00 | NOAA-20 | LUÍS EDUARDO MAGALHÃES | BAHIA | Brasil | 2919553 | 29 | 33 | nan | nan | nan | Cerrado | 23.5 |
| 50f127e3-2056-30e3-a7c8-691f8c340fe8 | -12.70888 | -46.37264 | 2025-08-11 04:27:00 | NOAA-20 | AURORA DO TOCANTINS | TOCANTINS | Brasil | 1702703 | 17 | 33 | nan | nan | nan | Cerrado | 0.6 |
| 739bf9e4-4fe6-3894-ac42-181d7dd2e67a | -12.70943 | -46.36897 | 2025-08-11 04:27:00 | NOAA-20 | AURORA DO TOCANTINS | TOCANTINS | Brasil | 1702703 | 17 | 33 | nan | nan | nan | Cerrado | 1.5 |
| 4039a6fd-db48-363e-b411-ab41ad04f083 | -13.05981 | -56.84769 | 2025-08-11 04:27:00 | NOAA-20 | NOVA MARINGÁ | MATO GROSSO | Brasil | 5108907 | 51 | 33 | nan | nan | nan | Amazônia | 1.0 |
| 5d083c4c-dd80-3a7f-b447-2f30d3d93cf7 | -16.53358 | -47.58064 | 2025-08-11 04:27:00 | NOAA-20 | CRISTALINA | GOIÁS | Brasil | 5206206 | 52 | 33 | nan | nan | nan | Cerrado | 0.7 |
| 0df8c08e-eb86-34ff-8772-7fbfeadea9aa | -11.5441 | -50.55958 | 2025-08-11 04:27:00 | NOAA-20 | LAGOA DA CONFUSÃO | TOCANTINS | Brasil | 1711902 | 17 | 33 | nan | nan | nan | Cerrado | 0.5 |
| a7146044-914a-3345-889f-98870fc46866 | -13.59103 | -46.94985 | 2025-08-11 04:27:00 | NOAA-20 | NOVA ROMA | GOIÁS | Brasil | 5214903 | 52 | 33 | nan | nan | nan | Cerrado | 3.8 |
| 177b501a-a7f4-368c-a4b2-63bed81faa36 | -16.01511 | -51.36482 | 2025-08-11 04:27:00 | NOAA-20 | MONTES CLAROS DE GOIÁS | GOIÁS | Brasil | 5213707 | 52 | 33 | nan | nan | nan | Cerrado | 0.8 |
| e211487d-122f-31d6-a6d2-6702f8302ed3 | -13.33772 | -43.37691 | 2025-08-11 04:27:00 | NOAA-20 | BOM JESUS DA LAPA | BAHIA | Brasil | 2903904 | 29 | 33 | nan | nan | nan | Caatinga | 1.9 |
| 8dc20903-cd01-3fa4-b3eb-14d765287049 | -15.43694 | -53.93547 | 2025-08-11 04:27:00 | NOAA-20 | POXORÉU | MATO GROSSO | Brasil | 5107008 | 51 | 33 | nan | nan | nan | Cerrado | 2.2 |
| a0314533-d07c-38a0-b691-033b0a2b5c62 | -16.7089 | -43.84735 | 2025-08-11 04:27:00 | NOAA-20 | MONTES CLAROS | MINAS GERAIS | Brasil | 3143302 | 31 | 33 | nan | nan | nan | Cerrado | 0.8 |
| 8f2221ea-d172-3a0b-919a-19d12dc7c551 | -15.42331 | -53.91726 | 2025-08-11 04:27:00 | NOAA-20 | POXORÉU | MATO GROSSO | Brasil | 5107008 | 51 | 33 | nan | nan | nan | Cerrado | 32.5 |
| 56b955be-a9de-37b4-895d-0e4f54157e0b | -18.03634 | -44.45694 | 2025-08-11 04:27:00 | NOAA-20 | LASSANCE | MINAS GERAIS | Brasil | 3138104 | 31 | 33 | nan | nan | nan | Cerrado | 1.8 |
| 3d2cfb14-63c2-378b-98e0-97245d711b7a | -16.01159 | -51.36417 | 2025-08-11 04:27:00 | NOAA-20 | MONTES CLAROS DE GOIÁS | GOIÁS | Brasil | 5213707 | 52 | 33 | nan | nan | nan | Cerrado | 1.2 |
| 24ef5368-0090-3896-86f0-454911d48ab0 | -11.69239 | -50.12615 | 2025-08-11 04:27:00 | NOAA-20 | FORMOSO DO ARAGUAIA | TOCANTINS | Brasil | 1708205 | 17 | 33 | nan | nan | nan | Cerrado | 4.3 |
| 27c5cd7a-138e-337b-8995-a525315320b6 | -11.77709 | -47.39914 | 2025-08-11 04:27:00 | NOAA-20 | ALMAS | TOCANTINS | Brasil | 1700400 | 17 | 33 | nan | nan | nan | Cerrado | 0.6 |
| bb3aaa64-f51d-310b-8c7f-465acb20728a | -16.68847 | -47.63582 | 2025-08-11 04:27:00 | NOAA-20 | CRISTALINA | GOIÁS | Brasil | 5206206 | 52 | 33 | nan | nan | nan | Cerrado | 2.6 |
| 3903f952-12f4-3b87-8848-6fe39c49e318 | -14.48525 | -47.07178 | 2025-08-11 04:27:00 | NOAA-20 | FLORES DE GOIÁS | GOIÁS | Brasil | 5207907 | 52 | 33 | nan | nan | nan | Cerrado | 1.3 |
| 3bbcf07c-28e1-378c-8bdd-7e750796b55c | -18.42478 | -44.70813 | 2025-08-11 04:27:00 | NOAA-20 | CORINTO | MINAS GERAIS | Brasil | 3119104 | 31 | 33 | nan | nan | nan | Cerrado | 0.8 |
| bed7270a-32f9-3f1a-a16d-e74e4f463672 | -16.68903 | -47.63216 | 2025-08-11 04:27:00 | NOAA-20 | CRISTALINA | GOIÁS | Brasil | 5206206 | 52 | 33 | nan | nan | nan | Cerrado | 1.3 |
| 9feaadab-69d4-361a-a983-8010e3ba0b19 | -13.96698 | -42.58589 | 2025-08-11 04:27:00 | NOAA-20 | CAETITÉ | BAHIA | Brasil | 2905206 | 29 | 33 | nan | nan | nan | Caatinga | 0.7 |
| 101d845e-e7bd-32bf-b29e-2572fa6e2d38 | -17.80415 | -42.92535 | 2025-08-11 04:27:00 | NOAA-20 | ITAMARANDIBA | MINAS GERAIS | Brasil | 3132503 | 31 | 33 | nan | nan | nan | Cerrado | 1.2 |
| aa6c0947-b3a8-37ed-a198-fa737c8fea01 | -11.58423 | -50.31834 | 2025-08-11 04:27:00 | NOAA-20 | FORMOSO DO ARAGUAIA | TOCANTINS | Brasil | 1708205 | 17 | 33 | nan | nan | nan | Cerrado | 0.9 |
| 9f713060-facc-3378-9b02-8b275972dfa7 | -15.41038 | -53.91867 | 2025-08-11 04:27:00 | NOAA-20 | POXORÉU | MATO GROSSO | Brasil | 5107008 | 51 | 33 | nan | nan | nan | Cerrado | 3.0 |
| 219702b0-0658-3b3d-8e06-126c1bb7d1d1 | -19.08743 | -43.54679 | 2025-08-11 04:27:00 | NOAA-20 | CONCEIÇÃO DO MATO DENTRO | MINAS GERAIS | Brasil | 3117504 | 31 | 33 | nan | nan | nan | Cerrado | 0.9 |
| 24a5f1e4-c017-370c-b994-d6d13728034e | -15.54098 | -49.9912 | 2025-08-11 04:27:00 | NOAA-20 | ITAPURANGA | GOIÁS | Brasil | 5211206 | 52 | 33 | nan | nan | nan | Cerrado | 4.7 |
| 9687e997-00f3-378f-817f-ec17a1f3355a | -15.54435 | -49.99181 | 2025-08-11 04:27:00 | NOAA-20 | ITAPURANGA | GOIÁS | Brasil | 5211206 | 52 | 33 | nan | nan | nan | Cerrado | 4.7 |
| 7b96750c-5e27-315f-9752-88d097f14d1b | -11.93048 | -49.55881 | 2025-08-11 04:27:00 | NOAA-20 | FORMOSO DO ARAGUAIA | TOCANTINS | Brasil | 1708205 | 17 | 33 | nan | nan | nan | Cerrado | 1.2 |
| b6013a52-00ed-3b58-b349-95184c02d8a4 | -18.32643 | -43.67606 | 2025-08-11 04:27:00 | NOAA-20 | DATAS | MINAS GERAIS | Brasil | 3121001 | 31 | 33 | nan | nan | nan | Cerrado | 1.6 |
| 80a695b2-be5d-3d5c-9f04-197091f6dd36 | -14.11147 | -45.39184 | 2025-08-11 04:27:00 | NOAA-20 | JABORANDI | BAHIA | Brasil | 2917359 | 29 | 33 | nan | nan | nan | Cerrado | 0.8 |
| 0f1866e5-5f66-3dde-a2d0-54a05dd24e19 | -17.95887 | -44.28688 | 2025-08-11 04:27:00 | NOAA-20 | BUENÓPOLIS | MINAS GERAIS | Brasil | 3109204 | 31 | 33 | nan | nan | nan | Cerrado | 1.5 |
| 79b1f21f-34d4-3403-b2e7-197279f80e6a | -14.11673 | -45.40512 | 2025-08-11 04:27:00 | NOAA-20 | JABORANDI | BAHIA | Brasil | 2917359 | 29 | 33 | nan | nan | nan | Cerrado | 0.9 |
| 6690149f-afa4-36b7-b77c-5767e4d8e681 | -15.45235 | -53.93831 | 2025-08-11 04:27:00 | NOAA-20 | POXORÉU | MATO GROSSO | Brasil | 5107008 | 51 | 33 | nan | nan | nan | Cerrado | 1.5 |
| 00d56575-7d79-3164-895d-6ba0f0373aae | -18.3254 | -43.68393 | 2025-08-11 04:27:00 | NOAA-20 | DATAS | MINAS GERAIS | Brasil | 3121001 | 31 | 33 | nan | nan | nan | Cerrado | 2.1 |
| 3044d728-f5c8-38ce-895c-d223d8224c27 | -13.33754 | -43.37584 | 2025-08-11 04:27:00 | NOAA-20 | BOM JESUS DA LAPA | BAHIA | Brasil | 2903904 | 29 | 33 | nan | nan | nan | Caatinga | 1.8 |
| bb3decdd-1e00-340e-9e1b-a7bbfd20e5e2 | -15.99269 | -47.50161 | 2025-08-11 04:27:00 | NOAA-20 | BRASÍLIA | DISTRITO FEDERAL | Brasil | 5300108 | 53 | 33 | nan | nan | nan | Cerrado | 0.5 |
| 882b3ecf-3f84-300b-86c2-0677f105862d | -19.1634 | -44.53138 | 2025-08-11 04:27:00 | NOAA-20 | CURVELO | MINAS GERAIS | Brasil | 3120904 | 31 | 33 | nan | nan | nan | Cerrado | 1.5 |
| 90d11dbb-33c0-3391-bf8f-5e8e63c5d96a | -11.69173 | -50.13011 | 2025-08-11 04:27:00 | NOAA-20 | FORMOSO DO ARAGUAIA | TOCANTINS | Brasil | 1708205 | 17 | 33 | nan | nan | nan | Cerrado | 4.3 |
| bc5c832a-8abd-335c-b2e0-2fdea29aad32 | -15.42604 | -53.92558 | 2025-08-11 04:27:00 | NOAA-20 | POXORÉU | MATO GROSSO | Brasil | 5107008 | 51 | 33 | nan | nan | nan | Cerrado | 40.4 |
| 23d2fab2-876b-3db8-8acb-49bcc4ce3ce7 | -11.76431 | -49.1155 | 2025-08-11 04:27:00 | NOAA-20 | CARIRI DO TOCANTINS | TOCANTINS | Brasil | 1703867 | 17 | 33 | nan | nan | nan | Cerrado | 1.7 |
| 3342269c-ab8a-3f97-852e-79e96e219a26 | -13.79907 | -41.19875 | 2025-08-11 04:27:00 | NOAA-20 | CONTENDAS DO SINCORÁ | BAHIA | Brasil | 2908804 | 29 | 33 | nan | nan | nan | Caatinga | 0.7 |
| 6be7db75-a249-3b9c-bcee-82c3ac4a682e | -11.1219 | -50.50459 | 2025-08-11 04:27:00 | NOAA-20 | LAGOA DA CONFUSÃO | TOCANTINS | Brasil | 1711902 | 17 | 33 | nan | nan | nan | Cerrado | 1.2 |
| e12af563-21dc-3878-8f89-90bda57fcf6e | -18.79297 | -43.87597 | 2025-08-11 04:27:00 | NOAA-20 | SANTANA DE PIRAPAMA | MINAS GERAIS | Brasil | 3158508 | 31 | 33 | nan | nan | nan | Cerrado | 3.2 |
| 3fd64c56-e267-3192-86f8-c6d9c1783c8b | -15.63036 | -48.54915 | 2025-08-11 04:27:00 | NOAA-20 | COCALZINHO DE GOIÁS | GOIÁS | Brasil | 5205513 | 52 | 33 | nan | nan | nan | Cerrado | 0.8 |
| 54a34e16-c4b6-3b3e-87fb-28d91ffed326 | -12.61085 | -47.12425 | 2025-08-11 04:27:00 | NOAA-20 | ARRAIAS | TOCANTINS | Brasil | 1702406 | 17 | 33 | nan | nan | nan | Cerrado | 0.6 |
| 14b3c775-a2b9-394f-92f9-b3e6f6e703c8 | -18.00793 | -43.48286 | 2025-08-11 04:27:00 | NOAA-20 | COUTO DE MAGALHÃES DE MINAS | MINAS GERAIS | Brasil | 3120102 | 31 | 33 | nan | nan | nan | Cerrado | 1.4 |
| 8f1546a7-f53b-3bb7-9254-443b539bf579 | -11.11381 | -50.46481 | 2025-08-11 04:27:00 | NOAA-20 | LAGOA DA CONFUSÃO | TOCANTINS | Brasil | 1711902 | 17 | 33 | nan | nan | nan | Cerrado | 0.7 |
| f6010ee6-f68b-378d-b1db-5e812e79aa22 | -15.44418 | -53.93674 | 2025-08-11 04:27:00 | NOAA-20 | POXORÉU | MATO GROSSO | Brasil | 5107008 | 51 | 33 | nan | nan | nan | Cerrado | 9.5 |
| ef2f9560-609c-31dd-98d7-1ed881fd9a09 | -13.20904 | -50.58023 | 2025-08-11 04:27:00 | NOAA-20 | SÃO MIGUEL DO ARAGUAIA | GOIÁS | Brasil | 5220207 | 52 | 33 | nan | nan | nan | Cerrado | 1.0 |
| cdcef366-1052-3953-a6f9-bec9261ef64e | -15.57664 | -42.69095 | 2025-08-11 04:27:00 | NOAA-20 | RIO PARDO DE MINAS | MINAS GERAIS | Brasil | 3155603 | 31 | 33 | nan | nan | nan | Mata Atlântica | 0.4 |
| d6a78e99-2065-3ea7-8e3c-b17ef21ab7ff | -14.7223 | -46.98577 | 2025-08-11 04:27:00 | NOAA-20 | FLORES DE GOIÁS | GOIÁS | Brasil | 5207907 | 52 | 33 | nan | nan | nan | Cerrado | 1.0 |
| 0f2373dc-f85b-3ec0-91f6-8fa26635f5ab | -16.04074 | -43.82593 | 2025-08-11 04:27:00 | NOAA-20 | SÃO JOÃO DA PONTE | MINAS GERAIS | Brasil | 3162401 | 31 | 33 | nan | nan | nan | Cerrado | 2.2 |
| 1cb657e5-5d1c-3c77-8a67-4a946403f082 | -13.60776 | -46.92997 | 2025-08-11 04:27:00 | NOAA-20 | NOVA ROMA | GOIÁS | Brasil | 5214903 | 52 | 33 | nan | nan | nan | Cerrado | 1.1 |
| 2e7d1e38-b131-3cd4-b4d1-ac3ea07905be | -13.64593 | -48.9986 | 2025-08-11 04:27:00 | NOAA-20 | SANTA TEREZA DE GOIÁS | GOIÁS | Brasil | 5219605 | 52 | 33 | nan | nan | nan | Cerrado | 2.8 |
| 5c378d85-b346-3700-8a90-c311668b03b9 | -17.79989 | -42.92476 | 2025-08-11 04:27:00 | NOAA-20 | ITAMARANDIBA | MINAS GERAIS | Brasil | 3132503 | 31 | 33 | nan | nan | nan | Cerrado | 1.2 |
| 99c7b788-d865-372d-82b0-4cff9046795b | -18.30118 | -43.96322 | 2025-08-11 04:27:00 | NOAA-20 | DIAMANTINA | MINAS GERAIS | Brasil | 3121605 | 31 | 33 | nan | nan | nan | Cerrado | 1.8 |
| 0bcc2f62-15c6-30bf-b386-4cda2c52f352 | -14.1138 | -45.40051 | 2025-08-11 04:27:00 | NOAA-20 | JABORANDI | BAHIA | Brasil | 2917359 | 29 | 33 | nan | nan | nan | Cerrado | 1.0 |
| 46e6b64b-0fa7-336a-8255-2972b0dfb69c | -14.47799 | -47.07434 | 2025-08-11 04:27:00 | NOAA-20 | FLORES DE GOIÁS | GOIÁS | Brasil | 5207907 | 52 | 33 | nan | nan | nan | Cerrado | 0.7 |
| 4b5e7918-59fe-358e-bd91-4c891dee85cf | -12.60643 | -47.13081 | 2025-08-11 04:27:00 | NOAA-20 | ARRAIAS | TOCANTINS | Brasil | 1702406 | 17 | 33 | nan | nan | nan | Cerrado | 0.9 |
| 8f1c645c-7aaa-3cf6-848e-3bf6c1da705c | -11.35824 | -50.45741 | 2025-08-11 04:27:00 | NOAA-20 | LAGOA DA CONFUSÃO | TOCANTINS | Brasil | 1711902 | 17 | 33 | nan | nan | nan | Cerrado | 1.1 |
| 5f699d6b-920d-35a9-aaaa-5fd4117afc70 | -18.32236 | -43.6753 | 2025-08-11 04:27:00 | NOAA-20 | DATAS | MINAS GERAIS | Brasil | 3121001 | 31 | 33 | nan | nan | nan | Cerrado | 1.6 |
| 2d9c56b6-4e10-3d56-8997-f474ca3f3176 | -19.68166 | -43.84673 | 2025-08-11 04:27:00 | NOAA-20 | LAGOA SANTA | MINAS GERAIS | Brasil | 3137601 | 31 | 33 | nan | nan | nan | Cerrado | 1.0 |
| b85c6e90-419a-3a1f-a615-a8ef3c737283 | -16.04772 | -48.48655 | 2025-08-11 04:27:00 | NOAA-20 | ALEXÂNIA | GOIÁS | Brasil | 5200308 | 52 | 33 | nan | nan | nan | Cerrado | 3.3 |
| f8bd6cd1-259b-3ede-850f-6fdde7049b61 | -13.5916 | -46.9461 | 2025-08-11 04:27:00 | NOAA-20 | NOVA ROMA | GOIÁS | Brasil | 5214903 | 52 | 33 | nan | nan | nan | Cerrado | 1.6 |
| 53156bd8-9fde-3271-8d58-c38ab7df0af3 | -18.16224 | -46.9976 | 2025-08-11 04:27:00 | NOAA-20 | VAZANTE | MINAS GERAIS | Brasil | 3171006 | 31 | 33 | nan | nan | nan | Cerrado | 0.5 |
| 41a99873-202e-36db-a451-ac84f663db10 | -15.43421 | -53.92715 | 2025-08-11 04:27:00 | NOAA-20 | POXORÉU | MATO GROSSO | Brasil | 5107008 | 51 | 33 | nan | nan | nan | Cerrado | 36.2 |
| 916761a6-737e-32b6-83fe-447a10f9b39b | -17.91385 | -43.92508 | 2025-08-11 04:27:00 | NOAA-20 | BUENÓPOLIS | MINAS GERAIS | Brasil | 3109204 | 31 | 33 | nan | nan | nan | Cerrado | 1.0 |
| b7a8fd96-56dc-3a5e-9e66-f50eeafc4464 | -15.41855 | -53.92024 | 2025-08-11 04:27:00 | NOAA-20 | POXORÉU | MATO GROSSO | Brasil | 5107008 | 51 | 33 | nan | nan | nan | Cerrado | 2.4 |
| e0535651-8114-3d86-a575-762e3f5bbdac | -12.54478 | -47.07019 | 2025-08-11 04:27:00 | NOAA-20 | ARRAIAS | TOCANTINS | Brasil | 1702406 | 17 | 33 | nan | nan | nan | Cerrado | 1.5 |
| d4e7a2b3-7903-3849-b841-1fe16a3d247a | -11.33713 | -51.44644 | 2025-08-11 04:27:00 | NOAA-20 | SÃO FÉLIX DO ARAGUAIA | MATO GROSSO | Brasil | 5107859 | 51 | 33 | nan | nan | nan | Cerrado | 0.8 |
| 71ddd018-14d0-3c64-b0f9-2d387a75381e | -12.23692 | -45.053 | 2025-08-11 04:27:00 | NOAA-20 | BARREIRAS | BAHIA | Brasil | 2903201 | 29 | 33 | nan | nan | nan | Cerrado | 0.8 |


[Clique aqui para ver as próximas entradas](README19.md)
