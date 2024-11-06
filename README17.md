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

## Dados Diários - Página 17

| ID | Latitude | Longitude | Data/Hora GMT | Satélite | Município | Estado | País | Município ID | Estado ID | País ID | Dias sem Chuva | Precipitação | Risco de Fogo | Bioma | FRP |
|----|----------|-----------|---------------|----------|-----------|--------|------|--------------|-----------|---------|----------------|--------------|----------------|-------|-----|
| 9014cfdc-457e-3632-9e62-6fa42d9f8bb4 | -4.1432 | -43.5822 | 2024-11-06 02:00:00 | GOES-16 | CHAPADINHA | MARANHÃO | Brasil | 2103208 | 21 | 33 | nan | nan | nan | Cerrado | 94.4 |
| c1483dd4-5777-3238-af3a-03b56d035b29 | -3.3285 | -50.0723 | 2024-11-06 02:00:00 | GOES-16 | PACAJÁ | PARÁ | Brasil | 1505486 | 15 | 33 | nan | nan | nan | Amazônia | 34.5 |
| 337fec34-6e8f-3456-9032-d373e2f7266f | -3.5305 | -50.3387 | 2024-11-06 02:00:00 | GOES-16 | PACAJÁ | PARÁ | Brasil | 1505486 | 15 | 33 | nan | nan | nan | Amazônia | 35.9 |
| a1aa7b98-4478-301b-83a2-745010435bb3 | -3.0609 | -47.7733 | 2024-11-06 02:00:00 | GOES-16 | PARAGOMINAS | PARÁ | Brasil | 1505502 | 15 | 33 | nan | nan | nan | Amazônia | 39.8 |
| 1a6ea1c8-d339-3332-a0bb-ade97321ab07 | -2.8065 | -51.4855 | 2024-11-06 02:00:00 | GOES-16 | ANAPU | PARÁ | Brasil | 1500859 | 15 | 33 | nan | nan | nan | Amazônia | 48.6 |
| a26e2b67-6ed0-35cd-82a9-b53a40015656 | -3.2054 | -53.2153 | 2024-11-06 02:00:00 | GOES-16 | MEDICILÂNDIA | PARÁ | Brasil | 1504455 | 15 | 33 | nan | nan | nan | Amazônia | 34.7 |
| 24e488c8-e34b-341a-b512-3a34b711c1fb | -4.1246 | -43.5833 | 2024-11-06 02:00:00 | GOES-16 | CHAPADINHA | MARANHÃO | Brasil | 2103208 | 21 | 33 | nan | nan | nan | Cerrado | 175.8 |
| 07191ae7-8c2e-3424-abc7-047c0436a747 | -6.4827 | -47.4827 | 2024-11-06 02:00:00 | GOES-16 | AGUIARNÓPOLIS | TOCANTINS | Brasil | 1700301 | 17 | 33 | nan | nan | nan | Cerrado | 170.3 |
| 6522cb36-a6e2-351c-8360-9f93230c2699 | -2.1947 | -46.5517 | 2024-11-06 02:00:00 | GOES-16 | CACHOEIRA DO PIRIÁ | PARÁ | Brasil | 1501956 | 15 | 33 | nan | nan | nan | Amazônia | 50.7 |
| e7a01412-900d-396a-aeac-2a3c07b6f76c | -3.0212 | -53.281 | 2024-11-06 02:00:00 | GOES-16 | MEDICILÂNDIA | PARÁ | Brasil | 1504455 | 15 | 33 | nan | nan | nan | Amazônia | 48.3 |
| ec03a878-c4aa-3901-afb2-3cfeff9a1434 | -6.1226 | -43.9809 | 2024-11-06 02:00:00 | GOES-16 | COLINAS | MARANHÃO | Brasil | 2103505 | 21 | 33 | nan | nan | nan | Cerrado | 123.4 |
| 12eb81e4-e2c0-3dab-be75-d6425cc438af | -2.8607 | -51.7937 | 2024-11-06 02:00:00 | GOES-16 | SENADOR JOSÉ PORFÍRIO | PARÁ | Brasil | 1507805 | 15 | 33 | nan | nan | nan | Amazônia | 92.8 |
| adc7c168-12a6-3e32-8be8-594a9effedd1 | 3.6184 | -51.3162 | 2024-11-06 02:00:00 | GOES-16 | OIAPOQUE | AMAPÁ | Brasil | 1600501 | 16 | 33 | nan | nan | nan | Amazônia | 82.3 |
| 9896574f-9ce3-334b-8cb0-6937e01d8995 | -2.8064 | -51.5061 | 2024-11-06 02:00:00 | GOES-16 | ANAPU | PARÁ | Brasil | 1500859 | 15 | 33 | nan | nan | nan | Amazônia | 36.6 |
| 23a66a4f-265b-394a-a30e-1d4bf9dba20d | -6.1039 | -43.9824 | 2024-11-06 02:00:00 | GOES-16 | COLINAS | MARANHÃO | Brasil | 2103505 | 21 | 33 | nan | nan | nan | Cerrado | 90.9 |
| 76f1a422-d47e-32cd-a3a1-4b02572eb70a | -2.9371 | -51.0465 | 2024-11-06 02:00:00 | GOES-16 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 100.7 |
| 0e95542e-e9d8-3cd2-a207-fb3613393ff7 | -2.8506 | -49.4744 | 2024-11-06 02:00:00 | GOES-16 | BAIÃO | PARÁ | Brasil | 1501204 | 15 | 33 | nan | nan | nan | Amazônia | 54.0 |
| 8bcdc141-a22f-3ea4-b5fe-39a6e11f99a4 | -3.0207 | -53.4227 | 2024-11-06 02:00:00 | GOES-16 | MEDICILÂNDIA | PARÁ | Brasil | 1504455 | 15 | 33 | nan | nan | nan | Amazônia | 88.6 |
| 25b009c2-d0fa-3154-82dc-811adaf204eb | -6.4909 | -44.6633 | 2024-11-06 02:00:00 | GOES-16 | MIRADOR | MARANHÃO | Brasil | 2106706 | 21 | 33 | nan | nan | nan | Cerrado | 63.4 |
| 8a8c7a5f-0f2d-3ce4-b195-17acab33cf34 | -2.81 | -52.94 | 2024-11-06 02:00:00 | MSG-03 | MEDICILÂNDIA | PARÁ | Brasil | 1504455 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| b705b76b-fde9-3c79-9866-ff9dc54109f7 | -3.56 | -47.4 | 2024-11-06 02:00:00 | MSG-03 | ULIANÓPOLIS | PARÁ | Brasil | 1508126 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| 7265dbf2-4170-362b-a7b9-fdcbf0a95a20 | -3.53 | -47.4 | 2024-11-06 02:00:00 | MSG-03 | ULIANÓPOLIS | PARÁ | Brasil | 1508126 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| 2bcfa006-9abd-3c13-8c36-383e880c0458 | -6.49 | -47.51 | 2024-11-06 02:00:00 | MSG-03 | AGUIARNÓPOLIS | TOCANTINS | Brasil | 1700301 | 17 | 33 | nan | nan | nan | Cerrado | nan |
| 6d0038ea-929a-34c1-9158-dbf93c9a3a1e | -3.1433 | -50.2044 | 2024-11-06 02:10:00 | GOES-16 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 36.6 |
| ce992f80-5d1a-312d-ac10-612bf5e85f8d | -2.8607 | -51.7937 | 2024-11-06 02:10:00 | GOES-16 | SENADOR JOSÉ PORFÍRIO | PARÁ | Brasil | 1507805 | 15 | 33 | nan | nan | nan | Amazônia | 92.5 |
| 561310c1-b971-3af5-b62e-1d87cd309517 | -3.2163 | -50.391 | 2024-11-06 02:10:00 | GOES-16 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 52.3 |
| 76b8af02-3953-3464-8f8d-190ae43bda55 | -3.0396 | -53.2805 | 2024-11-06 02:10:00 | GOES-16 | MEDICILÂNDIA | PARÁ | Brasil | 1504455 | 15 | 33 | nan | nan | nan | Amazônia | 84.4 |
| 07755c04-3df2-3f84-8185-4759ca8e16b7 | -3.1213 | -51.1036 | 2024-11-06 02:10:00 | GOES-16 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 54.7 |
| 2bf7c8f1-551d-364e-b1a6-825d77da004e | -3.2415 | -53.3967 | 2024-11-06 02:10:00 | GOES-16 | MEDICILÂNDIA | PARÁ | Brasil | 1504455 | 15 | 33 | nan | nan | nan | Amazônia | 49.3 |
| 5d8388b2-e42d-3921-a88f-2cf7c1735823 | -3.2348 | -50.3904 | 2024-11-06 02:10:00 | GOES-16 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 68.1 |
| fc05ae90-5853-3a3f-8d65-59ec34f53991 | -6.5094 | -44.6847 | 2024-11-06 02:10:00 | GOES-16 | MIRADOR | MARANHÃO | Brasil | 2106706 | 21 | 33 | nan | nan | nan | Cerrado | 125.9 |
| 7723c0da-2029-308f-b4a7-2b233e867be9 | -3.0207 | -53.443 | 2024-11-06 02:10:00 | GOES-16 | MEDICILÂNDIA | PARÁ | Brasil | 1504455 | 15 | 33 | nan | nan | nan | Amazônia | 76.5 |
| 30cfe3d6-61bb-3c10-b798-e0d10ac47226 | -2.8065 | -51.4855 | 2024-11-06 02:10:00 | GOES-16 | ANAPU | PARÁ | Brasil | 1500859 | 15 | 33 | nan | nan | nan | Amazônia | 39.3 |
| e86e0893-dc01-3f61-a6c7-4178c45abb91 | -3.5304 | -50.3597 | 2024-11-06 02:10:00 | GOES-16 | PACAJÁ | PARÁ | Brasil | 1505486 | 15 | 33 | nan | nan | nan | Amazônia | 34.7 |
| 9c4dfa23-da4e-3d55-b079-904e54793c43 | -3.2349 | -50.3695 | 2024-11-06 02:10:00 | GOES-16 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 61.9 |
| 86fbab6c-ae41-3605-9980-e7c9b3cb1638 | -6.1414 | -43.9794 | 2024-11-06 02:10:00 | GOES-16 | COLINAS | MARANHÃO | Brasil | 2103505 | 21 | 33 | nan | nan | nan | Cerrado | 70.8 |
| 52a47bd1-822f-3ccb-ba2c-9225ca2c9393 | -3.0213 | -53.2607 | 2024-11-06 02:10:00 | GOES-16 | MEDICILÂNDIA | PARÁ | Brasil | 1504455 | 15 | 33 | nan | nan | nan | Amazônia | 66.3 |
| 0cb427fd-f072-3a14-a691-4a1dd5c64add | -6.5096 | -44.6618 | 2024-11-06 02:10:00 | GOES-16 | MIRADOR | MARANHÃO | Brasil | 2106706 | 21 | 33 | nan | nan | nan | Cerrado | 66.9 |
| de521c20-b53c-3800-adec-6ef57c1b0144 | -3.0023 | -53.4232 | 2024-11-06 02:10:00 | GOES-16 | MEDICILÂNDIA | PARÁ | Brasil | 1504455 | 15 | 33 | nan | nan | nan | Amazônia | 70.8 |
| dbfa44d6-e045-354b-8b44-1c216b67c3f3 | -2.9185 | -51.0678 | 2024-11-06 02:10:00 | GOES-16 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 32.7 |
| 64d252ca-784f-3c93-87af-8a6f2f44f517 | -3.0607 | -52.5066 | 2024-11-06 02:10:00 | GOES-16 | BRASIL NOVO | PARÁ | Brasil | 1501725 | 15 | 33 | nan | nan | nan | Amazônia | 49.7 |
| c36fa4ba-5412-300f-98ef-b9ce889f0e7e | -2.8608 | -51.7524 | 2024-11-06 02:10:00 | GOES-16 | SENADOR JOSÉ PORFÍRIO | PARÁ | Brasil | 1507805 | 15 | 33 | nan | nan | nan | Amazônia | 62.1 |
| b4c22588-21ab-3918-b973-0ae302de8ff9 | -3.1802 | -50.2032 | 2024-11-06 02:10:00 | GOES-16 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 40.6 |
| 9a12f8dd-2575-3ed9-845f-670c835445eb | -2.9371 | -51.0465 | 2024-11-06 02:10:00 | GOES-16 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 77.5 |
| 044ff1cd-20aa-374b-b573-bc92c09f6b2a | -4.1246 | -43.5833 | 2024-11-06 02:10:00 | GOES-16 | CHAPADINHA | MARANHÃO | Brasil | 2103208 | 21 | 33 | nan | nan | nan | Cerrado | 176.7 |
| 1581c10d-0226-3fee-b0bb-d31fb3ff6425 | -2.8423 | -51.7735 | 2024-11-06 02:10:00 | GOES-16 | SENADOR JOSÉ PORFÍRIO | PARÁ | Brasil | 1507805 | 15 | 33 | nan | nan | nan | Amazônia | 109.5 |
| 05c6de60-82e0-3a24-9999-2be0289ad8b8 | -2.8608 | -51.7731 | 2024-11-06 02:10:00 | GOES-16 | SENADOR JOSÉ PORFÍRIO | PARÁ | Brasil | 1507805 | 15 | 33 | nan | nan | nan | Amazônia | 211.6 |
| 14ba3b32-7402-35c4-950e-d90f133bb564 | -3.0397 | -53.2603 | 2024-11-06 02:10:00 | GOES-16 | MEDICILÂNDIA | PARÁ | Brasil | 1504455 | 15 | 33 | nan | nan | nan | Amazônia | 92.0 |
| a814a165-4599-346a-9701-65e86a241b71 | -3.9669 | -48.1716 | 2024-11-06 02:10:00 | GOES-16 | DOM ELISEU | PARÁ | Brasil | 1502939 | 15 | 33 | nan | nan | nan | Amazônia | 42.3 |
| 6b279be1-41e4-33f0-a106-f97c244747e5 | -6.1041 | -43.9593 | 2024-11-06 02:10:00 | GOES-16 | COLINAS | MARANHÃO | Brasil | 2103505 | 21 | 33 | nan | nan | nan | Cerrado | 96.0 |
| a2e8fd0d-66f3-3a5e-9868-7132d80ee6cc | -6.1226 | -43.9809 | 2024-11-06 02:10:00 | GOES-16 | COLINAS | MARANHÃO | Brasil | 2103505 | 21 | 33 | nan | nan | nan | Cerrado | 134.4 |
| 924b64dd-3e12-33f0-bec8-c7251b5cc1ae | -2.8423 | -51.7942 | 2024-11-06 02:10:00 | GOES-16 | SENADOR JOSÉ PORFÍRIO | PARÁ | Brasil | 1507805 | 15 | 33 | nan | nan | nan | Amazônia | 65.9 |
| 6e29e922-1f5b-3e6e-8685-e4701531d963 | -1.2922 | -54.5585 | 2024-11-06 02:10:00 | GOES-16 | MONTE ALEGRE | PARÁ | Brasil | 1504802 | 15 | 33 | nan | nan | nan | Amazônia | 28.5 |
| c84fe871-e91e-3737-a7d3-557ec76e3f78 | -2.1746 | -53.7036 | 2024-11-06 02:10:00 | GOES-16 | PRAINHA | PARÁ | Brasil | 1506005 | 15 | 33 | nan | nan | nan | Amazônia | 39.9 |
| ae5b6c28-caea-3a3b-a943-ca1cf824192e | -2.8506 | -49.4744 | 2024-11-06 02:10:00 | GOES-16 | BAIÃO | PARÁ | Brasil | 1501204 | 15 | 33 | nan | nan | nan | Amazônia | 79.1 |
| c84f8c0b-33ae-3137-a6cc-025c64a29618 | -3.5305 | -50.3387 | 2024-11-06 02:10:00 | GOES-16 | PACAJÁ | PARÁ | Brasil | 1505486 | 15 | 33 | nan | nan | nan | Amazônia | 39.8 |
| 63765c71-ebf2-3913-8677-59d2ca016e0b | -2.7243 | -54.1552 | 2024-11-06 02:10:00 | GOES-16 | PRAINHA | PARÁ | Brasil | 1506005 | 15 | 33 | nan | nan | nan | Amazônia | 122.6 |
| 2e19c7e7-0312-3776-be53-d6640731b428 | -2.937 | -51.0673 | 2024-11-06 02:10:00 | GOES-16 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 49.8 |
| 3956cd11-dbb0-3cbf-abf4-c71fdacfb0e9 | -6.5012 | -47.5033 | 2024-11-06 02:10:00 | GOES-16 | AGUIARNÓPOLIS | TOCANTINS | Brasil | 1700301 | 17 | 33 | nan | nan | nan | Cerrado | 154.3 |
| c5a8a6a3-0459-3b71-98b9-8d8c98db0453 | -6.4906 | -44.6862 | 2024-11-06 02:10:00 | GOES-16 | MIRADOR | MARANHÃO | Brasil | 2106706 | 21 | 33 | nan | nan | nan | Cerrado | 93.3 |
| ab1ecf64-769f-3f31-a73d-1043c4880f50 | -3.2054 | -53.2153 | 2024-11-06 02:10:00 | GOES-16 | MEDICILÂNDIA | PARÁ | Brasil | 1504455 | 15 | 33 | nan | nan | nan | Amazônia | 47.7 |
| 27835d55-30a2-3623-bf68-3ac8a12499c8 | -3.1617 | -50.2038 | 2024-11-06 02:10:00 | GOES-16 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 112.5 |
| 9e7a90ef-fbdd-3efb-ab21-19a1c51ac3c5 | -2.6764 | -51.8189 | 2024-11-06 02:10:00 | GOES-16 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 60.6 |
| 1d457917-a1c8-3e48-bb9a-3a34e7c415d3 | -6.1229 | -43.9578 | 2024-11-06 02:10:00 | GOES-16 | COLINAS | MARANHÃO | Brasil | 2103505 | 21 | 33 | nan | nan | nan | Cerrado | 102.6 |
| 6e482ce3-1807-3276-b02d-45cb2f2a7a31 | -3.0023 | -53.4434 | 2024-11-06 02:10:00 | GOES-16 | MEDICILÂNDIA | PARÁ | Brasil | 1504455 | 15 | 33 | nan | nan | nan | Amazônia | 65.5 |
| 11634994-e1ea-32de-befc-ec31ee72cd06 | -2.8424 | -51.7529 | 2024-11-06 02:10:00 | GOES-16 | SENADOR JOSÉ PORFÍRIO | PARÁ | Brasil | 1507805 | 15 | 33 | nan | nan | nan | Amazônia | 41.3 |
| 42691cf7-92df-392d-9d55-a3c60d479afe | 3.6184 | -51.3162 | 2024-11-06 02:10:00 | GOES-16 | OIAPOQUE | AMAPÁ | Brasil | 1600501 | 16 | 33 | nan | nan | nan | Amazônia | 111.8 |
| a19a6ca7-85ed-3ee2-aa0d-456fd5355fc6 | -6.4827 | -47.4827 | 2024-11-06 02:10:00 | GOES-16 | AGUIARNÓPOLIS | TOCANTINS | Brasil | 1700301 | 17 | 33 | nan | nan | nan | Cerrado | 142.3 |
| 3fac9df5-64c6-3886-8a92-92f848247c91 | 3.6 | -51.3168 | 2024-11-06 02:10:00 | GOES-16 | OIAPOQUE | AMAPÁ | Brasil | 1600501 | 16 | 33 | nan | nan | nan | Amazônia | 108.9 |
| ea6883ec-c568-3cc3-8d91-bdf5b7276824 | -4.1432 | -43.5822 | 2024-11-06 02:10:00 | GOES-16 | CHAPADINHA | MARANHÃO | Brasil | 2103208 | 21 | 33 | nan | nan | nan | Cerrado | 94.3 |
| 6a8a1d17-26f8-3f35-8f38-f57839c72460 | -2.7244 | -54.1351 | 2024-11-06 02:10:00 | GOES-16 | PRAINHA | PARÁ | Brasil | 1506005 | 15 | 33 | nan | nan | nan | Amazônia | 67.7 |
| 4f7fd578-0212-36c8-81f9-fcf762eb65d0 | -3.1616 | -50.2248 | 2024-11-06 02:10:00 | GOES-16 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 53.0 |
| ade3a71b-a485-305b-850f-bcd22134d70d | -2.9186 | -51.047 | 2024-11-06 02:10:00 | GOES-16 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 87.4 |
| 3b200fd9-f92c-3c77-ab57-83910b7458d2 | -4.5614 | -48.0141 | 2024-11-06 02:10:00 | GOES-16 | RONDON DO PARÁ | PARÁ | Brasil | 1506187 | 15 | 33 | nan | nan | nan | Amazônia | 84.0 |
| fb62693c-f387-3c6e-bbc1-52efd071d275 | -2.658 | -51.8194 | 2024-11-06 02:10:00 | GOES-16 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 30.6 |
| a3c5d870-3a44-3135-ac23-a1a709191584 | -6.5014 | -47.4813 | 2024-11-06 02:10:00 | GOES-16 | AGUIARNÓPOLIS | TOCANTINS | Brasil | 1700301 | 17 | 33 | nan | nan | nan | Cerrado | 231.4 |
| d288e1e7-3153-3411-b614-268c8bd5bb5f | -3.1393 | -51.2069 | 2024-11-06 02:10:00 | GOES-16 | ANAPU | PARÁ | Brasil | 1500859 | 15 | 33 | nan | nan | nan | Amazônia | 52.1 |
| 4727fc68-a43b-3d8c-b802-3a7885ce67b0 | -3.2164 | -50.3701 | 2024-11-06 02:10:00 | GOES-16 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 49.5 |
| a26e3468-9e2a-3971-81c1-387ecedcabf1 | -6.4825 | -47.5046 | 2024-11-06 02:10:00 | GOES-16 | AGUIARNÓPOLIS | TOCANTINS | Brasil | 1700301 | 17 | 33 | nan | nan | nan | Cerrado | 99.1 |
| 4eb5ee46-d9d9-3f0f-9704-f1099b08d6cc | -3.0207 | -53.4227 | 2024-11-06 02:10:00 | GOES-16 | MEDICILÂNDIA | PARÁ | Brasil | 1504455 | 15 | 33 | nan | nan | nan | Amazônia | 78.9 |
| 6739b9a1-77a5-3fa8-a907-17aad5b84a50 | -4.1247 | -43.5601 | 2024-11-06 02:10:00 | GOES-16 | CHAPADINHA | MARANHÃO | Brasil | 2103208 | 21 | 33 | nan | nan | nan | Cerrado | 76.1 |
| 65fbfdd0-2e19-321f-b548-11ea2193ae78 | -3.3285 | -50.0723 | 2024-11-06 02:10:00 | GOES-16 | PACAJÁ | PARÁ | Brasil | 1505486 | 15 | 33 | nan | nan | nan | Amazônia | 38.5 |
| 2d557604-3e94-3535-98c3-80f4d6e74fe8 | -3.0609 | -47.7733 | 2024-11-06 02:10:00 | GOES-16 | PARAGOMINAS | PARÁ | Brasil | 1505502 | 15 | 33 | nan | nan | nan | Amazônia | 47.8 |
| 9614d13f-383c-3514-8bf2-bec9ace06453 | -6.1039 | -43.9824 | 2024-11-06 02:10:00 | GOES-16 | COLINAS | MARANHÃO | Brasil | 2103505 | 21 | 33 | nan | nan | nan | Cerrado | 71.3 |
| 6abc4954-1026-3dde-859a-9fcf6c64344b | -2.6764 | -51.8395 | 2024-11-06 02:10:00 | GOES-16 | SENADOR JOSÉ PORFÍRIO | PARÁ | Brasil | 1507805 | 15 | 33 | nan | nan | nan | Amazônia | 40.4 |
| 5f3623e9-b456-388b-976c-25e62f9b7dd1 | -3.967 | -48.15 | 2024-11-06 02:10:00 | GOES-16 | DOM ELISEU | PARÁ | Brasil | 1502939 | 15 | 33 | nan | nan | nan | Amazônia | 52.5 |
| 579c5ef7-8097-3f85-87b0-b635f6b8123e | -3.0212 | -53.281 | 2024-11-06 02:10:00 | GOES-16 | MEDICILÂNDIA | PARÁ | Brasil | 1504455 | 15 | 33 | nan | nan | nan | Amazônia | 55.0 |
| 3230f3f3-b5d0-378b-9ff4-49621fc5786d | -2.7243 | -54.1552 | 2024-11-06 02:20:00 | GOES-16 | PRAINHA | PARÁ | Brasil | 1506005 | 15 | 33 | nan | nan | nan | Amazônia | 83.6 |
| f4c5dfb0-93f3-32e8-b651-f2305327302f | -3.2415 | -53.3967 | 2024-11-06 02:20:00 | GOES-16 | MEDICILÂNDIA | PARÁ | Brasil | 1504455 | 15 | 33 | nan | nan | nan | Amazônia | 52.6 |
| 4304e8a2-aa6d-3e18-a4ba-b6c28904b69b | -3.1213 | -51.1036 | 2024-11-06 02:20:00 | GOES-16 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 59.4 |
| b14ed0ab-cd23-31c7-af91-a4132afe3396 | -1.2922 | -54.5784 | 2024-11-06 02:20:00 | GOES-16 | MONTE ALEGRE | PARÁ | Brasil | 1504802 | 15 | 33 | nan | nan | nan | Amazônia | 29.4 |
| f7c464fd-dee1-3921-9098-a543c844c34b | -2.8423 | -51.7735 | 2024-11-06 02:20:00 | GOES-16 | SENADOR JOSÉ PORFÍRIO | PARÁ | Brasil | 1507805 | 15 | 33 | nan | nan | nan | Amazônia | 148.3 |
| 6f9549ee-0a35-3af3-b20f-b5683315b256 | -3.1616 | -50.2248 | 2024-11-06 02:20:00 | GOES-16 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 49.7 |
| 040a0839-67e2-3399-937e-a809e6ea0a6d | -2.937 | -51.0673 | 2024-11-06 02:20:00 | GOES-16 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 34.6 |
| 4cd04cad-acc3-3d37-8b8c-5fbc1437553d | -6.1414 | -43.9794 | 2024-11-06 02:20:00 | GOES-16 | COLINAS | MARANHÃO | Brasil | 2103505 | 21 | 33 | nan | nan | nan | Cerrado | 87.0 |
| e35ef258-77da-3a26-8d62-c14d6f4961e1 | -2.7427 | -54.1548 | 2024-11-06 02:20:00 | GOES-16 | SANTARÉM | PARÁ | Brasil | 1506807 | 15 | 33 | nan | nan | nan | Amazônia | 35.4 |
| 80f62595-b7ee-372a-a364-032266315821 | -3.2349 | -50.3695 | 2024-11-06 02:20:00 | GOES-16 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 46.0 |
| 79d41d67-f8a5-3bf0-ab8e-3927514d0f9c | -4.5614 | -48.0141 | 2024-11-06 02:20:00 | GOES-16 | RONDON DO PARÁ | PARÁ | Brasil | 1506187 | 15 | 33 | nan | nan | nan | Amazônia | 70.2 |
| 6515f72e-4bfd-3550-b41a-8088460f6bad | -3.0794 | -47.7727 | 2024-11-06 02:20:00 | GOES-16 | PARAGOMINAS | PARÁ | Brasil | 1505502 | 15 | 33 | nan | nan | nan | Amazônia | 50.4 |
| dedecb5d-2fcc-3914-bf74-2b1f61ada9be | -2.7244 | -54.1351 | 2024-11-06 02:20:00 | GOES-16 | PRAINHA | PARÁ | Brasil | 1506005 | 15 | 33 | nan | nan | nan | Amazônia | 52.0 |


[Clique aqui para ver as próximas entradas](README18.md)
