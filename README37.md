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

## Dados Diários - Página 37

| ID | Latitude | Longitude | Data/Hora GMT | Satélite | Município | Estado | País | Município ID | Estado ID | País ID | Dias sem Chuva | Precipitação | Risco de Fogo | Bioma | FRP |
|----|----------|-----------|---------------|----------|-----------|--------|------|--------------|-----------|---------|----------------|--------------|----------------|-------|-----|
| e05b4199-d73e-3f17-a2b3-7fa01ee35d72 | -12.1027 | -50.0355 | 2026-09-26 15:10:00 | GOES-19 | SANDOLÂNDIA | TOCANTINS | Brasil | 1718840 | 17 | 33 | nan | nan | nan | Cerrado | 92.5 |
| cd5e0458-5f24-3742-adf6-104e9134e0d9 | -14.7485 | -45.5725 | 2026-09-26 15:10:00 | GOES-19 | COCOS | BAHIA | Brasil | 2908101 | 29 | 33 | nan | nan | nan | Cerrado | 100.4 |
| 3fa440cd-e4a6-3b34-b1f1-220efa9fabe1 | 1.6018 | -55.8446 | 2026-09-26 15:10:00 | GOES-19 | ORIXIMINÁ | PARÁ | Brasil | 1505304 | 15 | 33 | nan | nan | nan | Amazônia | 83.1 |
| 789ef81f-3437-3b39-9244-5787dedff71e | -12.9457 | -51.0695 | 2026-09-26 15:10:00 | GOES-19 | COCALINHO | MATO GROSSO | Brasil | 5103106 | 51 | 33 | nan | nan | nan | Cerrado | 126.7 |
| 87495d26-36c7-3711-83ad-67cc875fa504 | -11.7887 | -50.6521 | 2026-09-26 15:10:00 | GOES-19 | FORMOSO DO ARAGUAIA | TOCANTINS | Brasil | 1708205 | 17 | 33 | nan | nan | nan | Cerrado | 97.9 |
| 7a9dc9aa-8f91-3b8e-8560-26f2d857b3bc | -15.9265 | -56.2719 | 2026-09-26 15:10:00 | GOES-19 | NOSSA SENHORA DO LIVRAMENTO | MATO GROSSO | Brasil | 5106109 | 51 | 33 | nan | nan | nan | Pantanal | 48.7 |
| 6fb449da-a28e-3f18-876d-fbf15f25f70c | -13.6949 | -48.82 | 2026-09-26 15:10:00 | GOES-19 | FORMOSO | GOIÁS | Brasil | 5208103 | 52 | 33 | nan | nan | nan | Cerrado | 87.6 |
| 7226dc15-9bf7-3c61-bf17-46fbd4e10e4d | -14.6893 | -45.6064 | 2026-09-26 15:10:00 | GOES-19 | COCOS | BAHIA | Brasil | 2908101 | 29 | 33 | nan | nan | nan | Cerrado | 157.0 |
| 342d803b-43a0-342f-bdc9-1d98e03f58a3 | -11.8014 | -49.8129 | 2026-09-26 15:10:00 | GOES-19 | FORMOSO DO ARAGUAIA | TOCANTINS | Brasil | 1708205 | 17 | 33 | nan | nan | nan | Cerrado | 126.2 |
| fcb0c65b-7eb1-385f-8dc6-e750c832e506 | 1.6382 | -55.982 | 2026-09-26 15:10:00 | GOES-19 | ORIXIMINÁ | PARÁ | Brasil | 1505304 | 15 | 33 | nan | nan | nan | Amazônia | 69.6 |
| 96fb3b29-e5a8-36e2-a569-3a1e9496d46f | -11.1183 | -54.0062 | 2026-09-26 15:10:00 | GOES-19 | MARCELÂNDIA | MATO GROSSO | Brasil | 5105580 | 51 | 33 | nan | nan | nan | Amazônia | 102.8 |
| f726cc74-8e0c-311d-ab9b-f13da1215ab5 | -13.7142 | -48.8172 | 2026-09-26 15:10:00 | GOES-19 | FORMOSO | GOIÁS | Brasil | 5208103 | 52 | 33 | nan | nan | nan | Cerrado | 150.7 |
| 0ff8f6f4-ca5e-371b-8a6c-78422b8dddc6 | -10.4234 | -53.8014 | 2026-09-26 15:10:00 | GOES-19 | PEIXOTO DE AZEVEDO | MATO GROSSO | Brasil | 5106422 | 51 | 33 | nan | nan | nan | Amazônia | 89.4 |
| bb23d4fa-36dd-36df-bd67-0dfc265a2dbc | 2.023 | -55.8587 | 2026-09-26 15:10:00 | GOES-19 | ÓBIDOS | PARÁ | Brasil | 1505106 | 15 | 33 | nan | nan | nan | Amazônia | 57.5 |
| 0a2a0b4f-d114-34fe-aaca-94a9053d719b | -10.4232 | -53.8219 | 2026-09-26 15:10:00 | GOES-19 | PEIXOTO DE AZEVEDO | MATO GROSSO | Brasil | 5106422 | 51 | 33 | nan | nan | nan | Amazônia | 72.6 |
| 544c09ab-3483-317c-842d-c1c25b57bfd3 | -14.7284 | -45.5993 | 2026-09-26 15:10:00 | GOES-19 | COCOS | BAHIA | Brasil | 2908101 | 29 | 33 | nan | nan | nan | Cerrado | 119.8 |
| f6bc9981-b957-385f-abd1-a0760227ba93 | -13.6953 | -48.7979 | 2026-09-26 15:10:00 | GOES-19 | FORMOSO | GOIÁS | Brasil | 5208103 | 52 | 33 | nan | nan | nan | Cerrado | 73.3 |
| e1f19b34-0f30-3d96-a2ac-58e751b202db | 2.145 | -50.8784 | 2026-09-26 15:10:00 | GOES-19 | AMAPÁ | AMAPÁ | Brasil | 1600105 | 16 | 33 | nan | nan | nan | Amazônia | 79.4 |
| 1146473c-e230-3c84-ac38-d50cb373e1f6 | 1.5834 | -55.9236 | 2026-09-26 15:10:00 | GOES-19 | ORIXIMINÁ | PARÁ | Brasil | 1505304 | 15 | 33 | nan | nan | nan | Amazônia | 63.3 |
| 3adb627a-26f3-39c5-90dd-e5a93607d644 | -2.9579 | -50.3988 | 2026-09-26 15:10:00 | GOES-19 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 84.2 |
| d0e66dba-ec68-3ce8-96ad-293d1dff7014 | -0.84 | -48.6394 | 2026-09-26 15:10:00 | GOES-19 | SALVATERRA | PARÁ | Brasil | 1506302 | 15 | 33 | nan | nan | nan | Amazônia | 51.2 |
| f580e986-a36c-35c3-86d3-f83e929f3f72 | -12.8059 | -54.0255 | 2026-09-26 15:10:00 | GOES-19 | PARANATINGA | MATO GROSSO | Brasil | 5106307 | 51 | 33 | nan | nan | nan | Amazônia | 63.8 |
| 6d588908-8322-3ebc-949c-9e9f773a5ecb | 1.2794 | -50.851 | 2026-09-26 15:10:00 | GOES-19 | TARTARUGALZINHO | AMAPÁ | Brasil | 1600709 | 16 | 33 | nan | nan | nan | Amazônia | 91.5 |
| ade25ee2-5228-3a12-a662-613f2d63afdb | -10.7114 | -60.7505 | 2026-09-26 15:10:00 | GOES-19 | RONDOLÂNDIA | MATO GROSSO | Brasil | 5107578 | 51 | 33 | nan | nan | nan | Amazônia | 69.2 |
| 367f4dc0-c5a6-326f-a808-ae9a990b3e65 | -8.36 | -44.16 | 2026-09-26 15:15:00 | MSG-03 | MANOEL EMÍDIO | PIAUÍ | Brasil | 2205904 | 22 | 33 | nan | nan | nan | Cerrado | nan |
| 784241ce-a884-3213-a447-75abbebb0ca2 | -8.36 | -44.2 | 2026-09-26 15:15:00 | MSG-03 | MANOEL EMÍDIO | PIAUÍ | Brasil | 2205904 | 22 | 33 | nan | nan | nan | Cerrado | nan |
| 84b976d4-4348-3078-9c94-aaedc3e3010b | -10.7115 | -60.7312 | 2026-09-26 15:20:00 | GOES-19 | RONDOLÂNDIA | MATO GROSSO | Brasil | 5107578 | 51 | 33 | nan | nan | nan | Amazônia | 67.0 |
| fa7460ac-856b-352d-baeb-d20c7c000732 | -12.8059 | -54.0255 | 2026-09-26 15:20:00 | GOES-19 | PARANATINGA | MATO GROSSO | Brasil | 5106307 | 51 | 33 | nan | nan | nan | Amazônia | 69.0 |
| f4303243-3958-349d-bdd5-5ae524fb22cf | -12.5883 | -51.9406 | 2026-09-26 15:20:00 | GOES-19 | RIBEIRÃO CASCALHEIRA | MATO GROSSO | Brasil | 5107180 | 51 | 33 | nan | nan | nan | Amazônia | 81.0 |
| 4fee519e-b73a-3516-a51b-56cfaa11f3bf | -10.4232 | -53.8219 | 2026-09-26 15:20:00 | GOES-19 | PEIXOTO DE AZEVEDO | MATO GROSSO | Brasil | 5106422 | 51 | 33 | nan | nan | nan | Amazônia | 75.3 |
| 5c8cd77f-2abf-3ba2-a99d-7b643006efe6 | 1.6018 | -55.8446 | 2026-09-26 15:20:00 | GOES-19 | ORIXIMINÁ | PARÁ | Brasil | 1505304 | 15 | 33 | nan | nan | nan | Amazônia | 80.1 |
| 26522790-c6f3-3cea-b1ad-9c80cb8e0271 | -12.9461 | -51.0481 | 2026-09-26 15:20:00 | GOES-19 | COCALINHO | MATO GROSSO | Brasil | 5103106 | 51 | 33 | nan | nan | nan | Cerrado | 78.3 |
| 8e91dd92-0dca-3a23-9864-11aa8236be50 | -10.4046 | -53.803 | 2026-09-26 15:20:00 | GOES-19 | PEIXOTO DE AZEVEDO | MATO GROSSO | Brasil | 5106422 | 51 | 33 | nan | nan | nan | Amazônia | 74.8 |
| c8149c9f-45be-37af-a336-9752b7b70a68 | -13.4016 | -51.3114 | 2026-09-26 15:20:00 | GOES-19 | COCALINHO | MATO GROSSO | Brasil | 5103106 | 51 | 33 | nan | nan | nan | Cerrado | 62.5 |
| 8c8e22e7-01b8-3531-9ea5-90edf46adfd3 | -11.637 | -50.6267 | 2026-09-26 15:20:00 | GOES-19 | FORMOSO DO ARAGUAIA | TOCANTINS | Brasil | 1708205 | 17 | 33 | nan | nan | nan | Cerrado | 100.2 |
| beed3895-b9e3-38a4-b300-c6b0d7a1161a | -12.6608 | -50.9549 | 2026-09-26 15:20:00 | GOES-19 | RIBEIRÃO CASCALHEIRA | MATO GROSSO | Brasil | 5107180 | 51 | 33 | nan | nan | nan | Cerrado | 78.0 |
| 7ef7bce2-b80a-394b-ac9c-afc57695415b | -11.6561 | -50.6245 | 2026-09-26 15:20:00 | GOES-19 | FORMOSO DO ARAGUAIA | TOCANTINS | Brasil | 1708205 | 17 | 33 | nan | nan | nan | Cerrado | 106.9 |
| b02ff6d6-5757-3cad-a07a-b22711cf4133 | -13.2057 | -51.5703 | 2026-09-26 15:20:00 | GOES-19 | RIBEIRÃO CASCALHEIRA | MATO GROSSO | Brasil | 5107180 | 51 | 33 | nan | nan | nan | Cerrado | 81.7 |
| 43d6d819-1b48-3e83-9f54-1512c3c4b6d7 | 1.2978 | -50.8507 | 2026-09-26 15:20:00 | GOES-19 | TARTARUGALZINHO | AMAPÁ | Brasil | 1600709 | 16 | 33 | nan | nan | nan | Amazônia | 91.7 |
| daa37d59-42f2-39f5-9b93-66c55c47ba09 | -10.4234 | -53.8014 | 2026-09-26 15:20:00 | GOES-19 | PEIXOTO DE AZEVEDO | MATO GROSSO | Brasil | 5106422 | 51 | 33 | nan | nan | nan | Amazônia | 94.1 |
| edae1d4c-9602-3ef1-a4d1-a68587e8d5a8 | -11.1183 | -54.0062 | 2026-09-26 15:20:00 | GOES-19 | MARCELÂNDIA | MATO GROSSO | Brasil | 5105580 | 51 | 33 | nan | nan | nan | Amazônia | 103.0 |
| a54b92c2-35a0-33e1-8712-dc74bb4f2d93 | 1.1507 | -50.7275 | 2026-09-26 15:20:00 | GOES-19 | TARTARUGALZINHO | AMAPÁ | Brasil | 1600709 | 16 | 33 | nan | nan | nan | Amazônia | 96.0 |
| f7bd03dd-ab81-3524-9dac-5f7a7b3bfcd9 | -0.84 | -48.6394 | 2026-09-26 15:20:00 | GOES-19 | SALVATERRA | PARÁ | Brasil | 1506302 | 15 | 33 | nan | nan | nan | Amazônia | 53.7 |
| 95856d6a-8a6c-3ab8-a5da-a1812f189464 | -14.7671 | -45.6155 | 2026-09-26 15:20:00 | GOES-19 | COCOS | BAHIA | Brasil | 2908101 | 29 | 33 | nan | nan | nan | Cerrado | 152.0 |
| bfe1f28e-db91-38ef-9c30-4c5b9e1f473c | 1.5835 | -55.8448 | 2026-09-26 15:20:00 | GOES-19 | ORIXIMINÁ | PARÁ | Brasil | 1505304 | 15 | 33 | nan | nan | nan | Amazônia | 82.3 |
| 0c5795d0-684c-388b-808a-7de022c8fabb | -11.0802 | -54.0302 | 2026-09-26 15:20:00 | GOES-19 | MARCELÂNDIA | MATO GROSSO | Brasil | 5105580 | 51 | 33 | nan | nan | nan | Amazônia | 61.3 |
| 7e39f60c-99f6-3966-b95f-37df29cd354c | 1.6565 | -55.9621 | 2026-09-26 15:20:00 | GOES-19 | ORIXIMINÁ | PARÁ | Brasil | 1505304 | 15 | 33 | nan | nan | nan | Amazônia | 68.7 |
| 78d6ca4b-8f71-3f38-a117-1b4dc409b9c3 | -11.9352 | -49.7752 | 2026-09-26 15:20:00 | GOES-19 | FORMOSO DO ARAGUAIA | TOCANTINS | Brasil | 1708205 | 17 | 33 | nan | nan | nan | Cerrado | 100.1 |
| fab272f3-a50f-3305-9b52-c9cff515cdb3 | -1.135 | -48.8928 | 2026-09-26 15:20:00 | GOES-19 | CACHOEIRA DO ARARI | PARÁ | Brasil | 1502004 | 15 | 33 | nan | nan | nan | Amazônia | 54.7 |
| 21377733-7471-359f-b46b-427a81078280 | -14.748 | -45.5958 | 2026-09-26 15:20:00 | GOES-19 | COCOS | BAHIA | Brasil | 2908101 | 29 | 33 | nan | nan | nan | Cerrado | 141.9 |
| 73a9576d-f259-385e-90b2-10b260bc6327 | 1.4452 | -50.828 | 2026-09-26 15:20:00 | GOES-19 | TARTARUGALZINHO | AMAPÁ | Brasil | 1600709 | 16 | 33 | nan | nan | nan | Amazônia | 80.0 |
| ebbe127d-3b47-35ad-945f-db2bc4b9f7ee | 1.5649 | -56.042 | 2026-09-26 15:20:00 | GOES-19 | ORIXIMINÁ | PARÁ | Brasil | 1505304 | 15 | 33 | nan | nan | nan | Amazônia | 68.9 |
| b99bbc70-4492-32e0-96f7-479134c990b6 | 1.6383 | -55.9427 | 2026-09-26 15:20:00 | GOES-19 | ORIXIMINÁ | PARÁ | Brasil | 1505304 | 15 | 33 | nan | nan | nan | Amazônia | 75.7 |
| d5a9d816-8d36-38e3-a0bc-d3b70536b0cb | -15.9265 | -56.2719 | 2026-09-26 15:20:00 | GOES-19 | NOSSA SENHORA DO LIVRAMENTO | MATO GROSSO | Brasil | 5106109 | 51 | 33 | nan | nan | nan | Pantanal | 45.5 |
| ea67aedc-01fc-373a-a2c1-17deaab3f496 | -11.6751 | -50.6224 | 2026-09-26 15:20:00 | GOES-19 | FORMOSO DO ARAGUAIA | TOCANTINS | Brasil | 1708205 | 17 | 33 | nan | nan | nan | Cerrado | 108.3 |
| b2048e46-e430-302d-9c3c-eb8f8005386b | -12.6075 | -51.9384 | 2026-09-26 15:20:00 | GOES-19 | RIBEIRÃO CASCALHEIRA | MATO GROSSO | Brasil | 5107180 | 51 | 33 | nan | nan | nan | Amazônia | 94.6 |
| 9e52d903-e517-3220-955e-db9454ff355c | -11.6377 | -50.5839 | 2026-09-26 15:20:00 | GOES-19 | FORMOSO DO ARAGUAIA | TOCANTINS | Brasil | 1708205 | 17 | 33 | nan | nan | nan | Cerrado | 128.8 |
| 63fdd08b-adc5-315a-ac0b-46e22029a0d1 | -13.7146 | -48.7951 | 2026-09-26 15:20:00 | GOES-19 | FORMOSO | GOIÁS | Brasil | 5208103 | 52 | 33 | nan | nan | nan | Cerrado | 85.1 |
| f8aa558a-f4eb-32d7-a219-73f38f364e73 | -13.4012 | -51.3328 | 2026-09-26 15:20:00 | GOES-19 | COCALINHO | MATO GROSSO | Brasil | 5103106 | 51 | 33 | nan | nan | nan | Cerrado | 72.2 |
| d1ff59cb-35a9-350d-979b-6e1d9fcf4cd9 | -11.118 | -54.0268 | 2026-09-26 15:20:00 | GOES-19 | MARCELÂNDIA | MATO GROSSO | Brasil | 5105580 | 51 | 33 | nan | nan | nan | Amazônia | 96.5 |
| 3b70ddeb-ff09-3ec4-a3c8-a43d5a7213a5 | -12.9457 | -51.0695 | 2026-09-26 15:20:00 | GOES-19 | COCALINHO | MATO GROSSO | Brasil | 5103106 | 51 | 33 | nan | nan | nan | Cerrado | 223.4 |
| bd81e851-bccf-3495-b20c-5e1047be5517 | -12.0365 | -50.6233 | 2026-09-26 15:20:00 | GOES-19 | FORMOSO DO ARAGUAIA | TOCANTINS | Brasil | 1708205 | 17 | 33 | nan | nan | nan | Cerrado | 96.7 |
| 27117452-e522-3f10-9177-19416df08c5c | 2.1083 | -50.8375 | 2026-09-26 15:20:00 | GOES-19 | AMAPÁ | AMAPÁ | Brasil | 1600105 | 16 | 33 | nan | nan | nan | Amazônia | 85.5 |
| aecf7c71-1f90-3922-83f1-4c3061b91856 | -0.821 | -49.1304 | 2026-09-26 15:20:00 | GOES-19 | CACHOEIRA DO ARARI | PARÁ | Brasil | 1502004 | 15 | 33 | nan | nan | nan | Amazônia | 83.3 |
| 63f2240a-67e6-3fe0-9577-79ce8cca755e | 1.51 | -56.0032 | 2026-09-26 15:20:00 | GOES-19 | ORIXIMINÁ | PARÁ | Brasil | 1505304 | 15 | 33 | nan | nan | nan | Amazônia | 65.1 |
| 1901a643-861a-3668-9460-dd86991ffce4 | -11.8659 | -50.5791 | 2026-09-26 15:20:00 | GOES-19 | FORMOSO DO ARAGUAIA | TOCANTINS | Brasil | 1708205 | 17 | 33 | nan | nan | nan | Cerrado | 105.0 |
| 422c5ed4-6a21-3227-b734-0425aafc54d8 | -10.8532 | -54.0916 | 2026-09-26 15:20:00 | GOES-19 | MARCELÂNDIA | MATO GROSSO | Brasil | 5105580 | 51 | 33 | nan | nan | nan | Amazônia | 74.2 |
| 68e165d9-70f3-37c7-b081-693e5345dcb3 | 2.145 | -50.8784 | 2026-09-26 15:20:00 | GOES-19 | AMAPÁ | AMAPÁ | Brasil | 1600105 | 16 | 33 | nan | nan | nan | Amazônia | 80.2 |
| 0d70eca7-fd3a-3ea1-afde-60ec411943a4 | -11.1924 | -54.1225 | 2026-09-26 15:20:00 | GOES-19 | MARCELÂNDIA | MATO GROSSO | Brasil | 5105580 | 51 | 33 | nan | nan | nan | Amazônia | 68.0 |
| 5e2f41b1-b111-3ffa-a70f-0cc703e1d704 | -6.221 | -41.641 | 2026-09-26 15:20:00 | GOES-19 | PIMENTEIRAS | PIAUÍ | Brasil | 2208106 | 22 | 33 | nan | nan | nan | Caatinga | 88.0 |
| 8168aaef-559f-3fd4-a470-61574cf609ca | -12.0171 | -50.647 | 2026-09-26 15:20:00 | GOES-19 | FORMOSO DO ARAGUAIA | TOCANTINS | Brasil | 1708205 | 17 | 33 | nan | nan | nan | Cerrado | 87.0 |
| 66cb714d-3369-3e3a-8643-20582fe56efc | -12.6608 | -50.9549 | 2026-09-26 15:30:00 | GOES-19 | RIBEIRÃO CASCALHEIRA | MATO GROSSO | Brasil | 5107180 | 51 | 33 | nan | nan | nan | Cerrado | 78.1 |
| 97bbdb19-a168-3998-b318-deb8f68a3ae7 | -11.3031 | -51.4281 | 2026-09-26 15:30:00 | GOES-19 | SÃO FÉLIX DO ARAGUAIA | MATO GROSSO | Brasil | 5107859 | 51 | 33 | nan | nan | nan | Cerrado | 87.8 |
| 77e6a037-27bf-3084-b953-2ec17ab869e0 | -12.2696 | -50.3381 | 2026-09-26 15:30:00 | GOES-19 | FORMOSO DO ARAGUAIA | TOCANTINS | Brasil | 1708205 | 17 | 33 | nan | nan | nan | Cerrado | 114.0 |
| d7115baf-0456-3b14-8c74-44ad75c2cbad | -6.2024 | -41.6187 | 2026-09-26 15:30:00 | GOES-19 | PIMENTEIRAS | PIAUÍ | Brasil | 2208106 | 22 | 33 | nan | nan | nan | Caatinga | 161.6 |
| c97fa712-99ed-36c4-9941-7eff6c89785b | 1.6383 | -55.9427 | 2026-09-26 15:30:00 | GOES-19 | ORIXIMINÁ | PARÁ | Brasil | 1505304 | 15 | 33 | nan | nan | nan | Amazônia | 88.1 |
| 6ef83424-5382-3519-ac67-ea43c2c23f47 | -11.8665 | -50.5362 | 2026-09-26 15:30:00 | GOES-19 | FORMOSO DO ARAGUAIA | TOCANTINS | Brasil | 1708205 | 17 | 33 | nan | nan | nan | Cerrado | 139.9 |
| 0e61ba2d-9c1f-3052-ad6f-497480f10f29 | -11.6751 | -50.6224 | 2026-09-26 15:30:00 | GOES-19 | FORMOSO DO ARAGUAIA | TOCANTINS | Brasil | 1708205 | 17 | 33 | nan | nan | nan | Cerrado | 89.4 |
| 58a1e800-9f32-3649-9d67-bd7d761a5509 | -10.8532 | -54.0916 | 2026-09-26 15:30:00 | GOES-19 | MARCELÂNDIA | MATO GROSSO | Brasil | 5105580 | 51 | 33 | nan | nan | nan | Amazônia | 85.1 |
| d6cbeca2-f600-3ffd-b80b-386a08c30952 | -11.9228 | -50.5938 | 2026-09-26 15:30:00 | GOES-19 | FORMOSO DO ARAGUAIA | TOCANTINS | Brasil | 1708205 | 17 | 33 | nan | nan | nan | Cerrado | 74.8 |
| 0cb55d20-8e96-3b5c-832c-faf5efe9c3a7 | -1.116 | -49.2338 | 2026-09-26 15:30:00 | GOES-19 | MUANÁ | PARÁ | Brasil | 1504901 | 15 | 33 | nan | nan | nan | Amazônia | 71.3 |
| aa2125af-be22-3807-8f31-92f4ff99dce2 | -6.2213 | -41.617 | 2026-09-26 15:30:00 | GOES-19 | PIMENTEIRAS | PIAUÍ | Brasil | 2208106 | 22 | 33 | nan | nan | nan | Caatinga | 490.9 |
| 77e8358b-94c3-3eb7-9528-04d9b95fbfd4 | 1.6015 | -56.0415 | 2026-09-26 15:30:00 | GOES-19 | ORIXIMINÁ | PARÁ | Brasil | 1505304 | 15 | 33 | nan | nan | nan | Amazônia | 80.6 |
| a3b5c4b4-69d2-3181-afc0-83d49359ec43 | -11.8078 | -50.6499 | 2026-09-26 15:30:00 | GOES-19 | FORMOSO DO ARAGUAIA | TOCANTINS | Brasil | 1708205 | 17 | 33 | nan | nan | nan | Cerrado | 94.3 |
| 636b2ee2-7bef-3a95-b60c-01f003b9ac6d | -1.3008 | -49.0613 | 2026-09-26 15:30:00 | GOES-19 | PONTA DE PEDRAS | PARÁ | Brasil | 1505700 | 15 | 33 | nan | nan | nan | Amazônia | 72.4 |
| 90c34b72-1d71-3e8e-a561-14277599c69b | 1.1316 | -51.185 | 2026-09-26 15:30:00 | GOES-19 | TARTARUGALZINHO | AMAPÁ | Brasil | 1600709 | 16 | 33 | nan | nan | nan | Amazônia | 75.2 |
| 284427ce-2c61-37bf-b379-76ea433549a3 | -12.1027 | -50.0355 | 2026-09-26 15:30:00 | GOES-19 | SANDOLÂNDIA | TOCANTINS | Brasil | 1718840 | 17 | 33 | nan | nan | nan | Cerrado | 97.4 |
| 5f876675-ee73-3e2e-a883-678847ea43ac | -14.7676 | -45.5922 | 2026-09-26 15:30:00 | GOES-19 | COCOS | BAHIA | Brasil | 2908101 | 29 | 33 | nan | nan | nan | Cerrado | 116.8 |
| effa6eb7-62af-315d-b615-bcdab63e0ad9 | -6.221 | -41.641 | 2026-09-26 15:30:00 | GOES-19 | PIMENTEIRAS | PIAUÍ | Brasil | 2208106 | 22 | 33 | nan | nan | nan | Caatinga | 118.0 |
| 7aa38a01-421a-319a-bbcf-75e448261a0b | -13.2253 | -51.5466 | 2026-09-26 15:30:00 | GOES-19 | RIBEIRÃO CASCALHEIRA | MATO GROSSO | Brasil | 5107180 | 51 | 33 | nan | nan | nan | Cerrado | 81.0 |
| 28acc522-d4a1-3acf-bcda-8ff477c58c61 | -0.8215 | -48.6609 | 2026-09-26 15:30:00 | GOES-19 | SALVATERRA | PARÁ | Brasil | 1506302 | 15 | 33 | nan | nan | nan | Amazônia | 66.2 |
| d1155f17-2ebe-3cc4-a5ba-d414088b1ec0 | -12.1115 | -50.7001 | 2026-09-26 15:30:00 | GOES-19 | NOVO SANTO ANTÔNIO | MATO GROSSO | Brasil | 5106315 | 51 | 33 | nan | nan | nan | Cerrado | 93.9 |
| 6515f462-4f58-3ee8-8b2e-de7b79591837 | -12.2445 | -50.7271 | 2026-09-26 15:30:00 | GOES-19 | NOVO SANTO ANTÔNIO | MATO GROSSO | Brasil | 5106315 | 51 | 33 | nan | nan | nan | Cerrado | 113.9 |
| 5ff99f6d-305a-3a3a-b3dd-6582f460209e | -12.0921 | -50.7237 | 2026-09-26 15:30:00 | GOES-19 | NOVO SANTO ANTÔNIO | MATO GROSSO | Brasil | 5106315 | 51 | 33 | nan | nan | nan | Cerrado | 98.0 |
| 5171e423-798c-3b9d-a207-3e43aa664120 | -10.4046 | -53.803 | 2026-09-26 15:30:00 | GOES-19 | PEIXOTO DE AZEVEDO | MATO GROSSO | Brasil | 5106422 | 51 | 33 | nan | nan | nan | Amazônia | 74.0 |
| e38b7abf-1436-3611-b718-59ea132d9a62 | -12.1303 | -50.7192 | 2026-09-26 15:30:00 | GOES-19 | NOVO SANTO ANTÔNIO | MATO GROSSO | Brasil | 5106315 | 51 | 33 | nan | nan | nan | Cerrado | 121.1 |
| 7ba9936d-5adb-335c-8bf8-e7f997fb48b8 | 1.5832 | -56.0417 | 2026-09-26 15:30:00 | GOES-19 | ORIXIMINÁ | PARÁ | Brasil | 1505304 | 15 | 33 | nan | nan | nan | Amazônia | 76.5 |
| fe580672-64e5-3b61-90ec-87e0819d43ea | -1.9489 | -56.3319 | 2026-09-26 15:30:00 | GOES-19 | TERRA SANTA | PARÁ | Brasil | 1507979 | 15 | 33 | nan | nan | nan | Amazônia | 53.7 |
| 8621cb10-8ed1-38a0-adb8-2aa48b3a727d | -11.3046 | -51.3222 | 2026-09-26 15:30:00 | GOES-19 | SÃO FÉLIX DO ARAGUAIA | MATO GROSSO | Brasil | 5107859 | 51 | 33 | nan | nan | nan | Cerrado | 111.2 |
| 1c3e2d3c-e01f-3bc4-9d14-b155a61df70d | -12.9457 | -51.0695 | 2026-09-26 15:30:00 | GOES-19 | COCALINHO | MATO GROSSO | Brasil | 5103106 | 51 | 33 | nan | nan | nan | Cerrado | 198.4 |


[Clique aqui para ver as próximas entradas](README38.md)
