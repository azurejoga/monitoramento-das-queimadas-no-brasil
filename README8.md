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

## Dados Diários - Página 8

| ID | Latitude | Longitude | Data/Hora GMT | Satélite | Município | Estado | País | Município ID | Estado ID | País ID | Dias sem Chuva | Precipitação | Risco de Fogo | Bioma | FRP |
|----|----------|-----------|---------------|----------|-----------|--------|------|--------------|-----------|---------|----------------|--------------|----------------|-------|-----|
| 27a17569-53b8-394d-b947-5df24ec41a17 | -4.54284 | -48.02391 | 2025-07-01 04:44:00 | NOAA-21 | RONDON DO PARÁ | PARÁ | Brasil | 1506187 | 15 | 33 | nan | nan | nan | Amazônia | 5.1 |
| b9ca59ec-bc98-337b-94ac-d70c4a3e81fe | -4.37269 | -48.0689 | 2025-07-01 04:44:00 | NOAA-21 | RONDON DO PARÁ | PARÁ | Brasil | 1506187 | 15 | 33 | nan | nan | nan | Amazônia | 0.9 |
| 25540775-f77a-36ab-8736-d4961b90502a | -4.31996 | -48.08489 | 2025-07-01 04:44:00 | NOAA-21 | RONDON DO PARÁ | PARÁ | Brasil | 1506187 | 15 | 33 | nan | nan | nan | Amazônia | 4.6 |
| 3b952872-4318-3bef-ae79-e9cf0b4d70e7 | -4.38298 | -41.91466 | 2025-07-01 04:44:00 | NOAA-21 | PIRIPIRI | PIAUÍ | Brasil | 2208403 | 22 | 33 | nan | nan | nan | Caatinga | 2.0 |
| 02d49c6b-b246-34d5-b596-aec09ccccb4f | -4.70883 | -48.43431 | 2025-07-01 04:44:00 | NOAA-21 | RONDON DO PARÁ | PARÁ | Brasil | 1506187 | 15 | 33 | nan | nan | nan | Amazônia | 0.7 |
| 65664a54-b7fc-3bcf-a3ce-01bd30bd2237 | -4.28728 | -48.05696 | 2025-07-01 04:44:00 | NOAA-21 | DOM ELISEU | PARÁ | Brasil | 1502939 | 15 | 33 | nan | nan | nan | Amazônia | 0.8 |
| c1dd9fdb-111c-345e-888a-ed8177babe02 | -3.20615 | -41.84253 | 2025-07-01 04:44:00 | NOAA-21 | BURITI DOS LOPES | PIAUÍ | Brasil | 2202000 | 22 | 33 | nan | nan | nan | Cerrado | 0.8 |
| d09ce35b-a944-3d5b-ad2f-9a9201443b38 | -4.37731 | -48.08559 | 2025-07-01 04:44:00 | NOAA-21 | RONDON DO PARÁ | PARÁ | Brasil | 1506187 | 15 | 33 | nan | nan | nan | Amazônia | 1.0 |
| 9aeb2ece-4392-3aa7-84bf-c9c614600ce8 | -4.31936 | -48.08882 | 2025-07-01 04:44:00 | NOAA-21 | RONDON DO PARÁ | PARÁ | Brasil | 1506187 | 15 | 33 | nan | nan | nan | Amazônia | 4.6 |
| 0bfa4320-0684-371d-a1ca-33762d6407fc | -2.9085 | -54.48862 | 2025-07-01 04:44:00 | NOAA-21 | MOJUÍ DOS CAMPOS | PARÁ | Brasil | 1504752 | 15 | 33 | nan | nan | nan | Amazônia | 1.7 |
| 50179a32-6ed9-3d49-a222-690960124d31 | 2.74957 | -60.37033 | 2025-07-01 04:44:00 | NOAA-21 | CANTÁ | RORAIMA | Brasil | 1400175 | 14 | 33 | nan | nan | nan | Amazônia | 1.3 |
| db922011-6f43-38cf-88de-4c35f23e3285 | -4.31704 | -48.08043 | 2025-07-01 04:44:00 | NOAA-21 | RONDON DO PARÁ | PARÁ | Brasil | 1506187 | 15 | 33 | nan | nan | nan | Amazônia | 5.5 |
| 5aeb2e62-a254-3a4f-b0a0-5e25469d14fe | -4.32407 | -48.08144 | 2025-07-01 04:44:00 | NOAA-21 | RONDON DO PARÁ | PARÁ | Brasil | 1506187 | 15 | 33 | nan | nan | nan | Amazônia | 1.3 |
| 0b4556be-b913-37bf-978a-a32baa9ca4ee | -4.17493 | -47.53307 | 2025-07-01 04:44:00 | NOAA-21 | DOM ELISEU | PARÁ | Brasil | 1502939 | 15 | 33 | nan | nan | nan | Amazônia | 0.7 |
| 4d7fc1b1-8f2c-3550-bd00-93a6a1a295cf | -4.54344 | -48.01995 | 2025-07-01 04:44:00 | NOAA-21 | RONDON DO PARÁ | PARÁ | Brasil | 1506187 | 15 | 33 | nan | nan | nan | Amazônia | 5.1 |
| 649bc939-b3c5-3674-8025-3b3e4fad835d | -3.99505 | -43.24282 | 2025-07-01 04:44:00 | NOAA-21 | CHAPADINHA | MARANHÃO | Brasil | 2103208 | 21 | 33 | nan | nan | nan | Cerrado | 2.7 |
| 07506ed8-861f-3d3b-b5eb-c5db00b45640 | -4.37379 | -48.08508 | 2025-07-01 04:44:00 | NOAA-21 | RONDON DO PARÁ | PARÁ | Brasil | 1506187 | 15 | 33 | nan | nan | nan | Amazônia | 1.8 |
| 8bfc8e62-4c2e-3211-b35d-4e2f70273e86 | -4.25551 | -47.58352 | 2025-07-01 04:44:00 | NOAA-21 | DOM ELISEU | PARÁ | Brasil | 1502939 | 15 | 33 | nan | nan | nan | Amazônia | 1.3 |
| c95eedc0-0012-3a45-86c0-3af812caec1b | -3.21128 | -41.8434 | 2025-07-01 04:44:00 | NOAA-21 | BURITI DOS LOPES | PIAUÍ | Brasil | 2202000 | 22 | 33 | nan | nan | nan | Cerrado | 0.8 |
| 0690122e-5edf-394c-ad27-ead4b501b602 | -4.38322 | -48.07051 | 2025-07-01 04:44:00 | NOAA-21 | RONDON DO PARÁ | PARÁ | Brasil | 1506187 | 15 | 33 | nan | nan | nan | Amazônia | 0.9 |
| 4c13b51e-9405-3bf6-9616-ec4b79abccfd | 2.74888 | -60.36562 | 2025-07-01 04:44:00 | NOAA-21 | CANTÁ | RORAIMA | Brasil | 1400175 | 14 | 33 | nan | nan | nan | Amazônia | 1.3 |
| a0ef2f76-54cd-33a2-88c8-db358097acf0 | -4.55229 | -48.00914 | 2025-07-01 04:44:00 | NOAA-21 | RONDON DO PARÁ | PARÁ | Brasil | 1506187 | 15 | 33 | nan | nan | nan | Amazônia | 1.3 |
| 89b45652-6819-3a1e-bd3b-74dc41e2a9c9 | -4.32347 | -48.08539 | 2025-07-01 04:44:00 | NOAA-21 | RONDON DO PARÁ | PARÁ | Brasil | 1506187 | 15 | 33 | nan | nan | nan | Amazônia | 4.6 |
| 9b036791-0d93-3807-afb2-661bc038efa4 | -4.53991 | -48.0194 | 2025-07-01 04:44:00 | NOAA-21 | RONDON DO PARÁ | PARÁ | Brasil | 1506187 | 15 | 33 | nan | nan | nan | Amazônia | 5.1 |
| f56a46b9-c691-36b8-8fc1-1c410d98f8d6 | -4.28468 | -48.36426 | 2025-07-01 04:44:00 | NOAA-21 | RONDON DO PARÁ | PARÁ | Brasil | 1506187 | 15 | 33 | nan | nan | nan | Amazônia | 1.8 |
| 1e69403a-194d-331d-83e3-d1fd1a2da7cb | -9.23185 | -58.74081 | 2025-07-01 04:46:00 | NOAA-21 | COTRIGUAÇU | MATO GROSSO | Brasil | 5103379 | 51 | 33 | nan | nan | nan | Amazônia | 0.9 |
| caa1b54e-7165-38e6-a7d9-7e75327553c7 | -9.25664 | -58.75961 | 2025-07-01 04:46:00 | NOAA-21 | COTRIGUAÇU | MATO GROSSO | Brasil | 5103379 | 51 | 33 | nan | nan | nan | Amazônia | 3.6 |
| 6c215b95-a1df-3af8-bf41-eabbcd46e3f2 | -10.16025 | -53.92287 | 2025-07-01 04:46:00 | NOAA-21 | PEIXOTO DE AZEVEDO | MATO GROSSO | Brasil | 5106422 | 51 | 33 | nan | nan | nan | Amazônia | 0.5 |
| 4353d66a-b2d6-391f-bbe5-563215fcf584 | -9.12343 | -48.7607 | 2025-07-01 04:46:00 | NOAA-21 | COLMÉIA | TOCANTINS | Brasil | 1716703 | 17 | 33 | nan | nan | nan | Amazônia | 1.6 |
| 6ec9e630-26db-3cb0-8208-54efca76ff1e | -10.30502 | -57.13676 | 2025-07-01 04:46:00 | NOAA-21 | NOVA MONTE VERDE | MATO GROSSO | Brasil | 5108956 | 51 | 33 | nan | nan | nan | Amazônia | 4.1 |
| 8a1572cd-c28c-3bd9-af1c-cbc56ac9d25a | -6.48435 | -43.74447 | 2025-07-01 04:46:00 | NOAA-21 | SÃO JOÃO DOS PATOS | MARANHÃO | Brasil | 2111102 | 21 | 33 | nan | nan | nan | Cerrado | 2.8 |
| 0bdb02ca-ae67-3ba6-a4a1-52d1063d35c6 | -7.2906 | -45.37753 | 2025-07-01 04:46:00 | NOAA-21 | LORETO | MARANHÃO | Brasil | 2106102 | 21 | 33 | nan | nan | nan | Cerrado | 1.5 |
| 38759998-2810-3811-8533-6d62716fe0bb | -10.50978 | -49.78267 | 2025-07-01 04:46:00 | NOAA-21 | PIUM | TOCANTINS | Brasil | 1717503 | 17 | 33 | nan | nan | nan | Cerrado | 1.3 |
| 23ef2047-9b08-388f-a6cf-d5f6c36f20b3 | -11.02593 | -56.26252 | 2025-07-01 04:46:00 | NOAA-21 | NOVA CANAÃ DO NORTE | MATO GROSSO | Brasil | 5106216 | 51 | 33 | nan | nan | nan | Amazônia | 2.7 |
| d7974a43-82e7-353b-8d72-ec72cabd88a7 | -10.13041 | -52.34535 | 2025-07-01 04:46:00 | NOAA-21 | SANTA CRUZ DO XINGU | MATO GROSSO | Brasil | 5107743 | 51 | 33 | nan | nan | nan | Amazônia | 2.0 |
| 53f561e4-b99b-3e55-b9c3-f697c8dc702f | -10.8736 | -53.76973 | 2025-07-01 04:46:00 | NOAA-21 | MARCELÂNDIA | MATO GROSSO | Brasil | 5105580 | 51 | 33 | nan | nan | nan | Amazônia | 1.0 |
| 76622505-1d66-352b-a7d3-69f8465a07ff | -10.87538 | -53.75872 | 2025-07-01 04:46:00 | NOAA-21 | MARCELÂNDIA | MATO GROSSO | Brasil | 5105580 | 51 | 33 | nan | nan | nan | Amazônia | 1.3 |
| 74afc1e0-95c5-3ceb-ac57-fe92b5d7014a | -10.37431 | -51.78825 | 2025-07-01 04:46:00 | NOAA-21 | CONFRESA | MATO GROSSO | Brasil | 5103353 | 51 | 33 | nan | nan | nan | Amazônia | 1.2 |
| 3b2841c8-4738-30bf-af22-62bd8777e65f | -9.23844 | -58.75648 | 2025-07-01 04:46:00 | NOAA-21 | COTRIGUAÇU | MATO GROSSO | Brasil | 5103379 | 51 | 33 | nan | nan | nan | Amazônia | 1.2 |
| ae0c11fe-a88d-34bf-bbfb-c7cf366f19ae | -9.97703 | -48.24252 | 2025-07-01 04:46:00 | NOAA-21 | PALMAS | TOCANTINS | Brasil | 1721000 | 17 | 33 | nan | nan | nan | Cerrado | 3.8 |
| d14bef59-38ca-30b8-bec0-09e1bde28ed7 | -10.09229 | -52.73777 | 2025-07-01 04:46:00 | NOAA-21 | SANTA CRUZ DO XINGU | MATO GROSSO | Brasil | 5107743 | 51 | 33 | nan | nan | nan | Amazônia | 3.1 |
| 97340c76-9aab-3efc-bfc9-3df35860207e | -10.67899 | -49.15117 | 2025-07-01 04:46:00 | NOAA-21 | CRISTALÂNDIA | TOCANTINS | Brasil | 1706100 | 17 | 33 | nan | nan | nan | Cerrado | 1.2 |
| 807d68ab-4484-3aaa-b1bb-4dfa9746cb5f | -10.50665 | -53.57881 | 2025-07-01 04:46:00 | NOAA-21 | PEIXOTO DE AZEVEDO | MATO GROSSO | Brasil | 5106422 | 51 | 33 | nan | nan | nan | Amazônia | 1.4 |
| 081a7b5b-d07e-3ce7-ab77-c5b558b79fac | -9.24094 | -58.74237 | 2025-07-01 04:46:00 | NOAA-21 | COTRIGUAÇU | MATO GROSSO | Brasil | 5103379 | 51 | 33 | nan | nan | nan | Amazônia | 2.2 |
| ee0b4f47-e821-3563-8d11-6c4d7759dbbd | -9.13112 | -50.00292 | 2025-07-01 04:46:00 | NOAA-21 | SANTANA DO ARAGUAIA | PARÁ | Brasil | 1506708 | 15 | 33 | nan | nan | nan | Amazônia | 0.9 |
| 728af9e3-1085-3309-b0c6-90b5190205ea | -6.57275 | -47.37065 | 2025-07-01 04:46:00 | NOAA-21 | ESTREITO | MARANHÃO | Brasil | 2104057 | 21 | 33 | nan | nan | nan | Cerrado | 8.3 |
| 717a74de-946a-3e64-88c2-66f6fd20e571 | -10.36453 | -47.96991 | 2025-07-01 04:46:00 | NOAA-21 | MONTE DO CARMO | TOCANTINS | Brasil | 1713601 | 17 | 33 | nan | nan | nan | Cerrado | 2.0 |
| 2cbef14f-5468-3fe3-ae4d-288123f6810d | -9.1108 | -59.05244 | 2025-07-01 04:46:00 | NOAA-21 | COLNIZA | MATO GROSSO | Brasil | 5103254 | 51 | 33 | nan | nan | nan | Amazônia | 2.0 |
| e54f5ec2-0346-3aeb-9dac-214b5bb0d4be | -10.27794 | -52.83327 | 2025-07-01 04:46:00 | NOAA-21 | SANTA CRUZ DO XINGU | MATO GROSSO | Brasil | 5107743 | 51 | 33 | nan | nan | nan | Amazônia | 3.0 |
| 0ed7d677-cc09-308b-941a-0f72f4d189dc | -7.71972 | -47.85002 | 2025-07-01 04:46:00 | NOAA-21 | FILADÉLFIA | TOCANTINS | Brasil | 1707702 | 17 | 33 | nan | nan | nan | Cerrado | 1.3 |
| f5dbe2ae-a0e4-37ac-892a-06cad76563d1 | -10.07242 | -49.65982 | 2025-07-01 04:46:00 | NOAA-21 | PIUM | TOCANTINS | Brasil | 1717503 | 17 | 33 | nan | nan | nan | Cerrado | 2.4 |
| ce43c5e7-da5d-3061-bce3-e039f04181f3 | -9.68633 | -48.34019 | 2025-07-01 04:46:00 | NOAA-21 | TOCANTÍNIA | TOCANTINS | Brasil | 1721109 | 17 | 33 | nan | nan | nan | Cerrado | 1.6 |
| a54dff6e-b3a1-3802-aea0-5f273c24f68d | -10.86753 | -54.30469 | 2025-07-01 04:46:00 | NOAA-21 | MARCELÂNDIA | MATO GROSSO | Brasil | 5105580 | 51 | 33 | nan | nan | nan | Amazônia | 0.4 |
| 99c2f551-6fd8-3317-abdd-a813962f51bf | -9.12744 | -49.67782 | 2025-07-01 04:46:00 | NOAA-21 | ARAGUACEMA | TOCANTINS | Brasil | 1701903 | 17 | 33 | nan | nan | nan | Cerrado | 2.0 |
| ab757859-690c-3dd8-8c0c-c2397378eb62 | -6.47955 | -43.74422 | 2025-07-01 04:46:00 | NOAA-21 | SÃO JOÃO DOS PATOS | MARANHÃO | Brasil | 2111102 | 21 | 33 | nan | nan | nan | Cerrado | 29.4 |
| 93f82107-a55f-38ad-b765-a1971d5186c4 | -9.25043 | -50.25422 | 2025-07-01 04:46:00 | NOAA-21 | SANTANA DO ARAGUAIA | PARÁ | Brasil | 1506708 | 15 | 33 | nan | nan | nan | Amazônia | 1.3 |
| ff0b90fa-eeda-3d17-92e1-a1f854d3a836 | -7.24881 | -46.39827 | 2025-07-01 04:46:00 | NOAA-21 | RIACHÃO | MARANHÃO | Brasil | 2109502 | 21 | 33 | nan | nan | nan | Cerrado | 2.1 |
| 39bf4038-1aef-3dc8-b2be-0d55cc6eb193 | -6.29761 | -43.6792 | 2025-07-01 04:46:00 | NOAA-21 | PASSAGEM FRANCA | MARANHÃO | Brasil | 2107902 | 21 | 33 | nan | nan | nan | Cerrado | 3.4 |
| 98fe6633-bd28-3044-af66-cdcb03dada0a | -10.8855 | -53.76041 | 2025-07-01 04:46:00 | NOAA-21 | MARCELÂNDIA | MATO GROSSO | Brasil | 5105580 | 51 | 33 | nan | nan | nan | Amazônia | 1.8 |
| a65e6838-1e43-3974-bd94-0b5b9fb6f337 | -10.87905 | -56.44225 | 2025-07-01 04:46:00 | NOAA-21 | NOVA CANAÃ DO NORTE | MATO GROSSO | Brasil | 5106216 | 51 | 33 | nan | nan | nan | Amazônia | 6.2 |
| 921ecd16-ce59-33cc-8be6-2e2a7d3ff056 | -10.87816 | -53.76295 | 2025-07-01 04:46:00 | NOAA-21 | MARCELÂNDIA | MATO GROSSO | Brasil | 5105580 | 51 | 33 | nan | nan | nan | Amazônia | 2.2 |
| 4a06f8c9-f966-3066-8194-512f5cd2ad22 | -10.87976 | -53.77453 | 2025-07-01 04:46:00 | NOAA-21 | MARCELÂNDIA | MATO GROSSO | Brasil | 5105580 | 51 | 33 | nan | nan | nan | Amazônia | 1.0 |
| cee0399a-137d-3c9f-91d8-a90f20aa89cc | -10.08122 | -52.74321 | 2025-07-01 04:46:00 | NOAA-21 | SANTA CRUZ DO XINGU | MATO GROSSO | Brasil | 5107743 | 51 | 33 | nan | nan | nan | Amazônia | 6.2 |
| f7869754-f750-3452-ab2f-7bac19500d52 | -11.5773 | -48.14059 | 2025-07-01 04:46:00 | NOAA-21 | SANTA ROSA DO TOCANTINS | TOCANTINS | Brasil | 1718907 | 17 | 33 | nan | nan | nan | Cerrado | 2.0 |
| 92f82dcc-2786-37a1-b47c-f15942c014d3 | -9.24177 | -58.73774 | 2025-07-01 04:46:00 | NOAA-21 | COTRIGUAÇU | MATO GROSSO | Brasil | 5103379 | 51 | 33 | nan | nan | nan | Amazônia | 1.3 |
| eba17c73-be76-31c1-b1fa-431e6718b365 | -10.87141 | -53.76182 | 2025-07-01 04:46:00 | NOAA-21 | MARCELÂNDIA | MATO GROSSO | Brasil | 5105580 | 51 | 33 | nan | nan | nan | Amazônia | 0.7 |
| 76cad080-a7b5-3745-b60b-85fed365ab29 | -9.2521 | -58.75878 | 2025-07-01 04:46:00 | NOAA-21 | COTRIGUAÇU | MATO GROSSO | Brasil | 5103379 | 51 | 33 | nan | nan | nan | Amazônia | 3.1 |
| 5c313f07-04b8-336c-ad1a-a346fdd864b2 | -11.12823 | -55.44928 | 2025-07-01 04:46:00 | NOAA-21 | ITAÚBA | MATO GROSSO | Brasil | 5104559 | 51 | 33 | nan | nan | nan | Amazônia | 1.4 |
| 75ab48ba-5341-338a-b872-9a30f7994058 | -9.70464 | -56.18727 | 2025-07-01 04:46:00 | NOAA-21 | ALTA FLORESTA | MATO GROSSO | Brasil | 5100250 | 51 | 33 | nan | nan | nan | Amazônia | 12.4 |
| 4b31c1ba-f1d2-35b8-9f02-10ae2f8077ff | -6.56834 | -47.37457 | 2025-07-01 04:46:00 | NOAA-21 | ESTREITO | MARANHÃO | Brasil | 2104057 | 21 | 33 | nan | nan | nan | Cerrado | 2.0 |
| 4397d780-f8ef-391b-b579-3ac94b426ae6 | -10.29883 | -57.12474 | 2025-07-01 04:46:00 | NOAA-21 | NOVA MONTE VERDE | MATO GROSSO | Brasil | 5108956 | 51 | 33 | nan | nan | nan | Amazônia | 0.8 |
| 06e491dd-fae5-3257-8876-288e3617b895 | -9.97834 | -48.23345 | 2025-07-01 04:46:00 | NOAA-21 | PALMAS | TOCANTINS | Brasil | 1721000 | 17 | 33 | nan | nan | nan | Cerrado | 4.5 |
| 08e551ba-f08b-3f63-b541-cf863b288506 | -8.33613 | -55.0956 | 2025-07-01 04:46:00 | NOAA-21 | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 0.9 |
| fb497230-e88d-3b18-9752-2e134b33332b | -10.17383 | -51.65589 | 2025-07-01 04:46:00 | NOAA-21 | CONFRESA | MATO GROSSO | Brasil | 5103353 | 51 | 33 | nan | nan | nan | Amazônia | 0.7 |
| 2aab962a-c16a-3c69-9246-1115c249e575 | -7.164 | -49.51548 | 2025-07-01 04:46:00 | NOAA-21 | RIO MARIA | PARÁ | Brasil | 1506161 | 15 | 33 | nan | nan | nan | Amazônia | 0.8 |
| f642641c-45a8-38d5-a794-8c4282f2be93 | -9.68614 | -48.33804 | 2025-07-01 04:46:00 | NOAA-21 | TOCANTÍNIA | TOCANTINS | Brasil | 1721109 | 17 | 33 | nan | nan | nan | Cerrado | 2.9 |
| b322cac6-385c-3d85-af20-fa35020c1e29 | -9.19473 | -49.69519 | 2025-07-01 04:46:00 | NOAA-21 | ABREULÂNDIA | TOCANTINS | Brasil | 1700251 | 17 | 33 | nan | nan | nan | Cerrado | 1.2 |
| 1d427c12-06e4-3ea9-99c6-9011ba38ad41 | -7.09821 | -49.16223 | 2025-07-01 04:46:00 | NOAA-21 | SANTA FÉ DO ARAGUAIA | TOCANTINS | Brasil | 1718865 | 17 | 33 | nan | nan | nan | Amazônia | 0.7 |
| 2b5ca5c2-329c-33cc-af38-3cfbb6967a94 | -10.87825 | -56.44701 | 2025-07-01 04:46:00 | NOAA-21 | NOVA CANAÃ DO NORTE | MATO GROSSO | Brasil | 5106216 | 51 | 33 | nan | nan | nan | Amazônia | 6.2 |
| c014eab0-9293-3e07-ac96-b180de6b4f6e | -12.02085 | -47.77094 | 2025-07-01 04:46:00 | NOAA-21 | NATIVIDADE | TOCANTINS | Brasil | 1714203 | 17 | 33 | nan | nan | nan | Cerrado | 7.2 |
| 75f544dc-07f1-3447-b340-986159709548 | -10.13096 | -52.34186 | 2025-07-01 04:46:00 | NOAA-21 | SANTA CRUZ DO XINGU | MATO GROSSO | Brasil | 5107743 | 51 | 33 | nan | nan | nan | Amazônia | 2.0 |
| 8735c7a0-8b19-3447-ad6b-2a5212f42bb0 | -10.87994 | -53.75194 | 2025-07-01 04:46:00 | NOAA-21 | MARCELÂNDIA | MATO GROSSO | Brasil | 5105580 | 51 | 33 | nan | nan | nan | Amazônia | 1.5 |
| 220d0137-091b-3e99-9f47-e75a121d0bc9 | -9.18339 | -48.84339 | 2025-07-01 04:46:00 | NOAA-21 | DOIS IRMÃOS DO TOCANTINS | TOCANTINS | Brasil | 1707207 | 17 | 33 | nan | nan | nan | Cerrado | 1.3 |
| 5719e392-2684-3d8d-9044-378a618d8aca | -6.57092 | -47.36783 | 2025-07-01 04:46:00 | NOAA-21 | ESTREITO | MARANHÃO | Brasil | 2104057 | 21 | 33 | nan | nan | nan | Cerrado | 5.3 |
| 6263fad8-cff6-3378-82a2-e57c4d79d4d9 | -9.08497 | -59.47869 | 2025-07-01 04:46:00 | NOAA-21 | COLNIZA | MATO GROSSO | Brasil | 5103254 | 51 | 33 | nan | nan | nan | Amazônia | 1.7 |
| 5f5754d1-14f5-3596-bfaa-4c36fa2c1eae | -10.67482 | -49.15473 | 2025-07-01 04:46:00 | NOAA-21 | CRISTALÂNDIA | TOCANTINS | Brasil | 1706100 | 17 | 33 | nan | nan | nan | Cerrado | 1.9 |
| fd75d300-028d-3db0-a092-14a7c1459be9 | -9.2364 | -58.74158 | 2025-07-01 04:46:00 | NOAA-21 | COTRIGUAÇU | MATO GROSSO | Brasil | 5103379 | 51 | 33 | nan | nan | nan | Amazônia | 0.9 |
| 995c7972-ea06-34be-b881-c2229e5488d6 | -9.97027 | -48.23683 | 2025-07-01 04:46:00 | NOAA-21 | PALMAS | TOCANTINS | Brasil | 1721000 | 17 | 33 | nan | nan | nan | Cerrado | 13.3 |
| feb34d22-c6bf-3274-ab0f-e905169cfee4 | -8.70073 | -48.22572 | 2025-07-01 04:46:00 | NOAA-21 | GUARAÍ | TOCANTINS | Brasil | 1709302 | 17 | 33 | nan | nan | nan | Cerrado | 1.6 |
| 7c54bc55-0a90-3853-810e-0fd6cd360989 | -11.07517 | -55.38036 | 2025-07-01 04:46:00 | NOAA-21 | ITAÚBA | MATO GROSSO | Brasil | 5104559 | 51 | 33 | nan | nan | nan | Amazônia | 4.2 |
| 39f26162-6c53-3a4a-bfd6-716d9a565aa4 | -7.09764 | -49.166 | 2025-07-01 04:46:00 | NOAA-21 | SANTA FÉ DO ARAGUAIA | TOCANTINS | Brasil | 1718865 | 17 | 33 | nan | nan | nan | Amazônia | 2.3 |
| 8d215fec-f5fe-3238-a43f-6385f90dbe6b | -10.67542 | -49.15062 | 2025-07-01 04:46:00 | NOAA-21 | CRISTALÂNDIA | TOCANTINS | Brasil | 1706100 | 17 | 33 | nan | nan | nan | Cerrado | 1.2 |
| 9e2c5e9f-678b-32df-9851-1ef699a64af4 | -6.17373 | -47.27541 | 2025-07-01 04:46:00 | NOAA-21 | CAMPESTRE DO MARANHÃO | MARANHÃO | Brasil | 2102556 | 21 | 33 | nan | nan | nan | Cerrado | 0.8 |
| 3e254ef9-9af7-34bc-ac07-d524933bfcfa | -8.67273 | -51.46735 | 2025-07-01 04:46:00 | NOAA-21 | CUMARU DO NORTE | PARÁ | Brasil | 1502764 | 15 | 33 | nan | nan | nan | Amazônia | 1.3 |
| 9f63c27b-65be-3ae2-964a-f3ae6beecbd6 | -9.6576 | -50.74442 | 2025-07-01 04:46:00 | NOAA-21 | SANTANA DO ARAGUAIA | PARÁ | Brasil | 1506708 | 15 | 33 | nan | nan | nan | Amazônia | 3.9 |
| 81a93838-4949-3312-9e0f-4c72fbe83895 | -9.7169 | -56.18441 | 2025-07-01 04:46:00 | NOAA-21 | ALTA FLORESTA | MATO GROSSO | Brasil | 5100250 | 51 | 33 | nan | nan | nan | Amazônia | 2.5 |
| 037c1496-e5a8-3957-b522-863995e26d82 | -9.23928 | -58.75175 | 2025-07-01 04:46:00 | NOAA-21 | COTRIGUAÇU | MATO GROSSO | Brasil | 5103379 | 51 | 33 | nan | nan | nan | Amazônia | 1.2 |
| a7a072a8-3844-3f9c-a3ee-b5889eccbf9e | -6.21548 | -43.35812 | 2025-07-01 04:46:00 | NOAA-21 | LAGOA DO MATO | MARANHÃO | Brasil | 2105922 | 21 | 33 | nan | nan | nan | Cerrado | 7.5 |
| 81452f0c-21f5-397d-92b8-1528ae6a3451 | -7.66941 | -47.76347 | 2025-07-01 04:46:00 | NOAA-21 | FILADÉLFIA | TOCANTINS | Brasil | 1707702 | 17 | 33 | nan | nan | nan | Cerrado | 0.6 |
| dfb801e9-461e-3a6c-b986-e2a29a8a213d | -12.28365 | -50.10015 | 2025-07-01 04:46:00 | NOAA-21 | SANDOLÂNDIA | TOCANTINS | Brasil | 1718840 | 17 | 33 | nan | nan | nan | Cerrado | 1.3 |


[Clique aqui para ver as próximas entradas](README9.md)
