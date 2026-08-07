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

## Dados Diários - Página 27

| ID | Latitude | Longitude | Data/Hora GMT | Satélite | Município | Estado | País | Município ID | Estado ID | País ID | Dias sem Chuva | Precipitação | Risco de Fogo | Bioma | FRP |
|----|----------|-----------|---------------|----------|-----------|--------|------|--------------|-----------|---------|----------------|--------------|----------------|-------|-----|
| 6e018e84-3f72-3546-a5ed-41ff30fe4199 | -14.2677 | -45.3103 | 2026-08-07 12:20:00 | GOES-19 | COCOS | BAHIA | Brasil | 2908101 | 29 | 33 | nan | nan | nan | Cerrado | 89.3 |
| ef176889-20b0-3c4c-a952-b924a7cfd169 | -12.441 | -50.3602 | 2026-08-07 12:30:00 | GOES-19 | FORMOSO DO ARAGUAIA | TOCANTINS | Brasil | 1708205 | 17 | 33 | nan | nan | nan | Cerrado | 74.9 |
| 0d4271b3-8c85-3b74-835f-81afbfb9dbe2 | -15.0922 | -52.7708 | 2026-08-07 12:30:00 | GOES-19 | BARRA DO GARÇAS | MATO GROSSO | Brasil | 5101803 | 51 | 33 | nan | nan | nan | Cerrado | 102.9 |
| ce64fdad-729d-3ab1-ba8f-3d8020466b13 | -14.2677 | -45.3103 | 2026-08-07 12:30:00 | GOES-19 | COCOS | BAHIA | Brasil | 2908101 | 29 | 33 | nan | nan | nan | Cerrado | 89.5 |
| 2fc79a4d-54e1-3cb1-9fc2-e96e28707235 | -12.4789 | -50.377 | 2026-08-07 12:30:00 | GOES-19 | FORMOSO DO ARAGUAIA | TOCANTINS | Brasil | 1708205 | 17 | 33 | nan | nan | nan | Cerrado | 110.2 |
| 3f763e82-f7e3-309c-a73e-b5c752627a44 | -10.4994 | -46.6941 | 2026-08-07 12:40:00 | GOES-19 | MATEIROS | TOCANTINS | Brasil | 1712702 | 17 | 33 | nan | nan | nan | Cerrado | 82.0 |
| be0f2043-584b-3e51-9236-93ff1b802e92 | -12.441 | -50.3602 | 2026-08-07 12:40:00 | GOES-19 | FORMOSO DO ARAGUAIA | TOCANTINS | Brasil | 1708205 | 17 | 33 | nan | nan | nan | Cerrado | 65.7 |
| 9c53e13f-a01e-3e8e-826f-529fdcf984ae | -15.0922 | -52.7708 | 2026-08-07 12:40:00 | GOES-19 | BARRA DO GARÇAS | MATO GROSSO | Brasil | 5101803 | 51 | 33 | nan | nan | nan | Cerrado | 69.9 |
| 63eda0fa-488f-387b-b50c-cd00e4861bf1 | -12.4789 | -50.377 | 2026-08-07 12:40:00 | GOES-19 | FORMOSO DO ARAGUAIA | TOCANTINS | Brasil | 1708205 | 17 | 33 | nan | nan | nan | Cerrado | 92.0 |
| a0185c49-cee7-392a-9764-4a450827dcfb | -12.441 | -50.3602 | 2026-08-07 12:50:00 | GOES-19 | FORMOSO DO ARAGUAIA | TOCANTINS | Brasil | 1708205 | 17 | 33 | nan | nan | nan | Cerrado | 99.1 |
| 20d5c0c0-a609-3307-bd59-abbd5b66728a | -12.4789 | -50.377 | 2026-08-07 12:50:00 | GOES-19 | FORMOSO DO ARAGUAIA | TOCANTINS | Brasil | 1708205 | 17 | 33 | nan | nan | nan | Cerrado | 78.9 |
| a36157e8-7e7e-342c-8f31-d77bbf059954 | -11.3103 | -44.8337 | 2026-08-07 12:50:00 | GOES-19 | SANTA RITA DE CÁSSIA | BAHIA | Brasil | 2928406 | 29 | 33 | nan | nan | nan | Cerrado | 67.1 |
| c1fbc85d-230c-386a-b321-f8f750f2f5b6 | -13.8236 | -53.7264 | 2026-08-07 12:50:00 | GOES-19 | PARANATINGA | MATO GROSSO | Brasil | 5106307 | 51 | 33 | nan | nan | nan | Cerrado | 106.1 |
| bbdfbd6c-a7be-301f-b4ec-f2d3eb900f79 | -15.0922 | -52.7708 | 2026-08-07 12:50:00 | GOES-19 | BARRA DO GARÇAS | MATO GROSSO | Brasil | 5101803 | 51 | 33 | nan | nan | nan | Cerrado | 104.6 |
| 42af0633-b00c-3863-aad6-eaee6fd11604 | -13.8239 | -53.7055 | 2026-08-07 12:50:00 | GOES-19 | PARANATINGA | MATO GROSSO | Brasil | 5106307 | 51 | 33 | nan | nan | nan | Cerrado | 78.7 |
| 44f1e3b2-54aa-3c10-b393-b463e684ea2a | -14.3431 | -54.9309 | 2026-08-07 12:50:00 | GOES-19 | ROSÁRIO OESTE | MATO GROSSO | Brasil | 5107701 | 51 | 33 | nan | nan | nan | Cerrado | 86.4 |
| a9cd8918-5242-3d5a-9571-490d1ced2169 | -10.4994 | -46.6941 | 2026-08-07 12:50:00 | GOES-19 | MATEIROS | TOCANTINS | Brasil | 1712702 | 17 | 33 | nan | nan | nan | Cerrado | 180.3 |
| decd870d-fd3f-3bb0-b03e-734aae10f03d | -14.2677 | -45.3103 | 2026-08-07 12:50:00 | GOES-19 | COCOS | BAHIA | Brasil | 2908101 | 29 | 33 | nan | nan | nan | Cerrado | 93.2 |
| 0828d3af-6b39-3631-9bd7-df0344d8ab6d | -6.9092 | -42.4134 | 2026-08-07 13:00:00 | GOES-19 | OEIRAS | PIAUÍ | Brasil | 2207009 | 22 | 33 | nan | nan | nan | Caatinga | 74.7 |
| 727d8e16-951c-3522-adf0-810222cb0078 | -12.441 | -50.3602 | 2026-08-07 13:00:00 | GOES-19 | FORMOSO DO ARAGUAIA | TOCANTINS | Brasil | 1708205 | 17 | 33 | nan | nan | nan | Cerrado | 74.7 |
| a1d57772-8625-36ce-be8a-af10da96d226 | -13.8236 | -53.7264 | 2026-08-07 13:00:00 | GOES-19 | PARANATINGA | MATO GROSSO | Brasil | 5106307 | 51 | 33 | nan | nan | nan | Cerrado | 88.4 |
| 7c564987-358c-3e92-ab33-977fc7335b58 | -13.8239 | -53.7055 | 2026-08-07 13:00:00 | GOES-19 | PARANATINGA | MATO GROSSO | Brasil | 5106307 | 51 | 33 | nan | nan | nan | Cerrado | 66.0 |
| 46e89692-5f7e-313b-b2c0-1cebb19f152d | -14.2677 | -45.3103 | 2026-08-07 13:00:00 | GOES-19 | COCOS | BAHIA | Brasil | 2908101 | 29 | 33 | nan | nan | nan | Cerrado | 108.1 |
| 741eaf4c-2594-326c-b000-9a46b200ee3a | -12.4789 | -50.377 | 2026-08-07 13:00:00 | GOES-19 | FORMOSO DO ARAGUAIA | TOCANTINS | Brasil | 1708205 | 17 | 33 | nan | nan | nan | Cerrado | 88.3 |
| 0141971f-6ee3-3b75-a1df-1407cb0c3571 | -15.0922 | -52.7708 | 2026-08-07 13:00:00 | GOES-19 | BARRA DO GARÇAS | MATO GROSSO | Brasil | 5101803 | 51 | 33 | nan | nan | nan | Cerrado | 154.4 |
| 1429b0ae-3ba5-3c7b-9a2b-8fd34068ddb4 | -15.1116 | -52.7682 | 2026-08-07 13:00:00 | GOES-19 | BARRA DO GARÇAS | MATO GROSSO | Brasil | 5101803 | 51 | 33 | nan | nan | nan | Cerrado | 61.3 |
| 0faa8f9f-def0-3d66-b8ae-879b976b3d9a | -14.3431 | -54.9309 | 2026-08-07 13:00:00 | GOES-19 | ROSÁRIO OESTE | MATO GROSSO | Brasil | 5107701 | 51 | 33 | nan | nan | nan | Cerrado | 100.2 |
| 0e5bdced-e48a-3ec1-bc2d-69cd5ee4ec50 | -6.9092 | -42.4134 | 2026-08-07 13:10:00 | GOES-19 | OEIRAS | PIAUÍ | Brasil | 2207009 | 22 | 33 | nan | nan | nan | Caatinga | 80.7 |
| 8e80fb40-09c5-3847-a25b-648126eeb14e | -14.2677 | -45.3103 | 2026-08-07 13:10:00 | GOES-19 | COCOS | BAHIA | Brasil | 2908101 | 29 | 33 | nan | nan | nan | Cerrado | 97.9 |
| ce48cadd-3377-37a5-b1a7-6d0111434d5a | -11.3103 | -44.8337 | 2026-08-07 13:10:00 | GOES-19 | SANTA RITA DE CÁSSIA | BAHIA | Brasil | 2928406 | 29 | 33 | nan | nan | nan | Cerrado | 121.0 |
| 1ca03f79-1cb6-3605-bb69-6cdc5c4b883a | -12.441 | -50.3602 | 2026-08-07 13:10:00 | GOES-19 | FORMOSO DO ARAGUAIA | TOCANTINS | Brasil | 1708205 | 17 | 33 | nan | nan | nan | Cerrado | 77.8 |
| 460c7836-2f8c-332b-a379-52af8110c424 | -11.3099 | -44.8569 | 2026-08-07 13:10:00 | GOES-19 | SANTA RITA DE CÁSSIA | BAHIA | Brasil | 2928406 | 29 | 33 | nan | nan | nan | Cerrado | 63.2 |
| b65df79c-65db-3b87-a9a1-0823f03c52e8 | -13.8236 | -53.7264 | 2026-08-07 13:10:00 | GOES-19 | PARANATINGA | MATO GROSSO | Brasil | 5106307 | 51 | 33 | nan | nan | nan | Cerrado | 262.5 |
| 7e4bf84b-2c5b-3090-a533-5fc64773c274 | -13.8047 | -53.7077 | 2026-08-07 13:10:00 | GOES-19 | PARANATINGA | MATO GROSSO | Brasil | 5106307 | 51 | 33 | nan | nan | nan | Cerrado | 98.1 |
| 9ddd57e1-5cb1-38d9-9422-86bef867c0ef | -12.5554 | -46.9809 | 2026-08-07 13:10:00 | GOES-19 | ARRAIAS | TOCANTINS | Brasil | 1702406 | 17 | 33 | nan | nan | nan | Cerrado | 71.0 |
| a09b0980-99e6-3705-88e5-e66eec554ab9 | -12.4789 | -50.377 | 2026-08-07 13:10:00 | GOES-19 | FORMOSO DO ARAGUAIA | TOCANTINS | Brasil | 1708205 | 17 | 33 | nan | nan | nan | Cerrado | 75.3 |
| 8e4110df-bd64-3ffe-8b76-106fb2387c90 | -14.3431 | -54.9309 | 2026-08-07 13:10:00 | GOES-19 | ROSÁRIO OESTE | MATO GROSSO | Brasil | 5107701 | 51 | 33 | nan | nan | nan | Cerrado | 65.1 |
| 2ece9c73-bee1-3e28-8b93-d19d76924318 | -13.8239 | -53.7055 | 2026-08-07 13:10:00 | GOES-19 | PARANATINGA | MATO GROSSO | Brasil | 5106307 | 51 | 33 | nan | nan | nan | Cerrado | 232.0 |
| e46d6a83-b1ac-3be7-8ac6-e683d1f738c5 | -15.0922 | -52.7708 | 2026-08-07 13:10:00 | GOES-19 | BARRA DO GARÇAS | MATO GROSSO | Brasil | 5101803 | 51 | 33 | nan | nan | nan | Cerrado | 85.6 |
| 576d698e-98b5-3292-9c3c-1a3a01c1ce64 | -13.8047 | -53.7077 | 2026-08-07 13:20:00 | GOES-19 | PARANATINGA | MATO GROSSO | Brasil | 5106307 | 51 | 33 | nan | nan | nan | Cerrado | 72.1 |
| e5921e20-9419-3582-b6d0-8d59ba3f142d | -15.0922 | -52.7708 | 2026-08-07 13:20:00 | GOES-19 | BARRA DO GARÇAS | MATO GROSSO | Brasil | 5101803 | 51 | 33 | nan | nan | nan | Cerrado | 72.2 |
| e5440f22-cab6-3242-8fe6-63117c2f1390 | -13.8236 | -53.7264 | 2026-08-07 13:20:00 | GOES-19 | PARANATINGA | MATO GROSSO | Brasil | 5106307 | 51 | 33 | nan | nan | nan | Cerrado | 292.2 |
| a027f934-a950-3c45-ab13-8f2b52dc4e43 | -14.2677 | -45.3103 | 2026-08-07 13:20:00 | GOES-19 | COCOS | BAHIA | Brasil | 2908101 | 29 | 33 | nan | nan | nan | Cerrado | 80.1 |
| bcfff4e1-f63b-3708-a06d-722f2321beac | -12.441 | -50.3602 | 2026-08-07 13:20:00 | GOES-19 | FORMOSO DO ARAGUAIA | TOCANTINS | Brasil | 1708205 | 17 | 33 | nan | nan | nan | Cerrado | 60.6 |
| 99b84515-0063-3ca1-9401-0ec52b0f372d | -11.2912 | -44.8365 | 2026-08-07 13:20:00 | GOES-19 | SANTA RITA DE CÁSSIA | BAHIA | Brasil | 2928406 | 29 | 33 | nan | nan | nan | Cerrado | 106.0 |
| 1e12f3cc-f21f-35f4-9e05-3df86b076350 | -11.3107 | -44.8105 | 2026-08-07 13:20:00 | GOES-19 | SANTA RITA DE CÁSSIA | BAHIA | Brasil | 2928406 | 29 | 33 | nan | nan | nan | Cerrado | 90.3 |
| 6d65bdb5-8999-3b76-b560-35148c70a7fa | -11.3099 | -44.8569 | 2026-08-07 13:20:00 | GOES-19 | SANTA RITA DE CÁSSIA | BAHIA | Brasil | 2928406 | 29 | 33 | nan | nan | nan | Cerrado | 259.9 |
| e549f264-b969-33ce-b520-6d212045f79f | -13.8239 | -53.7055 | 2026-08-07 13:20:00 | GOES-19 | PARANATINGA | MATO GROSSO | Brasil | 5106307 | 51 | 33 | nan | nan | nan | Cerrado | 191.0 |
| e82e52e2-c0fe-3209-90d3-69c8c356c376 | -11.3103 | -44.8337 | 2026-08-07 13:20:00 | GOES-19 | SANTA RITA DE CÁSSIA | BAHIA | Brasil | 2928406 | 29 | 33 | nan | nan | nan | Cerrado | 496.1 |
| ce151277-a10b-339a-b0e5-5a7a48b69be4 | -6.9092 | -42.4134 | 2026-08-07 13:20:00 | GOES-19 | OEIRAS | PIAUÍ | Brasil | 2207009 | 22 | 33 | nan | nan | nan | Caatinga | 85.6 |
| bbb9b867-19d2-3d42-b9a8-c89eb93e5157 | -11.3103 | -44.8337 | 2026-08-07 13:30:00 | GOES-19 | SANTA RITA DE CÁSSIA | BAHIA | Brasil | 2928406 | 29 | 33 | nan | nan | nan | Cerrado | 240.0 |
| e79d380c-7ef6-3d74-8845-85cc0ac6815e | -6.909 | -42.4372 | 2026-08-07 13:30:00 | GOES-19 | OEIRAS | PIAUÍ | Brasil | 2207009 | 22 | 33 | nan | nan | nan | Caatinga | 83.8 |
| 5c8126c9-87ea-3b23-9f32-095bd039e7c3 | -14.3431 | -54.9309 | 2026-08-07 13:30:00 | GOES-19 | ROSÁRIO OESTE | MATO GROSSO | Brasil | 5107701 | 51 | 33 | nan | nan | nan | Cerrado | 70.5 |
| e908cf83-0abd-3900-914e-dccb15e96a01 | -17.9775 | -44.2865 | 2026-08-07 13:30:00 | GOES-19 | BUENÓPOLIS | MINAS GERAIS | Brasil | 3109204 | 31 | 33 | nan | nan | nan | Cerrado | 103.9 |
| 4ece9854-6158-355e-99c1-2f864fddef7a | -10.4994 | -46.6941 | 2026-08-07 13:30:00 | GOES-19 | MATEIROS | TOCANTINS | Brasil | 1712702 | 17 | 33 | nan | nan | nan | Cerrado | 108.5 |
| c33a7932-af38-33cc-a757-1526d7511389 | -13.8236 | -53.7264 | 2026-08-07 13:30:00 | GOES-19 | PARANATINGA | MATO GROSSO | Brasil | 5106307 | 51 | 33 | nan | nan | nan | Cerrado | 123.9 |
| d768693a-5b57-3b23-9d37-0bfd2c627c79 | -6.9092 | -42.4134 | 2026-08-07 13:30:00 | GOES-19 | OEIRAS | PIAUÍ | Brasil | 2207009 | 22 | 33 | nan | nan | nan | Caatinga | 84.8 |
| 27dbbc77-67bf-33c5-9db9-49077e432f4c | -13.8239 | -53.7055 | 2026-08-07 13:30:00 | GOES-19 | PARANATINGA | MATO GROSSO | Brasil | 5106307 | 51 | 33 | nan | nan | nan | Cerrado | 108.2 |
| 0f75f848-9aca-316b-9238-6d0f58ef56ac | -11.3099 | -44.8569 | 2026-08-07 13:30:00 | GOES-19 | SANTA RITA DE CÁSSIA | BAHIA | Brasil | 2928406 | 29 | 33 | nan | nan | nan | Cerrado | 128.5 |
| 7452b851-e297-3503-9a87-ffde0e96d6ba | -14.2677 | -45.3103 | 2026-08-07 13:30:00 | GOES-19 | COCOS | BAHIA | Brasil | 2908101 | 29 | 33 | nan | nan | nan | Cerrado | 79.3 |
| 5990b935-029b-3561-8d23-795ad87cf757 | -12.441 | -50.3602 | 2026-08-07 13:30:00 | GOES-19 | FORMOSO DO ARAGUAIA | TOCANTINS | Brasil | 1708205 | 17 | 33 | nan | nan | nan | Cerrado | 69.9 |
| f2fa23ea-3888-3684-88f0-20f301448260 | -6.9092 | -42.4134 | 2026-08-07 13:40:00 | GOES-19 | OEIRAS | PIAUÍ | Brasil | 2207009 | 22 | 33 | nan | nan | nan | Caatinga | 96.2 |
| b3407721-5e2d-3f37-bdaa-1250cdfb8281 | -6.909 | -42.4372 | 2026-08-07 13:40:00 | GOES-19 | OEIRAS | PIAUÍ | Brasil | 2207009 | 22 | 33 | nan | nan | nan | Caatinga | 96.7 |
| 52ac4a51-d574-3997-8aab-1d8568719005 | -13.8236 | -53.7264 | 2026-08-07 13:40:00 | GOES-19 | PARANATINGA | MATO GROSSO | Brasil | 5106307 | 51 | 33 | nan | nan | nan | Cerrado | 101.7 |
| 0a7555ca-5128-3407-8e86-4728e30de712 | -11.3103 | -44.8337 | 2026-08-07 13:40:00 | GOES-19 | SANTA RITA DE CÁSSIA | BAHIA | Brasil | 2928406 | 29 | 33 | nan | nan | nan | Cerrado | 107.6 |
| 0ec46f3a-b452-35cb-91d7-83e298d73e92 | -6.9791 | -42.9034 | 2026-08-07 13:40:00 | GOES-19 | FLORIANO | PIAUÍ | Brasil | 2203909 | 22 | 33 | nan | nan | nan | Caatinga | 91.9 |
| 8d558fc7-c085-34df-b365-ea943c6e21e2 | -10.4994 | -46.6941 | 2026-08-07 13:40:00 | GOES-19 | MATEIROS | TOCANTINS | Brasil | 1712702 | 17 | 33 | nan | nan | nan | Cerrado | 95.2 |
| a4718e42-f2ff-35b3-96e5-baf21e09dbb0 | -14.3431 | -54.9309 | 2026-08-07 13:40:00 | GOES-19 | ROSÁRIO OESTE | MATO GROSSO | Brasil | 5107701 | 51 | 33 | nan | nan | nan | Cerrado | 102.9 |
| a30fd5aa-96db-3522-976f-3487d466a951 | -14.3434 | -54.9103 | 2026-08-07 13:40:00 | GOES-19 | ROSÁRIO OESTE | MATO GROSSO | Brasil | 5107701 | 51 | 33 | nan | nan | nan | Cerrado | 63.8 |
| 7655f15d-8ebb-39ba-92ee-3b4b73ca5763 | -13.8239 | -53.7055 | 2026-08-07 13:40:00 | GOES-19 | PARANATINGA | MATO GROSSO | Brasil | 5106307 | 51 | 33 | nan | nan | nan | Cerrado | 81.8 |
| 4742bc87-246c-399c-9a54-039bd5039fa1 | -12.441 | -50.3602 | 2026-08-07 13:40:00 | GOES-19 | FORMOSO DO ARAGUAIA | TOCANTINS | Brasil | 1708205 | 17 | 33 | nan | nan | nan | Cerrado | 63.7 |
| f253b904-08fa-3a9c-a7d7-97ff2601f496 | -11.3107 | -44.8105 | 2026-08-07 13:50:00 | GOES-19 | SANTA RITA DE CÁSSIA | BAHIA | Brasil | 2928406 | 29 | 33 | nan | nan | nan | Cerrado | 86.6 |
| cffe77ce-1a7b-33e0-84ce-e44622f6b688 | -6.9979 | -42.9016 | 2026-08-07 13:50:00 | GOES-19 | FLORIANO | PIAUÍ | Brasil | 2203909 | 22 | 33 | nan | nan | nan | Caatinga | 100.2 |
| ab62be17-549d-3109-aa75-889b36a05458 | -12.441 | -50.3602 | 2026-08-07 13:50:00 | GOES-19 | FORMOSO DO ARAGUAIA | TOCANTINS | Brasil | 1708205 | 17 | 33 | nan | nan | nan | Cerrado | 84.9 |
| 2538ce35-6290-3b24-83d0-91f4179d8e58 | -6.9092 | -42.4134 | 2026-08-07 13:50:00 | GOES-19 | OEIRAS | PIAUÍ | Brasil | 2207009 | 22 | 33 | nan | nan | nan | Caatinga | 89.0 |
| c5225073-9273-307a-91b5-c3e216441b9e | -11.3103 | -44.8337 | 2026-08-07 13:50:00 | GOES-19 | SANTA RITA DE CÁSSIA | BAHIA | Brasil | 2928406 | 29 | 33 | nan | nan | nan | Cerrado | 215.0 |
| cd8a7e0f-bfc9-3f15-ac38-bffef68d4690 | -6.909 | -42.4372 | 2026-08-07 13:50:00 | GOES-19 | OEIRAS | PIAUÍ | Brasil | 2207009 | 22 | 33 | nan | nan | nan | Caatinga | 94.5 |
| ead2d31a-250c-3da3-8e11-90a59c1c4306 | -12.5554 | -46.9809 | 2026-08-07 13:50:00 | GOES-19 | ARRAIAS | TOCANTINS | Brasil | 1702406 | 17 | 33 | nan | nan | nan | Cerrado | 82.0 |
| d7aeba81-c3ef-3c69-8fd4-fb5de96386f3 | -10.4994 | -46.6941 | 2026-08-07 13:50:00 | GOES-19 | MATEIROS | TOCANTINS | Brasil | 1712702 | 17 | 33 | nan | nan | nan | Cerrado | 84.3 |
| d49647ee-6349-3756-a465-5d9e2cb7d0a8 | -12.5754 | -46.9329 | 2026-08-07 13:50:00 | GOES-19 | ARRAIAS | TOCANTINS | Brasil | 1702406 | 17 | 33 | nan | nan | nan | Cerrado | 92.9 |
| 3ce6b67e-b411-3557-a549-eb835aafbe66 | -14.3431 | -54.9309 | 2026-08-07 13:50:00 | GOES-19 | ROSÁRIO OESTE | MATO GROSSO | Brasil | 5107701 | 51 | 33 | nan | nan | nan | Cerrado | 69.9 |
| 10e51ebd-e601-3303-97a7-92ef3d53aac0 | -9.2918 | -60.9228 | 2026-08-07 13:50:00 | GOES-19 | COLNIZA | MATO GROSSO | Brasil | 5103254 | 51 | 33 | nan | nan | nan | Amazônia | 75.3 |
| 5b32b8c3-a20c-3cd4-9fcc-43767be55b94 | -12.5562 | -46.9357 | 2026-08-07 13:50:00 | GOES-19 | ARRAIAS | TOCANTINS | Brasil | 1702406 | 17 | 33 | nan | nan | nan | Cerrado | 86.7 |
| c9b9dc5b-4203-3850-b6f2-43a221cf380e | -11.3099 | -44.8569 | 2026-08-07 13:50:00 | GOES-19 | SANTA RITA DE CÁSSIA | BAHIA | Brasil | 2928406 | 29 | 33 | nan | nan | nan | Cerrado | 154.1 |
| 1822d439-01fb-3b58-a550-3fee506a2f35 | -6.9791 | -42.9034 | 2026-08-07 13:50:00 | GOES-19 | FLORIANO | PIAUÍ | Brasil | 2203909 | 22 | 33 | nan | nan | nan | Caatinga | 103.3 |
| 354f1723-93c4-3eb5-8f4f-020cf85163eb | -11.3845 | -47.2535 | 2026-08-07 13:50:00 | GOES-19 | ALMAS | TOCANTINS | Brasil | 1700400 | 17 | 33 | nan | nan | nan | Cerrado | 71.6 |
| f3018b66-b199-37a2-80be-1991484b32eb | -6.8901 | -42.439 | 2026-08-07 14:00:00 | GOES-19 | CAJAZEIRAS DO PIAUÍ | PIAUÍ | Brasil | 2202075 | 22 | 33 | nan | nan | nan | Caatinga | 80.3 |
| 70162315-5d69-3419-87e5-d2347e2a019c | -14.3232 | -54.9744 | 2026-08-07 14:00:00 | GOES-19 | ROSÁRIO OESTE | MATO GROSSO | Brasil | 5107701 | 51 | 33 | nan | nan | nan | Cerrado | 91.0 |
| e74591da-a161-3d1b-8f60-bad179274a4f | -14.3431 | -54.9309 | 2026-08-07 14:00:00 | GOES-19 | ROSÁRIO OESTE | MATO GROSSO | Brasil | 5107701 | 51 | 33 | nan | nan | nan | Cerrado | 98.6 |
| e61084fa-0cb2-3819-ac6c-617cfb979512 | -11.3845 | -47.2535 | 2026-08-07 14:00:00 | GOES-19 | ALMAS | TOCANTINS | Brasil | 1700400 | 17 | 33 | nan | nan | nan | Cerrado | 87.6 |
| 31947641-061e-3a7d-8d2f-7ddd617b16bf | -12.4789 | -50.377 | 2026-08-07 14:00:00 | GOES-19 | FORMOSO DO ARAGUAIA | TOCANTINS | Brasil | 1708205 | 17 | 33 | nan | nan | nan | Cerrado | 82.0 |
| 14508cc0-1f57-30e8-967c-f146e5f36ec5 | -11.3099 | -44.8569 | 2026-08-07 14:00:00 | GOES-19 | SANTA RITA DE CÁSSIA | BAHIA | Brasil | 2928406 | 29 | 33 | nan | nan | nan | Cerrado | 410.1 |
| 00d6a339-6518-3ef4-b50b-0321bc3861a5 | -14.2677 | -45.3103 | 2026-08-07 14:00:00 | GOES-19 | COCOS | BAHIA | Brasil | 2908101 | 29 | 33 | nan | nan | nan | Cerrado | 80.6 |
| 091529a2-e893-37a6-8832-7f16cd0a6ad2 | -11.3103 | -44.8337 | 2026-08-07 14:00:00 | GOES-19 | SANTA RITA DE CÁSSIA | BAHIA | Brasil | 2928406 | 29 | 33 | nan | nan | nan | Cerrado | 469.3 |
| 0aa1dc44-240f-366e-b89e-c02d0dc4c68f | -9.2918 | -60.9228 | 2026-08-07 14:00:00 | GOES-19 | COLNIZA | MATO GROSSO | Brasil | 5103254 | 51 | 33 | nan | nan | nan | Amazônia | 58.9 |
| c482e637-5682-3cb6-a2f7-4102bca050ca | -11.2912 | -44.8365 | 2026-08-07 14:00:00 | GOES-19 | SANTA RITA DE CÁSSIA | BAHIA | Brasil | 2928406 | 29 | 33 | nan | nan | nan | Cerrado | 98.3 |
| 442f39b1-0390-356b-83c3-df7f2cb0c2f5 | -12.4601 | -50.3578 | 2026-08-07 14:00:00 | GOES-19 | FORMOSO DO ARAGUAIA | TOCANTINS | Brasil | 1708205 | 17 | 33 | nan | nan | nan | Cerrado | 73.9 |
| 64073a6c-186b-3801-b063-19ba82ab8fe6 | -11.3107 | -44.8105 | 2026-08-07 14:00:00 | GOES-19 | SANTA RITA DE CÁSSIA | BAHIA | Brasil | 2928406 | 29 | 33 | nan | nan | nan | Cerrado | 93.3 |
| f30d8a51-aa81-357c-9235-186c837425f3 | -6.9092 | -42.4134 | 2026-08-07 14:00:00 | GOES-19 | OEIRAS | PIAUÍ | Brasil | 2207009 | 22 | 33 | nan | nan | nan | Caatinga | 81.9 |
| 033fe7b9-7992-3707-98e1-9de623e8f53b | -12.441 | -50.3602 | 2026-08-07 14:00:00 | GOES-19 | FORMOSO DO ARAGUAIA | TOCANTINS | Brasil | 1708205 | 17 | 33 | nan | nan | nan | Cerrado | 83.8 |


[Clique aqui para ver as próximas entradas](README28.md)
